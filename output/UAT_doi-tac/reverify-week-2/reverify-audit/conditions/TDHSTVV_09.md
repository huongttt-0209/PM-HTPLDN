# Bảng đối chiếu điều kiện — TDHSTVV_09 (Lưu nháp khi mất kết nối)

Evidence đối tác: `partner-evidence/TDHSTVV_09.webm` — frame 00:49: 3 nút "Lưu nháp" / "Gửi KQ" / "Trình duyệt" đều **kẹt ở trạng thái đang tải (spinner)**, Kết luận thẩm định = ĐẠT, **không có thông báo lỗi nào**; khay hệ thống hiện biểu tượng mất kết nối mạng.

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương — badge "Cán bộ NV Trung ương / CB_NV_TW", đơn vị BTP · TW | CB Nghiệp vụ Trung ương — `cbnv_tw`, badge CB_NV_TW, đơn vị BTP · TW (trùng khớp) | Không |
| Entity + trạng thái | Hồ sơ TVV `/chuyen-gia-tvv/720eda6c-…` (cùng hồ sơ loạt video TDHSTVV — `TVV-BTP-TW-0011`), tab Thẩm định mở được ⇒ trạng thái "Đang thẩm định" | Hồ sơ TVV `TVV-BTP-TW-0003`, trạng thái **"Đang thẩm định"** (đã seed ở TDHSTVV_08) | Không |
| Dữ liệu tiền đề | Biểu mẫu thẩm định đã điền, Kết luận thẩm định = ĐẠT | Biểu mẫu đã điền: Kết luận Pháp lý = Đạt, Nhận xét Nhóm 2 có nội dung, Kết luận thẩm định = ĐẠT | Không |
| Input / điều kiện mạng | **Mất kết nối mạng** (icon mạng lỗi ở khay hệ thống), rồi bấm "Lưu nháp" | **Mất kết nối mạng** — bật chế độ Offline của trình duyệt (`navigator.onLine = false`, mọi yêu cầu ra máy chủ đều hỏng), rồi bấm "Lưu nháp" | Không |

Kết luận: **0 GAP** — đã verify đúng vai trò CB_NV_TW, đúng trạng thái "Đang thẩm định", đúng điều kiện mất kết nối của đối tác.

## Quan sát (artifact real-data — loại claim "absence": phải báo lỗi nhưng không báo)

- `navigator.onLine = false` ⇒ trình duyệt thực sự offline.
- Bấm "Lưu nháp" → MutationObserver (cài **trước** cú bấm, theo dõi 5 giây): `addedNodes = 0`.
- Không có `.ant-message-notice-wrapper` / `.ant-notification-notice` / `[role=alert]` / `.ant-form-item-explain-error` nào.
- Console: **không có** thông báo lỗi/cảnh báo nào.
- Kiểm chứng yêu cầu lưu thực sự hỏng khi offline: gọi `POST /api/v1/tu-van-viens/{id}/tham-dinh` → ném `TypeError: Failed to fetch`.
- Ảnh: `TDHSTVV_09-web-offline-luu-nhap-khong-thong-bao-loi.png` — 3 nút "Lưu nháp"/"Gửi KQ"/"Trình duyệt" **kẹt spinner vô hạn**, không thông báo lỗi. **Trùng khớp frame 00:49 của đối tác.**

⇒ Quan sát của đối tác **tái hiện chính xác**: hệ thống nuốt lỗi trong im lặng, người dùng không biết bản nháp đã hỏng.

## Vì sao KHÔNG phải Open mà là BA confirm

- SRS module IV (`srs-fr-04-chuyen-gia-tvv.md`) — FR-IV-06 §Error Handling (dòng 537-541) chỉ có 3 lỗi **nghiệp vụ**: ERR-TD-02 (kết luận ĐẠT khi Nhóm Pháp lý chưa đạt), ERR-TD-03 (thiếu lý do bổ sung), ERR-TD-04 (trình duyệt khi kết luận khác ĐẠT). **Không có** mã lỗi/thông báo nào cho tình huống mất kết nối / lưu thất bại.
- Câu thông báo đối tác kỳ vọng — "Không thể lưu, vui lòng thử lại" — **không tồn tại trong SRS module IV**.
- Đối chiếu module khác: `srs-fr-05-vu-viec.md` dòng 1567 + 1574 **đã** quy định rõ ("Mất kết nối mạng. Đang thử kết nối lại…" / "Lưu thất bại. Vui lòng kiểm tra kết nối và thử lại." + nút [Thử lại]) ⇒ quy ước này có tồn tại trong hệ thống nhưng **chưa được áp cho module Thẩm định TVV**.
- Bất đồng nằm ở **ĐẶC TẢ** (SRS im lặng), không phải ở **THỰC TẾ** (đối tác quan sát đúng) ⇒ theo bảng Verdict: `BA confirm`, QA **không** được tự Reject.
