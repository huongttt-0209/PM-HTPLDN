# CHUẨN CHẤM — QLHSDNHTCP_03 (lô F7 · `Dopai = dev done` + `Trạng thái dev fix = Fixed`)

> **Khoá TRƯỚC khi mở màn.** Sau khi đo, CẤM đổi quan hệ `MATCH/DIFF/GAP` ở §4 để khớp kết quả.
> Phiếu này **KHÔNG có khối "CÁCH VERIFY sau khi dev fix"** trên bảng đối tác — file này khôi phục lại
> phép đo đã khoá từ bug entry nội bộ + dấu vết vòng trước + SRS bản chốt.

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Bảng đối tác · tab `bug` · **dòng 72** |
| Mã TC | **QLHSDNHTCP_03** — "Kiểm tra Cột dữ liệu trong bảng kết quả" |
| Các bước (đối tác) | `1. Chọn menu "Chi trả chi phí"` |
| Env đo lượt này | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu `htpldn-uat.ospgroup.vn` |
| Bản dựng lô F7 | `assets/index-eWHwDgt2.js` · deploy **09:11 giờ VN 07/08** ([../BAN-DUNG.md](../BAN-DUNG.md)) |
| Màn | Chi trả chi phí → Danh sách — **SCR-V.II-01** |
| URL | `https://18.143.165.120.nip.io/chi-tra/danh-sach?tab=TAT_CA&page=1` |

> 🔴 **Không được dùng lại kết quả vòng 06/08.** Vòng đó đo trên bó mã `index-DIABnbIr.js` (V1.0.8); lô F7
> chạy trên bó mã **khác hoàn toàn** (`index-eWHwDgt2.js`). Phải đo lại thật — xem [../BAN-DUNG.md](../BAN-DUNG.md).

---

## 1. Nguồn canonical đã xác định + ai viết ô "Kết quả verify"

### 1.1 Truy nguồn ô `T72` "Kết quả verify" — **KHÔNG phải QA ghi**

Đã quét **toàn bộ** `tools/*.log` + `tools/sheet_update_audit.jsonl` bằng parse JSON từng dòng (không grep chuỗi thô):

| Câu hỏi | Kết quả quét |
|---|---|
| QA từng ghi dòng 72 của tab `bug` chưa? | **Chưa bao giờ.** Tab `bug` chỉ có **4 dòng** từng bị QA ghi: `365` · `366` · `367` · `138`. **Không có dòng 72.** |
| QA từng ghi cột "Kết quả verify" chưa? | Có, **đúng 1 lần**: `tools/sheet_fix_row_fields.log:5` — `ts=2026-08-06T20:13:03`, **row 138** (`QLBMHD_02`), ô `T138`. **Không phải `T72`.** |
| QA từng ghi mã `QLHSDNHTCP_03` ở đâu? | **Đúng 1 lần, ở tab KHÁC:** `tools/sheet_write.log:196` — `ts=2026-07-20T17:45:26`, tab `UAT_TGPL Doanh Nghiệp-tuần 3`, **row 16**, ô `P16` (Trạng thái dev fix 1) + `R16` (DEV phản hồi lần 1), status `BA confirm`. |
| Chuỗi "tràn sang cột" có trong log ghi nào không? | **Không có trong bất kỳ log nào.** |

**⇒ Kết luận: ô `T72` do ĐỐI TÁC / TKM ghi, KHÔNG phải verdict của QA.** Ba dấu hiệu cùng chiều:

1. Ô `S72` "DEV phản hồi lần 1" **rỗng** — QA chưa từng chạm dòng này ở bất kỳ cột nào.
2. Ảnh kèm ở `U72` là `QLHSDNHTCP_03_v2.png` — ảnh chụp trên máy đối tác (thanh tác vụ Windows, dấu trang
   `Directus · CỔNG PH…`, khung đỏ do đối tác tự khoanh), trên env nghiệm thu `ospgroup.vn`, **10:53 ngày 30/07**.
3. Câu chữ ở `T72` trùng khít bản kết xuất phía đối tác `bug-con-fail-doi-tac-2026-07-31.md:94` (ngày 31/07).

### 1.2 Giá trị thực đọc từ bảng (chỉ đọc, không ghi) — `'bug'!A72:Y72`

| Ô | Cột | Giá trị |
|---|---|---|
| `K72` | Kết quả mong đợi | `- Hệ thống hiển thị các trường thông tin giống với thiết kế`<br>`- Dữ liệu hiển thị đúng định dạng và trường thông tin`<br>`- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị`<br>`- Mặc định: hệ thống sắp xếp theo ngày cập nhật mới nhất trước, 20 bản ghi mỗi trang.` |
| `L72` | Kết quả thực tế (vòng 1) | `Cột thông tin Mức cảnh báo thời hạn không giống với thiết kế` |
| `N72` | Trạng thái | `Fail` |
| `O72` | Dopai | `dev done` |
| `R72` | Trạng thái dev fix | `Fixed` |
| `S72` | DEV phản hồi lần 1 | *(rỗng)* |
| `T72` | Kết quả verify | `Dữ liệu cột "Mức cảnh báo thời hạn" bị tràn sang cột "Ngày nộp"` |
| `U72` | Ảnh/video verify | `QLHSDNHTCP_03_v2.png` |
| `V72` | Trạng thái 2 | `Fail` |

