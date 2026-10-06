Mã case: VVDTN_04        Vòng: 1 (dev Fixed; TKM retest 31/7 vẫn báo thiếu biểu đồ tròn)
Thời điểm viết: 2026-08-05 21:51
Môi trường verify: https://htpldn-uat.ospgroup.vn

1. Đối tác phản ánh: "Báo cáo thống kê" -> nhập tiêu chí -> Xem báo cáo:
   (a) không hiển thị biểu đồ TRÒN theo lĩnh vực
   (b) bảng tổng hợp thiếu các cột "Theo kênh", "Theo lĩnh vực"
   Bằng chứng VVDTN_04.webm (15/07 16:31, tài khoản QTHT — TÀI KHOẢN QUẢN TRỊ):
   URL /bao-cao?loai=vu-viec-tiep-nhan&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=...0001
   Frame cuối: có biểu đồ cột (Trực tiếp/Điện thoại) + biểu đồ đường "Số lượng" + bảng "Kênh tiếp nhận | Số lượng" (Trực tiếp 26).

2. Đặc tả nói gì — srs-fr-11-bao-cao.md:209-220 (FR-IX-02 / UC125) và :1065:
   ':213-217  1 tong_vu_viec | 2 theo_kenh[] | 3 theo_linh_vuc[] | 4 theo_don_vi[] | 5 theo_ky[]  — điều kiện "Luôn"'
   ':220  Given CB chọn kỳ Tháng When tạo BC Then hiển thị tổng VV tiếp nhận, phân theo kênh + lĩnh vực'
   ':1065 | Vụ việc | UC125 | BC Vụ việc đã tiếp nhận | Kênh tiếp nhận, Lĩnh vực PL | Bar + Trend |'
   -> (a) BIỂU ĐỒ TRÒN KHÔNG CÓ CĂN CỨ SPEC. UC125 quy định "Bar + Trend"; Donut chỉ gán cho UC124/UC127/UC131.
          Nếu app hiện Bar + Trend thì là ĐÚNG -> kỳ vọng đối tác sai.
   -> (b) theo_kenh[] và theo_linh_vuc[] điều kiện "Luôn" -> báo cáo PHẢI phân rã theo cả 2 chiều. Thiếu = lỗi.
   IM LẶNG: nhãn cột phải viết đúng chữ "Theo kênh"/"Theo lĩnh vực"; trình bày 1 bảng hay nhiều bảng.
   -> Chấm theo BẢN CHẤT (có phân rã theo kênh và theo lĩnh vực không), KHÔNG prescribe tên cột.

3. Precondition: tài khoản CB NV (KHÔNG dùng QTHT để ra verdict — quyền rộng che lỗi phân quyền;
   QTHT chỉ để đối chiếu). Màn /bao-cao, loại "vu-viec-tiep-nhan", kỳ NAM 2026, có >=1 vụ việc trong kỳ.
   CẢNH BÁO CACHE: báo cáo có cache server-side — kiểm "Thời điểm tạo"/ngayTaoBc; đổi denNgay 1 ngày
   để lấy cache key mới trước khi kết luận thiếu dữ liệu.

4. PASS khi (đủ cả 3):
   - Báo cáo hiển thị tổng số vụ việc tiếp nhận trong kỳ.
   - Có phân rã theo KÊNH TIẾP NHẬN (mỗi kênh + số lượng) — dù trình bày bằng bảng hay biểu đồ.
   - Có phân rã theo LĨNH VỰC PHÁP LUẬT (mỗi lĩnh vực + số lượng).
   FAIL nếu: thiếu phân rã theo kênh HOẶC thiếu phân rã theo lĩnh vực (dù đã loại trừ cache).
   KHÔNG chấm FAIL vì: không có biểu đồ tròn (spec đòi Bar + Trend) · nhãn cột không đúng chữ.
   -> Vế (a) của phiếu: verdict "không phải lỗi", giải thích cho đối tác.

5. Dạng dữ liệu phải phủ — M = 2 chiều bắt buộc (kênh, lĩnh vực), mỗi chiều >=2 giá trị khác nhau
   để chứng minh có phân rã thật (vd >=2 kênh tiếp nhận, >=2 lĩnh vực).
   Nguồn xác định M: :213-217 khai 4 chiều điều kiện "Luôn"; case này tranh chấp 2 chiều kênh + lĩnh vực.

── SỬA ĐỔI #1 — 2026-08-05 22:1x (ghi TRƯỚC khi đo, chưa mở màn của case trên env mới) ──
Sửa gì: đổi "Môi trường verify" từ https://htpldn-uat.ospgroup.vn (bản dựng V1.0.7)
        sang env dev https://18.143.165.120.nip.io (bản dựng V1.0.8, bundle index-D-YMo5bZ.js).
Vì sao: user báo dev vừa build bản fix mới lên env dev; env đối tác chưa nhận bản đó.
        Đã kiểm chứng: dev = 1.0.8 > đối tác = 1.0.7.
KHÔNG sửa: mục 1 (đối tác phản ánh), 2 (đặc tả), 4 (PASS/FAIL), 5 (M dạng) — giữ nguyên như 21:51.
Hệ quả phải ghi trong verdict: Pass ở đây là PASS TẠM cho bản 1.0.8 trên env dev;
        chưa chứng minh đối tác mở env nghiệm thu (1.0.7) sẽ hết lỗi. Phải re-verify khi 1.0.8 lên env đối tác.
Tài khoản: bộ tài khoản env dev (xem input/input.md phần trên) — khác bộ env đối tác.
