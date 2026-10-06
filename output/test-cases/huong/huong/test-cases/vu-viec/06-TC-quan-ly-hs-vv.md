# Test Cases — UC57: Quản lý Hồ sơ Vụ việc (FR-V.I-07)

> **SRS Ref**: FR-V.I-07 (srs-fr-05:561-623), SCR-V.I-03 (srs-fr-05:1750-1820), BR-FLOW-03 (srs-fr-05:2433), BR-EC-01 (Optimistic Locking)
> **Ngày tạo**: 2026-05-06 (BMAD A3) · **A7 filter applied**: 2026-05-06
> **Tài khoản chính**: `cb_nv_tw_01` (CB NV TW), `cb_nv_tw_02` (concurrent), `dn_01` (DN scope AG — verify chế độ DN xem chỉ đọc)
> **A7 note**: Toàn bộ TC dùng UI SCR-V.I-03 (CMS + DN mode). Verify Timeline/Accordion/file upload qua MCP UI + `list_network_requests` cho audit. KHÔNG TC chỉ-DB hay API thuần.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-QL-UI-01 | FR-V.I-07 / SCR-V.I-03 | Verify layout SCR-V.I-03 chế độ CMS: Stepper 10 bước + 8 Accordion + Timeline sidebar + action-bar context | `cb_nv_tw_01`. VV-X ở DANG_XU_LY (đã đi qua tiếp nhận, kiểm tra, phân công). | — | 1. Mở chi tiết VV-X. 2. Quan sát breadcrumb, header, Stepper, 8 Accordion, Timeline, action-bar. | **UI**: (1) Breadcrumb "Trang chủ > Vụ việc > Chi tiết > {ma_vu_viec}" (srs-fr-05:1759). (2) Header tiêu đề + 2-3 badge (trạng thái + SLA + "Đã công khai" nếu cong_khai=1) (srs-fr-05:1760). (3) Stepper 10 bước SM-VUVIEC, bước hiện tại nổi bật + bước done có ✓ (srs-fr-05:1761). (4) 8 Accordion theo srs-fr-05:1762-1769 (DN / Nội dung / Tài liệu / Kết quả KT / Phân công / Kết quả HT / Phê duyệt / Đánh giá). (5) Timeline sidebar load LICH_SU_VU_VIEC sắp xếp DESC (srs-fr-05:1770). (6) Action-bar nút context-sensitive theo trạng thái (srs-fr-05:1773-1789). | Happy | P1 |
| TC-VV-QL-UI-02 | SCR-V.I-03 chế độ DN | DN xem VV của mình hiển thị Accordion 4/5/7 ẨN, Accordion 8 cho phép nhập khi state HOAN_THANH | `dn_01`. VV-DN của dn_01 ở HOAN_THANH cong_khai=1. | — | 1. Login `dn_01` qua VNeID. 2. Vào `/ho-so-cua-toi/vu-viec/{id}`. | **UI**: Header "Trang chủ > Hồ sơ của tôi > Chi tiết vụ việc" (srs-fr-05:1834). Badge "Đã công khai" hiển thị (srs-fr-05:1835). Nhóm 1/2/3 chỉ đọc (srs-fr-05:1837-1839). Nhóm 4 (Kết quả KT) ẨN, Nhóm 5 (Phân công) ẨN, Nhóm 7 (PD) ẨN (srs-fr-05:1840-1843). Nhóm 6 (KQ hỗ trợ) chỉ đọc. Nhóm 8 (Đánh giá) cho phép nhập (srs-fr-05:1844). Action-bar chỉ 2 nút [Bổ sung hồ sơ] (nếu YEU_CAU_BO_SUNG) + [Đánh giá] (nếu HOAN_THANH/DA_DANH_GIA chưa đánh giá) (srs-fr-05:1846). | Happy | P0 |
| TC-VV-QL-UI-03 | SCR-V.I-03 / Accordion 3 nút [+ Thêm tài liệu] | Nút thêm tài liệu chỉ hiện khi VV ở trạng thái cho phép sửa (NOT HOAN_THANH/DA_DANH_GIA) | `cb_nv_tw_01`. So sánh 3 case: VV-A (DANG_XU_LY) / VV-B (HOAN_THANH) / VV-C (DA_DANH_GIA). | — | 1. Mở 3 VV lần lượt. 2. Quan sát Accordion 3 phần header có nút [+ Thêm tài liệu]? | **UI**: VV-A (DANG_XU_LY): nút [+ Thêm tài liệu] HIỂN THỊ (srs-fr-05:1764 "[+ Thêm] chỉ khi trạng thái cho phép sửa"). VV-B (HOAN_THANH): nút ẨN. VV-C (DA_DANH_GIA): nút ẨN (BR-FLOW-03 srs-fr-05:2433). | Happy | P1 |

