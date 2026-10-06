Mã case: XNTGHTVV_03     Vòng: 2
Thời điểm viết: 2026-08-05 21:51
Môi trường verify: https://htpldn-uat.ospgroup.vn

1. Đối tác phản ánh (v2, webm 30/07 09:36, V1.0.2):
   "Cán bộ nghiệp vụ phụ trách không nhận được thông báo kèm lý do từ chối."
   Bằng chứng: mở panel Thông báo bằng tài khoản CB_NV_TW -> chỉ có 3 tin "Tài khoản vừa đăng nhập ở nơi khác",
   1 tin CT HTPL, 1 tin câu hỏi quá hạn. Frame đầu: tài khoản huongcg (TVV·CG), 6 vụ việc, tab "Từ chối" trống.
   GAP CHƯA ĐÓNG TỪ BẰNG CHỨNG: không biết vụ việc nào bị từ chối, và ai là CB NV phụ trách vụ việc đó
   -> CB_NV_TW trong video có thể KHÔNG phải người đáng lẽ nhận thông báo.

2. Đặc tả nói gì — srs-fr-05-vu-viec.md:825 · :834 · :2480 (BR-NOTIF-01) · :2292:
   ":825  | 5 | Gửi thông báo CB NV |"     ":834 - CB NV nhận thông báo"
   ":2480 Mọi sự kiện workflow (... từ chối ...) đều gửi thông báo cho người liên quan qua 2 kênh:
          in-app (THONG_BAO) + email."
   -> Vế A "CB NV phụ trách phải nhận được thông báo khi bị từ chối" = CÓ CĂN CỨ, bắt buộc, 2 kênh.
   IM LẶNG: nội dung thông báo có bắt buộc chứa lý do từ chối hay không (:825 không có template;
   transition :2292 lại KHÔNG liệt kê gửi thông báo -> 2 vị trí spec không đồng nhất).
   -> Vế B "kèm lý do" = CHUYỂN BA, không log thẳng là sai spec.

3. Precondition: cần 2 tài khoản — (i) TVV/CG được phân công 1 vụ việc ở "Đã phân công";
   (ii) CB NV phụ trách chính vụ việc đó (phải xác định được, không lấy CB bất kỳ).
   Phải kiểm CẢ 2 kênh: in-app (chuông) + email (MailHog của env đối tác).

4. PASS khi (đủ cả 3):
   - TVV từ chối thành công, vụ việc chuyển "Đã phân công" -> "Đã tiếp nhận", bản ghi phân công lưu lý do.
   - Đúng CB NV phụ trách vụ việc đó nhận được thông báo in-app về sự kiện từ chối.
   - Có email tương ứng trong hộp thư của CB NV đó.
   FAIL nếu: từ chối lỗi/không đổi trạng thái · CB NV phụ trách không có thông báo in-app · không có email.
   CHUYỂN BA nếu: thông báo CÓ đến nhưng KHÔNG chứa lý do từ chối (spec im lặng vế nội dung).

5. Dạng dữ liệu phải phủ — M = 2 kênh nhận (in-app, email) x 1 luồng từ chối.
   Nguồn xác định M: BR-NOTIF-01 :2480 khai đích danh 2 kênh.

── SỬA ĐỔI #1 — 2026-08-05 22:1x (ghi TRƯỚC khi đo, chưa mở màn của case trên env mới) ──
Sửa gì: đổi "Môi trường verify" từ https://htpldn-uat.ospgroup.vn (bản dựng V1.0.7)
        sang env dev https://18.143.165.120.nip.io (bản dựng V1.0.8, bundle index-D-YMo5bZ.js).
Vì sao: user báo dev vừa build bản fix mới lên env dev; env đối tác chưa nhận bản đó.
        Đã kiểm chứng: dev = 1.0.8 > đối tác = 1.0.7.
KHÔNG sửa: mục 1 (đối tác phản ánh), 2 (đặc tả), 4 (PASS/FAIL), 5 (M dạng) — giữ nguyên như 21:51.
Hệ quả phải ghi trong verdict: Pass ở đây là PASS TẠM cho bản 1.0.8 trên env dev;
        chưa chứng minh đối tác mở env nghiệm thu (1.0.7) sẽ hết lỗi. Phải re-verify khi 1.0.8 lên env đối tác.
Tài khoản: bộ tài khoản env dev (xem input/input.md phần trên) — khác bộ env đối tác.
