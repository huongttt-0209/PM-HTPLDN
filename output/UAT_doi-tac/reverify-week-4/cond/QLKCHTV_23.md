# Bảng đối chiếu điều kiện — QLKCHTV_23 (row 12) — Nút "Xem" mở màn trả lời ở chế độ chỉnh sửa

**Kết luận:** Open.
- Tái hiện đúng: với phiên ở trạng thái **"CB trả lời"**, bấm nút con mắt (Xem) mở thẳng màn trả lời ở **chế độ nhập liệu** — ô soạn sửa được, nút [Gửi trả lời] hoạt động.
- Có căn cứ đặc tả: `srs-fr-13-tv-nhanh.md:569` quy định cột Hành động gồm **hai** hành động tách biệt *"(Xem / Tra loi)"*. Hệ thống chỉ có **một** nút và nút đó cho sửa.
- Chứng minh chế độ chỉ-xem **có tồn tại** trong hệ thống (phiên "Hoàn thành" mở ra không có ô nhập nào) ⇒ vấn đề là gán sai chế độ cho trạng thái "CB trả lời", không phải chưa làm.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_23.jpg` + `.webm`, 4 frame ở `reverify-audit/QLKCHTV_23/frames/`) | Mình test (env nip.io, 27/07/2026 11:56) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW (đọc rõ ở frame t003, t006, t009) | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Phiên `TVN-20260720-0001`, Trạng thái **"CB trả lời"** (frame t003 đọc rõ nhãn ở cột Trạng thái) | Phiên `TVN-20260727-0001`, Trạng thái **"CB trả lời"** — TRÙNG KHỚP. **Bổ sung**: đo thêm phiên `TVN-20260727-0002` ở trạng thái **"Hoàn thành"** để đối chứng chế độ chỉ-xem | Không |
| Dữ liệu tiền đề | Phiên đã được cán bộ mở xử lý (đang ở CB trả lời), chưa gửi trả lời | Phiên đã ở CB trả lời, chưa gửi trả lời — TRÙNG KHỚP. Phiên do QA tự dựng qua `cms-create` vì môi trường ban đầu 0 bản ghi | Không |
| Input / filter / giá trị nhập | Bấm nút con mắt ở cột Hành động của dòng đó (tooltip hiện chữ "Xem" — frame t003) | Bấm đúng nút đó: `button[aria-label="Xem chi tiết tư vấn TVN-20260727-0001"]` | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hành vi + Hiển thị/render)

- `bug-reports/image/BUG-TVN-man-tra-loi-cot-trai.png` — đã mở đọc: sau khi bấm Xem, màn hiện ô "Nội dung trả lời" **nhập được** (`0 / 5000`) + nút **[Gửi trả lời]** màu xanh đang bật.
- Đọc thẳng DOM sau khi bấm Xem trên phiên **CB trả lời**:
  - `textarea[placeholder="Nhập nội dung trả lời hoặc chọn từ Kho câu hỏi ở trên..."]` → `disabled=false`, `readOnly=false`
  - Ô tìm kiếm Kho câu hỏi → `disabled=false`
  - Danh sách nút: `["Quay lại danh sách", "Tìm kiếm", "Gửi trả lời"]`
- `bug-reports/image/BUG-TVN-danh-sach-cot-va-hanh-dong.png` — cột Hành động chỉ có **1** nút con mắt cho mọi dòng.

## Phương pháp thứ hai (bắt buộc)

- **Đối chứng bằng trạng thái khác (phép thử quyết định):** mở cùng một nút con mắt trên phiên `TVN-20260727-0002` ở trạng thái **"Hoàn thành"** → màn hiện **`soInput = 0`** (không có ô nhập nào), danh sách nút chỉ còn `["Quay lại danh sách"]`, không có [Gửi trả lời]. ⇒ **Chế độ chỉ-xem có tồn tại**; hệ thống chọn chế độ theo *trạng thái phiên* chứ không theo *hành động người dùng bấm*. Vì vậy ở "CB trả lời" người dùng không có cách nào chỉ xem mà không sửa.
- **Video của đối tác xác nhận cùng hành vi:** frame `t003.03s.jpg` cho thấy con trỏ trên nút con mắt (tooltip "Xem") ở dòng `TVN-20260720-0001` trạng thái "CB trả lời"; frame `t009.06s.jpg` cho thấy màn kết quả là màn trả lời **đang mở dropdown "Lĩnh vực pháp lý"**, ô "Nội dung trả lời" trống nhập được (`0 / 5000`) và nút [Gửi trả lời] hiện diện.
- **Đối chiếu đặc tả:** `srs-fr-13-tv-nhanh.md:569` — *"... / Hanh dong (**Xem / Tra loi**)"*. Đặc tả tách hai hành động; kèm theo `:571` mô tả cột trái và `:572` mô tả cột phải chỉ áp dụng ở *"mode tra loi"* ⇒ hàm ý tồn tại một chế độ khác không phải chế độ trả lời.
