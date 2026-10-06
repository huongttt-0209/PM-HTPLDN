# Kế Hoạch Kiểm Thử — FR-08 Theo dõi Đánh giá Hiệu quả Hỗ trợ Pháp lý (FR-VI-01 → FR-VI-10)

> **Phiên bản:** 1.0
> **Ngày tạo:** 2026-05-10
> **Owner:** QA Automation Lead
> **Module:** FR-08 / Nhóm VI — Theo dõi Đánh giá Hiệu quả HTPL
> **UC range:** UC83 → UC91 (9 UC CSV) + FR-VI-10 (UC chưa có trong CSV — gắn `[GAP-VI-04]`)
> **SRS reference:** [`input/srs-v3/srs-fr-08-danh-gia.-v3.1.md`](../../../input/srs-v3/srs-fr-08-danh-gia.-v3.1.md) (v3.5, 1247 dòng) + [`srs-v3.md`](../../../input/srs-v3/srs-v3.md) Phụ lục B/C
> **Plan parent:** [`Ver3.1/tasks/detailed-tc/plan.md`](../../../tasks/detailed-tc/plan.md) §W4.4
> **Source mode:** SRS local + NotebookLM secondary `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` (verify SM-DANHGIA 8 state canonical + BR-CALC-04 + Mẫu 21a/21b TT17/2025)
> **Recon log:** [`memory/fr08_recon.md`](../../../../C--HoaAG-LuatDN5/memory/fr08_recon.md) — URL `/danh-gia/ke-hoach/danh-sach`, 18 VV HOAN_THANH sẵn, 2 đợt pre-seeded LAP_KE_HOACH

---

## 1. Phạm vi kiểm thử

### 1.1 Chức năng được kiểm thử

- **10 FR** (FR-VI-01..10) trên 1 màn hình consolidated SCR-VI-01:
  - **Phần A — Danh sách đợt**: list + filter (tần suất / đối tượng / trạng thái / khoảng ngày) + search + form tạo/sửa/xóa + Xuất Excel + checkbox bulk + 18 cột table
  - **Phần B — Chi tiết đợt** (4 tabs):
    - **Tab 1 — Tiêu chí** (UC84, FR-VI-02): inline editable bảng tiêu chí, realtime tổng trọng số 100%, tham chiếu DM UC109
    - **Tab 2 — Phân công** (UC85+UC86, FR-VI-03+FR-VI-04): inline editable bảng phân công + Trình duyệt + Duyệt PC + Từ chối PC
    - **Tab 3 — Thực hiện chấm điểm** (UC87+UC88, FR-VI-05+FR-VI-06): chọn VV multi-select + bảng chấm inline + KPI cards xếp loại + Lưu nháp + Hoàn tất chấm điểm
    - **Tab 4 — Báo cáo** (UC89+UC90+UC91, FR-VI-07+FR-VI-08+FR-VI-09): KPI + bảng tổng hợp + biểu đồ Radar/Bar + nhận xét chung + Trình BC + Duyệt BC + Từ chối BC + Xuất XLSX/DOCX theo mẫu TT17/2025
  - **FR-VI-10** (read-only chế độ): CB NV thuộc `co_quan_duoc_danh_gia_id` xem KQ đánh giá khi đợt HOAN_THANH
- **Entity owned** (4): `KE_HOACH_DANH_GIA` (16 cột — có `file_dinh_kem` + `co_quan_duoc_danh_gia_id` v3.5), `KET_QUA_DANH_GIA`, `BAO_CAO_DANH_GIA` (mẫu 21a/21b), `TIEU_CHI_DANH_GIA` (FR-10 quản trị)
- **Entity referenced**: `VU_VIEC` (filter HOAN_THANH trong kỳ + cùng đơn vị), `TU_VAN_VIEN`, `TAI_KHOAN`, `DON_VI` (cây 3 tầng TW/BN/ĐP)
- **State Machine SM-DANHGIA:** 8 trạng thái + 11 transitions (Section 5 source of truth + GAP-VI-01: bổ sung HUY)
  - LAP_KE_HOACH → PHAN_CONG → CHO_DUYET_PC → THUC_HIEN → BAO_CAO → CHO_PHE_DUYET → HOAN_THANH
  - 4 transition HUY (từ LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO)
  - 2 transition reject (CHO_DUYET_PC → PHAN_CONG, CHO_PHE_DUYET → BAO_CAO)
