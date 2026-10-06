# Test Cases — FR-XI-01 sub: Lifecycle CT (Kích hoạt / Tạm dừng / Tiếp tục / Hoàn thành / Hủy / Rút trình)

> **SRS Ref**: FR-XI-01 sub-actions (Processing — Kích hoạt CT / Tạm dừng / Tiếp tục / Hoàn thành / Hủy / Rút trình), SCR-XI-01 action-bar Tab Thông tin
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: 6 transition của SM-KH-CTHTPL không thuộc CRUD core. Mỗi transition có guard state + audit log.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **Pre-conditions mặc định**: User đã đăng nhập, role phù hợp với action

---

## State Machine quick ref

```
DA_DUYET / DA_CONG_BO --[Kích hoạt]--> DANG_THUC_HIEN
DANG_THUC_HIEN --[Tạm dừng + lý do]--> TAM_DUNG
TAM_DUNG --[Tiếp tục]--> DANG_THUC_HIEN
DANG_THUC_HIEN --[Hoàn thành (CB PD, guard: BC done)]--> HOAN_THANH
DU_THAO --[Hủy + xác nhận]--> HUY
CHO_PHE_DUYET --[Rút trình (người trình)]--> DU_THAO
```

---

## A. KÍCH HOẠT CT — HAPPY + NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LC-001 | FR-XI-01 / Kích hoạt step 1-5 | CB NV kích hoạt CT từ DA_DUYET | cb_nv_tw_01 login. CT-DD01 trạng thái DA_DUYET. | — | 1. Mở chi tiết CT-DD01. 2. Click [Kích hoạt]. 3. Modal xác nhận → OK. | (1) PATCH `/api/v1/.../activate` 200. (3) Trạng thái → DANG_THUC_HIEN. Audit log (BR-DATA-05). | Happy 🔴 |
| TC-LC-002 | FR-XI-01 / Kích hoạt | Kích hoạt từ DA_CONG_BO | cb_nv_tw_01 login. CT-CB01 trạng thái DA_CONG_BO. | — | 1. Click [Kích hoạt]. 2. Confirm. | (3) Trạng thái → DANG_THUC_HIEN. CT vẫn `la_cong_bo=1`. | Happy 🟡 |
| TC-LC-003 | FR-XI-01 / Kích hoạt E2 ERR-XI-01-KH-02 | Kích hoạt khi state ≠ DA_DUYET/DA_CONG_BO | cb_nv_tw_01 login. CT-DT01 trạng thái DU_THAO. | — | 1. Mở chi tiết. | (1) Nút [Kích hoạt] ẩn. Nếu force qua API → reject "CT phải ở Đã duyệt hoặc Đã công bố để kích hoạt" (ERR-XI-01-KH-02). | Negative 🟡 |
| TC-LC-003b | FR-XI-01 / Kích hoạt E1 ERR-XI-01-KH-01 (Codex 2026-05-09) | Kích hoạt CT khi user không có quyền CB NV | cb_pd_tw_01 login (CB PD, KHÔNG có quyền Kích hoạt — srs-fr-15:189 "Kiểm tra quyền CB NV"). CT-DD20 DA_DUYET. | — | 1. Mở chi tiết. 2. Force API PATCH `/activate`. | (1) Nút [Kích hoạt] ẩn với CB PD. Force API → reject "Bạn không có quyền kích hoạt CT" (ERR-XI-01-KH-01, srs-fr-15:199). KHÔNG transition state. | Negative 🟡 |
| TC-LC-003c | FR-XI-01 / Kích hoạt guard "kế hoạch chi tiết" (Codex 2026-05-09 / SPEC-CLARIFY-CT-05) | Kích hoạt CT thiếu kế hoạch chi tiết / đơn vị thực hiện | cb_nv_tw_01 login. CT-DD21 DA_DUYET nhưng chưa có entry "kế hoạch chi tiết / đơn vị thực hiện". | — | 1. Click [Kích hoạt]. | **STATE**: SRS srs-fr-15:191 nguyên văn "Kiểm tra: đã có kế hoạch chi tiết, đơn vị thực hiện" — KHÔNG quote field UI cụ thể. Behavior thực tế cần verify: (a) reject với toast guard cụ thể; (b) cho phép pass với cảnh báo; (c) skip guard. **UI**: Tùy behavior. **PERSIST**: Mark **SPEC-CLARIFY-CT-05** field UI mapping cho guard "kế hoạch chi tiết". | Edge / SPEC 🟡 |

