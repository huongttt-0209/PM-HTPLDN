# Test Case — FR-X.2-02 Quản lý Phiên Tư vấn Nhanh (logic nội bộ ngoài CSV)

> **File:** `02-TC-FR-X2-02-quan-ly-phien-tu-van.md`
> **FR:** FR-X.2-02 (CMS xử lý phiên TVN do DN gửi từ chuyên trang)
> **SCR:** SCR-X2-03 — Quản lý Tư vấn Nhanh (gộp MH-13.3 + MH-13.4 v2.1)
> **SRS Reference:** [`srs-fr-13-tv-nhanh-v3.1.md`](../../../input/srs-v3/srs-fr-13-tv-nhanh-v3.1.md) §FR-X.2-02 line 169-230, §SCR-X2-03 line 553-580, SM-TVNHANH line 791-832
> **Loại:** B (browser, MCP chrome-devtools)

## TC Index

| TC ID | Tên TC | Trace | Tag | Role |
|-------|--------|-------|-----|------|
| TC-PHIEN-001 | Hiển thị danh sách phiên TVN | FR-X.2-02 / SCR row 5 | Happy | CB_NV_TW |
| TC-PHIEN-002 | Tab phân loại 4 (Tất cả / Chờ xử lý / Đã gợi ý / Hoàn thành) | FR-X.2-02 / SCR row 3 | Happy | CB_NV_TW |
| TC-PHIEN-003 | Lọc theo từ khóa + trạng thái + khoảng ngày | FR-X.2-02 / SCR row 4 | Happy | CB_NV_TW |
| TC-PHIEN-004 | Xem chi tiết phiên DA_GOI_Y → layout 2 cột | FR-X.2-02 / SCR row 7-8 | Happy | CB_NV_TW |
| TC-PHIEN-005 | TOP 5 gợi ý từ kho — relevance DESC | FR-X.2-02 / Processing 3 + BR-DATA-08 | Happy | CB_NV_TW |
| TC-PHIEN-006 | Click [Chọn] gợi ý → auto-fill ô soạn Rich Text | FR-X.2-02 / SCR row 8 | Happy | CB_NV_TW |
| TC-PHIEN-007 | Chỉnh sửa nội dung trả lời từ gợi ý → Gửi → CB_TRA_LOI | FR-X.2-02 / Processing 5 + SM trans #5 | Happy | CB_NV_TW |
| TC-PHIEN-008 | DA_GOI_Y → HOAN_THANH (DN hài lòng + đánh giá) | SM trans #6 | Happy | CB_NV_TW (verify side-effect) |
| TC-PHIEN-009 | CB_TRA_LOI → HOAN_THANH (DN đánh giá) | SM trans #7 | Happy | CB_NV_TW (verify side-effect) |
| TC-PHIEN-010 | DANG_TIM_KIEM → CB_TRA_LOI khi kho rỗng / không match | SM trans #4 + ERR-TVN-01 | Happy/Edge | CB_NV_TW |
| TC-PHIEN-011 | Auto MOI → HET_HAN sau 30 ngày (verify record đã seed) | SM trans #8 | Happy batch | CB_NV_TW |
| TC-PHIEN-012 | Phân trang 20 mục/trang | BR-DATA-07 | Happy | CB_NV_TW |
| TC-PHIEN-100 | E2 — nội dung trả lời rỗng → ERR-TVN-02 | FR-X.2-02 / E2 | Negative | CB_NV_TW |
| TC-PHIEN-101 | Phiên cấp ĐP truy cập bởi DP khác → 404 (BR-AUTH-08) | BR-AUTH-08 | Negative cross-tenant | CB_NV_DP_02 |
| TC-PHIEN-102 | Submit khi state HOAN_THANH → block | SM | Negative state cấm | CB_NV_TW |
| TC-PHIEN-200 | TOP 5 trả 3 kết quả khi kho có ≤5 Q&A | A4 edge | Edge | CB_NV_TW |
| TC-PHIEN-201 | Concurrent CB NV trả lời cùng phiên → 409 | A4 edge | Edge | CB_NV_TW |
| TC-PHIEN-202 | Sửa drastic gợi ý → nguon_tra_loi=THU_CONG | SPEC-CLARIFY-TVN-06 | Edge | CB_NV_TW |
| TC-PHIEN-203 | thoi_gian_xu_ly_phut cross-day | A4 edge | Edge | CB_NV_TW |

