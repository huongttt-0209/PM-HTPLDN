# Test Case — FR-X.2-03 + FR-X.2-04 DN Chuyên trang (Side-effect verify)

> **File:** `03-TC-FR-X2-03-04-DN-chuyen-trang-side-effect.md`
> **FR:** FR-X.2-03 (DN gửi câu hỏi qua Cổng PLQG) + FR-X.2-04 (DN tìm kiếm phản hồi qua Cổng)
> **SCR:** Chuyên trang Cổng PLQG — KHÔNG có UI CMS. **Loại M** — verify side-effect trên CMS sau API inbound từ Cổng.
> **SRS Reference:** [`srs-fr-13-tv-nhanh-v3.1.md`](../../../input/srs-v3/srs-fr-13-tv-nhanh-v3.1.md) §FR-X.2-03 line 232-291, §FR-X.2-04 line 293-345
> **Loại:** M (API inbound — verify UI side-effect, KHÔNG test API thuần)
> **Note A7:** A7 LOẠI module-level cho TC API thuần. **Giữ TC verify side-effect UI.**

## TC Index

| TC ID | Tên TC | Trace | Tag | Role |
|-------|--------|-------|-----|------|
| TC-DN-001 | DN gửi câu hỏi TV_NHANH → tạo phiên MOI hiển thị CMS | FR-X.2-03 / Processing 3 | Happy side-effect | CB_NV_TW (verify) |
| TC-DN-002 | DN gửi câu hỏi TV_THU_CONG → chuyển Nhóm II UC12 (HOI_DAP MOI) | FR-X.2-03 / Processing 4 | Happy cross-FR | CB_NV_TW (verify) |
| TC-DN-003 | DN chuyển kênh TV_NHANH → TV_THU_CONG → giữ lịch sử | FR-X.2-03 / Processing 5 | Happy | CB_NV_TW (verify) |
| TC-DN-004 | DN search Cổng PLQG → chỉ trả Q&A DA_DUYET + hieu_luc=1 | FR-X.2-04 / Processing 2 | Happy | (verify Cổng PLQG mock) |
| TC-DN-005 | DN search → hieu_luc=0 ẩn khỏi kết quả | FR-X.2-04 / Processing 2 | Happy | (verify Cổng PLQG mock) |
| TC-DN-100 | E1 — DN gửi câu hỏi trống → ERR-TVN-DN-01 (UI-bridge wrap network MCP) | FR-X.2-03 / E1 | Negative (Codex P1-001 fix) | (verify network + audit-log) |
| TC-DN-101 | E1 — DN search < 2 ký tự → ERR-TVN-TK-01 (UI-bridge wrap network MCP) | FR-X.2-04 / E1 | Negative (Codex P1-002 fix) | (verify network) |
| TC-DN-200 | DN gửi cùng câu hỏi 2 lần liên tiếp (duplicate) | SPEC-CLARIFY-TVN-07 | Edge | (verify CMS) |
| TC-DN-300 | DN search no results → INF-TVN-TK-01 | GAP-ERR-01 (A5) | Fill-gap A6 | (verify API) |

---

## Test Cases

### TC-DN-001 — DN gửi câu hỏi TV_NHANH → tạo phiên MOI hiển thị CMS

**Trace:** FR-X.2-03 / Processing 3
**Precondition:**
- Mock endpoint Cổng PLQG (hoặc dùng admin trigger qua test infra).
- DN có `doanh_nghiep_id` test = 100 đã đăng ký scope Sở TP AG.

**Steps:**
1. Trigger API inbound: `POST /api/v1/inbound/tu-van-nhanh` body:
   ```json
   {
     "doanh_nghiep_id": 100,
     "cau_hoi": "Hỏi về thuế TNDN cho DN nhỏ",
     "kenh_tu_van": "NHANH"
   }
   ```
2. Login `cb_nv_dp_01` (Sở TP AG).
3. Mở "Tư vấn Nhanh" tab "Chờ xử lý".

**Expected:**
- Network response API inbound: 200, body `{ma_phien: "TVN-...", trang_thai: "MOI"}`.
- Phiên mới hiển thị tab "Chờ xử lý" với:
  - Câu hỏi DN: "Hỏi về thuế TNDN cho DN nhỏ"
  - Kênh: TV_NHANH (nhãn xanh)
  - Trạng thái: MOI (xanh dương) → tự động chuyển DANG_TIM_KIEM → DA_GOI_Y trong vài giây
- AUDIT_LOG: INSERT TU_VAN_NHANH source=API_INBOUND.

---

