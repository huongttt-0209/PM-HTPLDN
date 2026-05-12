# Trả lời danh sách BA cần xác nhận - 4 module

**Nguồn rà soát:** `srs-v3.5/`  
**Danh sách câu hỏi đầu vào:** `/Users/linhsmac/Downloads/BA-CONFIRM-LIST-4-MODULE-2026-05-11.md`  
**Ngày lập:** 2026-05-11  
**Phạm vi:** Đào tạo, Biểu mẫu, CT HTPLDN, Quản trị hệ thống, các vấn đề dùng chung

## Kết luận tổng quan

SRS v3.5 đã chốt được một số điểm mà danh sách lỗi vẫn đang để mở: Khóa học dùng 9 trạng thái và khi từ chối thì quay về `DU_THAO`; Ngân hàng câu hỏi dùng 2 trạng thái `KICH_HOAT/VO_HIEU_HOA`; FR-VIII-26 chốt liên kết kích hoạt lần đầu là vĩnh viễn, còn liên kết đặt lại mật khẩu là 30 phút; Biểu mẫu và Thư mục biểu mẫu là dữ liệu sở hữu theo `don_vi_id`.

Các quyết định dưới đây đã được BA chốt trong lượt xác nhận ngày 2026-05-11. Với các mục không được nêu riêng trong phản hồi mới nhất, BA đồng ý theo đề xuất trong bản rà soát: QA/Dev sửa theo kết luận đã ghi, hoặc cập nhật SRS nếu phần đặc tả đang thiếu.

## P0 - Quyết định chặn phát hành

### #1 - Dữ liệu `congKhai=true` giữa CMS và chuyên trang

**Trả lời:** Cần tách rõ 2 kênh:

- **Trong CMS:** vẫn áp dụng phân quyền dữ liệu theo đơn vị (`BR-AUTH-08`). CB/NHT/DN nếu đăng nhập CMS mà gọi API CMS nội bộ thì không được tự động thấy dữ liệu đơn vị khác chỉ vì bản ghi có `cong_khai=true`, trừ khi SRS mở rõ quyền đọc public trong CMS.
- **Trên chuyên trang/Cổng PLQG:** đây là kênh/hệ thống khác, không áp dụng phân quyền CMS theo `don_vi_id` cho người đọc public. Chuyên trang chỉ cần lọc dữ liệu đủ điều kiện công khai: `cong_khai=true`, trạng thái publishable, chưa xóa, và không lộ dữ liệu nhạy cảm theo rule API.

Vì vậy cách gọi "bypass VPD" trong bug list dễ gây hiểu nhầm. Bản chất không phải là bỏ qua phân quyền CMS, mà là **API/kênh công khai phải lấy dữ liệu công khai theo điều kiện publish**, độc lập với phân quyền màn hình CMS.

**BA chốt:** Với FR-III-04/UC23, nếu DN/NHT đăng ký học viên qua chuyên trang thì luồng đọc danh sách khóa học phải đi qua API/chức năng public của chuyên trang, chỉ lọc theo `cong_khai=true` và trạng thái được phép đăng ký. Không dùng API danh sách CMS có VPD nội bộ rồi yêu cầu "bypass". Nếu hiện hệ thống đang dùng API CMS cho chuyên trang, Dev cần tách endpoint public hoặc bổ sung rõ rule cho endpoint đó.

### #2 - Lộ dữ liệu kế hoạch đào tạo năm xuyên đơn vị

**Trả lời:** SRS chốt rõ danh sách kế hoạch đào tạo năm phải lọc theo đơn vị. FR-III-14 Processing bước 2 ghi lấy danh sách `KE_HOACH_DAO_TAO` chưa xóa **thuộc đơn vị**; Acceptance Criteria ghi CB NV xem danh sách thì **chỉ thấy kế hoạch thuộc đơn vị mình**. BR-AUTH-03/04 chốt: BN/ĐP không thấy dữ liệu ngang cấp; TW thấy TW + BN + ĐP.

