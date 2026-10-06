# BA confirmation needed — BCTK Batch 1 (DISPLAY họ Vụ việc nhóm 1) — 2026-07-21

> **File này để làm gì:** gom các testcase batch 1 (module Báo cáo Thống kê, cụm hiển thị chỉ số/biểu đồ/bảng) mà QA đối chiếu SRS xong nhưng khác biệt nằm ở **đặc tả** (kỳ vọng đối tác ≠ SRS, hoặc SRS silent) → cần BA chốt. Bug có SRS reference rõ (app sai clause SRS) đã log vào `../../bug-reports/bctk/Pass-bug-report-bctk-batch1.md`.
>
> **Vai trò verify:** `cbnv_tw` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc). Môi trường `https://18.143.165.120.nip.io`. Kỳ = Năm 2026, Đơn vị = Toàn quốc (trùng cấu hình đối tác).
>
> **SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`.

---

## SLHDVM_03 — Bảng thống kê "theo đơn vị" khác thiết kế PTYC (SRS chỉ có cột Số lượng)

**Bối cảnh testcase**

- Dòng Excel: 190, mã TC `SLHDVM_03`.
- Nội dung kiểm tra: CB Nghiệp vụ TW mở Báo cáo thống kê → BC Số lượng hỏi đáp/vướng mắc pháp luật (UC124) → Kỳ Năm 2026 → Toàn quốc → Xem báo cáo → đối chiếu chỉ số + biểu đồ + bảng.
- Expected trong file UAT (đối tác): "Hệ thống hiển thị các trường thông tin giống với thiết kế" — thiết kế đối tác dẫn là tài liệu PTYC-CT v2.0.
- Actual đối tác ghi: "Bảng kết quả không giống với thiết kế".

**Đối chiếu SRS v3.5**

- SRS FR-IX-01 §Output đặc thù liệt kê 7 nhóm dữ liệu: `tong_hoi_dap`, `da_tra_loi`, `cho_tra_loi`, `ty_le_tra_loi`, `theo_linh_vuc[] {linh_vuc, ten, so_luong}`, `theo_don_vi[] {don_vi, ten, so_luong}`, `theo_ky[]` (trend).
- Bảng "theo đơn vị" theo SRS chỉ có 2 chiều dữ liệu: **tên đơn vị + số lượng** — KHÔNG có cột "Đã trả lời" hay "Tỷ lệ" ở cấp đơn vị.
- Biểu đồ kỳ vọng (bảng Mapping): **Donut + Trend** — Donut theo lĩnh vực + biểu đồ xu hướng theo kỳ.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:159-167` (§Output đặc thù FR-IX-01)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1060` (Mapping: Donut + Trend)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW (Toàn quốc).
- URL: `https://18.143.165.120.nip.io/bao-cao?loai=hoi-dap&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- 4 chỉ số hiển thị đủ: Tổng hỏi đáp = 11, Đã trả lời = 9, Chờ trả lời = 2, Tỷ lệ trả lời = 81,8%.
- Có biểu đồ tròn (donut) theo lĩnh vực (Thương mại 54,5% · Thuế 36,4% · Lao động 9,1%) + biểu đồ xu hướng "Số lượng" theo kỳ.
- Bảng "Lĩnh vực PL / Số lượng" (Thương mại 6, Thuế 4, Lao động 1) và bảng "Đơn vị / Số lượng" (Cục Bổ trợ tư pháp 10, Sở Tư pháp Hà Nội 1) — cả 2 bảng đều đúng cấu trúc SRS {tên, số lượng}.
- Evidence: `../../reverify-audit/SLHDVM_03/SLHDVM_03-web-kpi.png`, `SLHDVM_03-web-tables.png`.

**Kết luận QA**

- `SLHDVM_03` KHÔNG phải bug theo SRS v3.5 — web hiển thị đúng toàn bộ 7 nhóm dữ liệu + đúng loại biểu đồ (Donut + Trend) mà SRS FR-IX-01 quy định.
- Khác biệt "không giống thiết kế" là do thiết kế PTYC-CT v2.0 của đối tác quy định bảng "theo đơn vị" có thêm cột Tổng hỏi đáp / Đã trả lời / Tỷ lệ — các cột này KHÔNG có trong SRS §Output.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt hướng xử lý bảng thống kê theo đơn vị của BC Số lượng hỏi đáp:

- **Hướng 1 (giữ theo SRS):** bảng theo đơn vị chỉ gồm cột Đơn vị + Số lượng → web hiện tại đúng, cập nhật lại expected của `SLHDVM_03` cho khớp SRS.
- **Hướng 2 (bổ sung theo PTYC):** thêm cột "Đã trả lời" + "Tỷ lệ (%)" vào bảng theo đơn vị → cần cập nhật SRS §Output FR-IX-01 + gửi Dev bổ sung.
- Verdict QA đề xuất: `Cần BA xác nhận` (đặc tả PTYC vs SRS lệch nhau), chưa gửi Dev cho tới khi BA chốt source truth.

---

## VVDHT_03 — Chỉ số tổng hợp nhanh (KPI card) chỉ có 1 thẻ, các mức SLA nằm ở bảng/biểu đồ

**Bối cảnh testcase**

- Dòng Excel: 201, mã TC `VVDHT_03`.
- Nội dung kiểm tra: CB Nghiệp vụ TW mở BC Vụ việc đang hỗ trợ (UC126) → Kỳ Năm 2026 → Toàn quốc → Xem báo cáo → đối chiếu "Chỉ số tổng hợp nhanh".
- Expected đối tác (theo PTYC): các chỉ số nhanh gồm Tổng đang xử lý, Sắp hết hạn, Quá hạn, Quá hạn nghiêm trọng.
- Actual đối tác ghi: "Màn hình hiển thị thiếu các chỉ số: Sắp hết hạn, Quá hạn, Quá hạn nghiêm trọng".

**Đối chiếu SRS v3.5**

- SRS FR-IX-03 §Output liệt kê 4 trị scalar (đều "Luôn"): `tong_dang_xu_ly`, `binh_thuong` (SLA bình thường), `canh_bao` (SLA sắp hết hạn), `qua_han` (SLA quá hạn). KHÔNG có "Quá hạn nghiêm trọng" trong §Output — đó chỉ là 1 giá trị của **bộ lọc đầu vào** `muc_sla`.
- SCR-IX-01 §Thành phần màn hình chỉ spec component "Biểu đồ" (item 10) + "Bảng dữ liệu" (item 11) — KHÔNG có component "thẻ chỉ số / KPI card". Khái niệm "Chỉ số tổng hợp nhanh" đến từ thiết kế PTYC, không có trong SCR-IX-01.

**Citation**

- `srs-fr-11-bao-cao.md:255-262` (§Output đặc thù FR-IX-03: tong_dang_xu_ly, binh_thuong, canh_bao, qua_han)
- `srs-fr-11-bao-cao.md:245` (muc_sla input: BINH_THUONG / SAP_HET_HAN / QUA_HAN / QUA_HAN_NGHIEM_TRONG)
- `srs-fr-11-bao-cao.md:1050-1052` (SCR-IX-01 chỉ có Biểu đồ + Bảng dữ liệu, không có KPI card)

**Kết quả verify UI hiện tại**

- Verify 21/07/2026 qua Chrome DevTools MCP, `cbnv_tw` (Toàn quốc). URL `.../bao-cao?loai=vu-viec-dang-ho-tro&kyBaoCao=NAM...`.
- Chỉ có 1 thẻ chỉ số: "Tổng vụ việc = 7".
- Các mức SLA hiển thị đầy đủ ở **biểu đồ cột** (Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng) + **bảng "Mức SLA"**: Bình thường 7, Sắp hết hạn 0, Quá hạn 0, Quá hạn nghiêm trọng 0.
- Evidence: `../../reverify-audit/VVDHT_03/VVDHT_03-web-kpi.png`, `VVDHT_03-web-slatable.png`.

**Kết luận QA**

- `VVDHT_03` không phải bug về mất dữ liệu — mọi mức SLA mà SRS §Output yêu cầu đều đã hiển thị (trong bảng "Mức SLA" + biểu đồ cột).
- Khác biệt: đối tác muốn mỗi mức SLA là 1 thẻ "Chỉ số tổng hợp nhanh" riêng (theo PTYC); SRS §Output liệt kê các trị nhưng SCR-IX-01 KHÔNG spec dạng thẻ KPI. "Quá hạn nghiêm trọng" không nằm trong §Output.

**Nội dung đề xuất BA phản hồi đối tác**

