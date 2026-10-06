# Re-verify 8 bug Dev đã fix — trên MÔI TRƯỜNG NGHIỆM THU của đối tác

- Môi trường: **https://htpldn-uat.ospgroup.vn** — bản dựng **HTPLDN · V1.0.11** (đọc ở thanh bên, trùng bản dựng env nội bộ đã đo 10/08)
- Thời điểm: **2026-08-11**, khoảng 09:30 – 10:35
- Sheet: tab `bug`, cột `Trạng thái dev fix` → **UAT done** cho cả 8 dòng (không đụng cột khác trừ 309/321 đã ghi đè `Kết quả verify` từ lượt trước)
- Cách làm: bỏ kết quả lượt cũ, verify lại từ đầu theo đúng tiêu chí trong cột `Kết quả verify`; dòng không có tiêu chí (36 · 238 · 239) thì verify đúng theo nội dung lỗi ghi trong ô đó.
- Công cụ: Chrome DevTools MCP (không dùng công cụ dòng lệnh để kết luận). Các phép đọc dữ liệu đều gọi trong chính phiên trình duyệt đang đăng nhập.

## Tài khoản đã dùng — ghi rõ từng dòng

| Dòng | Mã TC | Tài khoản thực dùng | Cấp | Ghi chú |
|---|---|---|---|---|
| 32 | QLTVV_02 | `cbnv_tw` | TW | Chính tiêu chí chỉ định `cbnv_tw` |
| 35 | DKTGMLTVV_13 | `nht_01` = **NHT-STP-AG-0001, Sở Tư pháp An Giang** | **Địa phương** | Tiêu chí ghi `nht_ag_uat2`; tên đó không dùng được trên env nghiệm thu, nhưng chính bản ghi NHT An Giang đó tồn tại và tài khoản gắn với nó là `nht_01` |
| 36 | CNHSNLTVV_03 | `nht_01` (An Giang) | **Địa phương** | Đo trên hồ sơ `TVV-STP-AG-0003` do chính tài khoản này tạo |
| 149 | QLDMTCTV_12 | `cbnv_dp` (Sở Tư pháp Hà Nội) cho việc (a)–(e) trên `TC-STP-HN-0001`; `cbnv_tw` cho việc (f) trên `TVV-BTP-TW-0004` | Địa phương + TW | Việc (f) đòi hồ sơ TVV **cùng đơn vị** với người đo; pool TVV của Hà Nội rỗng nên phải dùng đơn vị BTP·TW |
| 238 | CPHTCT_06 | `cbnv_tw` | TW | Phạm vi Sở Tư pháp Hà Nội không có dữ liệu chi trả → không dựng được báo cáo |
| 239 | CPHTCT_07 | `cbnv_tw` | TW | như trên |
| 309 | QLHDTVVCG_03 | `cbnv_dp` (Hà Nội) | **Địa phương** | Đã ghi `UAT done` đầu lượt |
| 321 | QLHDTVVCG_15 | `cbnv_dp` (Hà Nội) | **Địa phương** | Đã ghi `UAT done` đầu lượt |

> Việc dùng tài khoản Trung ương ở các dòng 32 · 149(f) · 238 · 239 là theo phương án đã được đồng ý: tài khoản địa phương không tới được bản ghi/dữ liệu cần đo.

## Kết quả

| Dòng | Mã TC | Kết | Mấu chốt đo được |
|---|---|---|---|
| 32 | QLTVV_02 | ✅ | 11 bản ghi tab "Đang hoạt động" giảm dần theo ngày cập nhật (0 vi phạm); sửa hồ sơ cuối trang → nhảy lên dòng 1; mặc định 20/trang |
| 35 | DKTGMLTVV_13 | ✅ | Thông báo "Đăng ký thành công, chờ thẩm định. **Mã hồ sơ: TVV-STP-AG-0003**"; mã trùng khớp mã thật ở tab "Mới đăng ký" |
| 36 | CNHSNLTVV_03 | ✅ | Tab Năng lực hiện "cấp 15/06/2020" và "cấp 02/04/2024" — đúng ngày đã nhập, không còn "invalid Date" |
| 149 | QLDMTCTV_12 | ✅ | 5.000 lưu đủ; 8.000 không bị cắt; bộ đếm {n}/5000 + câu báo đỏ khi vượt; 5.001 và 9 ký tự đều không lưu được; máy chủ trả mã lỗi riêng; **cả hai màn** Tổ chức tư vấn và Tư vấn viên cùng hành vi |
| 238 | CPHTCT_06 | ✅ | Nội dung tệp Excel = đúng 5 mục của màn hình, **không** có mục theo quy mô doanh nghiệp |
| 239 | CPHTCT_07 | ✅ | Nội dung tệp PDF = đúng 5 mục của màn hình, **không** có mục theo quy mô doanh nghiệp |
| 309 | QLHDTVVCG_03 | ✅ | Tìm kiếm có dấu ra đúng bản ghi (xem file riêng của dòng 309) |
| 321 | QLHDTVVCG_15 | ✅ | Một câu "Đã lưu hợp đồng" dùng chung; mã `HDTV-20260811-0001`, trạng thái "Đang thực hiện" |

