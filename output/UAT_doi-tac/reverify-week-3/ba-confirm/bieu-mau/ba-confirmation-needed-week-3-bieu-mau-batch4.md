# BA confirmation needed — UAT tuần 3 — Biểu mẫu Batch 4 (QLBMHD tạo mới + upload/validation) — 2026-07-20

> **File này để làm gì:** gom các testcase/điểm QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI. Bug có SRS reference rõ đã log riêng ở `../../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch4.md`.

> **Bản SRS dùng để chấm:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md` (FR-VII-04 / UC95 / SCR-VII-02). Tab đối tác: `UAT_TGPL Doanh Nghiệp-tuần 3`. Mọi citation đã mở file verify số dòng thực (v3.5).

---

## QLBMHD_02 (điểm phụ) — "Ô chọn biểu mẫu" (checkbox chọn dòng) có cần bổ sung không

> **Ghi chú:** Verdict tổng của QLBMHD_02 là `Open` (thiếu cột Cơ quan ban hành — đã log BUG-QLBMHD_02). Riêng ý "thiếu ô chọn biểu mẫu" trong phản ánh của đối tác thuộc dạng SRS im lặng → tách ra đây.

**Bối cảnh testcase**

- Dòng Excel: 97, mã TC `QLBMHD_02`.
- Nội dung kiểm tra: CB Nghiệp vụ xem danh sách biểu mẫu (`/bieu-mau/danh-sach`).
- Expected trong file UAT: đối tác phản ánh **thiếu "ô chọn biểu mẫu"** (hiểu là checkbox chọn dòng để thao tác hàng loạt) + thiếu cột Cơ quan ban hành, Định dạng.

**Đối chiếu SRS v3.5**

- SCR-VII-02 (Quản lý Biểu mẫu) mô tả thành phần màn hình danh sách + form. **KHÔNG có** thành phần "checkbox chọn dòng" / "chọn hàng loạt biểu mẫu".
- Thao tác hàng loạt trong Nhóm VII chỉ xuất hiện ở màn **Thư mục** (SCR-VII-01: công khai/ẩn/xóa hàng loạt thư mục) và wizard **Nhập hàng loạt biểu mẫu** (SCR-VII-03), không có "chọn nhiều biểu mẫu để thao tác" trên màn danh sách biểu mẫu.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:634` (SCR-VII-02 §Thành phần màn hình — danh sách 11 thành phần, không có checkbox chọn dòng)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:662` (SCR-VII-03 — thao tác hàng loạt qua wizard Nhập biểu mẫu)

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- DOM `table thead` **không có** cột checkbox chọn dòng (`.ant-checkbox`). Danh sách chỉ có nút hành động per-row (Tải về / Sửa / Xóa).
- Bộ lọc "Định dạng" đã có; cột "Cơ quan ban hành" thiếu (đã log Open riêng).
- Evidence: `bug-reports/image/BUG-QLBMHD_02-danhsach-cot.png`.

**Kết luận QA**

- Ý "thiếu ô chọn biểu mẫu": SRS **không quy định** chức năng chọn hàng loạt biểu mẫu trên màn danh sách → QA không tự chốt Open/Reject.

**Nội dung đề xuất BA phản hồi đối tác**

- Đề nghị BA xác nhận: màn Danh sách biểu mẫu có **cần** thêm checkbox chọn dòng để thao tác hàng loạt (công khai/ẩn/xóa nhiều biểu mẫu) hay không — SRS hiện chưa quy định.
- Verdict QA đề xuất cho ý này: `Cần BA xác nhận`. (Ý chính "thiếu cột Cơ quan ban hành" đã là Open → gửi Dev.)

---

## QLBMHD_06 (dòng 99) — Thông báo upload file >20MB: wording khác chuỗi mẫu ERR-BM-02

**Bối cảnh testcase**

- Dòng Excel: 99, mã TC `QLBMHD_06`.
- Nội dung kiểm tra: upload file biểu mẫu vượt 20MB → hệ thống báo lỗi.
- Đối tác quan sát: web hiện toast **"File vượt quá 20MB (24.7 MB)"** khi upload file 24.7MB.

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`, form Thêm biểu mẫu, file `big-21mb.docx` (~21.0MB).
- Đo bằng observer (`toast-capture.js`): toast **"File vượt quá 20MB (21.0 MB)"**, 1 khung, **0 request ghi** (FE chặn client-side, file không đính kèm). → Tái hiện đúng như đối tác báo.
- Evidence: `../../reverify-audit/QLBMHD_06/toast-capture.md`.

