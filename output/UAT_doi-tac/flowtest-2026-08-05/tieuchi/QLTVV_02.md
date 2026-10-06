Mã case: QLTVV_02        Vòng: 2 (dev fix lần 1 xong, đối tác vẫn Fail)
Thời điểm viết: 2026-08-05 21:51
Môi trường verify: https://htpldn-uat.ospgroup.vn (env đối tác — bằng chứng chụp ở đây)

1. Đối tác phản ánh (vòng 2, ảnh QLTVV_02_v2.png 25/07 11:28, CB_NV_TW):
   (a) cột "Điểm ĐG" tràn/đè lên cột "Trạng thái"
   (b) cột Điểm ĐG hiển thị không đồng nhất: chưa có điểm "-/5", có điểm hiện số sao
   (c) nút Xem/Sửa bị xuống dòng

2. Đặc tả nói gì — srs-fr-04-chuyen-gia-tvv.md:1445-1457 (SCR-IV-01):
   #24 Điểm đánh giá | "số + sao" | 'Ví dụ: "4.5/5" + 5 sao. Nếu chưa có đánh giá: hiển thị "—/5"'
   #27 Hành động | "nhóm icon" | Icon Xem (mắt) / Sửa (bút chì) / Xóa (thùng rác)
   #29 phân trang 20 mục/trang
   srs-v3.5.md:579 (UI-07): "Cuộn ngang cho bảng nhiều cột"
   -> (a) tràn/đè = VI PHẠM UI-07.
   -> (b) "-/5" khi chưa có điểm = ĐÚNG spec. Vế này đối tác hiểu sai. Chỉ sai nếu bản CÓ điểm
          mà thiếu MỘT trong hai thành phần (số HOẶC sao).
   -> (c) spec đòi NHÓM ICON, app đang render nút CHỮ -> lệch spec ở mức kiểu thành phần.
   IM LẶNG: sắp xếp mặc định của bảng này (kỳ vọng "ngày công nhận mới nhất trước" KHÔNG có căn cứ).

3. Precondition: tài khoản cbnv_tw (CB_NV_TW) / Test@1234 · màn /chuyen-gia-tvv/danh-sach · tab "Đang hoạt động"
   Viewport rộng >=1440 (tràn cột phụ thuộc bề rộng - phải ghi rõ viewport đã dùng).

4. PASS khi (đủ cả 4):
   - Cột "Điểm ĐG" và "Trạng thái" KHÔNG chồng lấn ở viewport 1440; bảng nhiều cột có cuộn ngang.
   - Bản ghi CÓ điểm hiển thị đủ CẢ số dạng "{X.X}/5" VÀ dải sao; bản ghi CHƯA có điểm hiển thị "—/5".
   - Giá trị điểm nằm trong thang [0..5] — không có giá trị vượt 5.
   - Cụm hành động render dạng icon, không bị xuống dòng/cắt chữ.
   FAIL nếu: còn chồng lấn · thiếu số hoặc thiếu sao ở bản có điểm · xuất hiện giá trị >5 · nút chữ xuống dòng.
   CHUYỂN BA nếu: chỉ còn tranh chấp về thứ tự sắp xếp mặc định (spec im lặng).

5. Dạng dữ liệu phải phủ — M = 4:
   (1) TVV chưa có điểm  (2) TVV đã có điểm  (3) Chuyên gia (loại khác)  (4) bản ghi có >=2 lĩnh vực (tags "+N")
   Nguồn xác định M: bảng cột SCR-IV-01 #24 (2 trạng thái điểm) + #20 Loại + #22 Lĩnh vực tags.

── SỬA ĐỔI #1 — 2026-08-05 22:1x (ghi TRƯỚC khi đo, chưa mở màn của case trên env mới) ──
Sửa gì: đổi "Môi trường verify" từ https://htpldn-uat.ospgroup.vn (bản dựng V1.0.7)
        sang env dev https://18.143.165.120.nip.io (bản dựng V1.0.8, bundle index-D-YMo5bZ.js).
Vì sao: user báo dev vừa build bản fix mới lên env dev; env đối tác chưa nhận bản đó.
        Đã kiểm chứng: dev = 1.0.8 > đối tác = 1.0.7.
KHÔNG sửa: mục 1 (đối tác phản ánh), 2 (đặc tả), 4 (PASS/FAIL), 5 (M dạng) — giữ nguyên như 21:51.
Hệ quả phải ghi trong verdict: Pass ở đây là PASS TẠM cho bản 1.0.8 trên env dev;
        chưa chứng minh đối tác mở env nghiệm thu (1.0.7) sẽ hết lỗi. Phải re-verify khi 1.0.8 lên env đối tác.
Tài khoản: bộ tài khoản env dev (xem input/input.md phần trên) — khác bộ env đối tác.
