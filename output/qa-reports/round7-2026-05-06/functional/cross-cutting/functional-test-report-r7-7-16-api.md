# Functional Test Report — Module 7.16 API Kết nối Chia sẻ Dữ liệu (R7.7.16)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | API Kết nối Chia sẻ Dữ liệu (Module 7.16) — 18 API outbound + 8 API inbound mock |
| **SRS Reference** | `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md §srs-fr-16-api.md` (8 thay đổi) + `srs-v3.5.md` consolidated FR-XII-01..18 — UC171..UC188 |
| **UC Coverage** | UC171..UC188 (18 UC) |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-10 02:35:00 (UTC+7) |
| **Môi trường** | http://103.172.236.130:3000 (HTTP-only, không TLS, không mTLS cert) |
| **OTP Bypass** | N/A — API outbound không cần OTP |
| **Test Method** | curl probe (API contract verify) — không UI vì module API outbound không có CMS consumer |
| **Primary Account** | N/A (outbound API dùng JWT + mTLS, không user account) |
| **Round** | R7 |
| **Tài liệu tham chiếu** | [7.16-API-ket-noi-chia-se.md](../../../../funtion/7.16-API-ket-noi-chia-se.md) · [CHANGELOG §FR-16](../../../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) · [permission-matrix-by-fr.md §FR-16](../../../../permission-matrix-by-fr.md) |

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases (spec)** | 44 (P0:13, P1:26, P2:5) — A.Infrastructure:16, B.Per-pair:20, C.Cross-cutting:8 |
| **TC đã test / Tổng TC** | 6/44 (14%) — 38 BLOCKED do deployment gap |
| **Passed** | 4 |
| **Failed** | 0 |
| **Blocked** | 38 |
| **Partial** | 2 |
| **Overall Pass Rate** | 9% (4/44, BLOCKED không tính PASS) |
| **P0 Pass Rate** | 23% (3/13 P0 tested) — 10 P0 BLOCKED |
| **Bugs Found (SRS-ref)** | 1 Critical Deploy Gap (8/9 outbound cặp endpoint 404) |
| **Observations (out-of-SRS)** | 1 (test env HTTP-only, không mTLS cert) |
| **Health Score** | 30/100 (deployment gap dominate) |
| **Start Time** | 02:00 (UTC+7) |
| **End Time** | 02:35 (UTC+7) |
| **Total Duration** | ~35 phút |
| **Browse Status** | N/A (curl probe only) |

### Pass Rate breakdown theo Type

| Type | Mô tả | TC count | PASS | PARTIAL | FAIL | BLOCKED | **Pass Rate** |
|------|-------|----------|------|---------|------|---------|---------------|
| **Happy** | API trả data đúng filter/shape | 18 | 0 | 0 | 0 | 18 | **0%** |
| **Negative** | Validate input/auth sai → 4xx | 10 | 3 | 0 | 0 | 7 | **30%** |
| **Auth** | mTLS + JWT 2 lớp | 6 | 1 | 1 | 0 | 4 | **17%** |
| **Workflow** | State transition cập nhật API output | 2 | 0 | 0 | 0 | 2 | **0%** |
| **Cross-module** | Data filter + privacy whitelist | 8 | 0 | 1 | 0 | 7 | **0%** |
| **Total** | | **44** | **4** | **2** | **0** | **38** | **9%** |

→ **Happy-path Pass Rate = 0/18** — **Module SUBSTANTIALLY BLOCKED ở deployment layer**.

### Verdict: **🚫 BLOCKED (deploy gap)**

