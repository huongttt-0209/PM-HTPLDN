# Functional Test Report — R7.7.12.2 FR-V.II-14 DN bổ sung hồ sơ chi trả

> **Module:** Chi trả chi phí (FR-V.II / FR-06) · **Task:** R7.7.12.2 · **Round:** R7-R2 (2026-05-12 00:25:00 - 01:30:00) · **Tester:** QA Automation via Claude Code
> **SRS:** [srs-update-2026-5-5/srs-fr-06-chi-tra.md §FR-V.II-14 row 833-890](../../../../input/srs-update-2026-5-5/srs-fr-06-chi-tra.md) + [SCR-V.II-02 row 955-1033](../../../../input/srs-update-2026-5-5/srs-fr-06-chi-tra.md) + [02-thu-tu-module.md §10 SM-CHI-TRA B7](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md)
> **Bug:** [bug-report-r7-7-12-2-fr14-bo-sung.md](../../bug-reports/chi-tra/bug-report-r7-7-12-2-fr14-bo-sung.md) (3 lỗi: 2 Major + 1 Minor)

---

## Kết luận R2 (2026-05-12 01:30:00, LATEST)

⚠️ **Partial — FR-V.II-14 DVC-only path defer + phát hiện bug Major BE nội bộ.**

R2 deep review NotebookLM + grep SRS local đã **loại trừ ambiguous spec intent**: FR-V.II-14 thuần DN qua DVC, wording row 841 "hoặc CB NV (thủ công)" là drift (mâu thuẫn 8+ chỗ khác). Hệ quả: BUG-008 BE endpoint thiếu defer-able đến DVC sandbox sẵn sàng (downgrade Critical → Major); BUG-009 UI thiếu thực ra không phải bug (UI đúng spec — downgrade Major → Minor doc note).

Path test verify R2:
1. **CB NV manual UI (SCR-V.II-02 detail page state YCBS):** 0 file input + 0 ant-upload + 0 action button — **đúng spec, không phải bug**. Cross-check HSCT000011 (lichSu rỗng) + HSCT000004 (lichSu R3 đầy đủ) cùng pattern.
2. **BE endpoint direct probe:** 5/5 path variant `POST /api/v1/ho-so-chi-tras/{id}/bo-sung*` trả 404 ERR-SYS-00-04-01 → BUG-008 Major (LGSP receiver chưa expose).
3. **DN portal HTPLDN internal:** DN role 9999999990 sidebar không có module chi-tra, direct URL `/chi-tra/danh-sach` → 403 — **đúng FR-V.II-01**, không phải bug.
4. **Field-level integrity 6 HSCT YCBS:** API GET trả `ngayYeuCauBoSung = null` cho 6/6 dù transition DKT → YCBS đã xảy ra → **BUG-010 Major mới phát hiện** (vi phạm FR-V.II-03 Bước 5 + BR-CHITRA-BS01).
5. **BR-CALC-01 verify:** 6/6 HSCT có `mucHoTroPct` + `soTienDeNghi` khớp tier quy mô DN (SIEU_NHO 100%/3M, NHO 30%/5M, VUA 10%/10M).
6. **BR-CHITRA-BS01 soLanBoSung verify:** 6/6 trong range [1, 3], không vượt max 3.

**Pool YCBS thực tế** (cập nhật từ báo cáo R1 cũ ghi 4 record): **6 record** ở AG scope: HSCT000004 (Đại Việt SIEU_NHO, lichSu R3) + HSCT000011 (Bình Minh SIEU_NHO) + HSCT000012 (Phúc An NHO) + HSCT000013 (Hoàng Gia VUA) + HSCT000014 (Đại Việt SIEU_NHO) + HSCT200002 (Phúc An NHO).

**Accounts dùng:** `cb_nv_dp_01` AG (CB NV path) + `9999999990` HN (DN portal verify).

---

