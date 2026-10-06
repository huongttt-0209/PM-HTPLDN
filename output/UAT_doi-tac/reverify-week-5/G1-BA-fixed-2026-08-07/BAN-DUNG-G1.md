# Dấu vân tay bản dựng — lô G1 (2026-08-07)

> **Nhãn phiên bản ở sidebar KHÔNG dùng làm định danh** — đã có ca bó mã mới hơn mà nhãn lại lùi
> (xem `../BAN-DUNG.md` §cập nhật 07/08). Định danh thật = **bó mã `assets/index-*.js` + `last-modified`**.

## Vân tay ĐẦU lô (lead đo, chưa qua trình duyệt)

| Hạng mục | Giá trị |
|---|---|
| Thời điểm đo | **2026-08-07 14:51:13 giờ VN** (07:51:13 GMT) |
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, không phải env nghiệm thu đối tác |
| Bó mã FE | **`assets/index-BbPPdate.js`** · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | **Fri, 07 Aug 2026 06:47:57 GMT** = **07/08 13:47:57 giờ VN** |
| `GET /` etag | `W/"6a757f9d-428"` |
| Máy chủ web | `nginx/1.27.5` sau `Caddy` |

🔴 **Đây là bản dựng MỚI**, khác toàn bộ 5 bản đã ghi ở `../BAN-DUNG.md` (bản gần nhất ở đó là
`index-D4Buvu4S.js`, 06/08 19:23 GMT). Bản này lên lúc **13:47 hôm nay**, tức sau khi dev đánh dấu
`Fixed` — nên các fix của lô này **có khả năng nằm trong bản này**.

## Bắt buộc với mọi agent đo

1. Đo vân tay **đầu phiên và cuối phiên** của mình, ghi vào note case.
   Lệnh: `curl -sk -D - -o /tmp/idx.html https://18.143.165.120.nip.io/ | grep -iE "last-modified|etag"`
   rồi `grep -oE 'assets/index-[A-Za-z0-9_-]+\.js' /tmp/idx.html`
2. **Tải lại trang** (hard reload) trước khi verify — tab MCP mở lâu vẫn chạy bó mã cũ dù máy chủ đã đổi.
3. Hai đầu vân tay khác nhau ⇒ ghi rõ quan sát nào rơi trước / sau mốc deploy, và cân nhắc đo lại case
   đã chạy trước mốc.

## Bảng ghi vân tay theo agent — mỗi agent đo tự điền

| Agent | Case | Vân tay đầu phiên | Vân tay cuối phiên | Lệch? |
|---|---|---|---|---|
| B1 | VVDTN_06 · VVDHT_06 · VVDHTHT_06 | 07/08 14:53 — `index-BbPPdate.js` · lm `Fri, 07 Aug 2026 06:47:57 GMT` · etag `W/"6a757f9d-428"` | 07/08 15:35 — `index-BbPPdate.js` · lm `Fri, 07 Aug 2026 06:47:57 GMT` · etag `W/"6a757f9d-428"` | **Không lệch** — cả 3 case đo trọn trong cùng một bản dựng, không có deploy chen giữa |
| B2 | VVTTG_05 · VVTDVQL_06 · VVTLV_05 | | | |
| B3 | VVTLHDN_05 · VVTTGCT_05 · CPCTHTTTG_05 | | | |
| B4 | VVDTN_04 | | | |
| B5 | QLNDTVVCG_OOS_04 | | | |

## Giới hạn hiệu lực (ghi vào mọi verdict)

Đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn`. Lô này đo trên env nội bộ
⇒ mọi **Pass là Pass tạm** cho tới khi bản dựng này lên env đối tác.
