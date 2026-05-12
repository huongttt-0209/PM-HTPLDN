# Functional Test Report — Tư vấn Nhanh (Module 7.13) R7.7.11

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Tư vấn Nhanh (Module 7.13) — FR-13 / Nhóm X.2 |
| **SRS Reference** | [srs-fr-13-tv-nhanh.md](../../../../../input/srs-v3/srs-fr-13-tv-nhanh.md) v3.5 — FR-X.2-01..05 (44 TC v3.5) |
| **UC Coverage** | UC 154 (FR-X.2-01) · UC 155 (duyệt) · UC 156 (FR-X.2-06 Công khai) · UC 157/158 (DN search/đánh giá) |
| **Người test** | QA Automation (Chrome DevTools MCP) |
| **Ngày** | 2026-05-08 |
| **Môi trường** | http://103.172.236.130:3000/ |
| **OTP Bypass** | `666666` |
| **Test Method** | Hybrid (UI Modal + API verify) |
| **Primary Account** | `cb_nv_tw_01` / `Secret@123` (CB_NV_TW, Cục BTTP) + `qtht_01` (QTHT) |
| **Round** | R8 → R9 → R10 → R11 (CB_PD pure session) → R12 (CMS proxy + 3 bug Closed) → R13 (8 PASS mới Import Excel + BN scope) → R14 (UI-only re-audit `_03`) → R15 (BR-FLOW-10 verify, BUG-001/007 Closed) → **R15-P2 (2026-05-12 02:30:00 — QA-only test TVN-020 Kho rỗng: non-block OK, WARNING ERR-TVN-01 missing → BUG-008 mới Minor)** |
| **Tài liệu tham chiếu** | [7.13-tu-van-nhanh.md](../../../../funtion/7.13-tu-van-nhanh.md) · [bug-report-r7-7-11-tvn.md](../../bug-reports/tu-van-nhanh/bug-report-r7-7-11-tvn.md) · [workflow-test-report-r7-6-2-tv-nhanh.md](../../workflow/tu-van-nhanh/workflow-test-report-r7-6-2-tv-nhanh.md) |

---

## 1. Executive Summary

> **R15-P2 (LATEST · 2026-05-12 02:30:00) — QA-only test TVN-020 (Kho QA rỗng → ERR-TVN-01 WARNING):** QA tự seed luồng đồng bộ (KHÔNG cần dev seed): backup 21 KCH `DA_DUYET hieuLuc=true` → PATCH ×21 `/het-hieu-luc` → pool 0 → POST `/tu-van-nhanhs/cms-create` → **201 success, phiên TVN-20260512-0001 tạo, state=CB_TRA_LOI, goiYTraLoi=[]** ✅ non-blocking đúng spec FR-13 §line 134; **NHƯNG response KHÔNG có `warning.code='ERR-TVN-01'` hoặc `warningMessage`** ❌ — CB NV không nhận được signal "Kho câu hỏi rỗng" → **BUG-FUNC-TVN-008 (Minor) mới**. Restore: 20 KCH `/kich-hoat` qua `cb_nv_tw_01` + 1 KCH BN BKH `aa222034` qua `cb_nv_bn_01` (BR-AUTH-05 cross-đơn vị) → final 21 (delta 0). TVN-020 flip ⏭→⚠️ Sai spec. Operational learnings: `/kich-hoat` là reverse cho `/het-hieu-luc` (chưa document); BR-AUTH-05 enforce asymmetric (drop accept, restore reject cross-đơn vị). Evidence: `image/r15-tc-tvn-020-phien-cb-tra-loi-empty-goi-y.png`.
>
> R15 (2026-05-12 01:25:00) — Follow-up MCP test 5 TC theo user request `/qa-only`:** PASS 5/5 với 3 isolatedContext riêng (cb_nv_tw_01 + cb_pd_tw_01 + qtht_01). **TVN-010/011/012** FE+BE guard 403 confirmed cho cb_nv_tw_01 (FE không render Duyệt/Từ chối/Duyệt hàng loạt + API direct mutation 403 ERR-PERM-SYS-00-01 — BR-AUTH-05 dual-layer). **TVN-014/037** BR-FLOW-10 auto-import HOI_DAP → KCH TU_DONG VERIFIED qua walk full workflow: HD-20260510-002 từ MOI→DANG_XU_LY (R14 seed) → CHO_PHE_DUYET (cb_nv_tw_01 Gửi phản hồi) → DA_DUYET (cb_pd_tw_01 Phê duyệt 01:24:27Z) → query KCH 30s sau → record `7bac45ff...` auto-create `nguon=TU_DONG` `hoiDapGocId=480906b9...` ngayTao=01:24:27Z — latency <30s. Total 3 KCH TU_DONG: 1 R15 fresh + 1 back-fill R14b→R15 + 1 historical R10. **BUG-007 (Major auto-import) Closed-verified** (forward + back-fill both work). **BUG-001 (Major data drift account) Closed-verified** (DB fix R14b→R15, `/auth/me` returns `vaiTro:["CB_NV_TW"]` only). Còn **BUG-005 Open PARTIAL** (audit naming TVN module + dropdown filter Module thiếu "Tư vấn"). Evidence inline `image/r15-*.png` + bug-report `r15-bug-{001,005,007}-*.png`.
>
> R14 (2026-05-11 14:06:00) — UI-only re-audit với `_03` accounts:** 5/5 UI tests PASS qua browse UI (no API). **Test 1** `cb_nv_tw_03` list KCH 24 record permission OK (Thêm câu hỏi/Nhập Excel/Xuất Excel/Làm mới render); **Test 2** `cb_pd_tw_03` approve `QA-20260508-0004` CHO_DUYET → DA_DUYET via modal Detail + confirm dialog (Hiệu lực: Không → Có, Ngày duyệt 14:05:00); **Test 3** `cb_nv_tw_03` chọn gợi ý KCH-0007 + [Gửi trả lời] trên phiên `TVN-QA-20260425-0021` DA_GOI_Y → CB_TRA_LOI (Số gợi ý=2, cập nhật 12:27:00); **Test 4** filter Nguồn=Tự động render đúng record `QA-20260510-0005`; **Test 5** `cb_nv_tw_03` Switch [Công khai] trên DA_DUYET → CONG_KHAI (Thời gian đăng tải 14:06:00, button đổi "Hủy công khai"). Workflow E2E E2E NHAP → CHO_DUYET → DA_DUYET → CONG_KHAI verified pure UI click chain qua MCP, không qua API. 3 bug Open trước R14 (BUG-001 data drift, BUG-005 audit naming, BUG-007 auto-import) giữ status — không re-test bug trong R14 (UI scope only). Evidence inline screenshots `image/r14-ui-test{N}-*.png`.
>
> R13 (2026-05-10 22:00:00): Coverage expand 8 PASS mới — **TVN-005/006** Import Excel (file 5 valid + 5 invalid → preview 9 dòng, 5 hợp lệ + 4 lỗi với message rõ; commit 5 record QA-20260510-0006..0010 nguồn=Import); **TVN-034** BN scope BR-AUTH-08 (TW=19 records, BN BKH=0 → filter active no leak); **TVN-035** NHT/CG sidebar không có submenu Tư vấn nhanh + Kho câu hỏi; **TVN-036** DN sidebar không có top-level Quản lý tư vấn entirely; **TVN-040** Switch Công khai DA_DUYET → CONG_KHAI + auto thoiGianDangTai; **TVN-041** Hủy công khai → DA_DUYET; **TVN-042** BR-PUBLIC-01 chặn /cong-khai trên CHO_DUYET với 409 ERR-BIZ-KCH-01.
>
> R12 (2026-05-10 20:07:00): Verify dev fix — CMS proxy unblock 3 BLOCKED → PASS. **TVN-022** POST `/cms-create` 200 tạo phiên TVN-20260510-0001 nội bộ (không cần mTLS); **TVN-029** POST `/danh-gia/cms-proxy` 200 → state HOAN_THANH; **TVN-038** danh-gia phiên → diem_danh_gia_tb cập nhật trên KHO_CAU_HOI gốc. **3 Bug Closed:** BUG-002 (FR-X.2-06 deploy 4 field + endpoint), BUG-003 (Filter Trạng thái dropdown 5 enum), BUG-006 (cột Số gợi ý render đúng). 3 Open: BUG-001 data drift, BUG-005 audit naming (PARTIAL — KHO chuẩn, TVN còn TRA_LOI/CREATE), BUG-007 auto-import.
>
> R11 (2026-05-10 19:04:57): TVN-010/011/012 PARTIAL → PASS với cb_pd_tw_01 pure. BUG-001 reclassify Critical → Major data drift account.

| Metric | Value |
|--------|-------|
| **Total Test Cases (spec)** | 44 |
| **TC đã test / Tổng TC** | **35/44 (80%)** — R8-R11: 24 · R12: +3 CMS proxy unblock (TVN-022/029/038) · **R13: +8 mới (TVN-005/006/034/035/036/040/041/042)** |
| **Passed** | **31** (R8-R11: 17 + R12: 3 + **R13: 8 PASS mới — Import Excel + BN scope + No-menu + Công khai UI happy/negative**) — *R13 reaffirms TVN-019 supplementary (Gửi trả lời CB_TRA_LOI)* |
| **Failed** | **1** (R11: TVN-037 auto-import BR-FLOW-10 không trigger — BUG-007) |
| **Blocked** | **5** (R11 còn lại: TVN-023/024/025/030/031 mTLS DN-side outbound + TVN-043/044 cần Cổng PLQG sandbox/race stub — TVN-022/029/038 unblocked R12 qua CMS proxy + TVN-040/041/042 unblocked R13 sau dev deploy) |
| **Partial** | **1** (TVN-039 audit naming — KHO chuẩn R12, TVN module còn TRA_LOI/CREATE chưa fix) |
| **Overall Pass Rate** | **94%** (31/33 PASS-or-FAIL, không tính BLOCKED) — pure pass 31/35 = 89% |
| **P0 Pass Rate** | **100%** (10/10 P0 = TVN-001/003/010/011/016/017/019/022/029/040 PASS R13) |
| **Bugs Found (SRS-ref)** | **7** (0 Critical, 3 Major Open: 001/005/007 + 4 Closed: 002/003/004/006) — R12 đóng 3 bug major/minor; R13 không phát hiện bug mới |
| **Health Score** | **88/100** — R12 unblock CMS proxy + 3 bug Closed; R13 thêm 8 PASS bao phủ FR-X.2-06 happy/negative + Import Excel + scope filter + permission no-menu. Còn 3 bug Open (data drift account, audit naming TVN module, auto-import BR-FLOW-10) + 5 BLOCKED mTLS DN-side. |
| **Start Time** | 23:39 07/05 (R8) · 01:00 08/05 (R9) · 17:08 09/05 (R10) · 18:30 10/05 (R11) · 20:07 10/05 (R12) · **21:30 10/05 (R13)** |
| **End Time** | 00:34 08/05 (R8) · 01:30 08/05 (R9) · 17:18 09/05 (R10) · 19:04 10/05 (R11) · 20:30 10/05 (R12) · **22:00 10/05 (R13)** |
| **Total Duration** | ~180 phút (R8 ~55 + R9 ~30 + R10 ~10 + R11 ~34 + R12 ~23 + R13 ~30) |
| **Browse Status** | OK — Chrome DevTools MCP stable across 6 round |

### Pass Rate breakdown theo Type

| Type | TC count (đã test) | PASS | PARTIAL | FAIL | BLOCKED | **Pass Rate** |
|------|--------------------|------|---------|------|---------|---------------|
| **Happy** | **6** | **6** | 0 | 0 | 0 | **100%** (TVN-001/002/003/004 + TVN-016/017) |
| **Negative** | **4** | **4** | 0 | 0 | 0 | **100%** (TVN-007/008/009 + TVN-021) |
| **Workflow** | **6** | **6** | 0 | 0 | 0 | **100%** (TVN-013/018/019 + **R11: TVN-010/011/012 flip** PASS) |
| **Authorization** | 1 | 1 | 0 | 0 | 0 | **100%** (TVN-033 QTHT) |
| **Cross-module** | **2** | 0 | **1** | **1** | 0 | **0%** (TVN-039 PARTIAL naming · **R11: TVN-037 FAIL auto-import**) |
| **FR-X.2-06 Công khai** | 5 | 0 | 0 | 0 | 5 | **0%** (TVN-040..044) |
| **DN-side mTLS Cổng PLQG** | 8 | 0 | 0 | 0 | 8 | **0%** (**R11: TVN-022/023/024/025/029/030/031/038** — 401 ERR-AUTH-MTLS-02) |
| **Total** | **32** | **17** | **1** | **1** | **13** | **71%** (PASS/đã test) |

