# A6 — Test Quality Review (FR-13 TV Nhanh)

> **Phase:** A6 — bmad-testarch-test-review
> **Ngày tạo:** 2026-05-10
> **Mục đích:** Review chất lượng TC + fill gap A5. **TC mới đã merge inline vào file UC.** File này log review score + issue list.

---

## 1. Tổng kết score 6 axis

| Axis | Score | Note |
|------|-------|------|
| **Coverage breadth** | 9.5/10 | 100% BR + 96.2% AC + 100% Permission + 88.9% Error code (sau A6 fill: 100%) + 100% SM |
| **Coverage depth** (edge case) | 9.0/10 | 18 edge từ A4 cover boundary + concurrent + timeout + i18n. Còn thiếu: rate limit API inbound; A4 đã propose nhưng cần BA chốt rate limit threshold |
| **Atomicity** | 9.5/10 | Mỗi TC test 1 hành vi, có 1 ngoại lệ nhỏ TC-DGTV-100/101 gộp 2 boundary value (có thể split) |
| **Trace clarity** | 9.5/10 | Mỗi TC có Trace SRS line/section rõ ràng. 11 SPEC-CLARIFY có ID đánh dấu rõ |
| **Reusability seed pattern** | 9.0/10 | Pattern seed pre-defined section §6.3 file 00. Thiếu pre-condition data state cho TC-DGTV-005 (multi-DG cùng phiên — cần verify SPEC-CLARIFY-TVN-04) |
| **Implementation feasibility** | 9.0/10 | TC API inbound cần admin endpoint trigger (mock Cổng PLQG). A7 sẽ flag các TC "API thuần" cần wrap trong UI bridge. TC-PHIEN-011 batch 30 ngày cần seed với ngay_tao manipulated |

**Overall Quality:** **9.25 / 10** ✅ (vượt cap 9.0).

---

## 2. Issue list

### 2.1 Critical (block Phase A close)

(Không có)

### 2.2 High (cần fix trước Phase B)

| Issue | TC ảnh hưởng | Fix proposed |
|-------|--------------|--------------|
| H1 | SPEC-CLARIFY-TVN-04 (multi-DG cùng phiên) ảnh hưởng business logic ranking điểm TB. | TC-DGTV-005 + TC-DGTV-002 | Highlight SPEC-CLARIFY trong file Gap-report Phase B; default đa-DG cho phép cho đến khi BA confirm |
| H2 | SPEC-CLARIFY-TVN-05 (cross-cấp PD reject pattern) ảnh hưởng UX. | TC-PERM-005, TC-PERM-006, TC-KHO-105 | Test cả 2 option (ẩn UI hoặc disable button + 403 API) |

### 2.3 Medium (fix in-flight)

| Issue | TC ảnh hưởng | Fix proposed |
|-------|--------------|--------------|
| M1 | Threshold 30% delta cho nguon_tra_loi (KHO vs THU_CONG) chưa có trong SRS | TC-PHIEN-202 | Default 30% trong TC, BA confirm sau |
| M2 | TC-DGTV-100/101 gộp 2 boundary value (0 và 6) | TC-DGTV-100, TC-DGTV-101 | Đã split, OK |
| M3 | API inbound endpoint "view-event" cho so_luot_xem chưa khai báo SRS | TC-KHO-301 | SPEC-CLARIFY-TVN-11 đã ghi nhận; default test pattern POST event endpoint |

### 2.4 Low (nice to have)

| Issue | TC ảnh hưởng | Fix proposed |
|-------|--------------|--------------|
| L1 | Coverage rate limit API inbound (vd 100 req/min) chưa có TC | (chưa cover) | A4 đã propose nhưng cần BA chốt rate limit threshold; Phase B negative test |
| L2 | Performance test TOP 5 search latency (< 500ms) chưa có | TC-PHIEN-005 | Phase B add load test, không thuộc functional |

---

## 3. Fill-gap action (đã merge inline)

