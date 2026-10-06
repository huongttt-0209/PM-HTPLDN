# QLDX_04 — Kiểm tra Hộp thoại cảnh báo sắp hết phiên (đo Giai đoạn B)

**Case:** QLDX_04 · dòng 164 · tab `bug`
**Chuẩn chấm đã khóa:** [`../chuan/QLDX_04-05-06.md`](../chuan/QLDX_04-05-06.md) §2 (QLDX_04) — Giai đoạn B **không đổi** quan hệ MATCH/DIFF/GAP, **không mở rộng** phép đo.
**Nguồn chuẩn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (số dòng đã do Giai đoạn A mở đọc trực tiếp).

---

## 1. Điều kiện đo

| Hạng mục | Giá trị thực |
|---|---|
| **Tài khoản thực dùng** | **`cbnv_tw_03` / `Test@1234`** — đúng bộ `_03` theo prompt. **Không phải fallback**: đăng nhập thành công ngay lần đầu, không gặp lock, không dùng sibling `_04`/`_05`. **Không dùng `admin`.** |
| Danh tính hiển thị | "CB Nghiệp vụ - Trung ương #03" · "Cán bộ Nghiệp vụ Trung ương" · `BTP · TW` |
| Danh tính trong JWT | `vaiTro=["CB_NV_TW"]` · `capDonVi="TW"` · `authMethod="LOCAL"` · `idleTtl=1800` (=30 phút) |
| Cách đăng nhập | UI thật: mật khẩu → OTP 6 số lấy ở MailHog `http://18.143.165.120:8025`, lọc đúng mailbox `cbnv_tw_03@htpldn.test` (`limit=5`, mã `393168` tạo lúc 02:06:41) |
| **Env** | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (không phải env nghiệm thu đối tác `htpldn-uat.ospgroup.vn`) |
| **Bó mã FE** | `assets/index-DsMHK7Dp.js` · `assets/index-DVlgOkLg.css` — đọc trực tiếp từ DOM lúc 02:06:27, **khớp** [`../BAN-DUNG.md`](../BAN-DUNG.md) |
| Phiên bản app | sidebar hiện `HTPLDN · V1.0.9` |
| **Thời điểm đo** | 2026-08-07, giờ VN: tải trang 02:06:27 · đăng nhập xong 02:06:57 · dựng mốc 02:07:57 · **modal bật 02:08:28** · đọc lại 02:09:38 |
| Trang được tải mới | Có — tải lại `/login` lúc 02:06:27 rồi mới đo (không dùng tab mở sẵn giữ mã cũ) |
| `Ghi nhớ đăng nhập` | **KHÔNG tick** — đã verify `rememberChecked=false` ngay trước khi submit (theo `srs-fr-10-quan-tri.md:1884` tick vào là "Extend session TTL" → lệch mốc) |
| Số tab dùng phiên | 1 (tab `about:blank` của profile `--isolated` không dùng phiên) |

## 2. Tiền đề đã dựng

**Màn đang mở khi dựng mốc:** `/chuyen-gia-tvv/danh-sach` — "Tư vấn viên / Chuyên gia", bảng 7 dòng.
Đã **chủ động rời `/dashboard`** bằng click sidebar (không `navigate_page`) vì Dashboard tự làm mới 60 giây (`srs-fr-01-dashboard.md:49`) — đúng cảnh báo "Bẫy đo #3" của chuẩn chấm.

**Baseline đặt:**

| | Giá trị |
|---|---|
| `t0` (lúc đặt mốc) | 02:07:57 giờ VN — `Date.now() = 1786043277550` |
| Ghi vào `localStorage["auth-last-activity"]` | `1786041807550` = **01:43:27 giờ VN** = `t0 − 24.5 phút` |
| Mốc kỳ vọng modal bật | 02:08:27 (idle = 25.0′) |