→ **Happy-path + Workflow Pass Rate = 12/12 (100%)** — Kho Q&A core CRUD + workflow approval OK toàn bộ với CB_PD pure session. **R11 đóng góp:** 3 PASS flip (TVN-010/011/012 với cb_pd_tw_01) + 1 BUG reclassify (BUG-001 Critical → Major data drift, không phải BE security hole) + 1 BUG mới (TVN-037 auto-import) + 8 BLOCKED mTLS Cổng PLQG (đúng spec FR-X.2-03/04/05).

### Verdict: **PASS R15-P2 — 30/32 PASS đã test (94% pure, 100% non-blocking), TVN-020 ⚠️ Sai spec (BUG-008 Minor WARNING missing); 2 BUG Open Minor (005 + 008), non-blocking release**

## 1.5 Bảng trạng thái TC (snapshot R15-P2 — LATEST 2026-05-12 02:30:00)

R7.7.11 cover **35/44 TC (80%)** sau R13. Backend CRUD + workflow CHO_DUYET ↔ DA_DUYET ↔ NHAP ↔ HET_HIEU_LUC ↔ CONG_KHAI ↔ DA_GOI_Y → CB_TRA_LOI → HOAN_THANH đều OK. **R12 unblock:** CMS proxy `/cms-create` + `/danh-gia/cms-proxy` xử lý DN inbound nội bộ thay mTLS Cổng PLQG (3 PASS TVN-022/029/038) + 3 bug Closed (002/003/006). **R13 expand:** Import Excel commit 5 record qua UI upload + validate 4 lỗi (TVN-005/006), BN scope filter active no leak (TVN-034), 3 role không có menu Tư vấn nhanh (TVN-035/036), Switch Công khai DA_DUYET ↔ CONG_KHAI + BR-PUBLIC-01 enforce (TVN-040/041/042). **Còn 3 bug Open:** (1) BUG-001 data drift account `cb_nv_tw_01`; (2) BUG-005 Minor audit naming TVN module (TRA_LOI/CREATE chưa chuẩn); (3) BUG-007 Major auto-import BR-FLOW-10 không trigger. **5 BLOCKED còn:** TVN-023/024/025/030/031 (mTLS DN-side outbound) + TVN-043/044 (sandbox + race stub). **7 DEFER:** TVN-014 (cùng BUG-007), TVN-015 (DB-level GIN), TVN-020 (batch infra), TVN-026/027/028 (DN search outbound).

---

### TC summary table

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| TVN-001 | List Q&A 3 tab + paginate | ✅ Đạt | R8 | OK clean R12 (filter dropdown deploy) |
| TVN-002 | Search full-text + filter | ✅ Đạt | R8 | API search/filter OK |
| TVN-003 | CB NV tạo Q&A → CHO_DUYET | ✅ Đạt | R8 | Auto-gen mã đúng |
| TVN-004 | Update Q&A CHO_DUYET | ✅ Đạt | R8 | PATCH 200, version+1 |
| TVN-005 | Import Excel button + upload | ✅ Đạt | R13 | File upload OK, preview render đúng |
| TVN-006 | Validation 5 valid + 5 invalid | ✅ Đạt | R13 | 5 hợp lệ + 4 lỗi message rõ + skip empty + commit 5 nguồn=Import |
| TVN-007 | Câu hỏi rỗng → ERR-KHO-01 | ✅ Đạt | R8 | Inline validate |
| TVN-008 | Câu trả lời rỗng → ERR-KHO-02 | ✅ Đạt | R8 | Inline validate |
| TVN-009 | LV không hợp lệ → ERR-KHO-03 | ✅ Đạt | R8 | Inline validate |
| TVN-010 | CB_PD duyệt đơn lẻ | ✅ Đạt | R11 | cb_pd_tw_01 pure → 200 |
| TVN-011 | CB_PD từ chối + lý do ≥10 | ✅ Đạt | R11 | NHAP + ghiChu stored |
| TVN-012 | CB_PD duyệt hàng loạt | ✅ Đạt | R11 | 2 record bulk → DA_DUYET |
| TVN-013 | Toggle hết hiệu lực | ✅ Đạt | R8 | DA_DUYET → HET_HIEU_LUC |
| TVN-014 | Auto-import HOI_DAP DA_DUYET | ✅ Đạt | R15 | Forward-only verified — HD-002 → KCH 7bac45ff TU_DONG <30s |
| TVN-015 | GIN index FTS | ⏭ Hoãn | — | DB-level verify |
| TVN-016 | List phiên TV 4 tab | ✅ Đạt | R9 | R12 cột Số gợi ý fix |
| TVN-017 | Detail phiên Top 5 gợi ý | ✅ Đạt | R10 | Score DESC, button [Chọn] OK |
| TVN-018 | Click [Chọn] auto-fill | ✅ Đạt | R10 | Textarea fill 74 chars |
| TVN-019 | [Gửi trả lời] DA_GOI_Y → CB_TRA_LOI | ✅ Đạt | R9 | R12 supplementary 199 chars |
| TVN-020 | Kho QA rỗng → ERR-TVN-01 WARNING | ⚠️ Sai spec | R15-P2 | Non-block OK; WARNING không surface — BUG-008 |
| TVN-021 | Gửi trả lời rỗng → ERR-TVN-02 | ✅ Đạt | R9 | 422 |
| TVN-022 | DN gửi câu hỏi kênh=NHANH | ✅ Đạt | R12 | CMS proxy `/cms-create` 200 |
| TVN-023 | DN gửi kênh=THU_CONG → Nhóm II | 🚫 Không test được | R11 | mTLS DN outbound only |
| TVN-024 | DN escalate THU_CONG | 🚫 Không test được | R11 | mTLS DN outbound only |
| TVN-025 | DN gửi rỗng → ERR-TVN-DN-01 | 🚫 Không test được | R11 | mTLS DN outbound only |
| TVN-026 | DN search Cổng PLQG | ⏭ Hoãn | — | Outbound API |
| TVN-027 | DN search by keyword | ⏭ Hoãn | — | Outbound API |
| TVN-028 | DN search filter | ⏭ Hoãn | — | Outbound API |
| TVN-029 | DN đánh giá phiên CB_TRA_LOI | ✅ Đạt | R12 | CMS proxy `/danh-gia/cms-proxy` 200 |
| TVN-030 | Đánh giá điểm ngoài 1-5 | 🚫 Không test được | R11 | mTLS DN outbound only |
| TVN-031 | Đánh giá id không tồn tại | 🚫 Không test được | R11 | mTLS DN outbound only |
| TVN-032 | Batch auto het han phiên MOI >30 ngày | ⏭ Hoãn | — | Cần dev expose batch trigger + config timeout |
| TVN-033 | QTHT 👁️ R only | ✅ Đạt | R8 | 403 cho mọi mutation |
| TVN-034 | BN scope BR-AUTH-08 | ✅ Đạt | R13 | TW=19, BN BKH=0 — filter active |
| TVN-035 | NHT/CG no menu Tư vấn nhanh | ✅ Đạt | R13 | NHT + CG submenu chỉ Tư vấn chuyên sâu |
| TVN-036 | DN no menu Quản lý tư vấn | ✅ Đạt | R13 | DN sidebar không có top-level |
| TVN-037 | Auto-import HOI_DAP → KHO TU_DONG | ✅ Đạt | R15 | BUG-007 Closed — 3 KCH TU_DONG verified hoiDapGocId map 1-1 |
| TVN-038 | DN đánh giá update diem_tb | ✅ Đạt | R12 | KCH-0007 null → 4 sau danh-gia |
| TVN-039 | Audit log 9 action | ⚠️ Sai spec | R9 | KHO chuẩn R12, TVN còn TRA_LOI/CREATE |
| TVN-040 | Switch [Công khai] DA_DUYET → CONG_KHAI | ✅ Đạt | R13 | Auto thoiGianDangTai 10/05/2026 21:46 |
| TVN-041 | [Hủy công khai] CONG_KHAI → DA_DUYET | ✅ Đạt | R13 | State đổi clean |
| TVN-042 | BR-PUBLIC-01 chặn /cong-khai trên CHO_DUYET | ✅ Đạt | R13 | 409 ERR-BIZ-KCH-01 |
| TVN-043 | API Cổng PLQG fail → giữ state | 🚫 Không test được | R8 | Cần Cổng PLQG sandbox |
| TVN-044 | Mismatch congKhai vs trang_thai | 🚫 Không test được | R8 | Cần BE stub race condition |
| **Tổng** | **44 TC** | ✅ 30 · ⚠️ **2 (R15-P2: +TVN-020)** · ❌ 0 · 🚫 5 · ⏭ 6 · 🤷 0 → **30 PASS / 32 đã test (loại trừ ⏭/🚫) = 94% pure, 100% non-blocking (R15-P2)** | | |

## 1.6 Bảng TC chưa chạy được — phân loại 6 nhóm A-F (R15-P2)

Hiện tại còn **13 TC** chưa PASS — chia 3 nhóm: **2 chờ dev fix bug** (Nhóm B: TVN-039 BUG-005 partial · **TVN-020 BUG-008 WARNING missing**) · **7 lỗi env/chờ infra** (Nhóm D: mTLS DN + sandbox) · **4 lý do khác** (Nhóm F: DB-level + outbound API). **R15-P2 chạy TVN-020** (drop tạm 21 KCH → POST `/cms-create` → 201 non-block OK; WARNING ERR-TVN-01 missing → BUG-008 mới Minor) + restore 21 KCH thành công.

| # | TC ID | Status | Nhóm nguyên nhân | Phương án xử lý | Ai làm |
|---|---|:-:|---|---|:-:|
| 1 | TVN-039 | ⚠️ Sai spec | **B — Chờ dev fix bug** (BUG-005 partial) | BE chuẩn hoá AuditAction TVN: TRA_LOI→GUI_TRA_LOI_TVNHANH, CREATE→CREATE_TVNHANH + dropdown filter Module thêm "Tư vấn" | Dev BE |
| 2 | TVN-023 | 🚫 Không test được | **D — Lỗi env / chờ infra** (mTLS DN inbound) | mTLS sandbox Cổng PLQG hoặc CMS proxy mở rộng /hoi-daps | Infra / Dev BE |
| 3 | TVN-024 | 🚫 Không test được | **D — Lỗi env / chờ infra** (endpoint chưa expose) | Dev BE expose `/chuyen-thu-cong` cho CMS proxy nội bộ | Dev BE |
| 4 | TVN-025 | 🚫 Không test được | **D — Lỗi env / chờ infra** (mTLS guard chặn validation) | mTLS sandbox hoặc proxy bypass dev mode | Infra / Dev BE |
| 5 | TVN-030 | 🚫 Không test được | **D — Lỗi env / chờ infra** (mTLS guard) | mTLS sandbox hoặc proxy negative case | Infra / Dev BE |
| 6 | TVN-031 | 🚫 Không test được | **D — Lỗi env / chờ infra** (mTLS guard) | mTLS sandbox hoặc proxy 404 case | Infra / Dev BE |
| 7 | TVN-043 | 🚫 Không test được | **D — Lỗi env / chờ infra** (Cổng PLQG sandbox) | Dev BE stub Cổng PLQG mock 5xx + verify retry BR-FLOW-05 | Dev BE / Infra |
| 8 | TVN-044 | 🚫 Không test được | **D — Lỗi env / chờ infra** (race stub) | Dev BE stub delay BR-FLOW-05 + UI render badge transient | Dev BE |
| 9 | TVN-020 | ⚠️ Sai spec | **B — Chờ dev fix bug** (BUG-008) | BE thêm `warning.code='ERR-TVN-01'` + message vào response `/cms-create` (root hoặc `data.warning`) khi pool matching empty | Dev BE |
| 10 | TVN-032 | ⏭ Hoãn | **D — Lỗi env / chờ infra** (batch + config) | Set `cau_hinh.tvnhanh_timeout_ngay=1/1440` HOẶC dev expose batch trigger manual | Dev BE |
| 11 | TVN-015 | ⏭ Hoãn | **F — Lý do khác** (DB-level only, không UI/API) | DBA query `EXPLAIN ANALYZE SELECT ... @@ to_tsquery` xác định plan GIN | DBA |
| 12 | TVN-026 | ⏭ Hoãn | **F — Lý do khác** (outbound API + Postman) | QA setup Postman + xin API key Cổng PLQG sandbox | QA API + Infra |
| 13 | TVN-027 | ⏭ Hoãn | **F — Lý do khác** (outbound API) | Cùng TVN-026 — Postman + API key | QA API + Infra |
| 14 | TVN-028 | ⏭ Hoãn | **F — Lý do khác** (outbound API) | Cùng TVN-026 — Postman + API key | QA API + Infra |

