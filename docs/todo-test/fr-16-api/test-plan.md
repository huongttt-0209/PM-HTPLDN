# Kế Hoạch Kiểm Thử — API kết nối Cổng PLQG (FR-16, no UI)

> **Phiên bản**: 1.1 (revised sau review 2026-05-12 12:08:00 — apply G1/G2/G3/G5/G6/G7/G10/G12 + S1/S2/S3/S5/S6/S7)
> **Ngày tạo**: 2026-05-12 11:55:00 · **Ngày revise**: 2026-05-12 12:35:00
> **Nguồn dữ liệu**: SOURCE MODE = **LOCAL** (`input/srs-v3/srs-fr-16-api.md`, `input/quy-trinh-nghiep-vu/02-thu-tu-module.md`, `tasks/system-overview.md §4.19`, `input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md`).
> **SRS Reference**: FR-XII-01 ÷ FR-XII-18 (UC171 ÷ UC190), TPL-API-FULL (đặc tả chung 18 endpoint), KHÔNG có SCR (no UI).
> **Phân nhóm SRS v3.5**: **Nhóm D — SKIP / Smoke 5 phút.** KHÔNG có file `srs-update-2026-5-5/srs-fr-16-*.md` (verify: `ls input/srs-update-2026-5-5/ | grep -i fr-16` → empty). Δ ≈ 0% v3 → v3.5. Test plan này là baseline gốc dùng cho smoke API ping + sample 5-8 endpoint đại diện sau mỗi đợt SRS update các module upstream (FR-02/FR-04/FR-05/FR-06/FR-08/FR-09/FR-12/FR-15).

> **Quy trình:** Theo [scaling-test-strategy.md §4.1 Bước 3](../../../output/scaling-test-strategy.md) — trích BR từ `srs-fr-16-api.md` Phụ lục B + TPL-API-FULL §2a + sibling-check với 9 module upstream (FR-02/FR-03/FR-04/FR-05/FR-08/FR-09/FR-12/FR-15/FR-07) + BA sign-off trước khi viết TC.
>
> **v3.0 (2026-04-23):** GĐ 1 Seed + GĐ 2 Workflow là 2 phase riêng. Cho FR-16, GĐ 1 Seed dùng **upstream entity state cuối** (DA_DUYET / HOAN_THANH / CONG_KHAI / DA_CONG_BO) đã tạo ở 9 module upstream. **Không có "happy path GĐ2"** — toàn bộ TC ở đây là **functional API + auth/security + payload edge + cross-module data isolation**.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Module**: FR-16 API Kết nối Chia sẻ Dữ liệu (Nhóm XII), UC range 171–190, 18 FR outbound + ~8 FR inbound (chưa có SRS detail — xem §1.2 Inbound table).
- **Mục đích**: 18 API outbound expose dữ liệu publishable (đã duyệt/công khai/hoàn thành) cho consumer chính = **Cổng PLQG**, kết nối **REST JSON trực tiếp** (mTLS + JWT, KHÔNG qua LGSP). Inbound endpoint nhận data từ DVC/Cổng PLQG/HT TTHC BTP (event-driven qua LGSP với một số endpoint — xem ambiguity §1.2).
- **Đặc thù**: **KHÔNG có UI / SCR** — test 100% qua curl / Postman / Bruno / integration test. Toàn bộ verify qua HTTP status code + JSON envelope + AUDIT_LOG entry + state filter (BR-INTG-07).
- **Bảng dữ liệu chính**: read-only trên 11 entity upstream (HOI_DAP, KHOA_HOC, TU_VAN_VIEN, VU_VIEC, KE_HOACH_DANH_GIA, KET_QUA_DANH_GIA, BIEU_MAU, NOI_DUNG_TU_VAN_CS, CHUONG_TRINH_HTPL, DOANH_NGHIEP, DANH_MUC) + write vào `AUDIT_LOG`.
- **Màn hình**: **KHÔNG có** (ghi rõ ở §2.4).
- **State machine**: **KHÔNG có** (stateless REST — xem §2.5).

### 1.2 Danh sách FR / UC (18 outbound + 8 inbound)

#### 1.2.1 18 endpoint OUTBOUND (Cổng PLQG đọc từ PM HTPLDN)

> Cite: `srs-v3/srs-fr-16-api.md:31-43` (bảng 9 cặp API) + `srs-v3/srs-fr-16-api.md:149-892` (chi tiết từng FR).

| # | Mã FR | UC | Endpoint | Scope JWT | Source module | Filter state cuối + SRS cite |
|---|-------|----|----------|-----------|---------------|--------------------|
| 1 | FR-XII-01 | UC171 | `GET /api/v1/hoi-dap` | `htpldn:hoi-dap:read` | FR-02 Hỏi đáp | `trang_thai=DA_DUYET` (`srs-fr-16-api.md:168` + `:1010`) |
| 2 | FR-XII-02 | UC172 | `GET /api/v1/hoi-dap/search` | `htpldn:hoi-dap:search` | FR-02 Hỏi đáp | full-text trên DA_DUYET (`srs-fr-16-api.md:230`) |
| 3 | FR-XII-03 | UC173 | `GET /api/v1/dao-tao` | `htpldn:dao-tao:read` | FR-03 Đào tạo | publishable (đang/đã DR, đã duyệt) (`srs-fr-16-api.md:290`) |
| 4 | FR-XII-04 | UC174 | `GET /api/v1/dao-tao/search` | `htpldn:dao-tao:search` | FR-03 Đào tạo | full-text trên KH publishable (`srs-fr-16-api.md:340`) |
| 5 | FR-XII-05 | UC175 | `GET /api/v1/tu-van-vien` | `htpldn:tvv:read` | FR-04 CG/TVV | `trang_thai=HOAT_DONG` v3.5 rename (`srs-fr-16-api.md:395` + `:1021`) |
| 6 | FR-XII-06 | UC176 | `GET /api/v1/tu-van-vien/search` | `htpldn:tvv:search` | FR-04 CG/TVV | full-text trên HOAT_DONG (`srs-fr-16-api.md:415`) |
| 7 | FR-XII-07 | UC177 | `GET /api/v1/vu-viec` | `htpldn:vu-viec:read` | FR-05 Vụ việc | `trang_thai IN (HOAN_THANH, DA_DUYET)` (`srs-fr-16-api.md:461-462`) |
| 8 | FR-XII-08 | UC178 | `GET /api/v1/vu-viec/search` | `htpldn:vu-viec:search` | FR-05 Vụ việc | full-text trên VV publishable (`srs-fr-16-api.md:500`) |
| 9 | FR-XII-09 | UC179 | `GET /api/v1/danh-gia` | `htpldn:danh-gia:read` | FR-08 Đánh giá HQ | `trang_thai=DA_DUYET_BC` (`srs-fr-16-api.md:543` + `:559`) |
| 10 | FR-XII-10 | UC180 | `GET /api/v1/danh-gia/search` | `htpldn:danh-gia:search` | FR-08 Đánh giá HQ | full-text trên đợt đã duyệt (`srs-fr-16-api.md:580`) |
| 11 | FR-XII-11 | UC181 | `GET /api/v1/bieu-mau` | `htpldn:bieu-mau:read` | FR-09 Biểu mẫu | `la_cong_khai=1 AND trang_thai=CONG_KHAI` (`srs-fr-16-api.md:616` + `:1043`) |
| 12 | FR-XII-12 | UC182 | `GET /api/v1/bieu-mau/search` | `htpldn:bieu-mau:search` | FR-09 Biểu mẫu | full-text trên BM công khai (`srs-fr-16-api.md:645`) |
| 13 | FR-XII-13 | UC183 | `GET /api/v1/tu-van-chuyen-sau` | `htpldn:tvcs:read` | FR-12 TVCS | `trang_thai=HOAN_THANH`, **metadata only** (BR-FLOW-07, `srs-fr-16-api.md:685` + `:689` + `:1053`) |
| 14 | FR-XII-14 | UC184 | `GET /api/v1/tu-van-chuyen-sau/search` | `htpldn:tvcs:search` | FR-12 TVCS | full-text TVCS hoàn thành, metadata only (`srs-fr-16-api.md:720`) |
| 15 | FR-XII-15 | UC185 | `GET /api/v1/chuong-trinh-htpl` | `htpldn:ct-htpl:read` | FR-15 CT HTPLDN | `trang_thai=DA_CONG_BO`, KH only (`srs-fr-16-api.md:761` + `:1063`) |
| 16 | FR-XII-16 | UC186 | `GET /api/v1/chuong-trinh-htpl/search` | `htpldn:ct-htpl:search` | FR-15 CT HTPLDN | full-text CT đã công bố (`srs-fr-16-api.md:800`) |
| 17 | FR-XII-17 | UC189 | `GET /api/v1/ho-so-pl-dn` | `htpldn:ho-so-pl-dn:read` | FR-12 → HO_SO_PHAP_LY_DN / FR-07 DN | DN đã công khai (`srs-fr-16-api.md:840`) |
| 18 | FR-XII-18 | UC190 | `GET /api/v1/ho-so-pl-dn/search` | `htpldn:ho-so-pl-dn:search` | FR-12 → HO_SO_PHAP_LY_DN / FR-07 DN | full-text trên DN công khai (`srs-fr-16-api.md:875`) |

