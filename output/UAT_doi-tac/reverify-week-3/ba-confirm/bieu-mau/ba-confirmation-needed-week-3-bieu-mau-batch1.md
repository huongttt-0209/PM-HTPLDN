# BA confirmation needed — UAT tuần 3 — Biểu mẫu Batch 1 (QLTMBMHD) — 2026-07-20

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI để BA quyết nhanh. Bug có SRS reference rõ đã log riêng ở `../../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch1.md` (BUG-QLTMBMHD_13 / _19 / _23).

> **Bản SRS dùng để chấm:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md` (FR-VII-01 / SCR-VII-01). Tab đối tác: `UAT_TGPL Doanh Nghiệp-tuần 3`. Mọi citation đã mở file verify số dòng thực (v3.5).

> **4 TC dưới đây đều thuộc Dạng A** (QA đã có kết luận đối chiếu SRS, cần BA phản hồi đối tác) — không có TC nào thuộc dạng SRS tự mâu thuẫn.

---

## QLTMBMHD_08 — Chặn tên >500 ký tự bằng maxlength (im lặng), không hiển thị thông báo ERR-TM-03

**Bối cảnh testcase**

- Dòng Excel: 81, mã TC `QLTMBMHD_08`.
- Nội dung kiểm tra: CB Nghiệp vụ - TW thêm thư mục biểu mẫu với tên vượt quá 500 ký tự.
- Expected trong file UAT:
  - Hệ thống hiển thị thông báo **"Tên thư mục tối đa 500 ký tự"** khi nhập quá giới hạn.
- Actual đối tác ghi: hệ thống chặn nhập quá 500 ký tự nhưng **không hiển thị thông báo** cho người dùng.

**Đối chiếu SRS v3.5**

- SRS định nghĩa thông báo lỗi ERR-TM-03 **"Tên thư mục tối đa 500 ký tự"** cho điều kiện lỗi "Tên vượt 500 ký tự".
- SRS quy định trường Tên thư mục là bắt buộc, tối đa 500 ký tự, unique trong đơn vị — nhưng **KHÔNG quy định cơ chế enforce** (chặn cứng không cho nhập vs cho nhập rồi báo lỗi).
- Vì SRS chỉ mô tả *thông báo phải có khi điều kiện ">500 ký tự" xảy ra*, mà không nói cơ chế, nên cách app chặn ở đúng 500 (điều kiện ">500" không bao giờ xảy ra qua thao tác thường) là một lựa chọn implementation mà SRS không cấm cũng không yêu cầu.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:132` (ERR-TM-03)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:617` (SCR-VII-01 #15 — form Tên thư mục: "Bắt buộc, max 500 ký tự, unique trong đơn vị")

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, dùng tài khoản UAT `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- Ô "Tên thư mục" có thuộc tính `maxlength="500"` → trình duyệt chặn cứng khi gõ/dán vượt 500, **cắt âm thầm ở 500 ký tự, không bộ đếm, không thông báo**.
- App CÓ luật kiểm tra "Tối đa 500 ký tự" nhưng luật chỉ kích hoạt khi value > 500 — mà maxlength không cho value vượt 500 → message **không bao giờ hiển thị qua thao tác bàn phím/paste bình thường** (chỉ thấy khi ép value > 500 bằng script).
- Giới hạn 500 ký tự được enforce đúng (toàn vẹn dữ liệu OK). Điểm tranh luận: có cần hiện thông báo/bộ đếm khi chạm giới hạn hay không.
- Evidence: `../../reverify-audit/QLTMBMHD_08/over500-validation.png` (khi ép value > 500, message "Tối đa 500 ký tự" mới hiện) + `../../reverify-audit/QLTMBMHD_08/measurement.md`.

**Kết luận QA**

