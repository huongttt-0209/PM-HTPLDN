# Re-verify lần 2 — 2 bug Reopen UAT tuần 3

- Ngày kiểm tra: 24/07/2026
- Tab: `UAT_TGPL Doanh Nghiệp-tuần 3`
- Phạm vi: `TKDNHTPL_02`, `CTTLV_01`
- Cách kiểm tra: Chrome mới, context cô lập; bám đúng `CÁCH VERIFY` và PASS/FAIL trong cột `DEV phản hồi lần 1`
- Kết quả: **2 Pass, 0 Reopen**

## Tổng quan

| Module / task | Bug Open | Bug Closed | Bug re-verify | TC/path unblock | TC/path vẫn block | Next action |
|---|---:|---:|---:|---|---|---|
| Doanh nghiệp — bộ lọc lĩnh vực | 0 | 1 | 1 | Nhãn, `Tất cả`, chọn nhiều và cấu trúc bộ lọc | Không | Regression thêm thao tác chọn/xóa 3 giá trị |
| Chương trình HTPLDN / báo cáo lĩnh vực | 0 | 1 | 1 | Tạo chương trình theo lĩnh vực và báo cáo phân nhóm | Không | Regression form sửa và số DN tham gia |

## 1. Bug Re-verify

| Mã bug | Dòng sheet | Kết quả | Quan sát theo guide | Cập nhật sheet | Bằng chứng |
|---|---:|---|---|---|---|
| `TKDNHTPL_02` | 41 | Closed-verified / Pass | Có đúng nhãn `Lĩnh vực KD`; dropdown có `Tất cả`; chọn đồng thời 2 giá trị; không có bộ lọc `Ngành nghề` riêng | Chỉ đổi `Q41: Reopen → Pass`; `P41` và `R41` giữ nguyên | [Nhãn chính xác](image/TKDNHTPL_02-pass-exact-label.png), [Tất cả và multi-select](image/TKDNHTPL_02-pass-label-all-multiselect.png) |
| `CTTLV_01` | 270 | Closed-verified / Pass | Form dùng đúng tên `Lĩnh vực pháp lý`; bắt buộc; chọn đơn từ danh mục dùng chung. Báo cáo năm tách đúng Lao động = 1, Thương mại = 1, mỗi nhóm DN tham gia = 0; 3 bản ghi cũ vẫn ở `Chưa phân loại` theo lưu ý BA | Chỉ đổi `Q270: Reopen → Pass`; `P270` và `R270` giữ nguyên | [Nhãn trường bắt buộc](image/CTTLV_01-pass-form-linh-vuc-phap-ly.png), [Chọn đơn](image/CTTLV_01-pass-single-select.png), [Báo cáo 2 lĩnh vực](image/CTTLV_01-pass-report-2-linh-vuc.png) |

## 2. Bug Summary

| Trạng thái | Số lượng | Bug |
|---|---:|---|
| Closed-verified / Pass | 2 | `TKDNHTPL_02`, `CTTLV_01` |
| Open / Reopen | 0 | Không có |
| Blocked / chưa chạy | 0 | Không có |

## 3. TC/Path affected

| TC/path | Trạng thái sau re-verify | Ảnh hưởng |
|---|---|---|
| Danh sách doanh nghiệp — bộ lọc lĩnh vực | Unblocked | Có thể lọc nhiều lĩnh vực bằng đúng control `Lĩnh vực KD` |
| Tạo chương trình — trường lĩnh vực pháp lý | Unblocked | Nhãn, bắt buộc, chọn đơn và danh mục đều đạt |
| Báo cáo chương trình theo lĩnh vực | Unblocked | Chương trình được đếm đúng theo Lao động/Thương mại; dữ liệu null cũ tách riêng |
| Sửa chương trình ở trạng thái Dự thảo | Có thể regression tiếp | Không có bản ghi Dự thảo sẵn trong lượt này; route sửa bản ghi Đã duyệt tự quay về danh sách đúng quyền trạng thái |

## 4. Testability Sweep

