# TC FR-VI-05 + FR-VI-06 — Chọn VV (UC87) + Thực hiện chấm điểm (UC88) — Tab 3

> **SRS:** [`srs-fr-08-danh-gia.-v3.1.md`](../../../input/srs-v3/srs-fr-08-danh-gia.-v3.1.md) §FR-VI-05 (line 375-437) + §FR-VI-06 (line 441-512) + §3 Tab 3 (line 854-863)
> **SCR:** SCR-VI-01 — Tab 3 Thực hiện chấm điểm
> **Actor:** CB NV (chọn VV) + Người được phân công (chấm điểm) — `cb_nv_*_01` / `cg_01..06` / `nht_01..04`
> **Entity:** VU_VIEC_DANH_GIA (link VV → đợt) + KET_QUA_DANH_GIA (chi tiết điểm)
> **BR core:** BR-CALC-04 (điểm tổng = SUM diem_i × trong_so_i / 100) + BR-AUTH-08
> **SM transition:** THUC_HIEN → BAO_CAO (auto khi tất cả VV đã chấm)
> **Total TC:** 14

---

## Test Cases

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-DG-001 | Mở Tab Thực hiện — chọn VV multi-select | Login `cb_nv_tw_01`. Đợt THUC_HIEN (sau duyệt PC). 18 VV HOAN_THANH scope TW trong kỳ. | 1. Mở chi tiết đợt<br>2. Tab "Thực hiện chấm điểm" | Tab hiển thị multi-select "Chọn VV đánh giá" + bảng chấm rỗng + KPI cards 0/0 | Critical | SCR row #41-43 |
| TC-DG-DG-002 | Filter VV — chỉ HOAN_THANH trong kỳ + cùng đơn vị | Login. Kỳ đợt 2026-01-01 → 2026-06-30. | 1. Mở dropdown chọn VV<br>2. Search keyword | Dropdown chỉ chứa VV `trang_thai=HOAN_THANH` + `ngay_hoan_thanh` trong kỳ + `don_vi_id` cùng. 18 VV xuất hiện | Critical | UC87 process step 2, BR-AUTH-08 |
| TC-DG-DG-003 | Cảnh báo VV đã thuộc đợt khác (cho phép chọn lại) | Login. VV-001 đã thuộc đợt DG-20260502-0001. | 1. Mở đợt mới khác kỳ<br>2. Chọn VV-001 | Cảnh báo "Vụ việc đã thuộc đợt khác" nhưng vẫn cho phép chọn (per UC87 process step 5) | Medium | UC87 step 5, AC-3 |
| TC-DG-DG-004 | Chọn 5 VV → bảng chấm điểm hiện 5 hàng | Login. | 1. Multi-select 5 VV<br>2. Confirm | Bảng có 5 hàng. Mỗi hàng cột: Mã VV / Tên DN / Lĩnh vực / [1 cột per tiêu chí] / Điểm tổng (0) / Nhận xét | High | SCR row #42 |
| TC-DG-DG-005 | Chấm điểm 1 VV với 4 tiêu chí — happy path | Login `cb_nv_tw_01` (được phân công TRUONG_NHOM). 5 VV, 4 tiêu chí (40+30+20+10=100%). | 1. Hàng VV-001: nhập điểm tiêu chí 1=8 (max 10), 2=7, 3=9, 4=6<br>2. Tab/Save | Điểm tổng auto = (8×40 + 7×30 + 9×20 + 6×10) / 100 = (320+210+180+60)/100 = 7.7. Xếp loại "Tốt" (≥7.0) per SCR row #43 | Critical | UC88 happy, BR-CALC-04 |
| TC-DG-DG-006 | Validate điểm vượt diem_toi_da → ERR-DG-DG-01 | Login. Tiêu chí 1 max=10. | 1. Nhập điểm tiêu chí 1 = 11 | Inline error "Điểm phải từ 0 đến 10" (ERR-DG-DG-01) | High | ERR-DG-DG-01, AC E1 |
| TC-DG-DG-007 | Validate điểm âm → ERR-DG-DG-01 | Login. | 1. Nhập điểm = -5 | Inline error "Điểm phải từ 0 đến 10" | High | ERR-DG-DG-01 |
| TC-DG-DG-008 | Lưu nháp khi chấm dở (is_draft=1) | Login. 5 VV, chỉ chấm 2/5. | 1. Click [Lưu kết quả] | Toast "Đã lưu nháp". State giữ THUC_HIEN. KPI "Số VV đã chấm: 2/5" | High | UC88 process step 7 (lưu nháp), SCR row #44 |
| TC-DG-DG-009 | Hoàn tất chấm điểm — block khi chưa chấm hết | Login. 2/5 VV đã chấm. | 1. Click [Hoàn tất chấm điểm] | Nút disabled HOẶC click → toast "Còn 3/5 VV chưa chấm" | High | SCR row #45 condition |
| TC-DG-DG-010 | Hoàn tất chấm điểm — happy path → BAO_CAO | Login. 5/5 VV đã chấm + nhận xét đầy đủ. | 1. Click [Hoàn tất chấm điểm]<br>2. Confirm | State THUC_HIEN → BAO_CAO. Toast success. Tab Báo cáo unlock | Critical | SM-DANHGIA #6, AC §3 step 8 |
| TC-DG-DG-011 | KPI cards xếp loại realtime | Login. 5 VV đã chấm điểm tổng [9.5, 8.0, 7.5, 5.5, 4.5]. | 1. Quan sát KPI cards | "Số VV đã chấm: 5/5". "Điểm TB: 7.0". Xếp loại bins: Xuất sắc (1) / Tốt (2) / Đạt (1) / Chưa đạt (1) per SCR row #43 | High | SCR row #43, BR-CALC-04 |
| TC-DG-DG-012 | Sửa tiêu chí trong khi chấm → ERR-DG-TC-02 | Login. Đợt THUC_HIEN có 1 VV đã chấm. | 1. Quay lại Tab 1 Tiêu chí<br>2. Sửa trọng số | Block "Không thể sửa tiêu chí khi đợt đang đánh giá" (ERR-DG-TC-02) | High | ERR-DG-TC-02 |
| TC-DG-DG-013 | Người ngoài phân công không chấm được | Login `cg_05` (KHÔNG được phân công đợt này). | 1. Mở chi tiết đợt<br>2. Tab Thực hiện | Bảng chấm read-only HOẶC field input disabled. Toast "Bạn không được phân công đánh giá đợt này" | High | UC88 step 2, BR-AUTH-01 |
| TC-DG-DG-014 | 0 VV hoàn thành trong kỳ → empty state + WRN-DG-VV-01 | Login. Đợt mới kỳ 2027-01-01 → 2027-06-30 (chưa có VV trong kỳ). | 1. Mở Tab Thực hiện | Empty state hiển thị WRN-DG-VV-01 "Không có vụ việc nào hoàn thành trong kỳ đánh giá này". Multi-select rỗng | Medium | WRN-DG-VV-01, SCR §3.7 |

