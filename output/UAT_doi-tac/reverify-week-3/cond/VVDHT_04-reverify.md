# Bảng đối chiếu điều kiện — VVDHT_04 (row 202) — RE-VERIFY sau dev fix

**Case:** BC Vụ việc đang hỗ trợ (FR-IX-03 / UC126) — thiếu bảng/biểu đồ "theo người hỗ trợ" + bảng Đơn vị thiếu cột "Số quá hạn".
**Bug gốc:** FE bỏ render mục "theo người hỗ trợ" dù BE trả `theoNht`; bảng Đơn vị chỉ có cột Số lượng.
**Verdict re-verify:** Pass — nay có heading "Thống kê theo người hỗ trợ" + bảng (Người hỗ trợ/Số lượng/Số quá hạn/Tỷ lệ); bảng Đơn vị đã có thêm cột "Số quá hạn".

| Điều kiện có thể đổi kết quả | Bug gốc (bước tái hiện) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` (CB Nghiệp vụ TW) — Toàn quốc | `cbnv_tw_05` (CB Nghiệp vụ TW #05) — Toàn quốc. Cùng vai trò + scope | Không |
| Loại báo cáo | BC Vụ việc đang hỗ trợ (UC126) | BC Vụ việc đang hỗ trợ (UC126) | Không |
| Kỳ + thời gian | Kỳ Năm 2026 | Kỳ Năm, 01/01/2026 → 31/12/2026 | Không |
| Đơn vị | Toàn quốc | Toàn quốc | Không |
| Data / state | BE trả `theoNht` (1 NHT), Tổng vụ việc 7 | BE trả data, Tổng vụ việc 6 (data biến động theo thời gian, không đổi bản chất render); UI vẽ bảng NHT (QA TVV Seed28 2/0/100%) + bảng Đơn vị có cột Số quá hạn | Không |

**Kết quả đóng GAP:** 0 GAP. Chạy đủ luồng (chọn loại BC → Kỳ Năm → Đơn vị Toàn quốc → Xem báo cáo). Khu vực kết quả nay có: (1) heading "Thống kê theo người hỗ trợ" + bảng 4 cột Người hỗ trợ/Số lượng/Số quá hạn/Tỷ lệ; (2) bảng "Đơn vị" đã bổ sung cột "Số quá hạn". Đúng KQ mong đợi bug gốc — FE đã render `theoNht` + cột số quá hạn.
