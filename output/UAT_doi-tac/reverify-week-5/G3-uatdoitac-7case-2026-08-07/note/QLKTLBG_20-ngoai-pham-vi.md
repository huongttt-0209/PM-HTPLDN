# GHI NHẬN NGOÀI PHẠM VI — phát hiện trong lượt đo QLKTLBG_20 (dòng 14)

> BRIEF §4.12 — thấy bug ngoài phạm vi case vẫn phải ghi nhận và báo lead; **không tự thêm dòng sheet mới**.
> Không mục nào dưới đây ảnh hưởng verdict dòng 14 (**✅ Pass**).

## 1. 🔴 Ô lọc không được đặt lại khi vào lại màn, và điều kiện "ẩn" đó được áp lại ở lần tìm kiếm kế tiếp

**Env:** `https://htpldn-uat.ospgroup.vn` · bản dựng **V1.0.10** · `cbnv_tw` (CB_NV_TW, TW) · 2026-08-07 ~17:23.
**Màn:** Đào tạo, tập huấn → Kho tài liệu / Bài giảng (`/dao-tao/bai-giang/danh-sach`, SCR-III-03).

**Quan sát thật, theo đúng thứ tự đã xảy ra:**

| # | Thao tác | URL | Lời gọi danh sách máy chủ nhận | Số bản ghi | Ô lọc "Công khai" hiển thị |
|---|---|---|---|---|---|
| 1 | Tải lại trang (phiên bàn giao từ lượt đo trước) | `…/danh-sach?congKhai=false&page=1` | `?congKhai=false&page=1&pageSize=20` | 6 | "Không công khai" |
| 2 | Bấm menu sidebar "Kho tài liệu / Bài giảng" | `…/danh-sach` (**đã sạch**) | `?page=1&pageSize=20` (**đã sạch**) | **7** | **vẫn "Không công khai"** |
| 3 | Gõ từ khoá + bấm "Tìm kiếm" | `…?search=…&congKhai=false&page=1` | `?keyword=…&congKhai=false&page=1&pageSize=20` | — | "Không công khai" |

**Vấn đề:** ở bước 2, điều hướng vào lại màn bằng menu **đặt lại địa chỉ và đặt lại kết quả đang hiển thị**
(danh sách quay về đủ 7 bản ghi, tức không còn điều kiện nào được áp), **nhưng biểu mẫu lọc thì không được đặt
lại** — ô "Công khai" vẫn giữ giá trị của lượt trước. Đến bước 3, giá trị còn sót đó **được gửi kèm** lên máy
chủ dù người dùng không chủ động chọn lại.

**Yêu cầu nghiệp vụ liên quan (mô tả, không kê đơn cách sửa):** trạng thái mà thanh lọc hiển thị phải phản ánh
đúng điều kiện đang thực sự được áp cho danh sách; người dùng phải nhìn thấy đúng những gì hệ thống sẽ dùng khi
tìm kiếm. Hiện tại có một khoảng thời gian màn hiển thị một điều kiện **không** được áp (bước 2), rồi điều kiện
đó **lại được áp** ở thao tác kế tiếp mà người dùng không chọn (bước 3).

**Vì sao đáng lưu ý ngoài phạm vi UI:** đặc tả `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570` quy định tệp
Excel xuất **"theo bộ lọc hiện tại"**. Nếu bộ lọc thực tế lệch với bộ lọc người dùng nhìn thấy, thì tệp xuất ra
cũng lệch theo — người dùng có thể nhận một tệp không đúng tập dữ liệu mình nghĩ đang lọc.

**Ảnh hưởng tới dòng 14: KHÔNG.** Đã bấm **"Xóa bộ lọc"**, xác nhận mọi ô về rỗng và danh sách về 7, rồi mới
gõ lại từ khoá và đo lại. Mọi số đo dùng để chấm đều lấy từ lần đo sạch (chuỗi truy vấn **chỉ có `keyword`**).
Chi tiết: [`do/QLKTLBG_20.md`](../do/QLKTLBG_20.md) §4.

**Chưa đo (để lead quyết có mở rộng không):** hiện tượng này chỉ mới quan sát trên ô "Công khai" của màn Kho
tài liệu / Bài giảng, trong tình huống chuyển màn bằng menu. **Chưa** kiểm các ô lọc khác, các màn danh sách
khác, hay đường vào màn khác (bấm dải điều hướng, tải lại trang, mở từ liên kết). Không tự mở rộng phạm vi
theo BRIEF §4.1.

## 2. Câu chữ lựa chọn ô lọc "Công khai" lệch đặc tả (nhắc lại, đã ghi ở case 18)

Màn có 2 lựa chọn **"Công khai" / "Không công khai"**; `srs-fr-03-dao-tao.md:1958` ghi
**"Tất cả / Đã công khai / Chưa công khai"**, và badge trên bảng (`:1971`) dùng đúng "Đã công khai" /
"Chưa công khai". Ghi lại để không rơi rụng giữa các case.

## 3. Bảng tổng quan quy tắc thiếu FR-III-07 / FR-III-08 (điểm chỉnh TÀI LIỆU, không phải lỗi phần mềm)

`srs-fr-03-dao-tao.md:2243` liệt kê BR-DATA-06 cho `FR-III-01, FR-III-05, FR-III-06, FR-III-14` — **thiếu
FR-III-07 / FR-III-08**, trong khi đặc tả cấp màn `:1952` quy định rõ màn này có nút "Xuất Excel" và dẫn thẳng
BR-DATA-06. Đề nghị bổ sung cho khớp để vòng nghiệm thu sau không phải tra chéo.

## 4. Đề nghị BA về hành vi khi bộ lọc ra 0 kết quả (đã ghi trong ô sheet dòng 14)

Nội dung đầy đủ ở [`do/QLKTLBG_20.md`](../do/QLKTLBG_20.md) §15 và ở cuối
[`note/QLKTLBG_20-ketqua-verify.txt`](QLKTLBG_20-ketqua-verify.txt).
Tóm tắt: đặc tả Nhóm III **im lặng** về hành vi khi tập kết quả rỗng, trong khi 2 phân hệ khác đã chốt và chốt
**khác nhau**. Hệ thống hiện tạo tệp rỗng + báo "Xuất dữ liệu thành công.". **Không chặn bàn giao, không ảnh
hưởng verdict Pass của dòng 14.**