## Bảng trạng thái TC (snapshot R2 — LATEST 2026-05-12 01:30:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| CT-14-001 | CB NV manual upload bổ sung tài liệu | ⏭ SKIP | R7-R2 | Không trong spec intent — DVC-only (BUG-009 wording drift) |
| CT-14-002 | Validate file type (PDF/DOC/DOCX/JPG/PNG) | 🚫 BLOCKED | R7-R2 | Cascade BUG-008 (LGSP receiver thiếu) + DVC sandbox down |
| CT-14-003 | Validate file size ≤10MB → ERR-CT-BS-02 | 🚫 BLOCKED | R7-R2 | Cascade BUG-008 + DVC sandbox down |
| CT-14-004 | State transition YCBS → DKT sau bổ sung | 🚫 BLOCKED | R7-R2 | Cascade BUG-008 + DVC sandbox down |
| CT-14-005 | Notification CB NV phụ trách | 🚫 BLOCKED | R7-R2 | Cascade BUG-008 + DVC sandbox down |
| CT-14-006 | Counter bo_sung_count++ max 3 lần | 🚫 BLOCKED | R7-R2 | Cascade BUG-008 (so_lan++ qua endpoint thiếu) |
| CT-14-007 | ERR-CT-BS-01 (state ≠ YCBS) | 🚫 BLOCKED | R7-R2 | Cascade BUG-008 + DVC sandbox down |
| CT-14-008 | ERR-CT-BS-03 (quá hạn 5 ngày LV) | 🚫 BLOCKED | R7-R2 | Cascade BUG-010 (ngayYeuCauBoSung null → deadline không tính được) |
| CT-14-009 | DN qua DVC/Cổng PLQG sync vào CTN | ⏭ SKIP | R7-R2 | DVC out of test env (sandbox external) |
| CT-14-010 | DN portal HTPLDN internal access chi-tra | ✅ PASS | R7-R2 | DN role 403 đúng spec FR-V.II-01 |
| CT-14-R-001 | API field integrity 6 HSCT YCBS (`ngayYeuCauBoSung`) | ❌ FAIL | R7-R2 | 6/6 trả null — BUG-010 Major |
| CT-14-R-002 | BR-CALC-01 verify mức HT × quy mô DN 6/6 | ✅ PASS | R7-R2 | 100%/30%/10% khớp tier SIEU_NHO/NHO/VUA |
| CT-14-R-003 | BR-CHITRA-BS01 `soLanBoSung ∈ [0, 3]` | ✅ PASS | R7-R2 | 6/6 trong range (giá trị 1/3/1/2/3/1) |
| CT-14-R-004 | UI status badge "Yêu cầu bổ sung" dịch tiếng Việt | ✅ PASS | R7-R2 | 6/6 badge dịch OK, không enum code |
| CT-14-R-005 | UI action button "Kiểm tra" trên list YCBS | ✅ PASS | R7-R2 | 6/6 row hiện đúng action (đúng spec) |
| CT-14-R-006 | UI Lịch sử xử lý render từ lichSu array | ✅ PASS | R7-R2 | HSCT000004/200002 render 2 entry OK |
| CT-14-R-007 | UI Stepper 6 bước (Tiếp nhận → Thanh toán) | ✅ PASS | R7-R2 | Detail render đúng 6 step name tiếng Việt |
| CT-14-R-008 | DN role 9999999990 truy cập /chi-tra → 403 | ✅ PASS | R7-R2 | Đúng FR-V.II-01 — DN không access portal internal chi-tra |
| **Tổng** | **18 TC** | ✅8 · ❌1 · 🚫7 · ⏭2 | | |

## Bảng TC chưa chạy được — cần làm gì để chạy (R2)

