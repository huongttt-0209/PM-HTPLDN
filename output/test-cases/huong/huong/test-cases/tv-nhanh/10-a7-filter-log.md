# A7 — Filter UI/function-testable Audit Log (FR-13 TV Nhanh)

> **Phase:** A7 — Manual filter
> **Ngày tạo:** 2026-05-10
> **Mục đích:** Loại / sửa TC chỉ test được DB query / API curl thuần / cron job no-UI. Áp dụng [§3.1 A7 Filter rule](../../../tasks/detailed-tc/plan.md#31-phase-a--skill-bmad).

---

## 1. Tổng kết action

| File | TC trước A7 | LOẠI ban đầu | RESTORE Codex P1 | SỬA UI bridge | TC sau A7 + Codex |
|------|-------------|---------------|--------------------|----------------|---------------------|
| 01-Kho Q&A | 33 | 0 | 0 | 1 | 33 |
| 02-Phiên TVN | 19 | 0 | 0 | 1 | 19 |
| 03-DN chuyên trang | 9 | 2 (TC-DN-100/101) | +2 (Codex P1-001/002) | 4 | 9 |
| 04-API inbound DG | 15 | 0 | 0 | 8 | 15 + 2 Codex (TC-DGTV-104/301) = 17 |
| 05-Công khai/Hủy | 16 | 0 | 0 | 1 | 16 |
| 06-Permission | 6 | 0 | 0 | 0 | 6 |
| **Total** | **98** | **2** | **+2** | **15** | **100 active** |

> **Codex review apply 2026-05-10:** TC-DN-100 + TC-DN-101 RESTORE active với UI-bridge wrap (network MCP + AUDIT_LOG verify). Thêm TC-DGTV-104 (header negative) + TC-DGTV-301 (missing doanh_nghiep_id) per Codex P1-003/004.

---

## 2. LOẠI (TC chỉ-DB/API thuần, không có UI bridge) — đã RESTORE per Codex P1

| TC ID | File | Lý do LOẠI ban đầu | Codex P1 Action |
|-------|------|---------------------|------------------|
| ~~TC-DN-100~~ | 03-DN chuyên trang | A7 LOẠI ban đầu vì test thuần API status code | **RESTORE active 2026-05-10** với UI bridge wrap (network MCP + AUDIT_LOG verify) |
| ~~TC-DN-101~~ | 03-DN chuyên trang | A7 LOẠI ban đầu vì test thuần API endpoint Cổng | **RESTORE active 2026-05-10** với UI bridge wrap |

> **Codex P1-001/002:** Yêu cầu giữ active để cover ERR-TVN-DN-01 + ERR-TVN-TK-01 trong test suite. Pattern UI bridge giống TC-DGTV-100..104 (verify network MCP + AUDIT_LOG on Nhật ký HT).

---

## 3. SỬA (TC có verify-DB/API thuần → wrap trong UI bridge)

| TC ID | File | Sửa gì | Lý do |
|-------|------|--------|-------|
| TC-KHO-018 | 01 | "Verify trang Nhật ký HT (FR-10 W1.1) có record action=CREATE" thay vì query DB AUDIT_LOG | Có UI bridge (`/quan-tri/audit-log`) — không phải verify DB thuần |
| TC-PHIEN-011 | 02 | "Verify record sau batch trên UI list TV Nhanh tab Tất cả" thay vì query DB | Cần verify trang_thai = HET_HAN trên UI |
| TC-DN-001 | 03 | "Sau API trigger, login CMS verify phiên hiển thị tab 'Chờ xử lý'" — đã có UI bridge | OK, giữ. Chỉ note: trigger API qua admin endpoint hoặc Postman trong Test Notes |
| TC-DN-002 | 03 | Tương tự TC-DN-001 — verify HOI_DAP record qua UI Hỏi đáp | OK, giữ |
| TC-DN-003 | 03 | Verify HOI_DAP có lịch sử trao đổi qua tab "Lịch sử" trên UI | OK, giữ |
| TC-DN-004 | 03 | "Verify network response qua MCP `list_network_requests` từ admin endpoint" thay vì verify Cổng PLQG mock UI | API outbound - dùng MCP network |
| TC-DN-005 | 03 | Tương tự TC-DN-004 | API outbound - dùng MCP network |
| TC-DGTV-100/101/102/103 | 04 | "Trigger API qua admin endpoint hoặc Postman trong Test Notes. Verify response status + database COUNT qua quan-tri/audit-log UI hoặc MCP network" | Test API status code thuần — A7 wrap trong UI bridge: verify network log + AUDIT_LOG entry trên trang Nhật ký HT |
| TC-DGTV-200/201/202/300 | 04 | Tương tự TC-DGTV-100..103 | A7 wrap |
| TC-CK-003 | 05 | "MCP `list_network_requests` inspect outbound payload" — đã có UI bridge dạng network monitoring | OK, giữ |

---

## 4. GIỮ (TC có UI bridge rõ ràng — không cần sửa)

85 TC còn lại đều có UI bridge:
- File 01 Kho Q&A: 32 TC (toàn bộ trên SCR-X2-01 UI).
- File 02 Phiên TVN: 18 TC (toàn bộ trên SCR-X2-03 UI).
- File 03 DN chuyên trang: 3 TC (verify side-effect trên CMS).
- File 04 API inbound DG: 11 TC (verify accordion DG inline + COUNT records qua UI Nhật ký HT).
- File 05 Công khai/Hủy: 15 TC (toàn bộ verify trên SCR-X2-01 + MCP network).
- File 06 Permission: 6 TC (toàn bộ verify UI hidden / sidebar absence + 403/404 qua MCP network).

---

## 5. Acceptance check

> **Yêu cầu §3.1 A7 Filter rule (plan.md):** 0 TC còn keyword "verify DB row", "check index", "curl POST", "cron job", "background worker" mà không có UI bridge.

**Kết quả grep:**

| Keyword | Match trước A7 | Match sau A7 (sau SỬA) | OK? |
|---------|----------------|------------------------|-----|
| "query DB" / "verify DB row" | 3 | 0 (đã sửa trong TC-KHO-018, TC-PHIEN-011) | ✅ |
| "curl POST" | 0 | 0 | ✅ |
| "cron job" | 1 (TC-PHIEN-011) | 0 (đã sửa thành "verify list UI sau batch") | ✅ |
| "background worker" | 0 | 0 | ✅ |
| "API thuần" | 4 (TC-DGTV-100..103) | 0 (đã wrap UI bridge — verify network MCP + AUDIT_LOG UI) | ✅ |

**A7 acceptance:** ✅ PASS. 0 TC chỉ-DB/API thuần không có UI bridge.

---

## 6. Tổng kết Phase A done (post-Codex apply 2026-05-10)

| Metric | Value |
|--------|-------|
| Tổng TC active sau A1-A7 + Codex apply | **100** |
| Phân bố | 76 base + 18 edge A4 + 4 fill-gap A6 + 2 Codex P1 (P1-003/004) — 0 LOẠI net (TC-DN-100/101 RESTORE per Codex P1-001/002) |
| Coverage BR | 100% |
| Coverage AC | 96.2% (1 gap UI Cổng PLQG OOS) |
| Coverage Permission | 100% |
| Coverage Error code | 100% (sau Codex P1-003/004 cover Idempotency-Key/Content-Type + doanh_nghiep_id) |
| Coverage SM transitions | 100% |
| Coverage State lifecycle | 100% |
| Coverage Entity attribute | 100% |
| SPEC-CLARIFY pending BA | 11 |
| Quality score (A6) | 9.25/10 → **Codex 8.6/10 → final 9.4/10** sau apply |
| Codex Gate | **PASS (0 P0)** |
| LOẠI A7 net | 0 (2 RESTORE per Codex P1) |
| Đáp ứng §3.1 A7 Filter rule | ✅ (UI bridge wrap cho mọi TC API thuần) |

**Phase A:** ✅ **DONE** + Codex review applied — sẵn sàng Phase B.

---

*Generated 2026-05-10 — Phase A step A7 (Manual UI/function-testable filter)*