## Chi tiết từng dòng

- [QLTVV_02-r32-thu-tu-mac-dinh.md](QLTVV_02-r32-thu-tu-mac-dinh.md)
- [DKTGMLTVV_13-r35-thong-bao-kem-ma-ho-so.md](DKTGMLTVV_13-r35-thong-bao-kem-ma-ho-so.md)
- [CNHSNLTVV_03-r36-ngay-cap-tab-nang-luc.md](CNHSNLTVV_03-r36-ngay-cap-tab-nang-luc.md)
- [QLDMTCTV_12-r149-moc-5000-ky-tu.md](QLDMTCTV_12-r149-moc-5000-ky-tu.md)
- [CPHTCT_06-07-r238-239-noi-dung-file-xuat.md](CPHTCT_06-07-r238-239-noi-dung-file-xuat.md)

## Dữ liệu đã dựng / đã thay đổi trong lượt này

| Bản ghi | Thay đổi | Đã hoàn nguyên? |
|---|---|---|
| `TVV-BTP-TW-0004` (Trương Văn Mười Sáu) | sửa ô Ghi chú (bước 3 của tiêu chí dòng 32); trạng thái Đang hoạt động → Tạm dừng → Đang hoạt động | ✅ trạng thái đã về "Đang hoạt động"; ô Ghi chú giữ dòng ghi của QA |
| `TC-BTP-TW-0008` | mở cửa sổ Cập nhật trạng thái để so hành vi, bấm Hủy | ✅ vẫn Đang hoạt động, không lưu gì |
| `TC-STP-HN-0001` | đo mốc 5.000 ký tự (đầu lượt) | ✅ đã về Đang hoạt động |
| `TVV-STP-AG-0003` | **hồ sơ mới dựng** để đo dòng 35 + 36 | ✖ giữ lại làm bằng chứng (trạng thái "Mới đăng ký") |
| Tài khoản `nht_01` | đặt lại mật khẩu về `Test@1234` qua luồng Quên mật khẩu; bổ sung số CCCD `089185000835` do phần mềm bắt buộc khi đăng nhập | ✖ giữ nguyên — đã ghi vào `input/input.md` để lượt sau khỏi dò |

## Ghi nhận thêm (không đổi kết quả dòng nào)

1. **Đường dẫn tổ chức tư vấn trên trang chi tiết Tư vấn viên trả về trang 404.** Ở trang chi tiết TVV, ô "Tổ chức chính" là một liên kết trỏ tới `/to-chuc/{id}`, bấm vào ra trang "404 — Trang bạn tìm kiếm không tồn tại hoặc đã được di chuyển". Đường đúng của phần mềm là `/chuyen-gia-tvv/to-chuc/{id}`. Không thuộc bất kỳ tiêu chí nào trong 8 dòng nên chỉ ghi nhận, chưa lập phiếu.
2. **Bộ đếm ký tự giữ màu xám khi vượt mốc**, phần cảnh báo là dòng chữ đỏ "Lý do thay đổi tối đa 5.000 ký tự" ngay dưới ô. Cùng hành vi ở cả hai màn. Người dùng vẫn được cảnh báo đúng lúc vượt mốc nên chấm đạt việc (c); ghi lại để đơn vị chủ quản biết chữ trong tiêu chí là "bộ đếm chuyển sang trạng thái cảnh báo".
3. **Hai màn chặn lưu theo hai cách khác nhau:** màn Tổ chức tư vấn làm mờ nút [Đồng ý]; màn Tư vấn viên để nút [Xác nhận] sáng nhưng bấm không gửi gì lên máy chủ. Cả hai đều thoả "không lưu được + có câu báo tại ô".
4. **Pool Tổ chức tư vấn của Sở Tư pháp An Giang rỗng** ("Chưa có Tổ chức tư vấn ở trạng thái Đang hoạt động") nên ô "Tổ chức hành nghề chính" — không bắt buộc — để trống ở dòng 35.
5. **Cảnh báo về cách đo, không phải lỗi phần mềm:** ở vài phép đo giữa lượt, bộ theo dõi thông báo và bộ đếm request của tôi bị cài chồng nhiều lớp qua các lần gọi, làm một thao tác bị ghi thành 2–3 lượt. Đã tải lại trang, cài đúng một lớp, và đếm lại bằng công cụ mạng gốc: **1 lần bấm Lưu = đúng 1 request**, ảnh chụp cũng chỉ có 1 thông báo trên màn. Không có chuyện gửi trùng hay hiện thông báo đôi.
