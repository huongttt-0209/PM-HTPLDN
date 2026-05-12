# Danh sách bug cần dev fix — Cập nhật sau R19 reverify 2026-05-12 17:50:00

**Phạm vi:** Tổng hợp bug còn Open / Partial sau R19 reverify (audit file: [`reverify-audit-2026-05-12.md`](reverify-audit-2026-05-12.md)). Bug đã Fixed R19 đã loại khỏi danh sách (xem section "Bug đã đóng R19" cuối file).

**LOẠI TRỪ:** 4 bug Defer chờ phase tích hợp API ngoài (DVC LGSP / mTLS / Cổng PLQG) — không thuộc phạm vi dev fix nội bộ.

**Tổng số bug còn cần xử lý: 9** (giảm từ 14 sau R19)
- 5 bug ❌ Still Open
- 3 bug ⚠️ Partial (dev đã chạm, chưa xong hết surface)
- 1 bug ❌ Open kèm regression nặng (TVCS-R16-001: 5 → 11 path 404)

Tỉ lệ R19: **6 ✅ Fixed · 3 ⚠️ Partial · 5 ❌ Open** trong 14 bug verify.

---

## Bảng tổng hợp 9 bug còn cần fix

| # | Bug ID | Module | Sev | P | Status R19 | Ai làm | Phân loại fix | File bug report |
|:-:|---|---|:-:|:-:|:-:|:-:|---|---|
| 1 | BUG-CHITRA-010 | Chi trả | Medium | P2 | ❌ Open | **Dev BE** | Persist column data | [bug-report-r7-7-12-2-fr14-bo-sung.md](../bug-reports/chi-tra/bug-report-r7-7-12-2-fr14-bo-sung.md) |
| 2 | BUG-FUNC-DG-014 | Đánh giá | Minor | P3 | ❌ Open | **Dev FE + BA** | Dropdown filter null name | [bug-report-flow-danhgia.md](../bug-reports/danh-gia/bug-report-flow-danhgia.md) |
| 3 | BUG-HDTV-034 | HĐ tư vấn | Major | P1 | ❌ Open | **Dev FE + BE** | Route guard + BE 403 | [bug-report-r7-7-14-hdtv.md](../bug-reports/hop-dong-tv/bug-report-r7-7-14-hdtv.md) |
| 4 | BUG-FE-TVCS-R16-005 | TVCS | Major | P1 | ⚠️ Partial | **Dev FE** | Add button [Công khai]/[Hủy công khai] | [bug-report-r7-7-5-tvcs-r16.md](../bug-reports/tu-van-chuyen-sau/bug-report-r7-7-5-tvcs-r16.md) |
| 5 | BUG-BE-TVCS-R16-001 | TVCS | Major | P1 | ❌ Open ⚠️ REGRESSION | **Dev BE** | Deploy TLPL CRUD endpoint | [bug-report-r7-7-5-tvcs-r16.md](../bug-reports/tu-van-chuyen-sau/bug-report-r7-7-5-tvcs-r16.md) |
| 6 | BUG-FUNC-TVN-005 | Tư vấn nhanh | Minor | P3 | ❌ Open | **Dev FE + BE** | Add enum module "Tư vấn" | [bug-report-r7-7-11-tvn.md](../bug-reports/tu-van-nhanh/bug-report-r7-7-11-tvn.md) |
| 7 | BUG-VV-PC-WRN-01 | Vụ việc | Minor | P2 | ❌ Open | **Dev FE** | Add button [Tìm thủ công] | [bug-report-flow-vu-viec.md](../bug-reports/vu-viec/bug-report-flow-vu-viec.md) |
| 8 | BUG-VV-FN-LICHSU-01 | Vụ việc | Minor | P3 | ⚠️ Partial (16/18) | **Dev BE** | Bổ sung 2 enum còn thiếu | [bug-report-r7-7-3-functional-vu-viec.md](../bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md) |
| 9 | BUG-VV-FN-TVV-PERMISSION-GAP-01 | Vụ việc | Major | P1 | ⚠️ Partial (2/3) | **Dev BE** | Thêm perm `trinh-phe-duyet_vu_viec` | [bug-report-r7-7-3-functional-vu-viec.md](../bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md) |

