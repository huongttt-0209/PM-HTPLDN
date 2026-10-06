# Chuẩn chấm đã khóa — 21 phiếu "Kiểm tra chức năng Xuất PDF" (màn Báo cáo thống kê)

> **Khóa trước khi đo.** Người đo KHÔNG được tự thêm/bớt tiêu chí giữa chừng. Thấy điều gì ngoài bảng này →
> ghi "Ghi nhận thêm", báo lại, KHÔNG tự lật verdict.

**Nguồn đặc tả — DUY NHẤT của lô này (prompt session chỉ định):**
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
— `srs-fr-11-bao-cao.md` (1.295 dòng) · `srs-v3.5.md` (7.012 dòng) · `srs-fr-05-vu-viec.md` (2.506 dòng).

Mọi số dòng dưới đây **agent viết chuẩn tự mở file đọc lại lúc 18:25–18:30 ngày 2026-08-07**.
Không quote từ trí nhớ, không quote từ `input/srs-update-2026-5-5/`, không quote từ báo cáo đợt cũ.

**Nguồn quyết định nghiệp vụ:** `../../reverify-week-5/ba-confirm/phan-hoi-ba-7-diem-can-chot-2026-08-06.md`
**mục 5** (`:373`–`:441`) — trích nguyên văn ở §2.

**Tiền lệ đã đọc (không chấm lại thứ đã chốt):**
`../../reverify-round-2026-08-05/RECIPE.md` §6 · `../../reverify-round-2026-08-05/cond/SLHDVM_07.md` ·
`../../reverify-week-5/F7-devdone-fixed-2026-08-07/chuan/chuan-14-case-bctk.md` ·
`../../reverify-week-5/F7-devdone-fixed-2026-08-07/bao-cao-lo-F7-2026-08-07.md` §2.

---

## 🔎 SRS có lệch so với bản đọc sáng 07/08 không? — **KHÔNG LỆCH**

Đã đối chiếu **toàn bộ 20 dòng** mà `chuan-14-case-bctk.md` §1 dẫn. **20/20 khớp cả số dòng lẫn nguyên văn.**
Không có dấu hiệu SRS bị sửa tiếp trong ngày.

Bằng chứng bổ trợ — dấu thời gian tệp đọc lúc 18:30 ngày 07/08:

| Tệp | Sửa lần cuối | md5 |
|---|---|---|
| `srs-fr-11-bao-cao.md` | 2026-08-06 22:52:29 | `09cbbc41d86e07d00b7ecef3142ef8c4` |
| `srs-v3.5.md` | 2026-08-06 22:52:29 | `f6d98d75bfee67a19ae3639595beb000` |
| `srs-fr-05-vu-viec.md` | 2026-08-04 17:17:40 | `38bf3b276e7cc24f2f221b5b5cfcd66d` |

Cả ba tệp **không bị chạm trong ngày 07/08** ⇒ số dòng mà lô F7 dùng sáng nay vẫn còn hiệu lực nguyên vẹn.
**Vẫn phải mở file đọc lại nếu lô này kéo dài sang ngày khác** — đợt trước đã có tiền lệ SRS bị sửa làm lệch ±5 dòng.

---

## §0. Phạm vi

**21 phiếu, cùng MỘT cụm lỗi, cùng MỘT màn** `/bao-cao` (Báo cáo thống kê), **định dạng xuất là PDF cho cả 21**.

- Ô `Kết quả thực tế` (đối tác, 16/07): *Hệ thống hiển thị thông báo "Không thể tạo file xuất. Vui lòng thử lại."*
- Ô `TKM phản hồi lần 1` (31/07): *Hệ thống hiển thị thông báo "Forbidden"* — triệu chứng của vai trò Quản trị hệ thống.
- Ô `Kết quả mong đợi` (đối tác): PDF theo mẫu Thông tư 17/2025/TT-BTP — khổ A4, Times New Roman 13, đầu trang
  có quốc hiệu + tên cơ quan, cuối trang có ngày ký + **chức danh người ký**, tên tệp
  `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`, **hỗ trợ ký số**.
- **Env đo:** `https://18.143.165.120.nip.io` (env **nội bộ**, không phải env nghiệm thu của đối tác).
- **Bản dựng hiện tại:** bó mã `assets/index-BbPPdate.js`, `last-modified: Fri, 07 Aug 2026 06:47:57 GMT`
  (= 13:47:57 giờ VN 07/08) — **mới hơn** bó mã `index-eWHwDgt2.js` mà lô F7 đo lúc sáng (triển khai 09:11 giờ VN)
  ⇒ **không kế thừa được kết quả sáng nay**, phải đo lại thật (xem §5 bẫy 13).

### Bảng 21 dòng (tab `bug`, spreadsheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, gid 1714340219)

| # | Row | Mã TC | Loại báo cáo chọn trên màn | UC | Định dạng |
|---:|---:|---|---|---|---|
| 1 | 175 | SLHDVM_07 | BC Số lượng hỏi đáp/vướng mắc pháp luật | UC124 | PDF |
| 2 | 180 | VVDTN_07 | BC Vụ việc đã tiếp nhận | UC125 | PDF |
| 3 | 186 | VVDHT_07 | BC Vụ việc đang hỗ trợ | UC126 | PDF |
| 4 | 190 | VVDHTHT_07 | BC Vụ việc đã hoàn thành | UC127 | PDF |
| 5 | 196 | VVTTG_06 | BC Vụ việc theo thời gian | UC128 | PDF |
| 6 | 201 | CLDTBDDDR_07 | BC Lớp đào tạo đang diễn ra | UC129 | PDF |
| 7 | 206 | LDTBDDDR_07 | BC Lớp đào tạo đã diễn ra | UC130 | PDF |
| 8 | 211 | CGTVPL_07 | BC Số lượng CG/TVV | UC131 | PDF |
| 9 | 215 | DGHQHTPL_07 | BC Đánh giá hiệu quả HTPL | UC132 | PDF |
| 10 | 219 | CLDTBDPL_07 | BC Chất lượng đào tạo | UC133 | PDF |
| 11 | 223 | VVTDVQL_07 | BC Vụ việc theo đơn vị quản lý | UC134 | PDF |
| 12 | 227 | VVTLV_06 | BC Vụ việc theo lĩnh vực | UC135 | PDF |
| 13 | 231 | VVTLHDN_06 | BC Vụ việc theo loại hình DN | UC136 | PDF |
| 14 | 235 | VVTTGCT_06 | BC Vụ việc theo thời gian chi tiết | UC137 | PDF |
| 15 | 239 | CPHTCT_07 | BC Chi phí chi trả hỗ trợ | UC138 | PDF |
| 16 | 244 | CPCTHTTDVQL_07 | BC Chi phí theo đơn vị | UC139 | PDF |
| 17 | 259 | CPCTHTTLHDN_07 | BC Chi phí theo loại hình DN | UC141 | PDF |
| 18 | 268 | SLCTHT_07 | BC Số lượng chương trình hỗ trợ | UC143 | PDF |
| 19 | 273 | CTTDVQL_05 | BC Chương trình theo đơn vị | UC144 | PDF |
| 20 | 278 | CTTLV_06 | BC Chương trình theo lĩnh vực | UC145 | PDF |
| 21 | 282 | CTTTG_05 | BC Chương trình theo thời gian | UC146 | PDF |

Cột UC lấy từ bảng ánh xạ 23 loại BC trong dropdown, `srs-fr-11-bao-cao.md:1069`–`:1091`.

### Đối chiếu bảng ánh xạ với 2 nguồn tiền lệ — **21/21 khớp, 0 lệch**

Đã tự đối chiếu `RECIPE.md` §6 (bảng 20 dòng, tab tuần 3) + `chuan-14-case-bctk.md` (bảng 14 dòng, tab `bug`)
+ `id-crosswalk.csv`. Ba điều cần biết:

