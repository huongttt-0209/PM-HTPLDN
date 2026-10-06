# Bảng đối chiếu điều kiện — QLHSVV_OOS_01 (row 133, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Xem tài liệu đính kèm của hồ sơ vụ việc HTPL — FR-V.I-07 (UC57), màn SCR-V.I-03 (Accordion 3 — Tài liệu đính kèm)
**Nội dung TC:** cột "Loại" của bảng tài liệu đính kèm hiển thị mã nội bộ `BO_SUNG` thay vì nhãn tiếng Việt đọc được.
**Loại bug:** giá trị hiển thị phụ thuộc **loại tài liệu cụ thể của bản ghi** (mỗi loại tài liệu là một giá trị enum khác nhau) → KHÔNG phải bug tĩnh, BẮT BUỘC khai rõ đo trên bản ghi nào / loại tài liệu gì.
**Ngày verify lại:** 2026-08-04 · **Tài khoản QA dùng:** `cbnv_tw_01` (CB_NV_TW, đơn vị BTP · TW, `donViId = 00000000-0000-4000-8000-000000000001`)

> **Nguồn gốc dòng TC:** lỗi do QA tự phát hiện khi verify QLHSVV_07 (row 128), nằm ngoài tiêu chí của phiếu nên mở dòng mới. **Không có evidence đối tác cho riêng lỗi này** — cột giữa dưới đây ghi điều kiện của **BUG GỐC do QA dựng ngày 03/08/2026**, không suy diễn điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Bug gốc (QA dựng 03/08/2026) | Mình test lại (04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw_03` — vai trò `CB_NV_TW` ("CB Nghiệp vụ - Trung ương #03"), đơn vị `BTP · TW` | `cbnv_tw_01` — vai trò `CB_NV_TW` ("CB Nghiệp vụ - Trung ương #01"), đơn vị `BTP · TW`, `donViId = 00000000-0000-4000-8000-000000000001` **trùng đúng** đơn vị của tài khoản bug gốc (đọc từ phiên đăng nhập thực) | Không |
| Entity + **trạng thái** (state machine) | Vụ việc `VV-BTP-TW-20260803-002`, trạng thái **"Đã tiếp nhận"**, mở ở màn **Chi tiết** (`/vu-viec/4f340b58-…`), nhóm "Tài liệu đính kèm" đã bung | **Đúng cùng bản ghi** `VV-BTP-TW-20260803-002` (`/vu-viec/4f340b58-ce76-4274-86ad-a0e3cd0c638d`), badge trạng thái vẫn **"Đã tiếp nhận"**, mở ở màn Chi tiết, nhóm "Tài liệu đính kèm" đã bung | Không |
| Dữ liệu tiền đề (tệp + **loại tài liệu**) | Hồ sơ có **1 tệp**: `QLHSVV_07_qa.jpg` — **loại tài liệu `BO_SUNG`**, định dạng JPG, 38.8 KB, trạng thái quét `SACH`; ngày tải 03/08/2026 16:13 | **Đúng cùng tệp đó, không tạo tệp mới**: `QLHSVV_07_qa.jpg` — máy chủ vẫn trả `loaiTaiLieu = "BO_SUNG"`, `dinhDang = "JPG"`, `kichThuoc = 39772`, `trangThaiQuet = "SACH"`, ngày tải 03/08/2026 16:13 ⇒ dữ liệu gốc **không đổi**, chỉ lớp hiển thị đổi | Không |
| Input / thao tác đo | Bung nhóm "Tài liệu đính kèm" → đọc ô ở **cột "Loại"** trên hàng tệp | Bung nhóm "Tài liệu đính kèm" → đọc ô ở **cột "Loại"** trên hàng tệp, đo 2 cách: `innerText` từng ô của hàng + ảnh chụp full-res đọc bằng mắt | Không |

## Ghi chú đóng GAP

- **Đo trên đúng bản ghi của bug gốc, không phải bản ghi mới.** Vì đây là lỗi **lớp hiển thị** (dữ liệu lưu trong CSDL vẫn là mã enum `BO_SUNG` — máy chủ trả nguyên như cũ), bản ghi cũ vẫn là phép thử hợp lệ: nếu chưa sửa thì màn hình vẫn phải in ra `BO_SUNG`. Không thuộc nhóm "bug về trường lưu trong CSDL" (không cần dựng dữ liệu mới).
- **Khác số thứ tự tài khoản KHÔNG phải GAP:** `_01` và `_03` cùng vai trò `CB_NV_TW`, cùng đơn vị `BTP · TW` (`donViId` trùng khít), cùng quyền đọc vụ việc; cột "Loại" là nhãn hiển thị chung của bảng, không phân biệt theo người dùng.
- **Đối chứng cùng hàng làm mốc chứng minh phép đo đúng:** cột "Trạng thái quét" trên **chính hàng đó** hiện "Sạch" trong khi máy chủ trả `SACH` — chứng tỏ phép đo đang đọc **chữ hiển thị** chứ không phải dữ liệu thô; nếu cột "Loại" chưa sửa thì phép đo này vẫn phải bắt được `BO_SUNG`.
- **Đo 2 cách độc lập, không dùng `textContent`:** (1) đọc `innerText` từng ô của hàng — kết quả `["QLHSVV_07_qa.jpg", "Bổ sung", "JPG", "38.8 KB", "Sạch", "03/08/2026 16:13", "Xem\nTải"]`, ô cột "Loại" có diện tích chiếm chỗ thật (rộng 128 px × cao 61 px, loại trừ hàng đo ẩn cao 0 px của bảng); (2) ảnh chụp full-res đọc bằng mắt cũng ra "Bổ sung".
- **Đã tải lại trang bỏ bộ nhớ đệm** trước khi đo, gói giao diện đang chạy `index-BrKDNUvo.js` (bản `HTPLDN · V1.0.5`) — loại trừ mã cũ còn sống trong tab.

**Kết luận: 0 GAP** — đo lại đúng bản ghi, đúng loại tài liệu, đúng màn hình và đúng thao tác của bug gốc.
