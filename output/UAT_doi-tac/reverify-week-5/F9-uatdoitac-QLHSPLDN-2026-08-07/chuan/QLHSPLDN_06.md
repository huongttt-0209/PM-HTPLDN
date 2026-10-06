# GIAI ĐOẠN A — khóa phép thử · `QLHSPLDN_06` (tab `bug`, dòng 291 — "Xem")

```
Lô:            F9 — tái xác nhận trên env NGHIỆM THU của đối tác
Flow:          flows/03-reverify-sau-dev-fix.md — NHÁNH 2 "Tái xác nhận trên môi trường khác"
Env đích:      https://htpldn-uat.ospgroup.vn  (bó mã đo 12:43 VN 07/08: assets/index-D4NhKEjr.js
               · GET / last-modified Fri, 07 Aug 2026 04:17:55 GMT = 11:17 VN 07/08)
Tài khoản:     cbnv_tw / Test@1234  (vai trò CB_NV_TW, cấp TW) — env này CÓ bước mã xác thực,
               lấy ở https://htpldn-uat.ospgroup.vn/mailhog/. KHÔNG có sibling _01.._05 ⇒ khóa thì DỪNG.
               admin / Secret@123 (QTHT) KHÔNG dùng cho case này.
Nguồn canonical: tieuchi/QLHSPLDN_06.md §4 §5 §6 + entry BUG-HSPLDN-QLHSPLDN-06 trong bug-report.md
Nguồn SRS:     Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/  — đã MỞ FILE ĐỌC LẠI 07/08
Người viết:    agent CHUẨN-1 · 2026-08-07 · KHÔNG mở trình duyệt
```

> 🔴 **Bản dựng env đích khác hoàn toàn nơi đã Pass** (env nội bộ, bó mã `index-DIABnbIr.js`).
> ⇒ **MỌI vế `MATCH` phải đo lại từ đầu**, không vế nào được miễn vì "đã Pass ở env nguồn".

---

## 0. 🔴 SỐ DÒNG SRS ĐÃ ĐỔI — tieuchi cũ quote SAI, phải dùng cột "Thực tế 07/08"

`srs-fr-12-tv-chuyen-sau.md` và `srs-v3.5.md` được sửa lúc **2026-08-06 22:52:29**, tức **sau** khi
`tieuchi/QLHSPLDN_06.md` được viết (06/08 18:48) và sau vòng đo env nội bộ (06/08 18:54→18:59).
**Nội dung các dòng được trích vẫn nguyên văn — chỉ số dòng dịch.** Mọi trích dẫn dưới đây là số dòng
tôi tự mở file đọc được ngày 07/08.

| Nội dung | tieuchi ghi | **Thực tế 07/08** |
|---|---|---|
| `### FR-X.1-04: Quản lý hồ sơ pháp lý doanh nghiệp (UC150)` | `srs-fr-12:541` | **`:554`** |
| `**Màn hình:** ~~SCR-X1-03~~ (DEPRECATED v2.1 …)` | `:547` | **`:560`** |
| Mô tả `CRUD … xem danh sách, xem chi tiết, thêm mới, chỉnh sửa, xóa mềm, tìm kiếm.` | `:550` | **`:563`** |
| `**Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Người hỗ trợ` | `:552` | **`:565`** |
| Bảng **Inputs — Thêm mới / Chỉnh sửa** (11 trường) | `:560-574` | **`:573-587`** |
| `linh_vuc_id`…`mo_ta` (5 trường tuỳ chọn) | `:568-572` | **`:581-585`** |
| `trang_thai … HIEU_LUC / HET_HAN / THU_HOI` | `:573` | **`:586`** |
| `file_dinh_kem … N … PDF/image, max 20MB` | `:574` | **`:587`** |
| Bảng **Inputs — Tìm kiếm** (5 bộ lọc) | `:576-584` | **`:589-597`** |
| Processing **Thêm mới** (6 bước) | `:596-605` | **`:609-618`** |
| **Processing — Xem chi tiết** `[GAP-X.1-05]` | `:634` | **`:647`** |
| `Trả full record: thông tin hồ sơ + thông tin DN liên kết` | `:640` | **`:653`** |
| `Truy vấn danh sách file đính kèm (FILE_DINH_KEM)` | `:641` | **`:654`** |
| `Trả kết quả bao gồm file đính kèm (tên, loại, dung lượng, URL preview)` | `:642` | **`:655`** |
| **Processing — Xuất Excel** `[GAP-X.1-05]` | `:644` | **`:657`** |
| Outputs `ngay_cap` / `ngay_het_han` / `trang_thai` | `:663` `:664` `:665` | **`:676` `:677` `:678`** |
| AC "…danh sách hồ sơ thuộc đơn vị, phân trang" | `:692` | **`:705`** |
| AC "…CB NV xem chi tiết hồ sơ … đầy đủ thông tin + file đính kèm" | `:693` | **`:706`** |
| AC vai trò NHT xem chi tiết | `:700` | **`:713`** |
| `### ~~SCR-X1-03: Hồ sơ Pháp lý DN~~ (DEPRECATED v2.1)` + "Chuyển sang…" | `:1176` `:1178` | **`:1203` `:1205`** |
| `srs-v3.5.md` — "Áp dụng cho **mọi màn hình**…" (đầu §E.H) | `:6705` | **`:6749`** |
| `srs-v3.5.md` — **H6** "Cột Hành động dạng icon + tooltip BẮT BUỘC … Mắt = Xem…" | `:6714` | **`:6758`** |
| `srs-v3.5.md` — ghi chú Phụ lục E §A–G nằm ở `srs-fr-05` §3.A–G | `:6699-6701` | **`:6745`** |

