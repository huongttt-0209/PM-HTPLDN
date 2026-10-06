# Re-verify Dev fix sau phản hồi BA — UAT tuần 3

- Ngày kiểm tra: 24/07/2026
- Tab: `UAT_TGPL Doanh Nghiệp-tuần 3`
- Phạm vi: `QLDNDHTPL_05`, `QLDNDHTPL_06`, `QLDNDHTPL_13`, `TKDNHTPL_02`, `TKDNHTPL_03`, `CTTLV_01`
- Cách kiểm tra: Chrome DevTools, bám đúng `CÁCH VERIFY` và điều kiện PASS/FAIL trong cột `DEV phản hồi lần 1`
- Kết quả: **4 Pass, 2 Reopen**

## Tổng quan

| Module / task | Bug Open | Bug Closed | Bug re-verify | TC/path unblock | TC/path vẫn block | Next action |
|---|---:|---:|---:|---|---|---|
| Doanh nghiệp — form tạo mới | 0 | 3 | 3 | Bố cục nhóm A/B/C; prefill tỉnh theo phạm vi tài khoản | Không | Có thể chạy regression lưu mới DN |
| Doanh nghiệp — tìm kiếm/lọc | 1 | 1 | 2 | Hai nhánh 0 kết quả | Nhãn bộ lọc `Lĩnh vực KD` | Dev sửa nhãn rồi re-verify `TKDNHTPL_02` |
| Chương trình HTPLDN / báo cáo lĩnh vực | 1 | 0 | 1 | Bắt buộc, chọn đơn, danh mục và báo cáo theo lĩnh vực | Tên trường `Lĩnh vực pháp lý` | Dev đổi đúng tên trường rồi re-verify `CTTLV_01` |

## 1. Bug Re-verify

| Mã bug | Dòng sheet | Kết quả | Quan sát theo guide | Cập nhật sheet | Bằng chứng |
|---|---:|---|---|---|---|
| `QLDNDHTPL_05` | 26 | Closed-verified / Pass | Form có 3 khối đúng thứ tự; 5 trường Tên DN, MST, Người đại diện, Email, SĐT nằm trong khối đầu | `Q26 = Pass`; không đổi cột khác | [3 khối và Nhóm A](image/QLDNDHTPL_05-pass-3-khoi-nhom-A.png) |
| `QLDNDHTPL_06` | 27 | Closed-verified / Pass | Khối Địa lý và phân loại chứa Tỉnh/TP, Địa chỉ, Loại DN, Quy mô, Ngành nghề; form đủ 3 khối | `Q27 = Pass`; không đổi cột khác | [Nhóm B](image/QLDNDHTPL_06-pass-nhom-B.png) |
| `QLDNDHTPL_13` | 30 | Closed-verified / Pass | Tài khoản Hà Nội được điền sẵn Hà Nội và vẫn đổi được; tài khoản Trung ương để trống | `Q30 = Pass`; không đổi cột khác | [Hà Nội prefill và đổi được](image/QLDNDHTPL_13-dp-prefill-ha-noi-doi-duoc.png), [Trung ương để trống](image/QLDNDHTPL_13-tw-tinh-de-trong.png) |
| `TKDNHTPL_02` | 41 | Open / Reopen | Không còn bộ lọc Ngành nghề riêng; dropdown có `Tất cả` và chọn được nhiều giá trị. Tuy nhiên thanh lọc không hiển thị nhãn bắt buộc `Lĩnh vực KD` | `P41 = Reopen`, `Q41 = Reopen`; R41 đã ghi đè triệu chứng hiện tại | [Thiếu nhãn Lĩnh vực KD](image/TKDNHTPL_02-reopen-thieu-nhan-linh-vuc-kd.png) |
| `TKDNHTPL_03` | 42 | Closed-verified / Pass | Cả từ khóa không khớp và tổ hợp bộ lọc không khớp đều hiện đúng `Không tìm thấy doanh nghiệp phù hợp` | `Q42 = Pass`; không đổi cột khác | [Từ khóa không khớp](image/TKDNHTPL_03-pass-keyword-no-result.png), [Bộ lọc không khớp](image/TKDNHTPL_03-pass-filter-no-result.png) |
| `CTTLV_01` | 270 | Open / Reopen (Partial) | Trường bắt buộc, chọn một giá trị, danh mục dùng chung và báo cáo 2 lĩnh vực đều đạt. Form lại ghi `Lĩnh vực pháp luật`, không đúng tên `Lĩnh vực pháp lý` trong guide | `P270 = Reopen`, `Q270 = Reopen`; R270 đã ghi đè triệu chứng hiện tại | [Tên trường trên form](image/CTTLV_01-form-bat-buoc-linh-vuc-phap-luat.png), [Danh mục](image/CTTLV_01-form-dropdown-danh-muc.png), [Báo cáo 2 lĩnh vực](image/CTTLV_01-report-2-linh-vuc.png) |

