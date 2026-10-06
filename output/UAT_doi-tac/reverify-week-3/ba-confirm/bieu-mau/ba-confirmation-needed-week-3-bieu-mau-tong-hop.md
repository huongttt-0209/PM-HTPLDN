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
# BA confirmation needed — Biểu mẫu Batch 2 (Tìm kiếm thư mục & biểu mẫu) — 2026-07-20

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report (bug có SRS reference rõ → log vào `Pass-bug-report-bieu-mau-batch2.md`).

> **Phạm vi:** tab đối tác `UAT_TGPL Doanh Nghiệp-tuần 3`, sub-module TKTMBMHD (FR-VII-02/UC93) + TKBMHD (FR-VII-05/UC96). Verify env `https://18.143.165.120.nip.io`, login `cbnv_tw` (CB_NV_TW) / Test@1234, tool Chrome DevTools MCP.
>
> **SRS chấm:** `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md` (v3.5). Mọi citation dưới đây đã mở file verify số dòng thực.

---

## TKTMBMHD_04 (row 89) — Giá trị mặc định bộ lọc Danh sách chọn: "Tất cả" hay rỗng?

> **Dạng B — SRS tự mâu thuẫn, cần BA chốt source truth.**

**Bối cảnh testcase**

- Dòng Excel: 89, mã TC `TKTMBMHD_04`.
- Nội dung kiểm tra: CB Nghiệp vụ (CB_NV_TW) kiểm giá trị mặc định các trường Danh sách chọn của bộ lọc màn "Thư viện biểu mẫu → Thư mục" (SCR-VII-01).
- Expected trong file UAT: giá trị mặc định của các trường kiểu Danh sách chọn là **"Tất cả"**.
- Actual đối tác ghi: giá trị mặc định là **rỗng**.

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/bieu-mau/thu-muc`.
- Bộ lọc **Lĩnh vực**: chỉ hiện placeholder "Lĩnh vực"; danh sách chọn = `[Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư]` — **không có mục "Tất cả"**, không chọn sẵn.
- Bộ lọc **Trạng thái**: placeholder "Trạng thái"; danh sách chọn = `[Nháp, Đã công khai, Đã ẩn]` — **không có mục "Tất cả"**.
- Cơ chế app: placeholder rỗng = không áp bộ lọc = hiển thị toàn bộ (tab "Tất cả 4", list đủ record). → Web khớp §Inputs (default "—") nhưng lệch §Thành phần màn hình (default "Tất cả").
- Evidence: `../../reverify-audit/TKTMBMHD_04/web-default-filters.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **SCR-VII-01 §Thành phần màn hình**, bộ lọc để mặc định "Tất cả":
   - #4 Lọc lĩnh vực: "Mặc định: 'Tất cả'".
   - #5 Lọc trạng thái: liệt kê "Tất cả / NHAP / CONG_KHAI / AN" ("Tất cả" là option đầu).

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:606`
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:607`

2. Nhưng **FR-VII-02 §Inputs** lại đặt mặc định "—" (rỗng):
   - `linh_vuc_id`: Mặc định "—".
   - `trang_thai`: Mặc định "—".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:163`
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:166`

**Câu hỏi cần BA xác nhận**

Bộ lọc Danh sách chọn (Lĩnh vực, Trạng thái) trên màn tìm kiếm thư mục cần hiểu theo hướng nào?

1. **Hướng 1 — theo §Thành phần màn hình (SCR-VII-01:606–607):** thêm mục "Tất cả" vào danh sách chọn và đặt sẵn làm mặc định.
2. **Hướng 2 — theo §Inputs (FR-VII-02:163/166):** để mặc định rỗng (placeholder = không lọc) như hiện tại.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict `TKTMBMHD_04`: `Cần BA xác nhận`.
- Nếu BA chọn hướng 1: UI hiện tại `Vẫn lỗi`, owner dự kiến `Dev FE` (thêm option "Tất cả" + set default).
- Nếu BA chọn hướng 2: UI hiện tại **không phải lỗi** (đang đúng §Inputs); cập nhật lại expected testcase cho khớp SRS.
- Đồng bộ tiền lệ tuần 3 `LKHDG_03` (batch A) — cùng vấn đề placeholder vs mục "Tất cả".

---

## TKTMBMHD_07 (row 91) — Nút "Xóa bộ lọc" không đưa tab phân loại về "Tất cả"

> **Dạng A — QA đã kết luận (SRS không quy định), cần BA phản hồi đối tác.**

**Bối cảnh testcase**

- Dòng Excel: 91, mã TC `TKTMBMHD_07`.
- Nội dung kiểm tra: CB Nghiệp vụ (CB_NV_TW) bấm nút "Xóa bộ lọc" trên màn "Thư viện biểu mẫu → Thư mục" (SCR-VII-01).
- Expected trong file UAT:
  - Xoá toàn bộ giá trị đã nhập tại điều kiện tìm kiếm và bộ lọc (Tìm kiếm, Lọc lĩnh vực, Lọc trạng thái, Khoảng ngày tạo).
  - Đưa tab phân loại về "Tất cả".
  - Hiển thị lại danh sách mặc định (toàn bộ thư mục trong phạm vi phân quyền, sắp xếp ngày tạo giảm dần).
- Actual đối tác ghi: không đưa về tab "Tất cả".

**Đối chiếu SRS v3.5**

