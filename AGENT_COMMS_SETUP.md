# Agent comms: complete setup (macOS + Windows)

> **v2 (00:30): already set up? Don't restart anything.** Run `git pull --rebase --autostash`, then `bash scripts/comms/setup` (no id needed) and paste the §6 prompt into your running session. The hooks run the scripts from disk, so the new behavior starts on your agent's next tool call. New: replies now reach the thread's sender, `ack` / `done` / `wait` / `blast`, the Stop hook enforces answers, pushes and a background watcher, and `scripts/git/sync` handles all pushing and pulling (§12). A restart is needed only if `.claude/settings.json` itself changes.

Every pipeline's Claude Code agent can message every other pipeline's agent. Messages are **pushed into the receiving agent's session automatically**: the agent doesn't have to remember to check. The same tooling also reports each machine's pipeline, step and agent count to the team dashboard (`dashboard/`).

**Time to set up: about 10 minutes per machine.** Do it once per laptop. If one laptop runs two pipelines (Ayman runs P1 and P2 on two machines), do it on each machine.

---

## 0. What you're setting up (read once, 1 minute)

```
 Agent P3 (Evan's laptop)                     GitHub repo Proton-Designer/HackUTD26            Agent P1 (Ayman's laptop)
 bash scripts/comms/send P1 "subj" "body" ──► Issue "[P3→P1] subj"  labels to:P1, from:P3 ──► hook fires inside P1's Claude session
                                                                                               → message appears in P1's context
                                                                                               → P1 replies: send reply <#> "..."
```

- **Bus:** GitHub Issues on our repo (labels `to:P#`, `from:P#`). Nothing new to host, works on any Wi-Fi, full history.
- **Enforcer:** Claude Code *hooks* in `.claude/settings.json` (already in the repo). They run `scripts/comms/inbox` automatically:

| When | Hook | What the agent experiences |
|---|---|---|
| Session starts | `SessionStart` | Told its pipeline id + how to send/report; any unread mail is shown |
| You type a prompt | `UserPromptSubmit` | Unread mail is attached to your prompt |
| While working (after any tool, max once per 60 s) | `PostToolUse` | New mail interrupts it as a 📨 banner; it reads and replies |
| It tries to finish/go idle | `Stop` | **Not allowed to stop** while (1) unread mail exists, (2) a thread addressed to it has never been answered, (3) it has unpushed commits, or (4) no background `inbox watch` is armed |
| It's idle | background `inbox watch` | The watcher exits the moment mail arrives (checks every 15 s), which wakes the agent; it re-arms on its next stop |

- **Identity:** a one-line file `.backfire-pipeline` (gitignored) says which pipeline this machine is.
- **Presence:** the same hooks edit one comment per machine on the "📡 Agent presence board" issue: pipeline, step, agent count, last tool. That's what the dashboard displays.

### Pipeline ids

