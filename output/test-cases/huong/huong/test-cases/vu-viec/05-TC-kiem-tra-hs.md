# Test Cases — UC56: Kiểm tra Hồ sơ Vụ việc (FR-V.I-06)

> **SRS Ref**: FR-V.I-06 (srs-fr-05:493-557), SCR-V.I-03 Accordion 4 (srs-fr-05:1765), BR-EC-15 (srs-fr-05:2487), BR-EC-16 (srs-fr-05:2493)
> **Ngày tạo**: 2026-05-06 (BMAD A3) · **A7 filter applied**: 2026-05-06
> **Tài khoản chính**: `cb_nv_tw_01` (CB NV TW), `cb_nv_tw_02` (concurrent), `qtht_01` (admin verify)
> **A7 note**: TC scheduled job auto-reject quá hạn (BR-EC-16) verify gián tiếp qua time-shift seed (KHÔNG test scheduled directly — A7 LOẠI). 6 hạng mục checklist UC106 cấu hình ngoài scope FR-V.I-06.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-KT-UI-01 | FR-V.I-06 / SCR-V.I-03 Accordion 4 | Verify Accordion 4 "Kết quả Kiểm tra" hiển thị checklist 6 hạng mục Mẫu 01 NĐ55 + UI counter "Lần bổ sung: {n}/3" | `cb_nv_tw_01`. VV-X ở DA_TIEP_NHAN. Click [Kiểm tra Hồ sơ]. | — | 1. Mở SCR-V.I-03 chi tiết VV-X. 2. Click action [Kiểm tra Hồ sơ] (action-bar). 3. Quan sát Accordion 4 mở. | **UI**: Accordion 4 expand. Hiển thị checklist 6 hạng mục (srs-fr-05:516-522): (1) Văn bản đề nghị hỗ trợ Mẫu 01 NĐ55 (2) Bản chụp Giấy CNĐKKD (3) Tờ khai xác định quy mô DN NĐ39/2018 (4) Hợp đồng dịch vụ TVPL (5) Văn bản TVPL bản đầy đủ (6) Văn bản TVPL bản loại bỏ bí mật KD. Mỗi mục có 2 radio (Đạt/Không đạt) + ô ghi_chu text. Dropdown ket_luan 3 option (DAT/KHONG_DAT/YEU_CAU_BO_SUNG). Field ly_do textarea (initially không bắt buộc). Counter "Lần bổ sung: 0/3" (srs-fr-05:1765). | Happy | P1 |
| TC-VV-KT-UI-02 | BR-EC-15 / counter highlight | Counter highlight đỏ khi n ≥ 2 | `cb_nv_tw_01`. VV-Y có `bo_sung_count=2` (qua 2 lần YCBS). | — | 1. Mở SCR-V.I-03 chi tiết VV-Y. 2. Click [Kiểm tra Hồ sơ]. 3. Quan sát counter. | **UI**: Counter "Lần bổ sung: 2/3" highlight màu đỏ + có thể tooltip "Sắp tới giới hạn — lần 4 KHÔNG_ĐẠT sẽ tự động TỪ CHỐI" (BR-EC-15 srs-fr-05:2489). | Happy | P0 |
| TC-VV-KT-UI-03 | FR-V.I-06 / state-restricted Accordion | Accordion 4 KHÔNG cho edit khi VV ở DA_PHAN_CONG/DA_DUYET/HOAN_THANH | `cb_nv_tw_01`. VV-Z đã DA_PHAN_CONG. | — | 1. Mở SCR-V.I-03 chi tiết VV-Z. 2. Click Accordion 4. | **UI**: Accordion 4 hiển thị data lịch sử kiểm tra (read-only) — checklist + ket_luan + ly_do + nguoi_kiem_tra + ngay_kiem_tra. KHÔNG có nút [Hoàn tất Kiểm tra] (action-bar context-sensitive theo srs-fr-05:1773-1789, DA_PHAN_CONG → nút [Phân công] thay vì [Kiểm tra]). | Happy | P1 |

---

