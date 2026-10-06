# Nhật ký đo lại — CNHSNLTVV_03 (dòng 36) · R4 "đo bản mới" · 2026-08-07

**Chuẩn chấm:** [`chuan/CNHSNLTVV_03.md`](../chuan/CNHSNLTVV_03.md) — khối `✅ PASS khi / ❌ FAIL nếu` **KHÔNG sửa, không nới**.
**Phạm vi được giao:** CHỈ 2 quan sát quyết định (Q1 tên tệp sau khi lưu · Q2 mở lại form trên hồ sơ đã có tệp)
\+ đường đo thứ hai. **Không đo lại đủ 6 lượt của khối khóa** — xem §6 GAP.
**Lượt đo trước:** [`do/CNHSNLTVV_03.md`](CNHSNLTVV_03.md) (R3, verdict Reopen, đo trên bó mã `index-CxS5qW_0.js`).

**Verdict đề xuất: ✅ PASS cho cả 2 quan sát quyết định** — nhưng còn GAP về số lượt so với khối khóa (§6).

---

## 1. Vân tay bản dựng — ĐẦU và CUỐI phiên

| Hạng mục | **ĐẦU phiên** (2026-08-06 19:33:49 GMT) | **CUỐI phiên** (2026-08-06 19:41:40 GMT) | Đổi? |
|---|---|---|---|
| Bó mã `GET /` | `assets/index-D4Buvu4S.js` | `assets/index-D4Buvu4S.js` | **không** |
| Bó mã thực tải trong tab | `assets/index-D4Buvu4S.js` | `assets/index-D4Buvu4S.js` | **không** |
| CSS | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` | **không** |
| `last-modified` của `GET /` | `Thu, 06 Aug 2026 19:23:01 GMT` | `Thu, 06 Aug 2026 19:23:01 GMT` | **không** |
| `etag` của `GET /` | `W/"6a74df15-428"` | `W/"6a74df15-428"` | **không** |
| Nhãn chân sidebar | `HTPLDN · V1.0.9` | `HTPLDN · V1.0.9` | **không** |

➡️ **Env KHÔNG deploy giữa lượt đo.** Toàn bộ quan sát dưới đây thuộc **cùng một** bó mã `index-D4Buvu4S.js`
(19:23:01 GMT) — không phải chia trước/sau mốc nào.

**So với các mốc đã biết:**

| Mốc | Bó mã | Giờ | Quan hệ với lượt đo này |
|---|---|---|---|
| 06/08 07:13 | `index-DIABnbIr.js` | 07:13 GMT | cũ hơn 4 bó |
| 06/08 12:48 | `index-CxS5qW_0.js` | 12:48 GMT | **bó mà R3 đã đo** — cũ hơn 3 bó |
| 06/08 17:39 | `index-B2W2Krcs.js` | 17:39 GMT | cũ hơn 2 bó |
| 06/08 18:51 | `index-DsMHK7Dp.js` | 18:51 GMT | cũ hơn 1 bó |
| **06/08 19:23** | **`index-D4Buvu4S.js`** | **19:23 GMT** | ⬅️ **bó của lượt đo R4 này** |

⚠️ Nhãn sidebar **vẫn ghi `V1.0.9`** y hệt lượt R3, trong khi bó mã đã đổi **4 lần**. Đúng như cảnh báo:
**nhãn sidebar không phải định danh bản dựng**; bó mã + `last-modified` mới là định danh thật.

---

## 2. Tài khoản + hồ sơ đã dùng

- Đăng nhập giao diện thật `nht_qa_tw` / `Test@1234` (mã 6 số lấy ở MailHog `http://18.143.165.120:8025`).
  Không fallback tài khoản, không dùng `admin`.
- `GET /api/v1/auth/me` → `vaiTro:["NHT"]` · `donViId 00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp)
  · `capDonVi "TW"` ⇒ trùng khít chuẩn chấm §3.
- Môi trường `https://18.143.165.120.nip.io` (env nội bộ) — **không đổi env**.