1. **19/21 mã TC có mặt nguyên văn trong `RECIPE.md` §6** với **đúng cùng loại báo cáo** ⇒ khớp tuyệt đối.
2. **2 mã TC KHÔNG có trong `RECIPE.md` §6** — `CLDTBDPL_07` (BC Chất lượng đào tạo) và `VVTLV_06`
   (BC Vụ việc theo lĩnh vực). Đây là **thiếu sót của bảng RECIPE**, không phải lệch của lô này: chính RECIPE
   `:203` tự khai *"23 loại có trên màn: 20 loại trên + `BC Chất lượng đào tạo` · `BC Chi phí theo lĩnh vực` ·
   `BC Vụ việc theo lĩnh vực`"*. Hai mã này đã được xác nhận lại bằng **2 đường độc lập**:
   - `CLDTBDPL_07` ở row 219 nằm **ngay sau** row 218 = `CLDTBDPL_06` = *BC Chất lượng đào tạo*
     (`chuan-14-case-bctk.md:27`) — cùng gốc mã, khác hậu tố định dạng.
   - `VVTLV_06` ở row 227 nằm đúng vị trí **UC135** trong dãy liên tiếp theo thứ tự UC:
     223 → UC134 · 227 → UC135 · 231 → UC136 · 235 → UC137.
3. **1 mã TC có trong `RECIPE.md` §6 nhưng KHÔNG có trong lô này** — `CPCTHTTTG_06`
   (*BC Chi phí theo thời gian*). **Đúng, không phải bỏ sót:** phiếu đó nằm ở **row 264 tab `bug`**, đã đo và
   **đã Pass** trong lô F7 sáng 07/08 (`bao-cao-lo-F7-2026-08-07.md:24`, `:81`) ⇒ không đo lại trong lô này.
   ⚠️ Nhưng kết quả đó đo trên bó mã `index-eWHwDgt2.js` — **không suy ra được** cho bó mã mới.
4. Loại *BC Chi phí theo lĩnh vực* (UC140) **không có phiếu nào** — đã rà toàn bộ `id-crosswalk.csv`, không tồn
   tại mã TC nào cho loại này. Không cần tìm, không log thiếu.

> **Kiểm chéo cuối:** với 12 mã TC có cả cặp `_06`/`_07` trên tab `bug`, số dòng của lô này luôn **liền kề ngay
> sau** số dòng tương ứng trong `chuan-14-case-bctk.md` (174/175 · 200/201 · 205/206 · 210/211 · 214/215 ·
> 218/219 · 238/239 · 243/244 · 258/259 · 267/268 · 272/273 · 277/278 · 281/282). Không dòng nào lệch.

> ⚠️ **Điều KHÔNG tự kiểm chứng được:** agent viết chuẩn **không mở Google Sheet**. Số dòng trong bảng trên lấy
> nguyên từ bản dump prompt cấp. Người đo phải xác nhận Mã TC ở ô thật **trước** khi ghi verdict vào dòng đó.

---

## §1. Bảng "Dòng SRS đã mở đọc lại 07/08"

`{…}` = cắt bớt cho vừa ô, **không đổi chữ**. Cột cuối = kết quả so với `chuan-14-case-bctk.md` §1 (bản đọc sáng 07/08).

### 1.1 `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`

