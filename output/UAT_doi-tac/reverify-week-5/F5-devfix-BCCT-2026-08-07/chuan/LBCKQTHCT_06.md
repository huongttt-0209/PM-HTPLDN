# Chuẩn chấm đã khóa — LBCKQTHCT_06 (dòng 339) — Chi tiết đợt báo cáo · **Khối truy vết chương trình liên quan (tùy chọn)**

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

**Phần màn hình bị soi:** **Khối truy vết chương trình liên quan (tùy chọn)**.
**Kết quả thực tế đối tác:** *"Màn hình Chi tiết **không có Khối truy vết chương trình liên quan**"*.
**Bằng chứng:** `partner-evidence/LBCKQTHCT_06.jpg`.

> 🔴 **`LBCKQTHCT_06.jpg` và `LBCKQTHCT_05.jpg` là CÙNG MỘT FILE** — md5 `c0fb9837447ee90ac8c8f975a298aaef` (đã kiểm). Đối tác dùng **1 ảnh cho 2 claim khác nhau về 2 khối khác nhau**. Hệ quả xử lý: xem §10.

---

## 2. BẢNG SCOPE LOCK (khóa quan hệ từng vế)

**🔴 Đây là case duy nhất trong 4 case bị TÁCH LÀM 2 QUAN HỆ KHÁC NHAU.** Không gộp — gộp là chấm oan một chiều.

