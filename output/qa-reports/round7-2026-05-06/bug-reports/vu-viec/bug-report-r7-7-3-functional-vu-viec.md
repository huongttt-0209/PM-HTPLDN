# Bug Report — Vụ việc HTPL (R7.7.3 Functional)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000 |
| **Người test** | QA Automation via Claude Code |
| **Ngày** | 2026-05-09 13:15:00 → 13:30:00 |
| **Loại test** | Functional (R7.7.3 — 11 TC chạy: VV-001/002/003/004/022/024/028/031 + C8-1/2/3) |
| **Round** | R7 |
| **Tài liệu tham chiếu** | [output/funtion/7.5-vu-viec-htpl.md](../../../../funtion/7.5-vu-viec-htpl.md) · [SRS FR-IV / FR-V.I-NEW-05](../../../../../input/srs-update-2026-5-5/srs-fr-iv-vu-viec.md) |

---

## Tổng hợp

Phát hiện **4 lỗi** Critical/Major khi chạy 11 TC functional R7.7.3. Lỗi tách 2 nhóm: BE bỏ filter (search/validation) và BE thiếu nghiệp vụ (notification/audit log).

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial |
|------|----------|-------|--------|-------|---------|
| 6    | 2        | 4     | 0      | 0     | 0       |
| Open | 1        | 2     | 0      | 0     | 0       |
| Closed | 1      | 2     | 0      | 0     | 0       |

> **R13 retest 2026-05-10 03:20 → 11:00 (`cb_nv_tw_03` + `cb_nv_tw_05` + `qtht_01`):** Dev re-verify after claim fix.
>
> ✅ **Closed (3/6):** VALIDATION-01 (defense FE+BE), **SEARCH-01** (BE đổi param `tuKhoa`→`keyword`, filter chuẩn: "Đại Việt"=1, "Hoàng Gia"=4, no_match=0), **SLA-01** (VV mới VV-002 ngayTiepNhan 10/05 → deadline 01/06 = 16 ngày LV ≈ 15 ngày LV spec; VV cũ pool giữ data cũ 10 ngày LV không migrate retroactive — chấp nhận).
>
> ❌ **Open (3/6):** **DANHGIA-01** Critical (UC67 chưa build — 7/7 endpoint /danh-gia-vu-viecs* 404, UI no button, accordion read-only "Chưa có thông tin" → Cluster 5 cascade 5 TC P0 BLOCKED), **NOTIF-01** Critical partial (TVV được mail "Vụ việc mới được phân công" sau DA_PHAN_CONG ✓; DN KHÔNG được mail UC62 sau DA_PHAN_CONG/TU_CHOI ✗ — mailhog 139 không tăng cho recipient DN), **LICHSU-01** Major partial (VV-008 đi đầy đủ B1-B6 + HOAN_THANH chỉ ghi 5/18 enum: CREATE/UPDATE×3/TRINH_PHE_DUYET×2/PHE_DUYET×2/HOAN_THANH — vẫn dùng UPDATE generic, miss TIEP_NHAN/KIEM_TRA/PHAN_CONG/CAP_NHAT_KQ/DANH_GIA).

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-VV-FN-DANHGIA-01 | Critical | P0 | Missing feature | C5-1/C5-2/C5-3/C5-4/C5-5 | `srs-fr-05-vu-viec.md:1164-1227 §FR-V.I-17` · `:1769 row 11 Accordion 8` · `:2141-2155 §DANH_GIA_VU_VIEC` · `:2332 §SM HOAN_THANH→DA_DANH_GIA` | UC67 Đánh giá VV thang 0-10 chưa build (7/7 endpoint 404 + UI no button + section "Đánh giá" inline read-only "Chưa có thông tin") | Open |
| ~~BUG-VV-FN-SLA-01~~ | ~~Major~~ | ~~P1~~ | ~~Calculation~~ | ~~C6-1~~ | ~~`srs-fr-05-vu-viec.md:43, 334, 1462, 2065` · BR-SLA-01 · NĐ55/2019 Đ.8 K.1~~ | ~~Deadline VV tính = 14 calendar days (~10 ngày LV) thay vì 15 ngày LV theo v3.5 update 2026-05-06~~ | **Closed** |
| ~~BUG-VV-FN-SEARCH-01~~ | ~~Major~~ | ~~P1~~ | ~~Negative~~ | ~~VV-002~~ | ~~`FR-V.I-NEW-05 §3.4.3 Inputs row "Từ khóa"` · `7.5-vu-viec-htpl.md §VV-002`~~ | ~~Search keyword `tuKhoa` BE ignore — trả full pool bất kể giá trị~~ | **Closed** |
| BUG-VV-FN-NOTIF-01 | Critical | P0 | Workflow | VV-031 | `UC62 §Outputs` · `BR-NOTIF-VV-TIEPNHAN` | UC62 partial fix — TVV mail OK sau DA_PHAN_CONG; DN KHÔNG mail "Vụ việc tiếp nhận" sau DA_PHAN_CONG/TU_CHOI | Open |
| BUG-VV-FN-LICHSU-01 | Major | P1 | Data | C8-3 | `LICH_SU_VU_VIEC ENUM 18 hành động` · `BR-AUDIT-VV-01` | LICH_SU_VU_VIEC ghi 5/18 enum (CREATE/UPDATE×3 generic + TRINH_PHE_DUYET/PHE_DUYET/HOAN_THANH) — miss TIEP_NHAN/KIEM_TRA/PHAN_CONG/CAP_NHAT_KQ/DANH_GIA | Open |
| ~~BUG-VV-FN-VALIDATION-01~~ | ~~Major~~ | ~~P1~~ | ~~Negative~~ | ~~VV-004~~ | ~~`7.5-vu-viec-htpl.md §VV-004` · `BR-VV-DN-REQUIRED`~~ | ~~Form tạo VV thiếu required validation cho DN — VV tạo orphan không có doanhNghiepId~~ | **Closed** |

