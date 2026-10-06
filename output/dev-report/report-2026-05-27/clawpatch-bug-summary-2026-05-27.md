# Báo cáo Bug Tổng hợp (clawpatch)

**Ngày generate:** 2026-05-27
**Tool:** clawpatch + Codex CLI (codex-cli 0.133.0)
**Branch:** rebuild-fe-visual
**Repo:** `source_code`

**Báo cáo gốc đầy đủ (1.7 MB):** [`.clawpatch/reports/20260527T002749-c6f72f.md`](../source_code/.clawpatch/reports/20260527T002749-c6f72f.md)

---

## 1. Tổng quan

- **Tổng số finding:** 881
- **Open:** 876 | **Uncertain:** 5

### Theo mức độ (severity)

| Severity | Số lượng | % |
|----------|---------:|---:|
| **HIGH** | 87 | 9.9% |
| **MEDIUM** | 600 | 68.1% |
| **LOW** | 194 | 22.0% |

### Theo phân loại (category)

| Category | Tổng | High | Medium | Low |
|----------|-----:|-----:|-------:|----:|
| bug | 328 | 13 | 232 | 83 |
| api-contract | 196 | 3 | 143 | 50 |
| security | 111 | 35 | 73 | 3 |
| data-loss | 73 | 14 | 57 | 2 |
| concurrency | 67 | 11 | 52 | 4 |
| build-release | 53 | 11 | 39 | 3 |
| test-gap | 43 | 0 | 2 | 41 |
| performance | 8 | 0 | 2 | 6 |
| docs-gap | 1 | 0 | 0 | 1 |
| maintainability | 1 | 0 | 0 | 1 |

### Theo triage

| Triage | Số lượng |
|--------|---------:|
| confirmed-bug | 432 |
| risk | 209 |
| contract-mismatch | 196 |
| test-gap | 43 |
| docs-gap | 1 |

---

## 2. Ý nghĩa các trường

- **severity**: mức ảnh hưởng. `high` = cần xử lý sớm; `medium` = lỗi xác nhận nhưng tác động vừa; `low` = nhỏ/đề xuất.
- **category**:
  - `security` — lỗ hổng bảo mật (RLS bypass, AuthZ, injection, etc.)
  - `bug` — lỗi logic.
  - `data-loss` — mất hoặc sai lệch dữ liệu (import/export, round-trip).
  - `api-contract` — frontend/backend lệch contract (DTO, response shape).
  - `concurrency` — race condition, transaction, lock.
  - `build-release` — script build, CI, release.
  - `performance` — N+1, query chậm.
  - `test-gap` — thiếu test coverage cho path quan trọng.
- **triage**: `confirmed-bug` (chắc chắn lỗi), `risk` (rủi ro), `contract-mismatch` (lệch contract), `test-gap` (thiếu test).
- **status**: `open` (chưa fix), `uncertain` (chờ xác minh).

---

## 3. Danh sách HIGH severity (87 findings)

> Đây là các vấn đề được clawpatch đánh dấu mức cao nhất. Cần ưu tiên review và fix.

### 3.1 Bảo mật (Security) — 35 findings

#### #1. Assigned-scope users can read unassigned case timelines

- **ID:** `fnd_sig-feat-library-4879d8b29e-ce12_cdb15ea357`
- **Feature:** `feat_library_4879d8b29e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/vu-viec/vu-viec.controller.ts:443-451 (`VuViecController.getLichSu`)`
- `packages/api/src/modules/vu-viec/vu-viec.service.ts:1287-1308 (`VuViecService.getLichSu`)`
- `packages/api/src/modules/vu-viec/vu-viec.service.ts:2029-2072 (`VuViecService.findOne`)`

**Giải thích:**

> The detail read path explicitly enforces assignment scoping for TVV/CG/NHT via assertAssignmentAccess, but the timeline path bypasses that helper. TenantScoped only validates tenant/don_vi reachability, so an assignment-scoped user with Read on VuViec can request /vu-viecs/:id/lich-su for another case in the same unit and receive audit history, including old/new payloads and rejection reasons.

**Khuyến nghị fix:**

> Reuse findOne(vuViecId) or call assertSameDonVi plus assertAssignmentAccess before building the audit_log query in getLichSu.

---

#### #2. Attachment IDs are linked under system bypass without tenant or ownership checks

- **ID:** `fnd_sig-feat-library-7ec5f36678-3089_896469aae4`
- **Feature:** `feat_library_7ec5f36678`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/chi-tra/intake/chi-tra-intake.controller.ts:31-34 (`ChiTraIntakeController.tiepNhanDvc`)`
- `packages/api/src/modules/chi-tra/intake/chi-tra-intake.service.ts:170-171 (`ChiTraIntakeService.intakeFromDvc`)`
- `packages/api/src/modules/chi-tra/intake/chi-tra-intake.service.ts:176-189 (`ChiTraIntakeService.intakeFromDvc`)`

**Giải thích:**

> Because the attachment lookup runs inside the TW system bypass and filters only by file ID, RLS does not protect tenant ownership here. Any valid `fileDinhKemIds` value accepted from the DVC payload can be attached to the new dossier, even if the file belongs to another tenant or is already linked to another entity. That is both a cross-tenant permission gap and a data-corruption risk because existing `entityType/entityId` values are overwritten.

**Khuyến nghị fix:**

> Validate every file before linking: require it to belong to the resolved `donViId` or to a verifiable staging token for this intake, and require it to be unlinked or explicitly linkable. Reject mismatches instead of mutating them under the system bypass.

---

#### #3. Audit retention SECURITY DEFINER helpers are executable too broadly

- **ID:** `fnd_sig-feat-library-26ba3911c8-2d09_8bd4995f92`
- **Feature:** `feat_library_26ba3911c8`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050202000-AuditRetention.ts:39-43 (`AuditRetention2026050202000.up`)`
- `packages/api/src/database/migrations/2026050202000-AuditRetention.ts:74-78 (`AuditRetention2026050202000.up`)`
- `packages/api/src/database/migrations/2026050202000-AuditRetention.ts:90-94 (`purge_audit_log_partitions_before`)`
- `packages/api/src/database/migrations/2026050202000-AuditRetention.ts:113-115 (`purge_audit_log_partitions_before`)`

**Giải thích:**

> The migration creates SECURITY DEFINER functions but never revokes the default EXECUTE privilege from PUBLIC or grants a narrower role. Because purge runs with definer privileges and only enforces a one-year floor, any database role with EXECUTE can drop audit partitions well before the documented seven-year retention window; placing public before pg_catalog in the definer search_path also weakens the intended hardening.

**Khuyến nghị fix:**

> In a follow-up migration, REVOKE EXECUTE on both functions from PUBLIC, grant only the exact retention role/application role that needs them, enforce the seven-year cutoff inside purge_audit_log_partitions_before, and set search_path to pg_catalog with schema-qualified public.audit_log/public partitions.

---

#### #4. BaiGiang and DeKiemTra list queries bypass app-layer tenant filters

- **ID:** `fnd_sig-feat-library-23dc27379d-84e1_5bbd2b43f6`
- **Feature:** `feat_library_23dc27379d`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/dao-tao/bai-giang.service.ts:88-90 (`BaiGiangService.findAll`)`
- `packages/api/src/modules/dao-tao/de-kiem-tra.service.ts:490-497 (`DeKiemTraService.findAll`)`
- `packages/api/src/modules/dao-tao/chuong-trinh-dao-tao.service.ts:104-107 (`ChuongTrinhDaoTaoService.buildListQueryBuilder`)`

**Giải thích:**

> Collection routes marked with @TenantScoped rely on the service query builder to apply app-layer RLS predicates. These two list methods build from getRlsSafeRepo().createQueryBuilder, which the CTDT service comments identify as only pinning the QueryRunner and not applying applyRlsFilters. As a result, GET /bai-giangs and GET /de-kiem-tras can return rows from other units when database RLS is not the active enforcement layer or is bypassed by the app role.

**Cách tái hiện:**

> Seed BaiGiang or DeKiemTra rows for two don_vi_id values, authenticate as one non-TW unit, then call the list endpoint. The query has no bg.don_vi_id/dkt.don_vi_id predicate, so rows from both units can be returned.

**Khuyến nghị fix:**

> Build these list queries with tenantBaiGiangRepo.getRlsSafeQueryBuilder('bg') and tenantDeKiemTraRepo.getRlsSafeQueryBuilder('dkt') before adding joins and filters. Add unit tests asserting getRlsSafeQueryBuilder is used, plus an integration test with two tenants.

---

#### #5. Bulk import and folder aggregate paths bypass the request RLS connection

- **ID:** `fnd_sig-feat-library-c4299c692e-c68b_3d147bc2f4`
- **Feature:** `feat_library_c4299c692e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/bieu-mau/bieu-mau.service.ts:876-887 (`BieuMauService.confirmImport`)`
- `packages/api/src/modules/bieu-mau/bieu-mau.service.ts:917-938 (`BieuMauService.confirmImport`)`
- `packages/api/src/modules/bieu-mau/thu-muc-bieu-mau.service.ts:61-66 (`ThuMucBieuMauService.getRequestQueryRunner`)`
- `packages/api/src/modules/bieu-mau/thu-muc-bieu-mau.service.ts:634-658 (`ThuMucBieuMauService.saveBatchAuditLog`)`
- `packages/api/src/modules/bieu-mau/thu-muc-bieu-mau.service.ts:704-737 (`ThuMucBieuMauService.countActiveBieuMau`)`

**Giải thích:**

> This module documents that tenant-scoped mutations must reuse the CLS-pinned QueryRunner because the request RLS GUCs are local to that connection. confirmImport opens a fresh QueryRunner and performs FileDinhKem, BieuMau, and AuditLog operations on it. The folder count and batch audit helpers also use fresh DataSource access. Under fail-closed RLS this can make imports fail or silently miss file updates, make soBieuMau counts report zero, turn delete guards into FK-level 500s, and drop batch audit logs while only warning.

**Cách tái hiện:**

> Run import confirmation or folder list/delete under a real non-BYPASSRLS app role with RLS enabled. The fresh connection has no app.current_* settings, so tenant-scoped reads/writes do not see the same rows as the request-scoped repository.

**Khuyến nghị fix:**

> Route these operations through the CLS request QueryRunner manager or explicitly apply the same RLS GUCs to any dedicated transaction before touching tenant-scoped tables. Also check UpdateResult.affected for FileDinhKem and folder/template updates instead of treating zero-row writes as success.

---

#### #6. Client assertions can omit or overextend exp

- **ID:** `fnd_sig-feat-library-10582b7f1a-106f_d18c0addf8`
- **Feature:** `feat_library_10582b7f1a`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/api-public/services/api-consumer.service.ts:41-42 (`ApiConsumerService.authenticateWithAssertion`)`
- `packages/api/src/modules/api-public/services/api-consumer.service.ts:79-85 (`ApiConsumerService.authenticateWithAssertion`)`
- `packages/api/src/modules/api-public/services/api-consumer.service.spec.ts:24-31 (`signAssertion`)`

**Giải thích:**

> The documented contract requires a short-lived assertion, but jsonwebtoken only validates exp when the claim exists and this code never checks the verified payload for a numeric exp or a maximum future lifetime. A signed assertion with no exp, or with an exp far in the future, still satisfies issuer/subject/audience/signature and is accepted. That weakens replay resistance for the token endpoint.

**Cách tái hiện:**

> Sign an RS256 client_assertion with matching iss/sub/aud but no exp claim, store the matching public key and fingerprint for the consumer, then call authenticateWithAssertion; jwtVerify accepts it because no maxAge or explicit exp requirement is configured.

**Khuyến nghị fix:**

> After verification, require a numeric exp claim and reject assertions whose exp is missing, already expired, or beyond the allowed assertion lifetime. Consider also enforcing iat/nbf and aligning clockTolerance with the documented tolerance.

---

#### #7. Default admin password can create an active superuser

- **ID:** `fnd_sig-feat-library-fe878c98a9-d0ea_f7081345df`
- **Feature:** `feat_library_fe878c98a9`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/seeds/admin.seed.ts:18-19`
- `packages/api/src/database/seeds/admin.seed.ts:37-50 (`AdminSeed.run`)`
- `packages/api/package.json:26`

**Giải thích:**

> Running the seed without ADMIN_PASSWORD provisions username admin as an active account using the hard-coded Secret@123 password. The fallback is not gated to development/test, so the same seed command can create known production credentials.

**Khuyến nghị fix:**

> Require ADMIN_PASSWORD for any non-explicit development flow, reject known default values, and only allow a dev fallback behind an explicit local-only flag.

---

#### #8. Denied actions remain enabled when the child explicitly passes disabled={false}

- **ID:** `fnd_sig-feat-ui-flow-188cae5616-279c_8dafc0fc82`
- **Feature:** `feat_ui-flow_188cae5616`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/components/PermissionAction/permission-action.tsx:54-58 (`PermissionAction`)`
- `packages/web/src/components/PermissionAction/permission-action.test.tsx:40-58 (`PermissionAction denied test`)`

**Giải thích:**

> The denied branch is supposed to force-disable the wrapped action, but the nullish coalescing expression preserves any explicit boolean value from the child. A common caller pattern like <Button disabled={isPending}> passes disabled={false} when not pending; in that case PermissionAction clones the child with disabled: false even though ability.can(...) denied access, leaving the unauthorized action clickable and able to fire its onClick/network mutation. The existing denied test only covers an omitted disabled prop, so it passes while this common explicit-false case remains broken.

**Cách tái hiện:**

> Render PermissionAction with a denied ability and a child <Button disabled={false} onClick={handler}>. The button is not disabled and clicking it invokes handler.

**Khuyến nghị fix:**

> Force disabled on permission denial unless the existing prop is already true, e.g. disabled: true or disabled: children.props.disabled === true ? true : true. If preserving caller state matters for diagnostics, preserve it separately, but do not allow false to override a permission denial.

---

#### #9. Expired pending accounts can still activate through Redis first-login tickets

- **ID:** `fnd_sig-feat-library-bb39f9f67c-6622_31155e416f`
- **Feature:** `feat_library_bb39f9f67c`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/auth/auth.constants.ts:3-5 (`ACCOUNT_ACTIVATION_GRACE_MS`)`
- `packages/api/src/modules/auth/auth.service.ts:193-200 (`AuthService.login`)`
- `packages/api/src/modules/auth/auth.service.ts:466-475 (`AuthService.firstLoginSetPassword`)`
- `packages/api/src/modules/auth/auth.service.ts:487-499 (`AuthService.firstLoginSetPassword`)`
- `packages/api/src/modules/auth/auth.service.spec.ts:564-590 (`AuthService firstLoginSetPassword spec`)`
- `_…1 vị trí khác_`

**Giải thích:**

> The 7-day grace guard is only applied in the DB activation-token fallback branch. The normal first-login Redis ticket path, which is created by login() for any CHO_KICH_HOAT account, skips the ngayTao check and proceeds to activate under the lock. During the daily cron gap, or if the expiry job is delayed, an account older than 7 days can still set a password and, when it has a role, receive a session.

**Cách tái hiện:**

> Leave a CHO_KICH_HOAT account older than 7 days with an active role before the expiry job changes it. Log in with the temporary password to receive changePasswordToken, then call POST /auth/first-login-password. The Redis-ticket branch activates and can issue tokens instead of returning ACTIVATE_TOKEN_EXPIRED.

**Khuyến nghị fix:**

> Apply the ACCOUNT_ACTIVATION_GRACE_MS check to the Redis-ticket path as well, preferably inside the pessimistic-lock transaction against the locked user row. Also consider refusing to issue a first-login ticket from login() for already-expired pending accounts.

---

#### #10. Final paid and rejected dossiers can still accept file mutations

- **ID:** `fnd_sig-feat-library-4b3e6cdceb-db72_4ff795a6f3`
- **Feature:** `feat_library_4b3e6cdceb`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/chi-tra/chi-tra-file-policy.provider.ts:9-10 (`LOCKED_STATES`)`
- `packages/api/src/modules/chi-tra/chi-tra-file-policy.provider.ts:24-30 (`ChiTraFilePolicyProvider.canAttach`)`
- `packages/api/src/modules/chi-tra/chi-tra-file-policy.provider.ts:59-66 (`ChiTraFilePolicyProvider.canDelete`)`
- `packages/api/src/modules/chi-tra/chi-tra.service.ts:1430-1434 (`ChiTraService.capNhatThanhToan`)`
- `packages/api/src/modules/chi-tra/chi-tra.service.spec.ts:353`

**Giải thích:**

> The file policy locks legacy state names, but the module uses DA_THANH_TOAN/TU_CHOI/HUY as terminal or processed states. Because canAttach and canDelete only block LOCKED_STATES, a same-unit CB_NV user can still attach or delete files after final payment or rejection, which undermines audit integrity for financial records.

**Cách tái hiện:**

> Mock an HSCT row with trangThai='DA_THANH_TOAN', donViId='dv-1' and call canAttach/canDelete with user.vaiTro=['CB_NV_DP'], user.donViId='dv-1'. Both return true because DA_THANH_TOAN is not in LOCKED_STATES.

**Khuyến nghị fix:**

> Replace LOCKED_STATES with the actual terminal states from TrangThaiHoSoChiTra, at minimum DA_THANH_TOAN, TU_CHOI, and HUY, and use the enum instead of raw strings.

---

#### #11. IP whitelist trusts spoofable X-Forwarded-For values

- **ID:** `fnd_sig-feat-library-2b7d8128c5-e84b_fb29df1afc`
- **Feature:** `feat_library_2b7d8128c5`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/common/guards/ip-whitelist.guard.ts:32-37 (`IpWhitelistGuard.canActivate`)`
- `packages/api/src/common/guards/ip-whitelist.guard.spec.ts:38-44 (`IpWhitelistGuard spec`)`

**Giải thích:**

> The guard authorizes the first X-Forwarded-For address whenever the header is present, without checking whether the immediate peer is a trusted proxy or whether the proxy sanitized that header. A direct caller can set X-Forwarded-For to any whitelisted IP and bypass the socket.remoteAddress check, making the IP whitelist ineffective for the external API-key intake path unless every deployment layer strips or overwrites the header perfectly.

**Cách tái hiện:**

> Create a request with sourceSystem.duLieuMoRong.ip_whitelist = ['203.0.113.10'], socket.remoteAddress = '198.51.100.5', and headers['x-forwarded-for'] = '203.0.113.10'. IpWhitelistGuard.canActivate returns true.

**Khuyến nghị fix:**

> Only honor forwarded client IPs when the immediate remote address is a configured trusted proxy, or delegate to Express req.ip with a narrowly configured trust proxy setting. Otherwise use socket.remoteAddress. Add normalization for IPv4-mapped IPv6 addresses while touching this path.

---

#### #12. Implicit boolean conversion lets string false satisfy true-only validators

- **ID:** `fnd_sig-feat-library-b590a9efe7-d221_36bd7e7e5b`
- **Feature:** `feat_library_b590a9efe7`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/common/pipes/validation.pipe.ts:42-43 (`validationPipeOptions`)`
- `packages/api/src/common/pipes/validation.pipe.spec.ts:39-44 (`TermsAcceptedDto`)`

**Giải thích:**

> With class-transformer implicit conversion enabled globally, boolean DTO properties are converted before class-validator runs. Non-empty strings such as "false" and "0" are converted to boolean true, so a payload that explicitly says the consent checkbox is false can satisfy @Equals(true). The included regression test establishes that false consent must be rejected with ERR-REG-06, but it only covers boolean false, not string false.

**Cách tái hiện:**

> Call `pipe.transform({ dongYDieuKhoan: 'false' }, { type: 'body', metatype: TermsAcceptedDto, data: '' })`. The string is coerced to true before @Equals(true), so validation passes instead of returning ERR-REG-06.

**Khuyến nghị fix:**

> Do not use global implicit conversion for boolean body fields. Prefer disabling `enableImplicitConversion` and adding explicit DTO/query transforms where coercion is intended, or add a pre-validation guard that rejects string values for boolean-typed body properties before class-transformer can coerce them.

---

#### #13. JSONB file download endpoint authorizes only by file id, not by BieuMau attachment

- **ID:** `fnd_sig-feat-library-c4299c692e-10c5_9cb127d650`
- **Feature:** `feat_library_c4299c692e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/bieu-mau/bieu-mau.controller.ts:145-148 (`BieuMauController.downloadJsonbFile`)`
- `packages/api/src/modules/bieu-mau/bieu-mau.service.ts:657-676 (`BieuMauService.downloadJsonbFile`)`

**Giải thích:**

> The route accepts only a global fileId and skips tenant-scoped entity checks. The service then signs any RLS-visible FileDinhKem row by id without proving that the fileId is present in an accessible BieuMau. A user with Read on BieuMau who learns a same-tenant file UUID from another module can obtain a presigned URL even when that file is not an anh_dai_dien or file_dinh_kem_cong_khai of any BieuMau they are reading.

**Cách tái hiện:**

> Call GET /bieu-maus/files/{fileId}/download with the UUID of any same-tenant FileDinhKem row that is not referenced by a BieuMau JSONB publication snapshot; the service returns a presigned URL.

**Khuyến nghị fix:**

> Require a parent bieuMauId in the URL, load that BieuMau through the normal RLS path, and verify fileId appears in anhDaiDien or fileDinhKemCongKhai before signing. If the route must remain fileId-only, query for an accessible BieuMau containing that fileId before calling presignedGetObject.

---

#### #14. New tenant bridge enables RLS without forcing it for table owners

- **ID:** `fnd_sig-feat-library-d48d1976c5-a47b_06561e5d19`
- **Feature:** `feat_library_d48d1976c5`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050900043-CreateDoanhNghiepLinhVucBridge.ts:31 (`CreateDoanhNghiepLinhVucBridge2026050900043.up`)`
- `packages/api/src/database/migrations/2026050900043-CreateDoanhNghiepLinhVucBridge.ts:63-78 (`CreateDoanhNghiepLinhVucBridge2026050900043.up`)`

**Giải thích:**

> doanh_nghiep_linh_vuc is tenant-scoped by don_vi_id and has tenant policies, but the migration only enables RLS. PostgreSQL table owners bypass RLS unless FORCE ROW LEVEL SECURITY is set, so any runtime role that owns this migration-created table can bypass rls.check_don_vi_scope and read or write cross-tenant bridge rows.

**Khuyến nghị fix:**

> Add ALTER TABLE doanh_nghiep_linh_vuc FORCE ROW LEVEL SECURITY after enabling RLS, and cover the catalog flags in a migration test.

---

#### #15. Pending virus-scan rows are marked clean without being scanned

- **ID:** `fnd_sig-feat-library-60969dbb56-b3ed_820eae3312`
- **Feature:** `feat_library_60969dbb56`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050900011-DecommissionClamavScanQueue.ts:6-14`
- `packages/api/src/database/migrations/2026050900011-DecommissionClamavScanQueue.ts:27-33 (`DecommissionClamavScanQueue2026050900011.up`)`

**Giải thích:**

> Rows in CHO_QUET are precisely files that had not reached the clean state. The migration's new synchronous sniff only applies to future uploads, but the backfill changes all existing pending rows to SACH without reading or validating the stored object. That converts previously blocked files into downloadable clean files and can expose content that the old gate was intentionally withholding.

**Khuyến nghị fix:**

> Do not bulk-promote CHO_QUET to SACH. Keep those rows blocked, move them to an explicit quarantine/manual-review state, or run an out-of-band scan/sniff job that records which files were actually validated before updating them.

---

#### #16. Phan-cong list endpoint bypasses parent tenant authorization

