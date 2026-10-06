# Kiểm kê tiền đề sẵn có — đọc trước khi đo

> Đo ngày **2026-08-07** bằng `GET /api/v1/dot-bao-caos` với tài khoản `cbnv_dp_01`.
> **Đây là KIỂM KÊ (có sẵn dữ liệu gì), KHÔNG phải phép đo hành vi đang tranh chấp.**
> Cố ý **không** đọc nội dung báo cáo (`soLieuTongHop`, danh sách cột) — phần đó thuộc vế đang tranh chấp
> của LBCKQTHCT_03/04/05/06, phải đo sau khi khóa xong chuẩn chấm.

## Cách lấy phiên (đã kiểm chứng chạy được)

Env nội bộ **CÓ bước mã xác thực** (giống env đối tác). Trường đăng nhập là **`username` / `password`**
(KHÔNG phải `tenDangNhap` / `matKhau` — sai tên trường trả 422 `ERR-VAL-SYS-00-01`).

```
POST /api/v1/auth/login      {"username":"<u>","password":"Test@1234"}  -> data.otpToken (hạn 300s)
   lấy mã 6 số ở MailHog:  http://18.143.165.120:8025/api/v2/messages?limit=25
   (hộp thư dạng <username>@htpldn.test, vd cbnv_dp_01@htpldn.test)
POST /api/v1/auth/verify-otp {"otpToken":"…","otpCode":"######"}        -> data.accessToken (Bearer)
```
Script tiện dùng lại: `/tmp/login.sh <username> [password]` → in ra accessToken.
Token: `idleTtl = 1800` (30 phút không thao tác) — 1 phiên chạy trọn 1 lô.

## Danh tính tài khoản đã kiểm

| Tài khoản | hoTen | vaiTro | capDonVi | donViId |
|---|---|---|---|---|
| `cbnv_dp_01` | CB Nghiệp vụ - Địa phương #01 | `CB_NV_DP` | `DP` | `00000000-0000-4000-8002-000000000006` |

## 3 đợt báo cáo hiện có (toàn bộ, không có đợt nào khác)

| # | maDot | tenDot | kyBaoCao | `trangThai` (cấp ĐỢT) | `trangThaiNop` (cấp ĐƠN VỊ của `cbnv_dp_01`) | version | bieuMauSuDung | hanNop | phạm vi |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `DOT-THBC01-UAT` | THBCTHCT_01 - Đợt báo cáo sơ bộ 6 tháng 2026 (seed UAT) | `SO_BO_6_THANG` | `TAO_DOT` | **`DA_NOP`** | 2 | `MAU_21A` | 2026-07-31 | 2 đơn vị |
| 2 | `DOT-SO_BO_NAM-2026-1` | QA Reverify CTBC 715 v2 fresh | `SO_BO_NAM` | `TAO_DOT` | **`DANG_LAP`** | 1 | `MAU_21A` | 2026-12-31 | 83 đơn vị (20× `8001-*` + 63× `8002-*`) |
| 3 | `DOT-SO_BO_6_THANG-2026-1` | QA Reverify CTBC 715 BN | `SO_BO_6_THANG` | `TAO_DOT` | **`DANG_LAP`** | 1 | `MAU_21A` | 2026-12-31 | 83 đơn vị |

ID đầy đủ: `d7a62f6e-a119-4582-8b08-f935d25c534b` · `e9909d96-1391-463b-8072-b1b56c319f8e` · `a61e07f1-e205-4948-ad7d-a3ccac49830a`

- Đơn vị của `cbnv_dp_01` **nằm trong phạm vi** đợt #2 và #3 (đã kiểm: `True`).
- Đợt #2 có `baoCaoId = c1b1045d-007c-4104-a169-e267010557a0` (đã có bản ghi báo cáo) và `_links` cho phép `submit-bc`.
- Cả 3 đợt đều `bieuMauSuDung = MAU_21A`.

## 5 hệ quả cho việc lập kế hoạch đo

