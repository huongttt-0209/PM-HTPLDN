import json,sys
R=json.load(open("output/dev-report/report-2026-06-07/.qa-results.json",encoding='utf-8'))
order=sorted(R.keys(),key=lambda x:int(x))
ICON={"PASS":"✅ PASS","FAIL":"❌ FAIL","BLOCKED":"🚫 BLOCKED","ChờBA":"❓ Chờ BA","Env":"🔧 Env/Infra"}
rows=[]
for n in order:
    r=R[n]
    rows.append(f'| {n} | {r["slug"]} | {r["module"]} | {r["p"]} | {r["ba"]} | {ICON.get(r["qa"],r["qa"])} | {r.get("ev","-")[:70]} | {r.get("note","")[:60]} |')
cnt={"PASS":0,"FAIL":0,"BLOCKED":0,"ChờBA":0,"Env":0}
for n in R: cnt[R[n]["qa"]]=cnt.get(R[n]["qa"],0)+1
print("ROWS:",len(rows),"| PASS",cnt["PASS"],"FAIL",cnt["FAIL"],"BLOCKED",cnt["BLOCKED"],"ChờBA",cnt["ChờBA"],"Env",cnt["Env"])
open("output/dev-report/report-2026-06-07/.table-rows.txt","w",encoding='utf-8').write("\n".join(rows))
open("output/dev-report/report-2026-06-07/.counts.txt","w",encoding='utf-8').write(json.dumps(cnt))
