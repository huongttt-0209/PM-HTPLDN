# BA confirmation needed — Vụ việc HTPL — UAT tuần 3 — 2026-07-20

> Nội dung được tách theo module từ file BA confirm đa module của UAT tuần 3. Các section đối chiếu SRS, evidence và câu hỏi BA được giữ nguyên.

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
- Evidence: `bug-reports/image/BUG-CNKQHT_03-modal-cap-nhat-ket-qua.png` · `../../reverify-audit/PDHSVV_04/audit.md`.

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

- **CNKQVV_02**: verdict **`BA confirm`** (cập nhật 2026-07-20). App **có lệch** so với đặc tả text (đối tác phản ánh đúng "khác thiết kế") → ghi nhận **lệch đặc tả** BUG-CNKQVV_02 (describe lệch, không prescribe hướng sửa). Cả 2 lệch đều nhẹ + hợp lý → giống quyết định thiết kế cố ý; không có nguồn thiết kế uy tín (Figma) để khẳng định app SAI → **BA chốt**: giữ theo app (cập nhật đặc tả) hay sửa app theo đặc tả. Nếu BA chốt sửa app → dev fix theo BUG-CNKQVV_02. Chi tiết: `../../reverify-audit/CNKQVV_02/audit.md`.

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
- Evidence: `../../reverify-audit/TBKQTNHS_01/audit.md`.

**Câu hỏi cần BA xác nhận**

1. **Thông báo kết quả kiểm tra hồ sơ (Đạt/Không đạt) cho DN là TỰ ĐỘNG hay có nút bấm tay?**
   - Nếu **tự động** (theo `:905` + `:1758`): app đúng (không cần nút) → cần sửa AC `:947` cho nhất quán → đối tác không phải bug.
   - Nếu **thủ công** (theo AC `:947`): app **thiếu nút** → lỗi thật cần bổ sung.
2. Nếu chốt "tự động": đề nghị dev/BA xác minh **DN có thực sự nhận được thông báo tự động** khi chuyển trạng thái không. QA **chưa test được** phần này vì recipient là doanh nghiệp (không có tài khoản DN trong bộ test). Rủi ro: cùng module này đã xác nhận **4 bug thông báo KHÔNG được gửi** ở các bước khác (BUG-TPDHSVV_04, BUG-PDHSVV_05, BUG-PDHSVV_02, BUG-XNTGHTVV_04) → nếu auto-send cũng hỏng thì vẫn là lỗi chức năng thật.

**Đề xuất QA tạm thời**

- **TBKQTNHS_01**: verdict **`BA confirm`** (thuần). Đặc tả tự mâu thuẫn (auto vs nút tay), không tự quyết được Open/Reject; app khớp cách hiểu "auto". Chi tiết: `../../reverify-audit/TBKQTNHS_01/audit.md`.
