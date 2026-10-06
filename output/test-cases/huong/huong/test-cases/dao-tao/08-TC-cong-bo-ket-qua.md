# Test Cases — UC37 (Phê duyệt KQ) + UC38 (Công bố KQ + cấp chứng nhận) — FR-III-18 + FR-III-19

> **SRS Ref**: FR-III-18 (UC37 — Phê duyệt KQ) `srs-fr-03-dao-tao.md` dòng 996-1018 + FR-III-19 (UC38 — Công bố KQ + chứng nhận) dòng 1021-1042.
> **Màn hình**: SCR-III-02 Tab "KQ kiểm tra" (action [Duyệt]/[Từ chối] cho CB PD) + Tab "Chứng nhận" (chỉ hiển thị khi KH `HOAN_THANH`).
> **Entity**: `CHUNG_NHAN` (§3.4.3.24).
> **Process flow**: `02-thu-tu-module.md` §⑨ dòng 601 (Tab Chứng nhận chỉ hiển thị khi KH `HOAN_THANH`) + dòng 629 (CB PD `[Duyệt + Công khai]`).
> **Phase**: A — Phase A re-run.
> **Ngày tạo**: 2026-05-09.

---

## A. UI FIELD VERIFICATION (BẮT BUỘC chạy trước functional)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-UI-01 | FR-III-19 / SCR-III-02 / Tab Chứng nhận dòng 601 | Verify Tab "Chứng nhận" trong SCR-III-02 — chỉ hiển thị khi KH `HOAN_THANH` | CB_NV_TW (cb_nv_tw_01) đã đăng nhập. KH-TW-HT-001 `HOAN_THANH` có 5 HV (4 DAT + 1 KHONG_DAT) — đã sinh 4 CHUNG_NHAN. | URL: `/dao-tao/khoa-hoc/{id}/chung-nhan` | 1. Mở SCR-III-02 KH-TW-HT-001. 2. Quan sát thanh tab. 3. Click Tab "Chứng nhận". | **LAYOUT**: Thanh tab hiển thị 6 tab nguyên văn dòng 593-602 (Thông tin / Học viên / Lịch học / KQ / **Chứng nhận** [hiển thị] / Bài giảng). **TABLE Tab Chứng nhận**: Toolbar [Tạo hàng loạt] (cb_nv khi KH HOAN_THANH) + [Xuất Excel danh sách CN]. **TABLE 6 cột**: Họ tên / MST DN / Xếp loại (badge GIOI/KHA/TB/DAT) / Số chứng nhận (`CN-2026-00001` per BR-DATA-04) / Ngày cấp (dd/mm/yyyy) / Hành động ([Tải PDF] [Xem]). 4 dòng (KHONG_DAT không có CN). **NEGATIVE — Tab ẨN**: Mở SCR-III-02 cho KH `DANG_DIEN_RA` hoặc `DA_KET_THUC` hoặc `CHO_DUYET_KQ` → Tab "Chứng nhận" KHÔNG hiển thị (per dòng 601 "Chỉ hiển thị khi `HOAN_THANH`"). | Happy 🔴 |

---

