# Cross-module review summary — 18 module test plan

> **Source:** self-review qua `agent-skills:code-reviewer` (Phase 2, fallback từ Codex CLI bị user interrupt)
> **Generated:** 2026-05-12 22:15:00
> **Coverage:** 18/18 module — verdict ban đầu **REVISE** toàn bộ
> **Total review feedback:** 1052 dòng across 18 review.md files
> **Reviewers sampled cho aggregate:** fr-16-api (74) · fr-09-bieu-mau (71) · fr-04-chuyen-gia-tvv (71) · fr-06-chi-tra (70) · fr-13-tv-nhanh (67) · fr-05-vu-viec (65) · fr-11-bao-cao (52)

---

## Top pattern gap (lặp lại ≥3 module)

### Pattern 1 — Cross-module dep upstream thiếu TC verify trực tiếp

- **Module hit:** fr-05-vu-viec, fr-06-chi-tra, fr-04-chuyen-gia-tvv, fr-13-tv-nhanh, fr-11-bao-cao, fr-09-bieu-mau, fr-16-api
- **Mô tả gap:** Test plan có §2.6 list upstream dependency dạng text ("phụ thuộc FR-10 LINH_VUC_PL", "FR-05 VV HOAN_THANH", "FR-07 DN.quy_mo") nhưng KHÔNG có TC nào verify trực tiếp tình huống cross-module fail (vd LGSP inbound HSCT với `vu_viec_id` ≠ HOAN_THANH phải reject; DN đổi quy_mo SIEU_NHO → NHO snapshot HSCT giữ nguyên hay đổi; rename `DANG_HOAT_DONG`→`HOAT_DONG` impact 8 consumer dropdown). Mention ở §2.6 nhưng không xuống §4 TC table.
- **Action chung Phase 3:** Mỗi review đề xuất thêm 2-4 TC cross-module (vd `TC-API-07` FR-06 FK-state gate, `TC-15` bump từ 4→8 TC trong fr-04, mapping table TC-ID ↔ file trong fr-05).

### Pattern 2 — Mâu thuẫn nội bộ SRS v3.5 không được flag SPEC-CLARIFY / BA-Q

- **Module hit:** fr-05-vu-viec (BR-DATA-01 soft-delete vs C1 hard-delete), fr-11-bao-cao (Word→PDF + FR-IX-08 dia_ban + BR-DATA-06 50K vs 10K), fr-13-tv-nhanh (enum `kenh_tu_van` NHANH vs TV_NHANH + state `NHAP` ngoài CHECK constraint), fr-09-bieu-mau (`loai_hinh` enum vs free-text), fr-04-chuyen-gia-tvv (FR-VIII-26 sai → đúng FR-VIII-15)
- **Mô tả gap:** SRS v3.5 update có nhiều contradiction nội bộ chưa được BA chốt. Plan đang tự quyết theo 1 nguồn (vd 50K theo line 1088, không log BA-Q) — vi phạm memory `feedback_deep_review_before_ba_defer` (Sai spec → BẮT BUỘC NotebookLM + grep + escalate BA, không tự quyết).
- **Action chung Phase 3:** Thêm section §7 "Ambiguity / SPEC-CLARIFY" trong test-plan + log `BA-Q-FR{XX}-{NN}` với owner + deadline + gate TC tương ứng (Sai spec → 🚫 cho tới khi BA confirm). Không tự PASS.

### Pattern 3 — Cite SRS line không có path prefix (vi phạm memory `feedback_bug_srs_ref_path`)

- **Module hit:** fr-05-vu-viec, fr-09-bieu-mau, fr-04-chuyen-gia-tvv, fr-13-tv-nhanh, fr-06-chi-tra, fr-11-bao-cao (gần như mọi review)
- **Mô tả gap:** Test plan trộn 2 style cite: `srs-update-2026-5-5/srs-fr-XX.md:2074` (full path) và `:1664` (short). Memory 2026-05-06 yêu cầu path PREFIX bắt buộc — `srs-v3/` cho flow cũ, `srs-update-2026-5-5/` cho update mới. Cite không prefix → dev/BA verify nhầm SRS version, miss delta v3.5.
- **Action chung Phase 3:** Replace all short refs `:NNNN` thành full `<folder>/srs-fr-XX.md:NNNN`. Verify line numbers chính xác sau khi BA build srs-v3.5 từ CHANGELOG (line offset có thể shift).

### Pattern 4 — Permission matrix gộp action / không split per role × per action