| Hồ sơ | ID | Loại · Trạng thái | Tình trạng tệp chứng chỉ khi bắt đầu | Dùng cho |
|---|---|---|---|---|
| `TVV-BTP-TW-0002` | `98cfd963-3cd3-4c8a-bfa9-625460824d6d` | CG · Đang hoạt động (version 28) | **đã có** `cc120.pdf` (người khác đính, còn lại từ R3) | Q1 (dữ liệu cũ) · **Q2** |
| `TVV-BTP-TW-0038` | `7c9107b3-9476-4aba-8225-3765ed848635` | TVV · Mới đăng ký (version 5→6) | **đã có** `2K15 T3 (4.8) & CN (9.8).pdf` (QA đính ở R3) | **Q1 (đính mới)** · **Q2** |
| `TVV-BTP-TW-0037` | `f179382a-2033-48da-adcb-cd631179d0a3` | TVV · Mới đăng ký (version 2→3) | **chưa có** chứng chỉ nào | **Q1 (đính mới)** · **Q2 (sau khi đính)** |

Tệp dùng: `seed-files/B7-CNHSNLTVV03-chungchi-B.pdf` (tên thường) và
`seed-files/2K15 T3 (4.8) & CN (9.8).pdf` (tên có dấu cách + ngoặc đơn + `&`). Ô *Ghi chú cập nhật* = `a` cho cả 2 lượt.

**Bộ đếm thông báo:** dán `tools/toast-capture.js` trước MỖI lượt bấm, tự kiểm `soObserverDangSong = 1`
(**2/2 lượt đều = 1**), không lọc trùng, đọc bằng `innerText`, đếm request ghi song song.

---

## 3. Q1 — Tên tệp sau khi lưu + tải lại trang (quan sát thô từng hồ sơ)

> Cách đọc: mở hồ sơ → tab **"Năng lực"** (màn chỉ đọc) → đọc dòng **"Chứng chỉ chi tiết"**.

### 3.1 `TVV-BTP-TW-0038` — đính tệp MỚI trong phiên này (lượt quyết định)

| Bước | Quan sát thô |
|---|---|
| Đính `B7-CNHSNLTVV03-chungchi-B.pdf` vào khối "Thêm chứng chỉ mới", ghi chú `a` | vùng chọn tệp hiện `B7-CNHSNLTVV03-chungchi-B.pdf (624 B) · Xem · Xóa`; 1 request `POST /api/v1/tu-van-viens/{id}/files` → **201** |
| Bấm **[Lưu]** | `SO_REQUEST = 1` → `PATCH /api/v1/tu-van-viens/7c9107b3-…/nang-luc` → **200**; `SO_KHUNG_THONG_BAO = 1`; nguyên văn: **"Cập nhật năng lực thành công"** |
| **Tải lại trang** → tab "Năng lực" | dòng **"Chứng chỉ chi tiết"** đọc được nguyên văn:<br>`2K15 T3 (4.8) & CN (9.8).pdf`<br>`B7-CNHSNLTVV03-chungchi-B.pdf` |
| Mở lại form, khối "Chứng chỉ hiện có" | `2K15 T3 (4.8) & CN (9.8).pdf [Xóa]` · `B7-CNHSNLTVV03-chungchi-B.pdf [Xóa]` |

➡️ **Hiện TÊN TỆP.** Không có chuỗi kỹ thuật `{"fileDinhKemId":"…"}`.
**Đối chiếu R3:** cùng hồ sơ này, cùng tệp `2K15 T3 (4.8) & CN (9.8).pdf`, R3 đọc được
`{"fileDinhKemId":"80ae5609-a269-4bf3-a7b1-8c33942462c9"}` — nay bản ghi **y nguyên** trên máy chủ (§5) mà màn
hình đã hiện tên tệp ⇒ phần sửa nằm ở chiều **hiển thị + đọc tệp**, không phải ở dữ liệu đã lưu.

