# BA confirmation needed - UAT tuần 1 - 2026-07-07

## QLCHVMDXL_01 - Expected testcase đang khác SRS về nút Thêm mới / Xóa ở tab Đang xử lý

**Bối cảnh testcase**

- Dòng Excel: 196, mã TC `QLCHVMDXL_01`.
- Nội dung kiểm tra: CB_NV mở tab `Đang xử lý`.
- Expected trong file UAT:
  - Chỉ hiển thị `trang_thai IN (TIEP_NHAN, DA_PHAN_CONG, DANG_XU_LY)`.
  - Không hiển thị `MOI`, `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH`.
  - Không có nút `[Thêm mới]` / `[Xóa]`.
- Actual đối tác ghi: hệ thống hiển thị nút `Xóa`.

**Đối chiếu SRS v3.5**

- SRS không còn trạng thái `DA_PHAN_CONG` trong tab `Đang xử lý`; tab này hard-filter `trang_thai IN ('TIEP_NHAN','DANG_XU_LY')`.
- Nút `+ Thêm mới` hiển thị theo quyền tạo của user, không bị giới hạn theo tab.
- Cột hành động cho phép `Xem / Sửa / Xóa`; `Xóa` chỉ bị cấm khi bản ghi ở `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH`.
- Nút `Xóa hàng loạt` cũng được SRS cho phép ở tab `Tất cả`, `Mới`, `Đang xử lý`, với điều kiện chỉ xóa record chưa ở final state.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1015`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1020`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1044`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1050`

**Kết quả verify UI hiện tại**

- Verify lại ngày 08/07/2026 qua Chrome DevTools MCP, dùng tài khoản UAT `cbnv_tw/CB_NV_TW`.
- Mở URL `http://18.143.165.120/hoi-dap?tab=DANG_XU_LY`.
- UI hiển thị đúng tab `Đang xử lý`.
- Danh sách hiện có bản ghi `HD-20260708-001` ở trạng thái `Tiếp nhận`.
- Toolbar có `Thêm mới`; action dòng có `Xem`, `Sửa`, `Xóa`.
- Với trạng thái `Tiếp nhận`, việc có action `Xóa` là đúng SRS vì bản ghi chưa thuộc `DA_DUYET/CONG_KHAI/HOAN_THANH`.
- Evidence: `screenshots/QLCHVMDXL_01_reverify_2026-07-08_dang-xu-ly-actions.png`

**Kết luận QA**

- `QLCHVMDXL_01` không phải bug theo SRS v3.5.
- Web hiện tại đang làm đúng SRS ở phần hiển thị `Thêm mới` và `Xóa` cho bản ghi chưa final trong tab `Đang xử lý`.
- Expected testcase của đối tác đang sai so với SRS hiện hành ở 2 điểm:
  - đưa `DA_PHAN_CONG` vào danh sách trạng thái;
  - yêu cầu ẩn `Thêm mới` / `Xóa` ở tab `Đang xử lý`.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị cập nhật expected của `QLCHVMDXL_01` theo SRS v3.5:

- Tab `Đang xử lý` chỉ cần hiển thị các bản ghi `TIEP_NHAN` và `DANG_XU_LY`.
- Không yêu cầu ẩn nút `Thêm mới` nếu user có quyền tạo.
- Không yêu cầu ẩn nút `Xóa` với bản ghi `TIEP_NHAN` hoặc `DANG_XU_LY`; chỉ cấm/disable `Xóa` với bản ghi đã final: `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH`.
- Verdict QA đề xuất: `Không phải bug theo SRS`, không gửi Dev xử lý.

## QLTNXLHDVM_06 và QLCHVMDXL_06 - Tab Hoàn thành / danh sách đã xử lý

**Bối cảnh testcase**

- Dòng Excel: 143, mã TC `QLTNXLHDVM_06`.
- Dòng Excel: 201, mã TC `QLCHVMDXL_06`.
- Nội dung kiểm tra: CB_NV mở tab `Hoàn thành` để xem danh sách hỏi đáp đã xử lý / danh sách read-only.
- Expected trong file UAT: danh sách chỉ hiển thị các trạng thái `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH`; read-only; có cột `Người duyệt`, `Ngày duyệt`; cột hành động với bản ghi final/approved chỉ cần `Xem`.

**Kết quả verify UI hiện tại**

- Mở đúng tab `Hoàn thành` trên UI, URL là `tab=HOAN_THANH`.
- Tab `Hoàn thành` hiện đang trống trong dữ liệu kiểm tra.
- Bảng đã có cột `Người duyệt`, `Ngày duyệt`.
- Các trạng thái `Đã duyệt` và `Công khai` đang được hệ thống tách sang 2 tab riêng.
- Action trên các dòng final/approved chỉ có icon `Xem`; phần này đang phù hợp SRS read-only.
- Evidence: `screenshots/audit-QLTNXLHDVM_06-hoan-thanh-tab.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo FR-II-09/10, tab/màn `Hoàn thành` hoặc danh sách đã xử lý phải gom 3 trạng thái:
   - `DA_DUYET`
   - `CONG_KHAI`
   - `HOAN_THANH`

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:765`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:775`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:831`

2. Nhưng phần mô tả thành phần màn hình SCR-II-01 lại tách 3 tab riêng:
   - Tab `Đã duyệt`: `DA_DUYET`
   - Tab `Công khai`: `CONG_KHAI`
   - Tab `Hoàn thành`: `HOAN_THANH`, `HUY`

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1022`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1023`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1024`

**Câu hỏi cần BA xác nhận**

Với màn hình Hỏi đáp pháp lý của CB_NV, tab `Hoàn thành` / danh sách đã xử lý ở 2 testcase `QLTNXLHDVM_06` và `QLCHVMDXL_06` cần được hiểu theo hướng nào?

1. **Gom 3 trạng thái theo FR-II-09/10:** tab `Hoàn thành` phải hiển thị `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH`.
2. **Giữ 3 tab riêng theo SCR-II-01:** `Đã duyệt`, `Công khai`, `Hoàn thành` là 3 tab riêng; tab `Hoàn thành` chỉ hiển thị `HOAN_THANH/HUY`.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho cả `QLTNXLHDVM_06` và `QLCHVMDXL_06`: `Cần BA xác nhận`.
- Nếu BA chọn hướng 1: UI hiện tại là `Vẫn lỗi`, owner dự kiến `Dev FE`.
- Nếu BA chọn hướng 2: phần dữ liệu tab hiện tại có thể không phải lỗi; cần cập nhật lại expected testcase cho khớp SRS. Cột hành động chỉ có `Xem` trên các dòng final/approved đang đúng.
