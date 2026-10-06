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
