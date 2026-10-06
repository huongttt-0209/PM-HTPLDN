# SRS chuẩn đối chiếu — 14 case BCTK_QA

**Nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Ngày trích:** 2026-08-07 · **Phạm vi:** chỉ trích dẫn spec, KHÔNG kết luận Pass/Fail.

> **Ghi chú chung về số dòng:** phần lớn trích dẫn trong đề bài lệch **+3 dòng** so với bản chốt `srs-v3.5/` (do đề bài lấy từ bản `input/`). Riêng khối màn hình SCR-IX-01 lệch **+5**, và Phụ lục E §H8 lệch **+44**. Mọi số dòng dưới đây đều mở file đọc trực tiếp.

> **Bối cảnh áp cho cả nhóm — vai trò được vào màn Báo cáo:**
> - `srs-fr-11-bao-cao.md:79` — "**Kiểm tra vai trò trước:** chỉ CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP) được truy cập chức năng báo cáo. Vai trò khác (kể cả QTHT) → chặn ngay ở cửa vào, không mở màn hình. Sau đó kiểm phạm vi theo đơn vị `[BA chốt 2026-08-06]`"
> - `srs-fr-11-bao-cao.md:1046` — "**Điều kiện vào màn — áp cho TOÀN BỘ bảng dưới đây** `[BA chốt 2026-08-06]`: người dùng phải có vai trò **Cán bộ Nghiệp vụ** hoặc **Cán bộ Phê duyệt** (TW/BN/ĐP). Vai trò khác — kể cả **Quản trị hệ thống** — **không vào được màn này**; mục menu "Báo cáo thống kê" bị **ẩn** theo quy ước M-05 (ẩn, không làm mờ)."
> - `srs-fr-11-bao-cao.md:127` — "**Given** người dùng vai trò Quản trị hệ thống **When** đăng nhập **Then** **không thấy** mục menu "Báo cáo thống kê" (ẩn theo M-05, không làm mờ) `[BA chốt 2026-08-06]`"

---

## BCTK_QA01

