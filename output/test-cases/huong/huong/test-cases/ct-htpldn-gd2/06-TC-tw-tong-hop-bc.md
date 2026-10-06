# Test Cases — FR-XI-09 (UC170): TW tổng hợp BC

> **SRS Ref**: FR-XI-09, SCR-XI-01 Drill-down (action [Tổng hợp] + [Xuất Excel/Word]), Entity BAO_CAO_CT_HTPL (loại TONG_HOP_TW)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Chỉ CB NV TW xem DS BC từ BN/ĐP đã gửi (`da_gui_tw=1`), chọn nhiều BC (checkbox), auto-SUM cột 21a/21b, form editable, lưu BC tổng hợp loại `TONG_HOP_TW`. Side-effect: chuyển các đợt đã chọn sang `DA_TONG_HOP`. Xuất file Excel/Word theo mẫu TT17.
> **Scope**: Chọn → Tổng hợp → Lưu + Xuất file + verify state cuối DA_TONG_HOP.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-XI-09 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, thuộc cấp TW, có quyền tổng hợp BC, có ≥1 BC từ BN/ĐP đã gửi (DA_GUI_TW).

---

## Trường input FR-XI-09

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | bao_cao_ids | Y | identifier[] | FK BAO_CAO_CT_HTPL (đợt DA_GUI_TW), checkbox chọn |

---

## A. TW tổng hợp BC — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TH-001 | SM-DOT-BC / DA_GUI_TW → DA_TONG_HOP + BR-FLOW-08 | Tổng hợp BC happy path 2 BC | cb_nv_tw_01 (TW) login. Có 2 đợt DA_GUI_TW: DOT-CDP01-A (Sở TP AG) + DOT-CBN01-B (Bộ KH&ĐT) cùng kỳ SO_BO_NAM 2026. | bao_cao_ids = [BC-A, BC-B] | 1. Drill-down CT có đợt DA_GUI_TW. 2. Trong bảng "BC từ BN/ĐP" tick checkbox 2 BC. 3. Click [Tổng hợp]. 4. Form tổng hợp render với số liệu auto-SUM. 5. Click [Lưu]. | (3) Form editable hiển thị: số liệu = SUM của 2 BC theo cột tương ứng (21a/21b). (5) POST `/api/v1/bao-cao-ct/tong-hop` 200. (5) BAO_CAO_CT_HTPL record mới (`loai=TONG_HOP_TW`) lưu. (5) 2 đợt BC chuyển `DA_TONG_HOP`. (5) Toast "Tổng hợp thành công". Audit log INSERT (BR-DATA-05). | Happy 🔴 |
| TC-TH-002 | FR-XI-09 / AC#1 + BR-DATA-07 | DS BC từ BN/ĐP phân trang | cb_nv_tw_01 login. ≥25 BC ở DA_GUI_TW. | — | 1. Drill-down CT. 2. Mở bảng BC từ BN/ĐP. | (2) Bảng phân trang 20/page. Cột: Checkbox / Đơn vị / Cấp / Mã đợt / Kỳ / Ngày gửi / Trạng thái / Hành động (Xem). | Happy 🟡 |
| TC-TH-003 | FR-XI-09 / Processing step 4 — auto-SUM (SPEC-CLARIFY-CT-GD2-05) | Auto-SUM verify công thức cộng dồn | cb_nv_tw_01 login. 2 BC mock có số liệu cụ thể: BC-A cột "Số DN tham gia"=10, BC-B cột tương ứng=15. | — | 1. Chọn 2 BC. 2. Click [Tổng hợp]. 3. Verify cell "Số DN tham gia" trong form. | (3) ⚠️ SPEC-CLARIFY-CT-GD2-05: SRS srs-fr-15:984 nói "tổng các cột tương ứng 21a/21b" nhưng KHÔNG list cụ thể cột nào SUM cột nào lấy max/min/text. Expected: cell = 10+15=25 cho cột số. Cột text → nếu spec không nói → log GAP. | Edge 🟡 |
| TC-TH-004 | FR-XI-09 / Processing step 5 — CB NV chỉnh sửa | CB NV TW chỉnh sửa số liệu auto-SUM | cb_nv_tw_01 login. Sau TC-TH-003 form render. | so_lieu cell "Số DN tham gia" = 25 → sửa thành 23 | 1. Form đang mở. 2. Sửa cell từ 25 → 23. 3. [Lưu]. | (3) BC tổng hợp lưu với số 23 (KHÔNG bị overwrite back về 25). Comment/note "đã điều chỉnh" optional. | Happy 🟡 |
| TC-TH-005 | FR-XI-09 / Output#2 — Xuất Excel TT17 | Xuất Excel mẫu TT17 thành công | cb_nv_tw_01 login. BC tổng hợp đã lưu. | — | 1. Drill-down BC tổng hợp. 2. Click [Xuất Excel]. 3. MCP `list_network_requests` capture. | (2) GET `/api/v1/bao-cao-ct/tong-hop/{id}/export?format=xlsx` 200 với `Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`. File `.xlsx` download. (3) MCP `evaluate_script` mở file → verify sheet name khớp mẫu TT17/2025 (vd "Mẫu 21a", "Mẫu 21b"). | Happy 🔴 |
| TC-TH-006 | FR-XI-09 / Output#2 — Xuất Word TT17 | Xuất Word mẫu TT17 thành công | cb_nv_tw_01 login. BC tổng hợp đã lưu. | — | 1. Click [Xuất Word]. | (2) GET `/api/v1/bao-cao-ct/tong-hop/{id}/export?format=docx` 200 với `Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document`. File `.docx` download. | Happy 🟡 |

