# Re-verify UI - CBKQDTBD_OOS_01 (dòng 347)

- Ngày chạy: 2026-08-07
- Môi trường: `https://18.143.165.120.nip.io`
- Phiên bản hiển thị: `HTPLDN · V1.0.10`
- Tài khoản: `cbnv_tw_01` (bộ 01)
- Phương thức verify: Chrome DevTools trên cửa sổ Chrome hiển thị; đăng nhập và đọc OTP qua UI MailHog. API chỉ được dùng để tạo/chuẩn bị dữ liệu đầu vào, không dùng để kết luận.
- Kết luận: **PASS**
- Giá trị đề xuất ghi Sheet tại cột **Trạng thái dev fix**: `Test done`
- Cột **Kết quả verify**: không ghi vì verdict là Pass.

## Dữ liệu đầu vào và phạm vi

Hai khóa học gốc của bug, `KH-20260703-005` và `KH-20260509-006`, không còn trên môi trường. Một khóa học thay thế đã được seed qua API để xác nhận dữ liệu tạo mới xuất hiện đúng trên UI:

- ID: `25e918c8-3c4e-472e-8a70-352899e00d2b`
- Mã: `KH-20260807-001`
- Tên: `QA-RV347-20260807 - Verify consistency Don vi 3 tabs`
- Trạng thái sau khi chuẩn bị: `Đã duyệt`

Trên build hiện tại, chức năng thêm/import học viên thủ công đã được BA chốt loại bỏ và route cũ trả `404`; UI tab **Học viên** cũng không còn nút thêm/import. Vì vậy không thể tạo cả hai nhánh dữ liệu trên khóa học mới mà không can thiệp trái luồng nghiệp vụ. Để bao phủ đúng đặc tính dữ liệu của bug, việc verify UI dùng hai fixture còn hoạt động:

1. `AAA-KH-TW`: học viên `Học viên TW 01`, nguồn **Nhập tay**, không có đơn vị, đã có kết quả được duyệt/công bố.
2. `KH-QAW7-HOINGHI`: học viên `Nguyễn Văn Ngọc`, có đơn vị thật `TKM`. Đăng ký được duyệt qua API chỉ như bước chuẩn bị để dòng học viên xuất hiện trên các tab kết quả.

## Kết quả quan sát qua UI

| Nhánh dữ liệu | Khóa học / học viên | Học viên | Kết quả | Công bố kết quả |
|---|---|---:|---:|---:|
| Không có đơn vị, nguồn Nhập tay | `AAA-KH-TW` / `Học viên TW 01` | `-` | `—` | `—` |
| Có đơn vị thật | `KH-QAW7-HOINGHI` / `Nguyễn Văn Ngọc` | `TKM` | `TKM` | `TKM` |

Khác biệt ký tự `-` và `—` là hai cách trình bày giá trị trống trên các bảng, không phải dữ liệu đơn vị khác nhau.

## Các bước đã thực hiện qua UI

1. Mở phiên Chrome hiển thị mới, đăng nhập `cbnv_tw_01`, lấy OTP bằng cách mở và đọc thư trên UI MailHog.
2. Vào **Đào tạo, tập huấn > Khóa học** qua menu UI.
3. Xác nhận khóa học seed `KH-20260807-001` hiển thị trên danh sách với tên chứa `QA-RV347-20260807`, trạng thái **Đã duyệt**.
4. Mở `KH-QAW7-HOINGHI` từ danh sách UI, lần lượt chọn **Học viên**, **Kết quả**, **Công bố kết quả**; đọc cùng dòng `Nguyễn Văn Ngọc` và ghi nhận **Đơn vị = TKM** trên cả ba tab.
5. Quay lại danh sách bằng nút UI, mở `AAA-KH-TW`, lần lượt chọn cùng ba tab; đọc cùng dòng `Học viên TW 01` và ghi nhận **Đơn vị trống** (`-`/`—`) trên cả ba tab.

## Bằng chứng UI

- Ảnh chụp trực tiếp từ cửa sổ Chrome đã được lấy tại từng tab của hai fixture (tổng cộng 6 màn hình).
- Snapshot UI `AAA-KH-TW`:
  - **Học viên**: `Học viên TW 01` — `Đơn vị: -` — `Nguồn: Nhập tay` — `Trạng thái: Đã duyệt`.
  - **Kết quả**: `Học viên TW 01` — `Đơn vị: —` — thông báo `Kết quả đào tạo đã được phê duyệt`.
  - **Công bố kết quả**: `Học viên TW 01` — `Đơn vị: —` — `Trạng thái công bố: Đã công bố`.
- Snapshot UI `KH-QAW7-HOINGHI`:
  - **Học viên**: `Nguyễn Văn Ngọc` — `Đơn vị: TKM` — `Trạng thái: Đã duyệt`.
  - **Kết quả**: `Nguyễn Văn Ngọc` — `Đơn vị: TKM`.
  - **Công bố kết quả**: `Nguyễn Văn Ngọc` — `Đơn vị: TKM`.

## Đánh giá

Cùng một học viên không có đơn vị không bị hệ thống tự gán đơn vị quản lý khi chuyển giữa ba tab; cùng một học viên có đơn vị thật vẫn giữ nguyên `TKM`. Không còn tái hiện sai lệch được mô tả trong bug. Verdict: **PASS**.

Report này thay thế kết luận BLOCKED trước đó; nguyên nhân BLOCKED cũ (mất dữ liệu gốc) vẫn được bảo lưu như lịch sử và đã được xử lý bằng dữ liệu thay thế nêu trên.
