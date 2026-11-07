"""Count rows per hand-assigned archetype (TASK-105). Assignment: data/tables/Q04_archetype_assignment.csv.
Writes data/tables/Q04_archetype_counts.csv (archetype, field, value, n, N, pct, weighted_pct)."""
import csv, collections
rows=list(csv.DictReader(open('data/tables/Q04_general_1sts.csv')))
asg={(r['project'],r['event']):r['archetype'] for r in csv.DictReader(open('data/tables/Q04_archetype_assignment.csv'))}
by=collections.defaultdict(list)
for r in rows: by[asg[(r['project'],r['event'])]].append(r)
W=sum(float(r['weight']) for r in rows)
out=[]
for a,rs in by.items():
    n=len(rs); wn=sum(float(r['weight']) for r in rs)
    out.append([a,'_size','all',n,len(rows),round(100*n/len(rows)),round(100*wn/W)])
    for fld in ['pattern','ai_role','has_hardware','live_data','novelty_source','event_type']:
        c=collections.Counter(); cw=collections.Counter()
        for r in rs: c[r[fld]]+=1; cw[r[fld]]+=float(r['weight'])
        for v,k in c.most_common(): out.append([a,fld,v,k,n,round(100*k/n),round(100*cw[v]/wn)])
with open('data/tables/Q04_archetype_counts.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['archetype','field','value','n','N','pct','weighted_pct']); w.writerows(out)