### 1.3 Nguồn canonical dùng để chấm lượt này

| Hạng | Nguồn | Vai trò |
|---|---|---|
| **1 — chuẩn chấm** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` | **Nguồn DUY NHẤT** ra verdict. Mọi số dòng ở §3 đều tự mở file đọc. 🔴 KHÔNG dùng `input/srs-update-2026-5-5/`. |
| **2 — quyết định đã chốt** | `reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-week-3.md:56-63` (**2026-07-24**) | BA đã chốt đúng điểm tranh chấp của case này. Xem §3.2. |
| **3 — 2 vế phải chấm** | `L72` (vòng 1) + `T72` (vòng 2) | Đây là **phạm vi case**. Ngoài 2 vế này = ghi nhận, không dùng chấm. |
| **4 — ngữ cảnh** | `flowtest-kiemdinh/tieuchi/QLHSDNHTCP_03.md` · `flowtest-kiemdinh/bug-report.md:141-245` | Chỉ để biết tra chỗ nào. **Không mượn số dòng, không dùng làm căn cứ verdict.** |

### 1.4 Hồ sơ nội bộ vòng trước — tóm tắt

| Vòng | Ngày | Tài khoản / vai trò | Màn · URL | Kết luận |
|---|---|---|---|---|
| Tuần 3 R8 | 25/07 | `cbnv_tw` (CB_NV_TW) | `/chi-tra/danh-sach` | **Pass** (dòng 16 tab tuần 3) — sau khi BA chốt 24/07 |
| FLOW 04 | 06/08 00:18–00:40 | `cbnv_tw` (CB_NV_TW) + `cbpd_tw_01` (CB_PD_TW) | `/chi-tra/danh-sach?tab=TAT_CA&page=1` | **Cần BA** — cả 2 vế đối tác đã hết lỗi (0 px tràn / 28 lượt đo dòng; đã hiện 4 nhãn rời), nhưng phát sinh **nhãn thứ 5 "Đã hoàn thành"** nằm ngoài BR-SLA-02 → chuyển BA |

> **Câu hỏi BA vẫn đang TREO** — `reverify-week-5/ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md:82` **Mục 15**,
> cột "Có treo verdict?" = ✅. Chưa có file phản hồi nào trả lời mục này (`phan-hoi-ba-7-diem-can-chot-2026-08-06.md`
> chỉ gồm 7 điểm LKHDG / QLNDTVVCG / BC thống kê vụ việc). **⇒ Điểm "Đã hoàn thành" vẫn KHÔNG được dùng để chấm.**

---

## 2. Ba dữ kiện neo từ ảnh đối tác

Ảnh đã tải về `../partner-evidence/` bằng `UAT_TAB=bug python3 tools/fetch_evidence.py --row 72` (vòng 1, cột `M72`)
và `--col-header "Ảnh/video verify"` (vòng 2, cột `U72`). **Đã mở xem full-res cả 2 ảnh.**

### (a) URL / màn đối tác đang đứng

| | Vòng 1 — `QLHSDNHTCP_03.jpg` (288.741 bytes) | Vòng 2 — `QLHSDNHTCP_03_v2.png` (267.652 bytes) |
|---|---|---|
| URL trên thanh địa chỉ | `htpldn-uat.ospgroup.vn/chi-tra/danh-sach` | `htpldn-uat.ospgroup.vn/chi-tra/danh-sach?tab=TAT_CA&page=1` |
| Breadcrumb | `Trang chủ / Chi trả chi phí / Danh sách` | `Trang chủ / Chi trả chi phí / Danh sách` |
| Tab đang chọn | **Tất cả** | **Tất cả** (badge `5`) |
| Đồng hồ máy | **10:09 · 2026-07-10** | **10:53 · 2026-07-30** |

### (b) Vai trò / tài khoản trong ảnh

| | Vòng 1 | Vòng 2 |
|---|---|---|
| Tên hiển thị | **CB Nghiệp vụ TW 01** | **Cán bộ PD Bộ ngành** |
| Mã vai trò góc phải | **`CB_NV_TW`** | **`CB_PD_BN`** |
| Đơn vị | **`BTP · TW`** | **`BTP · BN`** |
| Chuỗi bản dựng chân sidebar | **`HTPLDN · V1.0`** | **`HTPLDN · V1.0.2`** |

> ⚠️ **Hai vòng KHÔNG cùng điều kiện:** khác vai trò, khác cấp đơn vị, khác bản dựng, khác bộ bản ghi
> (V1: `HSCT000066`–`000070` · V2: `HSCT000051`–`000055`). Không coi vòng 2 là "vòng 1 chụp lại".

### (c) Cột nào tràn sang cột nào, chữ gì bị đè

**Thứ tự cột đọc được trên ảnh (cả 2 vòng giống nhau):**
`Mã HS` → *(cột tên DN — **ô tiêu đề để trống**)* → `Quy mô DN` → `Số tiền đề nghị` → `Số tiền được duyệt` →
`Mức HT %` → `Trạng thái` → **`SLA`** → **`Ngày nộp`** → `Hành động`

**Vòng 1 (`.jpg`) — chưa tràn, nhưng thiếu nhãn mức:** ô cột `SLA` chỉ có **đếm ngày trần**, không có nhãn mức:
`Quá hạn 58 ngày LV` · `Quá hạn 60 ngày LV` · `Quá hạn 61 ngày LV` · `Quá hạn 62 ngày LV` · `Quá hạn 64 ngày LV`.
Cột `Ngày nộp` đọc **đủ 10 ký tự** ở cả 5 dòng (`05/04/2026` · `03/04/2026` · `01/04/2026` · `30/03/2026` · `28/03/2026`).
Chân bảng: `Hiển thị 1-5 / 5 kết quả` · bộ chọn `20 / trang`.

**Vòng 2 (`_v2.png`) — chính là chỗ tràn.** Khung đỏ đối tác khoanh **2 dòng đầu**:

| Dòng | Trạng thái | Nội dung ô `SLA` | Hệ quả trên cột `Ngày nộp` |
|---|---|---|---|
| `HSCT000051` | Đang thẩm định | thẻ **nền đen** `Quá hạn nghiêm trọng · 52 ngày LV` | thẻ kéo dài **đè lên** ô Ngày nộp — chỉ còn đọc được **3 ký tự cuối `026`** |
| `HSCT000052` | Yêu cầu bổ sung | thẻ **nền đen** `Quá hạn nghiêm trọng · 54 ngày LV` | y hệt — chỉ còn **`026`** |
| `HSCT000053` | Đã thanh toán | thẻ ngắn `Đã hoàn thành` | nằm gọn trong ô — Ngày nộp đọc đủ `01/05/2026` |
| `HSCT000054` | Từ chối | thẻ ngắn `Đã hoàn thành` | đọc đủ `29/04/2026` |
| `HSCT000055` | Đã thanh toán | thẻ ngắn `Đã hoàn thành` | đọc đủ `27/04/2026` |

**⇒ Cột tràn = `SLA` (thành phần #16). Cột bị đè = `Ngày nộp` (thành phần #17). Chữ bị đè = giá trị ngày
`dd/mm/yyyy`, chỉ sót lại 3 ký tự cuối `026`. Chỉ tràn ở nhãn dài nhất `Quá hạn nghiêm trọng` (20 ký tự).**

> 🔎 **Quan hệ nhân quả giữa 2 vòng:** vòng 1 ô SLA chỉ có đếm ngày trần (chuỗi ngắn) → không tràn.
> Dev sửa vế (a) bằng cách **thêm nhãn mức** → chuỗi dài ra → sinh ra vế (b) tràn. ⇒ **Phải chấm cả 2 vế
> trong CÙNG một lượt đo**, không được đóng vế này làm hỏng vế kia.

---

## 3. Bảng dòng SRS đã mở đọc

**Nguồn chuẩn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.
Mọi dòng dưới đây **tự mở file đọc**, không lấy từ trí nhớ / không lấy từ phiếu UAT.

### 3.1 `srs-fr-06-chi-tra.md` (1.565 dòng) — SCR-V.II-01 Danh sách Hồ sơ Chi trả

Đã đọc trọn khối `:1030–1082` (đầu mục → hết Quy tắc tương tác).

| Dòng | Nguyên văn (rút gọn đúng chữ) |
|---|---|
| `:1030` | `### SCR-V.II-01: Danh sách Hồ sơ Chi trả` |
| `:1035` | `**URL pattern:** /chi-tra/danh-sach` |
| `:1036` | `**Quyền truy cập:** CB NV (TW/BN/ĐP), CB PD (TW/BN/ĐP). Phân quyền theo phạm vi đơn vị (TW → toàn quốc, BN → chỉ BN, ĐP → chỉ ĐP).` |