- **ID:** `fnd_sig-feat-library-237acd59eb-ead4_1d7c3f2611`
- **Feature:** `feat_library_237acd59eb`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/danh-gia/phan-cong-danh-gia.controller.ts:31-35 (`PhanCongDanhGiaController.list`)`
- `packages/api/src/modules/danh-gia/phan-cong-danh-gia.service.ts:50-56 (`PhanCongDanhGiaService.listByKeHoach`)`
- `packages/api/src/modules/danh-gia/phan-cong-danh-gia.service.ts:68-76 (`PhanCongDanhGiaService.listByKeHoach`)`

**Giải thích:**

> The controller explicitly skips tenant scoping and the service never verifies that the parent ke_hoach_danh_gia is visible to the caller before reading phan_cong_danh_gia rows and hydrating evaluator names/emails. Any authenticated user with generic Read KeHoachDanhGia ability who knows or guesses another plan UUID can retrieve that plan's evaluator assignments.

**Khuyến nghị fix:**

> For listByKeHoach, first load the parent plan through the tenant-scoped repository or put @TenantScoped on the route, then query assignments only after the parent passes scope checks. Keep the assignment query on the RLS-pinned manager or join to the scoped parent.

---

#### #17. PheDuyetChiTra RLS trusts child don_vi_id without tying it to the parent dossier

- **ID:** `fnd_sig-feat-library-977556f978-32df_f6f6e5a2fc`
- **Feature:** `feat_library_977556f978`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050900035-CreatePheDuyetChiTra.ts:25-30 (`CreatePheDuyetChiTra2026050900035.up`)`
- `packages/api/src/database/migrations/2026050900035-CreatePheDuyetChiTra.ts:53-57 (`CreatePheDuyetChiTra2026050900035.up`)`
- `packages/api/src/database/migrations/2026050900035-CreatePheDuyetChiTra.ts:63-77 (`CreatePheDuyetChiTra2026050900035.up`)`

**Giải thích:**

> The new history table stores both ho_so_chi_tra_id and don_vi_id, but the foreign keys are independent and the RLS policy authorizes writes only from phe_duyet_chi_tra.don_vi_id. There is no constraint or policy proving that the referenced ho_so_chi_tra row belongs to the same don_vi_id. An app-role write can therefore satisfy RLS with its own don_vi_id while attaching approval history to another unit's dossier ID, breaking the tenant boundary the migration comment says it is preserving.

**Cách tái hiện:**

> Insert into phe_duyet_chi_tra with don_vi_id set to the current tenant and ho_so_chi_tra_id set to a dossier from a different tenant; the shown constraints do not reject that mismatch.

**Khuyến nghị fix:**

> Add a database-level tenant coupling: either a composite FK from (ho_so_chi_tra_id, don_vi_id) to a unique (id, don_vi_id) on ho_so_chi_tra, or a CHECK/trigger plus RLS policy that validates the parent row's don_vi_id matches the child row.

---

#### #18. Profile updates can move accounts into higher-level units without the cap guard

- **ID:** `fnd_sig-feat-library-fb2181fec9-28d4_a5afb548b7`
- **Feature:** `feat_library_fb2181fec9`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/tai-khoan/tai-khoan.controller.ts:73-83 (`TaiKhoanController.updateProfile`)`
- `packages/api/src/modules/tai-khoan/tai-khoan.service.ts:414-419 (`TaiKhoanService.updateProfile`)`
- `packages/api/src/modules/tai-khoan/tai-khoan.service.ts:855-891 (`TaiKhoanService.assertNoRoleEscalation`)`
- `packages/api/src/modules/tai-khoan/tai-khoan.service.ts:432-437 (`TaiKhoanService.updateProfile`)`

**Giải thích:**

> The update profile path accepts donViId and writes it directly after only an Action.Update policy check. The service already contains a cap-level escalation guard for account creation and role updates, but this profile update path bypasses it. Because donViId is later embedded into the target user's JWT/RLS scope, a lower-cap admin with update_tai_khoan can move an account into a higher-level unit and grant that higher scope on the next login.

**Cách tái hiện:**

> Call PUT /tai-khoan/:id as a non-QTHT DP/BN admin with update permission and a body containing version plus a TW/BN donViId; the service assigns the new donViId without checking the caller cap.

**Khuyến nghị fix:**

> When dto.donViId is present and changed, reuse assertNoRoleEscalation(currentUser, dto.donViId, activeRolesOrEmpty) or an equivalent unit-cap check before mutating the entity. Consider requiring Manage permission and forbidding self unit reassignment.

---

#### #19. Question-bank export can bypass tenant filtering

- **ID:** `fnd_sig-feat-library-22ade395f2-3c2b_63021bb06c`
- **Feature:** `feat_library_22ade395f2`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/dao-tao/khoa-hoc.service.ts:47-52 (`KhoaHocService.findAll`)`
- `packages/api/src/modules/dao-tao/ngan-hang-cau-hoi-export.service.ts:28-37 (`NganHangCauHoiExportService.export`)`
- `packages/api/src/modules/dao-tao/ngan-hang-cau-hoi-export.service.ts:65-66 (`NganHangCauHoiExportService.buildQuery`)`
- `packages/api/src/modules/dao-tao/ngan-hang-cau-hoi.controller.ts:85-93 (`NganHangCauHoiController.exportExcel`)`

**Giải thích:**

> The export path uses the exact repository QueryBuilder pattern that this module already documents as leaking cross-tenant rows when app-layer RLS filters are required. The export route is a collection action with no entity id to scope, and buildQuery has no currentUser/tenant predicate, so synchronous exports and especially queued exports can include question-bank rows outside the caller's tenant scope.

**Khuyến nghị fix:**

> Build exports with tenantNhchRepo.getRlsSafeQueryBuilder('nhch') for request-scoped exports, and make the background job reconstruct an explicit tenant/RLS context or apply a don_vi_id/allowedDonViIds predicate before reading rows.

---

#### #20. Read-only detail route exposes draft editing controls

- **ID:** `fnd_sig-feat-route-1efd5fab0f-975503_48421567ef`
- **Feature:** `feat_route_1efd5fab0f`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/ct-htpldn/index.tsx:79-86 (`CtHtpldnPage`)`
- `packages/web/src/pages/ct-htpldn/detail/index.tsx:142-143 (`ChuongTrinhHtplDetailPage`)`
- `packages/web/src/pages/ct-htpldn/detail/index.tsx:215-233 (`ChuongTrinhHtplDetailPage`)`
- `packages/web/src/pages/ct-htpldn/detail/index.tsx:278-287 (`ChuongTrinhHtplDetailPage`)`
- `packages/web/src/pages/ct-htpldn/detail/index.test.tsx:115-127 (`renderPage`)`
- `_…1 vị trí khác_`

**Giải thích:**

> The '/:id' route only requires read permission, but it renders the same detail component whose editable state is based solely on record status. For a DU_THAO record, a user with read but not update permission can see editable inputs and the Lưu button and can trigger the update mutation from the read-only route. The separate ':id/chinh-sua' update-guarded route does not protect this path because the component does not also require update permission before enabling edits.

**Cách tái hiện:**

> Render CtHtpldnPage at /ct-htpldn/test-id with an AbilityContext that grants read ChuongTrinhHtpl but not update, and mock the detail hook to return a DU_THAO record. The detail form still shows editable fields and the Lưu button, and submitting calls useUpdateChuongTrinhHtpl.

**Khuyến nghị fix:**

> Make editability require update permission as well as draft status, for example by checking ability.can(CaslActions.Update, CaslSubjects.ChuongTrinhHtpl) inside ChuongTrinhHtplDetailPage before enabling the form and rendering Lưu/Quay lại. If '/:id/chinh-sua' is meant to be the only edit surface, also derive edit mode from that route and keep '/:id' read-only.

---

#### #21. Read-only users can reach an editable instructor form

- **ID:** `fnd_sig-feat-library-80a98708fd-8d12_24b1afb045`
- **Feature:** `feat_library_80a98708fd`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/dao-tao/giang-vien/columns.tsx:34-35 (`getGiangVienColumns`)`
- `packages/web/src/pages/dao-tao/giang-vien/list/index.tsx:49-55 (`GiangVienListPage`)`
- `packages/web/src/pages/dao-tao/giang-vien/detail/index.tsx:65-72 (`GiangVienDetailPage`)`
- `packages/web/src/pages/dao-tao/giang-vien/detail/index.tsx:50-56 (`handleSubmit`)`
- `packages/web/src/pages/dao-tao/giang-vien/components/GiangVienForm.tsx:210-216 (`GiangVienForm`)`

**Giải thích:**

> The list only permission-gates the explicit edit icon, but the unguarded name link takes any reader to the same route as edit. The detail page then renders GiangVienForm in edit mode and wires submit to updateMutation without checking CaslActions.Update. A user with read but not update permission can therefore edit fields and trigger a PATCH attempt from the UI, bypassing the list action guard.

**Cách tái hiện:**

> Give a user only read permission for GiangVien, open the instructor list, click an instructor name, change a field on the detail page, and press Lưu. The UI attempts updateMutation even though the edit action was hidden.

**Khuyến nghị fix:**

> Separate read-only detail from edit, or pass an editable flag based on ability.can(Update, GiangVien). Hide or disable mutable fields and the Lưu button for read-only users, and also guard handleSubmit so an update cannot be fired without update permission.

---

#### #22. Registration submits a hard-coded CAPTCHA token

- **ID:** `fnd_sig-feat-ui-flow-75b08502ac-458e_ef11576262`
- **Feature:** `feat_ui-flow_75b08502ac`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/services/auth/register.service.ts:8-14 (`RegisterDoanhNghiepDto`)`
- `packages/web/src/pages/auth/register/doanh-nghiep.tsx:173-180 (`handleFinish`)`
- `packages/web/src/pages/auth/register/doanh-nghiep.test.tsx:28-30`

**Giải thích:**

> The public registration DTO requires a CAPTCHA token, but the page never collects one and always serializes the literal value 'mock-captcha' into the network request. In production this either makes valid registrations fail CAPTCHA verification or trains the server to accept a fake static token, defeating the anti-automation boundary for account creation.

**Cách tái hiện:**

> Fill the doanh-nghiep registration form with otherwise valid data and submit; the POST body constructed by handleFinish always contains captchaToken: 'mock-captcha' regardless of user interaction.

**Khuyến nghị fix:**

> Integrate the real CAPTCHA widget/provider into this page, store the issued token in form state, require it before submit, send that token in RegisterDoanhNghiepDto, and reset/refresh it after failed submissions.

---

#### #23. Report cache keys ignore the RLS scope that actually shapes query results

- **ID:** `fnd_sig-feat-library-2134992159-8370_95b42a8cd5`
- **Feature:** `feat_library_2134992159`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/bao-cao/services/report-query.factory.ts:53-75 (`ReportQueryFactory.create`)`
- `packages/api/src/modules/bao-cao/services/__tests__/report-query.factory.spec.ts:62-79 (`ReportQueryFactory BN scope test`)`
- `packages/api/src/modules/bao-cao/services/bc-vu-viec-tiep-nhan.service.ts:54-57 (`BcVuViecTiepNhanService.query`)`
- `packages/api/src/modules/bao-cao/services/bc-so-luong-cg-tvv.service.ts:29-31 (`BcSoLuongCgTvvService.query`)`

**Giải thích:**

> The database result for non-TW callers depends on the per-request RLS context, specifically allowedDonViIds. The report cache keys only include currentUser.donViId plus filter values. Two users from the same unit but with different PHAN_QUYEN_DU_LIEU grants can therefore share a key. If the broader-scope user fills the cache first, the narrower-scope user returns cached aggregate data before any scoped SQL runs.

**Cách tái hiện:**

> Use two BN users with the same donViId but different allowedDonViIds. Query the same report and date range as the user with extra grants, then query as the narrower user before TTL expiry. The second request can return the first user's broader cached result.

**Khuyến nghị fix:**

> Centralize report cache-key generation and include a deterministic scope component, such as capDonVi plus a sorted allowedDonViIds hash from RlsContext. Alternatively, disable shared caching for non-TW scoped reports.

---

#### #24. Report cache keys ignore the effective RLS scope

- **ID:** `fnd_sig-feat-library-5ad39280f7-c610_a4078ab914`
- **Feature:** `feat_library_5ad39280f7`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/bao-cao/services/bc-hoi-dap.service.ts:68-70 (`BcHoiDapService.query`)`
- `packages/api/src/modules/bao-cao/services/bc-chi-phi-theo-don-vi.service.ts:32-34 (`BcChiPhiTheoDonViService.query`)`
- `packages/api/src/modules/bao-cao/services/bc-ct-theo-thoi-gian.service.ts:35-39 (`BcCtTheoThoiGianService.query`)`
- `packages/api/src/modules/bao-cao/services/__tests__/report-query.factory.spec.ts:62-79 (`ReportQueryFactory spec`)`

**Giải thích:**

> The database query scope depends on CLS RLS context, especially allowedDonViIds, but the shared cache is keyed mostly by currentUser.donViId and filter values. On a cache hit, services return before ReportQueryFactory can apply the allowedDonViIds fence. Two users in the same donViId with different delegated data scopes can therefore share cached aggregate results, letting the narrower user receive data computed under the broader user's scope.

**Khuyến nghị fix:**

> Include the effective access scope in all report cache keys, for example capDonVi plus a stable hash of allowedDonViIds or userId when scope can differ per user. Alternatively disable shared caching for scoped report data unless the key is built from the same scope inputs used by ReportQueryFactory.

---

#### #25. Same-millisecond requests collapse into one rate-limit entry

- **ID:** `fnd_sig-feat-library-b8185085de-97e2_aa6a1105d6`
- **Feature:** `feat_library_b8185085de`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/api-public/interceptors/public-rate-limit.interceptor.ts:25 (`SLIDING_WINDOW_SCRIPT`)`
- `packages/api/src/modules/api-public/interceptors/public-rate-limit.interceptor.ts:44-54 (`PublicRateLimitInterceptor.intercept`)`
- `packages/api/src/modules/api-public/interceptors/public-rate-limit.interceptor.spec.ts:25-31 (`PublicRateLimitInterceptor spec setup`)`

**Giải thích:**

> The Lua script uses the millisecond timestamp as both the sorted-set score and member. Redis sorted-set members are unique, so concurrent requests for the same consumer that enter the interceptor during the same millisecond update the same member instead of adding distinct events. Under load, many requests can be counted as one and bypass the configured per-minute public API limit.

**Khuyến nghị fix:**

> Store a unique member for each request while keeping the timestamp as the score, for example pass a UUID or monotonic sequence as an additional ARGV value, or generate uniqueness inside Redis. Keep using the timestamp score for pruning and retry calculation.

---

#### #26. Single-create path bypasses the same-cap policy-set rule

- **ID:** `fnd_sig-feat-library-a07573a805-10cc_b80fde22da`
- **Feature:** `feat_library_a07573a805`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/phan-quyen-du-lieu/phan-quyen-du-lieu.service.ts:67-83 (`PhanQuyenDuLieuService.create`)`
- `packages/api/src/modules/phan-quyen-du-lieu/phan-quyen-du-lieu.service.ts:127-142 (`PhanQuyenDuLieuService.batchUpdate`)`

**Giải thích:**

> The batch path explicitly enforces that one role's policy set cannot contain two distinct units with the same cap, but the create path only validates the new target against the role hierarchy and then saves it. A caller can create one valid descendant policy, then create another valid descendant policy at the same cap for the same role; each request passes create validation, while the final policy set is a state batchUpdate would reject.

**Cách tái hiện:**

> For a BN role with two DP descendants A and B, call POST /phan-quyen-du-lieu for A, then POST /phan-quyen-du-lieu for B using the same vaiTroId. Both rows can be saved even though batchUpdate would throw NGANG_CAP for the same set.

**Khuyến nghị fix:**

> Apply the same cap-conflict check in create against existing policies plus the candidate, preferably under the same per-role lock used for mutations. Alternatively remove/deprecate single-create and force all changes through a serialized batch replacement path.

---

#### #27. State transitions run on a fresh connection without RLS context

- **ID:** `fnd_sig-feat-library-132c0ddff1-08d7_07dcf5948f`
- **Feature:** `feat_library_132c0ddff1`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/common/services/state-machine.service.ts:19-21 (`StateMachineService.transition`)`
- `packages/api/src/common/services/state-machine.service.ts:31-40 (`StateMachineService.transition`)`
- `packages/api/src/common/services/state-machine.service.ts:37 (`StateMachineService.transition`)`

**Giải thích:**

> The service opens a new TypeORM QueryRunner and reads by id only, but it has no RLS context parameter, no CLS lookup, and no GUC setup before the locked read/save. A fresh pool connection is not automatically scoped to the caller's request session, so tenant-scoped workflows either fail closed as not found under DB RLS or, where app-layer tenant filtering is relied on, can mutate a cross-tenant row by id. The inline comment's assumption that createQueryRunner is scoped to the caller is not enforced by this API.

**Cách tái hiện:**

> Call transition on a tenant-scoped entity during an authenticated non-TW request whose request-scoped QueryRunner has RLS GUCs. This service creates a separate QueryRunner, then SELECTs by id without applying those GUCs or a tenant predicate.

**Khuyến nghị fix:**

> Inject/read the current RLS context and apply it to the new QueryRunner after startTransaction, or require callers to pass a transaction manager/query runner that is already RLS-pinned. Also add an explicit tenant/access predicate or pre-authorized scoped lookup before saving.

---

#### #28. System roles can still be edited or disabled through the API

- **ID:** `fnd_sig-feat-library-a10207fa13-db3b_6ecc4cbc9c`
- **Feature:** `feat_library_a10207fa13`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/vai-tro/vai-tro.service.ts:133-153 (`VaiTroService.update`)`
- `packages/api/src/modules/vai-tro/vai-tro.service.ts:158-175 (`VaiTroService.toggleStatus`)`
- `packages/api/src/modules/vai-tro/vai-tro.service.ts:222-228 (`VaiTroService.remove`)`

**Giải thích:**

> The service blocks deletion when entity.isSystem is true, but update() and toggleStatus() load the same entity and save changes without the same guard. Any caller with Action.Update on VaiTro can directly PATCH a seeded system role, including disabling QTHT/DN-style roles or changing their cap/name/status, even though the backend already treats system roles as protected for delete.

**Cách tái hiện:**

> Authenticate as a user with update_vai_tro, then call PATCH /vai-tro/{systemRoleId}/toggle-status or PATCH /vai-tro/{systemRoleId} with a valid version. The service will save the mutation unless another unrelated error occurs.

**Khuyến nghị fix:**

> Add a shared assertMutableRole guard and call it from update() and toggleStatus() before saving. Return a domain 409/403 code for system-role mutation attempts, and keep delete using the same invariant.

---

#### #29. TCTV list and export bypass app-layer tenant filters

- **ID:** `fnd_sig-feat-library-9bb5d898e6-75e2_2390491110`
- **Feature:** `feat_library_9bb5d898e6`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/chuyen-gia-tvv/services/to-chuc-tu-van.service.ts:189-206 (`ToChucTuVanService.findAll`)`
- `packages/api/src/modules/chuyen-gia-tvv/services/to-chuc-tu-van-export.service.ts:77-83 (`ToChucTuVanExportService.buildQuery`)`
- `packages/api/src/modules/chuyen-gia-tvv/services/tu-van-vien-export.service.ts:73-77 (`TuVanVienExportService.buildQuery`)`

**Giải thích:**

> The feature already documents that the safe list/export pattern is getRlsSafeQueryBuilder because the plain repository query builder leaked cross-don_vi rows. TCTV list and TCTV export still use the plain getRlsSafeRepo().createQueryBuilder path, so DP/BN users can receive or export TCTV rows outside their allowed don_vi scope unless a caller-supplied donViId happens to narrow the query. The export includes representative/contact/address fields, so this crosses an authorization boundary.

**Cách tái hiện:**

> Create TCTV rows in two don_vi scopes, authenticate as a DP user scoped to one don_vi, then call the TCTV list/export without donViId. The service builds no mandatory don_vi predicate in these methods and can return rows from the other scope.

**Khuyến nghị fix:**

> Switch both TCTV builders to this.tenantRepo.getRlsSafeQueryBuilder('tctv') and add joins/filters on that builder. Keep any explicit donViId filter as an additional narrowing condition, not the only tenant predicate.

---

#### #30. TVV file delete endpoint bypasses the CB_NV-only file policy

- **ID:** `fnd_sig-feat-library-4315226f8e-6a48_cda4c1d593`
- **Feature:** `feat_library_4315226f8e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/chuyen-gia-tvv/tu-van-vien.controller.ts:247-257 (`TuVanVienController.removeFile`)`
- `packages/api/src/modules/chuyen-gia-tvv/ho-so-tvv-file-policy.provider.ts:50-53 (`HoSoTvvFilePolicyProvider.canDelete`)`
- `packages/api/src/modules/chuyen-gia-tvv/ho-so-tvv-file-policy.provider.spec.ts:173-184 (`HoSoTvvFilePolicyProvider canDelete tests`)`

**Giải thích:**

> The route deletes TVV profile files after only a parent TuVanVien update permission check. The included file-policy provider and its tests define a narrower delete contract: only CB_NV_ in the same đơn vị may delete, while NHT/TVV must be denied. Because the sub-endpoint calls FileService.removeForEntity directly, it never consults HoSoTvvFilePolicyProvider.canDelete, so any role granted Action.Update on the parent can erase supporting hồ sơ files contrary to the permission matrix.

**Cách tái hiện:**

> As a non-CB_NV caller that has Action.Update on an accessible TuVanVien, call DELETE /tu-van-viens/:id/files/:fileId for a file attached to the resolved TVV_HO_SO row. The controller resolves hoSoId and deletes via removeForEntity without applying canDelete.

**Khuyến nghị fix:**

> Before removeForEntity, enforce the same HoSoTvvFilePolicyProvider.canDelete decision for the resolved hồ sơ id, or inline the CB_NV_ same-donVi rule in the service layer. Prefer reusing the registry/provider so the generic and sub-endpoint paths cannot drift.

---

#### #31. Tenant-scoped read and export paths bypass service-layer RLS filtering

- **ID:** `fnd_sig-feat-library-017b22193d-4d4b_be7e37c9b1`
- **Feature:** `feat_library_017b22193d`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/dao-tao/giang-vien.service.ts:43-48 (`GiangVienService.findAll`)`
- `packages/api/src/modules/dao-tao/de-xuat-dao-tao.service.ts:77-85 (`DeXuatDaoTaoService.findAll`)`
- `packages/api/src/modules/dao-tao/diem-danh.service.ts:83-94 (`DiemDanhService.findByDate`)`
- `packages/api/src/modules/dao-tao/diem-danh.service.ts:395-415 (`DiemDanhService.exportToExcel`)`
- `packages/api/src/modules/dao-tao/ket-qua-dao-tao.controller.ts:26-30 (`KetQuaDaoTaoController.list`)`
- `_…2 vị trí khác_`

**Giải thích:**

> The module itself documents that createQueryBuilder from getRlsSafeRepo only pins a connection and does not apply the app-layer tenant predicate. Several list/export paths still use that pattern or raw repositories, and the child ket-qua routes explicitly skip the route-level tenant scope while not verifying the parent KhoaHoc before reading rows. In environments where PostgreSQL RLS is not enforced or the app role bypasses it, a user with the broad Read permission can enumerate or export another unit's proposals, attendance, or results by supplying filters or a known khoaHocId.

**Khuyến nghị fix:**

> Switch collection queries to the relevant TenantAwareRepository.getRlsSafeQueryBuilder, and for child resources load/authorize the parent KhoaHoc through the tenant-aware repository before any direct child query/export. Add permission-matrix coverage for cross-don-vi list and export attempts.

---

#### #32. TuLieuPhapLyVv create accepts a parent consultation id without tenant validation

- **ID:** `fnd_sig-feat-library-205015f24e-c301_4dac26c6d1`
- **Feature:** `feat_library_205015f24e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/tu-van/tu-lieu-phap-ly-vv.service.ts:58-68 (`TuLieuPhapLyVvService.validateNoiDungTv`)`
- `packages/api/src/modules/tu-van/tu-lieu-phap-ly-vv.service.ts:112-130 (`TuLieuPhapLyVvService.create`)`
- `packages/api/src/modules/tu-van/tu-lieu-phap-ly-vv.controller.ts:48-56 (`TuLieuPhapLyVvController.create`)`

**Giải thích:**

> validateNoiDungTv only checks that the supplied noiDungTvId exists; it does not load the parent through TENANT_REPO_NoiDungTuVanCs, apply RLS filters, or assert that the caller can access the parent's donVi. create then persists the new legal-material row with the attacker's donViId while linking it to the arbitrary parent id. This can create cross-tenant associations and later expose parent metadata through findOne/list joins.

**Cách tái hiện:**

> With Create TuLieuPhapLyVv permission in don_vi A, submit POST /tu-lieu-phap-ly-vvs using a noiDungTvId owned by don_vi B. The service validates existence only and creates a row owned by A but linked to B's consultation.

**Khuyến nghị fix:**

> Validate the parent through the tenant-aware NoiDungTuVanCs repository using the request RLS context, reject inaccessible parents, and set or verify the new row's donViId consistently with the validated parent ownership rules.

---

#### #33. `getRlsSafeRepo` exposes unfiltered repository operations while app-layer RLS is still required

- **ID:** `fnd_sig-feat-library-d01c3855e7-0bca_930cd91912`
- **Feature:** `feat_library_d01c3855e7`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/common/repositories/tenant-aware.repository.ts:116-124 (`TenantAwareRepository.getRlsSafeQueryBuilder`)`
- `packages/api/src/common/repositories/tenant-aware.repository.ts:139-150 (`TenantAwareRepository.getRlsSafeRepo`)`
- `packages/api/src/common/repositories/tenant-aware.repository.spec.ts:391-410 (`TenantAwareRepository.getRlsSafeRepo tests`)`

