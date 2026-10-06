# Bug Fix Summary — HTPLDN QA Run

_Branch: `rebuild-fe-visual` · Generated: 2026-06-07_

## Overview

| Status | Count |
|---|---|
| ✅ FIXED | 79 |
| ⏭️ WONTFIX (works-as-specified) | 9 |
| ⏳ DEFERRED | 2 |
| **Total unique bugs** | **90** |
| **Open** | **0** |

Fixed by severity: P1=19, P2=30, P3=30.

Fixed by module: api-consumer (2), audit-log (2), auth-session (2), auth-vneid (1), bao-cao (3), bieu-mau (2), cau-hinh-he-thong (1), chi-tra (2), chuyen-gia-tvv (2), cross-cutting (4), ct-htpldn (6), danh-gia (8), dao-tao-core (4), dao-tao-hoc-lieu (9), dashboard (3), doanh-nghiep (2), file-upload (1), ho-so-pl-dn (1), hoi-dap (1), hop-dong-tv (4), nguoi-ho-tro (1), quan-tri/don-vi (1), thong-bao (2), tieu-chi-danh-gia (3), tu-van (3), tv-cs (1), tv-nhanh (4), vu-viec (4).

---

## Fixed bugs by module

### api-consumer (2)

#### 1. `api-consumer-log-drawer-meta-null-crash` — P2

**API Consumer 'Xem log' drawer white-screens on open (data.meta.total on null meta)**

- Fix / root cause: Root cause: useConsumerLogs returned the raw /nhat-ky-tich-hops envelope {data:{items,total,page,pageSize}, meta:null}, but ConsumerLogDrawer read data.meta.total — meta is always null for this endpoint, so opening the drawer threw 'Cannot read properties of null'. Fix: map the nested {items,total,page,pageSize} into PaginatedResponseDto in the hook, and guard data?.meta?.total at the drawer. Verified on browser (admin/QTHT): /quan-tri/api-consumer -> Xem log opens the 'Log tich hop' drawer, table + empty state render, no white-screen, no null-crash in console. Regression unit test added (4 pass).

#### 2. `api-consumer-notfound-wrong-code` — P3

**api-consumer: GET missing id returned generic 404 code instead of resource code**

- Fix / root cause: findOne() threw NotFoundException with a 'CODE: message' STRING body, so GlobalExceptionFilter (object-with-code branch missed) fell back to the generic 404 code ERR-SYS-00-04; the resource code only survived inside the message. Fix: throw NotFoundException({code: ADM_CONSUMER_NOT_FOUND, message}) object body. Verified live as admin (QTHT): GET /api-consumers/<missing-uuid> -> 404 error.code ERR-NOT-FOUND-ADM-00-01. Spec strengthened to assert the structured code.

### audit-log (2)

#### 3. `audit-log-search-ignored` — P2

**audit-log: free-text search box does not filter**

- Fix / root cause: FE audit-log query useMemo now maps searchParams 'keyword' -> API 'search' (AuditLogQuery.search -> ILIKE). Verified live in audit-log UI.

#### 4. `audit-log-lock-account-null-endpoint-responsecode` — P3

**LOCK_ACCOUNT (and account state-change) audit rows had null endpoint + responseCode**

- Fix / root cause: PATCH /tai-khoan/:id/trang-thai (and POST /tai-khoan/bulk-trang-thai) audit account state-changes MANUALLY in TaiKhoanService (dynamic hanhDong KHOA->LOCK_ACCOUNT/MO_KHOA->UNLOCK_ACCOUNT + custom {fromState,toState} duLieuMoi), bypassing AuditInterceptor which is the component that captures endpoint+responseCode from the HTTP request/response. So all TAI_KHOAN audit rows landed with null endpoint+response_code. Root cause for the endpoint half: RlsContextInterceptor seeds the handler CLS via cls.runWith(store) which REPLACES the active store, shadowing nestjs-cls CLS_REQ — so a service cannot read the request from CLS. Fix: (1) RlsContextInterceptor now stashes the request endpoint ('METHOD /url') in its runWith store under new REQUEST_ENDPOINT_CLS_KEY (rls-context.ts); (2) TaiKhoanService.auditRequestContext() reads that key for endpoint and sets responseCode=HttpStatus.OK (the manual emit only fires on the post-commit success path, guaranteed 200 per @HttpCode(OK)); applied to both changeTrangThai + bulkChangeTrangThai emits. Browser-verified as admin: single PATCH lock+unlock rows -> endpoint 'PATCH /api/v1/tai-khoan/<id>/trang-thai', response_code 200; bulk lock+unlock rows -> endpoint 'POST /api/v1/tai-khoan/bulk-trang-thai', response_code 200; du_lieu_moi fromState/toState intact; both test accounts restored to HOAT_DONG. Unit tests: tai-khoan.service (108), rls-context.interceptor, audit.interceptor, audit.service, interceptor-order all pass; added a test asserting endpoint+responseCode on the LOCK_ACCOUNT row.

### auth-session (2)

#### 5. `auth-lockout-retry-after-stripped` — P3

**Lockout 401 loses retry_after_seconds (filter strips flat-payload extras)**

- Fix / root cause: GlobalExceptionFilter flat-payload branch now spreads extra machine-readable fields (e.g. retry_after_seconds) while keeping code/message/timestamp/requestId authoritative. Verified by new filter unit test (13/13 pass). Live account-lockout E2E intentionally skipped: lockAccount revokes all sessions + 30-min lock would disrupt shared QA seed accounts; the transform is pure serialization fully covered by the unit test.

#### 6. `password-cp02-weak-dto-preempts-service-code` — P3

**Weak-password ERR-VAL-VIII-CP-02 now promoted by DTO (was generic ERR-VAL-SYS-00-01)**

- Fix / root cause: ChangePasswordDto + FirstLoginSetPasswordDto: added message: ERROR_CODES.AUTH.CHANGE_PW_WEAK to @MinLength(8) and @IsStrongPassword() on newPassword (covers change-password L459 and first-login set-password L210). Fix: DTO validator now carries its SRS code as the class-validator message so CustomValidationPipe.exceptionFactory promotes the domain code to error.code (and looks up VI text via ERROR_MESSAGES_VI). This is the codebase's intended mechanism (14 DTOs already use it). Status stays 422 — the app-wide validation convention (UnprocessableEntityException) used by every other DTO error; SRS '400' wording deviates but 422 is consistent system-wide. Verified: validation.pipe.spec F8 block runs the REAL DTOs through the REAL pipe (9 cases, all green) + tsc clean + 392 module specs pass; live browser end-to-end confirmed change-password->ERR-VAL-VIII-CP-02 and hop-dong-tv create giaTriHopDong=0->ERR-HDTV-05 with proper VI messages. Browser-verified live: change-password weak pw -> 422 ERR-VAL-VIII-CP-02 'Mật khẩu mới chưa đủ mạnh'.

### auth-vneid (1)

#### 7. `vneid-callback-error-masked-by-global-401-interceptor` — P2

**VNeID callback 401 masked by global interceptor (logout+bounce instead of error Result)**

- Fix / root cause: web/src/utils/request.ts AUTH_ENDPOINTS lacked '/auth/vneid/callback', so the callback's legitimate 401 ERR-VN-01 (invalid/expired OIDC state, NOT a session expiry) triggered the global logout()+/login bounce, hiding the callback page's own error Result. Fix: allowlist '/auth/vneid/callback' (NOT a broad '/auth/vneid/' prefix — '/auth/vneid/link' is an authenticated action whose 401 SHOULD bounce). Browser-verified: navigating /auth/vneid/callback?code=invalid&state=invalid now renders '<Result status=error> Đăng nhập VNeID thất bại...' and stays on /auth/vneid/callback (location.pathname unchanged, no /login redirect).

### bao-cao (3)

#### 8. `bao-cao-export-no-double-submit-guard` — P3

**Bao cao export button lacks double-submit guard**

- Fix / root cause: Xuat Excel/PDF relied on isPending (next-render) so a synchronous double-click fired two POST /bao-cao/export. Added synchronous inFlightRef guard released via onSettled. Browser-verified 2 clicks -> 1 POST; regression test ReportExportButtons.test.tsx green.

#### 9. `bao-cao-filter-controls-not-hydrated-from-url` — P3

**Bao cao filter controls not hydrated from URL deep-link**

- Fix / root cause: ReportFilterPanel mount-only effect missed async-arriving initialValues; added ref-guarded [initialValues] hydration latch. Browser-verified deep-link reload populates Ky/Thoi gian.

#### 10. `bao-cao-lam-moi-does-not-clear-report-view` — P3

**Bao cao Lam moi does not clear report view**

- Fix / root cause: handleReset cleared local state + URL, but react-router store timing let a selectedLoai-guarded effect re-hydrate. Added one-shot hasHydratedRef latch in page + panel clears all controls when selectedLoai null. Browser-verified Lam moi resets to empty.

### bieu-mau (2)

#### 11. `bieu-mau-delete-folder-with-templates-500-fk-restrict` — P1

**DELETE thư mục biểu mẫu containing templates returns 500 (FK RESTRICT) instead of 409 ERR-TM-02**

- Fix / root cause: FIXED. countActiveBieuMau/Batch used raw this.dataSource.createQueryBuilder() — a GUC-less pooled connection where bieu_mau RLS fails closed -> COUNT=0, silently bypassing the THU_MUC_HAS_BIEU_MAU guard so the delete hit FK RESTRICT (bieu_mau.thu_muc_id ON DELETE RESTRICT) -> 500. Fix: route both counts through the injected RLS-safe bieuMauRepo.getRlsSafeQueryBuilder('bm') (the request-pinned runner with RLS GUCs). Live: reproduced 500 on DELETE folder b3aaaaaa-...001 (1 child); after fix -> 409 ERR-TM-02 'Thư mục chứa 1 biểu mẫu, không thể xóa' via API (cb_nv_tw_01) AND browser fetch (cb_nv_tw_02 session); folder+child intact. tsc/eslint clean, spec 51/51.

