# Bảng đối chiếu điều kiện — QLTLPLCVV_17 (dòng 326) — Xem tệp trực tuyến ở Tư liệu pháp lý liên kết

**Kết luận:** Pass — nút "Xem" của tệp không còn bị vô hiệu hoá; PDF và ảnh mở trình xem trực tuyến, định dạng khác tải về máy.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1 / phiếu đối tác) | Mình đo lại (04/08/2026 14:47–14:49, bản dựng index-DpIXRGaI.js · V1.0.5) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương | `cb_nv_tw_01` — `CB_NV_TW`, cấp TW, đơn vị Cục Bổ trợ tư pháp | Không |
| Màn hình / entity | Tư vấn → Tư vấn chuyên sâu → Xem chi tiết → Nhóm 3 "Tư liệu pháp lý liên kết" | Đúng 4 bước của phiếu, bản ghi `TVCS-20260713-0003`; nhóm 3 có 3 tư liệu | Không |
| Trạng thái tư liệu | Ảnh đối tác: tư liệu **"Đã công khai"** | Kiểm cả 2 trạng thái: "Đã công khai" (TKM kiểm thử chức năng, 5 tệp) và "Nháp" (tài liệu kiểm thử, 1 tệp) — cả hai đều có nút "Xem tệp" dùng được | Không |
| Định dạng tệp (quyết định nhánh xem trực tuyến hay tải về) | Ảnh đối tác là tệp Word | Kiểm đủ 4 định dạng trên cùng một tư liệu: `.pdf`, `.jpg`, `.docx`, `.xlsx` | Không |
| Thao tác | Bấm vào tệp đính kèm | Bấm nút "Xem" cạnh từng tên tệp trong cửa sổ "Xem tư liệu pháp luật" | Không |

**Bằng chứng:**
- `image/QLTLPLCVV_17-v2-01-nut-Xem-tep-khong-con-bi-vo-hieu-hoa.png` — cửa sổ "Xem tư liệu pháp luật" của tư liệu "TKM kiểm thử chức năng": 5 tệp, mỗi tệp có nút **"Xem" màu xanh, không bị làm mờ**. Kiểm bằng mã: cả 5 nút đều `disabled = false`, không mang lớp `ant-btn-disabled`.
- `image/QLTLPLCVV_17-v2-02-pdf-mo-trinh-xem-truc-tuyen.png` — bấm Xem trên `2K15 T3 (13.7) & CN (19.7).pdf`: mở tab mới hiển thị **trình xem PDF trực tuyến**, đọc được nội dung thật (đề Toán 2K15, 2 trang, có ô đếm trang 1/2 và bảng thu nhỏ trang bên trái).
- `image/QLTLPLCVV_17-v2-03-anh-mo-khung-xem-truc-tuyen.png` — bấm Xem trên `QLTLPLCVV_05.jpg`: mở **khung xem ảnh trực tuyến** ngay trong trang, hiển thị đúng ảnh kèm thanh công cụ xoay/phóng to.
- Định dạng không xem trực tuyến được thì **tải về**, đúng như đặc tả: `.docx` → tải `HTPLDN-PTYC-CT-v2.0(1).docx`, `.xlsx` → tải `vu-viec-export.xlsx` (đều qua thẻ tải có thuộc tính tên tệp).
- Không dừng ở chỗ "có tải được": tải thẳng 2 tệp đó về đọc byte — `.docx` 17.474.550 byte, `.xlsx` 7.231 byte, đầu tệp đều là `50 4b 03 04` (đúng định dạng Office thật, không phải tệp rỗng/hỏng), kiểu nội dung máy chủ trả về đúng loại Word/Excel.

**Lưu ý nhỏ (không đổi verdict):** phiếu ghi bước "Bấm vào **tên tệp** đính kèm", nhưng trong giao diện tên tệp chỉ là chữ tĩnh — chỗ bấm được là nút "Xem" ngay cạnh. Yêu cầu nghiệp vụ (mở trực tuyến / tải về) vẫn đạt.