---

## Test Cases

### TC-PHIEN-001 — Hiển thị danh sách phiên TVN

**Precondition:**
- Login `cb_nv_tw_01`. Có ≥3 phiên TVN trong scope TW (mix các state MOI / DA_GOI_Y / CB_TRA_LOI / HOAN_THANH).

**Steps:**
1. Sidebar "Tư vấn" → "Tư vấn Nhanh" hoặc navigate `/tu-van/tu-van-nhanh`.

**Expected:**
- Breadcrumb "Trang chủ > Tư vấn > Tư vấn Nhanh" hiển thị.
- Header `[Làm mới]`.
- Cột table: Mã phiên / Câu hỏi DN (cắt 100 ký tự) / Kênh (TV_NHANH xanh / TV_THU_CONG vàng) / Số gợi ý / Trạng thái SM-TVNHANH / Ngày gửi / Ngày cập nhật / Hành động.
- Network: `GET /api/v1/tu-van-nhanh?page=1&size=20`.

---

### TC-PHIEN-002 — Tab phân loại 4 (Tất cả / Chờ xử lý / Đã gợi ý / Hoàn thành)

**Trace:** SCR row 3
**Precondition:** Có phiên ở mỗi state.

**Steps:**
1. Click tab "Tất cả" → tất cả state.
2. Click "Chờ xử lý" → filter MOI + DANG_TIM_KIEM.
3. Click "Đã gợi ý" → filter DA_GOI_Y + CB_TRA_LOI.
4. Click "Hoàn thành" → filter HOAN_THANH + HET_HAN.

**Expected:** Mỗi tab hiển thị đúng số đếm + filter chính xác.

---

### TC-PHIEN-003 — Lọc theo từ khóa + trạng thái + khoảng ngày

**Steps:**
1. Filter từ khóa "thuế" + trang_thai = "DA_GOI_Y" + khoảng ngày 7 ngày gần nhất.
2. Quan sát.

**Expected:** Chỉ phiên khớp 3 điều kiện AND + có "thuế" trong cau_hoi.

---

### TC-PHIEN-004 — Xem chi tiết phiên DA_GOI_Y → layout 2 cột

**Trace:** SCR row 7-8
**Precondition:** Có phiên DA_GOI_Y.

**Steps:**
1. Click [Trả lời] trên dòng phiên DA_GOI_Y.
2. Quan sát layout.

**Expected:**
- Cột trái (40%): Mã phiên + badge SM-TVNHANH + Thông tin DN + Câu hỏi DN (card nền nhạt) + Lịch sử trao đổi (chat bubbles).
- Cột phải (60%): TOP 5 gợi ý + ô soạn Rich Text C16 + nút [Gửi trả lời].

---

### TC-PHIEN-005 — TOP 5 gợi ý từ kho relevance DESC

**Trace:** Processing 3 + BR-DATA-08
**Precondition:** Phiên có cau_hoi "Thuế GTGT cho DN nhỏ". Kho có ≥10 Q&A liên quan thuế.

**Steps:**
1. Mở chi tiết phiên → quan sát TOP 5.

**Expected:**
- Hiển thị tối đa 5 gợi ý, KHÔNG nhiều hơn.
- Mỗi gợi ý có: Mã Q&A / Câu hỏi (bold) / Câu trả lời / Điểm relevance (%) / nút [Chọn].
- Sắp xếp relevance DESC (cao xuống thấp).
- Network: `GET /api/v1/tu-van-nhanh/{id}/goi-y?limit=5` → 200, body 5 phần tử.

---

### TC-PHIEN-006 — Click [Chọn] gợi ý → auto-fill ô soạn Rich Text

**Steps:**
1. Trong layout 2 cột → click [Chọn] trên gợi ý #1.
2. Quan sát ô soạn cột phải.

