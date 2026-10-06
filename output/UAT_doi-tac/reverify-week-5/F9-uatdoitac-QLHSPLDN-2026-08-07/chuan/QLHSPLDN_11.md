# QLHSPLDN_11 — Tìm kiếm hồ sơ pháp lý có kết quả · GIAI ĐOẠN A (khóa phép thử)

**Dòng bảng:** 293 (tab `bug`) · **Flow:** [`flows/03-reverify-sau-dev-fix.md`](../../../../../flows/03-reverify-sau-dev-fix.md) nhánh 2
**Env đo:** `https://htpldn-uat.ospgroup.vn` (env nghiệm thu của đối tác) · **Tài khoản ra verdict:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`)
**Màn:** menu **Doanh nghiệp** → *Xem chi tiết* 1 DN → thẻ **Hồ sơ pháp lý doanh nghiệp** (`/doanh-nghiep/{id}?tab=ho-so-pl`)
**Nguồn canonical cách đo:** entry `BUG-HSPLDN-QLHSPLDN-11` trong [`F4-pilot/bug-report.md`](../../F4-pilot-QLHSPLDN-2026-08-07/bug-report.md) + vế C1 trong [`F4-pilot/bao-cao-lo`](../../F4-pilot-QLHSPLDN-2026-08-07/bao-cao-lo-2026-08-07.md)

> ⚠️ Mọi dòng SRS dưới đây đã **mở file đọc lại** trong lô này (nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`), không bê từ báo cáo cũ.

---

## 1. Ô phiếu đối tác (expected gốc — nguyên văn)

| Ô | Nội dung |
|---|---|
| **Mô tả** | Tìm kiếm hồ sơ pháp lý có kết quả |
| **Điều kiện** | Đã đăng nhập + tồn tại bản ghi phù hợp tiêu chí |
| **Bước 4** | *NSD nhập từ khóa và/hoặc chọn bộ lọc* |
| **Kết quả mong đợi** | *"Có kết quả, hệ thống hiển thị danh sách kết quả."* |
| **TKM phản hồi lần 1 (KQ thực tế phía đối tác)** | *"Không có trường thông tin tìm kiếm trên màn hình"* |

---

## 2. Bảng vế × quan hệ SRS

| Vế | Đối tác đòi gì | SRS `file:dòng` — quote nguyên văn | Quan hệ | Route |
|---|---|---|---|---|
| **C1a** — thẻ phải có ô từ khóa + bộ lọc | Bước 4: *"NSD nhập từ khóa và/hoặc chọn bộ lọc"* | `srs-fr-12-tv-chuyen-sau.md:589` — **"Inputs -- Tìm kiếm:"**; `:593` — "\| 1 \| keyword \| text \| N \| Tìm theo mã HS, tên DN, tên HS \| — \| người dùng nhập \|"; `:594` — "\| 2 \| loai_ho_so \| text \| N \| GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC \|"; `:595` — "\| 3 \| doanh_nghiep_id \| identifier \| N \|"; `:596` — "\| 4 \| tu_ngay / den_ngay \| date \| N \| tu_ngay <= den_ngay \|"; `:597` — "\| 5 \| trang_thai \| text \| N \| HIEU_LUC / HET_HAN / THU_HOI \|" | **MATCH** | TEST |
| **C1b** — bấm tìm thì ra đúng danh sách kết quả | *"Có kết quả, hệ thống hiển thị danh sách kết quả."* | `srs-fr-12:638` — **"Tìm kiếm:"**; `:643` — "\| 2 \| Áp dụng tất cả bộ lọc: từ khóa, loại hồ sơ, DN, khoảng ngày, trạng thái \|"; `:644` — "\| 3 \| AND logic cho tất cả điều kiện \|"; `:645` — "\| 4 \| Phân trang và trả về \| BR-DATA-07 \|"; `:710` — "**Given** CB NV tìm kiếm theo từ khóa **When** nhập keyword **Then** kết quả matching trong phạm vi đơn vị"; `:711` — "**Given** CB NV kết hợp nhiều điều kiện **When** tìm kiếm **Then** kết quả AND logic" | **MATCH** | TEST |
| **C1c** — chức năng này thuộc đúng thẻ đang tranh chấp | Phiếu chỉ đích danh thẻ *Hồ sơ pháp lý* trong chi tiết DN | `srs-fr-12:560` — "**Màn hình:** ~~SCR-X1-03~~ (DEPRECATED v2.1 — chuyển sang tab trong MH-07.2 chi tiết DN)"; `:1205` — "> **Chuyển sang:** Tab \"Hồ sơ PL\" trong MH-07.2 chi tiết Doanh nghiệp (srs-fr-07-doanh-nghiep.md)."; `srs-fr-07-doanh-nghiep.md:455` — "### SCR-V.III-02: Chi tiết / Chỉnh sửa Doanh nghiệp"; `:461` — "**Quyền truy cập:** Cán bộ nghiệp vụ (TW / Bộ ngành / Địa phương) có quyền CRUD doanh nghiệp." | **MATCH** | TEST |

