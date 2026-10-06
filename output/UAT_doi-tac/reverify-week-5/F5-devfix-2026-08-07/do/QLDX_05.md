# QLDX_05 — Gia hạn phiên (đo Giai đoạn B)

**Case:** QLDX_05 · dòng 165 · tab `bug`
**Chuẩn chấm đã khóa:** [`../chuan/QLDX_04-05-06.md`](../chuan/QLDX_04-05-06.md) §2 (QLDX_05) — Giai đoạn B **không đổi** quan hệ MATCH/DIFF/GAP, **không mở rộng** phép đo, **không ghi Google Sheet**.
**Nguồn chuẩn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (số dòng do Giai đoạn A mở đọc trực tiếp).

> 🔴 **Cả 2 vế của case này đều là GAP → route BA.** Số đo dưới đây **KHÔNG dùng để Pass**. Đo để BA có dữ kiện bổ sung đặc tả và để biết dev đang theo phía nào. Mọi cột "đạt/không đạt" là **đối chiếu với expected của ĐỐI TÁC**, **không phải** chuẩn SRS.

---

## 1. Điều kiện đo

| Hạng mục | Giá trị thực |
|---|---|
| **Tài khoản thực dùng** | **`cbnv_tw_03` / `Test@1234`** — đúng bộ `_03` theo prompt. **Không phải fallback**: đăng nhập thành công ngay lần đầu, không gặp lock, không dùng sibling `_04`/`_05`. **Không dùng `admin`.** |
| Danh tính hiển thị | "CB Nghiệp vụ - Trung ương #03" · "Cán bộ Nghiệp vụ Trung ương" · `BTP · TW` |
| Danh tính trong JWT | `sub=9b557200-be4b-46ac-b84b-fe6c154dc65f` · `vaiTro=["CB_NV_TW"]` · `capDonVi="TW"` · `authMethod="LOCAL"` · `idleTtl=1800` (=30 phút) · `jti=5e6ef7c9-…-06e8e9061965` · `iat=1786044017` (02:20:17) |
| Cách đăng nhập | UI thật: mật khẩu → OTP 6 số lấy ở MailHog `http://18.143.165.120:8025`, lọc đúng mailbox `cbnv_tw_03@htpldn.test` (`limit=5`, mã `146986` tạo lúc 02:20:05) |
| **Env** | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (không phải env nghiệm thu đối tác `htpldn-uat.ospgroup.vn`) |
| **Bó mã FE** | `assets/index-DsMHK7Dp.js` · `assets/index-DVlgOkLg.css` — đọc trực tiếp từ DOM lúc 02:19:39, **khớp** [`../BAN-DUNG.md`](../BAN-DUNG.md) |
| Phiên bản app | sidebar hiện `HTPLDN · V1.0.9` |
| **Thời điểm đo** | 2026-08-07, giờ VN: tải trang 02:19:39 · đăng nhập xong 02:20:17 · sang màn tĩnh 02:20:50 · dựng mốc 02:21:23 · **modal bật 02:21:54** · **bấm gia hạn 02:22:28** · mốc logout gốc 02:26:53 · đối chứng API 02:28:46 · mẫu cuối 02:30:13 |
| Trang được tải mới | Có — tải lại `/login` lúc 02:19:39 rồi mới đo (phiên của case trước đã tự hết do idle, tab đang nằm ở `/login`) |
| `Ghi nhớ đăng nhập` | **KHÔNG tick** — verify `checked=false` ngay trước submit (`srs-fr-10-quan-tri.md:1884` ghi checkbox này "Extend session TTL" → tick vào là lệch mốc đo) |
| Số tab dùng phiên | 1 (tab `about:blank` của profile `--isolated` không dùng phiên) |

## 2. Tiền đề đã dựng

**Màn đang mở khi dựng mốc:** `/chuyen-gia-tvv/danh-sach` — "Tư vấn viên / Chuyên gia", bảng 7 dòng.
Đã **chủ động rời `/dashboard`** bằng click sidebar (không `navigate_page`) vì Dashboard tự làm mới 60 giây (`srs-fr-01-dashboard.md:49`) — đúng cảnh báo "Bẫy đo #3".

**Baseline đặt (ép mốc, không chờ 25 phút thật):**

