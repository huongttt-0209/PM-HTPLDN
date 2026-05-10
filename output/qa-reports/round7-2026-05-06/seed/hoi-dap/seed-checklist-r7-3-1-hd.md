# Seed Checklist — Hỏi đáp pháp lý (R7.3.1)

> ✅ **R8 UI re-test 2026-05-09:** Seed lại 6 HD MOI qua **UI Drawer Thêm mới (SCR-II-01)** với tài khoản `cb_nv_tw_02`, không POST API. 6 record mới `HD-20260509-001..006` cover đủ 6 LV × 4 kênh. Network supporting evidence: 6× `POST /api/v1/hoi-daps [201]` (reqid 221/228/235/241/248/255) đều phát từ form submit click "Lưu", và `GET /api/v1/hoi-daps?tab=MOI&page=1&pageSize=20 [200]` (reqid 259) trả `meta.total=8` (6 UI-R7 + 2 pre-existing). Verify per-filter PASS — đóng task ⚠️ → ✅.
>
> ⚠️ **Method gap cũ (note 2026-05-08):** Lần seed gốc R7 chạy qua API thuần `POST /api/v1/hoi-daps` — vi phạm rule UI-only ban hành 2026-05-07. Đã re-test UI MCP R8, giữ lại lịch sử bảng dữ liệu API gốc bên dưới làm tham khảo.

**Ngày:** 2026-05-06 14:47 • **Tài khoản:** `cb_nv_tw_01` • **Trạng thái mong đợi:** `MỚI` (entry)
**Màn:** SCR-II-01 — Quản lý hỏi đáp • **Đường dẫn:** `/hoi-dap`
**Dữ liệu mẫu:** [seed-fixture.yaml v2.7.1 > hoi_dap_variants[1..6]](../../../../input/data/seed-fixture.yaml)
**SRS:** [FR-II-01 — Hỏi đáp pháp lý](../../../../input/srs-update-2026-5-5/srs-fr-ii-hoi-dap.md)

---

## Downstream consumer × filter (BẮT BUỘC trước khi seed)

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.4.A4 Workflow Hỏi đáp 11 transition | `trang_thai=MOI` (FR-II-01) | ≥6 / 6 LV × 4 kênh | `MOI` | `GET /api/v1/hoi-daps?trangThai=MOI` → 6 ≥ 6 | ✅ |
| R7.7.1 Functional 12 TC | `trang_thai=MOI ∧ linh_vuc khớp 6 LV` | ≥1/LV | `MOI` | per-LV count ≥1 | ✅ |
| R7.5.1 Dashboard KPI Hỏi đáp mới | tab counter `MOI` | total = 6 | `MOI` | dashboard `Hỏi đáp mới: 6` | ✅ |

**Acceptance pass:** mọi row Status ✅ qua API verify.

---

## Kết quả

### R8 (2026-05-09 — UI Drawer, account `cb_nv_tw_02`) ✅ XONG 6/6

Seed 6 HD entry MOI qua **UI Drawer Thêm mới SCR-II-01** (click "+ Thêm mới" → fill form → click "Lưu"). Cover 6 LV × 4 kênh (TRUC_TIEP / DVC / CONG_PLQG / HE_THONG_KHAC). Verify per-filter qua tab "Mới" + response `GET /api/v1/hoi-daps?tab=MOI` PASS.

| # | Mã HD | Lĩnh vực | Kênh | Người gửi | reqid POST |
|---|-------|----------|------|-----------|------------|
| 1 | HD-20260509-001 | Lao động | TRUC_TIEP | Nguyễn Văn Alpha | 221 [201] |
| 2 | HD-20260509-002 | Thuế | DVC | Trần Thị Beta | 228 [201] |
| 3 | HD-20260509-003 | Thương mại | CONG_PLQG | Lê Văn Gamma | 235 [201] |
| 4 | HD-20260509-004 | Doanh nghiệp | DVC | Phạm Thị Delta | 241 [201] |
| 5 | HD-20260509-005 | Sở hữu trí tuệ | CONG_PLQG | Hoàng Văn Epsilon | 248 [201] |
| 6 | HD-20260509-006 | Đất đai | HE_THONG_KHAC | Vũ Văn Zeta | 255 [201] |

