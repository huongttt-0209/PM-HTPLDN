# Tiêu chí verify — TKHSYCHTPL_03 (dòng 50, tab `bug`)

Mã case: **TKHSYCHTPL_03** — "Tìm kiếm bộ lọc có kết quả"  ·  Thời điểm viết: **2026-08-06 13:03**
Môi trường verify: **https://18.143.165.120.nip.io/**  ·  Bản dựng: **`HTPLDN · V1.0.8`** — đo lúc **2026-08-06 13:50 (giờ VN)**, đọc ở chân thanh điều hướng trái.
Dấu vân tay bản dựng (tự đo lại ở giai đoạn B, không chép của case trước): bó mã FE `assets/index-CNwX9JjX.js` + `assets/index-DVlgOkLg.css` · `GET /` trả `last-modified: Thu, 06 Aug 2026 02:51:16 GMT` (09:51:16 giờ VN) · `etag: W/"6a73f6a4-428"` · máy chủ `nginx/1.27.5` qua `via: 1.1 Caddy` · API `HTPLDN API` `info.version 1.0.0`.
→ **Trùng khít bản dựng case liền trước trong cùng ngày** (chuỗi etag đọc qua `fetch` có thêm tiền tố `W/` của bộ xác thực yếu, phần định danh `6a73f6a4-428` giống hệt) ⇒ không có lần triển khai mới xen giữa hai case.
→ **V1.0.8 mới hơn V1.0.2** (bản đối tác quay) ⇒ **đủ điều kiện đo**, không rơi vào ràng buộc dừng ở mục 6.
Chức năng: bộ lọc / tìm kiếm danh sách hồ sơ vụ việc — FR-V.I-01 (UC51) + FR-V.I-08 (UC58), màn **SCR-V.I-01**
Trạng thái phiếu: `Fail` · Dopai `dev done` · Trạng thái dev fix `Fixed` · ô "Kết quả verify" **TRỐNG** (chưa qua vòng verify nào trên tab `bug`)

> ⚠️ **KHÔNG nhầm với `TKHSYCHTPL_OOS_01`** (dòng 145 tab tuần-2): case đó nói cột **"Cảnh báo thời hạn" hiện nhãn "Đã hoàn thành"** — nhãn ngoài 4 mức. Case NÀY nói **bộ lọc BÁO LỖI, không ra kết quả**. Hai vấn đề khác nhau trên cùng màn.

> 📋 **Khai hồ sơ QA đợt trước đã đọc** (bắt buộc theo flow dòng 88-90): đã đọc
> `reverify-week-2/verify1-conlai-2026-08-03/cond/TKHSYCHTPL_03.md`,
> `reverify-week-2/verify1-conlai-2026-08-03/reverify-audit/TKHSYCHTPL_03.md`,
> `reverify-round-2026-08-05/note/145-TKHSYCHTPL_OOS_01.md`.
> Các file đó chứa **số đo cũ trên bản V1.0.5** (baseline 37 · Bình thường 30 · Sắp hết hạn 2 · Quá hạn 5 · Quá hạn nghiêm trọng 0).
> **Mục 4 dưới đây KHÔNG dùng bất kỳ con số nào trong đó làm ngưỡng** — mọi tiêu chí suy từ đặc tả, số bản ghi để ở dạng biến (`N`), đo lại từ đầu ở giai đoạn B.
> Ghi chú thêm: các trích dẫn dòng SRS trong hồ sơ cũ (`:87`, `:636`) **lệch** so với file thật (`:92`, `:668`) — mọi số dòng dưới đây do lần này tự mở file đọc lại.

---

## 1. Đối tác phản ánh — tách từng vế

**Vế (a) — vế chính, đối tác nêu trong "Kết quả thực tế":**
Chọn bộ lọc **"Mức SLA" = "Sắp hết hạn"** rồi bấm [Tìm kiếm] → hệ thống **hiện thông báo lỗi** thay vì trả danh sách.
🔴 **Nguyên văn chữ thông báo lỗi trong video** (mốc so sánh cho giai đoạn B):

```
mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG
```

Đúng **1 khung** thông báo đỏ, xuất hiện từ giây **~2,5** và **còn nguyên tới hết video (8,0s)** ⇒ loại thông báo không tự tắt.
Địa chỉ trên thanh URL ngay sau khi bấm: `.../vu-viec/danh-sach?mucSla=SAP_HET_HAN&page=1` — giá trị gửi lên là `SAP_HET_HAN`, trong khi chính thông báo liệt kê tập hợp lệ là `SAP_HET`.

**Vế (b) — danh sách có ra kết quả không:**
Sau khi bấm [Tìm kiếm], bảng **rỗng**, hiện "Không tìm thấy hồ sơ phù hợp"; số đếm trên 6 tab biến mất; nút [Xuất Excel] chuyển mờ.
Trước khi lọc (frame `t000.00s`) bảng **CÓ ≥3 dòng** mang nhãn cột "Cảnh báo thời hạn" = "Sắp hết hạn · còn 1 ngày LV" / "còn 0 ngày LV" ⇒ **bảng rỗng là hệ quả của yêu cầu bị từ chối, KHÔNG phải màn rỗng hợp lệ do thiếu dữ liệu.**

