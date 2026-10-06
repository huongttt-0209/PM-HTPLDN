# Quan sát real-data — NHSYC_07 (Chức năng Lưu nháp)

## Đã tự chạy lại đủ 2 nhánh

**Nhánh (a) — bấm "Lưu nháp" trên form TRỐNG:**
- Hệ thống **chặn lưu**, hiện 5 lỗi bắt buộc: *"Vui lòng chọn doanh nghiệp"*, *"Tiêu đề vụ việc là bắt buộc"*, *"Nội dung yêu cầu là bắt buộc"*, *"Lĩnh vực pháp luật là bắt buộc"*, *"Loại hình hỗ trợ là bắt buộc"*.
- ⇒ **Tái hiện đúng** phản ánh của đối tác ("hệ thống hiển thị kiểm tra bắt buộc nhập khi nhấn Lưu nháp").

**Nhánh (b) — điền đủ trường bắt buộc rồi bấm "Lưu nháp":**
- Toast: **"Đã lưu nháp — VV-BTP-TW-20260712-002"**.
- URL đổi từ `/vu-viec/tao-moi` → `/vu-viec/27cadeda-b600-4bb4-b2b5-9d777fe72428` = **trang chi tiết vụ việc**.
- Bản ghi ở trạng thái **"Mới tạo"** (stepper: Mới tạo → Chờ tiếp nhận → …).
- ⇒ **Tái hiện đúng** phản ánh ("không giữ nguyên màn hình sau khi Lưu nháp thành công").

## Đối chiếu Kết quả mong đợi của test case (3 ý)

| # | Kết quả mong đợi (test case) | Thực tế web | Kết luận |
|:-:|---|---|:-:|
| 1 | Sinh mã hồ sơ theo quy tắc `VV-{mã tỉnh}-{YYYYMMDD}-{số thứ tự}` | `VV-BTP-TW-20260712-002` — đúng quy tắc (BR-DATA-04) | ✅ ĐẠT |
| 2 | Lưu hồ sơ ở trạng thái "Mới tạo" | Trạng thái = **"Mới tạo"** (MOI_TAO) — đúng SCR-V.I-02 dòng 1695 `[Lưu nháp] (→ MOI_TAO)` | ✅ ĐẠT |
| 3 | Hiển thị thông báo + **giữ nguyên màn hình** để tiếp tục nhập | Có thông báo ("Đã lưu nháp — VV-…") nhưng **chuyển sang trang chi tiết** | ⚠️ Xem dưới |

## Điểm mấu chốt: ý 3 của đối tác TRÁI SRS

**FR-V.I-04 (UC54) §Outputs — `srs-fr-05-vu-viec.md` dòng 342, nguyên văn:**

> "**Outputs:** Không có output trực tiếp (xác nhận lưu thành công, **redirect chi tiết VV**)."

⇒ SRS **quy định rõ** sau khi lưu thành công thì **chuyển sang trang chi tiết vụ việc**. Web đang làm **ĐÚNG SRS**. Kỳ vọng "giữ nguyên màn hình để người dùng tiếp tục nhập" của test case **mâu thuẫn với SRS**.

## Ý (a) — validate bắt buộc khi Lưu nháp: SRS im lặng

- Grep toàn bộ `srs-fr-05-vu-viec.md`: **không có clause nào** quy định "Lưu nháp có/không kiểm tra trường bắt buộc" hay "giữ nguyên màn hình".
- SCR-V.I-02 dòng 1695 chỉ ghi nút `[Lưu nháp] (→ MOI_TAO)`, không nói validate gì.
- Đối chiếu thiết kế nội bộ (prototype `pages/vu-viec/form.tsx`): `handleSaveDraft()` chỉ validate **3 trường tối thiểu** (Tên DN, MST, Tiêu đề) rồi cảnh báo *"Cần nhập tối thiểu Tên DN, MST, Tiêu đề"*, và sau khi lưu cũng **rời khỏi form** (điều hướng về danh sách).
- ⇒ Web validate **đủ 5 trường bắt buộc** (chặt hơn thiết kế), SRS không quy định → **khoảng trống đặc tả**, không có căn cứ chấm dev sai.

## Verdict

**BA confirm.** Cả 2 phản ánh của đối tác đều **đúng thực tế** (đã tái hiện), nhưng **không ý nào vi phạm SRS**:
- Ý "không giữ nguyên màn hình" → web **đúng SRS dòng 342** (redirect chi tiết VV); kỳ vọng đối tác trái SRS.
- Ý "validate bắt buộc khi Lưu nháp" → SRS **im lặng**.

Theo quy tắc: đối tác quan sát đúng actual, tranh chấp nằm ở **đặc tả** → `BA confirm`, QA **không tự Reject**.
