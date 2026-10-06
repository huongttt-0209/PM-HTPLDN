#!/usr/bin/env python3
"""READ-ONLY: xuất bảng đối chiếu tuần 3 — BẢN SỬA, so đủ 4 cặp cột.
Không đụng Google Sheets.
"""
import json, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "audit_w3.json")))
OUT = ("/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/"
       "reverify-week-3/DOI-CHIEU-TRANG-THAI-BUG-tuan-3.md")

AXIS_LABEL = {
    "st1": ("Trạng thái 1", "Trạng thái"),
    "st2": ("Trạng thái 2", "Trạng thái 2"),
    "fix1": ("Trạng thái dev fix 1", "Trạng thái dev fix"),
    "fix2": ("Trạng thái dev fix 2", "Trạng thái dev fix 2"),
}
DKEY = {"st1": "d_st1", "st2": "d_st2", "fix1": "d_fix1", "fix2": "d_fix2"}
PKEY = {"st1": "p_st1", "st2": "p_st2", "fix1": "p_fix1", "fix2": "p_fix2"}


def esc(s, n=None):
    s = (s or "").replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()
    s = " ".join(s.split())
    if n and len(s) > n:
        s = s[:n - 1] + "…"
    return s


def b(s):
    s = esc(s)
    return s if s else "(trống)"


CLOSED_D = {"pass", "resolved", "reject"}


def bucket(e):
    """Phân loại nghiệp vụ theo cặp (DRIVE dev fix1 + Verify) vs (ĐỐI TÁC dev fix)."""
    if not e["axes"]:
        return "nomap"
    import re
    pf = e["p_fix1"].strip().lower().replace(" ", "")
    partner_open = pf.startswith("reopen")
    if partner_open:
        df = e["d_fix1"].strip().lower()
        if "reopen" in df:
            return "R1"   # DRIVE đã ghi nhận reopen + dev done, đối tác chưa cập nhật
        if "reject" in df:
            return "R2"   # DRIVE khẳng định không phải lỗi, đối tác mở lại -> đối đầu
        return "R3"       # DRIVE chưa hề ghi nhận đối tác reopen
    # đối tác coi là đóng
    df = e["d_fix1"].strip().lower()
    dv = e["d_ver1"].strip().lower()
    pf2 = e["p_fix1"].strip().lower().replace(" ", "")
    if "reject" in df and "resolv" in dv and pf2.startswith("reso"):
        return "CONV"     # quy ước Reject(dev fix) + Resolved(Verify) <-> Resoved
    if "reject" in df and "reject" in dv and pf2.startswith("reso"):
        return "LABEL"    # cùng kết luận đóng, DRIVE ghi Reject / đối tác Resoved
    return "OK"


# ---------- tính verdict mới ----------
for e in R:
    if not e["axes"]:
        e["diffs2"] = []
        e["bucket"] = "nomap"
        continue
    diffs = []
    for k in ["st1", "st2", "fix1", "fix2"]:
        v, why = e["axes"][k]
        if v != "same":
            dl, pl = AXIS_LABEL[k]
            diffs.append(f'`{dl}`: DRIVE `{b(e[DKEY[k]])}` ≠ ĐỐI TÁC `{b(e[PKEY[k]])}`')
    e["diffs2"] = diffs
    e["bucket"] = bucket(e)
    if e["verdict"] == "❔ Map không chắc":
        pass
    elif diffs:
        e["verdict"] = "⚠️ Lệch"
    elif e["verdict"] != "🚫 Không tìm thấy bên đối tác":
        e["verdict"] = "✅ Khớp"

c = Counter(e["verdict"] for e in R)
bk = Counter(e["bucket"] for e in R)
n_excl = sum(1 for e in R if e["excl"])
n_reopen = bk["R1"] + bk["R2"] + bk["R3"]

ORDER = {"⚠️ Lệch": 0, "🚫 Không tìm thấy bên đối tác": 1,
         "❔ Map không chắc": 2, "✅ Khớp": 3}
BORDER = {"R2": 0, "R3": 1, "R1": 2, "LABEL": 3, "OK": 4, "CONV": 5, "nomap": 6}


