# Re-verify vòng 2 — QLDMTCTV_OOS_09 (dòng 335, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`, Cục Bổ trợ tư pháp – Bộ Tư pháp)
**Verdict:** ✅ Pass — **case thuần tĩnh** (đọc chuỗi chữ trên thanh đường dẫn)

---

## Triệu chứng gốc cần kiểm (2 ý — phải hết cả hai)

1. Đường dẫn điều hướng ở chế độ Sửa **không kèm tên tổ chức**.
2. Còn **chèn thêm một cấp "Chi tiết"** không có trong đặc tả.
Chuỗi vòng 1: `Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Chi tiết / Chỉnh sửa`.

## Vì sao case này không phụ thuộc vai trò / trạng thái

Thanh đường dẫn của màn Chỉnh sửa do chính màn đó dựng, chỉ lấy tên tổ chức đang mở; không có nhánh hiển thị theo vai trò hay theo trạng thái hồ sơ trong đặc tả (SCR-IV-NEW-02 dòng 1675 ghi một chuỗi duy nhất cho chế độ sửa). Quyền vào màn Sửa chỉ có Cán bộ Nghiệp vụ cùng đơn vị (dòng 1667) — đúng vai trò đã dùng để đo. Để loại trừ khả năng tên bị gán cứng, đã đo trên **2 hồ sơ khác nhau**.

## Nhật ký đo

### 13:49 — Hồ sơ 1: TC-BTP-TW-0001
Bấm biểu tượng Sửa trên dòng TC-BTP-TW-0001 → `/chuyen-gia-tvv/to-chuc/beb25e6f-…/chinh-sua`.
Đọc nguyên văn thanh đường dẫn (`.ant-breadcrumb`):

> **Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Chỉnh sửa Công ty Luật TNHH Alpha Hà Nội**

- Có tên tổ chức đang sửa ✔
- Không còn cấp "Chi tiết" ✔ (4 cấp, đúng số cấp đặc tả)

Ảnh: `image/QLDMTCTV_09-v2-01-sua-TC-BTP-TW-0001-duong-dan-co-ten-to-chuc-va-du-lieu-dien-san.png` (đã mở đọc — thanh trên cùng ghi đúng chuỗi trên).

### 14:01 — Hồ sơ 2: TC-BTP-TW-0003 (loại trừ tên gán cứng)
Bấm Sửa trên dòng TC-BTP-TW-0003 → đọc lại thanh đường dẫn:

> **Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Chỉnh sửa Trung tâm TVPL Gamma Đà Nẵng**

Tên đổi theo đúng hồ sơ đang mở ⇒ không phải chuỗi gán cứng.
Ảnh: `image/QLDMTCTV_OOS_09-v2-01-duong-dan-Chinh-sua-kem-ten-to-chuc-khong-co-cap-Chi-tiet.png` (đã mở đọc).

### Đối chiếu để chắc không nhầm với màn khác
- Chế độ **Thêm mới**: `Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Thêm mới` — khớp nhánh "Thêm mới" của đặc tả.
- Màn **Chi tiết** (SCR-IV-NEW-03): `Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Công ty Luật TNHH Alpha Hà Nội` — đúng dòng 1715, và cấp "Chi tiết" cũng đã được gỡ ở màn này.

### Đối chiếu đặc tả
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1675:
> "Trang chủ > Mạng lưới Tư vấn viên > Tổ chức tư vấn > Thêm mới" hoặc "... > Chỉnh sửa [Tên TC]"

Chuỗi đo được khớp đúng nhánh "Chỉnh sửa [Tên TC]".

### Kết luận
Cả 2 ý của bug gốc đều hết, xác nhận trên 2 hồ sơ ⇒ **Pass**.
