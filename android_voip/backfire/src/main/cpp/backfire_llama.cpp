// JNI bridge: Nemotron 3 Nano 4B (Q4_K_M GGUF) on the phone via llama.cpp. Backfire's on-device "Is this a scam?" check.
//
// Built for speed on phone CPUs. Nemotron-H is a hybrid Mamba model (~80 MB of recurrent state), so nothing is ever
// serialized or re-evaluated:
//  - seq 2 holds the system prompt (evaluated once at load); a new call copies it to seq 0 inside the engine.
//  - seq 0 is the live transcript: each caller utterance is decoded once, appended in place.
//  - a check copies seq 0 -> seq 1 (in-engine copy), decodes the ~20-token question on seq 1, reads ONE set of logits,
//    returns P(yes) from the yes/no tokens, and drops seq 1. No sampling loop, no JSON.
#include <jni.h>
#include <android/log.h>
#include <algorithm>
#include <chrono>
#include <cmath>
#include <mutex>
#include <string>
#include <vector>
#include "llama.h"

#define TAG "BackfireLlama"
#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, TAG, __VA_ARGS__)
#define LOGE(...) __android_log_print(ANDROID_LOG_ERROR, TAG, __VA_ARGS__)

namespace {
constexpr llama_seq_id LIVE = 0, ASK = 1, PREFIX = 2;

struct Engine {
    llama_model *model = nullptr;
    llama_context *ctx = nullptr;
    const llama_vocab *vocab = nullptr;
    std::vector<llama_token> yes_ids, no_ids;
    int n_batch = 512;
    std::mutex mu;
    llama_memory_t mem() const { return llama_get_memory(ctx); }
};

std::string jstr(JNIEnv *env, jstring s) {
    if (!s) return {};
    const char *c = env->GetStringUTFChars(s, nullptr);
    std::string out(c);
    env->ReleaseStringUTFChars(s, c);
    return out;
}

std::vector<llama_token> tokenize(const llama_vocab *vocab, const std::string &text, bool add_bos) {
    int n = -llama_tokenize(vocab, text.c_str(), (int32_t) text.size(), nullptr, 0, add_bos, true);
    if (n <= 0) return {};
    std::vector<llama_token> toks(n);
    llama_tokenize(vocab, text.c_str(), (int32_t) text.size(), toks.data(), n, add_bos, true);
    return toks;
}

// Decode tokens onto one sequence, continuing its positions. Logits only for the last token (when wanted).
bool decode_seq(Engine *e, const std::vector<llama_token> &toks, llama_seq_id seq, bool want_logits) {
    llama_pos pos = llama_memory_seq_pos_max(e->mem(), seq) + 1;
    llama_batch b = llama_batch_init(e->n_batch, 0, 1);
    bool ok = true;
    for (size_t i = 0; i < toks.size() && ok; i += e->n_batch) {
        int n = (int) std::min((size_t) e->n_batch, toks.size() - i);
        b.n_tokens = n;
        for (int j = 0; j < n; j++) {
            b.token[j] = toks[i + j];
            b.pos[j] = pos++;
            b.n_seq_id[j] = 1;
            b.seq_id[j][0] = seq;
            b.logits[j] = want_logits && (i + j == toks.size() - 1);
        }
        ok = llama_decode(e->ctx, b) == 0;
    }
    llama_batch_free(b);
    return ok;
}

// First token of each spelling of the answer ("yes", "Yes", " yes", ...).
std::vector<llama_token> answer_ids(const llama_vocab *v, std::initializer_list<const char *> words) {
    std::vector<llama_token> ids;
    for (auto w : words) {
        auto t = tokenize(v, w, false);
        if (!t.empty() && std::find(ids.begin(), ids.end(), t[0]) == ids.end()) ids.push_back(t[0]);
    }
    return ids;
}
}  // namespace

