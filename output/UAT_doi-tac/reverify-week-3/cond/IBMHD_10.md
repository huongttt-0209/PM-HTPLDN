# Bảng đối chiếu điều kiện — IBMHD_10

Loại bug: **Import vượt tổng dung lượng → không hiện "Tổng dung lượng tối đa 500 MB".** Verdict phụ thuộc: (1) app có hiện message khi tổng >500MB, (2) đúng điểm kích hoạt.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (case chỉ định vai trò "CB Nghiệp vụ") | CB Nghiệp vụ (`cbnv_bn`) — cùng vai trò case yêu cầu | Không |
| Màn hình | `/bieu-mau/nhap-hang-loat` bước 1 | Cùng | Không |
| Thao tác (input) | Upload nhiều tệp tổng >500MB | Upload 27 tệp `.docx` ~19MB (tổng ~514 MiB) | Không |
| Kích hoạt kiểm tra tổng dung lượng | Bấm "Kiểm tra và tiếp tục" (điểm mà SRS ERR-IMP-03 chạy) | Chọn thư mục → nút "Kiểm tra và tiếp tục" enabled → bấm | Không |

**Kết luận: message HIỆN đúng → không tái hiện.** Khi tổng >500MB và bấm "Kiểm tra và tiếp tục", hệ thống hiện **"Tổng dung lượng tối đa 500MB mỗi lần import"** (đo qua MutationObserver, lặp 3 lần thao tác) + chặn sang bước 2 — khớp SRS ERR-IMP-03 (`srs-fr-09-bieu-mau.md:481`) / EC-01 (`:505`). Đối tác có bằng chứng (frame `t020.15s` cho thấy chưa chọn "Thư mục đích" → chưa tới bước kiểm tra) ⇒ không Reject. → **Resolved** (Verify) — không tái hiện trên bản hiện tại. Bằng chứng: `BUG-IBMHD_10-toast-500mb.png`.

> Chẩn đoán vì sao đối tác không thấy message (nội bộ): kiểm tra tổng dung lượng nằm ở bước "Kiểm tra và tiếp tục", mà nút này chỉ enabled sau khi ĐÃ chọn thư mục đích. Video đối tác cho thấy đã upload nhiều tệp nhưng chưa chọn thư mục → nút disabled → chưa tới điểm kiểm tra → nên không có message. Đây là luồng chưa hoàn tất phía đối tác, không phải app thiếu message.
>
> Ghi chú vai trò (nội bộ): case chỉ định vai trò "CB Nghiệp vụ"; test bằng `cbnv_bn` do `cbnv_tw` bị chiếm session. Kiểm tra tổng dung lượng là validate client-side, không phụ thuộc đơn vị.