---

## Chi tiết yêu cầu fix theo từng nhóm

### Nhóm Dev BE — 5 bug

#### 1. BUG-CHITRA-010 (Medium · P2 · ❌ Open) — `ngayYeuCauBoSung` không persist khi YCBS

- **SRS:** `srs-fr-06-chi-tra.md` §HSCT FR-V.II-14
- **Trạng thái R19:** HSCT000066 (state YEU_CAU_BO_SUNG, soLanBoSung=1) `ngayYeuCauBoSung = null`. Dev chưa đụng BE logic transition DKT→YCBS.
- **Acceptance:** Khi HSCT chuyển state sang `YEU_CAU_BO_SUNG`, BE BẮT BUỘC ghi `ngayYeuCauBoSung = NOW()` trước khi commit transaction. Deadline tracking 5 ngày LV phụ thuộc field này.
- **Verify (UI):** Login CB NV → list HSCT YEU_CAU_BO_SUNG → click record → check field "Hạn bổ sung" / "Ngày yêu cầu bổ sung" trên UI khác null + API `GET /api/v1/ho-so-chi-tras?trangThai=YEU_CAU_BO_SUNG` mỗi record có `ngayYeuCauBoSung` khác null.

#### 2. BUG-BE-TVCS-R16-001 (Major · P1 · ❌ Open · ⚠️ REGRESSION NẶNG) — TLPL CRUD endpoint chưa deploy + tăng số path 404

- **SRS:** `srs-fr-12-tv-chuyen-sau.md` §Tư liệu pháp luật + UC TLPL
- **Trạng thái R19:** R16 báo 5 path 404 → R19 **tăng lên 11 path 404** (regression). Dev có thể đã add endpoint mới vào spec nhưng chưa wire BE → 6 path mới thêm 404.
- **11 path 404 R19:**

| Path | Status |
|---|:-:|
| GET `/api/v1/tu-lieu-phap-luats?tuVanChuyenSauId=...` | 404 |
| POST `/api/v1/tu-lieu-phap-luats` | 404 |
| GET/PATCH/DELETE `/api/v1/tu-lieu-phap-luats/{id}` | 404 |
| POST `/api/v1/tu-lieu-phap-luats/{id}/cong-khai` | 404 |
| `/api/v1/tu-lieu-phap-luat` (singular) | 404 |
| `/api/v1/tu-lieu-phap-luats/tu-van-chuyen-sau/{id}` (nested) | 404 |
| `/api/v1/tu-van-chuyen-saus/{id}/tu-lieu-phap-luats` (owner-nested) | 404 |
| `/api/v1/tlpl` · `/api/v1/legal-documents` · `/api/v1/tu-lieu` | 404 |

- **Acceptance:** BE deploy đầy đủ REST controller TLPL VV (5 method):
  - `GET /api/v1/tu-lieu-phap-luats?tuVanChuyenSauId={id}` — list
  - `POST /api/v1/tu-lieu-phap-luats` — create
  - `PATCH /api/v1/tu-lieu-phap-luats/{tlplId}` — update
  - `DELETE /api/v1/tu-lieu-phap-luats/{tlplId}` — delete
  - `POST /api/v1/tu-lieu-phap-luats/{tlplId}/cong-khai` — chuyển NHAP→CONG_KHAI
- **Verify (UI):** Click button [Đang thực hiện]/[Tạm dừng]/[Kết thúc] trong UI TVCS detail → quan sát toast/redirect (không 404).

#### 3. BUG-VV-FN-LICHSU-01 (Minor · P3 · ⚠️ Partial 16/18) — LICH_SU_VU_VIEC miss 2 enum spec

