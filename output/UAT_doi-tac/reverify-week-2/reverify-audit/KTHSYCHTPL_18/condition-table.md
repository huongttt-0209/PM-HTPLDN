# KTHSYCHTPL_18 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra hiển thị Nhóm 7 — Phê duyệt (SCR-V.I-03).
**Evidence đối tác:** `partner-evidence/KTHSYCHTPL_18.jpg` — vụ việc **VV-STP-AG-20260709-001**, trạng thái **"Đã tiếp nhận"**, tài khoản **CB NV DP 01 (AG) / CB_NV_DP**; nhóm **"Phê duyệt"** VẪN hiển thị.
**Đối tác phản ánh:** hệ thống hiển thị Nhóm 7 — Phê duyệt ở các bản ghi **chưa đạt trạng thái yêu cầu**.

> **Lưu ý về evidence:** đối tác gắn **cùng một ảnh** cho KTHSYCHTPL_18 và KTHSYCHTPL_19 (`KTHSYCHTPL_18.jpg` và `KTHSYCHTPL_19.jpg` trùng mã băm MD5 `419907519bb4ae3b58ad0c54deaa2c36`). Ảnh đó cho thấy đủ cả nhóm "Phê duyệt" và nhóm "Đánh giá" nên vẫn đủ căn cứ cho cả 2 case.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_DP** — header "CB NV DP 01 (AG) / CB_NV_DP" | **`cbnv_dp`** — header "CB Nghiệp vụ - Địa phương / CB_NV_DP" | Không |
| Entity + trạng thái (state machine) | VV-STP-AG-20260709-001 — trạng thái **"Đã tiếp nhận"** (chưa qua trạng thái mà SRS yêu cầu để hiện nhóm này) | VV-STP-AG-20260712-002 — trạng thái **"Đã tiếp nhận"** (chưa qua trạng thái yêu cầu) | Không |
| Dữ liệu tiền đề (vụ việc chưa có dữ liệu của nhóm này) | Vụ việc mới tiếp nhận, chưa phân công / chưa xử lý / chưa duyệt / chưa đánh giá | Vụ việc tự seed, mới "Lưu & Tiếp nhận", chưa phân công / chưa xử lý / chưa duyệt / chưa đánh giá | Không |

## Quan sát (real-data)

Danh sách nhóm thực tế render trên màn Chi tiết vụ việc (trạng thái "Đã tiếp nhận", vai trò CB_NV_DP):

```json
["Thông tin Doanh nghiệp","Nội dung Yêu cầu","Tài liệu đính kèm","Kết quả kiểm tra",
 "Phân công Người hỗ trợ / Tư vấn viên","Kết quả hỗ trợ","Phê duyệt","Đánh giá","HĐ tư vấn liên kết"]
```

Nhóm tranh chấp — **"Phê duyệt"**: Nhóm hiển thị, nội dung "Chưa có thông tin"

Ảnh: `../../bug-reports/image/BUG-KTHSYCHTPL_16-19-web-nhom5678-hien-o-trang-thai-da-tiep-nhan.png`

## Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:1725` (SCR-V.I-03, Thành phần màn hình row 10 — Accordion 7 "Phê duyệt"), cột **"Điều kiện hiển thị"**: **Khi VV đã qua **CHO_PHE_DUYET** ("Chờ phê duyệt")**.
- **Thực tế web** — vụ việc đang ở **"Đã tiếp nhận"** (chưa qua trạng thái trên) nhưng nhóm **VẪN hiển thị**.
- **Kết luận** — app **không áp dụng điều kiện hiển thị theo trạng thái** mà SRS quy định → **Open**. Kỳ vọng của đối tác ("chỉ hiển thị khi hồ sơ đã qua trạng thái …") **trùng khớp với SRS**, không phải tranh chấp đặc tả.