**Yêu cầu case đòi:** Khi hệ thống từ chối thao tác vì lý do quyền, thông báo cho người dùng phải bằng tiếng Việt và cho biết đó là vấn đề phân quyền.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:117` — "| E7 | Không có quyền | ERR-RPT-05 | "Bạn không có quyền xem báo cáo này" | ERROR |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:120` — "| E10 | Không có quyền **thực hiện thao tác xuất tệp** (vai trò ngoài CB NV / CB PD) | ERR-RPT-08 | "Bạn không có quyền thực hiện thao tác này" (câu chuẩn `srs-fr-05-vu-viec.md` §3.E — Thông báo người dùng) `[BA chốt 2026-08-06]` | ERROR |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:128` — "**Given** vai trò ngoài CB Nghiệp vụ / CB Phê duyệt **When** gọi thẳng dịch vụ xuất tệp ở tầng máy chủ (không có đường bấm từ giao diện vì màn đã ẩn) **Then** từ chối với `ERR-RPT-08` — "Bạn không có quyền thực hiện thao tác này" `[BA chốt 2026-08-06]`"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:4697` — "| I18N-01 | Ngôn ngữ chính | Tiếng Việt là ngôn ngữ duy nhất cho giao diện CMS | ✅ CĐT xác nhận |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1339` — "| BAO_CAO | R | CRU* | CRU* | CRU* | RU* | RU* | RU* | — | — | — | — |" (tiêu đề cột ở `:1300` — QTHT chỉ `R`; DN / NHT / TVV / CG là `—`)

**Đối chiếu số dòng đề bài:**
- `:117` (ERR-RPT-05) — **khớp**.
- `srs-v3.5.md:1335` (ma trận quyền) — **lệch** (đề bài 1335 → thực tế **1339**; dòng 1335 là `VAI_TRO`).
- Đề bài **chưa nhắc dòng :120 và :128** — đây mới là dòng đặc tả riêng cho thao tác **xuất tệp** (`ERR-RPT-08`), sát với thao tác của case hơn `ERR-RPT-05` (dành cho hành vi *xem* báo cáo).

**Xác nhận mã lỗi:** grep `ERR-PERM-SYS` trên toàn thư mục `srs-v3.5/` → **0 kết quả**. Mã `ERR-PERM-SYS-00-01` không tồn tại trong bản chốt.

**Chốt để đo:** Đọc thẳng chữ hiển thị trên khung thông báo tại thời điểm bị từ chối. Nếu là tiếng Việt và cho biết người dùng không có quyền (theo câu ở `:120` cho thao tác xuất, hoặc `:117` cho thao tác xem) thì đạt; nếu là chuỗi tiếng Anh trần hoặc mã kỹ thuật thì chưa đạt. Phần "vai trò QTHT có được xuất không" đã có `:79` / `:1046` / `:127` trả lời — đó là câu hỏi khác, không lẫn vào câu chữ.

---

## BCTK_QA02

**Yêu cầu case đòi:** Chừng nào màn hình còn đang hiện kết quả báo cáo thì người dùng vẫn phải xuất được tệp, không phụ thuộc số lần đã bấm [Xem báo cáo].

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1057` — "| 8 | action-bar | Nút Xuất Excel | button | "Xuất Excel (.xlsx)" → xuất theo format TT17/2025 | click → auto-download | Sau khi đã "Xem báo cáo" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]` |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1058` — "| 9 | action-bar | Nút Xuất PDF | button | "Xuất PDF (.pdf)" → xuất theo khung trình bày TT17/2025 (không dùng Mẫu 21a/21b) | click → auto-download | Sau khi đã "Xem báo cáo" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]` |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:124` — "**Given** CB nhấn "Xuất Excel" **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (Phụ lục E §H8)"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1060` — "| 11 | content | Bảng dữ liệu | table | ... | sort → reorder | Khi có dữ liệu |"

**Đối chiếu số dòng đề bài:** **lệch cả 3** — đề bài `:123` → thực tế **:124** (dòng 123 là AC về xem báo cáo, không phải xuất Excel); đề bài `:1052` → thực tế **:1057**; đề bài `:1053` → thực tế **:1058**.

**Điểm SRS im lặng:** grep `disable | vô hiệu | làm mờ | khoá nút | nhấn lại | lần thứ` trên `srs-fr-11-bao-cao.md` → chỉ ra 2 dòng nói về ẩn menu theo M-05, **không có dòng nào cho phép khoá nút Xuất theo số lần bấm [Xem báo cáo]**. Điều kiện hiển thị của hai nút chỉ gồm đúng hai vế: đã xem báo cáo + đúng vai trò.

**Chốt để đo:** Trên màn còn đang hiện khối kết quả (có số liệu, đúng vai trò CB NV/CB PD), thử bấm [Xuất Excel]/[Xuất PDF] sau lần [Xem báo cáo] thứ 2 và thứ 3. Xuất được tệp = đạt; nút không bấm được trong khi bảng dữ liệu vẫn hiện = lệch điều kiện ở `:1057`/`:1058`.

---

## BCTK_QA03

**Yêu cầu case đòi:** Phần thống kê theo người hỗ trợ phải nêu được họ tên người hỗ trợ, và người dùng phải lọc lại được theo đúng người đó.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:264` — "| 5 | theo_nht[] | structured | Luôn | {nht_id, ho_ten, so_vv, qua_han} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:247` — "| 1 | nht_id | identifier | N | FK → NGUOI_DUNG | — | Chọn |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:252` — "**Dimensions:** Đơn vị, NHT phân công, SLA (bình thường / sắp hết hạn / quá hạn / quá hạn nghiêm trọng)"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1071` — "| | UC126 | BC Vụ việc đang hỗ trợ | NHT phụ trách, Mức SLA | Bar (snapshot) |"

**Đối chiếu số dòng đề bài:** **lệch cả 2** — đề bài `:261` → thực tế **:264**; đề bài `:244` → thực tế **:247**.

**Điểm cần lưu ý về tên thực thể:** `:247` ghi nguồn là `FK → NGUOI_DUNG`, nhưng bản chốt v3.5 không có thực thể tên `NGUOI_DUNG`; hồ sơ Người hỗ trợ nằm ở `NGUOI_HO_TRO` (`srs-v3.5.md:1219` — "| 16a | NGUOI_HO_TRO | tvv | Cán bộ HTPL DNNVV (NHT) theo NĐ 55/2019 Đ.7 — 1:1 với TAI_KHOAN ... | 500 |"), tài khoản nằm ở `TAI_KHOAN`. Đây là chỗ đặt tên chưa thống nhất trong SRS, **không** làm thay đổi yêu cầu `ho_ten` ở `:264`.

**Chốt để đo:** Đọc cột họ tên của từng dòng trong bảng thống kê theo người hỗ trợ. Mọi dòng có mã người hỗ trợ mà hồ sơ hệ thống đã có họ tên thì bảng phải in đúng họ tên đó (`:264`, điều kiện "Luôn"); và mã đó phải xuất hiện trong danh sách chọn của bộ lọc "NHT phụ trách" (`:247` + `:1071`) để lọc lại được.