### 3.2 `TVV-BTP-TW-0037` — đính tệp MỚI trong phiên này (lượt quyết định thứ 2)

| Bước | Quan sát thô |
|---|---|
| Trước khi đính | dòng "Chứng chỉ chi tiết" = `—` ; form: "Chứng chỉ hiện có — Chưa có chứng chỉ nào." |
| Đính `2K15 T3 (4.8) & CN (9.8).pdf` (tên có ký tự đặc biệt), ghi chú `a` | vùng chọn tệp hiện `2K15 T3 (4.8) & CN (9.8).pdf (638 B) · Xem · Xóa`; `POST …/files` → **201** |
| Bấm **[Lưu]** | `SO_REQUEST = 1` → `PATCH /api/v1/tu-van-viens/f179382a-…/nang-luc` → **200**; `SO_KHUNG_THONG_BAO = 1`; nguyên văn: **"Cập nhật năng lực thành công"** |
| **Tải lại trang** → tab "Năng lực" | dòng **"Chứng chỉ chi tiết"** đọc được nguyên văn:<br>`2K15 T3 (4.8) & CN (9.8).pdf` |
| Mở lại form, khối "Chứng chỉ hiện có" | `2K15 T3 (4.8) & CN (9.8).pdf [Xóa]` |

➡️ **Hiện TÊN TỆP**, giữ nguyên cả dấu cách, ngoặc đơn và `&`. Không có chuỗi kỹ thuật.

### 3.3 `TVV-BTP-TW-0002` — dữ liệu CŨ (không đính tệp mới trong phiên này)

Dòng "Chứng chỉ chi tiết" đọc được nguyên văn:

```
Chung chi hanh nghe Luat su — Bo Tu phap — cấp 15/03/2012
cc120.pdf
```

➡️ Bản ghi tệp `dac3cbb9-…` (do người khác đính, R3 đọc ra chuỗi kỹ thuật) **nay hiện tên tệp `cc120.pdf`**.
Đây là quan sát trên **dữ liệu cũ**, không phải phép thử đính mới — ghi để đối chiếu, **không dùng làm căn cứ chính**.

**Kết Q1 — 2/2 hồ sơ đính tệp MỚI hiện đúng tên tệp sau khi tải lại trang. 0/3 hồ sơ còn thấy chuỗi kỹ thuật.**

---

## 4. Q2 — Mở lại form [Cập nhật năng lực] trên hồ sơ ĐÃ CÓ tệp (quan sát thô từng hồ sơ)

| # | Hồ sơ | Tệp chứng chỉ đang có lúc bấm | Kết quả bấm [Cập nhật năng lực] | URL sau khi bấm |
|---|---|---|---|---|
| 1 | `TVV-BTP-TW-0002` (CG · Đang hoạt động) | `cc120.pdf` (`dac3cbb9-…`) | ✅ **form inline MỞ RA**; khối "Chứng chỉ hiện có" liệt kê `cc120.pdf [Xóa]` | `/chuyen-gia-tvv/98cfd963-…` (**không** đổi sang `/403`) |
| 2 | `TVV-BTP-TW-0038` (TVV · Mới đăng ký) | `2K15 T3 (4.8) & CN (9.8).pdf` (`80ae5609-…`, đính từ R3) | ✅ **form MỞ RA**; "Chứng chỉ hiện có": `2K15 T3 (4.8) & CN (9.8).pdf [Xóa]` | `/chuyen-gia-tvv/7c9107b3-…` |
| 3 | `TVV-BTP-TW-0038` **NGAY SAU khi đính tệp mới** | 2 tệp | ✅ **form MỞ RA**; liệt kê cả 2 tệp kèm [Xóa] | `/chuyen-gia-tvv/7c9107b3-…` |
| 4 | `TVV-BTP-TW-0037` **NGAY SAU khi đính tệp mới** | `2K15 T3 (4.8) & CN (9.8).pdf` (`61aa4cef-…`) | ✅ **form MỞ RA**; liệt kê tệp kèm [Xóa] | `/chuyen-gia-tvv/f179382a-…` |