| `file:LINE` | Nguyên văn dòng đọc được 07/08 18:2x | Dùng để chấm vế nào | So bản sáng 07/08 |
|---|---|---|---|
| `:51` | `**Tác nhân chính:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Cán bộ Phê duyệt (TW/BN/ĐP)` | Tiền đề vế A · căn cứ vế B (QTHT không phải tác nhân) | ✅ KHỚP |
| `:62` | `- User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)` | Tiền đề vế A · căn cứ vế B | ✅ KHỚP |
| `:73` | `\| 5 \| format_xuat \| text \| Y \| XLSX / PDF \| XLSX \| Chọn \|` | Chứng minh **Xem và Xuất là MỘT chức năng** (định dạng xuất là trường nhập bắt buộc của chính yêu cầu báo cáo) — nền của vế B | ✅ KHỚP (BA dẫn ở `:393` dưới dạng §Input chung) |
| `:79` | `\| 1 \| **Kiểm tra vai trò trước:** chỉ CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP) được truy cập chức năng báo cáo. Vai trò khác (kể cả QTHT) → chặn ngay ở cửa vào, không mở màn hình. Sau đó kiểm phạm vi theo đơn vị `[BA chốt 2026-08-06]` \| BR-AUTH-01 \|` | **Vế B — B2** (không mở màn hình) | ✅ KHỚP |
| `:86` | `\| 8 \| Nếu xuất PDF: tạo file .pdf theo khung văn bản hành chính Thông tư 17/2025 — khổ A4, font Times New Roman cỡ 13; **đầu trang** có quốc hiệu, tiêu ngữ và tên cơ quan ban hành; **cuối trang** có ngày ký, họ tên cán bộ xuất báo cáo và chỗ trống cho con dấu khi in chính thức. **Không in dòng chức danh người ký** — hồ sơ tài khoản không lưu chức vụ (ngoại lệ của khung chung §D.2.4). Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` theo **Phụ lục E §H8** `[BA chốt 2026-08-04]` — `{TenBaoCao}` là tên loại báo cáo viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số (dấu `/`, khoảng trắng, dấu câu) \| — \|` | **Vế A — A1, A3, A4, A5, A6, A7** · **Bẫy §5.1** (không ký số) · **Bẫy §5.2** (không có dòng chức danh) | ✅ KHỚP |
| `:105` | `- Không thay đổi dữ liệu nghiệp vụ (read-only)` | Nền của vế B (BA bác lập luận "xuất tệp là quyền Tạo") | ✅ KHỚP |
| `:116` | `\| E6 \| Lỗi xuất file \| ERR-RPT-04 \| "Không thể tạo file xuất. Vui lòng thử lại" \| ERROR \|` | **Vế A — A10**: đúng câu đối tác báo 16/07. Không tái hiện = điều kiện Pass | ✅ KHỚP (dòng này bản sáng không dẫn) |
| `:117` | `\| E7 \| Không có quyền \| ERR-RPT-05 \| "Bạn không có quyền xem báo cáo này" \| ERROR \|` | **Vế B — B3** (câu tiếng Việt) · **Bẫy §5.5** | ✅ KHỚP |
| `:120` | `\| E10 \| Không có quyền **thực hiện thao tác xuất tệp** (vai trò ngoài CB NV / CB PD) \| ERR-RPT-08 \| "Bạn không có quyền thực hiện thao tác này" (câu chuẩn `srs-fr-05-vu-viec.md` §3.E — Thông báo người dùng) `[BA chốt 2026-08-06]` \| ERROR \|` | **Vế B — B3** · **Bẫy §5.5** | ✅ KHỚP (dòng mới 06/08, vẫn còn) |
| `:125` | `- **Given** CB nhấn "Xuất PDF" **When** click **Then** tải file .pdf có đủ quốc hiệu + tiêu ngữ + tên cơ quan ở đầu trang, ngày ký + họ tên cán bộ xuất báo cáo + chỗ trống con dấu ở cuối trang, không có dòng chức danh, khổ A4 Times New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` (Phụ lục E §H8)` | **Vế A — AC gốc, phủ A1→A7** | ✅ KHỚP |
| `:127` | `- **Given** người dùng vai trò Quản trị hệ thống **When** đăng nhập **Then** **không thấy** mục menu "Báo cáo thống kê" (ẩn theo M-05, không làm mờ) `[BA chốt 2026-08-06]`` | **Vế B — B1** (căn cứ chính) | ✅ KHỚP |
| `:128` | `- **Given** vai trò ngoài CB Nghiệp vụ / CB Phê duyệt **When** gọi thẳng dịch vụ xuất tệp ở tầng máy chủ (không có đường bấm từ giao diện vì màn đã ẩn) **Then** từ chối với `ERR-RPT-08` — "Bạn không có quyền thực hiện thao tác này" `[BA chốt 2026-08-06]`` | **Vế B — B3, B4** (căn cứ chính) | ✅ KHỚP |
| `:1036` | `**Loại màn hình:** Dashboard (Unified Report Page)` | Căn cứ đo vế B **MỘT LẦN** áp chung 21 dòng | ✅ KHỚP |
| `:1037` | `**FR sử dụng:** FR-IX-01 ~ FR-IX-23` | Như trên | ✅ KHỚP (bản sáng không dẫn) |
| `:1042` | `Một trang báo cáo thống nhất cho tất cả 23 loại BC. Dropdown chọn loại BC phía trên, bộ lọc chung + bộ lọc đặc thù ở giữa, vùng kết quả (biểu đồ + bảng dữ liệu) phía dưới.` | Như trên | ✅ KHỚP |
| `:1046` | `> **Điều kiện vào màn — áp cho TOÀN BỘ bảng dưới đây** `[BA chốt 2026-08-06]`: người dùng phải có vai trò **Cán bộ Nghiệp vụ** hoặc **Cán bộ Phê duyệt** (TW/BN/ĐP). Vai trò khác — kể cả **Quản trị hệ thống** — **không vào được màn này**; mục menu "Báo cáo thống kê" bị **ẩn** theo quy ước M-05 (ẩn, không làm mờ). {…}` | **Vế B — B1, B2** · **Bẫy §5.9** | ✅ KHỚP |
| `:1052` | `\| 3 \| filter-bar \| Dropdown loại BC \| select (searchable, grouped) \| 23 loại BC phân nhóm theo optgroup. Mỗi option: "[Mã UC] Tên BC" \| change → load bộ lọc đặc thù \| Luôn hiển thị \|` | **Vế B — B2** (dấu hiệu quan sát: có ô chọn loại BC = đã vào được màn) · **Bẫy §5.9** | ✅ KHỚP (vẫn ghi "Luôn hiển thị") |
| `:1056` | `\| 7 \| action-bar \| Nút Xem báo cáo \| button (primary) \| "Xem báo cáo" → chạy query \| click → load data \| **Chỉ với vai trò CB Nghiệp vụ / CB Phê duyệt** — vai trò khác không vào được màn này (M-05 ẩn mục menu) `[BA chốt 2026-08-06]` \|` | **Vế B — B2** | ✅ KHỚP |
| `:1058` | `\| 9 \| action-bar \| Nút Xuất PDF \| button \| "Xuất PDF (.pdf)" → xuất theo khung trình bày TT17/2025 (không dùng Mẫu 21a/21b) \| click → auto-download \| Sau khi đã "Xem báo cáo" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]` \|` | **Vế A — A11** (tệp về máy) · **Vế B — B4** · **Bẫy §5.4** | ✅ KHỚP |
| `:1069`–`:1091` | Bảng ánh xạ 23 loại BC trong dropdown, mỗi dòng `Optgroup \| UC \| Tên hiển thị \| Bộ lọc đặc thù \| Biểu đồ` — vd `:1069` = `\| **Hỏi đáp pháp luật** \| UC124 \| BC Số lượng hỏi đáp/vướng mắc pháp luật \| Lĩnh vực PL, Trạng thái HD \| Donut + Trend \|` | Cột UC ở §0 · **Bẫy §5.10** (nhãn CT rút gọn) | ✅ KHỚP (bản sáng không dẫn) |
| `:1097` | `- Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file. Riêng PDF bổ sung khung văn bản hành chính: quốc hiệu + tên cơ quan ở đầu trang, ngày ký + họ tên cán bộ xuất báo cáo + chỗ con dấu ở cuối trang (không có dòng chức danh). Tên tệp cả hai định dạng theo **Phụ lục E §H8** — `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`` | **Vế A — A8** (đủ 4 mục đầu tệp) + A3→A5 | ✅ KHỚP |
| `:1273` | `\| BR-AUTH-08 \| chính sách phân quyền áp dụng cho MỌI bảng có cột `don_vi_id`. TW thấy toàn quốc, BN thấy BN, ĐP thấy ĐP \| Architecture AD-07 \| Toàn bộ FR-IX \| — (QTHT **không phải tác nhân của nhóm IX** nên không có ca bypass ở đây; ngoại lệ QTHT của BR-AUTH-08 chỉ áp cho các nhóm mà QTHT là tác nhân) `[BA chốt 2026-08-06]` \| Verify phân quyền \|` | **Vế B — B4**. Chữ "QTHT bypass" **đã bị gỡ** ⇒ căn cứ cũ của phiếu QA không còn | ✅ KHỚP · `:1268` vẫn là dòng trống |
| `:1285` | `\| BR-DATA-06 \| Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file \| Pattern IP-01 \| Toàn bộ FR-IX \| Báo cáo nhóm IX có xuất PDF \| Test export limit \|` | **Vế A — A9** (số trong tệp = số của **bộ lọc hiện tại**, tức số trên màn lần đo đó) | ✅ KHỚP (bản sáng không dẫn) |

### 1.2 `srs-v3.5.md`

| `file:LINE` | Nguyên văn dòng đọc được 07/08 | Dùng để chấm vế nào | So bản sáng 07/08 |
|---|---|---|---|
| `:116` | `\| 11 \| `srs-fr-11-bao-cao.md` \| IX — Báo cáo thống kê \| UC 124-146 \| 6 sub-menu: Báo cáo hỏi đáp pháp luật, Báo cáo vụ việc hỗ trợ pháp lý, Báo cáo đào tạo, tập huấn, Báo cáo chuyên gia, tư vấn viên và đánh giá, Báo cáo chi phí hỗ trợ, Báo cáo chương trình hỗ trợ pháp lý doanh nghiệp. Cùng mẫu chung, lọc sẵn theo nhóm \| `[CR-09]` \|` | **Vế B — B1**: phải duyệt **cả 6 sub-menu**, không dừng ở mục cha | ✅ KHỚP |
| `:684` | `\| M-05 \| **Hiển thị theo quyền** — menu item chỉ hiện nếu vai trò có quyền truy cập ≥ 1 chức năng trong đó. Ẩn (không disable) nếu không có quyền \| NF-Security \|` | **Vế B — B1**: **ẩn**, không phải làm mờ / disable | ✅ KHỚP |
| `:1294` | `**Ký hiệu:** C=Create, R=Read (toàn bộ phạm vi), R*=Read scoped (chỉ đơn vị mình), U=Update, D=Delete (soft), —=No access` | Đọc kèm `:1296` | ✅ KHỚP (bản sáng không dẫn) |
| `:1296` | `> **Bảng này là quyền ở MỨC DỮ LIỆU, không phải quyền chạy chức năng** `[làm rõ 2026-08-06]`. Một ô có `R` chỉ nói vai trò đó **được đọc dữ liệu** của thực thể; nó **không** đồng nghĩa vai trò đó là **tác nhân** của các chức năng thao tác trên thực thể ấy. Tác nhân của từng chức năng do dòng **Tác nhân** và **Điều kiện tiên quyết** của chính FR quyết định; menu hiển thị theo quyền chức năng (M-05).` | **Bẫy §5.8**: cấm dùng ô `R` để lập luận QTHT được xem/xuất | ✅ KHỚP |
| `:1298` | `> Ví dụ đã gây tranh chấp ở UAT tuần 5: `BAO_CAO` cột QTHT = `R`, nhưng cả 23 mục FR-IX lẫn 23 giao dịch UC124–146 đều ghi tác nhân là **CB Nghiệp vụ / CB Phê duyệt** — QTHT **không** vào màn báo cáo thống kê và **không** xuất tệp báo cáo. Ô `R` ở đây phục vụ vận hành, tra cứu dữ liệu ở tầng quản trị.` | **Bẫy §5.8** | ✅ KHỚP |
| `:1300` | `\| Entity \| QTHT \| CB_NV_TW \| CB_NV_BN \| CB_NV_DP \| CB_PD_TW \| CB_PD_BN \| CB_PD_DP \| DN \| NHT \| TVV \| CG \|` | Header cột của bảng quyền | ✅ KHỚP |
| `:1339` | `\| BAO_CAO \| R \| CRU* \| CRU* \| CRU* \| RU* \| RU* \| RU* \| — \| — \| — \| — \|` | **Bẫy §5.8** — ô QTHT vẫn `R`, BA **cố ý không sửa** | ✅ KHỚP |
| `:6719` | `- Khổ giấy: A4 (210 × 297mm)` | **Vế A — A6** | ✅ KHỚP (bản sáng dẫn gộp) |
| `:6720` | `- Phông chữ: Times New Roman, cỡ 13pt` | **Vế A — A7** · **Bẫy §5.3** | ✅ KHỚP |
| `:6721` | `- Header: Quốc hiệu + Tên cơ quan ban hành` | **Vế A — A3, A4** | ✅ KHỚP |
| `:6722` | `- Footer: Ngày ký + Họ tên cán bộ xuất + chỗ trống cho chữ ký, chức vụ và con dấu (nếu in chính thức)` | **Vế A — A5** | ✅ KHỚP |
| `:6723` | `- **Ngoại lệ chung cho mọi tệp xuất** `[BA chốt 2026-08-04, mở rộng phạm vi 2026-08-06]`: khối ký gồm **ngày ký + họ tên cán bộ xuất báo cáo + chỗ trống cho chữ ký, chức vụ và con dấu khi in chính thức**, **không in sẵn dòng chức danh**. Hai căn cứ: hồ sơ tài khoản (`TAI_KHOAN`) không lưu chức vụ nên không có nguồn dữ liệu; và biểu mẫu gốc 21a/21b để trống chỗ này cho người ký tự ghi khi ký tay. {…}` | **Vế A — A5** · **Bẫy §5.2** (căn cứ mạnh nhất cho "không có dòng chức danh") | ✅ KHỚP |
| `:6760` | `\| **H8** \| Tên tệp xuất thống nhất \| {…} **Khuôn:** `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số {…}. **Phần giờ-phút bắt buộc để xuất hai lần trong cùng ngày không đè tệp.** Tổng độ dài tối đa **255 ký tự** {…}. Trùng tên (hai lần xuất trong cùng phút) thì tự thêm hậu tố `_1`, `_2` {…} `[BA chốt 2026-08-06 — nâng phạm vi quyết định 2026-08-04 của Nhóm IX thành quy ước chung]` \| BẮT BUỘC \|` | **Vế A — A1, A2** · **Bẫy §5.7** | ✅ KHỚP |

