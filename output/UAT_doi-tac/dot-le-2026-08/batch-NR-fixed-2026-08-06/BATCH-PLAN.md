# BATCH PLAN — `Dopai = N/R` + `Trạng thái dev fix = Fixed`

Lọc ngày 2026-08-06, tab `bug` (295 case) → **39 case** khớp bộ lọc.
Tách theo cột `Trạng thái` vì 2 nhóm cần 2 loại việc khác hẳn:

| Nhóm | Điều kiện | Số case | Việc đúng |
|---|---|:-:|---|
| **A** | `Trạng thái = Fail` | 18 | verify bug — nhưng 3 case bị chặn ⇒ **15 chạy được** |
| **B** | `Trạng thái = N/R` | 21 | **KHÔNG** dùng flow 04 — chạy test case tươi |

🔴 **`Kết quả thực tế` rỗng ở cả 39/39 case.** Triệu chứng của nhóm A nằm ở cột **`TKM phản hồi lần 1`**.
Ai chỉ đọc `Kết quả thực tế` sẽ tưởng không có gì để verify.

---

## Nhóm A — 15 case verify được, chia 3 batch × 5

Chia theo **module + cụm triệu chứng** để 1 lần đăng nhập / 1 màn hình phủ nhiều case.

### Batch A1 — QLHSPLDN (Hồ sơ pháp lý DN) · 5 case · 1 màn hình

| row | Mã TC | Ảnh | Triệu chứng (TKM) |
|---|---|:-:|---|
| 293 | QLHSPLDN_11 | ✔ | Không có trường thông tin tìm kiếm trên màn hình |
| 294 | QLHSPLDN_12 | – | Không có trường thông tin tìm kiếm trên màn hình |
| 295 | QLHSPLDN_13 | – | Không có trường thông tin tìm kiếm trên màn hình |
| 296 | QLHSPLDN_14 | ✔ | Màn hình không có nút chức năng |
| 297 | QLHSPLDN_15 | – | Màn hình không có nút chức năng |

⚠️ Tên tệp ảnh **lệch 1 so với Mã TC**: row 293 (`_11`) đính `QLHSPLDN_12.jpg`, row 296 (`_14`) đính
`QLHSPLDN_15.jpg`. Kiểm ảnh mô tả case nào rồi mới dùng — đừng mặc định ảnh khớp mã dòng.

### Batch A2 — Đào tạo + Bài giảng · 5 case

| row | Mã TC | Ảnh | Triệu chứng (TKM) |
|---|---|:-:|---|
| 10 | KTDGKQHT_05 | ✔ | Màn danh sách không hiện mã học viên, nhưng nhập Excel điểm danh lại bắt buộc có mã học viên |
| 11 | KTDGKQHT_10 | – | Màn hình không có nút chức năng |
| 12 | QLKTLBG_18 | ✔ | Màn hình không có nút chức năng — **đã verify 2026-08-05 (đợt chạy thử), có kết quả sẵn** |
| 13 | QLKTLBG_19 | – | Màn hình không có nút chức năng |
| 14 | QLKTLBG_20 | – | Màn hình không có nút chức năng |

Row 10 có cột `Loại vấn đề` = *"nếu thêm cột MHV có đc ko"* — là **câu hỏi**, không phải khẳng định lỗi
⇒ nhiều khả năng rơi nhánh **cần BA**, không phải Pass/Reopen.

### Batch A3 — lẻ, mỗi module 1–2 case

| row | Mã TC | Ảnh | Triệu chứng (TKM) |
|---|---|:-:|---|
| 301 | QLTLPLCVV_22 | ✔ | Màn hình không có chức năng |
| 302 | QLTLPLCVV_23 | ✔ | Màn hình không có chức năng |
| 149 | QLDMTCTV_12 | ✔ | Màn hình không có nút chức năng |
| 35 | DKTGMLTVV_13 | ✔ | Màn không có button "Gửi đăng ký", chỉ có "Lưu" — nghi do đặt tên nút |
| 288 | QLNDTVVCG_38 | ✔ | Popup *"Phân công hàng loạt chưa được hỗ trợ"* |

