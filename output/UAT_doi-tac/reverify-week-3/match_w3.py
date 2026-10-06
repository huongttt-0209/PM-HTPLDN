#!/usr/bin/env python3
"""READ-ONLY: đối chiếu trạng thái bug tuần 3 giữa file DRIVE và file ĐỐI TÁC.
Không ghi bất cứ thứ gì lên Google Sheets — chỉ đọc cache JSON + xuất .md.
"""
import json, os, re, sys, unicodedata
from difflib import SequenceMatcher
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(HERE, "cache_w3.json")))
drive, partner, plinks = C["drive"], C["partner"], C["partner_links"]
dh, ph = drive[0], partner[0]

WEEK = "Tuần 3"
SIM_FLAG = 0.90     # dưới ngưỡng này -> ❔ map không chắc
SIM_FLOOR = 0.55    # dưới ngưỡng này -> coi như không tìm thấy


def col(hdr, name):
    for i, h in enumerate(hdr):
        if h.strip() == name:
            return i
    return None


DC = {n: col(dh, n) for n in ["Tuần", "Mã TC", "Mô tả", "Kết quả mong đợi",
                              "Trạng thái 1", "Trạng thái dev fix 1", "Verify",
                              "Trạng thái 2", "Trạng thái dev fix 2", "Verify 2"]}
PC = {n: col(ph, n) for n in ["Tuần", "Mã TC", "Mô tả", "Kết quả mong đợi",
                              "Ảnh/vieo 1", "Trạng thái", "Trạng thái dev fix",
                              "Trạng thái 2", "Trạng thái dev fix 2"]}
MISSING = [n for n, i in DC.items() if i is None]
print(f"[info] DRIVE cột thiếu (bỏ qua, không crash): {MISSING}", file=sys.stderr)


def g(row, ci):
    return row[ci].strip() if ci is not None and ci < len(row) else ""


def norm(s):
    s = unicodedata.normalize("NFC", s or "")
    return re.sub(r"\s+", " ", s).strip().lower()


def key(row, cmap, c_mota, c_kq):
    return norm(g(row, cmap[c_mota]) + " " + g(row, cmap[c_kq]))


def prefix(ma):
    m = re.match(r"^([A-Za-zÀ-Ỹà-ỹ]+)", (ma or "").strip())
    return m.group(1).upper() if m else ""


def code_from_files(cell):
    """Parse mã TC từ tên file cột Ảnh/vieo 1 (khoá phụ)."""
    out = []
    for tok in re.split(r"[\n,;]+", cell or ""):
        tok = tok.strip()
        if not tok:
            continue
        tok = re.sub(r"\.(jpg|jpeg|png|webm|mp4|mov|gif|pdf|xlsx|docx)$", "", tok, flags=re.I)
        tok = re.sub(r"\(\d+\)$", "", tok).strip()
        if tok:
            out.append(tok)
    return out


# ---------- gom dòng ----------
drows = []   # (sheet_row, row)
for i, r in enumerate(drive[1:], start=2):
    if g(r, DC["Tuần"]) != WEEK:
        continue
    st1, st2 = g(r, DC["Trạng thái 1"]), g(r, DC["Trạng thái 2"])
    if "fail" in st1.lower() or "fail" in st2.lower():
        drows.append((i, r))

prows_w3, prows_all = [], []
for i, r in enumerate(partner[1:], start=2):
    prows_all.append((i, r))
    if g(r, PC["Tuần"]) == WEEK:
        prows_w3.append((i, r))

print(f"[info] DRIVE bug rows (Trạng thái 1=Fail hoặc Trạng thái 2=Fail): {len(drows)}", file=sys.stderr)
print(f"[info] PARTNER rows tuần 3: {len(prows_w3)} / tổng {len(prows_all)}", file=sys.stderr)

# ---------- ghép cặp ----------
pkey = {i: key(r, PC, "Mô tả", "Kết quả mong đợi") for i, r in prows_w3}
pkey_all = {i: key(r, PC, "Mô tả", "Kết quả mong đợi") for i, r in prows_all}
ppref = {i: prefix(g(r, PC["Mã TC"])) for i, r in prows_w3}
pfilecodes = {i: code_from_files(g(r, PC["Ảnh/vieo 1"])) for i, r in prows_w3}
prow_by_idx = {i: r for i, r in prows_w3}
prow_all_by_idx = {i: r for i, r in prows_all}

by_pref = defaultdict(list)
for i, _ in prows_w3:
    by_pref[ppref[i]].append(i)

pairs = []
for di, dr in drows:
    dk = key(dr, DC, "Mô tả", "Kết quả mong đợi")
    dma = g(dr, DC["Mã TC"])
    dp = prefix(dma)
    for pi in by_pref.get(dp, []):
        sim = SequenceMatcher(None, dk, pkey[pi]).ratio()
        bonus = 0.0
        if dma and dma in pfilecodes[pi]:
            bonus = 0.05          # khoá phụ: tên file khớp mã drive
        pairs.append((sim + bonus, sim, di, pi))

pairs.sort(reverse=True)
assigned_d, assigned_p, match = {}, set(), {}
for score, sim, di, pi in pairs:
    if di in assigned_d or pi in assigned_p:
        continue
    if sim < SIM_FLOOR:
        continue
    assigned_d[di] = pi
    assigned_p.add(pi)
    match[di] = (pi, sim)

