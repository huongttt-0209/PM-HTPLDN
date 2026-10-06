# Vế B — vai trò Quản trị hệ thống · đo MỘT LẦN, áp chung 21 phiếu

**Vì sao đo chung:** cả 23 loại báo cáo dùng **một màn duy nhất** `/bao-cao`. Việc chặn nằm ở cửa vào
màn + ở tầng máy chủ, không phụ thuộc loại báo cáo nào được chọn.

**Vì sao có vế này:** ô `TKM phản hồi lần 1` của cả 21 dòng ghi *"TKM retest 31/7: Hệ thống hiển thị
thông báo `Forbidden`"* — triệu chứng phát sinh khi đăng nhập bằng vai trò Quản trị hệ thống. Nghiệp vụ
đã chốt ngày 06/08/2026: Quản trị hệ thống **không phải tác nhân** của chức năng báo cáo thống kê, nên
nhánh đúng là **chặn ở cửa vào + ẩn mục menu + câu từ chối bằng tiếng Việt**, không phải nhánh "quản trị
xuất được tệp".

## Điều kiện đo

| Hạng mục | Giá trị |
|---|---|
| Thời điểm | 2026-08-07 18:28–18:31 giờ VN (11:28–11:31 GMT) |
| Env | `https://18.143.165.120.nip.io` |
| Bó mã FE **đọc trong chính tab đang đo** | `assets/index-BbPPdate.js` — trùng khít bó mã máy chủ đang phục vụ |
| Nhãn phiên bản trên thanh bên | `HTPLDN · V1.0.10` (chỉ là nhãn, không phải định danh bản dựng) |
| Tài khoản | `admin` / `Secret@123` — hiển thị `Quản trị hệ thống`, đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`, phạm vi `Toàn quốc` |
| Cách vào phiên | Đăng nhập mới hoàn toàn trong ngữ cảnh trình duyệt tách biệt (`qtht`), có bước nhập mã xác thực |

## Kết quả 4 phép đo

### 1. Mục menu "Báo cáo thống kê" — ẩn hẳn ✅

Mở **toàn bộ** nhóm menu thu gọn rồi đếm: **32 mục**, không mục nào là "Báo cáo thống kê".

> Tổng quan · Hỏi đáp pháp lý · Đào tạo, tập huấn (Kế hoạch đào tạo · Chương trình đào tạo · Khóa học ·
> Kho tài liệu / Bài giảng · Ngân hàng câu hỏi & Đề kiểm tra · Giảng viên / Trợ giảng) · Mạng lưới Tư vấn
> viên (Tư vấn viên / Chuyên gia · Tổ chức tư vấn · Người hỗ trợ pháp lý) · Vụ việc HTPL · Chi trả chi phí ·
> Doanh nghiệp · Đánh giá hiệu quả · Biểu mẫu (Thư viện biểu mẫu · Danh sách biểu mẫu) · Tư vấn (Tư vấn
> chuyên sâu · Kho câu hỏi · Tư vấn nhanh) · Chương trình HTPLDN · Đợt báo cáo · Quản trị hệ thống (Danh
> mục dùng chung · Cấu hình hệ thống · Tài khoản & phân quyền · Vai trò · Nhật ký hệ thống)

Mục duy nhất có chữ "báo cáo" là **"Đợt báo cáo"** — đây là chức năng khác (quản lý đợt báo cáo định kỳ),
không phải màn Báo cáo thống kê của 21 phiếu.

**Ẩn chứ không làm mờ:** không có phần tử nào mang trạng thái vô hiệu hóa mang nhãn "Báo cáo thống kê" —
mục không tồn tại trong cây điều hướng.

Ảnh: [image/VE-B-01-QTHT-menu-khong-co-Bao-cao-thong-ke.png](../image/VE-B-01-QTHT-menu-khong-co-Bao-cao-thong-ke.png)

### 2. Vào thẳng địa chỉ `/bao-cao` — không mở được màn ✅

Đối chứng độc lập với phép đo menu: điều hướng thẳng tới `/bao-cao` bằng bộ định tuyến của chính ứng dụng.

| Quan sát | Kết quả |
|---|---|
| Địa chỉ sau khi điều hướng | quay về `https://18.143.165.120.nip.io/dashboard` |
| Ô chọn loại báo cáo | **không hiện** |
| Nút "Xem báo cáo" | **không hiện** |
| Nút "Xuất PDF" / "Xuất Excel" / "Xuất file" | **không hiện** (0 nút) |

Không có cảnh "vào được màn, xem đủ số liệu rồi mới chặn lúc bấm xuất".

### 3. Bước XEM ở tầng máy chủ — từ chối bằng tiếng Việt ✅

Dùng chính phiên đăng nhập Quản trị hệ thống gọi thẳng dịch vụ xem báo cáo:

| Dịch vụ | Mã trả về | Thân phản hồi |
|---|---|---|
| `GET /api/v1/bao-cao/hoi-dap` | **403** | `ERR-RPT-05` — "Bạn không có quyền xem báo cáo này" |
| `GET /api/v1/bao-cao/vu-viec-tiep-nhan` | **403** | `ERR-RPT-05` — "Bạn không có quyền xem báo cáo này" |
| `GET /api/v1/bao-cao/chi-phi-chi-tra` | **403** | `ERR-RPT-05` — "Bạn không có quyền xem báo cáo này" |

### 4. Bước XUẤT TỆP ở tầng máy chủ — từ chối bằng tiếng Việt, không sinh tệp ✅

| Dịch vụ | Mã trả về | Thân phản hồi |
|---|---|---|
| `POST /api/v1/bao-cao/export` | **403** | `ERR-RPT-08` — "Bạn không có quyền thực hiện thao tác này" |

Không tệp nào được tạo cho vai trò Quản trị hệ thống.

## Kết luận vế B

| Điều phải chứng minh | Kết quả |
|---|---|
| Mục menu bị **ẩn** (không phải làm mờ) | ✅ ĐẠT |
| Chặn ngay ở **cửa vào**, không mở màn hình | ✅ ĐẠT |
| Câu đẩy ra người dùng là **tiếng Việt**, không phải `Forbidden` / mã kỹ thuật | ✅ ĐẠT — cả hai bước |
| Máy chủ **không sinh tệp** cho vai trò Quản trị hệ thống | ✅ ĐẠT |

**Chuỗi `Forbidden` và mã `ERR-PERM-SYS-00-01` mà đối tác báo ngày 31/07 KHÔNG còn tái hiện** ở bất kỳ
bước nào — cả bước xem lẫn bước xuất.

**Ghi nhận thêm:** bản dựng này dùng `ERR-RPT-08` cho bước xuất — đúng mã mới mà nghiệp vụ chốt ngày
06/08. Lượt đo sáng cùng ngày (bó mã cũ hơn) còn trả `ERR-RPT-05` cho bước xuất; nay đã tách đúng hai mã
cho hai bước.
