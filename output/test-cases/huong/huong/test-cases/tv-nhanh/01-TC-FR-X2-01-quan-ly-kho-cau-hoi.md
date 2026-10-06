# Test Case — FR-X.2-01 Quản lý Kho Câu hỏi (UC154/155/157)

> **File:** `01-TC-FR-X2-01-quan-ly-kho-cau-hoi.md`
> **FR:** FR-X.2-01 (UC154 quản lý kho + UC155 phê duyệt inline + UC157 tìm kiếm CB NV)
> **SCR:** SCR-X2-01 — Quản lý Kho Câu hỏi (gộp MH-13.1 + MH-13.2 v2.1)
> **SRS Reference:** [`srs-fr-13-tv-nhanh-v3.1.md`](../../../input/srs-v3/srs-fr-13-tv-nhanh-v3.1.md) §FR-X.2-01 line 80-167, §SCR-X2-01 line 515-545
> **Loại:** B (browser, MCP chrome-devtools)

## TC Index

| TC ID | Tên TC | Trace | Tag | Role |
|-------|--------|-------|-----|------|
| TC-KHO-001 | Hiển thị danh sách Kho Q&A | FR-X.2-01 / AC1 | Happy | CB_NV_TW |
| TC-KHO-002 | Tab phân loại 3 (Tất cả / Đã duyệt / Chờ duyệt) | FR-X.2-01 / SCR row 3 | Happy | CB_NV_TW |
| TC-KHO-003 | Thêm Q&A thủ công - happy path → CHO_DUYET | FR-X.2-01 / AC2 | Happy | CB_NV_TW |
| TC-KHO-004 | Thêm Q&A với ảnh đại diện + mô tả công khai + file đính kèm | FR-X.2-01 / Inputs | Happy | CB_NV_TW |
| TC-KHO-005 | Lưu nháp (NHAP) — chưa Gửi duyệt | FR-X.2-01 / SCR row 8 | Happy | CB_NV_TW |
| TC-KHO-006 | Sửa Q&A NHAP của mình | FR-X.2-01 / Processing 3 | Happy | CB_NV_TW |
| TC-KHO-007 | Xóa Q&A NHAP (soft delete BR-DATA-01) | FR-X.2-01 / BR-DATA-01 | Happy | CB_NV_TW |
| TC-KHO-008 | Toggle hieu_luc DA_DUYET → HET_HIEU_LUC + ẩn khỏi Cổng | FR-X.2-01 / Processing 6 | Happy | CB_NV_TW |
| TC-KHO-009 | Auto-tạo từ HOI_DAP DA_DUYET (nguồn TU_DONG) | FR-X.2-01 / Processing 2 + BR-FLOW-10 | Happy cross-FR | CB_NV_TW |
| TC-KHO-010 | Phê duyệt đơn lẻ tab "Chờ duyệt" → DA_DUYET + hieu_luc=1 | FR-X.2-01 / SCR row 10 | Happy | CB_PD_TW |
| TC-KHO-011 | Từ chối đơn lẻ (modal lý do bắt buộc) → NHAP + TB CB NV | FR-X.2-01 / SCR row 10 | Happy | CB_PD_TW |
| TC-KHO-012 | Phê duyệt hàng loạt (≥1 checkbox) → modal xác nhận | FR-X.2-01 / SCR row 11 | Happy | CB_PD_TW |
| TC-KHO-013 | Import Excel - happy path → preview 10 dòng đầu + N thành công M lỗi | FR-X.2-01 / Processing 4 | Happy | CB_NV_TW |
| TC-KHO-014 | Tìm kiếm full-text (UC157 BR-DATA-08) | FR-X.2-01 / Processing 5 + BR-DATA-08 | Happy | CB_NV_TW |
| TC-KHO-015 | Lọc theo lĩnh vực + nguồn + trạng thái | FR-X.2-01 / SCR row 4 | Happy | CB_NV_TW |
| TC-KHO-016 | Phân trang 20 mục/trang | BR-DATA-07 | Happy | CB_NV_TW |
| TC-KHO-017 | Mã Q&A auto-gen QA-YYYYMMDD-SEQ | BR-DATA-04 | Happy | CB_NV_TW |
| TC-KHO-018 | AUDIT_LOG ghi nhận CRUD + duyệt | BR-DATA-05 | Happy | CB_NV_TW |
| TC-KHO-100 | E1 — câu hỏi trống → ERR-KHO-01 | FR-X.2-01 / E1 | Negative | CB_NV_TW |
| TC-KHO-101 | E2 — câu trả lời trống → ERR-KHO-02 | FR-X.2-01 / E2 | Negative | CB_NV_TW |
| TC-KHO-102 | E3 — lĩnh vực không hợp lệ → ERR-KHO-03 | FR-X.2-01 / E3 | Negative | CB_NV_TW |
| TC-KHO-103 | E4 — file Excel sai format → ERR-KHO-04 | FR-X.2-01 / E4 | Negative | CB_NV_TW |
| TC-KHO-104 | Sửa Q&A của đơn vị khác → 403 / 404 (BR-AUTH-08) | BR-AUTH-08 | Negative cross-tenant | CB_NV_DP_02 |
| TC-KHO-105 | Phê duyệt cross-cấp (PD_TW phê duyệt Q&A cấp ĐP) → block (BR-AUTH-05) | BR-AUTH-05 | Negative cross-cấp | CB_PD_TW |
| TC-KHO-200 | Boundary cau_hoi 5000 + 5001 ký tự | A4 edge | Edge | CB_NV_TW |
| TC-KHO-201 | Upload anh_dai_dien 5MB exact + 5.1MB | SRS line 110 | Edge | CB_NV_TW |
| TC-KHO-202 | Upload file_dinh_kem 20MB exact + 20.1MB | SRS line 112 | Edge | CB_NV_TW |
| TC-KHO-203 | Upload sai extension (.exe / .zip) → reject | SRS line 112 whitelist | Edge | CB_NV_TW |
| TC-KHO-204 | Concurrent edit 2 tab → 409 optimistic lock | A4 edge | Edge | CB_NV_TW |
| TC-KHO-205 | tu_khoa boundary 100 từ khóa | A4 edge | Edge | CB_NV_TW |
| TC-KHO-300 | Re-enable hieu_luc HET_HIEU_LUC → DA_DUYET | GAP-STATE-01 (A5) | Fill-gap A6 | CB_NV_TW |
| TC-KHO-301 | so_luot_xem counter increment | GAP-ATTR-01 (A5) | Fill-gap A6 | (verify CMS) |