def drive_status(e):
    v2 = "(không có cột Verify 2)" if not e["has_verify2_col"] else b(e["d_ver2"])
    return (f'V1: {b(e["d_st1"])} → {b(e["d_fix1"])} / {b(e["d_ver1"])}<br>'
            f'V2: {b(e["d_st2"])} → {b(e["d_fix2"])} / {v2}')


def partner_status(e):
    if not e["prow"]:
        return "(không tìm thấy)"
    return (f'V1: {b(e["p_st1"])} → {b(e["p_fix1"])}<br>'
            f'V2: {b(e["p_st2"])} → {b(e["p_fix2"])}')


def matc(e):
    s = e["dma"]
    if e["prow"] and e["pma"] and e["pma"] != e["dma"]:
        s += f' (đối tác `{e["pma"]}`)'
    return esc(s)


def khop(e):
    v = e["verdict"]
    flag = "🔴 " if e["bucket"] in ("R1", "R2", "R3") else ""
    if v == "⚠️ Lệch":
        return flag + v + " — " + "; ".join(e["diffs2"])
    if v == "❔ Map không chắc":
        x = f'sim={e["sim"]:.3f}; đối tác row {e["prow"]} mã `{e["pma"]}`'
        if e["diffs2"]:
            x += "; " + "; ".join(e["diffs2"])
        return flag + v + " — " + x
    if v == "🚫 Không tìm thấy bên đối tác":
        return (v + f' — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất '
                    f'sim={e["sim"]:.3f} là `{esc(e.get("best_global_ma"))}` '
                    f'({esc(e.get("best_global_tuan"))}) nhưng khác module/khác case')
    return flag + v


HDR = ("| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE "
       "| Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |\n"
       "|---|---|---|---|---|---|---|\n")


def line(e):
    return (f'| {e["drow"]} | `{matc(e)}` | {esc(e["mota"], 90)} | {drive_status(e)} '
            f'| {partner_status(e)} | {khop(e)} | '
            f'{"⛔ TRỪ (" + ", ".join(e["excl"]) + ")" if e["excl"] else "–"} |\n')


L = []
L.append("# Đối chiếu trạng thái bug — TUẦN 3 (DRIVE ↔ ĐỐI TÁC)\n\n")
L.append(f'**{len(R)} bug · {c["✅ Khớp"]} khớp · {c["⚠️ Lệch"]} lệch · '
         f'{c["🚫 Không tìm thấy bên đối tác"]} không tìm thấy · {n_excl} trừ** '
         f'(thêm {c["❔ Map không chắc"]} dòng ❔ map không chắc)\n\n')
L.append(f"> 🔴 **{n_reopen} dòng đối tác đang để `Reopent` trong khi DRIVE coi như đã xong.** "
         "Đây là nhóm cần xử trước.\n\n")
L.append("> **Chỉ đọc.** Không ghi/sửa bất kỳ ô nào trên 2 spreadsheet.\n\n")

L.append("## ⚠️ Đính chính so với bản đầu\n\n")
L.append("Bản đầu chỉ so 2 cặp `Trạng thái 1 ↔ Trạng thái` và `Trạng thái 2 ↔ Trạng thái 2` "
         "đúng như đặc tả nhận được, và ra `275 khớp`. **Con số đó sai lệch bản chất.** "
         "Lý do: bên DRIVE `Trạng thái 1` = `Fail` ở 309/309 dòng và `Trạng thái 2` trống ở 309/309 dòng "
         "— hai cột đó gần như là hằng số, so chúng không phát hiện được gì. "
         "Toàn bộ tín hiệu thật nằm ở cột `Trạng thái dev fix` và `Verify`.\n\n")
L.append("Ví dụ do người kiểm bắt được: **`QLBMHD_03`** — DRIVE `Reopen, dev done` + `Verify = Pass`, "
         "đối tác `Reopent`. Bản đầu xếp ✅ Khớp vì `Fail = Fail`. Bản này xếp ⚠️ Lệch.\n\n")
L.append("Bản này so **đủ 4 cặp**: `Trạng thái 1↔Trạng thái`, `Trạng thái 2↔Trạng thái 2`, "
         "`Trạng thái dev fix 1↔Trạng thái dev fix`, `Trạng thái dev fix 2↔Trạng thái dev fix 2`.\n\n")
L.append("---\n\n")

