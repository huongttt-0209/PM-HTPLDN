# VVTLV_01 (row 241) — Biểu đồ vs Bảng — Reconciliation — 2026-07-21

**Verdict: Open** (trùng gốc BUG-VVTLV_03 batch3). Tài khoản `cbnv_tw_04`, kỳ Năm 2026, Toàn quốc.

## So sánh biểu đồ vs bảng (lĩnh vực "Thương mại")

| Nguồn | Giá trị "Thương mại" | Ghi chú |
|---|:-:|---|
| Biểu đồ (hover tooltip) | **7** | Chỉ 1 chuỗi legend = "Cục Bổ trợ tư pháp - Bộ Tư pháp" — bằng đúng số riêng đơn vị này |
| Bảng tổng hợp (cột Tổng số) | **16** | Tổng toàn bộ 4 đơn vị |
| API `theoDonVi[]` | 7 + 4 + 2 + 3 = **16** | Cục Bổ trợ 7, Bộ KH&ĐT 4, STP HN 2, STP AG 3 |

## Bằng chứng đo

- Chart DOM: `.recharts-bar` series = **1**; legend 1 item ("Cục Bổ trợ tư pháp - Bộ Tư pháp"); 2 cột (Thuế h≈30px ≈ 1, Thương mại h≈210px). Tooltip cột Thương mại: `"Thương mại — Cục Bổ trợ tư pháp - Bộ Tư pháp : 7"`.
- Bảng: `[["Lĩnh vực PL","Tổng số"],["Thuế","1"],["Thương mại","16"]]`.
- API `vu-viec-theo-linh-vuc`: `chartType:"GROUPED_BAR"`, Thương mại `tongSo:16` gồm 4 `theoDonVi`.

## Kết luận

- Biểu đồ vẽ **1 đơn vị** (Cục Bổ trợ, Thương mại = 7), bỏ 3 đơn vị (Bộ KH&ĐT, STP HN, STP AG). Bảng hiển thị tổng 16 → **biểu đồ ≠ bảng** đúng như đối tác phản ánh.
- BE trả đủ 4 đơn vị + `chartType:"GROUPED_BAR"`; lỗi ở FE dựng biểu đồ chỉ 1 chuỗi đơn vị.
- **Cùng gốc lỗi với BUG-VVTLV_03** (batch3, row 242 — thiếu breakdown theo đơn vị ở cả bảng và biểu đồ). VVTLV_01 là triệu chứng → tham chiếu, không log bug trùng.

Evidence ảnh: `vvtlv-report-nam.png`, `vvtlv-chart-vs-table.png` (biểu đồ 1 legend đơn vị + bảng Thuế 1 / Thương mại 16). Ảnh gốc biểu đồ 1 chuỗi: `bug-reports/bctk/image/BUG-VVTLV_03-web.png`.

> Lưu ý capture: 2 ảnh chụp qua CDP không hiện rõ cột (layer SVG bar chưa vào ảnh); giá trị cột lấy từ tooltip + DOM (opacity 1, màu xanh) nên người dùng thực vẫn thấy cột. Điểm mấu chốt (1 chuỗi đơn vị, Thương mại = 7 ≠ 16) đã xác thực bằng tooltip + DOM + API.