#### 12. `bieu-mau-import-confirm-rls-write-500` — P2

**Bieu mau bulk import/confirm 500 — unscoped write to RLS table**

- Fix / root cause: FIX: confirmImport via getRequestQueryRunner().manager.transaction. VERIFIED LIVE qtht_01: upload+validate(1 valid)+confirm -> HTTP 200 imported:1, maBieuMau BM-20260606-003, bieu_mau +1.

### cau-hinh-he-thong (1)

#### 13. `mau-phan-hoi-keyword-search-ignored` — P2

**Response-template (mau-phan-hoi) list ignores the keyword search param**

- Fix / root cause: FE mau-phan-hoi SearchPanel now sets keywordParamName='search' so the term reaches the API's findAll search param. Search filters live.

### chi-tra (2)

#### 14. `chi-tra-trinh-phe-duyet-thamdinh-read-rls-context-409` — P1

**Chi-tra trinh-phe-duyet fails: tham_dinh read + StateMachineService locked read both fail-closed on FORCE-RLS**

- Fix / root cause: Two-layer RLS-context bug blocking the entire disbursement approval-submission workflow. Layer 1: trinhPheDuyet read the latest tham_dinh via a pool-bound repo (no request GUCs) -> tham_dinh_ho_so FORCE-RLS fails closed (0 rows) -> false ERR-CT-TRINH-01 'no DAT tham dinh'. Fixed by routing the read through getRlsSafeRepo().manager (CLS RLS-pinned QR). Layer 2 (exposed after layer 1): StateMachineService.transition opens its OWN dataSource.createQueryRunner() for pessimistic-write, which inherits no GUCs -> ho_so_chi_tra FORCE-RLS fails closed -> BadRequestException 'Entity <id> not found' (ERR-VAL-SYS-00-00). Fixed by injecting @Optional() ClsService and mirroring the request GUCs onto the new QR via the sanctioned applyRlsGucs(qr, rlsCtx) helper after startTransaction (same pattern as khoa-hoc/vu-viec/hoi-dap); no-op for cron/system callers with no CLS context. StateMachineService is only used by chi-tra (2 sites: HUY, TRINH_PHE_DUYET), both on FORCE-RLS HoSoChiTraEntity. Browser-verified as cb_nv_tw_01: POST /ho-so-chi-tras/c1aaaaaa-...-0006/trinh-phe-duyet {version:6} -> 200, DANG_THAM_DINH(v6) -> CHO_PHE_DUYET(v7). Specs: state-machine.service.spec (7 incl. 2 new GUC tests) + chi-tra.service.spec (143) green.

#### 15. `tabcounts-stripped-by-response-interceptor` — P2

**Tab count badges always 0: ResponseInterceptor strips top-level tabCounts sibling**

- Fix / root cause: chi-tra.service.findAll now nests tabCounts inside meta (peer convention) so the global ResponseInterceptor preserves it; FE chi-tra/list reads data.meta.tabCounts. Live-verified: API meta.tabCounts={TAT_CA:22,...}; FE renders 'Tất cả22 / Chờ xử lý3 / Đang đánh giá9 / Chờ phê duyệt1 / Đã xử lý9'.

### chuyen-gia-tvv (2)

#### 16. `tvv-vhh-500` — P1

**VO_HIEU_HOA on a HOAT_DONG TVV (no active case) returns 500 ERR-SYS-00-00-01**

- Scenario: `chuyen-gia-tvv:L205`
- Fix / root cause: FIXED commit ee0a17901: assertNoActiveWorkload hoi_dap guard filtered AND deleted_at IS NULL but hoi_dap has no such column -> QueryFailedError -> 500. Predicate removed; regression test added. Live re-verify: POST cap-nhat-trang-thai {VO_HIEU_HOA} now 200 (HOAT_DONG->VO_HIEU_HOA, ver 3->4), state restored. Full suite green (no regressions).

#### 17. `chuyen-gia-tvv-edit-save-files-404-blocks-patch` — P2

**TVV per-entity file upload 404 ERR-TVV-02: resolveHoSoId reads FORCE-RLS ho_so via pool-bound repo**

- Fix / root cause: POST /tu-van-viens/:id/files (and DELETE/download siblings) call resolveHoSoId(), which read ho_so_tu_van_vien via the plain @InjectRepository pool-bound repository. ho_so_tu_van_vien is FORCE RLS at the DB level, so the pool connection (no request GUCs) fails closed -> 0 rows -> false 404 ERR-TVV-02. This blocked the FE 'Lưu' edit flow, which uploads pending avatar/thẻ-hành-nghề/attachment files BEFORE the PATCH (form/index.tsx:148-180) — so any edit that touched a file (notably the TU_CHOI re-submit) failed before the PATCH could run. Fix: route the ho_so read through the RLS-pinned manager (tenantTvvRepo.getRlsSafeRepo().manager.findOne(HoSoTuVanVienEntity,...)) — identical pattern to update() in the same service. Removed the now-orphaned hoSoRepository injection. Browser-verified as cb_nv_tw_01 on TVV 483e19a3-...: fake-PDF blob -> got PAST resolveHoSoId to file-content validation (400 ERR-VAL-FILE-04); real minimal PDF -> 201 Created (fileId f595...); DELETE -> 204. Specs: tu-van-vien (182 pass; updated 3 resolveHoSoId tests to assert the RLS-pinned manager read).

### cross-cutting (4)

#### 18. `fe-create-no-double-submit-guard-duplicate-records` — P2

**Create/submit buttons lack in-flight guard -> double-click creates DUPLICATE records**

- Fix / root cause: Root cause: submit handlers across ct-htpldn/hop-dong-tv/bieu-mau/profile bind the button loading/disabled flag to a mutation's isPending, but isPending only flips true AFTER an awaited form.validateFields(); during that validation window the button stays enabled, so a fast double-click runs the handler twice and fires two POSTs. Fix: new useInFlightGuard() hook wraps each submit handler with a synchronous useRef guard set BEFORE any await, so the second concurrent call returns early. Applied to all 4 confirmed sites. Browser-verified on ct-htpldn create (CB_NV_TW): filled form, fired two synchronous Luu clicks -> exactly ONE POST /chuong-trinh-htpls [201] and ONE DB row (CT-20260607-0001), confirmed via psql. Unit tests for the hook (4 pass) + ct-htpldn create test (5 pass). tsc clean at all edited files.

#### 19. `qtht-manage-all-exceeds-srs` — P2

**QTHT can(Manage,'all') leaked write/workflow verbs on read-only business subjects (SoD)**

- Fix / root cause: QTHT super-admin gets can(Manage,'all') (ability.factory.ts) with enumerate-each-verb cannot() carve-outs; subjects/verbs missing from the enumeration leaked WRITE access to QTHT despite SRS read-only intent (UI hid controls but API was not gated). Fix: replaced the fragile enumerate-each-verb style for the leaked subjects with the robust cannot(Manage, X) + re-grant-read pattern (same as the existing TuVanVien carve-out) — covering all current AND future write verbs. Read-only (Read only): MauPhanHoi, ThuMucBieuMau, BieuMau, KhoaHoc, BaiGiang, DeKiemTra, TuVanNhanh, BaoCao. Read+Export kept: HoSoPhapLyDn, ChuongTrinhDaoTao, NoiDungTuVanCs, KhoCauHoi. BaoCao explicitly loses Export per scenario bao-cao 'POST /bao-cao/export requires can(Export,BaoCao) — QTHT is NOT granted export'. NoiDungTuVanCs + KhoCauHoi moved out of the C/U/D-only TVCS loop (they leaked Approve/Submit/Publish/Unpublish/Import); PhienTuVan/LichSuTraoDoiTv keep C/U/D-deny (no write endpoints). Browser-verified as admin(QTHT): POST /bao-cao/export -> 403, POST /mau-phan-hois -> 403, POST /khoa-hocs/:id/approve -> 403, GET /mau-phan-hois -> 200. Tests: ability.factory 302 pass (added SoD assertion test covering 12 subjects), policies.guard/mau-phan-hoi/bao-cao-export/ket-qua-publish/seed-coverage/file-policy 139 pass. System-admin subjects (TaiKhoan etc.) still can(Manage,'all').

#### 20. `list-keyword-maxlength-422-vs-spec-slice` — P3

**List keyword over 200 chars -> 422 rejection instead of spec slice-to-200**

- Fix / root cause: BaseListQueryDto.search now trims+slices to 200 chars via @Transform instead of @MaxLength(200) hard-reject; over-length keyword returns 200. Idempotent with services that re-slice.

#### 21. `list-pagesize-over-max-422-vs-spec` — P3

**List pageSize over max -> 422 rejection instead of spec cap-to-100**

- Fix / root cause: BaseListQueryDto.pageSize now clamps via @Transform to [1,100] instead of @Max(100) hard-reject; over-max request succeeds with 100 rows. Non-numeric still fails @IsInt. Verified live (pageSize=500 -> 100).

### ct-htpldn (6)

#### 22. `ct-htpl-pause-500` — P1

**Pause of an active CHUONG_TRINH_HTPL returns 500 (raw SQL references non-existent dot_bao_cao.chuong_trinh_id)**

- Fix / root cause: FIXED. Rewrote pauseChuongTrinh active-đợt guard FROM dot_bao_cao d WHERE d.trang_thai IN (TAO_DOT,DANG_LAP_BC,CHO_DUYET_KQ,DA_DUYET_KQ,DA_GUI_TW) AND EXISTS(SELECT 1 FROM bao_cao_ct_htpl b WHERE b.dot_bao_cao_id=d.id AND $1=ANY(b.ct_htpl_ids_lien_quan)). Live: CT-20260606-0008 DANG_THUC_HIEN -> pause (cb_nv_tw_01, confirmCoDotDangLap omitted -> guard SQL runs) -> 200, version 3->4, state TAM_DUNG. Also rewrote remove() dependent-đợt guard (same dead column). tsc/eslint clean, spec 76/76.

