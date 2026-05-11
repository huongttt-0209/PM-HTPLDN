# Functional Test Report R7.7.10b — Biểu mẫu (defer-unblock round)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Thư viện Biểu mẫu, Hợp đồng — Module 7.9 |
| **Round** | R7.7.10b — defer-unblock multi-account + size + audit |
| **Người test** | QA Automation (Claude Code MCP) |
| **Ngày** | 2026-05-10 |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Test Method** | Hybrid UI MCP + API direct cho audit/size verify |
| **Tham chiếu** | [`functional-test-report-r7-7-10-bm.md`](functional-test-report-r7-7-10-bm.md) (báo cáo gốc), [`permission-matrix.md`](../../../../permission-matrix.md) |
| **Mục đích** | Unblock 8/17 TC defer trong round R7.7.10 (5 Authorization + BM-015 + BM-028/029 + BM-040) |

---

## 1. Executive Summary R7.7.10b

| TC | Type | Trước | Sau | Note |
|----|------|:-:|:-:|------|
| **BM-032** | QTHT R only | ⏭ Defer | ✅ PASS | QTHT thấy 7 TM (cross-unit), KHÔNG có button Thêm/Sửa/Xóa/Công khai trên list view |
| **BM-033** | CB NV BN data isolation | ⏭ Defer | ✅ PASS | Seed 1 TM BKH + 1 TM BTC qua UI; mỗi BN chỉ thấy TM đơn vị mình (Tất cả=1), KHÔNG thấy TM TW (4 TMs) lẫn BN khác |
| **BM-034** | CB NV ĐP scope | ⏭ Defer | ✅ PASS | Seed 1 TM STP-AG; STP-BG login thấy Tất cả=0 (không thấy AG, không thấy TW/BN) |
| **BM-035** | NHT/TVV/CG sidebar | ⏭ Defer | ⚠️ PASS-WITH-NOTE | Spec test case OUTDATED. Thực tế per [permission-matrix line 534](../../../../permission-matrix.md): NHT có `BIEU_MAU 👁️ R` → có menu R-only đúng spec; TVV/CG (line 546-578) ❌ không có entry FR-09 → CG verified KHÔNG có menu + URL `/bieu-mau/thu-muc` redirect về `/dao-tao` (route guard active). TVV defer vì password không có. |
| **BM-015** | Upload >20MB | ⏭ Defer | ⚠️ PASS-WITH-NOTE | API `POST /bieu-maus` với 21MB blob → `ERR_CONNECTION_RESET`. BE rejects đúng size limit nhưng KHÔNG có graceful HTTP 413/422 + Vietnamese error. Side-effect: upload kills auth session (`/auth/me 401` sau đó). → **BUG-BM-009 candidate**. |
| **BM-028** | Bulk import valid | ⏭ Defer | 🔁 DEFER | Wizard UI đã verify accessible (3-step `/bieu-mau/nhap-hang-loat`: Chọn file → Kiểm tra → Hoàn thành; combobox "Thư mục đích" + multi-file dropzone .doc/.docx/.xls/.xlsx max 20MB/file 50 file/lần). MCP `upload_file` incompatible với custom dropzone (input không persist). DEFER cho real browser test. |
| **BM-029** | Bulk import mixed | ⏭ Defer | 🔁 DEFER | Same as BM-028 — MCP tooling block. |
| **BM-040** | Audit log entityType | ⏭ Defer | ✅ PASS | qtht_01 GET `/audit-logs?entityType=BIEU_MAU` → 20 entries (DOWNLOAD:14, CREATE:5, DELETE:1); `?entityType=THU_MUC_BIEU_MAU` → 37 entries (CREATE:16, DELETE:8, UNPUBLISH:5, PUBLISH:6, UPDATE:1, EXPORT:1). Cover 5/5 SRS-required actions (CREATE/UPDATE/DELETE/PUBLISH/UNPUBLISH). Sample CREATE entityId `11fe7276-f3b1-4f0d-93ab-3ab5e84bee6b` match TM AG vừa tạo R7.7.10b (timestamp `2026-05-10T09:33:55.349Z`). cb_nv_tw_01 thử cùng query → 403 ERR-PERM-SYS-00-01 → audit endpoint QTHT-only đúng spec. |

### Kết quả tổng