Hiện tại 10 TC chưa chạy được — chia 5 nhóm: 1 ❌ FAIL chờ dev BE fix `ngayYeuCauBoSung` (BUG-010, nhóm B), 6 🚫 BLOCKED chờ DVC sandbox + BE LGSP receiver (BUG-008, nhóm B+D), 1 🚫 BLOCKED cascade từ BUG-010 (nhóm B), 1 ⏭ SKIP wording drift đợi BA xoá (BUG-009, nhóm C), 1 ⏭ SKIP DVC out-of-env (nhóm D).

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| CT-14-001 | Spec intent là DN qua DVC, không phải CB NV manual (BUG-009 wording) | BA xoá wording row 841 "hoặc CB NV (thủ công)" để align spec | BA |
| CT-14-002 | LGSP receiver `/bo-sung*` thiếu + DVC sandbox chưa connect (BUG-008) | BE expose endpoint nhận multipart từ LGSP gateway + Infra mở DVC sandbox | Dev BE + Infra |
| CT-14-003 | LGSP receiver thiếu — không upload được file để test size | BE expose endpoint + validate size ≤10MB trả ERR-CT-BS-02 | Dev BE |
| CT-14-004 | LGSP receiver thiếu — không trigger state transition | BE expose endpoint + cập nhật state YCBS → DKT khi DVC sync | Dev BE |
| CT-14-005 | LGSP receiver thiếu — không trigger notification | BE expose endpoint + gửi thông báo CB NV phụ trách | Dev BE |
| CT-14-006 | LGSP receiver thiếu — không tăng so_lan_bo_sung qua DVC sync | BE expose endpoint + logic counter ++ với guard max 3 | Dev BE |
| CT-14-007 | LGSP receiver thiếu — không probe được mã lỗi E1 | BE expose endpoint + trả ERR-CT-BS-01 khi state ≠ YCBS | Dev BE |
| CT-14-008 | `ngayYeuCauBoSung = null` 6/6 → deadline 5 ngày LV không tính được (BUG-010) | BE fix transition DKT → YCBS set `ngayYeuCauBoSung = NOW()` | Dev BE |
| CT-14-009 | DVC LGSP integration external, không có staging mock | Infra mở DVC sandbox mock HOẶC out of HTPLDN test scope | Infra |
| CT-14-R-001 | BE không set `ngayYeuCauBoSung` khi advance DKT → YCBS (BUG-010) | BE fix transition handler theo FR-V.II-03 Bước 5 | Dev BE |

---

## Test approach R2

### Phase 1 — Deep review NotebookLM + SRS local (2026-05-12 01:00:00)

R1 raise 2 khả năng spec intent (a) DN qua DVC only / (b) cả 2 path. R2 loại trừ ambiguous trước khi escalate BA:

- **NotebookLM HTPLDN** (id `a4ae45bf-cea0-4325-8fee-b1e0be702cf2`): "FR-V.II-14 thuần DN qua DVC. Row 841 mâu thuẫn FR-V.II-01 cấm CB NV nhập tay HSCT".
- **Grep SRS local** (`srs-fr-06-chi-tra.md`): 8+ chỗ ủng hộ DVC-only (line 31, 295, 950, 962, 1014, 1026, 1283, 1317), 1 chỗ duy nhất drift (line 841).

→ Conclusion: intent thực = (a) DN qua DVC. BUG-008 downgrade Critical → Major (defer-able). BUG-009 reframe Major UI missing → Minor doc note wording drift.

### Phase 2 — Path 1: CB NV manual UI verify (verify spec intent thực)

1. Login `cb_nv_dp_01` AG (sở hữu 6 HSCT YCBS).
2. Vào "Quản lý chi trả chi phí" → tab "Chờ xử lý" — pool YCBS hiển thị 6 record.
3. List page cột HÀNH ĐỘNG chỉ có button "Kiểm tra" cho mọi YCBS — đúng spec, action navigate sang detail page, không phải trigger action workflow.
4. Click HSCT000011 (Bình Minh AG, SIEU_NHO, lichSu rỗng).
5. Detail page render: header info + Stepper 6 bước (Tiếp nhận / Kiểm tra / Đánh giá / Thẩm định / Phê duyệt / Thanh toán) + 3 section (DN info / TVV info / Lịch sử xử lý — "Chưa có lịch sử xử lý").
6. Inspect DOM bằng `evaluate_script`: 0 `<input type="file">` + 0 `.ant-upload` + 0 action button ngoài "Quay lại danh sách" — **đúng spec, không phải bug FE**.
7. Cross-check HSCT000004 (Đại Việt SIEU_NHO, lichSu R3 đầy đủ "Tiếp nhận → Đang kiểm tra → Yêu cầu bổ sung" by cb_nv_dp_01 lúc 10/05/2026 11:17): UI render identical, vẫn 0 upload UI.

