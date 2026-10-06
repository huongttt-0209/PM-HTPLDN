# Bảng đối chiếu điều kiện — CNKQHT_06

Loại bug: **Cập nhật kết quả hỗ trợ khi bản ghi đã bị người khác sửa → hệ thống lặng lẽ ghi đè, KHÔNG hiện thông báo xung đột (optimistic lock).** Kết quả phụ thuộc role (người được phân công / CB NV cùng đơn vị) + state (vụ việc Đang xử lý, có bản ghi kết quả) + có thao tác cập nhật thứ 2 dựa trên bản cũ → điền bảng, xác nhận đã test đúng điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác (từ cột Điều kiện/Bước + video) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **Cán bộ Nghiệp vụ / người được phân công** cập nhật kết quả hỗ trợ | Cập nhật lần 1–2 bằng `qa_tvvseed28` (TVV·CG — người **được phân công** xử lý VV); cập nhật lần 3 bằng `cbnv_tw` (CB_NV_TW cùng đơn vị BTP·TW) → đúng nhóm vai trò được phép cập nhật kết quả | Không |
| Trạng thái vụ việc | Vụ việc **Đang xử lý**, đã có bản ghi kết quả (đủ điều kiện cập nhật) | VV-BTP-TW-20260712-005 seed lên **DANG_XU_LY** (kiểm tra hồ sơ → phân công → chấp nhận), có bản ghi kết quả `id c557f69b` | Không |
| Bản ghi bị người khác sửa (tình huống xung đột) | Bản ghi kết quả **đã bị chỉnh** sau khi người dùng tải màn → thao tác cập nhật dựa trên bản cũ | **Tái hiện thật, 2 tầng:** (a) 2 lần cập nhật tuần tự cùng người → version bản ghi 1→2; (b) người **thứ 2 khác** (`cbnv_tw`) cập nhật đè lên nội dung do `qa_tvvseed28` vừa ghi → version 2→3, người cập nhật đổi sang cbnv_tw | Không |
| Hiện tượng cần quan sát | Hệ thống **không hiện thông báo** xung đột mà cập nhật **thành công** (ghi đè âm thầm) | Cả 3 lần cập nhật (kể cả người thứ 2 ghi đè) đều **HTTP 201**, **không có mã 409**, không hiện modal "Vụ việc đã được … cập nhật … vui lòng tải lại"; bản ghi bị ghi đè sang nội dung mới nhất | Không |

**Kết luận: 0 GAP về role/state/data.** Đã test đúng vai trò (người được phân công + CB NV cùng đơn vị) + đúng điều kiện (vụ việc đang xử lý, bản ghi kết quả bị người khác sửa) + tái hiện thao tác cập nhật thứ 2 dựa trên bản cũ (kể cả bằng người dùng **khác**).

**Bằng chứng cơ chế (không phải suy luận — số liệu thực từ phản hồi máy chủ):**
- Bản ghi kết quả **có sẵn trường `version`** (máy chủ tự tăng: lần 1 → `version 1`, lần 2 → `version 2`, người thứ 2 ghi đè → `version 3`) → mô hình dữ liệu **có hỗ trợ optimistic lock**.
- Nhưng **thân request cập nhật chỉ gồm `{noiDungKetQua}`, KHÔNG kèm version/updated_at kỳ vọng** → máy chủ không có căn cứ để phát hiện bản ghi đã bị sửa → lần cập nhật sau **luôn ghi đè** lần trước, trả 201, không bao giờ trả 409.
- Người thứ 2 (`cbnv_tw`, `userId f2e93500…`) ghi đè nội dung của người được phân công (`qa_tvvseed28`, `userId 5432719c…`) mà **không nhận bất kỳ cảnh báo nào** → mất dữ liệu âm thầm (last-write-wins).

→ Khớp đúng hiện tượng đối tác báo. Đối chiếu SRS: xem [`../reverify-audit/CNKQHT_06/audit.md`](../reverify-audit/CNKQHT_06/audit.md).
