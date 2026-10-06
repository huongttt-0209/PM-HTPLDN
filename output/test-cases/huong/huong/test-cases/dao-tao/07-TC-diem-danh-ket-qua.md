# Test Cases — UC24 (Điểm danh + KQ kiểm tra) + UC36 (Trình KQ AT-02) — FR-III-05 + FR-III-17

> **SRS Ref**: FR-III-05 (UC24 — Quản lý kiểm tra, đánh giá KQ) `srs-fr-03-dao-tao.md` dòng 412-498 + FR-III-17 (UC36 — Ghi nhận KQ AT-02) dòng 972-993.
> **Màn hình**: SCR-III-02 Tab "Lịch học & Điểm danh" (Tab 3) + Tab "KQ kiểm tra" (Tab 4).
> **Entity**: `KET_QUA_HOC_TAP` (§3.4.3.23).
> **Process flow**: `02-thu-tu-module.md` §⑨ dòng 599-600 (Tab Lịch học chỉ sửa khi `DANG_DIEN_RA`; Tab KQ chỉ sửa khi `DA_KET_THUC`) + dòng 628 (Trình KQ guard).
> **Phase**: A — Phase A re-run.
> **Ngày tạo**: 2026-05-09.

---

## A. UI FIELD VERIFICATION (BẮT BUỘC chạy trước functional)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-UI-01 | FR-III-05 / SCR-III-02 / Tab 3 dòng 599 | Verify Tab "Lịch học & Điểm danh" — bảng buổi × HV + tỷ lệ chuyên cần | CB_NV_TW. KH-TW-DDR-001 `DANG_DIEN_RA`, có 5 HV `DA_DUYET` + 6 buổi học. | URL: `/dao-tao/khoa-hoc/{id}/lich-hoc` | 1. Mở SCR-III-02 KH-TW-DDR-001. 2. Click Tab "Lịch học & Điểm danh". 3. Kiểm tra layout. | **LAYOUT**: Toolbar [Cấu hình lịch học] (cb_nv) + [Xuất Excel]. **TABLE 2D**: rows = 5 HV (Họ tên + MST), cols = 6 buổi (ngày dd/mm) + cột "Tỷ lệ chuyên cần" (auto). Mỗi cell điểm danh: dropdown 3 giá trị (Có mặt / Vắng mặt / Vắng có phép) — **SPEC-CLARIFY-DT-KQ-01**: SRS dòng 434 chỉ nói boolean Có mặt/Vắng, dòng 599 cũng chỉ 2 trạng thái — option "Vắng có phép" có hay không cần BA confirm. **TỶ LỆ AUTO**: %CC = (Có mặt + Vắng có phép) / Tổng buổi × 100 — formula **SPEC-CLARIFY-DT-KQ-02** (SRS không quote công thức). **NEGATIVE**: Khi KH `DA_KET_THUC`/`HOAN_THANH` → tất cả cell readonly. | Happy 🔴 |
| TC-KQ-UI-02 | FR-III-05 / SCR-III-02 / Tab 4 dòng 600 | Verify Tab "KQ kiểm tra" — form điểm + xếp loại + nhận xét | CB_NV_TW. KH-TW-DKT-001 `DA_KET_THUC`, có 5 HV. | URL: `/dao-tao/khoa-hoc/{id}/ket-qua` | 1. Mở SCR-III-02 KH-TW-DKT-001. 2. Click Tab "KQ kiểm tra". 3. Kiểm tra layout. | **LAYOUT**: Toolbar [Import Excel] [Xuất Excel] [Trình KQ] (cb_nv, chỉ enable khi state đủ điều kiện). **TABLE 5 cột nguyên văn dòng 600**: Họ tên / Điểm KT (input number 0-10, step 0.1) / Xếp loại (badge auto: GIOI ≥9 / KHA 7-8.9 / TB 5-6.9 / DAT 5-6.9 / KHONG_DAT <5 — **SPEC-CLARIFY-DT-KQ-03** thang xếp loại nguyên văn vì SRS dòng 600 enum 5 giá trị nhưng không quote ngưỡng) / Nhận xét (textarea 500 ký) / Trạng thái KQ (CHUA_NHAP / DA_NHAP / CHO_DUYET / DA_DUYET / TU_CHOI). **NEGATIVE**: Khi KH `DANG_DIEN_RA` → cell điểm KT readonly. Khi KH `CHO_DUYET_KQ` (sau Trình KQ) → cell readonly. | Happy 🔴 |

