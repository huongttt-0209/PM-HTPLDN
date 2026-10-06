# Nhật ký đo — QLTLPLCVV_17 (dòng 326) — vòng 2, 04/08/2026

**Bản dựng đang chạy:** `assets/index-DpIXRGaI.js` · `HTPLDN · V1.0.5`. **Tài khoản:** `cb_nv_tw_01` (`CB_NV_TW`, TW, Cục Bổ trợ tư pháp).
**Lỗi gốc cần kiểm:** nút "Xem" tệp trong nhóm "Tư liệu pháp lý liên kết" của Tư vấn chuyên sâu bị vô hiệu hoá.

| Giờ (VN) | Thao tác | Số liệu đo được |
|---|---|---|
| 14:47 | Chọn bản ghi: `GET /api/v1/tu-lieu-phap-ly-vvs?limit=50` | Chọn `TVCS-20260713-0003` vì có tư liệu **"Đã công khai" 5 tệp** (giống ảnh đối tác) **và** tư liệu "Nháp" 1 tệp để so trạng thái. |
| 14:47 | Menu Tư vấn chuyên sâu → mở chi tiết → mở nhóm "Tư liệu pháp lý liên kết" | 3 tư liệu. Dòng 0 tệp: chỉ có Sửa/Công khai/Xóa. Hai dòng có tệp (1 "Nháp", 1 "Đã công khai"): đều có nút **"Xem tệp"**, kiểm bằng mã `disabled = false`, không có lớp `ant-btn-disabled`. |
| 14:48 | Bấm "Xem tệp" trên tư liệu "TKM kiểm thử chức năng" (Đã công khai) | Mở cửa sổ "Xem tư liệu pháp luật" liệt kê 5 tệp: `.jpg`, `.xlsx`, 2× `.pdf`, `.docx`. **Cả 5 nút "Xem" đều dùng được.** Ảnh `image/QLTLPLCVV_17-v2-01-…png`. |
| 14:48 | Bấm "Xem" trên `2K15 T3 (13.7) & CN (19.7).pdf` | Mở **tab mới** với đường dẫn tệp có chữ ký thời hạn; hiển thị **trình xem PDF trực tuyến**, đọc được nội dung thật (2 trang, đề Toán 2K15). Ảnh `image/QLTLPLCVV_17-v2-02-…png`. |
| 14:48 | Bấm "Xem" trên `QLTLPLCVV_05.jpg` | Mở **khung xem ảnh trực tuyến** ngay trong trang, đúng ảnh, có thanh công cụ xoay/phóng to. Ảnh `image/QLTLPLCVV_17-v2-03-…png`. |
| 14:49 | Bấm "Xem" trên `.docx` rồi `.xlsx` | Không mở trình xem mà **tải về máy**, đúng tên `HTPLDN-PTYC-CT-v2.0(1).docx` và `vu-viec-export.xlsx` — khớp đặc tả "định dạng không hỗ trợ xem trực tuyến thì tải tệp về". |
| 14:49 | **Không dừng ở chỗ "tải được"** — tải thẳng 2 tệp đó về đọc byte | `.docx`: HTTP 200, **17.474.550 byte**, đầu tệp `50 4b 03 04`, kiểu Word. `.xlsx`: HTTP 200, **7.231 byte**, đầu tệp `50 4b 03 04`, kiểu Excel. → tệp thật, không rỗng, không hỏng. |

**Lưu ý nhỏ:** phiếu ghi bước "Bấm vào **tên tệp** đính kèm", nhưng trong giao diện tên tệp là chữ tĩnh (chỉ có biểu tượng ghim giấy), chỗ bấm được là nút "Xem" ngay cạnh. Yêu cầu nghiệp vụ vẫn đạt nên không đổi verdict.

**Kết luận: Pass.**
