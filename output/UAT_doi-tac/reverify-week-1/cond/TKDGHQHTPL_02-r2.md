# Bảng đối chiếu điều kiện — TKDGHQHTPL_02 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** Điểm đánh giá hiệu quả hỗ trợ pháp lý trung bình thang 0–100 nhưng số liệu trên màn hình hiển thị vượt quá 100.

**Evidence:** `TKDGHQHTPL_02_v2.png` — thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" hiện **164.0/100** (khoanh đỏ), trục Y chạy tới **172**, 2 cột 05/2026 và 07/2026. Thanh địa chỉ `htpldn-uat.ospgroup.vn/dashboard?donViCap=TW&donViId=00000000-0000-4000-8000-000000000001`, header **Cán bộ NV Trung ương · CB_NV_TW · BTP·TW**, đồng hồ máy 21/07/2026 15:32.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ NV Trung ương (`CB_NV_TW`), đơn vị BTP · TW — đọc ở header ảnh | `cbnv_tw` / CB_NV_TW, đơn vị BTP · TW (Cục Bổ trợ tư pháp) — đúng vai trò, đúng đơn vị | Không |
| Môi trường | `htpldn-uat.ospgroup.vn` (thanh địa chỉ, chụp 21/07/2026 15:32) | Đúng `htpldn-uat.ospgroup.vn` — đăng nhập trực tiếp env đối tác ngày 27/07/2026 14:10 | Không |
| Màn hình + thẻ | Màn "Tổng quan hệ thống", thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" | Đúng màn đó, đúng thẻ đó | Không |
| Bộ lọc | `donViCap=TW` + `donViId=00000000-0000-4000-8000-000000000001` (đọc từ URL trong ảnh) | Chọn Cấp đơn vị "Trung ương" + Đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp" → URL thành `?donViId=00000000-0000-4000-8000-000000000001` | Không |
| Tập dữ liệu nền (chứng minh cùng data) | Thẻ kế bên "Tỷ lệ tuân thủ thời hạn xử lý" = **17.4%**; Thời gian xử lý TB 0,3 ngày; 9 người CG/TVV | Thẻ kế bên "Tỷ lệ tuân thủ thời hạn xử lý" = **17.4%** — trùng khít, xác nhận cùng tập dữ liệu chưa bị đụng vào | Không |

**Kết luận:** 0 GAP — tái hiện trên **chính môi trường đối tác**, đúng vai trò, đúng màn, đúng bộ lọc, cùng tập dữ liệu.

Phép đo đầy đủ (thang điểm BE, xếp loại theo %, đối chiếu SRS): xem [`../reverify-audit/TKDGHQHTPL_02/audit.md`](../reverify-audit/TKDGHQHTPL_02/audit.md).