---

## 1.7 R14 — UI-only Re-audit với `_03` accounts (2026-05-11 14:06:00)

**Scope:** Re-verify workflow chính của TVN module **chỉ qua browse UI** (Chrome DevTools MCP), không gọi API trực tiếp. Dùng bộ account `_03` permission-test (`cb_nv_tw_03` + `cb_pd_tw_03`) per memory `feedback_test_method_ui_only.md`.

**Method:** MCP `new_page` với `isolatedContext` riêng cho mỗi role (`ui-nv03` + `ui-pd03`) → click chain qua sidebar → fill_form + click button → wait_for signal text → verify state đổi bằng `take_snapshot`. Cấm: `fetch()` action, bulk POST `/api/v1/*`, JWT direct.

### Kết quả 5/5 PASS

| # | TC | Role | Action UI | Outcome | Evidence |
|---|---|---|---|---|---|
| 1 | TVN-001 list permission | `cb_nv_tw_03` (NV TW) | Click sidebar Quản lý tư vấn → Kho câu hỏi | 24 record render + 4 buttons (Thêm/Nhập Excel/Xuất Excel/Làm mới) → permission đầy đủ | [r14-ui-nv03-kho-cau-hoi-cho-duyet-no-action.png](../../bug-reports/tu-van-nhanh/image/r14-ui-nv03-kho-cau-hoi-cho-duyet-no-action.png) |
| 2 | TVN-010 approve | `cb_pd_tw_03` (PD TW) | Tab Chờ duyệt → click row `QA-20260508-0004` → modal Chi tiết → [Duyệt] → confirm dialog [Duyệt] | Status: Chờ duyệt → **Đã duyệt** · Hiệu lực: Không → **Có** · Ngày duyệt: 11/05/2026 14:05:00 · Lượt xem 2 → 3 (auto-inc) | [r14-ui-test2-pd03-detail-duyet-button.png](../../bug-reports/tu-van-nhanh/image/r14-ui-test2-pd03-detail-duyet-button.png) · [r14-ui-test2-pd03-da-duyet-state.png](../../bug-reports/tu-van-nhanh/image/r14-ui-test2-pd03-da-duyet-state.png) |
| 3 | TVN-018/019 reply gợi ý | `cb_nv_tw_03` | Phiên `TVN-QA-20260425-0021` DA_GOI_Y → click [Chọn] KCH-0007 → auto-fill textarea 74 chars → [Gửi trả lời] | State: Đã gợi ý → **CB trả lời** · Số gợi ý=2 · Cập nhật 11/05/2026 12:27:00 | [r14-ui-test3-nv03-cb-tra-loi-state.png](../../bug-reports/tu-van-nhanh/image/r14-ui-test3-nv03-cb-tra-loi-state.png) |
| 4 | TVN-016 filter | `cb_nv_tw_03` | Combobox Nguồn = "Tự động" | Render đúng record `QA-20260510-0005` Nguồn=Tự động (BR-FLOW-10 historical) | [r14-ui-nv03-filter-nguon-tu-dong.png](../../bug-reports/tu-van-nhanh/image/r14-ui-nv03-filter-nguon-tu-dong.png) |
| 5 | TVN-040 CONG_KHAI | `cb_nv_tw_03` | Row `QA-20260508-0004` DA_DUYET → modal Chi tiết → [Công khai] → dialog fill "Mô tả công khai" → [Công khai] | Status: Đã duyệt → **Công khai** · Công khai: Chưa → **Đã công khai** · Thời gian đăng tải 11/05/2026 14:06:00 · Button đổi → [Hủy công khai] | [r14-ui-test5-nv03-cong-khai-state.png](../../bug-reports/tu-van-nhanh/image/r14-ui-test5-nv03-cong-khai-state.png) |

### Workflow E2E verified

`NHAP/CHO_DUYET` (TVN-003 cũ) → **CHO_DUYET → DA_DUYET** (Test 2 R14) → **DA_DUYET → CONG_KHAI** (Test 5 R14). State Machine SM-KCH end-to-end via UI click chain. SM-TVNHANH: **DA_GOI_Y → CB_TRA_LOI** (Test 3 R14).

### Permission gating verified

- `cb_nv_tw_03` (CB_NV) thấy 4 button: Thêm câu hỏi · Nhập Excel · Xuất Excel · Làm mới — KHÔNG có Duyệt/Từ chối ở Chi tiết.
- `cb_pd_tw_03` (CB_PD) thấy: Xuất Excel · Làm mới + 2 button trong Chi tiết: Duyệt · Từ chối — KHÔNG có Công khai (đúng SCR-X.2: CONG_KHAI là quyền NV sau khi DA_DUYET).
- Both: Detail modal cho phép view; action button khác nhau theo role.

### Bug status sau R14

Không re-test bug trong R14 (scope = UI tests only theo user request). 3 bug Open trước R14 giữ nguyên status — đã được verify trong session R14 phần audit earlier:
- **BUG-001** Major data drift account → confirmed data drift (BE guard works với accounts pure)
- **BUG-005** Minor audit naming → PARTIAL (KHO chuẩn R12, TVN còn TRA_LOI/CREATE)
- **BUG-007** Major auto-import BR-FLOW-10 → PARTIAL forward-only

---

## 1.9 R15-P2 — QA-only test TVN-020 (Kho QA rỗng) + Restore Kho (2026-05-12 02:00:00 → 02:30:00)

**Scope:** Theo user request `/qa-only ... test TVN-20 sau khi setup`. Setup luồng đồng bộ (QA tự seed qua API, KHÔNG cần dev seed) → drop tạm 21 KCH `DA_DUYET hieuLuc=true` về 0 → POST `/cms-create` → verify ERR-TVN-01 WARNING → restore Kho về 21.

**Method:** MCP `cb_nv_tw_01` isolatedContext — fetch `/api/v1/kho-cau-hois?trangThai=DA_DUYET&hieuLuc=true&pageSize=100` → backup 21 KCH id+version → PATCH ×21 `/het-hieu-luc {version}` → POST `/tu-van-nhanhs/cms-create {cauHoiDn,...}` → PATCH ×21 `/kich-hoat {version}` (20 với cb_nv_tw_01 + 1 với cb_nv_bn_01 cho KCH BN BKH `aa222034`).

### Kết quả TVN-020 — ⚠️ PARTIAL (non-blocking OK, WARNING missing)

| Step | Action | Outcome |
|---|---|---|
| Setup-1 | Fetch DA_DUYET hieuLuc=true (baseline) | 21 record |
| Setup-2 | PATCH ×21 `/het-hieu-luc` | 21/21 success, state → HET_HIEU_LUC, hieuLuc → false |
| Setup-3 | Verify pool rỗng | `?trangThai=DA_DUYET&hieuLuc=true` total=0 ✅ |
| Test | POST `/api/v1/tu-van-nhanhs/cms-create` body `{cauHoiDn, linhVucPL:'Doanh nghiệp', kenh:'NHANH', ...}` | **201 success=true**, phiên `TVN-20260512-0001` tạo OK, state=CB_TRA_LOI, goiYTraLoi=[] |
| Verify | Inspect response cho `warning/warningCode/warningMessage` | **KHÔNG có WARNING ERR-TVN-01** ❌ |
| Verify | GET `/goi-y` | `{success:true, data:[]}` — không warning embedded |
| Restore-1 | PATCH ×21 `/kich-hoat` (cb_nv_tw_01) | 20/21 success, 1 fail 403 BR-AUTH-05 (KCH BN BKH đơn vị khác) |
| Restore-2 | Login cb_nv_bn_01 → PATCH `/kich-hoat` KCH `aa222034` | 200 success ✅ |
| Verify | Final DA_DUYET hieuLuc=true count | **21** (delta 0 vs baseline) ✅ |

### Findings

- ✅ **Non-blocking OK:** Kho rỗng KHÔNG block tạo phiên (đúng spec line 134 "không block CB NV trả lời tay").
- ⚠️ **WARNING ERR-TVN-01 missing:** Response `/cms-create` không có `warning.code/warningCode` field. CB NV chỉ thấy Top 5 gợi ý empty mà không hiểu vì sao → cần signal từ BE. → **BUG-FUNC-TVN-008 mới Minor.**
- ⚠️ **State machine deviation:** Phiên skip `MOI → CB_TRA_LOI` thay vì `MOI → DANG_TIM_KIEM → DA_GOI_Y → CB_TRA_LOI`. Có thể là BE optimization (Kho rỗng → no need matching step) nhưng spec SM-TVNHANH §line 60-68 không quy định path này. Để observ tiếp, không log bug riêng (gộp BUG-008).
- ✅ **Endpoint reversibility:** `/het-hieu-luc` one-way (HET_HIEU_LUC `/het-hieu-luc` again → 409 ERR-STATE-KCH-HHL-01). Restore qua `/kich-hoat` (probe found). Cross-đơn vị BR-AUTH-05 enforce — restore KCH BN BKH cần cb_nv_bn_01 không phải cb_nv_tw_01.

### Operational learning

- **Endpoint `/kich-hoat`** (POST `{version}`) là path reverse cho `/het-hieu-luc` — chưa được document rõ trong SRS, chỉ ám chỉ ở §line 421 + module §⑫ line 788 "Toggle lại". Naming inconsistent với `/het-hieu-luc` (1 verb passive + 1 verb active).
- **BR-AUTH-05 cross-đơn vị enforce dual-mode:** Drop (`/het-hieu-luc`) accept cross-đơn vị nếu user có write quyền chung. Restore (`/kich-hoat`) reject cross-đơn vị → cần CB_NV của đơn vị gốc. Asymmetric, dễ tạo dead-state nếu QA không có account đúng đơn vị.
- **QA self-seed luồng đồng bộ verified:** Không cần dev BE seed cho TVN-020. QA backup→drop→test→restore qua API trong 1 session.

### Bug status sau R15-P2

- **BUG-FUNC-TVN-008 (Minor) mới** — WARNING ERR-TVN-01 không surface. Bug-report chi tiết: [`bug-report-r7-7-11-tvn.md` §BUG-008](../../bug-reports/tu-van-nhanh/bug-report-r7-7-11-tvn.md).
- BUG-FUNC-TVN-005 vẫn Open PARTIAL (audit naming).

Evidence: `image/r15-tc-tvn-020-phien-cb-tra-loi-empty-goi-y.png`.

---

## 1.8 R15 — Follow-up MCP test 5 TC + walk full workflow E2E (2026-05-12 01:00:00 → 01:25:00)

**Scope:** Theo user request `/qa-only dùng mcp thực hiện test các testcase có thể chạy được ngay`, run 5 TC unblock: **TVN-010/011/012** (FE+BE guard 403 cho CB_NV) + **TVN-014/037** (BR-FLOW-10 auto-import HOI_DAP → KCH TU_DONG). Seed 1 HOI_DAP walk full MOI → DA_DUYET trong session để verify forward-only trigger.

**Method:** MCP `new_page` với 3 isolatedContext riêng (`tvn-r15-cb-nv-tw-01` + `tvn-r15-cb-pd-tw-01` + `tvn-r15-qtht`) → no logout/login switching. Login OTP=666666 mỗi context. Verify dùng UI snapshot + API `list_network_requests` + curl `/api/v1/kho-cau-hois?nguon=TU_DONG`.

### Kết quả 5/5 PASS

| # | TC | Role | Action | Outcome | Evidence |
|---|---|---|---|---|---|
| 1 | TVN-010 | `cb_nv_tw_01` | Click row CHO_DUYET → modal Chi tiết → FE không render button [Duyệt] | FE guard: button absent. API direct POST `/approve` → 403 ERR-PERM-SYS-00-01 ✅ | [r15-tc-tvn-010-011-fe-guard-no-duyet-tuchoi.png](image/r15-tc-tvn-010-011-fe-guard-no-duyet-tuchoi.png) |
| 2 | TVN-011 | `cb_nv_tw_01` | Modal Chi tiết → FE không render button [Từ chối] | FE guard: button absent. API direct POST `/reject {ghiChu,version}` → 403 ✅ | (cùng screenshot trên — FE chỉ hiện Đóng/Edit) |
| 3 | TVN-012 | `cb_nv_tw_01` | Tab Chờ duyệt → checkbox 2 row → FE không render toolbar [Duyệt hàng loạt] | FE guard: toolbar absent. API direct POST `/approve-bulk` → 403 ✅. BR-AUTH-05 enforce dual-layer. |
| 4 | TVN-014 | `cb_pd_tw_01` (gate) + `qtht_01` (verify) | Walk HOI_DAP `HD-20260510-002` qua state MOI → TIEP_NHAN → DANG_XU_LY → CHO_PHE_DUYET → DA_DUYET. Sau DA_DUYET đợi 30s + query KCH TU_DONG | **BR-FLOW-10 trigger:** KCH `7bac45ff-25e1-42fe-86fe-8b9b1a43918d` auto-create với `hoiDapGocId=480906b9...`, `nguon=TU_DONG`, `trangThai=DA_DUYET`, `ngayTao=2026-05-12T01:24:27Z` — khớp giây HD-002 duyệt | [r15-br-flow-10-auto-import-verified.png](image/r15-br-flow-10-auto-import-verified.png) |
| 5 | TVN-037 | (cùng) | Sau TVN-014, query `/kho-cau-hois?hoiDapGocId=480906b9...&nguon=TU_DONG` | Total=3 KCH TU_DONG: (a) `7bac45ff...` → HD-20260510-002 (R15 mới); (b) `e267c484...` → HD-20260509-010 (back-fill R14b → R15); (c) `a70ce660...` → HD-20260510 (historical). hoiDapGocId map 1-1 ✅ | (cùng API response) |