**KHÔNG lệch (đã kiểm từng dòng):** `srs-fr-07-doanh-nghiep.md` `:455` `:459` `:461` `:468` `:496`
`:508` `:514` `:523` `:819-821` · `srs-fr-05-vu-viec.md` `:1490` `:1492`.

> ⚠️ `[GAP-X.1-05]` gắn ở `srs-fr-12:647` / `:657` là **nhãn soạn thảo BMAD** (khối bổ sung so với bản v3),
> KHÔNG phải "SRS im lặng" theo nghĩa của Flow 03. Nhãn này xuất hiện cả ở các khối được đặc tả đầy đủ
> (`:166`, `:183`, `:909`…). ⇒ **không** vì nhãn này mà xếp vế (a)(b)(c) thành `GAP`.

---

## 1. Bảng vế × quan hệ SRS

| Vế | Nội dung đối tác đòi (ô phiếu) | SRS hiện tại — `file:dòng` + nguyên văn | Quan hệ | Route |
|---|---|---|---|---|
| **a** | Trên bảng Hồ sơ pháp lý DN phải có **chức năng mở chi tiết từng hồ sơ** (đối tác: cột Hành động chỉ có `Sửa`/`Xoá`) | `srs-fr-12-tv-chuyen-sau.md:563` — *"CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, **xem chi tiết**, thêm mới, chỉnh sửa, xóa mềm, tìm kiếm."* · `:647` — *"**Processing — Xem chi tiết** `[GAP-X.1-05]`"* · `:706` — *"**Given** CB NV xem chi tiết hồ sơ **When** chọn bản ghi **Then** hiển thị đầy đủ thông tin + file đính kèm"* · `srs-v3.5.md:6749` — *"Áp dụng cho **mọi màn hình** trong hệ thống (Dashboard, … DN, …)"* · `:6758` — *"**H6** \| Cột Hành động dạng icon + tooltip BẮT BUỘC \| Cột Hành động trong mọi bảng dùng icon (**Mắt = Xem**, Bút = Sửa, Thùng rác = Xóa, …)…"* · `srs-fr-07-doanh-nghiep.md:455` — *"### SCR-V.III-02: Chi tiết / Chỉnh sửa Doanh nghiệp"*, `:468` — *"Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) \| tab \| CRUD hồ sơ pháp lý DN…"* (màn duy nhất còn thực thi FR-X.1-04 vì `srs-fr-12:560` + `:1203` khai `SCR-X1-03` DEPRECATED) | **MATCH** | TEST |
| **b** | Bấm vào đó **mở cửa sổ chi tiết**, hiển thị **toàn bộ thông tin của hồ sơ** | `srs-fr-12:653` — *"\| 3 \| Trả full record: thông tin hồ sơ + thông tin DN liên kết \| — \|"* · `:706` (nguyên văn ở vế a) · Outputs `:676` *"\| 6 \| ngay_cap \| date \| luôn \| dd/mm/yyyy \|"*, `:677` *"\| 7 \| ngay_het_han \| date \| luôn \| dd/mm/yyyy \|"*, `:678` *"\| 8 \| trang_thai \| text \| luôn \| HIEU_LUC / HET_HAN / THU_HOI \|"* · `srs-fr-05-vu-viec.md:1492` — *"Khi render UI, dev **phải dịch** mã DB (snake_case enum) sang nhãn tiếng Việt… Mã DB **không bao giờ** xuất hiện trên giao diện người dùng."* | **MATCH** | TEST |
| **c** | Cửa sổ có **danh sách tệp đính kèm (nếu có)** | `srs-fr-12:654` — *"\| 4 \| Truy vấn danh sách file đính kèm (FILE_DINH_KEM) \| — \|"* · `:655` — *"\| 5 \| Trả kết quả bao gồm file đính kèm (tên, loại, dung lượng, URL preview) \| — \|"* · `:706` · `:587` — *"\| 11 \| file_dinh_kem \| file \| N \| PDF/image, max 20MB \| — \| người dùng upload \|"* (tệp **không bắt buộc** ⇒ đúng chữ "(nếu có)") | **MATCH** | TEST |
| **d1** | Cửa sổ Xem phải là **thao tác riêng**, không phải chính biểu mẫu Chỉnh sửa | `srs-fr-12:620` — *"**Chỉnh sửa:**"* (bảng 4 bước `:624-627`) **tách khỏi** `:647` *"**Processing — Xem chi tiết**"* (bảng 5 bước `:651-655`) — hai khối xử lý riêng · `srs-v3.5.md:6758` **H6** phân biệt **Mắt = Xem** (tooltip *"Xem chi tiết"*) với **Bút = Sửa** (tooltip *"Chỉnh sửa"*) | **MATCH** | TEST |
| **d2** | Cửa sổ ở **chế độ chỉ đọc** (được phép chứa ô nhập / lưu tại chỗ hay không) | SRS **im lặng cho màn cán bộ**. Chỗ duy nhất trong toàn bộ v3.5 ghi "Read-only" cho tab HSPL là `srs-fr-07-doanh-nghiep.md:523` — *"\| 4 \| tab \| Tab 2 — Hồ sơ pháp lý DN \| tab \| Read-only danh sách HO_SO_PHAP_LY_DN \| Luôn \|"*, nhưng dòng đó **thuộc `SCR-V.III-04`** (`:508` — *"### SCR-V.III-04: Hồ sơ doanh nghiệp của tôi (chuyên trang DN)"*; `:514` — *"**Quyền truy cập:** Doanh nghiệp (Tier 2 VNeID)… **Vai trò khác KHÔNG truy cập trang này.**"*; `:537` — *"Tab 2/3/4 read-only — DN không sửa được"*). Màn đang tranh chấp là `SCR-V.III-02` (`:455`, `:461` — *"Cán bộ nghiệp vụ (TW / Bộ ngành / Địa phương) có quyền CRUD doanh nghiệp"*) — **không có** dòng read-only nào. Grep toàn `srs-fr-12` cũng không có câu nào về chế độ chỉ đọc của cửa sổ Xem HSPL. | **GAP** (có điều kiện — xem §1.1) | BA *(chỉ khi kích hoạt)* |

