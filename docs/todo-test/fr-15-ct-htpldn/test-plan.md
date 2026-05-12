# Kế Hoạch Kiểm Thử — CT HTPLDN GĐ1+GĐ2 (FR-15, SCR-XI-01)

> **Phiên bản:** 1.1 (Revised 2026-05-12 12:35:00 — re-classified nhóm C → B; fix UC numbering 164-172 → 160-170 v3.5; fix 2 SM transition Hoàn thành actor + Rút trình đích; bổ sung TC 6 lifecycle action + audit fields DOT_BAO_CAO)
> **Ngày tạo:** 2026-05-12
> **Nguồn dữ liệu (SOURCE MODE):** LOCAL — `srs-v3/srs-fr-15-ct-htpldn.md` (baseline v3, 1313 dòng) + `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` line 2508-2640 (8 thay đổi cherry-pick v4 áp v3.5)
> **SRS Reference:** FR-XI-01 → FR-XI-09 (UC160-UC170 v3.5 contiguous; mapping cũ UC164-172/195/196 ở §1.2), SCR-XI-01 (MH-15.1 + MH-15.5..8 đã gộp v2.1)

> **Phân nhóm SRS Update v3.5:** Module FR-15 thuộc **Nhóm B — DELTA+IMPACT** (theo Rule 4 CLAUDE.md global). CHANGELOG-v3-to-v3.5.md line 2508-2640 liệt kê **8 thay đổi nghiệp vụ** áp dụng cho FR-15:
> 1. **A-ITEM-13** — Đổi tên module "Chương trình HTPLDN" → "Quản lý kế hoạch thực hiện chương trình hỗ trợ pháp lý doanh nghiệp" (Breadcrumb + Tiêu đề trang SCR-XI-01 + Entity Module note DOT_BAO_CAO/BAO_CAO_CT_HTPL).
> 2. **B2d** — Re-numbering UC: UC164-172 + UC195/196 → **UC160-UC170 contiguous** (11 UC theo CSV transaction v1.1 §XI dòng 1453-1533).
> 3. **A-ITEM-09 `[SRS-FIX]`** — DOT_BAO_CAO bổ sung 5 audit fields (`created_at`/`updated_at`/`created_by`/`updated_by`/`is_deleted`) + đổi `han_nop`/`tu_ngay`/`den_ngay` datetime → **date** (datepicker chỉ ngày, không giờ phút).
> 4. **B1 `[GAP-XI-01]`** — Đặc tả đầy đủ 6 lifecycle action (Kích hoạt / Tạm dừng / Tiếp tục / Hoàn thành / Hủy / Rút trình) + sửa 2 lỗi SM-KH-CTHTPL: (a) **Hoàn thành actor = CB PD** (không phải CB NV) với guard "Tất cả đợt BC đã hoàn thành" + Lỗi "Chỉ CB PD mới được hoàn thành"; (b) **Rút trình `CHO_PHE_DUYET → DU_THAO`** (không phải HUY).
> 5. **B1 `[GAP-XI-04]`** — Bổ sung Processing "Xuất Excel DS CT" 5 bước trong FR-XI-02 (tên cũ) / **FR-XI-02 UC161** v3.5 (kiểm tra quyền + filter-aware + chặn >10K dòng + tệp 9 cột + danh sách rỗng).
> 6. **B1 `[GAP-XI-03]`** — Entity CHUONG_TRINH_HTPL: 3 trường `muc_tieu` / `doi_tuong` / `thoi_gian_bat_dau` đổi Bắt buộc N → Y (đồng bộ Inputs FR-XI-01).
> 7. **B1 `[GAP-XI-02]`** — Entity BAO_CAO_CT_HTPL: `ky_bao_cao` enum đổi `'THANG','QUY','NAM','TONG_KET'` → **`'SO_BO_6_THANG','SO_BO_NAM','TRON_NAM'`** (đồng bộ DOT_BAO_CAO khớp TT17/2025).
> 8. **B1** — Entity DON_VI mô tả viết lại "cấu trúc 2 tầng: TW cấp 1; BN và ĐP cấp 2 ngang cấp song song — BR-AUTH-02" (KHÔNG 3 tầng).
>
> **Verdict cross-cutting CR-01 cho FR-15:** Entity v3 có `la_cong_bo: boolean` + `ngay_cong_bo: datetime`. CHANGELOG line 2585-2640 **KHÔNG list rename `la_cong_bo` → `cong_khai`** cho FR-15 — FR-15 **GIỮ `la_cong_bo`** trong v3.5. Chỉ FR-02/05/07 + biểu mẫu rename theo CR-01.
>
> **Phạm vi test theo Rule 4 nhóm B:** Test full UC re-numbered (10 UC v3.5) + DOT_BAO_CAO audit fields + datepicker date-only + 6 lifecycle actions + enum kỳ BC mới + đổi tên module Breadcrumb. Sample happy path cho phần KHÔNG đổi (workflow chính DU_THAO→DA_DUYET đã PASS R7.6.4). **KHÔNG retest** chi tiết SCR layout nội bộ không thay đổi.

> **Quy trình:** Theo [scaling-test-strategy.md §4.1 Bước 3](../../../output/scaling-test-strategy.md) — trích BR + sibling-check ≥2 module + BA sign-off trước Bước 4. Sibling tham chiếu: FR-11 Báo cáo (LỚP 5 cùng aggregation), FR-05 Vụ việc (cùng SM-approval pattern CB NV ↔ CB PD cùng cấp).
>
> **v3.0 (2026-04-23):** Test plan này dùng cho **GĐ3 Functional + Auth + Edge**. GĐ1 Seed + GĐ2 Workflow tách output `seed-checklist-fr-15.md` + `workflow-test-report-fr-15.md`. Happy path đã cover ở GĐ2 — TC ở đây chỉ còn **negative + edge + auth + cross-module**.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- Module FR-15 — **Quản lý kế hoạch thực hiện CT HTPLDN** (đổi tên A-ITEM-13 v3.5) gồm **11 FR** (FR-XI-01 → FR-XI-09, bổ sung 05a + 07a) ứng với **10 UC** v3.5 contiguous (UC160-UC170, ánh xạ từ UC164-172 + UC195/196 v3 — xem §1.2) chia 2 lifecycle:
  - **GĐ1 Kế hoạch:** UC160 (CRUD KH) → UC161 (Tìm kiếm + Xuất Excel `[GAP-XI-04]`) → UC162 (Trình duyệt) → UC163 (Duyệt KH) → UC164 (Công bố Cổng PLQG) → 6 lifecycle action `[GAP-XI-01]` (kích hoạt / tạm dừng / tiếp tục / hoàn thành = **CB PD** / hủy / rút trình về DU_THAO).
  - **GĐ2 Đợt Báo cáo:** UC165 (CRUD Đợt BC) → UC166 (Lập BC mẫu 21a/21b TT17) → UC167 (Trình duyệt KQ) → UC168 (Duyệt KQ) → UC169 (Gửi TW) → UC170 (TW tổng hợp).
