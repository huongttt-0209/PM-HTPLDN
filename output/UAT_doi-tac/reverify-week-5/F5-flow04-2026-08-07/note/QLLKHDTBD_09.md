⚠️ Cần BA xác nhận — phần lọc đã đạt, phần danh mục cột tệp xuất xin ý kiến BA.

Đo trên môi trường https://18.143.165.120.nip.io, bản dựng bó mã index-D4Buvu4S.js (bản cập nhật lúc 19:23 ngày 06/08/2026 giờ máy chủ, thẻ phiên bản W/"6a74df15-428"), lúc 03:00–03:07 ngày 07/08/2026. Tài khoản cbnv_tw_02 — Cán bộ Nghiệp vụ Trung ương (CB_NV_TW), đơn vị BTP · TW, đúng vai trò như trong tư liệu nghiệm thu. Đã tải lại trang trước khi đo để chắc chắn không chạy trên bản cũ còn lưu trong trình duyệt. Chuỗi phiên bản hiển thị ở chân thanh điều hướng ghi V1.0.9; chúng tôi đối chiếu bản dựng bằng thẻ phiên bản và bó mã nêu trên chứ không dựa vào chuỗi này.

Màn đo: Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách (/dao-tao/ke-hoach/danh-sach).

Tiền đề: khi KHÔNG đặt bộ lọc, danh sách có 14 bản ghi trong phạm vi dữ liệu của tài khoản. Con số 14 lấy từ tổng số bản ghi máy chủ trả về, không đếm bằng mắt, và được kiểm chéo bằng số trên các thẻ trạng thái (Nháp 7 + Chờ duyệt 2 + Đã duyệt 4 + Đã công khai 1 + Từ chối 0 = 14).

── PHẦN 1 — Xuất Excel theo điều kiện lọc hiện tại: ĐÃ ĐẠT ──

Chúng tôi đo hai bộ lọc, mỗi lần đều bấm nút "Xuất Excel" trực tiếp trên giao diện (không gọi lệnh thay thao tác), và không dừng ở chỗ "tải được tệp" mà mở tệp ra đếm nội dung bên trong.

Lần 1 — lọc theo Trạng thái = "Đã duyệt": màn còn 4 kết quả (trên tổng 14). Hệ thống báo "Xuất Excel thành công" và tải về tệp ke-hoach-dao-tao-1786046602595.xlsx. Mở tệp: đúng 4 dòng dữ liệu, và 4 mã kế hoạch trong tệp trùng khít 4 mã trên màn (KH-20260803-0001, KHDT-QAW7-01, KHDT-2026-001, KHDT-SEED-0001); cột Trạng thái của cả 4 dòng đều là "Đã duyệt".

Lần 2 — lọc Từ ngày 01/07/2026 đến Đến ngày 31/07/2026, đúng bộ lọc đã dùng trong tư liệu nghiệm thu: màn còn 1 kết quả. Tệp tải về ke-hoach-dao-tao-1786046777916.xlsx có đúng 1 dòng dữ liệu, là bản ghi KH-20260803-0003 — đúng bản ghi duy nhất trên màn.

Số đo quyết định: 4 dòng khi màn 4 kết quả, và 1 dòng khi màn 1 kết quả, trong khi danh sách chưa lọc có 14 bản ghi. Nếu chức năng xuất bỏ qua bộ lọc thì cả hai tệp đã phải có 14 dòng. Ngoài ra, nội dung màn gửi lên chức năng xuất có mang đúng các tham số đang lọc (trạng thái ở lần 1; cả hai mốc ngày ở lần 2), cho thấy tệp được tạo theo bộ lọc hiện tại. Như vậy triệu chứng đã ghi trên phiếu — "Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách" — không tái hiện trên bản dựng đo.

Căn cứ đặc tả cho phần này: srs-v3.5.md:5570 quy định "Export Excel: Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10.000 rows/file", áp dụng cho "Toàn bộ CRUD list"; srs-fr-03-dao-tao.md:2243 xác nhận quy tắc này áp cho FR-III-14; srs-fr-03-dao-tao.md:1775 ghi 'Nút "Xuất Excel" (phụ): xuất danh sách KH theo bộ lọc, tối đa 10.000 dòng'; srs-fr-03-dao-tao.md:1175 ghi bước xử lý "Lấy danh sách theo filter, tối đa 10.000 dòng".

Phạm vi hiệu lực của phần 1: cả hai lần đo đều có số kết quả sau lọc (4 và 1) nhỏ hơn cỡ trang đang đặt (20 dòng/trang), và tổng dữ liệu (14) cũng nhỏ hơn cỡ trang, nên phép đo này khẳng định tệp bám theo bộ lọc, nhưng chưa tách bạch được trường hợp số kết quả sau lọc lớn hơn một trang. Chúng tôi nêu rõ để không ai hiểu kết quả rộng hơn thực tế.

── PHẦN 2 — Trường "Người tạo", "Ngày tạo" trong tệp xuất: XIN Ý KIẾN BA ──

Hiện trạng đo được: hàng tiêu đề của tệp xuất, giống hệt nhau ở cả hai tệp nêu trên, nguyên văn gồm 7 cột:

Mã KH | Tên kế hoạch | Năm | Từ ngày | Đến ngày | Ngân sách (VNĐ) | Trạng thái

Tệp KHÔNG có cột "Người tạo" và KHÔNG có cột "Ngày tạo". Chúng tôi không so tên cột theo chuỗi chữ cứng mà đã đối chiếu theo ý nghĩa, có xét các cách gọi khác như Người lập, Ngày lập, Thời điểm tạo, Cán bộ tạo: không cột nào trong 7 cột trên chứa họ tên người, và hai cột ngày duy nhất là thời gian hiệu lực của kế hoạch chứ không phải ngày lập bản ghi. Ví dụ quyết định: bản ghi KH-20260803-0003 trong tệp có Từ ngày 05/07/2026 và Đến ngày 25/07/2026, trong khi Ngày tạo của chính bản ghi đó trên màn là 03/08/2026 — ba giá trị khác nhau.

