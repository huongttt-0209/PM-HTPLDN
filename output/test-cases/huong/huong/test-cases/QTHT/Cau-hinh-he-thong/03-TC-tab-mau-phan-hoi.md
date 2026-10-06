# Test Cases — Tab 3: Mẫu phản hồi (FR-II-NEW-02, Mô hình B Hybrid 2 tầng)

> **SRS Ref**: FR-II-NEW-02 (srs-fr-02:891-967), SCR-VIII-06 Tab 3 (srs-fr-10:1655-1668), Entity `MAU_PHAN_HOI`, permission action-level `srs-v3.1.md §3.4.2 MAU_PHAN_HOI`
> **Ngày tạo**: 2026-05-08 (BMAD A3, A4 inline merge)
> **Tài khoản chính**: 4 role test — `qtht_01` (READ-only), `cb_nv_tw_01` (CRUD TW_QUOC_GIA), `cb_nv_bn_01` (CRUD BN_RIENG Bộ TC), `cb_nv_dp_01` (CRUD DP_RIENG Sở TP HN)
> **URL:** `/quan-tri/cau-hinh` → Tab 3

> **Mô hình B Hybrid 2 tầng (CĐT chốt 2026-05-02):**
> - TW soạn mẫu khung quốc gia (`pham_vi=TW_QUOC_GIA`) → 63 ĐP đọc dùng (BR-AUTH-08 exception).
> - BN soạn mẫu chuyên ngành (`pham_vi=BN_RIENG`) — chỉ CB cùng BN đó thấy.
> - ĐP soạn mẫu địa phương (`pham_vi=DP_RIENG`) — chỉ CB cùng ĐP đó thấy.
> - `pham_vi_ap_dung` **auto-fill theo `user.don_vi.cap`**, **read-only ở UI**, **immutable sau tạo**.
> - QTHT chỉ READ toàn quốc (KHÔNG CRUD — line 1691).

> **Pre-condition chung:** AUDIT_LOG enabled. DANH_MUC có ≥ 5 lĩnh vực PL (DAN_SU, HINH_SU, LAO_DONG, HANH_CHINH, KINH_TE). Seed 9 mẫu test trải đều 3 phạm vi:
> - 3 mẫu TW_QUOC_GIA (CB_NV_TW tạo): "Mẫu quốc gia DAN_SU", "Mẫu quốc gia HINH_SU", "Mẫu quốc gia LAO_DONG"
> - 3 mẫu BN_RIENG (Bộ TC: 2 mẫu, Bộ KH&ĐT: 1 mẫu)
> - 3 mẫu DP_RIENG (Sở HN: 2 mẫu, Sở HCM: 1 mẫu)

---

