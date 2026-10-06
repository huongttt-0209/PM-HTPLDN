# Bảng đối chiếu điều kiện — TKCHTV_02 (row 25) — Tìm kiếm không có kết quả

**Kết luận:** Open (Minor) + BA confirm.

Phiếu nêu 1 vế ở cột "Kết quả thực tế" và 2 vế ở cột "Kết quả mong đợi". Đo tách bạch:

- **Vế đối tác phản ánh** — *"Kho câu hỏi: nhập từ khóa không có kết quả nhưng hệ thống hiển thị toàn bộ bản ghi hiện có"* → **KHÔNG tái hiện**. Gõ chuỗi vô nghĩa `abcdxyzqwerty` trên kho 14 câu hỏi → bảng còn **0 dòng**, không còn hiện tượng trả về tất cả. Phần dữ liệu đã đúng.
- **Vế câu chữ** — phiếu mong *"Không tìm thấy câu hỏi phù hợp"* (Kho câu hỏi) và *"Không tìm thấy phiên tư vấn phù hợp"* (Tư vấn nhanh) → **không đạt**. Hệ thống hiện *"Chưa có câu hỏi nào."* và *"Không có phiên tư vấn nhanh nào."* — cả hai đều là câu dành cho trường hợp **chưa có dữ liệu**, trong khi kho đang có 14 câu hỏi và 4 phiên. → lỗi `BUG-TK-THONG-DIEP-RONG`.

