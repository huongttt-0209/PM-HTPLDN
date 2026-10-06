# Bảng đối chiếu điều kiện — VVHT_001 (row 53) — re-verify R4 sau khi dev báo fix

**Kết luận:** Pass.
- Thêm mới vụ việc bằng [Lưu & Tiếp nhận] **lưu được**, không còn lỗi *"ngayTiepNhan must be a valid ISO 8601 date string"*.
- Nút submit còn lại của cùng màn ([Lưu nháp]) cũng lưu được ⇒ không phải fix nửa vời.
- Bề mặt thứ hai mà dev khai sửa chung (ô "Ngày thanh toán" màn Chi trả) đã gửi ngày đúng khuôn ISO.

> ⚠️ **Phạm vi môi trường:** đo trên **env được giao `18.143.165.120.nip.io`** (bản dựng `V1.0.4`, tài nguyên `assets/index-C-Au2yTy.js`) theo đúng `input/input.md`. Env đối tác `htpldn-uat.ospgroup.vn` đang chạy bản dựng khác (`assets/index-B4L2Psgc.js`, nhãn `V1.0.3`) ⇒ kết luận chứng minh **mã nguồn đã sửa**, chưa chứng minh bản sửa đã được triển khai lên env đối tác; dev cần xác nhận việc triển khai.

| Điều kiện có thể đổi kết quả | Bug gốc (phiếu `VVHT_001` + mô tả tái hiện vòng 1 ghi trên sheet) | Mình test lại (env nip.io, 31/07/2026 · V1.0.4) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — CB Nghiệp vụ Trung ương, đơn vị Cục Bổ trợ tư pháp (BTP · TW) — đúng vai trò được tạo vụ việc | `cbnv_tw` — đăng nhập thành công, thanh tiêu đề ghi "CB Nghiệp vụ - Trung ương" + "BTP · TW"; thẻ định danh trong yêu cầu gửi lên có `vaiTro: CB_NV_TW`, `capDonVi: TW` — TRÙNG KHỚP | Không |
| Màn hình / chức năng | Vụ việc HTPL → **Thêm mới** (nút "Nhập thủ công") → form tạo mới → bấm **[Lưu & Tiếp nhận]** | Đúng màn `/vu-viec/tao-moi`, mở bằng nút "Nhập thủ công" trên màn danh sách, bấm đúng nút **[Lưu & Tiếp nhận]**; sau đó lặp lại lần 2 với nút **[Lưu nháp]** | Không |
| Entity + trạng thái (state machine) | Vụ việc **chưa tồn tại** — lỗi xảy ra ngay ở bước tạo, trước khi có bản ghi. Kỳ vọng: lưu xong vào trạng thái đã tiếp nhận | Tạo **2 bản ghi mới hoàn toàn**: `VV-BTP-TW-20260731-001` (qua [Lưu & Tiếp nhận] → trạng thái **"Đã tiếp nhận"**) và `VV-BTP-TW-20260731-002` (qua [Lưu nháp]) | Không |
| Dữ liệu tiền đề | Có chọn doanh nghiệp + điền đủ trường bắt buộc | Chọn doanh nghiệp `DN-HNI-0001` (Cong ty TNHH QA UAT Kiem Thu) qua hộp "Tìm doanh nghiệp"; điền đủ Tiêu đề, Nội dung yêu cầu, Lĩnh vực, Loại hình, Độ ưu tiên, Lý do ưu tiên, Kênh tiếp nhận | Không |
| Input / trường gây lỗi | Ô **"Ngày tiếp nhận"** để **nguyên giá trị mặc định**, không chạm vào (bug gốc: ô hiển thị 31/07/2026 mặc định mà máy chủ vẫn báo ngày không hợp lệ) | Ô "Ngày tiếp nhận" giữ nguyên mặc định **31/07/2026**, không bấm lịch, không gõ tay — ĐÚNG như điều kiện bug gốc | Không |
| Bề mặt thứ hai dev khai sửa chung | Màn "Ghi thanh toán" (Chi trả) — trường "Ngày thanh toán" dính cùng lỗi | Mở đúng màn Chi trả → hồ sơ `CT-SEED-107` trạng thái "Đã duyệt" → [Cập nhật TT] → ô "Ngày thanh toán" mặc định 31/07/2026, giữ nguyên rồi bấm gửi; đọc **nội dung yêu cầu gửi lên** để xem khuôn ngày | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hành vi luồng + Lỗi máy chủ)

