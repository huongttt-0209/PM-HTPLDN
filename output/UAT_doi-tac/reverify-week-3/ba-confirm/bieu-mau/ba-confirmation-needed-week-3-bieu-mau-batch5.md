# BA confirmation needed — Biểu mẫu Batch 5 (QLBMHD sửa/xem/preview/tải, rows 105–112) — 2026-07-20

> **File này để làm gì:** gom các testcase Batch 5 mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI. Bug có SRS reference rõ → log ở `../../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch5.md`.
> **SRS dùng:** v3.5 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md` (FR-VII-04 / UC95 / SCR-VII-02).

---

## QLBMHD_12 — Nút "Sửa" hiển thị trên biểu mẫu Công khai (SRS không quy định điều kiện state)

**Bối cảnh testcase**

- Dòng Excel: 105, mã TC `QLBMHD_12`.
- Nội dung kiểm tra: CB Nghiệp vụ mở màn Danh sách biểu mẫu, kiểm điều kiện hiển thị nút "Sửa" theo trạng thái biểu mẫu.
- Expected trong file UAT:
  - Nút "Sửa" **chỉ được hiện** ở biểu mẫu trạng thái Nháp / Ẩn + đúng đơn vị.
- Actual đối tác ghi: nút "Sửa" hiện **cả ở biểu mẫu Công khai**.

**Đối chiếu SRS v3.5**

- SCR-VII-02 (màn Quản lý biểu mẫu) quy định cột Hành động gồm "Xem trước (mặc định) / Tải về / Sửa / Xóa" — **không** kèm điều kiện trạng thái cho nút Sửa.
- Khác với SCR-VII-01 (màn *thư mục*): ở đó điều kiện "(khi NHAP/AN, rỗng)" chỉ gắn với nút **Xóa**, cũng **không** gắn với nút Sửa.
- FR-VII-04 phần AC "chỉnh sửa" chỉ nêu "cập nhật + upload lại file → validate và lưu", không ràng buộc trạng thái. State machine SM-BIEUMAU không có quy tắc cấm sửa khi CONG_KHAI.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:649` (SCR-VII-02 #12 — Cột Hành động)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:615` (SCR-VII-01 #13 — điều kiện chỉ áp cho Xóa, không áp cho Sửa)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:372` (FR-VII-04 AC chỉnh sửa)

**Kết quả verify UI hiện tại**

- Verify ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB Nghiệp vụ - Trung ương (BTP·TW).
- Mở URL `https://18.143.165.120.nip.io/bieu-mau/danh-sach`.
- Danh sách có 2 biểu mẫu: BM-20260715-001 (Nháp) và BM-SEED-0001 "Biểu mẫu hợp đồng tư vấn seed" (**Đã công khai**).
- Cả 2 dòng đều hiển thị nút Sửa; nút Sửa **có** hiện trên dòng biểu mẫu Công khai (BM-SEED-0001) — khớp phản ánh đối tác. Xác minh qua `evaluate_script` (actions = ["Tải về","Sửa","Xóa"]) + screenshot.
- Đối chiếu: hành vi web PHÙ HỢP SRS (SRS không cấm sửa khi Công khai).
- Evidence: `../../reverify-audit/QLBMHD_12/QLBMHD_12-list-sua-on-congkhai.png`

**Kết luận QA**

- `QLBMHD_12` không phải bug theo SRS v3.5: SRS không quy định ẩn nút Sửa theo trạng thái biểu mẫu.
- Web hiện tại đúng SRS ở điểm này; đối tác quan sát đúng thực tế nhưng kỳ vọng (Sửa chỉ Nháp/Ẩn) là ràng buộc SRS chưa có.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý:

- Có bổ sung ràng buộc "ẩn/không cho sửa biểu mẫu khi đang Công khai" vào đặc tả không? Đây là ràng buộc nghiệp vụ hợp lý (sửa nội dung đang công khai = đổi nội dung public) nhưng SRS hiện chưa quy định.
- Nếu CÓ → thay đổi đặc tả, owner Dev FE (ẩn nút Sửa theo state). Nếu KHÔNG → cập nhật lại expected của testcase theo SRS.
- Verdict QA đề xuất: `Cần BA xác nhận` — chưa gửi Dev tới khi BA chốt.

---

## QLBMHD_13 — Form Chỉnh sửa không hiển thị file đang đính kèm (SRS silent về hiển thị file hiện tại)

**Bối cảnh testcase**

- Dòng Excel: 106, mã TC `QLBMHD_13`.
- Nội dung kiểm tra: CB Nghiệp vụ bấm "Sửa" một biểu mẫu đã có file → quan sát form Chỉnh sửa có hiển thị file đính kèm không.
- Expected trong file UAT: form Chỉnh sửa hiển thị file đang đính kèm.
- Actual đối tác ghi: form Chỉnh sửa **không hiển thị file đính kèm dù tồn tại file**.

**Đối chiếu SRS v3.5**

- SCR-VII-02 #15: trường "File đính kèm" (file-upload) hiển thị "khi tạo/sửa", Bắt buộc.
- FR-VII-04 AC phần chỉnh sửa: "cập nhật + upload lại file (nếu cần)" — tải lại file là TÙY CHỌN khi sửa → hàm ý file cũ được giữ.
- SRS **không có clause minh thị** yêu cầu form Sửa phải hiển thị/preview file đang đính kèm.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:652` (SCR-VII-02 #15 — File đính kèm khi tạo/sửa)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:372` (FR-VII-04 AC chỉnh sửa — upload lại file nếu cần)

**Kết quả verify UI hiện tại**

- Verify ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw` / CB Nghiệp vụ - Trung ương (BTP·TW).
- Mở form Sửa `/bieu-mau/28104008-7b0d-4783-9825-a188ad11a289/sua` của BM-20260715-001 (có file 943 B).
- Vùng "File biểu mẫu" chỉ có ô tải trống "Kéo thả hoặc click để chọn file"; `evaluate_script`: `uploadListItemCount = 0`, không có tên file, không có link tải file cũ (`hasDownloadLinkInForm = false`). Khớp phản ánh đối tác (frame `QLBMHD_13.webm` t08.08s).
- Evidence: `../../reverify-audit/QLBMHD_13/QLBMHD_13-edit-form-no-file.png` + `../../reverify-audit/QLBMHD_13/dom-evidence-edit-form.md` + `../../reverify-audit/QLBMHD_13/frames/t008.08s.jpg`.
- **Chưa test được** hành vi bấm "Lưu" khi không upload lại file (env session TTL ngắn) — chưa biết file cũ được giữ hay bị chặn/mất.

**Kết luận QA**

- `QLBMHD_13` tái hiện đúng phần hiển thị (form Sửa không thể hiện file hiện có), nhưng SRS không quy định minh thị việc này; mẫu "ô tải trống = giữ file cũ" là pattern hợp lệ.
- Chưa đủ căn cứ Open (chưa chứng minh vi phạm clause SRS / functional break).

**Nội dung đề xuất BA phản hồi đối tác**

- Câu hỏi BA: form Chỉnh sửa có bắt buộc hiển thị tên/file đang đính kèm để người dùng biết + giữ lại không?
  + Nếu CÓ (hoặc nếu Lưu-không-upload bị chặn / mất file) → là lỗi, owner Dev FE (hiển thị file hiện tại trong form).
  + Nếu KHÔNG → cập nhật lại expected testcase; web hiện tại chấp nhận được.
- Verdict QA đề xuất: `Cần BA xác nhận` — chưa gửi Dev tới khi BA chốt (hoặc tới khi test được hành vi Lưu).

---
