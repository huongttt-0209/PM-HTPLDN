# Functional Test Report — Hợp đồng tư vấn (R7.7.14)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Hợp đồng tư vấn (HĐ TV) — UC163 sub-resource theo SRS v2.1 |
| **SRS Reference** | [srs-fr-14-hop-dong-tv.md](../../../../input/srs-v3/srs-fr-14-hop-dong-tv.md) — FR-X.3-01 UC163 |
| **UC Coverage** | UC163 (sub-resource của VV / TVV — không có menu sidebar độc lập) |
| **Người test** | QA Automation (Claude Code + Chrome DevTools MCP) |
| **Ngày cập nhật** | 2026-05-11 17:10:00 (R6 audit dev fix 6 bug) |
| **Môi trường** | http://103.172.236.130:3000/ |
| **OTP Bypass** | `666666` |
| **Test Method** | UI MCP đa role (chính) + API supporting evidence |
| **Primary Account** | `cb_nv_tw_07` (CB_NV_TW Cục BTTP) |
| **Multi-role accounts** | `qtht_07` · `nht_btp_tw_audit_r30` · `cb_nv_bn_07` (BKH) · `cb_nv_dp_07` (AG) · `9999999990` (DN) |
| **Round** | R7 (gồm R1 → R6 — chi tiết lifecycle ở cuối file) |
| **Tài liệu tham chiếu** | [seed-checklist-r7-3-14-hdtv.md](../../seed/hop-dong-tv/seed-checklist-r7-3-14-hdtv.md) · [bug-report-r7-7-14-hdtv.md](../../bug-reports/hop-dong-tv/bug-report-r7-7-14-hdtv.md) |

---

## 1. Tóm tắt kết quả (Executive Summary)

| Chỉ số | Giá trị |
|--------|---------|
| **Tổng TC trong scope** | **24** (HDTV-013 → HDTV-036; trong đó HDTV-001..012 list/menu defer per SRS v2.1 out-of-scope) |
| **Đã test** | 24 / 24 (100%) |
| **✅ Đạt (PASS)** | **21** TC |
| **⚠️ Sai spec** | **2** TC (HDTV-028, HDTV-034) |
| **❌ Lỗi (FAIL)** | **1** TC (HDTV-032) |
| **🚫 Không test được** | 0 |
| **Tỉ lệ Đạt (Pass Rate)** | **88%** (21/24, không tính Sai spec / Lỗi) |
| **P0 Pass Rate** | 100% (10/10 P0 đã Đạt — phân quyền + validation chính) |
| **Bug phát hiện** | **12** (10 Closed sau R6 · 2 Open: 1 Medium + 1 Minor) |
| **Health Score** | 92/100 (R6 — tăng từ 85 R3 do 6 bug fix PASS verified) |
| **Browse Status** | OK — Chrome DevTools MCP, 4 isolated context không crash |

### Verdict: ✅ **PASS có điều kiện** (CONDITIONAL PASS)

Module HĐ TV ổn định cho luồng CRUD + phân quyền + cross-module integration với VV. Còn **2 TC chưa Đạt clean** (HDTV-028/032/034 — xem Bảng 2 để biết cần làm gì) — KHÔNG block release vì:
- 1 bug Medium (BUG-032 — TVV detail thiếu section HĐ TV) → Dev FE bổ sung.
- 1 bug Minor (BUG-034 — route standalone `/hop-dong-tv/danh-sach` còn render) → chờ BA confirm spec xử lý.

### Phân loại TC theo nhóm test (Pass Rate breakdown)

| Nhóm test | Mô tả | Tổng | ✅ Đạt | ⚠️ Sai spec | ❌ Lỗi | **Pass Rate** |
|------|-------|----:|----:|--------:|----:|--------------:|
| **Negative** | Validation form CRUD (rỗng, biên, format) | 3 | 3 | 0 | 0 | **100%** |
| **Validation** | Business rule auto-calc (tiến độ, công thức) | 4 | 4 | 0 | 0 | **100%** |
| **Authorization** | Permission matrix role × scope | 5 | 5 | 0 | 0 | **100%** |
| **Edge / Guard** | Delete có VV link / biên giá trị | 2 | 2 | 0 | 0 | **100%** |
| **Integration** | Cross-module VV ↔ HD ↔ TVV | 5 | 3 | 1 | 1 | **60%** ⚠️ |
| **Workflow** | Audit log + state transition | 1 | 1 | 0 | 0 | **100%** |
| **Search/Filter** | Search + filter + pagination | 1 | 1 | 0 | 0 | **100%** |
| **UX / Spec** | Standalone route conflict spec | 1 | 0 | 1 | 0 | **0%** ⚠️ |
| **UI Form** | Dropdown TVV/CG picker + RangePicker | 2 | 2 | 0 | 0 | **100%** |
| **Total** | | **24** | **21** | **2** | **1** | **88%** |