- FR-VII-02 (UC93) và SCR-VII-01 §Thành phần màn hình **không mô tả nút "Xóa bộ lọc"**; không có clause nào quy định nút này phải reset tab phân loại về "Tất cả".
- Thanh lọc (SCR-VII-01 #3–6) gồm ô tìm kiếm / lọc lĩnh vực / lọc trạng thái / khoảng ngày; tab phân loại (#7) là control riêng ở vùng content — SRS không ràng buộc quan hệ giữa nút "Xóa bộ lọc" và tab.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:605` (thanh lọc: ô tìm kiếm)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:609` (tab phân loại: Tất cả / Đã công khai / Nháp / Đã ẩn)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Tiền đề: đang ở tab "Nháp" + có từ khóa `zzzqa123` trong ô tìm kiếm (URL `.../bieu-mau/thu-muc?tab=NHAP&keyword=zzzqa123`).
- Bấm **Xóa bộ lọc** → URL đổi thành `.../bieu-mau/thu-muc?tab=NHAP`: từ khóa + bộ lọc bị xoá, **nhưng tab vẫn là "Nháp"** (không về "Tất cả"); danh sách vẫn lọc theo tab Nháp (3 thư mục), không hiển thị lại toàn bộ.
- Evidence: `../../reverify-audit/TKTMBMHD_07/web-after-xoa-boloc.png`

**Kết luận QA**

- `TKTMBMHD_07` **không vi phạm clause SRS nào** — SRS im lặng về hành vi "Xóa bộ lọc" ↔ tab phân loại. Web xoá đúng các trường trong thanh lọc.
- Điểm khác biệt: đối tác kỳ vọng nút cũng reset tab về "Tất cả" — đây là kỳ vọng UX **vượt ngoài đặc tả** hiện có, không phải lỗi tái hiện được clause nào.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý cho `TKTMBMHD_07`:

- Nếu chuẩn hoá "Xóa bộ lọc" = đưa về trạng thái mặc định hoàn toàn → **bổ sung yêu cầu**: nút reset cả tab phân loại về "Tất cả" + hiển thị lại danh sách mặc định.
- Nếu giữ nguyên (nút chỉ xoá các trường trong thanh lọc, tab do người dùng chủ động đổi) → cập nhật expected testcase cho khớp hành vi.
- Verdict QA đề xuất: `Cần BA xác nhận`; **không gửi Dev** cho tới khi BA chốt (nếu BA đồng ý bổ sung thì owner `Dev FE`).

---

## TKBMHD_03 (row 113) — Bộ lọc màn Danh sách biểu mẫu: mặc định "Tất cả" + Định dạng có "PDF"

> **Dạng B — SRS tự mâu thuẫn / im lặng, cần BA chốt source truth.**

**Bối cảnh testcase**

- Dòng Excel: 113, mã TC `TKBMHD_03`.
- Nội dung kiểm tra: CB Nghiệp vụ (CB_NV_TW) kiểm điều kiện tìm kiếm / bộ lọc màn "Biểu mẫu → Danh sách biểu mẫu" (SCR-VII-02). Đối tác nêu 2 ý.
- Expected trong file UAT: các trường thông tin hiển thị giống thiết kế, đúng định dạng.
- Actual đối tác ghi: (1) các trường Danh sách chọn giá trị mặc định **không phải "Tất cả"**; (2) trường Định dạng **thừa giá trị "PDF"**.

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/bieu-mau/danh-sach`.
- (1) 4 bộ lọc Danh sách chọn (Thư mục, Lĩnh vực, Loại hình, Định dạng) đều chỉ hiện placeholder, **không có mục "Tất cả"**, không chọn sẵn — placeholder = không lọc.
- (2) Dropdown **Định dạng** = `[DOC, DOCX, XLS, XLSX, PDF]` — **có "PDF"**.
- Evidence: `../../reverify-audit/TKBMHD_03/web-dinhdang-pdf.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Về **giá trị mặc định "Tất cả"**:
   - FR-VII-05 §Inputs (keyword, linh_vuc_id, loai_hinh, thu_muc_id) đều "Mặc định —" (rỗng); SCR-VII-02 §Thành phần chỉ ghi "select | Các bộ lọc", **không** nêu default "Tất cả".
   - Nhưng màn chị em SCR-VII-01 (tìm kiếm thư mục) lại quy định lọc lĩnh vực "Mặc định: 'Tất cả'" → 2 màn cùng chức năng lệch chuẩn.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:400` (FR-VII-05 §Inputs linh_vuc_id, Mặc định "—")
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:640` (SCR-VII-02: "các bộ lọc", không nêu default)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:606` (SCR-VII-01 lọc lĩnh vực "Mặc định: Tất cả")

2. Về **giá trị "PDF" trong bộ lọc Định dạng**:
   - File biểu mẫu (chính) chỉ nhận **doc/docx/xls/xlsx** → biểu mẫu không thể có định dạng PDF → lọc PDF luôn 0 kết quả.
   - Nhưng **file đính kèm công khai** trong cùng module lại cho phép **PDF**/DOC/DOCX/XLS/XLSX → "PDF" là định dạng hợp lệ ở một phần của module.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:50` (module: file chấp nhận doc/docx/xls/xlsx)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:652` (form File đính kèm: doc/docx/xls/xlsx)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:779` (file_dinh_kem_cong_khai: PDF/DOC/DOCX/XLS/XLSX)

**Câu hỏi cần BA xác nhận**

Bộ lọc màn Danh sách biểu mẫu cần hiểu theo hướng nào?

1. **Giá trị mặc định:** thêm mục "Tất cả" + chọn sẵn (đồng bộ SCR-VII-01) hay giữ placeholder rỗng (đồng bộ §Inputs FR-VII-05)?
2. **Trường Định dạng:** lọc theo **định dạng file biểu mẫu chính** (chỉ doc/docx/xls/xlsx → **bỏ "PDF"**) hay bao gồm cả **định dạng file đính kèm công khai** (**giữ "PDF"**)?

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict `TKBMHD_03`: `Cần BA xác nhận`.
- Nếu BA: default phải "Tất cả" → UI `Vẫn lỗi`, owner `Dev FE` (thêm option + set default). Nếu giữ placeholder → cập nhật expected testcase.
- Nếu BA: bỏ "PDF" → UI `Vẫn lỗi`, owner `Dev FE` (loại PDF khỏi dropdown Định dạng). Nếu giữ "PDF" (lọc gồm cả file công khai) → **không phải bug**, cập nhật expected testcase.
# BA confirmation needed — Biểu mẫu Batch 3 (CKTMBMHDLCTT) — 2026-07-20

> **File này để làm gì:** gom các testcase Batch 3 mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI. Bug có SRS reference rõ → log ở `../../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch3.md`.

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE` mở file verify số dòng thực. SRS v3.5 (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`).