- `QLTMBMHD_08`: giới hạn 500 ký tự được enforce đúng nên **không phải lỗi toàn vẹn dữ liệu**; nhưng thông báo ERR-TM-03 **không đến tay người dùng** qua thao tác thường vì cơ chế chặn cứng làm điều kiện ">500" không xảy ra.
- QA **không tự chốt Open/Reject** được: SRS quy định message nhưng không quy định cơ chế enforce → việc chặn cứng im lặng có thỏa ERR-TM-03 hay không là quyết định của BA.
- Kèm điểm phụ: message app hiện tại "Tối đa 500 ký tự" khác chữ SRS "Tên thư mục tối đa 500 ký tự".

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý cho `QLTMBMHD_08`:

- Cơ chế chặn cứng bằng maxlength (im lặng, không bộ đếm/thông báo) có được xem là **thỏa** yêu cầu ERR-TM-03 không?
- Nếu KHÔNG: yêu cầu hiển thị thông báo/bộ đếm khi người dùng chạm giới hạn 500 ký tự (và chuẩn hóa chữ message theo ERR-TM-03).
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev cho tới khi BA chốt cơ chế.

---

## QLTMBMHD_10 — Nút "Sửa" hiển thị trên thư mục Công khai (SRS không giới hạn state cho nút Sửa)

**Bối cảnh testcase**

- Dòng Excel: 82, mã TC `QLTMBMHD_10`.
- Nội dung kiểm tra: CB Nghiệp vụ - TW xem điều kiện hiển thị nút "Sửa" trong cột Hành động.
- Expected trong file UAT:
  - Nút Sửa chỉ hiển thị khi thư mục ở trạng thái **Nháp/Ẩn** và CB NV thuộc đơn vị sở hữu.
- Actual đối tác ghi: hệ thống hiển thị nút chức năng đối với thư mục ở trạng thái **Công khai**.

**Đối chiếu SRS v3.5**

- SCR-VII-01 #13 (Cột Hành động) liệt kê từng nút kèm điều kiện: Công khai *(khi NHAP/AN, có BM)* / Ẩn *(khi CONG_KHAI)* / **Sửa** / Xóa *(khi NHAP/AN, rỗng)*.
- Nút **"Sửa" KHÔNG kèm điều kiện trạng thái** (khác Công khai/Ẩn/Xóa đều có điều kiện rõ) → theo SRS, Sửa hiển thị ở mọi trạng thái, kể cả Công khai.
- App hiển thị Sửa trên thư mục Công khai = **ĐÚNG SRS**; expected của đối tác (Sửa chỉ Nháp/Ẩn) **mâu thuẫn với SRS**.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:615` (SCR-VII-01 #13 — Cột Hành động)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, dùng tài khoản UAT `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- Mở màn `Thư viện biểu mẫu` (`/bieu-mau/thu-muc`), tab Tất cả.
- Nút **Sửa** hiển thị trên hàng "Thư mục biểu mẫu seed" (trạng thái Đã công khai, thuộc BTP·TW) — xác nhận qua evaluate_script + screenshot.
- Tất cả thư mục hiển thị đều thuộc đơn vị người xem (BTP·TW) → yếu tố đơn vị không phải nguyên nhân.
- Evidence: `../../reverify-audit/QLTMBMHD_17/bulk-select-congkhai-nonempty.png` (list chung, hàng "Thư mục biểu mẫu seed" Công khai có nút Sửa) + `../../cond/QLTMBMHD_10.md`.

**Kết luận QA**

- `QLTMBMHD_10`: **không phải bug theo SRS v3.5** — web hiện tại đúng SRS (nút Sửa không giới hạn trạng thái).
- Expected của đối tác sai so với SRS ở điểm:
  - Giới hạn Sửa chỉ Nháp/Ẩn — SRS không đặt điều kiện state cho nút Sửa.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị cập nhật expected của `QLTMBMHD_10` theo SRS v3.5, hoặc xác nhận nếu muốn đổi thiết kế:

- Nếu giữ theo SRS: nút Sửa hiển thị ở mọi trạng thái (kể cả Công khai) là đúng → cập nhật lại expected testcase.
- Nếu muốn Sửa chỉ Nháp/Ẩn: cần bổ sung điều kiện state cho nút Sửa vào SRS rồi mới log Dev.
- Verdict QA đề xuất: `Không phải bug theo SRS / Cần BA xác nhận` (do expected đối tác khác SRS), không gửi Dev cho tới khi BA chốt.

---

## QLTMBMHD_17 — Cho tích chọn thư mục Công khai / còn biểu mẫu để xóa hàng loạt (SRS không hạn chế tích chọn)

**Bối cảnh testcase**

- Dòng Excel: 84, mã TC `QLTMBMHD_17`.
- Nội dung kiểm tra: CB Nghiệp vụ - TW xem điều kiện checkbox chọn hàng loạt + nút "Xóa hàng loạt".
- Expected trong file UAT:
  - Chọn hàng loạt / Xóa hàng loạt chỉ có hiệu lực trên thư mục **Nháp/Ẩn** và **rỗng**.
- Actual đối tác ghi: hệ thống cho phép tích chọn cả thư mục ở trạng thái **Công khai** và thư mục **chứa biểu mẫu**.

**Đối chiếu SRS v3.5**