**Vai trò được phép:** `srs-fr-12:565` — "**Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Người hỗ trợ" ⇒ `cbnv_tw` (CB_NV_TW) đúng tác nhân.

### 2.1 Giải quyết điểm "hai nơi không khớp" — `srs-fr-12` (đủ bộ lọc) ↔ `srs-fr-07:468` (chỉ ghi "CRUD")

Đã đọc trọn cả hai đoạn:

- `srs-fr-07:468` (nguyên văn) — "| 2 | tab | Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) | tab | **CRUD hồ sơ pháp lý DN**: GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC. Trạng thái: HIEU_LUC / HET_HAN / THU_HOI. Gộp từ MH-12.3 (Tư vấn CS) | — | Chỉ khi xem chi tiết |". Cùng ý ở `:459` và `:502`.
- `srs-fr-12:563` (nguyên văn) — "CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, xem chi tiết, thêm mới, chỉnh sửa, xóa mềm, **tìm kiếm**."

⇒ Chữ **"CRUD"** ở `srs-fr-07:468` **chính là nhãn gọi tắt của FR-X.1-04**, và FR-X.1-04 tự định nghĩa phạm vi "CRUD" của nó **đã bao gồm "tìm kiếm"** (`:563`). Thêm nữa, bảng thành phần của `SCR-V.III-02` **không hề liệt kê nội dung bên trong bất kỳ thẻ nào** ngoài thẻ 1 (`:467`–`:470` là 4 dòng thẻ; `:471`–`:494` là trường của thẻ *Thông tin cơ bản*; `:495`–`:496` là thanh hành động) — nghĩa là nó **không enumerate**, chứ không **phủ định**. **Không có câu nào trong SRS nói thẻ này không có tìm kiếm.**

**Kết luận C1: `MATCH`** — không phải `DIFF`, không phải `GAP`. Được đo và được Pass nếu đo đạt. **Không có câu hỏi BA cho case này.**

### 2.2 Bẫy đã có tiền lệ — đã kiểm lại, xác nhận không áp

`srs-fr-07:523` — "| 4 | tab | Tab 2 — Hồ sơ pháp lý DN | tab | **Read-only** danh sách HO_SO_PHAP_LY_DN | Luôn |" thuộc **`SCR-V.III-04`** (`:508` — "### SCR-V.III-04: Hồ sơ doanh nghiệp của tôi (chuyên trang DN)"), mà `:514` ghi rõ "**Quyền truy cập:** Doanh nghiệp (Tier 2 VNeID) … **Vai trò khác KHÔNG truy cập trang này.**" và `:513` URL là `/doanh-nghiep/ho-so-cua-toi`.
⇒ **Cấm dùng `:523` để lập luận cho màn đang đo.** Màn đang đo là `SCR-V.III-02`, URL `/doanh-nghiep/:id`.

