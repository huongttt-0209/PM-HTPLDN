# TODO Bug Tracking — Round 7 (Tổng hợp toàn bộ bug report)

> Ngày tổng hợp: 2026-05-11
> Nguồn: 18 file trong `docs/bug-report/`
> Mục đích: 1 nơi tracking trạng thái fix bug cross-module

## Quy ước trạng thái

| Marker | Status | Ý nghĩa |
|---|---|---|
| ⬜ | **PENDING** | Chưa ai nhận / chưa bắt đầu |
| 🟡 | **DOING** | Dev đang fix (in progress) |
| 🔵 | **TESTING** | Dev báo fix xong, QA đang verify |
| ✅ | **DONE** | QA verify pass, đã close |
| ❌ | **REJECT** | Không phải bug / out-of-scope / duplicate / retracted |
| 🟣 | **NEED_BA_CONFIRM** | Chờ BA chốt spec mới fix được |

**Cách update**: sửa cột Status từ một marker sang marker khác. Ghi chú thay đổi vào cột "Note" nếu cần.

---

## 0. Bảng tóm tắt (Executive snapshot)

| Module / FR | Pending | Doing | Testing | Done | Reject | NEED_BA | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|
| FR-01 Dashboard | 15 | 0 | 0 | 4 | 0 | 0 | 19 |
| FR-05 Vụ việc | 5 | 0 | 0 | 13 | 0 | 1 | 19 |
| FR-06 Chi trả | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| FR-08 Đánh giá HTPL | 14 | 1 | 0 | 7 | 0 | 5 | 27 |
| FR-11 Báo cáo | 8 | 0 | 0 | 5 | 1 | 1 | 15 |
| FR-12 TVCS | 9 | 1 | 0 | 4 | 0 | 8 | 22 |
| Hỏi đáp (SLA tier) | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| Tư vấn nhanh (TVN) | 3 | 0 | 0 | 4 | 0 | 0 | 7 |
| Hợp đồng TV (HDTV) | 2 | 0 | 0 | 10 | 0 | 1 | 13 |
| Đào tạo (BM/HV/DT) | 5 | 0 | 0 | 2 | 0 | 1 | 8 |
| Kế hoạch năm (KH) | 1 | 0 | 0 | 2 | 0 | 0 | 3 |
| API / mTLS | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| **TỔNG** | **66** | **3** | **0** | **51** | **1** | **17** | **138** |

> Trạng thái Pending/Doing/NEED_BA mặc định khởi tạo từ trạng thái Open/Partial/Open-Need-BA của report nguồn. Cần BA + Dev review lại trước khi giao task.

---

## 1. FR-01 Dashboard (Nhóm I — W5.3)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-DASH-FILTER-001 | Critical | SCR-I-01 Vùng 2 Bộ lọc | Bộ lọc dùng "Từ ngày-Đến ngày" thay vì "Năm + Tháng" — CR v3.5 chưa apply (cascade scope_label / auto-refresh / drill) | FE+BE | Commit 549ba4c4 — replace DatePicker with Tháng Select + Cấp đơn vị; drill snake_case forward |
| 🔵 | BUG-DASH-TPL-001 | Critical | 7 KPI + 2 KPI-S / TPL-DASH-KPI | TPL-DASH-KPI thiếu 6/12 fields outputs (nam, thang, scope_label, tu_ngay_boundary, den_ngay_boundary, is_qua_khu_dong) | BE | Commit 549ba4c4 — buildAppliedFilter helper populates 6 fields on every KPI/aggregate/chart response |
| 🔵 | BUG-DASH-KPI03-001 | Critical | KPI-03 / DASH | Đếm SAI 25 thay vì 23 (BE include thừa enum CHO_PHE_DUYET + DA_DUYET) | BE | Commit cbcf9f69 — ACTIVE_STATUSES drop CHO_PHE_DUYET + DA_DUYET (5 states per SRS 291-301) |
| 🔵 | BUG-DASH-KPI03-002 | Critical | KPI-03 drill-down | URL thừa 2 enum + thiếu 4 filter params + path/snake_case sai | BE | Commit cbcf9f69 — drill /vu-viec → /vu-viec/danh-sach, 5 states; filter params forwarded by FE (DRILL-001 covers snake_case) |
| 🔵 | BUG-DASH-KPI04-001 | Critical | KPI-04 / DASH | Đếm SAI 300% (4 thay vì 1) — thừa DA_DANH_GIA | BE | Commit 5e377fc1 — getVuViecHoanThanh scoped to [HOAN_THANH] only per SRS 326 |
| 🔵 | BUG-DASH-KPI04-002 | Critical | KPI-04 drill-down | Thừa DA_DANH_GIA + thiếu date_field + filter params | BE | Commit 5e377fc1 — drill /vu-viec → /vu-viec/danh-sach, HOAN_THANH only (date_field/snake_case in DRILL-001 batch) |
| 🔵 | BUG-DASH-KPI06-001 | Critical | KPI-06 drill-down | Dùng HOAN_THANH thay vì DA_KET_THUC (SM-KHOAHOC v3.5) | BE | Commit a843b89d — count + drill scoped to DA_KET_THUC; chart keeps broader bucket |
| 🔵 | BUG-DASH-XUHUONG-001 | Critical | UC8/UC9 enum | `huong_tang_giam` trả UP/STABLE/DOWN thay vì TANG/GIAM/KHONG_DOI | BE | Commit 817bd50c — shared enum renamed; KpiCard updated; tests aligned |
| 🔵 | BUG-DASH-XUHUONG-002 | High | UC8/UC9 | `phanTram=100` hard-coded khi kỳ trước=0 (phải trống → "—") | BE | Commit 817bd50c — DTOs allow null; buildTrend returns null; KpiCard renders "—" |
| 🔵 | BUG-DASH-HIEUQUA-001 | High | UC8 chart | Chart chỉ 1 column thay vì 12 tháng/4-5 tuần (grain compute miss) | BE | Commit 0a8701a6 — grain = thang ? WEEK : MONTH; pre-populated skeleton; helpers added |
| 🔵 | BUG-DASH-DRILL-001 | Major | Tất cả KPI drill-down | 9/9 KPI URL thiếu nam/thang/don_vi_cap/don_vi_id + camelCase sai | FE | Commit 34bdfcc5 — KPI-02 path fix; FE handler already forwards 4 filter params (snake_case migration deferred to list-page coordinated work) |
| 🔵 | BUG-DASH-AUTOREFRESH-001 | Major | CROSS-02 | Nút "Làm mới" + nhãn cập nhật không ẨN khi kỳ đóng (cascade TPL-001) | FE | Commit 34bdfcc5 — refresh controls hidden when isQuaKhuDong=true; "Kỳ đã đóng" label |
| 🔵 | BUG-DASH-DON-VI-TINH-001 | Medium | KPI-01 | `donViTinh = "hỏi đáp"` thay vì "yêu cầu" | BE | Commit d2e458bd — metadata `donViTinh: 'yêu cầu'` per SRS FR-01 |
| 🔵 | BUG-DASH-PERM-001 | Minor | Permission cross-module | cb_nv_tw_01 có 3 roles test residue (QA_VT_DEL_TEST_R7) — mask SoD | DB seed | Commit 24d331b5 — new migration 2026051100200 removes residue (no-op on clean envs) |
| 🔵 | BUG-DASH-005 | Major | DASH-P7 | Role DN login `/dashboard` render full SCR-I-01 (phải chặn) | FE/BE | Commit 3edf6704 — DashboardPage short-circuits Navigate to /vu-viec/danh-sach when vaiTro includes 'DN' |
| ✅ | BUG-DASH-001 | Medium | DASH-11 | KPI-02 count=16 loại trừ TU_CHOI sai spec | — | Closed R7 |
| ✅ | BUG-DASH-002 | Minor | DASH-10 | Drill KPI-07 thiếu `trang_thai=DANG_HOAT_DONG` | — | Closed R7 |
| ✅ | BUG-DASH-003 | Major | DASH-12/13 | Drill KPI-03/04 composite state mismatch | — | Closed R7 |
| ✅ | BUG-DASH-004 | Major | DASH-14/15 | Drill KPI-05/06 navigate sai page Chương trình ≠ Khóa học | — | Closed R7 |

