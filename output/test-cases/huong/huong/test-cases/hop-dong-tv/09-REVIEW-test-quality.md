# A6 — Test Review Quality Score (FR-14 Hợp đồng Tư vấn)

> **Ngày:** 2026-05-10
> **Tool:** bmad-testarch-test-review (6-axis quality review)
> **Threshold:** ≥80% PASS

---

## 1. 6-Axis Quality Score (sau Codex review apply)

| Axis | Score | Note |
|------|-------|------|
| **1. Coverage (BR/AC/ERR/trang_thai/Permission)** | 9.8/10 | BR/AC/ERR 100%, trang_thai field 100%, Permission 100% (sau Codex P1-2/P1-3), Entity Inputs 100%. SM bỏ khỏi gate (P0-1). |
| **2. Clarity & repeatability** | 9.0/10 | TraceID rõ. Pre-conditions có user role + state cụ thể. Test data đầy đủ. |
| **3. Independence (no inter-TC dependency)** | 8.5/10 | Các TC trong cùng accordion tham chiếu HĐ "test-01" — yêu cầu B-Seed tạo HĐ trước. OK với pattern hiện hành. |
| **4. Negative depth** | 9.5/10 | 20 negative TC (24%) cover 7/7 ERR + permission block 6 role + cross-tenant + SQL injection + cascade + Excel block. |
| **5. Edge case rigor** | 9.5/10 | 44 edge TC (52%) cover boundary, concurrency (race SEQ), JSON array order, Unicode, soft-delete cascade, embedded drawer, M2M cross-entity scope, Excel filter, BN/DP scope. |
| **6. Maintainability** | 9.5/10 | Mỗi UC = 1 file. Audit log riêng (07/08/09/10) + Codex changelog inline. SPEC-CLARIFY chú thích inline với status RESOLVED/Pending BA. |

**Tổng:** 55.8/60 = **93% PASS** (≥80% threshold ✅, was 90.8% trước Codex)

---

## 2. Issue list (sorted P0/P1/P2)

| # | Severity | Issue | File | Đề xuất |
|---|----------|-------|------|---------|
| 1 | P0 | SM transition gap (4 TC missing) | 01 | ✅ A6 đã fill TC-HDTV-030..033 |
| 2 | P1 | Entity field ghi_chu chưa có TC boundary | 01 | ✅ A6 đã fill TC-HDTV-034 |
| 3 | P1 | SPEC-CLARIFY-HDTV-02 — SM transition flow ambiguous | 01 D | Quote SRS §5 + business §⑩, flag BA |
| 4 | P1 | SPEC-CLARIFY-HDTV-05 — file_dinh_kem format/size | 01 TC-HDTV-026 | Flag BA, default theo các module khác (≤20MB, .pdf/.doc/.xls) |
| 5 | P2 | Test sort/edit/delete row mốc trong table inline (UI tương tác) | 02 | A6 không fill — assume default UI behavior |
| 6 | P2 | Date picker UI (calendar) — không test riêng | 01 | Generic UI control, không cần TC riêng |

---

## 3. SPEC-CLARIFY tổng hợp (forward to Gap-report)

| Code | Mô tả | Vị trí | Severity |
|------|-------|--------|----------|
| HDTV-01 | CB_PD có Xuất Excel HĐ không? | srs-fr-14:174,195 | P1 |
| HDTV-02 | SM-HOPDONG có flow transition thực hay free-edit? | srs-fr-14:446-452 | P0 |
| HDTV-03 | Excel template columns chính thức? | srs-fr-14:132 (GAP-X.3-02) | P1 |
| HDTV-04 | Tìm kiếm theo TVV/khoảng ngày (`[GAP-X.3-03]`) | srs-fr-14:246-248 | P1 |
| HDTV-05 | file_dinh_kem định dạng + dung lượng + số lượng max? | srs-fr-14:90 | P1 |
| HDTV-06 | UI sort/edit/delete row JSON array (Mốc + Thanh toán) | srs-fr-14:382-383 + business §2 | P2 |
| HDTV-07 | Bỏ liên kết VV có audit log riêng? | business §3 G4 | P2 |
| HDTV-08 | "Thời hạn KT đỏ ≤30 ngày" — countdown realtime hay snapshot? | srs-fr-14:276 | P2 |
| HDTV-09 | Dropdown TVV filter loai_tvv/trang_thai chính xác? | srs-fr-14:180 + 02-thu-tu-module:649 | P1 |
| HDTV-10 | TVV trạng thái CHO_PHE_DUYET có loại trừ trong dropdown? | srs-fr-04 SM-TVV | P2 |
| HDTV-11 | Collation tiếng Việt cho keyword search? | srs-fr-14:216 | P2 |
| HDTV-12 | VV soft-delete cascade hide khỏi accordion HĐ? | BR-DATA-01 + N:N | P1 |
| HDTV-13 | Scope đơn vị áp lên list HĐ trong accordion VV cross-FR? | BR-AUTH-08 + N:N | P1 |
| HDTV-14 (A6 mới) | ghi_chu / noi_dung max length | srs-fr-14:89 | P2 |

