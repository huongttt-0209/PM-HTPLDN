# Kế Hoạch Kiểm Thử — Theo dõi Đánh giá HQ HTPL (FR-08, SCR-VI-01)

> **Phiên bản**: 1.1 (Revised 2026-05-12 13:30:00 sau review REVISE)
> **Ngày tạo**: 2026-05-12
> **Revision note 2026-05-12 13:30:00:** Apply review feedback — sửa filter VV FR-VI-05 (HOAN_THANH ∪ DA_DANH_GIA, SRS:858), tách TC-DG-21 calc vs xếp loại, thêm TC FR-VI-10 mutation 403, thêm file 13-TC-data-migration.md, log SPEC-CLARIFY-FR08-05 `tan_suat` DOT_XUAT contradiction, +SPEC-CLARIFY-FR08-06 HUY guard 2 state CB PD, sửa TC permission QTHT×FR-VI-10, thêm BR-NOTIF-01 dedicated TC, mở rộng file_dinh_kem matrix, sửa cite prefix BR cross-cutting, làm rõ TC-DG-35 scope BR-AUTH-08.
> **Module letter**: L (Module 12 — Đánh giá HQ trong system-overview §4.13)
> **Source mode**: LOCAL (cite SRS line cụ thể với prefix path)
> **SRS Reference (v3.5):** `input/srs-update-2026-5-5/srs-fr-08-danh-gia.md` (FR-VI-01..10, SCR-VI-01)
> **Delta map**: `input/srs-update-2026-5-5/_DELTA-MAP-FR08.md`
> **Baseline cũ**: `input/srs-v3/srs-fr-08-danh-gia.md`
> **CHANGELOG**: `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` (line 880-1006)

> **Quy trình:** Theo [scaling-test-strategy.md §4.1 Bước 3](../../../output/scaling-test-strategy.md) — trích BR từ SRS Phụ lục B + sibling-check ≥2 module cùng nhóm + BA sign-off trước Bước 4.
>
> **v3.0 (2026-04-23):** Test plan này dùng cho **GĐ 3 Functional + Auth + Edge**. GĐ 1 Seed + GĐ 2 Workflow là 2 phase riêng, output `seed-checklist-{module}.md` + `workflow-test-report-{module}.md`. Happy path đã cover ở GĐ 2 — TC ở đây chỉ còn **negative + edge + auth + cross-module**.

> **⚠️ Lưu ý rename v3.5 (CR-10 / A-ITEM-08):**
> - Module name: "Kế hoạch đánh giá" → **"Theo dõi Đánh giá Hiệu quả Hỗ trợ Pháp lý"**
> - Entity: `DOT_DANH_GIA` + `DANH_GIA_HQ` → `KE_HOACH_DANH_GIA` (rename consolidate)
> - FK: `dot_danh_gia_id` → `ke_hoach_danh_gia_id` (9 vị trí FR-VI-02..09 + SCR-VI-01)
> - FR mới: **FR-VI-10** (Nhận kết quả ĐG, read-only CB NV thuộc `co_quan_duoc_danh_gia_id`)
> - State machine: 8 states canonical (loại bỏ tên cũ `NHAP/DA_LAP_KH/DA_DUYET_PC/DANG_DANH_GIA/DA_DANH_GIA/DA_LAP_BC/CHO_DUYET_BC/DA_DUYET_BC`)
> - Mọi reference tên cũ → migrate sang tên mới. Tester KHÔNG nhầm 2 module khác nhau.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- Module 12 — Theo dõi Đánh giá Hiệu quả HTPL (FR-08, Nhóm VI), 10 FR (FR-VI-01..10).
- Vòng đời 1 kế hoạch đánh giá: tạo KH → thiết lập tiêu chí (Σ trọng số = 100%) → phân công người ĐG → trình + duyệt PC → chọn VV (đã `HOAN_THANH` ở FR-05) → chấm điểm TT17 → sinh báo cáo → trình + duyệt BC → `HOAN_THANH` (hoặc `HUY` ở bất kỳ điểm nào).
- Bảng dữ liệu chính (owned): `KE_HOACH_DANH_GIA`, `KET_QUA_DANH_GIA`, `BAO_CAO_DANH_GIA`, `TIEU_CHI_DANH_GIA`.
- Bảng dữ liệu referenced: `VU_VIEC`, `TU_VAN_VIEN`, `TAI_KHOAN`, `DON_VI`.
- Màn hình: **SCR-VI-01** Consolidated v2.1 — 1 màn duy nhất gồm Phần A (Danh sách KH ĐG) + Phần B (Chi tiết KH, 4 tab: Tiêu chí / Phân công / Thực hiện chấm điểm / Báo cáo) — `srs-update-2026-5-5/srs-fr-08-danh-gia.md:785-887`.
- Mẫu báo cáo: Mẫu 21a / 21b TT17/2025 (xuất Word/PDF + Excel).

### 1.2 Danh sách FR / UC

| # | Mã FR | UC | Tên chức năng | Entity chính | Tab SCR-VI-01 |
|---|-------|----|---------------|--------------|---------------|
| 1 | FR-VI-01 | UC83 | Lập kế hoạch đánh giá | `KE_HOACH_DANH_GIA` (entry state `LAP_KE_HOACH`) | Phần A — Form tạo/sửa |
| 2 | FR-VI-02 | UC84 | Thiết lập tiêu chí đánh giá (Σ trọng số = 100%) | `TIEU_CHI_DANH_GIA` | Tab 1 — Tiêu chí |
| 3 | FR-VI-03 | UC85 | Phân công người đánh giá | `PHAN_CONG_DANH_GIA` ⚠️ entity chưa list trong §4 SRS line 893-1109 (chỉ 4 owned: `KE_HOACH_DANH_GIA/KET_QUA_DANH_GIA/BAO_CAO_DANH_GIA/TIEU_CHI_DANH_GIA`). Có thể là sub-table inline trong KH (JSON assignees) — TC-DG-09/10/11 phải verify DB schema thực tế. Log SPEC-CLARIFY-FR08-08. | Tab 2 — Phân công |
| 4 | FR-VI-04 | UC86 | Phê duyệt phân công | `KE_HOACH_DANH_GIA.trang_thai` | Tab 2 — Action Phê duyệt PC |
| 5 | FR-VI-05 | UC87 | Chọn vụ việc đánh giá (VV `HOAN_THANH`) | `KET_QUA_DANH_GIA` | Tab 3 — Section Chọn VV |
| 6 | FR-VI-06 | UC88 | Thực hiện đánh giá / chấm điểm TT17 | `KET_QUA_DANH_GIA` | Tab 3 — Bảng chấm điểm |
| 7 | FR-VI-07 | UC89 | Lập báo cáo đánh giá | `BAO_CAO_DANH_GIA` | Tab 4 — Báo cáo |
| 8 | FR-VI-08 | UC90 | Trình phê duyệt báo cáo | `KE_HOACH_DANH_GIA.trang_thai → CHO_PHE_DUYET` | Tab 4 — Action |
| 9 | FR-VI-09 | UC91 | Phê duyệt báo cáo đánh giá | `KE_HOACH_DANH_GIA.trang_thai → HOAN_THANH` | Tab 4 — Action Phê duyệt BC |
| 10 | FR-VI-10 `[NEW v3.5][GAP-VI-04][CR-10]` | — (chưa gán UC, gắn GAP-VI-04) | Nhận kết quả đánh giá (read-only) | Read on 3 owned entities | Tab Báo cáo (read-only) |

### 1.3 Tài khoản & role liên quan

Reference: [`input/users.csv`](../../../input/users.csv).