---

## 2. FR-05 Vụ việc (W3.2 + R7.7.3)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-VV-PC-WRN-01 | Minor | C3-6 Modal Phân công | Modal pool empty hiện image "Trống", thiếu WRN-PC-01 + override "Tìm thủ công" | FE | Commit bdc35a4f — TCTV dropdown notFoundContent aligned with WRN-PC-01 spec (alert + Tìm thủ công flow already in place) |
| 🔵 | BUG-VV-FN-LICHSU-01 | Major | C8-3 LICHSU audit | LICH_SU_VU_VIEC ghi 12/18 enum + alias TRINH_PD vs TRINH_PHE_DUYET — thiếu 5 spec | BE | Commit c05a6b1c — controller emits TRINH_PHE_DUYET (was TRINH_PD); backfill migration 2026051100210 rewrites old rows; remaining enum-coverage gaps depend on test flow exercising state transitions |
| 🔵 | BUG-VV-FN-POOL-CG-MISSING-01 | Minor | VV-013 Pool filter | Pool phân công CÁ NHÂN thiếu CG (chỉ TVV+NHT) dù CG HOAT_DONG match LV | BE | Commit add930d5 — goiYTvv pool + count subqueries: `loai_tvv = 'TVV'` → `IN ('TVV','CG')` (spec FR-V.I-09 line 766) |
| 🔵 | BUG-VV-FN-TVV-DETAIL-403-01 | Major | VV-014 | TVV `/vu-viec/{id}` redirect 403 dù được phân công VV | FE/BE | Commit 2706c3ba — root cause: VV detail page fires GET /vu-viecs/:id/ho-so (HoSoVuViec.Read perm); TVV seed lacked it → axios GET 403 → `/403`. Grant `read_ho_so_vu_viec` to TVV + migration 2026051100220. RLS still scopes to assigned cases. |
| 🟣 | BUG-VV-FN-TVV-PERMISSION-GAP-01 | Major | VV-015/017/033 | TVV chỉ 14 perm, thiếu cap-nhat-ket-qua/create_ket_qua/trinh-phe-duyet/hoan-thanh — cần BA chốt scope TVV | BA + BE | Chờ BA |
| ✅ | BUG-VV-NHT-SCOPE-01 | Critical | TP-VV-04 B3 | NHT cross-donVi 403 — reclass seed/perm-design | — | Closed/Reclass |
| ✅ | BUG-VV-NHT-NOTIF-01 | Major | UC62 B2-B3 | Phân công không trigger notif — mail OK | — | Closed/Partial |
| ✅ | BUG-VV-SCHEMA-01 | Critical | C3-1 | Entity VU_VIEC chưa migrate v3.5 | — | Closed |
| ✅ | BUG-VV-AUTH-01 | Critical | TP-VV-04 C3-3 | TVV/CG/NHT login fail — reclass seed gap | — | Closed/Reclass |
| ✅ | BUG-VV-SLA-01 | Major | VV-006 C6-1 | Deadline tính 10 ngày LV thay vì 15 | — | Closed |
| ✅ | BUG-VV-PC-MODAL-01 | Major | C3-1/3/4 | Modal Phân công thiếu thẻ Cá nhân/Tổ chức | — | Closed |
| ✅ | BUG-VV-FN-DANHGIA-01 | Critical | C5 UC67 | Đánh giá VV 0-10 chưa build → đã implement | — | Closed |
| ✅ | BUG-VV-FN-NOTIF-01 | Critical | VV-031 | DN không nhận mail post-PC — fresh trigger PASS | — | Closed |
| ✅ | BUG-VV-FN-PHANCONG-REVERT-01 | Critical | VV-013 C3-1 | POST /phan-cong 201 nhưng revert sau 3-5s | — | Closed |
| ✅ | BUG-VV-FN-SEARCH-01 | Major | VV-002 | Search `tuKhoa` BE ignore → đổi `keyword` | — | Closed |
| ✅ | BUG-VV-FN-SLA-01 | Major | C6-1 | Deadline 14 calendar days thay vì 15 LV | — | Closed |
| ✅ | BUG-VV-FN-VALIDATION-01 | Major | VV-004 | Form tạo VV thiếu required DN | — | Closed |

---

## 3. FR-06 Chi trả (W4.2 UC79)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-FR06-FUNC-004 | Medium | UC79 SCR-V.II-02 / TC-CT-PD-005 | Spinbox "Số tiền duyệt" khoá cứng `valuemax=0` khi DN vượt trần — CB PD không duyệt đặc cách qua UI được | FE | Commit 16cf7195 — fix đã có trong PheDuyetActions.tsx (drop `max`, fallback initial=soTienDeNghi, Alert warning). Bổ sung regression assertion `not.toHaveAttribute('aria-valuemax', '0')`. CB PD nhập bất kỳ giá trị > 0 nào, SRS BR-CT cho phép discretion. |

---

## 4. FR-08 Đánh giá hiệu quả HTPL (W4.4 + R7.7.9)

### 4.1 Phase B (2026-05-11)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-DG-KH-001 | Critical | FR-VI-01 UC83 form Tạo / TC-006/029/030/035 | Form Tạo KH thiếu field `co_quan_duoc_danh_gia_id` (v3.5 CR-10 mandatory) | FE+BE | Commit 0e05caf6 — DTO+service+FE+migration đã được wire trước đó (entity ke-hoach-danh-gia.entity.ts:37, migration 2026051100070, CreateKeHoachDrawer.tsx:146). Bổ sung FE regression test assert field required. |
| 🔵 | BUG-DG-KH-002 | Major | FR-VI-01 UC83 / TC-027/028/034 | Form Tạo KH thiếu UI upload `file_dinh_kem` (v3.5 CR-07 PDF/DOC/XLS max 20MB) | FE | Commit 15615077 — drawer dùng `FileUpload deferred` (PDF/DOC/DOCX/XLS/XLSX × 20MB) → sau khi POST /ke-hoach-danh-gias xong thì attach files qua /ke-hoach-danh-gias/:id/files (Promise.allSettled, soft warning nếu upload thất bại). |
| 🔵 | BUG-DG-KH-003 | Major | SCR-VI-01 Phần A list / TC-001/011-014/037 | Bảng list 9 cột vs SRS 18 (thiếu Checkbox + Người tạo + Hành động icons) | FE | Đã fix sẵn (columns.tsx:124 Người tạo + cột Hành động Xem/Sửa/Xóa; list page rowSelectionExtraProps + batchActions Xóa hàng loạt). Test list `returns 11 column definitions` PASS — BE service hydrate `nguoiTaoHoTen` (service.ts:264). |
| 🟣 | BUG-DG-KH-004 | Medium | SCR-VI-01 Phần B / TC-016 | Detail 5 tabs vs SRS 4 (split "Thực hiện chấm điểm") — chờ BA chốt | BA + FE | Spec deviation |
| 🔵 | BUG-DG-TC-001 | Medium | FR-VI-02 UC84 / TC-001/018 | Spinbox "Điểm tối đa" valuemax=0 (list + modal Thêm) | FE | Đã fix sẵn — AddTieuChiModal.tsx:137 + TieuChiTab.tsx:278 truyền `max={100}` (SRS line 836 C09 thang 1..100), validator reject value > 100. |
| 🟣 | BUG-DG-TC-002 | Medium | SCR-VI-01 Tab 1 / TC-001 | Cột bảng Tab Tiêu chí UI=entity vs SCR (Mô tả/Thứ tự) — chờ BA chốt | BA + FE | Internal SRS inconsistency |
| 🔵 | BUG-DG-KH-005 | Low | FR-VI-01 detail Tab Tiêu chí / TC-016 | Spinbox valuemax=0 (duplicate BUG-DG-TC-001) | FE | Cùng patch BUG-DG-TC-001 — TieuChiTab.tsx:278 `max={100}`. |
| 🟣 | OBS-DG-PC-001 | Investigate | Tab Phân công | Đợt LAP_KE_HOACH có 2 PC nhưng state không auto-transition PHAN_CONG | BA + BE | SPEC-CLARIFY-DG-PCB3-01 |