---

## B. READ — Điểm danh + KQ

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-001 | FR-III-05 / Outputs dòng 468-477 | Xem Tab Lịch học của KH `DANG_DIEN_RA` — cells render đúng giá trị seed | CB_NV_TW. KH-TW-DDR-001 có 5 HV × 6 buổi = 30 cell, 25 ghi "Có mặt" + 5 "Vắng". | — | 1. Mở Tab Lịch học. 2. Quan sát bảng 2D. | **STATE**: Backend `GET /api/v1/khoa-hoc/{id}/diem-danh`. **UI**: 30 cell hiển thị đúng (25 dấu tick xanh, 5 dấu X đỏ). Cột chuyên cần: 3 HV 100%, 1 HV 83%, 1 HV 67%. **PERSIST**: Reload giữ. | Happy |
| TC-KQ-002 | FR-III-06 / Filter | Tìm KQ theo từ khóa họ tên + lọc ket_qua=DAT | CB_NV_TW. KH-TW-HT-001 `HOAN_THANH` có 10 HV trộn DAT/KHONG_DAT. | từ khóa "Nguyễn", filter ket_qua=DAT | 1. Tab KQ kiểm tra. 2. Search "Nguyễn". 3. Filter `ket_qua=DAT`. | **STATE**: API `?tu_khoa=Nguyễn&ket_qua=DAT`. **UI**: Chỉ HV họ Nguyễn xếp loại DAT trở lên hiển thị. Total count đúng. **PERSIST**: Reload giữ filter. | Happy |
| TC-KQ-003 | FR-III-06 / BR-DATA-07 | Pagination KQ default 20/page | CB_NV_TW. KH có ≥25 KQ. | — | 1. Tab KQ. 2. Quan sát pagination. 3. Click trang 2. | **STATE**: `GET ...?page=1&size=20` → 20 record; trang 2 → 5. **UI**: Pagination "20/page", tổng 25. **PERSIST**: Reload trang 2 giữ. | Happy |

---

## C. CREATE / UPDATE — Điểm danh

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-H-001 | FR-III-05 / dòng 599 | CB NV ghi điểm danh từng cell khi KH `DANG_DIEN_RA` | CB_NV_TW. KH-TW-DDR-001 `DANG_DIEN_RA`, HV-001 chưa điểm danh buổi 3. | cell (HV-001, buổi 3) = "Có mặt" | 1. Tab Lịch học. 2. Click cell (HV-001, buổi 3). 3. Chọn "Có mặt". | **STATE**: UPSERT KET_QUA_HOC_TAP row (hoc_vien_id=001, ngay_diem_danh=buổi 3, diem_danh=Có mặt). AUDIT_LOG hành động='UPDATE'. **UI**: Cell hiện dấu tick xanh + tooltip "Có mặt - cb_nv_tw_01 - HH:mm". Tỷ lệ chuyên cần auto recalc. **PERSIST**: Reload giữ giá trị. | Happy 🔴 |
| TC-KQ-H-002 | FR-III-05 / Bulk attendance | CB NV bulk điểm danh tất cả HV cho 1 buổi (nút "Tất cả có mặt") | CB_NV_TW. KH-TW-DDR-001 `DANG_DIEN_RA`, buổi 4 chưa điểm danh ai. | bulk = "Có mặt" cho 5 HV | 1. Header cột buổi 4 click [Tất cả có mặt]. 2. Confirm. | **STATE**: 5 row UPSERT cùng lúc với diem_danh=Có mặt. AUDIT_LOG 5 entries. **UI**: Cột buổi 4 5 cell xanh. Toast "Đã điểm danh 5 HV". **PERSIST**: Reload. | Happy |
| TC-KQ-H-003 | FR-III-05 / Import Excel | Import Excel kết quả điểm danh + điểm KT (dòng 448-457) | CB_NV_TW. KH-TW-DKT-001 `DA_KET_THUC`. File `kq-template.xlsx` 5 dòng. | file 5 dòng đầy đủ | 1. Tab KQ. 2. [Import Excel]. 3. Upload. 4. Review + Confirm. | **STATE**: 5 row UPSERT KET_QUA_HOC_TAP với diem_kiem_tra. AUDIT_LOG 5 entries. **UI**: Bảng review trước confirm. Toast "Import thành công 5/5". **PERSIST**: Tab KQ +5 record. | Happy |

