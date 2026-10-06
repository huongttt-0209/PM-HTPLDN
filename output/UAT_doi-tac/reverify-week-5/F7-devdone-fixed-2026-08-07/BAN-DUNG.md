# Dấu vân tay bản dựng — lô F7 (re-verify 15 phiếu `Dopai = dev done` + `Trạng thái dev fix = Fixed`)

**Env đo:** `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu của đối tác
(`htpldn-uat.ospgroup.vn`). Mọi verdict chỉ có hiệu lực trên env + bản dựng ghi dưới đây.

## Đo ĐẦU phiên

| Hạng mục | Giá trị đo được |
|---|---|
| Thời điểm đo | **2026-08-07 09:46:05 giờ VN** (02:46:05 GMT) |
| Bó mã FE | `assets/index-eWHwDgt2.js` · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | `Fri, 07 Aug 2026 02:11:03 GMT` → **09:11:03 giờ VN** |
| `GET /` etag | `W/"6a753eb7-428"` |
| Máy chủ web | `nginx/1.27.5` sau `Caddy` (`via: 1.1 Caddy`) |

> 🔴 **Đây là bản dựng MỚI, chưa từng đo ở lô nào trước.** Bó mã `index-eWHwDgt2.js` khác toàn bộ 5 bản
> đã liệt kê ở [../BAN-DUNG.md](../BAN-DUNG.md) (`DIABnbIr` · `CxS5qW_0` · `B2W2Krcs` · `DsMHK7Dp` ·
> `D4Buvu4S`). FE được deploy lúc **09:11 giờ VN 07/08**, tức 35 phút trước khi lô này bắt đầu đo.
> ⇒ Kết quả vòng 06/08 (bản `V1.0.8` / `index-DIABnbIr.js`) KHÔNG dùng lại được, phải đo lại thật.

**Quy tắc theo BAN-DUNG.md gốc:** chuỗi phiên bản in ở chân sidebar (`V1.0.x`) **KHÔNG phải định danh
bản dựng** — đã có tiền lệ bó mã mới hơn mà nhãn lùi số. Định danh thật = bó mã `assets/index-*.js`
+ `last-modified`. Mỗi phiên đo lấy vân tay **cả đầu và cuối**; hai đầu khác nhau ⇒ phải ghi rõ quan
sát nào rơi trước/sau mốc deploy.

## Đo CUỐI phiên

| Hạng mục | Giá trị đo được |
|---|---|
| Thời điểm đo | **2026-08-07 10:41 giờ VN** (03:41 GMT) — trước khi đo phiếu `QLHSDNHTCP_03` |
| Bó mã FE | `assets/index-eWHwDgt2.js` · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | `Fri, 07 Aug 2026 02:11:03 GMT` |
| `GET /` etag | `W/"6a753eb7-428"` |

> ✅ **Hai đầu phiên KHÔNG đổi.** Bó mã, `last-modified` và `etag` ở lần đo cuối trùng khít lần đo đầu
> (09:46) ⇒ **không có bản dựng nào xen giữa phiên**. Mọi quan sát trong lô — vế Quản trị hệ thống đo
> lúc 09:48, các vế Cán bộ Nghiệp vụ đo 09:54–10:32, phiếu `QLHSDNHTCP_03` đo 10:42–10:58 — đều rơi
> **cùng một bó mã**, nên so sánh được với nhau. Điều này đáp ứng đúng bẫy số 3 của phiếu `CTTTG_04`
> ("hai vai trò phải đo trên CÙNG một bó mã thì mới so sánh được").

## Tài khoản dùng đo

| Vai trò | Tài khoản | Dùng để |
|---|---|---|
| Quản trị hệ thống (QTHT, TW) | `admin` / `Secret@123` | **Vai trò ra verdict** cho 14 phiếu báo cáo — đúng vai trò trong ảnh nghiệm thu của đối tác (10/10 ảnh hai vòng đều hiện "Quản trị viên · QTHT") |
| CB Nghiệp vụ - Trung ương | `cbnv_tw_03` … `_05` / `Test@1234` | Vế chống hồi quy (phần đang chạy tốt không được hỏng) |

> Ngoại lệ có ý thức với §Nguyên tắc 3 "admin chỉ dùng prep data": ở 14 phiếu này **chính vai trò quản
> trị hệ thống là đối tượng kiểm** — lỗi đối tác báo phát sinh khi đăng nhập bằng vai trò đó. Đây đúng
> ca "quản trị chính là vai trò cần kiểm" mà FLOW 03 §Giai đoạn B bước 1 cho phép.