- **State Machine BAO_CAO_DANH_GIA**: 4 trạng thái — DU_THAO / CHO_PHE_DUYET / DA_DUYET / TU_CHOI (entity 1:1 KH)
- **API:** KHÔNG có kênh API (toàn bộ workflow CB NV nhập tay)

### 1.2 Danh sách FR / UC / TC file

| # | Mã FR | UC | Tên chức năng | Tab/SCR | TC dự kiến | File Test Case |
|---|--------|-----|--------------|---------|-----------|----------------|
| 1 | FR-VI-01 | UC83 | Lập kế hoạch đợt + Phần A danh sách (list/filter/search/form/CRUD/Xuất Excel/Hủy) | Phần A + Form | 18 | `01-TC-FR-VI-01-lap-ke-hoach.md` |
| 2 | FR-VI-02 | UC84 | Thiết lập tiêu chí đánh giá (CRUD inline + BR-CALC-04 trọng số 100% + tham chiếu DM UC109) | Tab 1 | 10 | `02-TC-FR-VI-02-thiet-lap-tieu-chi.md` |
| 3 | FR-VI-03 + FR-VI-04 | UC85, UC86 | Phân công người ĐG (CRUD inline) + Phê duyệt phân công (Duyệt/Từ chối PC) + transition CHO_DUYET_PC↔THUC_HIEN/PHAN_CONG | Tab 2 | 14 | `03-TC-FR-VI-03-04-phan-cong-duyet-pc.md` |
| 4 | FR-VI-05 + FR-VI-06 | UC87, UC88 | Chọn VV vào đợt (multi-select VV HOAN_THANH trong kỳ) + Chấm điểm từng VV theo tiêu chí (BR-CALC-04 + Lưu nháp + Hoàn tất → BAO_CAO) | Tab 3 | 14 | `04-TC-FR-VI-05-06-chon-vv-cham-diem.md` |
| 5 | FR-VI-07 + FR-VI-08 + FR-VI-09 | UC89, UC90, UC91 | Lập BC (auto tổng hợp số liệu 13 cột TT17 + nhập tay 4 trường) + Trình BC + Duyệt/Từ chối BC + Xuất XLSX/DOCX | Tab 4 | 14 | `05-TC-FR-VI-07-08-09-bao-cao-trinh-duyet.md` |
| 6 | FR-VI-10 | (no UC, GAP-VI-04) | Nhận kết quả ĐG (read-only) cho CB NV thuộc cơ quan được ĐG khi đợt HOAN_THANH | Tab 4 read-only | 6 | `06-TC-FR-VI-10-nhan-ket-qua.md` |
| 7 | (cross) | — | Permission matrix cross-FR-08 (BR-AUTH-01/05/08 + BR-FLOW-04 + BR-NOTIF-01) | cross-cutting | 8 | `07-TC-permission-matrix.md` |

**Tổng dự kiến A3 base: ~84 TC** (sau A4 edge merge + A6 fill GAP + A7 filter + Codex apply: target ~80-95 TC)

**Cấu trúc file output (sau A1-A7):**