**Vế (c) — phân trang 20 bản ghi/trang:**
Đối tác nêu con số **20** ở cột "Kết quả mong đợi" ("hiển thị danh sách kết quả tìm kiếm, phân trang 20 bản ghi mỗi trang").
⚠️ Trong video **KHÔNG có bằng chứng đo vế này** — bảng rỗng nên không thấy chân phân trang ở bất kỳ frame nào. Vế (c) là **kỳ vọng ghi trên phiếu**, không phải triệu chứng đối tác quan sát được.

**Bằng chứng đã mở xem:**
- Tệp: `partner-evidence/TKHSYCHTPL_03.webm` (1.816.715 byte, video ~8 giây, 1920×1080).
- Frame trích: `partner-evidence/frames-TKHSYCHTPL_03/` — 16 frame bước 0,5s (+5 frame bước 2s).
- **Frame đã MỞ XEM bằng công cụ đọc ảnh:** `t000.00s.jpg` (baseline trước lọc) · `t001.56s.jpg` (dropdown "Mức SLA" mở, đủ 4 lựa chọn, con trỏ trên "Sắp hết hạn") · `t002.07s.jpg` (đã chọn "Sắp hết hạn", con trỏ trên nút [Tìm kiếm]) · **`t002.58s.jpg`** (khung lỗi vừa hiện, bảng còn dữ liệu cũ) · **`t004.12s.jpg`** (khung lỗi đọc rõ nhất + bảng đã rỗng) · `t008.00s.jpg` (khung lỗi vẫn còn tới hết video).
- **Kiểm bằng chứng có đúng case này không:** ✅ ĐÚNG — video quay đúng màn "Vụ việc HTPL / Danh sách", đúng thao tác chọn ô "Mức SLA" = "Sắp hết hạn" + bấm [Tìm kiếm], và đúng triệu chứng "hệ thống hiển thị thông báo lỗi" như phiếu ghi. Không có cảnh nào liên quan cột "Cảnh báo thời hạn" hiện nhãn lạ (⇒ không lẫn sang `TKHSYCHTPL_OOS_01`).
- Bằng chứng chỉ có **1 vòng**, không có vấn đề lệch bản ghi/vai trò/bản dựng giữa nhiều vòng.

---

## 2. Đặc tả nói gì

