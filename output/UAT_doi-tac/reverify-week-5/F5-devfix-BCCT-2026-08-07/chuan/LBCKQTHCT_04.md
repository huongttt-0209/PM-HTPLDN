# Chuẩn chấm đã khóa — LBCKQTHCT_04 (dòng 337) — Chi tiết đợt báo cáo · **Biểu mẫu 21b**

> **Giai đoạn A — CHƯA ĐO WEB.** File này chỉ khóa chuẩn chấm. Mọi ô "web hiện tại" để **chờ đo**.
>
> **Đặc tả — nguồn duy nhất do prompt chỉ định:**
> `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`
> — **1.610 dòng**, mtime **2026-08-06 12:46**. Mọi số dòng dưới đây do agent này **tự mở file đếm lại ngày 2026-08-07**.
> Bản `input/srs-update-2026-5-5/` **KHÔNG** được dùng để lấy số dòng.
> Chuẩn bị chung (env · endpoint thật · tài khoản): [`00-CHUAN-BI-CHUNG.md`](00-CHUAN-BI-CHUNG.md).

---

## 1. Lỗi gốc (nguyên văn phiếu đối tác, tab `bug`)

**Các bước (chung 4 case):** 1. Chọn menu "Đợt báo cáo". 2. Mở Trang Chi tiết đợt báo cáo.

**Kết quả mong đợi (chung 4 case):**
- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị

**Phần màn hình bị soi:** **Biểu mẫu 21b**.
**Kết quả thực tế đối tác:** *"Hệ thống hiển thị thiếu các cột: **Số liệu kỳ trước**, **Ghi chú**"* (chữ giống hệt case 03, nhưng **soi biểu mẫu khác**).
**Bằng chứng:** `partner-evidence/LBCKQTHCT_04.jpg` (ảnh tĩnh — agent BẰNG-CHỨNG xử lý song song).

---

## 2. BẢNG SCOPE LOCK (khóa quan hệ từng vế)

| # | Expected đối tác (vế đang tranh chấp) | SRS — file:dòng | Nguyên văn dòng SRS (≤200 ký tự) | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|---|
| **C1** | Bảng biểu mẫu **21b** trên màn Chi tiết đợt BC phải cho cán bộ thấy **số liệu của kỳ trước** ứng với từng chỉ tiêu | `srs-fr-15-ct-htpldn.md:1168` **bắc cầu 1 bước sang `:1167`** | `:1168` = `\| 38 \| form \| Bieu mau 21b (TT17/2025) \| form (editable table, C23) \| Tuong tu 21a \| input \| khi bieu mau ap dung va dot o DANG_LAP_BC \|` | **MATCH** (⚠️ có cờ mâu thuẫn cross-file — §3) | **TEST** | (a) UI: đọc hàng tiêu đề bảng 21b · (b) `GET /api/v1/dot-bao-caos/{id}` → in **khóa thật** trong `soLieuTongHop` |
| **C2** | Bảng biểu mẫu **21b** phải có **chỗ ghi chú** | `:1168` → `:1167`; **củng cố** bởi master `srs-v3.5.md:6616-6617` + `:6699` | `srs-v3.5.md:6699` = `\| -14 \| Ghi chú \| Nhập thủ công \|` (D.2.2 — mapping cột 21b) | **MATCH** (2 nguồn cùng chiều) | **TEST** | như C1 |
| **C3** | *(điều kiện hiển thị)* Bảng 21b phải hiện trên màn Chi tiết đợt BC đang mở | `:1168` cột "Dieu kien hien thi" + `:1366` | `… \| khi bieu mau ap dung va dot o DANG_LAP_BC \|` · `:1366` = `\| 9 \| bieu_mau_su_dung \| text \| Y \| CHECK IN ('MAU_21A','MAU_21B','CA_HAI') — đơn vị nộp tự chọn ở FR-XI-06 \|` | **MATCH** (điều kiện có thật, phải thỏa trước khi đo) | **TEST** | Đọc `bieuMauSuDung` + `trangThai` của đợt **trước** khi kết luận |
| **C4** | *(điều kiện hiển thị ngoài `DANG_LAP_BC`)* Cột phải hiện mọi lúc khi mở Chi tiết | `:1168` | (SRS **IM LẶNG** về nội dung màn ở TAO_DOT / CHO_DUYET_KQ / DA_GUI_TW …) | **GAP** | **BA** | — (không đo được thành verdict) |