---

## 3. Dòng khóa phép đo

```
C1 · thẻ Hồ sơ pháp lý DN không có ô tìm kiếm / bộ lọc nên không tìm được hồ sơ
   · srs-fr-12-tv-chuyen-sau.md:589-597 + :638-645 + :710-711 (neo màn :560, :1205; srs-fr-07:455, :461, :468)
   · MATCH
   · thao tác: trên thẻ Hồ sơ pháp lý của 1 DN — (a) gõ từ khóa lấy từ CHÍNH dữ liệu đang hiển thị rồi bấm [Tìm kiếm];
              (b) giữ từ khóa đó + chọn thêm 1 bộ lọc (Loại hồ sơ hoặc Trạng thái) rồi bấm [Tìm kiếm]
   · PASS khi: cả 2 lượt — bảng thu về đúng tập con khớp điều kiện (≥1 dòng ở lượt (a)) VÀ phản hồi máy chủ của
              CHÍNH lệnh tìm đó có total + danh sách mã trùng khít bảng đang hiển thị; lượt (b) cho tập con
              ⊆ lượt (a) đúng logic AND
   · FAIL khi: thẻ không có ô tìm kiếm / không có nút Tìm kiếm; hoặc bấm mà bảng không đổi; hoặc bảng ≠ phản hồi
              máy chủ (số dòng hoặc danh sách mã lệch); hoặc lượt (b) trả tập KHÔNG phải giao của 2 điều kiện
   · biến thể bắt buộc: 2 — (a) tìm theo từ khóa (:710, và expected "nhập từ khóa") ·
              (b) kết hợp ≥2 điều kiện, kết quả AND (:711 + :644, và expected "và/hoặc chọn bộ lọc")
```

> 🔴 Hai biến thể này **đều do nguồn nêu đích danh**, không phải tự thêm. Vòng F4 chỉ chạy biến thể (a) và tự khai *"biến thể đã phủ: 1 tổ hợp lọc theo từ khóa"* ⇒ lượt này **phải chạy đủ 2** mới được Pass.

---

## 4. Đối chứng độc lập bắt buộc

🔴 **CẤM Pass bằng quan sát tĩnh.** Thấy ô tìm kiếm hiện trên màn **không phải** bằng chứng cho C1 — đó mới là điều kiện để bắt đầu đo.

| # | Việc phải làm | Vì sao tính là độc lập |
|---|---|---|
| 1 | **Chụp baseline trước khi lọc:** số dòng bảng + danh sách mã hồ sơ đang hiển thị | Mốc so sánh; không có nó thì "bảng đổi" không chứng minh được |
| 2 | **Gõ từ khóa + bấm [Tìm kiếm] thật bằng UI.** Ô nhập phải **clear trước khi điền** (công cụ điền hay **nối chuỗi** vào giá trị cũ — đã gãy ở vòng trước) | Hành động đang tranh chấp bắt buộc chạy bằng UI |
| 3 | **Đọc phản hồi máy chủ của chính lệnh tìm đó** (`list_network_requests` → lấy request `ho-so-phap-ly-dns` phát ra **sau** cú bấm) và đối chiếu **2 con số**: `total` = số dòng bảng, **và** danh sách mã trong `data[]` = danh sách mã trên bảng | Đây là phương pháp độc lập theo Flow 03 §Chạy.3 ("hiển thị → đối chiếu dữ liệu nguồn"). **Bấm lại cùng nút KHÔNG tính.** |
| 4 | Xác nhận tham số lọc **thật sự được gửi lên** (`keyword=…`, và ở lượt (b) thêm tham số bộ lọc thứ hai) | Phân biệt "lọc phía máy chủ" với "cắt bảng phía trình duyệt" — fix UI mà BE hỏng sẽ lộ ở đây |
| 5 | Lượt (b): tập kết quả phải ⊆ lượt (a); nếu bộ lọc thứ hai loại hết thì đổi giá trị bộ lọc để còn ≥1 dòng | Chứng minh AND logic `:644` `:711` |