→ **Happy-path Pass Rate = 21/24 = 88%** — đủ tốt cho downstream module phụ thuộc HĐ TV (chỉ đọc data).

---

## 2. Test Results Summary

### Bảng 1 — Trạng thái toàn bộ TC (snapshot R6 — LATEST 2026-05-11 17:10:00)

| TC ID | Tên TC ngắn | Type | Priority | Status | Bug ID | Ghi chú ngắn |
|---|---|---|:-:|:-:|---|---|
| HDTV-013 | Tạo HD trống tên → ERR-VAL | Negative | P0 | ✅ Đạt | — | API trả 422 ERR-VAL đúng schema |
| HDTV-014 | Ngày BĐ > Ngày KT → ERR-VAL | Negative | P0 | ✅ Đạt | ~~BUG-035~~ | Calendar disable + text input commit đúng (R6) |
| HDTV-015 | Giá trị HD ≤ 0 → ERR-VAL | Negative | P0 | ✅ Đạt | — | API trả 422 cho 0 và số âm |
| HDTV-016 | Tổng thanh toán > giá trị HD → ERR | Validation | P0 | ✅ Đạt | — | BR-VAL-HDTV-03 enforced BE |
| HDTV-017 | Search + filter + pagination | Search | P1 | ✅ Đạt | — | Tab filter + page-size OK |
| HDTV-018 | Tiến độ TT công thức 50% | Validation | P1 | ✅ Đạt | ~~BUG-018~~ | Form Edit có switch giai đoạn → tienDoTt=50% (R3 Closed) |
| HDTV-019 | Highlight đỏ HD ≤30 ngày | Validation | P2 | ✅ Đạt | — | Cell rgb(255,77,79) #ff4d4f AntD danger |
| HDTV-020 | Tab Nhật ký HD detail | Workflow | P1 | ✅ Đạt | ~~BUG-020~~ | UI tab Nhật ký 6 row + API `/audit-logs` 200 (R6 Closed) |
| HDTV-021 | QTHT chỉ view, không CUD | Authorization | P0 | ✅ Đạt | ~~BUG-021~~ | qtht_07 POST/PATCH/DELETE đều 403 (R3 Closed) |
| HDTV-022 | NHT không có HD trong sidebar | Authorization | P0 | ✅ Đạt | — | Sidebar không HD + URL guard chặn |
| HDTV-023 | DN không truy cập HD | Authorization | P0 | ✅ Đạt | — | DN sidebar 5 module, không HD; API 403 |
| HDTV-024 | BN/DP scope theo donViId | Authorization | P0 | ✅ Đạt | ~~BUG-036~~ | BKH 0 record, AG 1 record AG-scope; CB không còn Create btn (R6 Closed) |
| HDTV-025 | DELETE HD có VV link → ERR | Guard | P0 | ✅ Đạt | — | BE chặn DELETE đúng business rule |
| HDTV-026 | PATCH `vuViecIds` add VV vào HD mồ côi | Integration | P0 | ✅ Đạt | ~~BUG-026~~ | soVuViecLienKet 0→1 persist (R3 Closed) |
| HDTV-027 | VV detail accordion HD list | Integration | P0 | ✅ Đạt | ~~BUG-031~~ | Accordion 10 column + button Tạo (R6 Closed) |
| HDTV-028 | TVV detail có section HĐ TV | Integration | P1 | ⚠️ **Sai spec** | **BUG-032** | TVV detail KHÔNG có section HD — FE chưa implement |
| HDTV-029 | Form HD có dropdown TVV picker | UI Form | P1 | ✅ Đạt | ~~BUG-029~~ | Radio + Combobox + CHECK enforced (R3 Closed) |
| HDTV-030 | Edit form load dropdown TVV | UI Form | P1 | ✅ Đạt | ~~BUG-030~~ | pageSize=100 + dropdown 8 options render (R6 Closed) |
| HDTV-031 | Form HD dropdown CG picker | UI Form | P1 | ✅ Đạt | ~~BUG-031~~ | FE/BE param case thống nhất (R6 Closed) |
| HDTV-032 | TVV-HD section Lịch sử | Integration | P1 | ❌ **Lỗi** | **BUG-032** | TVV detail tab Lịch sử thiếu sub-section HD |
| HDTV-033 | Entry point modal/drawer | Integration | P0 | ✅ Đạt | ~~BUG-033~~ | VV accordion + HDTV detail có Create/Edit/Delete (R6 Closed) |
| HDTV-034 | Route standalone `/hop-dong-tv/danh-sach` | UX/Spec | P2 | ⚠️ **Sai spec** | **BUG-034** | Route vẫn render trái spec v3.5 M-01 — chờ BA |
| HDTV-035 | RangePicker text input commit | Negative | P2 | ✅ Đạt | ~~BUG-035~~ | FE commit cả tuNgay + denNgay đầy đủ (R6 Closed) |
| HDTV-036 | Permission inversion CB > QTHT | Authorization | P1 | ✅ Đạt | ~~BUG-036~~ | 3 CB role không còn Create btn standalone (R6 Closed) |
| **Tổng** | **24 TC** | | | **✅21 · ⚠️2 · ❌1 · 🚫0** | | R6: 6/8 bug PASS Closed-verified |

