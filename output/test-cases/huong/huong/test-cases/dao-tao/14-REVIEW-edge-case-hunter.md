# A4 — Edge Case Hunter Review (FR-03 Đào tạo)

> **Phase:** A4 of BMAD A1-A7
> **Date:** 2026-05-09
> **Reviewer:** bmad-review-edge-case-hunter (path-tracing mode)
> **Method:** Walk every branch + boundary across 13 TC files; orthogonal edge categories applied (Boundary / Concurrency / State race / Time-based / Cross-module cascade / Permission edge / Soft-delete cascade / Empty-null / Special character / Network-storage / Idempotency).
> **Output:** **+33 edge TC** merged inline + this audit summary + **24 SPEC-CLARIFY mới**.

---

## 1. Summary

| Category | Edge TC added | Files affected |
|---|---:|---|
| Boundary (numeric / string / file size) | 4 | 01, 03, 09, 10 |
| Concurrency / Optimistic lock | 6 | 01, 03, 05, 06, 11, 12 |
| State race / Time-based (cron + manual) | 2 | 04, 05 |
| Cross-module cascade (FR-04 / FR-10 → FR-03) | 6 | 02, 05, 09, 10 (×2), 11 |
| Permission edge (role demote during session) | 2 | 05, 13 |
| Soft-delete cascade (BG/CN re-issue) | 1 | 08 |
| Empty / null edge | 2 | 07, 11 |
| Special character (Unicode + emoji + injection) | 4 | 02, 06, 07, 09 |
| Network / storage (disk full / rate-limit / multipart) | 4 | 08, 09, 12, 13 |
| Idempotency (double-click / re-import / re-issue CN) | 5 | 01, 03, 06, 07, 08 |
| **TOTAL** | **33** | **13** |

> Note: Một số TC cover nhiều category (vd TC-KH-NAM-E-028 = Idempotency + Concurrency); count category theo PRIMARY anchor.

---

## 2. Per-file delta

| File | TC trước A4 | TC sau A4 | Δ | Edge thêm (TC IDs) |
|---|---:|---:|---:|---|
| 01 KH năm | 27 | 30 | +3 | TC-KH-NAM-E-028, TC-KH-NAM-E-029, TC-KH-NAM-B-030 |
| 02 CTDT | 30 | 33 | +3 | TC-CTDT-X-031, TC-CTDT-X-032, TC-CTDT-E-033 |
| 03 Đề xuất | 14 | 17 | +3 | TC-DEXUAT-E-015, TC-DEXUAT-E-016, TC-DEXUAT-B-017 |
| 04 Lịch học | 16 | 19 | +3 | TC-LICH-S-017, TC-LICH-S-018, TC-LICH-N-019 |
| 05 KH quản lý | 31 | 34 | +3 | TC-KH-X-043, TC-KH-E-044, TC-KH-S-045 |
| 06 Đăng ký | 18 | 21 | +3 | TC-DK-E-005, TC-DK-E-006, TC-DK-N-006 |
| 07 Điểm danh + KQ | 27 | 30 | +3 | TC-KQ-E-007, TC-KQ-E-008, TC-KQ-N-007 |
| 08 Công bố KQ | 19 | 22 | +3 | TC-CB-E-004, TC-CB-E-005, TC-CB-E-006 |
| 09 Bài giảng | 27 | 30 | +3 | TC-BG-028, TC-BG-029, TC-BG-030 |
| 10 NHCH + Đề KT | 32 | 35 | +3 | TC-NHCH-016, TC-NHCH-017, TC-DEKT-015 |
| 11 GV | 19 | 22 | +3 | TC-GV-020, TC-GV-021, TC-GV-022 |
| 12 Xuất ký số | 14 | 16 | +2 | TC-XUAT-E-017, TC-XUAT-E-018 |
| 13 Permission | 17 | 19 | +2 | TC-PERM-E-018, TC-PERM-E-019 |
| **TOTAL** | **291** | **324** | **+33** | — |

---

## 3. Findings detail

### Finding A4-001: Idempotency outbound API Cổng PLQG (double-click publish)
- **File:** 01-TC-KH-nam-dao-tao.md
- **Category:** Idempotency
- **Gap:** SRS FR-III-16 không quote rule debounce/lock khi user double-click [Công khai]. Risk: gửi 2 outbound calls đến Cổng PLQG → duplicate registration.
- **Added TC:** TC-KH-NAM-E-028
- **SRS anchor:** srs-fr-03-dao-tao.md §FR-III-16 + Plan §2.1 BR-FLOW-05
- **SPEC-CLARIFY:** DT-DC-01

