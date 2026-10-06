# Bảng đối chiếu điều kiện — CKTMBMHDLCTT_08 (row 94)

Bug loại **Kết quả bulk theo state/data** (phụ thuộc số thư mục đủ/không đủ điều kiện) → bắt buộc bảng điều kiện.

| Điều kiện | Đối tác (evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | cbnv_tw — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Thư mục #1 (đủ điều kiện công khai) | Nháp + có biểu mẫu (≥1 BM) | QA Hidden Folder 715 — Nháp + 1 biểu mẫu (≥1 BM = đủ đk) | Không |
| Thư mục #2 (không đủ điều kiện) | Nháp + rỗng (0 BM) | BM-B3-0720-Rong-1 — Nháp + 0 biểu mẫu (rỗng) | Không |
| Thao tác | Công khai hàng loạt 2 thư mục cùng lúc | Công khai hàng loạt 2 thư mục cùng lúc | Không |

**Kết luận GAP:** 0 GAP — cùng vai trò, cùng cấu hình 2 thư mục (1 đủ đk + 1 rỗng), cùng thao tác bulk. Số biểu mẫu của thư mục đủ đk khác nhau (đối tác nhiều BM, mình 1 BM) nhưng điều kiện SRS chỉ yêu cầu "≥1 biểu mẫu" (`srs-fr-09-bieu-mau.md:220`) — cả hai đều thoả cùng một lớp điều kiện, chênh lệch số BM không đổi kết quả eligibility.

**Quan sát:**
- Modal xác nhận: *"Công khai 2 thư mục? Các thư mục sẽ được đồng bộ lên Cổng PLQG."*
- Toast (đo bằng observer, 1 toast, không nhân đôi): *"Công khai 1/2 thư mục, 1 thất bại."*
- Network: 1 request `POST /api/v1/thu-muc-bieu-maus/batch-cong-khai`.
- After-state: **QA Hidden Folder 715 (đủ đk) → Đã công khai + Đã đồng bộ (THÀNH CÔNG)**; BM-B3-0720-Rong-1 (rỗng) → vẫn Nháp (thất bại đúng — thư mục rỗng).

**Đối chiếu 2 sub-issue đối tác báo:**

1. **Logic "0/2" (thư mục đủ đk cũng thất bại):** KHÔNG tái hiện. Thư mục đủ điều kiện (Nháp + ≥1 BM) **được công khai thành công** qua bulk → kết quả thực là **"1/2"**, không phải "0/2". → sub-issue logic: **Reject** (không tái hiện trên env hiện tại).

2. **Wording "Công khai X/Y thư mục, Z thất bại" khác thiết kế:** Message này KHÔNG có trong SRS. `srs-fr-09-bieu-mau.md:250-251` (§Error Handling) chỉ định nghĩa ERR-CK-01 (thư mục rỗng đơn lẻ không công khai được) + WRN-CK-01, KHÔNG có message chuẩn cho công khai hàng loạt một phần. Expected của đối tác ("Đã công khai {X}. {Y} không đủ điều kiện...") cũng không có nguồn SRS. → sub-issue wording: **BA confirm** (SRS silent về message bulk).

**Verdict tổng hợp (đa sub-issue):** Không có sub-issue nào Open (logic Reject + wording BA confirm) → verdict = **BA confirm** (còn ≥1 sub-issue cần BA chốt, không có Open).
