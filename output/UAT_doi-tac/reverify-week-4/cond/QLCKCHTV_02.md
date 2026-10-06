# Bảng đối chiếu điều kiện — QLCKCHTV_02 (row 23) — Hộp thoại Công khai thiếu ảnh đại diện và tệp đính kèm

**Kết luận:** Open (Medium).

Phiếu của đối tác nêu 3 thứ mà hộp thoại Công khai phải có. Đo tách bạch từng thứ:

- **Mô tả công khai** — **CÓ**. Hộp thoại hiển thị ô "Mô tả công khai" (nhập được, tối đa 2000 ký tự). Câu "Kết quả thực tế" trong phiếu ghi *"Hệ thống không hiển thị các trường thông tin cho phép NSD bổ sung mô tả hiển thị trên chuyên trang"* là **không đúng với chính ảnh đối tác gửi kèm** — trong ảnh đó ô "Mô tả công khai" đang hiện và có nội dung 56/2000. Nêu rõ để dev không mất công tìm lỗi không tồn tại.
- **Ảnh đại diện** — **KHÔNG CÓ**. → lỗi theo `:538`
- **Tệp đính kèm công khai** — **KHÔNG CÓ**. → lỗi theo `:538`

Vẫn chấm **Open** vì 2 trong 3 hạng mục thiếu thật, đúng phần cốt lõi mà đối tác phản ánh.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLCKCHTV_02.jpg`) | Mình test (env nip.io, 27/07/2026 13:14 và 13:18) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — thao tác trên màn Kho câu hỏi (đọc từ đường dẫn `/tv-nhanh/kho-cau-hoi/...` và bố cục màn) | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Đúng tác nhân `srs-fr-13-tv-nhanh.md:441` *"Tác nhân: Cán bộ Nghiệp vụ (TW/BN/ĐP)"* | Không |
| Entity + trạng thái (state machine) | Câu hỏi `QA-20260720-0005`, trạng thái **"Đã duyệt"**, cờ công khai **"Chưa công khai"**, hiệu lực **"Có"** (đọc từ cột phải trong ảnh) | Lần 1: `QA-20260727-0001` — `DA_DUYET`, `congKhai = false`, `hieuLuc = true`. Lần 2: `QA-20260727-0005` — cũng `DA_DUYET`, `congKhai = false`. Khớp điều kiện tiên quyết `:447` | Không |
| Dữ liệu tiền đề | Bản ghi nguồn Import, **không rõ có ảnh đại diện / tệp đính kèm hay không** (ảnh đối tác không cho thấy) | **Đo 2 lần với 2 mức dữ liệu khác nhau — đây là điểm chặt hơn đối tác.** Lần 1 bản ghi `anhDaiDien = null`, `fileDinhKemCongKhai = []`. Lần 2 QA **tự tạo** bản ghi có đủ: `anhDaiDien = {fileId: 743d5cfc-…}` + `fileDinhKemCongKhai = [{fileId: 8ae94569-…}]` + `moTaCongKhai` 110 ký tự. Cả 2 lần hộp thoại đều không hiện ảnh và tệp ⇒ loại trừ giả thuyết "ẩn vì chưa có dữ liệu" | Không |
| Input / filter / giá trị nhập | Bấm nút **[Công khai]** ở màn chi tiết câu hỏi | Bấm đúng nút **[Công khai]** ở màn chi tiết câu hỏi (cùng vị trí góc phải trên như ảnh đối tác). Đo nội dung hộp thoại bằng mã lệnh: đếm ô tải tệp, thẻ ảnh, liên kết, nhãn | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-CK-modal-cong-khai-thieu-anh-va-tep.png` — đã mở đọc: hộp thoại "Công khai câu hỏi QA-20260727-0001" gồm đúng 4 phần — khối thông tin nền xanh, nhãn + ô "Mô tả công khai" (88/2000), nút [Hủy], nút [Công khai]. **Không có** vùng ảnh, **không có** danh sách tệp. Trùng khít bố cục ảnh đối tác gửi.
- `bug-reports/image/BUG-CK-ban-ghi-co-anh-va-tep-modal-van-khong-hien.png` — đã mở đọc, **đây là bằng chứng khóa**: cùng hộp thoại đó với bản ghi `QA-20260727-0005` vốn ĐÃ có ảnh đại diện và tệp đính kèm trong dữ liệu, hộp thoại **vẫn chỉ hiện "Mô tả công khai"**.
- `bug-reports/image/BUG-CK-form-them-cau-hoi-co-du-3-truong.png` — đã mở đọc: form "Thêm câu hỏi" có đủ **Ảnh đại diện công khai** (kèm nút "Dùng ảnh hệ thống mặc định", ghi chú `.jpg, .png, .gif, ≤5MB`), **Mô tả công khai**, **Tệp đính kèm công khai** (`.pdf, .doc, .docx, .xls, .xlsx, ≤20MB/tệp`). ⇒ Ba trường này **đã được dựng ở nơi khác**, nên đây là lỗi thiếu hiển thị ở hộp thoại, không phải tính năng chưa làm.
- Đo nội dung hộp thoại bằng mã lệnh (định lượng, không phụ thuộc cảm nhận): `số thẻ ảnh = 0`, `số khối tải tệp = 0`, `số ô chọn tệp = 0`, `số liên kết = 0`, `nhãn = ["Mô tả công khai"]`, chữ trong hộp thoại không chứa cụm "ảnh đại diện" và "đính kèm".