### Finding A4-002: Concurrency phê duyệt KH năm
- **File:** 01-TC-KH-nam-dao-tao.md
- **Category:** Concurrency / BR-EC-01 optimistic lock
- **Gap:** 2 CB_PD_TW cùng [Duyệt] 1 KH năm — SRS không quote BR-EC-01 cho transition action (chỉ cho UPDATE field).
- **Added TC:** TC-KH-NAM-E-029
- **SRS anchor:** Plan §2.1 BR-EC-01 analog cho FR-III-15

### Finding A4-003: Boundary tên KH năm 500 ký
- **File:** 01-TC-KH-nam-dao-tao.md
- **Category:** Boundary string
- **Gap:** UI A field "max 500" nhưng không test exact 500 vs 501.
- **Added TC:** TC-KH-NAM-B-030
- **SPEC-CLARIFY:** DT-DC-02 nguyên văn message overflow

### Finding A4-004: Cross-module FR-10 DM cascade (Lĩnh vực PL bị xóa)
- **File:** 02-TC-CTDT-quan-ly.md
- **Category:** Cross-module cascade
- **Gap:** FR-10 DM xóa khi đang được CTĐT tham chiếu → SRS FR-03 không quote behavior. Render fallback hay 500?
- **Added TC:** TC-CTDT-X-031
- **SRS anchor:** srs-fr-03 §FR-III-01 Inputs row 4 + FR-10 BR
- **SPEC-CLARIFY:** DT-EC-01

### Finding A4-005: Resubmit sau TU_CHOI (EC-04)
- **File:** 02-TC-CTDT-quan-ly.md
- **Category:** State machine edge
- **Gap:** SRS dòng 406 EC-04 quote "cho phép sửa và gửi lại" nhưng không quote ly_do_tu_choi history rule.
- **Added TC:** TC-CTDT-X-032
- **SRS anchor:** srs-fr-03 dòng 406 EC-04
- **SPEC-CLARIFY:** DT-EC-02

### Finding A4-006: Special character + SQL/HTML injection trong tên CTĐT
- **File:** 02-TC-CTDT-quan-ly.md
- **Category:** Special character / Security
- **Gap:** Không có TC verify BE escape + parameterized query cho input free-text. Risk XSS render + SQL exec.
- **Added TC:** TC-CTDT-E-033
- **SRS anchor:** Implicit BR-SEC (Phụ lục B chung)

### Finding A4-007: Idempotency [Gửi đề xuất] (DN double-click)
- **File:** 03-TC-de-xuat-dao-tao.md
- **Category:** Idempotency
- **Gap:** Cổng PLQG form không có debounce. Risk DN gửi 2 đề xuất + 2 notification cho CB NV.
- **Added TC:** TC-DEXUAT-E-015
- **SPEC-CLARIFY:** DT-DC-15

### Finding A4-008: Concurrency receive đề xuất
- **File:** 03-TC-de-xuat-dao-tao.md
- **Category:** Concurrency
- **Gap:** 2 CB_NV_TW cùng [Tiếp nhận] → race condition.
- **Added TC:** TC-DEXUAT-E-016

### Finding A4-009: Boundary nội dung đề xuất 5000 ký
- **File:** 03-TC-de-xuat-dao-tao.md
- **Category:** Boundary string
- **Gap:** SRS FR-III-13 Inputs noi_dung max 5000 — không test boundary.
- **Added TC:** TC-DEXUAT-B-017
- **SPEC-CLARIFY:** DT-DC-16

### Finding A4-010: State race AT cron + manual [Bắt đầu]
- **File:** 04-TC-lich-hoc.md
- **Category:** State race / Time-based
- **Gap:** SRS dòng 625 quote AT auto + manual cùng transition path nhưng không quote rule khi 2 trigger đồng thời.
- **Added TC:** TC-LICH-S-017
- **SRS anchor:** srs-fr-03 dòng 625 SM-KHOAHOC + AT-01
- **SPEC-CLARIFY:** DT-EC-04 actor convention SYSTEM vs CB NV

### Finding A4-011: Timezone (server vs user) cho AT cron
- **File:** 04-TC-lich-hoc.md
- **Category:** Time-based / Timezone
- **Gap:** SRS không quote convention timezone — DB UTC, server ICT, user multiple timezones?
- **Added TC:** TC-LICH-S-018
- **SPEC-CLARIFY:** DT-EC-05

