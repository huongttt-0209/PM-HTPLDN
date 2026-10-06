# BA confirmation needed - UAT tuần 3 - 2026-07-20

Bản SRS được chỉ định dùng để chấm UAT tuần 3: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5`. Tab đối tác: `UAT_TGPL Doanh Nghiệp-tuần 3`. Phạm vi: luồng Vụ việc HTPL (`srs-fr-05-vu-viec.md`).

## CNKQHT_03 và PDHSVV_04 - Phiên bản SRS nào là chuẩn để chấm (giới hạn ký tự các trường)

**Bối cảnh testcase**

- Dòng Excel: 11, mã TC `CNKQHT_03`. Nội dung kiểm tra: người được phân công (TVV/CG) cập nhật kết quả hỗ trợ. Đối tác báo: "nội dung chỉ cho phép tối đa 5000 ký tự, SRS yêu cầu cho phép tối đa 10.000".
- Dòng Excel: 9, mã TC `PDHSVV_04`. Nội dung kiểm tra: Cán bộ Phê duyệt từ chối phê duyệt, nhập lý do từ chối. Đối tác báo: "app cho tối đa 1.000 ký tự, SRS yêu cầu 2.000".
- Expected đối tác: theo con số lớn hơn (10.000 / 2.000).
- Actual app (đã verify): Nội dung kết quả `maxLength=5000`; ô Lý do từ chối `maxLength=1000` — đúng như đối tác báo.

**Điểm mâu thuẫn trong SRS**

Trong `planning-artifacts` có **3 bản SRS song song** cho cùng module Vụ việc:

| Thư mục | Header "Phiên bản SRS" | Số FR | Ngày sửa thư mục |
|---|:-:|:-:|---|
| `srs-v3` | 3.0 | 19 | 29/06/2026 |
| `srs-v3.5` | **3.5** | 21 | **16/07/2026** (mới nhất) |
| `srs-v4` | 3.0 (?) | 24 | 29/06/2026 |

Metadata **mâu thuẫn**: thư mục tên `v4` nhưng header bên trong ghi "Phiên bản 3.0"; thư mục `v3.5` được sửa gần nhất + header ghi đúng "3.5". Tôi được chỉ định dùng **v3.5**, CLAUDE.md dự án cũng gọi v3.5 là bản "latest". **Nhưng con số đối tác đối chiếu (10.000 / 2.000) chỉ có trong `srs-v4`**, không có ở v3.5:

| Trường / tiêu chí | v3.5 (bản được giao) | v4 (bản đối tác có vẻ dùng) | Case bị ảnh hưởng |
|---|---|---|---|
| `noi_dung_ket_qua` (Nội dung kết quả hỗ trợ) — giới hạn ký tự | Không nêu giới hạn | max 10.000 ký tự | CNKQHT_03 (ý 3) |
| `ly_do` (Lý do từ chối phê duyệt, FR-V.I-13) — giới hạn ký tự | Không nêu max, chỉ min 10 | min 10, max 2000 | PDHSVV_04 |

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1083` (noi_dung_ket_qua — không nêu giới hạn)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:977` + `:1008` (ly_do — min 10, không nêu max)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v4/srs-fr-05-vu-viec.md:1127` (noi_dung_ket_qua — max 10.000)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v4/srs-fr-05-vu-viec.md:1007` (ly_do — min 10, max 2000)

**Kết quả verify UI hiện tại**

- CNKQHT_03: modal "Cập nhật kết quả hỗ trợ", trường Nội dung kết quả đếm "0 / 5000" (`maxLength=5000`).
- PDHSVV_04: ô Lý do từ chối `maxLength=1000` (đã xác nhận qua verify).
- Evidence: `bug-reports/image/BUG-CNKQHT_03-modal-cap-nhat-ket-qua.png` · `reverify-audit/PDHSVV_04/audit.md`.

**Câu hỏi cần BA xác nhận**

1. **Bản SRS nào là chuẩn chấm UAT tuần 3 — v3.5 hay v4?** (đối tác dường như đối chiếu theo v4).
2. Nếu **v3.5**: giới hạn 5000 (Nội dung kết quả) / 1000 (Lý do từ chối) hiện tại có được chấp nhận không (v3.5 không nêu con số)?
3. Nếu **v4** (hoặc "phải theo con số 10.000 / 2.000"): app đang giới hạn thấp hơn = **thiếu so với yêu cầu** → thành lỗi thật.

**Đề xuất QA tạm thời**

- **CNKQHT_03**: verdict **`BA confirm`**. LƯU Ý: 2 ý con (thiếu trường Tệp kết quả hỗ trợ, thừa trường Kết luận) là **lỗi thật ngay theo v3.5**, không phụ thuộc phiên bản → **dev fix bất kể BA** (BUG-CNKQHT_03). Chỉ riêng ý (3) "10.000 ký tự" chờ BA chốt phiên bản — nên toàn case để `BA confirm`.
- **PDHSVV_04**: verdict **`BA confirm`** (thuần). Chỉ có 1 vấn đề là giới hạn ký tự, con số 2.000 chỉ có ở v4 → **toàn bộ verdict phụ thuộc câu hỏi này**. Theo v3.5 (không quy định max) app không vi phạm; theo v4 (max 2000) thì thiếu. Nếu BA chốt v4 → mở bug "ô Lý do từ chối 1000 < 2000".

> **Lưu ý (đã tự kiểm, KHÔNG cần BA cho phần này):** cơ chế **optimistic lock** ("Vụ việc đã được {người} cập nhật lúc {giờ}, vui lòng tải lại") mà các case **CNKQHT_06 / CNKQVV_05** kiểm — **có trong cả v3.5** (`srs-v3.5/...:1586` + BR `:2294` "Tất cả chuyển trạng thái SHALL sử dụng optimistic locking"). → 2 case này verify được theo v3.5, không bị chặn bởi câu hỏi phiên bản.

## CNKQVV_02 - Tên nút + trường của modal "Hoàn thành vụ việc" có đúng thiết kế không

**Bối cảnh testcase**

- Dòng Excel: 13, mã TC `CNKQVV_02`.
- Nội dung kiểm tra: CB nghiệp vụ cập nhật kết quả cuối / hoàn thành vụ việc (vụ việc "Đã duyệt").
- Expected đối tác: hiển thị đúng tên nút + các trường theo thiết kế.
- Actual đối tác ghi: "tên nút chức năng và các trường thông tin không giống với thiết kế".

**Đối chiếu SRS v3.5 (FR-V.I-16)**

| # | App thực tế | Đặc tả v3.5 | Vị trí |
|---|---|---|---|
| 1 | Nút "Hoàn thành" / modal "Hoàn thành vụ việc" / nút gửi "Xác nhận" | Nút "Cập nhật kết quả cuối" / [Cập nhật KQ cuối] | `:1167` + `:1739` |
| 2 | Modal có thêm trường "Kết quả xử lý" (radio Thành công/Không thành công) | Inputs chỉ có `ket_luan_cuoi` ("Kết luận cuối cùng") | `:1136-1140` |

Trường "Kết luận cuối cùng" khớp `ket_luan_cuoi` ✅. Trường "Kết quả xử lý" ánh xạ field `ketQuaXuLy` có sẵn trong mô hình dữ liệu VU_VIEC → hợp lý về nghiệp vụ.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1167` (AC nút "Cập nhật kết quả cuối")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1739` (bảng nút hành động SCR-V.I-03)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1136-1140` (Inputs FR-V.I-16)

