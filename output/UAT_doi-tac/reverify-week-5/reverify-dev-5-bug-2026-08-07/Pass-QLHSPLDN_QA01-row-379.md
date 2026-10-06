# Re-verify dev — QLHSPLDN_QA01 (row 379)

- Môi trường: dev `https://18.143.165.120.nip.io`
- Công cụ: Chrome DevTools MCP, cửa sổ Chrome hiển thị
- Thời điểm kiểm tra cuối: 08/08/2026 10:31–10:45 (Asia/Ho_Chi_Minh)
- DEV phản hồi lần 1: rỗng; đối chiếu theo bug gốc/SRS
- Kết luận cuối: **PASS — cập nhật Sheet `Test done`**

## Lượt verify cuối — PASS

### Tiền điều kiện

- Không dùng `cbnv_tw` để ra verdict vì tài khoản này từng được QA nhập CCCD thử `000000000001` ngày 07/08/2026, không còn thỏa dữ liệu gốc.
- Dùng `cbnv_tw_05`, đúng lớp người dùng cần kiểm: tài khoản `Cán bộ`, trạng thái `Hoạt động`, vai trò `CB_NV_TW`, đơn vị cấp TW, đăng nhập `LOCAL` và chưa liên kết VNeID.
- Mở tài khoản này từ **Quản trị hệ thống → Tài khoản & phân quyền** bằng UI. Request chi tiết do chính UI tạo trả đúng ID tài khoản, loại `Cán bộ`, vai trò `CB_NV_TW`; DTO hiện tại không còn trả thuộc tính `cccd`. Không gọi API ngầm.

### Kết quả đo

1. Đăng nhập mới `cbnv_tw_05` qua form UI, lấy OTP trên MailHog UI và xác thực thành công.
2. Ngay sau đăng nhập: Dashboard tải bình thường, không có text **“Cập nhật thông tin bắt buộc”**, số dialog hiển thị bằng `0`.
3. Hard reload lần 1 (`ignoreCache=true`): không xuất hiện modal; bấm menu **Hỏi đáp pháp lý** thành công, danh sách tải đủ **23** bản ghi.
4. Hard reload lần 2 tại `/hoi-dap` (`ignoreCache=true`): không xuất hiện modal; bấm menu **Vụ việc HTPL** thành công, danh sách tải đủ **60** bản ghi.
5. Sau cả hai reload, các nút chức năng trên màn vẫn thao tác được. Không ghi nhận JavaScript error trong console.

### Đối chiếu bug gốc

| Điều kiện | Kết quả cuối |
|---|---|
| Cán bộ nội bộ, `CB_NV_TW`, cấp TW, `LOCAL` | Đạt |
| Đăng nhập mới bằng UI + OTP UI | Đạt |
| Không bị modal CCCD chặn ngay sau đăng nhập | Đạt |
| Reload tối thiểu 2 lần | Đạt |
| Không có modal sau từng reload | Đạt |
| Dùng được chức năng sau reload | Đạt — Hỏi đáp 23 bản ghi; Vụ việc 60 bản ghi |
| Console | 0 JavaScript error |

### Bằng chứng

- `evidence-QLHSPLDN_QA01-2026-08-08/01-cbnv-tw05-login-no-modal.png`
- `evidence-QLHSPLDN_QA01-2026-08-08/02-cbnv-tw05-reload1-hoi-dap.png`
- `evidence-QLHSPLDN_QA01-2026-08-08/03-cbnv-tw05-reload2-vu-viec.png`
- `evidence-QLHSPLDN_QA01-2026-08-08/04-sheet-r379-test-done.png`

### Cập nhật Sheet

- Ô `R379` được đổi qua dropdown UI từ `Fixed` sang `Test done`.
- Đã chọn lại đúng ô `R379`, đọc lại formula bar là `Test done` và xác nhận tài liệu ở trạng thái **Đã lưu vào Drive**.

Ghi chú quan sát: API/biểu mẫu của bản dựng hiện tại không còn expose trường `cccd`, nên không thể chụp literal `cccd:null`. Đây là khoảng trống quan sát dữ liệu, không còn là lỗi chức năng người dùng: trên đúng lớp tài khoản cán bộ nội bộ dùng đăng nhập cục bộ, cổng ép nhập CCCD không xuất hiện và hệ thống sử dụng bình thường qua hai lần reload.

## Lượt verify trước — lịch sử BLOCKED / INCONCLUSIVE

### Lý do từng chưa được phép chấm Pass

Luồng đăng nhập UI thực tế xác nhận được tài khoản là cán bộ nội bộ và dùng phương thức `LOCAL`, nhưng không có bằng chứng trực tiếp cho giá trị **`cccd=null`**:

- `GET /api/v1/auth/me` do chính luồng đăng nhập UI tạo: HTTP 200, `authMethod="LOCAL"`, `vaiTro=["CB_NV_TW"]`, `hoTen="CB Nghiệp vụ - Trung ương #05"`.
- Response `/auth/me` **không có key `cccd`**; không trả literal `"cccd": null`.
- Mở **Hồ sơ cá nhân** qua UI làm phát sinh `GET /api/v1/auth/profile` HTTP 200; response tiếp tục xác nhận `authMethod="LOCAL"`, `vaiTro=["CB_NV_TW"]`, nhưng cũng **không có key `cccd`**.
- Form Hồ sơ cá nhân hiển thị Tên đăng nhập, Email, Họ tên, Điện thoại và Vai trò; không có trường CCCD để đọc giá trị trống.

Việc response omit key có thể tương ứng dữ liệu null, nhưng đây chỉ là suy luận. Theo điều kiện chấm, không dùng suy luận này để Pass.

## Các bước đã thực hiện qua UI

1. Đăng nhập tài khoản cán bộ nội bộ qua form UI; lấy OTP từ MailHog UI và xác nhận OTP trên UI.
2. Sau đăng nhập, Dashboard hiển thị bình thường; không có modal **“Cập nhật thông tin bắt buộc”**.
3. Mở Hồ sơ cá nhân qua menu người dùng; xác nhận vai trò hiển thị `CB_NV_TW` và chụp trạng thái form.
4. **Hard reload lần 1** tại `/profile` (`ignoreCache=true`):
   - Không có text/modal “Cập nhật thông tin bắt buộc”.
   - Không có dialog đang mở trong accessibility snapshot.
   - Sau reload, bấm menu **Hỏi đáp pháp lý**; route `/hoi-dap` mở thành công và tải danh sách 23 bản ghi.
5. **Hard reload lần 2** tại `/hoi-dap` (`ignoreCache=true`):
   - Không có text/modal “Cập nhật thông tin bắt buộc”.
   - Sau reload, bấm menu **Vụ việc HTPL**; route `/vu-viec/danh-sach` mở thành công và tải danh sách 60 bản ghi.
6. Kiểm tra DOM ở trạng thái cuối: `coTextModal=false`, số modal/dialog đang hiển thị `0`.

Do modal không xuất hiện ở đăng nhập ban đầu và cả hai lần reload, ba đường đóng **X / Escape / click ngoài** thuộc nhánh điều kiện “nếu modal có” nên không áp dụng.

## Đối chiếu tiêu chí quyết định

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| Tài khoản `LOCAL` | Đạt | `/auth/me` 200 và `/auth/profile` 200 đều trả `authMethod="LOCAL"` |
| Vai trò cán bộ nội bộ | Đạt | Network và UI profile đều hiển thị `CB_NV_TW`; header hiển thị Cán bộ Nghiệp vụ Trung ương |
| Dữ liệu `cccd=null` | **Chưa chứng minh** | Hai response đều omit key `cccd`; UI profile không có trường CCCD |
| Reload tối thiểu 2 lần | Đạt | 2 hard reload có quan sát lại accessibility snapshot/UI |
| Không bị ép khai CCCD | Hành vi bề mặt đạt | Không xuất hiện modal ở login ban đầu, reload 1 và reload 2 |
| Chức năng dùng được sau reload 1 | Đạt | Mở Hỏi đáp pháp lý, danh sách 23 bản ghi tải thành công |
| Chức năng dùng được sau reload 2 | Đạt | Mở Vụ việc HTPL, danh sách 60 bản ghi tải thành công |

## Console và Network

- Network: `/auth/me` 200 sau xác thực OTP; hard reload sau đó có `/auth/me` 304; `/auth/profile` 200; danh sách Hỏi đáp 304; danh sách Vụ việc 200.
- Không ghi nhận request 4xx/5xx trong các thao tác quyết định.
- Console không có JavaScript error; có 2 DevTools Issue về form field thiếu `id` hoặc `name`, không chặn luồng kiểm tra này.

## Bằng chứng hình ảnh đã chụp trong Chrome DevTools

1. Dashboard ngay sau đăng nhập: không có modal, header đúng cán bộ nội bộ.
2. Hồ sơ cá nhân: vai trò `CB_NV_TW`, không có trường CCCD.
3. Sau hard reload lần 1: Hồ sơ cá nhân không có modal.
4. Sau reload 1 và mở chức năng: danh sách Hỏi đáp tải thành công.
5. Sau hard reload lần 2: danh sách Hỏi đáp không có modal.
6. Sau reload 2 và mở chức năng: danh sách Vụ việc tải thành công.

Các ảnh được capture trực tiếp và hiển thị trong kết quả Chrome DevTools của phiên verify; không dùng Playwright.

## Hướng gỡ Blocked

Cần một bằng chứng UI/Network của chính tài khoản đăng nhập trả rõ `cccd: null` (hoặc UI profile hiển thị trường CCCD đang trống). Sau khi có prerequisite này, có thể dùng lại session/flow trên để chốt Pass vì hành vi bề mặt hiện tại không còn modal và chức năng vẫn thao tác được sau hai reload.