| Role | Cấp | Username primary | Dùng cho TC loại |
|------|-----|------------------|-------------------|
| QTHT | — | `qtht_01` | Admin / cross-cutting / xem mọi đơn vị (BR-AUTH-03 ngoại lệ) |
| CB_NV_TW | TW | `cb_nv_tw_01` | FR-VI-01/02/03/05/06/07/08 — tạo KH, phân công, chấm điểm, lập BC, trình duyệt (scope TW) |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH) | FR-VI-01..08 scope BN, test cross-unit isolation |
| CB_NV_DP | ĐP | `cb_nv_dp_01` (AG) | FR-VI-01..08 scope ĐP |
| CB_PD_TW | TW | `cb_pd_tw_01` | FR-VI-04 (duyệt PC) + FR-VI-09 (duyệt BC), BR-AUTH-05 cùng cấp TW |
| CB_PD_BN | BN | `cb_pd_bn_01` (BKH) | FR-VI-04 / FR-VI-09 scope BN |
| CB_PD_DP | ĐP | `cb_pd_dp_01` (AG) | FR-VI-04 / FR-VI-09 scope ĐP |
| CB_NV_* (cơ quan ĐƯỢC ĐG) | bất kỳ | role-mapped per `co_quan_duoc_danh_gia_id` | **FR-VI-10 read-only mới v3.5** — CB NV của cơ quan được ĐG (có thể KHÁC `don_vi_id` cơ quan thực hiện ĐG) |
| TVV / CG / DN / NHT | — | `huongcg`, `nht_01`, `9999999990` | Permission negative — không có quyền vào SCR-VI-01 (403) |