### 1.1 Bẫy đã xác minh lại + cách xử vế `d2`

✅ **Đã mở trọn đoạn `srs-fr-07:452-537` đọc bằng mắt.** Xác nhận cảnh báo trong tieuchi là ĐÚNG:
`:523` **KHÔNG** áp cho màn cán bộ. **CẤM dùng `:523` để chấm case này.**

`d2` là **GAP có điều kiện** — nó chỉ trở thành câu hỏi BA khi số đo rơi vào **ca lửng**:

| Số đo được trên env đích | Xử |
|---|---|
| Cửa sổ có **0 ô nhập** (`input`/`textarea`/`select`/`.ant-select`/`.ant-picker`/`[contenteditable]`) **và 0 nút lưu/gửi** | Hiện trạng **thỏa đúng ô *Kết quả mong đợi*** của đối tác ⇒ **không tồn tại bất đồng nào để BA chốt** ⇒ `d2` không kéo case sang Cần BA. **Bắt buộc ghi trong hồ sơ:** kết luận này chỉ có hiệu lực với expected gốc của phiếu, **SRS vẫn im lặng** — không được viết như thể SRS quy định read-only. |
| Bấm "Xem" mở ra **đúng biểu mẫu chỉnh sửa** (có ô nhập + nút lưu) | Đây là **`d1` FAIL** (có căn cứ SRS `:620` vs `:647` + H6 `:6758`) ⇒ Reopen. **Không** phải câu hỏi BA. |
| **Ca lửng** — có vài ô nhập nhưng không lưu được / chỉ là ô tìm kiếm trong cửa sổ | **Kích hoạt `d2`** ⇒ **cấm Pass/Fail vế này**, ghi nguyên hiện trạng + đặt câu hỏi BA ở §8. Verdict case = **Cần BA**. |

---

## 2. Dòng khóa phép đo