**Tổng SPEC-CLARIFY:** 14 (3 P0, 7 P1, 4 P2)

---

## 4. Coverage delta sau A6

| Axis | Trước A6 | Sau A6 |
|------|----------|--------|
| Total TC | 75 | 80 |
| BR | 100% | 100% |
| AC | 100% | 100% |
| ERR | 100% | 100% |
| SM transition | 20% | 100% (5/5) |
| Permission | 91.7% | 91.7% |
| Entity field | 91.7% | 100% (sau ghi_chu fill) |

---

## 5. A7 forward (UI/function-testable filter)

Toàn bộ 85 TC (sau Codex) đều UI/function-testable. KHÔNG có TC API thuần (HĐ TV không có API outbound — business §9 quote "không nằm trong 18 API FR-16"). A7: 0 LOẠI confirmed.

---

## 6. Codex Review Changelog (2026-05-10)

**GATE before Codex:** ⚠️ FAIL (2 P0 + 5 P1 + 5 P2 findings)
**GATE after apply:** ✅ PASS

### P0 (must fix) — 2/2 RESOLVED

| # | Finding | Action | TC affected |
|---|---------|--------|-------------|
| P0-1 | TC SM transition contradicts SRS §5 (line 450-452 nói "không có SM, chỉ status field") | Đổi "SM transition" → "trang_thai field free-edit" + bỏ SM khỏi gate axis | TC-HDTV-030..033 (rewritten); 00 §2.4; 08 §4; 09 §1 |
| P0-2 | `DANG_HOAT_DONG` không có trong SRS enum (SRS line 401: `HOAT_DONG`) | Replace toàn bộ data | TC-HDTV-024, 025; 00 §2.5; 07 row#1 |

### P1 (should fix) — 5/5 RESOLVED

| # | Finding | Action | TC affected |
|---|---------|--------|-------------|
| P1-1 | Excel filter non-empty chưa test | +TC-HDTV-029 (TVV+ngày filter → Excel scope match) | 01 |
| P1-2 | Permission matrix thiếu CB_NV_BN CRUD + CB_PD BN/DP read | +TC-PERM-023 (BN CRUD), +TC-PERM-024 (CB_PD BN), +TC-PERM-025 (CB_PD DP) | 06 |
| P1-3 | CB_PD Excel SPEC-CLARIFY ambiguous → SRS line 129 đã rõ "Kiểm tra quyền CB NV" | +TC-PERM-026 (CB_PD block Excel); RESOLVE SPEC-CLARIFY-HDTV-01 | 06; 00 §2.3 |
| P1-4 | Entity field `so_hop_dong`, `ngay_ky` (line 373, 378) không có TC | Excluded as OBS HDTV-17 (form không có field này) | 00 §6; 08 §6 |
| P1-5 | CHECK constraint `IS JSON` (line 388-389) không UI testable | Excluded as OBS HDTV-18 (DB-level, không UI) | 00 §6 |

### P2 (nice to fix) — 5/5 noted as OBS

| # | Finding | Action |
|---|---------|--------|
| P2-1 | QTHT read HĐ — SRS không grant rõ | OBS HDTV-16, mark trong matrix |
| P2-2 | file_dinh_kem format/size SRS silent | SPEC-CLARIFY-HDTV-05 (đã có) |
| P2-3 | so_tien `> 0` SRS không có ERR riêng | OBS HDTV-15 |
| P2-4 | Search ngày SRS ambiguous (field nào) | SPEC-CLARIFY-HDTV-04 (đã có) |
| P2-5 | VV soft-delete cascade behavior SRS silent | SPEC-CLARIFY-HDTV-12 (đã có) |

### Coverage delta

| Axis | Before Codex | After Codex |
|------|-------------:|------------:|
| Total TC | 80 | 85 (+5) |
| Permission Matrix | 91.7% (12 cells) | 100% (16 cells) |
| Entity Inputs | 91.7% | 100% |
| trang_thai field (replace SM) | 100% (1/5 SM) | 100% (4/4 enum) |
| Quality score | 90.8% | 93% |

---

*A6 done 2026-05-10 + Codex review apply. Final 85 TC. Quality 93% PASS.*