> **Bonus endpoint download** (cite `srs-v3/srs-fr-16-api.md:631`): `GET /api/v1/bieu-mau/{id}/download` — trả binary file biểu mẫu (PDF/DOCX/XLSX). KHÔNG có FR-ID riêng nhưng cần test theo TC-OUT-DL-01.

#### 1.2.2 ~8 endpoint INBOUND (DVC / Cổng PLQG / HT TTHC BTP đẩy vào PM HTPLDN)

> Cite: `tasks/system-overview.md:566-571` ("18 endpoint outbound + 8 endpoint inbound"); `input/quy-trinh-nghiep-vu/02-thu-tu-module.md:941` warn "SRS FR-16 không liệt kê chi tiết endpoint inbound — cần CĐT clarify"; `input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md:62-63` ("Cổng PLQG: 18 API REST JSON không qua LGSP" vs "HT TTHC BTP: LGSP event-driven").

| # | Endpoint (suy luận từ flow) | Auth | Source consumer | Trigger nghiệp vụ | SRS ambiguity | Unblock condition |
|---|---------------------------|------|------------------|--------------------|----------------|------------------|
| 1 | `POST /api/v1/vu-viec` (inbound từ DVC) | mTLS + signature LGSP | HT TTHC BTP qua LGSP | DN submit YC TGPL qua DVC → tạo VV state `CHO_TIEP_NHAN` (FR-V.I, UC52) | ⚠️ Format LGSP message envelope chưa có spec | (a) BA confirm LGSP envelope, (b) Dev BE deploy sandbox endpoint, (c) Sample cert + signing key |
| 2 | `POST /api/v1/chi-tra` (inbound từ DVC) | mTLS + signature LGSP | HT TTHC BTP qua LGSP | DN submit HSCT qua DVC → tạo HS state `CHO_TIEP_NHAN` (FR-V.II, UC68) | ⚠️ FR-06 BR ghi "nguồn DUY NHẤT" — verify | (a) BA confirm "DUY NHẤT", (b) sandbox deploy, (c) sample HSCT payload |
| 3 | `POST /api/v1/hoi-dap` (inbound từ Cổng PLQG) | mTLS + JWT | Cổng PLQG (REST trực tiếp) | DN gửi HD qua Cổng → tạo HD state `MOI` (FR-II, UC10 kênh CONG_PLQG) | ⚠️ HOI_DAP entry state — verify với SM-HOIDAP | (a) BA confirm entry state (MOI vs CHO_TIEP_NHAN), (b) sandbox deploy |
| 4 | `POST /api/v1/tu-van-chuyen-sau` (inbound từ Cổng PLQG) | mTLS + JWT | Cổng PLQG | DN gửi YC TVCS → tạo TVCS state `TIEP_NHAN` (FR-12, UC149/UC151) | — | (a) Dev BE deploy sandbox, (b) sample payload TVCS |
| 5 | `POST /api/v1/ho-so-pl-dn` (inbound từ Cổng PLQG) | mTLS + JWT | Cổng PLQG | DN submit HSPL → upsert DN theo MST + tạo HSPL `nguon=CONG_PLQG` (FR-12, UC151) | ⚠️ Upsert logic chưa rõ | (a) BA confirm upsert rule (MST match → update vs duplicate), (b) sandbox deploy |
| 6 | `POST /api/v1/chi-tra/{id}/bo-sung` (FR-V.II-14 v3.5) | mTLS + JWT | Cổng PLQG / DVC | DN bổ sung HSCT khi state `YEU_CAU_BO_SUNG`, max 3 lần | ⚠️ Endpoint path suy luận, chưa có SRS quote | (a) BA confirm path + max 3 lần rule, (b) sandbox deploy |
| 7 | `POST /api/v1/auth/token` (consumer xin JWT) | mTLS only | Cổng PLQG/Consumer | Consumer đổi client cert → JWT Bearer | ⚠️ KHÔNG có trong SRS FR-16; suy luận theo BR-AUTH-01 | (a) Dev BE confirm auth flow (JWT issuance endpoint vs JWKS pull), (b) sample client cert |
| 8 | `POST /api/v1/notifications/cong-khai` (outbound trigger event-driven) | mTLS + JWT | PM HTPLDN → Cổng PLQG | CB NV nhấn "Công khai" trên HD/VV/BM → push notification về index Cổng | ⚠️ Đây là call OUT, không in — re-classify khi BA confirm | (a) BA confirm có cơ chế push event-driven hay không (event bus / webhook / cron polling), (b) Cổng PLQG receiver endpoint URL |

> **⚠️ AMBIGUITY toàn cục cho Inbound**: SRS FR-16 v3 không có section "API Inbound". Verify cần (a) đọc spec LGSP message envelope BA gửi sau, (b) curl POST thử trên dev env, (c) BA confirm số endpoint chính xác (system-overview ghi "~8", có thể 6/7/8). **Mark TC inbound = 🚫 Không test được nhóm B (chờ dev BE spec).** **Unblock gate per endpoint**: cả 3 điều kiện cột "Unblock condition" PHẢI đạt, không được defer vô thời hạn — escalate user lead nếu pending >2 round (theo CLAUDE.md nhóm F).

