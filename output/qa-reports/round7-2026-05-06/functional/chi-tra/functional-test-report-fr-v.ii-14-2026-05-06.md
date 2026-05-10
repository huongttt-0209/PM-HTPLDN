# Functional Test Report — FR-V.II-14 DN bổ sung hồ sơ chi trả

> **Module:** Chi trả chi phí (FR-V.II / FR-06) · **Task:** R7.7.12.2 · **Round:** R7-R2 (2026-05-10 02:10:00) · **Tester:** QA Automation via Claude Code
> **SRS:** [`srs-update-2026-5-5/srs-fr-06-chi-tra.md FR-V.II-14`](../../../../input/srs-update-2026-5-5/srs-fr-06-chi-tra.md) · [`02-thu-tu-module.md §10 SM-CHI-TRA B7`](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md)
> **Bug:** [`bug-report-flow-chi-tra.md`](../../bug-reports/chi-tra/bug-report-flow-chi-tra.md)

---

## Kết luận

🚫 **BLOCKED — không có HSCT thuộc QA DN trong môi trường test.**

Nguyên nhân gốc xác định 3 path tạo HSCT đều không khả dụng:

| Path tạo HSCT | Trạng thái | Bằng chứng |
|---|---|---|
| BE API direct `POST /api/v1/ho-so-chi-tras` | ❌ 404 ERR-SYS-00-04-01 | Confirmed 2026-05-10 02:05 — endpoint không tồn tại |
| UI manual ở CB NV (cb_nv_dp_01 AG) | ❌ Không có nút "Thêm mới" trên toolbar Quản lý chi trả | Snapshot toolbar chỉ có "Xuất Excel" + "Làm mới" |
| UI manual ở DN (QA DN tự reg, MST 1234567899) | ❌ Empty list, không có nút tạo | Snapshot list "Không có hồ sơ nào phù hợp" |
| DVC integration (tích hợp `dvc.gov.vn`) | ❌ Out of scope test env | Spec FR-V.II-01: HSCT tạo qua DVC sync vào CHO_TIEP_NHAN |

Pool hiện có **4 HSCT YEU_CAU_BO_SUNG** ở AG scope (HSCT000011/12/13/14) thuộc 4 DN khác (Bình Minh AG / Phúc An AG / Hoàng Gia AG / Đại Việt AG) nhưng `users.csv` không có credentials cho các DN đó — không thể login.

---

## Test approach đã thử

### Approach 1 — Tự register QA DN

✅ **Thành công** ở bước reg + activate:
- DN ID: `6738f415-8192-456c-89dd-ba6a0e7e2493`
- MST/Username: `1234567899`
- Email: `qatest_r7@htpldn.test`
- Tỉnh: An Giang (match cb_nv_dp_01 scope)
- Quy mô: SIEU_NHO
- Activation token: `4c891d1e-9f85-4fb9-acd8-24d74fc5dde1`

❌ **Sau login DN không có HSCT để bổ sung** — bảng `Hồ sơ Đề nghị Hỗ trợ Chi phí` empty: "Không có hồ sơ nào phù hợp". Không có nút "Tạo mới HSCT" / "Bổ sung" cho DN.

### Approach 2 — POST API direct

```bash
POST /api/v1/ho-so-chi-tras
Authorization: Bearer <cb_nv_dp_01 token>
Body: { doanhNghiepId: "<QA-DN-id>", soTienDeNghi: 2000000, ... }
→ HTTP 404 { "code": "ERR-SYS-00-04-01", "message": "Cannot POST /api/v1/ho-so-chi-tras" }
```

Endpoint không tồn tại. BE chỉ expose action endpoints (`/tu-choi`, `/phe-duyet`, `/cap-nhat-thanh-toan`...) — không có create endpoint manual.

### Approach 3 — UI CB NV tạo HSCT thay DN

❌ Sau login `cb_nv_dp_01` (AG), Quản lý chi trả chi phí toolbar chỉ có:
- `download Xuất Excel`
- `reload Làm mới`

KHÔNG có nút "Thêm mới HSCT" / "Tạo HSCT". Action per row chỉ: Kiểm tra (B2), Thẩm định, Trình PD. Spec FR-V.II-01 design: HSCT đến từ DVC, không phải CB tạo.

---

## Defect ghi nhận

KHÔNG log bug app — đây là **test infrastructure gap** (thiếu seed path cho QA DN), không phải bug code.

**Đề xuất escalate:**

1. **Dev seed HSCT cho QA DN** — script INSERT 1-2 HSCT vào `ho_so_chi_tra` với `doanhNghiep_id = 6738f415-8192-456c-89dd-ba6a0e7e2493` ở state `YEU_CAU_BO_SUNG`, đủ field BR-CALC-01 đúng (SIEU_NHO 100% / 3M).

2. **HOẶC mở DVC integration mock** — endpoint test/staging cho QA submit HSCT giả lập DVC.

3. **HOẶC thêm credentials cho 4 DN AG hiện có** vào `users.csv`:
   - Công ty TNHH Bình Minh AG (HSCT000011)
   - Công ty Cổ phần Phúc An AG (HSCT000012)
   - DNTN Hoàng Gia AG (HSCT000013)
   - Hộ kinh doanh Đại Việt AG (HSCT000014)

   → QA login DN gốc, click "Bổ sung" trên HSCT YCBS, test 5 file format upload + content.

Phương án 3 fastest, không cần dev code mới — chỉ thêm row CSV + sync `auth_users`.

---

## Coverage tóm tắt

- ❌ B7 (YCBS → DKT bổ sung) — không test được, thiếu HSCT YCBS thuộc DN có credentials.
- ❌ Upload 5 định dạng (PDF/DOC/DOCX/JPG/PNG ≤10MB) — không test được, blocked upstream.
- ✅ Validation negative (out of scope file type, >10MB) — không test được, blocked upstream.

**Liên quan:**
- BUG-CHITRA-001 ⚠️ Open — pool 97/108 sai BR đầy đủ, gián tiếp ảnh hưởng test environment.
- R7.6.1 ⚠️ ~83% — B6 (DKT→YCBS) chưa walk thành công với HSCT thuộc QA DN; pool có YCBS sẵn nhưng credentials missing.