#### 23. `ct-htpl-complete-500-bad-column-chuong-trinh-id` — P2

**Complete chuong-trinh-htpl 500 — bad SQL column chuong_trinh_id (should be 409 on unfinished dot)**

- Fix / root cause: FIXED. Rewrote completeChuongTrinh guard (total vs completed đợt) FROM dot_bao_cao d WHERE EXISTS(SELECT 1 FROM bao_cao_ct_htpl b WHERE b.dot_bao_cao_id=d.id AND $1=ANY(b.ct_htpl_ids_lien_quan)); qualifyingStates = isTwCt?[DA_TONG_HOP]:[DA_GUI_TW,DA_TONG_HOP]. Live: drove CT-20260606-0008 DANG_THUC_HIEN -> complete (cb_pd_tw_01) -> 200, version 4->5, state HOAN_THANH. tsc/eslint clean, spec 76/76.

#### 24. `ct-htpl-detail-no-error-state` — P2

**CT HTPL detail page shows infinite Skeleton on 404/error (no not-found state)**

- Fix / root cause: detail/index.tsx:138 guarded with 'if (isLoading \|\| !record) return <Skeleton active />'. On a failed detail query (404 not-found, 403 RLS-filtered, 500) isLoading flips to false but record stays undefined, so !record kept the Skeleton up forever — no escape. Fix mirrors the established chuyen-gia-tvv/chi-tiet pattern: pull isError+error from useChuongTrinhHtplDetail, split the guard into (1) isLoading -> Skeleton, (2) axios 404 -> Result status=404 'Chương trình HTPL không tồn tại' + ERR-VAL-XI-01-00 subtitle + 'Quay lại danh sách', (3) isError \|\| !record -> Result status=error 'Không thể tải chương trình'. Added 2 unit tests (404 + generic-error, assert no .ant-skeleton remains); 25/25 detail tests pass. Browser-verified at /ct-htpldn/<nonexistent-uuid> as cb_nv_tw_01: renders the 404 Result, no skeleton, back button present.

#### 25. `ct-htpl-export-500-bad-column-dbc-chuong-trinh-id` — P2

**ct-htpldn: POST /chuong-trinh-htpls/export -> 500 (column dbc.chuong_trinh_id does not exist)**

- Fix / root cause: FIXED. STT 52 RebuildDotBaoCaoIndependentModel removed dot_bao_cao.chuong_trinh_id (đợt is now TW-owned, scoped by pham_vi_don_vi_nop_ids; only CT link is bao_cao_ct_htpl.ct_htpl_ids_lien_quan). Rewrote so_dot_bao_cao addSelect subquery to EXISTS(SELECT 1 FROM bao_cao_ct_htpl b WHERE b.dot_bao_cao_id=dbc.id AND ct.id=ANY(b.ct_htpl_ids_lien_quan)). Live: UI 'Xuất Excel' click POST /chuong-trinh-htpls/export -> 200 xlsx (browser cb_nv_tw_02, reqid 10910); API 200. tsc/eslint clean, spec 76/76.

#### 26. `ct-htpl-list-tabcounts-stripped` — P2

**CHUONG_TRINH_HTPL list tabCounts dropped by ResponseInterceptor + FE never reads it**

- Fix / root cause: findAllChuongTrinh now nests tabCounts inside meta (peer convention); FE ct-htpldn/list reads data.meta.tabCounts and renders per-trạng-thái badges (TAT_CA = sum since BE groups by trang_thai only). Live-verified: API meta.tabCounts={DU_THAO:23,DA_DUYET:10,CHO_PHE_DUYET:7,...}; FE renders 'Tất cả44 / Dự thảo23 / Chờ PD7 / Đã duyệt10 / ...'.

#### 27. `ct-htpl-pause-lydo-dto-preempts-business-code` — P3

**ct-htpldn pause lyDo<10 now 422 ERR-VAL-XI-06-06 (was generic ERR-VAL-SYS-00-01)**

- Fix / root cause: PauseChuongTrinhHtplDto: @MinLength(10) on lyDo now carries ERROR_CODES.CHUONG_TRINH_HTPL.CT_TAM_DUNG_LY_DO_TOO_SHORT. Fix: DTO validator now carries its SRS code as the class-validator message so CustomValidationPipe.exceptionFactory promotes the domain code to error.code (and looks up VI text via ERROR_MESSAGES_VI). This is the codebase's intended mechanism (14 DTOs already use it). Status stays 422 — the app-wide validation convention (UnprocessableEntityException) used by every other DTO error; SRS '400' wording deviates but 422 is consistent system-wide. Verified: validation.pipe.spec F8 block runs the REAL DTOs through the REAL pipe (9 cases, all green) + tsc clean + 392 module specs pass; live browser end-to-end confirmed change-password->ERR-VAL-VIII-CP-02 and hop-dong-tv create giaTriHopDong=0->ERR-HDTV-05 with proper VI messages. Kept 422 (app convention) not SRS '400'; code now matches ERR-VAL-XI-06-06.

### danh-gia (8)

#### 28. `danh-gia-addassignment-trongso-read-rls-context-422` — P1

**Add evaluator blocked by false 'tong trong so != 100%' (weight-sum read RLS context)**

- Fix / root cause: FIX: listCatalog uses getRlsSafeRepo().createQueryBuilder (no applyRlsFilters strip of NULL rows). VERIFIED earlier: /trong-so works for DP, /cho-ke-hoach non-TW non-empty.

#### 29. `rls-write-500-baocao-danhgia-getorcreate` — P1

**GET ke-hoach-danh-gias/:id/bao-cao 500 on get-or-create — RLS-write on bao_cao_danh_gia**

- Fix / root cause: FIX: getOrCreate routes the INSERT through the CLS RLS QueryRunner (manager.transaction). VERIFIED LIVE qtht_01: GET ke-hoach 106 -> HTTP 200, bao_cao_danh_gia 0->1, maBaoCao BCDG-20260606-0001.

#### 30. `tieu-chi-batchupsert-rls-write-500` — P1

**PUT batchUpsert tieu-chis 500 (plan-scoped RLS write)**

- Fix / root cause: FIX: batchUpsert via CLS RLS QR manager.transaction. VERIFIED LIVE: PUT -> 200, version bumped, count stable.

#### 31. `bao-cao-danh-gia-ma-counter-collision-409` — P2

**bao_cao_danh_gia BCDG-YYYYMMDD-NNNN re-mints across đơn vị → 409 on uq_bcdg_ma_bao_cao**

- Fix / root cause: F2 family. generateMaBaoCao derived next seq via getCount over FORCE-RLS bao_cao_danh_gia on the RLS-pinned QueryRunner; 2nd same-day đơn vị re-minted -0001, colliding on GLOBAL unique uq_bcdg_ma_bao_cao (23505→409). Fix: atomic ma_sequence(namespace='bao_cao_danh_gia') INSERT…ON CONFLICT…RETURNING + backfill mig 2026060600090 (seed 06-06=1). Verified: unit spec drives real ma_sequence path, tsc + eslint green; mechanism identical to LIVE-verified HSPL/TVCS. Live HTTP not run (needs HOAN_THANH-state ke_hoach workflow fixtures per tenant).

#### 32. `ke-hoach-danh-gia-create-409-unique-collision` — P2

**ke_hoach_danh_gia DG-YYYYMMDD-NNNN: every same-day create after the first returns 409**

- Fix / root cause: generateMaKeHoach derived next seq from a getCount inside this.dataSource.transaction — a pooled connection without request RLS GUCs. ke_hoach_danh_gia has FORCE RLS so the count was fail-closed (0), re-minting DG-<day>-0001 on every create → 2nd+ same-day create collided on uq_khdg_ma_ke_hoach (23505→409 ERR-STATE-SYS-00-01). Fix: atomic allocation over non-RLS ma_sequence (namespace=ke_hoach_danh_gia, ngay) via INSERT…ON CONFLICT…RETURNING on dataSource.manager; migration 2026060600040 backfills per-day max (TW cap). Live-verified: cb_nv_bn_01 created DG-20260607-0001 then -0002 (same user, same day — the old 409 repro) and cb_nv_bn_02 (different đơn vị) got -0003, all 201, counter 0→3. 45/45 unit tests green.

#### 33. `qtht-readonly-upload-control-not-disabled` — P2

**danh-gia: QTHT (read-only) detail leaves 'Tai lieu dinh kem' upload dropzone active**

- Fix / root cause: Root cause: ke-hoach-danh-gia detail gated the FileUpload readOnly only on plan status (readOnly={trangThai !== 'LAP_KE_HOACH'}), ignoring the user's write ability — so a read-only QTHT viewing a LAP_KE_HOACH plan got an enabled dropzone. Fix: readOnly={!canMutate \|\| trangThai !== 'LAP_KE_HOACH'} reusing the existing canMutate = ability.can(Update, KeHoachDanhGia). FileUpload's Dragger already maps readOnly -> disabled + hides remove icon. Browser-verified as QTHT on DG-SEED-TW-0001 (LAP_KE_HOACH): dragger now has ant-upload-disabled and input[type=file].disabled=true; 'Huy dot' still hidden. No change for CB NV (canMutate true -> original status gate). Regression unit tests added (readOnly true for QTHT, false for CB NV); detail suite 11 pass.

#### 34. `danh-gia-tieuchi-validation-generic-errorcode` — P3

**tieu-chis item validation now promotes ERR-VAL-TC-02/03/04 (was generic ERR-VAL-SYS-00-01)**

