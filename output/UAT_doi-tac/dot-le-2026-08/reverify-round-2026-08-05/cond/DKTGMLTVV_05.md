# Bảng đối chiếu điều kiện — DKTGMLTVV_05 (re-verify vòng 1, 05/08/2026)

Loại bug: **ràng buộc bắt buộc của ô "Bằng cấp / Chứng chỉ" + bước xác nhận khi gỡ tệp** → phụ thuộc vai trò, luồng nhập và dữ liệu hồ sơ ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 1*) CÓ khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy nguyên khối đó làm tiêu chí (Precondition / ✅ PASS khi / ❌ FAIL nếu / dòng ⚠️).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `nht_qa_tw` — vai trò Người hỗ trợ pháp lý | `nht_qa_tw` · họ tên "QA NHT Trung uong" · vai trò NHT · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → tab "Mới đăng ký" → Thêm mới | Đúng đường đó: tab **Mới đăng ký** → nút **Thêm mới** → màn "Thêm mới Tư vấn viên" | Không |
| Bước 1 — dữ liệu nhập | Điền đủ mọi trường bắt buộc khác, nạp File thẻ hành nghề ở nhóm 2, CỐ Ý để trống ô "Bằng cấp / Chứng chỉ" | Điền đủ: Loại TVV · Họ tên · Ngày sinh · Giới tính · Căn cước · Email · Điện thoại · Địa chỉ · Trình độ · Chuyên ngành · Số năm kinh nghiệm · Số thẻ hành nghề. Nạp tệp PDF vào **File thẻ hành nghề** ở nhóm "Thông tin nghề nghiệp". Nhóm "File đính kèm" **để trống** | Không |
| Bước 2 — gỡ tệp ở màn tạo mới | Nạp một tệp PDF vào ô "Bằng cấp / Chứng chỉ" → bấm Xóa | Nạp `qa-bang-cap-0805.pdf` vào ô đó rồi bấm **Xóa** ngay trên dòng tệp | Không |
| Bước 3 — gỡ tệp ở màn chỉnh sửa | Lặp bước 2 ở chế độ Chỉnh sửa một hồ sơ tư vấn viên đã lưu có sẵn tệp đính kèm | Ban đầu **không hồ sơ nào trong kho có tệp đính kèm** → đã TỰ TẠO hồ sơ **TVV-BTP-TW-0035** ("QA Reverify TVV 0805", Mới đăng ký) kèm 1 tệp PDF qua đúng luồng người dùng, rồi mở **Chỉnh sửa** hồ sơ đó để đo | Không |
| Cách đo kết quả chặn | Đọc thông báo hệ thống trả về khi bấm Lưu | Bắt thông báo ngay lúc nó hiện (không đọc muộn), đồng thời **đếm lại số hồ sơ tư vấn viên trước/sau khi bấm Lưu** để chắc chắn hồ sơ không được tạo | Không |
| Cách đo bước xác nhận | Xem có bước xác nhận trước khi tệp bị gỡ; hủy xác nhận thì tệp còn nguyên | Bấm Xóa → đọc nội dung hộp xác nhận → bấm **Hủy** → kiểm lại dòng tệp còn hay mất (cả 2 màn) + ảnh chụp màn | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò và đường đi của phiếu, chạy trọn cả 3 bước sinh ra lỗi cũ (không chấm bằng quan sát tĩnh), tiền đề còn thiếu đã tự tạo bằng luồng người dùng.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `nht_qa_tw`)

### Bước 1 — để trống "Bằng cấp / Chứng chỉ" rồi bấm Lưu

