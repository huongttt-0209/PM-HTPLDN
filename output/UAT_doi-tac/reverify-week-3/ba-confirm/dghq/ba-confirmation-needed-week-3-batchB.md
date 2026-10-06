# BA confirmation needed — UAT tuần 3 — Batch B (Đánh giá hiệu quả) — 2026-07-20

> **File này để làm gì:** gom các testcase Batch B (module **Đánh giá hiệu quả**, luồng downstream Thực hiện → Báo cáo → Phê duyệt BC, rows 65–79) mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI để BA quyết nhanh. Case `Open` (bug có SRS reference rõ) → `../../bug-reports/dghq/Pass-bug-report-DGHQ-batchB.md`; `Reject` → `../../reverify-audit/<mã TC>/`.

> **SRS chấm:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md` (FR-VI-05 → FR-VI-09). Tab đối tác: `UAT_TGPL Doanh Nghiệp-tuần 3`. Tài khoản UAT dùng verify: `cbnv_hn` (CB_NV_DP — Sở Tư pháp Hà Nội), `cbpd_hn` (CB_PD_DP — Sở Tư pháp Hà Nội).

---

## CVVDG_01 (row 65) — Toast chọn vụ việc "Đã chọn vụ việc đánh giá" khác thiết kế đối tác "Đã lưu {N} vụ việc"

**Bối cảnh testcase**

- Dòng Excel: 65, mã TC `CVVDG_01`.
- Nội dung kiểm tra: CB Nghiệp vụ chọn vụ việc đánh giá (FR-VI-05, Tab Thực hiện) — quan sát thông báo sau khi lưu danh sách VV.
- Expected trong file UAT:
  - Sau khi chọn VV → thông báo hiển thị dạng **"Đã lưu {N} vụ việc"** (có số lượng + động từ "Lưu"), theo bản thiết kế.
- Actual đối tác ghi: toast không đúng chuỗi thiết kế.

**Đối chiếu SRS v3.5**

- FR-VI-05 mô tả bước xử lý khi chọn VV: hệ thống lọc VV `HOAN_THANH` trong kỳ và **lưu danh sách VV đánh giá** (bước 6). Đây là yêu cầu nghiệp vụ "lưu thành công danh sách VV", không quy định chuỗi ký tự thông báo cụ thể.
- Outputs / Error Handling của FR-VI-05 **không** prescribe wording toast nào cho thao tác lưu thành công → SRS **im lặng** về nội dung chuỗi thông báo.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:420` — bước 6 "Lưu danh sách VV đánh giá".
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:384-451` — toàn bộ FR-VI-05, không có dòng nào quy định chuỗi toast.

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_hn` / CB_NV_DP.
- Tích chọn VV hoàn thành → Xác nhận chọn → `POST .../vu-viec-select` [200]; VV chuyển "Đã chọn", KPI "Số VV đánh giá" +1 (nghiệp vụ đạt).
- Toast hiển thị **"Đã chọn vụ việc đánh giá"** — 1 toast / 1 request, không double.
- Đối chiếu SRS: nghiệp vụ lưu VV thành công (đúng bước 6), chỉ khác chuỗi thông báo so với bản thiết kế đối tác.
- Evidence: `../../reverify-audit/CVVDG_01/toast-chon-vv.png` · đối tác `../CVVDG_01.jpg`. Bảng điều kiện: `../../cond/CVVDG_01.md`.

**Kết luận QA**

- `CVVDG_01` không phải bug logic theo SRS v3.5 — chức năng chọn/lưu VV chạy đúng.
- Web hiện tại **đúng** yêu cầu nghiệp vụ FR-VI-05; chỉ **lệch chuỗi thông báo** so với bản thiết kế của đối tác. SRS không quy định wording nên QA không có căn cứ chốt đúng/sai chuỗi.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý chuỗi thông báo:

- Giữ nguyên "Đã chọn vụ việc đánh giá" (app hiện tại), hay đổi theo thiết kế "Đã lưu {N} vụ việc" (có số lượng).
- Nếu BA chốt theo thiết kế đối tác → cập nhật chuỗi toast (owner: Dev FE); nếu BA chấp nhận app → cập nhật lại expected của `CVVDG_01`.
- Verdict QA đề xuất: `Cần BA xác nhận` (SRS im lặng về wording), chưa gửi Dev.