**Phạm vi đúng nên triển khai:**
- CB NV/PD TW: thấy toàn quốc, gồm TW + BN + ĐP.
- CB NV/PD BN: chỉ thấy BN mình.
- CB NV/PD ĐP: chỉ thấy ĐP mình.
- CB PD duyệt vẫn phải đúng đơn vị theo BR-AUTH-05, không duyệt hộ cấp dưới.

Nếu API đang trả 7 bản ghi từ 3 `donViId` cho BN/ĐP thì đó là lỗi lộ dữ liệu, không phải điểm mơ hồ của SRS.

### #3 - Máy trạng thái Khóa học 11 trạng thái hay thực tế ít hơn

**Trả lời:** SRS v3.5 đã chốt **9 trạng thái**, không phải 11 trạng thái và không có trạng thái `TU_CHOI` riêng cho Khóa học. Danh sách chuẩn là: `DU_THAO`, `CHO_DUYET`, `DA_DUYET`, `DA_CONG_KHAI`, `DANG_DIEN_RA`, `DA_KET_THUC`, `CHO_DUYET_KQ`, `HOAN_THANH`, `DA_HUY`. Khi CB PD từ chối khóa học: `CHO_DUYET -> DU_THAO`, đồng thời ghi `ly_do_tu_choi`, `thoi_gian_tu_choi`, `nguoi_tu_choi`.

**Quyết định nên dùng:** Cập nhật kiểm thử/tài liệu theo 9 trạng thái của SRS v3.5. Nếu BE/UI hiện chỉ có khoảng 6 trạng thái thì BE/UI đang thiếu các trạng thái sau duyệt, công khai, kết thúc, chờ duyệt kết quả, hoàn thành/hủy.

### #4 - Đề kiểm tra có cần quy trình duyệt hay không

**Trả lời:** SRS entity `DE_KIEM_TRA` hiện có 4 trạng thái: `DU_THAO`, `DA_PHAN_PHOI`, `HOAN_THANH`, `HUY`; FR-III-NEW-01/02/03 không mô tả quy trình trình duyệt/phê duyệt. Vì vậy không có căn cứ SRS để yêu cầu BE phải có `CHO_DUYET` / `DA_DUYET`.

**BA chốt:** Giữ Đề kiểm tra là luồng đơn giản, **không cần phê duyệt riêng**, vì đề kiểm tra là công cụ nội bộ của Khóa học, còn kết quả đào tạo đã được duyệt ở FR-III-18. Định nghĩa "chưa sử dụng" để xóa là: chưa `DA_PHAN_PHOI` **và** chưa có `KET_QUA_DAO_TAO.de_kiem_tra_id` liên kết. QA/Dev sửa kiểm thử và logic theo quyết định này.

### #5 - CT HTPLDN hoàn thành khi "0/0 đợt báo cáo"

**Trả lời:** SRS FR-XI-01 ghi điều kiện hoàn thành CT là "tất cả đợt báo cáo đã hoàn thành"; SM-KH-CTHTPL cũng ghi `DANG_THUC_HIEN -> HOAN_THANH` khi "Tất cả đợt BC hoàn thành". SRS **không nói CT bắt buộc phải có tối thiểu 1 đợt báo cáo**. Vì vậy trường hợp 0 đợt báo cáo là khoảng trống đặc tả.

**BA chốt:** Cho phép hoàn thành CT không có đợt báo cáo **nếu CT được đánh dấu không yêu cầu báo cáo định kỳ**; ngược lại, nếu CT thuộc chương trình phải báo cáo theo TT17 thì phải có tối thiểu 1 đợt báo cáo và tất cả đợt báo cáo phải đạt trạng thái cuối hợp lệ. SRS cần bổ sung điều kiện rõ:

`HOAN_THANH` được phép khi `(khong_yeu_cau_bao_cao = true) OR (COUNT(DOT_BAO_CAO) > 0 AND ALL DOT_BAO_CAO.trang_thai = DA_TONG_HOP)`.

Nếu không thêm cờ `khong_yeu_cau_bao_cao`, BE không nên trả thông báo "0/0 chưa DA_TONG_HOP"; thông báo đúng nên là "Chương trình chưa có đợt báo cáo để xác nhận hoàn thành".