## Phương pháp thứ hai (bắt buộc)

- **Tự dựng dữ liệu tiền đề rồi đo lại — phép thử quyết định.** Thay vì kết luận từ một bản ghi rỗng, QA tạo mới `QA-20260727-0005` qua đúng luồng nghiệp vụ: form "Thêm câu hỏi" → tải lên ảnh `qa-anh-dai-dien.png` (7,7 KB) + tệp `qa-tep-dinh-kem.pdf` (404 B) + nhập mô tả công khai → Lưu → tài khoản `cbpd_tw` duyệt → quay lại mở hộp thoại Công khai. Máy chủ xác nhận bản ghi có `anhDaiDien` và `fileDinhKemCongKhai`, nhưng hộp thoại vẫn không hiện. Không còn cách giải thích nào khác ngoài "giao diện không dựng phần này".
- **Kiểm phần nghiệp vụ có chạy đúng không (để không quy kết quá phạm vi):** bấm [Công khai] trên `QA-20260727-0001` → 1 lần gọi `POST /api/v1/kho-cau-hois/{id}/cong-khai`, 1 khung thông báo "Đã công khai câu hỏi", không lặp (bộ bắt thông báo dùng chung, tự kiểm `soObserverDangSong = 1`). Đọc lại bản ghi: `trangThai = CONG_KHAI`, `congKhai = true`, `thoiGianDangTai = 2026-07-27T06:14:49.373Z`. ⇒ Khớp `srs-fr-13-tv-nhanh.md:464` (bước 4: SET `cong_khai = 1` + `trang_thai = CONG_KHAI` + `thoi_gian_dang_tai = NOW()`, BR-PUBLIC-03). **Phần xử lý công khai chạy đúng**, chỉ thiếu phần hiển thị trước khi xác nhận.
- **Đối chiếu đặc tả — trích nguyên văn:** `srs-fr-13-tv-nhanh.md:538` (§3 SCR-X2-01, dòng 12 "Hanh dong Cong khai / Huy cong khai (FR-X.2-06)"): *"Click [Cong khai] -> modal xac nhan + **hien thi anh dai dien / mo ta cong khai / file dinh kem cong khai sap cong khai**; xac nhan -> SET cong_khai = 1 + trang_thai = CONG_KHAI + thoi_gian_dang_tai = thoi diem hien tai (BR-PUBLIC-03)"*. Hộp thoại hiện 1/3 hạng mục.
- **Đối chiếu bước xử lý:** `srs-fr-13-tv-nhanh.md:463` (Processing — Công khai, bước 3): *"Lưu nội dung công khai: **ảnh đại diện + mô tả công khai + file đính kèm công khai**"* ⇒ cả 3 đều là nội dung sẽ đăng lên Cổng PLQG, nên đều thuộc phần cán bộ cần soát trước khi xác nhận.
- **Đối chiếu bảng thuộc tính entity** (chứng minh 3 trường là thật, không phải QA suy diễn): `:105` `anh_dai_dien` *"jpg/png/gif, max 5MB; mặc định ảnh hệ thống"* · `:106` `mo_ta_cong_khai` *"mô tả hiển thị trên Cổng PLQG"* · `:107` `file_dinh_kem_cong_khai` *"PDF/DOC/DOCX/XLS/XLSX, max 20MB/file, nhiều file"*. Ràng buộc trong form "Thêm câu hỏi" của hệ thống khớp đúng 3 dòng này.
- **Ảnh hưởng nghiệp vụ (vì sao không xếp Minor):** đây là bước xác nhận cuối trước khi nội dung ra Cổng Pháp luật quốc gia. Cán bộ không nhìn thấy ảnh và tệp sắp công khai thì mất chốt kiểm soát cuối — không phát hiện được ảnh/tệp gắn nhầm trước khi công khai ra ngoài.
