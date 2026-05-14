# Impact map BA Round 7 đã áp dụng

**Ngày cập nhật:** 2026-05-11  
**Nguồn chuẩn:** `output/BA-report/tra-loi-ba-round7-srs-v3.5-2026-05-11.md`

File này trace nhanh các quyết định BA đã được áp dụng vào tracker/report QA. Chỉ cập nhật phần expected/current verdict/action item; evidence lịch sử vẫn giữ nguyên.

## Quyết định đã apply

| Mục BA | Quyết định chuẩn | File đã cập nhật |
|---|---|---|
| FR-05.1 Duplicate đánh giá | Duplicate theo `(vu_viec_id, loai_nguoi_danh_gia)`, lỗi `ERR-DG-VV-03`; không dùng `ERR-DG-VV-04` cho duplicate | `bug-reports/vu-viec/non-dev-followup-vu-viec.md`, `bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md`, `functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md` |
| FR-05.2 Thiếu dữ liệu ưu tiên DN | Chặn/cảnh báo, yêu cầu DN cập nhật; không fallback âm thầm priority 3 | `bug-reports/vu-viec/non-dev-followup-vu-viec.md`, `bug-reports/vu-viec/dev-seed-request-vu-viec.md`, `functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md`, `bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md` |
| FR-05.3 Phân công khác đơn vị | Không cho nếu người nhận không xem được VV; UI lọc hoặc BE reject | `workflow/vu-viec/workflow-test-report-r7-4-a3-vu-viec.md` |
| FR-05.4 SLA vụ việc | Mặc định 15 ngày làm việc | `tasks/tmp/todo-qtht.md` |
| FR-05.5 Enum lịch sử phân công | Giữ enum chung `PHAN_CONG` | `bug-reports/vu-viec/dev-seed-request-vu-viec.md`, `functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md`, `bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md` |
| FR-05.6 Actor chấp nhận phân công | Người được phân công gồm NHT/TVV/CG hoặc TVV tổ chức cử | `workflow/vu-viec/workflow-test-report-r7-4-a3-vu-viec.md` |
| FR-06.1 Bổ sung lần 4 | `bo_sung_count=3` thì backend chặn yêu cầu bổ sung tiếp; không auto `TU_CHOI` | `functional/chi-tra/functional-test-report-ChiTra-v3.5.md` |
| FR-06.2 SLA 4 mức | warning 70-<85%, urgent 85-<100%, critical >=100% chưa hoàn thành, overdue quá deadline; cần SRS/UC108 ghi chính thức | `functional/chi-tra/functional-test-report-ChiTra-v3.5.md` |
| FR-08.1 Quyền QTHT tiêu chí | QTHT CRUD master criteria; không sửa tiêu chí đã gắn vào từng đợt | `bug-reports/danh-gia/Pass-bug-report-flow-danhgia.md` |
| FR-08.2 Eligible VV | `HOAN_THANH` + trong kỳ + đúng phạm vi đơn vị; không lọc lĩnh vực người đánh giá | `workflow/danh-gia/workflow-test-report-DanhGiaHQ.md`, `workflow/danh-gia/workflow-test-report-r7-4-d2-danhgiahq-bo03-2026-05-09.md` |
| FR-08.3 State sau duyệt PC | `THUC_HIEN`, label "Thực hiện đánh giá" | `workflow/danh-gia/workflow-test-report-DanhGiaHQ.md`, `workflow/danh-gia/workflow-test-report-r7-4-d2-danhgiahq-bo03-2026-05-09.md` |
| FR-08.4 State machine chuẩn | 8 state nghiệp vụ + `HUY`, Section 5 là source of truth | `workflow/danh-gia/workflow-test-report-DanhGiaHQ.md` |
| FR-08.5 KPI VV hoàn thành | Đếm `HOAN_THANH` + `DA_DANH_GIA`, theo `ngay_hoan_thanh` và scope đơn vị | `bug-reports/danh-gia/Pass-bug-report-flow-danhgia.md` |
| FR-08.6 Sửa phân công | Có, khi đợt còn `PHAN_CONG` | `functional/danh-gia/functional-test-report-r7-7-9-danh-gia.md` |
| FR-08.7 Mục tiêu | Bắt buộc ở FE/BE | `functional/danh-gia/functional-test-report-r7-7-9-danh-gia.md` |
| FR-12.1 Cron 2 ngày | QA không chờ thật; Dev cung cấp mock/trigger/test command | `tasks/tmp/todo-tvcs.md`, `functional/tu-van-chuyen-sau/functional-test-report-r7-7-5-tvcs.md` |
| Hợp đồng TV route | Không public/menu; nếu giữ thì route ẩn có guard/redirect, không là luồng nghiệp vụ chính | `tasks/tmp/todo-hop-dong-tv.md`, `functional/hop-dong-tv/functional-test-report-r7-7-14-hdtv.md`, `bug-reports/hop-dong-tv/bug-report-r7-7-14-hdtv.md` |

## Lưu ý

- Không sửa screenshot, JSON evidence, hoặc các đoạn mô tả "observed" lịch sử.
- Các dòng "BA confirm" thuộc module khác ngoài 17 mục Round 7 vẫn giữ nguyên, vì không có trong file phản hồi BA này.