| | Giá trị (giờ VN) |
|---|---|
| `t_set` — thời điểm đặt mốc | **02:21:23.717** |
| `t_baseline` ghi vào `localStorage["auth-last-activity"]` | **01:56:53.717** (= `t_set − 24.5 phút`) |
| Mốc modal cảnh báo kỳ vọng (`t_baseline + 25′`) | 02:21:53.717 |
| **`t_logout_goc` = `t_baseline + 30′`** | **02:26:53.717** ← **trục của phép đo C2** |

**Tiền đề đã kiểm tra ở case liền trước — KHÔNG đo lại:** [`QLDX_04.md`](QLDX_04.md) §3 C1 đã chốt modal cảnh báo bật đúng mốc **idle 25.0′**. Lần này modal bật ở **02:21:54.1 ± 0.13s**, kẹp giữa idle **25.004′ (chưa có)** và **25.008′ (đã có)** — tái lập đúng tiền đề, dùng làm điểm khởi hành cho C1/C2 chứ không chấm lại vế 25′.

**Cách quan sát:** bộ ghi `setInterval` 250 ms **thuần đọc DOM + đọc localStorage**. Không dispatch `mousemove`/`click`/`keydown`/`scroll`/`touchstart`; không reload; không navigate sau khi đặt mốc. Trong lúc chờ chỉ poll bằng `evaluate_script` (đọc không reset mốc). Lấy chữ bằng **`innerText` của phần tử modal đang hiển thị** (lọc `getClientRects().length>0` + `display`/`visibility`/`opacity` + `offsetParent|fixed`) — **không dùng `textContent`**. Tổng **2119 mẫu**.

## 3. Bảng kết quả theo từng vế

| Vế | Quan hệ (đã khóa) | Số đo thực | Đối chiếu **với expected ĐỐI TÁC** | Artifact |
|---|---|---|---|---|
| **C1** — bấm "Gia hạn phiên" → hộp thoại đóng | **GAP → BA** | Bấm **02:22:28.831** → modal hết hiện tại **02:22:29.218** ⇒ đóng trong **≤ 0.39 s**. Kẹp: mẫu 02:22:28.968 `modal=HIỆN` → mẫu 02:22:29.218 `modal=tắt`. Suốt **1608/1608** mẫu còn lại (tới 02:30:13) modal **không bật lại** | ✅ **Đúng y expected** ("đóng hộp thoại") — *ghi nhận, cấm chấm Pass* | `QLDX_05-C1-truoc-khi-bam-gia-han.png` · `QLDX_05-C1-sau-khi-bam-gia-han.png` · `QLDX_05-timeline.txt` §B |
| **C2** — đồng hồ đếm được đặt lại về 30 phút | **GAP → BA** | 3 dấu hiệu đồng thuận: **(a)** `auth-last-activity` **01:56:53.717 → 02:22:28.831** (idle FE về `0.002′`, độ trễ phát hiện ≤ 137 ms) · **(b)** đi qua `t_logout_goc` **02:26:53.717** mà **không** bị đá `/login`, vẫn đứng `/chuyen-gia-tvv/danh-sach`, `h1 = "Tư vấn viên / Chuyên gia"`, modal **không** bật lại (đúng suy luận: mốc cảnh báo mới **02:47:28.8** chưa tới) · **(c)** đối chứng API sau mốc gốc = **HTTP 200** | ✅ **Đúng y expected** ("đặt lại đồng hồ đếm 30 phút") — *ghi nhận, cấm chấm Pass* | `QLDX_05-timeline.txt` §C · `QLDX_05-C2-sau-moc-logout-goc.png` · `QLDX_05-doi-chung-api.txt` |

**Tổng: 0 vế route TEST (cả 2 vế đều GAP → BA). Hiện trạng app khớp y expected đối tác ở cả 2 vế, nhưng theo chuẩn chấm §4 "Chặn PASS-oan" thì KHÔNG được Pass — phải chuyển BA bổ sung đặc tả (Q4).**

### Chi tiết C1 — modal đóng, không phải "node biến mất"

Sau khi modal tắt, DOM **vẫn còn 1 node `.ant-modal`** nhưng node đó **không hiện** (bộ lọc visible trả `false`). Nếu chỉ kiểm "node có tồn tại hay không" sẽ kết luận sai là hộp thoại còn hiện. Số đo dùng bộ lọc visible nên phản ánh đúng thứ người dùng thấy — và ảnh `QLDX_05-C1-sau-khi-bam-gia-han.png` xác nhận trực quan: màn danh sách sạch, không còn lớp phủ.

