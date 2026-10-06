# BA confirmation needed — QTHT Batch 7 (Cấu hình hệ thống / SLA — SCR-VIII-06) — 2026-07-21

> Gom các testcase QA không tự chốt verdict được (bất đồng ĐẶC TẢ giữa SRS v3.5 / thực tế web / kỳ vọng đối tác) trên màn **Cấu hình hệ thống** Tab 1 "Thời hạn xử lý (SLA)". Màn này là **MÀN HÌNH MỚI v2.1** với spec churn nặng (4→3→2 tab qua 2 lần BA chốt 2026-05-07).
>
> - Account verify: `admin` / QTHT (Tab 1 SLA chỉ QTHT truy cập — SRS dòng 1731). URL: `/quan-tri/cau-hinh`.
> - Tool: Chrome DevTools MCP. Env verify `18.143.165.120.nip.io` hiển thị **giống hệt** env đối tác `htpldn-uat.ospgroup.vn` (cùng 6 dòng SLA, cùng cột, cùng toggle disabled).
> - Citation: `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:LINE` (đã mở file verify số dòng thực).

**Tóm tắt verdict batch 7:** 4 case BA confirm (152, 153, 154, 155) + 1 case Open (156 — xem `../../bug-reports/qtht/Pass-bug-report-qtht-batch7.md`).

| Row | Mã TC | Vấn đề | Verdict |
|---|---|---|---|
| 152 | QLCHTHXLHS_02 | Số thẻ tab (3 app vs 2 SRS vs 4 đối tác) | BA confirm |
| 153 | QLCHTHXLHS_03 | Cấu trúc cột bảng SLA (redesign + 2 vi phạm) | BA confirm |
| 154 | QLCHTHXLHS_05 | Toggle "Gửi email" không bật/tắt inline | BA confirm |
| 155 | QLCHTHXLHS_06 | Toggle "Gửi TB app" không bật/tắt inline | BA confirm |

---

## QLCHTHXLHS_02 — Số thẻ tab màn Cấu hình hệ thống (bất đồng 3 chiều: SRS 2 · web 3 · đối tác 4)

**Bối cảnh testcase**

