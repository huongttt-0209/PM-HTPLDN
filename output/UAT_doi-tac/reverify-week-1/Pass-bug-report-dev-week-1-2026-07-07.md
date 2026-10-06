# Bug Report — UAT PM HTPLDN Tuần 1 Re-verify

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | `http://18.143.165.120/login` |
| **Người test** | QA Automation qua Chrome DevTools MCP |
| **Ngày** | 2026-07-07 15:57:19 |
| **Loại test** | UAT Re-verify / Regression |
| **Round** | UAT tuần 1 - sau dev fix lần 1 |
| **Tài liệu tham chiếu** | `output/UAT_doi-tac/UAT-PM HTPLDN - Tuần 1.xlsx`; `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5`; `output/UAT_doi-tac/reverify-week-1/reverify-report-week-1-2026-07-07.md` |

---

## Tổng hợp

Phát hiện **0** lỗi còn Open đủ căn cứ gửi Dev trong quá trình re-verify UAT tuần 1. Các case `DB_06`, `DB_07`, `TKDGHQHTPL_02`, `TKHDVMPLDTNXL_04`, `TKHDVMTH_11`, `QLCKPHCHVM_01` đã được re-check hoặc được đối tác xác nhận pass nên chuyển sang Closed. Nhóm case BA-confirm ngày 2026-07-08 (`QLCHVMDXL_01`, `QLTNXLHDVM_06`, `QLCHVMDXL_06`, `PHCHVM_01`, `PHCHVM_06`) đã được re-verify lại theo SRS/BA mới và không còn là bug Open cần gửi Dev trong file này; riêng tab `Hoàn thành` đã seed đủ `HOAN_THANH` (`HD-20260707-005`) và `HUY` (`HD-20260708-002`) để xác nhận UI view đúng cả 2 trạng thái BA chốt.

> **Rule log bug (feedback 2026-04-23):** Bug chỉ log khi có SRS reference cụ thể (`FR-X`, `BR-X`, `SCR-X row Y`, `§Error Handling EN`, `Inputs row N`). Quan sát không map được clause SRS -> KHÔNG log vào file bug.

> **Rule hiển thị trạng thái (áp dụng cho các lần verify sau):** Bug `Open` luôn đặt phía trên để Dev theo dõi. Bug `Closed` chuyển xuống cuối bảng/chi tiết, gạch ngang nội dung ở summary và tiêu đề chi tiết; chữ <span style="color:#16a34a;font-weight:700">Closed</span> dùng màu xanh để phân biệt rõ bug đã pass.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 6    | 0        | 3     | 3      | 0     | 0       | 6      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-UAT-W1-TKDGHQHTPL_02-003~~ | ~~Medium~~ | ~~P2~~ | ~~UI/UX~~ | ~~TKDGHQHTPL_02~~ | ~~`srs-fr-01-dashboard.md:415`, `srs-fr-01-dashboard.md:419`, `srs-fr-01-dashboard.md:443`~~ | ~~Biểu đồ hiệu quả HTPLDN đã tách thành 2 biểu đồ cột song song theo SRS~~ | <span style="color:#16a34a;font-weight:700">Closed</span> |
| ~~BUG-UAT-W1-QLCKPHCHVM_01-005~~ | ~~Major~~ | ~~P1~~ | ~~Workflow~~ | ~~QLCKPHCHVM_01~~ | ~~`srs-fr-02-hoi-dap.md:1115`, `srs-fr-02-hoi-dap.md:1174`~~ | ~~Notification sau phê duyệt đã gửi đúng CB NV soạn phản hồi sau re-check~~ | <span style="color:#16a34a;font-weight:700">Closed</span> |
| ~~BUG-UAT-W1-DB_06-001~~ | ~~Major~~ | ~~P1~~ | ~~Workflow~~ | ~~DB_06~~ | ~~`srs-fr-01-dashboard.md:186`, `srs-fr-01-dashboard.md:194`, `srs-fr-01-dashboard.md:292`, `srs-fr-01-dashboard.md:294`~~ | ~~Dashboard KPI-03 drill-down năm 2025 đã khớp SRS sau re-check~~ | <span style="color:#16a34a;font-weight:700">Closed</span> |
| ~~BUG-UAT-W1-DB_07-002~~ | ~~Major~~ | ~~P1~~ | ~~Workflow~~ | ~~DB_07~~ | ~~`srs-fr-01-dashboard.md:186`, `srs-fr-01-dashboard.md:194`, `srs-fr-01-dashboard.md:342`, `srs-fr-01-dashboard.md:344`~~ | ~~Dashboard KPI-05 drill-down tháng 5/2026 đã khớp SRS sau re-check~~ | <span style="color:#16a34a;font-weight:700">Closed</span> |
| ~~BUG-UAT-W1-TKHDVMTH_11-008~~ | ~~Medium~~ | ~~P2~~ | ~~Validation/UI Text~~ | ~~TKHDVMTH_11~~ | ~~`srs-fr-02-hoi-dap.md:265`, `srs-fr-02-hoi-dap.md:1030`~~ | ~~Message validate Từ ngày > Đến ngày được đối tác xác nhận pass~~ | <span style="color:#16a34a;font-weight:700">Closed</span> |
| ~~BUG-UAT-W1-TKHDVMPLDTNXL_04-007~~ | ~~Medium~~ | ~~P2~~ | ~~UI/UX~~ | ~~TKHDVMPLDTNXL_04~~ | ~~`srs-fr-02-hoi-dap.md:1046`~~ | ~~Empty state khi tìm kiếm không có kết quả chỉ hiện `Trống`, thiếu message/action theo SRS~~ | <span style="color:#16a34a;font-weight:700">Closed</span> |