---

## Test Cases

### TC-KHO-001 — Hiển thị danh sách Kho Q&A

**Trace:** FR-X.2-01 / AC1 line 162
**Precondition:**
- Login `cb_nv_tw_01` / Secret@123 (Tier 1 + OTP=666666).
- Kho Q&A có ≥5 record DA_DUYET trong scope TW.

**Steps:**
1. Click sidebar "Tư vấn" → "Kho câu hỏi" hoặc navigate `/tu-van/kho-cau-hoi`.
2. Quan sát breadcrumb + table.

**Expected:**
- Breadcrumb "Trang chủ > Tư vấn > Kho câu hỏi" hiển thị.
- Header `[+ Thêm câu hỏi] [Nhập Excel] [Làm mới]` hiển thị.
- Table cột: Mã / Câu hỏi / Câu trả lời / Lĩnh vực / Từ khóa / Nguồn / Trạng thái / Công khai / Hiệu lực / Điểm TB / Ngày tạo / Hành động.
- Phân trang 20 mục/trang.
- Network request `GET /api/v1/kho-cau-hoi?page=1&size=20` 200 OK.

---

### TC-KHO-002 — Tab phân loại 3 (Tất cả / Đã duyệt / Chờ duyệt)

**Precondition:** Kho có ≥1 record DA_DUYET hieu_luc=1 + ≥1 record CHO_DUYET.

**Steps:**
1. Click tab "Tất cả" → ghi badge số đếm.
2. Click tab "Đã duyệt" → filter `trang_thai=DA_DUYET AND hieu_luc=1`.
3. Click tab "Chờ duyệt" → filter `trang_thai=CHO_DUYET`.