---

## B. TẠM DỪNG / TIẾP TỤC — HAPPY + NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LC-004 | FR-XI-01 / Tạm dừng step 1-6 | Tạm dừng có lý do | cb_pd_tw_01 login. CT-TH01 DANG_THUC_HIEN. | ly_do="Điều chỉnh ngân sách Q3" | 1. [Tạm dừng] + nhập lý do + Lưu. | (3) Trạng thái → TAM_DUNG. Lý do persist (`ly_do_tam_dung`). Audit log. | Happy 🔴 |
| TC-LC-005 | FR-XI-01 / Tạm dừng E3 ERR-XI-01-TD-03 (Codex fix 2026-05-09) | Thiếu lý do tạm dừng | cb_pd_tw_01 login. CT-TH02 DANG_THUC_HIEN. | ly_do="" | 1. [Tạm dừng] → bỏ trống lý do → Submit. | (2) Error inline "Vui lòng nhập lý do tạm dừng" (ERR-XI-01-TD-03, srs-fr-15:226). KHÔNG persist. **Note Codex 2026-05-09:** Bỏ trace `BR-FLOW-04` — BR-FLOW-04 (srs-fr-15:1467-1471) chỉ áp dụng cho hành động **Từ chối** (FR-XI-04, FR-XI-07a), KHÔNG áp dụng Tạm dừng. ERR-XI-01-TD-03 là rule riêng của FR-XI-01 Tạm dừng. | Negative 🔴 |
| TC-LC-006 | FR-XI-01 / Tạm dừng W1 WRN-XI-01-TD-01 | Cảnh báo có đợt BC đang lập | cb_pd_tw_01 login. CT-TH03 có 1 đợt BC trạng thái DANG_LAP_BC. | ly_do="Tạm hoãn" | 1. [Tạm dừng] → nhập lý do → Lưu. | (2) Modal WARNING "CT có đợt báo cáo đang trong quá trình lập. Xác nhận tạm dừng?" (WRN-XI-01-TD-01). Confirm → Trạng thái → TAM_DUNG. | Edge 🟡 |
| TC-LC-007 | FR-XI-01 / Tiếp tục step 1-4 | Tiếp tục từ TAM_DUNG | cb_pd_tw_01 login. CT-TD01 TAM_DUNG. | — | 1. [Tiếp tục] → confirm. | (3) Trạng thái → DANG_THUC_HIEN. Audit log. | Happy 🟡 |
| TC-LC-008 | FR-XI-01 / Tiếp tục E2 ERR-XI-01-TT-02 | Tiếp tục khi không TAM_DUNG | cb_pd_tw_01 login. CT-TH04 DANG_THUC_HIEN. | — | — | (1) Nút [Tiếp tục] ẩn. Force API → reject (ERR-XI-01-TT-02). | Negative 🟢 |
| TC-LC-004b | FR-XI-01 / Tạm dừng CB_NV (Codex 2026-05-09 ROLE-001) | CB_NV tạm dừng CT (per srs-fr-15:213 "CB NV/CB PD") | cb_nv_tw_01 login. CT-TH20 DANG_THUC_HIEN. | ly_do="Điều chỉnh ngân sách" | 1. [Tạm dừng] + nhập lý do + Lưu. | (3) Trạng thái → TAM_DUNG. Lý do persist. Audit log. **Note:** SRS line 213 cho phép CẢ CB_NV và CB_PD — TC bổ sung positive cho CB_NV (TC-LC-004 đã cover CB_PD). | Happy 🔴 |
| TC-LC-004c | FR-XI-01 / Tạm dừng E1 ERR-XI-01-TD-01 (Codex 2026-05-09) | Tạm dừng CT khi user không có quyền | nht_01 login (NHT — KHÔNG có quyền). CT-TH21 DANG_THUC_HIEN. | — | 1. Force deep-link + API PATCH `/pause`. | (1) Sidebar/menu KHÔNG có entry CT HTPLDN cho NHT. Force API → reject "Bạn không có quyền tạm dừng CT" (ERR-XI-01-TD-01, srs-fr-15:224). KHÔNG transition. | Negative 🟡 |
| TC-LC-004d | FR-XI-01 / Tạm dừng E2 ERR-XI-01-TD-02 (Codex 2026-05-09) | Tạm dừng CT khi state ≠ DANG_THUC_HIEN | cb_pd_tw_01 login. CT-TD05 TAM_DUNG (đã tạm dừng rồi). | ly_do="Test" | 1. Mở chi tiết CT-TD05. 2. Try [Tạm dừng]. | (1) Nút [Tạm dừng] ẨN khi CT đã TAM_DUNG (chỉ hiện [Tiếp tục]). Force API PATCH `/pause` → reject "CT phải ở trạng thái Đang thực hiện để tạm dừng" (ERR-XI-01-TD-02, srs-fr-15:225). KHÔNG transition. | Negative 🟡 |
| TC-LC-007b | FR-XI-01 / Tiếp tục CB_NV (Codex 2026-05-09 ROLE-001) | CB_NV tiếp tục CT (per srs-fr-15:241 "CB NV/CB PD") | cb_nv_tw_01 login. CT-TD20 TAM_DUNG. | — | 1. [Tiếp tục] → confirm. | (3) Trạng thái → DANG_THUC_HIEN. Audit log. **Note:** SRS line 241 cho phép CẢ CB_NV và CB_PD — TC bổ sung positive cho CB_NV. | Happy 🟡 |
| TC-LC-007c | FR-XI-01 / Tiếp tục E1 ERR-XI-01-TT-01 (Codex 2026-05-09) | Tiếp tục CT khi user không có quyền | tvv_01 login (TVV — KHÔNG có quyền). CT-TD21 TAM_DUNG. | — | 1. Force API PATCH `/resume`. | (1) Sidebar không có entry. Force API → reject "Bạn không có quyền tiếp tục CT" (ERR-XI-01-TT-01, srs-fr-15:250). KHÔNG transition. | Negative 🟡 |

