# VVTTG_01 (row 213) — Reconciliation số liệu

> **✅ Re-verify #2 2026-07-23 — PASS (Closed).** Báo cáo "Vụ việc theo thời gian" (Năm 2026, Toàn quốc, `cbnv_tw_04`) nay trả đúng 2 chuỗi: **Tiếp nhận = 14** (khớp `vu-viec-tiep-nhan` = 14 + dashboard 14), **Hoàn thành = 5** (khớp `vu-viec-hoan-thanh` = 5). API `vu-viec-theo-thoi-gian` data[0] = `{soVuViec:14, tiepNhan:14, hoanThanh:5}`, `theoDonVi[]` đủ 4 đơn vị (Σ=14). Hết mâu thuẫn 6≠14 bên dưới. Bằng chứng `reverify2-VVTTG_01-2series-14-5.png`.

---

**Đo gốc — 2026-07-21 (Verdict lúc đó: Open, trùng gốc BUG-VVTTG_03).** Tài khoản `cbnv_tw_04`, kỳ Năm/Tháng 2026, Toàn quốc.

## Số liệu đo được (API cookie-auth, cùng kỳ/phạm vi)

| Endpoint | Chỉ số | Tổng năm 2026 |
|---|---|:-:|
| `bao-cao/vu-viec-theo-thoi-gian` (VVTTG — case này) | `soVuViec` | **6** |
| `bao-cao/vu-viec-tiep-nhan` (SRS: `tiep_nhan`) | `tongVuViec` | 14 |
| `bao-cao/vu-viec-hoan-thanh` (SRS: `hoan_thanh`) | `tongVuViec` | 5 |

## Breakdown theo tháng

| Kỳ | VVTTG `soVuViec` | Tiếp nhận | Hoàn thành |
|---|:-:|:-:|:-:|
| T01 | 1 | 1 | 0 |
| T02 | 1 | 2 | 1 |
| T03 | 2 | 2 | 2 |
| T04 | 1 | 1 | 1 |
| T07 | 1 | 8 | 1 |
| **Tổng** | **6** | **14** | **5** |

## Kết luận

- `soVuViec = 6` không khớp tiếp nhận (14) cũng không khớp hoàn thành (5) — lệch mạnh ở T07 (1 vs 8 tiếp nhận).
- SRS FR-IX-05 §Output (dòng 337) yêu cầu mỗi kỳ có 2 chỉ số `{tiep_nhan, hoan_thanh}`; BE trả 1 chỉ số `soVuViec` không rõ định nghĩa → đối tác thấy "số liệu không chính xác" là có cơ sở.
- BE có đủ data 2 chuỗi (2 endpoint riêng trả 14 và 5); vấn đề là báo cáo "theo thời gian" gộp về 1 con số ngoài đặc tả.
- **Cùng gốc lỗi cấu trúc với BUG-VVTTG_03** (batch1, row 215). VVTTG_01 là triệu chứng → tham chiếu, không log bug trùng.

Evidence: `vvttg-report-nam-kpi6.png` (UI kỳ Năm — KPI 6, biểu đồ 1 chuỗi "Số vụ việc", không bảng chi tiết).