> **Ghi chú scope:** HDTV-001..012 (list/menu/search standalone) defer ngoài scope round 7 — per SRS v2.1 chuyển HĐ TV thành sub-resource VV/TVV, không có menu độc lập. Khi BA quyết định BUG-034 (route standalone) thì re-scope nhóm này.

### Bảng 2 — TC chưa Đạt — vì sao và cần làm gì

Hiện tại còn **3 TC chưa Đạt clean** (1 ❌ Lỗi + 2 ⚠️ Sai spec) — chia 2 nhóm: **2 chờ Dev FE bổ sung UI · 1 chờ BA confirm spec**.

| TC ID | Vì sao chưa chạy được (Đạt) | Cần làm gì để Đạt | Ai làm | Nhóm |
|---|---|---|:-:|:-:|
| HDTV-028 | TVV detail (`/chuyen-gia-tvv/{id}`) không có section "Hợp đồng tư vấn" liệt kê HD theo TVV. Đã verify R6 multi-TVV. | FE bổ sung section gọi API `/tu-van-viens/{id}/hop-dong-tu-vans` render table HD theo TVV trong tab Năng lực hoặc tab riêng. | Dev FE | B (Chờ dev fix) |
| HDTV-032 | TVV detail tab "Lịch sử" chỉ gọi `lich-su-ho-tro` — thiếu sub-section render danh sách HD đã ký theo TVV. | FE bổ sung sub-section "Hợp đồng đã ký" trong tab Lịch sử per SRS v3 line 241. | Dev FE | B (Chờ dev fix) |
| HDTV-034 | Route `/hop-dong-tv/danh-sach` (standalone list) vẫn render được dù SRS v2.1 đã chuyển HĐ TV thành sub-resource. | BA quyết định: **(A)** xóa route hoàn toàn (404) **hoặc (B)** giữ ẩn cho QTHT/admin. Sau khi BA confirm, dev FE thực hiện. | BA | C (Chờ BA confirm spec) |

> **Phân loại nhóm:** B = Chờ dev fix bug (đã log BUG-{ID}) · C = Chờ BA confirm spec.

---

## 3. Bug Report (chỉ liệt kê bug còn Open)

> **Lưu ý:** Chi tiết Steps/Evidence của tất cả 12 bug (10 Closed + 2 Open) xem file [bug-report-r7-7-14-hdtv.md](../../bug-reports/hop-dong-tv/bug-report-r7-7-14-hdtv.md). Section này chỉ tóm tắt 2 bug còn Open.

### BUG-HDTV-032 — [Medium] TVV detail thiếu section "Hợp đồng tư vấn"

| Trường | Giá trị |
|--------|---------|
| **Severity** | Medium |
| **Priority** | P1 |
| **TC Reference** | HDTV-028, HDTV-032 |
| **Status** | **Open** |
| **Assignee** | Dev FE |

