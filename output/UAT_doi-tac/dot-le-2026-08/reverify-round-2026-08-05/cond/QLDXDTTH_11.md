# Bảng đối chiếu điều kiện — QLDXDTTH_11 (re-verify vòng 1, 05/08/2026)

Loại bug: **thiếu thao tác Tiếp nhận / Đánh dấu thực hiện cho cán bộ nghiệp vụ ở tab "Đề xuất đào tạo"** → phụ thuộc vai trò, đơn vị và trạng thái bản ghi ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 1*) CÓ khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy nguyên khối đó làm tiêu chí (Precondition / ✅ PASS khi / ❌ FAIL nếu / dòng ⚠️).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` — Cán bộ nghiệp vụ Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Chương trình đào tạo → tab "Đề xuất đào tạo" | Đào tạo, tập huấn → Chương trình đào tạo → tab **Đề xuất đào tạo** (đi bằng menu bên trái, không gõ địa chỉ) | Không |
| Tiền đề dữ liệu | Có ít nhất 1 đề xuất trạng thái "Mới gửi" **thuộc cùng đơn vị** của cán bộ | Trong kho **không còn đề xuất nào thuộc Cục Bổ trợ tư pháp** → đã TỰ TẠO: đăng nhập `nht_qa_tw` (Người hỗ trợ pháp lý, cùng đơn vị Cục Bổ trợ tư pháp) và gửi đề xuất **"QA-REVERIFY-0805..."** qua đúng biểu mẫu Gửi đề xuất mới → sinh 1 đề xuất "Mới gửi" đúng đơn vị | Không |
| Bước 1 | Đọc cột "Hành động" của dòng đề xuất "Mới gửi" cùng đơn vị | Đọc đúng dòng QA-REVERIFY-0805 (đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, trạng thái Mới gửi) ở cột **Hành động** | Không |
| Bước 2 | Mở màn chi tiết của chính đề xuất đó, đọc vùng thao tác | Mở chi tiết đề xuất đó, đọc toàn bộ vùng nút phía dưới thẻ thông tin | Không |
| Bước 3 | Thực hiện tiếp nhận đề xuất, rồi mở lại danh sách | Bấm **Tiếp nhận** → xác nhận trong hộp thoại → đọc lại trạng thái; sau đó **tải lại trang (bỏ bộ nhớ đệm)** rồi đọc lại | Không |
| Cách đo | Đối chiếu trạng thái trước/sau và độ bền của thay đổi | Ghi trạng thái trước (Mới gửi) và sau (Đã tiếp nhận), kiểm lại sau khi tải lại trang, kèm ảnh chụp màn từng mốc | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò và đơn vị mà phiếu yêu cầu, tiền đề còn thiếu đã tự tạo bằng luồng người dùng, chạy trọn tới bước sinh ra lỗi cũ (không chấm bằng quan sát tĩnh).

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw`)

### Bước 1 — cột "Hành động" trên danh sách

- ✅ **Không còn dấu gạch ngang** — dòng đề xuất "QA-REVERIFY-0805..." (Cục Bổ trợ tư pháp - Bộ Tư pháp, trạng thái **Mới gửi**) hiện nút **Tiếp nhận** ngay tại cột Hành động.
- ✅ Các đề xuất "Mới gửi" khác cũng có nút **Tiếp nhận**; đề xuất đã ở "Đã tiếp nhận" hiện nút **Đánh dấu thực hiện** — đúng bước tiếp theo của quy trình.
  Ảnh: [`../image/QLDXDTTH_11-r1-danh-sach-co-nut-tiep-nhan.png`](../image/QLDXDTTH_11-r1-danh-sach-co-nut-tiep-nhan.png)

### Bước 2 — màn chi tiết đề xuất

- ✅ **Không còn cảnh chỉ có nút quay lại** — màn chi tiết có đủ "Quay lại danh sách" **và** nút **Tiếp nhận**.
  Ảnh: [`../image/QLDXDTTH_11-r1-chi-tiet-co-nut-tiep-nhan.png`](../image/QLDXDTTH_11-r1-chi-tiet-co-nut-tiep-nhan.png)

### Bước 3 — thực hiện tiếp nhận

- ✅ Bấm **Tiếp nhận** → hệ thống hỏi lại *"Tiếp nhận đề xuất? Đề xuất sẽ chuyển sang trạng thái \"Đã tiếp nhận\"."* → xác nhận → báo **"Đã tiếp nhận đề xuất"**.
- ✅ **Trạng thái chuyển khỏi "Mới gửi"** → ô Trạng thái đổi thành **Đã tiếp nhận**, nút thao tác đổi thành **Đánh dấu thực hiện**.
- ✅ **Thay đổi còn nguyên sau khi tải lại trang** (đã tải lại bỏ bộ nhớ đệm): vẫn là **Đã tiếp nhận**. Đề xuất không còn đứng mãi ở "Mới gửi".
  Ảnh: [`../image/QLDXDTTH_11-r1-sau-tiep-nhan-da-tiep-nhan.png`](../image/QLDXDTTH_11-r1-sau-tiep-nhan-da-tiep-nhan.png)

### Ý note dặn KHÔNG chấm FAIL — tôn trọng

- ⚠️ Ý phụ "vai trò cán bộ có được phép GỬI đề xuất không" được note tách riêng và dặn không chặn phiếu này. Trên bản đang chạy, tài khoản cán bộ **không còn thấy nút "Gửi đề xuất mới"** ở tab này (nút chỉ hiện với vai trò Người hỗ trợ pháp lý) — dù sao cũng không dùng ý này để chấm phiếu.

### Kết luận

Cả ba bước của khối hướng dẫn nghiệm thu đều đạt: cán bộ có đường tiếp nhận ở cả danh sách lẫn màn chi tiết, tiếp nhận xong trạng thái chuyển đúng và giữ nguyên sau khi tải lại trang → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Số đề xuất đào tạo mà cán bộ Trung ương nhìn thấy nay chỉ còn **6** (trước khi kiểm thử tạo thêm), trong khi lần đo 04/08 là 16. Nhóm không còn hiển thị gồm cả các đề xuất trước đây bỏ trống người đề xuất lẫn hai đề xuất cũ nhất (11/05 và 25/05). Tài khoản quản trị cũng chỉ thấy đúng 6. Không thuộc phạm vi phiếu này, chỉ ghi lại.
- Dữ liệu do kiểm thử tạo: đề xuất **"QA-REVERIFY-0805 - de xuat dao tao cap TW de kiem chuc nang Tiep nhan cua can bo nghiep vu"** (người gửi: QA NHT Trung uong), nay đang ở trạng thái **Đã tiếp nhận** sau khi đo.