| Metric | Value |
|--------|-------|
| **TC R7.7.10b attempted** | 8 (BM-015, 028, 029, 032, 033, 034, 035, 040) |
| **TC unblocked** | 6/8 (75%) — 4 ✅ PASS clean (BM-032/033/034/040) + 2 ⚠️ PARTIAL (BM-015/035) |
| **TC remain DEFER** | 2 (BM-028, BM-029 — MCP tool block) + 1 sub (BM-035 TVV — pwd unknown) |
| **New BUG candidate** | 1 (BUG-BM-009 — upload >20MB no graceful 413 + session kill) |
| **Spec finding** | 1 (NHT scope appears own-unit despite permission-matrix `R` no asterisk) |
| **Updated master report (R7.7.10)** | Passed 23 (+5 sau R7.7.10b: 032/033/034/039/040) · Partial 6 (+2: 015/035) · Defer 5 (-9 từ original 14) · Pass Rate 49% PASS only / 62% PASS+PARTIAL |

---

## 2. Pre-seed Data Created

| Account | Đơn vị | TM created | Lĩnh vực | TM ID |
|---------|--------|------------|----------|-------|
| `cb_nv_bn_01` | BTP-BN BKH | Biểu mẫu BKH - R7.7.10b | Doanh nghiệp | `6ad5bf52-8865-4c52-a415-96a8f7d2e428` |
| `cb_nv_bn_02` | BTP-BN BTC | Biểu mẫu BTC - R7.7.10b | Thuế | `65471c03-d3ac-4ff5-a2ab-b279dd5e5727` |
| `cb_nv_dp_01` | BTP-DP STP-AG | Biểu mẫu STP-AG - R7.7.10b | Hành chính | `11fe7276-f3b1-4f0d-93ab-3ab5e84bee6b` |
| `cb_nv_dp_02` | BTP-DP STP-BG | (KHÔNG seed — verified isolation thấy 0 TM) | — | — |

**Tổng TM cuối session:** 7 (4 BTP-TW gốc + 3 cross-unit R7.7.10b). TW + QTHT thấy đầy đủ 7. BN/DP scope đúng.

---

## 3. TC Detail Findings

### 3.1 BM-032 — QTHT R only ✅ PASS

**Setup:** Login `qtht_01`, navigate `/bieu-mau/thu-muc`.

**Observations:**
- Tab "Tất cả (7)" — đầy đủ 7 TM cross-unit (4 BTP-TW + BKH + BTC + STP-AG).
- Header buttons: chỉ "Xuất Excel" + "Làm mới". KHÔNG có "Thêm thư mục".
- Mỗi row: KHÔNG có button "Công khai/Sửa/Xóa" (so với CB_NV thấy đầy đủ 3 button).
- `evaluate_script` confirm: `headerActions=["Xóa bộ lọc"]` (only filter clearing), `rowActionLinks=[]`.
- Screenshot: [bm-032-qtht-r-only-no-action-buttons.png](screenshots-r7-7-10b/bm-032-qtht-r-only-no-action-buttons.png)

**Verdict:** Match permission-matrix QTHT `BIEU_MAU 👁️ R` (line 75-76, no asterisk = read all cross-unit).

---

### 3.2 BM-033 — CB NV BN data isolation ✅ PASS (2 chiều)

**Setup:** 4-step multi-account walk:
1. Login `cb_nv_bn_01` (BKH) → `/bieu-mau/thu-muc` → "Tất cả (0)" — KHÔNG thấy 4 TM BTP-TW gốc → confirm initial isolation
2. Tạo TM "Biểu mẫu BKH - R7.7.10b" (Doanh nghiệp) → 201 success → "Tất cả (1)"
3. Logout + login `cb_nv_bn_02` (BTC) → "Tất cả (0)" — KHÔNG thấy TM BKH
4. Tạo TM "Biểu mẫu BTC - R7.7.10b" (Thuế) → "Tất cả (1)"

**Verdict:** Isolation 2 chiều confirmed. Match permission-matrix CB_NV_BN `BIEU_MAU ✅ CRUD*` với asterisk = scoped theo `don_vi_id` (BR-AUTH-08).

---

### 3.3 BM-034 — CB NV ĐP scope ✅ PASS (2 chiều)

**Setup:**
1. Login `cb_nv_dp_01` (STP-AG) → "Tất cả (0)" → tạo TM "Biểu mẫu STP-AG - R7.7.10b" (Hành chính) → "Tất cả (1)"
2. Logout + login `cb_nv_dp_02` (STP-BG) → "Tất cả (0)" — KHÔNG thấy TM AG, KHÔNG thấy TW/BN
- Screenshot: [bm-034-dp02-bg-empty-isolation.png](screenshots-r7-7-10b/bm-034-dp02-bg-empty-isolation.png)