**Giải thích:**

> The query-builder path explicitly applies `applyRlsFilters` because the file documents that GUCs alone do not filter rows before database RLS is deployed. `getRlsSafeRepo` does not apply an equivalent tenant predicate or post-fetch assertion; it simply returns the QueryRunner repository or the raw pool repository. Any caller using repository methods such as `find`, `findOne`, `update`, or `delete` through this helper can run without the app-layer tenant filter that the same file says is required, which can expose or mutate cross-tenant rows until database RLS is enforced. The fallback path is especially risky because it returns the raw pool repository even when the missing QueryRunner is a misconfiguration rather than a system/test context.

**Cách tái hiện:**

> Create a BN/DP request context before database RLS is active, call `getRlsSafeRepo().find()` or `getRlsSafeRepo().update()` on a tenant table, and observe that no `don_vi_id` predicate or `assertCanAccessDonVi` check is applied by this wrapper.

**Khuyến nghị fix:**

> Do not expose raw repository operations as RLS-safe for user-scoped code. Either wrap the repository methods that are allowed with tenant predicates/assertions, make `getRlsSafeRepo` fail closed when a user RLS context exists but no QueryRunner is present, or rename/split the API so only system jobs can obtain an unscoped repository explicitly.

---

#### #34. fileDinhKemIds can re-parent existing attachments from other records

- **ID:** `fnd_sig-feat-library-12d84f0027-3dbb_99f4d0cc3e`
- **Feature:** `feat_library_12d84f0027`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:548-554 (`HoiDapService.update`)`
- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:684-693 (`HoiDapService.create`)`

**Giải thích:**

> Both create() and update() bulk-update every supplied file id to entityType='HOI_DAP' and entityId=<current id>. There is no predicate requiring the files to be orphaned, already owned by the same aggregate, or uploaded by this flow. A user with update access to one HoiDap and knowledge of another same-tenant file UUID can move that attachment away from its original record.

**Khuyến nghị fix:**

> Route attachment linking through FileService or add ownership predicates such as entity_type IS NULL/entity_id IS NULL or same aggregate ownership, then verify affected row count equals the requested ids before committing.

---

#### #35. goi-y endpoint bypasses TuVanNhanh tenant scoping and can mutate another unit's session

- **ID:** `fnd_sig-feat-library-205015f24e-4b78_941d57fc67`
- **Feature:** `feat_library_205015f24e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/tu-van/tu-van-nhanh.controller.ts:47-55 (`TuVanNhanhController.getGoiY`)`
- `packages/api/src/modules/tu-van/tu-van-nhanh.service.ts:404-412 (`TuVanNhanhService.getGoiY`)`
- `packages/api/src/modules/tu-van/tu-van-nhanh.service.ts:421-447 (`TuVanNhanhService.getGoiY`)`

**Giải thích:**

> The route intentionally skips tenant scope, but unlike findOne/traCuuKho it does not pass CurrentUser into the service and the service never applies applyRlsFilters or assertSameDonVi before reading, returning, and saving the TuVanNhanh row. A user with the coarse Read permission can call GET /tu-van-nhanhs/{otherDonViId}/goi-y and either read cached suggestions or overwrite goiYTraLoi/trangThai on a session outside their unit.

**Cách tái hiện:**

> Use an account from don_vi A with Action.Read on TuVanNhanh, call GET /tu-van-nhanhs/{id owned by don_vi B}/goi-y?tuKhoa=test. The service loads by id, updates goiYTraLoi, saves, and returns suggestions without any per-row tenant assertion.

**Khuyến nghị fix:**

> Pass CurrentUser to getGoiY, load the session through the same scoped query pattern used by findOne/traCuuKho, and call assertSameDonVi before returning cached suggestions or saving recalculated suggestions.

---

### 3.2 Mất/sai dữ liệu (Data Loss) — 14 findings

#### #36. Completing one aggregate report can mark unrelated report periods as aggregated

- **ID:** `fnd_sig-feat-library-b89215dbad-5e0a_923d662cd9`
- **Feature:** `feat_library_b89215dbad`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/ct-htpldn/bao-cao-ct-htpl/bao-cao-ct-htpl.entity.ts:16-21 (`BaoCaoCtHtplEntity.dotBaoCaoId`)`
- `packages/api/src/modules/ct-htpldn/bao-cao-ct-htpl/bao-cao-ct-htpl.service.ts:182-200 (`BaoCaoCtHtplService.hoanThanhTongHop`)`

**Giải thích:**

> The report entity is tied to a specific dot_bao_cao_id, but hoanThanhTongHop updates every dot_bao_cao row for the same chuong_trinh_id that is currently DA_GUI_TW. If a program has multiple reporting periods waiting at TW and only one aggregate report is completed, this broad update advances sibling periods to DA_TONG_HOP without completing their corresponding report flow.

**Cách tái hiện:**

> Create two DA_GUI_TW dot_bao_cao rows under the same ct_htpl_id, each with its own report; complete the TONG_HOP_TW report for only one of them. The update predicate matches both rows by chuong_trinh_id and advances both to DA_TONG_HOP.

**Khuyến nghị fix:**

> Restrict the cascade to the dot(s) that actually belong to the completed aggregate report. At minimum use baoCao.dotBaoCaoId; if aggregate reports can cover multiple source reports, persist and use that membership instead of updating all rows for the program.

---

#### #37. Completing scoring can lock in stale scores while discarding unsaved edits

- **ID:** `fnd_sig-feat-library-51d79f2ea7-24fb_cf6d5a655c`
- **Feature:** `feat_library_51d79f2ea7`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/danh-gia/ke-hoach/components/ChamDiemTab.tsx:61-80 (`ChamDiemTab editState handlers`)`
- `packages/web/src/pages/danh-gia/ke-hoach/components/ChamDiemTab.tsx:126-143 (`ChamDiemTab.handleComplete`)`
- `packages/web/src/pages/danh-gia/ke-hoach/components/ChamDiemTab.tsx:211-219 (`ChamDiemTab action bar props`)`
- `packages/web/src/pages/danh-gia/ke-hoach/components/ChamDiemActionBar.tsx:46-57 (`ChamDiemActionBar complete control`)`

**Giải thích:**

> Score and note edits live only in editState until the user clicks Lưu kết quả. The complete action does not inspect editState, does not save pending edits, and the action bar only disables completion when server rows are CHUA_DANH_GIA. If all rows are already DA_DANH_GIA, a user can modify a score or note and then complete scoring; the mutation finalizes the old server values, and the confirmation text says scores cannot be edited afterward.

**Cách tái hiện:**

> Start with all ketQuas returned as DA_DANH_GIA and keHoachLinks.complete present. Change a score in ScoringTable, do not click Lưu kết quả, then click Hoàn tất chấm điểm. The complete mutation runs with only version and no score payload, so the changed local value is not persisted before the plan is locked.

**Khuyến nghị fix:**

> Track dirty scoring state in ChamDiemTab and either disable Hoàn tất chấm điểm while editState is non-empty with a tooltip requiring save first, or make handleComplete await a successful save of buildSavePayload before calling completeScoringMutation.

---

#### #38. Delete can race with new vụ việc links

- **ID:** `fnd_sig-feat-library-f72aa3f50c-9f5e_12177aca67`
- **Feature:** `feat_library_f72aa3f50c`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.service.ts:584-588 (`HopDongTuVanService.remove`)`
- `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.service.ts:595-608 (`HopDongTuVanService.remove`)`

**Giải thích:**

> The 'cannot delete when linked' precondition is checked before the transaction and before the parent row is locked. A concurrent update can add a hop_dong_vu_viec link after linkedCount returns 0 but before remove locks and deletes the parent. The delete then cascades the newly-created link and removes a contract that had become linked, violating the guard and losing the association.

**Cách tái hiện:**

> Start DELETE /hop-dong-tu-vans/:id on a contract with no links, then concurrently add vuViecIds to the same contract after the count but before the delete transaction reaches remove. The delete can still commit and cascade the new join row.

**Khuyến nghị fix:**

> Move the linked-count check inside the transaction after acquiring the parent row lock, and ensure link insertion/update also locks the same parent row before changing hop_dong_vu_viec.

---

#### #39. Detail form can keep stale values after record changes

- **ID:** `fnd_sig-feat-library-71b15c1e71-ce17_5271c47d6a`
- **Feature:** `feat_library_71b15c1e71`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/ct-htpldn/detail/index.tsx:106-111 (`ChuongTrinhHtplDetailPage`)`
- `packages/web/src/pages/ct-htpldn/detail/index.tsx:168-172 (`initialValues`)`
- `packages/web/src/pages/ct-htpldn/detail/index.tsx:215-220 (`ProForm`)`
- `packages/web/src/pages/ct-htpldn/detail/index.tsx:227-233 (`ProForm.onFinish`)`

**Giải thích:**

> The component explicitly treats record id/version changes as possible while mounted, but it only clears isDirty. The form is not keyed by record id and no resetFields/setFieldsValue runs when initialValues changes, so a reused detail route or background refetch can leave old form fields displayed while updateMutation and record.version now target the new/current record. Saving then submits stale values to the current id/version, and the dirty guard may already have been cleared.

**Cách tái hiện:**

> Open editable detail record A, change route/params to editable record B without unmounting the route, then press Lưu. The form can still contain A's values while the mutation targets B.

**Khuyến nghị fix:**

> Remount or explicitly reset the ProForm when record.id changes, and do not clear isDirty on arbitrary record.version changes. Clear dirty only after the local save succeeds; for external refetches, either preserve dirty state or prompt before replacing form values.

---

#### #40. Invalid trongSo values are saved before the warning query crashes

- **ID:** `fnd_sig-feat-library-c6797f4fce-bcbf_1a5f3bfaa6`
- **Feature:** `feat_library_c6797f4fce`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/danh-muc/dto/create-danh-muc.dto.ts:49-51 (`CreateDanhMucDto.duLieuMoRong`)`
- `packages/api/src/modules/danh-muc/danh-muc.service.ts:431-435 (`DanhMucService.validateDuLieuMoRong`)`
- `packages/api/src/modules/danh-muc/danh-muc.service.ts:155-159 (`DanhMucService.createDanhMuc`)`
- `packages/api/src/modules/danh-muc/danh-muc.service.ts:584-589 (`DanhMucService.checkWeightWarning`)`

**Giải thích:**

> duLieuMoRong is only validated as an object, and the TIEU_CHI_DG_HIEU_QUA branch only range-checks with JavaScript comparisons. A string such as "abc" or "" is neither < 0 nor > 100, so it passes validation. The row is then saved before checkWeightWarning casts all active trongSo values to numeric in SQL, which will throw on non-numeric text. That leaves invalid dictionary data committed while the request fails, and future weight-warning queries can keep failing on the poisoned row.

**Cách tái hiện:**

> POST a TIEU_CHI_DG_HIEU_QUA danh mục with duLieuMoRong.trongSo set to "abc". Validation accepts it, save commits it, then the warning query attempts ::numeric and can raise a database error.

**Khuyến nghị fix:**

> Validate trongSo as a finite number before saving, reject non-numeric values with the structured DANH_MUC validation error, and wrap save plus post-save warning logic in a transaction if a later failure should abort the mutation. Apply the same validation to updates.

---

#### #41. Kế hoạch đào tạo refactor drops existing CTDT links before backfilling the new direction

- **ID:** `fnd_sig-feat-library-d48fe2270b-d50c_c8a3f3709f`
- **Feature:** `feat_library_d48fe2270b`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050601003-RefactorKeHoachDaoTaoSchema.ts:6-9 (`RefactorKeHoachDaoTaoSchema2026050601003`)`
- `packages/api/src/database/migrations/2026050601003-RefactorKeHoachDaoTaoSchema.ts:23-43 (`RefactorKeHoachDaoTaoSchema2026050601003.up`)`
- `packages/api/src/database/migrations/2026050601003-RefactorKeHoachDaoTaoSchema.ts:78-121 (`RefactorKeHoachDaoTaoSchema2026050601003.down`)`

**Giải thích:**

> The migration reverses the relationship from ke_hoach_dao_tao.ctdt_id to chuong_trinh_dao_tao.ke_hoach_id, but it drops the old ctdt_id column before copying existing mappings into the new column. Once the column is dropped, the old plan-to-program relationship is gone; down() recreates ctdt_id as an empty nullable column, so rollback cannot restore the lost links.

**Khuyến nghị fix:**

> Add chuong_trinh_dao_tao.ke_hoach_id first, backfill it from ke_hoach_dao_tao.ctdt_id, preflight any duplicate/ambiguous old mappings, and only then drop the old column. Preserve enough information for rollback or explicitly mark the migration irreversible with a safe preflight.

---

#### #42. Linh-vuc cleanup deletes whole business records, not just category links

- **ID:** `fnd_sig-feat-library-60969dbb56-a19d_a15686708f`
- **Feature:** `feat_library_60969dbb56`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050900009-AlignLinhVucPlSrs.ts:26-28`
- `packages/api/src/database/migrations/2026050900009-AlignLinhVucPlSrs.ts:56-75 (`FK_TABLES`)`
- `packages/api/src/database/migrations/2026050900009-AlignLinhVucPlSrs.ts:161-174 (`AlignLinhVucPlSrs2026050900009.up`)`

**Giải thích:**

> The approved trade-off documented in the migration is loss of a small number of NHT category picks, but the generic delete loop runs against every FK holder. Several listed tables are primary business/content tables by name, so any row classified under a removed legal field is permanently deleted, not remapped, nulled, archived, or reported for manual handling. The down migration also states FK rows cannot be restored.

**Khuyến nghị fix:**

> Split join/assignment tables from owner tables. Only hard-delete explicitly approved link rows; for business records, remap to a replacement SRS category, set the FK null if allowed, archive with an audit trail, or fail with a detailed report for manual remediation.

---

#### #43. Result submission overwrites override-protected grading with stale rules

- **ID:** `fnd_sig-feat-library-22ade395f2-d2b0_106c9e7dbb`
- **Feature:** `feat_library_22ade395f2`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/dao-tao/ket-qua-recompute.service.ts:21-30 (`KetQuaRecomputeService`)`
- `packages/api/src/modules/dao-tao/ket-qua-recompute.service.ts:48-55 (`KetQuaRecomputeService.recompute`)`
- `packages/api/src/modules/dao-tao/ket-qua-recompute.service.ts:78-98 (`KetQuaRecomputeService.recompute`)`
- `packages/api/src/modules/dao-tao/khoa-hoc-workflow.service.ts:690-725 (`KhoaHocWorkflowService.submitResult`)`

**Giải thích:**

> The dedicated recompute service sources diem_dat from DeKiemTra and honors xep_loai_override/ket_qua_override, but submitResult runs a separate raw UPDATE that hard-codes diem_kiem_tra >= 5.0 and updates ket_qua for every row in the course. Submitting results can therefore overwrite a manually overridden ket_qua or grade against the wrong pass threshold after the correct recompute flow already ran.

**Khuyến nghị fix:**

> Remove the duplicate grading SQL from submitResult and call KetQuaRecomputeService.recompute, or make the SQL use the same diem_dat lookup and skip_xep/skip_kq override semantics before moving rows to CHO_DUYET.

---

#### #44. Retention cron computes Asia/Ho_Chi_Minh schedules with UTC calendar math

- **ID:** `fnd_sig-feat-library-5f0ad78d7e-4401_7d4a7ed589`
- **Feature:** `feat_library_5f0ad78d7e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/audit-log/audit-log-retention.cron.ts:42 (`AuditLogRetentionCron.handleEnsureNextMonthPartition`)`
- `packages/api/src/modules/audit-log/audit-log-retention.cron.ts:89-91 (`AuditLogRetentionCron.runOnceEnsure`)`
- `packages/api/src/modules/audit-log/audit-log-retention.cron.ts:127-128 (`AuditLogRetentionCron.firstOfNextMonth`)`
- `packages/api/src/modules/audit-log/audit-log-retention.cron.ts:63 (`AuditLogRetentionCron.handlePurgeRetention`)`
- `packages/api/src/modules/audit-log/audit-log-retention.cron.ts:108-110 (`AuditLogRetentionCron.runOncePurge`)`

**Giải thích:**

> The cron jobs are scheduled in Asia/Ho_Chi_Minh, but the default dates are derived from the UTC month/day of new Date(). At 03:00 on 2027-12-01 in Ho Chi Minh, JavaScript sees 2027-11-30T20:00:00Z, so firstOfNextMonth returns 2027-12-01 instead of 2028-01-01. After the pre-seeded partition window ends, the next partition is created only at 03:00 on the first day of that month, leaving the first three local hours with no audit_log partition. The purge path has the same local/UTC drift and can retain eligible partitions longer than intended.

**Khuyến nghị fix:**

> Compute the default ensure and purge dates in the configured timezone, or move the default date calculation into SQL with an explicit Asia/Ho_Chi_Minh timezone. Keep the explicit Date override behavior for tests/admin triggers.

---

#### #45. Role permission selections can be saved to the wrong role after route changes

- **ID:** `fnd_sig-feat-library-90d1412283-c7df_69d807b9fa`
- **Feature:** `feat_library_90d1412283`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/quan-tri/vai-tro/quyen-han/index.tsx:38-52 (`VaiTroQuyenHanPage`)`
- `packages/web/src/pages/quan-tri/vai-tro/quyen-han/index.tsx:56-79 (`handleToggle / handleSelectAll`)`
- `packages/web/src/pages/quan-tri/vai-tro/quyen-han/index.tsx:82-88 (`handleSave`)`

**Giải thích:**

> After the first checkbox edit, checkedIds becomes non-null and effectiveCheckedIds permanently prefers that local Set over rolePerms. The state is not reset when vaiTroId changes, while the mutation hook is tied to the current vaiTroId. If the same SPA component instance moves from one role id to another, the UI can continue showing the previous role's permission IDs and Save will write those stale IDs to the new role, corrupting authorization configuration.

**Cách tái hiện:**

> Open /quan-tri/vai-tro/role-a/quyen-han, toggle any permission so checkedIds is non-null, then navigate within the SPA to /quan-tri/vai-tro/role-b/quyen-han without a full reload. The page can keep role-a's selected permissions; clicking Save sends those IDs to the role-b mutation.

**Khuyến nghị fix:**

> Reset or scope the local permission state by role id. For example, clear checkedIds in an effect keyed by vaiTroId, or store { roleId, ids } and only use the local set when it matches the current route param. Add a guard so Save cannot run against stale selections during role transitions.

---

#### #46. Rollback deletes pre-existing DotBaoCao permissions

- **ID:** `fnd_sig-feat-library-147f63b418-1441_5329815e6f`
- **Feature:** `feat_library_147f63b418`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/1744000000022-PermissionMatrixGapFixes.ts:46-57 (`PermissionMatrixGapFixes1744000000022.up`)`
- `packages/api/src/database/migrations/1744000000022-PermissionMatrixGapFixes.ts:80-99 (`PermissionMatrixGapFixes1744000000022.down`)`

**Giải thích:**

> The migration documents that the five generic DotBaoCao permissions already exist before this migration, while only gui-tw_dot_bao_cao and tong-hop_dot_bao_cao are net-new. The rollback path nevertheless deletes role grants and permission rows for all seven codes. A migration revert would remove existing authorization data, not just undo this migration's additions.

**Cách tái hiện:**

> Seed create/read/update/delete/approve_dot_bao_cao and grants, run PermissionMatrixGapFixes1744000000022.up(), then down(); the generic permission rows and their vai_tro_quyen_han grants are deleted.

**Khuyến nghị fix:**

> Restrict rollback deletion to permissions this migration truly owns, or make DotBaoCao permission rollback a no-op if the seed is now authoritative. Do not delete pre-existing CRUD/approve permissions or their grants.

---

#### #47. Tieu-chi batch upsert treats unknown IDs as new rows and can delete existing criteria

- **ID:** `fnd_sig-feat-library-237acd59eb-063e_00706bfe0b`
- **Feature:** `feat_library_237acd59eb`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/danh-gia/tieu-chi-danh-gia.service.ts:136-144 (`TieuChiDanhGiaService.batchUpsert`)`
- `packages/api/src/modules/danh-gia/tieu-chi-danh-gia.service.ts:157-175 (`TieuChiDanhGiaService.batchUpsert`)`
- `packages/api/src/modules/danh-gia/tieu-chi-danh-gia.service.ts:179-183 (`TieuChiDanhGiaService.batchUpsert`)`

**Giải thích:**

> When a payload item includes an id that is not in existingMap, the service does not reject it and does not preserve that id. It inserts a brand-new criterion, while payloadIds still contains the unknown id, then hard-deletes every existing criterion whose real id is absent from the payload. A stale or foreign id can therefore silently replace/delete criteria instead of producing a validation error.

**Khuyến nghị fix:**

> Before mutating, validate that every supplied id exists in the current plan's existingMap. Reject unknown or foreign ids with a 422/404. Only id-less items should enter the insert branch, and deletion should be explicit or guarded by a validated full-replacement contract.

---

#### #48. VSIC normalization destroys doanh_nghiep_linh_vuc rows despite requiring an empty bridge

- **ID:** `fnd_sig-feat-library-4a3c8e7bf3-d628_56029ad20c`
- **Feature:** `feat_library_4a3c8e7bf3`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026051200010-NormalizeLinhVucKinhDoanhVsic2025.ts:4-8 (`NormalizeLinhVucKinhDoanhVsic20252026051200010`)`
- `packages/api/src/database/migrations/2026051200010-NormalizeLinhVucKinhDoanhVsic2025.ts:31-34 (`NormalizeLinhVucKinhDoanhVsic20252026051200010.up`)`
- `packages/api/src/database/migrations/2026051200010-NormalizeLinhVucKinhDoanhVsic2025.ts:16-19 (`NormalizeLinhVucKinhDoanhVsic20252026051200010`)`

**Giải thích:**

> The migration documents a required production safety gate, but the code does not enforce it. If any real doanh_nghiep_linh_vuc rows exist, they are deleted irreversibly before the catalog reset. Rollback recreates legacy danh_muc rows only, not the deleted business-sector assignments.

**Cách tái hiện:**

> Run the migration on a database with at least one doanh_nghiep_linh_vuc row. The row is deleted by line 31 and cannot be recovered by down().

**Khuyến nghị fix:**

> Fail fast when the bridge is non-empty unless an explicit, audited migration path remaps those rows to VSIC 2025 IDs. A simple DO block that raises when EXISTS (SELECT 1 FROM doanh_nghiep_linh_vuc) would enforce the documented gate.

---

#### #49. congKhai validates snapshot files after the external publish side effect

- **ID:** `fnd_sig-feat-library-12d84f0027-1a97_103bf5e942`
- **Feature:** `feat_library_12d84f0027`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:1719-1732 (`HoiDapService.buildCongKhaiSnapshot`)`
- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:1856-1862 (`HoiDapService.congKhai`)`
- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:1908-1930 (`HoiDapService.congKhai`)`

**Giải thích:**

> buildCongKhaiSnapshot can throw for missing files, files still being scanned, or files owned by another aggregate. congKhai() calls congPlqgClient.congKhaiHoiDap() first and only then builds the avatar/attachment snapshot. If the external portal accepts the publish but snapshot validation fails, the API returns an error after the public side effect and the local row is left in a partially updated PENDING state rather than CONG_KHAI or FAILED.

**Khuyến nghị fix:**

> Validate and reserve all requested publication files before calling Cổng PLQG, or compensate on post-call validation failure by marking FAILED and undoing/unpublishing the external side effect if possible.

---

### 3.3 Lỗi logic (Bug) — 13 findings

#### #50. Activation listener is not RLS-safe, so NHT rows may never auto-promote

- **ID:** `fnd_sig-feat-library-5c0f2f22ea-da18_229f11abc6`
- **Feature:** `feat_library_5c0f2f22ea`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/nguoi-ho-tro/services/nguoi-ho-tro.service.ts:129-138 (`NguoiHoTroService.create`)`
- `packages/api/src/modules/nguoi-ho-tro/services/nguoi-ho-tro.service.ts:546-558 (`NguoiHoTroService.onTaiKhoanActivated`)`