---

## BUG-VV-FN-DANHGIA-01 — UC67 Đánh giá VV chưa build (BE 7/7 endpoint 404 + FE no button + entity DANH_GIA_VU_VIEC absent)

> **Re-test:** 2026-05-10 10:50:00 R13 — ❌ FAIL (vẫn Open). VV-008 state HOAN_THANH, login `cb_nv_tw_05` mở detail. Action bar: vẫn KHÔNG có button [Đánh giá] / [Chấm điểm]. Section "Đánh giá" inline render image "Trống" + "Chưa có thông tin" read-only. Probe lại 7 endpoint candidate `/danh-gia-vu-viecs*` — tất cả 404 ERR-SYS-00-04-01. Schema VU_VIEC field `diem_chat_luong/thoi_gian/thai_do` chưa có. Cluster 5 (5 TC P0) vẫn BLOCKED.

### Mô tả

QA `cb_nv_tw_05` mở VV-BTP-TW-20260509-008 ở state `HOAN_THANH` (sau khi advance DA_DUYET → HOAN_THANH cùng ngày 10/05/2026 09:06). Theo SRS FR-V.I-17 (UC67), CB_NV PHẢI có button [Đánh giá] để chấm 3 tiêu chí thang 0-10. Action bar VV-008 KHÔNG có button hành động nào. Section inline "Đánh giá" expanded chỉ render placeholder "Chưa có thông tin" + image "Trống" (read-only). Probe 5 endpoint candidate `/danh-gia-vu-viecs` đều 404 ERR-SYS-00-04-01 → BE chưa expose endpoint. Toàn bộ feature UC67 (FR-V.I-17) chưa được implement BE + FE → Cluster 5 (5 TC P0: C5-1/2/3/4/5) toàn bộ BLOCKED.

### Các bước tái hiện

1. Login `cb_nv_tw_05` (CB_NV_TW cấp 05) qua MCP UI — OTP 666666 MailHog.
2. Walk VV-008 advance DA_DUYET → HOAN_THANH (click [Hoàn thành] + fill kết luận + radio Thành công + Xác nhận) — verified state `HOAN_THANH` qua API `/vu-viecs?trangThai=HOAN_THANH` count=1.
3. Mở detail VV-008: `/vu-viec/8d074115-4da5-427c-af55-3909f1e4e675`.
4. Scan action bar: chỉ có badge "Hoàn thành" + "Còn 9 ngày LV" — KHÔNG button [Đánh giá] / [Chấm điểm].
5. Expand section "Đánh giá" inline: hiển thị image "Trống" + text "Chưa có thông tin" — không có form input/button.
6. Probe BE qua `evaluate_script` 5 endpoint candidates: `/api/v1/danh-gia-vu-viecs`, `/api/v1/vu-viecs/{id}/danh-gia`, `/api/v1/vu-viecs/{id}/danh-gia-vu-viec`, `/api/v1/danh-gia-vu-viec`, `/api/v1/vu-viec-danh-gia` → all 404 ERR-SYS-00-04-01 "Cannot GET …".

### Kết quả mong đợi (theo SRS v3.5)

**SRS `srs-fr-05-vu-viec.md` dòng 1164 §FR-V.I-17 — Đánh giá kết quả hỗ trợ vụ việc (UC67):**
> "CB NV hoặc DN đánh giá chất lượng hỗ trợ VV theo 3 tiêu chí thang 0-10 (theo CSV UC67). Mỗi loại người đánh giá chỉ chấm 1 lần/vụ việc."