Kiểm bằng biểu thức `/không có quyền truy cập/i` trên `document.body.innerText` sau mỗi lượt bấm → **false 4/4 lượt**.

**Kết Q2 — 3 hồ sơ khác nhau, 4 lượt bấm, 4/4 form mở ra. 0/4 lượt bị đẩy sang trang báo không có quyền truy cập.**
**Đối chiếu R3:** đúng 3 hồ sơ này (0002 · 0038 · và cơ chế "hễ đã có tệp là chặn") ở R3 đá thẳng sang
`/403 — "Bạn không có quyền truy cập trang này. Vai trò hiện tại: Người hỗ trợ pháp lý"`, tái hiện 3/3.
Nay **không tái hiện lần nào**, kể cả lượt bấm ngay sau khi đính tệp thành công (đúng cảnh gãy của R3).

---

## 5. Đường đo thứ hai (cùng phiên đăng nhập, `fetch(url,{credentials:'include'})`)

### 5.1 Đọc lại bản ghi hồ sơ từ máy chủ — so với màn hình

| Hồ sơ | `version` | `hoSo.chungChiChiTiet` (nguyên văn máy chủ trả) | `fileDinhKems` |
|---|---|---|---|
| `TVV-BTP-TW-0037` | 3 | `[{"fileDinhKemId":"61aa4cef-a4ec-4464-bdd1-3c3d1f16358d"}]` | `2K15 T3 (4.8) & CN (9.8).pdf`, `DKTGMLTVV_13-bang-cap.pdf`, `DKTGMLTVV_13-the-hanh-nghe.pdf` |
| `TVV-BTP-TW-0038` | 6 | `[{"fileDinhKemId":"80ae5609-…"},{"fileDinhKemId":"47afd6d2-…"}]` | `B7-CNHSNLTVV03-chungchi-B.pdf`, `2K15 T3 (4.8) & CN (9.8).pdf` |
| `TVV-BTP-TW-0002` | 28 | `[{"noiCap":"Bo Tu phap","ngayCap":"2012-03-15","tenChungChi":"Chung chi hanh nghe Luat su"},{"fileDinhKemId":"dac3cbb9-…"}]` | `cc120.pdf`, `the-hanh-nghe-qa.pdf` |

➡️ Máy chủ **vẫn lưu** `chungChiChiTiet` dưới dạng `{"fileDinhKemId":"…"}` (không kèm tên tệp). Màn hình hiện được
tên tệp là vì **giao diện nay phân giải được ID sang tên qua đường đọc tệp** (§5.2) — trước đây đường đó bị 403 nên
rơi về in thô chuỗi. **Hai đường (giao diện ↔ máy chủ) KHÔNG mâu thuẫn**: cùng 1 bộ tệp, chỉ khác cách trình bày.

### 5.2 Thử mở tệp qua đường đọc tệp — `GET /api/v1/files/{id}`