L.append("## Bức tranh trục `dev fix` vòng 1 — 299 dòng map được\n\n")
L.append("| Số dòng | DRIVE `dev fix 1` | DRIVE `Verify` | ĐỐI TÁC `dev fix` | Đọc là gì |\n|---|---|---|---|---|\n")
L.append("| 182 | `dev done` | `Pass` | `dev done` | ✅ Hai bên khớp hoàn toàn |\n")
L.append("| 45 | `Reject` | `Resolved` | `Resoved` | ⚠️ Tính là lệch khi so chặt từng cột (`Reject` ≠ `Resoved`), "
         "nhưng đây là **quy ước đã dùng** — `Reject` ở cột dev fix + `Resolved` ở cột Verify ≡ `Resoved` bên đối tác. "
         "Về thực chất hai bên đồng ý. Xem mục riêng cuối bảng lệch. |\n")
L.append("| 30 | `Reject` | `Reject` | `Resoved` | ⚠️ Lệch nhãn — cùng kết luận **đóng**, nhưng DRIVE ghi `Reject` còn đối tác đã chuyển `Resoved` |\n")
L.append("| 19 | `Reopen, dev done` | `Pass` | `Reopent` | 🔴 DRIVE đã ghi nhận reopen + dev fix lại + QA verify Pass; **đối tác chưa cập nhật** ← `QLBMHD_03` ở nhóm này |\n")
L.append("| 18 | `Reject` | `Reject` | `Reopent` | 🔴 **Đối đầu thật** — DRIVE khẳng định không phải lỗi, đối tác mở lại |\n")
L.append("| 3 | `dev done` | `Pass` | `Reopent` | 🔴 DRIVE **chưa hề ghi nhận** việc đối tác mở lại |\n")
L.append("| 2 | `Reject` | `Reject` | `Reject` | ✅ Khớp |\n\n")
L.append(f"**Cộng 🔴 = {n_reopen} dòng** đối tác còn để `Reopent` trong khi DRIVE coi như xong.\n\n")

L.append("## Hai trục vòng 2\n\n")
L.append("- `Trạng thái 2`: 22 dòng lệch — DRIVE trống, đối tác đã chấm (20 `Pass`, 2 `Fail`).\n")
L.append("- `Trạng thái dev fix 2`: 16 dòng lệch — DRIVE trống, đối tác ghi `Resoved`.\n")
L.append("- Cả hai đều là **DRIVE chưa chấm vòng 2**, không phải hai bên bất đồng.\n\n")
L.append("---\n\n")

L.append("## Nguồn & cách map\n\n")
L.append("- DRIVE `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` tab `UAT_TGPL Doanh Nghiệp-tuần 3` — 309 dòng.\n")
L.append("- ĐỐI TÁC `1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c` tab `UAT_TGPL Doanh Nghiệp` (gid 799081340) — 1671 dòng, lọc `Tuần` = `Tuần 3` → 961 dòng.\n")
L.append("- Loại trừ: `reverify-week-4/DANH-SACH-BA-CONFIRM-va-COMMIT-SAU-MOC.md` — 30 mã, **không mã nào thuộc tuần 3** → 0 dòng trừ.\n")
L.append("- Map bằng nội dung `Mô tả + Kết quả mong đợi` (chuẩn hoá khoảng trắng + lowercase, "
         "`difflib.SequenceMatcher`, chỉ trong cùng tiền tố module, ghép 1-1 theo similarity giảm dần). "
         "Khoá phụ: mã TC parse từ tên file cột `Ảnh/vieo 1` bên đối tác. "
         "Không dùng chuỗi Mã TC làm khoá chính, không dùng `id-crosswalk.csv`.\n")
L.append("- **0 dòng lệch mã TC** — 299 dòng map được đều trùng `Mã TC` hai bên. Tuần 3 không bị đánh số lại như tuần 1.\n")
L.append("- Tab tuần 3 bên DRIVE **không có cột `Verify 2`** → ghi `(không có cột Verify 2)`, phân biệt với ô rỗng thật.\n")
L.append("- So trạng thái theo **tập token** (tách dấu phẩy), chuẩn hoá chính tả khi so: "
         "`Resoved`→`resolved`, `Reopent`→`reopen`. Dữ liệu gốc giữ nguyên văn trong bảng.\n")
L.append("- `Reopen, dev done` vs `Reopent` → **lệch** (DRIVE có thêm token `dev done`), "
         "không gộp thành khớp.\n\n")