---

## D. UPDATE — Điểm KT (Tab KQ kiểm tra, chỉ khi `DA_KET_THUC`)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-H-004 | FR-III-05 / dòng 600 | CB NV nhập điểm KT 8.5 cho HV-001 → auto xếp loại "KHA" | CB_NV_TW. KH-TW-DKT-001 `DA_KET_THUC`. HV-001 chưa nhập điểm. | diem_kiem_tra=8.5, nhan_xet="Tốt" | 1. Tab KQ kiểm tra. 2. Cell HV-001 điểm = 8.5. 3. Cell nhận xét = "Tốt". 4. Lưu. | **STATE**: UPDATE KET_QUA_HOC_TAP SET diem_kiem_tra=8.5, xep_loai='KHA' (auto per **SPEC-CLARIFY-DT-KQ-03** thang ngưỡng), nhan_xet='Tốt', trang_thai='DA_NHAP'. AUDIT_LOG. **UI**: Toast OK. Badge xếp loại = KHA xanh dương. **PERSIST**: Reload giữ giá trị. | Happy 🔴 |
| TC-KQ-H-005 | FR-III-05 / dòng 600 | CB NV nhập điểm KT = 9.5 → auto "GIOI" | CB_NV_TW. KH-TW-DKT-001. HV-002. | diem_kiem_tra=9.5 | 1-4 như trên. | **STATE**: xep_loai='GIOI' (≥9). **UI**: Badge GIOI vàng. **PERSIST**: — | Happy |
| TC-KQ-H-006 | FR-III-05 / dòng 600 | CB NV nhập điểm = 4.5 → auto "KHONG_DAT" | CB_NV_TW. HV-003. | diem_kiem_tra=4.5 | 1-4. | **STATE**: xep_loai='KHONG_DAT' (<5). **UI**: Badge KHONG_DAT đỏ. **PERSIST**: — Note: HV này SẼ KHÔNG được cấp chứng nhận khi KH HOAN_THANH (xem FILE 8). | Happy |
| TC-KQ-H-007 | FR-III-05 / dòng 600 | CB NV nhập điểm = 5.0 (boundary) → "DAT" hay "TRUNG_BINH"? | CB_NV_TW. HV-004. | diem_kiem_tra=5.0 | 1-4. | **STATE**: Per **SPEC-CLARIFY-DT-KQ-03** — SRS không quote ngưỡng nguyên văn. Kỳ vọng: 5.0 = DAT (đúng ngưỡng đỗ). **UI**: Badge tùy implementation. **PERSIST**: — Test verify hành vi thực tế. | Edge 🟡 |

---