---

## ~~BUG-UAT-W1-TKDGHQHTPL_02-003 — Biểu đồ hiệu quả HTPLDN đã tách thành 2 biểu đồ cột song song theo SRS~~ <span style="color:#16a34a;font-weight:700">Closed</span>

### Trạng thái cập nhật

<span style="color:#16a34a;font-weight:700">Closed</span> ngày 2026-07-09 sau khi re-verify bằng Chrome DevTools MCP. Không gửi Dev xử lý tiếp cho `TKDGHQHTPL_02`.

### Mô tả

Bug cũ: Dashboard hiển thị một biểu đồ kết hợp với 2 legend/thang đo (`Tỷ lệ tuân thủ (%)`, `Điểm hài lòng (1-5)`). SRS yêu cầu 2 biểu đồ cột song song, mỗi biểu đồ một chỉ số đơn.

### Các bước tái hiện

1. Đăng nhập role `CB_NV_TW`.
2. Vào Dashboard năm 2026.
3. Quan sát khu vực biểu đồ hiệu quả hỗ trợ pháp lý.

### Kết quả mong đợi

- Theo `srs-fr-01-dashboard.md:415`, `srs-fr-01-dashboard.md:419`, `srs-fr-01-dashboard.md:443`, khu vực hiệu quả phải hiển thị 2 biểu đồ cột song song cho 2 chỉ số riêng.

### Kết quả thực tế

- UI hiện tại đã tách thành 2 card chart độc lập:
  - `Điểm đánh giá hiệu quả hỗ trợ pháp lý`: `76.7/100`, cỡ mẫu `Dựa trên 3 đánh giá`, chart riêng theo thang 0-100.
  - `Tỷ lệ tuân thủ thời hạn xử lý`: `50.0%`, cỡ mẫu `Tính trên 4 vụ việc`, chart riêng theo thang %.
- DOM check không còn legend/nội dung cũ `Điểm hài lòng` hoặc thang `1-5`.

### Bằng chứng

**1. Ảnh chụp**:

![BUG-UAT-W1-TKDGHQHTPL_02-003 — UC8 đã tách thành 2 biểu đồ cột song song](screenshots/round3-2026-07-09/TKDGHQHTPL_02-dashboard-uc8-two-charts.png)

### Ghi chú owner

Không cần Dev FE xử lý tiếp. Ảnh cũ `image/bug-uat-w1-003-bieu-do-hieu-qua.png` chỉ còn là evidence lịch sử trước khi fix.

---

## ~~BUG-UAT-W1-QLCKPHCHVM_01-005 — Notification sau phê duyệt đã gửi đúng CB NV soạn phản hồi sau re-check~~ <span style="color:#16a34a;font-weight:700">Closed</span>

### Trạng thái cập nhật

<span style="color:#16a34a;font-weight:700">Closed</span> ngày 2026-07-08 sau khi re-check đúng luồng bằng Chrome DevTools MCP. Không gửi Dev xử lý tiếp cho `QLCKPHCHVM_01`.

### Mô tả re-check

Re-check bằng bản ghi `HD-20260707-005` để tránh kết luận theo dữ liệu cũ `FFF-HD-003`.

Luồng đúng:

1. `cbnv_tw/CB_NV_TW` tiếp nhận, phân công, soạn phản hồi và gửi phê duyệt `HD-20260707-005`.
2. Audit log ghi `SUBMIT` bởi `CB Nghiệp vụ - Trung ương` lúc `2026-07-08T02:27:57.835Z`.
3. `cbpd_tw/CB_PD_TW` phê duyệt cùng bản ghi.
4. Audit log ghi `APPROVE` bởi `CB Phê duyệt - Trung ương` lúc `2026-07-08T02:30:42.010Z`.
5. Đăng nhập lại `cbnv_tw` và kiểm tra `/api/v1/thong-baos`.

### Kết quả mong đợi theo SRS

- Theo `srs-fr-02-hoi-dap.md:1115`, khi phê duyệt phải gửi thông báo trong hệ thống tới cán bộ nghiệp vụ.
- Theo `srs-fr-02-hoi-dap.md:1174`, event approve gửi `In-app` tới `CB NV soạn phản hồi`.

### Kết quả thực tế sau re-check

- Notification in-app tồn tại cho đúng người nhận `nguoiNhanId=f2e93500-f6dd-4660-a3f6-de7326acffd1`, chính là `cbnv_tw/CB_NV_TW`.
- Notification có tiêu đề `Phản hồi đã được phê duyệt`.
- Nội dung: `Hỏi đáp HD-20260707-005 đã được phê duyệt`.
- `entityType=HOI_DAP`, `entityId=763b9af9-1e48-401d-b5f5-35375a0f7b9d`.
- `ngayTao=2026-07-08T02:30:42.049Z`, ngay sau thời điểm `CB_PD_TW` approve.
- MailHog cũng có email tới `cbnv_tw@htpldn.test`, nhưng email chỉ là quan sát thêm; tiêu chí pass bắt buộc theo SRS là in-app notification.

### Bằng chứng

**1. Ảnh chụp**:

![BUG-UAT-W1-QLCKPHCHVM_01-005 — CB_NV_TW gửi phản hồi chờ phê duyệt](screenshots/round2-2026-07-08/QLCKPHCHVM_01_seed_sent_waiting_approval.png)
![BUG-UAT-W1-QLCKPHCHVM_01-005 — CB_PD_TW phê duyệt HD-20260707-005](screenshots/round2-2026-07-08/QLCKPHCHVM_01_cbpd_approved_HD-20260707-005.png)
![BUG-UAT-W1-QLCKPHCHVM_01-005 — CB_NV_TW nhận notification sau approve](screenshots/round2-2026-07-08/QLCKPHCHVM_01_cbnv_notification_popover_after_approve.png)

### Ghi chú QA

Kết luận Open cũ dựa trên bản ghi `FFF-HD-003`. Re-check mới với `HD-20260707-005` xác nhận notification đã gửi đúng tài khoản `cbnv_tw`, là CB NV soạn phản hồi. Bug được đóng.