---

## C. HOÀN THÀNH CT — HAPPY + NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LC-009 | FR-XI-01 / Hoàn thành E1 ERR-XI-01-HT-01 | CB NV không được hoàn thành (chỉ CB PD) | cb_nv_tw_01 login. CT-TH05 DANG_THUC_HIEN, đợt BC đã hoàn thành. | — | 1. Mở chi tiết. | (1) Nút [Hoàn thành] ẩn với CB NV. Force → reject "Chỉ CB Phê duyệt mới được hoàn thành CT" (ERR-XI-01-HT-01). | Negative 🟡 |
| TC-LC-010 | FR-XI-01 / Hoàn thành E3 ERR-XI-01-HT-03 | Còn đợt BC chưa hoàn thành | cb_pd_tw_01 login. CT-TH06 DANG_THUC_HIEN, có 1 đợt BC trạng thái CHO_DUYET_KQ. | — | 1. [Hoàn thành] → confirm. | (2) Error "Vui lòng hoàn thành tất cả đợt báo cáo trước khi hoàn thành CT" (ERR-XI-01-HT-03). KHÔNG transition. | Negative 🔴 |
| TC-LC-011 | FR-XI-01 / Hoàn thành step 1-5 | Hoàn thành CT (happy — defer GĐ2 đợt BC DA_TONG_HOP) | cb_pd_tw_01 login. CT-TH07 DANG_THUC_HIEN, tất cả đợt BC ở DA_TONG_HOP. | — | 1. [Hoàn thành] → confirm. | (3) Trạng thái → HOAN_THANH. `ngay_hoan_thanh=NOW()`. Audit log. | Happy 🟡 (cross-phase seed) |
| TC-LC-011b | FR-XI-01 / Hoàn thành E2 ERR-XI-01-HT-02 (Codex 2026-05-09) | Hoàn thành CT khi state ≠ DANG_THUC_HIEN | cb_pd_tw_01 login. CT-DD22 DA_DUYET (chưa kích hoạt). | — | 1. Mở chi tiết. | (1) Nút [Hoàn thành] ẨN khi CT chưa DANG_THUC_HIEN. Force API PATCH `/complete` → reject "CT phải ở trạng thái Đang thực hiện để hoàn thành" (ERR-XI-01-HT-02, srs-fr-15:274). KHÔNG transition. | Negative 🟡 |