**Expected:**
- Mỗi tab hiển thị badge số đếm chính xác.
- Tab "Đã duyệt" KHÔNG bao gồm record CONG_KHAI (CONG_KHAI có badge riêng cột 8).
- Tab "Chờ duyệt" hiển thị nút [Duyệt] [Từ chối] inline trên dòng (CB PD).

---

### TC-KHO-003 — Thêm Q&A thủ công happy path → CHO_DUYET

**Trace:** FR-X.2-01 / AC2 + Processing 3
**Precondition:** Login `cb_nv_tw_01`. Lĩnh vực PL `LV_THUE` đang KICH_HOAT.

**Steps:**
1. Click [+ Thêm câu hỏi] → modal hiển thị.
2. Nhập:
   - cau_hoi: "Thuế GTGT đối với DN nhỏ và vừa quy định ra sao?"
   - cau_tra_loi (Rich Text): "Theo Luật thuế GTGT 2008..."
   - linh_vuc: chọn "Thuế"
   - tu_khoa: "thuế, GTGT, DN nhỏ"
3. Click [Gửi duyệt].

**Expected:**
- Toast "Đã gửi duyệt câu hỏi."
- Modal đóng, danh sách refresh.
- Record mới hiển thị tab "Chờ duyệt" với:
  - mã: `QA-YYYYMMDD-NNN` (BR-DATA-04)
  - nguon: THU_CONG (nhãn vàng)
  - trang_thai: CHO_DUYET
- Network: `POST /api/v1/kho-cau-hoi` body `{nguon:"THU_CONG"}` → 201.

---

### TC-KHO-004 — Thêm Q&A với ảnh đại diện + mô tả công khai + file đính kèm

**Precondition:** Login `cb_nv_tw_01`. Có file ảnh test 200KB jpg + file PDF test 1MB.

**Steps:**
1. Mở modal Thêm Q&A.
2. Upload anh_dai_dien jpg 200KB.
3. Nhập mo_ta_cong_khai: "Hướng dẫn thuế GTGT cho DN."
4. Upload file_dinh_kem_cong_khai: 1 file PDF 1MB.
5. Điền các field bắt buộc + [Gửi duyệt].

**Expected:**
- Upload preview hiển thị thumb ảnh + tên file PDF.
- Sau Gửi duyệt: record mới có anh_dai_dien link + file_dinh_kem_cong_khai array 1 phần tử.
- Network: `POST /api/v1/kho-cau-hoi` multipart/form-data → 201.

---

### TC-KHO-005 — Lưu nháp (NHAP) chưa Gửi duyệt

**Precondition:** Login `cb_nv_tw_01`.

**Steps:**
1. Mở modal Thêm Q&A. Nhập cau_hoi + cau_tra_loi + linh_vuc.
2. Click [Lưu nháp].

**Expected:**
- Toast "Đã lưu nháp."
- Record mới `trang_thai=NHAP` (KHÔNG hiển thị tab "Chờ duyệt").
- Tab "Tất cả": record có badge "Nháp".

---

### TC-KHO-006 — Sửa Q&A NHAP của mình

**Precondition:** Login `cb_nv_tw_01`. Có record NHAP do user này tạo.

**Steps:**
1. Tab "Tất cả" → tìm record NHAP → click [Sửa].
2. Sửa cau_hoi → "Cập nhật câu hỏi."
3. Click [Lưu nháp].

**Expected:**
- Modal pre-fill đúng dữ liệu hiện tại.
- Sau lưu: cau_hoi mới hiển thị + AUDIT_LOG.action='UPDATE'.

---

### TC-KHO-007 — Xóa Q&A NHAP (soft delete BR-DATA-01)

**Trace:** BR-DATA-01
**Precondition:** Login `cb_nv_tw_01`. Có record NHAP.

**Steps:**
1. Click [Xóa] trên dòng NHAP → modal xác nhận.
2. Click [Xác nhận].