- **Bảng dữ liệu chính:** `CHUONG_TRINH_HTPL` (3 trường `muc_tieu`/`doi_tuong`/`thoi_gian_bat_dau` đổi Bắt buộc Y `[GAP-XI-03]`) + `DOT_BAO_CAO` (3.4.3.10a, **17 fields v3.5 = 12 v3 + 5 audit + date type fix** `[SRS-FIX]`) + `BAO_CAO_CT_HTPL` (`ky_bao_cao` enum mới TT17 `[GAP-XI-02]`).
- **Màn hình:** SCR-XI-01 (Danh sách + Chi tiết CT, đã gộp v2.1 — MH-15.2..8 thành 2 tab + drill-down) — **Breadcrumb + Tiêu đề v3.5 đổi "Quản lý kế hoạch thực hiện CT HTPLDN"** (A-ITEM-13).
- **Cross-module reads (GĐ2):** số liệu từ FR-02 Hỏi đáp / FR-05 Vụ việc / FR-06 Chi trả `DA_THANH_TOAN` / FR-03 Đào tạo `HOAN_THANH` / FR-08 Đánh giá (gợi ý mẫu 21a/21b).

### 1.2 Danh sách FR / UC (ánh xạ v3 cũ → v3.5 contiguous)

| # | Mã FR | UC v3.5 | UC v3 (cũ) | Tên chức năng | Entity | File Test Case |
|---|---|---|---|---|---|---|
| 1 | FR-XI-01 | **UC160** | UC164 | Quản lý KH thực hiện CT (CRUD `DU_THAO` + 6 lifecycle action `[GAP-XI-01]`) | CHUONG_TRINH_HTPL | `01-TC-crud-ct.md` |
| 2 | FR-XI-02 | **UC161** | UC165 | Tìm kiếm KH + Xuất Excel `[GAP-XI-04]` | CHUONG_TRINH_HTPL | `02-TC-search-ct.md` |
| 3 | FR-XI-03 | **UC162** | UC166 | Trình phê duyệt KH (DU_THAO → CHO_PHE_DUYET) | CHUONG_TRINH_HTPL | `03-TC-trinh-pd-ct.md` |
| 4 | FR-XI-04 | **UC163** | UC167 | CB PD duyệt/từ chối KH (BR-AUTH-05) | CHUONG_TRINH_HTPL | `04-TC-pd-ct.md` |
| 5 | FR-XI-05 | **UC164** | UC168 | Công bố / hủy công bố Cổng PLQG | CHUONG_TRINH_HTPL | `05-TC-cong-bo-ct.md` |
| 6 | FR-XI-05a | **UC165** | UC195 | CRUD Đợt báo cáo (TAO_DOT scope) | DOT_BAO_CAO | `06-TC-crud-dot-bc.md` |
| 7 | FR-XI-06 | **UC166** | UC169 | Lập BC mẫu 21a/21b TT17/2025 | BAO_CAO_CT_HTPL | `07-TC-lap-bc-21ab.md` |
| 8 | FR-XI-07 | **UC167** | UC170 | Trình phê duyệt BC KQ | DOT_BAO_CAO | `08-TC-trinh-pd-bc.md` |
| 9 | FR-XI-07a | **UC168** | UC196 | CB PD duyệt/từ chối BC KQ | DOT_BAO_CAO | `09-TC-pd-bc.md` |
| 10 | FR-XI-08 | **UC169** | UC171 | BN/ĐP gửi BC lên TW | DOT_BAO_CAO | `10-TC-gui-tw.md` |
| 11 | FR-XI-09 | **UC170** | UC172 | TW tổng hợp BC toàn quốc + xuất file | BAO_CAO_CT_HTPL | `11-TC-tw-tonghop.md` |
| 12 | FR-XI-01 (sub) | UC160 sub | — | **6 lifecycle action `[GAP-XI-01]`** — Kích hoạt / Tạm dừng / Tiếp tục / Hoàn thành (**CB PD**) / Hủy / Rút trình | CHUONG_TRINH_HTPL | `12-TC-lifecycle-actions.md` (mới v3.5) |
| 13 | (Schema) | — | — | **DOT_BAO_CAO audit fields + date type `[SRS-FIX]`** — 5 audit + datepicker date-only | DOT_BAO_CAO | `13-TC-dot-bc-audit-fields.md` (mới v3.5) |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|---|---|---|---|
| QTHT | — | `qtht_01` | Smoke truy cập read-only + audit log inspect. `_02` fallback, `_03` permission negative |
| CB_NV_TW | TW | `cb_nv_tw_01` | CRUD CT scope TW + lập BC TW + tổng hợp BC toàn quốc (UC172) |
| CB_NV_BN | BN (BKH) | `cb_nv_bn_01` | CRUD CT scope BN + lập BC BN + gửi TW (UC171) |
| CB_NV_DP | ĐP (AG) | `cb_nv_dp_01` | CRUD CT scope ĐP + lập BC ĐP + gửi TW (UC171) |
| CB_PD_TW | TW | `cb_pd_tw_01` | Duyệt CT/BC cùng cấp TW |
| CB_PD_BN | BN (BKH) | `cb_pd_bn_01` | Duyệt CT/BC cùng cấp BN. `cb_pd_bn_02` (BTC) cho negative cross-unit |
| CB_PD_DP | ĐP (AG) | `cb_pd_dp_01` | Duyệt CT/BC cùng cấp ĐP. `cb_pd_dp_02` (BG) cho negative cross-unit |
| DN (Doanh nghiệp) | — | `9999999990` | Permission negative: DN KHÔNG được CRUD/duyệt CT |
| NHT/CG | ĐP (AG/DN), TW | `nht_01`, `cg_01` (theo convention `_01/_02/_03`, xem [`input/users.csv`](../../../input/users.csv)) | Permission negative: KHÔNG được CRUD/duyệt CT |