---

## CKTMBMHDLCTT_08 (row 94) — Message "Công khai X/Y thư mục, Z thất bại" khi công khai hàng loạt một phần

**Bối cảnh testcase**

- Dòng Excel: 94, mã TC `CKTMBMHDLCTT_08`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương công khai hàng loạt nhiều thư mục cùng lúc, trong đó có thư mục đủ điều kiện và thư mục không đủ điều kiện.
- Expected trong file UAT:
  - Hệ thống công khai được các thư mục đủ điều kiện, báo rõ số thư mục không đủ điều kiện, message kiểu *"Đã công khai {X}. {Y} thư mục không đủ điều kiện..."*.
- Actual đối tác ghi: hệ thống báo *"Công khai 0/2 thư mục, 2 thất bại"* — tức thư mục đủ điều kiện cũng bị tính là thất bại, và wording khác thiết kế.

**Đối chiếu SRS v3.5**

- SRS định nghĩa điều kiện công khai 1 thư mục: thư mục tồn tại, không rỗng (có ≥1 biểu mẫu) — `srs-fr-09-bieu-mau.md:220` (FR-VII-03 Preconditions).
- SRS §Error Handling chỉ định nghĩa lỗi công khai **đơn lẻ**: ERR-CK-01 (thư mục rỗng không công khai được) + WRN-CK-01 — `srs-fr-09-bieu-mau.md:250-251`.
- SRS **KHÔNG** định nghĩa message chuẩn cho công khai **hàng loạt một phần** (partial success). Cả wording đối tác mong đợi lẫn wording thực tế của hệ thống đều không có nguồn SRS đối chiếu.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:220`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:250-251`

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB Nghiệp vụ Trung ương (CB_NV_TW).
- Mở URL `https://18.143.165.120.nip.io/bieu-mau/thu-muc`.
- Chọn 2 thư mục công khai hàng loạt: **QA Hidden Folder 715** (Nháp + 1 biểu mẫu = đủ đk) và **BM-B3-0720-Rong-1** (Nháp + 0 biểu mẫu = rỗng).
- Modal xác nhận: *"Công khai 2 thư mục? Các thư mục sẽ được đồng bộ lên Cổng PLQG."*
- Toast kết quả (đo bằng observer, 1 toast không nhân đôi): **"Công khai 1/2 thư mục, 1 thất bại."**
- Network: 1 request `POST /api/v1/thu-muc-bieu-maus/batch-cong-khai`.
- After-state: **thư mục đủ điều kiện (715) → Đã công khai + Đã đồng bộ (THÀNH CÔNG)**; thư mục rỗng → vẫn Nháp (thất bại đúng).
- Evidence: `../../reverify-audit/CKTMBMHDLCTT_08/web-after-batch-congkhai.png` + `../../reverify-audit/CKTMBMHDLCTT_08/observer-result.json`.

**Kết luận QA**

- `CKTMBMHDLCTT_08` gồm 2 sub-issue, chốt riêng:
  - **Sub-issue LOGIC ("0/2 — thư mục đủ đk cũng thất bại"): KHÔNG tái hiện.** Trên env hiện tại, thư mục đủ điều kiện (Nháp + ≥1 biểu mẫu) **được công khai thành công** qua bulk → kết quả "1/2 thư mục, 1 thất bại", không phải "0/2". Đây là hành vi ĐÚNG (thư mục rỗng đáng lẽ phải thất bại). Có thể build cũ của đối tác lỗi đã được fix.
  - **Sub-issue WORDING ("Công khai X/Y thư mục, Z thất bại" khác thiết kế): SRS silent.** SRS không quy định message chuẩn cho công khai hàng loạt một phần → QA không có căn cứ để khẳng định wording hiện tại đúng/sai.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận / phản hồi đối tác:

- Sub-issue logic "0/2": **không tái hiện** trên build hiện tại — thư mục đủ điều kiện công khai được (kết quả "1/2"). Đề nghị đối tác test lại trên build mới nhất; nếu vẫn "0/2" thì cung cấp cấu hình thư mục cụ thể (số biểu mẫu, trạng thái, lĩnh vực) để QA seed lại đúng.
- Sub-issue wording: BA chốt message chuẩn cho công khai hàng loạt một phần (VD *"Đã công khai {X}/{Y} thư mục; {Z} thư mục không đủ điều kiện"* — thay "thất bại" bằng "không đủ điều kiện" để rõ nguyên nhân), rồi cập nhật cả SRS §Error Handling lẫn expected testcase cho khớp.
- Verdict QA đề xuất: `BA confirm` (logic không tái hiện + wording SRS silent), **không gửi Dev** cho tới khi BA chốt message chuẩn.

