# Re-verify dev — QLHDTVVCG_15 (row 321)

- Môi trường: dev `https://18.143.165.120.nip.io`
- Công cụ: Chrome DevTools MCP, cửa sổ Chrome hiển thị; không dùng Playwright, không gọi API trực tiếp
- Thời điểm kiểm tra: 08/08/2026 (Asia/Ho_Chi_Minh)
- Kết luận: **BLOCKED / INCONCLUSIVE — không đủ điều kiện cập nhật `Test done` hoặc `Reopen`**

## Căn cứ BA/DEV

Đối chiếu bug gốc với cột **DEV phản hồi lần 1** và BA chốt 06/08/2026 hướng B:

- Giữ quyết định bỏ menu Hợp đồng tư vấn riêng; lối vào hợp lệ là màn ngữ cảnh Chi tiết Vụ việc.
- Chuỗi thành công dùng chung cho tạo mới/cập nhật theo `INF-HDTV-01` là chính xác **“Đã lưu hợp đồng”**.
- Sau lưu, đóng biểu mẫu và trả người dùng về ngữ cảnh đã mở biểu mẫu là hành vi hợp lệ.

## Dữ liệu đã tạo qua UI

Từ `VV-BTP-TW-20260804-002` → mở **HĐ tư vấn liên kết** → bấm **+ Tạo hợp đồng**, nhập fixture có marker `QA-R321-20260808-0012`:

| Nhóm | Dữ liệu đã nhập |
|---|---|
| Thông tin chính | Tên `Hợp đồng QA row321 tạo mới đầy đủ QA-R321-20260808-0012`; số HĐ `SO-QA-R321-0012`; Bên B `Doanh nghiệp QA-R321-20260808-0012`; TVV `TVV-BTP-TW-0016 — QA TVV PheDuyet TW R19`; giá trị 300.000.000 VNĐ; 08/08/2026–31/12/2026; nội dung và ghi chú mang marker |
| Mốc tiến độ | 2 mốc: `Mốc 1 QA-R321 phân tích hồ sơ` ngày 15/08/2026; `Mốc 2 QA-R321 bàn giao kết quả` ngày 30/09/2026; đều `Chưa bắt đầu` |
| Thanh toán giai đoạn | 2 giai đoạn: 100.000.000 VNĐ ngày 20/08/2026 và 150.000.000 VNĐ ngày 15/10/2026; tổng 250.000.000 ≤ giá trị HĐ 300.000.000 |
| Vụ việc liên kết | 2 vụ việc: `VV-BTP-TW-20260804-002` tự liên kết theo ngữ cảnh và `VV-BTP-TW-20260804-003` chọn thêm bằng UI |
| Tệp đính kèm tại màn tạo | Không có file input; UI hiển thị **“Vui lòng lưu hợp đồng trước khi đính kèm tài liệu.”** |

## Kết quả lưu tạo mới

- Bấm **Thêm mới** đúng một lần trên UI.
- Network do UI tạo: `POST /api/v1/hop-dong-tu-vans`, request 393, HTTP **201**.
- MutationObserver được cài trước khi bấm đã bắt exact toast **“Đã lưu hợp đồng”** tại một mốc thời gian `2026-08-07T17:19:17.178Z` (00:19:17 giờ Việt Nam). Các node wrapper/nested của Ant Design lặp cùng chuỗi và cùng timestamp, tương ứng một toast UI.
- Biểu mẫu đóng; URL trước/sau giữ nguyên Chi tiết Vụ việc `.../vu-viec/6bf98a2e-77ee-4c03-8e1f-a51561406a3b` theo BA; bảng HĐ tư vấn liên kết tự tải lại từ 3 thành 4 dòng.
- Bản ghi mới có mã **`HDTV-20260808-0001`**, đúng khuôn `HDTV-{YYYYMMDD}-{seq}` và đúng ngày tạo 08/08/2026.
- Bảng ngữ cảnh hiển thị trạng thái **Đang thực hiện**, giá trị 300.000.000 VNĐ, khoảng ngày đúng và badge 2 vụ việc.

## Persistence sau mở chi tiết và hard reload

Mở bản ghi mới qua nút **Xem chi tiết**, route:

`/hop-dong-tv/1d63d6ba-d194-423f-804e-89833b958bff`

Sau đó hard reload (`ignoreCache=true`) và quan sát lại UI:

