# Test Cases — Smoke 11 DM chuẩn TPL-DM-CRUD

> **Module:** QTHT — DM dùng chung · **FR:** FR-VIII-02, 07, 08, 09, 13, 18, 19 (7 DM smoke); +smoke partial cho 4 DM đã có file riêng (UC101 Chương trình HT, UC102 Tình trạng VV, UC105 Loại DN, UC106/107 Hồ sơ — chỉ 5 TC smoke ở đây, deep test ở file riêng)
> **Mục đích:** Verify TPL-DM-CRUD pattern áp dụng đúng cho 11 DM khác (ngoài LV-PL — file 01). 5 TC/DM × 11 DM = **55 TC**.
> **Pattern smoke:** Render list + Create happy path (với Inputs đặc thù) + Validate ma unique + Update + Delete (ràng buộc tham chiếu).

> **Scope note (R2.5 lesson learned từ Codex review):** Smoke 11 DM × 5 TC **CỐ Ý shallow** — chỉ test 1 negative validation (ERR-DM-01 trùng mã) per DM. **KHÔNG duplicate** các negative test ERR-DM-02 (tên trống), ERR-DM-04 (record không tồn tại), ERR-DM-05 (mã >20 ký tự) cho từng DM smoke vì:
>
> 1. **Backend chung TPL-DM-CRUD** (srs-fr-10:58-163) — 13 DM dùng cùng processing logic + validation rule. ERR-DM-02/04/05 đã được test sâu ở **file 01 LV-PL representative** (TC-LV-011, TC-LV-013, TC-LV-024) — cover backend behavior cho mọi DM dùng template.
> 2. **Avoid balloon redundancy** — duplicate 3 negative × 11 DM = 33 TC redundant không thêm coverage value (cùng code path, cùng error message, chỉ khác `loai_danh_muc` parameter).
> 3. **DM đặc thù** (UC101/102/105/109/110 + JSON UC106/107) có file deep riêng test full negative cho fields đặc thù (vd UC109 ERR-TC-01, UC102 mau HEX, UC101 date range).
>
> Phase B chạy file 01 trước → confirm TPL-DM-CRUD backend hoạt động đúng → smoke 11 DM chỉ verify pattern wiring (LIST + CREATE happy + UPDATE + DELETE). Bug ERR-DM-* nếu có sẽ phát hiện ở file 01.

---

## 1. FR-VIII-02 — Loại hình hỗ trợ (UC100)

> **Inputs đặc thù:** ma (vd TU_VAN, DAO_TAO), ten, loai_danh_muc='LOAI_HINH_HO_TRO'. Seed: Tư vấn PL, Tham gia tố tụng, Đào tạo/bồi dưỡng, Hòa giải, Đại diện ngoài tố tụng.
> **Ràng buộc xóa:** Tham chiếu từ HOI_DAP.loai_hinh_id, VU_VIEC.loai_hinh_id, TUVAN.loai_hinh_id (xác minh entity §3.4).

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-LH-001 | qtht_01 mở `/quan-tri/danh-muc/LOAI_HINH_HO_TRO` | List render 5 record seed; sub-tab "Loại hình HT" active | line 208-230 |
| TC-LH-002 | Click [+ Thêm mới], nhập ma="TEST_LH", ten="Test loại hình", submit | Tạo OK; xuất hiện trong list; audit INSERT | line 224-230 |
| TC-LH-003 | Tạo mới với ma="TU_VAN" (đã có) | ERR-DM-01 "Mã 'TU_VAN' đã tồn tại trong danh mục Loại hình hỗ trợ" | E3 |
| TC-LH-004 | Sửa ten "TEST_LH" → "Test loại hình updated" | Lưu OK; audit UPDATE old/new | line 100-110 |
| TC-LH-005 | Xóa "TEST_LH" (không có tham chiếu) | Soft delete OK; audit DELETE | BR-DATA-01 |

---

## 2. FR-VIII-07 — Loại doanh nghiệp (UC105)

> **Inputs đặc thù:** ma (SIEU_NHO/NHO/VUA), ten, tieu_chi_doanh_thu (text NĐ39/2018), tieu_chi_lao_dong (text), loai_danh_muc='LOAI_DOANH_NGHIEP'. Seed: DN siêu nhỏ, DN nhỏ, DN vừa.
> **Note:** Deep test fields tieu_chi ở file 08-TC-loai-dn-tieu-chi.md. File này chỉ smoke CRUD pattern.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-LDN-001 | qtht_01 mở `/quan-tri/danh-muc/LOAI_DOANH_NGHIEP` | List 3 record seed (Siêu nhỏ/Nhỏ/Vừa); cột Mã/Tên hiển thị | line 382-399 |
| TC-LDN-002 | [+ Thêm], ma="TEST_QM", ten="Test quy mô", tieu_chi_doanh_thu="< 10 tỷ", tieu_chi_lao_dong="< 30 người" | Tạo OK; audit INSERT | — |
| TC-LDN-003 | Tạo mới ma="SIEU_NHO" (trùng) | ERR-DM-01 | E3 |
| TC-LDN-004 | Sửa "TEST_QM" đổi tieu_chi_doanh_thu | Lưu OK; cột bổ sung không impact | — |
| TC-LDN-005 | Xóa "TEST_QM" (không tham chiếu DOANH_NGHIEP.loai_doanh_nghiep_id) | Soft delete OK | BR-DATA-01 |