## P1 - Đào tạo

### #6 - Tên trường lý do từ chối

**Trả lời:** SRS Đào tạo đang dùng bộ trường riêng `ly_do_tu_choi`, `thoi_gian_tu_choi`, `nguoi_tu_choi` cho Kế hoạch năm, CTĐT và Khóa học. BE dùng `ghiChuPheDuyet` là không khớp SRS.

**BA chốt:** Dùng trường từ chối riêng cho quy trình duyệt, không tái sử dụng `ghiChuPheDuyet`. API có thể nhận kiểu camelCase (`lyDoTuChoi`) nhưng DB/SRS giữ tên chuẩn snake_case.

### #7 - Tên trường từ chối kết quả đào tạo

**Trả lời:** SRS FR-III-18 chỉ nói từ chối kết quả thì Khóa học quay về `DA_KET_THUC`, đầu ra có `ly_do`; entity KHOA_HOC có `thoi_gian_duyet_kq`, `nguoi_duyet_kq` nhưng **chưa có bộ trường riêng cho từ chối kết quả**.

**BA chốt:** Bổ sung trường riêng cho từ chối kết quả: `ly_do_tu_choi_kq`, `thoi_gian_tu_choi_kq`, `nguoi_tu_choi_kq`. Không dùng chung `ly_do_tu_choi` của bước phê duyệt Khóa học vì đây là hai quy trình khác nhau.

### #8 - Lệch mã lỗi `ERR-CTDT-04` và `ERR-STATE-III-01-01`

**Trả lời:** SRS FR-III-01 đang khai báo mã lỗi theo nghiệp vụ (`ERR-CTDT-*`, `ERR-KH-PD-*`). Nếu BE trả `ERR-STATE-III-01-01` thì lệch quy ước hiện có trong SRS.

**BA chốt:** Giữ mã lỗi theo SRS dạng `ERR-CTDT-*` cho CTĐT. QA cập nhật kỳ vọng kiểm thử theo `ERR-CTDT-*`; Dev sửa BE nếu đang trả `ERR-STATE-III-01-01` cho cùng lỗi. Không để hai mã lỗi cho cùng một tình huống.

### #9 - Máy trạng thái Ngân hàng câu hỏi

**Trả lời:** SRS v3.5 đã chốt nguồn đúng là **2 trạng thái** `KICH_HOAT / VO_HIEU_HOA`. Dòng cũ `NHAP/CONG_KHAI/AN` là lỗi sao chép từ tài liệu cũ nếu còn xuất hiện ở tài liệu phụ.

### #10 - Liên kết Học viên với Tài khoản qua `taiKhoanId`

**Trả lời:** SRS FR-III-19 nói học viên xem kết quả "qua tài khoản doanh nghiệp / NHT đã đăng ký HV"; không bắt buộc mỗi HOC_VIEN phải có tài khoản 1:1. BR-AUTH-USERNAME-01 cũng không có quy ước sinh username cho học viên riêng.

**BA chốt:** `taiKhoanId` của HOC_VIEN là **không bắt buộc**, và học viên được quản lý dưới tài khoản DN/NHT đã đăng ký. Không tự tạo TAI_KHOAN cho từng học viên nếu SRS không mở actor "Học viên" độc lập.

### #11 - Điểm vào chính để tạo Học viên

**Trả lời:** FR-III-04/FR-III-03 định hướng đăng ký học viên qua DN/NHT/chuyên trang và duyệt đăng ký. Endpoint `POST /hoc-viens` nếu có trong BE nên xem là endpoint nội bộ/admin/seed, không phải luồng chính cho người dùng.

**BA chốt:** Luồng chính của sản phẩm là DN/NHT đăng ký học viên qua chuyên trang hoặc chức năng đăng ký đào tạo. CMS CB NV chỉ duyệt/quản lý danh sách theo phạm vi, không tạo học viên thay DN trừ khi có UC bổ sung.

### #12 - Hình thức Khóa học "Kết hợp"