### 1.3 Tài khoản & role liên quan

> **Đặc thù FR-16**: Consumer là **hệ thống ngoài** (Cổng PLQG, HT TTHC BTP), KHÔNG phải user role trong `input/users.csv`. Mỗi consumer có client certificate (mTLS) + JWT credentials riêng. Tài khoản dưới đây chỉ dùng để **seed upstream data state cuối** để API trả về có data.

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | `qtht_01` (primary) / `qtht_02` (fallback) | Seed JWT consumer credential ở SCR-VIII-04 (nếu có), tạo DM seed (lĩnh vực, loại DN) |
| CB_NV_TW | TW | `cb_nv_tw_01` / `_02` / `_03` | Seed HOI_DAP/VV/TVCS state DA_DUYET ở scope TW (dùng cho `/api/v1/hoi-dap` trả về data ≥1) |
| CB_PD_TW | TW | `cb_pd_tw_01` | Duyệt HD/VV/TVCS lên DA_DUYET (precondition data publishable cho API outbound) |
| CB_NV_DP | ĐP | `cb_nv_dp_01` (AG) / `_02` (BG) | Seed cross-scope data để verify API outbound KHÔNG bị filter theo `don_vi_id` consumer (consumer external = không có don_vi_id) |
| CG/TVV/NHT | — | `huongcg` (CG), `nht_01` (NHT) | Hoàn thành workflow VV/TVCS → state HOAN_THANH cho `/tu-van-chuyen-sau` |
| **Consumer external** | — | **N/A — credential = client cert + JWT (cấp ngoài users.csv)** | Test 18 outbound + 8 inbound theo perspective hệ thống ngoài |

**Consumer credential test setup (preparation 1 lần đầu vòng test):**
- Client certificate test: `cert/consumer-test.crt` + `cert/consumer-test.key` (cấp bởi BE/DevOps trước round)
- JWT test sign tool: `scripts/gen-jwt.sh` (RS256, issuer=`htpldn.moj.gov.vn`, consumer_id=`COTPLQG_TEST_01`, scope=full 18)
- JWT invalid test: signed bằng key khác / hết hạn / scope thiếu / consumer_id sai
- Base URL test: `https://htpldn-dev.moj.gov.vn/api/v1` (hoặc dev env equivalent)

> Reference: [input/users.csv](../../../input/users.csv) · [output/permission-matrix.md](../../../output/permission-matrix.md) (entity row × role col — FR-16 outbound = column "Consumer external = R-only")

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> Cite chính: `srs-v3/srs-fr-16-api.md:1097-1171` (Phụ lục B nhóm XII).

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|---------------------|---------------------|-----------|
| **BR-AUTH-01** | Consumer phải xác thực qua JWT Bearer token. Verify JWT RS256, issuer = `htpldn.moj.gov.vn`, claims: `consumer_id`, `scope`, `exp` | `srs-v3/srs-fr-16-api.md:1113-1119` | ✅ Yes — bước 1 mọi API | — | TC-AUTH-01..04 |
| **BR-INTG-02** | Bảo mật API 2 lớp: **mTLS + JWT Bearer RS256**. Kết nối trực tiếp Cổng PLQG, KHÔNG qua LGSP | `srs-v3/srs-fr-16-api.md:1124-1128` | ✅ Yes | "HT TTHC BTP gửi qua LGSP event-driven" (cite `01-tong-quan-nghiep-vu.md:63`) — riêng inbound `POST /vu-viec` / `/chi-tra` dùng LGSP signature thay JWT | TC-AUTH-05..07 + TC-IN-LGSP-01 |
| **BR-INTG-03** | Rate limit: **100 requests/phút/consumer_id** | `srs-v3/srs-fr-16-api.md:1131-1136` | ✅ Yes — bước 2 mọi API | — | TC-RATE-01..03 |
| **BR-INTG-04** | Response time API < 3 giây | `srs-v3/srs-fr-16-api.md:1139-1146` | ✅ Yes (default) | "Báo cáo nặng có thể > 3s (async)" (`srs-fr-16-api.md:1146`) — KHÔNG áp dụng `/danh-gia` nếu là aggregation lớn | TC-PERF-01..03 |
| **BR-INTG-07** | **Chỉ chia sẻ dữ liệu đã duyệt / công khai** qua API. Bản ghi draft / chờ duyệt KHÔNG xuất hiện trong response | `srs-v3/srs-fr-16-api.md:1148-1155` | ✅ Yes | — | TC-FILTER-01..09 (mỗi endpoint 1 TC verify state filter) |
| **BR-DATA-05** | Audit trail: mọi API call ghi vào `AUDIT_LOG`: `consumer_id, endpoint, timestamp, response_code, http_method, latency_ms` | `srs-v3/srs-fr-16-api.md:1157-1163` | ✅ Yes — bước cuối mọi API | — | TC-AUDIT-01..03 |
| **BR-DATA-08** | Tìm kiếm toàn văn (full-text), pagination default 20, max 100 | `srs-v3/srs-fr-16-api.md:1165-1171` | ✅ Yes cho 9 endpoint search (FR-XII-02/04/06/08/10/12/14/16/18) | — | TC-SEARCH-01..05 |
| **BR-SEC-01** | Loại trừ thông tin nhạy cảm khỏi response: CMND/CCCD/SĐT/địa chỉ cá nhân (TVV), MST/địa chỉ chi tiết DN (VV) | `srs-v3/srs-fr-16-api.md:381` (TVV) + `:472` (VV) | ✅ Yes (chỉ TVV + VV) | — | TC-SEC-01..03 |
| **BR-FLOW-07** | TVCS API chỉ trả **metadata**, KHÔNG có nội dung VB chi tiết tư vấn. Tư liệu pháp lý đính kèm TVCS có thể "công khai ngay" không cần phê duyệt thêm | `srs-v3/srs-fr-16-api.md:685` + `01-tong-quan-nghiep-vu.md:173` | ✅ Yes (chỉ FR-XII-13/14) | — | TC-OUT-TVCS-01 + TC-OUT-TVCS-02 |
| **BR-API-PAG-01** | Pagination: `?page=1&size=20`, default size=20, max size=100. `page >= 1`. Vượt max → ERR-API-400 | `srs-v3/srs-fr-16-api.md:74` + `:166` + `:179` | ✅ Yes | — | TC-PAG-01..03 |
| **BR-API-FMT-01** | Response envelope chuẩn: `{success, data, pagination{page,size,total_elements,total_pages}, timestamp}` | `srs-v3/srs-fr-16-api.md:90-103` | ✅ Yes | — | TC-FMT-01..02 |
| **BR-API-ERR-01** | Error envelope: `{success: false, error: {code, message, details}}` với 7 mã ERR-API-{400/401/403/404/429/500/503} | `srs-v3/srs-fr-16-api.md:75` + `:120-128` | ✅ Yes | — | TC-ERR-01..07 |

### 2.2 Error Codes

> Cite: `srs-v3/srs-fr-16-api.md:120-128` (chung TPL-API-FULL) + `:249` (search-specific).

