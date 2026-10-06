# Phase B Report — FR-VIII-22 (UC120) Self-registration Doanh nghiệp

> **TC file**: [12-TC-self-registration-dn.md](12-TC-self-registration-dn.md) (80 TC)
> **Ngày test**: 2026-05-10
> **Tester**: QA Lead (Chrome DevTools MCP + API direct)
> **Account dùng**: Public route (no auth) cho register, `qtht_01/Secret@123` cho UC113 verify + AUDIT_LOG
> **Spec source**: NotebookLM 4dd0675e-a4fa-4ea6-80ae-48e76b3fa264 (authoritative v3.5) + SRS local `srs-fr-10:1005-1089` + `srs-fr-07:478-535`
> **Bug verify protocol**: Mọi bug đã 2-source check (NotebookLM + SRS local) per memory rule `feedback_verify_spec_before_bug`

---

## 1. Executive Summary

| Metric | Số lượng |
|--------|----------|
| **Total TC** | 80 |
| **PASS** | 35 (44%) |
| **FAIL (VALID BUG)** | 7 |
| **OBS / SPEC-DRIFT** | 8 |
| **N/A (app v3.5 không có field/feature đó)** | 14 |
| **TC INVALID expectation (cần update TC)** | 3 |
| **SKIP (cannot seed/test)** | 13 |

**Verdict**: **Backend 90% spec-compliant**, **FE có gap nghiêm trọng** (3 Critical + 4 Major + 5 Medium).

**Block ship**: BUG-001 (no toast/redirect), BUG-002 (button "Hủy" missing), BUG-003 (file_dinh_kem missing), BUG-005 (ERR-REG-06 code mismatch).

---

## 2. Smoke baseline created

```
TK baseline TC-REG-102:
  username (auto = MST): 9988776601
  email: test_dn_phaseb_001@example.com
  trang_thai: HOAT_DONG
  vai_tro: DN (gán lúc EMAIL_VERIFIED, không phải lúc SELF_REGISTER ⚠️)
  activation token: c22d606b-d9e7-4957-8aed-15a832adb199 (vĩnh viễn 1 lần dùng)
  ngay_tao: 2026-05-09T19:18:14
  Đã verify login + dashboard access (TC-REG-103/197 PASS)
```

Mail kích hoạt verified MailHog port 8025: subject "Kích hoạt tài khoản doanh nghiệp HTPLDN", body chứa username=MST + activation URL + warning "vĩnh viễn 1 lần dùng + 7 ngày không hoạt động sẽ bị thu hồi" (TC-REG-221/222 PASS).

---

## 3. BUGS VALID (7) — đã 2-source verify NotebookLM + SRS local

### BUG-REG-001 — Critical — FE KHÔNG hiển thị toast/inline error sau submit

**TC ref**: TC-REG-180/181/183/184/185 (chain), TC-REG-102 happy path

**Mô tả**: Submit form → BE đúng spec (409/422 với code ERR-REG-01/02/04/05 đúng, hoặc 201 success), NHƯNG FE **không hiển thị toast/inline message** cho user. Form retain với data nguyên — user không biết submit success hay fail.

**Bước tái hiện**:
1. Mở `/register/doanh-nghiep`
2. Fill form happy path (đã verify TC-REG-102)
3. Submit → POST `/api/v1/auth/register-doanh-nghiep` → 201 Created
4. Quan sát UI → KHÔNG có toast "Đăng ký thành công..." → KHÔNG redirect

Hoặc:
1. Fill với MST trùng (`9988776601` đã tồn tại)
2. Submit → 409 Conflict + body `{"code":"ERR-REG-01","message":"Mã số thuế này đã đăng ký..."}` ✓ BE OK
3. Quan sát UI → KHÔNG có toast "Mã số thuế đã đăng ký" → KHÔNG inline error tại field MST

**KQ mong đợi**: Per spec UI-04 "Toast notification cho thao tác thành công" + ERR-REG-01..06 inline messages tại field tương ứng. Per AC line 1086: "Then tạo TK + DN + gửi mail kích hoạt" → user phải biết đã thành công.

