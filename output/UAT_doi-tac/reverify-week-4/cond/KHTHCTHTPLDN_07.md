# Bảng đối chiếu điều kiện — KHTHCTHTPLDN_07 (row 29) — Xuất tệp danh sách chương trình

**Kết luận:** BA confirm — đặc tả v3.5 không quy định tên tệp. Nội dung tệp thì phát sinh một lỗi khác, QA mở dòng riêng.

Phiếu ghi *"Tên tệp không giống với thiết kế"*, mong `DanhSachChuongTrinh_{YYYYMMDD_HHmm}.xlsx`, thực tế `ct-htpldn-2026-07-27.xlsx` → **đúng là khác**, nhưng `srs-fr-15-ct-htpldn.md:387-410` mô tả đầy đủ quy trình xuất Excel mà **không có dòng nào quy định tên tệp**. Mẫu tên đối tác mong đợi trùng quy ước của một nhóm khác (`srs-fr-02-hoi-dap.md:151`). → chuyển BA-19.

**Phát hiện thêm khi mở tệp ra đọc (ngoài phiếu):** hai cột thời gian trong tệp **lệch 1 ngày** so với màn hình. → mở dòng mới `KHTHCTHTPLDN_OOS_06`, lỗi `BUG-CT-XUAT-EXCEL-SAI-NGAY`.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/KHTHCTHTPLDN_07.jpg`) | Mình test (env nip.io, 27/07/2026 14:01) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Phiếu ghi tác nhân Cán bộ nghiệp vụ; ảnh là cửa sổ Excel nên không đọc được tài khoản, nhưng các case cùng nhóm đều chụp bằng `CB_NV_TW` | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Đây cũng là vai trò duy nhất thấy nút [Xuất Excel] (tài khoản `cbpd_tw` không có nút này) | Không |
| Entity + trạng thái (state machine) | Tệp đối tác gồm 15 chương trình trải đủ trạng thái Dự thảo / Chờ phê duyệt / Đã duyệt / Đã công bố / Đang thực hiện / Tạm dừng / Hoàn thành / Đã hủy | Tệp QA gồm 8 chương trình trải Đã duyệt / Đã công bố / Đang thực hiện / Hoàn thành. Ít trạng thái hơn nhưng **không ảnh hưởng phép đo**: case này kiểm tên tệp và tập cột, không kiểm nội dung theo trạng thái | Không |
| Dữ liệu tiền đề | Danh sách có dữ liệu để xuất | Có 8 chương trình, trong đó **có cả bản ghi đủ hai mốc thời gian, bản ghi chỉ có ngày bắt đầu, và bản ghi không gắn lĩnh vực** — dựng đủ các dạng để đọc được cả ô có giá trị lẫn ô trống trong tệp | Không |
| Input / filter / giá trị nhập | Bước 2 của phiếu là "Nhập/chọn tiêu chí lọc" rồi mới xuất | Xuất **không đặt bộ lọc** (toàn bộ 8 bản ghi). Chọn vậy để tách bạch: case này chấm tên tệp và tập cột; phần "xuất theo bộ lọc hiện tại" đã được xác nhận riêng qua việc tệp trả đúng 8/8 bản ghi đang hiển thị | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Tệp xuất / nội dung tệp)

- `partner-evidence/KHTHCTHTPLDN_07.jpg` — đã mở đọc: cửa sổ Excel, thanh tiêu đề ghi tên tệp **`ct-htpldn-2026-07-20.xlsx`**, sheet "Chương trình HTPL", hàng tiêu đề đọc được `Mã CT | Tên CT | Mục tiêu | Đối tượng | Trạng thái | Lĩnh vực | Đơn vị | ...`. Trùng khít với tệp QA tải về (chỉ khác phần ngày trong tên).
- Tệp `ct-htpldn-2026-07-27.xlsx` QA tải về — **đã mở ra đọc nội dung bằng công cụ đọc bảng tính, không chỉ kiểm tra tệp tải được**: 1 sheet "Chương trình HTPL", 8 dòng dữ liệu, 13 cột.
- `bug-reports/image/BUG-CT-danh-sach-thieu-loc-donvi-trangthai-va-cot-linhvuc.png` — đã mở đọc, dùng làm mốc đối chiếu ngày tháng trên màn hình với ngày tháng trong tệp.

## Phương pháp thứ hai (bắt buộc)

- **Mở tệp ra đọc từng cột thay vì chỉ xác nhận tệp tải được.** Đối chiếu 1-1 với 10 cột bắt buộc ở `srs-fr-15-ct-htpldn.md:396` — *"Tạo file .xlsx với các cột: Mã CT, Tên CT, Mục tiêu, Đối tượng, Lĩnh vực pháp lý, Thời gian (bắt đầu - kết thúc), Ngân sách, Đơn vị, Trạng thái, Số đợt BC"*. Kết quả: **đủ cả 10**, thêm 2 cột ngoài danh sách là "Là công bố" và "Ngày tạo", và cột thời gian được tách làm hai ("Thời gian bắt đầu", "Thời gian kết thúc"). Không thiếu cột nào.
- **Đối chiếu chéo giá trị màn hình ↔ tệp — đây là chỗ lộ lỗi.** Lấy `CT-20260724-0001`: bảng hiển thị *1/1/2026 — 31/12/2026*, tệp ghi *2025-12-31 17:00 — 2026-12-30 17:00*. Kiểm thêm 2 chương trình nữa, đều lệch **−1 ngày**. Nếu chỉ dừng ở "tệp tải được, có đủ cột" thì đã bỏ sót lỗi này.
- **Khoanh vùng nguyên nhân bằng dữ liệu gốc:** đọc thẳng máy chủ cho `CT-20260725-0002` → `thoiGianBatDau = "2025-12-31T17:00:00.000Z"`, cộng 7 giờ đúng bằng 01/01/2026 00:00 giờ Việt Nam. ⇒ Dữ liệu lưu đúng, màn hình quy đổi đúng, chỉ khâu ghi ra tệp không quy đổi múi giờ.
- **Rà toàn bộ đặc tả nhóm để tìm căn cứ tên tệp:** quét cả file `srs-fr-15-ct-htpldn.md`, không có chuỗi `DanhSach` và không có mẫu tên tệp nào. Chỗ duy nhất trong SRS v3.5 có mẫu tên dạng này là `srs-fr-02-hoi-dap.md:151` — *"Trả về file tải về. Tên file: `HoiDap_{YYYYMMDD_HHmm}.xlsx`"* — thuộc nhóm Hỏi đáp. ⇒ Không đủ căn cứ chấm lỗi cho nhóm CT HTPLDN, chuyển BA-19.
- **Kiểm phần chạy đúng để không quy kết quá phạm vi:** nút [Xuất Excel] có mặt đúng vai trò, tệp tải về ngay, đủ 8/8 bản ghi đang hiển thị (khớp yêu cầu "theo bộ lọc hiện tại" ở `:394`), mở được bằng Excel, 1 sheet đặt tên tiếng Việt có dấu. Phần cơ chế xuất chạy tốt.