- **Hướng 1 (giữ theo SRS/hiện tại):** các mức SLA hiển thị trong bảng "Mức SLA" + biểu đồ cột là đủ theo §Output → cập nhật expected `VVDHT_03`.
- **Hướng 2 (bổ sung theo PTYC):** thêm thẻ chỉ số nhanh cho từng mức SLA → cần bổ sung component KPI card vào SCR-IX-01 + gửi Dev. Lưu ý "Quá hạn nghiêm trọng" cần bổ sung vào §Output nếu muốn có thẻ này.
- Verdict QA đề xuất: `Cần BA xác nhận`.

---

## VVTTG_02 — BC Vụ việc theo thời gian hiển thị thẻ chỉ số tổng, đối tác kỳ vọng "không có chỉ số riêng"

**Bối cảnh testcase**

- Dòng Excel: 214, mã TC `VVTTG_02`.
- Nội dung kiểm tra: CB Nghiệp vụ TW mở BC Vụ việc theo thời gian (UC128) → Kỳ Năm 2026 → Toàn quốc → Xem báo cáo → đối chiếu chỉ số tổng hợp.
- Expected đối tác (theo PTYC): báo cáo dạng trend theo thời gian, **không có chỉ số/KPI tổng hợp riêng**.
- Actual đối tác ghi: "Hệ thống hiển thị chỉ số tổng hợp" (tức app có thẻ chỉ số mà thiết kế đối tác không có).

**Đối chiếu SRS v3.5**

- SRS FR-IX-05 §Output đặc thù chỉ liệt kê 3 nhóm dữ liệu: `trend_data[] {ky_label, tiep_nhan, hoan_thanh}`, `theo_don_vi[] {don_vi, ten, trend_data[]}`, `chart_type = LINE`. **KHÔNG có** trường chỉ số/KPI scalar (kiểu "tổng vụ việc toàn kỳ") trong §Output.
- Tuy nhiên §Output cũng **không cấm** hiển thị một con số tổng — đây là giá trị suy ra được từ tổng `trend_data`, mang tính phụ trợ, không mâu thuẫn với bất kỳ clause nào của SRS.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:335-339` (§Output đặc thù FR-IX-05: trend_data, theo_don_vi, chart_type — không có KPI scalar)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1064` (Mapping UC128 = Line chart trend)

**Kết quả verify UI hiện tại**

- Verify 21/07/2026 qua Chrome DevTools MCP, `cbnv_tw` (Toàn quốc). URL `.../bao-cao?loai=vu-viec-theo-thoi-gian&kyBaoCao=NAM...`.
- Có 1 thẻ chỉ số "Tổng vụ việc toàn kỳ = 6" + biểu đồ đường theo kỳ.
- API `GET /api/v1/bao-cao/vu-viec-theo-thoi-gian` trả `tongVuViecToanKy: 6` (feed thẻ tổng) + `data[]` trend + `chartType: LINE`.
- Evidence: `../../reverify-audit/VVTTG_02/VVTTG_02-web-kpi.png`.

**Kết luận QA**

- `VVTTG_02` không phải bug theo SRS v3.5 — thẻ "Tổng vụ việc toàn kỳ" là số liệu phụ trợ, không nằm trong §Output nhưng cũng không vi phạm §Output (SRS im lặng: không yêu cầu, không cấm).
- Khác biệt: thiết kế PTYC của đối tác không có chỉ số riêng cho báo cáo trend; app lại hiện 1 thẻ tổng. Đây là lệch giữa PTYC và implementation, không phải lỗi nghiệp vụ.

**Nội dung đề xuất BA phản hồi đối tác**

- **Hướng 1 (giữ thẻ tổng — hiện tại):** thẻ "Tổng vụ việc toàn kỳ" hữu ích cho người đọc, không vi phạm SRS → cập nhật expected `VVTTG_02` cho khớp (chấp nhận có thẻ tổng).
- **Hướng 2 (bỏ thẻ theo PTYC):** ẩn thẻ chỉ số để báo cáo trend chỉ còn biểu đồ + bảng đúng thiết kế đối tác → gửi Dev FE ẩn KPI card cho loại BC này.
- Verdict QA đề xuất: `Cần BA xác nhận` (SRS im lặng — BA chốt giữ hay bỏ thẻ tổng).