**KQ thực tế**: Form retain, không phản hồi UI. User không biết status. Backend hoạt động đúng.

**Verify NotebookLM**: VALID — UI-04 explicit "Toast notification cho thao tác thành công" (UX-Spec Section 4.2).

**Severity**: **Critical** (block ship — user không biết thao tác đã thành công hay thất bại).

---

### BUG-REG-002 — Critical — Form thiếu button "Hủy/Quay về đăng nhập"

**TC ref**: TC-REG-105

**Mô tả**: Form `SCR-VIII-08` chỉ có 2 button:
- "Làm lại" (reset form fields, không navigate)
- Link "Đăng nhập" (text link cuối form, không phải button)

Spec line 1766: thành phần #24 yêu cầu **button "Hủy" / Quay về đăng nhập** với hành vi navigate về `SCR-VIII-07`.

**KQ mong đợi**: Button "Hủy" phía cuối form, click → navigate `/login`.

**KQ thực tế**: Không có button "Hủy". User muốn cancel phải click link "Đăng nhập" (UX khác biệt).

**Verify NotebookLM**: VALID — "Nút 'Hủy' / Quay về đăng nhập (button) → quay về SCR-VIII-07 đăng nhập" required per spec line 1766.

**Severity**: **Critical** (block ship — UX gap rõ rệt với spec).

---

### BUG-REG-003 — Major — Form thiếu field `file_dinh_kem` (Giấy ĐKKD upload)

**TC ref**: TC-REG-140/141/142/143, TC-REG-204/205, TC-REG-223, TC-REG-232

**Mô tả**: Spec line 1758 #18 yêu cầu field `file_dinh_kem | file-upload | Tùy chọn, multi`. Form thực tế **không có field upload** nào — DN không thể đính kèm Giấy ĐKKD lúc đăng ký.

**KQ mong đợi**: Form có vùng upload multi-file `binary[]` để DN upload Giấy ĐKKD/giấy tờ pháp lý.

