# QLDMTCTV_12 (sheet `bug` dòng 149) — Mốc 5.000 ký tự ô "Lý do thay đổi trạng thái"

- Môi trường: https://htpldn-uat.ospgroup.vn — bản dựng **HTPLDN · V1.0.11**
- Thời điểm: 2026-08-11 ~09:40 – 10:14

## Tài khoản đã dùng — hai màn, hai đơn vị

Tiêu chí ghi Precondition `cbnv_tw_03` + bản ghi `TC-TW-DEMO-001`. Trên env nghiệm thu **không có** bản ghi `TC-TW-DEMO-001` (bản ghi đó thuộc env nội bộ). Yêu cầu cốt lõi của Precondition là "Cán bộ Nghiệp vụ **cùng đơn vị** với bản ghi, KHÔNG dùng tài khoản quản trị" — đã giữ đúng yêu cầu đó ở cả hai màn:

| Màn | Bản ghi | Tài khoản | Cùng đơn vị? |
|---|---|---|---|
| Chi tiết **Tổ chức tư vấn** — việc (a)…(e) | `TC-STP-HN-0001` (Sở Tư pháp Hà Nội) | **`cbnv_dp`** — CB Nghiệp vụ Sở Tư pháp Hà Nội (**địa phương**) | ✅ |
| Chi tiết **Tư vấn viên** — việc (f) | `TVV-BTP-TW-0004` (Cục Bổ trợ tư pháp - Bộ Tư pháp) | **`cbnv_tw`** — CB Nghiệp vụ Trung ương | ✅ |
| So hành vi màn Tổ chức tư vấn ở cùng đơn vị TW | `TC-BTP-TW-0008` | `cbnv_tw` | ✅ |

Vì sao việc (f) phải dùng tài khoản Trung ương: tiêu chí đòi "một hồ sơ TVV **cùng đơn vị**" với người đo, mà pool Tư vấn viên của Sở Tư pháp Hà Nội rỗng — không có hồ sơ nào để `cbnv_dp` bấm được nút "Cập nhật trạng thái". Đây là phương án dự phòng đã được đồng ý.

## Đo được, theo từng việc trong ô "CÁCH VERIFY"

