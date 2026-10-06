# TODO v3 — UAT 2026-05-26 (aligned 1-1 với xlsx 55 STT)

**Ngày soạn:** 2026-06-02 00:50:00
**Thay thế:** [todo-uat-2026-05-26.md](todo-uat-2026-05-26.md) (v2) — deprecated từ ngày này.
**Nguồn 1-1:** `[PM HTPLDN] Danh sách tối ưu_Bug+API (6).xlsx` Sheet "Phần mềm" R5-R59 (STT 1-55).

## Tổng quan sai sót của plan/todo cũ

| # | Sai chỗ nào | Sửa thế nào |
|---|---|---|
| 1 | Plan/todo cũ chỉ tập trung 12 STT BA chốt nghiệp vụ → bỏ 36 bug UI thuần | File v3 này list đủ 55 STT |
| 2 | Thêm 6 task "API mock" (T5.5/T5.7/T5.8/T5.9 + T7.4/T7.5) KHÔNG có trong xlsx | Đánh dấu OPTIONAL, không tính skip |
| 3 | Phase 8 "Regression 43 mục" gom đại → treo chờ Q6 | Bỏ Phase 8 — re-test từng STT cụ thể |
| 4 | Treo 4 Q (Q7-Q10) chờ BA dù SRS đã answer | Convert thành actionable (xem progress-audit-2026-06-01.md) |
| 5 | Số liệu skip count sai (báo 21 nhưng thực ~32) | Recount theo xlsx |

## Convention status

| Icon | Nghĩa | Khi nào dùng |
|:-:|---|---|
| ✅ | Closed — fix đúng, re-test PASS | Dev fix + QA re-test PASS |
| ❌ | Open — fix sai hoặc còn bug | QA re-test FAIL |
| ⚠️ | Sai spec một phần | PASS happy nhưng deviate SRS minor |
| 🚫 | Bác bỏ — BA quyết không sửa | STT 6 R10, STT 9 (Khóa học), STT 55 (Video) |
| ⏳ | Chờ dev fix xong | xlsx "Đang thực hiện" |
| 🟡 | Chưa test (treo) | xlsx "Đã thực hiện - chờ test lại" mà QA chưa re-test |

---

## Tiến độ — UPDATE 2026-06-02 10:45

**Tổng 55 STT trong xlsx:**

| Kết quả | Số STT | STT nào |
|---|:-:|---|
| ✅ Đạt | 47 | 2,3,4,5,8-24,26-35,38,40,41,42,43,44,45-51,53,54,55 |
| ❌ Lỗi (đã log bug, chờ dev fix) | 8 | 1, 6, 7, 25, 36, 37, 39, 52 |
| 🚫 Chưa test được | 0 | — |

**Bug tổng (trong file [Bug/bug-report-uat-2026-05-26.md](Bug/bug-report-uat-2026-05-26.md)): 12 bug — LATEST R22 2026-06-05: 11 Closed + 1 Open (BUG-UI-T1.4-002 ⚠️ nhãn "Tạo mới" trái H4 — chờ dev đổi nhãn). Bảng dưới là snapshot gốc lúc log (lịch sử), xem status mới nhất ở bug report.**

| Bug ID | Mức | STT liên quan | Tình trạng |
|---|:-:|:-:|---|
| BUG-HD-T1.1-001 | Minor | 7 | Open — editor 20k ký tự không báo lỗi |
| BUG-UI-T1.4-001 | Minor | 1 | Open — UI đào tạo thiếu count |
| BUG-UI-T1.4-002 | Minor | 1 | Open — nhãn nút Lưu không thống nhất |
| BUG-HD-T2.3-001 | Major | 6 | Open — CG vẫn thấy menu Hỏi đáp |
| BUG-VV-T5.2-001 | Major | 39 | Open — modal DN trong VV thiếu nút Thêm |
| BUG-DBC-T6.3-001 | Minor | 52 | Open — CB ĐP thấy nút Thêm Đợt báo cáo |
| BUG-BG-T24-001 | Medium | 24→25 | Open — Bài giảng PDF không preview |
| BUG-VV-T36-001 | Major | 36 | Open — Kiểm tra hồ sơ không lưu kết quả |
| BUG-VV-T37-001 | Minor | 37 | Open — back tab không giữ |
| BUG-DN-T7.7-001 | Major | — (ngoài 55 STT) | Open |
| BUG-AUTH-T5.4-001 | Minor | — (ngoài 55 STT) | Open |
| BUG-DG-T41-001 | Major | 41 | ✅ Closed — đã verify PASS |