> Reference: [input/users.csv](../../../input/users.csv) — 154 dòng (TK 1-9 mỗi role + fallback). [output/permission-matrix.md](../../../output/permission-matrix.md).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|---|---|---|---|---|---|
| BR-AUTH-01 | Xác thực user (username/password + 2FA OTP email) trước mọi truy cập | srs-v3/srs-fr-15-ct-htpldn.md:1242-1249 | ✅ Yes | "API outbound không yêu cầu session (dùng JWT)" — FR-XI-05 API push Cổng PLQG | TC login + TC API outbound |
| BR-AUTH-05 | Phê duyệt cùng cấp — CB NV cấp nào tạo, CB PD CÙNG cấp duyệt. KHÔNG xuyên cấp | srs-v3/srs-fr-15-ct-htpldn.md:1251-1258 | ✅ Yes | — | TC-04 (duyệt CT), TC-09 (duyệt BC), permission cross-unit |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` — TW thấy all, BN thấy BN của mình, ĐP thấy ĐP của mình | srs-v3.md:3958 (Phụ lục B) | ✅ Yes | — | TC permission data isolation tất cả TC list |
| BR-DATA-01 | Soft delete (set `is_deleted=1`) | srs-v3/srs-fr-15-ct-htpldn.md:1260-1265 | ✅ Yes | Áp cho CT khi `DU_THAO` + Đợt BC khi `TAO_DOT` | TC-01 DELETE CT + TC-06 DELETE Đợt BC verify is_deleted |
| BR-DATA-05 | Audit log mọi CUD + phê duyệt | srs-v3/srs-fr-15-ct-htpldn.md:1267-1272 | ✅ Yes | — | TC verify AUDIT_LOG INSERT cho mọi state transition |
| BR-DATA-06 | Export Excel max 10K rows | srs-v3.md:3977 (Phụ lục B) | ✅ Yes (default) | Áp ở FR-XI-09 TW tổng hợp xuất Excel + danh sách CT toolbar | TC export 10K boundary + filter-aware |
| BR-DATA-07 | Pagination default 20/page, max 100 | srs-v3/srs-fr-15-ct-htpldn.md:1274-1279 | ✅ Yes | Áp DS CT (FR-XI-01) + tìm kiếm (FR-XI-02) + DS Đợt BC (FR-XI-05a) | TC pagination boundary |
| BR-FLOW-03 | Không sửa/xóa sau phê duyệt — CT `DA_DUYET`+ trở đi read-only | srs-v3/srs-fr-15-ct-htpldn.md:1281-1287 | ✅ Yes | "QTHT có thể force-edit (audit đặc biệt)" — cần SPEC-CLARIFY UI có nút đó? | TC-01 edit CT `DA_DUYET` → 403/disabled, TC-06 edit Đợt BC `DANG_LAP_BC` → cho phép field BC nhưng KHÔNG cho phép field metadata |
| BR-FLOW-04 | Từ chối bắt buộc lý do (≥10 ký tự) | srs-v3/srs-fr-15-ct-htpldn.md:1289-1294 | ✅ Yes | — | TC-04 từ chối CT, TC-09 từ chối BC |
| BR-FLOW-05 | Công khai qua API trực tiếp (REST không qua LGSP) lên Cổng PLQG. Hủy công khai gỡ | srs-v3/srs-fr-15-ct-htpldn.md:1296-1301 | ✅ Yes | Chỉ áp CT đã `DA_DUYET` → `DA_CONG_BO`. Tuyến API: FR-XII-15 | TC-05 happy + ERR-XI-05-02 Cổng PLQG fail rollback |
| BR-FLOW-08 | BC CT HTPLDN: ĐP+BN gửi TW. TW tổng hợp toàn quốc trên biểu mẫu TT17 | srs-v3/srs-fr-15-ct-htpldn.md:1303-1309 | ✅ Yes | — | TC-10 BN/ĐP gửi TW + TC-11 TW tổng hợp |
| BR-EC-01 | Optimistic Locking trên UPDATE/DELETE (version mismatch → ERR-SYS-02) | srs-v3.md:4066 (Phụ lục B) | ✅ Yes | — | TC concurrent update CT từ 2 tab → ERR-SYS-02 |
| BR-EC-13 | Search sanitize max 200 ký tự (SQL/XSS guard) | srs-v3.md:4078 (Phụ lục B) | ✅ Yes | Áp FR-XI-02 keyword search | TC search SQL injection / XSS / payload >200 ký tự |
| BR-NHATKY-AUDIT | Audit immutable — hỗ trợ FR-IV-NhatKy (read-only view ở module Nhật ký) | srs-v3.md:3976 (Phụ lục B) | ✅ Yes | — | TC verify CT/Đợt BC CUD render trong Nhật ký hệ thống |
| **BR-XI-DOT-DUP** | Đợt BC không trùng (cùng CT + cùng kỳ + cùng khoảng thời gian) | srs-v3/srs-fr-15-ct-htpldn.md:484, 510 (ERR-XI-05a-02) | ✅ Yes | — | TC-06 tạo 2 đợt cùng kỳ → ERR-XI-05a-02 |
| **BR-XI-CT-STATE-DOT** | CT phải ở `DANG_THUC_HIEN` hoặc `HOAN_THANH` mới tạo được Đợt BC | srs-v3/srs-fr-15-ct-htpldn.md:460, 509 (ERR-XI-05a-01) | ✅ Yes | — | TC-06 tạo Đợt BC khi CT `DU_THAO`/`DA_DUYET` → ERR-XI-05a-01 |
| **BR-XI-BNDP-TO-TW** | Chỉ BN/ĐP được gửi BC lên TW. TW không gửi cho chính TW | srs-v3/srs-fr-15-ct-htpldn.md:734, 774 (ERR-XI-08-02) | ✅ Yes | — | TC-10 login `cb_nv_tw_01` ấn "Gửi TW" → ERR-XI-08-02 |
| **BR-XI-TW-AGG-EMPTY** | TW tổng hợp phải chọn ≥1 BC | srs-v3/srs-fr-15-ct-htpldn.md:840 (ERR-XI-09-01) | ✅ Yes | — | TC-11 không chọn BC nào → ERR-XI-09-01 |
| **BR-XI-HOAN-THANH-CBPD** | Hoàn thành CT actor = **CB PD** (không phải CB NV) + guard "Tất cả đợt BC đã hoàn thành" | srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:2570-2600 (Thay đổi 4 Phần 2 `[GAP-XI-01]`) | ✅ Yes (v3.5) | — | TC-12 (12-TC-lifecycle-actions.md) — login CB NV ấn Hoàn thành → "Chỉ CB PD mới được hoàn thành chương trình"; login CB PD + đợt BC còn TAO_DOT → block; CB PD + all DA_TONG_HOP → PASS |
| **BR-XI-RUT-TRINH-DUTHAO** | Rút trình CT: CHO_PHE_DUYET → **DU_THAO** (không phải HUY) — giữ nội dung để sửa rồi trình tiếp | srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:2600-2620 (Thay đổi 4 Phần 3 `[GAP-XI-01]`) | ✅ Yes (v3.5) | — | TC-12 — CB NV tạo CT trình → ấn Rút trình → verify state về DU_THAO + form còn data |
| **BR-XI-DOT-AUDIT-DATE** | DOT_BAO_CAO: 5 audit fields (`created_at`/`updated_at`/`created_by`/`updated_by`/`is_deleted`) + 3 trường `han_nop`/`tu_ngay`/`den_ngay` kiểu **date** (không datetime) | srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:2540-2560 (Thay đổi 3 `[SRS-FIX]`) | ✅ Yes (v3.5) | — | TC-13 (13-TC-dot-bc-audit-fields.md) — verify schema GET `/dot-bao-cao/{id}` trả 5 audit + 3 date string (`YYYY-MM-DD` không có `T00:00`); datepicker UI render ngày-tháng-năm KHÔNG có chọn giờ |
| **BR-XI-KY-BC-TT17** | BAO_CAO_CT_HTPL.ky_bao_cao enum khớp DOT_BAO_CAO: `SO_BO_6_THANG` / `SO_BO_NAM` / `TRON_NAM` (TT17/2025) | srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:2620-2635 (Thay đổi 7 `[GAP-XI-02]`) | ✅ Yes (v3.5) | — | TC-07 — dropdown kỳ BC chỉ 3 giá trị TT17; POST `ky_bao_cao=THANG` → reject 400 |
| **BR-XI-CT-CORE-FIELDS** | CHUONG_TRINH_HTPL: `muc_tieu`/`doi_tuong`/`thoi_gian_bat_dau` Bắt buộc Y (đồng bộ Inputs FR-XI-01) | srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:2614-2628 (Thay đổi 6 `[GAP-XI-03]`) | ✅ Yes (v3.5) | — | TC-01 — POST CT thiếu `muc_tieu` → reject + ERR-XI-01-01 |
| **BR-XI-EXPORT-EXCEL** | Xuất Excel DS CT: filter-aware + chặn >10K dòng + danh sách rỗng → INF | srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:2600-2614 (Thay đổi 5 `[GAP-XI-04]`) | ✅ Yes (v3.5) | — | TC-02 — Xuất Excel happy + boundary 10K + filter-aware + DS rỗng |
| **BR-XI-MODULE-RENAME** | Breadcrumb + Tiêu đề trang SCR-XI-01 = "Quản lý kế hoạch thực hiện CT HTPLDN" | srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:2510-2530 (Thay đổi 1 A-ITEM-13) | ✅ Yes (v3.5) | — | TC-01 happy — verify text Breadcrumb + Page title sau navigate |

> **Cross-cutting CR-01 verdict cho FR-15:** Entity v3 đã có `la_cong_bo: boolean` + `ngay_cong_bo: datetime` (srs-v3/srs-fr-15-ct-htpldn.md:1081-1082). CHANGELOG-v3-to-v3.5.md line 2508-2640 **KHÔNG list FR-15 rename `la_cong_bo` → `cong_khai`** — 8 thay đổi v3.5 không bao gồm CR-01 cho FR-15. **Verdict: FR-15 GIỮ `la_cong_bo` trong v3.5.** KHÔNG log bug nếu API trả `la_cong_bo` thay vì `cong_khai`. Chỉ FR-02/05/07 + biểu mẫu mới rename theo CR-01 (xem CHANGELOG ITEM-01).

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Severity |
|---|---|---|---|
| ERR-XI-01-01 | Thiếu trường CT bắt buộc khi tạo | "Vui lòng nhập đầy đủ thông tin bắt buộc" | ERROR |
| ERR-XI-01-02 | Sửa CT không ở `DU_THAO` | "Chỉ chỉnh sửa CT ở trạng thái Dự thảo" | ERROR |
| ERR-XI-01-03 | Xóa CT không ở `DU_THAO` | "Chỉ xóa CT ở trạng thái Dự thảo" | ERROR |
| ERR-XI-03-01 | Trình duyệt CT không ở `DU_THAO` | "CT không ở trạng thái cho phép trình duyệt" | ERROR |
| ERR-XI-04-01 | Duyệt CT không ở `CHO_PHE_DUYET` | "CT không ở trạng thái chờ phê duyệt" | ERROR |
| ERR-XI-04-02 | Từ chối CT không nhập lý do | "Vui lòng nhập lý do từ chối" | ERROR |
| ERR-XI-04-03 | CB PD khác cấp duyệt CT | "Bạn chỉ được phê duyệt CT cùng cấp" | ERROR |
| ERR-XI-05-01 | Công bố CT không ở `DA_DUYET` | "CT chưa được phê duyệt" | ERROR |
| ERR-XI-05-02 | API Cổng PLQG fail | "Không thể kết nối Cổng PLQG. Vui lòng thử lại" | ERROR |
| ERR-XI-05a-01 | Tạo Đợt BC khi CT không ở `DANG_THUC_HIEN`/`HOAN_THANH` | "Chỉ tạo đợt BC cho CT đang thực hiện hoặc đã hoàn thành" | ERROR |
| ERR-XI-05a-02 | Đợt BC trùng (CT + kỳ + khoảng TG) | "Đã tồn tại đợt báo cáo cho kỳ này" | ERROR |
| ERR-XI-05a-03 | Xóa Đợt BC không ở `TAO_DOT` | "Chỉ xóa đợt BC ở trạng thái Tạo đợt" | ERROR |
| ERR-XI-06-01 | Lập BC thiếu số liệu bắt buộc | "Vui lòng nhập đầy đủ số liệu bắt buộc" | ERROR |
| ERR-XI-07-01 | Trình BC chưa hoàn chỉnh | "Vui lòng hoàn chỉnh BC trước khi trình" | ERROR |
| ERR-XI-07a-01 | Duyệt BC không ở `CHO_DUYET_KQ` | "BC không ở trạng thái chờ duyệt kết quả" | ERROR |
| ERR-XI-07a-02 | Từ chối BC không nhập lý do | "Vui lòng nhập lý do từ chối" | ERROR |
| ERR-XI-07a-03 | CB PD khác cấp duyệt BC | "Bạn chỉ được phê duyệt BC cùng cấp" | ERROR |
| ERR-XI-08-01 | Gửi TW Đợt BC không ở `DA_DUYET_KQ` | "Đợt BC chưa được phê duyệt kết quả" | ERROR |
| ERR-XI-08-02 | User không phải BN/ĐP nhấn Gửi TW | "Chỉ đơn vị BN/ĐP mới gửi BC lên TW" | ERROR |
| ERR-XI-09-01 | TW tổng hợp không chọn BC | "Vui lòng chọn ít nhất 1 BC để tổng hợp" | ERROR |
| ERR-XI-09-02 | User không phải TW nhấn Tổng hợp | "Chỉ cấp TW mới tổng hợp BC" | ERROR |
| WRN-XI-09-01 | BC từ BN/ĐP dùng mẫu cũ | "BC từ {đơn vị} sử dụng mẫu cũ, cần chuyển đổi" | WARNING |
| INF-CT-TK-01 | Tìm kiếm không có kết quả | "Không tìm thấy chương trình phù hợp" | INFO |

> ⚠️ Message phải quote **nguyên văn** từ SRS. Khi test negative, expected message match exact — không "close enough" accept.

### 2.3 Permission Matrix (module-specific)

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md).

| Entity / Action | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | DN | NHT/CG/TVV |
|---|---|---|---|---|---|---|---|---|---|
| `CHUONG_TRINH_HTPL` — Read | R (all) | R (TW scope) | R (BN scope) | R (ĐP scope) | R (TW scope) | R (BN scope) | R (ĐP scope) | — | — |
| `CHUONG_TRINH_HTPL` — Create / Update / Delete (DU_THAO only) | CRUD (force-edit?) | CUD (TW) | CUD (BN) | CUD (ĐP) | — | — | — | — | — |
| `CHUONG_TRINH_HTPL` — Trình duyệt | — | T (TW) | T (BN) | T (ĐP) | — | — | — | — | — |
| `CHUONG_TRINH_HTPL` — Duyệt / Từ chối (BR-AUTH-05) | — | — | — | — | A (TW only) | A (BN only) | A (ĐP only) | — | — |
| `CHUONG_TRINH_HTPL` — Công bố / Hủy CB Cổng PLQG | — | C (TW) | C (BN) | C (ĐP) | — | — | — | — | — |
| `CHUONG_TRINH_HTPL` — Kích hoạt/Tạm dừng/Hoàn thành/Hủy | — | A (TW) | A (BN) | A (ĐP) | — | — | — | — | — |
| `DOT_BAO_CAO` — Create / Update / Delete (TAO_DOT only) | — | CUD (TW) | CUD (BN) | CUD (ĐP) | — | — | — | — | — |
| `BAO_CAO_CT_HTPL` — Lập BC | — | E (TW) | E (BN) | E (ĐP) | — | — | — | — | — |
| `BAO_CAO_CT_HTPL` — Trình duyệt BC | — | T (TW) | T (BN) | T (ĐP) | — | — | — | — | — |
| `BAO_CAO_CT_HTPL` — Duyệt KQ (BR-AUTH-05) | — | — | — | — | A (TW only) | A (BN only) | A (ĐP only) | — | — |
| `DOT_BAO_CAO` — Gửi TW (UC171) | — | ❌ ERR-XI-08-02 | S (BN→TW) | S (ĐP→TW) | — | — | — | — | — |
| `BAO_CAO_CT_HTPL` — TW tổng hợp + xuất file (UC172) | — | AGG (TW only) | ❌ ERR-XI-09-02 | ❌ ERR-XI-09-02 | — | — | — | — | — |

> Ghi chú: R=Read, C=Create, U=Update, D=Delete, T=Trình duyệt, A=Approve/Action, S=Send, E=Edit, AGG=Aggregate. Hành động "force-edit QTHT" ở BR-FLOW-03 → SPEC-CLARIFY (UI có nút không?).

### 2.4 UI Layout (SCR-XI-01)

**Components (trích từ SRS SCR-XI-01 — srs-v3/srs-fr-15-ct-htpldn.md:860-991):**

**Trang Danh sách CT (MH-15.1):**
- **Toolbar:** Breadcrumb "Trang chủ > Quản lý kế hoạch thực hiện CT HTPLDN" (v3.5 A-ITEM-13 — đổi tên từ "CT HTPLDN > Quản lý chương trình") + tiêu đề trang **"Quản lý kế hoạch thực hiện chương trình hỗ trợ pháp lý doanh nghiệp"** + nút `[+ Thêm KH]` `[Xuất Excel]` `[Làm mới]`.
- **Filter-bar:** Từ khóa (ten/ma) / Đơn vị (auto phân quyền BR-AUTH-05) / Trạng thái SM-KH-CTHTPL / Khoảng ngày (range).
- **Table:** Mã CT / Tên / Mục tiêu (cắt 100 ký tự) / Thời gian / Ngân sách / Đơn vị / Trạng thái (badge C06) / Số đợt BC / Hành động.
- **Pagination:** 20/page (BR-DATA-07).

**Trang Chi tiết CT — Tab "Thông tin":**
- Stepper 6 bước (`DU_THAO → CHO_PHE_DUYET → DA_DUYET → DA_CONG_BO → DANG_THUC_HIEN → HOAN_THANH`) — TAM_DUNG/HUY ẩn khỏi stepper nhưng vẫn ở enum 8 state.
- Form 8 trường (read-only nếu state ≠ `DU_THAO`): Mã CT (auto, read-only) / Tên / Mục tiêu / Thời gian BĐ-KT / Ngân sách / Đối tượng / Đơn vị (auto) / Ghi chú / File đính kèm.
- Action bar context-sensitive (theo state):
  - `DU_THAO`: `[Hủy]` `[Lưu nháp]` `[Gửi phê duyệt]` `[Hủy CT]`
  - `CHO_PHE_DUYET`: `[Phê duyệt]` `[Từ chối]` (chỉ CB PD cùng cấp)
  - `DA_DUYET`: `[Công bố]` `[Kích hoạt]`
  - `DA_CONG_BO`: `[Hủy công bố]` `[Kích hoạt]`
  - `DANG_THUC_HIEN`: `[Tạm dừng]` `[Hoàn thành]`
  - `TAM_DUNG`: `[Tiếp tục]`

**Trang Chi tiết CT — Tab "Đợt báo cáo":**
- Toolbar `[+ Tạo đợt mới]` (chỉ bật khi CT ở `DANG_THUC_HIEN`/`HOAN_THANH`) + `[Làm mới]`.
- Info-box deadline TT17/2025 (Sơ bộ 6T: ĐP/BN 10/06, TW 20/06. Sơ bộ năm: 10/11, 20/11. Tròn năm: 10/01, 20/01).
- Table Đợt BC (Mã / Tên / Kỳ / Biểu mẫu / Khoảng TG / Hạn nộp / Trạng thái SM-DOT-BC / Hành động).
- Modal tạo Đợt (Tên / Kỳ BC dropdown **3 giá trị TT17: `SO_BO_6_THANG`/`SO_BO_NAM`/`TRON_NAM` `[GAP-XI-02]`** / Biểu mẫu MAU_21A/21B/CA_HAI / **Hạn nộp datepicker DATE-ONLY** `[SRS-FIX]` / **Khoảng TG `tu_ngay`/`den_ngay` DATE-ONLY** `[SRS-FIX]` / Ghi chú). KHÔNG có ô chọn giờ-phút cho 3 trường ngày.
- Pagination 20/page.

**Drill-down Đợt BC (MH-15.6 + 15.7 + 15.8 đã gộp v2.1):**
- Card info (read-only) + Progress bar SM-DOT-BC 6 bước.
- Form biểu mẫu 21a/21b (editable table — Chỉ tiêu / Số liệu kỳ trước / Kỳ này / Ghi chú) + gợi ý số liệu từ HT (COUNT VV, SUM chi phí).
- Textarea nhận xét/kiến nghị max 5000 ký tự.
- Action bar context-sensitive:
  - `DANG_LAP_BC`: `[Hủy]` `[Lưu nháp]` `[Trình duyệt KQ]`
  - `CHO_DUYET_KQ`: `[Phê duyệt]` `[Từ chối]` (CB PD cùng cấp)
  - `DA_DUYET_KQ`: `[Gửi lên TW]` (BN/ĐP only)
  - `DA_GUI_TW`: hiển thị status, không action
- **[TW view]** Table BC từ BN/ĐP (filter `da_gui_tw=1`): checkbox / đơn vị / cấp / Mã đợt / Kỳ / Ngày gửi / Trạng thái + form Tổng hợp + `[Xuất Excel]` `[Xuất Word]` theo TT17.

**Cross-cutting features MẶC ĐỊNH có:**
- ☑ `[Xuất Excel]` toolbar DS CT (BR-DATA-06).
- ☑ Pagination 20/page (BR-DATA-07).
- ☑ Search keyword sanitize max 200 ký tự (BR-EC-13).
- ☑ URL sync filter (BR-UX-01) — SPEC-CLARIFY có quote SRS không, hay default global.
- ☑ Audit log mọi CUD + phê duyệt (BR-DATA-05).
- ☑ Optimistic lock mọi UPDATE/DELETE (BR-EC-01).

**Feature module KHÔNG có (cần QUOTE SRS hoặc SPEC-CLARIFY):**
- Import Excel CT/Đợt BC — SRS không quote (system-overview.md:981 ghi FR-15 ❌ Import Excel). KHÔNG test import.
- Hard delete v3.5 — SRS v3 quote soft delete BR-DATA-01, file update v3.5 KHÔNG list FR-15 → giữ soft delete. SPEC-CLARIFY nếu BA muốn ngược lại.

### 2.5 State Machine

**SM-KH-CTHTPL — Kế hoạch CT HTPLDN (8 state, srs-v3/srs-fr-15-ct-htpldn.md:1154-1192 + CHANGELOG v3.5 Thay đổi 4):**

```
       [*]
        │ CB NV tạo KH (UC160)
        ▼
   ┌─[DU_THAO]──[Hủy CT]──► [HUY]   (CB NV hủy khi còn DU_THAO)
   │     ▲ │
   │     │ │ CB NV trình
   │     │ ▼
   │     │ [CHO_PHE_DUYET]
   │     │     │ │ │
   │     │     │ │ └─ CB NV [Rút trình] ──► DU_THAO (v3.5 — giữ nội dung sửa lại)
   │     │     │ │
   │     │     │ └─ CB PD duyệt cùng cấp (BR-AUTH-05) ──► [DA_DUYET]
   │     │     ▼
   │     └── CB PD [Từ chối] (lý do ≥10 ký tự, về DU_THAO)
   │
   │  [DA_DUYET] ──[Công bố]──► [DA_CONG_BO] ──[Hủy công bố]──► [DA_DUYET]
   │       │                          │
   │       └──[Kích hoạt]──┬──────────┘
   │                       ▼
   │               [DANG_THUC_HIEN]
   │                   │  ▲
   │             Tạm   │  │ Tiếp tục (CB NV)
   │             dừng  ▼  │
   │             [TAM_DUNG]
   │                   │
   │             CB PD Hoàn thành (v3.5 — guard "Tất cả đợt BC đã hoàn thành")
   │                   ▼
   │              [HOAN_THANH]
