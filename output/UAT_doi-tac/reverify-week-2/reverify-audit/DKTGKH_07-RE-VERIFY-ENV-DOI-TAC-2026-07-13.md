# DKTGKH_07 — Re-verify TRÊN ENV ĐỐI TÁC (2026-07-13)

**Lý do chạy:** verdict cũ `Reject` dựa trên env được giao (`18.143.165.120`) — không tái hiện. Nghi vấn: khác môi trường.

**Kết luận: BUG THẬT trên env đối tác. Verdict `Reject` cũ SAI về lý do, và ghi chú audit cũ ("bác claim mọi cột = -") là SAI — đối tác đúng.**

---

## 1. Tái hiện trên chính env đối tác

- Đăng nhập `htpldn-uat.ospgroup.vn` bằng `cbnv_tw / Test@1234` (tài khoản dùng chung 2 env) → vào được.
- Mở **đúng khóa học trong video đối tác**: `/dao-tao/khoa-hoc/dd1adee1-715e-47f9-986d-52f9dcc60373?tab=hoc-vien` (khóa "Đang diễn ra").
- Tab Học viên: **7 bản ghi, tất cả nguồn "Nhập tay", tất cả 4 cột Họ tên / Email / SĐT / Đơn vị đều hiển thị "-"** — khớp 100% frame 00:28 của đối tác (các bản ghi tạo 06/07/2026, vẫn còn nguyên).
- Ảnh: `DKTGKH_07-envdoitac-taihien-cot-trong.png`

## 1b. Tạo DỮ LIỆU MỚI ngay hôm nay trên env đối tác (phép thử quyết định)

Dữ liệu ở mục 1 tạo ngày 06/07 → có thể do build cũ sinh ra. Nên tạo **bản ghi mới ngay bây giờ** để loại trừ khả năng "chỉ dữ liệu cũ mới sai".

- Khóa `dd1adee1…` (trong video) nay đã sang **"Đang diễn ra"** → thêm học viên bị chặn: *"ERR-BIZ-III-04-01: Chỉ có thể đăng ký khóa học đã duyệt"* (lúc đối tác quay, khóa còn ở "Đã duyệt"). **Ghi nhận thêm: thông báo lỗi này hiện LẶP 2 LẦN** — cùng pattern `BUG-KTHSYCHTPL_15`.
- Chuyển sang khóa đang ở **"Đã duyệt"**: `KH-20260509-003` (`707eaa5e-c72c-4c49-87bc-2e37ad024100`).
- Thêm học viên thủ công, nhập **đủ 4 trường**: `QA VERIFY 13-07 Nguyen Van Moi` / `qa.verify.1307@test.htpldn.vn` / `0912345678` / `Don vi QA 1307`.

**Kết quả — bản ghi tạo lúc `2026-07-13 11:20:04`:**

| | |
|---|---|
| Thông báo | "Đã thêm học viên" (**hiện 2 lần** — lại lặp) |
| Dòng trên màn hình | Nguồn "Nhập tay" · Trạng thái "Chờ duyệt" · **Họ tên / Email / SĐT / Đơn vị = "-"** |
| Dữ liệu máy chủ trả về | `hoTen/email/soDienThoai/donVi` (cùng cấp) = **null**<br>`hocVien.hoTen` = "QA VERIFY 13-07 Nguyen Van Moi" · `hocVien.email` · `hocVien.soDienThoai` · `hocVien.donVi` = **đủ cả 4** |

⇒ **Lỗi tái hiện với dữ liệu MỚI TINH, không phải hiện tượng của dữ liệu cũ.** Ảnh: `DKTGKH_07-envdoitac-DATA-MOI-13-07-cot-van-trong.png`

## 2. Nguyên nhân gốc — dữ liệu CÓ, màn hình đọc sai chỗ

Đọc API `GET /api/v1/khoa-hocs/{id}/dang-ky-dao-taos` trên **env đối tác**:

```json
{ "hoTen": null, "email": null, "soDienThoai": null, "donVi": null,
  "nguonDangKy": "NHAP_TAY",
  "hocVien": { "hoTen": "Nguyễn Văn A",
               "email": "nguyenvana@gmail.com",
               "soDienThoai": "0105545483",
               "donVi": "TKM" } }
```

⇒ Dữ liệu học viên **vẫn lưu đầy đủ**, nhưng nằm **lồng trong object `hocVien`**; các trường cùng cấp thì `null`. Màn hình đọc trường cùng cấp → in "-".

Cùng endpoint trên **env được giao** (`18.143.165.120`):

```json
{ "hoTen": "QA Verify DKTGKH07 R2 Now",
  "email": "qa.verify.dktgkh07r2@test.htpldn.vn",
  "nguonDangKy": "NHAP_TAY" }          // KHÔNG có object "hocVien"
```

⇒ **Hai môi trường đang chạy 2 bản backend khác nhau, trả về 2 cấu trúc dữ liệu khác nhau.** Backend env được giao trả trường phẳng (cùng cấp) — trùng chỗ màn hình đọc → hiển thị đúng. Backend env đối tác trả trường lồng — lệch chỗ màn hình đọc → hiển thị "-".

## 3. Đính chính ghi chú audit cũ

Ghi chú `EVIDENCE-AUDIT-2026-07-12.md` dòng 26 viết: *"bác claim 'mọi cột kể cả Họ tên = -'"* — dựa trên quan sát khóa `AAA-KH-TW` **của env được giao** (nơi Họ tên + Email vẫn render). **Suy luận này sai**: trên chính env đối tác, Họ tên cũng "-" đúng như họ quay. Không được dùng quan sát ở env này để bác một claim quay ở env kia.

## 4. Đề xuất xử lý

- Lỗi **có thật** trên bản build đối tác đang test, và **không còn** trên bản build của env được giao.
- Không nên giữ nguyên verdict `Reject` với lý do "không tái hiện" — vì đối tác mở lại env của họ vẫn thấy y nguyên.
- Hành động đúng: **đồng bộ build cho env đối tác** rồi đề nghị đối tác kiểm tra lại. Dev cần xác nhận bản fix (màn hình đọc đúng `hocVien.*`, hoặc backend trả trường phẳng) đã nằm trong bản sẽ phát hành.

## 5. Rủi ro lan rộng — CẦN RÀ LẠI

12 case đang để `Reject` trên Sheet đều dựa trên lập luận "không tái hiện trên env được giao". Nếu 2 env chạy 2 build khác nhau thì **mọi Reject kiểu này đều có nguy cơ false negative giống DKTGKH_07** → nên re-verify lại các Reject trực tiếp trên env đối tác.