---

## ~~BUG-UAT-W1-DB_06-001 — Dashboard KPI-03 drill-down năm 2025 đã khớp SRS sau re-check~~ <span style="color:#16a34a;font-weight:700">Closed</span>

### Trạng thái cập nhật

<span style="color:#16a34a;font-weight:700">Closed</span> ngày 2026-07-08 sau khi re-check SRS và thao tác lại qua Chrome DevTools MCP. Không gửi Dev xử lý tiếp cho DB_06.

### Mô tả lịch sử

Với role `CB_NV_TW`, Dashboard chọn năm 2025 và click card `Vụ việc đang xử lý`. Re-check lại SRS ngày 2026-07-08 xác định card này là KPI-03, thuộc nhóm KPI ảnh chụp/trạng thái sống, không phải KPI phát sinh theo `ngay_tiep_nhan` trong năm.

### Các bước re-check

1. Đăng nhập role `CB_NV_TW`.
2. Vào Dashboard, chọn `Năm = 2025`, `Tháng = Cả năm`, bấm `Áp dụng`.
3. Click card `Vụ việc đang xử lý`.
4. Quan sát count và trạng thái các dòng trong danh sách đích.

### Kết quả mong đợi theo SRS

- Theo `srs-fr-01-dashboard.md:186` và `srs-fr-01-dashboard.md:194`, KPI-03/05/07 là KPI ảnh chụp tại cuối kỳ, **không dùng khoảng thời gian**.
- Theo `srs-fr-01-dashboard.md:292` và `srs-fr-01-dashboard.md:294`, KPI-03 đếm/drill-down theo 5 trạng thái sống: `DA_TIEP_NHAN`, `DANG_KIEM_TRA`, `YEU_CAU_BO_SUNG`, `DA_PHAN_CONG`, `DANG_XU_LY`.

### Kết quả thực tế sau re-check

- Dashboard `Năm = 2025`, card `Vụ việc đang xử lý` hiển thị `2 vụ việc`.
- Click card mở `/vu-viec/danh-sach?trangThai=DA_TIEP_NHAN,DANG_KIEM_TRA,YEU_CAU_BO_SUNG,DA_PHAN_CONG,DANG_XU_LY&denNgay=2025-12-31`.
- Bảng hiển thị `1-2 / 2`, gồm `DDD-VV-001`, `DDD-VV-002`; cả 2 trạng thái `Đang xử lý`.
- Ngày tiếp nhận 2024 không phải tiêu chí fail cho KPI-03 theo SRS, vì card này không lọc bản ghi theo khoảng ngày tiếp nhận.

### Bằng chứng

**1. Ảnh chụp**:

![BUG-UAT-W1-DB_06-001 — Dashboard năm 2025 sau re-check](screenshots/round2-2026-07-08/DB_06-recheck-2026-07-08-dashboard-2025.png)
![BUG-UAT-W1-DB_06-001 — List vụ việc đang xử lý sau re-check](screenshots/round2-2026-07-08/DB_06-recheck-2026-07-08-list.png)

### Ghi chú QA

Kết luận Open trước đó là do áp nhầm tiêu chí ngày của KPI phát sinh trong kỳ cho KPI-03 ảnh chụp trạng thái.

---

## ~~BUG-UAT-W1-DB_07-002 — Dashboard KPI-05 drill-down tháng 5/2026 đã khớp SRS sau re-check~~ <span style="color:#16a34a;font-weight:700">Closed</span>

### Trạng thái cập nhật

<span style="color:#16a34a;font-weight:700">Closed</span> ngày 2026-07-08 sau khi re-check SRS và thao tác lại qua Chrome DevTools MCP. Không gửi Dev xử lý tiếp cho DB_07.

### Mô tả lịch sử

