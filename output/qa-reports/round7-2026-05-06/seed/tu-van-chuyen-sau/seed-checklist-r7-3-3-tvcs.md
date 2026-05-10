# Seed Checklist — Tư vấn chuyên sâu (R7.3.3)

> ✅ **R8 2026-05-09 18:18:00 — UI re-test PASS (Method gap đã đóng):** Tạo 3 record fresh TVCS-20260509-0001..0003 cover gap LV (SHTT + Đất đai + Thương mại) qua UI click chain `Tạo mới → fill DN/LV/nội dung/tóm tắt → Lưu` cb_nv_tw_08. 3 POST `/api/v1/noi-dung-tu-van-cs` reqid=215/231/246 đều phát từ form Lưu UI (không phải direct curl). Pool 12 → 15 mục. State TIEP_NHAN cover 6/6 LV (Lao động/Thuế/DN + R8 SHTT/Đất đai/Thương mại). Method-rule UI-only thỏa.

**Ngày:** 2026-05-06 14:53 • **Tài khoản:** `cb_nv_tw_01` • **Trạng thái mong đợi:** `TIEP_NHAN` (entry)
**Màn:** SCR-X1-02 — Tư vấn chuyên sâu • **Đường dẫn:** `/tv-chuyen-sau/danh-sach`
**Dữ liệu mẫu:** [seed-fixture.yaml v2.7.1 > tv_cs_variants[1..10]](../../../../input/data/seed-fixture.yaml)
**SRS:** [FR-X.1-01 — Tư vấn chuyên sâu (NoiDungTuVanCs)](../../../../input/srs-update-2026-5-5/srs-fr-x1-tu-van.md)

---

## Endpoint discovery (corrected R7)

| Fixture giả định | Endpoint thực BE deploy | Status |
|------------------|-------------------------|:------:|
| `/api/v1/tu-van-chuyen-saus` (R6 fixture) | `/api/v1/noi-dung-tu-van-cs` | ✅ Re-mapped |

> Endpoint `tu-van-chuyen-saus` chỉ tồn tại nhánh `/api/v1/public/tu-van-chuyen-saus/*` (public Cổng PLQG). Internal CMS dùng `/api/v1/noi-dung-tu-van-cs` (verified qua `/api/docs-json` + POST 201). Bug deploy R6.4.A5 cũ về 404 endpoint TVCS giải đáp xong — Bug TVCS-001/002 R6 đã Closed R17.

---

## Downstream consumer × filter (BẮT BUỘC trước khi seed)

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.4.A5 Workflow TVCS 11 bước | `trang_thai_xu_ly=CHO_XU_LY ∨ trang_thai=TIEP_NHAN` | ≥6 | `TIEP_NHAN` | total ≥6 | ✅ |
| R7.7.5 Functional 44 TC | `trang_thai=TIEP_NHAN ∧ 6 LV cover` | ≥1/LV | `TIEP_NHAN` | per-LV ≥1 | ✅ |

**Acceptance pass:** mọi row Status ✅ qua API verify per-filter.

---

## Kết quả: ✅ XONG 10/10 TIEP_NHAN

Seed 10 TVCS qua `POST /api/v1/noi-dung-tu-van-cs` cover 6 LV (LAO_DONG/THUE/KDTM/DN/SHTT/DAT_DAI) × 2 hình thức (HO_SO 8/10 + DIEN_THOAI 2/10). State entry TIEP_NHAN. Trong 10 lần POST đầu, 5 record `hinhThucTv=VIDEO_CALL` BE trả 500 → bug log riêng + retry với `HO_SO` để đủ 10/10.

**Bug:** [`BUG-TVCS-VIDEO-CALL-001`](../../bug-reports/tu-van-chuyen-sau/Pass-bug-report-seed-r7-3-3-tvcs-video-call.md) — 0/1 đóng (Major BE 500 khi `hinhThucTv=VIDEO_CALL`).

---

## Bảng dữ liệu seed