| Tệp | ID | R3 (bó `index-CxS5qW_0.js`) | **R4 (bó `index-D4Buvu4S.js`)** |
|---|---|---|---|
| `2K15 T3 (4.8) & CN (9.8).pdf` — QA đính R3 trên 0038 | `80ae5609-a269-4bf3-a7b1-8c33942462c9` | **403 `ERR-PERM-FILE-03`** | ✅ **200** · `tenFile: "2K15 T3 (4.8) & CN (9.8).pdf"` |
| `cc120.pdf` — người khác đính trên 0002 | `dac3cbb9-f22f-4d54-a53e-e8101bd6b783` | **403 `ERR-PERM-FILE-03`** | ✅ **200** · `tenFile: "cc120.pdf"` |
| `the-hanh-nghe-qa.pdf` — tệp cũ trên 0002 | `446e55ad-35a7-4aa1-b986-0644c6325e73` | **403 `ERR-PERM-FILE-03`** | ✅ **200** · `tenFile: "the-hanh-nghe-qa.pdf"` |
| `B7-CNHSNLTVV03-chungchi-B.pdf` — QA đính R4 trên 0038 | `47afd6d2-475a-48ef-8425-b31bfefe1572` | — (chưa tồn tại) | ✅ **200** · `tenFile: "B7-CNHSNLTVV03-chungchi-B.pdf"` |
| `2K15 T3 (4.8) & CN (9.8).pdf` — QA đính R4 trên 0037 | `61aa4cef-a4ec-4464-bdd1-3c3d1f16358d` | — (chưa tồn tại) | ✅ **200** · `tenFile: "2K15 T3 (4.8) & CN (9.8).pdf"` |

➡️ **0/5 tệp còn trả 403 `ERR-PERM-FILE-03`.** Đủ cả 3 tệp mà R3 bắt được 403 — nay đều 200.
Thông báo *"Loại đối tượng 'TVV_HO_SO' của tệp chưa được đăng ký"* **không còn xuất hiện lần nào.**

**Xác nhận thêm bằng lời gọi của chính giao diện (không phải QA gọi tay):** trong nhật ký mạng lúc dựng trang
`TVV-BTP-TW-0038` có `GET /api/v1/files/80ae5609-a269-4bf3-a7b1-8c33942462c9` → **200** — chính là lời gọi mà R3
ghi nhận trong nhật ký trình duyệt là `[403] Yêu cầu bị từ chối`.

**Nhật ký trình duyệt:** chỉ **1** dòng lỗi trong cả phiên — một `404` do **chính QA** thử một mã tệp bịa
(`446e55ad-0000-0000-0000-000000000000`) để dò; máy chủ trả `ERR-VAL-VII-02-01 "Bản ghi không tồn tại"`, **đúng**.
Sau đó tra ra mã thật `446e55ad-35a7-…` thì trả 200. **Không có dòng 403 nào.**

---

## 6. Đối chiếu TỪNG gạch đầu dòng của khối `✅ PASS khi / ❌ FAIL nếu` đã khóa

> Khối khóa (chép nguyên văn, KHÔNG sửa):
> ```
> ✅ PASS khi: đủ 6/6 lượt đều báo thành công VÀ sau khi tải lại trang, tệp vừa đính hiện trong khối
>    "Chứng chỉ hiện có" của đúng hồ sơ đó với đúng tên tệp, VÀ phản hồi máy chủ của cả 6 lượt đều là
>    thành công, VÀ mỗi lượt chỉ sinh đúng 1 thông báo (đếm theo mốc giờ khác nhau, không đếm số phần tử).
> ❌ FAIL nếu: bất kỳ lượt nào trong 6 lượt báo lỗi hoặc máy chủ trả lỗi — kể cả khi chỉ hỏng ở 1 trong 2
>    kiểu tên tệp, hoặc chỉ hỏng ở 1 trong 2 hồ sơ. Cũng FAIL nếu báo thành công nhưng tải lại trang thì
>    tệp không có trong "Chứng chỉ hiện có" (fix bề mặt).
> ```

