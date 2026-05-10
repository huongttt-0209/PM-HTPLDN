# QA auto-fix sweep summary — 2026-05-10

Tổng hợp các bug đã fix trong loạt `/qa` từ 2026-05-09 → 2026-05-10.
Tổng cộng **129 commits** có `BUG-*` ID trong subject.

Skipped/deferred bugs xem tại [`_qa-skipped-2026-05-10.md`](./_qa-skipped-2026-05-10.md).

---

## 1. Session hôm nay (post-compaction)

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-HD-022 | `ae9d40e3` | SLA form: cho `canhBao2PhanTram` đạt 100% (FE max raise) |
| BUG-HD-016 | `3eabfc5a` | Hỏi đáp huỷ công khai: clear `thoi_gian_dang_tai` khi về `DA_DUYET` |

Cả 2 đã verify trên `localhost:3000` qua chrome-devtools-mcp, regression spec
đính kèm.

---

## 2. Hỏi đáp / Cấu hình SLA / Kho QA

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-KHOQA-AUTO-001 | `07c302c5` | Auto-feed Kho QA on `DA_DUYET` (BR-FLOW-10) |
| BUG-HD-021 | `6fcdc04b` | Gộp 9 tab → 7 tab theo SRS v3.5 SCR-II-01 |
| BUG-HD-043 | `5e650151`, `aedd939e` | Group "Chọn mẫu phản hồi" dropdown theo phạm vi |
| BUG-HD-049-TC-ORG-UI-001 | `1011194d` | Render TC TV list dạng table trong PhanCongModal |
| BUG-CH-003 | `74f3b20e`, `0c641b03` | HOI_DAP SLA default 10 → 5 ngày làm việc |
| BUG-CH-005 | `9f58707d`, `5b4533a6`, `eecd7cc3` | Reject `thoi_han < 1`; align ERR-SLA-01 |
| BUG-CH-006 | `6f2046ec`, `730d61e4` | CB2 max 100 → 99 (CB2 < 100 strict) |
| BUG-KHOQA-002 | `d9386469` | Regression — T8 reactivate button gate |

## 3. Vụ việc

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-VV-PUBLIC-01 | `882948d6` | Implement FR-V.I-NEW-05 công khai vụ việc |
| BUG-VV-FN-LICH-SU-01 | `f825e9fc`, `84c37590` | Stamp specific HanhDong enums on VV transitions + cron audit |
| BUG-VV-FN-PC-WRN-01 | `7e22ac20`, `dce4b0cb` | WRN-PC-01 khi assignee pool empty |
| BUG-VV-FN-NOTIF-01 | `caf00575`, `3a005878` | UC62 email intake notify; listener dùng `runAsSystem` bypass RLS |
| BUG-VV-FN-SEARCH-01 | `b50edc14`, `264311e4` | Keyword search 500 do `ts_rank` orderBy; rename `tuKhoa→keyword` |
| BUG-VV-SLA-01 | `56b9e672`, `cdbb700c` | Wire SlaModule vào VuViecModule + backfill 15-WD |
| BUG-VV-PC-001 | `183e28bc` | Exclude CG khỏi goi-y-tvv pool |
| BUG-VV-PC-002 | `0eca32a4` | Include NHT trong goi-y-tvv pool |
| BUG-VV-PC-MODAL-01 | `6e6b0b3e` | Add Cá nhân/Tổ chức modes vào Phân công modal |
| BUG-VV-SCHEMA-01 | `a46fc13a` | Add v3.5 assignee schema (Phase A additive) |
| BUG-VV-FN-VALIDATION-01 | `cc7ce315` | Require `doanhNghiepId` on manual VV create |