### Chi tiết C2 — vì sao không phải PASS-oan

Chuẩn chấm §4 cảnh báo: *"Không Pass QLDX_05 chỉ vì hộp thoại đóng lại… phải có đối chứng 200 sau mốc 30′ gốc"*. Đã làm đúng:

- **Không** kết luận từ mỗi việc modal đóng (đó có thể chỉ là dismiss).
- **Không** kết luận từ mỗi `localStorage` (đó là đồng hồ FE).
- **Phép thử quyết định** = đi qua `t_logout_goc` **02:26:53.717** an toàn. Nếu đồng hồ **không** được đặt lại thì app phải tự đăng xuất tại đúng mốc đó. Thực tế: mẫu 02:26:40.971 và 02:26:56.219 đều `modal=tắt`, `url=/chuyen-gia-tvv/danh-sach`; ảnh chụp lúc **02:28:27** (+93.9 s) vẫn nguyên màn cũ, vẫn đăng nhập là `#03`.
- Hai lệnh chờ thụ động (`wait_for` trên chuỗi `"Nhập tên đăng nhập"`, tổng 265 s) đều **timeout** ⇒ trang **chưa từng** hiện form đăng nhập trong khoảng chờ. Đây là phép bắt redirect `/login` độc lập với bộ ghi.

## 4. Đối chứng độc lập (đúng MỘT đường)

`fetch('/api/v1/auth/me', {credentials:'include', cache:'no-store'})` — gọi từ trong trang vì `access_token` là cookie **HttpOnly** (`document.cookie` đọc ra **rỗng**).

| | Giá trị |
|---|---|
| reqid | **282** |
| Thời điểm gọi | **02:28:46** giờ VN = **+113.2 s** sau `t_logout_goc` |
| Server `date` header | `Thu, 06 Aug 2026 19:28:47 GMT` = 02:28:47 giờ VN |
| **Mã HTTP thật** | **200** (`ok=true`, body 5772 bytes, `application/json`) |
| Body | `{"success":true,"data":{"userId":"9b557200-…","hoTen":"CB Nghiệp vụ - Trung ương #03","vaiTro":["CB_NV_TW"],…}}` |

⇒ **200, không phải 401** ⇒ sau mốc auto-logout **gốc**, máy chủ **vẫn coi phiên còn hiệu lực** và vẫn phân giải đúng danh tính `cbnv_tw_03`. Gia hạn có hiệu lực thật, không chỉ là đóng modal ở FE.

**Request của chính cú bấm:** `reqid=269 GET /api/v1/auth/me [304]`, `date: 19:22:28 GMT` = **02:22:28** — trùng khít thời điểm bấm ⇒ việc gia hạn **có** gửi request xuống BE, **không** phải thao tác thuần client-side. Nhưng đó là `/auth/me` (đọc danh tính), **không** phải endpoint gia hạn/refresh riêng — khớp ghi nhận Giai đoạn A rằng `srs-fr-16-api.md` không đặc tả endpoint refresh/extend nào. Token **không** được phát hành lại: cookie ở `reqid=269`, `281`, `282` đều cùng `jti` và `iat=1786044017` (02:20:17, thời điểm đăng nhập).

**Không có 401 nào sau khi bấm.** Thống kê 33/33 request xhr/fetch: `401 × 1` (chỉ `reqid=181`, probe **trước** khi đăng nhập, referer `/login`) · `200 × 6` · `304 × 26` · 0 lỗi 5xx · 0 lỗi 4xx khác. `list_console_messages` (error + warn) = **rỗng**. ⇒ Bẫy đo #1 (nhầm modal 401 của `srs-fr-02-hoi-dap.md:1135`) đã loại trừ.

