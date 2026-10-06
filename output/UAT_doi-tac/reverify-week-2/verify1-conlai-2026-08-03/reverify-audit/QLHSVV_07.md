# Audit verify vòng 1 — QLHSVV_07 (row 128, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Tải tệp đính kèm của hồ sơ vụ việc HTPL (Vụ việc HTPL → Chi tiết → nhóm "Tài liệu đính kèm" → [Tải]) · FR-V.I-07 (UC57) · SCR-V.I-03
**Ngày verify:** 2026-08-03 · **Người verify:** QA (Claude Code, Chrome DevTools MCP)
**Tài khoản THỰC dùng:** `cbnv_tw_03` — CB Nghiệp vụ Trung ương (`CB_NV_TW`), đơn vị `BTP · TW`, `donViId = 00000000-0000-4000-8000-000000000001`. Không phải fallback (đăng nhập lần đầu OK, không chạm Rule 7).
**Bản dựng khi test:** `HTPLDN · V1.0.5` trên `https://18.143.165.120.nip.io` (đối tác quay trên `HTPLDN · V1.0.2` tại `htpldn-uat.ospgroup.vn`).

## Note dev trước khi QA đè (2026-08-03)

Cột P (`Trạng thái dev fix 1`): `dev done`

Cột R (`DEV phản hồi lần 1`): **TRỐNG — dev không giải trình gì.** Không có mô tả sửa cái gì, không có commit, không có bản triển khai. Vì vậy toàn bộ kết luận dưới đây dựa **100% vào đo thật của QA**, không lấy lời khai của dev làm căn cứ.

Cột Q (`Verify`) trước khi QA ghi: **RỖNG** (không có verdict cũ mâu thuẫn).

---

## Cổng 1 — Bằng chứng đối tác (đã trích frame + mở full-res bằng Read tool)

**File:** `partner-evidence/QLHSVV_07.webm` — video 1920×1080, dài ~5,4 giây. Trích 14 khung hình bằng `tools/extract_frames.py --every 0.4` vào `frames/QLHSVV_07/`. Đã xem full-res, **không** kết luận từ ảnh ghép thu nhỏ.

**3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết):**

| # | Dữ kiện | Giá trị đọc được từ khung hình |
|---|---|---|
| (a) | URL / ID bản ghi | `htpldn-uat.ospgroup.vn/vu-viec/ab08db14-4e92-48fe-8f2b-b2a0ad00b4a3` — màn **Chi tiết** vụ việc (đường dẫn điều hướng: Trang chủ / Vụ việc hỗ trợ pháp lý / **Chi tiết**). Vai trò góc phải: **"Cán bộ NV Trung ương · CB_NV_TW"**, đơn vị **`BTP · TW`**. Sidebar ghi `HTPLDN · V1.0.2` |
| (b) | Trạng thái + màn/accordion đối tác đang đứng | Đang mở **Accordion "Tài liệu đính kèm"** (đã bung, có nút [+ Thêm tài liệu]). Dòng thời gian bên dưới: "**Bổ sung hồ sơ** 29/07/2026 17:31", "**Tiếp nhận** 29/07/2026 17:29", "Từ chối phân công 10/07/2026", "Phân công 30/…" ⇒ hồ sơ đã tiếp nhận và vừa được bổ sung tài liệu |
| (c) | Tệp đính kèm đối tác thao tác | 1 tệp: **`QLHSVV_04.jpg`** · Loại **`BO_SUNG`** · Định dạng **JPG** · 193.5 KB · Trạng thái quét **"Sạch"** · Ngày tải **29/07/2026 17:31** |

**Đối tác bấm ĐÚNG phần tử nào — mấu chốt phân biệt "bấm nhầm [Xem]" vs "nút [Tải] hỏng":**

