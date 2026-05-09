# Bug Report — Người hỗ trợ pháp lý (NHT)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation via Claude Code |
| **Ngày** | 2026-05-08 23:45 (UTC+7) · **Re-classify:** 2026-05-09 |
| **Loại test** | Functional (R7.7.4.5) |
| **Round** | R7 (R8 verify) |
| **Tài liệu tham chiếu** | [functional-test-report-r7-7-4-5-nht.md](../../functional/nguoi-ho-tro/functional-test-report-r7-7-4-5-nht.md) · [7.4a-nguoi-ho-tro.md](../../../../funtion/7.4a-nguoi-ho-tro.md) |

---

## Tổng hợp

Phát hiện **5** lỗi trong R7.7.4.5 NHT functional. Sau BA chốt 2026-05-09 (QTHT KHÔNG có quyền thêm/sửa/xóa NHT), 2 bug đóng INVALID + 3 bug giữ Open.

### Severity breakdown (active sau re-classify 2026-05-09)

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed-Invalid |
|------|----------|-------|--------|-------|---------|----------------|
| 3    | 0        | 1     | 0      | 2     | 0       | 2              |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-NHT-003 | Major | P1 | Integration | NHT-003 | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1283` FR-VIII-26 §Processing Step 4 — "Gửi mail cho user kèm link đặt mật khẩu (URL chứa token)" | Mail kích hoạt: host hardcoded `localhost:3000` → link không click được trên máy ngoài BE host (BE flow OK với workaround replace IP) | Open |
| BUG-NHT-004 | Minor | P2 | UI/UX | NHT-017 (FR-IV-NHT-03) | `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md` FR-IV-NHT-03 — `3 tab: Thông tin / Bồi dưỡng / Vụ việc đã hỗ trợ` | Detail view thiếu tab "Bồi dưỡng" | Open |
| BUG-NHT-005 | Minor | P2 | UI/UX | NHT-004 | `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md` FR-IV-NHT-01 — ERR-NHT-01 | FE không hiện toast lỗi khi BE reject duplicate username | Open |
| ~~BUG-NHT-001~~ | ~~Major~~ | ~~P0~~ | Permission | NHT-001/006/007/008..012 | BA chốt 2026-05-09: QTHT KHÔNG có quyền thêm/sửa/xóa NHT | QTHT thiếu CRUD UI — INVALID (design đúng) | **Closed-Invalid** |
| ~~BUG-NHT-002~~ | ~~Major~~ | ~~P1~~ | UI/UX | NHT-001 | BA chốt 2026-05-09: QTHT không tạo NHT → field Đơn vị tự do không applicable | Modal Thêm NHT thiếu field Đơn vị cho QTHT — INVALID | **Closed-Invalid** |

---

## BUG-NHT-003 — Mail kích hoạt host hardcoded `localhost:3000` → link không click được trên máy ngoài BE host

> **Re-test 2026-05-09 17:42:** ⚠️ Re-classify Major P0 → P1 sau khi click thử thật qua MCP. BE consume token OK + chuyển HOAT_DONG. Bug nằm ở mail template — host literal `localhost:3000` thay vì lấy từ env config public URL → user thực tế (mail mở trên máy không phải BE server) không kích hoạt được.

### Mô tả

Mail "Kích hoạt tài khoản Người hỗ trợ pháp lý — PM-HTPLDN" gửi từ BE chứa link với **host hardcoded `http://localhost:3000`** thay vì public URL của môi trường (env `APP_URL` / `FRONTEND_URL`). Khi user mở mail trên máy bất kỳ ngoài BE server (LAN, Internet, mobile), `localhost` resolve về máy của user → không có service chạy port 3000 → link không kích hoạt được TK. Backend flow đúng spec — chỉ cấu hình host trong mail template sai.

### Các bước tái hiện

1. cb_nv_tw_03 (đơn vị BTP-TW) tạo NHT mới `nht_tc001_btp_tw` qua modal "Thêm mới"
2. Hệ thống tự động gửi mail kích hoạt đến `nht_tc001_btp_tw@htpldn.test`
3. Mở MailHog UI `http://103.172.236.130:8025/` (hoặc curl API `/api/v2/search?kind=to&query=nht_tc001_btp_tw`)
4. Inspect mail body HTML
5. Click link trong mail (host nguyên gốc `localhost:3000`) từ máy QA (không phải BE server)

