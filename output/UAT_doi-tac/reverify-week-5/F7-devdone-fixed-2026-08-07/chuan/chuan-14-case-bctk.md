# Chuẩn chấm đã khóa — 14 phiếu Báo cáo thống kê (cụm "QTHT xuất tệp bị 403 Forbidden")

> **Nguồn đặc tả — DUY NHẤT của cụm này (prompt session chỉ định):**
> `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
> — `srs-fr-11-bao-cao.md` (1.295 dòng) · `srs-v3.5.md` (7.012 dòng) · `srs-fr-05-vu-viec.md` (2.506 dòng).
> Mọi số dòng dưới đây **agent này tự mở file đọc lại ngày 2026-08-07**. Không quote từ trí nhớ, không quote
> từ `input/srs-update-2026-5-5/`, không quote từ báo cáo đợt cũ.
>
> **Quyết định BA đã chốt 2026-08-06 — mục 5** (`../../ba-confirm/phan-hoi-ba-7-diem-can-chot-2026-08-06.md:373-441`)
> đã được **thi hành vào SRS**: tệp `srs-fr-11-bao-cao.md` hiện mang 5 dấu `[BA chốt 2026-08-06]` (`:79`, `:120`,
> `:127`, `:128`, `:1046`, `:1056`, `:1057`, `:1058`, `:1273`). ⇒ SRS hiện hành **đã khác** SRS mà 14 phiếu và
> bug entry `BUG-BCTK-QA01` từng dẫn. Phải đọc lại trước khi đo.
>
> **Nguồn canonical cho cách đo:** khối `── CÁCH VERIFY sau Dev fix ──` đã ghi vào ô *Kết quả verify* tab `bug`
> ngày 06/08/2026 (nhật ký `output/UAT_doi-tac/tools/sheet_bug_verify_write.log`, có đủ cho cả 14 dòng). Khối đó
> khóa sẵn **hai nhánh PASS**; BA vừa chốt chính là **nhánh thứ hai**.

**Lô đo:** 14 phiếu, cùng một lỗi gốc, cùng một màn `/bao-cao`.

| Dòng | Mã TC | Loại báo cáo | Định dạng |
|---|---|---|---|
| 174 | SLHDVM_06 | BC Số lượng hỏi đáp/vướng mắc PL | Excel |
| 200 | CLDTBDDDR_06 | BC Lớp đào tạo đang diễn ra | Excel |
| 205 | LDTBDDDR_06 | BC Lớp đào tạo đã diễn ra | Excel |
| 210 | CGTVPL_06 | BC Số lượng CG/TVV | Excel |
| 214 | DGHQHTPL_06 | BC Đánh giá hiệu quả HTPL | Excel |
| 218 | CLDTBDPL_06 | BC Chất lượng đào tạo | Excel |
| 238 | CPHTCT_06 | BC Chi phí chi trả hỗ trợ | Excel |
| 243 | CPCTHTTDVQL_06 | BC Chi phí theo đơn vị | Excel |
| 258 | CPCTHTTLHDN_06 | BC Chi phí theo loại hình DN | Excel |
| **264** | **CPCTHTTTG_06** | **BC Chi phí theo thời gian** | **PDF** — nút thật là **[Xuất file]** trong hộp thoại |
| 267 | SLCTHT_06 | BC Số lượng chương trình hỗ trợ | Excel |
| 272 | CTTDVQL_04 | BC Chương trình theo đơn vị | Excel |
| 277 | CTTLV_05 | BC Chương trình theo lĩnh vực | Excel |
| 281 | CTTTG_04 | BC Chương trình theo thời gian | Excel |

---

## 1. Bảng "Dòng SRS đã mở đọc lại" (2026-08-07)

`{…}` = cắt bớt cho vừa ô, không đổi chữ. Cột cuối so với số dòng **đã dùng ở vòng 06/08** (bug entry
`BUG-BCTK-QA01` + thư BA mục 5).

### 1.1 `srs-fr-11-bao-cao.md`

| Dòng vòng trước | **Dòng THẬT 07/08** | Nguyên văn dòng đọc được | Khớp / lệch |
|---|---|---|---|
| `:51` | **`:51`** | `**Tác nhân chính:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Cán bộ Phê duyệt (TW/BN/ĐP)` | ✅ **KHỚP** cả số dòng lẫn nội dung |
| `:62` | **`:62`** | `- User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)` | ✅ **KHỚP** |
| `:79` | **`:79`** | `\| 1 \| **Kiểm tra vai trò trước:** chỉ CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP) được truy cập chức năng báo cáo. Vai trò khác (kể cả QTHT) → chặn ngay ở cửa vào, không mở màn hình. Sau đó kiểm phạm vi theo đơn vị `[BA chốt 2026-08-06]` \| BR-AUTH-01 \|` | ⚠️ **Số dòng khớp · NỘI DUNG ĐÃ ĐỔI** — vòng trước dòng này chưa có mệnh đề "kể cả QTHT → chặn ngay ở cửa vào, không mở màn hình" |
| `:85` | **`:85`** | `\| 7 \| Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo **Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]` \| — \|` | ✅ **KHỚP** (chỉ thêm nhãn "nâng thành quy ước chung 2026-08-06") |
| `:86` | **`:86`** | `\| 8 \| Nếu xuất PDF: tạo file .pdf theo khung văn bản hành chính Thông tư 17/2025 — khổ A4, font Times New Roman cỡ 13; **đầu trang** có quốc hiệu, tiêu ngữ và tên cơ quan ban hành; **cuối trang** có ngày ký, họ tên cán bộ xuất báo cáo và chỗ trống cho con dấu khi in chính thức. **Không in dòng chức danh người ký** {…} Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` theo **Phụ lục E §H8** `[BA chốt 2026-08-04]` {…}` | ✅ **KHỚP** |
| `:105` | **`:105`** | `- Không thay đổi dữ liệu nghiệp vụ (read-only)` | ✅ **KHỚP** |
| `:109-119` | **`:109-120`** | Bảng lỗi: `:109` header · `:110` separator · `:111`–`:120` = **E1…E10** | ⚠️ **BẢNG DÀI THÊM 1 DÒNG** — vòng trước chạy E1–E9 (`:111`–`:119`), nay có thêm **E10** ở `:120` |
| `:117` | **`:117`** | `\| E7 \| Không có quyền \| ERR-RPT-05 \| "Bạn không có quyền xem báo cáo này" \| ERROR \|` | ✅ **KHỚP** — dòng cũ giữ nguyên, KHÔNG bị gỡ |
| — (mới) | **`:120`** | `\| E10 \| Không có quyền **thực hiện thao tác xuất tệp** (vai trò ngoài CB NV / CB PD) \| ERR-RPT-08 \| "Bạn không có quyền thực hiện thao tác này" (câu chuẩn `srs-fr-05-vu-viec.md` §3.E — Thông báo người dùng) `[BA chốt 2026-08-06]` \| ERROR \|` | 🆕 **DÒNG MỚI** — đúng việc số 6 trong Phương án xử lý của BA |
| `:123` ("xuất + tự tải tệp") | **`:124`** (Excel) · **`:125`** (PDF) | `:124` = `- **Given** CB nhấn "Xuất Excel" **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (Phụ lục E §H8)` · `:125` = bản PDF, thêm quốc hiệu/tiêu ngữ/tên cơ quan + ngày ký + họ tên + chỗ con dấu, "không có dòng chức danh" | ❌ **LỆCH +1** — do chèn E10 ở `:120`. `:123` hiện là AC *xem* báo cáo, **không** phải AC xuất tệp. Quote `:123` cho vế xuất = quote sai dòng |
| — (mới) | **`:127`** | `- **Given** người dùng vai trò Quản trị hệ thống **When** đăng nhập **Then** **không thấy** mục menu "Báo cáo thống kê" (ẩn theo M-05, không làm mờ) `[BA chốt 2026-08-06]`` | 🆕 **AC MỚI** — căn cứ chính của vế C2 |
| — (mới) | **`:128`** | `- **Given** vai trò ngoài CB Nghiệp vụ / CB Phê duyệt **When** gọi thẳng dịch vụ xuất tệp ở tầng máy chủ (không có đường bấm từ giao diện vì màn đã ẩn) **Then** từ chối với `ERR-RPT-08` — "Bạn không có quyền thực hiện thao tác này" `[BA chốt 2026-08-06]`` | 🆕 **AC MỚI** — căn cứ chính của vế C1 + C3 |
| — (mới) | **`:1046`** | `> **Điều kiện vào màn — áp cho TOÀN BỘ bảng dưới đây** `[BA chốt 2026-08-06]`: người dùng phải có vai trò **Cán bộ Nghiệp vụ** hoặc **Cán bộ Phê duyệt** (TW/BN/ĐP). Vai trò khác — kể cả **Quản trị hệ thống** — **không vào được màn này**; mục menu "Báo cáo thống kê" bị **ẩn** theo quy ước M-05 (ẩn, không làm mờ). {…}` | 🆕 **KHỐI MỚI** — nâng điều kiện vai trò lên trên toàn bảng thành phần màn hình |
| `:1047` (ô chọn loại BC) | **`:1052`** | `\| 3 \| filter-bar \| Dropdown loại BC \| select (searchable, grouped) \| 23 loại BC phân nhóm theo optgroup {…} \| change → load bộ lọc đặc thù \| Luôn hiển thị \|` | ❌ **LỆCH +5** · cột Điều kiện hiển thị **vẫn ghi "Luôn hiển thị"** — nhưng khối `:1046` đã phủ điều kiện vai trò lên toàn bảng ⇒ **không phải khoảng trống đặc tả** (xem §4 ghi chú) |
| `:1051` (nút Xem BC) | **`:1056`** | `\| 7 \| action-bar \| Nút Xem báo cáo \| button (primary) \| "Xem báo cáo" → chạy query \| click → load data \| **Chỉ với vai trò CB Nghiệp vụ / CB Phê duyệt** — vai trò khác không vào được màn này (M-05 ẩn mục menu) `[BA chốt 2026-08-06]` \|` | ❌ **LỆCH +5 · NỘI DUNG ĐỔI** — vòng trước ghi "Luôn hiển thị" |
| `:1052` (nút Xuất Excel) | **`:1057`** | `\| 8 \| action-bar \| Nút Xuất Excel \| button \| "Xuất Excel (.xlsx)" → xuất theo format TT17/2025 \| click → auto-download \| Sau khi đã "Xem báo cáo" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]` \|` | ❌ **LỆCH +5 · NỘI DUNG ĐỔI** — vòng trước chỉ có "Sau khi đã Xem báo cáo" |
| `:1053` (nút Xuất PDF) | **`:1058`** | `\| 9 \| action-bar \| Nút Xuất PDF \| button \| "Xuất PDF (.pdf)" → xuất theo khung trình bày TT17/2025 (không dùng Mẫu 21a/21b) \| click → auto-download \| Sau khi đã "Xem báo cáo" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]` \|` | ❌ **LỆCH +5 · NỘI DUNG ĐỔI** |
| `:1092` (nội dung đầu tệp xuất) | **`:1097`** | `- Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file. Riêng PDF bổ sung khung văn bản hành chính: quốc hiệu + tên cơ quan ở đầu trang, ngày ký + họ tên cán bộ xuất báo cáo + chỗ con dấu ở cuối trang (không có dòng chức danh). Tên tệp cả hai định dạng theo **Phụ lục E §H8** — `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`` | ❌ **LỆCH +5** · nội dung giữ nguyên. (`:1092` hiện là dòng bảng mapping `UC146 — BC CT theo thời gian`) |
| `:1268` (BR-AUTH-08 "QTHT bypass") | **`:1273`** | `\| BR-AUTH-08 \| chính sách phân quyền áp dụng cho MỌI bảng có cột `don_vi_id`. TW thấy toàn quốc, BN thấy BN, ĐP thấy ĐP \| Architecture AD-07 \| Toàn bộ FR-IX \| — (QTHT **không phải tác nhân của nhóm IX** nên không có ca bypass ở đây; ngoại lệ QTHT của BR-AUTH-08 chỉ áp cho các nhóm mà QTHT là tác nhân) `[BA chốt 2026-08-06]` \| Verify phân quyền \|` | ❌ **LỆCH +5 · NỘI DUNG ĐỔI HẲN** — chữ **"QTHT bypass"** ĐÃ BỊ GỠ (việc số 7 của BA). `:1268` hiện là dòng trống. **Đây là dòng bug entry cũ từng dùng để lập luận QTHT được chạy nhóm IX ⇒ căn cứ đó không còn** |

### 1.2 `srs-v3.5.md`

| Dòng vòng trước | **Dòng THẬT 07/08** | Nguyên văn dòng đọc được | Khớp / lệch |
|---|---|---|---|
| `:684` | **`:684`** | `\| M-05 \| **Hiển thị theo quyền** — menu item chỉ hiện nếu vai trò có quyền truy cập ≥ 1 chức năng trong đó. Ẩn (không disable) nếu không có quyền \| NF-Security \|` | ✅ **KHỚP** cả số dòng lẫn nội dung |
| `:1335` (dòng BAO_CAO, ô R của QTHT) | **`:1339`** | `\| BAO_CAO \| R \| CRU* \| CRU* \| CRU* \| RU* \| RU* \| RU* \| — \| — \| — \| — \|` (header cột ở `:1300`: `\| Entity \| QTHT \| CB_NV_TW \| …`) | ❌ **LỆCH +4** · ô QTHT **vẫn là `R`**, BA cố ý **không sửa** dòng này |
| — (mới) | **`:1296`–`:1298`** | `:1296` = `> **Bảng này là quyền ở MỨC DỮ LIỆU, không phải quyền chạy chức năng** `[làm rõ 2026-08-06]`. Một ô có `R` chỉ nói vai trò đó **được đọc dữ liệu** {…} nó **không** đồng nghĩa vai trò đó là **tác nhân** {…}` · `:1298` = `> Ví dụ đã gây tranh chấp ở UAT tuần 5: `BAO_CAO` cột QTHT = `R`, nhưng cả 23 mục FR-IX lẫn 23 giao dịch UC124–146 đều ghi tác nhân là **CB Nghiệp vụ / CB Phê duyệt** — QTHT **không** vào màn báo cáo thống kê và **không** xuất tệp báo cáo. {…}` | 🆕 **KHỐI CHÚ THÍCH MỚI** (việc số 3 của BA) — **vô hiệu hóa lập luận "QTHT có `R` nên được xem/xuất"** của bug entry cũ (`bug-report-BCTK.md:50`) |
| — | **`:6760`** | Phụ lục E **§H8** — `**Khuôn:** {TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`; `{TenTep}` PascalCase, bỏ dấu tiếng Việt và mọi ký tự không phải chữ/số; `[BA chốt 2026-08-06 — nâng phạm vi quyết định 2026-08-04 của Nhóm IX thành quy ước chung]` | ✅ căn cứ khuôn tên tệp (dùng ở §3 "không được chấm FAIL") |

### 1.3 `srs-fr-05-vu-viec.md` — câu tiếng Việt chuẩn cho ca thiếu quyền

| Dòng BA dẫn | **Dòng THẬT 07/08** | Nguyên văn dòng đọc được | Khớp / lệch |
|---|---|---|---|
| `:1594` | **`:1594`** | `\| Không có quyền truy cập \| Toast error \| "Bạn không có quyền thực hiện thao tác này" \|` (bảng §3.E "Thông báo người dùng", header ở `:1588`) | ✅ **KHỚP** cả số dòng lẫn nội dung |

### 1.4 Mã lỗi / câu thông báo tiếng Việt SRS quy định cho ca thiếu quyền ở nhóm báo cáo

| Ca | Mã lỗi | Câu tiếng Việt bắt buộc | `file:dòng` |
|---|---|---|---|
| Không có quyền **xem** báo cáo | `ERR-RPT-05` (E7) | "Bạn không có quyền xem báo cáo này" | `srs-fr-11-bao-cao.md:117` |
| Không có quyền **thực hiện thao tác xuất tệp** | `ERR-RPT-08` (E10) | "Bạn không có quyền thực hiện thao tác này" | `srs-fr-11-bao-cao.md:120` · AC `:128` · câu gốc `srs-fr-05-vu-viec.md:1594` |

**Mã `ERR-PERM-SYS-00-01` và chuỗi `Forbidden` không tồn tại ở bất kỳ dòng nào của thư mục `srs-v3.5/`.**
Cả hai mã hợp lệ đều là **câu tiếng Việt** ⇒ vế "phải bằng tiếng Việt" là phần **chung của cả hai bản**, không
phụ thuộc việc BA đổi mã.

---

## 2. Bảng vế C1–C4

Quan hệ đã tính **sau** quyết định BA 06/08 và **sau** khi SRS đã được thi hành theo quyết định đó.

| Vế | Mô tả lỗi còn lại (điều đang phải chứng minh) | SRS `file:dòng` | Quan hệ | Thao tác đo | ✅ PASS khi | ❌ FAIL khi |
|---|---|---|---|---|---|---|
| **C1** | Máy chủ từ chối thao tác xuất tệp của vai trò QTHT — **kỳ vọng gốc của 14 phiếu đòi ngược lại** ("xuất và tự động tải tệp về máy") | `srs-fr-11-bao-cao.md:51` · `:62` · `:79` · `:120` · `:128` · `:1273` · `srs-v3.5.md:1296-1298` (ô `R` ≠ quyền chạy chức năng) | **DIFF — đã đóng bởi BA 06/08, SRS thắng.** Không hỏi lại BA. **CẤM Pass theo kỳ vọng gốc.** Ghi verdict kèm câu: `DEV ĐANG ĐÚNG SRS HIỆN HÀNH · EXPECTED GỐC KHÁC SRS` | Sau khi C2 đã fix thì giao diện **không còn đường bấm** ⇒ đo đúng ca AC `:128`: dùng phiên đăng nhập QTHT gọi thẳng dịch vụ xuất tệp ở tầng máy chủ, đọc mã trả về + thân phản hồi. (Nếu C2 chưa fix, đo bằng nút trên màn) | Hệ thống **từ chối**, không sinh tệp nào cho vai trò QTHT | Vai trò QTHT **nhận được tệp** — tức dev đã nới quyền, trái `:51`/`:62`/`:79` và trái quyết định BA. FAIL này **dừng lô ngay** |
| **C2** 🔴 **VẾ QUYẾT ĐỊNH VERDICT** | Giao diện vẫn **mời rồi mới chặn**: QTHT vẫn thấy mục menu, vẫn vào `/bao-cao`, bấm [Xem báo cáo] vẫn ra đủ số liệu, hai nút Xuất vẫn sáng | `srs-fr-11-bao-cao.md:79` (chặn ngay ở cửa vào, **không mở màn hình**) · `:127` (AC — **không thấy** mục menu, ẩn theo M-05, **không làm mờ**) · `:1046` (điều kiện vào màn áp toàn bảng) · `:1056` · `:1057` · `:1058` · `srs-v3.5.md:684` (M-05 — **ẩn, không disable**) | **MATCH** — kỳ vọng đã khóa ở nhánh 2 của `── CÁCH VERIFY sau Dev fix ──` ("chặn NGAY từ bước [Xem báo cáo], không cho xem đủ số liệu rồi mới chặn") trùng SRS hiện tại; SRS còn mạnh hơn: **ẩn hẳn mục menu** | Đăng nhập `admin` (QTHT, cấp TW) → tải lại trang → duyệt toàn cây điều hướng tìm mục "Báo cáo thống kê" (kể cả trong 6 sub-menu, `srs-v3.5.md:116`) → **đối chứng độc lập:** gõ thẳng địa chỉ `/bao-cao` | Cây điều hướng của QTHT **không có** mục "Báo cáo thống kê" (ẩn hẳn) **VÀ** vào thẳng `/bao-cao` không mở được màn báo cáo — không hiện ô chọn loại BC, không hiện số liệu, không hiện nút xuất nào | (a) Mục menu vẫn còn — **kể cả khi bị làm mờ / disable** (`:684` đòi ẩn) · (b) Vào được `/bao-cao` và [Xem báo cáo] vẫn trả đủ số liệu · (c) **Fix nửa vời:** chỉ ẩn/mờ hai nút Xuất nhưng vẫn cho vào màn và xem số liệu — đúng chữ BA gọi là *"vẫn mời rồi chặn, chỉ lùi một bước"* |
| **C3a** | Câu từ chối đẩy ra người dùng là chuỗi tiếng Anh kỹ thuật `Forbidden` / mã máy chủ `ERR-PERM-SYS-00-01` | `srs-fr-11-bao-cao.md:117` **và** `:120` (cả hai đều là câu tiếng Việt) · `:128` · `srs-fr-05-vu-viec.md:1594` | **MATCH** — phần "phải là câu tiếng Việt cho biết không có quyền" là phần **chung** của kỳ vọng gốc và SRS hiện tại, không đổi khi BA đổi mã | Nếu C2 **FAIL** (vẫn vào được màn): đọc **nguyên văn** chữ trên khung thông báo tại đúng thời điểm lỗi. Nếu C2 **PASS**: đọc thân phản hồi của lời gọi xuất ở tầng máy chủ (ca AC `:128`) | Chữ người dùng nhận được là **câu tiếng Việt** cho biết không có quyền, mã nằm trong **bộ mã báo cáo** (`ERR-RPT-08` đúng nhất; `ERR-RPT-05` **vẫn chấp nhận**, xem §3) | Vẫn là `Forbidden`, `ERR-PERM-SYS-00-01`, hoặc **bất kỳ** chuỗi tiếng Anh / mã kỹ thuật nào đẩy nguyên ra người dùng |
| **C3b** | Mã/câu **chính xác** cho thao tác **xuất**: phiếu QA cũ `BUG-BCTK-QA01` bắt câu `:117`; SRS nay quy định `ERR-RPT-08` `:120` | `srs-fr-11-bao-cao.md:120` vs `:117` | **DIFF — đã đóng bởi BA 06/08.** BA nêu đích danh: *"Cần báo lại QA chỉnh phiếu `BUG-BCTK-QA01` — phiếu đó đang yêu cầu Dev hiện đúng câu `:117`"* | — (không đo riêng) | — | **KHÔNG chấm FAIL vế này.** Chỉ ghi nhận dev đang dùng mã nào. Xem §3 mục 6 |
| **C4** | Chống hồi quy: vai trò **CB Nghiệp vụ TW** (vai trò SRS nêu đích danh) phải **vẫn** xuất được, tệp mở đọc được, số khớp màn | `srs-fr-11-bao-cao.md:124` (Excel) · `:125` (PDF) · `:85` · `:86` · `:1097` · `srs-v3.5.md:6760` (§H8) | **MATCH** — trùng kỳ vọng gốc của cả 14 phiếu ("xuất và tự động tải tệp về máy" + tên tệp đúng khuôn) | Đăng nhập CB NV TW (`cbnv_tw_0X`) → với **từng** loại BC trong lô: chọn kỳ + đơn vị → [Xem báo cáo] **đúng một lần**, ghi lại các số trên màn → bấm xuất → **MỞ TỆP RA ĐỌC** (openpyxl cho .xlsx, PyMuPDF cho .pdf) | Tệp về máy và **mở được**; phần đầu tệp có đủ **4 mục**: tên báo cáo · kỳ · đơn vị · ngày tạo (`:1097`); **số trong tệp khớp số trên màn của chính lần đo đó**. Riêng **CPCTHTTTG_06 (PDF)**: thêm — khổ **A4**; **đầu trang** có quốc hiệu + tiêu ngữ + tên cơ quan; **cuối trang** có ngày ký + họ tên cán bộ xuất báo cáo + chỗ trống con dấu (`:86`, `:125`) | Không có tệp / tệp không mở được / số trong tệp lệch số trên màn / thiếu bất kỳ mục nào trong 4 mục đầu tệp / PDF thiếu mục khung hành chính hoặc khổ giấy khác A4 khi để mặc định / tái hiện câu "Không thể tạo file xuất. Vui lòng thử lại." |

**Biến thể bắt buộc** (chỉ lấy từ nguồn canonical + SRS, không tự thêm):

- **C2** đo **một lần / một phiên QTHT** — kết quả áp chung cho cả 14 phiếu vì cả 14 dùng **cùng một màn** `/bao-cao` (SRS `:1042` — *"Một trang báo cáo thống nhất cho tất cả 23 loại BC"*; `:1036` = *"Loại màn hình: Dashboard (Unified Report Page)"*). Không cần lặp 14 lần.
- **C4** đo **theo từng loại BC** của 14 phiếu (13 Excel + 1 PDF) — vì mỗi phiếu là một loại báo cáo riêng trong ô chọn.
- Khối `── CÁCH VERIFY ──` của **SLHDVM_06** còn khóa thêm **2 cấu hình bộ lọc** (không lọc / Lĩnh vực PL = "Thuế") — chỉ áp cho **riêng phiếu 174**, không nâng thành yêu cầu chung cho 13 phiếu còn lại.
- **CPCTHTTTG_06** dùng **hộp thoại "Tùy chọn in báo cáo PDF"**, để **mặc định A4 + Dọc**, lượt xuất thật là nút **[Xuất file]** trong hộp thoại.

---

## 3. Bẫy / KHÔNG được chấm FAIL

Đều là **tiền lệ đã chốt**, không phải suy đoán:

1. **Tên tệp theo khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}`.** Ví dụ `BaoCaoChiPhiTheoThoiGian_20260806_1426.pdf` — **đúng**, không phải `BaoCaoChiPhi_…`. Căn cứ `:85`, `:86`, `srs-v3.5.md:6760` §H8 `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]`.
2. **Không in dòng chức danh người ký.** `:86` ghi thẳng *"**Không in dòng chức danh người ký** — hồ sơ tài khoản không lưu chức vụ (ngoại lệ của khung chung §D.2.4)"* `[BA chốt 2026-08-04]`. Phiếu gốc chờ có dòng chức danh — kỳ vọng đó **đã hết hiệu lực**.
3. **Phông đọc ra là "Tinos"** (`Tinos-Regular` / `Tinos-Bold` / `Tinos-Italic`) — bản tương thích số đo của Times New Roman ⇒ **đạt** tiêu chí "Times New Roman cỡ 13".
4. **Tệp không có chữ ký số** — `:86` chỉ đòi **chỗ trống cho con dấu khi in chính thức**, không đòi ký số.
5. **Tên sheet · thứ tự cột · màu sắc · biểu đồ trong tệp** — nằm ngoài điều 14 phiếu phản ánh. Nguồn canonical ghi thẳng: *"Đừng chấm Fail vì tên tệp, tên sheet, thứ tự cột, khổ giấy, phông chữ hay việc thiếu thông báo 'Đang tạo file...'"*.
6. **Dev hiện đúng câu `:117` ("Bạn không có quyền xem báo cáo này") thay vì `ERR-RPT-08`.** BA vừa đổi ngày 06/08, phiếu cũ `BUG-BCTK-QA01` đang bắt `:117` — dev làm theo phiếu cũ là **hợp lý**. Ghi nhận là điểm cần chỉnh phiếu + dev đổi mã ở lượt sau, **KHÔNG chấm FAIL**.
7. **Mục "Báo cáo thống kê" vẫn hiện với tài khoản CB NV / CB PD** — đúng, đó là tác nhân của chức năng.
8. **Không kết luận "đã fix" khi chỉ thấy CB Nghiệp vụ xuất được** — vai trò đó **vốn đã chạy tốt** ở lượt đo 06/08. Phép đo quyết định là chạy bằng chính vai trò **Quản trị hệ thống**.
9. **Không dừng ở "tải được tệp"** — phải **mở tệp ra đọc** mới chốt được C4 (tiền lệ: 200 + binary chỉ chứng minh tệp được TẠO, không chứng minh ĐÚNG).
10. **Bẫy nút [Xuất PDF]** (chỉ phiếu 264): nút này **chỉ mở hộp thoại**. Dừng ở đó sẽ không thấy lời gọi nào và dễ kết luận nhầm "hệ thống im lặng".
11. **Bẫy khung thông báo:** khung sống ~3,3 giây và giao diện **thay chữ ngay trong khung cũ**, không mọc khung mới ⇒ bộ bắt kiểu "node mới thêm" báo nhầm *"không có thông báo nào"*. Phải theo dõi **nội dung** khung theo thời gian; muốn chụp thì hẹn giờ bấm nút sau ~2500 ms rồi mới gọi lệnh chụp. Ứng dụng gửi lời gọi xuất qua **XHR**, không qua `fetch`.
12. **Bẫy nút Xuất bị mờ:** nếu báo cáo đang hiện số liệu mà nút Xuất mờ → do đã bấm [Xem báo cáo] **từ 2 lần trở lên**. Tải lại trang, chọn lại bộ lọc, bấm **đúng một lần**. Đừng ghi thành "dev đã ẩn nút cho QTHT".
13. **Bẫy bản dựng:** tab trình duyệt mở lâu vẫn chạy mã cũ. **Tải lại trang + ghi tên bản dựng một lần đầu lô** (tiền lệ: đã báo Reopen oan 01/08 vì bỏ bước này).
14. **Không chấm FAIL vì không nhìn thấy 3 mã quyền báo cáo bị gỡ khỏi vai trò QTHT** (việc số 5 của BA — dữ liệu khởi tạo). Không đo được từ giao diện; nếu dev ẩn menu bằng cách kiểm vai trò trực tiếp thay vì qua cơ chế phân quyền thì ghi **candidate một dòng**, không mở rộng điều tra.
15. **Không dùng ô `R` của QTHT ở `srs-v3.5.md:1339` để lập luận QTHT được xem/xuất** — khối chú thích mới `:1296-1298` đã bác thẳng lập luận đó. Bug entry cũ `bug-report-BCTK.md:50` dựa vào chính lập luận này ⇒ **căn cứ đã hết hiệu lực**.

---

## 4. Ghi chú cho người đo

**Vế bắt buộc phải chạy để Pass 14 phiếu:** **C2** và **C4**. **C1** chạy để xác nhận **không bị nới quyền ngược**.

- **C3a** đo được thì đo, nhưng **KHÔNG dùng để lật verdict của 14 phiếu** — câu chữ khi từ chối thuộc phiếu QA riêng `BUG-BCTK-QA01` (dòng 363 tab `bug`, mã `BCTK_QA01`), độc lập với việc 14 phiếu Pass hay Reopen.
- **C3b** không đo, không chấm.

**Luật dừng sớm (FLOW 03) — được dừng ngay khi:**

| Tình huống | Xử lý |
|---|---|
| **C2 FAIL** (menu vẫn hiện/mờ · vẫn vào được `/bao-cao` · vẫn xem đủ số liệu · chỉ ẩn 2 nút Xuất) | **Reopen cả lô 14 phiếu, dừng ngay.** Không cần chạy C4 cho đủ 14 loại. Vẫn ghi mọi vế kết luận được **từ chính artifact đã có** |
| **C1 FAIL** (QTHT nhận được tệp) | **Reopen, dừng ngay** — nới quyền trái `:51`/`:62`/`:79` + trái quyết định BA |
| **C4 FAIL** ở bất kỳ loại BC nào | **Reopen, dừng các loại còn lại.** Ghi rõ loại nào đã đo đạt, loại nào chưa đo |

**Muốn Pass thì phải chạy hết:** C2 (1 lượt) + C1 (1 lượt đối chứng) + C4 (đủ 14 loại, mỗi loại mở tệp ra đọc)
+ 2 cấu hình bộ lọc riêng cho phiếu 174.

**Điểm dễ hiểu nhầm — đọc trước khi đo:**

- Nếu **QTHT không vào được màn** thì tiền đề *"bấm [Xem báo cáo] rồi bấm [Xuất Excel]"* của 14 phiếu **tự tiêu**. Đó chính là **PASS**, **KHÔNG** phải blocker và **không** ghi "Chưa chốt".
- `:1052` (ô chọn loại BC) vẫn ghi *"Luôn hiển thị"* — **không** phải khoảng trống đặc tả: khối `:1046` đã tuyên bố cột "Điều kiện hiển thị" của **từng dòng** chỉ mô tả điều kiện **bổ sung bên trong màn**, luôn hiểu là đã thoả điều kiện vai trò. Đừng log bug spec ở dòng này.
- Verdict Pass phải ghi kèm một câu cho 14 phiếu: **kỳ vọng gốc của đối tác (QTHT xuất được tệp) KHÁC SRS hiện hành; BA đã chốt 06/08 giữ SRS, không nới quyền** — kèm nội dung `[Lý do]` + `[Nhận định]` BA đã soạn sẵn (`phan-hoi-ba-7-diem-can-chot-2026-08-06.md:437-439`).

**Tài khoản / môi trường:**

- QTHT: `admin` / `Secret@123`. CB NV TW: `cbnv_tw_0X` / `Test@1234` (tra `input/input.md` trước khi đăng nhập).
- Account lock → fallback **1 lượt trong cùng vai trò + cùng cấp** (`cbnv_tw_02` → `_03` → `_05`), **bắt buộc ghi
  account thực dùng** trong báo cáo. Tuyệt đối không đổi vai trò/cấp.
- Ghi **env + tên bản dựng một lần đầu lô**; chỉ kiểm lại khi có triển khai mới, đổi phiên, hoặc hành vi cho
  thấy đang chạy bản khác. Pass/Reopen chỉ có hiệu lực trên env + bản dựng đã đo.