| # | Điều kiện trong khối khóa | Đo được ở R4 | Kết |
|---|---|---|---|
| P1 | **đủ 6/6 lượt** đều báo thành công | **CHỈ chạy 2 lượt** (cả 2 đều CÓ đính tệp). 2/2 báo *"Cập nhật năng lực thành công"*. **4 lượt còn lại KHÔNG đo** | ⚠️ **GAP — chưa đủ số lượt** |
| P2 | sau khi tải lại trang, tệp vừa đính **hiện trong khối "Chứng chỉ hiện có" của đúng hồ sơ đó với đúng tên tệp** | 2/2 lượt: tải lại trang → mở form → "Chứng chỉ hiện có" liệt kê **đúng tệp vừa đính, đúng tên** (0038: 2 tệp; 0037: 1 tệp) | ✅ **thoả** |
| P3 | **phản hồi máy chủ** của cả 6 lượt đều thành công | 2/2 lượt đo được: `PATCH …/nang-luc` → **200** (kèm `POST …/files` → 201). 4 lượt còn lại không đo | ✅ thoả **trên 2 lượt đã đo** · ⚠️ GAP 4 lượt |
| P4 | **mỗi lượt chỉ sinh đúng 1 thông báo** (đếm theo mốc giờ, không đếm số phần tử) | 2/2 lượt: `SO_KHUNG_THONG_BAO = 1`, `SO_REQUEST = 1`, `khoangCachMs = null` (không có khung thứ 2). `soObserverDangSong = 1` cả 2 lượt | ✅ **thoả** |
| F1 | FAIL nếu **bất kỳ lượt nào báo lỗi hoặc máy chủ trả lỗi** | 0/2 lượt báo lỗi; 0/2 lượt máy chủ trả lỗi. **Không tái hiện** `500 ERR-SYS-00-00-01` / *"Lỗi hệ thống, vui lòng thử lại sau."* | ✅ **không kích hoạt** |
| F2 | FAIL nếu hỏng ở **1 trong 2 kiểu tên tệp** | tên có ký tự đặc biệt (`2K15 T3 (4.8) & CN (9.8).pdf`, trên 0037) → OK; tên thường (`B7-CNHSNLTVV03-chungchi-B.pdf`, trên 0038) → OK. **2/2 kiểu tên đều chạy** | ✅ **không kích hoạt** |
| F3 | FAIL nếu hỏng ở **1 trong 2 hồ sơ** | 2 hồ sơ (`0038` Mới đăng ký, `0037` Mới đăng ký) → cả 2 OK. ⚠️ **Chưa lưu trên hồ sơ Đang hoạt động** — xem GAP-3 | ✅ không kích hoạt **trên 2 hồ sơ đã chạy** · ⚠️ GAP trục trạng thái |
| F4 | FAIL nếu **báo thành công nhưng tải lại trang thì tệp không có trong "Chứng chỉ hiện có"** (fix bề mặt) | 2/2 lượt: tải lại trang → tệp **CÓ** trong "Chứng chỉ hiện có", đúng tên. Đọc lại từ máy chủ khớp. **Đây chính là vế đã làm R3 FAIL — nay không kích hoạt** | ✅ **không kích hoạt** |

### Bảng GAP — những gì R4 KHÔNG đo (ghi thẳng, không suy)

| GAP | Nội dung chưa đo | Vì sao | Ai cần chạy nốt |
|---|---|---|---|
| GAP-1 | **2 lượt M1 "không đính tệp"** (lượt đối chứng chống hồi quy) — **0 lượt** trong R4 | Ngoài phạm vi 2 quan sát được giao; điều phối dặn không mở rộng | QA đo — 2 lượt trên 2 hồ sơ |
| GAP-2 | **2 lượt có tệp còn thiếu** — khối khóa đòi 2 hồ sơ × 2 kiểu tên = 4 lượt có tệp; R4 chạy **2** (mỗi hồ sơ 1 kiểu tên). Hai *kiểu tên* đều đã được phủ, nhưng **không chéo trong cùng hồ sơ** | như trên | QA đo — 2 lượt bắt chéo kiểu tên |
| GAP-3 | **Chưa bấm [Lưu] trên hồ sơ trạng thái "Đang hoạt động"** (`TVV-BTP-TW-0002`, trục N1 của chuẩn chấm). R4 chỉ **mở form** được trên hồ sơ này (Q2 ✅), không thực hiện lượt lưu | Q1 chỉ đòi ≥2 hồ sơ; đã đủ bằng 0038 + 0037 | QA đo — 1 lượt lưu có tệp trên `TVV-BTP-TW-0002` |
| GAP-4 | **Đếm tệp thừa** (tab "Hồ sơ" → khối "File đính kèm", trước/sau mỗi lượt) — không đếm riêng | Phép kiểm này chỉ có ý nghĩa khi có lượt lưu **hỏng**; R4 **không có lượt hỏng nào** | — (không còn tiền đề) |
| GAP-5 | **Hoàn nguyên dữ liệu** theo chuẩn chấm §3 — chưa làm | Ngoài phạm vi 2 quan sát; xem §8 | Điều phối quyết |