**Trả lời:** SRS đang mâu thuẫn nhẹ: tổng quan ghi 2 hình thức `TRUC_TUYEN` và `TRUC_TIEP`; FR-III-22 lại nói buổi học có thể ghi đè hình thức từng buổi "nếu khóa kết hợp". Entity KHOA_HOC hiện chỉ CHECK `TRUC_TUYEN/TRUC_TIEP`.

**BA chốt:** Thêm enum `KET_HOP` cho `KHOA_HOC.hinh_thuc`. Khi `KET_HOP`, từng `LICH_HOC.hinh_thuc_buoi` bắt buộc chọn `TRUC_TUYEN` hoặc `TRUC_TIEP`.

### #13 - Ràng buộc sĩ số tối đa

**Trả lời:** SRS Inputs Khóa học ghi `so_luong_toi_da` không bắt buộc nhưng ràng buộc `>=1`; entity có CHECK `so_hoc_vien_toi_da > 0`. Hai phần này nghĩa là nếu có nhập thì phải >0, nhưng chưa rõ có bắt buộc trước khi trình duyệt hay không.

**BA chốt:** Bắt buộc `so_luong_toi_da >= 1` trước khi `DU_THAO -> CHO_DUYET`. Có thể cho phép bỏ trống khi lưu nháp, nhưng không cho gửi phê duyệt nếu thiếu.

### #14 - Hộp thoại "Công khai khóa học" thiếu trường công khai

**Trả lời:** SRS yêu cầu các trường công khai chung cho CTĐT/Khóa học: `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`, `cong_khai`. Màn hình Kế hoạch năm cũng mô tả hộp thoại công khai có mô tả, ảnh đại diện, file đính kèm.

**BA chốt:** FE phải bổ sung form công khai, không chỉ hiện xác nhận Có/Không. `thoi_gian_dang_tai` là trường hệ thống tự điền, người dùng không nhập.

### #15 - Quy tắc chống trùng lịch học

**Trả lời:** FR-III-22 đã có kiểm tra ngày trong khoảng khóa, giờ kết thúc > giờ bắt đầu, link/địa điểm theo hình thức, nhưng **chưa có quy tắc rõ về chống trùng lịch/thời gian**.

**BA chốt:** Bổ sung `BR-LH-CONFLICT-01` vào FR-III-22: không cho tạo/sửa buổi học trùng khoảng thời gian trong cùng Khóa học; nếu sau này quản lý lịch giảng viên thì mở rộng không cho trùng lịch theo giảng viên.

### #16 - Hợp đồng API tiếp nhận đăng ký đào tạo/học viên từ Cổng PLQG

**Trả lời:** SRS FR-16 hiện có 18 API cung cấp dữ liệu ra ngoài và 1 API tiếp nhận hỏi đáp; `danh-sach-api.md` liệt kê 8 API tiếp nhận từ hệ thống ngoài nhưng không có `dang-ky-dao-taos/inbound` hay `hoc-viens/inbound`. Đào tạo hiện chỉ có API chia sẻ/tìm kiếm khóa đào tạo FR-XII-03/04.

**BA chốt:** DN/NHT đăng ký đào tạo từ Cổng PLQG là **yêu cầu sản phẩm**. SRS đang thiếu API tiếp nhận đăng ký đào tạo/học viên từ Cổng PLQG. BA/SRS cần bổ sung endpoint inbound riêng, tối thiểu gồm:
- API tiếp nhận đăng ký đào tạo: tạo `DANG_KY_DAO_TAO` từ Cổng PLQG, có xác thực mTLS/JWT, chống gửi trùng, trả mã đăng ký nội bộ.
- API tiếp nhận/thêm học viên theo đăng ký: tạo hoặc liên kết `HOC_VIEN` với đăng ký/khóa học, kiểm tra dữ liệu bắt buộc và phạm vi khóa học được công khai.

Dev không nên dùng tạm endpoint CMS nội bộ cho luồng này; QA bổ sung test tích hợp inbound từ Cổng PLQG.

## P1 - CT HTPLDN

### #17 - Đường đi TW từ `DA_DUYET_KQ` đến `DA_TONG_HOP`

