# Nội dung CŨ của ô 'Kết quả verify' — dòng 127 · LKHDG_16

Chụp lại lúc bắt đầu lô F3-devfix-2026-08-07, TRƯỚC khi đè (prompt mục 6 cho phép đè `--cho-phep-de-ketqua`).

- Trạng thái dev fix (lúc chụp): `Fixed`
- Dopai (lúc chụp): `dev done`
- DEV phản hồi lần 1 (lúc chụp): (trống)

---

## Nguyên văn ô 'Kết quả verify'

```text
🔁 Còn lỗi — chuyển lại dev.

- Ba vế đối tác nêu ĐÃ HẾT LỖI ở trạng thái "Lập kế hoạch": bấm Sửa mở khung nhập đủ 9 mục, tất cả nhập/đổi được và nạp sẵn giá trị cũ; đổi rồi lưu thì mở lại thấy giá trị mới (bản ghi lên version 3); không còn rơi vào màn "Chi tiết" — đường dẫn giữ nguyên ".../ Danh sách", khung nhập ghi rõ "Sửa kế hoạch đánh giá"; danh sách tệp đính kèm hiện đủ kèm [Xem][Xóa], lưu form không làm mất tệp đã có.
- Nhưng ở trạng thái "Phân công" thì KHÔNG vào được chế độ sửa: hàng trong danh sách chỉ còn thao tác xem, màn chi tiết không có ô nhập nào cho khối Thông tin kế hoạch (chỉ có [Hủy đợt]), gọi thẳng API cập nhật trả 409 ERR-BIZ-XI-01-02 "Không thể cập nhật kế hoạch ở trạng thái 'PHAN_CONG'". Giao diện và máy chủ thống nhất nhau nên đây là luật đang cài đặt, không phải nút bị ẩn nhầm.
- Đặc tả đòi: srs-fr-08-danh-gia.md:837 — "Xem / Sửa (chỉ LAP_KE_HOACH/PHAN_CONG) / Xóa (chỉ LAP_KE_HOACH)"; và :159 — "CB NV chỉnh sửa KH chưa duyệt ... validate + lưu" (đợt Phân công vẫn là chưa duyệt, việc duyệt diễn ra ở bước Chờ duyệt PC → Thực hiện, :1188). Đặc tả không có dòng nào giới hạn sửa vào riêng Lập kế hoạch. Chính cột "Kết quả mong đợi" của phiếu này cũng ghi "Chỉ hiển thị khi đợt đang ở trạng thái 'Lập kế hoạch' hoặc 'Phân công'".
- Hệ quả: luồng trạng thái không có đường lùi Phân công → Lập kế hoạch (:1185-1194), nên sai sót trong thông tin kế hoạch sau khi đã phân công không sửa được nữa, chỉ còn cách hủy cả đợt.
- Đã test bằng: tài khoản cbnv_tw (CB Nghiệp vụ Trung ương, BTP·TW), 3 dạng dữ liệu — đợt Lập kế hoạch 1 tệp, đợt Lập kế hoạch 2 tệp khác định dạng, đợt Phân công 1 tệp. Bản dựng HTPLDN V1.0.8 (env kiểm thử nội bộ) — chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu.
- Chủ việc tiếp theo: Dev BE gỡ chặn cập nhật ở trạng thái PHAN_CONG, sau đó Dev FE hiện lại thao tác Sửa. Nếu luật thật sự là "chỉ sửa được ở Lập kế hoạch" thì BA cần chốt và sửa :837.
- Một điểm riêng đã tách sang phiếu hỏi BA (không ảnh hưởng verdict này): form Sửa đang hiển thị "Tài liệu đính kèm" và "Cơ quan được đánh giá", trong khi bảng thành phần form ở :843-851 là danh sách đóng 7 dòng không có 2 mục đó. Hiện trạng đang thoả kỳ vọng đối tác nên KHÔNG đề nghị dev gỡ.

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản `cbnv_tw` (CB Nghiệp vụ Trung ương, Test@1234) + màn
  https://18.143.165.120.nip.io/danh-gia/ke-hoach/danh-sach.
  Cần MỘT đợt ở trạng thái "Phân công" thuộc đơn vị của tài khoản và có >=1 tệp đính kèm.
  Chưa có thì tự dựng (tiền đề TẠO ĐƯỢC, không phải blocker):
    a) mở đợt "Lập kế hoạch" -> tab Tiêu chí -> [Nhập từ danh mục] -> chọn nhóm "Hiệu quả HTPL"
       (4 tiêu chí, tổng trọng số 100%) -> sửa cột "Điểm tối đa" = 100 từng dòng -> [Lưu];
    b) tab Phân công -> [Thêm người đánh giá] -> chọn 1 người + vai trò -> [Thêm mới].
  Bỏ bước (a) thì bước (b) bị chặn bởi guard "tổng điểm tối đa có trọng số phải = 100".
1) Ở màn Danh sách, đợt đang "Lập kế hoạch": ghi lại cột Hành động có mấy thao tác.
2) Đợt đang "Phân công": ghi lại cột Hành động có mấy thao tác. So với bước 1.
3) Mở [Sửa] của đợt "Phân công" (nếu có): đổi 1 trường rồi lưu, sau đó MỞ LẠI đối chiếu.
4) Đối chứng đường thứ hai: PATCH /api/v1/ke-hoach-danh-gias/{id} đổi trường Ghi chú,
   ghi lại mã HTTP + error.code.
✅ PASS khi: đợt "Phân công" vào được chế độ sửa, đổi rồi lưu thì mở lại thấy giá trị mới,
   VÀ yêu cầu ở bước 4 không bị từ chối vì lý do trạng thái.
❌ FAIL nếu: đợt "Phân công" không có lối vào sửa, hoặc lưu xong mở lại vẫn giá trị cũ,
   hoặc bước 4 trả 409 kèm thông điệp từ chối theo trạng thái.
⚠️ Đừng chấm Fail vì CHUỖI breadcrumb khác một mẫu cụ thể — đặc tả im lặng về breadcrumb màn Sửa;
   chỉ chấm "có rời khỏi ngữ cảnh Sửa hay không".
⚠️ Đừng kết luận "đã fix" khi chỉ thấy nút [Sửa] xuất hiện lại — phải bấm vào, đổi, lưu, rồi MỞ LẠI
   đối chiếu; và phải đo trên CẢ HAI trạng thái Lập kế hoạch và Phân công.
⚠️ Cảnh báo dụng cụ đo: bản dựng V1.0.8 dùng lớp CSS riêng (.ant-drawer-section, .ant-select-content,
   danh sách tệp KHÔNG dùng .ant-upload-list-item). Kịch bản đọc DOM theo tên lớp chuẩn sẽ báo
   "trống"/"0 tệp" ở chỗ THỰC TẾ CÓ dữ liệu -> luôn chốt bằng ảnh chụp đã mở xem + đọc lại bản ghi.
Ảnh lỗi cũ: image/LKHDG_16-D-hang-PhanCong-chi-con-nut-Xem-V108.png
```