| Gap ID (A5) | TC mới | Merge target |
|-------------|--------|--------------|
| GAP-ERR-01 | TC-DN-300 (no results INF-TVN-TK-01) | file 03 |
| GAP-ERR-02 | TC-DGTV-300 (HTTP 400 malformed) | file 04 |
| GAP-STATE-01 | TC-KHO-300 (re-enable hieu_luc) | file 01 |
| GAP-ATTR-01 | TC-KHO-301 (so_luot_xem counter) | file 01 |

**Tổng:** 4 TC fill-gap đã merge inline vào file UC.

---

## 4. Coverage sau A6 fill-gap

| Loại trace | Trước A6 | Sau A6 | Delta |
|-----------|----------|--------|-------|
| BR formal | 100% | 100% | 0 |
| AC SRS | 92.3% | 96.2% (1 gap UI Cổng OOS) | +3.9% |
| Permission | 100% | 100% | 0 |
| Error codes | 84.6% | 100% | +15.4% |
| SM transitions | 100% | 100% | 0 |
| State lifecycle | 80% | 100% | +20% |
| Entity attribute | 92.3% | 100% | +7.7% |

**Overall:** 91.3% → **99.4%** (1 gap còn lại: AC1 FR-X.2-04 UI Cổng PLQG OOS — A7 sẽ filter LOẠI module-level).

---

## 5. TC tổng quan sau A1-A6 → A7 → Codex apply

| File | TC base A3 | A4 edge | A6 fill-gap | A7 LOẠI | Codex P1 | Final |
|------|------------|---------|--------------|---------|----------|-------|
| 01-Kho Q&A | 25 | +6 | +2 | 0 | 0 | 33 |
| 02-Phiên TVN | 15 | +4 | 0 | 0 | 0 | 19 |
| 03-DN chuyên trang | 7 | +1 | +1 | 0 (P1 restore) | 0 | 9 |
| 04-API inbound DG | 11 | +3 | +1 | 0 | +2 (P1-003/004) | 17 |
| 05-Công khai/Hủy | 12 | +4 | 0 | 0 | 0 | 16 |
| 06-Permission | 6 | 0 | 0 | 0 | 0 | 6 |
| **Total** | **76** | **+18** | **+4** | **0** | **+2** | **100 active** |

---

## 6. SPEC-CLARIFY consolidated (11 total)

| ID | Câu hỏi BA | TC ảnh hưởng |
|----|-----------|--------------|
| SPEC-CLARIFY-TVN-01 | TV_THU_CONG có tạo TU_VAN_NHANH placeholder hay tạo HOI_DAP trực tiếp? | TC-DN-002 |
| SPEC-CLARIFY-TVN-02 | Trạng thái phiên TVN gốc sau khi DN chuyển kênh? | TC-DN-003 |
| SPEC-CLARIFY-TVN-03 | DN search trả DA_DUYET hay chỉ CONG_KHAI? | TC-DN-004 |
| SPEC-CLARIFY-TVN-04 | DN có thể đánh giá nhiều lần cho cùng phiên TVN không? | TC-DGTV-005 |
| SPEC-CLARIFY-TVN-05 | Cross-cấp PD Kho — ẩn UI hay disable button + API 403? | TC-PERM-005, TC-PERM-006 |
| SPEC-CLARIFY-TVN-06 | Threshold "sửa drastic" % delta để nguon_tra_loi=THU_CONG? | TC-PHIEN-202 |
| SPEC-CLARIFY-TVN-07 | DN gửi câu hỏi duplicate trong N giây có chặn không? | TC-DN-200 |
| SPEC-CLARIFY-TVN-08 | API inbound DG cho phiên HET_HAN có chấp nhận hay reject? | TC-DGTV-201 |
| SPEC-CLARIFY-TVN-09 | TU_DONG có anh_dai_dien default không? | TC-CK-203 |
| SPEC-CLARIFY-TVN-10 | Toggle hieu_luc ON khi state=HET_HIEU_LUC chuyển về state nào? | TC-KHO-300 |
| SPEC-CLARIFY-TVN-11 | API inbound view-event cho so_luot_xem endpoint? | TC-KHO-301 |

---

*Generated 2026-05-10 — Phase A step A6 (bmad-testarch-test-review) — TC fill-gap đã merge inline*