🔴 Nguồn duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` — **đã mở file đọc từng dòng**, số dòng dưới đây là số thật.

**(a) Bộ lọc "Mức SLA" — giá trị hợp lệ + hành vi**

- `srs-fr-05-vu-viec.md:1644` (SCR-V.I-01 §Thành phần màn hình, hàng 9):
  `| 9 | filter-bar | Mức SLA | C10 dropdown | BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG | change → filter | Luôn |`
- `srs-fr-05-vu-viec.md:1516` (bảng "Mức cảnh báo thời hạn (`VU_VIEC.muc_do_canh_bao`)", ánh xạ mã DB → nhãn UI):
  ``| `SAP_HET` | Sắp hết hạn | Vàng |``
  → nhãn "Sắp hết hạn" mà đối tác chọn ứng với mã `SAP_HET`, **là giá trị hợp lệ**.
- `srs-fr-05-vu-viec.md:114` (FR-V.I-01 §Inputs, hàng 7): `| 7 | muc_sla | text | N | BINH_THUONG / SAP_HET / QUA_HAN |`
- `srs-fr-05-vu-viec.md:92` (FR-V.I-01 §Mô tả): "Quản lý danh sách hồ sơ yêu cầu HTPL. Hỗ trợ tìm kiếm, lọc theo trạng thái, lĩnh vực, kênh tiếp nhận, **mức SLA**."
- `srs-fr-05-vu-viec.md:2031` (thực thể VU_VIEC): `| muc_do_canh_bao | text | N | CHECK IN ('BINH_THUONG','SAP_HET','QUA_HAN','QUA_HAN_NGHIEM_TRONG') | 'BINH_THUONG' | Mức cảnh báo SLA |`
- `srs-fr-05-vu-viec.md:2438` (BR-SLA-02 "4 mức cảnh báo"): "(1) Bình thường (>50% thời hạn còn lại), (2) Sắp hết hạn (<50%), (3) Quá hạn (>100%), (4) Quá hạn nghiêm trọng (>2x thời hạn)."

⇒ Đặc tả **NÓI RÕ** và **KHỚP** kỳ vọng đối tác: "Sắp hết hạn" là một lựa chọn hợp lệ của ô lọc, hành vi quy định là **`change → filter`** (lọc), **không phải** từ chối yêu cầu.

**(b) Kết quả lọc / màn rỗng**

- `srs-fr-05-vu-viec.md:149` (FR-V.I-01 §Error Handling — **toàn bảng chỉ có 1 hàng**):
  `| E1 | Không có kết quả | INF-VV-01 | "Không tìm thấy hồ sơ phù hợp" | INFO |`
- `srs-fr-05-vu-viec.md:692-693` (FR-V.I-08 §Error Handling — **toàn bảng chỉ có 2 hàng**):
  `| E1 | Không có kết quả | INF-VV-TK-01 | "Không tìm thấy hồ sơ phù hợp" | INFO |`
  `| E2 | tu_ngay > den_ngay | ERR-VV-TK-01 | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |`
  → **Không có** mục xử lý lỗi nào cho tình huống "giá trị mức SLA không hợp lệ". Tình huống duy nhất được phép ở mức ERROR trên màn này là ngày bắt đầu sau ngày kết thúc.
- `srs-fr-05-vu-viec.md:154` (FR-V.I-01 §AC): "**Given** CB NV lọc theo trạng thái/lĩnh vực/thời gian **When** áp dụng **Then** kết quả AND"
- `srs-fr-05-vu-viec.md:697-698` (FR-V.I-08 §AC): "**Given** CB NV lọc theo lĩnh vực/trạng thái/thời gian **When** áp dụng **Then** kết quả lọc" · "**Given** CB NV kết hợp nhiều điều kiện **When** tìm kiếm **Then** áp dụng AND"
- `srs-fr-05-vu-viec.md:1656` (SCR-V.I-01 hàng 21, cột kết quả):
  `| 21 | table | Cảnh báo thời hạn | C07 | 4 mức màu: 🟢 BINH_THUONG / 🟡 SAP_HET / 🔴 QUA_HAN / ⚫ QUA_HAN_NGHIEM_TRONG (80px) | — | Luôn |`

**(c) Phân trang**

- `srs-fr-05-vu-viec.md:125` (FR-V.I-01 §Processing bước 5): `| 5 | Phân trang (mặc định 20/trang) | BR-DATA-07 |`
- `srs-fr-05-vu-viec.md:668` (FR-V.I-08 §Processing bước 4): `| 4 | Phân trang (20/trang) | BR-DATA-07 |`
- `srs-fr-05-vu-viec.md:1659` (SCR-V.I-01 hàng 24): `| 24 | pagination | Phân trang | C05 | "Hiển thị 1-20 / N kết quả". Mặc định 20/trang | click → chuyển trang | Luôn |`
- `srs-fr-05-vu-viec.md:2394` (BR-DATA-07): "Mọi danh sách sử dụng phân trang. Default: 20 rows/page, max: 100 rows/page."

⇒ Đặc tả **NÓI RÕ** con số **20/trang** và **KHỚP** con số đối tác nêu ở vế (c).

**Phạm vi dữ liệu theo vai trò (để dựng tiền đề đúng):**
- `srs-fr-05-vu-viec.md:1663`: "Cán bộ TW xem toàn quốc; cán bộ BN/ĐP chỉ thấy vụ việc của đơn vị mình."
- `srs-fr-05-vu-viec.md:1665`: "Sắp xếp mặc định: ngày cập nhật DESC. Hỗ trợ sort theo từng cột"

**Mức SLA được sinh ra thế nào (dùng cho mục 5):**
- `srs-fr-05-vu-viec.md:1425` (FR-V.I-CROSS-01): "SLA 15 ngày làm việc… **Scheduled job chạy mỗi 30 phút** kiểm tra và cập nhật mức cảnh báo."
- `srs-fr-05-vu-viec.md:2456` (BR-CALC-03): "Mức cảnh báo tính theo công thức `(NOW() - ngay_tiep_nhan) / deadline * 100`."
  ⇒ Mức SLA là **giá trị dẫn xuất do hệ thống tính**, người dùng không nhập tay.

### ⚠️ IM LẶNG về (đặc tả KHÔNG quy định)

1. **Chữ + mã lỗi khi giá trị mức SLA không hợp lệ** — hai bảng Error Handling (dòng 147-149 và 690-693) không có hàng nào cho tình huống này.
2. **Ngôn ngữ hiển thị của thông báo hệ thống** ở màn này (không có dòng nào bắt buộc tiếng Việt cho thông báo kỹ thuật).
3. **Bộ chọn kích thước trang** — có hay không, gồm những giá trị nào; dòng 2394 chỉ chốt default 20 và max 100.
4. **Bản ghi chưa có mức cảnh báo** — dòng 2031 để cột "Bắt buộc" = `N`, nên không cấm bản ghi thiếu mức; đặc tả không nói bản ghi thiếu mức thì rơi vào nhóm lọc nào.
5. **Thứ tự sắp xếp bên trong tập kết quả đã lọc** — dòng 1665 chỉ nói mặc định của danh sách, không nói riêng cho kết quả lọc.
6. **Có phải loại hồ sơ đã đóng khỏi bộ lọc mức SLA không** — đặc tả im lặng; **đã có quyết định BA 04/08/2026** (nguồn: `reverify-round-2026-08-05/note/145-TKHSYCHTPL_OOS_01.md` dòng 27): giữ hồ sơ đã đóng trong kết quả lọc là **ĐÚNG**, việc loại bỏ là yêu cầu cải tiến, mở phiếu riêng.

### ⚠️ Đặc tả TỰ LỆCH ở 1 điểm (không chạm vế (a) của đối tác)

`srs-fr-05-vu-viec.md:114` (FR-V.I-01 §Inputs) liệt kê `muc_sla` chỉ **3** giá trị `BINH_THUONG / SAP_HET / QUA_HAN` — **thiếu `QUA_HAN_NGHIEM_TRONG`**, trong khi dòng 1644 (đặc tả màn hình), dòng 2031 (ràng buộc thực thể) và dòng 2438 (BR-SLA-02) đều nêu **4** mức.
👉 Điểm lệch này **không ảnh hưởng vế (a)**: `SAP_HET` có mặt ở **cả 4 vị trí**, nên "Sắp hết hạn" chắc chắn hợp lệ ⇒ vế (a) vẫn đo được, **không cần BA**.
👉 Chỉ khi **riêng** mức "Quá hạn nghiêm trọng" bị từ chối (3 mức kia chạy) thì mới chạm điểm lệch này → xem mục 4 §"KHÔNG được chấm Fail vì".

### Rẽ nhánh từng vế

| Vế | Đặc tả | Verdict nhánh |
|---|---|---|
| (a) Bộ lọc "Sắp hết hạn" báo lỗi | **Nói rõ + KHỚP** kỳ vọng đối tác (dòng 1644 `change → filter`, dòng 1516 `SAP_HET`↔"Sắp hết hạn"; không có mục lỗi nào cho giá trị lọc) | **Đo được** → viết mục 4 + 5, sang giai đoạn B |
| (b) Danh sách có ra kết quả | **Nói rõ + KHỚP** (dòng 154, 697-698 "kết quả AND"; dòng 149/692 chỉ 0-kết-quả mới là màn rỗng INFO) | **Đo được** (cần tiền đề ≥1 bản ghi ở mức đo) |
| (c) Phân trang 20 bản ghi/trang | **Nói rõ + KHỚP** đúng con số 20 (dòng 125, 668, 1659, 2394) | **Đo được** (cần ≥21 bản ghi trong phạm vi mới đo được cắt trang) |

⇒ **Không vế nào phải đưa BA.** Cả 3 vế đi thẳng giai đoạn B.

---

## 3. Precondition

- **Tài khoản CỤ THỂ:** `cbnv_tw_01` / `Test@1234` — vai trò `CB_NV_TW`, cấp TW, đơn vị Bộ Tư pháp · TW.
  Chọn tài khoản này vì **trùng vai trò + trùng cấp đơn vị với đối tác** (bằng chứng ghi "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW") ⇒ phạm vi dữ liệu tương đương, và cấp TW là cấp duy nhất thấy được ô lọc "Đơn vị" (dòng 1641) nên tái hiện đủ thanh lọc của đối tác.
  Nếu `cbnv_tw_01` login fail → fallback **cùng vai trò + cùng cấp** sang `cbnv_tw_02` → `cbnv_tw_03`, và **ghi rõ tài khoản thực dùng**. Cấm đổi sang vai trò/cấp khác.
  **Không** dùng tài khoản quản trị để ra verdict.
- **Màn / URL:** `https://18.143.165.120.nip.io/vu-viec/danh-sach` — màn "Vụ việc HTPL / Danh sách", **tab "Tất cả"**, khối "Bộ lọc nâng cao (3)" để **thu gọn** (giống đối tác), mọi ô lọc khác (từ khóa, Lĩnh vực PL, Đơn vị, Kênh tiếp nhận, khoảng ngày) **để trống**.
  Vào màn bằng **click menu** rồi **tải lại trang bỏ bộ nhớ đệm**; ghi bản dựng đọc từ giao diện + dấu vân tay bản dựng vào ô "Bản dựng:" ở đầu file này.
  🔴 **Không** gõ thẳng địa chỉ `?mucSla=SAP_HET_HAN` của đối tác để lấy verdict — đó là địa chỉ do bản cũ sinh ra, không phải thao tác người dùng trên giao diện hiện tại. Được mở riêng để ghi nhận, nhưng kết quả đó **không** dùng chấm PASS/FAIL.
