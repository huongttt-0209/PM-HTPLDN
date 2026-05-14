# Tổng hợp các nội dung cần BA xác nhận - Round 7

**Ngày tổng hợp:** 2026-05-11  
**Nguồn đọc:** `tasks/tmp`, `bug-reports`, `functional`, `workflow` trong round `round7-2026-05-06`.

Report này chỉ liệt kê các nội dung đang cần BA xác nhận. Không đưa các bug đã rõ hướng dev fix, các mục đã BA chốt, hoặc các dòng chỉ là note lịch sử.

## Bảng tổng hợp

| Module/FR | Số mục cần BA xác nhận | Nhóm nội dung chính |
|---|---:|---|
| FR-05 Vụ việc | 6 | Đánh giá trùng, dữ liệu ưu tiên DN, phân công khác đơn vị, SLA, enum lịch sử, actor chấp nhận phân công |
| FR-06 Chi trả | 2 | Lần bổ sung thứ 4, ngưỡng SLA 4 mức |
| FR-08 Đánh giá HTPL | 7 | Quyền QTHT, điều kiện chọn vụ việc, state machine, KPI, edit phân công, field bắt buộc |
| FR-12 TVCS | 1 | Cách nghiệm thu rule cron 2 ngày |
| Hợp đồng TV | 1 | Route standalone Hợp đồng TV |
| **Tổng** | **17** |  |

## FR-05 Vụ việc

### 1. Cách chặn đánh giá trùng cho vụ việc

Hiện tại sau khi CB_NV đánh giá vụ việc lần đầu, vụ việc tự chuyển từ `HOAN_THANH` sang `DA_DANH_GIA`. Nếu đánh giá lần hai, hệ thống chặn bằng trạng thái hiện tại, không đi tới lỗi duplicate theo spec.

**Cần BA xác nhận:** Chấp nhận cách chặn bằng trạng thái hiện tại, hay bắt buộc hệ thống phải trả đúng lỗi duplicate theo spec (`ERR-DG-VV-04`)?

**Nguồn:** `vu-viec/non-dev-followup-vu-viec.md`

### 2. Tạo vụ việc khi hồ sơ doanh nghiệp thiếu dữ liệu ưu tiên

Khi doanh nghiệp thiếu các field dùng để tính ưu tiên, hệ thống vẫn cho tạo vụ việc và tự fallback về mức ưu tiên 3 `Trung bình`. Spec lại đang yêu cầu cảnh báo hoặc lỗi để doanh nghiệp cập nhật hồ sơ trước.

**Cần BA xác nhận:** Có chấp nhận fallback mặc định về ưu tiên 3 không, hay bắt buộc phải cảnh báo/chặn tạo vụ việc cho đến khi doanh nghiệp cập nhật đủ hồ sơ?

**Nguồn:** `vu-viec/bug-report-r7-7-3-functional-vu-viec.md`, `vu-viec/non-dev-followup-vu-viec.md`

### 3. Phân công NHT khác đơn vị với vụ việc

CB_NV_TW có thể phân công một NHT cấp địa phương cho vụ việc cấp trung ương, nhưng khi NHT mở vụ việc thì bị chặn do khác đơn vị. Report đã reclass đây không phải lỗi BE đơn thuần, mà là điểm chưa rõ trong thiết kế phân công.

**Cần BA xác nhận:** FR-05 có cho phép phân công NHT/TVV khác đơn vị với vụ việc không? Nếu có, quyền xem nên theo assignment. Nếu không, màn hình phân công phải chỉ cho chọn người cùng đơn vị/phạm vi hợp lệ.

**Nguồn:** `vu-viec/bug-report-flow-vu-viec.md`

### 4. SLA vụ việc theo NĐ55/2019

Spec BR-SLA-01 đang có nghi vấn về số ngày xử lý: 10 ngày làm việc hay 15 ngày làm việc. Report ghi cần xác nhận lại căn cứ NĐ55/2019 trước khi fix.

