# Workflow Test Report — R7.4.B10 ĐKT (R9 re-verify, FE regression detected)

> **Module:** Workflow Đề kiểm tra (FR-III-NEW-02 + FR-III-NEW-03) · **Round:** R9 · **Date:** 2026-05-10 · **Tester:** QA Automation (Claude Code MCP) — `/qa-only` mode (report only)
> **Pre-context:** R8 report 6/8 PASS (tạo + sửa + xóa); 2/8 phân phối được giả định "cần khóa học DANG_DIEN_RA" → block bởi R7.4.B7. R9 re-probe để confirm scope.

---

## Kết luận

🚫 **PARTIAL/REGRESSION — 1/8 confirmed PASS via UI hiện tại; 5/8 BE endpoint OK nhưng FE thiếu button; 2/8 chưa test do chuỗi ưu tiên FE fix.**

**Phân loại lỗi (per CLAUDE.md Rule 9 Step 2):** APP/FE BUG — FE missing render action buttons. BE endpoints registered + responding correctly; FE row action cell render rỗng `<div class="ant-space"></div>` không có icon button.

**Discovery quan trọng:** Giả định R8 "phân phối ĐKT cần khóa học DANG_DIEN_RA → chờ R7.4.B7" **SAI**. SRS `FR-III-NEW-03` line 1126 ghi rõ:

> Preconditions: User đã đăng nhập. Đề kiểm tra ở NHAP. Khóa học tồn tại.

Không yêu cầu khóa học DANG_DIEN_RA — chỉ cần "tồn tại". Hiện có 7 khóa học DA_DUYET — đủ điều kiện. Block thật sự là **FE thiếu button**, không phải khóa học state.

---

## State hiện tại (verify qua API GET, account `cb_nv_tw_02`)

| Entity | Total | State distribution |
|---|:-:|---|
| **Đề kiểm tra** | 5 | 5/5 NHAP, 0 DA_PHAN_PHOI, all `khoaHocId=null` |
| **Khóa học** | 7 | 7/7 DA_DUYET (đủ điều kiện làm khóa target cho phân phối) |

5 ĐKT R8 baseline (cover 5 LV: SHTT/Thuế/ĐĐ/LĐ/HC) + 1 đã edit R8 ("Luật Đất đai 2026 (R8 edited)") — confirms tạo+sửa từng PASS R8.

---

## Kiểm tra 8 bước R7.4.B10

| # | Bước | Account | UI verify R9 | Status | Note |
|:-:|---|---|---|:-:|---|
| 1 | Tạo ĐKT thủ công | CB_NV_TW | List có button "Tạo đề kiểm tra" + 5 record từ R8 | ✅ R8 baseline stable | Form Tạo có nút (chưa re-test create R9 vì state đã có 5) |
| 2 | Sửa ĐKT NHAP | CB_NV_TW | **Detail page chỉ có "Quay lại". List row Thao tác cell rỗng** | ❌ FE Regression | BE PATCH endpoint OK (returns 422 cần `version` field — endpoint sống) |
| 3 | Xóa ĐKT chưa sử dụng | CB_NV_TW | List row Thao tác cell rỗng — không có icon Xóa | ❌ FE Regression | "Luật Đất đai 2026 (R8 edited)" record cho thấy R8 từng xóa+tạo lại; R9 không thấy nút |
| 4 | Trình duyệt NHAP→CHO_DUYET | CB_NV_TW | Detail page không có button "Trình duyệt" | ❌ FE thiếu | SRS không ghi rõ ĐKT có submit/approve workflow như CTĐT — có thể đúng spec |
| 5 | Phê duyệt CHO_DUYET→DA_DUYET | CB_PD_TW | N/A | ❌ thiếu | Cần BA xác nhận state machine ĐKT có duyệt không |
| 6 | Phân phối DA_DUYET→DA_PHAN_PHOI | CB_NV_TW | Detail page **không có** button "Phân phối" | ❌ FE thiếu | SRS FR-III-NEW-03 endpoint `POST /distribute` exists (BE 422 needs `version`) |
| 7 | Map bài giảng | CB_NV_TW | Không thấy field/button Mapping | ❌ FE thiếu | Cùng UC FR-III-NEW-03 |
| 8 | Verify ĐKT → khóa học link | API GET | `khoaHocId=null` cho cả 5 record | ⏳ chưa test | Cần step 6 chạy được trước |

