# Chuẩn chấm đã khóa — LBCKQTHCT_03 (dòng 336) — Chi tiết đợt báo cáo · **Biểu mẫu 21a**

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

**Phần màn hình bị soi:** **Biểu mẫu 21a**.
**Kết quả thực tế đối tác:** *"Hệ thống hiển thị thiếu các cột: **Số liệu kỳ trước**, **Ghi chú**"*.
**Bằng chứng:** `partner-evidence/LBCKQTHCT_03.webm` (video — agent BẰNG-CHỨNG xử lý song song).

> ⚠️ Expected của phiếu neo vào chữ **"thiết kế"**. **"Thiết kế" (Figma/mockup) KHÔNG phải nguồn chuẩn ở flow này.**
> Chỉ dòng SRS ở đường dẫn trên mới quyết định quan hệ. May mắn là ở case này SRS **có** liệt kê đích danh — xem §2.

---

## 2. BẢNG SCOPE LOCK (khóa quan hệ từng vế)

| # | Expected đối tác (vế đang tranh chấp) | SRS — file:dòng | Nguyên văn dòng SRS (≤200 ký tự) | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|---|
| **C1** | Bảng biểu mẫu 21a trên màn Chi tiết đợt BC phải cho cán bộ thấy **số liệu của kỳ trước** ứng với từng chỉ tiêu | `srs-fr-15-ct-htpldn.md:1167` | `\| 37 \| form \| Bieu mau 21a (TT17/2025) \| form (editable table, C23) \| Chi tieu / So lieu ky truoc / Ky nay / Ghi chu. …\| input \| khi bieu mau ap dung va dot o DANG_LAP_BC \|` | **MATCH** | **TEST** | (a) UI: đọc hàng tiêu đề bảng 21a · (b) `GET /api/v1/dot-bao-caos/{id}` → in **khóa thật** bên trong `soLieuTongHop` |
| **C2** | Bảng biểu mẫu 21a phải có **chỗ ghi chú** cho từng chỉ tiêu | `srs-fr-15-ct-htpldn.md:1167` | (cùng dòng C1 — cụm `… / Ghi chu.`) | **MATCH** | **TEST** | như C1 |
| **C3** | *(điều kiện hiển thị — không phải claim của đối tác, nhưng quyết định phép đo)* Hai cột trên phải hiện **mọi lúc** khi mở Chi tiết đợt BC | `srs-fr-15-ct-htpldn.md:1167` — cột "Dieu kien hien thi" | `… \| khi bieu mau ap dung va dot o DANG_LAP_BC \|` | **GAP** (SRS **IM LẶNG** về việc màn hiển thị gì khi đợt ở TAO_DOT / CHO_DUYET_KQ / DA_GUI_TW) | **BA** | — (không đo được thành verdict; xem §8 bẫy 1) |

**Vế nằm trong KQMĐ chung nhưng đối tác KHÔNG nêu ở Kết quả thực tế** (tràn/đè · đồng nhất ngôn ngữ):
**không kéo verdict case này.** Nếu khi đo tình cờ thấy tràn/đè hoặc lẫn tiếng Anh → **log bug riêng** (bug tình cờ vẫn phải log), **không** trộn vào LBCKQTHCT_03.

---

## 3. Kết luận quan hệ + lý do (chống kết luận "SRS im lặng" ẩu)

**Đã đọc TRỌN, không grep suông:**

