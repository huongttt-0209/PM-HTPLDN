# Đối chiếu điều kiện — QLBMHD_03 (Form Thêm biểu mẫu: Cơ quan ban hành + Tệp đính kèm định dạng)

Loại bug: **Form field presence + validation định dạng file.** Case gộp 2 lỗi con:
- (a) Thiếu trường "Cơ quan ban hành" khi bật Công khai.
- (b) Tệp đính kèm cho phép sai định dạng (.jpg/.png/.gif).

Verify đúng vai trò đối tác (**CB Nghiệp vụ**), thao tác thật trên form Thêm biểu mẫu, bật switch Công khai.

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_03.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | CB Nghiệp vụ thêm biểu mẫu | `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW) | Không |
| Màn hình / state | Form Thêm mới (`/bieu-mau/them-moi`), switch Công khai ON | Đúng form, đã bật switch Công khai ON (aria-checked=true, label "Bật") | Không |
| Trường đang xét (b) | "Tệp đính kèm" cho biểu mẫu công khai (thiết kế chỉ PDF/DOC/DOCX/XLS/XLSX) = File đính kèm công khai | Kiểm accept của File đính kèm công khai (input[type=file]) + hint text | Không |

**0 GAP.** Tái hiện đúng vai trò + đúng state (switch Công khai ON) + đúng trường (File đính kèm công khai, phân biệt với Ảnh đại diện).

## Cổng 3 — SRS SCR-VII-02 vs web (2 lỗi con)

**(a) Trường "Cơ quan ban hành":**
- SRS yêu cầu: SCR-VII-02 #21 `srs-fr-09:658` — "form / Cơ quan ban hành / text (read-only) / Auto = đơn vị tài khoản / khi tạo/sửa `[STT12]`"; Inputs #14 `srs-fr-09:304` (Y, auto, read-only).
- Web: KHÔNG có trường/label "Cơ quan ban hành" (cả switch OFF lẫn ON). `hasCoQuanBanHanh=false`. Label form: Thư mục · Tên biểu mẫu · Lĩnh vực · Loại hình · Mô tả · Thứ tự hiển thị · File biểu mẫu · Ảnh đại diện · Mô tả công khai · File đính kèm công khai.
- → **Open** (thiếu trường read-only bắt buộc theo SRS).

**(b) File đính kèm công khai — định dạng:**
- SRS yêu cầu: SCR-VII-02 #19 `srs-fr-09:656` + Inputs #13 `srs-fr-09:303` — "PDF/DOC/DOCX/XLS/XLSX, max 20MB/file" (KHÔNG có ảnh).
- Web: accept=`.pdf,.doc,.docx,.xls,.xlsx`; hint "Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Tối đa 20MB/tệp" — KHÔNG còn .jpg/.png/.gif. (.jpg/.png/.gif chỉ nhận ở Ảnh đại diện — đúng SRS #17 dòng 654.)
- → **Reject** (không tái hiện — build hiện tại đã đúng định dạng).

## Verdict

- (a) → `Open` (BUG-QLBMHD_03).
- (b) → `Reject`: File đính kèm công khai chỉ nhận PDF/DOC/DOCX/XLS/XLSX. Lỗi "cho phép ảnh" đối tác báo (build cũ) không tái hiện → đối tác kiểm tra lại.
- **Verdict tổng (≥1 ý Open → Open): `Open`.**

Evidence: [`../bug-reports/bieu-mau/image/BUG-QLBMHD_03-form-congkhai.png`](../bug-reports/bieu-mau/image/BUG-QLBMHD_03-form-congkhai.png) + [`../reverify-audit/QLBMHD_03/dom-evidence.json`](../reverify-audit/QLBMHD_03/dom-evidence.json).
