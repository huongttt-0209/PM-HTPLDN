# Bảng đối chiếu điều kiện — QLKCHTV_36 (row 18) — Thiếu chức năng "Lưu nháp"

**Kết luận:** BA confirm.
- Tái hiện đúng: màn trả lời **không có nút [Lưu nháp]**.
- Nhưng đặc tả v3.5 của Tư vấn nhanh **không hề có chức năng lưu nháp**: `srs-fr-13-tv-nhanh.md:572` chỉ khai hai thao tác gửi — *"[Gui tra loi] -> luu `noi_dung_tra_loi` cuoi cung …"* và nút phụ "Đẩy sang Nhóm II"; FR-X.2-02 (`:164-238`) không có bước xử lý, đầu ra, trạng thái hay mã lỗi nào cho bản nháp.
- Đặc tả còn nói theo hướng ngược lại: `:215` ghi *"**chỉ lưu** `noi_dung_tra_loi` cuối cùng cùng thông tin CB xử lý/thời điểm trả lời"* ⇒ chủ trương là chỉ lưu bản cuối. Vì vậy không chấm lỗi, chuyển BA chốt (BA-13).

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_36.jpg` — **cùng một ảnh với QLKCHTV_35**, đã đối chiếu mã băm MD5 `abc3fcf1…` trùng nhau) | Mình test (env nip.io, 27/07/2026 11:56) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Phiên `2f144009-…` ở màn trả lời, chế độ nhập liệu | Phiên `TVN-20260727-0001` trạng thái "CB trả lời", ở màn trả lời, chế độ nhập liệu | Không |
| Dữ liệu tiền đề | Ô "Nội dung trả lời" đang trống (ảnh cho thấy `0 / 5000` và dòng nhắc "Vui lòng nhập nội dung trả lời") | Đo **cả 2 tình huống**: ô trống (`0 / 5000`) **và** ô đã có nội dung — nút [Lưu nháp] không xuất hiện ở tình huống nào | Không |
| Input / filter / giá trị nhập | Phiếu test ghi "Nhập thông tin hợp lệ và Nhấn Lưu nháp"; ảnh cho thấy không tìm được nút | Liệt kê **toàn bộ** nút trong vùng nội dung bằng mã lệnh, ở cả 2 tình huống trên | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-TVN-man-tra-loi-cot-trai.png` (ô trả lời trống) và `bug-reports/image/BUG-TVN-chon-tu-kho-vuot-gioi-han-5000.png` (ô trả lời đã có nội dung) — đã mở đọc: cuối khối "Soạn trả lời" **chỉ có một nút [Gửi trả lời]**, không có nút phụ nào.
- Liệt kê nút trong vùng nội dung: `["Quay lại danh sách", "Tìm kiếm", "Gửi trả lời"]` — **không có** "Lưu nháp".
- Quét chữ toàn màn: không có cụm "Lưu nháp" / "nháp" ở bất kỳ đâu.

## Phương pháp thứ hai (bắt buộc)

- **Kiểm tầng máy chủ xem có đường lưu nháp bị giấu không:** đọc danh mục giao diện lập trình (`/api/docs-json`), nhóm tư vấn nhanh có đúng 10 đường dẫn: `tu-van-nhanhs` (danh sách) · `{id}` · `{id}/goi-y` · `{id}/tra-cuu-kho` · `{id}/tra-loi` · `{id}/chuyen-kenh` · `{id}/danh-gia/cms-proxy` · `cms-create` · `public/…/inbound` · `public/…/{id}/danh-gia`. **Không có đường nào cho bản nháp.** ⇒ chức năng chưa tồn tại ở cả hai tầng, không phải nút bị ẩn.
- **Đối chứng với module khác để thấy đây là khác biệt có chủ ý, không phải sót:** nhóm Hỏi đáp **có** đặc tả lưu nháp rất chi tiết — `srs-fr-02-hoi-dap.md:1127`: *"Nút Lưu nháp + Auto-save | **Auto-save mỗi 60 giây** nếu có thay đổi (silent save, không toast — chỉ đổi indicator "Đã lưu lúc {HH:mm:ss}"…)"*. Việc đặc tả viết rõ cho Hỏi đáp mà **không** viết cho Tư vấn nhanh cho thấy đây là lựa chọn thiết kế, không phải thiếu sót ngẫu nhiên. (Tư vấn nhanh vốn là luồng trả lời ngắn, dựa trên kho câu hỏi có sẵn.)
- **Tra nguyên văn trong đặc tả Tư vấn nhanh:** tìm cụm *"Luu nhap"* / *"Lưu nháp"* trong `srs-fr-13-tv-nhanh.md` → chỉ có **1** kết quả ở dòng `:534`, và đó là nút của **màn Kho câu hỏi** (SCR-X2-01), không phải màn Tư vấn nhanh.
- **Ghi nhận rủi ro để BA cân nhắc:** hiện cán bộ soạn dở mà rời màn thì mất toàn bộ nội dung (đã kiểm ở QLKCHTV_31: hệ thống cũng không cảnh báo khi ghi đè). Nếu BA muốn giữ công soạn, có thể chốt bổ sung lưu nháp hoặc chốt cảnh báo trước khi mất dữ liệu — hai câu hỏi này gắn với nhau.