- Fix / root cause: TieuChiItemDto: tenTieuChi @IsString/@IsNotEmpty -> TC_TEN_REQUIRED (ERR-VAL-TC-02); trongSo @Min(0)/@Max(100) -> TC_TRONG_SO_INVALID (ERR-VAL-TC-03); diemToiDa @Min(0.1) -> TC_DIEM_TOI_DA_INVALID (ERR-VAL-TC-04). Nested @ValidateNested promotion confirmed. Fix: DTO validator now carries its SRS code as the class-validator message so CustomValidationPipe.exceptionFactory promotes the domain code to error.code (and looks up VI text via ERROR_MESSAGES_VI). This is the codebase's intended mechanism (14 DTOs already use it). Status stays 422 — the app-wide validation convention (UnprocessableEntityException) used by every other DTO error; SRS '400' wording deviates but 422 is consistent system-wide. Verified: validation.pipe.spec F8 block runs the REAL DTOs through the REAL pipe (9 cases, all green) + tsc clean + 392 module specs pass; live browser end-to-end confirmed change-password->ERR-VAL-VIII-CP-02 and hop-dong-tv create giaTriHopDong=0->ERR-HDTV-05 with proper VI messages. Status already 422 (correct), only code drifted; now domain codes.

#### 35. `phan-cong-reject-lydo-generic-valcode-not-pc06` — P3

**phan-cong reject lyDoTuChoi<10 now ERR-VAL-PC-06 (was generic ERR-VAL-SYS-00-01)**

- Fix / root cause: RejectPhanCongDto: @MinLength(10) on lyDoTuChoi now carries ERROR_CODES.DANH_GIA.PC_LY_DO_TOO_SHORT; moved the inline VI string into ERROR_MESSAGES_VI[ERR-VAL-PC-06]. Fix: DTO validator now carries its SRS code as the class-validator message so CustomValidationPipe.exceptionFactory promotes the domain code to error.code (and looks up VI text via ERROR_MESSAGES_VI). This is the codebase's intended mechanism (14 DTOs already use it). Status stays 422 — the app-wide validation convention (UnprocessableEntityException) used by every other DTO error; SRS '400' wording deviates but 422 is consistent system-wide. Verified: validation.pipe.spec F8 block runs the REAL DTOs through the REAL pipe (9 cases, all green) + tsc clean + 392 module specs pass; live browser end-to-end confirmed change-password->ERR-VAL-VIII-CP-02 and hop-dong-tv create giaTriHopDong=0->ERR-HDTV-05 with proper VI messages. Status already 422 (correct), only code drifted; now domain code ERR-VAL-PC-06.

### dao-tao-core (4)

#### 36. `diem-danh-recalc-param-type-500` — P1

**recalculateAttendance 500: bare $2 (tongBuoi) untyped -> 'could not determine data type of parameter $2'**

- Fix / root cause: NEW (found during F1 diem-danh live verify). recalculateAttendance INSERT uses $2 bare as '$2 AS tong_buoi'; Postgres cannot infer type -> 500. FIX: cast $2::int at all 3 usages (tong_buoi int col). VERIFIED LIVE: batch-update -> 200 after fix; unit guard added (diem-danh.service.spec asserts $2::int, no bare $2).

#### 37. `rls-write-500-diem-danh-batch-update` — P1

**Save attendance 500 — RLS-write on diem_danh (batchUpdate)**

- Fix / root cause: FIX: batchUpdate upsert + recalc route through CLS RLS QR manager. VERIFIED LIVE qtht_01: POST khoa-hocs/406/diem-danhs/batch-update -> HTTP 200, diem_danh 0->2, ket_qua recomputed (ty_le 12.50%).

#### 38. `khoa-hoc-edit-no-editable-form-readonly-detail` — P2

**Khoa hoc: Sua opened read-only detail; edit form missing + BE update() dropped giangVienIds**

- Fix / root cause: Sua link on DU_THAO khoa hoc now routes to /dao-tao/khoa-hoc/:id/chinh-sua (editable form generalized from create page, prefilled from detail + giang-vien pool). BE khoa-hoc.service update() now re-syncs khoa_hoc_giang_vien junctions (giangVienIds was silently dropped via Object.assign). Browser-verified as CB_NV_TW: edit title + add instructor -> PATCH persists, version 1->2, pool reflects new instructor. Tests: 2 regression + full khoa-hoc web suite (61 pass), BE khoa-hoc.service spec (69 pass).

#### 39. `khoa-hoc-list-search-accent-insensitive` — P2

**Khoa hoc list search not accent-insensitive**

- Fix / root cause: khoa-hoc.service ILIKE clauses wrapped both sides in unaccent() so an unaccented query matches accented ten/ma. Spec updated to match. Verified live.

### dao-tao-hoc-lieu (9)

#### 40. `rls-write-500-giang-vien-create` — P1

**GiangVien create/update 500: unscoped createQueryRunner trips tenant_write**

- Fix / root cause: FIX: create/update via getRlsQueryRunner().manager.transaction. Unit 24/24 green; pattern verified live across F1 siblings.

#### 41. `rls-write-500-nganhang-import-confirm` — P1

**Question-bank import confirm 500: fresh createQueryRunner trips tenant_write**

- Fix / root cause: FIX: confirm() batch-insert via CLS RLS QR manager.transaction. VERIFIED LIVE qtht_01: validate (1 HOP_LE) -> confirm HTTP 201 imported:1, ngan_hang_cau_hoi +1.

#### 42. `de-kiem-tra-search-param-mismatch` — P2

**de-kiem-tra: search box sends 'search' but API only honors 'keyword'**

- Fix / root cause: FE de-kiem-tra/list now maps the SearchPanel term to the API's keyword param (apiParams.keyword=filters.search) while keeping the URL param 'search'. Search now filters live.

#### 43. `bai-giang-search-param-ignored` — P3

**Bai giang list search param ignored — returns all rows for any query**

- Fix / root cause: FE bai-giang/list now maps the SearchPanel term to apiParams.keyword (API honors 'keyword'). Search filters live.

#### 44. `de-xuat-dao-tao-delete-received-409-vs-422` — P3

**DELETE de-xuat-dao-tao (DA_TIEP_NHAN) returns 409 instead of spec'd 422**

- Fix / root cause: Covered by the de-xuat state-guard fix: delete guard now returns 422 ERR-DX-03. Live-verified: DELETE /de-xuat-dao-taos/:id on a DA_TIEP_NHAN proposal → 422 ERR-DX-03 (message unchanged, no removal).

#### 45. `dexuat-dao-tao-state-guard-409-vs-422` — P3

**De-xuat-dao-tao state/edit/delete guards return HTTP 409 instead of spec'd 422**

- Fix / root cause: de-xuat-dao-tao update/receive/transition/delete business guards now pass exception:'unprocessable' → 422 (codes ERR-DX-02/03 + messages unchanged). Optimistic-lock conflicts stay 409. Live-verified: receive→422 ERR-DX-02 (L567), update→422 ERR-DX-02 (L585), delete→422 ERR-DX-03 (L593).

#### 46. `dkt-empty-tende-accepted` — P3

**de-kiem-tra create accepts empty tenDe (DTO lacks IsNotEmpty)**

- Fix / root cause: Added @IsNotEmpty to tenDe in CreateDeKiemTraDto. Browser-verified via POST /de-kiem-tras: tenDe='' -> 422 field=tenDe.

#### 47. `dkt-illegal-transition-http-409-vs-422` — P3

**De-kiem-tra illegal-transition guard returns HTTP 409 instead of spec'd 422**

- Fix / root cause: de-kiem-tra kichHoat/tamDung transition guard now passes exception:'unprocessable' to assertGuardOrLog → 422 (code ERR-DKT-STATE + message unchanged). Optimistic-lock conflict stays 409. Live-verified: POST /de-kiem-tras/:id/kich-hoat on KICH_HOAT exam → 422 ERR-DKT-STATE.

#### 48. `empty-file-upload-500-chk-dung-luong` — P3

**upload: 0-byte file -> 500 (chk_file_dung_luong CHECK violation) instead of 4xx validation**

- Fix / root cause: FIXED. BaiGiangFileValidationPipe (and sibling BaiGiangImageValidationPipe) lacked the file.size===0 guard that the global FileValidationPipe has, so a 0-byte .pdf/.pptx/image passed the pipe -> uploadOrphan -> save dung_luong=0 -> chk_file_dung_luong (dung_luong>0) -> 500. Fix: add EMPTY_FILE (ERR-VAL-FILE-05) reject to both pipes. Belt-and-suspenders: uploadSingle now also translates a chk_file_dung_luong 23514 -> 400 EMPTY_FILE. Live: POST /bai-giangs/upload-file 0-byte -> 400 ERR-VAL-FILE-05 (was 500). tsc/eslint clean.

### dashboard (3)

#### 49. `dashboard-aggregate-cache-key-omits-donvicap` — P3

**Dashboard aggregate cache key omits donViCap (scope label bleed)**

- Fix / root cause: Aggregate built from per-KPI caches whose keys omitted donViCap, so the embedded scopeLabel/appliedFilter bled across TW/BN/DP scope toggles. Added donViCap to all cache keys (buildCacheKey, buildKpiCacheKey, aggregate + snapshot keys). Browser-verified: TW=Toan quoc, BN=Cap Bo/Nganh, DP=Cap Tinh/TP back-to-back through cache, no bleed; 84 dashboard unit tests pass.

#### 50. `dashboard-empty-period-ignores-hasData-shows-zero-bars` — P3

**Dashboard charts show misleading zero bars in empty periods**

- Fix / root cause: Chart API zero-fills chartData for every month even when hasData=false, so empty periods rendered real-looking zero bars + '0.0/100'/'0.0%' headlines. Gated chartScoreData/chartSlaData series and summaryScore/summarySla on chartHieuQuaQuery.data.hasData; empty -> ChartBar Empty placeholder. Browser-verified at ?nam=2020: both charts show 'Chua co du lieu ... trong ky', no 0.0 summary.

#### 51. `dashboard-scope-chip-dp-label-css-truncated` — P3

**Dashboard scope chip truncates long DP label**

- Fix / root cause: JS char-slice truncation at 25 clipped the 26-char fixed cap label 'Pham vi: Tat ca dia phuong' to '...phuon...'. Raised SCOPE_TRUNCATE_AT to 30 so all bounded cap-aggregate labels fit; long don-vi-specific names still truncate with the tooltip fallback. Browser-verified at ?donViCap=DP: full label renders, no ellipsis.

