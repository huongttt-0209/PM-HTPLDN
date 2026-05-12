# Bug Report — HĐ Tư vấn (R7.7.14 Functional)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code + Chrome DevTools MCP) |
| **Ngày** | 2026-05-12 15:55:00 |
| **Loại test** | Functional |
| **Round** | R7 |
| **Tài liệu tham chiếu** | [functional-test-report-r7-7-14-hdtv.md](../../functional/hop-dong-tv/functional-test-report-r7-7-14-hdtv.md) · [seed-checklist-r7-3-14-hdtv.md](../../seed/hop-dong-tv/seed-checklist-r7-3-14-hdtv.md) |

---

## Tổng hợp

Phát hiện **14** lỗi trong quá trình test functional HĐ Tư vấn (R7.7.14). Hiện trạng: **3 Open** (BUG-034 + BUG-037 + BUG-038 — đều Minor i18n / spec conflict) · **11 Closed** sau retest R3/R6/R7.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 14   | 1        | 7     | 2      | 4     | 0       | 11     | 3    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-HDTV-034 | Minor | P3 | Spec conflict | — | `srs-v3.5.md line 660 M-01` ("KHÔNG có menu riêng") + BA 2026-05-11 | Route /hop-dong-tv/danh-sach render standalone list page (8 records) — BA chốt không public/menu; nếu giữ thì route ẩn có guard/redirect | Open |
| BUG-HDTV-037 | Minor | P3 | UI/UX i18n | HDTV-028 | `srs-fr-14 line 369` enum + `srs-fr-04 §3.0` Quy ước UI + `srs-fr-06 Quy tắc tương tác` + NotebookLM | TVV detail tab "Lịch sử hỗ trợ" → cột "Trạng thái" trong table Hợp đồng tư vấn render raw enum `DANG_THUC_HIEN` thay vì label "Đang thực hiện" (i18n missing) | Open |
| BUG-HDTV-038 | Minor | P3 | UI/UX i18n | HDTV-028 | `srs-fr-14 line 262` + SCR-II-01/SCR-V.I-01/SCR-III-01 pagination text + NotebookLM | TVV detail tab "Lịch sử hỗ trợ" → pagination text dùng từ "mặt hàng" thay vì "kết quả"/"mục" (e-commerce template leak) | Open |
| ~~BUG-HDTV-032~~ | ~~Medium~~ | P2 | UI/UX | HDTV-014 | `srs-v3/srs-fr-14-hop-dong-tv.md line 241` ("tab Lich su -> HD") | ~~TVV detail tab "Lịch sử hỗ trợ" thiếu sub-section HĐ tư vấn theo spec v2.1~~ | Closed ✅ R7 |
| ~~BUG-HDTV-020~~ | ~~Medium~~ | P2 | UI/UX | HDTV-020 | `FR-X.3-01 §2 BR-AUD-HDTV-01` | ~~HD detail thiếu tab "Nhật ký" trên UI (BE audit-logs API ✅ fix R3)~~ | Closed ✅ R6 |
| ~~BUG-HDTV-030~~ | ~~Major~~ | P1 | UI/Data | HDTV-029 (regression) | `BR-VAL-SYS-pagination` | ~~FE Form Tạo HD truyền `pageSize=200` vượt BE max 100 → 422, dropdown TVV/CG empty trên UI~~ | Closed ✅ R6 |
| ~~BUG-HDTV-031~~ | ~~Major~~ | P1 | API contract | HDTV-013, HDTV-026 | `srs-fr-14 §3 SCR-X3-01 line 264` | ~~VV detail tab "HĐ tư vấn liên kết" empty do FE/BE param case mismatch (camelCase vs snake_case)~~ | Closed ✅ R6 |
| ~~BUG-HDTV-033~~ | ~~Major~~ | P1 | UI/UX | HDTV-013, HDTV-029, HDTV-031 | `srs-v3/srs-fr-14-hop-dong-tv.md line 241` | ~~VV detail accordion thiếu button [+Tạo/Liên kết HĐ] + HDTV detail thiếu button Sửa/Xóa~~ | Closed ✅ R6 |
| ~~BUG-HDTV-035~~ | ~~Minor~~ | P3 | UI/UX | HDTV-014 | `SCR-X3-01 line 248` + UX validation | ~~Filter Từ ngày/Đến ngày: typing reversed range → FE silently drop Đến ngày trên submit~~ | Closed ✅ R6 |
| ~~BUG-HDTV-036~~ | ~~Major~~ | P1 | Permission | HDTV-024 | `srs-fr-14 §SCR-X3-01 line 261` + `srs-v3.5.md line 660 M-01` + `BR-AUTH-HDTV-01` | ~~CB_NV_BN_07 + CB_NV_DP_07 có button "+ Tạo hợp đồng" trên `/hop-dong-tv/danh-sach`, QTHT_07 không có (permission inversion)~~ | Closed ✅ R6 |
| ~~BUG-HDTV-018~~ | ~~Major~~ | P1 | UI/UX + Data | HDTV-018 | `FR-X.3-01 §2 BR-VAL-HDTV-04` | ~~Form Edit thiếu toggle "Đã thanh toán" + PATCH HD silently drop nested thanhToans → không update được tiến độ TT~~ | Closed ✅ R3 |
| ~~BUG-HDTV-021~~ | ~~Critical~~ | P0 | Permission | HDTV-021 | `FR-X.3-01 §2 BR-AUTH-HDTV-01` | ~~QTHT bypass cả POST/PATCH/DELETE: POST→201, PATCH→200, DELETE→204. Vi phạm phân quyền nghiêm trọng.~~ | Closed ✅ R3 |
| ~~BUG-HDTV-026~~ | ~~Major~~ | P0 | Data | HDTV-026, HDTV-019 | `FR-X.3-01 §2 N:N relation HD↔VV` | ~~PATCH `vuViecIds` trả 200 nhưng không persist~~ | Closed ✅ R3 |
| ~~BUG-HDTV-029~~ | ~~Major~~ | P1 | UI/UX | HDTV-029, HDTV-031 | `FR-X.3-01 §2 BR-DROP-HDTV-01/02 + entity §3.4.3.13 CHECK constraint` | ~~Form Tạo/Sửa HD thiếu dropdown TVV và CG~~ | Closed ✅ R3 |

---

## BUG-HDTV-034 — Standalone list page `/hop-dong-tv/danh-sach` tồn tại nhưng spec v2.1 nói "KHÔNG có menu riêng" (spec conflict)

> **Re-verify #8 2026-05-12 15:55:00 R19 — ❌ STILL Open Minor.** Account `cb_nv_tw_06` navigate `/hop-dong-tv/danh-sach` → render UI standalone list 9 rows HDTV với breadcrumb đầy đủ, no route guard / no `/403`. Dev FE chưa add guard/redirect theo BA chốt 2026-05-11. Status giữ Open.


### Mô tả

Per spec `srs-update-2026-5-5/srs-v3.5.md line 106 + 440 + 660`: "Quản lý HĐ tư vấn — **KHÔNG có menu riêng** (SRS v2.1). Truy cập qua tab VV/TVV." Sidebar 13 menu items (cấp 1 + cấp 2 dưới "Mạng lưới Tư vấn viên" và "Quản lý tư vấn") đúng spec không hiển menu HDTV. **NHƯNG** route URL trực tiếp `/hop-dong-tv` redirect tới `/hop-dong-tv/danh-sach` **render full standalone list page** (6 HDTV records visible với pagination, search, filter, tab filter trạng thái). Spec conflict — có thể là legacy route từ trước v2.1 chưa cleanup.

### Các bước tái hiện

**Precondition:** Tài khoản role QTHT (`qtht_07` primary). Bug là về **route guard URL** — bản chất chỉ test được bằng cách so sánh "menu/tab không có path → URL standalone vẫn live". Bước 1-4 verify UI click thuần (không có entry HDTV ở menu/tab), bước 5-6 test route guard (so sánh module HDTV với module TVV).

1. **Login UI:** Mở browser → vào `http://103.172.236.130:3000/login` → fill form (username `qtht_07`, password `Secret@123`) → click [Đăng nhập] → nhập OTP `666666` (MailHog) → click [Xác nhận] → vào dashboard.
2. **Verify sidebar:** Click expand 4 menu group có expandable arrow (Quản lý đào tạo / Mạng lưới Tư vấn viên / Quản lý tư vấn / Quản trị hệ thống) → đếm tổng 30 menu items → **KHÔNG có entry "Hợp đồng tư vấn"** ở bất kỳ cấp nào (đúng spec v3.5 line 660 "KHÔNG có menu riêng").
3. **Verify VV detail không link ra HDTV danh sách:** Click menu "Quản lý vụ việc hỗ trợ pháp lý" → click 1 row VV bất kỳ → trong VV detail, click expand panel "HĐ tư vấn liên kết" → table render **nested trong VV detail**, KHÔNG có button "Xem danh sách HDTV" hay link nào dẫn ra route standalone.
4. **Verify TVV detail không có tab HDTV:** Click menu "Mạng lưới Tư vấn viên" → "Tư vấn viên / Chuyên gia" → click 1 row TVV bất kỳ → trong TVV detail, quan sát 5 tab (Hồ sơ / Thẩm định / Năng lực / Lịch sử hỗ trợ / Đánh giá) — **KHÔNG có tab HDTV** (đúng spec).
5. **Test route guard HDTV (cốt lõi bug):** Mở tab browser mới → gõ URL `http://103.172.236.130:3000/hop-dong-tv/danh-sach` vào address bar → Enter → **page render full** với heading "Hợp đồng tư vấn" + breadcrumb "Trang chủ / Hợp đồng tư vấn / Danh sách" + filter (Từ khóa / TVV / Từ ngày / Đến ngày) + tab 5 trạng thái + table 10 columns + 8 record + pagination → ❌ SAI SPEC.
6. **So sánh control với module TVV:** Mở tab browser khác → gõ URL `http://103.172.236.130:3000/tu-van-vien/danh-sach` → Enter → page trả **404 "Trang bạn tìm kiếm không tồn tại"** → ✅ TVV module có route guard đúng. Chứng minh chỉ riêng HDTV thiếu guard.