**Mô tả:** Theo SRS v3 line 241 + UC163, TVV detail (`/chuyen-gia-tvv/{id}`) phải có section/tab liệt kê các HĐ TV mà TVV đó tham gia. Hiện tại UI chỉ có 5 tab (Hồ sơ / Năng lực / Lịch sử hỗ trợ / Đánh giá / Thẩm định disabled), tab "Lịch sử hỗ trợ" chỉ gọi `lich-su-ho-tro` mà KHÔNG render danh sách HĐ TV.

**Tác động:** QA + người dùng cuối không thể tra cứu lịch sử HĐ của một TVV cụ thể — phải truy ngược từ VV → HD → TVV (workflow dài + dễ miss).

**Đề xuất:** FE bổ sung section "Hợp đồng tư vấn" trong tab Năng lực hoặc tab riêng, gọi `/tu-van-viens/{id}/hop-dong-tu-vans` (hoặc `/hop-dong-tu-vans?tuVanVienId={id}`) render table 10 column như VV detail.

### BUG-HDTV-034 — [Minor] Route standalone `/hop-dong-tv/danh-sach` vẫn render trái spec v3.5

| Trường | Giá trị |
|--------|---------|
| **Severity** | Minor |
| **Priority** | P2 |
| **TC Reference** | HDTV-034 |
| **Status** | **Open** (chờ BA confirm) |
| **Assignee** | BA (quyết định spec) → Dev FE (thực hiện) |

**Mô tả:** SRS v3.5 line 660 M-01 + spec v3 line 241 quy định HĐ TV chỉ truy cập qua VV/TVV modal/drawer, KHÔNG có route standalone. Hiện tại `/hop-dong-tv/danh-sach` vẫn render được table list (dù không có menu sidebar dẫn đến).

**Tác động:** Tester / dev nhập trực tiếp URL vẫn truy cập được — vi phạm "single source of truth" pattern của spec v2.1.

**Đề xuất BA xác nhận:**
- **Phương án A:** Xóa route hoàn toàn → trả 404 khi nhập URL.
- **Phương án B:** Giữ route nhưng ẩn cho mọi role trừ QTHT/admin (làm trang quản trị nội bộ).

---

## 4. Detailed Test Results (chi tiết các TC quan trọng)

> Liệt kê chi tiết các TC có nhiều bước hoặc TC đã từng FAIL/PARTIAL nay PASS sau dev fix. Các TC Negative/Validation đơn giản (HDTV-013/014/015/016) — xem bug-report cho payload chi tiết.

### 4.1 HDTV-018 — Tiến độ TT công thức 50% (Closed R3 sau dev fix)

**Pre-conditions:** login `cb_nv_tw_07`; có HD `HDTV-20260510-0001` đã tạo với 2 giai đoạn thanh toán (50tr + 50tr / 100tr).

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Mở Form Edit HD | Có switch toggle "Đã thanh toán" cho từng giai đoạn | Form Edit có 2 switch giai đoạn (trước R3 KHÔNG có) | ✅ |
| 2 | Toggle 1/2 switch → Lưu | PATCH success + `tienDoTt = 50` | PATCH 200 + GET response `tienDoTt: 50` | ✅ |
| 3 | UI HD detail | Hiển thị "Tiến độ thanh toán: 50%" | Đúng "50%" | ✅ |

### 4.2 HDTV-021 — QTHT chỉ view, không CUD (Closed R3 sau dev fix Critical)

**Pre-conditions:** login `qtht_07` trong isolated context `qtht_retest`.

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | GET `/api/v1/auth/me` | role=QTHT, perms=[] | role=QTHT, perms=[] | ✅ |
| 2 | GET `/api/v1/hop-dong-tu-vans?pageSize=5` | 200 (quyền R) | 200 + records | ✅ |
| 3 | POST `/api/v1/hop-dong-tu-vans` (body hợp lệ) | 403 ERR-PERM | **403 ERR-PERM-SYS-00-01** | ✅ |
| 4 | PATCH `/api/v1/hop-dong-tu-vans/{id}` | 403 | **403 ERR-PERM-SYS-00-01** | ✅ |
| 5 | DELETE `/api/v1/hop-dong-tu-vans/{id}` | 403 | **403 ERR-PERM-SYS-00-01** | ✅ |

