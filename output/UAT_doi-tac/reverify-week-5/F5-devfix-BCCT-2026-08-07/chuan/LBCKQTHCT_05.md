# Chuẩn chấm đã khóa — LBCKQTHCT_05 (dòng 338) — Chi tiết đợt báo cáo · **Khối nhận xét, kiến nghị**

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

**Phần màn hình bị soi:** **Khối nhận xét, kiến nghị**.
**Kết quả thực tế đối tác:** *"Màn hình Chi tiết **không có Khối nhận xét, kiến nghị**"*.
**Bằng chứng:** `partner-evidence/LBCKQTHCT_05.jpg`.

> 🔴 **`LBCKQTHCT_05.jpg` và `LBCKQTHCT_06.jpg` là CÙNG MỘT FILE** — md5 `c0fb9837447ee90ac8c8f975a298aaef` (đã kiểm). Đối tác dùng **1 ảnh cho 2 claim khác nhau về 2 khối khác nhau**. Hệ quả xử lý: xem §10.

---

## 2. BẢNG SCOPE LOCK (khóa quan hệ từng vế)

| # | Expected đối tác (vế đang tranh chấp) | SRS — file:dòng | Nguyên văn dòng SRS (≤200 ký tự) | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|---|
| **C1** | Màn Chi tiết đợt báo cáo phải có **chỗ cho cán bộ nhập/đọc nhận xét, kiến nghị** của báo cáo | `srs-fr-15-ct-htpldn.md:1169` | `\| 39 \| form \| Nhan xet kien nghi \| textarea \| Max 5000 ky tu \| input \| khi dot o DANG_LAP_BC \|` | **MATCH** (liệt kê **đích danh**, đúng bảng thành phần màn hình, đúng màn) | **TEST** | (a) UI: tìm ô nhập + nhãn quanh nó · (b) `GET /api/v1/dot-bao-caos/{id}` → đọc trường nhận xét thực có |
| **C2** | *(nội dung nghiệp vụ củng cố C1)* Khi lập BC, cán bộ được nhập nhận xét/kiến nghị | `:733` + `:744` | `:733` = `\| 10 \| nhan_xet \| text (long) \| N \| Max 5000 ký tự \| — \| Nhập tay \|` · `:744` = `\| 6 \| CB NV nhập/chỉnh sửa số liệu + nhận xét, kiến nghị; có thể chọn ct_htpl_ids_lien_quan[] để truy vết \| — \|` | **MATCH** (2 nguồn cùng chiều với C1) | **TEST** | như C1 |
| **C3** | *(điều kiện hiển thị)* Khối phải hiện **mọi lúc** khi mở Chi tiết đợt BC | `:1169` cột "Dieu kien hien thi" | `… \| input \| khi dot o DANG_LAP_BC \|` | **GAP** (SRS **IM LẶNG** về nội dung màn ở TAO_DOT / CHO_DUYET_KQ / DA_DUYET_KQ / DA_GUI_TW / DA_TONG_HOP) | **BA** | — (không đo được thành verdict) |

**Vế trong KQMĐ chung nhưng đối tác KHÔNG nêu ở Kết quả thực tế** (tràn/đè · đồng nhất ngôn ngữ): **không kéo verdict**. Thấy thì log bug riêng.

---

## 3. Kết luận quan hệ + lý do (chống kết luận "SRS im lặng" ẩu)

**Đã đọc TRỌN, không grep suông:**