**Note:** 1 STT có thể có 0-2 bug → tổng bug Open (11) > tổng STT lỗi (8) vì STT 1 có 2 bug + có 2 bug ngoài 55 STT.

---

## Bảng full 55 STT × QA Status

| STT | Row | Loại | Mức | Trạng thái xlsx | Module | Mô tả ngắn | QA Status | Bug ID | Note |
|:-:|:-:|:-:|:-:|---|---|---|:-:|---|---|
| 1 | R5 | Task | TB | Đang thực hiện | 0. Chung | UI/UX đồng nhất 7 nhóm | ⚠️ | BUG-UI-T1.4-001/002 | H2 + H4 fail |
| 2 | R6 | Task | Cao | Đang thực hiện | 0. Chung | Logo + tên phần mềm | ✅ | — | Re-test 2026-06-02: Logo HTPLDN (`logo.svg`) load OK + header "Bộ Tư Pháp / Hỗ trợ pháp lý doanh nghiệp / HTPLDN · v1.0" + page title đúng |
| 3 | R7 | Bug | Thấp | Chờ test lại | II Hỏi đáp | Popup đè text + button | ✅ | — | Popup Xóa HD layout sạch — text y120-196 / btn y208-240, no overlap |
| 4 | R8 | Bug | Thấp | Chờ test lại | II Hỏi đáp | Popup hiện mã `TIEP_NHAN` thay text | ✅ | — | Cột Trạng thái + popup hiển thị "Tiếp nhận" tiếng Việt, no raw enum |
| 5 | R9 | Bug | TB | Chờ test lại | II Hỏi đáp | Modal Phân công thiếu TVV (BA gộp STT 6) | ✅ | — | T2.2 PASS — modal chỉ CB HTPL, đúng STT 6 |
| 6 | R10 | Task | Cao | **Hủy** | II Hỏi đáp | TVV menu Hỏi đáp (BA bác) | ❌ | BUG-HD-T2.3-001 | FE chưa ẩn menu khỏi CG |
| 7 | R11 | Task | TB | Đang thực hiện | II Hỏi đáp | Editor + bỏ giới hạn 5k → 20k | ⚠️ | BUG-HD-T1.1-001 | Silent block 20001 |
| 8 | R12 | Bug | TB | Chờ test lại | III Đào tạo | Thiếu cột Hành động danh sách KHĐT | ✅ | — | Re-test 2026-06-02 R20 `_02`: KHĐT có cột Hành động (eye/edit/delete) |
| 9 | R13 | Task | Cao | Đang thực hiện | III Đào tạo | File đính kèm KHĐT/CTĐT/KH | ✅ | — | T1.3 PASS 3/3 nhánh |
| 10 | R14 | Task | TB | Đang thực hiện | III Đào tạo | Toast công khai KHĐT | ✅ | — | T7.3 PASS — toast hiển thị đúng |
| 11 | R15 | Bug | TB | Chờ test lại | III Đào tạo | Ngân sách thiếu ngăn cách hàng nghìn | ✅ | — | Re-test 2026-06-02 R20 `_02`: KHĐT `900.000.000` + CTĐT `500.000.000 ₫` đúng format |
| 12 | R16 | Bug | TB | Chờ test lại | III Đào tạo | Trạng thái Dự thảo thiếu nút Sửa riêng | ✅ | — | Re-test 2026-06-02 R20 `_02`: KHĐT Nháp có icon edit + button "Chỉnh sửa" trong detail |
| 13 | R17 | Bug | Cao | Chờ test lại | III Đào tạo | Không hiển thị cột Lĩnh vực | ✅ | — | Re-test 2026-06-02 R20 `_02`: CTĐT list có cột "Lĩnh vực" |
| 14 | R18 | Bug | Thấp | Chờ test lại | III Đào tạo | Lịch sử phê duyệt không realtime | ✅ | — | Re-test 2026-06-02 R20 `_02`: timestamp submit 00:10 + duyệt 00:12 xuất hiện ngay sau action (realtime OK) |
| 15 | R19 | Bug | Cao | Chờ test lại | III Đào tạo | Bản ghi Đã tiếp nhận thiếu button | ✅ | — | Workflow KHĐT hiện tại không có state "Đã tiếp nhận" (Nháp/Chờ duyệt/Đã duyệt/Từ chối/Đã công khai) — state removed |
| 16 | R20 | Bug | Thấp | Chờ test lại | III Đào tạo | Button "Hủy" hiển thị "Rút bản nháp" | ✅ | — | Re-test 2026-06-02 R20 `_02`: modal Edit KHĐT Nháp button "Hủy" + "Cập nhật" đúng wording |
| 17 | R21 | Bug | Cao | Chờ test lại | III Đào tạo | DS học viên thiếu Thêm + Import | ✅ | — | Re-test 2026-06-02 R20 `_02`: tab Học viên KH-20260601-001 có button Thêm + Import |
| 18 | R22 | Bug | Cao | Chờ test lại | III Đào tạo | Địa điểm/zoom bắt buộc khi lưu | ✅ | — | Re-test 2026-06-02 R20 `_02`: form Lịch học cho phép lưu Trực tuyến không cần URL zoom (không required) |
| 19 | R23 | Bug | TB | Chờ test lại | III Đào tạo | Định dạng ngày trong toast lỗi sai | ✅ | 2026-06-02 | Toast trùng giờ buổi học format `(09:00:00–11:00:00)` HH:MM:SS sạch, không ISO lỗi |
| 20 | R24 | Bug | Cao | Chờ test lại | III Đào tạo | Không hiển thị DS bài giảng để gán | ✅ | — | Re-test 2026-06-02 R20 `_02`: tab Bài giảng KH render DS bài giảng để gán OK |
| 21 | R25 | Bug | TB | Đang thực hiện | III Đào tạo | Cache bản ghi cũ khi mở Thêm bài giảng | ✅ | — | Re-test 2026-06-02 `cb_nv_dp_02`: Edit BG "R2 Test CTDT-013" → close → Thêm bài giảng → form empty (Tên/Mô tả/Tệp đều rỗng) — không cache |
| 22 | R26 | Bug | Cao | Chờ test lại | III Đào tạo | Mô tả bài giảng bắt buộc khi lưu | ✅ | — | Re-test 2026-06-02 R20 `_02`: form Thêm bài giảng textarea Mô tả không còn `*` required |
| 23 | R27 | Bug | Cao | Chờ test lại | III Đào tạo | Cột Khóa học thừa | ✅ | — | Re-test 2026-06-02 R20 `_02`: DS bài giảng không còn cột "Khóa học" (đã bỏ) |
| 24 | R28 | Bug | TB | Open | III Đào tạo | Không preview PDF | ✅ | BUG-BG-T24-001 **Closed** | Re-test 2026-06-02 09:35 `cb_nv_tw_02`: click Xem BG "R2 Test CTDT-013" → modal "Xem trước" có iframe 752x500 chứa MinIO signed URL inline OK. Dev đã fix |
| 25 | R29 | Task | Cao | Đang thực hiện | III Đào tạo | Tách Đề kiểm tra khỏi phân phối | ✅ + 🟡 | — | T3.1 PASS SM, T3.2 ⚠️ chờ test duplicate |
| 26 | R30 | Bug | Cao | Chờ test lại | III Đào tạo | GV vai trò theo Lịch học (STT 26 BA) | ✅ | — | Re-test 2026-06-02 R20 `_02`: form Lịch học có dropdown vai trò GV theo từng buổi (Giảng/Trợ giảng) |
| 27 | R31 | Bug | Cao | Chờ test lại | III Đào tạo | Cột Thời gian/Vai trò/Trạng thái hiện mã | ✅ | — | Tạo buổi học KH-20260601-001: ngày "15/06/2026" dd/mm/yyyy + giờ "09:00:00–11:00:00" + Hình thức "Trực tiếp" tiếng Việt, không enum |
| 28 | R32 | Bug | Cao | **Đang thực hiện** | IV TVV | Preview file đính kèm TVV lỗi | ✅ | — | Re-test 2026-06-02 `cb_nv_tw_02`: TVV-HDSD-AG-01 detail File đính kèm "Danh sách tư vấn viên 1.pdf" → click Xem → mở tab MinIO signed URL inline OK |
| 29 | R33 | Bug | Cao | Chờ test lại | IV TC TV | Thêm TC TV báo trùng dù chưa có | ✅ | — | Re-test 2026-06-02 R20 `cb_nv_tw_02`: tạo TC mới (tên+sốĐKHĐ unique) → 201 Created, không bị BE báo trùng |
| 30 | R34 | Bug | Cao | Chờ test lại | IV TC TV | TC TV chờ duyệt thiếu nút phê/từ chối | ✅ | — | Re-test 2026-06-02 R20 `cb_pd_tw_02`: detail TC "Chờ phê duyệt" section Thao tác có đủ 2 button "Phê duyệt" + "Từ chối" |
| 31 | R35 | Bug | TB | Chờ test lại | V VV | Sửa VV nút Sửa thừa → list | ✅ | — | List VV: nút Sửa chỉ hiện khi state "Đã tiếp nhận", state-gated đúng |
| 32 | R36 | Bug | Cao | Chờ test lại | V VV | Lưu nháp VV → Tiếp nhận lỗi | ✅ | — | Tạo VV-BTP-TW-20260602-001 nháp → Tiếp nhận OK ("Tiếp nhận vụ việc thành công") |
| 33 | R37 | Bug | Cao | Chờ test lại | V VV | Phân công ngoài đơn vị (STT 33 BA) | ✅ | — | T4.2-T4.5 PASS — TVV/CG toàn quốc, NHT lọc đơn vị |
| 34 | R38 | Bug | Thấp | Đang thực hiện | V VV | VV đã phân công vẫn còn nút Phân công | ✅ | — | Re-test 2026-06-02 `cb_nv_dp_02`: VV-QA-R9-DVC-002 state "Đang xử lý" top-level chỉ có "Cập nhật kết quả" + "Trình phê duyệt", không có nút Phân công thừa |
| 35 | R39 | Bug | TB | Chờ test lại | V VV | SLA + Ngày nộp đè + màu trắng | ✅ | — | List VV: cột Deadline/Cảnh báo tách riêng, tag "Còn 10 ngày" rgb(56,158,13) xanh trên bg sáng |
| 36 | R40 | Bug | Cao | Chờ test lại | V VV | Không lưu kết quả thẩm định | ❌ | BUG-VV-T36-001 | R20 2026-06-02 cb_nv_bn_01: tạo VV-BKH-20260602-001, submit Kiểm tra hồ sơ 6 hạng mục Đạt → state advance "Đang kiểm tra" + timeline OK, NHƯNG section Kết quả kiểm tra trống "—" + "Chưa có dữ liệu" → checklist không persist |
| 37 | R41 | Bug | Thấp | Chờ test lại | V VV | Phê duyệt back tab cũ | ❌ | BUG-VV-T37-001 | R20 2026-06-02 cb_pd_tw_02: mở VV-QA-R9-HTK-001 từ tab Chờ phê duyệt → click back → URL mất tab param, active "Tất cả" |
| 38 | R42 | Bug | Thấp | Chờ test lại | V VV | Số tiền/Ngày định dạng sai | ✅ | — | Chi trả list: số "4.740.711" dot-separator + ngày "05/04/2026" dd/mm/yyyy đúng VN |
| 39 | R43 | Bug | Cao | Đang thực hiện | V DN | Không có nút Thêm mới DN (STT 39 BA) | ✅ + ❌ | BUG-VV-T5.2-001 | T5.1 PASS nút Thêm mới; T5.2 FAIL modal trong VV thiếu CTA |
| 40 | R44 | Bug | Cao | Đang thực hiện | V VV | Loại DN hiển thị id | ✅ | — | Re-test 2026-06-02: DN detail field "Loại doanh nghiệp" hiện "Công ty cổ phần (đã ngừng)" tiếng Việt, không id/enum |
| 41 | R45 | Bug | Cao | Open | VI Đánh giá | Thêm đợt không lưu file | ✅ | BUG-DG-T41-001 **Closed** | Re-test 2026-06-02 09:38 `cb_nv_tw_02`: upload stt41-verify.pdf vào DG-20260602-0002 → BE `fileDinhKem=[stt41-verify.pdf 88B SACH]` → reload UI hiện file + delete button. Dev đã fix |
| 42 | R46 | Bug | TB | Chờ test lại | VI Đánh giá | DS VV thiếu Tên/Lĩnh vực/Trạng thái | ✅ | — | DG-20260512-0001 tab Thực hiện: cột Mã VV / Tên VV / Lĩnh vực / Trạng thái / Đã chọn đủ. Note minor: Trạng thái hiện enum "HOAN_THANH" thay "Hoàn thành" |
| 43 | R47 | Bug | Cao | Chờ test lại | VI Đánh giá | Chọn VV xong list vẫn hiện chưa chọn | ✅ | — | VV-HDSD-003 đã chọn → cột "Đã chọn?" hiển thị badge "Đã chọn" đúng |
| 44 | R48 | Bug | TB | Chờ test lại | VI Đánh giá | Toast lỗi kèm khi hoàn thành chấm | ✅ | — | Login `cb_nv_tw_06` (người được phân công DG-20260512-0001) → chấm 85 → Lưu kết quả OK → Hoàn tất chấm điểm → confirm popup → toast "Hoàn tất chấm điểm thành công" + alert success "Đã chuyển sang giai đoạn báo cáo". KHÔNG có toast lỗi kèm. Screenshot: image/stt44-hoantat-chamdiem-pass.png |
| 45 | R49 | Bug | TB | Chờ test lại | VI Đánh giá | Số liệu + Xếp loại + Trạng thái hiện mã | ✅ | — | Re-test 2026-06-02 R20: DS Đánh giá cột Tần suất/Đối tượng/Trạng thái render label tiếng Việt ("Sơ bộ 6 tháng"/"Vụ việc"/"Lập kế hoạch"), không phải mã |
| 46 | R50 | Bug | Cao | Chờ test lại | VI Đánh giá | Ngày bắt đầu/kết thúc lùi 1 ngày | ✅ | — | Re-test 2026-06-02 R20: nhập 15/06/2026 → 30/06/2026 → DS hiện đúng 15/06/2026 và 30/06/2026, không lùi |
| 47 | R51 | Bug | Cao | Chờ test lại | VII Biểu mẫu | Thiếu menu DS biểu mẫu | ✅ | — | Re-test 2026-06-02 R20 `cb_nv_tw_02`: sidebar có Biểu mẫu → "Thư mục biểu mẫu" + "Danh sách biểu mẫu" |
| 48 | R52 | Bug | TB | Chờ test lại | VII Biểu mẫu | Preview + Tải xuống lỗi | ✅ | — | Re-test 2026-06-02 R20: Xem trước mở tab MinIO inline OK + Tải về trigger presigned attachment OK (BM-HDSD-AG-003 PDF) |
| 49 | R53 | Bug | Cao | Đang thực hiện | XI KHTH | Thêm mới không upload file | ✅ | — | Re-test 2026-06-02 `cb_nv_tw_02`: form Tạo CT HTPLDN mới có field "File đính kèm" + button "upload Tải lên" |
| 50 | R54 | Bug | TB | Chờ test lại | XI KHTH | DS Mục tiêu không hiện data | ✅ | — | Re-test 2026-06-02 R20 `cb_nv_tw_02`: DS CT HTPLDN cột "Mục tiêu" hiện data đầy đủ 20/20 record |
| 51 | R55 | Bug | TB | Chờ test lại | XI KHTH | Tab Tài liệu thừa | ✅ | — | Re-test 2026-06-02 R20: detail CT (cả Dự thảo + Đang thực hiện) chỉ còn 1 tab "Thông tin", không còn tab Tài liệu thừa |
| 52 | R56 | Bug | Cao | Chờ test lại | XI Đợt BC | Đợt BC gắn CT + thiếu phạm vi (STT 52 BA) | ✅ + ❌ | BUG-DBC-T6.3-001 | T6.1 PASS form, T6.3 FAIL DP/BN thấy Thêm mới |
| 53 | R57 | Bug | Thấp | Đang thực hiện | X TVCS | Popup text phê duyệt câu hỏi sai | ✅ | — | R20 2026-06-02 cb_pd_tw_02: popup "Duyệt câu hỏi" body "Bạn xác nhận phê duyệt câu hỏi?" + buttons Hủy/Duyệt — wording OK |
| 54 | R58 | Bug | Thấp | Chờ test lại | X TVCS | Thiếu cột Hành động + hyperlink mã | ✅ | — | DS TVCS có cột Hành động (eye/team/edit/delete) + mã là `<a>` hyperlink |
| 55 | R59 | Task | Cao | Đang thực hiện | III Video | Upload file video (BA bác) | ✅ | — | T1.2 PASS — chỉ YouTube, không button upload |

