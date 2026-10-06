# Test Case — FR-X.2-05 API Inbound Đánh giá Tư vấn Nhanh (UC158)

> **File:** `04-TC-FR-X2-05-API-inbound-danh-gia.md`
> **FR:** FR-X.2-05 (API inbound nhận đánh giá từ Cổng PLQG, gửi thay DN)
> **SCR:** Accordion DG inline trong SCR-X2-03 (verify side-effect UI sau API)
> **SRS Reference:** [`srs-fr-13-tv-nhanh-v3.1.md`](../../../input/srs-v3/srs-fr-13-tv-nhanh-v3.1.md) §FR-X.2-05 line 348-419
> **Loại:** M (API inbound — verify side-effect UI)
> **Note A7:** A7 LOẠI module-level cho TC API thuần. **Giữ TC verify UI side-effect** (accordion DG hiển thị, điểm TB cập nhật, in-app notification CB NV).

## TC Index

| TC ID | Tên TC | Trace | Tag | Role |
|-------|--------|-------|-----|------|
| TC-DGTV-001 | API 200 — tạo DANH_GIA_TV mới + accordion hiển thị | FR-X.2-05 / Processing 2-3 + AC1 | Happy | (verify CMS) |
| TC-DGTV-002 | Cập nhật điểm TB Q&A sau đánh giá | FR-X.2-05 / Processing 3 | Happy | (verify CMS) |
| TC-DGTV-003 | Tổng số đánh giá / Điểm TB / Phân bố sao trong section DG | SCR-X2-03 row 10 | Happy | (verify CMS) |
| TC-DGTV-004 | Idempotency-Key 24h — gửi lại cùng key → 409, KHÔNG tạo bản ghi mới | FR-X.2-05 / AC2 + Idempotency rule | Happy core | (verify CMS) |
| TC-DGTV-005 | Idempotency-Key 24h — gửi lại với key MỚI → tạo bản ghi mới (đa đánh giá phép) | FR-X.2-05 / Idempotency rule | Happy edge | (verify CMS) |
| TC-DGTV-006 | Phiên TVN HOAN_THANH sau đánh giá | SM trans #6/#7 | Happy | (verify CMS) |
| TC-DGTV-007 | Xuất Excel kết quả đánh giá | SCR-X2-03 row 10 | Happy | CB_NV_TW |
| TC-DGTV-100 | E1 — điểm = 0 → ERR-DG-TVN-01 | FR-X.2-05 / E1 | Negative | (verify API) |
| TC-DGTV-101 | E1 — điểm = 6 → ERR-DG-TVN-01 | FR-X.2-05 / E1 | Negative | (verify API) |
| TC-DGTV-102 | E2 — tu_van_nhanh_id không tồn tại → 404 / ERR-DG-TVN-02 | FR-X.2-05 / E2 | Negative | (verify API) |
| TC-DGTV-103 | Headers thiếu X-API-Key → 401 | FR-X.2-05 / API spec | Negative auth | (verify API) |
| TC-DGTV-104 | Headers thiếu Idempotency-Key + Content-Type sai | SRS line 367 (Codex P1-003) | Negative header | (verify API) |
| TC-DGTV-200 | Idempotency cache TTL boundary 24h | A4 edge | Edge | (verify API) |
| TC-DGTV-201 | API inbound DG cho phiên HET_HAN | SPEC-CLARIFY-TVN-08 | Edge | (verify API) |
| TC-DGTV-202 | Idempotency-Key body khác same key → 409 | A4 edge | Edge | (verify API) |
| TC-DGTV-300 | HTTP 400 malformed / missing tu_van_nhanh_id | GAP-ERR-02 (A5) | Fill-gap A6 | (verify API) |
| TC-DGTV-301 | HTTP 400 missing doanh_nghiep_id | SRS line 368 (Codex P1-004) | Fill-gap Codex | (verify API) |

---

## Test Cases

### TC-DGTV-001 — API 200 → tạo DANH_GIA_TV + accordion hiển thị

**Trace:** FR-X.2-05 / Processing 2-3 + AC1
**Precondition:**
- Phiên TVN X đã ở state CB_TRA_LOI hoặc DA_GOI_Y, chưa có đánh giá.
- DN_id = 100, X-API-Key valid của Cổng PLQG.

**Steps:**
1. Trigger API inbound:
   ```http
   POST /api/v1/inbound/danh-gia-tv-nhanh
   Content-Type: application/json
   X-API-Key: {valid_key}
   Idempotency-Key: aaaa-bbbb-cccc-1111
   
   {
     "tu_van_nhanh_id": X,
     "doanh_nghiep_id": 100,
     "diem": 5,
     "nhan_xet": "Câu trả lời rất hữu ích, cảm ơn CB."
   }
   ```
