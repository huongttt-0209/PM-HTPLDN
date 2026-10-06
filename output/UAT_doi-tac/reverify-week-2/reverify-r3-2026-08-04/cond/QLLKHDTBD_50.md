# QLLKHDTBD_50 — Bảng đối chiếu điều kiện (re-verify vòng 2 lần 2, 04/08/2026)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` dòng 144. Vòng trước (04/08 16:03) QA chấm `Reopen` vì
> **4/5 ý đã đạt, còn ý "Số chương trình" luôn hiện 0**. Sau đó dev đặt lại `Trạng thái dev fix 2` = `dev done`
> ⇒ verify lại toàn bộ 5 ý.
>
> Bug gốc: bảng `Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách` thiếu **ô tích chọn dòng**, cột
> **Số chương trình**, cột **Người tạo**, cột **Ngày tạo**; cột ngân sách hiện số thô `100000000.00`.
> Bug gốc gộp 5 ý + phiếu ghi rõ đã kiểm bằng 2 vai trò cán bộ ⇒ có chiều vai trò ⇒ bắt buộc điền bảng này.

**Môi trường đo:** `https://18.143.165.120.nip.io` (đúng môi trường ghi trong `input/input.md`) ·
nhãn bản dựng **HTPLDN · V1.0.6** — **mới hơn** bản `V1.0.5` của vòng trước.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (04/08/2026 lần 2) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Tài khoản cán bộ — phiếu ghi đã kiểm với Cán bộ nghiệp vụ Địa phương và Cán bộ phê duyệt Trung ương, kết quả như nhau | Đo bằng 2 vai trò: `cbnv_tw_02` (CB Nghiệp vụ Trung ương) và `cbpd_tw_02` (**Cán bộ phê duyệt Trung ương** — đúng 1 trong 2 vai trò phiếu nêu, thanh trên hiện `CB_PD_TW · BTP · TW`). Cả 2 ra kết quả **giống hệt nhau** | Không |
| Màn hình + thao tác | Menu Đào tạo, tập huấn → Kế hoạch đào tạo; xem thanh tiêu đề bảng, cuộn ngang hết sang phải | Cùng menu, cùng màn `/dao-tao/ke-hoach/danh-sach`, tab Tất cả; cuộn ngang hết (`scrollLeft 472 / scrollWidth 1600 / clientWidth 1128`) rồi chụp và **mở ảnh ra đọc** | Không |
| Dữ liệu tiền đề — kế hoạch đã nhập ngân sách | `KH-20260803-0001` ngân sách 100.000.000, `KH-20260803-0004`; tổng 14 kế hoạch | Kho có đúng **14 kế hoạch**, `KH-20260803-0001` ngân sách 100.000.000 vẫn còn; đủ 3 dạng ngân sách để soi định dạng: có số (`100.000.000 đ`, `1.000.000 đ`, `2.000.000 đ`) và bỏ trống (`—`) | Không |
| Dữ liệu tiền đề — kế hoạch phải CÓ chương trình con (điều kiện của ý số 5) | Bug gốc không nêu (khi đó cột chưa tồn tại nên không kiểm được giá trị) | Kho có **8 chương trình đào tạo thuộc 4 kế hoạch khác nhau**; ngoài ra **tự tạo thêm 1 chương trình qua giao diện** (`CTDT-BTP-TW-2026-0006`) gắn vào kế hoạch đang hiện 0 để có bản ghi sinh **sau** bản vá | Không |
| Trạng thái bản ghi | Bug gốc không giới hạn trạng thái | Bảng phủ đủ các trạng thái: Nháp 7 · Chờ duyệt 2 · Đã duyệt 4 · Đã công khai 1 (tổng 14). Chương trình con đo được gồm cả Dự thảo, Đã duyệt, Đang thực hiện, Hoàn thành | Không |

**Kết luận: 0 GAP.**

## Kết quả từng ý (bug gốc gộp 5 ý)

- **Ý 1 — thiếu ô tích chọn dòng:** đã có. Bấm ô tích ở dòng tiêu đề → **14/14 dòng đang hiển thị được tích theo**. ✅ ĐẠT
- **Ý 2 — thiếu cột Người tạo:** đã có, hiện tên người lập (`CB Nghiệp vụ - Địa phương #01`, `CB Nghiệp vụ - Trung ương #03`, `Quản trị hệ thống`, `Hệ thống HTPLDN`). ✅ ĐẠT
- **Ý 3 — thiếu cột Ngày tạo:** đã có, đúng dạng ngày/tháng/năm (`03/08/2026`, `31/07/2026`, `30/06/2026`). ✅ ĐẠT
- **Ý 4 — ngân sách hiện số thô `100000000.00`:** nay hiện `100.000.000 đ` · `1.000.000 đ` · `2.000.000 đ`; kế hoạch bỏ trống hiện `—`. Không còn chuỗi thô nào trong bảng. ✅ ĐẠT
- **Ý 5 — cột Số chương trình (vòng trước luôn bằng 0):** nay **đếm đúng**. ✅ ĐẠT — chi tiết bên dưới.

## Đo ý số 5 — cột Số chương trình

Đối chiếu từng dòng với dữ liệu chương trình đào tạo thật:

- `KHDT-QAW7-01` hiện **4** — thực tế có 4 chương trình trỏ vào.
- `KHDT-2026-001` hiện **2** — thực tế có 2.
- `KH-20260731-0002` hiện **1** — thực tế có 1.
- `KHDT-SEED-0001` hiện **1** — thực tế có 1.
- 10 kế hoạch còn lại hiện **0** — thực tế không có chương trình nào trỏ vào.
- Cộng dồn cả bảng = **8**, đúng bằng tổng số chương trình đào tạo trong kho (8). Không thừa, không thiếu.

**Phép thử quyết định (bản ghi tạo MỚI sau bản vá):** kế hoạch `KH-20260803-0001` đang hiện `0` →
tạo chương trình `CTDT-BTP-TW-2026-0006` qua giao diện Thêm mới, chọn Kế hoạch năm là kế hoạch đó
(đúng 1 request ghi, đúng 1 thông báo `Tạo chương trình đào tạo thành công`) → quay lại bảng danh sách,
dòng `KH-20260803-0001` **đổi từ `0` thành `1`**, tổng cả bảng lên **9** khớp 9 chương trình.

## Đã cố BÁC BỎ kết luận Pass

1. Không dừng ở "đã thấy cột có số khác 0" — đối chiếu **từng dòng** với dữ liệu chương trình thật, và
   kiểm cả chiều ngược lại (kế hoạch hiện 0 thì đúng là không có chương trình nào).
2. Nghi "chỉ đúng với dữ liệu cũ, bản ghi mới vẫn không được đếm" → tạo bản ghi mới qua giao diện, cột tăng đúng.
3. Nghi "do vai trò / phạm vi xem dữ liệu" → đo lại bằng `cbpd_tw_02` (Cán bộ phê duyệt Trung ương), giống hệt.
4. Nghi "4 ý kia sửa xong rồi lại hỏng" → soi lại đủ 4 ý, không ý nào tái phát.

⇒ **5/5 ý đã hết lỗi** ⇒ verdict `Pass` (cột `Verify 2`).

## Ghi chú ngoài phạm vi phiếu

Không phát hiện thêm bất thường nào ở màn Kế hoạch đào tạo trong lượt đo này.
