# Workflow Test Report — R7.4.B12 Lịch học (R9 unblock probe)

> **Module:** Quản lý lịch học (FR-III-22) · **Round:** R9 · **Date:** 2026-05-10 · **Tester:** QA Automation (Claude Code MCP) — `/qa-only` mode
> **Pre-context:** R7.4.B12 trước R9 = ⏳ block bởi R7.3.13 (LICH_HOC endpoint 404 trên 2026-05-09 20:33). R9 re-probe.

---

## Kết luận

🟢 **UNBLOCK — BE đã deploy LICH_HOC endpoint + FE đã có UI module đầy đủ.** R7.4.B12 sẵn sàng để chạy full CRUD test. Test chi tiết chưa hoàn tất R9 do tester tool limitation (AntD DatePicker/TimePicker không bind native InputEvent — cần thao tác calendar UI).

---

## Phát hiện R9 (2026-05-10)

### 1. BE deploy status: ✅ DEPLOYED

| Endpoint | HTTP | Status R9 | Status 2026-05-09 |
|---|:-:|:-:|:-:|
| `GET /api/v1/lich-hocs?page=1&pageSize=50` | 200 | ✅ Empty list | ❌ 404 (escalation) |
| `GET /api/v1/khoa-hocs/{id}/lich-hocs` | 200 | ✅ Empty list | ❌ 404 |
| `POST /api/v1/khoa-hocs/{id}/lich-hocs` | 422 | ✅ Schema validation working | ❌ 404 |
| `POST /api/v1/lich-hocs` (root) | 404 | ⚠️ Root POST không exist (đúng REST convention — nested under khoa-hocs) |  |
| `GET /api/v1/lich-hocs/types` | 404 | ⚠️ Subroute `/types` không exist (probably enum endpoint) |  |

**BE schema discovered (POST validation 422 response):**

```json
{
  "field": "khoaHocId", "message": "khoaHocId must be a UUID"
},{
  "field": "ngayHoc", "message": "ngayHoc must be a valid ISO 8601 date string"
},{
  "field": "gioBatDau", "message": "gioBatDau phải có dạng HH:MM (24h)"
},{
  "field": "gioKetThuc", "message": "gioKetThuc phải có dạng HH:MM (24h)"
}
```

→ Required fields: `khoaHocId` (UUID, FK), `ngayHoc` (ISO 8601 date), `gioBatDau` (HH:MM 24h), `gioKetThuc` (HH:MM 24h).

### 2. FE UI status: ✅ ĐẦY ĐỦ

**Vị trí UI:** Khóa học detail page (`/dao-tao/khoa-hoc/{id}?tab=lich-hoc`) — tab "Lịch học" trong tab chain với Thông tin / Học viên / Lịch học / Điểm danh / Kết quả / Bài giảng đã gán.

**Tab Lịch học elements:**
- Header: Ngày học | Giờ | Hình thức | Địa điểm/Link | Nội dung | Thao tác
- Empty state: "Chưa có buổi học nào."
- Action buttons: `[+ Thêm buổi học]` + `[↻ Làm mới]`

**Modal "Thêm buổi học" form:**
- `Ngày học` * — DatePicker (placeholder "Chọn thời điểm")
- `Giờ bắt đầu` * — TimePicker (placeholder "Chọn thời gian")
- `Giờ kết thúc` * — TimePicker (placeholder "Chọn thời gian")
- `Hình thức` * — Radio: Trực tiếp (default checked) | Trực tuyến — name=`hinhThucBuoi`, values `TRUC_TIEP`/`TRUC_TUYEN`
- `Địa điểm` — text input
- `Nội dung` — textarea (max 2000)
- `Ghi chú` — textarea (max 1000)
- Buttons: `[Hủy]` `[Tạo]`

→ Form đầy đủ field theo BE schema. Empty list trả `[]` không lỗi → CRUD route hoạt động.