**Giải thích:**

> The service documents that nguoi_ho_tro requires the request-pinned QueryRunner because fresh DataSource connections have no RLS GUCs. The tai_khoan.activated listener ignores that and uses a bare DataSource repository, so under forced RLS its findOne can see no row, or its update can affect zero rows. The account activation path can report success while the NHT entity remains CHO_KICH_HOAT.

**Cách tái hiện:**

> Create an NHT, verify the email so AuthService emits tai_khoan.activated, and run as the app role with FORCE RLS enabled. The listener queries nguoi_ho_tro through DataSource.getRepository without app.* GUCs, so the row is not promoted to HOAT_DONG.

**Khuyến nghị fix:**

> Run this listener through an RLS-pinned manager when CLS has one, or open an explicit system transaction that sets the required RLS context. Check UpdateResult.affected and log or throw when the promotion did not happen.

---

#### #51. Background crons do not pin a DB-level system RLS context

- **ID:** `fnd_sig-feat-library-4879d8b29e-1330_5d93f24550`
- **Feature:** `feat_library_4879d8b29e`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/vu-viec/vu-viec-bo-sung-timeout.cron.ts:26-37 (`VuViecBoSungTimeoutCron.handleBoSungTimeout`)`
- `packages/api/src/modules/vu-viec/vu-viec-sla-warning.cron.ts:44-53 (`VuViecSlaWarningCron.handleSlaWarning`)`
- `packages/api/src/modules/vu-viec/vu-viec-notification.listener.ts:66-72 (`VuViecNotificationListener.onIntake`)`

**Giải thích:**

> The notification listener documents the same background-execution problem and uses InternalSystemQueryBuilder to pin app.current_cap='TW'. The two cron handlers instead use the lightweight runAsSystem wrapper and normal repository/transaction calls. Inspecting common/context/run-as-system.ts showed it only constructs a TenantContext; it does not set Postgres GUCs. With FORCE RLS enabled on vu_viec, these sweeps can find zero rows or fail writes in production while passing mocked unit tests.

**Khuyến nghị fix:**

> Run both cron sweeps through a QueryRunner that sets app.current_cap='TW' (for example InternalSystemQueryBuilder.runAsSystem), and use that runner/manager for the select, lock, update, and audit writes.

---

#### #52. Batch approval bypasses the BR-CALC-01 threshold invariant

- **ID:** `fnd_sig-feat-library-4b3e6cdceb-b960_57fbc628eb`
- **Feature:** `feat_library_4b3e6cdceb`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/chi-tra/chi-tra.service.ts:1186-1201 (`ChiTraService.pheDuyetHoSo`)`
- `packages/api/src/modules/chi-tra/chi-tra.service.ts:1335-1357 (`ChiTraService.batchPheDuyet`)`
- `packages/api/src/modules/chi-tra/chi-tra.service.br-calc-01-invariant.spec.ts:75-78 (`makeMismatchedEntity`)`
- `packages/api/src/modules/chi-tra/chi-tra.service.br-calc-01-invariant.spec.ts:196-206`

**Giải thích:**

> Single approval now rejects mismatched support thresholds, but batch approval goes straight from locked entity to approved state without calling getThresholds or checking mucHoTroPhanTram/tranHoTroNam. A dossier that pheDuyetHoSo rejects for NHO+90% can still be approved through batchPheDuyet, then paid at a rate the invariant explicitly forbids.

**Cách tái hiện:**

> Use the mismatched fixture from chi-tra.service.br-calc-01-invariant.spec.ts, but pass its id to batchPheDuyet({ ids: [id] }) as CB_PD_DP. The batch path has no BR-CALC-01 check and will count it as a success if state and donVi pass.

**Khuyến nghị fix:**

> Extract the BR-CALC-01 validation into a shared helper and call it from both pheDuyetHoSo and each per-record branch of batchPheDuyet before saving the approval.

---

#### #53. Case attachments are saved as file IDs but downloaded as MinIO object keys

- **ID:** `fnd_sig-feat-library-4879d8b29e-ed07_9b4b6ca955`
- **Feature:** `feat_library_4879d8b29e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/vu-viec/vu-viec.service.ts:279-291 (`VuViecService.createForDn`)`
- `packages/api/src/modules/vu-viec/vu-viec.service.ts:480-491 (`VuViecService.boSung`)`
- `packages/api/src/modules/vu-viec/vu-viec.service.ts:2143-2148 (`VuViecService.getHoSo`)`

**Giải thích:**

> The write paths accept fileDinhKemIds and persist each ID into duongDanFile, but the read path treats duongDanFile as the MinIO object key. Uploaded file rows normally separate id from object path, so DN submission and supplement attachments will produce broken presigned URLs. The same path also skips ownership/existence/linkage validation, so a caller can reference arbitrary UUIDs as case documents.

**Khuyến nghị fix:**

> Resolve each fileDinhKemId through the file service/repository, validate it exists, belongs to the caller's scope, and is not already linked, then either store the actual object key/metadata in HoSoVuViec or link file_dinh_kem to the VuViec/HoSo entity and generate downloads through FileService.

---

#### #54. DotBaoCao service cannot start newly created reporting periods

- **ID:** `fnd_sig-feat-library-ff05b92ee9-cb2e_886222e329`
- **Feature:** `feat_library_ff05b92ee9`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/services/ct-htpldn/dot-bao-cao.service.ts:15-27 (`createDotBaoCao`)`
- `packages/web/src/services/ct-htpldn/dot-bao-cao.service.ts:35-42 (`updateSoLieu, submitBc`)`

**Giải thích:**

> The service exposes create, detail, updateSoLieu, and submitBc, but no wrapper for the required POST /dot-bao-caos/:id/start transition. In the inspected backend workflow, created dots begin in TAO_DOT, start creates the associated BAO_CAO_CT_HTPL record and moves the dot to DANG_LAP_BC, while updateSoLieu and submitBc are guarded to DANG_LAP_BC. Without this service surface, newly created reporting periods cannot be progressed through the frontend into report entry/submission.

**Cách tái hiện:**

> Create a dot bao cao from the frontend, open its detail while it is still TAO_DOT, and observe there is no service-backed action that can call /dot-bao-caos/:id/start before updateSoLieu or submitBc.

**Khuyến nghị fix:**

> Add a startDotBaoCao(dotId, payload) service function posting to `${BASE}/${dotId}/start`, then wire a hook/action for TAO_DOT so users can create the report draft before saving/submitting data.

---

#### #55. Edit-mode load failure falls through to create

- **ID:** `fnd_sig-feat-library-2b550d51cd-d3d8_5e4b7f7e7e`
- **Feature:** `feat_library_2b550d51cd`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/chuyen-gia-tvv/to-chuc/form.tsx:36-40 (`ToChucTuVanFormPage`)`
- `packages/web/src/pages/chuyen-gia-tvv/to-chuc/form.tsx:102-105 (`handleSubmit`)`
- `packages/web/src/pages/chuyen-gia-tvv/to-chuc/form.tsx:109 (`ToChucTuVanFormPage`)`

**Giải thích:**

> On an edit URL, once getToChucTuVanById fails or returns no detail, isLoading becomes false and the page renders the edit form with detail still undefined. Submitting then enters the else branch and calls createToChucTuVan instead of blocking or showing an error, which can create a duplicate/incorrect organization from an edit workflow.

**Cách tái hiện:**

> Mock getToChucTuVanById to reject on /chuyen-gia-tvv/to-chuc/tctv-1/chinh-sua, fill the required fields, and submit. createToChucTuVan is called even though isEdit is true.

**Khuyến nghị fix:**

> In edit mode, never fall back to create. Render an error/empty state when the detail query fails or returns no data, disable submit until detail exists, and make handleSubmit return/throw if isEdit && !detail.

---

#### #56. HoiDap status backfill violates the legacy CHECK before it is dropped

- **ID:** `fnd_sig-feat-library-6677354b4e-d636_3cce6e4a44`
- **Feature:** `feat_library_6677354b4e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050201003-AlignTrangThaiHoiDap.ts:12-20 (`AlignTrangThaiHoiDap2026050201003.up`)`
- `packages/api/src/database/migrations/2026050201003-AlignTrangThaiHoiDap.ts:35-45 (`AlignTrangThaiHoiDap2026050201003.up`)`

**Giải thích:**

> The documented live constraint allows legacy values such as MOI_TAO, CHO_DUYET and XU_LY, but not the replacement values MOI, CHO_PHE_DUYET or DANG_XU_LY. Because up() performs the UPDATEs before dropping the old CHECK, any legacy row that this migration is meant to repair will fail with a check-constraint violation and abort the migration.

**Cách tái hiện:**

> On a database with chk_hoi_dap_trang_thai allowing MOI_TAO but not MOI, insert a hoi_dap row with trang_thai='MOI_TAO' and run this migration; the first UPDATE violates the still-active CHECK.

**Khuyến nghị fix:**

> Drop both existing hoi_dap status CHECK constraints before the backfill, then add the replacement constraint after all values have been normalized.

---

#### #57. Request paths leave the RLS-pinned transaction for code generation and writes

- **ID:** `fnd_sig-feat-library-237acd59eb-21fa_5f3daed468`
- **Feature:** `feat_library_237acd59eb`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/danh-gia/ket-qua-danh-gia.service.ts:114-118 (`KetQuaDanhGiaService.getEligibleCases`)`
- `packages/api/src/modules/danh-gia/bao-cao-danh-gia.service.ts:66-72 (`BaoCaoDanhGiaService.generateMaBaoCao`)`
- `packages/api/src/modules/danh-gia/bao-cao-danh-gia.service.ts:145-172 (`BaoCaoDanhGiaService.getOrCreate`)`
- `packages/api/src/modules/danh-gia/ke-hoach-danh-gia.service.ts:160-166 (`KeHoachDanhGiaService.generateMaKeHoach`)`
- `packages/api/src/modules/danh-gia/tieu-chi-danh-gia.service.ts:128-130 (`TieuChiDanhGiaService.batchUpsert`)`

**Giải thích:**

> This module documents that raw DataSource work uses a fresh pool connection without the request RLS GUCs, but several owned paths still use fresh DataSource transactions/query runners for RLS-protected tables. For non-TW users this can fail closed with empty counts or RLS write errors; the count-based code generators can also keep returning the first daily code, causing duplicate-code 500s after the first create.

**Khuyến nghị fix:**

> Run these operations through the CLS/RLS-pinned repository manager, or explicitly set the same RLS context on any new QueryRunner before touching tenant tables. Replace count-based daily code generation with the existing sequence-counter style helper if available.

---

#### #58. TVV create can succeed without the mandatory thẻ hành nghề file

- **ID:** `fnd_sig-feat-library-4372595c43-5d09_deabd8f501`
- **Feature:** `feat_library_4372595c43`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/chuyen-gia-tvv/form/index.tsx:124-130 (`handleSubmit`)`
- `packages/web/src/pages/chuyen-gia-tvv/form/index.tsx:217-226 (`handleSubmit`)`
- `packages/web/src/pages/chuyen-gia-tvv/form/index.tsx:235-258 (`handleSubmit`)`

**Giải thích:**

> The form only verifies that a TVV user selected a thẻ hành nghề file before creating the row. After POST /tu-van-viens succeeds, upload or FK-link failure for that mandatory file is downgraded to a warning, pending state is cleared, and the user is navigated to detail. That leaves a persisted TVV hồ sơ without the required fileTheHanhNgheId/file link, contradicting the form's own mandatory rule.

**Cách tái hiện:**

> Create a TVV with otherwise valid fields and a PDF selected, then make uploadTuVanVienFile or the follow-up updateTuVanVien link call fail. The page warns but still navigates to /chuyen-gia-tvv/:id with the mandatory file missing.

**Khuyến nghị fix:**

> For loaiTvv=TVV, treat thẻ hành nghề upload and link as part of the success condition. On failure, show a blocking error and keep the user on a recoverable form/edit state, or move create+mandatory-file linking into a backend transaction-like endpoint.

---

#### #59. TVV public list/search predicates are mutually exclusive

- **ID:** `fnd_sig-feat-library-c7a08e057f-9870_bc5d596e86`
- **Feature:** `feat_library_c7a08e057f`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/api-public/services/public-api-base.service.ts:8 (`PUBLISHABLE_STATES`)`
- `packages/api/src/modules/api-public/services/public-api-base.service.ts:15-17 (`PublicApiBaseService.buildPublishableQuery`)`
- `packages/api/src/modules/api-public/services/tu-van-vien-public.service.ts:23 (`TVV_PUBLISHABLE_STATE`)`
- `packages/api/src/modules/api-public/services/tu-van-vien-public.service.ts:141-143 (`TuVanVienPublicService.list`)`
- `packages/api/src/modules/api-public/services/tu-van-vien-public.service.ts:194-195 (`TuVanVienPublicService.search`)`

**Giải thích:**

> Both TVV list and search start with the shared publishable predicate `trangThai IN ('DA_DUYET','HOAN_THANH','CONG_KHAI','DA_CONG_BO')` and then add `trangThai = 'HOAT_DONG'`. No row can satisfy both, so active consultants are always filtered out and the public TVV endpoints return empty results.

**Khuyến nghị fix:**

> Do not use the cross-state `buildPublishableQuery` for TVV. Build a TVV-specific query with `tvv.trangThai = HOAT_DONG` and any explicit public-visibility flag required by the TVV contract.

---

#### #60. batchCongKhai publishes records with no approved response

- **ID:** `fnd_sig-feat-library-12d84f0027-221d_0c67e3d052`
- **Feature:** `feat_library_12d84f0027`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:1831-1842 (`HoiDapService.congKhai`)`
- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:2158-2168 (`HoiDapService.batchCongKhai`)`
- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:2171-2187 (`HoiDapService.batchCongKhai`)`

**Giải thích:**

> The single-record congKhai path refuses to publish unless a DA_DUYET PhanHoi exists. The batch path treats latestPhanHoi as optional, fills noiDungPhanHoi with an empty string, calls the external publish API, and marks the HoiDap CONG_KHAI. This lets batch publishing create public Q&A entries with no approved answer, violating the invariant enforced by the single endpoint.

**Khuyến nghị fix:**

> In batchCongKhai, fail each item that has no DA_DUYET PhanHoi before building the PLQG payload or changing local state; keep the single-record and batch preconditions identical.

---

#### #61. cau_hinh_phan_cong backfill can create duplicate non-null unique keys

- **ID:** `fnd_sig-feat-library-6677354b4e-436a_36f9c0ccc2`
- **Feature:** `feat_library_6677354b4e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050201009-CauHinhPhanCongDonViNotNull.ts:4-8 (`CauHinhPhanCongDonViNotNull2026050201009.up`)`
- `packages/api/src/database/migrations/2026050201009-CauHinhPhanCongDonViNotNull.ts:56-73 (`CauHinhPhanCongDonViNotNull2026050201009.up`)`
- `packages/api/src/database/migrations/2026050201009-CauHinhPhanCongDonViNotNull.ts:79-96 (`CauHinhPhanCongDonViNotNull2026050201009.up`)`

**Giải thích:**

> Duplicate NULL rows are exactly possible because the old partial unique index excluded don_vi_id IS NULL. If two NULL rows share the same linh_vuc_id, nguoi_xu_ly_id and loai_yeu_cau, the NOT EXISTS check sees sibling rows with don_vi_id still NULL, so both rows are updated to the same tk.don_vi_id. The existing partial unique index can reject the UPDATE, or the later full unique index can fail if the old index is absent.

**Cách tái hiện:**

> Create two cau_hinh_phan_cong rows with identical linh_vuc_id, nguoi_xu_ly_id and loai_yeu_cau, both don_vi_id=NULL, where the assignee tai_khoan has a non-null don_vi_id; run up().

**Khuyến nghị fix:**

> Deduplicate NULL rows before backfill, or use a CTE with row_number() partitioned by the target non-null key and only update the first row while deleting or auditing the rest.

---

#### #62. maChuongTrinh generation can collide across tenants and concurrent creates

- **ID:** `fnd_sig-feat-library-49045a8908-2f69_ecb91361f7`
- **Feature:** `feat_library_49045a8908`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/ct-htpldn/chuong-trinh-htpl.service.ts:253-279 (`ChuongTrinhHtplService.createChuongTrinh`)`
- `packages/api/src/modules/ct-htpldn/chuong-trinh-htpl.service.ts:607-616 (`ChuongTrinhHtplService.generateMaChuongTrinh`)`

**Giải thích:**

> The next code is derived from a count over the caller's RLS-scoped query and is not protected by a lock or database sequence. Two tenants that cannot see each other's rows can both generate the same CT-{date}-0001, and two concurrent creates in the same scope can also observe the same count before either save commits. That produces duplicate public program codes and, with the existing unique code constraint, turns normal create traffic into insert failures.

**Cách tái hiện:**

> Have two non-TW units create their first CT HTPL on the same date, or issue two concurrent createChuongTrinh calls after both generateMaChuongTrinh calls read the same count; both calls generate the same maChuongTrinh.

**Khuyến nghị fix:**

> Generate maChuongTrinh from a database sequence/identity-backed allocator or reserve the daily sequence in a single atomic statement under a unique key. Do not derive it from an RLS-visible COUNT(*).

---

### 3.4 Đồng thời/Giao dịch (Concurrency) — 11 findings

#### #63. Course capacity can be exceeded by concurrent registrations

- **ID:** `fnd_sig-feat-library-10582b7f1a-15ef_bcd81dc4cc`
- **Feature:** `feat_library_10582b7f1a`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/api-public/services/dang-ky-dao-tao-public.service.ts:115-125 (`DangKyDaoTaoPublicService.createInbound`)`
- `packages/api/src/modules/api-public/services/dang-ky-dao-tao-public.service.ts:153-165 (`DangKyDaoTaoPublicService.createInbound`)`

**Giải thích:**

> The max-capacity check is a read-count-then-insert sequence with no lock on the course, no lock on a per-course capacity key, and no conditional counter update. Under concurrent registrations, two transactions can both observe activeCount below soLuongToiDa and both insert CHO_DUYET rows, overbooking the course.

**Cách tái hiện:**

> For a public enrollable course with soLuongToiDa=1 and zero active registrations, submit two different maCongPlqg registration requests concurrently; both can pass the count check and save.

**Khuyến nghị fix:**

> Serialize capacity checks per khoaHocId using a pessimistic lock on the KhoaHoc row or an advisory transaction lock, then count and insert under that lock. A stronger fix is an atomic capacity counter or database-enforced invariant for active registrations.

---

#### #64. Expiry job can disable an account that activates after the initial scan

- **ID:** `fnd_sig-feat-library-10e9ed03ca-b313_eae1fd8836`
- **Feature:** `feat_library_10e9ed03ca`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/auth/jobs/expire-unactivated-accounts.job.ts:28-36 (`ExpireUnactivatedAccountsJob.handleExpiry`)`
- `packages/api/src/modules/auth/jobs/expire-unactivated-accounts.job.ts:48-53 (`ExpireUnactivatedAccountsJob.handleExpiry`)`
- `packages/api/src/modules/auth/jobs/expire-unactivated-accounts.job.ts:55-57 (`ExpireUnactivatedAccountsJob.handleExpiry`)`

**Giải thích:**

> The job first reads accounts in CHO_KICH_HOAT older than the cutoff, then later updates each account by id only. If a user activates between the read and the transaction, the transaction still overwrites the now-active account to VO_HIEU_HOA. For doanhNghiepId accounts it can also delete the associated DOANH_NGHIEP record after activation, which is a data-loss outcome. The state and cutoff predicates need to be rechecked atomically inside the write/delete transaction.

**Cách tái hiện:**

> Have the cron read an expired CHO_KICH_HOAT account, activate that account before its loop iteration runs, then let the job transaction execute. The current update predicate `{ id: account.id }` still disables it and the DN delete still runs from the stale in-memory `doanhNghiepId`.

**Khuyến nghị fix:**

> Make the transaction conditional on the account still being unactivated and older than the cutoff, and only delete the doanh nghiep row if that conditional update affected one row. Prefer a guarded update such as `{ id, trangThai: CHO_KICH_HOAT, ngayTao: LessThan(cutoff) }` followed by checking `affected === 1` before deleting, auditing, or notifying.

---

#### #65. HoiDap code generation can duplicate across tenants or concurrent creates

- **ID:** `fnd_sig-feat-library-12d84f0027-a959_2be468c225`
- **Feature:** `feat_library_12d84f0027`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:649-681 (`HoiDapService.create`)`
- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:1243-1265 (`HoiDapService.generateMaHoiDap`)`

**Giải thích:**

> create() calls generateMaHoiDap() without a transaction, advisory lock, or RLS-bypassing manager. generateMaHoiDap() uses MAX(maHoiDap) over the caller-visible repository, while the code comment notes that tenant-scoped MAX can miss rows in other donVi and collide with the global unique code. Two same-day creates, especially from different tenant scopes, can generate the same HD-YYYYMMDD-NNN value and fail on insert or surface a 500.

**Khuyến nghị fix:**

> Allocate maHoiDap with a database sequence or with an advisory transaction lock plus a manager that sees the global code namespace; also catch/retry unique violations as a final guard.

---

#### #66. Optimistic lock is checked outside the write, so concurrent updates can overwrite each other

- **ID:** `fnd_sig-feat-library-c6797f4fce-b107_f45c303a79`
- **Feature:** `feat_library_c6797f4fce`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/danh-muc/danh-muc.service.ts:167-180 (`DanhMucService.updateDanhMuc`)`
- `packages/api/src/modules/danh-muc/danh-muc.service.ts:202-208 (`DanhMucService.updateDanhMuc`)`
- `packages/api/src/modules/danh-muc/danh-muc.service.ts:214-234 (`DanhMucService.toggleStatus`)`

**Giải thích:**

> The service reads a row, compares the version in application code, then later saves by primary key. Two requests can both read version N, both pass the check, and both save version N+1; the later save silently wins instead of raising ERR optimistic lock. toggleStatus has the same read-modify-save pattern and does not require a caller-supplied version at all, so it can also overwrite concurrent field changes with a stale entity snapshot.

**Cách tái hiện:**

> Send two concurrent PATCH /danh-muc/:id requests with the same version but different field changes. Both can pass the version check before either save commits; the final row contains whichever save finishes last and both responses can report success.

**Khuyến nghị fix:**

> Make updates atomic: issue UPDATE ... WHERE id = :id AND version = :expectedVersion and treat affected=0 as OPTIMISTIC_LOCK, or use a transaction with a row lock plus a version predicate. Require the same version contract for toggleStatus or implement it as a conditional update that only changes status and version.

---

#### #67. Optimistic locking is checked outside the write

- **ID:** `fnd_sig-feat-library-a10207fa13-e907_700a599e90`
- **Feature:** `feat_library_a10207fa13`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/vai-tro/dto/update-vai-tro.dto.ts:7-10 (`UpdateVaiTroDto.version`)`
- `packages/api/src/modules/vai-tro/vai-tro.service.ts:133-153 (`VaiTroService.update`)`
- `packages/api/src/modules/vai-tro/vai-tro.service.ts:158-175 (`VaiTroService.toggleStatus`)`

**Giải thích:**

> UpdateVaiTroDto requires version specifically to avoid concurrent update conflicts, but update() performs findOne(), compares entity.version in memory, then later saves without constraining the UPDATE by that version. Two concurrent requests can both read version 1, both pass the check, and both save version 2, so one update is silently lost instead of returning ERR-STATE-LOCK-409. toggleStatus() has the same read-modify-write shape and does not accept a version at all.

**Cách tái hiện:**

> Start with a role at version 1. Send two PATCH /vai-tro/:id requests concurrently with body {"version":1,"tenVaiTro":"A"} and {"version":1,"tenVaiTro":"B"}. If both read before either save completes, both can return success and the later save overwrites the earlier one.

**Khuyến nghị fix:**

> Make the version check part of the database write, for example UPDATE ... WHERE id = :id AND version = :version with affected === 1, or use TypeORM optimistic locking/transactions correctly. For toggleStatus, require a version or perform a locked transactional read plus write.

---

#### #68. Optimistic update check is not atomic

- **ID:** `fnd_sig-feat-library-707dcd8fba-cef9_f764a18ce6`
- **Feature:** `feat_library_707dcd8fba`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/quan-tri/don-vi/don-vi.service.ts:184-192 (`DonViService.update`)`
- `packages/api/src/modules/quan-tri/don-vi/don-vi.service.ts:219-227 (`DonViService.update`)`

