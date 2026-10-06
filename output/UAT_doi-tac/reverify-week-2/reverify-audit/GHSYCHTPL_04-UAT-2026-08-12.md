# Audit verify lại UAT — GHSYCHTPL_04 — 12/08/2026

## Kết luận

- Verdict mới trên UAT: `Resolved` (giữ `Trạng thái dev fix = reject`).
- Bỏ hoàn toàn kết quả DEV cũ và chạy lại từ đầu trên `https://htpldn-uat.ospgroup.vn`.
- Lỗi đối tác có bằng chứng thật nhưng không còn tái hiện trên UAT: cả nhánh sai định dạng và nhánh vượt 20MB/tệp đều bị chặn trước khi tải lên, có thông báo cụ thể, form và trang vẫn hoạt động.

## Cổng 1 — Bằng chứng đối tác

- Đã lấy lại evidence bằng `UAT_TAB=bug python3 output/UAT_doi-tac/tools/fetch_evidence.py --row 383` và xem video full-res `partner-evidence/GHSYCHTPL_04.webm` (1920×1080, 20.633 giây).
- Frame lỗi `00:16`: form gửi hồ sơ đang tải tệp `CNKQHT_07.webm (135071 KB)`.
- Frame lỗi `00:19–00:20`: toàn trang chuyển sang `This page couldn’t load` thay vì từ chối tệp và báo lỗi.
- Neo URL: `uat.phapluat.gov.vn/danh-sach-vu-viec-vuong-mac-phap-ly`.
- Neo trạng thái: người dùng đã đăng nhập, modal gửi hồ sơ đang mở, tệp đang ở trạng thái `Đang tải lên...` trước khi trang lỗi.
- Dữ liệu tiền đề chính xác: `CNKQHT_07.webm`, 135.071 KB = khoảng 131,9 MB. Tệp vi phạm đồng thời định dạng cho phép và trần 20MB/tệp.

## Cổng 2 — Hiểu bug và cách tái hiện

- Đối tác phản ánh: khi chọn tệp vi phạm constraint, hệ thống không hiển thị cảnh báo cụ thể mà làm hỏng toàn trang.
- Claim cần kiểm: validation ngay lúc chọn tệp, trước khi gửi hồ sơ.
- Tài khoản UAT: `0151554887`, vai trò `Doanh nghiệp`, tên hiển thị `Tester TKM`, doanh nghiệp `TKM Company`; OTP lấy từ MailHog UAT theo cấu hình môi trường.
- Surface live: `Vụ việc HTPL` → `Gửi yêu cầu hỗ trợ pháp lý` → `Loại giấy tờ = Khác` → khu vực tải tệp.
- Lượt A khớp evidence: tạo tệp `CNKQHT_07.webm` đúng 138.312.704 byte = 135.071 KiB, giữ phần đầu video evidence và mở rộng kích thước.
- Lượt B tách riêng rule dung lượng: dùng `input/test-files/hd-file-dinh-kem-21mb-REJECT.pdf`, 22.020.094 byte, đúng định dạng PDF nhưng vượt 20MB.

## Cổng 3 — SRS so với web UAT

