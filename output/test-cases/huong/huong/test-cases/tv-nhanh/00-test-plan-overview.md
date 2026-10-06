# Kế Hoạch Kiểm Thử — FR-13 Tư vấn Nhanh (FR-X.2-01 → FR-X.2-06)

> **Phiên bản:** 1.0
> **Ngày tạo:** 2026-05-10
> **Owner:** QA Automation Lead
> **Module:** FR-13 / Nhóm X.2 — Tư vấn Nhanh
> **UC range:** UC154 → UC158 (5 UC CSV) + 3 luồng nội bộ ngoài CSV (FR-X.2-02 / FR-X.2-03 / FR-X.2-04)
> **SRS reference:** [`input/srs-v3/srs-fr-13-tv-nhanh-v3.1.md`](../../../input/srs-v3/srs-fr-13-tv-nhanh-v3.1.md) (v3.5, 935 dòng) + [`srs-v3.md`](../../../input/srs-v3/srs-v3.md) Phụ lục B/C
> **Plan parent:** [`Ver3.1/tasks/detailed-tc/plan.md`](../../../tasks/detailed-tc/plan.md) §W4.3
> **Source mode:** SRS local + NotebookLM secondary `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` (verify nghiệp vụ chi tiết SM-TVNHANH + API outbound BR-FLOW-05 + Idempotency-Key API inbound đánh giá)

---

## 1. Phạm vi kiểm thử

### 1.1 Chức năng được kiểm thử

- **6 FR** (FR-X.2-01..06) trên 2 màn hình chính (SCR-X2-04 + SCR-X2-02 đã DEPRECATED v2.1, gộp inline):
  - **SCR-X2-01** — Quản lý Kho câu hỏi (MH-13.1 + MH-13.2): CRUD Kho Q&A + 3 nguồn + Phê duyệt inline + Công khai/Hủy công khai
  - **SCR-X2-03** — Quản lý Tư vấn Nhanh (MH-13.3 + MH-13.4): Phiên TVN + TOP 5 gợi ý + đánh giá inline
- **Entity owned:** `KHO_CAU_HOI`, `TU_VAN_NHANH`, `DANH_GIA_TV`
- **Entity referenced:** `HOI_DAP` (nguồn TU_DONG), `TAI_KHOAN`, `DON_VI`, `DANH_MUC` (Lĩnh vực PL)
- **State Machine SM-TVNHANH:** 6 trạng thái (MOI/DANG_TIM_KIEM/DA_GOI_Y/CB_TRA_LOI/HOAN_THANH/HET_HAN) + 8 transitions (auto 30 ngày HET_HAN, auto chuyển từ DANG_TIM_KIEM khi kho rỗng)
- **State KHO_CAU_HOI:** 5 trạng thái (NHAP/CHO_DUYET/DA_DUYET/CONG_KHAI/HET_HIEU_LUC) — cong_khai (boolean UI switch) tách biệt với trang_thai='CONG_KHAI' (kết quả API outbound)
- **API inbound:** FR-X.2-05 (`/api/v1/inbound/danh-gia-tv-nhanh`) — Idempotency-Key 24h cache chống ghi trùng
- **API outbound:** FR-X.2-06 (gọi Cổng PLQG đẩy/gỡ Q&A công khai — BR-FLOW-05)
- **3 luồng ngoài CSV CMS** (DN chuyên trang Cổng PLQG): FR-X.2-02 (CMS xử lý phiên TVN), FR-X.2-03 (DN gửi câu hỏi), FR-X.2-04 (DN tìm kiếm phản hồi)

### 1.2 Danh sách FR / UC / TC file