## B. CRUD HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-KT-101 | FR-V.I-06 AC1 / Processing B2 | Mở action [Kiểm tra Hồ sơ] → VV chuyển DA_TIEP_NHAN → DANG_KIEM_TRA | `cb_nv_tw_01`. VV-A ở DA_TIEP_NHAN. | — | 1. Click action [Kiểm tra Hồ sơ]. | **STATE**: Backend chuyển trang_thai DA_TIEP_NHAN → DANG_KIEM_TRA (SM-VUVIEC, srs-fr-05:529). **UI**: Stepper highlight "Đang kiểm tra". Action-bar đổi nút thành [Hoàn tất Kiểm tra] (srs-fr-05:1779). Accordion 4 expand cho phép edit. **PERSIST**: AUDIT_LOG hanh_dong='KIEM_TRA' trang_thai_truoc=DA_TIEP_NHAN trang_thai_sau=DANG_KIEM_TRA (BR-DATA-05). Verify Timeline (sidebar SCR-V.I-03) thêm entry mới. | Happy | P0 |
| TC-VV-KT-102 | FR-V.I-06 AC3 / Processing B5 | Hoàn tất kiểm tra ket_luan=DAT (cả 6 mục đạt) → VV chuyển DA_PHAN_CONG | `cb_nv_tw_01`. VV-A ở DANG_KIEM_TRA. | checklist=[6 mục dat=1], ket_luan="DAT" | 1. Tích Đạt cả 6 mục. 2. Chọn ket_luan "ĐẠT". 3. Click [Hoàn tất Kiểm tra]. | **STATE**: Backend chuyển VV → DA_PHAN_CONG (srs-fr-05:532). **UI**: Toast success "Đã hoàn tất kiểm tra. Vui lòng phân công xử lý." Stepper next "Đã phân công". Action-bar đổi nút [Phân công] (srs-fr-05:1780). **PERSIST**: AUDIT_LOG hanh_dong='KIEM_TRA' ket_luan='DAT' trang_thai_sau=DA_PHAN_CONG. | Happy | P0 |
| TC-VV-KT-103 | FR-V.I-06 AC2 / Processing B6 | Hoàn tất kiểm tra ket_luan=YEU_CAU_BO_SUNG → counter +1, VV chuyển YEU_CAU_BO_SUNG, TB DN | `cb_nv_tw_01`. VV-B ở DANG_KIEM_TRA, bo_sung_count=0. | checklist=[3 đạt 3 không đạt], ket_luan="YEU_CAU_BO_SUNG", ly_do="Vui lòng bổ sung Mẫu 01 + CNĐKKD" (50 ký tự). | 1. Tích 3 mục Đạt + 3 mục Không đạt. 2. Chọn ket_luan "YEU_CAU_BO_SUNG". 3. Nhập ly_do. 4. Click [Hoàn tất Kiểm tra]. | **STATE**: Backend (1) chuyển VV → YEU_CAU_BO_SUNG (srs-fr-05:533); (2) bo_sung_count = 0 + 1 = 1; (3) ngay_yeu_cau_bo_sung = NOW() (srs-fr-05:2067 — track timer cho BR-EC-16); (4) gửi TB DN qua in-app + email với danh sách tài liệu cần bổ sung. **UI**: Toast success "Đã yêu cầu doanh nghiệp bổ sung hồ sơ" (srs-fr-05:1810). Stepper highlight "Đang kiểm tra" + badge phụ "Yêu cầu bổ sung" (srs-fr-05:1761) + counter "Lần bổ sung: 1/3". **PERSIST**: AUDIT_LOG hanh_dong='YEU_CAU_BO_SUNG' ly_do=full text. THONG_BAO INSERT cho DN. Verify network POST `/vu-viec/{id}/kiem-tra` 200. | Happy | P0 |
| TC-VV-KT-104 | FR-V.I-06 AC / Processing B7 | Hoàn tất kiểm tra ket_luan=KHONG_DAT → VV chuyển TU_CHOI, TB DN | `cb_nv_tw_01`. VV-C ở DANG_KIEM_TRA. | checklist=[2 đạt 4 không đạt], ket_luan="KHONG_DAT", ly_do="Hồ sơ thiếu CNĐKKD và HĐ TVPL không hợp lệ" (60 ký tự). | 1. Tích checklist. 2. Chọn ket_luan "KHÔNG_ĐẠT". 3. Nhập ly_do. 4. Click [Hoàn tất Kiểm tra]. | **STATE**: Backend chuyển VV → TU_CHOI (srs-fr-05:534), gửi TB DN. **UI**: Toast success. Stepper highlight badge "Từ chối" (srs-fr-05:1761). **PERSIST**: AUDIT_LOG hanh_dong='TU_CHOI' (vai_tro='CB_NV') ly_do=full text. THONG_BAO INSERT cho DN với thông báo từ chối + ly_do. | Happy | P0 |
| TC-VV-KT-105 | FR-V.I-06 / Re-kiểm tra sau bổ sung | DN bổ sung HS (NEW-02) → VV về DANG_KIEM_TRA → CB NV kiểm tra lại lần 2 | `cb_nv_tw_01`. VV-D ở YEU_CAU_BO_SUNG, bo_sung_count=1. DN dn_01 đã bổ sung file qua NEW-02 → VV chuyển DANG_KIEM_TRA. | checklist=[6 mục Đạt], ket_luan="DAT" | 1. Mở SCR-V.I-03 VV-D. 2. Quan sát Accordion 3 có file bổ sung mới. 3. Click [Hoàn tất Kiểm tra]. 4. Tích Đạt 6 mục, kết luận DAT. 5. Confirm. | **STATE**: VV-D từ DANG_KIEM_TRA → DA_PHAN_CONG. counter giữ nguyên = 1 (KHÔNG reset). **UI**: Accordion 3 có thêm file DN bổ sung (đánh dấu nguồn 'DN'). Toast success. **PERSIST**: AUDIT_LOG kèm chuỗi: BO_SUNG_HS (DN) → KIEM_TRA (CB NV) → mỗi entry độc lập. | Happy | P1 |
| TC-VV-KT-106 | FR-V.I-06 / Processing B6+B7 cross-account TB | DN nhận TB chính xác sau YCBS và TU_CHOI (cross-account verify) | Tab1 `cb_nv_tw_01`. Tab2 `dn_01` (DN sở hữu VV-T). VV-T ở DANG_KIEM_TRA. | YCBS: ket_luan=YEU_CAU_BO_SUNG, ly_do="Bổ sung CNĐKKD"; sau đó TU_CHOI: ket_luan=KHONG_DAT, ly_do="Hồ sơ vẫn không đạt" | 1. Tab1 submit YEU_CAU_BO_SUNG. 2. Tab2 DN refresh notification panel. 3. Tab1 (sau DN bổ sung) submit KHONG_DAT. 4. Tab2 refresh lại. | **STATE**: BE bước 6+7 (srs-fr-05:533-534) gửi TB DN sau mỗi action. **UI**: (1) Sau YCBS: Tab2 nhận TB "Yêu cầu bổ sung hồ sơ — VV [mã]: Bổ sung CNĐKKD"; (2) Sau TU_CHOI: Tab2 nhận TB "Hồ sơ bị từ chối — VV [mã]: Hồ sơ vẫn không đạt". Verify wording thực tế (SPEC-CLARIFY-VV-KT-05 nếu khác). **PERSIST**: 2 record THONG_BAO cho DN. **CRITICAL**: TB phải kèm ly_do để DN biết bổ sung gì hoặc lý do từ chối → nếu thiếu ly_do trong TB = compliance gap. | Happy | P1 |