```
C1 · Cột Hành động thiếu điều khiển mở chi tiết (đối tác chỉ thấy Sửa/Xoá) · srs-fr-12:563 + :647 + :706
   + srs-v3.5.md:6749 + :6758 · MATCH · đi đúng 4 bước phiếu bằng UI thật (menu Doanh nghiệp → nút mở chi
   tiết trên hàng DN → thẻ Hồ sơ pháp lý), KHÔNG gõ thẳng URL; đếm THÔ số hàng .ant-table-tbody
   tr.ant-table-row = N và số điều khiển mở chi tiết trong ô Hành động của chính các hàng đó
   · PASS khi: số điều khiển = N (mỗi hàng ≥1), hai cách đếm độc lập cùng ra N, và TỪNG điều khiển
   disabled=false · không aria-disabled="true" · pointer-events≠none · opacity=1 · rect > 0×0 · nằm trong
   khung nhìn hoặc cuộn tới được · FAIL khi: ≥1 hàng bất kỳ thiếu điều khiển (kể cả hàng khác có), hoặc
   điều khiển vô hiệu hoá / 0×0 / bị che không bấm được · biến thể bắt buộc: D1 D2 D3 D4 (mọi dạng hàng)

C2 · Bấm không mở được cửa sổ chi tiết · srs-fr-12:647 + :706 · MATCH · bấm bằng CHUỘT THẬT qua UI (cấm
   dispatchEvent, cấm gọi hàm JS) trên ≥1 hồ sơ của MỖI dạng D1–D4 · PASS khi: mỗi lần bấm hiện cửa sổ/lớp
   nổi chi tiết, đọc được tiêu đề + nội dung bằng innerText, và ĐÃ CHỤP ẢNH RỒI MỞ ẢNH ĐỌC BẰNG MẮT
   · FAIL khi: không hiện gì / văng lỗi bảng điều khiển / điều hướng sang màn khác thay vì mở chi tiết
   · biến thể bắt buộc: D1 D2 D3 D4

C3 · Nội dung cửa sổ lệch bản ghi gốc · srs-fr-12:653 + :706 + :676 :677 :678 + srs-fr-05:1492 · MATCH ·
   với MỖI hồ sơ đã bấm, đối chiếu từng trường (mã · tên · loại · lĩnh vực · nguồn · cơ quan cấp · ngày cấp
   · ngày hết hạn · trạng thái · mô tả) với NGUỒN ĐỘC LẬP = đọc lại bản ghi qua đúng đường request UI phát ra
   (list_network_requests — CẤM đoán đường dẫn API) · PASS khi: mọi trường đọc được khớp nguyên văn, ngày
   theo dd/mm/yyyy, không trường nào hiện null/undefined/[object Object]/ô rỗng mất nhãn, trường bỏ trống
   hiện ký hiệu rỗng · FAIL khi: ≥1 trường lệch, hoặc hiện null/undefined/[object Object]
   · biến thể bắt buộc: D1 D2 D3 D4 · bấm lại cùng nút KHÔNG tính là phương pháp thứ hai

C4 · Cửa sổ không liệt kê tệp / lệch số tệp · srs-fr-12:654 + :655 + :706 + :587 · MATCH · mở chi tiết hồ sơ
   CÓ tệp (D1) và hồ sơ KHÔNG tệp (D2) · PASS khi: (D1) mục tệp hiện, nhận diện được TỪNG tệp bằng tên, và
   số tệp hiển thị = số tệp thực của bản ghi đối chiếu bằng đường thứ hai (đọc lại bản ghi qua máy chủ hoặc
   mở biểu mẫu Sửa của chính hồ sơ đó — CHỈ ĐỌC, KHÔNG bấm lưu); (D2) cửa sổ vẫn mở bình thường, có trạng
   thái rỗng đọc được hoặc không có mục tệp, không trắng, không lỗi bảng điều khiển · FAIL khi: hồ sơ có tệp
   mà cửa sổ không liệt kê / số tệp lệch, hoặc hồ sơ không tệp mà cửa sổ vỡ · biến thể bắt buộc: D1 D2

C5 · "Xem" mở ra chính biểu mẫu Chỉnh sửa · srs-fr-12:620 (khối Chỉnh sửa) vs :647 (khối Xem chi tiết) +
   srs-v3.5.md:6758 · MATCH · trong phạm vi cửa sổ vừa mở, đếm THÔ input/textarea/select/.ant-select/
   .ant-picker/[contenteditable="true"] và liệt kê toàn bộ nút · PASS khi: cửa sổ Xem KHÔNG phải biểu mẫu
   chỉnh sửa lưu được (không có nút lưu/gửi kích hoạt được trên dữ liệu hồ sơ) · FAIL khi: bấm Xem mở đúng
   biểu mẫu chỉnh sửa có ô nhập + nút lưu và sửa-lưu được · biến thể bắt buộc: đo trên cả 3 dạng đã bấm ở C2

C6 · Cửa sổ Xem có ô nhập / lưu tại chỗ hay không (chế độ chỉ đọc) · SRS IM LẶNG cho SCR-V.III-02 —
   srs-fr-07:523 thuộc SCR-V.III-04 (:508, :514) · GAP · dùng CHÍNH số đo của C5, KHÔNG mở thêm vòng UI ·
   CẤM Pass · CẤM Reopen · nếu 0 ô nhập + 0 nút lưu ⇒ ghi "hiện trạng thỏa expected gốc, SRS im lặng",
   không phát sinh câu hỏi BA · nếu ca lửng ⇒ ghi nguyên hiện trạng + câu hỏi BA §8 · biến thể: không thêm
```

---

## 3. Tiền đề phải dựng trên env ĐỐI TÁC

### 3.1 Ranh giới cứng

- ❌ **CẤM sửa/xoá** `DN-XX-0005` (`1a715c55-bc31-46de-ae07-56dd4f403ce5`), `HSPL-20260803-0001`,
  `HSPL-20260731-0002`. ❌ **CẤM thêm hồ sơ mới vào `DN-XX-0005`** (làm đổi bảng trong ảnh bằng chứng của họ).
- ✅ **ĐƯỢC ĐỌC** `DN-XX-0005`: mở thẻ Hồ sơ pháp lý, đếm hàng/điều khiển, **bấm "Xem"** trên 2 hồ sơ của họ.
  Bấm Xem là thao tác đọc. **Nếu cửa sổ hoá ra là biểu mẫu sửa được ⇒ TUYỆT ĐỐI KHÔNG bấm lưu, đóng ngay.**
  Đây là bằng chứng mạnh nhất vì đối chiếu **đúng bảng, đúng bản ghi** trong ảnh đối tác.
- ✅ Hồ sơ QA tạo mới mang dấu nhận dạng `QA-W5-0807-…`.

### 3.2 Danh sách tiền đề + thứ tự dựng

