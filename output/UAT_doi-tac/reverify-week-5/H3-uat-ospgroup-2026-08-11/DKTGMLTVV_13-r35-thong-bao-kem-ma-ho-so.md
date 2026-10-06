# DKTGMLTVV_13 (sheet `bug` dòng 35) — Thông báo đăng ký phải kèm mã hồ sơ vừa sinh

- Môi trường: https://htpldn-uat.ospgroup.vn — bản dựng **HTPLDN · V1.0.11**
- Thời điểm: 2026-08-11 ~10:18 – 10:25

## Tài khoản: đã dùng đúng vai trò và đúng cấp địa phương mà tiêu chí nhắm tới

Tiêu chí ghi Precondition là `nht_ag_uat2 / Test@1234` (Người hỗ trợ pháp lý, Sở Tư pháp An Giang).

- `nht_ag_uat2` **không đăng nhập được** trên env nghiệm thu — thông báo "Tên đăng nhập hoặc mật khẩu không đúng." (bộ tài khoản env nghiệm thu khác env nội bộ).
- Nhưng **chính bản ghi NHT An Giang đó có thật** trên env này: `NHT-STP-AG-0001` — "Phùng Thị NHT An Giang", đơn vị **Sở Tư pháp An Giang**, đang hoạt động, đã gắn tài khoản; email của bản ghi là `nht_01@htpldn.test`.
- Tài khoản gắn với bản ghi đó là **`nht_01`**. Mật khẩu cũ không phải `Test@1234`, nên tôi giành lại phiên bằng **luồng Quên mật khẩu** (nhập email → lấy link đặt lại trong hộp thư giả lập của env → đặt mật khẩu `Test@1234`) — đúng cách QA đã dùng cho `truong_16` / `cb_nv_tw_03` trên env này.
- Lần đăng nhập đầu, phần mềm bắt buộc bổ sung **số CCCD của tài khoản** ("Cập nhật thông tin bắt buộc") mới cho dùng tiếp; đã nhập `089185000835` → "Cập nhật CCCD thành công".

⇒ Vai trò đo: **Người hỗ trợ pháp lý, cấp địa phương (Sở Tư pháp An Giang)** — đúng tinh thần Precondition, không phải dùng tài khoản Trung ương.

## Làm đúng 4 bước trong ô "CÁCH VERIFY"

| Bước | Thao tác | Đo được |
|---|---|---|
| 1 | Mạng lưới Tư vấn viên → Tư vấn viên/Chuyên gia → **Thêm mới**. Loại = "Tư vấn viên (TVV)", 2 lĩnh vực, tổ chức chủ quản. Bấm **Lưu** | Nhập: họ tên "QA Verify R35 NHT An Giang 11-08", CCCD 001199000835, ngày sinh 10/03/1985, trình độ Thạc sĩ, chuyên ngành Luật doanh nghiệp, 7 năm, số thẻ hành nghề, **2 lĩnh vực = Thuế + Doanh nghiệp**. Ô "Đơn vị quản lý" phần mềm **tự gán "Sở Tư pháp An Giang"** (khoá, không sửa được) |
| 2 | Đọc TRỌN câu thông báo ngay sau khi lưu | **"Đăng ký thành công, chờ thẩm định. Mã hồ sơ: TVV-STP-AG-0003"** — bắt bằng bộ theo dõi cài TRƯỚC khi bấm, không lọc trùng; đồng thời hẹn giờ chụp ảnh nên có cả bằng chứng hình |
| 3 | Mở tab "Mới đăng ký", tìm hồ sơ vừa tạo, đọc mã THẬT | Tab "Mới đăng ký" có 2 dòng, dòng đầu: `TVV-STP-AG-0003` · "QA Verify R35 NHT An Giang 11-08" · Tư vấn viên · **Doanh nghiệp, Thuế** · Mới đăng ký |
| 4 | Đối chiếu mã trong thông báo với mã thật | `TVV-STP-AG-0003` = `TVV-STP-AG-0003` — **trùng khớp** |

Hai lần bấm Lưu đầu bị phần mềm chặn vì thiếu tệp bắt buộc — "File thẻ hành nghề là bắt buộc đối với Tư vấn viên", rồi "File đính kèm (Bằng cấp / Chứng chỉ) là bắt buộc khi đăng ký ứng viên mới". Đây là ràng buộc dữ liệu của phần mềm, không phải điểm chấm; đã đính kèm tệp PDF rồi lưu lại.

## Chấm theo đúng mốc ✅ PASS trong ô Kết quả verify

| Việc | Yêu cầu | Đo được | Kết |
|---|---|---|---|
| (a) | Câu thông báo vừa giữ phần "Đăng ký thành công, chờ thẩm định", vừa kèm mã hồ sơ vừa sinh | "Đăng ký thành công, chờ thẩm định. Mã hồ sơ: TVV-STP-AG-0003" | ✅ |
| (b) | Mã trong thông báo TRÙNG KHỚP mã thật, dạng `TVV-STP-AG-000N`, không rỗng / undefined / null / mã hồ sơ khác | `TVV-STP-AG-0003`, đúng khuôn, trùng mã thật trên danh sách | ✅ |
| (c) | 7 vế đã đạt ở lượt 07/08 vẫn đạt | Hồ sơ vào tab "Mới đăng ký" ✅ · lưu đủ 2 lĩnh vực (Thuế + Doanh nghiệp) ✅ · đơn vị quản lý tự gán đúng theo người đăng ký (Sở Tư pháp An Giang) ✅ · quay về trang Danh sách sau khi lưu ✅. Vế "đúng tổ chức chủ quản" không đo được: pool Tổ chức tư vấn của Sở Tư pháp An Giang rỗng ("Chưa có Tổ chức tư vấn ở trạng thái Đang hoạt động"), ô này không bắt buộc nên để trống | ✅ (một vế không đo được vì thiếu dữ liệu nền, không phải vì phần mềm sai) |

## Bẫy đã tôn trọng

- **Bẫy 1** — nút vẫn mang nhãn "Lưu"; KHÔNG log lại "thiếu nút Gửi đăng ký".
- **Bẫy 2** — sau khi lưu phần mềm quay về trang Danh sách (`/chuyen-gia-tvv/danh-sach`); KHÔNG log lại "không chuyển sang trang theo dõi tiến độ".
- **Bẫy 3** — ô Loại chỉ có Tư vấn viên / Chuyên gia; KHÔNG log lại "thiếu loại Người hỗ trợ".
- **Bẫy 4** — không bắt bẻ câu chữ phần dẫn; chỉ đòi "thông báo thành công CÓ kèm mã hồ sơ vừa sinh" — đã thoả.

## Bằng chứng

- [image/DKTGMLTVV_13-r35-uat-thong-bao-dang-ky-kem-ma-ho-so.png](image/DKTGMLTVV_13-r35-uat-thong-bao-dang-ky-kem-ma-ho-so.png) — **một** thông báo trên màn: "Đăng ký thành công, chờ thẩm định. Mã hồ sơ: TVV-STP-AG-0003", đã về trang Danh sách, tab "Mới đăng ký" đếm 2
- [image/DKTGMLTVV_13-r35-uat-tab-moi-dang-ky-ma-that-khop.png](image/DKTGMLTVV_13-r35-uat-tab-moi-dang-ky-ma-that-khop.png) — mã thật trên danh sách tab "Mới đăng ký"