| Khoảng dòng đã đọc trọn | Nội dung | Kết quả |
|---|---|---|
| `:1088–1103` | Mở đầu §3 Màn hình chức năng + Layout tổng quan, gồm **[BA-23 tuần 4, chốt 2026-07-30]** ở `:1103` | Đợt báo cáo là **màn độc lập**, không còn là tab trong Chi tiết CT |
| `:1147–1159` | **Trọn** bảng thành phần màn "Dot bao cao dinh ky" (#30–#34) | Màn **danh sách** — không phải màn bị soi |
| `:1161–1175` | **Trọn** bảng thành phần **"Chi tiet Dot BC: Lap & Phe duyet & Gui TW"** (#35–#45) — **đúng màn đối tác mở** | **Dòng #39 (`:1169`) khai đích danh "Nhan xet kien nghi"** — thành phần độc lập, đặt ngay sau 2 dòng biểu mẫu 21a/21b và ngay trước thanh hành động #40 |
| `:701–771` | Trọn FR-XI-06 — Inputs `:722–733`, Processing `:737–747` | `:733` `nhan_xet` là Input; `:744` bước 6 khai thao tác "nhập/chỉnh sửa số liệu + **nhận xét, kiến nghị**" |
| `:773–831` | Trọn FR-XI-07 (Trình phê duyệt BC) | `:802` `[BA chốt 2026-08-06]` — `nhan_xet` **không** tính vào điều kiện "BC hoàn chỉnh" ⇒ **không bắt buộc NHẬP**, nhưng **không** miễn HIỂN THỊ (xem bẫy 3) |
| `:1400–1422` | Trọn entity BAO_CAO_CT_HTPL | Không có trường tên `nhan_xet` riêng ở bảng entity (`:1414` chỉ có `noi_dung`) ⇒ **không dùng entity để bác `:1169`**; tên trường lưu là chuyện implement |

**Đã grep những từ khóa nào (TOÀN thư mục `srs-v3.5/`):**

| Từ khóa | Kết quả |
|---|---|
| `nhận xét, kiến nghị` · `nhan xet, kien nghi` | `srs-fr-15:744` (Processing FR-XI-06) · `srs-fr-08-danh-gia.md:576` (nhóm khác, **không liên quan**) |
| `Nhan xet kien nghi` | **đúng 1 hit toàn bộ SRS: `srs-fr-15-ct-htpldn.md:1169`** — chính là dòng thành phần màn hình |
| `kiến nghị` | `:744` · `:1169` · `srs-fr-08:576`. Không hit nào phủ định hoặc dời khối này sang màn khác |
| `nhan_xet` | `srs-fr-15:733` · `:802`; master `srs-v3.5.md:1640` `:2620` `:2766` `:2893` `:2987` `:3623` `:3698` `:3747` (đều **module khác**) |

**⇒ Kết luận: MATCH (C1 + C2) — chắc nhất trong 4 case.** SRS liệt kê **đích danh** một thành phần tên *"Nhan xet kien nghi"*, kiểu `textarea`, **trong đúng bảng thành phần màn hình của đúng màn Chi tiết đợt báo cáo**, đứng thành **một dòng riêng** (#39). Không cần bắc cầu, không cần suy diễn, không phụ thuộc "thiết kế". ⇒ **Route TEST**: nếu đo được rằng ở đúng tiền đề màn không có chỗ nào cho cán bộ nhập/đọc nhận xét, kiến nghị → **Reopen hợp lệ**.

**Manh mối tầng dữ liệu (chỉ là manh mối, KHÔNG phải căn cứ verdict):** `00-CHUAN-BI-CHUNG.md §3` cho thấy `LapBaoCaoDto` và `UpdateSoLieuDto` **đều có** `nhanXet: string`. Nghĩa là hệ thống **có chỗ chứa** nhận xét ⇒ nếu giao diện không có chỗ nhập thì rất có thể là thiếu ở tầng giao diện, không phải "chưa làm gì cả". Nhưng **có trường trong DTO ≠ đặc tả yêu cầu hiển thị** — quan hệ vẫn khóa bằng `:1169`.

---

## 4. Precondition (chưa đo)

### 4.1 Vai trò / tài khoản

| Vai trò | Tài khoản | Mật khẩu | Vì sao |
|---|---|---|---|
| **Người ra verdict** — CB Nghiệp vụ cấp ĐP | **`cbnv_dp_01`** (`donViId 00000000-0000-4000-8002-000000000006`, `capDonVi = DP`) | `Test@1234` | `:712` — tác nhân FR-XI-06 là **"CB Nghiệp vụ cấp ĐP/BN (đơn vị thuộc phạm vi đợt BC)"** |
| Fallback Rule 7 | `cbnv_dp_02` → `cbnv_dp_03` (**cùng vai trò + cùng cấp**) | `Test@1234` | ⚠️ `cbnv_dp` (không hậu tố) **login FAIL 401** từ 03/08 (`input/input.md:31-33`) |
| **CẤM ra verdict** | `cbnv_tw*` | — | `:712` — **TW không tự lập BC** ⇒ sai tác nhân, verdict vô hiệu |
| **CẤM ra verdict** | `admin` / `Secret@123` | — | Quyền rộng che lỗi phân quyền; chỉ tra định danh và **phải khai** |

### 4.2 Màn / đường dẫn
Menu trái **"Đợt báo cáo"** → `/ct-htpldn/dot-bao-cao` → bấm **Xem** → **`/ct-htpldn/dot-bao-cao/{id}`**. Nhóm endpoint đúng: **`/api/v1/dot-bao-caos/...`** (số nhiều, có `dot-`); `/api/v1/bao-cao/...` là **nhóm IX — nhầm nhóm = đo sai màn**.

### 4.3 Trạng thái dữ liệu bắt buộc

| # | Điều kiện | SRS | Cách kiểm |
|---|---|---|---|
| 1 | Đơn vị của tài khoản trong `pham_vi_don_vi_nop_ids[]` | `:717` | `GET /api/v1/dot-bao-caos/{id}` |
| 2 | Bản ghi nộp ở **CHUA_NOP** / **DANG_LAP** | `:718` | cùng lệnh |
| 3 | 🔴 Đợt ở trạng thái **`DANG_LAP_BC`** | `:1169` cột "Dieu kien hien thi" | Thanh tiến trình 6 bước (`:1166`) / trường `trangThai` |

> ✅ **Case 05 dễ đo nhất trong 4 case.** `:1169` **KHÔNG** ràng buộc theo `bieu_mau_su_dung` — khối nhận xét phải có **bất kể** đợt dùng 21a, 21b hay cả hai. ⇒ **Không dính chặn seed biểu mẫu** như case 04 (cả 3 đợt trong env đang là `MAU_21A`).

🔴 **Chặn tiền đề — hai bậc trạng thái.** Theo kiểm kê [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) (đo 2026-08-07), env có **3 đợt** và **cả 3 ở `trangThai = TAO_DOT`**; nhưng **`trangThaiNop` của `cbnv_dp_01` = `DANG_LAP`** trên đợt #2 (`DOT-SO_BO_NAM-2026-1`, `e9909d96-1391-463b-8072-b1b56c319f8e`) và #3 (`DOT-SO_BO_6_THANG-2026-1`, `a61e07f1-e205-4948-ad7d-a3ccac49830a`). Đợt #2 đã có `baoCaoId = c1b1045d-007c-4104-a169-e267010557a0` (**đã tồn tại bản ghi báo cáo** — tức đơn vị thực sự đang ở pha lập BC).

**Hai bậc là hai trường khác nhau, CẤM lẫn:**
- `DOT_BAO_CAO.trang_thai` — **cấp ĐỢT** — `:1368` `CHECK IN ('TAO_DOT','**DANG_LAP_BC**', …)`
- `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop` — **cấp ĐƠN VỊ** — `:1389` `CHECK IN ('CHUA_NOP','**DANG_LAP**', …)`

`:1169` neo vào **`DANG_LAP_BC` — bậc ĐỢT**, mà env không có đợt nào ở bậc đó.

**Cách xử đúng (KHÔNG bỏ đo, cũng KHÔNG Reopen thẳng):**
1. Đo trên **đợt #2 và #3**, **ghi CẢ HAI bậc trạng thái** vào kết quả.
2. Có khối nhận xét → **PASS**, không bàn thêm.
3. Thiếu khối → **chưa Reopen ngay**: gắn cờ **hai-bậc-trạng-thái** + gửi câu hỏi BA §9 câu (3), vì theo chữ `:1169` thì đợt chưa tới `DANG_LAP_BC` nên chưa phát sinh nghĩa vụ hiển thị ⇒ **GAP đặc tả**, không phải lỗi dev thuần túy.
4. Phép đo sạch theo đúng chữ `:1169` cần đưa **đợt** lên `DANG_LAP_BC` — đó chính là bug **`LBCKQTHCT_01`** (Open) ⇒ **đo LBCKQTHCT_01 trước**. Đường dựng: `POST /api/v1/dot-bao-caos/{id}/start`, `GET` lấy `version` trước mỗi bước (sai `version` = **lỗi xung đột, không phải bug**).

---

## 5. Các bước đo (giao diện thật — Giai đoạn B)

0. Tải lại trang **bằng địa chỉ** (không dùng tab đang mở), ghi **tên bó mã FE + `last-modified` + `etag`** (kỳ vọng `assets/index-DsMHK7Dp.js`, 07/08/2026 01:51).
1. Đăng nhập **`cbnv_dp_01`** (khai account thực dùng nếu fallback).
2. Menu **"Đợt báo cáo"** → chọn đợt thỏa §4.3 → bấm **Xem** → `/ct-htpldn/dot-bao-cao/{id}`.
3. **Chốt định danh trước khi kết luận:** `mã đợt` · `trangThai đợt` · `trangThaiNop của đơn vị` · `bieuMauSuDung` (ghi để đối chiếu, dù `:1169` không ràng buộc theo mẫu).
4. **Cuộn hết chiều dọc trang** — theo thứ tự bảng thành phần, khối nhận xét nằm **sau** biểu mẫu 21a/21b (#37/#38) và **trước** thanh hành động [Hủy] [Lưu nháp] [Trình duyệt KQ] (#40, `:1170`). ⇒ **Mốc định vị: nếu thấy được thanh hành động #40 mà giữa 2 mốc không có ô nhập nào → đó là dấu hiệu thiếu thật.**
5. **Mở mọi accordion / section thu gọn / tab con** trước khi kết luận "không có".
6. Chạy **đường đo thứ hai** (§6) trên chính đợt đó.
7. Lặp bước 2–6 trên **đợt thứ hai** nếu dựng được; không thì **khai rõ chỉ đo được 1 đợt**.

---

## 6. Đường đo thứ hai (đối chứng độc lập — bắt buộc)

**6a — Đọc DOM bằng `innerText` (KHÔNG `textContent`; `textContent` gom cả node ẩn → bug ma):** liệt kê **mọi ô nhập nhiều dòng / vùng soạn thảo** trên màn kèm nhãn quanh nó, và soát cả chuỗi "nhận xét"/"kiến nghị" trên toàn màn:

```js
() => {
  const nhan = el => {
    const id = el.id, lab = id && document.querySelector(`label[for="${CSS.escape(id)}"]`);
    return (lab?.innerText
      || el.closest('[class*="form-item"],[class*="field"],section,div')?.querySelector('label,legend,[class*="label"],h3,h4')?.innerText
      || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').trim().slice(0,80);
  };
  const o = [...document.querySelectorAll('textarea,[contenteditable="true"],[role="textbox"]')]
    .map(el => ({ tag: el.tagName, nhan: nhan(el), maxlength: el.getAttribute('maxlength'),
                  hien: !!(el.offsetWidth || el.offsetHeight), gia_tri_dai: (el.value||el.innerText||'').length }));
  const t = document.body.innerText;      // innerText, KHÔNG textContent
  return { o_nhap_nhieu_dong: o,
           co_chu_nhan_xet: /nh[aậ]n\s*x[eé]t/i.test(t), co_chu_kien_nghi: /ki[eế]n\s*ngh[iị]/i.test(t) };
}
```

**6b — Đọc thẳng dữ liệu nguồn:** `GET /api/v1/dot-bao-caos/{id}` bằng **chính phiên `cbnv_dp_01`** (cookie-auth trong tab đang đăng nhập; hoặc Bearer token theo §"Cách lấy phiên" của [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) — env **có bước mã xác thực**, trường đăng nhập là `username`/`password`) → in **khóa thật** của bản ghi báo cáo, xem có chỗ chứa nhận xét và **giá trị hiện tại** là gì:

```js
async (id) => { const r = await fetch(`/api/v1/dot-bao-caos/${id}`, {credentials:'include'});
  const j = await r.json(); const d = j.data ?? j; const bc = d.baoCao ?? d;
  return { trangThai: d.trangThai, trangThaiNop: d.trangThaiNop, bieuMauSuDung: d.bieuMauSuDung,
           khoa_cap_cao_nhat: Object.keys(d), khoa_bao_cao: Object.keys(bc),
           co_khoa_nhan_xet: Object.keys(bc).filter(k=>/nhanxet|nhan_xet/i.test(k)),
           gia_tri_nhan_xet: bc.nhanXet ?? '(khong co khoa)' }; }
```
**Bắt buộc ghi kèm 2 bậc trạng thái** (`trangThai` + `trangThaiNop`) làm bằng chứng tiền đề — thiếu thì verdict vô hiệu.

**Phép thử quyết định (chỉ chạy khi UI CÓ ô nhập):** nhập một chuỗi mốc-giờ duy nhất dạng `QA-NXKN-<YYYYMMDD-HHMM>` → **Lưu nháp** → tải lại trang bằng địa chỉ → đọc lại. Đọc lại được **khớp từng chữ** ⇒ khối thực sự hoạt động, không phải ô trang trí.

**Hai đường khớp → dừng. Hai đường mâu thuẫn → CHƯA ĐƯỢC CHỐT**, ghi cả hai + hỏi lại.

---

## 7. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi: trên màn Chi tiết đợt báo cáo của một đợt ở DANG_LAP_BC, cán bộ có chỗ NHẬP ĐƯỢC
   nhận xét, kiến nghị của báo cáo (một vùng soạn văn bản nhiều dòng, nhãn quanh nó cho biết đó
   là nhận xét/kiến nghị), VÀ nội dung đã nhập lưu lại + đọc lại được sau khi tải lại trang.
   Đúng ở CẢ HAI đường đo, lặp lại được trên ≥2 đợt (env chỉ dựng được 1 thì khai rõ).

❌ FAIL nếu: ở đúng tiền đề trên, KHÔNG chỗ nào trên màn cho cán bộ nhập nhận xét, kiến nghị —
   sau khi ĐÃ cuộn hết trang và mở hết phần thu gọn.
   Cũng FAIL nếu có ô nhập nhưng nội dung KHÔNG lưu được / không đọc lại được sau khi tải lại
   (khối chỉ có vỏ) — ghi rõ đây là biến thể nào.

🚫 KHÔNG ĐO ĐƯỢC (ô TRỐNG + nêu blocker, CẤM chấm FAIL): không đưa được đợt nào về DANG_LAP_BC
   (nhóm E — dep bug LBCKQTHCT_01).
```

---

## 8. ⚠️ Bẫy — rule chống kết luận oan

1. **Bẫy trạng thái đợt (nguy hiểm nhất).** `:1169` ràng buộc hiển thị **"khi dot o DANG_LAP_BC"**. Mở màn ở `TAO_DOT` mà thấy thiếu khối thì **KHÔNG kết luận được gì** — SRS im lặng ở trạng thái đó (vế **C3 = GAP**). Bằng chứng tuần 4 cho thấy giao diện **vẫn vẽ biểu mẫu 21a ngay ở `TAO_DOT`**, tức màn ở `TAO_DOT` **trông rất giống** màn đang lập ⇒ cực dễ chụp nhầm rồi chấm FAIL oan.
2. **Bẫy "không thấy = không có".** Khối có thể nằm **dưới đáy trang** (sau bảng 13 chỉ tiêu, `:1167`/`:802`) hoặc trong **accordion thu gọn**. Dùng mốc định vị ở §5 bước 4 (kẹp giữa biểu mẫu #37/#38 và thanh hành động #40) trước khi kết luận.
3. **Bẫy "không bắt buộc nhập ⇒ không cần hiện".** `:802` `[BA chốt 2026-08-06]` nói `nhan_xet` **không** tính vào điều kiện "BC hoàn chỉnh". Đó là quy tắc **về việc chặn khi trình duyệt**, **không** miễn nghĩa vụ hiển thị ở `:1169`. Dev/BA viện `:802` để nói "không cần khối" = **hiểu sai dòng**; nếu vẫn tranh chấp thì chuyển BA, **không** tự chấm "Không phải lỗi".
4. **Bẫy nhầm chỗ nhận xét của module khác.** Chuỗi `nhan_xet` có ở **nhiều module khác** (`srs-v3.5.md:1640` `:2620` `:2766` `:2893` `:2987` `:3623` `:3698` `:3747` — đánh giá vụ việc, khảo sát DN…). Thấy "Nhận xét" ở màn khác mà chấm PASS = **Pass oan**. Chỉ tính ô nhận xét **trên đúng màn Chi tiết đợt báo cáo**.
5. **Bẫy nhầm với "Ghi chú" của đợt.** `:1158` (ô Ghi chú modal tạo đợt) và `:1369` (`DOT_BAO_CAO.ghi_chu`) là **ghi chú của ĐỢT**, không phải **nhận xét, kiến nghị của BÁO CÁO**. Hai thứ khác nhau — thấy "Ghi chú" mà chấm PASS = **Pass oan**.
6. **Bẫy nhầm với ghi chú của bước phê duyệt.** `:1171`/`:1172` (Phê duyệt / Từ chối BC) có modal **lý do / ghi chú phê duyệt**; `TrinhDuyetBcDto` có `ghiChu`. Đó là **ô của người duyệt / của thao tác trình**, không thay cho khối nhận xét của báo cáo.
7. **Bẫy câu chữ.** Dev có quyền đặt nhãn khác ("Nhận xét", "Nhận xét & kiến nghị", "Đánh giá chung"…). **KHÔNG FAIL vì câu chữ** — chỉ FAIL khi **không chỗ nào** cho cán bộ nhập nhận xét/kiến nghị. Ngược lại cũng **không PASS** chỉ vì thấy chữ "nhận xét" đâu đó trên màn mà **không có ô nhập** (ví dụ chữ nằm trong hướng dẫn).
8. **CẤM suy chéo case.** 4 case soi **4 phần khác nhau của cùng 1 màn**. Đặc biệt **case 06 (khối truy vết CT liên quan) dùng CHUNG file ảnh với case này** — càng dễ copy verdict. Mỗi case phải có **phép đo riêng + ảnh riêng do QA tự chụp**.
9. **Bẫy bản dựng cũ trong tab.** Tab MCP mở lâu vẫn chạy bó mã cũ — đã gây Reopen oan 01/08. Tải lại bằng địa chỉ + ghi tên bó mã.
10. **Giới hạn hiệu lực.** Verdict chỉ có giá trị cho env nội bộ `18.143.165.120.nip.io` + bó mã đo được; bằng chứng gốc của đối tác quay trên môi trường khác — **ghi câu giới hạn này trong kết quả**.
11. 🔴 **Bẫy hai bậc trạng thái (mới, từ kiểm kê 07/08).** `trangThai` (**đợt**, `:1368`, có `DANG_LAP_BC`) ≠ `trangThaiNop` (**đơn vị**, `:1389`, có `DANG_LAP`). `:1169` neo vào bậc **đợt**. Env: cả 3 đợt `TAO_DOT`, đơn vị `DANG_LAP`. **Ghi cả hai bậc vào kết quả**; thiếu khối trong tình huống này → gắn cờ GAP + BA §9 câu (3), **không Reopen thẳng** (xem §4.3).

---

## 9. Soạn sẵn — CẦN BA CONFIRM (chỉ cho vế C3, hoặc khi dev viện `:802`)

```
CẦN BA CONFIRM: đối tác kỳ vọng màn Chi tiết đợt báo cáo có khối nhận xét, kiến nghị (phiếu neo
vào "thiết kế").
SRS quy định srs-fr-15-ct-htpldn.md:1169 — thành phần màn hình #39 "Nhan xet kien nghi", kiểu
textarea, tối đa 5000 ký tự, điều kiện hiển thị "khi dot o DANG_LAP_BC"; củng cố bởi :733
(nhan_xet là Input của FR-XI-06) và :744 (bước 6: CB NV nhập số liệu + nhận xét, kiến nghị).
SRS IM LẶNG về việc màn hiển thị gì khi đợt KHÔNG ở DANG_LAP_BC. Riêng :802 [BA chốt 2026-08-06]
ghi nhan_xet KHÔNG tính vào điều kiện "BC hoàn chỉnh" — đây là quy tắc chặn khi trình duyệt,
không nói gì về nghĩa vụ hiển thị.
Web/dev hiện tại: <chờ đo>.

Câu hỏi BA:
(1) Khi đợt KHÔNG ở DANG_LAP_BC (đã trình duyệt / đã duyệt / đã gửi TW / đã tổng hợp), màn Chi
    tiết có phải hiển thị nhận xét, kiến nghị đã nhập ở dạng chỉ đọc không? Đề nghị bổ sung điều
    kiện hiển thị cho các trạng thái còn lại vào dòng #39 của bảng thành phần màn hình.
(2) Xác nhận :802 chỉ miễn nhan_xet khỏi điều kiện chặn khi trình duyệt, KHÔNG miễn nghĩa vụ
    hiển thị khối ở :1169 — để dev và đối tác không chấm bằng hai thước khác nhau.
(3) Mô hình STT-52 tách hai bậc trạng thái — cấp ĐỢT (:1368, có DANG_LAP_BC) và cấp ĐƠN VỊ NỘP
    (:1389, có DANG_LAP). Điều kiện hiển thị ở dòng #39 chỉ nhắc "dot o DANG_LAP_BC", trong khi đợt
    là bản ghi toàn quốc dùng chung cho ~70 đơn vị — một đơn vị đang lập báo cáo (trạng thái nộp
    DANG_LAP) vẫn có thể rơi vào cảnh đợt chưa ở DANG_LAP_BC. Đề nghị BA chốt: điều kiện hiển thị
    khối nhận xét nên neo vào trạng thái NỘP CỦA ĐƠN VỊ hay trạng thái của ĐỢT?
Mục đích: BỔ SUNG vào đặc tả màn hình — KHÔNG chặn bàn giao.
```

---

## 10. Ghi nhận về bằng chứng đối tác — **1 ảnh dùng cho 2 claim**

- `LBCKQTHCT_05.jpg` **trùng md5** với `LBCKQTHCT_06.jpg` (`c0fb9837447ee90ac8c8f975a298aaef`) ⇒ đối tác dùng **một ảnh duy nhất** để chứng minh **hai claim khác nhau** (thiếu khối nhận xét · thiếu khối truy vết CT liên quan).
- **Ảnh chung KHÔNG tự động vô hiệu cả 2 claim.** Một ảnh chụp trọn màn hình **có thể** chứng minh cả hai khối cùng vắng mặt — nhưng chỉ khi ảnh thỏa **cả 3 điều kiện**: (a) chụp **trọn chiều dọc** màn Chi tiết (thấy được cả mốc biểu mẫu #37/#38 lẫn thanh hành động #40 ở `:1170`); (b) đọc được **trạng thái đợt** (phải là `DANG_LAP_BC`); (c) không có phần thu gọn nào che khuất.
- **Yêu cầu agent BẰNG-CHỨNG trả lời rõ 4 câu:** (a) ảnh chụp trọn màn hay chỉ một khúc? (b) đọc được **trạng thái đợt** không? (c) có thấy **thanh hành động [Hủy]/[Lưu nháp]/[Trình duyệt KQ]** không? (d) có phần nào bị cắt/thu gọn không?
- Nếu ảnh **không** thỏa (a)+(b) ⇒ bằng chứng đối tác **chưa đủ** chứng minh vi phạm `:1169` ⇒ **vẫn phải tự đo lại**, và **không** vì thiếu bằng chứng mà chấm "Không phải lỗi".
- **QA phải tự chụp ảnh RIÊNG cho case này**, lưu tại `output/UAT_doi-tac/reverify-week-5/F5-devfix-BCCT-2026-08-07/image/`. **CẤM** dùng lại ảnh của case 06.