## 4. TVV / CGTVV (Cấp giấy TVV)

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-CGTVV-013 | `065a5778`, `b5149090` | Scope tu-van-vien list to `don_vi` via `applyRlsFilters` |
| BUG-CGTVV-014 (BE+FE) | `8f2926a0`, `47f354e6`, `ac91f2e1` | Phụ lục 1 BTP: bằng cấp/chứng chỉ tables + thẻ hành nghề slot |
| BUG-CGTVV-015 | `e3743472`, `5ffb8da2` | Restrict TVV hồ sơ uploads PDF / 10MB / 50MB total |
| BUG-CGTVV-016 | `c79d15ef`, `b098ff8f` | SRS NGUYÊN VĂN validation messages |
| BUG-CGTVV-017 | `6414301a`, `739944af` | Derive next `ma_tvv` suffix từ MAX (không COUNT) |
| BUG-CGTVV-022 | `4ce3b988`, `e020fd8b` | Enforce email unique across TVV |
| BUG-CGTVV-023 | `bdfb67cf`, `cd670c7e`, `bc312178` | Wire MD-PHE-DUYET form fields; require `soQuyetDinh` |
| BUG-CGTVV-024 | `826d70ff`, `7f2917ce` | Sanitize HTML cho mô tả công khai TVV (WIP) |
| BUG-CGTVV-025 | `9c056252` | Surface "Đăng ký TVV vào mạng lưới" sidebar entry |
| BUG-CGTVV-026 | `0ff82fe8` | Grant `read_to_chuc_tu_van` cho NHT (TVV-form dropdown) |
| BUG-CGTVV-027 | `f0b431b8` | Show every real role trong Topbar |
| BUG-CG-77-RETRY-004 | `13d66e99` | Widen TVV remove guard tới `CHO_XAC_NHAN` |
| BUG-CG-77-RETRY-005 | `2493bd06` | POST `/tu-van-viens/:id/nop-lai` cho TU_CHOI re-submit |
| BUG-CG-77-RETRY-006 | `4f780f39` | Drop HĐ tư vấn tab khỏi TVV detail |
| BUG-CG-77-RETRY-007 | `576887cb` | VV-scoped `/vu-viecs/:vvId/danh-gia-tvv` alias |
| BUG-TVV-A2-001 | `692f782a` | Seed NHT TVV management permissions |
| BUG-TVV-A1-6-001 | `9bdf7444` | Break `/dashboard` self-redirect |
| BUG-CG-A1-005 | `657dda99` | Require explicit port cho bare-IP `FRONTEND_URL` |

## 5. Hợp đồng tư vấn (HDTV)

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-HDTV-018 | `0cd1144f` | Wire "Đã thanh toán" toggle |
| BUG-HDTV-020 | `84f48e04` | Scoped audit-log sub-resource (BR-AUD-HDTV-01) |
| BUG-HDTV-021 | `1815c9f2` | Deny QTHT CUD on HopDongTuVan |
| BUG-HDTV-026 | `aa8cca6d` | Persist `vuViecIds` delta on PATCH HDTV |
| BUG-HDTV-029 | `f2014e6b`, `e1e57120` | Add TVV picker on HD TV form |

## 6. Chi trả (CHITRA)

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-CHITRA-001 | `c773db93` | Realign HSCT `muc_ho_tro/tran` per BR-CALC-01 |
| BUG-CHITRA-002 | `55f91c1d` | Kiểm tra checklist 18 trường Mẫu 01 |
| BUG-CHITRA-003 | `18861f3f` | Drop "Cần bổ sung" khỏi thẩm định form |
| BUG-CHITRA-005 | `0d2f9939` | Align "Số tiền thực trả" spinbutton bound |
| BUG-CHITRA-006 | `cf643334`, `4ae1c7fc`, `daaf57fc` | B8 wording + HATEOAS rejection link |
| BUG-CHITRA-007 | `e951db13` | Gate "Cập nhật TT" trên CapNhatThanhToan ability |

