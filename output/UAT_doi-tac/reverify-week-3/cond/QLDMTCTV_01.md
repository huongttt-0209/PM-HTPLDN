# Bảng đối chiếu điều kiện — QLDMTCTV_01 (row 141)

**Bug:** "Màn hình không có danh mục Tổ chức tư vấn".
**Verdict:** `Reject` (feature tồn tại ở Mạng lưới TVV, không mất — chuyển vị trí theo CR-02).

| Điều kiện có thể đổi kết quả | Đối tác (ảnh full-res, role QTHT) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT (Quản trị viên) | QTHT (`admin`) — cùng role | Không |
| Màn hình / vị trí feature | Chỉ xem màn "Danh mục dùng chung" | Xem cả Danh mục dùng chung (không có) + Mạng lưới TVV (CÓ, hoạt động) | Không |

**Kết luận:** Cùng role QTHT với đối tác. Tại Danh mục dùng chung: không có "Tổ chức tư vấn" (đúng SRS v3.5 — đã chuyển đi). Tại Mạng lưới Tư vấn viên → Tổ chức tư vấn: feature tồn tại, đầy đủ chức năng (3 record, 6 tab trạng thái, search/filter/xuất Excel). Kỳ vọng đối tác ("quản lý danh sách Tổ chức tư vấn tham gia mạng lưới") đã được đáp ứng ở vị trí mới → `Reject`. 0 GAP.