**Cách quan sát:** recorder `setInterval` 250 ms **thuần đọc DOM + đọc localStorage**. Không dispatch `mousemove`/`click`/`keydown`/`scroll`; không reload; không navigate sau khi đặt mốc. Lấy chữ bằng **`innerText` của phần tử modal đang hiển thị** (lọc `getClientRects()` + `display`/`visibility`/`opacity` + `offsetParent|fixed`) — **không dùng `textContent`**.

**Kỷ luật case:** **không bấm nút nào** trên modal ("Gia hạn phiên" thuộc QLDX_05, "Đăng xuất" thuộc QLDX_06).

## 3. Bảng kết quả theo từng vế

| Vế | Quan hệ (đã khóa) | Số đo / chuỗi thật quan sát được | Kết quả | Artifact |
|---|---|---|---|---|
| **C1** — modal bật đúng mốc 25′ | **MATCH → TEST** | Kẹp giữa idle **24.988′ (chưa có)** và **25.017′ (đã có)** ⇒ bật tại **idle = 25.0 phút**, sai số < 2 s. `auth-last-activity` **không bị reset** suốt 49/49 mẫu | ✅ **PASS** | `QLDX_04-timeline-idle.txt` · `QLDX_04-C1-modal-canh-bao-phut-25.png` · `QLDX_04-doi-chung-network.txt` |
| **C2a** — lõi nghĩa "phiên sắp hết hạn trong 5 phút" | **MATCH → TEST** | Tiêu đề "Phiên làm việc sắp hết hạn"; thân bài có nguyên cụm **"sắp hết hạn trong 5 phút"**; kèm đồng hồ "Phiên sẽ tự đăng xuất sau 5:00" (chạy thật → 4:37 → 3:50) | ✅ **PASS** | `QLDX_04-C2-C3-C4-modal-innerText.txt` · ảnh C1 |
| **C2b** — đúng y nguyên chuỗi dài của đối tác | **DIFF → BA** | Ghi lại: app hiện **trùng khớp từng ký tự** với expected đối tác (xem §4). SRS `:1891` chỉ ghi chuỗi ngắn khác | — *(cấm chấm; chuyển BA)* | `QLDX_04-C2-C3-C4-modal-innerText.txt` |
| **C3a** — có hành động gia hạn phiên | **MATCH → TEST** | Có nút primary **"Gia hạn phiên"**, `disabled=false`, visible trong modal | ✅ **PASS** | `QLDX_04-C2-C3-C4-modal-innerText.txt` · ảnh C1 |
| **C3b** — nhãn đúng chữ "Gia hạn phiên" | **DIFF → BA** | Ghi lại: nhãn thật = **`Gia hạn phiên`** (trùng khớp từng ký tự với đối tác). SRS `:1891` ghi `[Gia han]` (không có chữ "phiên") | — *(cấm chấm; chuyển BA)* | `QLDX_04-C2-C3-C4-modal-innerText.txt` |
| **C4** — có nút Đăng xuất | **MATCH → TEST** | Có nút default **"Đăng xuất"**, `disabled=false`, visible trong modal. Tổng nút visible **trong modal = đúng 2** | ✅ **PASS** | `QLDX_04-C2-C3-C4-modal-innerText.txt` · ảnh C1 |

**Tổng: 4/4 vế route TEST đều PASS. 2 vế route BA chỉ ghi nhận, không chấm.**

### Ghi chú C1 và lệch nội bộ SRS

Số đo 25.0′ **khớp `srs-fr-10-quan-tri.md:1959`** ("25 phut idle → Modal canh bao → 30 phut → Auto invalidate") ⇒ **Pass C1** đúng theo caveat §4 của chuẩn chấm. Ô "Điều kiện hiển thị" ở `:1891` ghi "30 phut idle" là **lệch nội bộ SRS** (di sản v3, CHANGELOG không chạm row 12) → giữ nguyên câu hỏi housekeeping **Q1**, **không** dùng để Fail.

## 4. Chuỗi thông báo thật + nhãn nút thật (nguyên văn, cho orchestrator viết câu CẦN BA CONFIRM)