**Bảng thành phần màn hình — 19 thành phần, `:1043–1061`. Trích đúng đoạn cột bảng dữ liệu:**

| # | Dòng | Nguyên văn |
|---|---|---|
| 9 | `:1051` | `\| 9 \| table \| Checkbox \| checkbox \| Chọn dòng (40px) \| click → select \| Luôn \|` |
| 10 | `:1052` | `\| 10 \| table \| Mã HS \| text (link) \| CT-{YYYYMMDD}-{SEQ} (160px) \| click → SCR-V.II-02 (chi tiết) \| Luôn \|` |
| 11 | `:1053` | `\| 11 \| table \| Tên DN \| text \| ten_doanh_nghiep (200px) \| — \| Luôn \|` |
| 12 | `:1054` | `\| 12 \| table \| Quy mô DN \| badge \| Nhãn hiển thị: "Siêu nhỏ" / "Nhỏ" / "Vừa" (map từ enum \`quy_mo_dn\` — 80px) \| — \| Luôn \|` |
| 13 | `:1055` | `\| 13 \| table \| Số tiền đề nghị \| number \| Giá trị \`so_tien_de_nghi\` (định dạng VNĐ, dấu chấm hàng nghìn, hậu tố "đ") (130px) \| — \| Luôn \|` |
| 14 | `:1056` | `\| 14 \| table \| Số tiền được duyệt \| number \| Giá trị \`so_tien_duoc_duyet\` (VNĐ). "—" nếu chưa duyệt (130px) \| — \| Luôn \|` |
| 15 | `:1057` | `\| 15 \| table \| Trạng thái \| C06 badge \| 10 trạng thái SM-CHITRA với màu tương ứng (140px) \| — \| Luôn \|` |
| **16** | **`:1058`** | **`\| 16 \| table \| SLA \| C07 \| 4 mức cảnh báo theo BR-SLA-02: Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng (80px) \| — \| Luôn \|`** |
| **17** | **`:1059`** | **`\| 17 \| table \| Ngày nộp \| date \| dd/mm/yyyy (110px) \| — \| Luôn \|`** |
| 18 | `:1060` | `\| 18 \| table \| Hành động \| buttons \| Tùy theo trạng thái: [Kiểm tra] / [Đánh giá] / [Thẩm định] / [Trình PD] / [Phê duyệt] / [Cập nhật TT] (100px) \| click → SCR-V.II-02 tại section tương ứng \| Luôn \|` |
| **19** | **`:1061`** | **`\| 19 \| pagination \| Phân trang \| C05 \| 20 mục/trang \| click → chuyển trang \| Luôn \|`** |

