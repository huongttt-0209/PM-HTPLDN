# SRS — Section 3.2.16: API Kết nối Chia sẻ Dữ liệu

**Dự án:** Phần mềm hỗ trợ pháp lý doanh nghiệp
**Phiên bản SRS:** 3.0
**Nhóm:** XII — API Kết nối Chia sẻ Dữ liệu
**UC range:** UC 171 – UC 188 + UC189 (mới — inbound hỏi đáp; CSV v1.1 chưa có, BA chốt giữ trạng thái này tại review 2026-05-10) + 2 API transaction bổ sung ngoài baseline UC cho tab "Tổ chức tư vấn" `[STT14]` (không làm tăng tổng số UC)
**Số FR:** 24 (20 outbound danh sách/tìm kiếm + 3 outbound xem chi tiết get-by-id `[STT9/11/15/17/19]` + 1 inbound)
**File chính:** `srs-v3.md` Section 3.2

---

## Mục lục file này

- [1. Tổng quan nhóm](#1-tổng-quan-nhóm)
- [2. Yêu cầu chức năng chi tiết](#2-yêu-cầu-chức-năng-chi-tiết)
- [3. Màn hình chức năng](#3-màn-hình-chức-năng)
- [4. Entity liên quan](#4-entity-liên-quan)
- [5. State Machine liên quan](#5-state-machine-liên-quan)
- [6. Business Rules liên quan](#6-business-rules-liên-quan)

---

## 1. Tổng quan nhóm

**Mục đích:** 24 endpoint API kết nối với hệ thống khác (chủ yếu Cổng PLQG module HTPLDN) qua REST + JSON, kết nối trực tiếp không qua LGSP. **23 outbound** (CMS cung cấp dữ liệu ra: 20 danh sách/tìm kiếm + 3 xem chi tiết) + **1 inbound** (Cổng PLQG đẩy hỏi đáp về CMS).

**Tác nhân chính:** Cổng PLQG (cả consumer outbound và sender inbound), Hệ thống khác (consumer outbound).

**Đặc thù:**
- **Outbound:** 10 cặp API (chia sẻ + tìm kiếm), mỗi cặp phục vụ 1 loại nội dung, cộng 3 API xem chi tiết get-by-id. Auth: mTLS + JWT scope `read`/`search`. Filter chỉ trả dữ liệu đã công khai (`cong_khai = true AND is_deleted = false` + trạng thái publishable theo từng entity).
- **Inbound:** Cổng PLQG đẩy câu hỏi DN về CMS để CB nghiệp vụ tiếp nhận. Auth: mTLS + JWT scope `write`. Idempotency qua `external_id` UNIQUE (UPSERT khi Cổng retry).
- **Hành vi "công khai" trong nghiệp vụ (FR-02/04/12/13/15):** chỉ là thao tác nội bộ — CB NV/PD set `cong_khai = 1` + cập nhật trạng thái công khai/publishable trên CSDL CMS. Cổng PLQG sẽ tự pull dữ liệu mới qua API outbound định kỳ. KHÔNG có API outbound push riêng từ CMS ra Cổng (BA chốt 2026-05-10 — mô hình a). Wording "đẩy lên Cổng PLQG" / "push API Cổng PLQG" trong các FR khác là viết tắt nghiệp vụ cho hành vi này.

**10 cặp API outbound:**

| # | Nội dung | UC Chia sẻ | UC Tìm kiếm | FR-ID Chia sẻ | FR-ID Tìm kiếm |
|---|---------|-----------|-------------|--------------|----------------|
| 1 | Hỏi đáp/vướng mắc PL | UC171 | UC172 | FR-XII-01 | FR-XII-02 |
| 2 | Đào tạo/bồi dưỡng | UC173 | UC174 | FR-XII-03 | FR-XII-04 |
| 3 | CG/TVV | UC175 | UC176 | FR-XII-05 | FR-XII-06 |
| 4 | Tổ chức tư vấn `[STT14]` | API transaction STT14-LIST (mở rộng UC175) | API transaction STT14-SEARCH (mở rộng UC176) | FR-XII-22 | FR-XII-23 |
| 5 | Vụ việc TGPL | UC177 | UC178 | FR-XII-07 | FR-XII-08 |
| 6 | Đánh giá hiệu quả | UC179 | UC180 | FR-XII-09 | FR-XII-10 |
| 7 | Thư viện biểu mẫu | UC181 | UC182 | FR-XII-11 | FR-XII-12 |
| 8 | Tư vấn chuyên sâu | UC183 | UC184 | FR-XII-13 | FR-XII-14 |
| 9 | CT HTPLDN | UC185 | UC186 | FR-XII-15 | FR-XII-16 |
| 10 | Hồ sơ pháp lý DN (entity HO_SO_PHAP_LY_DN — tài liệu pháp lý: giấy phép, hợp đồng, giấy chứng nhận, quyết định) | UC187 | UC188 | FR-XII-17 | FR-XII-18 |

> **Ghi chú trình bày:** `FR-XII-22/23` được đặt ngay sau `FR-XII-05/06` trong phần chi tiết để giữ ngữ cảnh nghiệp vụ Mạng lưới tư vấn viên. Registry chính thức vẫn theo `FR-ID`; các bảng traceability ở `srs-v3.5.md` ghi rõ `STT14-LIST/SEARCH`.

**1 endpoint inbound (mới):**

| # | Nội dung | UC | FR-ID | Tác nhân |
|---|---------|----|-----|---------|
| 1 | Tiếp nhận hỏi đáp/vướng mắc pháp lý từ Cổng PLQG | UC189 (mới) | FR-XII-19 | Cổng PLQG (sender) |

**Quy trình nghiệp vụ tổng quan:**

```mermaid
graph LR
    subgraph Outbound[23 Outbound API — CMS cung cấp dữ liệu]
        A[Cổng PLQG / Hệ thống khác] -->|GET REST+JSON, mTLS+JWT scope read/search| B[PM HTPLDN API Gateway]
        B --> C{Verify JWT + Rate Limit}
        C -->|OK| D[Truy vấn dữ liệu publishable]
        D --> E[Trả response JSON]
        C -->|Fail| F[HTTP 401/403/429]
    end
    subgraph Inbound[1 Inbound API — Cổng đẩy hỏi đáp về CMS]
        G[Cổng PLQG] -->|POST REST+JSON, mTLS+JWT scope write| H[PM HTPLDN API Gateway]
        H --> I{Verify JWT + Idempotency check external_id}
        I -->|Mới| J[INSERT HOI_DAP kenh=CONG_PLQG]
        I -->|Trùng external_id| K[Trả existing internal_id]
        J --> L[Trả 201 + internal_id + presigned upload URLs]
        K --> M[Trả 200 status=already_received]
    end
    D --> N[Ghi AUDIT_LOG]
    J --> N
```

---

## 2a. Đặc tả chung TPL-API

> Tất cả API outbound nhóm XII kế thừa đặc tả chung này. Mỗi FR bổ sung phần đặc thù (endpoint, scope, request/response, processing riêng).

**Đặc tả kỹ thuật chung:**

| Thuộc tính | Giá trị |
|-----------|---------|
| Format | RESTful JSON |
| Bảo mật | mTLS + JWT Bearer token (kết nối trực tiếp với Cổng PLQG, không qua LGSP) |
| Rate limit | 100 req/min/consumer |
| Response time | < 3 giây |
| Base URL | `https://htpldn.moj.gov.vn/api/v1` |
| Versioning | URL path: `/v1/...` |
| Pagination | `?page=1&size=20` (default 20, max 100) |
| Sorting | `?sort=ngay_tao,desc` |
| Error format | `{"success": false, "error": {"code": "...", "message": "...", "details": [...]}}` |
| Dữ liệu trả về | CHỈ bản ghi đã duyệt / công khai / hoàn thành (publishable) |

**Luồng xác thực:**

1. Consumer (Cổng PLQG) gửi request trực tiếp đến PM (REST JSON)
2. PM thực hiện mTLS verification (kết nối trực tiếp, không qua LGSP)
3. Request kèm Header: Authorization: Bearer {JWT}
4. PM verify JWT (RS256, issuer = htpldn.moj.gov.vn)
5. Kiểm tra claims: consumer_id, scope, exp
6. Rate limit check: 100 req/min/consumer_id
7. Xử lý business logic
8. Trả response JSON

**Response Envelope chung:**

```json
{
  "success": true,
  "data": { ... },
  "pagination": {
    "page": 1,
    "size": 20,
    "total_elements": 150,
    "total_pages": 8
  },
  "timestamp": "2026-03-25T10:30:00+07:00"
}
```

**Trường thời gian chung mọi response outbound:** Mọi response outbound nhóm XII đều kèm `ngay_tao` (= `created_at`) và `ngay_cap_nhat` (= `updated_at`) của bản ghi — kiểu `datetime`, định dạng ISO 8601 (Common Fields BR-DATA-03).

**Preconditions chung (TPL-API-FULL):**

- Consumer đã đăng ký kết nối trực tiếp và được cấp client certificate (mTLS)
- Consumer có JWT hợp lệ với scope tương ứng
- Kết nối trực tiếp PM<->Cổng PLQG khả dụng
- Dữ liệu nguồn ở trạng thái publishable (đã duyệt / đã công khai)
- **`[CR-01]`** Với entities có Common Public Fields: chỉ trả bản ghi có `cong_khai = 1`. Áp dụng BR-PUBLIC-01 (chỉ hoàn thành mới CK), BR-PUBLIC-04 (whitelist/blacklist fields cho VU_VIEC).

**Postconditions chung (TPL-API-FULL):**

- Dữ liệu được trả về cho consumer (read-only, không thay đổi dữ liệu PM)
- AUDIT_LOG ghi nhận: consumer_id, endpoint, timestamp, response_code
- Rate limit counter cập nhật cho consumer_id

**Error Handling chung (TPL-API-FULL):**

| # | Điều kiện lỗi | Mã lỗi | Phản hồi hệ thống | Severity |
|---|--------------|--------|-------------------|----------|
| E1 | Tham số request không hợp lệ | ERR-API-400 | HTTP 400 "Tham số không hợp lệ: {chi tiết}" | ERROR |
| E2 | JWT không hợp lệ, hết hạn, hoặc thiếu | ERR-API-401 | HTTP 401 "Xác thực thất bại. JWT không hợp lệ hoặc hết hạn" | ERROR |
| E3 | JWT scope không đủ quyền | ERR-API-403 | HTTP 403 "Không có quyền truy cập API này. Yêu cầu scope: {scope}" | ERROR |
| E4 | Resource không tồn tại hoặc đã bị xóa | ERR-API-404 | HTTP 404 "Không tìm thấy tài nguyên" | ERROR |
| E5 | Vượt rate limit (100 req/min/consumer) | ERR-API-429 | HTTP 429 "Vượt giới hạn tần suất. Thử lại sau {retry_after}s" | WARNING |
| E6 | Lỗi server nội bộ | ERR-API-500 | HTTP 500 "Lỗi hệ thống nội bộ. Vui lòng thử lại sau" | ERROR |
| E7 | PM không khả dụng hoặc đang bảo trì | ERR-API-503 | HTTP 503 "Dịch vụ tạm thời không khả dụng. Thử lại sau" | ERROR |

**Acceptance Criteria chung (TPL-API-FULL):**

- **Given** dữ liệu đã duyệt **When** consumer gọi API với JWT hợp lệ **Then** trả về JSON theo format envelope, HTTP 200
- **Given** PM down **When** consumer gọi API **Then** trả HTTP 503 + message, consumer queue và retry
- **Given** JWT hết hạn **When** consumer gọi API **Then** trả HTTP 401
- **Given** vượt rate limit **When** consumer gọi API **Then** trả HTTP 429 + header Retry-After

---

## 2. Yêu cầu chức năng chi tiết

---

### FR-XII-01: API Chia sẻ hỏi đáp (UC171)

**UC Reference:** UC 171
**Source:** Team thiết kế API, CĐT review
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/hoi-dap`
**Scope JWT:** `htpldn:hoi-dap:read`

**Mô tả:**
API cung cấp danh sách hỏi đáp/vướng mắc pháp lý **đã công khai** cho consumer (filter `trang_thai = CONG_KHAI AND cong_khai = true AND is_deleted = false`).

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + entity HOI_DAP có dữ liệu trạng thái CONG_KHAI (đã đẩy thành công lên Cổng).

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | page | number | N | >= 1 | 1 | query param |
| 2 | size | number | N | 1-100 | 20 | query param |
| 3 | linh_vuc_id | number | N | FK -> DANH_MUC | — | query param |
| 4 | tu_ngay | date | N | ISO 8601 | — | query param |
| 5 | den_ngay | date | N | ISO 8601 | — | query param |
| 6 | don_vi_id | number | N | FK → DON_VI. Lọc theo cơ quan tiếp nhận | — | query param `[CR-06]` |

**Processing (Xử lý):**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Xác thực JWT + scope htpldn:hoi-dap:read | BR-AUTH-01 |
| 2 | Kiểm tra rate limit | BR-API-01 |
| 3 | Kiểm tra tham số request | — |
| 4 | Truy vấn hỏi đáp `trang_thai = CONG_KHAI AND cong_khai = true AND is_deleted = false` (chỉ bản ghi đã đẩy thành công lên Cổng PLQG, không lộ DA_DUYET nội bộ) | BR-PUBLIC-01 `[CR-01]` |
| 5 | Áp dụng bộ lọc (lĩnh vực, khoảng ngày, don_vi_id) | `[CR-06]` |
| 6 | Phân trang | BR-DATA-08 |
| 7 | Ghi nhật ký thao tác | BR-DATA-05 |

**Outputs (Response Data):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ma_hoi_dap | text | luôn | HD-{date}-{seq} |
| 3 | cau_hoi | text | luôn | — |
| 4 | cau_tra_loi | text | luôn | — |
| 5 | linh_vuc | structured | luôn | {id, ten} |
| 6 | ngay_tra_loi | date | luôn | ISO 8601 |
| 7 | nguoi_tra_loi | text | luôn | — |
| 8 | ngay_tao | datetime | luôn | ISO 8601 |
| 9 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /hoi-dap?linh_vuc_id=1 **When** JWT hợp lệ **Then** trả danh sách hỏi đáp đã công khai (CONG_KHAI + cong_khai=true + is_deleted=false) thuộc lĩnh vực, phân trang

**Cross-ref:** Entity HOI_DAP, DANH_MUC

---

### FR-XII-02: API Tìm kiếm hỏi đáp (UC172)

**UC Reference:** UC 172
**Source:** Team thiết kế API, CĐT review
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/hoi-dap/search`
**Scope JWT:** `htpldn:hoi-dap:search`

**Mô tả:**
API tìm kiếm toàn văn hỏi đáp theo từ khóa.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | keyword | text | Y | Min 2 ký tự | — | query param |
| 2 | page | number | N | >= 1 | 1 | query param |
| 3 | size | number | N | 1-100 | 20 | query param |
| 4 | linh_vuc_id | number | N | FK -> DANH_MUC | — | query param |

**Processing (Xử lý):**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Xác thực JWT + scope | BR-AUTH-01 |
| 2 | Kiểm tra rate limit | BR-API-01 |
| 3 | Kiểm tra: từ khóa bắt buộc, tối thiểu 2 ký tự | — |
| 4 | Tìm kiếm toàn văn trên câu hỏi và câu trả lời | BR-DATA-08 |
| 5 | Sắp xếp theo điểm relevance giảm dần | — |
| 6 | Phân trang | BR-DATA-08 |
| 7 | Ghi nhật ký thao tác | BR-DATA-05 |

**Outputs:** Giống FR-XII-01 + trường relevance_score (number). Bổ sung khối `facets` để dựng dropdown lọc lĩnh vực: `facets.linh_vuc[]` = {id, ten, count} ← `HOI_DAP.linh_vuc_id` → DANH_MUC (chỉ lĩnh vực đang có hỏi đáp công khai) `[STT16]`.

**Postconditions:** Theo TPL-API-FULL.

**Error Handling:** Theo TPL-API-FULL. Bổ sung:

| # | Điều kiện lỗi | Mã lỗi | Phản hồi hệ thống | Severity |
|---|--------------|--------|-------------------|----------|
| E8 | Từ khóa trống hoặc < 2 ký tự | ERR-API-SEARCH-01 | "Từ khóa tìm kiếm phải có ít nhất 2 ký tự" | ERROR |

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "hợp đồng" **When** search **Then** trả danh sách hỏi đáp chứa từ khóa, sắp xếp theo relevance
- **Given** consumer gọi search **When** có kết quả **Then** response kèm khối `facets.linh_vuc[]` (id, ten, count) để dựng dropdown lọc `[STT16]`

**Cross-ref:** Entity HOI_DAP

---

### FR-XII-03: API Chia sẻ đào tạo (UC173)

**UC Reference:** UC 173
**Source:** Team thiết kế API
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/dao-tao`
**Scope JWT:** `htpldn:dao-tao:read`

**Mô tả:**
API cung cấp danh sách khóa đào tạo/bồi dưỡng cho consumer.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + entity KHOA_HOC có dữ liệu publishable.

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | page | number | N | >= 1 | 1 | query param |
| 2 | size | number | N | 1-100 | 20 | query param |
| 3 | hinh_thuc | text | N | TRUC_TUYEN / TRUC_TIEP | — | query param |
| 4 | tu_ngay | date | N | — | — | query param |
| 5 | den_ngay | date | N | — | — | query param |

**Processing (Xử lý):**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Xác thực JWT + scope htpldn:dao-tao:read | BR-AUTH-01 |
| 2 | Kiểm tra rate limit | BR-API-01 |
| 3 | Truy vấn khóa học ở trạng thái publishable (đang diễn ra / kết thúc / đã duyệt) | — |
| 4 | Áp dụng bộ lọc, phân trang | BR-DATA-08 |
| 5 | Ghi nhật ký thao tác | BR-DATA-05 |

**Outputs (Response Data):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ma_khoa_hoc | text | luôn | KH-{date}-{seq} |
| 3 | ten_khoa_hoc | text | luôn | — |
| 4 | hinh_thuc | text | luôn | TRUC_TUYEN / TRUC_TIEP |
| 5 | ngay_bat_dau | date | luôn | ISO 8601 |
| 6 | ngay_ket_thuc | date | luôn | ISO 8601 |
| 7 | so_hoc_vien | number | luôn | — |
| 8 | trang_thai | text | luôn | — |
| 9 | ngay_tao | datetime | luôn | ISO 8601 |
| 10 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /dao-tao **When** JWT hợp lệ **Then** trả danh sách khóa học, phân trang

**Cross-ref:** Entity KHOA_HOC

---

### FR-XII-04: API Tìm kiếm đào tạo (UC174)

**UC Reference:** UC 174
**Source:** Team thiết kế API
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/dao-tao/search`
**Scope JWT:** `htpldn:dao-tao:search`

**Mô tả:**
API tìm kiếm toàn văn khóa đào tạo theo từ khóa.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs:** keyword (text, Y, min 2 ký tự) + page + size. Tương tự pattern FR-XII-02.

**Processing:** Xác thực JWT -> rate limit -> tìm kiếm toàn văn trên tên khóa học + mô tả -> sắp xếp relevance -> phân trang -> ghi log.

**Outputs:** Giống FR-XII-03 + relevance_score.

**Error Handling:** Theo TPL-API-FULL + ERR-API-SEARCH-01.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "pháp luật" **When** search **Then** trả danh sách khóa học matching, sorted by relevance

**Cross-ref:** Entity KHOA_HOC

---

### FR-XII-05: API Chia sẻ CG/TVV (UC175)

**UC Reference:** UC 175
**Source:** Team thiết kế API
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/tu-van-vien`
**Scope JWT:** `htpldn:tvv:read`

**Mô tả:**
API cung cấp danh sách chuyên gia/tư vấn viên đang hoạt động. Loại trừ thông tin nhạy cảm (CMND, CCCD, địa chỉ cá nhân, SĐT).

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + entity TU_VAN_VIEN có dữ liệu trạng thái HOAT_DONG.

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | page | number | N | >= 1 | 1 | query param |
| 2 | size | number | N | 1-100 | 20 | query param |
| 3 | linh_vuc_id | number | N | FK -> lĩnh vực chuyên môn | — | query param |
| 4 | dia_ban | text | N | Tỉnh/TP | — | query param |
| 5 | loai | text | N | TVV / CG | — | query param `[STT14]` |

**Processing (Xử lý):**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Xác thực JWT + scope htpldn:tvv:read | BR-AUTH-01 |
| 2 | Kiểm tra rate limit | BR-API-01 |
| 3 | Truy vấn tư vấn viên đang hoạt động | — |
| 4 | Loại trừ thông tin nhạy cảm (CMND, CCCD, địa chỉ cá nhân, SĐT) | BR-SEC-01 |
| 5 | Áp dụng bộ lọc, phân trang | BR-DATA-08 |
| 6 | Ghi nhật ký thao tác | BR-DATA-05 |

**Outputs (Response Data):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ho_ten | text | luôn | — |
| 3 | loai | text | luôn | TVV / CG `[STT14]` |
| 4 | linh_vuc | structured | luôn | [{id, ten}] |
| 5 | dia_ban | text | luôn | — |
| 6 | to_chuc_hanh_nghe | text | luôn | — |
| 7 | trang_thai | text | luôn | HOAT_DONG |
| 8 | ngay_tao | datetime | luôn | ISO 8601 |
| 9 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /tu-van-vien?linh_vuc_id=1 **When** JWT hợp lệ **Then** trả DS TVV thuộc lĩnh vực, KHONG chứa CMND/SĐT

**Cross-ref:** Entity TU_VAN_VIEN, TVV_LINH_VUC

---

### FR-XII-06: API Tìm kiếm CG/TVV (UC176)

**UC Reference:** UC 176
**Source:** Team thiết kế API
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/tu-van-vien/search`
**Scope JWT:** `htpldn:tvv:search`

**Mô tả:**
API tìm kiếm CG/TVV theo từ khóa (tên, tổ chức). Loại trừ thông tin nhạy cảm.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs:** keyword (text, Y) + linh_vuc_id + dia_ban + page + size.

**Processing:** Xác thực JWT -> rate limit -> tìm kiếm trên họ tên, tổ chức -> loại trừ thông tin nhạy cảm -> sắp xếp, phân trang -> ghi log.

**Outputs:** Giống FR-XII-05.

**Error Handling:** Theo TPL-API-FULL + ERR-API-SEARCH-01.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "Luật ABC" **When** search **Then** trả DS TVV thuộc tổ chức Luật ABC

**Cross-ref:** Entity TU_VAN_VIEN, TVV_LINH_VUC

---

### FR-XII-22: API Chia sẻ Tổ chức tư vấn `[STT14]`

**UC Reference:** API transaction STT14-LIST (mở rộng UC175 — tab "Tổ chức tư vấn" trong Mạng lưới tư vấn viên; không tạo UC mới)
**Source:** STT14 báo cáo đối soát API — bổ sung API outbound riêng cho entity `TO_CHUC_TU_VAN`
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/to-chuc-tu-van`
**Scope JWT:** `htpldn:to-chuc-tu-van:read`

**Mô tả:**
API cung cấp danh sách Tổ chức tư vấn pháp luật đang hoạt động và đã công khai để Cổng PLQG hiển thị tab "Tổ chức tư vấn". API này **không dùng chung** FR-XII-05 vì `TO_CHUC_TU_VAN` là entity riêng, không phải giá trị `loai` của `TU_VAN_VIEN`.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + entity `TO_CHUC_TU_VAN` có dữ liệu `trang_thai = HOAT_DONG`, `cong_khai = 1`.

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | page | number | N | >= 1 | 1 | query param |
| 2 | size | number | N | 1-100 | 20 | query param |
| 3 | linh_vuc_id[] | identifier[] | N | FK → DANH_MUC | — | query param |
| 4 | loai_hinh[] | text[] | N | CONG_TY_LUAT / VP_LUAT_SU / TT_TVPL / KHAC | — | query param |
| 5 | don_vi_id[] | identifier[] | N | FK → DON_VI; mapping `TO_CHUC_TU_VAN.don_vi_id` | — | query param |
| 6 | sort | text | N | field,asc/desc | thoi_gian_dang_tai,desc | query param |

**Processing (Xử lý):**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Xác thực mTLS + JWT + scope `htpldn:to-chuc-tu-van:read` | BR-AUTH-01, BR-INTG-02 |
| 2 | Kiểm tra rate limit | BR-API-01, BR-INTG-03 |
| 3 | Truy vấn `TO_CHUC_TU_VAN` với điều kiện `trang_thai = 'HOAT_DONG' AND cong_khai = 1 AND is_deleted = false` | BR-INTG-07 |
| 4 | Áp dụng bộ lọc `linh_vuc_id[]`, `loai_hinh[]`, `don_vi_id[]` | BR-INTG-07 |
| 5 | Chỉ trả trường công khai; không trả `file_dinh_kem` nội bộ, `ghi_chu` nội bộ, lịch sử thao tác, thông tin tài khoản | BR-SEC-01 |
| 6 | Phân trang, sắp xếp | BR-API-01 |
| 7 | Ghi nhật ký thao tác | BR-DATA-05 |

**Outputs (Response Data):**

| # | Tên | Nguồn |
|---|-----|-------|
| 1 | id, ma_to_chuc | `TO_CHUC_TU_VAN.id`, `.ma_to_chuc` |
| 2 | ten_to_chuc | `TO_CHUC_TU_VAN.ten_to_chuc` |
| 3 | loai_hinh | `TO_CHUC_TU_VAN.loai_hinh` |
| 4 | linh_vuc[] | Junction lĩnh vực của tổ chức → DANH_MUC `{id, ten}` |
| 5 | dia_chi | `TO_CHUC_TU_VAN.dia_chi` |
| 6 | don_vi_quan_ly {id, ten} | `TO_CHUC_TU_VAN.don_vi_id` → DON_VI |
| 7 | nguoi_dai_dien | `TO_CHUC_TU_VAN.nguoi_dai_dien` |
| 8 | dien_thoai, email, website | `TO_CHUC_TU_VAN.dien_thoai`, `.email`, `.website` |
| 9 | so_giay_dkhd, ngay_cap_dkhd | `TO_CHUC_TU_VAN.so_giay_dkhd`, `.ngay_cap_dkhd` |
| 10 | so_qd_cong_bo, ngay_qd_cong_bo | `TO_CHUC_TU_VAN.so_qd_cong_bo`, `.ngay_qd_cong_bo`; quyết định công bố công khai tổ chức trên danh sách |
| 11 | so_quyet_dinh_cong_nhan, ngay_cong_nhan | `TO_CHUC_TU_VAN.so_quyet_dinh_cong_nhan`, `.ngay_cong_nhan`; quyết định công nhận/ghi nhận năng lực tổ chức, trả kèm nếu có dữ liệu |
| 12 | anh_dai_dien | `TO_CHUC_TU_VAN.anh_dai_dien` (mặc định ảnh hệ thống nếu trống) |
| 13 | mo_ta_cong_khai | `TO_CHUC_TU_VAN.mo_ta_cong_khai` |
| 14 | file_dinh_kem_cong_khai[] | `TO_CHUC_TU_VAN.file_dinh_kem_cong_khai` — chỉ file đã chọn để công khai |
| 15 | so_luong_tvv_lien_ket | Count `TVV_TO_CHUC` với `TVV_TO_CHUC.to_chuc_id = TO_CHUC_TU_VAN.id`, liên kết đang kích hoạt, `TVV_TO_CHUC.is_deleted = false`, `TU_VAN_VIEN.trang_thai = 'HOAT_DONG'`, `TU_VAN_VIEN.is_deleted = false` |
| 16 | trang_thai, thoi_gian_dang_tai, ngay_cap_nhat | `TO_CHUC_TU_VAN.trang_thai`, `.thoi_gian_dang_tai`, `.updated_at` |
| 17 | ngay_tao | `TO_CHUC_TU_VAN.created_at` |

**Response object chuẩn cho `file_dinh_kem_cong_khai[]`:**

| Field | Kiểu logic | Bắt buộc | Mô tả |
|-------|-----------|----------|-------|
| file_id | identifier | Y | ID file công khai, không dùng ID file nội bộ nếu file chưa được chọn công khai |
| ten_file | text | Y | Tên file hiển thị |
| url | text | Y | URL download/preview đã ký hoặc URL public theo cấu hình media |
| mime_type | text | N | MIME type |
| size_bytes | number | N | Kích thước file |
| thoi_gian_cong_khai | datetime | N | Thời điểm file được chọn công khai |

**Postconditions:** Theo TPL-API-FULL (read-only).
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /to-chuc-tu-van **When** JWT hợp lệ **Then** chỉ trả tổ chức `HOAT_DONG` + `cong_khai = 1` + `is_deleted = false`
- **Given** consumer truyền `don_vi_id[]` **When** gọi API **Then** chỉ trả tổ chức thuộc đơn vị quản lý tương ứng
- **Given** consumer truyền `linh_vuc_id[]` hoặc `loai_hinh[]` **When** gọi API **Then** chỉ trả tổ chức khớp lĩnh vực/loại hình và vẫn bảo toàn điều kiện công khai
- **Given** tổ chức có Common Public Fields (`anh_dai_dien`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai[]`, `thoi_gian_dang_tai`) **When** trả response **Then** response chứa đúng các trường công khai này theo schema đã định nghĩa
- **Given** tổ chức có `file_dinh_kem` nội bộ nhưng không có `file_dinh_kem_cong_khai` **When** trả response **Then** KHÔNG trả file nội bộ
- **Given** tổ chức có dữ liệu `ghi_chu`, lịch sử thao tác hoặc thông tin tài khoản nội bộ **When** trả response **Then** các trường này không xuất hiện trong payload

**Cross-ref:** Entity TO_CHUC_TU_VAN, TVV_TO_CHUC, TU_VAN_VIEN, DANH_MUC, DON_VI

---

### FR-XII-23: API Tìm kiếm Tổ chức tư vấn `[STT14]`

**UC Reference:** API transaction STT14-SEARCH (mở rộng UC176 — tab "Tổ chức tư vấn" trong Mạng lưới tư vấn viên; không tạo UC mới)
**Source:** STT14 báo cáo đối soát API — bổ sung API outbound riêng cho entity `TO_CHUC_TU_VAN`
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/to-chuc-tu-van/search`
**Scope JWT:** `htpldn:to-chuc-tu-van:search`

**Mô tả:**
API tìm kiếm Tổ chức tư vấn pháp luật theo từ khóa và bộ lọc lĩnh vực / loại hình / đơn vị quản lý. Output dùng chung cấu trúc với FR-XII-22.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | keyword | text | Y | >= 2 ký tự; bắt buộc với endpoint `/search` | — | query param |
| 2 | linh_vuc_id[] | identifier[] | N | FK → DANH_MUC | — | query param |
| 3 | loai_hinh[] | text[] | N | CONG_TY_LUAT / VP_LUAT_SU / TT_TVPL / KHAC | — | query param |
| 4 | don_vi_id[] | identifier[] | N | FK → DON_VI; mapping `TO_CHUC_TU_VAN.don_vi_id` | — | query param |
| 5 | page | number | N | >= 1 | 1 | query param |
| 6 | size | number | N | 1-100 | 20 | query param |

**Processing:** Xác thực JWT → rate limit → validate `keyword` bắt buộc và tối thiểu 2 ký tự → tìm kiếm toàn văn trên `ten_to_chuc`, `ma_to_chuc`, `nguoi_dai_dien`, lĩnh vực/loại hình đã đánh chỉ mục → áp filter `trang_thai = 'HOAT_DONG' AND cong_khai = 1 AND is_deleted = false` + các tham số lọc thêm → sắp theo relevance → phân trang → ghi log. Khi consumer không có từ khóa, consumer dùng API danh sách `GET /api/v1/to-chuc-tu-van` kèm bộ lọc thay vì gọi endpoint `/search`.

**Outputs:** Giống FR-XII-22.

**Error Handling:** Theo TPL-API-FULL. Bổ sung: nếu thiếu `keyword` hoặc `keyword` < 2 ký tự → `ERR-API-SEARCH-01`.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "Luật ABC" **When** search **Then** trả DS tổ chức matching keyword và chỉ gồm tổ chức đang hoạt động, đã công khai
- **Given** consumer không có keyword và chỉ cần lọc theo `linh_vuc_id[]`, `loai_hinh[]` hoặc `don_vi_id[]` **When** cần lấy dữ liệu **Then** consumer dùng FR-XII-22 `GET /api/v1/to-chuc-tu-van`, không gọi endpoint `/search`
- **Given** consumer gửi keyword 1 ký tự **When** search **Then** trả lỗi `ERR-API-SEARCH-01`
- **Given** consumer không gửi keyword **When** gọi `/api/v1/to-chuc-tu-van/search` **Then** trả lỗi `ERR-API-SEARCH-01`

**Cross-ref:** Entity TO_CHUC_TU_VAN, TVV_TO_CHUC, TU_VAN_VIEN, DANH_MUC, DON_VI, BR-DATA-08

---

### FR-XII-07: API Chia sẻ vụ việc (UC177)

**UC Reference:** UC 177
**Source:** Team thiết kế API
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/vu-viec`
**Scope JWT:** `htpldn:vu-viec:read`

**Mô tả:**
API cung cấp danh sách vụ việc TGPL đã hoàn thành/duyệt. Loại trừ thông tin DN nhạy cảm (MST, địa chỉ chi tiết).

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + entity VU_VIEC có dữ liệu publishable.

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | page | number | N | >= 1 | 1 | query param |
| 2 | size | number | N | 1-100 | 20 | query param |
| 3 | linh_vuc_id | number | N | — | — | query param |
| 4 | trang_thai | text | N | HOAN_THANH / DA_DUYET | — | query param |
| 5 | tu_ngay | date | N | — | — | query param |
| 6 | den_ngay | date | N | — | — | query param |

**Processing (Xử lý):**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Xác thực JWT + scope htpldn:vu-viec:read | BR-AUTH-01 |
| 2 | Kiểm tra rate limit | BR-API-01 |
| 3 | Truy vấn vụ việc đã hoàn thành AND cong_khai = 1. Chỉ trả fields whitelist theo BR-PUBLIC-04 | BR-PUBLIC-01, BR-PUBLIC-04 `[CR-01]` |
| 4 | Loại trừ thông tin DN nhạy cảm (MST, địa chỉ, tên DN — xem BR-PUBLIC-04 blacklist) | BR-SEC-01, BR-PUBLIC-04 `[CR-01]` |
| 5 | Áp dụng bộ lọc, phân trang | BR-DATA-08 |
| 6 | Ghi nhật ký thao tác | BR-DATA-05 |

**Outputs (Response Data):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ma_vu_viec | text | luôn | VV-{date}-{seq} |
| 3 | linh_vuc | structured | luôn | {id, ten} |
| 4 | trang_thai | text | luôn | HOAN_THANH / DA_DUYET |
| 5 | don_vi_xu_ly | text | luôn | — |
| 6 | ngay_tiep_nhan | date | luôn | ISO 8601 |
| 7 | ngay_hoan_thanh | date | luôn | ISO 8601 |
| 8 | tieu_de | text | luôn | nguồn `VU_VIEC.tieu_de` `[STT15]` |
| 9 | tom_tat | text | nếu có | nguồn `VU_VIEC.mo_ta_cong_khai` (mô tả công khai đã anonymize DN theo BR-PUBLIC-04) `[STT15]` |
| 10 | ngay_tao | datetime | luôn | ISO 8601 |
| 11 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /vu-viec **When** JWT hợp lệ **Then** trả DS VV đã hoàn thành, KHONG chứa MST DN

**Cross-ref:** Entity VU_VIEC, DOANH_NGHIEP

---

### FR-XII-08: API Tìm kiếm vụ việc (UC178)

**UC Reference:** UC 178
**Source:** Team thiết kế API
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/vu-viec/search`
**Scope JWT:** `htpldn:vu-viec:search`

**Mô tả:**
API tìm kiếm vụ việc theo từ khóa. Loại trừ thông tin nhạy cảm.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs:** keyword (text, Y) + linh_vuc_id + trang_thai + page + size.

**Processing:** Xác thực JWT -> rate limit -> tìm kiếm toàn văn trên lĩnh vực, đơn vị, mã vụ việc -> loại trừ thông tin nhạy cảm -> sắp relevance, phân trang -> ghi log.

**Outputs:** Giống FR-XII-07.

**Error Handling:** Theo TPL-API-FULL + ERR-API-SEARCH-01.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "hợp đồng" **When** search **Then** trả DS VV liên quan đến hợp đồng

**Cross-ref:** Entity VU_VIEC

---

### FR-XII-09: API Chia sẻ đánh giá hiệu quả (UC179)

**UC Reference:** UC 179
**Source:** Team thiết kế API
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/danh-gia`
**Scope JWT:** `htpldn:danh-gia:read`

**Mô tả:**
API cung cấp kết quả đánh giá hiệu quả đã duyệt báo cáo.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + đợt đánh giá đã hoàn thành toàn bộ quy trình: `KE_HOACH_DANH_GIA.trang_thai = HOAN_THANH` AND `BAO_CAO_DANH_GIA.trang_thai = DA_DUYET` (báo cáo tổng hợp đã được Cán bộ Phê duyệt duyệt — đảm bảo consumer không nhận số liệu nháp).

**Inputs:** page + size + ky (text: SO_BO_6_THANG / SO_BO_NAM / TRON_NAM) + don_vi_id.

**Processing:** Xác thực JWT -> rate limit -> truy vấn đợt đánh giá đã duyệt báo cáo -> áp dụng bộ lọc, phân trang -> ghi log.

**Outputs (Response Data):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ten_dot | text | luôn | — |
| 3 | ky | text | luôn | SO_BO_6_THANG / SO_BO_NAM / TRON_NAM |
| 4 | diem_trung_binh | number | luôn | — |
| 5 | so_vu_viec_danh_gia | number | luôn | — |
| 6 | don_vi | text | luôn | — |
| 7 | trang_thai | text | luôn | HOAN_THANH (của KE_HOACH_DANH_GIA) |
| 8 | mau_bao_cao | text | luôn | MAU_21A / MAU_21B (lấy từ BAO_CAO_DANH_GIA — để consumer biết format BC theo TT17/2025) |
| 9 | thoi_gian_duyet_bc | date | luôn | Ngày BAO_CAO_DANH_GIA chuyển sang trạng thái DA_DUYET, ISO 8601 |
| 10 | ngay_tao | datetime | luôn | ISO 8601 |
| 11 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /danh-gia?ky=SO_BO_6_THANG **When** JWT hợp lệ **Then** trả kết quả đánh giá của các đợt đã HOAN_THANH có BC đã DA_DUYET
- **Given** đợt đánh giá ở trạng thái BAO_CAO/CHO_PHE_DUYET (BC chưa duyệt) **When** consumer gọi API **Then** đợt đó KHÔNG xuất hiện trong response

**Cross-ref:** Entity KE_HOACH_DANH_GIA, KET_QUA_DANH_GIA, BAO_CAO_DANH_GIA

---

### FR-XII-10: API Tìm kiếm đánh giá (UC180)

**UC Reference:** UC 180
**Source:** Team thiết kế API
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/danh-gia/search`
**Scope JWT:** `htpldn:danh-gia:search`

**Mô tả:**
API tìm kiếm đợt đánh giá theo từ khóa (tên đợt, đơn vị).

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs:** keyword (text, Y) + ky + don_vi_id + page + size.

**Processing:** Xác thực JWT -> rate limit -> tìm kiếm trên tên đợt, đơn vị -> áp dụng bộ lọc, phân trang -> ghi log.

**Outputs:** Giống FR-XII-09.

**Error Handling:** Theo TPL-API-FULL + ERR-API-SEARCH-01.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "Hà Nội" **When** search **Then** trả DS đánh giá liên quan đến Hà Nội

**Cross-ref:** Entity KE_HOACH_DANH_GIA, BAO_CAO_DANH_GIA

---

### FR-XII-11: API Chia sẻ biểu mẫu (UC181)

**UC Reference:** UC 181
**Source:** Team thiết kế API
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/bieu-mau`
**Scope JWT:** `htpldn:bieu-mau:read`

**Mô tả:**
API cung cấp danh sách biểu mẫu đã duyệt + công khai, kèm URL tải về.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + entity BIEU_MAU có dữ liệu đã duyệt + công khai.

**Inputs:** page + size + linh_vuc_id + dinh_dang (DOC/DOCX/XLS/XLSX). _(API danh sách cơ bản; bộ lọc đa tiêu chí lĩnh vực/cơ quan ban hành/định dạng đặt ở FR-XII-12 `[STT12]`.)_

**Processing:** Xác thực JWT -> rate limit -> truy vấn biểu mẫu đã duyệt + công khai -> áp dụng bộ lọc, phân trang -> ghi log.

**Outputs (Response Data):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ten_bieu_mau | text | luôn | — |
| 3 | linh_vuc | structured | luôn | {id, ten} — nguồn `BIEU_MAU.linh_vuc_id` → DANH_MUC `[STT12]` |
| 4 | co_quan_ban_hanh | structured | luôn | {id, ten} — nguồn `BIEU_MAU.don_vi_id` → DON_VI (đơn vị tạo/sở hữu, hiển thị làm cơ quan ban hành) `[STT12]` |
| 5 | dinh_dang | text | luôn | DOC / DOCX / XLS / XLSX |
| 6 | kich_thuoc | number | luôn | bytes |
| 7 | url_tai_ve | text | luôn | /api/v1/bieu-mau/{id}/download |
| 8 | thoi_gian_dang_tai | date | luôn | ISO 8601 `[CR-01]` |
| 9 | ngay_tao | datetime | luôn | ISO 8601 |
| 10 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /bieu-mau **When** JWT hợp lệ **Then** trả DS biểu mẫu công khai + URL download, mỗi bản ghi kèm `linh_vuc` và `co_quan_ban_hanh` (từ don_vi_id) `[STT12]`

**Cross-ref:** Entity BIEU_MAU, THU_MUC_BIEU_MAU, DON_VI (cơ quan ban hành = BIEU_MAU.don_vi_id)

---

### FR-XII-12: API Tìm kiếm biểu mẫu (UC182)

**UC Reference:** UC 182
**Source:** Team thiết kế API
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/bieu-mau/search`
**Scope JWT:** `htpldn:bieu-mau:search`

**Mô tả:**
API tìm kiếm + lọc đa tiêu chí biểu mẫu phục vụ màn "Biểu mẫu, hợp đồng" trên chuyên trang. Hỗ trợ tìm theo từ khóa (tên biểu mẫu, mô tả) **và/hoặc** lọc theo lĩnh vực, cơ quan ban hành, định dạng. Từ khóa **không bắt buộc** — cho phép lọc thuần theo tiêu chí khi không nhập từ khóa `[STT12]`.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | keyword | text | N | Nếu có nhập: tối thiểu 2 ký tự | — | query param `[STT12]` |
| 2 | linh_vuc_id | number[] | N | Chọn nhiều, FK → DANH_MUC (LINH_VUC_PL) | — | query param `[STT12]` |
| 3 | co_quan_ban_hanh_id | number[] | N | Chọn nhiều, FK → DON_VI (lọc theo BIEU_MAU.don_vi_id) | — | query param `[STT12]` |
| 4 | dinh_dang | text[] | N | Chọn nhiều: DOC/DOCX/XLS/XLSX (Word = DOC+DOCX, Excel = XLS+XLSX) | — | query param `[STT12]` |
| 5 | page | number | N | >= 1 | 1 | query param |
| 6 | size | number | N | 1-100 | 20 | query param |

**Processing:** Xác thực JWT -> rate limit -> nếu có keyword: tìm kiếm toàn văn trên tên biểu mẫu + mô tả; nếu không có keyword: bỏ qua bước tìm toàn văn -> áp bộ lọc đa tiêu chí (linh_vuc_id, co_quan_ban_hanh_id = don_vi_id, dinh_dang — đều chọn nhiều) trên tập biểu mẫu đã duyệt + công khai -> tính `facets` -> sắp xếp (relevance nếu có keyword, ngược lại theo thoi_gian_dang_tai giảm dần), phân trang -> ghi log `[STT12]`.

**Outputs:** Giống FR-XII-11 (gồm `linh_vuc` + `co_quan_ban_hanh`). Bổ sung khối `facets` để dựng dropdown bộ lọc:
- `facets.linh_vuc[]` = {id, ten, count} ← `BIEU_MAU.linh_vuc_id` → DANH_MUC
- `facets.co_quan_ban_hanh[]` = {id, ten, count} ← `BIEU_MAU.don_vi_id` → DON_VI

(Chỉ liệt kê giá trị đang có biểu mẫu công khai. `dinh_dang` là enum cố định Word/Excel — consumer tự dựng, không cần facet.) `[STT12]`

**Error Handling:** Theo TPL-API-FULL. ERR-API-SEARCH-01 chỉ áp khi **có nhập** keyword nhưng < 2 ký tự (keyword bỏ trống là hợp lệ — lọc thuần tiêu chí) `[STT12]`.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "hợp đồng lao động" **When** search **Then** trả DS biểu mẫu matching
- **Given** consumer KHÔNG nhập keyword, chỉ chọn linh_vuc_id=[1,2] + dinh_dang=["DOCX"] **When** gọi API **Then** trả DS biểu mẫu thuộc 2 lĩnh vực + định dạng DOCX, sắp theo thoi_gian_dang_tai giảm dần `[STT12]`
- **Given** consumer chọn co_quan_ban_hanh_id=[X] **When** gọi API **Then** chỉ trả biểu mẫu có don_vi_id = X `[STT12]`
- **Given** consumer gọi API **When** có kết quả **Then** response chứa khối `facets` với danh sách lĩnh vực + cơ quan ban hành kèm count `[STT12]`

**Cross-ref:** Entity BIEU_MAU, DON_VI (cơ quan ban hành = don_vi_id), DANH_MUC (lĩnh vực)

---

### FR-XII-13: API Chia sẻ tư vấn chuyên sâu (UC183)

**UC Reference:** UC 183
**Source:** Team thiết kế API
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/tu-van-chuyen-sau`
**Scope JWT:** `htpldn:tvcs:read`

**Mô tả:**
API cung cấp danh sách tư vấn chuyên sâu đã hoàn thành (metadata + tiêu đề + tóm tắt). Nội dung chi tiết đầy đủ (Nội dung, Kết quả, File tư liệu): xem **FR-XII-21 — API chi tiết TVCS** `[STT11]`.

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + entity TU_VAN_CHUYEN_SAU có dữ liệu trạng thái HOAN_THANH.

**Inputs:** page + size + linh_vuc_id + tu_ngay + den_ngay + don_vi_id (number, N, FK→DON_VI, lọc theo cơ quan tiếp nhận `[CR-06]`).

**Processing:** Xác thực JWT -> rate limit -> truy vấn TVCS đã hoàn thành AND cong_khai = 1 `[CR-01]` -> loại trừ nội dung chi tiết VB tư vấn (chỉ trả metadata) -> áp dụng bộ lọc (lĩnh vực, khoảng ngày, don_vi_id `[CR-06]`), phân trang -> ghi log.

**Outputs (Response Data):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ma_yeu_cau | text | luôn | TVCS-{date}-{seq} |
| 3 | tieu_de | text | luôn | nguồn `TU_VAN_CHUYEN_SAU.tieu_de` `[STT11]` |
| 4 | tom_tat | text | nếu có | nguồn `TU_VAN_CHUYEN_SAU.mo_ta_cong_khai` `[STT11]` |
| 5 | linh_vuc | structured | luôn | {id, ten} |
| 6 | trang_thai | text | luôn | HOAN_THANH |
| 7 | chuyen_gia | text | luôn | — |
| 8 | ngay_hoan_thanh | date | luôn | ISO 8601 |
| 9 | ngay_tao | datetime | luôn | ISO 8601 |
| 10 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /tu-van-chuyen-sau **When** JWT hợp lệ **Then** trả DS TVCS đã hoàn thành (metadata only)

**Cross-ref:** Entity TU_VAN_CHUYEN_SAU

---

### FR-XII-14: API Tìm kiếm tư vấn chuyên sâu (UC184)

**UC Reference:** UC 184
**Source:** Team thiết kế API
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/tu-van-chuyen-sau/search`
**Scope JWT:** `htpldn:tvcs:search`

**Mô tả:**
API tìm kiếm tư vấn chuyên sâu theo từ khóa (lĩnh vực, chuyên gia).

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs:** keyword (text, Y) + linh_vuc_id + don_vi_id (number, N, FK→DON_VI `[CR-06]`) + page + size.

**Processing:** Xác thực JWT -> rate limit -> tìm kiếm trên lĩnh vực, chuyên gia (chỉ bản ghi cong_khai = 1 `[CR-01]`) -> sắp xếp, phân trang -> ghi log.

**Outputs:** Giống FR-XII-13.

**Error Handling:** Theo TPL-API-FULL + ERR-API-SEARCH-01.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "sở hữu trí tuệ" **When** search **Then** trả DS TVCS liên quan

**Cross-ref:** Entity TU_VAN_CHUYEN_SAU

---

### FR-XII-15: API Chia sẻ CT HTPLDN (UC185)

**UC Reference:** UC 185
**Source:** Team thiết kế API
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/chuong-trinh-htpl`
**Scope JWT:** `htpldn:ct-htpl:read`

**Mô tả:**
API cung cấp danh sách chương trình HTPLDN đã công bố (chỉ kế hoạch, KHONG kết quả thực hiện).

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL + entity CHUONG_TRINH_HTPL có dữ liệu trạng thái DA_CONG_BO.

**Inputs:** page + size + don_vi_id + nam (number).

**Processing:** Xác thực JWT -> rate limit -> truy vấn chương trình đã công bố -> chỉ kế hoạch (không kết quả thực hiện) -> áp dụng bộ lọc, phân trang -> ghi log.

**Outputs (Response Data):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ma_ct | text | luôn | CT-{date}-{seq} |
| 3 | ten_ct | text | luôn | — |
| 4 | muc_tieu | text | luôn | — |
| 5 | thoi_gian_bat_dau | date | luôn | ISO 8601 |
| 6 | thoi_gian_ket_thuc | date | luôn | ISO 8601 |
| 7 | don_vi | text | luôn | — |
| 8 | trang_thai | text | luôn | DA_CONG_BO |
| 9 | ngay_tao | datetime | luôn | ISO 8601 |
| 10 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /chuong-trinh-htpl?nam=2026 **When** JWT hợp lệ **Then** trả DS CT đã công bố năm 2026

**Cross-ref:** Entity CHUONG_TRINH_HTPL

---

### FR-XII-16: API Tìm kiếm CT HTPLDN (UC186)

**UC Reference:** UC 186
**Source:** Team thiết kế API
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/chuong-trinh-htpl/search`
**Scope JWT:** `htpldn:ct-htpl:search`

**Mô tả:**
API tìm kiếm chương trình HTPLDN theo từ khóa (tên CT, mục tiêu, đơn vị).

**Tác nhân:** Cổng PLQG (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs:** keyword (text, Y) + don_vi_id + nam + page + size.

**Processing:** Xác thực JWT -> rate limit -> tìm kiếm toàn văn trên tên CT + mục tiêu -> sắp relevance, phân trang -> ghi log.

**Outputs:** Giống FR-XII-15.

**Error Handling:** Theo TPL-API-FULL + ERR-API-SEARCH-01.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "doanh nghiệp nhỏ" **When** search **Then** trả DS CT matching

**Cross-ref:** Entity CHUONG_TRINH_HTPL

---

### FR-XII-17: API Chia sẻ hồ sơ pháp lý DN (UC187)

**UC Reference:** UC 187
**Source:** Fix trùng số UC (Đợt 0, bước 0.7); cập nhật F-11 lượt 6 (2026-05-02) — đặc tả lại đúng entity HO_SO_PHAP_LY_DN (§3.4.3.55), không phải DOANH_NGHIEP
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/ho-so-pl-dn`
**Scope JWT:** `htpldn:ho-so-pl-dn:read`

**Mô tả:**
API cung cấp danh sách **hồ sơ pháp lý của DN** (entity HO_SO_PHAP_LY_DN — gồm các tài liệu pháp lý: GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC) cho hệ thống bên ngoài đồng bộ. Mặc định chỉ trả các hồ sơ còn `trang_thai = 'HIEU_LUC'`. KHÔNG trả thông tin DN (DOANH_NGHIEP entity); chỉ trả `doanh_nghiep_id` để hệ thống consumer tự nối nếu cần.

**Tác nhân:** Hệ thống khác (consumer — qua xác thực JWT + mTLS)

**Preconditions:** Theo TPL-API-FULL.

**Inputs:**

| # | Tên | Kiểu logic | Bắt buộc | Mô tả |
|---|-----|-----------|----------|-------|
| 1 | don_vi_id | identifier | N | Lọc theo đơn vị sở hữu hồ sơ |
| 2 | doanh_nghiep_id | identifier | N | Lọc các hồ sơ của một DN cụ thể |
| 3 | loai_ho_so | text | N | Lọc theo loại: GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC |
| 4 | linh_vuc_id | identifier | N | Lọc theo lĩnh vực pháp luật |
| 5 | tu_ngay_cap | date | N | Lọc theo ngày cấp ≥ |
| 6 | den_ngay_cap | date | N | Lọc theo ngày cấp ≤ |
| 7 | page | number | N | Số trang (mặc định 1) |
| 8 | size | number | N | Cỡ trang (mặc định 50, max 200) |

**Processing:** Xác thực JWT → rate limit (BR-INTG-03) → truy vấn `HO_SO_PHAP_LY_DN` với điều kiện `trang_thai = 'HIEU_LUC'` + áp các tham số lọc → phân trang, sắp theo `ngay_cap` giảm dần → ghi log (consumer_id, endpoint, timestamp, response_code).

**Outputs (Response Data — metadata hồ sơ):**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | id | number | luôn | — |
| 2 | ma_ho_so | text | luôn | HSPL-{YYYYMMDD}-{SEQ} |
| 3 | ten_ho_so | text | luôn | — |
| 4 | loai_ho_so | text | luôn | GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC |
| 5 | linh_vuc_id | identifier | nếu có | FK DANH_MUC |
| 6 | doanh_nghiep_id | identifier | luôn | FK DN (consumer tự nối nếu cần thông tin DN qua API khác) |
| 7 | ngay_cap | date | nếu có | ISO 8601 |
| 8 | ngay_het_han | date | nếu có | ISO 8601 |
| 9 | co_quan_cap | text | nếu có | — |
| 10 | trang_thai | text | luôn | HIEU_LUC (mặc định filter) |
| 11 | ngay_tao | datetime | luôn | ISO 8601 |
| 12 | ngay_cap_nhat | datetime | luôn | ISO 8601 |

**Lưu ý phạm vi và bảo mật:**
- API là kênh **B2G (hệ thống ↔ hệ thống)** với xác thực JWT + mTLS — không phải public-facing cho công chúng/dân
- KHÔNG trả `mo_ta` (text dài) trong response danh sách — tránh payload nặng; nếu cần consumer xem chi tiết, dùng API chi tiết riêng (nếu có)
- KHÔNG trả file đính kèm (giấy phép scan PDF) qua API này — file lưu trên file server riêng, có cơ chế chia sẻ riêng nếu cần
- Mặc định chỉ hồ sơ `trang_thai = 'HIEU_LUC'`; nếu consumer cần xem cả HET_HAN/THU_HOI thì truyền tham số mở rộng (cần CĐT chốt)

**Postconditions:** Theo TPL-API-FULL.
**Error Handling:** Theo TPL-API-FULL.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** trong CSDL có 5 hồ sơ HIEU_LUC + 3 hồ sơ HET_HAN **When** consumer gọi GET /ho-so-pl-dn không kèm filter mở rộng **Then** chỉ trả 5 hồ sơ HIEU_LUC
- **Given** consumer truyền `loai_ho_so = 'GIAY_PHEP'` **When** gọi API **Then** chỉ trả các hồ sơ loại GIAY_PHEP
- **Given** consumer truyền `doanh_nghiep_id = X` **When** gọi API **Then** chỉ trả hồ sơ thuộc DN X
- **Given** consumer gọi API **When** response trả về **Then** KHÔNG chứa cột `mo_ta` hay file đính kèm

**Cross-ref:** Entity HO_SO_PHAP_LY_DN (§3.4.3.55), BR-INTG-02 (mTLS), BR-INTG-03 (rate limit), BR-DATA-05 (audit log)

---

### FR-XII-18: API Tìm kiếm hồ sơ pháp lý DN (UC188)

**UC Reference:** UC 188
**Source:** Fix trùng số UC (Đợt 0, bước 0.7); cập nhật F-11 lượt 6 (2026-05-02) — đặc tả lại đúng entity HO_SO_PHAP_LY_DN
**Priority:** Conditional
**Stability:** Medium
**Endpoint:** `GET /api/v1/ho-so-pl-dn/search`
**Scope JWT:** `htpldn:ho-so-pl-dn:search`

**Mô tả:**
API tìm kiếm **hồ sơ pháp lý của DN** (entity HO_SO_PHAP_LY_DN) theo từ khóa trên `ten_ho_so` và `co_quan_cap`. Mặc định chỉ tìm trong tập hồ sơ `trang_thai = 'HIEU_LUC'`.

**Tác nhân:** Hệ thống khác (consumer)

**Preconditions:** Theo TPL-API-FULL.

**Inputs:**

| # | Tên | Kiểu logic | Bắt buộc | Mô tả |
|---|-----|-----------|----------|-------|
| 1 | keyword | text | Y | Từ khóa tìm kiếm trên ten_ho_so + co_quan_cap |
| 2 | loai_ho_so | text | N | Lọc thêm theo loại |
| 3 | linh_vuc_id | identifier | N | Lọc thêm theo lĩnh vực |
| 4 | doanh_nghiep_id | identifier | N | Lọc thêm theo DN |
| 5 | page | number | N | mặc định 1 |
| 6 | size | number | N | mặc định 50, max 200 |

**Processing:** Xác thực JWT → rate limit → tìm kiếm toàn văn trên `ten_ho_so` và `co_quan_cap` (BR-DATA-08) → áp filter `trang_thai = 'HIEU_LUC'` + các tham số lọc thêm → sắp theo độ liên quan (relevance), phân trang → ghi log.

**Outputs:** Giống FR-XII-17 (cùng cấu trúc metadata hồ sơ).

**Error Handling:** Theo TPL-API-FULL + ERR-API-SEARCH-01.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gửi keyword "Giấy phép kinh doanh" **When** search **Then** trả các hồ sơ có `ten_ho_so` chứa từ khóa, sắp theo relevance
- **Given** consumer gửi keyword + `loai_ho_so = 'HOP_DONG'` **When** search **Then** trả các hợp đồng matching keyword
- **Given** consumer gửi keyword không có kết quả **When** search **Then** trả mảng rỗng + status 200 (không phải 404)

**Cross-ref:** Entity HO_SO_PHAP_LY_DN (§3.4.3.55), BR-DATA-08 (full-text search)

---

### FR-XII-19: API Tiếp nhận hỏi đáp từ Cổng PLQG (UC189 — INBOUND)

**UC Reference:** UC189 (mới — pending CSV transaction bổ sung từ CĐT)
**Source:** Phát sinh từ review FR-02 ngày 2026-05-08 (gap: SRS FR-02 dòng 121 mention `kenh_tiep_nhan = CONG_PLQG` và "API inbound" nhưng chưa có endpoint spec; CHANGELOG dòng 45 và 2556 đã flag gap này từ trước, BA chốt phương án (a) — mở khái niệm INBOUND vào FR-16).
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `POST /api/v1/inbound/hoi-dap`
**Scope JWT:** `htpldn:inbound:hoi-dap:write`

**Mô tả:**
API tiếp nhận câu hỏi/vướng mắc pháp lý của doanh nghiệp được Cổng Pháp luật Quốc gia đẩy về CMS. Câu hỏi được lưu vào HOI_DAP với `kenh_tiep_nhan = CONG_PLQG` + `external_id` (= ID gốc trên Cổng) để CB nghiệp vụ tiếp nhận xử lý theo luồng FR-II-01. Hỗ trợ idempotency: nếu Cổng retry → UPSERT theo `external_id`, không tạo bản ghi trùng lặp.

**Tác nhân:** Cổng Pháp luật Quốc gia (sender, gửi POST request).

**Preconditions:**
- Cổng PLQG có cert mTLS hợp lệ + JWT bearer token với scope `htpldn:inbound:hoi-dap:write`.
- DANH_MUC `LINH_VUC_PL` đã có entry tương ứng với `linh_vuc_id` trong payload.
- DON_VI có entry tương ứng với `don_vi_id` (cơ quan tiếp nhận do DN chọn trên Cổng).

**Inputs (Request Body — JSON):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mô tả |
|---|----------|-----------|----------|-----------|-------|
| 1 | external_id | text | Y | Max 100 ký tự, UNIQUE trên CMS | ID gốc của câu hỏi trên Cổng PLQG. Server dùng để chống duplicate khi retry. |
| 2 | noi_dung | text (long) | Y | Max 5000 ký tự | Nội dung câu hỏi. |
| 3 | linh_vuc_id | identifier | Y | FK → DANH_MUC | Lĩnh vực pháp luật DN chọn trên Cổng. |
| 4 | ten_nguoi_gui | text | N | Max 100 ký tự | Tên người gửi (nếu DN không đăng ký TK). |
| 5 | email_nguoi_gui | text | N | Max 100 ký tự, RFC 5322 | Email người gửi. |
| 6 | sdt_nguoi_gui | text | N | 10-11 chữ số (có thể có "+" đầu) | Số điện thoại người gửi. |
| 7 | doanh_nghiep_id | identifier | N | FK → DOANH_NGHIEP | DN đã đăng ký trên CMS (nếu có). |
| 8 | don_vi_id | identifier | Y | FK → DON_VI | Cơ quan tiếp nhận do DN chọn trên Cổng (mặc định Sở TP tỉnh DN). |
| 9 | muc_do_phuc_tap | text (enum) | N | THUONG / PHUC_TAP. Mặc định THUONG | Phân loại độ phức tạp (CB NV có thể đổi sau khi tiếp nhận). |
| 10 | files_metadata | array | N | Tối đa 10 file. Mỗi item: {filename, size, content_type, presigned_upload_url} | Metadata file đính kèm. File thực được upload qua presigned URL ở bước 2 (xem Processing). |

**Processing (Xử lý):**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Xác thực mTLS cert + verify JWT bearer + scope `htpldn:inbound:hoi-dap:write` | BR-AUTH-01 |
| 2 | Kiểm tra rate limit | BR-API-01 |
| 3 | Validate payload: `external_id` không trống, `noi_dung` ≤ 5000 ký tự, `linh_vuc_id` tồn tại, `don_vi_id` tồn tại | — |
| 4 | **Idempotency check:** SELECT HOI_DAP WHERE `external_id = {input.external_id}`. Nếu đã tồn tại → trả HTTP 200 OK với existing `internal_id` + `received_at`, KHÔNG tạo mới (UPSERT pattern). | — |
| 5 | Nếu chưa tồn tại: INSERT HOI_DAP với `kenh_tiep_nhan = CONG_PLQG`, `external_id = input.external_id`, `trang_thai = MOI`, `muc_do_phuc_tap` = input (mặc định THUONG nếu null), các field khác từ input | BR-DATA-03 |
| 6 | Trả về `internal_id` (HOI_DAP.id) + presigned URL cho từng file metadata để Cổng PLQG upload trực tiếp lên storage CMS (S3-compatible). TTL 1 giờ. | — |
| 7 | Sau khi Cổng PLQG upload file qua presigned URL → ClamAV scan async → cập nhật FILE_DINH_KEM | F-36 |
| 8 | Tính deadline SLA theo `muc_do_phuc_tap` (BR-CALC-03) | BR-CALC-03 |
| 9 | Ghi AUDIT_LOG với consumer_id từ JWT, endpoint, timestamp, response_code, external_id, internal_id | BR-DATA-05 |
| 10 | Gửi thông báo tới CB nghiệp vụ của `don_vi_id` để biết có hỏi đáp mới | — |

**Outputs (Response Body — JSON):**

| # | Tên | Kiểu logic | Điều kiện | Mô tả |
|---|-----|-----------|-----------|-------|
| 1 | internal_id | identifier | luôn | HOI_DAP.id trên CMS |
| 2 | ma_hoi_dap | text | luôn | HD-{date}-{seq} |
| 3 | external_id | text | luôn | Echo lại để Cổng đối soát |
| 4 | received_at | datetime | luôn | Thời điểm CMS nhận, ISO 8601 |
| 5 | upload_urls | array | khi có files_metadata | [{filename, presigned_url, expires_at}] để Cổng upload file |
| 6 | status | text | luôn | "received" (mới) hoặc "already_received" (idempotent retry) |

**Postconditions:**
- HOI_DAP được tạo với `kenh_tiep_nhan = CONG_PLQG` + `external_id` UNIQUE.
- Deadline SLA được tính theo BR-CALC-03.
- AUDIT_LOG ghi đầy đủ.
- Thông báo gửi CB nghiệp vụ của `don_vi_id`.

**Error Handling:** Theo TPL-API-FULL. Bổ sung:

| # | Điều kiện lỗi | Mã lỗi | Phản hồi hệ thống | Severity |
|---|--------------|--------|-------------------|----------|
| E1 | Thiếu external_id | ERR-API-INBOUND-01 | "Trường external_id là bắt buộc" | ERROR (HTTP 400) |
| E2 | Nội dung trống hoặc > 5000 ký tự | ERR-API-INBOUND-02 | "Nội dung câu hỏi phải có và tối đa 5000 ký tự" | ERROR (HTTP 400) |
| E3 | linh_vuc_id không tồn tại trong DANH_MUC | ERR-API-INBOUND-03 | "Lĩnh vực pháp luật không hợp lệ" | ERROR (HTTP 400) |
| E4 | don_vi_id không tồn tại trong DON_VI | ERR-API-INBOUND-04 | "Đơn vị tiếp nhận không hợp lệ" | ERROR (HTTP 400) |
| E5 | external_id đã tồn tại nhưng payload khác (data drift — Cổng gửi cùng external_id với nội dung khác) | ERR-API-INBOUND-05 | "external_id đã được dùng cho bản ghi khác. Không thể UPSERT" | ERROR (HTTP 409) |

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:

- **Given** Cổng PLQG POST `/api/v1/inbound/hoi-dap` với external_id mới + payload hợp lệ **When** mTLS+JWT OK **Then** trả HTTP 201 + `internal_id` + `status="received"` + INSERT HOI_DAP với kenh=CONG_PLQG.
- **Given** Cổng PLQG POST cùng external_id (retry) **When** mTLS+JWT OK **Then** trả HTTP 200 + existing `internal_id` + `status="already_received"`, KHÔNG tạo bản ghi trùng.
- **Given** Cổng PLQG POST cùng external_id nhưng payload khác (vd noi_dung đổi) **When** mTLS+JWT OK **Then** trả HTTP 409 + ERR-API-INBOUND-05.
- **Given** Payload thiếu `external_id` **When** server validate **Then** trả HTTP 400 + ERR-API-INBOUND-01.
- **Given** Payload có `files_metadata` **When** server xử lý OK **Then** response chứa `upload_urls[]` với presigned URL hợp lệ TTL 1 giờ.

**Cross-ref:**
- Entity HOI_DAP — **field `external_id` (mới, UNIQUE, nullable)** đã thêm vào srs-fr-02-hoi-dap.md.
- FR-II-01 Step 6: tham chiếu endpoint này khi `kenh_tiep_nhan = CONG_PLQG`.
- BR-CALC-03: tính deadline SLA theo `muc_do_phuc_tap`.

---

### FR-XII-20: API Xem chi tiết vụ việc (UC177 — get-by-id) `[STT15][STT19]`

**UC Reference:** UC 177 (bổ sung thao tác xem chi tiết — ngoài 2 transaction baseline chia sẻ + tìm kiếm)
**Source:** Issue STT15/STT19 (sheet Bug+API) — chuyên trang cần trang chi tiết vụ việc của DN
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/vu-viec/{id}`
**Scope JWT:** `htpldn:vu-viec:read`

**Mô tả:**
API trả chi tiết đầy đủ một vụ việc cho **doanh nghiệp sở hữu** xem trên chuyên trang. Vì người xem là DN sở hữu nên **KHÔNG ẩn trường** (không áp whitelist BR-PUBLIC-04 vốn dùng cho danh sách công khai); thay vào đó **lọc theo quyền sở hữu** — chỉ trả vụ việc thuộc DN đang đăng nhập.

**Tác nhân:** Cổng PLQG (consumer; truyền định danh DN sau khi DN xác thực VNeID).

**Preconditions:** Theo TPL-API-FULL + vụ việc tồn tại và thuộc DN đang xem.

**Inputs (Request Parameters):**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Nguồn |
|---|----------|-----------|----------|-----------|-------|
| 1 | id | number | Y | PK vụ việc | path param |
| 2 | doanh_nghiep_id | number | Y | Định danh DN đang xem (Cổng truyền sau VNeID) — API kiểm tra `VU_VIEC.doanh_nghiep_id` khớp | header/claim |

**Processing:** Xác thực mTLS+JWT + scope -> kiểm tra rate limit -> truy vấn vụ việc theo `id` -> **kiểm tra quyền sở hữu**: `VU_VIEC.doanh_nghiep_id = input.doanh_nghiep_id`, nếu không khớp → 404 (không lộ tồn tại) -> trả đầy đủ trường (không ẩn) -> ghi log.

**Outputs (Response Data):**

| # | Tên | Nguồn |
|---|-----|-------|
| 1 | id, ma_vu_viec | `VU_VIEC.id`, `.ma_vu_viec` |
| 2 | tieu_de | `VU_VIEC.tieu_de` |
| 3 | linh_vuc {id,ten} | `VU_VIEC.linh_vuc_id` → DANH_MUC |
| 4 | loai_hinh_ho_tro | `VU_VIEC.loai_hinh_ht_id` → DANH_MUC |
| 5 | noi_dung | `VU_VIEC.mo_ta` |
| 6 | ket_qua | `KET_QUA_VU_VIEC.noi_dung` (VB tư vấn PL) + `KET_QUA_VU_VIEC.ket_luan` (tóm tắt) |
| 7 | tai_lieu[] | `VU_VIEC.file_dinh_kem` |
| 8 | don_vi_xu_ly | `VU_VIEC.don_vi_id` → DON_VI.ten_don_vi |
| 9 | trang_thai, ngay_tiep_nhan, ngay_hoan_thanh | `VU_VIEC.*` |
| 10 | ngay_tao, ngay_cap_nhat | `VU_VIEC.created_at`, `.updated_at` |

**Postconditions:** Theo TPL-API-FULL (read-only).
**Error Handling:** Theo TPL-API-FULL. Bổ sung: vụ việc không tồn tại HOẶC không thuộc DN đang xem → HTTP 404.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** DN X gọi GET /vu-viec/{id} với vụ việc thuộc DN X **When** hợp lệ **Then** trả đầy đủ nội dung/kết quả/tài liệu, không ẩn trường
- **Given** DN X gọi GET /vu-viec/{id} với vụ việc của DN Y **When** kiểm tra sở hữu **Then** trả HTTP 404

**Cross-ref:** Entity VU_VIEC, KET_QUA_VU_VIEC, DON_VI, DANH_MUC

---

### FR-XII-21: API Xem chi tiết tư vấn chuyên sâu (UC183 — get-by-id) `[STT9][STT11]`

**UC Reference:** UC 183 (bổ sung thao tác xem chi tiết — ngoài 2 transaction baseline)
**Source:** Issue STT9/STT11 (sheet Bug+API) — chuyên trang cần trang chi tiết TVCS của DN
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/tu-van-chuyen-sau/{id}`
**Scope JWT:** `htpldn:tvcs:read`

**Mô tả:**
API trả chi tiết đầy đủ một yêu cầu tư vấn chuyên sâu cho **doanh nghiệp sở hữu**. Không ẩn trường; lọc theo quyền sở hữu (chỉ trả bản ghi của DN đang xem). File tư liệu pháp luật chỉ trả **sau khi đã công khai** (`cong_khai = 1`).

**Tác nhân:** Cổng PLQG (consumer; truyền định danh DN sau VNeID).

**Preconditions:** Theo TPL-API-FULL + bản ghi TVCS tồn tại và thuộc DN đang xem.

**Inputs:**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Nguồn |
|---|----------|-----------|----------|-----------|-------|
| 1 | id | number | Y | PK TVCS | path param |
| 2 | doanh_nghiep_id | number | Y | Định danh DN đang xem — API kiểm tra `TU_VAN_CHUYEN_SAU.doanh_nghiep_id` khớp | header/claim |

**Processing:** Xác thực mTLS+JWT + scope -> rate limit -> truy vấn TVCS theo `id` -> kiểm tra `TU_VAN_CHUYEN_SAU.doanh_nghiep_id` khớp, không khớp → 404 -> trả đầy đủ trường -> ghi log.

**Outputs (Response Data):**

| # | Tên | Nguồn |
|---|-----|-------|
| 1 | id, ma_yeu_cau | `TU_VAN_CHUYEN_SAU.id`, `.ma_tu_van` |
| 2 | tieu_de | `.tieu_de` |
| 3 | linh_vuc {id,ten} | `.linh_vuc_id` → DANH_MUC |
| 4 | chuyen_gia | `.chuyen_gia_id` → TU_VAN_VIEN.ho_ten |
| 5 | trang_thai, ngay_hoan_thanh | `.trang_thai`, `.ngay_hoan_thanh` |
| 6 | noi_dung | `.noi_dung` |
| 7 | ket_qua | `.ket_qua` (VB TVPL) |
| 8 | file_tu_lieu[] | `.file_dinh_kem_cong_khai` (chỉ trả khi `cong_khai = 1`) `[STT11]` |
| 9 | ngay_tao, ngay_cap_nhat | `TU_VAN_CHUYEN_SAU.created_at`, `.updated_at` |

**Postconditions:** Theo TPL-API-FULL (read-only).
**Error Handling:** Theo TPL-API-FULL. Bổ sung: bản ghi không tồn tại HOẶC không thuộc DN đang xem → HTTP 404.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** DN sở hữu gọi GET /tu-van-chuyen-sau/{id} **When** hợp lệ **Then** trả đầy đủ Nội dung + Kết quả; File tư liệu chỉ có khi bản ghi đã công khai
- **Given** gọi với bản ghi của DN khác **Then** trả HTTP 404

**Cross-ref:** Entity TU_VAN_CHUYEN_SAU, TU_VAN_VIEN, DANH_MUC

---

### FR-XII-24: API Xem chi tiết biểu mẫu (UC181 — get-by-id) `[STT17]`

**UC Reference:** UC 181 (bổ sung thao tác xem chi tiết — ngoài 2 transaction baseline)
**Source:** Issue STT17 (sheet Bug+API) — chuyên trang cần trang xem thông tin/xem trước biểu mẫu (UC CPLQG-VI-166)
**Priority:** Essential
**Stability:** Medium
**Endpoint:** `GET /api/v1/bieu-mau/{id}`
**Scope JWT:** `htpldn:bieu-mau:read`

**Mô tả:**
API trả chi tiết một biểu mẫu công khai, kèm **URL xem trước (preview)**. Biểu mẫu là nội dung công khai (không chứa dữ liệu cá nhân DN) → không lọc sở hữu; chỉ trả bản ghi `cong_khai = 1` AND `trang_thai = CONG_KHAI`.

**Tác nhân:** Cổng PLQG (consumer).

**Preconditions:** Theo TPL-API-FULL + biểu mẫu ở trạng thái công khai.

**Inputs:** `id` (number, Y, PK biểu mẫu — path param).

**Processing:** Xác thực JWT + scope -> rate limit -> truy vấn biểu mẫu theo `id` với điều kiện `cong_khai = 1` AND `trang_thai = CONG_KHAI` -> sinh `preview_url` từ file -> trả response -> ghi log.

**Outputs (Response Data):**

| # | Tên | Nguồn |
|---|-----|-------|
| 1 | id, ten_bieu_mau | `BIEU_MAU.id`, `.ten_bieu_mau` |
| 2 | linh_vuc {id,ten} | `BIEU_MAU.linh_vuc_id` → DANH_MUC |
| 3 | co_quan_ban_hanh {id,ten} | `BIEU_MAU.don_vi_id` → DON_VI.ten_don_vi |
| 4 | dinh_dang, kich_thuoc | `BIEU_MAU.dinh_dang`, `.kich_thuoc` |
| 5 | mo_ta | `BIEU_MAU.mo_ta_cong_khai` |
| 6 | url_tai_ve | `/api/v1/bieu-mau/{id}/download` (từ `.duong_dan_file`) |
| 7 | preview_url | **sinh từ `BIEU_MAU.duong_dan_file`** qua bộ chuyển đổi xem trước (doc→PDF, xls→bảng) — cùng cơ chế preview nội bộ FR-VII `[STT17]` |
| 8 | thoi_gian_dang_tai, so_luot_tai | `BIEU_MAU.*` |
| 9 | ngay_tao, ngay_cap_nhat | `BIEU_MAU.created_at`, `.updated_at` |

**Postconditions:** Theo TPL-API-FULL (read-only).
**Error Handling:** Theo TPL-API-FULL. Bổ sung: biểu mẫu không tồn tại hoặc không công khai → HTTP 404; không hỗ trợ preview định dạng → trả `preview_url = null` + cờ `preview_supported = false`.

**Acceptance Criteria:** Theo TPL-API-FULL. Bổ sung:
- **Given** consumer gọi GET /bieu-mau/{id} với biểu mẫu công khai **When** hợp lệ **Then** trả chi tiết + `preview_url`
- **Given** biểu mẫu chưa công khai **Then** trả HTTP 404

**Cross-ref:** Entity BIEU_MAU, DON_VI, DANH_MUC; cơ chế preview FR-VII (srs-fr-09)

---

---

## 3. Màn hình chức năng

> **Nhom nay khong co man hinh CMS -- chi cung cap API outbound.**
>
> Giám sát API qua:
> - Dashboard (MH-01): thẻ KPI trạng thái API, số request/ngày, tỷ lệ lỗi
> - Công cụ giám sát bên ngoài (Grafana, Prometheus...)
> - AUDIT_LOG: ghi consumer_id, endpoint, timestamp, response_code

---

## 4. Entity liên quan

> **Source of truth:** `srs-v3.md` Section 3.4.

### Tổng quan entity

| # | Entity | Vai trò | Mô tả |
|---|--------|---------|-------|
| 1 | HOI_DAP | referenced | Hỏi đáp/vướng mắc PL (FR-XII-01/02) |
| 2 | KHOA_HOC | referenced | Khóa đào tạo/tập huấn (FR-XII-03/04) |
| 3 | TU_VAN_VIEN | referenced | TVV/CG — cá nhân hành nghề tư vấn (FR-XII-05/06). NHT là cán bộ HTPL DN, lưu ở entity riêng NGUOI_HO_TRO, không xuất qua API nhóm này. |
| 3b | TO_CHUC_TU_VAN | referenced | Tổ chức tư vấn pháp luật tham gia mạng lưới (FR-XII-22/23) `[STT14]` |
| 3c | TVV_TO_CHUC | referenced | Liên kết TVV ↔ Tổ chức tư vấn; nguồn tính `so_luong_tvv_lien_ket` cho FR-XII-22/23 `[STT14]` |
| 4 | VU_VIEC | referenced | Vụ việc HTPL (FR-XII-07/08; **chi tiết FR-XII-20** `[STT15/19]`) |
| 4b | KET_QUA_VU_VIEC | referenced | Kết quả xử lý vụ việc (noi_dung, ket_luan) — nguồn `ket_qua` cho **FR-XII-20** `[STT15/19]` |
| 5 | KE_HOACH_DANH_GIA | referenced | Kế hoạch đánh giá hiệu quả (FR-XII-09/10) |
| 6 | KET_QUA_DANH_GIA | referenced | Kết quả đánh giá chi tiết từng vụ việc (FR-XII-09/10) |
| 6b | BAO_CAO_DANH_GIA | referenced | Báo cáo tổng hợp đợt đánh giá (mẫu 21a/21b TT17/2025), 1:1 với KE_HOACH_DANH_GIA — nguồn dữ liệu chính cho FR-XII-09 |
| 7 | BIEU_MAU | referenced | Biểu mẫu/hợp đồng mẫu (FR-XII-11/12; **chi tiết FR-XII-24** `[STT17]`) |
| 8 | TU_VAN_CHUYEN_SAU | referenced | Nội dung tư vấn chuyên sâu (FR-XII-13/14; **chi tiết FR-XII-21** `[STT9/11]`) |
| 9 | CHUONG_TRINH_HTPL | referenced | Chương trình HTPLDN (FR-XII-15/16) |
| 10 | HO_SO_PHAP_LY_DN | referenced | Hồ sơ pháp lý DN — tài liệu (giấy phép, hợp đồng, giấy chứng nhận, quyết định) (FR-XII-17/18) |
| 11 | DANH_MUC | referenced | Danh mục dùng chung (lĩnh vực PL, bộ lọc) |
| 12 | DON_VI | referenced | Đơn vị — nguồn `don_vi_quan_ly` (Tổ chức tư vấn, FR-XII-22/23), `co_quan_ban_hanh` (biểu mẫu, FR-XII-11/12/24) + `don_vi_xu_ly` (vụ việc) `[STT12][STT14]` |

### ERD nhóm (subset)

> Nhóm XII chỉ READ dữ liệu. ERD thể hiện các entity được expose qua 23 API outbound (20 danh sách/tìm kiếm + 3 xem chi tiết FR-XII-20/21/24; thêm KET_QUA_VU_VIEC + DON_VI cho các API chi tiết).

```mermaid
erDiagram
    HOI_DAP {
        identifier id PK
        text ma_hoi_dap UK
        text tieu_de
        text noi_dung
        text trang_thai
    }
    KHOA_HOC {
        identifier id PK
        text ma_khoa_hoc UK
        text ten_khoa_hoc
        text hinh_thuc
        text trang_thai
    }
    TU_VAN_VIEN {
        identifier id PK
        text ma_tvv UK
        text ho_ten
        text loai_tvv
        text trang_thai
    }
    TO_CHUC_TU_VAN {
        identifier id PK
        text ma_to_chuc UK
        text ten_to_chuc
        text loai_hinh
        boolean cong_khai
        text trang_thai
    }
    TVV_TO_CHUC {
        identifier id PK
        identifier tu_van_vien_id FK
        identifier to_chuc_id FK
        text trang_thai
    }
    VU_VIEC {
        identifier id PK
        text ma_vu_viec UK
        text tieu_de
        text trang_thai
    }
    BIEU_MAU {
        identifier id PK
        text ten_bieu_mau
        text dinh_dang
        boolean cong_khai
        text trang_thai
    }
    TU_VAN_CHUYEN_SAU {
        identifier id PK
        text ma_tu_van UK
        text trang_thai
    }
    CHUONG_TRINH_HTPL {
        identifier id PK
        text ma_chuong_trinh UK
        text ten_chuong_trinh
        text trang_thai
    }
    HO_SO_PHAP_LY_DN {
        identifier id PK
        text ma_ho_so UK
        text ten_ho_so
        text loai_ho_so
        identifier doanh_nghiep_id FK
        text trang_thai
    }
    DANH_MUC {
        identifier id PK
        text loai_danh_muc
        text ma UK
        text ten
    }
    DON_VI {
        identifier id PK
        text ma_don_vi UK
        text ten_don_vi
    }

    HOI_DAP }o--|| DANH_MUC : "linh_vuc_id"
    KHOA_HOC }o--o| DANH_MUC : "linh_vuc_id"
    TU_VAN_VIEN }o--o| TO_CHUC_TU_VAN : "to_chuc_chinh_id"
    TO_CHUC_TU_VAN }o--o{ DANH_MUC : "linh_vuc_ids"
    TO_CHUC_TU_VAN }o--|| DON_VI : "don_vi_id"
    TO_CHUC_TU_VAN ||--o{ TVV_TO_CHUC : "co_tvv"
    TU_VAN_VIEN ||--o{ TVV_TO_CHUC : "tham_gia_to_chuc"
    VU_VIEC }o--|| DANH_MUC : "linh_vuc_id"
    BIEU_MAU }o--o| DANH_MUC : "linh_vuc_id"
    TU_VAN_CHUYEN_SAU }o--|| DANH_MUC : "linh_vuc_id"
    HO_SO_PHAP_LY_DN }o--o| DANH_MUC : "linh_vuc_id"
```

### HOI_DAP (referenced — FR-XII-01/02)

**Mô tả:** Lưu trữ yêu cầu hỏi đáp/vướng mắc pháp lý từ DN. API outbound (FR-XII-01/02) chỉ trả bản ghi đã công khai thành công lên Cổng PLQG (`trang_thai = CONG_KHAI AND cong_khai = true AND is_deleted = false`).

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| ma_hoi_dap | text | Y | UNIQUE | Auto-gen | Mã hỏi đáp |
| tieu_de | text | Y | | | Tiêu đề câu hỏi |
| noi_dung | text (long) | Y | | | Nội dung câu hỏi |
| linh_vuc_id | identifier | Y | FK → DANH_MUC(id) | | Lĩnh vực pháp lý |
| trang_thai | text | Y | CHECK IN (..., 'CONG_KHAI', ...) | 'MOI' | API outbound filter: chỉ trả `CONG_KHAI` (đã đẩy thành công lên Cổng) |
| cong_khai | boolean | N | | 0 | Switch công khai (set 1 khi API outbound thành công) |

### TU_VAN_VIEN (referenced — FR-XII-05/06)

**Mô tả:** Thông tin TVV/CG (cá nhân ngoài hành nghề tư vấn theo NĐ 77/2008). API loại trừ thông tin nhạy cảm (CMND, CCCD, SĐT, địa chỉ). NHT (cán bộ HTPL theo NĐ 55/2019 Đ.7) lưu ở entity riêng NGUOI_HO_TRO, không xuất qua API này.

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| ma_tvv | text | Y | UNIQUE | Auto-gen | Mã TVV |
| ho_ten | text | Y | | | Họ tên đầy đủ |
| loai_tvv | text | Y | CHECK IN ('TVV','CG') | | Loại: TVV (có thẻ NĐ 77/2008 Đ.19) / CG (chuyên gia) |
| trang_thai | text | Y | ... | 'MOI_DANG_KY' | API filter: HOAT_DONG only |

### TO_CHUC_TU_VAN (referenced — FR-XII-22/23)

**Mô tả:** Tổ chức tư vấn pháp luật tham gia mạng lưới hỗ trợ pháp lý cho DNNVV. API chỉ trả tổ chức `trang_thai = HOAT_DONG`, `cong_khai = 1`, `is_deleted = false`; không trả tệp/ghi chú nội bộ.

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| ma_to_chuc | text | Y | UNIQUE | Auto: TC-{DV}-{SEQ} | Mã tổ chức |
| ten_to_chuc | text | Y | | | Tên tổ chức tư vấn |
| loai_hinh | text | Y | CHECK IN ('CONG_TY_LUAT','VP_LUAT_SU','TT_TVPL','KHAC') | | Loại hình tổ chức |
| nguoi_dai_dien | text | Y | | | Họ tên người đại diện |
| so_giay_dkhd | text | Y | Giấy đăng ký hoạt động | | Số giấy ĐKHĐ |
| ngay_cap_dkhd | date | Y | ≤ ngày hiện tại | | Ngày cấp giấy ĐKHĐ |
| dia_chi | text | Y | | | Địa chỉ trụ sở |
| dien_thoai, email, website | text | N | | | Thông tin liên hệ công khai |
| so_qd_cong_bo, ngay_qd_cong_bo | text/date | N | | | Thông tin công bố tham gia mạng lưới |
| so_quyet_dinh_cong_nhan, ngay_cong_nhan | text/datetime | N | | | Quyết định/ngày công nhận theo luồng phê duyệt TC TV |
| don_vi_id | identifier | Y | FK → DON_VI(id) | | Đơn vị/Tỉnh TP quản lý; nguồn filter `don_vi_id[]` |
| linh_vuc_ids | identifier[] | Y | FK → DANH_MUC, N:N | | Lĩnh vực tư vấn |
| trang_thai | text | Y | CHECK IN ('MOI_DANG_KY','CHO_PHE_DUYET','TU_CHOI','HOAT_DONG','TAM_DUNG','VO_HIEU_HOA') | 'MOI_DANG_KY' | API filter: HOAT_DONG only |
| cong_khai | boolean | N | | 0 | API filter: cong_khai = 1 |
| anh_dai_dien | structured | N | jpg/png/gif, max 5MB | Ảnh hệ thống | Ảnh đại diện công khai |
| thoi_gian_dang_tai | datetime | N | Auto fill khi cong_khai=1 | | Thời điểm đăng tải công khai |
| mo_ta_cong_khai | text_long | N | | | Mô tả hiển thị trên chuyên trang |
| file_dinh_kem_cong_khai | file[] | N | PDF/DOC/DOCX/XLS/XLSX, max 20MB/file | | File đã chọn để công khai |

### VU_VIEC (referenced — FR-XII-07/08, 20)

**Mô tả:** Vụ việc HTPL. API loại trừ thông tin DN nhạy cảm (MST, địa chỉ chi tiết).

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| ma_vu_viec | text | Y | UNIQUE | Auto-gen | Mã vụ việc |
| tieu_de | text | Y | | | Tiêu đề vụ việc |
| trang_thai | text | Y | ... | 'CHO_TIEP_NHAN' | API filter: HOAN_THANH/DA_DUYET only |

### BIEU_MAU (referenced — FR-XII-11/12, 22)

**Mô tả:** Biểu mẫu/hợp đồng mẫu (file, max 20MB). API chỉ trả biểu mẫu đã duyệt + công khai.

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| ten_bieu_mau | text | Y | | | Tên biểu mẫu |
| duong_dan_file | text | Y | | | Đường dẫn file |
| dinh_dang | text | N | CHECK IN ('DOC','DOCX','XLS','XLSX') | | Định dạng |
| cong_khai | boolean | N | | 0 | API filter: cong_khai = 1 `[CR-01]` |
| trang_thai | text | Y | CHECK IN ('NHAP','CONG_KHAI','AN') | 'NHAP' | API filter: CONG_KHAI only |

### TU_VAN_CHUYEN_SAU (referenced — FR-XII-13/14, 21)

**Mô tả:** Nội dung tư vấn chuyên sâu. API chỉ trả metadata (không nội dung chi tiết VB tư vấn).

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| ma_tu_van | text | Y | UNIQUE | Auto-gen | Mã yêu cầu TV |
| linh_vuc_id | identifier | Y | FK → DANH_MUC(id) | | Lĩnh vực PL |
| trang_thai | text | Y | ... | 'TIEP_NHAN' | API filter: HOAN_THANH only |

### CHUONG_TRINH_HTPL (referenced — FR-XII-15/16)

**Mô tả:** Chương trình HTPLDN. API chỉ trả kế hoạch đã công bố (không kết quả thực hiện).

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| ma_chuong_trinh | text | Y | UNIQUE | Auto-gen | Mã CT |
| ten_chuong_trinh | text | Y | | | Tên chương trình |
| trang_thai | text | Y | ... | 'DU_THAO' | API filter: DA_CONG_BO only |

### HO_SO_PHAP_LY_DN (referenced — FR-XII-17/18)

**Mô tả:** Hồ sơ pháp lý của DN — tài liệu pháp lý (giấy phép, hợp đồng, giấy chứng nhận, quyết định). API outbound trả metadata hồ sơ; mặc định lọc `trang_thai = 'HIEU_LUC'`.

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| ma_ho_so | text | Y | UNIQUE | Auto-gen | Mã hồ sơ HSPL-{YYYYMMDD}-{SEQ} |
| ten_ho_so | text | Y | | | Tên hồ sơ |
| loai_ho_so | text | Y | CHECK IN ('GIAY_PHEP','HOP_DONG','GIAY_CN','QUYET_DINH','KHAC') | | Loại hồ sơ |
| doanh_nghiep_id | identifier | Y | FK → DOANH_NGHIEP(id) | | DN sở hữu hồ sơ |
| linh_vuc_id | identifier | N | FK → DANH_MUC(id) | | Lĩnh vực pháp luật |
| ngay_cap | date | N | | | Ngày cấp |
| ngay_het_han | date | N | | | Ngày hết hạn |
| co_quan_cap | text | N | | | Cơ quan cấp |
| trang_thai | text | Y | CHECK IN ('HIEU_LUC','HET_HAN','THU_HOI') | 'HIEU_LUC' | Trạng thái hiệu lực — API filter: HIEU_LUC only |

### DANH_MUC (referenced)

**Mô tả:** Bảng danh mục dùng chung — dùng cho bộ lọc API (lĩnh vực, loại DN, v.v.).

| Attribute | Kiểu logic | Bắt buộc | Ràng buộc nghiệp vụ | Mặc định | Mô tả |
|-----------|-----------|----------|------------|---------|-------|
| loai_danh_muc | text | Y | | | Loại DM |
| ma | text | Y | UNIQUE per loai_danh_muc | | Mã danh mục |
| ten | text | Y | | | Tên hiển thị |

---

## 5. State Machine liên quan

> **Source of truth:** `srs-v3.md` Phụ lục C.

Nhóm XII (API Kết nối Chia sẻ Dữ liệu) không có state machine riêng. FR-XII-01~18 và FR-XII-20~24 là read-only outbound (không thay đổi trạng thái dữ liệu); FR-XII-19 là inbound (POST nhận hỏi đáp từ Cổng).

Các API chỉ trả dữ liệu ở trạng thái publishable (đã duyệt / đã công khai / hoàn thành) theo quy tắc BR-INTG-07.

---

## 6. Business Rules liên quan

> **Source of truth:** `srs-v3.md` Phụ lục B.

### Tổng quan BR

| BR ID | Tên | FR áp dụng (nhóm này) |
|-------|-----|----------------------|
| BR-AUTH-01 | Xác thực (JWT) | Tất cả API nhóm XII |
| BR-INTG-02 | Bảo mật API: mTLS + JWT RS256 | Tất cả API nhóm XII |
| BR-INTG-03 | Rate limit: 100 req/min/consumer | Tất cả API nhóm XII |
| BR-INTG-04 | Response time < 3 giây | Tất cả API nhóm XII |
| BR-INTG-07 | Chỉ chia sẻ dữ liệu đã duyệt/công khai | Toàn bộ outbound: FR-XII-01~18, FR-XII-20~24 |
| BR-RETRY-01 | Retry policy API outbound LGSP/Cổng PLQG (3 lần backoff 1s/2s/4s, sau 3 fail → manual_review_queue) | Toàn bộ outbound: FR-XII-01~18, FR-XII-20~24 |
| BR-API-01 | Quy ước API Outbound (mTLS+JWT+rate limit, đồng bộ BR-INTG-02/03) | Toàn bộ outbound: FR-XII-01~18, FR-XII-20~24 |
| BR-SEC-01 | Sanitize PII/dữ liệu nhạy cảm trước khi publish | Toàn bộ outbound: FR-XII-01~18, FR-XII-20~24 |
| BR-DATA-05 | Ghi nhật ký thao tác (audit trail) | Tất cả API nhóm XII |
| BR-DATA-08 | Tìm kiếm toàn văn | FR-XII-02, FR-XII-04, FR-XII-06, FR-XII-08, FR-XII-10, FR-XII-12, FR-XII-14, FR-XII-16, FR-XII-18, FR-XII-23 |

> **3 API xem chi tiết get-by-id (FR-XII-20 vụ việc, FR-XII-21 TVCS, FR-XII-24 biểu mẫu)** kế thừa cùng nhóm BR như API outbound danh sách: BR-AUTH-01, BR-INTG-02, BR-INTG-03, BR-INTG-04, BR-INTG-07, BR-API-01, BR-SEC-01, BR-DATA-05, BR-RETRY-01. **KHÔNG** áp BR-DATA-08 (không phải tìm kiếm toàn văn). Riêng FR-XII-20/21 (nội dung của DN) thay BR-SEC-01 "loại trừ PII" bằng **lọc theo quyền sở hữu** (chỉ trả bản ghi của DN đang xem) `[STT9/11/15/17/19]`.

### BR-AUTH-01: Xác thực (JWT cho API)

| Thuộc tính | Giá trị |
|-----------|---------|
| **Phát biểu** | Consumer phải xác thực qua JWT Bearer token. API verify JWT (RS256, issuer = htpldn.moj.gov.vn), kiểm tra claims: consumer_id, scope, exp |
| **Nguồn** | PRD A6, FR-VIII-20, Architecture AD-05 |
| **Applied in (nhóm XII)** | Tất cả API nhóm XII |

### BR-INTG-02: Bảo mật API — mTLS + JWT

| Thuộc tính | Giá trị |
|-----------|---------|
| **Phát biểu** | Mọi API outbound phải xác thực qua 2 lớp: mTLS + JWT Bearer token RS256. Áp dụng cho kết nối trực tiếp với Cổng PLQG |
| **Nguồn** | Architecture AD-05/06 |
| **Applied in (nhóm XII)** | Tất cả API nhóm XII |
| **Kiểm chứng** | Test invalid JWT = 401 |

### BR-INTG-03: Rate limit

| Thuộc tính | Giá trị |
|-----------|---------|
| **Phát biểu** | 100 requests/phút/consumer |
| **Nguồn** | PRD Section 6.16 |
| **Applied in (nhóm XII)** | Tất cả API nhóm XII (bước 2 mọi API) |
| **Kiểm chứng** | Load test rate limit |

### BR-INTG-04: Response time

| Thuộc tính | Giá trị |
|-----------|---------|
| **Phát biểu** | Response time API < 3 giây |
| **Nguồn** | NFR-01, PRD |
| **Applied in (nhóm XII)** | Tất cả API nhóm XII |
| **Ngoại lệ** | Báo cáo nặng có thể > 3s (async) |

### BR-INTG-07: Chỉ chia sẻ dữ liệu đã duyệt/công khai

| Thuộc tính | Giá trị |
|-----------|---------|
| **Phát biểu** | Chỉ chia sẻ dữ liệu đã duyệt/công khai qua API. Bản ghi draft/chờ duyệt KHÔNG xuất hiện trong API response |
| **Nguồn** | Pattern IP-03/05 |
| **Applied in (nhóm XII)** | Toàn bộ outbound: FR-XII-01~18, FR-XII-20~24 |
| **Kiểm chứng** | Test API filter trạng thái |

### BR-DATA-05: Ghi nhật ký thao tác

| Thuộc tính | Giá trị |
|-----------|---------|
| **Phát biểu** | Mọi API call ghi vào AUDIT_LOG: consumer_id, endpoint, timestamp, response_code |
| **Nguồn** | NFR-06 |
| **Applied in (nhóm XII)** | Tất cả API nhóm XII (bước cuối mọi API) |

### BR-DATA-08: Tìm kiếm toàn văn

| Thuộc tính | Giá trị |
|-----------|---------|
| **Phát biểu** | Hỗ trợ tìm kiếm toàn văn toàn văn |
| **Nguồn** | FR-II-02, FR-X.1-02, FR-X.2-04 |
| **Applied in (nhóm XII)** | FR-XII-02 (hỏi đáp), FR-XII-04 (đào tạo), FR-XII-06 (TVV), FR-XII-08 (vụ việc), FR-XII-10 (đánh giá), FR-XII-12 (biểu mẫu), FR-XII-14 (TVCS), FR-XII-16 (CT HTPL), FR-XII-18 (DN), FR-XII-23 (Tổ chức tư vấn) |

---

**-- Het file FR Group: XII -- API Ket noi Chia se Du lieu --**
