# Re-verify vòng 2 — QLDMTCTV_06 (dòng 319, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`, đơn vị Cục Bổ trợ tư pháp – Bộ Tư pháp). Đăng nhập KHÔNG hỏi OTP trên bản dựng này.
**Verdict:** ✅ Pass

---

## Triệu chứng gốc cần kiểm

"Biểu mẫu **Thêm mới** thiếu trường Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm."

## Nhật ký đo

### 13:46 — Mở biểu mẫu Thêm mới
Menu **Mạng lưới Tư vấn viên → Tổ chức tư vấn** → nút **+ Thêm mới** → `/chuyen-gia-tvv/to-chuc/tao-moi`, tiêu đề "Thêm mới Tổ chức tư vấn".

Đọc toàn bộ nhãn trên biểu mẫu (`.ant-form-item-label label`), được 15 nhãn:

> Tên tổ chức · Loại hình · Người đại diện · Chức vụ người đại diện · Số Giấy ĐKHĐ Sở TP · Ngày cấp Giấy đăng ký hành nghề · Lĩnh vực pháp luật · Số lao động · Địa chỉ trụ sở · Số điện thoại · Email · Website · **Số quyết định công bố** · **Ngày quyết định công bố** · Ghi chú

⇒ 2 trong 3 trường đối tác báo thiếu đã có mặt. Trường thứ 3 nằm ở nhóm "File đính kèm".

### 13:47 — Mở nhóm "Công bố" và "File đính kèm"
Bấm tiêu đề nhóm **Công bố** → panel bung ra cao 119px, chứa đúng 2 ô: "Số quyết định công bố" (ô nhập chữ, có biểu tượng trợ giúp) và "Ngày quyết định công bố" (ô chọn ngày có biểu tượng lịch).
Bấm tiêu đề nhóm **File đính kèm** → panel bung ra cao 244px, chứa vùng kéo thả: **"Kéo thả hoặc nhấp để chọn tệp đính kèm — Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp."**
`input[type=file]` có `accept=".pdf,.doc,.docx,.xls,.xlsx"`, `multiple=true`.

Ảnh: `image/QLDMTCTV_06-v2-02-them-moi-mo-het-6-nhom-du-3-truong-cong-bo-va-tep.png` (đã mở đọc: thấy ô "Số quyết định công bố", ô "Ngày quyết định công bố", vùng kéo thả tệp, ô "Ghi chú", 2 nút Hủy / Lưu).

⇒ **Cả 3 trường đối tác báo thiếu đều đã hiển thị.**

### 13:57–13:59 — Phép thử quyết định: nhập thật + lưu thật
Không dừng ở quan sát; tạo hẳn 1 tổ chức mới qua biểu mẫu này với 3 trường đó được điền:
- Tên tổ chức `Cong ty Luat QA Reverify V2 A2 Cong bo` · Loại hình `Công ty Luật` · Người đại diện `Nguyen Van Cong Bo` · Chức vụ `Giam doc` · Số Giấy ĐKHĐ `DKHD-QA-A2-0804` · Ngày cấp `01/01/2025` · Lĩnh vực `Thương mại` · Địa chỉ `So 1 Tran Phu, Ha Noi`
- **Số quyết định công bố** `QD-QA-A2-0804/2026`
- **Ngày quyết định công bố** `04/08/2026`
- **Tệp đính kèm** `qd-cong-bo-alpha-reverify-v2.pdf` (237 B) — sau khi chọn, danh sách tệp hiện tên + dung lượng + nút **Xem** / **Xóa**.

Ảnh trước khi lưu: `image/QLDMTCTV_06-v2-03-nhap-3-truong-cong-bo-va-dinh-kem-tep-truoc-khi-luu.png` (đã mở đọc).

Bấm **Lưu** (bộ bắt thông báo dùng chung đã cài trước, tự kiểm `soObserverDangSong = 1`):
- **1 request** `POST /api/v1/to-chuc-tu-vans` · **1 thông báo** "Tạo Tổ chức tư vấn thành công". Không có thông báo lặp.
- Bản ghi sinh ra: **TC-BTP-TW-0012**, trạng thái `MOI_DANG_KY`.

Đọc lại bản ghi qua API trong phiên (`GET /api/v1/to-chuc-tu-vans/0b4fc601-…`):
```
soQdCongBo    = "QD-QA-A2-0804/2026"
ngayQdCongBo  = "2026-08-04"
fileDinhKem   = [{ tenFile: "qd-cong-bo-alpha-reverify-v2.pdf", dungLuong: 237,
                   loaiFile: "application/pdf", trangThaiQuet: "SACH" }]
```
⇒ 3 trường không chỉ hiển thị mà **lưu xuống đúng**.

### Đối chiếu đặc tả
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`:
- dòng 1692 — "Số quyết định công bố | ô văn bản | Tùy chọn"
- dòng 1693 — "Ngày quyết định công bố | bộ chọn ngày | Tùy chọn"
- dòng 1694 — "File đính kèm | tải nhiều file | Định dạng PDF/DOC/DOCX/XLS/XLSX, tối đa 20MB/file. Quét virus"

Cả 3 khớp đúng, kể cả bộ định dạng và giới hạn dung lượng ghi trên vùng kéo thả.

### Kết luận
Biểu mẫu Thêm mới đã có đủ 3 trường đối tác báo thiếu, nhập được và lưu được ⇒ **Pass**.

### Dữ liệu để lại trên môi trường
`TC-BTP-TW-0012` — "Cong ty Luat QA Reverify V2 A2 Cong bo" (Mới đăng ký, có 1 tệp PDF + Số/Ngày QĐ công bố). Giữ lại làm bằng chứng cho vòng sau.
