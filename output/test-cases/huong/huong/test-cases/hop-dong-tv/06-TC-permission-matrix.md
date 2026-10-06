# Test Cases — FR-14 Permission Matrix (cross-FR-X.3-01/02)

> **SRS Ref**: FR-X.3-01 (BR-AUTH-01), FR-X.3-02 (BR-AUTH-01 + BR-AUTH-08), Phụ lục B Permission Matrix
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: HĐ TV CRUD chỉ CB NV. CB PD chỉ Read. QTHT chỉ Read (verify HT). Role nghiệp vụ ngoài (NHT/TVV/CG/DN/GV) chặn 403 toàn module.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `Permission FR-14 / {role}`
- **Pre-conditions mặc định**: Mọi role test login bằng tài khoản tương ứng từ users.csv. Có ≥1 HĐ HDTV-test-01 thuộc TW + 1 HĐ HDTV-AG-01 thuộc AG.

---

## Permission Matrix tham chiếu

| Entity / Action | QTHT | CB_NV TW | CB_NV BN | CB_NV DP | CB_PD TW/BN/DP | NHT/TVV/CG/DN/GV |
|-----------------|------|----------|----------|----------|-----------------|---------------------|
| Xem danh sách HĐ | 👁️ | 👁️ | 👁️ scope BN | 👁️ scope DP | 👁️ | ❌ |
| CRUD HĐ | ❌ | ✅ | ✅ scope BN | ✅ scope DP | ❌ | ❌ |
| Mốc / Thanh toán / Liên kết VV | ❌ | ✅ | ✅ scope BN | ✅ scope DP | ❌ | ❌ |
| Tìm kiếm | 👁️ | 👁️ | 👁️ scope BN | 👁️ scope DP | 👁️ | ❌ |
| Xuất Excel | ❌ | ✅ | ✅ | ✅ | SPEC-CLARIFY-HDTV-01 | ❌ |

---

## A. PERMISSION — HAPPY (đúng quyền)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-001 | Permission / CB_NV_TW | CB_NV_TW thấy + CRUD HĐ scope toàn TW | cb_nv_tw_01 login. | — | 1. Truy cập HĐ TV. 2. Thấy nút [+ Thêm], [Sửa], [Xóa], [Xuất Excel]. 3. Tạo HĐ mới. | (1) Thấy đầy đủ action button. (2) Tạo HĐ thành công (don_vi_id=TW). | Happy 🔴 |
| TC-PERM-002 | Permission / CB_PD_TW Read | CB_PD_TW chỉ xem + tìm kiếm | cb_pd_tw_01 login. | — | 1. Truy cập HĐ TV. 2. Xem danh sách. 3. Tìm kiếm. 4. Click [+ Thêm hợp đồng]. | (1) Thấy danh sách + thanh lọc. (2) Tìm kiếm OK. (3) Nút [+ Thêm] / [Sửa] / [Xóa] **KHÔNG hiển thị** hoặc disabled. | Happy 🔴 |
| TC-PERM-003 | Permission / QTHT Read | QTHT chỉ Read verify | qtht_01 login. | — | 1. Truy cập HĐ TV. 2. Cố click [+ Thêm]. | (1) Read được danh sách (verify HT). (2) Action CRUD bị disabled hoặc trả 403 nếu force. **SPEC-CLARIFY**: QTHT có thấy menu HĐ trên sidebar không? | Happy 🟡 |

---

## B. PERMISSION — NEGATIVE (chặn)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-010 | Permission / NHT block | NHT bị chặn 403 | nht_01 login. | — | 1. Truy cập URL `/hop-dong-tv` trực tiếp. | (1) 403 Forbidden / redirect "Không có quyền truy cập". (2) Menu sidebar không có HĐ TV. | Negative 🔴 |
| TC-PERM-011 | Permission / TVV block | TVV bị chặn (HĐ là dữ liệu nội bộ CMS) | tvv_01 login. | — | 1. Truy cập URL `/hop-dong-tv`. | (1) 403 / redirect. | Negative 🔴 |
| TC-PERM-012 | Permission / CG block | CG bị chặn | cg_01 login. | — | 1. Truy cập URL `/hop-dong-tv`. | (1) 403 / redirect. | Negative 🔴 |
| TC-PERM-013 | Permission / DN block | DN bị chặn (chỉ CMS, không Cổng) | dn_01 login (Cổng / CMS DN). | — | 1. Cố truy cập module HĐ. | (1) 403 / no menu. (HĐ KHÔNG có ngoài Cổng PLQG, business §9 line 152). | Negative 🔴 |
| TC-PERM-014 | Permission / CB_PD CRUD block | CB_PD KHÔNG được CRUD (force POST) | cb_pd_tw_01 login. | Force POST `/hop-dong-tv` | 1. DevTools / API call POST tạo HĐ. | (1) 403 Forbidden. (2) Audit log không có INSERT. | Negative 🔴 |
| TC-PERM-015 | Permission / cross-tenant scope | cb_nv_dp_01 (AG) cố Sửa/Xóa HĐ thuộc TW | cb_nv_dp_01 login. HDTV-test-01 thuộc TW. | Force GET HDTV-test-01 detail | 1. Direct URL `/hop-dong-tv/{id}` của HĐ TW. | (1) 404 hoặc 403 (BR-AUTH-08 — không thấy HĐ ngoài đơn vị). (2) IDOR block. | Negative 🔴 |

