# Hiện trạng menu "Báo cáo thống kê" với vai trò QTHT — đo bởi B1, 2026-08-07

> **Dùng cho B2/B3 (và B4 nếu cần).** File này chỉ ghi **quan sát menu + phép vào thẳng bằng địa chỉ**
> của vai trò `admin`/QTHT. **Mỗi agent vẫn phải tự chạy vế (a) trên đúng loại báo cáo của mình**, và
> nên tự chạy lại phép b2 với **địa chỉ mang `loai=` của case mình** (xem §4).

## 1. Điều kiện lượt đo

| Hạng mục | Giá trị |
|---|---|
| Thời điểm đo | **2026-08-07 15:02–15:04 giờ VN** |
| Môi trường | `https://18.143.165.120.nip.io` (nội bộ) |
| Tài khoản | **`admin` / `Secret@123`** — vai trò hiện trên giao diện: *Quản trị hệ thống*, đơn vị **BTP · TW** |
| Nhãn bản dựng ở chân sidebar | `HTPLDN · V1.0.10` |
| Bó mã FE thật đang chạy trong tab | **`assets/index-BbPPdate.js`** (đọc từ `document.querySelector('script[src]')`) — **khớp vân tay đầu lô** trong [`../BAN-DUNG-G1.md`](../BAN-DUNG-G1.md) |
| Phiên | Đăng nhập mới hoàn toàn (đã đăng xuất `cbnv_tw_04`, xoá `localStorage`/`sessionStorage` trước khi vào `/login`) |

## 2. Phép b1 — quét menu

**Kết quả: KHÔNG còn mục "Báo cáo thống kê" trong menu điều hướng của vai trò QTHT.**

Cách quét (không kết luận từ mắt nhìn):

- Đếm phần tử trong `<aside>` có chứa chuỗi `Báo cáo thống kê` → **0**.
- Kiểm cả `innerHTML` của `<aside>` (bắt được cả node bị ẩn bằng CSS) → **không khớp chuỗi nào**.
- Liệt kê 5 nhóm có submenu và kiểm **cả 5 đều đang bung** (`ant-menu-submenu-open`), không có nhóm nào
  gập lại che mục: *Đào tạo, tập huấn* (6 mục) · *Mạng lưới Tư vấn viên* (3) · *Biểu mẫu* (2) ·
  *Tư vấn* (3) · *Quản trị hệ thống* (5).
- Đếm mục bị làm mờ (`ant-menu-item-disabled` / `aria-disabled="true"`) → **0**.
  ⇒ Đây là **ẩn hẳn**, không phải làm mờ — đúng quy ước M-05 (`srs-v3.5/srs-v3.5.md:684`).

**Toàn bộ menu QTHT đọc được lượt này (31 mục):**

> Tổng quan · Hỏi đáp pháp lý · **Đào tạo, tập huấn** (Kế hoạch đào tạo · Chương trình đào tạo · Khóa học ·
> Kho tài liệu / Bài giảng · Ngân hàng câu hỏi & Đề kiểm tra · Giảng viên / Trợ giảng) ·
> **Mạng lưới Tư vấn viên** (Tư vấn viên / Chuyên gia · Tổ chức tư vấn · Người hỗ trợ pháp lý) ·
> Vụ việc HTPL · Chi trả chi phí · Doanh nghiệp · Đánh giá hiệu quả · **Biểu mẫu** (Thư viện biểu mẫu ·
> Danh sách biểu mẫu) · **Tư vấn** (Tư vấn chuyên sâu · Kho câu hỏi · Tư vấn nhanh) · Chương trình HTPLDN ·
> Đợt báo cáo · **Quản trị hệ thống** (Danh mục dùng chung · Cấu hình hệ thống · Tài khoản & phân quyền ·
> Vai trò · Nhật ký hệ thống)

⚠️ **Đừng nhầm "Đợt báo cáo" với "Báo cáo thống kê"** — *Đợt báo cáo* vẫn còn trong menu QTHT, đó là chức
năng khác, không phải màn báo cáo thống kê của cụm A.

Ảnh: [`../image/VVDTN_06-04-qtht-sidebar-khong-con-muc-bao-cao-thong-ke.png`](../image/VVDTN_06-04-qtht-sidebar-khong-con-muc-bao-cao-thong-ke.png)

## 3. Phép b2 — gõ thẳng địa chỉ màn báo cáo

**Kết quả: bị điều hướng đi, không vào được màn, không xem được số liệu.**