---

## D. HỦY CT — HAPPY + NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LC-012 | FR-XI-01 / Hủy step 1-5 | Hủy CT khi DU_THAO | cb_nv_tw_01 login. CT-DT03 DU_THAO. | — | 1. [Hủy CT] → modal xác nhận → OK. | (3) Trạng thái → HUY. CT KHÔNG xuất hiện trong DS active filter. Audit log. | Happy 🟡 |
| TC-LC-013 | FR-XI-01 / Hủy E2 ERR-XI-01-HC-02 | Hủy CT khi ≠ DU_THAO | cb_nv_tw_01 login. CT-DD05 DA_DUYET. | — | 1. Mở chi tiết. | (1) Nút [Hủy CT] ẩn. Force → reject "Chỉ hủy CT ở trạng thái Dự thảo" (ERR-XI-01-HC-02). | Negative 🟢 |
| TC-LC-013b | FR-XI-01 / Hủy E1 ERR-XI-01-HC-01 (Codex 2026-05-09) | Hủy CT khi user không có quyền | cb_pd_tw_01 login (CB PD — KHÔNG có quyền Hủy, srs-fr-15:288 "Kiểm tra quyền CB NV"). CT-DT20 DU_THAO. | — | 1. Mở chi tiết. 2. Force API PATCH `/cancel`. | (1) Nút [Hủy CT] ẨN với CB PD. Force API → reject "Bạn không có quyền hủy CT" (ERR-XI-01-HC-01, srs-fr-15:298). KHÔNG transition. | Negative 🟡 |

---

## E. RÚT TRÌNH — HAPPY + NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LC-014 | FR-XI-01 / Rút trình step 1-4 | Người trình rút trình | cb_nv_tw_01 đã trình CT-PD02 → CHO_PHE_DUYET. cb_nv_tw_01 login. | — | 1. [Rút trình] → confirm. | (3) Trạng thái → DU_THAO. Notification CB PD (đã hủy chờ duyệt). Audit log. | Happy 🟡 |
| TC-LC-015 | FR-XI-01 / Rút trình E1 ERR-XI-01-RT-01 | Không phải người trình → reject | cb_nv_tw_02 login (KHÔNG phải người trình). CT-PD03 CHO_PHE_DUYET trình bởi tw_01. | — | 1. Mở chi tiết. | (1) Nút [Rút trình] ẩn với user ≠ người trình. Force → reject "Chỉ người trình mới được rút trình" (ERR-XI-01-RT-01). | Negative 🟡 |
| TC-LC-015b | FR-XI-01 / Rút trình E2 ERR-XI-01-RT-02 (Codex 2026-05-09) | Rút trình khi state ≠ CHO_PHE_DUYET | cb_nv_tw_01 (người trình) login. CT-DD23 DA_DUYET (đã được duyệt rồi, không thể rút). | — | 1. Mở chi tiết. 2. Force API PATCH `/withdraw`. | (1) Nút [Rút trình] ẨN khi CT đã DA_DUYET (lifecycle move forward). Force API → reject "CT phải ở trạng thái Chờ phê duyệt để rút trình" (ERR-XI-01-RT-02, srs-fr-15:322). KHÔNG transition. | Negative 🟡 |