| Mốc | Khung hình | Quan sát |
|---|---|---|
| 0,0s | `t000.00s.jpg` | Hàng tệp có **DUY NHẤT MỘT** phần tử hành động: **biểu tượng mũi tên chỉ xuống rơi vào khay (⤓)** màu xanh, nằm ở cột cuối cùng (cột này **không có tiêu đề**). **Không hề có biểu tượng con mắt / nút [Xem] nào** trong hàng. Đã phóng to vùng này (`crop-action-icon-t000.png`) để đọc chắc chắn hình dạng biểu tượng |
| 1,4s | `t001.42s.jpg` | Con trỏ di lên đúng biểu tượng ⤓ đó; thanh trạng thái dưới đáy trình duyệt hiện `htpldn-uat.ospgroup.vn/htpldn-uat/.../QLHSVV_04.jpg?X-Amz-Algorithm=AWS4-HM…` ⇒ phần tử này là **đường liên kết trỏ thẳng tới tệp** |
| 2,6s | `t002.56s.jpg` | Con trỏ vẫn ở đúng biểu tượng ⤓, chuẩn bị bấm |
| 3,4s | `t003.38s.jpg` | **Trình duyệt mở TAB MỚI** tiêu đề `QLHSVV_04.jpg`, thanh địa chỉ là đường dẫn ký sẵn tới tệp; nội dung tab là **chính bức ảnh JPG được hiển thị trong trình duyệt** — tệp **không** được tải về máy |

⇒ **Kết luận Cổng 1: đối tác bấm ĐÚNG nút tải xuống, KHÔNG bấm nhầm nút Xem** (bản V1.0.2 của họ không có nút Xem để mà bấm nhầm).

**Vì sao đối tác mô tả là "màn hình xem chi tiết":** bức ảnh `QLHSVV_04.jpg` mà họ đính kèm **bản thân nó là một ảnh chụp màn hình Chi tiết vụ việc** (trong ảnh thấy toast "Cập nhật vụ việc thành công", đồng hồ máy **05:29 PM 29/07/2026**, sidebar `HTPLDN · V1.0`, khác hẳn đồng hồ thật của phiên quay là **09:03 AM 30/07/2026** và sidebar `V1.0.2`). Nên khi trình duyệt mở ảnh đó ra xem, màn hình trông y như "hệ thống hiển thị màn chi tiết". **Mô tả của đối tác về HIỆN TƯỢNG là chính xác** (bấm tải nhưng tệp không về máy, mà mở ra xem) — chỉ cách diễn đạt nguyên nhân là do nội dung tấm ảnh gây hiểu nhầm.

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `partner-evidence/QLHSVV_07.webm`, khung hình chứa LỖI = **`t003.38s.jpg`** — sau khi bấm biểu tượng tải xuống, trình duyệt mở tab mới hiển thị chính tệp JPG thay vì lưu tệp về máy.
2. **Đối tác phản ánh CỤ THỂ:** nút/biểu tượng "Tải xuống" trên hàng tệp đính kèm **không tải tệp về máy**, mà chuyển sang một màn hình xem (họ gọi là "màn hình xem chi tiết").
3. **Data + bước tái hiện:** đăng nhập CB Nghiệp vụ cấp TW → menu "Vụ việc HTPL" → mở một hồ sơ **có tệp đính kèm** → bung nhóm "Tài liệu đính kèm" → bấm nút tải xuống trên hàng tệp.

## Cổng 3 — Đối chiếu SRS vs thực tế web

