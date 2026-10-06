# Test Cases — Permission Matrix Cross-cutting (FR-VII-01..05 / BR-AUTH-01 + BR-AUTH-08)

> **SRS Ref**: BR-AUTH-01 (srs-fr-09:877), BR-AUTH-08 (srs-fr-09:883), Permission Matrix module-level (xem 00-test-plan-overview §2.3)
> **Ngày tạo**: 2026-05-06 (BMAD A3)
> **Pattern reference**: `output/test-cases/doanh-nghiep/06-TC-permission-matrix.md`

---

## A. ROLE-BASED ACCESS HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-PERM-001 | BR-AUTH-08 | CB_NV_TW thấy thư mục/BM thuộc TW (own scope) | `cb_nv_tw_01` đăng nhập. Seed 3 thư mục: 1 TW + 1 BN + 1 ĐP, mỗi thư mục có 2 BM. | — | 1. Vào SCR-VII-01. 2. Quan sát danh sách thư mục. 3. Vào SCR-VII-02 → quan sát danh sách BM. | **STATE**: Backend filter `WHERE don_vi_id=TW.id` (BR-AUTH-08 srs-fr-09:883). **UI**: SCR-VII-01 chỉ thấy 1 thư mục TW + 2 BM TW; KHÔNG thấy BN/ĐP. **PERSIST**: Verify `list_network_requests` thấy GET `/thu-muc?don_vi_id=TW.id` hoặc filter ngầm trong response. | Happy | P0 |
| TC-BM-PERM-002 | BR-AUTH-08 ngoại lệ | QTHT thấy tất cả thư mục/BM cross-cấp | `qtht_01` đăng nhập. Seed 3 thư mục TW+BN+ĐP. | — | 1. Vào SCR-VII-01. | **STATE**: QTHT bypass don_vi_id filter (srs-fr-09:883 ngoại lệ). **UI**: Bảng hiển thị cả 3 thư mục + 6 BM. Cột "Đơn vị" hiển thị TW/BN/ĐP. **PERSIST**: — | Happy | P0 |
| TC-BM-PERM-008 | BR-FLOW-05 / DN download flow (A4 merged) | DN tải biểu mẫu CONG_KHAI qua Cổng PLQG — verify download_url public + so_luot_tai counter | `dn_01` đăng nhập Cổng PLQG (Tier 2 SSO). BM "Mẫu HĐLĐ" cong_khai=1 (TC-BM-404 done) với so_luot_tai=0. | — | 1. DN browse danh sách BM công khai trên Cổng. 2. Click [Tải về] BM "Mẫu HĐLĐ". 3. Verify file download. 4. CB NV reload SCR-VII-02 trên app PM. | **STATE**: Cổng PLQG gọi `GET /api/v1/bieu-mau/{id}/download` với JWT → BE PM stream file (srs-fr-09:540-543). AUDIT_LOG hành động='TAI_BIEU_MAU' với actor=DN. so_luot_tai +=1. **UI Cổng**: File `mau-hd-ld.docx` download tự động. **UI App PM (CB NV)**: Cột Lượt tải tăng từ 0 → 1. **PERSIST**: Network: GET outbound từ Cổng → app PM. KHÔNG cần CB NV approve — BR-FLOW-07. | Happy | P1 |

---