**Kết quả verify UI hiện tại**

- `cbnv_tw` bấm "Hoàn thành" trên VV-BTP-TW-20260712-001 (DA_DUYET) → modal "Hoàn thành vụ việc" (Kết luận cuối cùng + Kết quả xử lý) → điền + Xác nhận → `POST .../hoan-thanh` [201], vụ việc → "Hoàn thành". Modal app **giống hệt** frame đối tác chụp.
- Evidence: `bug-reports/image/CNKQVV_02-modal-hoan-thanh.png`.

**Câu hỏi cần BA xác nhận**

1. **Tên nút** chuẩn là "Hoàn thành" (như app) hay "Cập nhật kết quả cuối" (như đặc tả)? Tên "Hoàn thành" rõ nghĩa theo transition → HOAN_THANH, có thể là quyết định thiết kế cố ý.
2. **Trường "Kết quả xử lý" (Thành công/Không thành công)** có thuộc thiết kế chính thức của bước hoàn thành không? Có → cập nhật Inputs FR-V.I-16; không → app thừa trường.

**Đề xuất QA tạm thời**

- **CNKQVV_02**: verdict **`BA confirm`** (cập nhật 2026-07-20). App **có lệch** so với đặc tả text (đối tác phản ánh đúng "khác thiết kế") → ghi nhận **lệch đặc tả** BUG-CNKQVV_02 (describe lệch, không prescribe hướng sửa). Cả 2 lệch đều nhẹ + hợp lý → giống quyết định thiết kế cố ý; không có nguồn thiết kế uy tín (Figma) để khẳng định app SAI → **BA chốt**: giữ theo app (cập nhật đặc tả) hay sửa app theo đặc tả. Nếu BA chốt sửa app → dev fix theo BUG-CNKQVV_02. Chi tiết: `reverify-audit/CNKQVV_02/audit.md`.

