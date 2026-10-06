# Test Cases — FR-III-20: Xuất file docx/PDF ký số cho CTĐT (UC mới)

> **SRS Ref**: FR-III-20 (srs-fr-03-dao-tao.md dòng 1045-1067), SCR-III-01 (action [Xuất ký số]), Entity CHUONG_TRINH_DAO_TAO + outbound BHXH/CA service ký số.
> **Nguồn**: Local SRS `input/srs-v3/srs-fr-03-dao-tao.md` §FR-III-20 + Plan overview §2.3 (ERR-EXP-02) + §3 Permission (CTDT scope-own).
> **Ngày tạo**: 2026-05-09
> **Phase**: A (re-run BMAD A1-A3)

---

## Quy ước

- **TC ID:** `TC-XUAT-{type}-{seq:03d}` — type: `H` happy / `N` negative / `B` boundary / `P` permission / `X` cross-module / `E` edge.
- **Kết quả mong đợi:** `**STATE**: ... **UI**: ... **PERSIST**: ...`.
- **Priority:** 🔴 Critical · 🟡 Major · 🟢 Minor.
- **Tài khoản:** primary `cb_nv_tw_01` / `cb_nv_bn_01` / `cb_nv_dp_01` / `cb_pd_tw_01`. Permission negative dùng `_03` accounts (qtht_03, dn_03, ...).
- **Mock outbound:** SPEC-CLARIFY-DT-EXP-01 — endpoint `/api/v1/ky-so/sign-doc` outbound (giả định). Test với mock service.

---

## SPEC-CLARIFY (file này)

| Mã | Mô tả | Trạng thái |
|----|-------|-----------|
| SPEC-CLARIFY-DT-EXP-01 | SRS không quote endpoint ký số cụ thể (chỉ ghi "Outbound BHXH/CA service" trong ERR-EXP-02). Assume `POST /api/v1/ky-so/sign-doc` với payload `{ctdt_id, dinh_dang}`. Cần BA xác nhận: (a) endpoint thật, (b) format response (binary stream hay download URL), (c) timeout BE, (d) retry policy. | Pending BA |
| SPEC-CLARIFY-DT-EXP-02 | SRS dòng 1053 ghi "CTDT ở DA_DUYET/DA_CONG_KHAI/HOAN_THANH" — KHÔNG bao DA_KET_THUC. Verify: CTĐT đã có KH `HOAN_THANH` thì CTĐT cũng `HOAN_THANH`? Hay CTĐT giữ DA_DUYET? Cần BA confirm SM-CTDT (SRS không quote SM CTĐT riêng). | Pending BA |
| SPEC-CLARIFY-DT-EXP-03 | SRS không quote message error nguyên văn cho ERR-EXP-02 (chỉ ghi "Xuất ký số fail" trong overview). Cần BA confirm message hiển thị (vd "Dịch vụ ký số đang bảo trì, vui lòng thử lại sau"). | Pending BA |
| SPEC-CLARIFY-DT-EXP-04 | SRS không quote template file path cho docx/PDF (vd `templates/ctdt-template.docx`). Test với assume template tồn tại; nếu missing → ERR-EXP-02 với message khác? | Pending BA |
| SPEC-CLARIFY-DT-EXP-05 | SRS không quote hash algorithm cho signature verify (SHA-256 / SHA-1). Test verify embedded signature dùng tool `pdfsig` hoặc OpenSSL — cần BA confirm chuẩn. | Pending BA |
| SPEC-CLARIFY-DT-EXP-06 | Concurrency 2 user export cùng CTĐT — lock theo ctdt_id hay cho phép parallel | BA confirm |
| SPEC-CLARIFY-DT-EXP-07 | Nguyên văn message khi BE storage full — generic vs specific | BA confirm |
| SPEC-CLARIFY-DT-A6-04 | dinh_dang blank/null vs invalid — phân biệt error code (TC-XUAT-N-018) | BA confirm error code distinction |

---