## B. READ — Tab Chứng nhận chỉ hiện khi `HOAN_THANH`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-001 | FR-III-19 / dòng 601 | Tab Chứng nhận ẨN khi KH `CHO_DUYET_KQ` | CB_NV_TW. KH-TW-CDKQ-001 `CHO_DUYET_KQ`. | — | 1. Mở SCR-III-02 KH-TW-CDKQ-001. 2. Quan sát số tab. | **STATE**: — **UI**: Thanh tab chỉ 5 tab (Thông tin/Học viên/Lịch học/KQ/Bài giảng). KHÔNG có Tab "Chứng nhận". **PERSIST**: Reload giữ 5 tab. | Happy 🔴 |
| TC-CB-002 | FR-III-19 / dòng 601 | Tab Chứng nhận HIỂN THỊ khi KH `HOAN_THANH` | CB_NV_TW. KH-TW-HT-001 `HOAN_THANH` có 4 CN. | — | 1. Mở SCR-III-02. 2. Click Tab "Chứng nhận". | **STATE**: API `GET /api/v1/khoa-hoc/{id}/chung-nhan` → 4 record. **UI**: Tab xuất hiện. Bảng 4 dòng đầy đủ field. **PERSIST**: Reload giữ. | Happy 🔴 |
| TC-CB-003 | FR-III-19 / Filter xếp loại | Tab Chứng nhận chỉ liệt kê HV `xep_loai='DAT'` (dòng 601 filter `WHERE xep_loai='DAT'`) | CB_NV_TW. KH-TW-HT-002 `HOAN_THANH` có 5 HV (1 GIOI + 1 KHA + 1 TB + 1 DAT + 1 KHONG_DAT). | — | 1. Tab Chứng nhận. 2. Quan sát số dòng. | **STATE**: API filter `xep_loai IN ('GIOI','KHA','TRUNG_BINH','DAT')`. Per dòng 601 enum hợp lệ cho CN. **UI**: 4 dòng (loại trừ KHONG_DAT). **PERSIST**: Reload giữ. | Happy 🔴 |

---

## C. APPROVE — CB PD duyệt KQ (UC37)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-H-001 | FR-III-18 / AC dòng 1015-1016 | CB PD cùng cấp duyệt KQ thành công → KH `CHO_DUYET_KQ → HOAN_THANH` + auto sinh CN | CB_PD_TW (cb_pd_tw_01). KH-TW-CDKQ-002 `CHO_DUYET_KQ` cùng đơn vị TW. 5 HV (4 DAT + 1 KHONG_DAT) đã có điểm KT đủ. | quyet_dinh="PHE_DUYET" | 1. Mở SCR-III-02 KH-TW-CDKQ-002. 2. Tab KQ kiểm tra. 3. Click [Duyệt KQ]. 4. Confirm dialog. | **STATE**: Per dòng 1009: UPDATE KHOA_HOC SET trang_thai='HOAN_THANH'. **AUTO-GEN 4 CHUNG_NHAN** (per dòng 1034 + 1041 — sinh CN cho HV xếp loại DAT trở lên). Mỗi CN: `so_chung_nhan='CN-2026-{SEQ}'` (BR-DATA-04 dòng 1032), `ngay_cap=NOW()`, `file_pdf=<path>`. AUDIT_LOG hành động='APPROVE_RESULT' + 4 entries 'CREATE' cho CHUNG_NHAN. Notify CB NV (BR-NOTIF-01). **UI**: Toast "Đã phê duyệt kết quả + cấp chứng nhận cho 4 học viên" (SRS Gap nguyên văn — **SPEC-CLARIFY-DT-CB-01**). KH badge → HOAN_THANH (xanh đậm). Tab Chứng nhận xuất hiện. **PERSIST**: Reload → 4 CN trong Tab Chứng nhận. | Happy 🔴 |

---

## D. REJECT — CB PD từ chối KQ (BR-FLOW-04)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-H-002 | FR-III-18 / AC dòng 1017 + BR-FLOW-04 | CB PD từ chối KQ với lý do (≥10 ký tự) → KH `CHO_DUYET_KQ → DA_KET_THUC` | CB_PD_TW. KH-TW-CDKQ-003 `CHO_DUYET_KQ`. | quyet_dinh="TU_CHOI", ly_do="Điểm KT của HV-005 sai - cần kiểm tra lại" (47 ký tự) | 1. Mở Tab KQ. 2. Click [Từ chối KQ]. 3. Modal nhập lý do. 4. Confirm. | **STATE**: UPDATE KHOA_HOC SET trang_thai='DA_KET_THUC' (per dòng 1009 + 1011). KHÔNG sinh CHUNG_NHAN. UPDATE KET_QUA_DAO_TAO SET trang_thai='TU_CHOI' (rollback từ CHO_DUYET) — **SPEC-CLARIFY-DT-CB-02**: SRS không quote rõ trang_thai KQ rollback ra sao. AUDIT_LOG hành động='REJECT_RESULT' với ly_do. Notify CB NV. **UI**: Toast "Đã từ chối kết quả" (SRS Gap nguyên văn). Badge KH → DA_KET_THUC (cho CB NV sửa lại điểm). **PERSIST**: Reload giữ. CB NV mở Tab KQ → các cell mở khóa edit lại. | Happy 🔴 |