## E. AT-02 — Trình KQ (UC36 — guard tests)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-S-001 | FR-III-17 / SM-KHOAHOC AT-02 dòng 628 | CB NV [Trình KQ] thành công khi đầy đủ điểm danh + điểm KT → KH `DA_KET_THUC → CHO_DUYET_KQ` | CB_NV_TW. KH-TW-DKT-002 `DA_KET_THUC`. 5 HV đã có đủ điểm danh (6/6 buổi) + đủ điểm KT (5/5 HV). | — | 1. Tab KQ. 2. Click [Trình KQ]. 3. Confirm. | **STATE**: Guard PASS (per dòng 628 + 985). UPDATE KHOA_HOC SET trang_thai='CHO_DUYET_KQ', updated_at, updated_by=cb_nv_tw_01. AUDIT_LOG hành động='SUBMIT_RESULT'. Notify CB_PD cùng cấp (BR-NOTIF-01). **UI**: Toast "Đã trình kết quả phê duyệt" (SRS Gap nguyên văn — **SPEC-CLARIFY-DT-KQ-04**). Badge KH đổi `CHO_DUYET_KQ` (cam). Nút [Trình KQ] disable, nút [Sửa KQ] disable. **PERSIST**: Reload giữ trạng thái. | Happy 🔴 |
| TC-KQ-S-002 | FR-III-17 / Guard điểm danh | [Trình KQ] FAIL khi thiếu điểm danh (1 HV chưa điểm danh buổi 5) | CB_NV_TW. KH-TW-DKT-003 `DA_KET_THUC`. HV-001 chưa điểm danh buổi 5 (4/6 thay vì 6/6). Điểm KT đầy đủ. | — | 1. Click [Trình KQ]. 2. Confirm. | **STATE**: Guard FAIL. KHÔNG UPDATE. **UI**: Toast/dialog "**Cần hoàn tất điểm danh trước khi trình kết quả**" (ERR-KQ-02 — SRS dòng 132 test plan + dòng 628 guard). Highlight HV thiếu điểm danh. **PERSIST**: KH giữ DA_KET_THUC. | Negative 🔴 |
| TC-KQ-S-003 | FR-III-17 / Guard điểm KT | [Trình KQ] FAIL khi thiếu điểm KT (1 HV chưa nhập điểm) | CB_NV_TW. KH-TW-DKT-004 `DA_KET_THUC`. Điểm danh đầy đủ. HV-001 chưa có điểm KT. | — | 1. Click [Trình KQ]. 2. Confirm. | **STATE**: Guard FAIL per dòng 628 "guard: điểm danh + điểm KT đầy đủ". **UI**: Toast "**Cần nhập đủ điểm kiểm tra trước khi trình kết quả**" (ERR-KQ-02 mở rộng — **SPEC-CLARIFY-DT-KQ-05** SRS chỉ ghi "thiếu điểm danh"). **PERSIST**: KH giữ DA_KET_THUC. | Negative 🔴 |
| TC-KQ-S-004 | FR-III-17 / SM invalid | [Trình KQ] FAIL khi KH chưa `DA_KET_THUC` (vd `DANG_DIEN_RA`) | CB_NV_TW. KH-TW-DDR-001 `DANG_DIEN_RA`. | — | 1. Vào SCR-III-02 KH `DANG_DIEN_RA`. 2. Quan sát nút [Trình KQ]. | **STATE**: Nút [Trình KQ] disable hoàn toàn ở Tab KQ (per state guard SM). API direct call → reject. **UI**: Nút disable + tooltip "Khóa học chưa kết thúc". **PERSIST**: — | Negative 🟡 |

---