- `bug-reports/image/R4-VVHT_001-01-form-truoc-khi-luu-tiep-nhan.png` — đã mở đọc: form tạo mới đã điền đủ, ô "Ngày tiếp nhận" = **31/07/2026** (mặc định, chưa chạm).
- `bug-reports/image/R4-VVHT_001-02-danh-sach-vu-viec-moi-da-tiep-nhan.png` — đã mở đọc: danh sách có `VV-BTP-TW-20260731-001`, cột Trạng thái **"Đã tiếp nhận"**, cột Ngày tiếp nhận **31/07/2026**.
- `bug-reports/image/R4-VVHT_001-03-post-vu-viecs-manual-201.network-response` — đã lưu: phần trả về của lượt tạo vụ việc (mã 201).
- `bug-reports/image/R4-VVHT_001-04-vu-viec-luu-nhap-thanh-cong.png` — đã mở đọc: bản ghi `VV-BTP-TW-20260731-002` tạo bằng nút [Lưu nháp].
- Đọc thẳng thông báo trên màn: *"Đã tiếp nhận — VV-BTP-TW-20260731-001"* và *"Đã lưu nháp — VV-BTP-TW-20260731-002"*; **0 dòng báo lỗi đỏ dưới ô nào**.

## Phương pháp thứ hai (bắt buộc)

- **Đọc thẳng nội dung trao đổi với máy chủ, không chỉ nhìn thông báo trên màn:** lượt tạo vụ việc gửi lên `POST /api/v1/vu-viecs/manual` với `"ngayTiepNhan":"2026-07-31"` — đúng khuôn ngày quốc tế mà máy chủ đòi — và nhận về **201 (tạo mới thành công)**. Bug gốc nêu giá trị gửi lên là chuỗi "Invalid Date" nên bị chặn; nay giá trị gửi lên đã đúng ⇒ chứng minh chỗ chuẩn hóa ngày đã được sửa, không chỉ là "màn hình trông ổn".
- **Đo cả hai nút submit của cùng một form** để loại khả năng fix một nửa: [Lưu & Tiếp nhận] → *"Đã tiếp nhận"*; [Lưu nháp] → *"Đã lưu nháp"*. Cả hai đều không sinh lỗi ngày.
- **Kiểm bản ghi sau khi lưu (không dừng ở thông báo):** mở màn chi tiết `VV-BTP-TW-20260731-001` — trạng thái **"Đã tiếp nhận"**, mốc "Ngày tiếp nhận" ghi **31/07/2026**, dòng thời gian có mục "Tạo vụ việc 31/07/2026 22:02"; quay ra danh sách vẫn thấy đúng bản ghi với đúng ngày ⇒ dữ liệu lưu thật, không phải chỉ hiện thông báo rồi mất.
- **Kiểm bề mặt thứ hai bằng cùng cách đọc nội dung gửi lên:** màn Chi trả gửi `"ngayThanhToan":"2026-07-31"` — cũng đúng khuôn ISO. Lượt gửi này bị máy chủ từ chối, nhưng lý do là **quy tắc nghiệp vụ** (`ERR-CT-TD-03` — *"Tổng chi trả trong năm vượt trần hỗ trợ (5.000.000,00 VNĐ)"*), **không phải** lỗi khuôn ngày ⇒ chỗ chuẩn hóa ngày ở màn này cũng đã đúng. QA **không** đi tiếp bước hạ số tiền để hoàn tất thanh toán vì việc đó sẽ tiêu mất bản ghi chi trả duy nhất đang ở trạng thái "Đã duyệt" của môi trường, mà mục này nằm ngoài phạm vi phiếu.
- **Bản dựng:** thanh bên trái ghi `HTPLDN · V1.0.4` ⇒ đúng bản đã có thay đổi của dev.
