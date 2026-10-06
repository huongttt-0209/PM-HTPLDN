# Dấu vân tay bản dựng — lô re-verify 21 phiếu "Xuất PDF · Báo cáo thống kê"

**Env đo:** `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu của đối tác
(`htpldn-uat.ospgroup.vn`). Mọi verdict chỉ có hiệu lực trên env + bản dựng ghi dưới đây.

## Đo ĐẦU phiên

| Hạng mục | Giá trị đo được |
|---|---|
| Thời điểm đo | **2026-08-07 18:2x giờ VN** (đo qua `curl`, trước khi mở phiên trình duyệt) |
| Bó mã FE | `assets/index-BbPPdate.js` · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | `Fri, 07 Aug 2026 06:47:57 GMT` → **13:47:57 giờ VN 07/08** |
| `GET /` etag | `"6a757f9d-428"` |
| Máy chủ web | `nginx/1.27.5` sau `Caddy` (`via: 1.1 Caddy`) |

> 🔴 **Bản dựng MỚI so với lô F7 sáng cùng ngày.** Lô F7 đo lúc 09:46–10:41 giờ VN trên bó mã
> `assets/index-eWHwDgt2.js` (`last-modified` 02:11:03 GMT = 09:11 giờ VN). Bó mã hiện tại
> `index-BbPPdate.js` được đẩy lên lúc **13:47 giờ VN**, tức SAU khi lô F7 kết thúc.
> ⇒ **Không được dùng lại kết quả của lô F7** — kể cả vế Quản trị hệ thống mà F7 đã ghi là ĐẠT.
> Phải đo lại thật trên bó mã này.

**Quy tắc định danh bản dựng:** chuỗi phiên bản in ở chân thanh bên (`V1.0.x`) **KHÔNG phải** định danh
bản dựng — đã có tiền lệ bó mã mới hơn mà nhãn phiên bản lùi số. Định danh thật = bó mã `assets/index-*.js`
+ `last-modified`. Mỗi phiên đo lấy vân tay **cả đầu và cuối**; hai đầu khác nhau ⇒ phải ghi rõ quan sát
nào rơi trước/sau mốc triển khai.

## Đo CUỐI phiên

| Hạng mục | Giá trị đo được |
|---|---|
| Thời điểm đo | **2026-08-07 18:52 giờ VN** (11:52 GMT) — sau khi đo xong phiếu cuối `CTTTG_05` |
| Bó mã FE | `assets/index-BbPPdate.js` · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | `Fri, 07 Aug 2026 06:47:57 GMT` |
| `GET /` etag | `"6a757f9d-428"` |

> ✅ **Hai đầu phiên KHÔNG đổi.** Bó mã, `last-modified` và `etag` ở lần đo cuối trùng khít lần đo đầu
> ⇒ **không có bản dựng nào xen giữa phiên**. Mọi quan sát trong lô — vế Quản trị hệ thống đo 18:28–18:31,
> 21 phiếu vế Cán bộ Nghiệp vụ đo 18:34–18:51 — đều rơi **cùng một bó mã**, nên so sánh được với nhau.
>
> Đối chứng thêm: bó mã đọc **trong chính tab đang đo** (`script[src]`) ở cả hai phiên trình duyệt
> (`admin` và `cbnv_tw_05`) đều là `index-BbPPdate.js`, trùng bó mã máy chủ đang phục vụ ⇒ không có
> chuyện tab chạy mã cũ còn sót trong bộ nhớ.

## Tài khoản dùng đo

| Vai trò | Tài khoản | Dùng để |
|---|---|---|
| CB Nghiệp vụ - Trung ương | `cbnv_tw_05` / `Test@1234` | **Vai trò ra verdict** cho vế A — chạy đúng 4 bước của bug gốc, xuất PDF từng loại báo cáo (bộ tài khoản 05 do prompt chỉ định) |
| Quản trị hệ thống (QTHT, TW) | `admin` / `Secret@123` | Vế B — kiểm quyết định nghiệp vụ chốt 06/08 (ẩn mục menu, chặn cửa vào, câu từ chối bằng tiếng Việt). Đo **một lần**, áp chung 21 phiếu vì cả 23 loại báo cáo dùng chung một màn |

> Ngoại lệ có ý thức với nguyên tắc "admin chỉ dùng để dựng dữ liệu": ở vế B **chính vai trò quản trị hệ
> thống là đối tượng kiểm** — triệu chứng đối tác báo lại ngày 31/07 (`Forbidden`) phát sinh khi đăng nhập
> bằng vai trò đó. `admin` nằm ngoài bộ tài khoản 05, đã báo và được chấp thuận trước khi chạy.