> **⚠️ Giới hạn của đối chứng — ghi rõ để không suy quá số đo.** Trong toàn bộ khoảng chờ, FE vẫn tự poll `/api/v1/thong-baos/unread-count` đều đặn (`reqid=270..281`, ~30 s/lần), mỗi request đều mang cookie. Vì vậy mã 200 chứng minh chắc chắn *"sau mốc gốc phiên vẫn còn hiệu lực phía máy chủ"*, nhưng **không tách riêng được** nguyên nhân là cú bấm — các poll nền cũng chạm máy chủ. Vế "đồng hồ đã được đặt lại" do đó được chốt bằng dấu hiệu **không bị nhiễu bởi poll nền**: app đi qua `t_logout_goc` mà không tự đăng xuất, trong khi [`QLDX_04.md`](QLDX_04.md) §6 đã ghi nhận app **có** tự đăng xuất khi idle vượt 30′ *dù* các poll nền này vẫn chạy (tức poll nền không ngăn được auto-logout). Quan sát 30′ auto-logout thuộc vế **QLDX_06 C2a** — ở đây chỉ dùng làm ngữ cảnh, không dùng làm số đo của QLDX_05.

## 5. Dữ kiện cho câu hỏi BA (Q4)

Chuẩn chấm §6 **Q4** hỏi 4 điểm về hành vi nút `[Gia han]` (`:1891` để ô "Hành vi" = "—"). Số đo lần này trả lời được 3/4 điểm — **là dữ kiện để BA chốt đặc tả, không phải verdict**:

| Câu hỏi Q4 | Hiện trạng đo được trên bó mã `index-DsMHK7Dp.js` |
|---|---|
| (a) Hộp thoại có tự đóng sau khi gia hạn không? | **Có** — đóng trong ≤ 0.39 s sau khi bấm |
| (b) Đồng hồ idle được đặt lại về bao nhiêu? | Đặt lại **về 0** (mốc thao tác cuối = chính thời điểm bấm) ⇒ trần idle quay lại **30 phút** đầy đủ, mốc cảnh báo mới = bấm + 25′ |
| (c) Việc gia hạn có gọi xuống BE hay chỉ là hành vi trình duyệt? | **Có gọi BE** — `GET /api/v1/auth/me` tại đúng thời điểm bấm, trả 304; phiên còn hiệu lực server-side sau mốc gốc (200). **Không** phát hành lại token (cùng `jti`/`iat`). **Không** có endpoint gia hạn/refresh riêng |
| (d) Có giới hạn số lần gia hạn liên tiếp không? | **Chưa đo** — phép đo này chỉ bấm **1 lần** theo kỷ luật "không mở rộng case". Cần BA chốt yêu cầu trước khi QA thiết kế phép đo nhiều lần |

## 6. Bug mới

**Không có.** Trong đúng các bước bắt buộc của vế đang verify (đăng nhập → sang màn danh sách → dựng mốc idle → chờ modal → bấm "Gia hạn phiên" → chờ qua mốc logout gốc → đối chứng API), không có 4xx/5xx nào tự lộ ra; console error + warn = **rỗng**. 401 duy nhất (`reqid=181`) xảy ra **trước** khi đăng nhập, là hành vi bình thường của trang đăng nhập khi chưa có token.

**Bug candidate:** không có.

## 7. Artifact

| File | Nội dung |
|---|---|
| [`../image/QLDX_05-C1-truoc-khi-bam-gia-han.png`](../image/QLDX_05-C1-truoc-khi-bam-gia-han.png) | Screenshot **viewport** lúc modal đang hiện, ngay trước khi bấm. Đã mở lại bằng Read xác nhận: hộp thoại "Phiên làm việc sắp hết hạn", đủ chuỗi thông báo, đồng hồ `4:53`, đúng 2 nút `[Đăng xuất] [Gia hạn phiên]`, account `#03`, `V1.0.9`, đang ở màn Tư vấn viên / Chuyên gia |
| [`../image/QLDX_05-C1-sau-khi-bam-gia-han.png`](../image/QLDX_05-C1-sau-khi-bam-gia-han.png) | Screenshot **viewport** ngay sau khi bấm. Đã Read xác nhận: **không còn hộp thoại**, không còn lớp phủ, bảng danh sách 7 dòng hiện rõ, vẫn đăng nhập `#03` |
| [`../image/QLDX_05-C2-sau-moc-logout-goc.png`](../image/QLDX_05-C2-sau-moc-logout-goc.png) | Screenshot **viewport** lúc **02:28:27** = `t_logout_goc` **+93.9 s**. Đã Read xác nhận: **vẫn ở** `/chuyen-gia-tvv/danh-sach`, `h1 "Tư vấn viên / Chuyên gia"`, **không** bị đá về đăng nhập, **không** có modal, header vẫn `CB Nghiệp vụ - Trung ương #03`. ⚠️ **Trùng byte với ảnh "sau khi bấm"** — xem ghi chú md5 ngay dưới bảng |
| [`../image/QLDX_05-timeline.txt`](../image/QLDX_05-timeline.txt) | Mốc `t_baseline` · `t_logout_goc` · thời điểm modal bật · thời điểm bấm · `auth-last-activity` trước/sau bấm · bảng poll 3 phần (cửa sổ modal bật 250 ms, cửa sổ bấm 250 ms, poll toàn phép đo 15 s) · 8 điểm toàn vẹn phép đo |
| [`../image/QLDX_05-doi-chung-api.txt`](../image/QLDX_05-doi-chung-api.txt) | Mã HTTP thật của request đối chứng sau mốc gốc + dump 33/33 request xhr/fetch + phân tích request của chính cú bấm + mục "giới hạn của đối chứng" |
| [`../image/QLDX_05-doi-chung-api-response-body.network-response`](../image/QLDX_05-doi-chung-api-response-body.network-response) | Body đầy đủ của response đối chứng `reqid=282` |