**Quy tắc tương tác `:1078–1082`:**

| Dòng | Nguyên văn |
|---|---|
| `:1080` | `- Phân quyền: TW → toàn quốc, BN → chỉ BN, ĐP → chỉ ĐP` |
| **`:1081`** | **`- Sắp xếp mặc định: ngày cập nhật DESC`** |
| `:1082` | `- Nguồn duy nhất: DVC qua LGSP — CB NV KHÔNG nhập tay hồ sơ chi trả` |

### 3.2 `srs-fr-06-chi-tra.md` — BR-SLA-02 (giá trị của cột SLA)

| Dòng | Nguyên văn |
|---|---|
| `:1311` | `\| muc_do_canh_bao \| text \| N \| CHECK IN ('BINH_THUONG','SAP_HET','QUA_HAN','QUA_HAN_NGHIEM_TRONG') \| 'BINH_THUONG' \| Mức cảnh báo SLA hồ sơ chi trả theo BR-SLA-02 (Bình thường >50% còn lại / Sắp hết hạn <50% / Quá hạn >100% / Quá hạn nghiêm trọng >200%). … (BA điều chỉnh 2026-07-24 — bỏ mô hình 70/85 riêng của Chi trả).` |
| `:1514` | `**Ngưỡng cảnh báo SLA cho hồ sơ chi trả — dùng chung BR-SLA-02 (BA điều chỉnh 2026-07-24, bỏ mô hình 70/85 riêng):**` |
| `:1516-1517` | header bảng: `\| Mức (mã DB) \| Nhãn hiển thị \| Điều kiện \|` |
| `:1518` | `` \| `BINH_THUONG` \| Bình thường \| Còn > 50% thời lượng SLA \| `` |
| `:1519` | `` \| `SAP_HET` \| Sắp hết hạn \| Còn < 50% thời lượng SLA \| `` |
| `:1520` | `` \| `QUA_HAN` \| Quá hạn \| Đã quá deadline (> 100%) \| `` |
| `:1521` | `` \| `QUA_HAN_NGHIEM_TRONG` \| Quá hạn nghiêm trọng \| Trễ vượt > 200% thời lượng SLA \| `` |
| `:1523` | `**Quy tắc ưu tiên mức:** \`QUA_HAN_NGHIEM_TRONG\` > \`QUA_HAN\` > \`SAP_HET\` > \`BINH_THUONG\`. … **Nếu không thỏa điều kiện nào thì hiển thị "Bình thường".**` |

**Quyết định BA 2026-07-24** (`reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-week-3.md:56-63`):
1. *"Tên cột **"SLA"** của app **khớp đặc tả**"* ⇒ kỳ vọng đối tác về tên `Mức cảnh báo thời hạn` **đã bị BA bác**.
2. *"Dev sửa lại hiển thị theo BR-SLA-02 … app hiện **4 nhãn rời** … + **giữ số ngày** còn lại"* ⇒ **bắt buộc**.

### 3.3 `srs-v3.5.md` (7.012 dòng) — quy tắc chung áp cho C3 / C4

