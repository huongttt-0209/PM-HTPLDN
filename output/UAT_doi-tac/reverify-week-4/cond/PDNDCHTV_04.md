# Bảng đối chiếu điều kiện — PDNDCHTV_04 (row 21) — Từ chối câu hỏi: không có thông báo kèm lý do; trạng thái hiển thị sai nhãn

**Kết luận:** Open (Major cho ý thông báo; ý trạng thái là **lỗi nhãn hiển thị**, đã có bug riêng).

Phiếu của đối tác gộp 2 ý. Đo tách bạch cho ra 2 kết quả KHÁC NHAU — cần nêu rõ để dev không sửa nhầm:

- **(1) Không gửi thông báo kèm lý do cho cán bộ tạo** — tái hiện ✅, đúng như đối tác mô tả. `:536` yêu cầu *"[Tu choi] modal ly do bat buoc + SET NHAP + **TB CB NV**"*. Đo được: 253 → 253 thông báo, chênh lệch 0. → **Open**
- **(2) "Trạng thái chuyển sang Bị từ chối"** — đối tác mô tả đúng những gì nhìn thấy trên màn, nhưng **nguyên nhân thật khác với suy đoán**: máy chủ lưu trạng thái `NHAP` (Nháp) — **ĐÚNG đặc tả `:536`**. Chỉ có **nhãn hiển thị** của giao diện đang gọi trạng thái `NHAP` là "Bị từ chối". Đây là lỗi nhãn, không phải lỗi luồng trạng thái. → gộp vào bug nhãn trạng thái đã log ở QLKCHTV_02 (đã hiệu chỉnh nguyên nhân gốc)

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/PDNDCHTV_04.webm`, frame t012/t030/t042) | Mình test (env nip.io, 27/07/2026 12:49) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Người từ chối `CB_PD_TW` — "Cán bộ PD Trung ương", BTP · TW. Người kiểm thông báo `CB_NV_TW` | Người từ chối `cbpd_tw` (CB Phê duyệt - Trung ương, BTP · TW); người kiểm thông báo `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP · TW) — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Bản ghi ở tab "Chờ duyệt" → bấm Từ chối → nhập lý do → sau đó dòng hiển thị "Bị từ chối" | Bản ghi `QA-20260727-0002` `CHO_DUYET` → bấm Từ chối → nhập lý do → máy chủ trả `trangThai = "NHAP"`, giao diện hiển thị "Bị từ chối" — **tái hiện đúng hiện tượng đối tác thấy** | Không |
| Dữ liệu tiền đề | Câu hỏi do cán bộ nghiệp vụ tạo | Câu hỏi có `nguoiTaoId` = chính tài khoản `cbnv_tw` dùng để kiểm thông báo (xác minh bằng `GET /api/v1/auth/me`) — điều kiện chặt hơn đối tác | Không |
| Input / filter / giá trị nhập | Nhập lý do từ chối rồi xác nhận | Nhập lý do `"Nội dung câu hỏi chưa rõ ràng, đề nghị cán bộ bổ sung căn cứ pháp lý cụ thể."` rồi bấm [Từ chối]. Đo bằng bộ bắt thông báo dùng chung (tự kiểm `soObserverDangSong = 1`) | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hành vi + Dữ liệu + Hiển thị)

- `bug-reports/image/BUG-PD-04-modal-tu-choi-ly-do.png` — đã mở đọc: modal "Từ chối câu hỏi", ô "Lý do từ chối" có dấu **\*** bắt buộc, nút [Hủy] [Từ chối].
- `bug-reports/image/BUG-PD-04-nhan-nhap-hien-thanh-bi-tu-choi.png` — đã mở đọc, đây là bằng chứng khóa cho ý (2): trên cùng một ảnh thấy đồng thời **địa chỉ trang có `?page=1&trangThai=NHAP`**, **thẻ lọc hiển thị "Bị từ chối"**, và **dòng `QA-20260727-0002` cột Trạng thái ghi "Bị từ chối"**. ⇒ Cùng một giá trị `NHAP` được dán nhãn "Bị từ chối" ở cả bộ lọc lẫn bảng.
- `bug-reports/image/BUG-PD-THONG-BAO-can-bo-tao-khong-nhan.png` — đã mở đọc: khung Thông báo của `CB_NV_TW` không có mục nào về từ chối câu hỏi; mục mới nhất "11 phút trước" (05:43), trong khi thao tác từ chối lúc 05:49.
- Đo bằng bộ bắt thông báo: `SO_REQUEST = 1` (`POST /api/v1/kho-cau-hois/{id}/reject`), `SO_KHUNG_THONG_BAO = 1` ("Từ chối câu hỏi thành công"), không lặp.

## Phương pháp thứ hai (bắt buộc)

- **Ý (1) — đếm ở tầng dữ liệu (phép thử quyết định):** `GET /api/v1/thong-baos` của `cbnv_tw` trước thao tác `total = 253`; sau thao tác từ chối (05:49:57), đo lại `total = 253` — **chênh lệch 0**; thông báo mới nhất vẫn là `2026-07-27T05:43:25`; không bản ghi nào nhắc `QA-20260727-0002` hay lý do từ chối. Đối chứng dương: tài khoản này vẫn nhận `PHE_DUYET` từ 8 entity khác ⇒ đường ống thông báo không hỏng, chỉ `KHO_CAU_HOI` im lặng.
- **Ý (2) — ba phép đo độc lập để chứng minh là lỗi nhãn, không phải lỗi trạng thái:**
  - Đọc bản ghi trực tiếp: `GET /api/v1/kho-cau-hois/{id}` → `"trangThai": "NHAP"` (không phải `BI_TU_CHOI`), `"ghiChuPheDuyet"` lưu đủ nguyên văn lý do từ chối.
  - Lọc theo giá trị thật: `GET /api/v1/kho-cau-hois?trangThai=NHAP` → **trả về đúng bản ghi**; `?trangThai=BI_TU_CHOI` → **0 bản ghi**.
  - Bấm lựa chọn "Bị từ chối" trên bộ lọc giao diện → địa chỉ trang thành `?trangThai=NHAP` và lọc **chạy đúng**. ⇒ Giao diện chỉ đặt sai chữ hiển thị cho giá trị `NHAP`; luồng dữ liệu bên dưới đúng đặc tả.
- **Đối chiếu đặc tả — trích nguyên văn:** `srs-fr-13-tv-nhanh.md:536` (§3 SCR-X2-01, dòng 10): *"[Tu choi] modal ly do bat buoc + **SET NHAP** + **TB CB NV**"*. Vế "modal lý do bắt buộc" ✅, vế "SET NHAP" ✅ (máy chủ đúng), vế "TB CB NV" ❌.
- **Hệ quả cho phiếu tuần trước:** phát hiện này **hiệu chỉnh** bug QLKCHTV_02 (tuần 4, luồng 1) — trước đó QA ghi là "thừa trạng thái Bị từ chối / thiếu Nháp trong bộ lọc". Bản chất đúng là: hệ thống **chỉ có** trạng thái `NHAP`, nhưng **dán nhãn** nó là "Bị từ chối" ở cả bộ lọc lẫn cột Trạng thái. Cách sửa là đổi chữ hiển thị, không phải thêm/bớt trạng thái. Đã cập nhật lại mô tả bug cho dev.