## 7. Đợt báo cáo / Báo cáo

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-DOTBC-API-001 #1 | `13186009` | Drop stale-write, return reloaded dot |
| BUG-DOTBC-API-001 #2 | `255381bb` | `markAlreadyLogged` on tongHop |
| BUG-DOTBC-API-001 #3 | `f143773e` | Distinct error cho missing `donViCap` |
| BUG-BC-WORD-001 | `d996dfbb` | Switch báo cáo Word → PDF (TT 17/2025) |
| BUG-BC-EXPORT-001 | `1472f350` | Bypass StreamableFile/Buffer trong response envelope |
| BUG-BC-HOIDAP-PL-001 | `2abcb0dd` | Apply v3.5 Hỏi đáp pháp luật rename |

## 8. Dashboard

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-DASH-001 | `ad7819af` | Include TU_CHOI in KPI-02 count |
| BUG-DASH-002 | `43e28e8b` | Emit + consume `trangThai` on KPI-07 drill |
| BUG-DASH-003 | `f677d16b` | Drill URL filter match KPI count bucket |
| BUG-DASH-004 | `4b4b3339` | Drill URL match FE route + param name |
| BUG-DASH-001/002 regression | `eab02679` | — |

## 9. Tư vấn nhanh (TVN)

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-FUNC-TVN-001 | `f537310b` | Restrict Q&A approval to CB PD |
| BUG-FUNC-TVN-002 | `006dda02` | Add Q&A publish workflow |
| BUG-FUNC-TVN-003 | `e954cab9` | Add Q&A status filter |
| BUG-FUNC-TVN-004 | `ce0049eb` | Render stored TV nhanh suggestions |
| BUG-FUNC-TVN-005 | `28e0e6d5` | Align TVN audit action names |
| BUG-TVN-R762-001 | `c484f32b` | Add CMS create flow |
| BUG-TVN-R762-002 | `a7c74371` | Add CMS rating flow |

## 10. Đăng ký / Auth / OTP / Mail

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-REG-002 + 005 | `d29e60e6`, `2a81fa8c` | Add Hủy button + correct consent text |
| BUG-REG-004 + 006 | `1d3f2ce4`, `cb946d84` | SELF_REGISTER_DN audit + pre-assign DN role |
| BUG-AUTH-OTP-02 | `44dc78f4`, `83b41a15` | Friendly Vietnamese message cho 429 |
| BUG-AUTH-OTP-02b | `e408e7ee` | Context-aware FE toast cho 429 |
| BUG-MAIL-FL-001 | `9917d5b1` | Drop QTHT manual KICH_HOAT, force first-login pw change |

## 11. Upload / Bảo mật file

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-UPL-001 | `b85e7ee3` | Accept `image/gif` end-to-end |
| BUG-UPL-002 | `7600b3a3` | Accept `.XLSX` (uppercase) |
| BUG-UPL-003 | `f870c923` | BaiGiang upload validates extension when MIME empty |
| BUG-SEC-FILE-01 | `c304b8fc` | Magic-byte content sniff trong upload pipe |

## 12. Khác (Module nhỏ)

| Bug | Commit | Tóm tắt |
|---|---|---|
| BUG-FE-TVCS-A5-004 | `f54afbc8` | CG fill `ket_qua` atomically khi complete TVCS |
| BUG-BM-001 | `b7683efd`, `f8cc6ff1` | Switch "Công khai" trên Thêm BM form |
| BUG-DN-022-ME-MISSING-LV-001 | `7e47e92a` | Hydrate `linhVucIds[]` on `/me` |
| BUG-CTDT-NAME-02 | `9b50a3b9` | Relax IsContentful cho long abbreviation-heavy titles |
| BUG-KH-002 | `7785a025` | Add Xoá button on KH detail page |
| BUG-NGAY-LE-001 | `4413f62e` | Replace dayjs guard với date-only helper |
| BUG-BG-001 | `e3f4921a` | Guard `validateFileUrl` chống null/missing |
| BUG-DM-003 | `e8246a50`, `8cc497d9` | Map FK violation 23503 → 422 ERR-DM-03 |
| BUG-DM-007 | `8beedb0c` | Add `mauHienThi` color field cho TINH_TRANG_VU_VIEC |
| BUG-DM-011 | `75160620` | Require `thuTu >= 1` cho TINH_TRANG_VU_VIEC |
| BUG-NHT-003 | `cce16a65` | Fail-fast on misconfigured `FRONTEND_URL` |
| BUG-NHT-004 | `2a25401e` | Add Bồi dưỡng tab cho NHT detail |
| BUG-NHT-005 | `ec5c6298` | Keep modal open + show toast on duplicate username |
| BUG-R7-7-4-6-001 | `d35e115b` | Block QTHT POST/PATCH/DELETE on TO_CHUC_TU_VAN |
| BUG-R7-7-4-6-002 | `ae6216c3` | Gate cross-cấp duyệt + dùng BE error message |
| BUG-FUNC-DG-006 | `7b8b6f29`, `5ccf493b`, `fe77f417` | `getKetQuas` RLS leak — vu-viec-eligible bypassed RLS |