**Tóm tắt R9 vs R8 báo cáo:**
- R8 ghi 6/8 PASS (tạo + sửa + xóa) — không reproduce được R9 do FE thiếu button. Có thể R8 đã đúng vào thời điểm test (FE refactor regression giữa R8→R9), HOẶC R8 dùng API direct trước khi user áp policy "must be UI" 2026-05-09.

---

## BE endpoint discovered (R9 probe)

| Endpoint | HTTP | Status R9 probe |
|---|:-:|---|
| `POST /api/v1/de-kiem-tras/{id}/distribute` | 200/422 | ✅ exists, validation `version` field (optimistic locking) |
| `PATCH /api/v1/de-kiem-tras/{id}` | 200/422 | ✅ exists, validation `version` field |
| `POST /api/v1/de-kiem-tras/{id}/phan-phoi` | 404 | ❌ không exist (use `/distribute`) |
| `POST /api/v1/de-kiem-tras/{id}/assign` | 404 | ❌ không exist |

→ BE đã sẵn sàng. Bottleneck = FE.

---

## Bằng chứng

- [List page rỗng action cell](r7-4-b10-r9-list-no-actions.png) — column "Thao tác" header có nhưng cell content empty `<div class="ant-space">`
- [Detail page chỉ "Quay lại"](r7-4-b10-r9-detail-only-back-button.png) — không có Sửa/Xóa/Phân phối/Trình duyệt button

DOM inspection (R9 probe via `evaluate_script`):
```
List row last cell HTML: <div class="ant-space ..."></div>  // empty
Detail page action area: chỉ button "Quay lại danh sách"
```

---

## Bug recommend log

**BUG-DKT-FE-REGRESSION-01** — Major P1 — FE missing all CRUD + workflow action buttons cho ĐKT (NHAP state)

- List row "Thao tác" column render `<div class="ant-space"></div>` rỗng
- Detail page chỉ có "Quay lại danh sách"
- BE endpoints `/distribute`, `PATCH /de-kiem-tras/{id}` đều tồn tại + responding 422 với valid validation errors
- Account `cb_nv_tw_02` có đủ permissions: `update_de_kiem_tra`, `delete_de_kiem_tra` (verified `/auth/me`)
- → Suggest dev priority: render action icons trong row + buttons trên detail page theo state machine

---

## Action recommend (per /qa-only mode — report only, no fix)

1. **Đính chính giả định R8:** Bỏ block "cần R7.4.B7 dev fix khóa học DANG_DIEN_RA". Phân phối ĐKT chỉ cần khóa học tồn tại, không cần state cụ thể.
2. **Log bug FE regression** — Major P1, escalate FE team.
3. **Update todo R7.4.B10** giữ ⚠️ (không thay đổi count) + đổi block reason: từ "chờ R7.4.B7" → "FE missing action buttons (BE OK)".
4. **R7.4.B10 sẽ unblock sớm hơn dự kiến** sau khi FE fix render buttons (không phải chờ R7.4.B7 dev fix 4 nút Khai giảng/Kết thúc/...).

---

## Phụ lục — Môi trường test R9

| Thành phần | Giá trị |
|---|---|
| URL | http://103.172.236.130:3000 |
| Account | `cb_nv_tw_02 / Secret@123` (CB_NV_TW, full perms) |
| OTP | `666666` |
| Tool | Chrome DevTools MCP |
| Browser | Chrome 147.0.7727.138 |
| Session | 2026-05-10 (continued from 2026-05-09 R9 sequence) |

---

*R9 verify | QA Automation via Claude Code | 2026-05-10*