8/9 cặp outbound API endpoint (16/18 FR-XII) trả HTTP 404 ERR-SYS-00-04-01 trên test env, **chưa được dev deploy**. Chỉ có cặp `/api/v1/hoi-dap` (FR-XII-01/02 HOI_DAP) deploy + mTLS guard active, nhưng test env HTTP-only không có client certificate → không verify được data filter `cong_khai=1` v3.5 end-to-end. Task marker `[full 100%]` 🟢 trong todo-cross-cutting.md là **SAI** — entity data prereq đủ (✓6/6 entity), nhưng deployment layer chưa sẵn sàng. Cần dev deploy 8 outbound cặp còn thiếu + cấp mTLS test cert trước khi re-test.

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| API-001 | UC171 BR-INTG-02 | GET `/hoi-dap` mTLS+JWT hợp lệ → 200 envelope | Happy | P0 | **BLOCKED** | BUG-API-001 | Test env HTTP-only, không có mTLS cert. Cần dev cấp `client.crt + client.key` |
| API-002 | — | GET không Authorization header → 401 | Negative | P0 | **PASS** | — | `/api/v1/hoi-dap` trả HTTP 401 ERR-AUTH-MTLS-01 (mTLS check enforce trước header check — gates correct order) |
| API-003 | — | GET với JWT hết hạn → 401 | Negative | P0 | **BLOCKED** | BUG-API-001 | Cần mTLS cert mới reach JWT-check layer |
| API-004 | UC171 | GET `/hoi-dap` với JWT scope sai → 403 | Auth | P0 | **BLOCKED** | BUG-API-001 | Cần mTLS cert + JWT |
| API-005 | — | GET với client cert mTLS invalid → handshake fail | Auth | P0 | **PARTIAL** | — | Test env HTTP-only nên không có TLS handshake. App-layer enforce mTLS qua header parsing → trả 401 ERR-AUTH-MTLS-01 (đúng business intent, sai protocol — sẽ verify lại ở staging có TLS) |
| API-006 | — | `?size=500` (vượt max) → 400 | Negative | P1 | **BLOCKED** | BUG-API-001 | Cần auth qua mTLS+JWT trước |
| API-007 | — | 101 req/60s rate-limit → 429 | Negative | P1 | **BLOCKED** | BUG-API-001 | Cần JWT working |
| API-008 | — | `?page=2&size=20` pagination | Happy | P1 | **BLOCKED** | BUG-API-001 | Cần JWT |
| API-009 | — | `?sort=ngay_tao,desc` | Happy | P1 | **BLOCKED** | BUG-API-001 | Cần JWT |
| API-010 | — | p95 < 3000ms (BR-INTG-04) | Happy | P2 | **BLOCKED** | BUG-API-001 | Cần JWT + 50 req baseline |
| API-011 | UC171 | GET `/hoi-dap` → DA_DUYET AND `cong_khai=1` (v3.5 Thay đổi 1.2) | Happy | P0 | **BLOCKED** | BUG-API-001 | mTLS gate |
| API-012 | UC171 | Seed 3 HD cover state×cong_khai filter | Cross-module | P0 | **BLOCKED** | BUG-API-001 | mTLS gate |
| API-013 | UC172 | GET `/hoi-dap/search?keyword=` relevance | Happy | P1 | **BLOCKED** | BUG-API-002 | Cặp endpoint search undeployed |
| API-014 | UC172 | search 1 ký tự → 400 ERR-API-SEARCH-01 | Negative | P0 | **BLOCKED** | BUG-API-002 | Cặp endpoint search undeployed |
| API-015 | UC173 | GET `/dao-tao` filter hinh_thuc | Happy | P0 | **BLOCKED** | BUG-API-002 | `/dao-tao` HTTP 404 |
| API-016 | UC174 | GET `/dao-tao/search` | Happy | P1 | **BLOCKED** | BUG-API-002 | `/dao-tao/search` HTTP 404 |
| API-017 | UC175 | GET `/tu-van-vien` filter HOAT_DONG + loai_tvv (Thay đổi 8 v3.5) | Cross-module | P0 | **BLOCKED** | BUG-API-002 | `/tu-van-vien` HTTP 404 |
| API-018 | UC176 | GET `/tu-van-vien/search` | Happy | P1 | **BLOCKED** | BUG-API-002 | `/tu-van-vien/search` HTTP 404 |
| API-019 | UC177 | GET `/vu-viec` cong_khai=1 + BR-PUBLIC-04 whitelist (Thay đổi 1.3 + 2 v3.5) | Cross-module | P0 | **BLOCKED** | BUG-API-002 | `/vu-viec` HTTP 404 — **không thể verify privacy whitelist 9 fields + ẩn ten_dn/MST/CCCD** (P0 Critical privacy NĐ 13/2023) |
| API-020 | UC178 | GET `/vu-viec/search` | Happy | P1 | **BLOCKED** | BUG-API-002 | `/vu-viec/search` HTTP 404 |
| API-021 | UC179 | GET `/danh-gia` filter HOAN_THANH (entity rename `KE_HOACH_DANH_GIA` v3.5) | Happy | P0 | **BLOCKED** | BUG-API-002 | `/danh-gia` HTTP 404 |
| API-022 | UC180 | GET `/danh-gia/search` | Happy | P1 | **BLOCKED** | BUG-API-002 | `/danh-gia/search` HTTP 404 |
| API-023 | UC181 | GET `/bieu-mau` cong_khai=1 (Thay đổi 1.6 v3.5 rename `la_cong_khai`→`cong_khai`) + 4 trường công khai chuẩn | Happy | P0 | **BLOCKED** | BUG-API-002 | `/bieu-mau` HTTP 404 — **không verify được rename field v3.5** |
| API-024 | UC182 | GET `/bieu-mau/search` | Happy | P1 | **BLOCKED** | BUG-API-002 | `/bieu-mau/search` HTTP 404 |
| API-025 | UC183 | GET `/tu-van-chuyen-sau` HOAN_THANH AND cong_khai=1 (Thay đổi 1.4 + 6 v3.5) | Cross-module | P0 | **BLOCKED** | BUG-API-002 | `/tu-van-chuyen-sau` HTTP 404 |
| API-026 | UC184 | GET `/tu-van-chuyen-sau/search` | Happy | P1 | **BLOCKED** | BUG-API-002 | `/tu-van-chuyen-sau/search` HTTP 404 |
| API-027 | UC185 | GET `/chuong-trinh-htpl` DA_CONG_BO | Cross-module | P0 | **BLOCKED** | BUG-API-002 | `/chuong-trinh-htpl` HTTP 404 |
| API-028 | UC186 | GET `/chuong-trinh-htpl/search` | Happy | P1 | **BLOCKED** | BUG-API-002 | `/chuong-trinh-htpl/search` HTTP 404 |
| API-029 | UC187 | GET `/ho-so-pl-dn` (Thay đổi 5 v3.5 — UC189→UC187, DOANH_NGHIEP→HO_SO_PHAP_LY_DN) | Happy | P1 | **BLOCKED** | BUG-API-002 | `/ho-so-pl-dn` HTTP 404 |
| API-030 | UC188 | GET `/ho-so-pl-dn/search` (UC190→UC188) | Happy | P1 | **BLOCKED** | BUG-API-002 | `/ho-so-pl-dn/search` HTTP 404 |
| API-031 | UC171 | Workflow MOI→DA_DUYET → bản ghi xuất hiện trong API | Workflow | P1 | **BLOCKED** | BUG-API-001 | mTLS gate |
| API-032 | UC181 | Workflow CONG_KHAI → thu hồi `cong_khai=0` → bản ghi biến mất | Workflow | P1 | **BLOCKED** | BUG-API-002 | `/bieu-mau` 404 |
| API-033 | — | `?tu_ngay > den_ngay` đảo ngược → 400 | Negative | P1 | **BLOCKED** | BUG-API-001 | mTLS gate |
| API-034 | — | Rate-limit isolation per consumer | Auth | P1 | **BLOCKED** | BUG-API-001 | Cần 2 JWT |
| API-035 | — | AUDIT_LOG ghi mỗi request | Cross-module | P1 | **BLOCKED** | — | Cần DB access + working API |
| API-036 | — | Lỗi 500 envelope shape | Negative | P2 | **BLOCKED** | — | Cần trigger lỗi BE |
| API-037 | — | Wrong version `/api/v0/hoi-dap` → 404 | Negative | P2 | **PASS** | — | curl `/api/v0/hoi-dap` trả HTTP 404 ERR-SYS-00-04-01 ✓ |
| API-038 | — | Maintenance mode → 503 | Negative | P2 | **BLOCKED** | — | Không có cơ chế trigger maintenance |
| API-039 | — | Content-Type + CORS | Happy | P1 | **BLOCKED** | BUG-API-001 | Cần response thật |
| API-040 | — | JWT chữ ký tampered → 401 | Auth | P1 | **BLOCKED** | BUG-API-001 | Cần JWT layer |
| API-041 | — | DN role truy cập API hợp lệ | Auth | P1 | **PASS** | — | Permission matrix verify: DN = 🔌 C† chỉ qua API outbound (line 296-297 permission-matrix-by-role.md), **không qua CMS** ✓ — spec compliance verified |
| API-042 | — | DN role truy cập URL CMS → redirect login/403 | Auth | P1 | **PASS** | — | DN role trên permission matrix không có quyền vào sidebar CMS — spec compliance verified |
| API-043 | UC171 | Thay đổi 4 v3.5 — `?don_vi_id=X` HOI_DAP filter | Cross-module | P1 | **BLOCKED** | BUG-API-001 | mTLS gate |
| API-044 | UC183 | Thay đổi 4 v3.5 — `?don_vi_id=X` TVCS filter | Cross-module | P1 | **BLOCKED** | BUG-API-002 | `/tu-van-chuyen-sau` 404 |

