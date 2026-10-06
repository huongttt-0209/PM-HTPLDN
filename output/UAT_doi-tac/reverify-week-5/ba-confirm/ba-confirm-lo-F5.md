# Câu hỏi cần BA chốt — lô F5 (07/08/2026)

Nguồn đối chiếu: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`. Mọi số dòng dưới đây đã tự mở file xác minh trong lượt này.

---

## NHÓM A — chặn verdict (2 câu)

### Q1 · QLDKTK_10 (dòng 169) — Doanh nghiệp đặt mật khẩu ở đâu?

- **Đối tác kỳ vọng:** bước 2 của phiếu = "Doanh nghiệp đặt mật khẩu thành công" **sau khi bấm liên kết kích hoạt** trong thư.
- **SRS nói cả hai hướng, trong CÙNG một chức năng FR-VIII-22:**
  - `srs-fr-10-quan-tri.md:1070-1071` — mật khẩu + xác nhận mật khẩu là **trường bắt buộc ở form đăng ký** (SCR-VIII-08).
  - `srs-fr-10-quan-tri.md:1109` · `:1116` · `:2299` — DN "đặt mật khẩu lần đầu" **qua liên kết kích hoạt**.
- **Web/dev hiện tại:** làm theo hướng **form đăng ký**. Màn kích hoạt có 0 ô nhập mật khẩu (đo 2/2 lượt); yêu cầu gửi lên chỉ mang mã kích hoạt. Phép thử 2 mật khẩu khác nhau: đăng nhập được bằng mật khẩu nhập ở form đăng ký; mật khẩu định đặt ở bước kích hoạt trả 401.
- **Kết quả cuối của phiếu thì đã đạt:** tài khoản về `HOAT_DONG` do chính bước kích hoạt (`lanDangNhapCuoi = null`), DN đăng nhập được bằng mã số thuế, mở được hồ sơ của mình.

> **CẦN BA CONFIRM:** đối tác kỳ vọng DN đặt mật khẩu ở màn kích hoạt qua liên kết trong thư; SRS quy định **cả hai hướng loại trừ nhau** — `:1070-1071` (form đăng ký) và `:1109`/`:1116`/`:2299` (màn kích hoạt); web/dev hiện tại làm theo `:1070-1071`.
> **Chốt xong thì:** nếu chọn hướng màn kích hoạt → là lỗi cần dev sửa. Nếu chọn hướng form đăng ký → sửa lại bước 2 của phiếu và đóng dòng này, đồng thời gỡ nhánh còn lại khỏi `:1109`/`:1116`/`:2299` cho khỏi mâu thuẫn.

### Q2 · QLDMTCTV_12 (dòng 149) — Mốc tối đa của "Lý do thay đổi trạng thái" Tổ chức tư vấn?

- **Đối tác kỳ vọng:** bắt buộc, tối thiểu 10 ký tự, **tối đa 5.000 ký tự**.
- **SRS im lặng về mốc tối đa:** `srs-fr-04-chuyen-gia-tvv.md:984` chỉ ghi `| 3 | ly_do | text (long) | Y | Min 10 ký tự |`. `srs-v3.5.md:805` cũng không đặt mốc tối đa mặc định cho kiểu `text (long)`. Trường `ly_do_tu_choi` giới hạn 2.000 ký tự (`:2232`) là **trường khác**, dùng cho luồng từ chối phê duyệt. Nhóm Hỏi đáp có tiền lệ đặt 10–500 ký tự (`srs-fr-02-hoi-dap.md:421`).
- **Web/dev hiện tại:** ô Lý do có `maxlength="1000"`; nhập 5.001 ký tự thì ô **chỉ nhận 1.000 và cắt âm thầm**, không câu nào báo cho người dùng biết đã bị cắt.

> **CẦN BA CONFIRM:** đối tác kỳ vọng tối đa 5.000 ký tự; SRS **không quy định mốc tối đa** (`:984` chỉ có Min 10); web/dev hiện tại chặn cứng ở 1.000 ký tự.
> **Chốt xong thì:** nếu chọn 5.000 → là lỗi cần dev sửa. Nếu chọn 1.000 → sửa mốc trong phiếu và bổ sung số vào `:984`. Trong cả hai trường hợp, đề nghị hiển thị một câu nhắc khi người dùng nhập vượt mốc, thay vì cắt âm thầm.

---

## NHÓM B — housekeeping đặc tả, KHÔNG chặn bàn giao (4 câu)

Cả 4 câu dưới đây **không làm đổi verdict** của lô này — web đang chạy đúng và các dòng liên quan đã ghi `Test done`. Nêu ra để đặc tả khớp bản đang chạy, tránh vòng sau lại tranh chấp.

### Q3 · Mốc hiển thị hộp thoại cảnh báo phiên — 25 hay 30 phút?
`srs-fr-10-quan-tri.md:1891` (SCR-VIII-07 dòng 12 "Session Warning") ghi điều kiện hiển thị là **"30 phut idle"**, trong khi `:1959` ghi **"25 phut idle → Modal canh bao → 30 phut → Auto invalidate"**. Hai số không thể cùng đúng: ở phút 30 phiên đã bị hủy nên không thể hiện hộp thoại "sắp hết hạn trong 5 phút". Web đo được: **đúng 25,0 phút** — khớp `:1959` và khớp phiếu đối tác.
→ Đề nghị sửa `:1891` thành 25 phút. (`CHANGELOG-v3-to-v3.5.md:1212` và `:1240` cho thấy bảng SCR-VIII-07 chỉ được soát lại ở dòng 2 và dòng 11, chưa soát dòng 12.)

### Q4 · Câu chữ hộp thoại cảnh báo + nhãn nút
`:1891` chỉ ghi chuỗi rút gọn **không dấu** `"Phien sap het han trong 5 phut. [Gia han] [Dang xuat]"`. Web hiện tại hiện: tiêu đề `"Phiên làm việc sắp hết hạn"`, nội dung `"Phiên làm việc sắp hết hạn trong 5 phút do không có thao tác. Vui lòng gia hạn để tiếp tục làm việc."`, dòng đếm ngược `"Phiên sẽ tự đăng xuất sau m:ss"`, 2 nút `[Đăng xuất]` `[Gia hạn phiên]` — **trùng từng ký tự** với kỳ vọng đối tác.
→ Đề nghị chép nguyên câu chữ + 2 nhãn nút đang chạy vào `:1891`. Cũng nên bổ sung đồng hồ đếm ngược (SRS hiện không nhắc, grep "đếm ngược/countdown" = 0 hit).

### Q5 · Hành vi khi bấm [Gia hạn phiên] chưa được viết thành câu
`:1891` khai báo nút `[Gia han]` nhưng ô "Hành vi" của chính dòng đó **để trống ("—")**. Đo được: bấm → hộp thoại đóng ≤0,39s, mốc không-thao-tác đặt lại về thời điểm bấm, vượt mốc tự đăng xuất cũ mà `/auth/me` vẫn trả 200. Hành vi này suy ra được từ `BR-AUTH-06` (`srs-v3.5.md:5527` · `srs-fr-10-quan-tri.md:2369` — "Session CMS: 30 phút idle timeout") nhưng chưa được viết rõ.
→ Đề nghị viết vào ô "Hành vi" của `:1891`. Đồng thời chốt: **có giới hạn số lần gia hạn liên tiếp hay không?** (SRS hiện không nói; QA không đo vì ngoài phạm vi phiếu).

### Q6 · Câu thông báo hết phiên tồn tại 4 dạng lệch nhau
`srs-fr-10-quan-tri.md:964` (ERR-DN-07 "Phiên làm việc hết hạn") · `:1011` (Outputs message = "Đăng xuất thành công" / "Phiên hết hạn") · `srs-fr-05-vu-viec.md:1593` · `srs-fr-02-hoi-dap.md:1135` — **không dạng nào** có cụm "do không có thao tác", trong khi web và phiếu đối tác đều dùng cụm đó.
→ Đề nghị chốt một câu chuẩn. Kèm đó, xin xác nhận cách hiểu QA đã dùng để chấm QLDX_06: **bấm [Đăng xuất] ở phút 25 thì phiên chưa hết hạn nên "Đăng xuất thành công" là đúng theo `:1011`**, còn câu hết-phiên chỉ dành cho nhánh để tới phút 30. Nếu nghiệp vụ muốn hiện câu hết-phiên ở **cả hai** nhánh thì cần BA nói rõ, vì yêu cầu đó ngược với `:1011`.

### Q7 · Lọc danh sách trạng thái theo máy trạng thái — hai màn quy định lệch nhau (phụ)
Màn Tư vấn viên `srs-fr-04-chuyen-gia-tvv.md:1554` quy định rất rõ "**Tùy chọn trạng thái mới hiển thị theo trạng thái hiện tại**" kèm 4 nhánh (a)-(d). Màn Tổ chức tư vấn `:1721` chỉ liệt kê phẳng "(Tạm dừng / Khôi phục / Vô hiệu hóa)", chốt kiểm tra transition đặt ở phía xử lý `:991`. Web đo được: màn Tổ chức tư vấn **đang lọc** đúng SM-TCTV (`:2392`-`:2395`) — tức làm nhiều hơn `:1721` yêu cầu và khớp kỳ vọng đối tác.
→ **Không có gì phải sửa ở code.** Chỉ đề nghị bổ sung câu lọc vào `:1721` cho khỏi lệch giữa hai màn.
