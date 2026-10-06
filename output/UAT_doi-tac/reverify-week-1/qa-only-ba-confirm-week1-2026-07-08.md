# QA-only Re-verify theo phản hồi BA — UAT tuần 1

**Ngày:** 2026-07-08  
**Nguồn BA:** `output/UAT_doi-tac/reverify-week-1/ba-response-QA-week1-2026-07-08.md`  
**SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md` cập nhật 2026-07-08  
**Môi trường:** `http://18.143.165.120`  
**Tài khoản:** `cbnv_tw` qua OTP MailHog  
**Phương thức:** Chrome DevTools MCP, thao tác UI, report-only, không sửa code.

## Kết quả tổng hợp

| Testcase | Verdict | Ghi chú |
|---|---|---|
| `QLCHVMDXL_01` | Không phải bug theo SRS | Tab Đang xử lý đúng `TIEP_NHAN/DANG_XU_LY`; `+ Thêm mới` và `Xóa` với bản ghi chưa final là đúng quyền/SRS. |
| `QLTNXLHDVM_06` | Pass sau fix | Tab Hoàn thành dùng `HOAN_THANH/HUY`, có cột `Người duyệt`, `Ngày duyệt`; `DA_DUYET` và `CONG_KHAI` nằm ở tab riêng. |
| `QLCHVMDXL_06` | Pass sau fix | Cùng vùng chức năng với `QLTNXLHDVM_06`; cột đã có và SRS mới đã bỏ yêu cầu gom `DA_DUYET/CONG_KHAI` vào Hoàn thành. |
| `PHCHVM_01` | Pass sau fix | Form soạn phản hồi có `Tệp đính kèm phản hồi`, counter `0/20000`, các trường phản hồi đúng SRS. |
| `PHCHVM_06` | Không phải bug theo SRS | 5001 ký tự được chấp nhận; 20001 ký tự bị chặn với `ERR-PH-03`. |

## Chi tiết verify

### `QLCHVMDXL_01`

BA chốt expected cũ sai: tab `Đang xử lý` chỉ gồm `TIEP_NHAN`, `DANG_XU_LY`; `+ Thêm mới` hiển thị theo quyền tạo; `Xóa` chỉ bị cấm với trạng thái final.

Kết quả UI:
- Mở `/hoi-dap?tab=DANG_XU_LY`.
- Tab `Đang xử lý 1` active.
- Bảng có bản ghi `HD-20260708-001`, trạng thái `Tiếp nhận`.
- Toolbar có `+ Thêm mới`.
- Dòng có action `Xem`, `Sửa`, `Xóa`.

Verdict: Không phải bug theo SRS.

Evidence: `screenshots/ba-confirm-2026-07-08/QLCHVMDXL_01-dang-xu-ly.png`

### `QLTNXLHDVM_06` và `QLCHVMDXL_06`

BA chốt SRS mới: tab `Hoàn thành` = `HOAN_THANH`, `HUY`; không gom `DA_DUYET`, `CONG_KHAI`. Hai cột `Người duyệt`, `Ngày duyệt` vẫn bắt buộc.

Kết quả UI/API:
- Mở `/hoi-dap?tab=HOAN_THANH`.
- Tab `Hoàn thành` active, dữ liệu hiện tại trống.
- Header bảng có đủ `Người duyệt`, `Ngày duyệt`.
- API `/api/v1/hoi-daps?page=1&tab=HOAN_THANH` trả `data=[]`, `tabCounts.HOAN_THANH=0`, `tabCounts.HUY=0`.
- Tab `Đã duyệt 8` hiển thị riêng dữ liệu `Đã duyệt`, có cột `Người duyệt`, `Ngày duyệt`, action chỉ `Xem`.
- Tab `Công khai 1` hiển thị riêng dữ liệu `Công khai`, có cột `Người duyệt`, `Ngày duyệt`, action chỉ `Xem`.

Seed data:
- Môi trường không có bản ghi `HOAN_THANH/HUY`.
- Đã thử seed qua endpoint UI `POST /api/v1/hoi-daps/{id}/dong-ho-so` từ record `DA_DUYET`, nhưng user `CB_NV_TW` nhận `403 Forbidden`.
- Do đó không verify trực tiếp được action trên row `HOAN_THANH/HUY`. Phần fix chính theo BA là cột và filter tab đã pass.

Verdict: Pass sau fix, có residual note về thiếu data final để kiểm action row final.

Evidence:
- `screenshots/ba-confirm-2026-07-08/QLTNXLHDVM_06-QLCHVMDXL_06-hoan-thanh-columns-empty.png`
- `screenshots/ba-confirm-2026-07-08/QLTNXLHDVM_06-da-duyet-separate-tab.png`
- `screenshots/ba-confirm-2026-07-08/QLTNXLHDVM_06-cong-khai-separate-tab.png`

### `PHCHVM_01`

Precondition được seed qua UI:
- Mở detail `HD-20260708-001`.
- Từ trạng thái `Tiếp nhận`, phân công cho `CB Nghiệp vụ - Trung ương`.
- Record chuyển sang `Đang xử lý`.

Kết quả UI:
- Form `Soạn phản hồi` xuất hiện.
- Có `Chọn mẫu phản hồi`.
- Có editor `Nội dung phản hồi *` với counter `0/20000 ký tự`.
- Có `Văn bản pháp luật`.
- Có `Gợi ý cho doanh nghiệp`.
- Có `Tệp đính kèm phản hồi`.
- Có hướng dẫn file: tối đa 10 tệp, định dạng doc/docx/xls/xlsx/pdf/jpg/png/gif, 20MB.
- Có `Lưu nháp`, `Gửi phản hồi`.

Verdict: Pass sau fix.

Evidence: `screenshots/ba-confirm-2026-07-08/PHCHVM_01-response-form-attachment-20000.png`

### `PHCHVM_06`

SRS mới: `PHAN_HOI.noi_dung` tối đa 20.000 ký tự; 5001 không lỗi, 20.001 mới lỗi `ERR-PH-03`.

Kết quả UI:
- Nhập 5001 ký tự vào editor, counter hiển thị `5001/20000 ký tự`, không có lỗi giới hạn 5000.
- Nhập 20001 ký tự và bấm `Gửi phản hồi`, UI giữ `20001/20000 ký tự` và hiển thị lỗi `Nội dung phản hồi tối đa 20.000 ký tự (ERR-PH-03)`.
- Không submit phản hồi khi vượt giới hạn.

Verdict: Không phải bug theo SRS.

Evidence:
- `screenshots/ba-confirm-2026-07-08/PHCHVM_06-5001-of-20000-no-error.png`
- `screenshots/ba-confirm-2026-07-08/PHCHVM_06-20001-error-err-ph-03.png`

## Bug còn mở sau round này

Không phát sinh bug mới từ 5 testcase BA confirm. Các issue đang Open ngoài phạm vi BA response giữ nguyên theo bug report hiện tại.

