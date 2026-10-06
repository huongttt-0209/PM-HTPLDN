# Đề xuất nội dung BA ghi chú cho đối tác — QLNDTVVCG_24

> **Trạng thái: BẢN NHÁP ĐỂ BA DUYỆT — QA chưa ghi gì vào file/sheet của đối tác.**
> Việc ghi vào tài liệu đối tác là của BA, không phải của QA.

---

## 1. Vì sao cần ghi chú, không chỉ đóng phiếu là xong

Phiếu QLNDTVVCG_24 nay **Pass**, nhưng Pass theo một **cách hiểu mới** mà đối tác chưa được thông báo:

- Đối tác kiểm bằng cách **mở chuông thông báo trong ứng dụng ở tài khoản doanh nghiệp** (đúng như video
  `QLNDTVVCG_24.webm`). Làm đúng y như vậy hôm nay thì **vẫn thấy trống** — vì DN nay nhận **thư điện tử**,
  không nhận in-app.
- Tệ hơn: chuông của DN *TKM Company* **vẫn còn** mục cũ *"Chuyên gia đã xác nhận tư vấn: TVCS-20260803-0003"*
  ngày 04/08. Người kiểm sẽ thấy "trước đây có, giờ mất" và rất dễ kết luận là **lỗi mới phát sinh**.
- Nếu không có ghi chú, khả năng cao đối tác **Reopen oan** ở vòng sau.

Đây là lý do phải ghi chú, chứ không phải thủ tục hình thức.

## 2. Nội dung đề nghị (BA có thể dùng nguyên văn)

> **QLNDTVVCG_24 — thay đổi kênh thông báo, đã được duyệt ngày 06/08/2026.**
>
> Với nghiệp vụ Tư vấn chuyên sâu, khi chuyên gia bấm *Chấp nhận*, hệ thống gửi thông báo theo hai kênh
> khác nhau tùy người nhận:
>
> - **Cán bộ nghiệp vụ:** nhận **thông báo trong ứng dụng** và **thư điện tử**.
> - **Doanh nghiệp:** **chỉ nhận thư điện tử** gửi tới địa chỉ thư đã khai trên hồ sơ doanh nghiệp.
>   Doanh nghiệp ở nhóm này **không** có thông báo trong ứng dụng.
>
> Lý do: nhóm doanh nghiệp của nghiệp vụ Tư vấn chuyên sâu không có cổng riêng trong hệ thống, nên kênh
> chính thức tới doanh nghiệp là thư điện tử. Hệ thống vẫn lưu vết thông báo trong cơ sở dữ liệu để tra
> cứu, nhưng không hiển thị lên chuông của doanh nghiệp.
>
> **Cách kiểm tra đúng:** mở hộp thư của địa chỉ đã khai trên hồ sơ doanh nghiệp, tìm thư tiêu đề
> *"Chuyên gia đã xác nhận tư vấn: <mã tư vấn>"*. **Không** kiểm bằng chuông thông báo của tài khoản
> doanh nghiệp — kiểm cách đó sẽ luôn thấy trống và không phản ánh đúng hiện trạng.
>
> **Lưu ý về dữ liệu cũ:** các thông báo trong ứng dụng của doanh nghiệp phát sinh **trước 06/08/2026**
> vẫn còn trong danh sách. Đó là dấu vết của cách làm cũ, không có nghĩa là cách làm mới bị lỗi.

## 3. Nơi nên đặt ghi chú

| Nơi | Ghi gì |
|---|---|
| Ô diễn giải của dòng `QLNDTVVCG_24` trên sheet đối tác | Toàn bộ mục 2 (hoặc rút gọn 3 gạch đầu dòng đầu) |
| Tài liệu đặc tả bàn giao / phụ lục thông báo | Mục 2, kèm trích `srs-fr-12-tv-chuyen-sau.md:192` và `srs-v3.5.md:5664` (BR-NOTIF-01) |
| Kịch bản nghiệm thu của đối tác cho nghiệp vụ Tư vấn chuyên sâu | Sửa bước kiểm: *"mở hộp thư của doanh nghiệp"* thay cho *"mở chuông thông báo của doanh nghiệp"* |

## 4. Căn cứ

| Nguồn | Nội dung |
|---|---|
| `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:192` | "CB NV: in-app + email; DN: chỉ thư điện tử tới `DOANH_NGHIEP.email` … `[BA chốt 2026-08-06]`" |
| `…/srs-fr-12-tv-chuyen-sau.md:1550` | Máy trạng thái PHAN_CONG → DANG_TU_VAN: "TB CB NV (in-app + email) + TB DN (chỉ thư điện tử)" |
| `Docs-PM-HTPLDN/…/srs-v3.5/srs-v3.5.md:5664` (BR-NOTIF-01) | "chỉ gửi thư điện tử … vẫn tạo bản ghi `THONG_BAO` để lưu vết nhưng đặt `hien_trong_ung_dung = 0`" |
| `reverify-week-5/ba-confirm/BA-phan-hoi/phan-hoi-ba-7-diem-can-chot-2026-08-06.md` | Quyết định gốc của BA ngày 06/08/2026 |
| Đo thực tế 10/08/2026 trên `htpldn-uat.ospgroup.vn` | [KET-QUA-REVERIFY-QLNDTVVCG_24.md](KET-QUA-REVERIFY-QLNDTVVCG_24.md) mục 2.1 và 4 |