| Tiêu chí quyết định | Kết quả |
|---|---|
| Mã hợp đồng | **Đạt** — `HDTV-20260808-0001` còn ở tiêu đề và trường Mã hợp đồng |
| Trạng thái | **Đạt** — `Đang thực hiện` còn ở badge và trường Trạng thái |
| Trường chính | **Đạt** — Chi tiết giữ nguyên tên, số HĐ, Bên A/B, giá trị, ngày ký, ngày bắt đầu/kết thúc, nội dung và ghi chú; mở lại Chỉnh sửa sau reload cũng xác nhận TVV `TVV-BTP-TW-0016 — QA TVV PheDuyet TW R19` còn được chọn |
| Mốc tiến độ | **Đạt** — đủ 2/2 mốc, đúng tên/ngày/trạng thái/ghi chú |
| Thanh toán giai đoạn | **Đạt** — đủ 2/2 giai đoạn, đúng 100tr + 150tr, ngày, trạng thái Chưa thanh toán và ghi chú |
| Vụ việc liên kết | **Đạt** — đủ 2/2 mã `-002` và `-003` |
| Tệp đính kèm | **Chưa đo được** — chi tiết hiển thị `Chưa có tài liệu đính kèm` vì màn tạo yêu cầu lưu trước; bước upload ở Chỉnh sửa bị chặn bởi sandbox của công cụ, xem dưới |

Nhật ký hoạt động trên UI có dòng Tạo mới lúc 08/08/2026 00:19 với endpoint `POST /api/v1/hop-dong-tu-vans`, HTTP 201.

## Blocker khi verify tệp đính kèm

Theo chỉ dẫn của chính UI, mở **Chỉnh sửa** sau khi hợp đồng đã tồn tại:

- Form Chỉnh sửa có 1 `input[type=file]` và control **“Kéo thả hoặc nhấp để chọn tệp đính kèm”**.
- Ràng buộc hiển thị: tối đa 10 tệp; `.pdf, .doc, .docx, .xls, .xlsx, .jpg, .png`; tối đa 20MB/tệp.
- Fixture chuẩn bị là file thật `QA-R321-20260808-0012.docx`, 36KB; lệnh `file` xác nhận `Microsoft OOXML`.

Đã thử đúng ba cách bằng công cụ upload của Chrome DevTools:

1. Đường dẫn tuyệt đối trong workspace.
2. Đường dẫn tương đối trong workspace.
3. Bản sao hợp lệ trong thư mục tạm `/tmp`.

Cả ba đều bị DevTools MCP từ chối **trước khi trình duyệt nhận file** với lỗi `not within any of the configured workspace roots`. Vì đây là giới hạn cấu hình công cụ, không phải response/hành vi của web, không được dùng để kết luận sản phẩm lỗi. Đã bấm Escape/Hủy chỉnh sửa; không phát sinh request upload hoặc cập nhật, không thay đổi bản ghi.

Thiếu bằng chứng tệp được upload và còn tồn tại sau reload là thiếu một ý quyết định của bug gốc. Theo điều kiện chấm, case không được Pass oan và cũng không đủ bằng chứng để Reopen.

## Destination sau save

Actual sau tạo mới:

- Modal đóng.
- Màn dừng ở **Chi tiết Vụ việc `VV-BTP-TW-20260804-002`**.
- Bảng **HĐ tư vấn liên kết** tự tải lại và hiển thị bản ghi mới.

Hành vi này khớp BA 06/08 hướng B về route contextual; không coi việc không có/quay về menu danh sách Hợp đồng riêng là lỗi.

## Console và Network

- Không có JavaScript error hoặc warning trong luồng tạo, reload và mở Chỉnh sửa.
- DevTools có các Issue về form field thiếu label hoặc thiếu `id/name`; không chặn luồng lưu.
- Request tạo mới HTTP 201; các request reload/chi tiết/audit đều HTTP 200/304; không có request 4xx/5xx của sản phẩm trong các bước quyết định.

## Bằng chứng hình ảnh đã chụp trong Chrome DevTools

1. Form trước lưu với 2 giai đoạn, tổng 250tr/300tr, 2 vụ việc liên kết và dòng yêu cầu lưu trước khi đính kèm.
2. Màn Chi tiết Vụ việc ngay sau lưu, modal đã đóng và bảng tự tải lại.
3. Full-page Chi tiết hợp đồng sau hard reload: mã, trạng thái, trường chính, 2 linked cases, 2 mốc và 2 giai đoạn còn nguyên; phần tệp ghi Chưa có tài liệu đính kèm.
4. Accessibility snapshot màn Chỉnh sửa xác nhận upload control và các ràng buộc định dạng/dung lượng.

Các ảnh/snapshot được capture trực tiếp trong phiên Chrome DevTools; không dùng Playwright.

## Dữ liệu môi trường đã thay đổi

- Đã tạo hợp đồng `HDTV-20260808-0001` trên dev, id `1d63d6ba-d194-423f-804e-89833b958bff`.
- Bản ghi có 2 mốc tiến độ, 2 giai đoạn thanh toán và 2 liên kết vụ việc.
- Không upload tệp, không lưu chỉnh sửa, không sửa/xóa dữ liệu khác.

## Điều kiện để chốt lại

Cần cấu hình Chrome DevTools MCP cho phép đọc một thư mục upload, rồi thực hiện qua UI: mở Chỉnh sửa → chọn file DOCX thật → Lưu → reload/mở lại Chi tiết → xác nhận tên tệp còn tồn tại. Khi có bằng chứng này mới đủ dữ liệu quyết định Pass/Reopen cho phần attachment.