| Dòng | Nguyên văn |
|---|---|
| `:518` | `\| C-05 \| Ngôn ngữ \| Giao diện tiếng Việt, Unicode UTF-8 \| Yêu cầu CĐT \| ✅ CĐT xác nhận \|` |
| `:692` | `\| P-01 \| Danh sách quản lý (List Management) \| Bảng dữ liệu + Tìm kiếm + Lọc + Phân trang (10/20/50/100 bản ghi/trang, hiển thị tổng số bản ghi) + CRUD + Xuất Excel + Chọn hàng loạt + **Tabs trạng thái** … \| ~60% UC: … V.II (UC68-80) … \|` |
| `:861` | `> **EC-DATA-PAGE — Ràng buộc Pagination:** Số bản ghi/trang nằm trong khoảng [1, 100], **mặc định 20**. Số trang >= 1, mặc định 1. … Luôn hiển thị tổng số bản ghi ở màn danh sách.` |
| `:4703` | `\| I18N-07 \| Thuật ngữ kỹ thuật \| Sử dụng tiếng Anh cho thuật ngữ kỹ thuật **trong code, API** (field names, endpoint paths). **Giao diện hiển thị tiếng Việt** \| 🟡 Đề xuất \|` |

### 3.4 🔴 Chỗ SRS **IM LẶNG** — đã quét từ đồng nghĩa, xác nhận không có

Quét trên `srs-fr-06-chi-tra.md`: `tràn` · `đè lên` · `cắt chữ` · `truncate` · `ellipsis` · `xuống dòng` · `wrap` · `tooltip`.
**Không có dòng nào** quy định hành vi khi nội dung ô dài hơn bề rộng cột. (2 kết quả trúng `tooltip` là
`:17` — changelog, và `:1136` — tooltip `uuid_dvc` ở màn chi tiết; **cả hai không liên quan cột SLA**.)

**⇒ SRS KHÔNG có luật trình bày "không được tràn/đè".** Bề rộng `(80px)` ở `:1058` là **gợi ý thiết kế**,
không có câu nào bắt buộc render đúng 80px. Hệ quả xử lý: xem C2 ở §4.

---

## 4. Bảng vế C1–C4 — quan hệ MATCH / DIFF / GAP

> Quan hệ so **kỳ vọng gốc trên phiếu (`K72` + `L72` + `T72`)** ↔ **SRS v3.5 hiện tại**.

| Vế | Kỳ vọng gốc (phiếu đối tác) | SRS v3.5 nói gì | Quan hệ |
|:--:|---|---|:--:|
| **C1a** | Cột tên **"Mức cảnh báo thời hạn"** (`L72`) | `:1058` — tên cột là **`SLA`**, ở vị trí **#16**, giữa `Trạng thái` (#15) và `Ngày nộp` (#17) | **DIFF** |
| **C1b** | "trường thông tin giống với thiết kế" (`K72` ý 1) — cột phải có mặt | `:1058` điều kiện hiển thị **`Luôn`** — cột SLA luôn có mặt | **MATCH** |
| **C1c** | "đúng định dạng" (`K72` ý 2) — giá trị cột SLA | `:1058` + `:1514-1523` — **4 nhãn mức rời**; BA 2026-07-24 chốt **kèm số ngày** | **MATCH** |
| **C2a** | "không bị **tràn/đè lên nhau**" (`K72` ý 3) + `T72` | **SRS im lặng** — không có luật render overflow (§3.4) | **GAP** |
| **C2b** | *(hệ quả nghiệp vụ của C2a)* Ngày nộp phải đọc được | `:1059` — `Ngày nộp \| date \| dd/mm/yyyy` điều kiện hiển thị **`Luôn`** ⇒ bị che = **không thoả `Luôn`** | **MATCH** |
| **C3** | "đồng nhất ngôn ngữ hiển thị" (`K72` ý 3) | `:518` C-05 *giao diện tiếng Việt* · `:4703` I18N-07 *thuật ngữ tiếng Anh chỉ trong code/API, giao diện tiếng Việt* · `:1518-1521` nhãn hiển thị là **chữ Việt**, không phải mã `QUA_HAN_NGHIEM_TRONG` | **MATCH** |
| **C4a** | "sắp xếp theo **ngày cập nhật mới nhất trước**" (`K72` ý 4) | `:1081` — `Sắp xếp mặc định: ngày cập nhật DESC` | **MATCH** |
| **C4b** | "**20 bản ghi mỗi trang**" (`K72` ý 4) | `:1061` — `20 mục/trang` · `:861` EC-DATA-PAGE **mặc định 20** · `:692` P-01 | **MATCH** |
| **C5** *(phát sinh)* | *(đối tác không nêu)* | **SRS im lặng** — không quy định cột SLA hiển thị gì khi hồ sơ **đã kết thúc**; `:1523` chỉ nói *"không thỏa điều kiện nào thì hiển thị Bình thường"* | **GAP — đang treo BA** |

### 4.1 Cách xử lý từng quan hệ

**C1a = DIFF → KHÔNG chấm Fail.** BA đã chốt 2026-07-24 rằng tên **`SLA` khớp đặc tả**; kỳ vọng đối tác về
tên `Mức cảnh báo thời hạn` **đã bị BA bác**. Đây là **áp quyết định có sẵn**, không phải QA tự bác đối tác.
Nếu lượt đo thấy tiêu đề cột là `SLA` → **đúng**, ghi nhận và đi tiếp.