| # | Việc | Cách làm bằng UI | Kết quả cần có |
|---|---|---|---|
| **T0** | Đăng nhập + ghi vân tay bản dựng (đầu) | `cbnv_tw` / `Test@1234` → lấy mã xác thực ở `https://htpldn-uat.ospgroup.vn/mailhog/api/v2/messages?limit=5` → **tải lại trang bỏ đệm** trước lô đo | Ghi `assets/index-*.js` + `GET /` `last-modified` + `etag` |
| **T1** | Chọn **DN QA** (nơi seed) | Menu trái → **Doanh nghiệp** → đọc danh sách. Chọn **1 DN trong phạm vi TW KHÁC `DN-XX-0005`** và không xuất hiện trong bằng chứng đối tác. Ghi lại **mã DN + id trên URL** | 1 DN QA đã chốt |
| **T1b** | *(chỉ khi T1 không tìm được DN nào khác)* Tạo DN mới | Màn Danh sách doanh nghiệp → nút **[Thêm mới]** (`srs-fr-07:459` — *"Tạo mới DN dùng SCR-V.III-03 riêng (FR-V.III-NEW-03), mở từ nút 'Thêm mới' ở SCR-V.III-01"*). Tên `QA-W5-0807 Kiem thu HSPL`, MST chưa tồn tại, tỉnh/thành thuộc phạm vi TW | DN QA mới, khai vào báo cáo |
| **T2** | Chuẩn bị tệp seed | Đặt 2 tệp PNG thật (vài chục byte là đủ) vào `F9-uatdoitac-QLHSPLDN-2026-08-07/seed-files/`, tên `QA-W5-0807-tep-06A.png` và `QA-W5-0807-tep-06C.png`. Có thể sao chép từ `reverify-week-5/seed-files/QA-W5-1907-tep-luot1.png` rồi đổi tên | 2 tệp sẵn sàng |
| **T3** | Seed **hồ sơ A** — dạng **D1** (có tệp) + trạng thái *Hiệu lực* + **mọi trường tuỳ chọn ĐƯỢC ĐIỀN** | Mở chi tiết DN QA → thẻ **Hồ sơ pháp lý** → nút **[Thêm hồ sơ]** → điền: Tên `QA-W5-0807-HS-A co tep` · Loại `Giấy phép` · Lĩnh vực (chọn 1 giá trị) · Ngày cấp `01/08/2026` · Ngày hết hạn `31/12/2026` · Cơ quan cấp `QA-W5-0807 coquan` · Mô tả `QA-W5-0807 mo ta A` · Trạng thái `Hiệu lực` → **đính kèm `QA-W5-0807-tep-06A.png`** → bấm **`Đồng ý`** | 1 hồ sơ *Hiệu lực*, **1 tệp**, 0 trường trống |
| **T4** | Seed **hồ sơ B** — dạng **D2** (không tệp) + **D3-Thu hồi** + **D4** (5 trường tuỳ chọn TRỐNG) | [Thêm hồ sơ] → chỉ điền Tên `QA-W5-0807-HS-B khong tep` · Loại `Khác` · Trạng thái `Thu hồi`. **Bỏ trống** Lĩnh vực · Ngày cấp · Ngày hết hạn · Cơ quan cấp · Mô tả (`srs-fr-12:581-585` khai 5 trường này là `N`). **Không đính tệp** → `Đồng ý` | 1 hồ sơ *Thu hồi*, **0 tệp**, 5 trường trống |
| **T5** | Seed **hồ sơ C** — dạng **D3-Hết hạn** (+ có tệp) | [Thêm hồ sơ] → Tên `QA-W5-0807-HS-C het han` · Loại `Quyết định` · Ngày cấp `01/03/2026` · Ngày hết hạn `01/07/2026` · Trạng thái `Hết hạn` → đính kèm `QA-W5-0807-tep-06C.png` → `Đồng ý` | 1 hồ sơ *Hết hạn*, 1 tệp |
| **T6** | **Xác nhận tiền đề bằng UI sau khi seed** | **Tải lại trang thật** → mở lại thẻ Hồ sơ pháp lý của DN QA → đọc bảng: đủ 3 hàng QA, đúng 3 trạng thái, đúng có/không tệp | Tiền đề đã đứng |
| **T7** | Khai vào báo cáo | DN QA (mã + id) · 3 mã hồ sơ QA vừa tạo · env `htpldn-uat.ospgroup.vn` · giờ tạo | **Bản ghi không khai = coi như chưa đo** |

> **Trạng thái *Hiệu lực*** đã có ở hồ sơ A **và** ở cả 2 hồ sơ của đối tác ⇒ D3 phủ đủ 3 trạng thái.
> **Thứ tự chạy trong lô:** làm **trọn `QLHSPLDN_06`** rồi mới sang `QLHSPLDN_07` — case `_07` có thao tác
> ghi đè 8 ô, chạy trước sẽ phá tiền đề D1/D4 của case này.

### 3.3 Độ phủ hàng khi đo

- Đo **toàn bộ hàng của trang đang xem, đếm thô, KHÔNG lấy mẫu** — trên **cả** bảng của DN QA **và** bảng
  của `DN-XX-0005`.
- Bấm mở chi tiết **≥1 hồ sơ cho mỗi dạng D1–D4** (1 hồ sơ có thể phủ nhiều dạng — ghi rõ hồ sơ nào phủ dạng nào).

---

## 4. Điều kiện PASS bắt buộc / FAIL

### ✅ PASS cả case — chỉ khi ĐỦ CẢ 5 nhóm