| # | Mã FR | UC | Tên chức năng | SCR | Loại | File Test Case |
|---|--------|-----|--------------|------|------|----------------|
| 1 | FR-X.2-01 | UC154/155/157 | Quản lý Kho Q&A (CRUD + 3 nguồn + Phê duyệt inline + Tìm kiếm CB NV) | SCR-X2-01 | B | `01-TC-FR-X2-01-quan-ly-kho-cau-hoi.md` |
| 2 | FR-X.2-02 | (nội bộ ngoài CSV) | Quản lý phiên Tư vấn Nhanh (CMS keyword search + TOP 5 + CB NV trả lời) | SCR-X2-03 | B | `02-TC-FR-X2-02-quan-ly-phien-tu-van.md` |
| 3 | FR-X.2-03 + FR-X.2-04 | (chuyên trang DN) | DN gửi câu hỏi + DN tìm kiếm phản hồi (verify side-effect UI CMS sau API inbound) | (no CMS UI) | M | `03-TC-FR-X2-03-04-DN-chuyen-trang-side-effect.md` |
| 4 | FR-X.2-05 | UC158 | Tiếp nhận đánh giá CL TVN (API inbound — verify side-effect UI accordion DG, điểm TB, Idempotency-Key 24h) | accordion SCR-X2-03 | M | `04-TC-FR-X2-05-API-inbound-danh-gia.md` |
| 5 | FR-X.2-06 | UC156 | Công khai / Hủy công khai Kho (CB NV → API outbound Cổng PLQG + BR-PUBLIC-01/02/03) | SCR-X2-01 | B | `05-TC-FR-X2-06-cong-khai-kho.md` |
| 6 | (cross) | — | Permission matrix cross-FR-X.2 (BR-AUTH-01/05/08) | cross-cutting | — | `06-TC-permission-matrix.md` |

**Cấu trúc file output (sau A1-A7):**

```
output/test-cases/tv-nhanh/
├── 00-test-plan-overview.md                                ← File này
├── 01-TC-FR-X2-01-quan-ly-kho-cau-hoi.md                   ← UC154/155/157 CRUD Kho + 3 nguồn + Phê duyệt + Tìm kiếm
├── 02-TC-FR-X2-02-quan-ly-phien-tu-van.md                  ← FR-X.2-02 phiên TVN + TOP 5 + SM-TVNHANH + auto HET_HAN
├── 03-TC-FR-X2-03-04-DN-chuyen-trang-side-effect.md        ← FR-X.2-03/04 verify side-effect (API inbound DN gửi câu hỏi + DN search)
├── 04-TC-FR-X2-05-API-inbound-danh-gia.md                  ← UC158 API inbound đánh giá + Idempotency-Key 24h
├── 05-TC-FR-X2-06-cong-khai-kho.md                         ← UC156 Công khai/Hủy CK + BR-PUBLIC + API outbound Cổng PLQG
├── 06-TC-permission-matrix.md                              ← Cross BR-AUTH (Kho + Phiên TVN)
├── 07-REVIEW-edge-case-hunter.md                           ← A4 audit log (TC mới đã merge inline)
├── 08-traceability-matrix.md                               ← A5 BR/AC ↔ TC matrix
├── 09-REVIEW-test-quality.md                               ← A6 audit log
└── 10-a7-filter-log.md                                     ← A7 audit log (LOẠI/SỬA/GIỮ)
```

### 1.3 Tài khoản test (`input/users.csv`)

| Role | Cấp | Username | Dùng cho TC loại |
|------|-----|----------|-------------------|
| QTHT | — | qtht_01 | Read-only verify (Permission Matrix) |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD Kho scope TW + xử lý phiên TVN scope TW + Công khai/Hủy CK |
| CB_NV_BN | BN | cb_nv_bn_01 (BKH), cb_nv_bn_02 (BTC) | CRUD scope BN + cross-unit isolation BR-AUTH-08 |
| CB_NV_DP | ĐP | cb_nv_dp_01 (AG), cb_nv_dp_02 (BG) | CRUD scope ĐP + cross-tenant test |
| CB_PD_TW | TW | cb_pd_tw_01 | Phê duyệt inline Kho cùng cấp TW (UC155 — BR-AUTH-05) |
| CB_PD_BN | BN | cb_pd_bn_01 | Phê duyệt cùng cấp BN; cross-cấp test BR-AUTH-05 |
| CB_PD_DP | ĐP | cb_pd_dp_01 | Phê duyệt cùng cấp ĐP |
| TVV / CG / NHT | — | tvv_01, cg_01, nht_01 | Negative — verify 403 (FR-13 không thuộc scope tác nhân ngoài) |
| DN | — | dn_01 | Negative — verify 403 (DN truy cập qua chuyên trang Cổng PLQG, không qua CMS) |

> **Source TK:** `c:/HoaAG/LuatDN5/Ver3.1/input/users.csv`. Password Secret@123 toàn bộ.

---

## 2. Quy tắc nghiệp vụ trích xuất từ SRS

