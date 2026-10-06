# Bảng đối chiếu điều kiện — QLKCHTV_24 (row 13) — Thiếu nút "Trả lời" trên dòng phiên

**Kết luận:** Open.
- Tái hiện đúng: cột **Hành động** chỉ có **duy nhất 1 nút** (con mắt "Xem chi tiết"). Không có nút "Trả lời" ở bất kỳ trạng thái nào.
- Căn cứ đặc tả: `srs-fr-13-tv-nhanh.md:569` yêu cầu cột Hành động gồm *"(Xem / Tra loi)"*.
- Cùng gốc lỗi với QLKCHTV_23 (chỉ có 1 hành động, và hành động đó lại mở chế độ sửa) — đề nghị dev xử lý chung một lần.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_24.jpg` + `.webm` — cùng file video với QLKCHTV_23, đã đối chiếu mã băm MD5 `b01c77c7…` trùng nhau) | Mình test (env nip.io, 27/07/2026 11:54) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Ảnh chụp thẻ **"Hoàn thành"** (URL `?tab=HOAN_TAT`) — các dòng Hoàn thành / Hết hạn. Video cùng đợt cho thấy thẻ **"Tất cả"** với dòng `TVN-20260720-0001` trạng thái **"CB trả lời"** cũng chỉ có nút con mắt | Đo **cả 3 nhóm trạng thái**: CB trả lời (3 phiên) · Hoàn thành (1 phiên) · và toàn bộ thẻ "Tất cả" — **mọi dòng đều chỉ 1 nút con mắt** | Không |
| Dữ liệu tiền đề | Môi trường có sẵn phiên ở nhiều trạng thái | QA tự dựng 4 phiên qua `cms-create` rồi đưa 1 phiên lên "Hoàn thành" bằng luồng trả lời + đánh giá, để phủ được cả nhóm "chưa xong" và "đã xong" | Không |
| Input / filter / giá trị nhập | Mở menu Tư vấn → Tư vấn nhanh, đọc cột Hành động | Mở menu Tư vấn → Tư vấn nhanh, đọc cột Hành động bằng mã lệnh (đếm số nút, đọc nhãn trợ năng) | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-TVN-danh-sach-cot-va-hanh-dong.png` — đã mở đọc: 3 dòng đều trạng thái "CB trả lời", cột Hành động mỗi dòng chỉ có 1 biểu tượng con mắt.
- Đọc thẳng DOM ô Hành động của dòng "CB trả lời":
  - `soNut = 1`
  - nút duy nhất: `aria-label = "Xem chi tiết tư vấn TVN-20260727-0003"`, biểu tượng `anticon-eye`, không có chữ
  - không có phần tử `button`/`a` nào khác trong ô

## Phương pháp thứ hai (bắt buộc)

- **Quét toàn bảng thay vì 1 dòng:** đo lại ở thẻ **"Hoàn thành"** — tiêu đề cột không đổi, dòng `TVN-20260727-0002` (Hoàn thành) cũng chỉ có nút `"Xem chi tiết tư vấn TVN-20260727-0002"`. ⇒ không có trạng thái nào làm xuất hiện nút thứ hai, nên đây không phải "nút bị ẩn theo điều kiện" mà là **không được dựng**.
- **Đối chứng bằng video của đối tác:** frame `reverify-audit/QLKCHTV_24/frames/t003.03s.jpg` (thẻ "Tất cả") cho thấy dòng `TVN-20260720-0001` trạng thái **"CB trả lời"** — đúng trạng thái mà phiếu test nói phải có nút "Trả lời" — cột Hành động vẫn chỉ 1 biểu tượng con mắt, tooltip hiện chữ **"Xem"**.
- **Đối chiếu đặc tả:** `srs-fr-13-tv-nhanh.md:569` — *"| 5 | content | Bang TV nhanh | table | ... / Hanh dong (**Xem / Tra loi**) |"*. Ngoài ra `:572` mô tả cột phải màn trả lời với điều kiện hiển thị *"mode tra loi"*, tức đặc tả có phân biệt rõ hai chế độ.
- **Hệ quả nghiệp vụ đo được:** vì không có nút "Trả lời", đường duy nhất để cán bộ vào soạn trả lời là bấm nút "Xem" — chính là hành vi bị phản ánh ở QLKCHTV_23.
