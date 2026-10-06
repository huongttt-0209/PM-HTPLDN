# Test Cases — Permission Matrix cross-FR-XI GĐ1

> **SRS Ref**: BR-AUTH-01, BR-AUTH-05, BR-AUTH-08, FR-XI-01..FR-XI-05a
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: Cross-cutting permission test. Dùng TK `_03` (permission test dedicated) hoặc fallback `_02`.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **Pre-conditions mặc định**: Test với TK isolation (xem `input/test-accounts-isolation.csv`)

---

## Permission Matrix recap

| Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | NHT/TVV/CG/DN |
|--------|------|------------------|-------------------|---------------|
| CT — CRUD (DU_THAO) | 👁️ R | ✅ scope | 👁️ R | ❌ |
| CT — Trình PD | ❌ | ✅ | ❌ | ❌ |
| CT — Phê duyệt / Từ chối | ❌ | ❌ | ✅ cùng cấp | ❌ |
| CT — Công bố / Hủy CB | ❌ | ✅ | ❌ | ❌ |
| CT — Kích hoạt / Tạm dừng / Tiếp tục | ❌ | ✅ Kích hoạt | ✅ Tạm dừng/Tiếp tục | ❌ |
| CT — Hoàn thành | ❌ | ❌ | ✅ | ❌ |
| Đợt BC — CRUD (TAO_DOT) | 👁️ R | ✅ scope | 👁️ R | ❌ |

---