- ✅ **Hệ thống CHẶN** — bấm Lưu, màn hình đứng nguyên ở "Thêm mới Tư vấn viên", không chuyển sang danh sách.
- ✅ **Người dùng đọc được đúng lý do** — thông báo hiện: *"File đính kèm (Bằng cấp / Chứng chỉ) là bắt buộc khi đăng ký ứng viên mới"*. Thông báo nhắc đúng bằng cấp/chứng chỉ, không phải nhắc thẻ hành nghề.
- ✅ **Hồ sơ KHÔNG được tạo** — đếm lại số hồ sơ tư vấn viên trước và sau khi bấm Lưu đều là **39**, không phát sinh bản ghi nào.
  Ảnh: [`../image/DKTGMLTVV_05-r1-chan-luu-thieu-bang-cap.png`](../image/DKTGMLTVV_05-r1-chan-luu-thieu-bang-cap.png)

### Bước 2 — gỡ tệp ở màn Thêm mới

- ✅ **Có bước xác nhận** — nạp `qa-bang-cap-0805.pdf` rồi bấm **Xóa**: hệ thống mở hộp thoại *"Xác nhận xóa tệp — Bạn có chắc chắn muốn xóa tệp \"qa-bang-cap-0805.pdf\"?"* với hai nút **Hủy** / **Xóa**. Tệp chưa bị gỡ ở thời điểm đó.
- ✅ **Hủy xác nhận thì tệp còn nguyên** — bấm **Hủy**, hộp thoại đóng, dòng tệp `qa-bang-cap-0805.pdf` vẫn còn đủ tên và dung lượng.
  Ảnh: [`../image/DKTGMLTVV_05-r1-xac-nhan-xoa-tep-tao-moi.png`](../image/DKTGMLTVV_05-r1-xac-nhan-xoa-tep-tao-moi.png)

### Bước 3 — gỡ tệp ở màn Chỉnh sửa hồ sơ đã lưu

- ✅ Lưu hồ sơ có kèm tệp thành công → sinh hồ sơ **TVV-BTP-TW-0035**, trạng thái Mới đăng ký.
- ✅ **Có bước xác nhận** — mở **Chỉnh sửa** hồ sơ đó, bấm **Xóa** ở dòng tệp: hiện đúng hộp thoại *"Xác nhận xóa tệp"* kèm tên tệp.
- ✅ **Hủy xác nhận thì tệp còn nguyên** — bấm **Hủy**, tệp vẫn còn trong hồ sơ. Không còn cảnh tệp bị gỡ ngay không hỏi lại.
  Ảnh: [`../image/DKTGMLTVV_05-r1-xac-nhan-xoa-tep-chinh-sua.png`](../image/DKTGMLTVV_05-r1-xac-nhan-xoa-tep-chinh-sua.png)

### Ý note dặn KHÔNG chấm FAIL — tôn trọng

- ⚠️ Nhóm "File đính kèm" chỉ có **một** ô ("Bằng cấp / Chứng chỉ"), không có ô "Tệp thẻ hành nghề" — đúng như dặn dò của note (ô thẻ hành nghề nằm ở nhóm "Thông tin nghề nghiệp", đã kiểm và có thật, nạp tệp bình thường). Không dùng ý này để chấm phiếu.

### Kết luận

Cả ba bước của khối hướng dẫn nghiệm thu đều đạt: bỏ trống bằng cấp/chứng chỉ bị chặn kèm lý do đúng và hồ sơ không được tạo; gỡ tệp ở cả màn tạo mới lẫn màn chỉnh sửa đều phải qua bước xác nhận và hủy thì tệp còn nguyên → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Nhãn ô "File đính kèm (Bằng cấp / Chứng chỉ)" trên biểu mẫu **không có dấu sao đỏ** đánh dấu bắt buộc, dù hệ thống thực sự chặn khi để trống. Người nhập chỉ biết ô này bắt buộc sau khi bấm Lưu và bị báo lỗi. Chỉ ghi lại để đối tác/BA biết.
- Dữ liệu do kiểm thử tạo: hồ sơ **TVV-BTP-TW-0035** ("QA Reverify TVV 0805", Mới đăng ký) kèm 1 tệp PDF — tạo để có hồ sơ đã lưu có tệp đính kèm phục vụ bước 3, vì trong kho không có hồ sơ nào sẵn tệp.
