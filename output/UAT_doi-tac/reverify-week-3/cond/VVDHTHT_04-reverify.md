# Bảng đối chiếu điều kiện — VVDHTHT_04 (row 208) — RE-VERIFY sau dev fix

**Case:** BC Vụ việc đã hoàn thành (FR-IX-04 / UC127) — Bar + Donut đều theo lĩnh vực, thiếu biểu đồ chiều kết quả.
**Bug gốc:** cả 2 biểu đồ cùng chiều "lĩnh vực"; không biểu đồ nào theo chiều "kết quả" dù BE trả `theoKetQua`.
**Verdict re-verify:** Pass — Donut nay theo chiều KẾT QUẢ (Chưa xác định 80.0% / Thành công 20.0%); Bar giữ chiều lĩnh vực → 2 chart 2 chiều khác nhau.

| Điều kiện có thể đổi kết quả | Bug gốc (bước tái hiện) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` (CB Nghiệp vụ TW) — Toàn quốc | `cbnv_tw_05` (CB Nghiệp vụ TW #05) — Toàn quốc. Cùng vai trò + scope | Không |
| Loại báo cáo | BC Vụ việc đã hoàn thành (UC127) | BC Vụ việc đã hoàn thành (UC127) | Không |
| Kỳ + thời gian | Kỳ Năm 2026 | Kỳ Năm, 01/01/2026 → 31/12/2026 | Không |
| Đơn vị | Toàn quốc | Toàn quốc | Không |
| Data / state | BE trả `theoKetQua` (THANH_CONG 1, CHUA_XAC_DINH 4) nhưng chỉ vẽ theo lĩnh vực | BE trả data; Bar = lĩnh vực (Thương mại 5), Donut = kết quả (Chưa xác định 80% / Thành công 20%) | Không |

**Kết quả đóng GAP:** 0 GAP. Chạy đủ luồng (chọn loại BC → Kỳ Năm → Đơn vị Toàn quốc → Xem báo cáo). Biểu đồ cột giữ chiều lĩnh vực (Thương mại), biểu đồ tròn nay thể hiện chiều KẾT QUẢ (Chưa xác định 80.0% / Thành công 20.0%) kèm bảng "Thống kê theo kết quả". Đúng KQ mong đợi bug gốc — chiều kết quả đã được trực quan hóa.
