# Dấu vân tay bản dựng — đợt reverify tuần 5 (2026-08-06)

Đo lúc **2026-08-06 18:44 giờ VN** (11:44 GMT), ngay sau khi tải lại trang đăng nhập.

| Hạng mục | Giá trị đo được |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu của đối tác (`htpldn-uat.ospgroup.vn`) |
| Chuỗi phiên bản trên màn | `HTPLDN · V1.0.8` (chân sidebar) |
| Bó mã FE | `assets/index-DIABnbIr.js` · `assets/index-DVlgOkLg.css` · `assets/index-DNsk8fKL.css` |
| `GET /` last-modified | `Thu, 06 Aug 2026 07:13:15 GMT` (14:13:15 giờ VN) |
| `GET /` etag | `W/"6a74340b-428"` |
| Máy chủ web | `nginx/1.27.5` sau `Caddy` (`via: 1.1 Caddy`) |
| BE (OpenAPI `info`) | `HTPLDN API` · `version 1.0.0` (chuỗi này KHÔNG đổi theo lần deploy → không dùng làm vân tay) |

> 🔴 **Bó mã FE + last-modified + etag GIỐNG HỆT** số đo của lô B7 cùng ngày (14:13:15 giờ VN).
> ⇒ FE **chưa được deploy lại** kể từ 14:13 hôm nay. Mọi kết luận của đợt này chỉ có hiệu lực cho
> đúng bản dựng ghi ở bảng trên; nếu dev deploy lại thì phải đo lại.

---

## 🔴 Cập nhật 2026-08-07 — bảng trên ĐÃ LẠC HẬU, và nhãn phiên bản KHÔNG dùng làm định danh được

Từ chiều 06/08 đến rạng sáng 07/08 env nội bộ deploy **5 bản khác nhau**. Đã loại trừ khả năng nhiều
máy chủ phục vụ bản khác nhau: 6/6 lượt `GET /` liên tiếp trả **cùng etag, cùng bó mã**.

| # | Bó mã FE | `GET /` last-modified (GMT) | Giờ VN | Nhãn ở sidebar | Ai đo ở đây |
|---|---|---|---|---|---|
| 1 | `index-DIABnbIr.js` | Thu, 06 Aug 2026 07:13:15 | 06/08 14:13 | V1.0.8 | đợt reverify tuần 5 gốc (bảng trên) |
| 2 | `index-CxS5qW_0.js` | Thu, 06 Aug 2026 12:48:25 | 06/08 19:48 | V1.0.9 | — |
| 3 | `index-B2W2Krcs.js` | Thu, 06 Aug 2026 17:39:54 | 07/08 00:39 | V1.0.10 | F3: case 37, 51, 64 |
| 4 | `index-DsMHK7Dp.js` | Thu, 06 Aug 2026 18:51:25 | 07/08 01:51 | **V1.0.9** ⚠️ | F3: case 126, 127 |
| 5 | `index-D4Buvu4S.js` | Thu, 06 Aug 2026 19:23:01 | 07/08 02:23 | — | lên giữa lúc đang đo case 127 |

🔴 **Bản #4 có bó mã MỚI HƠN bản #3 nhưng sidebar lại lùi nhãn từ V1.0.10 về V1.0.9.**
⇒ **Chuỗi phiên bản trên màn KHÔNG phải định danh bản dựng.** Định danh thật = **bó mã `assets/index-*.js`
+ `last-modified`**. Mọi báo cáo từ nay ghi bó mã, và ghi kèm **mốc giờ đo** — vì với nhịp deploy này,
ghi mỗi ngày là không đủ để truy ra bản nào.

⚠️ **Hệ quả cho quy trình đo:** tab trình duyệt mở lâu vẫn chạy mã JS cũ dù máy chủ đã đổi. Mỗi agent đo
phải lấy vân tay **cả đầu và cuối phiên**; hai đầu khác nhau ⇒ báo rõ quan sát nào rơi trước/sau mốc deploy.

**Tài khoản dùng đo:** `cbnv_tw` / `Test@1234` (CB Nghiệp vụ - Trung ương), đăng nhập qua UI thật
(mật khẩu → mã xác thực 6 số lấy ở MailHog `http://18.143.165.120:8025`). Không dùng `admin` để ra
verdict (quyền rộng che lỗi phân quyền — flow 04 §Giai đoạn B bước 1).

**Giới hạn hiệu lực:** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản `HTPLDN · V1.0`.
Đợt này đo trên env nội bộ bản `V1.0.8` ⇒ mọi verdict Pass là **Pass tạm** cho tới khi bản dựng này
lên env đối tác.
