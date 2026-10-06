# Bảng đối chiếu điều kiện — QLBMHD_02 (row 97) · RE-VERIFY sau dev fix

Re-test đúng vai trò/đơn vị/màn như **bug gốc** (Pass-bug-report-bieu-mau-batch4.md) mô tả.

| Điều kiện | Bug gốc (batch4) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ - Trung ương (cbnv_tw, CB_NV_TW) | cbnv_tw_03 — CB Nghiệp vụ - Trung ương (CB_NV_TW) | Không |
| Đơn vị | BTP·TW (Cục Bổ trợ tư pháp) | BTP·TW (donViId 00000000-0000-4000-8000-000000000001) | Không |
| Màn hình | Danh sách biểu mẫu (/bieu-mau/danh-sach) | Danh sách biểu mẫu (/bieu-mau/danh-sach) | Không |
| Thao tác | Mở danh sách, đọc header cột và giá trị từng dòng | Y hệt — đọc `thead th` + cột từng dòng | Không |
| Data | Danh sách biểu mẫu hiện có | Danh sách biểu mẫu hiện có (8 record) | Không |

**Kết luận GAP:** 0 GAP — re-test đúng vai trò + đơn vị + màn như bug gốc.

**Quan sát re-test (22/07/2026):** Header nay 12 cột (trước 11), có "Cơ quan ban hành" ở index 4, hiển thị tên đơn vị ban hành thực cho 8/8 dòng ("Cục Bổ trợ tư pháp - Bộ Tư pháp", "Bộ Kế hoạch và Đầu tư") → khớp KQ mong đợi bug gốc → PASS.