## 2. Bug Summary

| Trạng thái | Số lượng | Bug |
|---|---:|---|
| Closed-verified / Pass | 4 | `QLDNDHTPL_05`, `QLDNDHTPL_06`, `QLDNDHTPL_13`, `TKDNHTPL_03` |
| Open / Reopen | 2 | `TKDNHTPL_02`, `CTTLV_01` |
| Blocked / chưa chạy | 0 | Không có trong phạm vi 6 bug |

## 3. TC/Path affected

| TC/path | Trạng thái sau re-verify | Ảnh hưởng |
|---|---|---|
| Tạo mới doanh nghiệp — bố cục nhóm A/B/C | Unblocked | Có thể regression nhập và lưu dữ liệu theo từng nhóm |
| Tạo mới doanh nghiệp — prefill tỉnh ĐP/TW | Unblocked | Có thể regression lưu mới và kiểm tra dữ liệu chi tiết |
| Danh sách doanh nghiệp — 0 kết quả | Unblocked | Có thể chạy thêm tổ hợp từ khóa/bộ lọc |
| Danh sách doanh nghiệp — bộ lọc lĩnh vực | Vẫn block một phần | Chức năng lọc hoạt động nhưng tiêu chí nhãn chưa đạt |
| Tạo/sửa chương trình — lĩnh vực | Vẫn block một phần | Bắt buộc/chọn đơn/danh mục đạt; tên trường chưa đúng guide |
| Báo cáo chương trình theo lĩnh vực | Unblocked | Hai lĩnh vực được đếm riêng; record cũ chưa phân loại vẫn được phép theo lưu ý BA |

## 4. Testability Sweep

| Nhóm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Happy path | Đã chạy | 3 khối form DN; prefill tỉnh; chọn lĩnh vực; báo cáo theo lĩnh vực |
| Empty/no-result | Đã chạy | Từ khóa và tổ hợp bộ lọc đều trả đúng thông báo |
| Validation | Đã chạy | Không lưu form chương trình khi bỏ trống trường lĩnh vực |
| Role/scope | Đã chạy | Cán bộ Trung ương và cán bộ Hà Nội |
| Multi-select/single-select | Đã chạy | Lọc DN chọn nhiều; lĩnh vực chương trình chỉ giữ một giá trị |
| Legacy/null data | Đã quan sát | Báo cáo còn 3 chương trình `Chưa phân loại`; không tính FAIL theo lưu ý BA |
| Regression ngoài phạm vi | Chưa chạy | Không mở rộng sang các bug không có guide |

## 5. Setup

| Hạng mục | Trạng thái | Chi tiết |
|---|---|---|
| Tài khoản | Sẵn sàng | Dùng đúng tài khoản kiểm thử theo vai trò Trung ương, Hà Nội và phê duyệt Trung ương |
| Dữ liệu báo cáo | Đã bổ sung qua UI | Tạo và phê duyệt `CT-20260724-0001`, lĩnh vực Lao động, để đủ ít nhất 2 chương trình thuộc 2 lĩnh vực |
| Dữ liệu đối chứng | Sẵn có | `CT-20260721-0001` thuộc Thương mại |
| Công cụ | Sẵn sàng | Chrome DevTools; không dùng `curl` để kết luận |
| Sheet write-back | Hoàn tất | Tất cả 6 dòng đã đọc lại sau ghi; trạng thái khớp |