**Expected:** Ô soạn Rich Text auto-fill nội dung cau_tra_loi của gợi ý #1.

---

### TC-PHIEN-007 — Chỉnh sửa từ gợi ý → Gửi → CB_TRA_LOI

**Trace:** SM trans #5 (DA_GOI_Y → CB_TRA_LOI)
**Precondition:** Phiên DA_GOI_Y, đã chọn gợi ý.

**Steps:**
1. Sửa nội dung trong ô soạn (thêm 1 đoạn).
2. Click [Gửi trả lời] → modal xác nhận.
3. [Xác nhận].

**Expected:**
- Toast "Đã gửi trả lời cho DN."
- Phiên trang_thai = CB_TRA_LOI.
- TU_VAN_NHANH.noi_dung_tra_loi = nội dung sau chỉnh sửa.
- TU_VAN_NHANH.nguon_tra_loi = THU_CONG (do CB NV soạn) hoặc KHO (nếu không sửa từ gợi ý).
- TU_VAN_NHANH.cb_xu_ly_id = cb_nv_tw_01.id.
- TU_VAN_NHANH.ngay_tra_loi = NOW().
- Network: `POST /api/v1/tu-van-nhanh/{id}/tra-loi` body `{noi_dung, nguon_tra_loi}` → 200.

---

### TC-PHIEN-008 — DA_GOI_Y → HOAN_THANH (DN hài lòng + đánh giá)

**Trace:** SM trans #6
**Precondition:** Phiên DA_GOI_Y, DN trên Cổng PLQG đánh giá điểm 5.

**Steps (verify side-effect via API mock):**
1. Mock API inbound: POST `/api/v1/inbound/danh-gia-tv-nhanh` body `{tu_van_nhanh_id: X, diem: 5, doanh_nghiep_id: ...}` (cách trigger thủ công xem file 04).
2. Refresh CMS list.

**Expected:**
- Phiên X chuyển trang_thai = HOAN_THANH.
- DANH_GIA_TV record mới với diem=5, tu_van_nhanh_id=X.
- (Test side-effect chi tiết trong file 04, file này chỉ verify SM transition).

---

### TC-PHIEN-009 — CB_TRA_LOI → HOAN_THANH (DN đánh giá)

**Trace:** SM trans #7
**Precondition:** Phiên CB_TRA_LOI (CB NV đã trả lời).

**Steps:**
1. Mock API inbound DG → trigger transition.

**Expected:**
- Phiên trang_thai = HOAN_THANH.
- thoi_gian_xu_ly_phut = (ngay_tra_loi - ngay_tao) phút (cho báo cáo SLA).

---

### TC-PHIEN-010 — DANG_TIM_KIEM → CB_TRA_LOI khi kho rỗng

**Trace:** SM trans #4 + ERR-TVN-01
**Precondition:** Kho Q&A trống (xóa hết hoặc seed kho 0 record cho lĩnh vực test).

**Steps:**
1. DN gửi câu hỏi qua Cổng PLQG (mock API inbound) → tạo phiên MOI.
2. HT chuyển MOI → DANG_TIM_KIEM → search.
3. Search trả 0 kết quả.

**Expected:**
- Phiên auto chuyển CB_TRA_LOI (skip DA_GOI_Y).
- Hiển thị banner WARN ERR-TVN-01 "Chưa có dữ liệu trong kho câu hỏi" trên UI CB NV khi mở chi tiết phiên.

---

### TC-PHIEN-011 — Auto MOI → HET_HAN sau 30 ngày

**Trace:** SM trans #8
**Precondition:** Seed phiên MOI với `ngay_tao` = NOW() - 31 ngày.

**Steps:**
1. Trigger batch job qua admin endpoint hoặc đợi cron 30 phút.
2. Verify record sau batch.

**Expected:**
- Phiên trang_thai = HET_HAN.
- TB CB NV được gửi (in-app/email).
- AUDIT_LOG: action=AUTO_EXPIRE.

---

### TC-PHIEN-012 — Phân trang 20 mục/trang