### 2.1 Business Rules (BR formal §6 + working labels)

> **Footnote convention:**
> - **BR formal §6 srs-fr-13:** BR khai báo trong file SRS FR-13 §6 (lines 836-931). 8 BR áp dụng (3 BR-PUBLIC + BR-FLOW-05 + BR-FLOW-10 + BR-AUTH-01 + BR-DATA-05/08).
> - **Working labels (master srs-v3.md inline):** BR codes ref nhưng source ở Phụ lục B file chính.

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực bắt buộc — Tier 1 (CB nội bộ U/P + TOTP 2FA) / Tier 2 (DN/TVV/CG/NHT SSO VNeID OIDC) | srs-fr-13 §6 line 853-862 | ✅ | Precondition login mọi UC |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB PD cấp = đơn vị tạo) | srs-v3.md Phụ lục B | ✅ | TC phê duyệt Kho (file 01) + công khai (file 05) |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | srs-v3.md Phụ lục B | ✅ | TC scope đơn vị mọi list/detail (file 01, 02, 06) |
| BR-DATA-01 | Soft delete (is_deleted=1) | srs-v3.md Phụ lục B | ✅ | TC DELETE Kho (file 01) |
| BR-DATA-04 | Auto-gen mã `QA-YYYYMMDD-SEQ` | srs-fr-13 line 102 | ✅ | TC tạo Kho mới (file 01) |
| BR-DATA-05 | Audit trail INSERT-only | srs-fr-13 §6 line 863-871 | ✅ | TC CUD + state transition mọi file |
| BR-DATA-07 | Pagination default 20 | srs-fr-13 line 537 (SCR row 13) | ✅ | TC pagination (file 01, 02) |
| BR-DATA-08 | Full-text search (tsvector trên cau_hoi + cau_tra_loi + tu_khoa) | srs-fr-13 §6 line 873-881 | ✅ (core) | TC search Kho (file 01) + keyword TOP 5 (file 02) + DN search side-effect (file 03) |
| BR-FLOW-05 | Gọi API ra Cổng PLQG (đẩy/gỡ Q&A công khai). API thất bại → giữ trạng thái cũ | srs-fr-13 §6 line 893-901 | ✅ (core) | TC công khai/hủy CK (file 05) |
| BR-FLOW-10 | Kho TVN — 3 nguồn bổ sung (TU_DONG / THU_CONG / IMPORT) | srs-fr-13 §6 line 883-891 | ✅ | TC nguồn (file 01) — auto từ HOI_DAP DA_DUYET + manual + import Excel |
| BR-PUBLIC-01 | Điều kiện công khai — chỉ DA_DUYET mới được CONG_KHAI | srs-fr-13 §6 line 903-911 | ✅ | TC công khai negative state (file 05) |
| BR-PUBLIC-02 | Hủy công khai → clear `thoi_gian_dang_tai` + `cong_khai=0` + trang_thai → DA_DUYET | srs-fr-13 §6 line 913-921 | ✅ | TC hủy CK (file 05) |
| BR-PUBLIC-03 | thoi_gian_dang_tai auto fill khi cong_khai chuyển 0→1 + API thành công, không sửa tay | srs-fr-13 §6 line 923-931 | ✅ | TC công khai (file 05) — verify dd/mm/yyyy hh:mm format |

### 2.2 Error Codes

**FR-X.2-01 (Kho Q&A CRUD):**
- ERR-KHO-01 (cau_hoi trống)
- ERR-KHO-02 (cau_tra_loi trống)
- ERR-KHO-03 (linh_vuc invalid)
- ERR-KHO-04 (file Excel sai format)

**FR-X.2-02 (Phiên TVN):**
- ERR-TVN-01 (kho rỗng — WARNING)
- ERR-TVN-02 (noi_dung_tra_loi trống)

**FR-X.2-03 (DN gửi câu hỏi):**
- ERR-TVN-DN-01 (cau_hoi trống)

**FR-X.2-04 (DN search):**
- ERR-TVN-TK-01 (tu_khoa < 2 ký tự)
- INF-TVN-TK-01 (no results)