| # | Expected đối tác (vế đang tranh chấp) | SRS — file:dòng | Nguyên văn dòng SRS (≤200 ký tự) | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|---|
| **C1** | Khi lập BC, cán bộ phải **chọn được các chương trình HTPL đơn vị đã triển khai trong kỳ** để truy vết (không bắt buộc điền) | `srs-fr-15-ct-htpldn.md:732` (Input #9 của FR-XI-06) + `:744` (Processing bước 6) + `:707` (gắn màn) | `:732` = `\| 9 \| ct_htpl_ids_lien_quan[] \| identifier[] \| N \| **THÊM MỚI (STT 52):** Multi-select FK → CHUONG_TRINH_HTPL — truy vết các CT đơn vị đã triển khai trong kỳ (tham khảo, không bắt buộc) \| — \| **Chọn** \|` | **MATCH** (SRS gọi **đích danh**, khai nguồn nhập là **"Chọn"** ⇒ phải có chỗ chọn trên màn) | **TEST** | (a) UI: tìm ô chọn nhiều giá trị + nhãn quanh nó · (b) `GET /api/v1/dot-bao-caos/{id}` đọc lại giá trị đã chọn |
| **C2** | Nó phải là một **KHỐI riêng được khai trong bảng thành phần màn hình** của màn Chi tiết đợt BC | Bảng `:1163–1175` (dòng #35 → #45) | **IM LẶNG** — đọc trọn 11 dòng, **không dòng nào** nhắc chương trình liên quan / truy vết. Dòng gần nhất đã đọc: `:1169` = `\| 39 \| form \| Nhan xet kien nghi \| textarea \| Max 5000 ky tu \| input \| khi dot o DANG_LAP_BC \|` và `:1170` = `\| 40 \| action-bar \| [DANG_LAP_BC] Hanh dong lap BC …` | **GAP** | **BA** | — (không đo được thành verdict) |
| **C3** | Chương trình đã chọn phải **được lưu và đọc lại được** trên báo cáo | `:745` + `:1417` | `:745` = `\| 7 \| Lưu bản ghi BAO_CAO_CT_HTPL … với dot_id + don_vi_nop_id + ct_htpl_ids_lien_quan[] \| — \|` · `:1417` = `\| 11 \| ct_htpl_ids_lien_quan[] \| identifier[] \| N \| … Mảng FK → CHUONG_TRINH_HTPL(id) — truy vết các CT đơn vị đã triển khai trong kỳ …\|` | **MATCH** | **TEST** | Nhập qua UI → tải lại trang → đọc lại (§6) |
| **C4** | *(điều kiện hiển thị)* Khối hiện **mọi lúc** khi mở Chi tiết đợt BC | Bảng `:1163–1175` | **IM LẶNG** (không có dòng nên cũng không có cột "Dieu kien hien thi"). Suy theo `:744` thì thuộc bước **lập BC** ⇒ ngữ cảnh `DANG_LAP_BC` | **GAP** | **BA** | — |

**Vế trong KQMĐ chung nhưng đối tác KHÔNG nêu ở Kết quả thực tế** (tràn/đè · đồng nhất ngôn ngữ): **không kéo verdict**. Thấy thì log bug riêng.

---

## 3. Kết luận quan hệ + lý do (chống kết luận "SRS im lặng" ẩu)

**Đã đọc TRỌN, không grep suông:**

| Khoảng dòng đã đọc trọn | Nội dung | Kết quả |
|---|---|---|
| `:1088–1103` | Mở đầu §3 + Layout tổng quan SCR-XI-01, gồm **[BA-23 tuần 4, chốt 2026-07-30]** ở `:1103` | Đợt báo cáo là **màn độc lập** |
| `:1147–1159` | **Trọn** bảng thành phần màn "Dot bao cao dinh ky" (#30–#34) + ghi chú BA-23 `:1149` + `[CAN BA CHOT]` `:1151` | Màn **danh sách** — không có khối truy vết. Không phải màn bị soi |
| **`:1161–1175`** | **TRỌN 11 dòng** bảng **"Chi tiet Dot BC: Lap & Phe duyet & Gui TW"** (#35 Thông tin đợt · #36 Thanh tiến trình · #37 Biểu mẫu 21a · #38 Biểu mẫu 21b · #39 Nhận xét kiến nghị · #40 Hành động lập BC · #41 Phê duyệt BC · #42 Từ chối BC · #43 Gửi TW · #44 [TW] Bảng BC từ BN/ĐP · #45 [TW] Tổng hợp) | 🔴 **KHÔNG dòng nào** khai khối chương trình liên quan / truy vết ⇒ **bảng thành phần màn hình IM LẶNG** (vế C2) |
| `:1177–1233` | Trọn 3 bảng phụ (nhãn SM-KH-CTHTPL · nhãn SM-DOT-BC · hành động theo trạng thái CT) + **trọn** §"Quy tac tuong tac" (`:1217–1232`) | 16 quy tắc tương tác — **không** quy tắc nào nhắc CT liên quan ⇒ đã loại khả năng "khối được khai ở chỗ khác trong §3" |
| `:701–771` | **Trọn** FR-XI-06 — Inputs `:722–733`, Processing `:737–747`, Outputs, Postconditions, AC | `:732` khai `ct_htpl_ids_lien_quan[]` là **Input #9**, nguồn nhập ghi rõ **"Chọn"**; `:744` bước 6 khai thao tác **"có thể chọn `ct_htpl_ids_lien_quan[]` để truy vết"**; `:745` bước 7 lưu vào bản ghi; `:707` gắn chức năng này vào **SCR-XI-01** |
| `:1400–1422` | Trọn entity BAO_CAO_CT_HTPL | `:1417` khai trường mảng FK, mặc định `[]`, mô tả **"Các CT liên quan trong kỳ"** |

**Đã grep những từ khóa nào (TOÀN thư mục `srs-v3.5/`, cả bản có dấu và bản không dấu):**

| Từ khóa | Kết quả |
|---|---|
| `ct_htpl_ids_lien_quan` | **đúng 4 hit, toàn bộ nằm trong `srs-fr-15`: `:732` · `:744` · `:745` · `:1417`.** **Không hit nào nằm trong một bảng thành phần màn hình** |
| `truy vết` · `truy vet` | `srs-fr-15:732` `:744` `:1417`; còn lại là "ma trận truy vết" của master (`srs-v3.5.md:306` `:5144` `:5471` — nghĩa khác hoàn toàn) |
| `chương trình liên quan` · `chuong trinh lien quan` · `CT liên quan` | **0 hit** ngoài `:1417` ("Các CT liên quan trong kỳ" — cột Mô tả của entity) |
| `Multi-select` | `:646` (`pham_vi_don_vi_nop_ids[]` của FR-XI-05a) · `:732` (chính vế này). Cả hai đều là Input của FR, **không** dòng nào trong bảng màn hình |

**⇒ Kết luận — 2 quan hệ, phải giữ TÁCH:**

- **C1 + C3 = MATCH → route TEST.** SRS gọi **đích danh** `ct_htpl_ids_lien_quan[]`, mô tả nó là **"Multi-select FK → CHUONG_TRINH_HTPL — truy vết các CT đơn vị đã triển khai trong kỳ"**, cột **Nguồn** ghi **"Chọn"** (`:732`), và Processing bước 6 (`:744`) khai đó là **thao tác của cán bộ trong lúc lập BC**. FR-XI-06 gắn vào **SCR-XI-01** (`:707`), mà phần lập BC của SCR-XI-01 chính là bảng `:1161–1175` (dòng #40 ghi rõ *"gop tu MH-15.6"* = FR-XI-06). ⇒ Yêu cầu nghiệp vụ *"cán bộ chọn được các CT liên quan trên màn lập BC"* **có căn cứ SRS đích danh**, không phải suy từ "thiết kế". Đo được rằng không chỗ nào chọn được → **Reopen hợp lệ**.
- **C2 (+ C4) = GAP → route BA.** Bảng thành phần màn hình — nơi đặc tả *hình dạng* màn — **im lặng hoàn toàn**: không có dòng #46 nào cho khối này, nên cũng **không có** quy định nó phải là "một khối riêng", đặt ở đâu, hiện ở trạng thái nào, hay hiển thị dạng gì. ⇒ **KHÔNG được tự suy "SRS không nói = không cần"** (đó cũng là GAP, không phải "Không phải lỗi"), và **KHÔNG được tự suy "thiếu khối = lỗi"** ở tầng hình dạng. Đây là chỗ **bổ sung đặc tả**, không phải chỗ chặn bàn giao.

**Manh mối tầng dữ liệu (chỉ là manh mối, KHÔNG phải căn cứ verdict):** `00-CHUAN-BI-CHUNG.md §3` cho thấy `UpdateSoLieuDto` **có** `ctHtplIdsLienQuan: string[]`. ⇒ hệ thống **có chỗ chứa** và **có đường nhận** dữ liệu này; nếu giao diện không có chỗ chọn thì nhiều khả năng thiếu ở tầng giao diện. Nhưng **có trường trong DTO ≠ đặc tả yêu cầu hiển thị** — quan hệ vẫn khóa bằng dòng SRS.
⚠️ Lưu ý ngược lại rất quan trọng: `LapBaoCaoDto` (bước bắt đầu lập) **không** có `ctHtplIdsLienQuan`, chỉ `UpdateSoLieuDto` (bước cập nhật số liệu) mới có ⇒ **khối này có thể chỉ xuất hiện ở bước cập nhật/sửa số liệu, không ở màn vừa mở**. Đây là bẫy đo, xem §8 bẫy 2.

---

## 4. Precondition (chưa đo)

### 4.1 Vai trò / tài khoản

| Vai trò | Tài khoản | Mật khẩu | Vì sao |
|---|---|---|---|
| **Người ra verdict** — CB Nghiệp vụ cấp ĐP | **`cbnv_dp_01`** (`donViId 00000000-0000-4000-8002-000000000006`, `capDonVi = DP`) | `Test@1234` | `:712` — tác nhân FR-XI-06 là **"CB Nghiệp vụ cấp ĐP/BN (đơn vị thuộc phạm vi đợt BC)"** |
| Fallback Rule 7 | `cbnv_dp_02` → `cbnv_dp_03` (**cùng vai trò + cùng cấp**) | `Test@1234` | ⚠️ `cbnv_dp` (không hậu tố) **login FAIL 401** từ 03/08 (`input/input.md:31-33`) |
| **CẤM ra verdict** | `cbnv_tw*` | — | `:712` — **TW không tự lập BC** ⇒ sai tác nhân |
| **CẤM ra verdict** | `admin` / `Secret@123` | — | Quyền rộng che lỗi phân quyền; chỉ tra định danh và **phải khai** |

### 4.2 Màn / đường dẫn
Menu trái **"Đợt báo cáo"** → `/ct-htpldn/dot-bao-cao` → bấm **Xem** → **`/ct-htpldn/dot-bao-cao/{id}`**. Nhóm endpoint đúng: **`/api/v1/dot-bao-caos/...`** (số nhiều, có `dot-`).

### 4.3 Trạng thái dữ liệu bắt buộc

| # | Điều kiện | SRS | Cách kiểm |
|---|---|---|---|
| 1 | Đơn vị của tài khoản trong `pham_vi_don_vi_nop_ids[]` | `:717` | `GET /api/v1/dot-bao-caos/{id}` |
| 2 | Bản ghi nộp ở **CHUA_NOP** / **DANG_LAP** | `:718` | cùng lệnh |
| 3 | 🔴 Đợt ở **`DANG_LAP_BC`** (bối cảnh của Processing bước 6, `:744`) | `:744` (bảng màn hình im lặng) | Thanh tiến trình 6 bước (`:1166`) / trường `trangThai` |
| 4 | 🔴 **Phải có ≥1 CHUONG_TRINH_HTPL để chọn** trong danh sách | `:732` (FK → CHUONG_TRINH_HTPL) | `GET /api/v1/chuong-trinh-htpls` — env phải có chương trình thuộc phạm vi đơn vị |

> ✅ **Không dính chặn seed biểu mẫu.** `:732`/`:744` không ràng buộc theo `bieu_mau_su_dung` ⇒ việc cả 3 đợt trong env đang là `MAU_21A` **không** ảnh hưởng case này (khác hẳn case 04).

🔴 **Chặn tiền đề — case này có 2 chặn:**

**Chặn 1 — hai bậc trạng thái.** Theo kiểm kê [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) (đo 2026-08-07), env có **3 đợt**, **cả 3 ở `trangThai = TAO_DOT`**; nhưng **`trangThaiNop` của `cbnv_dp_01` = `DANG_LAP`** trên đợt #2 (`DOT-SO_BO_NAM-2026-1`, `e9909d96-1391-463b-8072-b1b56c319f8e`) và #3 (`DOT-SO_BO_6_THANG-2026-1`, `a61e07f1-e205-4948-ad7d-a3ccac49830a`). Đợt #2 đã có `baoCaoId = c1b1045d-007c-4104-a169-e267010557a0`.
**Hai bậc là hai trường khác nhau, CẤM lẫn:** `DOT_BAO_CAO.trang_thai` (**cấp ĐỢT**, `:1368`, có `DANG_LAP_BC`) vs `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop` (**cấp ĐƠN VỊ**, `:1389`, có `DANG_LAP`).
⇒ Đo trên đợt #2/#3, **ghi cả hai bậc**; thiếu khối trong tình huống này → gắn cờ GAP + BA §9, **không Reopen thẳng**. Phép đo sạch cần đưa **đợt** lên `DANG_LAP_BC` = bug **`LBCKQTHCT_01`** (Open) ⇒ **đo LBCKQTHCT_01 trước**. Đường dựng: `POST /api/v1/dot-bao-caos/{id}/start`, `GET` lấy `version` trước mỗi bước (sai `version` = **lỗi xung đột, không phải bug**).

**Chặn 2 — danh sách nguồn có thể rỗng.** `:732` là **FK → CHUONG_TRINH_HTPL**. Env **không có chương trình nào** thuộc phạm vi đơn vị `cbnv_dp_01` ⇒ ô chọn (nếu có) sẽ **rỗng**, trông y hệt "không có khối". **"Danh sách rỗng" KHÔNG phải "không có khối"** — bắt buộc **đếm số CT khả dụng TRƯỚC** (§5 bước 1).

⇒ Không thỏa 3 hoặc 4 ⇒ **ô TRỐNG + nêu blocker (chặn 1 = nhóm E dep upstream · chặn 2 = nhóm A thiếu seed)**, **CẤM chấm FAIL**.

---

## 5. Các bước đo (giao diện thật — Giai đoạn B)

0. Tải lại trang **bằng địa chỉ**, ghi **tên bó mã FE + `last-modified` + `etag`** (kỳ vọng `assets/index-DsMHK7Dp.js`).
1. **Đếm nguồn TRƯỚC:** `GET /api/v1/chuong-trinh-htpls` bằng phiên `cbnv_dp_01` → ghi **số CT khả dụng**. Bằng 0 ⇒ dừng, ghi blocker seed (§4.3 chặn 2).
2. Đăng nhập **`cbnv_dp_01`** (khai account thực dùng nếu fallback).
3. Menu **"Đợt báo cáo"** → chọn đợt thỏa §4.3 → **Xem** → `/ct-htpldn/dot-bao-cao/{id}`.
4. **Chốt định danh trước khi kết luận:** `mã đợt` · `trangThai đợt` · `trangThaiNop của đơn vị` · **số CT khả dụng**.
5. **Quét lượt 1 — màn vừa mở:** cuộn hết chiều dọc, mở mọi accordion/section thu gọn/tab con, tìm ô cho phép **chọn nhiều chương trình**.
6. 🔴 **Quét lượt 2 — sau khi vào chế độ nhập số liệu.** Theo §3, đường nhận dữ liệu có `ctHtplIdsLienQuan` là bước **cập nhật số liệu**, không phải bước bắt đầu lập ⇒ **bắt buộc** bấm vào biểu mẫu / bấm [Lưu nháp] / mở chế độ sửa rồi **quét lại**. **Bỏ lượt 2 = kết luận thiếu cơ sở.**
7. Chạy **đường đo thứ hai** (§6) trên chính đợt đó.
8. Lặp trên **đợt thứ hai** nếu dựng được; không thì **khai rõ chỉ đo được 1 đợt**.

---

## 6. Đường đo thứ hai (đối chứng độc lập — bắt buộc)

**6a — Đọc DOM bằng `innerText` (KHÔNG `textContent`; `textContent` gom cả node ẩn → bug ma):** liệt kê **mọi ô chọn nhiều giá trị** trên màn kèm nhãn, và soát chuỗi liên quan trên toàn màn:

```js
() => {
  const nhan = el => {
    const id = el.id, lab = id && document.querySelector(`label[for="${CSS.escape(id)}"]`);
    return (lab?.innerText
      || el.closest('[class*="form-item"],[class*="field"],section,div')?.querySelector('label,legend,[class*="label"],h3,h4')?.innerText
      || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').trim().slice(0,80);
  };
  const chon = [...document.querySelectorAll(
      'select[multiple], [class*="select"][class*="multiple"], [role="combobox"], [class*="ant-select"]')]
    .map(el => ({ nhan: nhan(el), multi: /multiple|multi/i.test(el.className),
                  hien: !!(el.offsetWidth || el.offsetHeight), noi_dung: el.innerText.trim().slice(0,60) }));
  const t = document.body.innerText;      // innerText, KHÔNG textContent
  return { o_chon: chon,
           co_chu_chuong_trinh: /ch(ươ|uo)ng\s*tr(ì|i)nh/i.test(t),
           co_chu_lien_quan: /li[êe]n\s*quan/i.test(t),
           co_chu_truy_vet: /truy\s*v[ếe]t/i.test(t) };
}
```

**6b — Đọc thẳng dữ liệu nguồn:** `GET /api/v1/dot-bao-caos/{id}` bằng **chính phiên `cbnv_dp_01`** (cookie-auth trong tab đang đăng nhập; hoặc Bearer token theo §"Cách lấy phiên" của [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) — env **có bước mã xác thực**, trường đăng nhập là `username`/`password`) → in **khóa thật** của bản ghi báo cáo và giá trị hiện tại:

```js
async (id) => { const r = await fetch(`/api/v1/dot-bao-caos/${id}`, {credentials:'include'});
  const j = await r.json(); const d = j.data ?? j; const bc = d.baoCao ?? d;
  return { trangThai: d.trangThai, trangThaiNop: d.trangThaiNop,
           khoa_cap_cao_nhat: Object.keys(d), khoa_bao_cao: Object.keys(bc),
           khoa_ct_lien_quan: Object.keys(bc).filter(k => /ctHtpl|ct_htpl|lienQuan|lien_quan/i.test(k)),
           gia_tri: bc.ctHtplIdsLienQuan ?? null }; }
```
**Bắt buộc ghi kèm 2 bậc trạng thái** (`trangThai` + `trangThaiNop`) + **số CT khả dụng** làm bằng chứng tiền đề — thiếu thì verdict vô hiệu.
🔴 **CẤM đoán tên khóa** — in ra rồi mới đối chiếu.

**Phép thử quyết định (chỉ chạy khi UI CÓ ô chọn):** chọn **đúng 1 chương trình đã biết mã** → Lưu nháp → **tải lại trang bằng địa chỉ** → đọc lại cả trên màn lẫn ở đường 6b. Đọc lại đúng chương trình đã chọn ⇒ C1 + C3 đạt.

**Hai đường khớp → dừng. Hai đường mâu thuẫn → CHƯA ĐƯỢC CHỐT**, ghi cả hai + hỏi lại.

---

## 7. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi (vế C1 + C3): trên màn Chi tiết đợt báo cáo của một đợt ở DANG_LAP_BC, cán bộ CHỌN
   ĐƯỢC một hoặc nhiều chương trình HTPL để truy vết cho báo cáo kỳ đó (ô chọn nhiều giá trị,
   nhãn quanh nó cho biết đó là chương trình liên quan), VÀ lựa chọn đó lưu lại + đọc lại được
   sau khi tải lại trang. Đúng ở CẢ HAI đường đo.
   Chỉ cần chọn được — KHÔNG đòi hệ thống bắt buộc điền (SRS :732 ghi rõ "không bắt buộc").

❌ FAIL nếu (vế C1): ở đúng tiền đề trên, và ĐÃ quét cả lượt 1 (màn vừa mở) lẫn lượt 2 (chế độ
   nhập số liệu), KHÔNG chỗ nào cho cán bộ chọn chương trình liên quan.
   Cũng FAIL nếu chọn được nhưng lựa chọn KHÔNG lưu / không đọc lại được sau khi tải lại (vế C3) —
   ghi rõ đây là biến thể nào.

⚠️ KHÔNG chấm FAIL cho vế C2/C4 (hình dạng khối + điều kiện hiển thị): bảng thành phần màn hình
   IM LẶNG ⇒ GAP ⇒ nêu BA confirm theo §9, KHÔNG Reopen vì lý do "phải là một khối riêng".

🚫 KHÔNG ĐO ĐƯỢC (ô TRỐNG + nêu blocker, CẤM chấm FAIL):
   - không đưa được đợt về DANG_LAP_BC → nhóm E (dep bug LBCKQTHCT_01)
   - không có chương trình HTPL nào khả dụng để chọn → nhóm A (thiếu seed)
```

---

## 8. ⚠️ Bẫy — rule chống kết luận oan

1. **Bẫy "không bắt buộc ⇒ không cần làm".** `:732` ghi `Bắt buộc = N` và *"tham khảo, không bắt buộc"* — đó là nói **dữ liệu không bắt buộc ĐIỀN**, **không** phải "chỗ chọn không bắt buộc CÓ". Chính phiếu đối tác cũng ghi **"(tùy chọn)"**. Dev viện "không bắt buộc" để nói không cần làm = **hiểu sai dòng**; nếu vẫn tranh chấp thì chuyển BA, **không** tự chấm "Không phải lỗi".
2. **Bẫy quét thiếu lượt 2 (riêng case này).** Đường nhận dữ liệu có `ctHtplIdsLienQuan` là **bước cập nhật số liệu**, không phải bước bắt đầu lập ⇒ khối rất có thể **chỉ hiện sau khi vào chế độ nhập/sửa số liệu**. Quét mỗi màn vừa mở rồi kết luận "không có" = **FAIL oan**. **Bắt buộc 2 lượt quét** (§5 bước 5 + 6).
3. **Bẫy "danh sách rỗng ≠ không có khối".** `:732` là FK → CHUONG_TRINH_HTPL. Env không có CT thuộc phạm vi đơn vị ⇒ ô chọn rỗng, trông như không có. **Đếm số CT khả dụng TRƯỚC** (§5 bước 1). Ô chọn rỗng vì thiếu dữ liệu = **thiếu seed (nhóm A)**, không phải bug hiển thị.
4. **Bẫy trạng thái đợt.** Bảng màn hình im lặng, nhưng `:744` đặt thao tác này trong bước **lập BC** ⇒ đo ở `TAO_DOT` mà thấy thiếu thì **không kết luận được** (vế **C4 = GAP**). Giao diện ở `TAO_DOT` **trông rất giống** màn đang lập (đã vẽ sẵn biểu mẫu 21a) ⇒ cực dễ chụp nhầm.
5. **Bẫy nhầm với "Chương trình" ở chỗ khác.** Màn danh sách CT (`/ct-htpldn`) và cột "Số đợt BC" (`:1115`) đều nói về chương trình nhưng **không phải** khối truy vết trên báo cáo. Thấy chữ "Chương trình" trên breadcrumb / menu mà chấm PASS = **Pass oan**.
6. **Bẫy nhầm chiều liên kết.** `:1115` cột "So dot BC" là **CT → đếm đợt**; vế này là **BC của đơn vị → chọn nhiều CT**. Hai chiều ngược nhau — không thay thế nhau.
7. **Bẫy câu chữ.** Dev có quyền đặt nhãn khác ("Chương trình liên quan", "CT đã triển khai trong kỳ", "Chương trình tham chiếu"…). **KHÔNG FAIL vì câu chữ** — chỉ FAIL khi **không chỗ nào** chọn được chương trình. Ngược lại **không PASS** chỉ vì thấy chữ "chương trình" mà **không có ô chọn**.
8. **CẤM suy chéo case.** 4 case soi **4 phần khác nhau của cùng 1 màn**; **case 05 dùng CHUNG file ảnh với case này** ⇒ nguy cơ copy verdict cao nhất trong lô. Mỗi case phải có **phép đo riêng + ảnh riêng do QA tự chụp**.
9. **Bẫy bản dựng cũ trong tab.** Tải lại bằng địa chỉ + ghi tên bó mã.
10. **Giới hạn hiệu lực.** Verdict chỉ có giá trị cho env nội bộ `18.143.165.120.nip.io` + bó mã đo được; bằng chứng gốc của đối tác quay trên môi trường khác — **ghi câu giới hạn này trong kết quả**.
11. 🔴 **Bẫy hai bậc trạng thái (mới, từ kiểm kê 07/08).** `trangThai` (**đợt**, `:1368`, có `DANG_LAP_BC`) ≠ `trangThaiNop` (**đơn vị**, `:1389`, có `DANG_LAP`). Bảng màn hình im lặng nên `:744` là mốc duy nhất, và nó đặt thao tác trong pha lập BC. Env: cả 3 đợt `TAO_DOT`, đơn vị `DANG_LAP`. **Ghi cả hai bậc vào kết quả**; thiếu khối trong tình huống này → gắn cờ GAP + BA §9, **không Reopen thẳng** (xem §4.3 chặn 1).

---

## 9. Soạn sẵn — CẦN BA CONFIRM (BẮT BUỘC gửi, vì C2/C4 = GAP dù C1 đo ra sao)

```
CẦN BA CONFIRM: đối tác kỳ vọng màn Chi tiết đợt báo cáo có "Khối truy vết chương trình liên quan
(tùy chọn)" (phiếu neo vào "thiết kế").
SRS quy định: srs-fr-15-ct-htpldn.md:732 khai ct_htpl_ids_lien_quan[] là Input #9 của FR-XI-06,
"Multi-select FK → CHUONG_TRINH_HTPL — truy vết các CT đơn vị đã triển khai trong kỳ (tham khảo,
không bắt buộc)", cột Nguồn ghi "Chọn"; :744 bước 6 khai cán bộ "có thể chọn ct_htpl_ids_lien_quan[]
để truy vết"; :745 lưu vào BAO_CAO_CT_HTPL; :1417 khai trường ở entity.
NHƯNG bảng thành phần màn hình của chính màn này (:1163–1175, dòng #35 → #45) IM LẶNG — không có
dòng nào cho khối này, nên không có quy định về hình dạng, vị trí, hay điều kiện hiển thị của nó.
Web/dev hiện tại: <chờ đo>.

Câu hỏi BA:
(1) Đề nghị BỔ SUNG một dòng vào bảng thành phần màn hình "Chi tiet Dot BC" cho khối truy vết
    chương trình liên quan: đặt ở vùng nào, dạng gì, và hiển thị ở những trạng thái đợt nào —
    hay xác nhận khối này KHÔNG thuộc phạm vi màn Chi tiết đợt báo cáo (khi đó nêu rõ cán bộ nhập
    ct_htpl_ids_lien_quan[] ở đâu, vì :732 và :744 đang yêu cầu cán bộ chọn được).
(2) Nếu thuộc phạm vi: khối hiện ngay khi mở màn, hay chỉ khi cán bộ vào chế độ nhập/sửa số liệu?
(3) Mô hình STT-52 tách hai bậc trạng thái — cấp ĐỢT (:1368, có DANG_LAP_BC) và cấp ĐƠN VỊ NỘP
    (:1389, có DANG_LAP). Khi bổ sung dòng cho khối này, đề nghị BA ghi rõ điều kiện hiển thị neo
    vào bậc nào — vì đợt là bản ghi toàn quốc dùng chung cho ~70 đơn vị.
Mục đích: BỔ SUNG vào đặc tả màn hình — KHÔNG chặn bàn giao.
```

> **Cách ghi verdict khi C1 và C2 lệch nhau** (rất dễ xảy ra ở case này): dùng **đa-trạng thái**.
> Ví dụ đo ra không chọn được chương trình ở đâu cả ⇒ ghi **"Open, BA confirm"** — Open cho vế C1
> (`:732`/`:744` yêu cầu cán bộ chọn được), BA confirm cho vế C2/C4 (bảng thành phần màn hình im lặng).
> Ngược lại nếu chọn được ⇒ vế C1 đạt, **vẫn gửi câu hỏi BA** cho C2/C4.

---

## 10. Ghi nhận về bằng chứng đối tác — **1 ảnh dùng cho 2 claim**

- `LBCKQTHCT_06.jpg` **trùng md5** với `LBCKQTHCT_05.jpg` (`c0fb9837447ee90ac8c8f975a298aaef`) ⇒ đối tác dùng **một ảnh duy nhất** cho **hai claim khác nhau** (thiếu khối nhận xét · thiếu khối truy vết CT liên quan).
- **Ảnh chung KHÔNG tự động vô hiệu claim này**, nhưng nó **yếu hơn hẳn** cho case 06 so với case 05, vì:
  - khối nhận xét (case 05) **có** vị trí xác định trong bảng thành phần màn hình (#39, kẹp giữa #38 và #40) ⇒ một ảnh chụp trọn màn **có thể** chứng minh nó vắng mặt;
  - khối truy vết (case 06) **không có** vị trí nào được đặc tả (C2 = GAP) ⇒ **không có chỗ để chỉ vào mà nói "đáng lẽ nó ở đây"**, và ảnh cũng không loại được khả năng khối chỉ hiện ở **chế độ nhập số liệu** (bẫy 2).
- **Yêu cầu agent BẰNG-CHỨNG trả lời rõ 4 câu:** (a) ảnh chụp trọn màn hay một khúc? (b) đọc được **trạng thái đợt** không? (c) màn trong ảnh đang ở **chế độ xem** hay **chế độ nhập số liệu**? (d) có phần nào bị cắt/thu gọn không?
- Nếu ảnh không thỏa (b)+(c) ⇒ bằng chứng đối tác **chưa đủ** ⇒ **vẫn phải tự đo lại 2 lượt quét**, và **không** vì thiếu bằng chứng mà chấm "Không phải lỗi".
- **QA phải tự chụp ảnh RIÊNG cho case này**, lưu tại `output/UAT_doi-tac/reverify-week-5/F5-devfix-BCCT-2026-08-07/image/`. **CẤM** dùng lại ảnh của case 05.
