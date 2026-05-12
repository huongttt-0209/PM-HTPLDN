# Bug Report — Module 7.16 API Kết nối Chia sẻ Dữ liệu (R7.7.16)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000 (HTTP-only, không TLS) |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-10 02:35:00 (UTC+7) — scope mở rộng 2026-05-11 19:35:00 (UTC+7) |
| **Loại test** | Functional — API contract probe |
| **Round** | R7 |
| **Tài liệu tham chiếu** | [functional-test-report-r7-7-16-api.md](../../functional/cross-cutting/functional-test-report-r7-7-16-api.md) · [7.16-API-ket-noi-chia-se.md](../../../../funtion/7.16-API-ket-noi-chia-se.md) · [CHANGELOG §FR-16](../../../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) |

---

## Tổng hợp

Phát hiện **2** lỗi có SRS reference cụ thể trong quá trình probe 9 cặp endpoint API outbound module 7.16.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 2    | 1        | 1     | 0      | 0     | 0       | 0      | 2    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-API-001 | Major | P0 | Auth | API-001/003/004/006-010/031/033/034/039/040/043 (16 TC) | `srs-fr-16-api §BR-INTG-02 mTLS+JWT 2 lớp` + `7.16 §Ghi chú thực thi line 226` | mTLS test cert missing — block 16 TC trên 1/9 cặp deployed | 🚫 Defer (chờ phase tích hợp API ngoài) |
| BUG-API-002 | Critical | P0 | Data | API-013..030, 032, 044 (22 TC) | `srs-fr-16-api FR-XII-03..18` (16 FR — 8/9 cặp endpoint) + CHANGELOG §FR-16 Thay đổi 1+3+5 | 8/9 cặp outbound API endpoint chưa deploy — block 22 TC + v3.5 verify | 🚫 Defer (chờ phase tích hợp API ngoài) |

---

## BUG-API-001 — mTLS test cert missing trên test env, không verify được mTLS handshake protocol-level

> **Defer 2026-05-12 — chờ phase tích hợp API ngoài.** Bug phụ thuộc infra outbound mTLS sandbox (FR-XII publish API publish cho external systems consume). Không fix dev nội bộ. Re-test khi infra cấp mTLS client cert + sandbox staging có.

> **Meta:** Severity Major / Priority P0 / Type Auth / Status Defer / TC API-001, 003, 004, 006-010, 031, 033, 034, 039, 040, 043 / SRS `srs-fr-16-api.md §BR-INTG-02` + `output/funtion/7.16-API-ket-noi-chia-se.md §Ghi chú thực thi`.

### Mô tả

QA chạy curl probe 9 cặp endpoint outbound API module 7.16 trên test env `103.172.236.130:3000`. Endpoint `/api/v1/hoi-dap` (1/9 cặp deployed) enforce mTLS gate trả 401 ERR-AUTH-MTLS-01, nhưng test env HTTP-only không có TLS handshake → không cấp được client certificate hợp lệ để vượt gate, không verify được data filter / pagination / sort / rate-limit / v3.5 filter rename `cong_khai=1`. Block 16 TC trên cặp HOI_DAP duy nhất đã deploy.

### Các bước tái hiện

1. QA chạy curl không gửi cert: `curl -i http://103.172.236.130:3000/api/v1/hoi-dap`
2. Quan sát: HTTP 401 + body `{"success":false,"error":{"code":"ERR-AUTH-MTLS-01","message":"mTLS client certificate verification failed"}}` ngay lập tức (không chờ TLS handshake fail)
3. Gửi `Authorization: Bearer fake-token` → vẫn HTTP 401 ERR-AUTH-MTLS-01 (mTLS check trước Authorization parse)
4. Quan sát: app-layer enforce mTLS qua header parsing (X-Client-Cert, X-Forwarded-Client-Cert, hoặc tương đương) → reject mọi request không có cert hợp lệ → block toàn bộ TC infrastructure cần data response thật

### Kết quả mong đợi

- Theo `srs-fr-16-api.md §BR-INTG-02` (mTLS + JWT 2 lớp): test env QA cần có `client.crt + client.key` từ PM CA test-only để probe full 16 TC infrastructure (envelope shape API-001, JWT auth API-003/004, pagination API-008, sort API-009, rate-limit API-007/034, response time API-010, workflow API-031, parameter validate API-033, content-type API-039, JWT tampered API-040, v3.5 don_vi_id API-043).
- Theo `7.16 §Ghi chú thực thi line 226-227`: "Test env `103.172.236.130:3000` hiện dùng **HTTP (không TLS)** + bypass OTP 666666. Dev cần xác nhận có test-only JWT endpoint và chấp nhận skip mTLS trên env này. Nếu skip mTLS → mark API-005 `BLOCKED — test env không có TLS handshake`, retest ở staging có cert."
- Spec cần dev xác nhận: hoặc cấp test cert + bật TLS trên dev env, hoặc tách 1 staging có TLS, hoặc bật mode bypass mTLS test-only qua flag env.

