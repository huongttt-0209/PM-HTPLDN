# Dấu vân tay bản dựng — lô F6 (FLOW 04, 4 case dev báo đã fix)

Env: `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu đối tác
`htpldn-uat.ospgroup.vn`. Máy chủ web `Caddy`.

## 🔴 Env deploy LIÊN TỤC trong đúng phiên đo — phải ghi vân tay theo từng case

| Mốc (giờ VN) | Bó mã FE | `last-modified` của `/` và bó mã | Ghi nhận |
|---|---|---|---|
| 06/08 14:13 | `index-DIABnbIr.js` | `06 Aug 2026 07:13:15 GMT` | Lô 06/08 (`../BAN-DUNG.md`) |
| 06/08 19:48 | `index-CxS5qW_0.js` | `06 Aug 2026 12:48:25 GMT` | Ghi nhận ở lô F3 |
| 07/08 **00:39** | `index-B2W2Krcs.js` | `06 Aug 2026 17:39:54 GMT` · etag `W/"6a74c6ea-1127fd"` | Bó mã lúc tôi mở trang đăng nhập (01:52) |
| 07/08 **01:51** | **`index-DsMHK7Dp.js`** | `06 Aug 2026 18:51:25 GMT` · etag `W/"6a74d7ad-1127fb"` (bó mã) · `W/"6a74d7ad-428"` (`/`) | **Bản dựng của case dòng 65 `DGKQHTVV_02` và dòng 68 `DGKQHTVV_04`** |
| 07/08 **02:23** | **`index-D4Buvu4S.js`** | `06 Aug 2026 19:23:01 GMT` · etag `W/"6a74df15-428"` (`/`) | **Bản dựng của case dòng 285 `QLNDTVVCG_19` và dòng 288 `QLNDTVVCG_38`** |

⚠️ **Deploy lần 5 rơi vào giữa lô đo.** Phát hiện lúc 02:23 khi tải lại `/` trước case dòng 285: tab đang chạy
`index-DsMHK7Dp.js` nhưng máy chủ đã phục vụ `index-D4Buvu4S.js`. Đã **tải lại trang bằng địa chỉ** trước khi
đo tiếp ⇒ hai case sau chạy trên bó mã mới, hai case trước chạy trên bó mã cũ. **Verdict của 4 case KHÔNG
cùng một bản dựng** — ghi rõ ở từng phiếu.

CSS kèm bản dựng hiện hành: `assets/index-DVlgOkLg.css` · `assets/resizable-title-CMKNK2uU.css`.
BE (OpenAPI `info`): `HTPLDN API` · `version 1.0.0` — chuỗi này KHÔNG đổi theo lần deploy ⇒ **không dùng làm vân tay**.

**Vì sao mọi phép đo lô F6 chạy trên `index-DsMHK7Dp.js`:** trang đăng nhập nạp lúc 01:52 còn chạy
`index-B2W2Krcs.js`, nhưng thao tác vào màn danh sách vụ việc là **điều hướng thật** (tải lại tài liệu) nên
từ đó trở đi trình duyệt nạp bó mã mới. Đo lại lúc 02:12: `GET /` phục vụ đúng `index-DsMHK7Dp.js`.

## 🔴 Chuỗi phiên bản ở chân sidebar KHÔNG dùng được làm vân tay

Chân sidebar đọc được `HTPLDN · V1.0.9` **ở cả ba bó mã** `index-B2W2Krcs.js` (deploy 00:39),
`index-DsMHK7Dp.js` (deploy 01:51) và `index-D4Buvu4S.js` (deploy 02:23) — đọc bằng cả ảnh chụp lẫn DOM
lúc 02:12 và 02:27. **Ba lần deploy liên tiếp, chuỗi này đứng yên** ⇒ bằng chứng đủ mạnh để loại nó khỏi vai
trò vân tay.

⚠️ **Lệch với hồ sơ lô F3 cùng ngày:** `F3-devfix-2026-08-07/TIEN-DO.md:169` và `do/CNDSMLTVV_01.md:16`
ghi bó mã `index-B2W2Krcs.js` ứng với chuỗi `HTPLDN · V1.0.10`. Tôi đo lại chính bó mã đó và chuỗi trên
màn là `v1.0.9`. **Không tự sửa hồ sơ lô F3** — ghi nhận chênh lệch để người điều phối chốt. Hệ quả thực
dụng: **dùng tên bó mã + `last-modified`, đừng dùng chuỗi chân sidebar** để nói "đo trên bản nào".

## Tài khoản dùng đo

Theo prompt ("dùng tài khoản 04"): **`cbnv_tw_04` / `Test@1234`** — thanh trên hiển thị
`CB Nghiệp vụ - Trung ương #04` · `Cán bộ Nghiệp vụ Trung ương` · `BTP · TW`; chân sidebar
`Bộ Tư Pháp · Cục Bổ trợ tư pháp`. `GET /api/v1/auth/me` trả `vaiTros: ["CB_NV_TW"]`,
`donViId = 00000000-0000-4000-8000-000000000001`, `capDonVi = TW`.

Đăng nhập bằng UI thật (mật khẩu → mã xác thực 6 số lấy ở MailHog `http://18.143.165.120:8025`,
mã `192370` lúc 01:53). **Không dùng `admin` để ra verdict.**

Vai trò khác (nếu vế Cn của case yêu cầu) được ghi bổ sung tại `do/<Mã TC>.md` của chính case đó.

## Giới hạn hiệu lực

Đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` (bộ tài khoản khác). Lô này đo trên env nội bộ,
bó mã `index-DsMHK7Dp.js` ⇒ mọi verdict là **kết luận cho đúng env + bó mã đó**, không suy sang env đối tác
và không suy ngược cho các bó mã trước.