1. 🔴 **Không có đợt nào ở `trangThaiNop = CHUA_NOP`** cho đơn vị này.
   ⇒ **LBCKQTHCT_01** (vế "Chưa nộp → Đang lập") **không có tiền đề sẵn**. Phải hoặc dùng đơn vị khác
   trong phạm vi 83 đơn vị (đăng nhập tài khoản của đơn vị đó), hoặc tạo đợt mới bằng CB NV cấp TW
   (`POST /api/v1/dot-bao-caos`). **Khai rõ đã dựng gì, trên đợt nào** (seed = làm thay đổi môi trường chung).

2. 🔴 **Không có đợt nào ở `trangThai = DANG_LAP_BC` / `CHO_DUYET_KQ` / `DA_DUYET_KQ`** — cả 3 đều `TAO_DOT`.
   ⇒ **TPDBCKQTHCT_01** (cần "Đang lập báo cáo") và **GKQTHCTHTPL_01** (cần "Đã duyệt kết quả")
   đều **phải tự dựng chuỗi tiền đề**, không dùng lại được.

3. 🟡 **Hai bậc trạng thái khác nhau — đây là chỗ dễ chấm oan nhất của lô này:**
   - `trangThai` = trạng thái của **ĐỢT** (đang là `TAO_DOT` ở cả 3).
   - `trangThaiNop` = trạng thái nộp của **ĐƠN VỊ** trong đợt (đang là `DANG_LAP` ở 2 đợt).

   Phiếu **LBCKQTHCT_01** viết *"Cập nhật **trạng thái nộp của đơn vị** thành «Đang lập»"* → nhắm `trangThaiNop`.
   Phiếu **TPDBCKQTHCT_01** viết *"Chuyển trạng thái **đợt báo cáo**: Đang lập báo cáo → Chờ duyệt kết quả"* → nhắm `trangThai`.
   ⚠️ Đối tác báo *"Hệ thống không chuyển trạng thái thành Đang lập"* — **phải xác định họ nhìn ô nào trên màn**.
   Nếu màn hiển thị `trangThai` của đợt (vẫn `TAO_DOT`) trong khi hệ thống cập nhật `trangThaiNop`, thì đây là
   vấn đề **hiển thị đúng bậc trạng thái**, không phải "không lưu". **CẤM kết luận trước khi đo trên giao diện thật**
   và trước khi khóa xem SRS quy định màn phải hiện bậc nào.

4. 🟢 **`soLieuKyTruoc` TỒN TẠI như một trường cấp cao nhất** trong phản hồi chi tiết đợt (hiện đang `null` ở đợt #2).
   Liên quan thẳng **LBCKQTHCT_03/04** ("thiếu cột *Số liệu kỳ trước*"). ⇒ Tầng dữ liệu **có** chỗ chứa.
   ⚠️ **Nhưng "có trường" ≠ "đặc tả buộc hiện cột đó trên màn"**, và cũng ≠ "màn đang hiện".
   Quan hệ MATCH/DIFF/GAP vẫn phải khóa bằng **dòng SRS**. Đây chỉ là manh mối chỉ chỗ cần đọc.
   ⚠️ Trường đang `null` ⇒ nếu màn ẩn cột khi không có dữ liệu thì phải seed số liệu kỳ trước mới kết luận được
   — **"cột không hiện vì rỗng" khác hẳn "cột không tồn tại"**.

5. 🟡 `tienDo` (bảng tiến độ nộp theo đơn vị ở chi tiết đợt) đang trả **mảng rỗng `[]`** ở đợt #2,
   dù phạm vi có 83 đơn vị. Ghi nhận làm **candidate**, KHÔNG điều tra trong lô này (không thuộc vế nào
   của 7 phiếu). Nếu nó chặn phép đo của một vế thì mới xử lý.

## Ràng buộc kỹ thuật khi dựng tiền đề

- Mọi hành động chuyển trạng thái đòi **`version`** hiện tại ⇒ `GET` trước mỗi bước.
  Sai `version` → lỗi xung đột, **không phải bug nghiệp vụ**, đừng log nhầm.
- Tạo đợt là quyền **CB NV cấp TW** (`ERR-XI-05a-00`) ⇒ cần `cbnv_tw` / `cbnv_tw_01`.
- Duyệt BC nội bộ (`approve-bc`) cần vai trò **CB Phê duyệt cùng đơn vị**.
- Hành động đang tranh chấp **phải bấm bằng giao diện thật**; API chỉ dùng để **dựng tiền đề** và **đối chứng**.
