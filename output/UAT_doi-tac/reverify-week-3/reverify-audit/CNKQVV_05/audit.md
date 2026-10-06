# Audit — CNKQVV_05 (row 14) · "Cập nhật kết quả cuối / hoàn thành vụ việc khi bị người khác sửa — thông báo sai + (đối tác báo) duplicate"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/CNKQVV_05-*.webm/jpg` (`fetch_evidence.py --row 14`). Cột mô tả sheet đối tác (row 14):
  - **Tên chức năng:** Cập nhật kết quả cuối và hoàn thành vụ việc (khi bản ghi đã bị người khác cập nhật/hoàn thành).
  - **Tác nhân:** Cán bộ Nghiệp vụ.
  - **Điều kiện:** vụ việc Đã duyệt; đã bị người khác hoàn thành trước khi mình bấm.
  - **Kỳ vọng:** hiện thông báo xung đột "Vụ việc đã được {người} cập nhật lúc {giờ}, vui lòng tải lại".
  - **Kết quả thực tế đối tác báo:** thông báo **sai** + **lặp (duplicate)**.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | CB NV hoàn thành vụ việc Đã duyệt, đã bị người khác hoàn thành trước |
| (b) | Hiện tượng đối tác báo | Thông báo SAI (không phải thông báo xung đột) + thông báo lặp |
| (c) | Kỳ vọng đối tác | Hiện thông báo "đã được {người} cập nhật … vui lòng tải lại" |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence:** cột sheet + video — người thứ 2 hoàn thành vụ việc đã bị người khác hoàn thành, nhận thông báo sai (không phải thông báo xung đột) và bị lặp.
2. **Đối tác phản ánh CỤ THỂ:** (i) thao tác hoàn thành khi xung đột không hiện thông báo optimistic lock đúng thiết kế mà hiện thông báo khác (sai); (ii) thông báo bị lặp.
3. **Data + bước tái hiện:** gọi thao tác hoàn thành trên vụ việc đã HOAN_THANH (mô phỏng người thứ 2) → quan sát mã + nội dung thông báo (có phải `:1586` không, có lộ mã lỗi không); đo số khung thông báo trên thao tác hoàn thành lỗi bằng observer.

## Bảng đối chiếu điều kiện

→ [`../../cond/CNKQVV_05.md`](../../cond/CNKQVV_05.md) — **0 GAP**. Test đúng vai trò (CB NV) + đúng state (vụ việc đã duyệt, bị người khác hoàn thành trước).

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

| Nguồn SRS v3.5 | Nói gì | Vị trí |
|---|---|---|
| BR (Lưu ý cuối §Xử lý) | "**Tất cả chuyển trạng thái SHALL sử dụng optimistic locking.**" — hoàn thành (DA_DUYET→HOAN_THANH) **là một chuyển trạng thái** → thuộc phạm vi này trực tiếp | `srs-fr-05-vu-viec.md:2294` |
| SCR-V.I-03 §Trạng thái lỗi màn hình — "Xung đột optimistic lock" | Hiện **Modal**: "Vụ việc đã được {ho_ten} cập nhật lúc {dd/mm HH:mm}. **Vui lòng tải lại**…" + [Tải lại] | `srs-fr-05-vu-viec.md:1586` |
| SCR-V.I-03 §Trạng thái lỗi màn hình — "Hai cán bộ thao tác cùng lúc" | "Vụ việc đang được {tên} thao tác. Vui lòng thử lại sau {n} giây." | `srs-fr-05-vu-viec.md:1773` |
| Chuẩn thông báo lỗi (chung) | Thông báo hiển thị cho người dùng **không được lộ mã lỗi kỹ thuật nội bộ** (mô tả nghiệp vụ, không phải mã ERR) | cùng chuẩn BUG-VV-MALOI-LO-UI |

→ Hoàn thành vụ việc **là chuyển trạng thái** → theo `:2294` **bắt buộc** dùng optimistic lock; khi phát hiện xung đột phải hiện thông báo `:1586`/`:1773`, và thông báo không được lộ mã lỗi.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

**Ý 1 — "thông báo SAI" (XÁC NHẬN đúng đối tác):**
- Mô phỏng "người thứ 2" hoàn thành vụ việc **đã ở HOAN_THANH** (VV-BTP-TW-20260712-001) bằng `cbnv_tw`: thân request `{ketLuanCuoi, ketQuaXuLy:"THANH_CONG"}` — **KHÔNG kèm version**.
- Máy chủ trả **HTTP 409**, thông báo: **"ERR-STATE-V-HT-01: Vụ việc không ở trạng thái DA_DUYET"**.
  - **KHÔNG** phải thông báo xung đột optimistic lock `:1586` ("Vụ việc đã được … cập nhật … vui lòng tải lại") mà đối tác kỳ vọng → **thông báo sai** đúng như đối tác báo.
  - Thông báo **lộ mã lỗi kỹ thuật** `ERR-STATE-V-HT-01` ra người dùng (cùng loại BUG-VV-MALOI-LO-UI).
- Kiểm chứng phương pháp thứ hai (UI): bấm [Hoàn thành] trên VV-SEED-0001 (DA_DUYET, chưa có kết quả) → POST `hoan-thanh` [409], thông báo hiển thị (observer bắt được): **"ERR-STATE-V-HT-02: Chưa có kết quả xử lý"** — cũng lộ mã lỗi.

**Ý 2 — "thông báo lặp / duplicate" (KHÔNG tái hiện):**
- Đo bằng observer (`MutationObserver`, **không lọc trùng**, đọc `innerText`) trên thao tác hoàn thành lỗi VV-SEED-0001 → chỉ **1** khung `.ant-message-notice-wrapper`, text "ERR-STATE-V-HT-02: Chưa có kết quả xử lý", **không lặp**.
- Con số "2" ở lần đo trước là do đếm cả node container lồng nhau (container + wrapper) của **cùng 1** thông báo, **không phải 2 thông báo**. → Ý "duplicate" **không xác nhận được** ở luồng hoàn thành này.
- Ảnh: `image/CNKQVV_05-modal-hoan-thanh.png` (modal "Hoàn thành vụ việc"), `image/CNKQVV_05-hoan-thanh-loi-state.png` (vụ việc vẫn "Đã duyệt" sau thao tác lỗi).

## Verdict

**`Open`** — theo quy tắc đa-ý (≥1 ý con là lỗi thật → Open):
- **Ý "thông báo sai" = lỗi thật:** khi hoàn thành vụ việc (một chuyển trạng thái — thuộc `:2294`) mà vụ việc đã bị người khác hoàn thành, hệ thống **không** hiện thông báo xung đột `:1586`/`:1773` mà hiện thông báo lỗi trạng thái **lộ mã kỹ thuật** ("ERR-STATE-V-HT-01: …"). Thao tác hoàn thành **không kèm version** → không có cơ chế phát hiện xung đột đúng thiết kế.
- **Ý "thông báo lặp" = KHÔNG tái hiện** (chỉ 1 khung thông báo) → ghi rõ để dev không phải sửa phần này.
- → Đề nghị dev: (1) bổ sung kiểm version + hiện thông báo xung đột đúng thiết kế (`:1586`/`:1773`) khi hoàn thành vụ việc đã bị người khác chuyển trạng thái; (2) bỏ mã lỗi kỹ thuật (`ERR-STATE-V-HT-*`) khỏi thông báo hiển thị cho người dùng.