## TBKQTNHS_01 - Thông báo kết quả kiểm tra hồ sơ: tự động hay có nút bấm tay

**Bối cảnh testcase**

- Dòng Excel: 6, mã TC `TBKQTNHS_01`.
- Nội dung kiểm tra: Cán bộ Nghiệp vụ mở vụ việc đã qua bước kiểm tra, tìm nút "Gửi thông báo kết quả" (gửi kết quả kiểm tra Đạt/Không đạt cho DN).
- Actual đối tác ghi: màn hình không có nút/chức năng này.

**Điểm mâu thuẫn trong SRS v3.5**

App **thật sự không có** nút "Gửi thông báo kết quả" ở cả trạng thái đang kiểm tra (DANG_KIEM_TRA) lẫn đã hoàn thành (HOAN_THANH). Nhưng đây là **mâu thuẫn trong chính đặc tả v3.5**:

| Nguồn đặc tả v3.5 | Nói gì | Vị trí |
|---|---|---|
| FR-V.I-12 §Màn hình | "Auto action — Thông báo KQ" (tự động) | `:905` |
| SCR-V.I-03 §Quy tắc màn hình | "Thông báo kết quả = auto trigger khi chuyển trạng thái, gửi tự động" (không nút) | `:1758` |
| FR-V.I-12 §Acceptance Criteria | "When nhấn 'Gửi Thông báo'..." (có nút bấm tay) | `:947` |

