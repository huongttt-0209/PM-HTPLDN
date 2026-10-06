# Bảng đối chiếu điều kiện — VVDTN_09 (row 199)

- **Case:** VVDTN_09 — Kiểm tra chức năng **Xóa bộ lọc** trên màn Báo cáo thống kê (SCR-IX-01), loại BC = **BC Vụ việc đã tiếp nhận** (FR-IX).
- **Verdict:** `BA confirm` — nút reset bộ lọc CÓ tồn tại (nút **"Làm mới"**, đúng SRS SCR-IX-01 item 2 dòng 1042) nhưng KHÁC tên đối tác kỳ vọng ("Xóa bộ lọc") + reset về **trống** thay vì pre-fill Kỳ=Tháng như KQMĐ đối tác mô tả.
- **Tài khoản verify:** `cbnv_tw_03` / CB_NV_TW (CB Nghiệp vụ Trung ương — phạm vi Toàn quốc).
- **Ngày verify:** 21/07/2026, Chrome DevTools MCP, `https://18.143.165.120.nip.io/bao-cao`.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | admin (Quản trị viên QTHT), phạm vi Toàn quốc — evidence `partner-evidence/VVDTN_09.jpg` | cbnv_tw_03 (CB Nghiệp vụ TW), phạm vi Toàn quốc — toolbar SCR-IX-01 item 2 "Luôn hiển thị" mọi role; cả 2 role đều thấy nút "Làm mới", KHÔNG thấy "Xóa bộ lọc" | Không |
| Entity + trạng thái (đã Xem báo cáo hay chưa) | Đã Xem báo cáo (màn hiện kết quả) rồi tìm nút reset | Test cả khi đã Xem báo cáo: bấm "Làm mới" → xóa bộ lọc VÀ xóa kết quả, không tự tải lại (Xem báo cáo disabled trở lại) | Không |
| Input / filter / giá trị nhập | Nhập tiêu chí lọc rồi tìm nút "Xóa bộ lọc" (theo Các bước sheet) | Kỳ=Năm 2026 (đối chiếu toolbar cùng màn SCR-IX-01) → toàn bộ bộ lọc về trống, Đơn vị về "Toàn quốc" | Không |

**Kết luận:** 0 GAP. Đối tác quan sát ĐÚNG thực tế (màn không có nút tên "Xóa bộ lọc") nhưng kỳ vọng nút tên/hành vi khác SRS (SRS spec "Nút Làm mới") → bất đồng về ĐẶC TẢ → `BA confirm`, KHÔNG tự Reject.

- **Evidence quan sát (real-data):** `reverify-audit/VVDTN_09/VVDTN_09-toolbar.png`