**FR-X.2-05 (API inbound đánh giá):**
- ERR-DG-TVN-01 (điểm ngoài 1-5)
- ERR-DG-TVN-02 (phiên TVN không tồn tại — HTTP 404)
- HTTP 400 Bad Request (sai dữ liệu)
- HTTP 409 Conflict (trùng Idempotency-Key — không tạo bản ghi mới, trả lại kết quả cũ)

**FR-X.2-06 (Công khai/Hủy CK):**
- ERR-TVN-CK-01 (API Cổng PLQG fail công khai)
- ERR-TVN-CK-02 (API Cổng PLQG fail hủy CK)
- ERR-TVN-CK-03 (state không hợp lệ — vd CHO_DUYET cố công khai)

### 2.3 Permission Matrix

| Action / Role | QTHT | CB_NV_{TW/BN/DP} | CB_PD_{TW/BN/DP} | TVV/CG/NHT | DN |
|---------------|------|-------------------|-------------------|------------|----|
| Xem Kho Q&A (scope đơn vị) | 👁️ R toàn HT | ✅ scope `don_vi_id` | ✅ cùng cấp | ❌ | ❌ |
| CREATE Kho thủ công (UC154 nguồn THU_CONG) | ❌ | ✅ cùng đơn vị → CHO_DUYET | ❌ | ❌ | ❌ |
| Import Excel Kho (UC154 nguồn IMPORT) | ❌ | ✅ cùng đơn vị → CHO_DUYET | ❌ | ❌ | ❌ |
| UPDATE / DELETE Kho | ❌ | ✅ cùng đơn vị (state hợp lệ) | ❌ | ❌ | ❌ |
| Phê duyệt / Từ chối Kho (UC155) | ❌ | ❌ | ✅ cùng cấp (BR-AUTH-05) | ❌ | ❌ |
| Toggle hieu_luc (HET_HIEU_LUC) | ❌ | ✅ cùng đơn vị | ❌ | ❌ | ❌ |
| Công khai / Hủy CK (UC156, FR-X.2-06) | ❌ | ✅ cùng đơn vị (theo CSV UC156 actor CB NV TW/BN/ĐP) | ❌ | ❌ | ❌ |
| Tìm kiếm Kho (UC157) | 👁️ | ✅ scope filter | ✅ scope filter | ❌ | ❌ |
| Xem phiên TVN (FR-X.2-02) | 👁️ R toàn HT | ✅ scope đơn vị | 👁️ scope cùng cấp | ❌ | ❌ |
| Trả lời phiên TVN (CB_TRA_LOI) | ❌ | ✅ cùng đơn vị | ❌ | ❌ | ❌ |
| Đánh giá TVN (UC158 — API inbound) | — | — | — | — | ✅ qua Cổng PLQG (không CMS) |

> **Cross-tenant test pattern:** cb_nv_dp_01 (Sở TP AG) tạo Kho X → cb_nv_dp_02 (Sở TP BG) attempt access → 404 IDOR block (BR-AUTH-08).
> **Cross-cấp test pattern:** Kho cấp ĐP → cb_pd_tw_01 phê duyệt → block (BR-AUTH-05).

### 2.4 State Machine SM-TVNHANH (TU_VAN_NHANH)

```
[*] → MOI → DANG_TIM_KIEM → DA_GOI_Y → CB_TRA_LOI → HOAN_THANH
                          ↘ CB_TRA_LOI (kho rỗng) ↗
       └→ HET_HAN (auto 30 ngày)              DA_GOI_Y → HOAN_THANH (DN hài lòng + đánh giá)
```

**8 transitions** (xem srs-fr-13 line 822-832):
1. `[*] → MOI` (DN gửi câu hỏi qua Cổng — FR-X.2-03)
2. `MOI → DANG_TIM_KIEM` (HT nhận câu hỏi — FR-X.2-02)
3. `DANG_TIM_KIEM → DA_GOI_Y` (Có kết quả search — FR-X.2-02)
4. `DANG_TIM_KIEM → CB_TRA_LOI` (Kho rỗng / không match — FR-X.2-02)
5. `DA_GOI_Y → CB_TRA_LOI` (DN chưa hài lòng, CB NV trả lời — FR-X.2-02)
6. `DA_GOI_Y → HOAN_THANH` (DN hài lòng + đánh giá — FR-X.2-05)
7. `CB_TRA_LOI → HOAN_THANH` (DN đánh giá — FR-X.2-05)
8. `MOI → HET_HAN` (Auto 30 ngày — batch job)