---

## Bug Open thêm ngoài 48 STT xlsx (phát hiện khi test)

Test 12 STT BA chốt phát hiện thêm bug KHÔNG có trong xlsx đối tác — log riêng:

| Bug ID | Severity | Task internal | Spec |
|---|:-:|---|---|
| BUG-AUTH-T5.4-001 | Major | T5.4 (test Claim Flow STT 39) | `srs-fr-10-quan-tri.md:1285` Form Quên MK chỉ accept email |
| BUG-DN-T7.7-001 | Medium | T7.7 (test optimistic lock STT 10) | Phụ lục E Mục I — BE không enforce version field |

→ Total bug Open hiện tại: **48 STT xlsx tracking + 2 bug QA phát hiện thêm = 50 vấn đề tracking**.

---

## Recount cuối session 2026-06-02 09:55

| Hạng mục | Số | STT |
|---|:-:|---|
| Tổng STT xlsx | 55 | — |
| ✅ Đạt | 46 | 2,3,4,5,8-23,24,26-35,38,40,41,45-51,53,54,55 + part 25,39,52 |
| ⚠️ Sai spec / bug Open track | 2 | 1, 7 |
| ❌ FAIL bug Open | 4 | 6 (BA bác), 24 (đã PASS R20 — flip ✅), 37 (mới log), 41 (đã PASS R20 — flip ✅) + part 39, 52 |
| 🚫 Cần seed lifecycle | 4 | 36 (BN thẩm định), 42, 43, 44 (Đánh giá full lifecycle) |
| **Tổng** | **55** | — |