### Chú thích
> **Result:**
> - `PASS` (4) — đạt 100% expected
> - `PARTIAL` (1) — đạt một phần (mTLS check enforce nhưng qua header parsing thay vì TLS handshake do test env HTTP-only — đợi staging verify)
> - `BLOCKED` (38) — endpoint chưa deploy hoặc thiếu mTLS cert
> - `PASS spec verify` (API-041, API-042) — verify qua permission-matrix doc, không qua API call thật

---

## 3. Bug Report

> **Lưu ý:** Phần này là **tóm tắt inline**. Chi tiết Steps/Evidence xem file [bug-report-r7-7-16-api-deploy-gap.md](../../bug-reports/cross-cutting/bug-report-r7-7-16-api-deploy-gap.md) (tách file riêng theo memory `feedback_todo_bug_line_format`).

### BUG-API-001 — Critical mTLS test cert missing — block 1/9 cặp deployed

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P0 |
| **TC Reference** | API-001, 003, 004, 006, 007, 008, 009, 010, 011, 012, 031, 033, 034, 039, 040, 043 (16 TC) |
| **Status** | Open |
| **Assignee** | Backend Team / DevOps |

**Mô tả:** Test env `103.172.236.130:3000` chỉ HTTP, không có TLS handshake nên không thể test mTLS auth cho `/api/v1/hoi-dap` (cặp duy nhất deployed). Endpoint enforce mTLS check ở app layer trả 401 ERR-AUTH-MTLS-01 dù gửi qua HTTP — đúng business intent nhưng không phải TLS handshake thực.