| Id | Pipeline | Person / machine |
|---|---|---|
| `P1` | Network & call control (Telnyx, server, Maria's app, contracts) | Ayman, machine A |
| `P2` | Detection brain | Ayman, machine B |
| `P3` | Decoy & voice | Evan |
| `P4a` | Intel & policy gate (`intel/`) | Kareem |
| `P4b` | Command center & story | Rayan |

Sending to `P4` reaches both P4a and P4b. `ALL` reaches everyone except the sender.

---

## 1. Prerequisites

You need **git**, the **GitHub CLI (`gh`)**, **Claude Code**, and **collaborator access** to `Proton-Designer/HackUTD26`.

### 1A. macOS

Open **Terminal** and run:

```bash
# git (skip if `git --version` already works)
xcode-select --install

# Homebrew (skip if `brew -v` works)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# GitHub CLI
brew install gh

# optional: gives the hooks an 8-second network cap
brew install coreutils
```

### 1B. Windows

Open **PowerShell** (normal, not admin is fine) and run:

```powershell
winget install --id Git.Git -e          # Git for Windows, includes Git Bash (REQUIRED)
winget install --id GitHub.cli -e       # GitHub CLI
```

Then **close and reopen** the terminal so `git` and `gh` are on PATH.

> **Why Git Bash is required on Windows:** Claude Code runs hook commands in Git Bash. Without Git Bash it falls back to PowerShell, and our hooks would silently not run (no messages delivered). If Git is installed somewhere unusual, set the environment variable `CLAUDE_CODE_GIT_BASH_PATH` to the full path of `bash.exe` (e.g. `C:\Program Files\Git\bin\bash.exe`) and restart Claude Code.
>
> **Using WSL instead?** Then do everything (clone, `gh`, Claude Code) *inside* WSL and follow the macOS/Linux steps; in WSL, install gh with `sudo apt install gh`.

From here on, Windows users type the commands in **Git Bash** (Start menu → "Git Bash"), not PowerShell. All commands below are identical on macOS and Windows.

### 1C. Log the GitHub CLI in (both OSes)

```bash
gh auth login
```
Answer: **GitHub.com** → **HTTPS** → *Authenticate Git with your GitHub credentials?* **Yes** → **Login with a web browser**. Copy the one-time code, press Enter, approve in the browser.

Check: `gh auth status` should say "Logged in to github.com".

### 1D. Repo access

Ayman (`Proton-Designer`) must add your GitHub username as a collaborator (repo → Settings → Collaborators). **Accept the email invite** (or open https://github.com/Proton-Designer/HackUTD26/invitations). Without write access you can't send messages.

### 1E. Claude Code

Already installed for most of us. Check with `claude --version`. If missing, install it from https://claude.com/claude-code. Hooks need a reasonably recent version, so run `claude update` if yours is old.

---

## 2. Get the code (the branch with the comms tooling)

**If you don't have the repo yet:**
```bash
cd ~/Documents            # or wherever you keep code
git clone https://github.com/Proton-Designer/HackUTD26.git
cd HackUTD26
git checkout finalized-idea-backfire
```

**If you already have it:**
```bash
cd path/to/HackUTD26
git fetch origin
git checkout finalized-idea-backfire
git pull
```

You should now see `scripts/comms/` and `.claude/settings.json` in the folder.

> Once this branch is merged to `main`, use `main` instead. The tooling lives wherever the branch you work on is; **your pipeline's working branch must contain `scripts/comms/` and `.claude/settings.json`** (if you branch off, branch from this one or merge it in).

---

## 3. Run the one-command setup

From the repo root (Git Bash on Windows, Terminal on macOS), with **your** pipeline id:

```bash
bash scripts/comms/setup P3        # Evan
bash scripts/comms/setup P4a       # Kareem
bash scripts/comms/setup P4b       # Rayan
bash scripts/comms/setup P1        # Ayman machine A
bash scripts/comms/setup P2        # Ayman machine B
```

It writes `.backfire-pipeline`, then checks and reports `[ OK ]` / `[FAIL]` for:
OS + shell, identity, gitignore, git, gh, gh login, write access to the repo, the to:/from: labels (creates any that are missing), the hooks file, LF line endings, and a live read of the message bus.

**Every line must be `[ OK ]`** (a `[WARN]` is fine). It ends with `All good.` Fix any `[FAIL]` using the message it prints and re-run `bash scripts/comms/setup` (no id needed the second time).

---

## 4. Start Claude Code so the hooks load

Hooks are read **when a session starts**. In the repo root:

```bash
claude
```

(or open the repo folder in the Claude desktop app's Code tab / your IDE extension; it must be this folder, because hooks come from `.claude/settings.json` here).

- If Claude Code asks whether to **trust this folder**, say yes (project hooks only run in trusted folders).
- If it says hooks changed or asks you to review them, open `/hooks`, review, and accept.
- Already had a session open? **Exit and start a new one**; the running one won't have the hooks.

**Verify:** type `/hooks` inside Claude Code. You should see `SessionStart`, `UserPromptSubmit`, `PostToolUse`, `Stop`, each running `bash ".../scripts/comms/inbox" hook-...`. Also, the first reply of a new session should mention "Backfire comms: you are pipeline P#".

---

## 5. Test it end to end (2 minutes, do it with one teammate)

1. On your machine (terminal, not inside Claude):
   ```bash
   bash scripts/comms/send ping P1      # ping any pipeline that's already set up
   ```
   It prints `sent: https://github.com/.../issues/N`.
2. Within about a minute, the receiver's agent shows a 📨 banner with "ping from P#" (or it shows on the receiver's next prompt).
3. Their agent closes it with `bash scripts/comms/send close N "pong from P1"`.
4. On your side, your agent gets the "Resolved: pong" reply automatically (or run `bash scripts/comms/inbox check` in a terminal to see it).

If the ping never arrives, see Troubleshooting below.

---

## 6. Tell your agent about it (paste once at the start of every session)

> You are pipeline **P#** of Backfire. Other pipelines' agents message you through `scripts/comms`; their messages are injected into your session automatically. Rules (the hooks enforce them):
> 1. **Answer every thread addressed to you immediately**, at least with `bash scripts/comms/send ack <#> "on it, ETA …"`. Never leave another agent waiting; never ask me to relay a message: send it yourself.
> 2. **Need something from another pipeline?** `bash scripts/comms/send wait <P#> "exactly what you need (endpoint, payload, file)"`, then keep working on whatever isn't blocked, with the watcher armed.
> 3. **Delivered something someone asked for?** Commit your own files (never `git add -A`, never BOARD.md), then `bash scripts/comms/send done <#> "what landed + how to use it"`. That pushes via `scripts/git/sync` and posts the commit SHA. No thread? `send done <P#> "…"`.
> 4. **Push as soon as a piece works** with `bash scripts/git/sync` (never `git push --force`). Pull teammates' work with `bash scripts/git/sync --pull` before starting a task and whenever a ✅ DONE / 📢 announcement says so.
> 5. **Before you go idle,** start `bash scripts/comms/inbox watch` as a **background** command (run_in_background) so a message wakes you. Re-arm it every time it exits.
> 6. **Report progress** each time you start an outcome from your pipeline guide: `bash scripts/comms/status <outcome#> "what"`. Blocked? `send wait` marks you blocked; `bash scripts/comms/status unblocked` when it clears.
> 7. 📢 announcements (`send blast`) are from the team lead: do what they say first. Contract changes are proposals to P1; only P1 edits `contracts/`. Tell me when a message changes my plan.

---

## 7. Command reference

| Command | What it does |
|---|---|
| `bash scripts/comms/send P3 "subject" "body"` | New thread to P3 (targets: `P1 P2 P3 P4 P4a P4b ALL`) |
| `bash scripts/comms/send P3 "subject" -` | Same, body from stdin (long text, quotes): `... - <<'EOF'` … `EOF` |
| `bash scripts/comms/send reply 12 "text" [P2]` | Reply on thread #12; optional extra recipient |
| `bash scripts/comms/send close 12 "resolution"` | Close #12 with a note |
| `bash scripts/comms/send ack 12 "on it, ETA 20m"` | Acknowledge #12 now (clears "you owe a reply") |
| `bash scripts/comms/send done 12 "what landed"` | **Push** (via sync), post commit SHA + branch on #12, close it; the asker is notified |
| `bash scripts/comms/send done P4a "what landed"` | Same, as a new ✅ READY thread to a pipeline (or ALL) |
| `bash scripts/comms/send wait P1 "what I need"` | ⛔ Ask for something you're blocked on; marks you blocked on the dashboard |
| `bash scripts/comms/send blast "subject" "body"` | 📢 Announcement to every agent (shown first, "act now") |
| `bash scripts/comms/inbox owed` | Threads addressed to me I haven't answered |
| `bash scripts/comms/send list` | Open threads addressed to me / ALL |
| `bash scripts/comms/send ping P2` | Test message |
| `bash scripts/comms/inbox check` | Show unread mail now (marks it read) |
| `bash scripts/comms/inbox watch` | Run in the **background**: exits (and wakes the agent) when mail arrives; auto-expires after 25 min |
| `bash scripts/comms/inbox reset` | Forget read-state; next check re-shows all open threads |
| `bash scripts/comms/status 3 "doing X"` | Report outcome #3 + what you're doing (dashboard) |
| `bash scripts/comms/status blocked "on P3"` / `unblocked` | Mark / clear blocked (red on dashboard) |
| `bash scripts/comms/setup` | Re-run all checks (also sets git pull.rebase / autoStash / rerere) |
| `bash scripts/git/sync` / `--pull` | Fetch + rebase (+ push with retries). The only way anyone should push/pull |

Everything can also be read on GitHub: https://github.com/Proton-Designer/HackUTD26/issues

---

## 8. How fast is it?

| Situation | Delay until the receiving agent sees it |
|---|---|
| Receiver agent is working (using tools) | ≤ ~30 s (`PostToolUse` checks at most every 30 s) |
| Receiver agent finishes its turn | Immediately at that moment (`Stop` hook) |
| Receiver's human types a prompt | Immediately (`UserPromptSubmit`) |
| Receiver agent is idle | ≤ ~15 s: its background `inbox watch` (enforced by the Stop hook) exits and wakes it |

**Integration windows (tight back-and-forth):** ask the receiving agent to run `bash scripts/comms/inbox watch` as a **background** command. It checks every 30 s (`BACKFIRE_WATCH_INTERVAL=10` for faster) and exits when mail arrives, which wakes the agent. Then it re-arms the watch. A back-and-forth then takes ~10–40 s per hop.

Tuning: `BACKFIRE_COMMS_THROTTLE=30` (env var, seconds) makes the in-work check more frequent. The GitHub API allows 5,000 calls/hour per person; defaults use well under 10% of that.

GitHub's label index can lag a few seconds after a message is created; a message that's missed on one check is delivered on the next (nothing is lost; delivery is tracked by message id, not by clock).

---

## 9. Rules of the road

- **Agents talk to agents here; humans talk on Discord.** Decisions that change the plan go through `@Delegation_Bot` on Discord. **Only the bot edits `BOARD.md`.**
- **Only P1 edits `contracts/`.** Others propose changes by message to P1.
- One topic per thread; reply in the thread; **close it when resolved** (keeps everyone's inbox clean).
- Concrete beats chatty: file paths, branch names, payload examples, exact error text.
- Never send secrets (API keys, tokens, phone numbers of real people) in messages. The repo is shared.
- Don't edit the "📡 Agent presence board" issue by hand; the scripts maintain it.

---

## 10. Troubleshooting

| Symptom | Fix |
|---|---|
| `setup` says `gh not found` | Install gh (§1), then **reopen the terminal**. Windows: run setup from **Git Bash**. |
| `gh is not logged in` | `gh auth login` (§1C). |
| `no write access` | Get added as collaborator **and accept the invite** (§1D). |
| `scripts have Windows (CRLF) line endings` | In Git Bash: `rm scripts/comms/* .claude/settings.json && git checkout -- scripts/comms .claude/settings.json` (the repo's `.gitattributes` forces LF from then on). |
| `/hooks` shows nothing | You started Claude outside the repo root, didn't trust the folder, or the session predates the pull. `cd` to the repo root and start a **new** session. |
| Windows: hooks listed but never fire / "bash is not recognized" | Git Bash missing or not found: install Git for Windows (§1B) or set `CLAUDE_CODE_GIT_BASH_PATH` to `C:\Program Files\Git\bin\bash.exe`, restart Claude Code. |
| Windows: mid-task banners don't appear but mail shows at turn end / on prompts | A known Claude Code issue on Windows can hide `PostToolUse` feedback. Delivery still happens via `Stop` and `UserPromptSubmit`; for tight loops use `inbox watch`. |
| Agent never sees anything; `bash scripts/comms/inbox check` in a terminal *does* show mail | The check marked it read; the hooks aren't loaded in that session (see the `/hooks` row). |
| Nothing anywhere | `cat .backfire-pipeline` must print your id; `bash scripts/comms/send list` must work. Re-run `bash scripts/comms/setup`. |
| Want to see old messages again | `bash scripts/comms/inbox reset` then `bash scripts/comms/inbox check`. |
| Hooks feel slow | They cap network calls at 8 s and never block on errors. On macOS install `coreutils` for the cap. Offline Wi-Fi = silently skipped, retried later. |
| Temporarily silence presence reporting | `export BACKFIRE_PRESENCE=0` before starting Claude. |

---

## 11. Files (for the curious)

| Path | Role |
|---|---|
| `.claude/settings.json` | Registers the four hooks (committed; applies to everyone who opens the repo) |
| `scripts/comms/setup` | One-command setup + self-test |
| `scripts/comms/send` | Send / reply / close / list / ping |
| `scripts/comms/inbox` | Hook entry point: fetch unread mail, deliver it, update presence |
| `scripts/comms/status` | Report step / blocked for the dashboard |
| `scripts/comms/common.sh`, `presence.sh` | Shared helpers (portable bash: macOS bash 3.2, Git Bash, Linux) |
| `.backfire-pipeline` | This machine's pipeline id (gitignored, per machine) |
| `.git/backfire-comms/` | Local read-state (never committed) |
| `.gitattributes` | Forces LF line endings so the scripts run on Windows |
| `dashboard/` | Live team dashboard (see `dashboard/README.md`) |

---

## 12. Git workflow (everyone, all night)

- **One trunk: `finalized-idea-backfire`.** Everyone commits to it directly; no per-pipeline branches, no PRs tonight. (`main` is the stale initial commit; P1 fast-forwards it to a known-good tag before judging.)
- **Own your folders.** Commit with explicit paths: `git add decoy/ && git commit -m "P3: echo decoy over Telnyx WS"`. Never `git add -A`, never edit `BOARD.md` (Discord bot only), never commit `.env`/keys. Shared seams (`contracts/`, `server/main.py`) are P1's: ask with `send wait P1 "…"`.
- **Pull before you start a task, push the moment a piece works:** `bash scripts/git/sync --pull` / `bash scripts/git/sync`. It rebases (autostash keeps uncommitted work), retries pushes up to 3×, never force-pushes, and refuses to push secrets, BOARD.md edits or files over 5 MB.
- **Rebase conflict?** sync stops and lists the files. Keep both sides' intent, `git add <files> && git rebase --continue && bash scripts/git/sync`. Not your file and unsure? `git rebase --abort` and message its owner.
- **Tell people:** if anyone asked for it, `send done <#> "…"` (it pushes for you). If it changes shared behavior, `send done ALL "…"`.
- **Known-good tags (P1 only):** after each green end-to-end run, `git tag -a demo-good-N -m "…" && git push origin demo-good-N`. Feature freeze at 07:30: only P1 pushes after that; the demo machine runs the last tag.