---

## B. CRUD HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-QL-101 | FR-V.I-07 AC1 / Outputs | Xem chi tiết VV — hiển thị đầy đủ thông tin DN + nội dung + lịch sử + tài liệu | `cb_nv_tw_01`. VV-A ở DANG_XU_LY có 3 file đính kèm + 5 entries lịch sử. | — | 1. Click [Xem] dòng VV-A trong DS. | **STATE**: Backend GET `/vu-viec/{id}` join DOANH_NGHIEP + HO_SO_VU_VIEC + LICH_SU_VU_VIEC + KET_QUA_VU_VIEC + PHAN_CONG_VU_VIEC (srs-fr-05:585-606). **UI**: SCR-V.I-03 load đầy đủ: Accordion 1 (thông tin DN), Accordion 2 (tieu_de + noi_dung_yeu_cau + linh_vuc + loai_hinh_ho_tro + ghi_chu), Accordion 3 (3 file: tên/loại/kích thước/ngày upload/[Xem]/[Tải]), Accordion 4-7 theo data đã có (KT pass + Phân công + KQ NHT). Timeline sidebar 5 entries DESC. **PERSIST**: AUDIT_LOG action='VIEW_VU_VIEC' (verify gián tiếp qua `list_network_requests` GET 200). | Happy | P0 |
| TC-VV-QL-102 | FR-V.I-07 AC3 / Processing B3 | Edit noi_dung_yeu_cau + ghi_chu — chỉ áp dụng khi VV chưa khóa | `cb_nv_tw_01`. VV-B ở DANG_XU_LY. | noi_dung_yeu_cau="Cập nhật làm rõ vướng mắc về thuế GTGT", ghi_chu="Update theo yêu cầu DN qua điện thoại 2026-05-06" | 1. Mở Accordion 2. 2. Click [Sửa]. 3. Update 2 field. 4. Click [Lưu]. | **STATE**: Backend (1) verify `trang_thai NOT IN ('HOAN_THANH','DA_DANH_GIA')` (srs-fr-05:589); (2) UPDATE VU_VIEC SET noi_dung_yeu_cau, ghi_chu, updated_at=NOW(), updated_by=cb_nv_tw_01.id; (3) ghi LICH_SU_VU_VIEC hanh_dong='CAP_NHAT_NOI_DUNG' (srs-fr-05:592). **UI**: Toast success "Đã cập nhật thông tin vụ việc" (srs-fr-05:1617). Accordion 2 reload. **PERSIST**: AUDIT_LOG UPDATE. Timeline thêm entry mới. | Happy | P0 |
| TC-VV-QL-103 | FR-V.I-07 AC3 / Processing B4 | Upload file_bo_sung mới (file PDF 10MB + DOCX 5MB) | `cb_nv_tw_01`. VV-C ở DANG_XU_LY. | file1="bo-sung-1.pdf" (10MB), file2="bo-sung-2.docx" (5MB) | 1. Mở Accordion 3. 2. Click [+ Thêm tài liệu]. 3. Upload 2 file. 4. Click [Lưu]. | **STATE**: Backend (1) validate format/size/virus mỗi file; (2) INSERT 2 record FILE_DINH_KEM với entity_type='VU_VIEC' (srs-fr-05:2018-2024); (3) ghi LICH_SU_VU_VIEC hanh_dong='UPLOAD_TAI_LIEU' (srs-fr-05:592). **UI**: Progress bar 2 file. Toast success. Accordion 3 reload với 2 file mới (cuối list). **PERSIST**: 2 entries FILE_DINH_KEM. AUDIT_LOG UPLOAD. Verify network POST `/vu-viec/{id}/files` 200 x2. | Happy | P0 |
| TC-VV-QL-104 | SCR-V.I-03 / Accordion 3 nút [Tải] | Tải file đính kèm — counter so_luot_tai +1 (nếu có) | `cb_nv_tw_01`. VV-D có file `mau-01-NDD55.pdf`. | — | 1. Mở Accordion 3. 2. Click [Tải] dòng file. | **STATE**: Backend stream file gốc. **UI**: Browser download `mau-01-NDD55.pdf`. **PERSIST**: AUDIT_LOG action='TAI_TAI_LIEU_VV' (BR-DATA-05). Counter so_luot_tai (nếu BIEU_MAU pattern) — verify behavior, mark **SPEC-CLARIFY-VV-QL-01** nếu HO_SO_VU_VIEC không có counter. | Happy | P1 |
| TC-VV-QL-105 | SCR-V.I-03 sidebar Timeline | Timeline auto-scroll đến entry mới nhất + format "dd/mm HH:mm — {ho_ten} {hanh_dong}" | `cb_nv_tw_01`. VV-E vừa được phân công lúc 2026-05-06 14:30. | — | 1. Mở chi tiết VV-E. 2. Quan sát Timeline sidebar. | **UI**: Timeline hiển thị entries DESC, mới nhất trên cùng (srs-fr-05:1770). Format: "06/05 14:30 — CB Nghiệp vụ TW 01 PHAN_CONG". Click entry → expand chi tiết + ly_do (nếu có). Auto-scroll đến entry mới nhất khi load. **PERSIST**: — | Happy | P1 |
| TC-VV-QL-106 | FR-V.I-07 / Output AC2 | Verify Accordion 1 (DN info) link sang chi tiết DN (MH-07.2) | `cb_nv_tw_01`. VV-F. | — | 1. Mở Accordion 1. 2. Click vào tên DN hoặc MST. | **UI**: Click → mở SCR DN chi tiết (FR-V.III-04, MH-07.2 theo srs-fr-05:1762) trong tab mới hoặc inline modal. URL `/doanh-nghiep/{id}`. **PERSIST**: AUDIT_LOG VIEW_DN. | Happy | P2 |

