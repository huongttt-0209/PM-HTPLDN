# Dev Seed Data Needed — Functional Round 7

> Rà soát thư mục `output/qa-reports/round7-2026-05-06/functional` ngày 2026-05-11.
> File này chỉ liệt kê các testcase bị block/defer do thiếu test data, account test, hoặc cần DB backdate/time-travel. Không tính các blocker thuần bug code, endpoint chưa deploy, mTLS/VNeID/Cổng PLQG hạ tầng, hoặc BA/spec confirmation.

## Tổng hợp nhanh

| Module | Testcase | Cần seed data gì | Mục đích test | File nguồn |
|---|---|---|---|---|
| QTHT Tài khoản | TP-TK-02/03 | Tài khoản legacy ở state `CHO_PHAN_QUYEN`, có đủ dữ liệu để chuyển `CHO_KICH_HOAT -> CHO_PHAN_QUYEN -> HOAT_DONG` | Verify legacy state path còn được SM-TAIKHOAN xử lý đúng | `qtht-tai-khoan/functional-test-report-FR-VIII-15-tk-sm.md` |
| QTHT Tài khoản | TP-TK-08 | Tài khoản `TAM_KHOA` có `locked_until = NOW() - 31 minutes` | Verify auto unlock `TAM_KHOA -> HOAT_DONG` sau 30 phút | `qtht-tai-khoan/functional-test-report-FR-VIII-15-tk-sm.md` |
| QTHT Tài khoản | TP-TK-11 | Tài khoản `CHO_KICH_HOAT` có `created_at = NOW() - 8 days` | Verify auto vô hiệu hóa tài khoản chưa kích hoạt quá 7 ngày | `qtht-tai-khoan/functional-test-report-FR-VIII-15-tk-sm.md` |
| QTHT Tài khoản | FR-VIII-26 TC03 | Reset-password token hết hạn: `token_het_han = NOW() - INTERVAL '31 minutes'` cho email test | Verify token expired trả đúng lỗi hết hạn | `qtht-tai-khoan/functional-test-report-FR-VIII-26-reset-mk.md` |
| Chi trả | FR-V.II-14, TC-FULL-04/B5 | 1-2 HSCT thuộc QA DN `6738f415-8192-456c-89dd-ba6a0e7e2493` ở state `YEU_CAU_BO_SUNG`, đủ field BR-CALC-01; hoặc cấp credentials cho 4 DN AG hiện có HSCT000011-000014 | DN login bổ sung hồ sơ, upload file, transition `YEU_CAU_BO_SUNG -> DANG_KIEM_TRA` | `chi-tra/functional-test-report-fr-v.ii-14-2026-05-06.md`, `chi-tra/functional-test-report-r3-fullflow-2026-05-10.md` |
| Chi trả | CT-017 | Negative HSCT qua DN path với `phi_tu_van <= 0` hoặc `so_tien_de_nghi <= 0` | Verify validation BR-EC-22 cho dữ liệu tiền không hợp lệ | `chi-tra/functional-test-report-ChiTra-v3.5.md` |
| Chi trả | CT-018 | DN có `da_chi_trong_nam` khoảng 80-90% trần hỗ trợ năm, kèm HSCT mới đủ BR-CALC-01/02 | Verify over-cap chỉ cấp phần dư còn lại | `chi-tra/functional-test-report-ChiTra-v3.5.md` |
| Hỏi đáp | HD-022c/d | Chạy thêm SQL update `deadline = ngay_tiep_nhan + INTERVAL '5 days'` cho 2 record `8c54715f-4ff5-487f-bc1b-bc405d162534`, `101f22b6-1cbe-4e1a-9d76-ab5d6cfd1322` | Verify SLA badge vàng "Sắp hết hạn" khoảng 70% và đỏ "Quá hạn" khoảng 110%. HD-022b và HD-057 đã PASS sau seed trước đó | `hoi-dap/functional-test-report-r7-7-1-hd-phase9.md` |
| Hỏi đáp | HD-064 | HOI_DAP cấp ĐP `don_vi=STP-AG`, state `DA_DUYET` | Login `cb_pd_bn_04`, POST `/cong-khai` cross-cấp để expect `ERR-PD-01` đúng spec | `hoi-dap/functional-test-report-r7-7-1-hd-phase3a.md` |
| Hỏi đáp | HD-020 stress | Khoảng 10.000 HOI_DAP records trong pool export | Verify cap xuất Excel danh sách hỏi đáp tối đa 10K records theo BR-DATA-06 | `hoi-dap/functional-test-report-r7-7-1-hd-phase4.md` |
| Vụ việc | VV-022, C3-1/2/3 | 3 VU_VIEC có deadline/backdate tương ứng 11/16/21 ngày hoặc đủ mốc `CHU_Y`, `CANH_BAO`, `QUA_HAN` | Verify SLA 4 mức cảnh báo và counter | `vu-viec/functional-test-report-r7-7-3-vu-viec.md` |
| Vụ việc | VV-026 | TVV active có mật khẩu đăng nhập được qua `/login`, liên kết scope phù hợp | Verify TVV scope filter trên Vụ việc | `vu-viec/functional-test-report-r7-7-3-vu-viec.md` |
| Vụ việc | Cluster 0 lifecycle | Tối thiểu 1 VU_VIEC cho mỗi state lifecycle còn thiếu: `PHAN_HOI`, `HOAN_THANH`, `DA_DUYET`, `DA_DANH_GIA` | Chạy các TC base còn lại phụ thuộc state pool | `vu-viec/functional-test-report-r7-7-3-vu-viec.md` |
| Vụ việc | R7.7.3-PRIVACY-1/2 | Bộ data multi-DN/cross-DN: DN test có Vụ việc của chính mình và Vụ việc của DN khác | Verify privacy/scope DN | `vu-viec/functional-test-report-r7-7-3-vu-viec.md` |
| Đào tạo | DT-011/011a/052 | HOC_VIEN records hợp lệ, gắn `lich_hoc_id`; hoặc fix POST `/hoc-viens` rồi seed HV qua chuyên trang DN/NHT | Verify điểm danh, validation điểm danh, tạo HV đồng thời tạo TAI_KHOAN | `dao-tao/functional-test-report-r7-7-6-khoa-hoc-r10.md` |
| Đào tạo | DT-019 | `DANG_KY_DAO_TAO` records đủ để đạt/vượt sức chứa khóa học | Verify đăng ký vượt sức chứa trả `ERR-DK-DT-03` | `dao-tao/functional-test-report-r7-7-6-khoa-hoc-r10.md` |
| Đào tạo | DT-031b/c/d | HOC_VIEN + kết quả khóa học đã công bố, có setup chuyên trang/Cổng PLQG mock | Verify công bố/hủy công bố kết quả và retry outbound | `dao-tao/functional-test-report-r7-7-6-khoa-hoc-r10.md` |
| Đào tạo | DT-054/055 | `KET_QUA_HOC_TAP` records cho HV với chuyên cần/điểm qua và không qua ngưỡng | Verify auto-classify xếp loại và quy tắc HV đạt khóa | `dao-tao/functional-test-report-r7-7-6-khoa-hoc-r10.md` |
| Báo cáo | BC-006/007 | KHOA_HOC ở state `DANG_DIEN_RA` và `KET_THUC` | Verify báo cáo đào tạo theo trạng thái khóa học | `bao-cao/functional-test-report-r7-7-13-bao-cao.md` |
| Báo cáo | BC-008 | Khóa học hoàn thành kèm chấm điểm/kết quả kiểm tra | Verify báo cáo khóa hoàn thành có dữ liệu điểm | `bao-cao/functional-test-report-r7-7-13-bao-cao.md` |
| Báo cáo | BC-010 | Đánh giá có state hoàn tất, tối thiểu 1 đợt `HOAN_THANH` | Verify báo cáo Đánh giá khi có dữ liệu hoàn thành | `bao-cao/functional-test-report-r7-7-13-bao-cao.md` |
| Tư vấn nhanh | TVN-034 | Ít nhất 1 `KHO_CAU_HOI` scoped BN/BKH | Verify positive case BN thấy record của chính BN, không chỉ negative total=0 | `tu-van-nhanh/functional-test-report-r7-7-11-tvn.md` |
| Tư vấn nhanh | TVN-035/036 | Account test dedicated cho TVV và GV trong `users.csv`/auth | Verify no-menu cho TVV/GV như spec, hiện mới có NHT/CG/DN | `tu-van-nhanh/functional-test-report-r7-7-11-tvn.md` |
| Tư vấn nhanh | TVN-032 | Phiên Tư vấn nhanh state `MOI` backdated >30 ngày hoặc config/cron stub timeout | Verify batch auto hết hạn phiên quá 30 ngày | `tu-van-nhanh/functional-test-report-r7-7-11-tvn.md` |
| Tư vấn chuyên sâu | TV-038 | TVCS cấp BN/ĐP, có dữ liệu thuộc đơn vị BN/ĐP khác nhau | Verify CB_NV_BN không thấy TVCS BN khác theo BR-AUTH-08 | `tu-van-chuyen-sau/functional-test-report-r7-7-5-tvcs.md` |
| Tư vấn chuyên sâu | TV-041 | TVCS có `vuViecId` trỏ tới VU_VIEC seed hợp lệ | Verify link cross-module TVCS -> Vụ việc | `tu-van-chuyen-sau/functional-test-report-r7-7-5-tvcs.md` |
| Tư vấn chuyên sâu | TV-053 | NHT có record TVV/NHT hợp lệ để phân công Vụ việc STP-AG, DN có HSPL/VV liên quan | Verify NHT xem HSPL DN có VV phân công | `tu-van-chuyen-sau/functional-test-report-r7-7-5-tvcs.md` |
| Tư vấn chuyên sâu | TV-059 | TVCS `DA_DUYET` đủ điều kiện tạo/link Hợp đồng tư vấn, kèm seed HD TV liên quan | Verify TVCS DA_DUYET tạo/link `hopDongTvId` | `tu-van-chuyen-sau/functional-test-report-r7-7-5-tvcs.md` |
| TVV/CG | UI walk TVV-023 supplement | TVV/CG ở state `TU_CHOI` có sẵn file thẻ hành nghề hợp lệ, cùng đơn vị với NHT test | Chạy UI E2E NHT sửa + lưu hồ sơ bị từ chối mà không bị FE chặn bởi missing file | `tu-van-vien-cg/functional-test-report-r7-7-2-tvv-cg.md` |
| Doanh nghiệp | Tab Hồ sơ chi trả | DN test có HSCT gắn `doanhNghiepId` | Verify tab DN "Hồ sơ chi trả" có dữ liệu thực, không chỉ empty structure | `doanh-nghiep/functional-r7-5-2-cross-module-dn.md` |
| CT HTPLDN | CT-035 | Chương trình HTPLDN cấp BN/ĐP, kèm đợt báo cáo đủ điều kiện gửi TW | Verify CB NV BN/ĐP gửi báo cáo lên TW | `functional-test-report-r7-7-15-cthtpldn.md`, `functional-test-report-r7-7-15-b-dot-bc.md` |
| CT HTPLDN | CT-038 | Tối thiểu 1 đợt BC từ BN và 1 đợt BC từ ĐP cùng kỳ, state `DA_GUI_TW` | Verify CB NV TW tổng hợp báo cáo từ BN/ĐP | `functional-test-report-r7-7-15-b-dot-bc.md` |
| Cross-cutting | Lưu nháp scope hẹp - Biểu mẫu | Ít nhất 1 biểu mẫu trong thư mục Nháp để mở form edit | Verify form Biểu mẫu không còn button "Lưu nháp" trong scope hẹp | `cross-cutting/functional-test-report-r7-8-3-luu-nhap-scope-hep.md` |

## Không tính là seed data

Các mục sau xuất hiện trong report nhưng không phải yêu cầu Dev seed data:

- Cổng PLQG/inbound endpoint 404, mTLS cert, TLS staging, VNeID sandbox: blocker hạ tầng hoặc deploy.
- Các bug UI/BE như PHANCONG-REVERT, TVCS TLPL endpoint 404, HOC_VIEN POST 500, DN menu route, validation/rendering bugs: cần fix code trước, seed chỉ có ý nghĩa sau khi fix.
- Dashboard report ghi rõ `Thiếu seed data = 0`, không có yêu cầu seed mới trong file dashboard.
- Các testcase chỉ cần manual browser thao tác hoặc BA confirm ngưỡng/spec không được đưa vào bảng trên.