**Giải thích:**

> The version comparison happens after a separate read and before a plain save. Two concurrent PATCH requests carrying the same version can both read the same entity, both pass the check, and both save version+1. The later save wins instead of returning the intended optimistic-lock ConflictException, so concurrent admin edits can be silently lost.

**Cách tái hiện:**

> Start with a DonVi row at version 1. Send two concurrent PATCH /don-vi/:id requests with body {"version":1} and different field changes. Both requests can pass the in-memory version check before either save commits; the second write overwrites the first while returning success.

**Khuyến nghị fix:**

> Make the write conditional at the database level, for example UPDATE don_vi SET ..., version = version + 1 WHERE id = :id AND version = :dtoVersion RETURNING *, or use a transaction with a row lock/TypeORM optimistic lock that fails when zero rows are affected.

---

#### #69. PATCH optimistic locking is not atomic

- **ID:** `fnd_sig-feat-library-f72aa3f50c-c3eb_c6e14d544d`
- **Feature:** `feat_library_f72aa3f50c`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.service.ts:439-453 (`HopDongTuVanService.update`)`
- `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.service.ts:492-498 (`HopDongTuVanService.update`)`
- `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.service.ts:503-514 (`HopDongTuVanService.update`)`

**Giải thích:**

> The service reads the row and checks dto.version before the write, but the subsequent save is not guarded by a WHERE version predicate and the vuViecIds branch starts its transaction only after that check. Two concurrent PATCH requests with the same version can both pass, then the later save overwrites the earlier update instead of returning the intended optimistic-lock conflict.

**Cách tái hiện:**

> Send two concurrent PATCH /hop-dong-tu-vans/:id requests with the same current version and different field changes. Both can pass the pre-save version check; the final row reflects whichever save lands last.

**Khuyến nghị fix:**

> Make the version check part of the write: use a conditional UPDATE with id + version in the WHERE clause, or lock the row with findForUpdateScoped inside a transaction before checking version and saving for both update branches.

---

#### #70. Payment update validates stale state before taking the row lock

- **ID:** `fnd_sig-feat-library-4b3e6cdceb-ed97_5db9d9803a`
- **Feature:** `feat_library_4b3e6cdceb`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/chi-tra/chi-tra.service.ts:1395-1407 (`ChiTraService.capNhatThanhToan`)`
- `packages/api/src/modules/chi-tra/chi-tra.service.ts:1430-1442 (`ChiTraService.capNhatThanhToan`)`
- `packages/api/src/modules/chi-tra/chi-tra.service.integration.spec.ts:87-95`
- `packages/api/src/modules/chi-tra/chi-tra.service.integration.spec.ts:147-155`

**Giải thích:**

> capNhatThanhToan performs the optimistic version check, state guard, and amount validation on an unlocked read. The locked entity fetched later is saved without rechecking version or state. Two requests that both read version 6 before either reaches findForUpdateScoped can both pass validation; the second request then waits for the first, locks the updated row, and still writes payment fields and sends notifications based on stale validation.

**Cách tái hiện:**

> Start with a DA_DUYET dossier at version 6. Send two capNhatThanhToan DA_THANH_TOAN requests concurrently with version 6. Arrange both initial findOne calls to return before either lock/save. The second request can save after the first because the locked entity is not revalidated.

**Khuyến nghị fix:**

> Move the version, workflow guard, and payment amount/date checks to run after findForUpdateScoped, or repeat them against the locked entity immediately before merge/save. Apply the same pattern to sibling workflows that pre-read then lock.

---

#### #71. Publish and unpublish jobs for the same row can run out of order

- **ID:** `fnd_sig-feat-library-176c85ef2e-8d17_7a2ba4d8cb`
- **Feature:** `feat_library_176c85ef2e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/tu-van/processors/noi-dung-tu-van-cs-sync.processor.ts:23-27 (`NOI_DUNG_TU_VAN_CS_SYNC_CONCURRENCY`)`
- `packages/api/src/modules/tu-van/processors/noi-dung-tu-van-cs-sync.processor.ts:42-47 (`NoiDungTuVanCsSyncProcessor.process`)`
- `packages/api/src/modules/tu-van/processors/tu-lieu-phap-ly-vv-sync.processor.ts:22-24 (`TU_LIEU_PHAP_LY_VV_SYNC_CONCURRENCY`)`
- `packages/api/src/modules/tu-van/processors/tu-lieu-phap-ly-vv-sync.processor.ts:38-43 (`TuLieuPhapLyVvSyncProcessor.process`)`

**Giải thích:**

> Both queues explicitly allow two jobs to be active at once, while the job name selects opposite external side effects for the same entity. There is no per-tvcsId/tuLieuId serialization, stale-operation check, or version check in process(). A publish job and a later unpublish job for the same row can therefore overlap and complete in the wrong order, leaving the external portal in the older state after the user's latest transition.

**Cách tái hiện:**

> Configure the default concurrency of 2, make the publish gateway call block, enqueue publish for an entity, then enqueue unpublish for the same entity. The unpublish job can run while publish is blocked; when publish resumes last, it performs the stale external publish after the later unpublish intent.

**Khuyến nghị fix:**

> Serialize jobs per entity or make each job conditional on the row still wanting that operation. A minimal conservative fix is concurrency 1 for these queues; a better fix is to include an operation/version in the job payload and skip stale jobs after loading the current row under a lock.

---

#### #72. Supplement timeout cron can reject a case after it was already supplemented

- **ID:** `fnd_sig-feat-library-4879d8b29e-9c21_8d0e14d821`
- **Feature:** `feat_library_4879d8b29e`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/vu-viec/vu-viec-bo-sung-timeout.cron.ts:32-37 (`VuViecBoSungTimeoutCron.handleBoSungTimeout`)`
- `packages/api/src/modules/vu-viec/vu-viec-bo-sung-timeout.cron.ts:48-57 (`VuViecBoSungTimeoutCron.handleBoSungTimeout`)`

**Giải thích:**

> The state/cutoff predicate is evaluated before the per-row transaction. If a DN submits bổ sung after the sweep selects the row but before findForUpdateScoped locks it, the locked entity can already be DANG_KIEM_TRA or have a newer ngayYeuCauBoSung, yet the cron still sets it to TU_CHOI. That loses a valid supplement and creates a false auto-rejection audit.

**Khuyến nghị fix:**

> After acquiring the lock, revalidate entity.trangThai, entity.ngayYeuCauBoSung, and the cutoff before updating, or perform a conditional UPDATE with WHERE id, state, and cutoff and only audit when affected=1.

---

#### #73. huyCongKhai can overwrite a newer state after releasing its validation lock

- **ID:** `fnd_sig-feat-library-12d84f0027-9d06_a30d758fc5`
- **Feature:** `feat_library_12d84f0027`
- **Confidence:** high | **Triage:** confirmed-bug | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:2008-2037 (`HoiDapService.huyCongKhai`)`
- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:2039-2042 (`HoiDapService.huyCongKhai`)`
- `packages/api/src/modules/hoi-dap/hoi-dap.service.ts:2064-2073 (`HoiDapService.huyCongKhai`)`

**Giải thích:**

> huyCongKhai validates state/version in a short transaction, commits and releases the row lock, calls the external API, then unconditionally updates the row back to DA_DUYET with snapshot.version + 1. If another request changes the same record after validation, such as dongHoSo moving it to HOAN_THANH, this final update can revert the newer state and reuse a stale version.

**Khuyến nghị fix:**

> Use a reservation state before the external call or perform the final update with a WHERE id/version/trangThai condition and fail/compensate when no row is affected; avoid overwriting rows whose version changed after validation.

---

### 3.5 Build & Release — 11 findings

#### #74. Ant Design notification config uses an unsupported `title` field

- **ID:** `fnd_sig-feat-library-d8982b2895-b962_2307679399`
- **Feature:** `feat_library_d8982b2895`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/services/cau-hinh-sla/cau-hinh-sla.service.ts:60 (`useUpdateCauHinhSlaMutation`)`
- `packages/web/package.json:7`
- `packages/web/package.json:20`

**Giải thích:**

> Ant Design notification configs use `message` for the visible title text, not `title`. Because this package builds with `tsc`, the object literal passed to `notification.success` should fail type checking against Ant Design's notification args; if it were emitted, the intended success text would not be displayed correctly.

**Cách tái hiện:**

> Run `npm run build` from `packages/web`; TypeScript should reject the `notification.success` config in `cau-hinh-sla.service.ts`.

**Khuyến nghị fix:**

> Change the success call to `notification.success({ message: 'Cập nhật cấu hình SLA thành công' });` or include `description` if secondary text is needed.

---

#### #75. Audit CHECK swap drops inherited constraints from partitions

- **ID:** `fnd_sig-feat-library-d48d1976c5-39f1_ed6ee451d3`
- **Feature:** `feat_library_d48d1976c5`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050900047-AddKhoaHocLifecycleHanhDong.ts:69-83 (`AddKhoaHocLifecycleHanhDong2026050900047.swapAuditConstraint`)`
- `packages/api/src/database/migrations/2026050900047-AddKhoaHocLifecycleHanhDong.ts:89-100 (`AddKhoaHocLifecycleHanhDong2026050900047.swapAuditConstraint`)`
- `packages/api/src/database/migrations/2026051000003-AddSelfRegisterDnHanhDong.ts:36-50 (`AddSelfRegisterDnHanhDong2026051000003.swapAuditConstraint`)`
- `packages/api/src/database/migrations/2026051000003-AddSelfRegisterDnHanhDong.ts:53-65 (`AddSelfRegisterDnHanhDong2026051000003.swapAuditConstraint`)`

**Giải thích:**

> Both migrations discover every relation that has chk_audit_log_hanh_dong and then run ALTER TABLE ${tbl} DROP CONSTRAINT on each result. For declarative partitions, CHECK constraints inherited from the audit_log parent cannot be dropped directly from the child partition; the safe operation is to drop and recreate the parent constraint so PostgreSQL cascades it. This can block migration or rollback on databases with inherited child constraints, especially newer partitions created after the parent constraint was added.

**Khuyến nghị fix:**

> Replace the per-partition DROP/ADD loop with parent-only ALTER TABLE audit_log DROP/ADD. If local child constraints must be cleaned up, query pg_constraint for conislocal constraints separately and handle them explicitly after the parent path.

---

#### #76. Audit IP conversion can abort on malformed numeric-looking values

- **ID:** `fnd_sig-feat-library-147f63b418-cb54_dd3b21cbe8`
- **Feature:** `feat_library_147f63b418`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/1744000000023-DataIntegrityHardening.ts:373-376 (`DataIntegrityHardening1744000000023.up`)`

**Giải thích:**

> The regex is not a valid inet validator. Values such as 999.999.999.999 or :::: match the character whitelist, then ip_address::inet raises invalid input syntax. Since the old column is free-form varchar and this migration explicitly tries to tolerate non-IP strings by mapping them to NULL, this remaining class of bad legacy rows can block deployment.

**Cách tái hiện:**

> Before this migration, insert or update any audit_log row with ip_address = '999.999.999.999', then run DataIntegrityHardening1744000000023.up(); the ALTER COLUMN ... TYPE inet statement fails during the cast.

**Khuyến nghị fix:**

> Use a safe cast path, for example a temporary try_inet(text) PL/pgSQL helper that catches invalid_text_representation and returns NULL, or run an explicit preflight cleanup/update before ALTER TYPE. If you prefer failing, fail before ALTER with a clear query listing invalid rows.

---

#### #77. Audit-log rewrite migrations update an append-only table

- **ID:** `fnd_sig-feat-library-4a3c8e7bf3-2a52_f17f3eda5a`
- **Feature:** `feat_library_4a3c8e7bf3`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/1744000000005-CreateSystemConfig.ts:61-75 (`CreateSystemConfig1744000000005.up`)`
- `packages/api/src/database/migrations/2026051300200-BackfillVuViecTrinhPheDuyetToTrinhPd.ts:24-29 (`BackfillVuViecTrinhPheDuyetToTrinhPd2026051300200.up`)`
- `packages/api/src/database/migrations/2026051200030-AddChuyenKenhAuditAction.ts:65-71 (`AddChuyenKenhAuditAction2026051200030.down`)`
- `packages/api/src/database/migrations/2026051300010-AddYeuCauBoSungAuditAction.ts:70-77 (`AddYeuCauBoSungAuditAction2026051300010.down`)`

**Giải thích:**

> audit_log is explicitly append-only. Any matching row causes the trigger to abort UPDATE, so 2026051300200 fails in the exact legacy-data case it is meant to backfill. The down paths for the audit enum migrations have the same problem once new audit rows exist.

**Cách tái hiện:**

> On a database with audit_log(entity_type='VU_VIEC', hanh_dong='TRINH_PHE_DUYET'), run migration 2026051300200. The UPDATE fires audit_log_immutable and raises 'audit_log is immutable: UPDATE and DELETE are not allowed'.

**Khuyến nghị fix:**

> Do not rewrite audit_log rows in normal migrations. Prefer read-time normalization for legacy action names, or use a tightly scoped, explicitly documented administrative migration that disables and re-enables the immutable trigger in the same transaction if policy allows that exception.

---

#### #78. DiemDanh FK switch validates old registration IDs against hoc_vien without remap

- **ID:** `fnd_sig-feat-library-0d48ae6e7c-7a48_c3dcaf280e`
- **Feature:** `feat_library_0d48ae6e7c`
- **Confidence:** medium | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050601005-AlignDiemDanhEnumAndLichHocFk.ts:19-21 (`AlignDiemDanhEnumAndLichHocFk2026050601005.up`)`
- `packages/api/src/database/migrations/2026050601005-AlignDiemDanhEnumAndLichHocFk.ts:83-90 (`AlignDiemDanhEnumAndLichHocFk2026050601005.up`)`

**Giải thích:**

> The migration changes diem_danh.hoc_vien_id from referencing dang_ky_dao_tao(id) to hoc_vien(id), but it does not remap existing column values through dang_ky_dao_tao.hoc_vien_id or preflight rows that cannot be remapped. Any existing attendance row whose hoc_vien_id currently stores a registration id, as enforced by the old FK described in the migration, will either fail FK creation or become semantically corrupt if UUIDs happen to overlap.

**Khuyến nghị fix:**

> Before dropping the old FK, backfill diem_danh.hoc_vien_id from the referenced dang_ky_dao_tao row, constrained by the same khoa_hoc_id, and fail loudly on unresolved or duplicate mappings before adding the new FK.

---

#### #79. HoiDap refactor adds stricter checks without migrating legacy values

- **ID:** `fnd_sig-feat-library-0d48ae6e7c-b829_f396cd8348`
- **Feature:** `feat_library_0d48ae6e7c`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050700008-RefactorHoiDapForSrsV35.ts:15-17 (`RefactorHoiDapForSrsV35_2026050700008.up`)`
- `packages/api/src/database/migrations/2026050700008-RefactorHoiDapForSrsV35.ts:53-62 (`RefactorHoiDapForSrsV35_2026050700008.up`)`
- `packages/api/src/database/migrations/2026050700008-RefactorHoiDapForSrsV35.ts:74-77 (`RefactorHoiDapForSrsV35_2026050700008.up`)`
- `packages/api/src/database/migrations/2026050700008-RefactorHoiDapForSrsV35.ts:106-112 (`RefactorHoiDapForSrsV35_2026050700008.up`)`

**Giải thích:**

> The migration says it is renaming SAP_HET_HAN to SAP_HET and adds a new completion timestamp, but it never updates existing hoi_dap rows before adding validating CHECK constraints. A database with valid pre-migration rows where muc_do_canh_bao='SAP_HET_HAN' or trang_thai='HOAN_THANH' will fail while adding the new constraints because SAP_HET_HAN is no longer allowed and newly added ngay_hoan_thanh is NULL for existing rows.

**Khuyến nghị fix:**

> Before adding the new CHECK constraints, remap legacy muc_do_canh_bao values to SAP_HET and backfill ngay_hoan_thanh for completed rows from an agreed source such as ngay_cap_nhat/ngay_tao, or add an explicit fail-loud preflight before structural changes. Mirror the reverse remap in down().

---

#### #80. Included test file breaks the web package TypeScript build

- **ID:** `fnd_sig-feat-library-6b22a4d1b7-0bb9_3f4d7a674e`
- **Feature:** `feat_library_6b22a4d1b7`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/web/package.json:5-10`
- `packages/web/src/components/LinhVucKinhDoanhSelect/index.test.tsx:199-203`

**Giải thích:**

> The package build runs TypeScript before Vite, and this linked test casts a partial mock object directly to ReturnType<typeof useDanhMucTree>. Running `pnpm --dir packages/web exec tsc --noEmit --pretty false` reports TS2352 at this file/line because the object lacks required UseQueryResult members. That blocks release builds even if the Vitest runtime assertions pass.

**Cách tái hiện:**

> pnpm --dir packages/web exec tsc --noEmit --pretty false

**Khuyến nghị fix:**

> Use a complete mocked UseQueryResult helper, or cast through `unknown` intentionally if the test only needs `data` and `isLoading`. Prefer a helper so hook mocks stay type-compatible.

---

#### #81. KeHoachDanhGia state migration updates into values blocked by the active CHECK

- **ID:** `fnd_sig-feat-library-92715499da-6927_47ecf79500`
- **Feature:** `feat_library_92715499da`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050101003-AlignTrangThaiKeHoachDanhGia.ts:23-27 (`AlignTrangThaiKeHoachDanhGia2026050101003`)`
- `packages/api/src/database/migrations/2026050101003-AlignTrangThaiKeHoachDanhGia.ts:35-47 (`AlignTrangThaiKeHoachDanhGia2026050101003.up`)`
- `packages/api/src/database/migrations/2026050101003-AlignTrangThaiKeHoachDanhGia.ts:49-55 (`AlignTrangThaiKeHoachDanhGia2026050101003.up`)`
- `packages/api/src/database/migrations/2026050101003-AlignTrangThaiKeHoachDanhGia.ts:82-88 (`AlignTrangThaiKeHoachDanhGia2026050101003.down`)`

**Giải thích:**

> The migration writes new state values while the legacy chk_khdg_trang_thai constraint is still active. Any existing row in NHAP, DA_LAP_KH, DANG_PHAN_CONG, DA_PHAN_CONG, CHO_DUYET_BC, or DA_DUYET_BC will violate the old CHECK before the migration reaches the DROP CONSTRAINT statements. The down path has the reverse problem: it reattaches the legacy CHECK without translating new values back, so rollback also fails when rows contain LAP_KE_HOACH, PHAN_CONG, CHO_DUYET_PC, THUC_HIEN, CHO_PHE_DUYET, HOAN_THANH, or BAO_CAO.

**Cách tái hiện:**

> On a database with the legacy chk_khdg_trang_thai constraint, insert ke_hoach_danh_gia(trang_thai='NHAP') and run this migration. The first UPDATE attempts to set trang_thai='LAP_KE_HOACH' and PostgreSQL rejects it with a check-constraint violation.

**Khuyến nghị fix:**

> Drop the legacy CHECK constraints before rewriting rows, then add the new CHECK after the backfill. For down(), either map every new state back to a valid legacy state before re-adding chk_khdg_trang_thai or make the rollback explicitly irreversible before mutating schema.

---

#### #82. Tổ chức tư vấn FK repointing has no legacy data migration

- **ID:** `fnd_sig-feat-library-d48fe2270b-8dee_899387c1b6`
- **Feature:** `feat_library_d48fe2270b`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050208001-CreateToChucTuVan.ts:7-16 (`CreateToChucTuVan2026050208001`)`
- `packages/api/src/database/migrations/2026050208001-CreateToChucTuVan.ts:28-79 (`CreateToChucTuVan2026050208001.up`)`
- `packages/api/src/database/migrations/2026050208001-CreateToChucTuVan.ts:111-119 (`CreateToChucTuVan2026050208001.up`)`
- `packages/api/src/database/migrations/2026050208001-CreateToChucTuVan.ts:121-134 (`CreateToChucTuVan2026050208001.up`)`

**Giải thích:**

> The migration creates an empty to_chuc_tu_van table and immediately validates existing tvv_to_chuc.to_chuc_id and tu_van_vien.to_chuc_chinh_id values against it. In any database that has rows using the documented legacy danh_muc IDs, adding either FK will fail because those IDs have not been inserted into to_chuc_tu_van. Even if a database happens to have no links, the migration contains no explicit preflight to prove that assumption.

**Khuyến nghị fix:**

> Before repointing the FKs, either migrate the referenced danh_muc organizations into to_chuc_tu_van while preserving IDs, or add a preflight that fails with a clear repair message when legacy references exist. Only add the new FKs after the referenced IDs are present.

---

#### #83. VuViec invariant migration can fail on the dirty rows it describes

- **ID:** `fnd_sig-feat-library-d519894ed5-81f2_63b8c68b09`
- **Feature:** `feat_library_d519894ed5`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/database/migrations/2026050800004-VuViecCompletedInvariant.ts:7-10 (`VuViecCompletedInvariant2026050800004`)`
- `packages/api/src/database/migrations/2026050800004-VuViecCompletedInvariant.ts:20-28 (`VuViecCompletedInvariant2026050800004.up`)`

**Giải thích:**

> PostgreSQL validates a new CHECK constraint against existing rows when it is added. The migration comment explicitly identifies existing terminal `vu_viec` rows with `ngay_hoan_thanh IS NULL`, but `up()` adds the constraint without first repairing or preflighting those rows, so databases containing the known bad data will fail the migration.

**Khuyến nghị fix:**

> Before adding the constraint, either backfill terminal rows to a defensible timestamp such as `COALESCE(ngay_hoan_thanh, ngay_cap_nhat, ngay_tao)` or run an explicit preflight that aborts with actionable row IDs. Then add the CHECK.

---

#### #84. Web release build is currently blocked by the TypeScript step

- **ID:** `fnd_sig-feat-release-1ae4c988c9-d747_fe1f9f1461`
- **Feature:** `feat_release_1ae4c988c9`
- **Confidence:** high | **Triage:** risk | **Status:** open

**Evidence (vị trí code):**

- `packages/web/package.json:7 (`scripts.build`)`

**Giải thích:**

> The build script gates the Vite production build behind a TypeScript compile step. A no-emit run of that first step for @htpldn/web exits with code 2 and reports current TypeScript errors, so the `&& vite build` step never runs and the package cannot produce release assets from this script until the typecheck surface is fixed or scoped correctly.

**Cách tái hiện:**

> Run `pnpm --filter @htpldn/web exec tsc --noEmit --pretty false`. It exits 2 with errors including missing Vitest globals in `src/utils/string-normalize.test.ts`, an incomplete `Record<KenhTiepNhanVuViec, string>` in `src/pages/vu-viec/list/columns.tsx`, and other strict type failures.

**Khuyến nghị fix:**

> Fix the reported TypeScript errors and make the build typecheck deterministic, for example by using a release tsconfig that excludes tests or includes Vitest globals where tests are intentionally typechecked. Then keep `vite build` gated on a passing typecheck.

---

### 3.6 Lệch API Contract — 3 findings

#### #85. Approval does not enforce the required TVV professional-card file gate

- **ID:** `fnd_sig-feat-library-4315226f8e-c139_9de4c54c1e`
- **Feature:** `feat_library_4315226f8e`
- **Confidence:** high | **Triage:** contract-mismatch | **Status:** open

**Evidence (vị trí code):**

- `packages/api/src/modules/chuyen-gia-tvv/dto/create-tu-van-vien.dto.regression-cgtvv-014.spec.ts:51-54 (`CreateTuVanVienDto regression CGTVV-014`)`
- `packages/api/src/modules/chuyen-gia-tvv/dto/create-tu-van-vien.dto.regression-cgtvv-014.spec.ts:64-68 (`CreateTuVanVienDto accepts deferred upload`)`
- `packages/api/src/modules/chuyen-gia-tvv/tu-van-vien.service.ts:1379-1387 (`TuVanVienService.pheDuyet`)`
- `packages/api/src/modules/chuyen-gia-tvv/tu-van-vien.service.ts:1450-1462 (`TuVanVienService.pheDuyet`)`

**Giải thích:**

> The regression test documents that DTO validation intentionally allows TVV creation without fileTheHanhNgheId because the backend workflow gate must enforce it at recognition/approval time. In pheDuyet, the service checks only state, same-unit approval, account/email setup, then sets ngayCongNhan and CHO_KICH_HOAT. There is no loaiTvv==='TVV' and fileTheHanhNgheId presence check before recognition, so a TVV can be approved without the legally required file.

**Cách tái hiện:**

> Create or update a TuVanVien with loaiTvv='TVV' and fileTheHanhNgheId=null, move it to CHO_PHE_DUYET, then POST /tu-van-viens/:id/phe-duyet with a valid version and soQuyetDinh. The service saves CHO_KICH_HOAT and ngayCongNhan without rejecting the missing file.

**Khuyến nghị fix:**

> Add a backend gate in pheDuyet before account creation/state mutation: if loaiTvv is TVV and fileTheHanhNgheId is missing, throw an SRS-coded 422/400. Ensure batchPheDuyet surfaces the per-row failure code.

---

#### #86. Draft updates call PUT while the CTDT update API is PATCH

- **ID:** `fnd_sig-feat-library-e1a669cf02-8323_871c494d64`
- **Feature:** `feat_library_e1a669cf02`
- **Confidence:** high | **Triage:** contract-mismatch | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/dao-tao/chuong-trinh/hooks/use-ctdt-queries.ts:86-93 (`useUpdateCtdt`)`
- `packages/web/src/pages/dao-tao/chuong-trinh/detail/index.tsx:116-118 (`handleFinish`)`
- `packages/api/src/modules/dao-tao/chuong-trinh-dao-tao.controller.ts:175-184 (`ChuongTrinhDaoTaoController.update`)`
- `packages/web/src/services/dao-tao/chuong-trinh-dao-tao.service.ts:154-160 (`updateCtdt`)`

