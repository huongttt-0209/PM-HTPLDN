# 00 — Test Plan Overview: FR-07 Quản lý Doanh nghiệp được Hỗ trợ pháp lý (Nhóm V.III) v3.1

> **SRS Ref**: FR-07 — `srs-fr-07-doanh-nghiep-v3.1.md` (613 dòng) + `srs-v3.5.md` §3.4.3.3 / §3.4.3.3a / §3.4.2 Permission Matrix / Phụ lục B BR
> **Source**: NotebookLM (id `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264`) + LOCAL `input/srs-v3/srs-fr-07-doanh-nghiep-v3.1.md` + `input/srs-update-05-05-2026/srs-fr-07-doanh-nghiep-v3.1.md` (giống nhau, không có delta)
> **Ngày tạo**: 2026-05-09
> **CHANGELOG ref**: `input/srs-v3/CHANGELOG-v3-to-v3.1.md` §srs-fr-07 (10 thay đổi cherry-pick + 1 OUT D.2.1 Xuất Excel)
> **Sibling check**: W2.2 CG-TVV (271 TC done 2026-05-09), W3.2 VV (294 TC FK trỏ DN), W1.4 TKPQ (FR-VIII-22 DN tự đăng ký), W2.4 CT GĐ1 (TVCS HSPL gộp tab)

---

## A. Phạm vi

**2 FR active · 2 SCR active · 0 SM · 2 entity owned + 1 cross-ref · 10 BR · 6 UC files · ~144 TC dự kiến**

### A.1 FR list (2 active + 1 BỎ + cross-ref)

| FR | UC | Mô tả | Trạng thái |
|----|----|----|----|
| FR-V.III-01 | UC81 | Quản lý DN được HTPL — Sửa / Xóa mềm / Xem chi tiết / Xem lịch sử / Xuất Excel | ✅ Active |
| FR-V.III-02 | UC82 | Tìm kiếm DN — 6 filter (từ khóa / quy mô / tỉnh / lĩnh vực multi / từ-đến ngày) + AND logic | ✅ Active |
| ~~FR-V.III-NEW-01~~ | ~~Mới~~ | ~~Import DN từ Excel~~ | ❌ BA chốt 2026-05-05 BỎ — DN tự đăng ký FR-VIII-22 |
| FR-V.III-01 (Thêm mới) | — | KHÔNG có chức năng Thêm mới CMS — DN tạo qua FR-VIII-22 (self-registration) | ❌ BỎ v3.1 |
| FR-X.1-04 (cross-ref) | UC150 | Quản lý hồ sơ pháp lý DN (HSPL) — gộp vào Tab 2 SCR-V.III-02 (DEPRECATED SCR-X1-03) | ✅ Active qua tab |

### A.2 SCR list (2 active + 1 deprecated)

| SCR | Mô tả | URL | Trạng thái |
|----|----|----|----|
| SCR-V.III-01 | Danh sách DN — toolbar (Xuất Excel / Làm mới) + filter-bar (6 filter) + table (8 cột) + pagination 20/page | `/doanh-nghiep/danh-sach` | ✅ Active |
| SCR-V.III-02 | Chi tiết DN — 4 TAB: (1) Thông tin cơ bản 28 trường + auto-suggest quy mô; (2) Hồ sơ PL DN (CRUD HSPL); (3) Lịch sử Hỗ trợ (3 KPI + DS VV); (4) Hồ sơ Chi trả (DS HS CT) | `/doanh-nghiep/:id` xem · `/doanh-nghiep/:id/sua` sửa | ✅ Active |
| ~~SCR-V.III-03~~ | ~~Wizard 3 bước Import Excel~~ | ~~`/doanh-nghiep/import`~~ | ❌ BỎ (đi cùng FR-V.III-NEW-01) — block test nếu UI vẫn còn → SPEC-CLARIFY-DN-01 |

### A.3 State Machines

**KHÔNG CÓ** — entity DOANH_NGHIEP không có vòng đời trạng thái (lifecycle). Bản ghi DN được tạo (qua FR-VIII-22 self-reg) / sửa / xóa mềm trực tiếp. Reference: `srs-fr-07-doanh-nghiep-v3.1.md:535`.

### A.4 Entity owned (2) + cross-ref (1)