### 1.3 `srs-fr-05-vu-viec.md`

| `file:LINE` | Nguyên văn dòng đọc được 07/08 | Dùng để chấm vế nào | So bản sáng 07/08 |
|---|---|---|---|
| `:1588` | `\| Tình huống \| Loại \| Nội dung tiếng Việt \|` (header bảng §3.E — Thông báo người dùng, mở ở `:1586`) | Ngữ cảnh của `:1594` | ✅ KHỚP |
| `:1594` | `\| Không có quyền truy cập \| Toast error \| "Bạn không có quyền thực hiện thao tác này" \|` | **Vế B — B3** (câu tiếng Việt chuẩn) | ✅ KHỚP |

### 1.4 Hai điều SRS **im lặng** (grep toàn thư mục 07/08, không phải suy đoán)

| Điều | Kết quả grep | Hệ quả chấm |
|---|---|---|
| **Ký số / chữ ký số cho nhóm IX** | Chuỗi `ký số` **không xuất hiện ở bất kỳ dòng nào** của `srs-fr-11-bao-cao.md` và `srs-v3.5.md`. Trong cả thư mục `srs-v3.5/` chỉ có ở `srs-fr-03-dao-tao.md`, `srs-fr-05-vu-viec.md`, `CHANGELOG-v3-to-v3.5.md` — không tệp nào thuộc nhóm báo cáo | **SRS im lặng** ⇒ kỳ vọng "hỗ trợ ký số" của đối tác **không có căn cứ trong nguồn đặc tả prompt cấp**. Xem bẫy §5.1 |
| **Chuỗi `Forbidden` và mã `ERR-PERM-SYS-00-01`** | `grep -rn "ERR-RPT-08\|ERR-PERM-SYS-00-01\|Forbidden"` toàn thư mục `srs-v3.5/*.md` chỉ trả về 2 dòng, cả hai là `ERR-RPT-08` ở `srs-fr-11-bao-cao.md:120` và `:128`. **Không dòng nào chứa `Forbidden` hay `ERR-PERM-SYS-00-01`** | Cả hai mã lỗi hợp lệ của ca thiếu quyền đều là **câu tiếng Việt** ⇒ vế "phải bằng tiếng Việt" (B3) đứng vững, không phụ thuộc việc BA đổi mã |

---

## §2. Quyết định BA 06/08 mục 5 — trích nguyên văn

**Nguồn:** `../../reverify-week-5/ba-confirm/phan-hoi-ba-7-diem-can-chot-2026-08-06.md`, mục 5
*"Quản trị viên vào được màn báo cáo, bấm xuất tệp thì bị máy chủ từ chối"* (`:373`–`:441`).

**Kết luận (nguyên văn `:415`):**

> **→ Kết luận: vai trò Quản trị hệ thống KHÔNG phải tác nhân của chức năng báo cáo thống kê — không xuất tệp,
> và cũng không vào màn báo cáo. Máy chủ chặn xuất là ĐÚNG, không nới quyền. Giao diện sai ở chỗ vẫn mở màn và
> vẫn mời bấm nút xuất. Dev action: Có (giao diện) · Sửa đặc tả: Có (ghi rõ điều kiện vai trò + bổ sung mã lỗi
> cho thao tác xuất) · Sheet: giữ xử lý cho cả 5 phiếu (189 · 222 · 226 · 230 · 234).** ✅ Tự chốt theo cây
> trọng tài — tầng "CSV UC/Transaction".

**Ba câu chống chế đã bị BA bác trước, trích nguyên văn để người đo không dùng lại:**

> `:393` — *"**Về lập luận "xuất là một dạng đọc":** không đứng được {…} Chỗ quyết định nằm khác: **Xem và Xuất
> là MỘT chức năng, không phải hai.** Định dạng xuất là **trường nhập bắt buộc** của chính yêu cầu báo cáo
> {…}. Đã không phải tác nhân của chức năng thì không có phần nào của chức năng."*

> `:395` — *"Ô `R` của quản trị hệ thống ở `srs-v3.5.md:1335` là **quyền mức dữ liệu phục vụ quản trị**, không
> phải quyền thực hiện chức năng nghiệp vụ."*

> `:403` — *"Cho quản trị viên xuất tệp là để tên một người không phải cán bộ nghiệp vụ đứng dưới một văn bản
> có quốc hiệu và chỗ đóng dấu. Đó là lý do đủ để chốt, độc lập với mọi tranh luận về chữ `R` hay `C`."*

> `:411` — *"**(2) Đối tác yêu cầu khác bản gốc không?** Khác ở chỗ họ thao tác bằng vai trò không có quyền —
> cả 10/10 ảnh hai vòng đều hiện "Quản trị viên · QTHT". Kỳ vọng *"xuất và tải tệp về máy"* của họ đúng, chỉ
> là đo bằng vai trò sai."*

### 2.1 Nhánh PASS đúng là nhánh nào

