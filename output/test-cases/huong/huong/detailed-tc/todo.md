# TODO — Plan Test Chi Tiết 16 Module (Phase A + B sync 1 file)

**Plan:** [plan.md](plan.md) · **Today:** 2026-04-30
**Estimate:** 24-30 ngày (A 7-9 + B 12-15 + C ~5-8 ngày cộng dồn từ ~20-32 sync events × 0.3 ngày avg)
**Tool A:** Skill BMAD · **Tool B:** MCP chrome-devtools + `/qa-only` · **Tool C:** Re-use BMAD A2-A7 + MCP + diff `srs-v3/` vs `srs-update-05-05-2026/`

**Icon:** ✅ xong · 🟢 sẵn sàng · 🔵 đang làm · ⏳ chờ data · ⚠️ partial · 🚫 block · 📝 chưa viết TC

**Quy ước:** mỗi module có 2 task `A` + `B` nested. Task `B` chia tiếp theo từng **TC file** (1 file = 1 unit), mỗi TC file đi qua 4 block **B-Seed → B-Run → B-Verify → B-Report**. Update A xong → flip B từ 🚫 chờ TC → 🟢 hoặc 🚫 chờ bug khác. **Task C — SRS Re-sync** event-driven (không cố định ngày) — mỗi file SRS update mới landing trong `input/srs-update-05-05-2026/` → thêm row vào section "C — SRS Re-sync log" + flip Module Phase C status.

---

## 📋 Template prompt per-TC-file (workflow chuẩn cho mọi TC file)

> Reference: [`plan.md` §4 Phase B](plan.md). Copy-paste template dưới đây mỗi khi chạy 1 TC file mới — chỉ thay biến `{NN-TC-name}` + `{module-folder}`.

```
Thông tin môi trường:
- URL: http://103.172.236.130:3000/
- OTP: mặc định 666666
- Tài khoản test: @/c:/HoaAG/LuatDN5/Ver3.1/input/users.csv
- File TC: @/c:/HoaAG/LuatDN5/Ver3.1/output/test-cases/{module-folder}/{NN-TC-name}.md

═══════ B-Seed: Chuẩn bị data ═══════
1. Rà soát toàn bộ TC trong file → liệt kê những TC nào cần seed data → BÁO CÁO trước khi seed.
2. Với mỗi data cần seed:
   a. Dùng chrome-devtools MCP login + check hệ thống xem đã có data tương đương chưa
      (KHÔNG cần exact theo TC, tương đương là OK — không tạo trùng).
   b. Nếu chưa có, query NotebookLM SRS để hỏi cách tạo:
      https://notebooklm.google.com/notebook/4dd0675e-a4fa-4ea6-80ae-48e76b3fa264
      (LUÔN dùng NotebookLM, KHÔNG đọc file local).
   c. Tạo data qua chrome-devtools MCP.
3. Sau B-Seed: liệt kê + báo cáo danh sách record đã tạo (mã + tên + state).

═══════ B-Run: Execute test ═══════
4. /qa-only chạy test theo file TC trên qua chrome-devtools MCP.

═══════ B-Verify: Xác minh bug trước report ═══════
5. Sau khi /qa-only chạy xong, với MỖI bug log được:
   a. Truy cập NotebookLM SRS:
      https://notebooklm.google.com/notebook/4dd0675e-a4fa-4ea6-80ae-48e76b3fa264
      → query BR/AC nào áp dụng cho hành vi quan sát.
   b. Kết hợp grep SRS local (input/srs-v3/srs-fr-XX.md) → tìm line tương ứng.
   c. Phân loại 2-source:
      - ✅ Cả 2 source xác nhận sai spec → BUG VALID, giữ trong bug-report (status: VALID).
      - ❌ Cả 2 source xác nhận đúng spec → LOẠI khỏi bug-report (ghi reasoning vào Gap-report).
      - ⚠️ 2 source mâu thuẫn / im lặng → GIỮ trong bug-report (status: GAP — chờ BA clarify),
        ĐỒNG THỜI cross-ref entry SPEC-CLARIFY tương ứng ở Gap-report.
   d. Bug VALID → thêm SRS ref line vào entry (vd "SRS BR-XYZ-01, srs-fr-07.md:1234"; status: VALID).
   e. Bug GAP → entry phải có: trích dẫn NotebookLM trả lời + grep SRS local trả lời + lý do mâu thuẫn
      (vd "NotebookLM nói X, SRS local line 234 không đề cập → cần BA clarify"; status: GAP).
   f. Bug bị loại (case ❌) → ghi reasoning vào Gap-report (không silent drop).

═══════ B-Report: Lưu kết quả 4-folder ═══════
6. Lưu output vào: output/execution-test/{module-folder}/report-{NN-TC-name}/
   ├── Tcs-report/      {NN-TC-name}-execution-report-YYYY-MM-DD.md
   ├── bug-report/      bug-report-functional-{module}.md (bug VALID + bug GAP, mỗi entry có status)
   ├── seed-report/     seed-report-{NN-TC-name}.md (đã sinh ở B-Seed)
   └── Gap-report/      gap-report-srs-{module}.md (SPEC-CLARIFY cho bug GAP + reasoning bug bị loại)
7. Update todo.md: flip ✅/⚠️/🚫 trên dòng B của TC file → cập nhật bảng "Tiến độ tổng".
```

**Iron rules:**
- B-Seed BẮT BUỘC trước B-Run — tránh fail vì thiếu data → false negative.
- B-Verify BẮT BUỘC trước B-Report — KHÔNG report bug nào chưa qua 2-source check.
- Bug-report file chứa **2 status**: `VALID` (đã verify sai spec) + `GAP` (mâu thuẫn 2 source, chờ BA clarify). KHÔNG drop bug GAP.
- Check existing trước khi tạo mới — không trùng data.
- NotebookLM > file local — luôn query trước.
- 1 TC file = 1 folder `report-{NN-TC-name}/` độc lập.
- **Phase A → B handoff rule (lesson learned 2026-05-06 W2.3):** B-block chỉ ref file UC gốc `NN-TC-*.md`. File phụ A4/A6/A7 (08/10/11) là audit log, KHÔNG phải TC source. Mọi TC mới từ A4/A6 hoặc TC bị A7 sửa PHẢI đã merged inline vào file UC trước khi flip Phase A ✅. Verify bằng `grep -c "^| TC-" {NN-TC-file}.md` khớp với count "Tổng số TC" footer.

---

## Tiến độ tổng

| Wave | Lớp | Modules | TC tổng | Phase A | Phase B |
|---|---|---|---:|---|---|
| W1 | 1 | 4 QTHT | 701 functional + 16 security (W1.1 54 + W1.2 124 + W1.3 255 + W1.4 252 = 184 base + 68 UC120 / 16 security vs estimate 52+107+187+178 = 524, +177 do cover sâu SRS + Codex R1+R2+R3+R4+R5 reviews + UC120 mở rộng 2026-05-10) | ✅ W1.1+W1.2+W1.3+W1.4 ✅ (redone + Codex R2 cho W1.4 done 2026-05-08; W1.4 mở rộng UC120 2026-05-10) | 🟢 W1.1 (3 file) + ⚠️ W1.2 (5 file done 2026-05-09 — 8 bug, Phân công vi phạm BA Q11. Tab Quy trình HT BA bỏ scope) + ⚠️ W1.3 (10 file done 2026-05-09 — 11 bug Critical/High) + ⚠️ W1.4 (B1 Vai trò + B2 TK done 2026-05-09 — 5 bug, scope điều chỉnh bỏ UC114+UC115. B3-B7 deferred. **B7 UC120 NEW 12-TC ready 2026-05-10**) |
| W2 | 2 | DN + CG-TVV + BM + CT GĐ1 | 631 (183 DN v3.1 actual + 271 CG-TVV v3.1 + 92 BM + 85 CT GĐ1; was 564 ước) | ✅ DN+CG-TVV+BM+CT GĐ1 (DN+CG-TVV done 2026-05-09) | ⚠️ 1 (DN done 2026-05-09 — 9 BUG: 1 Critical/3 Major/3 Medium/2 Low) + 🟢 1 BM ready + 🚫 2 (CG-TVV chờ bug TVCS-003/004, CT GĐ1 chờ bug) |
| W3 | 3 | HD + VV + TVCS + KH | 888 (HD 197 v3.1 actual + VV 294 + TVCS 134 + KH 263 v3.5; HD: 118 ước → 197 sau A1-A7 + Codex 2026-05-10; TVCS 125 → 130 → 134 sau codex review R1+R2 2026-05-09) | ✅ HD+VV+TVCS+KH (HD done 2026-05-10 + Codex review applied; KH done 2026-05-08; TVCS codex R1+R2 done 2026-05-09) | 🟢 1 HD ready + ⚠️ 1 TVCS (49/134 PASS 2026-05-11 — 6 BUG NEW: 2 Critical Export TVCS 404 + UC152 TLPL missing; 56 BLOCKED) + 🚫 2 (VV ⏳ chờ bug + W2.1/W2.2 B done; KH 🚫 chờ B7 close + DN/HV seed) |
| W4 | 4 | HĐTV + CT + TVN + ĐG | 609 (HĐTV 85 + CT 137 v3.1 actual + TVN 100 actual sau Codex 2026-05-10 + ĐG 167 actual sau A1-A7 + Codex 2026-05-10; ĐG: ~80 ước → 167 sau A1-A7 + A4 +49 + A6 +11 + Codex apply +23) | ✅ HĐTV+CT+TVN+ĐG (ĐG done 2026-05-10 + Codex apply) | ⚠️ 1 HĐTV done 2026-05-11 (25/85 PASS, 7 BUG, 52 BLOCKED) + 🚫 3 (CT chờ E3 + W3.2 VV, TVN chờ E4 + Kho QA, ĐG chờ W3.2 VV HOAN_THANH + DM Tiêu chí seed) |
| W5 | 5 | CT GĐ2 + BC + DB + API | 441 (CT GĐ2 74 actual sau A1-A7 + Codex 2026-05-10; BC 129 actual sau A1-A7 + Codex 2026-05-10; DB 178 actual sau A1-A7 + Codex 2026-05-10; API 60 estimate; DB: ~40 ước → 178 sau A1-A7 + A4 +30 + A6 +7 + Codex apply +10) | ✅ CT GĐ2 + BC + DB + 📝 1 | 🚫 4 |
| **Tổng** | — | **20 testable unit** (16 FR; FR-10 ×4 sub + FR-15 ×2 GĐ) | **~3012** (+178 DB sau A1-A7 + Codex 2026-05-10) | 18 ✅ + 2 📝 | 8 🟢/⚠️ (W1.1, W1.2, W1.3, W2.1, W2.3, W2.4, W3.2, W3.3, W3.4 — re-test scope=100% file affected khi C4) + 12 🚫 |

---

## D0 — Triage + audit (0.5 ngày → 1 ngày sau khi thêm D0.5)