| Khoảng dòng đã đọc trọn | Nội dung | Kết quả |
|---|---|---|
| `:1088–1103` | Mở đầu §3 Màn hình chức năng + Layout tổng quan SCR-XI-01, gồm dấu thay đổi **[BA-23 tuần 4, chốt 2026-07-30]** ở `:1103` | Xác nhận Đợt báo cáo **KHÔNG** còn là tab trong Chi tiết CT |
| `:1147–1159` | **Trọn** bảng thành phần màn "Dot bao cao dinh ky" (dòng #30–#34) + ghi chú BA-23 `:1149` + `[CAN BA CHOT]` `:1151` | Đây là màn **DANH SÁCH** đợt — không phải màn bị soi |
| `:1161–1175` | **Trọn** bảng thành phần **"Chi tiet Dot BC: Lap & Phe duyet & Gui TW"** (dòng #35–#45) — **đúng màn đối tác mở** | Dòng **#37 (`:1167`)** khai biểu mẫu 21a gồm 4 cụm: **Chi tieu / So lieu ky truoc / Ky nay / Ghi chu** |
| `:612–699` | Trọn FR-XI-05a (Quản lý đợt BC định kỳ) | Không nói cột biểu mẫu; chỉ khai `bieu_mau_su_dung` `:645` |
| `:701–771` | Trọn FR-XI-06 (Lập BC) — Inputs `:722–733`, Processing `:737–747` | `:731` `so_lieu … Số liệu theo cột 21a/21b`; `:742` "Hiển thị form BC theo mẫu TT17/2025 (21a/21b)" — **không phủ định**, không liệt kê cột |
| `:773–831` | Trọn FR-XI-07 — `:802` `[BA chốt 2026-08-06]` "MAU_21A → **13 chỉ tiêu** biểu 21a" | Khẳng định 21a có 13 chỉ tiêu; **13 chỉ tiêu = 13 DÒNG** trong mô hình `:1167`, không mâu thuẫn với 4 cột |
| `:1350–1422` | Trọn 3 entity DOT_BAO_CAO / DOT_BAO_CAO_DON_VI_NOP / BAO_CAO_CT_HTPL | `:1416` `so_lieu_tong_hop … Số liệu (JSON)` — cấu trúc **tự do**, không khai tên cột ⇒ không dùng entity để bác `:1167` |

**Đã grep những từ khóa nào (trên TOÀN thư mục `srs-v3.5/`, không chỉ 1 file):**

| Từ khóa | Kết quả |
|---|---|
| `ky truoc` · `kỳ trước` | **Trong nhóm XI chỉ đúng 1 chỗ: `srs-fr-15-ct-htpldn.md:1167`.** Các hit còn lại thuộc `srs-fr-01-dashboard.md` (xu hướng KPI) + `CHANGELOG` — khác nghiệp vụ |
| `Ghi chú` · `Ghi chu` | `:1158` (ô Ghi chú của **modal tạo đợt**) · `:1167` (**cột trong bảng 21a** — đúng vế) · `:1369` (`DOT_BAO_CAO.ghi_chu` — trường của **đợt**). **3 chỗ khác nhau — xem bẫy 3** |
| `21a` · `21A` · `MAU_21A` | `:27` `:621` `:645` `:710` `:730` `:731` `:742` `:768` `:802` `:980` `:1002` `:1158` `:1167` `:1168` `:1175` `:1366` `:1412` — đã mở đọc từng dòng |
| `chỉ tiêu` · `cột` | `:731` `:802` `:830` `:980` `:1002` — không dòng nào liệt kê tên cột khác `:1167` |

**⇒ Kết luận: MATCH (C1 + C2).** SRS liệt kê **đích danh** cả *"So lieu ky truoc"* lẫn *"Ghi chu"* trong ô "Dữ liệu / Nội dung" của **đúng dòng #37, đúng bảng thành phần màn hình Chi tiết Đợt BC**. Đây không phải suy diễn — không cần bắc cầu qua "thiết kế". ⇒ **Route TEST**: nếu đo được rằng bảng 21a không cho cán bộ thấy số liệu kỳ trước và không có chỗ ghi chú → **Reopen hợp lệ**.

**Điểm phải nói thật (không đổi verdict, nhưng phải ghi để dev không cãi vòng):**
Master `srs-v3.5.md` **Phụ lục D.1.2** (`:6577–6599`) vẽ **mẫu văn bản giấy 21a** chỉ gồm **13 cột chỉ tiêu `-1 → -13`**, và **D.2.1** (`:6674–6690`) map 13 cột đó — **không** có "Số liệu kỳ trước", **không** có "Ghi chú". Hai chỗ này thuộc **hai tầng khác nhau**: `:1167` đặc tả **form nhập trên màn** (bảng dựng đứng, mỗi chỉ tiêu 1 dòng); Phụ lục D đặc tả **mẫu văn bản xuất Excel/Word** (bảng nằm ngang). Prompt chỉ định nguồn = `srs-fr-15` ⇒ **verdict theo `:1167`**. Nếu dev viện mẫu giấy để nói "không cần 2 cột" thì đó là **bất đồng đặc tả** ⇒ chuyển BA, **CẤM tự chấm "Không phải lỗi"**.

---

## 4. Precondition (cần gì mới mở được đúng màn — chưa đo)

### 4.1 Vai trò / tài khoản

| Vai trò | Tài khoản | Mật khẩu | Vì sao |
|---|---|---|---|
| **Người ra verdict** — CB Nghiệp vụ cấp ĐP | **`cbnv_dp_01`** (`donViId 00000000-0000-4000-8002-000000000006`, `capDonVi = DP`) | `Test@1234` | `:712` khai tác nhân của FR-XI-06 là **"CB Nghiệp vụ cấp ĐP/BN (đơn vị thuộc phạm vi đợt BC)"** |
| Fallback Rule 7 | `cbnv_dp_02` → `cbnv_dp_03` (**cùng vai trò + cùng cấp**) | `Test@1234` | ⚠️ `cbnv_dp` (không hậu tố) **login FAIL 401** từ 03/08 — đã ghi ở `input/input.md:31-33` |
| **CẤM dùng ra verdict** | `cbnv_tw*` (TW) | — | `:712` — **"TW không tự lập BC"**. Đo bằng TW = sai tác nhân ⇒ verdict vô hiệu |
| **CẤM dùng ra verdict** | `admin` / `Secret@123` | — | Quyền rộng che lỗi phân quyền; chỉ tra định danh và **phải khai** |

### 4.2 Màn / đường dẫn

- Menu trái **"Đợt báo cáo"** (mục độc lập, ngang hàng "CT HTPLDN") → `/ct-htpldn/dot-bao-cao`
- Bấm **Xem** trên dòng đợt → **`/ct-htpldn/dot-bao-cao/{id}`** = **màn Chi tiết đợt báo cáo** đang tranh chấp
- ⚠️ Nhóm endpoint đúng là **`/api/v1/dot-bao-caos/...`** (số nhiều, có `dot-`). `/api/v1/bao-cao/...` là **báo cáo thống kê nhóm IX — nhầm nhóm = đo sai màn**.

### 4.3 Trạng thái dữ liệu bắt buộc (3 điều kiện SRS + 1 điều kiện hiển thị)

| # | Điều kiện | SRS | Cách kiểm trước khi đo |
|---|---|---|---|
| 1 | Đơn vị của tài khoản nằm trong `pham_vi_don_vi_nop_ids[]` của đợt | `:717` | `GET /api/v1/dot-bao-caos/{id}` → đối chiếu mã đơn vị |
| 2 | Bản ghi nộp của (đợt, đơn vị) ở **CHUA_NOP** hoặc **DANG_LAP** | `:718` | cùng lệnh trên |
| 3 | Đợt có `bieu_mau_su_dung` bao gồm **MAU_21A** (tức `MAU_21A` hoặc `CA_HAI`) | `:1366` + `:1167` ("khi bieu mau ap dung") | `GET /api/v1/dot-bao-caos` → đọc `bieuMauSuDung` — ✅ **cả 3 đợt trong env đều `MAU_21A`**, điều kiện này **THỎA** |
| 4 | 🔴 **Đợt ở trạng thái `DANG_LAP_BC`** | `:1167` cột "Dieu kien hien thi" | Thanh tiến trình 6 bước (`:1166`) / trường `trangThai` |

🔴 **Cảnh báo tiền đề — hai bậc trạng thái, đây là chỗ dễ chấm oan nhất.** Theo kiểm kê [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) (đo 2026-08-07), env có **3 đợt** và **cả 3 ở `trangThai = TAO_DOT`**; nhưng **`trangThaiNop` của đơn vị `cbnv_dp_01` = `DANG_LAP`** trên đợt #2 (`DOT-SO_BO_NAM-2026-1`, `e9909d96-1391-463b-8072-b1b56c319f8e`) và #3 (`DOT-SO_BO_6_THANG-2026-1`, `a61e07f1-e205-4948-ad7d-a3ccac49830a`).

**Hai bậc này là hai trường khác nhau, CẤM lẫn:**
- `DOT_BAO_CAO.trang_thai` — **cấp ĐỢT** — `:1368` `CHECK IN ('TAO_DOT','**DANG_LAP_BC**','CHO_DUYET_KQ','DA_DUYET_KQ','DA_GUI_TW','DA_TONG_HOP')`
- `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop` — **cấp ĐƠN VỊ** — `:1389` `CHECK IN ('CHUA_NOP','**DANG_LAP**','CHO_DUYET','DA_DUYET','DA_NOP','QUA_HAN')`

`:1167` neo điều kiện hiển thị vào **`DANG_LAP_BC` — bậc ĐỢT**. Env hiện **không có đợt nào ở bậc đó**, dù đơn vị đã ở pha lập BC.

**Cách xử đúng (KHÔNG bỏ đo, cũng KHÔNG Reopen thẳng):**
1. Đo trên **đợt #2 và #3** (đơn vị đang `DANG_LAP` — tức thực sự đang ở pha lập BC), **ghi CẢ HAI bậc trạng thái** vào kết quả.
2. Nếu 2 cột **có** → **PASS**, không cần bàn thêm.
3. Nếu 2 cột **thiếu** → **chưa Reopen ngay**: gắn cờ **hai-bậc-trạng-thái** và gửi câu hỏi BA §9 câu (3), vì theo chữ `:1167` thì đợt chưa tới `DANG_LAP_BC` nên chưa phát sinh nghĩa vụ hiển thị ⇒ đây là **GAP đặc tả** (mô hình STT-52 tách 2 bậc, `:1167` chỉ nhắc 1 bậc), không phải lỗi dev thuần túy.
4. Muốn có phép đo sạch theo đúng chữ `:1167` thì phải đưa được **đợt** lên `DANG_LAP_BC` — đó chính là bug **`LBCKQTHCT_01`** (Open). ⇒ **Đo LBCKQTHCT_01 trước.** Đường dựng: `POST /api/v1/dot-bao-caos/{id}/start`, `GET` lấy `version` trước mỗi bước (sai `version` = lỗi xung đột, **không phải bug**).

🟡 **Cảnh báo dữ liệu rỗng (riêng case 03/04).** Kiểm kê ghi nhận phản hồi chi tiết đợt **có** trường cấp cao nhất **`soLieuKyTruoc`**, đang **`null`** ở đợt #2. ⇒ Nếu giao diện **ẩn cột khi không có dữ liệu**, ta sẽ thấy "thiếu cột" trong khi thật ra là **thiếu dữ liệu**. **"Cột không hiện vì rỗng" KHÁC HẲN "cột không tồn tại"** — xem bẫy 10.

---

## 5. Các bước đo (giao diện thật — Giai đoạn B)

0. **Ghi dấu vân tay bản dựng TRƯỚC khi đo:** tải lại trang **bằng địa chỉ** (không dùng tab đang mở), ghi tên bó mã FE + `last-modified` + `etag`. Kỳ vọng `assets/index-DsMHK7Dp.js` (07/08/2026 01:51) — **khác đi thì ghi lại giá trị thực**.
1. Đăng nhập **`cbnv_dp_01`**. Khai account thực dùng nếu phải fallback.
2. Menu trái → **"Đợt báo cáo"**. Chụp danh sách: mã đợt · **biểu mẫu** · **trạng thái** của từng đợt.
3. Chọn đợt thỏa **cả 4 điều kiện §4.3** → bấm **Xem** → vào `/ct-htpldn/dot-bao-cao/{id}`.
4. **Chốt định danh vào báo cáo trước khi kết luận:** `mã đợt` · `bieuMauSuDung` · `trangThai đợt` · `trangThaiNop của đơn vị`. Thiếu 1 trong 4 ⇒ **chưa được ra verdict**.
5. Cuộn tới **bảng biểu mẫu 21a**. **Cuộn NGANG hết bảng** (bảng 13 dòng chỉ tiêu thường có thanh cuộn ngang riêng) và **mở mọi accordion/section thu gọn** trước khi kết luận "không có".
6. Đọc **hàng tiêu đề** của bảng 21a: ghi lại **đủ danh sách tiêu đề cột theo đúng thứ tự** + **số cột**.
7. Chạy **đường đo thứ hai** (§6) trên **chính đợt đó**.
8. **Lặp bước 3–7 trên đợt thứ hai** (khác kỳ, cùng trạng thái) để loại khả năng "một bản ghi hỏng cá biệt". Nếu chỉ dựng được 1 đợt → **khai rõ** trong kết quả.

---

## 6. Đường đo thứ hai (đối chứng độc lập — bắt buộc)

**6a — Đọc DOM bằng `innerText` (KHÔNG `textContent`; `textContent` gom cả node ẩn → bug ma):**

```js
() => [...document.querySelectorAll('table')].map((t, i) => ({
  i,
  nhan_gan_nhat: (t.closest('section,[class*="card"],[class*="Card"]')
      ?.querySelector('h1,h2,h3,h4,legend,[class*="title"]')?.innerText || '').trim().slice(0, 80),
  so_cot_header: t.querySelector('thead tr')?.children.length ?? null,
  tieu_de_cot: [...t.querySelectorAll('thead th')].map(th => th.innerText.trim()),
  so_dong_body: t.querySelectorAll('tbody tr').length,
  // chống kết luận "không có" khi cột bị đẩy ra ngoài khung nhìn:
  cuon_ngang: (() => { const b = t.closest('[class*="table-body"],[style*="overflow"]') || t.parentElement;
      return b ? { scrollWidth: b.scrollWidth, clientWidth: b.clientWidth, bi_cat: b.scrollWidth > b.clientWidth } : null; })()
}))
```
Bảng 21a nhận diện bằng: `so_dong_body` ≈ **13 chỉ tiêu** (`:802`) và/hoặc nhãn gần nhất chứa "21a".

**6b — Đọc thẳng dữ liệu nguồn:** `GET /api/v1/dot-bao-caos/{id}` bằng **chính phiên đăng nhập `cbnv_dp_01`** (cookie-auth trong tab đang đăng nhập; hoặc Bearer token lấy theo §"Cách lấy phiên" của [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) — env **có bước mã xác thực**, trường đăng nhập là `username`/`password`). **In cả khóa cấp cao nhất LẪN khóa bên trong `soLieuTongHop`:**

```js
async (id) => { const r = await fetch(`/api/v1/dot-bao-caos/${id}`, {credentials:'include'});
  const j = await r.json(); const d = j.data ?? j;
  const s = d.baoCao?.soLieuTongHop ?? d.soLieuTongHop ?? null;
  return { trangThai: d.trangThai, trangThaiNop: d.trangThaiNop, bieuMauSuDung: d.bieuMauSuDung,
           khoa_cap_cao_nhat: Object.keys(d),                    // kiểm kê thấy có soLieuKyTruoc ở đây
           soLieuKyTruoc: d.soLieuKyTruoc ?? d.baoCao?.soLieuKyTruoc ?? '(khong co khoa)',
           khoa_trong_soLieuTongHop: s && Object.keys(s), mau_1_phan_tu: s && Object.values(s)[0] }; }
```
🔴 **CẤM đoán tên khóa** — in ra xem rồi mới đối chiếu. Hai cột tranh chấp có thể nằm ở **hai chỗ**: `soLieuKyTruoc` là trường **cấp cao nhất** (kiểm kê 07/08 xác nhận có, giá trị `null`), còn ghi chú theo chỉ tiêu nhiều khả năng nằm **bên trong** `soLieuTongHop` (object tự do).
🟡 **`soLieuKyTruoc = null` là dữ liệu rỗng, KHÔNG phải bằng chứng thiếu cột** — xem bẫy 10.

**Hai đường khớp → dừng, không thêm đường thứ ba. Hai đường mâu thuẫn → CHƯA ĐƯỢC CHỐT**, ghi cả hai vào kết quả và hỏi lại.

---

## 7. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi: trên màn Chi tiết đợt báo cáo của một đợt ở DANG_LAP_BC có áp dụng mẫu 21a,
   bảng biểu mẫu 21a cho cán bộ (a) thấy được SỐ LIỆU CỦA KỲ TRƯỚC ứng với từng chỉ tiêu, VÀ
   (b) có chỗ GHI CHÚ riêng cho từng chỉ tiêu — đúng ở CẢ HAI đường đo (giao diện + dữ liệu nguồn),
   và lặp lại được trên ít nhất 2 đợt khác nhau (nếu env chỉ dựng được 1 thì khai rõ).

❌ FAIL nếu: ở đúng tiền đề trên, bảng 21a KHÔNG có chỗ nào cho cán bộ đọc số liệu kỳ trước,
   hoặc KHÔNG có chỗ ghi chú theo từng chỉ tiêu — sau khi ĐÃ cuộn ngang hết bảng và mở hết
   phần thu gọn. Thiếu 1 trong 2 vẫn là FAIL (fix một nửa vẫn FAIL), nhưng phải ghi rõ thiếu vế nào.

🚫 KHÔNG ĐO ĐƯỢC (ô TRỐNG + nêu blocker, CẤM chấm FAIL): không đưa được đợt nào về DANG_LAP_BC
   (dep bug LBCKQTHCT_01), hoặc không có đợt nào áp dụng mẫu 21a.
```

---

## 8. ⚠️ Bẫy — rule chống kết luận oan

1. **Bẫy trạng thái đợt (nguy hiểm nhất).** `:1167` ràng buộc hiển thị **"khi bieu mau ap dung va dot o DANG_LAP_BC"**. Mở màn ở `TAO_DOT` mà thấy thiếu cột thì **KHÔNG kết luận được gì** — SRS im lặng về trạng thái đó (vế **C3 = GAP**). Bằng chứng tuần 4 cho thấy giao diện **vẫn vẽ biểu mẫu 21a đủ 13 chỉ tiêu ngay ở `TAO_DOT`** ⇒ rất dễ chụp nhầm màn read-only rồi chấm FAIL oan.
2. **Bẫy "không thấy = không có".** Cột có thể bị đẩy ra ngoài khung nhìn sau **thanh cuộn ngang** của bảng, hoặc nằm trong **accordion/section thu gọn**. Bắt buộc kiểm `scrollWidth > clientWidth` (§6a) trước khi kết luận.
3. **Bẫy 3 chữ "Ghi chú" khác nhau.** SRS có **3** chỗ mang chữ này: `:1158` ô Ghi chú của **modal tạo đợt** · `:1369` `DOT_BAO_CAO.ghi_chu` = ghi chú **của đợt** · `:1167` **cột Ghi chú trong bảng 21a** ← **chỉ chỗ này** thuộc case. Thấy "Ghi chú" ở thẻ thông tin đợt (`:1165`) mà chấm PASS = **Pass oan**.
4. **Bẫy "Số liệu kỳ trước" ≠ "Kỳ báo cáo"/"Khoảng thời gian".** Thẻ thông tin đợt (`:1165`) có `Ky / Khoang TG` — đó là **kỳ của đợt**, không phải **số liệu của kỳ trước**.
5. **Bẫy câu chữ.** Dev có quyền đặt tên khác ("Kỳ trước", "Số liệu kỳ báo cáo trước", "Ghi chú/Diễn giải"…). **KHÔNG FAIL vì câu chữ** — chỉ FAIL khi **không chỗ nào** cho cán bộ đọc số liệu kỳ trước / ghi chú theo chỉ tiêu. (Describe requirement, not implementation.)
6. **CẤM suy chéo case.** LBCKQTHCT_03/04/05/06 soi **4 phần khác nhau của cùng 1 màn**. Đo 21a xong **KHÔNG** được suy cho 21b (case 04), khối nhận xét (05), khối truy vết (06). Mỗi case một phép đo riêng.
7. **Bẫy bản dựng cũ trong tab.** Tab MCP mở lâu vẫn chạy bó mã cũ — đã gây Reopen oan 01/08. Tải lại bằng địa chỉ + ghi tên bó mã.
8. **Bẫy mẫu giấy.** Nếu dev/BA viện Phụ lục D.1.2 (`srs-v3.5.md:6577–6599`, mẫu 21a giấy chỉ 13 cột) để nói "không cần 2 cột" → đó là **bất đồng đặc tả giữa 2 tầng**, chuyển BA; **không** tự đổi verdict.
9. **Giới hạn hiệu lực.** Verdict chỉ có giá trị cho env nội bộ `18.143.165.120.nip.io` + bó mã đo được. Bằng chứng gốc của đối tác quay trên môi trường khác — **phải ghi câu giới hạn này trong kết quả**.
10. 🟡 **Bẫy "cột ẩn vì dữ liệu rỗng" (mới, từ kiểm kê 07/08).** Trường `soLieuKyTruoc` **tồn tại** ở cấp cao nhất của phản hồi chi tiết đợt nhưng đang **`null`**. Nhiều giao diện **ẩn cột khi cả cột không có dữ liệu**. ⇒ Thấy thiếu cột mà chưa kiểm giá trị = có thể **FAIL oan**. **Bắt buộc**: (a) chạy §6b đọc `soLieuKyTruoc` trước; (b) nếu `null` thì **nhập thử số liệu vào 1 chỉ tiêu rồi Lưu nháp** và quét lại — cột xuất hiện sau khi có dữ liệu ⇒ **PASS** (kèm ghi nhận hành vi ẩn-khi-rỗng làm candidate, không kéo verdict). Chỉ FAIL khi **có dữ liệu mà vẫn không chỗ nào đọc được**.
11. 🔴 **Bẫy hai bậc trạng thái.** `trangThai` (**đợt**, `:1368`) và `trangThaiNop` (**đơn vị**, `:1389`) là hai trường khác nhau; `DANG_LAP` **không phải** `DANG_LAP_BC`. `:1167` neo vào bậc **đợt**. Env: cả 3 đợt `TAO_DOT`, đơn vị `DANG_LAP`. **Ghi cả hai bậc vào kết quả**; thiếu cột trong tình huống này → gắn cờ GAP + BA §9 câu (3), **không Reopen thẳng** (xem §4.3).

---

## 9. Nếu phát sinh GAP/DIFF khi đo — soạn sẵn

**Chỉ dùng cho vế C3** (điều kiện hiển thị ngoài `DANG_LAP_BC`), hoặc khi dev viện mẫu giấy Phụ lục D:

```
CẦN BA CONFIRM: đối tác kỳ vọng bảng biểu mẫu 21a trên màn Chi tiết đợt báo cáo luôn cho cán bộ
thấy số liệu kỳ trước và chỗ ghi chú theo từng chỉ tiêu (phiếu neo vào "thiết kế").
SRS quy định srs-fr-15-ct-htpldn.md:1167 — bảng 21a gồm "Chi tieu / So lieu ky truoc / Ky nay /
Ghi chu", nhưng điều kiện hiển thị chỉ ghi "khi bieu mau ap dung va dot o DANG_LAP_BC"; SRS
IM LẶNG về nội dung màn khi đợt ở TAO_DOT / CHO_DUYET_KQ / DA_DUYET_KQ / DA_GUI_TW / DA_TONG_HOP.
Ngoài ra srs-v3.5.md:6577-6599 (Phụ lục D.1.2, mẫu 21a văn bản xuất) chỉ có 13 cột chỉ tiêu,
không có hai cột này — hai chỗ thuộc hai tầng khác nhau (form nhập trên màn vs mẫu văn bản xuất).
Web/dev hiện tại: <chờ đo>.

Câu hỏi BA:
(1) Khi đợt KHÔNG ở DANG_LAP_BC, màn Chi tiết đợt báo cáo có phải hiển thị bảng 21a ở dạng chỉ đọc
    (kèm số liệu kỳ trước + ghi chú) hay không hiển thị? Đề nghị bổ sung điều kiện hiển thị cho các
    trạng thái còn lại vào dòng #37 của bảng thành phần màn hình.
(2) Xác nhận "Số liệu kỳ trước" và "Ghi chú" là thành phần của FORM NHẬP trên màn (không thuộc mẫu
    văn bản xuất TT17), để dev và đối tác không chấm bằng hai thước khác nhau.
(3) Mô hình STT-52 tách hai bậc trạng thái — cấp ĐỢT (:1368, có DANG_LAP_BC) và cấp ĐƠN VỊ NỘP
    (:1389, có DANG_LAP). Điều kiện hiển thị ở dòng #37 chỉ nhắc "dot o DANG_LAP_BC". Đợt là bản ghi
    toàn quốc dùng chung cho ~70 đơn vị, nên nếu neo vào bậc đợt thì một đơn vị đang lập báo cáo vẫn
    có thể không được hiển thị biểu mẫu. Đề nghị BA chốt: điều kiện hiển thị biểu mẫu 21a nên neo
    vào trạng thái NỘP CỦA ĐƠN VỊ (DANG_LAP) hay trạng thái của ĐỢT (DANG_LAP_BC)?
Mục đích: BỔ SUNG vào đặc tả màn hình — KHÔNG chặn bàn giao.
```

---

## 10. Ghi nhận về bằng chứng đối tác

- Case này dùng **video** `LBCKQTHCT_03.webm` (khác 3 case còn lại dùng ảnh tĩnh) ⇒ có thể đọc được **trạng thái đợt** và **thao tác cuộn** trong video — hai thứ quyết định bẫy 1 và bẫy 2. **Yêu cầu agent BẰNG-CHỨNG trả lời rõ 2 câu:** (a) đợt trong video ở trạng thái nào? (b) người quay có cuộn ngang hết bảng 21a không?
- Nếu video cho thấy đợt ở `TAO_DOT` ⇒ quan sát của đối tác **vẫn có thể đúng về bề mặt** nhưng **chưa đủ để chấm FAIL theo `:1167`** — phải đo lại ở `DANG_LAP_BC`.