### 2.5 State KHO_CAU_HOI (5 trạng thái)

| Trạng thái | Mã | Mô tả | Action UI cho phép |
|-----------|-----|-------|---------------------|
| Nháp | NHAP | Lưu nháp chưa gửi duyệt | [Sửa] [Xóa] [Gửi duyệt] |
| Chờ duyệt | CHO_DUYET | Đã gửi, chờ CB PD duyệt | [Xem] (tab "Chờ duyệt": [Duyệt] [Từ chối]) |
| Đã duyệt | DA_DUYET | Đã duyệt, sẵn sàng công khai | [Sửa] [Xóa] [Công khai] [Đánh dấu hết hiệu lực] |
| Công khai | CONG_KHAI | Đã công khai trên Cổng PLQG | [Hủy công khai] [Đánh dấu hết hiệu lực] |
| Hết hiệu lực | HET_HIEU_LUC | hieu_luc=0, ẩn khỏi Cổng | [Bật lại hiệu lực] |

> **Tách biệt 2 cờ:**
> - `cong_khai` (boolean — switch UI nội bộ, CB NV bật/tắt nhanh)
> - `trang_thai='CONG_KHAI'` (kết quả thực sự sau khi gọi API ra Cổng PLQG thành công)
> - `cong_khai=1` nhưng `trang_thai≠CONG_KHAI` = đang chờ API; `cong_khai=0` nhưng `trang_thai=CONG_KHAI` = đang chờ hủy.

### 2.6 3 nguồn bổ sung Kho (BR-FLOW-10)

| Mã DB | Nhãn | Trạng thái khi tạo | Cần phê duyệt? |
|-------|------|---------------------|-----------------|
| `TU_DONG` | Tự động từ HOI_DAP DA_DUYET (Nhóm II) | DA_DUYET | ❌ (tự động duyệt vì HOI_DAP đã duyệt) |
| `THU_CONG` | CB NV nhập tay | CHO_DUYET | ✅ |
| `IMPORT` | Upload Excel (.xlsx) | CHO_DUYET | ✅ |

---

## 3. API Inbound — FR-X.2-05 (UC158)

### 3.1 Specification

| Thuộc tính | Giá trị |
|-----------|---------|
| **Phương thức** | POST |
| **Đường dẫn** | `/api/v1/inbound/danh-gia-tv-nhanh` |
| **Headers BB** | `Content-Type: application/json`, `X-API-Key: {key}` (xác thực Cổng PLQG), `Idempotency-Key: {uuid}` (chống ghi trùng) |
| **Body** | `tu_van_nhanh_id` (BB), `doanh_nghiep_id` (BB), `diem` (BB, 1-5), `nhan_xet` (KBB) |
| **Response** | 200 OK (`danh_gia_id` + `diem_tb_cap_nhat`) / 400 (sai dữ liệu) / 404 (`tu_van_nhanh_id` không tồn tại) / 409 Conflict (trùng Idempotency-Key, trả kết quả cũ) |

### 3.2 Idempotency 24h

- Lưu `Idempotency-Key` đã xử lý trong cache 24h.
- Cổng PLQG gửi lại cùng key → trả kết quả của lần xử lý đầu, **KHÔNG tạo bản ghi mới**.
- Đảm bảo nguyên tắc CSV UC158 transaction 2: "không ghi đè sai lệch".

### 3.3 Side-effect verify (TC file 04)

- DANH_GIA_TV record được tạo (1 lần, không trùng nếu retry cùng Idempotency-Key).
- KHO_CAU_HOI.diem_danh_gia_tb cập nhật (nếu đánh giá Q&A cụ thể).
- Accordion "Đánh giá CL" trong SCR-X2-03 hiển thị điểm + nhận xét + ngày DG.
- Tổng số đánh giá / Điểm TB / Phân bố sao update real-time.

---

## 4. API Outbound — FR-X.2-06 (Cổng PLQG)

### 4.1 Use case