- **Dữ liệu tiền đề:**
  - Vế (a): **không cần** dữ liệu — mức có 0 bản ghi vẫn phải ra màn rỗng INFO, không được ra thông báo từ chối. Đo đủ **4/4 mức**.
  - Vế (b): cần **≥1 vụ việc** trong phạm vi đơn vị của tài khoản có mức cảnh báo đúng bằng mức đang lọc. Mức nào có **0 bản ghi** thì **ghi rõ "không đo được vế (b) ở mức này"**, KHÔNG chấm Fail.
    Nếu mức **"Sắp hết hạn"** (mức đối tác phản ánh) **không có bản ghi nào** → **BẮT BUỘC dựng tiền đề bằng luồng chuẩn**: tạo vụ việc mới → tiếp nhận để hệ thống tính `deadline` (dòng 1425 + 2456: mức tính theo `(NOW() - ngay_tiep_nhan)/deadline`), chờ/đẩy sang ngưỡng <50% thời hạn còn lại. Tạo được mà không tạo → **cấm mọi verdict cho vế (b)**.
  - Vế (c): cần **≥21 bản ghi** trong một tập kết quả để nhìn thấy cắt trang. Nếu tập đã lọc ≤20, đo vế (c) trên **tập KHÔNG lọc** (baseline) của cùng tài khoản, và ghi rõ đã đo trên tập nào.
  - Chỉ đụng **dữ liệu QA**, không đụng dữ liệu đối tác.
- **Bộ đo:** cài `tools/toast-capture.js` dùng chung **trước mỗi lần bấm [Tìm kiếm]** (tự kiểm `soObserverDangSong = 1`), **không** tự viết observer mới, **không** lọc trùng, đọc chữ bằng `innerText`. Mỗi lần điều hướng kiểu SPA phải cài lại observer.

---