## F. NEGATIVE / ERROR

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-N-001 | ERR-KQ-01 / dòng 486 | Nhập điểm KT < 0 (vd -1) | CB_NV_TW. KH-TW-DKT-005 `DA_KET_THUC`. | diem_kiem_tra=-1 | 1. Tab KQ. 2. Cell điểm = -1. 3. Lưu. | **STATE**: KHÔNG UPDATE. BE check 0 ≤ điểm ≤ 10. **UI**: Inline "**Điểm kiểm tra phải từ 0 đến 10**" (nguyên văn dòng 486 ERR-KQ-01). **PERSIST**: Cell giữ giá trị cũ. | Negative 🔴 |
| TC-KQ-N-002 | ERR-KQ-01 / dòng 486 | Nhập điểm KT > 10 (vd 11) | CB_NV_TW. KH-TW-DKT-005. | diem_kiem_tra=11 | 1-3. | **STATE**: KHÔNG UPDATE. **UI**: Inline ERR-KQ-01. **PERSIST**: Cell giữ giá trị cũ. | Negative 🔴 |
| TC-KQ-N-003 | FR-III-05 / dòng 600 invariant | Sửa điểm KT khi KH đã `CHO_DUYET_KQ` (sau Trình KQ) | CB_NV_TW. KH-TW-CDKQ-001 `CHO_DUYET_KQ`. | thử nhập điểm mới | 1. Tab KQ. 2. Click cell điểm. | **STATE**: Cell readonly per dòng 600 "Chỉ cho sửa khi `DA_KET_THUC`". UPDATE qua API trực tiếp → 409 Conflict. **UI**: Cell disable, tooltip "Đã trình duyệt — không sửa được". **PERSIST**: — | Negative 🔴 |
| TC-KQ-N-004 | FR-III-05 / dòng 599 invariant | Sửa điểm danh khi KH đã `DA_KET_THUC` | CB_NV_TW. KH-TW-DKT-006 `DA_KET_THUC`. | thử đổi cell điểm danh | 1. Tab Lịch học. 2. Click cell. | **STATE**: Cell readonly per dòng 599 "Chỉ cho sửa khi `DANG_DIEN_RA`". **UI**: Cell disable. **PERSIST**: — | Negative 🟡 |
| TC-KQ-N-005 | FR-III-05 / Import Excel ERR-KQ-02 dòng 487 | Import Excel sai format (file .xlsx nhưng thiếu cột bắt buộc) | CB_NV_TW. KH-TW-DKT-005 `DA_KET_THUC`. File `kq-broken.xlsx` thiếu cột "Điểm KT". | file thiếu cột | 1. Tab KQ. 2. Import. 3. Upload. | **STATE**: KHÔNG INSERT. **UI**: Modal review "**File không đúng định dạng mẫu**" (nguyên văn dòng 487 ERR-KQ-02). **PERSIST**: Count không đổi. | Negative |
| TC-KQ-N-006 | FR-III-05 / Import ERR-KQ-03 dòng 488 | Import Excel với mã HV không tồn tại trong KH | CB_NV_TW. KH-TW-DKT-005. File `kq-bad-mahv.xlsx` 3 dòng (2 mã HV hợp lệ + 1 mã HV không thuộc KH). | file 3 dòng | 1. Import. 2. Review. | **STATE**: 2 row INSERT + 1 row reject. **UI**: Bảng review hiển thị 2 OK + 1 LỖI dòng "**Mã học viên dòng {N} không tồn tại**" (nguyên văn dòng 488 ERR-KQ-03). **PERSIST**: 2 record. | Negative 🟡 |

---

## G. PERMISSION

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-P-001 | FR-III-05 / Permission Matrix dòng 163 | CB_PD không có quyền nhập điểm danh / điểm KT (chỉ READ) | CB_PD_TW (cb_pd_tw_01). KH-TW-DDR-001 `DANG_DIEN_RA`. | — | 1. Tab Lịch học. 2. Click cell điểm danh. | **STATE**: — **UI**: Cell readonly. KHÔNG có nút [+ Cấu hình lịch học]. KHÔNG có nút [Trình KQ] (chỉ CB NV — Permission Matrix dòng 163 KET_QUA Create = CB NV). **PERSIST**: — | Negative |
| TC-KQ-P-002 | FR-III-05 / BR-AUTH-08 | CB_NV_DP cố nhập điểm vào KH thuộc đơn vị TW (cross-cấp) | CB_NV_DP (cb_nv_dp_01). KH-TW-DKT-007 `DA_KET_THUC` thuộc đơn vị TW. | API direct PUT điểm | 1. CB_NV_DP cố call API PUT điểm KT. | **STATE**: KHÔNG UPDATE. BE check don_vi_id mismatch → 403. **UI**: HTTP 403. **PERSIST**: KQ không đổi. | Negative |
| TC-KQ-P-003 | FR-III-05 / DN/NHT view-only | DN xem KQ học của HV mình cử qua Cổng PLQG (read-only) | DN (dn_01). DN đã cử HV-001 vào KH-TW-HT-001 `HOAN_THANH`. | URL Cổng `/cong/dao-tao/lich-su` | 1. DN vào "Lịch sử đào tạo". | **STATE**: API `GET /api/cong/dao-tao/ket-qua?dn_id=...`. **UI**: Hiển thị KQ của HV mà DN cử (điểm + xếp loại + chứng nhận). KHÔNG cho sửa. **PERSIST**: — Note: SRS dòng 552 cite "FR-III-06 read-only public" implies DN can search results — **SPEC-CLARIFY-DT-KQ-06** xác nhận scope DN view-only. | Edge 🟡 |