**Per-filter verify R8 (response API supporting evidence reqid=259, `meta.total=8`):**

| Filter | UI-R7 R8 (count) | OK |
|--------|----:|:--:|
| Tab MOI total | 8 (6 UI-R8 + 2 pre-existing R7) | ✅ |
| LV Lao động | 1 | ✅ |
| LV Thuế | 1 | ✅ |
| LV Thương mại | 1 | ✅ |
| LV Doanh nghiệp | 1 | ✅ |
| LV Sở hữu trí tuệ | 1 | ✅ |
| LV Đất đai | 1 | ✅ |
| Kênh TRUC_TIEP | 1 | ✅ |
| Kênh DVC | 2 | ✅ |
| Kênh CONG_PLQG | 2 | ✅ |
| Kênh HE_THONG_KHAC | 1 | ✅ |

**Ảnh chụp R8:**
- Baseline trước seed: [r7-3-1-ui-baseline-list.png](r7-3-1-ui-baseline-list.png)
- Danh sách sau seed (13 mục TAT_CA): [r7-3-1-ui-list-final-13of13.png](r7-3-1-ui-list-final-13of13.png)
- Tab MOI 8 mục: [r7-3-1-ui-tab-moi-8of8.png](r7-3-1-ui-tab-moi-8of8.png)

**Bug observation R8:** SRS line 1071 ghi `kênh = TVN_BRIDGE` không hiển thị trong dropdown form, nhưng UI Drawer "Kênh tiếp nhận" có option "Từ Tư vấn nhanh" → log riêng (không block task).

---

### R7 (2026-05-06 — API thuần, vi phạm rule UI-only) ⚠️ Method gap

Seed 6 HD entry MOI qua `POST /api/v1/hoi-daps` cover 6 LV × 4 kênh. Verify per-filter PASS lúc đó nhưng **method vi phạm rule UI-only 2026-05-07** → đã re-test bằng UI ở R8 phía trên.

**Bug:** Không.

---

## Bảng dữ liệu seed

| # | Mã HD | Lĩnh vực | Kênh | DN gắn | Tiêu đề | Có vào kho? |
|---|-------|----------|------|--------|---------|:-----------:|
| 1 | HD-20260506-001 | Lao động | Trực tiếp | DN000001 | Hỏi về thời gian nghỉ phép năm | ✅ |
| 2 | HD-20260506-002 | Thuế | Dịch vụ công | DN000002 | Hoàn thuế GTGT đầu vào hàng nhập khẩu | ✅ |
| 3 | HD-20260506-003 | Kinh doanh thương mại | Cổng PLQG | DN000003 | Thời hạn HĐ lao động xác định thời hạn | ✅ |
| 4 | HD-20260506-004 | Doanh nghiệp | Dịch vụ công | DN000004 | Thủ tục tăng vốn điều lệ TNHH 2TV | ✅ |
| 5 | HD-20260506-005 | Sở hữu trí tuệ | Cổng PLQG | DN000005 | Đăng ký bảo hộ nhãn hiệu sản phẩm mới | ✅ |
| 6 | HD-20260506-006 | Đất đai | Hệ thống khác | DN000006 | Thế chấp đất KCN trả tiền hàng năm | ✅ |

**Tổng:** 6 vào kho / 0 chặn

### Per-filter verify

| Filter | Total | OK |
|--------|------:|:--:|
| Total state MOI | 6 | ✅ |
| LV LAO_DONG | 1 | ✅ |
| LV THUE | 1 | ✅ |
| LV KINH_DOANH_TM | 1 | ✅ |
| LV DOANH_NGHIEP | 1 | ✅ |
| LV SO_HUU_TRI_TUE | 1 | ✅ |
| LV DAT_DAI | 1 | ✅ |
| Kênh TRUC_TIEP | 1 | ✅ |
| Kênh DVC | 2 | ✅ |
| Kênh CONG_PLQG | 2 | ✅ |
| Kênh HE_THONG_KHAC | 1 | ✅ |

---

## Ảnh chụp

- [Danh sách 6 HD MOI sau seed](../screenshots/r7-3-1-hd-6of6-moi.png)

---

*2026-05-06 14:47 — QA chạy bằng Chrome DevTools MCP via API POST /api/v1/hoi-daps*