## A. UI VERIFY — Button [Xuất ký số] trong SCR-III-01

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-XUAT-H-001 | FR-III-20 / SCR-III-01 / UI | Verify button [Xuất ký số] hiển thị trong SCR-III-01 chi tiết CTĐT khi state ∈ {DA_DUYET, DA_CONG_KHAI, HOAN_THANH} | cb_nv_tw_01 đã đăng nhập. Seed CTĐT-TW-2026-001 trạng thái DA_DUYET (cấp TW, owner cb_nv_tw_01). | URL `/dao-tao/ctdt/CTDT-TW-2026-001` | 1. Login CB_NV_TW. 2. Navigate SCR-III-01 chi tiết CTĐT. 3. Quan sát action-bar header. | **STATE**: — (read-only). **UI**: Action-bar header chi tiết CTĐT có button **[Xuất ký số]** (icon ký + chữ). Tooltip: "Xuất file docx/PDF có ký số" (SPEC-CLARIFY-DT-EXP-03 message nguyên văn pending). Click button → mở dropdown 2 option: "Xuất DOCX" và "Xuất PDF". **PERSIST**: Reload giữ button visible. | Happy 🔴 |
| TC-XUAT-H-002 | FR-III-20 / SCR-III-01 / UI | Button [Xuất ký số] ẨN khi CTĐT trạng thái DU_THAO | cb_nv_tw_01 đăng nhập. Seed CTĐT-TW-2026-002 trạng thái DU_THAO. | — | 1. Mở chi tiết CTĐT-TW-2026-002. 2. Quan sát action-bar. | **STATE**: — **UI**: Button [Xuất ký số] **KHÔNG hiển thị** (per SRS dòng 1053: "Preconditions: CTĐT ở DA_DUYET/DA_CONG_KHAI/HOAN_THANH"). Action-bar chỉ có [Sửa], [Xóa], [Trình duyệt]. **PERSIST**: Reload — vẫn ẩn. | Negative 🔴 |

---

## B. EXPORT DOCX (Happy path)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-XUAT-H-003 | FR-III-20 / AC-1 / BR-DATA-05 | Xuất DOCX ký số thành công cho CTĐT DA_DUYET | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-001 trạng thái DA_DUYET, có 2 KH con (1 DA_DUYET + 1 DU_THAO). Mock service `POST /api/v1/ky-so/sign-doc` return 200 với binary `application/vnd.openxmlformats-officedocument.wordprocessingml.document` size ~150KB. | `ctdt_id=CTDT-TW-2026-001`, `dinh_dang=DOCX`, mock service ON | 1. Mở chi tiết CTĐT. 2. Click [Xuất ký số] > [Xuất DOCX]. 3. Quan sát loading. 4. Verify download. | **STATE**: BE call outbound `POST /api/v1/ky-so/sign-doc` payload `{ctdt_id, dinh_dang:'DOCX', user_id, ...}` (SPEC-CLARIFY-DT-EXP-01). Response binary stream → BE proxy về FE. AUDIT_LOG: hanh_dong='EXPORT_SIGNED', entity='CHUONG_TRINH_DAO_TAO', entity_id=CTDT-TW-2026-001, du_lieu_moi={dinh_dang:'DOCX'}, nguoi_thuc_hien_id=cb_nv_tw_01 (BR-DATA-05). **UI**: Loading spinner ~2-5s. Browser auto-download file `CTDT-TW-2026-001_ky-so_<timestamp>.docx`. Toast "Xuất tài liệu thành công" (message nguyên văn — SPEC-CLARIFY-DT-EXP-03). **PERSIST**: File mở được trong Word, content hiển thị đầy đủ thông tin CTĐT (tên, mã, đơn vị, KH danh sách). | Happy 🔴 |
| TC-XUAT-H-004 | FR-III-20 / AC-1 | Xuất DOCX cho CTĐT DA_CONG_KHAI | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-003 trạng thái DA_CONG_KHAI. | `ctdt_id=CTDT-TW-2026-003`, `dinh_dang=DOCX` | 1. Mở chi tiết. 2. [Xuất ký số] > [Xuất DOCX]. | **STATE**: Outbound call thành công. AUDIT_LOG ghi như TC-XUAT-H-003. **UI**: Download file DOCX. **PERSIST**: File hợp lệ, content match CTĐT-TW-2026-003. | Happy 🟡 |
| TC-XUAT-H-005 | FR-III-20 / AC-1 | Xuất DOCX cho CTĐT HOAN_THANH | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-004 trạng thái HOAN_THANH (đã có KH HOAN_THANH). | `ctdt_id=CTDT-TW-2026-004`, `dinh_dang=DOCX` | 1-2 như trên. | **STATE**: Outbound OK. AUDIT_LOG OK. **UI**: Download OK. **PERSIST**: Content có thêm section "Kết quả" (số HV hoàn thành, danh sách chứng nhận). | Happy 🟡 |

---