### Kết quả thực tế

- Endpoint `/api/v1/hoi-dap` (FR-XII-01 deployed) trả 401 ERR-AUTH-MTLS-01 cho mọi probe HTTP plaintext, không có cách bypass.
- Endpoint `/oauth/token` route bắt SPA HTML (Vite dev catch-all) → không phải OAuth real endpoint, không cấp được JWT.
- Endpoint `/api/v1/oauth/token` trả 401 (exists, cần auth riêng).
- Endpoint `/api/v1/auth/login` trả 404 (internal CMS auth dùng path khác — `/api/v1/auth/...` hoặc tương tự cho FE login session, không cho consumer outbound).
- Không có endpoint `/api/v1/health`, `/api/v1/version`, `/api/v1/swagger` để probe spec/devtools.
- API-005 spec yêu cầu test với cert mTLS invalid/expired/self-signed → TLS handshake fail (connection refused). Actual: app-layer 401 (HTTP plaintext, không reach TLS layer) → PARTIAL only.

### Bằng chứng

**curl probe HOI_DAP (mTLS gate):**

```bash
$ curl -i --max-time 5 http://103.172.236.130:3000/api/v1/hoi-dap
HTTP/1.1 401 Unauthorized
Content-Type: application/json; charset=utf-8

{"success":false,"error":{"code":"ERR-AUTH-MTLS-01","message":"mTLS client certificate verification failed","timestamp":"2026-05-09T19:04:00.806Z","requestId":"1ef0c6a6-1d1a-4a7a-a0ef-635e10e77ef0"}}
```

**curl probe với fake Bearer token:**

```bash
$ curl -i -H "Authorization: Bearer fake-token" http://103.172.236.130:3000/api/v1/hoi-dap
HTTP/1.1 401 Unauthorized

{"success":false,"error":{"code":"ERR-AUTH-MTLS-01","message":"mTLS client certificate verification failed","timestamp":"2026-05-09T19:04:34.243Z"}}
```

→ Order auth gate: mTLS check → JWT parse → scope verify. Fake token không reach JWT layer.

**Probe OAuth/devtools endpoints:**

```bash
$ curl -s -w "%{http_code}\n" http://103.172.236.130:3000/oauth/token
200  (returns SPA HTML, not OAuth)

$ curl -s -w "%{http_code}\n" http://103.172.236.130:3000/api/v1/oauth/token
401

$ curl -s -w "%{http_code}\n" http://103.172.236.130:3000/api/v1/auth/login
404

$ curl -s -w "%{http_code}\n" http://103.172.236.130:3000/api/v1/health
404

$ curl -s -w "%{http_code}\n" http://103.172.236.130:3000/api/v1/swagger
404
```

→ Không có cách lấy JWT consumer outbound qua test env. Không có Swagger/health endpoint để probe spec.

---

## BUG-API-002 — 8/9 cặp outbound API endpoint trả HTTP 404, module substantially undeployed

> **Defer 2026-05-12 — chờ phase tích hợp API ngoài.** 8/9 cặp outbound API endpoint (FR-XII-01..18) publish ra external systems consume. Bug phụ thuộc external integration deploy. Không fix dev nội bộ giai đoạn hiện tại. Re-test khi BE deploy 8 cặp endpoint còn lại + tích hợp xong.

> **Meta:** Severity Critical / Priority P0 / Type Data / Status Open / TC API-013..030, 032, 044 (22 TC) / SRS `srs-fr-16-api FR-XII-03..18` (16 FR) + CHANGELOG §FR-16 Thay đổi 1+3+5+6+7.

> **Update 2026-05-11 19:35:00 — scope mở rộng:** Re-probe live xác nhận (1) 9/9 outbound cặp 404 (kể cả `/api/v1/hoi-dap` outbound endpoint nay đã 404 — có thể BE đổi route từ R7 lần đầu sang `/api/v1/hoi-daps` plural, hoặc route flat `/api/v1/hoi-dap` mới còn deploy lúc R7 lần 1), (2) **module TVCS substantially undeployed cả internal lẫn outbound** — `/api/v1/tu-van-chuyen-saus` + `/api/v1/noi-dung-tu-van-css` đều 404 → workaround spec-verify TVCS qua internal CMS KHÔNG khả thi từ test env hiện tại, (3) internal CMS deploy 5/8 entity với schema v3.5 đúng — verify được API-017 (TVV `loaiTvv`+HOAT_DONG), API-021 (KE_HOACH_DANH_GIA entity rename), API-023 (BIEU_MAU `congKhai` rename PASS).