**Ghi lại tối thiểu:** ảnh baseline · ảnh sau lượt (a) · thân phản hồi của lượt (a) · ảnh + thân phản hồi lượt (b) · vân tay bản dựng ở **đầu và cuối** case.

---

## 5. Tiền đề dữ liệu trên env đối tác

**Ưu tiên tuyệt đối: KHÔNG seed gì.** Case này chỉ đọc (tìm kiếm / lọc).

| Hạng mục | Nội dung |
|---|---|
| DN dùng để đo | **`DN-XX-0005`** (`1a715c55-bc31-46de-ae07-56dd4f403ce5`), URL `/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` — đúng DN trong bằng chứng của đối tác |
| Hồ sơ đã biết trên DN đó (đọc từ ảnh đối tác vòng trước) | `HSPL-20260803-0001` *TKM hồ sơ pháp lý số 1* — Khác · Thuế · Thủ công · 03/08/2026 · 03/08/2026 · Hiệu lực<br>`HSPL-20260731-0002` *Hồ sơ x* — Giấy chứng nhận · Đất đai · Thủ công · 01/07/2026 · – · Hiệu lực |
| Điều kiện tối thiểu của C1 | ≥1 bản ghi khớp tiêu chí (phiếu ghi *"tồn tại bản ghi phù hợp"*). ≥2 bản ghi thì mới **nhìn thấy** tác dụng lọc ⇒ ưu tiên DN có ≥2 |
| 🔴 Cấm | **KHÔNG sửa, KHÔNG xoá** `DN-XX-0005`, `HSPL-20260803-0001`, `HSPL-20260731-0002` và mọi bản ghi QA không tự tạo |

### Từ khóa an toàn (không phụ thuộc dữ liệu đối tác)

**Quy tắc: đọc bảng TRƯỚC, rồi lấy từ khóa từ chính dòng đọc được.** Không đoán, không nhớ.

1. Đọc baseline → chọn **một chuỗi con của `mã hồ sơ` một dòng cụ thể** làm từ khóa, sao cho nó **không** khớp các dòng còn lại. Với 2 bản ghi đã biết: dùng `20260731` (chỉ khớp `HSPL-20260731-0002`) hoặc `20260803` (chỉ khớp `HSPL-20260803-0001`) ⇒ cắt 2 → 1.
   *Căn cứ hợp lệ:* `srs-fr-12:593` — keyword "Tìm theo **mã HS**, tên DN, tên HS".
2. Nếu bảng chỉ có 1 dòng: vẫn dùng chuỗi con của mã dòng đó (PASS = 1 dòng, `total=1`), và **khai vào báo cáo** rằng chưa quan sát được thao tác cắt tập.
3. Bộ lọc thứ hai của biến thể (b): lấy **giá trị đang có thật trên bảng** (vd *Loại hồ sơ* = `Giấy chứng nhận`, hoặc *Trạng thái* = `Hiệu lực`).

### Nếu DN đang xem không đủ hồ sơ

Điều kiện tối thiểu **không đạt** (0 bản ghi) → theo thứ tự:
1. **Đổi sang DN khác đã có sẵn hồ sơ** (mở màn danh sách DN, chọn DN có hồ sơ) — vẫn là đọc, không ghi. **Ưu tiên phương án này.**
2. Chỉ khi không DN nào có hồ sơ: dựng bằng **UI thật** — nút **[Thêm hồ sơ]** trên chính thẻ, `Tên hồ sơ` mang dấu nhận dạng **`QA-W5-…`** (vd `QA-W5-HSPL-A`), các trường bắt buộc theo `srs-fr-12:577-587`. **Khai đủ vào báo cáo:** đã tạo bản ghi nào, trên DN nào, env nào.
3. **Cấm** mượn/sửa bản ghi có sẵn để "làm cho khớp từ khóa".