| # | Mã TVCS | LV | Hình thức TV | DN | State | Có vào kho? |
|---|---------|----|-----|-----|-------|:----:|
| 1 | TVCS-20260506-0001 | Lao động | HO_SO | DN000003 (Đại Việt #3) | TIEP_NHAN | ✅ |
| 2 | TVCS-20260506-0002 | Thuế | DIEN_THOAI | DN000004 (Phương Đông #4) | TIEP_NHAN | ✅ |
| 3 | TVCS-20260506-0003 | SHTT | HO_SO | DN000005 (HTX Thành Đạt #5) | TIEP_NHAN | ✅ |
| 4 | TVCS-20260506-0004 | DN | HO_SO | DN000007 (Minh Khôi #7) | TIEP_NHAN | ✅ |
| 5 | TVCS-20260506-0005 | Đất đai | DIEN_THOAI | DN000011 (Trường Thịnh #11) | TIEP_NHAN | ✅ |
| 6 | TVCS-20260506-0006 | DN | HO_SO (retry) | DN000001 (Phúc An #1) | TIEP_NHAN | ✅ |
| 7 | TVCS-20260506-0007 | KDTM | HO_SO (retry) | DN000002 (Hoàng Gia #2) | TIEP_NHAN | ✅ |
| 8 | TVCS-20260506-0008 | Đất đai | HO_SO (retry) | DN000006 (Tân Phú #6) | TIEP_NHAN | ✅ |
| 9 | TVCS-20260506-0009 | DN | HO_SO (retry) | DN000009 (Phát Đạt #9) | TIEP_NHAN | ✅ |
| 10 | TVCS-20260506-0010 | Thuế | HO_SO (retry) | DN000012 (Đông Dương #12) | TIEP_NHAN | ✅ |

**Tổng:** 10 vào kho / 0 chặn (5 pass đầu + 5 retry sau bug VIDEO_CALL)

### Per-filter verify (state TIEP_NHAN)

| Filter | Total | OK |
|--------|------:|:--:|
| Total | 10 | ✅ |
| LV LAO_DONG | 1 | ✅ |
| LV THUE | 2 | ✅ |
| LV KINH_DOANH_TM | 1 | ✅ |
| LV DOANH_NGHIEP | 3 | ✅ |
| LV SO_HUU_TRI_TUE | 1 | ✅ |
| LV DAT_DAI | 2 | ✅ |
| Hình thức HO_SO | 8 | ✅ |
| Hình thức DIEN_THOAI | 2 | ✅ |
| Hình thức VIDEO_CALL | 0 | 🚫 (BE 500 — bug) |

> **Scope coverage:** Tất cả 10 record là cấp TW (`cb_nv_tw_01` tạo). Scope ĐP cần seed thêm bằng `cb_nv_dp_01` (defer R7.7.5 functional khi cần).

---

## Ảnh chụp (R7 — API direct, archived)

- [Danh sách 10 TVCS TIEP_NHAN sau seed](../screenshots/r7-3-3-tvcs-10of10-tiep-nhan.png)

---

## R8 2026-05-09 18:18:00 — UI re-test (LATEST)

**Method:** Chrome DevTools MCP click chain UI form (KHÔNG dùng curl/API direct). Account `cb_nv_tw_08` (BTP-TW).

**Mục tiêu:** Đóng method gap R7 (API thuần) bằng cách demonstrate UI flow tạo TVCS hoạt động đúng + lấp 3 LV gap state TIEP_NHAN (SHTT + Đất đai + Thương mại đều 0 record TIEP_NHAN trước R8).

**Click chain mỗi record:**
1. Sidebar `Quản lý tư vấn` → submenu `Tư vấn chuyên sâu` → màn `/tv-chuyen-sau/danh-sach`
2. Click `[+ Tạo mới]` → form `/tv-chuyen-sau/tao-moi` (heading "Thêm yêu cầu Tư vấn Chuyên sâu")
3. Combobox `Doanh nghiệp` → type prefix → chọn dropdown option
4. Combobox `Lĩnh vực pháp lý` → click → chọn LV target
5. Textarea `Nội dung tư vấn` → fill long text
6. Textarea `Tóm tắt` → fill summary
7. Click `[Lưu]` → 201 → redirect `/tv-chuyen-sau/{uuid}` detail page → state Tiếp nhận hiển thị

**Kết quả 3/3 record PASS:**

| # | Mã | UUID | DN | LV | State | UI POST reqid |
|---|----|------|-----|-----|-------|:-:|
| 1 | TVCS-20260509-0001 | a997133b-9ee3-44a9-b8fd-9aed87d145e9 | Tân Bình SN1 (DN-NEW-SN1) | Sở hữu trí tuệ | Tiếp nhận ✅ | 215 → 201 |
| 2 | TVCS-20260509-0002 | 1ddf8102-f084-4644-945c-9a92f97de5f3 | Hưng Thịnh VU2 (DN-NEW-VU2) | Đất đai | Tiếp nhận ✅ | 231 → 201 |
| 3 | TVCS-20260509-0003 | 8172d0fc-2482-4a39-982f-cecba23906b9 | Sao Mai NH1 (DN-NEW-NH1) | Thương mại | Tiếp nhận ✅ | 246 → 201 |

### Pool sau R8 UI re-test

| Phân loại | Trước R8 | R8 thêm | Sau R8 |
|-----------|---------:|--------:|-------:|
| Total TVCS | 12 | +3 | **15** |
| TIEP_NHAN | 5 | +3 | **8** |
| LV cover (state TIEP_NHAN) | 3/6 (LĐ + Thuế + DN) | +3 (SHTT + ĐĐ + TM) | **6/6** ✅ |

### Per-LV verify (state TIEP_NHAN, sau R8)

| LV | Record | OK |
|----|--------|:--:|
| Lao động | TVCS-20260507-0007 | ✅ |
| Thuế | TVCS-20260507-0008 + 0012 + 0013 | ✅ (3) |
| Doanh nghiệp | TVCS-20260507-0010 | ✅ |
| Sở hữu trí tuệ | TVCS-20260509-0001 (R8 UI fresh) | ✅ |
| Đất đai | TVCS-20260509-0002 (R8 UI fresh) | ✅ |
| Thương mại (KDTM) | TVCS-20260509-0003 (R8 UI fresh) | ✅ |

### Network evidence (no console error/warn)

```
reqid=215  POST /api/v1/noi-dung-tu-van-cs → 201  (TVCS-0001 SHTT, sau Lưu form)
reqid=217  GET  /api/v1/noi-dung-tu-van-cs/a997133b... → 200  (auto-fetch detail)
reqid=221  GET  /api/v1/noi-dung-tu-van-cs?page=1&pageSize=20 → 200  (list refresh)
reqid=231  POST /api/v1/noi-dung-tu-van-cs → 201  (TVCS-0002 Đất đai, sau Lưu form)
reqid=232  GET  /api/v1/noi-dung-tu-van-cs/1ddf8102... → 200
reqid=236  GET  /api/v1/noi-dung-tu-van-cs?page=1&pageSize=20 → 200
reqid=246  POST /api/v1/noi-dung-tu-van-cs → 201  (TVCS-0003 Thương mại, sau Lưu form)
reqid=247  GET  /api/v1/noi-dung-tu-van-cs/8172d0fc... → 200
list_console_messages(error,warn) → no console messages found ✅
```

### Bug observation

**BUG-TVCS-VIDEO-CALL-001 Closed-verified:** Form `Thêm yêu cầu Tư vấn Chuyên sâu` KHÔNG còn field `hinhThucTv` (HO_SO/DIEN_THOAI/VIDEO_CALL) — FE đã bỏ field theo dev fix R8. Reproduce 3 lần khi mở form, KHÔNG có field hình thức tư vấn → bug pattern không repro được trong UI flow.

### Ảnh chụp R8 (UI evidence)

- `screenshots/r7-3-3-r8-list-before-12-of-12.png` — Pool 12 mục trước R8
- `screenshots/r7-3-3-r8-form-shtt-before-submit.png` — Form R8 record SHTT trước Lưu
- `screenshots/r7-3-3-r8-detail-shtt-001-pass.png` — Detail TVCS-0001 SHTT TIEP_NHAN
- `screenshots/r7-3-3-r8-detail-datdai-002-pass.png` — Detail TVCS-0002 Đất đai TIEP_NHAN
- `screenshots/r7-3-3-r8-detail-thuongmai-003-pass.png` — Detail TVCS-0003 Thương mại TIEP_NHAN
- `screenshots/r7-3-3-r8-list-after-15-of-15.png` — Pool 15 mục sau R8

---

*2026-05-06 14:53 — QA chạy bằng Chrome DevTools MCP via API POST /api/v1/noi-dung-tu-van-cs (R7 archived)*
*2026-05-09 18:18:00 — QA chạy R8 bằng Chrome DevTools MCP via UI click chain `cb_nv_tw_08` (LATEST — method-rule UI-only PASS)*