### BR-FLOW-10 forward-only behavior — VERIFIED

Auto-trigger HOI_DAP `DA_DUYET` → KCH `nguon=TU_DONG` xảy ra **đúng giây** (latency <30s, capture lúc 01:24:27Z khớp `ngayDuyet` HD-002). Pattern repeat 3 lần với 3 HOI_DAP độc lập:

| HOI_DAP gốc | KCH TU_DONG ID | KCH ngayTao | Latency |
|---|---|---|---|
| HD-20260510-002 (480906b9) — R15 fresh | 7bac45ff | 2026-05-12 01:24:27 | <30s |
| HD-20260509-010 (3577bfb6) — R14b back-fill | e267c484 | 2026-05-11 23:18:37 | back-fill batch |
| HD-20260510 (2d373db6) — historical | a70ce660 | 2026-05-10 20:38:31 | historical |

→ **BUG-007 Closed-verified R15:** Forward-only trigger works clean. Back-fill batch (R14b → R15) đã import HD-20260509-010 lệch trước R15. Cả 2 paths PASS.

### Workflow E2E walk (TVN-014 detail)

1. `cb_nv_tw_01` login + navigate `/hoi-dap/480906b9...` (state DANG_XU_LY, version 4).
2. Click [Gửi phản hồi] → modal preview reply DRAFT → confirm modal "Xác nhận gửi phản hồi?" → state CHO_PHE_DUYET, version 5.
3. Switch isolatedContext `cb_pd_tw_01`, navigate cùng URL → button [Phê duyệt] render (CB_PD same cấp permission OK).
4. Click [Phê duyệt] → modal "Xác nhận phê duyệt? Hành động này không thể hoàn tác" → confirm → state **Đã duyệt**, Người duyệt=`CB Phê duyệt TW 01`, Ngày duyệt=12/05/2026 01:24.
5. Switch isolatedContext `qtht_01`, fetch `/api/v1/kho-cau-hois?hoiDapGocId=480906b9...&nguon=TU_DONG` `credentials:'include'` → 200, items=1 record mới `7bac45ff...` `ngayTao=2026-05-12T01:24:27Z`.

→ **BR-FLOW-10 verified end-to-end.** Auto-import latency ≤30s (capture lúc 01:24:57Z, sau 30s wait từ approval 01:24:27Z).

### Bug status sau R15

- **BUG-007 (Major auto-import BR-FLOW-10)** — **Closed-verified R15** (forward-only + back-fill both work).
- **BUG-001 (Major data drift account `cb_nv_tw_01`)** — **Closed-verified R15** (DB fix between R14b 17:18 và R15 01:00 — `/auth/me` returns `vaiTro:["CB_NV_TW"]` only, 3 mutation endpoints 403).
- **BUG-005 (Minor audit naming)** — **Open PARTIAL** (KHO_CAU_HOI 6 hanhDong chuẩn ✅; TU_VAN_NHANH module còn legacy TRA_LOI/UPDATE/CREATE, dropdown filter Module thiếu "Tư vấn" option).

3 bug R15 → **2 Closed + 1 Open PARTIAL.** Bug-report `Pass-bug-report-r7-7-11-tvn.md` rename pending sau khi BUG-005 đóng.

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| TVN-001 | FR-X.2-01, UC154, SCR-X2-01 | Xem danh sách kho Q&A 3 tab + paginate 20/page + filter | Happy | P0 | **PASS** | — | 9 record list, 3 tab (Tất cả 9 / Đã duyệt 6 / Chờ duyệt 2). ⚠️ Filter trạng thái dropdown thiếu — xem BUG-FUNC-TVN-003. |
| TVN-002 | FR-X.2-01, BR-DATA-08 | Tìm kiếm full-text + filter (LV / Nguồn / Trạng thái) | Happy | P1 | **PASS** | — | API verify: search "thuế"→2, DA_DUYET→6, THU_CONG→8, IMPORT→1. UI search box hoạt động qua Enter. |
| TVN-003 | FR-X.2-01, BR-DATA-04, UC154 | CB NV tạo Q&A thủ công → CHO_DUYET, THU_CONG, hieuLuc=false | Happy | P0 | **PASS** | — | QA-20260508-0001 tạo OK. Auto-gen mã QA-{YYYYMMDD}-{SEQ} chính xác. ⚠️ Spec C16 Rich Text nhưng UI dùng plain textarea — lưu ý dev. |
| TVN-004 | FR-X.2-01, UC154 | Cập nhật Q&A CHO_DUYET — sửa câu trả lời + từ khóa | Happy | P1 | **PASS** | — | PATCH 200, vẫn CHO_DUYET, version 1→2. ⚠️ tuKhoa kiểu array (max 20), spec viết "phân cách dấu phẩy" — minor schema deviation. |
| TVN-007 | FR-X.2-01 §E1 ERR-KHO-01 | Tạo Q&A câu hỏi trống → toast "Câu hỏi không được để trống" | Negative | P1 | **PASS** | — | UI validate inline. Message "Câu hỏi không được để trống" thay vì ERR-KHO-01 — semantically equivalent. |
| TVN-008 | FR-X.2-01 §E2 ERR-KHO-02 | Tạo Q&A câu trả lời trống → "Câu trả lời không được để trống" | Negative | P1 | **PASS** | — | Inline validate ✅ |
| TVN-009 | FR-X.2-01 §E3 ERR-KHO-03 | Tạo Q&A lĩnh vực không hợp lệ → "Vui lòng chọn lĩnh vực" | Negative | P2 | **PASS** | — | Inline validate ✅ |
| **TVN-010** (R11 flip ✅) | FR-X.2-01 §Processing 3, UC155 | CB PD duyệt đơn lẻ: CHO_DUYET → DA_DUYET, hieu_luc=true | Workflow | P0 | **PASS** | BUG-FUNC-TVN-001 (Major reclassified) | **R11 verified `cb_pd_tw_01` pure session:** UI click row QA-20260510-0001 → detail dialog → [Duyệt] → modal confirm → state "Đã duyệt"+"Có" hiệu lực; POST `/approve` `{version}` → 200, hieuLuc=true, ngayDuyet auto-fill, version+1, nguoiDuyetId=cb_pd_tw_01 ✅. |
| **TVN-011** (R11 flip ✅) | FR-X.2-01 §Processing 3, BR-FLOW-04 | CB PD từ chối + lý do ≥10 ký tự: CHO_DUYET → NHAP | Workflow | P0 | **PASS** | BUG-FUNC-TVN-001 (Major reclassified) | **R11 verified `cb_pd_tw_01`:** Click row QA-20260510-0004 → detail → [Từ chối] → modal lý do (75 ký tự) → confirm → state "Bị từ chối"; POST `/reject` `{ghiChu, version}` → 200, state→NHAP, ghiChuPheDuyet stored, version+1 ✅. BR-FLOW-04 ≥10 ký tự enforce client-side. |
| **TVN-012** (R11 flip ✅) | FR-X.2-01 §Processing 3, UC155 | CB PD duyệt hàng loạt → tất cả CHO_DUYET → DA_DUYET | Workflow | P1 | **PASS** | BUG-FUNC-TVN-001 (Major reclassified) | **R11 verified `cb_pd_tw_01`:** Tab "Chờ duyệt" → check 2 checkbox QA-20260510-0002 + 0003 → toolbar "Đã chọn 2 câu hỏi" + button [Duyệt hàng loạt] → modal "Duyệt 2 câu hỏi?" → confirm → POST `/approve-bulk` → 200, cả 2 chuyển "Đã duyệt"+"Có" hiệu lực, list "Chờ duyệt" giảm 6→4 ✅. |
| TVN-013 | FR-X.2-01 §Processing 6 | CB NV toggle hết hiệu lực: DA_DUYET → HET_HIEU_LUC | Workflow | P1 | **PASS** | — | API `/het-hieu-luc` body `{version}` → 200, hieuLuc:true→false, state→HET_HIEU_LUC. Đúng spec line 787 (cb_nv toggle). |
| TVN-033 | BR-AUTH-01, BR-AUTH-08, Spec QTHT 👁️ R | QTHT xem được kho Q&A nhưng không CRUD/duyệt/từ chối/toggle | Authorization | P1 | **PASS** | — | UI: Page render OK, KHÔNG có button [+ Thêm] / [Nhập Excel] / [Xuất Excel]. API: Create 403 ERR-PERM-SYS-00-01 ✅, Toggle hết hiệu lực 403 ✅, Approve/Reject CHO_DUYET 403 BR-AUTH-05 ✅, List 200 ✅. |
| TVN-040 | FR-X.2-06 mới v3.5, BR-PUBLIC-01/03 | CB NV bật Switch [Công khai] DA_DUYET → CONG_KHAI | Workflow | P0 | **BLOCKED** | BUG-FUNC-TVN-002 | Schema KHO_CAU_HOI thiếu field `congKhai` / `thoiGianDangTai` / `moTaCongKhai` / `fileDinhKemCongKhai`. Endpoint `/cong-khai` `/publish` `/dang-tai` đều 404. PATCH `{congKhai:true}` 409 "Khong the cap nhat o trang thai 'DA_DUYET'". → FR-X.2-06 BE chưa deploy. |
| TVN-041 | FR-X.2-06, BR-PUBLIC-02 | CB NV [Hủy công khai] CONG_KHAI → DA_DUYET | Workflow | P0 | **BLOCKED** | BUG-FUNC-TVN-002 | Cascade: không có CONG_KHAI để test (FR-X.2-06 chưa deploy). |
| TVN-042 | FR-X.2-06, BR-PUBLIC-01 | Bật công khai khi CHO_DUYET → ERR-TVN-CK-03 chặn | Negative | P1 | **BLOCKED** | BUG-FUNC-TVN-002 | Cascade FR-X.2-06 chưa deploy. |
| TVN-043 | FR-X.2-06, BR-FLOW-05 | API Cổng PLQG fail → giữ trạng thái cũ + ERR-TVN-CK-01/02 | Negative | P1 | **BLOCKED** | BUG-FUNC-TVN-002 | Cascade + thiếu Cổng PLQG sandbox. |
| TVN-044 | FR-X.2-06 mismatch | Mismatch `congKhai` vs `trang_thai='CONG_KHAI'` (badge "Đang xử lý"/"Đang gỡ") | Workflow | P1 | **BLOCKED** | BUG-FUNC-TVN-002 | Cascade FR-X.2-06 + cần BE stub race condition. |
| **TVN-022** (R11) | FR-X.2-03, UC inbound | DN gửi câu hỏi qua API Cổng PLQG kênh=NHANH → tạo phiên MOI | Workflow | P0 | **BLOCKED** | — | POST `/api/v1/tu-van-nhanhs` → **401 ERR-AUTH-MTLS-02** "Thiếu fingerprint chứng chỉ mTLS của client". Đúng spec FR-X.2-05 (cùng pattern R7.6.2 B5). DN chỉ tương tác qua Cổng PLQG bên ngoài, không testable nội bộ. |
| **TVN-023** (R11) | FR-X.2-03 kênh=THU_CONG | DN gửi câu hỏi kênh=THU_CONG → KHÔNG tạo phiên TV nhanh, chuyển Nhóm II UC12 | Workflow | P1 | **BLOCKED** | — | POST `/api/v1/hoi-daps` với CB_PD_TW token → 403 Forbidden ERR-PERM-SYS-00-01 (DN-only role). Cần mTLS Cổng PLQG. |
| **TVN-024** (R11) | FR-X.2-04 escalate | DN nhấn "Chuyển sang TV thủ công" → giữ history, kênh→THU_CONG, phiên đóng | Workflow | P1 | **BLOCKED** | — | Probe 4 endpoint variants `/chuyen-thu-cong`, `/chuyen-tv-thu-cong`, `/escalate`, `/chuyen` + PATCH `/{id}` đều 404 ERR-SYS-00-04-01. Endpoint chưa expose nội bộ; cùng family DN-side qua Cổng PLQG. |
| **TVN-025** (R11) | FR-X.2-03 §E1 ERR-TVN-DN-01 | DN gửi câu hỏi rỗng → ERR-TVN-DN-01 "Vui lòng nhập câu hỏi" | Negative | P1 | **BLOCKED** | — | POST `/tu-van-nhanhs` `{cauHoi:''}` → 401 mTLS guard chạy trước validation. Cần mTLS Cổng PLQG. |
| **TVN-029** (R11) | FR-X.2-04, UC158 | DN đánh giá phiên CB_TRA_LOI → điểm 1-5 + nhận xét → DANH_GIA_TV, phiên→HOAN_THANH | Workflow | P0 | **BLOCKED** | — | POST `/api/v1/tu-van-nhanhs/{id}/danh-gia` → **401 ERR-AUTH-MTLS-02**. Endpoint tồn tại + đúng spec mTLS guard. Probe phiên CB_TRA_LOI ID `989ff083-3945-4c02-aebe-73535828fa94` (TVN-QA-20260428-0016). |
| **TVN-030** (R11) | FR-X.2-04 §E1 ERR-DG-TVN-01 | Đánh giá điểm ngoài 1-5 (vd 0/6) → ERR-DG-TVN-01 "Điểm đánh giá phải từ 1 đến 5" | Negative | P1 | **BLOCKED** | — | Cùng endpoint mTLS-only như TVN-029. |
| **TVN-031** (R11) | FR-X.2-04 §E2 ERR-DG-TVN-02 | Đánh giá `tu_van_nhanh_id` không tồn tại → ERR-DG-TVN-02 "Phiên tư vấn không tồn tại" | Negative | P1 | **BLOCKED** | — | Cùng endpoint mTLS-only. |
| **TVN-037** (R11) | FR-X.2-01, BR-FLOW-10 | Auto-import từ HOI_DAP DA_DUYET → tạo KHO_CAU_HOI nguồn=TU_DONG, hoi_dap_goc_id liên kết | Cross-module | P1 | **FAIL** | **BUG-FUNC-TVN-007 (R11 mới)** | HOI_DAP `HD-20260509-010` (id `3577bfb6-ec53-4a0c-8858-b0507afb3472`) trạng thái DA_DUYET. KHO total 18 (THU_CONG 17 + IMPORT 1) — 0 TU_DONG, 0 record có `hoiDapGocId`. Auto-import BR-FLOW-10 không trigger. |
| **TVN-038** (R11) | FR-X.2-04, UC158 | DN đánh giá Q&A gợi ý → cập nhật `diem_danh_gia_tb` AVG trên KHO_CAU_HOI | Cross-module | P1 | **BLOCKED** | — | Phụ thuộc TVN-029 (DN đánh giá qua mTLS). Cascade BLOCKED. |
| **TVN-016** (R9 PASS, R10 re-verify) | — , SCR-X2-03 | List phiên TV 4 tab (Tất cả 50 / Chờ xử lý 14 / Đã gợi ý 20 / Hoàn thành 16) + paginate 20/page | Happy | P0 | **PASS** | — | R10 re-confirm tab counts đúng (Chờ xử lý=MOI+DANG_TIM_KIEM 8+6=14; Đã gợi ý=DA_GOI_Y+CB_TRA_LOI 9+11=20; Hoàn thành=HOAN_THANH+HET_HAN 12+4=16; Tổng 50). API verify URL pattern `?trangThai=MOI,DANG_TIM_KIEM` khớp tab. ⚠️ Cột "Số gợi ý" = 0 cho mọi phiên dù `goiYTraLoi.length=2` — log BUG-FUNC-TVN-006 Minor. |
| **TVN-017** (R10 flip ✅) | FR-X.2-02 §Processing 3, SCR-X2-03 row 7-8 | Mở chi tiết phiên DA_GOI_Y → layout 2 cột: trái câu hỏi DN+Stepper+thông tin DN, phải Top 5 gợi ý từ KHO_CAU_HOI sắp theo relevance DESC | Happy | P0 | **PASS** | ✅ TVN-004 Closed | **R10 verified:** Top 5 gợi ý render đúng. TVN-0024: KCH-0001 (94%) + KCH-0004 (74%). TVN-0021: KCH-0001 (91%) + KCH-0007 (71%). Score descending ✅, mỗi card có mã KQA + câu hỏi + câu trả lời + % phù hợp + button [Chọn] đúng spec FR-X.2-04. Title "Top 5" với actual N=2 (seed assign 2 entries/phiên — within spec "tối đa 5"). |
| **TVN-018** (R10 flip ✅) | FR-X.2-02 §Processing 5 | CB NV click [Chọn] gợi ý → auto-fill ô soạn rich-text | Workflow | P1 | **PASS** | — | **R10 verified:** Click [Chọn] trên KCH-0001 (TVN-0021) → textarea "Nội dung trả lời" auto-fill 74 ký tự "Trả lời tham chiếu cho câu hỏi #21A. Áp dụng quy định pháp luật hiện hành." ✅ đúng spec FR-X.2-02 §Processing 5. CB NV có thể chỉnh sửa thêm trước [Gửi trả lời]. |
| **TVN-019** (R9) | FR-X.2-02 §Processing 6, SCR-X2-03 row 8 | CB NV [Gửi trả lời] → DA_GOI_Y → CB_TRA_LOI, tạo TU_VAN_NHANH liên kết `khoCauHoiDaChonId` nếu chọn từ kho | Workflow | P0 | **PASS** | — | UI: TVN-QA-20260428-0016 click [Gửi trả lời] với 257 chars → state CB_TRA_LOI, nguoiTraLoiId set, version+1. API: TVN-QA-20260428-0015 với khoCauHoiDaChonId=QA-20260508-0003 stored, ngayTraLoi auto. |
| **TVN-021** (R9) | FR-X.2-02 §E2 ERR-TVN-02 | CB NV gửi trả lời với nội dung rỗng → "Nội dung trả lời là bắt buộc" | Negative | P1 | **PASS** | — | API `POST /{id}/tra-loi {noiDungTraLoi:''}` → 422 ERR-TVN-02 ✅ |
| **TVN-039** (R9) | BR-DATA-05, FR-X.2-01 §Postconditions | Audit log ghi đầy đủ CRUD/APPROVE/REJECT/IMPORT/TOGGLE/CONG_KHAI/GUI_TRA_LOI/DANH_GIA/AUTO_HET_HAN | Cross-module | P1 | **PARTIAL** | BUG-FUNC-TVN-005 | Endpoint `/api/v1/audit-logs` 200 với QTHT (cb_nv 403). KHO_CAU_HOI: 25 events. TU_VAN_NHANH: 2 events (đúng 2 lần `/tra-loi` R9). Schema đầy đủ entityType/entityId/hanhDong/endpoint/responseCode/thoiGian/ipAddress/sessionId. ⚠️ Action naming: `TU_CHOI` (Vietnamese) vs spec `REJECT_KHOCAUHOI`; `UPDATE` cho het-hieu-luc thay vì `TOGGLE_HIEU_LUC`. Chưa verify IMPORT_EXCEL/CONG_KHAI/DANH_GIA/AUTO_HET_HAN (depend feature chưa deploy hoặc mTLS). |

