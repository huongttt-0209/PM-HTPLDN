Mã case: QLKTLBG_18      Vòng: 1 (Dopai=N/R, dev báo Fixed)
Thời điểm viết: 2026-08-05 21:51
Môi trường verify: https://htpldn-uat.ospgroup.vn

1. Đối tác phản ánh: vào "Đào tạo, tập huấn" -> "Kho tài liệu / Bài giảng", nhập tiêu chí lọc rồi
   Xuất Excel -> "Màn hình không có nút chức năng".
   Bằng chứng QLKTLBG_18.jpg (25/07 08:51, CB_NV_TW): hàng nút trên cùng chỉ có [+ Thêm mới] [Làm mới];
   không thấy nút Xuất Excel. Bộ lọc nâng cao (2) đang bật.

2. Đặc tả nói gì — srs-fr-03-dao-tao.md:1952 (SCR-III-03 Thành phần 2):
   ':1952 - Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)'
   -> Màn PHẢI có chức năng xuất Excel, và kết quả xuất PHẢI áp theo bộ lọc hiện tại.
   API tồn tại: POST /api/v1/bai-giangs/export ("Xuất danh sách bài giảng ra Excel").
   IM LẶNG: danh sách cột của file Excel (FR-III-08 không có mục Processing xuất Excel, không có bảng cột)
   -> KHÔNG được chấm Fail vì thiếu/thừa cột trong file.

3. Precondition: tài khoản cbnv_tw · màn /dao-tao/bai-giang/danh-sach · có >=1 bài giảng hiển thị.

4. PASS khi (đủ cả 3):
   - Trên màn có chức năng xuất Excel truy cập được bằng thao tác UI (không phải chỉ có API).
   - Bấm xuất -> tải về được tệp Excel MỞ ĐỌC ĐƯỢC (không phải chỉ mã trả về 200).
   - Số dòng dữ liệu trong tệp KHỚP với kết quả đang lọc trên màn (đo bằng 2 phép: không lọc và có lọc,
     hai lần cho số dòng khác nhau đúng theo bộ lọc).
   FAIL nếu: không có chức năng xuất trên UI · bấm xuất không ra tệp · tệp mở không được/rỗng ·
   nội dung tệp KHÔNG đổi khi đổi bộ lọc (tức không áp bộ lọc hiện tại).
   KHÔNG chấm FAIL vì: thiếu cột / sai tên cột / sai tên tệp (spec im lặng).

5. Dạng dữ liệu phải phủ — M = 2: (1) xuất khi KHÔNG lọc  (2) xuất khi CÓ lọc (>=1 tiêu chí thu hẹp kết quả).
   Nguồn xác định M: chính câu spec "theo bộ lọc hiện tại" -> phải đo được sự khác biệt.

── SỬA ĐỔI #1 — 2026-08-05 22:1x (ghi TRƯỚC khi đo, chưa mở màn của case trên env mới) ──
Sửa gì: đổi "Môi trường verify" từ https://htpldn-uat.ospgroup.vn (bản dựng V1.0.7)
        sang env dev https://18.143.165.120.nip.io (bản dựng V1.0.8, bundle index-D-YMo5bZ.js).
Vì sao: user báo dev vừa build bản fix mới lên env dev; env đối tác chưa nhận bản đó.
        Đã kiểm chứng: dev = 1.0.8 > đối tác = 1.0.7.
KHÔNG sửa: mục 1 (đối tác phản ánh), 2 (đặc tả), 4 (PASS/FAIL), 5 (M dạng) — giữ nguyên như 21:51.
Hệ quả phải ghi trong verdict: Pass ở đây là PASS TẠM cho bản 1.0.8 trên env dev;
        chưa chứng minh đối tác mở env nghiệm thu (1.0.7) sẽ hết lỗi. Phải re-verify khi 1.0.8 lên env đối tác.
Tài khoản: bộ tài khoản env dev (xem input/input.md phần trên) — khác bộ env đối tác.