Chấm **Open** mức Minor cho phần câu chữ (nói sai sự thật với người dùng), kèm **BA confirm** vì đặc tả nhóm X.2 chưa quy định câu thông báo cho **màn danh sách** — xem BA-17.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/TKCHTV_02(1)-1.jpg`, `TKCHTV_02(1)-2.jpg`) | Mình test (env nip.io, 27/07/2026 14:10–14:35) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ theo cột Tác nhân của phiếu; ảnh chụp màn quản trị Kho câu hỏi và Tư vấn nhanh | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Nằm trong tập tác nhân phiếu ghi | Không |
| Entity + trạng thái (state machine) | Ảnh 1: Kho câu hỏi `?search=abcdxyz`, toàn bộ 44 bản ghi vẫn hiện. Ảnh 2: Tư vấn nhanh `?search=abcxyz`, bảng rỗng kèm chữ "Không có phiên tư vấn nhanh nào." | Kho câu hỏi 14 bản ghi, Tư vấn nhanh 4 phiên. Cả hai ở thẻ "Tất cả", không đặt bộ lọc phụ | Không |
| Dữ liệu tiền đề | Phiếu yêu cầu "Không tồn tại bản ghi phù hợp với tiêu chí tìm kiếm" — đối tác dùng chuỗi vô nghĩa `abcdxyz` / `abcxyz` | Dùng chuỗi vô nghĩa cùng kiểu `abcdxyzqwerty` trên cả hai màn. Đã xác nhận trước đó rằng danh sách KHÔNG rỗng (14 và 4 dòng) để phân biệt "không khớp" với "không có dữ liệu" | Không |
| Input / filter / giá trị nhập | Gõ chuỗi vô nghĩa vào ô tìm kiếm rồi kích hoạt tìm | Gõ vào đúng ô tìm kiếm của từng màn rồi bấm nút tìm của màn đó. Sau khi đọc kết quả, xóa từ khóa để xác nhận dữ liệu vẫn nguyên | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/thông báo)

- `partner-evidence/TKCHTV_02(1)-1.jpg` — đã mở đọc: Kho câu hỏi, địa chỉ `?search=abcdxyz`, bảng vẫn liệt kê đủ 44 bản ghi. Đây là hiện tượng đối tác phản ánh, và là thứ **không còn** trên bản hiện tại.
- `partner-evidence/TKCHTV_02(1)-2.jpg` — đã mở đọc: Tư vấn nhanh, địa chỉ `?search=abcxyz`, bảng rỗng, chữ hiển thị đúng là *"Không có phiên tư vấn nhanh nào."* — trùng khít với chữ đo được trên bản hiện tại.
- `bug-reports/image/BUG-TK-tim-khong-ket-qua-bao-chua-co-cau-hoi-nao.png` — đã mở đọc: Kho câu hỏi, ô tìm kiếm `abcdxyzqwerty`, bảng 0 dòng, chữ *"Chưa có câu hỏi nào."*, không có nút gợi ý xóa bộ lọc.
- `bug-reports/image/BUG-TK-tv-nhanh-tim-dung-ma-phien-ra-0.png` — đã mở đọc: Tư vấn nhanh, bảng 0 dòng, chữ *"Không có phiên tư vấn nhanh nào."*.

## Phương pháp thứ hai (bắt buộc)

- **Đọc chuỗi hiển thị thay vì mô tả cảm nhận.** Lấy trực tiếp chữ trong vùng bảng để tránh diễn giải sai: Kho câu hỏi trả về đúng chuỗi `"Chưa có câu hỏi nào."`, Tư vấn nhanh trả về đúng chuỗi `"Không có phiên tư vấn nhanh nào."`. Không màn nào kèm nút hay gợi ý thao tác tiếp theo.
- **Phép thử phân biệt "không khớp" với "không có dữ liệu" — đây là điểm mấu chốt.** Trước khi tìm, ghi nhận Kho câu hỏi 14 dòng và Tư vấn nhanh 4 dòng. Sau khi tìm chuỗi vô nghĩa, cả hai về 0 dòng kèm câu thông báo trên. Xóa từ khóa thì danh sách trở lại đủ 14 và 4 dòng. ⇒ Dữ liệu vẫn nguyên vẹn, chỉ có câu thông báo mô tả sai tình huống.
- **Kiểm chéo bằng đường khác giao diện** để chắc chắn phần dữ liệu đã đúng: gọi thẳng dịch vụ dữ liệu với `abcdxyzqwerty` — Kho câu hỏi trả 0 bản ghi, Tư vấn nhanh trả 0 bản ghi. Trùng với giao diện ⇒ hiện tượng "hiển thị toàn bộ bản ghi" mà đối tác phản ánh đã hết thật, không phải trùng hợp lúc chụp màn.
- **Đối chiếu đặc tả — trích nguyên văn, và nêu rõ giới hạn của căn cứ:** `srs-fr-13-tv-nhanh.md:225` (FR-X.2-02, bảng Error Handling, dòng E2): *"| E2 | Không có kết quả tìm kiếm | INF-TVN-TK-01 | **\"Không tìm thấy câu hỏi phù hợp\"** | INFO |"*, lặp lại ở `:349` (FR-X.2-04). Tuy nhiên hai dòng này thuộc **màn tra cứu kho trong lúc trả lời phiên** và **màn chuyên trang doanh nghiệp**, không phải màn danh sách quản trị đang test. Phần mô tả màn danh sách (`:530`, `:568`) không quy định câu thông báo khi rỗng ⇒ QA không quy kết vi phạm trực tiếp, mà gửi BA-17.
- **Đối chiếu quy ước toàn hệ thống (căn cứ mạnh nhất):** `srs-fr-02-hoi-dap.md:1047` tách rõ 5 biến thể trạng thái trống, trong đó biến thể (1) *"Chưa có hỏi đáp nào"* dùng khi **không có dữ liệu**, biến thể (4) *"Không tìm thấy hỏi đáp phù hợp với bộ lọc. [Xóa bộ lọc]"* dùng khi **lọc không khớp**. Hệ thống đang dùng câu kiểu (1) cho tình huống kiểu (4).
- **Kiểm cụm chữ đối tác mong đợi:** cụm *"Không tìm thấy phiên tư vấn phù hợp"* **không xuất hiện ở bất kỳ dòng nào trong SRS v3.5** — là chữ đối tác tự đặt, nên không lấy làm chuẩn để chấm. Đã ghi vào BA-17 để BA chốt câu chính thức.