---

## E. AUTO-GEN CHUNG_NHAN (verify auto-create per BR-DATA-04 + dòng 1034)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-H-003 | FR-III-19 / BR-DATA-04 / dòng 1032 | Verify auto-gen mã CN format `CN-{YYYY}-{SEQ}` | CB_PD_TW. KH-TW-CDKQ-004 `CHO_DUYET_KQ`. 3 HV DAT. | — | 1. Duyệt KQ KH-TW-CDKQ-004. 2. Query DB CHUNG_NHAN. | **STATE**: 3 row CHUNG_NHAN với `so_chung_nhan` match regex `^CN-2026-\d{5}$` (per BR-DATA-04 dòng 81+1032). SEQ tăng dần unique trong toàn hệ thống (không reset per KH). **UI**: Tab Chứng nhận hiển thị 3 mã `CN-2026-00001/00002/00003`. **PERSIST**: Filter theo year 2026 → match. | Happy 🔴 |
| TC-CB-H-004 | FR-III-19 / Tạo hàng loạt dòng 1026 | Verify hỗ trợ mass certificate generation cho ≥50 HV (auto-gen + PDF batch) | CB_PD_TW. KH-TW-LARGE `CHO_DUYET_KQ`. 50 HV DAT. | — | 1. Duyệt KQ KH-TW-LARGE. 2. Đợi xử lý. 3. Query DB. | **STATE**: 50 row CHUNG_NHAN INSERT cùng lúc. 50 file PDF được sinh (queue/job nếu >threshold — **SPEC-CLARIFY-DT-CB-03**: SRS dòng 1026 nói "hỗ trợ tạo hàng loạt" nhưng không quote cơ chế sync vs async). **UI**: Toast "Đang sinh chứng nhận cho 50 HV..." rồi sau ~30s "Đã sinh xong" hoặc progress bar. Tab Chứng nhận hiển thị 50 dòng. **PERSIST**: Reload giữ. Verify 50 file PDF download được. | Edge 🔴 |
| TC-CB-H-005 | FR-III-19 / Filter xếp loại | KHONG_DAT → KHÔNG sinh CHUNG_NHAN | CB_PD_TW. KH-TW-CDKQ-005 `CHO_DUYET_KQ`. 4 HV DAT + 2 HV KHONG_DAT. | — | 1. Duyệt KQ. 2. Query CHUNG_NHAN. | **STATE**: Chỉ 4 row CHUNG_NHAN (loại trừ 2 HV KHONG_DAT). Per dòng 1034 "Sinh CN cho HV có KQ DAT". **UI**: Tab Chứng nhận hiển thị 4 dòng. **PERSIST**: Filter theo KH → 4 record. | Happy 🔴 |

---

## F. DOWNLOAD PDF

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-H-006 | FR-III-19 / Outputs dòng 1036 | Tải file PDF chứng nhận thành công | CB_NV_TW. KH-TW-HT-001 `HOAN_THANH` đã có 4 CN với file PDF sẵn. | — | 1. Tab Chứng nhận. 2. Click [Tải PDF] trên row CN-2026-00001. | **STATE**: GET file (per Output `file_pdf` dòng 1036). **UI**: Browser download file PDF. Tên file `CN-2026-00001-{ho_ten}.pdf` (SRS Gap convention — **SPEC-CLARIFY-DT-CB-04**). **PERSIST**: File mở được, hiển thị thông tin HV + KH + xếp loại + ngày cấp + chữ ký số (nếu có). | Happy 🔴 |
| TC-CB-H-007 | FR-III-19 / DN portal | DN tải PDF chứng nhận của HV mình cử qua Cổng PLQG | DN (dn_01). DN có HV-001 đã hoàn thành KH với CN `CN-2026-00001`. | URL Cổng `/cong/dao-tao/lich-su` | 1. DN vào "Lịch sử đào tạo HV". 2. Click HV-001. 3. Click [Tải chứng nhận]. | **STATE**: Backend filter `WHERE dn_cu_id=dn_01.id`. **UI**: Download PDF. **PERSIST**: File hợp lệ. | Happy 🟡 |