- **SRS:** `LICH_SU_VU_VIEC ENUM 18 hành động` · `BR-AUDIT-VV-01`
- **Trạng thái R19:** Pool 17 enum (R19 +1 `MO_LAI` so R18). Còn miss 4: `TIEP_NHAN`, `TU_CHOI`, `TU_CHOI_DUYET`, `YEU_CAU_BO_SUNG`.
- **Pool đã có (17):** `APPROVE, CAP_NHAT_KQ, CONG_KHAI, CREATE, DANH_GIA, HOAN_THANH, HUY_CONG_KHAI, KIEM_TRA, MO_LAI, PHAN_CONG, PHAN_CONG_CA_NHAN, PHAN_CONG_TO_CHUC, PHE_DUYET, TAO_VV, TRINH_PHE_DUYET, UPDATE, XAC_NHAN_PHAN_CONG`.
- **Acceptance:** BE bổ sung 4 enum còn thiếu (`TIEP_NHAN`, `TU_CHOI`, `TU_CHOI_DUYET`, `YEU_CAU_BO_SUNG`) cho audit log khi state machine advance đúng transition.
- **Verify (UI):** Walk full lifecycle 1 VV qua tất cả transition → mở Tab "Dòng thời gian"/"Lịch sử" UI → cover 18/18 enum.

#### 4. BUG-VV-FN-TVV-PERMISSION-GAP-01 (Major · P1 · ⚠️ Partial 2/3) — TVV thiếu perm `trinh-phe-duyet_vu_viec`

- **SRS:** `srs-fr-05-vu-viec.md` FR-V.I-12 §Inputs "TVV nhập kết quả"
- **Trạng thái R19:** Perm count 14 → 20 (+6 trong đó `cap-nhat-ket-qua_ket_qua_vu_viec`, `create_ket_qua_vu_viec`, `read_ket_qua_vu_viec`, `update_ket_qua_vu_viec`, `hoan-thanh_vu_viec`, `read_ho_so_vu_viec`). API probe 3 endpoint:
  - POST `/cap-nhat-ket-qua` → 422 ✅ Perm OK (validation body)
  - POST `/trinh-phe-duyet` → **403 ❌ STILL Forbidden**
  - POST `/hoan-thanh` → 422 ✅ Perm OK (validation body)
- **Acceptance:** BE thêm perm `trinh-phe-duyet_vu_viec` (hoặc `trinh-phe-duyet_ket_qua_vu_viec` theo convention) vào role TVV.
- **Verify (UI):** TVV login → mở VV phân công → toolbar có button [Trình PD] hiện + click thật → 201/200 (không 403). KHÔNG dùng API direct probe — phải kiểm UI thao tác user.

#### 5. BUG-HDTV-034 (Major · P1 · ❌ Open) — Route `/hop-dong-tv/danh-sach` thiếu guard (FE) + BE chưa 403

- **SRS:** BA chốt 2026-05-11 — route HDTV chỉ truy cập từ accordion VV, không standalone. Sev nâng Major vì RBAC bypass.
- **Trạng thái R19:** Login `cb_nv_tw_06` → navigate `/hop-dong-tv/danh-sach` → render 9 records, no `/403`, no route guard. Vi phạm permission matrix.
- **Acceptance — 2 surface phải fix cả 2:**
  - **FE:** Add route guard — user navigate trực tiếp `/hop-dong-tv/danh-sach` không qua context VV → redirect dashboard hoặc 404 page.
  - **BE:** Middleware role check `/api/v1/hop-dong-tu-vans` — role không có perm `read_hdtv` thì 403 ERR-PERM-SYS-00-01.
- **Verify (UI):** `cb_nv_tw_06` gõ URL trực tiếp → /403 hoặc redirect; mở VV detail → accordion HDTV vẫn render đúng (positive path).

### Nhóm Dev FE — 3 bug

#### 6. BUG-FUNC-DG-014 (Minor · P3 · ❌ Open) — Dropdown Lĩnh vực render UUID raw

- **SRS:** `srs-fr-08-danh-gia.md` SCR-VI-01 Tab 2 §Phân công row 36
- **Trạng thái R19:** Modal "Thêm người đánh giá" dropdown LV có 13 options, gồm 2 raw UUID: `e5d17437-e267-42ce-9dbe-aa2eebc1e477` + `bbbbbbbb-0000-4000-8000-000000000018`. FE chưa filter LV không có tên.
- **Acceptance:**
  - **FE:** Filter dropdown chỉ render LV có `tenDanhMuc` không null.
  - **BA confirm:** LV `bbbbbbbb-...-0018` UUID không tên — BA quyết giữ hay xóa, nếu giữ thì set tên Vietnamese.