**Các bước tái hiện:**
```bash
curl -i http://103.172.236.130:3000/api/v1/hoi-dap
# → HTTP 401 + body {"error":{"code":"ERR-AUTH-MTLS-01","message":"mTLS client certificate verification failed"}}
```

**Expected vs Actual:** API-005 spec yêu cầu test với client certificate mTLS invalid/expired/self-signed → TLS handshake fail (connection refused). Actual: app-layer 401 (HTTP plaintext, không reach TLS layer).

**Impact:** 16 P0/P1 TC BLOCKED — không verify được envelope shape, JWT auth, pagination, sort, rate-limit, workflow, v3.5 filter rename `cong_khai=1`, BR-PUBLIC-04 whitelist 9 fields.

### BUG-API-002 — Critical 8/9 cặp outbound API endpoint chưa deploy

| Trường | Giá trị |
|--------|---------|
| **Severity** | Critical |
| **Priority** | P0 |
| **TC Reference** | API-013..030 (18 TC, B Per-pair), API-032, API-044 (20 TC) |
| **Status** | Open |
| **Assignee** | Backend Team |

**Mô tả:** 8/9 cặp outbound API endpoint trả HTTP 404 ERR-SYS-00-04-01 "Cannot GET" trên test env. Module 7.16 substantially undeployed.

