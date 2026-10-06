# Audit — CPCTHTTTG_03 (BC Chi phí theo thời gian — Biểu đồ đường + bảng)

**Verdict:** BA confirm. Claim "trục tung toàn bộ 0" KHÔNG tái hiện đúng — điểm Tổng chi phí khác 0; chỉ Số hồ sơ hiện ~0 do trộn scale count+money (cùng root CPCTHTTLHDN_04). SRS không quy định trục phụ.

## Evidence đã xem
- Đối tác: `partner-evidence/CPCTHTTTG_03.jpg` — env `htpldn-uat.ospgroup.vn`, admin QTHT, 16/07/2026. Line chart 2 series (Số hồ sơ xanh dương + Tổng chi phí xanh lá), 1 kỳ "2026". Điểm **Tổng chi phí ở đỉnh (~226M)**, điểm **Số hồ sơ (=25) ở đáy 0**. KPI: Tổng chi phí toàn kỳ 226.308.268, Tổng hồ sơ 25. Bảng: 2026, 01/01–31/12, Số hồ sơ 25, Tổng chi phí 226.308.268đ.
- Env test: `web-chart.png` — `18.143.165.120.nip.io`, `cbnv_tw` (Toàn quốc), 21/07/2026 15:11. Line chart 2 series, trục tung `0→8.000.000`. Điểm **Tổng chi phí (xanh lá) ở đỉnh ≈8M**, điểm **Số hồ sơ (xanh dương, =1) ở đáy 0**. KPI: Tổng chi phí 8.000.000, Tổng hồ sơ 1. Bảng: 2026, 01/01–31/12, Số hồ sơ 1, Tổng chi phí 8.000.000đ.

## So sánh 2 môi trường
- Cùng bố cục Line chart 2 series; điểm Tổng chi phí ở đỉnh (khác 0), điểm Số hồ sơ ở đáy (~0) do scale tiền. Chỉ khác số liệu tuyệt đối. → tái hiện đúng hiện tượng "Số hồ sơ hiện 0", KHÔNG đúng "toàn bộ 0".

## Phân tích API
- `GET /api/v1/bao-cao/chi-phi-theo-thoi-gian?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` (200) trả:
  `{"tongChiPhiToanKy":8000000,"tongHoSoToanKy":1,"data":[{"kyLabel":"2026","tuNgayKy":"2026-01-01","denNgayKy":"2026-12-31","soHoSo":1,"tongChiPhi":8000000}],"chartType":"LINE"}`
- BE trả số khác 0 (tongChiPhi 8M, soHoSo 1) → data không lỗi; biểu đồ vẽ đúng số. Số hồ sơ=1 hiện ~0 do dùng chung trục với tiền.

## Đối chiếu SRS v3.5
- Mapping UC142 (`srs-fr-11-bao-cao.md:1078`): "Line chart trend" — không định nghĩa trục/series composition.
- FR-IX-19 §Output (`srs-fr-11-bao-cao.md:869`): `trend_data[] = {ky_label, tong_chi_phi, so_ho_so}` (Luôn), `chart_type = LINE`. → SRS §Output CÓ đưa cả so_ho_so vào trend_data nên vẽ 2 series là khớp; nhưng KHÔNG quy định tách trục cho so_ho_so.
- AC (`:874`): "12 tháng → line chart 12 điểm trend chi phí". Kỳ=Năm chỉ 1 kỳ (2026) → 1 điểm là đúng filter, không phải lỗi.

## Điểm cần BA chốt
- Claim đối tác "trục tung toàn bộ 0" **không chính xác** (Tổng chi phí point khác 0). Không phải data bug.
- Vấn đề legibility: Số hồ sơ (đếm) và Tổng chi phí (tiền) chung 1 trục tung → Số hồ sơ hiện ~0, không đọc được. SRS không quy định. Cần BA/design quyết: tách trục phụ cho Số hồ sơ, hay chỉ vẽ trend chi phí (bỏ Số hồ sơ khỏi biểu đồ, giữ ở bảng)? Xem `../../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md`.