**Bug QA phát hiện thêm:** 3 (BUG-AUTH-T5.4-001 + BUG-DN-T7.7-001 + BUG-VV-T37-001)
**Bugs đã verify Closed session này:** 2 (BUG-BG-T24-001 + BUG-DG-T41-001)
**Total tracking:** **58 vấn đề** (55 xlsx + 3 QA add)

---

## Action plan ngay

### Còn lại — cần làm gì

| STT | Vì sao chưa pass | Cần làm gì | Ai |
|:-:|---|---|:-:|
| 1 | UI/UX subjective | BA review chốt sửa/accept | BA |
| 6 | CG vẫn thấy Hỏi đáp | Dev gỡ menu Hỏi đáp khỏi sidebar CG | Dev FE |
| 7 | Editor 20k silent block | Dev hiện thông báo lỗi khi vượt 20k | Dev FE |
| 25 | Bài giảng PDF không preview | Dev nhúng preview PDF | Dev FE |
| 36 | Checklist Kiểm tra hồ sơ không lưu | Dev BE lưu payload 6 hạng mục | Dev BE |
| 37 | Back tab mất query param | Dev FE giữ `?tab=` khi back | Dev FE |
| 39 | Modal DN trong VV thiếu nút Thêm | Dev FE thêm nút Thêm trong modal | Dev FE |
| 52 | CB ĐP thấy nút Thêm Đợt báo cáo | Dev FE ẩn nút theo role | Dev FE |