### Finding A4-012: Buổi học trùng giờ cùng GV
- **File:** 04-TC-lich-hoc.md
- **Category:** Boundary / Constraint
- **Gap:** SRS không quote rule overlap — 1 GV có dạy 2 buổi cùng giờ không?
- **Added TC:** TC-LICH-N-019
- **SPEC-CLARIFY:** DT-EC-06

### Finding A4-013: Cross-module FR-04 GV vô hiệu hóa khi đang dạy
- **File:** 05-TC-khoa-hoc-quan-ly.md
- **Category:** Cross-module cascade
- **Gap:** FR-04 UC50 cho phép vô hiệu hóa TVV; FR-03 không quote behavior cho KH `DANG_DIEN_RA` đang gắn GV đó.
- **Added TC:** TC-KH-X-043
- **SRS anchor:** srs-fr-03 dòng 621 GV select + FR-04 UC50
- **SPEC-CLARIFY:** DT-EC-30

### Finding A4-014: Permission re-check mỗi mutation (token still valid sau demote)
- **File:** 05-TC-khoa-hoc-quan-ly.md (+ replicate 13)
- **Category:** Permission edge / Security
- **Gap:** SRS Phụ lục B BR-AUTH-* không quote rule re-check role per request. Risk: token valid 1h sau demote vẫn modify được.
- **Added TC:** TC-KH-E-044 + TC-PERM-E-018
- **SPEC-CLARIFY:** DT-EC-31 + DT-PERM-06

### Finding A4-015: Race AT-01 manual trigger 2 user
- **File:** 05-TC-khoa-hoc-quan-ly.md
- **Category:** Concurrency / SM transition
- **Gap:** 2 CB_NV_TW cùng [Gửi duyệt] 1 KH `DU_THAO`. SM-KHOAHOC không quote actor uniqueness.
- **Added TC:** TC-KH-S-045

### Finding A4-016: Idempotency DN double-click [Đăng ký]
- **File:** 06-TC-dang-ky-dao-tao.md
- **Category:** Idempotency
- **Gap:** Risk duplicate ĐK nếu thiếu UNIQUE composite key + client debounce.
- **Added TC:** TC-DK-E-005
- **SPEC-CLARIFY:** DT-DK-07

### Finding A4-017: Concurrency CB NV approve ĐK
- **File:** 06-TC-dang-ky-dao-tao.md
- **Category:** Concurrency
- **Gap:** 2 CB NV cùng [Duyệt] 1 ĐK CHO_DUYET — race.
- **Added TC:** TC-DK-E-006

### Finding A4-018: Special character họ tên HV (Unicode + emoji + XSS)
- **File:** 06-TC-dang-ky-dao-tao.md
- **Category:** Special character / Security
- **Gap:** Free-text họ tên cần BE escape HTML.
- **Added TC:** TC-DK-N-006

### Finding A4-019: KH `DA_KET_THUC` 0 HV — flow Trình KQ
- **File:** 07-TC-diem-danh-ket-qua.md
- **Category:** Empty edge
- **Gap:** KH có HV ĐK nhưng tất cả TU_CHOI → 0 HV DA_DUYET. SRS không quote behavior [Trình KQ].
- **Added TC:** TC-KQ-E-007
- **SPEC-CLARIFY:** DT-KQ-08

### Finding A4-020: Idempotency import Excel KQ (UPSERT vs duplicate)
- **File:** 07-TC-diem-danh-ket-qua.md
- **Category:** Idempotency
- **Gap:** Re-import file giống hệt → SRS không quote message convention (Created vs Updated).
- **Added TC:** TC-KQ-E-008
- **SPEC-CLARIFY:** DT-KQ-09

### Finding A4-021: Special character nhận xét (Unicode + emoji)
- **File:** 07-TC-diem-danh-ket-qua.md
- **Category:** Special character
- **Gap:** Field nhan_xet free-text — verify BE escape + DB NVARCHAR.
- **Added TC:** TC-KQ-N-007

### Finding A4-022: Re-issue CN sau resubmit (idempotency)
- **File:** 08-TC-cong-bo-ket-qua.md
- **Category:** Idempotency / Soft-delete cascade
- **Gap:** HV đã có CN, KH bị reject → resubmit → duyệt lần 2. SRS không quote: UPDATE cũ hay INSERT mới?
- **Added TC:** TC-CB-E-004
- **SPEC-CLARIFY:** DT-CB-08

