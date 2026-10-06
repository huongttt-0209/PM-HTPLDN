# Audit — CPCTHTTDVQL_03 (BC Chi phí theo đơn vị — thẻ Chỉ số tổng hợp)

**Verdict:** BA confirm. Actual đối tác đúng (app có thẻ Chỉ số tổng hợp), tranh chấp đặc tả.

## Evidence đã xem
- Đối tác: `partner-evidence/CPCTHTTDVQL_03.jpg` — env `htpldn-uat.ospgroup.vn`, tài khoản admin QTHT, 16/07/2026 16:16. Thấy 2 thẻ "Tổng hồ sơ = 25" + "Tổng chi phí = 226.308.268" + chart bar theo đơn vị + bảng "Đơn vị / Số hồ sơ / Tổng chi phí / TB chi phí".
- Env test: `web-kpi.png` — env `18.143.165.120.nip.io`, `cbnv_tw` (Toàn quốc), 21/07/2026 14:54. Thấy 2 thẻ "Tổng hồ sơ = 1" + "Tổng chi phí = 8,000,000" + chart + bảng cùng cấu trúc.

## So sánh 2 môi trường
- Cùng bố cục: 2 thẻ Chỉ số tổng hợp + chart Bar cross-tab + bảng theo đơn vị. Chỉ khác số liệu (env test có 1 hồ sơ chi phí 8 triệu; đối tác 25 hồ sơ 226 triệu).
- → Hiện tượng "app hiển thị chỉ số tổng hợp" tái hiện đúng trên env test, không phụ thuộc build/data cụ thể.

## Phân tích API
- `GET /api/v1/bao-cao/chi-phi-theo-don-vi?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` (200) trả:
  `{"tongHoSo":1,"tongChiPhi":8000000,"rows":[{"tenDonVi":"Cục Bổ trợ tư pháp - Bộ Tư pháp","soHoSo":1,"tongChiPhi":8000000,"trungBinhChiPhi":8000000}],"chartType":"BAR_CROSS_TAB"}`
- BE trả sẵn `tongHoSo` + `tongChiPhi` ở top-level → aggregate là chủ đích của backend, FE chỉ render.

## Điểm cần BA chốt
- SRS §Output FR-IX-16 (dòng 752-758) không liệt kê thẻ chỉ số tổng hợp; aggregate KPI thuộc FR-IX-15 (dòng 718-724). SCR-IX-01 (dòng 1039-1054) không có component KPI card.
- SRS không cấm rõ ràng → cần BA quyết: giữ (bổ sung spec) hay bỏ (gửi Dev). Xem `../../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md`.