## C. EXPORT PDF

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-XUAT-H-006 | FR-III-20 / AC-2 | Xuất PDF ký số thành công cho CTĐT DA_DUYET | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-001 trạng thái DA_DUYET. Mock service trả PDF binary `application/pdf` ~200KB có signature embed. | `ctdt_id=CTDT-TW-2026-001`, `dinh_dang=PDF` | 1. Mở chi tiết. 2. [Xuất ký số] > [Xuất PDF]. 3. Verify download. | **STATE**: BE outbound `POST /api/v1/ky-so/sign-doc` payload `{dinh_dang:'PDF'}`. AUDIT_LOG: hanh_dong='EXPORT_SIGNED', du_lieu_moi={dinh_dang:'PDF'}. **UI**: Download `CTDT-TW-2026-001_ky-so_<timestamp>.pdf`. Toast thành công. **PERSIST**: PDF mở trong Adobe/PDF viewer hiển thị đầy đủ + có dấu ký số (panel "Signatures" trong viewer). | Happy 🔴 |

---

## D. VERIFY signature embedded (binary check)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-XUAT-H-007 | FR-III-20 / SPEC-CLARIFY-DT-EXP-05 | Verify signature embedded trong PDF — check qua `pdfsig` CLI | cb_nv_tw_01 đăng nhập. Đã download file PDF từ TC-XUAT-H-006. | File `CTDT-TW-2026-001_ky-so_*.pdf` | 1. Tải file PDF từ B5/D2. 2. Chạy `pdfsig <file.pdf>` (poppler-utils). 3. Quan sát output. | **STATE**: — **UI**: Output `pdfsig` chứa block: `Signature #1`, `Signer Certificate Common Name: <BHXH-CA>` (SPEC-CLARIFY-DT-EXP-05 — algorithm pending), `Signature Validation: Signature is Valid`, `Certificate Validation: Certificate issuer isn't Trusted` (nếu CA test) HOẶC `Trusted` (nếu CA prod). **PERSIST**: File hash match audit log (verify integrity — `sha256sum <file.pdf>`). | Happy 🔴 |
| TC-XUAT-H-008 | FR-III-20 / SPEC-CLARIFY-DT-EXP-05 | Verify signature trong DOCX — check XML signature tag | cb_nv_tw_01 đăng nhập. File DOCX từ TC-XUAT-H-003. | File `CTDT-TW-2026-001_ky-so_*.docx` | 1. Unzip file DOCX (DOCX = ZIP). 2. Check `_xmlsignatures/sig1.xml` tồn tại. 3. Verify `<DigestValue>` + `<SignatureValue>` không rỗng. | **STATE**: — **UI**: File ZIP chứa folder `_xmlsignatures/` với ≥1 file `sig*.xml`. Content XML có node `<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">` đầy đủ DigestValue + SignatureValue + KeyInfo (per OOXML signature standard). **PERSIST**: Mở file trong Word → tab "File > Info" hiển thị "Signed Document" badge. | Happy 🟡 |

---