- **Verify (UI):** Mở modal Thêm người đánh giá → dropdown LV không còn UUID raw.

#### 7. BUG-FE-TVCS-R16-005 (Major · P1 · ⚠️ Partial) — Thiếu button [Công khai]/[Hủy công khai]

- **SRS:** `srs-fr-12-tv-chuyen-sau.md` §Công khai TVCS DA_DUYET (BR-PUBLIC-01..03)
- **Trạng thái R19:** Panel 5/5 v3.5 field đã render OK (`Công khai`, `Thời gian đăng tải`, `Mô tả công khai`, `Ảnh đại diện`, `File đính kèm`). **Vẫn missing button action** [Công khai]/[Hủy công khai] để toggle workflow → user chỉ thấy read-only panel.
- **Acceptance — FE add button:**
  - Button [Công khai] khi TVCS `DA_DUYET` + `congKhai=false` → POST `/api/v1/tu-van-chuyen-saus/{id}/cong-khai`.
  - Button [Hủy công khai] khi `congKhai=true` → POST `/api/v1/tu-van-chuyen-saus/{id}/huy-cong-khai`.
- **Verify (UI):** TVCS-20260509-0002 (DA_DUYET) → button [Công khai]/[Hủy công khai] hiện + click toggle state thành công.

#### 8. BUG-VV-PC-WRN-01 (Minor · P2 · ❌ Open) — Modal Phân công thiếu button [Tìm thủ công]

- **SRS:** `srs-fr-05-vu-viec.md` SCR-V.II-01 §Phân công empty state + WRN-PC-01 line 768 + Acceptance line 778
- **Trạng thái R19:** R18 dev đã sửa text empty state khớp WRN-PC-01 ✅ nhưng **vẫn KHÔNG có nút [Tìm thủ công]** override action. Grep DOM `*` containing "tìm thủ công" → 0 hit.
- **Acceptance:** FE add button "Tìm thủ công" trong modal Phân công empty state, cho phép CB NV override search NHT/TVV ngoài LV phù hợp (theo Acceptance line 778).
- **Verify (UI):** Mở modal Phân công VV empty state → button [Tìm thủ công] hiện + click mở mode tìm override.

### Nhóm Dev FE + BE — 1 bug

#### 9. BUG-FUNC-TVN-005 (Minor · P3 · ❌ Open) — Dropdown Module audit-log thiếu option "Tư vấn"

- **SRS:** Audit log module list — phải có "Tư vấn" mapping `TU_VAN`
- **Trạng thái R19:** Dropdown Module trong Tư vấn nhanh có 12 enum (Tổng quan / HTQA / Đào tạo / Mạng lưới TVV / Vụ việc / Chi trả / DN / Đánh giá / Thư viện / Hỗ trợ DN / Báo cáo / QTHT). **KHÔNG có "Tư vấn"**.
- **Acceptance:**
  - **FE + BE:** Thêm enum `TU_VAN` (label "Tư vấn") vào danh mục module dropdown filter.
- **Verify (UI):** QTHT vào `/quan-tri/audit-log` (hoặc Tư vấn nhanh module filter) → dropdown có option "Tư vấn".

---

## Tóm lược ưu tiên (9 bug)

| Priority | Số bug | Bug ID |
|:-:|:-:|---|
| **P1 Major** | 4 | BUG-HDTV-034 · BUG-FE-TVCS-R16-005 · BUG-BE-TVCS-R16-001 · BUG-VV-FN-TVV-PERMISSION-GAP-01 |
| **P2 Medium** | 2 | BUG-CHITRA-010 · BUG-VV-PC-WRN-01 |
| **P3 Minor** | 3 | BUG-FUNC-DG-014 · BUG-FUNC-TVN-005 · BUG-VV-FN-LICHSU-01 |

**Lưu ý:** 0 bug P0 sau R19 (2 bug P0 cũ DG-013 + R17-008 đều ✅ Fixed).

---

## Bug đã đóng R19 — Đã loại khỏi danh sách (6 bug ✅ Fixed)