- **Module hit:** fr-11-bao-cao (gộp "Xuất Excel/Word/PDF" 1 cell), fr-09-bieu-mau (cột TVV trùng CG context), fr-04-chuyen-gia-tvv (BR-AUTH-10 chỉ test 1/3 actor), fr-05-vu-viec (QTHT vs CB_NV_TW scope khác nhau không note rõ), fr-06-chi-tra (TVV scope HSCT chưa cite SRS)
- **Mô tả gap:** Matrix §2.3 thường gộp 3 action vào 1 cell, không cho phép test "role X được Excel nhưng KHÔNG được PDF". BR-AUTH-10 lọc kép áp dụng cho 3 actor (NHT + TVV + CG) nhưng chỉ 1 actor có TC. QTHT "All scope" vs CB_NV_TW "TW scope" 2 khái niệm khác — TC-PERM dễ FAIL false negative.
- **Action chung Phase 3:** Mở rộng permission matrix thành 11 role × {action atomic, không gộp}. Tách TC-PERM theo từng (role × action × scope filter) — vd `TC-PERM-NHT`, `TC-PERM-TVV`, `TC-PERM-CG` riêng cho BR-AUTH-10.

### Pattern 5 — Cross-cutting TC-ID (TC-AUTH, TC-PERM, TC-AUDIT, TC-FILTER, TC-NOTIF) không map vào file §3

- **Module hit:** fr-05-vu-viec (62 TC cross-cutting không map vào 23 file), fr-16-api (TC-FILTER 2/9 endpoint coverage), fr-06-chi-tra (TC-AUDIT-01 coarse 14 transition trong 1 TC), fr-13-tv-nhanh (BR-AUTH-08 cross-don_vi miss)
- **Mô tả gap:** §2.1 BR matrix cite TC-AUTH-01..05, TC-PERM-01..12, TC-AUDIT-01..04, TC-FILTER-01..09 — nhưng §3 file structure chỉ list file theo FR (`01-TC-list-filter.md`...`25-TC-data-migration.md`). Cross-cutting TC-ID không 1:1 map vào file nào → tester không biết viết TC này ở đâu.
- **Action chung Phase 3:** Bổ sung mapping table cuối §2: mỗi cross-cutting TC-ID → 1 file `XX-TC-*.md` cụ thể. Hoặc tạo file riêng `XX-TC-cross-cutting-PERM.md`, `YY-TC-cross-cutting-AUDIT.md`.

### Pattern 6 — Test method KHÔNG note rõ MCP UI vs API curl vs DB query

- **Module hit:** fr-05-vu-viec, fr-06-chi-tra, fr-16-api, fr-13-tv-nhanh, fr-09-bieu-mau
- **Mô tả gap:** Test plan §3-§5 chỉ ghi file structure + bảng đếm TC, KHÔNG note test method. CLAUDE.md "Tool routing — BẮT BUỘC từ 2026-05-05" yêu cầu Chrome DevTools MCP default; memory `feedback_test_method_ui_only` cấm API direct cho seed test. TC-CALC hybrid (UI verify display + API verify response) cần note rõ.
- **Action chung Phase 3:** Thêm cột "Test method" trong bảng §4 (UI MCP / API curl / DB query / k6 / Bruno). Thêm §7 "Test method + tool routing" note mặc định + ngoại lệ.

### Pattern 7 — Bảng 1 + Bảng 2 (snapshot TC × status + TC chưa chạy được) thiếu trong test-plan baseline

- **Module hit:** fr-05-vu-viec, fr-13-tv-nhanh, fr-11-bao-cao, fr-04-chuyen-gia-tvv (mọi review nhắc)
- **Mô tả gap:** CLAUDE.md "Functional/Workflow report — 2 bảng tổng hợp BẮT BUỘC sau mỗi round (enforced 2026-05-10)" yêu cầu mọi report có Bảng 1 (snapshot toàn bộ TC × status) + Bảng 2 (TC non-PASS × nguyên nhân nhóm A-F × phương án). Test plan chưa link template `output/template/test-case-execution-report-template.md`.
- **Action chung Phase 3:** Thêm reference link template + ghi chú "Round 1 execute BẮT BUỘC add 2 bảng vào functional-test-report-r{N}.md". Test-plan baseline có thể chỉ link template trống.

---

## BA-Q tracker cross-module

