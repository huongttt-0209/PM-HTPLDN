# Test Cases — FR-XI-05a (cont) + FR-XI-06 step 1 (UC165→UC166): Bắt đầu lập BC

> **SRS Ref**: FR-XI-05a (continuation) + FR-XI-06 step 1, SCR-XI-01 (Tab "Đợt báo cáo" + Drill-down), Entity DOT_BAO_CAO + BAO_CAO_CT_HTPL
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Transition SM-DOT-BC: TAO_DOT → DANG_LAP_BC. Trigger: CB NV click "Bắt đầu lập BC" trên đợt BC đang ở TAO_DOT. Side-effect: tạo BAO_CAO_CT_HTPL record (trạng thái DU_THAO) liên kết với đợt.
> **Scope**: CHỈ transition + record creation — KHÔNG gồm form 21a/21b nhập số liệu (xem `02-TC-lap-bao-cao-kq.md`)

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-XI-05a / FR-XI-06 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập (BR-AUTH-01), có quyền "Quản lý đợt báo cáo CT HTPLDN" và "Lập BC kết quả thực hiện CT", CT ở DANG_THUC_HIEN/HOAN_THANH, đã có ≥1 đợt BC ở TAO_DOT.

---

## A. Bắt đầu lập BC — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LBC-001 | SM-DOT-BC / TAO_DOT → DANG_LAP_BC | Bắt đầu lập BC happy path | cb_nv_tw_01 login. CT-TW01 DANG_THUC_HIEN. Đợt DOT-CTW01-001 ở TAO_DOT. | — | 1. Mở chi tiết CT-TW01 → Tab "Đợt báo cáo". 2. Click row DOT-CTW01-001 → drill-down. 3. Click [Bắt đầu lập BC]. | (3) PATCH `/api/v1/dot-bao-cao/{id}/start-lap-bc` 200. (3) Đợt BC trạng thái = `DANG_LAP_BC`, badge đổi màu `--color-warning`. (3) BAO_CAO_CT_HTPL record mới tạo (`ma_bao_cao` auto-gen, `ct_htpl_id`=CT-TW01.id, `trang_thai`=DU_THAO, `ky_bao_cao` đồng bộ từ đợt). (3) Form 21a/21b render editable. (3) Audit log INSERT BAO_CAO_CT_HTPL + UPDATE DOT_BAO_CAO (BR-DATA-05). | Happy 🔴 |
| TC-LBC-002 | SM-DOT-BC / Guard "Đợt đã hoàn chỉnh" (SPEC-CLARIFY-CT-GD2-01) | Verify guard "Đợt đã hoàn chỉnh thông tin" | cb_nv_tw_01 login. Đợt DOT-CTW01-002 ở TAO_DOT, **thiếu** trường tùy chọn `ghi_chu` (mock incomplete tùy interpretation BA). | — | 1. Mở drill-down. 2. Click [Bắt đầu lập BC]. | (3) ⚠️ SPEC-CLARIFY-CT-GD2-01: SRS dòng 1391-1392 nói guard "Đợt đã hoàn chỉnh thông tin" nhưng không định nghĩa trường nào BẮT BUỘC trước transition. Expected: PASS nếu các trường BẮT BUỘC (ten/ky/han_nop/tu-den_ngay/bieu_mau) đầy đủ; ghi_chu optional không block. Nếu UI block → log GAP. | Edge 🟡 |
| TC-LBC-003 | FR-XI-06 / Inputs (auto-fill từ context) | BC mới kế thừa context từ đợt BC | cb_nv_dp_01 (Sở TP AG) login. Đợt DOT-CDP01-003 ở TAO_DOT, ky=SO_BO_NAM, tu_ngay=2026-01-01, den_ngay=2026-06-30. | — | 1. Drill-down + click [Bắt đầu lập BC]. 2. MCP `evaluate_script` đọc form data. | (2) Form auto-fill: `chuong_trinh_id`=CT-DP01.id; `ky_bao_cao`=SO_BO_NAM; `tu_ngay`=2026-01-01; `den_ngay`=2026-06-30 (read-only context). `so_lieu` rỗng (chưa nhập); `nhan_xet` rỗng. | Happy 🟡 |

---

## B. Bắt đầu lập BC — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LBC-010 | SM-DOT-BC / Đợt ≠ TAO_DOT | Bắt đầu lập BC khi đợt ≠ TAO_DOT | cb_nv_tw_01 login. Đợt DOT-CTW01-010 đã ở DANG_LAP_BC. | — | 1. Drill-down. 2. Click [Bắt đầu lập BC]. | (1) Nút [Bắt đầu lập BC] **ẩn** vì đợt đã DANG_LAP_BC HOẶC backend reject 400 với toast "Đợt BC không ở trạng thái TAO_DOT" (transition guard). KHÔNG tạo BC trùng. | Negative 🔴 |
| TC-LBC-011 | BR-AUTH-08 + BR-AUTH-01 | Role không có quyền lập BC | nht_01 login (NHT). Đợt DOT-CTW01-011 ở TAO_DOT. | — | 1. Truy cập trực tiếp URL `/ct-htpldn/{id}/dot-bc/{dot_id}`. | (1) 403 Forbidden HOẶC redirect khỏi module. KHÔNG hiển thị nút [Bắt đầu lập BC]. | Negative 🔴 |

---

## C. Bắt đầu lập BC — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LBC-012 | SM-DOT-BC / Idempotency double-click (A4) | Click [Bắt đầu lập BC] 2 lần liên tiếp | cb_nv_tw_01 login. Đợt DOT-CTW01-012 TAO_DOT. | — | 1. Click [Bắt đầu lập BC] lần 1 (không chờ response). 2. Click lần 2 ngay. | (2) Lần 2 reject HOẶC nút disable sau click 1. CHỈ 1 BAO_CAO_CT_HTPL record được tạo (không trùng). Audit log chỉ 1 INSERT. | Edge 🟡 |
| TC-LBC-013 | SM-KH-CTHTPL guard / CT TAM_DUNG (A4) | Bắt đầu lập BC khi CT TAM_DUNG | cb_nv_tw_01 login. CT-TW13 TAM_DUNG. Đợt DOT-CTW13-013 TAO_DOT (đã tạo trước khi CT bị tạm dừng). | — | 1. Drill-down. 2. Click [Bắt đầu lập BC]. | (2) ⚠️ SRS không nói rõ guard "CT TAM_DUNG có cho phép lập BC không". Expected: BLOCK với toast "CT đang tạm dừng, không thể lập BC" hoặc PASS (BC đã có). Log SPEC-CLARIFY-CT-GD2-06. | Edge 🟡 |

---

## Tổng kết file 01-TC

- **7 TC**: 3 Happy + 2 Negative + 2 Edge (A3 base 5 + A4 merged 2)
- **Critical TC (🔴)**: 001, 010, 011
- **A4 merged 2026-05-10**: TC-LBC-012, TC-LBC-013
- **SPEC-CLARIFY**: CT-GD2-01 (TC-LBC-002 guard "đợt hoàn chỉnh"), CT-GD2-06 (TC-LBC-013 CT TAM_DUNG)

*Generated 2026-05-10 — Phase A step A3 + A4 inline merge*