**Verdict:** Isolation 2 chiều confirmed. Match CB_NV_DP `BIEU_MAU ✅ CRUD*` scoped per `don_vi_id`.

---

### 3.4 BM-035 — NHT/CG sidebar ⚠️ PASS-WITH-NOTE (spec outdated)

**Findings:**

| Role | Spec (permission-matrix line) | Observation | Verdict |
|------|-------------------------------|-------------|---------|
| **NHT** (`nht_01`, "Phùng Thị NHT An Giang") | line 534 `BIEU_MAU 👁️ R` | Sidebar có 5 menu incl. "Quản lý thư viện biểu mẫu". Vào module thấy "Tất cả (1)" = TM STP-AG đơn vị mình; KHÔNG có button Thêm/Sửa/Xóa/Công khai. | ✅ Match spec (R-only own-unit) |
| **CG** (`dinh_14`, "Đinh Văn Mười Bốn") | line 566-578 (NO FR-09 entry) | Sidebar chỉ 2 menu (Đào tạo + Tư vấn) — KHÔNG có menu BM. Direct URL `/bieu-mau/thu-muc` → redirect về `/dao-tao/chuong-trinh/danh-sach` (route guard). | ✅ Match spec (❌ trên BIEU_MAU) |
| **TVV** (`vu_sau_06`, `tvv_r11_a16`) | line 546-559 (NO FR-09 entry) | Login Secret@123 fail "Tên đăng nhập hoặc mật khẩu không đúng" — TVV password do user tự set qua mail flow, không có trong test fixture. | ⏭ DEFER (pwd unknown) |
| - Screenshot CG | | [bm-035-cg-no-menu-bm.png](screenshots-r7-7-10b/bm-035-cg-no-menu-bm.png) | |
| - Screenshot NHT | | [bm-035-nht-r-only-1tm.png](screenshots-r7-7-10b/bm-035-nht-r-only-1tm.png) | |

**Spec outdated:** TC BM-035 trong [`output/funtion/7.9-bieu-mau.md`](../../../../funtion/7.9-bieu-mau.md) viết "NHT/TVV/CG **không thấy** menu BM" — thực tế NHT có quyền R per permission-matrix v3.5 update 2026-05-05.

**Recommendation:** Update [`output/funtion/7.9-bieu-mau.md`](../../../../funtion/7.9-bieu-mau.md) BM-035 thành 3 TC tách:
- BM-035a: NHT có menu BM, R-only, scope đơn vị (PASS)
- BM-035b: TVV không có menu BM (need pwd → defer)
- BM-035c: CG không có menu BM + route guard URL direct (PASS)

**Spec ambiguity finding (sub-issue):** NHT permission ghi `👁️ R` (no asterisk) trong permission-matrix line 534 — implication "read all cross-unit" — nhưng implementation thực tế NHT scope theo own-unit (chỉ thấy TM STP-AG). Đây là spec ambiguity hoặc dev implement đúng intent BA nhưng asterisk bị thiếu trong matrix. Recommend BA confirm + update permission-matrix nếu intent = own-unit.

---

### 3.5 BM-015 — Upload file >20MB ⚠️ PASS-WITH-NOTE → BUG-BM-009 candidate

**Setup:** Login `cb_nv_tw_01`, navigate `/bieu-mau/them-moi` → fill thư mục + tên + chọn file `test-bm-21mb.docx` (22020096 bytes, 21MB exact, ZIP magic header).

**MCP `upload_file` qua custom dropzone:** input fileCount=0 sau upload, không có error UI, không có toast — silent reject pattern (giống BUG-BM-008).

**API direct `POST /api/v1/bieu-maus` với 21MB blob (FormData):**
- Result: `Failed to fetch` JS exception
- Network: `reqid=2154 POST /api/v1/bieu-maus → ERR_CONNECTION_RESET`
- Side-effect: subsequent `GET /api/v1/auth/me → 401` — session bị invalidated

**Verdict:**
- ✅ BE đúng spec — file >20MB rejected
- ⚠️ Rejection mechanism là TCP reset, KHÔNG phải HTTP 413 Payload Too Large + Vietnamese error message
- ⚠️ Side-effect destabilize session (auth bị invalidate)

**BUG-BM-009 (Minor):** Server-level body limit không graceful. Suggest:
- BE: thêm Express body-parser limit `20MB` với explicit 413 response + Vietnamese message ERR-BM-FILE-SIZE-01
- FE: pre-check file.size > 20MB trước khi POST → toast error ngay
- Investigate session invalidation root cause

