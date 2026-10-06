# Bảng đối chiếu điều kiện — CNKQVV_05

Loại bug: **Cập nhật kết quả cuối / hoàn thành vụ việc khi vụ việc đã bị người khác hoàn thành trước → thông báo SAI (không phải thông báo xung đột) + đối tác báo thêm "thông báo lặp".** Kết quả phụ thuộc role (CB Nghiệp vụ hoàn thành) + state (vụ việc Đã duyệt, bị người khác hoàn thành trước) → điền bảng, xác nhận đã test đúng điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác (từ cột Điều kiện/Bước + video) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **Cán bộ Nghiệp vụ** hoàn thành vụ việc (cập nhật kết quả cuối) | `cbnv_tw` — CB_NV_TW (đúng nhóm vai trò được phép hoàn thành theo `FR-V.I-16 §PRE-03 role∈{CB_NV,DN}`) | Không |
| Trạng thái vụ việc | Vụ việc **Đã duyệt** (sẵn sàng hoàn thành), nhưng đã bị **người khác hoàn thành trước** | Gọi thao tác hoàn thành trên vụ việc đang ở **HOAN_THANH** (đã bị hoàn thành) — đúng tình huống "người thứ 2 bấm hoàn thành sau khi người thứ nhất đã xong"; đồng thời quan sát render thông báo lỗi hoàn thành trên VV-SEED-0001 (DA_DUYET) | Không |
| Tình huống xung đột (người khác đã hoàn thành) | Bản ghi đã bị người khác chuyển trạng thái sau khi mình mở màn | Tái hiện: thao tác hoàn thành của "người thứ 2" trên vụ việc **đã HOAN_THANH** → quan sát máy chủ trả gì (thông báo xung đột hay lỗi khác) | Không |
| Hiện tượng cần quan sát | (1) **Thông báo SAI** (không phải "vui lòng tải lại"); (2) đối tác báo thêm **thông báo lặp (duplicate)** | (1) Xác nhận thông báo SAI; (2) đo số khung thông báo bằng observer (không lọc trùng) | Không |

**Kết luận: 0 GAP về role/state/data.** Đã test đúng vai trò (CB NV) + đúng điều kiện (vụ việc đã duyệt, bị người khác hoàn thành trước) + tái hiện thao tác hoàn thành của người thứ 2.

**Kết quả 2 ý con (minh bạch — chỉ xác nhận 1/2):**
- **Ý "thông báo SAI" — XÁC NHẬN đúng đối tác:** người thứ 2 bấm hoàn thành trên vụ việc đã HOAN_THANH → máy chủ trả **HTTP 409** với thông báo **"ERR-STATE-V-HT-01: Vụ việc không ở trạng thái DA_DUYET"** — **KHÔNG** phải thông báo xung đột optimistic lock `:1586` ("Vụ việc đã được … cập nhật … vui lòng tải lại"). Thông báo còn **lộ mã lỗi kỹ thuật** `ERR-STATE-V-HT-01` ra người dùng (cùng loại BUG-VV-MALOI-LO-UI). Thân request hoàn thành **không kèm version** → không có cơ chế phát hiện xung đột đúng thiết kế.
- **Ý "thông báo lặp" — KHÔNG tái hiện:** đo bằng observer (không lọc trùng, đọc `innerText`) trên thao tác hoàn thành lỗi → chỉ **1** khung thông báo (`.ant-message-notice-wrapper`), text "ERR-STATE-V-HT-02: Chưa có kết quả xử lý", **không lặp**. (Con số "2" của lần đo cũ là do đếm cả node container lồng nhau, không phải 2 thông báo.)

→ Verdict tổng: **`Open`** (theo quy tắc đa-ý: ≥1 ý con là lỗi thật → Open). Chi tiết: xem [`../reverify-audit/CNKQVV_05/audit.md`](../reverify-audit/CNKQVV_05/audit.md).