---

## CKTMBMHDLCTT_10 (row 95) — Selection không tự xóa sau khi ẩn thư mục hàng loạt

**Bối cảnh testcase**

- Dòng Excel: 95, mã TC `CKTMBMHDLCTT_10`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương chọn nhiều thư mục đang công khai → Ẩn hàng loạt, quan sát trạng thái UI sau khi thao tác xong.
- Expected trong file UAT:
  - Sau khi ẩn hàng loạt, các dòng đã tích + thanh nút chức năng hàng loạt phải được xóa/ẩn đi (bỏ chọn tự động).
- Actual đối tác ghi: sau ẩn hàng loạt vẫn hiện dòng đã tích + nút chức năng hàng loạt (thanh "Đã chọn 2 thư mục" còn nguyên).

**Đối chiếu SRS v3.5**

- SCR-VII-01 #14: bar hành động hàng loạt `[Công khai hàng loạt] [Ẩn hàng loạt] [Xóa hàng loạt]` có **điều kiện hiển thị = "khi chọn nhiều"** — chỉ quy định KHI NÀO bar hiện, KHÔNG quy định phải **xóa selection sau khi thao tác hoàn tất**.
- FR-VII-03 (UC94) đặc tả thao tác **đơn thư mục** (`thu_muc_id` số ít); Postconditions chỉ nói về Cổng PLQG PULL + không cần phê duyệt — **KHÔNG có postcondition nào về trạng thái selection/UI**. SRS **KHÔNG có FR riêng cho thao tác bulk** → im lặng về hành vi deselect sau bulk.
- Không có clause SRS (dẫn line rõ) bị vi phạm, và hệ thống KHÔNG chặn luồng hợp lệ (ẩn hàng loạt vẫn thành công). → không đủ căn cứ Open.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:616` (SCR-VII-01 #14 — điều kiện hiển thị bar bulk)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:261-262` (FR-VII-03 Postconditions — không nhắc UI selection)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB Nghiệp vụ Trung ương (CB_NV_TW).
- Mở URL `https://18.143.165.120.nip.io/bieu-mau/thu-muc` (tab "Tất cả").
- Chọn 2 thư mục đang Đã công khai (QA Hidden Folder 715 + Thư mục biểu mẫu seed) → **Ẩn hàng loạt** → xác nhận "Ẩn".
- Toast (đo bằng observer, 1 toast không nhân đôi): **"Đã ẩn 2 thư mục."** — cả 2 → trạng thái AN. 1 request `POST /api/v1/thu-muc-bieu-maus/batch-an`.
- **Sau khi ẩn xong: thanh "Đã chọn 2 thư mục" + [Công khai/Ẩn/Xóa hàng loạt] + [Bỏ chọn] vẫn hiển thị; 2 checkbox vẫn tích (`anyRowChecked=true`).** → TÁI HIỆN đúng lỗi đối tác báo.
- Đối chiếu evidence đối tác: đối tác đứng tab "Đã công khai" nên 2 thư mục vừa ẩn rời khỏi tab, còn thanh "Đã chọn 2 thư mục" trỏ vào selection "bóng ma" (không có dòng nào hiện đang tích trong view). Lỗi cốt lõi giống nhau: selection không reset sau bulk.
- Evidence: `bug-reports/image/BUG-CKTMBMHDLCTT_10-web.png` + `../../reverify-audit/CKTMBMHDLCTT_10/observer-result.json`.

**Kết luận QA**

- `CKTMBMHDLCTT_10` **tái hiện đúng** hành vi đối tác báo (selection không tự xóa sau ẩn hàng loạt) — KHÔNG phải Reject.
- Nhưng đây là bất đồng về ĐẶC TẢ: SRS **im lặng** về việc deselect sau thao tác bulk. Kỳ vọng đối tác (tự bỏ chọn) là chuẩn UX phổ biến nhưng không được SRS quy định → QA không có clause để chốt Open.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA ra quyết định đặc tả:

- Xác nhận hành vi mong muốn sau khi thao tác bulk (công khai/ẩn/xóa) **hoàn tất**: hệ thống có phải **tự bỏ chọn** toàn bộ + ẩn thanh hành động hàng loạt không. Đây là chuẩn UX phổ biến; QA khuyến nghị bổ sung postcondition này vào SRS FR-VII-03 và áp cho cả bulk công khai (case 93) + ẩn (case này) + xóa (BUG-QLTMBMHD_19 Batch 1).
- Lưu ý mức độ: với **xóa** hàng loạt, selection tồn đọng trỏ vào bản ghi đã bị xóa → hệ quả nặng hơn công khai/ẩn (cần ưu tiên fix cụm này trước).
- Verdict QA đề xuất: `BA confirm` (SRS silent về deselect sau bulk), chờ BA bổ sung spec → khi đó chuyển Dev FE xử lý một lần cho cả 3 thao tác bulk.

---

## CKTMBMHDLCTT_07 (row 93) — Selection không tự xóa sau khi công khai thư mục hàng loạt

**Bối cảnh testcase**

- Dòng Excel: 93, mã TC `CKTMBMHDLCTT_07`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương chọn nhiều thư mục đủ điều kiện → Công khai hàng loạt, quan sát trạng thái UI sau khi thao tác xong.
- Expected trong file UAT:
  - Sau khi công khai hàng loạt, các dòng đã tích + thanh nút chức năng hàng loạt phải được xóa/ẩn (bỏ chọn tự động).