## 4. Tiêu chí chấm

### ✅ PASS khi — **tất cả** điều dưới đây đúng

**a. Bộ lọc không bị từ chối (đo đủ 4/4 mức)**

- **a1.** Với **mỗi** mức trong 4 mức của ô "Mức SLA" (Bình thường · Sắp hết hạn · Quá hạn · Quá hạn nghiêm trọng): chọn mức đó rồi chạy tìm kiếm → trong 3 giây kể từ lúc bấm, bộ bắt toast đếm được **đúng 0 khung thông báo mức lỗi**. (Khung mức INFO "Không tìm thấy hồ sơ phù hợp" ở mức có 0 bản ghi **không** tính là khung lỗi.)
- **a2.** Với **mỗi** mức: hệ thống **chấp nhận** yêu cầu danh sách — biểu hiện là màn hiện **hoặc** bảng kết quả có dòng, **hoặc** màn rỗng mức INFO; **không** xuất hiện bất kỳ thông báo nào có nội dung từ chối giá trị của ô "Mức SLA" (kiểu liệt kê lại tập giá trị hợp lệ).
- **a3.** Riêng mức **"Sắp hết hạn"** — vế đối tác phản ánh: lặp lại phép đo a1+a2 **2 lần trong 2 lần tải trang khác nhau** (một lần sau khi vào bằng click menu, một lần sau khi tải lại trang bỏ bộ nhớ đệm), cả 2 lần đều 0 khung lỗi.
- **a4.** Giá trị mức SLA mà giao diện gửi lên nằm trong tập 4 mã ở `srs-fr-05-vu-viec.md:1644`/`:2031` (`BINH_THUONG`/`SAP_HET`/`QUA_HAN`/`QUA_HAN_NGHIEM_TRONG`), **không** phải biến thể `SAP_HET_HAN` như bản V1.0.2 của đối tác. Đọc từ thanh địa chỉ sau khi bấm [Tìm kiếm].

**b. Danh sách ra kết quả đúng**

- **b1.** Với mỗi mức **đã xác nhận có ≥1 bản ghi** trong phạm vi tài khoản: bảng trả **≥1 dòng** (không phải màn rỗng).
- **b2.** Đọc cột "Cảnh báo thời hạn" của **mọi** dòng trả về: giá trị **bằng đúng mức đã lọc**, và nằm trong đúng 4 nhãn ở `srs-fr-05-vu-viec.md:1513-1518` ("Bình thường"/"Sắp hết hạn"/"Quá hạn"/"Quá hạn nghiêm trọng"). Đếm số dòng lệch = **0**.
- **b3.** Xác nhận 2 chiều cho **mức "Sắp hết hạn"**: số dòng đếm được trên bảng **=** tổng số bản ghi mà chính hệ thống báo ở chân bảng ("Hiển thị 1-N / T kết quả"), và cùng con số đó lặp lại sau khi tải lại trang.
- **b4.** Mức có **0 bản ghi**: màn hiện **màn rỗng mức INFO** với nội dung "Không tìm thấy hồ sơ phù hợp" (`srs-fr-05-vu-viec.md:149` và `:692`), **không kèm** khung lỗi. (Đây là PASS, không phải FAIL.)

**c. Phân trang**

- **c1.** Khi chưa đụng vào bộ chọn kích thước trang, một tập kết quả có **T > 20** bản ghi: **đếm tay số dòng thực trên trang 1 = đúng 20**, và chân bảng cho biết đang xem 20 bản ghi đầu trên tổng T (`srs-fr-05-vu-viec.md:1659`, `:125`, `:668`, `:2394`).
- **c2.** Chuyển sang trang 2 của cùng tập đó → số dòng thực = `min(20, T-20)`, và **không dòng nào trùng mã vụ việc** với trang 1 (đối chiếu cột "Mã vụ việc").
- **c3.** Tập kết quả có **T ≤ 20**: bảng hiện **đúng T dòng** trên 1 trang, không cắt trang. (Đây là PASS.)
- **c4.** Ghi rõ vế (c) đã đo trên tập nào (đã lọc mức nào, hay tập không lọc) và T bằng bao nhiêu.

### ❌ FAIL nếu — bất kỳ điều nào dưới đây xảy ra

- **F-a1.** Chọn "Sắp hết hạn" (hoặc bất kỳ mức nào trong 4 mức mà chính ô dropdown sinh ra) rồi chạy tìm kiếm → màn hiện thông báo **mức lỗi**, hoặc thông báo mang nội dung **từ chối giá trị của ô lọc** — kể cả khi bảng bên dưới vẫn có dữ liệu.
  *(Không chấm theo đúng từng chữ. Chữ đối tác gặp ở bản V1.0.2 chép ở mục 1 chỉ là mốc so sánh; chữ đổi mà yêu cầu vẫn bị từ chối thì vẫn FAIL.)*
