# Reverify QLHDTVVCG_03 - dòng 309

- Ngày chạy: 08/08/2026
- Môi trường: `https://18.143.165.120.nip.io`
- Giao diện: `HTPLDN · V1.0.10`
- Công cụ: Chrome DevTools trên cửa sổ Chrome hiển thị; không dùng Playwright, không gọi API trực tiếp, không seed dữ liệu
- Tài khoản: **CB Nghiệp vụ - Trung ương #03**, đăng nhập và xác thực OTP hoàn toàn qua UI/MailHog UI
- Căn cứ BA/DEV 06/08: **Loại 4, hướng A**; menu Hợp đồng riêng đã chủ động bỏ, route hợp lệ là **Chi tiết Vụ việc/Lịch sử TVV**. Không chấm thiếu menu riêng là lỗi.
- Verdict: **PASS / Test done**

## Luồng UI và baseline

1. Đăng nhập `cbnv_tw_03` qua UI, lấy OTP trên giao diện MailHog và xác thực thành công; header hiển thị `CB Nghiệp vụ - Trung ương #03`, `BTP · TW`.
2. Bấm menu **Vụ việc HTPL**, dùng ô tìm kiếm của danh sách để mở đúng `VV-BTP-TW-20260804-002`.
3. Tại Chi tiết vụ việc, mở accordion **HĐ tư vấn liên kết**.
4. Trước khi lọc, bảng có 4 hợp đồng; đã ghi lại mã, tên đầy đủ và Bên B để bảo đảm từ khóa thực sự tồn tại:

| Mã hợp đồng | Tên hợp đồng | Bên B |
|---|---|---|
| `HDTV-20260808-0001` | `Hợp đồng QA row321 tạo mới đầy đủ QA-R321-20260808-0012` | `Doanh nghiệp QA-R321-20260808-0012` |
| `HDTV-20260807-0008` | `Hop dong QA-G4-B1 kiem tra bo loc khoang ngay 20260807` | `QA TVV Seed28 Active` |
| `HDTV-20260807-0007` | `Hợp đồng tư vấn pháp luật lao động và bảo hiểm xã hội cho doanh nghiệp siêu nhỏ` | `QA TVV PheDuyet TW R19` |
| `HDTV-20260807-0006` | `Hợp đồng tư vấn xác lập quyền sở hữu trí tuệ và nhãn hiệu cho doanh nghiệp nhỏ và vừa` | `Chuyên gia UAT QLNDTVVCG 38` |

## Kết quả bốn phép tìm kiếm bắt buộc

Mỗi lượt đều nhập trên UI, bấm **Tìm kiếm**, ghi lại danh sách trả về, sau đó bấm **Xóa bộ lọc** và xác nhận bảng phục hồi `1-4 / 4 mục` trước lượt kế tiếp.

| # | Từ khóa/nguồn trường | Kết quả UI | Đối chiếu nonmatch | Network do UI tạo | Kết quả |
|---:|---|---|---|---|---|
| 1 | Cụm có dấu chính xác `sở hữu trí tuệ`, lấy từ Tên HĐ `...-0006` | Còn đúng `HDTV-20260807-0006`, `1-1 / 1 mục`; tên hiển thị vẫn chứa nguyên cụm có dấu | Loại đúng `...-0001`, `...-0008`, `...-0007` | req 594, `search=s%E1%BB%9F+h%E1%BB%AFu+tr%C3%AD+tu%E1%BB%87`, HTTP 200 | PASS |
| 2 | Từ có dấu `bảo`, lấy từ Tên HĐ `...-0007` và là từ khóa duy nhất trong baseline | Còn đúng `HDTV-20260807-0007`, `1-1 / 1 mục`; tên chứa `bảo hiểm` | Loại đúng `...-0001`, `...-0008`, `...-0006` | req 597, `search=b%E1%BA%A3o`, HTTP 200 | PASS |
| 3 | Từ có dấu `Chuyên`, lấy từ Bên B `Chuyên gia UAT QLNDTVVCG 38` | Còn đúng `HDTV-20260807-0006`, `1-1 / 1 mục`; Bên B chứa `Chuyên` | Loại đúng ba dòng còn lại | req 598, `search=Chuy%C3%AAn`, HTTP 200 | PASS |
| 4 | Mã đầy đủ `HDTV-20260807-0006` | Còn chính xác một dòng `HDTV-20260807-0006`, `1-1 / 1 mục` | Không trả `...-0001`, `...-0008`, `...-0007` | req 601, nguyên mã trong query, HTTP 200 | PASS |

Sau lượt cuối, **Xóa bộ lọc** phục hồi đủ bốn mã ban đầu. Không có dữ liệu nào bị thay đổi vì toàn bộ thao tác chỉ là đọc/tìm kiếm.

## Console, network và ảnh quan sát

- Bốn request tìm kiếm do nút UI tạo đều HTTP 200; ba từ khóa tiếng Việt được URL-encode đúng, không mất dấu hoặc biến dạng.
- Request baseline không có `search` trả đủ 4 hợp đồng; các lượt reset phục hồi đúng baseline, một số lượt dùng cache HTTP 304 nhưng UI vẫn hiển thị đủ 4 dòng.
- Console sau toàn bộ chuỗi thao tác: không có `error` hoặc `warning`.
- Chrome DevTools đã chụp trạng thái baseline và kết quả từng từ khóa: bảng 4 dòng; `sở hữu trí tuệ` 1 dòng; `bảo` 1 dòng; `Chuyên` 1 dòng; mã đầy đủ 1 dòng.

## Kết luận để cập nhật Sheet

`Trạng thái dev fix = Test done`.

`Kết quả verify`: **PASS - Tại Chi tiết Vụ việc > HĐ tư vấn liên kết, tìm kiếm tiếng Việt có dấu hoạt động đúng trên Tên HĐ và Bên B: cụm “sở hữu trí tuệ”, từ “bảo” và “Chuyên” đều trả đúng dòng chứa từ khóa, loại các dòng không khớp; tìm theo mã hợp đồng đầy đủ vẫn trả đúng một bản ghi.**
