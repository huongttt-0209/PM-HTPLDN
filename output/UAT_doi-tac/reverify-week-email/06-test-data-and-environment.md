# Test Data & Environment — Email

## 1. Mailbox thật và alias thực thi

Hộp thư thật duy nhất là `diupt01@gmail.com`. Các địa chỉ có dấu `+` không cần tạo tài khoản hay mật khẩu riêng; Gmail tự chuyển thư của mọi alias vào hộp thư này. Bộ test DEV dùng Gmail thật làm oracle nhận OTP và thông báo; không dùng dịch vụ bắt thư SMTP. Alias đã được preflight bằng thư thật tới `diupt01+check@gmail.com` ngày 2026-08-12.

| Alias/Fixture | Email hoặc pattern | Mục đích | Cách kiểm tra DEV/Gmail | Tách biệt/Ghi chú |
|---|---|---|---|---|
| MB_PRIMARY | diupt01@gmail.com | Oracle nhận OTP và email thông báo thật trên DEV | Đăng nhập Gmail; tìm `to:<alias>` kèm mốc thời gian/subject | Mọi diupt01+...@gmail.com sẽ về hộp thư này |
| MB_ALIAS_CHECK | diupt01+check@gmail.com | Preflight kiểm tra Gmail plus alias | to:diupt01+check@gmail.com | Đã gửi/nhận và xác minh trường To lúc 14:07 ICT 2026-08-12 |
| MB_QTHT | diupt01+qtht@gmail.com | Quản trị hệ thống | to:diupt01+qtht@gmail.com | TAI_KHOAN.email của username admin trên DEV |
| MB_TK_CURRENT | diupt01+tk-current@gmail.com | TAI_KHOAN.email hiện tại | to:diupt01+tk-current@gmail.com | Khác MB_TK_OLD/MB_TK_NEW/MB_DN_CONTACT |
| MB_TK_OLD | diupt01+tk-old@gmail.com | Email tài khoản trước khi đổi | to:diupt01+tk-old@gmail.com | Mailbox âm sau khi đổi |
| MB_TK_NEW | diupt01+tk-new@gmail.com | Email tài khoản sau khi đổi | to:diupt01+tk-new@gmail.com | Mailbox dương sau khi đổi |
| MB_DN_CONTACT | diupt01+dn-contact@gmail.com | DOANH_NGHIEP.email liên hệ | to:diupt01+dn-contact@gmail.com | Khác email TK khi test routing |
| MB_DN_LOGIN | diupt01+dn-login@gmail.com | TAI_KHOAN.email của DN đã có tài khoản | to:diupt01+dn-login@gmail.com | Khác MB_DN_CONTACT để kiểm đúng nguồn recipient |
| MB_DN_AG_LOGIN | diupt01+dn-ag-login@gmail.com | TAI_KHOAN.email của DN An Giang | to:diupt01+dn-ag-login@gmail.com | TK 0209888006; khác email liên hệ DN |
| MB_DN_AG_CONTACT | diupt01+dn-ag-contact@gmail.com | DOANH_NGHIEP.email liên hệ của DN An Giang | to:diupt01+dn-ag-contact@gmail.com | DN-AGG-0001; không dùng thay email TK trong workflow |
| MB_DN_NO_ACCOUNT | diupt01+dn-no-account@gmail.com | DOANH_NGHIEP.email của DN không có tài khoản | to:diupt01+dn-no-account@gmail.com | MST 0108051801; email-only; không tạo TAI_KHOAN |
| MB_DN_REGISTER | diupt01+dn-register@gmail.com | DN tự đăng ký: cùng giá trị ở TAI_KHOAN.email và DOANH_NGHIEP.email | to:diupt01+dn-register@gmail.com | Chỉ dùng case yêu cầu đồng bộ ban đầu |
| MB_CB_NV_A | diupt01+cb-nv-a@gmail.com | CB nghiệp vụ đúng đơn vị A | to:diupt01+cb-nv-a@gmail.com | Khác CB PD và đơn vị B |
| MB_CB_NV_A_2 | diupt01+cb-nv-a-2@gmail.com | CB nghiệp vụ thứ hai cùng đơn vị A | to:diupt01+cb-nv-a-2@gmail.com | Tách người tạo và người được giao xử lý |
| MB_CB_PD_A | diupt01+cb-pd-a@gmail.com | CB phê duyệt đúng đơn vị A | to:diupt01+cb-pd-a@gmail.com | Khác CB NV và đơn vị B |
| MB_CB_PD_A_2 | diupt01+cb-pd-a-2@gmail.com | CB phê duyệt thứ hai cùng đơn vị TW | to:diupt01+cb-pd-a-2@gmail.com | Chỉ dùng cho escalation sau khi dev xác nhận/config đúng quan hệ nhận |
| MB_CB_NV_B | diupt01+cb-nv-b@gmail.com | CB nghiệp vụ mailbox âm đơn vị B | to:diupt01+cb-nv-b@gmail.com | Không được nhận sự kiện của A |
| MB_CB_PD_B | diupt01+cb-pd-b@gmail.com | CB phê duyệt mailbox âm đơn vị B | to:diupt01+cb-pd-b@gmail.com | Không được nhận sự kiện của A |
| MB_CB_NV_HN | diupt01+cb-nv-dn@gmail.com | CB nghiệp vụ Sở Tư pháp Hà Nội | to:diupt01+cb-nv-dn@gmail.com | Dùng sửa/kiểm DN Hà Nội và workflow địa phương |
| MB_CB_PD_HN | diupt01+cb-pd-dn@gmail.com | CB phê duyệt Sở Tư pháp Hà Nội | to:diupt01+cb-pd-dn@gmail.com | Cùng đơn vị với DN 0109998887 |
| MB_CB_NV_AG | diupt01+cb-nv-ag@gmail.com | CB nghiệp vụ Sở Tư pháp An Giang | to:diupt01+cb-nv-ag@gmail.com | Dùng lane vụ việc/chi trả An Giang |
| MB_CB_PD_AG | diupt01+cb-pd-ag@gmail.com | CB phê duyệt Sở Tư pháp An Giang | to:diupt01+cb-pd-ag@gmail.com | Cùng đơn vị với DN/TVV/NHT An Giang |
| MB_TVV_TW | diupt01+tvv-tw@gmail.com | Tư vấn viên thuần cấp TW | to:diupt01+tvv-tw@gmail.com | qa_tvv_tw_r19 / TVV-BTP-TW-0016 |
| MB_TVV_AG | diupt01+tvv-ag@gmail.com | Tư vấn viên thuần An Giang | to:diupt01+tvv-ag@gmail.com | qa_tvv_dp_r18 / TVV-STP-AG-0001 |
| MB_CG | diupt01+cg@gmail.com | Chuyên gia/người được phân công đánh giá | to:diupt01+cg@gmail.com | Không dùng chung TVV/NHT |
| MB_NHT_TW | diupt01+nht-tw@gmail.com | Người hỗ trợ đơn vị TW | to:diupt01+nht-tw@gmail.com | Không dùng chung TVV/CG |
| MB_NHT_AG | diupt01+nht-ag@gmail.com | Người hỗ trợ Sở Tư pháp An Giang | to:diupt01+nht-ag@gmail.com | Dùng kiểm đúng phạm vi đơn vị/địa phương |
| MB_HV_01 | diupt01+hv-01@gmail.com | HOC_VIEN.email học viên 01 | to:diupt01+hv-01@gmail.com | Dùng sự kiện hủy/bắt đầu khóa theo BR-NOTIF-01; đã set |
| MB_HV_02 | diupt01+hv-02@gmail.com | HOC_VIEN.email học viên 02 | to:diupt01+hv-02@gmail.com | Dùng kiểm gửi đủ học viên; đã set |
| MB_GV_01 | diupt01+gv-01@gmail.com | GIANG_VIEN.email giảng viên của khóa | to:diupt01+gv-01@gmail.com | Dùng sự kiện khóa bắt đầu theo BR-NOTIF-01; đã set |
| MB_ORG_A | diupt01+org-a@gmail.com | Email liên hệ tổ chức tư vấn A/CC dương | to:diupt01+org-a@gmail.com | Khác ORG_B |
| MB_ORG_B | diupt01+org-b@gmail.com | Email liên hệ tổ chức tư vấn B/mailbox âm | to:diupt01+org-b@gmail.com | Không được nhận sự kiện của A |
| MB_ATTACKER | diupt01+attacker@gmail.com | Mailbox âm cho header injection | to:diupt01+attacker@gmail.com | Tuyệt đối không được nhận |
| PATTERN_TC | diupt01+uat-{test-case-id}@gmail.com | Email mới/unique theo từng TC tạo TK, đăng ký, token hoặc claim | to:<email cụ thể đã sinh> | Ví dụ EM-TK-ACT-01 → diupt01+uat-em-tk-act-01@gmail.com; không tái sử dụng |
| PATTERN_TC_VARIANT | diupt01+uat-{test-case-id}-{old\|new\|dn}@gmail.com | Các biến thể cần phân biệt email cũ/mới/DN trong cùng TC | to:<email biến thể> | Mỗi biến thể là một recipient logic riêng |
| MB_BOUNCE | bounce@example.invalid | SMTP failure/bounce | Không có inbox | Không thay bằng Gmail alias; cần SMTP stub/DSN harness |
| MST_RANGE | 0100000001..0100009999 | Mỗi TC một MST | — | Không tái sử dụng |