---

## CVVDG_02 (row 66) — Bảng chọn VV thiếu cột Tên DN / Ngày hoàn thành / Cảnh báo trùng đợt

**Bối cảnh testcase**

- Dòng Excel: 66, mã TC `CVVDG_02`.
- Nội dung kiểm tra: CB Nghiệp vụ mở bảng "Chọn vụ việc đánh giá" (FR-VI-05 / SCR item 41, Tab Thực hiện) — quan sát bộ cột của bảng.
- Expected trong file UAT:
  - Bảng chọn VV có thêm cột **Tên doanh nghiệp**, **Ngày hoàn thành**, **Cảnh báo trùng đợt**.
- Actual đối tác ghi: bảng thiếu các cột trên.

**Đối chiếu SRS v3.5**

- SCR item 41 mô tả control chọn VV là **C10 Multi-select** (search + multi-select), lọc VV `HOAN_THANH` trong kỳ thuộc phạm vi đơn vị — **không** liệt kê danh sách cột bắt buộc của bảng chọn.
- Cột "Tên DN" chỉ được SRS gắn cho **bảng chấm điểm** (SCR item 42) và **bảng tổng hợp báo cáo** (SCR item 47), không phải bảng chọn VV. "Ngày hoàn thành" không xuất hiện trong SCR nhóm VI.
- "Cảnh báo trùng đợt" là **hành vi** bắt buộc (VV đã thuộc đợt khác → cảnh báo, vẫn cho chọn) — SRS quy định là cảnh báo, **không** quy định phải là một **cột** trong bảng. Hành vi này kiểm riêng ở `CVVDG_03`.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:872` — SCR item 41 (C10 Multi-select, không liệt kê cột).
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:873` — cột "Tên DN" thuộc bảng chấm điểm (item 42).
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:449` — cảnh báo trùng đợt là hành vi (AC), không phải cột.

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_hn` / CB_NV_DP.
- Bảng "Chọn vụ việc đánh giá" có 5 cột: **Mã VV · Tên VV · Lĩnh vực · Trạng thái · Đã chọn?** — khớp y hệt bản đối tác chụp.
- Bảng đủ thông tin để chọn VV (mã, tên, lĩnh vực, trạng thái) → nghiệp vụ chọn đạt.
- Đối chiếu SRS: SCR không bắt buộc cột "Tên DN"/"Ngày hoàn thành" cho bảng chọn → app không vi phạm cột bắt buộc.
- Evidence: `../../reverify-audit/CVVDG_02/chon-vv-columns.png` · đối tác `../CVVDG_02.jpg`. Bảng điều kiện: `../../cond/CVVDG_02.md`.

**Kết luận QA**

- `CVVDG_02` không phải bug theo SRS v3.5 — SRS im lặng về danh sách cột bảng chọn VV; app render đủ 5 cột để thực hiện chọn.
- Cột "Tên DN" mà đối tác kỳ vọng thực chất thuộc bảng chấm điểm / báo cáo, không phải bảng chọn VV; "Ngày hoàn thành" không có trong SCR; "Cảnh báo trùng đợt" là hành vi (kiểm ở CVVDG_03), không phải cột.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt bộ cột chuẩn của bảng "Chọn vụ việc đánh giá":

- Giữ 5 cột hiện tại, hay bổ sung "Tên DN" / "Ngày hoàn thành" để hỗ trợ CB NV nhận diện VV.
- Verdict QA đề xuất: `Cần BA xác nhận` (SRS im lặng về cột); nếu BA yêu cầu thêm cột → owner Dev FE. Chưa gửi Dev.

---

## THDG_02 (row 69) — Chấm điểm: thiếu ô "Nhận xét từng tiêu chí"; ô nhận xét chung nhãn "Ghi chú" thay vì "Nhận xét tổng thể"

**Bối cảnh testcase**

