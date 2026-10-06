✅ Đã hết lỗi — Pass.

Đo lại trên môi trường https://18.143.165.120.nip.io, bản dựng V1.0.9 (bó mã index-D4Buvu4S.js, bản cập nhật lúc 19:23 ngày 06/08/2026 giờ máy chủ), lúc 02:30–02:36 ngày 07/08/2026. Tài khoản Cán bộ Nghiệp vụ Trung ương cbnv_tw_02 (CB_NV_TW, đơn vị BTP · TW) — đúng vai trò đặc tả quy định cho chức năng này (srs-fr-03-dao-tao.md:751 "Tác nhân: CB NV / CB PD"). Đã tải lại trang và đăng nhập lại trước khi đo.

Không có ảnh/video bằng chứng của bên nghiệm thu cho case này (ô Ảnh/video và ô Kết quả thực tế đều trống). Vì các bước của case chỉ gồm 2 thao tác và không cần dữ liệu đặc biệt, chúng tôi tự dựng lại điều kiện và ghi rõ dưới đây để có thể kiểm chứng lại.

Tiền đề đã tái hiện: màn Đào tạo, tập huấn → Kho tài liệu / Bài giảng (địa chỉ /dao-tao/bai-giang/danh-sach), để trống toàn bộ thanh lọc. Đã xác nhận "không có điều kiện lọc" bằng chính tham số mà màn gửi lên máy chủ khi tải danh sách — chỉ có tham số phân trang, không có tham số lọc nào. Lưu ý: màn có hiển thị chữ "Bộ lọc nâng cao (2)" ngay khi vào, nhưng đó chỉ là số ô lọc trong khung nâng cao, không phải bộ lọc đang được áp dụng. Tổng số bản ghi trong phạm vi tài khoản tại thời điểm đo: 11.

VẾ 1 — Màn hình có chức năng Xuất Excel: ĐẠT.
Đặc tả srs-fr-03-dao-tao.md:1952 (màn SCR-III-03, Thành phần 2 — Tiêu đề + Hành động chính) ghi: 'Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)'; quy tắc BR-DATA-06 tại srs-v3.5.md:5570 ghi "Mọi danh sách có tính năng xuất Excel", cột Áp dụng ghi "Toàn bộ CRUD list" và cột Ngoại lệ chỉ trừ Báo cáo nhóm IX. Trên bản dựng đo, nút "Xuất Excel" có mặt ở hàng hành động chính của màn, hiển thị bình thường và không bị vô hiệu hóa. Chúng tôi không kết luận bằng mắt qua ảnh mà đã liệt kê toàn bộ nút/liên kết trong vùng tiêu đề và thanh công cụ kèm cả nhãn ẩn, để chắc chắn không bỏ sót nút chỉ có biểu tượng; đối chiếu thêm với danh sách chức năng máy chủ công bố thì chức năng xuất của màn này có tồn tại. Ghi chú phân biệt: 4 biểu tượng ở cột "Thao tác" của từng dòng (xem · tải về · sửa · xóa) là thao tác trên một bài giảng theo srs-fr-03-dao-tao.md:1974, không phải chức năng xuất danh sách — hai thứ khác nhau.

Như vậy triệu chứng đã ghi trên phiếu ("Màn hình không có nút chức năng") không tái hiện được trên bản dựng đo.

VẾ 2 — Không đặt điều kiện lọc thì tệp xuất phải chứa toàn bộ danh sách: ĐẠT.
Bấm nút "Xuất Excel" trực tiếp trên giao diện (một lần), hệ thống báo "Xuất dữ liệu thành công." và tải về tệp DanhSachBaiGiang_20260807_0234.xlsx. Chúng tôi không dừng ở chỗ "tải được tệp" mà đã mở tệp ra đọc nội dung: tệp có 1 trang tính tên "Bài giảng", 12 dòng, trong đó 1 dòng tiêu đề và 11 dòng dữ liệu. Đối chiếu từng bản ghi với danh sách trên màn: trùng khớp hoàn toàn 11/11, không thừa không thiếu bản ghi nào.