| Mã lỗi | HTTP | Điều kiện trigger | Message (SRS-quoted) | Severity |
|--------|------|-------------------|----------------------|----------|
| ERR-API-400 | 400 | Tham số request không hợp lệ | "Tham số không hợp lệ: {chi tiết}" | ERROR |
| ERR-API-401 | 401 | JWT không hợp lệ / hết hạn / thiếu | "Xác thực thất bại. JWT không hợp lệ hoặc hết hạn" | ERROR |
| ERR-API-403 | 403 | JWT scope không đủ quyền | "Không có quyền truy cập API này. Yêu cầu scope: {scope}" | ERROR |
| ERR-API-404 | 404 | Resource không tồn tại / đã xóa | "Không tìm thấy tài nguyên" | ERROR |
| ERR-API-429 | 429 | Vượt rate limit (100 req/min/consumer) | "Vượt giới hạn tần suất. Thử lại sau {retry_after}s" | WARNING |
| ERR-API-500 | 500 | Lỗi server nội bộ | "Lỗi hệ thống nội bộ. Vui lòng thử lại sau" | ERROR |
| ERR-API-503 | 503 | PM không khả dụng / đang bảo trì | "Dịch vụ tạm thời không khả dụng. Thử lại sau" | ERROR |
| ERR-API-SEARCH-01 | 400 | Từ khóa search trống hoặc < 2 ký tự | "Từ khóa tìm kiếm phải có ít nhất 2 ký tự" | ERROR |

> ⚠️ Message phải quote **nguyên văn**. Khi test negative, expected message match exact → không "close enough" accept. Header `Retry-After` BẮT BUỘC ở response 429 và 503 (verify trong TC-RATE-02 + TC-ENV-01).

### 2.3 Permission Matrix (module-specific)

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md). FR-16 đặc thù: consumer là hệ thống ngoài, không phải role nội bộ. Permission qua **JWT scope**, không qua RBAC nội bộ.

| Entity / Action | QTHT (nội bộ) | CB_NV/PD (nội bộ) | DN | **Consumer Cổng PLQG** (JWT scope) |
|-----------------|:--:|:--:|:--:|:--:|
| HOI_DAP API outbound | — | — | — | R nếu `htpldn:hoi-dap:read` |
| TU_VAN_VIEN API outbound | — | — | — | R nếu `htpldn:tvv:read`, exclude PII |
| VU_VIEC API outbound | — | — | — | R nếu `htpldn:vu-viec:read`, exclude MST DN |
| NOI_DUNG_TU_VAN_CS API outbound | — | — | — | R metadata-only nếu `htpldn:tvcs:read` |
| BIEU_MAU download | — | — | — | R nếu `htpldn:bieu-mau:read` + `la_cong_khai=1` |
| AUDIT_LOG entry write | system | system | — | system auto |
| **Inbound POST** (LGSP/Cổng) | — | — | — | W nếu mTLS valid + LGSP signature OR JWT scope `:write` |

**Permission BR áp dụng:**
- BR-AUTH-08 phân quyền dữ liệu theo `don_vi_id` **KHÔNG áp dụng cho FR-16** vì consumer external KHÔNG có `don_vi_id`. API outbound trả toàn bộ data publishable cross-don_vi (BR-INTG-07).
- BR-AUTH-11 lọc data DN theo chính DN **KHÔNG áp dụng** vì DN không trực tiếp call FR-16 API.

### 2.4 UI Layout — **KHÔNG CÓ UI**

> ⚠️ **FR-16 KHÔNG có màn hình CMS / SCR.** Cite `srs-v3/srs-fr-16-api.md:897-905`:
>
> > "Nhom nay khong co man hinh CMS — chi cung cap API outbound. Giam sat API qua: Dashboard (MH-01) the KPI trang thai API, so request/ngay, ty le loi / Cong cu giam sat ben ngoai (Grafana, Prometheus...) / AUDIT_LOG: ghi consumer_id, endpoint, timestamp, response_code."

**Cách test không UI:**
- **Tool**: curl / Postman / Bruno / pytest+requests / k6 (load test rate limit). KHÔNG dùng Chrome DevTools MCP.
- **Verify response**: HTTP status code + JSON envelope theo BR-API-FMT-01 / BR-API-ERR-01.
- **Verify side-effect**: query `AUDIT_LOG` table qua API admin (`GET /api/admin/audit-log?consumer_id=...&endpoint=...`) hoặc DB nếu có quyền.
- **Verify negative**: invalid JWT → 401; missing scope → 403; vượt rate → 429.
- **Verify performance**: response time < 3s (BR-INTG-04), p95 nhỏ hơn ngưỡng SLA.

**Document API endpoint thay vì layout:**
- Mỗi endpoint document = (Method + Path + Auth + Scope + Request schema + Response schema + Error matrix) trong TC dưới §3-4.
- Reference OpenAPI/Swagger spec nếu BE cung cấp (chưa thấy file `swagger.yaml` trong repo — TODO BA/Dev BE).

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**
- ☐ Authorization Bearer JWT mọi request (BR-AUTH-01)
- ☐ mTLS handshake mọi connection (BR-INTG-02)
- ☐ Rate limit 100/min/consumer (BR-INTG-03)
- ☐ Response time < 3s (BR-INTG-04)
- ☐ Pagination default 20, max 100 (BR-DATA-07 / BR-API-PAG-01)
- ☐ Audit log mọi call (BR-DATA-05)
- ☐ State filter publishable only (BR-INTG-07)

**Tooling matrix (S2) — assign tool theo loại TC:**

| Loại TC | Tool ưu tiên | Lý do |
|---------|--------------|-------|
| TC-OUT-* (functional 9 outbound) | `curl + jq` script trong `scripts/qa-fr16/` | Verify HTTP status + envelope shape + field whitelist nhanh |
| TC-AUTH-* (9 TC JWT/mTLS) | `curl --cert/--key` + `scripts/gen-jwt.sh` để generate JWT variant | Cần control fine-grained issuer/algorithm/claim/exp |
| TC-RATE-* (4 TC rate limit) | `k6` (load script) | Cần đẩy 105 req/60s — curl loop không reliable |
| TC-PERF-* (3 TC performance) | `k6` (concurrent VU profile) | Đo p95/p99, concurrent 50 consumer cần load tool |
| TC-PAG-* / TC-SEARCH-* / TC-DATE-* (12a/b) | `curl + jq` | Edge negative đơn lẻ |
| TC-AUDIT-* (4 TC audit log) | `curl` + `psql` hoặc `GET /api/admin/audit-log` (nếu BE expose) | Cần query DB hoặc admin API sau call |
| TC-FILTER-* (9 TC state filter) | `pytest + requests` với fixture pre-seed | Cần pre-seed mix state (draft + DA_DUYET) rồi assert response shape |
| TC-IN-* (8 inbound BLOCKED) | TBD khi unblock | Postman collection / pytest tùy spec LGSP envelope |
| Regression suite (toàn bộ 59 TC) | `Bruno collection` (export JSON) | Re-run mỗi đợt SRS upstream update |