**Expected:**
- Toast "Đã xóa."
- Record không còn trong list.
- DB: `is_deleted=1` (soft delete, không DELETE physical).
- Network: `DELETE /api/v1/kho-cau-hoi/{id}` → 200.

---

### TC-KHO-008 — Toggle hieu_luc DA_DUYET → HET_HIEU_LUC

**Trace:** FR-X.2-01 / Processing 6
**Precondition:** Có record DA_DUYET hieu_luc=1.

**Steps:**
1. Click toggle Hiệu lực trên dòng DA_DUYET → tắt.
2. Quan sát badge.

**Expected (Codex P2 fix — chọn 1 outcome):**
- Toggle chuyển trạng thái OFF.
- Cột "Hiệu lực": OFF.
- Cột "Trạng thái": **HET_HIEU_LUC** (theo SRS line 108 enum trang_thai có HET_HIEU_LUC; toggle OFF → trang_thai chuyển HET_HIEU_LUC + hieu_luc=0).
- Q&A KHÔNG xuất hiện trên Cổng PLQG khi DN search (verify file 03).
- Network: `PATCH /api/v1/kho-cau-hoi/{id}/hieu-luc` body `{hieu_luc:false}` → 200.

---

### TC-KHO-009 — Auto-tạo từ HOI_DAP DA_DUYET (nguồn TU_DONG)

**Trace:** FR-X.2-01 / Processing 2 + BR-FLOW-10
**Precondition:** Có HOI_DAP đang ở CHO_PHE_DUYET trong scope TW.

**Steps:**
1. Login `cb_pd_tw_01`. Phê duyệt HOI_DAP đó (trans CHO_PHE_DUYET → DA_DUYET — FR-II-08).
2. Login `cb_nv_tw_01`. Truy cập "Kho câu hỏi" tab "Tất cả".

**Expected:**
- Record mới trong Kho có:
  - nguon = TU_DONG
  - hoi_dap_goc_id = HOI_DAP.id
  - trang_thai = DA_DUYET (NOT CHO_DUYET — TU_DONG bypass duyệt)
  - cau_hoi = HOI_DAP.tieu_de hoặc noi_dung tóm tắt
- AUDIT_LOG: `INSERT KHO_CAU_HOI nguon=TU_DONG`.

---

### TC-KHO-010 — Phê duyệt đơn lẻ tab "Chờ duyệt" → DA_DUYET + hieu_luc=1

**Trace:** FR-X.2-01 / SCR row 10
**Precondition:** Login `cb_pd_tw_01`. Có ≥1 record CHO_DUYET (nguồn THU_CONG hoặc IMPORT) trong scope TW.

**Steps:**
1. Tab "Chờ duyệt" → click [Duyệt] trên dòng.
2. Modal xác nhận → click [Duyệt].

**Expected:**
- Toast "Đã duyệt câu hỏi."
- Record chuyển sang tab "Đã duyệt" với:
  - trang_thai = DA_DUYET
  - hieu_luc = 1
- TB CB NV (in-app/email) gửi cho người tạo (kiểm tra thông báo).
- Network: `POST /api/v1/kho-cau-hoi/{id}/approve` → 200.

---

### TC-KHO-011 — Từ chối đơn lẻ với lý do bắt buộc

**Trace:** FR-X.2-01 / SCR row 10
**Precondition:** Login `cb_pd_tw_01`. Có record CHO_DUYET.

**Steps:**
1. Tab "Chờ duyệt" → click [Từ chối].
2. Modal hiện input "Lý do" (bắt buộc).
3. Để trống → click [Xác nhận]. **Expected:** ERROR "Lý do là bắt buộc".
4. Nhập lý do "Câu hỏi trùng lặp với QA-20260101-001." → [Xác nhận].

**Expected:**
- Record trang_thai = NHAP.
- TB CB NV gửi cho người tạo kèm lý do từ chối.

---

### TC-KHO-012 — Phê duyệt hàng loạt (modal xác nhận, không từ chối hàng loạt)

**Trace:** FR-X.2-01 / SCR row 11
**Precondition:** Có ≥3 record CHO_DUYET.

