# Dấu vân tay bản dựng — lô F5 (QLDX_04/05/06 · QLDKTK_10 · QLDMTCTV_12)

Đo lúc **2026-08-07 02:03:49 giờ VN** (2026-08-06 19:03:50 GMT), trước khi mở màn nào.

| Hạng mục | Giá trị đo được |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (không phải env nghiệm thu đối tác `htpldn-uat.ospgroup.vn`) |
| Bó mã FE | `assets/index-DsMHK7Dp.js` · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | `Thu, 06 Aug 2026 18:51:25 GMT` (2026-08-07 **01:51:25** giờ VN) |
| `GET /` etag | `"6a74d7ad-428"` |
| Máy chủ web | `nginx/1.27.5` sau `Caddy` (`via: 1.1 Caddy`) |
| BE (OpenAPI `info`) | `HTPLDN API` · `version 1.0.0` (chuỗi này không đổi theo lần deploy → không dùng làm vân tay) |
| MailHog | `http://18.143.165.120:8025` (IP thô, không qua nip.io) |

> 🔴 **FE ĐÃ ĐƯỢC DEPLOY LẠI** so với lô F3/F4 cùng thư mục tuần 5:
> - F3/F4 (06/08, 14:13 giờ VN): bó mã `index-DIABnbIr.js`, etag `W/"6a74340b-428"`
> - Lô F5 (đo 07/08 02:03): bó mã `index-DsMHK7Dp.js`, etag `"6a74d7ad-428"`, last-modified 01:51 VN
>
> ⇒ Bản dựng FE mới hơn F3/F4 khoảng 12 phút trước lúc đo. Mọi verdict của lô này chỉ có hiệu lực cho
> đúng bó mã ghi ở trên; dev deploy lại thì phải đo lại.

## 🔴 FE ĐƯỢC DEPLOY LẠI LẦN NỮA GIỮA LÔ — 02:23:01 giờ VN 07/08

Phát hiện khi đo QLDX_06. Bó mã đổi `index-DsMHK7Dp.js` → **`index-D4Buvu4S.js`**, etag
`"6a74df15-428"`, last-modified `Thu, 06 Aug 2026 19:23:01 GMT` = **02:23:01 giờ VN**. Đã tự đo lại
bằng `curl` sau khi đóng QLDX_06 để xác nhận.

| Case | Bó mã FE thực chạy trong tab lúc đo | Ghi chú |
|---|---|---|
| QLDX_04 | `index-DsMHK7Dp.js` | đo 02:07–02:09, trước deploy |
| QLDX_05 | `index-DsMHK7Dp.js` | đo 02:19–02:30. Deploy rơi vào 02:23:01 **giữa** khoảng đo, nhưng tab **không reload** (flow cấm reload sau khi đặt mốc) nên JS đang chạy vẫn là bó mã cũ. Đối chứng máy chủ 02:28:46 trả 200 ⇒ deploy không hủy phiên đang mở |
| QLDX_06 | `index-D4Buvu4S.js` | đo 02:45–03:05, sau deploy |
| QLDKTK_10 · QLDMTCTV_12 | ghi tại `do/<MA_TC>.md` | đo sau deploy |

**Selector ô nhập tên đăng nhập — CHƯA KẾT LUẬN, đừng chép làm sự thật:** trên cùng bó mã
`index-D4Buvu4S.js`, lượt đo QLDX_06 báo ô nhập **mất** `placeholder="Nhập tên đăng nhập"`, lượt đo
QLDKTK_10 báo ô nhập **vẫn có** placeholder đó kèm `id="login-username"`. Đã thử đối chứng bằng cách
tải `assets/index-D4Buvu4S.js` và grep: **cả hai chuỗi đều 0 hit** — màn đăng nhập nằm ở chunk tách
riêng nên grep bó mã chính không phân giải được. ⇒ Hai quan sát chưa hòa giải; lô sau **phải
`take_snapshot` lấy uid thật**, đừng dựa vào selector placeholder ở CLAUDE.md §Rule 11 cho tới khi có
người đo lại dứt điểm.

**Giới hạn hiệu lực:** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` (ảnh QLDMTCTV_12 hiện
`V1.0.2`, 31/07/2026). Lô này đo trên env nội bộ ⇒ mọi verdict Pass là **Pass cho đúng bó mã ghi ở
bảng trên**, tới khi bản dựng lên env đối tác.

**Tài khoản:** theo prompt dùng bộ `_03`. Ghi tài khoản thực dùng ở từng file `do/<MA_TC>.md`.
Không dùng `admin` để ra verdict (quyền rộng che lỗi phân quyền — Flow 04 §Giai đoạn B bước 1);
`admin` chỉ dùng chuẩn bị dữ liệu nếu cần và phải khai rõ.