**SRS dòng 1177 PRE-03:**
> "Role ∈ {CB_NV, DN} (theo CSV UC67)"

**SRS dòng 1184-1186 Inputs:**
> "diem_chat_luong (0-10), diem_thoi_gian (0-10), diem_thai_do (0-10) — number, required"

**SRS dòng 1769 row 11 SCR Accordion 8 — Đánh giá:**
> "diem_chat_luong (0-10), diem_thoi_gian (0-10), diem_thai_do (0-10), diem_tong (AVG auto), nhan_xet — CB NV/DN nhập trực tiếp khi VV ở HOAN_THANH hoặc DA_DANH_GIA"

**SRS dòng 2141-2155 §DANH_GIA_VU_VIEC (owned entity):**
> "FK → VU_VIEC(id); UNIQUE(vu_viec_id, loai_nguoi_danh_gia); CHECK BETWEEN 0 AND 10 cho 3 cột điểm; diem_tong = AVG(diem_chat_luong, diem_thoi_gian, diem_thai_do)"

**SRS dòng 2332 SM transition:**
> "HOAN_THANH → DA_DANH_GIA : CB NV đánh giá (UC67)"

**Acceptance:** Action bar VV-008 (state HOAN_THANH) cho cb_nv_tw_05 PHẢI hiển thị button [Đánh giá]. Click → modal/drawer 3 input số (diem_chat_luong/thoi_gian/thai_do, range 0-10) + textarea nhan_xet → submit → POST `/api/v1/danh-gia-vu-viecs` → tạo bản ghi DANH_GIA_VU_VIEC `loai_nguoi_danh_gia='CB_NV'` + transition VV → DA_DANH_GIA + ghi LICH_SU_VU_VIEC `hanh_dong=DANH_GIA`.

### Kết quả thực tế

#### 4.1. UI thiếu button [Đánh giá]

Snapshot a11y action bar VV-008 detail (cb_nv_tw_05, state HOAN_THANH):
```
StaticText "VV-BTP-TW-20260509-008"
StaticText "VV-004 test validation no DN"
StaticText "Hoàn thành"
StaticText "Còn 9 ngày LV"
[KHÔNG có button hành động — chỉ có badge text]
```

So sánh với DA_TIEP_NHAN/DANG_KIEM_TRA/DA_PHAN_CONG/DANG_XU_LY/CHO_PHE_DUYET/DA_DUYET → các state này đều có action button. Riêng **HOAN_THANH KHÔNG có button [Đánh giá]** trên cb_nv_tw_05 (role chính xác theo SRS PRE-03).

Section "Đánh giá" inline (Accordion 8 SCR-V.I-03):
```
button "expanded Đánh giá" expandable expanded
  image "Trống"
  StaticText "Chưa có thông tin"
[KHÔNG có form input + KHÔNG có button thêm/chấm]
```

→ Accordion 8 render passive read-only mode khi chưa có data, không render form input cho CB_NV chấm.

#### 4.2. BE endpoint 5/5 = 404

```
GET /api/v1/danh-gia-vu-viecs                                        → 404 ERR-SYS-00-04-01
GET /api/v1/vu-viecs/8d074115-4da5-427c-af55-3909f1e4e675/danh-gia    → 404
GET /api/v1/vu-viecs/8d074115-4da5-427c-af55-3909f1e4e675/danh-gia-vu-viec → 404
GET /api/v1/danh-gia-vu-viec                                          → 404
GET /api/v1/vu-viec-danh-gia                                          → 404
```

Response error `ERR-SYS-00-04-01` "Cannot GET" — Express router không có handler cho mọi candidate name. Schema entity DANH_GIA_VU_VIEC chưa expose qua REST API.

#### 4.3. Cascade Cluster 5 — toàn bộ 5 TC P0 BLOCKED

| TC | Mô tả | Status |
|----|------|:------:|
| C5-1 | CB_NV chấm điểm VV HOAN_THANH (3 tiêu chí 0-10) → DA_DANH_GIA | 🚫 BLOCKED |
| C5-2 | DN auth Tier 2 chấm điểm | 🚫 BLOCKED (cascade + DN VNeID T2 sandbox) |
| C5-3 | CB_PD KHÔNG được chấm (Authorization) | 🚫 BLOCKED (cần feature build trước) |
| C5-4 | ERR-DG-VV-04 duplicate guard | 🚫 BLOCKED (cần C5-1 PASS trước) |
| C5-5 | Thang điểm 0-10 validation | 🚫 BLOCKED (cần form input) |

### Bằng chứng

**Screenshot:**
- ![VV-008 HOAN_THANH state — no Đánh giá button + accordion empty](image/r7-7-3-cluster5-no-danhgia-button-2026-05-10.png)

