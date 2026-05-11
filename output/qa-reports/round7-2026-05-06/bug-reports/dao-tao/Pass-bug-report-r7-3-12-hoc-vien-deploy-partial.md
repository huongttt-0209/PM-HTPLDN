# Bug Report — HOC_VIEN Service POST Crash (R7.3.12 R10)

> **Module:** Đào tạo / Học viên (HOC_VIEN entity FR-III)
> **Discovered:** 2026-05-10 02:55 (R7.3.12 R10 re-probe)
> **Updated:** 2026-05-10 03:05 (after SRS FR-III-04 cite — corrected misclassified findings)
> **Reporter:** QA Automation Claude Code MCP

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| ~~BUG-HV-BE-01~~ | **Major** | POST `/api/v1/hoc-viens` (qtht_01) với valid DTO match swagger schema → 500 `ERR-SYS-00-00-01` (service crash) | **Closed** (R11 verified 2026-05-11 — BE thay crash 500 bằng 403 guard đúng spec FR-III-04) |
| ~~BUG-HV-FE-01~~ | ~~Major~~ | ~~FE thiếu route HV master CMS~~ → **WITHDRAWN** sau cite SRS FR-III-04: HV được tạo qua chuyên trang DN/NHT (UC23), KHÔNG có CMS form CB NV/QTHT manage. FE thiếu page master là **đúng spec**. Cần verify riêng chuyên trang DN có hoạt động không (out of scope task seed). | N/A |
| ~~BUG-HV-PERM-01~~ | ~~Medium~~ | ~~Permission cb_nv_tw_02 + cb_pd_tw_02 403~~ → **WITHDRAWN** sau cite SRS FR-III-04 line 397-399: Tác nhân = DN/NHT (chuyên trang). CB NV chỉ duyệt DANG_KY_DAO_TAO (FR-III-03 UC22 RU* trên DKDT), KHÔNG CRUD HV master. → 403 đúng spec. QTHT 200 vì admin scope `👁️ R` toàn hệ thống. | N/A |

---

## R10 vs R9 status change (KEY)

| Aspect | R9 (2026-05-09 20:33) | R10 (2026-05-10 02:48) |
|---|---|---|
| `/api/v1/hoc-viens` GET | 404 Cannot GET | **200 (qtht_01)** + 403 (cb_nv_tw, cb_pd_tw — đúng spec) |
| `/api/v1/hoc-viens` POST | 404 | **500 ERR-SYS-00-00-01** (qtht_01 valid DTO) |
| Swagger `/api/docs-json` HOC_VIEN | (chưa probe) | 5 routes registered: GET list, POST, GET/PATCH/DELETE by id |
| FE menu / sidebar CMS | 0 menu | **Vẫn 0 menu** (per spec — DN/NHT tạo qua chuyên trang) |
| FE route `/dao-tao/hoc-vien*` CMS | (chưa probe) | 404/redirect (per spec) |

→ **Status change real:** R9 "BE chưa code entity" → R10 "BE deploy + service POST handler crash". 1 bug Major thật (BE-01); 2 bug R10 lần đầu log đã withdraw sau spec cite.

---

## ~~BUG-HV-BE-01~~ [CLOSED] — POST /hoc-viens 500 với valid DTO (qtht_01)

> **Re-test:** 2026-05-11 R11 — ✅ PASS (Closed-verified). Sau cache clear + fresh login `qtht_01`, probe 3 case POST `/api/v1/hoc-viens`:
> - **P1 minimal valid** `{hoTen, email}` → **403 `ERR-PERM-SYS-00-01 "Forbidden"`** (không còn 500 crash)
> - **P2 full fields** `{hoTen, email, soDienThoai, donVi}` → **403** (cùng pattern)
> - **P3 invalid email** `{hoTen, email: "not-an-email"}` → **403** (permission check trước validation)
>
> BE giờ enforce **permission guard 403** thay vì crash 500. Match SRS FR-III-04 (UC23): HV master tạo qua chuyên trang DN/NHT, KHÔNG qua admin POST. QTHT chỉ có quyền `👁️ R` toàn hệ thống — verify GET `/api/v1/hoc-viens` (qtht_01) → **200 trả 6 records** (đã seed bởi DN/NHT/dev R11 2026-05-11), confirm permission scope đúng.
>
> 6 records HV trong DB (`QA R7 BC008 HV` + `QA R7 HV 01..05`) — source unclear nhưng có khả năng tạo qua chuyên trang DN/NHT FR-III-04 hoặc admin DB-direct seed. Không qua endpoint POST /hoc-viens vì giờ guard 403.
>
> Bug code-side đã closed. Screenshot: [r11-hv-be-01-no-more-500-crash.png](../../screenshots/r11-hv-be-01-no-more-500-crash.png).