**C2a = GAP → KHÔNG chấm bằng luật trình bày.** SRS không có câu nào cấm tràn, cũng không bắt cột rộng đúng 80px.
**⇒ CẤM chấm Fail vì "nhìn thấy chữ tràn"**, và CẤM chấm Fail vì cột không đúng 80px.
Chấm qua **C2b** — hệ quả nghiệp vụ đo được: `Ngày nộp` có điều kiện hiển thị `Luôn` (`:1059`), nên nếu giá trị
ngày bị phần tử khác phủ / không đọc đủ `dd/mm/yyyy` thì **`Luôn` không thoả** ⇒ đó mới là căn cứ Fail.

**C5 = GAP đang treo BA → CẤM dùng để chấm.** Mục 15 `cau-hoi-BA-tong-hop-2026-08-06.md:82` chưa có phản hồi.
Nếu lượt đo lại thấy nhãn `Đã hoàn thành`: **ghi nhận + giữ verdict "cần BA"**, KHÔNG chấm Fail, KHÔNG chấm Pass sạch.

### 4.2 ✅ PASS khi — thoả **cả 4**

1. **Nhãn mức rời (C1c):** với mọi dòng có hồ sơ **còn đang xử lý** (trạng thái chưa kết thúc), ô cột `SLA` chứa
   **nguyên văn 1 trong 4 chuỗi** `Bình thường` / `Sắp hết hạn` / `Quá hạn` / `Quá hạn nghiêm trọng` — khớp đúng
   mức `muc_do_canh_bao` của dòng đó — **kèm số ngày**. Ô chỉ có đếm ngày trần kiểu `Quá hạn 58 ngày LV` ⇒ **chưa đạt**.
2. **Không chồng lấn (C2b):** với mọi dòng, phần chồng lấn **theo trục ngang** giữa hộp bao **nội dung** ô `SLA`
   và hộp bao ô `Ngày nộp` **= 0 px**.
3. **Ngày nộp đọc được (C2b):** với mọi dòng, giá trị `Ngày nộp` hiện **đủ 10 ký tự** `dd/mm/yyyy`, và phép chạm
   điểm giữa ô trả về phần tử **thuộc chính ô Ngày nộp** (không bị phần tử khác phủ lên).
4. **Mặc định danh sách (C3 + C4):** chân bảng hiện `20 / trang`; thứ tự dòng theo **ngày cập nhật giảm dần**;
   không có chuỗi tiếng Anh / mã kỹ thuật (`QUA_HAN_NGHIEM_TRONG`, `null`, `undefined`) lộ trong bảng.

### 4.3 ❌ FAIL nếu — **bất kỳ** điều nào

- ≥1 dòng có ô `SLA` chồng lấn **> 0 px** sang ô `Ngày nộp`.
- ≥1 dòng có `Ngày nộp` bị che một phần / không đọc đủ 10 ký tự.
- ≥1 dòng hồ sơ **đang xử lý** vẫn hiện đếm ngày trần **không kèm** nhãn mức BR-SLA-02.
- Bảng lộ mã kỹ thuật thay cho nhãn tiếng Việt, hoặc mặc định ≠ 20 bản ghi/trang, hoặc thứ tự ≠ ngày cập nhật DESC.

### 4.4 ⚠️ KHÔNG được chấm Fail vì

| Bẫy | Lý do |
|---|---|
| Tiêu đề cột là **`SLA`** chứ không phải `Mức cảnh báo thời hạn` | **BA chốt 2026-07-24** — tên `SLA` khớp đặc tả (C1a = DIFF đã giải) |
| Cột `SLA` **không rộng đúng 80px** | `(80px)` ở `:1058` là gợi ý thiết kế; SRS im lặng về bề rộng render thật |
| Nhìn thấy chữ "có vẻ" tràn **khi chưa cuộn ngang** | Cột `Hành động` **dán cố định** che phần bên phải ở vị trí cuộn mặc định → dễ tưởng nhầm đè |
| Nhãn thứ 5 **`Đã hoàn thành`** ở hồ sơ đã kết thúc | **C5 = GAP đang treo BA** (Mục 15) — ghi nhận, không chấm |
| Cột **`Mức HT %`** có trên app nhưng **không có** trong 19 thành phần `:1043-1061` | **Ngoài phạm vi 2 vế đối tác** — ghi "phát hiện thêm", không dùng chấm case này |
| **Ô tiêu đề cột Tên DN để trống** (thấy ở cả 2 ảnh đối tác) dù `:1053` ghi `Tên DN` | **Ngoài phạm vi 2 vế** — ghi "phát hiện thêm", không dùng chấm case này |

---

## 5. Cách đo từng bước cho người chạy trình duyệt

### 5.1 Tiền đề bắt buộc — kiểm TRƯỚC khi đo

