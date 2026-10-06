# Bảng đối chiếu điều kiện — TKCHTV_03 (row 26) — Nút Xóa bộ lọc

**Kết luận:** Open (Minor) + BA confirm.

Phiếu nêu 2 vế, đo tách bạch:

- **Bước 2–3 — Kho câu hỏi** *"Không có nút chức năng 'Xóa bộ lọc'"* → **TÁI HIỆN**. Thanh lọc có 6 tiêu chí (từ khóa, Lĩnh vực, Nguồn, Trạng thái, Từ ngày, Đến ngày) nhưng không có nút nào xóa hết trong một thao tác. Thử thêm nút **[Làm mới]**: nút này **không** đặt lại bộ lọc. → lỗi `BUG-TK-KHONG-CO-XOA-BO-LOC`.
- **Bước 5–6 — Tư vấn nhanh** → **ĐẠT**. Màn này **có** nút [Xóa bộ lọc] và chạy đúng kết quả mong đợi của phiếu: xóa sạch mọi ô lọc, ô tìm kiếm, đưa danh sách về mặc định của thẻ hiện tại.

Chấm **Open** mức Minor vì phần đối tác phản ánh tái hiện đúng, kèm **BA confirm** vì đặc tả nhóm X.2 không liệt kê nút này ở màn nào — căn cứ hiện có là quy ước lặp ở 7 nhóm khác và ở chính màn anh em. Xem BA-18.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/TKCHTV_03(1)-1.jpg`, `TKCHTV_03(1)-2.jpg`) | Mình test (env nip.io, 27/07/2026 14:20–14:38) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ theo cột Tác nhân của phiếu; ảnh chụp màn quản trị Kho câu hỏi và Tư vấn nhanh | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Nằm trong tập tác nhân phiếu ghi | Không |
| Entity + trạng thái (state machine) | Ảnh cho thấy thanh lọc Kho câu hỏi không có nút xóa bộ lọc, còn thanh lọc Tư vấn nhanh có | Kho câu hỏi 14 bản ghi, Tư vấn nhanh 4 phiên, cả hai ở thẻ "Tất cả". Đọc toàn bộ nút trên từng màn để so, không chỉ nhìn ảnh | Không |
| Dữ liệu tiền đề | Phiếu yêu cầu "Tồn tại bản ghi phù hợp với tiêu chí tìm kiếm" để còn thấy tác dụng của việc xóa lọc | Đặt bộ lọc có tác dụng thật trước khi thử nút: Kho câu hỏi lọc `lao động` còn 1/14 dòng; Tư vấn nhanh lọc `abcdxyzqwerty` còn 0/4 dòng. Nhờ vậy phân biệt được "nút chạy" với "nút không làm gì" | Không |
| Input / filter / giá trị nhập | Bấm nút "↻ Xóa bộ lọc" sau khi đã đặt tiêu chí lọc | Kho câu hỏi: vì không có nút xóa bộ lọc nên thử nút gần nghĩa nhất là [Làm mới]. Tư vấn nhanh: bấm đúng nút [Xóa bộ lọc]. Cả hai lần đều đọc lại toàn bộ ô lọc, số dòng, thẻ đang chọn sau khi bấm | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Thành phần giao diện)

- `partner-evidence/TKCHTV_03(1)-1.jpg` và `TKCHTV_03(1)-2.jpg` — đã mở đọc: khẳng định thanh lọc Tư vấn nhanh có nút "Xóa bộ lọc", còn thanh lọc Kho câu hỏi không có. Trùng khít với đo được trên bản hiện tại.
- `bug-reports/image/BUG-TK-kho-cau-hoi-loc-dung-1-ket-qua.png` — đã mở đọc: toàn bộ thanh lọc Kho câu hỏi hiện trong khung — ô tìm kiếm, Lĩnh vực, Nguồn, Trạng thái, Từ ngày, Đến ngày — và hàng nút góc phải trên chỉ có [+ Thêm câu hỏi] [Nhập Excel] [Xuất Excel] [Làm mới]. Không có nút xóa bộ lọc ở bất kỳ vị trí nào trong khung nhìn.
- `bug-reports/image/BUG-TK-tv-nhanh-tim-dung-ma-phien-ra-0.png` — đã mở đọc, dùng làm **đối chứng dương tính**: cùng loại thanh lọc ở màn Tư vấn nhanh có đủ [Xóa bộ lọc] và [Tìm kiếm] nằm cạnh nhau.

## Phương pháp thứ hai (bắt buộc)

- **Đọc danh sách nút bằng mã lệnh thay vì nhìn ảnh** — tránh kết luận "không có" chỉ vì nút nằm ngoài khung nhìn. Kho câu hỏi trả về đúng 4 nút: `Thêm câu hỏi`, `Nhập Excel`, `Xuất Excel`, `Làm mới`; quét toàn bộ chữ trên màn cũng không có cụm "Xóa bộ lọc". Tư vấn nhanh trả về có cả `Xóa bộ lọc` lẫn `Tìm kiếm`.
- **Phép thử quyết định — thử nút gần nghĩa nhất trước khi kết luận là thiếu đường xử lý.** Nhiều màn dùng [Làm mới] để vừa tải lại vừa xóa lọc, nên phải loại khả năng này. Đặt từ khóa `lao động` (bảng còn 1/14 dòng, thẻ đếm "Tất cả 1") rồi bấm [Làm mới]: sau khi bấm ô tìm kiếm **vẫn là** `lao động`, bảng **vẫn** 1 dòng, thẻ **vẫn** "Tất cả 1". ⇒ [Làm mới] không đặt lại bộ lọc, nên hiện không có thao tác nào đưa danh sách về mặc định trong một lần bấm.
- **Đối chứng dương tính trong cùng phiên đăng nhập:** bấm [Xóa bộ lọc] ở Tư vấn nhanh — trước khi bấm: từ khóa `abcdxyzqwerty`, 0 dòng; sau khi bấm: từ khóa rỗng, Trạng thái rỗng, Từ ngày rỗng, Đến ngày rỗng, thẻ về "Tất cả", danh sách về "Hiển thị 1-4 / 4 kết quả". Chạy đúng nguyên văn kết quả mong đợi của phiếu. ⇒ Thành phần này đã có sẵn trong hệ thống, không phải thứ phải làm mới từ đầu.
- **Đối chiếu đặc tả — nêu thẳng giới hạn của căn cứ, không tự suy diễn:** `srs-fr-13-tv-nhanh.md:530` (thanh lọc Kho câu hỏi) và `:568` (thanh lọc Tư vấn nhanh) chỉ liệt kê các tiêu chí lọc, **không dòng nào** nhắc nút xóa bộ lọc. Vì vậy QA **không** quy kết vi phạm trực tiếp đặc tả nhóm X.2.
- **Đối chiếu quy ước toàn hệ thống (căn cứ thay thế):** nút [Xóa bộ lọc] được quy định lặp lại ở 7 nhóm khác của cùng SRS v3.5 — `srs-fr-02-hoi-dap.md:1033` *"| 18 | filter-bar | Nút Xóa bộ lọc | button | \"Xóa bộ lọc\" — reset tất cả | click → reset | luôn hiển thị |"*, `srs-fr-09-bieu-mau.md:622`, `srs-fr-07-doanh-nghiep.md:434`, `srs-fr-04-chuyen-gia-tvv.md:1439`, `srs-fr-05-vu-viec.md:1646`, `srs-fr-06-chi-tra.md:1050`, `srs-fr-08-danh-gia.md:817`. Cộng thêm việc chính màn anh em cùng nhóm đã có ⇒ đủ cơ sở chấm Open, nhưng vẫn gửi BA-18 để BA chốt chính thức.
- **Liên hệ với TKCHTV_02:** `srs-fr-02-hoi-dap.md:1047` đặt nút [Xóa bộ lọc] **ngay trong câu thông báo** khi lọc không khớp. Nghĩa là hai case này cùng một hướng sửa — đã ghi vào BA-18 để BA xem một lượt.