## E. NEGATIVE — Service ký số down + template missing

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-XUAT-N-009 | 🟠 DEFER (A7) ERR-EXP-02 | Service BHXH-CA ký số DOWN → ERR-EXP-02 | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-001 DA_DUYET. Cần mock signing service toggle (env config). | `ctdt_id=CTDT-TW-2026-001`, mock service OFF | 1. Admin disable mock signing service. 2. Click [Xuất ký số] > [Xuất DOCX]. 3. Quan sát network panel + error toast. | **STATE**: BE call outbound fail (network panel hiển thị 503/connection_refused). **UI**: Toast/modal error code **ERR-EXP-02** + message (SPEC-CLARIFY-DT-EXP-03). KHÔNG download file. **PERSIST**: F5 reload → state CTĐT không đổi. | Negative 🔴 (DEFER A7) |
| TC-XUAT-N-010 | 🟠 DEFER (A7) ERR-EXP-02 / SPEC-CLARIFY-DT-EXP-04 | Template file `ctdt-template.docx` MISSING ở server → ERR-EXP-02 | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-001 DA_DUYET. Cần infra thao tác xóa template file (server-side). | `ctdt_id=CTDT-TW-2026-001`, template missing | 1. Infra remove template file (Phase B coordinate). 2. Click [Xuất DOCX]. 3. Quan sát toast + network. | **STATE**: BE đọc template fail → return 500 hoặc custom error. **UI**: Toast error ERR-EXP-02 hoặc generic. Network response trả lỗi. **PERSIST**: State CTĐT không đổi. | Negative 🟡 (DEFER A7) |
| TC-XUAT-N-011 | FR-III-20 / SPEC-CLARIFY-DT-EXP-02 | Cố xuất ký số cho CTĐT DU_THAO qua API direct → reject | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-002 DU_THAO (UI ẩn button — TC-XUAT-H-002). | API direct `POST /api/v1/ctdt/CTDT-TW-2026-002/export-signed` body `{dinh_dang:'DOCX'}` | 1. Bypass UI gọi API direct với token cb_nv_tw_01. | **STATE**: BE precondition check: state ∉ {DA_DUYET, DA_CONG_KHAI, HOAN_THANH} → return 400 hoặc 422 với message "CTĐT chưa được phê duyệt". KHÔNG sinh file. AUDIT_LOG fail. **UI**: HTTP 400/422 + body chứa error code. **PERSIST**: State CTĐT giữ DU_THAO. | Negative 🔴 |
| TC-XUAT-N-012 | FR-III-20 | `dinh_dang` không hợp lệ (vd "TXT") → reject | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-001 DA_DUYET. | API direct body `{dinh_dang:'TXT'}` | 1. POST API direct với dinh_dang='TXT'. | **STATE**: BE validation reject (per SRS dòng 1055 "DOCX/PDF" only). HTTP 400 + message "Định dạng không hợp lệ". **UI**: HTTP 400. **PERSIST**: Không sinh file. | Negative 🟡 |
| TC-XUAT-N-018 | FR-III-20 / SPEC-CLARIFY-DT-A6-04 | Xuất ký số — bỏ trống dinh_dang field | cb_nv_tw_01. CTDT CTDT-TW-2026-001 DA_DUYET. | API direct POST `/api/v1/ctdt/{id}/export-signed` với body `{dinh_dang: null}` hoặc body không có field `dinh_dang`. | 1. POST export với dinh_dang=null. 2. POST với body bỏ field dinh_dang. | **STATE**: KHÔNG sinh file. **UI**: HTTP 400 + error code (BA confirm — SPEC-CLARIFY-DT-A6-04: distinguish missing vs invalid). **PERSIST**: storage không có file mới. | Negative 🟡 |

---

## F. PERMISSION — Scope-own + role allowed

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-XUAT-P-013 | BR-AUTH-08 / FR-III-20 | CB_NV_DP cố xuất ký số CTĐT cấp TW → 403 (BR-AUTH-08 violate) | cb_nv_dp_01 đăng nhập. CTĐT-TW-2026-001 (cấp TW, KHÔNG thuộc scope ĐP). | API direct `POST /api/v1/ctdt/CTDT-TW-2026-001/export-signed` token DP | 1. Login CB_NV_DP_01. 2. POST API direct. | **STATE**: BE check don_vi_id mismatch → 403 (BR-AUTH-08). KHÔNG outbound. AUDIT_LOG: hanh_dong='ACCESS_DENIED', entity_id=CTDT-TW-2026-001, ly_do='cross-cap'. **UI**: HTTP 403 hoặc UI toast "Bạn không có quyền". **PERSIST**: Không sinh file. | Permission 🔴 |
| TC-XUAT-P-014 | Permission Matrix / FR-III-20 | CB_PD_TW cố xuất ký số (chỉ Approve, không Export) → 403 | cb_pd_tw_01 đăng nhập. CTĐT-TW-2026-001 DA_DUYET. | API direct token cb_pd_tw_01 | 1. Login CB_PD_TW. 2. POST API direct. | **STATE**: Per Permission Matrix (Plan §3) — CB_PD chỉ Approve, KHÔNG Export. BE return 403. **UI**: HTTP 403. **PERSIST**: Không sinh file. **Note**: SRS dòng 1051 "Tác nhân: CB NV" — KHÔNG bao CB PD. Nếu app cho phép CB_PD export → log SPEC-CLARIFY hoặc bug. | Permission 🟡 |

---