## A. PERMISSION CROSS-FR — TC

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-CT-001 | BR-AUTH-08 + FR-XI-01 | CB NV ĐP chỉ thấy CT của đơn vị mình | cb_nv_dp_01 (Sở TP AG) login. CT-AG10 + CT-BG10 (Sở TP BG) tồn tại. | — | 1. Truy cập SCR-XI-01. | (3) DS chỉ chứa CT-AG10. CT-BG10 KHÔNG xuất hiện. Force deep-link CT-BG10 → 403. | Negative 🔴 |
| TC-PERM-CT-002 | BR-AUTH-05 + FR-XI-04 | CB PD TW không duyệt CT của BN | cb_pd_tw_01 login. CT-BN02 CHO_PHE_DUYET (cấp BN). | — | 1. Force deep-link CT-BN02. | (1) 403 hoặc CT không xuất hiện. Force API approve → reject ERR-XI-04-03. | Negative 🔴 |
| TC-PERM-CT-003 | BR-AUTH-08 + FR-XI-05 | CB NV BN không công bố CT của ĐP | cb_nv_bn_01 (BKHĐT) login. CT-AG11 DA_DUYET. | — | 1. Force deep-link. | (1) 403. Force API publish → reject. | Negative 🟡 |
| TC-PERM-CT-004 | BR-AUTH-01 + Permission | NHT/TVV/CG không truy cập module | nht_01 / tvv_01 / cg_01 / dn_01 login. | — | 1. Force navigate `/quan-ly-ke-hoach-thuc-hien-chuong-trinh-htpldn`. | (1) Sidebar KHÔNG có menu này. Force URL → 403 hoặc redirect. | Negative 🔴 |
| TC-PERM-CT-005 | BR-AUTH-01 + Permission | QTHT chỉ READ, không CRUD | qtht_01 login. SCR-XI-01 mở. | — | 1. Mở SCR-XI-01. 2. Verify nút action. | (3) Truy cập DS được (read-only). Nút [+ Thêm CT] / [Sửa] / [Xóa] / [Phê duyệt] / [Công bố] đều ẩn. | Negative 🟡 |
| TC-PERM-CT-006 | BR-AUTH-01 / Login | Unauthenticated user → redirect login | (logout) | — | 1. Truy cập deep-link SCR-XI-01. | (1) Redirect `/login`. | Negative 🟢 |
| TC-PERM-CT-007 | BR-AUTH-01 / Permission Matrix §2.3 — CB_PD Read CRUD CT (Codex 2026-05-09 PERM-001) | CB_PD positive read DS CT (Read-only nhưng KHÔNG ẩn module) | cb_pd_tw_01 login. CT-DT30 DU_THAO + CT-PD30 CHO_PHE_DUYET tồn tại. | — | 1. Truy cập SCR-XI-01. 2. Quan sát toolbar + cột Hành động. 3. Click vào CT-DT30 để mở Tab Thông tin. | **STATE**: Backend filter scope BR-AUTH-08 + role check (CB_PD = Read CRUD per matrix). **UI**: DS CT hiển thị (KHÁC với QTHT — cùng read nhưng CB_PD trong scope đơn vị; KHÁC TC-PERM-CT-005 vì QTHT cross-cấp). Nút [+ Thêm CT] / [Sửa] / [Xóa] / [Hủy CT] / [Rút trình] ẨN. Nút [Phê duyệt] / [Từ chối] hiển thị khi CT CHO_PHE_DUYET. **PERSIST**: — | Happy 🟡 |
| TC-PERM-CT-008 | BR-AUTH-01 / Permission Matrix §2.3 — CB_PD negative Hủy/Rút trình + Công bố (Codex 2026-05-09 PERM-001) | CB_PD KHÔNG có quyền Hủy/Rút trình/Công bố | cb_pd_tw_01 login. CT-DT31 DU_THAO + CT-PD31 CHO_PHE_DUYET (trình bởi cb_nv_tw_01) + CT-DD31 DA_DUYET. | — | 1. Mở chi tiết CT-DT31. 2. Mở chi tiết CT-PD31. 3. Mở chi tiết CT-DD31. 4. Force API các action. | **STATE**: Backend role check. Per matrix §2.3: CB_PD = ❌ Hủy + ❌ Rút trình + ❌ Công bố (chỉ CB_NV). **UI**: 3 nút [Hủy CT] (CT-DT31) + [Rút trình] (CT-PD31) + [Công bố] (CT-DD31) đều ẨN với CB_PD. Force API: PATCH `/cancel` → ERR-XI-01-HC-01; PATCH `/withdraw` → ERR-XI-01-RT-01; PATCH `/publish` → 403/ERR. **PERSIST**: KHÔNG transition state. | Negative 🔴 |
| TC-PERM-CT-009 | BR-AUTH-01 / Permission Matrix §2.3 — QTHT lifecycle Read-only (Codex 2026-05-09 PERM-001) | QTHT KHÔNG có nút lifecycle (Trình/Phê duyệt/Công bố/Kích hoạt/Tạm dừng/Hoàn thành/Hủy/Rút trình) | qtht_01 login. Seed 5 CT mỗi state khác nhau (DU_THAO/CHO_PHE_DUYET/DA_DUYET/DA_CONG_BO/DANG_THUC_HIEN). | — | 1. Truy cập SCR-XI-01. 2. Mở chi tiết từng CT. 3. Quan sát action-bar Tab Thông tin. 4. Mở Tab Đợt BC, quan sát [+ Tạo đợt mới]. | **STATE**: QTHT = 👁️ R toàn HT (per matrix §2.3 + srs-fr-15:1409-1417 BR-AUTH-01 ngoại lệ). **UI**: TẤT CẢ nút lifecycle ẨN với QTHT trên 5 CT (Trình/Phê duyệt/Từ chối/Công bố/Hủy CB/Kích hoạt/Tạm dừng/Tiếp tục/Hoàn thành/Hủy/Rút trình). Nút [+ Thêm CT] + [Sửa] + [Xóa] + [+ Tạo đợt mới] cũng ẨN. **PERSIST**: QTHT chỉ truy cập DS đầy đủ (cross-cấp/đơn vị) read-only. | Negative 🟡 |

---

## Tổng kết file 08-TC

- **9 TC**: 1 Happy + 8 Negative (A3 base 6 + Codex 2026-05-09 +3)
- **Critical TC (🔴)**: 001, 002, 004, 008
- **Codex review 2026-05-09 PERM-001:**
  - TC-PERM-CT-007 (CB_PD positive Read CRUD CT — fill cell CB_PD × CRUD).
  - TC-PERM-CT-008 (CB_PD negative Hủy/Rút trình/Công bố — fill 3 cells CB_PD × {Hủy, Rút trình, Công bố}).
  - TC-PERM-CT-009 (QTHT Read-only toàn lifecycle — fill 6+ cells QTHT × {Trình, Phê duyệt, Công bố, Kích hoạt, Tạm dừng, Tiếp tục, Hoàn thành, Hủy, Rút trình, Đợt BC CRUD}).
- **DUP note (Codex DUP-001/002):** TC-PERM-CT-001 trùng TC-CT-CRUD-006 + TC-PERM-CT-003 trùng TC-CB-CT-006 — giữ nguyên cả 2 vì scope khác (CRUD scope vs explicit permission isolation). Không xóa.

*Generated 2026-05-06 — Phase A step A3 · Updated 2026-05-09 sau Codex review*