**Feature KHÔNG có (giải thích với SRS quote):**
- KHÔNG có Excel export (BR-DATA-06 không áp dụng — consumer tự pagination JSON nếu cần bulk download)
- KHÔNG có CRUD UI / Drawer / Modal (cite `srs-fr-16-api.md:897`)
- KHÔNG có state machine (cite `srs-fr-16-api.md:1091-1093`)

### 2.5 State Machine — **KHÔNG CÓ (stateless REST)**

> Cite `srs-v3/srs-fr-16-api.md:1091-1093`:
>
> > "Nhom XII (API Ket noi Chia se Du lieu) khong co state machine rieng. Tat ca 18 API deu la read-only outbound, khong thay doi trang thai du lieu. Cac API chi tra du lieu o trang thai publishable (da duyet / da cong khai / hoan thanh) theo quy tac BR-INTG-07."

API stateless. Read filter theo state CUỐI của entity upstream. **State filter table:**

| Endpoint | Entity | State filter (cite SRS) |
|----------|--------|---------------------------|
| `/hoi-dap` | HOI_DAP | `trang_thai=DA_DUYET` (`srs-fr-16-api.md:168` + `:1010`) |
| `/tu-van-vien` | TU_VAN_VIEN | `trang_thai=HOAT_DONG` (v3.5 rename, `srs-fr-16-api.md:395` + `:1021`) |
| `/vu-viec` | VU_VIEC | `trang_thai IN (HOAN_THANH, DA_DUYET)` (`srs-fr-16-api.md:461-462`) |
| `/dao-tao` | KHOA_HOC | publishable: `DANG_DIEN_RA / KET_THUC / DA_DUYET` (`srs-fr-16-api.md:290`) |
| `/danh-gia` | DOT_DANH_GIA | `trang_thai=DA_DUYET_BC` (`srs-fr-16-api.md:543` + `:559`) |
| `/bieu-mau` | BIEU_MAU | `la_cong_khai=1 AND trang_thai=CONG_KHAI` (`srs-fr-16-api.md:616` + `:1043`) |
| `/tu-van-chuyen-sau` | NOI_DUNG_TU_VAN_CS | `trang_thai=HOAN_THANH` metadata-only (`srs-fr-16-api.md:689` + `:1053`) |
| `/chuong-trinh-htpl` | CHUONG_TRINH_HTPL | `trang_thai=DA_CONG_BO` (`srs-fr-16-api.md:761` + `:1063`) |
| `/ho-so-pl-dn` | DOANH_NGHIEP / HO_SO_PHAP_LY_DN | DN đã công khai |

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| **GĐ 1 Seed** (upstream entity state cuối) | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | 9 entity variants — `hoi_dap_variants`, `khoa_hoc_variants`, `tu_van_vien_variants`, `vu_viec_variants`, ... |
| **GĐ 1 click flow** (push state cuối) | [`input/flow-module.md`](../../../input/flow-module.md) | §FR-02/03/04/05/08/09/12/15 Bước duyệt → state DA_DUYET/CONG_KHAI/HOAN_THANH |
| **GĐ 2 Workflow** | N/A | FR-16 KHÔNG có workflow stateful — bỏ phase này |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | 9 entity × "Tạo tại module X / Đọc tại FR-16 API" |

**Upstream dependencies (Tier check):**

| Endpoint của FR-16 | Tier | Phụ thuộc entity (upstream) | Seed trước tại module (S4 hyperlink) |
|-------------------|:----:|----------------------------------|-----------------------|
| `/hoi-dap` | 5 | HOI_DAP DA_DUYET ≥ 5 record + 2-3 record state khác (MOI/CHO_DUYET) để verify filter | [FR-02 Hỏi đáp](../fr-02-hoi-dap/test-plan.md) (sau khi CB PD duyệt) |
| `/tu-van-vien` | 5 | TU_VAN_VIEN HOAT_DONG ≥ 5 record (đủ TVV/CG/NHT mix) + 2 record `KHOI_TAO/KHOA` | [FR-04 CG/TVV](../fr-04-chuyen-gia-tvv/test-plan.md) (sau khi CB PD duyệt + cong_khai=1) |
| `/vu-viec` | 5 | VU_VIEC HOAN_THANH ≥ 5 record + 2 record draft/từ chối | [FR-05 Vụ việc](../fr-05-vu-viec/test-plan.md) (sau khi hoàn tất workflow 9 bước) |
| `/dao-tao` | 5 | KHOA_HOC publishable ≥ 3 record + 2 record `KHOI_TAO/HUY` | [FR-03 Đào tạo](../fr-03-dao-tao/test-plan.md) (sau khi tạo + duyệt KH) |
| `/danh-gia` | 5 | DOT_DANH_GIA DA_DUYET_BC ≥ 1 record + 1 đợt `DANG_THUC_HIEN` | [FR-08 Đánh giá HQ](../fr-08-danh-gia-hq/test-plan.md) (sau khi hoàn tất đợt + duyệt báo cáo) |
| `/bieu-mau` | 5 | BIEU_MAU la_cong_khai=1 ≥ 3 record + 2 record `la_cong_khai=0` | [FR-09 Biểu mẫu](../fr-09-bieu-mau/test-plan.md) (sau khi upload + toggle Công khai) |
| `/tu-van-chuyen-sau` | 5 | NOI_DUNG_TU_VAN_CS HOAN_THANH ≥ 3 record + 1 record `DANG_THUC_HIEN` | [FR-12 TVCS](../fr-12-tv-chuyen-sau/test-plan.md) (sau khi CG hoàn thành + CB PD duyệt) |
| `/chuong-trinh-htpl` | 5 | CHUONG_TRINH_HTPL DA_CONG_BO ≥ 1 record + 1 record `KHOI_TAO/HUY` | [FR-15 CT HTPLDN](../fr-15-ct-htpldn/test-plan.md) (sau khi công bố KH) |
| `/ho-so-pl-dn` | 5 | DOANH_NGHIEP công khai ≥ 5 + HO_SO_PHAP_LY_DN HIEU_LUC ≥ 3 + 1 DN chưa công khai | [FR-07 Doanh nghiệp](../fr-07-doanh-nghiep/test-plan.md) + [FR-12 TVCS](../fr-12-tv-chuyen-sau/test-plan.md) |

> **Lưu ý**: FR-16 là Tier 5 cao nhất — chạy SAU CÙNG. Mọi 9 module upstream phải có data state cuối seeded. Acceptance gate cho mỗi endpoint: `verify API trả ≥1 record với JWT valid + filter mặc định`.

---

## 3. Cấu Trúc File Test Case

**TC ID prefix convention (S1):** File 01-09 outbound → `TC-OUT-<entity>-NN`. File 10 auth → `TC-AUTH-NN`. File 11 rate → `TC-RATE-NN`. File 11b perf → `TC-PERF-NN`. File 12 payload → `TC-PAG-NN` / `TC-SEARCH-NN` / `TC-DATE-NN`. File 13 audit → `TC-AUDIT-NN`. File 13b filter → `TC-FILTER-NN`. File 14 inbound → `TC-IN-NN`. Tester grep cross-report theo prefix dễ hơn.