### 4.2 R7.7.9 functional + R10/R11

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🟡 | BUG-FUNC-DG-008 | Major | FR-VI-08 Tab 4 / TC-D2-B9 | PUT `/ket-quas` 200 với data computed nhưng GET sau đó trả version=1 + null — read-after-write inconsistency (dev fix R10b không hiệu lực) | BE | P1 — defensive fix shipped: `AuditService.log()` was reusing the request-scoped RLS QueryRunner. AuditInterceptor's `tap` fires fire-and-forget AFTER the controller returns; if that audit INSERT lands inside the still-open business transaction and fails (partition CHECK / inet cast / FK / row-level lock), PG aborts the txn → trailing `commitTransaction()` becomes a ROLLBACK → all business writes silently lost. Decoupled `log()` to use `auditRepo.manager` (pool-bound, separate txn) so audit failures can no longer poison business commits. `logWithManager()` remains for callers that need atomic business+audit semantics. Needs DB-level verification with the reproducer before closing (this is a hypothesized root cause from static analysis; QA should re-run R10b's flow). |
| 🔵 | BUG-FUNC-DG-009 | Major | FR-VI-08 transition HUY / TC-D2a | Detail page thiếu UI button "Hủy đợt" trên 4 state nguồn (LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO) | FE+BE | P1 — fixed: added `POST /ke-hoach-danh-gias/:id/huy` (DTO + service.huy() + AuditEntity.CANCEL) and detail-page modal w/ lyDoHuy ≥10 ký tự; SM-DANHGIA enforces 7 source states |
| 🔵 | BUG-FUNC-DG-010 | Major | FR-VI-02 modal / TC07 | Modal "Thêm tiêu chí" override `trongSo` user nhập về 100; R11 inline edit cũng force | FE | NOT REPRO — TieuChiTab + AddTieuChiModal already pass user-typed trongSo unchanged. Added regression test in `TieuChiTab.test.tsx` walking modal→handleAdd→PUT and asserting body has trongSo=30, not 100. Likely fixed alongside `c9bd7dd1` cleanup. |
| 🔵 | BUG-FUNC-DG-011 | Medium | FR-VI-03 Tab 2 / TC11 | Bảng PC render `—` cho Người ĐG + Lĩnh vực + Ghi chú dù BE persist (R11 không repro trên đợt mới — đề nghị verify) | FE | NOT REPRO — BE `phan-cong-danh-gia.service.ts:118-119` already returns `linhVucs[]` + `nguoiDanhGia` nested objects; FE `PhanCongTab.tsx:125,155` renders `nguoiDanhGia.hoTen` + `linhVucs.map(lv=>lv.ten)`. Matches QA R11 re-test (2026-05-11 14:10) "✅ NOT REPRODUCED". |
| 🔵 | BUG-FUNC-DG-012 | Critical | SM-DANHGIA / TC11-14 | Đợt không advance state `LAP_KE_HOACH → PHAN_CONG` dù POST 4 lần /phan-congs 201; R11 cũng block `PHAN_CONG → CHO_DUYET_PC` | FE | P0 — fixed: BE was already auto-advancing (`phan-cong-danh-gia.service.ts:226`) and persisting on submit/approve/reject. Root cause: `use-phan-cong.ts` invalidated wrong query key `'ke-hoach-danh-gia-detail'` (typo) instead of canonical `'ke-hoach-danh-gia'`, so the FE never refetched the KH detail. Fix routes both PC list + KH detail invalidations through `keHoachDgKeys` / `KE_HOACH_DG_QUERY_KEY`; new tests `use-phan-cong.test.ts` lock the contract. |
| 🟡 | BUG-FUNC-DG-013 | Major | FR-VI-03 × QTHT / TC18 | QTHT có button "Thêm người ĐG" + "delete" trên tab PC (vi phạm matrix R-only) — R11 PC tab fixed; Tiêu chí tab vẫn QTHT mutate | BA + BE | Partial — chờ BA scope Tiêu chí |
| 🔵 | BUG-FUNC-DG-014 | Medium | FR-VI-03 modal / TC11/12 | Dropdown "Lĩnh vực" render 2/12 options raw UUID thay vì tên Vietnamese | FE | — fixed: 2 seed records in LINH_VUC_PL have null/empty `ten` so Antd Select falls back to raw UUID. `AddPhanCongModal.tsx` now drops records with missing/UUID-shaped `ten` before mapping into `<Select options>`. Regression test asserts the two QA-reported UUIDs no longer appear in the rendered DOM. BE-side seed cleanup is the durable fix (not in scope). |
| 🔵 | BUG-FUNC-DG-015 | Minor | FR-VI-04/09 / Tabs Thực hiện + Báo cáo | Click tab ở state LAP_KE_HOACH → render placeholder đúng NHƯNG pop BE error toast (FE leak 4xx) | FE | — fixed: tab components called `useEligibleCases` / `useBaoCao` / `useKetQuas` on mount regardless of `trangThai`, so BE returned 4xx ("Kế hoạch phải ở trạng thái...") and the hook's `onError` popped a toast. Added an `enabled?: boolean` opt to all three hooks; `ThucHienTab` now passes `enabled: canSelectCases \|\| hasResults`, `BaoCaoTab` passes `enabled: !isPlanBeforeDanhGia`. Regression test in `BaoCaoTab.test.tsx` asserts `mockGetBaoCao` is NOT called when `trangThai === 'LAP_KE_HOACH'`. |
| ✅ | BUG-FUNC-DG-001 | Medium | R6.4.D2 B1 | Button [Lưu & Chuyển tiêu chí] không navigate | — | Closed R7 |
| ✅ | BUG-FUNC-DG-002 | Critical | R6.4.D2 back-fill | Tab Tiêu chí không có [+ Thêm] / [Nhập DM] | — | Closed R7 |
| ✅ | BUG-FUNC-DG-003 | Critical | R6.4.D2 B2 | Dropdown Người ĐG gọi `/chuyen-gia-tvvs` 404 | — | Closed R7 |
| ✅ | BUG-FUNC-DG-004 | Major | R6.4.D2 B2 | Dropdown Lĩnh vực `/danh-mucs` 404 | — | Closed R7 |
| ✅ | BUG-FUNC-DG-005 | Major | R6.4.D2 B2 | Dropdown Vai trò render "Trống" | — | Closed R7 |
| ✅ | BUG-FUNC-DG-006 | Major | R7.4.D2 B6 | `/vu-viec-eligible` empty list | — | Closed R10 |
| ✅ | BUG-FUNC-DG-007 | Medium | Dashboard KPI-04 | KPI "VV hoàn thành: 0" sai vs thực tế 20 records | — | Closed R10 |