### Ưu tiên 2 — Chờ dev fix STT ❌ rồi test

Push dev notify khi fix xong → QA test ngay (5 phút/bug).

### Optional — 6 task tự thêm (T5.5/T5.7-9, T7.4/T7.5)

Gỡ khỏi todo. Test sau khi có sandbox Cổng PLQG + LGSP.

---

## Tóm tắt sửa file todo cũ

| File | Action |
|---|---|
| [todo-uat-2026-05-26.md](todo-uat-2026-05-26.md) v2 | Mark DEPRECATED, giữ làm history. Trỏ về file v3 này. |
| [plan-uat-2026-05-26.md](plan-uat-2026-05-26.md) | Update note: scope mở rộng từ 12 STT BA chốt sang full 55 STT xlsx |
| File v3 này | Source of truth duy nhất từ 2026-06-02 00:50:00 |
| [Bug/bug-report-uat-2026-05-26.md](Bug/bug-report-uat-2026-05-26.md) | Giữ — chứa 8 bug đã log với SRS line |
| [Bug/tong-hop-case-chua-pass.md](Bug/tong-hop-case-chua-pass.md) | Sẽ regen sau khi re-test 35 bug 🟡 |

---

## Bạn confirm

**Tôi sẽ chạy 35 bug re-test ngay không?** Ước tính 85 phút, output bảng 35 STT × Status sau khi xong.

Hoặc bạn muốn:
- (a) Chạy ngay full 35 (~85')
- (b) Test cluster Cao priority trước (~50' cho 20 bug Cao + TB Cao)
- (c) Test module quan trọng nhất trước (Đào tạo 16 bug ~35')
- (d) Khác

*Last update: 2026-06-02 00:50:00.*