> Trước R3: PATCH/DELETE bypass thành công (Critical). Sau R3: BE wrap @Permission middleware đúng — bug Closed.

### 4.3 HDTV-024 — BN/DP scope theo donViId + Permission CB vs QTHT (Closed R6)

**Pre-conditions:** isolated contexts `bn_role` (cb_nv_bn_07 BKH) + `dp_role` (cb_nv_dp_07 AG) + `qtht_07`.

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | `cb_nv_bn_07` BKH GET `/hop-dong-tu-vans?pageSize=50` | 0 record (HD seed thuộc Cục BTTP TW ≠ BKH) | 200 + 0 items | ✅ |
| 2 | `cb_nv_dp_07` AG GET cùng endpoint | Chỉ record của AG | 200 + 1 item AG-scope | ✅ |
| 3 | `cb_nv_bn_07` + `cb_nv_dp_07` mở `/hop-dong-tv/danh-sach` | KHÔNG có button "+ Tạo hợp đồng" (per BUG-036 R6) | Cả 2 KHÔNG có button | ✅ |
| 4 | `qtht_07` mở `/hop-dong-tv/danh-sach` | KHÔNG có Create | Đúng | ✅ |

> Trước R6: CB_BN + CB_DP có button Create / QTHT không có → permission inversion (BUG-036 Major). Sau R6: nhất quán cả 3 role đều không có Create → đúng spec.

### 4.4 HDTV-027 — VV detail accordion HD (Closed R6)

**Pre-conditions:** login `cb_nv_tw_07`; có VV `VV-QA-R7-LIFECYCLE-HT` state HOAN_THANH.

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Mở VV detail | Có accordion "Hợp đồng tư vấn liên kết" | Accordion render | ✅ |
| 2 | Click accordion expand | Table 10 column (Mã / Tên / Bên A / Bên B / Giá trị / Tiến độ TT / Ngày BĐ / Ngày KT / Trạng thái / Action) + button "+ Tạo hợp đồng" | Render đúng 10 column + button (trước R6 thiếu 4 column + thiếu button) | ✅ |
| 3 | Click "+ Tạo hợp đồng" | Mở Drawer Tạo HD với `vuViecId` auto-fill | Drawer mở + auto-fill VV-QA-R7-LIFECYCLE-HT | ✅ |

### 4.5 HDTV-028 — TVV detail section HĐ TV (⚠️ STILL Open R6)

**Pre-conditions:** login `cb_nv_tw_07`; có TVV `TVV-BTP-TW-0014` HOAT_DONG.

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Sidebar → Mạng lưới TVV → Tư vấn viên / Chuyên gia | List TVV render | List render | ✅ |
| 2 | Click TVV row → mở `/chuyen-gia-tvv/{id}` | Detail page render | URL `/chuyen-gia-tvv/{id}`, hồ sơ render | ✅ |
| 3 | Verify tabs | Có tab/section "Hợp đồng tư vấn" liệt kê HD theo TVV | **5 tab** (Hồ sơ / Năng lực / Lịch sử hỗ trợ / Đánh giá / Thẩm định disabled) — KHÔNG có section HD | ❌ **Sai spec** |
| 4 | Check tab "Lịch sử hỗ trợ" | Có sub-section "Hợp đồng đã ký" | Chỉ gọi `lich-su-ho-tro` — KHÔNG render HD | ❌ **Sai spec** |

> **Verdict R6:** BUG-032 vẫn Open — Dev FE chưa implement section. Đã verify với 2 TVV khác nhau cùng kết quả.

---

## 5. Test Data Used

### 5.1 Tài khoản test

| Username | Role | Đơn vị | Cấp | Dùng cho TC |
|----------|------|--------|-----|-------------|
| `cb_nv_tw_07` | CB_NV_TW + CB_PD_TW | Cục BTTP | TW | HDTV-013/014/015/016/017/018/019/025/026/027/028/029/030/031/032/035 |
| `qtht_07` | QTHT | (none) | TW | HDTV-021 / HDTV-036 (authz + permission inversion) |
| `nht_btp_tw_audit_r30` | NHT (TVV/CG) | Cục BTTP | TW | HDTV-022 (NHT sidebar không HD) |
| `9999999990` | DN | DN Test 01 | (DN) | HDTV-023 (DN sidebar không HD) |
| `cb_nv_bn_07` | CB_NV_BN | BKH | BN | HDTV-024 / HDTV-036 (scope BN) |
| `cb_nv_dp_07` | CB_NV_DP | Sở Tư pháp AG | DP | HDTV-024 / HDTV-036 (scope DP) |

