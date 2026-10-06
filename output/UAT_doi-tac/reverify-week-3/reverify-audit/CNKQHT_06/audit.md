# Audit — CNKQHT_06 (row 12) · "Cập nhật kết quả hỗ trợ khi bản ghi đã bị người khác sửa — ghi đè âm thầm, không hiện thông báo xung đột"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/CNKQHT_06-*.webm/jpg` (`fetch_evidence.py --row 12`). Cột mô tả sheet đối tác (row 12):
  - **Tên chức năng:** Cập nhật kết quả hỗ trợ (khi bản ghi đã bị người khác cập nhật).
  - **Tác nhân:** Cán bộ Nghiệp vụ / người được phân công.
  - **Điều kiện:** vụ việc đang xử lý; bản ghi kết quả đã bị một người khác cập nhật sau khi mình mở màn.
  - **Kỳ vọng:** hệ thống hiện thông báo "Vụ việc đã được {người} cập nhật lúc {giờ}, vui lòng tải lại" và chặn ghi đè.
  - **Kết quả thực tế đối tác báo:** hệ thống **không hiện thông báo** mà **cập nhật thành công** (ghi đè).

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | CB NV/người được phân công cập nhật kết quả, bản ghi đã bị người khác sửa |
| (b) | Hiện tượng đối tác báo | Không có thông báo xung đột → cập nhật ghi đè thành công âm thầm |
| (c) | Kỳ vọng đối tác | Hiện thông báo "đã được {người} cập nhật … vui lòng tải lại", chặn ghi đè |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence:** cột sheet + video — người dùng cập nhật kết quả hỗ trợ khi bản ghi đã cũ, mong đợi bị chặn nhưng lại ghi đè thành công, không có thông báo.
2. **Đối tác phản ánh CỤ THỂ:** thiếu cơ chế khoá lạc quan (optimistic lock) — thao tác cập nhật kết quả không phát hiện xung đột, không hiện thông báo "vui lòng tải lại".
3. **Data + bước tái hiện:** seed 1 vụ việc lên DANG_XU_LY (có bản ghi kết quả) → cập nhật kết quả nhiều lần (cùng người + người thứ 2 khác) dựa trên bản cũ → quan sát mã trả về (201 vs 409) + thông báo + trường `version` của bản ghi.

## Bảng đối chiếu điều kiện

→ [`../../cond/CNKQHT_06.md`](../../cond/CNKQHT_06.md) — **0 GAP**. Test đúng vai trò (người được phân công + CB NV cùng đơn vị) + đúng state (vụ việc đang xử lý, bản ghi kết quả bị người khác sửa) + tái hiện thao tác cập nhật thứ 2 dựa trên bản cũ, kể cả bằng **người dùng khác**.

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

| Nguồn SRS v3.5 | Nói gì | Vị trí |
|---|---|---|
| SCR-V.I-03 §Trạng thái lỗi màn hình — dòng "Xung đột optimistic lock" | Khi có xung đột optimistic lock, hiện **Modal**: "Vụ việc đã được {ho_ten} cập nhật lúc {dd/mm HH:mm}. **Vui lòng tải lại** để xem thông tin mới nhất." + nút **[Tải lại]** | `srs-fr-05-vu-viec.md:1586` |
| SCR-V.I-03 §Trạng thái lỗi màn hình — dòng "Hai cán bộ thao tác cùng lúc" | "Vụ việc đang được {tên cán bộ khác} thao tác. **Vui lòng thử lại sau** {n} giây." (Toast error) | `srs-fr-05-vu-viec.md:1773` |
| BR (Lưu ý cuối §Xử lý) | "**Tất cả chuyển trạng thái SHALL sử dụng optimistic locking.**" | `srs-fr-05-vu-viec.md:2294` |

→ Đặc tả **yêu cầu rõ**: hệ thống phải có cơ chế khoá lạc quan và khi phát hiện bản ghi đã bị người khác cập nhật thì phải hiện thông báo xung đột (`:1586` / `:1773`), **không được ghi đè âm thầm**.