### TC-DN-002 — DN gửi TV_THU_CONG → chuyển Nhóm II UC12 (HOI_DAP MOI)

**Trace:** FR-X.2-03 / Processing 4 (cross-FR-13 ↔ FR-02)
**Precondition:** DN test = 100 (Sở TP AG).

**Steps:**
1. Trigger API inbound: `POST /api/v1/inbound/tu-van-nhanh` body:
   ```json
   {
     "doanh_nghiep_id": 100,
     "cau_hoi": "Đề nghị tư vấn chi tiết về luật thuế",
     "kenh_tu_van": "THU_CONG"
   }
   ```
2. Login `cb_nv_dp_01`.
3. Mở "Hỏi đáp" (FR-02) tab "Mới".

**Expected:**
- KHÔNG có phiên TVN tạo (kênh THU_CONG bypass FR-13).
- HOI_DAP record mới hiển thị với:
  - kenh_tiep_nhan = TVN_BRIDGE (theo FR-II line 162-170 — auto-set từ FR-13 escalate)
  - tu_van_nhanh_goc_id = NULL (vì kênh là THU_CONG ngay từ đầu, KHÔNG escalate)
  - HOẶC: Theo BA quyết định (cần verify) — có thể HOI_DAP có tu_van_nhanh_goc_id link tới phiên gốc.
  - **SPEC-CLARIFY-TVN-01:** SRS không nói rõ TV_THU_CONG có tạo TU_VAN_NHANH placeholder hay tạo HOI_DAP trực tiếp. Cần BA xác nhận luồng.

---

### TC-DN-003 — DN chuyển kênh TV_NHANH → TV_THU_CONG → giữ lịch sử

**Trace:** FR-X.2-03 / Processing 5
**Precondition:** Phiên TVN có lịch sử trao đổi (≥2 message DN-CB).

**Steps:**
1. DN trên Cổng PLQG nhấn "Chuyển sang TV thủ công".
2. Trigger API inbound: `POST /api/v1/inbound/tu-van-nhanh/{ma_phien}/chuyen-kenh` body `{kenh_moi: "THU_CONG"}`.
3. Login CB NV → mở Hỏi đáp (FR-02).

**Expected:**
- HOI_DAP mới tạo có:
  - kenh_tiep_nhan = TVN_BRIDGE
  - tu_van_nhanh_goc_id = phiên TVN cũ
  - noi_dung kế thừa câu hỏi gốc + lịch sử trao đổi (verify field "lịch sử" có chat bubbles).
- Phiên TVN gốc giữ trạng thái cũ (hoặc chuyển HET_HAN — cần BA xác nhận).
- **SPEC-CLARIFY-TVN-02:** SRS không nói rõ trạng thái phiên TVN gốc sau khi chuyển kênh. Cần BA xác nhận.

---

### TC-DN-004 — DN search Cổng PLQG → chỉ trả Q&A DA_DUYET + hieu_luc=1

**Trace:** FR-X.2-04 / Processing 2
**Precondition:**
- Kho có Q&A:
  - QA-1: trang_thai=CONG_KHAI, hieu_luc=1
  - QA-2: trang_thai=DA_DUYET, hieu_luc=1
  - QA-3: trang_thai=CHO_DUYET, hieu_luc=1
  - QA-4: trang_thai=CONG_KHAI, hieu_luc=0

**Steps:**
1. Mock API inbound: `GET /api/v1/inbound/kho-cau-hoi/search?tu_khoa=thue` (call from Cổng PLQG).
2. Quan sát response.

**Expected:**
- Response chỉ trả QA-1 (CONG_KHAI + hieu_luc=1).
- KHÔNG trả QA-2 (chưa CONG_KHAI), QA-3 (chưa duyệt), QA-4 (hết hiệu lực).
- **SPEC-CLARIFY-TVN-03:** SRS line 321-322 nói "DA_DUYET + hieu_luc" nhưng FR-X.2-06 nói chỉ Q&A `trang_thai=CONG_KHAI` mới hiển thị Cổng. Cần BA xác nhận: DN search trả DA_DUYET hay chỉ CONG_KHAI?
  - Default: chỉ CONG_KHAI + hieu_luc=1 (vì BR-PUBLIC-01 + BR-FLOW-05 nói chỉ CONG_KHAI mới đẩy ra Cổng).

---

### TC-DN-005 — DN search → hieu_luc=0 ẩn khỏi kết quả

**Steps:**
1. Tạo Q&A trang_thai=CONG_KHAI, hieu_luc=1.
2. CB NV toggle hieu_luc → 0 (TC-KHO-008).
3. Mock API inbound: search keyword match Q&A đó.