- 🟢 **D0.1** Update `00-tong-so-luong-testcase.md` — DN 224, total 717
- 🟢 **D0.2** Audit 5 file REVIEW edge-case-hunter — verify TC merge file chính
- 🟢 **D0.3** Map dependency 16 module × seed/workflow → `_dep-matrix.md`
- ⏳ **D0.4** User duyệt thứ tự + strategy
- 🟢 **D0.5** **A7 Filter pass** cho 7 module ✅ đã có TC (viết theo workflow A1-A6 cũ, có thể chứa TC chỉ-DB/API thuần). Áp dụng [§3.1 A7 Filter rule](plan.md#31-phase-a--skill-bmad).
  - **Scope:** 46 TC file × 7 module ✅ = W1.1 (1) + W1.2 (4) + W1.3 (10) + W1.4 (4) + W2.1 (6) + W2.2 (14) + W3.1 (7)
  - **Action:** Manual scan từng TC → loại TC require DB query / API curl thuần / cron job no-UI; sửa TC verify-DB → verify-network qua MCP `list_network_requests`
  - **Output:** Update TC file + log số TC loại/sửa vào `output/test-cases/_a7-filter-log.md` (theo module)
  - **Acceptance:** 0 TC còn keyword "verify DB row", "check index", "curl POST", "cron job", "background worker" mà không có UI bridge

---

## C — SRS Re-sync log (event-driven, dự kiến ~20-32 sync events trong plan)

**Source folder:** `input/srs-update-05-05-2026/`
**Naming convention:** `srs-fr-{XX}-{module-slug}-v{N}.md` (vd `srs-fr-07-doanh-nghiep-v3.1.md`)
**Tracker file:** `output/test-cases/_srs-sync-log.md`
**Workflow:** [`plan.md` §4 Phase C](plan.md) — 5 step C1 Detect → C2 Impact → C3 Re-write → C4 Re-test → C5 Log
**Status icons:** 📭 chờ trigger · 🔵 đang sync · ⏸️ paused (user pause giữa chừng — dùng `Resume Phase C FR-XX vN` để tiếp) · ✅ done · ⚠️ partial (bug Open mới chặn) · 🚫 block (cascade upstream / user defer)
**Priority rule:** User tự kiểm soát thứ tự khi nhiều file landing cùng lúc — KHÔNG cap cứng. Đề xuất ưu tiên Lớp dependency 1→5.
**Default mode:** `auto-c3-checkpoint` — auto C1-C3, pause sau C3 chờ confirm C4, C4.1 pause khi bug transition ambiguous, C4.2 scope = 100% TC trong file affected (Option 1 full regression). Override: `auto` / `verbose` / `dry-run`.

### Sync events log (thêm row mỗi lần SRS update mới landing)

| # | Date | SRS file | FR | Version | TC affected | Bug delta | Re-test | Last step | Phase C status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-05-06 | `srs-fr-07-doanh-nghiep-v3.1.md` | FR-07 | v3.1 | 5 file: 00 overview, 01 CRUD (Section C deprecate), 03 import (full deprecate), 06 permission, 99 review · TC delta: 207→~144 (-63) | _(pending C4.1 — predict: BUG-FR07-001 VALID→INVALID)_ | _(pending C4.2 — scope 100% TC trong 5 file affected, Option 1)_ | **C3** | ⏸️ paused — user defer C4/C5 |
| 2 | 2026-05-07 | `srs-fr-10-quan-tri-v3.1.md` | FR-10 | v3.1 | 10 file: 4 overview (4 sub) + 4 TC affected (SLA badge nhãn, co-quan-don-vi 2 tầng, nhat-ky-he-thong formalize FR-VIII-28, quan-ly-tai-khoan SM CHO_PHAN_QUYEN) + 2 TC NEW (`05-TC-ngay-le.md` FR-VIII-29, `05-TC-quen-mk-kich-hoat.md` FR-VIII-26) · TC delta: ~440 → ~480 (+~40) | _(pending C4.1 — bug-report 4 sub-module hiện 0 Open, forecast 0 transition)_ | _(pending C4.2 — scope 100% TC trong 10 file affected, Option 1)_ | **C3** | ⏸️ paused — chờ user confirm proceed C4 |

### Module Phase C status (default 📭 · ⏸️ khi user pause giữa chừng · ✅ khi C5 done)

| FR | Module | Phase A | Phase C | Note |
|---|---|---|---|---|
| FR-01 | Dashboard | ✅ | 📭 | Phase A done 2026-05-10 (178 TC sau A1-A7 + Codex review applied: 161 A3+A4 base + 7 A6 fill + 10 Codex apply — 8 UC + 5 audit). 4 SPEC-CLARIFY pending BA (DASH-01/03/04/05; DASH-02 RESOLVED by Codex P0-1/P0-2 → relative %). Coverage BR/AC/Permission/Error/State enum/Outputs = 100%. Codex Gate PASS (2P0 + 3P1 → all 5 fixed, +10 TC). Quality 9.6/10. Sẵn sàng cascade W5 — Phase B chờ ≥3 record/state cuối từ mỗi module nguồn (HD + VV + KH + TVV + KQ_DG + KQ_DT). |
| FR-02 | Hỏi đáp | ✅ | 📭 | Phase A done 2026-05-10 (197 TC sau A1-A7 full cycle + Codex review applied — 7 UC files + 5 audit). 11 SPEC-CLARIFY pending BA. Coverage BR/SM/Permission/Error 100%, AC 97.4%. Quality 9.75/10. Sẵn sàng Phase B |
| FR-03 | Đào tạo | ✅ | 📭 | Phase A done 2026-05-08 (263 TC sau A4 inline +15 + A6 inline +8 - A7 -1 LOẠI — 13 UC files + 4 audit). 38 SPEC-CLARIFY pending BA. Coverage BR 100%, SM 100%, AC 99.1%, Error 97.9%. Sẵn sàng sync khi có SRS update |
| FR-04 | CG/TVV | ✅ | 📭 | Phase A done 2026-05-09 (271 TC sau A4 +42 edge + A6 +11 fill + A7 4 SỬA + Codex 1 split — 14 UC files + 5 audit). 28 SPEC-CLARIFY pending BA. Coverage BR/AC/ERR/SM/Permission = 100% explicit. Quality 9.55/10. Sẵn sàng sync khi có SRS update |
| FR-05 | Vụ việc | ✅ | 📭 | Phase A done 2026-05-06 (294 TC sau A4 inline +4 + A6 inline +1 — 14 UC files). Sẵn sàng sync khi có SRS update |
| FR-06 | Chi trả | ✅ | 📭 | Phase A done 2026-05-10 (137 TC sau A1-A7 full cycle + A4 +39 edge + A6 +5 fill GAP-A5 + Codex review (3 P0 + 4 P1 + 3 P2 → all 10 fixed) — 10 UC files + 5 audit). 13 SPEC-CLARIFY pending BA. Coverage BR/Error code/Permission = 100%, AC 97.4%, SM 92.9% (1 SPEC-CLARIFY-CT-01 nút Từ chối TT). Quality 9.8/10. Sẵn sàng sync khi có SRS update. Phase B chờ E3 + W3.2 VV HOAN_THANH. |
| FR-07 | Doanh nghiệp | ✅ | 📭 | Phase A done 2026-05-09 redo (183 TC sau A4 +37 edge + A6 +7 fill + A7 5 SỬA UI bridge + Codex +5 fix — 6 UC files + 5 audit). 46 SPEC-CLARIFY pending BA. Coverage BR/AC/SM/Permission/Error 100%. Quality 9.8/10. **Phase C row #1 (v3.1 2026-05-06) deprecated** — các TC C3 cũ đã xóa, version mới 2026-05-09 đã apply trực tiếp Phase A v3.1. |
| FR-08 | Đánh giá | ✅ | 📭 | Phase A done 2026-05-10 (167 TC sau A1-A7 + Codex review apply: 84 base + 49 A4 edge + 11 A6 fill + 23 Codex — 7 UC files + 5 audit). 6 SPEC-CLARIFY pending BA, 2 RESOLVED. Coverage BR/AC/SM/Error 100%. Codex Gate PASS (30/30). Quality 9.65/10. Sẵn sàng sync khi có SRS update. Phase B chờ W3.2 VV HOAN_THANH + DM Tiêu chí UC109 seed. |
| FR-09 | Biểu mẫu | ✅ | 📭 | Phase A done 2026-05-06 (84 TC sau A4 inline merge + A6+A7). Sẵn sàng sync |
| FR-10 | QTHT (4 sub) | ✅ | ⏸️ | **v3.1 (2026-05-07)** — C1-C3 done (FR-VIII-26 + FR-VIII-28 formalize + FR-VIII-29 mới + BR-AUTH-02 2-tầng + SM-TAIKHOAN CHO_PHAN_QUYEN); C4/C5 ⏸️ paused. Resume: `Resume Phase C FR-10 v3.1 (continue from C4.1)`. **2026-05-10 mở rộng**: W1.4 TKPQ thêm UC120 / FR-VIII-22 self-registration DN — Phase A A1-A7 done, file mới `12-TC-self-registration-dn.md` 68 TC. |
| FR-11 | Báo cáo TK | ✅ | 📭 | Phase A done 2026-05-10 (129 TC sau A1-A7 + Codex review apply: 110 base + 15 A4 edge + 3 A6 fill + 1 Codex F-03 PERM-000 unauth — 5 UC files + 5 audit). Strategy "1 đại diện + smoke" 23 BC trên 1 SCR-IX-01. 10 SPEC-CLARIFY pending BA. Coverage BR formal/AC/Error/Permission 100%. Quality 9.55/10. Codex Gate PASS (1P0+4P1+4P2 ALL applied). Sẵn sàng sync khi có SRS update. |
| FR-12 | TV Chuyên sâu | ✅ | 📭 | Phase A done 2026-05-07 (125 TC sau A4 inline +26 + A6 inline +8 — 6 UC files + 4 audit). 17 SPEC-CLARIFY pending BA. Coverage BR/AC/SM = 100%, Error 97.1%, Permission ~95% nghiệp vụ. Sẵn sàng sync khi có SRS update |
| FR-13 | TV Nhanh | ✅ | 📭 | Phase A done 2026-05-10 (100 TC sau A1-A7 + Codex review apply: 76 base + 18 A4 edge + 4 A6 fill + 2 Codex P1 — 6 UC files + 5 audit). 11 SPEC-CLARIFY pending BA. Coverage BR/Permission/Error/SM/State/Entity 100%, AC 96.2%. Codex Gate PASS. Quality 9.4/10. Sẵn sàng sync khi có SRS update |
| FR-14 | Hợp đồng TV | ✅ | 📭 | Phase A done 2026-05-10 (85 TC sau A1-A7 + Codex review apply: 54 base + 21 A4 edge inline + 5 A6 fill status field/entity + 5 Codex P1-1..P1-3 — 6 UC + 4 audit). 2 P0 RESOLVED (DANG_HOAT_DONG → HOAT_DONG, SM transition → status field per SRS §5). Coverage BR/AC/ERR/trang_thai/Permission/Entity Inputs = 100%. Quality 93% PASS. 16 SPEC-CLARIFY pending BA (3 RESOLVED). Sẵn sàng sync khi có SRS update. |
| FR-15 | CT HTPLDN (GĐ1+GĐ2) | ✅ GĐ1 ✅ / GĐ2 ✅ | 📭 | GĐ1 Phase A done 2026-05-06 (100 TC sau A4 +9 + A6 +2 + Codex +15 — 8 UC + 4 audit). GĐ2 Phase A done 2026-05-10 (74 TC sau A1-A7 + Codex review applied: 51 A3 + 19 A4 + 3 A6 + 1 Codex — 7 UC + 5 audit). GĐ2: 9 SPEC-CLARIFY pending BA. Coverage BR/AC/SM/ERR 100%, Permission Matrix 33/64 explicit + 31 suy luận. Quality 9.3/10. Sẵn sàng cascade W3.2/W4.2 unblock. |
| FR-16 | API Kết nối | 📝 | 📭 | — |

---

## Wave 1 — LỚP 1 QTHT nền tảng (3 ngày) — ✅ DONE Phase A (W1.1 + W1.2 + W1.3 + W1.4 ✅ redone 2026-05-08)

### W1.1 QTHT Nhật ký HT (53 TC active v3.1, 0.5 ngày) — ✅ Phase A done 2026-05-08 + codex review applied

- ✅ **A** — TC đã có (3 UC files 01-03 = 54 TC, 4 audit files 08-11). Xong 2026-05-08 — BMAD A1-A7 full cycle: A1 đọc SRS srs-fr-10:1314-1372 + 1803-1834 + sibling Biểu mẫu/Đào tạo + A2 overview (00) + A3 3 UC files (51 TC base) + A4 inline merge (15 edge: 90 ngày boundary 89/90/91, 10K Excel boundary 9999/10K/10001/50001, timezone UTC+7, soft-delete user, immutable double-verify, perf 50K/30s, reset filter, security download URL) + A5 trace matrix (BR/AC/Error/Permission = 100% / Output column 75% explicit) + A6 fill 3 TC inline (TC-NK-112 Mã bản ghi, TC-NK-113 7 badge màu, TC-NK-124 empty AUDIT_LOG fresh) + A7 0 LOẠI (TC-NK-142/PERM-009 dùng `evaluate_script` UI context — A7 OK). 6 SPEC-CLARIFY pending BA. Quality 9.42/10.
  - **Output:** `output/test-cases/QTHT/Nhat-ky-he-thong/` (3 UC + 00 + 08-11 audit)
- 🟢 **B** — 3 TC file × 4 block (B-Seed → B-Run → B-Verify → B-Report). Áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-tra-cuu-loc-nhat-ky.md` | 33 | 🟢 ready | Filter 6 trường + sort + pagination + JSON diff. 90-ngày boundary on-bound. TK: qtht_01 |
  | B2 | `02-TC-xuat-excel-nhat-ky.md` | 12 | 🟢 ready | Export Excel 10K boundary (BR-DATA-06). SPEC-CLARIFY-NHATKY-01 (10K vs 50K) sẽ rõ ở Phase B |
  | B3 | `03-TC-permission-matrix.md` | 9 | 🟢 ready | Chỉ QTHT (BR-AUTH-01) + BR-DATA-05 immutable. TK `_03` permission test |

  **Output:** `output/execution-test/QTHT/Nhat-ky-he-thong/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W1.2 QTHT Cấu hình HT (125 TC active v3.1, 0.5 ngày) — ✅ Phase A done 2026-05-08 + codex review applied

- ✅ **A** — TC đã có (6 UC files 01-06 = 124 TC, 4 audit files 08-11). Xong 2026-05-08 — BMAD A1-A7 full cycle: A1 đọc srs-fr-10:440-516 (FR-VIII-10 SLA) + 1376-1434 (FR-VIII-29 Ngày lễ) + 1609-1697 (SCR-VIII-06 4 tab) + srs-fr-02:885-967 (FR-II-NEW-02 + FR-II-NEW-01 ĐÃ BỎ Q11) + sibling W1.1 + A2 overview + A3 6 UC files (~85 TC base) + A4 inline merge 32 TC (snapshot pattern Tab 1+4, Mô hình B Hybrid 2 tầng cross-cấp/cross-don_vi, sanitize XSS multi-field, integration BR-CALC-03 ↔ NGAY_LE, deprecation FR-II-NEW-01) + A5 trace matrix (BR 97% / AC 92.3% / Error 100% / Permission 100% / SM 100%) + A6 fill 7 TC inline (Add new SLA AC2, ERR-SLA-03 duplicate, toggle gui_thong_bao_app, tu_khoa, mo_ta x2, empty filter no-match) + A7 0 LOẠI (cross-cấp BE check qua `evaluate_script` UI bridge). 8 SPEC-CLARIFY pending BA. Quality 9.28/10.
  - **Output:** `output/test-cases/QTHT/Cau-hinh-he-thong/` (6 UC + 00 + 08-11 audit)
- 🟢 **B** — 6 TC file × 4 block (B-Seed → B-Run → B-Verify → B-Report). Áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-tab-sla.md` | 27 | 🟢 ready | Tab 1 SLA inline + boundary CB1<CB2<100 + snapshot HS đang xử lý. TK: qtht_01 |
  | B2 | `02-TC-tab-phan-cong-deprecated.md` | 3 | 🟢 ready | Verify Tab 2 ẨN/banner sau BA Q11 (FR-II-NEW-01 bỏ) |
  | B3 | `03-TC-tab-mau-phan-hoi.md` | 41 | 🟢 ready | Mô hình B Hybrid — 4 role × CRUD scope. ERR-MPH-01..06 + cross-cấp BE check. Seed 9 mẫu TW/BN/DP |
  | B4 | `04-TC-tab-quy-trinh-ho-tro.md` | 12 | 🟢 ready | Snapshot quy trình VV. SPEC-CLARIFY-CAUHINH-08 spec field thiếu |
  | B5 | `05-TC-ngay-le.md` | 22 | 🟢 ready | FR-VIII-29 v3.1 — CRUD + Import Excel + integration BR-CALC-03 e2e |
  | B6 | `06-TC-permission-matrix.md` | 19 | 🟢 ready | Tab gating + cross-don_vi + IDOR. TK `_03` permission |

  **Output:** `output/execution-test/QTHT/Cau-hinh-he-thong/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W1.3 QTHT DM dùng chung (255 TC active v3.1, 1.5 ngày) — ✅ Phase A done 2026-05-08 (R1+R2+R3+R4 Codex review)

- ✅ **A** — TC đã có (10 UC files 01-10 = 255 TC active sau R3 LOẠI 3, 4 audit files 08/09/10/11). Xong 2026-05-08 — BMAD A1-A7 full cycle: A1 đọc SRS srs-fr-10:56-880 + 1444-1496 + entity DON_VI/DANH_MUC §3.4 + sibling Nhật ký HT/Cấu hình HT + A2 overview (00) + A3 10 UC files (228 TC base — 47 TPL representative LV-PL + 55 smoke 11 DM + 32 cây 2-tầng UC103 + 18 TC HQ + 15 TC CP + 10 CT date + 10 TT mau + 10 LDN tieu_chi + 15 HSDN JSON + 16 permission) + A4 edge inline merge (+18 TC: concurrency/unicode/whitespace/soft-delete/XSS/regex/pagination boundary/sort secondary, tree change cap with children/perf/session active, TC HQ toggle reactive/UPDATE validate, TC CP overflow/decimal, CT snapshot, TT cascade msg, HS dup item) + A5 trace matrix (BR 100% sau fill / AC 100% / Error 14/14 / Permission 5/5) + A6 fill 3 GAP inline (BR-AUTH-08 ngoại lệ DM hệ thống NULL, BR-DATA-02+03 common fields) + A7 0 LOẠI (1 SỬA TC-PERM-008 chuyển direct curl → DevTools fetch UI bridge — sau bị Codex R3 challenge → LOẠI hẳn). **Codex full review (R1+R2+R3+R4):** R1 fix count/scope wording, R2 +9 fill (UC103 enum/UC109 required/UC110 required), R3 −3 LOẠI + 7 REPHRASE assumption→UI bridge, R4 −9 SPEC-CLARIFY cleared theo SRS. **20 SPEC-CLARIFY active** pending BA. Quality 9.1/10 (sau cleanup). **FR-VIII-06 Tổ chức tư vấn KHÔNG nằm trong scope (CR-02 chuyển Nhóm IV).**
  - **Output:** `output/test-cases/QTHT/DM-dung-chung/` (10 UC + 00 + 08/09/10/11 audit)
- ⚠️ **B** — 10 TC file × 4 block (B-Seed → B-Run → B-Verify → B-Report) **DONE 2026-05-09**. Pass rate ~30%, 11 bug VALID + 8 OBS GAP. **Block ship critical** chờ dev fix UC-specific modals + LV-PL whitelist enum.

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-tpl-dm-CRUD-representative-LV-PL.md` | 56 + 1 UI = 57 | ⚠️ 21 PASS / 4 PARTIAL / 4 FAIL / 22 BLOCKED / 6 DEFERRED | BUG-DM-001 Critical (whitelist enum LV-PL), BUG-DM-002 High (mã disabled Edit), BUG-DM-003 High (DELETE 500 LV-PL), 3 OBS (Export Excel, Danh mục cha, radio vs toggle) |
  | B2 | `02-TC-smoke-11-dm-chuan.md` | 55 | ⚠️ 28 PASS / 4 PARTIAL / 11 FAIL / 6 BLOCKED / 6 DEFERRED | 5 BUG mới (DM-004..008): UC101/102/105/106/107/110 modal MISSING UC-specific fields. BUG-DM-001/003 SCOPE DOWNGRADE → chỉ LV-PL |
  | B3 | `03-TC-co-quan-don-vi-tree-2tier.md` | 38 | ⚠️ 1 PASS / 4 FAIL / 33 BLOCKED | BUG-DM-009 Critical UC103 implementation gap (no tree, no cap enum, no don_vi endpoint, empty seed) |
  | B4 | `04-TC-tieu-chi-dg-hieu-qua.md` | 24 | ⚠️ 6 PASS / 3 PARTIAL / 1 FAIL / 8 BLOCKED / 6 DEFERRED | UC109 modal có specialized fields ✅. OBS-DM-010 GAP BR-CALC-04 enforce mode + OBS-DM-011 GAP table column |
  | B5 | `05-TC-tieu-chi-dg-chi-phi.md` | 19 | ⚠️ 1 PASS / 4 FAIL / 14 BLOCKED | BUG-DM-008 Critical UC110 modal nhầm UC109 layout (toàn bộ business NĐ18/2026 sai) |
  | B6 | `06-TC-chuong-trinh-ho-tro-date.md` | 11 | ⚠️ 1 PASS / 3 FAIL / 7 BLOCKED | BUG-DM-006 Critical UC101 modal MISSING date+don_vi |
  | B7 | `07-TC-tinh-trang-vv-mau.md` | 11 | ⚠️ 1 PASS / 3 FAIL / 7 BLOCKED | BUG-DM-007 High UC102 MISSING mau HEX + BUG-DM-011 Low thu_tu enforcement |
  | B8 | `08-TC-loai-dn-tieu-chi.md` | 10 | ⚠️ 1 PASS / 3 FAIL / 6 BLOCKED | BUG-DM-004 Critical (cross-ref B2) + OBS-DM-012 GAP semantic mismatch legal vs size |
  | B9 | `09-TC-ho-so-thanh-phan.md` | 16 | ⚠️ 2 PASS / 4 FAIL / 10 BLOCKED | BUG-DM-005 High UC106+107 JSON repeater missing |
  | B10 | `10-TC-permission-matrix.md` | 15 active | ⚠️ 4 PASS / 4 BLOCKED / 7 DEFERRED | qtht_01 happy path verify ngầm B1-B9. cb_nv/cb_pd/Tier 2 defer login switch sau dev fix |

  **Output:** `output/execution-test/QTHT/DM-dung-chung/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

  **Bug summary:** 11 BUG VALID (3 Critical LV-PL/UC103/UC110 + 6 High UC101/102/105/106/107/Edit-disable + 2 Low) + 8 OBS GAP (Export Excel, Danh mục cha, radio toggle, search 201, BR-CALC-04 enforce, Table column TS, Semantic LDN, JSON repeater spec)
  **Block ship:** BUG-DM-001 (LV-PL whitelist enum) + BUG-DM-006/007/008/009 + UC101/102/103/110 modal incomplete chặn re-test sâu

### W1.4 QTHT TKPQ (268 TC v3.1 = 252 functional + 16 security, 2 ngày) — ✅ Phase A done + Codex R2 2026-05-08 + UC120 mở rộng 2026-05-10

- ✅ **A** — TC đã có (6 UC functional `01-06` = 184 TC + 1 security suite `07` = 16 TC + 4 audit `08-11` + **1 UC functional `12` UC120 = 68 TC NEW 2026-05-10**). Xong 2026-05-08 cho UC112-117 — BMAD A1-A7 full cycle + Codex R2 review (xem chi tiết v1 cũ). **Append 2026-05-10**: BMAD A1-A7 full cycle cho UC120 / FR-VIII-22 self-registration DN: A1 đọc srs-fr-10:1005-1089 + 1722-1768 + 1772-1786 + SM-TAIKHOAN T1/T4 paths + sibling FR-VIII-15/26 + A2 update overview (mở rộng scope FR-VIII-22 + permission matrix public no-auth + SM T1/T4 cover) + A3 51 TC base (6 Happy + 23 Validation Nhóm 1 + 18 Validation Nhóm 2 + 6 ERR-REG + 10 Security/Audit/Integration) + A4 inline merge (+13 edge: Unicode CJK + whitespace trim + leading-zero MST + phone intl + file dup name + MIME spoof + re-register soft-delete MST/email + same DN name + network mid-submit + browser autofill + email IDN + cancel cleanup) + A5 trace matrix (BR 100% / AC 100% 4/4 / SM T1+T4 100% / ERR-REG 100% 6/6 / 22 fields full BVA / Permission public no-auth) + A6 fill 4 TC inline (form layout + mail HTML + SMTP MailHog API + file storage UUID) + A7 0 LOẠI / 0 SỬA / 68 GIỮ. Renumber UC120 SPEC-CLARIFY → TKPQ-30..43 (14 entries) tránh đụng existing TKPQ-12..29. Quality UC120 9.27/10. **BR coverage 100% (15/15)** sau UC120 add BR-DATA-02 unique. AC 20/20. ERR 25/25. Quality cumulative 9.45/10.
  - **Output:** `output/test-cases/QTHT/Tai-khoan-phan-quyen/` (7 UC functional + 1 security IDOR + 00 + 08-11 audit) — file 12-TC NEW
- 🟢 **B** — 7 functional TC file × 4 block (B-Seed → B-Run → B-Verify → B-Report). File 07 security chạy ngoài Phase B functional. Áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-vai-tro.md` | 27 | 🟢 ready | UC112 CRUD + ERR-VT-01/02 + soft delete (UI+audit verify, không SELECT raw). TK: qtht_01. Codex R2 -1 IDOR -1 false flag. |
  | B2 | `02-TC-tai-khoan.md` | 65 | 🟢 ready | UC113 CRUD + SM 12 transitions + 6 ERR-TK + tab counter + Codex R2 NEW BR-AUTH-06/09 + BR-DATA-03. TC-TK-139/142/197 wait time deferral. TC-TK-198 cần Tier 2. |
  | B3 | `03-TC-phan-quyen-du-lieu.md` | 22 | 🟢 ready | UC114 cây 2-tầng + BR-AUTH-02/03/04 + ERR-PQ-01..03 + role-cap reframe (Codex R2). TC-127 force reject empty. |
  | B4 | `04-TC-phan-quyen-chuc-nang.md` | 19 | 🟢 ready | UC115 matrix 6×N + cha-con cascade + cross-module verify. TC-122 force reject empty. |
  | B5 | `05-TC-quen-mk-kich-hoat.md` | 30 | 🟢 ready | FR-VIII-26 v3.1 + 6 ERR-PWD + trigger SM-TVV/SM-NHT (cần W2.2) + MailHog UI + Codex R2 NEW BR-EC-13 200 char. |
  | B6 | `06-TC-permission-matrix.md` | 21 | 🟢 ready | Cross-FR role-based UI access + Tier 2 chặn + cross-tenant + audit. IDOR moved 07. TK `_03`. |
  | **B7** | **`12-TC-self-registration-dn.md`** | **68** | **🟢 ready (NEW 2026-05-10)** | **UC120 FR-VIII-22 self-registration DN public form 22 fields + ERR-REG-01..06 + chain mail kích hoạt → SM T1+T4 path → HOAT_DONG. Public no-auth. MailHog UI + AUDIT_LOG SCR-VIII-10 verify. Defer items: TC-REG-104 token vĩnh viễn (manual time check), TC-REG-198/199/209 race + network throttle, TC-REG-212 storage cleanup. 14 SPEC-CLARIFY (TKPQ-30..43) pending BA.** |
  | (sep) | `07-TC-security-IDOR.md` | 16 | 🔧 separate | Security/dev team chạy ngoài Phase B functional, qua tool API. |

  **Output:** `output/execution-test/QTHT/tai-khoan-phan-quyen/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

**Checkpoint W1:** 4 functional report + 0 Critical Open → duyệt W2

---

## Wave 2 — LỚP 2 Master Data (4 ngày)

### W2.1 Doanh nghiệp (183 TC v3.1, was 224 v3.0 + estimate 144, 1 ngày) — ✅ Phase A done 2026-05-09 + Codex review applied

- ✅ **A** — TC đã có (6 UC files 01-06 = 183 TC, 5 audit files 00 + 08-12 codex log). Xong 2026-05-09 — BMAD A1-A7 full cycle + Codex review: A1 đọc SRS srs-fr-07-doanh-nghiep-v3.1.md (613 dòng — 2 FR active + Import Excel BỎ + Thêm mới CMS BỎ) + srs-v3.5 §3.4.3.3/3a entity + §3.4.2 Permission + Phụ lục B BR + sibling W2.2 CG-TVV/W3.2 VV + CHANGELOG-v3-to-v3.1 (10 thay đổi cherry-pick + 1 OUT D.2.1) + A2 overview (00 + permission matrix DN/HSPL/LINH_VUC × 11 role) + A3 6 UC files (134 TC base — 2 FR + Tab 2 HSPL FR-X.1-04 + Tab 3 KPI cross-FR-05 + Tab 4 cross-FR-06 + Permission cross BR-AUTH/EMAIL/USERNAME) + A4 inline merge (+37 edge: 4 concurrency + 4 XSS sanitize + 2 SQL injection + 2 Unicode + 3 file edge + 3 soft delete invariants + 3 counter sync + 3 date logical + 1 timezone + 1 sort + 2 performance + 3 session/auth + others) + A5 trace matrix (BR 100% / AC 100% / SM 60% / Permission 100% / Error 92.3%) + A6 fill 7 TC inline (SM-HSPL HET_HAN/THU_HOI restore + ERR-HSPL-02 + BR-DATA-03 common fields + DN role redirect + la_nu_lam_chu badge + strengthen file metadata) + A7 5 SỬA UI bridge (DevTools fetch → MCP `list_network_requests` UI-triggered, security tests vẫn giữ qua MCP `evaluate_script`) + 0 LOẠI + Codex review (3 P0: MST boundary 3 TC negative + LV junction remove/cascade 2 TC + TC-DN-PERM-603 NGUYÊN VĂN drift fix). 46 SPEC-CLARIFY pending BA. Quality 9.8/10. **Lưu ý**: SRS file v3.1 vẫn còn SCR-V.III-03 Wizard Import section (line 387-416) dù FR-V.III-NEW-01 BỎ — TC verify UI cũng phải BỎ (TC-DN-UI-01 cover).
  - **Output:** `output/test-cases/quan-ly-doanh-nghiep/` (6 UC + 00 + 08-12 audit)
- ⚠️ **B** — 6 TC file × 4 block done 2026-05-09. **31 TC executed / 102 BLOCKED / 19 DEFERRED / 31 / 183 TC = 17% conclusive**. **9 BUG VALID** (1 Critical + 3 Major + 3 Medium + 2 Low) sau 2-source verify (NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + grep SRS local) + 7 OBS GAP + 6 SPEC-CLARIFY mới (DN-PB-01..08).

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-FR-V.III-01-quan-ly-dn-CRUD.md` | 41 | ⚠️ 9 PASS / 4 PARTIAL / 6 FAIL / 17 BLOCKED / 5 DEFERRED | **BUG-DN-FUNC-005 Critical** (phone reject 11-digit landline) + **BUG-DN-FUNC-006 Major** (URL view-only mode missing) + BUG-DN-FUNC-001 (LV textbox not multi-select) + BUG-DN-FUNC-003 (file upload missing) + BUG-DN-FUNC-007 (doanh thu float32 precision) + BUG-DN-FUNC-002/004 Low |
  | B2 | `02-TC-FR-V.III-02-tim-kiem-dn.md` | 32 | ⚠️ 5 PASS / 2 PARTIAL / 1 FAIL / 17 BLOCKED / 7 DEFERRED | Search PASS (POST /export endpoint), filter LV BLOCK by BUG-DN-FUNC-001, Excel boundary 10K BLOCKED (env data) |
  | B3 | `03-TC-tab-ho-so-phap-ly-dn.md` | 40 | ⚠️ 2 PASS / 0 FAIL / 36 BLOCKED / 2 DEFERRED | **BUG-DN-FUNC-008 Major** form HSPL thiếu `linh_vuc_id` + `file_dinh_kem` → block 36/40 TC |
  | B4 | `04-TC-tab-lich-su-ho-tro.md` | 19 | ⚠️ 4 PASS / 1 PARTIAL / 1 FAIL / 9 BLOCKED / 4 DEFERRED | KPI 3 cards verify với DN-BCT-001 (3 VV). **BUG-DN-FUNC-009 Medium** Mã VV không clickable navigate FR-05 |
  | B5 | `05-TC-tab-ho-so-chi-tra.md` | 18 | ⚠️ 3 PASS / 1 PARTIAL / 12 BLOCKED / 2 DEFERRED | Empty state OK (env 0 HSCT cho DN-BCT-001). Bonus 2 KPI Tab 4 ngoài SRS — SPEC-CLARIFY-DN-PB-07. Currency drift "đ" vs "₫" |
  | B6 | `06-TC-permission-matrix.md` | 33 | ⚠️ 8 PASS / 1 PARTIAL / 18 BLOCKED / 6 DEFERRED → updated 8/11 role tested sau supplementary | BR-AUTH-08 cấp 1 TW: cb_nv_tw_01 ✅ 27 DN; **cb_pd_tw_01 🐛 0 DN (BUG-010 NEW)** vi phạm SRS:297. BR-AUTH-08 cấp 2 BN: cb_nv_bn_01 (BKH) ✅ 1 DN. BR-AUTH-08 cấp 2 DP: cb_nv_dp_01 (AG) ✅ 11 DN. dn_01 + tvv_01 401 ✅ (đúng SRS no-CMS). IDOR URL DN cross-tenant → 404. **BUG-001 RE-CLASSIFIED**: conditional render — cb_pd_tw_01 thấy multi-select LV nhưng cb_nv_tw_01 thấy textbox |

  **Block ship critical**: BUG-DN-FUNC-005 (phone validation reject landline) — KHÔNG thể edit DN có 11-digit phone (mọi DN seed default đều có). **Block compliance**: BUG-DN-FUNC-010 (cb_pd_tw_01 0 DN) vi phạm BR-AUTH-08 TW exception cho CB_PD.
  **Output:** `output/execution-test/quan-ly-doanh-nghiep/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W2.2 CG/TVV (FR-04, 271 TC v3.1, 1 ngày) — ✅ Phase A done 2026-05-09 + Codex review applied

- ✅ **A** — TC đã có (14 UC files 01-14 = 271 TC, 5 audit files 00 + 08/09/10/11 + 12 codex log). Xong 2026-05-09 — BMAD A1-A7 full cycle + Codex review: A1 đọc SRS srs-fr-04-chuyen-gia-tvv- v3.1.md (2547 dòng) + CHANGELOG (18 thay đổi cherry-pick + 1 OUT D.2.1) + sibling W1.4 TKPQ + W3.2 VV + A2 overview (00 + permission matrix 10 vai trò × 6 action) + A3 14 UC files (217 TC base — covering 19 FR + 9 SCR + 3 SM + 7 entity + 13 BR) + A4 inline merge (+42 edge: 17 EC categories — concurrency/unicode/whitespace/SQL/timezone/file 0-byte/API timeout/round-half-up tie/IDOR/CHO_KICH_HOAT special/NHT cross-entity) + A5 trace matrix (BR/AC/ERR/SM/Permission 100% sau A6) + A6 fill 11 TC inline (BR-DATA-03/05 + BR-FLOW-03 + ERR-LS-01/CT-02 + WRN-TCTV-04 + ERR-TT-TC-03 + 4 SM transitions + AUDIT_LOG) + A7 4 SỬA reroute UI bridge (queue → list reload + FR-VIII-28 audit UI), 0 LOẠI + Codex review (2 P0 NGUYÊN VĂN ERR-TD-03/PD-03 + 4 P1 logic + 1 P2 BR-PUBLIC-01 conflict — 1 split TC-TN-001a/b). 28 SPEC-CLARIFY pending BA. Quality 9.55/10. Coverage BR/AC/ERR/SM/Permission = 100% explicit. **CHANGELOG v3.1 18/18 cherry-pick COVERED**, 1 OUT D.2.1 PARTIAL (conflict SRS body — SPEC-CLARIFY-CGTVV-27).
  - **Output:** `output/test-cases/CG-TVV/` (14 UC + 00 + 08/09/10/11/12 audit)
- ✅ **B** — 14/14 TC file Phase B done 2026-05-10 (sau batch 03+05+07+08+09+10+14 + 2-source verify NotebookLM `4dd0675e`). **8 BUG VALID cumulative** (5 Critical + 1 High + 3 Medium) + 11 OBS GAP + 17 SPEC-CLARIFY active. Total ~244/271 TC tested, ~67/244 PASS conclusive (~27% conclusive rate). 8/14 file đã chạy với 67 PASS / 13 FAIL/BUG / 11 OBS / 64 DEFERRED / 12 BLOCKED / 8 N/A.

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-FR-IV-01-quan-ly-tvv-CRUD.md` | 34 | ⚠️ **12/22 PASS** (2026-05-09) | CRUD core + 5 BUG (013 Critical list leak DP role + 014/015/016 + 017 Investigate). 9 BUG VALID prior batch |
  | B2 | `02-TC-FR-IV-02-tim-kiem-tvv.md` | 19 | ⚠️ 5 PASS / 2 FAIL / 12 DEFERRED (2026-05-09 v2) | **BUG-CGTVV-008 Critical**: Backend API `/export` 404 → block Export PL1 BTP compliance |
  | B3 | `03-TC-FR-IV-03-13-dang-ky-tiep-nhan.md` | 26 | ⚠️ **5 PASS / 4 FAIL/BUG / 14 DEFERRED / 2 N/A (2026-05-10)** | **BUG-CGTVV-022 Critical (NEW)**: Email duplicate KHÔNG enforce + **BUG-CGTVV-025 High (NEW)**: NHT UI entry point `/chuyen-gia-tvv/tao-moi` 403 → block FR-IV-03 main flow + BUG-026 Medium TC TV list 403 cascade. ERR-CT-01 NGUYÊN VĂN match. D.2.1 OUT confirmed gộp Tab Thẩm định direct |
  | B4 | `04-TC-FR-IV-04-cap-nhat-nang-luc.md` | 14 | ⚠️ 1/4 PASS (2026-05-09) | BUG-018 High form Năng lực thiếu fields chuyên môn |
  | B5 | `05-TC-FR-IV-05-10-xem-chi-tiet-lich-su.md` | 12 | ⚠️ **3 PASS / 5 PARTIAL / 1 FAIL/OBS / 3 DEFERRED (2026-05-10)** | TC-CT-004 ERR-HS-01 NGUYÊN VĂN match. UI 6 tabs vs spec 5 (extra "HĐ tư vấn"). Tab Thẩm định disabled drift. Empty state Điểm TB "—" match INF-TVV-DG-01. 3 TC lịch sử DEFERRED env không có VV với TVV |
  | B6 | `06-TC-FR-IV-06-tham-dinh.md` | 16 | ⚠️ **9/14 PASS** (2026-05-09) | 7/9 SM transitions verified. ERR-TD-02 NGUYÊN VĂN MATCH. BUG-019 Medium thiếu Lĩnh vực |
  | **B7** | `07-TC-FR-IV-07-phe-duyet.md` | 24 | ⚠️ **3 PASS w/ drift / 2 FAIL / 19 DEFERRED (2026-05-10)** | **BUG-CGTVV-023 Critical (NEW)**: Modal Phê duyệt MISSING so_quyet_dinh + y_kien_phe_duyet + backend POST `/phe-duyet` không enforce ERR-PD-05 (lưu NULL). Block compliance NĐ 77/2008. ERR-PD-03 drift wording. TC-PD-001 happy path PASS auto cấp TK |
  | **B8** | `08-TC-FR-IV-08-cong-khai.md` | 18 | ⚠️ **3 PASS / 3 PASS w/ drift / 1 PARTIAL / 1 FAIL / 10 DEFERRED (2026-05-10)** | **BUG-CGTVV-024 Critical Security (NEW)**: XSS sanitize KHÔNG enforce server-side. Lưu raw `<script>` + `javascript:` payload. Vi phạm EC-SEC-06a 3-layer sanitize. ERR-CK-01 NGUYÊN VĂN match. Modal MD-CONG-KHAI 2 fields verified |
  | **B9** | `09-TC-FR-IV-09-CROSS-01-danh-gia.md` | 12 | ⚠️ **3 PASS / 9 DEFERRED (2026-05-10)** | TC-DG-002 ERR-DG-01 NGUYÊN VĂN MATCH. INF-TVV-DG-01 empty state diemTb null match. **BUG-028 Low** field name drift `diemThoiGian` vs spec `diem_dung_han`. **OBS-037**: CB role allowed POST đánh giá (spec FR-IV-09 chỉ DN). 9 DEFERRED env 1 VV DA_DANH_GIA + token revoke during batch |
  | **B10** | `10-TC-FR-IV-11-12-cap-nhat-trang-thai.md` | 17 | ⭐ **7/7 conclusive PASS / 10 DEFERRED (2026-05-10)** | Best file batch! **5 NGUYÊN VĂN match**: ERR-TT-01 (invalid transition) + ERR-TT-02 với count substitution + **v3.1 guard HOI_DAP confirmed** ("Tư vấn viên đang có 2 vụ việc và 1 hỏi đáp chưa hoàn thành, không thể vô hiệu hóa") + ERR-TT-03 (lý do ≥10) + ERR-AUTH-VPD-00-02. SM-TVV HOAT_DONG ↔ TAM_DUNG verified |
  | B11 | `11-TC-FR-IV-NEW-01-quan-ly-TC-TV.md` | 22 | ⚠️ 3/5 PASS (2026-05-09 v2) | TC TV module IMPL đầy đủ |
  | B12 | `12-TC-FR-IV-NEW-02-04-trang-thai-phe-duyet-TC-TV.md` | 18 | ⚠️ **10/10 PASS** (2026-05-09 v3) | SM-TCTV full lifecycle 7/9 transitions PASS |
  | B13 | `13-TC-FR-IV-NHT-01-02-03-quan-ly-NHT.md` | 23 | ⚠️ **14 PASS / 1 FAIL** (2026-05-09 v3) | **BUG-CGTVV-010 Critical**: NHT không xem được hồ sơ chính mình. 4 NGUYÊN VĂN match |
  | **B14** | `14-TC-permission-matrix.md` | 17 | ⚠️ **8 PASS / 1 PARTIAL / 8 DEFERRED (2026-05-10)** | nht_01 cross-tenant 100% block (GET/PATCH/DELETE all 403). ERR-AUTH-VPD-00-02 NGUYÊN VĂN match. OTP=666666 + redirect login verified. **BUG-CGTVV-027 Medium**: multi-role display drift. **OBS-036**: single-session enforce CB role (spec EC-SEC-03a 3 phiên đồng thời) |

  **Bug summary cumulative all 14 file Phase B (2026-05-09 + 2026-05-10):** **8 bug VALID** (5 Critical + 1 High + 3 Medium) + 2 Low. **5 ship-blocker REAL**:
  1. ~~BUG-008 Critical~~ → BUG-CGTVV-008 backend API Export TVV PL1 BTP 404 (W3.3 dependency)
  2. BUG-CGTVV-010 Critical: NHT không xem được hồ sơ chính mình (403 ERR-PERM-SYS-00-01)
  3. BUG-CGTVV-013 Critical: List endpoint không filter donVi cho DP role (data leak — DP user thấy 37 TW TVV)
  4. **BUG-CGTVV-022 Critical (NEW 2026-05-10)**: Email duplicate KHÔNG enforce → vi phạm FR-IV-03 step 5 + ERR-DK-09. 2-source verify NotebookLM `4dd0675e` + SRS local
  5. **BUG-CGTVV-023 Critical (NEW 2026-05-10)**: Modal Phê duyệt MISSING fields + backend không enforce ERR-PD-05. Block compliance NĐ 77/2008. 2-source verify
  6. **BUG-CGTVV-024 Critical Security (NEW 2026-05-10)**: XSS sanitize KHÔNG enforce server-side cho mo_ta_cong_khai. Vi phạm EC-SEC-06a. 2-source verify
  7. **BUG-CGTVV-025 High (NEW 2026-05-10)**: NHT UI entry point `/chuyen-gia-tvv/tao-moi` 403 → block FR-IV-03 main flow. 2-source verify

  **3 Medium gap NEW**: BUG-026/027/028 (TC TV list cascade, multi-role display, field name drift)
  **11 OBS GAP** chờ BA confirm (drift wording, design choice intentional)

  4 bug v1 INVALID đã loại trong session 2026-05-09 (BUG-001/002/003/007 — false-positive qtht_01).
  **Cross-tenant verified 100%:** BR-AUTH-08 enforce qua API guard (cb_nv_dp_01 + nht_01 → 403 NGUYÊN VĂN exact). Riêng list endpoint cb_nv_dp_01 leak (BUG-013).

  **B done:** Còn 0/14 file. Phase B 2026-05-10 batch 7 file (03+05+07+08+09+10+14) bổ sung sau prior 7 file batch (01+02+04+06+11+12+13). Cleanup test data pending: 10+ TVV test + 2 duplicates email + XSS payload trên TVV-001 + TVV-019 soQuyetDinh NULL.
  - **Output:** `output/execution-test/chuyen-gia-tu-van-vien/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/` + `Tcs-report-03-05-07-08-09-10-14/` (PHASE-B-FINAL-SUMMARY-2026-05-10 + BUG-REPORT-2026-05-10)

### W2.3 Biểu mẫu (FR-09, 92 TC, 0.5 ngày)

- ✅ **A** — TC đã có (7 UC files 01-07 = 92 TC sau Codex review 2026-05-09 +8, was 84 TC, 4 audit files 08-11). Xong 2026-05-06 — BMAD A1-A7 full cycle + A4 inline merge 2026-05-06. UC98 LOẠI A7 (API thuần). 19 SPEC-CLARIFY pending BA (was 14, +5 sau Codex). Coverage BR formal §6 100%, AC SRS 28/28 = 100% (was 24/28), SM-BIEUMAU 6/6 transitions BIEU_MAU entity, Permission Matrix ~14/16 cells. Quality 86.7% PASS.
  - **Output:** `output/test-cases/bieu-mau/` (B-block CHỈ ref 7 file UC; file 08-11 là audit log)
- **B** — 7 TC file × 4 block (B-Seed → B-Run → B-Verify → B-Report). Áp dụng [Template prompt per-TC-file](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-quan-ly-thu-muc.md` | 17 | 🟢 ready | CRUD TM (A4 +4 edge: whitespace/mô tả/thu_tự/race CREATE; Codex +1 TC-TM-027 detail view). TK: cb_nv_tw_01 |
  | B2 | `02-TC-tim-kiem-thu-muc.md` | 11 | 🟢 ready | Search TM (A4 +3: Unicode/wildcard escape/boundary 200; Codex +1 TC-BM-211 pagination) |
  | B3 | `03-TC-cong-khai-thu-muc.md` | 9 | 🟢 ready | Publish/Unpublish TM (A4 +2: AN→CONG_KHAI re-publish/timeout; Codex fix TC-BM-305 BR-EC-20 → SPEC-CLARIFY-BM-15) |
  | B4 | `04-TC-quan-ly-bieu-mau.md` | 25 | 🟢 ready | CRUD BM + CR-01 Switch (A6 +3, A4 +5, A7 -1 UC98; Codex +3: TC-BM-422/423/424 list/detail/SM-BIEUMAU + fix TC-BM-416 SPEC-CLARIFY-BM-16) |
  | B5 | `05-TC-tim-kiem-bieu-mau.md` | 9 | 🟢 ready | Search BM (A4 +2: exact mã BM/multi-filter empty; Codex +1 TC-BM-509 pagination + fix TC-BM-507 SPEC-CLARIFY-BM-17) |
  | B6 | `06-TC-import-hang-loat.md` | 11 | 🟢 ready | Import wizard (A4 +3: metadata mismatch/duplicate/metadata 5MB; Codex BR-DATA-01 traceability note added) |
  | B7 | `07-TC-permission-matrix.md` | 10 | 🟢 ready | Permission cross-FR-VII (A4 +2: BN ngang cấp/DN download Cổng; Codex +2: TC-BM-PERM-009/010 CB_PD Import + NHT/TVV/CG block) |

  **Output:** `output/execution-test/bieu-mau/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W2.4 CT HTPLDN GĐ1 (FR-15, 100 TC, 0.5 ngày)

- ✅ **A** — TC đã có (8 UC files 01-08 = **100 TC sau Codex review 2026-05-09 +15** — was 85, 4 audit files 09-12). Xong 2026-05-06 — BMAD A1-A7 full cycle + A4 inline merge (+9 TC) + A6 inline merge (+2 TC fill gap audit/notification). Codex review 2026-05-09 GATE FAIL → patched: ERR codes 30/30 = 100% (was 77%), Permission Matrix ~94% (was 75%), Tạm dừng/Tiếp tục role correction per SRS line 213/241. **5 SPEC-CLARIFY** pending BA (CT-01/02/04/05/06). Coverage BR formal §6 100% + AC 100% + SM transitions 100% + ERR codes 100%.
  - **Output:** `output/test-cases/ct-htpldn-gd1/` (B-block CHỈ ref 8 file UC; file 09-12 là audit log)
- **B** — 8 TC file × 4 block (B-Seed → B-Run → B-Verify → B-Report). Áp dụng [Template prompt per-TC-file](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file). 🚫 chờ 3 bug-flow-CTHTPLDN verify.

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-quan-ly-ct-CRUD.md` | 15 | 🚫 chờ bug | CRUD core + audit log E2E. TK: cb_nv_tw_01 |
  | B2 | `02-TC-tim-kiem-ct.md` | 12 | 🚫 chờ bug | Search + Export Excel + sanitize SQL/XSS (Codex fix TC-CT-TK-007 BR-DATA-06→BR-DATA-07) |
  | B3 | `03-TC-lifecycle-ct.md` | 27 | 🚫 chờ bug | 6 transition SM-KH-CTHTPL + 2 cycle re-submit + Codex 2026-05-09 +10 (7 ERR codes thiếu + CB_NV Tạm dừng/Tiếp tục + Kích hoạt guard SPEC-CLARIFY-CT-05) |
  | B4 | `04-TC-trinh-phe-duyet-ct.md` | 6 | 🚫 chờ bug | DU_THAO → CHO_PHE_DUYET + concurrent submit |
  | B5 | `05-TC-phe-duyet-ct.md` | 10 | 🚫 chờ bug | BR-AUTH-05 cùng cấp + BR-FLOW-04 lý do TC + notification NV (TC-PD-CT-010) |
  | B6 | `06-TC-cong-bo-ct.md` | 9 | 🚫 chờ bug | BR-FLOW-05 API Cổng PLQG + rollback persistent. TC-CB-CT-009 SPEC-CLARIFY-CT-04 |
  | B7 | `07-TC-quan-ly-dot-bc.md` | 12 | 🚫 chờ bug | CRUD đợt BC TAO_DOT + Codex 2026-05-09 +2 (DOT-011 sửa state guard SPEC-CLARIFY-CT-06, DOT-012 thiếu trường) |
  | B8 | `08-TC-permission-matrix.md` | 9 | 🚫 chờ bug | Permission cross-FR-XI GĐ1. Codex 2026-05-09 +3 (PERM-007 CB_PD Read positive, PERM-008 CB_PD negative Hủy/Rút/Công bố, PERM-009 QTHT lifecycle Read-only) |

  **Output:** `output/execution-test/ct-htpldn-gd1/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

**Checkpoint W2:** Master data đủ → duyệt W3

---

## Wave 3 — LỚP 3 Giao dịch lõi (3 ngày)

### W3.1 Hỏi đáp (197 TC v3.1, 1 ngày) — ✅ Phase A done 2026-05-10 + Codex review applied

- ✅ **A** — Viết TC mới 7 file UC + 5 audit (00 plan + 08 A4 + 09 A5 + 10 A6 + 11 A7 + 12 Codex). 197 TC sau full A1-A7 + Codex (155 A3 + 32 A4 + 6 A6 GAP fix + 4 Codex). 11 SPEC-CLARIFY pending BA. Coverage: BR 100% (24/24), AC 97.4% (38/39), SM 100% (12/12), Permission 100% (21/21), Error 100% (45/45). Quality 9.75/10.
  - **Output:** `output/test-cases/hoi-dap/` (12 file)
- ⚠️ **B** — Phase B 4 sessions cumulative 2026-05-10. ~50/197 PASS (25.4%). **3 BUG Critical + 1 BUG Major + 5 OBS Major + 3 OBS Investigate + 3 EP-MISSING**.
  - **Kết quả:** ~50/197 PASS — 3 BUG Critical block ship (HD-001 mucDoPhucTap missing + PC-001 auto-filter + AUTH-001 cross-tenant POST). [BUG-REPORT-TONG-HOP-FR02-2026-05-10.md]
  - **Bug:** [BUG-REPORT-TONG-HOP-FR02-2026-05-10.md] — 0/16 đóng (chờ dev fix)
  - **Output:** `output/execution-test/hoi-dap/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/` + `_phase-b-status/status-2026-05-10-session4-FINAL.md`

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-quan-ly-hoi-dap.md` | 32 | ⚠️ partial | 14 PASS (TC-001/100/101/200/210/220/etc) + BUG-HD-001 Critical + BUG-HD-201 Major emoji strip + BUG-HD-PUT-001 + 4 BLOCKED batch xóa (EP-MISSING-02) |
  | B2 | `02-TC-tim-kiem-tong-hop.md` | 22 | ⚠️ partial | 8 PASS (search/SQL/XSS/pageSize) + 3 OBS (HDTK-100 invalid range + HDTK-204 Vietnamese broken + HDTK-020 ✅ FIXED) |
  | B3 | `03-TC-tiep-nhan-xu-ly.md` | 17 | ⚠️ partial | TC-TN-001 PASS happy + OBS-FR03-001 modal thiếu textarea + OBS-TN-001 SLA 5 ngày legacy |
  | B4 | `04-TC-quan-ly-tiep-nhan.md` | 25 | ⚠️ partial | TC-DXL-001/100/101/102/104 PASS + 4 BLOCKED (DXL-110..113 đổi mức độ) bởi BUG-HD-001 |
  | B5 | `05-TC-phan-cong-xu-ly.md` | 32 | ⚠️ partial | TC-PC-001/100/101/106 PASS + **BUG-PC-001 Critical 4-sub** auto-filter 48 candidates + CB_PD lẫn + no LIMIT 10 + no linh_vuc filter (sub-OBS-PC-004 SRS sort = uu_tien ASC → khối lượng ASC) |
  | B6 | `06-TC-phan-hoi-cau-hoi.md` | 28 | 🚫 BLOCKED | EP-MISSING-01 Gửi phản hồi 404 (5 endpoint thử). 2 PASS Lưu nháp |
  | B7 | `07-TC-phe-duyet-cong-khai.md` | 41 | ⚠️ partial | TC-PD-020/022/030/101 PASS (Cổng PLQG works) + EP-MISSING-03 batch phê duyệt + 5 BLOCKED chờ CHO_PHE_DUYET state seed |
  | B-CROSS | Permission BR-AUTH-08 | — | ⚠️ partial | 4 PASS (DP block TW READ/UPDATE/DELETE/transition) + **BUG-HD-AUTH-001 Critical** DP POST cross-tenant donViId=TW thành công 201 |

### W3.2 Vụ việc TGPL ⭐ (FR-05, 294 TC, module phức tạp nhất)

- ✅ **A** — TC đã có (14 file UC + 4 audit log, **294 TC** sau A4 inline +4 + A6 inline +1, 2026-05-06). BMAD A1-A7 full cycle: A1 đọc SRS v3.5 rev2 (2527 dòng) + A2 overview + A3 14 UC files + A4 4 cross-cutting edge cases inline merged + A5 trace matrix (≥95% BR, 98% AC, ≥94% errors, 95% SM transitions) + A6 quality 88.4% avg + 1 gap-fill (BR-SLA-03 escalate) + A7 0 violation (UC53 LGSP API + UC55 API Inbound + CROSS-01 scheduled job LOẠI module-level). ~50 SPEC-CLARIFY pending BA.
  - **Output:** `output/test-cases/vu-viec/` (14 UC + 00 + 08-11 audit)
- **B** — 14 TC file × 4 block (B-Seed → B-Run → B-Verify → B-Report). Áp dụng [Template prompt per-TC-file](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-quan-ly-vu-viec-DS.md` | 21 | 🚫 chờ bug + W2.1/W2.2 | UC51+UC58 SCR-V.I-01 DS + tìm kiếm |
  | B2 | `02-TC-tao-vu-viec-DN.md` | 23 | 🚫 chờ bug + W2.1 | UC52 DN gửi HS Tier 2 VNeID |
  | B3 | `03-TC-nhap-thu-cong-vv.md` | 25 | 🚫 chờ bug + W2.1 | UC54 nhập thủ công SCR-V.I-02 |
  | B4 | `04-TC-tiep-nhan-cms-ht-khac.md` | 14 | 🚫 chờ bug | UC55 CMS phần (API Inbound LOẠI A7) |
  | B5 | `05-TC-kiem-tra-hs.md` | 19 | 🚫 chờ bug | UC56 checklist 6 hạng mục Mẫu 01 NĐ55 |
  | B6 | `06-TC-quan-ly-hs-vv.md` | 21 | 🚫 chờ bug | UC57 SCR-V.I-03 chế độ CMS+DN |
  | B7 | `07-TC-phan-cong-xac-nhan.md` | 25 | 🚫 chờ bug + W2.2 | UC59+UC60 phân công Cá nhân/Tổ chức |
  | B8 | `08-TC-trinh-phe-duyet-pd.md` | 21 | 🚫 chờ bug | UC61+62+63 trình + TB + PD |
  | B9 | `09-TC-cap-nhat-ket-qua.md` | 21 | 🚫 chờ bug | UC65+66 KQ NHT + KQ cuối HOAN_THANH |
  | B10 | `10-TC-danh-gia-vv.md` | 19 | 🚫 chờ bug | UC67 đánh giá CB_NV/DN thang 0-10 |
  | B11 | `11-TC-cong-khai-vv.md` | 27 | 🚫 chờ bug | NEW-05 BR-PUBLIC-04 whitelist + BR-EC-20 atomic |
  | B12 | `12-TC-DN-bo-sung-thong-bao.md` | 29 | 🚫 chờ bug | NEW-02 + UC64 DN bổ sung + nhận TB |
  | B13 | `13-TC-cau-hinh-quy-trinh.md` | 11 | 🚫 chờ bug | NEW-01 QTHT versioning |
  | B14 | `14-TC-permission-matrix.md` | 18 | 🚫 chờ bug | Cross-FR-V.I BR-AUTH-01/03/04/05/08 + IDOR |

  **B chờ:** BUG-FLOW-VUVIEC-001 close + W2.1 (DN Phase B done) + W2.2 (CG-TVV Phase B done).
  - **Output:** `output/execution-test/vu-viec/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W3.3 TV Chuyên sâu (FR-12, 134 TC, 0.5 ngày)

- ✅ **A** — TC đã có (6 UC files 01-06 = 134 TC, 4 audit files 07-10). Xong 2026-05-07 — BMAD A1-A7 full cycle + A4 inline merge (+26 edge case) + A6 inline merge (+8 fill gap A5). **Codex review Round 1+2 2026-05-09: +9 TC + 13 fix R1 + 6 fix R2 → 125 → 130 → 134 TC.** R1 closes Error code matrix UC149/151/153 + ERR-TVCS-05 + INF-TVCS-TK-01 + TC-PERM-003 logic. R2 closes field constraint boundary (tom_tat/ghi_chu/anh_dai_dien) + cross-FR-14 hop_dong_tv_id + BR-DATA-04 SEQ uniqueness. 0 TC LOẠI A7. 19 SPEC-CLARIFY pending BA (17 cũ + MSG-01 + MSG-02 + CROSS-01 + SEQ-01). Coverage BR 100% + AC 100% + SM-TVCS/TLPL/HSPL 100% + Error ~100% + Field constraint 100% + Cross-FR-14 cover. Quality 9.13/10 → 9.5/10 → 9.7/10.
  - **Output:** `output/test-cases/tv-chuyen-sau/` (B-block CHỈ ref 6 file UC; file 07-10 là audit log)
- ⚠️ **B** — 6 TC file × 4 block done 2026-05-11: **49/134 PASS (37%)**. **6 BUG VALID NEW** (2 Critical ship-blocker: BUG-NEW-004 Export TVCS 404 + BUG-NEW-005 UC152 TLPL module backend missing; 4 Major: BUG-007 Ngày TV field missing form, BUG-NEW-001 UPDATE UI entry missing, BUG-NEW-006 UC149/151/153 endpoints missing, BUG-NEW-002 50KB no enforce). BUG-FR12-001 FIXED, BUG-003/004 INVALIDATED. 56 BLOCKED (CG.lvIds seed gap chặn T2-T8 + cần role rotation cb_pd_tw/dp + nht/cg login). Áp dụng [Template prompt per-TC-file](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-FR-X1-01-quan-ly-tvcs.md` | 44 | ⚠️ 14 PASS / 28 BLOCKED | 3 BUG NEW (Ngày TV form / UPDATE UI entry / 50KB BE). BUG-FR12-001 FIXED verified. CG seed gap chặn T2-T8. |
  | B2 | `02-TC-FR-X1-02-tim-kiem-tvcs.md` | 20 | ✅ 17 PASS / 1 BLOCKED role / 3 UI defer | 0 BUG. FTS unaccent + sanitize + boundary BR-EC-13/BR-DATA-07 enforce. |
  | B3 | `03-TC-FR-X1-04-quan-ly-hspl.md` | 20 | ⚠️ 12 PASS / 4 BLOCKED role / 3 UI defer | BUG-NEW-004 Critical Export TVCS 404 (HSPL export WORKS). HSPL CRUD/filter/validation full health. |
  | B4 | `04-TC-FR-X1-06-quan-ly-tu-lieu-pl.md` | 21 | 🔴 0 PASS / 21 BLOCKED | BUG-NEW-005 Critical UC152 TLPL backend module MISSING (15+ endpoint patterns 404). |
  | B5 | `05-TC-permission-matrix.md` | 14 | ⚠️ 4 PASS TW scope / 10 BLOCKED role | 0 BUG. BR-AUTH-01 + IDOR + UUID validation TW OK. Cần role rotation 6 accounts. |
  | B6 | `06-TC-FR-X1-03-05-07-API-inbound-side-effect.md` | 15 | ⚠️ 2 PASS / 11 BLOCKED / 2 UI defer | BUG-NEW-006 Major UC149/151/153 endpoints MISSING. Thông báo /api/v1/thong-baos WORKS. |

  **Resume Phase B:** Dev fix 6 BUG + seed CG.lvIds + session role rotation 6 accounts.
  - **Output:** `output/execution-test/tv-chuyen-sau/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W3.4 Đào tạo Khóa học (FR-03, 263 TC, 1 ngày) — ✅ Phase A done 2026-05-08

- ✅ **A** — TC đã có (13 UC files 01-13 = 263 TC tổng / 262 active sau A7 -1 LOẠI, 4 audit files 14-17). Xong 2026-05-08 — BMAD A1-A7 full cycle: A1 đọc SRS v3.5 (1963 dòng) + A2 overview + A3 13 UC files (240 TC) + A4 edge inline merge (+15 TC, 17 categories) + A5 trace matrix (BR 100% / AC 99.1% / SM 100% / Error 97.9% / Permission 79% explicit) + A6 review fill gap (+8 TC, quality 9.09/10) + A7 filter UI (-1 LOẠI TC-NHCH-012 migration backfill, 11 TC SỬA DB→UI/network). 38 SPEC-CLARIFY pending BA. Coverage BR/SM = 100% / AC 99.1% / Error 97.9%.
  - **Output:** `output/test-cases/dao-tao/` (13 UC + 4 audit 14/15/16/17)
- 🚫 **B** — 13 TC file × 4 block (B-Seed → B-Run → B-Verify → B-Report). Áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file). 🚫 chờ B7 close + 3 học viên seed (qua DN chuyên trang FR-III-04).

  | # | TC file | TC | Status | Note |
  |---|---|---:|---|---|
  | B1 | `01-TC-FR-III-14-15-16-ke-hoach-nam.md` | 27 | 🚫 chờ seed | KH năm SM-KH-DAO-TAO 7 trans + 5 CPF (Mô hình A cấp 1). TK cb_nv_tw_01 |
  | B2 | `02-TC-FR-III-01-02-quan-ly-CTDT.md` | 30 | 🚫 chờ B1 | CTDT SM-CTDT 8 trans + Mô hình A guard (KH năm cha DA_DUYET) |
  | B3 | `03-TC-FR-III-13-de-xuat-dao-tao.md` | 14 | 🚫 chờ seed | Đề xuất DN/NHT submit + CB tiếp nhận, 3 state SM-DEXUAT |
  | B4 | `04-TC-FR-III-22-lich-hoc-buoi-day.md` | 16 | 🚫 chờ B5 | Lịch học LICH_HOC CRUD + overlap detection |
  | B5 | `05-TC-FR-III-01-quan-ly-khoa-hoc.md` | 31 | 🚫 chờ B2 | Khóa học SM-KHOAHOC 12 trans + GV junction N-N + 5 CPF |
  | B6 | `06-TC-FR-III-03-04-dang-ky-hoc-vien.md` | 18 | 🚫 chờ B5 + DN seed | CB duyệt/từ chối + DN chuyên trang + import Excel |
  | B7 | `07-TC-FR-III-05-06-diem-danh-ket-qua.md` | 27 | 🚫 chờ B6 | Điểm danh enum 3 + BR-KQ-01 5 ngưỡng + BR-KQ-02 AND |
  | B8 | `08-TC-FR-III-18-19-cong-bo-ket-qua.md` | 19 | 🚫 chờ B7 | UC37 PD KQ + UC38 Hướng B KHÔNG PDF + Retry BR-INTG-05 |
  | B9 | `09-TC-FR-III-07-08-quan-ly-bai-giang.md` | 17 | 🚫 chờ seed | Bài giảng 3 loại Slide/PDF/Video + 5 CPF |
  | B10 | `10-TC-FR-III-09-10-NEW-01-02-03-NHCH-de-KT.md` | 26 active (1 LOẠI A7) | 🚫 chờ seed | NHCH + Đề KT (random/manual + phân phối) |
  | B11 | `11-TC-FR-III-11-12-quan-ly-giang-vien.md` | 13 | 🚫 chờ seed | GV CRUD + Tab Lịch sử derive junction |
  | B12 | `12-TC-FR-III-20-xuat-docx-pdf.md` | 7 | 🚫 chờ B2 | Xuất DOCX/PDF cho CTDT DA_DUYET/DA_CONG_KHAI/HOAN_THANH |
  | B13 | `13-TC-permission-matrix.md` | 17 | 🚫 chờ all B | Cross-FR-III BR-AUTH-01/05/08 + IDOR + cron actor |

  **Output:** `output/execution-test/dao-tao/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

**Checkpoint W3:** Lõi đủ data Hoàn thành → duyệt W4

---

## Wave 4 — LỚP 4 Phái sinh (2 ngày)

### W4.1 Hợp đồng TV (FR-14, 85 TC v3.5, was estimate ~50) — ✅ Phase A done 2026-05-10 + Codex review applied

- ✅ **A** — TC đã có (6 UC files 01-06 = 85 TC sau Codex apply, 4 audit files 07-10). Xong 2026-05-10 — BMAD A1-A7 full cycle + A4 inline merge (21 TC) + A6 fill (5 TC) + Codex review (+5 TC fix 2 P0 + 5 P1 + 5 P2). 16 SPEC-CLARIFY pending BA (3 RESOLVED: HDTV-01 + HDTV-02 + HDTV-09 sửa enum). Coverage BR formal 6/6 = 100%, AC SRS 11/11 = 100%, ERR Code 7/7 = 100%, trang_thai field enum 4/4 = 100%, Permission Matrix 16/16 = 100%, Entity Inputs 11/11 = 100%. Quality 93% PASS.
- ⚠️ **B** — Phase B done 2026-05-11: **25/85 TC PASS (29.4%) + 7 BUG VALID + 1 OBS GAP + 52 BLOCKED**. Aggregate: [`output/execution-test/hop-dong-tv/_phase-b-summary-2026-05-11.md`](../../output/execution-test/hop-dong-tv/_phase-b-summary-2026-05-11.md). **2 Critical block ship**: BUG-HDTV-FUNC-001 ben_a không auto-fill + BUG-LVV-001 thiếu Accordion "Vụ việc liên kết" + nút [+ Liên kết VV]. **5 Major**: form thiếu noi_dung/ghi_chu/file_dinh_kem + Accordion Nhật ký + Thanh lọc thiếu TVV dropdown. ENV blocker: token revoke + rate-limit 429.
  - **Output:** `output/execution-test/hop-dong-tv/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

  | # | TC file | TC | Status | Note |
  |---|---------|----|--------|------|
  | B1 | `01-TC-quan-ly-hd-tv-CRUD.md` | 26 | ⚠️ 14 PASS / 5 BUG / 1 GAP / 5 BLOCKED | BUG-FUNC-001/002/003/004 + AUDIT-001. OBS-001 mã 4-digit |
  | B2 | `02-TC-moc-tien-do.md` | 9 | 🚫 1 UI / 8 BLOCKED env token revoke | UI surface verified, inline-edit không reached |
  | B3 | `03-TC-thanh-toan-giai-doan.md` | 11 | 🚫 2 UI / 9 BLOCKED | UI surface + progress bar OK |
  | B4 | `04-TC-lien-ket-vu-viec.md` | 11 | 🚫 1 PASS / 1 Critical BUG-LVV-001 / 10 BLOCKED | Accordion VV missing block toàn bộ TC link/unlink |
  | B5 | `05-TC-tim-kiem-hd-tv.md` | 12 | ⚠️ 6 PASS / 1 BUG-HDTK-001 Major / 5 BLOCKED | TVV filter missing |
  | B6 | `06-TC-permission-matrix.md` | 16 | 🚫 1 PASS / 15 BLOCKED | Rate-limit block role switch |

### W4.2 Chi trả (FR-06, 137 TC, 1 ngày) — ✅ Phase A done 2026-05-10 + Codex review applied

- ✅ **A** — TC viết xong (10 UC files + 5 audit files = 15 file). 137 TC sau A1-A7 + A4 +39 edge + A6 +5 fill GAP-A5 + Codex review (3 P0 BUG + 4 P1 + 3 P2 → all 10 fixed). Coverage BR 100% (sau fill BR-CALC-03 ngày lễ), AC 97.4% (1 SPEC-CLARIFY-CT-13), Error code 100% (24/24 sau Codex link), SM 92.9% (1 SPEC-CLARIFY-CT-01), Permission 100%. 13 SPEC-CLARIFY pending BA. Quality 9.8/10. Xong 2026-05-10 — BMAD A1-A7 full cycle + Codex apply.
- ⚠️ **B** — Phase B done 2026-05-10 + Re-run 2026-05-11: **51/137 = 37% conclusive** (49 PASS + 2 BUG Critical + 8 OBS + 4 SPEC-CLARIFY active + 2 RESOLVED). Còn 45 BLOCKED final (CHO_TIEP_NHAN/DANG_KIEM_TRA + LGSP/DVC inbound endpoint không expose — verified NotebookLM Phụ lục D-02). **2 BUG Critical**: PERM-001 qtht_01 không R toàn HT + PERM-002 CB_NV phê duyệt thành công vi phạm BR-AUTH-05. Aggregate: [`output/execution-test/chi-tra/_re-run-phase-b-2026-05-11.md`](../../output/execution-test/chi-tra/_re-run-phase-b-2026-05-11.md).
  - **Output:** `output/execution-test/chi-tra/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

  | # | TC file | TC | Status | Note |
  |---|---------|----|--------|------|
  | B1 | `01-TC-FR-V.II-02-quan-ly-HS-de-nghi.md` | 19 | 🚫 chờ E3 | DS 5 tab + filter + tiếp nhận + DN rút |
  | B2 | `02-TC-FR-V.II-03-kiem-tra-HS.md` | 15 | 🚫 chờ E3 | UC70 checklist + counter bổ sung |
  | B3 | `03-TC-FR-V.II-05-danh-gia-tieu-chi.md` | 19 | 🚫 chờ E3 | UC72 BR-CALC-01/02 auto-calc 3 quy mô |
  | B4 | `04-TC-FR-V.II-09-tham-dinh.md` | 13 | 🚫 chờ E3 | UC76 đối chiếu 4 checklist + 3 kết quả |
  | B5 | `05-TC-FR-V.II-11-12-trinh-PD-phe-duyet.md` | 18 | 🚫 chờ E3 | UC78 + UC79 + multi-loop trả về N:1 |
  | B6 | `06-TC-FR-V.II-13-cap-nhat-thanh-toan.md` | 12 | 🚫 chờ E3 | UC80 cập nhật TT + DA_DUYET → TU_CHOI |
  | B7 | `07-TC-FR-V.II-14-DN-bo-sung-HS.md` | 10 | 🚫 chờ E3 | GAP-V.II-01 DN bổ sung qua DVC |
  | B8 | `08-TC-FR-V.II-08-thong-bao-TVV.md` | 6 | 🚫 chờ E3 | UC75 TVV nhận TB |
  | B9 | `09-TC-API-side-effect.md` | 7 | 🚫 chờ E3 + admin endpoint | LGSP inbound/outbound + in-app TB side-effect |
  | B10 | `10-TC-permission-matrix.md` | 18 | 🚫 chờ E3 | BR-AUTH-05 cùng cấp + BR-AUTH-08 scope đơn vị |

### W4.3 TV Nhanh (FR-13, 100 TC v3.5) — ✅ Phase A done 2026-05-10 + Codex review applied

- ✅ **A** — Viết TC mới 6 file UC + 5 audit (00 plan + 07 A4 + 08 A5 + 09 A6 + 10 A7). 100 TC sau A1-A7 + Codex apply (76 base + 18 A4 edge + 4 A6 fill + 2 Codex P1: TC-DGTV-104 header + TC-DGTV-301 doanh_nghiep_id missing). 11 SPEC-CLARIFY pending BA. Coverage BR/Permission/Error/SM/State/Entity = 100%, AC 96.2% (1 gap UI Cổng PLQG OOS). Codex Gate PASS (0 P0, 4 P1 + 6 P2 đã apply). Quality 9.4/10.
- 🚫 **B** — Chạy khi E4 + Kho QA. **Khi A xong → breakdown per-TC-file áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).**
  - **Output:** `output/execution-test/tv-nhanh/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

  | # | TC file | TC | Status | Note |
  |---|---------|----|--------|------|
  | B1 | `01-TC-FR-X2-01-quan-ly-kho-cau-hoi.md` | 33 | 🚫 chờ E4 | UC154/155/157 CRUD Kho + 3 nguồn + Phê duyệt + Tìm kiếm |
  | B2 | `02-TC-FR-X2-02-quan-ly-phien-tu-van.md` | 19 | 🚫 chờ E4 | FR-X.2-02 phiên TVN + TOP 5 + SM-TVNHANH + auto HET_HAN |
  | B3 | `03-TC-FR-X2-03-04-DN-chuyen-trang-side-effect.md` | 9 | 🚫 chờ E4 + admin endpoint | API inbound DN gửi câu hỏi + DN search side-effect (network MCP wrap) |
  | B4 | `04-TC-FR-X2-05-API-inbound-danh-gia.md` | 17 | 🚫 chờ E4 + admin endpoint | UC158 API inbound DG + Idempotency-Key 24h + headers BB |
  | B5 | `05-TC-FR-X2-06-cong-khai-kho.md` | 16 | 🚫 chờ E4 + Cổng PLQG mock | UC156 CK/Hủy CK + BR-PUBLIC + API outbound mock |
  | B6 | `06-TC-permission-matrix.md` | 6 | 🚫 chờ E4 | Cross BR-AUTH (Kho + Phiên TVN) |

### W4.4 Đánh giá HQ (FR-08, 167 TC v3.5) — ✅ Phase A done 2026-05-10 + Codex review applied

- ✅ **A** — Viết TC mới 7 file UC + 5 audit (00 plan + 08 A4 + 09 A5 + 10 A6 + 11 A7 + 12 Codex). 167 TC sau A1-A7 + Codex apply (84 base + 49 A4 edge + 11 A6 fill + 23 Codex apply). 6 SPEC-CLARIFY pending BA (DG-02/03/04/05/07/08), 2 RESOLVED (DG-01 read-only mode + DG-06 WRN-DG-TR-01). Coverage BR/AC/SM/Error = 100% (10 BR / 28 AC / 13 SM transitions / 22 ERR), Permission Matrix 95% (16 explicit cells), Entity CRUD 95%. Codex Gate PASS (4 P0 + 16 P1 + 10 P2 = 30/30 applied). Quality 9.65/10.
- 🚫 **B** — Chạy khi A ✅ + Vụ việc Hoàn thành (W3.2) + D2. **Khi A xong → breakdown per-TC-file áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).**
  - **Output:** `output/execution-test/danh-gia/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

  | # | TC file | TC | Status | Note |
  |---|---------|----|--------|------|
  | B1 | `01-TC-FR-VI-01-lap-ke-hoach.md` | 37 | 🚫 chờ W3.2 VV B done | UC83 + Phần A list/filter/form/CRUD/Hủy/file_dinh_kem/co_quan_duoc_dg |
  | B2 | `02-TC-FR-VI-02-thiet-lap-tieu-chi.md` | 19 | 🚫 chờ DM Tiêu chí seed | UC84 Tab 1 + BR-CALC-04 trọng số 100% + tham chiếu DM UC109 |
  | B3 | `03-TC-FR-VI-03-04-phan-cong-duyet-pc.md` | 28 | 🚫 chờ A2 done | UC85+UC86 Tab 2 + Trình/Duyệt/Từ chối PC + BR-AUTH-05 + BR-NOTIF-01 |
  | B4 | `04-TC-FR-VI-05-06-chon-vv-cham-diem.md` | 29 | 🚫 chờ W3.2 VV HOAN_THANH | UC87+UC88 Tab 3 + BR-CALC-04 normalized + multi-evaluator |
  | B5 | `05-TC-FR-VI-07-08-09-bao-cao-trinh-duyet.md` | 32 | 🚫 chờ B4 done + 13 cột seed (FR-04/06/03) | UC89+UC90+UC91 Tab 4 + Xuất XLSX/DOCX TT17 + 13 cột BC |
  | B6 | `06-TC-FR-VI-10-nhan-ket-qua.md` | 8 | 🚫 chờ B5 đợt HOAN_THANH | FR-VI-10 read-only cơ quan được ĐG |
  | B7 | `07-TC-permission-matrix.md` | 16 | 🚫 chờ B1-B5 baseline | Cross BR-AUTH-01/05/08 + BR-FLOW-04 + BR-NOTIF-01 + audit immutability |

**Checkpoint W4:** Phái sinh đủ → duyệt W5

---

## Wave 5 — LỚP 5 Tổng hợp & Đầu ra (2 ngày)

### W5.1 CT HTPLDN GĐ2 (FR-15, 74 TC v3.1, was estimate ~50) — ✅ Phase A done 2026-05-10 + Codex review applied

- ✅ **A** — TC viết xong (7 UC files 01-07 = 74 TC sau Codex review 2026-05-10 +1, was 73 TC after A1-A7; 5 audit files 08-12). 51 A3 base + 19 A4 edge + 3 A6 fill GAP-A5 + 1 Codex TC-PERM-017 + Codex sửa TC-TH-019 + rename TC-PD-BC-010. 9 SPEC-CLARIFY pending BA. Coverage BR 12/12 = 100% (loại BR-DATA-01 N/A); AC 12/12 = 100%; SM 11/11 = 100% (5 SM-DOT-BC + 6 SM-BC sub); ERR 9/9 + 1 WRN = 100%; Permission Matrix ~33/64 explicit + 31 suy luận = 100%. Quality 9.17/10 → 9.3/10 sau Codex apply. Codex Gate: initial FAIL (2 P0 + 4 P1 + 1 P2) → sau verify 3 APPLY + 4 REJECT (false positive/hallucinated/out-of-scope).
- 🚫 **B** — Chạy khi W2.4 (CT GĐ1 done) + W3.2 (Vụ việc HOAN_THANH cho gợi ý số liệu cascade) + W4.2 (Chi trả DA_DUYET cho tổng chi phí). **Khi unblock → breakdown per-TC-file áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).** 🚫 chờ W3.2 BUG-VUVIEC-001 + W4.2 E3 unblock + cascade data.
  - **Output:** `output/execution-test/ct-htpldn-gd2/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W5.2 Báo cáo TK (FR-11, 129 TC sau Codex)

- ✅ **A** — Phase A done 2026-05-10 (129 TC sau A1-A7 + Codex review apply: 110 base + 15 A4 edge inline + 3 A6 fill + 1 Codex F-03 PERM unauth — 5 file UC + 5 audit). Strategy "1 đại diện + smoke" — file 01 representative TPL-REPORT-FULL via FR-IX-01 (39 TC), file 02 smoke 23 BC (40 TC), file 03 permission 2-tier (19 TC), file 04 export TT17/2025 (19 TC), file 05 charts (12 TC). 10 SPEC-CLARIFY pending BA (BC-01 RE-OPEN 50K vs 10K + BC-11 NEW BR-SLA-02 ngưỡng %). Coverage BR formal 100%, AC 100% sau A6 fill, Error 100%, Permission 100% sau F-09. Quality 9.55/10. Codex Gate PASS (1 P0 + 4 P1 + 4 P2 → ALL applied).
  - **Output:** `output/test-cases/bao-cao-tk/` (5 UC + 00 + 08-12 audit)
- 🚫 **B** — Chạy khi A ✅ + 9 module có data DA_DUYET. **Khi A xong → breakdown per-TC-file áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).**
  - **Output:** `output/execution-test/bao-cao/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W5.3 Dashboard (FR-01, 178 TC v3.5, was estimate ~40) — ✅ Phase A done 2026-05-10 + Codex review applied

- ✅ **A** — TC viết xong (8 UC files 01-08 = 178 TC sau Codex apply, 5 audit files 09-13). Xong 2026-05-10 — BMAD A1-A7 full cycle (manual variant) + A4 inline merge (30 edge TC) + A6 fill (7 TC) + Codex review (2 P0 + 3 P1 → all 5 fixed, +10 TC: 6 TPL outputs cho KPI-02..07 + 4 Permission P5-P8 cho QTHT/CB_PD). 4 SPEC-CLARIFY pending BA (DASH-01/03/04/05; **DASH-02 RESOLVED** by Codex P0-1/P0-2 → relative %). Coverage BR 6/6 = 100%, AC 74/74 = 100%, Permission Matrix 60/60 = 100% (P5-P8 cho QTHT + CB_PD explicit), Error 5/5 = 100%, State enum source 7/7 = 100% (KPI-07 8 loại trừ exhaustive), Outputs TPL-DASH-KPI 28/28 = 100%. Quality 9.6/10. Codex Gate PASS. 11 TC DEFERRED (cần Chrome DevTools network throttling cho stub backend 5xx — workaround feasible). 0 LOẠI A7. **Module READ-ONLY** — không có transition.
- 🚫 **B** — Chạy khi A ✅ + ≥3 record/state cuối từ mỗi module nguồn (HD MOI + VV 5 sống/HOAN_THANH + KH DANG_DIEN_RA/DA_KET_THUC + TVV DANG_HOAT_DONG + KQ_DANH_GIA + KQ_DAO_TAO). **Khi unblock → breakdown per-TC-file áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).**
  - **Output:** `output/execution-test/dashboard/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