- **F-a2.** Giao diện gửi lên giá trị mức SLA **không** thuộc tập 4 mã đặc tả (`:1644`/`:2031`) — tức lỗi gốc của đối tác chưa được sửa, chỉ bị che.
- **F-b1.** Mức đã xác nhận **có** bản ghi mà bảng trả **0 dòng**.
- **F-b2.** Có ≥1 dòng trong kết quả mà cột "Cảnh báo thời hạn" **khác** mức đã lọc, hoặc mang nhãn **ngoài** 4 nhãn ở `:1513-1518`.
- **F-b3.** Số dòng trên bảng **lệch** với tổng bản ghi hệ thống tự báo ở chân bảng.
- **F-c1.** Tập kết quả có T > 20 mà trang 1 hiện **≠ 20** dòng khi chưa đụng bộ chọn kích thước trang.
- **F-c2.** Trang 2 lặp lại bản ghi đã có ở trang 1, hoặc không chuyển được trang.

### 🚫 KHÔNG được chấm Fail vì (đặc tả im lặng / đã có quyết định)

1. **Chữ, ngôn ngữ, mã, kiểu khung của thông báo khi 0 kết quả** — đặc tả chỉ nêu nội dung "Không tìm thấy hồ sơ phù hợp" mức INFO (`:149`, `:692`), không quy định vị trí/kiểu hiển thị.
2. **Mức nào đó trả 0 bản ghi** (thường gặp ở "Quá hạn nghiêm trọng") — đặc tả không đòi phải có dữ liệu ở cả 4 mức; 0 kết quả + màn rỗng INFO là hợp lệ.
3. **Hồ sơ đã đóng (Hoàn thành / Từ chối) vẫn lọt bộ lọc mức SLA** — **BA đã chốt 04/08/2026** đây là ĐÚNG (nguồn: `reverify-round-2026-08-05/note/145-TKHSYCHTPL_OOS_01.md` dòng 27; công việc tự động chỉ quét vụ việc đang hoạt động — `srs-fr-05-vu-viec.md:1436`). Đây là phạm vi case `TKHSYCHTPL_OOS_01`, không thuộc phiếu này.
4. **Có / không có bộ chọn kích thước trang, và những giá trị nó cho chọn** — đặc tả im lặng, chỉ chốt default 20 + max 100 (`:2394`).
5. **Tổng bản ghi của 4 mức cộng lại ≠ tổng bản ghi baseline** — đặc tả để `muc_do_canh_bao` không bắt buộc (`:2031` cột "Bắt buộc" = N) và không nói bản ghi thiếu mức rơi vào nhóm nào ⇒ **ghi nhận số đo + nêu ra**, không tự chấm Fail.
6. **Thứ tự sắp xếp bên trong tập kết quả đã lọc** — đặc tả chỉ nói mặc định cho danh sách (`:1665`), không nói riêng cho kết quả lọc.
7. **CHỈ riêng mức "Quá hạn nghiêm trọng" bị từ chối trong khi 3 mức kia chạy** — đặc tả **tự lệch** ở điểm này (`:114` liệt kê 3 mức vs `:1644`/`:2031`/`:2438` liệt kê 4 mức) ⇒ **ghi nhận hiện trạng + ảnh, đưa BA phân xử**, KHÔNG tự chấm Fail cho riêng mức đó. (Nếu mức "Sắp hết hạn" cũng lỗi thì FAIL theo F-a1, không rơi vào ngoại lệ này.)
8. **Chênh lệch số bản ghi giữa môi trường QA và môi trường đối tác** — hai môi trường khác tập dữ liệu; verdict dựa trên hành vi bộ lọc, không dựa trên con số trùng nhau.

---

## 5. Dạng dữ liệu phải phủ

**M = 4** — bốn mức của bộ lọc "Mức SLA", phủ **đủ cả 4**, mỗi mức 1 phép đo riêng:

| # | Nhãn trên giao diện | Mã đặc tả |
|---|---|---|
| 1 | Bình thường | `BINH_THUONG` |
| 2 | **Sắp hết hạn** ← mức đối tác phản ánh | `SAP_HET` |
| 3 | Quá hạn | `QUA_HAN` |
| 4 | Quá hạn nghiêm trọng | `QUA_HAN_NGHIEM_TRONG` |

**+ 1 phép đo đối chứng (không tính vào M):** baseline **không chọn mức nào** — để biết tổng bản ghi trong phạm vi tài khoản và để đo vế (c) khi tập đã lọc quá nhỏ.

**Nguồn xác định M** (tra theo thứ tự flow §"Xác định M", dừng ở bước ②):
- ① *Đặc tả mục nói về nguồn dữ liệu / cách bản ghi được tạo*: `srs-fr-05-vu-viec.md:1425` + `:2456` — mức SLA là **giá trị dẫn xuất do hệ thống tính** (job 30 phút, công thức `(NOW()-ngay_tiep_nhan)/deadline`), người dùng không nhập tay ⇒ **không** sinh thêm dạng theo đường nhập liệu.
- ② *Bộ lọc + giá trị enum ngay trên màn đó*: `srs-fr-05-vu-viec.md:1644` liệt kê **đúng 4** giá trị của ô lọc "Mức SLA". Xác nhận chéo 3 chỗ độc lập: `:2438` (BR-SLA-02 "4 mức cảnh báo"), `:1513-1518` (bảng ánh xạ 4 mã → 4 nhãn UI), `:2031` (ràng buộc thực thể `CHECK IN` đúng 4 mã). Bằng chứng đối tác `t001.56s.jpg` cũng cho thấy dropdown mở ra **đúng 4** lựa chọn ⇒ **M = 4, chốt ở bước ②, không cần hỏi dev/BA.**
- ⚠️ Lệch đã ghi nhận: `:114` chỉ liệt kê 3 mức — coi là **thiếu sót của bảng Inputs**, vì 3 nguồn còn lại + chính giao diện đều nêu 4. Xử lý theo mục 4 §"KHÔNG được chấm Fail vì" điểm 7.