| Hạng mục | Yêu cầu | Vì sao |
|---|---|---|
| Bản dựng | **Tải lại trang** rồi ghi lại bó mã `assets/index-*.js` | Tab MCP mở lâu vẫn chạy JS cũ → đã có tiền lệ báo Reopen oan |
| Số dòng bảng | **≥1 dòng**; nếu bảng rỗng ⇒ **phép đo vô nghĩa**, dừng, mark thiếu tiền đề | Không có dòng thì không đo được chồng lấn |
| Mức cảnh báo | **BẮT BUỘC ≥1 hồ sơ mức `QUA_HAN_NGHIEM_TRONG`** | `Quá hạn nghiêm trọng` = **20 ký tự**, chuỗi dài nhất ⇒ dạng dễ tràn nhất. **Thiếu mức này thì KHÔNG kết luận được** — đúng dạng đã gây ra lỗi ở ảnh vòng 2 |
| Độ phủ | Nên có đủ **M = 4/4** mức BR-SLA-02 | Case là bug về **cột hiển thị dữ liệu** ⇒ M **không được** = 1 |
| Khung nhìn | **1440×900** hoặc hẹp hơn | Hẹp hơn khung đối tác ⇒ phép đo **ngặt hơn**, không dễ dãi hơn |

> Không đủ hồ sơ `QUA_HAN_NGHIEM_TRONG` → **seed**, và **khai vào báo cáo**: đổi bản ghi nào, đổi gì, env nào.
> Lượt 06/08 env này sẵn **14 hồ sơ `CT-*` phủ 4/4 mức** — kiểm lại trước, nhiều khả năng không cần seed.

### 5.2 Tài khoản — phải khớp vai trò trong ảnh đối tác

Nguồn: [`../../../input/input.md`](../../../input/input.md).

| Lượt | Vai trò trong ảnh | Tài khoản | Mật khẩu | Ghi chú |
|---|---|---|---|---|
| **1** | **`CB_NV_TW`** (ảnh vòng 1) | **`cbnv_tw`** | `Test@1234` | Trùng khít vai trò + cấp đơn vị `BTP · TW` của vòng 1 |
| **2** | **`CB_PD_BN`** (ảnh vòng 2) | `cbpd_bn` → **fallback `cbpd_tw_01`** | `Test@1234` | Xem cảnh báo dưới |

> ⚠️ **`cbpd_bn` cấp BN có 0 hồ sơ chi trả** (đã xác minh lượt 06/08) → không đo được. Fallback đúng **Rule 7**:
> giữ **cùng vai trò CB Phê duyệt**, đổi cấp sang TW = **`cbpd_tw_01`** (`cbpd_tw` gốc đang lỗi đăng nhập 401
> `ERR-AUTH-LOGIN-01`, xem `input/input.md:26-34`). **BẮT BUỘC khai tài khoản thực dùng trong báo cáo.**
> Đo 2 vai trò vì **bộ cột khác nhau** (CB PD có thêm ô chọn dòng + nút thao tác khác ⇒ độ rộng cột khác).
> **KHÔNG dùng `admin`** ra verdict cho case này.

### 5.3 Các bước

1. Đăng nhập `cbnv_tw` / `Test@1234` (OTP MailHog `http://18.143.165.120:8025`).
2. **Click sidebar** `Chi trả chi phí` (KHÔNG `navigate_page` — mất phiên). Vào tab **`Tất cả`**.
   Xác nhận URL = `/chi-tra/danh-sach?tab=TAT_CA&page=1`, không nhập từ khoá, không bật bộ lọc nào.
3. **Ghi lại chân bảng**: chuỗi `Hiển thị 1-N / T kết quả` + bộ chọn `… / trang` → phục vụ **C4b**.
4. **Chụp thứ tự dòng** + đọc `ngày cập nhật` để kiểm **C4a** (DESC). Nếu bảng không hiện cột ngày cập nhật,
   đối chiếu thứ tự `id` trả về ở `GET /api/v1/ho-so-chi-tras` (`list_network_requests`).
5. **Cuộn bảng sang phải** cho tới khi cột `SLA` **và** cột `Ngày nộp` **cùng nằm trong tầm nhìn**
   *(bỏ bước này = bẫy §4.4)*. Đo ở **2 vị trí cuộn**: mặc định + cuộn hết sang phải.
6. Chạy **script đo §5.4**. Ghi lại bảng số cho **từng dòng**.
7. Chụp ảnh vào `../image/` (đúng kỷ luật ảnh của dự án), tên gồm mã TC + vai trò + ngày.
8. **Đăng xuất sạch** (`POST /api/v1/auth/logout` + clear `localStorage`/`sessionStorage`), lặp bước 1–7
   bằng **`cbpd_tw_01`**.

### 5.4 Script đo — chứng minh bằng SỐ, không bằng cảm tính

Chạy qua `mcp__chrome-devtools__evaluate_script`. **Đây là bằng chứng quyết định**, ảnh chỉ là phụ.