→ App (không có nút) **khớp** cách hiểu "tự động" (`:905` + `:1758`) nhưng **trái** AC `:947`. Đối tác kỳ vọng nút tay theo AC `:947`.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:905`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1758`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:947`

**Kết quả verify UI hiện tại**

- Không thấy nút "Gửi thông báo kết quả" ở cả DANG_KIEM_TRA lẫn HOAN_THANH.
- Evidence: `reverify-audit/TBKQTNHS_01/audit.md`.

**Câu hỏi cần BA xác nhận**

1. **Thông báo kết quả kiểm tra hồ sơ (Đạt/Không đạt) cho DN là TỰ ĐỘNG hay có nút bấm tay?**
   - Nếu **tự động** (theo `:905` + `:1758`): app đúng (không cần nút) → cần sửa AC `:947` cho nhất quán → đối tác không phải bug.
   - Nếu **thủ công** (theo AC `:947`): app **thiếu nút** → lỗi thật cần bổ sung.
2. Nếu chốt "tự động": đề nghị dev/BA xác minh **DN có thực sự nhận được thông báo tự động** khi chuyển trạng thái không. QA **chưa test được** phần này vì recipient là doanh nghiệp (không có tài khoản DN trong bộ test). Rủi ro: cùng module này đã xác nhận **4 bug thông báo KHÔNG được gửi** ở các bước khác (BUG-TPDHSVV_04, BUG-PDHSVV_05, BUG-PDHSVV_02, BUG-XNTGHTVV_04) → nếu auto-send cũng hỏng thì vẫn là lỗi chức năng thật.

**Đề xuất QA tạm thời**

- **TBKQTNHS_01**: verdict **`BA confirm`** (thuần). Đặc tả tự mâu thuẫn (auto vs nút tay), không tự quyết được Open/Reject; app khớp cách hiểu "auto". Chi tiết: `reverify-audit/TBKQTNHS_01/audit.md`.

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
- Evidence: `reverify-audit/QLHSDNHTCP_03-web-danhsach-cot.png` · `reverify-audit/QLHSDNHTCP_03/audit.md`.

**Câu hỏi cần BA xác nhận**

1. Cột cảnh báo thời hạn (SLA) có **bắt buộc hiển thị đúng 4 nhãn mức rời** theo BR-CALC-03 (Sắp đến hạn / Cần xử lý gấp / Sát hạn / Quá hạn) không, hay dạng "đếm ngược + mã màu" hiện tại được chấp nhận?
2. Tên cột chuẩn là "Mức cảnh báo thời hạn" (thiết kế đối tác) hay "Hạn xử lý" (app) — hay chỉ cần tiếng Việt rõ nghĩa là đạt?

**Đề xuất QA tạm thời**

- **QLHSDNHTCP_03**: verdict **`BA confirm`**. App đáp ứng yêu cầu chức năng (có cột SLA + cảnh báo qua màu, tiếng Việt) → không phải Open; quan sát đối tác đúng (format khác thiết kế) → không Reject. SRS không quy định chính xác tên cột + format giá trị → BA chốt có ép đúng 4 nhãn mức / tên thiết kế không. Chi tiết: `reverify-audit/QLHSDNHTCP_03/audit.md`.

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
- Evidence: `reverify-audit/QLHSDNHTCP_09-web-tieude-stepper.png` · `reverify-audit/QLHSDNHTCP_09/audit.md`.

**Câu hỏi cần BA xác nhận**

1. Tiêu đề trang màn Chi tiết có **bắt buộc** theo thiết kế "Chi tiết hồ sơ #{mã}" không, hay dùng tên DN làm tiêu đề (các trường header đủ) được chấp nhận?
2. Breadcrumb có **bắt buộc** kèm "#{ma_ho_so}" theo component #1 không (app đang hiển thị "Chi tiết" thiếu #mã)?

**Đề xuất QA tạm thời**

- **QLHSDNHTCP_09**: verdict **`BA confirm`**. Tiêu đề = tên DN tái hiện đúng đối tác báo → không Reject; SRS không quy định chuỗi tiêu đề h1 → không có SRS violation rõ ràng → không tự Open. Stepper đúng 6 bước → phần này không phải lỗi. Breadcrumb thiếu #mã gộp vào câu hỏi 2. Chi tiết: `reverify-audit/QLHSDNHTCP_09/audit.md`.

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
- Evidence: `reverify-audit/QLHSDNHTCP_10-web-thanh-tongquan-sla.png` · `reverify-audit/QLHSDNHTCP_10/audit.md` · `condition-table.md` (0 GAP).

**Câu hỏi cần BA xác nhận**

1. Trường SLA trên thanh tổng quan màn Chi tiết có **bắt buộc hiển thị đúng 4 nhãn mức rời** theo BR-CALC-03 (Sắp đến hạn / Cần xử lý gấp / Sát hạn / Quá hạn) không, hay dạng "đếm ngược + màu" hiện tại được chấp nhận? (Trùng câu hỏi 1 của QLHSDNHTCP_03 — nếu BA chốt 1 lần thì áp dụng cho cả list + detail.)

**Đề xuất QA tạm thời**

- **QLHSDNHTCP_10**: verdict **`BA confirm`**. Thanh tổng quan đủ trường + không tràn/đè → không Open toàn case; SLA format đếm ngược tái hiện đúng đối tác báo → không Reject; SRS không quy định chính xác format → BA chốt (gộp với _03). Chi tiết: `reverify-audit/QLHSDNHTCP_10/audit.md`.

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
- Evidence: `reverify-audit/QLHSDNHTCP_19-web-cot-khong-sort.png` · `reverify-audit/QLHSDNHTCP_19/audit.md`.

**Câu hỏi cần BA xác nhận**

1. Click-sort theo tên cột có phải **yêu cầu chung toàn hệ thống** (khi đó màn Danh sách Chi trả thiếu = bug cần fix), hay chỉ áp dụng cho các màn có "Hành vi=sắp xếp" trong SRS (khi đó Chi trả đúng spec, đóng case)?

**Đề xuất QA tạm thời**

- **QLHSDNHTCP_19**: verdict **`BA confirm`**. App khớp SRS Chi trả (không đủ căn cứ Open) nhưng lệch chuẩn các module sibling (không thể Reject dứt khoát) → BA chốt phạm vi yêu cầu click-sort. Chi tiết: `reverify-audit/QLHSDNHTCP_19/audit.md`.

<!-- DẠNG A — QA đã kết luận, cần BA phản hồi đối tác. Gộp 6 TC sibling (_23→_28) cùng 1 gốc: expected đối tác theo bố cục "6 Nhóm" của thiết kế đối tác, SRS v3.5 dùng danh sách trường phẳng. -->

## QLDNDHTPL_23 → _28 — Expected đối tác chấm theo bố cục "6 Nhóm" (thiết kế đối tác `HTPLDN-PTYC-CT-v2.0`) trong khi SRS v3.5 dùng danh sách trường phẳng ở màn Chi tiết DN

**Bối cảnh testcase**

- Dòng Excel: 34–39; mã TC `QLDNDHTPL_23` / `_24` / `_25` / `_26` / `_27` / `_28`.
- Nội dung kiểm tra: CB Nghiệp vụ mở màn Chi tiết DN qua nút "Xem" (SCR-V.III-02, FR-V.III-01, UC81) → kiểm tra hiển thị từng nhóm thông tin.
- Expected trong file UAT (đối tác chấm theo thiết kế `HTPLDN-PTYC-CT-v2.0`, mỗi nhóm phải "giống thiết kế", đúng định dạng, không tràn/đè, đồng nhất ngôn ngữ):
  - `_23` — Nhóm 1 Thông tin DN; `_24` — Nhóm 2 Người đại diện; `_25` — Nhóm 3 Tiêu chí ưu tiên NĐ55 Điều 4.
  - `_26` — Nhóm 4 Thông tin khác; `_27` — Nhóm 5 Chỉ số tổng hợp (kỳ vọng có mục này); `_28` — Nhóm 6 Lịch sử hỗ trợ (kỳ vọng có cột "Lĩnh vực" + "Tư vấn viên").
- Actual đối tác ghi: các nhóm "không giống với thiết kế" (khác cách gom nhóm); Nhóm 5 "Chỉ số tổng hợp" không hiển thị; Nhóm 6 thiếu cột "Lĩnh vực" + "Tư vấn viên".

**Đối chiếu SRS v3.5**

- Màn Chi tiết DN (SCR-V.III-02) đặc tả các trường dưới dạng **danh sách phẳng** (bảng thành phần), **KHÔNG** gom thành "6 Nhóm". Bố cục gom nhóm trong SRS ("Nhóm A/B/C") **chỉ tồn tại ở màn THÊM MỚI DN** (SCR-V.III-03), không phải màn Chi tiết → "6 Nhóm" là cấu trúc của thiết kế đối tác, không có trong SRS được giao chấm.
- SRS **không có** mục "Chỉ số tổng hợp" ở màn Chi tiết DN — chỉ có 3 KPI (Tổng VV / VV hoàn thành / Tổng chi phí) ở tab Lịch sử Hỗ trợ.
- Tab Lịch sử Hỗ trợ chỉ được đặc tả là "Danh sách VV liên kết + 3 KPI" — SRS **không quy định** danh sách cột (không nêu cột "Lĩnh vực" hay "Tư vấn viên").
- Trường "File đính kèm" thuộc nhóm cuối màn Chi tiết ("Luôn hiển thị") — cần xác nhận đã dời sang tab "Hồ sơ pháp lý" (gộp theo v2.1) hay chưa.

Bảng đối chiếu chi tiết theo từng case:

| Case | Đối tác kỳ vọng (theo thiết kế) | App thực tế | SRS v3.5 |
|---|---|---|---|
| _23 | Nhóm 1 gom đúng thiết kế | Trường cơ bản đủ, gom trong "Thông tin chung" + "Thông tin liên hệ", không tràn/đè | Danh sách phẳng, không quy định "6 Nhóm" (dòng 464–495) |
| _24 | Nhóm 2 "Người đại diện" riêng | "Người đại diện" + "Chức vụ đại diện" nằm trong "Thông tin chung" | Liệt kê phẳng, không tách nhóm riêng (dòng 483–484) |
| _25 | Nhóm 3 "Tiêu chí ưu tiên NĐ55" riêng | Phụ nữ làm chủ / Số LĐ nữ / Số LĐ khuyết tật nằm chung khối "Thông tin lao động & tài chính" | 3 trường NĐ55 liệt kê phẳng, không tách nhóm (dòng 488–490) |
| _26 | Nhóm 4 "Thông tin khác" đúng thiết kế | Khối "Thông tin khác" = Ghi chú; **chưa thấy** "File đính kèm" trên tab này | Nhóm cuối = Ghi chú (dòng 492) + File đính kèm (dòng 493, "Luôn hiển thị") |
| _27 | Nhóm 5 "Chỉ số tổng hợp" hiển thị | **Không có** mục "Chỉ số tổng hợp"; chỉ có 3 KPI ở tab Lịch sử hỗ trợ | **Không có** mục "Chỉ số tổng hợp" ở SCR-V.III-02 (dòng 464–495) |
| _28 | Nhóm 6 danh sách VV có cột "Lĩnh vực" + "Tư vấn viên" | Danh sách VV 4 cột: Mã / Tiêu đề / Trạng thái / Ngày tiếp nhận + 3 KPI; **không có** 2 cột đó | Tab Lịch sử Hỗ trợ = "Danh sách VV liên kết + 3 KPI", **không quy định cột** (dòng 468) |

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:464-495` (SCR-V.III-02 — bảng thành phần màn Chi tiết, danh sách trường phẳng)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:468` (tab Lịch sử Hỗ trợ = "Danh sách VV liên kết + 3 KPI", không quy định cột)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:483-484` (Người đại diện + Chức vụ ĐD) · `:488-490` (3 trường NĐ55) · `:492-493` (Ghi chú + File đính kèm)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:552` · `:562` · `:572` (bố cục "Nhóm A/B/C" — CHỈ ở màn Thêm mới SCR-V.III-03, không phải Chi tiết)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:79` (UC Reference UC81 cho FR-V.III-01)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, dùng tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/doanh-nghiep/5eed0010-0000-4000-8000-000000000001` (DN-SEED-0001 "Công ty TNHH Seed Publishable").
- Tab "Thông tin": 4 khối (Thông tin chung / Thông tin liên hệ / Thông tin lao động & tài chính / Thông tin khác), 23 trường — đủ trường cơ bản + đủ 3 trường NĐ55 (Phụ nữ làm chủ, Số LĐ nữ, Số LĐ khuyết tật); tìm toàn trang KHÔNG có mục "Chỉ số tổng hợp".
- Tab "Lịch sử hỗ trợ": danh sách VV 4 cột (Mã / Tiêu đề / Trạng thái / Ngày tiếp nhận) + 3 KPI (Tổng VV 14 / VV hoàn thành 5 / Tổng chi phí 0₫) — không có cột "Lĩnh vực" / "Tư vấn viên".
- Đối chiếu: app hiển thị đủ mọi trường/thành phần SRS v3.5 yêu cầu; khác biệt với đối tác chỉ ở cách gom nhóm/có mục "Chỉ số tổng hợp"/có 2 cột — đều là những thứ SRS v3.5 không quy định.
- Evidence: `reverify-audit/QLDNDHTPL_23/thong-tin-tab-full.png` (dùng chung _23–_27) · `reverify-audit/QLDNDHTPL_28/lich-su-ho-tro-columns.png` (_28).

**Kết luận QA**

- Cả 6 case `_23` → `_28` **không phải bug theo SRS v3.5**: app đủ trường/đủ thành phần đặc tả, đúng định dạng, không tràn/đè, đồng nhất ngôn ngữ.
- Web hiện tại **đúng SRS v3.5**; điểm đối tác phản ánh là khác biệt so với **thiết kế đối tác** (`HTPLDN-PTYC-CT-v2.0`), không phải khác biệt so với SRS:
  - `_23`/`_24`/`_25`/`_26`: chỉ khác **cách gom nhóm** — SRS dùng danh sách phẳng, không ép "6 Nhóm";
  - `_27`: mục "Chỉ số tổng hợp" **không có trong SRS** (app khớp SRS, thiết kế đối tác thừa mục này);
  - `_28`: SRS **silent về cột** danh sách VV (app đủ "Danh sách VV + 3 KPI").
- QA **không tự Reject** vì chưa rõ thiết kế đối tác có phải nguồn ràng buộc bổ sung không → cần BA chốt (không tự chốt được phần "thiết kế đối tác có hiệu lực trên SRS hay không").

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận với đối tác 4 điểm để chốt hướng xử lý:

1. **Bố cục màn Chi tiết DN** — bắt buộc theo "6 Nhóm" của thiết kế đối tác, hay danh sách trường phẳng theo SRS v3.5 (đủ trường, gom 4 khối) là đạt? (áp cho `_23`/`_24`/`_25`/`_26` — cùng 1 quyết định).
2. **Trường "File đính kèm"** (SRS `:493`, "Luôn hiển thị") — đặt ngay tab Thông tin hay đã chuyển hẳn sang tab "Hồ sơ pháp lý" (gộp v2.1)? (`_26`).
3. **Mục "Chỉ số tổng hợp"** (Nhóm 5) — bắt buộc bổ sung vào màn Chi tiết theo thiết kế đối tác, hay theo SRS v3.5 (không có mục này) là đạt? (`_27`).
4. **Cột danh sách VV tab Lịch sử hỗ trợ** — bắt buộc thêm "Lĩnh vực" + "Tư vấn viên" theo thiết kế đối tác, hay bộ 4 cột hiện tại là đạt? (`_28`).

- Verdict QA đề xuất: `Cần BA xác nhận` cho cả 6 case (`_23`→`_28`) — **chưa gửi Dev** cho tới khi BA chốt thiết kế đối tác có ràng buộc hay không.
- Nếu BA chốt **theo SRS v3.5**: cả 6 case đóng "Không phải bug theo SRS", QA cập nhật lại expected testcase của đối tác.
- Nếu BA chốt **theo thiết kế đối tác** (bắt buộc "6 Nhóm" / có "Chỉ số tổng hợp" / có 2 cột): chuyển thành yêu cầu bổ sung, owner `Dev FE` (bố cục/cột/mục hiển thị).
- Chi tiết note từng case: `reverify-audit/QLDNDHTPL_23..28/note.txt`.

---

*(Các mục BA khác sẽ bổ sung khi phát sinh trong quá trình verify các case còn lại.)*