extern "C" JNIEXPORT jlong JNICALL
Java_com_example_backfire_detect_LlamaBridge_nativeLoad(JNIEnv *env, jobject, jstring path, jint threads, jint n_ctx) {
    llama_log_set([](ggml_log_level lvl, const char *text, void *) {
        if (lvl >= GGML_LOG_LEVEL_INFO) __android_log_print(lvl >= GGML_LOG_LEVEL_WARN ? ANDROID_LOG_WARN : ANDROID_LOG_INFO, "llama.cpp", "%s", text);
    }, nullptr);
    llama_backend_init();
    LOGI("system: %s", llama_print_system_info());
    auto mp = llama_model_default_params();
    // Weights stay memory-mapped (file-backed): Android can page them out instead of killing us. Loading into RAM
    // enables q4_K repacking but needs ~3.2 GB; measured on a Galaxy S22 with 3.4 GB free it swapped (3 tok/s) and
    // was killed. mmap: ~11 tok/s prompt, ~5 tok/s decode on the 4 performance cores.
    mp.use_extra_bufts = true;  // repack Q4 weights for the CPU's dotprod/i8mm kernels (big speedup on ARM)
    llama_model *model = llama_model_load_from_file(jstr(env, path).c_str(), mp);
    if (!model) { LOGE("model load failed"); return 0; }
    auto cp = llama_context_default_params();
    cp.n_ctx = n_ctx;
    cp.n_batch = 512;
    cp.n_ubatch = 512;
    cp.n_threads = threads;
    cp.n_threads_batch = threads;
    cp.n_seq_max = 3;          // LIVE, ASK, PREFIX
    cp.kv_unified = true;      // the sequences share one prefix: one buffer, cheap copies
    llama_context *ctx = llama_init_from_model(model, cp);
    if (!ctx) { llama_model_free(model); LOGE("context init failed"); return 0; }
    auto *e = new Engine();
    e->model = model; e->ctx = ctx; e->vocab = llama_model_get_vocab(model);
    e->yes_ids = answer_ids(e->vocab, {"yes", "Yes", " yes", " Yes", "YES"});
    e->no_ids = answer_ids(e->vocab, {"no", "No", " no", " No", "NO"});
    LOGI("loaded: ctx=%d threads=%d yes_ids=%zu no_ids=%zu", n_ctx, threads, e->yes_ids.size(), e->no_ids.size());
    return (jlong) e;
}

// System prompt + the opening of the user turn. Evaluated once, kept on PREFIX; LIVE starts as a copy.
extern "C" JNIEXPORT jboolean JNICALL
Java_com_example_backfire_detect_LlamaBridge_nativeSetPrefix(JNIEnv *env, jobject, jlong h, jstring prefix) {
    auto *e = (Engine *) h;
    std::lock_guard<std::mutex> lock(e->mu);
    llama_memory_clear(e->mem(), true);
    auto toks = tokenize(e->vocab, jstr(env, prefix), true);
    if (!decode_seq(e, toks, PREFIX, false)) return false;
    llama_memory_seq_cp(e->mem(), PREFIX, LIVE, -1, -1);
    LOGI("prefix: %zu tokens", toks.size());
    return true;
}

// New call: the transcript goes back to just the system prompt (an in-engine copy, no re-evaluation).
extern "C" JNIEXPORT void JNICALL
Java_com_example_backfire_detect_LlamaBridge_nativeReset(JNIEnv *, jobject, jlong h) {
    auto *e = (Engine *) h;
    std::lock_guard<std::mutex> lock(e->mu);
    llama_memory_seq_rm(e->mem(), LIVE, -1, -1);
    llama_memory_seq_rm(e->mem(), ASK, -1, -1);
    llama_memory_seq_cp(e->mem(), PREFIX, LIVE, -1, -1);
}

// Append caller text to the live transcript (decoded once). Returns the context position, or -1 on failure.
extern "C" JNIEXPORT jint JNICALL
Java_com_example_backfire_detect_LlamaBridge_nativeAppend(JNIEnv *env, jobject, jlong h, jstring text) {
    auto *e = (Engine *) h;
    std::lock_guard<std::mutex> lock(e->mu);
    auto toks = tokenize(e->vocab, jstr(env, text), false);
    if (!decode_seq(e, toks, LIVE, false)) return -1;
    return llama_memory_seq_pos_max(e->mem(), LIVE) + 1;
}