| Nhóm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Happy path | Đạt | Bộ lọc lĩnh vực và báo cáo chương trình theo lĩnh vực |
| Validation | Đạt | Bỏ trống lĩnh vực khi lưu phát sinh `Vui lòng chọn lĩnh vực pháp lý` |
| Multi-select / single-select | Đạt | Lọc DN giữ đồng thời 2 giá trị; form chương trình thay Lao động bằng Thương mại, không giữ cả hai |
| Shared catalogue | Đạt | Dropdown có Thuế, Lao động, Đất đai, Dân sự, Thương mại và các mục danh mục chung khác |
| Legacy/null data | Đạt theo lưu ý BA | 3 chương trình `Chưa phân loại` không tính FAIL |
| Role/scope | Đạt | Kiểm tra bằng tài khoản nghiệp vụ Trung ương |
| Regression ngoài phạm vi | Chưa chạy | Không mở rộng sang bug khác |

## 5. Setup

| Hạng mục | Trạng thái | Chi tiết |
|---|---|---|
| Trình duyệt | Sẵn sàng | Chrome context mới, cô lập với phiên trước |
| Tài khoản | Sẵn sàng | Dùng đúng tài khoản kiểm thử nghiệp vụ Trung ương |
| Dữ liệu báo cáo | Sẵn có | `CT-20260724-0001` thuộc Lao động và `CT-20260721-0001` thuộc Thương mại |
| Công cụ | Sẵn sàng | Chrome DevTools; không dùng `curl` để kết luận |
| Sheet write-back | Hoàn tất | Đã ghi bằng `tools/sheet_verify_write.py` và đọc lại: Q41/Q270 đều `Pass` |

## 6. Spec/BA Confirmation

| Nội dung | Kết luận áp dụng |
|---|---|
| Bộ lọc lĩnh vực DN | Phải có nhãn `Lĩnh vực KD`, có `Tất cả`, chọn nhiều và không có bộ lọc Ngành nghề riêng |
| Trường lĩnh vực chương trình | Phải có tên `Lĩnh vực pháp lý`, bắt buộc, chọn một và lấy từ danh mục dùng chung |
| Báo cáo theo lĩnh vực | Hiển thị tên lĩnh vực, số chương trình và số DN tham gia; chương trình đã gán không nằm trong nhóm chưa phân loại |
| Chương trình cũ chưa có lĩnh vực | Có thể ở `Chưa phân loại`; không tính FAIL nếu không có yêu cầu migrate |
| Quy tắc ghi sheet khi Pass | Chỉ thay cột Verify; không sửa trạng thái Dev hoặc nội dung phản hồi cũ |

## 7. Next actions

| Ưu tiên | Owner | Việc cần làm | Điều kiện hoàn tất |
|---:|---|---|---|
| 1 | QA | Regression bộ lọc với 3 lĩnh vực, xóa từng lựa chọn và xóa toàn bộ | Kết quả danh sách và bộ đếm filter cập nhật đúng |
| 2 | QA | Mở form sửa một chương trình Dự thảo khi có dữ liệu phù hợp | Nhãn vẫn là `Lĩnh vực pháp lý`, chọn đơn và lưu đúng |
| 3 | QA | Gắn doanh nghiệp tham gia chương trình rồi chạy lại báo cáo | `Số DN tham gia` tăng đúng lĩnh vực |
| 4 | QA/BA | Audit trạng thái module đầy đủ nếu cần kết luận readiness | Bao phủ toàn workflow, không chỉ 2 bug vừa re-verify |

## Follow-up TC đề xuất

| TC | Mục tiêu | Thời điểm |
|---|---|---|
| FUP-DN-01 | Chọn 3 lĩnh vực, bỏ từng giá trị rồi dùng `Xóa bộ lọc` | Ngay sau lượt này |
| FUP-CT-01 | Mở form sửa bản ghi Dự thảo và xác nhận nhãn/validation/chọn đơn | Khi có bản ghi Dự thảo phù hợp |
| FUP-CT-02 | Tạo chương trình ở lĩnh vực thứ ba, đối chiếu báo cáo tăng đúng 1 | Regression kế tiếp |
| FUP-CT-03 | Thêm DN tham gia và đối chiếu cột `Số DN tham gia` | Sau khi hoàn tất dữ liệu tham gia |

## Kết luận

- Closed-verified: **2/2**.
- Open/Reopen: **0/2**.
- Hai path từng bị block đã được mở lại: bộ lọc lĩnh vực DN và trường/báo cáo lĩnh vực chương trình.
- Không có blocker môi trường hoặc blocker ngoài hệ thống.
- Không cần BE seed thêm cho lượt re-verify này.
- Kết quả này chỉ đóng 2 bug Reopen; chưa thay thế audit readiness toàn module.