## 2. Cách chọn email khi chạy TC

1. Khi chạy DEV, chỉ đăng nhập Gmail bằng `MB_PRIMARY`; không đăng nhập từng alias. Tìm thư bằng query `to:<alias>` kết hợp `after:YYYY/MM/DD`, subject và mốc trigger.
2. TC workflow trên actor/record đã setup dùng alias cố định tương ứng: `MB_CB_*`, `MB_TVV_TW`, `MB_TVV_AG`, `MB_CG`, `MB_NHT_*`, `MB_HV_*`, `MB_GV_01`, `MB_ORG_*`.
3. TC tạo tài khoản, tự đăng ký DN, activation/reset token, claim hoặc kiểm unique phải sinh email từ `PATTERN_TC`, thay `{test-case-id}` bằng ID viết thường. Ví dụ `EM-TK-ACT-01` dùng `diupt01+uat-em-tk-act-01@gmail.com`.
4. TC cần phân biệt email TK cũ/mới/DN dùng `MB_TK_OLD`, `MB_TK_NEW`, `MB_DN_CONTACT` hoặc `PATTERN_TC_VARIANT`; tuyệt đối không cho các giá trị giống nhau.
5. Riêng DN tự đăng ký, gán cùng một alias của TC cho `TAI_KHOAN.email` và `DOANH_NGHIEP.email` để kiểm đồng bộ ban đầu.
6. Trước khi trigger, tìm Gmail theo `to:<alias>` và ghi baseline count/thời gian. Sau trigger, tìm lại đúng alias, mở **Show details/Show original** và lưu To/CC, subject, timestamp, message-id đã mask.
7. Mailbox âm cũng được kiểm bằng query `to:<alias>` trong cùng khoảng thời gian. Không kết luận chỉ vì thấy thư trong inbox chung.
8. Không tái sử dụng alias của case tạo TK/token nếu fixture cũ chưa cleanup; TAI_KHOAN.email vẫn phải unique.

