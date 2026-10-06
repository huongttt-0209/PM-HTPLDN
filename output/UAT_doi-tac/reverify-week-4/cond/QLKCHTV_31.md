# Bảng đối chiếu điều kiện — QLKCHTV_31 (row 15) — Không cảnh báo khi thay thế nội dung trả lời đã soạn

**Kết luận:** BA confirm.
- Hiện tượng **tái hiện đúng và đo được 2 lần**: khi ô "Nội dung trả lời" đã có chữ do cán bộ tự soạn, bấm [Chọn] ở một câu hỏi khác trong kho thì nội dung cũ **bị ghi đè ngay, không có hộp thoại xác nhận nào**, không có thông báo nào.
- Nhưng đặc tả v3.5 **không có yêu cầu cảnh báo** này: `srs-fr-13-tv-nhanh.md:572` chỉ ghi *"Click [Chon] -> copy `cau_tra_loi` vao o soan"*; FR-X.2-02 bước 6 (`:201`) cũng chỉ ghi *"CB NV chọn một Q&A phù hợp -> copy `cau_tra_loi` vào ô soạn; CB NV được chỉnh sửa trước khi gửi"*.
- Rủi ro mất công soạn của cán bộ là có thật ⇒ chuyển BA chốt (BA-11) thay vì chấm lỗi spec.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_31.jpg` + `.webm`, 5 frame ở `reverify-audit/QLKCHTV_31/frames/`) | Mình test (env nip.io, 27/07/2026 11:58) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW (đọc rõ ở frame t006, t009) | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Phiên `2f144009-…` đang ở màn trả lời, chế độ nhập liệu; kết quả tra cứu có ≥2 câu hỏi | Phiên `TVN-20260727-0001` (trạng thái "CB trả lời") ở màn trả lời, chế độ nhập liệu; kết quả tra cứu **4 câu hỏi** | Không |
| Dữ liệu tiền đề | Ô trả lời **đã có nội dung tùy chỉnh**: frame t006 đo được **371 ký tự** = nội dung câu hỏi kho thứ nhất + đoạn cán bộ tự gõ thêm ("tkm test") | Ô trả lời **đã có nội dung tùy chỉnh**, đo 2 lần: lần 1 = **128 ký tự** (nội dung kho + đoạn tự soạn "[QA TỰ SOẠN THÊM …]"); lần 2 = **94 ký tự** (**hoàn toàn** do cán bộ tự gõ, không lấy từ kho) | Không |
| Input / filter / giá trị nhập | Bấm [Chọn] ở thẻ kết quả **khác** (`QA-20260508-0002`) | Lần 1: bấm [Chọn] ở `QA-20260706-0002`. Lần 2: bấm [Chọn] ở `QA-20260707-0006`. **Bổ sung** so với đối tác: lần 2 dùng nội dung 100% tự soạn để loại trừ lập luận "chữ đó vốn là của kho nên ghi đè là đúng" | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hành vi)

Đo bằng bộ bắt thông báo dùng chung (`tools/toast-capture.js`), đã tự kiểm trước khi đo: **`soObserverDangSong = 1`** ⇒ số liệu hợp lệ.

- **Lần 1** — trước: 128 ký tự (có đoạn "[QA TỰ SOẠN THÊM …]") → sau: 53 ký tự (chỉ nội dung câu hỏi mới). Mất đoạn tự soạn: **Có**. Hộp thoại xác nhận: **0**. Thông báo: 1 (xem ghi chú cuối mục). Lần gọi máy chủ: 0.
- **Lần 2** — trước: 94 ký tự (100% tự soạn) → sau: 5.007 ký tự (chỉ nội dung câu hỏi mới). Mất đoạn tự soạn: **Có**. Hộp thoại xác nhận: **0**. Thông báo: **0**. Lần gọi máy chủ: 0.

> **Ghi chú trung thực về thông báo ở lần 1:** bộ đo bắt được 1 khung chữ *"Lỗi máy chủ, vui lòng thử lại sau."*. Đã truy tầng mạng: khung này đến từ `GET /api/v1/thong-baos/unread-count` trả **502** — là lời gọi nền đếm thông báo chưa đọc, **không liên quan** thao tác [Chọn] (thao tác [Chọn] không gọi máy chủ lần nào). Gọi lại 3 lần sau đó đều **200** ⇒ trục trặc hạ tầng thoáng qua. **Không tính là lỗi**, và lần đo thứ 2 chạy sạch với 0 thông báo.

## Phương pháp thứ hai (bắt buộc)

- **Đo lại lần 2 với nội dung 100% tự soạn** (nêu ở bảng trên) — đây là phép thử quyết định: nếu hệ thống có bất kỳ cơ chế bảo vệ nào cho chữ do người dùng gõ thì phải kích hoạt ở tình huống này. Kết quả: **0 hộp thoại, 0 thông báo**, chữ tự soạn biến mất hoàn toàn.
- **Kiểm tra bằng lớp DOM thay vì chỉ nhìn màn:** đếm `.ant-modal-wrap` đang hiển thị và `.ant-modal-confirm` ngay sau khi bấm → **0** ở cả hai lần. Loại trừ khả năng "hộp thoại có hiện nhưng tự tắt quá nhanh".
- **Đối chứng bằng video của đối tác:** frame `t006.06s.jpg` → ô trả lời **371 ký tự** (có đoạn tự gõ "tkm test"); frame `t009.06s.jpg` (sau khi bấm [Chọn] thẻ khác) → ô trả lời còn **119 ký tự**, đúng bằng nội dung câu hỏi mới, đoạn tự gõ đã mất. Trùng khớp với kết quả đo trên nip.io.
- **Tra nguyên văn câu cảnh báo trong đặc tả:** đã tìm toàn bộ `srs-v3.5/` cụm *"Bạn đang thay thế"* và các biến thể → **0 kết quả**. Câu mà phiếu test nêu (*"Bạn đang thay thế nội dung trả lời đã soạn. Tiếp tục?"*) không tồn tại trong đặc tả v3.5.
- **Đối chiếu quy ước toàn hệ thống:** quy ước UI-08 (`srs-v3.5.md:577`) có yêu cầu hỏi xác nhận, nhưng phạm vi là *"khi người dùng **rời hoặc hủy** một form đang nhập dở"* — không phủ tình huống ghi đè một ô ngay trong form. Vì vậy không thể dựa vào UI-08 để chấm lỗi; cần BA mở rộng quy ước hoặc bổ sung yêu cầu riêng cho màn này.