⚠️ Tên tệp lệch 1: row 301 (`_22`) đính `QLTLPLCVV_23.jpg`, row 302 (`_23`) đính `QLTLPLCVV_24.jpg`.

### Không xếp batch — 3 case bị chặn, gán nhãn Fail nhầm

| row | Mã TC | TKM ghi | Cần làm trước |
|---|---|---|---|
| 73 | QLHSDNHTCP_15 | *Chưa có dữ liệu test, a/c bổ sung dữ liệu giúp e* | seed dữ liệu |
| 285 | QLNDTVVCG_19 | *chưa có dữ liệu test* | seed dữ liệu |
| 169 | QLDKTK_10 | *sau khi tc QLDKTK_01 được fix sẽ test* | chờ QLDKTK_01 |

---

## Nhóm B — 21 case `Trạng thái = N/R`: KHÔNG chạy bằng flow 04

Không ảnh · `Kết quả thực tế` rỗng · 20/21 không có ghi chú TKM. Row 343 ghi rõ lý do:
*"Chưa thực hiện được do uc GKQTHCTHTPL_01 lỗi"*. Đây là **test case chưa chạy**, không có bug nào để verify.

- `QLHDTVVCG` ×17 — rows 308, 309, 310, 311, 314, 315, 319, 322, 323, 324, 325, 327, 328, 329, 330, 332, 333
- `THBCTHCT` ×3 — rows 343, 344, 345
- `TPDBCKQTHCT` ×1 — row 341

17/21 cùng module `QLHDTVVCG` (Hợp đồng Tư vấn) ⇒ nhiều khả năng cả module không vào được ở vòng của đối tác.
Việc đúng: **chạy test case tươi** đối chiếu cột `Kết quả mong đợi`, và kiểm trước xem module đã vào được chưa.

---

## Prompt cho từng batch

Đổi dòng `Phạm vi:` theo bảng trên, các dòng khác giữ nguyên.

```
Áp dụng @flows/04-verify-bug-dev-fix-khong-ho-so.md
- Bảng: https://docs.google.com/spreadsheets/d/1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s | Tab: bug
- Ô mã case: "Mã TC" | Ô trạng thái dev: "Trạng thái dev fix" + "Dopai" (chỉ ĐỌC)
  | Ô kết quả QA: "<...>" | Ô note: "<...>"
- Từ vựng: đã fix="Fixed" · Pass="<...>" · Reopen="<...>" · không phải lỗi="<...>" · cần BA="<...>"
- 🔴 Cột "Kết quả thực tế" RỖNG ở mọi case của đợt này. Triệu chứng đối tác báo nằm ở cột
  "TKM phản hồi lần 1" — đọc cột đó thay cho "Kết quả thực tế".
- Đặc tả: Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/
  | Môi trường + tài khoản: output/UAT_doi-tac/input/input.md
- MÔI TRƯỜNG VERIFY: https://18.143.165.120.nip.io
- Bug report: output/UAT_doi-tac/batch-NR-fixed-2026-08-06/<batch>/bug-report.md
  | Ảnh: output/UAT_doi-tac/batch-NR-fixed-2026-08-06/<batch>/image/
- File gửi BA: output/UAT_doi-tac/batch-NR-fixed-2026-08-06/<batch>/cau-hoi-BA.md
- Thư mục tiêu chí: output/UAT_doi-tac/batch-NR-fixed-2026-08-06/<batch>/tieuchi/
- Công cụ: tải bằng chứng=cd output/UAT_doi-tac && UAT_TAB=bug python3 tools/fetch_evidence.py --row <N>
- Phạm vi: <dán danh sách "Mã TC (row N)" của batch>
```

Slot `Ô kết quả QA` · `Ô note` · `Từ vựng` phải điền trước khi chạy thật — flow 04 dừng hỏi nếu thiếu.
