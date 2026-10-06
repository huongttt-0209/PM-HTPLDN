# BA confirmation needed — TVCS Batch F (Quản lý tư liệu pháp lý của vụ việc, QLTLPLCVV / FR-X.1-06 / UC152) — 2026-07-21

> **File này để làm gì:** gom testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng thay bug-report (bug có SRS reference rõ → `bug-report-tvcs-batchF.md`).

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE` — SRS v3.5 `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md`.

---

## QLTLPLCVV_15 — Upload file mã độc: không tái hiện được message vì bước Quét virus chưa chặn file mã độc mẫu (EICAR)

**Bối cảnh testcase**

- Dòng Excel: **300**, mã TC `QLTLPLCVV_15`.
- Nội dung kiểm tra: CB Nghiệp vụ upload một tệp **chứa mã độc** vào tư liệu pháp lý của vụ việc (widget "File đính kèm").
- Expected trong file UAT (đối tác):
  - Khi upload tệp chứa mã độc, hệ thống chặn và báo thông báo chuẩn "File '{tên}' chứa mã độc".
- Actual đối tác ghi: hệ thống báo **"Tải file thất bại"** (thông báo chung chung, không phải message chuẩn).

**Đối chiếu SRS v3.5**

- Quy trình "Tải lên file" có bước **"Quét virus"** trước khi lưu file.
- Error Handling định nghĩa mã lỗi **ERR-TLPL-04**: khi file chứa mã độc → báo *"File '{ten_file}' chứa mã độc"* (mức ERROR).
- Tức SRS yêu cầu: (1) có bước quét virus; (2) nếu phát hiện mã độc → chặn + báo message chuẩn ERR-TLPL-04.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:858` (Processing "Tải lên file" — bước "Quét virus")
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:955` (Error Handling E4 — ERR-TLPL-04 "File '{ten_file}' chứa mã độc")

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Dùng tệp test **EICAR chuẩn** (chuỗi 68 byte mà mọi phần mềm diệt virus được thiết kế để phát hiện; hoàn toàn vô hại, dùng đúng mục đích kiểm thử AV):
  - Biến thể chuỗi EICAR thô đặt đuôi `.pdf` → bị chặn ở **cổng kiểm tra định dạng** ("Nội dung file không khớp định dạng", HTTP 400) — chặn vì định dạng, KHÔNG phải vì mã độc.
  - Biến thể **PDF hợp lệ nhúng nguyên chuỗi EICAR** (đi qua được cổng định dạng) → **upload THÀNH CÔNG**: `POST /api/v1/tu-lieu-phap-ly-vvs/upload` trả **HTTP 201**, `trangThaiQuet="SACH"` (sạch), không có thông báo lỗi, file hiển thị bình thường.
- ⇒ Trên hệ thống hiện tại, **bước quét virus không phát hiện tệp chứa chữ ký mã độc mẫu**; không đạt được tình huống "tệp bị chặn vì mã độc" nên **không có message để đối chiếu** với "Tải file thất bại" đối tác báo.
- Evidence: `../../reverify-audit/QLTLPLCVV_15/eicar-accepted-modal.png`, `../../cond/QLTLPLCVV_15.md` (kèm log network).

**Kết luận QA**

- `QLTLPLCVV_15`: **không tự chốt được** verdict wording (Open/Reject) vì tình huống mã độc **không tái hiện được** — hệ thống hiện chưa chặn tệp mã độc mẫu, nên chưa hề hiển thị message nào để so với chuẩn ERR-TLPL-04.
- Nghi vấn: tính năng **quét virus chưa được bật/triển khai** trên môi trường này (khớp ghi nhận nội bộ rằng phần virus/mã độc trước đây được hoãn).
- Kèm **phát hiện bảo mật**: tệp chứa chữ ký mã độc chuẩn được hệ thống nhận là "sạch" và cho lưu → nếu quét virus lẽ ra phải hoạt động thì đây là lỗ hổng cần xử lý.

**Câu hỏi cần BA xác nhận**

1. Bước **Quét virus** (SRS dòng 858) có nằm trong **phạm vi bản phát hành hiện tại / được bật trên môi trường này** không, hay đang **được hoãn**?

**Nội dung đề xuất BA phản hồi đối tác (theo nhánh)**

- **Nếu quét virus đang được HOÃN / chưa trong phạm vi:** phản hồi đối tác rằng chức năng quét mã độc chưa được kích hoạt ở giai đoạn này, nên khiếu nại về nội dung thông báo khi chặn mã độc **tạm hoãn đánh giá**; sẽ kiểm thử lại wording (đối chiếu chuẩn "File '{tên}' chứa mã độc") khi tính năng được bật. Verdict QA: `Cần BA xác nhận` (chưa gửi Dev về phần wording).
- **Nếu quét virus PHẢI hoạt động ở bản này:** đây là **lỗ hổng bảo mật** — hệ thống hiện cho phép tải lên tệp chứa chữ ký mã độc mẫu (đánh dấu "sạch"). Ưu tiên chuyển **Dev BE** khắc phục bước quét virus TRƯỚC; phần nội dung thông báo (message chuẩn ERR-TLPL-04) đánh giá lại sau khi tệp mã độc đã bị chặn. Verdict QA: `Cần BA xác nhận` + cảnh báo bảo mật.

---

## QLTLPLCVV_16 — Xóa tệp đính kèm không hiển thị hộp xác nhận (SRS silent về confirm cho xóa file)

**Bối cảnh testcase**

- Dòng Excel: **301**, mã TC `QLTLPLCVV_16`.
- Nội dung kiểm tra: CB Nghiệp vụ mở form "Sửa tư liệu pháp luật" của 1 tư liệu có file đính kèm → bấm nút xóa cạnh 1 file.
- Expected trong file UAT (đối tác):
  - Khi xóa tệp đính kèm, hệ thống **phải hiển thị hộp xác nhận** trước khi xóa.
- Actual đối tác ghi: bấm xóa file → file bị xóa ngay, **không có hộp xác nhận** nào.

**Đối chiếu SRS v3.5**

- Quy trình "Xóa file đính kèm" gồm 6 bước nghiệp vụ (kiểm quyền & phạm vi đơn vị → kiểm file tồn tại và thuộc tư liệu → xóa file khỏi storage → cập nhật danh sách liên kết → cảnh báo CB NV nếu tư liệu đang công khai và không còn file nào → ghi nhật ký). **Trong 6 bước KHÔNG có bước "hiển thị xác nhận".**
- Ngược lại, quy trình "Xóa mềm **tư liệu**" **có** bước hiển thị xác nhận: *"Bạn có chắc chắn muốn xóa tư liệu '{tên}'?"*. Tức là spec CHỦ ĐÍCH phân biệt: xóa **tư liệu** có confirm, xóa **file** thì không mô tả confirm.
- Vì vậy hành vi "xóa file không confirm" mà đối tác quan sát **đang khớp với SRS hiện hành**; kỳ vọng "phải có confirm" của đối tác là thứ SRS **chưa quy định**.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:904` (đầu bảng "Processing — Xóa file đính kèm") → `:913` (bước 6, hết bảng — không có step confirm)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:900` (Processing "Xóa mềm tư liệu" step 4 — CÓ hiển thị xác nhận, để đối chiếu)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Bằng chứng đối tác (video `../../partner-evidence/QLTLPLCVV_16.webm`): frame t002 form "Sửa" hiển thị file cũ `2K15 T5 (16.7) & T7 (18.7).pdf` kèm icon thùng rác; frame t003→t004 sau khi bấm thùng rác, file **biến mất ngay, không có hộp xác nhận** → khớp actual đối tác.
- Trên env verify `18.143.165.120.nip.io`: KHÔNG thao tác lại được đúng bước vì form "Sửa" **không hiển thị file đính kèm cũ** (endpoint chi tiết trả `files: []` dù `soFile: 1` — xem mục Ghi chú anomaly). Evidence: `../../reverify-audit/QLTLPLCVV_16/nipio-edit-form-no-existing-file.png` + `../../cond/QLTLPLCVV_16.md`.
- Đối chiếu: hành vi "không confirm khi xóa file" trên env đối tác **đúng với SRS 904–913**.

**Kết luận QA**

- `QLTLPLCVV_16`: theo SRS v3.5, **không confirm khi xóa file đính kèm là ĐÚNG spec hiện hành** — không phải bug so với SRS.
- Kỳ vọng "phải có hộp xác nhận" của đối tác **chưa được SRS quy định** cho thao tác xóa **file** (chỉ xóa **tư liệu** mới có confirm) → bất đồng về đặc tả, cần BA quyết.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận **có bổ sung bước "hiển thị hộp xác nhận" cho thao tác Xóa file đính kèm hay không**:

- **Nếu GIỮ theo SRS hiện hành:** không cần confirm khi xóa file → cập nhật expected của `QLTLPLCVV_16` cho khớp SRS (chỉ xóa tư liệu mới confirm); phản hồi đối tác đây không phải lỗi.
- **Nếu BỔ SUNG confirm:** cập nhật SRS 904–913 thêm step "hiển thị xác nhận" → chuyển Dev FE bổ sung hộp xác nhận; khi đó UI hiện tại (không confirm) mới là lỗi.
- Verdict QA đề xuất: `Cần BA xác nhận` (chưa gửi Dev cho tới khi BA chốt spec confirm).

---

## Ghi chú anomaly (ngoài phạm vi TC — phát hiện khi verify QLTLPLCVV_16, cần dev/BA)

Trên env verify `18.143.165.120.nip.io`, **form "Sửa tư liệu pháp luật" không hiển thị file đính kèm hiện có** → CB NV không xem/xóa được file cũ qua form Sửa. Đo 2 phương pháp: (1) UI — quét `[role=dialog]` không thấy item file nào; (2) API — `GET /api/v1/tu-lieu-phap-ly-vvs/{id}` trả `files: []` dù `soFile: 1`, cho cả tư liệu NHAP mới tạo lẫn tư liệu CONG_KHAI (chắc chắn có file vì đã công khai — SRS 867). Đề nghị dev xác nhận: endpoint chi tiết có nên trả mảng `files` không, hoặc FE có nạp file qua endpoint khác không (env đối tác `ospgroup.vn` hiển thị được file). *Chưa log bug Open vì chưa loại trừ khả năng khác biệt build/endpoint — chờ dev confirm.*