| Hành động | Method | Endpoint Cổng PLQG (mock) | Payload | Side-effect |
|----------|--------|---------------------------|---------|-------------|
| Công khai | POST | `/api/v1/cong-plqg/kho-cau-hoi/publish` | cau_hoi + cau_tra_loi + anh_dai_dien + mo_ta_cong_khai + file_dinh_kem_cong_khai | API OK → SET trang_thai=CONG_KHAI + thoi_gian_dang_tai=NOW() |
| Hủy công khai | DELETE | `/api/v1/cong-plqg/kho-cau-hoi/{ma}` | — | API OK → SET trang_thai=DA_DUYET + thoi_gian_dang_tai=NULL |

### 4.2 Fail-safe (BR-FLOW-05)

- API fail → giữ nguyên trang_thai cũ + hiển thị ERR-TVN-CK-01/02 cho user thử lại.
- KHÔNG tự cập nhật trạng thái nội bộ trước khi xác nhận thành công từ Cổng.

---

## 5. Cấu Trúc File Test Case

### 5.1 Convention TC ID

- Prefix theo file: `TC-KHO-XXX` (file 01) · `TC-PHIEN-XXX` (file 02) · `TC-DN-XXX` (file 03) · `TC-DGTV-XXX` (file 04) · `TC-CK-XXX` (file 05) · `TC-PERM-XXX` (file 06).
- Range: 001-099 Happy · 100-199 Negative · 200-299 Edge · 300+ Codex review additions.
- TraceID format: `FR-X.2-XX / {section}` hoặc `FR-X.2-XX / E{N}` cho error codes.

### 5.2 Phân bổ TC final (sau A1-A7 + Codex review apply 2026-05-10)

> **Note:** Estimate ban đầu 60-70 TC. Final 100 TC active sau khi Codex review apply 4 P1 fix (TC-DN-100/101 restore + TC-DGTV-104 + TC-DGTV-301).

| File | Tên | TC base A3 | Edge A4 | Fill A6 | Filter A7 | Codex P1 | Final |
|------|-----|------------|---------|---------|-----------|----------|-------|
| 01 | quan-ly-kho-cau-hoi | 25 | +6 | +2 | 0 | 0 | 33 |
| 02 | quan-ly-phien-tu-van | 15 | +4 | 0 | 0 | 0 | 19 |
| 03 | DN-chuyen-trang-side-effect | 7 | +1 | +1 | 0 (P1-001/002 restore) | 0 | 9 |
| 04 | API-inbound-danh-gia | 11 | +3 | +1 | 0 | +2 (P1-003/004) | 17 |
| 05 | cong-khai-kho | 12 | +4 | 0 | 0 | 0 | 16 |
| 06 | permission-matrix | 6 | 0 | 0 | 0 | 0 | 6 |
| **Total** | | **76** | **+18** | **+4** | **0** | **+2** | **100** |

---

## 6. Đặc Thù Cần Lưu Ý Khi Viết TC

### 6.1 SCR-X2-01 đa tab + cong_khai 2 cờ

- 3 tab: Tất cả / Đã duyệt (DA_DUYET + hieu_luc=1) / Chờ duyệt (CHO_DUYET) — badge số đếm.
- Action button trên dòng đổi theo `trang_thai` × `cong_khai` × role:
  - `DA_DUYET` + `cong_khai=0` → [Công khai]
  - `CONG_KHAI` (sau API OK) → [Hủy công khai]
  - `cong_khai=1` nhưng `trang_thai≠CONG_KHAI` → spinner "Đang đẩy..." / disabled button
- BR-PUBLIC-03: thoi_gian_dang_tai format dd/mm/yyyy hh:mm — disabled input.

### 6.2 SCR-X2-03 layout 2 cột (mode trả lời)

- **Cột trái (40%):** Mã phiên + Trạng thái SM-TVNHANH + Thông tin DN + Câu hỏi DN (card) + Lịch sử trao đổi.
- **Cột phải (60%):** TOP 5 gợi ý từ KHO_CAU_HOI (relevance DESC) + Click [Chọn] auto-fill ô soạn (Rich Text C16) + [Gửi trả lời] → SM CB_TRA_LOI.
- Section đánh giá inline (gộp MH-13.4): chỉ hiển thị tab "Hoàn thành" hoặc chi tiết phiên.

### 6.3 Test data seeding pattern

