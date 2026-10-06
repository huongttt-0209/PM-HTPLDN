# A4 — Edge Case Hunter Review (FR-14 Hợp đồng Tư vấn)

> **Ngày:** 2026-05-10
> **Tool:** bmad-review-edge-case-hunter (manual sweep theo SRS + business-flow + sibling pattern)
> **Status:** ✅ MERGED INLINE (theo Iron Rule plan.md §3.1)

---

## 1. Mục tiêu

Hunt edge case + concurrency + boundary + cross-FR side effect + integrity rule mà A3 base TC chưa cover.

---

## 2. Proposal → Merge mapping

| # | Edge Case | Severity | Source | File Merge | TC ID mới | Status |
|---|-----------|----------|--------|------------|-----------|--------|
| 1 | tvv_id dropdown filter `trang_thai=HOAT_DONG` | P1 | 02-thu-tu-module:649 | 01 | TC-HDTV-024 | ✅ merged |
| 2 | tvv_id loai_tvv='CG' AC#7 explicit | P1 | srs-fr-14:180 | 01 | TC-HDTV-025 | ✅ merged |
| 3 | file_dinh_kem format/size SPEC-CLARIFY | P1 | srs-fr-14:90 (gap) | 01 | TC-HDTV-026 | ✅ merged |
| 4 | Mã HĐ format `HDTV-YYYYMMDD-NNN` exact | P2 | BR-DATA-04 | 01 | TC-HDTV-027 | ✅ merged |
| 5 | Excel scope đơn vị (BR-AUTH-08) | P1 | srs-fr-14:483 | 01 | TC-HDTV-028 | ✅ merged |
| 6 | Mốc trang_thai_moc enum invalid restrict | P1 | srs-fr-14:100 | 02 | TC-MTD-022 | ✅ merged |
| 7 | Mốc JSON array order persist | P2 | srs-fr-14:382 (JSON column) | 02 | TC-MTD-023 | ✅ merged |
| 8 | Sửa gia_tri HĐ < Σ giai đoạn → reject | P0 | srs-fr-14:119 (Processing 4) | 03 | TC-TTGD-022 | ✅ merged |
| 9 | Σ = gia_tri boundary 4 GĐ | P1 | srs-fr-14:119 boundary | 03 | TC-TTGD-023 | ✅ merged |
| 10 | Progress bar tính trên DA_THANH_TOAN, không Σ tổng GĐ | P0 | srs-fr-14:289 + Outputs#9 | 03 | TC-TTGD-024 | ✅ merged |
| 11 | VV soft-delete cascade hide khỏi accordion HĐ | P0 | BR-DATA-01 + N:N integrity | 04 | TC-LVV-022 | ✅ merged |
| 12 | VV detail back-ref accordion "HĐ tư vấn liên kết" | P1 | srs-fr-14:256 (drawer truy cập từ VV) | 04 | TC-LVV-023 | ✅ merged |
| 13 | TVV detail back-ref tab "Lịch sử" → HĐ | P1 | srs-fr-14:256 + 02-thu-tu-module:624 | 04 | TC-LVV-024 | ✅ merged |
| 14 | N:N many HD per VV scope SPEC-CLARIFY | P1 | BR-AUTH-08 cross-entity | 04 | TC-LVV-025 | ✅ merged |
| 15 | Keyword full-text 3 fields (TÊN+MÃ+BÊN B) | P1 | srs-fr-14:216 + business §6 | 05 | TC-HDTK-023 | ✅ merged |
| 16 | SQL injection sanitize | P0 | NFR security | 05 | TC-HDTK-024 | ✅ merged |
| 17 | Keyword Unicode tiếng Việt có dấu | P1 | locale vi-VN | 05 | TC-HDTK-025 | ✅ merged |
| 18 | Empty keyword → trả all (scope đơn vị) | P2 | srs-fr-14:206 (keyword N optional) | 05 | TC-HDTK-026 | ✅ merged |
| 19 | GV block | P0 | Permission Matrix complete coverage | 06 | TC-PERM-020 | ✅ merged |
| 20 | Cross-DP scope (AG ↔ BG) | P0 | BR-AUTH-08 horizontal isolation | 06 | TC-PERM-021 | ✅ merged |
| 21 | NHT embedded drawer access via FR-05 | P1 | srs-fr-14:256 + permission cascade | 06 | TC-PERM-022 | ✅ merged |

**Tổng:** 21 TC mới đã merge inline vào 6 file UC (01-06).

---

## 3. Phân loại theo Priority

- **P0 critical:** 6 (TTGD-022, TTGD-024, LVV-022, HDTK-024, PERM-020, PERM-021)
- **P1 high:** 13
- **P2 medium:** 2 (HDTV-027, MTD-023, HDTK-026)

---

## 4. SPEC-CLARIFY mới phát hiện trong A4

| Code | Mô tả | Vị trí SRS | Đề xuất |
|------|-------|-----------|---------|
| HDTV-10 | Lọc TVV dropdown — TVV trạng thái CHO_PHE_DUYET có loại trừ không? | srs-fr-04 SM-TVV | Flag BA |
| HDTV-11 | Collation tiếng Việt cho keyword search (có dấu vs không dấu) | srs-fr-14:216 | Flag BA |
| HDTV-12 | VV soft-delete có cascade hide khỏi accordion HĐ hay vẫn show với badge "Đã xóa"? | BR-DATA-01 + N:N | Flag BA |
| HDTV-13 | Scope đơn vị áp lên list HĐ trong accordion VV (FR-05 detail) — TW thấy HĐ BN/DP linked với VV mình owner? | BR-AUTH-08 + N:N cross-entity | Flag BA |

---

## 5. Coverage delta

| Coverage axis | Trước A4 | Sau A4 |
|---------------|----------|--------|
| Total TC | 54 | 75 |
| Edge / boundary | 13 | 31 |
| Concurrency / race | 1 (TC-HDTV-022) | 1 |
| Cross-FR side effect | 0 | 4 (LVV-022..025, PERM-022) |
| Security / injection | 0 | 1 (HDTK-024) |
| Permission edge | 0 | 3 (PERM-020..022) |

---

*A4 done 2026-05-10 — 21 edge case merged inline. File này là audit log, KHÔNG phải TC source.*