**Trả lời:** SRS SM-DOT-BC hiện chỉ có `DA_DUYET_KQ -> DA_GUI_TW -> DA_TONG_HOP`; FR-XI-08 actor BN/ĐP, FR-XI-09 tổng hợp báo cáo từ BN/ĐP đã gửi. Chưa có đường trực tiếp cho đợt báo cáo cấp TW.

**BA chốt:** Thêm chuyển trạng thái riêng cho TW: `DA_DUYET_KQ -> DA_TONG_HOP` khi đợt báo cáo thuộc TW và CB NV TW xác nhận tổng hợp/nội bộ. BN/ĐP vẫn phải qua `DA_GUI_TW`.

### #18 - Tên trường từ chối Đợt báo cáo

**Trả lời:** FR-XI-07a input/output dùng `ly_do`; thông báo nói "lý do từ chối"; DB/BE có thể dùng `ghiChuPheDuyet`. SRS chưa chuẩn hóa tên trường.

**BA chốt:** Dùng `ly_do_tu_choi` / `lyDoTuChoi` cho API từ chối. `ghiChuPheDuyet` nếu tồn tại chỉ nên là ghi chú duyệt chung, không thay thế lý do từ chối.

### #19 - Cho phép `soLieuTongHop.fields` rỗng khi bắt đầu lập báo cáo

**Trả lời:** FR-XI-06 mô tả lập báo cáo theo mẫu 21a/21b và SM-DOT-BC chốt điều kiện `DANG_LAP_BC -> CHO_DUYET_KQ` là "BC đầy đủ số liệu". SRS không nói rõ validation tại bước `/start` phải có tối thiểu 1 trường số liệu.

**BA chốt:** `/start` được tạo khung báo cáo rỗng, nhưng khi trình duyệt phải kiểm tra `soLieuTongHop.fields` không rỗng và đủ trường bắt buộc theo mẫu. Nếu `/start` nghĩa là "bắt đầu lập báo cáo" thì chấp nhận rỗng là hợp lý.

### #20 - Thiết kế response `POST /tong-hop`

**Trả lời:** FR-XI-09 input `bao_cao_ids` là danh sách và output là "BC tổng hợp TW" + các đợt BC được chọn chuyển sang `DA_TONG_HOP`. Nếu response chỉ có `dotBaoCaoId` dạng đơn thì thiết kế không phù hợp với use case chọn nhiều báo cáo.

**BA chốt:** Đổi response thành `dotBaoCaoIds: []`, `baoCaoTongHopId`, `soDotTongHop`.

## P1 - Biểu mẫu

### #21 - Phạm vi quyền NHT với BIEU_MAU

**Trả lời:** SRS FR-VII nhiều lần ghi BIEU_MAU/THU_MUC_BIEU_MAU là dữ liệu owned theo `don_vi_id`, query theo `BR-AUTH-08`, "chỉ xem thư mục thuộc đơn vị mình", "kết quả matching trong phạm vi đơn vị". Tuy nhiên BA chốt thêm ngoại lệ nghiệp vụ: BN/ĐP được thấy biểu mẫu dùng chung/cấp TW.

**BA chốt:** Phạm vi đọc BIEU_MAU cho BN/ĐP/NHT không phải chỉ own-unit thuần. Quy tắc đúng là: thấy biểu mẫu của đơn vị mình **và** biểu mẫu cấp TW dùng chung. Không thấy biểu mẫu của BN/ĐP ngang cấp khác. Dev sửa BE nếu đang chỉ trả own-unit; QA bổ sung case BN/ĐP thấy bản ghi TW nhưng không thấy ngang cấp.

## P1 - Quản trị hệ thống

### #22 - FR-VIII-22 thông báo "24 giờ" hay "vĩnh viễn"

**Trả lời:** SRS FR-VIII-22 và FR-VIII-26 chốt: liên kết kích hoạt lần đầu là **vĩnh viễn, dùng 1 lần**; liên kết đặt lại mật khẩu cho tài khoản đang `HOAT_DONG` là **30 phút**. Thông báo UI "24 giờ" sai với SRS.

