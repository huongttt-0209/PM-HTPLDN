# QLHSVV_OOS_01 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 133 · Verdict Verify 2: `Pass`
> **Bug gốc:** cột **"Loại"** của bảng "Tài liệu đính kèm" trong Chi tiết vụ việc in ra **mã nội bộ viết hoa có gạch
> dưới `BO_SUNG`** thay vì chữ tiếng Việt. **Kết quả mong đợi:** cột "Loại" hiển thị **chữ tiếng Việt dễ hiểu**
> (ví dụ "Bổ sung"), thống nhất với các cột khác trong cùng bảng và với cách gọi ở khối "Dòng thời gian".
> **Loại bug:** chữ hiển thị **phụ thuộc giá trị loại tài liệu của từng bản ghi** (mỗi loại là một giá trị khác nhau,
> có giá trị được dịch có giá trị không) ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện `index-DpIXRGaI.js`
(phần bảng tài liệu nằm ở gói con `index-BnFEJahL.js`).

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương (`CB_NV_TW`), đơn vị BTP · TW | **`cbnv_tw`** — `CB_NV_TW`, cấp TW, thanh trên hiện `BTP · TW` ⇒ **trùng đúng** vai trò + cấp + đơn vị. (Cột "Loại" là nhãn chung của bảng, không đổi theo người dùng — vẫn giữ đúng vai trò của phiếu để không tạo lệch) | Không |
| Màn hình + trạng thái entity | Chi tiết vụ việc → nhóm "Tài liệu đính kèm" đã bung; vụ việc `VV-BTP-TW-20260803-002` trạng thái "Đã tiếp nhận" | Đúng màn đó. Đo trên **3 vụ việc**: (1) **chính `VV-BTP-TW-20260803-002`** của phiếu — nay ở trạng thái "Đã duyệt" và mang 4 tệp khác (dữ liệu môi trường đã được dựng lại giữa 2 vòng, mã vụ việc giữ nguyên nhưng nội dung khác); (2) `VV-BTP-TW-20260804-003` (Đã tiếp nhận); (3) `VV-BTP-TW-20260804-005` (Đã tiếp nhận). **Không GAP** vì thứ quyết định chữ hiển thị là **giá trị loại tài liệu của hàng tệp**, và giá trị `BO_SUNG` của bug gốc đã được tái lập đủ ở cả 3 vụ việc | Không |
| Dữ liệu tiền đề — **loại tài liệu** (chính là biến gây lỗi) | 1 tệp ảnh JPG **loại `BO_SUNG`** | Phủ **toàn bộ giá trị loại tài liệu mà phần mềm thực sự sinh ra**: quét **13 tệp trên 6 vụ việc** mà tài khoản này đọc được, máy chủ chỉ trả **2 giá trị**: **`BO_SUNG` (9 tệp)** và **`YEU_CAU` (4 tệp)**. Cả 2 giá trị đều được đo. Phủ thêm 4 định dạng tệp (JPG/PDF/DOCX/XLSX) để loại khả năng nhãn phụ thuộc định dạng | Không |
| Thao tác đo | Bung nhóm "Tài liệu đính kèm" → đọc ô cột "Loại" | Đúng thao tác đó, đo **3 cách độc lập**: (1) đọc `innerText` từng ô cột "Loại" của từng hàng (không dùng `textContent`); (2) đọc ảnh chụp bằng mắt; (3) quét **toàn bộ chữ trên màn** bằng biểu thức bắt mã viết hoa có gạch dưới để xem còn sót mã máy ở bất kỳ chỗ nào không | Không |
| Đối chứng để chứng minh phép đo còn "bắt" được lỗi | — | Trên **chính hàng đó**, máy chủ trả `loaiTaiLieu = "BO_SUNG"` nhưng màn hình in "Bổ sung" ⇒ phép đo đang đọc **chữ hiển thị**, không phải dữ liệu thô; nếu chưa sửa thì phép đo này vẫn phải bắt được `BO_SUNG` | Không |

## Kết quả đo

- **`BO_SUNG` → "Bổ sung"**: đúng trên **9/9** tệp, gồm 4 tệp của chính vụ việc `VV-BTP-TW-20260803-002` mà phiếu nêu
  (ảnh `…-v2-02`), 4 tệp của `VV-BTP-TW-20260804-003` và 1 tệp cũ ngày 30/06.
- **`YEU_CAU` → "Yêu cầu"**: đúng trên **4/4** tệp (ảnh `…-v2-01` — cùng một bảng có cả "Bổ sung" lẫn "Yêu cầu",
  không giá trị nào lộ mã máy).