Sau khi filter tháng trên Dashboard, click card `Đào tạo đang diễn ra`. Re-check lại SRS ngày 2026-07-08 xác định card này là KPI-05, thuộc nhóm KPI ảnh chụp/trạng thái, đếm khóa học đang ở trạng thái `DANG_DIEN_RA`; không phải KPI khóa học có `ngay_bat_dau` nằm trong tháng.

### Các bước re-check

1. Đăng nhập role `CB_NV_TW`.
2. Vào Dashboard, chọn `Năm = 2026`, `Tháng = Tháng 5`, bấm `Áp dụng`.
3. Click card `Đào tạo đang diễn ra`.
4. Quan sát count và trạng thái các khóa học trong danh sách đích.

### Kết quả mong đợi theo SRS

- Theo `srs-fr-01-dashboard.md:186` và `srs-fr-01-dashboard.md:194`, KPI-03/05/07 là KPI ảnh chụp tại cuối kỳ, **không dùng khoảng thời gian**.
- Theo `srs-fr-01-dashboard.md:342` và `srs-fr-01-dashboard.md:344`, KPI-05 đếm/drill-down khóa học ở trạng thái `DANG_DIEN_RA`.

### Kết quả thực tế sau re-check

- Dashboard `Năm = 2026`, `Tháng = Tháng 5`, card `Đào tạo đang diễn ra` hiển thị `2 khóa học`.
- Click card mở `/dao-tao/khoa-hoc/danh-sach?tab=DANG_DIEN_RA&dateField=ngay_bat_dau&denNgay=2026-05-31`.
- Bảng hiển thị `1-2 / 2`, gồm `DDD-KH-011`, `DDD-KH-012`; cả 2 trạng thái `Đang diễn ra`.
- Ngày bắt đầu ngoài tháng 05/2026 không phải tiêu chí fail cho KPI-05 theo SRS, vì card này kiểm trạng thái đang diễn ra, không lọc khóa học theo `ngay_bat_dau` trong tháng.

### Bằng chứng

**1. Ảnh chụp**:

![BUG-UAT-W1-DB_07-002 — Dashboard tháng 5/2026 sau re-check](screenshots/round2-2026-07-08/DB_07-recheck-2026-07-08-dashboard-thang-5.png)
![BUG-UAT-W1-DB_07-002 — List đào tạo đang diễn ra sau re-check](screenshots/round2-2026-07-08/DB_07-recheck-2026-07-08-list.png)

### Ghi chú QA

Route hiện có thêm `dateField/denNgay`; chưa thấy gây sai dữ liệu theo SRS vì tiêu chí kiểm chính là trạng thái `Đang diễn ra` và list count khớp card.

---

## ~~BUG-UAT-W1-TKHDVMTH_11-008 — Message validate Từ ngày > Đến ngày được đối tác xác nhận pass~~ <span style="color:#16a34a;font-weight:700">Closed</span>

### Trạng thái cập nhật

<span style="color:#16a34a;font-weight:700">Closed</span> ngày 2026-07-08 theo phản hồi đối tác: case `TKHDVMTH_11` đã pass. Không gửi Dev xử lý tiếp cho case này.

### Mô tả lịch sử

Case `TKHDVMTH_11` kiểm tra nhập `Từ ngày` lớn hơn `Đến ngày` tại màn `Hỏi đáp pháp lý`. UI đã chặn tìm kiếm sai dữ liệu khi `Từ ngày > Đến ngày`; nội dung message inline là `Từ ngày phải trước Đến ngày`. Dù khác literal SRS `Ngày bắt đầu phải trước ngày kết thúc`, đối tác đã xác nhận pass nên verdict chính thức là Closed.

### Các bước tái hiện

1. Đăng nhập role `CB_NV_TW`.
2. Vào `Hỏi đáp pháp lý`.
3. Nhập `Từ ngày` lớn hơn `Đến ngày`, ví dụ `25/06/2026` và `24/06/2026`.
4. Quan sát validate tại bộ lọc ngày và trạng thái nút `Tìm kiếm`.

