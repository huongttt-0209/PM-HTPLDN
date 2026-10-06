# Nội dung CŨ của ô 'Kết quả verify' — dòng 64 · DGKQHTVV_01

Chụp lại lúc bắt đầu lô F3-devfix-2026-08-07, TRƯỚC khi đè (prompt mục 6 cho phép đè `--cho-phep-de-ketqua`).

- Trạng thái dev fix (lúc chụp): `Fixed`
- Dopai (lúc chụp): `dev done`
- DEV phản hồi lần 1 (lúc chụp): (trống)

---

## Nguyên văn ô 'Kết quả verify'

```text
🔁 Còn lỗi — chuyển lại dev.

CÒN LỖI Ở ĐÂU
Doanh nghiệp không đánh giá được vụ việc của chính mình. Đăng nhập bằng tài khoản doanh nghiệp rồi
bấm mở chi tiết một vụ việc đã "Hoàn thành" của chính doanh nghiệp đó thì bị đẩy sang trang báo
không có quyền, nên không nhìn thấy chỗ nào để bắt đầu đánh giá. Kiểm thêm bằng cách gọi thẳng
thao tác đánh giá thì hệ thống cũng từ chối vì lý do phân quyền, tức không phải chỉ là giao diện
thiếu nút. Thử trên 2 tài khoản doanh nghiệp khác nhau, kết quả như nhau.

ĐÚNG RA PHẢI THẾ NÀO
Doanh nghiệp là một trong hai đối tượng được đánh giá vụ việc, cùng với cán bộ nghiệp vụ. Nên
doanh nghiệp phải mở được vụ việc của mình và chấm được khi vụ việc ở "Hoàn thành" hoặc
"Đã đánh giá", mỗi doanh nghiệp chấm một lần cho mỗi vụ việc.

PHẦN ĐÃ HẾT LỖI — KHÔNG CẦN TEST LẠI
Nhánh cán bộ nghiệp vụ nay chạy đúng, tức lỗi cũ "gửi xong không lưu" đã được sửa. Chấm 9 - 8 - 10
kèm nhận xét rồi tải lại trang thì Nhóm 8 hiện đủ 3 điểm, điểm tổng 9/10, nhận xét đúng nguyên văn,
người đánh giá và thời điểm đều đúng; trạng thái vụ việc chuyển sang "Đã đánh giá". Đo trên 2 vụ
việc riêng, đối chiếu cả màn hình lẫn dữ liệu máy chủ, khớp nhau. Chấm lần thứ hai trên cùng vụ
việc bị chặn đúng, không ghi đè điểm cũ. Nhập điểm ngoài khoảng 0 - 10 cũng bị chặn đúng.

AI SỬA
Dev BE — phần phân quyền cho doanh nghiệp trên chức năng đánh giá và trên dữ liệu màn chi tiết.
Dev FE — phần màn chi tiết vụ việc ở chế độ doanh nghiệp.

CÁCH KIỂM LẠI SAU KHI SỬA
Đăng nhập bằng tài khoản doanh nghiệp, mở một vụ việc "Hoàn thành" của chính doanh nghiệp đó, chấm
3 điểm kèm nhận xét, sau đó TẢI LẠI TRANG rồi xem Nhóm 8 có hiện lại đúng những gì vừa nhập không.
Làm trên ít nhất 2 vụ việc và 2 doanh nghiệp khác nhau.
Đạt khi: doanh nghiệp mở được vụ việc của mình, chấm được, và sau khi tải lại trang đọc lại được
đủ 3 điểm, điểm tổng và nhận xét.
Chưa đạt khi: vẫn bị đẩy sang trang báo không có quyền; hoặc chấm được nhưng tải lại trang thì
Nhóm 8 trống; hoặc doanh nghiệp chấm được vụ việc của doanh nghiệp khác.

CHƯA KIỂM ĐƯỢC
Trường hợp vụ việc đã có đánh giá của cán bộ rồi, doanh nghiệp vào chấm tiếp. Muốn dựng được
trường hợp này thì phía doanh nghiệp phải chấm được trước, nên phải đợi sửa xong mới kiểm.

ĐÃ ĐO: ngày 06/08/2026, bản dựng V1.0.8. Phía cán bộ nghiệp vụ trên VV-BTP-TW-20260806-003 và
-004. Phía doanh nghiệp trên VV-STP-AG-20260806-005 và một vụ việc của doanh nghiệp thứ hai. Kiểm
cả trên màn hình lẫn dữ liệu máy chủ.
Tham chiếu đặc tả: srs-fr-05-vu-viec.md:1190 · :1198 · :2116 · :1809 · :1811
```