---

## C. NEGATIVE — VALIDATION ERRORS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-KT-201 | ERR-KT-01 / state invalid | Click [Hoàn tất Kiểm tra] khi VV ở DA_PHAN_CONG | `cb_nv_tw_01`. VV-E đã DA_PHAN_CONG. Sửa URL hoặc replay request action UC56. | — | 1. Forge POST `/vu-viec/{id}/kiem-tra` cho VV-E. | **STATE**: Backend reject với ERR-KT-01 (srs-fr-05:549). **UI**: Toast error nguyên văn "Vụ việc không ở trạng thái cho phép kiểm tra". Action-bar đã ẩn nút này — chỉ replay request mới trigger được lỗi. **PERSIST**: AUDIT_LOG ATTEMPT_INVALID_STATE. | Negative | P1 |
| TC-VV-KT-202 | ERR-KT-02 / thiếu lý do YCBS | ket_luan=YEU_CAU_BO_SUNG nhưng ly_do trống | `cb_nv_tw_01`. VV-F ở DANG_KIEM_TRA. | checklist=[partial], ket_luan="YEU_CAU_BO_SUNG", ly_do="" | 1. Chọn ket_luan YEU_CAU_BO_SUNG. 2. Để trống ly_do. 3. Click [Hoàn tất Kiểm tra]. | **STATE**: Backend reject với ERR-KT-02 (srs-fr-05:550). **UI**: Hoặc client validate (border đỏ + helper "Lý do là bắt buộc"); hoặc submit → toast error "Lý do là bắt buộc". Confirm modal trước đó (srs-fr-05:1810) cũng có textarea ly_do bắt buộc. **PERSIST**: KHÔNG có transition. | Negative | P0 |
| TC-VV-KT-203 | ERR-KT-02 / thiếu lý do KHONG_DAT | ket_luan=KHONG_DAT nhưng ly_do trống | `cb_nv_tw_01`. VV-G ở DANG_KIEM_TRA. | ket_luan="KHONG_DAT", ly_do="" | 1. Chọn ket_luan KHÔNG_ĐẠT. 2. Để trống ly_do. 3. Click [Hoàn tất Kiểm tra]. | **STATE**: Backend reject ERR-KT-02. **UI**: Toast error "Lý do là bắt buộc". **PERSIST**: KHÔNG có transition. | Negative | P0 |
| TC-VV-KT-204 | BR-EC-13 / XSS ly_do textarea | ly_do chứa XSS payload | `cb_nv_tw_01`. VV-H ở DANG_KIEM_TRA. | ly_do=`<script>alert('XSS-KT')</script>` + `<img src=x onerror=alert(1)>` | 1. Chọn YEU_CAU_BO_SUNG. 2. Paste XSS vào ly_do. 3. Submit. | **STATE**: Backend sanitize HTML — strip `<script>`, `onerror`. KHÔNG execute. **UI**: Sau submit, render ly_do trên Timeline (sidebar) + Accordion 4 → hiển thị raw text escaped, KHÔNG fire alert. `list_console_messages` clean. **PERSIST**: BE store sanitized text trong LICH_SU_VU_VIEC.ly_do. | Negative | P0 |
| TC-VV-KT-205 | FR-V.I-06 / boundary ly_do | ly_do boundary 5000 ký tự (max LICH_SU_VU_VIEC.noi_dung srs-fr-05:2176) | `cb_nv_tw_01`. VV-I ở DANG_KIEM_TRA. | ly_do = "A" × 5000 (boundary), "A" × 5001 (over) | 1. Test 5000 ký tự + Submit. 2. Test 5001 ký tự + Submit. | **STATE**: 5000 → INSERT thành công. 5001 → BE reject hoặc client maxlength truncate. **UI**: 5000 → toast success; 5001 → toast error/inline "Lý do tối đa 5000 ký tự" (SRS Gap message — mark **SPEC-CLARIFY-VV-KT-01**). **PERSIST**: 5000 record OK; 5001 KHÔNG record. | Negative | P1 |