- Actual đối tác ghi: sau công khai hàng loạt vẫn hiện dòng đã tích + nút chức năng (thanh "Đã chọn 2 thư mục" còn nguyên).

**Đối chiếu SRS v3.5**

- Giống hệt cơ sở của CKTMBMHDLCTT_10 (case 95): SCR-VII-01 #14 chỉ định điều kiện hiển thị bar bulk = "khi chọn nhiều", KHÔNG quy định xóa selection sau thao tác. FR-VII-03 (UC94) đặc tả đơn thư mục, Postconditions không nhắc UI selection. SRS **im lặng** về deselect sau bulk.
- Không có clause SRS bị vi phạm; hệ thống KHÔNG chặn luồng hợp lệ (công khai hàng loạt thành công cả 2 thư mục đủ điều kiện).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:616` (SCR-VII-01 #14)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:261-262` (FR-VII-03 Postconditions)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB Nghiệp vụ Trung ương (CB_NV_TW).
- Mở URL `https://18.143.165.120.nip.io/bieu-mau/thu-muc` (tab "Tất cả").
- Chọn 2 thư mục đang Đã ẩn có biểu mẫu (QA Hidden Folder 715 = 1 BM, Thư mục biểu mẫu seed = 3 BM) → **Công khai hàng loạt** → xác nhận "Công khai".
- Toast (observer, 1 toast không nhân đôi): **"Đã công khai 2 thư mục."** — cả 2 → CONG_KHAI. 1 request `POST /api/v1/thu-muc-bieu-maus/batch-cong-khai`.
- **Sau khi công khai xong: thanh "Đã chọn 2 thư mục" + [Công khai/Ẩn/Xóa hàng loạt] + [Bỏ chọn] vẫn hiển thị; 2 checkbox vẫn tích (`anyRowChecked=true`).** → TÁI HIỆN đúng lỗi đối tác báo.
- Đối chiếu evidence đối tác: đối tác đứng tab "Đã ẩn" nên 2 thư mục vừa công khai rời khỏi tab, thanh "Đã chọn 2 thư mục" trỏ vào selection "bóng ma". Lỗi cốt lõi giống nhau.
- Evidence: `bug-reports/image/BUG-CKTMBMHDLCTT_07-web.png` + `../../reverify-audit/CKTMBMHDLCTT_07/observer-result.json`.

**Kết luận QA**

- `CKTMBMHDLCTT_07` **tái hiện đúng** hành vi đối tác báo (selection không tự xóa sau công khai hàng loạt) — KHÔNG phải Reject.
- Bất đồng về ĐẶC TẢ: SRS im lặng về deselect sau bulk. → không đủ căn cứ Open.

**Nội dung đề xuất BA phản hồi đối tác**

- Cùng đề xuất với CKTMBMHDLCTT_10: BA xác nhận có bổ sung postcondition "tự bỏ chọn + ẩn thanh hành động hàng loạt sau khi thao tác bulk hoàn tất" vào SRS FR-VII-03 không, áp chung cho cả 3 thao tác bulk (công khai – case này, ẩn – case 95, xóa – BUG-QLTMBMHD_19 Batch 1).
- Verdict QA đề xuất: `BA confirm`, chờ BA bổ sung spec → chuyển Dev FE xử lý một lần cho cả cụm.

---

## CKTMBMHDLCTT_11 (row 96) — Message "Ẩn X/Y thư mục, Z thất bại" khi ẩn hàng loạt một phần

**Bối cảnh testcase**

- Dòng Excel: 96, mã TC `CKTMBMHDLCTT_11`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương ẩn hàng loạt nhiều thư mục, trong đó có thư mục đủ điều kiện (đang công khai) và thư mục không đủ điều kiện (chưa công khai).
- Expected trong file UAT: message rõ ràng theo thiết kế (kiểu "Đã ẩn {X}. {Y} thư mục không đủ điều kiện...").
- Actual đối tác ghi: hệ thống báo *"Ẩn 1/3 thư mục, 2 thất bại"* — wording khác thiết kế (dùng "thất bại" cho thư mục không đủ điều kiện).

**Đối chiếu SRS v3.5**