| Entity | Vai trò | Mô tả | Volume |
|--------|------|-------|---|
| DOANH_NGHIEP | owned | Hồ sơ DNNVV (28 trường + 7 common fields). Tạo qua FR-VIII-22; CB NV chỉ Edit/Delete; UNIQUE `ma_so_thue` | ~10.000/năm |
| DOANH_NGHIEP_LINH_VUC | owned (junction N:N) | Liên kết DN ↔ DANH_MUC (`loai='LINH_VUC_KINH_DOANH'`). Multi-select. UNIQUE (`doanh_nghiep_id`, `linh_vuc_id`) WHERE `is_deleted=0` | ~30.000/năm |
| HO_SO_PHAP_LY_DN | cross-ref (FR-X.1-04) | Hồ sơ pháp lý DN — 5 loại (GIAY_PHEP/HOP_DONG/GIAY_CN/QUYET_DINH/KHAC) × 3 trạng thái (HIEU_LUC/HET_HAN/THU_HOI). Auto-gen mã `HSPL-{YYYYMMDD}-{SEQ}` | ~10.000/năm |

### A.5 BR list (10)

| BR ID | Tên | FR áp dụng |
|-------|-----|-----|
| BR-AUTH-01 | Xác thực truy cập (TOTP 2FA, OTP test=666666) | FR-V.III-01, 02, FR-X.1-04 |
| BR-AUTH-08 | Phân quyền dữ liệu theo đơn vị (cây 2 tầng TW → {BN, ĐP} ngang cấp) | FR-V.III-01, 02, FR-X.1-04 |
| BR-AUTH-EMAIL-01 | 2 email DN: `TAI_KHOAN.email` (UNIQUE, login + workflow) vs `DOANH_NGHIEP.email` (KHÔNG UNIQUE, công văn). Đổi độc lập, không cần OTP. | FR-V.III-02 (Edit DN.email) |
| BR-AUTH-USERNAME-01 | DN tự đăng ký auto username = ma_so_thue (10 chữ số, TT 105/2020/TT-BTC Điều 5) — read-only sau đăng ký | FR-VIII-22 (cross-ref) |
| BR-DATA-01 | Soft delete (set `is_deleted=1`) | FR-V.III-01, FR-X.1-04 |
| BR-DATA-02 | Multi-tenant scoping (mọi entity phải có `don_vi_id` NOT NULL) | FR-V.III-01 |
| BR-DATA-03 | Common fields (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id) | FR-V.III-01, FR-X.1-04 |
| BR-DATA-04 | Auto-gen mã: `DN-{TINH}-{SEQ}` (DN), `HSPL-{YYYYMMDD}-{SEQ}` (HSPL) | FR-V.III-01, FR-X.1-04 |
| BR-DATA-05 | Audit trail (mọi CUD ghi AUDIT_LOG immutable) | FR-V.III-01, FR-X.1-04 |
| BR-DATA-07 | Pagination default 20/page, max 100/page | FR-V.III-01, 02, FR-X.1-04 |
| BR-CALC-05 | Kiểm tra quy mô DNNVV (NĐ 39/2018/NĐ-CP Điều 5) — Siêu nhỏ/Nhỏ/Vừa theo LĐ + Doanh thu + Vốn | FR-V.III-01 (auto-suggest + WRN-DN-01) |

### A.6 Error codes (DN: 5 ERR + 1 WRN + 1 INF; HSPL: 6 ERR + 1 INF)

**Module DN:**
| Code | Severity | Message | Trigger |
|------|---|---|---|
| ERR-DN-01 | ERROR | "Tên doanh nghiệp là bắt buộc" | ten_doanh_nghiep rỗng |
| ERR-DN-02 | ERROR | "Mã số thuế đã tồn tại" | UNIQUE violation ma_so_thue |
| WRN-DN-01 | WARNING | "Quy mô {X} không khớp với số liệu lao động/doanh thu. Vẫn lưu?" | BR-CALC-05 mismatch |
| ERR-DN-03 | ERROR | "Không thể xóa DN đang có vụ việc xử lý" | DELETE khi có VV state ≠ HOAN_THANH/HUY |
| ERR-DN-04 | WARNING | "Kết quả vượt 10.000 dòng. Vui lòng thu hẹp bộ lọc" | Export Excel > 10K rows |
| INF-DN-TK-01 | INFO | "Không tìm thấy doanh nghiệp phù hợp" | Search 0 result |