---

## C. NEGATIVE — VALIDATION ERRORS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-QL-201 | ERR-VV-02 / BR-FLOW-03 | Edit noi_dung_yeu_cau khi VV ở HOAN_THANH → reject | `cb_nv_tw_01`. VV-G ở HOAN_THANH. | noi_dung_yeu_cau (mới) | 1. Mở Accordion 2. 2. Quan sát có nút [Sửa]? Nếu có → click. 3. Replay request UPDATE qua MCP `evaluate_script`. | **STATE**: Backend reject với ERR-VV-02 "Không thể chỉnh sửa vụ việc đã hoàn thành" (srs-fr-05:616, BR-FLOW-03 srs-fr-05:2433). **UI**: Nút [Sửa] KHÔNG hiển thị (action ẩn theo state). Replay request → toast error nguyên văn. **PERSIST**: KHÔNG có UPDATE. | Negative | P0 |
| TC-VV-QL-202 | FR-V.I-07 / state DA_DANH_GIA cấm sửa | Upload file_bo_sung khi VV ở DA_DANH_GIA → reject | `cb_nv_tw_01`. VV-H ở DA_DANH_GIA. | file="extra.pdf" (3MB) | 1. Mở Accordion 3. 2. Quan sát nút [+ Thêm tài liệu]? 3. Replay request POST upload. | **STATE**: Backend reject ERR-VV-02 (srs-fr-05:589 cấm sửa khi HOAN_THANH/DA_DANH_GIA). **UI**: Nút [+ Thêm tài liệu] ẨN (srs-fr-05:1764). Replay request → toast error. **PERSIST**: KHÔNG có FILE_DINH_KEM mới. | Negative | P0 |
| TC-VV-QL-203 | BR-EC-13 / XSS noi_dung_yeu_cau rich-text | Update noi_dung_yeu_cau với XSS payload | `cb_nv_tw_01`. VV-I ở DANG_XU_LY. | noi_dung_yeu_cau=`<script>alert('XSS-VV')</script>` + `<img src=x onerror=alert(1)>` | 1. Mở Accordion 2. 2. Click [Sửa]. 3. Paste XSS vào rich-text editor. 4. [Lưu]. | **STATE**: Backend sanitize HTML — strip `<script>`, `onerror`, `onclick` (BR-EC-13). **UI**: Sau lưu, render Accordion 2 + Timeline → KHÔNG fire alert. `list_console_messages` clean. Rich-text editor whitelist tag (vd `<b>`, `<i>`, `<a href>` allow). **PERSIST**: BE store sanitized text trong VU_VIEC.noi_dung_yeu_cau. KHÔNG store raw `<script>`. | Negative | P0 |
| TC-VV-QL-204 | FR-V.I-07 / file format vi phạm | Upload file_bo_sung định dạng .exe / .zip / .txt | `cb_nv_tw_01`. VV-J ở DANG_XU_LY. | file="malware.exe" (1MB) | 1. Mở Accordion 3. 2. Click [+ Thêm tài liệu]. 3. Upload `.exe`. | **STATE**: Backend reject ngay khi validate format (chỉ chấp nhận PDF/DOC/DOCX/XLS/XLSX/JPG/PNG theo file_dinh_kem rule cross-cutting). **UI**: Toast error "Chỉ chấp nhận file PDF, DOC, DOCX, XLS, XLSX, JPG, PNG" (SRS Gap exact message — mark **SPEC-CLARIFY-VV-QL-02**). File-input clear. **PERSIST**: KHÔNG có FILE_DINH_KEM. | Negative | P0 |
| TC-VV-QL-205 | FR-V.I-07 / file > 20MB | Upload file_bo_sung 25MB | `cb_nv_tw_01`. VV-K ở DANG_XU_LY. | file="big.pdf" (25MB) | 1. Upload file 25MB. | **STATE**: Backend reject (max 20MB). **UI**: Toast error "File vượt quá giới hạn 20MB. Kích thước: 25MB" (verify interpolation `{size}` thay 25 — pattern from BIEU_MAU). **PERSIST**: KHÔNG có record. | Negative | P0 |
| TC-VV-QL-206 | FR-V.I-07 / virus scan EICAR | Upload file chứa EICAR test signature | `cb_nv_tw_01`. VV-L ở DANG_XU_LY. File EICAR test signature trong `mau-virus.docx`. | file="mau-virus.docx" | 1. Upload. | **STATE**: ClamAV detect → reject. KHÔNG lưu file vào storage. **UI**: Toast error "File chứa mã độc, không thể tải lên" (SRS Gap exact message — mark **SPEC-CLARIFY-VV-QL-03**). **PERSIST**: KHÔNG có record. AUDIT_LOG ghi attempt + virus signature. | Negative | P0 |

