# Bảng đối chiếu điều kiện — IBMHD_07

Loại bug: **Import một số tệp lỗi → không hiện "{Y} tệp lỗi: xem chi tiết" + bảng chi tiết lý do.** Verdict phụ thuộc: (1) app có phát sinh lỗi tại bước Import không, (2) SRS message E2.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (case chỉ định vai trò "CB Nghiệp vụ") | CB Nghiệp vụ (`cbnv_bn`) — cùng vai trò case yêu cầu | Không |
| Màn hình | `/bieu-mau/nhap-hang-loat` bước 3 | Cùng | Không |
| Thao tác | Import lô có tệp lỗi | Import 2 tệp hợp lệ; thử import trùng (duplicate) | Không |
| Giá trị quan sát | Không hiện "{Y} tệp lỗi: xem chi tiết" | Y hệt — lỗi định dạng/kích thước bị chặn tại bước Chọn file → tới bước Import chỉ còn tệp hợp lệ → "Đã nhập thành công 2 biểu mẫu" (chỉ success). Tệp trùng tên được chấp nhận (không lỗi) | Không |

**Kết luận: 0 GAP.** App validate định dạng/kích thước SỚM (bước chọn) nên tệp lỗi không tới bước Import → nhánh "{M} tệp lỗi: xem chi tiết" (E2 WRN-IMP-01, `srs-fr-09-bieu-mau.md:479`; Outputs chi_tiet_loi `:489`) không kích hoạt trong luồng thường. Duplicate không bị chặn → cũng không sinh lỗi import. → **BA confirm** (BA chốt: mô hình kiểm-sớm này có đạt AC "hiển thị tổng hợp N thành công, M lỗi" `:499` không). Bằng chứng: `BUG-IBMHD_07-step3-ket-qua-import.png`.

> Ghi chú vai trò (nội bộ): case chỉ định vai trò "CB Nghiệp vụ"; test bằng `cbnv_bn` do `cbnv_tw` bị chiếm session. Luồng import + thông báo kết quả không phụ thuộc đơn vị.