| Nhánh | Nội dung | Có phải nhánh Pass không |
|---|---|---|
| **(a)** | Vai trò **Quản trị hệ thống** bấm [Xuất PDF] và **nhận được tệp** | ❌ **KHÔNG.** Đây là kỳ vọng gốc của 21 phiếu — BA đã bác 06/08, SRS đã thi hành. Nếu quan sát thấy điều này thì **FAIL** (dev nới quyền ngược), xem §4 B4 |
| **(b)** | Hệ thống **chặn ngay ở cửa vào** với vai trò QTHT (ẩn hẳn mục menu, không mở màn), **và** vai trò **Cán bộ Nghiệp vụ** xuất được tệp PDF đúng khung văn bản hành chính | ✅ **ĐÂY LÀ NHÁNH PASS.** Vế B (§4) + vế A (§3) đều phải đạt |

### 2.2 🔴 Kỳ vọng gốc của 21 phiếu ở vế QTHT đã KHÔNG còn là nhánh Pass

Phải nói thẳng điều này với người đo, vì nó ngược trực giác:

- Ô `Kết quả mong đợi` của 21 phiếu đòi **PDF xuất ra được** trong bối cảnh đối tác đang đăng nhập bằng vai trò
  **Quản trị hệ thống** (chính ô `TKM phản hồi lần 1` ghi triệu chứng `Forbidden` — dấu hiệu của vai trò này).
- Sau quyết định BA 06/08 + SRS đã thi hành (`:79`, `:127`, `:128`, `:1046`, `:1273`), **vai trò đó không còn
  đường bấm nào để xuất tệp**. Tiền đề *"đăng nhập QTHT → vào `/bao-cao` → bấm Xuất PDF"* **tự tiêu**.
- ⇒ **Việc QTHT không xuất được tệp CHÍNH LÀ PASS**, không phải blocker, không ghi "Chưa chốt", không hỏi lại BA.
- ⇒ **CẤM** chấm Pass theo kỳ vọng gốc (tức cấm coi "QTHT xuất được tệp" là đạt).
- Verdict Pass **bắt buộc kèm câu**: *kỳ vọng gốc của đối tác (Quản trị hệ thống xuất được tệp) KHÁC đặc tả hiện
  hành; nghiệp vụ đã chốt 06/08 giữ nguyên đặc tả, không nới quyền* — kèm nội dung `[Lý do]` + `[Nhận định]`
  BA đã soạn sẵn (`phan-hoi-ba-7-diem-can-chot-2026-08-06.md:437`–`:439`).

> **Không hỏi lại BA vế này.** Mục 5 đã đóng, quan hệ là **DIFF — SRS thắng**.

---

## §3. Vế A — xuất PDF bằng vai trò Cán bộ Nghiệp vụ

**Tài khoản:** `cbnv_tw_05` / `Test@1234` (CB Nghiệp vụ - Trung ương, `CB_NV_TW` — `../../input/input.md:55`).
**Đo theo TỪNG loại báo cáo** — 21 loại, mỗi loại một tệp PDF, vì mỗi phiếu là một loại riêng trong ô chọn.

**Tiền đề bắt buộc (thiếu là chưa đo được, KHÔNG được Pass):** vai trò này **vào được** màn `/bao-cao`
(`:51`, `:62`) → chọn đúng loại BC của phiếu → chọn kỳ + đơn vị → bấm **[Xem báo cáo] đúng MỘT lần** →
**ghi lại các số hiện trên màn** → bấm **[Xuất PDF]** → hộp thoại *Tùy chọn in báo cáo PDF* **để nguyên mặc
định (A4 · Dọc)** → bấm **[Xuất file]** → **MỞ TỆP RA ĐỌC**.

### Bảng tiêu chí PASS/FAIL

| Mã | Tiêu chí | ✅ PASS khi | ❌ FAIL khi | Căn cứ `file:LINE` |
|---|---|---|---|---|
| **A1** | Tên tệp đúng khuôn, **có cả ngày và giờ-phút** | Tên tệp dạng `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`; `{TenBaoCao}` viết liền PascalCase, bỏ dấu tiếng Việt, bỏ mọi ký tự không phải chữ/số | Thiếu phần `_HHmm`; hoặc còn dấu tiếng Việt / khoảng trắng / dấu `/` / dấu câu trong tên; hoặc không có phần ngày | `srs-fr-11-bao-cao.md:86` · `:125` · `:1097` · `srs-v3.5.md:6760` |
| **A2** | **Hai lần xuất khác phút ra hai tên khác nhau** | Xuất lần 2 sau khi đã sang phút mới → tên tệp khác lần 1, tệp cũ không bị đè | Hai lượt xuất khác phút cho ra **cùng một tên tệp** | `srs-v3.5.md:6760` (*"Phần giờ-phút bắt buộc để xuất hai lần trong cùng ngày không đè tệp"*) |
| **A3** | Đầu trang có **quốc hiệu + tiêu ngữ** | Đọc được trong tệp: `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` và `Độc lập - Tự do - Hạnh phúc` | Thiếu một trong hai dòng | `srs-fr-11-bao-cao.md:86` · `:125` · `:1097` · `srs-v3.5.md:6721` |
| **A4** | Đầu trang có **tên cơ quan ban hành** | Đọc được tên cơ quan của đơn vị người xuất (vd `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP`) | Không có tên cơ quan nào ở đầu trang | `srs-fr-11-bao-cao.md:86` · `:125` · `srs-v3.5.md:6721` |
| **A5** | **Khối cuối trang đủ 4 phần**: ngày ký · nhãn người xuất báo cáo · chỗ trống cho con dấu · họ tên cán bộ | Đọc được: dòng ngày ký dạng `Ngày ... tháng ... năm ...`; nhãn `NGƯỜI XUẤT BÁO CÁO`; chỗ trống cho con dấu (thể hiện bằng dòng `(Ký, ghi rõ họ tên và đóng dấu)`); và **họ tên của chính tài khoản đang đăng nhập** | Thiếu bất kỳ phần nào trong 4 phần; hoặc họ tên in ra **không phải** của tài khoản đang đăng nhập | `srs-fr-11-bao-cao.md:86` · `:125` · `:1097` · `srs-v3.5.md:6722` · `:6723` |
| **A6** | **Khổ A4** | Kích thước trang ≈ **595,28 × 841,89 pt** (= 210 × 297 mm) khi để nguyên tuỳ chọn mặc định | Khổ giấy khác A4 **khi để nguyên mặc định** (đổi tay sang A3/Letter rồi kêu sai = lỗi của người đo, không phải bug) | `srs-fr-11-bao-cao.md:86` · `srs-v3.5.md:6719` |
| **A7** | **Phông chữ** | Phông nhúng là Times New Roman **hoặc bản tương thích số đo của nó** (`Tinos-Regular` / `Tinos-Bold` / `Tinos-Italic`) | Phông không tương thích số đo Times New Roman (vd Arial, Roboto, DejaVu) | `srs-fr-11-bao-cao.md:86` · `srs-v3.5.md:6720` · bẫy §5.3 |
| **A8** | **Đủ 4 mục đầu tệp** | Đọc được đủ: **tên báo cáo** · **`Kỳ báo cáo:`** kèm khoảng thời gian · **`Đơn vị:`** · **`Ngày tạo:`** | Thiếu bất kỳ mục nào trong 4 mục | `srs-fr-11-bao-cao.md:1097` · Output chung `:94`–`:99` |
| **A9** | **Số trong tệp khớp số trên màn của CHÍNH lần đo đó** | Các chỉ số tổng và các hàng của bảng trong tệp trùng khít với số đã ghi lại trên màn ở đúng lượt [Xem báo cáo] sinh ra tệp này | Bất kỳ số nào trong tệp lệch số trên màn của cùng lượt đo | `srs-fr-11-bao-cao.md:1285` (BR-DATA-06 — *"File xuất theo bộ lọc hiện tại"*) · `:1097` |
| **A10** | **Không tái hiện lỗi gốc đối tác báo** | Không xuất hiện câu *"Không thể tạo file xuất. Vui lòng thử lại."* ở bất kỳ lượt xuất nào | Câu đó xuất hiện lại | `srs-fr-11-bao-cao.md:116` (E6 / `ERR-RPT-04`) |
| **A11** | **Tệp thật sự về được máy và mở được** | Có tệp `.pdf` thu được từ thao tác trên giao diện, mở ra đọc được nội dung | Không có tệp / tệp hỏng, không mở được / phải dùng đường vòng ngoài giao diện mới lấy được tệp | `srs-fr-11-bao-cao.md:125` · `:1058` |