### Mô tả

QA chạy curl probe 9 cặp endpoint outbound module 7.16 (FR-XII-01..18). 8/9 cặp trả HTTP 404 ERR-SYS-00-04-01 "Cannot GET /api/v1/{resource}" — endpoint chưa được dev deploy lên test env. Block 22 TC bao gồm 8 thay đổi v3.5 (filter rename `cong_khai=1`, BR-PUBLIC-04 privacy whitelist, rename field `la_cong_khai → cong_khai` + `ngay_cong_khai → thoi_gian_dang_tai`, parameter mới `don_vi_id`, UC renumber HSPL DN UC189/190 → UC187/188, rename TVCS, rename KE_HOACH_DANH_GIA, TU_VAN_VIEN HOAT_DONG state). Đặc biệt nghiêm trọng: API-019 (P0 Critical privacy whitelist 9 fields VỤ VIỆC ngoài cổng — NĐ 13/2023 + NQ 03/2017) không thể verify do `/api/v1/vu-viec` 404.

### Các bước tái hiện

1. QA chạy probe loop cho 9 endpoint chia sẻ: `for ep in /api/v1/{hoi-dap,dao-tao,tu-van-vien,vu-viec,danh-gia,bieu-mau,tu-van-chuyen-sau,chuong-trinh-htpl,ho-so-pl-dn}; do curl -sw "${ep} → HTTP %{http_code}\n" -o /dev/null --max-time 5 "http://103.172.236.130:3000${ep}?cong_khai=1&size=2"; done`
2. Quan sát: 1/9 cặp (HOI_DAP) trả 401 ERR-AUTH-MTLS-01 → endpoint exist
3. 8/9 cặp còn lại trả 404 ERR-SYS-00-04-01 "Cannot GET /api/v1/..." → endpoint chưa định nghĩa route
4. Verify thêm probe biến thể `/search` (ví dụ `/api/v1/vu-viec/search`) → cũng 404
5. Verify probe wrong version `/api/v0/hoi-dap` → 404 ERR-SYS-00-04-01 (đúng spec API-037)
6. Verify probe `/api/v1` root → 404 (no API root listing)

### Kết quả mong đợi

- Theo `srs-fr-16-api.md FR-XII-01..18`, 9 cặp endpoint outbound (chia sẻ + tìm kiếm) phải tồn tại + active mTLS gate:
  - `/api/v1/hoi-dap` (UC171), `/api/v1/hoi-dap/search` (UC172) — FR-XII-01/02
  - `/api/v1/dao-tao` (UC173), `/api/v1/dao-tao/search` (UC174) — FR-XII-03/04
  - `/api/v1/tu-van-vien` (UC175), `/api/v1/tu-van-vien/search` (UC176) — FR-XII-05/06
  - `/api/v1/vu-viec` (UC177), `/api/v1/vu-viec/search` (UC178) — FR-XII-07/08
  - `/api/v1/danh-gia` (UC179), `/api/v1/danh-gia/search` (UC180) — FR-XII-09/10
  - `/api/v1/bieu-mau` (UC181), `/api/v1/bieu-mau/search` (UC182) — FR-XII-11/12
  - `/api/v1/tu-van-chuyen-sau` (UC183), `/api/v1/tu-van-chuyen-sau/search` (UC184) — FR-XII-13/14
  - `/api/v1/chuong-trinh-htpl` (UC185), `/api/v1/chuong-trinh-htpl/search` (UC186) — FR-XII-15/16
  - `/api/v1/ho-so-pl-dn` (UC187 — rename từ UC189), `/api/v1/ho-so-pl-dn/search` (UC188 — rename từ UC190) — FR-XII-17/18 (Thay đổi 5 v3.5)
- Mỗi endpoint phải:
  - Trả HTTP 401 ERR-AUTH-MTLS-01 khi không có mTLS cert (tương tự cặp HOI_DAP đã deployed)
  - Sau khi qua mTLS+JWT, trả data theo filter publishable + envelope `{success, data, pagination, timestamp}`
  - Áp dụng v3.5 thay đổi: filter `cong_khai=1` cho 4 cặp HD/VV/BM/TVCS (Thay đổi 1), rename field `la_cong_khai → cong_khai` (Thay đổi 3), BR-PUBLIC-04 whitelist 9 fields VỤ VIỆC (Thay đổi 2), parameter `don_vi_id` cho HD+TVCS (Thay đổi 4), entity rename TVCS+KE_HOACH_DANH_GIA+TU_VAN_VIEN (Thay đổi 6/7/8)

