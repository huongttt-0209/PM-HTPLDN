# A4 Review — Edge Case Hunter (audit log)

> **Module**: QTHT Cấu hình Hệ thống (SCR-VIII-06 + FR-VIII-29)
> **Ngày chạy**: 2026-05-08
> **Skill**: bmad-review-edge-case-hunter (manual) — tham chiếu pattern Biểu mẫu / Đào tạo / Nhật ký HT (W1.1)
> **Output**: TC mới đã merge inline vào file UC tương ứng; file này chỉ là audit log proposal + mapping.
> **Iron rule (plan §3.1):** TC mới PHẢI merge vào file UC gốc. File 08 là audit log, KHÔNG phải TC source.

---

## 1. Phương pháp

Phân tích SCR-VIII-06 (4 tab gộp) + FR-VIII-29 + permission Mô hình B Hybrid theo 8 categories edge case:

| Category | Mô tả | TC merged |
|----------|-------|-----------|
| Snapshot pattern | HS đang xử lý giữ config cũ; HS mới áp config mới | TC-CH-SLA-020/021/022, TC-CH-QT-010/011/032 |
| Concurrent edit (BR-EC-01) | 2 user sửa cùng record → optimistic lock | TC-CH-SLA-040, TC-CH-MPH-063, TC-CH-QT-030 |
| Cross-don_vi isolation (Mô hình B) | BN A vs BN B; DP A vs DP B; cấp khác nhau | TC-CH-MPH-036/037/038/067, TC-CH-PERM-010/011/012 |
| Direct API bypass (BE check) | UI auto-fill bypass + cross-cấp direct API | TC-CH-MPH-033/034/035, TC-CH-PERM-040/041/042 |
| Sanitize XSS multi-field | Không chỉ noi_dung mà cả ten_mau, mo_ta | TC-CH-MPH-004/061/065 |
| Boundary numeric/text | thoi_han 1/999, ten_mau 200/201, noi_dung 10K | TC-CH-SLA-041/042, TC-CH-MPH-005/006/064 |
| Integration / cascading | NGAY_LE ↔ BR-CALC-03 SLA; xóa ngày lễ ↔ deadline VV | TC-CH-NL-040/041 |
| Deprecation verification | FR-II-NEW-01 đã bỏ — verify Tab 2 behavior | TC-CH-PC-001/002/003 |
| Audit log delta | BR-DATA-05 verify chi_tiet old/new chính xác | TC-CH-SLA-043, TC-CH-QT-031 |
| Element gating UI | Disabled state + tooltip + read-only field | TC-CH-MPH-048/049, TC-CH-PERM-030/031/033 |
| Token expire / session | JWT expire trên tab page | TC-CH-PERM-043 |
| Import file Excel edge | Format sai, empty file, 10K boundary, invalid row | TC-CH-NL-021/022/023/024 |

---

## 2. Proposal & Reasoning chi tiết

### 2.1 Snapshot pattern (đặc thù v3.1 Tab 1 + Tab 4)

**Lý do:** SRS line 492-493 + line 1645 + line 1675 nguyên văn "Hồ sơ MỚI áp dụng cấu hình mới. Hồ sơ đang xử lý giữ deadline cũ (snapshot SLA)". Đây là invariant quan trọng — bug nhất thường thấy: dev áp config mới cho TẤT CẢ HS (kể cả đang xử lý) → mất compliance NĐ55 deadline.

**Merge mapping:**
- 01-TC-tab-sla.md Section D → TC-020 (HS cũ giữ deadline), TC-021 (HS mới áp config mới), TC-022 (race condition)
- 04-TC-tab-quy-trinh-ho-tro.md Section B → TC-010 (VV cũ giữ quy trình), TC-011 (VV mới áp), TC-032 (reload không nhảy)

### 2.2 Cross-don_vi + Mô hình B Hybrid (Tab 3 đặc thù nhất)

**Lý do:** Mô hình B có 3 cấp scope. Bug phổ biến: BE forget filter scope, FE auto-fill bypassable. Cần test:
- Direct API CREATE với pham_vi của cấp khác (ERR-MPH-04)
- Direct API UPDATE record của đơn vị khác (ERR-MPH-06)
- Direct API READ record của đơn vị khác (IDOR)
- Cross-cấp ngang (BN A vs BN B; DP A vs DP B)

**Merge mapping:**
- 03-TC-tab-mau-phan-hoi.md Section D → TC-033/034 (cross-cấp CREATE), TC-035 (immutable pham_vi), TC-036/037/038 (cross-don_vi UPDATE/DELETE), TC-067 (IDOR READ)
- 06-TC-permission-matrix.md Section B → TC-010/011/012 (cross-isolation list view)

### 2.3 BR-EC-01 Optimistic Locking