**Luật dừng sớm vế A:** A-bất-kỳ FAIL ở một loại báo cáo → **Reopen**, dừng các loại còn lại, **ghi rõ loại nào
đã đo đạt, loại nào chưa đo**. Không suy kết quả từ loại này sang loại khác.

**Cấm Pass bằng quan sát tĩnh.** Nhìn thấy nút [Xuất PDF] sáng ≠ đạt. Tải được tệp ≠ đạt — **phải mở tệp ra đọc**
(tiền lệ: mã trả về thành công + tệp nhị phân chỉ chứng minh tệp được **TẠO**, không chứng minh **ĐÚNG**).

---

## §4. Vế B — vai trò Quản trị hệ thống

**Tài khoản:** `admin` / `Secret@123` (QTHT, cấp TW — `../../input/input.md:8`–`:12`).

**Đo MỘT LẦN, kết quả áp chung cho cả 21 dòng.** Căn cứ: 23 loại báo cáo dùng **chung một màn** —
`srs-fr-11-bao-cao.md:1036` (*"Loại màn hình: Dashboard (Unified Report Page)"*) · `:1037`
(*"FR sử dụng: FR-IX-01 ~ FR-IX-23"*) · `:1042` (*"Một trang báo cáo thống nhất cho tất cả 23 loại BC"*).
Không cần lặp 21 lần.

**Cách đo:** đăng nhập `admin` → **tải lại trang** (bắt buộc, xem bẫy §5.11) → duyệt **toàn bộ** cây điều hướng,
**mở cả 6 sub-menu** của nhóm báo cáo mà `srs-v3.5.md:116` liệt kê → **đối chứng độc lập**: gõ thẳng địa chỉ
`/bao-cao`.

### Bảng tiêu chí PASS/FAIL

| Mã | Tiêu chí | ✅ PASS khi | ❌ FAIL khi | Căn cứ `file:LINE` |
|---|---|---|---|---|
| **B1** | **Mục menu bị ẩn hẳn — không phải làm mờ** | Cây điều hướng của tài khoản QTHT **không có** mục "Báo cáo thống kê" ở bất kỳ vị trí nào, kể cả trong 6 sub-menu. Đối chứng: tài khoản CB Nghiệp vụ **vẫn thấy** mục đó ⇒ ẩn theo vai trò, không phải gỡ chức năng | Mục menu **vẫn còn** — **kể cả khi bị làm mờ / vô hiệu hoá / không bấm được** (đặc tả đòi **ẩn**, không đòi disable) | `srs-fr-11-bao-cao.md:127` · `:1046` · `srs-v3.5.md:684` (M-05) · `:116` |
| **B2** | **Vào thẳng `/bao-cao` không mở được màn** | Gõ thẳng địa chỉ **không** mở được màn báo cáo: không hiện ô chọn loại BC, không hiện số liệu, không hiện nút xuất nào | (a) Vào được màn và bấm [Xem báo cáo] vẫn trả đủ số liệu · (b) **Fix nửa vời**: chỉ ẩn/mờ nút [Xuất PDF] nhưng vẫn cho vào màn, vẫn chọn được loại BC và vẫn xem được số liệu — đúng chữ BA gọi là *"vẫn mời rồi chặn, chỉ lùi một bước"* (`:424`) | `srs-fr-11-bao-cao.md:79` (*"chặn ngay ở cửa vào, không mở màn hình"*) · `:1046` · `:1052` · `:1056` |
| **B3** | **Câu từ chối là tiếng Việt, không phải chuỗi kỹ thuật** | Chữ mà người dùng nhận được là **câu tiếng Việt** cho biết không có quyền; mã đi kèm nằm trong **bộ mã của nhóm báo cáo** (`ERR-RPT-08` đúng nhất; `ERR-RPT-05` **vẫn chấp nhận** — xem bẫy §5.5) | Vẫn là `Forbidden`, `ERR-PERM-SYS-00-01`, hoặc **bất kỳ** chuỗi tiếng Anh / mã kỹ thuật nào đẩy nguyên ra người dùng | `srs-fr-11-bao-cao.md:117` · `:120` · `:128` · `srs-fr-05-vu-viec.md:1594` · §1.4 (SRS không có chuỗi `Forbidden`) |
| **B4** | **Máy chủ không sinh tệp cho QTHT** | Hệ thống **từ chối** thao tác xuất tệp của vai trò QTHT — **không tệp nào được sinh ra** cho vai trò này. Vì B1/B2 đã ẩn màn nên đo đúng ca `:128`: dùng chính phiên đăng nhập QTHT yêu cầu thẳng dịch vụ xuất tệp ở tầng máy chủ, đọc kết quả trả về | Vai trò QTHT **nhận được tệp** — tức nới quyền ngược, trái `:51`/`:62`/`:79` và trái quyết định BA. **FAIL này dừng lô ngay** | `srs-fr-11-bao-cao.md:128` · `:51` · `:62` · `:1273` · `srs-v3.5.md:1296`–`:1298` |

**Ghi chú đo B3 khi B1/B2 đã đạt:** màn đã ẩn thì không còn nút để bấm ⇒ đọc **chữ trong phần trả về** của lời
gọi ở tầng máy chủ (đúng ca AC `:128`). Nếu B2 FAIL (vẫn vào được màn) thì đọc **nguyên văn chữ trên khung thông
báo** tại đúng thời điểm lỗi.

### Luật dừng sớm vế B

| Tình huống | Xử lý |
|---|---|
| **B1 hoặc B2 FAIL** (menu vẫn hiện/mờ · vẫn vào được `/bao-cao` · vẫn xem đủ số liệu · chỉ ẩn nút Xuất) | **Reopen cả lô 21 phiếu, dừng ngay.** Không cần chạy hết 21 loại ở vế A. Vẫn ghi mọi vế kết luận được **từ chính bằng chứng đã có** |
| **B4 FAIL** (QTHT nhận được tệp) | **Reopen, dừng ngay** — nới quyền ngược |
| **B3 FAIL** (còn `Forbidden` / mã kỹ thuật) | Ghi FAIL vế B3 và **tiếp tục** đo vế A. B3 **một mình nó KHÔNG lật verdict 21 phiếu** — câu chữ khi từ chối thuộc phiếu QA riêng `BUG-BCTK-QA01` (dòng 363 tab `bug`), độc lập. Báo lại để người ra đề quyết |

**Muốn Pass cả lô thì phải chạy hết:** B1 + B2 + B4 (1 lượt QTHT) **và** A1→A11 cho **đủ 21 loại**, mỗi loại
mở tệp ra đọc.

---

## §5. Bẫy — KHÔNG được chấm FAIL

Đều là **tiền lệ đã chốt hoặc căn cứ SRS đọc được**, không phải suy đoán.

1. **Tệp không có chữ ký số** (`sigflags = -1`, tệp không có trường ký điện tử). `srs-fr-11-bao-cao.md:86` và
   `srs-v3.5.md:6722`–`:6723` chỉ đòi **chỗ trống cho chữ ký, chức vụ và con dấu khi in chính thức** — không đòi
   ký số. Chuỗi `ký số` **không xuất hiện ở bất kỳ dòng nào** của `srs-fr-11-bao-cao.md` lẫn `srs-v3.5.md`
   (grep 07/08, §1.4). Kỳ vọng *"hỗ trợ ký số"* trong ô `Kết quả mong đợi` **không có căn cứ ở nguồn đặc tả
   prompt cấp**. Tiền lệ: `cond/SLHDVM_07.md:39`, `RECIPE.md:173`.