### Kết quả mong đợi

- Per spec v3.5 line 660: HDTV truy cập **CHỈ** qua tab Chi tiết VV + Chi tiết TVV. Standalone list page không nằm trong spec navigation.
- Route `/hop-dong-tv/danh-sach` không được là màn hình/menu nghiệp vụ public.
- Nếu xóa route: redirect `/dashboard` hoặc 404.
- Nếu giữ route kỹ thuật: route ẩn, có guard quyền đầy đủ, tốt nhất redirect về ngữ cảnh VV/TVV hoặc chỉ dùng nội bộ admin/dev.
- Quyết định BA đã chốt ngày 2026-05-11; còn lại là Dev FE thực hiện.

### Kết quả thực tế

- Standalone list page render đầy đủ, KHÔNG có permission gate riêng (qtht_07 view được, các role khác chưa test multi-role).
- Page hoạt động đầy đủ chức năng list/filter/search nhưng đa số column row không có nút Action (xem detail OK qua URL `/hop-dong-tv/{id}`, không có button trong row).

### Bằng chứng

![BUG-HDTV-034 — Standalone list /hop-dong-tv/danh-sach render 6 records](image/r7-4-033-standalone-list-exists.png)

Sidebar verify (R4 2026-05-11): 13 menu items, KHÔNG có "Hợp đồng tư vấn" item — match spec line 660 phần "KHÔNG có menu riêng".

Submenu "Quản lý tư vấn" expand: 3 items "Tư vấn chuyên sâu / Kho câu hỏi / Tư vấn nhanh" — KHÔNG có HDTV submenu.

Submenu "Mạng lưới Tư vấn viên" expand: 3 items "Tư vấn viên / Chuyên gia / Tổ chức tư vấn / Người hỗ trợ pháp lý" — KHÔNG có HDTV submenu.

→ Sidebar đúng spec, nhưng route URL `/hop-dong-tv/danh-sach` không match spec. Cần BA quyết định cuối cùng.

---

## BUG-HDTV-037 — TVV detail tab "Lịch sử hỗ trợ" → table "Hợp đồng tư vấn" hiển thị raw enum `DANG_THUC_HIEN` thay vì label "Đang thực hiện" (i18n missing)

### Mô tả

Sau khi BUG-032 fix (TVV detail có sub-section HD trong tab Lịch sử hỗ trợ), cột "Trạng thái" trong table này render **raw enum DB** `DANG_THUC_HIEN` thay vì label tiếng Việt "Đang thực hiện". Cùng entity HD, page detail `/hop-dong-tv/{id}` hiển thị đúng "Đang thực hiện" → inconsistency i18n giữa 2 nơi cùng app. Vi phạm convention i18n nhất quán toàn dự án (SRS FR-04 §3.0 + FR-06 nói "KHÔNG hiển thị mã enum DB cho người dùng cuối").

### Các bước tái hiện

1. Login `cb_nv_tw_07` (Secret@123, OTP 666666) → dashboard.
2. Navigate `/chuyen-gia-tvv/978354d7-feac-4330-a750-6b8c07b46c24` (TVV-BTP-TW-0035 đã có ≥1 HD link).
3. Click tab "Lịch sử hỗ trợ".
4. Scroll xuống section "Hợp đồng tư vấn" (heading level 5).
5. Quan sát cột "Trạng thái" của row HD: hiển thị `DANG_THUC_HIEN` (raw uppercase enum).
6. Đối chiếu: navigate `/hop-dong-tv/{id}` (cùng HD record) → trang detail hiển thị "Đang thực hiện" (label tiếng Việt).

### Kết quả mong đợi

Per `srs-v3/srs-fr-14-hop-dong-tv.md line 369` enum: `'DANG_THUC_HIEN','HOAN_THANH','HUY','TAM_DUNG'` chỉ là giá trị DB.

Per `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md §3.0` (Quy ước UI Nhóm IV — TVV/CG): *"Mọi badge/tag trạng thái trong section này phải hiển thị **label tiếng Việt thuần** theo bảng dưới đây. KHÔNG hiển thị mã enum DB cho người dùng cuối"*.

Per `srs-update-2026-5-5/srs-fr-06-chi-tra.md` Quy tắc tương tác: *"Tất cả label, button, badge, radio, message hiển thị bằng tiếng Việt chuẩn (không viết tắt, không dùng enum/field code như DANG_KIEM_TRA). Enum chỉ dùng làm giá trị nội bộ — khi hiển thị phải map sang nhãn Việt tương ứng"*.

Per `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md line 1052`: HDTV statuses canonical Vietnamese form là "Đang thực hiện / Hoàn thành / Hủy / Tạm dừng".

NotebookLM HTPLDN xác nhận: "**UI BẮT BUỘC phải render label tiếng Việt chuẩn (ví dụ: 'Đang thực hiện'), tuyệt đối KHÔNG được phép render raw enum DB như `DANG_THUC_HIEN` cho người dùng cuối xem.**" — match SRS local.

→ Map enum → label: `DANG_THUC_HIEN` → "Đang thực hiện", `HOAN_THANH` → "Hoàn thành", `HUY` → "Hủy", `TAM_DUNG` → "Tạm dừng".

### Kết quả thực tế

Table "Hợp đồng tư vấn" trong TVV-BTP-TW-0035 → tab Lịch sử hỗ trợ render 2 row (HDTV-20260512-0001 + HDTV-20260510-0001) — cả 2 row đều có cột "Trạng thái" = `DANG_THUC_HIEN` (raw enum, uppercase, có dấu underscore). KHÔNG có badge color, KHÔNG có label mapping.

Network log: `GET /api/v1/hop-dong-tu-vans?tuVanVienId=978354d7-...&page=1&pageSize=20` → 200 trả `trangThai: "DANG_THUC_HIEN"` (BE trả enum DB đúng — BE không lỗi). FE render thẳng giá trị API không map qua i18n dictionary.

