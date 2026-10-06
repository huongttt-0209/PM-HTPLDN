Mã case: KTHSYCHTPL_11   Vòng: 2 (dev đóng "Bỏ qua" + phản hồi "không phải lỗi theo BA-SRS")
Thời điểm viết: 2026-08-05 21:51
Môi trường verify: https://htpldn-uat.ospgroup.vn

1. Đối tác phản ánh:
   v1: bấm "Hoàn tất kiểm tra" chọn Đạt -> kỳ vọng "Đang kiểm tra" -> "Đã phân công"; màn không có nút
       "Hoàn tất kiểm tra" mà có "Kiểm tra lại".
   v2: "Hệ thống không chuyển trạng thái hồ sơ".
   Bằng chứng: v1 jpg 09/07 (VV-QA-R7-SLA-QHNT, CB_NV_DP, V1.0) · v2 webm 03/08 (VV-BTP-TW-20260514-002,
   CB_NV_TW, V1.0.4) -> HAI VỤ VIỆC KHÁC NHAU, hai vai trò khác nhau, hai bản dựng khác nhau.
   Cả hai vụ việc đều do QA seed (tên chứa "QA R7", "QA R23v3").

2. Đặc tả nói gì — srs-fr-05-vu-viec.md:541 · :564 · :1744 · :2288:
   ":541  Nếu DAT: vụ việc sẵn sàng phân công, giữ trạng thái DANG_KIEM_TRA — chỉ chuyển DA_PHAN_CONG
          khi CB NV phân công người/tổ chức xử lý qua FR-V.I-09"
   ":2288 DANG_KIEM_TRA | DA_PHAN_CONG | Đạt + chọn người/tổ chức xử lý"
   Changelog :22 — BA chốt riêng cho CHÍNH mã case này [UAT tuần 2, 2026-07-16].
   -> Kết luận Đạt GIỮ NGUYÊN DANG_KIEM_TRA là ĐÚNG SPEC. Kỳ vọng của đối tác đã bị BA bác từ tuần 2.
   IM LẶNG: không có (spec phủ đủ 3 nhánh Đạt / YCBS / Không đạt).

3. Precondition: tài khoản CB_NV cùng đơn vị sở hữu vụ việc · vụ việc ở trạng thái "Đang kiểm tra",
   đã đánh dấu đủ hạng mục kiểm tra · màn /vu-viec/{id}.

4. PASS khi (đủ cả 3):
   - Màn vụ việc ở "Đang kiểm tra" có thao tác hoàn tất kiểm tra với lựa chọn kết luận Đạt.
   - Chọn Đạt -> hệ thống chấp nhận, vụ việc VẪN ở "Đang kiểm tra" (đúng :541), có ghi người + thời điểm kiểm tra.
   - Tồn tại thao tác Phân công riêng, và chỉ khi chọn được người/tổ chức xử lý thì mới sang "Đã phân công".
   FAIL nếu: không có thao tác hoàn tất kiểm tra · chọn Đạt bị lỗi/không lưu · Đạt tự động nhảy "Đã phân công"
   (ngược spec) · không ghi người/thời điểm kiểm tra.
   LƯU Ý VERDICT: nếu PASS thì kết luận với đối tác là "không phải lỗi" (web đúng spec), KHÔNG phải "đã fix".

5. Dạng dữ liệu phải phủ — M = 1 (chỉ nhánh kết luận Đạt).
   Nhánh YCBS / Không đạt ngoài phạm vi case này.

── SỬA ĐỔI #1 — 2026-08-05 22:1x (ghi TRƯỚC khi đo, chưa mở màn của case trên env mới) ──
Sửa gì: đổi "Môi trường verify" từ https://htpldn-uat.ospgroup.vn (bản dựng V1.0.7)
        sang env dev https://18.143.165.120.nip.io (bản dựng V1.0.8, bundle index-D-YMo5bZ.js).
Vì sao: user báo dev vừa build bản fix mới lên env dev; env đối tác chưa nhận bản đó.
        Đã kiểm chứng: dev = 1.0.8 > đối tác = 1.0.7.
KHÔNG sửa: mục 1 (đối tác phản ánh), 2 (đặc tả), 4 (PASS/FAIL), 5 (M dạng) — giữ nguyên như 21:51.
Hệ quả phải ghi trong verdict: Pass ở đây là PASS TẠM cho bản 1.0.8 trên env dev;
        chưa chứng minh đối tác mở env nghiệm thu (1.0.7) sẽ hết lỗi. Phải re-verify khi 1.0.8 lên env đối tác.
Tài khoản: bộ tài khoản env dev (xem input/input.md phần trên) — khác bộ env đối tác.