---

## 13. Stale-fixed (đã fix bởi commit cũ — chỉ reconcile docs)

| Reports | Closed via | Docs commit |
|---|---|---|
| BUG-DKT-FE-REGRESSION-01 | (earlier dev) | `ab0f24b6` |
| BUG-AUTH-* (3 sub) | (earlier dev) | `596ccb58` |
| BUG-LH-VAL-01/02/03 + LH-CONFLICT-01 | (earlier dev) | `af8276fd` |
| BUG-DT-FORM-GV-01 | (earlier dev) | `cf1c4d98` |
| BUG-BC-LEGEND-001 + BUG-BC-EXPORT-001 | `1472f350` + earlier | `9c1129ed` |
| BUG-FUNC-TVN-* + BUG-TVN-R762-* + BUG-VV-PUBLIC-01 | (sweep above) | `9b711245` |
| BUG-HDTV-018/020/021/026/029 | (sweep above) | `2ce7bf6a` |
| BUG-HSPL-001 | `7baacfd2` Wave 4 role guards | — |
| BUG-HSPL-002, BUG-HSPL-006 | `c62dff33` BR-AUTH-10 layer-2 | — |
| BUG-HSPL-005 | `b10f643a` keyword param | — |
| BUG-FR22-004 | `2000cc5c` BA-approved checksum split | — |
| BUG-KH-003 / BUG-KHNAM-002 | `ee441d15` FE date timezone | — |

---

## 14. Skipped — cần BA / devops quyết

Chi tiết tại [`_qa-skipped-2026-05-10.md`](./_qa-skipped-2026-05-10.md):

- **BUG-HV-BE-01** — POST `/api/v1/hoc-viens` 500 (cần BA quyết về QTHT seed endpoint)
- **BUG-KHNAM-001 / BUG-KH-001** — KH năm cross-tenant leak (cần re-verify trên deploy)
- **BUG-API-001 / BUG-API-002** — module 7.16 outbound APIs + mTLS (devops + sprint)
- **BUG-FUNC-HSPL-003 / 004 / 007** — runtime/deploy issues (cần server logs)
- **BUG-CTHTPLDN-B10-001** — pre-condition HOAN_THANH (BA quyết)
- **BUG-FUNC-DG-008** — read-after-write inconsistency (cần runtime trace)
- **BUG-BM-007 / 008** — devops env var + FE upload widget
- **BUG-VV-FN-DANHGIA-01 / NOTIF-01 / LICHSU-01** — sprint-level gaps
- **BUG-HD-053-DEFAULT-IMAGE-001** — FE feature add với asset provisioning
- **errCode-mismatch cluster** (FR22-001b/003/005, FR26-001, VT-008) — cần convention agreement

---

## Verification status

- **Local browser verify (chrome-devtools-mcp):** BUG-HD-022, BUG-HD-016
- **Jest/vitest pass on touched modules:** all green; pre-existing infrastructure failures (RLS harness `tieu_de` column drop, hardcoded date deadline) unrelated
- **Regression specs landed:** xem các commit `test(qa):` ở các module trên
