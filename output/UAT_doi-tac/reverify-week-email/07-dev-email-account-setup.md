# Dev Setup — Tài khoản, liên kết và email trên DEV

> Hộp thư thật duy nhất: `diupt01@gmail.com`. Tất cả địa chỉ `diupt01+...@gmail.com` tự đổ về hộp thư này, không cần tạo Gmail hay mật khẩu riêng. OTP và email thông báo DEV phải được kiểm trực tiếp trong Gmail thật bằng trường `To`.  
> Căn cứ SRS: `TAI_KHOAN.email` là email duy nhất của tài khoản để nhận kích hoạt/reset/workflow; `DOANH_NGHIEP.email` là email liên hệ và có thể trùng; DN không có tài khoản nhận email-only qua `DOANH_NGHIEP.email`.
> Nguồn kiểm tra: `https://18.143.165.120.nip.io` — đọc trực tiếp API DEV ngày 2026-08-12. Mọi username/ID trong bảng là record thực tế trên DEV.
> Trạng thái: mapping email trong bảng đã được áp dụng và đọc lại. OTP/login đã được kiểm chứng cho các fixture trọng yếu được ghi rõ ở cột cuối.

## Kết quả setup

1. Không cần seed thêm actor bắt buộc: các role/record cần cho luồng email đều đã tồn tại. Một tài khoản TVV thuần được khôi phục và hai tài khoản TVV thuần được reset để đăng nhập test; không tạo record rời không liên kết nghiệp vụ.
2. Mỗi `TAI_KHOAN.email` dùng một plus alias riêng để giữ unique và kiểm chính xác trường `To`; mọi alias cùng đổ về Gmail thật `diupt01@gmail.com`.
3. DN `0109998887` và `0209888006` cố ý tách email tài khoản với email liên hệ DN. DN `0108051801` chỉ có email nghiệp vụ và không có tài khoản. DN `0722072207` giữ email NULL cho negative case.
4. Duyệt/từ chối đăng ký và công bố kết quả đào tạo gửi tới `TAI_KHOAN.email` của DN/NHT đã tạo đăng ký. Riêng hủy/bắt đầu khóa gửi học viên qua `HOC_VIEN.email`; sự kiện bắt đầu còn gửi giảng viên qua `GIANG_VIEN.email`, đúng BR-NOTIF-01.
5. Các dòng `DYNAMIC` do QA tạo trong lúc chạy đúng testcase, không seed trước.

## Phương án setup escalation không cần dev gán recipient cố định

1. Dùng hồ sơ thuộc Bộ KH&ĐT cho `EM-NOT-HDD-04`, `EM-NOT-HDD-07`, `EM-NOT-VV-10`. Theo BR-AUTH-02, Bộ/ngành có `don_vi_cha_id` trỏ trực tiếp tới TW. Trước trigger, đọc lại quan hệ này và danh sách tài khoản hoạt động có role `CB_PD_TW` tại đơn vị cha.
2. Pass recipient khi có ít nhất một email escalation tới tài khoản thỏa đúng role + đơn vị cha, và mọi recipient escalation thực tế đều thỏa điều kiện đó. Không ép hệ thống gửi riêng `cbpd_tw_02`, cũng không ép gửi một hay tất cả vì SRS không quy định cardinality.
3. Do chỉ dùng Gmail thật, trước khi chạy ba case phải map toàn bộ tài khoản `CB_PD_TW` hoạt động mà resolver có thể chọn sang các alias Gmail riêng. Hiện `cbpd_tw_01` và `cbpd_tw_02` đã map; các tài khoản ứng viên còn lại phải được QA cập nhật nếu có quyền, nếu không thì liệt kê cho dev. Nếu không có quyền tạo fixture thời gian/chạy scheduled job thì Blocked riêng do clock/job.

## Danh sách setup