---

## Edge bổ sung (A4 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-DG-015 | Điểm decimal — chấp nhận 7.5 (số thập phân) | Login. Tiêu chí max=10. | 1. Nhập điểm = 7.5 | Lưu OK. KQ tổng tính floating | Medium | UC88 input #3 |
| TC-DG-DG-016 | Boundary điểm = 0 và điểm = max | Login. Max=10. | 1. Nhập điểm 0<br>2. Nhập điểm 10 | Cả 2 lưu OK (boundary inclusive) | High | UC88 input #3 ràng buộc 0..max |
| TC-DG-DG-017 | Boundary nhan_xet 1000 ký tự | Login. | 1. Nhập nhan_xet 1000 chars | Lưu OK | Low | UC88 input #4 max 1000 |
| TC-DG-DG-018 | nhan_xet 1001 ký tự → block | Login. | 1. Nhập 1001 chars | Inline error | Low | UC88 input #4 |
| TC-DG-DG-019 | Boundary nhan_xet_tong_the 2000 ký tự | Login. | 1. Nhập 2000 chars | Lưu OK | Low | UC88 input #5 max 2000 |
| TC-DG-DG-020 | Xếp loại boundary — điểm chuẩn hóa 7.00 (=70%) → "Tốt" (P1 F-013) | Login. Tiêu chí thang max=10. | 1. Chấm để điểm tổng (normalized 0-10) = 7.00 | KPI hiển thị xếp loại "Tốt" (≥70% boundary inclusive). Display % = 70.0% | Medium | SCR row #43 ranges, BR-CALC-04 normalized scale |
| TC-DG-DG-021 | Xếp loại boundary điểm chuẩn hóa 4.99 (=49.9%) → "Chưa đạt" (P1 F-013) | Login. | 1. Chấm điểm tổng = 4.99 (49.9% normalized) | "Chưa đạt" (<50%). Display % = 49.9% | Medium | SCR row #43, BR-CALC-04 normalized scale |
| TC-DG-DG-022 | Concurrent chấm điểm — 2 TRUONG_NHOM cùng VV | Login 2 tab cg_01 + cg_02 (cùng phân công TRUONG_NHOM, cùng VV-001). | 1. Cả 2 chấm điểm khác nhau<br>2. Save song song | Last-write-wins HOẶC merge per `nguoi_danh_gia_id` (1 record per người per VV per đợt). DB không conflict | High | SPEC-CLARIFY-DG-03 (single record per đợt hay per người ĐG?) |
| TC-DG-DG-023 | Chọn lại VV đã chấm → giữ điểm cũ | Login. VV-001 đã chấm. | 1. Multi-select VV-001 lần 2 (idempotent) | Bảng giữ điểm cũ. Không xóa KET_QUA_DANH_GIA | Medium | UC87 step 4 |
| TC-DG-DG-024 | Bỏ chọn VV đã chấm → SPEC-CLARIFY (P1 F-014) | Login. VV-001 đã chấm. | 1. Bỏ tích VV-001<br>2. Quan sát hành vi | Spec FR-VI-05 KHÔNG đặc tả xử lý KET_QUA_DANH_GIA khi deselect. Verify behavior thực tế (preserve / cảnh báo + xóa / không cho phép) → log SPEC-CLARIFY-DG-08 | Medium | SPEC-CLARIFY-DG-08 |

