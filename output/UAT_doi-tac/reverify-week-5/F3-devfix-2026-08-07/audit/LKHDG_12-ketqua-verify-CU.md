# Nội dung CŨ của ô 'Kết quả verify' — dòng 126 · LKHDG_12

Chụp lại lúc bắt đầu lô F3-devfix-2026-08-07, TRƯỚC khi đè (prompt mục 6 cho phép đè `--cho-phep-de-ketqua`).

- Trạng thái dev fix (lúc chụp): `Fixed`
- Dopai (lúc chụp): `dev done`
- DEV phản hồi lần 1 (lúc chụp): (trống)

---

## Nguyên văn ô 'Kết quả verify'

```text
🔁 Còn lỗi — chuyển lại dev.

- Triệu chứng lần này: sau khi lọc, nút [Xuất Excel] vẫn tạo tệp chứa TOÀN BỘ danh sách. Lọc Tần suất "Tròn năm" → màn 19 kết quả, tệp 20 dòng (thừa DG-20260806-0001 là "Sơ bộ 6 tháng"). Lọc Trạng thái "Hoàn thành" → màn 4 kết quả, tệp vẫn 20 dòng, đủ 7 trạng thái. Hai lượt cho tệp cùng kích thước 8520 byte.
- Đường dẫn yêu cầu xuất CÓ mang tham số lọc (?tanSuat=... / ?trangThai=...) nhưng tệp không phản ánh — giao diện gửi đúng, phần sinh tệp không dùng tham số. Gọi thẳng API cùng chuỗi truy vấn: danh sách trả 4 / 19 / 20 bản ghi đúng theo lọc, còn tệp xuất trả 8519 byte y hệt ở cả 3 trường hợp, kể cả khi không lọc.
- Đặc tả đòi: BR-DATA-06 (srs-v3.5.md:5525) — "File xuất theo bộ lọc hiện tại", áp dụng "Toàn bộ CRUD list", ngoại lệ chỉ nêu báo cáo nhóm IX. Nút [Xuất Excel] của màn: srs-fr-08-danh-gia.md:821.
- Đã test bằng: tài khoản cbnv_tw (CB Nghiệp vụ Trung ương), màn Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách, 20 đợt phủ 7 trạng thái và 2 giá trị Tần suất. Bản dựng HTPLDN V1.0.8 (env kiểm thử nội bộ) — chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu.
- Hai vế còn lại của phiếu ĐÃ HẾT LỖI: tệp nay đủ 10 cột (có "Số vụ việc", "Người tạo", "Ngày tạo") và nhãn ghi tiếng Việt có dấu ("Sơ bộ 6 tháng", "Lập kế hoạch"). Vì còn 1 vế lỗi nên cả phiếu vẫn là Còn lỗi.
- Chủ việc tiếp theo: Dev BE — áp bộ lọc vào truy vấn của POST /api/v1/ke-hoach-danh-gias/export.

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản `cbnv_tw` (CB Nghiệp vụ Trung ương, Test@1234) + màn
  https://18.143.165.120.nip.io/danh-gia/ke-hoach/danh-sach.
  Danh sách phải có ≥2 giá trị khác nhau ở cột định lọc (nếu mọi đợt cùng Tần suất thì phải
  tạo thêm 1 đợt khác Tần suất, nếu không thì phép đo vô nghĩa).
1) Ghi lại tổng số kết quả khi CHƯA lọc (đọc ở chân bảng "Hiển thị 1-N / N kết quả").
2) Chọn Tần suất = "Tròn năm" → bấm [Tìm kiếm]. Ghi lại số kết quả sau lọc = n_lọc (phải < tổng).
3) Bấm [Xuất Excel] → mở tệp, đếm số dòng dữ liệu (không kể dòng tiêu đề) và liệt kê cột "Mã KH".
4) Lặp lại bước 2-3 với cột lọc KHÁC: [Xóa bộ lọc] rồi Trạng thái = "Hoàn thành".
✅ PASS khi: cả 2 lượt, số dòng dữ liệu trong tệp = đúng n_lọc của lượt đó, VÀ tập "Mã KH"
   trong tệp trùng khít tập mã đang hiện trên màn (so từng mã, không chỉ so số lượng).
❌ FAIL nếu: tệp chứa ≥1 mã không thuộc tập sau lọc, hoặc số dòng ≠ n_lọc, hoặc 2 lượt lọc
   khác nhau lại cho 2 tệp cùng kích thước byte.
⚠️ Đừng chấm Fail vì tệp thiếu cột hay vì định dạng nhãn — đặc tả không quy định tập cột của
   tệp xuất; chỉ chấm đúng phần "theo bộ lọc hiện tại" của BR-DATA-06.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy đường dẫn yêu cầu xuất CÓ mang tham số lọc — giao diện
   gửi đúng tham số ngay cả khi đang lỗi (lượt này URL có `?trangThai=HOAN_THANH` mà tệp vẫn
   20 dòng); phải mở tệp đếm dòng.
Ảnh lỗi cũ: image/LKHDG_12-luot1-man-loc-TronNam-19ketqua-V108.png
            image/LKHDG_12-luot2-man-loc-HoanThanh-4ketqua-V108.png
```
