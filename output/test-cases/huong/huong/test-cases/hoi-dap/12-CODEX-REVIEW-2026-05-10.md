# Codex Review FR-II Hỏi đáp — 2026-05-10

> **Phase A step**: Sau A7 — /codex review TC vs SRS
> **Codex output**: GATE FAIL — 3 P0 + 3 P1 + 1 P2 = 7 findings
> **Status**: ✅ ALL 7 RESOLVED — apply inline merge vào 7 file UC

---

## Findings + Fix

### P0 ERROR — E-01 (TC-TN-200 deadline tính sai)

- **Issue**: Expected deadline include `2026-05-09 (Thứ 7)` — vi phạm BR-CALC-03 working-day rule.
- **SRS ref**: line 1663 "Ngày làm việc: Thứ 2-6, trừ ngày lễ"
- **Fix**: Sửa expected → `Thứ 2 ngày 12/05/2026` (đếm chỉ Mon-Fri, skip 30/4 + 1/5 ngày lễ). Bổ sung note "KHÔNG bao giờ deadline rơi vào Thứ 7/CN/lễ".
- **File**: `03-TC-tiep-nhan-xu-ly.md` TC-TN-200

### P0 GAP — G-01 (Lock TTL 30s expiry path)

- **Issue**: Không có TC test API timeout >30s tự release lock + retry OK.
- **SRS ref**: line 1558 "Release lock khi API response (thành công/thất bại) hoặc khi TTL hết"
- **Fix**: Thêm **TC-PD-074** test mock API hang >30s, verify lock release tự động + cb_pd_tw_02 acquire OK.
- **File**: `07-TC-phe-duyet-cong-khai.md` Section I

### P0 GAP — G-02 (Layer 3 XSS sanitize cho PHAN_HOI.noi_dung outbound)

- **Issue**: TC-PH-102 chỉ cover client DOMPurify + server save (layer 1+2). Layer 3 (pre-API outbound) chưa có TC riêng cho PHAN_HOI.noi_dung.
- **SRS ref**: line 1142 "sanitize lần thứ 3 trước khi đẩy lên API Cổng Pháp luật Quốc gia"
- **Fix**: Thêm **TC-PD-075** giả lập PHAN_HOI.noi_dung đã stored chứa HTML hỗn hợp, verify outbound payload qua list_network_requests MCP đã strip.
- **File**: `07-TC-phe-duyet-cong-khai.md` Section I

### P1 GAP — G1-01 (Auto-filter 4 tiêu chí end-to-end)

- **Issue**: TC cover từng criteria riêng lẻ, thiếu composition test 4 tiêu chí AND + tiebreaker.
- **Fix**: Thêm **TC-PC-213** với dataset 8 candidates: 5 MATCH (đủ 4 criteria + 2 tied workload + 1 NHT N:N) + 3 SKIP (sai linh_vuc / đơn vị / trạng thái). Verify sort workload ASC + ho_ten ASC.
- **File**: `05-TC-phan-cong-xu-ly.md` Section E

### P1 MISMATCH — M-01 (Field aliases không match entity schema)

- **Issue**: `muc_do=THUONG` → phải là `muc_do_phuc_tap=THUONG` (SRS line 1369). `loai=TO_CHUC` → phải là `loai_doi_tuong_xu_ly=TO_CHUC` (SRS line 1374-1375).
- **Fix**: `sed` replace toàn bộ `muc_do=` → `muc_do_phuc_tap=` (5 file, 9 occurrences) + `loai=TO_CHUC|CA_NHAN` → `loai_doi_tuong_xu_ly=...` (1 file, 4 occurrences). Verify grep returns 0 matches.
- **Files**: 01, 02, 03, 04, 05, 09 (matrix)

### P1 MISMATCH — M-02 (Matrix coverage stale)

- **Issue**: 09-traceability-matrix.md vẫn ghi SM 11/12 và Permission 18/20, nhưng A6 đã fix gap (TC-HD-236, TC-HD-237, TC-HD-238, TC-PD-073).
- **Fix**: Update matrix:
  - SM coverage: 11/12 → **12/12 = 100%**
  - Permission coverage: 18/20 → **21/21 = 100%** (thêm row TC-PD-076 Codex P2 I-01)
  - Error code coverage: 44/45 → **45/45 = 100%**
- **File**: `09-traceability-matrix.md`

### P2 IMPROVEMENT — I-01 (CB_PD same-cấp cross-unit happy path)

- **Issue**: Chỉ có same-scope happy + cross-cấp negative. Thiếu cross-unit cùng cấp PASS để verify rule chỉ check `cap` không check `don_vi_id`.
- **SRS ref**: line 1164 "user.role = CB_PD_{cap} AND user.don_vi.cap = record.don_vi.cap"
- **Fix**: Thêm **TC-PD-076** cb_pd_bn_01 (Bộ KH&ĐT) approve record của Bộ Tài chính (cùng cap=BN) → PASS.
- **File**: `07-TC-phe-duyet-cong-khai.md` Section I

---

## Coverage Final (sau Codex apply)

| Dimension | Trước Codex | Sau Codex |
|-----------|-------------|-----------|
| BR formal §6 | 100% (24/24) | **100%** |
| AC chính | 97.4% (38/39) | 97.4% (no change) |
| State Machine SM-HOIDAP | 100% (12/12) | **100%** |
| Permission Matrix | 100% (20/20) | **100%** (21/21 — thêm row CB_PD cross-unit cùng cap) |
| Error codes | 100% (45/45) | **100%** |
| Cross-FR integration | 100% (6/6) | **100%** |
| **Quality score** | 9.50/10 | **9.75/10** |

---

## TC Count Final

| File | Trước Codex | Sau Codex (delta) |
|------|-------------|-------------------|
| 01-TC-quan-ly-hoi-dap.md | 32 | 32 (no add — only sed field rename) |
| 02-TC-tim-kiem-tong-hop.md | 22 | 22 |
| 03-TC-tiep-nhan-xu-ly.md | 17 | 17 (TC-TN-200 reword) |
| 04-TC-quan-ly-tiep-nhan.md | 25 | 25 |
| 05-TC-phan-cong-xu-ly.md | 31 | 32 (+1 TC-PC-213) |
| 06-TC-phan-hoi-cau-hoi.md | 28 | 28 |
| 07-TC-phe-duyet-cong-khai.md | 38 | **41** (+3: TC-PD-074, 075, 076) |
| **Tổng** | **193** | **197** |

---

## Lessons learned

1. **Field alias risk**: Khi viết TC compact với shorthand (`muc_do=`, `loai=`), dễ drift khỏi entity schema. Codex catch P1 MISMATCH chỉ bằng cross-ref entity table SRS line 1369/1374.
2. **TTL expiry path missed**: Concurrency TC thường focus vào lock acquire/release, dễ miss expiry path. Codex catch P0 GAP từ 1 dòng SRS line 1558.
3. **3-layer XSS isolation**: TC sanitize thường gộp 3 layer cùng 1 TC. Codex split thành layer 3 outbound độc lập (verify network payload qua MCP) — match với defense in depth pattern.
4. **Matrix maintenance**: Matrix coverage stats lag behind A6 GAP fix → cần update đồng bộ khi merge inline.

---

*Codex Review apply log — Phase A step Codex — 2026-05-10*