- Dòng Excel: 69, mã TC `THDG_02`.
- Nội dung kiểm tra: CB Nghiệp vụ chấm điểm VV (FR-VI-06, Tab Thực hiện) — quan sát các ô nhận xét trong bảng chấm điểm.
- Expected trong file UAT: có ô **"Nhận xét từng tiêu chí"** (per tiêu chí) và ô nhận xét chung mang nhãn **"Nhận xét tổng thể"** (app đang để "Ghi chú").

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_hn` / CB_NV_DP, đợt DGHQ-B1 tab Chấm điểm.
- Mỗi dòng VV có: Mã VV · Tên DN · Lĩnh vực · Trạng thái · **1 ô điểm cho mỗi tiêu chí** (không có ô nhận xét riêng cho từng tiêu chí) · Điểm tổng · Xếp loại · **1 ô "Ghi chú"** (nhận xét chung / dòng).
- App có **một** ô nhận xét (nhãn "Ghi chú"), **không** có ô nhận xét theo từng tiêu chí — khớp với mô tả SCR item 42 (1 cột Nhận xét) nhưng thiếu so với FR-VI-06 Inputs.
- Evidence: `../../reverify-audit/THDG_02/cham-diem-cot-ghichu.png`. Bảng điều kiện: `../../cond/THDG_02.md`.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **FR-VI-06 Inputs**, chấm điểm có **hai** loại nhận xét tách biệt:
   - #4 `nhan_xet` — nhận xét **từng tiêu chí** (Max 1000 ký tự).
   - #5 `nhan_xet_tong_the` — nhận xét **tổng thể** (Max 2000 ký tự).

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:480` — `nhan_xet` (từng tiêu chí, Max 1000).
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:481` — `nhan_xet_tong_the` (Max 2000).

2. Nhưng **SCR item 42** (thiết kế màn chấm điểm) chỉ mô tả **một** cột nhận xét trong bảng:
   - "… / Nhận xét (textarea inline)" — 1 cột duy nhất, không tách theo tiêu chí.
   - SCR item 49 có thêm "Nhận xét chung" cho đợt — cũng chỉ là 1 ô chung, không phải per tiêu chí.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:873` — SCR item 42, một cột "Nhận xét (textarea inline)".
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:885` — SCR item 49, "Nhận xét chung".

> Ngoài ra: cả FR-VI-06 lẫn SCR **đều không** quy định nhãn hiển thị là "Ghi chú" hay "Nhận xét tổng thể" → wording nhãn ô cũng không có nguồn chốt.

**Câu hỏi cần BA xác nhận**

Màn Chấm điểm (FR-VI-06) cần có **mấy** ô nhận xét, và nhãn ô nhận xét chung là gì?

1. **Hướng 1 — theo FR-VI-06 Inputs:** phải có ô "Nhận xét từng tiêu chí" (per tiêu chí) **và** ô "Nhận xét tổng thể" → app hiện tại **thiếu** ô nhận xét theo tiêu chí.
2. **Hướng 2 — theo SCR item 42/49:** chỉ cần **một** ô nhận xét chung (textarea inline) → app hiện tại **đủ**, chỉ cần chốt nhãn ("Ghi chú" vs "Nhận xét tổng thể").

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth (FR-VI-06 Inputs vs SCR item 42).
- Tạm verdict cho `THDG_02`: `Cần BA xác nhận`.
- Nếu BA chọn Hướng 1 (FR Inputs): app `Vẫn lỗi` — thiếu ô nhận xét từng tiêu chí, owner `Dev FE` (+ Dev BE nếu cần field `nhan_xet` per tiêu chí).
- Nếu BA chọn Hướng 2 (SCR): app không phải lỗi cấu trúc — chỉ cần cập nhật nhãn ô cho khớp thiết kế + sửa lại expected testcase.

---

## LBCDG_02 (row 73) — Trường thông tin màn Lập báo cáo không giống thiết kế / SRS

**Bối cảnh testcase**

- Dòng Excel: 73, mã TC `LBCDG_02`.
- Nội dung kiểm tra: CB Nghiệp vụ lập báo cáo đánh giá (FR-VI-07, Tab Báo cáo) — quan sát bộ trường nhập của báo cáo.
- Expected trong file UAT:
  - Bộ trường báo cáo theo bản thiết kế của đối tác (khác với app hiện tại).
- Actual đối tác ghi: trường app không giống thiết kế.

**Đối chiếu SRS v3.5**

- FR-VI-07 sinh báo cáo theo **template nhóm VI / TT17/2025** với các cột số liệu (tự động + nhập tay). Các ô **nhập tay** SRS quy định: `kp_hoat_dong_khac` (KP hoạt động khác), `kp_xa_hoi_hoa` (KP xã hội hóa), `nhan_xet_tong_the`, `kien_nghi`; kèm các cột số liệu **tự động điền** (số TVV, tập huấn, hội nghị, VB, hồ sơ, kinh phí…).
- App hiện tại có 4 ô: Tiêu đề · Nội dung · Nhận xét tổng thể · Kiến nghị → **thiếu** 2 ô kinh phí (`kp_hoat_dong_khac`, `kp_xa_hoi_hoa`) và bộ số liệu TT17; **thừa** ô "Nội dung"/"Tiêu đề" không có trong SRS Inputs.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:551-554` — Inputs nhập tay: `kp_hoat_dong_khac`, `kp_xa_hoi_hoa`, `nhan_xet_tong_the`, `kien_nghi`.
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:538` — báo cáo theo "template nhóm VI với các cột số liệu".
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:563` — "Tự động điền các cột số liệu: số TVV, số tập huấn, số hội nghị, số VB, số hồ sơ, kinh phí".

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_hn` / CB_NV_DP.
- Form Chỉnh sửa báo cáo có 4 ô nhập: **Tiêu đề · Nội dung · Nhận xét tổng thể · Kiến nghị**.
- Phần "Số liệu tổng hợp" rút gọn (Tổng VV · Đã đánh giá · Điểm TB · Xếp loại) + biểu đồ radar/cột — không có 2 ô kinh phí và không có bảng số liệu TT17 đầy đủ.
- Đối chiếu SRS: app thiếu ô KP + bộ số liệu TT17; đồng thời cũng lệch bản thiết kế của đối tác.
- Evidence: `../../reverify-audit/LBCDG_02/edit-form-4-fields.png` · `../../reverify-audit/LBCDG_02/bao-cao-fields.png`. Bảng điều kiện: `../../cond/LBCDG_02.md`.

**Kết luận QA**

- `LBCDG_02` — app **lệch cả** thiết kế đối tác **lẫn** SRS FR-VI-07 (template TT17): thiếu 2 ô kinh phí + bộ số liệu TT17, thừa ô "Nội dung".
- Đây là quyết định **phạm vi thiết kế** (giữ bản rút gọn hay hiện thực đủ template TT17/2025) chứ không phải lỗi logic đơn lẻ → QA không tự chốt nên/không nên bổ sung, cần BA quyết bộ trường chuẩn.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt bộ trường/bố cục màn Lập báo cáo:

- Giữ bản rút gọn hiện tại, hay bổ sung đủ ô `kp_hoat_dong_khac` / `kp_xa_hoi_hoa` + bảng số liệu theo template TT17/2025 như SRS.
- Verdict QA đề xuất: `Cần BA xác nhận` (scope thiết kế). Nếu BA chốt theo SRS TT17 → owner `Dev FE + Dev BE`; nếu BA chấp nhận bản rút gọn → cập nhật lại expected testcase.

---

## LBCDG_04 (row 74) — Tên nút xuất báo cáo "Xuất báo cáo" khác thiết kế "Xuất Excel/XLSX"

**Bối cảnh testcase**

- Dòng Excel: 74, mã TC `LBCDG_04`.
- Nội dung kiểm tra: CB Nghiệp vụ xuất báo cáo (FR-VI-07, Tab Báo cáo) — quan sát nhãn nút xuất.
- Expected trong file UAT:
  - Nút xuất mang tên **"Xuất Excel"** (theo thiết kế / SCR "[Xuất XLSX]").
- Actual đối tác ghi: nút tên khác thiết kế.

**Đối chiếu SRS v3.5**

- SCR item 53 mô tả **2 nút** "[Xuất XLSX] / [Xuất DOCX]" (xuất theo mẫu TT17/2025). Đây là mô tả thiết kế control, không phải chuỗi nhãn bắt buộc theo Error Handling.
- FR-VI-07 Outputs #2 quy định file xuất là Excel (.xlsx) / Word (.docx) — yêu cầu **chức năng** xuất, không prescribe nhãn nút.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:889` — SCR item 53 "[Xuất XLSX] / [Xuất DOCX]".
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:595` — Outputs #2 "File xuất | Excel (.xlsx) / Word (.docx)".

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_hn` / CB_NV_DP.
- Thanh thao tác có **1 nút "Xuất báo cáo"**; bấm → tải file Excel (`.xlsx`) đúng chức năng.
- Chức năng xuất Excel chạy đúng; chỉ khác **nhãn nút** so với thiết kế/SCR (app gộp 1 nút tên chung).
- Evidence: `../../reverify-audit/LBCDG_04/nut-xuat-bao-cao.png`. Bảng điều kiện: `../../cond/LBCDG_04.md`.