| Nhóm setup | Username/Mã record | ID trên DEV | Vai trò/Loại | Đơn vị đã xác minh | Trạng thái | Email trước setup | Email hiện tại/đã set | Trường đã cập nhật | Liên kết/Điều kiện | Mục đích test | Kết quả xác minh |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TAI_KHOAN | admin | 00000000-0000-4000-8000-000000000099 | QTHT | Không gắn đơn vị | HOAT_DONG | admin@htpldn.gov.vn | diupt01+qtht@gmail.com | TAI_KHOAN.email | Tài khoản quản trị hiện hữu | Quản trị/cấp tài khoản | ĐÃ SET + đọc lại API |
| TAI_KHOAN | cbnv_tw_01 | 6647b7bb-db9a-4a12-9535-766c77a4f04b | CB_NV_TW | Cục Bổ trợ tư pháp - Bộ Tư pháp | HOAT_DONG | cbnv_tw_01@htpldn.test | diupt01+cb-nv-a@gmail.com | TAI_KHOAN.email | CB NV chính lane TW | Hỏi đáp/đào tạo/TVV-CG/TVCS/đánh giá | ĐÃ SET + OTP/login verified |
| TAI_KHOAN | cbnv_tw_02 | 75ef9f6b-5f5b-474d-9861-dde1c1563f50 | CB_NV_TW | Cục Bổ trợ tư pháp - Bộ Tư pháp | HOAT_DONG | cbnv_tw_02@htpldn.test | diupt01+cb-nv-a-2@gmail.com | TAI_KHOAN.email | Assignee thứ hai cùng đơn vị | Phân công/chuyển xử lý | ĐÃ SET + đọc lại API |
| TAI_KHOAN | cbpd_tw_01 | 2bd5fc7f-8b33-4427-954d-c011a7555f06 | CB_PD_TW | Cục Bổ trợ tư pháp - Bộ Tư pháp | HOAT_DONG | cbpd_tw_01@htpldn.test | diupt01+cb-pd-a@gmail.com | TAI_KHOAN.email | CB phê duyệt chính lane TW | Duyệt/từ chối/đánh giá | ĐÃ SET + OTP/login verified |
| TAI_KHOAN | cbpd_tw_02 | 305a7f9c-cfcd-41ea-8354-108f42dfca7f | CB_PD_TW | Cục Bổ trợ tư pháp - Bộ Tư pháp | HOAT_DONG | cbpd_tw_02@htpldn.test | diupt01+cb-pd-a-2@gmail.com | TAI_KHOAN.email | Một ứng viên nhận escalation tại đơn vị cha TW; không cố định cardinality khi SRS không nêu | Escalation | ĐÃ SET email; đối soát recipient theo role + don_vi_cha_id |
| TAI_KHOAN | cbnv_bn_01 | a2ad2192-ebaf-4971-9b36-2beca4d1c216 | CB_NV_BN | Bộ Kế hoạch và Đầu tư | HOAT_DONG | cbnv_bn_01@htpldn.test | diupt01+cb-nv-b@gmail.com | TAI_KHOAN.email | Đơn vị B | Mailbox âm | ĐÃ SET + đọc lại API |
| TAI_KHOAN | cbpd_bn_01 | e8a57e11-77a4-40f6-8907-30a95b1e229f | CB_PD_BN | Bộ Kế hoạch và Đầu tư | HOAT_DONG | cbpd_bn_01@htpldn.test | diupt01+cb-pd-b@gmail.com | TAI_KHOAN.email | Đơn vị B | Mailbox âm | ĐÃ SET + đọc lại API |
| TAI_KHOAN | cbnv_hn | 87bb5785-2ab8-4fa1-847b-ce2ac61f1793 | CB_NV_DP | Sở Tư pháp Hà Nội | HOAT_DONG | cbnv.hn@htpldn.test | diupt01+cb-nv-dn@gmail.com | TAI_KHOAN.email | Lane Hà Nội | DN 0109998887 | ĐÃ SET + OTP/login verified |
| TAI_KHOAN | cbpd_hn | 82ff67b4-7702-4a6a-b4bd-0d41ddc3311d | CB_PD_DP | Sở Tư pháp Hà Nội | HOAT_DONG | cbpd.hn@htpldn.test | diupt01+cb-pd-dn@gmail.com | TAI_KHOAN.email | Lane Hà Nội | Duyệt hồ sơ Hà Nội | ĐÃ SET + đọc lại API |
| TAI_KHOAN | cbnv_dp_01 | e81aa51b-e132-49a4-8831-fd404512af40 | CB_NV_DP | Sở Tư pháp An Giang | HOAT_DONG | cbnv_dp_01@htpldn.test | diupt01+cb-nv-ag@gmail.com | TAI_KHOAN.email | Lane An Giang | Vụ việc/chi trả | ĐÃ SET + đọc lại API |
| TAI_KHOAN | cbpd_dp_01 | 8ed9e497-387f-4d37-ac06-8c1545b593a5 | CB_PD_DP | Sở Tư pháp An Giang | HOAT_DONG | cbpd_dp_01@htpldn.test | diupt01+cb-pd-ag@gmail.com | TAI_KHOAN.email | Lane An Giang | Duyệt vụ việc/chi trả | ĐÃ SET + đọc lại API |
| TAI_KHOAN | nht_qa_tw | a31689a8-019e-40ff-b084-58f55589b694 | NHT | Cục Bổ trợ tư pháp - Bộ Tư pháp | HOAT_DONG | nht.qa.tw@htpldn.test | diupt01+nht-tw@gmail.com | TAI_KHOAN.email | NHT TW | Nộp hồ sơ/đăng ký học | ĐÃ SET + đọc lại API |
| TAI_KHOAN | nht_qa_01 | 9a1fbbcd-364a-4b41-9dac-15696847caba | NHT | Sở Tư pháp An Giang | HOAT_DONG | nht_qa_01@htpldn.test | diupt01+nht-ag@gmail.com | TAI_KHOAN.email | NHT An Giang | Nộp hồ sơ/đăng ký học | ĐÃ SET + đọc lại API |
| TAI_KHOAN + TU_VAN_VIEN | qa_tvv_tw_r19 \| TVV-BTP-TW-0016 | TK 3f9d5fc4-eac3-4229-8c2c-3f79a952ed83 \| TVV aaaa1707-0000-4000-8000-000000000d01 | TVV thuần | Cục Bổ trợ tư pháp - Bộ Tư pháp | HOAT_DONG | qa.tvv.tw.r19@htpldn.gov.vn | diupt01+tvv-tw@gmail.com | TAI_KHOAN.email + TU_VAN_VIEN.email | Đã khôi phục TK; reset mật khẩu test | TVV lane TW | ĐÃ SET + reset/login verified |
| TAI_KHOAN + TU_VAN_VIEN | qa_tvv_dp_r18 \| TVV-STP-AG-0001 | TK a0529ecc-e050-4723-8b6b-5c15045cadf4 \| TVV 4c1d3aab-db59-40f8-9a58-b8637c42d8ab | TVV thuần | Sở Tư pháp An Giang | HOAT_DONG | qa.tvv.dp.r18@htpldn.gov.vn | diupt01+tvv-ag@gmail.com | TAI_KHOAN.email + TU_VAN_VIEN.email | Liên kết TC-STP-AG-0001; reset mật khẩu test | TVV lane An Giang | ĐÃ SET + reset/login verified |
| TAI_KHOAN + TU_VAN_VIEN | qa_tvvseed28 \| TVV-BTP-TW-0002 | TK 5432719c-c542-4a5d-8c3a-db1b8a918bbf \| TVV 98cfd963-3cd3-4c8a-bfa9-625460824d6d | TVV+CG; hồ sơ CG | Cục Bổ trợ tư pháp - Bộ Tư pháp | HOAT_DONG | qa.tvvseed28@htpldn-uat.local | diupt01+cg@gmail.com | TAI_KHOAN.email + TU_VAN_VIEN.email | Liên kết TCTV-SEED-0001 | CG fixture chính; người được phân công đánh giá | ĐÃ SET + login endpoint verified |
| TAI_KHOAN + DOANH_NGHIEP | 0109998887 \| DN-HNI-0001 | TK 996cc5db-43c5-4903-b3d1-1c21adb2ece8 \| DN 829abcac-b0af-4cde-9af9-ec51bc79014c | DN | Sở Tư pháp Hà Nội | HOAT_DONG | qa.uat.dn.verify@test.htpldn.vn | TK: diupt01+dn-login@gmail.com \| DN: diupt01+dn-contact@gmail.com | TAI_KHOAN.email + DOANH_NGHIEP.email | Hai email cố ý khác nhau | Routing nguồn TK/DN | ĐÃ SET + OTP/login verified |
| TAI_KHOAN + DOANH_NGHIEP | 0209888006 \| DN-AGG-0001 | TK b9c7f944-989f-48f4-8457-9d2e28875fc5 \| DN c03a66bc-f584-437d-89c8-1371f6a69772 | DN | Sở Tư pháp An Giang | HOAT_DONG | qa.uat.dn.angiang@test.htpldn.vn | TK: diupt01+dn-ag-login@gmail.com \| DN: diupt01+dn-ag-contact@gmail.com | TAI_KHOAN.email + DOANH_NGHIEP.email | Hai email cố ý khác nhau | Vụ việc/chi trả An Giang | ĐÃ SET + đọc lại API |
| DOANH_NGHIEP | DN-01-0002 \| MST 0108051801 | 6c75f283-d560-48ca-ba7c-524e6a690ff0 | DN không TK | Cục Bổ trợ tư pháp - Bộ Tư pháp | Đang hoạt động | uat.v108.tvcs@example.test | diupt01+dn-no-account@gmail.com | DOANH_NGHIEP.email | Không có TAI_KHOAN trùng MST | TVCS email-only | ĐÃ SET + xác minh không có account |
| DOANH_NGHIEP | DN-07-0001 \| MST 0722072207 | 92cdc9c1-41d1-4802-bc1f-bd7fb2e239de | DN không TK | Cục Bổ trợ tư pháp - Bộ Tư pháp | Đang hoạt động | NULL | Giữ NULL | Không cập nhật | Không có TAI_KHOAN trùng MST | Negative thiếu recipient | ĐÃ xác minh giữ NULL |
| TO_CHUC_TU_VAN | TCTV-SEED-0001 | 5eed0004-0000-4000-8000-000000000001 | Tổ chức A | Cục Bổ trợ tư pháp - Bộ Tư pháp | HOAT_DONG | NULL | diupt01+org-a@gmail.com | TO_CHUC_TU_VAN.email | Liên kết TVV-BTP-TW-0002 | CC tổ chức A | ĐÃ SET + đọc lại API |
| TO_CHUC_TU_VAN | TC-STP-AG-0001 | d19eb64b-58ba-4993-b1d7-7762845459b6 | Tổ chức B | Sở Tư pháp An Giang | HOAT_DONG | tctv.qa.dp@htpldn.test | diupt01+org-b@gmail.com | TO_CHUC_TU_VAN.email | Liên kết TVV-STP-AG-0001 | CC/mailbox âm | ĐÃ SET + đọc lại API |
| HOC_VIEN | Học viên TW 01 | aaaa1111-0000-4000-8001-000000000001 | HOC_VIEN | Cục Bổ trợ tư pháp - Bộ Tư pháp | taiKhoanId=NULL | hv.aaaa1@htpldn.local | diupt01+hv-01@gmail.com | HOC_VIEN.email | Dùng/gắn vào khóa fixture khi chạy TC | Hủy/bắt đầu khóa gửi HV | ĐÃ SET + đọc lại API |
| HOC_VIEN | Học viên TW 02 | aaaa1111-0000-4000-8001-000000000002 | HOC_VIEN | Cục Bổ trợ tư pháp - Bộ Tư pháp | taiKhoanId=NULL | hv.aaaa2@htpldn.local | diupt01+hv-02@gmail.com | HOC_VIEN.email | Dùng/gắn vào cùng khóa fixture khi chạy TC | Kiểm gửi đủ HV | ĐÃ SET + đọc lại API |
| GIANG_VIEN | GV-QA-001 \| TS. Lê Hoàng Thái | f0fafafa-0000-4000-8000-000000000001 | GIANG_VIEN | Cục Bổ trợ tư pháp - Bộ Tư pháp | DANG_HOAT_DONG; taiKhoanId=NULL | qa-gv-thai@htpldn.test | diupt01+gv-01@gmail.com | GIANG_VIEN.email | Có lịch sử giảng dạy; chọn làm GV cùng khóa fixture | Khóa bắt đầu gửi GV | ĐÃ SET + đọc lại API |
| DYNAMIC | DYNAMIC_NEW_ACCOUNT | Không pre-seed | Theo từng TC | — | Chưa tồn tại | — | diupt01+uat-{test-case-id}@gmail.com | QA tạo qua UI/API | Không seed trước; cleanup sau TC | Activation/reset/unique/claim | QA tạo khi chạy |
| DYNAMIC | DYNAMIC_DN_REGISTER | Không pre-seed | DN | — | Chưa tồn tại | — | Alias theo TC; TK.email = DN.email lúc đăng ký | QA tạo qua tự đăng ký | MST/username/email phải chưa tồn tại | DN tự đăng ký | QA tạo khi chạy |

## Nguyên tắc không vượt SRS

Chỉ setup trường/quan hệ cần bởi testcase có trace SRS. Học viên/giảng viên không cần tài khoản đăng nhập riêng; BR-NOTIF-01 vẫn yêu cầu email ở sự kiện hủy/bắt đầu khóa nên dùng email trực tiếp trên entity. Các case kỹ thuật không có căn cứ SRS đã được loại khỏi suite.

## Lưu ý riêng cho alias và username TVV/CG

SRS cho biết username TVV/CG tự sinh từ phần trước `@`, trong khi regex username chỉ cho chữ thường, số và `_`. Plus alias như `diupt01+tvv@gmail.com` có dấu `+`, nên **không dùng plus alias cho testcase đang kiểm việc tự sinh username**. Các tài khoản có sẵn trong bảng giữ nguyên username hiện hữu; chỉ thay trường email. Riêng testcase auto-create cần một địa chỉ có local-part hợp regex và chưa tồn tại trong `TAI_KHOAN`, rồi cleanup sau test. Đây là giới hạn dữ liệu test cần dev biết, không phải yêu cầu tạo thêm Gmail.
