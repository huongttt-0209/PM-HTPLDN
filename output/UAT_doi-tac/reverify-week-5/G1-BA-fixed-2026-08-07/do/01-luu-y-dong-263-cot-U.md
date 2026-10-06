# Lưu ý riêng dòng 263 (`CPCTHTTTG_05`) — ô `Ảnh/video verify` ĐÃ CÓ nội dung

**Dành cho agent B3** (người đo `CPCTHTTTG_05`). A2 đã cảnh báo: đây là ô cột U **duy nhất** trong
11 dòng của lô có sẵn nội dung → `sheet_g1_anhverify_write.py` sẽ chặn theo guard 2.

## Nội dung đang có (810 ký tự, do lượt đo 06/08 để lại)

```
CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png — Vai trò Quản trị hệ thống: ẢNH CHỤP ĐƯỢC khung thông báo "Forbidden" khi bấm Xuất (cùng màn, cùng tài khoản, cùng mã lỗi với lượt Xuất Excel)
CPCTHTTTG_05-B1-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc-V108.png — Vai trò Quản trị hệ thống: báo cáo hiện đủ số liệu và nút Xuất đang bấm được (trạng thái ngay trước khi bị từ chối)
CPCTHTTTG_05-thong-bao-va-phan-hoi-may-chu.txt — Nguyên văn chữ hiện cho người dùng + phản hồi 403 của máy chủ, có mốc giờ và số hiệu request; kèm kết quả đọc nội dung tệp Excel
CPCTHTTTG_05-xuat-excel-dang1.xlsx — Tệp Excel hệ thống giao ra cho Cán bộ Nghiệp vụ, kỳ Năm (mở đọc được, số khớp màn)
CPCTHTTTG_05-xuat-excel-dang2-khoang-thang6.xlsx — Tệp Excel lượt thứ hai, kỳ Khoảng 01/06-30/06 (nhãn kỳ đổi theo bộ lọc)
```

## Việc B3 phải làm trước khi quyết ghi đè

1. 🔴 **Kiểm xem 5 dòng này có phải siêu liên kết thật không.** `get_all_values()` chỉ trả chữ, **giấu**
   liên kết — nên "nhìn thấy tên tệp" chưa kết luận được là không có link. Đọc `hyperlink` /
   `textFormatRuns` của ô `U263` qua API (xem cách `fetch_evidence.py` và
   `sheet_g1_anhverify_write.py` đọc liên kết) rồi mới kết luận.
2. **Nếu chỉ là chữ trần, không có liên kết** → đây là bằng chứng **không xem được** đối với người đọc
   sheet (dev/đối tác mở sheet không mở nổi tệp trên máy QA). Khi đó phải thay bằng liên kết Drive thật
   của lượt đo hôm nay: `--cho-phep-ghi-de`, nhưng **giữ lại nhãn mô tả cũ nếu tệp cũ vẫn còn giá trị**
   (upload luôn tệp cũ lên Drive rồi gắn link, đừng xoá trắng chứng cứ của lượt trước).
3. **Nếu đã là siêu liên kết Drive thật** → **nối thêm** liên kết mới của lượt hôm nay, đừng đè mất
   liên kết cũ.
4. Ghi rõ trong note của case: đã chọn hướng nào và vì sao.

## Bẫy dễ mắc

- Dòng đầu của ô là ảnh mang mã **`CPCTHTTTG_06`** — tức bằng chứng của **case khác** bị để nhờ ở dòng
  263. Đừng coi nó là bằng chứng của `CPCTHTTTG_05`, và cũng đừng xoá nó đi mà không nói.
- Nội dung cũ mô tả trạng thái **trước** khi dev fix. Nhãn ảnh mới phải nói rõ mốc thời gian + bó mã
  bản dựng để không lẫn với ảnh 06/08.