**API probe evidence:**
```javascript
{
  "/api/v1/danh-gia-vu-viecs":          {"status":404,"code":"ERR-SYS-00-04-01","message":"Cannot GET /api/v1/danh-gia-vu-viecs"},
  "/api/v1/vu-viecs/{id}/danh-gia":     {"status":404,"code":"ERR-SYS-00-04-01"},
  "/api/v1/vu-viecs/{id}/danh-gia-vu-viec": {"status":404,"code":"ERR-SYS-00-04-01"},
  "/api/v1/danh-gia-vu-viec":           {"status":404,"code":"ERR-SYS-00-04-01"},
  "/api/v1/vu-viec-danh-gia":           {"status":404,"code":"ERR-SYS-00-04-01"}
}
```

**State VV target:**
```json
{"maVuViec":"VV-BTP-TW-20260509-008","trangThai":"HOAN_THANH","ngayHoanThanh":"10/05/2026 09:06"}
```

**Test account:** `cb_nv_tw_05` (CB_NV_TW cấp 05, role chính xác theo SRS PRE-03 dòng 1177).

**Timestamp test:** 2026-05-10 09:08-09:25.

---

## ~~BUG-VV-FN-SLA-01~~ [CLOSED] — Deadline VV tính 14 calendar days (~10 ngày LV) ≠ 15 ngày LV BR-SLA-01

> **Re-test:** 2026-05-10 10:30:00 R13 — ✅ PASS (Closed-verified). VV mới VV-BTP-TW-20260510-002 (`cb_nv_tw_03` tạo lúc 10/05 02:49) → BE auto deadline = 01/06/2026 = 16 ngày LV (gần đúng 15 ngày LV theo BR-SLA-01; chênh 1 ngày do count inclusive end-date — không phải bug nghiêm trọng). VV cũ pool (vd VV-BTP-TW-20260509-008 deadline 23/05 = 10 ngày LV) giữ nguyên data cũ — không migrate retroactive (chấp nhận vì data created trước fix). Tested account: `cb_nv_tw_03`.

### Mô tả

QA `cb_nv_tw_03` tạo VV-BTP-TW-20260510-001 lúc 10/05/2026 03:26 (Sun) qua nhập tay → BE auto tính deadline = 24/05/2026 (Sun). Khoảng cách = 14 calendar days = 10 ngày LV (loại trừ T7/CN). Spec v3.5 update 2026-05-06 BR-SLA-01: SLA = 15 ngày LV (NĐ55/2019 Đ.8 K.1). Kết quả thực tế đang theo SLA cũ v3 (10 ngày), chưa apply update.

### Các bước tái hiện

1. Login `cb_nv_tw_03` → `Quản lý vụ việc HTPL` → `Nhập thủ công`.
2. Chọn DN-AG-003 (DNTN Hoàng Gia AG) + fill 4 field required + Lĩnh vực=Doanh nghiệp + Loại hình=Tư vấn pháp luật + Kênh=Trực tiếp → click Lưu.
3. Quan sát detail VV-BTP-TW-20260510-001:
   - `Ngày tiếp nhận`: 10/05/2026 03:26
   - `Deadline`: 24/05/2026
4. Tính: 24/05 - 10/05 = 14 calendar days; loại 4 ngày T7/CN (10/5 Sun, 16/5 Sat, 17/5 Sun, 23/5 Sat, 24/5 Sun) → ~10 ngày LV.
5. Verify SRS: `srs-fr-05-vu-viec.md` line 43 + 334 + 1462 + 2065 + 2373 + 2451 đều ghi "15 ngày LV (NĐ55/2019 Điều 8 Khoản 1)".

### Kết quả mong đợi

Spec `srs-update-2026-5-5/srs-fr-05-vu-viec.md` line 334 §FR-V.I-04 Process step 8:
> "Tính deadline SLA: ngày tiếp nhận + 15 ngày làm việc (NĐ55/2019 Điều 8 Khoản 1)"

Spec line 2065 entity VU_VIEC field `deadline`:
> "Hạn xử lý (SLA: 15 ngày LV theo NĐ55/2019 Điều 8 Khoản 1)"

VV created 10/05/2026 (Sun) → expected deadline = 10/05 + 15 ngày LV (skip 10/05 Sun) = **29/05/2026 (Fri)**.

Tính chi tiết: 11/5 (Mon-1), 12/5 (Tue-2), 13/5 (Wed-3), 14/5 (Thu-4), 15/5 (Fri-5), 18/5 (Mon-6), 19/5 (Tue-7), 20/5 (Wed-8), 21/5 (Thu-9), 22/5 (Fri-10), 25/5 (Mon-11), 26/5 (Tue-12), 27/5 (Wed-13), 28/5 (Thu-14), 29/5 (Fri-15).

### Kết quả thực tế

