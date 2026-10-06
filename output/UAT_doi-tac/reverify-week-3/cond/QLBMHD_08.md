# Đối chiếu điều kiện — QLBMHD_08 (Upload tệp có mã độc — hành vi quét virus)

Loại: **Security — quét virus file đính kèm.** Đối tác báo thông báo mã độc "sai thiết kế". Kiểm bằng chuỗi test chuẩn EICAR.

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_08.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | CB Nghiệp vụ upload biểu mẫu | `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW) | Không |
| Màn / trường upload | Form Thêm biểu mẫu, trường File biểu mẫu | Đúng form `/bieu-mau/them-moi`, trường File biểu mẫu | Không |
| File chứa mã độc | File có mã độc | `valid-eicar.docx` — docx OOXML HỢP LỆ chứa chuỗi test AV chuẩn EICAR (thay chuẩn cho "file mã độc") | Không |
| File qua được kiểm định dạng | (đối tác không nêu) | File là docx hợp lệ → qua format check → tới bước quét AV | Không |
| Cách đo | Quan sát thông báo/hành vi | Observer toast + network status (201) + record tạo | Không |

**0 GAP.** EICAR là file test AV chuẩn công nghiệp (thay hợp lệ cho "file có mã độc"); file được dựng docx HỢP LỆ để chắc chắn qua bước format và tới bước quét virus.

## Cổng 3 — SRS vs web (dạng bullet)

- SRS yêu cầu quét virus 3 nơi: `srs-fr-09:314` ("Quét virus file đính kèm"), `:382` (EC-02 "Quét antivirus TRƯỚC lưu trữ → ERR-BM-07 nếu phát hiện mã độc"), `:652` (Inputs #15 "Quét virus").
- Web đo được: `valid-eicar.docx` → `POST /bieu-maus/upload` **HTTP 201**, 0 toast, `ant-upload-list-item-done`; submit "Thêm mới" → tạo biểu mẫu THÀNH CÔNG, 0 chặn / 0 ERR-BM-07.
- Đối chiếu: SRS bắt quét virus + chặn nếu phát hiện; thực tế file test mã độc EICAR được **chấp nhận + lưu + tạo biểu mẫu** → vi phạm yêu cầu quét virus.
- Caveat: EICAR nằm trong ZIP docx; nếu AV không giải nén archive có thể bỏ sót — đề nghị Dev/Security xác nhận pipeline AV (có chạy trước lưu trữ + có quét trong archive không). Dù cách nào, hành vi quan sát không khớp SRS.

## Verdict

- Hành vi quan sát (file `.docx` hợp lệ chứa EICAR được lưu 201 + tạo biểu mẫu, có thể công khai lên Cổng) trái với yêu cầu quét virus SRS (dòng 314/382/652). Đây là **rủi ro bảo mật thật**, KHÔNG phải câu hỏi wording.
- Nhưng vì EICAR nằm trong ZIP `.docx` + không quan sát được server-side → chưa khẳng định chắc "không có AV" hay "AV không quét trong archive". Cần BA + Dev/Security xác nhận pipeline quét virus trước khi chốt bug.
- → **BA confirm** (route BA → Dev/Security). Lỗi "thông báo mã độc sai wording" đối tác báo không tái hiện; thực tế cần xác minh pipeline AV.

Evidence: [`../reverify-audit/QLBMHD_08/toast-capture.md`](../reverify-audit/QLBMHD_08/toast-capture.md) + [`../reverify-audit/QLBMHD_08/eicar-accepted-list.png`](../reverify-audit/QLBMHD_08/eicar-accepted-list.png).