| Bug ID | Module | Sev | Verify R19 |
|---|---|:-:|---|
| BUG-FUNC-DG-013 | Đánh giá | Critical | QTHT vào DG detail: spinbutton=0, Hủy/Thêm/Xóa hidden cả Tab Tiêu chí + Tab Phân công — permission OK |
| BUG-FUNC-DG-010 | Đánh giá | Major | Thêm tiêu chí trọng số=30 → FE honor đúng (row=30, total=90) — KHÔNG force =100 nữa |
| BUG-FEBE-TVCS-R20-009 | TVCS | Major | Form `/tv-chuyen-sau/tao-moi` có dropdown "Vụ việc liên kết" + filter narrow `?doanhNghiepId` — DN-HNI-0015 total=2 OK |
| BUG-FE-TVCS-R16-004 | TVCS | Medium | NHT sidebar không còn "Quản lý tư vấn"; route `/tv-chuyen-sau/*` bounced về `/dao-tao/chuong-trinh/danh-sach` |
| BUG-BE-TVCS-R17-008 | TVCS | Major | NHT GET DN-003 happy=200 + DN cross-scope (001/002/004/005)=403 — row-level filter đúng FR-X.1-04 |
| BUG-CHITRA-009 | Chi trả | Minor | SRS `srs-fr-06-chi-tra.md` line 841 đã có "Tác nhân: Doanh nghiệp (qua DVC/Cổng PLQG) hoặc CB NV (thủ công)" |

---

## 4 bug đã loại trừ khỏi danh sách này (chờ phase tích hợp API ngoài)

Để dev tham khảo, KHÔNG fix nội bộ — chờ infra/external sandbox staging:

| Bug ID | Module | External dependency |
|---|---|---|
| BUG-CHITRA-008 | Chi trả | DVC LGSP gateway sandbox (FR-V.II-14 receiver sync HS bổ sung) |
| BUG-API-001 | Cross-cutting | mTLS cert client + sandbox staging (BR-INTG-02) |
| BUG-API-002 | Cross-cutting | 8/9 cặp outbound API publish cho external systems (FR-XII-01..18) |
| BUG-FUNC-TVN-008 | Tư vấn nhanh | Cổng PLQG CMS proxy `/cms-create` external integration |

---

## Lưu ý cho dev khi fix tiếp

1. **R16-001 regression cảnh báo:** từ 5 → 11 path 404 sau R16. Dev cần attach regression checklist endpoint touched + endpoint not-yet-implemented sau mỗi fix BE TVCS.
2. **3 bug "Nửa fix" cần done definition rõ:** HDTV-034 (FE route + BE 403), R16-005 (panel + button), VV-PC-WRN-01 (text + button). Đã list rõ "Acceptance — 2 surface phải fix cả 2".
3. **TVV-PERM-GAP-01 — sau khi BE thêm perm:** QA R20 sẽ test bằng UI thao tác (mở VV detail → click toolbar button) chứ không probe API direct, để bắt FE button missing nếu có.
4. **LICHSU-01 — verify 18 enum đầy đủ:** không nhận đóng partial, BE phải log đủ 4 enum còn miss (`TIEP_NHAN`/`TU_CHOI`/`TU_CHOI_DUYET`/`YEU_CAU_BO_SUNG`).

---

## Cách verify khi fix xong

Mỗi bug entry trong file bug-report tương ứng (link cột "File bug report") đã có:
- **Mô tả** (1-3 câu)
- **Các bước tái hiện** (đã rewrite UI thuần 2026-05-12 cho 6 bug Mixed)
- **Kết quả mong đợi** (theo SRS)
- **Kết quả thực tế** + Supporting network evidence
- **Bằng chứng** (screenshot inline)

Dev sau khi fix → QA chạy lại đúng bước tái hiện trên UI → so sánh với "Kết quả mong đợi" → đóng bug nếu khớp. R20 retest sẽ ưu tiên UI thao tác cho 4 bug Nhóm 2 (CHITRA-010 UI deadline column, LICHSU-01 Tab Dòng thời gian UI, TVV-PERM-GAP UI toolbar button, R16-001 UI button click).