| Nhóm | Điều kiện |
|---|---|
| **A** *(vế a — C1)* | ① Đếm **thô** hàng = N, đếm **thô** điều khiển mở chi tiết = N (mỗi hàng ≥1). **Cấm** `unique`/lọc/gộp trước khi đếm; **cấm** lấy mẫu 2–3 hàng suy ra cả bảng. ② Đếm lại bằng **≥2 cách độc lập** cùng ra N (vd đếm điều khiển trong ô cuối mỗi hàng · đếm phần tử có nhãn/`aria-label`/tooltip nghĩa "Xem"/"Xem chi tiết", đọc bằng **`innerText`** — không `textContent`). ③ Từng điều khiển dùng được thật: `disabled=false` · không `aria-disabled="true"` · `pointer-events ≠ none` · `opacity = 1` · rect **> 0×0** · trong khung nhìn hoặc cuộn tới được. |
| **B** *(vế b — C2)* | ④ Bấm bằng **chuột thật qua UI** trên ≥1 hồ sơ của **mỗi dạng D1–D4**; mỗi lần đều hiện cửa sổ chi tiết, đọc được tiêu đề + nội dung bằng `innerText`, **và đã chụp ảnh rồi mở ảnh đọc bằng mắt**. ⑤ Selector dò cửa sổ trả 0 **không** được kết luận "không mở" — phải đo lại bằng đường khác (quét lớp bao ngoài · `innerText` toàn trang · chụp ảnh) rồi mới chốt. Nếu có lời gọi lấy chi tiết thì mã trả về phải **2xx**; nếu FE lấy dữ liệu từ danh sách đã tải (0 lời gọi) thì **không** vì thế mà chấm Fail. |
| **C** *(vế b — C3)* | ⑥ Với **mỗi** hồ sơ đã bấm, đối chiếu **từng trường** với nguồn độc lập; mọi trường đọc được **khớp nguyên văn**; ngày theo `dd/mm/yyyy` (`srs-fr-12:676`, `:677`). Bấm lại cùng nút **không** tính. ⑦ Không trường nào hiện `null` / `undefined` / `[object Object]` / ô rỗng mất cả nhãn; trường bỏ trống hiện ký hiệu rỗng. |
| **D** *(vế c — C4)* | ⑧ Hồ sơ **có tệp (D1)**: cửa sổ hiển thị mục tệp, **nhận diện từng tệp bằng tên**, **số tệp hiển thị = số tệp thực** (đối chiếu đường thứ hai). ⑨ Hồ sơ **không tệp (D2)**: cửa sổ **vẫn mở bình thường**, có trạng thái rỗng đọc được (hoặc không có mục tệp), **không** trắng, **không** lỗi bảng điều khiển. |
| **E** *(vế d1 — C5)* | ⑩ Cửa sổ Xem **không phải** biểu mẫu chỉnh sửa lưu được. *(Vế d2/C6 chỉ ghi hiện trạng — xem §1.1.)* |

**Verdict tổng:** (a)(b)(c)(d1) đều đạt **và** `d2` không rơi vào ca lửng ⇒ **Pass**.
≥1 vế `MATCH` FAIL đủ 4 điều kiện Flow 03 ⇒ **Reopen** (dừng ngay, không chạy nốt biến thể).
Không vế nào lỗi nhưng `d2` rơi vào **ca lửng** ⇒ **Cần BA**.
Vừa có FAIL vừa có ca lửng ⇒ **Reopen + Cần BA**.

### ❌ FAIL (Reopen) nếu ≥1 điều sau

- **≥1 hàng bất kỳ** (dạng D1–D4 nào cũng vậy) **không có** điều khiển mở chi tiết — kể cả khi các hàng khác
  có. Ca *"chỉ hàng Hiệu lực có nút, hàng Hết hạn/Thu hồi không có"* = **fix một phần** ⇒ vẫn FAIL.
- Có điều khiển nhưng **bấm bằng UI thật không mở được gì** (không cửa sổ / lỗi bảng điều khiển / điều hướng
  sang màn khác), hoặc điều khiển bị vô hiệu hoá / 0×0 / bị che không bấm được.
- Cửa sổ mở nhưng **≥1 trường lệch** so với nguồn độc lập, hoặc hiện `null`/`undefined`/`[object Object]`.
- Hồ sơ **có tệp** mà cửa sổ **không liệt kê tệp**, hoặc **số tệp lệch** so với bản ghi thực.
- Hồ sơ **không có tệp** mà cửa sổ **vỡ** (trắng / văng lỗi / không mở được).
- Bấm "Xem" mở ra **biểu mẫu chỉnh sửa lưu được** (C5).
- Fix **đẻ ra lỗi mới ngay trong luồng này** (bấm Xem xong bảng mất dữ liệu / mở cửa sổ không đóng được).

---

## 5. Biến thể bắt buộc — **M = 4**

| # | Dạng | Căn cứ (SRS 07/08) | Vế cần | Bắt buộc? |
|---|---|---|---|---|
| **D1** | Hồ sơ **CÓ ≥1 tệp** | `srs-fr-12:654`, `:655` quy định riêng việc truy vấn + trả danh sách tệp — dạng **duy nhất** chứng minh được vế (c) | a·b·c | ✅ **BẮT BUỘC** — dựng ở T3 |
| **D2** | Hồ sơ **KHÔNG có tệp** | `:587` khai `file_dinh_kem` **không bắt buộc**; đối tác ghi rõ "(nếu có)" | a·b·c | ✅ **BẮT BUỘC** — dựng ở T4 |
| **D3** | Đủ **3 trạng thái** *Hiệu lực · Hết hạn · Thu hồi* | `:586` — *"trang_thai … HIEU_LUC / HET_HAN / THU_HOI"* + `srs-fr-07:468`. Đây là biến thể kinh điển làm nút biến mất theo điều kiện hiển thị | a·b | ✅ **BẮT BUỘC** — T3 (Hiệu lực) · T4 (Thu hồi) · T5 (Hết hạn) |
| **D4** | Hồ sơ có **trường tuỳ chọn để trống** | `:581-585` khai 5 trường `N`; **chính ảnh đối tác** có hàng ngày hết hạn `-` ⇒ ca có thật trên dữ liệu họ | b | ✅ **BẮT BUỘC** — T4 (5 trường trống) |