- `srs-fr-09-bieu-mau.md:250-251` (FR-VII-03 Error Handling): chỉ định nghĩa ERR-CK-01 (thư mục rỗng) + WRN-CK-01 (thư mục đã công khai) cho **công khai đơn lẻ**. KHÔNG có message chuẩn cho **ẩn hàng loạt một phần**, cũng không có message riêng cho hướng ẩn.
- Expected của đối tác không có nguồn SRS. SRS **im lặng** về message bulk một phần → cùng bản chất với sub-issue wording của case 94 (công khai hàng loạt một phần).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:250-251`

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB Nghiệp vụ Trung ương (CB_NV_TW).
- Chọn 2 thư mục ẩn hàng loạt: QA Hidden Folder 715 (đang Đã công khai = đủ đk ẩn) + BM-B3-0720-Rong-1 (Nháp = chưa công khai, không thể ẩn).
- Toast (observer, 1 toast không nhân đôi): **"Ẩn 1/2 thư mục, 1 thất bại."** — 715 → Đã ẩn (thành công); Rong-1 → vẫn Nháp (thất bại đúng). 1 request `POST /api/v1/thu-muc-bieu-maus/batch-an`.
- Đối chiếu evidence đối tác: toast **"Ẩn 1/3 thư mục, 2 thất bại."** — cùng dạng wording `Ẩn {X}/{Y} thư mục, {Z} thất bại`, chỉ khác con số do đối tác chọn 3 thư mục.
- Evidence: `../../reverify-audit/CKTMBMHDLCTT_11/web-after-batch-an-partial.png` + `../../reverify-audit/CKTMBMHDLCTT_11/observer-result.json`.

**Kết luận QA**

- `CKTMBMHDLCTT_11` **tái hiện đúng** dạng wording đối tác báo — KHÔNG phải Reject.
- Bất đồng về ĐẶC TẢ (wording): SRS không quy định message chuẩn cho ẩn hàng loạt một phần → không đủ căn cứ Open.

**Nội dung đề xuất BA phản hồi đối tác**

- BA chốt message chuẩn cho thao tác hàng loạt một phần (áp chung công khai – case 94 + ẩn – case này). Gợi ý dùng "không đủ điều kiện" thay "thất bại" để rõ nguyên nhân (thư mục chưa công khai / rỗng không phải "lỗi", chỉ là không áp dụng được).
- Cập nhật SRS §Error Handling (bổ sung message bulk partial) + expected testcase cho khớp.
- Verdict QA đề xuất: `BA confirm`, **không gửi Dev** cho tới khi BA chốt message chuẩn.
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
# BA confirmation needed — UAT đối tác tuần 3, Batch 6 (Biểu mẫu) — 2026-07-20

> **File này để làm gì:** gom các testcase re-verify Batch 6 mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI để BA quyết nhanh.
>
> **Phạm vi:** module Biểu mẫu — Nhập hàng loạt (FR-VII-06 / SCR-VII-03) + Công khai (FR-VII-07). 5/7 case của batch cần BA. 2 case còn lại (IBMHD_10, CKBMHDLCTT_01) đã Reject — không tái hiện trên bản hiện tại, không đưa vào file này.
>
> **SRS dùng:** v3.5 — `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md`. Tài khoản verify: `cbnv_bn` (CB Nghiệp vụ - Bộ ngành). Case chỉ định vai trò "CB Nghiệp vụ"; `cbnv_tw` đang bị session khác chiếm liên tục nên dùng `cbnv_bn` cùng vai trò — các case này là render UI / validate client / diễn giải SRS, không phụ thuộc đơn vị.

---

## IBMHD_02 (và IBMHD_03) — Màn Nhập hàng loạt: trường "Tải file Excel metadata" + nút "Tải mẫu Excel"

**Bối cảnh testcase**

- Dòng Excel: 116, mã TC `IBMHD_02` — "Màn Import thiếu trường Tệp Excel mô tả dữ liệu + nút Tải mẫu Excel".
- Dòng Excel: 117, mã TC `IBMHD_03` — "Chức năng Tải mẫu Excel bị thiếu" (cùng gốc: nút Tải mẫu Excel là thành phần của trường Excel metadata).
- Nội dung kiểm tra: CB Nghiệp vụ mở màn Nhập hàng loạt biểu mẫu (`/bieu-mau/nhap-hang-loat`).
- Expected trong file UAT: màn phải có trường "Tệp Excel mô tả dữ liệu" và nút "Tải mẫu Excel".

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_bn` / CB Nghiệp vụ. URL `/bieu-mau/nhap-hang-loat`.
- Màn bước 1 "Chọn file" chỉ có: **Thư mục đích** (select) + **Tải lên file biểu mẫu** (.doc/.docx/.xls/.xlsx, kéo-thả).
- KHÔNG có trường "Tải file Excel metadata", KHÔNG có nút "Tải mẫu Excel".
- Khớp 100% với ảnh đối tác chụp trên bản đối tác → hành vi giống nhau hai bản.
- Evidence: `bug-reports/image/BUG-IBMHD_02-03-import-screen-step1.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **FR-VII-06 §Inputs**, luồng import chỉ nhận 2 field và KHÔNG có Excel metadata:
   - `thu_muc_id` (Thư mục đích, bắt buộc)
   - `files` (binary[], Max 50 file / 20MB / tổng 500MB)
   - Không bước Processing nào (kiểm quyền → validate → tạo bản ghi → tổng hợp → log) tiêu thụ file metadata.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:460` (thu_muc_id)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:461` (files)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:463-472` (Processing — không có metadata)