```

**Bảng transition (full ở SRS:1178-1192 + v3.5 fix Thay đổi 4):**

| Từ | Đến | Actor | Trigger | Guard | FR Ref |
|---|---|---|---|---|---|
| [*] | DU_THAO | CB NV | Tạo KH | — | FR-XI-01 (UC160) |
| DU_THAO | CHO_PHE_DUYET | CB NV | [Gửi phê duyệt] | Đủ field Y (3 trường core `[GAP-XI-03]`) | FR-XI-03 (UC162) |
| CHO_PHE_DUYET | DA_DUYET | CB PD | [Phê duyệt] | Cùng cấp BR-AUTH-05 | FR-XI-04 (UC163) |
| CHO_PHE_DUYET | DU_THAO | CB PD | [Từ chối] | `ly_do` ≥10 ký tự BR-FLOW-04 | FR-XI-04 (UC163) |
| **CHO_PHE_DUYET** | **DU_THAO** ⚠️v3.5 fix | **CB NV** | **[Rút trình]** | **CB NV tạo ban đầu (giữ nội dung sửa lại — KHÔNG sang HUY)** | **FR-XI-01 `[GAP-XI-01]`** |
| DA_DUYET | DA_CONG_BO | CB NV | [Công bố] | API Cổng PLQG OK | FR-XI-05 (UC164) |
| DA_CONG_BO | DA_DUYET | CB NV | [Hủy công bố] | API gỡ Cổng | FR-XI-05 (UC164) |
| DA_DUYET / DA_CONG_BO | DANG_THUC_HIEN | CB NV | [Kích hoạt] | — | FR-XI-01 `[GAP-XI-01]` |
| DANG_THUC_HIEN | TAM_DUNG | CB NV | [Tạm dừng] | Có lý do | FR-XI-01 `[GAP-XI-01]` |
| TAM_DUNG | DANG_THUC_HIEN | CB NV | [Tiếp tục] | — | FR-XI-01 `[GAP-XI-01]` |
| **DANG_THUC_HIEN** | **HOAN_THANH** ⚠️v3.5 fix | **CB PD** | **[Hoàn thành]** | **Tất cả đợt BC đã hoàn thành (DA_TONG_HOP) + Lỗi "Chỉ CB PD mới được hoàn thành"** | **FR-XI-01 `[GAP-XI-01]`** |
| DU_THAO | HUY | CB NV | [Hủy CT] | — | FR-XI-01 `[GAP-XI-01]` |

**SM-DOT-BC — Đợt báo cáo (6 state, srs-v3/srs-fr-15-ct-htpldn.md:1194-1220):**

```
   [*]
    │ CB NV tạo (UC195, guard: CT ở DANG_THUC_HIEN/HOAN_THANH)
    ▼