### doanh-nghiep (2)

#### 52. `doanh-nghiep-create-button-hidden-cb-nv-tw` — P3

**DN 'Thêm mới' hidden for cb_nv_tw_01 — backend seed drift dropped migration's create_doanh_nghiep grant**

- Fix / root cause: ROOT CAUSE is backend seed drift, NOT an FE bug (FE correctly gates the button on <Can Create DoanhNghiep>). Migration 2026053100020 (STT 39 / FR-V.III-NEW-03) creates create_doanh_nghiep + grants to CB_NV_TW/BN/DP, and a full FE them-moi feature + live @Post createByCbNv endpoint exist. But role-permissions.map.ts (fresh-seed source-of-truth) still omitted create_doanh_nghiep (stale 'FR07-01 retired' comment), so a re-seed of htpldn_dev dropped the migration grant -> live DB had ZERO grants -> cb_nv_tw_01 ability lacked create -> button hidden. FIX: added create_doanh_nghiep to CB_NV_TW/BN/DP blocks in role-permissions.map.ts (updated comment to cite STT 39) so re-seeds keep it; applied idempotent grant to live DB (mirrors migration); added role-permissions.map.spec regression (CB_NV_TW/BN/DP must HAVE; QTHT/NHT/TVV/CG/DN must NOT). VERIFIED: 430 specs green incl new assertions; /auth/me for cb_nv_tw_01 now returns create_doanh_nghiep; browser end-to-end after restart+relogin -> 'Thêm mới' button renders on DN list and navigates to a working /doanh-nghiep/them-moi create form (not DeniedAccess). No FE change needed.

#### 53. `doanh-nghiep-default-sort-ngaytao-vs-ngaycapnhat` — P3

**DoanhNghiep list default sort uses ngayTao DESC instead of spec'd ngayCapNhat**

- Fix / root cause: DoanhNghiepListQueryDto now overrides sortBy default to 'ngayCapNhat' (override keyword per htpldn-rls/forbid-pagination-reinvention) so the omit-sort case lands on FR07-08 'mới cập nhật lên đầu'.

### file-upload (1)

#### 54. `vuviec-file-upload-500-chk-entity-type` — P2

**file-upload: POST /files/upload entityType=VuViec -> 500 (chk_file_entity_type CHECK violation)**

