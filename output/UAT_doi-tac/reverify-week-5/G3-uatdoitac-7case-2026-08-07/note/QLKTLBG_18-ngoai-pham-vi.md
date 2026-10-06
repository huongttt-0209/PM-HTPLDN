# QLKTLBG_18 — ghi nhận NGOÀI phạm vi phiếu (báo lead, KHÔNG tự thêm dòng sheet)

> Đo ngày 2026-08-07 17:00–17:12 trên `https://htpldn-uat.ospgroup.vn`, bản dựng **V1.0.10**
> (bó mã `index-Bd1akG3f.js`), tài khoản `cbnv_tw` (CB_NV_TW, cấp TW).
> Chi tiết số đo: [`do/QLKTLBG_18.md`](../do/QLKTLBG_18.md).

## 0. Điều KHÔNG thuộc mục này — đã tính vào verdict

Lỗi **bộ lọc "Công khai" trả sai tập kết quả** (chọn "Không công khai" → nhận 6 bản ghi đều
"Đã công khai", tệp Excel xuất ra cũng 6/6 dòng "Đã công khai") **KHÔNG** nằm ở đây.
Màn hình **có** ô lọc đó, `congKhai` là một tiêu chí lọc của chính chức năng xuất
(`BaiGiangExportDto`), nên theo phiếu giao việc nó **thuộc phạm vi case 18** và đã tính vào
verdict **Reopen** ghi ở dòng 12. Xem `do/QLKTLBG_18.md` §10.

## 1. Câu chữ lựa chọn ô lọc "Công khai" lệch đặc tả (candidate — chưa log bug)

| Nguồn | Nội dung |
|---|---|
| Trên màn (đọc thật danh sách xổ) | 2 lựa chọn: **"Công khai"** · **"Không công khai"** |
| `srs-fr-03-dao-tao.md:1958` | `- Lọc Công khai: Tất cả / Đã công khai / Chưa công khai [STT66 UAT 2026-06-02]` |
| `srs-fr-03-dao-tao.md:1971` (badge cột) | `**Badge** "Đã công khai" / "Chưa công khai"` |

Chênh 2 điểm: (a) thiếu mục **"Tất cả"**; (b) câu chữ 2 giá trị còn lại không khớp badge đang
dùng ngay trên cùng màn. Người dùng thấy 2 hệ chữ khác nhau cho cùng một khái niệm.

## 2. Ô lọc "Loại tài liệu" không có mục "Tất cả" (candidate)

Trên màn có đúng 3 lựa chọn **PDF / Slide / Video**; `srs-fr-03-dao-tao.md:1956` ghi
*"Lọc Loại tài liệu: Tất cả / Slide / PDF / Video"*. Việc bỏ lọc hiện làm bằng nút xoá (×) của
chính ô hoặc nút "Xóa bộ lọc" — vẫn dùng được, chỉ khác cách đặc tả mô tả.

## 3. Nút "Làm mới" thừa so với đặc tả (candidate — đã nêu sẵn ở chuẩn chấm §4)

`srs-fr-03-dao-tao.md:1949–1952` liệt kê Hành động chính của SCR-III-03 gồm **2 nút**
("+ Thêm mới", "Xuất Excel"). Màn thực tế có **3 nút**, thêm **"Làm mới"**. Không cản trở nghiệp vụ.

## 4. Tài liệu — bảng §6 thiếu FR-III-07 / FR-III-08 ở dòng BR-DATA-06 (không phải lỗi phần mềm)

`srs-fr-03-dao-tao.md:2243` liệt kê BR-DATA-06 cho `FR-III-01, FR-III-05, FR-III-06, FR-III-14`,
**thiếu FR-III-07 / FR-III-08**, trong khi đặc tả cấp màn `:1952` quy định màn này **có** nút
Xuất Excel và `srs-v3.5.md:5570` ghi Áp dụng FR = *"Toàn bộ CRUD list"*. Đây là **điểm cần chỉnh ở
tài liệu**, không phải lỗi phần mềm. (Cùng nội dung đã ghi ở chuẩn chấm `chuan/QLKTLBG_18.md` §4
và ở `do/QLKTLBG_19.md` §12.)

## 5. Không tồn tại quyền xuất riêng cho bài giảng (đã do người đo case 19 ghi nhận — nhắc lại để không sót)

Bộ quyền hệ thống **không có** `export_bai_giang` (trong khi các danh sách khác đều có quyền xuất
riêng: `export_vu_viec`, `export_doanh_nghiep`, `export_tu_van_vien`…), nhưng lời gọi xuất bài giảng
vẫn trả **200**. Ghi nhận để lead cân nhắc; **không** thuộc phạm vi case 18.