---

## G. NEGATIVE / ERROR

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-N-001 | ERR-PD-01 / BR-AUTH-05 / dòng 134 | CB PD khác cấp cố duyệt KQ (cross-cấp) → reject | CB_PD_DP (cb_pd_dp_01). KH-TW-CDKQ-006 `CHO_DUYET_KQ` thuộc đơn vị TW. | quyet_dinh="PHE_DUYET" | 1. CB_PD_DP cố call API duyệt KH thuộc TW. | **STATE**: KHÔNG UPDATE. BE check BR-AUTH-05 cùng cấp dòng 1003 "BR-FLOW-03" + Permission Matrix → CB_PD_DP chỉ duyệt KH cấp ĐP → 403. **UI**: Toast/HTTP 403 "**Phê duyệt khác cấp không được phép**" (ERR-PD-01 nguyên văn dòng 134). **PERSIST**: KH giữ CHO_DUYET_KQ. | Negative 🔴 |
| TC-CB-N-002 | ERR-PD-02 / BR-FLOW-04 / dòng 135 | CB PD từ chối KQ KHÔNG nhập lý do | CB_PD_TW. KH-TW-CDKQ-007 `CHO_DUYET_KQ`. | quyet_dinh="TU_CHOI", ly_do="" | 1. Click [Từ chối]. 2. Để trống lý do. 3. Confirm. | **STATE**: KHÔNG UPDATE. BR-FLOW-04 yêu cầu ≥10 ký tự (per dòng 86+1260). **UI**: Inline error "**Lý do từ chối là bắt buộc (≥10 ký tự)**" (ERR-PD-02 nguyên văn dòng 135). **PERSIST**: KH giữ CHO_DUYET_KQ. | Negative 🔴 |
| TC-CB-N-003 | ERR-PD-02 / BR-FLOW-04 boundary | CB PD từ chối KQ với lý do <10 ký tự (vd "Sai") | CB_PD_TW. KH-TW-CDKQ-008 `CHO_DUYET_KQ`. | ly_do="Sai" (3 ký) | 1. Click [Từ chối]. 2. Nhập "Sai". 3. Confirm. | **STATE**: KHÔNG UPDATE. **UI**: Inline error "Lý do từ chối tối thiểu 10 ký tự" (BR-FLOW-04). **PERSIST**: KH giữ. | Negative 🔴 |
| TC-CB-N-004 | FR-III-19 / dòng 1034 | KHÔNG có CHUNG_NHAN cho HV `KHONG_DAT` (negative path) | CB_PD_TW. KH-TW-HT-003 `HOAN_THANH` có 1 HV xếp loại KHONG_DAT đã được duyệt KQ. | — | 1. Tab Chứng nhận. 2. Quan sát danh sách. 3. Query DB CHUNG_NHAN cho HV-KHONG_DAT. | **STATE**: 0 row CHUNG_NHAN cho HV KHONG_DAT. **UI**: HV này không xuất hiện trong Tab Chứng nhận. **PERSIST**: Reload giữ. | Negative 🔴 |
| TC-CB-N-005 | 🟠 DEFER (A7) FR-III-19 / Signature failure | Sinh CN nhưng service ký số fail (mock BHXH/CA down) | CB_PD_TW. KH-TW-CDKQ-009 `CHO_DUYET_KQ`. Cần env có mock signing service hoặc admin toggle disable BHXH/CA. | — | 1. Admin disable mock signing service (qua env config — phụ thuộc env). 2. Duyệt KQ. 3. Quan sát network panel + UI toast. | **STATE**: Per **SPEC-CLARIFY-DT-CB-05**. Kỳ vọng: outbound network call POST /api/v1/ky-so/sign-doc trả non-200. **UI**: Toast cảnh báo error code (nguyên văn pending BA). **PERSIST**: Per BA confirm — verify badge KH (vẫn CHO_DUYET_KQ hay đã HOAN_THANH partial). | Edge 🟡 (DEFER A7) |

