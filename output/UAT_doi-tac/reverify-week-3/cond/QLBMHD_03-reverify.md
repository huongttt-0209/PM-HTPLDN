# Bảng đối chiếu điều kiện — QLBMHD_03 (row 98) · RE-VERIFY sau dev fix

Re-test đúng vai trò/đơn vị/màn/state như **bug gốc** (Pass-bug-report-bieu-mau-batch4.md) mô tả.

| Điều kiện | Bug gốc (batch4) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ - Trung ương (cbnv_tw, CB_NV_TW) | cbnv_tw_03 — CB Nghiệp vụ - Trung ương (CB_NV_TW) | Không |
| Đơn vị | BTP·TW (Cục Bổ trợ tư pháp) | BTP·TW (donViId 00000000-0000-4000-8000-000000000001) | Không |
| Màn hình | Form Thêm biểu mẫu (/bieu-mau/them-moi) | Form Thêm biểu mẫu (/bieu-mau/them-moi) | Không |
| State switch Công khai | Kiểm cả OFF và ON (bug báo thiếu ở cả 2) | Đã kiểm OFF (mặc định) + bật ON (aria-checked=true) | Không |
| Trường đang xét | Trường "Cơ quan ban hành" read-only auto = đơn vị | Đọc label + input.disabled + input.value của form-item | Không |

**Kết luận GAP:** 0 GAP — re-test đúng vai trò + đơn vị + màn + đủ 2 state switch như bug gốc.

**Quan sát re-test (22/07/2026):** Form CÓ trường "Cơ quan ban hành", input `disabled=true` (read-only), value auto = "Cục Bổ trợ tư pháp - Bộ Tư pháp" (đúng đơn vị account). Hiển thị ở cả switch OFF lẫn ON. Giá trị persist xác nhận qua cột danh sách (QLBMHD_02: các record BM-20260720-* của đơn vị này hiển thị "Cục Bổ trợ tư pháp - Bộ Tư pháp") → khớp KQ mong đợi → PASS.