```
fr-16-api/
├── test-plan.md                            ← File này
├── 01-TC-OUTBOUND-hoi-dap.md               ← FR-XII-01/02 (3 TC: list + search + PII-not-applicable)
├── 02-TC-OUTBOUND-dao-tao.md               ← FR-XII-03/04 (3 TC: list + search + draft-exclude)
├── 03-TC-OUTBOUND-tu-van-vien.md           ← FR-XII-05/06 (3 TC: list + search + PII exclude BR-SEC-01)
├── 04-TC-OUTBOUND-vu-viec.md               ← FR-XII-07/08 (3 TC: list + search + MST exclude)
├── 05-TC-OUTBOUND-danh-gia.md              ← FR-XII-09/10 (3 TC: list + search + KQDG-leak-check S9)
├── 06-TC-OUTBOUND-bieu-mau.md              ← FR-XII-11/12 + download (5 TC: list + search + la_cong_khai=0 hide + download integrity + download scope)
├── 07-TC-OUTBOUND-tvcs.md                  ← FR-XII-13/14 (3 TC: list + search + metadata-only field whitelist)
├── 08-TC-OUTBOUND-ct-htpl.md               ← FR-XII-15/16 (3 TC: list + search + KQ-exclude)
├── 09-TC-OUTBOUND-ho-so-pl-dn.md           ← FR-XII-17/18 (3 TC: list + search + DN-not-cong-khai-exclude)
├── 10-TC-AUTH-jwt-mtls.md                  ← 9 auth TC (1 happy issuance + 8 negative)
├── 11a-TC-RATE-LIMIT.md                    ← 4 rate limit TC (happy + 429 + reset window + scope)
├── 11b-TC-PERFORMANCE.md                   ← 3 perf TC (p95 list + concurrent + search latency)
├── 12a-TC-PAYLOAD-pagination-search.md     ← 8 payload edge TC (pagination boundary + search edge)
├── 12b-TC-PAYLOAD-date-range.md            ← 2 date range edge TC
├── 13a-TC-AUDIT.md                         ← 4 audit log TC (happy INSERT + error path + consumer_id verify + latency_ms field check)
├── 13b-TC-FILTER-state.md                  ← 9 filter TC (BR-INTG-07 mỗi endpoint 1 TC verify draft/chờ duyệt KHÔNG hiện)
├── 14-TC-INBOUND-FROM-CONG-DVC.md          ← 8 inbound TC (BLOCKED — chờ BE spec, ghi 🚫)
└── (15-REVIEW-edge-case-hunter.md)         ← Optional review
```

---

## 4. Tổng Quan Số Lượng Test Cases (revised v1.1)

| File | Happy | Negative | Edge | Tổng | Priority |
|------|-------|----------|------|------|----------|
| 01 Outbound `/hoi-dap` | TC-OUT-HD-01 (list), TC-OUT-HD-02 (search) | TC-OUT-HD-03 (no PII personal data) | — | 3 | P0×3 |
| 02 Outbound `/dao-tao` | TC-OUT-DT-01, TC-OUT-DT-02 | TC-OUT-DT-03 (`KHOI_TAO` KH không hiện) | — | 3 | P0×2 + P1×1 |
| 03 Outbound `/tu-van-vien` | TC-OUT-TVV-01, TC-OUT-TVV-02 | TC-OUT-TVV-03 (BR-SEC-01 exclude `cmnd/cccd/sdt/dia_chi_ca_nhan`) | — | 3 | P0×3 |
| 04 Outbound `/vu-viec` | TC-OUT-VV-01, TC-OUT-VV-02 | TC-OUT-VV-03 (exclude `mst_dn/dia_chi_chi_tiet_dn`) | — | 3 | P0×3 |
| 05 Outbound `/danh-gia` | TC-OUT-DG-01 (list aggregate), TC-OUT-DG-02 (search) | TC-OUT-DG-03 (KHÔNG leak `KET_QUA_DANH_GIA` per-VV detail — S9) | — | 3 | P0×1 + P1×2 |
| 06 Outbound `/bieu-mau` + download | TC-OUT-BM-01 (list), TC-OUT-BM-02 (search), TC-OUT-BM-DL-01 (download OK) | TC-OUT-BM-03 (`la_cong_khai=0` không hiện), TC-OUT-BM-DL-02 (file integrity binary diff vs `kich_thuoc`) | — | 5 | P0×3 + P1×2 |
| 07 Outbound `/tu-van-chuyen-sau` | TC-OUT-TVCS-01, TC-OUT-TVCS-02 | TC-OUT-TVCS-03 (whitelist 6 field metadata, blacklist `noi_dung_chi_tiet`) | — | 3 | P0×3 |
| 08 Outbound `/chuong-trinh-htpl` | TC-OUT-CT-01, TC-OUT-CT-02 | TC-OUT-CT-03 (KH only, KHÔNG kết quả `dot_thuc_hien[]` detail) | — | 3 | P1×3 |
| 09 Outbound `/ho-so-pl-dn` | TC-OUT-DN-01, TC-OUT-DN-02 | TC-OUT-DN-03 (DN chưa công khai không hiện) | — | 3 | P1×3 |
| 10 Auth (JWT/mTLS) | TC-AUTH-00 (cấp JWT happy — S5 promote P0 prereq) | TC-AUTH-01 (no JWT → 401), TC-AUTH-02 (expired → 401), TC-AUTH-03 (sig sai → 401), TC-AUTH-04 (scope thiếu → 403), TC-AUTH-05 (mTLS cert sai → handshake fail), TC-AUTH-06 (issuer sai → 401 — G2), TC-AUTH-07 (algorithm HS256 thay RS256 → 401 — G2), TC-AUTH-08 (missing claim `consumer_id`/`exp` → 401 — G2) | — | 9 | P0×9 |
| 11a Rate limit | TC-RATE-01 (100 req/min OK) | TC-RATE-02 (req 101 → 429 + Retry-After), TC-RATE-03 (reset window — chờ Retry-After s rồi retry OK — G8), TC-RATE-04 (scope per-consumer vs per-endpoint — G8) | — | 4 | P0×2 + P1×2 |
| 11b Performance | — | TC-PERF-01 (p95 list < 3s), TC-PERF-02 (concurrent 50 consumer × 2 req/s — G7), TC-PERF-03 (search p99 < 5s — G7) | — | 3 | P1×3 |
| 12a Payload pagination + search | — | TC-PAG-01 (page=0 → 400), TC-PAG-02 (size=101 → cap 100 hoặc 400), TC-PAG-04 (page=-1 → 400 — G9), TC-PAG-05 (size=0 → 400 — G9), TC-PAG-06 (page=999999 vượt total → empty data — G9), TC-PAG-07 (default `?page` `?size` thiếu → 1+20 — G9), TC-SEARCH-01 (keyword="" → ERR-API-SEARCH-01), TC-SEARCH-02 (keyword=1 ký tự → 400) | TC-PAG-03 (size=100 boundary OK) | 9 | P1×9 |
| 12b Payload date range | — | TC-DATE-01 (`tu_ngay > den_ngay` → 400) | TC-DATE-02 (tu_ngay = den_ngay boundary OK) | 2 | P2×2 |
| 13a Audit log | TC-AUDIT-01 (INSERT row sau 200 OK) | TC-AUDIT-02 (INSERT row sau 401/403/429/500 — G6), TC-AUDIT-03 (consumer_id chính xác, không null khi JWT invalid — G6), TC-AUDIT-04 (verify field `latency_ms` có giá trị — G6 + check fixture vs SRS) | — | 4 | P0×4 |
| 13b Filter state BR-INTG-07 | — | TC-FILTER-01 `/hoi-dap` (MOI/CHO_DUYET hide — G5), TC-FILTER-02 `/dao-tao` (KH `KHOI_TAO/HUY` hide), TC-FILTER-03 `/tu-van-vien` (TVV `KHOI_TAO/KHOA` hide), TC-FILTER-04 `/vu-viec` (VV draft/từ chối hide), TC-FILTER-05 `/danh-gia` (đợt `DANG_THUC_HIEN` hide), TC-FILTER-06 `/bieu-mau` (`la_cong_khai=0` + `trang_thai≠CONG_KHAI` hide), TC-FILTER-07 `/tvcs` (TVCS chưa HOAN_THANH hide), TC-FILTER-08 `/ct-htpl` (CT chưa DA_CONG_BO hide), TC-FILTER-09 `/ho-so-pl-dn` (DN chưa công khai hide) | — | 9 | P0×9 |
| 14 Inbound 8 endpoint | — | TC-IN-01..08 (8 placeholder — BLOCKED 🚫 nhóm B chờ BE spec) | — | 8 | P2×8 (defer) |
| **TỔNG** | **18** | **47** | **2** | **67 TC** | (xem dưới) |

