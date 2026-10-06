# DKTGMLTVV_OOS_02 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 139 · Verdict Verify 2: `Pass`
> **Bug gốc (3 nhãn lệch đặc tả trên biểu mẫu Thêm mới Tư vấn viên):** tên nhóm 2 hiện *"Nghề nghiệp"*; ô giấy tờ tùy
> thân hiện *"Số CMND/CCCD"*; ô trình độ hiện *"Trình độ học vấn"*. Phần "Kết quả thực tế" của phiếu nói thêm: **màn
> hình chi tiết hồ sơ cũng hiển thị "CMND/CCCD"**.
> **Kết quả mong đợi:** đúng `srs-fr-04-chuyen-gia-tvv.md` — `:1500` nhóm 2 là *"Thông tin nghề nghiệp"* · `:1495` mục
> 2.7 là *"Số Căn cước công dân *"* · `:1503` mục 3.1 là *"Trình độ *"*. Đối chiếu thêm `:1481`: biểu mẫu SCR-IV-02 chia
> **5 nhóm** — *"Thông tin cá nhân, Thông tin nghề nghiệp, Tổ chức & Mạng lưới, File đính kèm, Ghi chú"*.
> Bug đọc trên biểu mẫu còn trống, nhưng **biểu mẫu chỉ mở được bằng đúng vai trò Người hỗ trợ** ⇒ vẫn điền bảng này để
> chứng minh đã đọc nhãn ở đúng vai trò, không đọc nhờ vai trò khác.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5`.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | *"Người hỗ trợ pháp lý cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp"*; lần đo trước dùng `nht_qa_tw` | **`nht_tc001_btp_tw`** — `GET /api/v1/auth/me` trả `vaiTro ["NHT"]`, `capDonVi "TW"`, `donViId 00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - Bộ Tư pháp); thanh trên hiện `NHT TC001 Test BTP TW · NHT · BTP · TW` (thấy rõ trong cả 2 ảnh). `nht_qa_tw` **không tồn tại** trên môi trường này nên dùng NHT cùng vai trò + cùng cấp + cùng đơn vị (Rule 7) | Không |
| Màn hình + lối vào | *"Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → Thêm mới"* | Đúng lối vào đó — `/chuyen-gia-tvv/tao-moi`, tiêu đề *"Thêm mới Tư vấn viên"* | Không |
| Trạng thái biểu mẫu | *"Không cần nhập dữ liệu — chỉ đọc nhãn trên biểu mẫu còn trống"* | Đọc trên biểu mẫu **còn trống hoàn toàn** (mọi ô hiện gợi ý, chưa gõ gì), đúng như phiếu | Không |
| Phạm vi nhãn phải đọc | Phiếu nêu **3 nhãn** (bước 2/3/4) **+ 1 chỗ nhắc thêm** ở phần Kết quả thực tế: nhãn trên **màn chi tiết hồ sơ** | Đọc **cả 4 chỗ**: 3 nhãn trên biểu mẫu + mở **màn chi tiết** một hồ sơ tư vấn viên (`/chuyen-gia-tvv/b0077951-…`) để đọc nhãn giấy tờ tùy thân ở đó | Không |
| Cách quan sát | *"Đọc nhãn rồi đối chiếu bảng Danh sách trường của SCR-IV-02"* | Đọc bằng máy (`innerText` — chỉ chữ nhìn thấy) **và** chụp ảnh đối chiếu; đồng thời liệt kê **đủ tên 5 nhóm** của biểu mẫu để so với `:1481`, không chỉ so mỗi nhóm 2 | Không |

## Kết quả đo

**Đủ 3 nhãn của phiếu đều đúng đặc tả:**

- Tên **nhóm 2** = **"Thông tin nghề nghiệp"** (`:1500`). Đủ 5 nhóm đúng thứ tự `:1481`:
  *Thông tin cá nhân · Thông tin nghề nghiệp · Tổ chức & Mạng lưới · File đính kèm · Ghi chú*.
- Nhãn ô giấy tờ tùy thân = **"Số Căn cước công dân"** kèm dấu sao đỏ (`:1495`) — ảnh `DKTGMLTVV_OOS_02-v2-02`.
- Nhãn ô trình độ = **"Trình độ"** kèm dấu sao đỏ (`:1503`) — ảnh `DKTGMLTVV_OOS_02-v2-01`.

**Chỗ phiếu nhắc thêm cũng đã đúng:** màn hình **chi tiết** hồ sơ nay hiển thị **"Căn cước công dân"**
(*"Giới tính NAM | Căn cước công dân 038119880503"*), không còn *"CMND/CCCD"*.

## Đã cố BÁC BỎ kết luận `Pass` bằng những cách nào

1. **Nghi "chỉ sửa nhãn ở màn Thêm mới, màn chi tiết vẫn chữ cũ"** (đúng ý phiếu nhắc thêm) → **BÁC**: mở màn chi tiết
   đọc lại, đã là *"Căn cước công dân"*.
2. **Nghi "đọc trúng lúc trang chưa dựng xong nên ra nhãn tạm"** → **BÁC**: đọc sau khi biểu mẫu dựng đủ 28 ô, và đọc
   **hai lần ở hai lần mở biểu mẫu khác nhau** trong phiên, kết quả giống nhau.
3. **Nghi "sửa nhóm 2 nhưng làm lệch tên nhóm khác"** → **BÁC**: liệt kê đủ **5 tên nhóm**, khớp nguyên văn `:1481`.
4. **Nghi "chữ hiển thị khác chữ trong mã nguồn / có chữ ẩn"** → **BÁC**: đọc bằng `innerText` (chỉ lấy chữ nhìn thấy)
   **và** chụp ảnh pixel, hai phép đo khớp nhau.
5. **Nghi "đọc nhãn bằng vai trò khác nên không đại diện"** → **BÁC**: toàn bộ phép đọc thực hiện bằng tài khoản **NHT**
   đúng cấp + đúng đơn vị, tên vai trò hiện ngay trên thanh tiêu đề trong ảnh.

**Đã cân nhắc, KHÔNG tính là lỗi của phiếu này:** (a) trên **màn chi tiết**, tiêu đề khối vẫn là *"Nghề nghiệp"* —
`:1500` quy định tên nhóm của **SCR-IV-02** (biểu mẫu Thêm mới/Chỉnh sửa), còn màn chi tiết là **SCR-IV-03** và đã được
BA chốt 2026-07-30 là *"mô tả rút gọn ở cấp nhóm"*, không ràng buộc tên khối; (b) gợi ý trong ô là *"9-12 chữ số"*
trong khi `:1495` chỉ quy định *"tối đa 12 ký tự"* — không trái đặc tả (đúng như dev đã nêu ở vòng trước).

**Kết luận: 0 GAP** — đúng vai trò Người hỗ trợ pháp lý cấp TW cùng đơn vị, đúng màn hình, đúng trạng thái biểu mẫu
trống, và đã đọc **cả 4 chỗ** mà phiếu đề cập chứ không chỉ 3 nhãn ở phần Kết quả mong đợi.