**Kết luận QA**

- `LBCDG_04` không phải bug chức năng — xuất Excel chạy đúng; chỉ **lệch nhãn nút** so với SCR ("Xuất báo cáo" vs "Xuất XLSX"). SRS không prescribe chuỗi nhãn bắt buộc nên QA không chốt được đúng/sai nhãn.
- **Lưu ý tách bug:** việc **thiếu chức năng xuất Word (.docx)** đã tách riêng thành `BUG-LBCDG_05` (Open, `../../bug-reports/dghq/Pass-bug-report-DGHQ-batchB.md`) — case này chỉ xét **nhãn nút xuất Excel**.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt nhãn nút xuất:

- Giữ "Xuất báo cáo" (app), hay đổi theo SCR "Xuất XLSX" (và bổ sung "Xuất DOCX" khi có chức năng Word — xem BUG-LBCDG_05).
- Verdict QA đề xuất: `Cần BA xác nhận` (SRS không prescribe nhãn). Nếu BA chốt theo SCR → owner `Dev FE`; nếu chấp nhận app → cập nhật expected testcase.

---

## CVVDG_04 (row 68) — Message khi kỳ đánh giá không có VV: app "Không có vụ việc nào phù hợp" khác SRS "…hoàn thành trong kỳ đánh giá này"