**Giải thích:**

> The detail page save path goes through useUpdateCtdt, but that hook sends PUT to /chuong-trinh-dao-taos/:id. The API controller and existing service wrapper define the update operation as PATCH, so saving an existing draft via Lưu nháp will hit the wrong method and fail instead of persisting the edit.

**Khuyến nghị fix:**

> Change useUpdateCtdt to call the existing updateCtdt service wrapper or switch the hook to api.patch for the same endpoint.

---

#### #87. Inbound/write scopes cannot be assigned from the API consumer UI

- **ID:** `fnd_sig-feat-library-d818cf5cb5-da90_39311a73de`
- **Feature:** `feat_library_d818cf5cb5`
- **Confidence:** high | **Triage:** contract-mismatch | **Status:** open

**Evidence (vị trí code):**

- `packages/web/src/pages/quan-tri/api-consumer/constants.ts:1-20 (`PREDEFINED_SCOPES`)`
- `packages/web/src/pages/quan-tri/api-consumer/ConsumerFormModal.tsx:154-168 (`ConsumerFormModal`)`

**Giải thích:**

> The form uses PREDEFINED_SCOPES as the complete selectable set and the Select is plain multi-select, not tags/custom input. The current list only contains read/search scopes, so admin users cannot grant required inbound/write scopes such as the public inbound API permissions. Consumers configured through this page will be unable to call those endpoints even though the backend/API catalogue supports them.

**Khuyến nghị fix:**

> Add the missing inbound/write scopes to PREDEFINED_SCOPES or load the authoritative scope catalogue from the backend, and keep create/edit plus filtering on the same source.

---


## 4. Medium severity — Confirmed Bugs (302 findings)

Liệt kê title + file để overview. Chi tiết xem trong [`.clawpatch/reports/20260527T002749-c6f72f.md`](../source_code/.clawpatch/reports/20260527T002749-c6f72f.md).

### bug (177)

- **Merging target defaults drops repeated incoming query parameters** — `packages/web/src/components/RedirectPreservingSearch/redirect-preserving-search.tsx:23` (`fnd_sig-feat-ui-flow-2891234127-ef41_a3bfc9936d`)
- **Changing the selected report type re-runs results with the previous submitted filters** — `packages/web/src/pages/bao-cao/index.tsx:113` (`fnd_sig-feat-ui-flow-6724572bf6-de8c_2293b8eeea`)
- **Detail drawer navigation drops the list filters** — `packages/web/src/pages/tv-nhanh/kho-cau-hoi/hooks/use-kch-filters.ts:22` (`fnd_sig-feat-route-1572d21fb9-57f5be_34972d5469`)
- **VuViec assignment constraints allow assigned rows with no direct handler** — `packages/api/src/database/migrations/2026050900038-AddVuViecAssigneeV35Schema.ts:15` (`fnd_sig-feat-library-977556f978-bfc7_36a956c931`)
- **Detail drawer shows an endless skeleton on detail fetch errors** — `packages/web/src/pages/tv-nhanh/kho-cau-hoi/components/KhoCauHoiDetailDrawer.tsx:41` (`fnd_sig-feat-library-8cfc320c72-d439_f2ae49398f`)
- **UpdateDeKiemTraDto lets invalid exam shape reach persistence** — `packages/api/src/modules/dao-tao/dto/update-de-kiem-tra.dto.ts:9` (`fnd_sig-feat-library-7439eb4425-801b_3a7296cc6d`)
- **Unread count polling stops after any transient error** — `packages/web/src/components/NotificationBell/use-notification-bell.ts:27` (`fnd_sig-feat-ui-flow-c564a67961-1122_78740f5af2`)
- **denyRoles over-blocks multi-role users allowed by the sidebar contract** — `packages/web/src/components/PermissionRoute/permission-route.tsx:23` (`fnd_sig-feat-ui-flow-ee0fa88971-66a1_6462bebdf9`)
- **Clearing a column sort never notifies the parent** — `packages/web/src/components/ProTableWrapper/pro-table-wrapper.tsx:30` (`fnd_sig-feat-library-62ada3328b-60a5_4e6deb4e3c`)
- **Unread badge polling stops after a transient error** — `packages/web/src/components/NotificationBell/use-notification-bell.ts:27` (`fnd_sig-feat-library-69278b5daa-3514_d1a8edac1d`)
- **Batch delete still treats cancelled Hỏi đáp as eligible** — `packages/web/src/pages/hoi-dap/list/columns.tsx:52` (`fnd_sig-feat-library-0d6624624f-b579_a18b3e855a`)
- **Clearing optional fields in edit mode does not get persisted** — `packages/web/src/pages/bieu-mau/components/ThuMucBieuMauModal.tsx:70` (`fnd_sig-feat-ui-flow-e215dbfe90-f405_9145f2ea7d`)
- **Whitespace-only approval/rejection fields pass validation then submit empty strings** — `packages/web/src/pages/chuyen-gia-tvv/danh-sach/ModalPheDuyetHangLoat.tsx:56` (`fnd_sig-feat-library-e51849c94d-30f7_296e611f6e`)
- **Avatar dropdown trigger is mouse-only** — `packages/web/src/components/UserAvatar/user-avatar.tsx:32` (`fnd_sig-feat-ui-flow-1203cafb33-b494_5d7645d234`)
- **Detail-page delete button is rendered but inert** — `packages/web/src/pages/vu-viec/detail/index.tsx:222` (`fnd_sig-feat-library-d434ed7f1d-5e91_2499c66f5a`)
- **Toggle and delete mutations leave detail queries stale** — `packages/web/src/services/danh-muc/danh-muc.service.ts:69` (`fnd_sig-feat-library-463d709082-4382_50c47599e0`)
- **Lecture assignment modal builds options from partial pages** — `packages/web/src/pages/dao-tao/khoa-hoc/components/BaiGiangDaGanTab.tsx:51` (`fnd_sig-feat-library-ed17c37cb6-dc83_e26cc4461c`)
- **Chart bars show an empty state during initial loading** — `packages/web/src/pages/dashboard/components/ChartBar.tsx:50` (`fnd_sig-feat-library-61514462f1-1e2c_b5bd2c9555`)
- **Severe SLA tag does not render as the intended black tag** — `packages/web/src/components/SlaIndicator/sla-indicator.tsx:71` (`fnd_sig-feat-library-d4a9aa1ae1-e580_ea5f065acd`)
- **Filtered timeline can show an empty state before all visible events are loaded** — `packages/web/src/pages/vu-viec/detail/components/SectionTimeline.tsx:139` (`fnd_sig-feat-library-1587383e71-89bb_f5d93b076b`)
- **Trend line reads primary aggregate rows instead of time-series rows** — `packages/web/src/pages/bao-cao/components/charts/TrendLineChart.tsx:21` (`fnd_sig-feat-ui-flow-02e9a54db3-673f_1b4b4ff19c`)
- **Late URL initialValues never hydrate the form** — `packages/web/src/pages/bao-cao/components/ReportFilterPanel.tsx:50` (`fnd_sig-feat-ui-flow-e9746ee861-0a6b_f4b2df6f53`)
- **VNeID logins drop session IP and user-agent metadata** — `packages/api/src/modules/auth/services/vneid.service.ts:137` (`fnd_sig-feat-library-bff8b9f2f8-4963_48504b0ad5`)
- **Delayed login redirect can fire after leaving the verification page** — `packages/web/src/pages/auth/verify-email/index.tsx:22` (`fnd_sig-feat-ui-flow-19675ce472-933f_1956539cc4`)
- **Legacy edit alias redirects to the wrong doanh-nghiep id** — `packages/web/src/pages/doanh-nghiep/index.tsx:41` (`fnd_sig-feat-route-d4efd1de54-7f54d8_5ef1bda984`)
- **Training module denies users who only have permissions for tab-hosted subfeatures** — `packages/web/src/pages/dao-tao/index.tsx:36` (`fnd_sig-feat-library-6d3c3b11da-d6a0_8aeb147526`)
- **Required text fields accept whitespace-only values** — `packages/api/src/modules/nguoi-ho-tro/dto/cap-nhat-trang-thai-nht.dto.ts:25` (`fnd_sig-feat-library-594b783a37-e6db_3c70378529`)
- **VNeID login button never starts VNeID authorization** — `packages/web/src/pages/auth/login/index.tsx:217` (`fnd_sig-feat-library-a20cd4d819-3c5d_bfcba10abd`)
- **Export drops the selected complexity filter** — `packages/web/src/pages/hoi-dap/list/components/HoiDapFilterBar.tsx:46` (`fnd_sig-feat-library-0d6624624f-2cb3_f11f812056`)
- **Notification failures after the bulk update permanently drop escalation notifications** — `packages/api/src/modules/hoi-dap/queues/hoi-dap-sla-check.processor.ts:102` (`fnd_sig-feat-library-16fd9d07ce-39ab_458a0540f4`)
- **The detail route captures the DeXuat list URL as an id** — `packages/web/src/pages/dao-tao/index.tsx:117` (`fnd_sig-feat-route-b102d10823-b594f3_49ee8778b8`)
- **file_dinh_kem rollback cannot re-add the old entity_type CHECK after feature use** — `packages/api/src/database/migrations/2026052600100-AddKeHoachDanhGiaToFileEntityTypeCheck.ts:4` (`fnd_sig-feat-library-8cc0881110-c5af_f87f859870`)
- **Mock VNeID link seed is never executed by seed:run** — `packages/api/package.json:26` (`fnd_sig-feat-library-2b6a1bb952-b21e_e7e3d06e39`)
- **Clearing sort state is not reported to the parent** — `packages/web/src/components/ProTableWrapper/pro-table-wrapper.tsx:31` (`fnd_sig-feat-ui-flow-d51f315791-5b1e_507354f234`)
- **Self-loop fallback can choose a route that role guards will immediately deny** — `packages/web/src/components/PermissionRoute/denied-access.tsx:48` (`fnd_sig-feat-ui-flow-94d7211d1d-bbbb_e8b3a1f9a3`)
- **TVV owners cannot edit their own capability tab from the detail page** — `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/TabNangLuc.tsx:31` (`fnd_sig-feat-library-26e56c9ad7-a687_528622a6cb`)
- **PDF previews are marked done even when no tab opens** — `packages/web/src/components/FileViewer/FileViewerProvider.tsx:13` (`fnd_sig-feat-ui-flow-63dddca1ee-12c6_6072d62bb5`)
- **TVCS update can bypass expert-field compatibility validation** — `packages/api/src/modules/tu-van/noi-dung-tu-van-cs.service.ts:121` (`fnd_sig-feat-library-40298d2981-fdfb_340a3b6e58`)
- **Page-size changes invoke onPaginationChange twice** — `packages/web/src/components/proto/ProtoTable.tsx:31` (`fnd_sig-feat-ui-flow-7172a6cf65-4e48_8d1f5904e8`)
- **Custom date range shows an error but is not validated by the form** — `packages/web/src/pages/bao-cao/components/KyBaoCaoFilter.tsx:89` (`fnd_sig-feat-ui-flow-bd07c74edb-7694_58202f5403`)
- **Lexicographic MAX breaks after sequence 9999** — `packages/api/src/modules/tu-van/helpers/ma-tu-van.helper.ts:27` (`fnd_sig-feat-library-7e953d0413-468f_dee3d5ec97`)
- **Bulk account actions can send an empty or partial id list after pagination or data changes** — `packages/web/src/pages/quan-tri/tai-khoan/index.tsx:84` (`fnd_sig-feat-library-0354b82887-028e_9e3707ecea`)
- **`Lưu nháp` and `Gửi KQ` submit the same request** — `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/TabThamDinh.tsx:62` (`fnd_sig-feat-ui-flow-97af2fc7d8-d568_5502cbed70`)
- **Batch DTOs allow duplicate IDs, enabling duplicate side effects** — `packages/api/src/modules/hoi-dap/dto/batch-cong-khai.dto.ts:4` (`fnd_sig-feat-library-312eaefdd1-9573_f973cb2f19`)
- **FRONTEND_URL localhost guard can be bypassed by valid URL syntax** — `packages/api/src/common/assert-frontend-url.ts:15` (`fnd_sig-feat-library-989eb2a2e3-2474_e8739124ef`)
- **Standalone reporting periods are created but cannot be listed** — `packages/api/src/modules/ct-htpldn/dot-bao-cao/dot-bao-cao.entity.ts:21` (`fnd_sig-feat-library-e415d40de4-1461_e0d9b9bc4a`)
- **Malformed date props can lock the browser in an infinite business-day loop** — `packages/web/src/components/SlaIndicator/sla-indicator.tsx:20` (`fnd_sig-feat-ui-flow-cccbb4c8f5-f60b_52363dd685`)
- **Search panel filters are not fully applied to list/export requests** — `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienSearchPanel.tsx:34` (`fnd_sig-feat-ui-flow-a7907198da-fa0e_7060208684`)
- **Template lookup cannot filter by template type** — `packages/web/src/services/mau-phan-hoi.api.ts:28` (`fnd_sig-feat-library-4fbc00e032-81c1_267afb12ff`)
- **Missing callback parameters leave the VNeID page spinning forever** — `packages/web/src/pages/auth/vneid/callback/index.tsx:17` (`fnd_sig-feat-ui-flow-4faff82a25-714e_cdda038df1`)
- **Report header omits creator and falls back to raw unit IDs** — `packages/web/src/pages/bao-cao/components/ReportHeader.tsx:5` (`fnd_sig-feat-library-3ef18b4a13-34f1_bcb1e1c542`)
- **Non-positive range reservations can move the counter backward or return impossible ranges** — `packages/api/src/common/sequence/next-ma-code.helper.ts:56` (`fnd_sig-feat-library-7b7f1767aa-b6ea_6a8d14bde4`)
- **Failed document uploads leave the upload UI stuck disabled** — `packages/web/src/pages/dao-tao/bai-giang/form/BaiGiangForm.tsx:116` (`fnd_sig-feat-library-9e880477cc-978c_5454156b90`)
- **Required free-text reasons accept whitespace-only content** — `packages/api/src/modules/vu-viec/dto/gui-thong-bao.dto.ts:4` (`fnd_sig-feat-library-fddf342792-affe_5b5d34e362`)
- **Batch approval selection survives list filter and pagination changes** — `packages/web/src/pages/chi-tra/list/index.tsx:34` (`fnd_sig-feat-ui-flow-a09d850f60-da05_b0484725af`)
- **Invalid first-login tokens trigger the global logout redirect before local handling** — `packages/web/src/pages/auth/first-login-password/index.tsx:37` (`fnd_sig-feat-ui-flow-c278dbf386-704f_13b42a8b90`)
- **Secondary trend lines still read the primary breakdown rows** — `packages/web/src/pages/bao-cao/components/ReportChartRenderer.tsx:53` (`fnd_sig-feat-ui-flow-d9edef04e9-ae1f_c057022301`)
- **TABLE_OWNERS has drifted from real module table ownership** — `packages/api/src/infra/db/table-ownership.ts:1` (`fnd_sig-feat-library-94ffc9e51a-e602_c497eba89b`)
- **Publish and unpublish idempotency cache keys are not scoped to the folder** — `packages/api/src/modules/bieu-mau/thu-muc-bieu-mau.controller.ts:126` (`fnd_sig-feat-library-c4299c692e-3bda_d0b76f9d1d`)
- **Optional-field clears are omitted from update payloads** — `packages/web/src/pages/doanh-nghiep/detail/index.tsx:147` (`fnd_sig-feat-library-ab32d8be8d-ca82_1b218bbc74`)
- **Copying Feb 29 to a non-leap year creates March 1** — `packages/api/src/modules/ngay-le/ngay-le.service.ts:117` (`fnd_sig-feat-library-a68ea50ad8-66a7_4910fcd773`)
- **VNeID callback spins forever when code or state is missing** — `packages/web/src/pages/auth/vneid/callback/index.tsx:17` (`fnd_sig-feat-library-a20cd4d819-be17_f27ed3e77f`)
- **Status filter survives tab changes and overrides the selected tab** — `packages/web/src/pages/tv-nhanh/use-tvn-filters.ts:31` (`fnd_sig-feat-library-9776f0af57-e765_b8ac23523c`)
- **DeKiemTra detail route permits users who can be denied from its list return path** — `packages/web/src/pages/dao-tao/index.tsx:129` (`fnd_sig-feat-route-fe532ea944-5861d6_0f7cfccf55`)
- **Hoi dap period aggregation buckets a different date expression than the report filter** — `packages/api/src/modules/bao-cao/services/bc-hoi-dap.service.ts:137` (`fnd_sig-feat-library-5ad39280f7-5d9a_863c9f3ba0`)
- **Bulk approve is offered for rejected rows in the mixed pending tab** — `packages/web/src/pages/tv-nhanh/kho-cau-hoi/hooks/use-kch-filters.ts:62` (`fnd_sig-feat-route-1572d21fb9-c58aa6_239cd0f4fd`)
- **Video session link validation permits unusable values** — `packages/api/src/modules/tu-van/dto/create-phien-tu-van.dto.ts:18` (`fnd_sig-feat-library-af51cdc7f3-7b2e_38afc7da8d`)
- **Selected rows survive filter changes and batch approval can target hidden records** — `packages/web/src/pages/chi-tra/list/index.tsx:56` (`fnd_sig-feat-library-f1eb03ed90-7b4a_70200cf649`)
- **Virus scan status can remain stuck after the backend marks a file clean** — `packages/web/src/components/FileUpload/file-upload.tsx:140` (`fnd_sig-feat-ui-flow-4e9c2c2d4f-7467_d862fc1c0b`)
- **Ongoing-training KPI cache ignores the requested period while caching period-specific fields** — `packages/api/src/modules/dashboard/dashboard.service.ts:906` (`fnd_sig-feat-library-e0fc374753-142e_c4507a25d3`)
- **Invalid ISO timestamp dates can be normalized instead of rejected** — `packages/api/src/common/utils/date.util.ts:25` (`fnd_sig-feat-library-16211c48c4-714f_0c4b43ea7b`)
- **URL pagination is applied to fetches but not to the table pager** — `packages/web/src/hooks/use-pagination-params.ts:13` (`fnd_sig-feat-ui-flow-a7907198da-6fd5_2f2aa7c0fc`)
- **Non-decomposable check rejects snake-action permission codes that the audit otherwise accepts** — `scripts/permission-audit.mjs:189` (`fnd_sig-feat-library-710c9f5545-7b24_ac0a71117d`)
- **Processed congKhai=false query is coerced to true** — `packages/api/src/modules/hoi-dap/dto/processed-hoi-dap-list-query.dto.ts:16` (`fnd_sig-feat-library-8e4b50b2a3-4fba_04552bd03c`)
- **Blank quick-consultation answers pass validation** — `packages/api/src/modules/tu-van/dto/tra-loi-tu-van-nhanh.dto.ts:5` (`fnd_sig-feat-library-f79f52fbee-0f16_f247d08b4a`)
- **Rendered filters are not propagated into list/export queries** — `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienSearchPanel.tsx:34` (`fnd_sig-feat-library-e51849c94d-ca10_5d8923ab4a`)
- **Public first-login password failures can trigger the global logout redirect** — `packages/web/src/pages/auth/login/index.tsx:135` (`fnd_sig-feat-ui-flow-eb7ca14d1e-1a89_f367c53767`)
- **Date-only period boundaries shift with host timezone** — `packages/api/src/modules/bao-cao/utils/generate-periods.util.ts:16` (`fnd_sig-feat-library-e66ddf62f0-5abc_6c89179af2`)
- **Vu-viec terminal-state fixtures skip workflow-required child rows** — `packages/api/src/database/seeds/__qa__/vu-viec-qa-fixtures.seed.ts:15` (`fnd_sig-feat-library-7ea88dbfd9-bd84_0c1a4f27c9`)
- **Base URL validation allows configurations that corrupt every appended endpoint path** — `packages/api/src/modules/common/services/cong-plqg.client.ts:84` (`fnd_sig-feat-library-1b2549ebec-836b_8bd46617fb`)
- **Contract value can be lowered below scheduled payments** — `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.service.ts:303` (`fnd_sig-feat-library-f72aa3f50c-38e8_7f826156f6`)
- **Imported attendance leaves cached results stale** — `packages/web/src/pages/dao-tao/khoa-hoc/hooks/use-khoa-hoc-queries.ts:65` (`fnd_sig-feat-library-6298469036-20ab_a7a17ff856`)
- **Hoàn thành blocks legal-advice results above 1000 characters** — `packages/web/src/pages/tv-chuyen-sau/detail/index.tsx:363` (`fnd_sig-feat-library-8914d6caba-0388_fcd4e92477`)
- **Rejected async action callbacks become unhandled promises** — `packages/web/src/components/ApprovalActions/approval-actions.tsx:81` (`fnd_sig-feat-library-37a8ba827a-7e9c_7da89f734d`)
- **Phân tích vụ việc totals include statuses that no visible bucket counts** — `packages/api/src/modules/bao-cao/services/bc-vu-viec-phan-tich.service.ts:67` (`fnd_sig-feat-library-2134992159-4d85_6b5aab907c`)
- **Attendance import can skip recomputation for valid rows from a partially invalid learner** — `packages/api/src/modules/dao-tao/diem-danh.service.ts:300` (`fnd_sig-feat-library-017b22193d-4a51_5029109a06`)
- **Payment amount parser lets NaN pass validation** — `packages/web/src/pages/chi-tra/detail/forms/ThanhToanForm.tsx:98` (`fnd_sig-feat-library-98701b2752-377a_53c4bca344`)
- **Whitespace-only reasons can pass validation and be submitted** — `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/ModalCapNhatTrangThai.tsx:26` (`fnd_sig-feat-ui-flow-d9cb1a864c-4148_9a6527f4d3`)
- **Bulk delete bypasses the same state guard as row delete** — `packages/web/src/pages/vu-viec/list/columns.tsx:34` (`fnd_sig-feat-library-a6ef7af5da-da7b_83f91329a0`)
- **Detail child tables truncate data after the first 100 rows** — `packages/web/src/pages/doanh-nghiep/detail/HoSoChiTraTab.tsx:34` (`fnd_sig-feat-library-ab32d8be8d-4800_3603c0f7d0`)
- **Assignment mode switches can submit a stale TVV account as a personal assignee** — `packages/web/src/pages/hoi-dap/detail/components/PhanCongModal.tsx:98` (`fnd_sig-feat-library-db7c9e6d6a-feb1_4f3555b338`)
- **Company code generation can collide after hard deletes** — `packages/api/src/modules/doanh-nghiep/doanh-nghiep.service.ts:347` (`fnd_sig-feat-library-95396f72d7-a7ac_f0d015e5df`)
- **Whitespace-only rejection reason can pass client validation** — `packages/web/src/pages/chi-tra/detail/forms/ThamDinhForm.tsx:51` (`fnd_sig-feat-ui-flow-ae7db0d7fb-0a37_99a1c6b731`)
- **Fixture silently continues when privilege escalation fails** — `packages/api/scripts/bug-008-fixture.ts:6` (`fnd_sig-feat-library-e268df9eb8-125e_bf193f4d10`)
- **Transient outbox failures can exhaust all retries in one drain call** — `packages/api/src/modules/dao-tao/tich-hop-outbox.service.ts:53` (`fnd_sig-feat-library-e2c8c8bb98-d65f_efc002879b`)
- **Export can use form values that do not match the displayed report** — `packages/web/src/pages/bao-cao/components/ReportFilterPanel.tsx:70` (`fnd_sig-feat-library-3ef18b4a13-328f_c981ce33fb`)
- **Changing report type keeps the previous executed filters/result state active** — `packages/web/src/pages/bao-cao/index.tsx:83` (`fnd_sig-feat-library-840d44d989-965f_68f32d6321`)
- **Whitespace CHECK constraints only trim spaces** — `packages/api/src/database/migrations/2026050203000-CheckConstraintsPreflight.ts:117` (`fnd_sig-feat-library-26ba3911c8-3bf4_6ee042e0d0`)
- **Manual supplement timeout and auto-reject cutoff disagree** — `packages/api/src/modules/vu-viec/vu-viec.service.ts:103` (`fnd_sig-feat-library-4879d8b29e-26fe_fc98ce0210`)
- **Existing answer is hidden in CB_TRA_LOI detail mode** — `packages/web/src/pages/tv-nhanh/detail/index.tsx:77` (`fnd_sig-feat-library-599bb3f4ae-a5aa_0ad0950d98`)
- **Legacy edit alias drops the business id during redirect** — `packages/web/src/pages/doanh-nghiep/index.tsx:73` (`fnd_sig-feat-route-62a6007182-2e747f_c4faaadb74`)
- **`laCongBo=false` is coerced to `true` during DTO transformation** — `packages/api/src/modules/ct-htpldn/dto/chuong-trinh-htpl-list-query.dto.ts:15` (`fnd_sig-feat-library-89bc5ad47b-0288_27961cba13`)
- **Status-changing detail mutations leave list/tab caches stale** — `packages/web/src/pages/chi-tra/detail/use-ho-so-chi-tra-detail.ts:107` (`fnd_sig-feat-library-98701b2752-21aa_eed150d408`)
- **Registration close date rejects the same-day range that the DTO documents as valid** — `packages/api/src/modules/dao-tao/dto/create-khoa-hoc.dto.ts:98` (`fnd_sig-feat-library-de78a76c36-6292_0584694fa8`)
- **Deep-linked URL filters are missed by the form after the catalog loads** — `packages/web/src/pages/bao-cao/index.tsx:70` (`fnd_sig-feat-ui-flow-6724572bf6-6448_cc10f4771b`)
- **Edit modal can submit a create before edit detail loads** — `packages/web/src/pages/bieu-mau/ThuMucBieuMauPage.tsx:93` (`fnd_sig-feat-ui-flow-194f7950f9-2f88_fd5ef70973`)
- **Required reason fields accept blank whitespace** — `packages/web/src/pages/chi-tra/detail/forms/PheDuyetActions.tsx:50` (`fnd_sig-feat-ui-flow-4db3a070c1-5d26_e27a536c39`)
- **Trạng thái filter conflicts with the tab-owned status** — `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienSearchPanel.tsx:39` (`fnd_sig-feat-ui-flow-df660fbcc5-f31c_0ae9f2197d`)
- **custom-multi controls are not connected to SearchPanel form state** — `packages/web/src/components/SearchPanel/search-panel.tsx:60` (`fnd_sig-feat-library-f97ffb374b-0148_8db9b0a761`)
- **Count label rendering drops zero counts and does not match the tested text contract** — `packages/web/src/components/StateTabs/state-tabs.tsx:115` (`fnd_sig-feat-ui-flow-91e70e2f57-31b6_3ab35d5190`)
- **Holiday matching mixes local weekdays with UTC date keys** — `packages/api/src/modules/chi-tra/helpers/sla.helper.ts:8` (`fnd_sig-feat-library-c992ecf2a8-fd0e_00b58a4d0e`)
- **Bài giảng list duplicates rows for multi-lĩnh-vực records** — `packages/api/src/modules/api-public/services/bai-giang-public.service.ts:42` (`fnd_sig-feat-library-10582b7f1a-e9be_4b8a272da8`)
- **TW-approved aggregation candidates are rendered but cannot be selected** — `packages/web/src/pages/ct-htpldn/tong-hop/index.tsx:24` (`fnd_sig-feat-library-258eb93915-630f_5e0f389053`)
- **Whitespace-only rejection and supplement reasons pass validation** — `packages/web/src/components/ApprovalActions/approval-actions.tsx:162` (`fnd_sig-feat-library-37a8ba827a-7ad0_4798101711`)
- **Several public FTS queries are accent-sensitive** — `packages/api/src/modules/api-public/services/bieu-mau-public.service.ts:103` (`fnd_sig-feat-library-10582b7f1a-cbb3_f92464ad71`)
- **CASL tab visibility stays stale after ability rules update** — `packages/web/src/pages/quan-tri/cau-hinh/index.tsx:72` (`fnd_sig-feat-library-0f189e08e7-00c4_f4568441de`)
- **Owner editing of the Năng lực tab is broken from the detail page** — `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/index.tsx:49` (`fnd_sig-feat-ui-flow-35dfe36261-cee2_4c0c132811`)
- **KhoCauHoi code generation reuses existing codes after hard delete** — `packages/api/src/modules/tu-van/kho-cau-hoi.service.ts:98` (`fnd_sig-feat-library-40298d2981-9ed3_2f16e5d84a`)
- **Count labels do not match the StateTabs rendering contract** — `packages/web/src/components/StateTabs/state-tabs.tsx:115` (`fnd_sig-feat-library-8a3b83ee7a-9bc5_090b19b5e4`)
- **Extension allow-list rejects valid files when the browser omits MIME type** — `packages/web/src/components/FileUpload/file-upload.tsx:64` (`fnd_sig-feat-library-3f5bb5da44-595d_a05572e5a3`)
- **Mandatory reason fields accept whitespace-only input** — `packages/web/src/pages/chi-tra/detail/forms/PheDuyetActions.tsx:50` (`fnd_sig-feat-library-98701b2752-6ea2_8c98d7d8a7`)
- **Status tabs can keep a stale explicit status filter** — `packages/web/src/pages/tv-nhanh/list/index.tsx:34` (`fnd_sig-feat-library-8e31e6e638-c944_9e6589c0c9`)
- **Admin session management panel is unreachable from the account detail page** — `packages/web/src/pages/quan-tri/tai-khoan/[id]/components/SessionsPanel.tsx:22` (`fnd_sig-feat-library-0354b82887-aa3a_a363b3a259`)
- **Header omits the required creator field when nguoiTao is not supplied** — `packages/web/src/pages/bao-cao/components/ReportHeader.tsx:5` (`fnd_sig-feat-ui-flow-b9b7c8d0d7-d598_b42803466e`)
- **SET NULL delete actions are applied to non-null actor columns** — `packages/api/src/database/migrations/1744000000014-CreateHopDongBieuMau.ts:132` (`fnd_sig-feat-library-147f63b418-098a_3246d8d31a`)
- **Authz audit treats every Action.Manage requirement as non-orphan** — `packages/api/src/scripts/authz-audit.ts:396` (`fnd_sig-feat-library-ff6714dae5-6bc4_c49a52aa6d`)
- **Subtable silently hides biểu mẫu after the first page** — `packages/web/src/pages/bieu-mau/components/BieuMauSubTable.tsx:17` (`fnd_sig-feat-ui-flow-818817ecb7-a3e7_0fc3579cca`)
- **KCH backfill counts existing QA codes under a prefix that never joins** — `packages/api/src/database/migrations/2026051100250-BackfillKchTuDongForApprovedHoiDap.ts:58` (`fnd_sig-feat-library-4a3c8e7bf3-2965_1d134a21ec`)
- **Create/update errors are handled twice** — `packages/web/src/services/thu-muc-bieu-mau/thu-muc-bieu-mau.service.ts:188` (`fnd_sig-feat-ui-flow-e215dbfe90-8218_326af8d1e5`)
- **Turning public mode off does not clear the saved public description** — `packages/web/src/pages/bieu-mau/BieuMauForm.tsx:117` (`fnd_sig-feat-ui-flow-3211a8344c-da50_0886c99496`)
- **User account dropdown is mouse-only** — `packages/web/src/layouts/main-layout.tsx:514` (`fnd_sig-feat-library-841aa7e2b0-1971_9f7b34245a`)
- **Missing /hoi-dap/tao-moi alias still falls into the detail route** — `packages/web/src/routes/router.tsx:101` (`fnd_sig-feat-library-0f8a9f8dc8-d3f2_d486e68a76`)
- **Optional fields cannot be cleared in edit mode** — `packages/web/src/pages/quan-tri/tieu-chi-danh-gia/components/TieuChiForm.tsx:29` (`fnd_sig-feat-library-f1bdfd05d6-5c88_03ac1b0d99`)
- **Chart auto-detection drops valid report series for several bao-cao payload shapes** — `packages/web/src/pages/bao-cao/components/charts/TrendLineChart.tsx:21` (`fnd_sig-feat-library-23000349fb-e0eb_d023172dd1`)
- **Radar scale ignores the maximum score** — `packages/web/src/pages/bao-cao/components/charts/RadarChartView.tsx:35` (`fnd_sig-feat-ui-flow-c8d4541c2a-4e51_f2c7779c7d`)
- **Edit mode can fall through to the create mutation when detail data is missing** — `packages/web/src/pages/bieu-mau/BieuMauForm.tsx:101` (`fnd_sig-feat-ui-flow-3211a8344c-04c6_f28d6c30f0`)
- **Bulk approve can submit rejected rows from the Chờ duyệt tab** — `packages/web/src/pages/tv-nhanh/kho-cau-hoi/hooks/use-kch-filters.ts:62` (`fnd_sig-feat-library-8cfc320c72-e8e6_49e1b29ef0`)
- **Detail view omits the saved plan content field** — `packages/web/src/pages/dao-tao/ke-hoach/form/KeHoachDaoTaoForm.tsx:201` (`fnd_sig-feat-library-c7e9ed440b-aef4_b38b496d20`)
- **Checklist length check allows duplicate checklist items** — `packages/api/src/modules/vu-viec/dto/kiem-tra-vu-viec.dto.ts:14` (`fnd_sig-feat-library-fddf342792-12a5_fe5f593d19`)
- **Notification recipient SET NULL violates contact check** — `packages/api/src/database/migrations/1744000000005-CreateSystemConfig.ts:79` (`fnd_sig-feat-library-eb23e70db4-25b8_75ce140c6e`)
- **Malformed row arrays can crash SimpleBarChart instead of showing the empty state** — `packages/web/src/pages/bao-cao/components/charts/SimpleBarChart.tsx:29` (`fnd_sig-feat-ui-flow-580d3bf6a2-78a3_050b873b67`)
- **Audit export downloads the same blob twice** — `packages/web/src/pages/quan-tri/audit-log/index.tsx:209` (`fnd_sig-feat-library-6a49b33973-b824_9d059c22c0`)
- **ISO week labels use calendar year instead of ISO week-year** — `packages/api/src/modules/bao-cao/utils/generate-periods.util.ts:38` (`fnd_sig-feat-library-e66ddf62f0-d4a5_8db67f258d`)
- **cleanup-demo-garbage exits successfully after an abort condition** — `packages/api/src/scripts/cleanup-demo-garbage.ts:110` (`fnd_sig-feat-library-ff6714dae5-9e16_1359a64eef`)
- **Request QueryRunner can be leaked when transaction setup or commit fails** — `packages/api/src/common/rls/rls-context.interceptor.ts:67` (`fnd_sig-feat-library-fe01083dbe-225f_cab8ddee48`)
- **Bulk folder actions operate only on selected rows still present on the current page** — `packages/web/src/pages/bieu-mau/ThuMucBieuMauPage.tsx:128` (`fnd_sig-feat-library-654c5151cb-90b4_d6875e49da`)
- **`hieuLuc=false` query is coerced to `true`** — `packages/api/src/modules/tu-van/dto/kho-cau-hoi-list-query.dto.ts:24` (`fnd_sig-feat-library-9bde4a0f5f-69cd_916afc1e8a`)
- **Manual audit inserts are not suppressed, so successful endpoints double-log** — `packages/api/src/modules/ct-htpldn/bao-cao-ct-htpl/bao-cao-ct-htpl.controller.ts:26` (`fnd_sig-feat-library-b89215dbad-d182_875e224465`)
- **January reporting deadlines for the current year are skipped** — `packages/web/src/pages/ct-htpldn/components/DeadlineInfoBox.tsx:15` (`fnd_sig-feat-library-3d659a4ab9-1042_68214a8971`)
- **Report header never receives required creator or human unit label** — `packages/web/src/pages/bao-cao/components/ReportHeader.tsx:5` (`fnd_sig-feat-ui-flow-d72455dc9b-46b9_cd0b214578`)
- **Rejected uploads leak Multer temp files before service cleanup runs** — `packages/api/src/modules/file/pipes/file-validation.pipe.ts:51` (`fnd_sig-feat-library-8b822a2346-88df_a496476dc3`)
- **Create page can preassign a consultant outside the CG and lĩnh vực constraints** — `packages/web/src/pages/tv-chuyen-sau/tao-moi/index.tsx:106` (`fnd_sig-feat-library-8914d6caba-f0a4_a900814974`)
- **Direct URLs bypass the danh-muc tab allowlist** — `packages/web/src/pages/quan-tri/danh-muc/index.tsx:33` (`fnd_sig-feat-library-f129b296cc-c1ad_9af92ed45c`)
- **Bulk actions use current-page rows while selection count keeps stale keys** — `packages/web/src/pages/bieu-mau/ThuMucBieuMauPage.tsx:124` (`fnd_sig-feat-ui-flow-194f7950f9-dc1e_ce060d6104`)
- **Time-series vụ việc report can render rows with zero table columns** — `packages/web/src/pages/bao-cao/components/ReportResultView.tsx:90` (`fnd_sig-feat-ui-flow-d72455dc9b-97de_9c8f628fbf`)
- **Missing hoSoJson bypasses DVC intake validation** — `packages/api/src/modules/chi-tra/dto/tiep-nhan-dvc.dto.ts:12` (`fnd_sig-feat-library-bd84c54d5e-d384_f2c39fdd74`)
- **Approval defaults ignore the thẩm định proposal amount** — `packages/web/src/pages/chi-tra/detail/forms/ThamDinhForm.tsx:34` (`fnd_sig-feat-ui-flow-4db3a070c1-ee97_af3136b447`)
- **Attendance cannot be created for a selected date that is absent from returned records** — `packages/web/src/pages/dao-tao/khoa-hoc/tabs/LichHocDiemDanhTab.tsx:20` (`fnd_sig-feat-library-8b8d72555b-44dd_99271cc387`)
- **BUG-008 fixture inserts assigned vu_viec rows without the current assignee mirror columns** — `packages/api/scripts/bug-008-fixture.ts:134` (`fnd_sig-feat-library-e268df9eb8-2e0a_cbd361267f`)
- **OIDC discovery failures still mark the strategy ready with guessed endpoints** — `packages/api/src/modules/auth/strategies/vneid.strategy.ts:29` (`fnd_sig-feat-library-5757cf68a0-790f_87210761ee`)
- **Legacy edit alias drops the enterprise id** — `packages/web/src/pages/doanh-nghiep/index.tsx:41` (`fnd_sig-feat-route-446dcb8e70-0a3216_676a7a3ef0`)
- **Existing public TLPL rows are migrated to private** — `packages/api/src/database/migrations/2026050800001-AddCongKhaiContentColumnsTlpl.ts:11` (`fnd_sig-feat-library-d519894ed5-1534_6f1b6db5ee`)
- **Lowering total employees bypasses merged subcount validation** — `packages/api/src/modules/doanh-nghiep/doanh-nghiep.service.ts:246` (`fnd_sig-feat-library-95396f72d7-070c_0aa6abbe37`)
- **Create DTOs accept negative size and duration values** — `packages/api/src/modules/dao-tao/dto/create-bai-giang.dto.ts:34` (`fnd_sig-feat-library-47ccc7b3b9-aebf_ad6d453b5b`)
- **Rejected transition callbacks become unhandled promise rejections** — `packages/web/src/components/ApprovalActions/approval-actions.tsx:81` (`fnd_sig-feat-ui-flow-9879dfac3b-d014_24552117d1`)
- **Create-only GiangVien users are blocked by the parent dao-tao route guard** — `packages/web/src/pages/dao-tao/index.tsx:171` (`fnd_sig-feat-route-6b51d94be6-a2d7a1_040ac4854b`)
- **KetQua Excel import does not transition imported scores to DA_NHAP** — `packages/api/src/modules/dao-tao/ket-qua-dao-tao.service.ts:124` (`fnd_sig-feat-library-017b22193d-d5e4_7c68b02b0d`)
- **Tab counts ignore the doanhNghiepId filter used by the list query** — `packages/api/src/modules/chi-tra/chi-tra.service.ts:178` (`fnd_sig-feat-library-4b3e6cdceb-02ae_8fe9650f6e`)
- **String false can submit a draft response** — `packages/api/src/modules/hoi-dap/dto/update-phan-hoi.dto.ts:18` (`fnd_sig-feat-library-f52d371609-c134_d99612935c`)
- **Whitespace-only criterion names pass modal validation as empty names** — `packages/web/src/pages/danh-gia/ke-hoach/components/AddTieuChiModal.tsx:27` (`fnd_sig-feat-library-51d79f2ea7-335d_7b3ebee2a7`)
- **SLA calculation can skip holidays outside the start year and following year** — `packages/api/src/modules/sla/sla-calculator.service.ts:41` (`fnd_sig-feat-library-b0d83a0675-5706_1e50df7237`)
- **PhienTuVan create sends notifications to tu_van_vien id instead of tai_khoan recipient id** — `packages/api/src/modules/tu-van/phien-tu-van.service.ts:194` (`fnd_sig-feat-library-205015f24e-bc9b_c31dbc87fd`)
- **Network failures are rendered as an empty catalog** — `packages/web/src/components/LinhVucKinhDoanhSelect/index.tsx:62` (`fnd_sig-feat-ui-flow-36ad0689a9-5f61_60f8945d39`)
- **Server-driven pagination state is not forwarded to the table control** — `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienTable.tsx:36` (`fnd_sig-feat-ui-flow-8bdcbec39a-e2f5_029a3d03b6`)
- **Deep-linked filters are displayed but not applied to the list query** — `packages/web/src/pages/hoi-dap/da-xu-ly/index.tsx:12` (`fnd_sig-feat-library-1e752cac43-259e_12ce0f92bd`)
- **URL pagination is used for fetching but not bound back to the table** — `packages/web/src/pages/quan-tri/danh-muc/components/DanhMucTable.tsx:55` (`fnd_sig-feat-library-d8bcb61367-7f1b_3680347bb1`)
- **Completed-training trend reports annual requests as monthly buckets** — `packages/api/src/modules/bao-cao/services/bc-lop-dao-tao-da-dien-ra.service.ts:31` (`fnd_sig-feat-library-2134992159-78b4_105abd350a`)

