# Bảng đối chiếu điều kiện — TKTVV_04 (re-verify sau dev fix, 2026-07-15)

Re-test đúng vai trò/màn/data mà bug gốc mô tả (bug-report §Các bước tái hiện).

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — `cbnv_tw` | CB_NV_TW — `cbnv_tw`, banner BTP·TW | Không |
| Màn / thẻ | Danh sách TVV, thẻ "Đang hoạt động", baseline 4 bản ghi | Đúng màn, thẻ "Đang hoạt động", baseline 4 bản ghi | Không |
| Data tiền đề | Có TVV thuộc tổ chức "Trung tâm Tư vấn Pháp luật Seed…" + TVV không có tổ chức | Có TVV-BTP-TW-0002 (org "Trung tâm Tư vấn Pháp luật Seed") + 3 TVV không org | Không |
| Thao tác lọc Tổ chức | Nhập Tổ chức khớp / không khớp → Tìm kiếm, đếm kết quả | Chọn Tổ chức khớp (Trung tâm Seed) → 1 bản ghi; chọn org không khớp (QĐ Địa phương) → 0 bản ghi | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix**. Bộ lọc "Tổ chức" áp dụng đúng — org khớp trả đúng 1 bản ghi (TVV-BTP-TW-0002), org không khớp trả 0 ("Không tìm thấy tư vấn viên phù hợp"); tham số gửi lên là `toChucId=<UUID thật>` (không còn chuỗi chữ tự do). "Trạng thái" nay lọc qua tab (ẩn ở tab cụ thể theo cùng fix TKTVV_02) nên tình huống xung đột thẻ↔bộ lọc không còn.