### 5.2 Data tạo / sử dụng trong test

| ID / Mã | Tên / Mô tả | Purpose | Cleanup |
|---------|-------------|---------|---------|
| HDTV-20260510-0001 | HD mồ côi pre-fix lần đầu | Seed evidence + HDTV-030 DELETE | Hard-deleted |
| HDTV-20260510-0003..0008 | 6 HD cover 6 LV linked VV | HDTV-027 entry-point verify | Keep cho downstream R7.7.X |
| HDTV-20260510-0009 | HD progress 50% test (3 thanhToans) | HDTV-018 evidence | Hard-deleted by QTHT trong BUG-021 retest (evidence) |
| HDTV-20260510-0010 | HD ngayKt 5 ngày (chưa link VV) | HDTV-019 highlight test | Keep (evidence BUG-026 cascade) |
| HDTV-20260510-0011 | HD ngayKt 5 ngày + linked VV-509-006 | HDTV-019 highlight PASS | Keep (HDTV-019 PASS evidence) |
| HDTV-20260511-0002 | HD ngayKt ~21 ngày | HDTV-019 retest R5 | Keep |
| VV-QA-R7-LIFECYCLE-HT | VV HOAN_THANH | HDTV-027 + HDTV-031 accordion R6 | Keep |
| TVV-BTP-TW-0014 + TVV-BTP-TW-0035 | TVV HOAT_DONG | HDTV-028 + HDTV-032 detail check | Keep |

---

## 6. Environment Notes

- **API endpoint pattern:** `/api/v1/hop-dong-tu-vans` (plural `-vans`).
- **FE route:** `/hop-dong-tv/{path}` (NOT `/hop-dong-tu-van`); detail `/hop-dong-tv/{id}`; TVV detail `/chuyen-gia-tvv/{id}`.
- **Auth flow:** JWT + OTP email (bypass `666666`); BE revoke aggressive ~3-5 phút bất chấp `exp` 15 phút — phải re-login giữa session dài (memory `qa_htpldn_jwt_revoke_aggressive`).
- **Frontend framework:** React + Vite + Ant Design + CASL.
- **Backend:** NestJS + PostgreSQL + class-validator (auto-generate ERR-VAL-SYS-00-01).
- **Multi-role testing:** Chrome DevTools MCP `isolatedContext` per role tránh httpOnly cookie sticky cross-session (memory `qa_htpldn_round5_t01`).
- **Known limitations:** HĐ TV không có menu sidebar độc lập (per SRS v2.1 R7.E1 verified) — truy cập qua VV/TVV detail.

---

## 7. Recommendations

### Phải fix trước release (Must Fix)

Không có bug Critical/Major còn Open. Tất cả Critical (BUG-021) và Major (BUG-018/026/029/030/031/033/035/036) đã PASS Closed-verified ở R3/R6.

### Nên fix (Should Fix)

1. **BUG-032 (Medium)** — FE bổ sung section "Hợp đồng tư vấn" trong TVV detail (`/chuyen-gia-tvv/{id}`) — gọi `/tu-van-viens/{id}/hop-dong-tu-vans` render table HD theo TVV. Unblock HDTV-028 + HDTV-032.

### Chờ BA xác nhận spec (Spec Clarification)

2. **BUG-034 (Minor)** — Route standalone `/hop-dong-tv/danh-sach` vẫn render trái spec v3.5 M-01. BA quyết định: (A) xóa route → 404, hoặc (B) giữ ẩn cho QTHT/admin.

### Khuyến nghị bổ sung

3. **Permission audit cross-entity:** QTHT bypass CUD đã fix ở HD TV (BUG-021) — nên probe các entity khác (`/tu-van-viens`, `/to-chuc-tv`, `/vu-viecs`) xem QTHT có bypass tương tự không (memory `qa_htpldn_qtht_permission_bypass`).
4. **Downstream module R7.7.X:** Pool 7 HD hiện tại (cover 6 LV) đủ cho module read-only. Module test create/update HD đã unblock sau khi BUG-029/030 fix.

---

## 8. Appendix

