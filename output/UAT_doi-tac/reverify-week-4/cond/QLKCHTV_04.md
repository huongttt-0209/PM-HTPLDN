# Bảng đối chiếu điều kiện — QLKCHTV_04 (row 4) — Nút trong cửa sổ "Thêm câu hỏi"

**Kết luận:** Open — cửa sổ Thêm câu hỏi chỉ có [Hủy] [Lưu]; đặc tả yêu cầu [Hủy] [Lưu nháp] [Gửi duyệt].

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res `partner-evidence/QLKCHTV_04.jpg`) | Mình test (env nip.io, 27/07/2026 10:55) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — Cán bộ Nghiệp vụ Trung ương (các ảnh cùng phiên đọc rõ "CB_NV_TW · BTP · TW") | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP. Đây cũng là vai trò duy nhất có quyền tạo câu hỏi theo ma trận `srs-v3.5.md:1325` (`KHO_CAU_HOI` = CRUD* cho CB_NV; CB_PD chỉ RU*) | Không |
| Entity + trạng thái (state machine) | Cửa sổ mở ở chế độ **thêm mới**, form trắng chưa nhập, chưa có bản ghi nên chưa có trạng thái | Cửa sổ mở ở chế độ **thêm mới**, form trắng chưa nhập | Không |
| Dữ liệu tiền đề | Không cần bản ghi sẵn có (thao tác tạo mới) | Không cần bản ghi sẵn có | Không |
| Input / filter / giá trị nhập | Chưa nhập gì khi chụp — quan sát vùng nút cố định ở đáy cửa sổ | Quan sát vùng nút cố định ở đáy cửa sổ khi form trắng; **và** kiểm lại sau khi đã nhập đủ trường bắt buộc (Câu hỏi + Câu trả lời + Lĩnh vực) — vẫn đúng 2 nút, không phát sinh nút thứ ba | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-QLKCHTV_04-drawer-them-cau-hoi.png` — full-res, đã mở đọc: cửa sổ "Thêm câu hỏi", vùng nút cố định đáy chỉ có **[Hủy]** và **[Lưu]**.
- Đọc DOM vùng nút cố định: `nut_footer = ["Hủy", "Lưu"]`; toàn bộ nút trong cửa sổ = `["Dùng ảnh hệ thống mặc định", "Hủy", "Lưu"]` ⇒ không có [Lưu nháp], không có [Gửi duyệt] ở bất kỳ vị trí nào trong cửa sổ (không phải bị khuất do cuộn).

## Phương pháp thứ hai (bắt buộc)

- **Đo bằng hành vi thật, không chỉ đọc nhãn:** bấm [Lưu] với dữ liệu hợp lệ → 1 request `POST /api/v1/kho-cau-hois`, 1 thông báo *"Tạo câu hỏi thành công, đang chờ duyệt"*, bản ghi `QA-20260727-0001` ra thẳng trạng thái **"Chờ duyệt"**. Nghĩa là nút [Lưu] đang gánh vai trò của [Gửi duyệt], còn đường tạo bản ghi ở trạng thái "Nháp" thì **không tồn tại** trên giao diện.
- Kết quả này khớp với BUG-QLKCHTV_02: trạng thái "Nháp" vắng cả ở ô lọc lẫn ở nút tạo.
- Đối chiếu đầy đủ các TRƯỜNG của cửa sổ (để không quy oan): 7 trường đặc tả yêu cầu đều CÓ — Câu hỏi, Câu trả lời, Lĩnh vực, Từ khóa, Ảnh đại diện công khai, Mô tả công khai, Tệp đính kèm công khai. Sai lệch **chỉ nằm ở vùng nút**.