## A. HAPPY PATH — CREATE per cấp (Mô hình B)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-MPH-001 | FR-II-NEW-02 AC1 + step 3 | CB_NV_TW tạo mẫu — auto-fill `pham_vi=TW_QUOC_GIA` | `cb_nv_tw_01`. | ten_mau="Mẫu test TW", linh_vuc=DAN_SU, noi_dung="Cảm ơn quý cơ quan...", trang_thai=KICH_HOAT | 1. Login. 2. Vào Tab 3. 3. Click [+ Thêm mẫu phản hồi]. 4. Fill modal: tên + lĩnh vực + nội dung. 5. Quan sát field "Phạm vi áp dụng" + "Tác giả" auto-fill read-only. 6. Click [Lưu]. | **STATE**: BE POST `/api/mau-phan-hoi` với payload + auto `pham_vi_ap_dung=TW_QUOC_GIA`, `don_vi_id=user.don_vi_id`. **UI**: Modal "Phạm vi áp dụng" hiển thị badge 🟦 "Khung quốc gia (TW)" + tooltip *"Phạm vi tự gán theo cấp đơn vị bạn (TW). Không thể thay đổi sau khi tạo."* — KHÔNG cho input. Sau Save: toast success, modal đóng, bảng refresh có row mới với cột Phạm vi=🟦. **PERSIST**: AUDIT_LOG `entity=MAU_PHAN_HOI`, `action=CREATE`, `chi_tiet` chứa pham_vi=TW_QUOC_GIA. | Happy | P0 |
| TC-CH-MPH-002 | FR-II-NEW-02 AC2 | CB_NV_BN (Bộ TC) tạo mẫu — auto-fill `pham_vi=BN_RIENG` | `cb_nv_bn_01`. | Tương tự TC-001 | Same flow. | **UI**: Field "Phạm vi" hiển thị 🟩 "Chuyên ngành Bộ Tài chính". BE POST với pham_vi=BN_RIENG, don_vi_id=BoTC.id. **PERSIST**: Mẫu chỉ CB Bộ TC thấy được. | Happy | P0 |
| TC-CH-MPH-003 | FR-II-NEW-02 AC3 | CB_NV_DP (Sở HN) tạo mẫu — auto-fill `pham_vi=DP_RIENG` | `cb_nv_dp_01`. | Tương tự | Same flow. | **UI**: Field "Phạm vi" hiển thị 🟨 "Địa phương Sở TP HN". BE POST pham_vi=DP_RIENG. | Happy | P0 |
| TC-CH-MPH-004 | step 4 + AC7 | Sanitize XSS — nội dung chứa `<script>` | `cb_nv_tw_01`. | noi_dung=`<p>Test</p><script>alert('XSS')</script>` | 1. Modal create. 2. Paste vào rich-text editor. 3. Save. | **STATE**: BE F-38 sanitize: lưu chỉ `<p>Test</p>`, loại bỏ `<script>`. **UI**: Modal đóng. Reload xem mẫu — `<script>` đã loại. `list_console_messages` không có alert. **PERSIST**: BR-DATA-05 audit chỉ chứa nội dung sạch. | Edge | P0 |
| TC-CH-MPH-005 | input #7 boundary | Nội dung max 10.000 ký tự plain | `cb_nv_tw_01`. | noi_dung 10.000 ký tự | 1. Paste 10K. 2. Save. | **STATE**: BE accept. **UI**: Toast success. **PERSIST**: — | Edge | P1 |
| TC-CH-MPH-006 | input #1 boundary | ten_mau max 200 ký tự | `cb_nv_tw_01`. | ten_mau "A"×200 | 1. Save. | **STATE**: BE accept. **UI**: Toast success. (Boundary 201 → reject — paired TC-CH-MPH-064 ở Section F.) | Edge | P2 |
| TC-CH-MPH-007 | A6 fill A5-GAP-CH-04 + input #5 | Field tu_khoa happy + dùng để search | `cb_nv_tw_01`. | tu_khoa="hợp đồng, lao động" | 1. Modal create. 2. Nhập tu_khoa. 3. Save. 4. Search box gõ "lao động". | **STATE**: BE lưu tu_khoa. Search có thể match cả ten_mau lẫn tu_khoa (verify spec). **UI**: Mẫu mới hiện trong bảng. Search "lao động" tìm thấy. **PERSIST**: — | Happy | P2 |
| TC-CH-MPH-008 | A6 fill A5-GAP-CH-05 + input #4 | Field mo_ta happy — lưu + hiển thị | `cb_nv_tw_01`. | mo_ta="Mẫu phản hồi cho hỏi đáp về quyền lao động cơ bản" | 1. Modal. 2. Nhập mo_ta. 3. Save. 4. Click 👁 Xem mẫu vừa tạo. | **STATE**: BE lưu mo_ta. **UI**: Modal read-only hiển thị field "Mô tả" với giá trị nhập. **PERSIST**: — | Happy | P2 |

---