---

## BCTK_QA04

**Yêu cầu case đòi:** Phần thống kê theo đơn vị phải luôn có mặt, kể cả khi người dùng đã lọc về đúng một đơn vị.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:219` — (FR-IX-02, BC Vụ việc đã tiếp nhận) "| 4 | theo_don_vi[] | structured | Luôn | {don_vi, ten, so_luong} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:265` — (FR-IX-03, BC Vụ việc đang hỗ trợ) "| 6 | theo_don_vi[] | structured | Luôn | {don_vi, ten, so_luong, qua_han} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:308` — (FR-IX-04, BC Vụ việc đã hoàn thành) "| 6 | theo_don_vi[] | structured | Luôn | {don_vi, ten, so_luong} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:341` — (FR-IX-05, BC Vụ việc theo thời gian — dùng làm đối chứng) "| 2 | theo_don_vi[] | structured | Luôn | {don_vi, ten, trend_data[]} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1097` — "Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file..."

**Đối chiếu số dòng đề bài:** **lệch cả 3** — đề bài `:216` → thực tế **:219**; `:262` → **:265**; `:305` → **:308**.

**SRS IM LẶNG (phần ngoại lệ):** grep `Luôn` trong 3 khối FR nêu trên không tìm thấy dòng nào miễn trừ `theo_don_vi[]` khi bộ lọc thu về một đơn vị. Điều kiện chỉ ghi đúng một chữ "Luôn", không kèm ngoại lệ.

**Chốt để đo:** Với cùng kỳ, chạy 2 lượt (lọc 1 đơn vị và Toàn quốc) rồi đếm số dòng dữ liệu ở phần "Theo đơn vị" trên màn và trong tệp xuất. Lượt lọc 1 đơn vị có ≥1 dòng nêu đúng tên đơn vị đó = đạt; ra 0 dòng trong khi tổng vụ việc vẫn > 0 = lệch điều kiện "Luôn".

---

## BCTK_QA05

**Yêu cầu case đòi:** Báo cáo chi phí theo loại hình DN phải tách số liệu theo từng quy mô doanh nghiệp có phát sinh trong kỳ, và bộ lọc theo quy mô phải trả về đúng hồ sơ của quy mô đó.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:826` — "| 1 | loai_dn | text | N | SIEU_NHO / NHO / VUA | — | Chọn |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:830` — "**Dimensions:** Loại DN, Mức hỗ trợ (100%/30%/10%), Số HS, Tổng chi phí, Trần so sánh"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:837` — "| 2 | ten_loai_dn | text | Luôn | Siêu nhỏ / Nhỏ / Vừa |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:839-842` — "| 4 | so_ho_so | number | Luôn | Số hồ sơ | · | 5 | tong_chi_phi | money | Luôn | Tổng chi phí | · | 6 | tran_chi_phi | money | Luôn | Trần chi phí theo NĐ55 | · | 7 | chenh_lech | money | Luôn | Tổng CP - Trần |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:845` — "**Given** CB tạo BC **When** hiển thị **Then** bảng phân theo loại DN + mức hỗ trợ + so sánh trần chi phí"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:1301` — "| quy_mo_dn | text | Y | CHECK IN ('SIEU_NHO','NHO','VUA') | | Quy mô DN |" (quy mô là thuộc tính của chính hồ sơ chi trả — nguồn đối chiếu)

**Đối chiếu số dòng đề bài:** **lệch cả 2** — đề bài `:823` → thực tế **:826** (dòng 823 là dòng trống); đề bài `:831-839` → thực tế **:830** (Dimensions) + **:834-842** (bảng Output đặc thù).

**SRS IM LẶNG:** grep `nhất quán | đối chiếu số liệu giữa | cùng nguồn dữ liệu` trên `srs-fr-11-bao-cao.md` → **0 kết quả**. SRS **không** phát biểu quy tắc hai báo cáo khác nhau phải cho ra cùng con số. Vế "hai báo cáo phải khớp nhau" trong đề bài là suy luận nghiệp vụ, không có dòng spec. Vế đo được nằm ở `:826` + `:837` + `:845` (báo cáo FR-IX-18 phải tách theo từng quy mô, lọc theo quy mô phải chạy) và nguồn đối chiếu là `quy_mo_dn` trên hồ sơ chi trả (`srs-fr-06-chi-tra.md:1301`).

