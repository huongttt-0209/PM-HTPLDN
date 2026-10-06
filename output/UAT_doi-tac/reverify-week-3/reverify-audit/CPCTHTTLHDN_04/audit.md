# Audit — CPCTHTTLHDN_04 (BC Chi phí theo loại hình DN — Biểu đồ + bảng tổng hợp)

**Verdict:** BA confirm. SRS Mapping chỉ ghi "Grouped bar" (không định nghĩa series); tranh chấp thành phần biểu đồ + claim "trục tung toàn bộ 0" KHÔNG tái hiện đúng.

## Evidence đã xem
- Đối tác: `partner-evidence/CPCTHTTLHDN_04.jpg` — env `htpldn-uat.ospgroup.vn`, admin QTHT, 16/07/2026. Chart Grouped bar 6 metric × 3 loại hình (Nhỏ/Siêu nhỏ/Vừa). Tooltip "Nhỏ": Chênh lệch **-211.843.371đ**, Mức hỗ trợ **30**, Số hồ sơ **11**, Trần/hồ sơ **30M**, Trần chi phí **330M**, Tổng chi phí **118M** → có giá trị, KHÔNG phải 0. Bảng 3 dòng.
- Env test: `web-chart.png` — `18.143.165.120.nip.io`, `cbnv_tw` (Toàn quốc), 21/07/2026 14:59. Chart Grouped bar, nhóm "Siêu nhỏ": Tổng chi phí ≈8M (xanh lá +), Trần/hồ sơ ≈30M (đỏ +), Trần chi phí ≈30M (tím +), Chênh lệch ≈-22M (teal −). Số hồ sơ (1) + Mức hỗ trợ% (100) vô hình vì trục tung scale tiền. Legend đủ 6 series.

## So sánh 2 môi trường
- Cùng bố cục biểu đồ: Grouped bar plot 6 metric số (Chênh lệch / Mức hỗ trợ % / Số hồ sơ / Trần / hồ sơ / Trần chi phí / Tổng chi phí) nhóm theo loại hình DN. → Thành phần biểu đồ tái hiện đúng.
- Cả 2 env: bar tiền (chục-trăm triệu) có giá trị rõ; count/% bị nén ~0 do dùng chung trục tung với tiền.

## Phân tích API
- `GET /api/v1/bao-cao/chi-phi-theo-loai-dn?...` (200) trả:
  `{"tongHoSo":1,"tongChiPhi":8000000,"data":[{"quyMoDn":"SIEU_NHO","tenQuyMo":"Siêu nhỏ","soHoSo":1,"tongChiPhi":8000000,"mucHoTroPhanTram":100,"tranChiPhiMoiHoSo":30000000,"tranChiPhi":30000000,"chenhLech":-22000000}],"chartType":"GROUPED_BAR"}`
- BE trả đủ 6 metric số per loại hình → chart plot 6 series là do BE/FE chủ đích, không phải data lỗi. Giá trị Số hồ sơ=1, Mức hỗ trợ=100 → nhỏ so scale tiền → hiện ~0.

## Đối chiếu 2 ý đối tác báo
1. **"Biểu đồ cột theo nhiều nhóm mà tài liệu không yêu cầu"** — ĐÚNG thực tế (chart plot 6 metric). Nhưng SRS Mapping UC141 chỉ ghi "Grouped bar" + bộ lọc "Loại DN" — KHÔNG định nghĩa series nào; đối tác kỳ vọng "nhóm theo loại hình và mức hỗ trợ" cũng là 1 cách diễn giải, không có dòng SRS chốt. → tranh chấp đặc tả.
2. **"Trục tung hiển thị toàn bộ giá trị 0"** — SAI theo nghĩa đen. Bar tiền (Tổng chi phí, Trần/hồ sơ, Trần chi phí, Chênh lệch) có giá trị; chỉ Số hồ sơ + Mức hỗ trợ% ẩn ~0 do trộn scale. Ảnh chính đối tác cũng cho thấy giá trị khác 0.

## Điểm cần BA chốt
- SRS Mapping (`srs-fr-11-bao-cao.md:1077`): UC141 = "Grouped bar", bộ lọc "Loại DN" — không quy định series.
- SRS §Output FR-IX-18 (`srs-fr-11-bao-cao.md:831-839`): liệt kê cột **bảng** (loai_dn, ten_loai_dn, muc_ho_tro, so_ho_so, tong_chi_phi, tran_chi_phi, chenh_lech) — không mô tả series biểu đồ.
- Cần BA quyết: (a) thành phần series của biểu đồ Grouped bar; (b) có tách trục phụ (secondary axis) cho Số hồ sơ / Mức hỗ trợ % để đọc được không (hiện bị nén thành 0 do dùng chung trục tiền). Xem `../../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md`.
