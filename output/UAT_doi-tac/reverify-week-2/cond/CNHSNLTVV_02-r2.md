# Bảng đối chiếu điều kiện — CNHSNLTVV_02 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:**
- (a) "Màn hình chi tiết hiển thị các trường thông tin không giống với màn hình cập nhật"
- (b) "Khi nhấn Cập nhật, trường thông tin Mô tả kinh nghiệm không hiển thị giá trị hiện tại mặc dù tồn tại dữ liệu"

**Evidence:** `CNHSNLTVV_02_v2.webm` — video 8,2 giây, 11 khung hình (trích bằng `tools/extract_frames.py`).
Diễn biến: màn Chương trình đào tạo → bấm menu "Tư vấn viên / Chuyên gia" → danh sách tab "Mới đăng ký" (3 bản ghi)
→ mở chi tiết `TVV-STP-HN-0004 — NHT TKM` (t≈6,1 s, màn chi tiết render đủ 4 thẻ Hồ sơ / Năng lực / Lịch sử hỗ trợ (0) / Đánh giá (0))
→ **t≈6,3 s trang tự nhảy sang `/403 Forbidden — Mã lỗi ERR-PERM-SYS-00-01 — Vai trò hiện tại: NHT`** và dừng ở đó tới hết video.
Header trong video: **"BTP · DP · hương 3 NHT · NHT"**, thời điểm 25/07/2026 16:01.
⇒ Video dừng ở trang 403, **không** đi tới biểu mẫu "Cập nhật năng lực" — nhưng nó ghi lại **chính sự cố** mà QA log thành bug ở vòng này.

## Bảng đối chiếu — điều kiện tái hiện sự cố trong video

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | Người hỗ trợ pháp lý (**NHT**) — badge "BTP · DP" | `nht_qa_01` — vai trò **NHT** | Không |
| Thao tác | Mở chi tiết 1 tư vấn viên từ danh sách (`/chuyen-gia-tvv/{id}`) | Cùng thao tác, cùng dạng đường dẫn | Không |
| Quan hệ đơn vị NHT ↔ TVV | TVV "NHT TKM" thuộc Sở Tư pháp Hà Nội; video không đọc được đơn vị của NHT | NHT và TVV **cùng đơn vị** — đã đối chiếu `donViId` trùng khít `…8002-000000000006` (Sở Tư pháp An Giang), tức thoả điều kiện thuận lợi nhất mà đặc tả đòi | Không |
| Trạng thái tư vấn viên | Mới đăng ký | Đang hoạt động — đã kiểm chéo: điểm hỏng là lời gọi số đếm đánh giá bị từ chối **theo vai trò** chứ không theo trạng thái (cùng bản ghi: CB Nghiệp vụ nhận 200, NHT nhận 403) | Không |
| Trình duyệt / kích thước cửa sổ | Cốc Cốc trên Windows, cửa sổ tối đa | Chrome 1440×900 — lỗi nằm ở tầng quyền, đã xác nhận bằng nhật ký mạng chứ không bằng quan sát giao diện | Không |

**Kết luận:** 0 GAP — tái hiện đúng hiện tượng trong video, ở điều kiện còn thuận lợi hơn (cùng đơn vị).

## Ghi chú phạm vi — phần kiểm ý (b)

Ý (b) ("Mô tả kinh nghiệm không nạp giá trị") **không dùng để bác bỏ phản ánh của đối tác** và **không tham gia quyết định verdict**;
verdict `Open` đến từ chính sự cố ở bảng trên.

Khi kiểm ý (b), QA buộc phải dùng vai trò **CB Nghiệp vụ cùng đơn vị** — vì vai trò NHT **không mở được** màn chi tiết do đúng lỗi ở bảng trên,
nên không tồn tại cách nào chạy phép đo này bằng NHT trên môi trường hiện tại. Chênh lệch vai trò này được ghi rõ trong
[`audit.md`](../reverify-audit/CNHSNLTVV_02/audit.md) và trong ghi chú gửi đối tác, và là lý do QA **không** kết luận "đối tác báo sai" ở ý (b) —
chỉ ghi nhận "không tái hiện được" kèm đề nghị gửi mã tư vấn viên cụ thể để kiểm đúng bản ghi.

Toàn bộ phép đo + đối chiếu SRS: xem [`../reverify-audit/CNHSNLTVV_02/audit.md`](../reverify-audit/CNHSNLTVV_02/audit.md).