```js
() => {
  const heads = [...document.querySelectorAll('.ant-table-thead th')].map(t => t.innerText.trim());
  const iSLA  = heads.findIndex(h => /^SLA|Mức cảnh báo/i.test(h));
  const iDate = heads.findIndex(h => /Ngày nộp/i.test(h));
  if (iSLA < 0 || iDate < 0) return { LOI: 'Không thấy cột SLA hoặc Ngày nộp', heads };

  const rows = [...document.querySelectorAll('.ant-table-tbody tr.ant-table-row')];
  const out = rows.map(tr => {
    const tds  = tr.querySelectorAll('td');
    const cSLA = tds[iSLA], cDate = tds[iDate];
    // hộp bao NỘI DUNG ô SLA (thẻ badge bên trong), không phải hộp bao <td>
    const inner = cSLA.querySelector('.ant-tag, .ant-badge, span, div') || cSLA;
    const a = inner.getBoundingClientRect();       // nội dung ô SLA
    const b = cDate.getBoundingClientRect();       // ô Ngày nộp
    const s = cSLA.getBoundingClientRect();        // ô SLA

    // 1) chồng lấn NGANG giữa nội dung SLA và ô Ngày nộp
    const overlapPx = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
    // 2) nội dung có nằm trọn trong ô của nó không (số âm = nằm trong)
    const spillRight = +(a.right - s.right).toFixed(1);
    // 3) nội dung có bị cắt ngầm không
    const clipped = inner.scrollWidth > inner.clientWidth + 1;
    // 4) phép CHẠM ĐIỂM GIỮA ô Ngày nộp: phần tử trên cùng phải thuộc chính ô đó
    const top = document.elementFromPoint(b.left + b.width / 2, b.top + b.height / 2);
    const dateCovered = !(top && cDate.contains(top));
    const dateText = (cDate.innerText || '').trim();

    return {
      ma:   (tds[iSLA - 1] ? '' : '') || tr.innerText.split('\n')[0],
      sla:  (cSLA.innerText || '').trim().replace(/\s+/g, ' '),
      ngayNop: dateText,
      overlapPx: +overlapPx.toFixed(1),
      spillRight, clipped, dateCovered,
      dateDu10: /^\d{2}\/\d{2}\/\d{4}$/.test(dateText),
    };
  });

  return {
    soDong: out.length,
    viewport: `${innerWidth}x${innerHeight}`,
    // ==== 4 con số ra verdict ====
    maxOverlapPx:  Math.max(0, ...out.map(r => r.overlapPx)),
    soDongTran:    out.filter(r => r.overlapPx > 0).length,
    soDongNgayBiChe: out.filter(r => r.dateCovered || !r.dateDu10).length,
    soDongThieuNhan: out.filter(r =>
      !/(Bình thường|Sắp hết hạn|Quá hạn nghiêm trọng|Quá hạn|Đã hoàn thành)/.test(r.sla)).length,
    chiTiet: out,
  };
};
```

**Đọc kết quả:**

| Số đo | Ngưỡng PASS | Ứng với vế |
|---|---|---|
| `maxOverlapPx` | **= 0** | C2b — chồng lấn ngang |
| `soDongTran` | **= 0** | C2b |
| `soDongNgayBiChe` | **= 0** | C2b — `:1059` điều kiện `Luôn` |
| `soDongThieuNhan` | **= 0** (bỏ qua dòng hồ sơ đã kết thúc) | C1c — 4 nhãn BR-SLA-02 |
| `chiTiet[].sla` | chứa nhãn Việt **+ số ngày**, không lộ mã `QUA_HAN_*` | C1c + C3 |

> `spillRight` **âm** = nội dung nằm trong ô (lượt 06/08 xấu nhất **−8 px**). `clipped = true` ở dòng nào thì
> ghi rõ — nội dung bị cắt ngầm cũng là một dạng không đọc được, phải nêu trong báo cáo dù C2a là GAP.

**Đối chiếu chéo bắt buộc (3-Step Verify §3):** gọi `GET /api/v1/ho-so-chi-tras` qua `list_network_requests`,
so `mucDoCanhBao` của từng bản ghi với nhãn UI đang hiện. Lệch UI ↔ API (ví dụ API trả `BINH_THUONG` mà UI
hiện `Đã hoàn thành`) ⇒ **ghi cả 2 trong báo cáo**, đừng chỉ tin UI.

### 5.5 Ranh giới verdict

| Kết quả đo | Verdict |
|---|---|
| Thoả cả 4 điều §4.2 **và** không thấy nhãn `Đã hoàn thành` | **Pass** |
| Thoả cả 4 điều §4.2 **nhưng** vẫn thấy nhãn `Đã hoàn thành` ở hồ sơ đã kết thúc | **Cần BA** *(giữ nguyên như lượt 06/08 — C5 chưa được trả lời)* |
| Vi phạm bất kỳ điều nào §4.3 | **Reopen** — kèm bảng số `chiTiet` + ảnh + bó mã `index-*.js` |
| Bảng rỗng / thiếu mức `QUA_HAN_NGHIEM_TRONG` và không seed được | **Không kết luận được** — mark thiếu tiền đề, KHÔNG chấm Pass |