### security (46)

- **Course CTDT validation is unscoped and weaker on update** — `packages/api/src/modules/dao-tao/khoa-hoc.service.ts:126` (`fnd_sig-feat-library-22ade395f2-1507_0906695bb3`)
- **Enterprise registration always submits a fake CAPTCHA token** — `packages/web/src/pages/auth/register/doanh-nghiep.tsx:173` (`fnd_sig-feat-library-a20cd4d819-9071_ebb79d0699`)
- **Read-only users can reach mutation controls from the detail route** — `packages/web/src/pages/danh-gia/index.tsx:35` (`fnd_sig-feat-route-ec3a19cf75-a7d5fe_ab01bd39c1`)
- **Internal service token is part of the persisted queue payload** — `packages/api/src/modules/chi-tra/jobs/dvc-notification.job.ts:5` (`fnd_sig-feat-library-93ddbbdae4-596e_cc7ff07c80`)
- **JWT rotation grace key is configured in tests but ignored by runtime config** — `packages/api/src/config/jwt.config.ts:11` (`fnd_sig-feat-service-e9ea9e670d-44b8_3afa168162`)
- **History statistics ignore the own-history authorization filter** — `packages/api/src/modules/chuyen-gia-tvv/services/lich-su-ho-tro-tvv.service.ts:45` (`fnd_sig-feat-library-9bb5d898e6-0ddf_db11cc5743`)
- **Virus-flagged documents still expose a download action** — `packages/web/src/pages/vu-viec/detail/components/SectionTaiLieu.tsx:19` (`fnd_sig-feat-library-1587383e71-cf8b_84e477bd75`)
- **Unvalidated sortBy is interpolated into the ORDER BY expression** — `packages/api/src/modules/notification/notification.controller.ts:43` (`fnd_sig-feat-library-55493e8ef2-c7f4_dc351d7f79`)
- **Clearing key or certificate fields omits them from PATCH, leaving old credentials active** — `packages/web/src/pages/quan-tri/api-consumer/ConsumerFormModal.tsx:37` (`fnd_sig-feat-library-d818cf5cb5-6bb2_037c18b7b3`)
- **Audit scrubbing can leak deep secrets and corrupt non-plain values** — `packages/api/src/common/services/audit.service.ts:40` (`fnd_sig-feat-library-132c0ddff1-c3ed_05e07b7647`)
- **CTDT creation validates parent training plan through an unscoped raw query** — `packages/api/src/modules/dao-tao/chuong-trinh-dao-tao.service.ts:222` (`fnd_sig-feat-library-23dc27379d-6d1b_40b9ca504a`)
- **Callback response still models and caches an access token in the SPA** — `packages/web/src/services/auth/vneid.service.ts:10` (`fnd_sig-feat-ui-flow-4faff82a25-8f26_419b9f9a3b`)
- **Approval entrypoints enforce different permission predicates** — `packages/web/src/pages/chuyen-gia-tvv/to-chuc/detail.tsx:134` (`fnd_sig-feat-library-2b550d51cd-aa74_a2bdc73ed0`)
- **generateRandomPassword accepts non-finite lengths and can violate the password policy** — `packages/shared/src/utils/password-policy.ts:59` (`fnd_sig-feat-library-92b7b8923f-5974_9d5470dd66`)
- **Upload type validation accepts mismatched and spoofed file types** — `packages/api/src/modules/dao-tao/pipes/bai-giang-file-validation.pipe.ts:5` (`fnd_sig-feat-library-cc670ea1fe-7611_7cce8beb6b`)
- **Delete and publish batch actions bypass CASL UI gating** — `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienTable.tsx:48` (`fnd_sig-feat-library-e51849c94d-170e_ee96b6dc06`)
- **Cong-khai file preview accepts unrelated orphan file IDs** — `packages/api/src/modules/chuyen-gia-tvv/controllers/tu-van-vien-cong-khai.controller.ts:87` (`fnd_sig-feat-library-acac522380-d792_2903b7bd77`)
- **QTHT read-only subjects still allow non-CRUD workflow actions** — `packages/api/src/common/casl/ability.factory.ts:48` (`fnd_sig-feat-library-42fb89e7c8-bda5_491a05a22e`)
- **Draft action bar ignores update, submit, and cancel permissions** — `packages/web/src/pages/dao-tao/chuong-trinh/detail/index.tsx:146` (`fnd_sig-feat-library-e1a669cf02-85d3_ca14a84ea2`)
- **Email activation treats inactive role mappings as provisioning** — `packages/api/src/modules/auth/auth.service.ts:539` (`fnd_sig-feat-library-bb39f9f67c-2265_1be07e0180`)
- **Export endpoint checks read permission instead of export permission** — `packages/api/src/modules/ct-htpldn/chuong-trinh-htpl.controller.ts:64` (`fnd_sig-feat-library-49045a8908-7631_db25da28c5`)
- **Batch delete is exposed without CASL delete permission** — `packages/web/src/pages/danh-gia/ke-hoach/list/index.tsx:111` (`fnd_sig-feat-library-08cbbfd1e6-f8ed_682e0e7323`)
- **Attachment uploads ignore CASL update permission** — `packages/web/src/pages/danh-gia/ke-hoach/detail/index.tsx:107` (`fnd_sig-feat-library-e8bf756a55-cf40_e73c74654f`)
- **Read-only doanh nghiệp route exposes write controls** — `packages/web/src/pages/doanh-nghiep/index.tsx:77` (`fnd_sig-feat-library-ab32d8be8d-c458_745cd6885a`)
- **Batch publish actions are exposed without a publish permission check** — `packages/web/src/pages/chuyen-gia-tvv/danh-sach/index.tsx:17` (`fnd_sig-feat-ui-flow-a7907198da-8ecf_db26a8886f`)
- **KhoCauHoi import size limit is enforced only after upload buffering** — `packages/api/src/modules/tu-van/kho-cau-hoi.controller.ts:77` (`fnd_sig-feat-library-40298d2981-897b_4c0f869161`)
- **Export bypasses accordion-only context gating** — `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.controller.ts:59` (`fnd_sig-feat-library-f72aa3f50c-cbfd_b9e31eb6ac`)
- **Resume omits the same cross-unit guard used by pause** — `packages/api/src/modules/ct-htpldn/chuong-trinh-htpl.controller.ts:246` (`fnd_sig-feat-library-49045a8908-f2d4_3cdace420e`)
- **DeXuat tab is protected by the ChuongTrinh permission instead of DeXuat permission** — `packages/web/src/pages/dao-tao/index.tsx:38` (`fnd_sig-feat-route-30a667b969-6f5be4_6e44d3d4ed`)
- **Authenticated in-memory sessions are not revalidated by the guard** — `packages/web/src/components/AuthGuard/auth-guard.tsx:17` (`fnd_sig-feat-library-17e85c2e9e-a0c2_f416e2e181`)
- **Denied actions stay enabled when the child explicitly passes disabled={false}** — `packages/web/src/components/PermissionAction/permission-action.tsx:48` (`fnd_sig-feat-library-97dbdef48a-ab1f_960988329e`)
- **Authorization submit accepts and redirects to any redirect_uri** — `packages/api/src/modules/auth/mock-vneid/mock-vneid.controller.ts:96` (`fnd_sig-feat-library-4afe3e2a5d-85ef_8ccca51eec`)
- **Consumer expiry accepted by DTO is not persisted or enforced** — `packages/api/src/modules/api-public/dto/create-api-consumer.dto.ts:56` (`fnd_sig-feat-library-867723febc-4c51_d05b211580`)
- **DN self-submit permission opens the staff-only manual intake route** — `packages/web/src/pages/vu-viec/index.tsx:38` (`fnd_sig-feat-library-8a0f990586-7589_0e5171b9da`)
- **Edit and delete actions are gated by create permission** — `packages/web/src/pages/quan-tri/ngay-le/index.tsx:31` (`fnd_sig-feat-library-29b20f4ee9-6fa6_b8307f5c2b`)
- **Read-only detail route can render and submit the edit form** — `packages/web/src/pages/ct-htpldn/index.tsx:79` (`fnd_sig-feat-library-8413aae896-e65b_737341bf89`)
- **Read-only route renders the edit-only doanh nghiệp form** — `packages/web/src/pages/doanh-nghiep/index.tsx:65` (`fnd_sig-feat-route-81e80d4926-c92224_2236c0468b`)
- **Virus scan terminal states are not reliably applied to uploaded files** — `packages/web/src/components/FileUpload/file-upload.tsx:32` (`fnd_sig-feat-library-3f5bb5da44-1105_e16e6229ff`)
- **Rating list bypasses the parent TVV tenant check** — `packages/api/src/modules/chuyen-gia-tvv/controllers/danh-gia-tu-van-vien.controller.ts:47` (`fnd_sig-feat-library-acac522380-cc05_06af12a458`)
- **TCTV publish sends before sanitizing or persisting the public description** — `packages/api/src/modules/chuyen-gia-tvv/services/to-chuc-tu-van.service.ts:584` (`fnd_sig-feat-library-9bb5d898e6-c98d_a7f144b7b9`)
- **Assignment guard never checks expert assignments** — `packages/api/src/common/subscribers/rls.subscriber.ts:125` (`fnd_sig-feat-library-c3f5112c70-0237_496bd852b0`)
- **Test distribution persists arbitrary lesson IDs without validation** — `packages/api/src/modules/dao-tao/de-kiem-tra.service.ts:472` (`fnd_sig-feat-library-23dc27379d-5bd2_4dc98d47c6`)
- **AuthGuard renders protected routes from unverified localStorage state** — `packages/web/src/components/AuthGuard/auth-guard.tsx:12` (`fnd_sig-feat-ui-flow-2fa116db0c-7a89_776a6be7dc`)
- **Database SSL disables certificate verification whenever enabled** — `packages/api/src/config/database.config.ts:27` (`fnd_sig-feat-service-e9ea9e670d-85f5_d5e966f0a1`)
- **Logout treats failed server revocation as success** — `packages/web/src/store/auth.store.ts:49` (`fnd_sig-feat-service-791e3e7577-3de5_fd390f1521`)
- **Publish and delete mutations are exposed without CASL gates** — `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienTable.tsx:65` (`fnd_sig-feat-ui-flow-8bdcbec39a-350f_0581a77b54`)

