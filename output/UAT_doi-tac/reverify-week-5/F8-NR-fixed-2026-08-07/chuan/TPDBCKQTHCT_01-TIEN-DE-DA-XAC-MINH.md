# `TPDBCKQTHCT_01` — tiền đề ĐÃ XÁC MINH LIVE (điều phối, 07/08/2026 18:2x)

> Phụ lục cho [`TPDBCKQTHCT_01.md`](TPDBCKQTHCT_01.md). **Không sửa chuẩn chấm** — file này chỉ trả lời
> 2 câu hỏi mà §3.1 và §4.3 của chuẩn chấm bỏ ngỏ ("chưa ai đọc được, KHÔNG được đoán").
> Toàn bộ đo bằng `GET` qua API, **không thao tác gì trên giao diện**, không mutate bản ghi nào.

---

## 1. §3.1 câu 1+2 — ĐÃ TRẢ LỜI: cặp tài khoản `_04` HỢP LỆ, không phải fallback

Đăng nhập thật qua `POST /api/v1/auth/login` → `POST /api/v1/auth/verify-otp` (env nội bộ **có** bước mã
xác thực; lấy mã ở MailHog `http://18.143.165.120:8025`), rồi đọc `GET /api/v1/auth/me`:

| Tài khoản | `hoTen` | `capDonVi` | `donViId` |
|---|---|---|---|
| `cbnv_dp_04` | `CB Nghiệp vụ - Địa phương #04` | `DP` | `00000000-0000-4000-8002-000000000006` |
| `cbpd_dp_04` | `CB Phê duyệt - Địa phương #04` | `DP` | `00000000-0000-4000-8002-000000000006` |

✅ **`donViId` TRÙNG NHAU** ⇒ đo được vế `C2` (thông báo tới CB PD **cùng đơn vị**).
✅ Đúng cấp `DP` mà `:712` đòi cho khâu lập báo cáo.
✅ **KHÔNG cần Rule 7**, không lệch prompt — dùng đúng bộ `_04` như prompt chỉ định.

`donViId` này trùng với đơn vị mà chuẩn chấm §3.1 đã tra sẵn cho bộ `_03` = **Sở Tư pháp An Giang**
(`…-8002-…0006`). Vẫn nên đọc tên đơn vị hiển thị trên giao diện sau khi đăng nhập và ghi vào `do/`.

> ⚠️ **Lưu ý khi đăng nhập bằng API:** thân yêu cầu dùng khóa **`username` / `password`**
> (đọc từ `LoginDto` trong `/api/docs-json`), **không phải** `tenDangNhap`/`matKhau`. Giới hạn
> **5 lượt đăng nhập / 60 giây** — sai khóa vài lần là dính `ERR-VAL-SYS-00-01` rồi bị chặn nhịp.

---

## 2. §4.3 dòng 2 — ĐÃ TRẢ LỜI: **KHÔNG phải dựng** trạng thái nộp

`GET /api/v1/dot-bao-caos?limit=20` bằng chính phiên `cbnv_dp_04`. Máy chủ trả **4 đợt**, và trường
**`trangThaiNop` chính là trạng thái nộp của ĐƠN VỊ tài khoản đang đăng nhập** (An Giang):

| `maDot` | `id` | `bieuMauSuDung` | `trangThai` (bản ghi ĐỢT) | **`trangThaiNop`** (An Giang) | Dùng được? |
|---|---|---|---|---|---|
| `DOT-SO_BO_NAM-2026-1` | `e9909d96-1391-463b-8072-b1b56c319f8e` | `MAU_21A` | `TAO_DOT` | **`DANG_LAP`** | ✅ **ưu tiên 1** |
| `DOT-SO_BO_6_THANG-2026-1` | `a61e07f1-e205-4948-ad7d-a3ccac49830a` | `MAU_21A` | `TAO_DOT` | **`DANG_LAP`** | ✅ **ưu tiên 2 — đợt độc lập, đo lượt thứ hai** |
| `DOT-THBC01-UAT` | `d7a62f6e-…` | `MAU_21A` | `DA_TONG_HOP` | `DA_NOP` | ❌ đã tiêu |
| `DOT-TRON_NAM-2026-1` | `a63a3214-…` | `CA_HAI` | `TAO_DOT` | `CHUA_NOP` | ❌ sai biểu mẫu + chưa lập |

**Hệ quả — bớt được một bước mutate:**

- Điều kiện của phiếu (*"Đợt ở trạng thái **Đang lập báo cáo**"*) **đã thỏa sẵn** cho An Giang ở **2 đợt**.
- ⇒ **KHÔNG cần bấm [Lập báo cáo]**, **KHÔNG cần gọi `POST /{id}/start`**. Bảng §4.3 dòng 2 của chuẩn chấm
  xem như đã đạt; phần mutate `CHUA_NOP → DANG_LAP` **không phát sinh**.
- ⇒ Việc dựng còn lại **chỉ là 13 chỉ tiêu số liệu**, và cổng **TĐ-UI §4.4 vẫn nguyên hiệu lực:
  🔴 CHỈ ĐƯỢC ĐIỀN BẰNG GIAO DIỆN.** Cấm `PATCH /dot-bao-caos/{id}/bao-cao`, cấm truyền `soLieuTongHop`.
- Có **2 đợt độc lập** ⇒ thỏa luôn §10 nếu cần lượt đo thứ hai; **chạy `DOT-SO_BO_NAM-2026-1` trước**.

**Xác nhận thêm về §1.2 / vế `C1b`:** bản ghi **ĐỢT** của cả 4 đợt đều còn `trangThai = TAO_DOT`, kể cả
`DOT-SO_BO_NAM-2026-1` — đúng như §4.2 của chuẩn chấm dự đoán, và là bằng chứng trực tiếp cho `C1b`
(không có chức năng hợp lệ nào đổi trường này). **Không được chấm FAIL vì nó đứng ở `TAO_DOT`.**

---

## 3. Vẫn phải tự làm trước khi đo (điều phối KHÔNG làm hộ)

1. **Đọc lại 2 đợt ngay trước khi đo** — môi trường dùng chung, `trangThaiNop` đổi được bất cứ lúc nào.
   Đã có phiên khác chạm `DOT-THBC01-UAT` lúc 07/08 06:30 (`ngayCapNhat`, `version` 1→3).
2. **Đọc bản ghi báo cáo của An Giang trong đợt** để biết 13 chỉ tiêu hiện có giá trị chưa, và ô nào
   **có ô nhập** trên màn — đây là tâm điểm của phiếu (§1.2).
3. **Ghi `version`** trước mỗi bước chuyển trạng thái (`409` là xung đột kỹ thuật, **không phải bug nghiệp vụ**).
4. Ghi tên đơn vị đọc được trên giao diện vào `do/` — file này mới chỉ chứng minh **`donViId` trùng nhau**,
   chưa đọc tên hiển thị.