2. Nhưng **SCR-VII-03 §Thành phần màn hình mục #2** lại yêu cầu trường Excel metadata + nút Tải mẫu, **luôn hiển thị**:
   - "Tải file Excel metadata | file-upload | .xlsx (max 5MB), Template: **[Tải mẫu Excel]** | luôn hiển thị"

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:673`

**Câu hỏi cần BA xác nhận**

Màn Nhập hàng loạt biểu mẫu có bắt buộc trường "Tải file Excel metadata" + nút "Tải mẫu Excel" không? SRS đang mâu thuẫn giữa đặc tả nghiệp vụ (FR-VII-06 không dùng metadata) và đặc tả màn hình (SCR-VII-03 #2 yêu cầu hiển thị).

1. **Hướng 1 — theo SCR-VII-03 #2:** phải bổ sung trường Excel metadata + nút Tải mẫu Excel → app hiện tại **thiếu** → Dev FE bổ sung; đồng thời BA làm rõ metadata được xử lý ở bước Processing nào.
2. **Hướng 2 — theo FR-VII-06:** luồng import chỉ cần `thu_muc_id` + `files`, metadata không dùng → app hiện tại **đúng** → cập nhật SCR-VII-03 bỏ mục #2 + cập nhật expected của đối tác.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt source truth.
- Verdict tạm cho `IBMHD_02` + `IBMHD_03`: **Cần BA xác nhận** (đã ghi sheet `BA confirm`, dòng 116 + 117).
- Nếu BA chọn Hướng 1: UI hiện tại `Vẫn thiếu`, owner `Dev FE` (thêm trường + nút) + `BA` (định nghĩa cách dùng metadata).
- Nếu BA chọn Hướng 2: UI hiện tại `Đúng SRS nghiệp vụ`; owner `QA/BA` cập nhật SCR-VII-03 + expected đối tác.

---

## IBMHD_04 — Chọn tệp → bảng kiểm tra không liệt kê tệp lỗi (Hợp lệ/Lỗi)

**Bối cảnh testcase**

- Dòng Excel: 118, mã TC `IBMHD_04`.
- Nội dung kiểm tra: CB Nghiệp vụ upload tệp sai định dạng / vượt kích thước ở màn Nhập hàng loạt, xem bảng kiểm tra.
- Expected trong file UAT: tệp lỗi hiển thị trong bảng kiểm tra với trạng thái Hợp lệ/Lỗi kèm lý do.
- Actual đối tác ghi: tệp lỗi không xuất hiện trong bảng kiểm tra.

**Đối chiếu SRS v3.5**

- SCR-VII-03 #4 (Bảng kiểm tra) quy định bảng có cột **"Trạng thái (Hợp lệ/Lỗi)"**, hiển thị "sau upload" → hàm ý tệp lỗi phải xuất hiện thành dòng có trạng thái Lỗi. Bảng **không có cột "Lý do"** → kỳ vọng "kèm lý do" của đối tác vượt quá SRS.
- SCR-VII-03 #5 (Thống kê) quy định "Tổng: {N} file. Hợp lệ: {X}. **Lỗi: {Y}**" → SRS kỳ vọng có đếm số tệp lỗi.
- FR-VII-06 §Processing bước 2 "Kiểm tra từng file: định dạng + kích thước" — SRS không nói rõ kiểm ở bước chọn hay bước import.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:675` (Bảng kiểm tra — cột Trạng thái Hợp lệ/Lỗi)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:676` (Thống kê — Lỗi: {Y})
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:468` (Processing bước 2 — validate định dạng + kích thước)

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, `cbnv_bn` / CB Nghiệp vụ. Upload `.txt` (sai định dạng) + `.docx` 22MB (>20MB) + 2 tệp hợp lệ.
- Tệp lỗi bị **chặn NGAY tại bước Chọn file** kèm thông báo lý do ("Định dạng không hỗ trợ: ... Chỉ chấp nhận .doc,.docx,.xls,.xlsx" / "vượt quá 20MB (22.0 MB)").
- Bảng kiểm tra (STT / Tên / Định dạng / Kích thước / Trạng thái) + Thống kê (Tổng/Hợp lệ/Không hợp lệ) **chỉ liệt kê tệp hợp lệ**; tệp lỗi không thành dòng.
- Đối chiếu: app báo lỗi + lý do (đạt mục tiêu "người dùng biết tệp nào sai + vì sao"), nhưng KHÁC cách trình bày mà SCR-VII-03 #4/#5 mô tả (tệp lỗi thành dòng Lỗi trong bảng + đếm Lỗi:{Y}).
- Evidence: `bug-reports/image/BUG-IBMHD_04-step1-valid-2-reject-txt.png`, `bug-reports/image/BUG-IBMHD_04-step2-bang-kiem-tra.png`

**Kết luận QA**