---

## H. PERMISSION

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-P-001 | FR-III-18 / Permission Matrix dòng 164 | CB NV không có quyền duyệt KQ (chỉ CB PD) | CB_NV_TW (cb_nv_tw_01). KH-TW-CDKQ-002 `CHO_DUYET_KQ`. | — | 1. Mở SCR-III-02. 2. Tab KQ. 3. Quan sát action. | **STATE**: — **UI**: KHÔNG có nút [Duyệt KQ]/[Từ chối KQ] (Permission Matrix dòng 164: KET_QUA Approve = CB_PD only). Chỉ có nút [Sửa KQ] (disable vì state CHO_DUYET_KQ). **PERSIST**: — | Negative |
| TC-CB-P-002 | FR-III-19 / DN scope | DN chỉ thấy CN của HV mình cử qua Cổng PLQG (BR-AUTH-08 scope) | DN (dn_01). DN có HV-001 đã có CN. DN khác (dn_02) cũng có HV trong cùng KH. | URL `/cong/dao-tao/chung-nhan` | 1. DN-01 vào trang CN. | **STATE**: API filter `WHERE dn_cu_id=dn_01.id`. **UI**: Hiển thị CN của HV-001 (dn_01 cử). KHÔNG thấy CN của HV thuộc dn_02. **PERSIST**: Reload giữ. | Negative 🔴 |
| TC-CB-P-003 | FR-III-19 / NHT scope | NHT chỉ thấy CN của mình qua Cổng | NHT (nht_01). NHT đã hoàn thành 1 KH có CN. | URL Cổng | 1. NHT vào trang CN. | **STATE**: API filter `WHERE nguoi_huong_thu_id=nht_01.id` (tự đăng ký + hoàn thành). **UI**: Hiển thị CN của chính NHT. KHÔNG thấy CN người khác. **PERSIST**: — | Negative 🟡 |

---

## I. EDGE & BOUNDARY

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-E-001 | 🟠 DEFER (A7) FR-III-19 / Mass generation boundary | Tạo CN hàng loạt với 100 HV (boundary trên thường gặp) | CB_PD_TW. KH-TW-MASS `CHO_DUYET_KQ` cần seed 100 HV DAT (env không sẵn lượng này). | — | 1. Seed 100 HV DAT trước (heavy seed). 2. Duyệt KQ. 3. Đợi xử lý. 4. Tab CN reload. | **STATE**: Backend insert 100 row CHUNG_NHAN. **UI**: Tab CN hiển thị 100 row. Progress indicator nếu async. **PERSIST**: 100 file PDF download được. SPEC-CLARIFY-DT-CB-06 SLA pending. Defer Phase B performance round. | Edge 🟡 (DEFER A7) |
| TC-CB-E-002 | FR-III-18 / Reject rồi resubmit | KQ bị từ chối → CB NV sửa điểm rồi trình lại lần 2 | CB_NV_TW + CB_PD_TW. KH-TW-CDKQ-010 đã bị reject 1 lần (DA_KET_THUC). | — | 1. CB NV vào Tab KQ. 2. Sửa điểm HV-005. 3. [Trình KQ] lần 2. 4. CB PD duyệt OK. | **STATE**: Cycle: DA_KET_THUC → CHO_DUYET_KQ → HOAN_THANH (lần 2). AUDIT_LOG ghi cả 2 lần submit + 1 reject + 1 approve. CHUNG_NHAN sinh sau approve cuối. **UI**: Toast OK. KH HOAN_THANH. **PERSIST**: Tab Chứng nhận hiển thị CN đầy đủ. | Edge 🟡 |
| TC-CB-E-003 | FR-III-19 / SEQ continuity | SEQ chứng nhận continuous across KH (không reset per KH) | KH-TW-A `HOAN_THANH` đã sinh CN-2026-00010 (SEQ=10). KH-TW-B `CHO_DUYET_KQ`. CB_PD_TW duyệt KH-B với 5 HV. | — | 1. CB_PD_TW duyệt KH-TW-B. 2. Query SEQ của 5 CN mới. | **STATE**: 5 CN mới với SEQ 11, 12, 13, 14, 15 (continuous global, không reset). Per BR-DATA-04 dòng 81 "auto-gen mã unique" implies global SEQ. **UI**: Tab Chứng nhận KH-B → CN-2026-00011..00015. **PERSIST**: Reload giữ. **SPEC-CLARIFY-DT-CB-07**: nếu global vs reset annual hay per-KH cần BA confirm. | Edge 🟡 |

