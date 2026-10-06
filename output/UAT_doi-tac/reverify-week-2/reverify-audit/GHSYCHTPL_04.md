# Audit verify GHSYCHTPL_04

> **KHÔNG DÙNG ĐỂ CHỐT VERDICT.** Đây là lượt DEV cũ, đã bị thay thế bởi
> `GHSYCHTPL_04-UAT-2026-08-12.md` theo yêu cầu verify lại từ đầu trên UAT.
> Lượt cũ còn có sai số đơn vị: `135071 KB` tương đương khoảng **131,9 MB**,
> không phải 13,2 MB. File đối tác vi phạm cả định dạng và giới hạn 20MB/tệp.

## Cổng 1 — Bằng chứng đối tác

- Đã xem toàn bộ video full-res `partner-evidence/GHSYCHTPL_04.webm` (1920×1080, 20.633 giây).
- Frame lỗi ở khoảng `00:19–00:20`: sau khi chọn tệp `CNKQHT_07.webm` dung lượng `135071 KB`, trang Cổng Pháp luật Quốc gia chuyển sang màn trình duyệt `This page couldn’t load`.
- Neo URL: `uat.phapluat.gov.vn/danh-sach-vu-viec-vuong-mac-phap-ly`.
- Neo trạng thái: người dùng đang đăng nhập, modal gửi hồ sơ đang mở; upload đang ở trạng thái `Đang tải lên...` trước khi trang lỗi.
- Dữ liệu tiền đề: tệp `.webm` sai định dạng; dung lượng khoảng 13.2MB, dưới trần 20MB/tệp.

## Cổng 2 — Hiểu bug

- Đối tác phản ánh thao tác đính kèm tệp vi phạm giới hạn làm hỏng toàn trang thay vì từ chối tệp và hiển thị thông báo cụ thể.
- Claim cần kiểm là validation ngay lúc chọn tệp `.webm`, không phải submit tạo hồ sơ.
- Lượt live dùng DN `0109998887` trên môi trường được giao, mở `Vụ việc HTPL` → `Gửi yêu cầu hỗ trợ pháp lý`, chọn loại giấy tờ `Khác`, rồi upload chính file evidence `.webm`.

## Cổng 3 — Đối chiếu SRS với web

| SRS yêu cầu | Thực tế web hiện tại | Đủ/thiếu |
|---|---|---|
| FR-V.I-02 (UC52), dòng 185: chỉ nhận PDF/DOC/DOCX/XLS/XLSX/JPG/PNG; tối đa 20MB/tệp, tổng 100MB, 10 tệp. | `.webm` bị từ chối ngay ở client. | Đủ |
| Error Handling E4, dòng 215: file vi phạm phải trả lỗi về dung lượng/số lượng/định dạng. | Toast hiển thị `GHSYCHTPL_04.webm: Định dạng không được hỗ trợ. Chấp nhận: .pdf, .doc, .docx, .xls, .xlsx, .jpg, .png`. | Đủ |
| SCR-V.I-02 dòng 1695: khu vực upload công bố đúng định dạng và trần 20MB/tệp. | UI hiển thị đúng danh sách định dạng, tối đa 10 tệp và 20MB/tệp. | Đủ |

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|---|
| Vai trò / đăng nhập | Người dùng đã đăng nhập trên chuyên trang và mở form gửi hồ sơ | DN `0109998887`, role Doanh nghiệp, đã đăng nhập bằng OTP Gmail thật | Không |
| Hành động | Chọn tệp tại khu vực tài liệu đính kèm của form gửi hồ sơ | Chọn tệp tại `Vụ việc HTPL` → `Gửi yêu cầu hỗ trợ pháp lý` → loại giấy tờ `Khác` | Không |
| Quy tắc bị vi phạm | Tệp `.webm`, 13.2MB: sai định dạng, không vượt 20MB | Chính file evidence `GHSYCHTPL_04.webm`, 4.9MB: sai định dạng, không vượt 20MB | Không — cùng nhánh validation sai định dạng |

## Gate real-data

- Artifact live: `GHSYCHTPL_04-repeat-immediate.png`; form vẫn mở sau validation.
- Bộ bắt thông báo chuẩn tự kiểm đúng `1` observer.
- Lượt xác nhận độc lập: `SO_REQUEST=0`; `SO_KHUNG_THONG_BAO=1`; toast nêu đúng tên file, sai định dạng và danh sách định dạng được chấp nhận; `dialogExists=true`; URL không đổi.
- Không phát sinh hồ sơ mới vì thao tác bị chặn trước request.
- Lượt chụp full-page đầu làm modal biến mất trong artifact `GHSYCHTPL_04-after-invalid-upload.png`; lặp lại bằng viewport bình thường không tái hiện, nên không log đây là bug ứng dụng.
- Ngoài tiêu chí BA: không phát hiện thêm bất thường có thể tái hiện độc lập.

## Verdict

- `Resolved`: đối tác có video lỗi thật trên build/môi trường trước, nhưng bản hiện tại không tái hiện; validation hoạt động đúng và không làm hỏng trang.
