# Bảng đối chiếu điều kiện — QLLKHDTBD_50 (re-verify vòng 2, 05/08/2026)

Loại bug: **bảng danh sách Kế hoạch đào tạo thiếu cột và sai định dạng số tiền** → có ý "Số chương trình" phụ thuộc dữ liệu chương trình thật ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 2*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy **5 nội dung của phiếu** liệt kê trong note (ô tích chọn dòng · cột "Người tạo" · cột "Ngày tạo" · định dạng cột ngân sách · cột "Số chương trình" đếm đúng) làm điều kiện phải hết lỗi. Note kết luận "đã đạt" nhưng **vẫn tự đo lại đủ 5 nội dung**, không lấy kết luận của note làm căn cứ.

| Điều kiện | Bug gốc (phiếu + note vòng 2) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | Tài khoản cán bộ (phiếu đã kiểm với cán bộ nghiệp vụ và cán bộ phê duyệt, kết quả như nhau) | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách | Đúng đường đó, đi bằng menu bên trái | Không |
| Tiền đề dữ liệu | Có ít nhất 1 kế hoạch đã nhập ngân sách dự kiến; tổng 14 kế hoạch | Danh sách hiện **14 kế hoạch**, trong đó **KH-20260803-0001** có ngân sách 100.000.000, **KH-20260714-0001** và **KH-20260712-0001** có 1.000.000, **KH-20260712-0002** có 2.000.000, phần còn lại bỏ trống | Không |
| Nội dung 1 — ô tích chọn dòng | Toàn trang không có ô tích nào | Bấm thật ô tích ở **dòng tiêu đề** rồi đếm số dòng được chọn theo | Không |
| Nội dung 2 — cột "Người tạo" | Thiếu cột | Đọc thanh tiêu đề bảng sau khi **cuộn ngang hết sang phải** + đọc giá trị từng dòng | Không |
| Nội dung 3 — cột "Ngày tạo" | Thiếu cột | Như trên, kèm kiểm định dạng ngày/tháng/năm | Không |
| Nội dung 4 — định dạng cột ngân sách | Hiện số thô "100000000.00", rỗng không hiện "—" | Đọc giá trị thật của cột **Ngân sách (VNĐ)** trên cả 14 dòng | Không |
| Nội dung 5 — cột "Số chương trình" | Thiếu cột; vòng trước còn lỗi đếm sai | Đọc số của **cả 14 dòng** rồi đối chiếu với **dữ liệu chương trình đào tạo thực tế** (đếm từng chương trình xem thuộc kế hoạch nào) | Không |
| Cách đo | Note yêu cầu đo cả với dữ liệu phát sinh mới, không chỉ dữ liệu cũ | Ngoài đối chiếu tĩnh, **tạo mới 1 chương trình đào tạo qua giao diện** gắn vào một kế hoạch cụ thể rồi quay lại đọc lại bảng (không chấm bằng quan sát tĩnh) | Không |
| Số cách đo | Phiếu đo 2 cách: đọc tiêu đề bảng trong mã trang + nhìn ảnh sau khi cuộn ngang | Đo **2 cách**: đọc thẳng thanh tiêu đề và ô dữ liệu của bảng; và ảnh chụp màn sau khi cuộn ngang hết sang phải | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò và màn hình, đủ dữ liệu để đọc cả 5 nội dung, đo bằng 2 cách và có thêm phép thử với dữ liệu phát sinh mới.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw`)

Thanh tiêu đề bảng đọc được đủ **12 cột**: ô tích chọn · Mã kế hoạch · Tên kế hoạch · Năm · Từ ngày · Đến ngày · Ngân sách (VNĐ) · **Số chương trình** · Trạng thái · **Người tạo** · **Ngày tạo** · Hành động.

### Nội dung 1 — ô tích chọn dòng

- ✅ **Đã có ô tích** ở cột đầu bảng, cả ở dòng tiêu đề lẫn từng dòng dữ liệu.
- ✅ Tích ở dòng tiêu đề → **14/14 dòng đang hiển thị được chọn theo**.
  Ảnh: [`../image/QLLKHDTBD_50-r2-danh-sach-du-cot-tich-chon.png`](../image/QLLKHDTBD_50-r2-danh-sach-du-cot-tich-chon.png)

### Nội dung 2 + 3 — cột "Người tạo" và "Ngày tạo"

- ✅ **Cột "Người tạo" đã có**, hiện đúng người lập từng kế hoạch: "CB Nghiệp vụ - Trung ương", "CB Nghiệp vụ - Địa phương #01", "CB Nghiệp vụ - Bộ ngành", "CB Nghiệp vụ - Trung ương #03", "Quản trị hệ thống", "Hệ thống HTPLDN".
- ✅ **Cột "Ngày tạo" đã có**, đúng dạng ngày/tháng/năm: 03/08/2026 · 31/07/2026 · 25/07/2026 · 15/07/2026 · 14/07/2026 · 12/07/2026 · 30/06/2026.
  Ảnh (đã cuộn ngang hết sang phải): [`../image/QLLKHDTBD_50-r2-cot-nguoi-tao-ngay-tao-so-chuong-trinh.png`](../image/QLLKHDTBD_50-r2-cot-nguoi-tao-ngay-tao-so-chuong-trinh.png)

### Nội dung 4 — định dạng cột ngân sách

- ✅ **Đúng định dạng dấu chấm kèm đơn vị**: `100.000.000 đ` · `1.000.000 đ` · `2.000.000 đ`. Không còn dòng nào ra số thô kiểu "100000000.00".
- ✅ **Kế hoạch chưa nhập ngân sách hiện dấu "—"** (10/14 dòng), không để trống trơn.

### Nội dung 5 — cột "Số chương trình" đếm đúng

- ✅ Số đọc trên bảng: KH-20260803-0001 = **1** · KH-20260731-0002 = **1** · KHDT-QAW7-01 = **4** · KHDT-2026-001 = **2** · KHDT-SEED-0001 = **1** · 9 kế hoạch còn lại = **0**.
- ✅ **Đối chiếu với dữ liệu chương trình đào tạo thực tế**: kho đang có **9 chương trình**, đếm theo kế hoạch mà từng chương trình gắn vào ra đúng **1 · 1 · 4 · 2 · 1** cho năm kế hoạch trên. **Khớp tuyệt đối cả 14 dòng**, cộng dồn cả bảng bằng đúng tổng số chương trình đang có.
- ✅ **Cập nhật đúng với dữ liệu phát sinh mới**: tạo mới chương trình **"QA-REVERIFY-0805 CTDT kiem cot So chuong trinh"** qua giao diện, gắn vào kế hoạch **KH-20260731-0002**; lưu xong quay lại bảng danh sách thì kế hoạch đó **chuyển từ 1 thành 2** và tổng cả bảng tăng từ **9 lên 10**. Cột này không phải số cũ đóng băng.

### Kết luận

Tự đo lại đủ cả 5 nội dung của phiếu, không lấy kết luận sẵn của lần trước: bảng danh sách Kế hoạch đào tạo nay có ô tích chọn dòng, có cột "Số chương trình" đếm đúng (kể cả với dữ liệu mới tạo), có cột "Người tạo" và "Ngày tạo", cột ngân sách đúng định dạng dấu chấm kèm đơn vị và hiện "—" khi bỏ trống → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Bảng phải **cuộn ngang** mới thấy hết các cột "Người tạo" / "Ngày tạo" / "Hành động" ở bề ngang 1440. Không thuộc phạm vi phiếu, chỉ ghi lại.
- Ô chọn "Kế hoạch năm" khi tạo chương trình chỉ liệt kê **5 kế hoạch** (các kế hoạch đã duyệt / đã công khai), nên không thể gắn chương trình vào kế hoạch còn ở trạng thái Nháp hay Chờ duyệt. Đây là hành vi hợp lý theo quy trình, chỉ ghi lại để giải thích vì sao phép thử dữ liệu mới được gắn vào kế hoạch đang có sẵn 1 chương trình.
- Dữ liệu do kiểm thử tạo: chương trình đào tạo **"QA-REVERIFY-0805 CTDT kiem cot So chuong trinh"** (lĩnh vực Thương mại) thuộc kế hoạch KH-20260731-0002.
