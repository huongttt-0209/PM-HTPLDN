# Bảng đối chiếu điều kiện — VVDTN_04 (row 195) — RE-VERIFY sau dev fix

**Case:** BC Vụ việc đã tiếp nhận (FR-IX-02 / UC125) — thiếu mục thống kê "theo lĩnh vực".
**Bug gốc:** FE bỏ render mục "theo lĩnh vực pháp luật" dù BE trả `theoLinhVuc`.
**Verdict re-verify:** Pass — mục "Thống kê theo lĩnh vực pháp luật" nay ĐÃ hiển thị (bảng Lĩnh vực PL / Số lượng / Tỷ lệ: Thương mại 14 · 100%).

| Điều kiện có thể đổi kết quả | Bug gốc (bước tái hiện) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` (CB Nghiệp vụ TW) — phạm vi Toàn quốc | `cbnv_tw_05` (CB Nghiệp vụ TW #05) — phạm vi Toàn quốc. Cùng vai trò + scope; báo cáo là chức năng dùng chung | Không |
| Loại báo cáo | BC Vụ việc đã tiếp nhận (UC125) | BC Vụ việc đã tiếp nhận (UC125) | Không |
| Kỳ + thời gian | Kỳ Năm, 01/01/2026 → 31/12/2026 | Kỳ Năm, 01/01/2026 → 31/12/2026 | Không |
| Đơn vị | Toàn quốc | Toàn quốc | Không |
| Data / state | BE trả `theoLinhVuc: [{Thương mại, 14}]`, Tổng vụ việc 14 | `GET /bao-cao/vu-viec-tiep-nhan` trả 200, Tổng vụ việc 14; UI vẽ bảng lĩnh vực Thương mại 14 (100%) | Không |

**Kết quả đóng GAP:** 0 GAP. Chạy đủ luồng (chọn loại BC → Kỳ Năm → Đơn vị Toàn quốc → Xem báo cáo). Khu vực kết quả nay có heading "Thống kê theo lĩnh vực pháp luật" + bảng Lĩnh vực PL/Số lượng/Tỷ lệ (Thương mại 14 · 100%) đúng KQ mong đợi bug gốc. Endpoint `vu-viec-tiep-nhan` trả 200, giá trị lĩnh vực khớp UI.