---

## 6. Chuẩn chấm

### ✅ PASS khi (phải đủ **tất cả**)
1. Trên thẻ có ô nhập từ khóa và bộ lọc, bấm được [Tìm kiếm].
2. **Lượt (a)** — gõ từ khóa lấy từ dữ liệu thật → bảng còn đúng tập con khớp (≥1 dòng).
3. **Lượt (b)** — từ khóa đó + 1 bộ lọc nữa → kết quả đúng giao của 2 điều kiện (⊆ lượt (a)).
4. Cả 2 lượt: phản hồi máy chủ của **chính lệnh tìm đó** có `total` = số dòng bảng **và** danh sách mã trùng khít bảng.
5. Tham số lọc có mặt thật trong lệnh gửi lên máy chủ.
6. Vân tay bản dựng đầu case = cuối case.

### ❌ FAIL khi (chỉ cần **một**)
- Thẻ không có ô tìm kiếm / không có nút [Tìm kiếm] ⇒ đúng triệu chứng đối tác báo, Reopen ngay.
- Bấm [Tìm kiếm] mà bảng không đổi dù từ khóa chỉ khớp một phần dữ liệu.
- Bảng lệch phản hồi máy chủ (số dòng hoặc danh sách mã).
- Lượt (b) trả tập **không** phải giao 2 điều kiện (vd bỏ qua từ khóa, hoặc OR thay vì AND).
- Lệnh tìm trả 4xx/5xx.

### 🚫 KHÔNG được chấm **Fail** vì
- **Thiếu ô chọn *Doanh nghiệp*** (`srs-fr-12:595` liệt kê `doanh_nghiep_id`). Thẻ này nằm **trong** chi tiết 1 DN, `doanh_nghiep_id` bị ràng buộc bởi ngữ cảnh URL (`:560`, `:1205`); phiếu đối tác cũng không nhắc ô này. ⇒ Ghi nhận, **không** chấm lỗi, **không** đẩy BA.
- Nhãn ô / vị trí ô khác mong đợi (SRS không quy định câu chữ nhãn ô tìm kiếm).
- Bảng trên màn có **10 cột** (thêm *Lĩnh vực pháp lý* · *Nguồn* · *Có tệp đính kèm*, thiếu *Doanh nghiệp* · *Cơ quan cấp*) — `:664` là quy định cho **tệp xuất**, thuộc `QLHSPLDN_14`, không phải cho bảng trên màn. Xem `chuan/QLHSPLDN_14.md` §6.
- Kết quả ít dòng vì dữ liệu env đối tác ít — đó là dữ liệu, không phải lỗi.
- Lần điền đầu bị **nối chuỗi** vào ô (lỗi công cụ) → clear ô, đo lại; không tính là lỗi sản phẩm.

### 🚫 KHÔNG được chấm **Pass** vì
- **Chỉ nhìn thấy ô tìm kiếm/bộ lọc đã hiện trên màn** (quan sát tĩnh) — cấm tuyệt đối.
- Chỉ chạy biến thể (a), bỏ biến thể (b) — thiếu biến thể do `:711` + expected nêu đích danh ⇒ **Chưa chốt**, không phải Pass.
- Chỉ đối chiếu bằng mắt "bảng có vẻ ít dòng hơn" mà không đọc phản hồi máy chủ.
- Lấy kết quả Pass ở env nội bộ (bản dựng `V1.0.9`) làm căn cứ — khác env, khác bản dựng, **không chứng minh gì cho lô này**.
- Bấm lại cùng nút lần hai và coi đó là đối chứng độc lập.

---

## 7. Câu hỏi BA

**Không có.** Cả 3 vế con đều `MATCH` (xem §2.1). Case này đi thẳng **TEST**, không có phần chờ BA.