## Fill GAP A5 (A6 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-DG-025 | Hủy đợt từ THUC_HIEN → HUY (GAP-A5-02) | Login `cb_nv_tw_01`. Đợt THUC_HIEN có 5 VV chọn + 2 đã chấm. | 1. Mở chi tiết<br>2. Click [Hủy đợt]<br>3. Lý do "Đợt sai phạm vi đơn vị, hủy"<br>4. Confirm | State THUC_HIEN → HUY. KQ chấm còn nguyên (soft-delete đợt). Audit log | High | SM-DANHGIA #12 |
| TC-DG-DG-026 | Chọn VV khi đợt KHÔNG ở THUC_HIEN → ERR-DG-VV-01 (GAP-A5-05) | Login. Đợt LAP_KE_HOACH. | 1. Mở Tab Thực hiện<br>2. Cố mở multi-select VV | Tab disabled HOẶC click → "Đợt không ở trạng thái phù hợp" (ERR-DG-VV-01) | High | ERR-DG-VV-01 |
| TC-DG-DG-027 | WRN-DG-VV-02 executable — đợt THUC_HIEN có 0 VV chọn (P0 F-002) | Login. Đợt THUC_HIEN, multi-select VV để rỗng (chưa chọn VV nào). | 1. Mở Tab Thực hiện chấm điểm<br>2. Quan sát empty state | Hiển thị WRN-DG-VV-02 NGUYÊN VĂN "Không có VV nào trong kỳ" + bảng chấm rỗng. KHÔNG cho phép Hoàn tất chấm điểm | Critical | WRN-DG-VV-02, FR-VI-06 E4 |

## Codex Review apply (2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-DG-028 | ERR-DG-TC-01 trong scoring context — tiêu chí lệch tolerance (P1 F-015) | Login. Đợt THUC_HIEN. Trọng số tổng tiêu chí = 99.5% (vi phạm tolerance ±0.01%). | 1. Mở Tab Thực hiện<br>2. Cố Save kết quả chấm | Block + ERR-DG-TC-01 NGUYÊN VĂN "Tổng trọng số phải bằng 100%" trong scoring | High | FR-VI-06 E2 ERR-DG-TC-01, BR-CALC-04 tolerance |
| TC-DG-DG-029 | VU_VIEC_DANH_GIA persistence sau reload (P2 F-028) | Login. 5 VV đã chọn vào đợt. | 1. Reload page<br>2. Mở lại Tab Thực hiện | 5 VV vẫn xuất hiện trong bảng. KET_QUA_DANH_GIA persisted. Xác nhận FR-VI-05 Postcondition | Medium | FR-VI-05 Outputs #1, Postconditions |

## Tổng số TC: 29 (14 base + 10 edge A4 + 3 fill A6 + 2 Codex apply)

> **SPEC-CLARIFY-DG-08:** Behavior khi deselect VV đã chấm — preserve KET_QUA hay xóa? — pending BA per FR-VI-05 Processing step 4 mơ hồ.

> **A4 done 2026-05-10** — 10 TC mới merge inline.
> **A6 placeholder — Fill GAP-A5.**
> **A7 placeholder — LOẠI/SỬA log.**
> **SPEC-CLARIFY-DG-03:** KET_QUA_DANH_GIA scheme: 1 record per VV per đợt hay per người ĐG per VV per đợt (multi-evaluator)? — pending BA.
