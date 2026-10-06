# Hướng dẫn kiểm tra 1 bug đang Open — R26 reverify

**Ngày:** 2026-05-18 14:35:00
**Mục đích:** Hướng dẫn người dùng cuối kiểm tra lại bug còn Open trên web không cần thao tác kỹ thuật.

**Thông tin chung:**
- URL: http://103.172.236.130:3000/
- OTP login: gõ `666666` (dev bypass)
- File bug-report gốc nằm trong `bug-reports/vu-viec/`

> **R26 update 2026-05-18 14:35:00:** Sau R26 verify, **1 bug nữa đã đóng** (BUG-VV-FN-LICHSU-01 — FE FIX option (b) derive label theo `duLieuMoi.trangThai`, xem mục cuối) → còn lại **1 bug Open**: BUG-VV-PC-WRN-01.
>
> **R25 history:** R25 đóng BUG-FUNC-DG-013 (Đánh giá HQ — cả BE + FE align spec).

---

## Bug 1 — BUG-VV-PC-WRN-01

### Thông tin nhanh

| Trường | Giá trị |
|---|---|
| Module | **Quản lý Vụ việc HTPL** |
| Màn hình | Detail vụ việc → Modal **"Phân công tư vấn viên"** |
| Severity | **Minor P2** |
| Trạng thái | Open — chờ dev quyết cách cho phép tìm TVV ngoài lĩnh vực |
| R26 verify | 2026-05-18 14:35:00 — re-confirm Open unchanged R25→R26, BE+FE chưa fix |

### Bug là gì (dễ hiểu)

- Cán bộ nghiệp vụ tạo 1 vụ việc thuộc lĩnh vực **"Doanh nghiệp"** → bấm Phân công → tìm tư vấn viên.
- Hệ thống chỉ hiện TVV có lĩnh vực **"Doanh nghiệp"**.
- Nếu không có TVV nào phù hợp, web hiện popup **"Liên hệ QTHT để mở rộng lĩnh vực TVV/NHT, hoặc chọn vụ việc khác"** → cán bộ bị kẹt.
- Spec yêu cầu cho cán bộ một **cách để tìm tư vấn viên thuộc lĩnh vực khác** (vd nút "Tìm thủ công", hoặc bỏ filter lĩnh vực).
- Hiện tại web không có nút nào để vượt qua tình huống này → vụ việc đó không phân công được.

### Cách kiểm tra trên web

**Account cần dùng:** `cb_nv_tw_01` / `Secret@123` (cán bộ Trung ương — có quyền phân công).

1. Login `cb_nv_tw_01` + OTP `666666`.
2. Sidebar → **"Quản lý vụ việc HTPL"** → danh sách vụ việc.
3. Tìm 1 vụ việc thuộc lĩnh vực **"Doanh nghiệp"** state **"Đang kiểm tra"** (vd `VV-QA-R7-PRIVACY-DNAG002`). Nếu không có, dùng cách dưới đây tạo mới:
   - Click **[Tạo vụ việc mới]** → fill: Doanh nghiệp = bất kỳ, Lĩnh vực = **Doanh nghiệp**, Loại hình = Tư vấn pháp luật → Lưu.
   - Mở detail vụ việc vừa tạo → click **[Kiểm tra hồ sơ]** → **[Xác nhận]** (state chuyển sang "Đang kiểm tra").
4. Click nút **[Phân công]** ở thanh action bar → modal "Phân công tư vấn viên" mở.
5. Click dropdown **"Chọn người được phân công"** → quan sát danh sách.
6. Gõ vào ô search trong dropdown: `XXKHONGMATCH99` (chuỗi bừa để force empty).

### Kết quả thấy được (R26 2026-05-18)

