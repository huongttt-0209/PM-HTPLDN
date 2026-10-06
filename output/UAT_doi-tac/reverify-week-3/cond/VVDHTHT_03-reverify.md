# Bảng đối chiếu điều kiện — VVDHTHT_03 (row 207) — RE-VERIFY sau dev fix

**Case:** BC Vụ việc đã hoàn thành (FR-IX-04 / UC127) — thiếu chỉ số Thành công / Không thành công / Tỷ lệ thành công.
**Bug gốc:** FE bỏ render các chỉ số kết quả dù BE trả `theoKetQua`.
**Verdict re-verify:** Pass — nay có 3 thẻ KPI (Thành công 1 · Không thành công 0 · Tỷ lệ thành công 20.0%) + bảng "Thống kê theo kết quả".

| Điều kiện có thể đổi kết quả | Bug gốc (bước tái hiện) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` (CB Nghiệp vụ TW) — Toàn quốc | `cbnv_tw_05` (CB Nghiệp vụ TW #05) — Toàn quốc. Cùng vai trò + scope | Không |
| Loại báo cáo | BC Vụ việc đã hoàn thành (UC127) | BC Vụ việc đã hoàn thành (UC127) | Không |
| Kỳ + thời gian | Kỳ Năm, 01/01/2026 → 31/12/2026 | Kỳ Năm, 01/01/2026 → 31/12/2026 | Không |
| Đơn vị | Toàn quốc | Toàn quốc | Không |
| Data / state | BE trả `theoKetQua` (THANH_CONG 1, CHUA_XAC_DINH 4), Tổng 5 | BE trả data, Tổng 5; UI vẽ 3 KPI kết quả + bảng "Thống kê theo kết quả" (Chưa xác định 4/80%, Thành công 1/20%) | Không |

**Kết quả đóng GAP:** 0 GAP. Chạy đủ luồng (chọn loại BC → Kỳ Năm → Đơn vị Toàn quốc → Xem báo cáo). Khu vực kết quả nay có 3 thẻ chỉ số Thành công (1) / Không thành công (0) / Tỷ lệ thành công (20.0%) + bảng "Thống kê theo kết quả". Đúng KQ mong đợi bug gốc — FE đã render `theoKetQua`.