### Kết quả mong đợi

Theo **FR-VIII-26 §Processing Step 4** (file `srs-update-2026-5-5/srs-fr-10-quan-tri.md` line 1283): "Gửi mail cho user kèm link đặt mật khẩu (URL chứa token). Note: nếu là TK do hệ thống cấp lần đầu (TVV/CG/NHT) thì mail kích hoạt được gửi tự động ngay khi tạo TK".

Mục đích step 4: **link click được** trên môi trường thực để user đặt MK lần đầu. Format đúng:
```
http://${APP_URL}/auth/verify-email?token=<UUID>
```
Trong đó `${APP_URL}` là biến env config (vd dev: `103.172.236.130:3000`, staging: `staging.htpldn.gov.vn`, prod: `htpldn.gov.vn`).

### Kết quả thực tế

**Step 5 click link host `localhost:3000` từ máy QA → fail** (browser resolve `localhost` về máy QA, không phải BE server `103.172.236.130`):
- Hoặc trang trống (không có service chạy port 3000)
- Hoặc lỗi `ERR_CONNECTION_REFUSED`

**Verify backend flow OK** bằng cách replace host → IP server:
- URL fix: `http://103.172.236.130:3000/auth/verify-email?token=6ee6d7cd-7db7-4047-bfdb-38d47fbfbd3b`
- POST `/api/v1/auth/verify-email` body `{"token":"..."}` → 200
- Response: `{"success":true,"data":{"message":"Tài khoản đã được kích hoạt. Vui lòng đăng nhập để tiếp tục.","trangThai":"HOAT_DONG"}}`
- NHT-BTP-TW-0005: CHO_KICH_HOAT → HOAT_DONG ✅

→ **BE flow + token verify đúng spec**. Bug chỉ nằm ở mail template config: host literal `localhost:3000` thay vì biến env.

**Note phụ (Trivial, không phải hard-spec):** Link nằm raw text trong `<p>` thay vì `<a href>`. Đa số mail client (Gmail/Outlook) auto-linkify URL nên user vẫn click được; chỉ MailHog UI hiện text. SRS FR-VIII-26 không quy định format anchor → đây là best-practice UX, không log thành bug riêng. Đính chính bug log gốc R7: `&#x3D;` HTML entity KHÔNG phải bug (browser tự decode khi parse HTML).

### Bằng chứng

**1. Mail HTML body raw — host literal `localhost:3000`** (curl MailHog `/api/v2/search?kind=to&query=nht_tc001_btp_tw` → QP decode):

```html
<!DOCTYPE html>
<html lang="vi">
<body style="font-family: Arial, sans-serif; max-width: 600px; ...">
  <h2 style="color: #EF4444;">🔔 Thông báo hệ thống: Kích hoạt tài khoản Người hỗ trợ pháp lý — PM-HTPLDN</h2>
  <p>Xin chào NHT TC001 Test BTP TW,
  ...
  Vui lòng click link dưới đây để kích hoạt tài khoản (link có hiệu lực vĩnh viễn):
  http://localhost:3000/auth/verify-email?token&#x3D;6ee6d7cd-7db7-4047-bfdb-38d47fbfbd3b</p>
</body>
</html>
```
→ Host `localhost:3000` literal, không phải biến env. BE server thực ở `103.172.236.130:3000`.

**2. Workaround test 2026-05-09 17:42 — replace host → IP, BE flow OK:**

