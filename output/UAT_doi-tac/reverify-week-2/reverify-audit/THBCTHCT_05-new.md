# Audit verify THBCTHCT_05-new

## Cổng 1 — Bằng chứng đối tác

- Đã xem full-res: `partner-evidence/THBCTHCT_05.jpg`.
- Bằng chứng đối tác chụp trước khi hoàn tất tổng hợp: trang vẫn còn nút `Tổng hợp`, vì vậy riêng ảnh này chưa đáp ứng điều kiện “đã hoàn thành tổng hợp toàn quốc”.
- Neo URL/ID: `/ct-htpldn/dot-bao-cao/5adb3002-9de8-4188-bef8-d769d7cee6b7`.
- Claim cần kiểm: sau khi hoàn thành tổng hợp toàn quốc phải có chức năng xuất Excel hoặc Word theo Biểu 21a/21b.

## Cổng 2 — Hiểu bug

- Điều kiện quyết định kết quả là trạng thái sau khi CBNV TW xác nhận tổng hợp thành công, không phải trạng thái trước khi bấm nút.
- Đã chuyển seed `DOT-THBC01-UAT` sang trạng thái tổng hợp bằng đúng flow UI và kiểm tra lại toàn trang sau toast thành công.

## Cổng 3 — Đối chiếu SRS với web

| SRS yêu cầu | Thực tế web | Đủ/thiếu |
|---|---|---|
| FR-XI-09 (UC170), dòng 1011: báo cáo tổng hợp có thể xuất Excel/Word. | Sau khi tổng hợp thành công, toàn trang không có nút/link xuất, tải, Excel hoặc Word. | Thiếu |
| FR-XI-09, dòng 1022: đầu ra có file `.xlsx` hoặc `.docx`. | Không có control tạo/tải file; DOM lần hai trả `totalExportControls=0`. | Thiếu |

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương | `cbnv_tw_01` — Cán bộ Nghiệp vụ Trung ương | Không |
| Có báo cáo đơn vị đã gửi | Có dữ liệu Biểu 21a trên trang | `DOT-THBC01-UAT`, 2/2 đơn vị đã nộp | Không |
| Đã hoàn thành tổng hợp toàn quốc | Ảnh đối tác chưa thể hiện điều kiện này | Đã bấm `Tổng hợp` → `Đồng ý`; POST tổng hợp thành công, toast `Tổng hợp báo cáo thành công`, hai đơn vị chuyển `Đã tổng hợp` | Không — đã bổ sung đúng trạng thái bằng live test |

## Gate real-data

- Bộ bắt thông báo chuẩn được cài trước thao tác và tự kiểm có đúng `1` observer.
- Kết quả thao tác: `1` request `POST /api/v1/dot-bao-caos/d7a62f6e-a119-4582-8b08-f935d25c534b/tong-hop`, `1` toast `Tổng hợp báo cáo thành công`, không lặp.
- Artifact ngay sau state change: `THBCTHCT_05-after-confirm-immediate.png`.
- Phương pháp 1: ảnh full-page sau tổng hợp đã được mở kiểm tra, không có chức năng xuất file.
- Phương pháp 2: DOM kiểm toàn bộ control nhìn thấy theo từ khóa `xuất|excel|word|tải`, kết quả `totalExportControls=0`.
- Bất thường ngoài tiêu chí BA: nút `Tổng hợp` vẫn còn sau khi tổng hợp thành công; chưa ghi thêm bug vì nằm ngoài phạm vi claim và chưa có test độc lập.

## Verdict

- `Bug` (Open): app thiếu chức năng xuất Excel/Word ở đúng trạng thái sau tổng hợp, sai FR-XI-09 dòng 1011 và 1022.