### Kết quả mong đợi

- Theo `srs-fr-02-hoi-dap.md:1030`, DatePicker `Từ/Đến ngày` phải validate `tu_ngay <= den_ngay`.
- Theo `srs-fr-02-hoi-dap.md:265`, khi `tu_ngay > den_ngay`, hệ thống hiển thị lỗi và không thực hiện tìm kiếm sai dữ liệu.

### Kết quả thực tế sau xác nhận

- UI chặn tìm kiếm khi `Từ ngày > Đến ngày`.
- Nút `Tìm kiếm` disabled, không submit query sai.
- Đối tác xác nhận pass ngày 2026-07-08, nên không cần Dev xử lý tiếp.

### Bằng chứng

**1. Ảnh chụp**:

![BUG-UAT-W1-TKHDVMTH_11-008 — Validate khoảng ngày](screenshots/TKHDVMTH_11_reaudit_invalid_date_range.png)

### Ghi chú owner

Không cần dev xử lý tiếp theo phản hồi đối tác ngày 2026-07-08. Nội dung bên trên được giữ làm lịch sử trước khi đóng.

---

## ~~BUG-UAT-W1-TKHDVMPLDTNXL_04-007 — Empty state khi tìm kiếm không có kết quả chỉ hiện `Trống`, thiếu message/action theo SRS~~ <span style="color:#16a34a;font-weight:700">Closed</span>

### Trạng thái cập nhật

<span style="color:#16a34a;font-weight:700">Closed</span> ngày 2026-07-08 theo xác nhận đối tác: case `TKHDVMPLDTNXL_04` đã pass. Bug này không còn cần gửi Dev xử lý.

### Mô tả lịch sử

Với role `CB_NV_TW`, khi tìm kiếm từ khóa không tồn tại `xyz999`, filter chạy đúng và bảng không còn dữ liệu. Tuy nhiên empty state chỉ hiển thị text mặc định `Trống`, không hiển thị thông điệp context-aware và action reset theo SRS.

### Các bước tái hiện

1. Đăng nhập role `CB_NV_TW`.
2. Vào `Hỏi đáp pháp lý`.
3. Ở tab `Tất cả`, nhập từ khóa `xyz999`.
4. Bấm `Tìm kiếm`.

### Kết quả mong đợi

Theo `srs-fr-02-hoi-dap.md:1046`, với trường hợp tìm kiếm/bộ lọc không khớp, empty state phải hiển thị `Không tìm thấy hỏi đáp phù hợp với bộ lọc` và có action `[Xóa bộ lọc]`.

### Kết quả thực tế lịch sử

- URL đổi đúng thành `/hoi-dap?keyword=xyz999&page=1`.
- Ô keyword giữ giá trị `xyz999`, bảng không có row dữ liệu.
- Empty state chỉ hiển thị `Trống`.
- Không có message `Không tìm thấy hỏi đáp phù hợp với bộ lọc` và không có action reset ngay trong empty state.

### Bằng chứng

**1. Ảnh chụp**:

![BUG-UAT-W1-TKHDVMPLDTNXL_04-007 — Empty state filter không có kết quả](screenshots/audit-TKHDVMPLDTNXL_04-keyword-empty.png)

### Ghi chú owner

Không cần dev xử lý tiếp theo phản hồi đối tác ngày 2026-07-08. Nội dung bên trên được giữ làm lịch sử bug trước khi đóng.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | `http://18.143.165.120/login` |
| OTP login | OTP lấy từ MailHog theo từng lần đăng nhập |
| MailHog (OTP inbox) | `http://18.143.165.120:8025/` |
| API base | Không dùng API để verify; thao tác manual qua UI |
| Frontend | Web app staging |
| Xác thực | Login + OTP MailHog |
| Tool test | Chrome DevTools MCP / manual UI |

---

*Bug report generated: 2026-07-07 15:57:19 | QA Automation via Chrome DevTools MCP*