Đối chiếu cùng entity HD ở chỗ khác:
- `/hop-dong-tv/9054a0a9-...` (HDTV detail) → status hiển thị "Đang thực hiện" ✅ (label tiếng Việt).
- `/hop-dong-tv/danh-sach` (standalone list, qtht_07) → tab "Đang thực hiện / Hoàn thành / Tạm dừng / Hủy" + cột status badge tiếng Việt ✅.
- VV detail → accordion HĐ tư vấn liên kết → cột TRẠNG THÁI hiển thị "Đang thực hiện" ✅ (verified Follow-up #7b step 3).
- TVV detail tab Lịch sử hỗ trợ → section Hợp đồng tư vấn → cột Trạng thái = `DANG_THUC_HIEN` ❌ (chỗ duy nhất render raw enum).

→ FE component cho section HD-in-TVV chưa apply i18n mapping mà các component khác đã apply.

### Bằng chứng

![BUG-HDTV-037 — Raw enum DANG_THUC_HIEN trong TVV detail HD section](image/r7-2026-05-12-hdtv-028-multi-row-tvv0035-2-rows.png)

Screenshot chụp tab Lịch sử hỗ trợ TVV-BTP-TW-0035, focus section "Hợp đồng tư vấn" — 2 row HD đều có cột "Trạng thái" = `DANG_THUC_HIEN` (raw enum).

### So sánh

| Vị trí | Hiển thị Trạng thái | i18n compliance |
|---|---|---|
| `/hop-dong-tv/{id}` detail page | "Đang thực hiện" | ✅ Đúng |
| `/hop-dong-tv/danh-sach` standalone list | Badge "Đang thực hiện" + tab tiếng Việt | ✅ Đúng |
| VV detail accordion HĐ tư vấn liên kết | "Đang thực hiện" | ✅ Đúng |
| **TVV detail tab Lịch sử hỗ trợ → section Hợp đồng tư vấn** | **`DANG_THUC_HIEN`** | **❌ Sai** |

---

## BUG-HDTV-038 — TVV detail tab "Lịch sử hỗ trợ" → pagination text dùng từ "mặt hàng" thay vì "kết quả"/"bản ghi"/"mục" (i18n e-commerce template leak)

### Mô tả

Section "Hợp đồng tư vấn" trong TVV detail (tab Lịch sử hỗ trợ) có pagination text `1-2 trên 2 mặt hàng`. Từ "mặt hàng" là thuật ngữ e-commerce (item/product) không phù hợp ngữ cảnh nghiệp vụ pháp lý — hợp đồng tư vấn không phải mặt hàng bán. SRS các module quy định pagination text chuẩn là "kết quả" / "bản ghi" / "mục". Có 2 chỗ khác trong cùng app (VV accordion HD + standalone list HDTV) dùng đúng "mục" → inconsistency.

### Các bước tái hiện

1. Login `cb_nv_tw_07` → dashboard.
2. Navigate `/chuyen-gia-tvv/978354d7-feac-4330-a750-6b8c07b46c24` (TVV có ≥2 HD link để pagination text hiển thị "X-Y trên Z").
3. Click tab "Lịch sử hỗ trợ".
4. Scroll xuống section "Hợp đồng tư vấn" (heading level 5).
5. Quan sát text pagination dưới table: `1-2 trên 2 mặt hàng`.
6. Đối chiếu: VV detail accordion HĐ tư vấn liên kết → pagination text `1-1 / 1 mục`. Standalone list HDTV → `Hiển thị X-Y / N kết quả` (theo spec).

### Kết quả mong đợi

Per `srs-v3/srs-fr-14-hop-dong-tv.md line 262` (SCR-X3-01 pagination): *"20 mục/trang"*.

Per `srs-update-2026-5-5/srs-fr-02-hoi-dap.md SCR-II-01 phân trang`: *"20 muc/trang. 'Hien thi 1-20 / {total_count} ket qua'"* — text chuẩn "kết quả".

Per `srs-update-2026-5-5/srs-fr-05-vu-viec.md SCR-V.I-01 phân trang`: *"'Hiển thị 1-20 / N kết quả'. Mặc định 20/trang"* — text chuẩn "kết quả".

Per `srs-update-2026-5-5/srs-fr-03-dao-tao.md SCR-III-01 phân trang`: *"Hiển thị 1–20 trên tổng số {tổng} bản ghi"* — text chuẩn "bản ghi".

NotebookLM HTPLDN xác nhận: *"text pagination chuẩn cho '20 mục/trang' **không sử dụng từ 'mặt hàng' (từ này thường do lỗi dịch máy của từ 'items' và không được dùng trong phần mềm nghiệp vụ này)**. Text hiển thị chuẩn xoay quanh các cụm từ chỉ 'kết quả' hoặc 'bản ghi'."*

→ Pagination text chuẩn: `Hiển thị X-Y / Z kết quả` hoặc `Hiển thị X-Y trên tổng số Z bản ghi`. Có thể chấp nhận `X-Y / Z mục` (đang dùng trong VV accordion). KHÔNG dùng "mặt hàng".

### Kết quả thực tế

Pagination dưới table HD section trong TVV detail hiển thị: `1-2 trên 2 mặt hàng`. Cùng nghiệp vụ HDTV, 3 chỗ khác:
- VV detail accordion HĐ tư vấn liên kết → `1-1 / 1 mục` ✅
- Standalone list `/hop-dong-tv/danh-sach` → `Hiển thị 1-N / X kết quả` ✅
- HDTV detail page Mốc tiến độ + Thanh toán giai đoạn — không có pagination (table inline).
- **TVV detail tab Lịch sử hỗ trợ → section Hợp đồng tư vấn → `1-2 trên 2 mặt hàng` ❌**

→ FE component pagination cho section HD-in-TVV dùng i18n string khác với các table khác (có thể copy nhầm template e-commerce default của library, vd Ant Design `Pagination` mặc định trong tiếng Anh là "items" → dịch máy "mặt hàng").

### Bằng chứng

![BUG-HDTV-038 — Pagination 'mặt hàng' trong TVV detail HD section](image/r7-2026-05-12-hdtv-028-multi-row-tvv0035-2-rows.png)

Screenshot chụp tab Lịch sử hỗ trợ TVV-BTP-TW-0035 → section "Hợp đồng tư vấn" — text pagination dưới table: `1-2 trên 2 mặt hàng`.

### So sánh

| Vị trí | Pagination text | i18n compliance |
|---|---|---|
| `/hop-dong-tv/danh-sach` standalone list | `Hiển thị X-Y / N kết quả` | ✅ Đúng spec |
| VV detail accordion HĐ tư vấn liên kết | `1-1 / 1 mục` | ✅ Acceptable |
| Các SRS module khác (Hỏi đáp/Vụ việc/Đào tạo/Chi trả/DN/Đánh giá) | `X-Y / Z kết quả` hoặc `X-Y / Z bản ghi` | ✅ Đúng spec |
| **TVV detail tab Lịch sử hỗ trợ → section Hợp đồng tư vấn** | **`1-2 trên 2 mặt hàng`** | **❌ Sai (i18n e-commerce leak)** |

---

## ~~BUG-HDTV-018~~ [CLOSED] — Form Edit HD thiếu toggle "Đã thanh toán" + BE silently drop thanhToans patch → không test được tiến độ TT 50%

> **Re-test #3 2026-05-10 21:38:00 — ✅ PASS Closed-verified.** Form Edit modal có 3 switch toggle "Đã thanh toán" cho 3 giai đoạn (uid 121_57/69/81 a11y `switch question-circle`). Click switch giai đoạn 1+2 → fill ngày dự kiến → Cập nhật → toast success → detail render Đợt 1+2 = "Đã thanh toán" với ngày 09/06+09/07. API GET trả `tienDoTt=50` (đúng công thức 50tr/100tr × 100), `thanhToans[0,1].trangThaiTt='DA_THANH_TOAN'` + ngayThanhToan populated. Version 1→4. Account `cb_nv_tw_07`. HDTV-20260510-0001 (id `9054a0a9-...`).
>
> Evidence: ![Form Edit có 3 switch toggle](image/r7-3-018-form-edit-with-switch-r3.png) ![Detail render tienDoTt 50%](image/r7-3-018-detail-tiendott-50-r3.png)

### Mô tả

CB Nghiệp vụ TW (`cb_nv_tw_01`) tạo HDTV-20260510-0009 với 3 thanhToans (30tr+20tr+50tr / 100tr giá trị). Cần mark 2 đợt đầu thành DA_THANH_TOAN để verify công thức `tienDoTt = 50%` per BR-VAL-HDTV-04. Form Edit modal render 4 field per giai đoạn (Tên/Số tiền/Ngày dự kiến/Ghi chú) — KHÔNG có toggle/checkbox `trangThaiTt`. Thử PATCH API trực tiếp với `thanhToans[].trangThaiTt='DA_THANH_TOAN'` BE trả 200 nhưng GET sau patch vẫn `CHUA_THANH_TOAN × 3`. Sub-resource endpoint `/thanh-toans/:id` trả 404.

### Các bước tái hiện

1. Login `cb_nv_tw_01` (CB_PD_TW + CB_NV_TW), OTP `666666`.
2. POST `/api/v1/hop-dong-tu-vans` body `{tenHopDong, benA, benB, giaTriHopDong:100000000, ngayBatDau:'2026-05-10', ngayKetThuc:'2026-08-10', thanhToans:[{giaiDoan:'Đợt 1', soTien:30000000, thuTu:1},{giaiDoan:'Đợt 2', soTien:20000000, thuTu:2},{giaiDoan:'Đợt 3', soTien:50000000, thuTu:3}]}` → 201 với id HD `a6006815-...`.
3. Navigate UI `/hop-dong-tv/a6006815-468c-4fcf-ace2-a4725db62ae8` → click button "Chỉnh sửa".
4. Modal mở: scroll xuống section "Thanh toán giai đoạn" — quan sát chỉ có Tên/Số tiền/Ngày/Ghi chú, không có toggle "Đã thanh toán".
5. Đóng modal. Thử PATCH `/api/v1/hop-dong-tu-vans/{id}` body `{version, thanhToans: [{...trangThaiTt:'DA_THANH_TOAN', ngayThanhToan:'2026-05-10'}, ...]}` → 200.
6. GET `/api/v1/hop-dong-tu-vans/{id}` → `tienDoTt=0`, `thanhToans[].trangThaiTt = CHUA_THANH_TOAN × 3` (không thay đổi).
7. PATCH `/api/v1/hop-dong-tu-vans/{id}/thanh-toans/{ttId}` → 404. PATCH `/api/v1/thanh-toan-hop-dongs/{ttId}` → 404. PATCH `/api/v1/thanh-toans/{ttId}` → 404.

### Kết quả mong đợi

- Per **FR-X.3-01 §2 BR-VAL-HDTV-04**: hệ thống phải auto-tính `tienDoTt = SUM(thanhToans WHERE trangThaiTt=DA_THANH_TOAN) / giaTriHopDong * 100`.
- UI Form Edit phải có cơ chế (toggle/checkbox/dropdown) để mark từng giai đoạn thanh toán → DA_THANH_TOAN + nhập ngayThanhToan.
- Hoặc API có sub-resource `/hop-dong-tu-vans/{id}/thanh-toans/{ttId}` PATCH với body `{trangThaiTt, ngayThanhToan}`.
- Sau khi 2 đợt đầu mark paid (50tr / 100tr) → GET HD trả `tienDoTt=50`.

### Kết quả thực tế

- Form Edit chỉ render 4 field per giai đoạn, không có UI để update trạng thái.
- PATCH HD whole record với `thanhToans[]` mới: BE trả 200 OK nhưng silently drop array → record không thay đổi.
- 3 path API sub-resource cho thanhToans đều 404.
- Tester KHÔNG có cách nào set HD đến `tienDoTt > 0` để verify công thức.

### Bằng chứng

![BUG-HDTV-018 — HD detail render 3 thanhToans tất cả "Chưa thanh toán" + form Edit không có toggle](image/r7-7-14-hdtv-018-detail-no-paid-toggle.jpeg)

API response sample:

```json
{
  "data": {
    "tienDoTt": 0,
    "thanhToans": [
      {"thuTu":1, "soTien":30000000, "trangThaiTt":"CHUA_THANH_TOAN", "ngayThanhToan":null},
      {"thuTu":2, "soTien":20000000, "trangThaiTt":"CHUA_THANH_TOAN", "ngayThanhToan":null},
      {"thuTu":3, "soTien":50000000, "trangThaiTt":"CHUA_THANH_TOAN", "ngayThanhToan":null}
    ]
  }
}
```

PATCH attempt response:

```json
{ "patchStatus": 200, "afterStatuses": ["CHUA_THANH_TOAN","CHUA_THANH_TOAN","CHUA_THANH_TOAN"] }
```

---

## ~~BUG-HDTV-020~~ [CLOSED] — HD detail thiếu tab "Nhật ký" + endpoint audit log không tồn tại (BR-AUD-HDTV-01)

> **Re-test #6 2026-05-11 16:57:00 — ✅ PASS Closed-verified.** HDTV-20260510-0001 detail page (cb_nv_tw_07 view) render section "Nhật ký hoạt động" với 6 audit log row (CREATE × 2 + UPDATE × 4). Columns: Thời gian / Hành động / Người thực hiện / Vai trò / Endpoint / HTTP. Network: `GET /api/v1/hop-dong-tu-vans/{id}/audit-logs?page=1&pageSize=10&sort=thoiGian&order=desc` → 200. UI tab thiếu giờ đã có. Evidence: ![Nhật ký HDTV detail QTHT](image/r7-reverify-hdtv-detail-qtht-nhatky.png)

### Mô tả

CB Nghiệp vụ TW navigate `/hop-dong-tv/{id}` quan sát detail page chỉ render: Header, Thông tin hợp đồng, Mốc tiến độ, Thanh toán giai đoạn, button Chỉnh sửa/Xóa. KHÔNG có tab "Nhật ký" / "Lịch sử" / "Audit log" để xem audit trail CRUD per BR-AUD-HDTV-01. Probe API: 4 sub-resource path đều 404; top-level `/audit-logs?entityType=HOP_DONG_TU_VAN` 403 cho `cb_nv_tw_01` (role có 235 perm).

### Các bước tái hiện

1. Login `cb_nv_tw_01` (235 permissions).
2. Navigate `/hop-dong-tv/a6006815-468c-4fcf-ace2-a4725db62ae8`.
3. Quan sát layout: section heading "Tiến độ thanh toán", "Thông tin hợp đồng", "Mốc tiến độ", "Thanh toán giai đoạn" — không có tab "Nhật ký".
4. Probe sub-resource API:
   - GET `/api/v1/hop-dong-tu-vans/{id}/audit-logs` → 404
   - GET `/api/v1/hop-dong-tu-vans/{id}/nhat-ky` → 404
   - GET `/api/v1/hop-dong-tu-vans/{id}/lich-su` → 404
   - GET `/api/v1/hop-dong-tu-vans/{id}/history` → 404
5. Probe top-level:
   - GET `/api/v1/audit-logs?entityType=HOP_DONG_TU_VAN&entityId={id}` → 403
   - GET `/api/v1/audit-logs?resource=hop-dong-tu-van&id={id}` → 403

### Kết quả mong đợi

- Per **FR-X.3-01 §2 BR-AUD-HDTV-01**: Mọi CRUD trên HD phải log audit trail (CREATE/UPDATE/DELETE/STATUS_CHANGE), kèm `actorId`, `timestamp`, `before/after snapshot` (hoặc tối thiểu event log).
- UI HD detail có tab "Nhật ký" hiển thị audit trail từ mới nhất → cũ.
- Hoặc UI riêng `/audit-logs?entityType=HOP_DONG_TU_VAN` cho QTHT.
- API `/hop-dong-tu-vans/{id}/audit-logs` trả 200 + array events cho CB có permission.

### Kết quả thực tế

- UI: KHÔNG có tab "Nhật ký" trong HD detail page.
- API: 4 path sub-resource 404 (endpoint chưa được implement).
- API top-level 403 (endpoint có thể tồn tại nhưng không expose cho `cb_nv_tw_01` — không clear).
- Tester KHÔNG có cách nào kiểm tra audit log của HD.

### Bằng chứng

![BUG-HDTV-020 — HD detail full page, không có tab "Nhật ký"](image/r7-7-14-hdtv-018-detail-no-paid-toggle.jpeg)

*(Cùng screenshot với BUG-HDTV-018 — vì cả 2 issue đều ở trên cùng detail page)*

API probe response:

```json
{
  "/hop-dong-tu-vans/{id}/audit-logs": 404,
  "/hop-dong-tu-vans/{id}/nhat-ky":   404,
  "/hop-dong-tu-vans/{id}/lich-su":   404,
  "/hop-dong-tu-vans/{id}/history":   404,
  "/audit-logs?entityType=HOP_DONG_TU_VAN": 403
}
```

---

## ~~BUG-HDTV-021~~ [CLOSED] — QTHT bypass cả CUD trên HD TV: POST→500, PATCH→200 (modify), DELETE→204 (hard-delete)

> **Re-test #3 2026-05-10 21:44:00 — ✅ PASS Closed-verified.** Login `qtht_07` (vai trò QTHT) trong isolated context `qa_r3_hdtv_qtht_07`. Probe 4 endpoint:
> - GET `/api/v1/hop-dong-tu-vans?pageSize=2` → 200 (đúng quyền R)
> - POST `/api/v1/hop-dong-tu-vans` body `{tenHopDong, benA, benB, giaTriHopDong, ngayBatDau, ngayKetThuc, tuVanVienId}` → **403 ERR-PERM-SYS-00-01 "Forbidden"**
> - PATCH `/api/v1/hop-dong-tu-vans/{id}` body `{version, ghiChu}` → **403 ERR-PERM-SYS-00-01 "Forbidden"**
> - DELETE `/api/v1/hop-dong-tu-vans/{id}` → **403 ERR-PERM-SYS-00-01 "Forbidden"**
>
> Permission middleware giờ block QTHT đúng spec BR-AUTH-HDTV-01 (R-only). Không còn bypass. Severity downgrade Critical → Closed.

### Mô tả

QTHT (`qtht_01`) per BR-AUTH-HDTV-01 chỉ có permission R (read) trên HD TV. Test phân quyền: GET `/api/v1/hop-dong-tu-vans` trả 200 (đúng); POST tạo HD trả **500 ERR-SYS-00-00-01 "Lỗi hệ thống, vui lòng thử lại sau"** thay vì 403; DELETE `/api/v1/hop-dong-tu-vans/{id}` trả **404 ERR-VAL-X3-159-02 "Hợp đồng tư vấn không tồn tại"** (business error, leak existence info) thay vì 403 perm error.

### Các bước tái hiện

1. Login `qtht_01` (Quản trị hệ thống) trong isolated context (Chrome DevTools MCP `isolatedContext=qtht_role`).
2. GET `/api/v1/hop-dong-tu-vans?pageSize=5` → 200 OK (đúng — quyền R).
3. POST `/api/v1/hop-dong-tu-vans` body `{tenHopDong:'qtht-test', benA:'a', benB:'b', giaTriHopDong:1000, ngayBatDau:'2026-05-10', ngayKetThuc:'2026-05-15'}` → 500 ERR-SYS-00-00-01 (sai).
4. DELETE `/api/v1/hop-dong-tu-vans/{validHdId}` (HD thật, đã verify GET thấy) → 404 ERR-VAL-X3-159-02 (sai — phải 403).

### Kết quả mong đợi

- Per **FR-X.3-01 §2 BR-AUTH-HDTV-01**: QTHT chỉ có permission R. CUD attempts phải trả `403 ERR-AUTH-PERM-01` consistent.
- POST 403 trước khi vào handler (permission middleware).
- DELETE 403 trước khi check existence (permission middleware).

### Kết quả thực tế

- POST trả `500 ERR-SYS-00-00-01` — có thể là CHECK constraint violation (`tu_van_vien_id IS NOT NULL OR to_chuc_tu_van_id IS NOT NULL`) bypass permission check vào tận BE.
- DELETE trả `404 ERR-VAL-X3-159-02 "Hợp đồng tư vấn không tồn tại"` — leak info HD tồn tại hay không (security concern); permission check không chạy trước existence check.
- Tham chiếu memory `qa_htpldn_qtht_permission_bypass` — pattern đã thấy trên TU_VAN_VIEN R14 W1, có vẻ lặp ở entity HD TV.

### Bằng chứng

API response:

```json
{
  "POST /hop-dong-tu-vans (qtht_01)": {
    "status": 500,
    "body": {"success":false,"error":{"code":"ERR-SYS-00-00-01","message":"Lỗi hệ thống, vui lòng thử lại sau","timestamp":"2026-05-10T02:27:32.600Z","requestId":"479ac42c-..."}}
  },
  "DELETE /hop-dong-tu-vans/{id} (qtht_01)": {
    "status": 404,
    "body": {"success":false,"error":{"code":"ERR-VAL-X3-159-02","message":"Hợp đồng tư vấn không tồn tại","timestamp":"2026-05-10T02:27:32.625Z","requestId":"d40f5ff6-..."}}
  }
}
```

### So sánh

| Role | GET list | POST create | DELETE |
|------|----------|-------------|--------|
| `cb_nv_tw_01` (CB_NV_TW) | ✅ 200 | ✅ 201 | ✅ 204 hoặc 403 ERR-HDTV-04 (nếu có VV link) |
| `qtht_01` (QTHT) | ✅ 200 (R quyền) | ❌ 500 (BUG! phải 403) | ❌ 404 leak (BUG! phải 403) |
| `nht_01` (NHT) | ❌ 403 | ❌ 403 (chưa test cụ thể) | ❌ 403 (chưa test) |
| `9999999990` (DN) | ❌ 403 | ❌ 403 (chưa test) | ❌ 403 (chưa test) |

---

## ~~BUG-HDTV-026~~ [CLOSED] — N:N linking VV vào HD broken: PATCH `vuViecIds` không persist + 4 sub-resource POST 404

> **Re-test #3 2026-05-10 21:46:00 — ✅ PASS Closed-verified.** PATCH HDTV-0001 (`9054a0a9-...`) body `{version: 4, tuVanVienId: "978354d7-...", vuViecIds: ["dce4c308-..." VV-BTP-TW-20260510-002]}` → 200, version bump 4→5. GET sau patch `soVuViecLienKet=0→1` (persist OK). 4 sub-resource POST path (`/vu-viecs`, `/vu-viec-links`, `/lien-ket-vu-viec`, `/links`) vẫn 404 ERR-SYS-00-04-01 — chấp nhận vì PATCH whole record là main path đã work, sub-resource là alternate optional.

### Mô tả

CB Nghiệp vụ TW tạo HD mồ côi (HDTV-20260510-0010, không link VV). Cần add VV-BTP-TW-20260509-009 (Lao động) vào HD qua API để verify N:N relation per spec FR-X.3-01 §2. PATCH `/api/v1/hop-dong-tu-vans/{id}` body `{version, vuViecIds:[vvId]}` trả 200 OK nhưng GET sau patch `soVuViecLienKet` vẫn `0`. Thử 4 path sub-resource POST đều 404 (`/vu-viecs`, `/vu-viec-links`, `/lien-ket-vu-viec`, `/links`).

### Các bước tái hiện

1. Login `cb_nv_tw_01`.
2. POST tạo HDTV-0010 mồ côi (no `vuViecIds` trong body) → 201, `soVuViecLienKet=0`.
3. GET `/api/v1/vu-viecs?pageSize=30` → tìm VV-BTP-TW-20260509-009 (Lao động) id `765920aa-43e4-...`.
4. GET `/api/v1/hop-dong-tu-vans/{hdId}` → lấy `version` field.
5. PATCH `/api/v1/hop-dong-tu-vans/{hdId}` body `{version, vuViecIds:[vvId]}` → 200 OK.
6. GET `/api/v1/hop-dong-tu-vans/{hdId}` lại → `soVuViecLienKet=0` (KHÔNG đổi).
7. POST `/api/v1/hop-dong-tu-vans/{hdId}/vu-viecs` body `{vuViecId}` → 404.
8. POST `/api/v1/hop-dong-tu-vans/{hdId}/vu-viec-links` → 404.
9. POST `/api/v1/hop-dong-tu-vans/{hdId}/lien-ket-vu-viec` → 404.
10. POST `/api/v1/hop-dong-tu-vans/{hdId}/links` → 404.

### Kết quả mong đợi

- Per **FR-X.3-01 §2** N:N relation: HD và VV có quan hệ N:N (1 HD link nhiều VV; 1 VV có thể link nhiều HD).
- POST tạo HD với `vuViecIds: [vvId, vvId2]` đã work trong seed (HDTV-0003..0008 cover 6 LV với `soVvLink=1`).
- PATCH HD đã tồn tại với `vuViecIds: [vvId]` phải persist + tăng `soVuViecLienKet`.
- Hoặc có sub-resource endpoint `POST /hop-dong-tu-vans/{id}/vu-viecs` body `{vuViecId}` để add từng link.

### Kết quả thực tế

- PATCH với `vuViecIds` trong body: BE trả 200 nhưng silently drop array — không có error message, không có state change.
- 4 path sub-resource POST đều 404 → endpoint chưa implement.
- Tester chỉ có thể link VV vào HD tại thời điểm POST tạo HD; sau đó không có cách nào add/remove VV link.

### Bằng chứng

API response:

```json
{
  "PATCH /hop-dong-tu-vans/{id}": {
    "request_body": { "version": 1, "vuViecIds": ["765920aa-43e4-47c0-a8ce-bf6e9c24e53e"] },
    "response_status": 200,
    "after_get_soVuViecLienKet": 0
  },
  "POST /hop-dong-tu-vans/{id}/vu-viecs":          404,
  "POST /hop-dong-tu-vans/{id}/vu-viec-links":     404,
  "POST /hop-dong-tu-vans/{id}/lien-ket-vu-viec":  404,
  "POST /hop-dong-tu-vans/{id}/links":             404
}
```

---

## ~~BUG-HDTV-029~~ [CLOSED] — Form Tạo/Sửa HD thiếu dropdown TVV (`tu_van_vien_id`) + CG (`to_chuc_tu_van_id`) — vi phạm CHECK constraint entity §3.4.3.13

> **Re-test #3 2026-05-10 21:48:00 — ✅ PASS Closed-verified.** Form Tạo HD `/hop-dong-tv/tao-moi` + Form Edit modal đều đã có:
> - **Radio "Loại chủ thể thực hiện"** (segmented control): "Cá nhân (TVV/CG)" (mặc định checked) vs "Tổ chức (TCTV)"
> - **Combobox required "Tư vấn viên / Chuyên gia"** với placeholder "Chọn tư vấn viên hoặc chuyên gia" — uid 126_65 trong form Tạo
> - CHECK constraint enforced ở BE: POST không kèm `tuVanVienId`/`toChucTuVanId` → 400 **ERR-HDTV-CHU-THE-01 "Hợp đồng phải gán Tư vấn viên hoặc Tổ chức tư vấn"**
>
> Bug gốc về thiếu dropdown đã fix. **Phát hiện regression mới: dropdown options KHÔNG load** do FE call `pageSize=200` vượt BE max 100 → log riêng tại BUG-HDTV-030.

### Mô tả

Form modal "Tạo hợp đồng tư vấn" (mở từ VV detail accordion "HĐ tư vấn liên kết" → button "Tạo hợp đồng") render 12 field: Tên/Vụ việc liên kết (auto-fill disabled)/Số HD/Bên A/Bên B/Giá trị/Trạng thái/Thời gian/Ngày ký/Mốc tiến độ/Thanh toán/Hủy-Tạo. KHÔNG có dropdown picker cho TVV (`tu_van_vien_id`) hoặc CG (`to_chuc_tu_van_id`). Form Sửa cũng tương tự. Spec entity HOP_DONG_TU_VAN §3.4.3.13 có column `tu_van_vien_id` UUID NULL (verified GET API trả `tuVanVienId` trong allKeys); CHECK constraint yêu cầu `tu_van_vien_id IS NOT NULL OR to_chuc_tu_van_id IS NOT NULL` để HD có entity tư vấn cụ thể.

### Các bước tái hiện

1. Login `cb_nv_tw_01`.
2. Navigate `/vu-viec/{vvId}` (VV detail của VV-BTP-TW-20260509-001 Lao động).
3. Cuộn xuống section "HĐ tư vấn liên kết" → click button "Tạo hợp đồng" → modal mở.
4. Quan sát 12 field trong form: không có select/combobox cho "Tư vấn viên" hoặc "Tổ chức tư vấn".
5. Đóng modal. Mở 1 HD đã tồn tại (vd HDTV-0009) → click "Chỉnh sửa" → modal Cập nhật cùng layout, cũng không có dropdown TVV/CG.
6. Verify entity field qua API: GET `/api/v1/hop-dong-tu-vans/{id}` → response có key `tuVanVienId` (giá trị `null` cho mọi HD seed via API direct vì BE chưa enforce CHECK constraint).

### Kết quả mong đợi

- Per **FR-X.3-01 §2 + entity §3.4.3.13 CHECK**: Form Tạo/Sửa HD phải có dropdown picker cho phép chọn 1 trong 2:
  - **TVV picker** (filter `loaiTvv=TU_VAN_VIEN, trangThai=HOAT_DONG`) — per BR-DROP-HDTV-01.
  - **CG picker** (filter `loaiTvv=CHUYEN_GIA, trangThai=HOAT_DONG`) — per BR-DROP-HDTV-02. *(Spec gốc dùng chung field `loaiTvv` cho TU_VAN_VIEN/CHUYEN_GIA hoặc 2 entity riêng — cần BA confirm)*.
  - Hoặc **TCTV picker** (`to_chuc_tu_van_id`) — chọn tổ chức tư vấn pháp luật.
- Submit không thoả CHECK → form hiển thị error inline.

### Kết quả thực tế

- Form chỉ có "Bên B" textbox tự do — user nhập chuỗi text bất kỳ ("DN test", "Test BR-VAL-HDTV-04 progress" v.v.) làm `benB` field, không liên kết entity.
- BE accept POST với `tuVanVienId=null + toChucTuVanId=null` (CHECK constraint không enforce hoặc field optional contrary spec).
- Cascade impact: HDTV-029/031 (test dropdown filter HOAT_DONG) không thực hiện được vì không có dropdown để filter.

### Bằng chứng

![BUG-HDTV-029 — Form Tạo HD modal post-fix, có Vụ việc liên kết auto-fill nhưng KHÔNG có TVV/CG picker](image/r7-3-14-create-form-postfix-vv-field.jpeg)

API response sample (GET HD chỉ ra schema có `tuVanVienId` key):

```json
{
  "data": {
    "id": "...",
    "maHopDong": "HDTV-20260510-0008",
    "tuVanVienId": null,
    "benA": "Bộ Tư pháp - Cục Bổ trợ tư pháp",
    "benB": "Công ty Cổ phần Phúc An AG",
    "..."
  }
}
```

---

## ~~BUG-HDTV-030~~ [CLOSED] — FE Form Tạo HD truyền `pageSize=200` vượt BE max 100 → dropdown TVV/CG empty trên UI

> **Re-test #6 2026-05-11 16:59:00 — ✅ PASS Closed-verified.** Mở Edit form HDTV-20260510-0001 (cb_nv_tw_07) → click combobox "Tư vấn viên / Chuyên gia". Network: `GET /api/v1/tu-van-viens?trangThai=HOAT_DONG&pageSize=100` → **200 OK** (đúng max 100). Tương tự `/to-chuc-tu-vans?pageSize=100` → 200. Dropdown render 8 TVV options đầy đủ. FE đã đổi pageSize 200 → 100. Evidence: ![Edit form dropdown TVV](image/r7-reverify-bug-030-edit-form-dropdown.png)

### Mô tả

CB Nghiệp vụ TW (`cb_nv_tw_07`) navigate `/hop-dong-tv/tao-moi`. Modal "Tạo hợp đồng tư vấn" mở. Click combobox "Tư vấn viên / Chuyên gia" → dropdown ant-select-dropdown render class `ant-select-dropdown-empty`, 0 option. Inspect Network: FE thực hiện 2 GET liền tiếp `/api/v1/tu-van-viens?trangThai=HOAT_DONG&pageSize=200` và `/api/v1/to-chuc-tu-vans?trangThai=HOAT_DONG&pageSize=200` — cả 2 đều **422 ERR-VAL-SYS-00-01** "pageSize must not be greater than 100". Do response 422, FE không có data populate dropdown → user UI thuần KHÔNG chọn được TVV/CG → form submit fail.

### Các bước tái hiện

1. Login `cb_nv_tw_07` (CB_NV_TW), OTP `666666`.
2. Navigate `/hop-dong-tv/tao-moi`.
3. Modal "Tạo hợp đồng tư vấn" mở; "Loại chủ thể" mặc định "Cá nhân (TVV/CG)".
4. Click combobox "Tư vấn viên / Chuyên gia".
5. Quan sát dropdown render empty (`.ant-select-dropdown-empty`).
6. Mở DevTools Network: 2 request fail `pageSize=200 → 422`.
7. Đổi radio sang "Tổ chức (TCTV)" → kết quả tương tự `/to-chuc-tu-vans?pageSize=200 → 422`.

### Kết quả mong đợi

- Per **BR-VAL-SYS-pagination** (BE convention chung): mọi pagination request `pageSize ≤ 100`.
- FE phải truyền `pageSize ≤ 100` (hoặc dùng pagination + lazy load) để fetch danh sách TVV/CG.
- Dropdown render đầy đủ option active để user chọn.

### Kết quả thực tế

- FE hard-code `pageSize=200` trong fetch dropdown TVV/CG → BE return 422.
- Dropdown empty → user không submit được form qua UI thuần.
- API direct POST `/hop-dong-tu-vans` với `tuVanVienId` lấy từ list khác vẫn work, nhưng đó không phải user flow.

### Bằng chứng

![BUG-HDTV-030 — Form Tạo HD dropdown TVV empty do pageSize=200 → 422](image/r7-3-029-create-form-pagesize422-r3.png)

Network response (reqid 600):

```json
{
  "url": "/api/v1/tu-van-viens?trangThai=HOAT_DONG&pageSize=200",
  "status": 422,
  "body": {
    "success": false,
    "error": {
      "code": "ERR-VAL-SYS-00-01",
      "field": "pageSize",
      "message": "pageSize must not be greater than 100",
      "details": [{"field":"pageSize","message":"pageSize must not be greater than 100"}],
      "timestamp": "2026-05-10T14:43:54.579Z",
      "requestId": "5145b62c-..."
    }
  }
}
```

---

## ~~BUG-HDTV-031~~ [CLOSED] — VV detail tab "HĐ tư vấn liên kết" empty do FE/BE param case mismatch (camelCase vs snake_case)

> **Re-test #6 2026-05-11 17:01:00 — ✅ PASS Closed-verified.** VV detail accordion "HĐ tư vấn liên kết" expand (cb_nv_tw_07, VV-QA-R7-LIFECYCLE-HT) → render table 10 columns đầy đủ (MÃ HỢP ĐỒNG / TÊN / BÊN A / BÊN B / GIÁ TRỊ / NGÀY BẮT ĐẦU / NGÀY KẾT THÚC / VỤ VIỆC / TIẾN ĐỘ TT / TRẠNG THÁI) + heading "Hợp đồng tư vấn liên kết" + button [+ Tạo hợp đồng]. VV này chưa link HD → empty state "Vụ việc này chưa có hợp đồng tư vấn liên kết." (đúng behavior). FE/BE contract giờ thống nhất param case.

### Mô tả

QTHT (`qtht_07`) mở chi tiết VV-BTP-TW-20260510-001 (id `9cc24b55-7c6b-4faa-8051-9a2b0db86cb5`) — đây là VV đã được link với HDTV-20260510-0001 (counter `soVuViecLienKet=1`, đã verify R3). Expand accordion "HĐ tư vấn liên kết" trong VV detail → render empty "Vụ việc này chưa có hợp đồng tư vấn liên kết." mặc dù link tồn tại. Network log cho thấy FE gọi `GET /api/v1/hop-dong-tu-vans?vuViecId=9cc24b55-...&page=1&pageSize=20` (param camelCase) trả 200 + total=0. BE thực tế accept param `vu_viec_id=` (snake_case) → cùng UUID trả total=1.

### Các bước tái hiện

1. Login `qtht_07` (Secret@123, OTP 666666).
2. Sidebar → "Quản lý vụ việc hỗ trợ pháp lý".
3. Click VV-BTP-TW-20260510-001 (row first hoặc id `9cc24b55-7c6b-4faa-8051-9a2b0db86cb5`).
4. Scroll xuống → click accordion "HĐ tư vấn liên kết" để expand.
5. Quan sát table render columns đầy đủ (MÃ HỢP ĐỒNG, TÊN HỢP ĐỒNG, BÊN A, BÊN B, GIÁ TRỊ, NGÀY BẮT ĐẦU, NGÀY KẾT THÚC, VỤ VIỆC, TIẾN ĐỘ TT, TRẠNG THÁI) nhưng row trống + thông báo "Vụ việc này chưa có hợp đồng tư vấn liên kết."
6. Mở DevTools Network → xem request `/api/v1/hop-dong-tu-vans?vuViecId=...` trả `{total:0, items:[]}`.

### Kết quả mong đợi

- Per `srs-v3/srs-fr-14-hop-dong-tv.md line 241` ("Truy cap tu (1) Chi tiet Vu viec MH-05.3 -> tab/section 'HD tu van lien ket'") + counter `soVuViecLienKet=1` đã verify R3 — accordion phải render 1 row HDTV-20260510-0001 với đầy đủ thông tin và link để mở detail.
- FE/BE contract param tên thống nhất (cùng camelCase hoặc cùng snake_case).

### Kết quả thực tế

- Accordion render empty state mặc dù counter HDTV side đã tăng.
- FE gọi `?vuViecId=` (camelCase) — BE ignore param không nhận biết → trả tất cả HDTV trong scope (filter by user nếu có), không filter theo VV ID.
- BE chỉ accept `?vu_viec_id=` (snake_case) — đã verify R3 cùng UUID trả total=1 record.

### Bằng chứng

![BUG-HDTV-031 — VV detail accordion HD empty + network log camelCase param](image/r7-4-031-vv-detail-hdtv-tab-empty.png)

Network log evidence:
```
reqid=555 GET /api/v1/hop-dong-tu-vans?vuViecId=9cc24b55-7c6b-4faa-8051-9a2b0db86cb5&page=1&pageSize=20 [200]
→ {"total":0, "items":[]}
```

vs param đúng (snake_case) trả result:
```
GET /api/v1/hop-dong-tu-vans?vu_viec_id=9cc24b55-7c6b-4faa-8051-9a2b0db86cb5&page=1&pageSize=20 [200]
→ {"total":1, "items":[{"id":"9054a0a9-...", "maHopDong":"HDTV-20260510-0001", ...}]}
```

---

## ~~BUG-HDTV-032~~ [CLOSED] — TVV detail tab "Lịch sử hỗ trợ" thiếu sub-section HĐ tư vấn theo spec v2.1

> **Re-verify #7 2026-05-12 02:00:00 — ✅ PASS Closed-verified.** TVV-BTP-TW-0035 (id `978354d7-...`) detail tab "Lịch sử hỗ trợ" giờ render đủ 2 section: (1) table VV với 9 columns (empty, đúng vì TVV chưa tham gia VV trực tiếp) + (2) heading "Hợp đồng tư vấn" level 5 + table 5 columns (Mã HĐ / Tên hợp đồng / Trạng thái / Ngày bắt đầu / Ngày kết thúc) + 1 row HDTV-20260510-0001 (DANG_THUC_HIEN, 09/05/2026 → 09/08/2026) với link `<a>` clickable mở HDTV detail + pagination "1-1 trên 1 mặt hàng". Network log (qtht_07): reqid 415 `GET /api/v1/hop-dong-tu-vans?tuVanVienId=978354d7-feac-4330-a750-6b8c07b46c24&page=1&pageSize=20` → 200 (NEW endpoint call song song với `/lich-su-ho-tro` cũ). FE giờ implement HD section đúng spec v3 line 241. Evidence: ![BUG-032 PASS](image/r7-reverify-2026-05-12-bug-032-tvv-history-with-hd-section-passed.png)
>

### Mô tả

QTHT (`qtht_07`) mở chi tiết TVV-BTP-TW-0035 (id `978354d7-feac-4330-a750-6b8c07b46c24`) — TVV ký HDTV-20260510-0001. UI render 5 tab: "Hồ sơ" (selected), "Thẩm định" (disabled), "Năng lực", "Lịch sử hỗ trợ", "Đánh giá". Click "Lịch sử hỗ trợ" → render table list VV với columns "Mã vụ việc / Tên vụ việc / Doanh nghiệp / Lĩnh vực / Vai trò / Ngày phân công / Ngày hoàn thành / Kết quả / Đánh giá". **KHÔNG có sub-section/sub-tab "HĐ tư vấn"** theo spec v3 line 241.

### Các bước tái hiện

1. Login `qtht_07`, OTP 666666.
2. Sidebar → "Mạng lưới Tư vấn viên" → "Tư vấn viên / Chuyên gia".
3. Tab "Đang hoạt động" → click "Xem" trên row TVV-BTP-TW-0035 (TVV R13 A19 Gate Verify).
4. Trang detail mở với 5 tab. Click tab "Lịch sử hỗ trợ".
5. Quan sát chỉ có table 1 list VV. KHÔNG có sub-tab/sub-section "HĐ tư vấn" hoặc dropdown filter "Loại lịch sử: VV / HĐ".

### Kết quả mong đợi

- Per `srs-v3/srs-fr-14-hop-dong-tv.md line 241`: "Truy cap tu (2) Chi tiet TVV MH-04.3 -> tab 'Lich su' -> HD."
- Tab "Lịch sử hỗ trợ" phải có 2 sub-section: VV (đang có) + HD (đang thiếu); hoặc 2 sub-tab; hoặc dropdown filter cho phép xem riêng HD.
- TVV-BTP-TW-0035 có 1 HDTV (HDTV-20260510-0001) → sub-section HD phải render row này.

### Kết quả thực tế

- Tab "Lịch sử hỗ trợ" chỉ render table VV (currently 0 records do TVV này chưa tham gia VV nào trực tiếp dù ký HDTV).
- KHÔNG có UI element nào hiển thị HD liên kết với TVV này.
- → User UI thuần KHÔNG biết TVV này có HD nào nếu đi từ TVV detail.

### Bằng chứng

Snapshot UI tab "Lịch sử hỗ trợ" — tabpanel chỉ có columns VV-centric, không có columns HD. (Screenshot pending — `image/r7-4-032-tvv-history-no-hd-section.png` — tester có thể chụp lại từ URL `http://103.172.236.130:3000/chuyen-gia-tvv/978354d7-feac-4330-a750-6b8c07b46c24` tab Lịch sử hỗ trợ).

---

## ~~BUG-HDTV-033~~ [CLOSED] — Thiếu button Create/Edit + modal/drawer entry point per spec v2.1 (UI implementation gap)

> **Re-test #6 2026-05-11 17:03:00 — ✅ PASS Closed-verified.** Phần A: VV detail accordion "HĐ tư vấn liên kết" có button **[+ Tạo hợp đồng]** ngay cạnh heading. Phần B: HDTV-20260510-0001 detail page (cb_nv_tw_07 view) render 2 button cuối page: **"Chỉnh sửa"** (uid 194_156) + **"Xóa"** (uid 194_157). UI entry point Create/Edit/Delete đã đầy đủ qua VV accordion + HDTV detail (cho role có quyền CUD).

### Mô tả

Per spec `srs-v3/srs-fr-14-hop-dong-tv.md line 241`: "Noi dung MH-14.1 ben duoi giu lai de tham chieu element-level — **implement dang modal/drawer khi truy cap tu VV/TVV**." UI hiện tại VV detail accordion "HĐ tư vấn liên kết" CHỈ có table read-only + empty state — **KHÔNG có button [+ Tạo HĐ TV]** hay **[+ Liên kết HĐ]**. HDTV detail standalone (`/hop-dong-tv/{id}`) cũng **KHÔNG có button "Sửa"** / **"Xóa"** (chỉ có button "Quay lại danh sách"). Test URL Create direct (`/hop-dong-tv/new`, `/hop-dong-tv/tao`, `/hop-dong-tv/them-moi`) đều trả "Không tìm thấy hợp đồng tư vấn." (FE treat as ID lookup → 404). URL Edit direct (`/hop-dong-tv/{id}/sua`) redirect về `/danh-sach`. **→ Hệ thống KHÔNG có entry point UI nào để user UI thuần Create / Edit / Xóa HDTV** — chỉ truy cập được qua API direct (POST/PATCH/DELETE).

### Các bước tái hiện

**Phần A — VV detail accordion thiếu button:**

1. Login `qtht_07` (hoặc `cb_nv_tw_07`).
2. Sidebar → Quản lý VV → click VV bất kỳ (vd VV-BTP-TW-20260510-001).
3. Expand accordion "HĐ tư vấn liên kết".
4. Quan sát: chỉ có table read-only + empty state. KHÔNG có button [+ Tạo HĐ], [+ Liên kết HĐ], [Thêm HĐ tư vấn].

**Phần B — HDTV detail thiếu button:**

1. Navigate `/hop-dong-tv/9054a0a9-3139-42e3-b817-e7d8a0edb4b2` (HDTV-20260510-0001).
2. Detail page render: button duy nhất là "Quay lại danh sách". KHÔNG có "Sửa" / "Xóa" / "Liên kết VV" buttons. KHÔNG có Hành động column trong sub-table thanhToans.

**Phần C — URL Create routes đều fail:**

1. `/hop-dong-tv/new` → "Không tìm thấy hợp đồng tư vấn." (treat "new" as ID)
2. `/hop-dong-tv/tao` → "Không tìm thấy hợp đồng tư vấn."
3. `/hop-dong-tv/them-moi` → "Không tìm thấy hợp đồng tư vấn."
4. `/hop-dong-tv/{id}/sua` → redirect `/hop-dong-tv/danh-sach`.

### Kết quả mong đợi

- Per spec v3 line 241: VV detail accordion phải có button mở **modal/drawer Form HDTV** (Create + Edit + Liên kết VV). Spec line 261 column "Hành động" cho mỗi row HDTV.
- Per spec v3 line 264: HDTV form Edit modal phải có nested accordion "Vụ việc liên kết" + button [+ Liên kết VV] mở modal multi-select N:N.
- User UI thuần phải có thể thực hiện toàn bộ CRUD HDTV qua các entry point này — không cần truy cập API direct.

### Kết quả thực tế

- VV detail accordion: 0 button thao tác.
- HDTV detail standalone: 1 button "Quay lại danh sách" (không phải CRUD).
- 4 URL Create attempt đều fail.
- 1 URL Edit attempt redirect.
- **→ UI gap nghiêm trọng:** R7.7.14 các TC HDTV-029 (Create form), HDTV-030 (Form pageSize regression), HDTV-031 (Form chủ thể CHECK), HDTV-020 (Audit log tab UI) đều BLOCKED re-test vì không có UI entry point.

### Bằng chứng

![BUG-HDTV-033 Phần B — HDTV detail thiếu button Sửa/Xóa](image/r7-4-033-standalone-list-exists.png)

Snapshot HDTV detail page `/hop-dong-tv/9054a0a9-3139-42e3-b817-e7d8a0edb4b2`:
- uid 147_38 button "arrow-left Quay lại danh sách" (chỉ 1 button)
- KHÔNG có button "Sửa" / "Edit" / "Xóa" / "Delete" trên detail
- KHÔNG có "Hành động" column trong table thanhToans

URL test evidence (Re-test #4 2026-05-11):

| URL | Kết quả thực tế | Mong đợi |
|---|---|---|
| `/hop-dong-tv/new` | "Không tìm thấy" 404 | Form Create render |
| `/hop-dong-tv/tao` | "Không tìm thấy" 404 | Form Create render |
| `/hop-dong-tv/them-moi` | "Không tìm thấy" 404 | Form Create render |
| `/hop-dong-tv/{id}/sua` | Redirect `/danh-sach` | Form Edit render |

---

## ~~BUG-HDTV-035~~ [CLOSED] — Filter RangePicker text input cho phép reversed range, FE silently drop Đến ngày trên submit (không validation error)

> **Re-test #6 2026-05-11 17:05:00 — ✅ PASS Closed-verified.** Standalone list filter test: type `Từ ngày=01/06/2026` + `Đến ngày=31/12/2026` (cb_nv_tw_07) + click Tìm kiếm → Network: `GET /api/v1/hop-dong-tu-vans?tuNgay=2026-06-01&denNgay=2026-12-31&page=1&pageSize=20` → **200 OK với cả 2 param** (không còn silent drop denNgay). FE commit text input đầy đủ vào query.

### Mô tả

QTHT (`qtht_07`) lọc danh sách HDTV trên page `/hop-dong-tv/danh-sach`. Type Từ ngày=`31/12/2026` rồi type Đến ngày=`01/01/2026` (range reversed). Click Tìm kiếm → FE silently drop field Đến ngày: URL chỉ có `?tuNgay=2026-12-31` không có `denNgay`, ô input Đến ngày bị xóa trống, table trả 0 records, không hiển thị toast/inline validation error. User không biết tại sao kết quả 0 → confusing UX. (Calendar UI thì disable đúng ô <Từ ngày trong picker Đến ngày — PASS phần này).

### Các bước tái hiện

1. Login QTHT `qtht_07` + OTP 666666 → dashboard.
2. Navigate `/hop-dong-tv/danh-sach`.
3. Click textbox "Từ ngày" → type `31/12/2026` + Enter.
4. Click textbox "Đến ngày" → type `01/01/2026` + Enter.
5. Quan sát: cả 2 ô input đã hiển thị giá trị nhập.
6. Click button "Tìm kiếm".
7. Quan sát: URL = `?tab=DANG_THUC_HIEN&pageSize=10&tuNgay=2026-12-31&page=1` (KHÔNG có `denNgay`). Ô Đến ngày bị xóa trống. Table empty 0 records. KHÔNG có toast/inline error.

### Kết quả mong đợi

- FE hiển thị inline error "Đến ngày phải sau Từ ngày" hoặc swap 2 giá trị tự động; HOẶC
- Nếu cho phép submit với reversed range thì BE phải trả validation error → FE hiển thị toast "Khoảng ngày không hợp lệ".
- User PHẢI biết input bị reject (không silent drop).

### Kết quả thực tế

- FE silently strip field `denNgay` khỏi query, gửi GET `/api/v1/hop-dong-tu-vans?tuNgay=2026-12-31` không có `denNgay`.
- Console clean, không có error.
- Ô Đến ngày bị reset về placeholder "Chọn Đến ngày".
- Table empty + pagination "Không có dữ liệu".

### Bằng chứng

![FE silent drop reversed RangePicker](image/r7-4-014-rangepicker-silent-drop.png)

---

## ~~BUG-HDTV-036~~ [CLOSED] — CB_NV_BN/CB_NV_DP có button "+ Tạo hợp đồng" trên standalone list (QTHT KHÔNG có), standalone create route `/hop-dong-tv/tao-moi` render OK trái spec

> **Re-test #6 2026-05-11 17:07:00 — ✅ PASS Closed-verified.** 4 role test standalone list `/hop-dong-tv/danh-sach`:
> - `qtht_07` (QTHT): KHÔNG có button "+ Tạo hợp đồng" (giữ nguyên).
> - `cb_nv_tw_07` (CB_NV_TW): KHÔNG có button (mới fix). Chỉ "Xuất Excel" + "Làm mới".
> - `cb_nv_bn_07` (CB_NV_BN BKH): KHÔNG có button (mới fix). Chỉ "Xuất Excel" disabled + "Làm mới".
> - `cb_nv_dp_07` (CB_NV_DP AG): KHÔNG có button (mới fix). Chỉ "Xuất Excel" + "Làm mới".
>
> Permission inversion đã fix — 3 role CB không còn button "+ Tạo hợp đồng" trên standalone list. Spec v3.5 M-01 enforce: HDTV chỉ Create qua modal/drawer trong VV accordion.
>
> Evidence: ![CB_NV_BN no Create btn](image/r7-reverify-bug-036-cb-nv-bn-no-create.png) ![CB_NV_DP no Create btn](image/r7-reverify-bug-036-cb-nv-dp-no-create.png) ![QTHT no Create btn](image/r7-reverify-bug-036-qtht-no-create.png)

### Mô tả

Trên page standalone list `/hop-dong-tv/danh-sach`, button "+ Tạo hợp đồng" render conditional theo role: `cb_nv_bn_07` (CB_NV_BN cấp TW, đơn vị BKH) + `cb_nv_dp_07` (CB_NV_DP cấp ĐP, AG) **CÓ** button, click → navigate `/hop-dong-tv/tao-moi` standalone create page render đầy đủ form. Trong khi `qtht_07` (QTHT root) **KHÔNG có** button này (chỉ có "Làm mới"). 2 vấn đề: (1) Permission inversion — CB cấp dưới có quyền create HDTV trong khi QTHT root không có, sai logic phân quyền chuẩn. (2) Standalone create route tồn tại trái spec v3.5 line 660 M-01 "HDTV chỉ truy cập qua tab Chi tiết VV và TVV" + spec v3 line 241 "implement dang modal/drawer khi truy cap tu VV/TVV". Standalone page Create là legacy chưa cleanup hoặc do FE/BE bypass permission gate.

### Các bước tái hiện

1. Login QTHT `qtht_07` + OTP → navigate `/hop-dong-tv/danh-sach`. Toolbar render chỉ "Làm mới" — KHÔNG có "+ Tạo hợp đồng".
2. Logout (close tab + new isolated context).
3. Login `cb_nv_bn_07` (CB_NV_BN, BKH) + OTP → navigate `/hop-dong-tv/danh-sach`. Toolbar render "+ Tạo hợp đồng" + "Xuất Excel" + "Làm mới". Click "+ Tạo hợp đồng" → navigate `/hop-dong-tv/tao-moi` standalone create page render: heading "Tạo hợp đồng tư vấn", form đầy đủ.
4. Logout. Login `cb_nv_dp_07` (CB_NV_DP, AG) + OTP → navigate `/hop-dong-tv/danh-sach`. Toolbar cũng có "+ Tạo hợp đồng" giống CB_NV_BN. (List trả 1 record AG scope).

### Kết quả mong đợi

Per spec v3.5 line 660 M-01 + v3 line 241:
- KHÔNG role nào có button "+ Tạo hợp đồng" trên standalone list (vì standalone không phải entry point chính thức).
- Standalone create route `/hop-dong-tv/tao-moi` cần redirect/404 hoặc xóa hoàn toàn.
- Entry point Create HDTV CHỈ qua modal/drawer trong VV detail accordion "HĐ tư vấn liên kết" (per BUG-033 đã log).
- Theo BA 2026-05-11, nếu giữ standalone như route kỹ thuật thì phải ẩn và có guard/redirect; không expose như entry point chính cho CB role.

### Kết quả thực tế

- 3 role × button "+ Tạo hợp đồng":
  - `qtht_07`: KHÔNG có button (PASS theo spec, nhưng inverted vs CB).
  - `cb_nv_bn_07`: CÓ button + create page mở OK.
  - `cb_nv_dp_07`: CÓ button + create page mở OK.
- Standalone create route `/hop-dong-tv/tao-moi` render đầy đủ form Tạo hợp đồng tư vấn.

### Bằng chứng

![cb_nv_bn_07 có button + Tạo hợp đồng](image/r7-4-024-cb-nv-bn-07-has-create-btn.png)
![Standalone create page render](image/r7-4-new-standalone-create-page.png)
![cb_nv_dp_07 scope AG + có button](image/r7-4-024-cb-nv-dp-07-scope-ag.png)

### So sánh permission cross-role (R5 UI test)

| Role | Sidebar HDTV menu | Standalone list access | Button "+ Tạo hợp đồng" | Standalone create page |
|---|:-:|:-:|:-:|:-:|
| QTHT (qtht_07) | KHÔNG (đúng spec) | ✅ Render | ❌ KHÔNG (inverted) | (chưa test trực tiếp, suy luận có) |
| CB_NV_BN_07 | KHÔNG (đúng spec) | ✅ Render (0 records BKH scope) | ✅ **CÓ** (sai spec) | ✅ Render OK |
| CB_NV_DP_07 | KHÔNG (đúng spec) | ✅ Render (1 record AG scope) | ✅ **CÓ** (sai spec) | (suy luận có) |
| DN 9999999990 | KHÔNG (đúng spec) | ❌ Redirect /dashboard (đúng spec) | N/A | N/A |

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (bypass tạm) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | `/api/v1/` |
| Frontend | React + Vite + Ant Design + CASL |
| Backend | NestJS + PostgreSQL + class-validator |
| Xác thực | JWT + OTP email; session timeout aggressive ~3-5 phút |
| Tool test | Chrome DevTools MCP (`mcp__chrome-devtools__*`) với 6 isolated context |

---

*Bug report generated: 2026-05-10 09:30:00 | QA Automation via Claude Code + Chrome DevTools MCP*

---