> **Note**: 14-TC-INBOUND-* mark P2 + Status 🚫 trong functional report — defer cho đến khi 3 unblock condition đạt (BA confirm + sandbox deploy + sample cert). Tổng "live testable" round 1 = 67 - 8 (inbound block) = **59 TC test được round này** (nếu mTLS sandbox + JWT cấp xong).

**Phân bổ priority (revised v1.1):**

| Priority | Số TC | % | Ghi chú |
|----------|------:|--:|---------|
| P0 (bắt buộc — auth + 9 outbound list + filter state + audit + JWT issuance prereq) | 38 | 57% | 9 auth + 9 filter + 4 audit + 4 PII exclude (TVV/VV/TVCS metadata) + 9 outbound happy core (HD/DT/TVV/VV/DG/BM/TVCS) + rate happy/limit + 2 download |
| P1 (quan trọng — rate scope/reset, perf, payload edge, ct-htpl/dg-leak, ho-so-pl-dn) | 21 | 31% | rate reset + scope, 3 perf, 8 payload pagination/search edge, ct-htpl 3, ho-so-pl-dn 3, danh-gia leak |
| P2 (defer — inbound + date edge thấp risk) | 10 | 12% | 8 inbound BLOCKED + 2 date range |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md).

- ✅ **PASS**: 100% P0 (20/20) pass + ≥ 90% P1 (10/11) pass + AUDIT_LOG verify 100% (BR-DATA-05). Inbound 8 TC mark 🚫 KHÔNG tính vào tỷ lệ (defer).
- ⚠️ **CONDITIONAL PASS**: 95-99% P0 pass — log ⚠️ Sai spec cho TC fail nhẹ (vd message format khác SRS exact), không block release nếu Minor. Phải log Bug + plan re-test.
- ❌ **FAIL**: bất kỳ P0 nào FAIL nghiêm trọng (vd: API trả data draft = vi phạm BR-INTG-07 leak data publishable; JWT invalid trả 200; PII không exclude), HOẶC P1 pass rate < 90%, HOẶC AUDIT_LOG missing.

**Pass gate đặc thù FR-16 (revised v1.1):**
- **G1**: 9/9 endpoint outbound list (read) trả ≥ 1 record với JWT valid (chứng minh routing + auth + filter state cuối hoạt động).
- **G2**: 9/9 endpoint search trả ≥ 1 record matching keyword + sort relevance giảm dần.
- **G3**: 8/8 negative auth (no JWT, expired, signature, scope, mTLS cert sai, issuer sai, algorithm confusion HS256, missing claim) trả đúng HTTP code **+ envelope match shape BR-API-ERR-01 `{success:false, error:{code, message, details}}` + message text khớp SRS quoted exact** (S6 — không "close enough" accept).
- **G4**: Rate limit 429 + Retry-After header verify với 105 req trong 60s + reset behavior verify sau Retry-After + scope per-consumer xác định rõ.
- **G5**: Response time p95 < 3s qua sample 100 req/endpoint list (BR-INTG-04) + p99 search < 5s + concurrent 50 consumer × 2 req/s ổn định.
- **G6**: AUDIT_LOG verify INSERT row với đủ field (consumer_id, endpoint, timestamp, response_code) sau MỌI call sample (kể cả error 4xx/5xx) + consumer_id chính xác không null khi JWT invalid.
- **G7**: BR-SEC-01 exclude PII verify: response TVV không chứa key `cmnd|cccd|sdt|dia_chi_ca_nhan`; response VV không chứa `mst_dn|dia_chi_chi_tiet_dn`; response TVCS không chứa `noi_dung_chi_tiet`; response `/danh-gia` không leak `KET_QUA_DANH_GIA[]` per-VV detail (S9).
- **G8**: BR-INTG-07 verify 9/9 endpoint — record state draft/chờ duyệt/khóa KHÔNG xuất hiện trong response list/search (filter publishable only).

---

## 6. Tham chiếu