**Lý do:** Module config có nhiều QTHT (đa người dùng cao cấp). Concurrent save phổ biến. SRS không nói rõ behavior nhưng BR-EC-01 (Phụ lục B) bắt buộc.

**Merge mapping:**
- TC-CH-SLA-040 (Tab 1 SLA)
- TC-CH-MPH-063 (Tab 3 mẫu)
- TC-CH-QT-030 (Tab 4 quy trình)

### 2.4 Sanitize XSS multi-field

**Lý do:** SRS line 912 + step 4 chỉ nói sanitize `noi_dung`. Nhưng `ten_mau`, `mo_ta`, `tu_khoa` cũng là user input → vẫn cần escape. Bug phổ biến: dev chỉ sanitize 1 field, các field khác leak XSS.

**Merge mapping:**
- TC-CH-MPH-004 (XSS noi_dung happy)
- TC-CH-MPH-061 (XSS search box)
- TC-CH-MPH-065 (XSS ten_mau, mo_ta)

### 2.5 Integration NGAY_LE ↔ SLA / BR-CALC-03

**Lý do:** Mục đích chính của FR-VIII-29 là để BR-CALC-03 tính deadline trừ ngày lễ. Test e2e bắt buộc — không chỉ CRUD ngày lễ riêng.

**Merge mapping:**
- TC-CH-NL-040 (e2e SLA tính trừ ngày lễ)
- TC-CH-NL-041 (xóa ngày lễ → deadline VV cập nhật?)

### 2.6 FR-II-NEW-01 Deprecation

**Lý do:** Tab 2 spec mâu thuẫn (UI render vs FR đã bỏ). Verify thực tế behavior là quan trọng để clarify với BA.

**Merge mapping:**
- 02-TC-tab-phan-cong-deprecated.md TC-001/002/003 (verify deprecation + endpoint cũ + cross-FR replacement)

### 2.7 Token expire / session edge

**Lý do:** Module config có nhiều mật khẩu/setting. Session timeout giữa khi đang sửa → behavior không xác định nếu không test.

**Merge mapping:**
- TC-CH-PERM-043 (JWT expire khi reload)

### 2.8 Import Excel edge (Ngày lễ)

**Lý do:** AC2 nói "import file Excel". Nhưng spec không cover edge: format sai, empty file, boundary, partial fail. Phase B sẽ thấy bug nếu không test trước.

**Merge mapping:**
- TC-CH-NL-021/022/023/024 (file format / empty / 10K boundary / invalid row partial fail)

---

## 3. Tổng kết merge

| File | Base TC (A3) | A4 merged | Final |
|------|-------------:|----------:|------:|
| 01-TC-tab-sla.md | 19 | 5 | 24 |
| 02-TC-tab-phan-cong-deprecated.md | 2 | 1 | 3 |
| 03-TC-tab-mau-phan-hoi.md | 28 | 10 | 38 |
| 04-TC-tab-quy-trinh-ho-tro.md | 7 | 5 | 12 |
| 05-TC-ngay-le.md | 14 | 7 | 21 |
| 06-TC-permission-matrix.md | 15 | 4 | 19 |
| **Total** | **85** | **32** | **117** |

> Edge merge rate: 27% — cao hơn baseline 18% các module nhỏ (do module này có Mô hình B Hybrid + snapshot pattern + tích hợp BR-CALC-03).

---

## 4. Edge case xét nhưng KHÔNG merge (out of scope hoặc duplicate)

| Đề xuất | Lý do drop |
|---------|-----------|
| Verify export Excel Tab 3 mẫu phản hồi | OUT-OF-SCOPE: SCR-VIII-06 Tab 3 KHÔNG có nút Export Excel. Nếu có, phải seed 10K mẫu để test BR-DATA-06. |
| Audit log retention 5 năm cho CAU_HINH_SLA | OUT-OF-SCOPE: thuộc module Nhật ký HT (W1.1), không phải Cấu hình. |
| Performance test 1000 mẫu phản hồi load < 2s | OUT-OF-SCOPE Phase A — Phase B thực tế đo. |
| Tab 4 spec field detailed (ten_buoc / SLA per-step) | DEFER: SRS chưa cung cấp đầy đủ — đợi BA. |
| Cron job scheduled SLA crossing (FR-II-CROSS-01) | OUT-OF-SCOPE A7: cron không có UI feedback trực tiếp. |
| FR-VIII-25 Đồng bộ VNeID (line 1612 ref nhầm) | OUT-OF-SCOPE: thuộc TKPQ (W1.4), không phải Cấu hình. |
| WebSocket realtime update khi SLA đổi | OUT-OF-SCOPE: spec không yêu cầu realtime. |
| Filter Tab 3 4 trường combo (Phạm vi+Lĩnh vực+Trạng thái+Search) | DUPLICATE: TC-040..044 đã cover từng filter; combo logic giống pattern UC93. |