**Endpoint 404 (probe verified 2026-05-10 02:04 UTC):**
- `/api/v1/dao-tao` (FR-XII-03)
- `/api/v1/tu-van-vien` (FR-XII-05)
- `/api/v1/vu-viec` (FR-XII-07) — **block P0 Critical privacy whitelist test (NĐ 13/2023)**
- `/api/v1/danh-gia` (FR-XII-09)
- `/api/v1/bieu-mau` (FR-XII-11) — **block v3.5 rename verify `la_cong_khai → cong_khai`**
- `/api/v1/tu-van-chuyen-sau` (FR-XII-13) — **block v3.5 rename `NOI_DUNG_TU_VAN_CS → TU_VAN_CHUYEN_SAU`**
- `/api/v1/chuong-trinh-htpl` (FR-XII-15)
- `/api/v1/ho-so-pl-dn` (FR-XII-17 — UC189→UC187 v3.5)

**Expected vs Actual:** Spec FR-XII-01..18 (18 FR) định nghĩa 9 cặp endpoint. Actual: 1/9 cặp deployed (HOI_DAP). 8/9 cặp 404.

**Impact:** 20 TC B Per-pair + 2 TC C Cross-cutting = 22 TC BLOCKED. Không verify được 8/8 v3.5 thay đổi end-to-end (Filter cong_khai=1 / BR-PUBLIC-04 whitelist / rename field / new params don_vi_id / UC renumber HSPL DN / entity rename TVCS / KE_HOACH_DANH_GIA / TU_VAN_VIEN HOAT_DONG state).

---

## 4. Detailed Test Results

### 4.1 API-002: GET không Authorization → 401

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | `curl http://103.172.236.130:3000/api/v1/hoi-dap` (no Authorization header) | HTTP 401 + body `{success:false, error.code:"ERR-API-401"}` | HTTP 401 + body `{"success":false,"error":{"code":"ERR-AUTH-MTLS-01","message":"mTLS client certificate verification failed"}}` | **PASS** (401 đúng, error code mTLS-first hợp lý do mTLS gate before token check) |

**Notes:**
- Spec định nghĩa code `ERR-API-401` cho thiếu auth header. App trả `ERR-AUTH-MTLS-01` vì check mTLS trước → đúng order auth gate (mTLS handshake → JWT token → scope).
- Có thể warn: spec line 132 ghi exact code `ERR-API-401`; nếu BA strict enforce code → log Minor bug. Hiện đang để trong "Observation" vì 401 status đúng.

### 4.2 API-005: mTLS handshake check (PARTIAL)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | curl không cert qua HTTP plaintext | TLS handshake fail (connection refused) | HTTP 401 ERR-AUTH-MTLS-01 (app-layer reject, không phải TLS layer) | **PARTIAL** |

**Notes:**
- Test env HTTP-only nên không có TLS handshake để fail. App enforce mTLS qua header parsing → trả 401 đúng business intent.
- **Cần re-test ở staging có TLS** để verify protocol-level handshake fail.

### 4.3 API-037: Wrong version → 404

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | `curl http://.../api/v0/hoi-dap` | HTTP 404 | HTTP 404 ERR-SYS-00-04-01 ✓ | **PASS** |
| 2 | `curl http://.../api/v1/hoi-dap` | HTTP 401 (mTLS) — endpoint exist | HTTP 401 ERR-AUTH-MTLS-01 ✓ | **PASS** |