---

## D. EDGE CASES

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-QL-301 | BR-EC-01 / Optimistic lock concurrent edit | 2 CB NV cùng edit Accordion 2 cùng VV | Tab1 `cb_nv_tw_01` + Tab2 `cb_nv_tw_02`. VV-M ở DANG_XU_LY. Cả 2 tab mở Accordion 2 [Sửa]. | Tab1 noi_dung="A", Tab2 noi_dung="B" | 1. Tab1 [Lưu]. 2. Tab2 [Lưu] (chưa reload). | **STATE**: Tab1 SUCCESS — VU_VIEC.noi_dung_yeu_cau = "A", updated_at mới. Tab2 FAIL với optimistic lock conflict (BR-EC-01). **UI**: Tab1 toast success. Tab2 modal "Vụ việc đã được CB Nghiệp vụ TW 01 cập nhật lúc dd/mm HH:mm. Vui lòng tải lại để xem thông tin mới nhất." (srs-fr-05:1623) + nút [Tải lại]. **PERSIST**: 1 entry CAP_NHAT_NOI_DUNG bởi cb_nv_tw_01. | Edge | P0 |
| TC-VV-QL-302 | FR-V.I-07 / file boundary 20MB | Upload file boundary 20MB exact (PASS) + 20MB+1byte (FAIL) | `cb_nv_tw_01`. VV-N ở DANG_XU_LY. | file20MB="exact-20mb.pdf" (20971520 bytes), file20MB1B="over.pdf" (20971521 bytes) | 1. Upload 20MB exact. 2. Upload 20MB+1B. | **STATE**: 20MB → INSERT thành công (CHECK <= 20971520, srs-fr-05:2260). 20MB+1B → reject. **UI**: 20MB toast success. 20MB+1B toast error "File vượt quá giới hạn 20MB". **PERSIST**: 20MB record OK; 20MB+1B KHÔNG record. | Edge | P1 |
| TC-VV-QL-303 | FR-V.I-07 / multi-file batch upload | Upload đồng thời 10 file (max) + 11 file (over) | `cb_nv_tw_01`. VV-O ở DANG_XU_LY. | 10 file PDF mỗi file 2MB | 1. Click [+ Thêm tài liệu]. 2. Drag-drop 10 file. 3. Lặp với 11 file. | **STATE**: 10 file → INSERT 10 entries FILE_DINH_KEM. 11 file → reject hoặc client-side limit (max 10 file pattern from srs-fr-05:317). **UI**: 10 file → progress 10 bar + toast success. 11 file → toast error "Tối đa 10 file/lần upload" (SRS Gap message — mark gap). **PERSIST**: 10 entries OK; 11 KHÔNG. | Edge | P1 |
| TC-VV-QL-304 | EC-01 / upload bị ngắt mạng | Upload 15MB, set offline khi 50% → cleanup blob orphan | `cb_nv_tw_01`. VV-P ở DANG_XU_LY. DevTools Network throttle Offline khi upload đang chạy. | file="mau-15mb.docx" | 1. Upload. 2. Đợi 50% progress. 3. Set Offline. 4. Đợi timeout. | **STATE**: Backend dọn blob mồ côi. KHÔNG có FILE_DINH_KEM record. **UI**: Toast error "Upload bị gián đoạn, vui lòng thử lại" (SRS Gap — mark **SPEC-CLARIFY-VV-QL-04**). **PERSIST**: Storage không có blob orphan. Retry upload cùng tên KHÔNG conflict. | Edge | P1 |
| TC-VV-QL-305 | DN scope / IDOR | DN sửa URL truy cập VV của DN khác | `dn_01` (DN-AG). VV-Y của DN-BG khác. | — | 1. Login `dn_01`. 2. Sửa URL `/ho-so-cua-toi/vu-viec/{id-Y}`. | **STATE**: Backend kiểm tra `VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id` (srs-fr-05:1881). Reject 403 + redirect `/ho-so-cua-toi/vu-viec` (srs-fr-05:1828). **UI**: Toast error "Bạn không có quyền truy cập vụ việc này" hoặc 403 page. **PERSIST**: AUDIT_LOG ATTEMPT_403 (security audit). | Edge | P0 |
| TC-VV-QL-306 | SCR-V.I-03 chế độ DN / Timeline filter | DN xem Timeline chỉ thấy event public (tiếp nhận/kết luận KT/KQ PD/HT/từ chối/CK), ẨN event nội bộ (phân công/trao đổi cán bộ) | `dn_01`. VV-Q của dn_01 đã trải qua: tiếp nhận → kiểm tra YCBS → bổ sung → kiểm tra DAT → phân công nht_01 → NHT xác nhận → KQ NHT → trình PD → PD duyệt → CB NV cập nhật KQ cuối → HOAN_THANH. | — | 1. Login `dn_01`. 2. Mở chi tiết VV-Q. 3. Quan sát Timeline. | **UI**: Timeline hiển thị event public: TIEP_NHAN, YEU_CAU_BO_SUNG, BO_SUNG_HS (DN), KIEM_TRA (DAT), PHE_DUYET (kết quả), HOAN_THANH (srs-fr-05:1845). ẨN event nội bộ: PHAN_CONG, XAC_NHAN_PHAN_CONG, CAP_NHAT_KQ (NHT), TRINH_PD, TU_CHOI_PD nội bộ. Verify count entries < count chế độ CMS. **PERSIST**: — | Edge | P1 |

