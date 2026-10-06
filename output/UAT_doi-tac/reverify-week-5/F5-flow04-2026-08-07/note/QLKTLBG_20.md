✅ Đã hết lỗi — Pass.

Đo lại trên môi trường https://18.143.165.120.nip.io, bản dựng V1.0.9 (bó mã index-D4Buvu4S.js, bản cập nhật lúc 19:23 ngày 06/08/2026 giờ máy chủ), lúc 02:44–02:49 ngày 07/08/2026. Tài khoản Cán bộ Nghiệp vụ Trung ương cbnv_tw_02 (CB_NV_TW, đơn vị BTP · TW) — đúng vai trò đặc tả quy định cho chức năng này (srs-fr-03-dao-tao.md:751 "Tác nhân: CB NV / CB PD"). Đã tải lại trang trước khi đo để chắc chắn không chạy trên bản cũ còn lưu trong trình duyệt.

Không có ảnh/video bằng chứng của bên nghiệm thu cho case này (ô Ảnh/video và ô Kết quả thực tế đều trống). Vì các bước của case chỉ gồm 2 thao tác và không cần dữ liệu đặc biệt, chúng tôi tự dựng lại điều kiện và ghi rõ dưới đây để có thể kiểm chứng lại.

Tiền đề đã tái hiện: màn Đào tạo, tập huấn → Kho tài liệu / Bài giảng (địa chỉ /dao-tao/bai-giang/danh-sach). Khi chưa lọc, danh sách có 11 bản ghi trong phạm vi tài khoản. Sau đó nhập vào ô "Tìm theo tên bài giảng" (srs-fr-03-dao-tao.md:1955) chuỗi vô nghĩa ZZQAKHONGTONTAI20260807 rồi bấm "Tìm kiếm" để tạo đúng tình huống "điều kiện lọc không có kết quả". Đã xác nhận màn thật sự về 0 bản ghi TRƯỚC khi bấm xuất, bằng 6 chiều cùng lúc: tổng số bản ghi máy chủ trả về = 0, số trang = 0, danh sách trả về rỗng, bảng không còn dòng nào, màn hiện chữ "Không có bài giảng nào phù hợp.", vùng phân trang biến mất. Lưu ý: màn có hiển thị chữ "Bộ lọc nâng cao (2)" ngay khi vào, nhưng đó chỉ là số ô lọc trong khung nâng cao, không phải bộ lọc đang được áp dụng — đã kiểm bằng chính tham số màn gửi lên máy chủ khi tải danh sách.

VẾ 1 — Màn hình có chức năng Xuất Excel: ĐẠT.
Đặc tả srs-fr-03-dao-tao.md:1952 (màn SCR-III-03, Thành phần 2 — Tiêu đề + Hành động chính) ghi: 'Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)'; quy tắc BR-DATA-06 tại srs-v3.5.md:5570 ghi "Mọi danh sách có tính năng xuất Excel", cột Áp dụng ghi "Toàn bộ CRUD list" và cột Ngoại lệ chỉ trừ Báo cáo nhóm IX. Trên bản dựng đo, nút "Xuất Excel" có mặt ở hàng hành động chính của màn, hiển thị bình thường và không bị vô hiệu hóa. Chúng tôi không kết luận bằng mắt qua ảnh mà đã liệt kê toàn bộ nút và liên kết trong vùng tiêu đề cùng thanh công cụ, kèm cả nhãn ẩn, để chắc chắn không bỏ sót nút chỉ có biểu tượng; đối chiếu thêm với danh sách chức năng máy chủ công bố thì chức năng xuất của màn này có tồn tại. Ghi chú phân biệt: các biểu tượng ở cột "Thao tác" của từng dòng (xem · tải về · sửa · xóa) là thao tác trên một bài giảng theo srs-fr-03-dao-tao.md:1974, không phải chức năng xuất danh sách — hai thứ khác nhau; ở tình huống này bảng rỗng nên cột đó cũng không hiện.

Như vậy triệu chứng đã ghi trên phiếu ("Màn hình không có nút chức năng") không tái hiện được trên bản dựng đo.

VẾ 2 — Khi điều kiện lọc không có kết quả: ĐẠT.
Kỳ vọng ghi trên phiếu là "Hệ thống xuất danh sách rỗng HOẶC hiển thị thông báo không có dữ liệu" — chỉ cần một trong hai vế xảy ra là đạt. Bấm nút "Xuất Excel" trực tiếp trên giao diện đúng một lần, hệ thống báo "Xuất dữ liệu thành công." và tải về tệp DanhSachBaiGiang_20260807_0248.xlsx. Chúng tôi không dừng ở chỗ "tải được tệp" mà đã mở tệp ra đọc nội dung: tệp có 1 trang tính tên "Bài giảng", tổng cộng đúng 1 dòng và đó là dòng tiêu đề — tức 0 dòng dữ liệu.