# ---------- fallback: quét TOÀN BỘ tab đối tác cho dòng chưa match ----------
fallback = {}
for di, dr in drows:
    if di in match:
        continue
    dk = key(dr, DC, "Mô tả", "Kết quả mong đợi")
    best = (0.0, None)
    for pi, _pr in prows_all:
        if pi in assigned_p:
            continue
        s = SequenceMatcher(None, dk, pkey_all[pi]).ratio()
        if s > best[0]:
            best = (s, pi)
    fallback[di] = best

# ---------- danh sách loại trừ ----------
EXCL_FILE = ("/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/"
             "UAT_doi-tac/reverify-week-4/DANH-SACH-BA-CONFIRM-va-COMMIT-SAU-MOC.md")
excl_txt = open(EXCL_FILE, encoding="utf-8").read()
EXCL = set()
for m in re.finditer(r"\b([A-Z]{2,}(?:_[A-Z0-9]+)*_\d{2,})\b", excl_txt):
    EXCL.add(m.group(1))
print(f"[info] mã trong file loại trừ ({len(EXCL)}): {sorted(EXCL)}", file=sys.stderr)


def cmp_status(a, b):
    """So 'chứa' 2 chiều, chuẩn hoá khoảng trắng + lowercase."""
    na, nb = norm(a), norm(b)
    if na == nb:
        return True
    if not na and not nb:
        return True
    if not na or not nb:
        return False
    return na in nb or nb in na


def blank(s):
    return s if s else "(trống)"


rows_out = []
for di, dr in drows:
    dma = g(dr, DC["Mã TC"])
    dmota = g(dr, DC["Mô tả"])
    d_st1 = g(dr, DC["Trạng thái 1"])
    d_fix1 = g(dr, DC["Trạng thái dev fix 1"])
    d_ver1 = g(dr, DC["Verify"])
    d_st2 = g(dr, DC["Trạng thái 2"])
    d_fix2 = g(dr, DC["Trạng thái dev fix 2"])
    d_ver2 = g(dr, DC["Verify 2"]) if DC["Verify 2"] is not None else ""

    entry = {
        "drow": di, "dma": dma, "mota": dmota,
        "d_st1": d_st1, "d_fix1": d_fix1, "d_ver1": d_ver1,
        "d_st2": d_st2, "d_fix2": d_fix2, "d_ver2": d_ver2,
        "has_verify2_col": DC["Verify 2"] is not None,
    }

    if di in match:
        pi, sim = match[di]
        pr = prow_by_idx[pi]
        entry.update({
            "prow": pi, "sim": sim,
            "pma": g(pr, PC["Mã TC"]),
            "pfile": g(pr, PC["Ảnh/vieo 1"]),
            "pfilecodes": pfilecodes[pi],
            "p_st1": g(pr, PC["Trạng thái"]),
            "p_fix1": g(pr, PC["Trạng thái dev fix"]),
            "p_st2": g(pr, PC["Trạng thái 2"]),
            "p_fix2": g(pr, PC["Trạng thái dev fix 2"]),
        })
        d1 = not cmp_status(d_st1, entry["p_st1"])
        d2 = not cmp_status(d_st2, entry["p_st2"])
        diffs = []
        if d1:
            diffs.append(f'"Trạng thái 1": DRIVE `{blank(d_st1)}` ≠ ĐỐI TÁC `{blank(entry["p_st1"])}`')
        if d2:
            diffs.append(f'"Trạng thái 2": DRIVE `{blank(d_st2)}` ≠ ĐỐI TÁC `{blank(entry["p_st2"])}`')
        entry["diffs"] = diffs
        if sim < SIM_FLAG:
            entry["verdict"] = "❔ Map không chắc"
        elif diffs:
            entry["verdict"] = "⚠️ Lệch"
        else:
            entry["verdict"] = "✅ Khớp"
    else:
        s, pi = fallback[di]
        entry.update({"prow": None, "sim": s, "best_global": pi,
                      "best_global_ma": g(prow_all_by_idx[pi], PC["Mã TC"]) if pi else "",
                      "best_global_tuan": g(prow_all_by_idx[pi], PC["Tuần"]) if pi else "",
                      "pma": "", "pfile": "", "pfilecodes": [],
                      "p_st1": "", "p_fix1": "", "p_st2": "", "p_fix2": "",
                      "diffs": [], "verdict": "🚫 Không tìm thấy bên đối tác"})

    codes = {c for c in ([dma] + list(entry.get("pfilecodes") or []) +
                         ([entry["pma"]] if entry.get("pma") else [])) if c}
    hit = sorted(codes & EXCL)
    entry["excl"] = hit
    rows_out.append(entry)

json.dump(rows_out, open(os.path.join(HERE, "result_w3.json"), "w"), ensure_ascii=False, indent=1)

vc = Counter(e["verdict"] for e in rows_out)
print("\n=== VERDICT ===", file=sys.stderr)
for k, v in vc.most_common():
    print(f"  {v:4d}  {k}", file=sys.stderr)
print(f"  TRỪ: {sum(1 for e in rows_out if e['excl'])}", file=sys.stderr)
sims = sorted(e["sim"] for e in rows_out)
print(f"\nsim min={sims[0]:.3f} p10={sims[len(sims)//10]:.3f} median={sims[len(sims)//2]:.3f}", file=sys.stderr)
print(f"sim <0.90: {sum(1 for s in sims if s < 0.90)}   <0.55: {sum(1 for s in sims if s < 0.55)}", file=sys.stderr)
print("\n=== ĐỐI TÁC 'Trạng thái' của các dòng đã map ===", file=sys.stderr)
for k, v in Counter(e["p_st1"] for e in rows_out if e["prow"]).most_common():
    print(f"  {v:4d}  {k!r}", file=sys.stderr)