| BA-Q ID | Module block | Câu hỏi | TC block | Priority |
|---|---|---|---|:-:|
| BA-Q-FR11-001 | fr-11-bao-cao | Format export final: DOCX (v3) vs PDF (v3.5) — TT17/2025 yêu cầu? | TC-FR11-EXPORT-02/03 | High |
| BA-Q-FR11-002 | fr-11-bao-cao | BR-DATA-06 limit: 50K (SRS line 1088) vs 10K (SRS line 1258) | TC-FR11-EXPORT-04 | High |
| BA-Q-FR11-003 | fr-11-bao-cao | FR-IX-08 contradiction: Inputs bỏ `dia_ban_id`, Output vẫn `theo_dia_ban[]` | TC-FR11-IX08-01 | High |
| BA-Q-FR16-001 | fr-16-api | LGSP message envelope format cho 8 endpoint inbound | TC-IN-01..08 (BLOCKED) | High |
| BA-Q-FR16-002 | fr-16-api | HMAC signature algorithm + sample key cấp cho QA | TC-AUTH-* | High |
| BA-Q-FR16-003 | fr-16-api | FR-XII-13 metadata-only — `tu_lieu_pl_lien_ket[]` có expose hay không? | TC-OUT-TVCS-03 | Med |
| BA-Q-FR16-004 | fr-16-api | Rate limit scope: per-consumer vs per-endpoint-per-consumer | TC-RATE-03/04 | Med |
| BA-Q-FR05-001 | fr-05-vu-viec | BR-DATA-01 soft-delete vs C1 cross-cutting hard-delete cho VU_VIEC | TC25 data migration | High |
| BA-Q-FR05-002 | fr-05-vu-viec | BR-AUTH-10 source chính cho FR-05 (SRS update CHANGELOG ghi OUT) | TC-PERM-AUTH-10 | High |
| BA-Q-FR13-001 | fr-13-tv-nhanh | Enum `kenh_tu_van` final: `NHANH/THU_CONG` (line 719) vs `TV_NHANH/TV_THU_CONG` (line 262) | TC-TVN-API-005 | High |
| BA-Q-FR13-002 | fr-13-tv-nhanh | State `NHAP` cho KHO_CAU_HOI: line 103 có / CHECK constraint line 697 không | SM-KHOCAUHOI | High |
| BA-Q-FR13-003 | fr-13-tv-nhanh | Transition "Đẩy Nhóm II → HOAN_THANH" có trong SRS chính thức không? | SM-TVNHANH | Med |
| BA-Q-FR09-001 | fr-09-bieu-mau | BR-PUBLIC-02 atomic rollback khi Cổng PLQG fail (3 action) | BM-CR-008 | High |
| BA-Q-FR09-002 | fr-09-bieu-mau | `loai_hinh` field: enum CHECK 4 giá trị vs form free-text | TC verify dropdown | Med |
| BA-Q-FR09-003 | fr-09-bieu-mau | Version control entity BIEU_MAU_VERSION có/không? | REG-006 | Med |
| BA-Q-FR06-001 | fr-06-chi-tra | TVV permission Read HSCT (BR-AUTH gắn TVV) — SRS line cụ thể | TC-PERM-07 | High |
| BA-Q-FR06-002 | fr-06-chi-tra | Hard-delete HSCT trigger: admin script hay UC user-facing? | TC-CR-01 | Med |
| BA-Q-FR04-001 | fr-04-chuyen-gia-tvv | Migration `loai_tvv='NHT'` record cũ — UI behavior | SPEC-MIGRATION-IV-01 | High |
| BA-Q-FR04-002 | fr-04-chuyen-gia-tvv | SRS ref FR-VIII-26 không tồn tại — chính xác là FR-VIII-15? | §1.2 + §2.5 SM | High |
| BA-Q-SLA-001 | fr-05-vu-viec | NĐ55 Đ.8 K.1 SLA 15 ngày — web-verify chưa có | BR-SLA-01 | Med |

**Tổng:** ≥20 BA-Q ambiguity cần BA confirm trước Round 1 execute. Đặc biệt 12 BA-Q High priority gate TC P0.

---

## Env infra blocker (cần Infra/DBA provision trước Round 1)

| Blocker | Module impact | TC block | Owner |
|---|---|:-:|:-:|
| mTLS sandbox Cổng PLQG + client cert + signature key cho QA | fr-16-api | 8 TC inbound + 31 TC outbound | Infra |
| LGSP sandbox endpoint `POST /api/v1/vu-viec` cho inbound test | fr-16-api | 8 TC inbound | Dev BE |
| Mock LGSP `POST /api/v1/lgsp/chi-tra/inbound` cho HSCT test | fr-06-chi-tra | TC-API-01..06 | Dev BE / QA API |
| Mock Cổng PLQG outbound endpoint cho BR-PUBLIC-04 verify | fr-05-vu-viec, fr-09-bieu-mau, fr-13-tv-nhanh | TC-CK-02..03 + BR-PUBLIC test | Dev BE |
| VNeID sandbox NĐ69/2024 cho DN role login | fr-05-vu-viec (DN UC67 chấm điểm), fr-07-doanh-nghiep | TC-PERM DN role | Infra |
| Endpoint admin query `GET /api/admin/audit-log` (hoặc DB read AUDIT_LOG) | fr-16-api, fr-06-chi-tra, fr-05-vu-viec | Mọi TC-AUDIT verify | Dev BE / DBA |
| Endpoint chuyên trang `/chuyen-trang` cho 5 trường công khai render | fr-09-bieu-mau, fr-13-tv-nhanh, fr-12-tv-chuyen-sau | BM-CR-009, TC-CK-* | Dev FE |
| ClamAV ASYNC scan post-commit hook | fr-09-bieu-mau (BM-009 virus scan) | TC virus + MIME spoof | Dev BE / Infra |