## B. NEGATIVE — CROSS-DON_VI ISOLATION + ROLE BLOCK

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-PERM-003 | BR-AUTH-08 | CB_NV_TW KHÔNG sửa được thư mục của BN (cross-don_vi) | `cb_nv_tw_01` đăng nhập. Thư mục BN ID=`thu-muc-bn-001` tồn tại. | thu_muc_id=`thu-muc-bn-001` (cross-don_vi) | 1. Direct URL `/bieu-mau/thu-muc/thu-muc-bn-001/edit`. | **STATE**: Backend reject (don_vi_id mismatch, BR-AUTH-08). **UI**: HTTP 403 hoặc redirect SCR-VII-01 với toast "Bạn không có quyền truy cập tài nguyên này" (SRS Gap message → SPEC-CLARIFY-BM-10). **PERSIST**: KHÔNG có UPDATE log. | Negative | P0 |
| TC-BM-PERM-004 | BR-AUTH-08 / Permission low-priv | CB_NV_TW_03 không có quyền "Quản lý biểu mẫu" — UI ẩn nút | `cb_nv_tw_03` đăng nhập (giả định role không có quyền `BIEU_MAU.CRUD` per permission-matrix.md). | — | 1. Vào SCR-VII-01. 2. Quan sát toolbar + table action. | **STATE**: Backend role check (BR-AUTH-01 + permission-matrix). **UI**: Nút [+ Thêm thư mục] ẨN/disable. Cột Hành động chỉ có [Xem trước], không có [Sửa]/[Xóa]/[Công khai]. Tương tự SCR-VII-02 [+ Thêm biểu mẫu] ẩn. **PERSIST**: — | Negative | P0 |
| TC-BM-PERM-005 | BR-FLOW-07 | CB_PD_TW KHÔNG có nút "Phê duyệt" cho biểu mẫu (BR-FLOW-07) | `cb_pd_tw_01` đăng nhập. ≥1 thư mục NHAP có ≥1 BM. | — | 1. Vào SCR-VII-01. 2. Quan sát workflow. | **STATE**: BR-FLOW-07 nguyên văn "công khai trực tiếp, KHÔNG cần phê duyệt" (srs-fr-09:919). **UI**: CB_PD chỉ thấy view + filter, KHÔNG có nút [Phê duyệt]/[Từ chối] (KHÁC với pattern Hỏi đáp UC10/UC15). Nút [Công khai] cũng ẨN nếu role CB_PD không có permission. **PERSIST**: — | Negative | P1 |
| TC-BM-PERM-006 | BR-AUTH-01 / Tier 2 | DN không truy cập được SCR-VII-01/02/03 | `dn_01` đăng nhập (Tier 2 SSO VNeID — srs-fr-09:877). | — | 1. URL direct `http://app/bieu-mau/quan-ly`. | **STATE**: Backend reject. DN chỉ có quyền GET qua API outbound `/api/v1/bieu-mau` (UC98), KHÔNG có UI app nội bộ. **UI**: Redirect → trang Cổng PLQG hoặc 403. Sidebar/menu không có entry "Thư viện biểu mẫu" cho DN. **PERSIST**: — | Negative | P0 |
| TC-BM-PERM-007 | BR-AUTH-08 / cross-don_vi same-cấp (A4 merged) | CB_NV_BN_A KHÔNG thấy thư mục/BM của BN_B (ngang cấp BN) | `cb_nv_bn_01` (Bộ KH&ĐT) đăng nhập. Seed: TM "BN_A-folder" thuộc BKHĐT + TM "BN_B-folder" thuộc BTC (cùng cấp BN nhưng khác don_vi_id). | thu_muc_id_BN_B (Bộ Tài chính) | 1. Vào SCR-VII-01. 2. Quan sát danh sách. 3. URL direct edit TM thuộc BTC. | **STATE**: Backend filter `WHERE don_vi_id=BKHĐT.id` (BR-AUTH-08 srs-fr-09:883) — KHÔNG bypass cho ngang cấp. **UI**: SCR-VII-01 chỉ thấy TM của BKHĐT, KHÔNG thấy BTC. URL direct → 403/redirect. **PERSIST**: KHÔNG có UPDATE log. Verify isolation cấp BN ngang nhau (KHÁC cấp TW/ĐP). | Negative | P1 |
| TC-BM-PERM-009 | Permission Matrix §2.3 / CB_PD Import + Công khai chặn (Codex 2026-05-09) | CB_PD KHÔNG thấy nút [Nhập hàng loạt] + KHÔNG thấy [Công khai] (per matrix CB_PD = ❌ cho 2 action) | `cb_pd_tw_01` đăng nhập. ≥1 thư mục NHAP có ≥3 BM. | — | 1. Vào SCR-VII-01. 2. Quan sát toolbar + cột Hành động. 3. Vào SCR-VII-02. 4. Try URL direct `/bieu-mau/import` (SCR-VII-03). 5. Try URL direct trigger publish API. | **STATE**: Backend role check (BR-AUTH-01 + permission-matrix). CB_PD permission = chỉ Read (00-test-plan §2.3 row "Công khai" = ❌ cho CB_PD; row "Import" = ❌ cho CB_PD). **UI**: Toolbar SCR-VII-02 KHÔNG có nút [Nhập hàng loạt]. Dòng Hành động KHÔNG có [Công khai]/[Ẩn]. URL direct SCR-VII-03 → 403 hoặc redirect SCR-VII-01. **PERSIST**: KHÔNG có BIEU_MAU record nào tạo bằng CB_PD. | Negative | P1 |
| TC-BM-PERM-010 | BR-AUTH-01 / NHT/TVV/CG block toàn module (Codex 2026-05-09) | NHT/TVV/CG (Tier 1 nội bộ) KHÔNG truy cập module Biểu mẫu (per matrix = ❌ all action) | `nht_01` đăng nhập. (Test với `tvv_01`, `cg_01` lặp 3 lần.) | — | 1. Quan sát menu/sidebar. 2. URL direct `/bieu-mau/quan-ly` SCR-VII-01. 3. URL direct `/bieu-mau/quan-ly-bieu-mau` SCR-VII-02. 4. URL direct `/bieu-mau/import` SCR-VII-03. | **STATE**: Backend role check (BR-AUTH-01 srs-fr-09:877). 00-test-plan §2.3 row cuối "NHT/TVV/CG/DN" = ❌ all action module Biểu mẫu. **UI**: Menu/sidebar KHÔNG có entry "Thư viện biểu mẫu" cho 3 role. URL direct → 403 hoặc redirect dashboard. KHÔNG hiển thị danh sách nào. **PERSIST**: KHÔNG có UPDATE log. Verify isolation hoàn toàn 3 role nội bộ Tier 1 không có chức năng. | Negative | P0 |

---

## Tổng số TC: 10 (3 Happy + 7 Negative) — A3 base 6 + A4 merged 2 + Codex 2026-05-09 +2
**Priority**: P0=6 / P1=4 / P2=0

**Coverage:**
- BR: BR-AUTH-01 (Tier 1+2), BR-AUTH-08 (cross-don_vi cross-cấp + ngang cấp + QTHT exception), BR-FLOW-05 (DN download), BR-FLOW-07 (no PD step)
- Roles tested: QTHT (positive R), CB_NV_TW (full CRUD + low-priv `_03` UI hide), CB_NV_BN_A vs BN_B (ngang cấp), CB_PD_TW (positive Read + negative Công khai/Import), DN (negative URL direct + happy download Cổng), NHT/TVV/CG (negative all action)
- Permission Matrix §2.3 cells covered: 4 entity-action × 4 role groups = 16 cells. After Codex 2026-05-09: ~14/16 explicit + 2 implicit (QTHT bypass Công khai/Import — không có nút).
- A4 merged 2026-05-06: TC-BM-PERM-007 (ngang cấp BN_A/BN_B), TC-BM-PERM-008 (DN download Cổng PLQG)
- Codex review 2026-05-09: TC-BM-PERM-009 (CB_PD Import/Công khai block), TC-BM-PERM-010 (NHT/TVV/CG block toàn module — fill BM-CRIT-005).
- SPEC-CLARIFY: BM-10 (403 cross-don_vi message)