---

## B. TW tổng hợp BC — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TH-010 | FR-XI-09 / E1 ERR-XI-09-01 | Không chọn BC nào | cb_nv_tw_01 login. ≥1 BC DA_GUI_TW available. | bao_cao_ids = [] | 1. Mở bảng BC. 2. KHÔNG tick. 3. Click [Tổng hợp]. | (3) Reject với **"Vui lòng chọn ít nhất 1 BC để tổng hợp"** (ERR-XI-09-01). KHÔNG tạo bản ghi tổng hợp. | Negative 🔴 |
| TC-TH-011 | FR-XI-09 / E2 ERR-XI-09-02 | BN/ĐP truy cập Tổng hợp TW | cb_nv_dp_01 (ĐP) login. | — | 1. Truy cập URL `/ct-htpldn/{id}/tong-hop-tw` trực tiếp. | (1) 403 Forbidden. HOẶC nút [Tổng hợp] **ẩn** trong UI cho ĐP. Backend reject với **"Chỉ cấp TW mới tổng hợp BC"** (ERR-XI-09-02). | Negative 🔴 |
| TC-TH-012 | FR-XI-09 / E3 WRN-XI-09-01 (SPEC-CLARIFY-CT-GD2-04) | BC schema khác version (mẫu cũ) | cb_nv_tw_01 login. 2 BC: BC-A schema v1 (mẫu cũ), BC-B schema v2 (mẫu hiện tại). | bao_cao_ids = [BC-A, BC-B] | 1. Chọn 2 BC. 2. Click [Tổng hợp]. | (2) ⚠️ SPEC-CLARIFY-CT-GD2-04: SRS dòng 1013 nói "BC schema khác version → WRN-XI-09-01" nhưng không định nghĩa cơ chế nhận diện "mẫu cũ". Expected: hiển thị warning "BC từ {Sở TP AG} sử dụng mẫu cũ, cần chuyển đổi" + cho phép proceed (warning level) hoặc block (cần BA clarify). | Edge 🟡 |

---

## C. TW tổng hợp BC — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TH-013 | BR-EC-19 — batch >100 BC | Tổng hợp >100 BC chọn batch | cb_nv_tw_01 login. ≥101 BC DA_GUI_TW (mock). | bao_cao_ids = 101 ids | 1. Chọn 101 BC. 2. Click [Tổng hợp]. | (2) Backend reject 400 với toast/error "Số lượng BC chọn vượt quá giới hạn batch (100)" (BR-EC-19, srs-v3:4084). KHÔNG tạo bản ghi tổng hợp partial. | Edge 🟡 |
| TC-TH-014 | BR-DATA-06 + BR-DATA-07 — pagination guard 1 BC chọn | Tổng hợp 1 BC duy nhất (boundary min) | cb_nv_tw_01 login. Có 1 BC DA_GUI_TW. | bao_cao_ids = [BC-X] | 1. Chọn 1 BC. 2. Tổng hợp. 3. Lưu. | (3) PASS — boundary min 1 BC. BC tổng hợp = copy of BC-X (no SUM logic vì 1 BC). Đợt BC-X chuyển DA_TONG_HOP. | Edge 🟢 |

---