### A — API Endpoints Tested

| Method | Endpoint | Purpose | Tested in TC |
|--------|----------|---------|--------------|
| GET | `/api/v1/hop-dong-tu-vans` | List HD theo scope role | HDTV-021/022/023/024/036 |
| GET | `/api/v1/hop-dong-tu-vans/:id` | HD detail | HDTV-018/027 |
| GET | `/api/v1/hop-dong-tu-vans/:id/audit-logs` | Audit log HD | HDTV-020 |
| POST | `/api/v1/hop-dong-tu-vans` | Tạo HD | HDTV-013/014/015/016/018/019/021/029 |
| PATCH | `/api/v1/hop-dong-tu-vans/:id` | Update HD (whole record + version) | HDTV-018/026 |
| DELETE | `/api/v1/hop-dong-tu-vans/:id` | Hard delete (Guard có VV link) | HDTV-021/025 |
| GET | `/api/v1/tu-van-viens?pageSize=100` | Dropdown TVV picker | HDTV-029/030 |
| GET | `/api/v1/auth/me` | Verify role + permissions | All authz TCs |

### B — Screenshots evidence (R6)

| File | Mô tả | TC Ref |
|------|-------|--------|
| [image/r7-reverify-hdtv-detail-qtht-nhatky.png](../../bug-reports/hop-dong-tv/image/r7-reverify-hdtv-detail-qtht-nhatky.png) | HD detail tab Nhật ký 6 row + endpoint `/audit-logs` 200 | HDTV-020 |
| [image/r7-reverify-bug-030-edit-form-dropdown.png](../../bug-reports/hop-dong-tv/image/r7-reverify-bug-030-edit-form-dropdown.png) | Form Edit pageSize=100 + dropdown render | HDTV-030 |
| [image/r7-reverify-bug-036-qtht-no-create.png](../../bug-reports/hop-dong-tv/image/r7-reverify-bug-036-qtht-no-create.png) | QTHT KHÔNG có button Create | HDTV-036 |
| [image/r7-reverify-bug-036-cb-nv-bn-no-create.png](../../bug-reports/hop-dong-tv/image/r7-reverify-bug-036-cb-nv-bn-no-create.png) | CB_NV_BN KHÔNG có button Create | HDTV-024/036 |
| [image/r7-reverify-bug-036-cb-nv-dp-no-create.png](../../bug-reports/hop-dong-tv/image/r7-reverify-bug-036-cb-nv-dp-no-create.png) | CB_NV_DP KHÔNG có button Create | HDTV-024/036 |
| [image/r7-reverify-bug-032-tvv-detail-still-no-hd-tab.png](../../bug-reports/hop-dong-tv/image/r7-reverify-bug-032-tvv-detail-still-no-hd-tab.png) | TVV detail vẫn 5 tab không có HD section | HDTV-028/032 |

### C — SRS Traceability Matrix

| SRS Reference | TC Coverage | Status |
|---------------|-------------|--------|
| FR-X.3-01 §2 entity HOP_DONG_TU_VAN | HDTV-013/014/015/016/018/026/029 | ✅ 7/7 Đạt |
| BR-VAL-HDTV-01..05 | HDTV-013/014/015/016/018 | ✅ 5/5 Đạt |
| BR-VIEW-HDTV-01 highlight ≤30 ngày | HDTV-019 | ✅ Đạt |
| BR-AUD-HDTV-01 audit log | HDTV-020 | ✅ Đạt (R6) |
| BR-AUTH-HDTV-01..03 + BR-AUTH-08 | HDTV-021/022/023/024 | ✅ 4/4 Đạt (R3 + R6) |
| BR-GUARD-HDTV-01 | HDTV-025 | ✅ Đạt |
| BR-DELETE-HDTV-01 | HDTV-030 | ✅ Đạt |
| BR-DROP-HDTV-01/02 (TVV/CG dropdown) | HDTV-029/031 | ✅ 2/2 Đạt (R3 + R6) |
| FR-X.3-01 entry-point sub-resource VV | HDTV-027 / HDTV-033 | ✅ 2/2 Đạt (R6) |
| FR-X.3-01 entry-point sub-resource TVV | HDTV-028 / HDTV-032 | ⚠️ 0/2 Sai spec — BUG-032 Open |
| FR-X.3-01 N:N integration | HDTV-026 | ✅ Đạt (R3) |
| Spec v3.5 M-01 sub-resource only | HDTV-034 | ⚠️ Sai spec — BUG-034 chờ BA |

