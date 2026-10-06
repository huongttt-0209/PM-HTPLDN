# Bảng đối chiếu điều kiện — VVTTG_03 (row 215) — RE-VERIFY sau dev fix

**Case:** BC Vụ việc theo thời gian (FR-IX-05 / UC128) — trend chỉ 1 chuỗi + không có bảng theo đơn vị.
**Bug gốc:** biểu đồ trend chỉ vẽ `soVuViec` (1 chuỗi), thiếu tiếp nhận/hoàn thành; không có bảng chi tiết/theo đơn vị nào dưới biểu đồ (BE không trả `theoDonVi`).
**Verdict re-verify:** Pass — trend nay 2 chuỗi (Tiếp nhận + Hoàn thành); nay có bảng "Kỳ/Tiếp nhận/Hoàn thành" + bảng "Đơn vị/Số lượng".

| Điều kiện có thể đổi kết quả | Bug gốc (bước tái hiện) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` (CB Nghiệp vụ TW) — Toàn quốc | `cbnv_tw_05` (CB Nghiệp vụ TW #05) — Toàn quốc. Cùng vai trò + scope | Không |
| Loại báo cáo | BC Vụ việc theo thời gian (UC128) | BC Vụ việc theo thời gian (UC128) | Không |
| Kỳ + thời gian | Kỳ Năm 2026 (01/01 → 31/12) | Kỳ Năm, 01/01/2026 → 31/12/2026 | Không |
| Đơn vị | Toàn quốc | Toàn quốc | Không |
| Data / state | BE trả `data[].soVuViec` (1 chuỗi), không `theoDonVi`; UI không có bảng nào | BE trả trend 2 chuỗi (tiếp nhận 6 / hoàn thành 5) + `theoDonVi`; UI vẽ biểu đồ 2 chuỗi + 2 bảng | Không |

**Kết quả đóng GAP:** 0 GAP. Chạy đủ luồng (chọn loại BC → Kỳ Năm → Đơn vị Toàn quốc → Xem báo cáo). Biểu đồ trend nay có 2 chuỗi "Tiếp nhận" + "Hoàn thành"; dưới biểu đồ có bảng "Kỳ / Tiếp nhận / Hoàn thành" (2026: 6/5) + bảng "Đơn vị / Số lượng" (Cục Bổ trợ 3, Bộ KH&ĐT 2, STP Hà Nội 1). Cả 2 defect gốc (trend 1 chuỗi + không có bảng) đã hết — đúng KQ mong đợi §Output 337/338 + AC 342.