2. **Không có dòng chức danh người ký.** `srs-fr-11-bao-cao.md:86` ghi thẳng *"**Không in dòng chức danh người
   ký** — hồ sơ tài khoản không lưu chức vụ (ngoại lệ của khung chung §D.2.4)"* `[BA chốt 2026-08-04]`;
   `srs-v3.5.md:6723` nhắc lại *"**không in sẵn dòng chức danh**"* `[mở rộng phạm vi 2026-08-06]`. Ô `Kết quả
   mong đợi` của 21 phiếu đòi có chức danh — **kỳ vọng đó đã hết hiệu lực**. Tiền lệ: `RECIPE.md:174`,
   `cond/SLHDVM_07.md:38`, `chuan-14-case-bctk.md:122`.
3. **Phông đọc ra là `Tinos-*`** (`Tinos-Regular` / `Tinos-Bold` / `Tinos-Italic`) thay vì đúng chữ
   "Times New Roman" — bản tương thích số đo của Times New Roman ⇒ **đạt** tiêu chí `:86` / `srs-v3.5.md:6720`.
   Tiền lệ: `RECIPE.md:171`, `cond/SLHDVM_07.md:33`, `chuan-14-case-bctk.md:123`.
4. **Nút [Xuất PDF] chỉ MỞ HỘP THOẠI, không xuất luôn.** Lượt xuất thật là nút **[Xuất file]** trong hộp thoại
   *Tùy chọn in báo cáo PDF*. Dừng ở nút [Xuất PDF] sẽ không thấy lời gọi nào và dễ kết luận nhầm *"bấm Xuất PDF
   không có phản hồi"* / *"hệ thống im lặng"*. Tiền lệ: `RECIPE.md:121`, `cond/SLHDVM_07.md:47`,
   `chuan-14-case-bctk.md:130`.
   *(Ghi chú: `srs-fr-11-bao-cao.md:1058` ghi hành vi là `click → auto-download`, tức SRS không mô tả hộp thoại
   này. Đã có tiền lệ ghi nhận **"không phải lỗi"** ở `cond/SLHDVM_07.md:47`. **KHÔNG chấm FAIL trong lô này**;
   muốn theo đuổi thì phải tách phiếu riêng, không lật verdict 21 phiếu.)*
5. **Dev hiện đúng câu `:117` ("Bạn không có quyền xem báo cáo này") thay vì mã `ERR-RPT-08` `:120`.** Nghiệp vụ
   vừa đổi mã ngày 06/08, còn phiếu QA cũ `BUG-BCTK-QA01` (dòng 363 tab `bug`) **đang bắt dev hiện đúng câu
   `:117`** — dev làm theo phiếu cũ là hợp lý. BA nêu đích danh ở `:426`: *"**Cần báo lại QA chỉnh phiếu
   `BUG-BCTK-QA01`** — phiếu đó đang yêu cầu Dev hiện đúng câu `:117`"*. Chỉ **ghi nhận** dev đang dùng mã nào,
   **KHÔNG chấm FAIL**. Tiền lệ: `chuan-14-case-bctk.md:126`, `bao-cao-lo-F7-2026-08-07.md:65`.
6. **Các bug đã tách phiếu riêng — KHÔNG chấm lại trong lô này.** Nội dung lấy nguyên từ
   `bao-cao-lo-F7-2026-08-07.md` §2.2 (`:97`–`:100`) và §4 (`:147`–`:148`):

   | Mã phiếu | Dòng tab `bug` | Nội dung đã tách |
   |---|---:|---|
   | `BCTK_QA05` | 368 | Hồ sơ 15.000.000 ₫ xếp nhầm quy mô *(lượt đo 07/08 sáng: hồ sơ đã về đúng quy mô Nhỏ)* |
   | `BCTK_QA07` | 370 | Nút Xuất bị **khoá sau lần [Xem báo cáo] thứ 2** |
   | `BCTK_QA09` | 372 | Tệp in **mã kỹ thuật `KHOANG`** ở dòng Kỳ báo cáo khi chọn kỳ *"Khoảng tuỳ chọn"* |
   | `BCTK_QA13` | 377 | **BC Số lượng chương trình hỗ trợ** — bảng "Thống kê theo kỳ" trên màn để **trống** cả ô Số lượng lẫn Tỷ lệ, trong khi tệp xuất in đúng số |
   | `BCTK_QA14` | 378 | **BC Chương trình theo thời gian** — vẫn còn chỉ tiêu **số doanh nghiệp** ở cả thẻ tổng, chú giải biểu đồ, cột bảng và trong tệp xuất, dù nghiệp vụ đã chốt bỏ chỉ tiêu này 24/07 (`srs-fr-11-bao-cao.md:1021`; báo cáo anh em *CT theo lĩnh vực* `:964` đã bỏ đúng) |

   ⚠️ **`BCTK_QA13` và `BCTK_QA14` không nằm trong danh sách prompt nêu, nhưng phải đưa vào** — chúng chạm đúng
   **2 trong 21 loại** của lô này (`SLCTHT_07` row 268 và `CTTTG_05` row 282). Gặp lại hai triệu chứng đó thì
   **KHÔNG** dùng để lật verdict PDF, chỉ ghi nhận đã có phiếu.
7. **Hai lượt xuất rơi vào CÙNG một phút mà tên tệp trùng hệt.** `srs-v3.5.md:6760` quy định trùng tên thì tự
   thêm hậu tố `_1`, `_2`. Nhưng đây **không phải ý con của bug gốc** (ô `Kết quả mong đợi` chỉ đòi khuôn
   `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`). Nếu gặp → **ghi candidate một dòng**, KHÔNG lật verdict lô này. Tiêu chí
   A2 chỉ đòi **khác phút → khác tên**.
8. **Không dùng ô `R` của QTHT ở `srs-v3.5.md:1339` để lập luận QTHT được xem/xuất.** Khối chú thích `:1296`–
   `:1298` đã bác thẳng lập luận đó `[làm rõ 2026-08-06]`; BA cố ý **không sửa** dòng `:1339`. Cũng không dùng
   `BR-AUTH-08 "QTHT bypass"` — câu đó **đã bị gỡ**, `:1273` nay ghi ngược lại, `:1268` là dòng trống.
9. **`srs-fr-11-bao-cao.md:1052` (ô chọn loại BC) vẫn ghi "Luôn hiển thị" — KHÔNG phải khoảng trống đặc tả.**
   Khối `:1046` đã tuyên bố cột "Điều kiện hiển thị" của **từng dòng** chỉ mô tả điều kiện **bổ sung bên trong
   màn**, luôn hiểu là đã thoả điều kiện vai trò. **Đừng log bug đặc tả ở dòng này.**
10. **Nhãn loại báo cáo trên màn khác chữ trong bảng ánh xạ SRS.** `srs-fr-11-bao-cao.md:1088`–`:1091` viết tắt
    *"BC Số lượng CT hỗ trợ"* / *"BC CT theo đơn vị"* / *"BC CT theo lĩnh vực"* / *"BC CT theo thời gian"*, trong
    khi nhãn quan sát trên màn là *"BC Số lượng chương trình hỗ trợ"* / *"BC Chương trình theo…"*. Chỉ là cách
    viết tắt của cùng một loại — **KHÔNG chấm FAIL**, và **KHÔNG** vì thế mà chọn nhầm loại. Không tìm thấy đúng
    loại của phiếu → **DỪNG, báo lại**, tuyệt đối không chọn loại gần giống.
11. **Bẫy bản dựng.** Tab trình duyệt mở lâu vẫn chạy mã cũ. **Tải lại trang + ghi tên bó mã một lần đầu lô, đo
    lại vân tay ở cuối lô.** Tiền lệ: đã báo Reopen oan 01/08 vì bỏ bước này. Bó mã của lô này là
    `index-BbPPdate.js` — **khác** bó mã `index-eWHwDgt2.js` của lô F7 sáng nay ⇒ **không kế thừa quan sát cũ**,
    kể cả các vế F7 đã ghi ĐẠT.