- Dòng Excel: 152, mã TC `QLCHTHXLHS_02`.
- Nội dung kiểm tra: QTHT mở màn Cấu hình hệ thống (`/quan-tri/cau-hinh`), đếm số thẻ tab.
- Expected trong file UAT: đối tác kỳ vọng **4 thẻ** — SLA / Phân công / Mẫu phản hồi / Quy trình.
- Actual đối tác ghi: hệ thống hiển thị **3 thẻ** — SLA / Mẫu phản hồi / **Quản lý ngày lễ**.

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, account `admin` (QTHT). URL `/quan-tri/cau-hinh`.
- Web hiển thị đúng **3 tab**: "Thời hạn xử lý (SLA)" · "Mẫu phản hồi" · "Quản lý ngày lễ" (khớp actual đối tác).
- Evidence: `../../reverify-audit/QLCHTHXLHS_02/QLCHTHXLHS_02-tabs-table.png`.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo SCR-VIII-06, màn = **2 tab**: Tab 1 "Thời hạn xử lý / SLA", Tab 2 "Mẫu phản hồi". Đã **bỏ** Tab "Phân công mặc định" (Q11) + Tab "Quy trình hỗ trợ" (Hướng A) — BA chốt 2026-05-07.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1724` — "Loại màn hình: Tab Page (2 tabs)"
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1728` — "Đã bỏ: Tab 4 Quy trình hỗ trợ ... Tab 2 Phân công mặc định"
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1742` — "Tab 1: Thời hạn xử lý / SLA — Tab 2: Mẫu phản hồi"

2. Nhưng web thực tế có **tab thứ 3 "Quản lý ngày lễ"** — SCR-VIII-06 (2 tab) **không liệt kê** tab này (chức năng quản lý ngày nghỉ lễ nằm ở FR riêng, không thuộc 2 tab của màn Cấu hình theo spec hiện hành).

**Câu hỏi cần BA xác nhận**

Màn Cấu hình hệ thống phải có **bao nhiêu tab** và **tab nào**?

1. **Theo SRS v3.5 (2 tab):** SLA + Mẫu phản hồi. → tab "Quản lý ngày lễ" là **thừa** so với spec.
2. **Theo thực tế web (3 tab):** SLA + Mẫu phản hồi + Quản lý ngày lễ → cần BA bổ sung "Quản lý ngày lễ" vào SCR-VIII-06 nếu đây là thiết kế mới.
3. **Kỳ vọng đối tác (4 tab, gồm Phân công + Quy trình):** là **spec CŨ đã bị bỏ** (BA chốt 2026-05-07) → không còn hiệu lực.

**Đề xuất QA tạm thời**

- Tạm verdict `QLCHTHXLHS_02`: **BA confirm**. Chưa gửi Dev tới khi BA chốt số tab chuẩn.
- Kỳ vọng "4 thẻ" của đối tác dựa trên spec cũ (Phân công/Quy trình đã bỏ) → **đề nghị cập nhật expected testcase** theo spec hiện hành.
- Nếu BA giữ SRS 2 tab: tab "Quản lý ngày lễ" cần gỡ khỏi màn (owner Dev FE) hoặc bổ sung vào SCR-VIII-06.
- Nếu BA chấp nhận 3 tab: cập nhật SCR-VIII-06 thành 3 tab.

---

## QLCHTHXLHS_03 — Cấu trúc cột bảng Tab SLA (redesign inline→modal + 2 điểm vi phạm SRS)

**Bối cảnh testcase**

- Dòng Excel: 153, mã TC `QLCHTHXLHS_03`.
- Nội dung kiểm tra: QTHT xem bảng Tab 1 "Thời hạn xử lý (SLA)", đối chiếu các cột.
- Expected/actual đối tác: bảng SLA khác spec — Loại yêu cầu tách 2 cột · 6 giá trị (spec 4) · Cảnh báo mức 1&2 gộp "Vùng cảnh báo" · thiếu cột Quá hạn(%)/Số ngày BS tối đa · thừa "Hệ số quá hạn".

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, account `admin` (QTHT).
- Bảng thực tế có **8 cột**: `Loại yêu cầu` (mã enum) · `Tên loại` · `Thời hạn (ngày LV)` · `Vùng cảnh báo` (1 thanh gộp) · `Hệ số quá hạn` (=2) · `Email` (toggle) · `Thông báo app` (toggle) · `Hành động` (nút Sửa).
- **6 dòng** loại YC: HOI_DAP · HOI_DAP_PHUC_TAP · HO_SO_CHI_TRA · HO_SO_HT · HO_SO_TT · VU_VIEC.
- Giá trị CB mức 1/mức 2 vẫn sửa được trong modal "Sửa" (Ngưỡng cảnh báo 1=50, Ngưỡng cảnh báo 2=100).
- Evidence: `../../reverify-audit/QLCHTHXLHS_03/QLCHTHXLHS_03-cols-right-clean.png`.

**Đối chiếu SRS v3.5 — tách từng ý con**

| # | Đối tác phản ánh | SRS v3.5 | Web thực tế | Đánh giá QA |
|---|---|---|---|---|
| a | Loại yêu cầu tách 2 cột | SCR dòng 1749: 1 cột "Loại yêu cầu". Nhưng FR Inputs có cả `loai_yeu_cau` + `ten_loai` (dòng 465–466) | 2 cột (mã + tên loại) | Thiết kế thêm hợp lý (đủ hơn) — **cần BA chốt** |
| b | 6 giá trị (spec 4) | SCR 1749 + FR 465: 4 giá trị (HOI_DAP/VU_VIEC/HO_SO_HT/HO_SO_TT) | 6 giá trị (thêm HOI_DAP_PHUC_TAP, HO_SO_CHI_TRA) | Thêm 2 loại SLA ngoài enum SRS — **cần BA chốt** có bổ sung vào spec |
| c | Gộp "Vùng cảnh báo" | SCR dòng 1751–1752: 2 cột riêng "CB mức 1 (%)" + "CB mức 2 (%)" | 1 thanh "Vùng cảnh báo" (hiển thị); giá trị vẫn sửa trong modal | Khác cách hiển thị, giá trị vẫn cấu hình được — **cần BA chốt** |
| d | Thiếu cột Quá hạn(%) | SCR dòng 1753: cột readonly "Quá hạn (%)" = 100% | Giá trị 100% nhúng trong thanh Vùng cảnh báo, không có cột riêng | Khác cách hiển thị — **cần BA chốt** |
| e | **Thiếu cột Số ngày BS tối đa** | SCR 11a dòng 1756 + FR Inputs #10 dòng 474 + AC dòng 515: bắt buộc cho loại ≠ HOI_DAP (default 5) | **Không có** ở cả bảng lẫn modal | **QA khẳng định vi phạm** — thiếu trường cấu hình bắt buộc |
| f | **Thừa "Hệ số quá hạn"** | SCR dòng 1759 + FR dòng 471 (BA chốt 2026-05-07 Q5): `qua_han_he_so` **ngầm, KHÔNG hiển thị UI** | Hiện cột "Hệ số quá hạn" = 2 (và cả trong modal) | **QA khẳng định vi phạm** — hiện field mà BA đã chốt phải ẩn |

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1749` (4 giá trị, 1 cột loại)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1751` · `:1752` (CB mức 1 / mức 2 = 2 cột riêng)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1753` (cột Quá hạn %)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1756` (cột Số ngày BS tối đa)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1759` + `:471` (Hệ số quá hạn ngầm, không UI — BA Q5)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:474` (so_ngay_bo_sung_toi_da — BA chốt 2026-05-13) + `:515` (AC cột Số ngày BS tối đa)

**Câu hỏi cần BA xác nhận**

Bảng Tab SLA đã được **redesign** so với SRS (bảng read-only + nút "Sửa" mở modal, thay vì inline-edit + 1 nút [Lưu cấu hình]). BA chốt hướng nào cho các điểm a–d (cấu trúc cột)?
- 2 điểm **e** (thiếu Số ngày BS tối đa) và **f** (thừa Hệ số quá hạn) là **vi phạm rõ SRS + BA đã chốt trước** → QA đề xuất **chuyển Dev fix** (đã ghi chi tiết ở `Pass-bug-report-qtht-batch7.md` BUG-QLCHTHXLHS_07).

**Đề xuất QA tạm thời**

- Tạm verdict `QLCHTHXLHS_03`: **BA confirm** (vừa có điểm cần BA chốt thiết kế a–d, vừa có 2 vi phạm rõ e–f).
- Nếu BA giữ SRS: e (thêm cột/trường Số ngày BS) + f (ẩn Hệ số quá hạn) → owner Dev FE. a–d tùy BA chốt giữ SRS hay chấp nhận redesign.

---

## QLCHTHXLHS_05 & QLCHTHXLHS_06 — Toggle "Gửi email" / "Gửi TB app" không bật/tắt được trên dòng (redesign inline → modal-edit)

**Bối cảnh testcase**

- Dòng Excel: 154 (`QLCHTHXLHS_05` — Email) · 155 (`QLCHTHXLHS_06` — Thông báo app).
- Nội dung kiểm tra: QTHT thử bật/tắt toggle "Gửi email" / "Gửi TB app" **trực tiếp trên dòng** bảng SLA.
- Actual đối tác ghi: hệ thống **KHÔNG cho bật/tắt trên dòng** (video hiện con trỏ 🚫 khi hover toggle).

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, account `admin` (QTHT).
- Cả 12 toggle (6 dòng × 2 cột Email/Thông báo app) đều ở trạng thái `disabled` (đo DOM: `disabled=true` toàn bộ) → **không bật/tắt được inline** (khớp phản ánh đối tác + con trỏ 🚫 trong video).
- **Tuy nhiên**, giá trị Email/Thông báo app **sửa được** trong modal "Sửa cấu hình SLA" (2 switch "Gửi email cảnh báo" / "Gửi thông báo in-app" ở trạng thái enabled, bật/tắt được, lưu qua [Đồng ý]).
- Evidence: `../../reverify-audit/QLCHTHXLHS_05/QLCHTHXLHS_05-toggle-disabled-inline.png` (disabled inline) + `...-modal-editable.png` (sửa được trong modal). Tương tự `../../reverify-audit/QLCHTHXLHS_06/`.

**Đối chiếu SRS v3.5**

- SCR-VIII-06 dòng 1754 (Gửi email) + 1755 (Gửi TB app): mô tả là **cột toggle** (hành vi = toggle) trong bảng SLA → thiết kế gốc là **inline toggle**.
- SCR dòng 1757: có nút [Lưu cấu hình] chung → thiết kế gốc: sửa inline nhiều dòng rồi Lưu 1 lần.
- Web đã **redesign**: bảng read-only + nút "Sửa" từng dòng mở modal; toggle Email/app chỉ sửa trong modal.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1754` (Cột Gửi email — toggle)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1755` (Cột Gửi TB app — toggle)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1757` (nút [Lưu cấu hình])

**Câu hỏi cần BA xác nhận**

SRS thiết kế Tab SLA dạng **inline-edit** (toggle + input trực tiếp trên bảng). Web đã đổi sang **read-only table + modal-edit** (bật/tắt Email/Thông báo app trong modal "Sửa", không sửa được trên dòng). Chức năng cấu hình **KHÔNG bị chặn** (vẫn đổi được qua modal), chỉ khác cách tương tác. BA chốt:
1. **Bắt buộc inline toggle** theo SRS → hiện web là lỗi, owner Dev FE.
2. **Chấp nhận modal-edit** (sửa qua nút Sửa) → cập nhật SCR-VIII-06 + cập nhật expected testcase 154/155.

**Đề xuất QA tạm thời**

- Tạm verdict `QLCHTHXLHS_05` + `QLCHTHXLHS_06`: **BA confirm**. Chưa gửi Dev tới khi BA chốt inline vs modal.
- Actual đối tác (không bật/tắt inline) là **đúng thực tế** → không Reject; nhưng chức năng cấu hình Email/app không mất (sửa qua modal) → không phải bug chặn luồng, để BA chốt thiết kế.
