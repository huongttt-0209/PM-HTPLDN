# Bảng đối chiếu điều kiện — CNDSMLTVV_OOS_01 (row 140, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Công khai mạng lưới TVV — FR-IV-08 (UC46), màn SCR-IV-01 "Danh sách Tư vấn viên", thanh thao tác hàng loạt
**Nội dung TC:** nút "Hủy công khai" hàng loạt gỡ hồ sơ khỏi Cổng PLQG ngay khi bấm, không mở `MD-HUY-CONG-KHAI` để xác nhận (SRS `:1465` + `:1407`).
**Loại bug:** hành vi phụ thuộc **trạng thái entity** (chỉ bấm được khi dòng đang ở trạng thái Công khai) + **thao tác** → KHÔNG phải bug tĩnh, BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG).
**Ngày verify:** 2026-08-03 · **Tài khoản QA dùng:** `cbnv_tw_02` (CB_NV_TW, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW)

> **Nguồn gốc dòng TC:** lỗi do QA tự phát hiện khi verify CNDSMLTVV_01 (row 124), nằm ngoài tiêu chí của phiếu nên mở dòng mới. **Không có evidence đối tác cho riêng lỗi này** — cột "Đối tác" ghi rõ "Không áp dụng" thay vì suy diễn điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | `cbnv_tw_02` — "CB Nghiệp vụ - Trung ương #02", vai trò `CB_NV_TW`, đơn vị `Cục Bổ trợ tư pháp - Bộ Tư pháp`, cấp `BTP · TW`. Chọn đúng vai trò này vì `FR-IV-08:657` chỉ đích danh **CB Nghiệp vụ** là người thao tác trong luồng công khai | Không |
| Màn hình + tab | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Màn "Tư vấn viên / Chuyên gia" (`/chuyen-gia-tvv/danh-sach`), tab **"Đang hoạt động"** — đúng tab mà `:1465` quy định cho thao tác hủy công khai hàng loạt | Không |
| Trạng thái entity (điều kiện bắt buộc để bấm được nút) | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | `TVV-SEED-0001` "Nguyễn Văn Seed" — `trangThai = HOAT_DONG`, **`laCongKhai = true`**. Trạng thái công khai này do QA **dựng bằng chính luồng công khai hàng loạt của phần mềm** ngay trước bước đo (1 lệnh, 1 thông báo "Đã công khai tư vấn viên thành công"), không sửa dữ liệu trực tiếp | Không |
| Thao tác / nút bấm | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Tích chọn 1 dòng → bấm **[Hủy công khai]** trên thanh thao tác hàng loạt, đúng 1 lần | Không |
| Cửa sổ quan sát | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Quan sát tại **7 mốc**: 50 / 150 / 300 / 600 / 1000 / 1500 / 2200 mili-giây sau khi bấm; mỗi mốc kiểm cả hộp thoại thường, hộp thoại xác nhận và bong bóng xác nhận | Không |

## Ghi chú đóng GAP

- **Không có ô GAP nào vì không có điều kiện đối tác để lệch:** dòng TC do QA mở, toàn bộ điều kiện do QA tự dựng và đã ghi đủ ở cột "Mình test".
- **Điều kiện tiền đề được SEED, không né:** muốn quan sát hành vi hủy công khai thì bắt buộc phải có hồ sơ đang công khai. QA đã dựng đúng trạng thái đó qua giao diện thay vì đổi sang hồ sơ "tiện hơn" hay kết luận suông.
- **Đo được cả sự vắng mặt lẫn thời điểm:** cả 7/7 mốc đều `coModal = false` và `coHopThoaiXacNhan = false`. Quan trọng hơn: **tại mốc 50 mili-giây, số lệnh đã gửi = 1** — nghĩa là lệnh gỡ công khai đi trước bất kỳ cơ hội xác nhận nào, không phải "hộp thoại đóng quá nhanh nên không chụp kịp".
- **Đối chứng chiều ngược lại trong cùng màn hình, cùng tài khoản:** thao tác **công khai** hàng loạt **có** mở hộp thoại (đo được `.ant-modal-container`, tiêu đề "Công khai hàng loạt lên Cổng PLQG"). Vậy thiếu bước xác nhận chỉ xảy ra ở chiều hủy công khai, không phải app không dùng hộp thoại.
- **Đã loại trừ lỗi phép đo:** bộ bắt thông báo tự kiểm `soObserverDangSong = 1` trước khi tin số liệu; đếm được đúng 1 lệnh — 1 thông báo *"Đã hủy công khai tư vấn viên thành công"*. Tái hiện 3/3 lần.
- **Dữ liệu đã hoàn trả:** `TVV-SEED-0001` kết thúc ở đúng trạng thái ban đầu **Chưa công khai** (`laCongKhai = false`); các hồ sơ khác (`TVV-BTP-TW-0002`, `DDD-TVV-022`, `DDD-TVV-021`, `TVV-STP-AG-0001`) không bị đụng.

**Kết luận: 0 GAP** — mọi điều kiện quan sát lỗi đã được dựng và test thật.