### Mô tả
Endpoint `POST /api/v1/hoc-viens` đã deploy + swagger expose schema đúng (`hoTen`, `email` required + `soDienThoai`, `donVi` optional). Body hợp lệ với schema vẫn trả 500 generic, không phải 422 validation. Service layer crash.

### Bước tái hiện
```bash
# Login qtht_01 (role có quyền POST per admin scope)
TOKEN=<qtht_01 access_token>

# POST minimal valid body theo swagger DTO
curl -X POST http://103.172.236.130:3000/api/v1/hoc-viens \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"hoTen":"R10 Test HV-001","email":"hv001r10@htpldn.test"}'
```

### Kết quả mong đợi
- HTTP 201 Created
- Body trả HOC_VIEN record với UUID + ngayTao + version=1

### Kết quả thực tế
```json
HTTP 500
{
  "success": false,
  "error": {
    "code": "ERR-SYS-00-00-01",
    "message": "Lỗi hệ thống, vui lòng thử lại sau",
    "timestamp": "2026-05-09T19:52:11.074Z",
    "requestId": "52613db9-06ec-4834-b7e7-c8ba8527263b"
  }
}
```

Thử nhiều biến thể (full 4 fields, thêm soDienThoai, donVi, mst, dnId, taiKhoanId, gioiTinh, ngaySinh, etc.) → vẫn 500. Khi test với invalid `email` → 422 ERR-VAL-SYS-00-01 đúng (validation layer OK, chỉ service crash).

### Bằng chứng

**Swagger DTO discovered (`/api/docs-json`):**
```json
CreateHocVienDto:
  required: [hoTen, email]
  properties:
    - hoTen: string
    - email: string
    - soDienThoai: string
    - donVi: string
```

**Network log:**
- POST /hoc-viens body `{"hoTen":"x","email":"valid@test.com"}` → 500 (service crash)
- POST /hoc-viens body `{"email":"invalid","hoTen":"x"}` → 422 `field=email must be an email` (validation OK)

→ Suspected: BE service implementation thiếu logic xử lý mặc định fields (vd auto-fill nguoiTaoId, donViId từ JWT context, hoặc handle null taiKhoanId). Cần dev debug log.

### Recommend dev BE
- Debug `hocVienService.create()` để tìm crash point
- Trả 422 với field name nếu thiếu data, không 500 generic
- Verify entry-point này dùng cho ai (per spec FR-III-04 user-facing là DN/NHT qua chuyên trang). Có thể endpoint này chỉ dành admin seed manual hoặc backup CMS — cần BA xác nhận intent.

---

## ~~BUG-HV-FE-01~~ và ~~BUG-HV-PERM-01~~ — WITHDRAWN sau SRS cite

### Lý do withdraw

**SRS FR-III-04 (UC23) line 397-468:**
> **Mô tả:** DN/NHT đăng ký tham gia khóa học qua chuyên trang. 3 cách: chuyên trang, nhập tay, import Excel.
> **Tác nhân:** DN / NHT
> **Inputs:** ho_ten, email, so_dien_thoai, don_vi, ghi_chu, nguon_dang_ky (CHUYEN_TRANG / NHAP_TAY / IMPORT_EXCEL)
> **Processing:**
> | 1 | Kiểm tra khóa học đang mở (DA_CONG_KHAI) | SM-KHOAHOC |
> | 2 | Kiểm tra chưa đăng ký trùng | — |
> | 3 | Xác nhận dữ liệu đầu vào | — |
> | 4 | Tạo bản ghi DANG_KY_DAO_TAO, trạng thái = CHO_DUYET | — |