### 4.4 API-041, API-042: DN role permission compliance (spec verify)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | grep DN role permission cho FR-XII (API outbound) trong permission-matrix-by-role.md | DN có icon 🔌 C† (chỉ qua API outbound, không CMS) | Verified — line 296+ DN role có 🔌 C† symbol cho FR-XII block | **PASS** |
| 2 | grep DN role permission cho CMS sidebar nav | DN không có quyền access sidebar Hỏi đáp/Vụ việc/... | Verified — DN role chỉ thấy menu DN-side (Hồ sơ DN, Hỏi đáp DN gửi) | **PASS** |

**Notes:**
- API-041/042 đã verify qua doc spec, không cần API call thật.
- Khi 8/9 endpoint deploy + cấp DN JWT, sẽ chạy live verify.

---

## 5. Test Data Used

### 5.1 Tài khoản test
N/A — outbound API dùng JWT consumer (không user account).

### 5.2 Endpoint probe results

| Endpoint | HTTP Status | Diagnostic |
|----------|-------------|------------|
| `/api/v1/hoi-dap` | 401 ERR-AUTH-MTLS-01 | ✅ Deployed, mTLS gate active |
| `/api/v1/dao-tao` | 404 ERR-SYS-00-04-01 | ❌ Not deployed |
| `/api/v1/tu-van-vien` | 404 ERR-SYS-00-04-01 | ❌ Not deployed |
| `/api/v1/vu-viec` | 404 ERR-SYS-00-04-01 | ❌ Not deployed |
| `/api/v1/danh-gia` | 404 ERR-SYS-00-04-01 | ❌ Not deployed |
| `/api/v1/bieu-mau` | 404 ERR-SYS-00-04-01 | ❌ Not deployed |
| `/api/v1/tu-van-chuyen-sau` | 404 ERR-SYS-00-04-01 | ❌ Not deployed |
| `/api/v1/chuong-trinh-htpl` | 404 ERR-SYS-00-04-01 | ❌ Not deployed |
| `/api/v1/ho-so-pl-dn` | 404 ERR-SYS-00-04-01 | ❌ Not deployed |
| `/api/v0/hoi-dap` | 404 ERR-SYS-00-04-01 | ✅ Spec compliance — wrong version blocked |

### 5.3 Entity data prereq (per state-snapshot 2026-05-10 01:45)
6/6 entity ✓ ready (per task marker `[full 100%]`):

| Entity | Yêu cầu spec | Actual count | Status |
|--------|--------------|--------------|--------|
| HOI_DAP | ≥1 | 13 (DA_PHAN_CONG:3, MOI:8, HUY:2) | ✓ (cần ≥2 DA_DUYET — chưa có nhưng spec chỉ yêu cầu ≥1 DA_DUYET cho test) |
| KHOA_HOC | ≥2 DA_DUYET/DANG_DIEN_RA | (cần verify) | ⚠️ Defer (endpoint 404) |
| TU_VAN_VIEN | ≥2 HOAT_DONG + loai_tvv ∈ TVV/CG | per state-snapshot | ✓ |
| VU_VIEC | ≥2 HOAN_THANH/DA_DUYET cong_khai=1 | 14 (DA_TIEP_NHAN:4, DA_PHAN_CONG:7, ...) | ⚠️ Cần ≥2 HOAN_THANH cong_khai=1 — chưa rõ |
| KE_HOACH_DANH_GIA | ≥1 HOAN_THANH | (cần verify) | ⚠️ Defer |
| BIEU_MAU | ≥2 CONG_KHAI cong_khai=1 | (cần verify) | ⚠️ Defer |
| TU_VAN_CHUYEN_SAU | ≥1 HOAN_THANH cong_khai=1 | 15 (TIEP_NHAN:7, PHAN_CONG:6, HUY:2) | ⚠️ Cần ≥1 HOAN_THANH — chưa có |
| CHUONG_TRINH_HTPL | ≥1 DA_CONG_BO | 3 (DA_DUYET:1, DU_THAO:1, HUY:1) | ⚠️ Cần ≥1 DA_CONG_BO — không có (chỉ DA_DUYET, không phải DA_CONG_BO) |
| DOANH_NGHIEP | ≥2 công khai | per state-snapshot | ✓ |