> **⚠️ Công bố trước về md5 ảnh (chống nghi vấn "chụp lại cùng một file").**
> `d5ec792e372ab7471e83dd58259f4b96` — `QLDX_05-C1-truoc-khi-bam-gia-han.png`
> `05a1c72e2b1ba59f3a4076bb0128f2a5` — `QLDX_05-C1-sau-khi-bam-gia-han.png` (02:22:39)
> `05a1c72e2b1ba59f3a4076bb0128f2a5` — `QLDX_05-C2-sau-moc-logout-goc.png` (02:28:27)
>
> Hai ảnh sau **trùng byte hoàn toàn** (cùng md5, cùng 480612 bytes) dù chụp cách nhau **5 phút 48 giây**. Nguyên nhân: vùng nhìn thấy của trang **không có phần tử nào biến thiên theo thời gian** (bảng danh sách tĩnh 7 dòng, không có đồng hồ trên màn, badge thông báo giữ nguyên `56`). Việc trùng byte **chính là bằng chứng cho điều cần chứng minh**: giữa hai mốc đó không có auto-logout, không có modal bật lại, không đổi màn. Nhưng ảnh trùng byte **tự nó không neo được thời gian** — thời gian được neo bằng bảng poll 250 ms liên tục 02:21:23 → 02:30:13 trong `QLDX_05-timeline.txt` §5 và header `date` của máy chủ (`19:28:47 GMT` = 02:28:47 VN) trong `QLDX_05-doi-chung-api.txt`. Người kiểm chứng nên đọc hai nguồn đó, không dựa riêng vào ảnh.

## 8. Đề xuất verdict logic của case

> **Cần BA confirm** — không Pass, không Fail.

Cả 2 vế của QLDX_05 đều là **GAP** đã khóa ở Giai đoạn A: `srs-fr-10-quan-tri.md:1891` khai báo nút `[Gia han]` nhưng ô "Hành vi" để trống "—", và grep toàn thư mục SRS v3.5 chỉ ra **1 hit duy nhất** là dòng đó — không nơi nào quy định bấm gia hạn thì hệ thống phải làm gì. Vì vậy **không có mốc chuẩn để Pass**, kể cả khi hiện trạng app **khớp y từng chữ** expected của đối tác ở cả 2 vế (hộp thoại đóng ≤ 0.39 s; đồng hồ idle đặt lại về 0 ⇒ trần 30 phút, và phiên còn hiệu lực server-side sau mốc auto-logout gốc). Việc cần làm là **BA bổ sung đặc tả** theo **Q4** (a/b/c/d), không phải chặn bàn giao.

**Về nghiệp vụ:** khiếu nại gốc của đối tác ở case này **không tái hiện** — app làm đúng điều đối tác mong đợi.

**Giới hạn hiệu lực:** số đo này chỉ có hiệu lực cho **bản dựng nội bộ** `index-DsMHK7Dp.js` trên `18.143.165.120.nip.io`. Đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn` ⇒ cần đo lại khi bản dựng lên env đối tác, hoặc dev deploy lại. Điểm (d) của Q4 (giới hạn số lần gia hạn liên tiếp) **chưa đo** vì kỷ luật không mở rộng case.
