import json,sys
OUT="data/tagged/content/shard_pri_08_out.jsonl"
def F(v,ev): return {"v":v,"ev":ev}
def R(i,t,c,d,im,p):
    return {k:{"v":v,"why":w} for k,(v,w) in zip(["innovation","technical_complexity","completeness","design","impact","presentation"],[i,t,c,d,im,p])}
def add(rec):
    with open(OUT,"a") as f: f.write(json.dumps(rec,ensure_ascii=False)+"\n")
def SF(track,feat,fe,rem,re,lit,lite,w,we,own,owne):
    return {"track":track,"sponsor_features_used":F(feat,fe),"sponsor_removable":F(rem,re),"prompt_literalness":F(lit,lite),"prompt_words_in_title":F(w,we),"problem_owner":F(own,owne)}