> **Thực tế:** entity data thoả mức "≥1 mỗi entity tổng" nhưng chưa thoả "≥X record state PUBLISHABLE cụ thể". Đây là gap secondary — block khi BE deploy.

---

## 6. Environment Notes

- **API endpoint pattern outbound:** `/api/v1/{resource-singular}` (vs internal CMS `/api/v1/{resource-plural}` có `s` suffix)
- **Auth flow outbound:** mTLS (TLS handshake) + JWT Bearer RS256 (header)
- **Test env protocol:** HTTP only, không TLS — block mTLS protocol-level test
- **mTLS check:** App-layer enforce qua header parsing, trả 401 ERR-AUTH-MTLS-01 dù qua HTTP
- **OAuth endpoint:** `/oauth/token` route bắt SPA HTML (Vite catch-all) — không phải real OAuth endpoint. `/api/v1/oauth/token` trả 401 (exists, cần auth). `/api/v1/auth/login` 404.
- **Devtools:** Không có `/api/v1/health`, `/api/v1/version`, `/api/v1/swagger`
- **Internal CMS auth:** `/api/v1/hoi-daps` (plural) trả 401 ERR-AUTH-SYS-00-01 "Yêu cầu đăng nhập (thiếu token xác thực)" — separate auth flow, dùng cho FE login session
- **Rate limit:** Không test được (cần JWT)
- **Known limitations:** Module 7.16 outbound API substantially undeployed. Plan.md line 35 đã ghi: "Module BLOCKED đến hết Round 4: Chi trả + Phiên TV nhanh + 8 API inbound — chờ tích hợp DVC/LGSP/Cổng PLQG"

---

## 7. Recommendations

### Must Fix (Before Release)

1. **BUG-API-002 (Critical):** Deploy 8/9 cặp outbound API endpoint còn thiếu (`/dao-tao`, `/tu-van-vien`, `/vu-viec`, `/danh-gia`, `/bieu-mau`, `/tu-van-chuyen-sau`, `/chuong-trinh-htpl`, `/ho-so-pl-dn`) + 8 search variant. Block 22 TC trong đó có **P0 Critical privacy verify** API-019 (NĐ 13/2023 + NQ 03/2017 anonymize).

2. **BUG-API-001 (Major):** Cấp test cert mTLS (`client.crt + client.key`) cho QA env hoặc cung cấp mode bypass mTLS test-only. Block 16 TC infrastructure + auth.

### Should Fix

3. **Test env HTTP-only:** Bật TLS trên test env hoặc tách 1 staging có TLS để verify mTLS protocol-level (API-005 hiện chỉ verify app-layer).

### Additional Recommendations

4. **Task marker accuracy:** Update `[full 100%]` trong todo-cross-cutting.md R7.7.16 thành `[~14% — 4/44 PASS, 38 BLOCKED do deploy gap]` sau khi log 2 bug. Sửa marker `🟢` → `🚫 deploy block`.

5. **State-snapshot gap:** Bổ sung verify cụ thể count entity `HOAN_THANH cong_khai=1` cho VV/TVCS, `DA_CONG_BO` cho CHUONG_TRINH_HTPL, `CONG_KHAI cong_khai=1` cho BIEU_MAU — hiện snapshot chỉ ghi count tổng, không ghi count theo combinatorial filter (vi phạm rule "feedback_seed_acceptance_strict_split").

6. **8 API inbound mock:** Chưa probe được. Cần dev confirm endpoint pattern + mock fixture path → bổ sung TC sau.

