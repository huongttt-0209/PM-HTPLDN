#!/usr/bin/env python3
"""READ-ONLY: rà lại 309 case tuần 3 với ĐỦ 4 cặp cột (bổ sung trục dev fix).
Không ghi bất cứ thứ gì lên Google Sheets.
"""
import json, os, re, unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(HERE, "cache_w3.json")))
R = json.load(open(os.path.join(HERE, "result_w3.json")))
drive, partner = C["drive"], C["partner"]
dh, ph = drive[0], partner[0]


def col(hdr, name):
    for i, h in enumerate(hdr):
        if h.strip() == name:
            return i
    return None


DC = {n: col(dh, n) for n in ["Trạng thái 1", "Trạng thái dev fix 1", "Verify",
                              "Trạng thái 2", "Trạng thái dev fix 2", "Verify 2"]}
PC = {n: col(ph, n) for n in ["Trạng thái", "Trạng thái dev fix",
                              "Trạng thái 2", "Trạng thái dev fix 2"]}


def g(row, ci):
    return row[ci].strip() if ci is not None and ci < len(row) else ""


# Chính tả thật trong dropdown đối tác -> dạng chuẩn để SO SÁNH.
# KHÔNG sửa dữ liệu, chỉ dùng khi so.
SPELL = {
    "resoved": "resolved", "resolve": "resolved",
    "reopent": "reopen", "re-open": "reopen", "reopen": "reopen",
    "devdone": "dev done", "done": "dev done",
}


def toks(s):
    """Tách trạng thái đa giá trị thành TẬP token đã chuẩn hoá chính tả."""
    s = unicodedata.normalize("NFC", s or "")
    out = set()
    for t in re.split(r"[,;/]+|\n+", s):
        t = re.sub(r"\s+", " ", t).strip().lower()
        if not t:
            continue
        out.add(SPELL.get(t.replace(" ", ""), SPELL.get(t, t)))
    return out


def cmp_tok(a, b):
    """Trả (verdict, mô tả). verdict: same | subset_drive | subset_partner | diff"""
    ta, tb = toks(a), toks(b)
    if ta == tb:
        return "same", ""
    if not ta and tb:
        return "diff", "DRIVE trống"
    if ta and not tb:
        return "diff", "ĐỐI TÁC trống"
    if ta > tb:
        return "subset_drive", "DRIVE có thêm: " + ", ".join(sorted(ta - tb))
    if tb > ta:
        return "subset_partner", "ĐỐI TÁC có thêm: " + ", ".join(sorted(tb - ta))
    return "diff", "khác hẳn"


rows = []
for e in R:
    dr = drive[e["drow"] - 1]
    pr = partner[e["prow"] - 1] if e["prow"] else None
    r = dict(e)
    r["d_ver1"] = g(dr, DC["Verify"])
    r["p_fix1"] = g(pr, PC["Trạng thái dev fix"]) if pr else ""
    r["p_fix2"] = g(pr, PC["Trạng thái dev fix 2"]) if pr else ""

    if not pr:
        r["axes"] = None
        rows.append(r)
        continue

    a = cmp_tok(r["d_st1"], r["p_st1"])          # Trạng thái 1 <-> Trạng thái
    b = cmp_tok(r["d_st2"], r["p_st2"])          # Trạng thái 2 <-> Trạng thái 2
    c = cmp_tok(r["d_fix1"], r["p_fix1"])        # dev fix 1 <-> dev fix
    d = cmp_tok(r["d_fix2"], r["p_fix2"])        # dev fix 2 <-> dev fix 2
    r["axes"] = {"st1": a, "st2": b, "fix1": c, "fix2": d}

    # Xung đột quan điểm: DRIVE coi như xong, ĐỐI TÁC coi như còn mở
    dv = toks(r["d_ver1"])
    pf = toks(r["p_fix1"])
    r["conflict"] = bool(dv & {"pass", "resolved"} and "reopen" in pf)
    rows.append(r)

# ---------- thống kê ----------
print("=== Phân bố lệch theo TRỤC (chỉ 299 dòng map được) ===")
for axis, label in [("st1", "Trạng thái 1 ↔ Trạng thái"),
                    ("st2", "Trạng thái 2 ↔ Trạng thái 2"),
                    ("fix1", "Trạng thái dev fix 1 ↔ Trạng thái dev fix"),
                    ("fix2", "Trạng thái dev fix 2 ↔ Trạng thái dev fix 2")]:
    c = Counter(r["axes"][axis][0] for r in rows if r["axes"])
    print(f"  {label:46s} {dict(c)}")

conf = [r for r in rows if r.get("conflict")]
print(f"\n=== XUNG ĐỘT (DRIVE Verify=Pass/Resolved  vs  ĐỐI TÁC dev fix=Reopen*): {len(conf)} ===")
for r in conf:
    print(f"  drive row {r['drow']:4d} {r['dma']:22s} | DRIVE fix1={r['d_fix1']!r} Verify={r['d_ver1']!r}"
          f"  | ĐỐI TÁC fix={r['p_fix1']!r}")

print("\n=== Cặp giá trị dev fix 1 <-> dev fix (đã map), theo tần suất ===")
for (a, b), n in Counter((r["d_fix1"], r["p_fix1"]) for r in rows if r["axes"]).most_common():
    v = cmp_tok(a, b)
    mark = "OK " if v[0] == "same" else "!! "
    print(f"  {mark}{n:4d}  DRIVE {a!r:26s} <-> ĐỐI TÁC {b!r:22s}  {v[0]} {v[1]}")

json.dump(rows, open(os.path.join(HERE, "audit_w3.json"), "w"), ensure_ascii=False, indent=1)
