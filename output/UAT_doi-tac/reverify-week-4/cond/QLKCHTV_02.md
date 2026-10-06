# Bảng đối chiếu điều kiện — QLKCHTV_02 (row 2) — Bộ lọc màn Kho câu hỏi

**Kết luận:** Open — tái hiện 3/3 ý trên env được giao, cùng vai trò CB_NV_TW như đối tác.
Ý quyết định verdict Open = danh sách **Trạng thái** của thanh lọc lệch SRS (thừa "Bị từ chối", thiếu "Nháp").

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res `partner-evidence/QLKCHTV_02.webm`, frame t022.79s + t026.96s) | Mình test (env nip.io, 27/07/2026 10:46) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "CB Nghiệp vụ - Trung ương", đơn vị hiển thị "BTP · TW" (đọc được ở góc phải trên video) | `cbnv_tw` — "CB Nghiệp vụ - Trung ương", "BTP · TW" (ảnh `BUG-QLKCHTV_02-dropdown-nguon.png`) — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Màn `/tv-nhanh/kho-cau-hoi`, chưa áp bộ lọc nào, đang ở tab "Tất cả" | Màn `/tv-nhanh/kho-cau-hoi`, chưa áp bộ lọc nào, đang ở tab "Tất cả" | Không |
| Dữ liệu tiền đề (số bản ghi trong kho) | 36 bản ghi (badge "Tất cả 36 / Đã duyệt 30 / Chờ duyệt 5") | 9 bản ghi (badge "Tất cả 9 / Đã duyệt 9 / Chờ duyệt" trống); API `GET /api/v1/kho-cau-hois?pageSize=100` → 9 record, 100% `trangThai=DA_DUYET`, 100% `nguon=TU_DONG`. **Đã đóng GAP bằng thử nghiệm thật, không phải lập luận:** kho của tôi chỉ chứa DUY NHẤT `DA_DUYET`+`TU_DONG` mà dropdown Nguồn vẫn hiện đủ 3 mục và dropdown Trạng thái vẫn hiện đủ 5 mục ⇒ danh sách lựa chọn là hằng số phía giao diện, KHÔNG sinh từ dữ liệu ⇒ chênh lệch 36 vs 9 bản ghi không đổi được kết quả | Không |
| Input / filter / giá trị nhập | Không nhập gì, chỉ bấm mở dropdown "Nguồn" rồi dropdown "Trạng thái" | Y hệt: không nhập gì, bấm mở dropdown "Nguồn" rồi "Trạng thái" | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-QLKCHTV_02-dropdown-nguon.png` — full-res, đã mở đọc: dropdown Nguồn mở ra đúng 3 mục `Tự động` / `Thủ công` / **`Import`**; đồng thời thấy rõ cả 3 ô lọc (Lĩnh vực, Nguồn, Trạng thái) đang là chữ xám placeholder.
- `bug-reports/image/BUG-QLKCHTV_02-dropdown-trangthai.png` — full-res, đã mở đọc: dropdown Trạng thái mở ra đúng 5 mục **`Bị từ chối`** / `Chờ duyệt` / `Đã duyệt` / `Công khai` / `Hết hiệu lực` — KHÔNG có `Nháp`.
- Đọc DOM xác nhận ô lọc rỗng thật (không phải giá trị đã chọn): cả 3 ô chỉ có `<div class="ant-select-placeholder">`, không có `.ant-select-selection-item`.

## Phương pháp thứ hai (bắt buộc — postmortem C2 "bug candidate ≠ bug")

Ngoài quan sát giao diện, đo thêm bằng tầng mạng — **hai phép đo độc lập cho cùng kết luận**:
- Chính giao diện gọi `GET /api/v1/kho-cau-hois?trangThai=CHO_DUYET,**NHAP**&page=1&pageSize=1` để đếm badge tab "Chờ duyệt" ⇒ trạng thái `NHAP` là trạng thái CÓ THẬT và đang được dùng trong hệ thống, nhưng lại **vắng mặt trong dropdown lọc**.
- Không có bản ghi `BI_TU_CHOI` nào trong dữ liệu (9/9 là `DA_DUYET`) ⇒ mục "Bị từ chối" là hằng số giao diện, không phải sinh từ dữ liệu.
- `GET /api/docs-json`: `KhoCauHoiListQueryDto.trangThai` khai kiểu `string` trần, **không khai enum** ⇒ tầng API không ràng buộc danh sách trạng thái; danh sách hiển thị hoàn toàn do giao diện quyết định.