---

## H. EDGE & BOUNDARY

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-E-001 | FR-III-05 / Boundary | Điểm KT = 0 (boundary dưới) | CB_NV_TW. KH-TW-DKT-005. HV-005. | diem_kiem_tra=0 | 1-3. | **STATE**: UPDATE OK với điểm=0, xep_loai='KHONG_DAT'. **UI**: OK. **PERSIST**: Reload giữ. | Edge |
| TC-KQ-E-002 | FR-III-05 / Boundary | Điểm KT = 10 (boundary trên) | CB_NV_TW. HV-006. | diem_kiem_tra=10 | 1-3. | **STATE**: UPDATE OK với điểm=10, xep_loai='GIOI'. **UI**: Badge GIOI. **PERSIST**: — | Edge |
| TC-KQ-E-003 | FR-III-05 / Boundary | Điểm KT lẻ 0.5 (vd 7.5) | CB_NV_TW. HV-007. | diem_kiem_tra=7.5 | 1-3. | **STATE**: UPDATE OK với điểm=7.5, xep_loai='KHA'. **UI**: OK. **PERSIST**: — | Edge |
| TC-KQ-E-004 | FR-III-05 / Half-class điểm danh | Điểm danh nửa lớp buổi 1, nửa lớp buổi 2 — verify chuyên cần auto recalc | CB_NV_TW. KH-TW-DDR-002 `DANG_DIEN_RA`, 6 HV × 6 buổi. Điểm danh: HV 1-3 có mặt buổi 1 + vắng buổi 2; HV 4-6 ngược lại. | matrix điểm danh | 1. Lưu điểm danh từng cell. 2. Quan sát cột chuyên cần. | **STATE**: 6 KET_QUA_HOC_TAP row được UPSERT đúng. **UI**: HV 1-3 chuyên cần buổi 1 100% + buổi 2 0%; HV 4-6 ngược. Tỷ lệ tổng auto recalc per HV. **PERSIST**: Reload giữ. | Edge |
| TC-KQ-E-005 | FR-III-05 / EC-03 dòng 405 | Concurrency — 2 CB NV cùng nhập điểm cho cùng HV | CB_NV_TW user A và user B (cb_nv_tw_02). KH-TW-DKT-008 `DA_KET_THUC`. HV-001 điểm chưa nhập. | A: 8.0; B: 7.5 | 1. A và B mở Tab KQ cùng lúc. 2. A lưu trước (điểm=8.0). 3. B lưu sau (điểm=7.5). | **STATE**: A INSERT thành công. B BE check updated_at conflict → reject (per EC-03 dòng 405 + BR-EC-01 row-lock). **UI**: A toast OK. B toast/error "**Khóa học đang được cập nhật bởi người khác**" (nguyên văn dòng 405 ERR-DK-DT-04 — adapt cho UC24). **PERSIST**: KQ HV-001 = 8.0 (A's value). | Edge 🟡 |
| TC-KQ-E-006 | FR-III-05 / Tỷ lệ chuyên cần threshold | HV chuyên cần <50% có được nhập điểm KT không? | CB_NV_TW. KH-TW-DKT-009 `DA_KET_THUC`. HV-001 chuyên cần 33% (2/6 buổi). | diem_kiem_tra=8 | 1. Tab KQ. 2. Cell HV-001 điểm = 8. 3. Lưu. | **STATE**: SRS không có rule chặn nhập điểm theo chuyên cần — **SPEC-CLARIFY-DT-KQ-07**: BA confirm có chặn không (vd ngưỡng 50% chuyên cần mới được KT). Mặc định: cho phép nhập, xếp loại theo điểm. **UI**: Tùy implementation. **PERSIST**: — | Edge 🟡 |

---

## I. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KQ-E-007 | FR-III-17 / Empty edge | KH `DA_KET_THUC` 0 HV ĐK — có cho [Trình KQ] không? | cb_nv_tw_01. KH "KH-EMPTY-HV" `DA_KET_THUC`, 0 DANG_KY DA_DUYET. | — | 1. Tab KQ. 2. Quan sát button [Trình KQ]. 3. Click nếu có. | **STATE**: SRS Gap. SPEC-CLARIFY-DT-KQ-08: KH 0 HV thì có cần [Trình KQ] để chuyển HOAN_THANH? Default: cho phép trình + auto duyệt = HOAN_THANH với 0 CN. **UI**: Tùy logic. **PERSIST**: Mark BA confirm. | Edge 🟡 |
| TC-KQ-E-008 | FR-III-05 / Idempotency import | Import Excel KQ 2 lần với cùng file (5 dòng) — verify upsert idempotent | cb_nv_tw_01. KH-TW-DKT-005 `DA_KET_THUC`. File `kq.xlsx` 5 dòng đã import 1 lần thành công. | Import lại file giống hệt | 1. Import lần 1 → 5 row INSERT. 2. Import lại file giống hệt. 3. Query AUDIT_LOG. | **STATE**: Import lần 2 → UPDATE (UPSERT theo `khoa_hoc_id + hoc_vien_id`) — KHÔNG duplicate row. AUDIT_LOG: 5 entry CREATE lần 1 + 5 entry UPDATE (du_lieu_cu=du_lieu_moi nếu giống) lần 2. **UI**: Toast lần 2: "Cập nhật 5/5 dòng" (không "Thêm mới"). **PERSIST**: Count KET_QUA_HOC_TAP không tăng sau lần 2. SPEC-CLARIFY-DT-KQ-09 nguyên văn message lần 2. | Edge 🟡 |
| TC-KQ-N-007 | FR-III-05 / Special character điểm danh nhận xét | Nhập nhận xét chứa Unicode + ký tự đặc biệt + dài | cb_nv_tw_01. KH `DA_KET_THUC`. HV-008. | nhan_xet="Học sinh giỏi 🌟 — đạt yêu cầu cao. Đề nghị phát triển lĩnh vực 'Hợp đồng' & <khuyến khích> tham gia Khóa học nâng cao." (180 ký) | 1. Cell nhận xét HV-008. 2. Paste text. 3. Lưu. | **STATE**: UPDATE OK với nhan_xet (text NVARCHAR). **UI**: Cell hiển thị literal (HTML escape, không exec). Tooltip hover full text. **PERSIST**: Reload giữ nguyên Unicode + emoji. | Edge 🟢 |

---

## SPEC-CLARIFY tickets bổ sung (file này)

| ID | Mô tả | Action |
|----|-------|--------|
| SPEC-CLARIFY-DT-KQ-01 | Option điểm danh — SRS dòng 434 nói boolean 2 trạng thái (Có mặt/Vắng), nhưng nghiệp vụ thường có thêm "Vắng có phép". Cần xác nhận enum đúng | BA confirm enum diem_danh |
| SPEC-CLARIFY-DT-KQ-02 | Công thức tỷ lệ chuyên cần — SRS không quote công thức. Kỳ vọng `(Có mặt + Vắng có phép) / Tổng buổi × 100` | BA confirm formula |
| SPEC-CLARIFY-DT-KQ-03 | Thang xếp loại theo điểm — SRS dòng 600 enum `GIOI/KHA/TRUNG_BINH/DAT/KHONG_DAT` nhưng KHÔNG quote ngưỡng. Kỳ vọng GIOI≥9, KHA 7-8.9, TB 5-6.9, DAT 5-6.9, KHONG_DAT<5 | BA confirm thresholds + xử lý overlap TB vs DAT |
| SPEC-CLARIFY-DT-KQ-04 | Toast nguyên văn cho "Đã trình kết quả phê duyệt" — SRS Gap | BA confirm copy |
| SPEC-CLARIFY-DT-KQ-05 | Guard "thiếu điểm KT" — SRS dòng 132 ERR-KQ-02 chỉ ghi "thiếu điểm danh", nhưng dòng 628 nói guard cả "điểm danh + điểm KT". Cần error code riêng cho thiếu điểm KT? | BA confirm error codes |
| SPEC-CLARIFY-DT-KQ-06 | DN/NHT có quyền view KQ học của HV mình cử qua Cổng — SRS không quote rõ scope | BA confirm DN read-only |
| SPEC-CLARIFY-DT-KQ-07 | Có chặn nhập điểm KT khi chuyên cần dưới ngưỡng (vd <50%)? SRS không có rule | BA confirm có/không có rule chuyên cần threshold |
| SPEC-CLARIFY-DT-KQ-08 | KH `DA_KET_THUC` 0 HV — flow Trình KQ có cần thiết? Default cho phép tiến HOAN_THANH với 0 CN | BA confirm |
| SPEC-CLARIFY-DT-KQ-09 | Idempotency import Excel KQ — message nguyên văn cho UPSERT lần 2 ("Cập nhật 5/5" vs "Đã tồn tại") | BA confirm |
| SPEC-CLARIFY-DT-A6-02 | SRS có 2 tên entity cho cùng concept — `KET_QUA_HOC_TAP` (FR-III-05 lines 445/463/496) và `KET_QUA_DAO_TAO` (entity overview §4 line 1203). File này dùng `KET_QUA_HOC_TAP` theo FR-III-05 chính thức. Cần BA confirm tên canonical. | BA confirm canonical name |

---

## A7 Filter Notes

- **KEEP all 34 TC:** Mọi TC observable qua UI Tab Lịch học/KQ + network. Concurrency TC-KQ-E-005 thực thi 2 tabs/sessions parallel. TC-KQ-E-006 chuyên cần threshold KEEP nhưng pending BA SPEC-CLARIFY-DT-KQ-07 (downgrade priority nếu BA confirm KHÔNG có rule).

---

## Tóm tắt file

- **Tổng TC**: 34 active (post-A4 + A6 reconciled).
- **Section count**:
  - A. UI = 2 (TC-KQ-UI-01, 02)
  - B. READ = 3 (TC-KQ-001..003)
  - C. CREATE/UPDATE điểm danh = 3 (TC-KQ-H-001..003)
  - D. UPDATE điểm KT = 4 (TC-KQ-H-004..007)
  - E. AT-02 Trình KQ = 4 (TC-KQ-S-001..004)
  - F. NEGATIVE = 6 (TC-KQ-N-001..006)
  - G. PERMISSION = 3 (TC-KQ-P-001..003)
  - H. EDGE & BOUNDARY = 6 (TC-KQ-E-001..006 — boundary 0/10/0.5, half-class, concurrency, chuyên cần threshold)
  - I. EDGE A4 = 3 (TC-KQ-E-007, E-008, N-007)
  - **Total**: 34 active (note: 7 TCs → 27 estimate trong plan, vượt do split điểm danh/điểm KT + A4 edge).

> **A7-filter recommendation**: giữ tất cả 34 TC. Cân nhắc downgrade priority cho TC-KQ-E-006 (chuyên cần threshold pending SPEC-CLARIFY-DT-KQ-07) nếu BA confirm KHÔNG có rule.
> **SPEC-CLARIFY active**: 9 (DT-KQ-01..09).