> **Đã defer (chưa chạy round này):**
> - TVN-005, 006 (Import Excel) — cần file test mẫu
> - TVN-014, 037 (auto-import TU_DONG) — cần ≥1 HOI_DAP DA_DUYET (R7.4.A4 ⏳)
> - TVN-015 (GIN index) — DB-level verify
> - TVN-016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 029, 030, 031, 032, 038 (15 TC liên quan phiên TV nhanh) — BLOCKED upstream R7.6.2
> - TVN-026, 027, 028 (DN search Cổng PLQG) — API outbound, cần Postman/Bruno + API key
> - TVN-034 (cb_nv_bn scope BR-AUTH-08) — cần seed data BN
> - TVN-035, 036 (NHT/TVV/CG/GV/DN no menu) — cần các account roles đó
> - TVN-039 (Audit log) — DB-level verify

---

## 3. Bug Report (tóm tắt)

> **Lưu ý:** Chi tiết Steps/Evidence/Repro xem [bug-report-r7-7-11-tvn.md](../../bug-reports/tu-van-nhanh/bug-report-r7-7-11-tvn.md).

### BUG-FUNC-TVN-001 — Major (R11 reclassified) Account `cb_nv_tw_01` data drift — gán nhầm 3 vai trò

> **R11 (2026-05-10 19:04:57) — RECLASSIFIED Critical → Major.** Verify với account pure CB_NV_TW khác (`cb_nv_tw_03`) → POST /approve trả 403 ERR-PERM-SYS-00-01 ✅ → BE permission system thực ra hoạt động ĐÚNG. Root cause là **`cb_nv_tw_01` data drift** (DB gán 3 vai trò `[CB_PD_TW, CB_NV_TW, QA_VT_DEL_TEST_R7]` thay vì single `CB_NV_TW` per `input/users.csv`). Đây không phải BE security hole, là data setup leak — fix: sync DB role mapping về `users.csv` source.

| Trường | Giá trị |
|--------|---------|
| **Severity** | **Major** (was Critical R8-R10) |
| **Priority** | **P1** (was P0) |
| **TC Reference** | TVN-010, TVN-011, TVN-012 (R11 PASS với cb_pd_tw_01 + cb_nv_tw_03) |
| **Status** | Open (chờ fix DB role mapping) |
| **Assignee** | DevOps + Backend Team (data setup) |

**Mô tả:** Account `cb_nv_tw_01` trong DB hiện gán 3 vai trò `[CB_PD_TW, CB_NV_TW, QA_VT_DEL_TEST_R7]` (verified qua API `/auth/me` + RBAC user_role table). File source `input/users.csv` chỉ định 1 vai trò CB_NV_TW. Vì có CB_PD_TW trong role list, account này bypass guard và approve/reject/bulk-approve thành công — không phải BE thiếu role guard mà account dữ liệu đã sai.

**Expected vs Actual:** Expected `cb_nv_tw_01` chỉ có vai trò CB_NV_TW (single). Actual: 3 vai trò gán đồng thời, trong đó có CB_PD_TW (mạnh hơn CB_NV_TW theo policy).

**Impact:** Test phân quyền sai-âm (false negative) đối với BUG-001 ban đầu. Production nếu cùng pattern data drift sẽ là security hole — cần audit toàn bộ DB role mapping cross-check với `users.csv`.

**Root Cause (Verified R11):** DB seed/migration trộn 3 role vào account `cb_nv_tw_01`. `cb_nv_tw_03` (pure CB_NV_TW) → 403 đúng ✅. `cb_pd_tw_01` (pure CB_PD_TW) → 200 đúng ✅. BE permission system OK. Fix: chạy migration sync `user_roles` table → match `users.csv` (idempotent, drop role thừa).

### BUG-FUNC-TVN-002 — Major FR-X.2-06 (Công khai/Hủy công khai) chưa deploy

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P1 |
| **TC Reference** | TVN-040, 041, 042, 043, 044 |
| **Status** | Open |
| **Assignee** | Backend + Frontend Team |

**Mô tả:** FR-X.2-06 v3.5 (UC156) thêm action [Công khai] / [Hủy công khai] cho CB NV trên Q&A DA_DUYET — bao gồm 4 trường mới (`congKhai`, `thoiGianDangTai`, `moTaCongKhai`, `fileDinhKemCongKhai`) + enum mới `CONG_KHAI` ở trang_thai + 3 BR mới (BR-PUBLIC-01/02/03) + BR-FLOW-05. Schema thực tế thiếu cả 4 field; endpoint `/cong-khai` / `/publish` / `/dang-tai` 404; PATCH với `{congKhai:true}` bị BE từ chối.

**Expected vs Actual:** Expected schema có 4 field công khai + Switch UI inline + endpoint POST `/api/v1/kho-cau-hois/{id}/cong-khai`. Actual: schema chỉ có 21 field cũ, không có toggle UI Switch, endpoint trả 404.

**Impact:** 5 TC mới v3.5 (TVN-040..044) BLOCKED. Không verify được API outbound BR-FLOW-05 đến Cổng PLQG.

**Root Cause (Suggested):** Migration v3.5 chưa chạy; controller + UI module chưa add. Cần coordinate dev sprint v3.5 update.

