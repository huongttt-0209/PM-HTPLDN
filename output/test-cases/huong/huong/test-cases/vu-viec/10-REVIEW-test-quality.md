# Test Quality Review — FR-V.I Vụ việc TGPL (BMAD A6)

> **Ngày**: 2026-05-06 · **Reviewer**: BMAD testarch-test-review
> **Status**: ✅ **REVIEWED 2026-05-06** — 6-axis quality assessment + 1 gap-fill (TC-VV-TB-307 SLA escalate đã merge inline file 12).
> **File này KHÔNG còn là TC source** — chỉ là quality audit. Phase B B-block KHÔNG ref file này.
> **Tiêu chí**: ≥85% PASS overall (per BM model precedent 86.7%).

---

## 1. Quy ước 6-axis

| # | Trục | Định nghĩa | Trọng số |
|---|------|-----------|---------:|
| 1 | **Coverage** | BR + AC + Error codes + SM transitions cover ≥95% | 25% |
| 2 | **Specificity** | Test data cụ thể (giá trị thực, không placeholder), assertions exact (cite SRS line + match nguyên văn) | 20% |
| 3 | **Independence** | Mỗi TC standalone; nếu phụ thuộc TC khác → state explicitly trong Pre-conditions | 15% |
| 4 | **Determinism** | Reproducible: cùng input → cùng output. Tránh flake (timing race, random seed, server clock drift) | 15% |
| 5 | **A7 compliance** | UI/function-testable (KHÔNG TC chỉ-DB query / API thuần) — Plan §3.1 iron rule | 15% |
| 6 | **Spec quality** | Cite SRS line số cụ thể; SPEC-CLARIFY khi gap; phân biệt rõ STATE/UI/PERSIST | 10% |

**Pass threshold:** ≥7/10 mỗi axis hoặc ≥85% weighted average.

---

## 2. Score per file

| File | Coverage | Specificity | Independence | Determinism | A7 | Spec quality | Weighted | Status |
|------|---------:|------------:|-------------:|------------:|---:|-------------:|---------:|:------:|
| 01 — DS hồ sơ VV | 9 | 9 | 8 | 8 | 10 | 9 | **88.5%** | ✅ |
| 02 — DN gửi HS | 9 | 9 | 9 | 8 | 10 | 9 | **89.5%** | ✅ |
| 03 — Nhập thủ công | 9 | 9 | 9 | 8 | 10 | 9 | **89.5%** | ✅ |
| 04 — CMS HT khác | 8 | 8 | 9 | 9 | 10 | 8 | **86.0%** | ✅ |
| 05 — Kiểm tra HS | 9 | 9 | 8 | 7 (counter race) | 10 | 9 | **86.5%** | ✅ |
| 06 — Quản lý HS VV | 9 | 8 | 9 | 9 | 10 | 8 | **87.5%** | ✅ |
| 07 — Phân công + xác nhận | 9 | 9 | 8 (dependency) | 8 | 10 | 9 | **88.0%** | ✅ |
| 08 — Trình + PD | 9 | 9 | 9 | 8 | 10 | 9 | **89.5%** | ✅ |
| 09 — Cập nhật KQ | 9 | 9 | 9 | 9 | 10 | 9 | **90.5%** | ✅ |
| 10 — Đánh giá VV | 9 | 9 | 9 | 9 | 10 | 9 | **90.5%** | ✅ |
| 11 — Công khai VV | 10 | 9 | 9 | 8 (concurrent CK race) | 10 | 10 | **92.5%** | ✅ |
| 12 — DN bổ sung + TB | 9 | 9 | 9 | 7 (time-shift) | 10 | 9 | **86.5%** | ✅ |
| 13 — Cấu hình quy trình | 8 | 8 | 9 | 9 | 9 (versioning verify gián tiếp) | 8 | **84.5%** | ⚠️ |
| 14 — Permission matrix | 10 | 9 | 9 | 9 | 10 | 9 | **92.0%** | ✅ |