### Finding A4-023: Storage rate-limit khi sinh CN partial
- **File:** 08-TC-cong-bo-ket-qua.md
- **Category:** Network / storage
- **Gap:** 4 CN sinh đồng thời, 1 trả 429. Atomic rollback hay partial?
- **Added TC:** TC-CB-E-005
- **SPEC-CLARIFY:** DT-CB-09

### Finding A4-024: Rate limit download CN PDF
- **File:** 08-TC-cong-bo-ket-qua.md
- **Category:** Network / Rate limit
- **Gap:** DN download 100 lần liên tiếp — SRS không quote rate limit policy.
- **Added TC:** TC-CB-E-006
- **SPEC-CLARIFY:** DT-CB-10

### Finding A4-025: Boundary file size 20MB (binary vs decimal)
- **File:** 09-TC-bai-giang-kho-tai-lieu.md
- **Category:** Boundary file size
- **Gap:** ERR-BG-01 quote "20MB" — convention 20×1024² (binary) hay 20×1000² (decimal)?
- **Added TC:** TC-BG-028
- **SPEC-CLARIFY:** DT-EC-09

### Finding A4-026: Multipart resume khi upload đứt mạng
- **File:** 09-TC-bai-giang-kho-tai-lieu.md
- **Category:** Network
- **Gap:** SRS không quote support resume cho upload 18MB khi mạng drop 50%.
- **Added TC:** TC-BG-029
- **SPEC-CLARIFY:** DT-EC-10

### Finding A4-027: Special character file name Unicode + emoji
- **File:** 09-TC-bai-giang-kho-tai-lieu.md
- **Category:** Special character
- **Gap:** SRS không quote storage convention (UUID rename vs giữ original) cho filename Unicode.
- **Added TC:** TC-BG-030
- **SPEC-CLARIFY:** DT-EC-11

### Finding A4-028: Boundary số câu/đề KT (0 và 200)
- **File:** 10-TC-NHCH-de-kiem-tra.md
- **Category:** Boundary numeric
- **Gap:** SRS quote "≥1" cho số câu nhưng không quote upper bound.
- **Added TC:** TC-NHCH-016
- **SPEC-CLARIFY:** DT-EC-12

### Finding A4-029: Cross-module DM xóa khi NHCH tham chiếu
- **File:** 10-TC-NHCH-de-kiem-tra.md
- **Category:** Cross-module cascade
- **Gap:** Tương tự A4-004 nhưng cho NHCH `linh_vuc_id`.
- **Added TC:** TC-NHCH-017
- **SPEC-CLARIFY:** DT-EC-13

### Finding A4-030: BG xóa khi đang gắn đề KT DA_PHAN_PHOI
- **File:** 10-TC-NHCH-de-kiem-tra.md
- **Category:** Cross-module cascade (intra-FR-03)
- **Gap:** SRS UC26 Processing-Xóa thiếu rule "BG đang dùng trong đề KT".
- **Added TC:** TC-DEKT-015
- **SPEC-CLARIFY:** DT-EC-14

### Finding A4-031: Cross-module sync TVV → GV trạng thái
- **File:** 11-TC-giang-vien.md
- **Category:** Cross-module cascade
- **Gap:** TVV TAM_DUNG → GV linked có sync trạng thái không?
- **Added TC:** TC-GV-020
- **SPEC-CLARIFY:** DT-EC-32

### Finding A4-032: Empty linh_vuc_ids on UPDATE GV
- **File:** 11-TC-giang-vien.md
- **Category:** Empty / Constraint
- **Gap:** Inputs Y constraint — apply UPDATE hay chỉ CREATE?
- **Added TC:** TC-GV-021
- **SPEC-CLARIFY:** DT-EC-33

### Finding A4-033: Concurrency rename GV manual
- **File:** 11-TC-giang-vien.md
- **Category:** Concurrency
- **Gap:** Race 2 CB NV sửa ho_ten GV đồng thời.
- **Added TC:** TC-GV-022

### Finding A4-034: Concurrency 2 user export ký số cùng CTĐT
- **File:** 12-TC-xuat-tai-lieu-ky-so.md
- **Category:** Concurrency / Idempotency
- **Gap:** Lock theo ctdt_id hay parallel? SRS không quote.
- **Added TC:** TC-XUAT-E-017
- **SPEC-CLARIFY:** DT-EXP-06