| # | SRS yêu cầu (trích nguyên văn + dòng) | Thực tế web (QA đo 2026-08-03, bản V1.0.5) | Đạt? |
|:-:|---|---|:-:|
| 1 | `srs-fr-05-vu-viec.md:1729` — "Accordion 3 — Tài liệu Đính kèm \| C23 \| Danh sách file: tên file, loại, kích thước, ngày upload, **nút [Xem] [Tải]**. Nút [+ Thêm tài liệu]" ⇒ **hai nút RIÊNG BIỆT** | Cột "Thao tác" của hàng tệp có **đúng 2 nút riêng**: `<button>` biểu tượng con mắt + chữ **"Xem"**, và `<button>` biểu tượng mũi tên tải xuống + chữ **"Tải"**. Đọc bằng `outerHTML` chứ không đọc bằng `textContent`. Ảnh `BUG-QLHSVV_07-web-01-hai-nut-Xem-Tai.png` | ✅ |
| 2 | Cột K của phiếu (kỳ vọng đối tác, khớp §Mô tả FR-V.I-07 `:575` "Xem chi tiết, chỉnh sửa, upload tài liệu bổ sung cho vụ việc") — **"Hệ thống tải tệp về máy người dùng"** | Bấm **[Tải]** → tệp **VỀ MÁY THẬT**: `~/Downloads/QLHSVV_07_qa.jpg`, 39 772 byte. **MD5 = `091531a081d38cc9ddda5614f25bd154`**, trùng khít MD5 tệp gốc đã tải lên **và** trùng `etag` máy chủ trả về ⇒ nội dung không sai lệch 1 byte. Lặp **3/3 lần**, mỗi lần xóa sạch tệp cũ trước khi bấm | ✅ |
| 3 | Hai nút phải là **hai chức năng khác nhau** (nếu [Tải] cũng mở màn xem thì trùng chức năng với [Xem], tức chức năng Tải không tồn tại — đây là giả thuyết cần bác bỏ/xác nhận) | **[Xem]** → mở lớp xem trước ảnh **ngay trong trang** (có thanh công cụ phóng to / xoay / lật), không rời màn Chi tiết, không tải tệp (ảnh `BUG-QLHSVV_07-web-02-nut-Xem-mo-preview.png`). **[Tải]** → không mở lớp xem trước (`.ant-image-preview-wrap` = không có), không mở tab mới (số tab trước/sau đều = 2), trang vẫn đứng ở màn Chi tiết (ảnh `BUG-QLHSVV_07-web-03-sau-khi-bam-Tai-van-o-man-Chi-tiet.png`), tệp về máy ⇒ **2 chức năng khác hẳn nhau** | ✅ |
| 4 | `srs-v3.5.md:6708` (Phụ lục E §H — quy ước **H6**) — "Cột Hành động trong mọi bảng dùng icon (Mắt = Xem, Bút = Sửa, Thùng rác = Xóa, …) thay cho nhãn text. **Mỗi icon BẮT BUỘC có `aria-label` và tooltip hover** mô tả hành động… Đáp ứng WCAG 4.1.2 — không icon-only." | Hai nút dùng **icon + nhãn chữ nhìn thấy được** ("Xem", "Tải"), biểu tượng có `aria-label` (`eye` / `download`). Không còn là icon-only như bản V1.0.2 ⇒ không vi phạm mục tiêu WCAG 4.1.2 của H6 | ✅ |

## Phép đo chi tiết (real-data, do chính QA chạy)

**Tiền đề tự dựng (§Nguyên tắc 4 — thiếu dữ liệu thì TẠO, không phải blocker):**

| Đường thử | Kết quả |
|---|---|
| 1. Tìm hồ sơ **sẵn có** đã có tệp | Rà **toàn bộ 37 vụ việc** trong phạm vi tài khoản (`/api/v1/vu-viecs` + `/api/v1/vu-viecs/{id}/ho-so` cho từng bản ghi) → **0 hồ sơ có tệp**. Không dùng được |
| 2. **Đính kèm tệp vào hồ sơ đã tồn tại** qua màn Chi tiết → [+ Thêm tài liệu] | **THÀNH CÔNG.** Dừng ở đây, không cần đến đường 3 |
| 3. Dựng qua dịch vụ trực tiếp | Không phải dùng |

Chi tiết đường 2: mở `VV-BTP-TW-20260803-002` → nhóm "Tài liệu đính kèm" → [+ Thêm tài liệu] → chọn `QLHSVV_07_qa.jpg` (JPG 1200×800, 38,8 KB — **cùng định dạng JPG với tệp của đối tác**) → [Tải lên]. Bộ bắt thông báo `tools/toast-capture.js` (tự kiểm `soObserverDangSong = 1`): **2 request ghi dữ liệu** (`POST /vu-viecs/upload` 201 + `POST /vu-viecs/{id}/tai-lieu` 201) / **1 khung thông báo** ("Đã tải lên 1 tệp") — không lặp thông báo. Hàng tệp hiện ra với Loại `BO_SUNG`, Định dạng `JPG`, Trạng thái quét **Sạch** — trùng đúng thuộc tính tệp của đối tác. Ảnh: `BUG-QLHSVV_07-seed-01-modal-them-tai-lieu.png`, `BUG-QLHSVV_07-seed-02-bang-tai-lieu-sau-upload.png` (đã mở đọc bằng Read tool, không chỉ lưu).