### data-loss (41)

- **Trao-doi attachment link failures are silently swallowed** — `packages/api/src/modules/tu-van/lich-su-trao-doi-tv.service.ts:154` (`fnd_sig-feat-library-40298d2981-6af7_7c02730f70`)
- **Unsaved-change guard is bypassed by SPA navigation** — `packages/web/src/pages/ct-htpldn/detail/index.tsx:113` (`fnd_sig-feat-library-71b15c1e71-f39f_cb97b3d588`)
- **Changing a parent unit's cap can corrupt existing child hierarchy** — `packages/api/src/modules/quan-tri/don-vi/don-vi.service.ts:194` (`fnd_sig-feat-library-707dcd8fba-42ea_f8a1120f0e`)
- **Audit failures are still only logged, never enqueued to the DLQ** — `packages/api/src/common/services/audit-log-dlq.service.ts:11` (`fnd_sig-feat-library-132c0ddff1-5fb5_b4d6c765fe`)
- **Draft report edits can be submitted or overwritten without being saved** — `packages/web/src/pages/ct-htpldn/dot-bao-cao/components/Form21aTable.tsx:31` (`fnd_sig-feat-library-fe644110a5-373c_2f756d0889`)
- **Voided records remain editable and deletable from the list** — `packages/web/src/pages/chuyen-gia-tvv/to-chuc/detail.tsx:235` (`fnd_sig-feat-library-2b550d51cd-13c7_39297613ad`)
- **Delete dependency check fails open on query errors** — `packages/api/src/modules/ct-htpldn/chuong-trinh-htpl.service.ts:366` (`fnd_sig-feat-library-49045a8908-b057_32b1cf8bff`)
- **Rollback can move untouched seeded accounts to BTP-TW** — `packages/api/src/database/migrations/1744000000019-CleanupGiangVienAndFixNht.ts:38` (`fnd_sig-feat-library-147f63b418-b1c6_0cf71ba901`)
- **Removed attendance import file can still be submitted** — `packages/web/src/pages/dao-tao/khoa-hoc/components/ImportDiemDanhModal.tsx:34` (`fnd_sig-feat-library-ed17c37cb6-c93a_e9820ec088`)
- **Test-lecture junction does not enforce bai_giang referential integrity** — `packages/api/src/modules/dao-tao/entities/de-kiem-tra-bai-giang.entity.ts:18` (`fnd_sig-feat-library-3fabd1e2f9-6305_58badd095e`)
- **CreatePhanHoiDto accepts attachment IDs that are not consumed downstream** — `packages/api/src/modules/hoi-dap/dto/create-phan-hoi.dto.ts:21` (`fnd_sig-feat-library-312eaefdd1-3ee0_7acf4b0bc5`)
- **Role-permission reseed deletes mappings outside an atomic rewrite** — `packages/api/src/database/seeds/vai-tro-quyen-han.seed.ts:32` (`fnd_sig-feat-library-e9b840709c-e584_65814c9405`)
- **NHT account link is not modeled as a foreign-key relation** — `packages/api/src/modules/nguoi-ho-tro/entities/nguoi-ho-tro.entity.ts:8` (`fnd_sig-feat-library-577ef24af7-a01d_b80a25ec50`)
- **phan_cong_linh_vuc stores unconstrained linh_vuc_id values** — `packages/api/src/modules/danh-gia/entities/phan-cong-linh-vuc.entity.ts:13` (`fnd_sig-feat-library-1c728ca205-1be7_6a2afc2651`)
- **Batch approvals do not create per-case timeline audit rows** — `packages/api/src/modules/vu-viec/vu-viec.controller.ts:135` (`fnd_sig-feat-library-4879d8b29e-54fc_856aefafed`)
- **Free-text feedback sanitizer deletes non-HTML content between angle brackets** — `packages/api/src/modules/chuyen-gia-tvv/dto/create-danh-gia-tvv.dto.ts:4` (`fnd_sig-feat-library-30560fa5dc-9256_0685a14fa6`)
- **ket_qua_danh_gia allows duplicate result rows for the same plan and case** — `packages/api/src/modules/danh-gia/entities/ket-qua-danh-gia.entity.ts:12` (`fnd_sig-feat-library-1c728ca205-2de1_cbf1d895b6`)
- **Random-config edits are accepted in the modal but never submitted** — `packages/web/src/pages/dao-tao/de-kiem-tra/form/DeKiemTraForm.tsx:129` (`fnd_sig-feat-library-a486558955-48bb_685359f3a0`)
- **Fractional 1-5 scores are converted as 0-100 values and collapse to 1** — `packages/api/src/database/migrations/2026050900012-NormalizeThamDinhTvvScale.ts:4` (`fnd_sig-feat-library-60969dbb56-5a7f_3a334ffa50`)
- **Selecting cases is not idempotent and can duplicate ket_qua rows** — `packages/api/src/modules/danh-gia/ket-qua-danh-gia.service.ts:194` (`fnd_sig-feat-library-237acd59eb-712e_b3918f3380`)
- **Attendance edits can be saved to the wrong date after changing the picker** — `packages/web/src/pages/dao-tao/khoa-hoc/tabs/LichHocDiemDanhTab.tsx:44` (`fnd_sig-feat-library-8b8d72555b-9c34_31b80b426b`)
- **Import validation silently truncates overlong text** — `packages/api/src/modules/ngay-le/ngay-le-import.service.ts:193` (`fnd_sig-feat-library-a68ea50ad8-a950_a663631bd8`)
- **Rollback deletes decoupled dot_bao_cao records** — `packages/api/src/database/migrations/2026052600030-DecoupleDotBaoCaoFromChuongTrinh.ts:37` (`fnd_sig-feat-library-8cc0881110-b63c_faf3079d3b`)
- **Profile file relinking writes entity_type values that the read and sub-endpoint paths never use** — `packages/api/src/modules/chuyen-gia-tvv/tu-van-vien.controller.ts:229` (`fnd_sig-feat-library-4315226f8e-e554_e7f3d550aa`)
- **Audit log export silently truncates results at 10,000 rows** — `packages/api/src/modules/audit-log/audit-log.service.ts:268` (`fnd_sig-feat-library-5f0ad78d7e-ac69_d6506f9529`)
- **Cancelled certificate removals persist and can be submitted later** — `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/TabNangLuc.tsx:38` (`fnd_sig-feat-library-26e56c9ad7-e53f_e9c891d9f9`)
- **Delete guard allows removing rows while unpublish sync is still pending** — `packages/api/src/modules/tu-van/workflow/tu-lieu-phap-ly-vv.workflow.ts:23` (`fnd_sig-feat-library-61cbcaef2b-5862_917e9b7dcb`)
- **Journal write failures are reported as integration failures after the external call already succeeded** — `packages/api/src/modules/chuyen-gia-tvv/gateways/tu-van-vien.gateway.ts:73` (`fnd_sig-feat-library-4a9c280009-ec60_1f7044fdeb`)
- **Cleanup verification can be invalidated before the delete** — `packages/api/src/scripts/cleanup-demo-garbage.ts:70` (`fnd_sig-feat-library-ff6714dae5-18d3_6f68fdc39d`)
- **Token issuance mutates Redis session state before JWT issuance is guaranteed** — `packages/api/src/modules/auth/services/token.service.ts:37` (`fnd_sig-feat-library-bff8b9f2f8-b815_5c276daca4`)
- **Unsaved attendance and result edits are overwritten by query refreshes** — `packages/web/src/pages/dao-tao/khoa-hoc/components/DiemDanhTab.tsx:29` (`fnd_sig-feat-library-ed17c37cb6-cd14_18d28508a4`)
- **Canceled certificate deletions persist into later saves** — `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/TabNangLuc.tsx:39` (`fnd_sig-feat-ui-flow-e69cf38b52-013c_4083be73b7`)
- **Saved draft responses can render as a blank form after the response query resolves** — `packages/web/src/pages/hoi-dap/detail/index.tsx:274` (`fnd_sig-feat-library-db7c9e6d6a-8e6f_e9a357832f`)
- **TO_CHUC_TU_VAN cleanup deletes more than the documented seed rows** — `packages/api/src/database/migrations/2026050900007-DropDanhMucToChucTuVan.ts:6` (`fnd_sig-feat-library-d519894ed5-6f2a_b83f0ea370`)
- **Automatic unlock can commit without a durable audit entry** — `packages/api/src/modules/auth/processors/account-unlock.processor.ts:54` (`fnd_sig-feat-library-2965791578-be58_8cee7e69e3`)
- **Attendance Excel round-trip loses VANG_PHEP state** — `packages/api/src/modules/dao-tao/diem-danh.service.ts:197` (`fnd_sig-feat-library-017b22193d-04ff_0036817e2a`)
- **Relationship tables can store orphaned core links** — `packages/api/src/database/migrations/1744000000009-CreateVuViec.ts:86` (`fnd_sig-feat-library-eb23e70db4-09d6_d94176ac67`)
- **Budget field silently saves cleared or negative input as a number** — `packages/web/src/pages/dao-tao/ke-hoach/form/KeHoachDaoTaoForm.tsx:77` (`fnd_sig-feat-library-c7e9ed440b-e7ea_5bc6ce06d2`)
- **Edit save discards milestone edits and cannot clear the last payment** — `packages/web/src/pages/hop-dong-tv/form/HopDongForm.tsx:169` (`fnd_sig-feat-library-a2858dcb59-a180_e16023b42f`)
- **Seed rollback paths delete or overwrite rows they may not own** — `packages/api/src/database/migrations/2026051000011-SeedSubmitTuVanVienForCg.ts:18` (`fnd_sig-feat-library-4e172f5967-d19f_9aa3168824`)
- **Audit logs lose entityId for valid {data, meta} create responses** — `packages/api/src/common/interceptors/audit.interceptor.ts:102` (`fnd_sig-feat-library-cd51a58fe5-9f7f_f146c51a78`)

### concurrency (38)

- **Submit buttons become active again while deferred file uploads are still running** — `packages/web/src/pages/danh-gia/ke-hoach/form/CreateKeHoachDrawer.tsx:83` (`fnd_sig-feat-library-5e0f024231-31f9_0c423059bb`)
- **Concurrent activation resends can email already-invalid temporary passwords** — `packages/api/src/modules/tai-khoan/tai-khoan.service.ts:737` (`fnd_sig-feat-library-fb2181fec9-30c7_da2530f1eb`)
- **Successful SMTP sends are not idempotent across post-send failures and retries** — `packages/api/src/modules/notification/notification.service.ts:81` (`fnd_sig-feat-library-55493e8ef2-dd34_68e7780ab5`)
- **Closing the import dialog does not cancel in-flight import state updates** — `packages/web/src/pages/dao-tao/ngan-hang-cau-hoi/components/NganHangCauHoiImportDialog.tsx:97` (`fnd_sig-feat-library-141d780651-27d1_de50843911`)
- **Import validation can restore stale state after the wizard is closed** — `packages/web/src/pages/tv-nhanh/kho-cau-hoi/components/KhoCauHoiImportWizard.tsx:51` (`fnd_sig-feat-library-8cfc320c72-3987_819b8beb14`)
- **Version checks are not atomic, so concurrent updates can overwrite each other** — `packages/api/src/modules/tu-van/phien-tu-van.service.ts:279` (`fnd_sig-feat-library-205015f24e-7355_89fd154b72`)
- **Outbox uniqueness does not enforce the documented duplicate-enqueue guard** — `packages/api/src/modules/dao-tao/entities/tich-hop-outbox.entity.ts:15` (`fnd_sig-feat-library-2963bb5d18-f2ec_13ce36429d`)
- **Inbound idempotency races on first insert** — `packages/api/src/modules/api-public/services/inbound-public-base.service.ts:108` (`fnd_sig-feat-library-10582b7f1a-f22f_5477264a1c`)
- **OTP auto-submit paths can send concurrent verification requests while pending** — `packages/web/src/pages/auth/login/index.tsx:221` (`fnd_sig-feat-ui-flow-eb7ca14d1e-5721_719c1e25e1`)
- **TVCS unpublish has no state or optimistic-lock guard** — `packages/api/src/modules/tu-van/noi-dung-tu-van-cs.controller.ts:249` (`fnd_sig-feat-library-40298d2981-7654_20bfa59068`)
- **OTP verification state is updated with non-atomic Redis get/set/delete operations** — `packages/api/src/modules/auth/auth.service.ts:282` (`fnd_sig-feat-library-bb39f9f67c-3942_a3dea9cf62`)
- **Case code allocation can return duplicates under concurrent creates** — `packages/api/src/modules/vu-viec/helpers/ma-vu-viec.helper.ts:30` (`fnd_sig-feat-library-0d21b29d01-6a1a_736cf9efe6`)
- **Concurrent registration approvals can increment course enrollment twice** — `packages/api/src/modules/dao-tao/dang-ky-dao-tao.controller.ts:109` (`fnd_sig-feat-library-23dc27379d-b7a9_d993d7c165`)
- **Optimistic-lock check is not atomic with the update** — `packages/api/src/modules/dao-tao/ngan-hang-cau-hoi.service.ts:142` (`fnd_sig-feat-library-e2c8c8bb98-15e2_c6cec1dda7`)
- **Duplicate-insert idempotency path reports creation and re-emits intake events** — `packages/api/src/modules/vu-viec/intake/vu-viec-intake.service.ts:89` (`fnd_sig-feat-library-8a29d10d90-4ca9_44712c8196`)
- **maTvv generation races on MAX(seq)+1 under concurrent creates** — `packages/api/src/modules/chuyen-gia-tvv/tu-van-vien.service.ts:567` (`fnd_sig-feat-library-4315226f8e-3adb_8f6d02c26b`)
- **GiangVien code generation races under concurrent creates** — `packages/api/src/modules/dao-tao/giang-vien.service.ts:151` (`fnd_sig-feat-library-017b22193d-7ddc_39a0cbe3e1`)
- **Transactional notification emails can be dropped by the fixed pre-commit queue delay** — `packages/api/src/modules/notification/notification.service.ts:43` (`fnd_sig-feat-library-55493e8ef2-167f_605be980ca`)
- **Idempotency recovery can fail after duplicate intake races** — `packages/api/src/modules/chi-tra/intake/chi-tra-intake.controller.ts:19` (`fnd_sig-feat-library-7ec5f36678-fdac_d2f971d3d6`)
- **Removed queued files can still upload and be imported** — `packages/web/src/pages/bieu-mau/BieuMauImportWizard.tsx:115` (`fnd_sig-feat-ui-flow-0d5b79a422-069f_afe7023a51`)
- **Advisory lock is not pinned to one Postgres session** — `packages/api/src/modules/tu-van/jobs/tu-van-cs-phan-cong-expiry.job.ts:50` (`fnd_sig-feat-library-390573fa72-31ab_de6adaa915`)
- **Import wizard can reopen on a canceled validation session** — `packages/web/src/pages/quan-tri/ngay-le/components/ImportNgayLeModal.tsx:59` (`fnd_sig-feat-library-29b20f4ee9-a0b6_083c53174c`)
- **Removed files in the import wizard can re-enter the hidden import payload** — `packages/web/src/pages/bieu-mau/BieuMauImportWizard.tsx:115` (`fnd_sig-feat-library-654c5151cb-904c_d11164284c`)
- **HSPL code generation lock ends before insert** — `packages/api/src/modules/api-public/services/ho-so-pl-dn-public.service.ts:75` (`fnd_sig-feat-library-10582b7f1a-3b2b_c8dda3c2e5`)
- **Expiry state changes bypass optimistic version increments** — `packages/api/src/modules/tu-van/jobs/tu-van-cs-phan-cong-expiry.job.ts:135` (`fnd_sig-feat-library-390573fa72-f5f2_f633d23345`)
- **Save can be submitted again while deferred file uploads are still running** — `packages/web/src/pages/hoi-dap/form/components/SectionFileDinhKem.tsx:11` (`fnd_sig-feat-library-05e76ac903-a3c4_b5946d06d8`)
- **Profile optimistic locking is a non-atomic pre-check** — `packages/api/src/modules/tai-khoan/tai-khoan.service.ts:397` (`fnd_sig-feat-library-fb2181fec9-ef24_642d602501`)
- **Course code generation races under concurrent creates** — `packages/api/src/modules/dao-tao/khoa-hoc.service.ts:141` (`fnd_sig-feat-library-22ade395f2-f4f5_1e7897e8a0`)
- **Edit modal can open in create mode while edit detail is still loading** — `packages/web/src/pages/nguoi-ho-tro/index.tsx:57` (`fnd_sig-feat-library-5dd8f9a059-00f3_432e2a4e15`)
- **Publish can race in-flight uploads and leave public-file orphans** — `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/ModalCongKhaiTvv.tsx:93` (`fnd_sig-feat-ui-flow-85547f04f4-10ac_22a1f54e1e`)
- **Import confirmation can be processed twice because the session is not atomically claimed** — `packages/api/src/modules/bieu-mau/bieu-mau.service.ts:833` (`fnd_sig-feat-library-c4299c692e-4547_444eb5cf43`)
- **Successful journals can be written after zero-row updates** — `packages/api/src/modules/tu-van/gateways/noi-dung-tu-van-cs.gateway.ts:112` (`fnd_sig-feat-library-51e1b7693b-4095_f3bd7f0b39`)
- **Idle-session refresh ignores Redis EXPIRE returning zero** — `packages/api/src/common/guards/jwt-auth.guard.ts:87` (`fnd_sig-feat-library-2b7d8128c5-401f_3f5b4c63d3`)
- **In-flight upload can restore a file after the user removes or replaces it** — `packages/web/src/pages/bieu-mau/components/BieuMauFileUpload.tsx:45` (`fnd_sig-feat-ui-flow-d74fc66d7a-eee1_6e23bac453`)
- **Transition dialogs can submit outside the single-pending guard** — `packages/web/src/components/ApprovalActions/approval-actions.tsx:43` (`fnd_sig-feat-ui-flow-9879dfac3b-cfa9_fb1dd3b5d3`)
- **maNht generation races concurrent creates** — `packages/api/src/modules/nguoi-ho-tro/services/nguoi-ho-tro.service.ts:167` (`fnd_sig-feat-library-5c0f2f22ea-c56e_9ad0f55671`)
- **linkFilesToEntity can overwrite associations in concurrent requests** — `packages/api/src/modules/file/file.service.ts:429` (`fnd_sig-feat-library-8b822a2346-cd9c_5b210d6e3a`)
- **Batch replacement is not serialized per role** — `packages/api/src/modules/phan-quyen-du-lieu/phan-quyen-du-lieu.service.ts:145` (`fnd_sig-feat-library-a07573a805-29ba_4949842647`)

---

## 5. Low severity (194 findings)

| Category | Count |
|----------|------:|
| bug | 83 |
| api-contract | 50 |
| test-gap | 41 |
| performance | 6 |
| concurrency | 4 |
| build-release | 3 |
| security | 3 |
| data-loss | 2 |
| docs-gap | 1 |
| maintainability | 1 |

Chi tiết: xem [`.clawpatch/reports/20260527T002749-c6f72f.md`](../source_code/.clawpatch/reports/20260527T002749-c6f72f.md).

---

## 6. Hành động tiếp theo

```bash
# Xem finding ưu tiên kế tiếp
clawpatch --root <source_code> next

# Auto-fix một finding
clawpatch --root <source_code> fix --finding <fnd_id>

# Triage một finding (mark resolved / false-positive)
clawpatch --root <source_code> triage --finding <fnd_id>
```

> Tài liệu này chỉ là digest. Để xem đầy đủ reasoning + test analysis của từng finding,
> mở `.clawpatch/reports/20260527T002749-c6f72f.md` (1.7 MB).