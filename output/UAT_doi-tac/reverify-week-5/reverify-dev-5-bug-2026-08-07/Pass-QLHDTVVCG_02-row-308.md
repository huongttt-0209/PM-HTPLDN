# Re-verify dev — QLHDTVVCG_02 (row 308)

- Môi trường: dev `https://18.143.165.120.nip.io`
- Công cụ: Chrome DevTools MCP, cửa sổ Chrome hiển thị; không dùng Playwright, không gọi API trực tiếp
- Thời điểm kiểm tra: 08/08/2026 (Asia/Ho_Chi_Minh)
- Tài khoản: cán bộ nghiệp vụ Trung ương đăng nhập bằng UI và OTP MailHog UI
- Kết luận: **PASS — đề xuất `Trạng thái dev fix = Test done`**

## Căn cứ chấm

Đối chiếu bug gốc với cột **DEV phản hồi lần 1** và nội dung BA đã chốt ngày 06/08/2026 theo hướng A:

- Giữ quyết định BA ngày 11/05/2026: không có menu Hợp đồng tư vấn độc lập.
- Lối vào hợp lệ là màn ngữ cảnh **Chi tiết Vụ việc** hoặc **Lịch sử TVV**.
- Vì vậy không xem việc thiếu menu Hợp đồng riêng là lỗi; lần verify này chấm tại **Chi tiết Vụ việc → HĐ tư vấn liên kết**.

## Dữ liệu và lối vào đã kiểm tra

1. Từ menu **Vụ việc HTPL**, tìm bằng UI mã `VV-BTP-TW-20260804-002`: danh sách từ 60 còn 1 bản ghi.
2. Bấm **Xem** để mở Chi tiết Vụ việc, sau đó mở accordion **HĐ tư vấn liên kết**.
3. Bảng ngữ cảnh tải 3 hợp đồng (`1-3 / 3 mục`):

| Mã HĐ | Bên B | Giá trị | Bắt đầu → Kết thúc | Vụ việc | Tiến độ TT | Trạng thái |
|---|---|---:|---|---:|---:|---|
| `HDTV-20260807-0008` | QA TVV Seed28 Active | 150.000.000 VNĐ | 01/06/2026 → 20/06/2026 | 1 | 0% | Đang thực hiện |
| `HDTV-20260807-0007` | QA TVV PheDuyet TW R19 | 200.000.000 VNĐ | 07/08/2026 → 30/12/2026 | 1 | 25% | Đang thực hiện |
| `HDTV-20260807-0006` | Chuyên gia UAT QLNDTVVCG 38 | 250.000.000 VNĐ | 07/08/2026 → 25/08/2026 | 3 | 40% | Đang thực hiện |

Không seed thêm dữ liệu vì fixture hiện có đã đủ cả bộ lọc và comparator cảnh báo.

## Verify bộ lọc theo ngữ cảnh

Mỗi tiêu chí đều được thao tác trên UI, quan sát before/after và bấm **Xóa bộ lọc** để chứng minh restore về 3 bản ghi:

| Tiêu chí | Thao tác UI | Kết quả |
|---|---|---|
| Tên hợp đồng | Nhập `lao động` → Tìm kiếm | 3 → 1; chỉ còn `HDTV-20260807-0007`; reset 1 → 3 |
| Mã hợp đồng | Nhập `HDTV-20260807-0006` → Tìm kiếm | 3 → 1; đúng `0006`; reset về 3 |
| Bên B | Nhập `QA TVV Seed28 Active` → Tìm kiếm | 3 → 1; đúng `0008`; reset về 3 |
| Tư vấn viên | Chọn `TVV-BTP-TW-0016 — QA TVV PheDuyet TW R19` → Tìm kiếm | 3 → 1; đúng `0007`; reset về 3 |
| Khoảng ngày | Chọn 01/06/2026–30/06/2026 → Tìm kiếm | 3 → 1; đúng `0008`; reset về 3 |

Network do các thao tác UI tạo xác nhận tham số lọc được gửi đúng và đều thành công:

- Tên: request 348, `search=lao động`, HTTP 200.
- Mã: request 351, `search=HDTV-20260807-0006`, HTTP 200.
- Bên B: request 352, `search=QA TVV Seed28 Active`, HTTP 200.
- TVV: request 356 có `tuVanVienId`, HTTP 200.
- Khoảng ngày: request 360 có đủ `tuNgay=2026-06-01&denNgay=2026-06-30`, HTTP 200.
- Các lượt reset tải lại bảng không filter bằng HTTP 200/304.

## Đối chiếu bảng và định dạng