**Chiều phụ cần ghi nhận trong mỗi mức (không cộng vào M cho phiếu này):** hồ sơ **đang hoạt động** (mức tính lại theo job) vs hồ sơ **đã đóng** (mức đóng băng tại thời điểm đóng — BA chốt 04/08/2026). Cả hai đều được trả về hợp lệ; ghi vào biên bản đo để dev đọc, không dùng để chấm.

---

## 6. Bảng điều kiện

Cột "Đối tác" điền NGAY từ bằng chứng; 2 cột sau điền ở giai đoạn B.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — nhãn góc phải khung hình ghi "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" (đọc ở `t000.00s.jpg`, `t004.12s.jpg`) | **`cbnv_tw_01`** — vai trò `CB_NV_TW`, `capDonVi = TW`, `donViId = 00000000-0000-4000-8000-000000000001` (đọc từ `GET /api/v1/auth/me`); tiêu đề góc phải màn ghi "CB Nghiệp vụ - Trung ương #01" + "BTP · TW". Đăng nhập được ngay lần đầu, **không phải fallback**. Không dùng tài khoản quản trị | **Không** — trùng khít cả vai trò lẫn cấp đơn vị của đối tác, không nới chiều nào |
| Entity + trạng thái | Màn "Vụ việc HTPL / Danh sách" (`VU_VIEC`), **tab "Tất cả"** đang chọn. Trước khi lọc: Tất cả **56** · Chờ tiếp nhận (—) · Đang xử lý **35** · Chờ phê duyệt **2** · Hoàn thành **14** · Từ chối **5**. Các dòng nhìn thấy ở trạng thái Hoàn thành / Đã phân công / Đang kiểm tra. Không mở chi tiết bản ghi nào | Cùng màn `/vu-viec/danh-sach`, cùng **tab "Tất cả"**, khối "Bộ lọc nâng cao (3)" **thu gọn**. Trước khi lọc: Tất cả **52** · Chờ tiếp nhận **3** · Đang xử lý **23** · Chờ phê duyệt **1** · Hoàn thành **22** · Từ chối **1**. Kết quả lọc phủ đủ dải trạng thái (Mới tạo · Chờ tiếp nhận · Đã tiếp nhận · Đang kiểm tra · Đã phân công · Đang xử lý · Chờ phê duyệt · Đã duyệt · Hoàn thành · Từ chối · Yêu cầu bổ sung · Đã đánh giá). Không mở chi tiết bản ghi nào | **Không** — cùng entity, cùng màn, cùng tab. Số bản ghi lệch (52 vs 56) là do hai môi trường khác tập dữ liệu, đã chốt ở mục 4 §"KHÔNG chấm Fail vì" điểm 8 |
| Dữ liệu tiền đề | **CÓ** bản ghi thuộc nhóm "Sắp hết hạn": `t000.00s.jpg` hiện 3 dòng cột "Cảnh báo thời hạn" = "Sắp hết hạn · còn 1 ngày LV" (VV-BTP-TW-20260711-002, VV-BTP-TW-20260711-001) và "Sắp hết hạn · còn 0 ngày LV" (VV-STP-AG-20260709-001) ⇒ bảng rỗng sau khi lọc **không phải** do thiếu dữ liệu | **CÓ sẵn, đủ cả 4 mức — KHÔNG phải seed gì.** Đếm trên máy chủ (`GET /api/v1/vu-viecs?mucSla=…&pageSize=100`, chống nhớ đệm): Bình thường **38** · **Sắp hết hạn 2** (`VV-BTP-TW-20260712-006`, `VV-BTP-TW-20260712-005`) · Quá hạn **6** · Quá hạn nghiêm trọng **6**; cộng lại **52 = đúng tổng baseline**. Mức "Sắp hết hạn" (mức đối tác phản ánh) có ≥1 bản ghi ⇒ vế (b) đo được. Tập T>20 cho vế (c): baseline **52** và tập đã lọc "Bình thường" **38** | **Không** — mọi mức đều có bản ghi thật nên không mức nào phải kết luận "không đo được"; không phải dựng thêm tiền đề nên không có nguy cơ "tạo được mà không tạo" |
| Input / filter / giá trị nhập | Ô từ khóa **trống** · "Lĩnh vực PL" **trống** · "Đơn vị" **trống** · "Kênh tiếp nhận" **trống** · **"Mức SLA" = "Sắp hết hạn"** (dropdown mở ra đúng 4 lựa chọn ở `t001.56s.jpg`) · khối "Bộ lọc nâng cao (3)" **thu gọn** · tab **"Tất cả"** → bấm **[Tìm kiếm]** (`t002.07s.jpg`). Giá trị giao diện gửi lên: `mucSla=SAP_HET_HAN` | Giữ **y hệt** bộ ô lọc của đối tác: từ khóa / Lĩnh vực PL / Đơn vị / Kênh tiếp nhận đều **trống**, "Bộ lọc nâng cao (3)" **thu gọn**, tab **"Tất cả"**, chỉ đặt ô **"Mức SLA"** rồi bấm **[Tìm kiếm]**. Dropdown mở ra **đúng 4 lựa chọn**. **Không** gõ thẳng địa chỉ của đối tác để lấy verdict. Giá trị giao diện gửi lên lần này: **`mucSla=SAP_HET`** (và `BINH_THUONG` / `QUA_HAN` / `QUA_HAN_NGHIEM_TRONG`) — đọc trên thanh địa chỉ + `GET /api/v1/vu-viecs?mucSla=…`. Thêm 1 phép phụ: "Sắp hết hạn" + từ khóa `ZZZKHONGTONTAI` để ép ra tập 0 kết quả | **Không** — bộ ô lọc trùng khít. Giá trị gửi lên khác đối tác (`SAP_HET` thay vì `SAP_HET_HAN`) chính là **điều cần đo**, không phải chiều điều kiện bị bỏ sót |
| Độ phủ biến thể (N bản ghi, M dạng) | Đối tác chỉ đo **1/4 mức** ("Sắp hết hạn"), **1 lần**, **1 phiên**. N = **56** bản ghi trong phạm vi trước khi lọc. **Không** đo phân trang (bảng rỗng nên không có chân phân trang trong bất kỳ frame nào) | **M = 4/4 mức**, mỗi mức 1 phép đo riêng + **1 phép baseline** không chọn mức + **1 phép ép 0 kết quả**. Riêng mức "Sắp hết hạn" đo **2 lần trong 2 lần tải trang khác nhau** (vào bằng bấm menu; rồi tải lại trang bỏ nhớ đệm), hai lần cho **cùng một kết quả**. Hai cách thao tác ô chọn khác nhau (chuột và bàn phím) cho cùng kết quả. **N = 52** bản ghi baseline; tổng số dòng đã đọc qua các phép đo: 20 + 38 + 2 + 6 + 6 = **72 dòng**. Vế (c) đo trên **2 tập** có T>20 (baseline 52 và "Bình thường" 38, có cả trang 1 lẫn trang 2) + 3 tập T≤20 | **Không** — phủ đủ M = 4/4 và vượt độ phủ của đối tác ở cả 3 vế |