12. **Bẫy nút Xuất bị mờ:** báo cáo đang hiện số liệu mà nút Xuất mờ → do đã bấm [Xem báo cáo] **từ 2 lần trở
    lên** (đã có phiếu `BCTK_QA07`). Tải lại trang, chọn lại bộ lọc, bấm **đúng một lần**. Đừng ghi thành
    *"dev đã ẩn nút"*.
13. **Bẫy khung thông báo:** khung sống ~3,3 giây và giao diện **thay chữ ngay trong khung cũ**, không mọc khung
    mới ⇒ bộ bắt kiểu "node mới thêm" báo nhầm *"không có thông báo nào"*. Phải theo dõi **nội dung** khung theo
    thời gian; muốn chụp thì hẹn giờ bấm nút sau ~2500 ms **rồi mới** gọi lệnh chụp. Ứng dụng gửi lời gọi xuất
    qua **XHR**, không qua `fetch`.
14. **Số trên màn lệch với dữ liệu thật do bộ nhớ đệm máy chủ.** `srs-v3.5.md:5691` (BR-RPT-01) mô tả cron tổng
    hợp hàng đêm 02:00 vào bảng đệm. Tiêu chí **A9 so tệp với MÀN của chính lần đo đó**, không so với dữ liệu
    gốc ⇒ đệm cũ **không** phải lý do FAIL của lô này. Đừng mở rộng điều tra.
15. **Không chấm FAIL vì không nhìn thấy ba mã quyền báo cáo bị gỡ khỏi vai trò QTHT** (việc số 5 của BA,
    `:425` — thuộc dữ liệu khởi tạo). Không đo được từ giao diện. Nếu có dấu hiệu màn được ẩn bằng cách kiểm vai
    trò trực tiếp thay vì qua cơ chế phân quyền → **ghi candidate một dòng**, không mở rộng điều tra.
    *(BA cũng tự ghi ở `:433` rằng ba mã quyền đó hiện **không tra được** vì `srs-fr-10-quan-tri.md` §3.4.3.41
    không có danh sách.)*
16. **Mục "Báo cáo thống kê" vẫn hiện với tài khoản CB Nghiệp vụ / CB Phê duyệt** — **đúng**, đó là tác nhân của
    chức năng (`:51`, `:62`). Đây còn là **đối chứng cần thiết** cho B1.
17. **Không kết luận "đã fix" khi mới chỉ thấy CB Nghiệp vụ xuất được.** Vai trò đó vốn đã chạy tốt ở lượt đo
    trước. Phép đo quyết định của cụm này là chạy bằng chính vai trò **Quản trị hệ thống** (vế B).

---

## §6. Quy tắc ra verdict

1. **Bug gốc gộp nhiều ý → mọi ý hết lỗi mới Pass.** Còn ≥1 ý lỗi → **Reopen**.
   Với lô này, "mọi ý" = **vế B đạt (B1+B2+B4)** **VÀ** **vế A đạt A1→A11 trên đúng loại báo cáo của phiếu đó**.
2. **Fix một phần = Reopen**, không phải "Pass kèm ghi chú". Đặc biệt: chỉ ẩn nút Xuất mà vẫn cho vào màn = Reopen.
3. **Cấm Pass bằng quan sát tĩnh.** Phải chạy hết luồng tới bước sinh ra lỗi cũ, và với vế A phải **mở tệp ra
   đọc**. Nhìn thấy nút / tải được tệp ≠ đạt.
4. **Cấm Pass theo kỳ vọng gốc** (QTHT xuất được tệp) — xem §2.2. Nếu quan sát thấy QTHT nhận được tệp thì đó là
   **FAIL B4**, không phải Pass.
5. **QTHT không vào được màn CHÍNH LÀ PASS**, không phải blocker, không ghi "Chưa chốt", không hỏi lại BA.
6. **Verdict ghi vào ô `Trạng thái dev fix`:**
   - `Test done` — khi Pass.
   - `Reopen` — khi còn ≥1 ý lỗi.
7. **Verdict Pass bắt buộc kèm câu** cho cả 21 phiếu: *kỳ vọng gốc của đối tác (Quản trị hệ thống xuất được tệp)
   KHÁC đặc tả hiện hành; nghiệp vụ đã chốt 06/08 giữ nguyên đặc tả, không nới quyền* — kèm nội dung `[Lý do]` +
   `[Nhận định]` BA đã soạn sẵn (`phan-hoi-ba-7-diem-can-chot-2026-08-06.md:437`–`:439`).
8. **Thấy bất thường NGOÀI phạm vi 21 phiếu** → ghi mục "Ghi nhận thêm", báo lại. **Không tự thêm dòng mới vào
   sheet đối tác**; phiếu bug mới chỉ mở trên sheet làm việc theo quy ước mã `<tiền tố module>_QA<số>`.
9. **Hiệu lực verdict** chỉ trên env `18.143.165.120.nip.io` + đúng bó mã `index-BbPPdate.js`. Env nghiệm thu của
   đối tác là môi trường khác ⇒ phải đo lại sau khi bản dựng lên môi trường đó.

---

## §7. Tài khoản · môi trường · điểm cần người ra đề quyết

**Tài khoản:**

| Vai trò | Tài khoản | Dùng cho |
|---|---|---|
| Cán bộ Nghiệp vụ - Trung ương | `cbnv_tw_05` / `Test@1234` (`../../input/input.md:55`) | **Vế A** — 21 loại báo cáo |
| Quản trị hệ thống (TW) | `admin` / `Secret@123` (`../../input/input.md:8`–`:12`) | **Vế B** — 1 lượt, áp chung 21 dòng |

- Tài khoản bị khoá → **fallback 1 lượt trong CÙNG vai trò + CÙNG cấp** (`cbnv_tw_05` → `_04` → `_03` → `_02` →
  `_01` → `cbnv_tw`), **bắt buộc ghi tài khoản thực dùng** trong báo cáo. Tuyệt đối không đổi vai trò/cấp.
- `admin` **không có sibling** ⇒ khoá thì **STOP, báo lại**, không thay bằng tài khoản khác.
- **Ngoại lệ có ý thức với quy ước "admin chỉ dùng để dựng dữ liệu":** ở lô này **chính vai trò quản trị hệ
  thống là đối tượng kiểm** — lỗi đối tác báo phát sinh khi đăng nhập bằng vai trò đó.

**Ba điểm cần người ra đề quyết trước/trong khi đo:**

1. **Vế B3 nếu FAIL** (còn `Forbidden` / mã kỹ thuật): theo `chuan-14-case-bctk.md:143`, câu chữ khi từ chối
   thuộc phiếu QA riêng `BUG-BCTK-QA01` (dòng 363), **không** dùng để lật verdict cụm phiếu. Chuẩn này giữ nguyên
   quy ước đó (§4, luật dừng sớm). Nếu người ra đề muốn B3 lật được verdict 21 phiếu thì **phải nói trước khi đo**.
2. **`VVTLV_06` (row 227) → *BC Vụ việc theo lĩnh vực*** là mã DUY NHẤT trong 21 dòng **không có tiền lệ ánh xạ
   trực tiếp** (không có trong `RECIPE.md` §6, không có anh em `_07` trong `chuan-14`). Ánh xạ suy từ tiền tố mã
   + vị trí UC135 trong dãy liên tiếp. Người đo **phải đọc nhãn thật trên ô chọn** và xác nhận trước khi chạy.
3. **`CPCTHTTTG_06` (row 264, *BC Chi phí theo thời gian*, PDF)** đã Pass sáng 07/08 nhưng trên **bó mã cũ**
   `index-eWHwDgt2.js`. Bó mã hiện tại đã đổi. Nếu muốn kết quả đó còn hiệu lực trên bó mã mới thì **phải đo
   lại** — chuẩn này **không** đưa nó vào lô 21, chờ người ra đề quyết.
