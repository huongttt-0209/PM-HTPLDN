# Re-verify bug Dev đã fix — Round 6, ngày 25/07/2026

Tab sheet: `UAT_TGPL Doanh Nghiệp-tuần 3` · Môi trường `https://18.143.165.120.nip.io`
Công cụ: Chrome DevTools MCP (thao tác trên giao diện thật, không kết luận bằng curl).

## Kết quả 9 dòng

| Dòng | Mã TC | Kết luận | Vì sao |
|---|---|---|---|
| 296 | QLTLPLCVV_07 | **Pass** | Sửa tư liệu Nháp còn tệp: lưu được, không còn báo "file đã gắn vào bản ghi khác" |
| 308 | QLTLPLCVV_OOS_01 | **Pass** | Gỡ tệp trong form Sửa: mở lại tệp đã mất đúng như mong đợi |
| 286 | QLNDTVVCG_22 | **Pass** | Ô "Chuyên môn" lấy đúng theo thứ tự ưu tiên; trống cả hai thì hiện "Chưa cập nhật" |
| 290 | QLNDTVVCG_40 | **Reopen** → Pass ở vòng 7 | Giờ-phút trong TÊN TỆP Excel không phải giờ Việt Nam (cột "Ngày tạo" đã đúng) |
| 289 | QLNDTVVCG_36 | **Pass** | Hủy TVCS ở Đang tư vấn: không còn phần dư của luồng duyệt-hủy |
| 307 | QLDNDHTPL_OOS_01 | **Pass** | DN đơn vị khác đã ẩn nút Sửa/Xóa; lưu vượt quyền chỉ còn 1 thông báo (xem `QLDNDHTPL_OOS_01-do-toast.md`) |
| 11 | CNKQHT_03 | **Pass** | TVV đính tệp không còn "Forbidden"; CB nghiệp vụ đính tệp, mở lại vẫn còn; bấm Xem mở đúng nội dung PDF |
| 70 | THDG_03 | **Reopen** → Pass ở vòng 7 | Điểm âm đã báo lỗi tại ô, nhưng khi bấm Lưu thì thông báo hiện bằng tiếng Anh thô |
| 293 | QLHSPLDN_03 | **Reopen** → Pass ở vòng 7 | Tệp đã hiện lại khi mở bằng [Sửa], nhưng bấm [Xem] bị đá sang trang 403 (ERR-PERM-FILE-03) |

> Cả 3 dòng Reopen trên đã được kiểm lại và đạt ở vòng 7 cùng ngày — xem [README-vong-7.md](README-vong-7.md).

## Dữ liệu đã dựng để verify (không xoá, phục vụ đối chiếu sau)

- Tư liệu "R6-0725 TL fresh 2 tep de test unlink" (2 tệp) — cho 296 / 308.
- TVCS-20260725-0007 — cho 286 / 289.
- Vụ việc VV-BTP-TW-20260712-004: kết quả hỗ trợ kèm `R6-KQHT-TVV.pdf` (TVV nhập) và `R6-KQHT-CBNV.pdf` (CB nghiệp vụ nhập) — cho 11.
- Đợt đánh giá **DG-20260725-0003** "R6-THDG03-20260725 verify diem am" (trạng thái Thực hiện, 1 vụ việc EEE-VH-014, người chấm cbnv_hn) — cho 70. Điểm âm không lưu được nên đợt vẫn 0/1 đã chấm.
- Hồ sơ pháp lý **HSPL-20260725-0003** trên DN-HNI-0006, kèm `R6-HSPL-NEW.pdf` — cho 293.

## Một lần suýt kết luận sai — đã tự bắt lại

Lần tạo hồ sơ pháp lý đầu tiên, ô "Mô tả" mở lại bị trống nên trông như thêm một lỗi mới.
Kiểm tra request `POST /api/v1/ho-so-phap-ly-dns` thì thân request **không hề có trường mô tả** —
tức chữ chưa vào được biểu mẫu do cách nhập của công cụ kiểm thử, không phải lỗi phần mềm.
Nhập lại đúng cách rồi lưu thì mô tả hiển thị lại bình thường. Không ghi lỗi này vào sheet.

Tương tự, ở dòng 286 vòng trước, ô "Chuyên môn" đọc sai do danh sách chọn còn nhớ dữ liệu cũ;
tải lại trang bỏ qua bộ nhớ đệm mới ra kết quả đúng.

## Ghi chú về ảnh chụp thông báo tự tắt

Thông báo dạng nổi của giao diện chỉ sống ~3 giây, trong khi lệnh chụp màn hình qua công cụ
mất từ 2,5 giây trở lên nên hay chụp trượt. Với các trường hợp đó, bằng chứng dùng bản đo
đọc trực tiếp phần tử thông báo trong trang (ghi trong file `*-do-toast.md`), đo lặp ≥2 lần.