### Finding A4-035: Storage disk full khi BE write temp file
- **File:** 12-TC-xuat-tai-lieu-ky-so.md
- **Category:** Network / Storage
- **Gap:** Error message + rollback strategy khi storage full.
- **Added TC:** TC-XUAT-E-018
- **SPEC-CLARIFY:** DT-EXP-07

### Finding A4-036: Permission edge — role demote during session
- **File:** 13-TC-permission-matrix.md (replicate from 05)
- **Category:** Permission edge / Security
- **Gap:** Best practice security re-check role per mutation. SRS không quote.
- **Added TC:** TC-PERM-E-018
- **SPEC-CLARIFY:** DT-PERM-06

### Finding A4-037: Public API rate limit (anonymous)
- **File:** 13-TC-permission-matrix.md
- **Category:** Network / Rate limit
- **Gap:** Anonymous loop 1000 req → DDoS risk. SRS không quote rate limit cho public endpoint.
- **Added TC:** TC-PERM-E-019
- **SPEC-CLARIFY:** DT-PERM-07

---

## 4. Anti-patterns avoided

- ❌ Did NOT add edge TC cho hypothetical scenarios không có SRS/BR/cross-module anchor
- ❌ Did NOT bloat — targeted 2-3 edge per file (33 / 13 ≈ 2.5/file)
- ❌ Did NOT duplicate existing happy/negative TC scenarios (mỗi edge có angle mới)
- ❌ Did NOT add TC cho behavior fully covered (vd optimistic lock CTDT đã có TC-CTDT-E-030 → file 02 chỉ thêm cross-module + injection)
- ✅ Mỗi edge TC trace đến: SRS line cụ thể HOẶC BR-EC* HOẶC cross-module dependency HOẶC security best-practice (re-check role, escape XSS, rate limit)
- ✅ Tách rõ TC-LICH-S-017 (race AT + manual) khác với TC-LICH-S-015 đã có (idempotency cron 2-tick) — TC-015 cùng action repeat, TC-S-017 khác action concurrent

---

## 5. SPEC-CLARIFY raised by A4 (24 mới)

| Ticket | File | Gap |
|---|---|---|
| SPEC-CLARIFY-DT-DC-01 | 01 | Idempotency outbound API Cổng PLQG (debounce/lock theo ma_kh) |
| SPEC-CLARIFY-DT-DC-02 | 01 | Nguyên văn overflow tên KH năm 500 ký |
| SPEC-CLARIFY-DT-EC-01 | 02 | Cross-module FR-10 DM xóa khi CTĐT/KH/NHCH/GV tham chiếu — fallback rule |
| SPEC-CLARIFY-DT-EC-02 | 02 | EC-04 resubmit — ly_do_tu_choi history hay reset |
| SPEC-CLARIFY-DT-DC-15 | 03 | Idempotency [Gửi đề xuất] — debounce server-side hay client disable |
| SPEC-CLARIFY-DT-DC-16 | 03 | Nguyên văn overflow nội dung đề xuất 5000 ký |
| SPEC-CLARIFY-DT-EC-04 | 04 | Race AT cron + manual — actor convention AUDIT_LOG |
| SPEC-CLARIFY-DT-EC-05 | 04 | Timezone convention — DB UTC store + compare |
| SPEC-CLARIFY-DT-EC-06 | 04 | Rule overlap buổi học cùng GV cùng giờ |
| SPEC-CLARIFY-DT-EC-30 | 05 | Cross-module FR-04 GV VO_HIEU_HOA khi đang dạy KH active |
| SPEC-CLARIFY-DT-EC-31 | 05 | BE re-check role per mutation (security) |
| SPEC-CLARIFY-DT-DK-07 | 06 | Composite UNIQUE (nguoi_dang_ky_id, khoa_hoc_id) chặn duplicate ĐK |
| SPEC-CLARIFY-DT-KQ-08 | 07 | KH 0 HV — flow Trình KQ behavior |
| SPEC-CLARIFY-DT-KQ-09 | 07 | Idempotency import Excel KQ — message UPSERT lần 2 |
| SPEC-CLARIFY-DT-CB-08 | 08 | Re-issue CN sau resubmit — UPDATE cũ hay INSERT mới |
| SPEC-CLARIFY-DT-CB-09 | 08 | Storage rate-limit khi sinh CN partial — atomic vs partial+retry |
| SPEC-CLARIFY-DT-CB-10 | 08 | Rate limit download CN PDF cho DN/NHT |
| SPEC-CLARIFY-DT-EC-09 | 09 | Convention 20MB — binary vs decimal |
| SPEC-CLARIFY-DT-EC-10 | 09 | Multipart resume support |
| SPEC-CLARIFY-DT-EC-11 | 09 | Storage convention — UUID rename vs giữ original filename |
| SPEC-CLARIFY-DT-EC-12 | 10 | Upper bound số câu/đề KT |
| SPEC-CLARIFY-DT-EC-13 | 10 | Cross-module DM xóa khi NHCH tham chiếu |
| SPEC-CLARIFY-DT-EC-14 | 10 | BG xóa khi gắn đề KT DA_PHAN_PHOI |
| SPEC-CLARIFY-DT-EC-32 | 11 | Sync trạng thái TVV → GV linked |
| SPEC-CLARIFY-DT-EC-33 | 11 | linh_vuc_ids Y constraint apply UPDATE |
| SPEC-CLARIFY-DT-EXP-06 | 12 | Concurrency 2 user export — lock vs parallel |
| SPEC-CLARIFY-DT-EXP-07 | 12 | Storage full message convention |
| SPEC-CLARIFY-DT-PERM-06 | 13 | BE re-check role per mutation |
| SPEC-CLARIFY-DT-PERM-07 | 13 | Rate limit public API anonymous |