---

## 3. FR-VIII-08 — Hồ sơ đề nghị HT (UC106)

> **Inputs đặc thù:** ma, ten, thanh_phan_bat_buoc (structured JSON), thanh_phan_tuy_chon (structured JSON). Smoke chỉ test CRUD; JSON cấu trúc deep test ở file 09.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-HSHT-001 | qtht_01 mở `/quan-tri/danh-muc/HO_SO_DE_NGHI_HT` | List render | line 403-419 |
| TC-HSHT-002 | [+ Thêm], ma="TEST_HSHT", ten="Test HSDN HT", thanh_phan_bat_buoc=[]/null, submit | Tạo OK | — |
| TC-HSHT-003 | Tạo trùng ma | ERR-DM-01 | E3 |
| TC-HSHT-004 | Sửa "TEST_HSHT" đổi ten | Lưu OK; audit | — |
| TC-HSHT-005 | Xóa "TEST_HSHT" | Soft delete OK | BR-DATA-01 |

---

## 4. FR-VIII-09 — Hồ sơ đề nghị TT (UC107)

> **Inputs đặc thù:** ma, ten, thanh_phan_ho_so (structured JSON). Tương tự UC106. Deep test JSON ở file 09.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-HSTT-001 | qtht_01 mở `/quan-tri/danh-muc/HO_SO_DE_NGHI_TT` | List render | line 422-436 |
| TC-HSTT-002 | [+ Thêm], ma="TEST_HSTT", ten="Test HSDN TT", thanh_phan_ho_so=[]/null | Tạo OK | — |
| TC-HSTT-003 | Tạo trùng ma | ERR-DM-01 | E3 |
| TC-HSTT-004 | Sửa "TEST_HSTT" | Lưu OK | — |
| TC-HSTT-005 | Xóa "TEST_HSTT" | Soft delete OK | BR-DATA-01 |

---

## 5. FR-VIII-13 — Loại tài khoản (UC111)

> **Inputs đặc thù:** ma, ten, loai_danh_muc='LOAI_TAI_KHOAN'. Seed: CB NV TW, CB NV BN, CB NV ĐP, CB PD TW, CB PD BN, CB PD ĐP, TVV, CG, DN, NHT, QTHT (~11 record).
> **Ràng buộc xóa:** TAI_KHOAN.loai_tai_khoan_id.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-LTK-001 | qtht_01 mở `/quan-tri/danh-muc/LOAI_TAI_KHOAN` | List 11 record seed | line 575-591 |
| TC-LTK-002 | [+ Thêm], ma="TEST_LTK", ten="Test loại TK" | Tạo OK | — |
| TC-LTK-003 | Trùng ma="QTHT" | ERR-DM-01 | E3 |
| TC-LTK-004 | Sửa "TEST_LTK" | Lưu OK | — |
| TC-LTK-005 | Xóa "QTHT" (đang dùng cho TAI_KHOAN của qtht_01..02..03) | Reject ERR-DM-03 "Đang được sử dụng bởi N bản ghi TAI_KHOAN" | E5 line 591 |

---

## 6. FR-VIII-18 — Loại hình tiếp nhận (UC116)

> **Inputs đặc thù:** ma (TRUC_TUYEN/TRUC_TIEP/HE_THONG_KHAC/BUU_CHINH/DIEN_THOAI), ten, loai_danh_muc='LOAI_HINH_TIEP_NHAN'. Seed: 5 record.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-LHTN-001 | qtht_01 mở `/quan-tri/danh-muc/LOAI_HINH_TIEP_NHAN` | List 5 record seed | line 846-861 |
| TC-LHTN-002 | [+ Thêm], ma="TEST_LHTN", ten="Test loại hình TN" | Tạo OK | — |
| TC-LHTN-003 | Trùng ma="TRUC_TUYEN" | ERR-DM-01 | E3 |
| TC-LHTN-004 | Sửa "TEST_LHTN" đổi ten | Lưu OK | — |
| TC-LHTN-005 | Xóa "TEST_LHTN" | Soft delete OK | BR-DATA-01 |

---

## 7. FR-VIII-19 — Kênh tiếp nhận (UC117)

> **Inputs đặc thù:** ma, ten, loai_danh_muc='KENH_TIEP_NHAN'. Spec không có seed list explicit.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-KTN-001 | qtht_01 mở `/quan-tri/danh-muc/KENH_TIEP_NHAN` | List render (có thể empty hoặc seed) | line 865-878 |
| TC-KTN-002 | [+ Thêm], ma="WEBSITE", ten="Website cổng" | Tạo OK | — |
| TC-KTN-003 | Trùng ma | ERR-DM-01 | E3 |
| TC-KTN-004 | Sửa | Lưu OK | — |
| TC-KTN-005 | Xóa | Soft delete OK | BR-DATA-01 |