**Steps:**
1. Tab "Chờ duyệt" → tick checkbox 3 record.
2. Click [Duyệt hàng loạt].
3. Modal xác nhận → [Xác nhận].

**Expected:**
- 3 record cùng chuyển DA_DUYET + hieu_luc=1.
- Toast "Đã duyệt 3 câu hỏi."
- KHÔNG có nút [Từ chối hàng loạt] (theo SRS row 11).

---

### TC-KHO-013 — Import Excel happy path

**Trace:** FR-X.2-01 / Processing 4
**Precondition:** Login `cb_nv_tw_01`. Có file mau-import-kho.xlsx 5 dòng hợp lệ.

**Steps:**
1. Click [Nhập Excel] → modal C15.
2. Upload file mau-import-kho.xlsx.
3. Hệ thống validate + preview 10 dòng đầu.
4. Click [Xác nhận import].

**Expected:**
- Preview hiển thị 5 dòng (vì file 5 dòng).
- Sau import: kết quả "5 thành công, 0 lỗi".
- 5 record mới với nguon=IMPORT, trang_thai=CHO_DUYET.
- Network: `POST /api/v1/kho-cau-hoi/import` multipart → 200.

---

### TC-KHO-014 — Tìm kiếm full-text (UC157)

**Trace:** FR-X.2-01 / Processing 5 + BR-DATA-08
**Precondition:** Kho có Q&A: "Thuế GTGT...", "Thuế TNDN...", "Hợp đồng lao động...".

**Steps:**
1. Filter-bar nhập "thuế" vào ô Tìm kiếm.
2. Quan sát kết quả.

**Expected:**
- 2 Q&A liên quan thuế match (loại trừ "Hợp đồng lao động").
- Sắp xếp theo relevance DESC.
- Network: `GET /api/v1/kho-cau-hoi?q=thu%E1%BA%BF` → 200, body chứa `total: 2`.

---

### TC-KHO-015 — Lọc theo lĩnh vực + nguồn + trạng thái

**Steps:**
1. Filter linh_vuc = "Thuế", nguon = "TU_DONG", trang_thai = "DA_DUYET".
2. Quan sát.

**Expected:**
- Chỉ Q&A khớp 3 điều kiện AND hiển thị.
- Network query string chứa cả 3 filter.

---

### TC-KHO-016 — Phân trang 20 mục/trang

**Trace:** BR-DATA-07
**Precondition:** Kho có ≥41 record DA_DUYET.

**Steps:**
1. Mở danh sách → trang 1 hiển thị 20 record.
2. Click trang 2 → 20 record tiếp theo.
3. Click trang 3 → ≥1 record.

**Expected:** mỗi trang đúng 20 (trừ trang cuối). Network query `?page=2&size=20`.

---

### TC-KHO-017 — Mã Q&A auto-gen QA-YYYYMMDD-SEQ

**Trace:** BR-DATA-04
**Precondition:** Tạo 3 record cùng ngày.

**Steps:**
1. Tạo Q&A 1 → ghi mã.
2. Tạo Q&A 2 → ghi mã.
3. Tạo Q&A 3 → ghi mã.

**Expected:** Mã có format `QA-YYYYMMDD-NNN`. SEQ tăng dần (vd 001, 002, 003) trong cùng ngày, KHÔNG trùng.

---

### TC-KHO-018 — AUDIT_LOG ghi nhận CRUD + duyệt

**Trace:** BR-DATA-05
**Steps:**
1. Tạo Q&A mới → quan sát network `POST /api/v1/audit-log` hoặc verify trang Nhật ký HT (FR-10 W1.1) có record action=CREATE entity=KHO_CAU_HOI.
2. Sửa → action=UPDATE.
3. Xóa → action=DELETE.
4. Phê duyệt → action=APPROVE.

**Expected:** Mỗi action có entry AUDIT_LOG với user_id + timestamp + entity_id.

---

### TC-KHO-100 — E1 câu hỏi trống → ERR-KHO-01