**Module HSPL (cross-ref FR-X.1-04):**
| Code | Severity | Message | Trigger |
|------|---|---|---|
| ERR-HSPL-01 | ERROR | "Tên hồ sơ pháp lý là bắt buộc" | ten_ho_so rỗng |
| ERR-HSPL-02 | ERROR | "Doanh nghiệp không tồn tại hoặc đã bị xóa" | doanh_nghiep_id invalid |
| ERR-HSPL-03 | ERROR | "File đính kèm tối đa 20MB" | file > 20MB |
| ERR-HSPL-04 | ERROR | "File '{ten_file}' chứa mã độc, không thể tải lên" | virus scan fail |
| ERR-HSPL-05 | ERROR | "Loại hồ sơ '{loai}' không hợp lệ" | loai_ho_so ∉ enum 5 |
| ERR-HSPL-06 | ERROR | "Ngày bắt đầu phải trước ngày kết thúc" | tu_ngay > den_ngay (search) |
| INF-HSPL-01 | INFO | "Không tìm thấy hồ sơ pháp lý phù hợp" | Search 0 result |

---

## B. Permission Matrix (snapshot từ srs-v3.5 §3.4.2)

**Ký hiệu:** C=Create, R=Read toàn cục, R*=Read scoped, U=Update, D=Delete (soft), —=No access

### B.1 DOANH_NGHIEP

| Entity | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | DN | NHT | TVV | CG |
|--------|------|----------|----------|----------|----------|----------|----------|----|-----|-----|----|
| DOANH_NGHIEP | R | CRUD* | CRUD* | CRUD* | R* | R* | R* | RU* | — | — | — |
| DOANH_NGHIEP_LINH_VUC | R | CRUD* | CRUD* | CRUD* | R* | R* | R* | RU* | — | — | — |
| HO_SO_PHAP_LY_DN | R | CRUD* | CRUD* | CRUD* | R* | R* | R* | RU* | CRU* | — | — |

> **Lưu ý**: Theo `srs-v3.5.md` §3.4.2 ghi chú "DN không truy cập CMS trực tiếp. Quyền Create/Read của DN thực hiện qua API inbound từ Cổng PLQG". DN trong test scope CMS = không truy cập; DN truy cập chuyên trang riêng (Nhóm VII Cổng PLQG).
> **CB_NV CRUD\***: ngoại lệ "C" — `Create` qua self-reg FR-VIII-22, **CB NV không tạo DN trực tiếp** từ CMS (BA chốt 2026-05-05 — Thay đổi 2). Nên CB NV chỉ test RUD trên CMS.
> **NHT trên HSPL**: `CRU*` ngoại lệ — chỉ R + U, **không Create + không Delete** (xem AC FR-X.1-04 dòng 671 SRS) — clarify cuối phần 3.

### B.2 SCR-V.III-02 menu visibility per role

| Role | Tab Thông tin cơ bản | Tab HSPL | Tab Lịch sử | Tab Chi trả | Edit nút | Delete nút |
|------|---|---|---|---|---|---|
| qtht_01 | R | R | R | R | — (R toàn cục) | — |
| cb_nv_tw_01 / bn_01 / dp_01 | RU\* (CRUD\* tổng) | CRUD\* | R\* | R\* (cross-ref FR-06) | ✅ scope | ✅ scope (BR-DATA-01) |
| cb_pd_tw_01 / bn_01 / dp_01 | R\* | R\* | R\* | R\* | — | — |
| dn_01 (chuyên trang) | RU\* (own) | RU\* (own) | R\* (own) | R\* (own) | ✅ chính DN | — |
| nht_01 | — DN list KHÔNG hiện trên sidebar CMS — | R\*+U\* (own VV scope) | — | — | — (chỉ HSPL) | — |
| tvv_01 / cg_01 | — | — | — | — | — | — |

---

## C. Files structure (6 UC + 4 audit)

| File | TC dự kiến | Mô tả |
|------|----:|-----|
| `00-test-plan-overview.md` | — | File này |
| `01-TC-FR-V.III-01-quan-ly-dn-CRUD.md` | ~30 | Edit DN (28 trường) + Xóa mềm + auto-suggest quy mô + WRN-DN-01 + auto-gen mã + KHÔNG có Thêm mới |
| `02-TC-FR-V.III-02-tim-kiem-dn.md` | ~25 | Tìm kiếm 6 filter + AND + Xuất Excel + ERR-DN-04 boundary |
| `03-TC-tab-ho-so-phap-ly-dn.md` | ~30 | Tab 2 SCR-V.III-02: CRUD HSPL (5 loại × 3 trạng thái) + upload file 20MB + virus scan |
| `04-TC-tab-lich-su-ho-tro.md` | ~15 | Tab 3 SCR-V.III-02: 3 KPI (Tổng VV / VV hoàn thành / Tổng chi phí) + DS VV liên kết readonly |
| `05-TC-tab-ho-so-chi-tra.md` | ~15 | Tab 4 SCR-V.III-02: DS HS chi trả liên kết (cross-ref FR-06) readonly |
| `06-TC-permission-matrix.md` | ~25 | BR-AUTH-01 + BR-AUTH-08 cây 2 tầng + BR-AUTH-EMAIL-01 + IDOR cross-tenant + AUDIT_LOG verify |
| `08-REVIEW-edge-case-hunter.md` | — | A4 audit log (proposal + merge mapping) |
| `09-traceability-matrix.md` | — | A5 BR/AC/SM/Permission/Error ↔ TC |
| `10-REVIEW-test-quality.md` | — | A6 issue list + score |
| `11-a7-filter-log.md` | — | A7 LOẠI/SỬA/GIỮ log |