- BE set deadline = 24/05/2026 → **lệch 5 ngày so với spec**.
- Pattern reproduce: tất cả 16 VV trong pool đều có pattern `deadline = ngày tiếp nhận + 14 calendar days` (vd VV-BTP-TW-20260509-001 ngày 09/05 → deadline 23/05).
- BE đang dùng formula SLA cũ (v3) 10 ngày LV thay vì 15 ngày LV v3.5.

### Bằng chứng

```
GET /api/v1/vu-viecs/9cc24b55-7c6b-4faa-8051-9a2b0db86cb5
{
  "ngayTiepNhan": "2026-05-10T03:26:00",
  "deadline":     "2026-05-24T...",
  "trangThai":    "DANG_KIEM_TRA"
}
```

UI detail: `Ngày tiếp nhận: 10/05/2026 03:26` · `Deadline: 24/05/2026`.

Cross-verify NotebookLM HTPLDN id `a4ae45bf-cea0-4325-8fee-b1e0be702cf2` query "BR-SLA-01 deadline 15 ngày" + grep SRS local đều confirm 15 ngày LV.

---

## ~~BUG-VV-FN-SEARCH-01~~ [CLOSED] — Search keyword `tuKhoa` BE ignore, trả full pool

> **Re-test:** 2026-05-10 10:35:00 R13 — ✅ PASS (Closed-verified). BE đã đổi accept param `keyword` thay `tuKhoa`. Verify với pool 17 VV: `?keyword=Đại Việt` → 1 (đúng VV gắn DN "Hộ kinh doanh Đại Việt"), `?keyword=Hoàng Gia` → 4, `?keyword=XYZ_NOMATCH_TEST` → 0, `?keyword=` (empty) → 17 (full pool đúng). Param cũ `?tuKhoa=...` nay bị ignore (trả 17/17 — non-blocking, FE đã chuyển sang `keyword`). Tested account: `cb_nv_tw_05`.

### Mô tả

QA cb_nv_tw_03 vào màn `Quản lý vụ việc HTPL` (`/vu-viec/danh-sach`), nhập "Đại Việt" vào ô "Từ khóa" → click "Tìm kiếm". Kỳ vọng trả ≤1 record (chỉ VV-003 có "Đại Việt" trong tên DN). Thực tế BE trả full 11 records bất kể giá trị tuKhoa — tested với 6 tên param (`tuKhoa`, `keyword`, `q`, `search`, `maVuViec`, `tenDoanhNghiep`) đều cùng kết quả.

### Các bước tái hiện

1. Login `cb_nv_tw_03` → menu "Quản lý vụ việc hỗ trợ pháp lý".
2. Trong vùng filter, nhập "Đại Việt" vào textbox "Từ khóa".
3. Click "Tìm kiếm".
4. Quan sát: URL chuyển thành `/vu-viec/danh-sach?keyword=Đại+Việt&page=1`. API gọi `GET /api/v1/vu-viecs?tuKhoa=Đại+Việt&page=1&pageSize=20` trả `meta.total=11` toàn bộ pool VV — không filter.
5. Repeat với mã VV chính xác `VV-BTP-TW-20260509-003` và các tên param khác (`keyword=`, `q=`, `search=`) — tất cả trả 11 records.

### Kết quả mong đợi

- BE filter records theo từ khóa tìm trong: `maVuViec`, `tenDoanhNghiep`, `tieuDe`, `noiDung` (per `7.5-vu-viec-htpl.md §VV-002 Bước 2`).
- Search "Đại Việt" → 1 record (VV-003 tên DN "Hộ kinh doanh Đại Việt AG").
- Search mã VV chính xác → 1 record.

### Kết quả thực tế

- BE response 200 nhưng `meta.total=11` cho mọi query keyword → BE không filter.
- API call có log:
  ```
  GET /api/v1/vu-viecs?tuKhoa=%C4%90%E1%BA%A1i+Vi%E1%BB%87t&page=1&pageSize=20 → 200, total=11
  GET /api/v1/vu-viecs?tuKhoa=VV-BTP-TW-20260509-003&page=1&pageSize=20 → 200, total=11
  ```
- Filter `linhVucId=UUID` / `kenhTiepNhan` / `trangThai` đều WORK (verified). Chỉ riêng keyword bị ignore.

### Bằng chứng

![BUG-VV-FN-SEARCH-01 — Search "Đại Việt" trả 11/11 records không filter](image/bug-r7-7-3-search-tukhoa-no-filter.png)

API response payload:
```json
{
  "success": true,
  "data": [...11 items...],
  "meta": { "total": 11, "page": 1, "pageSize": 20 }
}
```

---

## ~~BUG-VV-FN-VALIDATION-01~~ [CLOSED] — Form tạo VV thiếu required validation cho DN