```
Network requests (chrome-devtools MCP):
reqid=1   GET  http://103.172.236.130:3000/auth/verify-email?token=6ee6d7cd-7db7-4047-bfdb-38d47fbfbd3b → 200
reqid=149 POST http://103.172.236.130:3000/api/v1/auth/verify-email
          Request body:  {"token":"6ee6d7cd-7db7-4047-bfdb-38d47fbfbd3b"}
          Response 200:  {"success":true,"data":{"message":"Tài khoản đã được kích hoạt. Vui lòng đăng nhập để tiếp tục.","trangThai":"HOAT_DONG"},"meta":null}
reqid=154 GET  http://103.172.236.130:3000/api/v1/auth/me → 401 (chưa login, redirect /login)
```
→ Token consume thành công + state chuyển HOAT_DONG. Bug verify đúng nằm ở mail template host config, không phải BE logic.

**3. NotebookLM/SRS local 2-source verify:**

- **SRS local match:** `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1283` — quote nguyên văn Step 4: "Gửi mail cho user kèm link đặt mật khẩu (URL chứa token)"
- Spec không quy định cụ thể `${APP_URL}` từ env nhưng **mục đích step** (link click được) bị vi phạm khi host literal `localhost`

---

## BUG-NHT-004 — Detail view NHT thiếu tab "Bồi dưỡng"

### Mô tả

Detail view `/nguoi-ho-tro/{id}` chỉ hiển thị 2 tab: "Thông tin" và "Vụ việc đã hỗ trợ". SRS NHT-017 yêu cầu **3 tab**: Thông tin / Bồi dưỡng / Vụ việc đã hỗ trợ. Tab "Bồi dưỡng" mất → không xem được lịch sử bồi dưỡng NHT (NĐ 55/2019 Đ.7).

### Các bước tái hiện

1. cb_nv_tw_03 vào `/nguoi-ho-tro`
2. Click `eye` button bất kỳ NHT
3. Quan sát số tab trên detail view

### Kết quả mong đợi

- 3 tab: `Thông tin` / `Bồi dưỡng` / `Vụ việc đã hỗ trợ`
- Tab Bồi dưỡng hiển thị danh sách khoá đào tạo NHT đã tham gia (từ FR-III)

### Kết quả thực tế

- 2 tab: `Thông tin` (selected) + `Vụ việc đã hỗ trợ`
- Thiếu tab `Bồi dưỡng` hoàn toàn

### Bằng chứng

Detail view structure (a11y snapshot trích):
```
uid=191_14 tab "Thông tin" selectable selected
uid=191_15 tab "Vụ việc đã hỗ trợ" selectable
[KHÔNG có uid tab "Bồi dưỡng"]
```

(Screenshot detail view không capture riêng — đã verify qua a11y snapshot.)

---

## BUG-NHT-005 — FE không hiển thị toast lỗi khi BE reject duplicate username

### Mô tả

Submit form tạo NHT với username trùng (đã tồn tại trong DB) — BE reject (record không được tạo, count list không tăng) nhưng FE đóng modal mà không hiển thị toast/notification để user biết lý do fail. UX: user nghĩ tạo thành công.

### Các bước tái hiện

1. cb_nv_tw_03 đã tạo `nht_tc001_btp_tw` thành công ở NHT-001
2. Click "Thêm mới" lần 2
3. Fill: Họ tên `NHT TC004 Duplicate`, Email `nht_tc004_other@htpldn.test`, Username **`nht_tc001_btp_tw`** (trùng), Lĩnh vực `Thuế`
4. Click "Tạo"
5. Quan sát phản hồi UI

### Kết quả mong đợi

- Theo `ERR-NHT-01`: BE reject với message "Tên đăng nhập đã tồn tại" (hoặc tương đương)
- FE hiện toast `.ant-message-error` / `.ant-notification-error` chứa message lỗi
- Modal giữ nguyên data + highlight field bị conflict
- User biết phải sửa username

### Kết quả thực tế

- Modal đóng ngay sau click "Tạo"
- Không có toast/notification hiển thị (DOM rỗng `.ant-message`, `.ant-notification`, `[role="alert"]`)
- List count giữ nguyên 12 (không tăng 13) → BE đã block đúng
- User không có feedback → nhìn list không thấy record mới mà không biết tại sao

### Bằng chứng

**Verify count không tăng (proof BE đã block):**

```js
// API verify before/after submit duplicate
GET /api/v1/nguoi-ho-tro?size=100
→ before: 12 records
→ after submit duplicate: 12 records (no new TC004)
```