**Tiêu đề hộp thoại:**

```
Phiên làm việc sắp hết hạn
```

**Câu thông báo chính:**

```
Phiên làm việc sắp hết hạn trong 5 phút do không có thao tác. Vui lòng gia hạn để tiếp tục làm việc.
```

**Dòng phụ (đồng hồ đếm ngược, chạy thật):**

```
Phiên sẽ tự đăng xuất sau 5:00.
```

**Hai nhãn nút (đúng 2 nút visible trong modal, theo thứ tự trái → phải):**

```
Đăng xuất
Gia hạn phiên
```

**Đối chiếu với expected đối tác — GHI LẠI, không chấm:**

| | Expected đối tác | App thật (bó mã `index-DsMHK7Dp.js`) | So sánh |
|---|---|---|---|
| Thông báo | `Phiên làm việc sắp hết hạn trong 5 phút do không có thao tác. Vui lòng gia hạn để tiếp tục làm việc.` | y hệt | **trùng từng ký tự** |
| Nút gia hạn | `Gia hạn phiên` | `Gia hạn phiên` | **trùng từng ký tự** |
| Nút đăng xuất | `Đăng xuất` | `Đăng xuất` | **trùng từng ký tự** |

⚠️ **Dù trùng khớp y nguyên expected đối tác, C2b/C3b vẫn KHÔNG được chấm Pass** (chuẩn chấm §4 "Chặn PASS-oan"): chuỗi dài và chữ "phiên" trong nhãn **không có trong SRS v3.5** — `:1891` chỉ ghi `"Phien sap het han trong 5 phut."` và `[Gia han]`. Việc cần làm là **BA bổ sung / chốt đặc tả** (Q2, Q3), không phải chặn bàn giao.

**Dữ kiện bổ trợ cho Q6:** SRS v3.5 grep "đếm ngược / countdown" = 0 hit, nhưng app **có** đồng hồ đếm ngược. Không tính là lỗi; là dữ kiện để BA chốt Q6.

## 5. Đối chứng độc lập (đúng MỘT đường) — không có 401 tại thời điểm modal bật

`mcp__chrome-devtools__list_network_requests` (xhr + fetch + document, 19/19 request, không cắt trang): **401 × 1 · 200 × 14 · 304 × 4**, không 5xx, không 4xx khác.

- **401 duy nhất** = `reqid=18 GET /api/v1/auth/me` — `date: 19:05:51 GMT` = **02:05:51 VN**, `referer: /login`, body `ERR-AUTH-SYS-00-01` "Yêu cầu đăng nhập (thiếu token xác thực)". Đây là cú probe FE tự gọi khi vừa mở trang đăng nhập, **trước** `reqid=19 POST /auth/login [200]`, và **trước lúc modal bật 2 phút 37 giây**.
- **Chứng minh xuôi:** `reqid=115 GET /thong-baos/unread-count` — `date: 19:08:54 GMT` = **02:08:54 VN** (26 s **sau** khi modal bật) trả **304**, cookie `access_token` có mặt ⇒ lúc modal bật server **vẫn coi phiên hợp lệ**.
- Bracket quanh mốc bật: trước = `reqid=112/113/114` [304], sau = `reqid=115` [304] — **không có 401 nào**.

⇒ Modal quan sát được **đúng là modal (a)** — cảnh báo **chủ động** do đồng hồ idle phía FE bật, **không phải** modal (b) phản ứng HTTP 401 (`srs-fr-02-hoi-dap.md:1135`, tiêu đề "Phiên đăng nhập đã hết hạn"). **Bẫy đo #1 đã loại trừ, phép đo hợp lệ.**

⇒ Đồng thời loại trừ **Bẫy đo #3**: request nền `/thong-baos/unread-count` poll đều trong khoảng đo mà `auth-last-activity` **không hề bị ghi lại** (`lsEqualsBaseline = true` ở 49/49 mẫu) ⇒ FE tính idle theo **event người dùng**, không theo hoạt động mạng.

