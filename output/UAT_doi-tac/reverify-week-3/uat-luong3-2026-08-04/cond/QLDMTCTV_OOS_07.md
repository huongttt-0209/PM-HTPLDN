# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_07 (dòng 333) — Màn rỗng chỉ hiện chữ "Trống"

**Kết luận:** Pass — vùng rỗng nay có đủ hình minh họa + câu "Chưa có tổ chức tư vấn nào trong mục này", và thẻ "Mới đăng ký" khi rỗng có thêm nút "+ Thêm tổ chức tư vấn".

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (cbnv_tw, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ cấp Trung ương (`cbnv_tw_04`), Cục Bổ trợ tư pháp – Bộ Tư pháp | `cbnv_tw` — `CB_NV_TW`, đơn vị "Bộ Tư Pháp · Cục Bổ trợ tư pháp" (cùng vai trò + cùng cấp + cùng đơn vị) | Không |
| Màn hình / entity + trạng thái | Danh sách Tổ chức tư vấn, các thẻ không có bản ghi | Đúng màn `/chuyen-gia-tvv/to-chuc`; đo ở **4 thẻ rỗng**: Mới đăng ký · Đã từ chối · Tạm dừng · Vô hiệu hóa | Không |
| Dữ liệu tiền đề | Thẻ "Đã từ chối", "Tạm dừng", "Vô hiệu hóa" chưa có tổ chức nào | **Không phải dựng gì** — 3 thẻ đó vẫn đang có 0 bản ghi thật (đo bằng `GET /api/v1/to-chuc-tu-vans` → chỉ có HOAT_DONG / CHO_PHE_DUYET / MOI_DANG_KY). Riêng thẻ "Mới đăng ký" cũng đang rỗng ở thời điểm đo nên **đo được luôn nút "+ Thêm tổ chức tư vấn"** — thứ vòng 1 chưa kiểm được | Không |
| Thao tác / input | Bấm từng thẻ rồi đọc nội dung vùng bảng | Bấm lần lượt 4 thẻ, đọc `innerText` vùng rỗng + kiểm sự tồn tại của phần tử hình minh họa (`.ant-empty-image > svg`) | Không |

**Số đo từng thẻ rỗng:**

- Thẻ "Mới đăng ký" — 0 dòng — CÓ hình minh họa — chữ "Chưa có tổ chức tư vấn nào trong mục này" — trong vùng rỗng có nút **"+ Thêm tổ chức tư vấn"**.
- Thẻ "Đã từ chối" — 0 dòng — CÓ hình minh họa — chữ "Chưa có tổ chức tư vấn nào trong mục này" — không có nút (đúng đặc tả).
- Thẻ "Tạm dừng" — 0 dòng — CÓ hình minh họa — chữ "Chưa có tổ chức tư vấn nào trong mục này" — không có nút.
- Thẻ "Vô hiệu hóa" — 0 dòng — CÓ hình minh họa — chữ "Chưa có tổ chức tư vấn nào trong mục này" — không có nút.

**Về chữ "Trống":** không còn hiển thị cho người dùng. Chuỗi "Trống" chỉ còn nằm trong thẻ `<title>` bên trong hình minh họa (phần dành cho trình đọc màn hình), không xuất hiện trên `innerText` và không thấy trên ảnh chụp.

**Bằng chứng:**
- `image/QLDMTCTV_OOS_07-v2-01-the-moi-dang-ky-rong-co-hinh-cau-huong-dan-va-nut-them.png` — thẻ "Mới đăng ký" rỗng: hình minh họa xám (hộp tài liệu) + dòng chữ "Chưa có tổ chức tư vấn nào trong mục này" + nút xanh "+ Thêm tổ chức tư vấn". Không có chữ "Trống".
- `image/QLDMTCTV_OOS_07-v2-02-the-vo-hieu-hoa-rong-co-hinh-va-cau-huong-dan.png` — thẻ "Vô hiệu hóa" rỗng: hình minh họa + câu hướng dẫn, không có nút thêm.
- Đặc tả: `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1649 (trạng thái rỗng: "hình ảnh + 'Chưa có tổ chức tư vấn nào trong mục này' + nút '+ Thêm tổ chức tư vấn' (chỉ ở tab Mới đăng ký)").