---

## 8. FR-VIII-03 — Chương trình hỗ trợ (UC101) — SMOKE

> **Note:** Deep test ở file 06-TC-chuong-trinh-ho-tro-date.md. File này chỉ verify pattern CRUD chuẩn vẫn work với fields đặc thù (date range + don_vi_chu_tri).

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-CT-SM-001 | qtht_01 mở `/quan-tri/danh-muc/CHUONG_TRINH_HT` | List render | line 234-256 |
| TC-CT-SM-002 | [+ Thêm], ma="TEST_CT", ten="Test CT", thoi_gian_bat_dau=2026-01-01, thoi_gian_ket_thuc=2026-12-31, don_vi_chu_tri="Cục BLDS" | Tạo OK | — |
| TC-CT-SM-003 | Trùng ma | ERR-DM-01 | E3 |
| TC-CT-SM-004 | Sửa "TEST_CT" đổi don_vi_chu_tri | Lưu OK | — |
| TC-CT-SM-005 | Xóa "TEST_CT" (không có CHUONG_TRINH_HTPL tham chiếu) | Soft delete OK; (nếu có tham chiếu → ERR-DM-03 với entity CHUONG_TRINH_HTPL) | line 256, BR-DATA-01 |

---

## 9. FR-VIII-04 — Tình trạng vụ việc (UC102) — SMOKE

> **Note:** Deep test ở file 07-TC-tinh-trang-vv-mau.md. File này chỉ verify pattern CRUD.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-TT-SM-001 | qtht_01 mở `/quan-tri/danh-muc/TINH_TRANG_VU_VIEC` | List render 7 seed (Mới tiếp nhận, Đang kiểm tra, ...) | line 260-282 |
| TC-TT-SM-002 | [+ Thêm], ma="TEST_TT", ten="Test TT", thu_tu=99, mau_hien_thi="#FF0000" | Tạo OK | — |
| TC-TT-SM-003 | Trùng ma="MOI" | ERR-DM-01 | E3 |
| TC-TT-SM-004 | Sửa "TEST_TT" đổi mau_hien_thi="#00FF00" | Lưu OK; verify badge color đổi | — |
| TC-TT-SM-005 | Xóa "TEST_TT" (không có VU_VIEC.tinh_trang_id tham chiếu) | Soft delete OK | BR-DATA-01 |

---

## 10. FR-VIII-11 — Tiêu chí ĐG hiệu quả (UC109) — SMOKE

> **Note:** Deep test ở file 04-TC-tieu-chi-dg-hieu-qua.md (BR-CALC-04 trọng số 100%, thang điểm). File này chỉ verify pattern CRUD.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-TCHQ-SM-001 | qtht_01 mở `/quan-tri/danh-muc/TIEU_CHI_DG_HIEU_QUA` | List render với cột Trọng số/Thang điểm; label "Tổng: {X}%" | line 519-549, 1480-1485 |
| TC-TCHQ-SM-002 | [+ Thêm], ma="TEST_TCHQ", ten="Test tiêu chí", trong_so=20, thang_diem_min=1, thang_diem_max=10 | Tạo OK | — |
| TC-TCHQ-SM-003 | Trùng ma | ERR-DM-01 | E3 |
| TC-TCHQ-SM-004 | Sửa "TEST_TCHQ" đổi trong_so=30 | Lưu OK; label tổng cập nhật | — |
| TC-TCHQ-SM-005 | Xóa "TEST_TCHQ" | Soft delete OK | BR-DATA-01 |

---

## 11. FR-VIII-12 — Tiêu chí ĐG chi phí (UC110) — SMOKE

> **Note:** Deep test ở file 05-TC-tieu-chi-dg-chi-phi.md. File này chỉ verify pattern CRUD.

| ID | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|
| TC-TCCP-SM-001 | qtht_01 mở `/quan-tri/danh-muc/TIEU_CHI_DG_CHI_PHI` | List render với cột Quy mô/Mức/Trần | line 553-571, 1488-1491 |
| TC-TCCP-SM-002 | [+ Thêm], ma="TEST_TCCP", ten="Test CP", quy_mo_dn="SIEU_NHO", muc_ho_tro_phan_tram=100, tran_ho_tro_nam=3000000 | Tạo OK | — |
| TC-TCCP-SM-003 | Trùng ma | ERR-DM-01 | E3 |
| TC-TCCP-SM-004 | Sửa "TEST_TCCP" đổi tran_ho_tro_nam | Lưu OK | — |
| TC-TCCP-SM-005 | Xóa "TEST_TCCP" | Soft delete OK | BR-DATA-01 |

---

**Tổng số TC:** 55 (5 × 11 DM smoke)
**Note:** 4 DM (UC101 CT, UC102 TT, UC109 TCHQ, UC110 TCCP) chỉ có 5 TC smoke pattern CRUD — fields đặc thù được test deep ở file riêng (06/07/04/05). 7 DM còn lại (LH/LDN/HSHT/HSTT/LTK/LHTN/KTN) có 5 TC trọn vẹn — đủ smoke vì pattern thuần TPL-DM-CRUD.