**Tổng dự kiến A3: ~140 TC** (sát ước todo.md ~144).

---

## D. Test data seed plan (Phase B)

| Loại | Mô tả | Quantity | Phương thức |
|------|------|---:|---|
| DN HOAT_DONG TW | DN do CB NV TW tạo | ≥3 | Self-reg FR-VIII-22 + CB NV TW edit |
| DN HOAT_DONG BN | DN thuộc Bộ Tư pháp | ≥2 | Tương tự |
| DN HOAT_DONG ĐP HN/HP | DN ngang cấp địa phương | ≥3 mỗi tỉnh | Verify BR-AUTH-08 |
| DN có VV đang xử lý | Block test xóa | ≥1 | Cross-FR-05 (W3.2) |
| DN có HS chi trả | Tab 4 verify | ≥1 | Cross-FR-06 |
| DN multi linh_vuc | Test M-N | ≥1 với 3 LV | Multi-select |
| HSPL × 5 loại × 3 trạng thái | Tab 2 verify | 15 record | CB NV/NHT tạo |
| MST trùng | Edge ERR-DN-02 | 1 | Tạo trước |
| Quy mô mismatch | WRN-DN-01 | 1 (LĐ=300, quy mô=NHỎ) | Edge BR-CALC-05 |
| Excel >10K | ERR-DN-04 | environment OR mock filter | Cap test |

**Account test (per `users.csv` Secret@123):**
- qtht_01 — toàn cục R
- cb_nv_tw_01 / cb_nv_bn_01 / cb_nv_dp_01 — CRUD scope (chỉ RUD vì BỎ Create)
- cb_pd_tw_01 / cb_pd_bn_01 / cb_pd_dp_01 — R scope (Phê duyệt không có ở DN module)
- nht_01 — HSPL R/U own VV scope
- dn_01 — chuyên trang DN tự xem RU own (KHÔNG test CMS — Permission Matrix dòng 1262)

---

## E. Acceptance criteria Phase A done

- ✅ A1-A7 hoàn thành (7 bước)
- ✅ Traceability ≥95% BR + 100% AC + 100% Error code (dự kiến)
- ✅ 0 TC chỉ-DB/API thuần sau A7 filter
- ✅ Mọi TC mới từ A4/A6 inline merge vào file UC gốc; file 08/10/11 chỉ là audit
- ✅ SPEC-CLARIFY listed kèm proposal answer (gửi BA Phase B)
- ✅ Codex review pass-fail gate

---

## F. SPEC-CLARIFY pending (sẽ accumulate qua A1-A7 + Codex)

> Sẽ list cuối quá trình. Pre-known clarify từ A1:
> - **SPEC-CLARIFY-DN-01**: SCR-V.III-03 Wizard Import Excel **vẫn còn** trong file SRS (line 387-416) dù FR-V.III-NEW-01 đã BỎ — UI có còn nút/route `/doanh-nghiep/import` không? Áp dụng memory rule "UI vs business → theo business" → assume BỎ hoàn toàn cả route + UI.
> - **SPEC-CLARIFY-DN-02**: Header file SRS ghi "Phiên bản 3.0" nhưng filename `v3.1.md` + đã có cherry-pick 10 thay đổi → assume tag v3.1 (per CHANGELOG entry 1372).
> - **SPEC-CLARIFY-DN-03**: SCR-V.III-02 dòng 22 "Fax" — Inputs FR-V.III-01 không liệt kê, Entity DOANH_NGHIEP có `fax` (line 1594 srs-v3.5). Form CMS có hiển thị field này không?

---

**— Hết 00 Test Plan Overview FR-07 v3.1 —**