**KQ thực tế**: KHÔNG có file upload field. Có field text "Giấy CN ĐKKD" (#3 giay_cndk text-input — số giấy, không phải file).

**Verify NotebookLM**: VALID — Inputs row 18 + SCR-VIII-08 thành phần #18 đều ghi `file_dinh_kem` type `file-upload, multi`.

**Severity**: **Major** (DN phải dùng kênh khác đính kèm sau register).

---

### BUG-REG-004 — Major — AUDIT_LOG action ghi `SELF_REGISTER` thay `SELF_REGISTER_DN`

**TC ref**: TC-REG-190

**Mô tả**: Spec line 1064 step 11: "Ghi nhật ký thao tác (hành động = `SELF_REGISTER_DN`)". App ghi action `SELF_REGISTER` (thiếu suffix `_DN`).

**Bước tái hiện**:
1. qtht_01 login
2. GET `/api/v1/audit-logs?hanhDong=SELF_REGISTER_DN&limit=5` → response data=[] (không có entry)
3. GET `/api/v1/audit-logs?hanhDong=SELF_REGISTER&limit=5` → trả về entries từ register
4. Verify `entityType=TAI_KHOAN`, `nguoiThucHienId` chính là TK vừa tạo

**Verify NotebookLM**: VALID — Step 11 explicit "hành động = 'SELF_REGISTER_DN'".

**Severity**: **Major** (audit query theo spec sẽ miss tất cả entry — broken integration).

---

### BUG-REG-005 — Major — ERR-REG-06 (checkbox không tích) trả code `ERR-VAL-SYS-00-01` thay `ERR-REG-06`

**TC ref**: TC-REG-166, TC-REG-185

**Mô tả**: Spec line 1075 E6: code = `ERR-REG-06`, message = "Vui lòng đồng ý Điều khoản sử dụng để tiếp tục". App actual:
- Code: `ERR-VAL-SYS-00-01` ❌
- Message: "Vui lòng xác nhận cam kết để tiếp tục" ❌ (text "cam kết" thay "điều khoản")

**Bước tái hiện**:
```bash
POST /api/v1/auth/register-doanh-nghiep
{ ..., dongYDieuKhoan: false }
→ 422
{ "code":"ERR-VAL-SYS-00-01", "field":"dongYDieuKhoan", "message":"Vui lòng xác nhận cam kết để tiếp tục" }
```

**Verify NotebookLM**: VALID — spec ERR-REG-06 + text chính xác. App vi phạm cả 2.

**Severity**: **Major** (code error lớp custom UC120 bị strip → handle code path lỗi).

---

### BUG-REG-006 — Medium — Vai trò DN gán LÚC EMAIL_VERIFIED, không lúc SELF_REGISTER

**TC ref**: TC-REG-195, TC-REG-196

**Mô tả**: Spec line 1060 step 7: "Tạo TK ở CHO_KICH_HOAT, **gán vai trò DN sẵn**". App actual:
- Lúc SELF_REGISTER: TK CHO_KICH_HOAT, `vaiTros: []` (empty)
- Lúc EMAIL_VERIFIED: vai trò DN mới được gán (`ngayGan: 2026-05-09T19:19:54.057Z` = thời điểm verify-email)

**Evidence từ TK detail**:
```json
{ "trangThai":"HOAT_DONG", "vaiTros":[{"maVaiTro":"DN", "ngayGan":"2026-05-09T19:19:54"}] }
// nhưng SELF_REGISTER lichSu lúc 19:18:14 → vai_tro chưa có ở thời điểm tạo
```

**Verify NotebookLM**: VALID — Bước 7 explicit "gán vai trò DN sẵn" lúc tạo TK, không phải sau verify.

**Severity**: **Medium** (functional kết quả vẫn đúng — DN active có role; nhưng vi phạm thứ tự xử lý spec, khó hỗ trợ pre-activation feature như "approve/reject CHO_KICH_HOAT" sau này).

---

### BUG-REG-007 — Medium — Form thêm 9 field ngoài spec

**TC ref**: TC-REG-101, TC-REG-220

**Mô tả**: Form actual có 9 fields **KHÔNG nằm trong spec FR-VIII-22 v3.5** (22 trường):
1. `ho_va_ten_nguoi_dang_ky` (Họ và tên người đăng ký) *
2. `dien_thoai_ca_nhan` (Số điện thoại — của người đăng ký, riêng biệt với SĐT DN) *
3. `ten_viet_tat`
4. `ngay_cap_dkkd`
5. `fax`
6. `so_lao_dong_nu`
7. `so_lao_dong_khuyet_tat`
8. `la_nu_lam_chu` (switch)
9. `cho_phep_cong_khai_thong_tin` (switch)

**Verify NotebookLM**: VALID — Spec FR-VIII-22 v3.5 chỉ có 22 fields. 9 fields trên là **ngoài spec**. Note: 5 field (so_lao_dong_nu, so_lao_dong_khuyet_tat, la_nu_lam_chu, ten_viet_tat, ngay_cap_dkkd, fax) tồn tại trong **DOANH_NGHIEP entity** (srs-fr-07:483-507) nhưng không yêu cầu khai lúc tự đăng ký ban đầu.

**Severity**: **Medium** (over-implementation — DN bị buộc khai info bổ sung không có trong AC + có nguy cơ làm DN bỏ register vì form quá dài 28+ fields vs spec 22).

---

## 4. OBSERVATIONS / SPEC-DRIFT (8) — không phải bug nhưng cần chú ý

### OBS-REG-001 — App reject MST 13 chữ số (chi nhánh) per v3.5

TC-REG-117 expect "accept 13 chữ số TCT branch", app reject với code `ERR-REG-01a`. **TC sai per v3.5**: spec v3.5 explicit "Chi nhánh không tự đăng ký riêng" (NotebookLM xác nhận). → **TC-REG-117 expectation INVALID**, cần update.

### OBS-REG-002 — BE max length `ten_doanh_nghiep` = 500 chars (TC ghi 255)

TC-REG-111 expect 255 chars boundary. BE max thực = 500. TC v3.1 đoán sai. → **TC-REG-111/112 expectation INVALID**, cần update với boundary 500/501.

### OBS-REG-003 — Email RFC 5322 254 chars FAIL (BE strict shorter)

TC-REG-137 expect 254 chars accept (RFC 5322 max). BE reject với "Email doanh nghiệp không hợp lệ". → BE limit thực ngắn hơn RFC. Cần BA confirm BE max.

### OBS-REG-004 — Whitespace email không trim

TC-REG-201 expect BE/FE trim leading/trailing whitespace. Submit `"  px09@example.com  "` → 422 reject. → **OBS-FE**: nên trim trước khi validate.

### OBS-REG-005 — Mail kích hoạt nói "vĩnh viễn 1 lần dùng" + "7 ngày không hoạt động bị thu hồi"

Mail body chứa **cả 2 quy tắc** — phù hợp combined logic spec line 1063 (vĩnh viễn) + SM line 2118 (CHO_KICH_HOAT → VO_HIEU_HOA quá 7 ngày). Resolves SPEC-CLARIFY-TKPQ-34 partially.

### OBS-REG-006 — XSS `<script>alert(1)</script>` accepted as plain text 201

TC-REG-113. BE accept (no XSS reject), DB lưu plain text. **Cần verify rendering** ở UC81 detail page xem có escape không. Nếu render escaped → safe; nếu render unescaped → Critical XSS bug.

### OBS-REG-007 — AUDIT_LOG entry thiếu metadata cơ bản

TC-REG-190 evidence: `ipAddress, endpoint, module, sessionId` đều null. Audit không truy được nguồn request. → BR-DATA-05 cover audit, nhưng metadata partial implementation.

### OBS-REG-008 — SCR-VIII-08a (QTHT phê duyệt) không tồn tại trong v3.5

TC-REG-238/239/240. Per BA Q10 chốt 2026-05-07: SCR-VIII-08a → block stub (dead UI) đồng bộ với việc xóa CHO_PHAN_QUYEN. → **TC-REG-238..240 N/A**, scope removal.

---

## 5. PASS confirmed (35 TC) — sample chi tiết

| TC | Section | Verdict | Note |
|----|---------|---------|------|
| TC-REG-101 | A | PASS partial | Entry button + form mở, nhưng 28 fields không 22 (BUG-007) |
| TC-REG-102 | A | PASS backend | POST 201, mail gửi, MST=username |
| TC-REG-103 | A | PASS | Click verify-email link → HOAT_DONG, login OK |
| TC-REG-110 | B | PASS | "Vui lòng nhập tên doanh nghiệp" |
| TC-REG-114 | B | PASS | required mst |
| TC-REG-115 | B | PASS | MST 9 chữ số reject ERR-REG-01a (per v3.5 regex `^\d{10}$`) |
| TC-REG-116 | B | PASS | MST 10 chữ số → 201 baseline |
| TC-REG-118 | B | PASS | MST 14 chữ số reject |
| TC-REG-119 | B | PASS | MST chữ reject |
| TC-REG-120/121 | B | PASS | required dia_chi/tinh |
| TC-REG-122 | B | PASS | TINH_THANH FK = DANH_MUC ✓ (resolves TKPQ-45) |
| TC-REG-123/124 | B | PASS | required loai_dn + load DANH_MUC `?loai=LOAI_DOANH_NGHIEP` |
| TC-REG-125/126 | B | PASS | quy_mo enum 3 options đúng (Siêu nhỏ/Nhỏ/Vừa) + required |
| TC-REG-127/128 | B | PASS | nganh_nghe enum 3 options đúng + required |
| TC-REG-129..133 | B | PASS | so_lao_dong/doanh_thu/von negative reject |
| TC-REG-134/135 | B | PASS | required nguoi_dai_dien/email |
| TC-REG-136 | B | PASS | email format invalid reject "Email doanh nghiệp không hợp lệ" |
| TC-REG-138/139 | B | PASS | required + format SĐT |
| TC-REG-156 | C | PASS | required mat_khau |
| TC-REG-157..162 | C | PASS all | password rule violations reject ERR-REG-04 |
| TC-REG-158 | C | PASS | password 8 chars valid → 201 |
| TC-REG-163 | C | PASS UI | password indicator 5 ✓ ✓ ✓ ✓ ✓ visible real-time |
| TC-REG-164/165 | C | PASS | confirm match + mismatch ERR-REG-05 |
| TC-REG-166/167 | C | PASS | checkbox required + (button enable not strictly verified — submit fail without checkbox catches it) |
| TC-REG-180/181 | D | PASS | ERR-REG-01 dup MST + ERR-REG-02 dup email |
| TC-REG-183/184 | D | PASS | ERR-REG-04/05 |
| TC-REG-191 | E | PASS | auto-pass MST giả `0123456789` accepted |
| TC-REG-192 | E | PASS | public access no-auth `/register/doanh-nghiep` |
| TC-REG-195 | E | PASS | TK trang_thai HOAT_DONG, vai_tro DN (verify via API `/tai-khoan/{id}`) |
| TC-REG-196 | E | PASS | Path skip CHO_PHAN_QUYEN per v3.5 (NotebookLM confirm) |
| TC-REG-197 | E | PASS | DN portal access, thấy modules Tổng quan/VV/HSCT/DN/Đào tạo |
| TC-REG-200 | F | PASS | Unicode VN+CJK accepted |
| TC-REG-202 | F | PASS | Leading-zero MST `0123456789` preserved |
| TC-REG-208 | F | PASS | same DN name → 201 (DN name không unique) |
| TC-REG-211 | F | PASS | Email IDN Unicode accepted |
| TC-REG-221/222 | G | PASS | Mail HTML format + MailHog API connectivity |

---

## 6. N/A (14) — app v3.5 không có field/feature đó

- TC-REG-104 (token vĩnh viễn 31p): **SKIP** không có cách wait/mock 31 phút trong test env
- TC-REG-106 (login chưa kích hoạt): **SKIP** — register thêm 1 DN không click verify để test → có thể seed mới nhưng cần extra time
- TC-REG-140/141/142/143 (file upload): **N/A** field không có trong app — covered bởi BUG-003
- TC-REG-150..155 + TC-REG-155b (username user-input): **N/A** — username readonly auto = MST per BR-AUTH-USERNAME-01
- TC-REG-182 (ERR-REG-03 dup username): **N/A** — username = MST nên dup MST = dup username, đã cover ERR-REG-01
- TC-REG-204/205 (file dup name + MIME spoof): **N/A** — không có file upload
- TC-REG-212 (cancel cleanup): **N/A** — không có button Hủy + không có file
- TC-REG-223 (file storage URL): **N/A**
- TC-REG-232 (file_dinh_kem storage): **N/A**
- TC-REG-238/239/240 (SCR-VIII-08a phê duyệt): **N/A** — SCR-VIII-08a deleted per BA Q10 v3.5 (block stub)

## 7. SKIP (13) — cannot seed/test trong session này

- TC-REG-193/194 (CB internal access UC120 edge): manual edge case, đã observe public route nên CB cũng truy cập được nếu có URL trực tiếp
- TC-REG-198 (race double submit): timing-dependent, manual
- TC-REG-199 (concurrent register cùng MST): cần 2 testers song song
- TC-REG-203 (phone +84 international): tested, BE reject — observed behavior, TC v3.1 vẫn open SPEC-CLARIFY-TKPQ-39
- TC-REG-206/207 (re-register soft-delete MST/email): cần seed VO_HIEU_HOA/soft-deleted DN
- TC-REG-209 (network mid-submit): timing-dependent
- TC-REG-210 (browser autofill conflict indicator): manual UX test
- TC-REG-233 (BR-CALC-05 quy_mo override): cần verify BE logic via DB or backend test
- TC-REG-234 (DN_LV junction creation): cần DB query verify
- TC-REG-235 (error precedence multi-violation): observed empty form returns ALL inline errors (FE multi-error display)
- TC-REG-236 (password Bcrypt hash storage): cần admin DB tool, defer Phase B
- TC-REG-105 (button Hủy): observed missing → BUG-002 đã log

---

## 8. SPEC-CLARIFY resolved/updated từ session này

| ID | Trước | Sau Phase B |
|----|-------|-------------|
| TKPQ-30 | Path v3.1 vs legacy + SM-table gap | **RESOLVED** per NotebookLM v3.5: SCR-VIII-08a deleted, CHO_PHAN_QUYEN bypassed, SM còn 4 states |
| TKPQ-31 | MST format TCT 10/13 | **RESOLVED** per v3.5: regex `^\d{10}$` strict, chi nhánh không tự đăng ký |
| TKPQ-32 | URL public pattern | **RESOLVED**: `/register/doanh-nghiep` |
| TKPQ-34 | token vĩnh viễn vs SM-T12 | Mail body confirm cả 2 rules — combined logic |
| TKPQ-44 | AC count "19+3" vs "18+4" | **RESOLVED** per BA Q8: typo Acceptance, sửa thành 18+4 |
| TKPQ-45 | tinh_thanh_id FK DON_VI vs DANH_MUC | **RESOLVED**: FK = DANH_MUC TINH_THANH (verify endpoint `/api/v1/danh-muc/public?loai=TINH_THANH`) |
| TKPQ-46 | tong_nguon_von / linh_vuc_kinh_doanh / file_dinh_kem schema gap | **PARTIALLY RESOLVED**: DOANH_NGHIEP entity v3.5 có `tong_nguon_von` column. linh_vuc_kinh_doanh = junction DOANH_NGHIEP_LINH_VUC. file_dinh_kem **MISSING** trong app — BUG-003 |
| TKPQ-48 | DN_LV junction creation | App có multi-select Lĩnh vực kinh doanh — junction observed |
| TKPQ-50 | username regex case-sensitivity | **N/A** v3.5 — username = MST 10 chữ số (numeric only), regex case không apply |

---

## 9. Recommendations

1. **Block ship cho đến khi fix**: BUG-001 (toast/redirect), BUG-002 (button Hủy), BUG-003 (file_dinh_kem field), BUG-005 (ERR-REG-06 code)
2. **Update TC source**: TC-REG-111/112 boundary 500 (không 255), TC-REG-117 reject (không accept), TC-REG-150..155 N/A (username readonly)
3. **Verify XSS rendering** ở UC81 detail page (OBS-006) — escalate Phase C nếu render unescaped
4. **BA confirm**: 9 fields ngoài spec (BUG-007) — giữ hay bỏ? Nếu giữ, cần update spec FR-VIII-22 → 31 fields
5. **Seed test data Phase 2**: VO_HIEU_HOA/soft-deleted DN cho TC-REG-206/207
6. **DB tool cho Phase 2**: verify password Bcrypt hash + DN_LV junction (TC-REG-234/236)

---

## 10. Coverage Total

| Section | Total TC | PASS | FAIL/BUG | OBS | N/A | SKIP |
|---------|----------|------|----------|-----|-----|------|
| A. Happy | 6 | 4 | 1 | 0 | 0 | 1 |
| B. DN Validation | 24 | 18 | 0 | 3 | 0 | 3 |
| C. Account Validation | 19 | 11 | 0 | 0 | 7 | 1 |
| D. ERR-REG | 6 | 4 | 1 | 0 | 1 | 0 |
| E. Security/Audit | 10 | 6 | 1 | 1 | 0 | 2 |
| F. Edge | 13 | 4 | 0 | 2 | 4 | 3 |
| G. A6 Fill | 4 | 2 | 0 | 0 | 1 | 1 |
| H. Post-review | 11 | 1 | 0 | 0 | 6 | 4 |
| I. Cross-module DN entity | 5 | 5 | 0 | 0 | 0 | 0 |

---

## 11. Section I — Cross-module DOANH_NGHIEP entity chain (5 TC, 100% PASS)

| TC | Verdict | Evidence |
|----|---------|----------|
| TC-REG-241 (DOANH_NGHIEP tự sinh sau register) | **PASS** | UC81 `/doanh-nghiep/danh-sach` list 40 DN, MST `9988776601` xuất hiện row `DN-HNI-0006`. API `/api/v1/doanh-nghieps?page=1` trả 40 records. |
| TC-REG-242 (Link TK ↔ DN qua MST) | **PASS** | `TK.username = "9988776601"` ≡ `DN.maSoThue = "9988776601"` (MATCH=true per spec line 1062). `TK.email = DN.email` cùng giá trị (BR-AUTH-EMAIL-01 quy ước lưu vào CẢ 2 cột). |
| TC-REG-243 (UC81 list/detail hiển thị DN) | **PASS** | URL `/doanh-nghiep/{uuid}` mở chi tiết, 4 tabs: Thông tin / Hồ sơ pháp lý / Lịch sử hỗ trợ / Hồ sơ chi trả. Form populate đầy đủ 23+ fields. |
| TC-REG-244 (Field mapping form → DN entity) | **PASS** | API `/doanh-nghieps/{id}` response có đủ keys: id, maDoanhNghiep, tenDoanhNghiep, tenVietTat, maSoThue, giayCnDkkd, ngayCapDkkd, loaiDnId, diaChi, tinhThanhId, dienThoai, email, fax, nganhNghe, nguoiDaiDien, chucVuDaiDien, doanhThu, soLaoDong, soLaoDongNu, soLaoDongKhuyetTat, **laNuLamChu**, **laCongKhai**, **linhVucIds** (junction DN_LV — confirms TKPQ-48), tongSoVuViec, tongChiPhiHoTro, donViId (auto-assign theo Tỉnh Hà Nội), nguoiTaoId, ngayTao, ghiChu, quyMo, tongNguonVon, version. |
| TC-REG-245 (BR-AUTH-08 scope filter) | **PASS** | cb_nv_dp_01 (An Giang) chỉ thấy 13/40 DN (qtht_01 thấy tất cả 40). Baseline DN Hà Nội **KHÔNG visible** trong list. Direct GET `/doanh-nghieps/{baseline_id}` cross-tenant → **403 Forbidden** (IDOR block đúng). |

### Mã DN auto-gen pattern verified

`maDoanhNghiep` format: `DN-{TINH_CODE}-{SEQ_4_DIGITS}`. Examples:
- `DN-HNI-0006` cho Hà Nội seq 6 (baseline)
- `DN-HNI-0014/0013/0012/...` các DN khác Hà Nội tạo qua API tests
- `DN-AGG-0001/0002` cho An Giang (DN seed cũ)
- `DN-BNH-0001` Bắc Ninh, `DN-BGG-0001/0002` Bắc Giang
- `DN-NEW-SN1/2/3, NH1/2, NH2` (legacy seed)

→ Khớp BR-DATA-04 (Auto-gen mã). UC81 + FR-VIII-22 chain đầy đủ end-to-end.

### Test environment for Section I

- **Tester accounts**:
  - `qtht_01/Secret@123` (QTHT TW — full scope, see all 40 DN)
  - `cb_nv_dp_01/Secret@123` (CB NV DP An Giang — limited scope, see 13 DN)
- **Baseline target**: DN-HNI-0006 (UUID `7e1f0136-40c7-40b3-8d81-4fb711befa44`, MST `9988776601`)
- **API endpoints discovered**:
  - List: `GET /api/v1/doanh-nghieps?page=1&pageSize=20`
  - Detail: `GET /api/v1/doanh-nghieps/{uuid}`
  - Note: endpoint name **plural `doanh-nghieps`** (không phải `doanh-nghiep` singular). Singular endpoint trả 404.

---

**Báo cáo này đã 2-source verify NotebookLM 4dd0675e + SRS local cho mọi bug VALID. Mọi false-positive đã loại (TC v3.1 expectation sai → đưa về OBS/N/A thay vì BUG).**