**Trace:** FR-X.2-01 / E1
**Steps:**
1. Modal Thêm Q&A → để cau_hoi rỗng.
2. Điền các field khác → [Gửi duyệt].

**Expected:** Inline error "Câu hỏi là bắt buộc" hoặc toast ERR-KHO-01. Form không submit.

---

### TC-KHO-101 — E2 câu trả lời trống → ERR-KHO-02

**Steps:**
1. Modal Thêm Q&A → để cau_tra_loi (Rich Text) rỗng.
2. [Gửi duyệt].

**Expected:** Inline "Câu trả lời là bắt buộc" / ERR-KHO-02.

---

### TC-KHO-102 — E3 lĩnh vực không hợp lệ → ERR-KHO-03

**Steps:**
1. Tạo Q&A → ban đầu chọn linh_vuc đúng → submit qua DevTools change linh_vuc_id thành 99999 (không tồn tại) hoặc lĩnh vực VO_HIEU_HOA.
2. Gửi.

**Expected:** Server reject 400 / ERR-KHO-03 "Lĩnh vực PL không hợp lệ".

---

### TC-KHO-103 — E4 file Excel sai format → ERR-KHO-04

**Steps:**
1. Click [Nhập Excel] → upload file .csv (không phải .xlsx).
2. Submit.

**Expected:** ERR-KHO-04 "File không đúng định dạng. Tải mẫu Excel". Link download mẫu hiển thị.

---

### TC-KHO-104 — Sửa Q&A của đơn vị khác → 403/404 (BR-AUTH-08)

**Trace:** BR-AUTH-08
**Precondition:**
- `cb_nv_dp_01` (Sở TP AG) tạo Q&A X.
- Login `cb_nv_dp_02` (Sở TP BG).

**Steps:**
1. Truy cập trực tiếp URL `/tu-van/kho-cau-hoi/{X.id}/edit` hoặc API `PATCH /api/v1/kho-cau-hoi/{X.id}`.

**Expected:** 404 (IDOR block) hoặc 403 ERR-AUTH-08. UI list không hiển thị Q&A X cho dp_02.

---

### TC-KHO-105 — Phê duyệt cross-cấp (PD_TW phê duyệt Q&A cấp ĐP) → block (BR-AUTH-05)

**Trace:** BR-AUTH-05
**Precondition:** Q&A CHO_DUYET tạo bởi cb_nv_dp_01 (cấp ĐP).

**Steps:**
1. Login `cb_pd_tw_01` (cấp TW).
2. Tab "Chờ duyệt" → quan sát Q&A cấp ĐP.

**Expected:**
- Q&A cấp ĐP KHÔNG hiển thị cho cb_pd_tw_01 (BR-AUTH-05 — phê duyệt cùng cấp).
- Hoặc hiển thị nhưng nút [Duyệt] disabled / API reject ERR-PD-01 (theo pattern FR-II-08 line 86).

---

---

## Edge bổ sung A4

### TC-KHO-200 — Boundary cau_hoi 5000 ký tự + 5001 ký tự

**Trace:** A4 edge boundary
**Steps:**
1. Tạo Q&A với cau_hoi đúng 5000 ký tự → Gửi duyệt.
2. Sửa cau_hoi thành 5001 ký tự → Gửi.

**Expected:**
- 5000 ký tự: lưu thành công.
- 5001 ký tự: backend reject với inline error "Câu hỏi tối đa 5000 ký tự" (sibling FR-II ERR-HD-02 line 102).
- **SPEC-CLARIFY:** SRS không khai báo cap rõ ràng cho cau_hoi/cau_tra_loi — cần BA chốt 5000 hay khác.

---

### TC-KHO-201 — Upload anh_dai_dien 5MB exact + 5.1MB

**Trace:** SRS line 110 max 5MB
**Steps:**
1. Upload ảnh JPG đúng 5,242,880 bytes (5MB exact).
2. Upload ảnh 5,300,000 bytes (~5.05MB).

**Expected:**
- 5MB exact: nhận (inclusive max).
- > 5MB: reject "Ảnh đại diện vượt quá 5MB".

---