**Dạng KHÔNG dựng được ⇒ MIỄN:** hồ sơ `nguon = CONG_PLQG` (`srs-fr-12:681` khai `THU_CONG / CONG_PLQG`)
phải đến từ API inbound của Cổng PLQG — QA không tạo được bằng UI. **Miễn hợp lệ** vì đối tác cũng chỉ có
hồ sơ *Thủ công* (đọc được trên ảnh) ⇒ không lệch điều kiện đo với họ. Khai vào báo cáo, **không** để thành GAP.

**Thiếu dạng bắt buộc nào mà không dựng được ⇒ Chưa chốt**, ghi rõ thiếu gì — **không** Pass thiếu biến thể.

---

## 6. Chống chấm oan

### ⚠️ KHÔNG được chấm **Fail** vì *(ghi nhận / log candidate riêng, KHÔNG kéo verdict case)*

- **Điều khiển là nhãn chữ "Xem" thay vì icon con mắt, hoặc thiếu `aria-label`/tooltip.** `srs-v3.5.md:6758`
  (H6) có quy định thật, nhưng **không phải vế đối tác nêu** (họ nói *thiếu hẳn chức năng*) ⇒ candidate riêng.
- **Nút thêm ghi "Thêm hồ sơ" thay vì "Thêm mới".** `srs-v3.5.md:6756` (H4 — *"Nút thêm mới luôn đặt nhãn
  **'Thêm mới'**"*, BẮT BUỘC) — vẫn **khác vế** ⇒ candidate riêng.
- **Thẻ này không có ô tìm kiếm / bộ lọc / nút Xuất Excel.** Hai chỗ SRS không khớp nhau (`srs-fr-12:589-597`
  khai 5 bộ lọc + `:657-665` khai hẳn khối *Processing — Xuất Excel* ↔ `srs-fr-07:468` chỉ ghi *"CRUD"*)
  ⇒ **cần BA**, **ngoài vế** của case này.
- **Không bấm được vào hàng để mở chi tiết** (chỉ mở bằng nút) — SRS không quy định click-hàng cho bảng này.
- **Cửa sổ chi tiết không hiển thị thông tin DN liên kết.** `srs-fr-12:653` là bước xử lý **phía máy chủ**,
  còn cửa sổ đang mở **bên trong** màn chi tiết của chính DN đó ⇒ candidate, không kéo verdict.
- **Bố cục / thứ tự trường / kiểu cửa sổ (lớp nổi hay trang riêng) / màu nhãn trạng thái / phải cuộn ngang mới
  thấy cột Trạng thái** — SRS không quy định (`SCR-X1-03` DEPRECATED tại `:560` + `:1203`; bản thay thế
  `srs-fr-07:468` chỉ ghi "CRUD").
- **Ký hiệu ô trống không nhất quán** (`—` cột này, `-` cột kia) — thuần mỹ thuật.
- **Vai trò khác** (NHT theo `srs-fr-12:713`, hoặc vai trò Doanh nghiệp ở `SCR-V.III-04`) — **ngoài vế**;
  chỉ đo đúng vai trò `CB_NV_TW` của đối tác.
- **Mã enum thô hiện trên màn** (`HIEU_LUC`, `GIAY_CN`, `THU_CONG`) — có căn cứ `srs-fr-05:1492` nhưng
  **khác vế**; log riêng, trừ khi vì thế mà trường trở nên sai/không đọc được ⇒ khi đó rơi vào C3.
- **Dữ liệu / số hồ sơ trên env đối tác khác env nội bộ** — lệch env là bối cảnh, không phải lỗi.

### 🚫 KHÔNG được chấm **Pass** vì *(chống Pass oan)*

- ❌ **Thấy có nút "Xem" trên màn là đủ.** Yêu cầu chủ việc, nguyên văn: *"CẤM Pass bằng quan sát tĩnh."*
  Phải bấm thật, đọc nội dung cửa sổ, đối chiếu từng trường với bản ghi.
- ❌ **Lấy mẫu 2–3 hàng rồi suy ra cả bảng** — case này chính là "thiếu điều khiển trên hàng".
- ❌ **Chỉ đo trên hàng *Hiệu lực*** (bỏ *Hết hạn* / *Thu hồi*) — D3 là biến thể bắt buộc.
- ❌ **Chỉ đo hồ sơ có tệp** (bỏ D2) hoặc **chỉ đo hồ sơ điền đủ trường** (bỏ D4).
- ❌ **Kết luận 100% từ script chạy trong trang mà không mở ảnh ra đọc.**
- ❌ **Suy từ số đo env nội bộ 06/08** (bó mã `index-DIABnbIr.js`) sang bản dựng `index-D4NhKEjr.js` của env đích.
- ❌ **Đối chứng bằng cách bấm lại cùng nút** — không phải phương pháp độc lập.
- ❌ **Chỉ đo trên bảng DN QA** mà không đọc bảng của `DN-XX-0005` (chính bảng đối tác báo lỗi).

---

## 7. Cảnh báo dụng cụ — đọc TRƯỚC khi bấm

*(chép từ `tieuchi/QLHSPLDN_07.md` §4 Precondition — các bẫy đã làm hỏng số đo ở vòng trước)*

1. **Đếm tệp** phải dùng `.ant-upload-list-item-container` — **KHÔNG** `.ant-upload-list-item`.
2. **Đọc ô chọn** phải dùng `.ant-select-content` — **KHÔNG** `.ant-select-selection-item`.
3. **Điền ô** phải **đặt giá trị qua setter gốc + phát `input`/`change`**. `fill_form` / `Control+A`
   **NỐI CHUỖI** thay vì thay thế ⇒ phải **clear field trước**. (Áp cho bước seed T3–T5.)
4. **Bộ đếm request** phải bọc **cả `fetch` LẪN `XMLHttpRequest`** — vòng trước báo `SO_REQUEST = 0` vì
   thiếu XHR.
5. **Đọc chữ trên DOM** bằng `innerText`, **không** `textContent` (bắt node ẩn AntD → bug ma).
6. Bộ bắt thông báo: cài **TRƯỚC** khi bấm (bước seed), **CẤM dedupe**, tự kiểm `soObserverDangSong = 1`;
   observer bị xoá sau mỗi lần tải lại trang → **cài lại + kiểm lại**.
7. Đường gọi máy chủ để đối chứng **lấy từ chính request UI phát ra** (`list_network_requests`) —
   **CẤM đoán đường dẫn API, CẤM ghi thẳng CSDL**.
8. Nút submit form là **`Đồng ý`**, không phải `Lưu`. Row action `Sửa`/`Xoá` là thẻ `<a>`.
9. Ảnh lưu vào `F9-uatdoitac-QLHSPLDN-2026-08-07/image/`.

---

## 8. Câu hỏi BA — **chỉ gửi khi vế `d2` bị kích hoạt (ca lửng)**

> Không gửi nếu số đo là 0 ô nhập + 0 nút lưu, hoặc nếu cửa sổ Xem là đúng biểu mẫu Sửa (khi đó là lỗi, không
> phải câu hỏi).

**Câu hỏi 1 (chính — về vế d2):**
> Trên màn *Chi tiết doanh nghiệp* → thẻ **Hồ sơ pháp lý** dành cho **cán bộ nghiệp vụ**
> (`SCR-V.III-02`, `srs-fr-07-doanh-nghiep.md:455`), cửa sổ **Xem chi tiết hồ sơ pháp lý**
> (khối `Processing — Xem chi tiết`, `srs-fr-12-tv-chuyen-sau.md:647`) **có được phép chứa ô nhập hoặc cho
> chỉnh sửa tại chỗ không**, hay bắt buộc **chỉ đọc** giống quy định đã có cho màn của vai trò Doanh nghiệp
> (`srs-fr-07-doanh-nghiep.md:523` — *"Tab 2 — Hồ sơ pháp lý DN | tab | Read-only danh sách
> HO_SO_PHAP_LY_DN | Luôn"*, thuộc `SCR-V.III-04` ở `:508`)?
>
> **Vì sao hỏi:** ô *Kết quả mong đợi* của đối tác đòi *"ở chế độ chỉ đọc"*, nhưng SRS v3.5 **không có dòng
> nào** quy định điều này cho màn cán bộ — dòng duy nhất nói "Read-only" thuộc màn của vai trò Doanh nghiệp
> (`:514`: *"Vai trò khác KHÔNG truy cập trang này"*). Hiện trạng đo được trên env nghiệm thu: **`<điền số đo
> C5: n ô nhập, danh sách nút>`**. QA **chưa chấm đạt hay lỗi** vế này, chờ BA chốt.
>
> **BA trả lời bằng cách chọn 1:**
> - (A) Bắt buộc chỉ đọc ⇒ bổ sung dòng tương ứng vào `SCR-V.III-02` §Thành phần màn hình.
> - (B) Được phép chỉnh sửa tại chỗ ⇒ ghi rõ trong SRS, và QA sẽ chấm expected gốc của đối tác là **không áp**.
> - (C) Tuỳ triển khai, không ràng buộc ⇒ QA đóng vế này là **không phải lỗi**, ghi rõ SRS im lặng.

**Câu hỏi 2 (kèm theo, chỉ khi khi đo thấy thẻ thiếu ô tìm kiếm / bộ lọc / nút Xuất Excel):**
> `srs-fr-12-tv-chuyen-sau.md:589-597` khai **5 bộ lọc tìm kiếm** và `:657-665` khai hẳn khối
> **Processing — Xuất Excel** cho FR-X.1-04; nhưng mô tả thẻ ở `srs-fr-07-doanh-nghiep.md:468` chỉ ghi
> vỏn vẹn *"CRUD hồ sơ pháp lý DN"*. Thẻ **Hồ sơ pháp lý** trên màn chi tiết DN **có phải** hiển thị ô tìm
> kiếm/bộ lọc và nút Xuất Excel không? Nếu có, ở vị trí nào; nếu không, đề nghị gỡ hai khối trên khỏi
> FR-X.1-04 để hai chỗ hết mâu thuẫn.
