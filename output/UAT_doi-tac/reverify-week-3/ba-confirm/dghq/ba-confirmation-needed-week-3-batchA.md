# BA confirmation needed — UAT tuần 3 — Batch A (module Đánh giá hiệu quả) — 2026-07-20

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. Các case là bug có SRS reference rõ (Open) đã log ở `../../bug-reports/dghq/Pass-bug-report-DGHQ-batchA.md`, KHÔNG nằm ở đây.

> **Quy tắc citation:** mọi khẳng định SRS trỏ `file-srs.md:LINE`, số dòng đã mở file verify thực (không dùng trí nhớ). Bản SRS chấm: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md` (v3.5). Tab đối tác: `UAT_TGPL Doanh Nghiệp-tuần 3`. Verify env: `18.143.165.120.nip.io`, login `cbnv_tw` (CB_NV_TW).

> **2 dạng case trong file này:** Dạng A = QA đã kết luận, cần BA phản hồi đối tác (LKHDG_02, LKHDG_03, LKHDG_10, PCNTHDG_06). Dạng B = SRS tự mâu thuẫn, QA không tự chốt (LKHDG_19).

---

## LKHDG_02 (Dạng A) — Cột "Tên đợt" bị cắt bớt: web đúng SRS, kỳ vọng đọc đầy đủ nằm ngoài spec

**Bối cảnh testcase**

- Dòng Excel: 43, mã TC `LKHDG_02`.
- Nội dung kiểm tra: CB Nghiệp vụ TW (`cbnv_tw`) kiểm tra hiển thị cột "Tên đợt" trong danh sách đợt đánh giá (màn Kế hoạch đánh giá → Danh sách).
- Expected trong file UAT:
  - "Tên đợt là thông tin quan trọng nhưng cắt bớt quá nhiều dẫn đến khó quan sát" → đối tác kỳ vọng đọc được đầy đủ tên đợt.
- Actual đối tác ghi: cột "Tên đợt" bị cắt bớt quá mức.

**Đối chiếu SRS v3.5**

- SCR-VI-01 (Danh sách đợt), cột "Tên đợt" quy định giá trị hiển thị là "Tên đợt đánh giá (cắt bớt + '...')" → cắt bớt là hành vi ĐÚNG thiết kế.
- SRS không quy định độ rộng cột, mức cắt tối đa, hay tooltip hiện đầy đủ tên khi hover.

**Citation**

- `srs-v3.5/srs-fr-08-danh-gia.md:820`

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB Nghiệp vụ TW.
- Mở màn Kế hoạch đánh giá → Danh sách.
- Danh sách CÓ cột "Tên đợt", nhưng cột hẹp: header cột bị cắt thành "Tên đ...", giá trị "Đợt đánh giá seed 2026" hiển thị thành "Đợt đánh...".
- Đối chiếu SRS: cắt bớt đúng như dòng 820 quy định; điểm đối tác nêu (đọc không đủ) SRS chưa quy định.
- Evidence: `../../reverify-audit/LKHDG_02/web-danhsach.png`

**Kết luận QA**

- `LKHDG_02` không phải bug theo SRS v3.5: SRS sanction cắt bớt tên đợt (dòng 820), không có clause nào bị vi phạm.
- Web hiện tại đúng SRS ở hành vi cắt bớt.
- Không Reject: hiện tượng đối tác nêu (tên bị cắt) có tái hiện — nhưng đây là đúng thiết kế, không phải lỗi.
- QA không tự chốt "phải sửa" vì SRS không quy định mức hiển thị đầy đủ (tooltip/độ rộng).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị xác nhận hướng xử lý hiển thị "Tên đợt":

- Giữ nguyên cắt bớt "..." như SRS dòng 820, HOẶC bổ sung tooltip hiện đầy đủ tên khi hover / mở rộng cột.
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev (SRS chưa quy định mức hiển thị đầy đủ, cần BA chốt trước).

---

## LKHDG_03 (Dạng A) — Bộ lọc danh sách: 1 ý web đúng, 2 ý khác dạng SRS mô tả (placeholder vs "Tất cả", tabs vs dropdown)

**Bối cảnh testcase**

- Dòng Excel: 44, mã TC `LKHDG_03`.
- Nội dung kiểm tra: CB Nghiệp vụ TW kiểm tra điều kiện tìm kiếm / bộ lọc màn danh sách đợt đánh giá. Đối tác nêu 3 ý.
- Expected trong file UAT:
  - #1: Tần suất phải hiển thị "Tròn năm" (đối tác nghi app ghi sai chính tả).
  - #2: Bộ lọc phải mặc định "Tất cả".
  - #3: Phải có bộ lọc Trạng thái trong thanh lọc.
- Actual đối tác ghi: nghi hiển thị sai chữ + thiếu default "Tất cả" + thiếu lọc trạng thái.

**Đối chiếu SRS v3.5**

- #1: cột Tần suất SRS ghi "TRON_NAM → 'Tròn năm'"; app hiển thị "Trọn năm" (đúng chính tả tiếng Việt hơn — nghi SRS typo). App không sai nghiệp vụ.
- #2: dropdown Lọc tần suất / Lọc đối tượng SRS liệt kê "Tất cả" là một option. App dùng cơ chế placeholder (không chọn = không lọc = tất cả) thay cho mục "Tất cả".
- #3: SRS quy định Lọc trạng thái là dropdown C10 trong thanh lọc. App có lọc trạng thái nhưng dạng tabs (Tất cả/Lập kế hoạch/.../Hủy), không phải dropdown trong filter bar.

**Citation**

- `srs-v3.5/srs-fr-08-danh-gia.md:821` (cột Tần suất — "Tròn năm")
- `srs-v3.5/srs-fr-08-danh-gia.md:813` (Lọc tần suất — có option "Tất cả")
- `srs-v3.5/srs-fr-08-danh-gia.md:814` (Lọc đối tượng — có option "Tất cả")
- `srs-v3.5/srs-fr-08-danh-gia.md:815` (Lọc trạng thái — dropdown C10)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`.
- Dropdown Tần suất hiển thị đúng "Trọn năm" (cả dropdown + cột) → ý #1 lỗi KHÔNG tái hiện.
- Dropdown Tần suất = [Sơ bộ 6 tháng, Trọn năm] (không có mục "Tất cả"); Đối tượng chỉ có placeholder → app dùng cơ chế placeholder.
- Filter bar không có ô Trạng thái, nhưng có lọc trạng thái dạng tabs.
- Evidence: `../../reverify-audit/LKHDG_03/web-tansuat-dropdown.png`

