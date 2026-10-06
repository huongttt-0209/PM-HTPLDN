# Bảng đối chiếu điều kiện — TBKQTNHS_01

Loại bug: **Không có nút "Gửi thông báo kết quả" (kết quả tiếp nhận/kiểm tra hồ sơ) cho DN.** Việc nút có hiển thị hay không phụ thuộc role (CB NV) + state (hồ sơ đã qua bước kiểm tra) → điền bảng, xác nhận app test đúng điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác (từ cột Điều kiện/Bước + video) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **Cán bộ nghiệp vụ** (TW/BN/ĐP) | `cbnv_tw` — CB_NV_TW (Cán bộ Nghiệp vụ - Trung ương), đơn vị BTP·TW | Không |
| Trạng thái hồ sơ | **Hồ sơ vụ việc đã qua bước kiểm tra** | Kiểm ở **DANG_KIEM_TRA** (đang/kết luận kiểm tra) + **HOAN_THANH** (đã qua kiểm tra) — 2 mốc bao trọn "đã qua kiểm tra" | Không |
| Thao tác đối chiếu | Mở chi tiết vụ việc → tìm nút **"Gửi thông báo kết quả"** | Mở chi tiết → quét toàn bộ nút (thanh hành động + accordion) + tìm nguyên văn "Gửi thông báo kết quả" trong toàn trang | Không |
| Hiện tượng cần quan sát | Màn hình **không hiển thị/cung cấp** chức năng gửi thông báo kết quả | Không có nút "Gửi thông báo kết quả" ở cả 2 trạng thái (`hasPartnerLabel=false`); thanh hành động chỉ có [Phân công]/[Kiểm tra lại] (ở kiểm tra) hoặc không có nút (ở hoàn thành) | Không |

**Kết luận: 0 GAP về role/state/data.** Đã test đúng vai trò (CB NV) + đúng điều kiện "hồ sơ đã qua bước kiểm tra". Kết quả:

- **Xác nhận đúng hiện tượng đối tác:** KHÔNG có nút "Gửi thông báo kết quả" ở bất kỳ trạng thái nào sau kiểm tra (quét full-page + thanh hành động 2 trạng thái).
- **Nhưng đây là điểm MÂU THUẪN trong chính đặc tả** — không kết luận Đạt/Không đạt được:
  - `srs-fr-05-vu-viec.md:905` §Màn hình: FR-V.I-12 là **"Auto action — Thông báo KQ"** (hành động tự động).
  - `srs-fr-05-vu-viec.md:1758` (SCR-V.I-03, quy tắc màn hình): "Thông báo kết quả = **auto trigger khi chuyển trạng thái**. Gửi tự động qua Cổng PLQG + in-app" → **không có nút bấm tay**.
  - Ngược lại `srs-fr-05-vu-viec.md:947` (AC): "**When** nhấn **'Gửi Thông báo'**" → hàm ý **có nút bấm tay**.
  - → App (không có nút) khớp với quy tắc màn hình `:1758` (auto) nhưng trái AC `:947` (nút tay). Đối tác kỳ vọng nút tay theo AC `:947`. → **BA confirm** (đặc tả tự mâu thuẫn, không tự quyết đúng/sai).

Chi tiết: xem [`../reverify-audit/TBKQTNHS_01/audit.md`](../reverify-audit/TBKQTNHS_01/audit.md).