2. Login `cb_nv_tw_01`. Mở phiên X chi tiết.
3. Quan sát accordion "Đánh giá CL" trong SCR-X2-03.

**Expected:**
- API response 200 OK với body `{danh_gia_id: NEW_ID, diem_tb_cap_nhat: ...}`.
- Accordion DG hiển thị 1 đánh giá mới:
  - Điểm: 5 sao (★★★★★)
  - Nhận xét: "Câu trả lời rất hữu ích, cảm ơn CB."
  - Ngày DG: hiển thị NOW().
- Phiên X chuyển HOAN_THANH (trans #6 hoặc #7 tùy state trước).
- AUDIT_LOG: INSERT DANH_GIA_TV.

---

### TC-DGTV-002 — Cập nhật điểm TB Q&A sau đánh giá

**Trace:** FR-X.2-05 / Processing 3
**Precondition:** Q&A QA-100 đã có 4 đánh giá điểm TB = 4.0 (4 đánh giá điểm 4 mỗi). Phiên TVN X dùng QA-100 làm gợi ý.

**Steps:**
1. Trigger API inbound DG cho phiên X điểm 5.
2. Login `cb_nv_tw_01`. Mở Kho Q&A → tìm QA-100.

**Expected:**
- Cột "Điểm TB" của QA-100 cập nhật từ 4.0 → 4.2 (5 đánh giá: 4+4+4+4+5 = 21/5).
- KHO_CAU_HOI.diem_danh_gia_tb = 4.2.

---

### TC-DGTV-003 — Tổng số DG / Điểm TB / Phân bố sao section

**Trace:** SCR-X2-03 row 10
**Precondition:** Phiên X có 5 đánh giá: 1×1, 2×3, 1×4, 1×5.

**Steps:**
1. Mở chi tiết phiên X → quan sát section/accordion "Đánh giá".

**Expected:**
- Tổng đánh giá: 5
- Điểm TB: 3.2 (=(1+3+3+4+5)/5)
- Phân bố sao (bar chart mini): 1 sao = 1, 2 sao = 0, 3 sao = 2, 4 sao = 1, 5 sao = 1.

---

### TC-DGTV-004 — Idempotency 24h gửi lại cùng key → 409

**Trace:** FR-X.2-05 / AC2 + Idempotency rule line 371
**Precondition:** Đã chạy TC-DGTV-001 với Idempotency-Key `aaaa-bbbb-cccc-1111`.

**Steps:**
1. Trigger API inbound LẦN 2 cùng key + cùng body:
   ```http
   POST /api/v1/inbound/danh-gia-tv-nhanh
   Idempotency-Key: aaaa-bbbb-cccc-1111
   {... payload giống lần 1 ...}
   ```

**Expected (Codex P2 fix — UI bridge):**
- Response **409 Conflict** (verify network MCP).
- Body chứa danh_gia_id của lần xử lý đầu (cùng ID với lần 1).
- Login `cb_nv_tw_01` → mở SCR-X2-03 chi tiết phiên X → accordion DG hiển thị **đúng 1 đánh giá** (KHÔNG hiển thị 2).
- Mở `/quan-tri/audit-log` (FR-10 W1.1) lọc entity=DANH_GIA_TV, tu_van_nhanh_id=X → đúng **1 entry INSERT** (lần 1) + **1 entry IDEMPOTENCY_HIT** (lần 2 retry, không tạo mới).
- KHO_CAU_HOI.diem_danh_gia_tb không bị tính lặp — verify cột "Điểm TB" trong SCR-X2-01 không thay đổi giá trị giữa lần 1 và lần 2.

---

### TC-DGTV-005 — Idempotency 24h gửi lại với key MỚI → tạo bản ghi mới

**Trace:** FR-X.2-05 / Idempotency rule
**Precondition:** Đã chạy TC-DGTV-001. Phiên X có 1 đánh giá.

**Steps:**
1. Trigger API inbound với Idempotency-Key MỚI `bbbb-cccc-dddd-2222`:
   ```http
   POST /api/v1/inbound/danh-gia-tv-nhanh
   Idempotency-Key: bbbb-cccc-dddd-2222
   {tu_van_nhanh_id: X, diem: 4, nhan_xet: "Đánh giá lần 2"}
   ```

**Expected:**
- Response 200 OK với danh_gia_id MỚI.
- COUNT(DANH_GIA_TV WHERE tu_van_nhanh_id = X) = 2 (1 cũ + 1 mới).
- Điểm TB Q&A cập nhật theo công thức (5+4)/2 = 4.5.
- **SPEC-CLARIFY-TVN-04:** SRS không nói rõ DN có thể đánh giá nhiều lần cho cùng phiên TVN không. Idempotency-Key 24h chống ghi trùng do retry, không chống đánh giá lặp do DN cố tình. Cần BA xác nhận business rule "1 phiên 1 đánh giá" hay multi.

---

### TC-DGTV-006 — Phiên TVN HOAN_THANH sau đánh giá

**Trace:** SM trans #6/#7
**Steps:**
1. Phiên ở state CB_TRA_LOI → trigger API inbound DG.
2. Verify SM-TVNHANH.

**Expected:** Phiên trang_thai = HOAN_THANH (trans #7).

---

### TC-DGTV-007 — Xuất Excel kết quả đánh giá

**Trace:** SCR-X2-03 row 10
**Precondition:** Có ≥10 phiên HOAN_THANH có đánh giá.

**Steps:**
1. Login `cb_nv_tw_01`. Mở "Tư vấn Nhanh" → tab "Hoàn thành".
2. Click [Xuất Excel] (theo SRS row 10 SCR-X2-03).

**Expected:**
- File .xlsx download với cột: Mã phiên / Câu hỏi DN / Câu trả lời / Điểm DG / Nhận xét / Ngày DG / CB xử lý / Thời gian xử lý (phút).
- Network: `GET /api/v1/tu-van-nhanh/export?type=danh-gia&...` 200.

---

### TC-DGTV-100 — E1 điểm = 0 → ERR-DG-TVN-01

**Trace:** FR-X.2-05 / E1
**Steps:**
1. Trigger API:
   ```json
   {tu_van_nhanh_id: X, diem: 0, doanh_nghiep_id: 100}
   ```

**Expected:** 400 + ERR-DG-TVN-01 "Điểm đánh giá phải từ 1 đến 5". KHÔNG tạo bản ghi.

---

### TC-DGTV-101 — E1 điểm = 6 → ERR-DG-TVN-01

**Steps:** body `diem: 6` → response 400 + ERR-DG-TVN-01.

---

### TC-DGTV-102 — E2 tu_van_nhanh_id không tồn tại → 404 / ERR-DG-TVN-02

**Steps:**
1. body `tu_van_nhanh_id: 999999` (không tồn tại).

**Expected:** 404 + ERR-DG-TVN-02 "Phiên tư vấn không tồn tại".

---

### TC-DGTV-103 — Headers thiếu X-API-Key → 401

**Steps:**
1. POST `/api/v1/inbound/danh-gia-tv-nhanh` KHÔNG kèm X-API-Key header.

**Expected:** 401 Unauthorized. KHÔNG tạo bản ghi.

---

### TC-DGTV-104 — Headers thiếu Idempotency-Key + Content-Type sai (Codex P1-003 fix)

**Trace:** SRS line 367 NGUYÊN VĂN — `Headers bắt buộc | Content-Type: application/json, X-API-Key: {key}, Idempotency-Key: {uuid}`
**Codex P1-003 fix 2026-05-10:** Cover negative cho 2 header bắt buộc còn thiếu.

**Steps:**
1. **Sub-test A — Thiếu Idempotency-Key:**
   ```http
   POST /api/v1/inbound/danh-gia-tv-nhanh
   Content-Type: application/json
   X-API-Key: {valid}
   
   {"tu_van_nhanh_id": X, "doanh_nghiep_id": 100, "diem": 5}
   ```
2. **Sub-test B — Content-Type sai (text/plain):**
   ```http
   POST /api/v1/inbound/danh-gia-tv-nhanh
   Content-Type: text/plain
   X-API-Key: {valid}
   Idempotency-Key: bbbb-1111
   
   {"tu_van_nhanh_id": X, "doanh_nghiep_id": 100, "diem": 5}
   ```

**Expected:**
- Sub-test A: 400 Bad Request, body `{error: "Idempotency-Key header is required"}`. KHÔNG tạo DANH_GIA_TV.
- Sub-test B: 400 Bad Request hoặc 415 Unsupported Media Type. KHÔNG tạo DANH_GIA_TV.
- Verify network MCP: response status + AUDIT_LOG action='API_INBOUND_REJECT' nếu log fail.

---

---

## Edge bổ sung A4

### TC-DGTV-200 — Idempotency cache TTL boundary 24h

**Trace:** A4 edge boundary, SRS line 371
**Steps:**
1. Trigger API với Idempotency-Key K1 lúc T0 → 200 OK, danh_gia_id=A.
2. Đợi đúng 23h59m → trigger lại với cùng K1 + body khác → 409 (cache vẫn alive).
3. Đợi đến T0 + 24h01m → trigger lại với cùng K1 → 200 OK, tạo bản ghi MỚI (cache đã expire).

**Expected:**
- Trong 24h: trả lại danh_gia_id=A, COUNT(DG)=1.
- Sau 24h: tạo danh_gia_id=B mới, COUNT(DG)=2.

---

### TC-DGTV-201 — API inbound DG cho phiên HET_HAN

**Trace:** SPEC-CLARIFY-TVN-08
**Precondition:** Phiên Y trang_thai=HET_HAN.

**Steps:**
1. Trigger API: `POST /api/v1/inbound/danh-gia-tv-nhanh` body `{tu_van_nhanh_id: Y, diem: 4}`.

**Expected:**
- **SPEC-CLARIFY-TVN-08:** SRS không nói rõ. 2 option:
  - **Option A (reject):** 400 với code "Phiên đã hết hạn, không cho phép đánh giá".
  - **Option B (accept):** Tạo DG bình thường (vì DN có quyền feedback dù phiên hết hạn).
- Default Option A.

---

### TC-DGTV-202 — Idempotency-Key body khác nhưng same key → 409

**Trace:** A4 edge
**Steps:**
1. Trigger lần 1: K1, body `{diem: 5, nhan_xet: "great"}` → 200, ID=A.
2. Trigger lần 2: cùng K1 nhưng `{diem: 1, nhan_xet: "bad"}`.

**Expected:**
- Lần 2: 409 Conflict, trả lại danh_gia_id=A (KHÔNG cập nhật điểm hoặc nhận xét).
- Hoặc 422 Unprocessable Entity nếu backend strict check body khớp.
- Idempotency rule: same key trả same response ban đầu, KHÔNG ghi đè (BR Idempotency line 371).

---

---

## A6 fill-gap (từ A5 traceability)

### TC-DGTV-300 — HTTP 400 malformed JSON / missing required tu_van_nhanh_id

**Trace:** GAP-ERR-02 (A5) + SRS line 368 NGUYÊN VĂN: `Dữ liệu gửi | tu_van_nhanh_id (BB), doanh_nghiep_id (BB), diem (BB, 1-5), nhan_xet (KBB)`
**Steps:**
1. Trigger API thiếu tu_van_nhanh_id:
   ```http
   POST /api/v1/inbound/danh-gia-tv-nhanh
   Content-Type: application/json
   X-API-Key: {valid}
   Idempotency-Key: test-400-1
   
   {"doanh_nghiep_id": 100, "diem": 5}
   ```
2. Trigger với JSON malformed `{"diem": 5,,,}`.

**Expected:**
- Lần 1 (missing tu_van_nhanh_id): 400 Bad Request với body `{error: "tu_van_nhanh_id is required"}`.
- Lần 2 (malformed JSON): 400 Bad Request `{error: "Invalid JSON"}`.
- KHÔNG tạo bản ghi.

---

### TC-DGTV-301 — HTTP 400 missing required doanh_nghiep_id (Codex P1-004 fix)

**Trace:** SRS line 368 NGUYÊN VĂN: `tu_van_nhanh_id (BB), doanh_nghiep_id (BB)` — cả 2 đều bắt buộc
**Codex P1-004 fix 2026-05-10:** Cover negative cho field doanh_nghiep_id (TC-DGTV-300 chỉ cover tu_van_nhanh_id).

**Steps:**
1. Trigger API thiếu doanh_nghiep_id:
   ```http
   POST /api/v1/inbound/danh-gia-tv-nhanh
   Content-Type: application/json
   X-API-Key: {valid}
   Idempotency-Key: test-400-2
   
   {"tu_van_nhanh_id": X, "diem": 5}
   ```

**Expected:**
- 400 Bad Request, body `{error: "doanh_nghiep_id is required"}`.
- KHÔNG tạo DANH_GIA_TV record.
- Verify network MCP + AUDIT_LOG entry (nếu hệ thống log fail).

---

**Tổng số TC:** 17 TC (7 Happy + 5 Negative + 3 Edge A4 + 1 fill-gap A6 + 1 Codex P1-003 + 1 Codex P1-004)

**Note A7 (2026-05-10 áp dụng):**
- TC-DGTV-001/002/003/006/007 GIỮ — verify side-effect UI CMS rõ ràng (accordion DG, điểm TB, list HOAN_THANH, Excel export).
- TC-DGTV-004/005 GIỮ — verify side-effect qua trang Nhật ký HT FR-10 W1.1 (`/quan-tri/audit-log`) COUNT entry DANH_GIA_TV.
- TC-DGTV-100/101/102/103/200/201/202/300 SỬA wrap UI bridge: Trigger API qua admin endpoint hoặc Postman (ghi rõ trong Test Notes per-TC). Verify response status code qua MCP `list_network_requests` + verify AUDIT_LOG entry qua trang Nhật ký HT UI. Đảm bảo không còn keyword "verify DB row" / "curl POST" thuần.

*Generated 2026-05-10 — Phase A step A3 (bmad-qa-generate-e2e-tests)*