**Chốt để đo:** Lấy danh sách hồ sơ chi trả đã thanh toán trong kỳ kèm `quy_mo_dn` của từng hồ sơ làm mốc. Báo cáo FR-IX-18 phải có đủ dòng cho mọi quy mô xuất hiện trong danh sách đó; và chọn bộ lọc "Loại DN = Nhỏ" phải ra đúng những hồ sơ có `quy_mo_dn = NHO`, không ra thông báo trống.

---

## BCTK_QA06

**Yêu cầu case đòi:** BC Chi phí chi trả hỗ trợ phải có phần chia theo kỳ, hiện cả trên màn và trong tệp xuất.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:709` — "Báo cáo tổng chi phí chi trả hỗ trợ đã thanh toán trong kỳ, phân theo đơn vị, kỳ."
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:717` — "**Dimensions:** Kỳ, Đơn vị, Tổng HS, Tổng chi phí, Trung bình/HS"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:727` — "| 5 | theo_ky[] | structured | Luôn | {ky, tong_cp, so_hs} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:721-727` — bảng Output đặc thù FR-IX-15 có đúng 5 mục: `tong_chi_phi` (723), `tong_ho_so` (724), `trung_binh_ho_so` (725), `theo_don_vi[]` (726), `theo_ky[]` (727) — **không có mục chia theo quy mô doanh nghiệp**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:713` — "**Template:** Kế thừa TPL-REPORT-FULL (không bổ sung input)" (FR-IX-15 không có bộ lọc `loai_dn`)

**Đối chiếu số dòng đề bài:** **lệch cả 3** — đề bài `:706` → thực tế **:709**; `:714` → **:717**; `:718-724` → thực tế **:721-727** (mục #5 nằm ở dòng **727**).

**Chốt để đo:** Trên màn và trong tệp xuất của BC Chi phí chi trả hỗ trợ, tìm khối liệt kê theo kỳ gồm nhãn kỳ + tổng chi phí + số hồ sơ. Có mặt = đạt điều kiện "Luôn" ở `:727`. Phần chia theo quy mô DN đang hiện thêm là mục nằm ngoài bảng `:721-727` — ghi nhận riêng, không dùng để bù cho phần theo kỳ.

---

## BCTK_QA07

**Yêu cầu case đòi:** Giống QA02, đo trên BC Chi phí theo thời gian — nút Xuất phải dùng được chừng nào báo cáo còn hiện số liệu.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1057` — "| 8 | action-bar | Nút Xuất Excel | button | ... | Sau khi đã "Xem báo cáo" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]` |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1058` — "| 9 | action-bar | Nút Xuất PDF | button | ... | Sau khi đã "Xem báo cáo" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]` |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:124` và `:125` — AC "Given CB nhấn 'Xuất Excel'/'Xuất PDF' When click Then tải file..."

**Đối chiếu số dòng đề bài:** **lệch cả 2** — đề bài `:1052` → thực tế **:1057**; đề bài `:1053` → thực tế **:1058**. (Dòng 1052 thực tế là Dropdown loại BC, dòng 1053 là Bộ lọc kỳ BC.)

**SRS IM LẶNG:** không có dòng nào trong `srs-fr-11-bao-cao.md` đặt điều kiện khoá nút Xuất theo số lần nhấn [Xem báo cáo] (grep `disable | vô hiệu | làm mờ | khoá nút | nhấn lại | lần thứ` chỉ trả về 2 dòng nói về ẩn menu M-05).

**Chốt để đo:** Đúng như QA02 nhưng trên loại "BC Chi phí theo thời gian": sau lần [Xem báo cáo] thứ 2 trở đi, khối kết quả còn hiện số liệu thì hai nút Xuất phải còn bấm được và tải được tệp.

---

## BCTK_QA08

**Yêu cầu case đòi:** Cán bộ phải có đường chọn khoảng 12 tháng trên giao diện và nhận về biểu đồ đường 12 điểm.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:858` — "Báo cáo trend chi phí theo thời gian dạng line chart."
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:864` — "**Công thức:** Tính tổng chi phí theo kỳ thời gian. Biểu đồ line chart"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:872` — "| 1 | trend_data[] | structured | Luôn | {ky_label, tong_chi_phi, so_ho_so} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:877` — "**Given** CB chọn 12 tháng **When** tạo BC **Then** hiển thị line chart 12 điểm trend chi phí"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:70-71` — "| 2 | tu_ngay | datetime | Y | <= den_ngay | — | Chọn / Auto | · | 3 | den_ngay | datetime | Y | >= tu_ngay | — | Chọn / Auto |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1053` — "| 4 | filter-bar | Bộ lọc kỳ BC | select + date-picker | Tuần / Tháng / Quý / Năm / Khoảng tùy chọn. Validate: tu_ngay <= den_ngay; khoảng <= 366 ngày (trừ Năm) | change → auto tính ngày | Luôn hiển thị |"

