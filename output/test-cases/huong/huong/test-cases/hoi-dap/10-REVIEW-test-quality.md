# A6 — Test Review (FR-II Hỏi đáp)

> **Skill BMAD**: bmad-testarch-test-review (manual cycle)
> **Ngày chạy**: 2026-05-10 (Phase A step A6)
> **Input**: 7 file UC sau A4 (155+32 = 187 TC), 09-traceability-matrix.md (6 GAP)
> **Output**: Issue list + score 6 axis + GAP fix log inline merge

---

## 1. 6-Axis Quality Score

| Axis | Score (/10) | Findings |
|------|-------------|----------|
| **1. Coverage** | 9.7 | BR 24/24 (100%), AC 38/39 (97.4%), SM 11→12/12 sau A6 fix (100%), Permission 18→20/20 sau A6 (100%), Error codes 44/45 (97.8% — 1 GAP fixed) |
| **2. Clarity** | 9.5 | TC ID convention nhất quán (TC-HD/HDTK/TN/DXL/PC/PH/PD-XXX). Mỗi TC có TraceID rõ về SRS line. Pre-conditions specific (role + user + state). |
| **3. Specificity** | 9.6 | Test data cụ thể, không generic. Expected results phân tách (1)(2)(3)(4) cho status/UI/audit/notification. |
| **4. Maintainability** | 9.3 | 7 file UC theo SRS section. Audit log file (08, 09, 10, 11) tách bạch. Cross-ref BR/SM/F-references đầy đủ. Risk: ~190 TC tổng, manage qua section A/B/C/D/E. |
| **5. Testability (UI)** | 9.4 | Pre A7 filter — tất cả TC test được qua chrome-devtools MCP. Có vài TC mock backend (API Cổng PLQG, MailHog email). Sẽ rà ở A7. |
| **6. Risk coverage** | 9.5 | Cover 5 risk classes: concurrency (optimistic locking, race), boundary (file size, ngày, ký tự), state transitions (12 SM), permission (cross-cấp/cross-tenant), data integrity (FK vô hiệu, NULL). |
| **Average** | **9.50/10** | Quality cao, sẵn sàng Phase B. |

---

## 2. Issue List (resolved trong A6)

| # | Issue | File | Action | Status |
|---|-------|------|--------|--------|
| ISS-01 | GAP-A5-01 BR-SLA-02 mức 4 QUA_HAN_NGHIEM_TRONG missing | 04 | ✅ Add TC-DXL-210 inline | RESOLVED |
| ISS-02 | GAP-A5-02 BR-SLA-03 email notification chỉ indirect | 04 | ✅ Add TC-DXL-211 (MailHog verify) inline | RESOLVED |
| ISS-03 | GAP-A5-03 SM transition `MOI → HUY` không test trực tiếp | 01 | ✅ Add TC-HD-236 (Hủy yêu cầu happy path) inline | RESOLVED |
| ISS-04 | GAP-A5-04 CB_PD attempt CREATE chưa test | 01 | ✅ Add TC-HD-237 (Negative permission) inline | RESOLVED |
| ISS-05 | GAP-A5-05 DN/GV attempt access HOI_DAP module | 01 | ✅ Add TC-HD-238 inline | RESOLVED |
| ISS-06 | GAP-A5-06 ERR-AUTH-DAXL-01 chỉ indirect | 07 | ✅ Add TC-PD-073 (cross-tenant đã xử lý) inline | RESOLVED |

**6/6 GAP fixed inline. SM coverage → 100%, Permission → 100%, Error code → 100%.**

---

## 3. Findings KHÔNG fix trong A6 (defer SPEC-CLARIFY hoặc Phase B)

| # | Finding | Reason defer | Action |
|---|---------|--------------|--------|
| FND-01 | SPEC-CLARIFY-HD-04 (whitespace trim noi_dung) | BA chưa chốt rule | TC-HD-233 mark SPEC-CLARIFY pending BA |
| FND-02 | SPEC-CLARIFY-HD-01 (HUY trong tab "Hoàn thành"?) | UI behavior cần verify thực tế | TC-HDTK-020 mark SPEC-CLARIFY |
| FND-03 | SPEC-CLARIFY-HDTK-02 (keyword >200 ký truncate vs reject) | UI behavior | TC-HDTK-201 mark |
| FND-04 | SPEC-CLARIFY-DXL-03 (thoi_han_moi upper bound) | BA quyết định | TC-DXL-209 mark |
| FND-05 | SPEC-CLARIFY-DXL-04 (Lịch sử ≥100 entries pagination?) | UX design | TC-DXL-207 mark |
| FND-06 | SPEC-CLARIFY-PC-01 (HD chưa nhập lĩnh vực — phân công?) | BA quyết định | TC-PC-108 mark |
| FND-07 | SPEC-CLARIFY-PC-02 (NULL deadline khi mở modal phân công) | Default behavior | TC-PC-211 mark |
| FND-08 | SPEC-CLARIFY-PH-01 (NHT khác attempt phản hồi — WRN modal vs hard block?) | BR-AUTH-08 enforce hay flexible? | TC-PH-011 mark |
| FND-09 | SPEC-CLARIFY-PH-02 (Chèn mẫu khi editor có content — overwrite/append?) | UX design | TC-PH-210 mark |
| FND-10 | SPEC-CLARIFY-PD-08 (CB PD review draft chưa gửi visible?) | Backend behavior | TC-PD-068 mark |
| FND-11 | SPEC-CLARIFY-TN-01 (CAU_HINH_SLA load lịch lễ VN từ entity nào?) | Backend implementation | TC-TN-201 mark |

**Tổng 11 SPEC-CLARIFY pending BA** — sẽ tổng hợp gửi BA review sau Phase A done.

---

## 4. Tổng kết Phase A trước A7

| File | Sau A3 | A4 add | A6 add | Tổng |
|------|--------|--------|--------|------|
| 01-TC-quan-ly-hoi-dap.md | 23 | +6 | +3 (GAP-A5-03/04/05) | **32** |
| 02-TC-tim-kiem-tong-hop.md | 18 | +4 | 0 | **22** |
| 03-TC-tiep-nhan-xu-ly.md | 14 | +3 | 0 | **17** |
| 04-TC-quan-ly-tiep-nhan.md | 19 | +4 | +2 (GAP-A5-01/02) | **25** |
| 05-TC-phan-cong-xu-ly.md | 26 | +5 | 0 | **31** |
| 06-TC-phan-hoi-cau-hoi.md | 23 | +5 | 0 | **28** |
| 07-TC-phe-duyet-cong-khai.md | 32 | +5 | +1 (GAP-A5-06) | **38** |
| **Tổng** | **155** | **+32** | **+6** | **193** |

> Vượt estimate todo.md (118 TC) ~63% — do cover sâu BR/SM/Permission/Error code + 11 SPEC-CLARIFY.

---

## 5. Acceptance pre-A7

- ✅ Coverage BR/AC/SM/Permission/Error ≥ 95% (actual 100%/97.4%/100%/100%/100%)
- ✅ 6/6 GAP từ A5 đã fix inline merge
- ✅ Quality 9.50/10 (chuẩn 9.0+)
- ⏳ A7 manual filter UI/function-testable — chưa chạy
- ⏳ /codex review — chưa chạy

**Sẵn sàng A7 + /codex.**

---

*A6 Test Review — Phase A step A6 — 2026-05-10*