---

## D. EDGE CASES

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-KT-301 | BR-EC-15 / lần 4 KHONG_DAT auto-TU_CHOI | bo_sung_count=2, lần kiểm tra thứ 3 ket_luan=KHONG_DAT (sau khi DN đã bổ sung 3 lần) | `cb_nv_tw_01`. VV-J seed: bo_sung_count=2 (đã qua 2 lần YCBS), DN bổ sung lần 3 → DANG_KIEM_TRA. | checklist=[partial], ket_luan="KHONG_DAT", ly_do="Vẫn không đạt sau lần bổ sung 3" | 1. Tích checklist. 2. Chọn KHÔNG_ĐẠT. 3. Submit. | **STATE**: Backend kiểm tra `bo_sung_count >= 3 AND ket_luan='KHONG_DAT'` → auto chuyển TU_CHOI với lý do system "Đã bổ sung 3 lần không đạt" (BR-EC-15 srs-fr-05:2487). **UI**: Toast khác biệt warning "Vụ việc đã yêu cầu bổ sung 3 lần. Tự động chuyển TỪ CHỐI." Stepper badge "Từ chối". **PERSIST**: AUDIT_LOG 2 entries: KIEM_TRA + TU_CHOI_AUTO_LIMIT. THONG_BAO DN với reasoning. | Edge | P0 |
| TC-VV-KT-302 | BR-EC-15 / chặn YCBS lần 4 | bo_sung_count=3, ket_luan=YEU_CAU_BO_SUNG → KHÔNG cho phép chọn (hoặc backend reject) | `cb_nv_tw_01`. VV-K seed: bo_sung_count=3. | ket_luan="YEU_CAU_BO_SUNG" | 1. Mở Accordion 4. 2. Try chọn ket_luan YEU_CAU_BO_SUNG. | **STATE**: Backend BR-EC-15 chặn — chỉ cho phép DAT hoặc KHONG_DAT khi counter ≥ 3 (lần 4 chỉ KHONG_DAT auto-TU_CHOI). **UI**: Option "YEU_CAU_BO_SUNG" disabled trong dropdown + tooltip "Đã đạt giới hạn 3 lần bổ sung" (SRS Gap UX — mark **SPEC-CLARIFY-VV-KT-02**). Hoặc cho phép select nhưng backend reject với toast. **PERSIST**: KHÔNG có transition mới. | Edge | P0 |
| TC-VV-KT-303 | BR-EC-01 / Optimistic lock concurrent | 2 CB NV cùng [Hoàn tất Kiểm tra] cùng VV | Tab1 `cb_nv_tw_01` + Tab2 `cb_nv_tw_02`. VV-L ở DANG_KIEM_TRA. Cả 2 tab đã mở Accordion 4. | Tab1: ket_luan=DAT. Tab2: ket_luan=YEU_CAU_BO_SUNG. | 1. Tab1 submit. 2. Tab2 submit (chưa reload). | **STATE**: Tab1 SUCCESS — VV → DA_PHAN_CONG. Tab2 FAIL với optimistic lock conflict (BR-EC-01). **UI**: Tab1 toast success. Tab2 modal "Vụ việc đã được CB Nghiệp vụ TW 01 cập nhật lúc dd/mm HH:mm. Vui lòng tải lại để xem thông tin mới nhất." (srs-fr-05:1623) + nút [Tải lại]. **PERSIST**: 1 entry KIEM_TRA bởi cb_nv_tw_01. | Edge | P0 |
| TC-VV-KT-304 | BR-EC-16 / quá hạn auto-reject (gián tiếp) | VV ở YEU_CAU_BO_SUNG quá 5 ngày LV → scheduled job auto-set TU_CHOI | Seed VV-M `trang_thai=YEU_CAU_BO_SUNG`, `ngay_yeu_cau_bo_sung = NOW() - 6 ngày LV` (giả lập quá hạn). Đợi scheduled job CROSS-01 chạy (hoặc trigger manual qua QTHT — **SPEC-CLARIFY-VV-KT-03**). | — | 1. Login QTHT trigger scheduled job manual. 2. Login `cb_nv_tw_01` xem VV-M sau 30 phút. | **STATE**: Backend auto chuyển VV-M → TU_CHOI (BR-EC-16 srs-fr-05:2493) + ghi LICH_SU_VU_VIEC hanh_dong='TU_CHOI_AUTO_QUA_HAN' vai_tro='HE_THONG'. **UI**: VV-M Stepper badge "Từ chối". Timeline có entry "HE_THONG tự động từ chối — quá hạn bổ sung". **PERSIST**: AUDIT_LOG. THONG_BAO DN. **Note**: Verify scheduled trực tiếp KHÔNG khả thi với MCP — verify gián tiếp qua state sau time-shift. | Edge | P1 |
| TC-VV-KT-305 | FR-V.I-06 / partial checklist save draft | Tích 4/6 mục, đóng modal không submit | `cb_nv_tw_01`. VV-N ở DANG_KIEM_TRA. | checklist=[4 mục Đạt, 2 mục bỏ trống] | 1. Tích 4 mục Đạt. 2. Đóng modal/Accordion (không submit). 3. Reload page. 4. Mở lại Accordion 4. | **STATE**: Backend KHÔNG persist draft trừ khi user submit explicitly (verify với BA — SRS không spec auto-save). **UI**: Sau reload, checklist reset về trạng thái ban đầu. KHÔNG cảnh báo "Bạn có muốn lưu nháp?" (giả định). Mark **SPEC-CLARIFY-VV-KT-04** — UX expected behavior. **PERSIST**: KHÔNG có change. | Edge | P2 |
| TC-VV-KT-306 | FR-V.I-06 / multi-round verify counter | VV-O qua 3 vòng YCBS → counter = 1, 2, 3 sau mỗi vòng | `cb_nv_tw_01`. VV-O ở DA_TIEP_NHAN. | Vòng 1: ket_luan=YCBS + DN bổ sung. Vòng 2: tương tự. Vòng 3: tương tự. | 1. Vòng 1: kiểm tra → YCBS → DN bổ sung → VV về DANG_KIEM_TRA. 2. Vòng 2: lặp. 3. Vòng 3: lặp. 4. Quan sát counter sau mỗi vòng. | **STATE**: counter +1 sau mỗi vòng YCBS. Sau vòng 3 counter=3. Vòng kiểm tra thứ 4 ket_luan KHONG_DAT → auto-TU_CHOI (link TC-VV-KT-301). **UI**: Counter cập nhật realtime: 0 → 1 → 2 (highlight đỏ) → 3 (highlight đỏ + warning). **PERSIST**: AUDIT_LOG 6 entries (3 KIEM_TRA + 3 BO_SUNG_HS). | Edge | P0 |

