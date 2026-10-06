# Reverify THBCTHCT_01 - dòng 343

- Ngày chạy: 07/08/2026, khoảng 23:44-23:51 giờ Việt Nam
- Môi trường: `https://18.143.165.120.nip.io`
- Bản giao diện: `index-LoDAkSbB.js`, nhãn UI `HTPLDN · V1.0.10`
- Công cụ: Chrome DevTools trên cửa sổ Chrome hiển thị, không dùng Playwright
- Tài khoản thao tác nghiệp vụ: Cán bộ Nghiệp vụ Trung ương #05, `BTP · TW`
- OTP: đọc trực tiếp trên giao diện MailHog, không dùng API MailHog
- DEV phản hồi lần 1/BA chốt dùng để đối chiếu: danh sách tổng hợp phải trả bản ghi riêng theo từng đơn vị; thông báo thành công theo `INF-XI-09-01` là **"Đã tổng hợp báo cáo toàn quốc"**.
- Verdict: **PASS / Test done**

## Phép thử theo bug gốc

1. Đăng nhập đúng vai trò CB NV TW bằng UI, xác thực OTP từ MailHog UI.
2. Bấm menu **Đợt báo cáo** trên UI.
3. Mở màn **Tổng hợp báo cáo toàn quốc**. Dữ liệu sẵn có đủ comparator, không seed API:
   - cùng đợt `DOT-TRON_NAM-2026-1`, cùng kỳ `Tròn năm` có hai bản ghi riêng theo đơn vị;
   - chọn đúng **Sở Tư pháp An Giang**, trạng thái trước `Đã gửi TW`;
   - không chọn **Sở Tư pháp Hà Nội**, trạng thái trước `Đã gửi TW`;
   - báo cáo đối chứng chưa gửi: **Sở Tư pháp An Giang** ở `DOT-SO_BO_NAM-2026-1`, trạng thái UI trước là `Chờ duyệt`, không có trong danh sách tổng hợp.
4. Tick đúng một dòng An Giang, nút đổi thành **Tổng hợp (1)**; bấm **Tổng hợp**.
5. Hộp tổng hợp hiển thị đúng đợt, kỳ, biểu mẫu và **Số đơn vị: 1**; bấm **Lưu tổng hợp**.
6. Đọc lại ngay sau lưu, hard reload, mở lại màn một lần nữa; sau đó mở chi tiết đợt đối chứng và Nhật ký hệ thống bằng UI.

## Đối chiếu 8 ý quyết định

| # | Tiêu chí | Bằng chứng UI/DevTools | Kết quả |
|---:|---|---|---|
| 1 | Chọn chính xác tập báo cáo | UI tô chọn duy nhất dòng Sở TP An Giang của `DOT-TRON_NAM-2026-1`; Hà Nội cùng đợt vẫn bỏ chọn; nút ghi `Tổng hợp (1)`. Request do chính thao tác UI gửi chỉ có `baoCaoIds = [b63fe4e2-0af5-4945-aeab-825814107209]`. | PASS |
| 2 | Tổng hợp + Lưu tổng hợp qua UI | Đã bấm cả hai nút trên UI thật. Form ghi `Số đơn vị: 1`; request `POST /api/v1/dot-bao-caos/tong-hop` trả HTTP 201. | PASS |
| 3 | Tạo bản tổng hợp toàn quốc | Response của lượt bấm tạo bản ghi `04ae77a6-3c28-479c-98ce-a42154264828`, mã `TH-TW-1786121286031`, `loai = TONG_HOP_TW`, đúng `dotBaoCaoId` của `DOT-TRON_NAM-2026-1`. Nhật ký UI mở rộng cũng hiện dữ liệu mới `loai: TONG_HOP_TW`, đúng mã báo cáo và đúng `baoCaoIds`. | PASS |
| 4 | Chỉ báo cáo được chọn đổi trạng thái | Ngay sau lưu, Sở TP An Giang đổi `Đã gửi TW` -> `Đã tổng hợp`. Hard reload và mở lại màn lần hai vẫn `Đã tổng hợp`. | PASS |
| 5 | Báo cáo cùng đợt nhưng không chọn không đổi/không bị kéo theo | Sở TP Hà Nội cùng `DOT-TRON_NAM-2026-1` vẫn `Đã gửi TW` ngay sau lưu, sau hard reload và lần mở lại tiếp theo. | PASS |
| 6 | Báo cáo chưa gửi không xuất hiện/không đổi | Sở TP An Giang của `DOT-SO_BO_NAM-2026-1` không có trong danh sách tổng hợp trước/sau. Chi tiết đợt trên UI trước và sau đều là `Chờ duyệt`, ngày nộp `-`; không bị gán `Đã tổng hợp`. | PASS |
| 7 | Có lưu vết thao tác | UI **Nhật ký hệ thống** có mục lúc `07/08/2026 23:48:06`, người dùng `CB Nghiệp vụ - Trung ương #05`, đơn vị Cục Bổ trợ tư pháp, module `CT HTPLDN`, entity `BAO_CAO_CT_HTPL`, mã bản ghi `04ae77a6...`, thao tác `Tổng hợp`. Mã bản ghi khớp bản tổng hợp vừa tạo. | PASS |
| 8 | Toast đúng BA/DEV confirm | UI hiển thị chính xác **"Đã tổng hợp báo cáo toàn quốc"**, trùng `INF-XI-09-01`. | PASS |

