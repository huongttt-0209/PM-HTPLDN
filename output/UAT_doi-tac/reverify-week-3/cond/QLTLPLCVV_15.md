# Bảng đối chiếu điều kiện — QLTLPLCVV_15 (row 300) — Upload file mã độc: message

**Kết luận:** BA confirm. Không tái hiện được tình huống đối tác báo ("Tải file thất bại" khi upload file mã độc) vì trên env verify `18.143.165.120.nip.io` **bước Quét virus chưa chặn file chứa chữ ký mã độc chuẩn EICAR** — file PDF hợp lệ nhúng chuỗi EICAR upload **thành công** (HTTP 201, `trangThaiQuet="SACH"` = sạch). Nghi vấn tính năng quét virus **chưa được bật/triển khai** trên env (khớp ghi nhận nội bộ: phần virus/mã độc trước đây được hoãn). Đây là **câu hỏi phạm vi + hướng phản hồi đối tác cần BA chốt**, không phải bug wording đơn thuần; đồng thời kèm **phát hiện bảo mật** (mã độc không bị chặn) — xem mục Câu hỏi BA.

> Verdict (BA confirm) đến từ **câu hỏi phạm vi/đặc tả** "bước quét virus có trong phạm vi/được bật không?" — không phụ thuộc điều kiện role/state/data (các điều kiện dưới đều khớp, 0 GAP). Việc BE nhận file EICAR là "sạch" chính là **nội dung cần BA chốt**, không phải một GAP tiền đề chưa đóng.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLTLPLCVV_15.jpg`) | Mình test (cbnv_tw / CB_NV_TW, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW | cbnv_tw (CB_NV_TW — đúng Tác nhân SRS dòng 806, CRUD đầy đủ) | Không |
| Entity + surface upload | Tư liệu PL của 1 TVCS, đang thêm/sửa (widget File đính kèm) | Modal "Thêm tư liệu pháp luật" của TVCS-SEED-0001 (đúng surface upload) | Không |
| Dữ liệu tiền đề (file test) | File chứa mã độc (nội dung không rõ) | File test chuẩn **EICAR** (chuỗi 68 byte chuẩn ngành, vô hại) — 2 biến thể (raw + nhúng PDF hợp lệ) | Không |
| Thao tác + kết quả tranh chấp | Upload file mã độc → hệ thống chặn + báo "Tải file thất bại" (generic) | Upload EICAR (đã qua cổng định dạng) → BE nhận **`trangThaiQuet="SACH"`**, HTTP 201, **KHÔNG chặn** → không có message mã độc để đối chiếu. Khác biệt env này = nội dung cần BA chốt (quét virus có bật không) | Không |

## Đã thử cạn kiệt mọi cách đưa file mã độc qua cổng định dạng tới bước Quét virus

- **File 1 — `eicar_test.pdf`** (chuỗi EICAR thô, đuôi `.pdf`): nội dung ≠ PDF → bị chặn ở **cổng kiểm tra định dạng** (EC-FILE-01, dòng 857). `POST /api/v1/tu-lieu-phap-ly-vvs/upload` → **HTTP 400** "Nội dung file không khớp định dạng" — chặn vì **định dạng**, KHÔNG phải vì mã độc.
- **File 2 — `eicar_valid.pdf`** (PDF hợp lệ `%PDF-1.4`, 475 B, **nhúng nguyên chuỗi EICAR 68 byte**): hợp lệ → **qua** cổng định dạng, vào bước Quét virus. `POST .../upload` → **HTTP 201**, `success:true`, **`trangThaiQuet:"SACH"`** (sạch) — file được nhận, hiển thị trong modal (Xem/Gỡ), KHÔNG toast lỗi.

**Định dạng cho phép (hint widget):** `.pdf, .doc, .docx, .xls, .xlsx, .jpg, .png` (max 20MB). File thô EICAR (`.com`/`.txt`/`.exe`) bị cổng định dạng chặn TRƯỚC khi tới bước Quét virus → cách duy nhất đưa chữ ký mã độc qua cổng định dạng là nhúng vào file hợp lệ (case #2). Case #2 cho thấy bước Quét virus (SRS dòng 858) **không** đánh dấu file chứa EICAR là mã độc → không có surface nào còn lại để kích hoạt E4 (ERR-TLPL-04).

**Bằng chứng network (case #2, `get_network_request`):**
```
POST /api/v1/tu-lieu-phap-ly-vvs/upload  →  201
response.data = { "id":"d5e4546f-02ba-4ca3-b93b-b5287faf979b", "tenFile":"eicar_valid.pdf",
                  "dungLuong":475, "loaiFile":"application/pdf", "trangThaiQuet":"SACH" }
No error toast. File hiển thị trong modal "Thêm tư liệu pháp luật" (Xem / Gỡ bỏ tập tin).
```
Ảnh: `reverify-audit/QLTLPLCVV_15/eicar-accepted-modal.png`.

## Đối chiếu SRS

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:858` — Processing "Tải lên file" step 3 = "Quét virus".
- `:955` — Error Handling E4 `ERR-TLPL-04` "File '{ten_file}' chứa mã độc" (ERROR).
- Vì bước 858 trả SẠCH cho file EICAR → E4 (dòng 955) không được kích → không có message để đối chiếu với "Tải file thất bại" đối tác báo.

## Câu hỏi cần BA chốt (chi tiết ở `../ba-confirm/tvcs/ba-confirmation-needed-tvcs-batchF.md`)

1. **Phạm vi:** bước Quét virus (SRS dòng 858) có nằm trong phạm vi release / được bật trên env này không, hay đã được hoãn? (Vì file chứa chữ ký EICAR chuẩn vẫn được nhận là "sạch".)
2. **Hướng xử lý theo nhánh:**
   - Nếu quét virus **CHƯA trong phạm vi/bị hoãn** → khiếu nại wording của đối tác (message khi chặn mã độc) **tạm hoãn đánh giá** đến khi tính năng được bật; ghi rõ với đối tác.
   - Nếu quét virus **PHẢI hoạt động** → đây là **lỗ hổng bảo mật** (mã độc không bị chặn) cần **Dev BE** xử lý TRƯỚC; wording message là thứ yếu, đánh giá lại sau khi AV chặn được.