**Average overall: 88.4%** ≥ threshold 85% → **PASS** ✅

**Outlier ⚠️ file 13 (84.5%):** Coverage 8/10 do versioning testing limited (verify chỉ qua deadline UI, không inspect DB version field trực tiếp — A7 chấp nhận). Spec quality 8/10 do SCR cụ thể chưa quote (SPEC-CLARIFY-VV-NEW-01). **Acceptable** — flag for Phase B re-test khi BA confirm SCR.

---

## 3. Issue list (per axis)

### 3.1 Coverage gaps (forward A5 đã liệt kê)

| Gap | File | Forward action | Status |
|-----|------|---------------|--------|
| BR-DATA-03 verify gián tiếp | 06 (UC57) | Acceptable — audit log cover | ✅ Accept |
| BR-CALC-03 scheduled job | All | A7 LOẠI scheduled, verify badge UI gián tiếp | ✅ Accept |
| **BR-SLA-03 escalate TB theo mức** | 12 (UC64) | **Fill gap → TC-VV-TB-307 merged inline** (A6) | ✅ FIXED |
| AT-04 "Mở lại HS" placeholder | — | Defer per SPEC-CLARIFY-VV-MO-LAI | ⏸️ Defer |
| FR-V.I-12 AC2 LGSP outbound | 08 (UC62) | A7 LOẠI nhánh LGSP outbound; verify WRN-TB-02 indirect | ✅ Accept |
| ERR-FILE-01..03 (UC55 API) | 04 | A7 LOẠI; verify file constraint UI qua TC khác | ✅ Accept |

### 3.2 Specificity issues

| Issue | File | TC ID | Note |
|-------|------|-------|------|
| Test data placeholder "≥3 VV" thay cho mã VV cụ thể | 01, 04 | TC-VV-DS-101, TC-VV-HK-101 | Acceptable — Phase B B-Seed sẽ tạo bằng MCP với mã thực tế |
| File path placeholder "mau-15mb.docx" | 06, 11 | TC-VV-QL-304, TC-VV-CK-* | Phase B B-Seed sẽ chuẩn bị file thật trong test data folder |
| Boundary message "SRS Gap" không quote nguyên văn | Multiple | Boundary TC | SPEC-CLARIFY backlog (~10 entries) — gửi BA |

### 3.3 Independence issues

| Issue | File | TC ID dependency | Mitigation |
|-------|------|------------------|-----------|
| TC-VV-NH-303 (concurrent SEQ race) phụ thuộc TC-VV-NH-301 (modal tạo DN) | 03 | Parent: TC-VV-NH-301 | Pre-conditions explicit "DN MST=1234567890 đã tồn tại" |
| TC-VV-PC-* (phân công) phụ thuộc TC-VV-KT-102 (kiểm tra DAT) | 07 | Parent: file 05 | Pre-conditions explicit "VV ở DA_PHAN_CONG" |
| TC-VV-PD-* (PD) phụ thuộc TC-VV-PC-* + TC-VV-KQ-* | 08 | Parent: file 07 + 09 | Pre-conditions explicit "VV ở CHO_PHE_DUYET có KQ NHT" |
| TC-VV-CK-103, TC-VV-CK-303 phụ thuộc CK lần 1 | 11 | Parent: TC-VV-CK-101 | Pre-conditions explicit |
| TC-VV-DG-* phụ thuộc TC-VV-KQ-* | 10 | Parent: file 09 | Pre-conditions explicit "VV ở HOAN_THANH" |

**Conclusion:** Dependency chain chấp nhận được vì SM-VUVIEC linear (15 transitions). Phase B B-Seed pre-create VV ở mỗi state để execute parallel.

### 3.4 Determinism issues