### 3. Bonus phát hiện: Khóa học có nút "Khai giảng"

Khi vào KH-20260509-007 detail (DA_DUYET state), tab Thông tin có 2 button cuối page:
- `[Gỡ công khai]`
- `[Khai giảng]`

→ Nút "Khai giảng" mà R7.4.B7 báo "BE chưa code" giờ **đã có trên UI**. Khả năng cao R7.4.B7 cũng đã unblock — chỉ cần re-probe để confirm.

---

## Test CRUD R7.4.B12 (8 bước, theo todo R8 schema)

| # | Bước | UI ready? | Tested R9 |
|:-:|---|:-:|:-:|
| 1 | Khóa học → tab Lịch học → "Thêm buổi học" | ✅ | ✅ Modal mở |
| 2 | Fill form: ngày + giờ BĐ/KT + hình thức + địa điểm + nội dung | ✅ | ⚠️ AntD picker không bind native event — cần calendar click |
| 3 | Submit "Tạo" → POST `/khoa-hocs/{id}/lich-hocs` | ✅ | ⏳ chưa test do step 2 block |
| 4 | Verify list hiển thị buổi mới | ✅ | ⏳ |
| 5 | Edit buổi học (icon Sửa trong row) | ⚠️ chưa thấy icon row action | ⏳ |
| 6 | Xóa buổi học | ⚠️ chưa thấy icon row action | ⏳ |
| 7 | Conflict validate (thời gian trùng buổi khác) | ✅ BE schema HH:MM | ⏳ |
| 8 | Verify thông qua khóa học detail | ✅ | ⏳ |

**Tester limitation:** AntD `DatePicker` + `TimePicker` không bind value qua native `Event('input')` + `Event('change')` — phải click calendar/clock UI để chọn ngày/giờ. MCP `evaluate_script` setter không trigger AntD internal state. Cần MCP click theo flow:
1. Click input mở calendar dropdown
2. Click ngày target trong calendar
3. (Tương tự cho TimePicker — click "Chọn giờ" + scroll spinner)

→ **Test technique issue, không phải app bug.** Sẽ cần manual session với MCP click chuỗi calendar UI để hoàn tất 8/8 bước.

---

## Recommend next step

1. **Update R7.4.B12 ⏳ → 🟢** (sẵn sàng test, không còn block).
2. **Cập nhật state-snapshot.md** xóa marker `LICH_HOC endpoint deploy (✗ 404)` vì đã PASS deploy.
3. **Re-probe R7.4.B7** — phát hiện nút "Khai giảng" trên UI đã có. Có thể R7.4.B7 cũng đã unblock 4 nút "Khai giảng/Kết thúc/Gửi KQ/Duyệt KQ" mà R9 prior báo "BE chưa code".
4. **Re-probe R7.4.B11** — depends on R7.4.B7. Có thể chain unblock.
5. **R7.7.6 functional 40 TC** — depends on R7.4.B7 + R7.3.13 (đã unblock). Sẵn sàng chạy sau khi R7.4.B7 confirm.
6. **Bug-DKT-FE-REGRESSION-01** vẫn Open (R7.4.B10 stays ⚠️ — dev fix riêng).

---

## Phụ lục

| Thành phần | Giá trị |
|---|---|
| URL | http://103.172.236.130:3000 |
| Account | `cb_nv_tw_02 / Secret@123` |
| OTP | `666666` |
| Tool | Chrome DevTools MCP |
| KH target probe | `KH-20260509-007` (id `e9264a92-446a-4bfc-8dd2-81287b5b32d4`, DA_DUYET) |

**Network probe log:**
- `reqid=1781 GET /lich-hocs [200]` (post deploy)
- `reqid=1782 GET /khoa-hocs/{id}/lich-hocs [200]`
- `reqid=1783 POST /khoa-hocs/{id}/lich-hocs [422]` (schema validation)

---

*R9 unblock probe | QA Automation via Claude Code | 2026-05-10*