## B. HAPPY PATH — READ scope (Mô hình B Hybrid)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-MPH-010 | FR-II-NEW-02 Postcondition + line 1662 | CB_NV_TW thấy TẤT CẢ mẫu (TW + BN + DP) | `cb_nv_tw_01`. Seed 9 mẫu (3 TW + 3 BN + 3 DP). | — | 1. Tab 3. 2. Quan sát bảng. 3. Filter "Phạm vi" = "Tất cả". | **STATE**: BE GET `/api/mau-phan-hoi` cho TW user trả 9 mẫu. **UI**: Bảng 9 dòng. Cột Phạm vi: 3 dòng 🟦 + 3 dòng 🟩 + 3 dòng 🟨. Sort mặc định pham_vi ASC + updated_at DESC (line 1662). **PERSIST**: — | Happy | P0 |
| TC-CH-MPH-011 | FR-II-NEW-02 Postcondition + Permission §3.4.2 (CAUHINH-10 RESOLVED 2026-05-08 — BA chốt BN thấy TW) | CB_NV_BN (Bộ TC) thấy TW + BN mình; KHÔNG thấy BN khác hay DP | `cb_nv_bn_01`. | — | 1. Tab 3. 2. Quan sát bảng. | **STATE**: BE filter `WHERE pham_vi=TW_QUOC_GIA OR (pham_vi=BN_RIENG AND don_vi_id=BoTC.id)` (Permission matrix §3.4.2 MPH_READ — BA confirm 2026-05-08 file `phan-hoi-ba-review-srs-fr-02-hoi-dap.md` mục 3). **UI**: Bảng **5 dòng** = 3 TW + 2 BN BoTC. KHÔNG có mẫu Bộ KH&ĐT, KHÔNG có DP. **Note**: FR-II-NEW-02 Postcondition line 955 viết "BN không thấy TW" là **sai spec**, cần update SRS theo BA chốt mới — KHÔNG ảnh hưởng test. **PERSIST**: BR-AUTH-08 ngoại lệ áp dụng đúng. | Happy | P0 |
| TC-CH-MPH-012 | FR-II-NEW-02 AC4 | CB_NV_DP (Sở HN) thấy TW + DP mình; KHÔNG thấy DP HCM hay BN | `cb_nv_dp_01`. | — | 1. Tab 3. 2. Quan sát bảng. | **STATE**: BE filter `WHERE pham_vi=TW_QUOC_GIA OR (pham_vi=DP_RIENG AND don_vi_id=SoHN.id)`. **UI**: Bảng 5 dòng = 3 TW + 2 DP Sở HN. KHÔNG có Sở HCM, KHÔNG có BN. **PERSIST**: — | Happy | P0 |
| TC-CH-MPH-013 | line 1662 + 1689 | QTHT thấy tất cả 9 mẫu (READ-only) | `qtht_01`. | — | 1. Tab 3. 2. Quan sát. | **STATE**: BE return all (QTHT bypass). **UI**: Bảng 9 dòng đa cấp. Cột Hành động chỉ có nút 👁 Xem (KHÔNG có Sửa/Xóa per row vì QTHT chỉ READ — line 1691). Nút [+ Thêm mẫu phản hồi] **disabled** với tooltip giải thích. **PERSIST**: — | Happy | P0 |
| TC-CH-MPH-014 | line 1689 | CB_PD_BN thấy READ scope cấp BN, không có nút CRUD | `cb_pd_bn_01`. | — | 1. Tab 3. 2. Quan sát. | **STATE**: BE filter scope BN. **UI**: Bảng theo scope CB_PD_BN cấp BN. KHÔNG có nút Sửa/Xóa per row. KHÔNG có [+ Thêm mẫu]. **PERSIST**: — | Happy | P1 |

---