**Đối chiếu SRS v3.5**

- ERR-BM-02 (`srs-fr-09:343`): "**File vượt quá giới hạn 20MB. Kích thước: {size}MB**".
- Web: "File vượt quá 20MB ({size} MB)".
- **Cùng nội dung nghiệp vụ** (chặn file >20MB + hiển thị kích thước thực). Khác **cách diễn đạt**: bỏ chữ "giới hạn"; format "(21.0 MB)" thay vì ". Kích thước: 21.0MB".

**Kết luận QA**

- Yêu cầu nghiệp vụ ERR-BM-02 (chặn file >20MB + báo kích thước) **đã được đáp ứng**. Chỉ khác wording so với chuỗi mẫu SRS. Theo "describe don't prescribe", QA không tự Open cũng không Reject.

**Nội dung đề xuất BA phản hồi đối tác**

- Đề nghị BA xác nhận: chuỗi thông báo ERR-BM-02 trong SRS là **văn bản bắt buộc đúng nguyên văn** hay chỉ là **mô tả yêu cầu** (báo vượt 20MB + kích thước). Nếu chỉ mô tả yêu cầu → wording hiện tại của web đạt, đề nghị đối tác không tính lỗi.
- Verdict QA đề xuất: `BA confirm`.

---

## QLBMHD_07 (dòng 100) — Thông báo upload tệp hỏng: wording khác chuỗi ERR-BM-04

**Bối cảnh testcase**

- Dòng Excel: 100, mã TC `QLBMHD_07`. Nội dung: upload tệp hỏng → hệ thống báo lỗi.
- Đối tác quan sát (env `htpldn-uat.ospgroup.vn`): toast generic **"Upload file thất bại. Vui lòng thử lại."** (không nêu file hỏng).

**Kết quả verify UI hiện tại**

- Verify 20/07/2026, `cbnv_tw`, form Thêm biểu mẫu, file `corrupt.docx` (bytes rác đuôi .docx).
- Đo bằng observer: toast **"Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng loại đã chọn."** (1 request POST upload, file không đính kèm) → app chặn + báo cụ thể. Lỗi generic đối tác báo KHÔNG tái hiện.
- Evidence: `../../reverify-audit/QLBMHD_07/toast-capture.md`.

**Đối chiếu SRS v3.5**

- ERR-BM-04 (`srs-fr-09:345`): "File không hợp lệ hoặc bị hỏng". ERR-BM-01 (`srs-fr-09:342`): "Chỉ chấp nhận file doc, docx, xls, xlsx".
- Web truyền tải đúng ý (file không hợp lệ / nội dung không khớp định dạng), cụ thể + hướng dẫn hơn, khác **cách diễn đạt**.

**Kết luận QA + đề xuất BA phản hồi**

- Yêu cầu nghiệp vụ (chặn file hỏng + báo lỗi rõ) đã đạt; chỉ khác wording so chuỗi mẫu ERR-BM-04.
- Đề nghị BA xác nhận chuỗi ERR-BM-04 là bắt buộc đúng nguyên văn hay chỉ mô tả yêu cầu. Verdict QA đề xuất: `BA confirm`.

---

## QLBMHD_08 (dòng 101) — 🔴 Không quét virus file đính kèm (rủi ro bảo mật) — cần BA + Dev/Security xác nhận

> **Lưu ý mức độ:** Đây là **rủi ro bảo mật thật**, KHÔNG phải câu hỏi wording. Đưa vào file BA confirm vì chưa quan sát được server-side để khẳng định chắc nguyên nhân — cần BA route sang Dev/Security xác nhận pipeline quét virus, KHÔNG nên coi là câu hỏi UX thường.

**Bối cảnh testcase**

- Dòng Excel: 101, mã TC `QLBMHD_08`. Nội dung: upload tệp có mã độc → hệ thống báo lỗi.
- Đối tác quan sát (env `htpldn-uat.ospgroup.vn`): toast generic "Upload file thất bại. Vui lòng thử lại.".

**Kết quả verify UI hiện tại**