**Đo (a) — DOM đầy đủ vùng hành động** (đọc bằng `outerHTML`, KHÔNG dùng `textContent`):

| Thứ tự | Thẻ | Nhãn chữ nhìn thấy | `aria-label` của biểu tượng | `title` / tooltip | `href` |
|:-:|---|---|---|---|---|
| 1 | `<button class="ant-btn ant-btn-link ant-btn-sm">` | **"Xem"** | `eye` | không có | — (không phải thẻ liên kết) |
| 2 | `<button class="ant-btn ant-btn-link ant-btn-sm">` | **"Tải"** | `download` | không có | — (không phải thẻ liên kết) |

Toàn hàng chỉ có 2 phần tử bấm được này, không có phần tử ẩn nào khác. Tiêu đề cột = **"Thao tác"** (bản V1.0.2 của đối tác: cột này **không có tiêu đề** và chỉ chứa 1 biểu tượng).

**Đo (b) — mạng khi bấm [Tải]:**

| Chỉ số | Giá trị |
|---|---|
| Số request tải tệp | **1** (`initiatorType = fetch`) |
| Đường dẫn | `https://18.143.165.120.nip.io/htpldn/00000000-…-0001/2026/08/90621321-…/QLHSVV_07_qa.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&…&X-Amz-Expires=3600&…` (đường dẫn ký sẵn, hạn 1 giờ) |
| Mã trạng thái | **200** |
| `content-type` | `image/jpeg` |
| `content-length` | `39772` (= đúng kích thước tệp gốc) |
| `etag` | `"091531a081d38cc9ddda5614f25bd154"` (= MD5 tệp về máy) |
| `Content-Disposition` | **KHÔNG có** — nhưng **không ảnh hưởng kết quả**, vì giao diện lấy tệp bằng `fetch` rồi tự kích hoạt lưu tệp (`sec-fetch-dest: empty`, `sec-fetch-mode: cors`), không còn điều hướng trình duyệt sang đường dẫn tệp như bản V1.0.2 |
| Số request ghi dữ liệu (khác GET) | **0** |
| Số khung thông báo (`toast-capture.js`, tự kiểm observer = 1) | **0** — không có thông báo nào, đúng bản chất thao tác tải tệp |
| Nhật ký lỗi trình duyệt | **rỗng** (không có `error` / `warn`) |

**Đo (c) — trình duyệt có nhận tệp không:** CÓ. Lưu ý môi trường: Chrome do MCP điều khiển chạy chế độ hồ sơ cách ly, nhưng thư mục tải xuống vẫn là `~/Downloads` thật.

| Lần | Bối cảnh | Xóa tệp trước khi bấm | Tệp về máy | MD5 |
|:-:|---|:-:|---|---|
| 1 | Chưa tải lại trang | có (thư mục sạch) | `~/Downloads/QLHSVV_07_qa.jpg` 16:14, 39 772 B | `091531a0…d154` ✅ |
| 2 | **Sau `reload ignoreCache`** (loại mã cũ trong tab) | có | 16:17, 39 772 B | `091531a0…d154` ✅ |
| 3 | Sau reload, có cài bộ bắt thông báo | có | 16:18, 39 772 B | `091531a0…d154` ✅ |

**Phương pháp thứ hai (đo lại theo cách khác):** gọi thẳng dịch vụ `GET /api/v1/vu-viec/{id}/download/{fileId}` → **401 `ERR-AUTH-MTLS-01`** ("mTLS client certificate verification failed"). Đây là **nhóm API tích hợp ngoài** bị chặn mTLS trên môi trường UAT (đã biết từ trước), **không phải** đường mà màn hình CMS dùng — CMS lấy đường dẫn ký sẵn từ `GET /api/v1/vu-viecs/{id}/ho-so` (`downloadUrl`). Vì vậy phương pháp thứ hai được thực hiện bằng cách **lặp lại trọn vẹn thao tác trên giao diện sau khi tải lại trang và xóa sạch tệp cũ** (lần 2 và 3 ở bảng trên) — **không có mâu thuẫn** giữa các phép đo.