---

## Module có ≥5 cross-module dep upstream

| Module | Số dep upstream | Module upstream chính | Risk khi upstream chưa seed |
|---|:-:|---|---|
| fr-11-bao-cao | 8 module | FR-02, 03, 04, 05, 06, 07, 08, 15 | Mọi báo cáo trống → 23 loại không verify được |
| fr-01-dashboard | 8 module | FR-02, 03, 04, 05, 06, 07, 08, 14 | 9 KPI + 2 chart show 0 → không verify formula |
| fr-16-api | 9 module | FR-02, 03, 04, 05, 06, 07, 08, 09, 12 | 9 outbound endpoint trả data=[] → không verify state filter |
| fr-06-chi-tra | 3 module | FR-05 (VV HOAN_THANH), FR-14 (HĐ), FR-07 (DN quy_mo) | LGSP inbound reject → 0 HSCT để test workflow |
| fr-08-danh-gia-hq | 2 module + DG | FR-05 (VV danh giá), FR-10 (KE_HOACH_DG) | 0 DOT_DG → tab 1-4 trống |
| fr-13-tv-nhanh | 2 module | FR-02 (HOI_DAP auto-feed), FR-12 (Đẩy Nhóm II) | KHO_CAU_HOI trống + bridge sang Nhóm II không test được |
| fr-14-hop-dong-tv | 2 module | FR-04 (TVV/CG), FR-05 (VV) | Dropdown TVV/CG trống → không tạo HĐ |
| fr-05-vu-viec | 4 module | FR-10, FR-07, FR-04, FR-09 | LV/DN/TVV/Biểu mẫu thiếu → không tạo VV |
| cross-cutting-permission | ALL | 18 module | Cần data tối thiểu mọi entity để test 11 role × 49 entity matrix |

---

## Hành động đề xuất trước Round 1 execute

1. **BA confirm ≥20 BA-Q ambiguity** (xem BA-Q tracker trên) — đặc biệt 12 BA-Q High priority. Deadline đề xuất 2026-05-19.
2. **Infra provision env blocker** — mTLS sandbox + VNeID sandbox + Mock LGSP + Mock Cổng PLQG outbound. Không có 4 mock này = 50+ TC nhóm D BLOCKED.
3. **Seed presets theo Phụ lục 2 flow-module.md** — review entity-map.md cột "Đọc tại" cho mỗi module. Apply rule "≥1 record per filter coverage downstream", KHÔNG theo count tổng.
4. **Permission matrix update cho 5 entity v3.5 mới** — TO_CHUC_TU_VAN approval workflow (FR-04), NHT lifecycle riêng (FR-04), KE_HOACH_DG rename từ DOT_DANH_GIA (FR-08), Kho QA state machine (FR-13), HO_SO_CHI_TRA DN bổ sung (FR-06). Cross-cutting permission task R0.X cần update permission-matrix.md project trước.
5. **Sửa cite SRS path prefix toàn 18 test-plan** — replace short ref `:NNNN` → full `<folder>/srs-fr-XX.md:NNNN` (vi phạm pattern 3 trên).
6. **Thêm mapping table TC-ID ↔ file** cho cross-cutting TC-AUTH/PERM/AUDIT/FILTER/NOTIF trong fr-05-vu-viec + fr-16-api + fr-13-tv-nhanh (vi phạm pattern 5).

---

## Verdict distribution

| Verdict | Count | Module |
|---|:-:|---|
| APPROVE | 0/18 | — |
| REVISE | 18/18 | All — đa phần có 6-14 gap mức medium, fix trong 1 round revise |

> **Kết luận:** Toàn bộ 18 module có baseline test plan đủ structure (≥150 dòng, 6 section, cite SRS line, permission matrix, TC count ≥10) NHƯNG cần round Phase 3 revise (đã chạy) + BA sign-off 20 BA-Q + Infra provision 4 mock trước khi enter Round 1 execute thực tế.

---

*Aggregated from 18 review.md files Phase 2. Source: agent-skills:code-reviewer subagent self-review (Codex CLI fallback). 2026-05-12 22:15:00.*