**Kết luận QA**

- `LKHDG_03` là case hỗn hợp:
  - ý #1: app đúng (không phải bug, thậm chí đúng chính tả hơn SRS);
  - ý #2 + #3: app đáp ứng chức năng nhưng khác DẠNG SRS mô tả (placeholder vs mục "Tất cả"; tabs vs dropdown).
- Không có clause nghiệp vụ bị vi phạm rõ ràng → QA không tự chốt Open; cần BA quyết chuẩn hoá UI.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị:

- #1: cập nhật expected của đối tác — app hiển thị "Trọn năm" là đúng; cân nhắc sửa typo SRS dòng 821 ("Tròn năm" → "Trọn năm").
- #2: BA chốt dropdown lọc dùng placeholder ("không chọn = tất cả") có chấp nhận không, hay phải thêm mục "Tất cả" + đặt mặc định.
- #3: BA chốt lọc trạng thái bằng bộ tabs có thay được dropdown "Lọc trạng thái" theo SRS #6 (dòng 815) không.
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev.

---

## LKHDG_10 (Dạng A) — Sau "Lưu nháp" không điều hướng chi tiết: đúng SRS, kỳ vọng điều hướng nằm ngoài spec

**Bối cảnh testcase**

- Dòng Excel: 48, mã TC `LKHDG_10`.
- Nội dung kiểm tra: CB Nghiệp vụ TW kiểm tra chức năng "Lưu nháp" trên form Tạo kế hoạch đánh giá.
- Expected trong file UAT:
  - Sau khi Lưu nháp, giữ/chuyển user đến màn chi tiết đợt.
- Actual đối tác ghi: "Không giữ/chuyển đến màn hình chi tiết đợt".

**Đối chiếu SRS v3.5**