```
output/test-cases/danh-gia/
├── 00-test-plan-overview.md                                    ← File này
├── 01-TC-FR-VI-01-lap-ke-hoach.md                              ← UC83 + Phần A list/filter/form/CRUD/Hủy
├── 02-TC-FR-VI-02-thiet-lap-tieu-chi.md                        ← UC84 Tab 1 Tiêu chí + BR-CALC-04
├── 03-TC-FR-VI-03-04-phan-cong-duyet-pc.md                     ← UC85+UC86 Tab 2 Phân công + Duyệt PC
├── 04-TC-FR-VI-05-06-chon-vv-cham-diem.md                      ← UC87+UC88 Tab 3 Chọn VV + Chấm điểm
├── 05-TC-FR-VI-07-08-09-bao-cao-trinh-duyet.md                 ← UC89+UC90+UC91 Tab 4 BC + Xuất XLSX/DOCX
├── 06-TC-FR-VI-10-nhan-ket-qua.md                              ← FR-VI-10 read-only cơ quan được ĐG
├── 07-TC-permission-matrix.md                                  ← Cross BR-AUTH + BR-NOTIF + BR-FLOW
├── 08-REVIEW-edge-case-hunter.md                               ← A4 audit log (TC mới đã merge inline)
├── 09-traceability-matrix.md                                   ← A5 BR/AC ↔ TC matrix
├── 10-REVIEW-test-quality.md                                   ← A6 audit log
├── 11-a7-filter-log.md                                         ← A7 audit log (LOẠI/SỬA/GIỮ)
└── 12-codex-review-log.md                                      ← Codex review patches applied
```

### 1.3 Tài khoản test (`input/users.csv`)

| Role | Cấp | Username | Dùng cho TC loại |
|------|-----|----------|-------------------|
| QTHT | — | qtht_01 | Read-only verify (Permission Matrix) + DM tiêu chí UC109 (FR-10) |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD đợt scope TW + Phân công + Chấm điểm + Lập BC + Trình BC scope TW |
| CB_NV_BN | BN | cb_nv_bn_01 (BKH), cb_nv_bn_02 (BTC) | Scope BN + cross-unit isolation BR-AUTH-08 + co_quan_duoc_danh_gia_id BN |
| CB_NV_DP | ĐP | cb_nv_dp_01 (AG), cb_nv_dp_02 (BG) | Scope ĐP + cross-tenant test + nhận KQ khi `co_quan_duoc_danh_gia_id`=DP |
| CB_PD_TW | TW | cb_pd_tw_01 | Duyệt PC + Duyệt BC cùng cấp TW (UC86 + UC91 — BR-AUTH-05) |
| CB_PD_BN | BN | cb_pd_bn_01 | Duyệt PC + BC cùng cấp BN; cross-cấp test BR-AUTH-05 |
| CB_PD_DP | ĐP | cb_pd_dp_01 | Duyệt PC + BC cùng cấp ĐP |
| CG / NHT | — | cg_01..06, nht_01..04 | Người ĐG được phân công (DANH_GIA_VIEN / TRUONG_NHOM) — chấm điểm |
| TVV | — | tvv_01 | Negative — verify 403 trên đợt ĐG (TVV không thuộc nhóm VI) |
| DN | — | dn_01 | Negative — verify 403 (DN không truy cập SCR-VI-01) |

> **Source TK:** `c:/HoaAG/LuatDN5/Ver3.1/input/users.csv`. Password Secret@123 toàn bộ.

> **Lưu ý DM Tiêu chí (UC109):** `cb_nv_*` không có quyền access `/quan-tri/danh-muc` (recon 2026-05-03). Phase B nếu cần seed DM phải dùng `qtht_01`. Phase A test các TC tham chiếu DM = mock tên tiêu chí + nhập tay số liệu (acceptable per BR-CALC-04 inline).

### 1.4 Dữ liệu tiền điều kiện

| Loại dữ liệu | Yêu cầu | Trạng thái thực tế (recon 2026-05-03) |
|--------------|---------|----------------------------------------|
| Đợt pre-seeded LAP_KE_HOACH | ≥2 | ✅ DG-20260502-0001 Q2/2026 + DG-20260502-0002 Q3/2026 (cb_nv_tw_01 thấy) |
| VV HOAN_THANH (FR-05) | ≥10 trong kỳ đánh giá | ✅ 18 VV (1-18 / 18 mục) scope TW |
| DM Tiêu chí (UC109/FR-10) | ≥4 tiêu chí HIEU_QUA_HTPL `KICH_HOAT` | ⚠️ chưa verify role gap — Phase A skip nhập tay |
| Tài khoản CB ĐG đủ điều kiện | ≥2 (≥1 TRUONG_NHOM) | ✅ cg_01..06 + nht_01..04 + cb_nv_*_01..02 |
| co_quan_duoc_danh_gia_id (FR-VI-10) | DON_VI khác `don_vi_id` của user lập đợt | ✅ DON_VI master có TW/BN/ĐP đầy đủ |