- Verify 20/07/2026, `cbnv_tw`, form Thêm biểu mẫu. Dùng chuẩn test AV **EICAR** (file test antivirus chuẩn công nghiệp, vô hại).
- Bước 1 — `eicar.docx` (EICAR bytes thô đuôi .docx): bị chặn ở bước kiểm **định dạng** ("Nội dung file không khớp định dạng...") → chưa tới bước quét mã độc.
- Bước 2 — `valid-eicar.docx` (docx OOXML **HỢP LỆ** chèn EICAR vào `word/document.xml`): `POST /api/v1/bieu-maus/upload` **HTTP 201**, 0 toast, file đính kèm "done"; submit "Thêm mới" → tạo biểu mẫu **THÀNH CÔNG**, 0 chặn / 0 ERR-BM-07.
- Evidence: `../../reverify-audit/QLBMHD_08/toast-capture.md` + `../../reverify-audit/QLBMHD_08/eicar-accepted-list.png`.

**Đối chiếu SRS v3.5**

- SRS bắt buộc quét virus 3 nơi: `srs-fr-09:314` ("Quét virus file đính kèm"), `:382` (EC-02 "Quét antivirus **TRƯỚC lưu trữ** → **ERR-BM-07** nếu phát hiện mã độc"), `:652` (Inputs #15 "Quét virus").
- Thực tế: file `.docx` hợp lệ chứa chuỗi test mã độc chuẩn EICAR được **chấp nhận + lưu (201) + tạo biểu mẫu** → không có bước quét/chặn.

**Rủi ro**

- File mã độc có thể được lưu và **công khai lên Cổng PLQG** (biểu mẫu công khai) → phát tán tới người dùng ngoài.

**Caveat (ghi trung thực)**

- EICAR nằm trong ZIP `.docx` (`document.xml`); nếu bộ quét không giải nén archive thì có thể bỏ sót. Không quan sát được server-side để biết "không có AV" hay "AV không quét trong archive".

**Nội dung đề xuất BA phản hồi + hành động**

- Đề nghị BA route sang **Dev/Security** xác nhận: (1) AV có chạy **trước lưu trữ** không; (2) có quét nội dung **bên trong archive `.docx`** không.
- Nếu AV không chạy / không quét trong archive → nâng thành bug bảo mật (Major/Critical, chặn file mã độc trước lưu trữ theo ERR-BM-07). Verdict QA đề xuất: `BA confirm` (chờ Dev/Security xác nhận pipeline).

---

## QLBMHD_09 (dòng 102) — Thông báo tải tệp gián đoạn: wording khác ERR-BM-06 + chưa kiểm được ngắt-giữa-chừng

**Bối cảnh testcase**

- Dòng Excel: 102, mã TC `QLBMHD_09`. Nội dung: upload bị gián đoạn (mất mạng) → hệ thống báo lỗi.
- Đối tác quan sát (env `htpldn-uat.ospgroup.vn`, video `QLBMHD_09.webm`): toast generic "Upload file thất bại. Vui lòng thử lại.".

**Kết quả verify UI hiện tại**

- Verify 20/07/2026, `cbnv_tw`, form Thêm biểu mẫu; mô phỏng mất mạng bằng Chrome DevTools `emulate Offline` → upload.
- Kết quả: toast **"Không kết nối được máy chủ."**, upload item trạng thái lỗi, file không đính kèm → app có xử lý + báo lỗi khi upload không tới được server.
- Evidence: `../../reverify-audit/QLBMHD_09/toast-capture.md`.

**Đối chiếu SRS v3.5**

- EC-01 (`srs-fr-09:381`): "Upload bị ngắt giữa chừng (mất mạng) → Dọn blob mồ côi → **ERR-BM-06** 'Upload bị gián đoạn, vui lòng thử lại'".
- Web: "Không kết nối được máy chủ." — truyền tải đúng ý (không kết nối được / mất mạng), khác **cách diễn đạt**.
- Caveat: mình test Offline TRƯỚC upload (chưa phải ngắt-giữa-chừng khi đã lên 1 phần); vế "dọn blob mồ côi" không kiểm được ở tầng UI.

**Kết luận QA + đề xuất BA phản hồi**

- App báo lỗi kết nối khi upload mất mạng (nghiệp vụ đạt), wording khác ERR-BM-06 + còn phần chưa kiểm (ngắt-giữa-chừng + dọn blob).
- Đề nghị BA xác nhận wording ERR-BM-06 + Dev xác nhận xử lý ngắt-giữa-chừng + dọn blob mồ côi. Verdict QA đề xuất: `BA confirm`.

---

