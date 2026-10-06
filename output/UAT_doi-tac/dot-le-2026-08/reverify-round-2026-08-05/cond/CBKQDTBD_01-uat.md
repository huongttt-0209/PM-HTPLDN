# CBKQDTBD_01 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối từ cột `DEV phản hồi lần 2` của chính dòng 121 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`),
không tự đặt thêm.

| Điều kiện | Bug gốc (khối tiêu chí cột Y) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — bundle `assets/index-Dn5IWt_M.js`, nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | Cán bộ nghiệp vụ | `cbnv_tw` · CB_NV_TW · `donViId 00000000-0000-4000-8000-000000000001` · cấp TW | Không |
| Màn hình | Chi tiết khóa học → tab riêng "Công bố kết quả" | Tab "Công bố kết quả" có thật, mở được | Không |
| Khóa học tiền đề | Khóa đã Hoàn thành, có học viên đã chấm kết quả | `KH-20260703-005` — Hoàn thành, 2 học viên (5.0 Đạt · 10.0 Không đạt) | Không |
| Khóa đối chứng trạng thái khác | Khóa chưa Hoàn thành để kiểm phần chặn | `KH-20260722-002` — Đang diễn ra | Không |
| Thao tác đo | Bấm thật trên giao diện | Toàn bộ thao tác bấm trên màn; thông báo bắt bằng bộ theo dõi DOM không lọc trùng (tự kiểm `soObserverDangSong = 1`) | Không |
| Trả lại dữ liệu | — | Sau khi đo đã hủy công bố cả khóa, hai học viên về lại "Chưa công bố" như trước | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- Ý 1 · tích chọn một học viên rồi bấm công bố cho phần đã chọn: tích dòng "Hoàng Minh Đức" → nút đổi thành
  `Công bố đã chọn (1)` → xác nhận → **chỉ** dòng đó sang "Đã công bố" (`05/08/2026 14:39`), dòng "tester tkm"
  giữ nguyên "Chưa công bố / —".
- Ý 2 · nút "Công bố"/"Hủy" ở cột Hành động của từng học viên: bấm được ở cả hai dòng, chạy đúng; rà toàn trang
  không còn chuỗi "sẽ khả dụng khi hệ thống hỗ trợ", cũng không còn ở thuộc tính chú thích của nút.
- Ý 3 · ô tích chọn và hai nút thao tác: ô tích từng dòng và ô chọn tất cả đều có tác dụng; số trong ngoặc chạy
  đúng theo số đang chọn; hai nút tự bật/tắt theo trạng thái của chính các dòng đang chọn — chọn dòng đã công bố
  thì `Công bố đã chọn (0)` tắt còn `Hủy công bố đã chọn (1)` bật, và ngược lại.
- Ý 4 · sau khi hủy công bố, cột "Thời điểm công bố" xóa về dấu gạch ngang: công bố "Hoàng Minh Đức" lúc 14:36
  rồi hủy → ô về "—" ngay. Dòng "tester tkm" ban đầu còn giữ mốc cũ `04/08/2026 16:47` dù đang "Chưa công bố";
  chạy lại một lượt công bố rồi hủy trên chính dòng đó thì mốc cũng về "—" ⇒ giá trị cũ là dữ liệu đóng băng từ
  trước bản sửa, không phải lỗi còn lại.
- Ý 5 · công bố cả khóa → hủy công bố cả khóa → công bố lại: cả ba lượt đều chạy, không lượt nào bị chặn vì
  "đang có yêu cầu chờ xử lý".
- Ý 5 (phần giữ nguyên) · yêu cầu nhập lý do hủy: bấm xác nhận khi bỏ trống bị chặn với lời nhắc
  "Vui lòng nhập lý do", không có lượt gọi nào tới máy chủ.
- Ý 5 (phần giữ nguyên) · chặn khi khóa chưa Hoàn thành: mở `KH-20260722-002` (Đang diễn ra) → dải chữ
  "Chưa thể công bố kết quả — Chỉ có thể công bố/hủy công bố kết quả khi khóa học đã ở trạng thái Hoàn thành",
  cả bốn nút thao tác đều tắt.
- Số lượt gọi máy chủ và số khung thông báo khớp 1–1 ở mọi thao tác, không có thông báo lặp.

Ảnh: `../image/CBKQDTBD_01-uat-cong-bo-rieng-1-hoc-vien.png` ·
`../image/CBKQDTBD_01-uat-chan-khi-khoa-chua-hoan-thanh.png`

## Ghi nhận thêm — NGOÀI phạm vi phiếu, không chấm là lỗi ở đây

Khóa `KH-HDSD-AG-003` (thuộc đơn vị An Giang, `donViId 00000000-0000-4000-8002-000000000006`) mở và xem được
đầy đủ bằng tài khoản cấp Trung ương, nhưng khi bấm hủy công bố thì máy chủ trả về "Khóa học không tồn tại"
(`ERR-VAL-III-04-01`, HTTP 404) trong khi bản ghi vẫn tồn tại và đang ở trạng thái Hoàn thành. Cùng thao tác
trên khóa thuộc đơn vị của chính tài khoản thì chạy bình thường ⇒ nhiều khả năng là ràng buộc phạm vi đơn vị
nhưng báo sai bản chất (nói không tồn tại thay vì nói không có quyền). Điểm này nằm ngoài mọi ý của khối tiêu
chí phiếu CBKQDTBD_01 nên không tính vào kết luận; đề nghị báo lại để BA/Dev quyết có tách phiếu riêng không.
