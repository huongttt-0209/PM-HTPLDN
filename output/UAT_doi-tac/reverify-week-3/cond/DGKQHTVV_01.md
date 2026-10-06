# Bảng đối chiếu điều kiện — DGKQHTVV_01

Loại bug: **Vụ việc đã "Hoàn thành" nhưng không hiện nút chức năng đánh giá (Nhóm 8).** Việc nút [Đánh giá] có hiển thị hay không phụ thuộc role (CB NV) + state (HOAN_THANH) + scope (đúng đơn vị) → điền bảng, xác nhận app test đúng điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res DGKQHTVV_01-2.jpg + video) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **Cán bộ NV Trung ương** — hiển thị góc phải "Cán bộ NV Trung ương / CB_NV_TW" | `cbnv_tw` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ - Trung ương), đơn vị BTP·TW | Không |
| Trạng thái vụ việc | **"Hoàn thành"** — Dòng thời gian ghi "Hoàn thành 10/07/2026 09:54" | VV-BTP-TW-20260712-001 ở **HOAN_THANH** ("Hoàn thành") | Không |
| Đơn vị (scope) | CB NV cùng đơn vị vụ việc (BTP·TW, vụ việc thuộc Cục Bổ trợ tư pháp - BTP) | `cbnv_tw` đơn vị BTP·TW, là CB NV được giao của vụ việc → cùng đơn vị | Không |
| Màn hình/thao tác | Mở màn chi tiết → mục **"Đánh giá"** (Nhóm 8) để đánh giá kết quả hỗ trợ | Mở chi tiết → thanh hành động + mở mục "Đánh giá" (Nhóm 8) | Không |
| Hiện tượng cần quan sát | Mục "Đánh giá" hiển thị **"Chưa có thông tin"**, không có nút chức năng đánh giá | Thanh hành động KHÔNG có nút [Đánh giá]; mục "Đánh giá" chỉ hiện "Chưa có thông tin", không có biểu mẫu chấm điểm | Không |

**Kết luận: 0 GAP về role/state/data.** Đối tác dùng **cùng vai trò (CB_NV_TW)** + **cùng trạng thái (Hoàn thành)** + cùng màn "Đánh giá" (Nhóm 8) như mình test → điều kiện trùng khớp hoàn toàn. Kết quả:

- **Tái hiện đúng:** thanh hành động không có nút [Đánh giá]; mục "Đánh giá" chỉ hiển thị "Chưa có thông tin" (chỉ đọc), không có ô nhập điểm/nhận xét, không có nút gửi → CB NV không thể đánh giá vụ việc qua giao diện.
- **Không phải trạng thái rỗng thiếu data:** gọi API đánh giá trực tiếp (thân rỗng) trả **HTTP 422** *"Điểm chất lượng phải từ 0-10"* → **máy chủ đã có chức năng đánh giá và cho phép chính tài khoản này** (nếu thiếu quyền sẽ trả 403). → Lỗi nằm ở **giao diện thiếu nút + biểu mẫu**, không phải thiếu dữ liệu. → Log **BUG-DGKQHTVV_01** (Major).

Chi tiết: xem [`../reverify-audit/DGKQHTVV_01/audit.md`](../reverify-audit/DGKQHTVV_01/audit.md).