**Cần BA xác nhận:** Mốc SLA đúng là 10 ngày làm việc hay 15 ngày làm việc?

**Nguồn:** `vu-viec/bug-report-flow-vu-viec.md`

### 5. Enum lịch sử phân công

Hệ thống đang gom `PHAN_CONG_CA_NHAN` và `PHAN_CONG_TO_CHUC` thành enum chung `PHAN_CONG`.

**Cần BA xác nhận:** Có giữ enum chung `PHAN_CONG` không, hay phải tách riêng lịch sử phân công cá nhân và phân công tổ chức như test/spec đang kỳ vọng?

**Nguồn:** `vu-viec/dev-seed-request-vu-viec.md`

### 6. Actor chấp nhận phân công ở bước B3

Workflow có ghi nhận điểm chưa rõ: CG không có UI để chấp nhận phân công trên chi tiết vụ việc. Trong khi đó, một phần spec lại mô tả CG đi qua TVCS, không phải qua FR-05.

**Cần BA xác nhận:** Bước chấp nhận phân công trong FR-05 chỉ dành cho NHT, hay cả TVV/CG cũng phải chấp nhận phân công trực tiếp trong module Vụ việc?

**Nguồn:** `workflow/vu-viec/workflow-test-report-r7-4-a3-vu-viec.md`

## FR-06 Chi trả

### 1. Lần yêu cầu bổ sung thứ 4

Test case CT-006 chưa chạy được vì spec chưa nói rõ khi hồ sơ đã bị yêu cầu bổ sung 3 lần thì lần thứ 4 phải xử lý thế nào.

**Cần BA xác nhận:** Khi `bo_sung_count = 3`, hệ thống nên: không cho yêu cầu bổ sung tiếp, cho backend chặn, hay tự động chuyển hồ sơ sang `TU_CHOI`?

**Nguồn:** `functional/chi-tra/functional-test-report-ChiTra-v3.5.md`

### 2. Ngưỡng SLA 4 mức cảnh báo

Test case CT-021 cần kiểm tra SLA 4 mức cảnh báo, nhưng tài liệu chưa nêu rõ ngưỡng cho từng mức.

**Cần BA xác nhận:** Ngưỡng cụ thể cho 4 mức SLA là gì: warning, urgent, critical, overdue?

**Nguồn:** `functional/chi-tra/functional-test-report-ChiTra-v3.5.md`

## FR-08 Đánh giá HTPL

### 1. Quyền QTHT trên tiêu chí của từng đợt đánh giá

QTHT không còn thao tác ở tab Phân công, nhưng vẫn có thể chỉnh trọng số, điểm tối đa và xóa dòng trong tab Tiêu chí của một đợt đánh giá. Matrix ghi QTHT có CRUD với `TIEU_CHI_DANH_GIA`, nhưng chưa rõ đây là danh mục tiêu chí dùng chung hay tiêu chí riêng của từng đợt.

**Cần BA xác nhận:** QTHT được CRUD tiêu chí ở cấp danh mục dùng chung thôi, hay được sửa cả tiêu chí đã gắn riêng vào từng đợt đánh giá?

**Nguồn:** `danh-gia/Pass-bug-report-flow-danhgia.md`

### 2. Điều kiện chọn vụ việc vào đợt đánh giá

API lấy danh sách vụ việc eligible trả rỗng dù có vụ việc `HOAN_THANH` trong khoảng thời gian. Spec FR-VI-05 chưa mô tả rõ logic lọc.

**Cần BA xác nhận:** Khi chọn vụ việc vào đợt đánh giá, hệ thống cần lọc theo những điều kiện nào: chỉ theo thời gian, theo lĩnh vực người đánh giá, theo đơn vị/phạm vi dữ liệu, hay kết hợp các điều kiện này?

