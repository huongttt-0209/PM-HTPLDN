# QLLSHTCTVV_04 — Bảng đối chiếu điều kiện

Bug loại **Filter** → kết quả phụ thuộc vai trò + dữ liệu + giá trị lọc → bắt buộc điền bảng
(QA_VERIFY_PROTOCOL §Quy tắc VÀNG). Không dùng miễn trừ `--static-bug`.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ NV Trung ương — góc phải ảnh ghi "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" | `cbnv_tw_02` — "CB Nghiệp vụ - Trung ương #02", vai trò `CB_NV_TW`, đơn vị "BTP · TW". Cùng vai trò, cùng cấp, cùng đơn vị | Không |
| Entity + **trạng thái** (state machine) | Hồ sơ Tư vấn viên ở màn chi tiết `/chuyen-gia-tvv/06748bb5-…`, đã có "Ngày công nhận: 08/05/2026" (tức đã qua phê duyệt), tab "Lịch sử hỗ trợ (4)" | Hồ sơ `TVV-BTP-TW-0002` "QA TVV Seed28 Active", badge **"Đang hoạt động"**, đã có "Ngày công nhận: 12/07/2026" + "Số QĐ công nhận: QD-SEED28-2026", tab "Lịch sử hỗ trợ (6)". Cùng loại entity, cùng giai đoạn state machine (đã công nhận, đang hoạt động) | Không |
| Dữ liệu tiền đề (số vụ việc trong tab + độ trải trạng thái) | 4 vụ việc (thẻ "Tổng vụ việc 4", "Đã hoàn thành 2"); bảng hiện 4 dòng có Ngày phân công 10–13/05/2026, 2 dòng đã có Ngày hoàn thành | 6 vụ việc (thẻ "Tổng vụ việc 6", "Đã hoàn thành 3"); trải **5 trạng thái** `DA_DUYET` 1 · `DA_DANH_GIA` 2 · `DA_PHAN_CONG` 1 · `DANG_XU_LY` 1 · `HOAN_THANH` 1. Tiền đề của mình **rộng hơn** đối tác (nhiều bản ghi hơn, trải nhiều trạng thái hơn) → đủ để tái hiện và đo thêm, không thu hẹp điều kiện | Không |
| Input / filter / giá trị nhập | Bấm mở dropdown "Trạng thái vụ việc", không nhập khoảng ngày. Ảnh bắt đúng khoảnh khắc dropdown đang mở | Bấm mở đúng dropdown "Trạng thái vụ việc" đó, không nhập khoảng ngày; sau đó chọn lần lượt cả 3 giá trị + thử chọn 2 giá trị liên tiếp + thử nút xóa lọc | Không |

**Kết luận: 0 GAP** — đã test đúng vai trò / đúng loại và trạng thái entity / đúng bề mặt và thao tác
của đối tác. Đủ điều kiện chốt verdict.

## Ghi chú khác biệt môi trường (không phải GAP)

Đối tác chụp trên `htpldn-uat.ospgroup.vn`, QA test trên `18.143.165.120.nip.io` (bản dựng
HTPLDN · V1.0.5) — đây là khác biệt môi trường mặc định của đợt UAT này, đã nêu ở
QA_VERIFY_PROTOCOL §Ca biên. Không ảnh hưởng kết luận vì **dropdown trên bản QA test cho ra
đúng 3 giá trị giống hệt ảnh đối tác** ("Đang xử lý" / "Hoàn thành" / "Từ chối") → hiện tượng
tái hiện nguyên vẹn, không phải ca "không tái hiện được".