---

## C. PERMISSION — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-020 | Permission / GV block (A4 merged) | GV (Giảng viên) bị chặn | gv_01 login (nếu role tồn tại). | — | 1. URL `/hop-dong-tv`. | (1) 403 / no menu. HĐ TV không liên quan đào tạo. | Edge 🔴 |
| TC-PERM-021 | Permission / cross-DP scope (A4 merged) | cb_nv_dp_01 (AG) cố search HĐ thuộc BG → KHÔNG thấy | cb_nv_dp_01 (AG) login. HDTV-BG-01 thuộc BG. | keyword="BG" | 1. Filter keyword "BG". | (1) KHÔNG hiển thị HDTV-BG-01 (BR-AUTH-08 — DP horizontal isolation). (2) Mặc dù keyword match, scope filter loại trước. | Edge 🔴 |
| TC-PERM-022 | Permission / NHT search via embedded (A4 merged) | NHT cố access HĐ qua embedded drawer chi tiết VV (FR-05) | nht_01 login. NHT có quyền xem VV mình hỗ trợ → mở drawer "HĐ liên kết". | — | 1. Vào FR-05 chi tiết VV (NHT có quyền). 2. Mở accordion "HĐ tư vấn liên kết". | (1) Accordion ẩn hoặc hiển thị empty (NHT không có quyền HĐ). (2) Click drill-down → 403. | Edge 🟡 |
| TC-PERM-023 | Permission / CB_NV_BN CRUD scoped (Codex P1-2) | CB_NV_BN CRUD HĐ scope BN | cb_nv_bn_01 (Bộ KH&ĐT) login. | ten_hd="Tư vấn BN", gia_tri=20tr, ngày BĐ/KT hợp lệ | 1. Tạo HĐ mới. 2. Verify ben_a auto = "Bộ KH&ĐT" (đơn vị BN). 3. List HĐ. | (1) HĐ tạo OK với don_vi_id=BN. (2) Danh sách chỉ list HĐ của BN (BR-AUTH-08). (3) KHÔNG thấy HĐ TW + DP. | Edge 🔴 |
| TC-PERM-024 | Permission / CB_PD_BN read+search (Codex P1-2) | CB_PD_BN scope BN — read + search only | cb_pd_bn_01 login. HĐ thuộc BN + HĐ thuộc TW. | keyword="" | 1. Vào HĐ TV. 2. List + tìm kiếm. 3. Click [+ Thêm hợp đồng]. | (1) Chỉ list HĐ BN (BR-AUTH-08). (2) Tìm kiếm OK. (3) Nút CRUD hidden/disabled. | Edge 🟡 |
| TC-PERM-025 | Permission / CB_PD_DP read+search (Codex P1-2) | CB_PD_DP scope DP | cb_pd_dp_01 (Sở TP AG) login. | keyword="" | 1. List HĐ + search. | (1) Chỉ list HĐ AG. (2) KHÔNG thấy HĐ DP khác (BG) hoặc TW. (3) Read-only (no CRUD). | Edge 🟡 |
| TC-PERM-026 | Permission / CB_PD Excel block (Codex P1-3, SRS §2 line 129 chỉ CB NV) | CB_PD KHÔNG được Xuất Excel HĐ | cb_pd_tw_01 login. | — | 1. Vào HĐ. 2. Xem toolbar có nút [Xuất Excel] không. 3. Force GET endpoint export qua DevTools. | (1) Nút [Xuất Excel] **hidden** trên toolbar (Processing Excel step 1 SRS line 129 quote "Kiểm tra quyền CB NV"). (2) Force GET → 403 Forbidden. | Edge 🔴 |

---

## Tổng kết file 06-TC

- **Tổng số TC: 16** (3 Happy + 6 Negative + 7 Edge — A4 +3, Codex +4)
- **Critical TC (🔴)**: TC-PERM-001, 002, 010..015, 020, 021, 023, 026
- **A4 merged 2026-05-10**: TC-PERM-020, 021, 022
- **Codex 2026-05-10 patches**: +TC-PERM-023 (CB_NV_BN scope), +TC-PERM-024 (CB_PD_BN), +TC-PERM-025 (CB_PD_DP), +TC-PERM-026 (CB_PD Excel block — SRS §2 line 129 chỉ CB NV). SPEC-CLARIFY-HDTV-01 RESOLVED (CB_PD KHÔNG có Excel — đã rõ trong SRS).

*Generated 2026-05-10 — Phase A step A3 + A4 + Codex review patch*
