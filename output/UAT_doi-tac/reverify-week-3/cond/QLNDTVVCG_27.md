# Bảng đối chiếu điều kiện — QLNDTVVCG_27 (row 288) — Hoàn thành TV → thông báo CB Phê duyệt

**Case:** CG bấm **"Hoàn thành tư vấn"** → hệ thống **KHÔNG gửi thông báo** tới Cán bộ Phê duyệt cùng đơn vị.
**Điểm neo SRS:** Processing Hoàn thành TV `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:196` (step 5: "Auto chuyển → CHO_PHE_DUYET, **gửi thông báo CB Phê duyệt cùng đơn vị**" | BR-FLOW-01); SM dòng 1508 (`HOAN_THANH → CHO_PHE_DUYET | Auto | Action = **TB CB PD** | BR-FLOW-01`).
**GATE Internal:** TB do hành động nội bộ CG "Hoàn thành" sinh ra → verify TRÊN CMS (chuông + API notifications của CB PD), KHÔNG punt external.
**Verify:** 21/07/2026, Chrome DevTools MCP. Account: CG `qa_tvvseed28` (hoàn thành) + CB PD `cbpd_tw_04` (người nhận TB).

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLNDTVVCG_27.webm) | Mình test | GAP? |
|---|---|---|:-:|
| Role sinh TB (CG hoàn thành) | CG (TVV·CG) bấm "Hoàn thành tư vấn" | `qa_tvvseed28` (TVV·CG) bấm [Hoàn thành], nhập kết quả (165 ký tự) → POST `/hoan-thanh` 200, toast "Đã hoàn thành tư vấn" | Không |
| Record chuyển đúng state | Record → "Chờ phê duyệt" | TVCS-20260721-0003: DANG_TU_VAN → HOAN_THANH → **auto CHO_PHE_DUYET** (stepper 4 bước ✓, API `trangThai=CHO_PHE_DUYET`) | Không |
| Người nhận TB = CB PD cùng đơn vị | CB Phê duyệt cùng đơn vị | `cbpd_tw_04` (CB_PD_TW) donViId `00000000-0000-4000-8000-000000000001` = donViId record (khớp) → đúng người duyệt (record nằm trong list `?trangThai=CHO_PHE_DUYET` của account này) | Không |
| Hệ thống TB có hoạt động cho account này | (không rõ trong video) | `cbpd_tw_04` NHẬN được 4 TB "CT HTPL...gửi phê duyệt" (CT-0001→0004) → kênh TB/chuông của account hoạt động bình thường | Không |

**Kết quả verify (0 GAP):**
- Sau khi CG hoàn thành record → chuông CB PD `cbpd_tw_04` vẫn **4 chưa đọc**, cả 4 đều là TB CT HTPL cũ (timestamp 08:37–08:45Z, có từ trước), **KHÔNG có TB nào về TVCS-20260721-0003**.
- API `GET /api/v1/thong-baos?pageSize=100` (đúng endpoint thực): tổng 4 item, không item nào tham chiếu record TVCS vừa hoàn thành. Chờ thêm 45s re-fetch: vẫn 4, unread-count vẫn 4 → loại trừ delay async.
- Đối chứng: cùng account `cbpd_tw_04` NHẬN TB "gửi phê duyệt" cho CT HTPL → kênh TB chạy; riêng luồng TVCS `HOAN_THANH → CHO_PHE_DUYET` **không phát TB "TB CB PD"** như SRS dòng 196/1508 (BR-FLOW-01) yêu cầu.
- Record vẫn vào hàng chờ duyệt của CB PD (auto-transition + scope filter OK) → CB PD tự tìm được nếu chủ động mở danh sách, nhưng KHÔNG được thông báo chủ động ⇒ có workaround (Major).
- Evidence: `bug-reports/tvcs/image/BD-case27-cbpd-notifications-noTVCS.png` (panel chuông CB PD chỉ có 4 TB CT HTPL); `BD-case27-R1-chophduyet.png` (record ở CHO_PHE_DUYET).

**Verdict:** `Open` — Tái hiện đúng phản ánh đối tác. Record chuyển CHO_PHE_DUYET nhưng CB Phê duyệt cùng đơn vị KHÔNG nhận thông báo (vi phạm SRS dòng 196 step 5 + SM dòng 1508, BR-FLOW-01). Bug: `bug-reports/tvcs/Pass-bug-report-tvcs-batchD.md` (BUG-QLNDTVVCG_27).