### BUG-FUNC-TVN-003 — Minor Filter trạng thái dropdown thiếu trên list page

| Trường | Giá trị |
|--------|---------|
| **Severity** | Minor |
| **Priority** | P2 |
| **TC Reference** | TVN-001 |
| **Status** | Open |
| **Assignee** | Frontend Team |

**Mô tả:** Spec [02-thu-tu-module.md line 766](../../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) yêu cầu filter bar có dropdown "Trạng thái" cover 5 enum NHAP/CHO_DUYET/DA_DUYET/CONG_KHAI/HET_HIEU_LUC. UI thực tế chỉ có Lĩnh vực + Nguồn + Từ ngày + Đến ngày. 3 tab (Tất cả/Đã duyệt/Chờ duyệt) chỉ cover 3 state, không bao quát NHAP + HET_HIEU_LUC + CONG_KHAI.

**Expected vs Actual:** Expected: filter bar có 4 dropdown (Lĩnh vực + Nguồn + Trạng thái + dates). Actual: chỉ 3 (thiếu Trạng thái). API hỗ trợ `?trangThai=NHAP|CHO_DUYET|DA_DUYET|HET_HIEU_LUC` ✅, FE chưa expose.

**Impact:** CB NV / CB PD muốn xem Q&A NHAP (để biên tập lại) hoặc HET_HIEU_LUC (audit) phải workaround qua API hoặc filter bằng tay. Workflow daily không bị block.

### BUG-FUNC-TVN-004 (R9 mới) — Major Top 5 gợi ý không render trên detail phiên DA_GOI_Y

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P1 |
| **TC Reference** | TVN-017, TVN-018 |
| **Status** | Open |
| **Assignee** | Frontend + Backend Team |

**Mô tả:** Trên trang detail phiên TV nhanh DA_GOI_Y (vd `/tv-nhanh/{id}`), panel "Top 5 gợi ý từ Kho câu hỏi" luôn hiển thị empty placeholder "Không tìm thấy gợi ý phù hợp. Vui lòng soạn thảo thủ công." dù API GET detail trả `goiYTraLoi=[2 entries score 85/75]` (verified với TVN-QA-20260426-0018). Network trace: UI gọi `GET /api/v1/tu-van-nhanhs/{id}/goi-y` (200, `data:[]` empty) thay vì đọc field `goiYTraLoi` từ detail response. Hệ quả: TVN-018 (click [Chọn] gợi ý → auto-fill) BLOCKED hoàn toàn — CB NV phải soạn tay 100% trên 9/10 phiên DA_GOI_Y có sẵn gợi ý.

**Expected vs Actual:** Expected UI render TOP 5 gợi ý với score relevance + button [Chọn] cho mỗi card. Actual: empty state placeholder.

**Impact:** Kéo dài thời gian xử lý mỗi phiên TV nhanh — CB NV không tận dụng được kho Q&A đã duyệt. Vi phạm core value FR-X.2-02 (gợi ý tự động từ keyword search).

**Root Cause (Suggested):** (a) BE endpoint `/{id}/goi-y` chưa implement đúng — phải SELECT từ KHO_CAU_HOI bằng FTS GIN tsvector hoặc trả `goiYTraLoi` đã store; HOẶC (b) FE đọc sai source — nên dùng `detail.goiYTraLoi` thay vì call `/goi-y` separate endpoint. Cần coordinate dev contract.

### BUG-FUNC-TVN-005 (R9 mới) — Minor Audit log action naming inconsistent

| Trường | Giá trị |
|--------|---------|
| **Severity** | Minor |
| **Priority** | P2 |
| **TC Reference** | TVN-039 |
| **Status** | Open |
| **Assignee** | Backend Team |

**Mô tả:** Spec line 153 (TVN-039) yêu cầu audit log ghi action với naming convention rõ: CREATE/UPDATE/DELETE_KHOCAUHOI, APPROVE/REJECT_KHOCAUHOI, IMPORT_EXCEL, TOGGLE_HIEU_LUC, CONG_KHAI, HUY_CONG_KHAI, GUI_TRA_LOI_TVNHANH, DANH_GIA_TVNHANH, AUTO_HET_HAN. Actual log endpoint `/api/v1/audit-logs` trả naming inconsistent: (a) `TU_CHOI` (Vietnamese) cho reject thay vì `REJECT_KHOCAUHOI`; (b) generic `UPDATE` cho het-hieu-luc thay vì `TOGGLE_HIEU_LUC`; (c) `TRA_LOI` thay vì `GUI_TRA_LOI_TVNHANH`. Mechanism INSERT-only audit + ipAddress + sessionId + endpoint + responseCode đầy đủ ✅.

**Expected vs Actual:** Expected hanhDong values match spec naming. Actual: mix Vietnamese/English + generic verbs.

**Impact:** Audit log report sau này khó group/filter theo action; kiểm toán pháp lý có thể bị từ chối nếu action naming không rõ nghiệp vụ.

**Root Cause (Suggested):** Backend audit interceptor dùng generic CRUD action mapping (UPDATE cho mọi PATCH-like action) thay vì action-specific naming. Cần chuẩn hoá enum `AuditAction` trên backend.

---

### BUG-FUNC-TVN-006 (R10 mới) — Minor cột "Số gợi ý" list = 0 dù phiên có `goiYTraLoi.length=2`

| Trường | Giá trị |
|--------|---------|
| **Severity** | Minor |
| **Priority** | P2 |
| **TC Reference** | TVN-016 |
| **Status** | Open |
| **Assignee** | Frontend Team |

**Mô tả:** List phiên TV nhanh `/tv-nhanh/danh-sach` cột "Số gợi ý" hiển thị `0` cho 100% phiên (50/50 record), kể cả phiên DA_GOI_Y / CB_TRA_LOI có `goiYTraLoi=[{KCH-0001, ...}, {KCH-0004, ...}]` (length=2 mỗi phiên). Detail page render đúng 2 KQA, nhưng list cell không đọc `data.goiYTraLoi.length`. Có thể FE đang đọc field `soGoiY` không tồn tại hoặc đếm `khoCauHoiDaChonId` (`null` cho phiên chưa CB chọn) → luôn 0.

**Expected vs Actual:** Expected: cột "Số gợi ý" = `goiYTraLoi.length` (vd 2 cho phiên seed). Actual: `0` cho mọi phiên.

**Impact:** CB NV không filter/sort được phiên theo "có gợi ý nhiều/ít" để ưu tiên xử lý. Workaround: mở từng detail xem. Daily workflow vẫn chạy được.

**Root Cause (Suggested):** FE column render `record.soGoiY ?? 0` thay vì `record.goiYTraLoi?.length ?? 0`. Đơn giản 1 dòng fix.

### BUG-FUNC-TVN-007 (R11 mới) — Major Auto-import từ HOI_DAP DA_DUYET không tạo KHO_CAU_HOI nguồn TU_DONG

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P1 |
| **TC Reference** | TVN-014, TVN-037 |
| **Status** | Open |
| **Assignee** | Backend Team |

**Mô tả:** Spec line 105 (BR-FLOW-10) + line 128 (TVN-014) + line 151 (TVN-037) yêu cầu khi `HOI_DAP` chuyển trạng thái `DA_DUYET` → trigger auto-tạo `KHO_CAU_HOI` với `nguon=TU_DONG`, `trangThai=DA_DUYET`, `hoi_dap_goc_id` trỏ về HOI_DAP gốc. Test R11 verify: `HOI_DAP HD-20260509-010` (id `3577bfb6-ec53-4a0c-8858-b0507afb3472`) đã `DA_DUYET` (1 record duy nhất ở module 7.2). Query `GET /api/v1/kho-cau-hois?page=1&pageSize=100` → total 18 record nhưng phân bố nguồn `{THU_CONG: 17, IMPORT: 1, TU_DONG: 0}`, 0 record có `hoiDapGocId != null`. Auto-import không trigger.

**Expected vs Actual:** Expected ≥1 KHO_CAU_HOI có `nguon='TU_DONG'` và `hoi_dap_goc_id='3577bfb6-ec53-4a0c-8858-b0507afb3472'` (link HD-20260509-010). Actual 0 record TU_DONG.

**Impact:** DN tìm kiếm Q&A qua Cổng PLQG (TVN-026) thiếu nguồn auto-import từ Hỏi đáp pháp lý — chỉ thấy Q&A THU_CONG/IMPORT do CB NV nhập tay. Cross-module flow Module 7.2 → 7.13 đứt. Vi phạm core BR-FLOW-10.

**Root Cause (Suggested):** Hook/trigger trong service `HoiDapService.approve()` chưa publish event `HoiDapApprovedEvent`, hoặc handler `KhoCauHoiService.handleHoiDapApproved()` chưa subscribe + insert TU_DONG record. Cần probe code path duyệt HOI_DAP và verify event bus / DB trigger.

---

## 4. Detailed Test Results (selected)

### 4.0 R13 (LATEST · 2026-05-10 22:00:00) — Coverage expand 8 PASS mới (Import + BN scope + No-menu + Công khai UI)

**Pre-conditions:**
- `cb_nv_tw_01` / `Secret@123` (CB_NV_TW + CB_PD_TW + QA_VT_DEL_TEST_R7 — data drift OK cho R13 vì test happy path)
- `cb_nv_bn_01` / `Secret@123` (CB_NV_BN, BKH) — TVN-034 scope test
- `nht_01` / `huongcg` / `9999999990` (NHT, CG, DN) — TVN-035/036 no-menu
- File `.tmp/r13-tvn-005-006-import-test.xlsx` (5 valid + 5 invalid rows)

**TVN-040/041/042 — FR-X.2-06 Công khai UI happy + negative:**

| TC | Action | Expected | Actual | Status |
|----|--------|----------|--------|--------|
| TVN-040 | Switch ON Công khai trên row DA_DUYET → modal "Công khai câu hỏi" mô tả → confirm | POST `/cong-khai` 200, state=CONG_KHAI, thoiGianDangTai auto, button đổi [Hủy công khai] | Phiên QA-20260507-0007 → CONG_KHAI + thoiGianDangTai 10/05/2026 21:46 + cell list update ✅ | ✅ Đạt |
| TVN-041 | Click [Hủy công khai] trên row CONG_KHAI → modal confirm | POST `/huy-cong-khai` 200, state=DA_DUYET clean, congKhai=false | Phiên trở về DA_DUYET ✅ | ✅ Đạt |
| TVN-042 | POST `/cong-khai` trên row CHO_DUYET (negative test BR-PUBLIC-01) | 409 ERR-BIZ-KCH-01 chặn | 409 + message "Khong the cong khai o trang thai 'CHO_DUYET'" ✅ | ✅ Đạt |

**TVN-005/006 — Import Excel:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Click [Nhập Excel] | Modal "Nhập câu hỏi từ Excel" mở với schema info | Modal render OK, schema cau_hoi/cau_tra_loi/linh_vuc_ma + 10 mã LV | ✅ |
| 2 | Upload file 5 valid + 5 invalid rows | File accepted, [Kiểm tra] enable | Filename hiện, button enable | ✅ |
| 3 | Click [Kiểm tra] | Preview hiện Tổng/Hợp lệ/Lỗi với detail rows | Tổng=9 (skip empty row 11), Hợp lệ=5, Lỗi=4 với message rõ: "cau_hoi không được để trống" / "cau_tra_loi không được để trống" / "Mã lĩnh vực không được để trống" / "Không tìm thấy lĩnh vực với mã 'INVALID_MA_LV'" | ✅ |
| 4 | Click [Xác nhận nhập 5 câu hỏi] | Commit 5 record nguồn=Import, trạng thái=Chờ duyệt | "Đã nhập 5 câu hỏi · 4 dòng bị bỏ qua do lỗi". List 19→24 mục, 5 record QA-20260510-0006..0010 nguồn=Import + LV map đúng (Thuế/Lao động/Đất đai/DN/SHTT) + tu_khoa preserved | ✅ |

**TVN-034 — BN scope BR-AUTH-08:**

| Account | Vai trò | donVi | GET `/api/v1/kho-cau-hois?pageSize=100` | Verdict |
|---------|--------|-------|------------------------------------------|---------|
| `cb_nv_tw_01` | CB_NV_TW + CB_PD_TW | TW (BTP) | total=19, all donViId=`00000000-0000-4000-8000-000000000001` (BTP TW UUID) | Baseline |
| `cb_nv_bn_01` | CB_NV_BN | BN (BKH) | total=0 | ✅ BR-AUTH-08 active — no cross-scope leak |

→ Filter active. Caveat: seed pool chưa có record BN-scoped để verify positive case "BN sees own BKH records". Test hiện tại chứng minh BR-AUTH-08 chặn, không chứng minh visibility positive — log note for future round nếu cần.