---

## 2. Quy tắc nghiệp vụ trích xuất từ SRS

### 2.1 Business Rules (BR formal §6 + working labels)

> **Footnote convention:**
> - **BR formal §6 srs-fr-08:** BR khai báo trong file SRS FR-08 §6 (lines 1173-1244). 9 BR áp dụng.
> - **Working labels (master srs-v3.md inline):** BR codes ref nhưng source ở Phụ lục B file chính.

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực bắt buộc — Tier 1 (CB nội bộ U/P + TOTP 2FA) | srs-fr-08 §6 line 1191-1195 | ✅ | Precondition login mọi UC |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB PD cấp = đơn vị tạo) | srs-fr-08 §6 line 1197-1201 | ✅ | TC duyệt PC (file 03) + duyệt BC (file 05) + cross-cấp negative (file 07) |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | srs-v3.md Phụ lục B (working) | ✅ | TC scope đơn vị mọi list/detail (file 01, 02, 03, 04, 05, 06, 07) |
| BR-CALC-04 | Tổng trọng số tiêu chí = 100%. Điểm tổng = SUM(diem_i × trong_so_i / 100) | srs-fr-08 §6 line 1221-1225 | ✅ (core) | TC trọng số 100% (file 02) + tính điểm tổng (file 04) |
| BR-DATA-03 | Common fields (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id) | srs-fr-08 §6 line 1203-1207 | ✅ | TC tạo/sửa/xóa mọi entity (file 01-06) |
| BR-DATA-04 | Auto-gen mã DG-{YYYYMMDD}-{SEQ} | srs-fr-08 §6 line 1209-1213 | ✅ | TC tạo đợt mới (file 01) |
| BR-DATA-05 | Audit trail INSERT-only | srs-fr-08 §6 line 1215-1219 | ✅ | TC CUD + state transition mọi file |
| BR-FLOW-04 | Mọi action "Từ chối" yêu cầu lý do ≥10 ký tự | srs-fr-08 §6 line 1227-1231 | ✅ | TC từ chối PC (file 03) + từ chối BC (file 05) |
| BR-LEGAL-08 | Tần suất đánh giá hiệu quả: sơ bộ 6 tháng + tròn năm. KHÔNG đột xuất | srs-fr-08 §6 line 1233-1237 | ✅ | TC tan_suat enum (file 01) |
| BR-NOTIF-01 | Gửi thông báo kết quả phê duyệt cho CB NV | srs-fr-08 §6 line 1239-1243 | ✅ | TC notif sau Duyệt/Từ chối PC + BC (file 03 + 05 + 07) |

### 2.2 Error Codes

**FR-VI-01 (Lập kế hoạch):**
- ERR-DG-KH-01 (thiếu trường bắt buộc)
- ERR-DG-KH-02 (tu_ngay >= den_ngay)
- ERR-AUTH-01 (không quyền)

**FR-VI-02 (Tiêu chí):**
- ERR-DG-TC-01 (tổng trọng số != 100%)
- ERR-DG-TC-02 (thiếu tên tiêu chí)
- ERR-DG-TC-03 (điểm tối đa <= 0)

**FR-VI-03 (Phân công):**
- ERR-DG-PC-01 (0 người đánh giá)
- ERR-DG-PC-02 (thiếu TRUONG_NHOM)
- ERR-DG-PC-03 (người trùng lặp)
- ERR-DG-PC-04 (đợt không ở PHAN_CONG)

**FR-VI-04 (Duyệt PC):**
- ERR-DG-PD-01 (đợt không ở CHO_DUYET_PC)
- ERR-DG-PD-02 (từ chối thiếu lý do >= 10)

**FR-VI-05 (Chọn VV):**
- WRN-DG-VV-01 (0 VV hoàn thành trong kỳ)
- ERR-DG-VV-01 (đợt không ở THUC_HIEN)