---

## Tổng kết file

**Tổng TC: 21** (3 UI + 6 Happy + 6 Negative + 6 Edge) — sau Codex review 2026-05-09

| Section | TC IDs | Count |
|---------|--------|------:|
| A. UI verification | UI-01, UI-02, UI-03 | 3 |
| B. Happy | 101, 102, 103, 104, 105, 106 | 6 |
| C. Negative | 201, 202, 203, 204, 205, 206 | 6 |
| D. Edge | 301, 302, 303, 304, 305, 306 | 6 |

**Priority**: P0=11 / P1=8 / P2=2

> **Codex review 2026-05-09:**
> - CLEANUP recount confusion (line 59-63 — actual 21 TC, đã clarify count chính xác)
> - Coverage UC57 SRS đầy đủ — không thêm TC mới (BR/AC/Error/Processing 6/6 covered, 2 chế độ CMS+DN cover, IDOR + Timeline filter cover)
> - File mạnh ở: optimistic lock (TC-301), XSS (TC-203), file boundary (TC-302), virus EICAR (TC-206), DN IDOR (TC-305), DN Timeline filter (TC-306)

**Coverage:**
- BR: BR-AUTH-01, BR-AUTH-08 (DN scope — TC-305), BR-DATA-01 (file is_deleted), BR-DATA-05 (audit), BR-EC-01 (optimistic lock — TC-301), BR-EC-13 (XSS — TC-203), BR-FLOW-03 (cấm sửa sau PD — TC-201/202), file_dinh_kem cross-cutting (TC-204/205/206/302/303/304)
- Error codes: ERR-VV-02 (full coverage UC57 — only 1 error code in SRS:616)
- AC SRS: 3/3 (srs-fr-05:619-622) — AC1 (DS — actually scope file 01) / AC2 (chi tiết — TC-101) / AC3 (chỉnh sửa upload — TC-102/103)
- Processing steps: 6/6 covered (1 quyền — DN scope TC-305 + permission file 14 / 2 state guard / 3 update / 4 lưu file / 5 lịch sử — TC-105 Timeline / 6 audit — implicit)
- Outputs: 8/8 field tested via UI-01 + TC-101

**SPEC-CLARIFY:**
- **VV-QL-01**: HO_SO_VU_VIEC (file đính kèm) có counter so_luot_tai như BIEU_MAU không? SRS không quote
- **VV-QL-02**: Format reject message exact wording — SRS không quote
- **VV-QL-03**: ClamAV virus detect message exact wording (cross-ref BIEU_MAU SPEC-CLARIFY-BM-04)
- **VV-QL-04**: Upload bị ngắt timeout message exact wording
- **VV-QL-05**: SCR-V.I-03 chế độ DN — Timeline filter logic (event nào public vs nội bộ) cần BA enumerate
