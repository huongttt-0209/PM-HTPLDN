# Test Cases — FR-IV-08: Công khai TVV + TC TV lên Cổng PLQG

> **SRS Ref**: FR-IV-08 (UC46), SCR-IV-01 batch + SCR-IV-03 modal MD-CONG-KHAI + SCR-IV-NEW-01/03, Entity TU_VAN_VIEN/TO_CHUC_TU_VAN
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:631-685`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CK-UI-01 | FR-IV-08 / SCR-IV-03 / Modal MD-CONG-KHAI | Verify modal MD-CONG-KHAI có 2 field nhập | cb_nv_tw_01, TVV-TW-600 HOAT_DONG | — | 1. Mở chi tiết TVV-TW-600<br>2. Click "Công khai" header → Modal MD-CONG-KHAI | **MODAL fields**: mo_ta_cong_khai* (textarea max 5000 ký, REQUIRED), file_dinh_kem_cong_khai (file upload PDF/DOC/DOCX/XLS/XLSX max 20MB/file, multi files, optional)<br>**Title**: "Công khai lên Cổng pháp luật quốc gia"<br>**Cảnh báo**: "Sau khi công khai, thông tin **{tên}** sẽ hiển thị toàn quốc trên Cổng pháp luật quốc gia. Bạn có thể hủy công khai bất kỳ lúc nào — mô tả + file vẫn được giữ lại để tái công khai sau."<br>**Buttons**: "Công khai" (primary) / "Hủy" | Happy 🔴 |
| TC-CK-UI-02 | FR-IV-08 / SCR-IV-01 batch | Verify batch action "Công khai" trên SCR-IV-01 | cb_nv_tw_01, ≥3 TVV HOAT_DONG | — | 1. SCR-IV-01 tab "Đang hoạt động" check 3 row<br>2. Verify action bar | Action bar có "Công khai hàng loạt" / "Hủy công khai hàng loạt" | Happy 🟡 |

## B. Công khai TVV cá nhân

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CK-001 | FR-IV-08 / AC1 | Happy path công khai TVV HOAT_DONG | cb_nv_tw_01, TVV-TW-600 HOAT_DONG, MailHog UP | mo_ta_cong_khai: "TVV chuyên môn Lao động 10+ năm" + 1 file PDF 5MB | 1. Click Công khai → Modal<br>2. Nhập mô tả + upload file<br>3. Confirm | **STATE**: TU_VAN_VIEN cập nhật cong_khai=1, thoi_gian_dang_tai=NOW, mo_ta_cong_khai, file_dinh_kem_cong_khai; **API outbound** `POST https://congphapluat.gov.vn/api/v1/tu-van-vien` với 9 trường whitelist BR-PUBLIC-04 (NHƯNG file FR-04 dùng FR-IV-08 + entity TVV — verify SRS); AUDIT_LOG<br>**UI**: Toast "Công khai thành công"; Badge "Đã công khai" hoặc switch state ON<br>**PERSIST**: Mở Cổng PLQG (mock) thấy TVV-TW-600 | Happy 🔴 |
| TC-CK-002 | FR-IV-08 / TVV CHO_KICH_HOAT công khai (mới v3.1) | TVV vừa được phê duyệt CHO_KICH_HOAT vẫn được công khai | cb_nv_tw_01, TVV-TW-601 CHO_KICH_HOAT (vừa qua FR-IV-07) | mo_ta_cong_khai | 1. Click Công khai TVV CHO_KICH_HOAT<br>2. Verify | **STATE**: PASS — TVV ở CHO_KICH_HOAT vẫn được công khai (v3.1 nới điều kiện theo Thay đổi 4 phần 2 — vì TVV đã được pháp lý công nhận, chưa cần đợi kích hoạt TK)<br>**UI**: Toast "Công khai thành công" | Edge 🔴 |
| TC-CK-003 | FR-IV-08 / E1 ERR-CK-01 | TVV TAM_DUNG cố công khai → ERR-CK-01 | cb_nv_tw_01, TVV-TW-602 TAM_DUNG | — | 1. Cố click Công khai (DevTools force) | API 400 "Chỉ tư vấn viên đã được công nhận (Chờ kích hoạt hoặc Đang hoạt động) hoặc tổ chức đang hoạt động mới được công khai" (NGUYÊN VĂN ERR-CK-01); UI nút "Công khai" disabled | Negative 🔴 |
| TC-CK-004 | FR-IV-08 / E2 ERR-CK-02 | Công khai thiếu mô tả → ERR-CK-02 | cb_nv_tw_01 | mo_ta_cong_khai: "" | 1. Modal Confirm không nhập mô tả | Inline error "Mô tả công khai là bắt buộc trước khi đẩy lên Cổng pháp luật quốc gia" (NGUYÊN VĂN ERR-CK-02) | Negative 🟡 |
| TC-CK-005 | FR-IV-08 / Hủy công khai | Hủy công khai → giữ lại mô tả + file để tái công khai | cb_nv_tw_01, TVV-TW-600 cong_khai=1 | — | 1. Click "Hủy công khai" → Modal MD-HUY-CONG-KHAI<br>2. Confirm | **STATE**: cong_khai=0, thoi_gian_dang_tai=NULL, **mo_ta_cong_khai + file_dinh_kem_cong_khai GIỮ LẠI** (BR-PUBLIC-02); API outbound DELETE Cổng<br>**UI**: Toast "Hủy công khai thành công"<br>**PERSIST**: Tái công khai → modal pre-filled mô tả cũ | Happy 🔴 |
| TC-CK-006 | FR-IV-08 / WRN-CK-01 retry | API Cổng PLQG fail → retry 3 lần (BR-PUBLIC-03) | cb_nv_tw_01, mock Cổng API down | — | 1. Click Công khai<br>2. Verify retry | **STATE**: cong_khai vẫn 0 (chưa OK Cổng); BR-EC-20 KHÔNG set cong_khai trước API OK<br>**UI**: Warning "Cập nhật Cổng pháp luật quốc gia thất bại, sẽ thử lại" (NGUYÊN VĂN WRN-CK-01)<br>**PERSIST**: Backend queue retry 5 phút, max 10 lần, email admin (BR-PUBLIC-03) | Edge 🔴 |