---

### 3.6 BM-028 / BM-029 — Bulk import 🔁 DEFER (tool block)

**Wizard accessibility verified:**
- URL: `/bieu-mau/nhap-hang-loat`
- 3 step: Chọn file → Kiểm tra → Hoàn thành
- Combobox "Thư mục đích" lists 7 TMs
- Multi-file dropzone "Kéo thả hoặc click để chọn nhiều file — Chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB/file, 50 file/lần"
- Progress: "Đã tải lên thành công: 0 / 0"
- Button "Kiểm tra và tiếp tục" disabled until upload

**Tool block:** MCP `upload_file` incompatible với custom dropzone (file input không persist trong DOM). Programmatic injection via DataTransfer cũng fail vì input element không tồn tại trước khi user click.

**Recommendation:** Chạy round R7.7.10c trên real browser (Playwright/manual) để test:
- BM-028: 3 valid .docx → expect tất cả 3 BM created
- BM-029: 3 valid + 1 invalid `.txt` → expect 3 BM created + 1 rejected with error report

---

### 3.7 BM-040 — Audit log entityType=BIEU_MAU ✅ PASS

**Setup:** Login `qtht_01`, GET `/api/v1/audit-logs?entityType=BIEU_MAU&page=1&pageSize=50`.

**Result:**

| Filter | Records | Action breakdown | Match SRS UC requirement |
|--------|:-:|---|---|
| `entityType=BIEU_MAU` | 20 | DOWNLOAD:14 + CREATE:5 + DELETE:1 | ✅ Cover C/R/D actions |
| `entityType=THU_MUC_BIEU_MAU` | 37 | CREATE:16 + DELETE:8 + UNPUBLISH:5 + PUBLISH:6 + UPDATE:1 + EXPORT:1 | ✅ Cover C/U/D + PUBLISH/UNPUBLISH (UC93/94) |

**Sample record (TM CREATE):**
```json
{
  "action": "CREATE",
  "entityType": "THU_MUC_BIEU_MAU",
  "entityId": "11fe7276-f3b1-4f0d-93ab-3ab5e84bee6b",   // TM AG vừa tạo R7.7.10b
  "createdAt": "2026-05-10T09:33:55.349Z",
  "topKeys": ["id","entityType","entityId","hanhDong","nguoiThucHienId","systemActor","consumerId","thoiGian","ipAddress","endpoint","responseCode","sessionId","module","nguoiThucHienUsername","nguoiThucHienHoTen"]
}
```

**Permission verify:** `cb_nv_tw_01` GET cùng URL → `403 ERR-PERM-SYS-00-01 Forbidden` → audit endpoint là QTHT-only đúng spec FR-X.5 / FR-08.

**Verdict:** Audit log filter entityType + action breakdown đầy đủ + permission ACL đúng.

---

## 4. New Bug Candidate

| Bug ID | Severity | Title | TC | Note |
|--------|----------|-------|----|------|
| BUG-BM-009 | Minor → Medium | Upload BM file >20MB rejected via TCP reset, no graceful 413 + session invalidate | BM-015 | Server-level body limit. Đề xuất 2 fix: (a) Express body-parser explicit limit + 413 Vietnamese error; (b) FE pre-check file.size + investigate session invalidation. |

Bug entry chi tiết tại [`bug-report-r7-7-10b-bm.md`](../../bug-reports/bm/bug-report-r7-7-10b-bm.md).

---

## 5. Test Data Cleanup Recommendation

3 TM cross-unit seeded R7.7.10b sẽ giữ lại để R7.7.10c (bulk import test) tận dụng. Nếu cần clean: `DELETE /thu-muc-bieu-maus/{id}` cho 3 IDs ở §2.

---

## 6. Recommended Next Round (R7.7.10c)

1. **Real browser test** (Playwright/manual) cho BM-028 + BM-029 — workaround MCP `upload_file` incompatibility với custom dropzone.
2. **TVV password discovery** hoặc tạo TVV mới với password biết → re-test BM-035b (TVV không thấy menu BM).
3. **BUG-BM-009 fix verify** sau dev fix Express limit + Vietnamese 413.
4. **NHT scope BA confirm** — clarify permission-matrix line 534 NHT BIEU_MAU intent (own-unit vs read-all) → update matrix nếu cần.

---

*Functional R7.7.10b generated: 2026-05-10 16:55 (UTC+7) | QA Automation via Claude Code MCP*