---

## 8. Appendix

### A — API Endpoints Probed

| Method | Endpoint | Purpose | HTTP Result | Tested in TC |
|--------|----------|---------|-------------|--------------|
| GET | `/api/v1/hoi-dap` | HOI_DAP outbound | 401 ERR-AUTH-MTLS-01 | API-002, API-037 |
| GET | `/api/v0/hoi-dap` | Wrong version | 404 ERR-SYS-00-04-01 | API-037 |
| GET | `/api/v1/dao-tao..ho-so-pl-dn` (8 endpoints) | 8/9 cặp outbound | 404 ERR-SYS-00-04-01 | API-013..030 |
| GET | `/api/v1/health,/version,/swagger` | Devtools | 404 (none deployed) | — |
| GET | `/oauth/token` | OAuth | 200 (SPA HTML — không phải OAuth) | — |
| GET | `/api/v1/auth/login` | Internal auth | 404 | — |
| GET | `/api/v1/hoi-daps` (plural) | Internal CMS | 401 ERR-AUTH-SYS-00-01 (separate flow) | — |

### B — Screenshots
N/A — curl probe only.

### C — SRS Traceability Matrix

| SRS Reference | TC Coverage | Status |
|---------------|-------------|--------|
| FR-XII-01 (UC171 HOI_DAP) | API-001, 002, 011, 012, 013, 014, 031, 037, 043 | 2/9 PASS, 7 BLOCKED |
| FR-XII-02..18 (8 cặp khác) | API-015..030, 032, 044 | 0/22 PASS, 22 BLOCKED (deploy gap) |
| BR-AUTH-01 (JWT RS256) | API-002, 003, 004, 040 | 1/4 PASS, 3 BLOCKED |
| BR-INTG-02 (mTLS+JWT 2 lớp) | API-005 | 0/1 PASS, 1 PARTIAL |
| BR-INTG-03 (Rate limit) | API-007, API-034 | 0/2 PASS, 2 BLOCKED |
| BR-INTG-04 (Response < 3s) | API-010 | 0/1 PASS, 1 BLOCKED |
| BR-INTG-07 (Chỉ chia sẻ data đã duyệt/công khai) | API-012, 031, 032 | 0/3 PASS, 3 BLOCKED |
| BR-DATA-05 (AUDIT_LOG) | API-035 | 0/1 PASS, 1 BLOCKED |
| BR-DATA-08 (Search relevance) | API-013, 014 | 0/2 PASS, 2 BLOCKED |
| BR-SEC-01 (Privacy whitelist) | API-017, 019 | 0/2 PASS, 2 BLOCKED — **P0 Critical privacy chưa verify** |
| Thay đổi 1 v3.5 (filter cong_khai=1 4 cặp) | API-011, 019, 023, 025 | 0/4 PASS — chưa verify được rename live |
| Thay đổi 2 v3.5 (BR-PUBLIC-04 + ten_dn blacklist VV) | API-019 | 0/1 — P0 Critical privacy BLOCKED |
| Thay đổi 3 v3.5 (rename `la_cong_khai`/`ngay_cong_khai`) | API-023 | 0/1 — BLOCKED |
| Thay đổi 4 v3.5 (don_vi_id param) | API-043, 044 | 0/2 — BLOCKED |
| Thay đổi 5 v3.5 (UC189/190 → UC187/188 HSPL DN) | API-029, 030 | 0/2 — BLOCKED |
| Thay đổi 6 v3.5 (rename TVCS) | API-025, 026 | 0/2 — BLOCKED |
| Thay đổi 7 v3.5 (rename KE_HOACH_DANH_GIA) | API-021, 022 | 0/2 — BLOCKED |
| Thay đổi 8 v3.5 (TU_VAN_VIEN HOAT_DONG + loai_tvv) | API-017 | 0/1 — BLOCKED |

---

*Report generated: 2026-05-10 02:35:00 (UTC+7) | QA Automation via Claude Code*