- Fix / root cause: FIXED. Generic /files/upload accepts the PascalCase CASL-subject vocabulary (FILE_ENTITY_TYPES: VuViec, HoSoVuViec, ... via DTO @IsIn) but persists entity_type verbatim; the column CHECK only allows snake_case domain codes (VU_VIEC, ...), so 'VuViec' -> 23514 -> 500. (vu-viec's real file path uses snake 'VU_VIEC' via its own service; the FE has no VuViec upload UI — tracked separately as vu-viec-attachment-no-path.) Fix: uploadSingle now wraps repo.save and translates chk_file_entity_type 23514 -> 422 ERR-VAL-FILE-03 with a clear message. Live: POST /files/upload entityType=VuViec valid.pdf -> 422 ERR-VAL-FILE-03 (was 500). tsc/eslint clean, file.service.spec green.

### ho-so-pl-dn (1)

#### 55. `ho-so-phap-ly-dn-ma-counter-collision-409` — P1

**ho_so_phap_ly_dn HSPL-YYYYMMDD-NNNN re-mints across đơn vị → 409 on uq_hspl_ma_ho_so**

- Fix / root cause: F2 family. Internal generateMaHoSo derived next seq via MAX(ma_ho_so) on the RLS-pinned manager over FORCE-RLS ho_so_phap_ly_dn; 2nd same-day đơn vị re-minted -0001, colliding on GLOBAL unique uq_hspl_ma_ho_so (23505→409). Dual-path: public inbound (runAsSystem/TW) shares the same code, so both internal+public now route through ma_sequence(namespace='ho_so_phap_ly_dn') to avoid allocator divergence. Fix + backfill mig 2026060600060. Verified LIVE cross-tenant: STP-BG→HSPL-20260607-0001, BKH→0002, both 201, no 409; unit specs + tsc + eslint + migration seed green.

### hoi-dap (1)

#### 56. `hoi-dap-lacongkhai-filter-ignored` — P2

**hoi-dap: laCongKhai filter ignored (true returned congKhai=false rows)**

- Fix / root cause: Two fixes: FE da-xu-ly SearchPanel filter key laCongKhai->congKhai with proper tri-state conversion; BE ProcessedHoiDapListQueryDto.congKhai @Transform now reads obj.congKhai raw (global pipe enableImplicitConversion coerced 'false'->true before value-based transform). Both filter directions verified live (1 public + 3 private reconciles).

### hop-dong-tv (4)

#### 57. `hop-dong-tu-van-ma-counter-collision-409` — P1

**hop_dong_tu_van HDTV-YYYYMMDD-NNNN re-mints across đơn vị → 409 on global unique index**

- Fix / root cause: generateMaHopDong derived next seq from MAX(SUBSTRING(ma_hop_dong)) over FORCE-RLS hop_dong_tu_van on the request's RLS-pinned QR (applyRlsGucs) → each đơn vị only saw its own contracts, re-minted …-0001, collided on uq_hdtv_ma_hop_dong (23505→opaque 409). Fix: atomic allocation over non-RLS ma_sequence (namespace=hop_dong_tu_van, ngay) via INSERT…ON CONFLICT…RETURNING on qr.manager; migration 2026060600030 backfills per-day max (TW cap). Live-verified: BKH + BTP-TW (different đơn vị) created sequential HDTV-20260607-0001 and -0002, both 201, no collision. 59/59 unit tests green.

#### 58. `hop-dong-tv-export-500-typeorm-orderby-databasename` — P2

**hop-dong-tv: POST /hop-dong-tu-vans/export -> 500 (TypeORM orderBy databaseName TypeError)**

- Fix / root cause: FIXED. exportExcel used qb.orderBy('hd.ngay_tao','DESC').take(10000); with the to-one leftJoinAndSelect('hd.toChucTuVan') present, .take() triggers TypeORM distinct-id pagination -> createOrderByCombinedWithSelectExpression resolves orderBy via findColumnWithPropertyName('ngay_tao') (entity property is 'ngayTao') -> undefined.databaseName TypeError -> 500. Fix: .take(10000) -> .limit(10000), matching findAll's proven .offset()/.limit() + raw-column orderBy. Live: browser fetch POST /hop-dong-tu-vans/export -> 200 xlsx isZip (cb_nv_dp_c2 session); API 200. spec 54/54 + regression assertion (limit called, take undefined).

#### 59. `hop-dong-tv-giatri-zero-dto-preempts-err-hdtv-05` — P3

**HopDongTuVan giaTriHopDong<=0 now 422 ERR-HDTV-05 (was generic ERR-VAL-SYS-00-01)**

- Fix / root cause: Create+Update HopDongTuVanDto: @Min(0.01) on giaTriHopDong now carries ERROR_CODES.TU_VAN.HDTV_GIA_TRI_INVALID. Fix: DTO validator now carries its SRS code as the class-validator message so CustomValidationPipe.exceptionFactory promotes the domain code to error.code (and looks up VI text via ERROR_MESSAGES_VI). This is the codebase's intended mechanism (14 DTOs already use it). Status stays 422 — the app-wide validation convention (UnprocessableEntityException) used by every other DTO error; SRS '400' wording deviates but 422 is consistent system-wide. Verified: validation.pipe.spec F8 block runs the REAL DTOs through the REAL pipe (9 cases, all green) + tsc clean + 392 module specs pass; live browser end-to-end confirmed change-password->ERR-VAL-VIII-CP-02 and hop-dong-tv create giaTriHopDong=0->ERR-HDTV-05 with proper VI messages. Browser-verified live: create giaTriHopDong=0 -> 422 ERR-HDTV-05 'Giá trị hợp đồng phải lớn hơn 0'. Kept 422 (app convention) not SRS '400'.

#### 60. `hop-dong-tv-subresource-404-code-inconsistent` — P3

**HopDongTuVan moc-tien-do/thanh-toan sub-resource POSTs returned generic 404 code**

- Fix / root cause: batchUpsertMocTienDos/batchUpsertThanhToans loaded the parent contract via tenantRepo.findForUpdateScoped, which throws the generic ERR-VAL-VII-02-01 (HOI_DAP.NOT_FOUND) when the row is missing/cross-tenant; update/remove instead pre-check and throw the contract-specific HDTV_NOT_FOUND (ERR-VAL-X3-159-02). Fix: added a localized lockContractForSubResource helper in the hop-dong service that re-maps the generic NotFoundException to HDTV_NOT_FOUND (shared tenant repo untouched, zero blast radius). Verified live: POST /moc-tien-dos and /thanh-toans on a missing contract -> 404 ERR-VAL-X3-159-02. Added regression spec.

### nguoi-ho-tro (1)

#### 61. `nht-vohieuhoa-guard-bypass-rls-pool-count-0` — P1

**NHT vo-hieu-hoa guard bypassed: active-vu-viec count ran on pool conn (FORCE RLS -> 0)**

- Fix / root cause: FIX: countActiveVuViecForNht runs on getRlsSafeRepo().manager (RLS-pinned) so phan_cong_vu_viec rows are visible. VERIFIED LIVE qtht_01: VHH on NHT 5aaaaaaa-...b01 (2 active) -> HTTP 422 ERR-NHT-04, NHT stays HOAT_DONG. Unit: nguoi-ho-tro spec VHH-block test green.

### quan-tri/don-vi (1)

#### 62. `concurrent-create-race-generic-23505-409-code` — P3

**Concurrent don-vi create race surfaces generic 409 SYS_CONFLICT instead of domain DV_DUPLICATE_MA**

- Fix / root cause: create() pre-checks maDonVi then saves; a lost concurrent INSERT hits unique index uq_don_vi_ma_don_vi (23505), which GlobalExceptionFilter mapped to generic ERR-STATE-SYS-00-01. Fix: wrap save() in try/catch, re-throw ConflictException with DON_VI.DV_DUPLICATE_MA (ERR-VAL-VIII-103-03) on 23505 — same code as the sequential pre-check path. Mirrors the module existing remove() 23503 catch. Verified: live unique index confirmed; don-vi.service.spec 48/48 incl new 23505-race regression test; tsc clean. Actual race window infeasible to reproduce via HTTP (sub-ms gap) — unit-verified by nature. Scope kept surgical to flagged module; systemic across other create endpoints noted.

### thong-bao (2)

#### 63. `thong-bao-keyword-accent` — P2

**Notification keyword search not accent-insensitive (plain ILIKE)**

- Fix / root cause: notification.service keyword clause wrapped in unaccent() on both sides (tieuDe/noiDung) so unaccented query matches accented notifications.

#### 64. `thong-bao-empty-title-accepted` — P3

**Notification create accepts empty tieuDe/noiDung (missing IsNotEmpty)**

- Fix / root cause: Added @IsNotEmpty to tieuDe and noiDung in CreateThongBaoDto. Browser-verified via authenticated POST /thong-baos: empty tieuDe -> 422 field=tieuDe; empty noiDung -> 422 field=noiDung.

### tieu-chi-danh-gia (3)

#### 65. `tieu-chi-catalog-danh-muc-read-empty` — P1

**Master-criteria catalog unreadable (RLS read fail-closed on NULL don_vi)**

- Fix / root cause: FIX: migration 2026060600010 relaxes tenant_read to allow don_vi_id IS NULL master rows. VERIFIED LIVE: /danh-muc -> 10 rows all caps.

#### 66. `tieu-chi-rls-write-500` — P1

**All tieu_chi_danh_gia master-catalog writes 500 (RLS reject)**

- Fix / root cause: FIX: create/update/delete via CLS RLS QR manager.transaction. VERIFIED LIVE qtht_01: POST/PATCH/DELETE -> 201/200/409/204.

#### 67. `tieu-chi-danh-gia-ma-counter-collision-409` — P2

**tieu_chi_danh_gia TC-YYYYMMDD-NNNN re-mints across đơn vị → 409 on uq_tieu_chi_ma**

- Fix / root cause: F2 family. generateMaTieuChi derived next seq via getCount over FORCE-RLS tieu_chi_danh_gia on the RLS-pinned manager (per-plan tiêu chí carry don_vi_id); 2nd same-day đơn vị re-minted -0001, colliding on GLOBAL unique uq_tieu_chi_ma (23505→409). Fix: atomic ma_sequence(namespace='tieu_chi_danh_gia') INSERT…ON CONFLICT…RETURNING + backfill mig 2026060600080 (no date-based codes existed yet → fresh counter). Verified: unit spec drives real ma_sequence path, tsc + eslint green; mechanism identical to LIVE-verified HSPL/TVCS. Live HTTP not run (needs editable ke_hoach_danh_gia workflow fixtures per tenant).

### tu-van (3)

#### 68. `hspl-patch-silently-ignores-doanhnghiepid` — P2

**PATCH ho-so-phap-ly-dn silently ignores immutable doanhNghiepId instead of 400 ERR-VAL-X1-04-07**

- Fix / root cause: UpdateHoSoPhapLyDnDto used OmitType(Create, ['doanhNghiepId']), so the global CustomValidationPipe (whitelist:true, forbidNonWhitelisted=false by default) silently STRIPPED any doanhNghiepId from the PATCH body before it reached the service. The service's immutability guard ('doanhNghiepId in dto') therefore never fired — the field was silently ignored and PATCH returned 200. Fix: declare doanhNghiepId as an optional, validator-less field on UpdateHoSoPhapLyDnDto so whitelist keeps it; it now reaches the service guard which throws 400 ERR-VAL-X1-04-07 for ANY supplied value (no IsUUID precedence). Simplified the guard from a Record<string,unknown> cast to dto.doanhNghiepId!==undefined (the cast became a TS2352 error once the field was typed). Browser-verified as cb_nv_tw_01 on HSPL 85f1bc44-...: PATCH {doanhNghiepId:'other'} -> 400 ERR-VAL-X1-04-07 'Không thể thay đổi doanh nghiệp của hồ sơ'; control PATCH {ghiChu} -> 200 with doanhNghiepId unchanged. Specs: ho-so-phap-ly-dn (22 pass, incl. existing service-layer immutability test).

#### 69. `tv-nhanh-rerate-wrong-code-empty-msg` — P2

**tv-nhanh: re-rate of HOAN_THANH session returned wrong code + empty message**

- Fix / root cause: taoDanhGia() ran the allowedStates guard (DA_GOI_Y/CB_TRA_LOI) before the already-rated existence check. A rated session is already HOAN_THANH, so re-rating failed the state guard and returned generic ERR-DG-TVN-02 with the wrong-state message instead of ERR-DG-TVN-03. Fix: moved the DanhGiaTvEntity existence check before the state guard. Verified live: 1st rate 201 -> HOAN_THANH; 2nd rate 409 code ERR-DG-TVN-03 message 'Phien tu van nhanh da duoc danh gia'. Spec updated: HOAN_THANH re-rate test now asserts ERR-DG-TVN-03 + message.

#### 70. `tvcs-material-create-404-validateNoiDungTv` — P3

**POST tu-lieu-phap-ly-vvs 404 ERR-TLPL-01: validateNoiDungTv reads FORCE-RLS parent via pool query**

- Fix / root cause: TuLieuPhapLyVvService.validateNoiDungTv checked parent existence with a raw this.dataSource.query() on noi_dung_tu_van_cs, which grabs a pool connection carrying no request GUCs. noi_dung_tu_van_cs is FORCE RLS (11 rows visible with cap=TW, 0 with no GUCs), so the fail-closed policy returned 0 rows -> false 404 ERR-TLPL-01 (TLPL_NDTV_NOT_FOUND) even when the parent exists in scope. Fix: run the existence SELECT on the request's RLS-pinned QueryRunner (cls.get(RLS_QUERY_RUNNER_KEY)), falling back to dataSource for non-HTTP/cron callers. Verified sibling validateLinhVuc is safe (danh_muc is NOT FORCE RLS). Browser-verified as cb_nv_tw_01: POST {noiDungTvId:9ff71191-..., loaiTuLieu:TAI_LIEU} -> 201 Created (was 404); negative POST with non-existent parent -> still 404 ERR-TLPL-01 (real misses not masked); cleanup DELETE -> 204. Specs: tu-lieu-phap-ly-vv (42 pass).

### tv-cs (1)

#### 71. `noi-dung-tu-van-cs-ma-counter-collision-409` — P1

**noi_dung_tu_van_cs TVCS-YYYYMMDD-NNNN re-mints across đơn vị → 409 on uq_ndtvcs_ma_tu_van**

- Fix / root cause: F2 family. generateMaTuVan derived next seq via MAX(ma_tu_van) on the RLS-pinned manager over FORCE-RLS noi_dung_tu_van_cs; each đơn vị saw only its own rows so the 2nd same-day creator re-minted -0001 and collided on GLOBAL unique uq_ndtvcs_ma_tu_van (23505→opaque 409). Latent in dev (≤1 đơn vị/day). Fix: atomic ma_sequence(namespace='noi_dung_tu_van_cs') INSERT…ON CONFLICT…RETURNING + backfill mig 2026060600050. Verified LIVE cross-tenant: STP-BG→TVCS-20260607-0001, BKH→0002, both 201, no 409; unit specs + tsc + eslint + migration seed green.

### tv-nhanh (4)

#### 72. `kho-cau-hoi-ma-counter-collision-409` — P1

**kho_cau_hoi QA-YYYYMMDD-NNNN re-mints across đơn vị → 409 on global unique index**

- Fix / root cause: generateMaCauHoi/allocateMaCauHoiBlock derived next seq from an RLS-scoped getCount over FORCE-RLS kho_cau_hoi → each đơn vị restarts at 0001 and collides on uq_kho_cau_hoi_ma_cau_hoi (23505→opaque 409). Fix: atomic allocation over non-RLS ma_sequence (namespace=kho_cau_hoi, ngay) via INSERT…ON CONFLICT…RETURNING; migration 2026060600020 backfills the counter from existing per-day max (TW cap). Live-verified: two different đơn vị (BKH, BTC) created sequential QA-20260606-0002 and -0003, both 201, counter 1→3, no collision.

#### 73. `kho-cau-hoi-search-param-mismatch-and-accent` — P2

**kho_cau_hoi search non-functional: FE search vs API keyword + not accent-insensitive**

- Fix / root cause: FE kho-cau-hoi/list maps term to keyword (apiParams + tabCountParams); BE migrated search to search_vector_v2 GENERATED column built with public.f_unaccent + GIN index (migration 2026060700010), queried via f_unaccent(plainto_tsquery). Accent-insensitive + param wired.

#### 74. `tu-van-nhanh-ma-counter-collision-409` — P2

**tu_van_nhanh TVN-YYYYMMDD-NNNN re-mints across đơn vị → 409 on uq_tu_van_nhanh_ma_phien**

- Fix / root cause: F2 family. generateMaPhien derived next seq via getCount over FORCE-RLS tu_van_nhanh on the RLS-pinned manager (don_vi_id server-derived from DN tỉnh); 2nd same-day đơn vị re-minted -0001, colliding on GLOBAL unique uq_tu_van_nhanh_ma_phien (23505→409). Fix: atomic ma_sequence(namespace='tu_van_nhanh') INSERT…ON CONFLICT…RETURNING + backfill mig 2026060600070. Verified: unit spec drives real ma_sequence path, tsc + eslint + migration seed (06-04=1,06-05=2,06-06=8) green; mechanism identical to LIVE-verified HSPL/TVCS. Live HTTP not run (public-API scope-auth inbound endpoint).

#### 75. `kho-cau-hoi-view-counter-not-incrementing` — P3

**kho-cau-hoi so_luot_xem never increments on detail GET**

- Fix / root cause: Increment ran on pool-level dataSource.query without RLS GUCs so the FORCE-RLS policy matched 0 rows. Now runs the raw UPDATE on the request RLS-pinned QueryRunner (RLS_QUERY_RUNNER_KEY) and awaits it so it commits before QR release; raw SQL still avoids @VersionColumn bump. Browser-verified: so_luot_xem 0 -> 2 after two detail GETs (committed list read). Added RLS-pinned-path unit test.

### vu-viec (4)

#### 76. `vu-viec-assignedtome-guard-rejects-assigned-tvv` — P1

**Assigned TVV gets 403 on accept/update-result/reject — AssignedToMeGuard false-negative (RLS-context read)**

- Fix / root cause: ROOT CAUSE: AssignedToMeGuard runs in the GUARD phase, before RlsContextInterceptor (a NestInterceptor) pins the per-request RLS QueryRunner into CLS. VuViecPolicyService.isAssigned used tenantVuViecRepo.getRlsSafeRepo(), which falls back to a pool connection with NO GUCs when CLS.queryRunner is absent → FORCE-RLS on vu_viec fails closed (0 rows) → isAssigned=false → assigned TVV wrongly denied 403 ERR-PERM-VI-10-01 on nhan-phan-cong / cap-nhat-ket-qua / tu-choi-phan-cong. FIX: VuViecPolicyService.isAssigned now runs the ownership count via InternalSystemQueryBuilder.runAsSystem (the sanctioned RLS bypass). Safe because the predicate is self-scoping — vv.nguoi_ho_tro_id = :userId only matches a case assigned to the *calling* user, so the bypass leaks nothing cross-tenant (answer is a single boolean). Dropped the now-unused TENANT_REPO_VuViec injection from the policy service. Updated vu-viec-policy.service.spec.ts (mock runAsSystem); 3/3 pass. BROWSER/API-VERIFIED as tvv_01 (role TVV): nhan-phan-cong on DA_PHAN_CONG VV-QA-TW-DPC-01 -> 201, trang_thai DA_PHAN_CONG->DANG_XU_LY (was 403); cap-nhat-ket-qua + tu-choi-phan-cong with empty body -> 422 ERR-VAL-SYS-00-01 (reached DTO pipe past the guard), no longer 403 ERR-PERM-VI-10-01.

#### 77. `vu-viec-already-rated-generic-409-not-vi-16-02` — P2

**Re-rating an already-rated vu viec returned generic state code instead of ALREADY_RATED**

- Fix / root cause: danhGia() ran the generic 'danhGia' state guard (requires HOAN_THANH) before the ALREADY_RATED existence check. After the first rating the case is DA_DANH_GIA, so a 2nd rating failed the state guard and returned ERR-STATE-VI-16-01 instead of ERR-VAL-VI-16-02. Fix: moved the danh_gia_vu_viec existence check before the state guard. Verified live: 1st rating 201 -> DA_DANH_GIA; 2nd rating 409 ERR-VAL-VI-16-02. Spec updated to assert the code on the real DA_DANH_GIA path.

#### 78. `vu-viec-kenh-doanh-nghiep-enum-not-whitelisted-422` — P2

**vu-viec list filter ?kenhTiepNhan=DOANH_NGHIEP rejected 422 though such rows exist**

- Fix / root cause: VuViecListQueryDto.kenhTiepNhan @IsIn whitelist (VU_VIEC_KENH_TIEP_NHAN) omitted 'DOANH_NGHIEP', so filtering by the DN self-service channel returned 422 even though 4 such rows exist and the DB check constraint chk_vu_viec_kenh explicitly allows it (value is set server-side in vu-viec.service.ts createTuDoanhNghiep:269). Added 'DOANH_NGHIEP' to the list-query whitelist only; left the manual-create DTO (create-vu-viec-thu-cong) untouched since staff manual intake intentionally excludes the DN self-service channel. Browser-verified as cb_nv_tw_01: GET /vu-viecs?kenhTiepNhan=DOANH_NGHIEP -> 200, total=4, all items kenhTiepNhan=DOANH_NGHIEP (was 422). Note: entity @Check decorator (vu-viec.entity.ts:16) is stale vs live constraint — cosmetic drift only (synchronize off); left as-is.

#### 79. `vu-viec-tenant-isolation-shared-rls-code-not-module-code` — P3

**Vu-viec tenant-isolation 404 leaked shared HOI_DAP code instead of vu-viec module code**

- Fix / root cause: GET /vu-viecs/:id for a non-existent or RLS-hidden (cross-tenant) row returned 404 ERR-VAL-VII-02-01 (shared HOI_DAP.NOT_FOUND wire code) because TenantScopeInterceptor hardcoded that code for ALL modules. Added notFoundCode/notFoundMessage to TenantScopedOptions; wired both interceptor 404 throws (malformed-UUID + entity-not-found) to opts.notFoundCode ?? ERROR_CODES.HOI_DAP.NOT_FOUND (backward-compatible default). Defined VU_VIEC_SCOPE with notFoundCode=ERR-VAL-VI-03-02 + message 'Vu viec khong ton tai' and applied to all 27 @TenantScoped decorators in vu-viec.controller.ts. Browser-verified on page 2 (cb_nv_tw_01): GET non-existent id -> 404 ERR-VAL-VI-03-02. tenant-scope.interceptor/vu-viec.controller/service/approval unit specs pass (default-fallback tests still assert ERR-VAL-VII-02-01). 4 failing tests are pre-existing DB-seed issues in test/rls/vu-viec-intake.spec.ts, untouched by this fix.

---

## WONTFIX (verified against SRS — code is correct)

- **`api-consumer-no-responsive-layout-hard-gate-1024`** (P3, api-consumer) — Narrow viewport shows desktop-only guard (>=1024px) instead of responsive layout
  - WONTFIX - works as specified. SRS UI-07 (docs/srs-v3.5/srs-v3.5.md:570) mandates 'Desktop-only. Min width: 1024px ... Duoi 1024px: hien thi thong bao Vui long su dung man hinh >= 1024px ... Khong ho tro mobile/tablet'. PRT-01 (:4513) marks desktop-only as PO-confirmed (CDT xac nhan); OS-02 (:158) says the CMS only supports desktop browsers. main-layout.tsx:348-350 renders ScreenBlocker below 1024px and auto-collapses the sidebar at 1024-1279px (:341), exactly matching UI-07. The hard gate is intentional, not a defect; the scenario expecting a responsive/stacked layout below 1024px contradicts the spec. No code change.
- **`danh-muc-ma-editable-on-update-spec-conflict`** (P3, danh-muc) — Danh muc edit modal renders editable Ma (scenario claims immutable)
  - WONTFIX - code matches the authoritative SRS, the QA scenario premise is wrong. SRS TPL-DM-CRUD UPDATE step 4 (docs/srs-v3.5/srs-fr-10-quan-tri.md:113) explicitly says 'Kiem tra khong trung ma (neu doi ma): loai tru chinh minh' = duplicate-check IF the code is changed -> renaming ma on update is spec-permitted. UpdateDanhMucDto whitelists ma (update-danh-muc.dto.ts:25-29, comment cites TPL-DM-CRUD/BUG-DM-002), danh-muc.service.ts:266-271 validates whitelist + duplicate (id != self, 409) on rename, and DanhMucForm renders ma editable in both modes by design. Data-integrity risk LOW (FKs use UUID id, not ma). Scenario danh-muc:L132 should be corrected to expect editable ma; no code change.
- **`dao-tao-khoahoc-approve-cross-bn-403-vs-404-tenant`** (P3, dao-tao-core) — CB_PD_TW approve of BN-owned khoa-hoc returns 403 ERR-PERM-III-15-01 (scenario L728 expected 404)
  - WONTFIX — intended, spec-sanctioned behavior. Actor cb_pd_tw_01 (TW cap) approving a BN-owned (BKH, 8001..401) khoa-hoc. rls.check_don_vi_scope returns TRUE for cap=TW, so a TW user legitimately SEES all BN/DP rows (GET 200 is correct TW-oversight, not a leak). approve() then hits checkSameTier (khoa-hoc-workflow.service.ts:956): user.donViId !== entity.donViId -> 403 KHOA_HOC_SAME_DON_VI_REQUIRED = ERR-PERM-III-15-01 (BR-AUTH-05 strict, 'BA chot #2 §6 2026-05-08'). The cited scenario L728 expects 404 on a FALSE premise ('record not in my don vi scope') — but TW cap's RLS scope DOES include BN, so the record is exposed and 404 cannot apply. The SAME feature file 15 lines below (L743-747) describes the identical actor+situation: 'same-don-vi approve guard returns 403 if the record passes RLS but don vi differs ... cb_pd_tw_01 attempts approve -> 403 with code ERR-PERM-III-15-01 (or 404 if RLS already hid it)'. Observed behavior exactly matches L743. Sibling TVV scenario L724 ('CB_PD_TW cannot approve a BN/DP TVV even though it is visible -> BR-AUTH-05 same don-vi') confirms the same 403 contract. No security impact (approve correctly blocked). Spec L728 is internally inconsistent with L743/L724; no code change.
- **`doanh-nghiep-dup-mst-wrong-error-code`** (P3, doanh-nghiep) — doanh-nghiep: duplicate-MST self-registration error code (SPEC CONFLICT - not a code bug)
  - INVESTIGATED: false positive from conflicting specs. POST /auth/register-doanh-nghiep returns 409 ERR-REG-MST-EXIST with the 'Quen mat khau' claim-flow message. This EXACTLY matches auth-session.feature:277 (P1, owning-domain spec) and the documented intent in error-codes.ts:72-74 (REGISTER_MST_EXIST = intentional claim-flow CTA, distinct from generic ERR-REG-01/ERR-DN-02). The conflicting doanh-nghiep.feature:115 (P2) expects ERR-DN-02 + generic message, which predates the claim-flow unification (single findByMstAsSystem check covers both profile-only and account-exists cases). Changing to ERR-DN-02 would REGRESS the P1 claim-flow UX. Recommendation: reconcile doanh-nghiep.feature:115 to ERR-REG-MST-EXIST; no code change.
- **`import-oversize-multer-413-preempts-app-400`** (P3, cau-hinh-he-thong) — Oversize ngay-le import returns Multer 413 (correct, memory-safe) — stray spec L560 expects 400; specs contradict
  - Live-verified: POST /ngay-le/import/validate with a >5MB file returns 413 (Multer LIMIT_FILE_SIZE -> NestJS PayloadTooLargeException, code ERR-SYS-00-00-01 'File too large'). This is HTTP-correct and DELIBERATE: ngay-le.controller.ts:84-88 rejects oversized uploads BEFORE buffering to prevent memory-exhaustion from hostile uploads; the service file.size>5MB check (NL-12, 400) correctly remains as belt-and-suspenders for Multer-bypassed/sub-limit paths. Specs contradict: ngay-le.feature L458-462 (feature-of-record) explicitly accepts '413/400' and documents this design; cau-hinh-he-thong.feature L560 outline row demands strict 400 ERR-VAL-VIII-NL-12. The ONLY way to force 400 is to lift the Multer fileSize limit, which reintroduces the DoS vector the code guards against — a security regression. WONTFIX (code is correct + secure). RECOMMENDATION: update cau-hinh-he-thong.feature L560 'file > 5MB' row from 400 to 413 to match ngay-le L458 and the memory-safe behavior; keep NL-12 as the documented Multer-bypass fallback. Mirrors the doanh-nghiep spec-conflict WONTFIX precedent (don't regress secure behavior to satisfy a contradictory P2/P3 line).
- **`parseuuidpipe-malformed-id-400-vs-404`** (P3, common) — ParseUUIDPipe returns 400 for malformed id where spec expects 404
  - BY DESIGN / framework default. NestJS ParseUUIDPipe returns 400 Bad Request for a syntactically-invalid UUID, which is correct REST semantics (malformed client input = 400, not 404). The QA spec's expectation of 404 here is an outlier and is internally inconsistent with the companion bug tvcs-invalid-uuid-404 (which expects 400 for the same malformed-UUID condition on a tenant-scoped route). Standardizing the whole API on one of 400/404 for malformed ids would be a broad cross-cutting change contradicted by the spec itself. Keeping the framework default (400 on raw-pipe routes, 404 on tenant-scoped routes via the anti-enumeration interceptor) is the consistent, defensible position. No code change.
- **`profile-save-button-label-luu-vs-luu-thay-doi`** (P3, profile) — Profile save button 'Lưu' is correct per mandatory rule H4 — scenario expectation 'Lưu thay đổi' is wrong
  - FE correctly reads 'Lưu' (ProfileInfoTab.tsx:156), browser-confirmed live on /profile (primary button = 'Lưu'). This is MANDATORY per rule H4 (SRS srs-v3.5.md:6570, Phụ lục E mục H): create button='Thêm mới', save button='Lưu' (NOT 'Lưu thay đổi'). Commit 595a08a4c intentionally normalized this very button from 'Lưu thay đổi'->'Lưu' per H4. The scenario profile:L495 asserting 'Lưu thay đổi' contradicts the mandatory rule. WONTFIX (code correct). RECOMMENDATION: fix scenario profile:L495 to assert 'Lưu'. Reverting would violate H4 + undo an intentional commit.
- **`profile-save-button-label-mismatch`** (P3, profile) — Profile save button 'Lưu' is correct per mandatory rule H4 — scenario expectation 'Lưu thay đổi' is wrong
  - FE correctly reads 'Lưu' (ProfileInfoTab.tsx:156), browser-confirmed live on /profile (primary button = 'Lưu'). This is MANDATORY per rule H4 (SRS srs-v3.5.md:6570, Phụ lục E mục H): create button='Thêm mới', save button='Lưu' (NOT 'Lưu thay đổi'). Commit 595a08a4c intentionally normalized this very button from 'Lưu thay đổi'->'Lưu' per H4. The scenario profile:L495 asserting 'Lưu thay đổi' contradicts the mandatory rule. WONTFIX (code correct). RECOMMENDATION: fix scenario profile:L495 to assert 'Lưu'. Reverting would violate H4 + undo an intentional commit.
- **`tvcs-invalid-uuid-404-interceptor-precedes-pipe`** (P3, tu-van) — GET noi-dung-tu-van-cs/:id with non-UUID returns 404 (interceptor) instead of 400 (pipe)
  - BY DESIGN. TenantScopeInterceptor deliberately returns 404 'Bản ghi không tồn tại' for malformed-UUID :id params on tenant-scoped routes (tenant-scope.interceptor.ts:28-34, 90-102): (a) anti-enumeration — a malformed id and a non-existent id are indistinguishable, no info leak; (b) avoids a PG 'invalid input syntax for type uuid' 500. Interceptors run before param pipes in NestJS by framework design, so the controller's TvCsIdPipe (400 ERR-TVCS-00-01) only fires on @SkipTenantScope routes (e.g. :id/audit-logs, verified 400). Making the tenant-scoped route also return 400 requires either changing the interceptor's 404->400 globally (high blast radius across the entire HOI-001 family + every tenant-scoped route; some QA specs expect 404 for malformed ids — see companion bug parseuuidpipe-malformed-id-400-vs-404) or per-route config (over-engineering for a P3). 404 for a syntactically-invalid resource id is defensible REST semantics. Verified current behavior: /noi-dung-tu-van-cs/not-a-uuid -> 404 ERR-VAL-VII-02-01; /not-a-uuid/audit-logs -> 400 ERR-TVCS-00-01.

## DEFERRED

- **`danh-gia-cqdg-read-kq-wrong-errorcode-dg10-vs-dg11`** (P3, danh-gia) — cqdg read-ket-qua on non-HOAN_THANH plan returns ERR-DG-10 instead of ERR-DG-11 (RLS-blocked, deferred)
  - INVESTIGATED + verified live. Root cause is architectural, not a simple code swap. The RLS policy fr_vi_10_cqdg_read (migration 2026051300100) admits a cqdg SELECT on ke_hoach_danh_gia ONLY when trang_thai='HOAN_THANH'. For a BAO_CAO plan the RLS-scoped findOne returns NULL (row hidden), so both the TenantScopeInterceptor and KeHoachDanhGiaService.findOne hit their not-found branch and emit the generic ERR-DG-10 before any status check; the service ERR-DG-11 branch is effectively dead for the RLS-enforced cqdg path. The interceptor (lines 140-146) documents ERR-DG-10-for-both as the deliberate enumeration-safe choice (FORCE RLS, no BYPASSRLS). Emitting ERR-DG-11 requires a privilege-bypassing status-probe (SECURITY DEFINER fn scoped to caller allowedDonViIds) to distinguish 'exists-but-not-complete' from 'missing/forbidden' — new security-sensitive DB infrastructure, disproportionate for a P3 where current behavior (403, no data leak) is correct. Verified live: cb_nv_bn_01 GET /ke-hoach-danh-gias/<BAO_CAO,in-cqdg-scope>/ket-quas -> 403 ERR-DG-10; HOAN_THANH in-scope -> 200. App-layer fix attempted then reverted (never fires under RLS). RECOMMEND: add rls.cqdg_plan_pending(id, allowed[]) SECURITY DEFINER probe if ERR-DG-11 distinction is required by product/security.
- **`vu-viec-attachment-no-path`** (P2, vu-viec) — Vu viec: no working path to attach documents (create eager-upload 422s; detail Thêm tài liệu never renders)
  - ARCHITECTURAL GAP — needs BE endpoint design + product/SRS decision; out of scope for a surgical FE fix. Two parallel, disconnected attachment stores: (1) ho_so_vu_viec — feeds the detail 'Tài liệu' table (vu-viec.service.getHoSo: hoSoRepo.find by vuViecId); written ONLY by dn-submit (createForDoanhNghiep, fileDinhKemIds) and the state/role-gated bo-sung path. (2) file_dinh_kem — generic polymorphic store written by POST /files/upload (entityType+entityId required; has a VuViec FilePolicyProvider canAttach/canAccess/canDelete). The detail tab shows (1) but the generic uploader writes (2) — they never meet. CREATE half: tao-moi/index.tsx renders SectionTaiLieuDinhKem whose FileUpload eagerly POSTs /files/upload with NO entityType/entityId -> 422 toast on first file drop; and createManual (+CreateVuViecThuCongDto/CreateVuViecDto) never declares or reads fileDinhKemIds, so even a passed list is silently dropped (whitelist strips it). DETAIL half: detail/index.tsx:191-197 passes canUpload but NOT onUpload, and SectionTaiLieu.tsx:90 gates the button on canUpload && onUpload -> 'Thêm tài liệu' can never render (browser-verified on DA_TIEP_NHAN case VV-BKH-20260606-001 as cb_nv_tw_01 with edit rights: panel shows 'Chưa có tài liệu', no button). Even if onUpload were wired to /files/upload, uploads land in file_dinh_kem and would NOT appear in the ho_so_vu_viec-fed table; there is NO generic endpoint to add a ho_so_vu_viec doc to an existing case outside gated bo-sung. RECOMMENDATION: pick ONE store for 'tài liệu vụ việc'. Cleanest: add POST /vu-viecs/:id/ho-so (role=update_vu_viec, state in editable set) that creates ho_so_vu_viec rows from pre-uploaded/file ids; wire detail onUpload -> modal FileUpload(deferred) -> attach -> refetch getHoSo; remove the dead SectionTaiLieuDinhKem from manual-create OR route it through the same post-create attach. Requires confirming SRS intent on which roles/states may attach.
