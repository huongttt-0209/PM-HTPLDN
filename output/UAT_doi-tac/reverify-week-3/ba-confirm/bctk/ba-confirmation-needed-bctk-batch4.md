# BA confirmation needed — BCTK Batch 4 (họ Chương trình HTPLDN) — 2026-07-21

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** vì SRS chưa quy định rõ, cần BA quyết. Batch 4 verify 4 case (CTTDVQL_02, CTTDVQL_03, CTTLV_03, CTTLV_04); trong đó **CTTDVQL_02 + CTTLV_03** cần BA xác nhận (2 case này cùng 1 vấn đề: báo cáo có thẻ chỉ số tổng hợp mà §Output đặc thù không liệt kê). CTTDVQL_03 (Open) đã log ở `../../bug-reports/bctk/Pass-bug-report-bctk-batch4.md`; CTTLV_04 **đổi Reject → `BA confirm` (re-verify 22/07/2026)** — chi tiết ở `ba-confirm-CTTLV_04.md` + `../../reverify-audit/CTTLV_04/`.

> **Môi trường verify:** https://18.143.165.120.nip.io · Chrome DevTools MCP · tài khoản `cbnv_tw_01` (CB Nghiệp vụ - Trung ương) · kỳ Năm 2026 · đơn vị Toàn quốc · đã seed chương trình HTPLDN đã duyệt (được báo cáo đếm).

---

## CTTDVQL_02 (và CTTLV_03) — Báo cáo hiển thị thẻ chỉ số tổng hợp mà §Output đặc thù không liệt kê

**Bối cảnh testcase**

- Dòng Excel: **266**, mã TC `CTTDVQL_02` — BC Chương trình theo đơn vị (FR-IX-21 / UC144); đối tác phản ánh **"KPI thừa"** (báo cáo hiện thẻ chỉ số tổng hợp không có trong đặc tả).
- Dòng Excel: **271**, mã TC `CTTLV_03` — BC Chương trình theo lĩnh vực (FR-IX-22 / UC145); đối tác phản ánh **"KPI thừa"** (cùng bản chất vấn đề).
- Nội dung kiểm tra: CB Nghiệp vụ TW xem 2 báo cáo trên, quan sát khối thẻ chỉ số (KPI card) phía trên biểu đồ/bảng.
- Expected trong file UAT: đối tác kỳ vọng **không có thẻ chỉ số tổng hợp riêng** cho các báo cáo này (chỉ có biểu đồ + bảng dữ liệu).

**Kết quả verify UI hiện tại**

- Verify ngày **21/07/2026** qua Chrome DevTools MCP, tài khoản `cbnv_tw_01` (CB Nghiệp vụ - Trung ương), kỳ Năm 2026, đơn vị Toàn quốc.
- **CTTDVQL_02 — BC Chương trình theo đơn vị:** phía trên biểu đồ/bảng hiển thị **2 thẻ chỉ số**: "Tổng chương trình" và "Tổng ngân sách". Evidence: `../../reverify-audit/CTTDVQL_02/cttdvql-report-kpi-cards.png`.
- **CTTLV_03 — BC Chương trình theo lĩnh vực:** phía trên biểu đồ/bảng hiển thị **2 thẻ chỉ số**: "Tổng chương trình" và "Tổng DN tham gia". Evidence: `../../reverify-audit/CTTLV_03/cttlv-report-thuongmai-kpi.png`.
- Cả 2 báo cáo: biểu đồ + bảng dữ liệu phía dưới hiển thị đúng theo §Output đặc thù; điểm tranh cãi **chỉ nằm ở khối thẻ chỉ số**.

**Điểm mâu thuẫn trong SRS v3.5**

1. **§Output đặc thù của từng báo cáo KHÔNG liệt kê thẻ chỉ số tổng hợp riêng** — chỉ liệt kê cột bảng dữ liệu:
   - FR-IX-21 (CT theo đơn vị): cột `don_vi`, `cap_don_vi`, `so_ct`, `tong_ngan_sach`.
   - FR-IX-22 (CT theo lĩnh vực): cột `linh_vuc_id`, `ten_linh_vuc`, `so_ct`, `so_dn_tham_gia`.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:939` – `:945` (FR-IX-21 §Output đặc thù)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:979` – `:984` (FR-IX-22 §Output đặc thù)

2. **Nhưng Template chung TPL-REPORT-FULL lại CÓ trường tổng hợp `tong_ban_ghi` ("Tổng số bản ghi")** áp dụng cho báo cáo full — có thể được FE hiện thực hoá thành thẻ chỉ số tổng hợp:

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:100` (Template TPL-REPORT-FULL, trường `tong_ban_ghi`)

**Câu hỏi cần BA xác nhận**

Hai báo cáo **BC Chương trình theo đơn vị** (CTTDVQL_02) và **BC Chương trình theo lĩnh vực** (CTTLV_03) có **được/nên hiển thị thẻ chỉ số tổng hợp** ("Tổng chương trình", "Tổng ngân sách", "Tổng DN tham gia") ở đầu báo cáo không?

1. **Hướng 1 — theo §Output đặc thù từng báo cáo:** không hiển thị thẻ chỉ số riêng, chỉ có biểu đồ + bảng → UI hiện tại **thừa thẻ chỉ số** (khớp phản ánh đối tác), owner `Dev FE` (ẩn khối KPI).
2. **Hướng 2 — theo Template chung TPL-REPORT-FULL:** thẻ chỉ số tổng hợp là thành phần chuẩn của báo cáo full → UI hiện tại **đúng**, cần cập nhật lại expected của đối tác cho CTTDVQL_02 + CTTLV_03.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth (§Output đặc thù vs Template chung).
- Tạm verdict cho `CTTDVQL_02` (row 266) và `CTTLV_03` (row 271): **`Cần BA xác nhận`**.
- Nếu BA chọn **Hướng 1**: UI hiện tại `Vẫn lỗi` (thừa thẻ chỉ số), owner dự kiến `Dev FE` (ẩn khối KPI card của 2 báo cáo).
- Nếu BA chọn **Hướng 2**: UI hiện tại `Đúng` — thẻ chỉ số tổng hợp là chuẩn báo cáo full; QA cập nhật lại expected của đối tác, không gửi Dev.

---

*BA confirmation doc generated: 2026-07-21 15:55:00 | QA via Claude Code*