- Thanh hành động form (SCR-VI-01 #27) quy định RÕ 2 nút khác nhau: "[Lưu nháp] (→ LAP_KE_HOACH)" chỉ lưu trạng thái, KHÔNG mở chi tiết; "[Lưu & Chuyển tiêu chí] (→ lưu + mở Tab 1 chi tiết)" mới điều hướng.
- FR-VI-01 (UC83) Outputs #3 chỉ yêu cầu "Thông báo thành công | Toast".
- Postconditions chỉ yêu cầu tạo bản ghi trạng thái LAP_KE_HOACH (+ audit log), không yêu cầu điều hướng chi tiết.

**Citation**

- `srs-v3.5/srs-fr-08-danh-gia.md:841` (#27 thanh hành động form — "Lưu nháp" vs "Lưu & Chuyển tiêu chí")
- `srs-v3.5/srs-fr-08-danh-gia.md:139` (UC83 Outputs #3 — Toast)
- `srs-v3.5/srs-fr-08-danh-gia.md:143` (Postconditions — tạo bản ghi LAP_KE_HOACH)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`.
- Nhập đủ trường → bấm "Lưu nháp" → toast "Tạo kế hoạch đánh giá thành công"; tạo đợt DG-20260720-0002 trạng thái "Lập kế hoạch"; mã đúng định dạng DG-{YYYYMMDD}-{seq}.
- Sau lưu: đóng biểu mẫu, ở lại màn danh sách (không sang chi tiết) → hiện tượng đối tác nêu CÓ tái hiện, và ĐÚNG mô tả nút "Lưu nháp".
- Evidence: `../../reverify-audit/LKHDG_10/web-luunhap-stay-list.png`

**Kết luận QA**

- `LKHDG_10` không phải bug theo SRS v3.5: mọi yêu cầu SRS-mandated (toast + mã + trạng thái LAP_KE_HOACH) đều đạt; "Lưu nháp" không điều hướng chi tiết là đúng thiết kế (khác với "Lưu & Chuyển tiêu chí").
- Không Reject: hiện tượng có tái hiện — nhưng là hành vi đúng.
- Kỳ vọng điều hướng của đối tác nằm ngoài SRS (SRS silent về navigation sau "Lưu nháp").

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị:

- Cập nhật expected của đối tác: "Lưu nháp" chỉ lưu + ở lại danh sách (đúng SRS #27 dòng 841); muốn vào chi tiết thì dùng "Lưu & Chuyển tiêu chí".
- Nếu BA muốn "Lưu nháp" cũng điều hướng chi tiết → là yêu cầu MỚI ngoài SRS, cần bổ sung spec trước khi gửi Dev.
- Verdict QA đề xuất: `Cần BA xác nhận` (nghiêng "Không phải bug theo SRS"), chưa gửi Dev.

---

## LKHDG_19 (Dạng B) — Chi tiết đợt không hiển thị "Cơ quan được đánh giá": SRS mâu thuẫn nội bộ

**Bối cảnh testcase**

- Dòng Excel: 51, mã TC `LKHDG_19`.
- Nội dung kiểm tra: CB Nghiệp vụ TW kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá.
- Expected trong file UAT: màn chi tiết hiển thị trường "Cơ quan được đánh giá".

**Kết quả verify UI hiện tại**

- Verify ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`. Mở chi tiết đợt DG-20260720-0002.
- Thẻ "Thông tin kế hoạch" hiển thị: Mã kế hoạch, Tên đợt, Tần suất, Đối tượng, Thời gian bắt đầu/kết thúc, Số vụ việc, Điểm trung bình.
- KHÔNG hiển thị "Cơ quan được đánh giá" dù đã nhập "Bộ Công an" lúc tạo → hiện tượng đối tác nêu CÓ tái hiện.
- Điểm phù hợp SRS: thẻ hiển thị khớp danh sách trường mô tả ở SCR-VI-01 #28.
- Evidence: `../../reverify-audit/LKHDG_19/web-chitiet-thieu-coquan.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo SCR-VI-01 (mô tả thẻ hiển thị "Thông tin đợt" #28), thẻ chi tiết chỉ liệt kê 5 trường: Mã đợt, Tên đợt, Tần suất, Kỳ đánh giá, Đối tượng (read-only) → KHÔNG có "Cơ quan được đánh giá". App khớp mô tả này.

   Citation:
   - `srs-v3.5/srs-fr-08-danh-gia.md:849`

2. Nhưng data model KE_HOACH_DANH_GIA #16 quy định `co_quan_duoc_danh_gia_id` là trường **bắt buộc (Y)**, FK → DON_VI, "Cơ quan được đánh giá (1:1, Q-07)" — thông tin cốt lõi user bắt buộc nhập khi tạo đợt.

   Citation:
   - `srs-v3.5/srs-fr-08-danh-gia.md:1033`

**Câu hỏi cần BA xác nhận**

Màn chi tiết đợt có cần hiển thị "Cơ quan được đánh giá" không (trường bắt buộc trong data model nhưng vắng trong mô tả thẻ hiển thị #28)? Cần hiểu theo hướng nào?

1. **Hướng 1 — theo data model #16 (dòng 1033):** thẻ chi tiết PHẢI bổ sung "Cơ quan được đánh giá" (và cân nhắc "Mục tiêu" cũng bắt buộc nhưng vắng) → UI hiện tại thiếu là lỗi.
2. **Hướng 2 — theo mô tả hiển thị #28 (dòng 849):** thẻ chỉ hiển thị 5 trường như SRS → UI hiện tại đúng, cập nhật lại expected của testcase.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict `LKHDG_19`: `Cần BA xác nhận`.
- Nếu BA chọn hướng 1: UI hiện tại `Vẫn lỗi`, owner dự kiến `Dev FE` (bổ sung trường hiển thị) + BA cập nhật mô tả #28 cho khớp data model.
- Nếu BA chọn hướng 2: UI hiện tại không phải lỗi; cập nhật lại expected của đối tác cho khớp SRS #28.

---

## PCNTHDG_06 (Dạng A) — Nút [Hủy] modal "Thêm người đánh giá" không có cửa sổ xác nhận: SRS silent

**Bối cảnh testcase**

- Dòng Excel: 60, mã TC `PCNTHDG_06`.
- Nội dung kiểm tra: CB Nghiệp vụ TW kiểm tra nút "Hủy" trong tab Phân công. "Hủy" = nút [Hủy] trên modal "Thêm người đánh giá" (xác định qua video đối tác `PCNTHDG_06.webm` — đối tác đã chọn Người ĐG + Vai trò Trưởng nhóm rồi bấm Hủy).
- Expected trong file UAT:
  - Bấm "Hủy" → hiện cửa sổ xác nhận hủy bỏ thay đổi chưa lưu, sau đó hoàn tác.
- Actual đối tác ghi: không hiển thị cửa sổ xác nhận.

**Đối chiếu SRS v3.5**

- SCR-VI-01 không quy định modal "Thêm người đánh giá" phải có bước xác nhận trước khi hủy input chưa lưu.
- Thanh hành động Phân công #38 có nút [Hủy] nhưng không mô tả bước xác nhận.
- Khác với Xóa tiêu chí #29 được gán component C12; C12 = "confirm" được thiết lập qua #39 ("→ C12 confirm"). Modal thêm mới (dữ liệu chưa commit) KHÔNG được gán C12.

**Citation**

- `srs-v3.5/srs-fr-08-danh-gia.md:864` (#38 thanh hành động Phân công — có [Hủy], không mô tả xác nhận)
- `srs-v3.5/srs-fr-08-danh-gia.md:850` (#29 Xóa tiêu chí gán C12)
- `srs-v3.5/srs-fr-08-danh-gia.md:865` (#39 "→ C12 confirm" — định nghĩa C12 = confirm)

**Kết quả verify UI hiện tại**

- Verify ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`, đợt DG-20260720-0002.
- Tab Phân công → "Thêm người đánh giá" → chọn "Cán bộ Nghiệp vụ Demo" + Vai trò "Trưởng nhóm" → bấm [Hủy].
- Kết quả: modal đóng ngay, `confirmPopup=false` (không có `.ant-modal-confirm`/popover xác nhận), Tổng: 0 người (input chưa lưu bị bỏ im lặng) → hiện tượng đối tác nêu CÓ tái hiện.
- Evidence: `../../reverify-audit/PCNTHDG_06/modal-them-nguoi-danh-gia.png`, `../../reverify-audit/PCNTHDG_06/dom-evidence.txt`

**Kết luận QA**

- `PCNTHDG_06` không phải bug theo SRS v3.5: không có clause nào quy định modal cancel phải xác nhận → không vi phạm (không Open).
- Không Reject: hành vi (đóng im lặng, không xác nhận) tái hiện đúng như đối tác báo.
- SRS silent + kỳ vọng đối tác khác hành vi thực tế → QA không tự chốt "phải có/không có xác nhận"; đóng im lặng khi hủy modal thêm mới (dữ liệu chưa commit) là chuẩn UX phổ biến.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt:

- Khi bấm [Hủy] trên modal "Thêm người đánh giá" (đã nhập dữ liệu chưa lưu), có cần hộp thoại xác nhận "hủy bỏ thay đổi chưa lưu?" không, hay giữ hành vi đóng im lặng như hiện tại?
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev.