- `IBMHD_04` tái hiện đúng phần "tệp lỗi không có trong bảng kiểm tra" — nhưng KHÔNG "im lặng": app báo lý do tại bước chọn.
- App đạt yêu cầu nghiệp vụ (thông báo tệp lỗi + lý do trước khi import) nhưng lệch đặc tả màn SCR-VII-03 #4/#5 (kỳ vọng Lỗi thành dòng + đếm trong bảng).
- Kỳ vọng "kèm lý do trong bảng" của đối tác vượt SRS (SCR-VII-03 #4 không có cột Lý do).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt mô hình kiểm tra tệp lỗi:

- **Hướng 1 (theo literal SCR-VII-03 #4/#5):** tệp lỗi phải hiện thành dòng "Lỗi" trong Bảng kiểm tra + đếm ở Thống kê "Lỗi: {Y}" → app hiện tại `Vẫn lỗi`, owner `Dev FE`.
- **Hướng 2 (chấp nhận early-validation):** app báo lỗi + lý do tại bước chọn là đủ (đạt mục tiêu nghiệp vụ) → app hiện tại `Đúng`, owner `QA/BA` cập nhật SCR-VII-03 + expected đối tác (bỏ kỳ vọng "kèm lý do").
- Verdict QA đề xuất: `Cần BA xác nhận` (đã ghi sheet dòng 118), chưa gửi Dev tới khi BA chốt.

---

## IBMHD_07 — Import lô có tệp lỗi → không hiện "{Y} tệp lỗi: xem chi tiết"

**Bối cảnh testcase**

- Dòng Excel: 119, mã TC `IBMHD_07`.
- Nội dung kiểm tra: CB Nghiệp vụ import một lô có cả tệp hợp lệ + tệp lỗi, xem kết quả import.
- Expected trong file UAT: kết quả import hiện "{Y} tệp lỗi: xem chi tiết" + bảng chi tiết lý do lỗi.
- Actual đối tác ghi: không hiện thông báo tệp lỗi + bảng chi tiết.

**Đối chiếu SRS v3.5**

- FR-VII-06 §Processing bước 4-5: "Với mỗi file lỗi: ghi vào báo cáo lỗi" → "Trả về tổng hợp: N thành công, M lỗi".
- Error Handling E2 (WRN-IMP-01): "Import thành công {N} file. **{M} file lỗi: xem chi tiết**".
- Outputs `chi_tiet_loi` structured `[{file_ten, ly_do}]` — "Khi có lỗi".
- Postcondition + AC: "File lỗi được ghi vào báo cáo chi tiết"; "Given 1+ file lỗi When import Then báo cáo lỗi chi tiết, import các file hợp lệ còn lại"; "hiển thị tổng hợp: N file thành công, M file lỗi".

**Citation**

- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:479` (E2 WRN-IMP-01)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:489` (Outputs chi_tiet_loi)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:498-499` (AC — báo cáo lỗi chi tiết + tổng hợp N/M)

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, `cbnv_bn` / CB Nghiệp vụ.
- Vì app validate định dạng/kích thước SỚM ở bước chọn (xem IBMHD_04), **tệp lỗi không tới được bước Import** → tới bước import chỉ còn tệp hợp lệ → kết quả chỉ hiện "Đã nhập thành công 2 biểu mẫu" (không có nhánh "{M} tệp lỗi").
- Thử import trùng tên (duplicate): app **chấp nhận**, không coi là lỗi → cũng không sinh nhánh lỗi.
- Không tái hiện được lỗi phát sinh TẠI bước import trong luồng thường.
- **Giới hạn kiểm thử (honest):** chưa thử được loại lỗi chỉ phát sinh ở bước import (vd file .docx đúng đuôi nhưng nội dung hỏng / lỗi ghi DB). Nhánh "{M} tệp lỗi" có thể vẫn tồn tại cho các lỗi này — chưa reproduce.
- Evidence: `bug-reports/image/BUG-IBMHD_07-step3-ket-qua-import.png`

**Kết luận QA**

- `IBMHD_07`: nhánh "{M} tệp lỗi: xem chi tiết" (E2) không kích hoạt trong luồng nhập thường vì lỗi định dạng/kích thước đã bị chặn sớm; duplicate không bị coi là lỗi.
- Chưa khẳng định app THIẾU nhánh này (có thể vẫn có cho lỗi import-time chưa test được).

**Nội dung đề xuất BA phản hồi đối tác**

- **Hướng 1:** nếu SRS bắt buộc nhánh "{M} tệp lỗi" luôn có (vd cả với lỗi định dạng), thì mô hình kiểm-sớm hiện tại chưa đạt AC → cần Dev bổ sung / đổi điểm kiểm → `Cần Dev BE/FE`.
- **Hướng 2:** nếu chấp nhận app catch lỗi định dạng/kích thước ở bước chọn (chỉ giữ nhánh {M} lỗi cho lỗi import-time), thì cần một test-case tạo lỗi import-time để xác minh nhánh — QA sẽ seed file hỏng để verify tiếp.
- Verdict QA đề xuất: `Cần BA xác nhận` (đã ghi sheet dòng 119). Đề nghị BA xác nhận mô hình kiểm-sớm có đạt AC "báo cáo lỗi chi tiết" không.

---

## IBMHD_11 — Nút "Hủy" màn Import không hiện hộp xác nhận

**Bối cảnh testcase**

- Dòng Excel: 121, mã TC `IBMHD_11`.
- Nội dung kiểm tra: CB Nghiệp vụ đã chọn thư mục + tải tệp lên màn Nhập hàng loạt, bấm "Hủy".
- Expected trong file UAT: bấm "Hủy" hiện hộp xác nhận (tránh mất tệp đã tải).
- Actual đối tác ghi: không hiện hộp xác nhận.

**Đối chiếu SRS v3.5**

- FR-VII-06 (toàn UC, `:444-508`) đặc tả Inputs / Processing / Error / AC — KHÔNG đề cập nút "Hủy" lẫn hành vi xác nhận khi hủy.
- SCR-VII-03 §Thành phần màn hình (`:670-677`) liệt kê 6 thành phần (Thư mục đích, Excel metadata, Tải nhiều file, Bảng kiểm tra, Thống kê, Nút xác nhận) — **không có nút "Hủy"** và không có yêu cầu hộp xác nhận khi hủy.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:444-508` (FR-VII-06 — không có nút Hủy)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:670-677` (SCR-VII-03 Thành phần — không có nút Hủy / hộp xác nhận)

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, `cbnv_bn` / CB Nghiệp vụ.
- Đã chọn thư mục + tải 1 tệp (có thay đổi chưa lưu) → bấm "Hủy" → **điều hướng NGAY** sang `/bieu-mau/danh-sach`, KHÔNG có modal xác nhận (điều hướng tức thì = không có modal chặn).
- Tái hiện đúng claim đối tác.
- Evidence: `bug-reports/image/BUG-IBMHD_11-huy-navigated-no-confirm.png`

**Kết luận QA**

- `IBMHD_11` tái hiện đúng: Hủy rời màn ngay, không xác nhận, kể cả khi đã tải tệp.
- Nhưng SRS **không quy định** nút Hủy phải có hộp xác nhận → kỳ vọng của đối tác chưa có cơ sở SRS. Đây là gap yêu cầu (SRS thiếu đặc tả), không phải app sai so với SRS hiện có.

**Nội dung đề xuất BA phản hồi đối tác**

- Đề nghị BA quyết có bổ sung yêu cầu "hộp xác nhận trước khi Hủy khi đã tải tệp" vào SRS không (UX chống mất dữ liệu vô ý).
- Nếu **có** → owner `Dev FE` thêm Popconfirm + `BA` bổ sung SRS. Nếu **không** → app hiện tại đúng, cập nhật expected đối tác.
- Verdict QA đề xuất: `Cần BA xác nhận` (đã ghi sheet dòng 121). Chưa gửi Dev tới khi BA chốt.