## C. HAPPY PATH — UPDATE / DELETE (per ownership)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-MPH-020 | line 1663 (b) | CB_NV_TW sửa mẫu của mình (cùng don_vi_id) | `cb_nv_tw_01`. Mẫu TW của mình tồn tại. | ten_mau mới + noi_dung mới | 1. Hover row TW của mình. 2. Click ✏️ Sửa. 3. Modal hiển thị giá trị cũ. 4. Sửa + Save. | **STATE**: BE PATCH `/api/mau-phan-hoi/{id}`. AUDIT_LOG action=UPDATE chi_tiet old/new. **UI**: Toast success. Bảng refresh. **PERSIST**: pham_vi_ap_dung KHÔNG đổi (read-only). | Happy | P0 |
| TC-CH-MPH-021 | line 1663 (c) | CB_NV_BN xóa mẫu của BN mình — confirm vì so_lan_su_dung > 0 | `cb_nv_bn_01`. Mẫu BN BoTC có `so_lan_su_dung=5`. | — | 1. Hover row BN của mình. 2. Click 🗑 Xóa. 3. Modal confirm "Mẫu đã được dùng 5 lần. Vẫn xóa?". 4. Click "OK". | **STATE**: BE soft delete `is_deleted=1` (BR-DATA-01). AUDIT_LOG action=DELETE. **UI**: Modal C12 nguyên văn. Sau OK, row biến mất khỏi bảng. **PERSIST**: GET reload không hiện. | Happy | P0 |
| TC-CH-MPH-022 | line 1665 (#22 trang_thai toggle) | Toggle trang_thai KICH_HOAT → VO_HIEU_HOA | `cb_nv_tw_01`. | — | 1. Sửa mẫu của mình. 2. Toggle trang_thai. 3. Save. | **STATE**: BE PATCH `trang_thai=VO_HIEU_HOA`. **UI**: Cột Trạng thái cell hiển thị badge "Vô hiệu hóa". Khi user khác tạo phản hồi (FR-II-07), mẫu này không hiện trong dropdown. **PERSIST**: — | Happy | P1 |

---

## D. NEGATIVE — VALIDATION ERR-MPH-01..06

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-MPH-030 | ERR-MPH-01 | ten_mau trống | `cb_nv_tw_01`. | ten_mau="" | 1. Modal create. 2. Bỏ trống ten_mau. 3. Save. | **STATE**: BE/FE reject. **UI**: Toast/inline error nguyên văn "Tên mẫu là bắt buộc" (srs-fr-02:934). | Negative | P0 |
| TC-CH-MPH-031 | ERR-MPH-02 | noi_dung trống | `cb_nv_tw_01`. | noi_dung="" | 1. Modal. 2. Bỏ noi_dung. 3. Save. | Same — "Nội dung mẫu là bắt buộc" (srs-fr-02:935). | Negative | P0 |
| TC-CH-MPH-032 | ERR-MPH-03 | linh_vuc_id không tồn tại | `cb_nv_tw_01`. | linh_vuc_id=`uuid-not-exist` (manipulate qua devtools) | 1. Devtools console: PATCH với linh_vuc_id giả. | **STATE**: BE reject 400. **UI**: Toast "Lĩnh vực pháp luật không hợp lệ" (srs-fr-02:936). | Negative | P1 |
| TC-CH-MPH-033 | ERR-MPH-04 (403) | **CB_NV_BN cố tạo mẫu pham_vi=TW_QUOC_GIA qua API direct** | `cb_nv_bn_01`. | API payload: `{ten_mau:"hack", pham_vi_ap_dung:"TW_QUOC_GIA"}` | 1. Devtools console qua MCP `evaluate_script`: `fetch('/api/mau-phan-hoi', {method:'POST', body:JSON.stringify({ten_mau:'hack',linh_vuc_id:'...',noi_dung:'...',pham_vi_ap_dung:'TW_QUOC_GIA'}), headers:{Authorization:'Bearer '+token}})`. | **STATE**: BE check `MPH_CREATE_TW` permission (action-level srs-v3.md §3.4.2). User cấp BN không có quyền → reject 403. **UI**: Toast/HTTP 403 "Bạn không có quyền tạo mẫu khung quốc gia. Chỉ Cán bộ Nghiệp vụ Trung ương được phép" (srs-fr-02:937). **PERSIST**: KHÔNG có MAU_PHAN_HOI mới. AUDIT_LOG có thể log attempt failed. | Negative | P0 |
| TC-CH-MPH-034 | ERR-MPH-04 (403) | CB_NV_DP cố tạo mẫu pham_vi=BN_RIENG qua API | `cb_nv_dp_01`. | pham_vi=BN_RIENG | Tương tự TC-033. | **STATE**: BE reject 403. **UI**: Cùng error pattern. | Negative | P1 |
| TC-CH-MPH-035 | ERR-MPH-05 | Cố sửa pham_vi_ap_dung qua API direct | `cb_nv_tw_01`. Mẫu TW của mình. | PATCH pham_vi=BN_RIENG | 1. Devtools: PATCH với pham_vi_ap_dung mới. | **STATE**: BE reject 400 immutable. **UI**: Toast "Phạm vi áp dụng không thể thay đổi sau khi tạo" (srs-fr-02:938). **PERSIST**: pham_vi cũ giữ nguyên. | Negative | P0 |
| TC-CH-MPH-036 | ERR-MPH-06 (403) | **CB_NV_DP cố sửa mẫu của TW (cross-cấp)** | `cb_nv_dp_01`. Mẫu TW tồn tại id=`mph-tw-001`. | PATCH `/api/mau-phan-hoi/mph-tw-001` | 1. Devtools: PATCH với JWT DP. | **STATE**: BE check `record.don_vi_id != user.don_vi_id` → reject 403. **UI**: Toast "Bạn chỉ được sửa/xóa mẫu thuộc đơn vị mình" (srs-fr-02:939). | Negative | P0 |
| TC-CH-MPH-037 | ERR-MPH-06 (403) | **CB_NV_BN (Bộ TC) cố xóa mẫu Bộ KH&ĐT (cross-BN)** | `cb_nv_bn_01`. Mẫu BN Bộ KH&ĐT tồn tại. | DELETE `/api/mau-phan-hoi/mph-bn-bkhdt` | 1. Devtools: DELETE. | Same TC-036 message. **PERSIST**: Mẫu BoKHDT vẫn còn. | Negative | P0 |
| TC-CH-MPH-038 | ERR-MPH-06 (403) | CB_NV_DP (Sở HN) cố sửa mẫu Sở HCM (cross-ĐP ngang cấp) | `cb_nv_dp_01`. Mẫu DP Sở HCM tồn tại. | PATCH | Tương tự. | Same. | Negative | P1 |

---

## E. UI INTERACTIONS (Filter / Search / Tabs / Modals)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-MPH-040 | line 1661 (a) Filter Phạm vi | Filter "Mẫu khung quốc gia (TW)" | `cb_nv_dp_01`. | filter pham_vi=TW_QUOC_GIA | 1. Dropdown "Phạm vi" → "Mẫu khung quốc gia (TW)". | **STATE**: BE filter `WHERE pham_vi=TW_QUOC_GIA`. **UI**: Bảng chỉ TW (3 dòng). | Happy | P1 |
| TC-CH-MPH-041 | line 1661 (a) | Filter "Mẫu của đơn vị tôi" — DP user | `cb_nv_dp_01`. | filter "Đơn vị tôi" | 1. Dropdown filter. | **STATE**: BE filter `WHERE pham_vi=DP_RIENG AND don_vi_id=SoHN.id`. **UI**: Bảng chỉ DP Sở HN (2 dòng). | Happy | P1 |
| TC-CH-MPH-042 | line 1661 (b) Filter lĩnh vực | Filter linh_vuc=DAN_SU | `cb_nv_tw_01`. | linh_vuc=DAN_SU | 1. Filter lĩnh vực. | **STATE**: BE WHERE linh_vuc_id=DAN_SU.id. **UI**: Bảng chỉ mẫu DAN_SU. | Happy | P1 |
| TC-CH-MPH-043 | line 1661 (c) Filter trạng thái | Filter trang_thai=VO_HIEU_HOA | `cb_nv_tw_01`. ≥ 1 mẫu KICH_HOAT + 1 VO_HIEU_HOA. | trang_thai=VO_HIEU_HOA | 1. Filter trạng thái. | **UI**: Bảng chỉ mẫu vô hiệu hóa. Badge "Vô hiệu hóa". | Happy | P1 |
| TC-CH-MPH-044 | line 1661 (d) Search ten_mau | Search keyword substring | `cb_nv_tw_01`. | keyword="quốc gia" | 1. Gõ vào search box. 2. Wait debounce. | **STATE**: BE WHERE `ten_mau ILIKE '%quốc gia%'` (case-insensitive substring). **UI**: Bảng filter live. | Happy | P0 |
| TC-CH-MPH-045 | line 1662 sort | Sort mặc định: pham_vi ASC, updated_at DESC | `cb_nv_tw_01`. | — | 1. Mở Tab 3. 2. Quan sát thứ tự. | **STATE/UI**: Dòng đầu = mẫu TW (badge 🟦), tiếp BN (🟩), tiếp DP (🟨). Trong mỗi nhóm, bản updated_at mới nhất lên đầu. | Happy | P1 |
| TC-CH-MPH-046 | BR-DATA-07 | Pagination 20/page | `cb_nv_tw_01`. ≥ 50 mẫu seed. | — | 1. Footer pagination. 2. Click trang 2. | **STATE**: BE LIMIT 20 OFFSET 20. **UI**: 20 dòng/page. | Happy | P1 |
| TC-CH-MPH-047 | line 1666 modal read-only | DP user click [Xem] mẫu TW (read-only modal) | `cb_nv_dp_01`. | Mẫu TW. | 1. Click 👁 Xem mẫu TW. | **STATE**: GET. **UI**: Modal đầy đủ field read-only, KHÔNG có nút [Lưu], chỉ [Đóng]. | Happy | P0 |
| TC-CH-MPH-048 | line 1664 disabled state | QTHT thấy nút [+ Thêm mẫu phản hồi] disabled với tooltip | `qtht_01`. | — | 1. Tab 3. 2. Hover nút. | **UI**: Nút disabled (greyed). Tooltip "Bạn chỉ có quyền xem mẫu, không có quyền tạo." (verify text). | Happy | P1 |
| TC-CH-MPH-049 | line 1667 empty state | DP user mới + CHƯA có mẫu nào trong scope (env clean DP) | `cb_nv_dp_02` (Sở chưa có mẫu). Sở HCM seed 0 mẫu DP. | — | 1. Tab 3. 2. Quan sát. | **UI**: Bảng vẫn show 3 mẫu TW (read-only) + empty section "Mẫu của đơn vị bạn" với placeholder *"Chưa có mẫu phản hồi nào trong phạm vi của bạn. Bấm '+ Thêm mẫu phản hồi' để tạo mới."* | Happy | P2 |
| TC-CH-MPH-050 | A6 fill A5-GAP-CH-07 + line 1667 | Empty state khi filter no-match (sau khi đã có data) | `cb_nv_tw_01`. ≥ 9 mẫu seed. | filter linh_vuc=KINH_TE (không có mẫu KINH_TE) | 1. Filter linh_vuc = KINH_TE. 2. [Tìm kiếm]. | **STATE**: BE trả 0 row. **UI**: Empty state placeholder, nhưng KHÁC empty state lúc DB clean — verify text khác hoặc thêm hint "Thử bộ lọc khác". (Verify behavior thực tế.) **PERSIST**: — | Edge | P2 |

---

## F. SECURITY & EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-MPH-060 | BR-EC-13 | Search SQL injection | `cb_nv_tw_01`. | keyword=`'; DROP TABLE MAU_PHAN_HOI; --` | 1. Search. | **STATE**: BE escape. MAU_PHAN_HOI còn nguyên. **UI**: Empty hoặc match literal. KHÔNG stack trace. **PERSIST**: Reload — bảng còn data. | Negative | P0 |
| TC-CH-MPH-061 | BR-EC-13 | Search XSS | `cb_nv_tw_01`. | keyword=`<script>alert(1)</script>` | 1. Search. | `list_console_messages` không alert. | Negative | P0 |
| TC-CH-MPH-062 | BR-EC-13 boundary | Search 200 ký tự | `cb_nv_tw_01`. | keyword="A"×200 | 1. Search. | BE accept; 201 → reject. | Edge | P2 |
| TC-CH-MPH-063 | A4 (A4 merged) | Concurrent Edit 2 BN user trên cùng 1 mẫu BN | `cb_nv_bn_01` + `cb_nv_bn_03` (cùng Bộ TC nếu có). | Concurrent | 1. 2 user mở edit cùng mẫu. 2. Save lệch nhau. | **STATE**: BE optimistic lock 409 cho user thứ 2. **UI**: Toast WARNING. | Edge | P1 |
| TC-CH-MPH-064 | input #1 boundary 201 (A4 merged) | ten_mau 201 ký tự — reject | `cb_nv_tw_01`. | ten_mau "A"×201 | 1. Save. | **STATE**: BE reject 400. **UI**: Inline error "Tên mẫu vượt quá 200 ký tự" hoặc tương đương. | Negative | P2 |
| TC-CH-MPH-065 | A4 (A4 merged) | Sanitize XSS in ten_mau và mo_ta (ngoài noi_dung) | `cb_nv_tw_01`. | ten_mau=`<img src=x onerror=alert(1)>` | 1. Save. 2. Reload danh sách. | **STATE**: BE sanitize hoặc escape. **UI**: Cell ten_mau hiển thị literal text (escape) hoặc clean. KHÔNG execute. | Negative | P0 |
| TC-CH-MPH-066 | A4 (A4 merged) | DELETE mẫu so_lan_su_dung=0 — không hiện modal C12 | `cb_nv_tw_01`. Mẫu mới tạo so_lan_su_dung=0. | — | 1. Click 🗑. | **STATE**: BE soft delete. **UI**: KHÔNG hiện confirm "đã dùng N lần" (vì n=0). Có thể hiện confirm chung "Bạn có chắc xóa?". | Edge | P2 |
| TC-CH-MPH-067 | A4 cross-cấp READ direct (A4 merged) | DP user GET mẫu của DP khác qua API direct (IDOR) | `cb_nv_dp_01`. Mẫu DP HCM id=`mph-dp-hcm-001`. | GET `/api/mau-phan-hoi/mph-dp-hcm-001` | 1. Devtools: GET. | **STATE**: BE check scope → reject 403 hoặc 404. **UI**: Network 403/404. **PERSIST**: KHÔNG leak data. | Negative | P0 |
| TC-CH-MPH-068 | A4 dropdown insert (A4 merged) — DP user OK theo cả 2 source | Verify mẫu xuất hiện đúng nhóm trong dropdown FR-II-07 — **DP user only** | `cb_nv_dp_01`. Có 1 hỏi đáp đang soạn phản hồi. | — | 1. Vào màn hình soạn phản hồi (FR-II-07). 2. Click dropdown chèn mẫu. | **STATE**: BE GET mẫu theo MPH_READ scope. **UI**: Dropdown 2 nhóm: "Mẫu khung quốc gia (TW)" + "Mẫu của Sở TP Hà Nội". KHÔNG có Sở HCM, KHÔNG có BN. **DP scope đồng nhất giữa permission matrix + FR Postcondition** (cả 2 đều cho DP đọc TW), nên TC này KHÔNG ảnh hưởng SPEC-CLARIFY-CAUHINH-10. (Chéo TC FR-II-07.) | Edge | P0 |
| TC-CH-MPH-069 | FR-II-07 dropdown BN (CAUHINH-10 RESOLVED 2026-05-08 — BA chốt BN thấy TW) | Verify mẫu xuất hiện trong dropdown FR-II-07 cho **BN user** | `cb_nv_bn_01`. Có 1 hỏi đáp đang soạn phản hồi. | — | 1. Vào màn hình soạn phản hồi. 2. Click dropdown chèn mẫu. | **STATE**: BE GET mẫu theo MPH_READ scope BN. **UI**: Dropdown **2 nhóm** giống pattern DP user: "Mẫu khung quốc gia (TW)" + "Mẫu của Bộ Tài chính". KHÔNG có mẫu Bộ KH&ĐT, KHÔNG có DP. (Cross-check pattern TC-CH-MPH-068 cho DP — BA confirm BN có quyền tương đương DP về việc đọc mẫu TW.) **PERSIST**: — | Happy | P0 |

---

## Tổng số TC: 41 (~8 Create + 5 Read + 3 Update/Delete + 9 Validation + 11 UI + 5 Security/Edge) — A3 base 28 + A4 merged 10 + A6 fill 3
**Priority**: P0=20 / P1=12 / P2=9

**Coverage:**
- BR: BR-AUTH-01, BR-AUTH-08 (Mô hình B exception), BR-DATA-01 (soft delete), BR-DATA-03 (common fields), BR-DATA-05 (audit), BR-DATA-07 (pagination), BR-EC-01 (concurrent), BR-EC-13 (sanitize)
- AC SRS: AC1-AC7 ✅ (7/7) — TC-001-004 (CRUD per cấp), TC-010-012 (READ scope), TC-033 (BE direct CREATE), TC-036 (cross-don_vi UPDATE)
- Error codes: ERR-MPH-01..06 (6/6 cover, TC-030-038)
- Mô hình B Hybrid: full coverage 3 cấp × CRUD × Scope rules
- A4 merged 2026-05-08: TC-063 (concurrent), TC-064 (boundary 201), TC-065 (XSS multi-field), TC-066 (delete n=0), TC-067 (IDOR direct GET), TC-068 (dropdown FR-II-07)
- A6 fill 2026-05-08: TC-007 (tu_khoa happy), TC-008 (mo_ta happy), TC-050 (empty state filter no-match)
- SPEC-CLARIFY: CAUHINH-04 (filter scope cho TW user — TC-040)