**Bối cảnh testcase**

- Dòng Excel: 68, mã TC `CVVDG_04`.
- Nội dung kiểm tra: CB Nghiệp vụ mở màn Chọn vụ việc (FR-VI-05, Tab Thực hiện) khi kỳ đánh giá **không có vụ việc nào hoàn thành** — quan sát thông báo trạng thái rỗng.
- Expected trong file UAT:
  - Message báo "không có vụ việc trong kỳ" đúng chuỗi thiết kế.
- Actual đối tác ghi: message kỳ rỗng sai/khác mong đợi.

**Đối chiếu SRS v3.5**

- FR-VI-05 Error Handling E1 quy định: khi **0 VV hoàn thành trong kỳ**, hệ thống hiển thị cảnh báo `WRN-DG-VV-01` với nội dung **"Không có vụ việc nào hoàn thành trong kỳ đánh giá này"** (severity WARNING).
- Đây là chuỗi thông báo được SRS mô tả cụ thể cho tình huống kỳ rỗng — mang thông tin "hoàn thành trong kỳ đánh giá này" (giải thích lý do rỗng).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:442` — E1 `WRN-DG-VV-01` "Không có vụ việc nào hoàn thành trong kỳ đánh giá này".

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_hn` / CB_NV_DP.
- Tạo đợt B3 (DGHQ-B3) kỳ 01/01/2024–31/03/2024 (kỳ rỗng, 0 VV hoàn thành), đưa lên THUC_HIEN, mở tab Thực hiện.
- Bảng "Chọn vụ việc đánh giá" hiển thị "Đã chọn: 0 / 0 vụ việc", nút "Xác nhận chọn" **disabled**, và dòng empty-state **"Không có vụ việc nào phù hợp"**.
- Đối chiếu SRS: hành vi (xử lý kỳ rỗng, disable nút xác nhận) **đúng**; chỉ **chuỗi message khác** SRS — app dùng empty-state chung "Không có vụ việc nào phù hợp" thay vì chuỗi có ngữ cảnh "…hoàn thành trong kỳ đánh giá này".
- Evidence: `../../reverify-audit/CVVDG_04/message-khong-co-vv-phu-hop.png`. Bảng điều kiện: `../../cond/CVVDG_04.md`.

**Kết luận QA**

- `CVVDG_04` — hành vi xử lý kỳ rỗng **đúng**, không phải bug logic. Điểm khác biệt duy nhất là **chuỗi message** so với SRS `WRN-DG-VV-01`.
- SRS có mô tả chuỗi cụ thể, nhưng theo nguyên tắc describe-not-prescribe QA không tự chốt buộc app khớp đúng chuỗi ký tự → cần BA quyết.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt chuỗi thông báo khi kỳ đánh giá không có VV hoàn thành:

- Giữ "Không có vụ việc nào phù hợp" (app), hay đổi theo SRS "Không có vụ việc nào hoàn thành trong kỳ đánh giá này" (rõ ngữ cảnh hơn).
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA chốt theo SRS → owner `Dev FE`; nếu chấp nhận app → cập nhật lại expected của `CVVDG_04`.

---

## THDG_03 (row 70) — Nhập điểm vượt max: FE tự nắn về max im lặng (không message); BE validate đúng

**Bối cảnh testcase**

- Dòng Excel: 70, mã TC `THDG_03`.
- Nội dung kiểm tra: CB Nghiệp vụ chấm điểm VV (FR-VI-06, Tab Chấm điểm) — nhập điểm **vượt điểm tối đa** của tiêu chí (max=10).
- Expected trong file UAT:
  - Khi nhập điểm > max, hệ thống báo lỗi.
- Actual đối tác ghi: điểm vượt max bị **tự nắn về max, không báo lỗi**.

**Đối chiếu SRS v3.5**

- FR-VI-06 Error Handling E1: khi **điểm vượt điểm tối đa**, hệ thống phản hồi `ERR-DG-DG-01` "Điểm phải từ 0 đến {max}" (severity ERROR) — tức khi giá trị vượt max, hệ thống phải **từ chối và thông báo** cho người dùng.
- SRS mô tả yêu cầu là "reject + inform" khi điểm vượt max; không prescribe cụ thể phải chặn ở FE hay BE, cũng không cấm cơ chế clamp.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:517` — E1 `ERR-DG-DG-01` "Điểm phải từ 0 đến {max}".

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_hn` / CB_NV_DP, đợt B2 (DGHQ-B2) DANG_DANH_GIA, tab Chấm điểm.
- **Tầng FE:** nhập `15` vào ô tiêu chí max=10 → khi blur, AntD InputNumber **nắn về `10.0`** — KHÔNG hiển thị toast, KHÔNG error-message, không đánh dấu lỗi. (đúng như đối tác báo).
- **Tầng BE (verify 2nd method):** gọi trực tiếp `PUT /api/v1/ke-hoach-danh-gias/{id}/ket-quas` với điểm=15 (vượt max) → **422 `ERR-DG-SC-06`** "Điểm cho tiêu chí 'Mức độ hoàn thành vụ việc' vượt quá điểm tối đa (10)"; dữ liệu giữ nguyên 10/8/9/7 (không bị ghi sai).
- Đối chiếu SRS: ràng buộc 0..max **được enforce đúng cả 2 tầng** (FE clamp + BE reject). Điểm khác biệt duy nhất so với SRS E1: khi FE nắn giá trị, **không hiển thị message tường minh** cho user (user gõ 15 nhưng bị đổi về 10 mà không được báo).
- Evidence: `../../reverify-audit/THDG_03/diem-15-clamp-10-khong-message.png`. Bảng điều kiện: `../../cond/THDG_03.md`.

**Kết luận QA**

- `THDG_03` — hệ thống **KHÔNG chấp nhận điểm sai** (FE clamp + BE `ERR-DG-SC-06`), không phải lỗi logic/dữ liệu. Đây không phải "chấm điểm sai được lưu".
- Vấn đề còn lại thuần **UX**: FE nắn im lặng về max thay vì hiện message như SRS E1 mô tả. Việc silent-clamp là mẫu chuẩn của number-input; QA không tự chốt đây có phải defect hay không.
- Lưu ý: mã lỗi BE thực tế là `ERR-DG-SC-06` (khác `ERR-DG-DG-01` trong SRS) nhưng nội dung tương đương ("vượt quá điểm tối đa") — theo describe-not-prescribe, khác mã không tính là bug.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hành vi khi nhập điểm vượt max:

- Chấp nhận FE tự nắn về max (im lặng) — vì ràng buộc vẫn được đảm bảo (FE clamp + BE reject); hay yêu cầu FE hiện message tường minh "Điểm phải từ 0 đến {max}" khi phát hiện nhập vượt max.
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA yêu cầu message tường minh → owner `Dev FE` (BE đã validate đúng, không cần sửa); nếu chấp nhận clamp → cập nhật lại expected của `THDG_03`.