## C. Công khai Tổ chức TV

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CK-101 | FR-IV-08 / TC TV HOAT_DONG | Công khai TC TV HOAT_DONG | cb_nv_tw_01, TC-TW-001 HOAT_DONG | mo_ta + file | 1. Mở SCR-IV-NEW-03<br>2. Click Công khai<br>3. Modal MD-CONG-KHAI<br>4. Confirm | **STATE**: TO_CHUC_TU_VAN cập nhật cong_khai=1; API outbound POST Cổng với ref_type='TO_CHUC_TU_VAN'; AUDIT_LOG<br>**UI**: Toast "Công khai thành công"<br>**PERSIST**: Cổng PLQG hiển thị TC-TW-001 | Happy 🔴 |
| TC-CK-102 | FR-IV-08 / TC TV không HOAT_DONG → ERR-CK-01 | TC TV CHO_PHE_DUYET → reject | cb_nv_tw_01, TC-TW-002 CHO_PHE_DUYET | — | 1. Cố click Công khai | API 400 ERR-CK-01 (NGUYÊN VĂN); KHÔNG cập nhật | Negative 🟡 |

## D. Batch + LEGAL-09 toàn quốc

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CK-201 | FR-IV-08 / Batch Công khai | Công khai hàng loạt 3 TVV | cb_nv_tw_01, 3 TVV-TW-700/701/702 HOAT_DONG | shared mô tả "Đợt công khai T05/2026" + 1 file chung | 1. Tab Đang hoạt động check 3 row<br>2. Action "Công khai hàng loạt" | 3 record cùng cập nhật cong_khai=1; 3 API call đồng thời (hoặc batch); Toast "Đã công khai 3 tư vấn viên thành công"; Modal MD-CONG-KHAI-PARTIAL-FAIL nếu N-K thành công | Happy 🟡 |
| TC-CK-202 | FR-IV-08 / BR-LEGAL-09 toàn quốc | TVV cong_khai=1 thuộc HN hiển thị cho user HP | tvv_HN_001 cong_khai=1, cb_nv_dp_HP_01 | — | 1. Login cb_nv_dp_HP_01<br>2. Mở SCR-IV-01 — nhưng filter khác đơn vị<br>3. Cổng PLQG public view | TVV của HN KHÔNG hiển thị trong CMS list của HP (BR-AUTH-08); NHƯNG Cổng PLQG public view hiển thị toàn quốc → DN ở HP tra cứu thấy TVV của HN (BR-LEGAL-09) | Happy 🔴 |
| TC-CK-203 | FR-IV-08 / VO_HIEU_HOA tự gỡ Cổng | TVV đã cong_khai=1 → VO_HIEU_HOA → tự gỡ Cổng (BR-PUBLIC-02) | cb_nv_tw_01, TVV-TW-703 cong_khai=1 HOAT_DONG | — | 1. Click "Vô hiệu hóa"<br>2. Confirm + lý do<br>3. Verify Cổng | **STATE**: TU_VAN_VIEN.trang_thai=VO_HIEU_HOA, cong_khai=0 auto, thoi_gian_dang_tai=NULL; API outbound DELETE Cổng (theo FR-IV-12 step 4)<br>**UI**: Toast "Vô hiệu hóa thành công, đã gỡ khỏi Cổng PLQG"<br>**PERSIST**: Cổng public KHÔNG còn TVV-TW-703 | Happy 🔴 |
| TC-CK-204 | FR-IV-08 / Tab Lịch sử công khai | History công khai/hủy lưu trong AUDIT_LOG | qtht_01 | — | 1. Mở Tab Audit (nếu có) hoặc check AUDIT_LOG qua FR-VIII-28<br>2. Verify entries | Mỗi action CONG_KHAI / HUY_CONG_KHAI insert AUDIT_LOG entry với user + timestamp + diff cong_khai 0↔1; Verify qua FR-VIII-28 list audit | Edge 🟡 |