## G. EDGE — File lớn + retry timeout

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-XUAT-E-015 | FR-III-20 / SPEC-CLARIFY-DT-EXP-01 | Xuất ký số CTĐT có nhiều KH (file lớn ~5MB) — verify không timeout BE | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-005 DA_DUYET có 50 KH con + 200 HV (data lớn → render docx ~5MB). Mock service trả binary 5MB. | `ctdt_id=CTDT-TW-2026-005`, `dinh_dang=DOCX` | 1. Click [Xuất DOCX]. 2. Quan sát loading + timing. | **STATE**: BE outbound thành công, timeout BE đủ (per SPEC-CLARIFY-DT-EXP-01 timeout pending). AUDIT_LOG OK. **UI**: Loading có thể 10-15s nhưng KHÔNG fail. Download file ~5MB. Toast OK. **PERSIST**: File mở được, content đầy đủ 50 KH. | Edge 🟡 |
| TC-XUAT-E-016 | 🟠 DEFER (A7) FR-III-20 / SPEC-CLARIFY-DT-EXP-01 | Service ký số timeout (mock chậm 30s) — verify retry hoặc fail-fast | cb_nv_tw_01 đăng nhập. CTĐT-TW-2026-001 DA_DUYET. Cần mock signing service delay 30s (env config). | `ctdt_id=CTDT-TW-2026-001`, mock delay 30s | 1. Admin set mock service delay 30s. 2. Click [Xuất DOCX]. 3. Đợi 30s. 4. Quan sát toast + network. | **STATE**: BE timeout (assume 20s) → return ERR-EXP-02. Network panel hiển thị request pending → timeout. **UI**: Toast ERR-EXP-02 message. **PERSIST**: User có thể click lại button → request mới. | Edge 🟡 (DEFER A7) |

---

## H. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-XUAT-E-017 | FR-III-20 / Concurrency / Idempotency | 2 CB NV cùng [Xuất ký số] cho cùng CTĐT (race) | cb_nv_tw_01 + cb_nv_tw_02. CTĐT-TW-2026-001 DA_DUYET. Mock service đếm số lần gọi. | Cả 2 click [Xuất DOCX] cùng moment | 1. CB-A click. 2. CB-B click <500ms sau. 3. Quan sát mock service log. | **STATE**: BE behavior 2 lựa chọn: (A) 2 outbound calls riêng biệt (mỗi user file riêng) — chấp nhận vì mỗi export là 1 attempt; (B) Lock theo ctdt_id để tránh duplicate cost. Default: (A) — file output không ảnh hưởng nhau. AUDIT_LOG ghi 2 entry EXPORT_SIGNED. **UI**: Cả 2 download file riêng. **PERSIST**: SPEC-CLARIFY-DT-EXP-06 nếu BA muốn lock. | Edge 🟡 |

---

## Tổng hợp file 12

- **Total TC sau A8 Codex:** 18 active (LOẠI 1 + DEFER 4) trên 19 raw — +1 TC P1 codex (TC-XUAT-N-018 dinh_dang null).
  - A: 2 (UI verify + button hide)
  - B: 3 (DOCX × 3 state)
  - C: 1 (PDF happy)
  - D: 2 (signature embedded verify — PDF + DOCX)
  - E: 5 (negative — 2 KEEP state/dinh_dang + 1 P1 codex + 2 DEFER service down/template missing)
  - F: 2 (permission cross-cấp + cross-role)
  - G: 2 (edge file lớn KEEP + timeout DEFER)
  - H: 1 (A4 edge — concurrency 2 user export KEEP; storage disk full LOẠI A7)
- **SPEC-CLARIFY:** 8 (DT-EXP-01..07 + DT-A6-04)
- **Priority:** 7 🔴 + 11 🟡

---

## A7 Filter Notes

- **LOẠI:** TC-XUAT-E-018 (storage disk full) — environmental, không có cách reproduce trong env smoke; rare edge case không justify mock infra. SPEC-CLARIFY-DT-EXP-07 vẫn pending BA về message convention.
- **DEFER (A7) — env mock signing service required:**
  - TC-XUAT-N-009 service down (cần mock toggle)
  - TC-XUAT-N-010 template missing (cần infra remove file)
  - TC-XUAT-E-016 timeout (cần mock delay)
- **KEEP all others 13 TC:** UI verify + happy DOCX/PDF + signature embedded verify (binary check via pdfsig CLI / unzip DOCX = local tooling) + negative state-based + permission + concurrency 2 user export.

---

## Liên kết

- SRS: [`srs-fr-03-dao-tao.md`](../../../input/srs-v3/srs-fr-03-dao-tao.md) §FR-III-20 dòng 1045-1067
- Plan: [`00-test-plan-overview.md`](00-test-plan-overview.md) §1.2 file 12 + §2.3 ERR-EXP-02
- Permission: [`permission-matrix.md`](../../permission-matrix.md) section Đào tạo
- Sibling: [`output/test-cases/CG-TVV/01-TC-FR-IV-01-quan-ly-tvv.md`](../CG-TVV/01-TC-FR-IV-01-quan-ly-tvv.md)