| Việc | Yêu cầu | Đo được | Kết |
|---|---|---|---|
| (a) | Chuỗi đúng 5.000 ký tự lưu thành công, đọc lại ở tab Lịch sử ĐỦ 5.000 ký tự | Màn Tổ chức tư vấn (`TC-STP-HN-0001`, `cbnv_dp`): lưu 5.000 ký tự thành công, đọc lại ở tab "Lịch sử" đủ 5.000 ký tự. Màn Tư vấn viên (`TVV-BTP-TW-0004`, `cbnv_tw`): lưu 5.000 ký tự → "Cập nhật trạng thái thành công", trạng thái đổi Đang hoạt động → Tạm dừng. *Màn Tư vấn viên không có tab Lịch sử trạng thái nên không đọc lại được độ dài trên giao diện ở màn này — vế đọc lại đã đo xong ở màn Tổ chức tư vấn.* | ✅ |
| (b) | Dán 8.000 ký tự thì ô GIỮ NGUYÊN 8.000, không tự cắt | Màn Tư vấn viên: ô giữ **8.000**. Màn Tổ chức tư vấn: ô giữ **8.000**. Thuộc tính giới hạn ký tự của ô là `-1` (không chặn cứng) ⇒ không còn cắt âm thầm | ✅ |
| (c) | Bộ đếm đúng dạng {n}/5000 và chuyển sang trạng thái cảnh báo khi n > 5000 | Bộ đếm hiện `0/5000` → `5000/5000` → `8000/5000` → `5001/5000` ở cả hai màn. Khi n > 5000 thì ô vào trạng thái lỗi (`ant-form-item-has-error`) và hiện **dòng chữ đỏ** (#f5222d) "Lý do thay đổi tối đa 5.000 ký tự" ngay dưới bộ đếm. Ghi nhận thẳng: **chữ số của bộ đếm giữ màu xám**, phần cảnh báo là dòng đỏ bên dưới — người dùng vẫn được cảnh báo đúng lúc vượt mốc, cùng hành vi ở cả hai màn | ✅ (kèm ghi nhận) |
| (d) | Ở 5.001 và ở 9 ký tự đều KHÔNG lưu được VÀ có câu báo ngay tại ô | **5.001 ký tự:** màn Tư vấn viên — bấm [Xác nhận] → cửa sổ vẫn mở, **0 request** lên máy chủ, không có thông báo thành công, trạng thái bản ghi không đổi, dòng đỏ vẫn đứng; màn Tổ chức tư vấn — nút [Đồng ý] bị làm mờ + dòng đỏ cùng nội dung. **9 ký tự:** bộ đếm `9/5000`, câu báo "Lý do thay đổi là bắt buộc (≥ 10 ký tự)", bấm xác nhận → **0 request** | ✅ |
| (e) | Máy chủ từ chối chuỗi 5.001 ký tự bằng mã lỗi riêng của chức năng, không phải mã hệ thống chung | Màn Tư vấn viên: `POST /api/v1/tu-van-viens/{id}/cap-nhat-trang-thai` với lý do 5.001 ký tự → **422**, `code: ERR-VAL-IV-TT-03`, `field: lyDo`, thông báo "Lý do thay đổi phải từ 10 đến 5.000 ký tự"; trạng thái bản ghi **không đổi** sau lượt gọi. Màn Tổ chức tư vấn: **422**, `ERR-TT-TC-03`, `field: lyDo` | ✅ |
| (f) | Cả hai màn Tổ chức tư vấn và Tư vấn viên cùng hành vi | Cùng hành vi ở mọi mốc: không cắt ở 8.000 · bộ đếm {n}/5000 · dòng đỏ khi vượt · chặn lưu ở 5.001 · máy chủ trả mã riêng. Khác nhau duy nhất là **cách chặn**: màn Tổ chức tư vấn làm mờ nút, màn Tư vấn viên để nút sáng nhưng bấm không gửi gì. Cả hai đều thoả "không lưu được + có câu báo tại ô" | ✅ |

## Bẫy đã tôn trọng

- **Bẫy 1** — KHÔNG log lại "màn hình không có nút chức năng". Đo đúng tiền đề (Cán bộ Nghiệp vụ cùng đơn vị) thì trang chi tiết có đủ **Sửa hồ sơ · Cập nhật trạng thái · Công khai lên Cổng PLQG**.
- **Bẫy 2** — không bắt bẻ chính tả câu báo; chỉ đòi "có câu báo tại ô + chặn được nút Lưu".
- **Bẫy 3** — ô "Trạng thái mới" lọc theo trạng thái hiện tại là ĐÚNG: bản ghi Đang hoạt động chỉ hiện "Tạm dừng" + "Vô hiệu hóa"; sau khi thành Tạm dừng thì hiện "Đang hoạt động" + "Vô hiệu hóa". Không báo thiếu lựa chọn.
- **Bẫy 4** — đã kiểm đúng điểm này: **có THÊM câu báo tại ô**, không chỉ làm mờ nút.

## Hoàn nguyên dữ liệu (bước 8)

- `TVV-BTP-TW-0004`: Tạm dừng → **Đang hoạt động** (lý do hợp lệ, `POST …/cap-nhat-trang-thai` → 200).
- `TC-BTP-TW-0008`: chỉ mở cửa sổ để so hành vi rồi bấm **Hủy** — vẫn Đang hoạt động, không lưu gì.
- `TC-STP-HN-0001`: đã về **Đang hoạt động**.

## Bằng chứng

- [image/QLDMTCTV_12-r149-uat-dan-8000-ky-tu-dem-8000-5000-co-cau-bao-do.png](image/QLDMTCTV_12-r149-uat-dan-8000-ky-tu-dem-8000-5000-co-cau-bao-do.png) — màn Tổ chức tư vấn: 8.000 ký tự không bị cắt, bộ đếm `8000/5000`, dòng báo đỏ
- [image/QLDMTCTV_12-r149-uat-man-chi-tiet-TVV-5001-ky-tu-chan-luu.png](image/QLDMTCTV_12-r149-uat-man-chi-tiet-TVV-5001-ky-tu-chan-luu.png) — màn Chi tiết Tư vấn viên: 5.001 ký tự, bộ đếm `5001/5000`, dòng báo đỏ, bấm xác nhận không lưu được