> Fallback rule (CLAUDE.md §Rule 7): khi `_01` lock → thử `_02` → `_03` cùng `vai_tro` + `don_vi_ma`. Hết sibling → STOP, báo user.

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> ⚠️ **Quy định điền bảng:**
> - Cột "Ngoại lệ SRS-quoted": chỉ điền khi SRS có dòng ngoại lệ cụ thể (quote nguyên văn + link line).
> - Để trống nếu không có ngoại lệ — nghĩa là **BR áp dụng 100%** cho module này.
> - **KHÔNG** viết "KHÔNG áp dụng cho module X" nếu không có SRS quote → thay bằng SPEC-CLARIFY ticket.

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|---------------------|---------------------|-----------|
| BR-AUTH-01 | Xác thực truy cập (login + JWT) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1181`, `:1191-1195` | ✅ Yes — FR-VI-01..10 | — | Precondition mọi TC + FR-VI-10 access check |
| BR-AUTH-03 | Ngang cấp KHÔNG thấy nhau (cross-unit isolation) | `srs-v3/srs-v3.md:3951` | ✅ Yes | "QTHT thấy tất cả" | TC permission cross-unit (CB_NV_BN BKH vs BTC) |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB PD cùng cấp với CB NV trình) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1182`, `:1197-1201` | ✅ Yes — FR-VI-04, FR-VI-09 | — | TC PD cùng cấp + reject xuyên cấp (CB PD TW duyệt KH BN → 403) |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` (2-tier TW/BN, BN không có ĐP trực thuộc v3.5) | `srs-v3/srs-v3.md:3958` | ✅ Yes | — | TC scope KH theo `don_vi_id`; dropdown người ĐG lọc cùng đơn vị |
| BR-CALC-04 | **Tổng trọng số tiêu chí = 100%**. Điểm tổng = SUM(diem_i × trong_so_i / 100) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1186`, `:1221-1225` | ✅ Yes — FR-VI-02, FR-VI-06 | Cho lưu nháp khi != 100% nhưng WARNING; **BẮT BUỘC = 100% khi chuyển `CHO_DUYET_PC`** (`:881`) | TC edge case trọng số 99% / 101% / 100.01% / tolerance ±0.01% |
| BR-DATA-03 | Common fields (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1183`, `:1203-1207` | ✅ Yes — FR-VI-01 | — | TC verify entity tạo có đủ 7 common fields |
| BR-DATA-04 | Auto-gen mã đợt: **DG-{YYYYMMDD}-{SEQ}** | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1184`, `:1209-1213`, `:118` | ✅ Yes — FR-VI-01 | — | TC verify mã tự sinh đúng format khi tạo KH |
| BR-DATA-05 | Audit trail CUD + phê duyệt (immutable) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1185`, `:1215-1219` | ✅ Yes — FR-VI-01..10 | — | TC AUDIT_LOG INSERT khi tạo/sửa/xóa/duyệt KH |
| BR-DATA-06 | Export Excel max 10k rows | `srs-v3/srs-v3.md:3977` | ✅ Yes (default) | — | TC xuất Excel danh sách + Tab Báo cáo Excel/Word |
| BR-DATA-07 | Pagination default 20, max 100 | `srs-v3/srs-v3.md:3978`, ref SCR-VI-01 `:815` "20 mục/trang" | ✅ Yes | — | TC pagination boundary |
| BR-EC-01 | Optimistic Locking — `updated_at` conflict → ERR-SYS-02 | `srs-v3/srs-v3.md:4066` | ✅ Yes | — | TC 2 user sửa tiêu chí cùng lúc |
| BR-EC-13 | Search sanitize max 200 ký tự | `srs-v3/srs-v3.md:4078` | ✅ Yes | — | TC search SQL/XSS/long query trên Phần A filter-bar |
| BR-FLOW-04 | **Từ chối yêu cầu lý do** (≥10 ký tự) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1187`, `:1227-1231` | ✅ Yes — FR-VI-04 (từ chối PC), FR-VI-09 (từ chối BC) | — | TC reject + missing reason / reject + reason 9 chars (negative) |
| BR-LEGAL-08 | Tần suất ĐG: **sơ bộ 6 tháng + tròn năm**. KHÔNG cho đột xuất | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1188`, `:1233-1237` | ⚠️ **Defer SPEC-CLARIFY-FR08-05** — line 1006 DB CHECK CỘt vẫn cho phép `DOT_XUAT` (`('SO_BO_6_THANG','TRON_NAM','DOT_XUAT')`) trong khi BR-LEGAL-08 line 1235 cấm. 2 vị trí SRS mâu thuẫn nội bộ. BA chốt giữ/xoá `DOT_XUAT` trước khi viết TC negative. | — | TC tạo KH với `tan_suat` ngoài enum → ERR (defer đến khi BA chốt) |
| BR-NOTIF-01 | Gửi thông báo kết quả phê duyệt (CB NV) — **mở rộng v3.5 lên 4 FR** (FR-VI-03, 04, 08, 09) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1189`, `:1239-1243`, delta map line 50 | ✅ Yes — FR-VI-03/04/08/09 | v3 cũ chỉ FR-VI-09 → **v3.5 thêm FR-VI-03 + 04 + 08** | TC verify gửi TB đúng 4 thời điểm: trình PC / duyệt PC / trình BC / duyệt BC |
| BR-VI-08-01 (module-specific) | KH ĐG có **2 vai trò cơ quan tách bạch**: `don_vi_id` = cơ quan thực hiện ĐG, `co_quan_duoc_danh_gia_id` = cơ quan được ĐG (1:1, BẮT BUỘC v3.5, có thể KHÁC nhau) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:919`, `:1017`, delta map line 51-52 | ✅ Yes | — | TC FR-VI-10 cross-unit read + TC create KH thiếu `co_quan_duoc_danh_gia_id` |
| BR-VI-08-02 | File đính kèm KH ĐG (CR-07): `file_dinh_kem[]`, PDF/DOC/DOCX/XLS/XLSX, ≤20MB/file, optional | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1016` | ✅ Yes — FR-VI-01 | — | TC upload file valid + edge case >20MB / sai định dạng |
| BR-VI-08-03 | Chọn VV: lấy `trang_thai ∈ {HOAN_THANH, DA_DANH_GIA}` + `ngay_hoan_thanh ∈ [tu_ngay, den_ngay]` của KH + scope `don_vi_id` user | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:858` ("vụ việc có trạng thái Hoàn thành hoặc Đã đánh giá, trong kỳ đợt ĐG"), system-overview `:603` | ✅ Yes — FR-VI-05 | "Nếu VV đã ở KH khác (DA_DANH_GIA), cảnh báo nhưng vẫn cho phép chọn lại" (system-overview `:834`) — VV `DA_DANH_GIA` là pattern bình thường, không phải edge | TC dropdown hiện VV `HOAN_THANH` + `DA_DANH_GIA` + edge case VV `DANG_XU_LY` KHÔNG xuất hiện |
| BR-VI-08-04 | Xếp loại điểm: ≥90% Xuất sắc / ≥70% Tốt / ≥50% Đạt / <50% Chưa đạt | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:860` | ✅ Yes — FR-VI-06 | — | TC boundary calculation 89.9% / 90% / 70% / 50% / 49.9% |
| BR-EC-VI-08-05 | UNIQUE(`ke_hoach_id`, `vu_viec_id`) trong KET_QUA_DANH_GIA — không chấm trùng | inferred từ `srs-update-2026-5-5/srs-fr-08-danh-gia.md:922-930` ERD + `:858` (multi-select VV) | ✅ Yes — FR-VI-06 | — | TC chọn cùng VV 2 lần trong cùng KH → conflict / merge |
| BR-VI-08-06 (cross-cutting C1 v3.5) | **Hard-delete** (bỏ trạng thái `DA_XOA`): DELETE soft → DELETE thật + AUDIT_LOG ghi | system-overview `:845` (C1) | ⚠️ **Cần verify** — entity field line 1015 vẫn có `is_deleted boolean DEFAULT 0` + SM line 1167 ghi HUY = "Audit, soft-delete". C1 cross-cutting có override field-level không, hoặc đổi label. Log SPEC-CLARIFY-FR08-07. | — | TC xóa KH `LAP_KE_HOACH` → verify record DELETE thật (DB query) hoặc soft-flag (defer đến khi clarify) |
| BR-VI-08-07 (cross-cutting CR-01 v3.5) | 5 trường công khai chuyên trang (CR-01) — KH ĐG **PENDING** (delta map §6 T4): defer hỏi BA xem FR-08 có thuộc 12 DS công khai không | `_DELTA-MAP-FR08.md:120` (T4 PENDING) | ⏸️ Defer | — | SPEC-CLARIFY-FR08-01: BA confirm FR-08 có cong_khai/anh_dai_dien/thoi_gian_dang_tai/mo_ta_cong_khai/file_dinh_kem_cong_khai không |

### 2.2 Error Codes

| Mã lỗi | FR / Điều kiện trigger | Message (SRS-quoted) | Severity |
|--------|------------------------|----------------------|----------|
| ERR-DG-KH-01 | FR-VI-01 — Thiếu trường bắt buộc | "Vui lòng nhập đầy đủ thông tin bắt buộc" | ERROR |
| ERR-DG-KH-02 | FR-VI-01 — `tu_ngay >= den_ngay` | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |
| ERR-DG-TC-01 | FR-VI-02/06 — Tổng trọng số ≠ 100% khi chuyển trạng thái (tolerance ±0.01%) | "Tổng trọng số phải bằng 100%" | ERROR |
| ERR-DG-TC-02 | FR-VI-02/06 — Thiếu tên tiêu chí / sửa tiêu chí khi đang chấm điểm | "Vui lòng nhập tên tiêu chí" / "Không thể sửa tiêu chí khi đợt đang đánh giá" | ERROR |
| ERR-DG-TC-03 | FR-VI-02 — Điểm tối đa ≤ 0 | "Điểm tối đa phải lớn hơn 0" | ERROR |
| ERR-DG-PC-01 | FR-VI-03 — Không có người ĐG | "Vui lòng phân công ít nhất 1 người" | ERROR |
| ERR-DG-PC-02 | FR-VI-03 — Không có TRƯỞNG NHÓM | "Cần ít nhất 1 người vai trò Trưởng nhóm" | ERROR |
| ERR-DG-PC-03 | FR-VI-03 — Người trùng lặp | "Người đánh giá đã được phân công" | ERROR |
| ERR-DG-PC-04 | FR-VI-03 — KH không ở `PHAN_CONG` | "Đợt không ở trạng thái phù hợp để phân công" | ERROR |
| ERR-DG-PD-01 | FR-VI-04 — KH không ở `CHO_DUYET_PC` | "Đợt không ở trạng thái chờ duyệt phân công" | ERROR |
| ERR-DG-PD-02 | FR-VI-04 — Từ chối thiếu lý do (BR-FLOW-04) | "Vui lòng nhập lý do từ chối (tối thiểu 10 ký tự)" | ERROR |
| ERR-DG-VV-01 | FR-VI-05 — KH không ở `THUC_HIEN` | "Đợt không ở trạng thái phù hợp" | ERROR |
| ERR-DG-DG-01 | FR-VI-06 — Điểm vượt điểm tối đa | "Điểm phải từ 0 đến {max}" | ERROR |
| ERR-DG-BC-01 | FR-VI-07 — KH không ở `BAO_CAO` | "Đợt chưa hoàn thành đánh giá" | ERROR |
| ERR-DG-TR-01 | FR-VI-08 — KH không ở `BAO_CAO` khi trình BC | "Đợt không ở trạng thái đã lập BC" | ERROR |
| ERR-DG-PD-03 | FR-VI-09 — KH không ở `CHO_PHE_DUYET` | "Đợt không ở trạng thái chờ duyệt BC" | ERROR |
| ERR-DG-PD-04 | FR-VI-09 — Từ chối BC thiếu lý do | "Vui lòng nhập lý do từ chối (tối thiểu 10 ký tự)" | ERROR |
| ERR-DG-10 | FR-VI-10 — User không thuộc `co_quan_duoc_danh_gia_id` | "Bạn không có quyền xem kết quả đánh giá này" | ERROR |
| ERR-DG-11 | FR-VI-10 — KH chưa `HOAN_THANH` | "Kết quả đánh giá chưa hoàn thành" | ERROR |
| WRN-TC-01 | FR-VI-02 — Tổng trọng số ≠ 100% (warning UI) | "Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100%" | WARN |
| ERR-SYS-02 | BR-EC-01 — Optimistic lock conflict | "Bản ghi đã thay đổi bởi user khác. Tải lại trang" | ERROR |

> ⚠️ Message phải quote nguyên văn từ SRS. Khi test negative, expected message match exact — KHÔNG "close enough" accept.

### 2.3 Permission Matrix (module-specific)

> Reference: [`output/permission-matrix.md`](../../../output/permission-matrix.md).

| Entity / Action | QTHT | CB_NV (don_vi thực hiện ĐG) | CB_NV (`co_quan_duoc_danh_gia_id`) v3.5 | CB_PD (cùng cấp) | TVV/CG | NHT | DN |
|-----------------|:----:|:--:|:--:|:--:|:--:|:--:|:--:|
| `KE_HOACH_DANH_GIA` Create (FR-VI-01) | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| `KE_HOACH_DANH_GIA` Read (Phần A list + Phần B detail) | ✅ all | ✅ scope `don_vi_id` | ✅ R-only khi `HOAN_THANH` (FR-VI-10) | ✅ scope cùng cấp | ❌ 403 | ❌ 403 | ❌ 403 |
| `KE_HOACH_DANH_GIA` Update / Delete (FR-VI-01) | ✅ | ✅ chỉ khi `LAP_KE_HOACH`/`PHAN_CONG` | ❌ R-only | ❌ chỉ approve action | ❌ | ❌ | ❌ |
| `TIEU_CHI_DANH_GIA` CRUD (FR-VI-02) | ✅ | ✅ owner KH | ❌ | ❌ | ❌ | ❌ | ❌ |
| `PHAN_CONG_DANH_GIA` Create/Update/Delete (FR-VI-03) | ✅ | ✅ owner KH | ❌ | ❌ | ❌ | ❌ | ❌ |
| Action [Trình duyệt PC] (FR-VI-03 → `CHO_DUYET_PC`) | ✅ | ✅ owner KH | ❌ | ❌ | ❌ | ❌ | ❌ |
| Action [Phê duyệt PC] / [Từ chối PC] (FR-VI-04) | ✅ | ❌ | ❌ | ✅ cùng cấp BR-AUTH-05 | ❌ | ❌ | ❌ |
| `KET_QUA_DANH_GIA` Create/Update (FR-VI-05/06 chấm điểm) | ✅ | ✅ owner KH | ❌ | ❌ | ❌ | ❌ | ❌ |
| `BAO_CAO_DANH_GIA` Create/Update (FR-VI-07 lập BC) | ✅ | ✅ owner KH | ❌ R-only khi `HOAN_THANH` | ❌ | ❌ | ❌ | ❌ |
| Action [Trình duyệt BC] (FR-VI-08) | ✅ | ✅ owner KH | ❌ | ❌ | ❌ | ❌ | ❌ |
| Action [Phê duyệt BC] / [Từ chối BC] (FR-VI-09) | ✅ | ❌ | ❌ | ✅ cùng cấp BR-AUTH-05 | ❌ | ❌ | ❌ |
| **FR-VI-10 Tab Báo cáo read-only (khi KH `HOAN_THANH`)** | ✅ | ✅ (đã có Read) | ✅ NEW v3.5 — R-only KE_HOACH_DANH_GIA + KET_QUA_DANH_GIA + BAO_CAO_DANH_GIA | ✅ (đã có Read) | ❌ | ❌ | ❌ |

> **Tổng số role ≥ 6**: QTHT, CB_NV, CB_NV-được-ĐG (FR-VI-10), CB_PD, TVV/CG, NHT, DN — đủ 7 nhóm cho coverage permission matrix.

### 2.4 UI Layout (SCR-VI-01 Consolidated v2.1)

> ⚠️ **CẢNH BÁO:** Visual spec components từ SRS `srs-update-2026-5-5/srs-fr-08-danh-gia.md:785-887` (Phần A list + Phần B 4 tab + action buttons).
> KHÔNG dùng absence (UI spec không list X) để khẳng định "module KHÔNG có X". Mọi feature không có trên UI phải đối chiếu §2.1 BR table trước.

**Phần A — Danh sách kế hoạch đánh giá** (`:792-815`):
- **Toolbar**: Breadcrumb "Trang chủ > Đánh giá > Theo dõi đánh giá hiệu quả HTPL" + nút [+ Tạo đợt đánh giá] [Xuất Excel] [Làm mới]. [+ Tạo] chỉ khi role có quyền.
- **Filter-bar**: Search (tên / mã đợt) + Lọc tần suất (Tất cả / SO_BO_6_THANG / TRON_NAM) + Lọc đối tượng (VU_VIEC / DAO_TAO / TONG_HOP) + Lọc trạng thái (8 states + Tất cả) + Khoảng ngày.
- **Table** (`:804-815`): Checkbox / Mã đợt (link → chi tiết) / Tên đợt / Tần suất / Đối tượng / Kỳ ĐG / **Trạng thái badge 8 màu** (Xám LAP_KE_HOACH, Xanh dương PHAN_CONG, Cam CHO_DUYET_PC, Vàng THUC_HIEN, Xanh dương đậm BAO_CAO, Cam đậm CHO_PHE_DUYET, Xanh lá HOAN_THANH, Đỏ HUY) / Người tạo / Ngày tạo / Hành động (Xem / Sửa chỉ `LAP_KE_HOACH`+`PHAN_CONG` / Xóa chỉ `LAP_KE_HOACH`).
- **Action-bar batch**: "Đã chọn {N} mục" + [Xóa hàng loạt] khi ≥1 checkbox.
- **Pagination**: 20 mục/trang (BR-DATA-07).

**Phần B — Form tạo/sửa KH** (`:821-827`): Tên đợt / Mục tiêu (Rich Text) / Tần suất / Từ ngày + Đến ngày / Đối tượng / Ghi chú / **+ `co_quan_duoc_danh_gia_id`** (dropdown DON_VI cùng cấp/cấp dưới) / **+ `file_dinh_kem[]`** (CR-07, ≤20MB).

**Tab 1 — Tiêu chí** (`:831-841`): Bảng tiêu chí editable (Tên / Mô tả / **Trọng số %** / Điểm tối đa / Thứ tự drag-drop / Sửa-Xóa) + Label realtime tổng trọng số (🟢 = 100% / 🔴 ≠ 100%) + Alert banner WRN-TC-01 + Link tham chiếu DM tiêu chí (UC109) + [+ Thêm tiêu chí] / [Nhập từ DM].

**Tab 2 — Phân công** (`:845-852`): Bảng phân công (Người ĐG / Vai trò DANH_GIA_VIEN/TRUONG_NHOM / Lĩnh vực phụ trách / Ghi chú) + [+ Thêm người ĐG] + [Lưu nháp] + [Trình phê duyệt → `CHO_DUYET_PC`] + [Phê duyệt PC → `THUC_HIEN`] (CB PD only) + [Từ chối PC → `PHAN_CONG`] (CB PD, modal lý do ≥10 ký tự).

**Tab 3 — Thực hiện chấm điểm** (`:856-862`): Multi-select VV `HOAN_THANH` trong kỳ + Bảng chấm điểm inline (Mã VV / Tên DN / Lĩnh vực / 1 cột/tiêu chí input 0-`diem_toi_da` / **Điểm tổng auto = Σ điểm × trọng số / 100** / Nhận xét) + KPI cards (số VV đã chấm / Điểm TB / Xếp loại) + [Lưu kết quả] + [Hoàn tất chấm điểm → `BAO_CAO`].

**Tab 4 — Báo cáo** (`:866-875`): KPI cards (tổng VV / điểm TB / tỷ lệ SLA) + Bảng tổng hợp readonly + Biểu đồ Radar + Bar + Nhận xét chung + [Trình duyệt BC → `CHO_PHE_DUYET`] + [Phê duyệt BC → `HOAN_THANH`] (CB PD) + [Từ chối BC → `BAO_CAO`] (CB PD) + [Xuất XLSX] + [Xuất DOCX] theo mẫu 21a/21b TT17/2025.

**Cross-cutting features MẶC ĐỊNH có** (theo BR global):
- ☐ [Xuất Excel] toolbar (BR-DATA-06).
- ☐ Pagination 20/page (BR-DATA-07).
- ☐ Search sanitize max 200 chars (BR-EC-13).
- ☐ Audit log mọi CUD + approve action (BR-DATA-05).
- ☐ Optimistic lock UPDATE/DELETE (BR-EC-01).
- ☐ Hard-delete C1 v3.5 (BR-VI-08-06): xóa KH ở `LAP_KE_HOACH` → DELETE thật.

**Feature module CẦN SPEC-CLARIFY:**
- 5 trường công khai chuyên trang CR-01 (`cong_khai`/`anh_dai_dien`/`thoi_gian_dang_tai`/`mo_ta_cong_khai`/`file_dinh_kem_cong_khai`): PENDING BA — defer (`_DELTA-MAP-FR08.md:120`).

### 2.5 State Machine — SM-DANHGIA (8 states v3.5 canonical)

> **Source of truth:** `srs-update-2026-5-5/srs-fr-08-danh-gia.md:56-71` (§1) + `:1117-1167` (§5) + system-overview `:825-840`.
> **Resolved 2026-05-06 (Thay đổi 5, GAP-VI-01):** v3 cũ có 3 phiên bản state mâu thuẫn (6/7/9 state). v3.5 chốt **8 state canonical**. Bỏ tên cũ `NHAP/DA_LAP_KH/DA_DUYET_PC/DANG_DANH_GIA/DA_DANH_GIA/DA_LAP_BC/CHO_DUYET_BC/DA_DUYET_BC`. DB enum CHECK = SM state. Default = `LAP_KE_HOACH`.

**Diagram (text):**

```
[*]
  │ CB NV tạo KH (FR-VI-01, UC83)
  ▼
[LAP_KE_HOACH]  ──┬─→ phân công người ĐG (FR-VI-03, UC85) ──→ [PHAN_CONG]
                  └─→ XOA hard-delete (BR-VI-08-06)
[PHAN_CONG]     ──→ Trình duyệt PC (FR-VI-03) ──→ [CHO_DUYET_PC]
[CHO_DUYET_PC]  ──┬─→ CB PD duyệt (FR-VI-04, UC86) ──→ [THUC_HIEN]
                  └─→ CB PD từ chối (FR-VI-04, BR-FLOW-04) ──→ [PHAN_CONG]
[THUC_HIEN]     ──→ Chọn VV (FR-VI-05, UC87) + Chấm điểm xong tất cả VV (FR-VI-06, UC88) ──→ [BAO_CAO]
[BAO_CAO]       ──→ Lập BC (FR-VI-07, UC89) + Trình duyệt BC (FR-VI-08, UC90) ──→ [CHO_PHE_DUYET]
[CHO_PHE_DUYET] ──┬─→ CB PD duyệt BC (FR-VI-09, UC91) ──→ [HOAN_THANH]
                  └─→ CB PD từ chối BC (FR-VI-09, BR-FLOW-04) ──→ [BAO_CAO]
[HOAN_THANH]    ──→ Read-only (FR-VI-10 v3.5, CB NV `co_quan_duoc_danh_gia_id` xem được)
[*bất kỳ*]      ──→ Hủy đợt (FR-VI-04/06 admin override) ──→ [HUY]  ← NEW v3.5
```

**State × Color × Action transition table** (`:801`, `:810`):

| State | Màu badge | Action chính | FR | Actor | Transition → |
|-------|-----------|--------------|----|----|--------------|
| `LAP_KE_HOACH` (default) | Xám | Sửa / Phân công / Xóa hard | FR-VI-01/03 | CB NV | `PHAN_CONG` hoặc HUY |
| `PHAN_CONG` | Xanh dương | Trình duyệt PC | FR-VI-03 | CB NV | `CHO_DUYET_PC` hoặc HUY |
| `CHO_DUYET_PC` | Cam | Phê duyệt PC / Từ chối PC | FR-VI-04 | CB PD | `THUC_HIEN` hoặc `PHAN_CONG` hoặc HUY |
| `THUC_HIEN` | Vàng | Chọn VV + Chấm điểm | FR-VI-05/06 | CB NV | `BAO_CAO` hoặc HUY |
| `BAO_CAO` | Xanh dương đậm | Lập BC + Trình duyệt BC | FR-VI-07/08 | CB NV | `CHO_PHE_DUYET` hoặc HUY |
| `CHO_PHE_DUYET` | Cam đậm | Phê duyệt BC / Từ chối BC | FR-VI-09 | CB PD | `HOAN_THANH` hoặc `BAO_CAO` hoặc HUY |
| `HOAN_THANH` | Xanh lá | Read-only (FR-VI-10 v3.5) | FR-VI-10 | CB NV `co_quan_duoc_danh_gia_id` | (terminal) |
| `HUY` | Đỏ | (terminal) — không cho restore | — | — | (terminal) |

### 2.6 Data dependencies & Seed / Workflow input (v3.0)

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| GĐ 1 Seed (entry state) | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | Block `ke_hoach_danh_gia_variants` (rename từ `dot_danh_gia_variants` v3.5) |
| GĐ 1 click flow | [`input/quy-trinh-nghiep-vu/flow-module.md`](../../../input/quy-trinh-nghiep-vu/flow-module.md) | §FR-08 / SM-DANHGIA Bước 1 (CB NV tạo KH thủ công) |
| GĐ 2 Workflow | [`input/quy-trinh-nghiep-vu/flow-module.md`](../../../input/quy-trinh-nghiep-vu/flow-module.md) | §FR-08 flow Bước 1 → 9 (8 state transition + HUY) |
| Cross-module map | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | `KE_HOACH_DANH_GIA` "Tạo tại / Đọc tại" (rename từ `DOT_DANH_GIA`) |
| Thứ tự module | [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) `:795-840` | FR-08 § ⑬ — 8 state SM + 2 vai trò cơ quan + FR-VI-10 |

**Upstream dependencies (Tier check):**

| Entity của module | Tier | Phụ thuộc entity nào (upstream) | Seed trước tại module |
|-------------------|:----:|----------------------------------|-----------------------|
| `KE_HOACH_DANH_GIA` (owned) | 4 | `DON_VI` (don_vi_id + co_quan_duoc_danh_gia_id), `TAI_KHOAN` (CB NV + CB PD), `VU_VIEC` `HOAN_THANH` (FR-VI-05), `TIEU_CHI_DANH_GIA` (FR-10 DM) | FR-10 (TC), FR-04 (TVV/CG), FR-05 VV `HOAN_THANH`, FR-10 (DM TIEU_CHI_DANH_GIA) |
| `KET_QUA_DANH_GIA` (owned) | 4 | `KE_HOACH_DANH_GIA` `THUC_HIEN`, `VU_VIEC`, `TIEU_CHI_DANH_GIA` | Trong-module |
| `BAO_CAO_DANH_GIA` (owned) | 4 | `KE_HOACH_DANH_GIA` `BAO_CAO`, `KET_QUA_DANH_GIA` | Trong-module |
| `TIEU_CHI_DANH_GIA` (owned) | 1 | `DANH_MUC` (FR-10 nhóm `TIEU_CHI_DG_HQ`) | FR-10 DM |

> **Lưu ý:** KHÔNG hardcode `N records, states X/Y` ở đây — fixture đã chốt variants. Workflow advance state là việc của GĐ 2 (workflow-test-report-danh-gia.md).

---

## 3. Cấu Trúc File Test Case

```
fr-08-danh-gia-hq/
├── test-plan.md                      ← File này (overview)
├── 01-TC-FR-VI-01-tao-ke-hoach.md   ← Tạo KH ĐG + 2 vai trò cơ quan + file_dinh_kem
├── 02-TC-FR-VI-02-tieu-chi.md       ← Tiêu chí + trọng số 100% (BR-CALC-04)
├── 03-TC-FR-VI-03-phan-cong.md      ← Phân công + TRUONG_NHOM
├── 04-TC-FR-VI-04-duyet-pc.md       ← Phê duyệt PC + BR-AUTH-05 cùng cấp
├── 05-TC-FR-VI-05-chon-vv.md        ← Chọn VV HOAN_THANH ∪ DA_DANH_GIA trong kỳ
├── 06-TC-FR-VI-06-cham-diem.md      ← Chấm điểm TT17 + auto-calc + xếp loại (tách 21a/21b)
├── 07-TC-FR-VI-07-08-lap-trinh-bc.md ← Lập BC + Trình duyệt BC + verify TT17 21a/21b
├── 08-TC-FR-VI-09-duyet-bc.md       ← Phê duyệt BC + Từ chối BR-FLOW-04
├── 09-TC-FR-VI-10-readonly-cross-unit.md ← FR-VI-10 read-only cross-unit (v3.5 NEW) + mutation 403
├── 10-TC-HUY-state.md               ← HUY transition + guard lý do + không cho restore
├── 11-TC-permission-matrix.md       ← Permission matrix 7 role × 49 action + QTHT×FR-VI-10
├── 12-TC-edge-calculation.md        ← Edge case: trọng số ±0.01%, xếp loại boundary, file_dinh_kem matrix
└── 13-TC-data-migration.md          ← NEW: KH legacy DOT_DANH_GIA migrate KE_HOACH_DANH_GIA + backfill co_quan_duoc_danh_gia_id (Required=Y line 1017)
```

---

## 4. Tổng Quan Số Lượng Test Cases

### Bảng tổng TC theo file × loại

| File / Tab SCR-VI-01 | Happy | Negative | Edge | Tổng |
|----------------------|:-----:|:--------:|:----:|:----:|
| 01 — FR-VI-01 Phần A (tạo KH) | 1 | 2 | 1 | 4 |
| 02 — FR-VI-02 Tab 1 (Tiêu chí) | 1 | 2 | 1 | 4 |
| 03 — FR-VI-03 Tab 2 (Phân công) | 1 | 2 | 0 | 3 |
| 04 — FR-VI-04 Tab 2 (Duyệt PC) | 1 | 2 | 1 | 4 |
| 05 — FR-VI-05 Tab 3 (Chọn VV HOAN_THANH ∪ DA_DANH_GIA) | 1 | 1 | 1 | 3 |
| 06 — FR-VI-06 Tab 3 (Chấm điểm, tách calc vs xếp loại) | 1 | 1 | 2 | 4 |
| 07 — FR-VI-07/08 Tab 4 (Lập BC + Trình + verify TT17) | 1 | 1 | 1 | 3 |
| 08 — FR-VI-09 Tab 4 (Duyệt BC) | 1 | 1 | 0 | 2 |
| 09 — FR-VI-10 read-only + mutation 403 (NEW v3.5) | 1 | 3 | 2 | 6 |
| 10 — HUY transition + guard lý do | 1 | 2 | 0 | 3 |
| 11 — Permission matrix + QTHT×FR-VI-10 + BR-NOTIF-01 | 0 | 5 | 1 | 6 |
| 12 — Edge calculation (tolerance + file matrix) | 0 | 0 | 5 | 5 |
| 13 — Data migration (NEW v3.5) | 0 | 1 | 2 | 3 |
| **TỔNG** | **10** | **23** | **17** | **50** |

### Bảng chi tiết 40 TC

| TC ID | Tên TC ngắn | FR / BR | Loại | Priority | File |
|-------|-------------|---------|:----:|:--:|---|
| TC-DG-01 | Tạo KH ĐG happy path + auto-gen mã DG-{YYYYMMDD}-{SEQ} | FR-VI-01, BR-DATA-04 | Happy | P0 | 01 |
| TC-DG-02 | Tạo KH thiếu trường bắt buộc → ERR-DG-KH-01 | FR-VI-01 | Negative | P0 | 01 |
| TC-DG-03 | Tạo KH `tu_ngay >= den_ngay` → ERR-DG-KH-02 | FR-VI-01 | Negative | P0 | 01 |
| TC-DG-04 | Tạo KH với `co_quan_duoc_danh_gia_id` ≠ `don_vi_id` (cross-unit valid) v3.5 | FR-VI-01, BR-VI-08-01 | Edge | P0 | 01 |
| TC-DG-05 | Thêm tiêu chí + trọng số 100% → save OK | FR-VI-02, BR-CALC-04 | Happy | P0 | 02 |
| TC-DG-06 | Tổng trọng số = 99% khi chuyển `CHO_DUYET_PC` → ERR-DG-TC-01 | FR-VI-02 | Negative | P0 | 02 |
| TC-DG-07 | Điểm tối đa = 0 → ERR-DG-TC-03 | FR-VI-02 | Negative | P1 | 02 |
| TC-DG-08 | Trọng số tolerance ±0.01% (vd 100.00 vs 100.01) | FR-VI-02, BR-CALC-04 | Edge | P1 | 02 |
| TC-DG-09 | Phân công ≥1 TRUONG_NHOM + ≥1 DANH_GIA_VIEN → save + trình duyệt | FR-VI-03, BR-NOTIF-01 | Happy | P0 | 03 |
| TC-DG-10 | Phân công không có TRUONG_NHOM → ERR-DG-PC-02 | FR-VI-03 | Negative | P0 | 03 |
| TC-DG-11 | Phân công người trùng lặp → ERR-DG-PC-03 | FR-VI-03 | Negative | P1 | 03 |
| TC-DG-12 | CB PD cùng cấp duyệt PC → `THUC_HIEN` + gửi TB CB NV | FR-VI-04, BR-AUTH-05, BR-NOTIF-01 | Happy | P0 | 04 |
| TC-DG-13 | CB PD từ chối PC không lý do → ERR-DG-PD-02 | FR-VI-04, BR-FLOW-04 | Negative | P0 | 04 |
| TC-DG-14 | CB PD xuyên cấp (CB PD TW duyệt KH BN) → 403 BR-AUTH-05 | FR-VI-04, BR-AUTH-05 | Negative | P0 | 04, 11 |
| TC-DG-15 | CB PD duyệt PC khi KH `THUC_HIEN` (sai state) → ERR-DG-PD-01 | FR-VI-04 | Edge | P1 | 04 |
| TC-DG-16 | Chọn VV `HOAN_THANH` ∪ `DA_DANH_GIA` trong kỳ → multi-select OK (SRS:858) | FR-VI-05, BR-VI-08-03 | Happy | P0 | 05 |
| TC-DG-17 | Dropdown KHÔNG hiển thị VV `DANG_XU_LY` / VV ngoài kỳ; VV `DA_DANH_GIA` ở KH khác có hiển thị (cảnh báo) | FR-VI-05, BR-VI-08-03 | Negative | P0 | 05 |
| TC-DG-18 | Chọn VV đã `DA_DANH_GIA` ở KH khác → cảnh báo nhưng cho phép (system-overview:834) | FR-VI-05 | Edge | P1 | 05 |
| TC-DG-19 | Chấm điểm tất cả VV → auto SET `BAO_CAO` + KPI xếp loại | FR-VI-06, BR-CALC-04 | Happy | P0 | 06 |
| TC-DG-20 | Điểm vượt `diem_toi_da` → ERR-DG-DG-01 | FR-VI-06 | Negative | P0 | 06 |
| TC-DG-21a | Auto-calc formula `điểm tổng = Σ(diem_i × trong_so_i / 100)` — verify công thức với input fixture cố định | FR-VI-06, BR-CALC-04 | Edge | P0 | 06 |
| TC-DG-21b | Xếp loại boundary 5 case: 89.9% (Tốt) / 90% (Xuất sắc) / 70% (Tốt→Đạt boundary) / 50% (Đạt) / 49.9% (Chưa đạt) | FR-VI-06, BR-VI-08-04 | Edge | P0 | 06, 12 |
| TC-DG-22 | Lập BC + Trình duyệt BC → `CHO_PHE_DUYET` + gửi TB | FR-VI-07/08, BR-NOTIF-01 | Happy | P0 | 07 |
| TC-DG-23 | Trình BC khi KH chưa `BAO_CAO` → ERR-DG-TR-01 | FR-VI-08 | Negative | P1 | 07 |
| TC-DG-23a | Xuất XLSX/DOCX TT17 — verify nội dung mẫu 21a (`mau_bao_cao=MAU_21A`) vs 21b (`MAU_21B`) đúng template line 1058 | FR-VI-07, BR-DATA-06 | Edge | P1 | 07 |
| TC-DG-24 | CB PD duyệt BC → `HOAN_THANH` + xuất XLSX/DOCX TT17 | FR-VI-09, BR-DATA-06 | Happy | P0 | 08 |
| TC-DG-25 | CB PD từ chối BC lý do 9 chars → ERR-DG-PD-04 | FR-VI-09, BR-FLOW-04 | Negative | P0 | 08 |
| TC-DG-26 | **FR-VI-10**: CB NV `co_quan_duoc_danh_gia_id` xem được Tab BC read-only khi KH `HOAN_THANH` | FR-VI-10, BR-VI-08-01 | Happy | P0 | 09 |
| TC-DG-27 | **FR-VI-10**: User cơ quan khác (KHÔNG thuộc `co_quan_duoc_danh_gia_id`) → ERR-DG-10 | FR-VI-10 | Negative | P0 | 09 |
| TC-DG-28 | **FR-VI-10**: KH chưa `HOAN_THANH` (đang `THUC_HIEN`) → ERR-DG-11 | FR-VI-10 | Negative | P0 | 09 |
| TC-DG-29 | **FR-VI-10 cross-unit (BTP-TW × STP-AG)**: `cb_nv_dp_01` AG xem được, `cb_nv_dp_02` BG → 403 | FR-VI-10, BR-VI-08-01 | Edge | P0 | 09, 11 |
| TC-DG-29a | **FR-VI-10 cross-tier matrix**: BN×BN (BKH×BTC), BN×ĐP, ĐP×ĐP — verify FR-VI-10 R-only đúng theo từng pair | FR-VI-10, BR-AUTH-08 | Edge | P0 | 09 |
| TC-DG-29b | **FR-VI-10 mutation 403**: CB NV của `co_quan_duoc_danh_gia_id` cố PUT/PATCH/DELETE qua API direct trên 3 owned entity → 403 BE-layer (không chỉ UI hide). Memory `qa_htpldn_qtht_permission_bypass`. | FR-VI-10 | Negative | P0 | 09 |
| TC-DG-30 | HUY KH từ `LAP_KE_HOACH` → terminal, không restore + có lý do | HUY transition | Happy | P1 | 10 |
| TC-DG-31 | HUY KH từ `THUC_HIEN` (mid-life) → terminal + KET_QUA_DANH_GIA giữ history | HUY transition | Negative | P1 | 10 |
| TC-DG-31a | HUY thiếu lý do → reject (SRS:1167 Guard "Có lý do") + HUY từ `HOAN_THANH`/`HUY` terminal → reject | HUY transition | Negative | P1 | 10 |
| TC-DG-32 | TVV / CG truy cập SCR-VI-01 → 403 | Permission | Negative | P0 | 11 |
| TC-DG-33 | NHT truy cập SCR-VI-01 → 403 | Permission | Negative | P0 | 11 |
| TC-DG-34 | DN truy cập SCR-VI-01 → 403 | Permission | Negative | P0 | 11 |
| TC-DG-35 | CB_NV_TW xem KH `don_vi_id=BN-BKH` → expected 403 (CB_NV_TW scope chỉ TW per BR-AUTH-08, không phải "all"); KH `don_vi_id=TW` × `co_quan_duoc_danh_gia_id=BN/ĐP` thì TW xem được | Permission | Negative | P0 | 11 |
| TC-DG-35a | **QTHT × FR-VI-10**: QTHT đọc được KH `HOAN_THANH` của bất kỳ `co_quan_duoc_danh_gia_id` (BR-AUTH-03 ngoại lệ) | Permission | Edge | P1 | 11 |
| TC-DG-35b | **BR-NOTIF-01 channel + payload**: verify TB gửi đúng 4 thời điểm (FR-VI-03/04/08/09) — recipient (CB NV creator + CB PD reviewer), channel (in-app/email), content fields | BR-NOTIF-01 | Negative | P0 | 11 |
| TC-DG-36 | **Edge calc tolerance ±0.01%**: 99.99% (lower) / 100% / 100.01% (upper) / 100.02% (just outside) → save OK 3 case, ERR 1 case | FR-VI-02, BR-CALC-04 | Edge | P0 | 12 |
| TC-DG-37 | **Edge calc**: VV `DANG_XU_LY` KHÔNG xuất hiện dropdown FR-VI-05 + backend reject nếu hack request POST `vu_viec_id` của VV `DANG_XU_LY` → ERR | FR-VI-05, BR-VI-08-03 | Edge | P0 | 12 |
| TC-DG-38 | **Edge calc FR-VI-10 timing**: `co_quan_duoc_danh_gia_id` edit retro sau khi KH `HOAN_THANH` → CB NV mới có quyền xem ngay không? (defer SPEC-CLARIFY-FR08-04) | FR-VI-10 | Edge | P1 | 12 |
| TC-DG-39 | **Edge calc**: Trùng VV trong 2 KH cùng kỳ — verify constraint thực tế trên `KET_QUA_DANH_GIA` (UNIQUE per KH inferred) → cảnh báo cross-KH nhưng cho phép | FR-VI-05, BR-EC-VI-08-05 | Edge | P1 | 12 |
| TC-DG-40 | **Edge calc file matrix**: `file_dinh_kem[]` 5 format (PDF/DOC/DOCX/XLS/XLSX) × valid/>20MB/sai format + multi-file (50 file concurrent, aggregate size, drag-drop reorder, replace) | FR-VI-01, BR-VI-08-02 | Edge | P1 | 12 |
| TC-DG-41 | **Migration KH legacy** (NEW v3.5 §13): KH cũ DB `DOT_DANH_GIA` rename → `KE_HOACH_DANH_GIA` + backfill `co_quan_duoc_danh_gia_id` (Required=Y line 1017). Test: load form edit có default value, reject save khi NULL | Migration | Negative | P0 | 13 |
| TC-DG-42 | **Migration FR-VI-10 legacy**: KH legacy `co_quan_duoc_danh_gia_id=NULL` chưa backfill → FR-VI-10 behavior gì? (defer Open issue delta map §6) | Migration | Edge | P0 | 13 |
| TC-DG-43 | **Migration rename reference**: code/API path/i18n string cũ `dot-danh-gia` còn tồn tại không → grep + verify 0 reference cũ; URL /dot-danh-gia/* → 404 hoặc redirect | Migration | Edge | P1 | 13 |

**Phân bổ priority (sau revise):**

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc) | 33 | 66% |
| P1 (quan trọng) | 17 | 34% |
| P2 (nên có) | 0 | 0% |
| **Tổng** | **50** | **100%** |

**Phân bổ theo loại:**

| Loại | Số TC | % |
|------|------:|--:|
| Happy | 10 | 20% |
| Negative | 23 | 46% |
| Edge | 17 | 34% |

**Edge case calculation cụ thể (≥6):**

1. **TC-DG-08 / TC-DG-36** — Trọng số tổng tolerance ±0.01% boundary 4 case (99.99 / 100 / 100.01 / 100.02).
2. **TC-DG-21a** — Auto-calc formula `Σ(điểm × trọng số / 100)`.
3. **TC-DG-21b** — Xếp loại boundary 5 case 89.9/90/70/50/49.9 (BR-VI-08-04).
4. **TC-DG-37** — VV `DANG_XU_LY` không xuất hiện FR-VI-05 dropdown + backend reject hack request.
5. **TC-DG-29 / TC-DG-29a / TC-DG-38** — FR-VI-10 cross-unit matrix (BTP-TW × STP-AG, BN×BN, BN×ĐP, ĐP×ĐP, timing retro edit).
6. **TC-DG-29b** — FR-VI-10 mutation 403 BE-layer (PUT/PATCH/DELETE).
7. **TC-DG-39** — Trùng VV cross-KH (UNIQUE per KH).
8. **TC-DG-40** — File matrix 5 format × valid/>20MB/sai format + multi-file concurrent.
9. **TC-DG-41/42/43** — Migration KH legacy + backfill `co_quan_duoc_danh_gia_id` + rename reference.

---

## 5. Tiêu chí đạt/không đạt

> Reference: [`output/test-strategy.md §10`](../../../output/test-strategy.md).

- ✅ **PASS:** 100% P0 + ≥90% P1 pass.
- ❌ **FAIL:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%.
- ⚠️ **Sai spec (defer Minor):** nếu FE/BE behavior khác SRS nhưng KHÔNG block workflow chính (vd toast khác wording) → log Minor, defer round sau.
- 🤷 **Không xác định:** chỉ dùng khi retry method (reload fresh, isolatedContext, curl direct) đã đủ; CẤM kết luận khi chưa retry (xem memory `feedback_deep_review_before_ba_defer`).
- ⏸️ **Defer SPEC-CLARIFY-FR08-01:** 5 trường công khai chuyên trang CR-01 (delta map §6 T4 PENDING) — BA xác nhận có thuộc 12 DS công khai không.

**Gate cụ thể FR-VI-10 (NEW v3.5):**
- Phải PASS cả 3 TC: TC-DG-26 (happy `co_quan_duoc_danh_gia_id` user xem được) + TC-DG-27 (cơ quan khác → 403) + TC-DG-28 (KH chưa `HOAN_THANH` → ERR-DG-11) + TC-DG-29 (cross-unit isolation).
- Nếu FR-VI-10 fail → toàn module fail (vì là FR mới v3.5 critical theo delta map Finding 4).

---

## 6. Tham chiếu

- [`input/srs-update-2026-5-5/srs-fr-08-danh-gia.md`](../../../input/srs-update-2026-5-5/srs-fr-08-danh-gia.md) — SRS v3.5 (FR-VI-01..10, SCR-VI-01).
- [`input/srs-update-2026-5-5/_DELTA-MAP-FR08.md`](../../../input/srs-update-2026-5-5/_DELTA-MAP-FR08.md) — Delta map 8 thay đổi + findings critical.
- [`input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md`](../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) line 880-1006 — source thay đổi gốc.
- [`input/srs-v3/srs-fr-08-danh-gia.md`](../../../input/srs-v3/srs-fr-08-danh-gia.md) — baseline cũ (chỉ tham chiếu, KHÔNG dùng cite test).
- [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) line 795-840 — § ⑬ FR-08 thứ tự module + SM 8 states.
- [`tasks/system-overview.md`](../../../tasks/system-overview.md) §4.13 (M12 Đánh giá HQ) + §6.1 (rename v3.5) + §6.2.4 (FR-VI-10).
- [`output/test-strategy.md`](../../../output/test-strategy.md) — chiến lược tổng thể.
- [`output/scaling-test-strategy.md`](../../../output/scaling-test-strategy.md) — quy trình 7 bước onboard.
- [`output/permission-matrix.md`](../../../output/permission-matrix.md) — ma trận phân quyền 49 entity × 11 role.
- [`output/permission-matrix-by-fr.md`](../../../output/permission-matrix-by-fr.md) — view by FR (FR-VI-10 mới v3.5).
- [`input/data/entity-map.md`](../../../input/data/entity-map.md) — `KE_HOACH_DANH_GIA` cross-module map (rename từ `DOT_DANH_GIA`).
- [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) — block `ke_hoach_danh_gia_variants` v3.5.
- [`input/users.csv`](../../../input/users.csv) — test accounts.
- [`output/template/test-case-template.md`](../../../output/template/test-case-template.md) — template TC field-level.
- [`output/template/bug-report-template.md`](../../../output/template/bug-report-template.md) — template bug report (6 sections strict).

### Open issues / SPEC-CLARIFY pending (defer khi test)

- **SPEC-CLARIFY-FR08-01** (T4 delta map): 5 trường công khai chuyên trang CR-01 — BA xác nhận FR-08 có thuộc 12 DS công khai không (`_DELTA-MAP-FR08.md:120`).
- **SPEC-CLARIFY-FR08-02** (T9 delta map): CB PD có vào tác nhân FR-VI-02/06 không? v4 ghi "theo CSV UC 84/88" nhưng CSV chỉ liệt kê "CB NV TW/BN/ĐP" → giữ v3 (chỉ CB NV).
- **SPEC-CLARIFY-FR08-03** (D.3 delta map): NĐ 55/2019 Điều 11 ref cho FR-VI-10 — chưa web-verify.
- **SPEC-CLARIFY-FR08-04** (TC-DG-38): `co_quan_duoc_danh_gia_id` edit retro sau khi KH `HOAN_THANH` → CB NV mới có quyền xem ngay không? (FR-VI-10 timing).
- **SPEC-CLARIFY-FR08-05** ⚠️ NEW 2026-05-12 13:30:00: `tan_suat` enum DB CHECK line 1006 `('SO_BO_6_THANG','TRON_NAM','DOT_XUAT')` vs BR-LEGAL-08 line 1235 "KHÔNG cho đột xuất" — 2 vị trí SRS nội bộ mâu thuẫn. BA chốt giữ/xoá `DOT_XUAT` enum trước khi viết TC negative tần suất ngoài enum.
- **SPEC-CLARIFY-FR08-06** ⚠️ NEW 2026-05-12 13:30:00: SM HUY guard — SRS line 1167 list HUY chỉ từ `LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO`. Diagram §2.5 line 209 ghi "[*bất kỳ*] → HUY". 2 state `CHO_DUYET_PC` + `CHO_PHE_DUYET` có cancel-able không?
- **SPEC-CLARIFY-FR08-07** ⚠️ NEW 2026-05-12 13:30:00: BR-VI-08-06 hard-delete claim (system-overview C1) vs entity field `is_deleted` line 1015 + SM line 1167 soft-delete. C1 cross-cutting có override field-level không?
- **SPEC-CLARIFY-FR08-08** ⚠️ NEW 2026-05-12 13:30:00: `PHAN_CONG_DANH_GIA` entity (§1.2 FR-VI-03) không có trong §4 SRS owned entity list (line 893-1109). Là sub-table inline trong `KE_HOACH_DANH_GIA` (JSON assignees) hay table riêng? TC-DG-09/10/11 phụ thuộc DB schema thực tế.
- **Data migration** (delta map §3 Finding 5): KH cũ DB `DOT_DANH_GIA` không có cột `co_quan_duoc_danh_gia_id` → backfill thế nào? **Cover bởi TC-DG-41/42/43 file 13 NEW**, log thêm bug data migration nếu fail.

---

*Test plan v1.1 — generated 2026-05-12 từ SRS v3.5 update + delta map + system-overview §4.13. Revised 2026-05-12 13:30:00 sau review REVISE (12 gap + 10 suggestion): apply 4 blocker + 8 important gap. Tester BẮT BUỘC đọc delta map + 8 SPEC-CLARIFY pending TRƯỚC khi viết TC chi tiết để hiểu rename impact + FR-VI-10 cross-unit semantics + DOT_XUAT enum contradiction + migration scope.*