| SRS yêu cầu | Thực tế UAT 12/08/2026 | Đủ/thiếu |
|---|---|---|
| FR-V.I-02 (UC52), dòng 185: chỉ nhận PDF/DOC/DOCX/XLS/XLSX/JPG/PNG; tối đa 20MB/tệp, tổng 100MB, tối đa 10 tệp. | UI công bố đúng 7 định dạng, 20MB/tệp, tối đa 10 tệp. | Đủ |
| FR-V.I-02 Error Handling E4, dòng 215: tệp vi phạm constraint phải trả lỗi dung lượng/số lượng/định dạng. | `.webm` bị chặn với thông báo nêu sai định dạng và danh sách được chấp nhận; PDF 22.020.094 byte bị chặn với thông báo nêu vượt 20MB. | Đủ |
| SCR-V.I-02 dòng 1695: upload nhiều tệp, tối đa 20MB/tệp, tổng 100MB, tối đa 10; định dạng PDF/DOC/DOCX/XLS/XLSX/JPG/PNG. | Khu vực tải tệp hiển thị đúng định dạng, số lượng và trần từng tệp; hai input vi phạm đều không được thêm vào danh sách. | Đủ |

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res) | Mình test trên UAT | GAP? |
|---|---|---|---|
| Vai trò / đăng nhập | Người dùng đã đăng nhập trên chuyên trang, mở form gửi hồ sơ | DN `0151554887`, vai trò `Doanh nghiệp`, đã đăng nhập UAT bằng OTP | Không |
| Surface / hành động | Modal gửi hồ sơ, chọn tệp ở mục tài liệu đính kèm | `Vụ việc HTPL` → `Gửi yêu cầu hỗ trợ pháp lý` → `Loại giấy tờ = Khác` → chọn tệp | Không — UAT có thêm trường loại giấy tờ để bật upload, không đổi rule định dạng/dung lượng |
| Input khớp evidence | `CNKQHT_07.webm`, 135.071 KB, sai định dạng và vượt 20MB | `CNKQHT_07.webm`, đúng 135.071 KiB, sai định dạng và vượt 20MB | Không |
| Rule dung lượng độc lập | File đối tác đồng thời vượt 20MB nên nhánh định dạng có thể chặn trước | PDF hợp lệ 22.020.094 byte, chỉ vi phạm trần 20MB | Không — đã tách và đo riêng nhánh dung lượng |

## Gate real-data

- Chỉ dùng `output/UAT_doi-tac/tools/toast-capture.js`; self-check `soObserverDangSong=1`.
- Lượt A, input khớp evidence:
  - `SO_REQUEST=0`.
  - `SO_KHUNG_THONG_BAO=1`, không lặp.
  - Nội dung: `CNKQHT_07.webm: Định dạng không được hỗ trợ. Chấp nhận: .pdf, .doc, .docx, .xls, .xlsx, .jpg, .png`.
  - Ảnh đã mở đọc: `GHSYCHTPL_04-UAT-exact-invalid-toast.png`.
- Lượt B, tách rule dung lượng:
  - `SO_REQUEST=0`.
  - `SO_KHUNG_THONG_BAO=1`, không lặp.
  - Nội dung: `GHSYCHTPL_04-size-21mb.pdf: Kích thước vượt quá giới hạn 20MB.`
  - Ảnh đã mở đọc: `GHSYCHTPL_04-UAT-size-invalid-toast.png`.
- Cả hai lượt: modal vẫn mở, URL vẫn là `/vu-viec/danh-sach`, trang không crash, không thêm tệp vào form, không tạo hồ sơ.
- Phương pháp xác nhận thứ hai: ảnh pixel full-res của hai toast trùng với dữ liệu observer; không có mâu thuẫn giữa phép đo DOM và hình người dùng thấy.
- Ngoài tiêu chí BA: không phát hiện thêm bất thường có thể tái hiện độc lập.

## Các bước re-verify sau này

1. Đăng nhập đúng tài khoản DN trên UAT, vào `Vụ việc HTPL` → `Gửi yêu cầu hỗ trợ pháp lý`.
2. Chọn `Loại giấy tờ = Khác` để bật khu vực tải tệp.
3. Chọn tệp `.webm` dung lượng 135.071 KB. Đạt khi tệp bị chặn ngay, có thông báo sai định dạng kèm danh sách định dạng cho phép, trang/form không bị đóng hoặc crash.
4. Chọn một tệp PDF lớn hơn 20MB. Đạt khi tệp bị chặn ngay, có thông báo vượt giới hạn 20MB, trang/form vẫn hoạt động.
5. Với mỗi lượt, bộ bắt thông báo phải tự kiểm bằng 1 observer; kỳ vọng 0 request upload và đúng 1 toast.

## Verdict

- `Resolved`: đối tác có video lỗi thật trên portal/build cũ, nhưng UAT hiện tại không tái hiện; validation đúng SRS và không làm hỏng trang.