## Retry, network và console

- Quan sát trạng thái ba lần: ngay sau lưu, sau hard reload không cache, và sau khi rời màn rồi mở lại. Cả ba lần đều cho cùng kết quả: An Giang selected `Đã tổng hợp`, Hà Nội unselected `Đã gửi TW`.
- Network của thao tác UI: `POST /tong-hop/goi-y` = 200; `POST /tong-hop` = 201; GET làm mới danh sách = 200.
- Thân request lưu chỉ chứa đúng một mã báo cáo được chọn; response tạo đúng bản ghi `TONG_HOP_TW`.
- Console sau thao tác và sau lần quan sát lại: không có `error` hoặc `warning`.

## Ảnh quan sát đã chụp trong Chrome DevTools

Chrome DevTools đã chụp ảnh hiển thị trực tiếp ở các mốc bắt buộc:

1. Trước thao tác: danh sách có hai dòng riêng An Giang/Hà Nội cùng đợt, cả hai `Đã gửi TW`.
2. Tập chọn: chỉ An Giang được tick, nút `Tổng hợp (1)`.
3. Form tổng hợp: đúng đợt, kỳ và `Số đơn vị: 1`.
4. Ngay sau lưu: An Giang `Đã tổng hợp`, Hà Nội vẫn `Đã gửi TW`; toast được snapshot giữ nguyên văn.
5. Sau hard reload/mở lại: trạng thái vẫn đúng.
6. Comparator chưa gửi trước/sau: An Giang ở đợt đối chứng vẫn `Chờ duyệt`.
7. Nhật ký hệ thống: mục `Tổng hợp` đúng người, thời gian, entity và mã bản ghi.

## Dữ liệu bị thay đổi bởi lượt verify

- Bản ghi báo cáo Sở Tư pháp An Giang `b63fe4e2-0af5-4945-aeab-825814107209` của `DOT-TRON_NAM-2026-1`: `Đã gửi TW` -> `Đã tổng hợp`.
- Tạo bản ghi tổng hợp TW `04ae77a6-3c28-479c-98ce-a42154264828` / `TH-TW-1786121286031`.
- Bản ghi Hà Nội cùng đợt và báo cáo chưa gửi ở đợt đối chứng không đổi.

## Kết luận để cập nhật Sheet

`Trạng thái dev fix = Test done`.

`Kết quả verify`: **PASS - Danh sách đã tách đúng theo từng đơn vị. Khi chỉ chọn An Giang để tổng hợp, chỉ dòng được chọn chuyển sang Đã tổng hợp; Hà Nội cùng đợt không chọn vẫn Đã gửi TW, báo cáo chưa gửi vẫn Chờ duyệt và không xuất hiện. Hệ thống tạo đúng bản ghi TONG_HOP_TW, có nhật ký thao tác và hiển thị đúng "Đã tổng hợp báo cáo toàn quốc". Kết quả giữ nguyên sau reload.**