- Modal có: radio **Cá nhân**/**Tổ chức tư vấn** + 1 dropdown chọn người + 1 ô **Ghi chú** + 2 nút **[Hủy]** / **[Xác nhận]**.
- Empty state hiện text: **"Trống / Không tìm thấy đối tượng phù hợp lĩnh vực / Liên hệ QTHT để mở rộng lĩnh vực TVV/NHT, hoặc chọn vụ việc khác."**.
- ❌ **KHÔNG có nút [Tìm thủ công]** hoặc nút bỏ filter lĩnh vực.
- ❌ Gõ tên TVV thật ở lĩnh vực khác (vd `hương`) → vẫn 0 kết quả (dù TVV "hương tvv1" tồn tại trong hệ thống).

### Khi nào coi là FIXED

- Modal phân công có thêm 1 trong các cơ chế: nút **[Tìm thủ công]**, hoặc **toggle bỏ filter lĩnh vực**, hoặc **dropdown thứ 2 không lọc lĩnh vực**.
- Cán bộ chọn được TVV thuộc lĩnh vực khác.

---

## Tóm tắt 1 bug Open còn lại

| Bug | Module | Màn hình | Account | Bước nhanh |
|---|---|---|---|---|
| BUG-VV-PC-WRN-01 | Vụ việc | Modal Phân công TVV | `cb_nv_tw_01` | Mở VV LV Doanh nghiệp → Phân công → search bừa → xem có nút override không |

**Bug Minor**, không block nghiệp vụ chính — chỉ là UX. Dev fix xong sẽ retest.

---

## Bug đã đóng R26 (tham khảo)

### ~~BUG-VV-FN-LICHSU-01~~ — Đã đóng 2026-05-18 R26 ✅

| Trường | Giá trị |
|---|---|
| Module | **Quản lý Vụ việc HTPL** |
| Severity gốc | Minor P3 |
| Trạng thái | ✅ **Closed-verified** |
| R26 verify | 2026-05-18 14:35:00 — FE đã FIX option (b) |

**R26 fresh probe** (`cb_nv_tw_01`):
- Vụ việc MỚI `VV-BTP-TW-20260514-001` (`4a1a6889-...`): timeline render "Yêu cầu bổ sung" + "Tạo vụ việc" ✓ (giữ vững từ R24).
- Vụ việc CŨ `VV-002` (`33b5a612-...`): API vẫn trả `[UPDATE, UPDATE, CREATE]` 3 entries (BE chưa migrate) NHƯNG **UI NAY render đủ 3 entries** label tiếng Việt: **"Yêu cầu bổ sung" + "Kiểm tra" + "Tạo mới"** — FE đã thêm fallback derive label theo `duLieuMoi.trangThai` cho enum UPDATE.
- Cả 2 path (fresh + legacy) PASS. Người xem timeline VV cũ NAY thấy đủ các bước chuyển trạng thái.

Bug đóng hoàn toàn — file bug-report đã rename `Pass-bug-report-r7-7-3-functional-vu-viec.md`.

---

## Bug đã đóng R25 (tham khảo)

### ~~BUG-FUNC-DG-013~~ — Đã đóng 2026-05-16 R25 ✅

| Trường | Giá trị |
|---|---|
| Module | **Đánh giá hiệu quả HTPL** |
| Severity gốc | Minor P3 (đã downgrade từ Major P1) |
| Trạng thái | ✅ **Closed-verified** |
| R25 verify | 2026-05-16 10:15:00 — cả BE + FE đã align spec |

**R25 fresh probe** (`cb_nv_dp_02` STP-BG, cross-cơ quan, KH `440b6dd1-...` của STP-AG):
- API 3/3 endpoint `/ke-hoach-danh-gias/{id}` + `/bao-cao` + `/ket-quas` đều trả `HTTP 403 + ERR-DG-10 + message: "Bạn không có quyền xem kết quả đánh giá này"` đúng nguyên văn spec.
- FE auto-redirect `/403` render đúng câu **"Bạn không có quyền xem kết quả đánh giá này"** + **"Mã lỗi: ERR-DG-10"** + "Vai trò hiện tại: CB_NV_DP". KHÔNG còn câu generic "Bạn không có quyền truy cập trang này".

Bug đóng hoàn toàn — file bug-report đã rename `Pass-bug-report-r22-fr-vi-10.md`.