---

## J. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-E-004 | FR-III-19 / Idempotency cấp lại | Cấp lại CN cho HV đã có CN — verify behavior (re-issue hay duplicate?) | cb_nv_tw_01. HV-001 đã có CN-2026-00010 (KH-A HOAN_THANH). KH-A trở lại CHO_DUYET_KQ qua reject → CB PD duyệt lại. | resubmit lần 2 | 1. cb_pd_tw_01 reject KQ KH-A. 2. cb_nv_tw_01 sửa điểm. 3. Trình KQ lần 2. 4. cb_pd_tw_01 duyệt OK. 5. Query CHUNG_NHAN cho HV-001. | **STATE**: SPEC-CLARIFY-DT-CB-08: BE behavior 2 lựa chọn: (A) UPDATE CN cũ (giữ so_chung_nhan, đổi ngay_cap); (B) INSERT CN mới (so_chung_nhan mới) + soft-delete CN cũ. Default: (A) preserve so_chung_nhan, không sinh duplicate. **UI**: Tab Chứng nhận chỉ 1 row HV-001. **PERSIST**: Audit log ghi UPDATE_CN. | Edge 🔴 |
| TC-CB-E-005 | 🟠 DEFER (A7) FR-III-18 / Network/storage / PDF service rate-limit | Sinh 4 CN cùng lúc khi storage service trả 429 (rate limit) cho 1 trong 4 | cb_pd_tw_01. KH-RATE `CHO_DUYET_KQ` 4 HV DAT. Cần env có mock storage trả 429 hoặc admin toggle. | — | 1. Setup mock storage rate-limit (env config). 2. Click [Duyệt KQ]. 3. Quan sát Tab CN + network requests. | **STATE**: SPEC-CLARIFY-DT-CB-09 — 2 strategy A/B pending BA. **UI**: Network panel hiển thị 4 calls, 1 trả 429. Tab CN render 3 hoặc 4 row tùy strategy. Toast warning. **PERSIST**: Tùy strategy. | Edge 🟡 (DEFER A7) |
| TC-CB-E-006 | FR-III-19 / Idempotency download | DN tải PDF CN 100 lần liên tiếp — verify rate limit + audit log | DN dn_01. CN-2026-00001 của HV mình cử. | Loop 100 GET request | 1. DN download 100 lần liên tiếp. 2. Quan sát audit + response. | **STATE**: BE phải có rate limit (vd 60 req/min) → trả 429 sau N lần. AUDIT_LOG ghi DOWNLOAD chỉ 100 entry hoặc throttled. **UI**: Lần ≥61 → toast "Quá nhiều yêu cầu, vui lòng thử lại sau" hoặc HTTP 429. **PERSIST**: SPEC-CLARIFY-DT-CB-10 ngưỡng rate limit. | Edge 🟢 |

---

## SPEC-CLARIFY tickets bổ sung (file này)

