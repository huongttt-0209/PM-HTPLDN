# Seed Checklist — Đánh giá Hiệu quả HTPLDN (R7.4.D1)

**Ngày:** 2026-05-09 18:41 • **Tài khoản:** `cb_nv_tw_03` • **Trạng thái mong đợi:** `Lập kế hoạch` (LAP_KE_HOACH)
**Màn:** SCR-VI-01 — Kế hoạch Đánh giá • **Đường dẫn:** `/danh-gia/ke-hoach/danh-sach`
**Dữ liệu mẫu:** Runtime QA seed bằng bộ tài khoản 03, tham chiếu pattern [seed-fixture.yaml > danh_gia_hq_variants](../../../../input/data/seed-fixture.yaml)
**SRS:** [FR-VI-01 UC83 — Lập kế hoạch đánh giá](../../../../input/srs-v3/srs-fr-08-danh-gia.md) + SCR-VI-01 button `Lưu & Chuyển tiêu chí`
**Template sử dụng:** [seed-checklist-template.md](../../../../template/seed-checklist-template.md)
**Folder lưu:** `output/qa-reports/round7-2026-05-06/seed/danh-gia/`

---

## Downstream consumer × filter (BẮT BUỘC trước khi seed)

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query (curl/UI) | Status |
|-----------------|------------------------|---------------|----------------------|------------------------|:---:|
| R7.4.D2 Workflow ĐG | `trang_thai = LAP_KE_HOACH` (`srs-fr-08` SM-DANHGIA `[*] → LAP_KE_HOACH`) | ≥1 đợt | LAP_KE_HOACH | `GET /api/v1/ke-hoach-danh-gias?keyword=QA+R7.4.D1+bo+03+202605091141&page=1&pageSize=20` → `meta.total = 1 ∧ data[0].trangThai = "LAP_KE_HOACH"` | ✅ |
| R7.7.9 Functional ĐG HQ | id đợt + state active | ≥1 đợt | LAP_KE_HOACH | UI `/danh-gia/ke-hoach/danh-sach` search exact tên đợt → 1 record `DG-20260509-0001`, badge `Lập kế hoạch` | ✅ |

**Acceptance pass khi:** verify query trả đúng 1 đợt state `LAP_KE_HOACH`, UI list tìm thấy record, detail page mở được, tab `Tiêu chí` active sau submit `Lưu & Chuyển tiêu chí`.

---

## Kết quả: ✅ XONG 1/1

Tạo 1 đợt `DG-20260509-0001` state `Lập kế hoạch` qua flow `cb_nv_tw_03` → SCR-VI-01 → modal `Tạo kế hoạch đánh giá` → click `Lưu & Chuyển tiêu chí` → `POST /api/v1/ke-hoach-danh-gias` 201 → navigate detail tab `Tiêu chí`.

**Bug:** không log bug mới. 1 observation cũ vẫn tái hiện: timezone offset ngày BĐ/KT lệch -1 ngày sau save.

---

## Bảng dữ liệu seed

| # | Tên đợt | Tần suất | Đối tượng | Từ ngày → Đến ngày | Mã đợt (auto) | UUID | Trạng thái | Có vào kho? |
|---|---------|----------|-----------|---------------------|---------------|------|------------|:-----------:|
| 1 | `QA R7.4.D1 bo 03 202605091141` | Sơ bộ 6 tháng (`SO_BO_6_THANG`) | Vụ việc (`VU_VIEC`) | input `01/04/2026 → 30/06/2026` · display/API `31/03/2026 → 29/06/2026` | `DG-20260509-0001` | `c521f1f1-82b2-424a-a14c-6d01e91ce540` | Lập kế hoạch (`LAP_KE_HOACH`) | ✅ |

**Tổng:** 1/1 vào kho.

**Form input thực tế:**
- Tên đợt đánh giá: `QA R7.4.D1 bo 03 202605091141`
- Mục tiêu: `QA report-only R7.4.D1 bằng bộ tài khoản 03. Kiểm tra tạo kỳ Đánh giá Hiệu quả HTPL trạng thái LAP_KE_HOACH và chuyển sang tab Tiêu chí.`
- Tần suất: `Sơ bộ 6 tháng`
- Đối tượng: `Vụ việc`
- Thời gian bắt đầu: `01/04/2026`
- Thời gian kết thúc: `30/06/2026`
- Ghi chú: `QA-only R7.4.D1, account cb_nv_tw_03.`