| Issue | File | TC ID | Risk | Mitigation |
|-------|------|-------|------|-----------|
| Counter race khi 2 CB NV submit kiểm tra cùng VV | 05 | TC-VV-KT-303 | Optimistic lock có thể fail-open nếu BE thiếu version field | Verify BE optimistic lock per VV.version trong Phase B |
| Time-shift dependency cho BR-EC-16 + BR-SLA-* | 05, 12 | TC-VV-KT-304, TC-VV-BS-*, TC-VV-TB-307 | Phụ thuộc QTHT cấu hình hoặc admin override system clock | **SPEC-CLARIFY-VV-A6-01**: Phase B verify endpoint admin trigger scheduled job (hoặc fallback seed VV ngày lùi sẵn) |
| Concurrent CK ⟷ Hủy CK race | 11 | TC-VV-CK-307 (A4) | Optimistic lock per CONG_KHAI/HUY_CONG_KHAI hay per VU_VIEC.version | **SPEC-CLARIFY-VV-A4-03**: implementation detail BA confirm |
| Email delivery race (deep-link click trước/sau token expire) | 12 | TC-VV-TB-306 (A4) | VNeID OAuth state lifetime / cookie session | **SPEC-CLARIFY-VV-A4-04**: implementation detail |

### 3.5 A7 compliance

**A7 iron rule:** KHÔNG TC chỉ-DB query / API thuần.

| Check | Result | Evidence |
|-------|:------:|----------|
| Có TC require "verify DB row in table X"? | ❌ NO | Tất cả assertions qua UI bridge hoặc `list_network_requests` |
| Có TC require curl/Postman? | ❌ NO | Tất cả UC trigger qua MCP click/fill_form |
| Có TC verify scheduled job trực tiếp? | ❌ NO | BR-CALC-03 + BR-SLA-* verify gián tiếp qua badge UI / time-shift |
| Có TC verify cron / queue / background worker? | ❌ NO | A7 LOẠI: UC53 LGSP API thuần + UC55 API Inbound + CROSS-01 scheduled |

**A7 score: 10/10 cho hầu hết file.** Các file 13 9/10 do versioning verify gián tiếp.

### 3.6 Spec quality

| Issue | Count |
|-------|------:|
| TC cite SRS line số cụ thể | 95% TCs (mỗi TC có 1+ srs-fr-05:line) |
| TC có SPEC-CLARIFY entry khi gap | ~30 SPEC-CLARIFY entries across 14 files |
| STATE/UI/PERSIST phân biệt rõ | 100% TCs (per template) |
| Cite BR ID đúng (BR-AUTH-01, BR-EC-15...) | 100% |

---

## 4. Quality summary

| Metric | Value |
|--------|-------|
| Total TC sau A4 + A6 | **294** (290 base + 4 A4 inline + 1 A6 inline = 295 — minus 1 misalign file 12 footer cũ) |
| TC PASS quality (≥7/10 mỗi axis) | 285 (96.9%) |
| TC PARTIAL (1 axis ≤6/10, acceptable) | 7 (gap edge cases versioning, time-shift) |
| TC REJECT (≥2 axis ≤6/10) | 0 |
| Average weighted score | **88.4%** |
| Pass threshold ≥85% | **PASS** ✅ |

---

## 5. SPEC-CLARIFY backlog (consolidated)