**SRS FR-III-03 (UC22) line 325-388:**
> **Mô tả:** Quản lý đăng ký đào tạo
> **Tác nhân:** CB NV (duyệt/từ chối DKDT)

**Suy diễn permission đúng:**
| Role | HOC_VIEN master | DANG_KY_DAO_TAO | Cách tạo HV |
|---|---|---|---|
| DN | ✅ Create (qua chuyên trang) | ✅ Create | Self-registration FR-III-04 |
| NHT | ✅ Create (qua chuyên trang) | ✅ Create | Self-registration FR-III-04 |
| CB NV | 👁️ R | 📝 RU* (duyệt) | KHÔNG tạo HV master, chỉ duyệt DKDT |
| CB PD | 👁️ R (cùng cấp) | 👁️ R | KHÔNG tạo HV master |
| QTHT | 👁️ R toàn hệ thống | 👁️ R | KHÔNG tạo HV master, chỉ admin seed manual nếu được phép |

→ **403 cho cb_nv_tw_02 và cb_pd_tw_02 trên POST `/hoc-viens` là ĐÚNG SPEC.** Tôi đã sai khi log BUG-HV-PERM-01.

→ **FE thiếu CMS page HV master cho CB NV/QTHT là đúng spec** — entry-point user là chuyên trang DN/NHT (FR-III-04). FE chỉ cần render tab "Học viên" trong KH detail (= DKDT list, đã có) + chuyên trang DN/NHT register flow (cần verify riêng — out of scope task R7.3.12 seed).

→ **BUG-HV-FE-01 cũng withdraw**, BUT cần follow-up task verify chuyên trang DN/NHT FR-III-04 form đăng ký có hoạt động không. Out of scope R7.3.12 (seed task scope là tạo HV master records, không test self-reg flow).

### Implication cho R7.3.12 seed task

Per spec: HV master records được tạo qua DN/NHT chuyên trang self-reg (FR-III-04). Seed task R7.3.12 nên:
- **Option A:** Login DN account (vd `dn_test_01` nếu có) → đăng ký KH qua chuyên trang → tạo HV master + DKDT
- **Option B:** Login NHT account → cùng flow
- **Option C:** Admin seed manual qua POST `/hoc-viens` (qtht_01) — hiện block bởi BUG-HV-BE-01

→ Cần xác minh chuyên trang DN có hoạt động không trong session khác. R7.3.12 hiện vẫn 🚫 do BUG-HV-BE-01 + chưa test chuyên trang DN.

---

## Recommend escalate

**Dev BE** — fix BUG-HV-BE-01:
- Debug service `hocVienService.create()` để tìm crash point
- Trả 422 field-level error nếu thiếu context, không 500 generic
- Verify endpoint POST `/hoc-viens` intent (admin seed? backup CMS?)

**BA confirm** — clarify entry-point HV master:
- HV master tạo qua FR-III-04 chuyên trang DN/NHT (UC23) là duy nhất, hay BE expose admin-only POST `/hoc-viens` cho seed/backup?
- Nếu admin endpoint thuộc QTHT → cần thêm row HOC_VIEN trong [permission-matrix.md](../../../../permission-matrix.md) `QTHT 👁️ R` với note "POST chỉ cho admin seed manual"

**Test follow-up** (out of scope R7.3.12):
- Login DN account → navigate chuyên trang Cổng PLQG `/dao-tao/khoa-hoc/<id>/dang-ky` (suspected route) → verify form đăng ký FR-III-04
- Test 3 cách: chuyên trang / nhập tay / import Excel

---

*R10 log | QA Automation via Claude Code MCP | 2026-05-10 02:55 (created), 03:05 (corrected after SRS cite)*