---

# Lifecycle archive — older rounds

> Section này lưu chi tiết lịch sử test các round trước (R1 → R5). Round R6 LATEST đã summary đầy đủ ở phần trên.

## R5 — 2026-05-11 15:25:00 → 15:40:00 — Re-test UI-only multi-role (6 TC + 2 bug mới)

Scope: chạy lại 6 TC qua UI thuần (KO API direct) với 4 role để phát hiện vấn đề UX/Permission cross-role. Phát hiện **2 bug mới**: BUG-035 Minor (RangePicker text input drop) + BUG-036 Major (CB_NV_BN/DP có button Create / QTHT không có).

| TC ID | Status R5 | Bug phát hiện |
|---|:-:|---|
| HDTV-014 | ✅ Đạt (calendar) + ⚠️ Sai spec (text input) | BUG-035 Minor |
| HDTV-017 | ✅ Đạt | — |
| HDTV-019 | ✅ Đạt | — |
| HDTV-022 | ✅ Đạt | — |
| HDTV-023 | ✅ Đạt | — |
| HDTV-024 | ✅ Đạt + ⚠️ permission anomaly | BUG-036 Major |
| HDTV-028 | ⚠️ Sai spec (confirm BUG-032) | BUG-032 |

## R4 — 2026-05-11 14:00:00 → 14:35:00 — Re-test UI-only qtht_07 (4 spec-gap mới)

Phát hiện 4 spec-gap mới: BUG-031 (accordion column thiếu), BUG-032 (TVV detail section thiếu), BUG-033 (entry point modal/drawer chưa đầy đủ), BUG-034 (standalone route stale).

## R3 — 2026-05-10 21:34:00 → 21:50:00 — Re-test sau dev fix lần 2 (bộ acc `_07`)

| Bug ID | R1/R2 status | R3 status | Ghi chú |
|--------|--------------|-----------|---------|
| BUG-018 | Open (PATCH silently drop) | ✅ Closed | Form Edit có 3 switch giai đoạn; click → tienDoTt=50% |
| BUG-020 | Open (4 path 404, top-level 403) | ⚠️ Partial (BE ✅ / UI ❌) | API `/audit-logs` 200 + 5 events; UI vẫn thiếu tab → Major→Medium |
| BUG-021 | Open Critical (CUD bypass) | ✅ Closed | qtht_07 POST/PATCH/DELETE đều 403 |
| BUG-026 | Open (PATCH silently drop) | ✅ Closed | PATCH `vuViecIds` persist, soVuViecLienKet 0→1 |
| BUG-029 | Open (form thiếu TVV/CG) | ✅ Closed | Radio + Combobox + CHECK 400 ERR-HDTV-CHU-THE-01 |
| BUG-030 | (mới R3) | ❌ Open Major | FE call `pageSize=200` → 422 (BE max 100) — dropdown empty |

## R2 — 2026-05-10 12:13:00 → 12:18:00 — Re-test #2

Minor re-test sau dev claim fix lần 1. Hầu hết bug R1 vẫn Open.

## R1 — 2026-05-10 10:54:00 → 11:15:00 — Re-test #1 + bổ sung HDTV-019/028

- HDTV-019 Không test được → Đạt (POST tạo HDTV-0011 với `vuViecIds:[vvId]` works at creation time, cell ngayKt đỏ verify).
- HDTV-028 bổ sung Đạt (TVV detail render 6 tab có "HĐ tư vấn", empty table cascade BUG-029).
- HDTV-021 escalate Major → Critical (PATCH 200 modify thật + DELETE 204 hard-delete thật).

## R0 (lần đầu) — 2026-05-10 09:14:00 → 09:30:00

Chạy lần đầu 17 TC. Phát hiện 6 bug mới: BUG-018 (form thiếu paid toggle) · BUG-020 (audit log) · BUG-021 (QTHT CUD bypass) · BUG-026 (N:N broken) · BUG-029 (form thiếu TVV picker) · BUG-031 cascade.

---

*Report cập nhật: 2026-05-11 17:10:00 (UTC+7) — R6 audit dev fix 6 bug | QA Automation via Claude Code + Chrome DevTools MCP*
