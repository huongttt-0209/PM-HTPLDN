# Audit — CPCTHTTLHDN_03 (BC Chi phí theo loại hình DN — thẻ Chỉ số tổng hợp)

**Verdict:** BA confirm. Actual đối tác đúng (app có thẻ Chỉ số tổng hợp), tranh chấp đặc tả.

## Evidence đã xem
- Đối tác: `partner-evidence/CPCTHTTLHDN_03.jpg` — env `htpldn-uat.ospgroup.vn`, admin QTHT, 16/07/2026 16:25. Thấy 2 thẻ "Tổng hồ sơ = 25" + "Tổng chi phí = 226.308.268" + chart Grouped bar 6 metric × 3 loại hình.
- Env test: `web-kpi.png` — `18.143.165.120.nip.io`, `cbnv_tw` (Toàn quốc), 21/07/2026 14:59. Thấy 2 thẻ "Tổng hồ sơ = 1" + "Tổng chi phí = 8,000,000" + chart Grouped bar 6 metric + bảng đúng §Output FR-IX-18.

## So sánh 2 môi trường
- Cùng bố cục: 2 thẻ Chỉ số tổng hợp + chart Grouped bar (6 metric) + bảng theo loại hình. Chỉ khác số liệu.
- → Hiện tượng "app hiển thị chỉ số tổng hợp" tái hiện đúng trên env test.

## Phân tích API
- `GET /api/v1/bao-cao/chi-phi-theo-loai-dn?...` (200) trả:
  `{"tongHoSo":1,"tongChiPhi":8000000,"data":[{"quyMoDn":"SIEU_NHO","tenQuyMo":"Siêu nhỏ","soHoSo":1,"tongChiPhi":8000000,"mucHoTroPhanTram":100,"tranChiPhiMoiHoSo":30000000,"tranChiPhi":30000000,"chenhLech":-22000000}],"chartType":"GROUPED_BAR"}`
- BE trả sẵn `tongHoSo` + `tongChiPhi` top-level → aggregate là chủ đích backend; bảng `data[]` khớp §Output FR-IX-18 (thêm `tranChiPhiMoiHoSo` = Trần/hồ sơ, ngoài spec nhưng hợp lý).

## Điểm cần BA chốt
- SRS §Output FR-IX-18 (dòng 831-839) liệt kê cột theo loại hình (loai_dn, ten_loai_dn, muc_ho_tro, so_ho_so, tong_chi_phi, tran_chi_phi, chenh_lech), KHÔNG có thẻ chỉ số tổng hợp; aggregate KPI thuộc FR-IX-15. SCR-IX-01 (dòng 1039-1054) không có component KPI card.
- SRS không cấm rõ ràng → cần BA quyết. Xem `../../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md`.