---

## 7. Verdict đề xuất

### ✅ PASS — cho **cả 2 quan sát quyết định** đã được giao đo

**Q1 — Tên tệp sau khi lưu: ĐẠT.** 2/2 hồ sơ đính tệp mới, tải lại trang, dòng "Chứng chỉ chi tiết" hiện **đúng
tên tệp**; khối "Chứng chỉ hiện có" trong form cũng liệt kê đúng tệp đúng tên. **Không còn** chuỗi kỹ thuật
`{"fileDinhKemId":"…"}` ở bất kỳ hồ sơ nào (kể cả 3 bản ghi cũ từ R3). ⇒ Vế
*"báo thành công nhưng tải lại trang thì tệp không có trong 'Chứng chỉ hiện có' (fix bề mặt)"* **không còn kích hoạt**.

**Q2 — Mở lại form trên hồ sơ đã có tệp: ĐẠT.** 3 hồ sơ, 4 lượt bấm, **4/4 form mở ra**, kể cả lượt bấm ngay sau
khi đính tệp thành công (đúng cảnh gãy R3). **0/4** lượt bị đẩy sang trang báo không có quyền truy cập.
Khớp `srs-fr-04-chuyen-gia-tvv.md:432` — *"**Given** NHT xem chi tiết TVV cùng đơn vị **When** nhấn 'Cập nhật năng lực'
**Then** form inline edit mở"* (đã tự mở file đếm lại 2026-08-07; file 2542 dòng, số dòng không lệch).

**Đường đo thứ hai: ĐẠT.** `GET /api/v1/files/{id}` trả **200 · 0/5 tệp còn 403 `ERR-PERM-FILE-03`**, gồm đủ cả
3 tệp mà R3 bắt được 403. Đọc lại bản ghi từ máy chủ khớp với màn hình, không mâu thuẫn.

### 🔴 Kèm điều kiện — verdict này KHÔNG tự nó đóng được case

Khối khóa đòi **6/6 lượt**; R4 chỉ chạy **2 lượt** (theo đúng phạm vi được giao). Muốn chấm **Pass cho cả phiếu**
theo đúng câu chữ đã khóa thì phải chạy nốt **GAP-1 + GAP-2 + GAP-3** (4 lượt: 2 lượt không tệp + 2 lượt có tệp,
trong đó ≥1 lượt trên hồ sơ *Đang hoạt động*). **Điều phối quyết** — tôi không nới khối khóa để lấp phần chưa đo.

**Điểm cần biết khi đọc verdict:** máy chủ **vẫn lưu** `chungChiChiTiet` dạng `{"fileDinhKemId":"…"}` không kèm
tên tệp (§5.1). Việc màn hình hiện được tên là nhờ đường đọc tệp đã thôi trả 403. Đây là **quan sát**, không phải
kết luận về cách dev nên làm — khối khóa không nói gì về hình dạng dữ liệu lưu, nên **không** dùng điểm này để FAIL.

---

## 8. Hiện trạng dữ liệu để lại (chưa hoàn nguyên)