---

## Tổng kết file

**Tổng TC: 20** (3 UI + 6 Happy + 5 Negative + 6 Edge) — sau Codex review 2026-05-09

| Section | TC IDs | Count |
|---------|--------|------:|
| A. UI verification | UI-01, UI-02, UI-03 | 3 |
| B. Happy | 101, 102, 103, 104, 105, **106** ⭐ | 6 |
| C. Negative | 201, 202, 203, 204, 205 | 5 |
| D. Edge | 301, 302, 303, 304, 305, 306 | 6 |

⭐ = thêm sau Codex review 2026-05-09.

**Priority**: P0=12 / P1=6 / P2=2

> **Codex review 2026-05-09:**
> - CLEANUP recount confusion (line 57-61 — actual count 19 TC trước, sau review = 20)
> - ADD TC-VV-KT-106 (Cross-account TB DN sau YCBS + TU_CHOI — gap srs-fr-05:533-534)
> - ADD SPEC-CLARIFY-VV-KT-05 (TB wording cho DN — SRS không quote message format)

**Coverage:**
- BR: BR-AUTH-01, BR-DATA-05 (audit), BR-EC-01 (optimistic lock), BR-EC-13 (XSS sanitize), BR-EC-15 (YCBS 3 lần auto-reject), BR-EC-16 (quá hạn auto-reject), BR-NOTIF-01 (TB DN — TC-106), SM-VUVIEC transitions 4 (DA_TIEP_NHAN→DANG_KIEM_TRA, DA_PHAN_CONG, YEU_CAU_BO_SUNG, TU_CHOI)
- Error codes: ERR-KT-01, ERR-KT-02 (full 2/2)
- AC SRS: 3/3 (srs-fr-05:553-555)
- Processing steps: 9/9 covered (1 quyền in file 14 / 2 chuyển DANG_KIEM_TRA / 3 tải checklist UC106 / 4 mark / 5 DAT→DA_PHAN_CONG / 6 YCBS / 7 KHONG_DAT→TU_CHOI / 8 lịch sử / 9 audit)
- Auto-transitions: AT-01 (BR-EC-16 quá hạn), AT-02 (BR-EC-15 lần 4 KHONG_DAT)

**SPEC-CLARIFY:**
- **VV-KT-01**: Boundary message ly_do > 5000 ký tự — SRS không quote nguyên văn message
- **VV-KT-02**: UX khi counter=3 — option YEU_CAU_BO_SUNG disabled vs backend reject (UI behavior chưa spec)
- **VV-KT-03**: Trigger scheduled job manual cho QA — endpoint admin có sẵn không?
- **VV-KT-04**: Partial checklist auto-save draft — SRS không spec, expected behavior?
- **VV-KT-05 (mới)**: TB wording cho DN sau YCBS / TU_CHOI — SRS:533-534 chỉ note "gửi thông báo" không quote message format