**Đối chiếu số dòng đề bài:** **lệch cả 4** — đề bài `:855` → thực tế **:858**; `:861` → **:864**; `:869` → **:872**; `:874` → **:877**.

**SRS IM LẶNG (một phần):** SRS không quy định mức gom nhóm khi người dùng chọn kỳ "Khoảng tùy chọn" — `:872` chỉ nói `ky_label`, `:1053` chỉ nói "change → auto tính ngày" mà không nói ngày sau khi auto tính còn sửa được hay không. Yêu cầu đo được nằm ở `:877` (chọn 12 tháng → 12 điểm) kết hợp `:70-71` (tu_ngay/den_ngay có nguồn "Chọn", tức người dùng chọn được).

**Chốt để đo:** Trên giao diện, tìm đường đưa báo cáo về mốc 12 tháng (chọn kỳ Tháng rồi kéo khoảng 01/01–31/12, hoặc tổ hợp tương đương) rồi đếm số điểm trên biểu đồ đường và số dòng trong bảng. Ra 12 điểm/12 dòng = đạt `:877`; mọi tổ hợp trên giao diện đều chỉ ra 1 điểm = chưa có đường đi mà `:877` đòi.

---

## BCTK_QA09

**Yêu cầu case đòi:** Dòng "Kỳ báo cáo" in trong tệp xuất phải là chữ tiếng Việt như người dùng thấy, không phải mã nội bộ.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1097` — "Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file. Riêng PDF bổ sung khung văn bản hành chính: quốc hiệu + tên cơ quan ở đầu trang, ngày ký + họ tên cán bộ xuất báo cáo + chỗ con dấu ở cuối trang (không có dòng chức danh)..."
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1053` — "| 4 | filter-bar | Bộ lọc kỳ BC | select + date-picker | Tuần / Tháng / Quý / Năm / Khoảng tùy chọn. ... |" (nhãn hiển thị cho người dùng)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:69` — "| 1 | ky_bao_cao | text | Y | TUAN / THANG / QUY / NAM / KHOANG | — | Chọn |" (giá trị **nội bộ**)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:95` — "| 2 | ky_bao_cao | text | Luôn | Kỳ đã chọn |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:86` — "Nếu xuất PDF: tạo file .pdf theo khung văn bản hành chính Thông tư 17/2025 — khổ A4, font Times New Roman cỡ 13; **đầu trang** có quốc hiệu, tiêu ngữ và tên cơ quan ban hành..."
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:4697` — "| I18N-01 | Ngôn ngữ chính | Tiếng Việt là ngôn ngữ duy nhất cho giao diện CMS | ✅ CĐT xác nhận |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:4703` — "| I18N-07 | Thuật ngữ kỹ thuật | Sử dụng tiếng Anh cho thuật ngữ kỹ thuật trong code, API (field names, endpoint paths). Giao diện hiển thị tiếng Việt | 🟡 Đề xuất |"

**Đối chiếu số dòng đề bài:**
- `:86` (PDF theo TT17/2025) — **khớp**.
- `:1092` → **lệch**, thực tế **:1097** (dòng 1092 là dòng trống cuối bảng mapping 23 loại BC).
- `:1048` → **lệch**, thực tế **:1053** (dòng 1048 là dòng tiêu đề cột của bảng thành phần màn hình).

**Chốt để đo:** Mở tệp Excel và PDF vừa xuất, đọc dòng "Kỳ báo cáo" ở phần đầu. Nếu in nhãn người dùng ("Khoảng tùy chọn" / "Khoảng") thì đạt; nếu in mã nội bộ ở `:69` (`KHOANG`, `THANG`...) thì lệch — bởi `:1097` xếp thông tin kỳ vào phần header dành cho người đọc và `:95` gọi giá trị này là "Kỳ đã chọn".

---

## BCTK_QA10