### #23 - FR-VIII-15 field `mat_khau`

**Trả lời:** SRS FR-VIII-15 hiện vẫn có input `mat_khau` bắt buộc khi tạo mới và bước xử lý hash mật khẩu, đồng thời lại gửi email kích hoạt. Nếu logic đã chốt là hệ thống tạo tài khoản rồi gửi email để người dùng đặt mật khẩu lần đầu thì SRS cần dọn lại.

**BA chốt:** Bỏ `mat_khau` khỏi form tạo tài khoản nội bộ; tạo tài khoản ở `CHO_KICH_HOAT`, gửi liên kết kích hoạt vĩnh viễn, người dùng đặt mật khẩu qua FR-VIII-26. Chỉ giữ input mật khẩu cho DN tự đăng ký ở FR-VIII-22.

### #24 - Mâu thuẫn `LOAI_DOANH_NGHIEP`

**Trả lời:** SRS FR-VIII-07 seed `LOAI_DOANH_NGHIEP` = DN siêu nhỏ/nhỏ/vừa, trong FR-VIII-22 lại có field `quy_mo` riêng `SIEU_NHO/NHO/VUA` và `loai_doanh_nghiep_id` riêng. Tên danh mục hiện gây nhầm giữa quy mô DN và loại hình pháp lý.

**BA chốt:** Tách thành 2 danh mục: `QUY_MO_DN` cho siêu nhỏ/nhỏ/vừa theo NĐ39/2018 và `LOAI_HINH_PHAP_LY_DN` cho TNHH/CP/DNTN/HKD. Không giữ gộp.

### #25 - Mật khẩu có bắt buộc ký tự đặc biệt hay không

**Trả lời:** Các FR chính hiện yêu cầu ký tự đặc biệt: FR-VIII-15, FR-VIII-22, FR-VIII-26 đều ghi mật khẩu ít nhất 8 ký tự, gồm chữ hoa + chữ thường + số + ký tự đặc biệt. Tuy nhiên NFR SEC-06 trong master vẫn ghi thiếu ký tự đặc biệt.

**BA chốt:** Quy tắc chuẩn: `minLength >= 8`, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt. Cập nhật SEC-06 cho khớp.

### #26 - Tab "Phiên đăng nhập" trong Profile

**Trả lời:** SRS không mô tả màn hình/tab "Phiên đăng nhập" trong profile. Chỉ có đăng xuất, hết phiên và giới hạn số phiên đồng thời ở NFR/BR.

**BA chốt:** **Bỏ tab "Phiên đăng nhập" khỏi Profile**. Dev ẩn/xóa UI này; QA không kiểm như tính năng thuộc phạm vi phát hành.

### #27 - Quyền đọc VAI_TRO cho người không phải QTHT

**Trả lời:** SRS FR-VIII-14 precondition là "vai trò QTHT"; FR-VIII-15 form tạo tài khoản cũng chỉ QTHT. Không có căn cứ cho người không phải QTHT đọc danh sách vai trò, trừ các trường hợp đặc thù khác đã được mở rõ trong SRS.

**BA chốt:** Giữ strict QTHT-only cho quản lý vai trò. Nếu BE cần `read_vai_tro` cho dropdown nội bộ của workflow khác, phải tạo endpoint chỉ đọc có phạm vi rõ và cấp quyền rõ trong SRS, không mở ngầm.

### #28 - Quy ước mã lỗi Vai trò và Đặt lại mật khẩu

**Trả lời:** SRS QTHT dùng mã lỗi theo nghiệp vụ: `ERR-VT-01/02`, `ERR-PWD-01..06`, `ERR-TK-*`. Nếu BE dùng `ERR-VAL-VIII-*` thì không khớp SRS.

**BA chốt:** Trong phạm vi SRS v3.5 hiện tại, QA kiểm theo mã trong SRS (`ERR-VT-*`, `ERR-PWD-*`). Dev sửa BE nếu đang dùng mã khác cho cùng lỗi.

### #29 - TVV đăng nhập sau đặt mật khẩu lần đầu bị 401