### Kết quả thực tế

- Chỉ 1/9 cặp deployed: `/api/v1/hoi-dap` (FR-XII-01) trả 401 ERR-AUTH-MTLS-01.
- 8/9 cặp deploy thiếu — trả 404 ERR-SYS-00-04-01:

| Endpoint | HTTP | FR thiếu |
|----------|------|----------|
| `/api/v1/dao-tao` | 404 | FR-XII-03 |
| `/api/v1/tu-van-vien` | 404 | FR-XII-05 |
| `/api/v1/vu-viec` | 404 | FR-XII-07 (block P0 Critical privacy) |
| `/api/v1/danh-gia` | 404 | FR-XII-09 |
| `/api/v1/bieu-mau` | 404 | FR-XII-11 (block v3.5 rename `la_cong_khai`) |
| `/api/v1/tu-van-chuyen-sau` | 404 | FR-XII-13 (block v3.5 rename TVCS) |
| `/api/v1/chuong-trinh-htpl` | 404 | FR-XII-15 |
| `/api/v1/ho-so-pl-dn` | 404 | FR-XII-17 (block UC189→UC187 v3.5) |

- Cặp `/search` của 8 endpoint trên cũng 404 (tổng 16 endpoint thiếu = 8 cặp).
- Verify cặp HOI_DAP search: chưa probe (mTLS gate). Có khả năng `/api/v1/hoi-dap/search` đã deploy nhưng cần mTLS để verify.

### Bằng chứng

**curl probe loop (9 endpoint chia sẻ):**

```bash
$ for ep in /api/v1/hoi-dap /api/v1/dao-tao /api/v1/tu-van-vien /api/v1/vu-viec /api/v1/danh-gia /api/v1/bieu-mau /api/v1/tu-van-chuyen-sau /api/v1/chuong-trinh-htpl /api/v1/ho-so-pl-dn; do
    curl -sw "${ep} → HTTP %{http_code}\n" -o /dev/null --max-time 5 "http://103.172.236.130:3000${ep}?cong_khai=1&size=2"
done

/api/v1/hoi-dap            → HTTP 401   (✅ deployed, mTLS gate)
/api/v1/dao-tao            → HTTP 404   (❌ NOT DEPLOYED)
/api/v1/tu-van-vien        → HTTP 404   (❌ NOT DEPLOYED)
/api/v1/vu-viec            → HTTP 404   (❌ NOT DEPLOYED — P0 Critical privacy block)
/api/v1/danh-gia           → HTTP 404   (❌ NOT DEPLOYED)
/api/v1/bieu-mau           → HTTP 404   (❌ NOT DEPLOYED — v3.5 rename block)
/api/v1/tu-van-chuyen-sau  → HTTP 404   (❌ NOT DEPLOYED — v3.5 rename block)
/api/v1/chuong-trinh-htpl  → HTTP 404   (❌ NOT DEPLOYED)
/api/v1/ho-so-pl-dn        → HTTP 404   (❌ NOT DEPLOYED — UC renumber block)
```

**Sample 404 response body:**

```json
{
  "success": false,
  "error": {
    "code": "ERR-SYS-00-04-01",
    "message": "Cannot GET /api/v1/vu-viec?cong_khai=1&size=2",
    "timestamp": "2026-05-09T19:04:00.967Z",
    "requestId": "8fbed0be-3d09-40d1-a2e2-624657015ac2"
  }
}
```

→ ERR-SYS-00-04-01 = NestJS default "Cannot GET" handler (route không tồn tại), không phải ERR-API-401/403 (auth) → confirm endpoint chưa được mount.

**State-snapshot 2026-05-10 01:45 UTC entity prereq verified:** 6/6 entity ready (HOI_DAP=13, VU_VIEC=14, TVCS=15, HSCT=108, CT HTPLDN=3, TVN=50). Data sẵn sàng nhưng endpoint không có để consume → confirm bug ở deployment layer, không phải data layer.

**Bonus evidence 2026-05-11 19:28 — internal CMS deploy partial (5/8 entity):**

```bash
# Live re-probe outbound 2026-05-11 12:16 UTC+7 — 9/9 cặp đều 404
for ep in hoi-dap hoi-daps dao-tao tu-van-vien vu-viec danh-gia bieu-mau tu-van-chuyen-sau chuong-trinh-htpl ho-so-pl-dn; do
  curl -sw "/api/v1/outbound/${ep}: %{http_code}\n" -o /dev/null --max-time 5 "http://103.172.236.130:3000/api/v1/outbound/${ep}?cong_khai=1&limit=1"
done
# → tất cả 404
```

