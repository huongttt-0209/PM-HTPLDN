# Audit — PCNTHDG_11 (row 62) · Verdict: Open

## Cổng 1 — Evidence đối tác
- KQ mong đợi đối tác: (1) "Đã trình phê duyệt phân công"; (2) chuyển đợt → "Chờ duyệt phân công"; (3) **Gửi thông báo cho Cán bộ phê duyệt cùng đơn vị**.
- KQ thực tế đối tác: "Hệ thống không gửi thông báo cho cán bộ phê duyệt cùng đơn vị".

## Cổng 2 — Hiểu bug
- Test: CB NV trình phê duyệt phân công → verify (a) message + state, (b) CB PD cùng đơn vị có nhận thông báo không. Bug đối tác báo = thiếu (3) thông báo cho CB PD.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, đợt DG-20260720-0002, id eaf06391-...)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Message + state | KQ mong đợi #1/#2 | Toast "Đã trình phê duyệt phân công"; state Phân công → Chờ duyệt PC (CHO_DUYET_PC) | ĐẠT |
| Gửi TB CB PD | SCR-VI-01 #38 (dòng 864): "[Trình phê duyệt] (→ SET CHO_DUYET_PC + **gửi TB CB PD**)". Confirm modal app: "Phân công sẽ được gửi cho cán bộ phê duyệt" | [cbnv_tw] trình lúc ~13:39 → POST .../phan-congs/submit [200]. [cbpd_tw] cùng donViId (00000000-...-0001), đợt hiện đúng trong hàng đợi CHO_DUYET_PC, NHƯNG GET /api/v1/thong-baos: mới nhất 2026-07-16, không có TB nào ngày 07-20 / về đợt này (anyToday=false). Re-fetch: vẫn trống → không phải delay async | **THIẾU** |

- Evidence: `action-log.txt`.

## Verdict: Open
- Message + chuyển trạng thái đạt, nhưng thiếu bước SRS-mandated "gửi TB CB PD" (dòng 864) — CB phê duyệt cùng đơn vị không nhận thông báo dù đợt đã vào hàng đợi duyệt. Khớp báo cáo đối tác.
- Mã lỗi nội bộ: BUG-PCNTHDG_11.