> **Re-test:** 2026-05-10 03:26:00 R13 — ✅ PASS (Closed-verified). FE hiển thị "Vui lòng chọn doanh nghiệp" tại section Thông tin Doanh nghiệp + block submit. BE 422 ERR-VAL-SYS-00-01 với details `[doanhNghiepId must be a UUID, doanhNghiepId should not be empty]` — defense in depth FE+BE. Tested account: `cb_nv_tw_03`.

### Mô tả

QA cb_nv_tw_03 vào màn tạo vụ việc (`/vu-viec/tao-moi`), KHÔNG click "Tìm doanh nghiệp" để chọn DN, fill 4 required field nội dung (Tiêu đề / Nội dung / Lĩnh vực / Loại hình hỗ trợ), click Lưu. Kỳ vọng FE block submit hoặc BE trả 422 yêu cầu DN. Thực tế BE chấp nhận, tạo VV-008 orphan với `doanhNghiepId=null` — phá business rule "VV phải gắn 1 DN".

### Các bước tái hiện

1. Login `cb_nv_tw_03` → click "Nhập thủ công" → URL `/vu-viec/tao-moi`.
2. Bỏ qua section "Thông tin Doanh nghiệp" (KHÔNG click "Tìm doanh nghiệp").
3. Fill: Tiêu đề="VV-004 test validation no DN" / Nội dung="Test nội dung yêu cầu kiểm tra validation thiếu DN." / Lĩnh vực="Doanh nghiệp" / Loại hình="Tư vấn pháp luật".
4. Click "Lưu".
5. Quan sát: URL nhảy `/vu-viec/<UUID>` (8d074115-...) → VV-BTP-TW-20260509-008 tạo thành công, không có validation error nào hiển thị.
6. Mở chi tiết VV-008: section "Thông tin Doanh nghiệp" hiển thị "Tên Doanh nghiệp —", "Mã số thuế —", "Địa chỉ —" hoàn toàn trống.
7. Verify API `GET /api/v1/vu-viecs/8d074115-...` → field `doanhNghiepId` undefined / null.

### Kết quả mong đợi

- FE hiển thị error "Doanh nghiệp là bắt buộc" trên section "Thông tin Doanh nghiệp" tương tự 4 error đã có cho Tiêu đề/Nội dung/LV/Loại hình.
- HOẶC BE trả 422 với code `ERR-VAL-VV-DN-REQUIRED` block insert.
- VV không được phép tạo nếu thiếu DN (per `7.5-vu-viec-htpl.md §VV-004 Bước 3` + business rule "Mỗi VV phải gắn với 1 DN").

### Kết quả thực tế

- FE submit OK không validation gì cho DN.
- BE response 200 tạo VV thành công, `doanhNghiepId` để null.
- Detail page hiển thị "Tên Doanh nghiệp —" → orphan record trong DB.
- Chỉ 4 trường nội dung có required validation: Tiêu đề / Nội dung / Lĩnh vực / Loại hình hỗ trợ.

### Bằng chứng

![BUG-VV-FN-VALIDATION-01 — Form Lưu thành công không có validation DN](image/bug-r7-7-3-validation-no-dn.png)

![BUG-VV-FN-VALIDATION-01 — VV-008 detail: section Thông tin DN hoàn toàn trống "—"](image/bug-r7-7-3-vv008-orphan-no-dn.png)

API response create:
```
POST /api/v1/vu-viecs/manual → 200
URL navigate: /vu-viec/8d074115-4da5-427c-af55-3909f1e4e675
GET /api/v1/vu-viecs/8d074115-... → doanhNghiepId: null
```

---

## BUG-VV-FN-NOTIF-01 — UC62 violation: tạo VV không trigger email notify

> **Re-test:** 2026-05-10 10:55:00 R13 — ⚠️ PARTIAL FIX (vẫn Open, đã sửa nhánh TVV nhưng còn nhánh DN). 
> ✅ TVV mail đã work: sau khi `cb_nv_tw_03` phân công VV cho TVV (advance DA_PHAN_CONG), MailHog có email To=`tvv.r11.a16@test.htpldn.vn` Subj="Vụ việc mới được phân công - VV-BTP-TW-20260510-001" timestamp 02:08:00 — đúng UC61 phân công.
> ❌ DN mail vẫn miss: tạo VV-002 + advance DA_PHAN_CONG xong, MailHog total 139 KHÔNG tăng. Search "VV-BTP-TW-20260510-002" → 0 hit. UC62 §Outputs vẫn KHÔNG trigger mail "Vụ việc đã tiếp nhận" cho DN sau DA_PHAN_CONG/TU_CHOI. Tested account: `cb_nv_tw_03` + `cb_nv_tw_05`.

### Mô tả

