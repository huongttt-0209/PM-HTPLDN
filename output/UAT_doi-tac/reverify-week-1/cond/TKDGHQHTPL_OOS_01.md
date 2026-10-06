# Bảng đối chiếu điều kiện — TKDGHQHTPL_OOS_01 (bug QA phát hiện ngoài phạm vi)

**Bối cảnh:** Bug do QA phát hiện khi verify TKDGHQHTPL_02, không thuộc case nào của đối tác nên cột tham chiếu là **điều kiện của lần quan sát gốc** (thay cho evidence đối tác).

**Quan sát gốc:** 27/07/2026, màn "Tổng quan hệ thống" — thẻ hiển thị `29.5/100` kèm chú thích "Dựa trên **14** đánh giá" trong khi chỉ có **11** kết quả ở trạng thái "Đã đánh giá".

| Điều kiện có thể đổi kết quả | Quan sát gốc | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw_02` — Cán bộ NV Trung ương (`CB_NV_TW`), đơn vị BTP · TW | Đúng tài khoản đó, đúng vai trò, đúng đơn vị | Không |
| Môi trường | Env được giao `18.143.165.120.nip.io` — **KHÔNG phải** env đối tác `htpldn-uat.ospgroup.vn` | Đúng `18.143.165.120.nip.io` | Không |
| Màn hình + thẻ | Màn "Tổng quan hệ thống", thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" | Đúng màn đó, đúng thẻ đó | Không |
| Bộ lọc | Năm 2026, Tháng "Cả năm" (mặc định khi mở màn) | Đúng bộ lọc mặc định đó | Không |
| Tiền đề dữ liệu (quyết định lỗi có lộ ra hay không) | Cần đồng thời: ≥1 kết quả đánh giá còn ở "Chưa đánh giá" nhưng đã có sẵn điểm, VÀ ≥1 kế hoạch ở trạng thái "Hủy" có kết quả đã có điểm | Env này có đủ cả hai: 3 kết quả "Chưa đánh giá" mang điểm 80 / 60 / 90 (kế hoạch KHDG-SEED-0001) và kế hoạch DG-20260727-0001 trạng thái "Hủy" có kết quả 100,00 | Không |

**Kết luận:** 0 GAP — đo đúng tài khoản, đúng môi trường, đúng màn, đúng bộ lọc, và tiền đề dữ liệu đã được xác nhận có mặt.

**Lưu ý khi dev re-verify:** env đối tác `htpldn-uat.ospgroup.vn` tại 27/07/2026 **không** thoả tiền đề (6 kết quả có điểm và cả 6 đều đã ở "Đã đánh giá"; không có kế hoạch "Hủy" nào có kết quả mang điểm) — nên mở Dashboard ở env đó sẽ **không** thấy lỗi. Phải dựng đủ tiền đề ở dòng cuối bảng trước khi kết luận.