**Yêu cầu case đòi:** Khi người dùng chọn một lĩnh vực, báo cáo trên màn và tệp xuất chỉ còn dữ liệu thuộc lĩnh vực đó.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:369` — (FR-IX-06, BC Lớp đào tạo đang diễn ra) "| 2 | linh_vuc_id | identifier | N | FK → DANH_MUC | — | Chọn |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:373` — "**Dimensions:** Đơn vị, Hình thức, Lĩnh vực"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:452` — (FR-IX-08, BC Số lượng CG/TVV) "| 2 | linh_vuc_id | identifier | N | FK → DANH_MUC | — | Chọn |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:457` — "**Dimensions:** Đơn vị, Loại (TVV/CG), Lĩnh vực chuyên môn"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1285` — "| BR-DATA-06 | Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ FR-IX | Báo cáo nhóm IX có xuất PDF | Test export limit |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1055` — "| 6 | filter-bar | Bộ lọc đặc thù | select/text-input (dynamic) | Tùy loại BC: lĩnh vực PL, trạng thái, kênh tiếp nhận, loại TVV, đợt ĐG, khóa học, loại DN... | change → filter | Khi loại BC cần lọc đặc thù |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:180` — (mẫu câu AC lọc, FR-IX-01) "**Given** CB chọn lĩnh vực cụ thể **When** filter **Then** chỉ hiển thị HD thuộc lĩnh vực đó"

**Đối chiếu số dòng đề bài:** **lệch cả 4** — đề bài `:366` → thực tế **:369**; `:449` → **:452**; `:370` → **:373**; `:1280` → **:1285**.

**Chốt để đo:** Cùng phiên, cùng kỳ, chỉ đổi bộ lọc lĩnh vực. So số liệu màn (Tổng / TVV / CG hoặc Tổng khóa học) giữa lượt không lọc và lượt lọc; rồi so nội dung tệp xuất hai lượt. Con số và tệp phải đổi theo lĩnh vực đã chọn (`:369`/`:452` + `:1285`). Trùng khít với lượt không lọc = bộ lọc không tác dụng.

---

## BCTK_QA11

**Yêu cầu case đòi:** Những nhóm dữ liệu SRS ghi điều kiện "Luôn" phải có mặt cả trên màn lẫn trong tệp xuất.

**Trích SRS:**
- BC Lớp đào tạo đang diễn ra (FR-IX-06):
  - `…/srs-fr-11-bao-cao.md:383` — "| 5 | theo_linh_vuc[] | structured | Luôn | {linh_vuc, ten, so_luong} |"
  - `…/srs-fr-11-bao-cao.md:384` — "| 6 | ds_khoa_hoc[] | structured | Luôn | {ma_kh, ten_kh, hinh_thuc, ngay_bd, so_hv} |"
- BC Lớp đào tạo đã diễn ra (FR-IX-07):
  - `…/srs-fr-11-bao-cao.md:424` — "| 4 | theo_hinh_thuc[] | structured | Luôn | {hinh_thuc, so_kh, so_hv} |"
  - `…/srs-fr-11-bao-cao.md:425` — "| 5 | theo_ky[] | structured | Luôn | {ky, so_kh, so_hv} |"
- BC Đánh giá hiệu quả HTPL (FR-IX-09):
  - `…/srs-fr-11-bao-cao.md:510` — "| 5 | theo_dot[] | structured | Luôn | {dot_id, ten_dot, diem_tb} |"
- BC Chất lượng đào tạo (FR-IX-10):
  - `…/srs-fr-11-bao-cao.md:551` — "| 5 | theo_don_vi[] | structured | Luôn | {don_vi, ten, diem_tb, ty_le_dat} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1285` — BR-DATA-06 "File xuất theo bộ lọc hiện tại..." (áp "Toàn bộ FR-IX")