| Hạng mục bug gốc | Kết quả verify |
|---|---|
| Trường/cột theo màn ngữ cảnh BA chốt | **Đạt** — đủ 11 nhãn: Mã hợp đồng, Tên hợp đồng, Bên A, Bên B, Giá trị (VNĐ), Ngày bắt đầu, Ngày kết thúc, Vụ việc, Tiến độ TT, Trạng thái, Hành động |
| Mã và dữ liệu từng dòng | **Đạt** — 3 mã HĐ và nội dung đúng theo từng fixture, không lẫn dòng sau các lượt lọc/reset |
| Tiền | **Đạt** — `150.000.000 VNĐ`, `200.000.000 VNĐ`, `250.000.000 VNĐ`, có dấu chấm phân tách và đơn vị |
| Ngày | **Đạt** — toàn bộ ngày hiển thị `dd/MM/yyyy` |
| Số vụ việc | **Đạt** — badge xanh tương ứng 1, 1, 3 |
| Tiến độ thanh toán | **Đạt** — progress bar và chữ 0%, 25%, 40%; DOM có `role=progressbar` và `aria-valuenow` tương ứng |
| Trạng thái | **Đạt** — badge/tag `Đang thực hiện`, không lộ mã enum kỹ thuật |
| Hành động | **Đạt** — đủ Xem chi tiết, Sửa, Xóa qua biểu tượng có nhãn truy cập |

## Cảnh báo hợp đồng sắp hết hạn

- `HDTV-20260807-0006` kết thúc **25/08/2026**, còn 17 ngày tại thời điểm verify: UI hiển thị **đỏ và đậm**; computed style `rgb(255, 77, 79)`, font-weight `600`.
- Comparator `HDTV-20260807-0007` kết thúc **30/12/2026**, xa hơn 30 ngày: UI hiển thị màu chữ thường `rgb(31, 31, 31)`, font-weight `400`.

Kết quả chứng minh cảnh báo được áp dụng có điều kiện, không tô đỏ toàn bộ dữ liệu.

## Bố cục và ngôn ngữ

- Viewport hiện tại: `1440×736`; chiều rộng trang `scrollWidth = clientWidth = 1432`, không có cuộn ngang toàn trang.
- Bảng có nội dung rộng 1700 px trong vùng 972 px và dùng cuộn ngang nội bộ `overflow-x: auto`; cuộn sang phải trên UI xem được đầy đủ Giá trị, Ngày bắt đầu/kết thúc, badge Vụ việc, Tiến độ TT, Trạng thái và Hành động mà không làm vỡ trang.
- Tên hợp đồng dài được giới hạn 2 dòng (`-webkit-line-clamp: 2`, `overflow: hidden`); chiều cao dòng 65 px, không thấy chữ tràn hoặc đè lên hàng/cột khác.
- Các nhãn hệ thống, filter, nút, trạng thái và phân trang đều dùng tiếng Việt; không tìm thấy mã `DANG_THUC_HIEN` hoặc nhãn tiếng Anh thô trên UI. Chuỗi không dấu ở tên `0008` là dữ liệu fixture do người dùng nhập, không phải nhãn hệ thống.

## Console và Network

- Không có JavaScript error hoặc warning trong toàn bộ luồng quyết định.
- DevTools ghi 1 Issue: hai form field thiếu thuộc tính `id` hoặc `name`; không gây lỗi chức năng của case này.
- Không có request 4xx/5xx. Các request tìm Vụ việc, tải bảng và lọc hợp đồng đều HTTP 200/304.

## Bằng chứng hình ảnh đã chụp trong Chrome DevTools

1. Danh sách Vụ việc trước/sau khi tìm đúng mã và màn Chi tiết Vụ việc.
2. Baseline 3 hợp đồng tại accordion HĐ tư vấn liên kết.
3. Kết quả 3 → 1 riêng cho tên, mã, bên B và tư vấn viên; ảnh baseline restore sau reset.
4. Kết quả khoảng ngày 01/06/2026–30/06/2026 chỉ còn `0008`, sau đó reset về 3.
5. Góc trái bảng ở baseline và trạng thái cuộn ngang sang phải; ảnh phía phải thể hiện ngày `25/08/2026` màu đỏ, comparator `30/12/2026` màu thường, badge 1/1/3, progress 0/25/40% và trạng thái.

Các ảnh được capture trực tiếp và hiển thị trong kết quả Chrome DevTools của phiên verify.

## Kết quả verify đề xuất ghi Sheet

`Pass theo BA confirm 06/08 hướng A: truy cập danh sách HĐ qua Chi tiết Vụ việc; bộ lọc tên/mã/bên B, TVV và khoảng ngày đều lọc đúng và reset đúng. Bảng hiển thị đủ trường, đúng định dạng tiền/ngày/badge/progress/trạng thái; HĐ kết thúc 25/08/2026 cảnh báo đỏ, comparator 30/12/2026 không đỏ; không tràn/đè, nhãn tiếng Việt.`