**Expected:** Q&A KHÔNG hiển thị trong kết quả (theo Processing 6 SRS line 123).

---

### TC-DN-100 — E1 DN gửi câu hỏi trống → ERR-TVN-DN-01 (UI-bridge wrap)

**Trace:** FR-X.2-03 / E1 line 283 — `| E1 | Câu hỏi trống | ERR-TVN-DN-01 | "Vui lòng nhập câu hỏi" | ERROR |`
**Codex P1-001 fix 2026-05-10:** Restore active với UI-bridge wrap (verify network MCP từ admin trigger + AUDIT_LOG entry trên trang Nhật ký HT FR-10 W1.1).

**Steps:**
1. Trigger API inbound qua admin endpoint hoặc Postman (ghi rõ trong Test Notes):
   ```http
   POST /api/v1/inbound/tu-van-nhanh
   {"cau_hoi": "", "kenh_tu_van": "NHANH", "doanh_nghiep_id": 100}
   ```
2. MCP `list_network_requests` capture response.
3. Login `qtht_01` → mở `/quan-tri/audit-log`.

**Expected:**
- Network MCP: status 400 + body chứa ERR-TVN-DN-01 "Vui lòng nhập câu hỏi".
- KHÔNG có TU_VAN_NHANH record mới hiển thị trên SCR-X2-03 list (verify by login `cb_nv_tw_01` mở list TVN).
- AUDIT_LOG entry action='API_INBOUND_REJECT', error_code='ERR-TVN-DN-01' (nếu hệ thống log fail attempts).

---

### TC-DN-101 — E1 DN search từ khóa < 2 ký tự → ERR-TVN-TK-01 (UI-bridge wrap)

**Trace:** FR-X.2-04 / E1 line 339 — `| E1 | Từ khóa < 2 ký tự | ERR-TVN-TK-01 | "Từ khóa tìm kiếm phải có ít nhất 2 ký tự" | ERROR |`
**Codex P1-002 fix 2026-05-10:** Restore active với UI-bridge wrap.

**Steps:**
1. Trigger API inbound qua admin endpoint:
   ```http
   GET /api/v1/inbound/kho-cau-hoi/search?tu_khoa=a
   ```
2. MCP `list_network_requests` capture response.

**Expected:**
- Network MCP: status 400 + body chứa ERR-TVN-TK-01 "Từ khóa tìm kiếm phải có ít nhất 2 ký tự".
- KHÔNG có data Q&A returned.

---

---

## Edge bổ sung A4

### TC-DN-200 — DN gửi cùng câu hỏi 2 lần liên tiếp

**Trace:** SPEC-CLARIFY-TVN-07
**Steps:**
1. Mock API inbound: gửi 2 lần liên tiếp cùng cau_hoi + cùng doanh_nghiep_id trong vòng 5 giây.

**Expected:**
- **SPEC-CLARIFY-TVN-07:** SRS không nói rõ chống duplicate. Có 2 option:
  - **Option A (allow):** Tạo 2 phiên TVN riêng biệt (DN có quyền hỏi nhiều lần).
  - **Option B (block):** Reject lần 2 với 409 hoặc warn DN.
- Default Option A: 2 phiên tạo, 2 record TU_VAN_NHANH.

---

---

## A6 fill-gap (từ A5 traceability)

### TC-DN-300 — DN search no results → INF-TVN-TK-01 hiển thị Cổng

**Trace:** GAP-ERR-01 (A5)
**Precondition:** Kho có 0 Q&A match keyword "xyzzz123nonexistent".

**Steps:**
1. Mock API inbound: `GET /api/v1/inbound/kho-cau-hoi/search?tu_khoa=xyzzz123nonexistent`.

**Expected:**
- Response 200 OK với body `{danh_sach_qa: [], message: "Không tìm thấy câu hỏi phù hợp"}` (INF-TVN-TK-01).
- KHÔNG là 404 hay 400 — INF-level response.

---

**Tổng số TC:** 9 TC active (5 Happy + 2 Negative restore Codex P1-001/002 + 1 Edge A4 + 1 fill-gap A6)

**Note A7:** Các TC này test API inbound thuần — A7 sẽ filter:
- TC-DN-100/101 LOẠI nếu không có UI bridge (verify trên CMS).
- TC-DN-001/002/003 GIỮ vì verify side-effect UI CMS sau API.
- TC-DN-004/005 verify qua Cổng PLQG mock — A7 sửa thành "verify network request từ CMS export".

*Generated 2026-05-10 — Phase A step A3 (bmad-qa-generate-e2e-tests)*