**FR-VI-06 (Chấm điểm):**
- ERR-DG-DG-01 (điểm > điểm tối đa)
- ERR-DG-TC-01 (tổng trọng số lệch ±0.01%)
- ERR-DG-TC-02 (sửa tiêu chí khi đang chấm)
- WRN-DG-VV-02 (0 VV trong kỳ)

**FR-VI-07 (Lập BC):**
- ERR-DG-BC-01 (đợt không ở BAO_CAO)

**FR-VI-08 (Trình BC):**
- ERR-DG-TR-01 (đợt không ở BAO_CAO)
- WRN-DG-TR-01 (BC thiếu dữ liệu)

**FR-VI-09 (Duyệt BC):**
- ERR-DG-PD-03 (đợt không ở CHO_PHE_DUYET)
- ERR-DG-PD-04 (từ chối thiếu lý do >= 10)

**FR-VI-10 (Nhận KQ):**
- ERR-DG-10 (user không thuộc co_quan_duoc_danh_gia_id)
- ERR-DG-11 (KH chưa HOAN_THANH)

### 2.3 State Machine SM-DANHGIA — 8 states + 11 transitions

> **Source of truth:** srs-fr-08 §5 line 1117-1167 (Section 5 + GAP-VI-01).
> **Cảnh báo:** 02-thu-tu-module ⑬ flag 3 phiên bản tự mâu thuẫn — **canonical ở v3.5 = 8 state per Section 5**, BA đã chốt (CHANGELOG line 16).

| # | Từ | Đến | Trigger | Actor | Guard | TC ref |
|---|----|-----|---------|-------|-------|--------|
| 1 | [*] | LAP_KE_HOACH | Tạo đợt | CB NV | Tần suất 6T/năm | file 01 |
| 2 | LAP_KE_HOACH | PHAN_CONG | Phân công người ĐG | CB NV | Có KH | file 03 |
| 3 | PHAN_CONG | CHO_DUYET_PC | Trình duyệt PC | CB NV | ≥1 người, ≥1 TRUONG_NHOM, trọng số = 100% | file 03 |
| 4 | CHO_DUYET_PC | THUC_HIEN | Duyệt PC | CB PD | Cùng cấp | file 03 |
| 5 | CHO_DUYET_PC | PHAN_CONG | Từ chối PC | CB PD | Lý do ≥10 ký tự | file 03 |
| 6 | THUC_HIEN | BAO_CAO | Hoàn tất chấm điểm tất cả VV | System / CB NV | Tất cả VV đã chấm | file 04 |
| 7 | BAO_CAO | CHO_PHE_DUYET | Trình duyệt BC | CB NV | BC đầy đủ dữ liệu | file 05 |
| 8 | CHO_PHE_DUYET | HOAN_THANH | Duyệt BC | CB PD | Cùng cấp | file 05 |
| 9 | CHO_PHE_DUYET | BAO_CAO | Từ chối BC | CB PD | Lý do ≥10 ký tự | file 05 |
| 10-13 | LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO | HUY | Hủy đợt | CB NV/PD | Có lý do, chưa HOAN_THANH | file 01 |

### 2.4 Permission Matrix (cross-FR)

| Hành động | qtht | cb_nv_tw | cb_nv_bn | cb_nv_dp | cb_pd_tw | cb_pd_bn | cb_pd_dp | cg/nht | tvv | dn |
|-----------|------|----------|----------|----------|----------|----------|----------|--------|-----|-----|
| Xem danh sách đợt (scope đơn vị) | R | RW | RW | RW | R | R | R | R (DG) | — | — |
| Tạo đợt + Sửa + Xóa (LAP_KE_HOACH) | — | RW | RW | RW | — | — | — | — | — | — |
| Thiết lập tiêu chí Tab 1 | — | RW | RW | RW | — | — | — | — | — | — |
| Phân công Tab 2 | — | RW | RW | RW | — | — | — | — | — | — |
| Trình duyệt PC | — | RW | RW | RW | — | — | — | — | — | — |
| Duyệt/Từ chối PC | — | — | — | — | RW (TW only) | RW (BN only) | RW (DP only) | — | — | — |
| Chọn VV vào đợt (Tab 3) | — | RW | RW | RW | — | — | — | — | — | — |
| Chấm điểm VV (Tab 3) | — | RW (nếu PC) | RW (nếu PC) | RW (nếu PC) | — | — | — | RW (nếu PC) | — | — |
| Lập BC + Trình BC (Tab 4) | — | RW | RW | RW | — | — | — | — | — | — |
| Duyệt/Từ chối BC | — | — | — | — | RW (TW only) | RW (BN only) | RW (DP only) | — | — | — |
| Xuất XLSX/DOCX (Tab 4) | — | RW | RW | RW | R | R | R | — | — | — |
| Nhận KQ ĐG (FR-VI-10, read-only) | — | R (nếu thuộc co_quan_duoc_dg) | R | R | — | — | — | — | — | — |