---

## E. EDGE bổ sung (A4 inline merge — 4 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CK-301 | EDGE-A4-c / Race công khai vs vô hiệu hóa | 2 user đồng thời (1 công khai, 1 vô hiệu hóa) | cb_nv_tw_01 (công khai) + cb_nv_tw_02 (vô hiệu hóa) cùng TVV-TW-700 HOAT_DONG cong_khai=0 | — | 1. 2 tab cùng submit | Race: vô hiệu hóa win (precedence) → TVV chuyển VO_HIEU_HOA, cong_khai=0; công khai bị reject ERR-CK-01 (state đã thay đổi); SPEC-CLARIFY-CGTVV-15 nếu SRS không quy định precedence | Edge 🔴 |
| TC-CK-302 | EDGE-A4-w / API Cổng timeout 30s + queue retry | API Cổng timeout 30s → BR-PUBLIC-03 queue retry (verify qua UI list reload) | cb_nv_tw_01, mock Cổng API timeout >30s | — | 1. Click Công khai<br>2. **Verify qua list reload** sau 5 phút | Network timeout sau 30s; **STATE**: cong_khai vẫn 0 (BR-EC-20); UI WRN-CK-01 immediately; **A7 SỬA: verify retry success qua list reload sau 5 phút (cong_khai=1) + verify Cổng PLQG public hiển thị TVV; KHÔNG verify queue table trực tiếp** | Edge 🔴 |
| TC-CK-303 | EDGE-A4-dd / Batch mixed states | Batch công khai 5 TVV (3 HOAT_DONG + 1 CHO_KICH_HOAT + 1 TAM_DUNG) | cb_nv_tw_01 | mixed | 1. Check 5 row → Công khai hàng loạt | 4 PASS (3 HOAT_DONG + 1 CHO_KICH_HOAT theo v3.1 BR-PUBLIC-01 nới); 1 FAIL TAM_DUNG ERR-CK-01; UI MD-CONG-KHAI-PARTIAL-FAIL "Đã công khai 4/5, 1 thất bại do trạng thái" | Edge 🔴 |
| TC-CK-304 | EDGE-A4-i / Sanitize javascript: URI | mo_ta_cong_khai chứa `javascript:alert(1)` | cb_nv_tw_01 | mo_ta_cong_khai: `<a href="javascript:alert(1)">Click</a>` | 1. Submit | DB lưu sau sanitize (strip `javascript:` URI); UI render plain text hoặc href trống; KHÔNG execute alert | Edge 🔴 |

---

**Tổng số TC**: 18 (2 UI + 6 TVV + 2 TC TV + 4 Batch/LEGAL/VO_HIEU + 4 Edge A4) — A6 sẽ điều chỉnh
