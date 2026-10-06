# Re-verify bug QLNDTVVCG_OOS_01 — dòng 358

- Môi trường: `https://18.143.165.120.nip.io` — HTPLDN v1.0.10
- Thời điểm: 07/08/2026 21:42–21:48 (Asia/Ho_Chi_Minh)
- Tài khoản dựng tiền đề: `cbnv_tw_01`
- Tài khoản thực hiện: `qa_tvvseed28` (CG được phân công)
- Bản ghi đo quyết định: `TVCS-20260805-0003`
- Verdict: **PASS**

## Căn cứ BA ưu tiên

Phiếu BA ngày 06/08/2026 chốt hai tiêu chí sau khi chuyên gia từ chối:

1. Thông báo phải là **“Đã từ chối yêu cầu tư vấn”**.
2. Bản ghi rời phạm vi của chuyên gia nên hệ thống phải đưa chuyên gia về màn danh sách.

## Luồng đã chạy

1. Dùng `cbnv_tw_01` phân công bản ghi đang ở `Tiếp nhận` cho `qa_tvvseed28`.
2. Đăng nhập đúng tài khoản chuyên gia được phân công, mở chi tiết bản ghi.
3. Bấm **Từ chối nhiệm vụ**, nhập lý do dài hơn 10 ký tự rồi xác nhận.
4. Bắt trực tiếp DOM notification và kiểm URL sau thao tác.

## Kết quả

- Notification bắt được lúc `2026-08-07T14:48:46.219Z`: **“Đã từ chối yêu cầu tư vấn”**. Không còn câu sai **“Đã xác nhận”**.
- Hệ thống điều hướng từ trang chi tiết về `/tv-chuyen-sau/danh-sach`.
- Danh sách của chuyên gia không còn bản ghi vừa từ chối, phù hợp việc gỡ phân công/trả về hàng chờ.
- Hai lỗi console 403 ở API tra cứu doanh nghiệp đã tồn tại trên trang danh sách và không thuộc request từ chối; thao tác từ chối vẫn hoàn tất đúng.

## Bằng chứng

- `image/358-before-tu-choi.png`: chi tiết bản ghi ở trạng thái Đã phân công, đúng CG, có nút Từ chối nhiệm vụ.
- `image/358-after-tu-choi-redirect-list.png`: hệ thống đã quay về danh sách và bản ghi không còn trong hàng chờ của CG.
- Bản đo DOM lưu tại phiên kiểm thử ghi nhận chính xác nội dung toast và timestamp nêu trên.

## Cập nhật Sheet

- Dòng: 358
- `Trạng thái dev fix`: `Test done`
- Không ghi `Kết quả verify` vì verdict Pass, đúng quy tắc người dùng giao.
