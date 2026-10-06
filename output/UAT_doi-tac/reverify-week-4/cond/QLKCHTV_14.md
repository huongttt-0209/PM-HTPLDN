# Bảng đối chiếu điều kiện — QLKCHTV_14 (row 8) — Màn chi tiết câu hỏi

**Kết luận:** Open, BA confirm.
- **Open** — màn chi tiết KHÔNG hiển thị **Người tạo**, trong khi đặc tả liệt kê rõ trường này.
- **KHÔNG phải lỗi** — **Từ khóa** CÓ hiển thị; chỉ bị ẩn dòng khi bản ghi không có từ khóa. Bản ghi đối tác chụp rơi vào trường hợp không có từ khóa.
- **BA confirm** — **Lịch sử thẩm định** không có trong đặc tả v3.5 ở bất kỳ đâu.
- Phát hiện thêm: phần "Câu trả lời" hiện nguyên văn thẻ HTML (tách bug riêng).

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_14.jpg`) | Mình test (env nip.io, 27/07/2026 11:15) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Không đọc được trên ảnh (khung hình bắt đầu từ breadcrumb, không có vùng avatar). Suy từ các ảnh cùng đợt: `CB_NV_TW` | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Màn chi tiết Kho câu hỏi chỉ mở cho vai trò có quyền trên `KHO_CAU_HOI` (`srs-v3.5.md:1325`) nên không có lựa chọn khác | Không |
| Entity + trạng thái (state machine) | Bản ghi `QA-20260702-0003` — Nguồn "Tự động", Trạng thái **"Đã duyệt"**, Hiệu lực "Có" | Test **2 bản ghi ở 2 trạng thái/nguồn khác nhau** để phủ hết: `QA-20260708-0001` (Tự động, **Đã duyệt**, có "Ngày duyệt" — cùng loại với bản ghi đối tác) và `QA-20260727-0002` (Import, **Chờ duyệt**) | Không |
| Dữ liệu tiền đề (có/không có từ khóa) | Bản ghi đối tác chụp **không thấy dòng Từ khóa** — nhưng ảnh không cho biết bản ghi đó có từ khóa trong dữ liệu hay không | **Đã chủ động dựng cả 2 vế**: bản ghi **CÓ** từ khóa (`QA-20260727-0002`, dữ liệu `tuKhoa=["thue","mien giam","dnnvv"]`) và bản ghi **KHÔNG có** từ khóa (`QA-20260727-0001`, `QA-20260708-0001`) | Không |
| Input / filter / giá trị nhập | Bấm nút Xem (biểu tượng mắt) trên dòng bảng | Bấm nút Xem (biểu tượng mắt) trên dòng bảng; đọc toàn bộ chữ trong panel bằng mã lệnh, không phụ thuộc vùng nhìn thấy | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-QLKCHTV_14-chi-tiet-co-tu-khoa.png` — đã mở đọc: bản ghi **CÓ** từ khóa → panel hiện đủ dòng **"Từ khóa: thue / mien giam / dnnvv"**; vẫn **KHÔNG có** dòng "Người tạo", **KHÔNG có** mục "Lịch sử thẩm định".
- `bug-reports/image/BUG-KCH-HTML-THO-chi-tiet-cau-tra-loi.png` — đã mở đọc: bản ghi cùng loại với bản ghi đối tác (Tự động / Đã duyệt) → **không có** dòng "Từ khóa" (vì bản ghi không có từ khóa), **không có** "Người tạo", và phần "Câu trả lời" hiện nguyên văn `<p>...</p>`.
- Đọc thẳng danh sách trường trong panel (bản ghi Đã duyệt): `Mã · Lĩnh vực · Nguồn · Trạng thái · Công khai · Hiệu lực · Lượt xem · Đánh giá TB · Ngày tạo · Ngày duyệt` → rồi tới "Câu hỏi" / "Câu trả lời".

## Phương pháp thứ hai (bắt buộc)

- **Tách bạch "thiếu trường hiển thị" với "thiếu dữ liệu" bằng cách đọc dữ liệu máy chủ trả về:**
  - `tuKhoa` — máy chủ trả `["thue","mien giam","dnnvv"]` cho bản ghi có từ khóa, trả rỗng cho bản ghi không có. Panel hiện dòng "Từ khóa" đúng theo dữ liệu ⇒ **trường này KHÔNG thiếu**, chỉ ẩn khi rỗng.
  - `nguoiTaoId` — máy chủ **có** trả mã người tạo (`"nguoiTaoId":"f2e93500-..."`) nhưng **không** trả tên/họ tên người tạo, và panel không hiển thị gì. ⇒ thiếu ở cả tầng dữ liệu (không kèm tên) lẫn tầng hiển thị.
  - Không có trường nào liên quan lịch sử thẩm định trong dữ liệu trả về (danh sách trường đầy đủ: `id, nguoiTaoId, nguoiCapNhatId, ngayTao, ngayCapNhat, donViId, seqId, version, trangThai, nguoiGuiDuyetId, ngayGuiDuyet, nguoiDuyetId, ngayDuyet, ghiChuPheDuyet, maCauHoi, cauHoi, cauTraLoi, linhVucId, tuKhoa, nguon, hoiDapGocId, hieuLuc, congKhai, thoiGianDangTai, moTaCongKhai, fileDinhKemCongKhai, anhDaiDien, soLuotXem, soLuotSuDung, diemDanhGiaTb, linhVuc`). Đáng chú ý: máy chủ **có** các trường `nguoiGuiDuyetId / ngayGuiDuyet / nguoiDuyetId / ngayDuyet / ghiChuPheDuyet` — đủ nguyên liệu để dựng lịch sử thẩm định nếu BA yêu cầu.
- **Đối chiếu đặc tả:** `srs-fr-13-tv-nhanh.md:545` (§3 SCR-X2-01, Quy tắc tương tác) — *"Chi tiet Q&A: side panel/modal hien thi day du cau hoi, cau tra loi (rich text), linh vuc, tu khoa, nguon, **nguoi tao**"*. Danh sách này **có "nguoi tao"**, **có "tu khoa"**, **KHÔNG có** lịch sử thẩm định. Đã tìm toàn bộ file, không có mục "Lịch sử thẩm định" nào cho Kho câu hỏi.
- **Mâu thuẫn nội bộ đặc tả cần báo BA:** bảng thuộc tính entity `KHO_CAU_HOI` (`srs-fr-13-tv-nhanh.md:683-698`) **không khai trường người tạo** nào, trong khi dòng `:545` lại yêu cầu hiển thị "nguoi tao".