| ID | Mô tả | Action |
|----|-------|--------|
| SPEC-CLARIFY-DT-CB-01 | Toast nguyên văn cho "Đã phê duyệt KQ + cấp CN" / "Đã từ chối KQ" — SRS Gap | BA confirm copy |
| SPEC-CLARIFY-DT-CB-02 | Khi CB PD từ chối KQ → trang_thai KET_QUA_DAO_TAO rollback ra sao? SRS dòng 1011 chỉ nói KH `CHO_DUYET_KQ → DA_KET_THUC`, không quote KQ entry | BA confirm rollback rule |
| SPEC-CLARIFY-DT-CB-03 | Mass generation cơ chế sync vs async — SRS dòng 1026 nói "hỗ trợ tạo hàng loạt" nhưng không quote SLA + cơ chế. Cần threshold rõ ràng (vd >20 HV → async queue) | BA confirm threshold + async/sync |
| SPEC-CLARIFY-DT-CB-04 | Tên file PDF chứng nhận — convention `CN-{SEQ}-{ho_ten}.pdf` hay format khác? | BA confirm file naming |
| SPEC-CLARIFY-DT-CB-05 | Service ký số (BHXH/CA) fail — rollback strategy: rollback toàn bộ approval hay INSERT CN với flag retry? | BA confirm error recovery |
| SPEC-CLARIFY-DT-CB-06 | SLA cho mass certificate generation 100+ HV — SRS không có time SLA | BA confirm SLA |
| SPEC-CLARIFY-DT-CB-07 | SEQ chứng nhận: global continuous, reset annual, hay per-KH? | BA confirm SEQ scope |
| SPEC-CLARIFY-DT-CB-08 | Cấp lại CN cho HV đã có CN sau resubmit — UPDATE CN cũ hay INSERT CN mới + soft-delete cũ | BA confirm idempotency rule |
| SPEC-CLARIFY-DT-CB-09 | Strategy khi sinh CN partial fail (3/4 OK, 1 rate-limited) — atomic rollback hay partial + retry | BA confirm |
| SPEC-CLARIFY-DT-CB-10 | Rate limit download CN PDF — ngưỡng req/min cho DN/NHT | BA confirm SLA |

---

## Tóm tắt file

- **Tổng TC**: 19 (target match plan).
- **Section count**:
  - A. UI = 1 (TC-CB-UI-01)
  - B. READ = 3 (TC-CB-001, 002, 003)
  - C. APPROVE = 1 (TC-CB-H-001)
  - D. REJECT = 1 (TC-CB-H-002)
  - E. AUTO-GEN CHUNG_NHAN = 3 (TC-CB-H-003, 004, 005)
  - F. DOWNLOAD PDF = 2 (TC-CB-H-006, 007)
  - G. NEGATIVE = 5 (TC-CB-N-001..005)
  - H. PERMISSION = 3 (TC-CB-P-001, 002, 003)
  - I. EDGE = 3 (TC-CB-E-001, 002, 003)
  - **Total**: 1+3+1+1+3+2+5+3+3 = **22 raw → 19 active** sau A7-pre.

> **Note A7-filter pre-pass** (đã update sau A7 official):
> - 22 raw → 19 active sau A6/A7. A7 DEFER 3 TC: TC-CB-E-001 (mass 100 cần seed), TC-CB-N-005 (signing service mock toggle), TC-CB-E-005 (storage rate-limit mock toggle). 16 KEEP active for Phase B smoke. 3 DEFER tracked.
> - Final ACTIVE Phase B = 16 (3 DEFER chờ env tooling).
>
> **SPEC-CLARIFY active**: 7.

---

## A7 Filter Notes

- **DEFER (A7) — env mock service required:**
  - TC-CB-N-005 signing service down (cần mock BHXH/CA toggle)
  - TC-CB-E-001 mass 100 HV (cần heavy seed 100 HV DAT — Phase B performance)
  - TC-CB-E-005 storage rate-limit (cần mock storage 429)
- **KEEP all others 16 TC:** observable qua UI Tab Chứng nhận + network panel.