## 6. Bug mới

**Không có.** Trong đúng các bước bắt buộc của vế đang verify (đăng nhập → sang màn danh sách → dựng mốc idle → chờ modal → đọc modal), không có 4xx/5xx nào tự lộ ra; `list_console_messages` (error + warn) = **rỗng**. 401 duy nhất là hành vi bình thường của trang đăng nhập khi chưa có token (đã phân tích §5), không phải lỗi.

**Bug candidate:** không có.

**Quan sát tình cờ (KHÔNG phải số đo, ngoài phạm vi case này):** sau khi đã chụp đủ bằng chứng, tôi để đồng hồ chạy tiếp và **không bấm nút nào**. Đến lượt kiểm tra lúc ~02:13+ (idle đã vượt 30′) thì trang đã ở `/login` và biến recorder trong trang đã bị xoá ⇒ app **có** tự đăng xuất sau mốc 30′. **Không dùng làm số đo**: tôi không quan sát được đúng thời điểm chuyển, không bắt được thông báo trên trang đăng nhập, và cũng **không** kiểm 401 với cookie cũ. Vế "idle tới phút 30 → tự đăng xuất" thuộc **QLDX_06 C2a/C2b** — để agent của case đó đo và chấm.

## 7. Artifact

| File | Nội dung |
|---|---|
| [`../image/QLDX_04-C1-modal-canh-bao-phut-25.png`](../image/QLDX_04-C1-modal-canh-bao-phut-25.png) | Screenshot **viewport** lúc modal đang hiện (đã mở lại bằng Read xác nhận: modal, đủ chuỗi, 2 nút, đồng hồ `4:37`, account `#03`, `V1.0.9`, đang ở màn Tư vấn viên / Chuyên gia) |
| [`../image/QLDX_04-C2-C3-C4-modal-innerText.txt`](../image/QLDX_04-C2-C3-C4-modal-innerText.txt) | `innerText` nguyên văn của modal (2 lần đọc) + danh sách nhãn nút visible + phương pháp lọc visible |
| [`../image/QLDX_04-doi-chung-network.txt`](../image/QLDX_04-doi-chung-network.txt) | Dump 19/19 request + timestamp `reqid=18` và `reqid=115` + kết luận không có 401 tại mốc bật |
| [`../image/QLDX_04-timeline-idle.txt`](../image/QLDX_04-timeline-idle.txt) | Bảng 49 mẫu `{giờ thực, idle phút, modal hiện?, mốc còn nguyên?}` + 7 điểm toàn vẹn phép đo |

## 8. Đề xuất verdict logic của case

> **Pass** — kèm thành phần **Cần BA confirm** (housekeeping đặc tả, không chặn bàn giao).

Cả 4 vế route TEST (C1 mốc 25.0′ · C2a lõi nghĩa · C3a có hành động gia hạn · C4 có nút Đăng xuất) đều PASS trên bó mã `index-DsMHK7Dp.js`, và chuỗi thông báo lẫn hai nhãn nút thực tế **trùng khớp từng ký tự** với expected của đối tác ⇒ về nghiệp vụ, khiếu nại gốc của case đã được giải quyết. Phần **Cần BA** chỉ là **bổ sung đặc tả** cho hai vế DIFF đã khóa (C2b chuỗi dài, C3b chữ "phiên" trong nhãn — SRS `:1891` đang ghi khác) cộng housekeeping mốc 25′ vs 30′ ở `:1891` (Q1), theo caveat §4 thì cấm Pass hai vế này kể cả khi app khớp y đối tác.

**Giới hạn hiệu lực:** đây là **Pass cho bản dựng nội bộ** `index-DsMHK7Dp.js` trên `18.143.165.120.nip.io`. Đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn` ⇒ cần đo lại khi bản dựng lên env đối tác, hoặc dev deploy lại.