**Nguồn:** `danh-gia/Pass-bug-report-flow-danhgia.md`

### 3. Tên trạng thái sau khi phê duyệt phân công

Sau khi CB_PD đã phê duyệt phân công, app vẫn hiển thị `CHO_DUYET_PC`. Tên này dễ hiểu là “đang chờ duyệt phân công”, nhưng thực tế đã duyệt xong.

**Cần BA xác nhận:** State sau khi phê duyệt phân công nên là trạng thái nào và label tiếng Việt chính thức là gì?

**Nguồn:** `danh-gia/Pass-bug-report-flow-danhgia.md`, `workflow/danh-gia/workflow-test-report-DanhGiaHQ.md`

### 4. Chuẩn state machine của module Đánh giá

Report workflow ghi nhận SRS có nhiều phiên bản state machine khác nhau: bản 6 state, bản 7 state và UI filter 9 trạng thái.

**Cần BA xác nhận:** Phiên bản state machine nào là chuẩn chính thức để Dev và QA cùng bám theo?

**Nguồn:** `workflow/danh-gia/workflow-test-report-DanhGiaHQ.md`

### 5. KPI “Vụ việc hoàn thành” trên Dashboard/Đánh giá

Có note cần xác nhận rule filter cho KPI `Vụ việc hoàn thành`, đặc biệt khi có các trạng thái cuối như `HOAN_THANH` và `DA_DANH_GIA`.

**Cần BA xác nhận:** KPI “Vụ việc hoàn thành” phải đếm những trạng thái nào và theo filter thời gian/đơn vị nào?

**Nguồn:** `danh-gia/Pass-bug-report-flow-danhgia.md`

### 6. Có cần chức năng sửa phân công không?

Test plan có case sửa vai trò/lĩnh vực phân công, nhưng SRS FR-VI-03 chỉ mô tả thêm và xóa người đánh giá, không mô tả sửa.

**Cần BA xác nhận:** Có cần chức năng sửa phân công không? Nếu có, cần bổ sung vào SRS; nếu không, QA sẽ coi delete + add lại là workaround đúng.

**Nguồn:** `functional/danh-gia/functional-test-report-r7-7-9-danh-gia.md`

### 7. Field “Mục tiêu” có bắt buộc không?

SRS ghi field `Mục tiêu` là bắt buộc, nhưng UI không đánh dấu bắt buộc và submit form trống không báo lỗi cho field này.

**Cần BA xác nhận:** `Mục tiêu` vẫn là field bắt buộc hay đã chuyển thành optional?

**Nguồn:** `functional/danh-gia/functional-test-report-r7-7-9-danh-gia.md`

## FR-12 TVCS

### 1. Cách kiểm thử rule cron 2 ngày

Test case TV-011 kiểm tra việc tự động reset `PHAN_CONG -> TIEP_NHAN` sau 2 ngày làm việc. QA không trigger được trong phiên test ngắn.

**Cần BA xác nhận:** Rule này cần được nghiệm thu bằng cách chờ đủ 2 ngày E2E thật, hay cần Dev cung cấp mock/trigger endpoint để QA kiểm thử?

**Nguồn:** `functional/tu-van-chuyen-sau/functional-test-report-r7-7-5-tvcs.md`

## Hợp đồng TV

### 1. Route standalone `/hop-dong-tv/danh-sach`

Spec v3.5 nói Hợp đồng TV không có menu riêng, chỉ truy cập qua tab trong chi tiết Vụ việc/TVV. Tuy nhiên route trực tiếp `/hop-dong-tv/danh-sach` vẫn render danh sách.

**Cần BA xác nhận:** Xóa hoàn toàn route standalone này, hay giữ route ẩn cho admin/QTHT?

**Nguồn:** `hop-dong-tv/bug-report-r7-7-14-hdtv.md`, `functional/hop-dong-tv/functional-test-report-r7-7-14-hdtv.md`