**Vế trong KQMĐ chung nhưng đối tác KHÔNG nêu ở Kết quả thực tế** (tràn/đè · đồng nhất ngôn ngữ): **không kéo verdict**. Thấy thì log bug riêng.

---

## 3. Kết luận quan hệ + lý do (chống kết luận "SRS im lặng" ẩu)

**Đã đọc TRỌN, không grep suông:** giống LBCKQTHCT_03 — `:1088–1103` · `:1147–1159` · **`:1161–1175` (trọn bảng thành phần màn Chi tiết Đợt BC, dòng #35–#45)** · `:612–699` (FR-XI-05a) · `:701–771` (FR-XI-06) · `:773–831` (FR-XI-07) · `:1350–1422` (3 entity). Riêng case này đọc thêm:

| Khoảng dòng | Nội dung | Kết quả |
|---|---|---|
| `:971–1040` | Trọn FR-XI-09 (TW tổng hợp) | `:980` + `:1002` "tổng các cột tương ứng 21a/21b" — không liệt kê tên cột |
| `srs-v3.5.md:6601–6625` | Trọn Phụ lục **D.1.3** — mẫu văn bản 21b | Bảng giấy 21b = `STT / Sở-ban-ngành / -1 … -13 / **-14 Ghi chú**`. **Có** Ghi chú, **không có** cột kỳ trước |
| `srs-v3.5.md:6692–6699` | Trọn Phụ lục **D.2.2** — mapping cột 21b | `:6698` `\| -1 → -13 \| Tương tự 21a \| SUM từ các Sở/ban ngành thuộc tỉnh \|` · `:6699` `\| -14 \| Ghi chú \| Nhập thủ công \|` |

**Đã grep những từ khóa nào (TOÀN thư mục `srs-v3.5/`):** `ky truoc`/`kỳ trước` · `Ghi chú`/`Ghi chu` · `21b`/`21B`/`MAU_21B` · `chỉ tiêu`/`cột`. Kết quả **giống hệt** bảng grep ở [LBCKQTHCT_03.md §3](LBCKQTHCT_03.md) — trong nhóm XI, chuỗi *"ky truoc"* xuất hiện **đúng 1 lần**, tại `srs-fr-15-ct-htpldn.md:1167`.

**⇒ Kết luận: MATCH (C1 + C2), nhưng C1 yếu hơn C2 — phải nói thật độ chắc:**

- **C2 (cột Ghi chú) — MATCH mạnh, 2 nguồn cùng chiều.** `:1168` "Tuong tu 21a" ⇒ thừa hưởng cụm *"Ghi chu"* của `:1167`; đồng thời mẫu văn bản 21b ở Phụ lục D cũng có cột **-14 Ghi chú** (`srs-v3.5.md:6616-6617` + `:6699`). Hai tầng **không đá nhau**.
- **C1 (cột Số liệu kỳ trước) — MATCH theo nguồn prompt cấp, nhưng có cờ mâu thuẫn cross-file.** Trong `srs-fr-15` (nguồn được chỉ định) `:1168` nói rõ 21b **"Tuong tu 21a"** — đây là **quy chiếu 1 bước, cùng bảng, cùng ô "Dữ liệu / Nội dung"**, không phải suy diễn ⇒ đủ để tính là **liệt kê**. Nhưng master `srs-v3.5.md` D.1.3 (`:6614-6622`) + D.2.2 (`:6698`) mô tả 21b chỉ gồm `STT / Sở-ban-ngành / -1…-13 / -14 Ghi chú` — **không có** cột kỳ trước.
  **Cách xử đúng:** hai chỗ thuộc **hai tầng khác nhau** — `:1168` đặc tả **form nhập trên màn**, Phụ lục D đặc tả **mẫu văn bản xuất Excel/Word**. Prompt chỉ định nguồn = `srs-fr-15` ⇒ **verdict theo `:1168`**, route **TEST**.
  🔴 **Nhưng nếu đo ra THIẾU cột kỳ trước ở 21b và dev phản hồi bằng mẫu giấy Phụ lục D** ⇒ chuyển thành **bất đồng đặc tả → BA confirm** (đã soạn sẵn §9), **CẤM** tự chấm "Không phải lỗi", cũng **CẤM** ép Reopen bằng lập luận một chiều.

**Điểm hình học phải để ý (dễ đo sai):** 21a và 21b **khác cấu trúc** — 21b có thêm 2 cột định danh `STT` + `Sở/ban ngành` và **mỗi dòng là 1 đơn vị** (bảng tổng hợp cấp tỉnh, `srs-v3.5.md:6619-6621`), trong khi mô hình form nhập ở `:1167` mỗi dòng là **1 chỉ tiêu**. ⇒ **Đếm số dòng để nhận diện bảng 21b là không đáng tin.** Nhận diện bằng **nhãn chứa "21b"** hoặc bằng `bieuMauSuDung` của đợt.

---

## 4. Precondition (chưa đo)

### 4.1 Vai trò / tài khoản
Giống LBCKQTHCT_03 §4.1: **`cbnv_dp_01`** / `Test@1234` (`:712` — tác nhân FR-XI-06 là **CB NV cấp ĐP/BN**). Fallback Rule 7 **cùng vai trò + cùng cấp**: `cbnv_dp_02` → `cbnv_dp_03`. ⚠️ `cbnv_dp` (không hậu tố) **login FAIL 401**. **CẤM** ra verdict bằng `cbnv_tw*` (`:712` — TW không tự lập BC) hoặc `admin`.

### 4.2 Màn / đường dẫn
Menu trái **"Đợt báo cáo"** → `/ct-htpldn/dot-bao-cao` → bấm **Xem** → **`/ct-htpldn/dot-bao-cao/{id}`**. Nhóm endpoint đúng: **`/api/v1/dot-bao-caos/...`** (số nhiều, có `dot-`).

### 4.3 Trạng thái dữ liệu bắt buộc

| # | Điều kiện | SRS | Cách kiểm |
|---|---|---|---|
| 1 | Đơn vị của tài khoản trong `pham_vi_don_vi_nop_ids[]` | `:717` | `GET /api/v1/dot-bao-caos/{id}` |
| 2 | Bản ghi nộp ở **CHUA_NOP** / **DANG_LAP** | `:718` | cùng lệnh |
| 3 | 🔴 Đợt có `bieu_mau_su_dung` bao gồm **MAU_21B** — tức `MAU_21B` **hoặc** `CA_HAI` | `:1366` + `:1168` | `GET /api/v1/dot-bao-caos` → đọc `bieuMauSuDung` — ❌ **KHÔNG THỎA**, xem chặn 1 |
| 4 | 🔴 Đợt ở trạng thái **`DANG_LAP_BC`** | `:1168` | Thanh tiến trình 6 bước (`:1166`) / trường `trangThai` — ❌ **KHÔNG THỎA**, xem chặn 2 |

🔴🔴 **HAI CHẶN TIỀN ĐỀ — case 04 là case BỊ CHẶN NẶNG NHẤT trong 4 case.** Theo kiểm kê [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) (đo 2026-08-07 bằng `GET /api/v1/dot-bao-caos`):

**Chặn 1 — KHÔNG CÓ ĐỢT NÀO DÙNG MẪU 21B (chặn cứng, riêng case này).**
Env có **đúng 3 đợt** và **cả 3 đều `bieuMauSuDung = MAU_21A`**:
`DOT-THBC01-UAT` · `DOT-SO_BO_NAM-2026-1` · `DOT-SO_BO_6_THANG-2026-1`.
⇒ Theo `:1168` (**"khi bieu mau ap dung"**), **21b KHÔNG PHẢI hiện trên bất kỳ đợt nào đang có** ⇒ mở màn thấy vắng 21b là **ĐÚNG đặc tả, KHÔNG phải lỗi**.
🔴 **Đây là nguy cơ Reopen oan số 1 của case này.** Nếu đo bằng dữ liệu hiện có rồi chấm FAIL ⇒ **sai chắc chắn**.
⇒ Muốn đo được, phải **CB NV cấp TW tạo một đợt mới có `bieuMauSuDung = MAU_21B` hoặc `CA_HAI`** (`:625` — chỉ CB NV cấp TW được tạo đợt; `ERR-XI-05a-00` nếu sai vai trò). Dùng `cbnv_tw` / `cbnv_tw_01`, endpoint `POST /api/v1/dot-bao-caos` — **kiểm lại schema trong `/api/docs-json` trước khi gọi, CẤM đoán tên trường**. Seed = **thay đổi môi trường chung** ⇒ **khai rõ đã tạo đợt nào, mã gì, ai tạo**.

**Chặn 2 — hai bậc trạng thái, không đợt nào ở `DANG_LAP_BC`.**
Cả 3 đợt ở `trangThai = TAO_DOT`; riêng `trangThaiNop` của `cbnv_dp_01` = **`DANG_LAP`** trên 2 đợt. **Hai bậc này là hai trường khác nhau, CẤM lẫn:**
- `DOT_BAO_CAO.trang_thai` — **cấp ĐỢT** — `:1368` `CHECK IN ('TAO_DOT','**DANG_LAP_BC**', …)`
- `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop` — **cấp ĐƠN VỊ** — `:1389` `CHECK IN ('CHUA_NOP','**DANG_LAP**', …)`

`:1168` neo vào **`DANG_LAP_BC` — bậc ĐỢT**. Đưa đợt lên bậc đó chính là bug **`LBCKQTHCT_01`** (Open) ⇒ **đo LBCKQTHCT_01 trước**; đường dựng `POST /api/v1/dot-bao-caos/{id}/start`, `GET` lấy `version` trước mỗi bước (sai `version` = lỗi xung đột, **không phải bug**).

⇒ **Chưa gỡ được cả 2 chặn thì LBCKQTHCT_04 KHÔNG ĐO ĐƯỢC:** ghi **ô TRỐNG + nêu blocker** (chặn 1 = nhóm **A** thiếu seed · chặn 2 = nhóm **E** dep upstream), **CẤM chấm FAIL**, và cũng **CẤM chấm "Không phải lỗi"** chỉ vì đợt hiện tại không dùng 21b — đó là chưa đo, không phải đã đo và đúng.

---

## 5. Các bước đo (giao diện thật — Giai đoạn B)

0. Tải lại trang **bằng địa chỉ**, ghi **tên bó mã FE + `last-modified` + `etag`** (kỳ vọng `assets/index-DsMHK7Dp.js`).
1. Đăng nhập **`cbnv_dp_01`** (khai account thực dùng nếu fallback).
2. Menu **"Đợt báo cáo"** → chụp danh sách kèm **cột Biểu mẫu** + **cột Trạng thái** của từng đợt.
3. **Chọn đợt có mẫu bao gồm 21b và ở `DANG_LAP_BC`.** Không có → dừng, ghi blocker (§4.3).
4. **Chốt định danh trước khi kết luận:** `mã đợt` · `bieuMauSuDung` · `trangThai đợt` · `trangThaiNop của đơn vị`.
5. Vào Chi tiết → **tìm đúng bảng 21b** (nhãn chứa "21b"; **KHÔNG** nhận diện bằng số dòng — xem §3). Nếu đợt là `CA_HAI` thì trên màn có **2 bảng** — **đo đúng bảng 21b**, đừng đo nhầm 21a của case 03.
6. **Cuộn NGANG hết bảng** + mở mọi accordion/section thu gọn.
7. Ghi lại **đủ danh sách tiêu đề cột theo thứ tự** + **số cột** của bảng 21b.
8. Chạy **đường đo thứ hai** (§6) trên chính đợt đó.
9. Lặp trên **đợt thứ hai** nếu dựng được; không thì **khai rõ chỉ đo được 1 đợt**.

---

## 6. Đường đo thứ hai (đối chứng độc lập — bắt buộc)

**6a — Đọc DOM bằng `innerText` (KHÔNG `textContent`):** dùng đúng đoạn ở [LBCKQTHCT_03.md §6a](LBCKQTHCT_03.md), nhưng **nhận diện bảng 21b bằng nhãn**, không bằng số dòng:

```js
() => [...document.querySelectorAll('table')].map((t, i) => {
  const nhan = (t.closest('section,[class*="card"],[class*="Card"]')
      ?.querySelector('h1,h2,h3,h4,legend,[class*="title"]')?.innerText || '').trim();
  const box = t.closest('[class*="table-body"],[style*="overflow"]') || t.parentElement;
  return { i, nhan: nhan.slice(0,80), la_21b: /21\s*b/i.test(nhan),
    so_cot_header: t.querySelector('thead tr')?.children.length ?? null,
    tieu_de_cot: [...t.querySelectorAll('thead th')].map(th => th.innerText.trim()),
    so_dong_body: t.querySelectorAll('tbody tr').length,
    cuon_ngang: box ? {scrollWidth: box.scrollWidth, clientWidth: box.clientWidth,
                       bi_cat: box.scrollWidth > box.clientWidth} : null };
})
```

**6b — Đọc thẳng dữ liệu nguồn:** `GET /api/v1/dot-bao-caos/{id}` bằng **chính phiên `cbnv_dp_01`** (cookie-auth trong tab đang đăng nhập; hoặc Bearer token theo §"Cách lấy phiên" của [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md)) → **in khóa cấp cao nhất LẪN khóa bên trong `soLieuTongHop`** (đoạn mã ở [LBCKQTHCT_03.md §6b](LBCKQTHCT_03.md)). 🔴 **CẤM đoán tên khóa.**
**Bắt buộc ghi kèm 3 giá trị làm bằng chứng tiền đề:** `bieuMauSuDung` (phải chứa 21b) · `trangThai` (bậc đợt) · `trangThaiNop` (bậc đơn vị). Thiếu 1 trong 3 ⇒ **verdict vô hiệu**.
🟡 Kiểm kê 07/08 ghi nhận có trường cấp cao nhất **`soLieuKyTruoc`**, hiện **`null`** ⇒ đọc luôn giá trị này; **`null` là dữ liệu rỗng, KHÔNG phải bằng chứng thiếu cột** (bẫy 10).

**Hai đường khớp → dừng. Hai đường mâu thuẫn → CHƯA ĐƯỢC CHỐT**, ghi cả hai + hỏi lại.

---

## 7. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi: trên màn Chi tiết đợt báo cáo của một đợt ở DANG_LAP_BC CÓ ÁP DỤNG MẪU 21B
   (bieuMauSuDung = MAU_21B hoặc CA_HAI), bảng biểu mẫu 21b cho cán bộ (a) thấy được SỐ LIỆU
   CỦA KỲ TRƯỚC, VÀ (b) có chỗ GHI CHÚ — đúng ở CẢ HAI đường đo, lặp lại được trên ≥2 đợt
   (nếu env chỉ dựng được 1 thì khai rõ).

❌ FAIL nếu: ở đúng tiền đề trên, bảng 21b KHÔNG có chỗ nào đọc được số liệu kỳ trước, hoặc
   KHÔNG có chỗ ghi chú — sau khi ĐÃ cuộn ngang hết bảng và mở hết phần thu gọn.
   Thiếu 1 trong 2 vẫn FAIL, nhưng ghi rõ thiếu vế nào.
   ⚠️ Nếu chỉ thiếu "Số liệu kỳ trước" (còn Ghi chú có): ghi FAIL vế C1 + ĐỒNG THỜI gắn cờ
      "cần BA confirm" theo §9, vì đây đúng chỗ srs-fr-15:1168 và Phụ lục D.1.3 lệch nhau.

🚫 KHÔNG ĐO ĐƯỢC (ô TRỐNG + nêu blocker, CẤM chấm FAIL):
   - không đợt nào áp dụng mẫu 21b  → nhóm A (thiếu seed), cần TW tạo đợt CA_HAI
   - không đưa được đợt về DANG_LAP_BC → nhóm E (dep bug LBCKQTHCT_01)
```

---

## 8. ⚠️ Bẫy — rule chống kết luận oan

1. **Bẫy "đợt không dùng 21b".** `:1168` ràng buộc **"khi bieu mau ap dung"**. Đợt `MAU_21A` **không** phải hiện 21b ⇒ vắng mặt là **ĐÚNG spec**. Không đọc `bieuMauSuDung` trước mà chấm FAIL = **Reopen oan**. Đây là bẫy **riêng của case 04**, case 03 không có.
2. **Bẫy trạng thái đợt.** Như case 03: `:1168` chỉ ràng buộc hiển thị **khi đợt ở `DANG_LAP_BC`**; SRS **im lặng** ở các trạng thái khác (vế **C4 = GAP**).
3. **Bẫy đo nhầm bảng.** Đợt `CA_HAI` hiện **2 bảng** trên cùng màn. Đo nhầm 21a rồi ghi cho case 04 = kết quả rác. Nhận diện bằng **nhãn**, không bằng số dòng (21b có thêm `STT` + `Sở/ban ngành`, số dòng phụ thuộc số đơn vị — `srs-v3.5.md:6619-6621`).
4. **Bẫy "không thấy = không có".** Cột có thể nằm sau **thanh cuộn ngang** (21b nhiều cột hơn 21a ⇒ **khả năng bị cắt cao hơn hẳn**) hoặc trong accordion. Bắt buộc kiểm `scrollWidth > clientWidth`.
5. **Bẫy 3 chữ "Ghi chú" khác nhau.** `:1158` modal tạo đợt · `:1369` `DOT_BAO_CAO.ghi_chu` · `:1167`/`:1168` cột trong bảng biểu mẫu ← **chỉ chỗ này** thuộc case. Thấy "Ghi chú" ở thẻ thông tin đợt mà chấm PASS = **Pass oan**.
6. **Bẫy câu chữ.** Không FAIL vì tên cột khác chữ — chỉ FAIL khi **không chỗ nào** cho cán bộ đọc số liệu kỳ trước / ghi chú.
7. **CẤM suy chéo case.** Đã đo 21a (case 03) **KHÔNG** được suy cho 21b. Chữ "Kết quả thực tế" của 2 phiếu **giống hệt nhau** — đây chính là chỗ dễ copy verdict nhất; mỗi case phải có phép đo riêng + ảnh riêng.
8. **Bẫy bản dựng cũ trong tab.** Tải lại bằng địa chỉ + ghi tên bó mã.
9. **Giới hạn hiệu lực.** Verdict chỉ có giá trị cho env nội bộ `18.143.165.120.nip.io` + bó mã đo được; bằng chứng đối tác quay trên môi trường khác.
10. 🟡 **Bẫy "cột ẩn vì dữ liệu rỗng" (mới, từ kiểm kê 07/08).** Trường `soLieuKyTruoc` **tồn tại** ở cấp cao nhất của phản hồi chi tiết đợt nhưng đang **`null`**. Giao diện có thể **ẩn cột khi cả cột rỗng**. ⇒ Trước khi kết luận thiếu cột: (a) đọc `soLieuKyTruoc` bằng §6b; (b) nếu `null` thì **nhập thử số liệu vào 1 chỉ tiêu rồi Lưu nháp** và quét lại. Cột xuất hiện khi có dữ liệu ⇒ **PASS** (ghi hành vi ẩn-khi-rỗng làm candidate, không kéo verdict). Chỉ FAIL khi **có dữ liệu mà vẫn không chỗ nào đọc được**.
11. 🔴 **Bẫy hai bậc trạng thái.** `trangThai` (**đợt**, `:1368`, có `DANG_LAP_BC`) ≠ `trangThaiNop` (**đơn vị**, `:1389`, có `DANG_LAP`). `:1168` neo vào bậc **đợt**. Env: cả 3 đợt `TAO_DOT`, đơn vị `DANG_LAP`. **Ghi cả hai bậc vào kết quả**; thiếu cột trong tình huống này → gắn cờ GAP + BA §9 câu (3), **không Reopen thẳng**.
12. 🔴 **Bẫy "đợt hiện tại không dùng 21b ⇒ Không phải lỗi".** Cả 3 đợt đang là `MAU_21A` ⇒ 21b vắng mặt là **đúng spec**, nhưng điều đó chỉ chứng minh **chưa đo được**, **KHÔNG** chứng minh dev đã làm đúng. Chấm "Không phải lỗi" bằng lập luận này = **Pass oan**. Phải seed đợt `MAU_21B`/`CA_HAI` rồi mới ra verdict.

---

## 9. Soạn sẵn — CẦN BA CONFIRM (dùng khi đo ra thiếu cột kỳ trước, hoặc cho vế C4)

```
CẦN BA CONFIRM: đối tác kỳ vọng bảng biểu mẫu 21b trên màn Chi tiết đợt báo cáo cho cán bộ thấy
số liệu kỳ trước và có chỗ ghi chú (phiếu neo vào "thiết kế").
SRS quy định: srs-fr-15-ct-htpldn.md:1168 — biểu mẫu 21b "Tuong tu 21a", mà :1167 khai 21a gồm
"Chi tieu / So lieu ky truoc / Ky nay / Ghi chu"; điều kiện hiển thị "khi bieu mau ap dung va dot
o DANG_LAP_BC". NHƯNG srs-v3.5.md:6614-6622 (Phụ lục D.1.3, mẫu 21b văn bản) + :6698-6699
(D.2.2 mapping cột) mô tả 21b gồm STT / Sở-ban-ngành / -1…-13 / -14 Ghi chú — CÓ Ghi chú nhưng
KHÔNG có cột số liệu kỳ trước. Hai chỗ thuộc hai tầng khác nhau (form nhập trên màn vs mẫu văn
bản xuất Excel/Word). SRS cũng IM LẶNG về nội dung màn khi đợt không ở DANG_LAP_BC.
Web/dev hiện tại: <chờ đo>.

Câu hỏi BA:
(1) Biểu mẫu 21b trên FORM NHẬP của màn Chi tiết đợt báo cáo có phải gồm cột "Số liệu kỳ trước"
    như 21a không, hay 21b chỉ theo đúng mẫu văn bản TT17 (13 cột chỉ tiêu + Ghi chú)?
    Đề nghị ghi thẳng tập cột của 21b vào dòng #38 bảng thành phần màn hình, thay cho chữ
    "Tuong tu 21a" — để dev và đối tác không chấm bằng hai thước khác nhau.
(2) Khi đợt KHÔNG ở DANG_LAP_BC, màn Chi tiết có phải hiển thị bảng 21b ở dạng chỉ đọc không?
(3) Mô hình STT-52 tách hai bậc trạng thái — cấp ĐỢT (:1368, có DANG_LAP_BC) và cấp ĐƠN VỊ NỘP
    (:1389, có DANG_LAP). Điều kiện hiển thị ở dòng #38 chỉ nhắc "dot o DANG_LAP_BC", trong khi đợt
    là bản ghi toàn quốc dùng chung cho ~70 đơn vị. Đề nghị BA chốt: điều kiện hiển thị biểu mẫu nên
    neo vào trạng thái NỘP CỦA ĐƠN VỊ hay trạng thái của ĐỢT?
Mục đích: BỔ SUNG / làm rõ đặc tả màn hình — KHÔNG chặn bàn giao.
```

---

## 10. Ghi nhận về bằng chứng đối tác

- Bằng chứng là **ảnh tĩnh** `LBCKQTHCT_04.jpg` ⇒ **không** đọc được thao tác cuộn ngang, và **có thể** không đọc được trạng thái đợt / biểu mẫu áp dụng. Cả hai đều là điều kiện quyết định (bẫy 1 + bẫy 2).
- **Yêu cầu agent BẰNG-CHỨNG trả lời rõ 3 câu:** (a) ảnh có đọc được **trạng thái đợt** không? (b) ảnh có đọc được **biểu mẫu áp dụng** của đợt không? (c) ảnh chụp **bảng 21b** hay **bảng 21a**?
- Nếu ảnh không trả lời được (a)+(b) ⇒ bằng chứng đối tác **chưa đủ chứng minh vi phạm `:1168`**; vẫn phải tự đo lại, **không** vì thế mà chấm "Không phải lỗi".