(Đường dẫn đầy đủ của 6 dòng trên: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`)

**Đối chiếu số dòng đề bài:** **lệch cả 6, đều +3** — `:380` → **:383**; `:381` → **:384**; `:421` → **:424**; `:422` → **:425**; `:507` → **:510**; `:548` → **:551**.

**Chốt để đo:** Với kỳ có dữ liệu, rà đủ ba nơi (màn hình, dữ liệu máy chủ trả về, tệp xuất) cho từng nhóm nêu trên. Nhóm nào vắng mặt ở cả ba nơi = lệch điều kiện "Luôn" của đúng dòng SRS tương ứng. Lưu ý phân biệt "vắng nhóm" với "nhóm có mặt nhưng rỗng do kỳ không có dữ liệu".

---

## BCTK_QA12

**Yêu cầu case đòi:** Hai lần xuất tệp trong cùng một phút phải nhận tên tệp khác nhau nhờ hậu tố tự thêm.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:6760` — "| **H8** | Tên tệp xuất thống nhất | Áp cho **tệp kết xuất dữ liệu** phần mềm sinh ra theo yêu cầu người dùng (xuất danh sách, xuất báo cáo), ở **mọi nhóm chức năng**. … **Khuôn:** `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. … Phần giờ-phút bắt buộc để xuất hai lần trong cùng ngày không đè tệp. Tổng độ dài tối đa **255 ký tự**; … **Trùng tên (hai lần xuất trong cùng phút) thì tự thêm hậu tố `_1`, `_2`** — theo cách đã dùng cho tệp tải lên tại `srs-fr-02-hoi-dap.md:108`. `[BA chốt 2026-08-06 — nâng phạm vi quyết định 2026-08-04 của Nhóm IX thành quy ước chung]` | BẮT BUỘC |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:85` — "Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo **Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]`"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:124` — AC "…tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (Phụ lục E §H8)"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1097` — "…Tên tệp cả hai định dạng theo **Phụ lục E §H8** — `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`"

**Đối chiếu số dòng đề bài:** **lệch** — đề bài `srs-v3.5.md:6716` → thực tế **:6760** (lệch +44, lớn hơn hẳn mức +3/+5 của các case khác).

**Chốt để đo:** Xuất hai lần trong cùng một phút và đọc tên tệp do **máy chủ** đặt (không đọc tên trình duyệt tự đổi thành " (1)"). Lần thứ hai có hậu tố `_1` = đạt `:6760`; hai lần trùng khít tên = lệch. Phần còn lại của khuôn tên (`{TenTep}` PascalCase + `YYYYMMDD_HHmm`) đo riêng cũng theo `:6760`.

---

## BCTK_QA13

**Yêu cầu case đòi:** Bảng thống kê theo kỳ của BC Số lượng chương trình hỗ trợ phải hiện số chương trình của kỳ đó.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:914` — "| 5 | theo_ky[] | structured | Luôn | {ky, so_ct} |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:904` — "**Dimensions:** Đơn vị, Trạng thái CT, Kỳ"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1060` — "| 11 | content | Bảng dữ liệu | table | Nhóm theo chiều phân tích tùy loại BC. Cột sắp xếp. Sticky header. Hàng tổng cộng (bold) | sort → reorder | Khi có dữ liệu |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1062` — "| 13 | content | Empty state | empty | "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" | — | Khi không có dữ liệu |"

**Đối chiếu số dòng đề bài:** **khớp** — đề bài `:914` đúng bằng dòng thực tế.

**SRS IM LẶNG:** cột "Tỷ lệ" mà màn đang hiện **không** nằm trong khai báo `theo_ky[]` ở `:914` (chỉ có `{ky, so_ct}`). SRS không quy định cột tỷ lệ cho FR-IX-20 — không lấy ô Tỷ lệ trống làm căn cứ.

**Chốt để đo:** Cùng một lượt xem, đối chiếu ô "Số lượng" của dòng kỳ trên màn với `soCt` trong dữ liệu máy chủ trả về và với ô tương ứng ở phần "Theo kỳ" của tệp xuất. Ba nơi cùng một số = đạt `:914`; màn để trống trong khi hai nơi kia có số = lệch ở khâu hiển thị.

---

## BCTK_QA14

**Yêu cầu case đòi:** BC Chương trình theo thời gian không được còn chỉ tiêu số doanh nghiệp ở bất kỳ chỗ nào.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1021` — "| 1 | trend_data[] | structured | Luôn | {ky_label, so_ct} `[CTTLV_04 chốt 2026-07-24: bỏ so_dn — CSV UC146 chỉ "thống kê chương trình theo thời gian", không có số DN; không có mô hình CT↔DN. Cùng lý do FR-IX-22.]` |"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1017-1023` — bảng Output đặc thù FR-IX-23 chỉ có 3 mục: `trend_data[]` (1021), `chart_type` (1022), `tong_ct` (1023) — **không có mục nào về số doanh nghiệp**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:964` — (FR-IX-22, báo cáo anh em) "Báo cáo chương trình theo lĩnh vực: hàng = lĩnh vực, cột = số CT. `[CTTLV_04 chốt 2026-07-24: bỏ cột "Số DN tham gia" — CSV UC145 chỉ yêu cầu "thống kê số lượng chương trình theo lĩnh vực"; không có mô hình dữ liệu CT↔DN và không có định nghĩa nghiệp vụ "DN tham gia chương trình" (NĐ55 — chương trình do cơ quan tổ chức, DN thụ hưởng hoạt động).]`"
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1026` — "**Given** CB chọn 12 tháng **When** tạo BC **Then** hiển thị biểu đồ trend số CT theo thời gian" (chỉ số CT)

**Đối chiếu số dòng đề bài:** **khớp cả 2** — đề bài `:1021` và `:964` đúng bằng dòng thực tế.

**Chốt để đo:** Rà 4 chỗ trên BC Chương trình theo thời gian: thẻ tổng, chú giải biểu đồ, cột trong bảng "Theo kỳ", và tệp xuất. Không còn chỉ tiêu số DN ở cả 4 = đạt quyết định `CTTLV_04` ghi tại `:1021`. Dùng FR-IX-22 (`:964`, cùng quyết định) làm đối chứng cho thấy quyết định đã được triển khai ở nơi khác.

---

## Tổng hợp đối chiếu số dòng

| Case | Trích dẫn đề bài | Kết quả | Ghi chú |
|---|---|---|---|
| QA01 | `fr-11:117` · `v3.5:1335` | khớp / **lệch** | 1335 → **1339**; thiếu `:120` + `:128` (ERR-RPT-08 dành cho thao tác xuất tệp) |
| QA02 | `fr-11:123` · `:1052` · `:1053` | **lệch cả 3** | → **:124** · **:1057** · **:1058** |
| QA03 | `fr-11:261` · `:244` | **lệch cả 2** | → **:264** · **:247** |
| QA04 | `fr-11:216` · `:262` · `:305` | **lệch cả 3** | → **:219** · **:265** · **:308** |
| QA05 | `fr-11:823` · `:831-839` | **lệch cả 2** | → **:826** · **:830 + :834-842** |
| QA06 | `fr-11:706` · `:714` · `:718-724` | **lệch cả 3** | → **:709** · **:717** · **:721-727** |
| QA07 | `fr-11:1052` · `:1053` | **lệch cả 2** | → **:1057** · **:1058** |
| QA08 | `fr-11:855` · `:861` · `:869` · `:874` | **lệch cả 4** | → **:858** · **:864** · **:872** · **:877** |
| QA09 | `fr-11:1092` · `:1048` · `:86` | 2 lệch / 1 khớp | → **:1097** · **:1053**; `:86` khớp |
| QA10 | `fr-11:366` · `:449` · `:370` · `:1280` | **lệch cả 4** | → **:369** · **:452** · **:373** · **:1285** |
| QA11 | `fr-11:380/381/421/422/507/548` | **lệch cả 6** | → **:383/384/424/425/510/551** |
| QA12 | `v3.5:6716` | **lệch** | → **:6760** (lệch +44) |
| QA13 | `fr-11:914` | **khớp** | — |
| QA14 | `fr-11:1021` · `:964` | **khớp cả 2** | — |

## Các điểm SRS im lặng (không bịa dòng cho đủ)

| Case | Điều SRS không quy định | Từ khoá đã grep |
|---|---|---|
| QA02 · QA07 | Không có dòng nào cho phép khoá nút Xuất theo số lần nhấn [Xem báo cáo]; điều kiện hiển thị chỉ gồm "đã Xem báo cáo" + đúng vai trò | `disable`, `vô hiệu`, `làm mờ`, `khoá nút`, `khóa nút`, `nhấn lại`, `lần thứ` (trên `srs-fr-11-bao-cao.md`) |
| QA04 | Không có ngoại lệ nào miễn trừ `theo_don_vi[]` khi bộ lọc thu về một đơn vị | đọc trực tiếp cột "Điều kiện" của `:219` / `:265` / `:308` |
| QA05 | Không có quy tắc buộc hai báo cáo khác nhau phải cho ra cùng con số | `nhất quán`, `đối chiếu số liệu giữa`, `cùng nguồn dữ liệu` |
| QA08 | Không quy định mức gom nhóm khi kỳ = "Khoảng tùy chọn", cũng không nói ngày sau khi auto tính còn sửa được hay không | đọc trực tiếp `:872` + `:1053` |
| QA13 | Không quy định cột "Tỷ lệ" cho `theo_ky[]` của FR-IX-20 (chỉ khai `{ky, so_ct}`) | đọc trực tiếp `:914` |
| QA01 | Mã `ERR-PERM-SYS-00-01` không tồn tại trong bản chốt | `ERR-PERM-SYS` (grep đệ quy toàn thư mục `srs-v3.5/` → 0 kết quả) |