---

## TPDBC_03 (row 77) — Trình phê duyệt BC ở sai state: message "Báo cáo đánh giá không tồn tại" khác SRS "Đợt không ở trạng thái đã lập BC"

**Bối cảnh testcase**

- Dòng Excel: 77, mã TC `TPDBC_03`.
- Nội dung kiểm tra: CB Nghiệp vụ trình phê duyệt báo cáo (FR-VI-08) khi đợt **không ở trạng thái đã lập BC** (không ở BAO_CAO) — quan sát thông báo lỗi.
- Expected trong file UAT:
  - Thông báo lỗi đúng trạng thái/đúng wording khi trình BC sai state.
- Actual đối tác ghi: message sai state / sai wording.

**Đối chiếu SRS v3.5**

- FR-VI-08 Precondition: đợt phải ở trạng thái **BAO_CAO** và BC đã được lưu mới được trình phê duyệt.
- FR-VI-08 Error Handling E1: khi **đợt không ở BAO_CAO**, hệ thống phản hồi `ERR-DG-TR-01` "Đợt không ở trạng thái đã lập BC" (severity ERROR) — yêu cầu nghiệp vụ là **chặn thao tác + báo cho user biết đợt chưa ở trạng thái lập BC**.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:631` — Precondition "Đợt ở trạng thái BAO_CAO".
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:670` — E1 `ERR-DG-TR-01` "Đợt không ở trạng thái đã lập BC".

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_hn` / CB_NV_DP.
- Gọi trực tiếp `POST /api/v1/ke-hoach-danh-gias/{id}/bao-cao/submit` trên đợt B3 đang ở **THUC_HIEN** (chưa lập BC) → **404 `ERR-VAL-BC-DG-02`** "Báo cáo đánh giá không tồn tại".
- Trên UI: ở trạng thái THUC_HIEN **không có nút "Trình phê duyệt"** (UI gate nút — đã xác nhận ở `TPDBC_02`), nên user thao tác bình thường không chạm tới lỗi này; lỗi chỉ xuất hiện khi gọi API trực tiếp ở sai state.
- Đối chiếu SRS: hành vi **đúng** (chặn trình BC ở sai state + UI ẩn nút). Điểm khác biệt: message app "Báo cáo đánh giá không tồn tại" (`ERR-VAL-BC-DG-02`) khác chuỗi SRS E1 "Đợt không ở trạng thái đã lập BC" (`ERR-DG-TR-01`). Ở THUC_HIEN chưa có BC nên "báo cáo không tồn tại" cũng hợp lý về logic, chỉ khác góc diễn đạt.
- Evidence: `../../reverify-audit/TPDBC_03/bao-cao-tab-thuc-hien-gate-nut-trinh.png` (tab Báo cáo ở THUC_HIEN hiện "Chưa hoàn thành đánh giá", không có nút Trình phê duyệt) + API 404 `ERR-VAL-BC-DG-02`. Bảng điều kiện: `../../cond/TPDBC_03.md`.

**Kết luận QA**

- `TPDBC_03` — hành vi chặn trình BC ở sai state **đúng**, UI gate nút nên user không gặp lỗi trong luồng thường; không phải bug logic.
- Điểm khác biệt là **wording/framing** message so với SRS E1 (report-không-tồn-tại vs đợt-sai-state). SRS quy định chuỗi E1 nhưng theo describe-not-prescribe QA không tự chốt buộc khớp chuỗi.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt message khi trình BC ở sai state:

- Giữ "Báo cáo đánh giá không tồn tại" (app, đúng logic THUC_HIEN chưa có BC), hay đổi theo SRS E1 "Đợt không ở trạng thái đã lập BC" cho nhất quán khung thông báo state.
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA chốt theo SRS → owner `Dev BE`; nếu chấp nhận app → cập nhật lại expected của `TPDBC_03`.

---

_Các case Batch B còn lại đã chốt ngoài file này: `CVVDG_03` → Open (`../../bug-reports/dghq/Pass-bug-report-DGHQ-batchB.md`); `THDG_05` → **Closed / PASS** (re-verify 22/07/2026 sau dev fix — `../../bug-reports/thdg/Pass-bug-report-THDG_05.md`). Toàn bộ 15 case Batch B (rows 65–79) đã verify xong._