## 6. Spec/BA Confirmation

| Nội dung | Kết luận áp dụng |
|---|---|
| Nhãn khối A/B | Không cần trùng từng ký tự; đúng cách gom và ý nghĩa là đạt |
| Tỉnh của tài khoản Trung ương | Để trống là đúng thiết kế |
| Thông báo 0 kết quả | Phải đúng `Không tìm thấy doanh nghiệp phù hợp` ở cả hai nhánh |
| Bộ lọc lĩnh vực DN | Phải có nhãn `Lĩnh vực KD`, có `Tất cả`, hỗ trợ chọn nhiều và không có bộ lọc Ngành nghề riêng |
| Trường lĩnh vực chương trình | Phải có tên `Lĩnh vực pháp lý`, bắt buộc, chọn một và lấy từ danh mục dùng chung |
| Chương trình cũ chưa có lĩnh vực | Có thể còn ở nhóm chưa phân loại; không tính FAIL nếu không có yêu cầu migrate |

## 7. Next actions

| Ưu tiên | Owner | Việc cần làm | Điều kiện đóng |
|---:|---|---|---|
| 1 | Dev FE | Hiển thị nhãn `Lĩnh vực KD` cho bộ lọc lĩnh vực doanh nghiệp | Nhãn xuất hiện đúng; giữ `Tất cả`, multi-select và không thêm bộ lọc Ngành nghề riêng |
| 2 | Dev FE | Đổi tên trường form chương trình từ `Lĩnh vực pháp luật` thành `Lĩnh vực pháp lý` | Tạo mới và sửa đều hiển thị đúng tên; không làm hỏng validation/chọn đơn |
| 3 | QA | Re-verify ngay 2 bug Reopen | `TKDNHTPL_02` và `CTTLV_01` đạt toàn bộ guide |
| 4 | QA | Chạy regression các path vừa unblock | Không phát sinh lỗi ở lưu mới DN và báo cáo chương trình theo lĩnh vực |

## Follow-up TC đề xuất

| TC | Mục tiêu | Thời điểm |
|---|---|---|
| FUP-DN-01 | Lưu mới DN đủ 3 khối rồi mở chi tiết, đối chiếu dữ liệu | Ngay sau đợt này |
| FUP-DN-02 | Thử 3 lĩnh vực cùng lúc, xóa từng lựa chọn và `Xóa bộ lọc` | Sau khi `TKDNHTPL_02` được sửa |
| FUP-CT-01 | Mở cả form tạo mới và form sửa, xác nhận cùng nhãn `Lĩnh vực pháp lý` | Sau khi `CTTLV_01` được sửa |
| FUP-CT-02 | Tạo thêm một chương trình ở lĩnh vực thứ ba và đối chiếu tăng đúng 1 trong báo cáo | Sau khi `CTTLV_01` được sửa |
| FUP-CT-03 | Gắn doanh nghiệp tham gia chương trình rồi đối chiếu cột `Số DN tham gia` | Sau khi hoàn tất setup dữ liệu tham gia |

## Kết luận

- Closed-verified: **4/6**.
- Open/Reopen: **2/6**; không có bug bị block do môi trường.
- Có thể chạy ngay regression form DN, prefill tỉnh và hai nhánh 0 kết quả.
- Cần Dev sửa trước khi đóng: nhãn `Lĩnh vực KD` và tên trường `Lĩnh vực pháp lý`.
- Không cần BE seed thêm cho lượt re-verify hiện tại; dữ liệu hai lĩnh vực đã được tạo qua UI.
- Sau khi 2 bug Reopen đạt, nên chạy audit trạng thái module đầy đủ để xác nhận toàn bộ workflow, không chỉ 6 bug này.
