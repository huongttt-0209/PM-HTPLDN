# Bảng đối chiếu điều kiện — TKHDVMTH_07 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** Khi chọn trạng thái "Tiếp nhận", hệ thống hiển thị các bản ghi bao gồm "Đang xử lý" và "Tiếp nhận".

**Evidence:** `TKHDVMTH_07_v2.webm` — frame `t003.03s` (thanh lọc **Trạng thái = "Tiếp nhận"**, thẻ **"Đang xử lý 21"** đang active, URL `htpldn-uat.ospgroup.vn/hoi-dap?sortBy=ngayTao&sortOrder=ASC&page=1&trangThai=TIEP_NHAN`, header **Cán bộ NV Trung ương · CB_NV_TW · BTP·TW**, bảng toàn dòng "Đang xử lý"), frame `t009.06s` (đối tác bôi đen chữ "Tiếp nhận" ở HD-20260510-003 — bảng lẫn cả 2 trạng thái).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ NV Trung ương (`CB_NV_TW`), đơn vị BTP · TW — đọc ở header frame `t003.03s` | `cbnv_tw` / CB_NV_TW, đơn vị BTP · TW (Cục Bổ trợ tư pháp) — đúng vai trò, đúng đơn vị | Không |
| Môi trường | `htpldn-uat.ospgroup.vn` (thanh địa chỉ frame `t003.03s`, quay 21/07/2026 16:08) | Đúng `htpldn-uat.ospgroup.vn` — đăng nhập trực tiếp env đối tác ngày 27/07/2026 | Không |
| Màn hình + thẻ (tab) đang đứng | Màn "Quản lý hỏi đáp, vướng mắc pháp lý", thẻ **"Đang xử lý"** active (badge 21) | Đúng màn đó, thẻ **"Đang xử lý"** active (badge 22 — dữ liệu tăng 1 bản ghi mới trong tuần) | Không |
| Input / bộ lọc | Ô lọc **Trạng thái = "Tiếp nhận"**, bấm Tìm kiếm | Đúng: chọn "Tiếp nhận" trong ô lọc Trạng thái rồi bấm Tìm kiếm | Không |

**Kết luận:** 0 GAP — tái hiện trên **chính môi trường đối tác**, đúng vai trò, đúng thẻ, đúng bộ lọc.

Phép đo đầy đủ (4 truy vấn phân biệt) + đối chiếu SRS vs web: xem [`../reverify-audit/TKHDVMTH_07/audit.md`](../reverify-audit/TKHDVMTH_07/audit.md).