**3 dữ kiện neo của đối tác:**
1. **URL / bản ghi:** `htpldn-uat.ospgroup.vn/vu-viec/danh-sach?mucSla=SAP_HET_HAN&page=1` — màn danh sách, **không mở bản ghi nào**. Mã vụ việc nhìn thấy trước khi lọc: `VV-BTP-TW-20260713-001`, `VV-BTP-TW-20260711-002`, `VV-BTP-TW-20260711-001`, `VV-STP-AG-20260709-001`.
2. **Trạng thái entity:** danh sách `VU_VIEC` ở tab "Tất cả" (56 bản ghi); các dòng thấy được mang trạng thái Hoàn thành / Đã phân công / Đang kiểm tra. Sau khi bấm [Tìm kiếm]: bảng rỗng "Không tìm thấy hồ sơ phù hợp", số đếm 6 tab biến mất, [Xuất Excel] chuyển mờ.
3. **Vai trò + env + bản dựng:** `CB_NV_TW` (đơn vị BTP · TW) · môi trường **đối tác** `htpldn-uat.ospgroup.vn` · bản dựng đọc ở góc trái màn: **"HTPLDN · V1.0.2"** · thời điểm quay: **2026-07-30 09:08** (đồng hồ hệ điều hành trong khung hình).

**Lệch môi trường / bản dựng — giới hạn hiệu lực của verdict (không phải GAP):**
Đối tác đo trên `htpldn-uat.ospgroup.vn` bản **V1.0.2**; lần này đo trên `https://18.143.165.120.nip.io` bản **V1.0.8** (dấu vân tay ghi ở đầu file). Verdict chỉ có hiệu lực cho bản dựng ghi ở giai đoạn B. Bản đo được **mới hơn** V1.0.2 ⇒ **không** rơi vào điều kiện dừng.

**Kết luận mục 6: 0/5 GAP — không dòng nào bỏ trống, không chiều nào phải nới.**

---

## 7. Sửa đổi

**2026-08-06 14:05 (giờ VN) — bổ sung 1 phép đo, KHÔNG sửa mục 4 và mục 5.**

- **Sửa gì:** thêm **1 phép đo phụ** ngoài M = 4 — đặt "Mức SLA" = "Sắp hết hạn" **kèm** ô từ khóa `ZZZKHONGTONTAI` để ép tập kết quả về **0 bản ghi**.
- **Vì sao:** mục 4 điểm **b4** chấm hành vi ở "mức có 0 bản ghi", nhưng khi đo thật thì **cả 4 mức đều có bản ghi** (38 / 2 / 6 / 6) nên nhánh màn-rỗng không tự xảy ra. Không ép ra tập 0 kết quả thì b4 không có phép đo nào chứng minh, và câu "màn rỗng mức INFO chứ không phải khung lỗi" sẽ thành lập luận suông.
- **Không đụng vào:** ngưỡng PASS/FAIL ở mục 4 và M = 4 ở mục 5 giữ **nguyên văn**; phép đo thêm này **không** được dùng thay cho bất kỳ mức nào trong 4 mức.