### W5.4 API Kết nối (FR-16, ~50 TC)

- 📝 **A** — Viết TC mới (18 outbound; 8 inbound TODO clarify)
- 🚫 **B** — Chạy khi A ✅ + data CONG_KHAI từ 9 module. **Khi A xong → breakdown per-TC-file áp dụng [Template](#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file).**
  - **Output:** `output/execution-test/api-ket-noi/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`

**Checkpoint W5:** Final aggregate → user duyệt đóng plan

---

## D-Final — Aggregate (0.5 ngày)

- ⏳ **DF.1** Tổng hợp 20 functional-detailed report → `output/execution-test/_aggregate-detailed-tc.md`
- ⏳ **DF.2** Retest TC FAIL nếu dev fix kịp (cap 1 lần/TC)
- ⏳ **DF.3** Update plan + todo status final

---

## Risk

| ID | Risk | Module ảnh hưởng | Mitigation |
|---|---|---|---|
| R1 | Skill BMAD generate TC chất lượng thấp | All Phase A | A4 edge-case-hunter + A6 test-review bắt buộc |
| R2 | BUG-VUVIEC-001 STILL OPEN R8 | W3.2 + W4.2 + W4.4 + W5.1 | Phase A vẫn viết, defer Phase B |
| R3 | BUG-TVCS-003/004 STILL OPEN R8 | W2.2 + W3.3 | Phase A viết, defer Phase B |
| R4 | BUG-HOIDAP-001 + 004 Open | W3.1 (4 TC skip) | Skip TC, đánh dấu defer |
| R5 | E1-E4 chưa unblock | W4.1-3 + W5.x | DEFER Wave 4-5 nếu cuối T2 chưa ready |
| R6 | Phase A blow up >2 ngày/module | All Phase A | Cap cứng, P0 trước, P1/P2 defer |
| R7 | 5 mâu thuẫn SRS pending BA | Cross-module | Quote BA email, không log bug mới |
| R8 | 5 file REVIEW chưa merge | W1 + W2.1 + W3.1 | D0.2 audit trước W1 |
| R9 | SRS update cascade nhiều module cùng lúc (Phase C) | All ✅ modules | User tự kiểm soát thứ tự ưu tiên theo Lớp dependency 1→5; KHÔNG cap cứng số file/ngày — tùy bandwidth thực tế |
| R10 | Bug VALID cũ thành INVALID khi SRS đổi (Phase C C4.1) | All ✅ modules có bug log | Re-validate 2-source bắt buộc; ghi rõ status transition trong bug-report ("VALID v3 → INVALID v3.1 do spec clarify ...") |

---

## Quy tắc update (BẮT BUỘC)

Khi xong 1 task:
1. Flip icon trên dòng task (A hoặc B) → ✅/⚠️/🚫
2. Cập nhật bảng "Tiến độ tổng" đầu file nếu wave thay đổi
3. Notify cell Phase B của module đó nếu Phase A vừa xong → 🚫 chờ TC chuyển 🟢 (nếu không bug khác)
4. Update bảng §2 Scope trong [`plan.md`](plan.md) cùng lúc