## 3. Giới hạn khi dùng một inbox Gmail thật

- `EM-INF-08` cần nhiều recipient logic; với một Gmail phải đối chiếu chính xác trường `To` và SMTP envelope, không chỉ nhìn inbox chung.
- Bounce/4xx/5xx/timeout không dùng Gmail alias; bắt buộc SMTP stub/DSN harness và `MB_BOUNCE`.
- Email xuất hiện trong Gmail chứng minh thư đã được chuyển tới hộp thư thật; với case `in-app`, phải đối chiếu thêm chuông/trang thông báo của đúng tài khoản. Queue/audit chỉ kiểm khi môi trường cho phép; không yêu cầu DB.
- Các alias chung một inbox chỉ chứng minh routing theo địa chỉ To, không chứng minh cách ly vật lý giữa các mailbox.

## 4. Fixture trạng thái và routing đào tạo

- TAI_KHOAN: CHO_KICH_HOAT, HOAT_DONG, TAM_KHOA, VO_HIEU_HOA; email TK khác email DN ở case routing.
- DOANH_NGHIEP: có/không email; có/không TK liên kết; hai DN dùng chung email.
- TVV/NHT: CHO_PHE_DUYET, CHO_KICH_HOAT, HOAT_DONG.
- Hỏi đáp/Vụ việc/TVCS/Đào tạo/Báo cáo: đủ state nguồn của từng transition.
- Cấu hình: email ON/OFF; in-app ON/OFF; lịch/ngày lễ; SMTP success/4xx/5xx/timeout/bounce.
- FR-III-03/19: duyệt/từ chối đăng ký và công bố kết quả dùng `DANG_KY_DAO_TAO.nguoi_dang_ky_id → TAI_KHOAN.email` của DN/NHT. BR-NOTIF-01(5)(6): hủy/bắt đầu khóa gửi `HOC_VIEN.email`; bắt đầu khóa còn gửi `GIANG_VIEN.email`. Không tạo tài khoản riêng cho HV/GV.

## 5. Quy tắc dữ liệu và bằng chứng

1. Mỗi TC dùng MST/username riêng; không tái sử dụng nếu TC kiểm unique/token.
2. Lưu baseline count, event timestamp và message-id trước/sau trigger.
3. Dùng clock cố định cho test 30 phút, 5 phút, ngày làm việc và reminder 24h.
4. Không ghi mật khẩu thật/token đầy đủ vào evidence hoặc file testcase.
5. Nếu ứng dụng từ chối dấu `+`, dừng các case nhận mail và mở defect/blocker môi trường; không tự đổi sang email không tồn tại.