Số đo quyết định: 0 dòng dữ liệu trong tệp, trong khi danh sách chưa lọc có 11 bản ghi.

Đây là điểm dễ nhầm nhất của case nên chúng tôi kiểm bằng ba đường độc lập, cả ba đều cho kết quả 0 và khớp nhau: (1) máy chủ trả tổng số bản ghi khớp bộ lọc = 0 khi tải danh sách; (2) phản hồi của chính lời gọi xuất tự khai số bản ghi đã xuất = 0 và tổng khớp bộ lọc = 0; (3) mở tệp đếm được 0 dòng dữ liệu. Ngoài ra, nội dung màn gửi lên chức năng xuất có kèm đúng từ khóa đang lọc, cho thấy tệp được tạo theo bộ lọc hiện tại chứ không bỏ qua bộ lọc. Nếu chức năng xuất bỏ qua bộ lọc thì tệp đã phải chứa 11 dòng — thực tế là 0. Như vậy hệ thống đi theo vế "xuất danh sách rỗng", đúng câu chữ "xuất danh sách theo bộ lọc hiện tại" tại srs-fr-03-dao-tao.md:1952 và "File xuất theo bộ lọc hiện tại" tại srs-v3.5.md:5570.

Về việc hệ thống báo "Xuất dữ liệu thành công." thay vì một thông báo dạng "không có dữ liệu": điều này không làm case không đạt, vì kỳ vọng trên phiếu là mệnh đề "hoặc" và vế "xuất danh sách rỗng" đã xảy ra đúng. Đặc tả nhóm III cũng không quy định câu chữ thông báo cho tình huống này ở màn Kho tài liệu / Bài giảng, nên chúng tôi không chấm theo câu chữ.

Không tạo, sửa hay xóa bản ghi nào trong quá trình đo; thao tác duy nhất là nhập từ khóa vào ô tìm kiếm. Nhật ký trình duyệt không có lỗi nào.

Phạm vi kết luận: đặc tả srs-fr-03-dao-tao.md:1981 quy định danh sách lọc theo đơn vị sở hữu, nên số 11 nêu trên là tổng trong phạm vi dữ liệu của tài khoản đang dùng. Giới hạn 10.000 dòng của BR-DATA-06 không thuộc nội dung case và cũng không chạm tới ở đây. Đặc tả nhóm III không quy định danh mục cột của tệp xuất cho màn này nên chúng tôi không chấm theo bộ cột; xin ghi lại để tham khảo, tệp gồm các cột: Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo · Ngày tạo · Mô tả.

Lưu ý về cách hiểu kết quả: chúng tôi không có ảnh hiện trạng trước khi sửa nên chỉ khẳng định được hiện trạng hiện nay đúng đặc tả, không suy đoán về việc thao tác sửa nào đã tạo ra kết quả này.

Ảnh bằng chứng: https://drive.google.com/file/d/1QHJN3tb_bKve_JAO2kVH9FVlpbHjyMKg/view?usp=drivesdk (màn Kho tài liệu / Bài giảng sau khi lọc bằng từ khóa ZZQAKHONGTONTAI20260807: bảng hiện "Không có bài giảng nào phù hợp.", đồng thời nút "Xuất Excel" vẫn có mặt ở hàng hành động chính). Tệp xuất ra đã được giữ lại để đối chiếu: DanhSachBaiGiang_20260807_0248.xlsx (mã kiểm tra sha256 a88970f2f31cd207f34042c75f12c202f8569030d2f7c08d8008549c9037d795).

Kết quả trên chỉ có hiệu lực cho môi trường https://18.143.165.120.nip.io bản dựng V1.0.9 (bó mã index-D4Buvu4S.js) tại thời điểm đo.

Đề nghị BA (không chặn bàn giao, không ảnh hưởng kết quả case): bảng tổng quan quy tắc tại srs-fr-03-dao-tao.md:2243 liệt kê BR-DATA-06 áp dụng cho FR-III-01, FR-III-05, FR-III-06, FR-III-14 mà chưa có FR-III-07 và FR-III-08, trong khi phần đặc tả màn SCR-III-03 tại :1952 lại dẫn thẳng BR-DATA-06. Đề nghị bổ sung cho khớp để vòng nghiệm thu sau không phải tra chéo.