Số đo quyết định: 11 dòng dữ liệu trong tệp = 11 bản ghi của danh sách.

Để phép đo phân biệt được "xuất toàn bộ danh sách" với "chỉ xuất trang đang xem" — vì nếu để mặc định 20 dòng/trang thì cả 11 bản ghi nằm gọn trong một trang, không tách bạch được — chúng tôi đã hạ phân trang xuống 10 dòng/trang (tùy chọn hợp lệ của chính màn theo srs-fr-03-dao-tao.md:1976) rồi mới bấm xuất. Khi đó trang đang xem chỉ hiển thị 10 dòng, tổng vẫn 11, danh sách chia làm 2 trang. Tệp xuất ra vẫn có đủ 11 dòng, bao gồm cả bản ghi thứ 11 ("QA UAT Bài giảng Test QLKTLBG_08") vốn nằm ở trang 2 và không hiển thị trên trang đang xem. Đây là bằng chứng tệp xuất theo toàn bộ danh sách chứ không cắt theo trang, đúng câu chữ "xuất danh sách theo bộ lọc hiện tại" tại srs-fr-03-dao-tao.md:1952.

Không tạo, sửa hay xóa bản ghi nào trong quá trình đo; toàn bộ 11 bản ghi là dữ liệu có sẵn. Nhật ký trình duyệt không có lỗi nào.

Phạm vi kết luận: đặc tả srs-fr-03-dao-tao.md:1981 quy định danh sách lọc theo đơn vị sở hữu, nên "toàn bộ danh sách" ở đây được hiểu là toàn bộ trong phạm vi dữ liệu của tài khoản đang dùng. Giới hạn 10.000 dòng của BR-DATA-06 chưa được kiểm vì tổng chỉ có 11 bản ghi, và giới hạn này cũng không nằm trong nội dung case. Đặc tả nhóm III không quy định danh mục cột của tệp xuất cho màn này nên chúng tôi không chấm theo bộ cột; xin ghi lại để tham khảo, tệp gồm các cột: Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo · Ngày tạo · Mô tả.

Lưu ý về cách hiểu kết quả: chúng tôi không có ảnh hiện trạng trước khi sửa nên chỉ khẳng định được hiện trạng hiện nay đúng đặc tả, không suy đoán về việc thao tác sửa nào đã tạo ra kết quả này.

Ảnh bằng chứng: https://drive.google.com/file/d/1fRdfaHZHJ_NVWw65ZmHblh8RYTe0AWeb/view?usp=drivesdk (màn Kho tài liệu / Bài giảng có nút "Xuất Excel" ở hàng hành động chính, thanh lọc để trống) · https://drive.google.com/file/d/1gaQyfOaaEAG1yqhdwDUGo-rXVCHH3gNt/view?usp=drivesdk (dòng "Hiển thị 1-10 / 11 kết quả" với 2 trang, ở thời điểm bấm xuất — cho thấy trang đang xem chỉ có 10 dòng trong khi tệp xuất ra 11 dòng).

Kết quả trên chỉ có hiệu lực cho môi trường https://18.143.165.120.nip.io bản dựng V1.0.9 (bó mã index-D4Buvu4S.js) tại thời điểm đo; đợt kiểm trước của bên nghiệm thu thực hiện trên htpldn-uat.ospgroup.vn bản V1.0.

Đề nghị BA (không chặn bàn giao, không ảnh hưởng kết quả case): bảng tổng quan quy tắc tại srs-fr-03-dao-tao.md:2243 liệt kê BR-DATA-06 áp dụng cho FR-III-01, FR-III-05, FR-III-06, FR-III-14 mà chưa có FR-III-07 và FR-III-08, trong khi phần đặc tả màn SCR-III-03 tại :1952 lại dẫn thẳng BR-DATA-06. Đề nghị bổ sung cho khớp để vòng nghiệm thu sau không phải tra chéo.