**Trả lời:** Đây không phải vấn đề đặc tả nếu luồng đúng theo FR-VIII-26: token dùng 1 lần, sau khi đặt mật khẩu thành công thì TK/TVV chuyển `HOAT_DONG`, token bị hủy, người dùng đăng nhập bằng mật khẩu mới. Bị 401 sau khi form báo thành công là lỗi triển khai hoặc lỗi môi trường kiểm thử.

**BA chốt:** Cần tài khoản TVV/NHT mới, độc lập để kiểm thử. Kết quả đúng: đặt mật khẩu lần đầu thành công -> token đã dùng -> đăng nhập bằng mật khẩu mới thành công -> trạng thái tài khoản và entity liên quan là `HOAT_DONG`.

## P2/P3 - Vấn đề dùng chung

### #30 - Dấu tiếng Việt trong thông báo BE

**Trả lời:** Thông báo hướng người dùng trong SRS hầu hết là tiếng Việt có dấu. BE trả thông báo không dấu là nợ trải nghiệm, không nên xem là lỗi chặn phát hành nếu mã lỗi và logic đúng.

**BA chốt:** Chuẩn i18n: thông báo hiển thị cho người dùng phải có dấu tiếng Việt; log/field/code nội bộ có thể để ASCII. Dev sửa thông báo hướng người dùng, ưu tiên thông báo lỗi workflow/chính sách.

## Tóm tắt quyết định để đưa vào backlog

| # | Kết luận ngắn |
|---|---|
| 1 | Không gọi là bypass VPD trong CMS; chuyên trang/API public phải dùng luồng công khai riêng, lọc `cong_khai=true` + trạng thái publishable |
| 2 | KH năm phải scoped: TW toàn quốc, BN đơn vị mình, ĐP đơn vị mình; lộ toàn bộ là bug |
| 3 | Khóa học chuẩn 9 trạng thái, từ chối về `DU_THAO` |
| 4 | ĐKT không có workflow duyệt; xóa khi chưa phân phối và chưa có kết quả liên kết |
| 5 | CT 0 đợt BC: cho hoàn thành nếu có cờ không yêu cầu báo cáo; nếu phải báo cáo thì bắt `COUNT > 0` và tất cả đạt trạng thái cuối |
| 6-7 | Lý do từ chối nên dùng field riêng, từ chối kết quả cần bổ sung field riêng |
| 8,28 | Giữ mã lỗi theo SRS: `ERR-CTDT-*`, `ERR-VT-*`, `ERR-PWD-*`; Dev/QA sửa theo SRS |
| 9 | NHCH chuẩn 2 trạng thái |
| 10-11 | HV không bắt buộc tài khoản 1:1; luồng chính qua DN/NHT đăng ký |
| 12 | Nên thêm `KET_HOP` cho Khóa học |
| 13 | Sĩ số tối đa bắt buộc trước khi trình duyệt |
| 14 | Công khai phải có form trường công khai |
| 15 | Thêm BR-LH-CONFLICT-01 |
| 16 | DN/NHT đăng ký đào tạo từ Cổng PLQG là yêu cầu sản phẩm; bổ sung API inbound đăng ký đào tạo/học viên |
| 17-20 | CT HTPLDN cần bổ sung đường tổng hợp trực tiếp cho TW, chuẩn hóa field từ chối, kiểm tra khi trình báo cáo, response tổng hợp dạng danh sách |
| 21 | Biểu mẫu: BN/ĐP/NHT thấy dữ liệu đơn vị mình + dữ liệu TW dùng chung; không thấy ngang cấp |
| 22-23 | Kích hoạt lần đầu vĩnh viễn; tạo TK nội bộ nên bỏ field mật khẩu |
| 24-27 | Tách danh mục DN, mật khẩu có ký tự đặc biệt, bỏ tab Phiên đăng nhập, VAI_TRO strict QTHT trừ khi spec mở read-only |
| 29 | TVV first-login fail là bug/môi trường kiểm thử, không phải spec |
| 30 | Message BE hướng người dùng nên có dấu tiếng Việt |