---

## 3. Strategy & Risk

### 3.1 Strategy

- **Pyramid:** Functional UI 70% / SM transitions 15% / Permission Matrix 10% / Edge cases 5% (boundary, format, tolerance)
- **Approach:** Đi tuần tự theo SM-DANHGIA → 1 happy path xuyên suốt (file 01 → 02 → 03 → 04 → 05) + đặc tả negative tại từng tab + cross BR-AUTH file 07
- **Reuse:** Đợt LAP_KE_HOACH pre-seeded (DG-20260502-0001 Q2/2026) làm baseline. 18 VV HOAN_THANH scope TW dùng chung Tab 3.
- **Approval idempotency:** Test transition 2 chiều (Duyệt/Từ chối PC, Duyệt/Từ chối BC) + verify BR-NOTIF-01 fire 1 lần per transition.

### 3.2 Risk

| ID | Risk | Mitigation |
|----|------|-----------|
| R1 | DM Tiêu chí UC109 cb_nv không access | Phase A nhập tay 4 tiêu chí mock; Phase B coordinate với QTHT seed DM |
| R2 | BUG-VUVIEC-001 STILL OPEN R8 (chặn HOAN_THANH VV) | Phase A vẫn viết TC đầy đủ, Phase B defer chờ FR-05 unblock |
| R3 | Tab pattern UI 11 tab vs SRS 8 state (recon flag) | Phase A test theo SRS canonical; gap log trong A7-filter |
| R4 | SM-DANHGIA 3 phiên bản tự mâu thuẫn (02-thu-tu-module ⑬) | Per BA CHANGELOG v3.5 line 16 → canonical = §5 8 state |
| R5 | Biểu đồ Radar/Bar Tab 4 (component C21) | Phase A verify hiển thị (sự tồn tại); skip pixel-perfect chart QA |

---

## 4. Definition of Done — Phase A

- [x] A1 — Đọc SRS đầy đủ + sibling-check FR-13 (template gần nhất) + recon
- [ ] A2 — `00-test-plan-overview.md` (file này)
- [ ] A3 — 7 file UC TC (`01-..07-`)
- [ ] A4 — Edge case hunter (`08-REVIEW-edge-case-hunter.md`) + merge inline TC mới
- [ ] A5 — Traceability matrix (`09-traceability-matrix.md`)
- [ ] A6 — Test review (`10-REVIEW-test-quality.md`) + fill gap inline
- [ ] A7 — Manual UI/function-testable filter (`11-a7-filter-log.md`)
- [ ] **A8 — Codex review (`12-codex-review-log.md`) — `/codex` review TC vs SRS + apply patches**
- [ ] Coverage targets: BR ≥95% (9/9), AC ≥95% (∼28 AC), SM ≥100% (8/8 + 11 transitions), Permission ≥90%, Error ≥95%
- [ ] 0 TC chỉ test DB/API thuần (A7 verified)

---

## 5. Hand-off

- **Phase B output:** `output/execution-test/danh-gia/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`
- **Pre-condition Phase B:** A done ✅ + W3.2 Vụ việc Phase B HOAN_THANH (R7.E3 finding 2026-05-07 — env có 70 HSCT 8 state, BUG-VUVIEC-001 R8 chưa fix) + DM Tiêu chí seed bởi QTHT
- **Defer Phase B nếu:** BUG-VUVIEC-001 chưa close (R7 todo.md Risk R2)