---

## F. RE-SUBMIT CYCLE — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LC-016 | FR-XI-01 / Rút trình + FR-XI-03 (A4 merged) | Cycle Trình → Rút trình → Trình lại | cb_nv_tw_01 login. CT-DT11 DU_THAO. | — | 1. [Gửi PD] → CHO_PHE_DUYET. 2. [Rút trình] → DU_THAO. 3. Sửa lại tên. 4. [Gửi PD] lần 2. | (3) Cycle hoàn chỉnh: state DU_THAO → CHO_PHE_DUYET → DU_THAO → CHO_PHE_DUYET. Audit log có 4 records. Lần 2 trình PD: notification CB PD lại. | Edge 🟡 |
| TC-LC-017 | FR-XI-04 + BR-FLOW-04 (A4 merged) | Cycle Trình → Từ chối → Sửa → Trình lại | cb_nv_tw_01 + cb_pd_tw_01 login. CT-DT12 DU_THAO. | ly_do_tu_choi="Cần làm rõ đối tượng" | 1. NV trình PD. 2. PD từ chối + lý do. 3. CT → DU_THAO + lý do persist. 4. NV mở CT, sửa `doi_tuong`. 5. NV trình PD lần 2. 6. PD duyệt. | (3) Cycle: DU_THAO → CHO_PHE_DUYET → DU_THAO (TC) → CHO_PHE_DUYET (re-submit) → DA_DUYET. Audit log đầy đủ. NV thấy lý do TC trên UI khi mở CT lần 2. | Edge 🔴 |

---

## Tổng kết file 03-TC

- **27 TC**: 9 Happy + 14 Negative + 1 Edge cũ + 2 Edge cycle + 1 SPEC-CLARIFY (A3 base 15 + A4 merged 2 + Codex 2026-05-09 +10)
- **Critical TC (🔴)**: 001, 004, 004b, 005, 010, 017
- **Cross-phase note**: TC-LC-011 (Hoàn thành happy) phụ thuộc đợt BC DA_TONG_HOP — cross-phase seed thủ công hoặc defer GĐ2.
- **A4 merged 2026-05-06**: TC-LC-016, TC-LC-017
- **Codex review 2026-05-09:** Thêm 10 TC fill ERR code coverage + role correction:
  - **ERR codes thiếu (7 TC):** TC-LC-003b (KH-01 permission), TC-LC-004c (TD-01 permission), TC-LC-004d (TD-02 state), TC-LC-007c (TT-01 permission), TC-LC-011b (HT-02 state), TC-LC-013b (HC-01 permission), TC-LC-015b (RT-02 state).
  - **Role correction (2 TC):** TC-LC-004b (CB_NV Tạm dừng — per SRS line 213 cho phép CẢ CB_NV/CB_PD), TC-LC-007b (CB_NV Tiếp tục — per SRS line 241).
  - **Guard SPEC-CLARIFY (1 TC):** TC-LC-003c (Kích hoạt guard "kế hoạch chi tiết" — SPEC-CLARIFY-CT-05).
  - **BR ref fix:** TC-LC-005 — bỏ ref `BR-FLOW-04` (chỉ áp Từ chối, không Tạm dừng), giữ ERR-XI-01-TD-03 only.

*Generated 2026-05-06 — Phase A step A3 + A4 inline merge · Updated 2026-05-09 sau Codex review*