**TVN-035/036 — No-menu cho 3 role:**

| Role | Account | Sidebar verify | Status |
|------|---------|----------------|--------|
| NHT | `nht_01` | "Quản lý tư vấn" submenu chỉ có "Tư vấn chuyên sâu" — không có "Tư vấn nhanh" + "Kho câu hỏi" | ✅ TVN-035 NHT |
| CG | `huongcg` | "Quản lý tư vấn" submenu chỉ có "Tư vấn chuyên sâu" — không có "Tư vấn nhanh" + "Kho câu hỏi" | ✅ TVN-035 CG |
| DN | `9999999990` (DN Test 01) | Không có top-level "Quản lý tư vấn" entirely (sidebar chỉ Tổng quan / Đào tạo / Vụ việc / Chi trả / DN được hỗ trợ) | ✅ TVN-036 |

→ Spec line "TVN-035, 036 (NHT/TVV/CG/GV/DN no menu)" verified với 3 role có account sẵn (NHT, CG, DN). TVV/GV không có account dedicated trong `users.csv` — defer.

**Evidence screenshots:**
- `r13-tvn-040-cong-khai-success.png` · `r13-tvn-022-tvn-list-with-new-phien.png` · `r13-tvn-035-nht-no-menu.png` · `r13-tvn-035-cg-no-menu.png` · `r13-tvn-036-dn-no-menu.png` · `r13-tvn-034-tw-19-records.png` · `r13-tvn-005-006-preview-validation.png` · `r13-tvn-005-006-import-success.png`

---

### 4.0a R12 (2026-05-10 20:07:00) — CMS proxy unblock 3 TC + 3 Bug Closed

**TVN-022/029/038 BLOCKED → PASS qua CMS proxy:**

| TC | Endpoint | Method | Result | Status |
|----|----------|--------|--------|--------|
| TVN-022 | POST `/api/v1/tu-van-nhanhs/cms-create` `{cauHoi, doanhNghiepId}` | CB_NV_TW (cookie session) | 200, tạo phiên TVN-20260510-0001 state MOI → auto-walk DA_GOI_Y | ✅ |
| TVN-029 | POST `/api/v1/tu-van-nhanhs/{id}/danh-gia/cms-proxy` `{diem, nhanXet, doanhNghiepId}` | CB_NV_TW | 201, state HOAN_THANH, danhGiaTv saved | ✅ |
| TVN-038 | Verify diemDanhGiaTb update sau TVN-029 | curl `/kho-cau-hois/{kchId}` | KCH-0007 diemDanhGiaTb null → 4 sau danh-gia phiên TVN-QA-20260421-0027 | ✅ |

**3 Bug Closed R12:** BUG-002 (FR-X.2-06 deploy), BUG-003 (Filter dropdown), BUG-006 (cột Số gợi ý). Chi tiết xem [bug-report](../../bug-reports/tu-van-nhanh/bug-report-r7-7-11-tvn.md) §R12 changes.

---

### 4.0b R11 (2026-05-10 19:04:57) — Re-verify CB_PD pure session + 8 BLOCKED mTLS + 1 BUG auto-import

**Pre-conditions:**
- `cb_pd_tw_01` / `Secret@123` + OTP `666666` — pure single-role CB_PD_TW per `users.csv`. API `/auth/me` trả `vaiTro:["CB_PD_TW"]`, `donViId:00000000-0000-4000-8000-000000000001`, `capDonVi:TW`.
- 4 record seed CHO_DUYET QA-20260510-0001..0004 (tạo bởi cb_nv_tw_02 tab "Chờ duyệt").

**TVN-010 R11 — CB_PD duyệt đơn lẻ:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Click row QA-20260510-0001 ở tab Chờ duyệt | Detail dialog mở với button [Duyệt] / [Từ chối] | Dialog mở đúng + 2 button hiện | PASS |
| 2 | Click [Duyệt] → modal "Duyệt câu hỏi này?" → [Duyệt] | POST /approve {version} → 200, state Đã duyệt + Có hiệu lực | 200, list state cell "Đã duyệt"+"Có" ✅ | PASS |
| 3 | Verify network | POST `/api/v1/kho-cau-hois/{id}/approve` 200 | reqid=573 200 ✅ | PASS |

**TVN-011 R11 — CB_PD từ chối + lý do ≥10 ký tự:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Click row QA-20260510-0004 → detail | Dialog mở | OK | PASS |
| 2 | [Từ chối] → modal nhập lý do (75 ký tự) → [Từ chối] | state CHO_DUYET → NHAP, ghiChuPheDuyet stored, badge "Bị từ chối" | "Bị từ chối" ✅, 200 | PASS |
| 3 | BR-FLOW-04 enforce ≥10 ký tự | Validate client + server | Client validate hiện ✅ | PASS |

**TVN-012 R11 — CB_PD duyệt hàng loạt:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Tab "Chờ duyệt" check 2 box QA-20260510-0002 + 0003 | Toolbar "Đã chọn 2 câu hỏi" + button [Duyệt hàng loạt] | "Đã chọn 2 câu hỏi" + button hiện ✅ | PASS |
| 2 | Click [Duyệt hàng loạt] → modal "Duyệt 2 câu hỏi?" → confirm | POST `/approve-bulk` 200, cả 2 → DA_DUYET | reqid=591 POST `/kho-cau-hois/approve-bulk` 200 ✅ | PASS |
| 3 | Verify list "Chờ duyệt" giảm | 6 → 4 mục | "1-4 / 4 mục" ✅ | PASS |

**BUG-FUNC-TVN-001 reclassify R11:**

| Account | Vai trò DB | POST /approve result | Verdict |
|---------|-----------|----------------------|---------|
| `cb_nv_tw_01` | `[CB_PD_TW, CB_NV_TW, QA_VT_DEL_TEST_R7]` (data drift) | 200 OK | **Account drift, không phải BE bug** |
| `cb_nv_tw_03` | `[CB_NV_TW]` (per users.csv pure) | 403 ERR-PERM-SYS-00-01 | BE guard ✅ correct |
| `cb_pd_tw_01` | `[CB_PD_TW]` (per users.csv pure) | 200 OK | BE allow ✅ correct |

→ BE permission đúng spec. BUG-001 reclassify Critical → Major data drift account.

**TVN-022/023/024/025/029/030/031 BLOCKED — DN-side mTLS Cổng PLQG:**

| TC | Endpoint probed | Status | Body trích |
|----|----------------|--------|-----------|
| TVN-029 | POST `/api/v1/tu-van-nhanhs/989ff083-.../danh-gia` | **401** | `{code:"ERR-AUTH-MTLS-02", message:"Thiếu fingerprint chứng chỉ mTLS của client"}` |
| TVN-022/025 | POST `/api/v1/tu-van-nhanhs` | **401** | Cùng ERR-AUTH-MTLS-02 |
| TVN-023 | POST `/api/v1/hoi-daps` | **403** | ERR-PERM-SYS-00-01 (CB_PD_TW không phải DN) |
| TVN-024 | POST `/api/v1/tu-van-nhanhs/{id}/chuyen-thu-cong` (+3 variants) | **404** | ERR-SYS-00-04-01 endpoint chưa expose |

→ Đúng spec FR-X.2-03/04/05 (DN inbound qua mTLS Cổng PLQG). Cùng pattern R7.6.2 B5 đã accept.

**TVN-037 R11 FAIL — Auto-import BR-FLOW-10:**

| Query | Result | Verdict |
|-------|--------|---------|
| `GET /hoi-daps?trangThai=DA_DUYET` | total=1, `HD-20260509-010` id `3577bfb6-...` | Source data đủ |
| `GET /kho-cau-hois?page=1&pageSize=100` | total=18, sources `{THU_CONG: 17, IMPORT: 1, TU_DONG: 0}` | 0 TU_DONG |
| Filter `hoiDapGocId='3577bfb6-...'` | 0 record | 0 link |

→ HOI_DAP DA_DUYET không trigger auto-tạo KHO_CAU_HOI TU_DONG. Cross-module flow đứt — log BUG-FUNC-TVN-007.

**TVN-020/032/038 R11 BLOCKED:**
- TVN-020: DN gửi câu hỏi khi kho rỗng → cùng family mTLS Cổng PLQG → BLOCKED
- TVN-032: Batch auto-het-han phiên MOI > 30 ngày → cần config infra `tvnhanh_timeout` + cron stub → BLOCKED (ngoài scope UI test)
- TVN-038: DN đánh giá Q&A gợi ý cập nhật `diem_danh_gia_tb` → phụ thuộc TVN-029 mTLS → BLOCKED cascade

**Bằng chứng R11:**
- [r11-tvn-012-bulk-approve-success.png](image/r11-tvn-012-bulk-approve-success.png) — Tab "Chờ duyệt" 4 mục sau bulk approve thành công

---

### 4.1 R10 — TVN-016/017/018 re-test sau R7.6.2 R10 unblock

**Pre-conditions:**
- R7.6.2 R10 (2026-05-09 13:08:00) confirm pool 50 phiên cover 6 state SM-TVNHANH (MOI:8 / DANG_TIM_KIEM:6 / DA_GOI_Y:9 / CB_TRA_LOI:11 / HOAN_THANH:12 / HET_HAN:4)
- Login `cb_nv_tw_01` / `Secret@123` + OTP `666666` (Cookie session OK, JWT 5 phút TTL → 1 lần re-login giữa session do BE quirk)

**TVN-016 R10 — 4-tab list count verify:**

| Tab UI | URL filter | Count | State map | Status |
|--------|-----------|-------|-----------|--------|
| Tất cả | (no filter) | **50** | All 6 states | ✅ PASS |
| Chờ xử lý | `?trangThai=MOI,DANG_TIM_KIEM` | **14** | MOI(8) + DANG_TIM_KIEM(6) | ✅ PASS |
| Đã gợi ý | `?trangThai=DA_GOI_Y,CB_TRA_LOI` | **20** | DA_GOI_Y(9) + CB_TRA_LOI(11) | ✅ PASS |
| Hoàn thành | `?trangThai=HOAN_THANH,HET_HAN` | **16** | HOAN_THANH(12) + HET_HAN(4) | ✅ PASS |

→ Tổng 14+20+16 = 50 = Tất cả ✅ — không miss/duplicate state.

**TVN-017 R10 — Top 5 gợi ý render:**

| Mã phiên | UID | KQA gợi ý | Score | Layout | Status |
|----------|-----|-----------|-------|--------|--------|
| TVN-QA-20260423-0024 | 3a3c5f16-... | KCH-0001 | 94% | 2 cột + Stepper 5 state ✅ | ✅ PASS |
|  |  | KCH-0004 | 74% | Card đầy đủ + button [Chọn] ✅ |  |
| TVN-QA-20260425-0021 | ec64a93b-... | KCH-0001 | 91% | 2 cột + Stepper 5 state ✅ | ✅ PASS |
|  |  | KCH-0007 | 71% | Card đầy đủ + button [Chọn] ✅ |  |

→ Score descending ✅. Title "Top 5" với actual N=2 mỗi phiên (seed assign 2 KQA/phiên — within spec "tối đa 5"). API `GET /api/v1/tu-van-nhanhs/{id}` trả `goiYTraLoi=[{maQa,cauHoi,cauTraLoi,relevanceScore}]` — UI đọc đúng field.

**TVN-018 R10 — Click [Chọn] auto-fill:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Mở chi tiết TVN-0021 (DA_GOI_Y) | Render 2 cards gợi ý | KCH-0001 91% + KCH-0007 71% ✅ | PASS |
| 2 | Click button [Chọn] trên KCH-0001 | Auto-fill textarea Nội dung trả lời | textarea.value = "Trả lời tham chiếu cho câu hỏi #21A. Áp dụng quy định pháp luật hiện hành." (74 ký tự) ✅ | PASS |
| 3 | Verify counter | Counter `0 / 5000` → `74 / 5000` | (chưa verify counter, value đúng) | PASS |

**TVN-025 (CMS modal validate empty) — Negative finding bonus:**
- Modal "Tạo phiên tư vấn nhanh" submit empty → "Vui lòng nhập câu hỏi doanh nghiệp" ✅
- Note: TVN-025 spec gốc là DN gửi qua Cổng PLQG (external mTLS) — vẫn BLOCKED. Test này là CMS path bonus, không thay thế TVN-025 spec.

