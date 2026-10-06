# Test Cases — FR-II-06 (UC15): Phân công xử lý câu hỏi

> **SRS Ref**: FR-II-06 (lines 468-552), SCR-II-03 (lines 1207-1242), SM-HOIDAP transition `TIEP_NHAN/DANG_XU_LY → DANG_XU_LY`
> **Ngày tạo**: 2026-05-10
> **Đặc thù**:
> - **2 nhánh**: `loai_doi_tuong_xu_ly = CA_NHAN` (TVV/CG/NHT/CB tự do) hoặc `TO_CHUC` (TC TV theo NĐ77/2008 + NĐ55/2019 Đ.9 — Cty Luật / VP LS / TT TVPL).
> - **Validation cờ**: CA_NHAN → `nguoi_xu_ly_id` REQUIRED, `to_chuc_tu_van_id` PHẢI NULL. TO_CHUC → cả 2 REQUIRED + TVV phải thuộc TC.
> - **Auto-filter 4 tiêu chí (BA chốt 2026-05-07 Q11)**: lĩnh vực + đơn vị + workload ASC + FIFO (ho_ten ASC), LIMIT 10. CB NV bỏ qua filter lĩnh vực.
> - **State re-fetch khi mở modal (F-15)**: nếu state không ∈ {TIEP_NHAN, DANG_XU_LY} → đóng modal + ERR-PC-02.
> - **7 ERR codes**: ERR-PC-01..06, WRN-PC-01.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-II-06 / {section}`
- **Pre-conditions**: User CB_NV_{cap} cùng đơn vị bản ghi, có quyền `HOI_DAP_ASSIGN`. HD state ∈ {TIEP_NHAN, DANG_XU_LY}, `linh_vuc_id NOT NULL`.

---

## Trường input

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_id | Y | identifier | URL/system |
| 2 | loai_doi_tuong_xu_ly | Y | enum 2 | CA_NHAN / TO_CHUC, default CA_NHAN |
| 3 | to_chuc_tu_van_id | Y nếu loai_doi_tuong_xu_ly=TO_CHUC | identifier | FK TO_CHUC_TU_VAN HOAT_DONG. NULL nếu CA_NHAN |
| 4 | nguoi_xu_ly_id | Y (cả 2 loại) | identifier | FK TAI_KHOAN HOAT_DONG. Nếu TO_CHUC: TVV thuộc TC (`TU_VAN_VIEN.to_chuc_chinh_id = to_chuc_tu_van_id`) |
| 5 | ghi_chu | N | text | Placeholder "Ghi chú cho người được phân công..." |
| 6 | thoi_han | N | date | Default deadline SLA |

---

## A. PHÂN CÔNG CÁ NHÂN — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PC-001 | FR-II-06 / AC #2 + Processing step 5 (auto-filter) | Phân công TVV cá nhân tự do — happy | cb_nv_tw_01 login. HD-X TIEP_NHAN, linh_vuc=Đất đai. ≥3 TVV cá nhân (`to_chuc_chinh_id IS NULL`) HOAT_DONG có `linh_vuc_chuyen_mon` chứa Đất đai trong scope TW. | tab=Cá nhân, nguoi_xu_ly=TVV-001 | 1. SCR-II-02 HD-X. 2. Click [Phân công] dòng 10. 3. Modal SCR-II-03 mở. 4. Tab "Cá nhân tự do" mặc định active. 5. Bảng gợi ý 4a hiển thị ≥3 TVV theo workload ASC. 6. Click radio TVV-001. 7. nguoi_xu_ly auto-fill. 8. Click [Phân công]. | (1) PUT /hoi-dap/{id}/phan-cong thành công. (3) Modal đóng + toast "Đã phân công cho TVV-001". (4) HD: `loai_doi_tuong_xu_ly=CA_NHAN`, `nguoi_phan_cong_id=TVV-001`, `to_chuc_tu_van_id=NULL`, `trang_thai=DANG_XU_LY`. (5) Notification in-app + email cho TVV-001 (BR-DATA-05). | Happy 🔴 |
| TC-PC-002 | FR-II-06 / AC #3 (NHT) | Phân công NHT cá nhân — verify NHT.linh_vuc_ids[] N:N filter | cb_nv_dp_01 login. HD-Y TIEP_NHAN, linh_vuc=Lao động. NHT-001 có `linh_vuc_ids=[Lao động, Đầu tư]`. | tab=Cá nhân, nguoi_xu_ly=NHT-001 | 1. Mở modal phân công. 2. Bảng 4a hiển thị NHT-001 (vì linh_vuc_ids chứa Lao động). 3. Click radio NHT-001. 4. Lưu. | (3) HD: `nguoi_phan_cong_id=NHT-001`, state DANG_XU_LY. Auto-filter dùng N:N junction `NGUOI_HO_TRO_LINH_VUC` cho NHT. | Happy 🔴 |
| TC-PC-003 | FR-II-06 / AC #1 + auto-filter sort | Bảng gợi ý 4a sort workload ASC + tiebreaker ho_ten ASC | cb_nv_tw_01 login. HD-Z TIEP_NHAN, linh_vuc=Dân sự. 3 TVV cùng linh_vuc Dân sự: TVV-A (workload=5, ho_ten="An"), TVV-B (workload=2, ho_ten="Bình"), TVV-C (workload=2, ho_ten="Châu"). | — | 1. Mở modal. 2. Verify thứ tự bảng 4a. | (3) Thứ tự: TVV-B (2, Bình) → TVV-C (2, Châu) → TVV-A (5, An). Sort workload ASC, tie-break ho_ten ASC alphabetical. LIMIT 10. | Happy 🟡 |
| TC-PC-004 | FR-II-06 / Phân công lại DANG_XU_LY | Phân công lại khi DANG_XU_LY | cb_nv_tw_01 login. HD-W state DANG_XU_LY, đang phân công TVV-001. | tab=Cá nhân, nguoi_xu_ly=TVV-002 | 1. Click [Phân công] (ghi nhãn "Phân công lại — #{ma}" SCR-II-03 dòng 1). 2. Bảng 4a hiển thị "Đang phân công cho: TVV-001" dòng 2. 3. Chọn TVV-002. 4. Lưu. | (3) HD: `nguoi_phan_cong_id=TVV-002` (overwrite), state vẫn DANG_XU_LY. Notification cho TVV-002. Audit log "Phân công lại TVV-001 → TVV-002". | Happy 🟡 |

---

## B. PHÂN CÔNG TỔ CHỨC TƯ VẤN — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PC-010 | FR-II-06 / AC #4 (TC TV) + 2-cấp picker | Phân công TC TV + TVV thuộc TC — happy | cb_nv_tw_01 login. HD-V TIEP_NHAN, linh_vuc=Doanh nghiệp. TC-TV "Cty Luật ABC" HOAT_DONG có `linh_vuc=[Doanh nghiệp]`, có 3 TVV: TVV-D, TVV-E, TVV-F (`to_chuc_chinh_id=TC-ABC`, HOAT_DONG). | tab=Tổ chức, tc=TC-ABC, tvv=TVV-D | 1. Mở modal. 2. Click tab "Tổ chức tư vấn". 3. Bảng 4b hiển thị TC-ABC (linh_vuc match). 4. Click radio TC-ABC. 5. Bảng 4c load 3 TVV thuộc TC-ABC. 6. Click radio TVV-D. 7. nguoi_xu_ly auto-fill TVV-D. 8. Lưu. | (3) HD: `loai_doi_tuong_xu_ly=TO_CHUC`, `to_chuc_tu_van_id=TC-ABC`, `nguoi_phan_cong_id=TVV-D`, state DANG_XU_LY. (4) Notification TVV-D + CC email TC-ABC.email_lien_he (NĐ77/2008 + NĐ55/2019 Đ.9). | Happy 🔴 |
| TC-PC-011 | FR-II-06 / Bảng 4c filter | Bảng 4c chỉ hiển thị TVV thuộc TC vừa chọn | cb_nv_tw_01 login. HD-U TIEP_NHAN. 2 TC TV: TC-A (3 TVV) + TC-B (2 TVV). Cả 2 match linh_vuc. | — | 1. Mở modal. 2. Tab Tổ chức. 3. Click TC-A. 4. Verify bảng 4c chỉ 3 TVV của TC-A. 5. Click TC-B. | (3) Bảng 4c reload 2 TVV của TC-B. KHÔNG hiển thị TVV của TC-A nữa. Filter `TU_VAN_VIEN.to_chuc_chinh_id = to_chuc_tu_van_id`. | Happy 🟡 |

---

## C. PHÂN CÔNG — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PC-100 | FR-II-06 / E1 ERR-PC-01 | Cá nhân vô hiệu | cb_nv_tw_01 login. HD-T TIEP_NHAN. TVV-VOHIEU đã `trang_thai=VO_HIEU_HOA`. | nguoi_xu_ly=TVV-VOHIEU (force qua DevTools) | 1. Modal mở. 2. Bảng 4a KHÔNG hiển thị TVV-VOHIEU (filter HOAT_DONG). 3. Force PUT API với nguoi_xu_ly=TVV-VOHIEU. | (2) ERR-PC-01 **"Người được chọn đã bị vô hiệu hóa"**. UI dòng 6: hàng mờ disabled tooltip "Đã bị vô hiệu hóa". | Negative 🔴 |
| TC-PC-101 | FR-II-06 / E3 ERR-PC-02 (F-15) | State đã đổi (concurrent) — re-fetch | cb_nv_tw_01 mở SCR-II-02 HD-S (TIEP_NHAN). cb_nv_tw_02 đã tích "Đã trả lời" trên HD-S → CHO_PHE_DUYET. | — | 1. cb_nv_tw_01 click [Phân công] sau khi state đã đổi. | (2) State re-fetch trước render modal → state=CHO_PHE_DUYET ≠ {TIEP_NHAN, DANG_XU_LY}. Modal KHÔNG render. Toast ERR-PC-02 **"Hỏi đáp ở trạng thái 'Chờ phê duyệt' không thể phân công"**. SCR-II-02 reload với state mới. | Negative 🔴 |
| TC-PC-102 | FR-II-06 / E4 ERR-PC-03 | TC TV vô hiệu | cb_nv_tw_01 login. HD-R TIEP_NHAN. TC-XYZ `trang_thai=TAM_DUNG`. | tab=Tổ chức | 1. Mở modal. 2. Tab Tổ chức. 3. Bảng 4b KHÔNG hiển thị TC-XYZ. 4. Force select TC-XYZ qua API. | (2) ERR-PC-03 **"Tổ chức tư vấn 'XYZ' đã bị vô hiệu hóa hoặc tạm dừng hoạt động"**. | Negative 🟡 |
| TC-PC-103 | FR-II-06 / E5 ERR-PC-04 | TO_CHUC thiếu nguoi_xu_ly_id | cb_nv_tw_01 login. HD-Q TIEP_NHAN. | loai_doi_tuong_xu_ly=TO_CHUC, tc=TC-A, nguoi_xu_ly=null | 1. Tab Tổ chức. 2. Chọn TC-A. 3. KHÔNG chọn TVV ở bảng 4c. 4. Click [Phân công]. | (2) ERR-PC-04 **"Phân công cho Tổ chức tư vấn phải chọn đủ 2 thông tin: Tổ chức + Tư vấn viên thuộc tổ chức"**. UI: highlight border đỏ field thiếu. Modal giữ mở. | Negative 🔴 |
| TC-PC-104 | FR-II-06 / E6 ERR-PC-05 | TVV không thuộc TC (UI bypass via API) | cb_nv_tw_01 login. HD-P TIEP_NHAN. TC-A (TVV-1, TVV-2). TC-B (TVV-3). | loai_doi_tuong_xu_ly=TO_CHUC, tc=TC-A, nguoi_xu_ly=TVV-3 (qua API) | 1. Force API PUT với mismatched IDs. | (2) Server validate `TU_VAN_VIEN[TVV-3].to_chuc_chinh_id = TC-B ≠ TC-A`. Reject ERR-PC-05 **"Tư vấn viên 'TVV-3' không thuộc Tổ chức 'TC-A'. Vui lòng chọn lại"**. UI giữ modal + toast. | Negative 🔴 |
| TC-PC-105 | FR-II-06 / E7 ERR-PC-06 | CA_NHAN truyền to_chuc_tu_van_id thừa | cb_nv_tw_01 login. HD-O TIEP_NHAN. | loai_doi_tuong_xu_ly=CA_NHAN, nguoi_xu_ly=NHT-001, tc_id=TC-A (thừa) | 1. Force API PUT với cờ thừa. | (2) UI ẩn dropdown TC TV ở tab Cá nhân (prevention). API: ERR-PC-06 **"Phân công cá nhân không cần chọn Tổ chức tư vấn"** + hủy submit. | Negative 🟡 |
| TC-PC-106 | FR-II-06 / E2 WRN-PC-01 | Workload quá tải — cảnh báo không block | cb_nv_tw_01 login. HD-N TIEP_NHAN. TVV-G workload=15 (ngưỡng cảnh báo VD 10). | nguoi_xu_ly=TVV-G | 1. Mở modal. 2. Bảng 4a hiển thị TVV-G với badge đỏ "Quá tải (15 yêu cầu)" dòng 5. 3. Chọn TVV-G. 4. Lưu. | (2) Modal C12 confirm "Cán bộ TVV-G đang xử lý 15 yêu cầu. Xác nhận phân công?" (WRN-PC-01). User OK → tiến hành. KHÔNG block. | Negative 🟡 |
| TC-PC-107 | FR-II-06 / Permission CB_PD | CB_PD attempt phân công | cb_pd_tw_01 login. HD-M TIEP_NHAN scope TW. | — | 1. Mở SCR-II-02. | (2) Nút [Phân công] KHÔNG hiển thị (chỉ CB_NV cùng đơn vị, quyền HOI_DAP_ASSIGN). | Negative 🟡 |
| TC-PC-108 | FR-II-06 / Preconditions linh_vuc_id NULL | HD chưa nhập lĩnh vực → modal cần fallback | cb_nv_tw_01 login. HD-L TIEP_NHAN, `linh_vuc_id=NULL`. | — | 1. Click [Phân công]. | (2) **SPEC-CLARIFY-PC-01**: Per Preconditions FR-II-06 line 483, `linh_vuc_id NOT NULL` bắt buộc. Hành vi expected: hoặc (a) nút disabled + tooltip "Chưa nhập lĩnh vực, không thể phân công" hoặc (b) modal mở nhưng bảng gợi ý empty + dropdown TK toàn bộ trong đơn vị. Verify thực tế. | Negative 🟡 |

---

## D. PHÂN CÔNG — EDGE & BOUNDARY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PC-200 | FR-II-06 / Auto-filter limit 10 | Bảng 4a có ≥15 TVV match → chỉ 10 đầu | cb_nv_tw_01 login. HD-K TIEP_NHAN, linh_vuc=Đất đai. 15 TVV match scope TW. | — | 1. Mở modal. 2. Tab Cá nhân. | (3) Bảng 4a hiển thị **10 records** (LIMIT 10 theo BA chốt 2026-05-07 Q11). Workload ASC + ho_ten ASC. | Edge 🟡 |
| TC-PC-201 | FR-II-06 / CB NV bỏ qua filter lĩnh vực | CB NV (không có linh_vuc_chuyen_mon) hiển thị bất kể lĩnh vực HD | cb_nv_tw_01 login. HD-J TIEP_NHAN, linh_vuc=Hôn nhân. CB NV-X (cb_nv_tw_03) cùng TW không có chuyên môn cụ thể. | — | 1. Mở modal Cá nhân. | (3) CB NV-X xuất hiện trong bảng 4a (CB NV bypass filter linh_vuc, theo BA chốt 2026-05-07 Q11 step 5b). | Edge 🟡 |
| TC-PC-202 | FR-II-06 / Empty bảng 4a | Không có TVV/NHT/CG khớp lĩnh vực | cb_nv_tw_01 login. HD-I TIEP_NHAN, linh_vuc=Hàng hải. Không TVV/NHT match. | — | 1. Mở modal Cá nhân. | (3) Empty bảng 4a: **"Chưa có cá nhân nào khớp lĩnh vực. Bạn có thể chọn cán bộ khác ở ô Người xử lý bên dưới."** Dropdown nguoi_xu_ly fallback toàn TK trong đơn vị. | Edge 🟢 |
| TC-PC-203 | FR-II-06 / Empty bảng 4c | TC-A có 0 TVV HOAT_DONG | cb_nv_tw_01 login. TC-A khớp linh_vuc nhưng tất cả TVV `trang_thai=TAM_DUNG`. | — | 1. Tab Tổ chức. 2. Click TC-A. | (3) Bảng 4c empty: **"Tổ chức 'TC-A' chưa có Tư vấn viên nào ở trạng thái Hoạt động. Vui lòng chọn tổ chức khác."** | Edge 🟢 |
| TC-PC-204 | FR-II-06 / thoi_han custom | Override thoi_han khác SLA mặc định | cb_nv_tw_01 login. HD-H TIEP_NHAN, deadline mặc định=2026-05-30. | thoi_han=2026-05-20 (sớm hơn) | 1. Mở modal. 2. Date-picker chọn 20/05. 3. Lưu. | (3) HD: `deadline=2026-05-20`. Audit log entry "Phân công kèm cập nhật thời hạn". | Edge 🟢 |
| TC-PC-205 | FR-II-06 / BR-AUTH-08 cross-tenant | Bảng 4a chỉ TK cùng đơn vị | cb_nv_dp_01 (Sở TP AG) login. HD-AG TIEP_NHAN. TVV-AG (Sở TP AG) + TVV-BG (Sở TP BG) cùng linh_vuc. | — | 1. Mở modal. | (3) Bảng 4a chỉ TVV-AG. TVV-BG KHÔNG hiển thị (BR-AUTH-08 scope đơn vị). | Edge 🔴 |
| TC-PC-206 | FR-II-06 / Notification TC TV email_lien_he | Verify CC email tổ chức khi phân công TO_CHUC | cb_nv_tw_01 login. HD-G TIEP_NHAN. TC-OPP có `email_lien_he=opp@law.vn`. | tc=TC-OPP, tvv=TVV-X | 1. Phân công TO_CHUC. | (4) Notification: email gửi TVV-X (chính) + CC opp@law.vn. Verify qua MailHog hoặc audit log entry. | Edge 🟡 |
| TC-PC-207 | FR-II-06 / Tab switch reset selection | Đổi tab Cá nhân ↔ Tổ chức → reset radio | cb_nv_tw_01 login. HD-F TIEP_NHAN. | — | 1. Tab Cá nhân + chọn TVV-001. 2. Switch tab Tổ chức. | (3) Selection reset (loai_doi_tuong_xu_ly đổi tương ứng). nguoi_xu_ly_id clear. Modal tiêu đề/dropdown đổi theo tab. | Edge 🟢 |

---

---

## E. EDGE BỔ SUNG (A4 merged 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PC-208 | FR-II-06 / Data integrity | TVV `to_chuc_chinh_id` inconsistent (data corruption edge) | qtht_01 seed: TVV-Z có `to_chuc_chinh_id=NULL` nhưng được assign vào TC-A trong các record cũ. | tab=Tổ chức, tc=TC-A, tvv=TVV-Z | 1. Force API PUT. | (3) Backend validate `TVV.to_chuc_chinh_id = TC-A` → nếu NULL → ERR-PC-05 hoặc cho phép (tùy data integrity rule). | Edge 🟡 |
| TC-PC-209 | FR-II-06 / Race TVV inactive | TVV vừa bị TAM_DUNG giữa lúc bảng 4a load | cb_nv_tw_01 login. TVV-Y HOAT_DONG khi mở modal. Admin TAM_DUNG TVV-Y giữa chừng. | nguoi_xu_ly=TVV-Y | 1. Modal mở, bảng 4a hiển thị TVV-Y. 2. Click radio TVV-Y. 3. Submit. | (2) Backend re-check trang_thai → reject ERR-PC-01. UI: toast "Người được chọn đã bị vô hiệu hóa giữa chừng. Vui lòng chọn lại". | Edge 🟡 |
| TC-PC-210 | FR-II-06 / UI rapid-fire | Click radio nhiều lần liên tiếp trên bảng 4a | cb_nv_tw_01 login. HD-X TIEP_NHAN. | — | 1. Modal. 2. Click TVV-A → TVV-B → TVV-A → TVV-C trong 1 giây. | (3) UI verify chỉ giữ TVV-C cuối cùng. nguoi_xu_ly auto-fill TVV-C. | Edge 🟢 |
| TC-PC-211 | FR-II-06 / NULL deadline / SPEC-CLARIFY-PC-02 | HD chưa có deadline (NULL) khi mở modal | cb_nv_tw_01 login. HD-W TIEP_NHAN, deadline=NULL (chưa tính). | — | 1. Mở modal. 2. Verify date-picker thoi_han dòng 10. | (3) **SPEC-CLARIFY-PC-02**: hoặc empty (placeholder "Chọn ngày") hoặc default deadline tính theo SLA. | Edge 🟡 |
| TC-PC-212 | FR-II-06 / Modal cleanup | Tab Tổ chức + chọn TC + Hủy modal → không có dirty state | cb_nv_tw_01 login. HD-V TIEP_NHAN. | — | 1. Tab Tổ chức. 2. Chọn TC-A → bảng 4c load. 3. Click [Hủy]. 4. Reopen modal. | (3) Modal reset hoàn toàn. Tab về Cá nhân (default), bảng 4b/4c clear. KHÔNG dirty state. | Edge 🟢 |
| TC-PC-213 | FR-II-06 / Auto-filter 4 tiêu chí end-to-end (Codex P1 G1-01) | Composition test: lĩnh vực + đơn vị + workload + tiebreaker ho_ten | cb_nv_tw_01 login. HD-AUTO TIEP_NHAN, linh_vuc=Đất đai, scope TW. **Seed dataset 8 candidates:** (a) TVV-01 cùng TW, linh_vuc Đất đai, workload=2, ho_ten="An" → MATCH; (b) TVV-02 cùng TW, linh_vuc Đất đai, workload=2, ho_ten="Bình" → MATCH (tied workload); (c) TVV-03 cùng TW, linh_vuc Đất đai, workload=5, ho_ten="Châu" → MATCH; (d) TVV-04 cùng TW, linh_vuc Đất đai, workload=8, ho_ten="Dũng" → MATCH; (e) TVV-05 cùng TW, **linh_vuc Hôn nhân (FAIL criterion 1)** → SKIP; (f) TVV-06 **đơn vị BN (FAIL criterion 2 BR-AUTH-08)**, linh_vuc Đất đai → SKIP; (g) TVV-07 cùng TW, Đất đai, workload=11 nhưng `trang_thai=TAM_DUNG` (FAIL criterion 0 hoạt động) → SKIP; (h) NHT-01 cùng TW, `linh_vuc_ids=[Đất đai]`, workload=1 → MATCH (N:N junction). | — | 1. Mở modal phân công. 2. Tab Cá nhân tự do. 3. Verify bảng 4a. | (3) Bảng 4a hiển thị **5 candidates** đã pass cả 4 tiêu chí (TVV-01, TVV-02, TVV-03, TVV-04, NHT-01). KHÔNG có TVV-05 (sai lĩnh vực), TVV-06 (sai đơn vị), TVV-07 (sai trạng thái). (4) Sort order: NHT-01 (workload=1) → TVV-01 (2, "An") → TVV-02 (2, "Bình") → TVV-03 (5) → TVV-04 (8). Verify workload ASC + tiebreaker ho_ten ASC alphabetical Vietnamese. LIMIT 10 (5 < 10 OK). Per BA chốt 2026-05-07 Q11 step 5b-5d. | Edge 🔴 (P1 G1-01 fix) |

---

## Tổng kết file 05

- **Tổng số TC: 31** (4 Happy CN + 2 Happy TC + 9 Negative + 8 Edge + 3 cross-cutting + 5 A4 merged)
- **Critical TC (🔴)**: TC-PC-001, 002, 010, 100, 101, 103, 104, 205
- **Coverage**: FR-II-06 đầy đủ (CA_NHAN + TO_CHUC + auto-filter 4 tiêu chí + state re-fetch F-15 + permission CB_NV vs CB_PD + cross-tenant BR-AUTH-08)
- **Error codes**: ERR-PC-01..06, WRN-PC-01 (đầy đủ 7 codes)
- **SPEC-CLARIFY**: PC-01 (HD chưa nhập lĩnh vực → nút disabled vs fallback dropdown)

*Generated 2026-05-10 — Phase A step A3*