> **Ghi chú phạm vi (minh bạch):** câu `:2294` diễn đạt trực tiếp cho **"chuyển trạng thái"**. Thao tác cập nhật kết quả hỗ trợ (`cap-nhat-ket-qua`) **không đổi trạng thái** (vẫn DANG_XU_LY). Tuy nhiên (1) bản ghi kết quả **có sẵn trường `version`** → hệ thống được **thiết kế để dùng optimistic lock** cho chính bản ghi này; (2) `:1586` là quy tắc **màn hình chi tiết vụ việc** (chung), áp cho mọi cập nhật trên màn; (3) đối tác — bên nắm thiết kế — kỳ vọng có thông báo xung đột. → Việc ghi đè âm thầm giữa 2 người là **lỗi toàn vẹn dữ liệu thật**, không phải mơ hồ đặc tả.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

Seed VV-BTP-TW-20260712-005 lên DANG_XU_LY (kiểm tra hồ sơ → phân công `qa_tvvseed28` → chấp nhận), sau đó cập nhật kết quả nhiều lần và đọc phản hồi máy chủ:

| Lần | Người thao tác | Thân request | HTTP | `version` bản ghi trả về | Kết quả |
|---|---|---|:-:|:-:|---|
| 1 | `qa_tvvseed28` (được phân công) | `{"noiDungKetQua":"…KQ lần 1"}` | **201** | **1** | Tạo/ghi bản ghi kết quả `c557f69b` |
| 2 | `qa_tvvseed28` | `{"noiDungKetQua":"…KQ lần 2"}` (dựa bản cũ) | **201** | **2** | **Ghi đè** lần 1, **không 409**, không thông báo xung đột |
| 3 | **`cbnv_tw` (người KHÁC)** | `{"noiDungKetQua":"…người thứ 2 ghi đè"}` | **201** | **3** | **Ghi đè** nội dung của `qa_tvvseed28`, `nguoiCapNhatId` đổi sang cbnv_tw, **không 409**, không thông báo |

- **Thân request cập nhật KHÔNG kèm version/updated_at kỳ vọng** (chỉ `{noiDungKetQua}`) → máy chủ **không có căn cứ phát hiện xung đột** → không bao giờ trả 409.
- Trường `version` **có tồn tại và tự tăng 1→2→3** → mô hình dữ liệu hỗ trợ optimistic lock, **nhưng endpoint cập nhật không kiểm** → cơ chế bị vô hiệu.
- Không hề xuất hiện modal `:1586` ("vui lòng tải lại") hay toast `:1773` ở bất kỳ lần nào.
- Kiểm bằng phương pháp thứ hai (UI): mở modal "Cập nhật kết quả hỗ trợ" (giới hạn 5000 ký tự) và bấm Xác nhận trên bản ghi đã bị sửa → thao tác vẫn đi qua (POST `cap-nhat-ket-qua` [201]), **không có modal xung đột** (`conflictTextPresent=false`).
- Ảnh: `image/CNKQHT_06-cap-nhat-ket-qua-overwrite-no-conflict.png` (màn kết quả sau khi bị ghi đè).

## Verdict

**`Open`** — Đối tác báo **đúng**. Hệ thống **không áp dụng khoá lạc quan** khi cập nhật kết quả hỗ trợ: 2 người khác nhau (`qa_tvvseed28` → `cbnv_tw`) lần lượt ghi đè cùng một bản ghi kết quả, đều trả **201**, không lần nào phát hiện xung đột (không 409), không hiện thông báo "Vụ việc đã được … cập nhật … vui lòng tải lại" (`:1586`). Bản ghi **có sẵn trường `version` (1→2→3)** chứng minh optimistic lock được thiết kế nhưng **thao tác cập nhật không gửi/không kiểm version** → cơ chế bị vô hiệu → **mất dữ liệu âm thầm (last-write-wins)**. → Đề nghị dev bổ sung kiểm version khi cập nhật kết quả + hiện thông báo xung đột đúng thiết kế khi bản ghi đã bị người khác sửa.
