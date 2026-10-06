# Bảng đối chiếu điều kiện — QLKCHTV_32 (row 16) — Bấm mã câu trả lời không mở cửa sổ chi tiết

**Kết luận:** BA confirm.
- Hiện tượng **tái hiện đúng**: mã câu hỏi trong kết quả tra cứu là chữ thường, **không bấm được**; bấm 1 lần và bấm đúp đều không mở cửa sổ nào.
- Nhưng đặc tả v3.5 **không quy định hành vi bấm vào mã**: `srs-fr-13-tv-nhanh.md:572` chỉ liệt kê *thành phần hiển thị* của mỗi kết quả — *"Moi ket qua: Ma Q&A / Cau hoi (bold) / Cau tra loi rut gon / Linh vuc / Tu khoa / Diem relevance (%) / [Chon]"* — và hành vi duy nhất được mô tả là *"Click [Chon] -> copy `cau_tra_loi` vao o soan"*. Không có mục nào nói mã Q&A mở cửa sổ chi tiết, cũng không có nút [Đóng] nào cho cửa sổ đó.
- Ghi nhận thêm: phần lớn thông tin mà phiếu test muốn xem trong "cửa sổ chi tiết" **đã hiển thị sẵn ngay trên thẻ kết quả** (xem phần đo bên dưới) ⇒ BA cần chốt có thực sự cần cửa sổ riêng không (BA-12).

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_32.webm`, 3 frame ở `reverify-audit/QLKCHTV_32/frames/`) | Mình test (env nip.io, 27/07/2026 11:57) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW (đọc rõ frame t003) | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Phiên `TVN-QA-20260422-0025`, trạng thái **"Đã gợi ý"**, đang ở màn trả lời; đã tra cứu ra ≥3 kết quả | Phiên `TVN-20260727-0001`, trạng thái **"CB trả lời"**, đang ở màn trả lời; đã tra cứu ra **4 kết quả**. Cột phải là thành phần của *"mode tra loi"* (`:572`), giống nhau ở cả 2 trạng thái | Không |
| Dữ liệu tiền đề | Kho câu hỏi có bản ghi khớp từ khóa "lao động" | Kho câu hỏi có **9 bản ghi Đã duyệt + còn hiệu lực**; tra từ khóa **"đăng ký kinh doanh"** ra 4 kết quả (từ khóa "lao động" không khớp bản ghi đã duyệt nào trên môi trường này nên đổi từ khóa — điều kiện tương đương: "có ≥1 kết quả tra cứu") | Không |
| Input / filter / giá trị nhập | Bấm (và bấm đúp) vào mã `QA-20260525-0001` trong thẻ kết quả — frame t003 cho thấy phần "0001" bị bôi đen do bấm đúp | Bấm 1 lần **và** bấm đúp vào mã `QA-20260706-0001`. **Bổ sung** kiểm tra cấu trúc phần tử để loại trừ "có bấm được nhưng lỗi tạm thời" | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hành vi + Hiển thị/render)

- `bug-reports/image/BUG-TVN-ket-qua-tra-cuu-ma-khong-bam-duoc.png` — đã mở đọc: 3 thẻ kết quả, mã (`QA-20260706-0001`, `QA-20260706-0002`, `QA-20260707-0001`) hiện bằng **chữ xám mờ**, không gạch chân, không màu liên kết.
- Đo cấu trúc phần tử của cả 4 mã bằng mã lệnh:
  - thẻ HTML = `SPAN`, lớp `ant-typography ant-typography-secondary`
  - `cursor = "auto"` (không phải `pointer`)
  - `href = null`, `role = null`, không gắn hàm xử lý bấm
  - phần tử cha cũng `cursor = "auto"`, không gắn hàm xử lý bấm
- Đo hành vi (bấm 1 lần → chờ 1,2s → bấm đúp → chờ 1,5s):
  - số cửa sổ/ngăn kéo đang mở: **0 → 0**
  - địa chỉ trang: **không đổi**
  - không xuất hiện nút **[Đóng]** nào trên màn

## Phương pháp thứ hai (bắt buộc)

- **Đối chứng bằng video của đối tác:** frame `t003.04s.jpg` cho thấy con trỏ chữ (dạng I-beam) trên mã `QA-20260525-0001` và cụm "0001" **bị bôi đen như chữ thường** — dấu hiệu điển hình của bấm đúp vào văn bản không phải liên kết. Màn hình sau đó không có cửa sổ nào. Trùng khớp kết quả đo trên nip.io.
- **Kiểm chứng ngược — đo nội dung đã có sẵn trên thẻ kết quả** để biết cửa sổ chi tiết còn thiếu gì. Đọc nguyên văn 1 thẻ:

  ```
  QA-20260706-0001
  100% phù hợp
  Doanh nghiệp hỏi về thủ tục đăng ký kinh doanh và nghĩa vụ thuế ban đầu?
  <p>Nội dung phản hồi test PHCHVM_09 để kiểm tra double toast.</p>
  Thương mại
  Nguồn: Tự động
  Chọn
  ```

  Các trường phiếu test muốn thấy trong cửa sổ chi tiết — đã có sẵn trên thẻ kết quả hay chưa:
  - Câu hỏi → ✅ đã có
  - Câu trả lời → ✅ đã có (nhưng bị rút gọn, và lộ thẻ HTML — xem BUG-KCH-HTML-THO)
  - Lĩnh vực pháp lý → ✅ đã có ("Thương mại")
  - Từ khóa → ⚠️ bản ghi này không có từ khóa nên chưa kết luận được
  - Nguồn → ✅ đã có ("Nguồn: Tự động")

  ⇒ Giá trị thực của một cửa sổ chi tiết chủ yếu là **xem câu trả lời đầy đủ** (không bị rút gọn). BA nên chốt trên cơ sở đó.
- **Đối chiếu đặc tả:** đã đọc trọn `srs-fr-13-tv-nhanh.md:572` và toàn bộ FR-X.2-02 (`:164-238`) — không có câu nào mô tả cửa sổ chi tiết câu hỏi trong màn tra cứu, cũng không có nút [Đóng] nào. Cửa sổ chi tiết Q&A **chỉ được đặc tả ở màn Kho câu hỏi** (`:545`), là màn khác.