// Ask the question at the end of the transcript (on a scratch copy); returns P(yes) in [0,1], or -1 on failure.
extern "C" JNIEXPORT jfloat JNICALL
Java_com_example_backfire_detect_LlamaBridge_nativeAsk(JNIEnv *env, jobject, jlong h, jstring question) {
    auto *e = (Engine *) h;
    std::lock_guard<std::mutex> lock(e->mu);
    llama_memory_seq_rm(e->mem(), ASK, -1, -1);
    llama_memory_seq_cp(e->mem(), LIVE, ASK, -1, -1);
    auto toks = tokenize(e->vocab, jstr(env, question), false);
    bool ok = !toks.empty() && decode_seq(e, toks, ASK, true);
    const float *logits = ok ? llama_get_logits_ith(e->ctx, -1) : nullptr;
    float p = -1.f;
    if (logits) {
        float mx = -INFINITY;
        for (auto t : e->yes_ids) mx = std::max(mx, logits[t]);
        for (auto t : e->no_ids) mx = std::max(mx, logits[t]);
        double py = 0, pn = 0;
        for (auto t : e->yes_ids) py += std::exp(logits[t] - mx);
        for (auto t : e->no_ids) pn += std::exp(logits[t] - mx);
        if (py + pn > 0) p = (float) (py / (py + pn));
    }
    llama_memory_seq_rm(e->mem(), ASK, -1, -1);
    return p;
}

// Speed check: for each thread count, time prompt processing of n_tok tokens and one-token decodes (on a scratch
// sequence). Returns lines "threads pp_tok_per_s tg_tok_per_s". Restores the given thread count afterwards.
extern "C" JNIEXPORT jstring JNICALL
Java_com_example_backfire_detect_LlamaBridge_nativeBench(JNIEnv *env, jobject, jlong h, jintArray threads, jint n_tok, jint keep) {
    auto *e = (Engine *) h;
    std::lock_guard<std::mutex> lock(e->mu);
    jsize n = env->GetArrayLength(threads);
    std::vector<jint> ts(n);
    env->GetIntArrayRegion(threads, 0, n, ts.data());
    auto filler = tokenize(e->vocab, " the caller said that the bank account needs to be verified today", false);
    std::vector<llama_token> pp;
    while ((int) pp.size() < n_tok) pp.insert(pp.end(), filler.begin(), filler.end());
    pp.resize(n_tok);
    std::string out;
    for (auto t : ts) {
        llama_set_n_threads(e->ctx, t, t);
        llama_memory_seq_rm(e->mem(), ASK, -1, -1);
        llama_memory_seq_cp(e->mem(), PREFIX, ASK, -1, -1);
        auto t0 = std::chrono::steady_clock::now();
        decode_seq(e, pp, ASK, true);
        auto t1 = std::chrono::steady_clock::now();
        for (int i = 0; i < 8; i++) decode_seq(e, {pp[i]}, ASK, true);
        auto t2 = std::chrono::steady_clock::now();
        double pp_s = std::chrono::duration<double>(t1 - t0).count(), tg_s = std::chrono::duration<double>(t2 - t1).count();
        char line[96];
        snprintf(line, sizeof line, "%d %.1f %.1f\n", t, n_tok / pp_s, 8 / tg_s);
        LOGI("bench threads=%d pp=%.1f tok/s tg=%.1f tok/s", t, n_tok / pp_s, 8 / tg_s);
        out += line;
    }
    llama_memory_seq_rm(e->mem(), ASK, -1, -1);
    llama_set_n_threads(e->ctx, keep, keep);
    return env->NewStringUTF(out.c_str());
}

extern "C" JNIEXPORT void JNICALL
Java_com_example_backfire_detect_LlamaBridge_nativeFree(JNIEnv *, jobject, jlong h) {
    auto *e = (Engine *) h;
    if (!e) return;
    llama_free(e->ctx);
    llama_model_free(e->model);
    delete e;
}