| Bước | Việc làm | Kết quả |
|---|---|---|
| Đối chứng trước | Gõ thẳng `https://18.143.165.120.nip.io/doanh-nghiep` trong **cùng phiên** `admin` | **Vào được**, dừng ở `/doanh-nghiep/danh-sach`, bảng danh sách doanh nghiệp có dữ liệu ⇒ **tải lại trang KHÔNG làm rớt phiên** — đây là bước bắt buộc, thiếu nó thì không phân biệt được "bị chặn quyền" với "bị đá vì hết phiên" |
| Phép b2 | Gõ thẳng `https://18.143.165.120.nip.io/bao-cao?loai=vu-viec-tiep-nhan&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` | Địa chỉ **tự đổi về `/dashboard`**, màn hiện Tổng quan hệ thống. Không thấy khối bộ lọc báo cáo, không có nút Xem báo cáo / Xuất Excel, không có số liệu báo cáo nào |
| Chốt phiên | Gọi kiểm phiên ngay sau đó | Phiên **còn sống** ⇒ đây là chặn quyền thật |

Ảnh: [`../image/VVDTN_06-05-qtht-go-dia-chi-man-bao-cao-bi-dua-ve-tong-quan.png`](../image/VVDTN_06-05-qtht-go-dia-chi-man-bao-cao-bi-dua-ve-tong-quan.png)

**Đã lặp lại phép b2 cho 2 loại báo cáo còn lại của B1 — kết quả giống hệt** (mỗi lượt là một phiên `admin`
mới, đều có bước đối chứng riêng trong cùng phiên):

| Loại BC (`loai=`) | Case | Đối chứng cùng phiên | Kết quả gõ thẳng địa chỉ màn báo cáo |
|---|---|---|---|
| `vu-viec-tiep-nhan` | VVDTN_06 | `/doanh-nghiep` vào được | → `/dashboard`, phiên còn sống |
| `vu-viec-dang-ho-tro` | VVDHT_06 | `/vu-viec` vào được | → `/dashboard`, phiên còn sống |
| `vu-viec-hoan-thanh` | VVDHTHT_06 | `/chi-tra` vào được (bảng 14 dòng) | → `/dashboard`, phiên còn sống (kiểm phiên trả 200) |

⇒ Đường chặn nằm ở **cửa vào `/bao-cao`**, không phụ thuộc giá trị `loai=`. B2/B3 vẫn phải tự bấm một lượt
với `loai=` của mình rồi ghi lại (chuẩn cụm A cấm suy từ loại này sang loại khác), nhưng có thể dự liệu
kết quả giống 3 dòng trên.

⇒ Vì màn đã ẩn và địa chỉ bị chặn, **với QTHT không còn tồn tại bước "bấm [Xuất Excel]"** — đúng hệ quả
đã ghi ở [`../chuan/chuan-cum-A-xuat-excel.md`](../chuan/chuan-cum-A-xuat-excel.md) §2.1.

## 4. Việc B2/B3 vẫn phải tự làm

1. **Vế (a) của chính loại báo cáo mình phụ trách** — bắt buộc, không suy từ case khác.
2. **Phép b2 với địa chỉ mang `loai=` của case mình** (vd `loai=vu-viec-theo-thoi-gian`). §3 ở trên mới
   chỉ chứng minh cho `loai=vu-viec-tiep-nhan`; đường chặn nằm ở cửa vào `/bao-cao` nên nhiều khả năng
   giống nhau, **nhưng vẫn phải tự bấm một lượt** rồi ghi lại — chuẩn cụm A cấm suy từ loại này sang loại khác.
3. **Phép b1 thì KHÔNG cần dựng lại** — menu là một quan sát chung cho cả phiên QTHT, §2 ở trên đủ dùng;
   chỉ cần trỏ về file này. Nếu bản dựng đổi giữa chừng (xem `../BAN-DUNG-G1.md`) thì phải đo lại.

## 5. Ghi nhận thêm (KHÔNG kéo verdict 9 phiếu)

Ngoài 2 phép bắt buộc, đã hỏi thêm tầng máy chủ **trong cùng phiên `admin`** — chuẩn cụm A §3.4 xếp việc
này là *ghi nhận thêm*, không phải bước bắt buộc:

| Việc hỏi | Kết quả |
|---|---|
| Xem báo cáo vụ việc đã tiếp nhận | Bị từ chối, mã `ERR-RPT-05`, câu **tiếng Việt** *"Bạn không có quyền xem báo cáo này"* |
| Xuất tệp báo cáo | Bị từ chối, mã **`ERR-RPT-08`**, câu **tiếng Việt** *"Bạn không có quyền thực hiện thao tác này"* |
| Kiểm phiên ngay sau đó | Còn sống |

⇒ Chuỗi tiếng Anh `"Forbidden"` (`ERR-PERM-SYS-00-01`) mà đối tác chụp ở vòng 2 **không còn tái hiện**;
câu từ chối nay đúng cặp mã mà BA chốt cho hai tình huống *xem* và *thao tác*. Điểm này liên quan phiếu
QA `BUG-BCTK-QA01` — **QA tự xử lý phiếu đó**, không kéo verdict 9 dòng cụm A.