### Phase 3 — Path 2: BE endpoint direct (probe LGSP receiver)

5 path variant `POST /api/v1/ho-so-chi-tras/{id}/bo-sung*` với body `{}` qua fetch authenticated `cb_nv_dp_01`:

| Path | OPTIONS Status | OPTIONS Allow | POST Status | POST Body |
|---|:-:|---|:-:|---|
| `/bo-sung` | 204 | `GET,HEAD,PUT,PATCH,POST,DELETE` (CORS wildcard) | **404** | `ERR-SYS-00-04-01` Cannot POST .../bo-sung |
| `/bo-sung-ho-so` | 204 | same | **404** | `ERR-SYS-00-04-01` Cannot POST .../bo-sung-ho-so |
| `/upload-bo-sung` | 204 | same | **404** | `ERR-SYS-00-04-01` Cannot POST .../upload-bo-sung |
| `/file-bo-sung` | 204 | same | **404** | `ERR-SYS-00-04-01` Cannot POST .../file-bo-sung |
| `/dinh-kem` | 204 | same | **404** | `ERR-SYS-00-04-01` Cannot POST .../dinh-kem |

→ LGSP receiver chưa register. OPTIONS 204 + allow wildcard `*` là CORS preflight, không phải route thực.

### Phase 4 — Path 3: DN portal HTPLDN internal (verify FR-V.II-01)

1. Logout `cb_nv_dp_01` qua `POST /api/v1/auth/logout` + `localStorage.clear()`.
2. Login `9999999990` (Nguyễn Văn A - DN Test 01, HN scope).
3. Dashboard redirect `/vu-viec/danh-sach` — DN landing page chính.
4. Sidebar chỉ có **4 module:** Tổng quan / Quản lý đào tạo, tập huấn / Quản lý vụ việc HTPL / Quản lý DN được hỗ trợ. **Không có "Quản lý chi trả chi phí".**
5. Truy cập trực tiếp `/chi-tra/danh-sach` → redirect `/403` "Bạn không có quyền truy cập trang này. Vai trò hiện tại: DN".

→ DN qua HTPLDN portal internal không có entry FR-V.II-14 — **đúng spec FR-V.II-01**. DN bổ sung phải qua DVC/Cổng PLQG external.

### Phase 5 — Field-level integrity 6 HSCT YCBS (R2 extend)

Login lại `cb_nv_dp_01`. Fetch GET `/api/v1/ho-so-chi-tras/{id}` cho 6 HSCT:

| HSCT | trangThai | soLanBoSung | ngayYeuCauBoSung | mucHoTroPct | quyMoDN | BR-CALC-01 |
|---|---|:-:|:-:|:-:|---|:-:|
| HSCT000004 | YCBS | 1 | **null** | 100% | SIEU_NHO | ✅ PASS |
| HSCT000011 | YCBS | 3 | **null** | 100% | SIEU_NHO | ✅ PASS |
| HSCT000012 | YCBS | 1 | **null** | 30% | NHO | ✅ PASS |
| HSCT000013 | YCBS | 2 | **null** | 10% | VUA | ✅ PASS |
| HSCT000014 | YCBS | 3 | **null** | 100% | SIEU_NHO | ✅ PASS |
| HSCT200002 | YCBS | 1 | **null** | 30% | NHO | ✅ PASS |

→ **BUG-010 mới phát hiện:** 6/6 `ngayYeuCauBoSung = null` dù transition DKT → YCBS đã xảy ra. BR-CALC-01 + BR-CHITRA-BS01 `soLanBoSung ∈ [0, 3]` đều PASS.