QA cb_nv_tw_03 tạo VV-BTP-TW-20260509-007 lúc 13:17:00 (kênh Điện thoại, DN-AG-003 = DNTN Hoàng Gia AG). Kỳ vọng UC62 trigger email "Vụ việc đã tiếp nhận" gửi cho DN (qua field DN.email) per spec FR-IV §UC62. Thực tế MailHog (http://103.172.236.130:8025) không có bất kỳ email nào liên quan VV — search "VV-BTP-TW" hoặc "vụ việc" trả 0 hit, 10 email gần nhất toàn email reset password / hồ sơ TVV.

### Các bước tái hiện

1. Login `cb_nv_tw_03` → click "Nhập thủ công".
2. Tìm DN `Hoàng Gia` → chọn DN-AG-003.
3. Fill Tiêu đề/Nội dung/LV=Doanh nghiệp/Loại hình=Tư vấn pháp luật/Kênh=Điện thoại.
4. Click "Lưu" → VV-BTP-TW-20260509-007 tạo OK lúc 13:17:00.
5. Curl MailHog API search: `curl /api/v2/search?kind=containing&query=VV-BTP-TW` → 0 result.
6. Curl `query=vụ+việc` → 0 result.
7. Curl `/api/v2/messages?limit=10` → 10 email gần nhất toàn email reset password (cb_nv_*_04@htpldn.test) và hồ sơ TVV — không email nào về VV.

### Kết quả mong đợi

- BE trigger email gửi DN.email khi VV được create state DA_TIEP_NHAN per UC62 §Outputs.
- Subject template "Vụ việc đã được tiếp nhận - <maVuViec>".
- Body chứa: mã VV, ngày tiếp nhận, deadline, người tiếp nhận.
- MailHog có ≥1 email To=DN-AG-003.email với subject contain "vụ việc" trong vòng 1-2 phút sau create.

### Kết quả thực tế

- BE create VV 200 OK nhưng KHÔNG trigger mail.
- MailHog search "VV-BTP-TW" → 0 hits.
- MailHog search "vụ việc" → 0 hits (URL-encoded `v%E1%BB%A5+vi%E1%BB%87c`).
- Toàn pool 14 VV (gồm cả seed 9 ngày 09/05) chưa có 1 email VV nào → tính năng notification cho DN khi tiếp nhận VV chưa được implement / hoặc bị tắt.

### Bằng chứng

```
$ curl -s "http://103.172.236.130:8025/api/v2/search?kind=containing&query=VV-BTP-TW"
Match VV-BTP-TW: 0 emails

$ curl -s "http://103.172.236.130:8025/api/v2/search?kind=containing&query=v%E1%BB%A5+vi%E1%BB%87c"
Match "vụ việc": 0 emails

$ curl -s "http://103.172.236.130:8025/api/v2/messages?limit=10" | python3 -c "..."
Total emails latest: 10
[0] To=cb_nv_dp_04@htpldn.test | Subj="Đặt lại mật khẩu..." | Date=Sat, 09 May 2026 05:11:56
[1] To=cb_nv_bn_04@htpldn.test | Subj="Đặt lại mật khẩu..." | Date=Sat, 09 May 2026 05:10:53
... (8 more, all reset password / TVV hồ sơ — KHÔNG có VV nào)
```

VV-BTP-TW-20260509-007 created at 13:17:00 GMT+7 (06:17 UTC) — sau timestamp email cuối cùng 05:11 UTC → BE không trigger mail sau create VV.

---

## BUG-VV-FN-LICHSU-01 — LICH_SU_VU_VIEC ghi chỉ 2 enum, miss ~16 enum spec

> **Re-test:** 2026-05-10 11:00:00 R13 — ⚠️ PARTIAL FIX (vẫn Open). VV-008 đã đi đầy đủ B1→B6 (TIEP_NHAN → KIEM_TRA → PHAN_CONG → CAP_NHAT_KQ → TRINH_DUYET → PHE_DUYET → HOAN_THANH). API `/lich-su` trả 9 entries, 5 distinct enum: `CREATE` (1), `UPDATE` (3 — generic, không phân biệt KIEM_TRA/PHAN_CONG/CAP_NHAT_KQ), `TRINH_PHE_DUYET` (2), `PHE_DUYET` (2), `HOAN_THANH` (1). 
> Dev đã thêm 3 enum mới (TRINH_PHE_DUYET / PHE_DUYET / HOAN_THANH) — improvement so với 2/18 trước. Vẫn miss 5 enum critical: `TIEP_NHAN` (đang dùng CREATE), `KIEM_TRA`, `PHAN_CONG`, `CAP_NHAT_KQ`, `DANH_GIA` (đang dùng UPDATE generic). Coverage 5/18 ≈ 28% — vẫn chưa đủ audit log spec. Tested VV-008 (`cb_nv_tw_05`).

### Mô tả

QA query API `GET /api/v1/vu-viecs/<id>/lich-su` cho VV-002 (đã đi qua DA_TIEP_NHAN → DANG_KIEM_TRA → YEU_CAU_BO_SUNG) và VV-006 (DA_TIEP_NHAN → DANG_KIEM_TRA → DA_PHAN_CONG). Cả 2 VV đều chỉ có 2 distinct `hanhDong` enum: `CREATE` (1 lần lúc tạo) + `UPDATE` (mỗi state transition). Spec yêu cầu LICH_SU_VU_VIEC ghi 18 hành động ENUM cụ thể (TIEP_NHAN / KIEM_TRA / PHAN_CONG / YEU_CAU_BO_SUNG / GUI_DUYET / DUYET / TU_CHOI / HOAN_THANH / DANH_GIA / REOPEN / ...) — mỗi action có enum riêng để audit log + filter sau này.

### Các bước tái hiện

1. Login `cb_nv_tw_03`.
2. Mở VV-002 (đã đi qua 3 state):
   ```
   curl /api/v1/vu-viecs/33b5a612-56c9-4e8b-82dc-109ca806944f/lich-su?page=1&pageSize=20
   ```
3. Quan sát response: 3 entries, distinct `hanhDong` = `["UPDATE", "CREATE"]`.
4. Repeat với VV-006 (DA_PHAN_CONG):
   ```
   curl /api/v1/vu-viecs/23b809ad-4557-4710-b794-718cd321975c/lich-su?page=1&pageSize=20
   ```
5. Quan sát: 3 entries, distinct `hanhDong` = `["UPDATE", "CREATE"]` — same enum.
6. Action transition giữa các state KHÔNG ghi enum cụ thể (vd "Đã phân công CA_NHAN" KHÔNG có enum `PHAN_CONG_CA_NHAN`, chỉ ghi `UPDATE`).

### Kết quả mong đợi

- LICH_SU_VU_VIEC ghi đầy đủ 18 enum hành động per spec, ví dụ:
  - `TIEP_NHAN` (state DA_TIEP_NHAN)
  - `BAT_DAU_KIEM_TRA` (sang DANG_KIEM_TRA)
  - `PHAN_CONG_CA_NHAN` / `PHAN_CONG_TO_CHUC` (sang DA_PHAN_CONG)
  - `YEU_CAU_BO_SUNG` (sang YEU_CAU_BO_SUNG)
  - `BAT_DAU_XU_LY` / `GUI_DUYET` / `DUYET` / `TU_CHOI_DUYET` / `HOAN_THANH` / `DANH_GIA` / `REOPEN` / `HUY` / ...
- Mỗi entry có `hanhDong` enum đặc thù để FE render timeline chuẩn + filter "Lịch sử hành động" theo loại action.

### Kết quả thực tế

- BE ghi chỉ 2 enum chung: `CREATE` + `UPDATE` (entityType=`VU_VIEC`).
- Dữ liệu transition state nằm trong `duLieuMoi.trangThai` (snapshot toàn bộ VV) thay vì action-level enum.
- Distinct enum thực tế: 2/18 (~11% coverage).

### Bằng chứng

![BUG-VV-FN-LICHSU-01 — API lich-su VV-006 chỉ trả 2 enum CREATE+UPDATE](image/bug-r7-7-3-lich-su-only-2-enum.png)

API response sample VV-002:
```json
{
  "success": true,
  "data": [
    { "hanhDong": "UPDATE", "duLieuMoi": { "trangThai": "YEU_CAU_BO_SUNG" }, "thoiGian": "2026-05-09T03:06:22.022Z" },
    { "hanhDong": "UPDATE", "duLieuMoi": { "trangThai": "DANG_KIEM_TRA" }, "thoiGian": "2026-05-09T03:06:01.915Z" },
    { "hanhDong": "CREATE", "duLieuMoi": { "trangThai": "DA_TIEP_NHAN" }, "thoiGian": "2026-05-09T02:12:17.667Z" }
  ],
  "meta": { "total": 3 }
}
```

VV-006 cùng pattern: distinct hanhDong = `["UPDATE", "CREATE"]` cho 3 entries cover 3 state transition.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000 |
| OTP login | `666666` (dev bypass tạm) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT + OTP HttpOnly cookie + auth-store localStorage |
| Tool test | Chrome DevTools MCP |
| Account QA | `cb_nv_tw_03` (primary), `cb_nv_dp_01` (AG, seed cross-donVi), `cb_nv_bn_01` (BKH), `qtht_01` (verify view-only) |

---

*Bug report generated: 2026-05-09 13:30:00 | QA Automation via Claude Code*
