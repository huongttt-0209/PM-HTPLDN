# Plan Test Chi Tiết — 16 Module PM HTPLDN

> **Mục đích:** Viết + chạy TC chi tiết field-level (BVA/EP/XSS/permission) cho **toàn bộ 16 module FR-01 → FR-16**. Khác với [`plan.md`](plan.md) (workflow + functional smoke). Bổ sung cho §G9 plan cũ.
>
> **Ngày tạo:** 2026-04-30 · **Owner:** 1 tester FT · **Estimate:** 24-30 ngày (Phase A 7-9 + Phase B 12-15 + Phase C ~5-8 ngày cộng dồn từ ~20-32 sync events × 0.3 ngày avg, có overlap song song)
>
> **Nguồn thứ tự:** [`02-thu-tu-module.md`](../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — 5 lớp dependency Lớp 1 → 5

---

## 1. Ba Phase

| Phase | Mục đích | Tool chính | Áp dụng cho |
|---|---|---|---|
| **A — Viết TC** | Sinh TC từ SRS | Skill BMAD (test-design + generate-e2e + edge-case-hunter) | 13 testable unit 📝 (chưa có TC) |
| **B — Chạy TC** | Execute TC, log bug | MCP chrome-devtools + `/qa-only` | 20 testable unit (7 ✅ + 13 sau khi A xong) |
| **C — SRS Re-sync** | Update TC + re-test khi SRS đổi | Re-use BMAD A2-A7 + MCP + diff srs-v3 vs srs-update | Event-driven, ~20-32 sync (16 FR × 1-2 lần) |

**Quy ước trạng thái mỗi module:**
- Phase A: 📝 chưa viết · 🔵 đang viết · ✅ có TC · ⚠️ partial (SRS gap)
- Phase B: 🚫 chờ TC/bug · 🟢 sẵn sàng · 🔵 đang chạy · ✅ PASS · ⚠️ partial · 🚫 FAIL
- Phase C: 📭 chờ trigger · 🔵 đang sync · ⏸️ paused (chờ user resume) · ✅ done · ⚠️ partial (bug Open mới chặn) · 🚫 block (cascade upstream)

---

## 2. Scope — 20 testable unit theo thứ tự ràng buộc nhân quả

> **Iron rule:** module Lớp N+1 chỉ test khi data Lớp N đủ. Vi phạm = TC fail dù code đúng.

| # | Lớp | Module | FR | TC | Phase A | Phase B | Bug chặn |
|---|---|---|---|---:|---|---|---|
| 1 | 1 | QTHT — Cấu hình HT | FR-10 (VIII-06) | 124 (was 79 v3.0, +45 v3.1 actual; estimate 107) | ✅ Có TC (6 UC + 4 audit, 2026-05-08) | 🟢 ready | — |
| 2 | 1 | QTHT — DM dùng chung | FR-10 (VIII-01) | 255 active (was estimate 187 v3.1; sau Codex R1+R2+R3+R4: +9 fill, −3 LOẠI, 7 REPHRASE, −9 SPEC-CLARIFY cleared; 13 DM scope sau loại FR-VIII-06 CR-02 + tree 2-tầng + 14 ERR codes + **20 SPEC-CLARIFY** active) | ✅ Có TC (10 UC + 4 audit, 2026-05-08) | 🟢 ready | — |
| 3 | 1 | QTHT — TKPQ | FR-10 (VIII-14..17, VIII-22, VIII-26) | 268 (252 functional + 16 security file 07; was 200 trước UC120 mở rộng — 6 UC + 1 permission + 1 security IDOR suite + 1 UC120 self-reg DN NEW 2026-05-10 + SM-TAIKHOAN 12 transitions + 25 ERR + cây 2-tầng v3.1 + BR 100% + 43 SPEC-CLARIFY) | ✅ Có TC (7 UC functional + 1 security + 4 audit, 2026-05-08 + Codex R2 + UC120 BMAD A1-A7 append 2026-05-10) | 🟢 ready | — |
| 4 | 1 | QTHT — Nhật ký HT | FR-10 (VIII-28) | 54 (was 46 v3.0, +8 v3.1 actual; estimate 52) | ✅ Có TC (3 UC + 4 audit, 2026-05-08) | 🟢 ready | — |
| 5 | 2 | Doanh nghiệp | FR-07 | 183 (SRS v3.1 actual sau A4 +37 + A6 +7 + Codex +5; was estimate 144, was 224 v3.0) | ✅ Có TC (6 UC + 5 audit, 2026-05-09) | 🟢 ready | — |
| 6 | 2 | CG/TVV | FR-04 | 271 v3.1 (was estimate 80 v3.0; A3 base 217 + A4 +42 edge + A6 +11 fill + Codex +1 split — 19 FR + 9 SCR + 3 SM + 7 entity + 13 BR; CHANGELOG 18 thay đổi cherry-pick COVERED + 1 OUT D.2.1 PARTIAL via SPEC-CLARIFY-27) | ✅ Có TC (14 UC + 5 audit, 2026-05-09) | 🚫 chờ bug TVCS-003/004 + W2.1 DN | — |
| 7 | 2 | Biểu mẫu | FR-09 | 84 (7 UC files inline merged) | ✅ Có TC (7 UC + 4 audit, 2026-05-06) | 🟢 ready | 3 bug-flow-BIEUMAU |
| 8 | 2 | CT HTPLDN GĐ1 | FR-15 | 85 (8 UC files inline merged) | ✅ Có TC (8 UC + 4 audit, 2026-05-06) | 🚫 chờ bug | 3 bug-flow-CTHTPLDN |
| 9 | 3 | Vụ việc TGPL ⭐ | FR-05 | 294 (14 UC files inline merged) | ✅ Có TC (14 UC + 4 audit, 2026-05-06) | 🚫 chờ bug + W2.1/W2.2 B done | BUG-FLOW-VUVIEC-001 + cascade |
| 10 | 3 | Hỏi đáp | FR-02 | 118 | 📝 chưa viết (rolled back 2026-05-08) | 🚫 chờ A | — |
| 11 | 3 | TV Chuyên sâu | FR-12 | 125 (6 UC files inline merged) | ✅ Có TC (6 UC + 4 audit, 2026-05-07) | 🚫 chờ bug + W2.2 B done | BUG-TVCS-004 + cascade W2.2 |
| 12 | 3 | Đào tạo Khóa học | FR-03 | 263 (13 UC files inline merged) | ✅ Có TC (13 UC + 4 audit, 2026-05-08) | 🚫 chờ B7 + DN/HV seed | bug-flow-KHOAHOC |
| 13 | 4 | Hợp đồng TV | FR-14 | 85 v3.5 (was estimate 50; A3 base 54 + A4 +21 edge inline + A6 +5 fill status field/entity + Codex +5 P1-1..P1-3; 2 UC + 5 accordion + Permission 16 cells) | ✅ Có TC (6 UC + 4 audit, 2026-05-10 + Codex apply) | 🚫 chờ E1 unblock | E1 unblock pending |
| 14 | 4 | Chi trả | FR-06 | 137 v3.1 (was estimate 70; A3 base 93 + A4 +39 edge inline + A6 +5 fill GAP-A5 + Codex review apply 0 add: 3 P0 BUG fix + 4 P1 + 3 P2 → 13 SPEC-CLARIFY pending BA; 14 FR + 2 SCR + 10 SM transitions + 4 owned entity + 14 BR) | ✅ Có TC (10 UC + 5 audit, 2026-05-10 + Codex apply) | 🚫 chờ E3 + #9 | E3 + Vụ việc HT |
| 15 | 4 | TV Nhanh | FR-13 | 100 v3.5 (was estimate 60; A3 base 76 + A4 +18 edge + A6 +4 fill + Codex P1 +2 — 6 UC + 5 audit + Permission 10/10 + SM-TVNHANH 8/8 transitions + 13 BR + 11 SPEC-CLARIFY) | ✅ Có TC (6 UC + 5 audit, 2026-05-10 + Codex apply) | 🚫 chờ E4 + Kho QA | E4 + Kho QA |
| 16 | 4 | Đánh giá HQ | FR-08 | 167 v3.5 (was estimate ~80; A3 base 84 + A4 +49 edge inline + A6 +11 fill GAP-A5 + Codex apply +23 — 4 P0 + 16 P1 + 10 P2 → all 30 fixed; 10 FR + 1 SCR consolidated 4 tabs + 4 owned entities + SM-DANHGIA 8 state/13 transitions + 9 BR + 22 ERR codes; 6 SPEC-CLARIFY pending BA, 2 RESOLVED) | ✅ Có TC (7 UC + 5 audit, 2026-05-10 + Codex apply) | 🚫 chờ #9 + DM Tiêu chí seed | Vụ việc HT + D2 + DM Tiêu chí UC109 |
| 17 | 5 | CT HTPLDN GĐ2 | FR-15 | 74 v3.1 (was estimate ~50; A3 base 51 + A4 +19 edge inline + A6 +3 fill GAP-A5 + Codex +1 PERM-017 + sửa TC-TH-019 + rename TC-PD-BC-010 — 7 UC + 5 audit + Permission Matrix ~33/64 explicit + SM-DOT-BC 6/6 transitions + 13 BR + 9 SPEC-CLARIFY) | ✅ Có TC (7 UC + 5 audit, 2026-05-10 + Codex apply) | 🚫 cascade | #8 + #9 + #14 |
| 18 | 5 | Báo cáo TK | FR-11 | 129 v3.1 (was estimate 80; A3 base 110 + A4 +15 edge inline + A6 +3 fill + Codex F-03 +1 PERM-000 unauth — 5 UC + 5 audit; strategy "1 đại diện + smoke" 23 BC trên 1 SCR-IX-01 thừa kế TPL-REPORT-FULL; 5 BR formal + 7 BR inline + 10 ERR + Permission 8/8 + 10 SPEC-CLARIFY) | ✅ Có TC (5 UC + 5 audit, 2026-05-10 + Codex apply) | 🚫 chờ 9 module DA_DUYET data | 9 module DA_DUYET |
| 19 | 5 | Dashboard | FR-01 | 178 v3.5 (was estimate ~40; A3 base 161 sau A1-A4 + A6 fill +7 + Codex apply +10 — 11 FR + 9 UC + SCR-I-01 30 components + 5 BR + 9 entity referenced READ-ONLY + Permission Matrix 8×7 + 5 ERR + 12 Outputs TPL-DASH-KPI; 4 SPEC-CLARIFY pending BA — DASH-02 RESOLVED by Codex P0-1/P0-2) | ✅ Có TC (8 UC + 5 audit, 2026-05-10 + Codex apply) | 🚫 chờ ≥3 record/module nguồn (HD MOI + VV 5 sống/HOAN_THANH + KH DANG_DIEN_RA/DA_KET_THUC + TVV DANG_HOAT_DONG + KQ_DG + KQ_DT) | cascade Wave 5 |
| 20 | 5 | API Kết nối | FR-16 | ~50 | 📝 chưa viết | 🚫 cascade | data CONG_KHAI |

\* 187 = TPL strategy (47 đại diện + 5×13 smoke + 75 đặc thù)

**Tổng:** 20 testable unit (16 FR Module gốc, FR-10 split 4 sub-module + FR-15 split GĐ1/GĐ2) — 12 ✅ Có TC + 8 📝 chưa viết · ~442 TC dự kiến viết thêm + 1762 đã có = **~2204 TC** toàn plan (HD rolled back; BC + CT GĐ2 done 2026-05-10)
- 12 ✅ unit: 3 QTHT (Cấu hình HT 124 + DM 255 + Nhật ký 54) + BM (W2.3 92 done 2026-05-06 + Codex) + **CT GĐ1 (W2.4 100 done 2026-05-06 + Codex)** + **VV (W3.2 done 2026-05-06)** + **TVCS (W3.3 134 done 2026-05-07 + Codex)** + **KH (W3.4 done 2026-05-08)** + **CG-TVV (W2.2 done 2026-05-09 — 271 TC)** + **DN (W2.1 done 2026-05-09 — 183 TC)** + **BC (W5.2 done 2026-05-10 — 129 TC)** + **CT GĐ2 (W5.1 done 2026-05-10 — 74 TC sau Codex)**
- 8 📝 unit: HD (rolled back) + TKPQ (đã có 200 TC trong tổng) + HĐTV + CT + TVN + ĐG + DB + API
- Đã có 1762 TC active: 3 QTHT 433 (124+255+54) + TKPQ 200 + **DN 183 v3.1** + **BM 92** + **CT GĐ1 100** + **VV 294** + **TVCS 134** + **KH 263** + **CG-TVV 271 v3.1** + **BC 129 v3.1** + **CT GĐ2 74 v3.1** (tổng 1762 = 633 QTHT + 184 TKPQ functional + 16 security + 183 DN + 92 BM + 100 CT GĐ1 + 294 VV + 134 TVCS + 263 KH + 271 CG-TVV + 129 BC + 74 CT GĐ2)
- Dự kiến viết 442 TC: HD 118 + HĐTV 50 + CT 70 + TVN 60 + ĐG 80 + DB 40 + API 50 + buffer 24

> **Quy tắc sync:** Update [`todo.md`](todo.md) cột Phase A xong → cell Phase B tự ready. Không cần file index trung gian.

---

## 3. Tools & Skills

### 3.1 Phase A — Skill BMAD

| Bước | Skill | Output | Inline-merge rule? |
|---|---|---|---|
| A1 | `bmad-domain-research` (nếu module phức tạp) | Hiểu nghiệp vụ trước khi viết | — |
| A2 | `bmad-testarch-test-design` | `00-test-plan-overview.md` | — |
| A3 | `bmad-qa-generate-e2e-tests` | `01..NN-TC-*.md` (mỗi UC = 1 file) | — (đây là source of truth) |
| A4 | `bmad-review-edge-case-hunter` | **TC mới (edge case) → MERGE TRỰC TIẾP vào file UC tương ứng (Section "Edge bổ sung")** + `08-REVIEW-edge-case-hunter.md` chỉ là log audit (proposal + reasoning + merge mapping) | ✅ **BẮT BUỘC** |
| A5 | `bmad-testarch-trace` | `09-traceability-matrix.md` (matrix BR/AC ↔ TC). KHÔNG sinh TC mới — chỉ phát hiện gap. Gap → forward sang A6 fix. | — (audit only) |
| A6 | `bmad-testarch-test-review` | `10-REVIEW-test-quality.md` (issue list + score). **TC mới (fill gap A5) → MERGE TRỰC TIẾP vào file UC tương ứng** + log review riêng | ✅ **BẮT BUỘC** |
| **A7** | **Manual review + Edit (UI/function-testable filter)** | **Loại / sửa TC chỉ test được DB/API thuần — Edit IN-PLACE file UC tương ứng** + `11-a7-filter-log.md` log action | ✅ **BẮT BUỘC** |

**Skill hỗ trợ:** `bmad-advanced-elicitation` (SRS mơ hồ), NotebookLM (verify SRS), `/browse` (explore UI thực).

**Iron Rule — Inline merge cho A4/A6/A7 (lesson learned 2026-05-06 W2.3 Biểu mẫu):**
> Mọi TC mới phát sinh từ A4/A6 hoặc TC bị xóa/sửa từ A7 PHẢI Edit trực tiếp vào file UC gốc (`NN-TC-*.md`). KHÔNG để TC sống ở file phụ (08/10/11) vì Phase B chạy `/qa-only @{path-to-NN-TC-file}` — file phụ không có B-block trong todo.md → tester sẽ MISS các TC đó.
>
> File 08/10/11 là **audit log** (proposal + reasoning + changelog), KHÔNG phải TC source. Sau A4/A6/A7, nội dung 08/10/11 là history "đã merge gì vào đâu", không phải "TC chờ chạy".

**A7 — Filter rule (lý do tester không test DB/API trực tiếp):**
- ❌ LOẠI: TC require query DB trực tiếp (vd "verify row trong bảng X", "check INDEX tồn tại"), TC require curl/Postman call API thuần (vd "POST /api/v1/... với header X"), TC verify cron job / queue / background worker không có UI feedback.
- ✏️ SỬA: TC có verification chỉ-DB → chuyển thành verification UI tương đương (vd "verify network request fired" thay "verify DB row"); TC API-only nếu module có UI bridge → re-route qua UI flow.
- ✅ GIỮ: TC chạy 100% qua UI/function user-facing — bao gồm verify network response qua MCP `list_network_requests` (API call gián tiếp khi user thao tác UI vẫn OK).

### 3.2 Phase B — MCP + skill QA

| Tool | Dùng cho |
|---|---|
| MCP `new_page` + `navigate_page` | Login, isolated context multi-role |
| MCP `take_snapshot` + `wait_for` | Lấy uid + chờ render (≥10s) |
| MCP `fill_form` + `click` + `type_text` | Field input + OTP `666666` |
| MCP `list_network_requests` | Verify API URL/payload/status |
| MCP `list_console_messages` | Bắt FE error |
| MCP `evaluate_script` | Đếm rows, dropdown virtual scroll |
| MCP `take_screenshot` | Bằng chứng + bug embed |
| `/qa-only` | Chạy batch TC — không tự fix |
| `/investigate` | Bug → root cause |
| `/qa` | **TRÁNH** — auto-fix code không phù hợp |

### 3.3 Phase C — SRS Re-sync tools

| Tool | Dùng cho |
|---|---|
| Manual diff `srs-v3/srs-fr-XX.md` vs `srs-update-05-05-2026/srs-fr-XX-{slug}-v{N}.md` | C2 Impact — list BR mới/đổi/xóa |
| BMAD A2-A7 (re-use) | C3 Re-write TC affected (partial — chỉ TC bị ảnh hưởng) |
| MCP chrome-devtools + `/qa-only` (re-use) | C4.2 Re-test 100% TC file affected qua 4-block Phase B |
| NotebookLM SRS query | C4.1 Re-validate bug cũ với SRS version mới |
| Grep `input/srs-update-05-05-2026/` | C4.1 cross-check bug status transition |

**Source folder:** `input/srs-update-05-05-2026/`
**Naming convention:** `srs-fr-{XX}-{module-slug}-v{N}.md` (vd `srs-fr-07-doanh-nghiep-v3.1.md`)
**Granularity:** per FR per version

---

## 4. Workflow chuẩn

### Phase A — 7 bước/module

```
A1. Đọc SRS srs-fr-XX.md + 02-thu-tu-module §module + sibling-check ≥2 module
A2. bmad-testarch-test-design → 00-test-plan-overview.md (template + BR + permission)
A3. bmad-qa-generate-e2e-tests → 01-TC-*.md (mỗi UC = 1 file) — SOURCE OF TRUTH
A4. bmad-review-edge-case-hunter → propose edge case
    → ⚠️ BẮT BUỘC: Edit inline vào Section "E. Edge bổ sung" của file UC tương ứng
    → Log proposal + merge mapping vào 08-REVIEW-edge-case-hunter.md (audit only)
A5. bmad-testarch-trace → 09-traceability-matrix.md (BR/AC ↔ TC matrix)
    → Gap phát hiện ở đây → forward sang A6 fix (KHÔNG sinh TC trực tiếp ở A5)
A6. bmad-testarch-test-review → review chất lượng + fix gap A5
    → ⚠️ BẮT BUỘC: TC mới (fill gap) Edit inline vào file UC tương ứng
    → Log issue + score vào 10-REVIEW-test-quality.md (audit only)
A7. Manual filter UI/function-testable → Edit IN-PLACE file UC: loại/sửa TC chỉ-DB/API thuần
    → Log action LOẠI/SỬA/GIỮ vào 11-a7-filter-log.md (audit only)
    Output: TC final chỉ chứa case chạy được qua MCP chrome-devtools.
```

**Rule cứng:**
- Mọi BR phải QUOTE SRS line; permission TC tách file riêng theo pattern DN; nếu SRS gap → log SPEC-CLARIFY, không bịa.
- A7 BẮT BUỘC trước khi đóng Phase A — TC nào không chạy được trên UI thì loại hoặc rewrite, KHÔNG để lại "chờ DB access".
- **A4/A6/A7 inline merge rule** (xem §3.1): Mọi TC mới hoặc TC bị xóa/sửa PHẢI Edit trực tiếp vào file UC gốc. File 08/10/11 chỉ là audit log, KHÔNG phải TC source. Vi phạm → Phase B miss case.

**Phase A done acceptance:**
- ✅ 7 bước A1-A7 done
- ✅ Traceability ≥95% BR + 100% AC
- ✅ 0 TC chỉ-DB/API thuần (A7 verified)
- ✅ **0 TC sống ở file phụ (08/10/11)** — mọi TC phải nằm trong file UC `NN-TC-*.md` để Phase B B-block chạy đầy đủ
- ✅ SPEC-CLARIFY listed (gửi BA Phase B)

### Phase B — 4 block/TC file (1 file `NN-TC-*.md` = 1 unit of work)

> **Đơn vị thực thi tối thiểu là 1 file TC** (vd `02-TC-tim-kiem-dn.md`), KHÔNG phải module. Mỗi file đi qua đủ 4 block (B-Seed → B-Run → B-Verify → B-Report) rồi mới chuyển sang file kế tiếp. Tránh seed dồn cuối → fail vì thiếu data.

#### B-Seed — Chuẩn bị data (BẮT BUỘC trước B-Run)

```
B-Seed.1  Đọc TC file → liệt kê data cần seed cho từng TC (báo user trước khi seed)
B-Seed.2  MCP login + navigate module liên quan → check data đã tồn tại chưa
          (data tương đương OK, KHÔNG cần exact theo TC — không tạo trùng)
B-Seed.3  Data thiếu nghiệp vụ chưa rõ → query NotebookLM SRS
          (id `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264`, KHÔNG đọc file local)
B-Seed.4  Tạo data qua chrome-devtools MCP (login đúng role tạo entity → fill_form → submit)
B-Seed.5  Output: `seed-report-{NN-TC-name}.md` — list từng record đã tạo (mã + tên + state)
```

**Rule cứng:** check trước khi seed (không tạo trùng); query NotebookLM thay vì đọc file local; report list cụ thể, KHÔNG mô tả "đã seed xong".

#### B-Run — Execute /qa-only via chrome-devtools MCP

```
B-Run.1  /qa-only @{path-to-NN-TC-file.md} (KHÔNG dùng /qa — auto-fix code không phù hợp)
B-Run.2  MCP login đúng role (MCP-Template từ CLAUDE.md) — KHÔNG navigate_page sau login
B-Run.3  Click sidebar → wait_for → take_snapshot fresh uid trước mỗi fill/click
B-Run.4  Thực thi steps + capture: take_screenshot + list_network_requests + list_console_messages
B-Run.5  So expected vs actual:
         - PASS → log 1 dòng vào execution-report
         - FAIL → /investigate → 2-source SRS verify (NotebookLM + grep local) → log bug
```

**Rule cứng:** bug có SRS ref; bug Open embed screenshot inline; dropdown AntD scroll virtual list; permission TC dùng tài khoản `_03`; OTP `666666`.

#### B-Verify — Xác minh bug trước khi report (BẮT BUỘC trước B-Report)

```
B-Verify.1  Với mỗi bug từ B-Run, mở NotebookLM SRS:
            https://notebooklm.google.com/notebook/4dd0675e-a4fa-4ea6-80ae-48e76b3fa264
            → query nghiệp vụ liên quan: "BR/AC nào áp dụng cho <hành vi quan sát>"
B-Verify.2  Kết hợp grep SRS local: `input/srs-v3/srs-fr-XX.md` cùng module
            → tìm BR/AC line tương ứng (verify text NotebookLM trả).
B-Verify.3  Phân loại 2-source (3 nhãn status):
            - ✅ VALID: Cả 2 source xác nhận hành vi sai spec → giữ trong bug-report,
              status=VALID
            - ❌ INVALID: Cả 2 source xác nhận hành vi đúng spec / expected
              → LOẠI khỏi bug-report, ghi reasoning vào Gap-report
            - ⚠️ GAP: 2 source mâu thuẫn / im lặng (NotebookLM trả 1 đằng,
              SRS local 1 nẻo, hoặc cả 2 không đề cập)
              → GIỮ trong bug-report status=GAP, ĐỒNG THỜI cross-ref SPEC-CLARIFY
              entry ở Gap-report (không drop, chờ BA clarify)
B-Verify.4  Update bug-report file: giữ cả bug VALID + bug GAP, mỗi entry MUST có:
            - Field "Status": VALID hoặc GAP
            - Bug VALID: thêm SRS ref line (vd "SRS Phụ lục B BR-XYZ-01,
              srs-fr-07.md:line-1234")
            - Bug GAP: trích dẫn NotebookLM answer + grep SRS local result +
              lý do mâu thuẫn (vd "NotebookLM trả lời: ...; SRS local line N
              không đề cập / nói khác → cần BA clarify")
B-Verify.5  Bug INVALID (case ❌) → ghi nhật ký vào Gap-report: "Đã quan sát hành vi X,
            verify NotebookLM + SRS local đều xác nhận đúng spec → loại khỏi bug list".
            Bug GAP (case ⚠️) → tạo entry SPEC-CLARIFY-{module}-{NN} ở Gap-report,
            link 2 chiều với entry trong bug-report.
```

**Rule cứng:** KHÔNG report bug nào chưa qua 2-source verify; NotebookLM > file local nhưng phải kèm grep local để bắt khoảng cách dịch thuật; bug GAP **vẫn giữ trong bug-report** với status rõ ràng (không silent drop, không tự ý reject case mâu thuẫn); chỉ bug INVALID (case ❌ — cả 2 source xác nhận đúng spec) mới loại khỏi bug-report.

#### B-Report — Lưu kết quả 4-folder structure

```
B-Report.1  Tạo folder `report-{NN-TC-name}/` trong output/execution-test/{module}/
B-Report.2  Phân loại + lưu output theo 4 subfolder:
            ├── Tcs-report/    {NN-TC-name}-execution-report-YYYY-MM-DD.md
            ├── bug-report/    bug-report-functional-{module}.md
                               (bug VALID + bug GAP — mỗi entry có field Status)
            ├── seed-report/   seed-report-{NN-TC-name}.md (đã sinh ở B-Seed)
            └── Gap-report/    gap-report-srs-{module}.md
                               (SPEC-CLARIFY entries cross-ref bug GAP +
                                reasoning bug INVALID đã loại)
B-Report.3  Update todo.md → flip ✅/⚠️/🚫 + cập nhật bảng "Tiến độ tổng"
B-Report.4  Update §2 Scope plan.md đồng bộ status module
```

**Rule cứng:** mỗi TC file = 1 folder report độc lập (dễ trace bug + seed history); Gap-report cùng folder TC file (không gộp module-level).

### Phase C — 5 step/SRS update (event-driven, re-entrant)

> **Trigger:** file mới landing trong `input/srs-update-05-05-2026/`. Phase C có thể chạy bất kỳ lúc nào sau Phase A của module — không cần đợi Phase B xong. User tự kiểm soát thứ tự ưu tiên khi nhiều file landing cùng lúc (theo Lớp dependency 1→5).

#### Default mode: `auto-c3-checkpoint`

| Step | Behavior | Pause? |
|---|---|---|
| C1 Detect | Auto | — |
| C2 Impact | Auto (kể cả list TC affected dài) | — |
| C3 Re-write | Auto (KHÔNG show TC mới preview) | ⏸️ **Pause sau C3** — báo summary, chờ user confirm proceed C4 |
| C4.1 Re-validate bug | Auto cho bug rõ ràng | ⏸️ Pause khi bug transition **ambiguous**: VALID→INVALID / GAP→VALID / VALID→GAP |
| C4.2 Re-test | Auto, **scope = 100% TC trong file affected** (Option 1 — full regression) | — |
| C5 Log | Auto | — |

**Override mode khi user request:**
- `auto`: skip mọi pause, full auto C1→C5
- `verbose`: pause sau MỖI step (C1→C2→C3→C4→C5)
- `dry-run`: chạy đến hết C2 rồi STOP, không C3-C5

#### Resume rule (khi user pause giữa chừng)

```
1. Mọi pause lưu `Last step` vào sync log row + flip Phase C status → ⏸️
2. User trigger resume bằng 1 trong 2 cách:
   a. Explicit: `Resume Phase C FR-XX vN (continue from C{step})`
   b. Implicit: `Resume Phase C FR-XX vN`
      → tôi đọc `Last step` từ sync log, tự continue từ step kế tiếp
3. Trước khi resume, verify state:
   - TC files KHÔNG bị sửa thêm sau pause (so checksum hoặc git diff)
   - Bug-report KHÔNG bị sửa thêm sau pause
   - Nếu state đã thay đổi → STOP, báo user "state inconsistent, cần re-run từ Cn"
4. Resume bắt đầu chạy → status flip ⏸️ → 🔵
```

**Mapping `Last step` → step kế tiếp:**

| Last step | Continue from |
|---|---|
| C1 | C2 |
| C2 | C3 |
| C3 | C4.1 (default checkpoint của mode `auto-c3-checkpoint`) |
| C4.1 | C4.2 |
| C4.2 | C5 |
| C5 | (đã done, không resume) |

#### C1 — Detect

```
C1.1  Scan định kỳ `input/srs-update-05-05-2026/` (hoặc user notify khi push file mới)
C1.2  Identify file mới qua naming `srs-fr-XX-{slug}-v{N}.md`
C1.3  Tạo entry mới ở `output/test-cases/_srs-sync-log.md` với date + SRS version + FR module
```

#### C2 — Impact analysis

```
C2.1  Đọc file SRS update + file SRS gốc tương ứng `input/srs-v3/srs-fr-XX.md`
C2.2  Diff content:
      - BR/AC mới (added)
      - BR/AC sửa (modified) — quote line cũ vs line mới
      - BR/AC xóa (removed)
C2.3  Map qua traceability matrix (output A5) → list TC file affected (100%)
C2.4  Output: list TC file đầy đủ tên trong sync-log row
```

**Rule cứng:** 100% TC file chứa TC affected → mark whole file affected, KHÔNG cherry-pick TC riêng lẻ.

#### C3 — Re-write (per TC file affected)

```
C3.1  A2 partial: update `00-test-plan-overview.md` nếu BR mới được thêm
C3.2  A3 partial: rewrite TC bị affected
      - BR đổi: sửa expected result
      - BR mới: thêm TC mới
      - BR xóa: xóa TC cũ
C3.3  A4: bmad-review-edge-case-hunter cho BR mới
C3.4  A5: update traceability matrix (link TC mới ↔ BR mới)
C3.5  A6: bmad-testarch-test-review chất lượng TC updated
C3.6  A7: filter UI/function-testable
C3.7  Output: TC file updated in-place + header note
      "Updated YYYY-MM-DD cho SRS FR-XX v{N}"
```

#### C4 — Re-test (Option 1: full regression — 100% TC trong từng TC file affected)

```
C4.1  Re-validate bug cũ trong `bug-report` của TC file affected:
      - Đọc list bug VALID + bug GAP cũ
      - Query NotebookLM SRS version mới + grep `srs-update-05-05-2026/`
      - Bug VALID cũ:
        → vẫn sai spec mới → giữ VALID, update SRS ref line tới version mới
        → đúng spec mới → đổi INVALID, ghi reasoning vào Gap-report
        → mâu thuẫn 2 source ở version mới → đổi GAP, log SPEC-CLARIFY
      - Bug GAP cũ:
        → spec mới đã clarify → đổi VALID hoặc INVALID
        → vẫn mâu thuẫn → giữ GAP, update note với SRS version transition

C4.2  Phase B 4-block cho TỪNG TC file affected — re-run **100% TC trong file** (Option 1):
      - Scope: KHÔNG chỉ TC mới/sửa từ C3; KHÔNG chỉ TC dependency; KHÔNG smoke subset
      - PHẢI re-run TẤT CẢ TC trong file (kể cả TC unchanged) để full regression check
      - Lý do: tránh silent miss bug khi BR đổi data shape / shared component
        (vd BR-DN-15 thêm MST validation → all CRUD TC tạo DN đều implicit affected)
      - B-Seed: re-check data đã có (data Phase A cũ vẫn dùng được nếu BR data không đổi)
      - B-Run: /qa-only @{TC file path} (full file, không filter TC ID)
      - B-Verify: 2-source verify với SRS version mới
      - B-Report: tạo file mới `re-sync-v{N}-execution-report-YYYY-MM-DD.md`
        trong folder `Tcs-report/` cũ (KHÔNG ghi đè execution report cũ)
```

**Rule cứng:** C4.2 scope = 100% TC mỗi file (Option 1, KHÔNG dùng delta-only Option 2 hay hybrid Option 3); B-Seed phải check data còn match BR mới — nếu BR đổi data shape, có thể phải seed lại; bug-report cập nhật in-place với status transition rõ ràng (vd "Originally VALID v3, now INVALID v3.1 — spec clarified that ...").

#### C5 — Log

```
C5.1  Update `output/test-cases/_srs-sync-log.md` với row mới:
      - SRS version (vd v3.1)
      - Date trigger
      - FR module
      - TC file affected (count + list)
      - Bug re-validate delta (vd "5 VALID giữ, 1 VALID→INVALID, 2 GAP→VALID")
      - Re-test status (✅ PASS / ⚠️ partial / 🚫 FAIL)
      - **Last step** (C1 / C2 / C3 / C4.1 / C4.2 / C5) — track step cuối cùng đã hoàn thành,
        dùng cho resume khi pause
      - **Phase C status** (📭 / 🔵 / ⏸️ / ✅ / ⚠️ / 🚫)
C5.2  Update §2 Scope plan.md: thêm note "SRS v{N}" vào module bị re-sync
C5.3  Update todo.md: section "C — SRS Re-sync log" với row mới + Module Phase C status flip
```

**Rule cứng:** mỗi sync event = 1 row riêng trong `_srs-sync-log.md`; KHÔNG gộp 2 SRS version vào 1 row; Phase C chỉ ✅ done khi C5.3 update todo.md xong.

---

## 5. Thứ tự thực thi (5 wave Lớp 1→5)

> Phase A và Phase B chạy **song song**: WB1 (4 module ✅) chạy ngay khi user duyệt; WA2 viết TC song song để khi WB1 xong, WB2 sẵn sàng.

| Wave | Lớp | Modules | Phase A | Phase B | Estimate |
|---|---|---|---|---|---|
| W1 | 1 | 4 QTHT | (đã có) | 🟢 ready ngay | 3 ngày |
| W2 | 2 | DN + CG-TVV + BM + CT GĐ1 | WA2.1-2.3 (1.5 ngày) | WB2.1 ngay; WB2.2-4 sau A | 4 ngày (gồm A) |
| W3 | 3 | HD + VV + TVCS + KH | WA3.1-3.3 (2.5 ngày) | WB3.1 ngay; WB3.2-4 sau A | 3 ngày (gồm A) |
| W4 | 4 | HĐTV + CT + TVN + ĐG | WA4.1-4.4 (2 ngày) | sau A + Trụ E unblock | 2 ngày |
| W5 | 5 | CT GĐ2 + BC + DB + API | WA5.1-5.4 (2 ngày) | sau A + cascade | 2 ngày |

**Checkpoint sau mỗi wave:** user duyệt qua wave kế (xem `todo.md`).

---

## 6. Strategy đặc thù

### 6.1 TPL-DM-CRUD-chung (W1.3)
47 TC × 14 DM = 658 → **187 TC** (47 đại diện DM Lĩnh vực + 5×13 smoke + 75 đặc thù 9 DM riêng)

### 6.2 Module bị block bug Open (Phase B)
- **CG-TVV (#6):** Phase A vẫn viết TC, Phase B defer chờ BUG-TVCS-003/004 close
- **Vụ việc (#9):** Phase A viết TC, Phase B defer chờ BUG-VUVIEC-001 close
- **Hỏi đáp 4 TC (#10):** skip do BUG-HOIDAP-001+004, đánh dấu defer

### 6.3 Module phụ thuộc Trụ E
HĐTV (E1), CT HTPLDN (E2), Chi trả (E3), TV nhanh (E4) — daily monitor [`plan.md` §3.3 Trụ E](plan.md). Cuối T2 chưa unblock → defer Wave 4-5.

---

## 7. Acceptance criteria

| Mức | Ngưỡng |
|---|---|
| Module Phase A DONE | 7 bước A1-A7 + traceability ≥95% BR + 0 SPEC-CLARIFY pending + 0 TC chỉ-DB/API thuần |
| Module Phase B PASS | P0 100% + P1 ≥90% + 0 Critical Open |
| Module Phase C DONE | 100% TC affected re-tested PASS + bug cũ re-validated với SRS version mới + sync-log entry complete + todo.md status flip |
| Wave PASS | Mọi module trong wave PASS hoặc DEFER có lý do |
| Plan PASS | 5/5 wave + Aggregate report duyệt + 0 SRS update pending re-sync |

---

## 8. Risk

| Risk | Impact | Mitigation |
|---|---|---|
| Skill BMAD generate TC chất lượng thấp | High | A4 edge-case-hunter + A6 test-review bắt buộc |
| 5 bug Critical Open chặn ≥4 module Phase B | High | Defer module bị block, chạy module 🟢 trước |
| Trụ E không unblock | High | DEFER Wave 4-5 nếu cuối T2 chưa ready |
| Phase A blow up >2 ngày/module | Medium | Cap cứng, P0 trước, P1/P2 defer |
| 5 mâu thuẫn SRS pending BA | Medium | Quote BA email, không log bug mới |
| R9 — SRS update cascade nhiều module cùng lúc (Phase C) | Medium | User tự kiểm soát thứ tự ưu tiên theo Lớp dependency 1→5; KHÔNG cap cứng số file/ngày — tùy bandwidth thực tế |
| R10 — Bug VALID cũ thành INVALID khi SRS đổi (Phase C C4.1) | Low-Med | Re-validate 2-source bắt buộc; ghi rõ status transition trong bug-report ("VALID v3 → INVALID v3.1 do spec clarify ...") |

---

## 9. Output kỳ vọng

```
input/srs-update-05-05-2026/                                   ← Phase C input (MỚI)
├── srs-fr-{XX}-{module-slug}-v{N}.md                          ← per FR per version
│   (vd srs-fr-07-doanh-nghiep-v3.1.md)
└── _changelog.md (optional)                                   ← master changelog cross-FR

output/test-cases/{module}/                                    ← Phase A output
├── 00-test-plan-overview.md
└── 01-TC-*.md ... NN-TC-*.md

output/test-cases/_srs-sync-log.md                             ← Phase C running log (MỚI)

output/execution-test/{module}/                                ← Phase B output (+ Phase C re-test)
├── report-01-TC-{name}/                                       ← 1 folder/TC file
│   ├── Tcs-report/
│   │   ├── 01-TC-{name}-execution-report-YYYY-MM-DD.md       ← B-Run initial
│   │   └── re-sync-v{N}-execution-report-YYYY-MM-DD.md       ← Phase C re-test (MỚI, mỗi version 1 file)
│   ├── bug-report/      bug-report-functional-{module}.md     ← updated in-place khi C4.1 re-validate
│   ├── seed-report/     seed-report-01-TC-{name}.md
│   └── Gap-report/      gap-report-srs-{module}.md            ← updated với SPEC-CLARIFY khi SRS đổi
├── report-02-TC-{name}/
│   └── ... (cấu trúc như trên)
├── ...
└── report-NN-TC-{name}/

output/execution-test/_aggregate-detailed-tc.md                ← cuối plan
```

**Ví dụ thực tế (module DN, 6 TC file):**
```
output/execution-test/quan-ly-doanh-nghiep/
├── report-01-TC-quan-ly-dn-CRUD/
│   ├── Tcs-report/      01-TC-DN-CRUD-execution-report-2026-05-05.md
│   ├── bug-report/      bug-report-functional-doanh-nghiep.md
│   ├── seed-report/     seed-report-01-TC-quan-ly-dn-CRUD.md
│   └── Gap-report/      gap-report-srs-doanh-nghiep.md
├── report-02-TC-tim-kiem-dn/
├── report-03-TC-import-excel-dn/
├── report-04-TC-tab-ho-so-pl-dn/
├── report-05-TC-tab-lich-su-tab-chi-tra/
└── report-06-TC-permission-matrix/
```

**Folder đã có sẵn (giữ nguyên tên cấp module — sẽ thêm `report-NN-TC-*/` con):**
- `execution-test/QTHT/{Cau-hinh-he-thong, DM-dung-chung, Nhat-ky-he-thong, tai-khoan-phan-quyen}` → cho W1.1-W1.4
- `execution-test/quan-ly-doanh-nghiep/` → cho W2.1
- `execution-test/chuyen-gia-tu-van-vien/` → cho W2.2
- `execution-test/hoi-dap/` → cho W3.1

**Folder cần tạo mới cấp module (13 module 📝, sau đó thêm `report-NN-TC-*/` con khi bắt đầu B-Run):**
- `execution-test/bieu-mau/` (W2.3)
- `execution-test/ct-htpldn-gd1/` (W2.4)
- `execution-test/vu-viec/` (W3.2)
- `execution-test/tv-chuyen-sau/` (W3.3)
- `execution-test/dao-tao/` (W3.4)
- `execution-test/hop-dong-tv/` (W4.1)
- `execution-test/chi-tra/` (W4.2)
- `execution-test/tv-nhanh/` (W4.3)
- `execution-test/danh-gia/` (W4.4)
- `execution-test/ct-htpldn-gd2/` (W5.1)
- `execution-test/bao-cao/` (W5.2)
- `execution-test/dashboard/` (W5.3)
- `execution-test/api-ket-noi/` (W5.4)

---

## 10. Liên kết

- Todo (Phase A + B sync 1 file): [`todo.md`](todo.md)
- Plan tổng workflow: [`tasks/plan.md`](../plan.md)
- Source thứ tự module: [`02-thu-tu-module.md`](../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md)
- Test strategy: [`test-strategy.md`](../../output/test-strategy.md)
- BR Phụ lục B: [`srs-v3.md` line 3939-4088](../../input/srs-v3/srs-v3.md)
- Permission matrix: [`permission-matrix.md`](../../output/permission-matrix.md)
- Template TC: [`output/template/`](../../output/template/)
