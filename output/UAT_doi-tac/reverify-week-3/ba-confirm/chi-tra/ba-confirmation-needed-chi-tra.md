# BA confirmation needed — Chi trả chi phí — UAT tuần 3 — 2026-07-20

> Nội dung được tách theo module từ file BA confirm đa module của UAT tuần 3. Các section đối chiếu SRS, evidence và câu hỏi BA được giữ nguyên.

## QLHSDNHTCP_03 - Cột cảnh báo thời hạn (SLA) danh sách Hồ sơ Chi trả có phải đúng 4 nhãn mức + tên thiết kế không

**Bối cảnh testcase**

- Dòng Excel: 16, mã TC `QLHSDNHTCP_03` (module Chi trả chi phí, FR-V.II-02 / UC69, màn SCR-V.II-01).
- Nội dung kiểm tra: cột dữ liệu trong bảng danh sách hồ sơ chi trả.
- Actual đối tác ghi: "Cột thông tin **Mức cảnh báo thời hạn** không giống với thiết kế".

**Đối chiếu SRS v3.5**

| # | App thực tế (đã seed 10 hồ sơ, CB_NV_TW) | Đặc tả v3.5 | Vị trí |
|---|---|---|---|
| 1 | Cột tên "**Hạn xử lý**" | Thành phần "SLA" (component #16) | `srs-fr-06-chi-tra.md:935` |
| 2 | Giá trị đếm ngược + mã màu: "Còn 4 ngày LV" (xanh), "Quá hạn X ngày LV" (đỏ ≤6, đen ≥11) | 4 mức cảnh báo rời: `warning` "Sắp đến hạn" · `urgent` "Cần xử lý gấp" · `critical` "Sát hạn" · `overdue` "Quá hạn" | `srs-fr-06-chi-tra.md:1383-1392` (BR-CALC-03) |

→ App **có** cột cảnh báo SLA + phân biệt mức qua màu (đạt yêu cầu chức năng, nhãn tiếng Việt theo §1041) nhưng **không hiện đủ 4 nhãn mức rời** như BR-CALC-03 và **tên khác** thiết kế đối tác. SRS quy định thành phần "SLA" + "4 mức cảnh báo" nhưng **không quy định chính xác** chữ tiêu đề cột lẫn format giá trị (đếm ngược vs nhãn rời). Evidence đối tác (env `ospgroup.vn`, build cũ) cũng hiện đếm ngược "Quá hạn 58 ngày LV" → cả 2 build đều đếm ngược, khác thiết kế discrete-levels.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:935` (component #16 SLA)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:1383-1392` (BR-CALC-03 — 4 ngưỡng cảnh báo)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:1041` (Quy tắc: nhãn tiếng Việt, không viết tắt)

**Kết quả verify UI hiện tại**

- Cột "Hạn xử lý" = index 7 trong bảng, giá trị đếm ngược ("Còn N ngày LV" / "Quá hạn N ngày LV"), màu nền: xanh (35,120,4) còn hạn · đỏ (207,19,34) quá hạn ≤6 ngày · đen (0,0,0) quá hạn ≥11 ngày. Cột hiển thị đầy đủ (bị cột "Hành động" sticky che trong screenshot là do cuộn ngang bình thường, KHÔNG phải tràn/đè).
- Evidence: `../../reverify-audit/QLHSDNHTCP_03-web-danhsach-cot.png` · `../../reverify-audit/QLHSDNHTCP_03/audit.md`.

**Câu hỏi cần BA xác nhận**

1. Cột cảnh báo thời hạn (SLA) có **bắt buộc hiển thị đúng 4 nhãn mức rời** theo BR-CALC-03 (Sắp đến hạn / Cần xử lý gấp / Sát hạn / Quá hạn) không, hay dạng "đếm ngược + mã màu" hiện tại được chấp nhận?
2. Tên cột chuẩn là "Mức cảnh báo thời hạn" (thiết kế đối tác) hay "Hạn xử lý" (app) — hay chỉ cần tiếng Việt rõ nghĩa là đạt?

**Đề xuất QA tạm thời**

- **QLHSDNHTCP_03**: verdict **`BA confirm`**. App đáp ứng yêu cầu chức năng (có cột SLA + cảnh báo qua màu, tiếng Việt) → không phải Open; quan sát đối tác đúng (format khác thiết kế) → không Reject. SRS không quy định chính xác tên cột + format giá trị → BA chốt có ép đúng 4 nhãn mức / tên thiết kế không. Chi tiết: `../../reverify-audit/QLHSDNHTCP_03/audit.md`.

## QLHSDNHTCP_09 - Tiêu đề trang màn Chi tiết hồ sơ chi trả có phải theo thiết kế "Chi tiết hồ sơ #{mã}" không

**Bối cảnh testcase**

- Dòng Excel: 18, mã TC `QLHSDNHTCP_09` (module Chi trả chi phí, FR-06 / UC69, màn SCR-V.II-02).
- Nội dung kiểm tra: tiêu đề trang + thanh tiến trình (stepper) màn Chi tiết hồ sơ chi trả.
- Actual đối tác ghi: "Tiêu đề trang không giống với thiết kế" (kỳ vọng tiêu đề "Chi tiết hồ sơ #{mã hồ sơ}").

**Đối chiếu SRS v3.5 (SCR-V.II-02)**

| # | App thực tế (CT-SEED-101, CB_NV_TW) | Đặc tả v3.5 | Vị trí |
|---|---|---|---|
| 1 | Tiêu đề trang (h1) = TÊN DN "Công ty TNHH Seed Publishable" | Component #3 "Header info" liệt kê Mã hồ sơ / Tên DN / Quy mô / Trạng thái / SLA — KHÔNG quy định chuỗi tiêu đề h1 | `srs-fr-06-chi-tra.md:979` |
| 2 | Breadcrumb "Trang chủ / Chi trả chi phí / Chi tiết" (thiếu #mã) | Component #1 "Chi tiết #{ma_ho_so}" | `srs-fr-06-chi-tra.md:977` |
| 3 | Stepper 6 bước: Tiếp nhận → Kiểm tra → Đánh giá → Thẩm định → Phê duyệt → Thanh toán | Component #4 stepper 6 bước đúng thứ tự | `srs-fr-06-chi-tra.md:980` |

→ Tiêu đề trang = tên DN **tái hiện đúng** như đối tác báo (bug reproduces), NHƯNG SRS component #3 chỉ liệt kê các trường header, **không quy định** chuỗi tiêu đề h1 phải là "Chi tiết hồ sơ #{mã}". App đủ trường bắt buộc. Stepper (component #4) đúng 6 bước → phần thanh tiến trình KHÔNG phải lỗi. Phát hiện thêm: breadcrumb thiếu "#{ma_ho_so}" so với component #1.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:977` (component #1 Breadcrumb "Chi tiết #{ma_ho_so}")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:979` (component #3 Header info — không quy định chuỗi tiêu đề h1)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:980` (component #4 Stepper 6 bước)

**Kết quả verify UI hiện tại**

- Màn Chi tiết CT-SEED-101 (`/chi-tra/47b1f556-...`): h1 = "Công ty TNHH Seed Publishable"; breadcrumb "Trang chủ / Chi trả chi phí / Chi tiết"; stepper đủ 6 bước; header đủ Mã HS / Quy mô / Trạng thái.
- Evidence: `../../reverify-audit/QLHSDNHTCP_09-web-tieude-stepper.png` · `../../reverify-audit/QLHSDNHTCP_09/audit.md`.

**Câu hỏi cần BA xác nhận**

1. Tiêu đề trang màn Chi tiết có **bắt buộc** theo thiết kế "Chi tiết hồ sơ #{mã}" không, hay dùng tên DN làm tiêu đề (các trường header đủ) được chấp nhận?
2. Breadcrumb có **bắt buộc** kèm "#{ma_ho_so}" theo component #1 không (app đang hiển thị "Chi tiết" thiếu #mã)?

**Đề xuất QA tạm thời**

- **QLHSDNHTCP_09**: verdict **`BA confirm`**. Tiêu đề = tên DN tái hiện đúng đối tác báo → không Reject; SRS không quy định chuỗi tiêu đề h1 → không có SRS violation rõ ràng → không tự Open. Stepper đúng 6 bước → phần này không phải lỗi. Breadcrumb thiếu #mã gộp vào câu hỏi 2. Chi tiết: `../../reverify-audit/QLHSDNHTCP_09/audit.md`.

## QLHSDNHTCP_10 - Trường SLA trên thanh tổng quan màn Chi tiết có phải đúng 4 nhãn mức BR-CALC-03 không

**Bối cảnh testcase**

- Dòng Excel: 19, mã TC `QLHSDNHTCP_10` (module Chi trả chi phí, FR-06 / UC69, màn SCR-V.II-02).
- Nội dung kiểm tra (Mô tả): "Nhóm 0 — Thanh thông tin tổng quan hồ sơ".
- Actual đối tác ghi: "Mức cảnh báo thời hạn không giống với thiết kế".

**Đối chiếu SRS v3.5 (SCR-V.II-02 + BR-CALC-03)**

| # | App thực tế (CT-SEED-103, Yêu cầu bổ sung, CB_NV_TW) | Đặc tả v3.5 | Vị trí |
|---|---|---|---|
| 1 | Thanh tổng quan đủ trường: Mã HS / Quy mô DN / Trạng thái / SLA; layout gọn không tràn/đè | Component #3 "Header info": Mã hồ sơ / Tên DN / Quy mô / Trạng thái / SLA | `srs-fr-06-chi-tra.md:979` |
| 2 | Trường "SLA" = "Quá hạn 3 ngày LV" (badge đỏ, đếm ngược) | SLA = "4 mức cảnh báo": warning "Sắp đến hạn" / urgent "Cần xử lý gấp" / critical "Sát hạn" / overdue "Quá hạn" | `srs-fr-06-chi-tra.md:1383-1392` (BR-CALC-03) |

→ Thanh tổng quan đủ trường bắt buộc + tiếng Việt + không tràn/đè (đạt chức năng). Riêng trường SLA hiển thị **đếm ngược + màu** thay vì **4 nhãn mức rời** như BR-CALC-03. SRS không quy định chính xác format hiển thị SLA. **Cùng gốc câu hỏi với QLHSDNHTCP_03** (list screen), khác ở đây là thanh tổng quan màn Chi tiết (label "SLA" khớp SRS #3). Ghi chú kỹ thuật: enum BE `mucDoCanhBao` = BINH_THUONG/SAP_HET_HAN/QUA_HAN/QUA_HAN_NGHIEM_TRONG cũng khác 4 mức BR-CALC-03 (data model, không phải phần đối tác phản ánh).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:979` (component #3 Header info — trường SLA)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:1383-1392` (BR-CALC-03 — 4 mức cảnh báo)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:1041` (nhãn tiếng Việt)

**Kết quả verify UI hiện tại**

- Màn Chi tiết CT-SEED-103 (Yêu cầu bổ sung, deadline 15/07): thanh tổng quan SLA badge đỏ "Quá hạn 3 ngày LV". Hồ sơ CHO_TIEP_NHAN (CT-SEED-101) SLA "Còn 4 ngày LV" (chưa quá hạn). Format đếm ngược đồng nhất mọi state.
- Evidence: `../../reverify-audit/QLHSDNHTCP_10-web-thanh-tongquan-sla.png` · `../../reverify-audit/QLHSDNHTCP_10/audit.md` · `condition-table.md` (0 GAP).

**Câu hỏi cần BA xác nhận**

1. Trường SLA trên thanh tổng quan màn Chi tiết có **bắt buộc hiển thị đúng 4 nhãn mức rời** theo BR-CALC-03 (Sắp đến hạn / Cần xử lý gấp / Sát hạn / Quá hạn) không, hay dạng "đếm ngược + màu" hiện tại được chấp nhận? (Trùng câu hỏi 1 của QLHSDNHTCP_03 — nếu BA chốt 1 lần thì áp dụng cho cả list + detail.)

**Đề xuất QA tạm thời**

- **QLHSDNHTCP_10**: verdict **`BA confirm`**. Thanh tổng quan đủ trường + không tràn/đè → không Open toàn case; SLA format đếm ngược tái hiện đúng đối tác báo → không Reject; SRS không quy định chính xác format → BA chốt (gộp với _03). Chi tiết: `../../reverify-audit/QLHSDNHTCP_10/audit.md`.

## QLHSDNHTCP_19 - Danh sách Chi trả có bắt buộc hỗ trợ sắp xếp theo click tên cột không

**Bối cảnh testcase**

- Dòng Excel: 23, mã TC `QLHSDNHTCP_19` (module Chi trả chi phí, FR-06 / UC69, màn SCR-V.II-01 — Danh sách).
- Nội dung kiểm tra (Mô tả): "Sắp xếp danh sách theo cột".
- Actual đối tác ghi: "Hệ thống không thực hiện sắp xếp khi nhấn vào tên cột". Expected đối tác: "Hệ thống sắp xếp danh sách theo cột đó, luân phiên tăng dần / giảm dần qua mỗi lần bấm".

**Đối chiếu SRS v3.5 (SCR-V.II-01 + sibling modules)**

| # | App thực tế (`/chi-tra/danh-sach`, CT-SEED-101→110, CB_NV_TW) | Đặc tả v3.5 | Vị trí |
|---|---|---|---|
| 1 | Bấm tên cột (Mã HS / Số tiền đề nghị / Trạng thái / Ngày nộp) → danh sách KHÔNG đổi thứ tự. DOM: 0 cột có marker sắp xếp (không class sort / aria-sort / column-sorter) | Bảng cột danh sách: cột "Hành vi" của mọi cột = "—" (không mô tả tương tác click-sort) | `srs-fr-06-chi-tra.md:918-938` |
| 2 | Danh sách mặc định theo ngày cập nhật giảm dần | "Sắp xếp mặc định: ngày cập nhật DESC" (chỉ default, không click-sort) | `srs-fr-06-chi-tra.md:958` |
| 3 | — | Module Vụ việc HTPL: cột có hành vi sắp xếp | `srs-fr-05:1654` |
| 4 | — | Module Quản trị hệ thống: cột có hành vi sắp xếp | `srs-fr-10:1573` |
| 5 | — | Module Hỏi đáp pháp lý: cột có hành vi sắp xếp | `srs-fr-02:1043` |

→ Xét RIÊNG module Chi trả: SRS SCR-V.II-01 không mô tả click-sort ("Hành vi=—", chỉ default sort ngày cập nhật DESC) → app đúng spec module này. NHƯNG các module sibling (Vụ việc / Quản trị / Hỏi đáp) đều có click-sort → hệ thống không đồng nhất cross-module.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:918-938` (SCR-V.II-01 bảng cột — "Hành vi=—")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:958` (sắp xếp mặc định ngày cập nhật DESC)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05...:1654` · `srs-fr-10...:1573` · `srs-fr-02...:1043` (sibling modules có click-sort)

**Kết quả verify UI hiện tại**

- Bấm header "Số tiền đề nghị" → thứ tự dòng giữ nguyên (CT-SEED-108/109/110/101/102...), giá trị số tiền không sắp (8.000.000 / 7.000.000 / 8.500.000 / 6.000.000 / 9.000.000). `anySorterActive`=false, `any_sortable_marker`=0.
- Evidence: `../../reverify-audit/QLHSDNHTCP_19-web-cot-khong-sort.png` · `../../reverify-audit/QLHSDNHTCP_19/audit.md`.

**Câu hỏi cần BA xác nhận**

1. Click-sort theo tên cột có phải **yêu cầu chung toàn hệ thống** (khi đó màn Danh sách Chi trả thiếu = bug cần fix), hay chỉ áp dụng cho các màn có "Hành vi=sắp xếp" trong SRS (khi đó Chi trả đúng spec, đóng case)?

**Đề xuất QA tạm thời**

- **QLHSDNHTCP_19**: verdict **`BA confirm`**. App khớp SRS Chi trả (không đủ căn cứ Open) nhưng lệch chuẩn các module sibling (không thể Reject dứt khoát) → BA chốt phạm vi yêu cầu click-sort. Chi tiết: `../../reverify-audit/QLHSDNHTCP_19/audit.md`.

<!-- DẠNG A — QA đã kết luận, cần BA phản hồi đối tác. Gộp 6 TC sibling (_23→_28) cùng 1 gốc: expected đối tác theo bố cục "6 Nhóm" của thiết kế đối tác, SRS v3.5 dùng danh sách trường phẳng. -->