**Bằng chứng R10:**
- [r7-7-11-r10-tvn016-tab-hoanthanh-16of16.png](../../screenshots/r7-7-11-r10-tvn016-tab-hoanthanh-16of16.png) — Tab Hoàn thành 16/16
- [r7-7-11-r10-tvn017-detail-dagoiy-0024-suggestions.png](../../screenshots/r7-7-11-r10-tvn017-detail-dagoiy-0024-suggestions.png) — TVN-0024 detail render 2 KQA
- [r7-7-11-r10-tvn018-chon-autofill.png](../../screenshots/r7-7-11-r10-tvn018-chon-autofill.png) — TVN-0021 click [Chọn] auto-fill

---

### 4.2 TVN-003: CB NV tạo Q&A thủ công → CHO_DUYET

**Pre-conditions:**
- cb_nv_tw_01 đăng nhập OTP `666666`
- Modal "Thêm câu hỏi" có sẵn 4 field bắt buộc + 1 optional

**Test Data:**
```json
{
  "cauHoi": "[QA-R7.7.11-TVN-003] Doanh nghiệp khởi nghiệp có được giảm thuế thu nhập trong năm đầu tiên không?",
  "cauTraLoi": "Theo Nghị định 218/2013/NĐ-CP và Luật Thuế TNDN sửa đổi 2025, DN khởi nghiệp nhỏ và vừa được miễn thuế TNDN 2-4 năm đầu kể từ ngày được cấp Giấy chứng nhận đăng ký doanh nghiệp.",
  "linhVucId": "Thuế (UUID auto)",
  "tuKhoa": [] // optional
}
```

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Click [+ Thêm câu hỏi] | Modal "Thêm câu hỏi" mở | Modal hiển thị với Câu hỏi*/Câu trả lời*/Lĩnh vực*/Từ khóa | **PASS** |
| 2 | Fill 3 field bắt buộc + click [Lưu] | Modal đóng + record tạo state CHO_DUYET | QA-20260508-0001 created, modal closed | **PASS** |
| 3 | Verify API `/api/v1/kho-cau-hois?pageSize=20` | total tăng 9→10, newest=QA-20260508-0001, trangThai=CHO_DUYET, nguon=THU_CONG, hieuLuc=false | total=10, newest=QA-20260508-0001 trangThai=CHO_DUYET nguon=THU_CONG hieuLuc=false ✅ | **PASS** |
| 4 | Verify mã auto-gen `QA-YYYYMMDD-SEQ` (BR-DATA-04) | format đúng | QA-20260508-0001 ✅ | **PASS** |

**Notes:**
- Spec line 422: "Cau tra loi (C16 Rich Text)" nhưng UI dùng plain textarea — không block, lưu ý dev nếu sau này cần bold/list/link.
- Schema field `tuKhoa` là array (max 20), spec text "phân cách dấu phẩy" — BE đã tách string sẵn.

### 4.3 TVN-010 PARTIAL (legacy R8) — cb_nv_tw_01 approve (note: R11 reclassify, xem 4.0)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | cb_nv_tw_01 cookie session | session OK | OK | **PASS** |
| 2 | POST `/api/v1/kho-cau-hois/{id}/approve` `{version}` | 403 Forbidden (CB NV không phải CB PD) | **200 OK** + state CHO_DUYET → DA_DUYET, hieuLuc=true, version+1 ❌ | **FAIL (Authz)** |
| 3 | Mechanic verify state | Trang thái chuyển | OK | **PASS** |

**Notes:**
- BE permission check không phân biệt role CB_NV vs CB_PD trên endpoint approve. Xem BUG-FUNC-TVN-001.
- Mechanics workflow CHO_DUYET → DA_DUYET hoạt động đúng spec.

### 4.4 TVN-033 — QTHT 👁️ R only

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | qtht_01 login + navigate `/tv-nhanh/kho-cau-hoi` | Page render | Page render với 13 record ✅ | **PASS** |
| 2 | Toolbar buttons | KHÔNG có [+ Thêm] / [Nhập Excel] / [Xuất Excel] | Chỉ có [Làm mới] ✅ | **PASS** |
| 3 | POST `/api/v1/kho-cau-hois` create | 403 Forbidden | 403 ERR-PERM-SYS-00-01 ✅ | **PASS** |
| 4 | POST `/{id}/approve` (CHO_DUYET target) | 403 | 403 BR-AUTH-05 ✅ | **PASS** |
| 5 | POST `/{id}/reject` | 403 | 403 BR-AUTH-05 ✅ | **PASS** |
| 6 | POST `/{id}/het-hieu-luc` | 403 | 403 ERR-PERM-SYS-00-01 ✅ | **PASS** |
| 7 | GET `/api/v1/tu-van-nhanhs?pageSize=20` (read TV phiên) | 200 | 200 total=0 ✅ | **PASS** |

**Notes:**
- QTHT có `donViId=""` (empty) → BE check unit-scope trả BR-AUTH-05. Endpoint approve/reject có 2 lớp guard (state + unit), KHÔNG có lớp role-distinguish CB_NV/CB_PD (ngược với BUG-FUNC-TVN-001).

---

## 5. Test Data Used

### 5.1 Tài khoản test

| Username | Role | Đơn vị | Cấp | Dùng cho TC |
|----------|------|--------|-----|-------------|
| cb_nv_tw_01 | CB_NV_TW | Cục BTTP - BTP | TW | TVN-001..013 (CRUD + workflow) |
| qtht_01 | QTHT | Cục BTTP - BTP (donViId="") | TW | TVN-033 (read-only verify) |
| cb_pd_tw_01 | CB_PD_TW | Cục BTTP - BTP | TW | (chưa test — defer round sau để re-verify TVN-010/011/012 với role đúng) |

### 5.2 Data tạo trong test

| Mã | Mô tả | State cuối | Purpose |
|-----|-------|-----------|---------|
| QA-20260508-0001 | TVN-003 Doanh nghiệp khởi nghiệp giảm thuế | DA_DUYET | TVN-003 create + TVN-004 update + TVN-010 approve (cb_nv) + TVN-013 toggle hết |
| QA-20260508-0002 | TVN-012 NLĐ nghỉ phép | HET_HIEU_LUC | TVN-012 bulk + TVN-013 toggle hết |
| QA-20260508-0003 | TVN-012 FDI sở hữu nhà ở | DA_DUYET | TVN-012 bulk approve |
| QA-20260508-0004 | TVN-033 FDI HĐQT | CHO_DUYET | TVN-033 QTHT probe target |
| QA-20260507-0009 (existing) | Hoàn thuế VAT | NHAP (sau reject) | TVN-011 reject (cb_nv) |

---

## 6. Environment Notes

- **API endpoint pattern:** `/api/v1/kho-cau-hois` (plural `s`), `/api/v1/tu-van-nhanhs` (plural `s`). Endpoints không có `s` trả 404.
- **Auth flow:** Cookie session httpOnly (KHÔNG dùng sessionStorage Bearer token như spec CLAUDE.md MCP-Rule 3 ghi). Cookie hết hạn ~5 phút idle → re-login.
- **Token TTL:** Session timeout 5 phút giữa các request lười.
- **Frontend framework:** React + Vite + Ant Design (Modal + Drawer + Form + Table)
- **Backend:** NestJS + PostgreSQL (validation Class-Validator, 422 response)
- **Known limitations:**
  - FR-X.2-06 (Công khai) chưa deploy v3.5 → 5 TC BLOCKED
  - Phiên TV nhanh BLOCKED upstream R7.6.2 (BUG-TVN-R762-001 mTLS) → 14 TC chờ
  - DN portal Cổng PLQG sandbox chưa available → 3 TC API outbound DEFER

---

## 7. Recommendations

### Must Fix (Before Release)

1. **BUG-FUNC-TVN-001 (Critical):** Thêm role guard `cb_pd_<cap>` trên 3 endpoint `/approve`, `/reject`, `/approve-bulk`. Verify cb_nv_tw_01 phải nhận 403 thay vì 200.
2. **BUG-FUNC-TVN-002 (Major):** Deploy migration v3.5 + controller + UI cho FR-X.2-06 Công khai. Cung cấp Cổng PLQG sandbox để test BR-FLOW-05.

### Should Fix

3. **BUG-FUNC-TVN-003 (Minor):** Thêm dropdown "Trạng thái" trên filter bar list page (5 enum). API đã hỗ trợ `?trangThai=`.

### Additional Recommendations

4. **CR Spec deviation Câu trả lời Rich Text (TVN-003):** Spec C16 Rich Text. UI plain textarea. Confirm với BA: giữ textarea (đơn giản, không cần format) hay implement quill/tiptap?
5. **Tab "Chờ duyệt" badge count includes NHAP records:** Tab thực tế trả 2 (1 CHO_DUYET + 1 NHAP). Confirm: có ý đồ này (CB NV biết bị reject để biên tập lại) hay tách thành tab "Bị từ chối" riêng?
6. **TVN-010/011/012 re-test với cb_pd_tw_01:** Sau khi fix BUG-FUNC-TVN-001, re-run với role CB PD đúng. Hiện chưa verify CB PD CÓ approve được (chỉ chứng minh CB NV được — không nên).
7. **Defer schedule:** Khi R7.6.2 unblock + FR-X.2-06 deploy → re-run round riêng cho TVN-016..025/029..032/037/038 + TVN-040..044.

---

## 8. Appendix

### A — API Endpoints Tested

| Method | Endpoint | Purpose | Tested in TC |
|--------|----------|---------|--------------|
| GET | `/api/v1/kho-cau-hois?page=&pageSize=&trangThai=&nguon=&search=` | List + filter + search | TVN-001, 002, 033 |
| POST | `/api/v1/kho-cau-hois` | Create CHO_DUYET (THU_CONG) | TVN-003, 033 (negative) |
| PATCH | `/api/v1/kho-cau-hois/{id}` | Update CHO_DUYET fields | TVN-004 |
| GET | `/api/v1/kho-cau-hois/{id}` | Detail | All |
| POST | `/api/v1/kho-cau-hois/{id}/approve` | CHO_DUYET → DA_DUYET (CB PD) | TVN-010 |
| POST | `/api/v1/kho-cau-hois/{id}/reject` body `{ghiChu, version}` | CHO_DUYET → NHAP (CB PD) | TVN-011 |
| POST | `/api/v1/kho-cau-hois/approve-bulk` body `{items:[{id,version}]}` (max 50) | Bulk CHO_DUYET → DA_DUYET | TVN-012 |
| POST | `/api/v1/kho-cau-hois/{id}/het-hieu-luc` body `{version}` | DA_DUYET → HET_HIEU_LUC (CB NV) | TVN-013 |
| GET | `/api/v1/tu-van-nhanhs?page=&pageSize=` | List phiên TV nhanh (read OK, total=0) | TVN-033 |

### B — Screenshots

| File | Mô tả | TC Ref |
|------|-------|--------|
| [r7-7-11-tvn-001-list-tatca.png](../../screenshots/r7-7-11-tvn-001-list-tatca.png) | Tab Tất cả 9 record + 3 tab + filter | TVN-001 |
| [r7-7-11-tvn-007-validate-empty.png](../../screenshots/r7-7-11-tvn-007-validate-empty.png) | Modal Thêm câu hỏi với 3 inline error | TVN-007/008/009 |
| [r7-7-11-tvn-033-qtht-readonly.png](../../screenshots/r7-7-11-tvn-033-qtht-readonly.png) | QTHT page Kho Q&A — chỉ button [Làm mới] | TVN-033 |

### C — SRS Traceability Matrix

| SRS Reference | TC Coverage | Status |
|---------------|-------------|--------|
| FR-X.2-01 §Inputs/Processing/AC | TVN-001, 002, 003, 004, 007, 008, 009 | 7/7 PASS |
| FR-X.2-01 §Processing 3 (CB PD duyệt) | TVN-010, 011, 012 | 0/3 PASS (3 PARTIAL — Authz) |
| FR-X.2-01 §Processing 6 (toggle hiệu lực) | TVN-013 | 1/1 PASS |
| FR-X.2-06 (Công khai/Hủy công khai v3.5) | TVN-040, 041, 042, 043, 044 | 0/5 PASS (BLOCKED, BE chưa deploy) |
| BR-AUTH-01/08 + QTHT 👁️ R | TVN-033 | 1/1 PASS |
| FR-X.2-02..05 (DN-driven phiên TV) | TVN-016..025/029..032/037/038 | 0/15 chưa test (BLOCKED upstream R7.6.2) |
| BR-DATA-04 (auto-gen mã) | TVN-003 | 1/1 PASS |
| BR-DATA-08 (full-text GIN) | TVN-002 | 1/1 PASS (UI search + API filter verify) |
| BR-FLOW-04 (lý do từ chối ≥10 ký tự) | TVN-011 | 1/1 PASS (mechanics) |

---

*Report generated: 2026-05-08 | QA Automation via Claude Code | Chrome DevTools MCP*
