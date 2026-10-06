# Audit — QLLKHDTBD_02 (row 31) → Reject (không tái hiện)

## Đối tác báo
- Chức năng (sheet ghi nhầm "Tìm kiếm kho tài liệu"): thực chất màn **Kế hoạch đào tạo** (list).
- Bước: Đăng nhập → Đào tạo, tập huấn → Kế hoạch đào tạo.
- Actual: toast đỏ "Lỗi hệ thống, vui lòng thử lại sau." + bảng rỗng.
- Evidence: `partner-evidence/QLLKHDTBD_02.jpg` — env `htpldn-uat.ospgroup.vn/dao-tao/ke-hoach/danh-sach`, role CB_NV_TW, 06/07 16:56.

## 3 dữ kiện neo (full-res)
- (a) URL: `htpldn-uat.ospgroup.vn/dao-tao/ke-hoach/danh-sach` — **env đối tác khác env giao (18.143.165.120)**.
- (b) State: trang list "Tất cả" render tabs+headers, bảng RỖNG + toast "Lỗi hệ thống".
- (c) Tiền đề: role CB_NV_TW, đã login.

## Verify trên env được giao (18.143.165.120)
- Account: `cbnv_tw` (CB_NV_TW) — đúng vai trò bug.
- `GET /api/v1/ke-hoach-dao-taos?page=1&pageSize=20` → **200**, list hiển thị 1 record `KHDT-SEED-0001` "Đã duyệt", "Hiển thị 1-1 / 1 kết quả". KHÔNG toast lỗi.
- Reload x2 → 304 (ổn định). Tab rỗng `?trangThai=NHAP` → **200** (empty state sạch, không lỗi).
- Ảnh: `web-list-load-ok-api-200.png`.

## Bảng đối chiếu điều kiện
| Điều kiện | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB_NV_TW | CB_NV_TW | Không |
| Entity+state | list "Tất cả", rỗng+lỗi | list "Tất cả", 1 record, OK | (khác KQ) |
| Data tiền đề | env ospgroup.vn | env 18.143.165.120, seed | env khác |
| Filter/input | mặc định vừa vào | mặc định + tab NHAP rỗng | Không |

→ GAP duy nhất = **khác env/build**. Đã đóng GAP điều kiện (role/state/empty-data) trên env giao: hệ thống hoạt động đúng, không tái hiện lỗi.

## SRS
- FR-III-14 (UC33) "Lập kế hoạch đào tạo năm" §Processing — Xem danh sách: hiển thị danh sách KE_HOACH_DAO_TAO theo đơn vị, phân trang 20/trang. Web đáp ứng đúng.

## Verdict: Reject + "đối tác kiểm tra lại"
Env được giao load list bình thường (API 200), không có "Lỗi hệ thống", ổn định qua nhiều lần thử + điều kiện rỗng. Lỗi đối tác là env/thời điểm, không tái hiện. Ghi sheet row 31: Reject.