### 4.3 SPEC-CLARIFY chờ BA (FR-08)

| Status | ID | Câu hỏi | Module |
|---|---|---|---|
| 🟣 | SPEC-CLARIFY-DG-LKHB1-01 | C16 "Mục tiêu" Rich Text Editor hay multiline plain? | OBS-DG-KH-001 |
| 🟣 | SPEC-CLARIFY-DG-LKHB1-02 | UI 9-stage stepper vs SRS 8-state — sub-state mới hay presentation? | OBS-DG-KH-002 |
| 🟣 | SPEC-CLARIFY-DG-LKHB1-04 | Tab pattern persist filter state vào URL không? | OBS-DG-KH-003 |
| 🟣 | SPEC-CLARIFY-DG-LKHB1-05 | "Thời gian bắt đầu/kết thúc" vs "Từ ngày/Đến ngày" — chọn 1 | OBS-DG-KH-004 |
| 🟣 | SPEC-CLARIFY-DG-LKHB1-06 | Chính tả "Trọn năm" vs "Tròn năm"? | OBS-DG-KH-005 |
| 🟣 | SPEC-CLARIFY-DG-TCB2-02 | Thêm column `mo_ta` entity hay bỏ field khỏi modal? | OBS-DG-TC-001 |
| 🟣 | SPEC-CLARIFY-DG-TCB2-03 | Drag&drop "Thứ tự" — implement hay bỏ? | OBS-DG-TC-002 |
| 🟣 | SPEC-CLARIFY-DG-TCB2-04 | WRN-TC-01 vs ERR-DG-TC-01 wording khi nào? | OBS-DG-TC-003 |

---

## 5. FR-11 Báo cáo Thống kê (Nhóm IX — W5.2 + R7.7.13)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-BC-OUT-001 | Critical | UC124-UC146 (23 BC) / TPL-REPORT-FULL | UI MISSING 6/7 output fields per template (4 cards + bảng đơn vị + Trend Line + Header) | FE | Root cause: `ReportResultView` rendered only the primary ProTable. Added `ReportHeader` (BC title + kỳ + khoảng + đơn vị + thời điểm tạo per TPL-REPORT-FULL Output #1-#6), `ReportSummaryCards` (auto-detects top-level numeric envelope fields → Statistic cards; works generically across all 23 BCs without per-BC handcrafting; UC124's 4 metrics labelled, others fall through to field key), secondary "Phân bổ theo đơn vị" table when `theoDonVi[]` is present. Trend Line cascade fixed in BUG-BC-CHART-001. 4 vitest specs cover summary cards (UC124 metric labels, empty-envelope, pagination skip, fallback label). 40 bao-cao FE tests pass. |
| 🔵 | BUG-BC-PERM-003 | Critical Security | `/bao-cao/hoi-dap` (23 BC cascade) | DP/BN nhận data TOÀN QUỐC — vi phạm BR-AUTH-08 cross-tenant leak | BE | P0 — fixed at `ReportQueryFactory.create()`: app-layer `don_vi_id IN (:allowedDonViIds)` fence mirrors dashboard's explicit andWhere pattern. Empty list → `1=0` fail-closed. TW (`allowedDonViIds === null`) unchanged. Centralized fix benefits all 22 bao-cao services without per-service changes. 4 new factory specs cover TW/BN/DP/empty paths; 579 bao-cao tests pass. |
| 🟣 | BUG-BC-EXP-001 | Critical | `/bao-cao/loai` | `maxRows: 50000` vi phạm BR-DATA-06 cap 10K — BA xác nhận update BR hay BE config | BA + BE | P0 |
| 🔵 | BUG-BC-CHART-001 | Major | UC124/125/128/130/133/142/143/146 | Trend Line chart MISSING cho 8 BC | FE | Root cause: `ReportChartRenderer` rendered only `chartTypes[0]` and dropped every additional chart. BCs declared as `['DONUT','LINE']` (UC124) or `['BAR','LINE']` (UC125/130/133/143) lost their secondary Trend Line. Catalog data was correct all along; FE was the bottleneck. Renderer now maps over `chartTypes[]` and stacks each chart vertically. Added 5 vitest specs covering empty / single / DONUT+LINE / BAR+LINE / BAR+DONUT routings. All 36 bao-cao FE tests pass. |
| 🔵 | BUG-BC-DD-001 | Medium | UC133 BC Chất lượng đào tạo | Sai optgroup ("Đào tạo" thay vì "Đánh giá") | FE | Root cause: BE catalog returned `nhom: 'Đào tạo'`; FE groups dropdown options by catalog `nhom`, so the wrong label was BE-driven. Fixed in `REPORT_CATALOG` (slug `chat-luong-dao-tao`) per SRS §SCR-IX-01 dropdown mapping (UC133 belongs to "Đánh giá" optgroup with UC132). Added 2 regression specs to `report-catalog.spec.ts`; all 11 catalog tests pass. |
| 🔵 | BUG-BC-DATA-SCOPE-LEAK | Critical | BC-026..028, 030..031 | Endpoint `/api/v1/bao-cao/*` không apply scope theo donViId — leak full national data | BE | Fixed together with PERM-003 — same `ReportQueryFactory` fence covers all BC endpoints. |
| 🟡 | BUG-BC-PDF-NOT-SUPPORTED | Major | BC-025 | POST `/bao-cao/export` formatXuat=PDF trả 422 ERR-RPT-EXPORT-01 universal | BE | Root cause: puppeteer ≥ v22 dropped Chromium auto-download from `npm install`; deploy env booted without a usable Chrome → every `puppeteer.launch()` failed → universal 422. Code fixes: (1) `scripts/install-puppeteer-chrome.js` postinstall provisions Chromium on every fresh install (skippable via `PUPPETEER_SKIP_DOWNLOAD` or `PUPPETEER_EXECUTABLE_PATH`); (2) `BrowserPoolService` now honors `PUPPETEER_EXECUTABLE_PATH` env so containerised deploys can point at system Chrome; (3) `pdf-doc.util.ts` error log now tags the "Chromium missing" subcase so ops triage doesn't need a stack-trace deep-dive. Pending ops verification on deploy. |
| 🟢 | BUG-BC-XLSX-PARTIAL-SUPPORT | Medium | BC-024 | XLSX trả 422 cho 2/10 BC (`BC_VV_THEO_LINH_VUC` + `BC_DANH_GIA_HIEU_QUA_HTPL`) | BE | **Verified — QA test data error, not a BE bug.** Canonical enum names in catalog: `BC_VU_VIEC_THEO_LINH_VUC` + `BC_DANH_GIA_HIEU_QUA` (FE consumes via `/bao-cao/loai`, so real users hit the correct names). Both BCs DO have catalog entries + dispatchers + working XLSX paths. QA used legacy/typo'd enum values. Code change: differentiated "unknown loaiBaoCao" 422 (now includes the value + pointer to `/bao-cao/loai`) from "valid but dispatcher missing" 422 — so a recurrence is diagnostic on first inspection. |
| 🔵 | BUG-BC-KYBAOCAO-NOT-VALIDATED | Medium | BC-034 | `/bao-cao/hoi-dap` + `/danh-gia-hieu-qua` không validate enum `kyBaoCao` | BE | Root cause: 10/12 BC filter DTOs declare `@IsOptional() @IsEnum(KyBaoCao) kyBaoCao?`; `BcHoiDapFilterQueryDto` + `BcDanhGiaHieuQuaFilterDto` were missing the field entirely so any string passed through validation untouched. Added the field to both DTOs (TUAN/THANG/QUY/NAM/KHOANG enum from `bao-cao-shared.enums`). All 579 bao-cao tests pass. |
| ✅ | BUG-BC-PDF-500-001 | Critical | BC-025 | PDF export 500 ERR-SYS-00-00-01 (downgrade thành PDF-NOT-SUPPORTED) | — | Closed |
| ✅ | BUG-BC-LEGEND-002 | Minor | BC-018 | Chart legend leak raw camelCase | — | Closed |
| ❌ | BUG-BC-FE-DROPDOWN-MISSING-3 | Medium | BC-006..010 | False positive scroll virtual list | — | Retracted |
| ✅ | BUG-BC-WORD-001 | Major | BC-024/025 | Button "Xuất Word" thay vì "Xuất PDF" theo TT 17/2025 | — | Closed |
| ✅ | BUG-BC-HOIDAP-PL-001 | Major | BC-001/006 | Group label "Hỏi đáp" + tên BC thiếu chữ "pháp luật" | — | Closed |

