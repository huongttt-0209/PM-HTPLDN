# QLDX_06 — Xác nhận "Đăng xuất" trên hộp thoại cảnh báo hết phiên (đo Giai đoạn B)

**Case:** QLDX_06 · dòng 166 · tab `bug`
**Chuẩn chấm đã khóa:** [`../chuan/QLDX_04-05-06.md`](../chuan/QLDX_04-05-06.md) §2 (QLDX_06) — Giai đoạn B **không đổi** quan hệ MATCH/DIFF/GAP, **không mở rộng** phép đo, **không ghi Google Sheet**.
**Nguồn chuẩn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (số dòng do Giai đoạn A mở đọc trực tiếp).

> 🔴 **Expected đối tác có 2 nhánh ("hoặc") → đã đo RIÊNG trên 2 phiên độc lập, không gộp verdict** (đúng Bẫy đo #6 của chuẩn chấm).

---

## 1. Điều kiện đo

| Hạng mục | Giá trị thực |
|---|---|
| **Tài khoản thực dùng** | **`cbnv_tw_03` / `Test@1234`** — đúng bộ `_03` theo prompt. **Không phải fallback**: cả 4 lần đăng nhập đều thành công ngay lần đầu, không gặp lock, không dùng sibling `_04`/`_05`. **Không dùng `admin`.** |
| Danh tính hiển thị | "CB Nghiệp vụ - Trung ương #03" · "Cán bộ Nghiệp vụ Trung ương" · `BTP · TW` |
| Danh tính trong JWT | `sub=9b557200-be4b-46ac-b84b-fe6c154dc65f` · `vaiTro=["CB_NV_TW"]` · `capDonVi="TW"` · `authMethod="LOCAL"` · `idleTtl=1800` (=30 phút) |
| Cách đăng nhập | UI thật: mật khẩu → OTP 6 số lấy ở MailHog `http://18.143.165.120:8025`, lọc đúng mailbox `cbnv_tw_03@htpldn.test` (`limit=5`). Mã dùng: `235196` (02:41:24) · `509887` (02:46:18) · `742741` (02:52:49) · `851223` (03:02:59) |
| **Env** | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (không phải env nghiệm thu đối tác `htpldn-uat.ospgroup.vn`) |
| **🔴 Bó mã FE** | **`assets/index-D4Buvu4S.js`** · `assets/index-DVlgOkLg.css` + `assets/index-DNsk8fKL.css` — đọc trực tiếp từ DOM lúc 02:40:27. **KHÁC [`../BAN-DUNG.md`](../BAN-DUNG.md)** — xem §2 |
| Phiên bản app | sidebar hiện `HTPLDN · V1.0.9` |
| **Thời điểm đo** | 2026-08-07, giờ VN: 02:40:27 → 03:04:49 (4 lần đo, xem §3) |
| Trang được tải mới | Có — tải lại `/login` trước mỗi lần đo, không dùng tab mở sẵn giữ mã cũ |
| `Ghi nhớ đăng nhập` | **KHÔNG tick** — verify `checked=false` ngay trước mỗi lần submit (`srs-fr-10-quan-tri.md:1884` ghi checkbox này "Extend session TTL" → tick vào là lệch mốc đo) |
| Số tab dùng phiên | 1 (tab `about:blank` của profile `--isolated` không dùng phiên) |
| Rate-limit | 4 lần đăng nhập cách nhau ≥4 phút → không chạm rate-limit 5 lần/60 s |

## 2. 🔴 Bó mã FE đã đổi GIỮA lô F5 — giới hạn hiệu lực của verdict

| | Bó mã | etag `GET /` | last-modified |
|---|---|---|---|
| [`../BAN-DUNG.md`](../BAN-DUNG.md) (đo 02:03:49) | `index-DsMHK7Dp.js` | `"6a74d7ad-428"` | 01:51:25 VN |
| **QLDX_06 (đo 02:40:36)** | **`index-D4Buvu4S.js`** | **`W/"6a74df15-428"`** | **02:23:01 VN** |

Dev **deploy lại FE lúc 02:23:01 giờ VN**, tức **sau** khi QLDX_04 đo xong (02:09:38) và **giữa** khoảng đo của QLDX_05 (02:19:39 → 02:30:13 — QLDX_05 giữ tab đã tải nên vẫn chạy mã cũ). Vì vậy:

- **QLDX_06 là case duy nhất trong lô F5 đo trên bó mã `index-D4Buvu4S.js`.** Verdict dưới đây chỉ có hiệu lực cho bó mã này.
- Tiền đề mốc 25′ mượn từ QLDX_04/QLDX_05 vẫn hợp lệ vì đã **tái lập được 3/3 lần** trên bó mã mới (idle 25.008′ · 25.008′ · 25.017′).
- Ghi nhận phụ (không phải bug, ghi để tester sau khỏi mất thời gian): bó mã mới **bỏ placeholder** ở input login, chỉ còn label `Tên đăng nhập *` / `Mật khẩu *`. Selector cũ `input[placeholder="Nhập tên đăng nhập"]` (CLAUDE.md §Rule 11) **không còn match** → dùng `wait_for(["Tên đăng nhập"])`.

## 3. Tiền đề đã dựng + 4 lần đo

**Màn đang mở khi dựng mốc (cả 4 lần):** `/chuyen-gia-tvv/danh-sach` — "Tư vấn viên / Chuyên gia", bảng 7 dòng. Đã **chủ động rời `/dashboard`** bằng click sidebar (không `navigate_page`) vì Dashboard tự làm mới 60 giây (`srs-fr-01-dashboard.md:49`) — đúng Bẫy đo #3.

**Tiền đề dùng lại, KHÔNG đo lại:** [`QLDX_04.md`](QLDX_04.md) §3 C1 (mốc bật modal = idle 25.0′) và [`QLDX_05.md`](QLDX_05.md) §2 (cách dựng mốc idle). Modal tái lập đúng ở cả 4 lần → tiền đề còn hiệu lực trên bó mã mới.

**Cách quan sát:** bộ ghi `setInterval` 250 ms **thuần đọc DOM + đọc localStorage**. Không dispatch `mousemove`/`click`/`keydown`/`scroll`/`touchstart`; không reload; không navigate sau khi đặt mốc; poll ngoài bằng `evaluate_script` (đọc không reset mốc).

| Lần | Nhánh | `t_baseline` | Modal bật (idle) | Sự kiện chính | Vai trò |
|---|---|---|---|---|---|
| **A** | 1 | 02:18:20.009 | 02:43:20.510 (25.008′) | bấm [Đăng xuất] 02:43:45 | ❌ **HUỶ** làm bằng chứng thông báo (bộ bắt không attach được) — giữ làm đối chiếu |
| **B** | 1 | 02:24:07.375 | 02:49:07.877 (25.008′) | bấm [Đăng xuất] 02:49:37.177 | ✅ **chính thức cho C1a + C1b** |
| **C** | 2 | 02:28:54.888 | 02:53:55.390 (25.008′) | **tự đăng xuất 02:58:55** (đồng hồ thật chạy đủ 5 phút) | ✅ **chính thức cho C2a** |
| **D** | 2 | 02:38:59.006 | 03:04:00.007 (25.017′) | ép mốc 03:04:28.144 → tự đăng xuất ~03:04:29 | ✅ **chính thức cho C2b + C2c** (lấy nguyên văn thông báo) |

**Vì sao phải có lần D:** ở lần C, vòng round-trip giữa 2 lệnh MCP (~11–16 s) **dài hơn tuổi thọ thông báo** (đo được ∈ [6 s, 13 s]) nên không bắt được chuỗi. Không được kết luận "không có thông báo" từ lần C — đó đúng là Bẫy đo #4 (toast tự tắt → "im lặng giả"). Chuẩn chấm §3 cho phép `"không thao tác cho tới phút 30 (hoặc ép mốc idle)"` → lần D ép mốc để thời điểm tự đăng xuất rơi vào cửa sổ chụp ảnh. **Lần D đi đúng đường idle-watcher như lần C, không bấm nút nào; và lần D KHÔNG dùng để chấm C2a.**

**Vì sao huỷ lần A:** cú bấm [Đăng xuất] gây **hard reload** (biến trong trang mất, `window.name` bị xoá, `localStorage` bị clear) **và** bộ bắt thông báo khi đó không attach được (`MutationObserver.observe` ném `parameter 1 is not of type 'Node'` vì `document.documentElement` còn null ở document-start). Phát hiện bằng **self-test** (chèn node giả) → làm lại lần B với kênh `console` preserved. Self-test bộ bắt PASS ở 02:47:58 (lần B) và 02:52:30 (lần C/D).

## 4. Bảng kết quả theo từng vế

| Vế | Quan hệ (đã khóa) | Số đo / chuỗi thật quan sát được | Kết quả | Artifact |
|---|---|---|---|---|
| **C1a** — bấm [Đăng xuất] trên hộp thoại → chuyển về trang đăng nhập | **MATCH → TEST** | Bấm 02:49:37.177 (idle ≈25.49′, **phiên chưa hết hạn**) → `location.href` = `https://18.143.165.120.nip.io/login`; `wait_for(["Tên đăng nhập"])` **tìm thấy** form đăng nhập; `POST /api/v1/auth/logout` **200**, máy chủ hết hạn **cả 2 cookie**; đối chứng `/api/v1/auth/me` = **401** | ✅ **PASS** | `QLDX_06-C1a-truoc-khi-bam-dang-xuat.png` · `QLDX_06-C1a-sau-khi-bam-ve-login.png` · `QLDX_06-doi-chung-api.txt` |
| **C1b** — nhánh bấm nút kèm câu "Phiên làm việc đã hết hạn do không có thao tác" | **DIFF → BA** | Ghi lại: app hiện **1** thông báo, kiểu **success** (xanh lá): `Đăng xuất thành công`. Bộ bắt trên trang gốc: **0** emission sau cú bấm ⇒ không có toast trên trang gốc, không double-toast | — *(cấm chấm; chuyển BA)* | `QLDX_06-thongbao.txt` · `QLDX_06-C1a-sau-khi-bam-ve-login.png` |
| **C2a** — để idle tới phút 30 → tự đăng xuất + về trang đăng nhập | **MATCH → TEST** | `t_logout_goc` = 02:58:54.888. Mẫu sống cuối 02:58:55.142 (idle **30.004′**, vẫn ở màn danh sách) → document bị huỷ. `POST /api/v1/auth/logout` **200**, server `date` = **02:58:55** ⇒ **lệch dưới 1 giây**. Trang đích `/login`, có form đăng nhập. Đối chứng `/auth/me` = **401** | ✅ **PASS** | `QLDX_06-C2a-modal-truoc-moc-30.png` · `QLDX_06-C2-sau-tu-dang-xuat.png` · `QLDX_06-timeline.txt` §Lần đo C · `QLDX_06-doi-chung-api.txt` |
| **C2b** — trang đăng nhập có thông báo cho biết phiên đã hết hạn (lõi nghĩa) | **MATCH → TEST** | Có. App hiện **1** thông báo, kiểu **info** (xanh dương, icon "i"): `Phiên làm việc đã hết hạn do không có thao tác` — truyền đạt đúng lõi nghĩa "phiên đã hết hạn". Severity nhẹ (info) **vẫn khớp** `srs-fr-10-quan-tri.md:964` (ERR-DN-07 severity = **INFO**) | ✅ **PASS** | `QLDX_06-C2b-thongbao-idle-cap2.png` · `QLDX_06-thongbao.txt` |
| **C2c** — đúng y chuỗi "…do không có thao tác" | **DIFF/MÂU THUẪN → BA** | Ghi lại: chuỗi thật = `Phiên làm việc đã hết hạn do không có thao tác` — **trùng khớp từng ký tự** với expected đối tác. Nhưng **không** chuỗi nào trong SRS v3.5 chứa cụm "do không có thao tác" (4 biến thể ở `:964`, `:1011`, `srs-fr-05:1593`, `srs-fr-02:1135`) | — *(cấm chấm; chuyển BA)* | `QLDX_06-thongbao.txt` |

**Tổng: 3/3 vế route TEST (C1a · C2a · C2b) đều PASS. 2 vế route BA (C1b, C2c) chỉ ghi nhận, không chấm.**

### Ghi chú C1b — đây là chỗ FAIL-oan lớn nhất của case, đã chặn

Chuẩn chấm §4 ghi rõ: *"🔴 Cấm Fail QLDX_06 nhánh bấm nút vì thông báo ghi 'Đăng xuất thành công'."* Số đo xác nhận đúng tình huống đó:

- Thời điểm bấm 02:49:37.177, mốc thao tác cuối 02:24:07.375 ⇒ **idle ≈ 25.49′**, còn ~4.5 phút nữa mới tới mốc hết hạn 30′. **Phiên VẪN CÒN HIỆU LỰC** khi bấm (chứng minh xuôi: request nền `reqid=645 /thong-baos/unread-count` ngay trước cú bấm trả **304** kèm cookie).
- Theo `srs-fr-10-quan-tri.md:1958` đây là **"Dang xuat chu dong"** (phân biệt với "Dang xuat tu dong" ở `:1959`), và `:1011` cho message của FR-VIII-21 là **"Đăng xuất thành công" / "Phiên hết hạn"**.
- ⇒ App báo "Đăng xuất thành công" là **đúng bản chất trạng thái và đúng SRS**. Expected đối tác đòi "đã hết hạn do không có thao tác" cho **cả** nhánh bấm nút là **trái bản chất trạng thái** → route BA (**Q5**), **không** route bug.

### Ghi chú C2c — cấm Fail vì lệch câu chữ, cấm Pass vì SRS không có chuỗi này

App hiện **đúng y từng ký tự** chuỗi đối tác kỳ vọng. Nhưng theo chuẩn chấm §4 "Chặn PASS-oan": chuỗi đó **không có trong SRS v3.5** → vẫn phải chuyển BA bổ sung đặc tả (**Q2**), không được Pass. Đồng thời **cấm Fail** vì lệch câu chữ. Cách sửa đúng là **bổ sung / đồng bộ đặc tả**, không phải chặn bàn giao.

## 5. Chuỗi thông báo thật của từng nhánh (nguyên văn, cho orchestrator viết câu CẦN BA CONFIRM)

**Nhánh 1 — bấm [Đăng xuất] trên hộp thoại** (1 thông báo, kiểu success/xanh lá, mốc giờ 02:49:43):

```
Đăng xuất thành công
```

**Nhánh 2 — để idle tới phút 30** (1 thông báo, kiểu info/xanh dương, mốc giờ 03:04:33):

```
Phiên làm việc đã hết hạn do không có thao tác
```

**Hộp thoại cảnh báo ở phút 25** (tái lập trên bó mã mới, giống hệt QLDX_04):

```
Phiên làm việc sắp hết hạn
Phiên làm việc sắp hết hạn trong 5 phút do không có thao tác. Vui lòng gia hạn để tiếp tục làm việc.
Phiên sẽ tự đăng xuất sau 4:44.
[Đăng xuất]  [Gia hạn phiên]
```

**Đối chiếu với expected đối tác — GHI LẠI, không chấm:**

| Nhánh | Expected đối tác | App thật (`index-D4Buvu4S.js`) | So sánh |
|---|---|---|---|
| Bấm [Đăng xuất] | `Phiên làm việc đã hết hạn do không có thao tác` | `Đăng xuất thành công` | **LỆCH** — nhưng app đúng SRS `:1011` + `:1958` (phiên chưa hết hạn) → BA Q5 |
| Idle tới phút 30 | `Phiên làm việc đã hết hạn do không có thao tác` | `Phiên làm việc đã hết hạn do không có thao tác` | **trùng từng ký tự** |

**Số lượng thông báo + phương pháp đọc:** mỗi nhánh **đúng 1** thông báo. Đọc bằ`innerText` của phần tử (**không** `textContent`), bộ bắt **không lọc trùng**, mỗi bản ghi có `elemId` riêng cho từng phần tử DOM + mốc giờ ms + cờ `vis`. Ví dụ chống đếm nhầm: hộp thoại cảnh báo lúc 02:49:07.769 sinh **2 bản ghi cùng mốc giờ ms** (`E6` wrapper `vis=true` + `E7` `.ant-modal` `vis=false`) — đó là **1 hộp thoại**, không phải 2 thông báo. Chi tiết + giới hạn phép đo: `QLDX_06-thongbao.txt`.

**Đối chứng phụ từ chính bó mã FE** (chỉ là manh mối, không dùng làm verdict): grep `index-D4Buvu4S.js` ra bảng ánh xạ lý do đăng xuất → thông báo, truyền qua `sessionStorage["logout-notice"]`: `user` → "Đăng xuất thành công" (success) · `idle` → "Phiên làm việc đã hết hạn do không có thao tác" (info) · `expired` → "Phiên làm việc hết hạn" (info); nút cancel của hộp thoại gọi `logout("user")`. Khớp hoàn toàn với 2 chuỗi đã đo live.

## 6. Đối chứng độc lập (đúng MỘT đường / nhánh)

`fetch('/api/v1/auth/me', {credentials:'include', cache:'no-store'})` gọi **từ trong trang** vì `access_token` là cookie **HttpOnly** (`document.cookie` đọc ra **rỗng**).

| Nhánh | Thời điểm gọi | Server `date` | **Mã HTTP thật** | Body |
|---|---|---|---|---|
| **1** (lần B) | 02:50:14 | `Thu, 06 Aug 2026 19:50:14 GMT` | **401** | `ERR-AUTH-SYS-00-01` "Yêu cầu đăng nhập (thiếu token xác thực)" |
| **2** (lần C) | 03:00:15 (= mốc 30′ + 80 s) | `Thu, 06 Aug 2026 20:00:15 GMT` | **401** | `ERR-AUTH-SYS-00-01` (requestId `6ad26431-…`) |

⇒ **401, không phải 200** ở cả 2 nhánh ⇒ sau khi về `/login`, máy chủ **không còn coi phiên là hợp lệ**. Không phải FE chỉ đổi màn hình.

> **Giới hạn của đối chứng — ghi rõ để không suy quá số đo.** Mã lỗi trả về là `ERR-AUTH-SYS-00-01` **"thiếu token xác thực"**, nên 401 này chứng minh **cookie đã bị xoá** (không còn token để gửi lên), **không tự nó** chứng minh JWT đã vào **danh sách đen** theo `srs-fr-10-quan-tri.md:1001` — vì không còn token nào được gửi để máy chủ có cơ hội trả lỗi "token bị thu hồi". Bằng chứng phía máy chủ cho việc huỷ phiên nằm ở **response của chính cú logout**: `POST /api/v1/auth/logout` trả **200** kèm `Set-Cookie` hết hạn **cả** `access_token` **và** `refresh_token` (`Expires=Thu, 01 Jan 1970`).

**Chặn bẫy "tự đăng xuất do đồng hồ" vs "bị đá do 401 từ máy chủ"** (bẫy quan trọng nhất của nhánh 2): dump **28/28** request xhr+fetch của lần C — **toàn bộ 11 request nền** `/thong-baos/unread-count` trong 5 phút chờ đều **304** (có cookie, còn hiệu lực), **không có bất kỳ 401 nào** trước `reqid=798 POST /auth/logout [200]`. Thống kê: `401 × 3` (1 probe trước đăng nhập + 1 probe của trang `/login` mới + 1 cú đối chứng của QA) · `200 × 5` · `304 × 20` · **0 lỗi 5xx · 0 lỗi 4xx khác**. ⇒ Đây là **tự đăng xuất do đồng hồ idle**, không phải bị đá do 401.

Đồng thời loại trừ **Bẫy đo #3**: poll nền chạy đều ~30 s/lần suốt 5 phút mà `auth-last-activity` **không hề bị ghi lại** (mốc còn nguyên = 1 ở **100%** mẫu; sau khi bị đá về `/login`, giá trị **vẫn đúng** baseline `02:28:54.888`) ⇒ FE tính idle theo **sự kiện người dùng**, không theo hoạt động mạng.

**Không gặp `chrome-error://chromewebdata`:** URL sau khi chuyển ở cả 2 nhánh đều là `https://18.143.165.120.nip.io/login`, trang đích render đủ form và gọi được `/api/v1/auth/me` tới máy chủ (401 thật, có body JSON, có header `date` của nginx) ⇒ không phải triệu chứng rớt mạng giả dạng tự đăng xuất.

## 7. Bug mới

**Không có.** Trong đúng các bước bắt buộc của 2 vế đang verify (đăng nhập → sang màn danh sách → dựng mốc idle → chờ modal → bấm [Đăng xuất] **hoặc** để idle tới phút 30 → đọc trang đích → đối chứng API), không có 4xx/5xx nào tự lộ ra. Console (sau khi lọc bỏ message do chính QA chèn) chỉ còn `401` của cú probe `/api/v1/auth/me` trên trang `/login` khi chưa có token — hành vi bình thường, không phải lỗi. **0 lỗi 5xx, 0 TypeError của app.**

**Bug candidate:** không có.

**Ghi nhận không phải bug (để tester sau khỏi mất thời gian):** bó mã `index-D4Buvu4S.js` bỏ placeholder ở input login → selector `input[placeholder="Nhập tên đăng nhập"]` trong CLAUDE.md §Rule 11 không còn match; dùng `wait_for(["Tên đăng nhập"])`. Đây là thay đổi UI của bản dựng mới, không nằm trong 2 vế đang verify nên **không mở rộng case để điều tra**.

## 8. Artifact

| File | Nội dung |
|---|---|
| [`../image/QLDX_06-C1a-truoc-khi-bam-dang-xuat.png`](../image/QLDX_06-C1a-truoc-khi-bam-dang-xuat.png) | Screenshot **viewport** 02:49:24, ngay trước khi bấm. Đã mở lại bằng Read xác nhận: hộp thoại "Phiên làm việc sắp hết hạn", đủ chuỗi thông báo, đồng hồ `4:44`, đúng 2 nút `[Đăng xuất] [Gia hạn phiên]`, account `#03`, `V1.0.9`, đang ở màn Tư vấn viên / Chuyên gia |
| [`../image/QLDX_06-C1a-sau-khi-bam-ve-login.png`](../image/QLDX_06-C1a-sau-khi-bam-ve-login.png) | Screenshot **viewport** 02:49:43 (+6 s sau cú bấm). Đã Read xác nhận: đã ở trang đăng nhập, có form `Tên đăng nhập`/`Mật khẩu`, và **1 thông báo xanh lá "Đăng xuất thành công"** |
| [`../image/QLDX_06-C2a-modal-truoc-moc-30.png`](../image/QLDX_06-C2a-modal-truoc-moc-30.png) | Screenshot **viewport** 02:54:09, trước mốc 30′ của lần đo C. Đã Read xác nhận: hộp thoại cảnh báo, đồng hồ `4:46`, 2 nút, account `#03`, đang ở màn danh sách |
| [`../image/QLDX_06-C2-sau-tu-dang-xuat.png`](../image/QLDX_06-C2-sau-tu-dang-xuat.png) | Screenshot **viewport** 03:00:09 = mốc 30′ **+ 74 s** (lần đo C). Đã Read xác nhận: đã ở `/login`, có form đăng nhập, **không** còn thông báo (đã tự tắt) — nên C2b lấy chuỗi từ lần đo D |
| [`../image/QLDX_06-C2b-thongbao-idle-cap1.png`](../image/QLDX_06-C2b-thongbao-idle-cap1.png) | Screenshot **viewport** 03:04:28 (lần D, ngay trước thời điểm ép mốc). Đã Read xác nhận: hộp thoại cảnh báo, đồng hồ `4:32`, 2 nút |
| [`../image/QLDX_06-C2b-thongbao-idle-cap2.png`](../image/QLDX_06-C2b-thongbao-idle-cap2.png) | Screenshot **viewport** 03:04:33 = tự đăng xuất **+ ~4 s** (lần D). Đã Read xác nhận: đã ở `/login`, và **1 thông báo xanh dương (info) "Phiên làm việc đã hết hạn do không có thao tác"** |
| [`../image/QLDX_06-timeline.txt`](../image/QLDX_06-timeline.txt) | 2 nhánh × 4 lần đo: bó mã FE, `t_baseline`, `t_logout_goc`, thời điểm modal bật (kẹp 250 ms), thời điểm bấm / thời điểm tự chuyển, **bảng poll quanh mốc 30′**, md5 + mốc giờ 6 ảnh, 7 điểm toàn vẹn phép đo |
| [`../image/QLDX_06-thongbao.txt`](../image/QLDX_06-thongbao.txt) | Nguyên văn **mọi** thông báo bắt được ở **cả hai** nhánh + số lượng + mốc giờ từng cái + phương pháp đọc (innerText, không lọc trùng, self-test bộ bắt) + giới hạn phép đo + đối chứng phụ từ bó mã FE |
| [`../image/QLDX_06-doi-chung-api.txt`](../image/QLDX_06-doi-chung-api.txt) | Mã HTTP thật của **2** lần đối chứng + dump request liên quan + header `Set-Cookie` của cú logout + **kết luận không có 401 nào trước lúc chuyển trang** ở cả 2 nhánh + phân tích console |

> **md5 6 ảnh (chống nghi vấn "chụp lại cùng một file") — 6 md5 KHÁC NHAU:**
> `4aa4e74c0a956004b26e8dffdac6795f` — `QLDX_06-C1a-truoc-khi-bam-dang-xuat.png` (02:49:24)
> `30d900c265eadf676e4eda089d6ad557` — `QLDX_06-C1a-sau-khi-bam-ve-login.png` (02:49:43)
> `431a7979e80b68179c91f6a69d64f9c9` — `QLDX_06-C2a-modal-truoc-moc-30.png` (02:54:09)
> `95231a4d33224e7c4e5e77f66c16ebb0` — `QLDX_06-C2-sau-tu-dang-xuat.png` (03:00:09)
> `1e2145c15cadcc7c6af5687c81bf9223` — `QLDX_06-C2b-thongbao-idle-cap1.png` (03:04:28)
> `40987d74712fa5d8eedd50ebe33dab14` — `QLDX_06-C2b-thongbao-idle-cap2.png` (03:04:33)
>
> Hai ảnh trang `/login` của 2 nhánh **không trùng byte**: một ảnh có thông báo xanh lá "Đăng xuất thành công", ảnh kia không còn thông báo (chụp +74 s). Thời gian được neo bằng **bảng poll 250 ms** trong `QLDX_06-timeline.txt` và **header `date` của máy chủ** trong `QLDX_06-doi-chung-api.txt` — người kiểm chứng nên đọc hai nguồn đó, không dựa riêng vào ảnh.

## 9. Blocker

**Không có blocker.** Cả 2 nhánh đo được trọn vẹn. Hai khó khăn kỹ thuật đã tự giải quyết và ghi rõ phương pháp: (a) hard reload xoá log bộ bắt → chuyển sang kênh `console` preserved + self-test bộ bắt; (b) round-trip MCP dài hơn tuổi thọ thông báo → thêm lần đo D ép mốc để thời điểm tự đăng xuất rơi vào cửa sổ chụp ảnh.

## 10. Đề xuất verdict logic của case

> **Pass** — kèm thành phần **Cần BA confirm** (bổ sung đặc tả câu chữ, không chặn bàn giao).

Cả 3 vế route TEST đều PASS trên bó mã `index-D4Buvu4S.js`: **C1a** bấm [Đăng xuất] → về trang đăng nhập và phiên bị huỷ thật ở máy chủ (401, máy chủ hết hạn cả 2 cookie); **C2a** để idle tới phút 30 → tự đăng xuất **lệch dưới 1 giây** so với mốc 30′, và đã loại trừ khả năng "bị đá do 401" (toàn bộ 11 request nền trước đó đều 304); **C2b** trang đăng nhập có thông báo truyền đạt đúng lõi nghĩa phiên đã hết hạn, severity info — vẫn khớp `srs-fr-10-quan-tri.md:964` (ERR-DN-07 = INFO). Ở nhánh idle, chuỗi thông báo thật còn **trùng khớp từng ký tự** với expected đối tác ⇒ **về nghiệp vụ, khiếu nại gốc của đối tác ở case này không tái hiện**.

Phần **Cần BA** chỉ là bổ sung đặc tả cho 2 vế DIFF đã khóa ở Giai đoạn A:
- **Q5 (C1b):** nhánh người dùng **chủ động** bấm [Đăng xuất] trên hộp thoại cảnh báo (phút 25, phiên **chưa** hết hạn) dùng thông báo nào. App đang báo "Đăng xuất thành công" — đúng `:1011` + `:1958`; đối tác kỳ vọng "đã hết hạn do không có thao tác" cho cả nhánh này, trái bản chất trạng thái. **QA không chấm Fail nhánh này.**
- **Q2 (C2c):** SRS có 4 chuỗi khác nhau cho "phiên hết hạn" (`:964`, `:1011`, `srs-fr-05-vu-viec.md:1593`, `srs-fr-02-hoi-dap.md:1135`) và **không** chuỗi nào chứa cụm "do không có thao tác" mà app đang hiển thị. Nhờ BA chốt: (a) có yêu cầu đúng nguyên văn hay chỉ đúng nghĩa; (b) nếu đúng nguyên văn thì chốt 1 chuỗi và đồng bộ 4 vị trí trên.

**Giới hạn hiệu lực:** đây là **Pass cho bản dựng nội bộ `index-D4Buvu4S.js`** (deploy 02:23:01 VN) trên `18.143.165.120.nip.io` — **bó mã MỚI HƠN bó mã ghi ở [`../BAN-DUNG.md`](../BAN-DUNG.md)**, xem §2. Đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn` ⇒ cần đo lại khi bản dựng lên env đối tác, hoặc dev deploy lại.