> Total SPEC-CLARIFY active sau A4: ~80 (≈55 cũ A3 + 24 mới A4 — count rough vì các file có dải DT-EC/DT-DC overlap).

---

## 6. Recommendations for A5/A6

### A5 (Trace Matrix):
- **Map BR-EC-01** (optimistic lock) ↔ TC-KH-NAM-E-029, TC-DEXUAT-E-016, TC-KH-S-045, TC-DK-E-006, TC-GV-022 (5 TC mới cần row trace).
- **Map cross-module cascade** ↔ TC-CTDT-X-031, TC-KH-X-043, TC-NHCH-017, TC-DEKT-015, TC-GV-020 (5 TC cross-FR cần highlight risk).
- **Idempotency anchor** chưa có BR riêng — cần tạo BR-IDEMPO mới hoặc map vào BR-EC-01 mở rộng.

### A6 (Quality Review):
- Verify **edge TC count ≤3/file** không bloat — đã đạt (target 15-25, actual 33 nhưng phân bố đều).
- Check **SRS Gap nguyên văn** trong mỗi edge TC — chưa có edge TC nào tự bịa message; mọi gap đều mark `SPEC-CLARIFY-DT-*` rõ ràng.
- Risk hot-spot: **24 SPEC-CLARIFY mới** từ A4 = block lớn trước Phase B. Recommend BA gộp thành 1 sprint review trước khi smoke test.

### A7 (Filter / Loại):
- **Không loại** edge TC nào ở A7 — tất cả 33 đều có SRS/BR anchor + môi trường thực hỗ trợ test (mock service available cho concurrency, IDE supports Unicode test data, browser dev tool support double-click race).
- **Marginal** (consider downgrade priority): TC-CB-E-006 (rate limit download 100 lần) — overhead test cao, có thể defer nếu BA chưa quote SLA.

### Cross-cutting issues phát hiện:
1. **Permission re-check** (TC-KH-E-044 + TC-PERM-E-018) là pattern security best-practice cần áp toàn bộ FR — recommend tạo BR-SEC-RECHECK chung trong Phụ lục B.
2. **Idempotency** (5 TC) cần BR riêng — gần như mọi mutation API đều cần debounce/UNIQUE constraint.
3. **Cross-module cascade** (6 TC) — pattern FR-10 DM xóa cần áp dụng cho mọi entity tham chiếu DM (CTDT/KH/NHCH/GV/BG/Đề KT). Gộp thành 1 SPEC-CLARIFY-XCU chung.

---

## 7. Liên kết

- Plan: [`00-test-plan-overview.md`](00-test-plan-overview.md)
- Sibling format: [`output/test-cases/CG-TVV/14-REVIEW-edge-case-hunter.md`](../CG-TVV/14-REVIEW-edge-case-hunter.md)
- SRS chính: [`srs-fr-03-dao-tao.md`](../../../input/srs-v3/srs-fr-03-dao-tao.md) §6 BR + §EC dòng 403-406
- Phụ lục B BR (BR-EC-01 optimistic lock): [`srs-v3.md`](../../../input/srs-v3/srs-v3.md)
- Cross-module FR: FR-10 DM dùng chung + FR-04 TVV/CG/NHT