- [input/srs-v3/srs-fr-16-api.md](../../../input/srs-v3/srs-fr-16-api.md) — SRS chính FR-16 (1176 dòng, 18 FR + TPL-API-FULL + 7 BR)
- [tasks/system-overview.md §4.19](../../../tasks/system-overview.md) — tóm tắt M18 API (line 564-571)
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md §FR-16](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — 18 outbound endpoint table + warn inbound spec (line 919-945)
- [input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md](../../../input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md) — luồng nghiệp vụ đụng API (line 60-65 phân biệt Cổng PLQG vs LGSP)
- [output/test-strategy.md](../../../output/test-strategy.md) — chiến lược tổng thể
- [output/scaling-test-strategy.md](../../../output/scaling-test-strategy.md) — quy trình 7 bước onboard
- [output/permission-matrix.md](../../../output/permission-matrix.md) — ma trận phân quyền (FR-16 = column consumer external R-only)
- [output/template/test-case-template.md](../../../output/template/test-case-template.md) — template TC field-level
- [output/template/bug-report-template.md](../../../output/template/bug-report-template.md) — template bug report
- [input/users.csv](../../../input/users.csv) — 11 role × cấp (dùng cho seed upstream)

---

## 7. Note ambiguity + TODO BA confirm (revised v1.1, S7 + S8)

> **Đây là section thêm vào ngoài template chuẩn 6 section** — để track 6 ambiguity phát hiện khi đọc SRS FR-16. Cần BA/Dev BE confirm trước khi viết TC chi tiết file 01-14.

**Pre-check trước round live (S8):**
- ☐ Confirm Dev BE: endpoint `GET /api/admin/audit-log?consumer_id=...&endpoint=...` có sẵn không? Nếu không, QA có quyền `SELECT` trực tiếp `AUDIT_LOG` table không (cần DBA approve)? — Gate cho G6 (4 TC-AUDIT).
- ☐ Confirm Infra: mTLS sandbox provisioned (test cert `cert/consumer-test.crt` + base URL dev) — Gate cho TOÀN BỘ TC.
- ☐ Confirm Dev BE: JWKS endpoint URL chính thức (cho TC-AUTH-03 verify signature) — Gate cho 9 TC-AUTH.

| # | Ambiguity | Nguồn | Phương án tạm | Cần confirm | Asked to | Asked on | Deadline |
|---|-----------|-------|---------------|-------------|----------|----------|----------|
| 1 | **Auth scheme chi tiết**: SRS ghi "mTLS + JWT Bearer RS256, issuer = htpldn.moj.gov.vn". KHÔNG nói rõ JWT signing key public key endpoint (`/.well-known/jwks.json` hay tĩnh?). Cũng không có endpoint cấp JWT (`POST /auth/token` suy luận) | `srs-fr-16-api.md:82-86` | Assume JWKS endpoint chuẩn + `POST /api/v1/auth/token` đổi mTLS cert → JWT | Dev BE cung cấp JWKS URL + auth flow tài liệu | Dev BE | 2026-05-12 | 2026-05-19 |
| 2 | **HMAC signature header**: User prompt nhắc "HMAC?" trong auth. SRS FR-16 KHÔNG nói HMAC — chỉ JWT RS256 | `srs-fr-16-api.md:118-128` (chỉ JWT) | KHÔNG test HMAC | BA xác nhận HMAC có/không | BA | 2026-05-12 | 2026-05-15 |
| 3 | **LGSP event-driven format** (inbound từ HT TTHC BTP): SRS FR-16 KHÔNG có section "inbound". Format message envelope LGSP (SOAP? AMQP? Kafka?) chưa rõ | `01-tong-quan-nghiep-vu.md:63` + `02-thu-tu-module.md:941` | Mark 8 TC inbound = 🚫 BLOCKED Nhóm B (chờ dev BE spec) | Dev BE cung cấp LGSP message spec + sandbox endpoint test | Dev BE | 2026-05-12 | 2026-05-26 |
| 4 | **Số endpoint inbound chính xác**: `system-overview.md` ghi "~8" — có thể 6/7/8/9 | `system-overview.md:566` | Liệt kê 8 placeholder ở §1.2.2 | BA chốt count + danh sách path | BA | 2026-05-12 | 2026-05-19 |
| 5 | **FR-XII-13 metadata only**: SRS rõ "metadata only" — nhưng schema có thêm field `tu_lieu_pl_lien_ket[]` không (UC-152) — verify whitelist field cụ thể | `srs-fr-16-api.md:697-704` + `02-thu-tu-module.md:619` | Test theo schema SRS 6 field | BA confirm có expose tư liệu PL link không | BA | 2026-05-12 | 2026-05-15 |
| 6 | **Auto-push event-driven outbound** (G4 review): SRS không quote cơ chế push khi HD/VV/BM chuyển DA_DUYET/CONG_KHAI → call Cổng PLQG. Có event bus / webhook / cron polling? FR-13 TV Nhanh cũng không có endpoint riêng | `02-thu-tu-module.md:939` + user prompt | KHÔNG test endpoint auto-push — assume Cổng pull qua `/search` | CĐT + BA clarify event-driven có hay không + nếu có spec ở đâu | BA + CĐT | 2026-05-12 | 2026-05-19 |
| 7 | **JWT scope wildcard** (G12 review): SRS line 124 implies dynamic per-endpoint. Scope wildcard `htpldn:*:read` accept hay reject? | `srs-fr-16-api.md:124` | Test theo SRS literal — chỉ scope exact match | Dev BE confirm wildcard support | Dev BE | 2026-05-12 | 2026-05-19 |
| 8 | **Rate limit window + scope** (G8 review): SRS `:1131` ghi "100 req/min/consumer" — sliding window vs fixed? per-consumer global hay per-endpoint-per-consumer? | `srs-fr-16-api.md:1131-1136` | Test theo per-consumer global (toàn bộ endpoint chung 100/min) | BA + Dev BE confirm | BA + Dev BE | 2026-05-12 | 2026-05-19 |
| 9 | **AUDIT_LOG field `latency_ms`** (G6 review): Test plan §2.1 ghi field này nhưng SRS line 1161-1163 KHÔNG list — fixture mismatch SRS hay SRS thiếu? | `srs-fr-16-api.md:1157-1163` | Test schema theo SRS line 1161-1163; nếu BE expose `latency_ms` thì log Minor ⚠️ "fixture extra field" | Dev BE confirm field thực có không | Dev BE | 2026-05-12 | 2026-05-15 |

---

*Template gốc: `output/template/test-plan-overview-template.md`. Test plan FR-16 v1.1 (revised 2026-05-12 12:35:00) — module Nhóm D (no v3.5 update). Re-run smoke API ping mỗi đợt seed upstream module để chứng minh endpoint chưa break sau SRS update lan từ FR-04/05/06 v3.5.*

**Revision changelog v1.0 → v1.1:**
- G1 (uneven coverage): danh-gia/ct-htpl/ho-so-pl-dn từ 2 TC → 3 TC mỗi cái (thêm filter/leak/exclude).
- G2 (auth coverage): 5 TC → 9 TC (thêm TC-AUTH-06 issuer, -07 algorithm, -08 missing claim + TC-AUTH-00 issuance flow S5).
- G3 (inbound unblock): thêm cột "Unblock condition" cho 8 inbound + escalate rule >2 round.
- G5 (filter coverage): TC-FILTER 2 → 9 (mỗi endpoint outbound 1 TC verify BR-INTG-07).
- G6 (audit negative): TC-AUDIT 1 → 4 (error path, consumer_id, latency_ms field check).
- G7 (perf): 1 → 3 TC (concurrent + search latency).
- G8 (rate): 1 → 4 TC (reset + scope + ambiguity #8 chốt trước).
- G9 (pagination): 3 → 7 TC (page âm, page=999999, size=0, default missing).
- G10 (download): 1 → 2 TC (binary integrity vs `kich_thuoc`).
- G12 (scope granularity): ambiguity #7 + giữ TC-AUTH-04 nhưng note cần verify wildcard.
- S1 (TC ID prefix): convention rõ trong §3.
- S2 (tooling): bảng tooling matrix mới trong §2.4.
- S3 (SRS line cite): cite line cho mỗi filter state trong §1.2.1.
- S5 (JWT issuance prereq): TC-AUTH-00 P0 đầu file 10.
- S6 (G3 gate): thêm requirement envelope shape + message exact match.
- S7 (ambiguity owner): thêm cột Asked to / Asked on / Deadline.
- S8 (audit endpoint pre-check): thêm pre-check section đầu §7.
- S9 (KQDG leak): thêm TC-OUT-DG-03 verify response không leak `KET_QUA_DANH_GIA[]` per-VV.
- S10 (split payload file): 12 → 12a (pagination/search) + 12b (date range).
- **Tổng TC**: 39 → 67 (live testable: 31 → 59).