### Phase 6 — UI extended verify (badge / stepper / lichSu / action button)

- **CT-14-R-004 Status badge:** 6/6 hiển thị "Yêu cầu bổ sung" tiếng Việt thuần, không enum code.
- **CT-14-R-005 Action button:** 6/6 row chỉ có "Kiểm tra" — đúng spec (CB NV review HSCT, không phải bổ sung).
- **CT-14-R-006 Lịch sử xử lý:** HSCT000004/200002 render 2 entry đúng (Tiếp nhận → Đang kiểm tra → Yêu cầu bổ sung); HSCT000011/012/013/014 hiển thị "Chưa có lịch sử xử lý" (consistent với API `lichSu = []`).
- **CT-14-R-007 Stepper:** 6 bước tiếng Việt đúng: Tiếp nhận / Kiểm tra / Đánh giá / Thẩm định / Phê duyệt / Thanh toán.

---

## Defects ghi nhận trong round (xem chi tiết bug-report-r7-7-12-2-fr14-bo-sung.md)

| Bug ID | Severity | Tóm tắt |
|---|---|---|
| BUG-CHITRA-008 | **Major** | LGSP gateway endpoint nhận sync HS bổ sung từ DVC chưa expose — 5/5 path variant trả 404 ERR-SYS-00-04-01. Defer-able đến khi DVC sandbox sẵn sàng. |
| BUG-CHITRA-010 | **Major** | `ngayYeuCauBoSung = null` 6/6 HSCT YCBS — BE không set timestamp khi DKT → YCBS, vô hiệu hoá deadline tracking 5 ngày LV. Lỗi nội bộ, fix được ngay. |
| BUG-CHITRA-009 | Minor | Wording SRS line 841 "hoặc CB NV (thủ công)" mâu thuẫn 8+ chỗ DVC-only — đề xuất BA xoá. |

---

## Đề xuất unblock

**Ngắn hạn (Dev BE, 1 ngày):**
- Fix BUG-010 — set `ngay_yeu_cau_bo_sung = NOW()` trong transition handler DKT → YCBS (FR-V.II-03 Bước 5). Đây là bug nội bộ độc lập DVC.
- Backfill data cho 6 HSCT YCBS hiện có (UPDATE timestamp dựa vào `audit_log` entry "KIEM_TRA → YCBS" gần nhất, vd HSCT000004/200002 lấy từ lichSu @ 10/05/2026 11:17).

**Trung hạn (BA, 1-2 ngày):**
- Fix BUG-009 — sửa SRS row 841 + 837 xoá phần "hoặc CB NV (thủ công)" để align toàn bộ context DVC-only.

**Dài hạn (Infra + Dev BE, defer):**
- Mở DVC LGSP sandbox staging cho QA test full path DN qua DVC (CT-14-009).
- Fix BUG-008 — BE expose LGSP receiver endpoint nhận multipart từ DVC, validate file + cập nhật state + AUDIT_LOG (chỉ làm sau khi DVC sandbox sẵn sàng để test end-to-end).

---

## Lịch sử round

| Round | Date | Kết quả tóm tắt |
|---|---|---|
| R7-R2 | 2026-05-12 00:25:00 - 01:30:00 | **⚠️ Partial** — Deep review NotebookLM + SRS local loại trừ ambiguous spec intent (DVC-only). 18 TC tổng (8 PASS / 1 FAIL / 7 BLOCKED / 2 SKIP). 3 bug log: BUG-008 Major (LGSP receiver defer), BUG-010 Major (ngayYeuCauBoSung null 6/6 — bug nội bộ), BUG-009 Minor (wording drift). Pool YCBS thực 6 record. |
| R7-R1 | 2026-05-10 02:10:00 | **🚫 BLOCKED** — báo cáo cũ ghi không có HSCT thuộc QA DN. Stale: pool YCBS thực có 6 record (báo cáo cũ ghi 4). Verify R2 đào sâu BE + UI confirm root cause là DVC-only intent, không phải seed gap. |
