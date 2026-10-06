# Bảng đối chiếu điều kiện — THDG_05 (row 72)

**Case:** Chấm điểm ở đợt đánh giá **nhiều người** — đối tác báo bấm "Lưu kết quả" phát sinh lỗi *"Vụ việc 'aad90004-…-002' không có kết quả đánh giá trong kế hoạch này"*.
**Verdict:** **Open** (bug ĐÚNG — hiện tượng TÁI HIỆN ở kịch bản đúng: chấm vụ việc đã phân cho người đánh giá khác).
**Verify:** 22/07/2026, Chrome DevTools MCP, tài khoản `cbnv_tw` (CB Nghiệp vụ - Trung ương / CB_NV_TW — trùng vai trò đối tác), đợt tự seed `DG-20260722-0002` (2 người đánh giá, 2 VV round-robin).

> **Điều kiện gây lỗi của đối tác (đọc full-res `partner-evidence/THDG_05.jpg`):** tab Chấm điểm có **4 VV**, đối tác chấm 3 VV, thao tác **"Lưu kết quả"** → toast đỏ *"Vụ việc 'aad90004-0000-4000-8000-000000000002' không có kết quả đánh giá trong kế hoạch này"*. Thông báo này chỉ phát sinh khi payload chứa một VV **không có bản ghi kết quả gắn với người đang đăng nhập** trong kế hoạch — tức VV thuộc kế hoạch nhưng **được phân cho người đánh giá khác** (đợt nhiều người). Điều kiện gây lỗi = **"đợt có nhiều người đánh giá + người dùng nhập/lưu điểm cho VV đã phân cho người khác"**.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res THDG_05.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ - Trung ương (CB_NV_TW), tab Chấm điểm | `cbnv_tw` (CB Nghiệp vụ - Trung ương / CB_NV_TW) — trùng vai trò | Không |
| Entity + trạng thái | Đợt đánh giá đang ở bước chấm điểm (nhiều VV được chọn để chấm) | Đợt `DG-20260722-0002` bước Thực hiện, tab Chấm điểm, 2 VV được chọn | Không |
| Dữ liệu tiền đề: **đợt NHIỀU người đánh giá** (điều kiện gây lỗi) | Toast trích mã VV nội bộ (`aad90004-…-002`) → có VV trong bảng không gắn kết quả của người đăng nhập ⇒ đợt phân cho **nhiều người** | Seed đợt **2 người đánh giá** (`cbnv_tw` Trưởng nhóm + `cbnv_tw_02` Đánh giá viên); chọn 2 VV → round-robin: `EEE-VH-013` phân `cbnv_tw`, **`EEE-VH-014` phân `cbnv_tw_02`** (xác nhận qua API `GET .../ket-quas` `nguoiDanhGiaId`) — trùng điều kiện gây lỗi | Không |
| Hành vi khi nhập/lưu điểm cho VV người khác | Đối tác báo: toast lỗi *"Vụ việc X không có kết quả đánh giá trong kế hoạch này"* | **TÁI HIỆN:** FE Chấm điểm hiển thị cả `EEE-VH-014` (của `cbnv_tw_02`) với ô nhập điểm mở như VV của mình; nhập 8 → "Lưu kết quả" → toast đỏ + `PUT .../ket-quas` **[422]** `ERR-DG-SC-04` *"Vụ việc 'eeeeeeee-…-014' không có kết quả đánh giá trong kế hoạch này"* | Không |

**Kết luận: 0 GAP điều kiện.** Đã tái hiện đúng kịch bản gây lỗi của đối tác (đợt nhiều người đánh giá, thao tác trên VV phân cho người khác) trên env được giao. **Lỗi TÁI HIỆN** → không thuộc định nghĩa Reject. App sai rule SRS rõ ràng: FR-VI-06 (UC88) §Preconditions dòng 471 + §Processing Bước 2 (BR-AUTH-01) dòng 488 quy định *người đánh giá chỉ chấm VV được phân công*; FE lại cho nhập điểm VV của người khác rồi backend trả lỗi **sai bản chất** (mã `ERR-DG-SC-04` + thông báo không có trong SRS, khiến hiểu nhầm VV không thuộc kế hoạch). → **Open**.

> **Lưu ý audit (không partner-facing) — đính chính so với bảng round trước:** Bảng cũ kết luận `Reject` vì test SAI kịch bản — chỉ dựng đợt **1 người đánh giá** và thử "lưu một phần / để trống VV". Ở đợt 1 người, MỌI VV đều thuộc người đăng nhập nên lưu một phần chạy đúng → không chạm điều kiện gây lỗi. Toast của đối tác trích **mã VV nội bộ** ⇒ payload có VV không gắn kết quả của người đăng nhập ⇒ điều kiện thực là **đợt NHIỀU người đánh giá + chấm VV người khác**. Bảng này dựng đúng đợt nhiều người → đóng GAP thật, lỗi tái hiện.

**Evidence:**
- `../../bug-reports/thdg/image/THDG_05-01-scoringtable-shows-foreign-vv-editable.png` — tab Chấm điểm hiển thị cả `EEE-VH-014` (phân cho `cbnv_tw_02`) với ô nhập điểm mở.
- `../../bug-reports/thdg/image/THDG_05-02-foreign-vv-save-422-toast.png` — nhập điểm 8 cho `EEE-VH-014` ngay trong bảng.
- Toast đỏ (MutationObserver, class `ant-message-notice-error`): *"Vụ việc 'eeeeeeee-…-014' không có kết quả đánh giá trong kế hoạch này"*.
- Network `PUT /api/v1/ke-hoach-danh-gias/de086bc5-.../ket-quas` → **422** `ERR-DG-SC-04`.
- API `GET .../ket-quas`: `EEE-VH-013 → nguoiDanhGiaId f2e93500` (cbnv_tw), `EEE-VH-014 → nguoiDanhGiaId 75ef9f6b` (cbnv_tw_02) → `EEE-VH-014` thuộc kế hoạch nhưng phân cho người khác.
