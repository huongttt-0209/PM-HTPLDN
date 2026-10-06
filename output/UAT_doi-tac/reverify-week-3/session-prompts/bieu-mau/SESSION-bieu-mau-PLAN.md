# Kế hoạch verify module "Biểu mẫu" (Thư viện Biểu mẫu/Hợp đồng) — tuần 3

> **Vì sao chia batch:** module Biểu mẫu có **42 case** (rows 80–121, tab `UAT_TGPL Doanh Nghiệp-tuần 3`).
> Chạy 42 case trong 1 session → vỡ context → chất lượng verify tụt (đúng bài học postmortem 16/07: "mù" khi chạy nhiều).
> → Chia **6 batch** theo **màn hình + tiền đề seed dùng chung** để mỗi session seed 1 lần, test nhiều case cùng surface.
> Mỗi batch **mở 1 session Claude Code MỚI**, dán nguyên khối file `SESSION-bieu-mau-batch{N}-prompt.md` tương ứng.

## SRS gốc của module
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md` (Nhóm VII — Thư viện Biểu mẫu/Hợp đồng).
Map sub-module → FR/UC:

| Sub-module (prefix mã TC) | FR / UC | Chức năng | Batch |
|---|---|---|:-:|
| QLTMBMHD | FR-VII-01 / UC92 | Quản lý **thư mục** biểu mẫu | 1 |
| TKTMBMHD | FR-VII-02 / UC93 | Tìm kiếm **thư mục** | 2 |
| CKTMBMHDLCTT | FR-VII-03 / UC94 | Công khai **thư mục** lên Cổng (hàng loạt) | 3 |
| QLBMHD | FR-VII-04 / UC95 | Quản lý **biểu mẫu** (tạo/upload/sửa/xem/preview) | 4 + 5 |
| TKBMHD | FR-VII-05 / UC96 | Tìm kiếm **biểu mẫu** | 2 |
| IBMHD | FR-VII-06 / UC98 | Import **biểu mẫu** hàng loạt | 6 |
| CKBMHDLCTT | FR-VII-07 / UC97 | Công khai **biểu mẫu** lên Cổng | 6 |

## 6 batch (tổng 42 case)

| Batch | Sub-module | # | Rows | Màn hình / tiền đề seed chung | File prompt |
|:-:|---|:-:|---|---|---|
| **1** | QLTMBMHD | 8 | 80–87 | Màn Quản lý thư mục. Seed: thư mục ở **Nháp / Ẩn / Công khai**, có/không có biểu mẫu bên trong | `SESSION-bieu-mau-batch1-prompt.md` |
| **2** | TKTMBMHD + TKBMHD | 6 | 88–91, 113–114 | 2 màn Tìm kiếm (thư mục & biểu mẫu) — cùng pattern: default dropdown, empty-state, xóa lọc, phân trang. Seed nhẹ | `SESSION-bieu-mau-batch2-prompt.md` |
| **3** | CKTMBMHDLCTT | 5 | 92–96 | Màn Công khai/Ẩn thư mục hàng loạt. Seed: thư mục Nháp/Ẩn/Công khai + có/không biểu mẫu | `SESSION-bieu-mau-batch3-prompt.md` |
| **4** | QLBMHD (tạo + upload) | 8 | 97–104 | Màn Quản lý biểu mẫu + form Thêm mới. Seed: 1 thư mục + **bộ file test** (đúng/sai định dạng, >20MB, hỏng) | `SESSION-bieu-mau-batch4-prompt.md` |
| **5** | QLBMHD (sửa/xem/preview/tải) | 8 | 105–112 | Màn chi tiết/sửa + preview/tải. Seed: **biểu mẫu đã có file** DOC/DOCX/XLS/XLSX ở Nháp/Ẩn/Công khai | `SESSION-bieu-mau-batch5-prompt.md` |
| **6** | IBMHD + CKBMHDLCTT | 7 | 116–121, 115 | Màn Import hàng loạt + Công khai biểu mẫu. Seed: mẫu Excel + nhiều file (có file lỗi) | `SESSION-bieu-mau-batch6-prompt.md` |

**Kích thước 8/6/5/8/8/7 — mỗi batch ≤8 case** → 1 session verify trọn không vỡ context.

## 🔴 Chạy song song được không?
- **Batch 1 & 3** đều thao tác trên **thư mục** (tạo/xóa/công khai/ẩn) → dễ giẫm chân nhau nếu chung dữ liệu. Nếu chạy song song, **mỗi batch tự seed thư mục RIÊNG, đặt tiền tố tên phân biệt** (vd `BM-B1-<ngày>` vs `BM-B3-<ngày>`), chỉ thao tác trên thư mục do chính mình seed.
- **Batch 4 & 5 & 6** đều thao tác trên **biểu mẫu** → tương tự, seed biểu mẫu riêng, tiền tố tên phân biệt.
- An toàn nhất: chạy **tuần tự** (hoặc 2–3 batch song song ở các sub-module khác nhau: 1+2, 4+... ). Batch 2 (tìm kiếm, read-only) an toàn chạy song song bất kỳ lúc nào.

## 🔴 Cụm lỗi xuyên batch — verify chéo, tránh log trùng / tránh bỏ sót gốc chung
Ghi rõ để tester các batch **đối chiếu nhau**, nghi 1 bug gốc chung thay vì log rời:

1. **Cụm "Ảnh đại diện / upload công khai từ chối ảnh hợp lệ"** — `QLBMHD_03` (b4) · `QLBMHD_11` (b4) · `QLBMHD_14` (b5) · `CKBMHDLCTT_01` (b6). Triệu chứng giống hệt: trường **Ảnh đại diện** (kiểu ảnh) báo "chỉ chấp nhận .doc/.docx/.xls/.xlsx". SRS `srs-fr-09:374` xác nhận công khai **cần ảnh đại diện** (là ảnh) → khả năng **1 bug FE** áp nhầm rule file-đính-kèm cho trường ảnh. Verify 1 lần kỹ, các case còn lại tham chiếu.
2. **Cụm "sau bulk action vẫn hiện dòng đã chọn + nút chức năng"** — `QLTMBMHD_19` (b1) · `QLTMBMHD_20` (b1) · `CKTMBMHDLCTT_07` (b3) · `CKTMBMHDLCTT_10` (b3). Khả năng **1 bug** (không clear selection sau bulk).
3. **Cụm "Xem trước → tải file thay vì preview"** — `QLBMHD_17` (b5) · `QLBMHD_18` (b5) · `QLBMHD_19` (b5). SRS `srs-fr-09:60` nêu "ưu tiên xem trực tuyến trước khi tải". Khả năng **1 bug** (preview chưa implement, fallback download).
4. **Cụm "thông báo nhân đôi (duplicate toast)"** — `QLTMBMHD_07` (b1) · `QLTMBMHD_19` (b1). ⚠️ **Vùng nóng postmortem 16/07.** BẮT BUỘC đo bằng `tools/toast-capture.js` (KHÔNG lọc trùng, đọc `innerText`, **đếm request song song số toast**). Lưu ý: case `TPDHSVV_02` tuần 3 đối tác báo "nhân đôi" nhưng **KHÔNG tái hiện** → đừng mặc định Open, phải đo.
5. **Cụm "thông báo không giống thiết kế" (wording)** — rất nhiều case (`QLBMHD_06/07/08/09`, `TKTMBMHD_06`, `CKTMBMHDLCTT_08/11`, `QLTMBMHD_19/20`, `TKBMHD_04`…). **Quy tắc verdict:** SRS `srs-fr-09` §Error Handling có ghi **mã + Message chuẩn** (vd `ERR-TM-01 "Thư mục '{tên}' đã tồn tại trong đơn vị"`, `ERR-CK-01`, …). App sai **đúng chữ SRS quy định** → `Open`; SRS chỉ nêu chung/không có message chuẩn → `BA confirm`. Mở đúng dòng SRS trước khi chốt (§3-Step Verify, describe-not-prescribe).

## Verdict wording — mẹo nhanh (theo protocol, KHÔNG thay bảng Verdict)
- Nút hiển thị sai theo state → SRS `SCR-VII-01:615` + `SCR-VII-02` quy định rõ điều kiện hiện nút → thường `Open`.
- Thiếu cột/trường so thiết kế → SRS §Inputs/§Thành phần màn hình quy định rõ → `Open`; thiết kế đối tác thêm cột SRS không nêu → `BA confirm`.
- Message wording → xem cụm 5 ở trên.
- **CẤM** kết luận từ SRS suông — mọi verdict phải kèm **artifact real-data** (ảnh full-res / toast+network của chính thao tác) chạy trên data đã seed (§GATE).

## Output — mỗi batch ghi FILE RIÊNG (tránh clobber khi song song), merge cuối
- **Verdict → Google Sheet NGAY** sau mỗi case: `python3 tools/sheet_write.py --mode verify1 --row N --ma-tc <MÃ> --status <Open|Reject|BA confirm|""> --evidence <path> --condition-table <file.md> --note-file <note.txt>` (bug tĩnh: `--static-bug "<lý do>"`; ô TRỐNG: `--blocker-category A-F`).
- **Bug Open** → `bug-reports/bug-report-bieu-mau-batch{N}.md` (template `output/template/bug-report-template.md`, 6 sections; Bug ID = `BUG-<mã TC>`) + ≥1 screenshot `bug-reports/image/` (tên theo Bug ID).
- **BA confirm** → `ba-confirmation-needed-week-3-bieu-mau-batch{N}.md`.
- **Reject / BA confirm** → evidence audit vào `reverify-audit/<mã TC>/`.
- **Bảng đối chiếu điều kiện** từng case → `cond/<mã TC>.md`.
- **Cuối cùng (1 session, tuần tự):** merge 6 file `bug-report-bieu-mau-batch{N}.md` → `bug-reports/bug-report-bieu-mau.md`; merge BA → `ba-confirmation-needed-week-3.md`.

> ⚠️ **Không ghi vào `Pass-bug-report-UAT-tuan-3.md`** — file đó đang là report module **Vụ việc HTPL** (14 case). Trộn 42 bug Biểu mẫu vào sẽ lẫn module + clobber khi 6 batch chạy song song. Dùng file riêng `bug-report-bieu-mau*.md` như trên.

## Tài khoản dùng chung 6 batch (login đúng vai trò bug, KHÔNG dùng admin ra verdict)
- Chính: **CB Nghiệp vụ** — `cbnv_tw` / `cbnv_dp` (An Giang) / `cbnv_hn` (Sở Tư pháp Hà Nội) — mật khẩu `Test@1234`.
- Case kiểm "nút KHÔNG hiện cho đơn vị khác" → cần 2 account khác đơn vị (vd `cbnv_tw` sở hữu thư mục vs `cbnv_dp` xem).
- `admin` chỉ dùng seed/điều tra, **không ra verdict** (quyền rộng che lỗi phân quyền — protocol §Nguyên tắc 3).
- Thiếu account/data/state → **TỰ SEED** (protocol §Nguyên tắc 4), ghi lại vào `input/input.md`.