**Trace:** BR-DATA-07 + SCR row 6
**Precondition:** ≥41 phiên trong list.

**Steps:** click trang 1, 2, 3.

**Expected:** mỗi trang đúng 20.

---

### TC-PHIEN-100 — E2 nội dung trả lời rỗng → ERR-TVN-02

**Trace:** FR-X.2-02 / E2
**Steps:**
1. Mở phiên DA_GOI_Y → KHÔNG nhập gì vào ô soạn.
2. Click [Gửi trả lời].

**Expected:** Inline error "Nội dung trả lời là bắt buộc" / ERR-TVN-02. Form không submit.

---

### TC-PHIEN-101 — Phiên cấp ĐP truy cập bởi DP khác → 404 (BR-AUTH-08)

**Trace:** BR-AUTH-08
**Precondition:** Phiên X tạo trong scope `cb_nv_dp_01` (Sở TP AG).

**Steps:**
1. Login `cb_nv_dp_02` (Sở TP BG).
2. Truy cập URL trực tiếp `/tu-van/tu-van-nhanh/{X.id}` hoặc API `GET /api/v1/tu-van-nhanh/{X.id}`.

**Expected:** 404 hoặc 403 ERR-AUTH-08. List không hiển thị phiên X.

---

### TC-PHIEN-102 — Submit khi state HOAN_THANH → block

**Steps:**
1. Mở phiên HOAN_THANH (read-only mode).

**Expected:**
- Layout chi tiết hiển thị nhưng nút [Gửi trả lời] disabled hoặc ẩn hoàn toàn.
- API `POST /api/v1/tu-van-nhanh/{id}/tra-loi` reject 400 với lý do state không cho phép.

---

---

## Edge bổ sung A4

### TC-PHIEN-200 — TOP 5 trả 3 kết quả khi kho có ≤5 Q&A liên quan

**Trace:** A4 edge boundary
**Precondition:** Kho có 3 Q&A liên quan keyword.

**Steps:**
1. DN gửi câu hỏi → phiên DA_GOI_Y.
2. Mở chi tiết phiên.

**Expected:**
- TOP 5 hiển thị 3 (tất cả Q&A có), KHÔNG lỗi "thiếu kết quả".
- Sắp relevance DESC.

---

### TC-PHIEN-201 — Concurrent CB NV trả lời cùng phiên

**Steps:**
1. CB-A và CB-B (cùng đơn vị TW) cùng mở phiên DA_GOI_Y.
2. CB-A nhập trả lời + Gửi → CB_TRA_LOI thành công.
3. CB-B nhập trả lời + Gửi.

**Expected:**
- CB-B nhận HTTP 409 hoặc state validation error "Phiên đã được trả lời bởi CB khác."
- Lịch sử phiên có 1 trả lời (của CB-A).

---

### TC-PHIEN-202 — Threshold sửa drastic gợi ý → nguon_tra_loi=THU_CONG

**Trace:** SPEC-CLARIFY-TVN-06
**Steps:**
1. Chọn gợi ý #1 (auto-fill ô soạn).
2. Sửa toàn bộ nội dung khác hoàn toàn → Gửi.

**Expected:**
- TU_VAN_NHANH.nguon_tra_loi = THU_CONG (do sửa nhiều).
- **SPEC-CLARIFY-TVN-06:** Threshold % delta để xác định KHO vs THU_CONG cần BA chốt. Default: nếu sửa > 30% nội dung → THU_CONG; nếu giữ 100% → KHO.

---

### TC-PHIEN-203 — thoi_gian_xu_ly_phut khi cross-day

**Steps:**
1. Phiên ngay_tao = "2026-05-10 23:50".
2. CB NV trả lời lúc "2026-05-11 00:10".

**Expected:**
- thoi_gian_xu_ly_phut = 20 (chính xác qua midnight).

---

**Tổng số TC:** 19 TC (12 Happy + 3 Negative + 4 Edge A4)

*Generated 2026-05-10 — Phase A step A3 (bmad-qa-generate-e2e-tests) + A4 edge merge*
