#!/usr/bin/env python3
"""doi-soat cuoi vong 2: bang 1 trong report  <->  cot W/X/Y tren 2 tab sheet.

CHI DOC, khong ghi gi. Chay: python3 reverify-round-doi-soat.py
"""
import os, re, sys, warnings
warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, "tools")
REPORT = os.path.join(HERE, "reverify-week-4", "reverify-round-2026-08-03",
                      "KET-QUA-REVERIFY-VONG-2.md")
sys.path.insert(0, TOOLS)

# case ngoai le: ghi bang --mode qaverdict (cot Q/R vong 1) vi dong khong co claim vong 2
EXCEPT_QAVERDICT = {"TLCTCDG_11"}

# --------- 1. doc bang 1 trong report ----------------------------------------
rows_md = []
for ln in open(REPORT, encoding="utf-8"):
    m = re.match(r"\|\s*(\d+)\s*\|\s*([A-Za-z0-9_]+)\s*\|\s*T([23])\s*·\s*(\d+)\s*\|"
                 r"[^|]*\|\s*[^ ]+\s*([^|]+?)\s*\|", ln)
    if m:
        rows_md.append(dict(stt=int(m.group(1)), ma=m.group(2), tab=m.group(3),
                            row=int(m.group(4)), verdict=m.group(5).strip()))
print(f"Report: {len(rows_md)} case trong Bang 1")

# --------- 2. doc 2 tab sheet -------------------------------------------------
sheet = {}
for tab_no, tab_name in (("2", "UAT_TGPL Doanh Nghiệp-tuần 2"),
                         ("3", "UAT_TGPL Doanh Nghiệp-tuần 3")):
    os.environ["UAT_TAB"] = tab_name
    for mod in [m for m in list(sys.modules) if m == "sheet_read"]:
        del sys.modules[mod]
    import sheet_read
    vals = sheet_read.get_ws().get_all_values()
    hdr = [h.strip() for h in vals[0]]
    ci = {n: hdr.index(n) for n in ("Mã TC", "Verify", "DEV phản hồi lần 1",
                                    "Trạng thái dev fix 2", "Verify 2", "DEV phản hồi lần 2")
          if n in hdr}
    for i, r in enumerate(vals[1:], start=2):
        g = lambda n: (r[ci[n]].strip() if n in ci and ci[n] < len(r) else "")
        sheet[(tab_no, i)] = dict(ma=g("Mã TC"), q=g("Verify"), rr=g("DEV phản hồi lần 1"),
                                  w=g("Trạng thái dev fix 2"), x=g("Verify 2"),
                                  y=g("DEV phản hồi lần 2"))
    print(f"Sheet tuan {tab_no}: doc {len(vals)-1} dong")

# --------- 3. doi chieu ------------------------------------------------------
bad, ok = [], 0
for c in rows_md:
    s = sheet.get((c["tab"], c["row"]))
    if not s:
        bad.append((c, "KHONG THAY dong tren sheet")); continue
    if s["ma"] != c["ma"]:
        bad.append((c, f"Ma TC lech: sheet={s['ma']!r}")); continue

    # LUU Y: W ('dev done') va Y co the la chu cua DEV — QA khong dung toi.
    # Vi vay chi rang buoc o cell QA thuc su ghi; "ai ghi" tra bang nhat ky (buoc 3b).
    v, probs = c["verdict"], []
    if c["ma"] in EXCEPT_QAVERDICT:
        if s["q"] != "Pass":
            probs.append(f"ngoai le qaverdict: Verify(Q)={s['q']!r} (can 'Pass')")
        if "QA kiểm thử lại" not in s["rr"]:
            probs.append("ngoai le qaverdict: cot R thieu doan QA them")
        if s["x"]:
            probs.append(f"ngoai le qaverdict: X phai TRONG (dang {s['x']!r})")
    elif v == "Pass":
        if s["x"] != "Pass":
            probs.append(f"Verify 2 = {s['x']!r} (can 'Pass')")
    elif v == "Reopen":
        if s["w"] != "Reopen": probs.append(f"Trang thai dev fix 2 = {s['w']!r} (can 'Reopen')")
        if s["x"] != "Reopen": probs.append(f"Verify 2 = {s['x']!r} (can 'Reopen')")
        if not s["y"]:          probs.append("Reopen nhung cot Y TRONG")
    elif v == "BA confirm":
        if s["x"] != "BA confirm": probs.append(f"Verify 2 = {s['x']!r} (can 'BA confirm')")
        if not s["y"]:             probs.append("BA confirm nhung cot Y TRONG")
    else:
        probs.append(f"verdict la {v!r} — khong hop le")

    if probs: bad.append((c, " · ".join(probs)))
    else: ok += 1

print(f"\n{'='*70}\nKHOP: {ok}/{len(rows_md)}    LECH: {len(bad)}")
for c, why in bad:
    print(f"  ❌ #{c['stt']:>2} {c['ma']:<16} T{c['tab']}·{c['row']:<4} [{c['verdict']}] -> {why}")
if not bad:
    print("  ✅ Khong lech dong nao.")

# --------- 3b. tra nhat ky: QA da ghi dung cot chua ------------------------
import json
LOGF = os.path.join(TOOLS, "sheet_write.log")
wrote = {}          # (tab,row) -> set(cot chu cai)
for ln in open(LOGF, encoding="utf-8"):
    ln = ln.strip()
    if not ln: continue
    try: d = json.loads(ln)
    except Exception: continue
    if not d.get("ts", "").startswith("2026-08-03"): continue
    t = "2" if d["tab"].endswith("2") else "3" if d["tab"].endswith("3") else "?"
    k = (t, d["row"])
    wrote.setdefault(k, set()).update(w["cell"][0] for w in d.get("writes", []))

print("\n--- nhat ky ghi (chi 54 case trong scope) ---")
missing, p_touch = [], []
for c in rows_md:
    cols = wrote.get((c["tab"], c["row"]))
    if not cols:
        missing.append(c)
    elif "P" in cols:
        p_touch.append((c, cols))
print(f"  Case KHONG co ban ghi nao hom nay: {len(missing)}"
      + ("" if not missing else " -> " + ", ".join(f"{x['ma']}(T{x['tab']}·{x['row']})" for x in missing)))
print(f"  Case QA lo ghi vao cot P (cua dev): {len(p_touch)}"
      + ("" if not p_touch else " -> " + ", ".join(f"{c['ma']}{sorted(s)}" for c, s in p_touch)))

# --------- 4. thong ke -------------------------------------------------------
from collections import Counter
print("\nPhan bo verdict:", dict(Counter(c["verdict"] for c in rows_md)))
dup = [m for m, n in Counter(c["ma"] for c in rows_md).items() if n > 1]
print("Ma TC trung trong report:", dup or "khong co")