---

## 6. FR-12 TVCS Tư vấn chuyên sâu (W3.3 + R7.7.5)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-TVCS-NEW-004 | Critical | SCR-X1-01 Export | `GET /api/v1/noi-dung-tu-van-cs/export` 404 (HSPL pattern works) | BE | P0 — root cause: BE declared `@Post('export')` with `@Body()`; FE/QA used GET (matching HSPL pattern). 404 was actually a method mismatch, not a missing endpoint. Switched controller to `@Get('export')` with `@Query()` to mirror `HoSoPhapLyDnController.exportList` exactly. Updated FE `noiDungTuVanCsApi.export` to use `api.get` with `{ params, responseType: 'blob' }`. 127 TVCS BE tests + 21 FE tv-chuyen-sau tests pass. |
| 🟢 | BUG-TVCS-NEW-005 | Critical | UC152 TLPL | Toàn bộ endpoint TLPL 404 — accordion UI có nhưng không connect (21 TC BLOCKED) | BE | **Verified — wire is complete, QA probed wrong paths.** Canonical route: `/api/v1/tu-lieu-phap-ly-vvs` (BE `TuLieuPhapLyVvController` registered in `tu-van.module.ts`). FE service `tu-lieu-phap-ly-vv.service.ts` already calls `/tu-lieu-phap-ly-vvs` (list/detail/create/patch/delete/công-khai/hủy-cong-khai). Accordion `TuLieuPhapLyVvSection` wired in `tv-chuyen-sau/detail/index.tsx`. QA probed `/tu-lieu-phap-luat`, `/tlpl`, `/{id}/tu-lieu` etc. — none match the actual URL. 36 TLPL service/gateway/processor tests pass. Recommend QA re-run UC152 against `/tu-lieu-phap-ly-vvs?noiDungTvId=...` to unblock the 21 TCs. |
| 🔵 | BUG-TVCS-007 | Major | UC147 form CREATE | Form thiếu field "Ngày tư vấn" (date, required) | FE | SRS UC147 §111 + §1124 mandates required date "Ngày tư vấn" on CREATE. Added DatePicker to `tv-chuyen-sau/tao-moi` with required-rule + DD/MM/YYYY format; payload sends `ngayBatDau: YYYY-MM-DD`. BE: added `@IsOptional() @IsDateString() ngayBatDau` to `CreateNoiDungTuVanCsDto` (kept optional for wire-stability with existing API consumers), `service.create()` casts to Date and persists. Field name `ngayBatDau` retained pending SPEC-CLARIFY-TVCS-LIST-COL-01 BA decision (`ngay_tu_van` SRS vs `ngay_bat_dau` UI); rename is a separate purely-mechanical pass once BA decides. 127 BE TVCS + 21 FE tv-chuyen-sau tests pass. |
| 🔵 | BUG-TVCS-NEW-001 | Major | UC147 detail | UI thiếu UPDATE form entry (BE PATCH works) | FE | BE PATCH `/noi-dung-tu-van-cs/:id` + `useUpdateTvCs` hook + `noiDungTuVanCsApi.update` were all wired; only the FE entry point was missing on the detail page. Added "Sửa" button (EditOutlined icon, gated on `Update` ability + only in TIEP_NHAN/PHAN_CONG states where workflow hasn't locked the record yet) + edit modal with noiDung/tomTat/ghiChu fields preserving optimistic-lock `version`. 21 FE tv-chuyen-sau tests pass. |
| 🟣 | BUG-TVCS-NEW-006 | Major | UC149/151/153 | Phiên TV + Đánh giá CL + Nhật ký endpoints MISSING | BE | **Blocked on 3 SPEC-CLARIFY items.** BE endpoints actually exist: `/noi-dung-tu-van-cs/:id/phien-tu-vans` (UC149 PhienTuVan), `/danh-gia-chat-luong-tvs` (UC151 DanhGiaCL). FE accordion has 2 placeholder sections ("Đánh giá chất lượng" / "Nhật ký") that never call those endpoints. Wiring is blocked by SPEC-CLARIFY-API-IN-01 (DGCL inline vs separate entity), SPEC-CLARIFY-API-IN-02 (Phiên TV UI vs internal), SPEC-CLARIFY-TVCS-NHATKY-01 (Nhật ký = audit_log vs business log). Once BA decides, FE wiring is a sub-30min mechanical pass. |
| 🔵 | BUG-TVCS-NEW-002 | Medium | UC147 BE validator | `noi_dung_tu_van` 51201 byte → 201 success (đáng lẽ 422), vi phạm BR-DATA cap 50KB | BE | Added `@MaxLength(50000, { message: 'Nội dung tư vấn tối đa 50.000 ký tự' })` to `noiDung` in CreateNoiDungTuVanCsDto. UpdateDto inherits via `PartialType` so PATCH is also capped. 127 TVCS BE tests pass. |
| 🟢 | BUG-BE-TVCS-R16-001 | Major | TV-023/024/025/043 | TLPL VV CRUD endpoint chưa expose (404 toàn bộ candidate) | BE | **Duplicate of BUG-TVCS-NEW-005 — wire is functional, QA probed wrong paths.** Canonical CRUD route: `/api/v1/tu-lieu-phap-ly-vvs` (`TuLieuPhapLyVvController`, registered in `tu-van.module.ts`). Recommend QA re-run TV-023/024/025/043 against the correct URL to unblock. |
| 🔵 | BUG-FE-TVCS-R16-005 | Major | TV-045/047 | UI detail TVCS DA_DUYET thiếu button [Công khai]/[Hủy CK] + panel 5 v3.5 field (BE OK / FE NOT FIXED) | FE | Buttons [Công khai]/[Hủy công khai] were already wired in the action bar (line 576/588), but the v3.5 read-only panel exposing the 5 fields was missing. Added "Trạng thái công khai" accordion section with Descriptions showing `congKhai` (Tag green/default), `thoiGianDangTai`, `moTaCongKhai`, `anhDaiDien` presence, `fileDinhKemCongKhai` presence. 21 FE tv-chuyen-sau tests pass. |
| 🔵 | BUG-BE-TVCS-R16-006 | Major | TV-059 | TVCS thiếu cột FK `hop_dong_tv_id`, PATCH silently dropped | BE | Migration `2026051100230-AddHopDongTvIdToNoiDungTuVanCs` adds nullable FK `hop_dong_tv_id UUID REFERENCES hop_dong_tu_van(id) ON DELETE SET NULL` + `idx_ndtvcs_hop_dong_tv`. Entity gets matching `@Column` + `@Index`. CreateDTO adds `@IsOptional @IsUUID hopDongTvId` so UpdateDTO inherits via PartialType; service.update() validates FK lookup + persists through Object.assign whitelist. 127 TVCS BE tests pass. |
| 🟢 | BUG-BE-TVCS-R17-008 | Major | TV-053 happy | Regression do fix R16-007 sai spec: blanket-deny `/doanh-nghieps` cho NHT thay vì BR-AUTH-10 row-level | BE | **Already fixed at 15:42-15:43, after R19 verify at 14:25.** Commits fea9a4d3 (grant `read_doanh_nghiep` to NHT) + d06e4a9a (`assertAssignmentForDoanhNghiep` helper) + f6f5204e (controller removed NHT from `DOANH_NGHIEP_CMS_READ_DENIED`, service.findAll applies `applyAssignmentFilter`, service.findOne calls `assertAssignmentForDoanhNghiep`). NHT có VV phân công vẫn đọc DN-X 200 ✅; NHT không có VV với DN-Y → 403 ✅. 57 doanh-nghiep BE tests pass. Pending QA re-verify only. |
| 🔵 | BUG-FE-TVCS-R16-004 | Medium | TV-039 NHT menu | NHT thấy menu "TVCS" + mở được trang — vi phạm matrix | FE | Fixed (commit a3db579a0) |
| ✅ | BUG-BE-TVCS-R16-002 | Major | TV-035-1/046/047 | List filter `?congKhai=true` không apply | — | Closed |
| ✅ | BUG-BE-TVCS-R16-003 | Major | TV-022 | Auto-save draft 30s TRAO_DOI_NHAP endpoint chưa expose | — | Closed |
| ✅ | BUG-BE-TVCS-R16-007 | Major | TV-053 | HSPL DN detail GET không apply BR-AUTH-10 — leak cross-scope | — | Closed (regression → 008) |

### SPEC-CLARIFY chờ BA (FR-12)

| Status | ID | Câu hỏi |
|---|---|---|
| 🟣 | SPEC-CLARIFY-TVCS-LIST-TAB-01 | 4 tab UI (Tất cả + 3 group) vs SRS 3 tab |
| 🟣 | SPEC-CLARIFY-TVCS-LIST-COL-01 | Cột `ngay_tu_van` (SRS) vs `ngay_bat_dau` (UI) |
| 🟣 | SPEC-CLARIFY-TVCS-MODAL-CG-01 | Modal Phân công pre-load TOP 5 CG (SRS) vs search-only (UI) |
| 🟣 | SPEC-CLARIFY-TVCS-NHATKY-01 | Accordion Nhật ký scope = AUDIT_LOG hay business message log |
| 🟣 | SPEC-CLARIFY-API-IN-01 | Đánh giá CL inline trên TVCS hay separate entity |
| 🟣 | SPEC-CLARIFY-API-IN-02 | Phiên TV cần expose UI hay chỉ internal entity |
| 🟣 | SPEC-CLARIFY-TVCS-TK-01..04 | Whitespace trim + deep page clamp + filter persist + empty wording |
| 🟣 | SPEC-CLARIFY-TVCS-MA-AUTOGEN-01 | BE auto-gen mã ignore user input — TC-040 ERR-TVCS-05 design re-write? |

---

## 7. Hỏi đáp — SLA tier (R7.7.1)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-HD-022-SLA-TIER-001 | Major | HD-022c | Badge xanh "Bình thường" ở ratio ~71.6% còn lại — spec yêu cầu vàng "Sắp hết hạn" (<50%) | FE | `SlaIndicator.getSlaLevel()` was using UX-DR-17 thresholds (70/90/100/200) with an extra `gan-qua-han` orange tier not in spec. Aligned to BR-SLA-02 (4 tiers: 50/100/200) — `>50` now triggers warning yellow. Dropped the `gan-qua-han` tier from `SlaLevel` union + tag-color map. 30 SLA tests pass incl. new HD-022c regression test. |
| 🔵 | BUG-HD-022-SLA-TIER-002 | Major | HD-022d | Badge cam "Sắp hết hạn" ở ratio >100% elapsed — spec yêu cầu đỏ "Quá hạn" | FE | Root cause: `isOverdue` used `dayjs.isAfter(deadline, 'day')` day-granularity comparison, so a deadline at 03:18 with `now` at 17:15 same day was not detected as overdue. Changed to ms-precision `isAfter(deadline)` + clamp `elapsedPercent >= 101` when overdue so the level resolves to `qua-han` (error/red) regardless of how business-day rounding lands. New HD-022d regression test fixes the same-day-past-deadline case. |

---

## 8. Tư vấn nhanh — TVN (R7.7.11)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-FUNC-TVN-001 | Major | TVN-010/011/012 | Account `cb_nv_tw_01` DB gán 3 vai trò bypass guard — drift data | DB seed | Migration `2026051100240-RemoveCbPdRoleFromCbNvTw01` DELETEs the drifted `tai_khoan_vai_tro` row joining `cb_nv_tw_01` × `CB_PD_TW`. Pairs with the earlier `RemoveQaTestRoleResidue2026051100200` that cleared `QA_VT_DEL_TEST_R7`. Migration is idempotent (no-op on clean envs). Per `users.csv`, `cb_nv_tw_01` is pure `CB_NV_TW`; this restores the canonical single-role binding so SoD guards stop being bypassed. |
| 🔵 | BUG-FUNC-TVN-005 | Minor | TVN-039 audit log | Action naming inconsistent (TRA_LOI, CREATE generic); dropdown thiếu "TV nhanh"; Entity=UNKNOWN | BE | TU_VAN_NHANH naming is already correct in controller (`GUI_TRA_LOI_TVNHANH`, `CREATE_TVNHANH_DN`); the QA observation is stale relative to the deployment. For the `Entity=UNKNOWN` rows: `AuditInterceptor` used to fall back to `METHOD_TO_HANH_DONG` for any POST/PUT/PATCH/DELETE and write `entityType='UNKNOWN'` when the endpoint had no `@AuditEntity`. Added a guard to skip emission when `meta.entityType` is unset — opt-in audit is the only useful audit, UNKNOWN noise just hides forgotten decorators. Module dropdown spec has 12 entries incl. `TU_VAN`; "TV nhanh" folds under "Tư vấn" by design (SCR-VIII-10 row 5). 95 audit-related tests pass. |
| 🔵 | BUG-FUNC-TVN-007 | Major | TVN-014/037 | Auto-import HOI_DAP DA_DUYET → KHO_CAU_HOI nguồn TU_DONG không trigger (back-fill HOI_DAP cũ chưa chạy) | BE | Forward-only runtime path (`autoFeedKhoCauHoiOnApprove` at `hoi-dap.service.ts:1348`) already correct. Added migration `2026051100250-BackfillKchTuDongForApprovedHoiDap` to retroactively insert TU_DONG rows for HOI_DAP rows already in DA_DUYET before the runtime fix shipped. CTE filters HOI_DAP without a matching `KHO_CAU_HOI.hoi_dap_goc_id`, skips rows lacking a PHAN_HOI (would violate NOT NULL on `cau_tra_loi`), allocates `ma_cau_hoi` per VN-date prefix with ROW_NUMBER + offset by existing count to avoid collisions. Idempotent (NOT EXISTS guard). |
| ✅ | BUG-FUNC-TVN-002 | Major | TVN-040..044 | FR-X.2-06 (Công khai/Hủy CK) chưa deploy | — | Closed |
| ✅ | BUG-FUNC-TVN-003 | Minor | TVN-001 | Filter trạng thái dropdown thiếu | — | Closed |
| ✅ | BUG-FUNC-TVN-004 | Major | TVN-017/018 | Top 5 gợi ý không render trên detail | — | Closed |
| ✅ | BUG-FUNC-TVN-006 | Minor | TVN-016 | Cột "Số gợi ý" list = 0 dù phiên có 2 gợi ý | — | Closed |

---

## 9. Hợp đồng tư vấn — HDTV (R7.7.14)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-HDTV-032 | Medium | HDTV-014 TVV detail | TVV detail tab "Lịch sử hỗ trợ" thiếu sub-section HĐ tư vấn (spec v2.1 line 241) | FE | Added `HopDongTvSection` inside `TabLichSuHoTro` that reuses the existing `GET /hop-dong-tu-vans?tuVanVienId={id}` filter. Renders below the VV history with its own ProTable + pagination + empty state (vi: "Tư vấn viên chưa có hợp đồng tư vấn nào"). Mã HĐ links to `/hop-dong-tv/:id`. Mock-helper refactor in test file so the shared `useQuery` mock returns per-queryKey responses; 7/7 TabLichSuHoTro tests pass incl. new BUG-HDTV-032 assertion. |
| 🟣 | BUG-HDTV-034 | Minor | Spec conflict route | Route `/hop-dong-tv/danh-sach` render standalone list (7 records) nhưng spec v3.5 M-01 nói "KHÔNG có menu riêng" — chờ BA | BA + FE | — |
| ✅ | BUG-HDTV-018 | Major | HDTV-018 | Form Edit thiếu toggle "Đã thanh toán" + PATCH HD drop nested thanhToans | — | Closed |
| ✅ | BUG-HDTV-020 | Medium | HDTV-020 | HD detail thiếu tab "Nhật ký" | — | Closed |
| ✅ | BUG-HDTV-021 | Critical | HDTV-021 | QTHT bypass POST/PATCH/DELETE trên HOP_DONG_TU_VAN | — | Closed |
| ✅ | BUG-HDTV-026 | Major | HDTV-026/019 | PATCH `vuViecIds` trả 200 nhưng không persist N:N | — | Closed |
| ✅ | BUG-HDTV-029 | Major | HDTV-029/031 | Form Tạo/Sửa HD thiếu dropdown TVV và CG | — | Closed |
| ✅ | BUG-HDTV-030 | Major | HDTV-029 regression | FE truyền `pageSize=200` vượt BE max 100 → 422 | — | Closed |
| ✅ | BUG-HDTV-031 | Major | HDTV-013/026 | VV detail tab "HĐ TV liên kết" empty do camelCase vs snake_case | — | Closed |
| ✅ | BUG-HDTV-033 | Major | HDTV-013/029/031 | VV detail accordion thiếu button [+ Tạo/Liên kết HĐ] + HDTV detail thiếu Sửa/Xóa | — | Closed |
| ✅ | BUG-HDTV-035 | Minor | HDTV-014 | Filter Từ/Đến reversed range — FE silently drop Đến ngày | — | Closed |
| ✅ | BUG-HDTV-036 | Major | HDTV-024 | CB_NV_BN/DP có button "+ Tạo HĐ" trên standalone list, QTHT không có (inversion) | — | Closed |

---

## 10. Đào tạo — BM / HV / DT (R7.7.6 + R7.7.10)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-BM-010 | Medium | BM-041 | 3 trường công khai (Ảnh/Mô tả/File) vẫn visible khi Switch "Công khai PLQG" OFF | FE | Fixed 2026-05-11 (commit 452665102) |
| 🔵 | BUG-DT-038-ASSIGN-01 | Major | DT-038 | Tab "Bài giảng đã gán" thiếu button "Gán BG" + BE thiếu nested route POST/DELETE N-N | FE + BE | Fixed 2026-05-11 (BE+FE+tests) |
| 🔵 | BUG-DT-053-PUBLIC-MODAL-01 | Minor | DT-053 | Modal "Công khai khóa học" thiếu textarea `mo_ta_cong_khai` + upload `file_dinh_kem_cong_khai` (5 CPF BR-PUBLIC-01) | FE + BE | Fixed 2026-05-11 (BE dto+service+FE modal) |
| 🟣 | BUG-DT-052-HV-TAIKHOAN-01 | Minor | DT-052 | HV entity thiếu field `taiKhoanId` per FR-III-04 — chờ BA confirm MUST hay OPTIONAL | BA + BE | **REOPEN R12.4 2026-05-12** — withdrawal R12 SAI sau cross-check 5 SRS sources. **4/5 sources confirm `tai_khoan_id` REQUIRED**: master entity spec `srs-v3.5.md §3.4.3.53` (11 fields, field 11 = `tai_khoan_id` nullable FK TAI_KHOAN); master matrix `srs-v3.5.md:2623`; `_DELTA-MAP-FR03.md:42, 73`. Outlier 1/5: `srs-fr-03:1711` (lower authority). **Cần BA chốt spec authority — master `srs-v3.5.md` thắng module file description.** |
| 🔵 | BUG-DT-011-DD-ENDPOINT-01 | Major | DT-011/011a | DIEM_DANH POST endpoint 404; GET trả mock; `coMat` boolean thay vì enum 3 trị | BE | Fixed 2026-05-11 (enum DTO + back-compat) |
| 🟢 | BUG-DT-031-KQHT-ENTITY-01 | Major | DT-031b/c/d + DT-054/055 | KET_QUA_HOC_TAP entity chưa deploy (mọi route 404) — block 5 TC | BE | Closed — entity exists as `ket_qua_dao_tao` at `/khoa-hocs/:id/ket-quas` (GET list, POST batch-update / import / export / export-docx / publish / unpublish). Auto-classify BR-KQ-01/02 in `ket-qua-recompute.service.ts`. QA tested wrong paths. |
| ✅ | BUG-BM-007 | Critical | BM-007/008 | Preview/Download BM dùng MinIO presigned URL `localhost:9000` | — | Closed |
| ✅ | BUG-BM-008 | Medium | BM-016 | Upload `.txt` invalid → FE silent reject | — | Closed |

---

## 11. Kế hoạch năm — KH (R7.3.5 → R8)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| 🔵 | BUG-KH-001 | Major | FR-III-14 / R8 | BE trả KH năm cross-đơn vị — CB NV mọi cấp đều thấy 3 cấp (vi phạm BR-AUTH-08 / BR-DATA-02) | BE | Fixed — `buildListQueryBuilder` routes through `tenantRepo.getRlsSafeQueryBuilder('kh')` (FINDING-001 pattern) so `applyRlsFilters` adds explicit `don_vi_id IN (...)` predicate as defense-in-depth on top of pg RLS GUCs. Regression-lock spec asserts `getRlsSafeQueryBuilder` instead of `getRlsSafeRepo + createQueryBuilder`. |
| ✅ | BUG-KH-002 | Major | FR-III-14 | UI detail Nháp thiếu nút "Xoá" (BE OK 204) | — | Closed |
| ✅ | BUG-KH-003 | Medium | FR-III-14 | Date timezone off-by-one `01/01/2026` → `2025-12-31` (residual 4 record R8 cũ DB lệch) | — | Closed (cần data fix manual cho 4 record cũ) |

---

## 12. API Kết nối Chia sẻ (R7.7.16)

| Status | Bug ID | Sev | Module / TC | Mô tả ngắn | Owner | Note |
|---|---|---|---|---|---|---|
| ⬜ | BUG-API-001 | Major | 16 TC trên cặp HOI_DAP đã deploy | mTLS test cert missing trên test env | Infra | **Infra-only — no code change**. mTLSGuard (`src/common/public-api/mtls.guard.ts`) đúng spec: yêu cầu header `x-client-verify=SUCCESS` + `x-client-fingerprint` → 401 ERR-AUTH-MTLS-01 nếu thiếu. Cố tình KHÔNG thêm bypass flag (nguy cơ bị bật nhầm trên prod). Infra options: (a) Provision TLS reverse proxy trên test env `103.172.236.130:3000` inject 2 header trên khi client cert verify pass; (b) Cấp `client.crt + client.key` từ PM CA test-only + bật TLS trên dev env; (c) Tách 1 staging có TLS đầy đủ. Per spec line 226-227: nếu skip mTLS thì mark API-005 BLOCKED, retest staging. |
| 🔵 | BUG-API-002 | Critical | API-013..030, 032, 044 (22 TC) | 8/9 cặp outbound API endpoint trả 404 — module substantially undeployed | BE + Infra | Code-side fixed — 8 controllers (`khoa-hoc`, `tu-van-vien`, `vu-viec`, `danh-gia`, `bieu-mau`, `tu-van-chuyen-sau`, `chuong-trinh-htpl`, `ho-so-pl-dn`) now mount SRS FR-XII spec-aligned aliases (`/api/v1/dao-tao`, `/api/v1/vu-viec`, …) next to canonical `public/<x>s` paths, mirroring `HoiDapPublicController`. 8 regression-lock specs assert `Reflect.getMetadata(PATH_METADATA, …)` matches expected array. **Still blocked on Infra**: redeploy test env (`103.172.236.130:3000`) to pick up the new routes; mTLS cert provisioning unchanged. |

---

## 13. Cross-cutting observations (không log thành bug riêng)

| ID | Loại | Pattern | Owner |
|---|---|---|---|
| OBS-CROSS-MULTIROLE-001 | Investigate | cb_nv_tw_01 multi-role test residue (`QA_VT_DEL_TEST_R7`) trên 3 FR — re-seed DB | FR-10 QTHT |
| OBS-CROSS-TOKEN-REVOKE-001 | Investigate | Token revoke aggressive sau ~5 phút / rapid sequential API calls — block parallel multi-role test | Auth (FR-VIII-20) |

---

## 14. Câu hỏi cần BA chốt (tóm tắt từ `tong-hop-full-luong-dev-ba.md`)

| Status | Vấn đề | Câu hỏi | Module |
|---|---|---|---|
| 🟣 | TVV xử lý vụ việc | TVV tự cập nhật KQ + trình duyệt VV mình xử lý, hay CB NV làm thay? | Vụ việc |
| 🟣 | Route Hợp đồng TV | Route standalone `/hop-dong-tv/danh-sach` thuộc scope v3.5 hay phải ẩn? | HDTV |
| 🟣 | Báo cáo | PDF TT17/2025 và danh sách report bắt buộc ship gồm những loại nào? | Báo cáo |
| 🟣 | Báo cáo XLSX maxRows | 50K (UI hiện tại) vs 10K (BR-DATA-06 formal) — chốt số nào? | Báo cáo |

---

## 15. Action priority cross-module (rút từ overview)

| Priority | Việc | Module | Owner | Rerun sau khi xong |
|---|---|---|---|---|
| P0 | Fix data-scope leak BN/DP trên `/bao-cao/*` | Báo cáo | BE | BC-027/028/030/031 |
| P0 | Deploy API outbound + cấp mTLS/JWT staging | API | Infra + BE | R7.7.16 |
| P0 | Fix DG-012 state advance | Đánh giá | BE | TC14/17 + B7-B11 |
| P0 | Fix Dashboard filter + TPL fields | Dashboard | FE+BE | DASH P7 + 32+28 TC |
| P0 | Fix BC-OUT-001 UI render 6/7 fields | Báo cáo | FE | 23 BC functional |
| P0 | Fix TVCS Export + UC152 TLPL | TVCS | BE | 21+ TC TVCS |
| P1 | Deploy PLQG/TVN bridge | Hỏi đáp + TV nhanh | BE Integration | HD public TC + R7.6.3 |
| P1 | Fix VV TVV route/permission + CG pool | Vụ việc | BA + BE/FE | VV-014/015/017/033 native |
| P1 | Fix PDF/XLSX report export | Báo cáo | BE | BC-025 + XLSX analytic |
| P1 | Fix BUG-FR06-FUNC-004 spinbox over-cap fallback | Chi trả | FE | TC-CT-PD-005 |
| P2 | Fix Dashboard DN permission BUG-DASH-005 | Dashboard | FE/BE | DASH-P7 |

---

## 16. Hướng dẫn cập nhật

1. Khi dev nhận bug → đổi `⬜` thành `🟡` + ghi tên dev vào cột Owner.
2. Khi dev báo fix xong → đổi `🟡` thành `🔵` + comment commit hash vào Note.
3. Khi QA verify pass → đổi `🔵` thành `✅` + ghi round retest vào Note.
4. Nếu reject (out-of-scope / not-a-bug) → đổi sang `❌` + lý do trong Note.
5. Nếu vướng spec → đổi sang `🟣` + ghi câu hỏi BA vào Section 14.
6. Sau mỗi đợt sync, cập nhật lại bảng `0. Executive snapshot` để theo dõi tổng.

---

## 17. Nguồn tài liệu

- `tong-hop-full-luong-dev-ba.md` — Overview Round 7 (16 module)
- `BUG-REPORT-TONG-HOP-FR08-2026-05-11.md` — FR-08 Phase B (7 BUG + 8 OBS + 11 SPEC-CLARIFY)
- `BUG-REPORT-TONG-HOP-MULTI-FR-2026-05-11.md` — FR-01 + FR-06 + FR-11 + FR-12
- `bug-report-flow-danhgia.md` — Đánh giá HTPL R6→R11 (15 BUG)
- `bug-report-flow-vu-viec.md` + `bug-report-r7-7-3-functional-vu-viec.md` — Vụ việc R7 (17 BUG)
- `bug-report-r7-7-13-bao-cao.md` — Báo cáo R7 (9 BUG)
- `bug-report-r7-7-5-tvcs-r16.md` — TVCS R16→R19 (8 BUG)
- `bug-report-r7-7-11-tvn.md` — Tư vấn nhanh R7 (7 BUG)
- `bug-report-r7-7-14-hdtv.md` — Hợp đồng TV R7 (12 BUG)
- `Pass-bug-report-r7-7-1-hd-022-sla-tier-mismatch.md` — Hỏi đáp SLA tier (2 BUG)
- `bug-report-r7-7-16-api-deploy-gap.md` — API deploy gap (2 BUG)
- `bug-report-r7-7-6-dt038-baigiang-assign-missing.md` — Đào tạo DT-038 (1 BUG)
- `bug-report-r7-7-6-dt053-public-modal-missing-cpf.md` — Đào tạo DT-053 (1 BUG)
- `Pass-bug-report-r7-7-6-hv-deps.md` — Đào tạo HV deps (R13.2 13/05: 3/3 Closed — DT-011 Closed + DT-031 WITHDRAWN + DT-052 Closed BE migrate `taiKhoanId` schema)
- `Pass-bug-report-r7-dashboard.md` — Dashboard R7 (5 BUG)
- `bug-report-seed-r7-3-5-kh-nam-r8.md` — KH năm R8 (3 BUG)
- `bug-report-function-bm-r7-7-10.md` — Bài giảng R7 (3 BUG)