Xin lưu ý một điểm để tránh hiểu nhầm phạm vi: BẢNG HIỂN THỊ TRÊN MÀN đã có đủ hai cột "Người tạo" và "Ngày tạo" kèm dữ liệu thật (ví dụ "CB Nghiệp vụ - Trung ương" và "03/08/2026"), đúng như đặc tả màn quy định. Khoảng trống chỉ nằm ở tệp Excel xuất ra.

CẦN BA CONFIRM: đối tác kỳ vọng tệp Excel xuất từ màn Kế hoạch đào tạo năm phải có trường "Người tạo" và "Ngày tạo"; SRS quy định hai cột này thuộc BẢNG HIỂN THỊ TRÊN MÀN (srs-fr-03-dao-tao.md:1795-1796) nhưng không có điều khoản nào quy định danh mục cột của TỆP EXCEL XUẤT RA — phần xuất Excel chỉ ràng buộc phạm vi dữ liệu ("theo bộ lọc hiện tại", tối đa 10.000 dòng) tại srs-v3.5.md:5570 và srs-fr-03-dao-tao.md:1775, :1175; đồng thời mục "Outputs — Danh sách" của FR-III-14 tại srs-fr-03-dao-tao.md:1189-1200 lại KHÔNG có hai trường này, tức bản thân đặc tả đang có hai định nghĩa khác nhau cho chữ "danh sách"; web/dev hiện tại xuất tệp 7 cột không có "Người tạo" và "Ngày tạo".

Mục đích của việc xin ý kiến là BỔ SUNG NỘI DUNG NÀY VÀO ĐẶC TẢ để các vòng nghiệm thu sau có căn cứ chấm thống nhất — KHÔNG phải để chặn bàn giao. Xin lưu ý thêm: đây không phải lỗi mới phát sinh từ bản sửa lần này; tư liệu nghiệm thu vòng đầu (25/07) cho thấy tệp xuất đã gồm đúng 7 cột như trên ngay từ thời điểm đó.

Ba câu hỏi cụ thể xin BA quyết:

1. Tệp Excel xuất từ màn Kế hoạch đào tạo năm phải gồm đúng những cột nào — lấy theo bảng hiển thị trên màn (srs-fr-03-dao-tao.md:1786-1796, có "Người tạo" và "Ngày tạo"), hay theo mục "Outputs — Danh sách" của FR-III-14 (srs-fr-03-dao-tao.md:1189-1200, không có hai cột này)? Đề nghị bổ sung một bảng "Outputs — Tệp Xuất Excel" vào FR-III-14, theo đúng cách đặc tả đã làm ở FR-III-05 (srs-fr-03-dao-tao.md:609-625).

2. Nếu chốt theo bảng trên màn: cột "Số chương trình" (srs-fr-03-dao-tao.md:1793) có phải nằm trong tệp xuất không? Hiện tệp xuất cũng không có cột này, nên câu trả lời sẽ quyết định phạm vi cần chỉnh rộng hơn hai cột mà bên nghiệm thu nêu.

3. Cột "Mã KH" có trong tệp xuất thực tế nhưng không có trong cả hai bảng cột nói trên của đặc tả. Đây là cột được chấp nhận và cần bổ sung vào đặc tả, hay là cột thừa cần gỡ?

── Ghi chú chung ──

Không tạo, sửa hay xóa bản ghi nào trong quá trình đo; thao tác chỉ gồm chọn thẻ trạng thái, nhập hai ô ngày và bấm nút xuất. Nhật ký trình duyệt không ghi nhận lỗi nào. Mỗi lần bấm nút, hệ thống hiện đúng một thông báo "Xuất Excel thành công", không có hiện tượng thông báo lặp.

Chúng tôi không có ảnh hiện trạng trước khi sửa nên chỉ khẳng định được hiện trạng hiện nay so với đặc tả, không suy đoán về việc thao tác sửa nào đã tạo ra kết quả này. Kết quả trên chỉ có hiệu lực cho môi trường và bản dựng đã nêu tại thời điểm đo.

Hai tệp Excel đã tải về được giữ lại để đối chiếu: ke-hoach-dao-tao-1786046602595.xlsx (mã kiểm tra sha256 5cf082c473357c8b608bc8e62f3c246a4717fc9210f7494d8eefb1594b58bcae) và ke-hoach-dao-tao-1786046777916.xlsx (sha256 62e1eb2dbb8ee0dceadc874f2e09cce4c8d46b57c00c9894236270850bff8fad).

Ảnh bằng chứng:
- https://drive.google.com/file/d/1sAbSLkWYmRTV693XojhcvTIvDX3_Q8d2/view?usp=drivesdk (màn sau khi lọc Trạng thái "Đã duyệt": chân bảng "Hiển thị 1-4 / 4 kết quả", thẻ "Tất cả 14", nút "Xuất Excel" có mặt)
- https://drive.google.com/file/d/1ofW-UmqNK2SdSnu8qD6DcKDzejK_ikTx/view?usp=drivesdk (màn sau khi lọc Từ ngày 01/07/2026 – Đến ngày 31/07/2026: chân bảng "Hiển thị 1-1 / 1 kết quả")
- https://drive.google.com/file/d/1LTwZarKWmdDpMIhmGgCPJJwUiqI_It2F/view?usp=drivesdk (bảng trên màn đã cuộn sang phải, thấy rõ hai cột "Người tạo" và "Ngày tạo" có dữ liệu)