- **Kho Q&A state coverage:** ≥1 record mỗi state (NHAP/CHO_DUYET/DA_DUYET/CONG_KHAI/HET_HIEU_LUC) × 3 cấp đơn vị.
- **3 nguồn bổ sung:** ≥1 record TU_DONG (link `hoi_dap_goc_id` to HOI_DAP DA_DUYET) + ≥1 THU_CONG + ≥1 IMPORT.
- **Phiên TVN state coverage:** ≥1 record mỗi state SM-TVNHANH (6 states).
- **Cross-tenant:** ≥2 record cùng cấp khác đơn vị (BR-AUTH-08).
- **TOP 5 search:** Seed kho ≥10 Q&A cùng lĩnh vực để verify ranking relevance giảm dần.
- **Đánh giá API inbound:** Seed ≥3 phiên HOAN_THANH (chưa đánh giá) để Cổng PLQG có target gửi DG.

### 6.4 Auto HET_HAN 30 ngày (batch job)

- Test gián tiếp: seed phiên MOI với `ngay_tao` = NOW() - 31 ngày → trigger batch → verify trang_thai = HET_HAN + TB CB NV.
- Cap: TC không yêu cầu chạy batch live, chỉ verify trên record đã seed sẵn.

### 6.5 TU_DONG nguồn auto từ HOI_DAP

- Khi HOI_DAP (Nhóm II) chuyển DA_DUYET → trigger tạo KHO_CAU_HOI mới với:
  - nguon='TU_DONG'
  - hoi_dap_goc_id = HOI_DAP.id
  - trang_thai='DA_DUYET' (không cần phê duyệt thêm)
- Test cross-FR-13 ↔ FR-02: trigger HOI_DAP DA_DUYET → verify KHO_CAU_HOI mới (file 01).

### 6.6 Idempotency-Key cache 24h (FR-X.2-05)

- Cổng PLQG gửi lần 1 với UUID-X → 200 OK + tạo DANH_GIA_TV.
- Cổng PLQG gửi lại lần 2 cùng UUID-X (mô phỏng đồng bộ thất bại) → 409 Conflict + KHÔNG tạo bản ghi mới + trả lại danh_gia_id cũ.
- Verify: COUNT(DANH_GIA_TV WHERE tu_van_nhanh_id = X) = 1 (không phải 2).

### 6.7 API outbound mock pattern (FR-X.2-06)

- Mock endpoint Cổng PLQG (qua test infra hoặc verify network request qua MCP `list_network_requests`).
- API OK (200) → SET trang_thai=CONG_KHAI, thoi_gian_dang_tai=NOW().
- API fail (4xx/5xx/timeout) → KEEP trang_thai cũ, ERR-TVN-CK-01/02.
- Verify: nếu API fail, `cong_khai` cờ UI có thể đã set 1 nhưng `trang_thai` không đổi → user thấy spinner + nút "Thử lại".

### 6.8 Full-text search (BR-DATA-08)

- tsvector index trên `cau_hoi + cau_tra_loi + tu_khoa`.
- Test: keyword "thuế" → match Q&A có "thuế" trong bất kỳ field nào, sắp theo relevance DESC.
- Edge: dấu tiếng Việt unaccent ("thue" match "thuế"), cụm từ chính xác (`"thuế GTGT"` quoted).

---

## 7. Out-of-Scope (cần xác nhận BA / chuyển module khác)

| Item | Lý do |
|------|-------|
| FR-X.2-03 (DN gửi câu hỏi trên chuyên trang) | UI ở chuyên trang Cổng PLQG — KHÔNG có UI CMS. Chỉ test side-effect API inbound (file 03). |
| FR-X.2-04 (DN tìm kiếm phản hồi trên chuyên trang) | UI ở chuyên trang Cổng PLQG — KHÔNG có UI CMS. Chỉ test side-effect API inbound (file 03). |
| API inbound chi tiết FR-X.2-05 (request/response) | Black-box — verify trạng thái local sau API call qua MCP network. Mock Cổng PLQG. |
| API outbound FR-X.2-06 (request payload Cổng PLQG) | Black-box — verify trạng thái local + network request qua MCP. |
| Auto batch job 30 ngày HET_HAN | Backend cron — không có UI riêng. Verify gián tiếp qua record đã seed deadline + trigger artificial. |
| Báo cáo điểm TB phân bố sao | Phục vụ FR-11 Báo cáo TK (W5.2) — chỉ verify số liệu accordion DG inline (file 04). |

---

*Generated 2026-05-10 — Phase A step A2 (00-test-plan-overview)*