```bash
# Internal CMS probe — 5/8 entity deploy đúng schema v3.5
/api/v1/hoi-daps        : 401 ERR-AUTH-SYS-00-01  (deploy)
/api/v1/tu-van-viens    : 401 ERR-AUTH-SYS-00-01  (deploy — verify loaiTvv + HOAT_DONG via login probe)
/api/v1/vu-viecs        : 401 ERR-AUTH-SYS-00-01  (deploy)
/api/v1/bieu-maus       : 401 ERR-AUTH-SYS-00-01  (deploy — verify congKhai rename PASS)
/api/v1/chuong-trinh-htpls: 401 ERR-AUTH-SYS-00-01  (deploy — nhưng 0 record DA_CONG_BO, seed gap)
/api/v1/ke-hoach-danh-gias: (login probe) 200, 4 record HOAN_THANH (deploy — Thay đổi 7 verified)
/api/v1/dao-taos        : 404  (NOT DEPLOYED)
/api/v1/tu-van-chuyen-saus: 404  (NOT DEPLOYED — scope mở rộng)
/api/v1/danh-gia-htpls  : 404  (NOT DEPLOYED — chỉ ke-hoach-danh-gias)
/api/v1/ho-so-pl-dns    : 404  (NOT DEPLOYED)
```

**v3.5 field rename verify via internal CMS (MCP login `qtht_01` 2026-05-11 19:28):**

```javascript
// fetch('/api/v1/bieu-maus?limit=2') sample[0] keys:
// [..., trangThai, congKhai, thoiGianDangTai, anhDaiDien, moTaCongKhai, fileDinhKemCongKhai, ...]
// → congKhai field EXIST, la_cong_khai/laCongKhai ABSENT → Thay đổi 1.6 v3.5 PASS

// fetch('/api/v1/tu-van-viens?trangThai=HOAT_DONG&limit=3')
// meta: { total: 8, totalPages: 1 }
// sample[0]: { loaiTvv: 'TVV', trangThai: 'HOAT_DONG', ... }
// → Thay đổi 8 v3.5 PASS

// fetch('/api/v1/ke-hoach-danh-gias?limit=2')
// HTTP 200, 4 record, sample[0].trangThai: 'HOAN_THANH'
// → Entity rename DANH_GIA → KE_HOACH_DANH_GIA (Thay đổi 7 v3.5) PASS

// fetch('/api/v1/chuong-trinh-htpls?trangThai=DA_CONG_BO&limit=3')
// HTTP 200, meta { total: 0 }
// → SEED GAP — cần ≥1 CT trạng thái DA_CONG_BO trước outbound deploy
```

**Pre-flag risk privacy outbound:**
```javascript
// fetch('/api/v1/vu-viecs?limit=1') sample[0] keys:
// [..., maVuViec, tieuDe, trangThai, ..., tenDoanhNghiep: 'Công ty TNHH Bình Minh AG', tenNguoiHoTro]
// → Internal lộ tenDoanhNghiep. Khi outbound /api/v1/vu-viec deploy, BE PHẢI implement
//   separate serializer ẩn tenDoanhNghiep/MST/CCCD theo BR-PUBLIC-04 + NĐ 13/2023
```

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000 |
| API base | http://103.172.236.130:3000/api/v1 |
| Protocol | HTTP only (không TLS) — vi phạm BR-INTG-02 mTLS yêu cầu |
| Xác thực CMS internal | JWT login + OTP 666666 bypass |
| Xác thực API outbound | mTLS + JWT consumer (test env không có cert) |
| Frontend | React + Vite + Ant Design + CASL |
| Backend | NestJS + PostgreSQL (per ERR-SYS-00-04-01 default handler) |
| Tool test | curl + jq |
| OAuth real | Không có endpoint test-only (`/oauth/token` bắt SPA HTML; `/api/v1/oauth/token` trả 401 cần auth riêng) |
| Devtools | Không có `/health`, `/version`, `/swagger` — không probe spec runtime được |

---

*Bug report generated: 2026-05-10 02:35:00 (UTC+7) | Updated 2026-05-11 19:35:00 (UTC+7) — scope mở rộng: 9/9 outbound 404 (re-probe live) + 3/8 internal CMS cũng 404 (TVCS/dao-tao/danh-gia/ho-so) + 5/8 internal deploy verify được 3 v3.5 thay đổi qua field shape | QA Automation via Claude Code*