[TAO_DOT]
    │ CB NV bắt đầu lập BC
    ▼
[DANG_LAP_BC]──────────────┐
    │ CB NV trình KQ       │ CB PD từ chối KQ (lý do)
    ▼                      │
[CHO_DUYET_KQ]─────────────┘
    │ CB PD duyệt cùng cấp (BR-AUTH-05)
    ▼
[DA_DUYET_KQ]
    │ CB NV BN/ĐP gửi TW (chỉ BN/ĐP)
    ▼
[DA_GUI_TW]
    │ CB NV TW tổng hợp
    ▼
[DA_TONG_HOP]
```

**Bảng transition (full ở SRS:1212-1220):**

| Từ | Đến | Actor | Trigger | Guard | FR Ref |
|---|---|---|---|---|---|
| [*] | TAO_DOT | CB NV | Tạo đợt | CT ở DANG_THUC_HIEN/HOAN_THANH (BR-XI-CT-STATE-DOT) | FR-XI-05a |
| TAO_DOT | DANG_LAP_BC | CB NV | Bắt đầu lập BC | Đợt đã đủ info | FR-XI-06 |
| DANG_LAP_BC | CHO_DUYET_KQ | CB NV | [Trình duyệt KQ] | BC đầy đủ số liệu | FR-XI-07 |
| CHO_DUYET_KQ | DA_DUYET_KQ | CB PD | [Duyệt KQ] | Cùng cấp BR-AUTH-05 | FR-XI-07a |
| CHO_DUYET_KQ | DANG_LAP_BC | CB PD | [Từ chối KQ] | Lý do ≥10 ký tự BR-FLOW-04 | FR-XI-07a |
| DA_DUYET_KQ | DA_GUI_TW | CB NV BN/ĐP | [Gửi TW] | Chỉ BN/ĐP BR-XI-BNDP-TO-TW | FR-XI-08 |
| DA_GUI_TW | DA_TONG_HOP | CB NV TW | [Tổng hợp] | ≥1 BC chọn BR-XI-TW-AGG-EMPTY | FR-XI-09 |

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|---|---|---|
| **GĐ1 Seed (pure entry state)** | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | `chuong_trinh_htpl_variants[1..6]` (cấp TW/BN/ĐP × kỳ × ngân sách) |
| **GĐ1 click flow** | [`input/flow-module.md`](../../../input/flow-module.md) | §FR-15 Bước 1 (thủ công UC164) |
| **GĐ2 Workflow** | [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) | §⑤ FR-15 GĐ1 (LỚP 2, 11 transition) + §⑭-bis FR-15 GĐ2 (LỚP 5, 7 transition) |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | `CHUONG_TRINH_HTPL`, `DOT_BAO_CAO`, `BAO_CAO_CT_HTPL` — "Tạo tại / Đọc tại" |

**Upstream dependencies (Tier check):**

| Entity của module | Tier | Phụ thuộc entity nào (upstream) | Seed trước tại module |
|---|---|---|---|
| `CHUONG_TRINH_HTPL` | 2 | `DON_VI` + `TAI_KHOAN` (CB NV + CB PD cùng cấp) | FR-10 Quản trị |
| `DOT_BAO_CAO` | 5 | `CHUONG_TRINH_HTPL` ở state `DANG_THUC_HIEN`/`HOAN_THANH` | FR-15 GĐ1 |
| `BAO_CAO_CT_HTPL` (BC kết quả) | 5 | `DOT_BAO_CAO` `DANG_LAP_BC` + số liệu `VU_VIEC`/`HO_SO_CHI_TRA DA_THANH_TOAN`/`KHOA_HOC HOAN_THANH` trong kỳ | FR-15 GĐ2 + FR-05 + FR-06 + FR-03 |
| `BAO_CAO_CT_HTPL` (loại TONG_HOP_TW) | 5 | ≥1 `DOT_BAO_CAO` `DA_GUI_TW` từ BN/ĐP | UC171 đã chạy |

> **Lưu ý:** KHÔNG hardcode `N records` ở đây — fixture chốt 6 variants/entity. Workflow advance state là việc GĐ2 (`workflow-test-report-fr-15.md`), không phải precondition.

---

## 3. Cấu Trúc File Test Case

```
fr-15-ct-htpldn/
├── test-plan.md                       ← File này (v1.1 revised v3.5)
├── 01-TC-crud-ct.md                   ← UC160 CRUD KH + BR-FLOW-03 + 3 trường core bắt buộc [GAP-XI-03] + verify Breadcrumb v3.5
├── 02-TC-search-ct.md                 ← UC161 Tìm kiếm + BR-EC-13 sanitize + Xuất Excel [GAP-XI-04] (5 step + 2 error + boundary 10K)
├── 03-TC-trinh-pd-ct.md               ← UC162 (trình duyệt KH)
├── 04-TC-pd-ct.md                     ← UC163 (CB PD duyệt/từ chối + BR-AUTH-05)
├── 05-TC-cong-bo-ct.md                ← UC164 (Công bố Cổng PLQG + rollback ERR-XI-05-02)
├── 06-TC-crud-dot-bc.md               ← UC165 (CRUD Đợt BC + BR-XI-DOT-DUP + state guard + datepicker DATE-ONLY)
├── 07-TC-lap-bc-21ab.md               ← UC166 (Lập BC 21a/21b + gợi ý số liệu + dropdown kỳ BC 3 giá trị TT17 [GAP-XI-02])
├── 08-TC-trinh-pd-bc.md               ← UC167 (trình duyệt BC KQ)
├── 09-TC-pd-bc.md                     ← UC168 (CB PD duyệt/từ chối BC + BR-AUTH-05)
├── 10-TC-gui-tw.md                    ← UC169 (BN/ĐP gửi TW + ERR-XI-08-02)
├── 11-TC-tw-tonghop.md                ← UC170 (TW tổng hợp + Xuất Excel/Word TT17)
├── 12-TC-lifecycle-actions.md         ← 🆕 v3.5 [GAP-XI-01] — 6 lifecycle: Kích hoạt/Tạm dừng/Tiếp tục/Hoàn thành (CB PD)/Hủy/Rút trình (DU_THAO)
├── 13-TC-dot-bc-audit-fields.md       ← 🆕 v3.5 [SRS-FIX] — verify 5 audit fields + 3 date-only field DOT_BAO_CAO
└── (14-REVIEW-edge-case-hunter.md)    ← Optional review
```

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Permission | Tổng |
|---|---|---|---|---|---|
| 01 — CRUD CT (UC160) | 2 | 3 | 1 | 1 | **7** |
| 02 — Tìm kiếm + Xuất Excel (UC161) | 1 | 3 | 2 | 0 | **6** |
| 03 — Trình PD CT (UC162) | 1 | 1 | 0 | 0 | **2** |
| 04 — CB PD duyệt CT (UC163) | 2 | 2 | 0 | 1 (cross-cấp) | **5** |
| 05 — Công bố Cổng PLQG (UC164) | 1 | 2 | 0 | 0 | **3** |
| 06 — CRUD Đợt BC (UC165) | 2 | 3 | 1 | 0 | **6** |
| 07 — Lập BC 21a/21b (UC166) | 1 | 2 | 1 | 0 | **4** |
| 08 — Trình PD BC (UC167) | 1 | 1 | 0 | 0 | **2** |
| 09 — CB PD duyệt BC (UC168) | 2 | 2 | 0 | 1 (cross-cấp) | **5** |
| 10 — Gửi TW (UC169) | 1 | 1 | 0 | 1 (TW gửi TW) | **3** |
| 11 — TW tổng hợp + Xuất file (UC170) | 1 | 2 | 1 | 1 (BN nhấn tổng hợp) | **5** |
| **12 — Lifecycle actions `[GAP-XI-01]`** (🆕 v3.5) | 6 (6 action happy) | 4 (CB NV ấn Hoàn thành / Rút trình về DU_THAO verify / state guard) | 1 | 1 (CB PD-only Hoàn thành) | **12** |
| **13 — DOT_BAO_CAO audit + date `[SRS-FIX]`** (🆕 v3.5) | 2 (schema + datepicker) | 2 (POST datetime → reject) | 1 | 0 | **5** |
| **TỔNG** | **23** | **28** | **7** | **6** | **65** |

> **Note nhóm B:** Test plan định nghĩa scope đầy đủ **65 TC** v3.5 (46 baseline + 17 mới `[GAP-XI-XX]`/`[SRS-FIX]`). Khi execute round QA cụ thể, **chọn sample 28-32 TC P0** ưu tiên cover 17 TC v3.5 mới + 11 happy core UC + BR-AUTH-05 cross-cấp. 65 TC còn dùng cho **regression suite định kỳ**.

**Phân bổ priority:**

| Priority | Số TC | % |
|---|---|---|
| P0 (bắt buộc — happy core UC160-UC170 + permission cross-cấp + 6 lifecycle action + DOT_BAO_CAO audit/date + 3 trường core CT + Hoàn thành CB PD + Rút trình DU_THAO + Breadcrumb v3.5 + enum kỳ BC) | 32 | 49% |
| P1 (quan trọng — negative state guard, ERR codes, rollback Cổng PLQG, Xuất Excel `[GAP-XI-04]`) | 25 | 38% |
| P2 (nên có — edge sanitize/SQL/XSS, boundary 10K Excel, 5000 ký tự nhận xét) | 8 | 12% |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md).

- ✅ **PASS:** 100% P0 + ≥90% P1 pass + cross-cutting CR-01 không break (la_cong_bo render đúng + audit ghi đủ).
- ❌ **FAIL:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%, hoặc CR-01 break entity (vd `la_cong_bo=true` mà GET API outbound `/chuong-trinh-htpl` không filter `DA_CONG_BO`).
- 🤷 **CẤM kết luận** khi: dropdown CT BN/ĐP trống ở SCR-XI-01 mà CHƯA verify (a) login đúng cấp, (b) seed CT đủ variant cấp tương ứng, (c) API `list_network_requests` 200 OK có data — phải retry method trước khi mark non-PASS.

---

## 6. Tham chiếu

- [output/test-strategy.md](../../../output/test-strategy.md) — chiến lược tổng thể.
- [output/scaling-test-strategy.md](../../../output/scaling-test-strategy.md) — quy trình 7 bước.
- [input/srs-v3/srs-fr-15-ct-htpldn.md](../../../input/srs-v3/srs-fr-15-ct-htpldn.md) — SRS module (1313 dòng).
- [input/srs-v3/srs-v3.md Phụ lục B](../../../input/srs-v3/srs-v3.md) — BR cross-cutting.
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md §⑤ + §⑭-bis](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — Transition GĐ1 + GĐ2.
- [tasks/system-overview.md §4.6 + §4.16](../../../tasks/system-overview.md) — Module 5 + Module 15 trong system overview.
- [output/permission-matrix.md](../../../output/permission-matrix.md) — ma trận phân quyền tổng.
- [output/template/test-case-template.md](../../../output/template/test-case-template.md) — template TC field-level.
- [output/template/bug-report-template.md](../../../output/template/bug-report-template.md) — template bug report.
- [input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md](../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) line 2508-2640 — 8 thay đổi v3.5 cho FR-15 (nhóm B DELTA+IMPACT).

---

*Test plan generated 2026-05-12. Revised 2026-05-12 12:35:00 — re-classified nhóm C → **B (DELTA+IMPACT)** sau review code-reviewer. Baseline SRS v3 + 8 thay đổi v3.5 cherry-pick từ v4 (A-ITEM-13 + A-ITEM-09 + B2d + 5×B1, ref CHANGELOG-v3-to-v3.5.md line 2508-2640). Fix chính: UC numbering 164-172/195-196 → UC160-UC170 contiguous; SM Hoàn thành actor = CB PD; SM Rút trình `CHO_PHE_DUYET → DU_THAO`; bổ sung TC-12 lifecycle + TC-13 audit/date; verdict FR-15 GIỮ `la_cong_bo` (CR-01 không áp). Sibling check: FR-11 Báo cáo (SM tương đương) + FR-05 Vụ việc (BR-AUTH-05 pattern).*
