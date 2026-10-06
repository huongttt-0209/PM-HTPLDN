# Bảng đối chiếu điều kiện — QLTVV_24 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** "Khi nhấn **Xóa** file ảnh chân dung đính kèm, hệ thống hiển thị thông báo **'Lỗi hệ thống. Vui lòng thử lại sau'**".

**Evidence:** `QLTVV_22_v2.jpg` — ảnh chụp toàn màn hình (đối tác đánh số tệp lệch một bậc so với mã ca kiểm thử; đối chiếu theo **nội dung**, không theo số hiệu).
Đọc được từ ảnh:
- Đường dẫn: `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/d973a0e6-e63b-4499-b7a2-ea4bcf5c4e06/**chinh-sua**` — màn **Chỉnh sửa hồ sơ tư vấn viên**.
- Thanh trên: **"BTP · TW"**, **"Cán bộ NV Trung ương"**, **"CB_NV_TW"**.
- Bản ghi: **TVV-BTP-TW-0059** — "Hoàng Thị Thanh Thảo"; Loại "Tư vấn viên (TVV)".
- Khối **"Ảnh chân dung"**: vùng kéo thả "Tối đa 1 tệp. Định dạng: .jpg, .png. Dung lượng tối đa: 5MB/tệp." + **một dòng tệp đã lưu** nhãn "📎 Ảnh chân dung" kèm 2 liên kết **"Xem"** và **"Xóa"**; bên phải có ảnh xem trước hiển thị bình thường ⇒ tệp đã lưu vào hồ sơ từ trước.
- Hộp thông báo đỏ: **"Lỗi hệ thống, vui lòng thử lại sau"**.
- Đồng hồ máy: 25/07/2026 14:21, trình duyệt Chrome trên Windows.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / cấp | Cán bộ Nghiệp vụ **Trung ương** (`CB_NV_TW`), badge "BTP · TW" | `cbnv_tw` — vai trò **CB_NV_TW**, badge "BTP · TW" (trùng khít) | Không |
| Màn hình | Màn **Chỉnh sửa hồ sơ tư vấn viên** `/chuyen-gia-tvv/{id}/chinh-sua` | Cùng đường dẫn `/chuyen-gia-tvv/de22ef5c-…/chinh-sua` | Không |
| Loại bản ghi | Tư vấn viên (TVV), mã `TVV-BTP-TW-0059` | Tư vấn viên (TVV), mã `TVV-BTP-TW-0020` — cùng loại, cùng dải mã đơn vị | Không |
| Quan hệ đơn vị người thao tác ↔ hồ sơ | Mã `TVV-BTP-TW-…` ⇒ cùng Cục Bổ trợ tư pháp – Bộ Tư pháp với người thao tác | Cùng đơn vị — hồ sơ thuộc "Cục Bổ trợ tư pháp - Bộ Tư pháp", trùng đơn vị của `cbnv_tw` | Không |
| Trạng thái tệp ảnh trước thao tác | Ảnh **đã lưu vào hồ sơ** (dòng tệp hiện sẵn ngay khi mở màn sửa, có ảnh xem trước) | Ảnh **đã lưu vào hồ sơ**: tải lên → bấm **Lưu** → tải lại màn sửa mới bấm Xóa; đọc dữ liệu hồ sơ ngay trước khi bấm, `anhChanDungFileId = c100d6bf-…` (khác rỗng) | Không |
| Nhãn dòng tệp | "Ảnh chân dung — Xem — Xóa" | "Ảnh chân dung — Xem — Xóa" (đọc trực tiếp từ giao diện, trùng từng chữ) | Không |
| Nút được bấm | Liên kết **"Xóa"** trên dòng tệp ảnh chân dung | Chọn đúng dòng chứa chữ "Ảnh chân dung", rồi chọn phần tử có nhãn đúng bằng **"Xóa"** trong dòng đó mới bấm | Không |
| Trình duyệt / kích thước cửa sổ | Chrome trên Windows, cửa sổ tối đa | Chrome 1440×900 — kết luận dựa trên mã trả về của lời gọi máy chủ nên không phụ thuộc kích thước cửa sổ | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng màn, cùng loại hồ sơ, cùng quan hệ đơn vị, cùng trạng thái tệp (đã lưu), cùng nút bấm.

**Kết quả tái hiện: TÁI HIỆN 100%.** Bấm "Xóa" trên ảnh chân dung đã lưu → hộp thông báo đỏ **"Lỗi hệ thống, vui lòng thử lại sau"**, dòng tệp **vẫn còn nguyên**, lời gọi xóa trả mã **500**.
Phép thử đối chứng cô lập được điều kiện gây lỗi (ảnh còn đang gắn vào hồ sơ ⇒ lỗi hệ thống; ảnh chưa gắn ⇒ xóa được):
xem [`../reverify-audit/QLTVV_24/audit.md`](../reverify-audit/QLTVV_24/audit.md).