**API verify:**
```text
POST /api/v1/ke-hoach-danh-gias [201 Created]
GET  /api/v1/ke-hoach-danh-gias/c521f1f1-82b2-424a-a14c-6d01e91ce540 [200]
GET  /api/v1/ke-hoach-danh-gias/c521f1f1-82b2-424a-a14c-6d01e91ce540/tieu-chis [200]
GET  /api/v1/ke-hoach-danh-gias?keyword=QA+R7.4.D1+bo+03+202605091141&page=1&pageSize=20 [200]
```

Detail API:
```json
{
  "maKeHoach": "DG-20260509-0001",
  "tenDot": "QA R7.4.D1 bo 03 202605091141",
  "trangThai": "LAP_KE_HOACH",
  "tanSuat": "SO_BO_6_THANG",
  "doiTuong": "VU_VIEC",
  "thoiGianBatDau": "2026-03-31",
  "thoiGianKetThuc": "2026-06-29"
}
```

Detail page render:
- Mã: `DG-20260509-0001`
- Trạng thái: `Lập kế hoạch`
- Stepper: `1 Lập kế hoạch` active → `2 Phân công` → `3 Chờ duyệt PC` → ... → `9 Hoàn thành`
- Tabs: `Tiêu chí` active / `Phân công` / `Thực hiện` / `Chấm điểm` / `Báo cáo`
- Tab `Tiêu chí`: `Thêm tiêu chí`, `Nhập từ danh mục`, `Lưu thay đổi`, table header `STT/Tên tiêu chí/Nhóm tiêu chí/Trọng số (%)/Điểm tối đa/Trạng thái/Thao tác`

---

## Observations (không log thành bug)

### OBS-D1-BO03-001 — Timezone offset ngày BĐ/KT vẫn tái hiện

App nhận input `01/04/2026 → 30/06/2026`, nhưng sau save:

- UI detail/list: `31/03/2026 → 29/06/2026`
- API detail: `thoiGianBatDau = 2026-03-31`, `thoiGianKetThuc = 2026-06-29`

Không block acceptance seed-create vì record vào kho đúng state `LAP_KE_HOACH`, nhưng đây là risk cho downstream filter theo kỳ đánh giá.

### OBS-D1-BO03-002 — Console noise trong login

Login page có `GET /api/v1/auth/me` 401 trước khi xác thực và warning AntD `maskClosable` deprecated. Không có lỗi user-facing trong flow seed.

---

## Ảnh chụp

- [Login page](r74d1-login.png)
- [OTP screen sau login `cb_nv_tw_03`](r74d1-after-login-click.png)
- [Dashboard sau OTP](r74d1-dashboard.png)
- [List rỗng trước khi tạo seed](r74d1-01-list-empty-before-create.png)
- [Form tạo kế hoạch đã điền dữ liệu](r74d1-02-create-form-filled.png)
- [Detail page sau save — `DG-20260509-0001`, state `Lập kế hoạch`, tab `Tiêu chí` active](r74d1-03-after-save-detail.png)
- [List search exact tên đợt — 1 record `DG-20260509-0001`](r74d1-04-list-search-created.png)

---

## Phụ lục

- Raw run result: [r7-4-d1-bo03-run-result.json](r7-4-d1-bo03-run-result.json)
- QA generic report phụ: [qa-report-r7-4-d1-danhgiahq-bo03-2026-05-09.md](qa-report-r7-4-d1-danhgiahq-bo03-2026-05-09.md)
- Baseline phụ: [baseline-r7-4-d1-danhgiahq-bo03-2026-05-09.json](baseline-r7-4-d1-danhgiahq-bo03-2026-05-09.json)

---

*2026-05-09 18:41 — QA chạy bằng Playwright headless fallback do gstack browse binary exited 137/-1 trong session này*