L.append("---\n\n")

SUB = [
    ("R2", "🔴 Đối đầu — DRIVE `Reject`, đối tác `Reopent`",
     "DRIVE khẳng định không phải lỗi; đối tác không chấp nhận và mở lại. Cần trả lời đối tác."),
    ("R3", "🔴 DRIVE chưa ghi nhận đối tác mở lại",
     "DRIVE ghi `dev done` + `Verify Pass`, không có token `Reopen` nào — tức phản hồi reopen của đối tác chưa vào sheet DRIVE."),
    ("R1", "🔴 DRIVE đã fix lại, đối tác chưa cập nhật",
     "DRIVE `Reopen, dev done` + `Verify Pass`. Cần báo đối tác đổi trạng thái."),
    ("LABEL", "⚠️ Lệch nhãn — DRIVE `Reject`, đối tác đã chuyển `Resoved`",
     "Hai bên cùng coi là **đóng**, chỉ khác chữ. DRIVE có thể cân nhắc đồng bộ nhãn."),
    ("OK", "⚠️ Lệch còn lại — hai bên cùng coi là đóng",
     "Phần lớn là DRIVE chưa chấm vòng 2 (`Trạng thái 2` / `dev fix 2` trống trong khi đối tác đã điền)."),
    ("CONV", "⚠️ Lệch hình thức theo quy ước `Reject` + `Verify Resolved` ↔ `Resoved`",
     "**Nhóm này gần như chắc chắn KHÔNG cần xử.** So chặt từng cột thì `Reject` ≠ `Resoved` nên bị đánh ⚠️, "
     "nhưng cột `Verify` bên DRIVE ghi `Resolved` — trùng kết luận với `Resoved` bên đối tác. "
     "Đây là quy ước đã dùng nhất quán. Liệt kê ra để người kiểm tự quyết, không tự gộp thành ✅."),
]

rows = sorted(R, key=lambda e: (ORDER[e["verdict"]], BORDER[e["bucket"]], e["drow"]))

L.append(f'## ⚠️ Lệch — {c["⚠️ Lệch"]} dòng\n\n')
for bkey, title, desc in SUB:
    sel = [e for e in rows if e["verdict"] == "⚠️ Lệch" and e["bucket"] == bkey]
    if not sel:
        continue
    L.append(f"### {title} — {len(sel)} dòng\n\n{desc}\n\n")
    L.append(HDR)
    for e in sel:
        L.append(line(e))
    L.append("\n")

for tag, note in [
    ("🚫 Không tìm thấy bên đối tác",
     "9/10 là mã QA tự mở (`_OOS_`, `_LINHVUC`, `_CONGKHAI`) — đúng như dự kiến. "
     "Dòng còn lại `QLHSDNHTCP_19`: module `QLHSDNHTCP` bên đối tác dừng ở `_19` = "
     "\"Chọn số bản ghi mỗi trang\", không có case \"Sắp xếp theo cột\". "
     "Các dòng similarity cao đều là module khác (mô tả chung chung trùng chữ)."),
    ("❔ Map không chắc",
     "Trùng `Mã TC` + trùng tên file ảnh hai bên; similarity thấp chỉ vì một bên đã sửa "
     "text `Kết quả mong đợi`. Nhiều khả năng map đúng, vẫn để ❔ để người kiểm mắt."),
    ("✅ Khớp", "Khớp trên cả 4 cặp cột."),
]:
    sel = [e for e in rows if e["verdict"] == tag]
    L.append(f"## {tag} — {len(sel)} dòng\n\n{note}\n\n")
    L.append(HDR)
    for e in sel:
        L.append(line(e))
    L.append("\n")

open(OUT, "w", encoding="utf-8").writelines(L)
json.dump(R, open(os.path.join(HERE, "audit_w3.json"), "w"), ensure_ascii=False, indent=1)
print("written ->", OUT)
print(f"{len(R)} bug · {c['✅ Khớp']} khớp · {c['⚠️ Lệch']} lệch · "
      f"{c['🚫 Không tìm thấy bên đối tác']} không tìm thấy · {n_excl} trừ · "
      f"{c['❔ Map không chắc']} map không chắc")
print("bucket:", dict(bk), "| 🔴 reopen =", n_reopen)