| ID | Source | Nội dung | Owner |
|----|--------|----------|-------|
| VV-PERM-01 | 14 | CSV thiếu user CB_NV_BN/DP và CB_PD_BN/DP | BA + DevOps seed |
| VV-NEW-01 | 13 | SCR cấu hình quy trình QTHT — URL cụ thể | BA |
| VV-NEW-02 | 13 | Versioning mechanism — process_version snapshot vs FK + audit version | BA + Backend |
| VV-NEW-03 | 13 | Message reject xóa bước active | BA |
| VV-NEW-04 | 13 | Concurrent test cần seed thêm `qtht_02` | DevOps seed |
| VV-MO-LAI | 09 (trace) | UC mở lại HS placeholder FR-V.I-xx | BA formal |
| VV-DS-01 | 01 | Boundary message search > 200 ký tự | BA |
| VV-DS-02 | 01 | Deep-link query params filter | BA + Frontend |
| VV-DN-01..10 | 02 | Multiple gaps (Tìm DN nút, kenh default, BR-CALC-04 weight, ...) | BA |
| VV-NH-01..08 | 03 | UC54 mâu thuẫn kenh DVC (srs-fr-05:316 vs SCR srs-fr-05:1733), boundary message, SEQ generation strategy | BA |
| VV-HK-01 | 04 | Deep-link query params CMS HT khác | BA + Frontend |
| VV-KT-01..04 | 05 | Boundary message ly_do, UX counter=3, scheduled job trigger, partial checklist auto-save | BA + UX |
| VV-QL-01..05 | 06 | so_luot_tai counter HO_SO_VU_VIEC, format reject message, EICAR message, upload interrupt message, Timeline filter logic | BA |
| VV-PC-01..03 | 07 (agent) | BR-CALC-04 weight expose, business calendar VN holidays, email TC TV template | BA |
| VV-PD-01..02 | 08 (agent) | Batch HOAN_THANH eligible filter, WRN-TB-02 LGSP fallback | BA |
| VV-KQ-01..02 | 09 (agent) | file_ket_qua format policy, KQ versioning | BA |
| VV-DG-01..02 | 10 (agent) | BR-CALC-06 trigger timing FR-IV cross | BA + Backend |
| VV-CK-01..02 | 11 (agent) | mo_ta_cong_khai boundary message, thoi_gian_xu_ly đơn vị ngày LV | BA |
| VV-PUBLIC-04 | 11 | Field gửi Cổng PLQG snake_case enum vs Vietnamese label | BA + API contract |
| VV-BS-TIMEOUT | 12 (agent) | cau_hinh_sla.bo_sung_timeout cấu hình UI module | BA |
| VV-A4-01..04 | 08-REVIEW | A4 cross-cutting (holidays, browser back, concurrent CK, email Tier 2) | BA |
| VV-A6-01 | 10-REVIEW (this) | Time-shift endpoint cho QA SLA escalate test | DevOps |

**Total: ~50 SPEC-CLARIFY entries** — Phase B B-Verify gửi BA consolidate.

---

## 6. Recommendations cho Phase B

1. **B-Seed priority:** Pre-create 12 VV mỗi state SM-VUVIEC + 4 VV per cong_khai 0/1 × DA_DUYET/HOAN_THANH (4 records) + 3 VV bo_sung_count 1/2/3 + DN đủ field BR-CALC-04 (5) + DN thiếu (1) — total ~25 record seed trước khi B-Run.
2. **B-Run order:** Theo dependency chain — file 02/03 (tạo VV) → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 01 (DS verify cuối).
3. **B-Verify focus:** SPEC-CLARIFY pending (~50 entries) consolidate gửi BA 1 lần. Không log bug riêng cho mỗi SPEC-CLARIFY.
4. **Time-shift workaround:** Liên hệ DevOps cho admin endpoint trigger scheduled job thủ công, hoặc seed VV với ngay_tiep_nhan đã lùi sẵn (cheaper).
5. **Mock outbound API:** TC-VV-CK-301 (BR-EC-20 atomic) cần mock Cổng PLQG — Phase B chuẩn bị MITM proxy hoặc test stub. Cùng pattern cho TC-VV-CK-302 (4xx business reject).

---

## 7. Next step

- **A7** (UI/function-testable filter): Manual scan + log LOẠI (UC53 LGSP + UC55 API Inbound + CROSS-01 scheduled) trong `11-a7-filter-log.md`. Predict A7 LOẠI ≤ 5 TC (đã chủ động filter ở A3 prompts).
- **Close Phase A:** Update todo.md W3.2 Phase A → ✅ + plan.md §2 row 9 status update.
