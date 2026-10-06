# Bảng đối chiếu điều kiện — QLDMCQDVQL_05 (row 139)

**Bug:** Tìm kiếm cây "Cơ quan đơn vị" không ra kết quả → không hiện message "Không tìm thấy...".
**Verdict:** `BA confirm` (actual tái hiện đúng; SRS silent về message empty-search).

| Điều kiện có thể đổi kết quả | Đối tác (ảnh full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT (màn Quản trị hệ thống) | QTHT (`admin`) | Không |
| Entity + trạng thái | Cây đơn vị có data, search lọc còn 0 node | Cây có node "Cục Bổ trợ tư pháp", search lọc còn 0 | Không |
| Input / filter / giá trị nhập | Từ khóa "tư pháp HCM" (không match) | Đúng từ khóa "tư pháp HCM" (không match) | Không |

**Kết luận:** Tái hiện đúng 100% điều kiện đối tác (cùng tab, cùng từ khóa, cùng kết quả 0 node). Vùng cây trắng, không message empty-state. Bất đồng nằm ở KỲ VỌNG (đối tác muốn message) vs SRS (không quy định) → `BA confirm`. 0 GAP.