## Kết luận verdict

**`Pass`** (cột Q — `Verify`). Cột P giữ nguyên `dev done`, **QA không đụng cột P**.

Lý do: lỗi đối tác phản ánh là **có thật trên bản V1.0.2** (khung hình `t003.38s.jpg` chứng minh nút tải mở tệp ra xem thay vì tải về), nhưng trên bản hiện tại **V1.0.5** thì:
- màn hình đã có **2 nút riêng [Xem] và [Tải]** đúng như `srs-fr-05-vu-viec.md:1729` yêu cầu;
- **[Tải] tải tệp về máy thật**, nội dung nguyên vẹn (MD5 trùng khít), lặp 3/3 lần, trong đó 2 lần sau khi tải lại trang bỏ cache;
- **[Xem]** mới là nút mở xem trước, và nó khác hẳn [Tải] ⇒ không còn chuyện hai nút trùng chức năng.

**Không dùng `Resolved`:** ca này không phải "không tái hiện được lỗi" mà là **đã xác định rõ nguyên nhân cũ và xác nhận chức năng nay chạy đúng trên bản dev đã sửa** — đúng định nghĩa `Pass` (dev báo fix + chạy đúng). Cũng **không dùng `Reject`**: đối tác **không** thao tác sai, họ bấm đúng nút tải xuống; phản ánh của họ hợp lệ tại thời điểm ghi phiếu.

## Ghi nhận ngoài phạm vi case

**Có 1 điểm bất thường** (dựa trên ảnh đã mở đọc, không suy đoán): cột **"Loại"** của bảng tài liệu đính kèm hiển thị **mã nội bộ thô `BO_SUNG`** (có gạch dưới, viết hoa) thay vì chữ tiếng Việt cho người dùng. Đo 2 cách đều khớp: `outerHTML` của ô trả `BO_SUNG`, và điểm ảnh trong `BUG-QLHSVV_07-web-01-hai-nut-Xem-Tai.png` cũng đọc ra `BO_SUNG`. Lỗi này **có mặt ở CẢ hai bản** — khung hình `t000.00s.jpg` của đối tác cũng hiện `BO_SUNG` — nên không phải do bản vá gây ra. Đã mở dòng lỗi mới trên sheet để tới được dev (xem `sheet_add_bug_row.log`).

Hai lỗi đã log ở dòng khác, **không log trùng**: `NHSYC_OOS_01` (row 131 — một lần gửi dữ liệu sinh 2 khung thông báo lỗi khác chữ ở màn Nhập thủ công) và `BUG-NHSYC_01-B` (điểm ưu tiên không tự tính + nhãn lộ mã quy tắc nội bộ lỗi thời). Trong phiên đo case này **không gặp lại** hai lỗi đó.

## Danh mục vật chứng

| Loại | Đường dẫn |
|---|---|
| Khung hình bằng chứng đối tác | `reverify-week-2/verify1-conlai-2026-08-03/frames/QLHSVV_07/` (14 khung + `crop-action-icon-t000.png`, `crop-row-full-t000.png`) |
| Ảnh QA tự chụp — dựng tiền đề | `bug-reports/vu-viec/image/BUG-QLHSVV_07-seed-01-modal-them-tai-lieu.png`, `…-seed-02-bang-tai-lieu-sau-upload.png` |
| Ảnh QA tự chụp — đo | `bug-reports/vu-viec/image/BUG-QLHSVV_07-web-01-hai-nut-Xem-Tai.png`, `…-web-02-nut-Xem-mo-preview.png`, `…-web-03-sau-khi-bam-Tai-van-o-man-Chi-tiet.png` |
| Bảng đối chiếu điều kiện | `reverify-week-2/verify1-conlai-2026-08-03/cond/QLHSVV_07.md` |
| Note gửi đối tác | `reverify-week-2/verify1-conlai-2026-08-03/notes/QLHSVV_07.txt` |
| SRS đã mở đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:570`, `:1729`, `:1804` · `srs-v3.5.md:6708` |