- SCR-VII-01 #8 (Checkbox "Chọn hàng loạt") có điều kiện hiển thị **"luôn hiển thị"** — không nêu hạn chế tích chọn theo state/rỗng.
- SCR-VII-01 #14 (Hành động hàng loạt [Xóa hàng loạt]) có điều kiện **"khi chọn nhiều"** — không nêu điều kiện eligibility cho việc tích chọn.
- Kỳ vọng của chính đối tác ở case liền kề `QLTMBMHD_20` ("Đã xóa {X} thư mục. {Y} thư mục không đủ điều kiện xóa (còn biểu mẫu)") cho thấy thiết kế là **chọn bất kỳ → validate khi xóa** (select-then-validate) → cho tích chọn thư mục ineligible không hẳn là lỗi.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:610` (SCR-VII-01 #8 — Checkbox "Chọn hàng loạt": "luôn hiển thị")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:616` (SCR-VII-01 #14 — Hành động hàng loạt: "khi chọn nhiều")

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, dùng tài khoản UAT `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- Mở màn `Thư viện biểu mẫu`, checkbox bật (`disabled=false`) trên MỌI hàng, kể cả thư mục Công khai / còn biểu mẫu.
- Tích 2 thư mục ineligible (Công khai + còn biểu mẫu) → thanh "Đã chọn 2 thư mục" hiện + nút **"Xóa hàng loạt" enabled** (`disabled=false`).
- ⚠️ Việc bulk delete có XÓA NHẦM thư mục ineligible hay không đã verify riêng ở `QLTMBMHD_20`: app chỉ xóa thư mục đủ điều kiện, thư mục còn biểu mẫu **còn nguyên** (không xóa nhầm) — nên đây thuần là câu hỏi UX tích chọn, không phải lỗi mất dữ liệu.
- Evidence: `../../reverify-audit/QLTMBMHD_17/bulk-select-congkhai-nonempty.png` + `../../cond/QLTMBMHD_17.md`.

**Kết luận QA**

- `QLTMBMHD_17`: **không phải bug toàn vẹn dữ liệu** — SRS không quy định hạn chế tích chọn theo state/rỗng, và app validate đúng khi thực xóa (không xóa nhầm).
- QA không tự chốt: chặn tích chọn ineligible từ đầu (disable checkbox) hay cho chọn rồi validate khi xóa (select-then-validate) là quyết định UX của BA.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng UX cho `QLTMBMHD_17`:

- UX mong muốn là **chặn tích chọn** thư mục không đủ điều kiện ngay từ đầu (disable checkbox), hay **cho chọn rồi validate khi xóa** (giữ hành vi hiện tại, đã báo phần bị bỏ qua ở modal xác nhận)?
- Nếu chọn hướng disable checkbox: cần bổ sung điều kiện eligibility cho checkbox vào SRS rồi log Dev.
- Verdict QA đề xuất: `Cần BA xác nhận`, không gửi Dev cho tới khi BA chốt hướng UX.

---

## QLTMBMHD_20 — Wording/thời điểm thông báo khi xóa hàng loạt MỘT PHẦN (phần bị bỏ qua báo ở modal xác nhận thay vì toast thành công)

> ⚠️ Case `QLTMBMHD_20` có **2 phần**. Phần "sau khi xóa vẫn hiển thị dòng đã chọn + nút hành động hàng loạt" đã kết luận **Open** và log ở `../../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch1.md` (BUG-QLTMBMHD_19). Mục dưới đây **chỉ** là điểm wording thông báo cần BA chốt.

**Bối cảnh testcase**

- Dòng Excel: 86, mã TC `QLTMBMHD_20`.
- Nội dung kiểm tra: CB Nghiệp vụ - TW xóa hàng loạt khi chọn cả thư mục đủ điều kiện và không đủ điều kiện.
- Expected trong file UAT:
  - Một thông báo thành công dạng **"Đã xóa {X} thư mục. {Y} thư mục không đủ điều kiện xóa (còn biểu mẫu)"**.
- Actual đối tác ghi: thông báo "sai thiết kế".

**Đối chiếu SRS v3.5**

- SRS ERR-TM-02 **"Thư mục chứa {N} biểu mẫu, không thể xóa"** định nghĩa thông báo cho hành động xóa đơn không hợp lệ.
- SRS **KHÔNG quy định mẫu thông báo cho xóa hàng loạt MỘT PHẦN** (kết hợp đã-xóa + bị-bỏ-qua) → không có source truth để khẳng định wording nào đúng.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:131` (ERR-TM-02)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, dùng tài khoản UAT `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- Tích 1 thư mục eligible (Nháp rỗng) + 1 ineligible (còn biểu mẫu) → "Xóa hàng loạt".
- **Modal xác nhận** hiện TRƯỚC khi xóa: "Xóa 1 thư mục? ... **(1 thư mục đang chứa biểu mẫu sẽ được bỏ qua)**" → app CÓ thông báo phần bị bỏ qua, tại bước xác nhận.
- **Toast thành công** (đo `tools/toast-capture.js`): `SO_KHUNG_THONG_BAO=1`, "Đã xóa 1 thư mục.", `BI_LAP=false` → chỉ báo số đã xóa, không nhắc lại phần bị bỏ qua.
- App xử lý đúng: chỉ xóa thư mục eligible (`SO_REQUEST=1` DELETE), thư mục ineligible "QA Hidden Folder 715" còn nguyên (không xóa nhầm).
- Evidence: `../../reverify-audit/QLTMBMHD_20/post-partial-delete-selection-not-cleared.png` + `../../cond/QLTMBMHD_20.md`.

**Kết luận QA**

- `QLTMBMHD_20` (phần wording): app **có** thông báo phần bị bỏ qua, nhưng đặt ở **modal xác nhận (trước khi xóa)** thay vì gộp vào toast thành công như đối tác kỳ vọng.
- QA không tự chốt: SRS không có mẫu thông báo cho xóa hàng loạt một phần → không có cơ sở khẳng định app sai hay đối tác sai.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý cho `QLTMBMHD_20` (phần wording):

- Thông báo phần "không đủ điều kiện" ở **modal xác nhận (trước xóa)** có được xem là thỏa yêu cầu không, hay **bắt buộc nhắc lại** trong toast thành công sau xóa theo mẫu đối tác đề xuất?
- Nếu bắt buộc gộp vào toast thành công: chuẩn hóa mẫu thông báo rồi log Dev.
- Verdict QA đề xuất: `Cần BA xác nhận` (phần wording). Lưu ý phần "sau xóa vẫn hiển thị dòng đã chọn + nút" đã là bug Open riêng — owner: `Dev FE` (BUG-QLTMBMHD_19).
