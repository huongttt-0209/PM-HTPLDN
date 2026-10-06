# Bảng đối chiếu điều kiện — IBMHD_04

Loại bug: **File lỗi không hiển thị trong bảng kiểm tra (Hợp lệ/Lỗi kèm lý do).** Verdict phụ thuộc: (1) app có báo file lỗi + lý do không, (2) SRS có bắt buộc liệt kê file lỗi trong bảng không.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (case chỉ định vai trò "CB Nghiệp vụ") | CB Nghiệp vụ (`cbnv_bn`) — cùng vai trò case yêu cầu | Không |
| Màn hình | `/bieu-mau/nhap-hang-loat` bước 1→2 | Cùng | Không |
| Thao tác | Upload tệp sai định dạng + tệp lỗi | Upload `.txt` (sai định dạng) + tệp `.docx` 22MB (>20MB) + 2 tệp hợp lệ | Không |
| Giá trị quan sát | File lỗi không vào bảng kiểm tra Hợp lệ/Lỗi | Y hệt — tệp lỗi bị loại NGAY tại bước Chọn file kèm lý do ("Định dạng không hỗ trợ..." / "vượt quá 20MB (22.0 MB)"); bảng kiểm tra chỉ liệt kê tệp hợp lệ | Không |

**Kết luận: 0 GAP.** Tái hiện đúng: tệp lỗi không xuất hiện thành dòng trong bảng kiểm tra — nhưng KHÔNG "im lặng": app báo lý do qua thông báo tại bước chọn. SCR-VII-03 mục #4 (`srs-fr-09-bieu-mau.md:675`) mô tả bảng có cột "Trạng thái (Hợp lệ/Lỗi)" nhưng **không có cột Lý do**; app kiểm sớm ở bước chọn thay vì liệt kê Lỗi trong bảng. Khác cách trình bày, không phải lỗi im lặng. → **BA confirm** (BA chốt: tệp lỗi có bắt buộc thành dòng trong bảng kiểm tra không, hay báo tại bước chọn là đủ). Bằng chứng: `BUG-IBMHD_04-step1-valid-2-reject-txt.png`, `BUG-IBMHD_04-step2-bang-kiem-tra.png`.

> Ghi chú vai trò (nội bộ): case chỉ định vai trò "CB Nghiệp vụ"; test bằng `cbnv_bn` do `cbnv_tw` bị chiếm session. Validate định dạng/kích thước là logic client-side chung, không phụ thuộc đơn vị.