| TC-TH-015 | FR-XI-09 / Filter cross-kỳ (A4) | Tổng hợp 2 BC khác kỳ — block hay cho phép? | cb_nv_tw_01 login. BC-A kỳ SO_BO_NAM, BC-B kỳ TRON_NAM cùng CT. | bao_cao_ids = [BC-A, BC-B] | 1. Chọn 2 BC khác kỳ. 2. Click [Tổng hợp]. | (2) ⚠️ SRS không nói rõ "tổng hợp BC phải cùng kỳ". Expected: BLOCK với toast "Vui lòng chọn các BC cùng kỳ báo cáo" HOẶC cho phép tổng hợp cross-kỳ (tùy interpretation). Log SPEC-CLARIFY-CT-GD2-08. | Edge 🟡 |
| TC-TH-016 | FR-XI-09 / Đợt DA_TONG_HOP idempotency (A4) | Tổng hợp BC đã DA_TONG_HOP — re-tổng hợp | cb_nv_tw_01 login. BC-A đã DA_TONG_HOP (đã tổng hợp trước). | bao_cao_ids = [BC-A, BC-mới-DA_GUI_TW] | 1. Chọn BC-A (DA_TONG_HOP) + BC-mới (DA_GUI_TW). 2. Click [Tổng hợp]. | (2) BC-A bị filter khỏi DS chọn (chỉ DA_GUI_TW filter `da_gui_tw=1` không TONG_HOP). Nếu vẫn chọn được → backend reject với "BC đã được tổng hợp, không thể chọn lại". | Edge 🟡 |
| TC-TH-017 | FR-XI-09 / Xuất file DRY-RUN trước Lưu (A4) | Xuất Excel preview trước khi Lưu BC tổng hợp | cb_nv_tw_01 login. Form tổng hợp đã render auto-SUM. | — | 1. Form đang mở chưa Lưu. 2. Click [Xuất Excel]. | (2) ⚠️ Behavior unclear — UI có cho phép xuất preview không Lưu không? Expected: Block với toast "Vui lòng Lưu trước khi xuất" HOẶC cho phép preview với watermark "DRAFT". | Edge 🟢 |
| TC-TH-018 | BR-EC-12 / Pagination guard `[1,100]` (A6 fill GAP-A5-01 + A7 SỬA UI) | DS BC từ BN/ĐP — param size boundary | cb_nv_tw_01 login. ≥10 BC DA_GUI_TW. | — | 1. Mở bảng BC từ BN/ĐP. 2. MCP `evaluate_script` set `window.location.search = '?page=0&size=20'` rồi `wait_for(".ant-table-tbody, .ant-empty")`. 3. Set `window.location.search = '?page=1&size=101'` + `wait_for`. | (2) UI re-render: hoặc auto-default page=1 (table render) HOẶC error toast/empty với message "Trang không hợp lệ" (BR-EC-12). (3) UI re-render: hoặc auto-cap size=100 (table 100 rows) HOẶC error toast "Kích thước trang vượt quá giới hạn 100". KHÔNG silent process invalid param. | Edge 🟡 |
| TC-TH-019 | FR-XI-09 / Output#1 — `loai=TONG_HOP_TW` (A6 fill GAP-A5-02 + A7 SỬA UI + Codex CT-GD2-02) | Verify visual differentiation BC tổng hợp vs BC gốc — `loai` field gap | cb_nv_tw_01 login. Sau TC-TH-001 tổng hợp xong. | — | 1. Drill-down BC tổng hợp vừa tạo. 2. MCP `take_snapshot` + `evaluate_script` đọc badge label hoặc card title. 3. Drill-down BC ĐP/BN gốc (đã DA_TONG_HOP). | (2) ⚠️ **SPEC-CLARIFY-CT-GD2-09 (Codex 2026-05-10):** SRS line 998 ghi `BAO_CAO_CT (loai = TONG_HOP_TW)` nhưng entity `BAO_CAO_CT_HTPL` (lines 1293-1300) **KHÔNG có column `loai`**. UI verify gián tiếp: hiển thị badge/label "BC tổng hợp toàn quốc" (đặc trưng) + card title prefix "Báo cáo tổng hợp". (3) BC gốc ĐP/BN KHÔNG có badge "tổng hợp" — chỉ hiển thị "Báo cáo kết quả". Verify visual differentiation; field schema gap chờ BA clarify. | Edge 🟡 |

---

## Tổng kết file 06-TC

- **16 TC**: 6 Happy + 3 Negative + 7 Edge (A3 base 11 + A4 merged 3 + A6 merged 2)
- **Critical TC (🔴)**: 001, 005, 010, 011
- **A4 merged 2026-05-10**: TC-TH-015, 016, 017
- **A6 merged 2026-05-10**: TC-TH-018 (GAP-A5-01), TC-TH-019 (GAP-A5-02)
- **SPEC-CLARIFY**: CT-GD2-04 (TC-TH-012 schema versioning), CT-GD2-05 (TC-TH-003 auto-SUM), CT-GD2-08 (TC-TH-015 cross-kỳ)

*Generated 2026-05-10 — Phase A step A3 + A4 + A6 inline merge*
