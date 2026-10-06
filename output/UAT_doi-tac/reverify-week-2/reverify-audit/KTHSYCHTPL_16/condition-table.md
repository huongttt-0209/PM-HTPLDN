# KTHSYCHTPL_16 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra hiển thị Nhóm 5 — Phân công Người hỗ trợ (SCR-V.I-03).
**Evidence đối tác:** `partner-evidence/KTHSYCHTPL_16.jpg` — vụ việc **VV-STP-AG-20260709-001**, trạng thái **"Đã tiếp nhận"**, tài khoản **CB NV DP 01 (AG) / CB_NV_DP**; nhóm **"Phân công Người hỗ trợ / Tư vấn viên"** VẪN hiển thị.
**Đối tác phản ánh:** hệ thống hiển thị Nhóm 5 — Phân công Người hỗ trợ ở các bản ghi **chưa đạt trạng thái yêu cầu**.

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

Nhóm tranh chấp — **"Phân công Người hỗ trợ / Tư vấn viên"**: Nhóm hiển thị đầy đủ: bảng "Lĩnh vực / Đơn vị quản lý / NHT-TVV phụ trách" (giá trị "—") + bảng Tư vấn viên rỗng

Ảnh: `../../bug-reports/image/BUG-KTHSYCHTPL_16-19-web-nhom5678-hien-o-trang-thai-da-tiep-nhan.png`

## Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:1723` (SCR-V.I-03, Thành phần màn hình row 8 — Accordion 5 "Phân công xử lý"), cột **"Điều kiện hiển thị"**: **Khi VV đã qua **DA_PHAN_CONG** ("Đã phân công")**.
- **Thực tế web** — vụ việc đang ở **"Đã tiếp nhận"** (chưa qua trạng thái trên) nhưng nhóm **VẪN hiển thị**.
- **Kết luận** — app **không áp dụng điều kiện hiển thị theo trạng thái** mà SRS quy định → **Open**. Kỳ vọng của đối tác ("chỉ hiển thị khi hồ sơ đã qua trạng thái …") **trùng khớp với SRS**, không phải tranh chấp đặc tả.