| Hồ sơ | Thay đổi do R4 gây ra |
|---|---|
| `TVV-BTP-TW-0038` | +1 tệp `B7-CNHSNLTVV03-chungchi-B.pdf`; version 5→6; nay có 2 chứng chỉ đính tệp |
| `TVV-BTP-TW-0037` | +1 tệp `2K15 T3 (4.8) & CN (9.8).pdf`; version 2→3; từ 0 → 1 chứng chỉ đính tệp |
| `TVV-BTP-TW-0002` | **không đổi** — chỉ mở form rồi rời đi, không bấm [Lưu] |

**Chưa hoàn nguyên** (chuẩn chấm §3 đòi trả `TVV-BTP-TW-0002` về mốc gốc — hồ sơ này R4 không đụng, nhưng dữ liệu
`"Kiem thu CNHSNLTVV_03 tren 120 v1.0.9"` + `cc120.pdf` do người khác để lại **vẫn còn nguyên**).
**Nay [Xóa] trong khối "Chứng chỉ hiện có" đã bấm được** (form mở được) ⇒ hoàn nguyên khả thi khi điều phối yêu cầu.

---

## 9. Ảnh (5 tấm) — `output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/image/`

| Tệp | Bắt được gì |
|---|---|
| [`CNHSNLTVV_03-R4-01-Q2-TVV0002-co-tep-form-mo-duoc.png`](../../../batch-B7-tuvan-mangluoi-2026-08-06/image/CNHSNLTVV_03-R4-01-Q2-TVV0002-co-tep-form-mo-duoc.png) | **Q2 · 0002** — hồ sơ đã có `cc120.pdf`, bấm [Cập nhật năng lực] → form mở, khối "Chứng chỉ hiện có" liệt kê `cc120.pdf [Xóa]`; sidebar `HTPLDN · V1.0.9` |
| [`CNHSNLTVV_03-R4-02-Q2-TVV0038-co-tep-form-mo-duoc.png`](../../../batch-B7-tuvan-mangluoi-2026-08-06/image/CNHSNLTVV_03-R4-02-Q2-TVV0038-co-tep-form-mo-duoc.png) | **Q2 · 0038** — hồ sơ đã có tệp từ R3, form mở, "Chứng chỉ hiện có": `2K15 T3 (4.8) & CN (9.8).pdf [Xóa]` |
| [`CNHSNLTVV_03-R4-03-Q1-TVV0038-sau-tai-lai-hien-ten-tep.png`](../../../batch-B7-tuvan-mangluoi-2026-08-06/image/CNHSNLTVV_03-R4-03-Q1-TVV0038-sau-tai-lai-hien-ten-tep.png) | **Q1 · 0038** — sau lượt lưu có đính tệp + **tải lại trang**: "Chứng chỉ chi tiết" hiện 2 tên tệp, không có chuỗi kỹ thuật |
| [`CNHSNLTVV_03-R4-04-Q1-TVV0037-sau-tai-lai-hien-ten-tep.png`](../../../batch-B7-tuvan-mangluoi-2026-08-06/image/CNHSNLTVV_03-R4-04-Q1-TVV0037-sau-tai-lai-hien-ten-tep.png) | **Q1 · 0037** — sau lượt lưu có đính tệp tên đặc biệt + **tải lại trang**: "Chứng chỉ chi tiết" hiện `2K15 T3 (4.8) & CN (9.8).pdf` |
| [`CNHSNLTVV_03-R4-05-Q2-TVV0037-sau-dinh-tep-form-van-mo-duoc.png`](../../../batch-B7-tuvan-mangluoi-2026-08-06/image/CNHSNLTVV_03-R4-05-Q2-TVV0037-sau-dinh-tep-form-van-mo-duoc.png) | **Q2 · 0037** — bấm [Cập nhật năng lực] **ngay sau khi** đính tệp thành công (đúng cảnh gãy R3): form vẫn mở, không bị đá `/403` |

*(Thông báo dạng toast tự tắt ~3s nên ảnh bắt trạng thái ngay sau lượt lưu; nguyên văn từng câu thông báo lấy từ
`tools/toast-capture.js` + mã phản hồi máy chủ, đã ghi ở §3.)*