- **Quét toàn màn Chi tiết vụ việc**: không còn chuỗi nào dạng mã máy viết hoa có gạch dưới (chỉ khớp đúng tên tệp
  kiểm thử do tôi tự đặt như `QLHSVV_07-v2-…`).
- **Khối "Dòng thời gian"** ngay dưới bảng gọi sự kiện là **"Bổ sung hồ sơ"** ⇒ đã thống nhất cách diễn đạt như
  "Kết quả mong đợi" của phiếu yêu cầu.
- Các cột đối chứng cùng hàng vẫn đúng: "Trạng thái quét" hiện "Sạch" (dữ liệu thô là `SACH`), "Định dạng" hiện
  JPG/PDF/DOCX/XLSX.

## Đã cố BÁC BỎ kết luận `Pass` bằng những cách nào

1. **Nghi "chỉ dịch mỗi giá trị `BO_SUNG` mà đối tác chụp được, giá trị khác vẫn lộ mã"** → **BÁC**: liệt kê **mọi**
   giá trị loại tài liệu mà máy chủ thực sự trả về trên toàn bộ dữ liệu tài khoản này đọc được (13 tệp / 6 vụ việc) —
   chỉ có `BO_SUNG` và `YEU_CAU`, và **cả hai** đều ra tiếng Việt.
2. **Nghi "nhãn chỉ đúng với ảnh JPG như bản ghi đối tác"** → **BÁC**: phủ thêm PDF, DOCX, XLSX; nhãn không phụ thuộc
   định dạng.
3. **Nghi "bản ghi cũ đã sửa nhãn, bản ghi mới lại lộ mã"** → **BÁC**: tự tạo **2 hồ sơ mới hôm nay** qua luồng chuẩn
   (`…-003`, `…-005`), cả hai đều hiện tiếng Việt.
4. **Nghi "chỗ khác trong màn vẫn in mã máy, chỉ sửa mỗi 1 ô"** → **BÁC**: quét toàn bộ chữ hiển thị của màn Chi tiết
   vụ việc bằng biểu thức bắt mã viết hoa có gạch dưới — không còn mã máy nào.
5. **Nghi "màn Kiểm tra hồ sơ (bung từ chính màn này) vẫn in mã máy"** → **BÁC**: mở màn đó, 6 hạng mục checklist đều
   là tiếng Việt, không có mã máy.
6. **Nghi "phép đo đọc nhầm dữ liệu thô nên tưởng đã dịch"** → **BÁC**: cùng phép đo đó đọc được "Sạch" trong khi dữ
   liệu thô là `SACH` ⇒ đang đọc đúng lớp hiển thị; ngoài ra ảnh chụp đọc bằng mắt cho kết quả trùng khớp.
7. **Nghi "tab mở lâu còn chạy mã cũ"** → **BÁC**: trong phiên đo có nhiều lần chuyển màn và một lần đăng nhập lại
   (tải lại toàn bộ trang); kết quả không đổi.
8. **Đào sâu vào chỗ dễ vỡ nhất — cách phần mềm dịch nhãn**: bảng dịch của giao diện chỉ có **3 mục**
   ("Yêu cầu", "Bổ sung", "Khác") và **nếu gặp giá trị lạ thì in nguyên mã máy ra màn hình**. Tôi đã tìm cách ép phần
   mềm sinh ra một giá trị thứ tư để bắt lỗi này, nhưng **không đường nào làm được**: cả 2 chỗ đưa tệp vào hồ sơ đều
   **không cho người dùng chọn loại tài liệu** (hệ thống tự gán), nên với phần mềm hiện tại **không tồn tại giá trị
   nào lọt ra ngoài bảng dịch**. ⇒ không bác được kết luận `Pass` cho phiếu này. (Việc bảng loại tài liệu hiện chỉ có
   2 giá trị chung chung, **khác với 6 loại giấy tờ mà đặc tả quy định**, là một vấn đề **riêng**, đã mở dòng phiếu
   mới — không thuộc phạm vi phiếu này vì phiếu này chỉ hỏi "chữ hiển thị có phải tiếng Việt không".)

**Kết luận: 0 GAP** — đúng vai trò/đơn vị, đúng màn hình, đúng thao tác; phủ **toàn bộ** giá trị loại tài liệu mà phần
mềm thực sự sinh ra, trên cả bản ghi cũ của phiếu lẫn bản ghi mới tạo hôm nay.