**Verify DOM toast rỗng:**

```js
document.querySelectorAll('.ant-message-error, .ant-notification-error, [role="alert"]')
→ NodeList(0)
```

---

## ~~BUG-NHT-001~~ [CLOSED-INVALID] — QTHT thiếu CRUD UI buttons trên module Người hỗ trợ pháp lý

> **Re-classify 2026-05-09:** ⛔ INVALID — BA chốt QTHT KHÔNG có quyền thêm/sửa/xóa NHT. NHT do CB Nghiệp vụ (cùng đơn vị) quản lý theo NĐ 55/2019 Đ.7. UI ẩn buttons Add/Edit/Delete/Swap với QTHT là **design đúng**. SRS srs-fr-04 §SCR-IV-NHT-01/02 line 1737-1738 + 1781-1782 (ghi "QTHT thêm/sửa/xóa toàn hệ thống") là **outdated** so với BA chốt 2026-05-09 — cần BA update SRS.

### Mô tả (giữ lịch sử)

qtht_03 vào `/nguoi-ho-tro` chỉ thấy button `eye` (xem chi tiết); KHÔNG có "Thêm mới"/Edit/Delete/Swap. cb_nv_tw_03 vào cùng URL hiển thị đầy đủ. Trước đây QA gọi đây là "permission inversion" — sau BA chốt 2026-05-09 đây là **design đúng**.

### Bằng chứng (giữ lịch sử)

**1. View qua qtht_03 (chỉ có Eye — design đúng theo BA chốt):**

![qtht_03 read-only NHT — design đúng](image/00-list-qtht-03-readonly.png)

**2. View qua cb_nv_tw_03 (đầy đủ Add/Edit/Delete/Swap — đúng spec):**

![cb_nv_tw_03 full CRUD NHT](image/00-list-cb-nv-tw-03.png)

### Permission UI matrix (sau BA chốt 2026-05-09)

| Role | URL | Add btn | Edit btn | Delete btn | Swap btn | Eye btn |
|------|-----|---------|----------|------------|----------|---------|
| qtht_03 (QTHT) | /nguoi-ho-tro | ❌ (đúng) | ❌ (đúng) | ❌ (đúng) | ❌ (đúng) | ✅ |
| cb_nv_tw_03 (CB NV TW) | /nguoi-ho-tro | ✅ | ✅ | ✅ | ✅ (HOAT_DONG only) | ✅ |

---

## ~~BUG-NHT-002~~ [CLOSED-INVALID] — Modal "Thêm NHT" thiếu field "Đơn vị"

> **Re-classify 2026-05-09:** ⛔ INVALID — BA chốt QTHT KHÔNG tạo NHT → yêu cầu "field Đơn vị tự do cho QTHT" không còn applicable. CB NV tạo NHT với đơn vị auto-lock = đơn vị mình (đúng BR-AUTH-08), modal 4 field (Họ tên, Email, Username, Lĩnh vực) là đúng workflow CB NV.

### Mô tả (giữ lịch sử)

Modal "Thêm người hỗ trợ pháp lý" chỉ có 4 field bắt buộc (Họ và tên, Email, Tên đăng nhập, Lĩnh vực chuyên môn). Trước đây QA giả định spec yêu cầu 5 field cho QTHT; sau BA chốt 2026-05-09: QTHT KHÔNG tạo NHT → 4 field là đủ.

### Bằng chứng (giữ lịch sử)

**Modal thêm NHT (4 field — đúng workflow CB NV):**

![Modal NHT 4 field — design đúng cho CB NV](image/01-nht001-modal-filled.png)

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (bypass tạm — dev confirm 2026-04-19) |
| MailHog (OTP/activation inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design (Modal pattern, button labels Vietnamese) |
| Xác thực | JWT + OTP email |
| Tool test | Chrome DevTools MCP (`mcp__chrome-devtools__*`) |

---

*Bug report generated: 2026-05-08 23:45 (UTC+7) | Re-classify: 2026-05-09 — BA chốt QTHT không có quyền tạo NHT | QA Automation via Claude Code*