### TC-KHO-202 — Upload file_dinh_kem_cong_khai 20MB exact + 20.1MB

**Trace:** SRS line 112 max 20MB/file
**Steps:** Upload file PDF 20MB → nhận. Upload 20.1MB → reject.

---

### TC-KHO-203 — Upload file_dinh_kem_cong_khai sai extension (.exe / .zip)

**Trace:** SRS line 112 whitelist PDF/DOC/DOCX/XLS/XLSX
**Steps:**
1. Upload file `malware.exe`.
2. Upload `archive.zip`.

**Expected:** Reject cả 2 với error "Định dạng file không hỗ trợ. Chỉ chấp nhận PDF/DOC/DOCX/XLS/XLSX".

---

### TC-KHO-204 — Concurrent edit Q&A 2 tab

**Steps:**
1. Tab A: mở Q&A QA-100 edit, chưa save.
2. Tab B: mở cùng Q&A QA-100 edit + sửa cau_hoi + Save → 200.
3. Tab A: tiếp tục sửa + Save.

**Expected:**
- Tab A nhận HTTP 409 Conflict (optimistic lock — version mismatch).
- Toast "Bản ghi đã bị thay đổi. Tải lại để xem dữ liệu mới."
- (Pattern giống sibling FR-II ERR-TH-CONFLICT.)

---

### TC-KHO-205 — tu_khoa boundary 100 từ khóa phân cách dấu phẩy

**Steps:**
1. Nhập tu_khoa = 100 từ khóa "tag1, tag2, ..., tag100".
2. Gửi.

**Expected:** Hệ thống xử lý OK, lưu tất cả 100 tag. Hoặc cap ở mức 50 (tùy BA).
- **SPEC-CLARIFY:** SRS line 106 không cap số tag — cần BA chốt.

---

---

## A6 fill-gap (từ A5 traceability)

### TC-KHO-300 — Re-enable hieu_luc HET_HIEU_LUC → DA_DUYET

**Trace:** GAP-STATE-01 (A5)
**Precondition:** QA-100 đã HET_HIEU_LUC (hieu_luc=0, từ TC-KHO-008).

**Steps:**
1. Login `cb_nv_tw_01`. Mở SCR-X2-01 → tìm QA-100.
2. Toggle Hiệu lực ON.

**Expected:**
- Toast "Đã bật lại hiệu lực."
- hieu_luc = 1, trang_thai có thể chuyển DA_DUYET (nếu trước đó đã CK thì giữ CONG_KHAI hoặc DA_DUYET tùy spec — cần BA chốt).
- **SPEC-CLARIFY-TVN-10:** Toggle hieu_luc ON khi state=HET_HIEU_LUC chuyển về state nào? DA_DUYET hay CONG_KHAI?
- AUDIT_LOG: action=ENABLE_HIEU_LUC.
- Q&A xuất hiện lại trên Cổng PLQG (nếu trang_thai=CONG_KHAI).

---

### TC-KHO-301 — so_luot_xem counter increment khi DN xem trên Cổng

**Trace:** GAP-ATTR-01 (A5) — so_luot_xem counter (entity attribute)
**Precondition:** QA-100 trang_thai=CONG_KHAI, so_luot_xem=10.

**Steps:**
1. Mock API inbound từ Cổng PLQG: `POST /api/v1/inbound/kho-cau-hoi/{QA-100}/view-event` (DN xem chi tiết).
2. Login `cb_nv_tw_01`. Mở SCR-X2-01 → tìm QA-100.
3. Quan sát cột so_luot_xem (nếu có hiển thị) hoặc query DB.

**Expected:**
- so_luot_xem = 11.
- **SPEC-CLARIFY-TVN-11:** SRS không khai báo endpoint API inbound view-event — có thể là tự tăng khi Cổng PLQG render hoặc cần endpoint riêng. Cần BA chốt.

---

**Tổng số TC:** 33 TC (18 Happy + 6 Negative + 1 cross-cấp + 6 Edge A4 + 2 fill-gap A6)

*Generated 2026-05-10 — Phase A step A3 + A4 edge merge + A6 fill-gap*
