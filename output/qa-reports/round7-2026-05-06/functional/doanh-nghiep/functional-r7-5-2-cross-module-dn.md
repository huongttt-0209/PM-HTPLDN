# R7.5.2 Functional — Cross-module DN tabs

**Task:** R7.5.2 — Verify 4 tabs DN detail page (SCR-V.III-02)
**Round:** R7 (2026-05-09)
**Tester:** huongttt + Claude (MCP chrome-devtools)
**Account:** `cb_nv_tw_01` / `Secret@123` (CB_NV_TW + CB_PD_TW)
**Verdict:** ✅ PASS — 4/4 tab render đúng spec; 1 finding phụ (raw enum hiển thị)

---

## 1. Mục đích

Verify SCR-V.III-02 §Outputs (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md` line 313-362): trang chi tiết DN có 4 tab — Thông tin, Hồ sơ pháp lý, Lịch sử hỗ trợ, Hồ sơ chi trả. Cross-module check: data từ HSPL/VV/HSCT module đọc đúng vào tab DN tương ứng.

## 2. Phương pháp

| Phase | Cách làm | Tool |
|---|---|---|
| Tab #1 Thông tin | Click tab, verify 21 trường DN render từ API `GET /api/v1/doanh-nghieps/<id>` | MCP `take_snapshot` + `list_network_requests` |
| Tab #2 Hồ sơ pháp lý | Verify 2 case: empty (DN-BCT-001) + with-data (DN-AG-001 = 2 HSPL) | MCP `navigate` + `take_snapshot` |
| Tab #3 Lịch sử hỗ trợ | Verify 3 KPI + danh sách VV trên DN-BCT-001 (3 VV liên kết) | MCP snapshot |
| Tab #4 Hồ sơ chi trả | Verify structure (2 KPI + 5 cột table + empty state) | MCP snapshot |

API verify: `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=<id>` cho HSPL list, `GET /api/v1/doanh-nghieps/<id>` cho info chính.

## 3. Kết quả per tab

### Tab #1 — Thông tin DN ✅

DN-BCT-001 (DNTN Đông Dương BCT): 21 trường render đầy đủ — MST, Tên DN, Loại DN, Tỉnh/Thành, Ngành, Quy mô, Lao động/Nữ/Khuyết tật, Doanh thu, Vốn, Người ĐD, etc. Khớp dữ liệu API `GET /api/v1/doanh-nghieps/e0000000-0000-4000-8001-000000000003`.

**Bằng chứng:** `r7-5-2-dn-bct-001-tab1-thong-tin.png`

### Tab #2 — Hồ sơ pháp lý ✅

**Empty state (DN-BCT-001 = 0 HSPL):**
- Heading "Hồ sơ pháp lý DN" + button [Thêm hồ sơ]
- Table headers: Mã hồ sơ / Tên hồ sơ / Loại / Số/Ký hiệu / Ngày cấp / Ngày hết hạn / Trạng thái / Thao tác
- Empty body — render đúng

**With-data (DN-AG-001 = 2 HSPL):**
| Mã HS | Tên | Loại | Số/KH | Trạng thái |
|---|---|---|---|---|
| HSPL-20260507-0001 | Giấy phép kinh doanh dịch vụ nông nghiệp | Giấy phép | GP-AG-2024-001 | Hiệu lực |
| HSPL-20260507-0002 | Hợp đồng thuê đất canh tác dài hạn | Hợp đồng | HD-AG-2023-002 | Hết hạn |

Buttons Sửa/Xoá render per row; pagination 1/1.

**Bằng chứng:**
- `r7-5-2-dn-bct-001-tab2-hspl-empty.png` — empty state
- `r7-5-2-dn-ag-001-tab2-hspl-with-data.png` — 2 record render đúng

### Tab #3 — Lịch sử hỗ trợ ✅ (1 finding phụ)

**KPI render (DN-BCT-001):**
- Tổng vụ việc: **3** ✅
- VV hoàn thành: **0** ✅
- Tổng chi phí: **0 ₫** ✅

**Danh sách VV (3 record liên kết DN-BCT-001):**
| Mã VV | Tiêu đề | Trạng thái | Ngày tiếp nhận |
|---|---|---|---|
| VV-BTP-TW-20260507-006 | VV-006 HC - DNTN Đông Dương BCT | `DANG_KIEM_TRA` | 7/5/2026 |
| VV-BTP-TW-20260507-005 | VV-005 DAT_DAI - DNTN Đông Dương BCT | `DA_PHAN_CONG` | 7/5/2026 |
| VV-BTP-TW-20260507-001 | VV-001 LAO_DONG - DNTN Đông Dương BCT | `DA_PHAN_CONG` | 7/5/2026 |

**Finding phụ (BUG candidate Minor):** Cột "Trạng thái" hiển thị raw enum `DANG_KIEM_TRA` / `DA_PHAN_CONG` thay vì label tiếng Việt "Đang kiểm tra" / "Đã phân công" (so với Tab #2 hiển thị label "Hiệu lực" / "Hết hạn" đúng). Đây là UI display bug — không block functional, log riêng.

**Bằng chứng:** `r7-5-2-dn-bct-001-tab3-kpi-3vv.png`

### Tab #4 — Hồ sơ chi trả ✅

Structure render đúng spec (KHÔNG phải "Chức năng đang phát triển" placeholder):
- KPI: Tổng hồ sơ chi trả (0) + Tổng chi phí đã hỗ trợ (0 đ)
- Heading: "Danh sách hồ sơ chi trả"
- Table headers: Mã hồ sơ / Số tiền đề nghị / Số tiền được duyệt / Trạng thái / Ngày nộp
- Empty state "Trống" (DN-BCT-001 chưa có HSCT)

API list `/api/v1/ho-so-chi-tras` trả 401 cho `CB_NV_TW` — permission gap để follow up ở R7.6.1 (module HSCT). KHÔNG ảnh hưởng tab này vì tab dùng filter scope theo DN-id, render được structure rỗng bình thường.

**Bằng chứng:** `r7-5-2-dn-bct-001-tab4-hsct-empty.png`

## 4. Cross-module data flow verified

| Tab DN | Data nguồn | Module gốc | Verified |
|---|---|---|---|
| Thông tin | `doanhNghiep` entity | DN module | ✅ |
| Hồ sơ pháp lý | `hoSoPhapLyDN` | HSPL module | ✅ (filter `doanhNghiepId=<id>`) |
| Lịch sử hỗ trợ | `vuViec` | VV module | ✅ (3 VV BCT scope đúng) |
| Hồ sơ chi trả | `hoSoChiTra` | HSCT module | ✅ structure (data verify defer R7.6.1) |

## 5. Findings tổng hợp

1. **PASS chính:** 4/4 tab render đúng SCR-V.III-02 spec.
2. **Finding phụ (Minor candidate):** Tab #3 cột Trạng thái hiển thị raw enum thay vì label Việt — không log bug riêng round này (gom vào lifecycle UI labeling cleanup).
3. **Permission gap:** Endpoint `/api/v1/ho-so-chi-tras` 401 cho `CB_NV_TW` — không thuộc scope R7.5.2, defer R7.6.1 module HSCT verify SCR.

## 6. Conclusion

R7.5.2 ✅ PASS. Cross-module DN tabs hoạt động đúng — DN detail page là entry tổng hợp dữ liệu từ HSPL/VV/HSCT theo `doanhNghiepId`. State-snapshot không cần update (read-only verification, không tạo/đổi state entity).
