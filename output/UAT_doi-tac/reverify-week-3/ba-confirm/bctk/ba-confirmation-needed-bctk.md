# BA confirmation needed — Báo cáo Thống kê — UAT tuần 3 — 2026-07-21

> Tài liệu tổng hợp các nội dung cần BA xác nhận của module Báo cáo Thống kê từ 6 nhóm kiểm thử UAT tuần 3. Nội dung chi tiết, citation, evidence và đề xuất QA được giữ nguyên từ các file nguồn.

---

## Nhóm 1 — DISPLAY họ Vụ việc nhóm 1

> **File này để làm gì:** gom các testcase batch 1 (module Báo cáo Thống kê, cụm hiển thị chỉ số/biểu đồ/bảng) mà QA đối chiếu SRS xong nhưng khác biệt nằm ở **đặc tả** (kỳ vọng đối tác ≠ SRS, hoặc SRS silent) → cần BA chốt. Bug có SRS reference rõ (app sai clause SRS) đã log vào `../../bug-reports/bctk/Pass-bug-report-bctk-batch1.md`.
>
> **Vai trò verify:** `cbnv_tw` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc). Môi trường `https://18.143.165.120.nip.io`. Kỳ = Năm 2026, Đơn vị = Toàn quốc (trùng cấu hình đối tác).
>
> **SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`.

---

### SLHDVM_03 — Bảng thống kê "theo đơn vị" khác thiết kế PTYC (SRS chỉ có cột Số lượng)

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

### VVDHT_03 — Chỉ số tổng hợp nhanh (KPI card) chỉ có 1 thẻ, các mức SLA nằm ở bảng/biểu đồ

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

### VVTTG_02 — BC Vụ việc theo thời gian hiển thị thẻ chỉ số tổng, đối tác kỳ vọng "không có chỉ số riêng"

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

---

## Nhóm 2 — DISPLAY họ Đào tạo / CG-TVV / Đánh giá

> **File này để làm gì:** gom các testcase batch 2 (module Báo cáo Thống kê, cụm hiển thị chỉ số/biểu đồ/bảng — họ Đào tạo / CG-TVV / Đánh giá) mà QA đối chiếu SRS xong nhưng khác biệt nằm ở **đặc tả** (kỳ vọng đối tác ≠ SRS, hoặc SRS silent về chi tiết chiều biểu đồ) → cần BA chốt. Bug có SRS reference rõ (app sai clause SRS) đã log vào `../../bug-reports/bctk/Pass-bug-report-bctk-batch2.md`.
>
> **Vai trò verify:** `cbnv_tw` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc). Môi trường `https://18.143.165.120.nip.io`. Kỳ = Năm 2026, Đơn vị = Toàn quốc.
>
> **SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`.

---

### CLDTBDDDR_04 — Biểu đồ cột hiển thị theo Đơn vị (đối tác kỳ vọng theo Hình thức) + không có biểu đồ đường xu hướng

**Bối cảnh testcase**

- Dòng Excel: 221, mã TC `CLDTBDDDR_04`.
- Nội dung kiểm tra: CB Nghiệp vụ TW mở BC Lớp đào tạo đang diễn ra (UC129) → Kỳ Năm 2026 → Toàn quốc → Xem báo cáo → đối chiếu biểu đồ.
- Expected trong file UAT (đối tác):
  - Biểu đồ cột thống kê **theo hình thức** (trực tuyến / trực tiếp).
  - Có thêm **biểu đồ đường thể hiện xu hướng**.
- Actual đối tác ghi: "SRS yêu cầu biểu đồ cột theo hình thức, app hiển thị theo Đơn vị; thiếu biểu đồ đường xu hướng".

**Đối chiếu SRS v3.5**

- Bảng Mapping 23 loại BC quy định biểu đồ của báo cáo này = **"Bar (snapshot)"** — chỉ nêu LOẠI biểu đồ (cột), KHÔNG quy định trục ngang là hình thức hay đơn vị.
- §Mô tả FR-IX-06: báo cáo snapshot "phân theo hình thức (trực tuyến/trực tiếp), lĩnh vực, đơn vị" — cả 3 đều là chiều phân tích; SRS không chỉ định chiều nào là trục chính của biểu đồ.
- Vì là báo cáo **snapshot** (đếm khóa đang diễn ra tại thời điểm), SRS Mapping KHÔNG kèm "Trend" → không có biểu đồ đường xu hướng cho báo cáo này (khác FR-IX-07 "Bar + Trend").
- SCR-IX-01 item 10 (Biểu đồ): "Tùy loại BC: Line (trend) / Bar / Stacked bar / Donut / Radar" — không prescribe chiều dữ liệu của trục.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1065` (Mapping: BC Lớp đào tạo đang diễn ra → "Bar (snapshot)")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:355` (§Mô tả FR-IX-06: phân theo hình thức, lĩnh vực, đơn vị)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1050` (SCR-IX-01 item 10 — loại biểu đồ, không nêu chiều trục)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW (Toàn quốc).
- URL: `https://18.143.165.120.nip.io/bao-cao?loai=lop-dao-tao-dang-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- Có đúng **1 biểu đồ cột (Bar)**: trục ngang = **Đơn vị** (Bộ Kế hoạch và Đầu tư — tại thời điểm verify Toàn quốc có 1 lớp đang diễn ra), chuỗi phân màu theo **hình thức** (legend "Trực tuyến"). → Biểu đồ CÓ thể hiện chiều hình thức (dưới dạng chuỗi màu), trục ngang là đơn vị.
- KHÔNG có biểu đồ đường xu hướng (đúng vì báo cáo là snapshot, SRS Mapping không có Trend).
- (Đối tác test 15/07 có 3 lớp: Cục Bổ trợ 2 + Sở Tư pháp An Giang 1 — cùng cấu trúc biểu đồ x=đơn vị. Số lượng lớp thay đổi theo thời gian vì đây là snapshot.)
- Evidence: `../../reverify-audit/CLDTBDDDR_04/CLDTBDDDR_04-web-chart-theodonvi.png`

**Kết luận QA**

- App render **đúng loại biểu đồ SRS quy định** ("Bar (snapshot)") và vẫn thể hiện chiều hình thức (chuỗi màu), chỉ khác ở việc chọn trục ngang = đơn vị thay vì hình thức.
- SRS **không prescribe** trục ngang của biểu đồ cột phải là hình thức → không đủ căn cứ kết luận `Open`.
- Yêu cầu "thêm biểu đồ đường xu hướng" KHÔNG có trong SRS (báo cáo snapshot) → app không thiếu theo SRS hiện tại.
- Khác biệt thuộc **đặc tả** (kỳ vọng đối tác về chiều trục + trend) → cần BA chốt.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt hướng hiển thị biểu đồ của BC Lớp đào tạo đang diễn ra:

- **Câu hỏi 1 — trục biểu đồ:** biểu đồ cột nên để trục ngang theo **HÌNH THỨC** (đúng mục đích báo cáo "phân theo hình thức trực tuyến/trực tiếp") hay giữ theo **ĐƠN VỊ** như hiện tại (hình thức là chuỗi màu)?
- **Câu hỏi 2 — biểu đồ xu hướng:** có bổ sung biểu đồ đường xu hướng cho báo cáo này không? (SRS hiện quy định snapshot, chỉ có Bar, không có Trend.)
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA chốt "trục theo hình thức" và/hoặc "bổ sung trend" → cập nhật SRS Mapping/§Output + gửi Dev; nếu giữ nguyên → cập nhật expected `CLDTBDDDR_04` cho khớp SRS.

---

### LDTBDDDR_04 — Biểu đồ cột (BC Lớp đào tạo đã diễn ra) hiển thị theo Đơn vị (đối tác kỳ vọng theo Hình thức)

**Bối cảnh testcase**

- Dòng Excel: 226, mã TC `LDTBDDDR_04`.
- Nội dung kiểm tra: CB Nghiệp vụ TW mở BC Lớp đào tạo **đã diễn ra** (UC130) → Kỳ Năm 2026 → Toàn quốc → Xem báo cáo → đối chiếu biểu đồ.
- Expected trong file UAT (đối tác): biểu đồ cột thống kê **theo hình thức** (trực tuyến / trực tiếp).
- Actual đối tác ghi: "SRS yêu cầu biểu đồ cột theo hình thức, app hiển thị theo Đơn vị".
- ⚠️ Ghi chú evidence: đối tác gắn **nhầm ảnh** vào dòng 226 (dùng lại ảnh của `CLDTBDDDR_04.jpg` = báo cáo "đang diễn ra"). QA verify trực tiếp báo cáo "đã diễn ra" đúng trên web để lấy bằng chứng chuẩn.

**Đối chiếu SRS v3.5**

- Bảng Mapping 23 loại BC quy định biểu đồ báo cáo này = **"Bar + Trend"** — nêu 2 LOẠI biểu đồ (cột + xu hướng), KHÔNG quy định trục ngang của biểu đồ cột là hình thức hay đơn vị.
- §Output FR-IX-07 liệt kê: `tong_da_dien_ra`, `tong_hoc_vien`, `theo_don_vi[]`, `theo_hinh_thuc[]` {hinh_thuc, so_kh, so_hv}, `theo_ky[]` — cả đơn vị, hình thức, kỳ đều là chiều phân tích "Luôn".
- §Mô tả FR-IX-07: "báo cáo khóa học đã kết thúc trong kỳ, phân theo hình thức, đơn vị, kèm tổng số học viên".

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1066` (Mapping: BC Lớp đào tạo đã diễn ra → "Bar + Trend")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:416-422` (§Output FR-IX-07: theo_don_vi, theo_hinh_thuc, theo_ky)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:397` (§Mô tả FR-IX-07)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW (Toàn quốc).
- URL: `https://18.143.165.120.nip.io/bao-cao?loai=lop-dao-tao-da-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- Hiển thị 2 thẻ chỉ số: Tổng khóa học = 5, Tổng học viên = 11.
- Có **2 biểu đồ** đúng loại Mapping "Bar + Trend":
  - Biểu đồ cột (Bar): trục ngang = **Đơn vị** (Cục Bổ trợ 2 khóa, Bộ KH&ĐT 1, Sở Tư pháp Hà Nội 2), chuỗi Số khóa học / Số học viên.
  - Biểu đồ đường (Trend): trục ngang = **kỳ** (2026-02 → 2026-12), chuỗi Số khóa học / Số học viên.
- Bảng "Đơn vị | Số khóa học | Số học viên | **Trực tuyến | Trực tiếp**": chiều hình thức được thể hiện dưới dạng **cột trong bảng** (Trực tuyến/Trực tiếp), không phải trục của biểu đồ cột.
- API `chartType: "BAR_TREND"`, trả `theoDonVi[]` (kèm trucTuyen/trucTiep) + `trendData[]` (5 điểm theo tháng); KHÔNG có `theoHinhThuc[]` aggregate riêng — hình thức nằm trong bảng theo đơn vị.
- Evidence: `../../reverify-audit/LDTBDDDR_04/LDTBDDDR_04-web-bar-theodonvi.png`

**Kết luận QA**

- App render **đúng 2 loại biểu đồ SRS quy định** ("Bar + Trend") và thể hiện chiều hình thức (Trực tuyến/Trực tiếp) trong bảng theo đơn vị. Khác biệt chỉ ở việc biểu đồ cột lấy trục ngang = đơn vị thay vì hình thức.
- SRS **không prescribe** trục ngang của biểu đồ cột phải là hình thức → không đủ căn cứ `Open`.
- Khác biệt thuộc **đặc tả** → cần BA chốt (cùng bản chất với `CLDTBDDDR_04`).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt trục biểu đồ cột của BC Lớp đào tạo đã diễn ra:

- **Câu hỏi:** biểu đồ cột nên để trục ngang theo **HÌNH THỨC** (trực tuyến/trực tiếp — đúng mục đích "phân theo hình thức") hay giữ theo **ĐƠN VỊ** như hiện tại (hình thức đã có trong bảng)?
- Verdict QA đề xuất: `Cần BA xác nhận`. Đề nghị BA quyết chung 1 hướng cho cả họ báo cáo Đào tạo (`CLDTBDDDR_04` + `LDTBDDDR_04`) để nhất quán.

---

### CGTVPL_04 — Biểu đồ tròn (BC Số lượng CG/TVV) theo Đơn vị (đối tác kỳ vọng theo Loại TVV/CG); biểu đồ cột "không hiển thị" KHÔNG tái hiện

**Bối cảnh testcase**

- Dòng Excel: 229, mã TC `CGTVPL_04`.
- Nội dung kiểm tra: CB Nghiệp vụ TW mở BC Số lượng CG/TVV (UC131) → Kỳ Năm 2026 → Toàn quốc → Xem báo cáo → đối chiếu biểu đồ.
- Expected trong file UAT (đối tác): biểu đồ tròn thống kê **theo loại** (TVV / CG).
- Actual đối tác ghi: "SRS yêu cầu biểu đồ tròn theo loại, app hiển thị theo Đơn vị; biểu đồ cột không hiển thị".

**Đối chiếu SRS v3.5**

- Bảng Mapping quy định biểu đồ báo cáo này = **"Donut + Bar"** — nêu 2 LOẠI biểu đồ (tròn + cột), KHÔNG quy định biểu đồ tròn thể hiện chiều loại hay đơn vị.
- §Output FR-IX-08 liệt kê scalar `tong_tvv`, `so_tvv`, `so_cg` + `theo_don_vi[]` {don_vi, ten, tvv, cg} + `theo_linh_vuc[]`. Chiều **loại (TVV/CG)** được thể hiện qua các trị scalar `so_tvv`/`so_cg` (không có mảng `theo_loai[]` riêng).
- §Mô tả FR-IX-08: "snapshot số lượng CG/TVV đang hoạt động, phân theo loại, lĩnh vực, đơn vị".

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1067` (Mapping: BC Số lượng CG/TVV → "Donut + Bar")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:458-466` (§Output FR-IX-08: tong_tvv/so_tvv/so_cg, theo_don_vi, theo_linh_vuc)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:437` (§Mô tả FR-IX-08)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW (Toàn quốc).
- URL: `https://18.143.165.120.nip.io/bao-cao?loai=so-luong-cg-tvv&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- 3 thẻ chỉ số: Tổng Tư vấn viên = 5, **Số Tư vấn viên = 5, Số Chuyên gia = 0** → chiều loại (TVV/CG) ĐƯỢC thể hiện ở thẻ chỉ số.
- Biểu đồ tròn (Donut): thể hiện tỷ lệ theo **Đơn vị** (Cục Bổ trợ 40%, Bộ KH&ĐT 20%, Sở Tư pháp Hà Nội 20%, Sở Tư pháp An Giang 20%) — không theo loại.
- Biểu đồ cột (Bar): **CÓ hiển thị**, theo Đơn vị (Số Tư vấn viên: Cục Bổ trợ 2, các đơn vị khác 1). → Ý "biểu đồ cột không hiển thị" của đối tác KHÔNG tái hiện.
- Bảng "Đơn vị | Số Tư vấn viên | Số Chuyên gia | Tổng số": chiều loại cũng có trong cột bảng.
- API `chartType: "DONUT_BAR"`.
- Evidence: `../../reverify-audit/CGTVPL_04/CGTVPL_04-web-donut-theodonvi.png`

**Kết luận QA**

- App render **đúng 2 loại biểu đồ SRS quy định** ("Donut + Bar") và thể hiện chiều loại (TVV/CG) qua thẻ chỉ số + cột bảng. Khác biệt chỉ ở việc biểu đồ tròn lấy chiều = đơn vị thay vì loại.
- SRS **không prescribe** biểu đồ tròn phải thể hiện chiều loại → không đủ căn cứ `Open`. → Đặc tả, cần BA chốt.
- Ý phụ đối tác "biểu đồ cột không hiển thị" **KHÔNG tái hiện** (bar có hiển thị) → không phải lỗi.
- (Ghi chú: trong khi verify, phát hiện thêm 1 lỗi ngoài phạm vi câu hỏi này — app KHÔNG render phần "theo lĩnh vực" dù BE trả `theoLinhVuc` — đã log riêng vào `../../bug-reports/bctk/Pass-bug-report-bctk-batch2.md`.)

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt chiều biểu đồ tròn của BC Số lượng CG/TVV:

- **Câu hỏi:** biểu đồ tròn nên thể hiện tỷ lệ theo **LOẠI** (Tư vấn viên vs Chuyên gia — đúng mục đích báo cáo "Số lượng CG/TVV") hay giữ theo **ĐƠN VỊ** như hiện tại (loại đã có ở thẻ chỉ số + bảng)?
- Verdict QA đề xuất: `Cần BA xác nhận`. Ý "biểu đồ cột không hiển thị" của đối tác không đúng thực tế (bar có hiển thị).

---

### CLDTBDPL_04 — Biểu đồ (BC Chất lượng đào tạo) nhãn trục theo Đơn vị (đối tác kỳ vọng theo Khóa học); "thiếu đường điểm TB" KHÔNG tái hiện

**Bối cảnh testcase**

- Dòng Excel: 236, mã TC `CLDTBDPL_04`.
- Nội dung kiểm tra: CB Nghiệp vụ TW mở BC Chất lượng đào tạo (UC133) → Kỳ Năm 2026 → Toàn quốc → Xem báo cáo → đối chiếu biểu đồ.
- Expected trong file UAT (đối tác): biểu đồ thống kê **theo khóa học** + có **đường điểm trung bình**.
- Actual đối tác ghi: "SRS yêu cầu biểu đồ theo khóa học, app hiển thị theo Đơn vị; thiếu đường điểm TB".

**Đối chiếu SRS v3.5**

- Bảng Mapping quy định biểu đồ báo cáo này = **"Bar + Line"** — nêu 2 LOẠI biểu đồ (cột + đường), KHÔNG quy định trục ngang là khóa học hay đơn vị.
- §Output FR-IX-10 liệt kê scalar `diem_trung_binh`, `ty_le_dat`, `tong_hoc_vien` + `theo_khoa_hoc[]` {khoa_hoc, ten_kh, diem_tb, ty_le_dat, so_hv} + `theo_don_vi[]` {don_vi, ten, diem_tb, ty_le_dat}. Cả khóa học và đơn vị đều là chiều phân tích "Luôn".
- §Mô tả FR-IX-10: "báo cáo chất lượng đào tạo: điểm TB kiểm tra, tỷ lệ đạt, phân theo khóa học, đơn vị".

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1069` (Mapping: BC Chất lượng đào tạo → "Bar + Line")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:544-548` (§Output FR-IX-10: diem_trung_binh, ty_le_dat, tong_hoc_vien, theo_khoa_hoc, theo_don_vi)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:524` (§Mô tả FR-IX-10)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW (Toàn quốc).
- URL: `https://18.143.165.120.nip.io/bao-cao?loai=chat-luong-dao-tao&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- Có **2 biểu đồ** đúng loại Mapping "Bar + Line":
  - Biểu đồ cột (Bar): chuỗi "Số học viên", 4 cột = 4 khóa học, nhãn trục ngang = **tên Đơn vị** (tooltip xác nhận "Sở Tư pháp Hà Nội / Số học viên: 3").
  - Biểu đồ đường (Line combo): 3 chuỗi **Số học viên / Tỷ lệ đạt / Điểm TB** — **đường Điểm TB CÓ hiển thị** (chuỗi màu xanh lá). → Ý "thiếu đường điểm TB" của đối tác KHÔNG tái hiện.
- Bảng "Mã KH | Tên KH | Đơn vị | Số học viên | Điểm TB | Tỷ lệ đạt": chiều khóa học được thể hiện đầy đủ trong bảng.
- API `chartType: "BAR_LINE"`, trả `danhSachKhoaHoc[]` (per-khóa-học, kèm tenDonVi) → dữ liệu biểu đồ là per-khóa-học nhưng nhãn trục dùng tên đơn vị.
- Evidence: `../../reverify-audit/CLDTBDPL_04/CLDTBDPL_04-web-chart-theodonvi-duongdiemTB.png`

**Kết luận QA**

- App render **đúng 2 loại biểu đồ SRS quy định** ("Bar + Line") và có **đường Điểm TB** như đối tác kỳ vọng. Khác biệt chỉ ở việc nhãn trục ngang = đơn vị thay vì khóa học.
- SRS **không prescribe** trục ngang biểu đồ phải là khóa học → không đủ căn cứ `Open`. → Đặc tả, cần BA chốt.
- Ý phụ đối tác "thiếu đường điểm TB" **KHÔNG tái hiện** (đường Điểm TB có hiển thị) → không phải lỗi. **Chính ảnh đối tác gửi (`../../partner-evidence/CLDTBDPL_04.jpg`) đã có đường "Điểm TB" (legend xanh lá) trong biểu đồ combo** — mâu thuẫn với nội dung họ ghi.
- **Lưu ý UI (BA cân nhắc):** dữ liệu biểu đồ là per-khóa-học (4 cột = 4 khóa) nhưng nhãn trục dùng tên đơn vị → 2 cột cùng nhãn "Cục Bổ trợ tư pháp" (2 khóa cùng đơn vị) khó phân biệt. Nếu giữ trục theo khóa học sẽ tự khắc phục vấn đề này.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt nhãn trục biểu đồ của BC Chất lượng đào tạo:

- **Câu hỏi:** biểu đồ nên để nhãn trục ngang theo **KHÓA HỌC** (mã/tên khóa — đúng mục đích "phân theo khóa học", đồng thời phân biệt được các khóa cùng đơn vị) hay giữ theo **ĐƠN VỊ** như hiện tại?
- Verdict QA đề xuất: `Cần BA xác nhận`. Ý "thiếu đường điểm TB" của đối tác không đúng thực tế (đường Điểm TB có hiển thị). Nếu BA chốt "trục theo khóa học" → gửi Dev đổi nhãn trục; nếu giữ nguyên → cập nhật expected `CLDTBDPL_04` cho khớp SRS.

---

## Nhóm 3 — DISPLAY: Vụ việc theo chiều / Chi phí / Số lượng chương trình

> **File này để làm gì:** gom các testcase batch 3 mà QA verify xong nhưng cần BA phản hồi đối tác (chủ yếu: đối tác kỳ vọng "không có / có" một thành phần hiển thị mà SRS §Output không quy định rõ). Bug có SRS reference rõ ràng → đã log vào `../../bug-reports/bctk/Pass-bug-report-bctk-batch3.md`.

> **Quy tắc citation:** SRS v3.5 = `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`. Mọi khẳng định dẫn số dòng thực đã mở file kiểm.

---

### CPCTHTTDVQL_03 — Đối tác cho rằng báo cáo "Chi phí theo đơn vị" KHÔNG được có thẻ Chỉ số tổng hợp, nhưng app hiện 2 thẻ (Tổng hồ sơ + Tổng chi phí)

**Bối cảnh testcase**

- Dòng Excel: 252, mã TC `CPCTHTTDVQL_03`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ TW xem báo cáo "BC Chi phí theo đơn vị" (UC139 / FR-IX-16), kiểm tra phần "Chỉ số tổng hợp".
- Expected trong file UAT: "Không có chỉ số tổng hợp riêng".
- Actual đối tác ghi: "Hệ thống hiển thị chỉ số tổng hợp" (2 thẻ: Tổng hồ sơ = 25, Tổng chi phí = 226.308.268).

**Đối chiếu SRS v3.5**

- FR-IX-16 §Output đặc thù chỉ liệt kê các trường **theo đơn vị** (cross-tab): `don_vi_id`, `ten_don_vi`, `tong_chi_phi`, `so_ho_so`, `trung_binh` — KHÔNG liệt kê thẻ chỉ số tổng hợp (aggregate Tổng hồ sơ / Tổng chi phí toàn quốc).
- Ngược lại, FR-IX-15 (BC Chi phí chi trả hỗ trợ) §Output có aggregate `tong_chi_phi`, `tong_ho_so`, `trung_binh_ho_so` là trường "Luôn" — tức thiết kế đặt phần chỉ số tổng hợp ở FR-IX-15, không ở FR-IX-16.
- SCR-IX-01 §Thành phần màn hình (dòng 1039–1054) KHÔNG có component "Chỉ số tổng hợp / KPI card" riêng — chỉ có biểu đồ (item 10) + bảng dữ liệu có hàng tổng cộng (item 11).
- SRS **không cấm rõ ràng** thẻ chỉ số tổng hợp ở FR-IX-16; chỉ là §Output không liệt kê. Aggregate hiển thị (Tổng hồ sơ, Tổng chi phí) là số đúng, suy ra trực tiếp từ bảng theo đơn vị.

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:752-758` (FR-IX-16 §Output — chỉ có trường theo đơn vị, không có aggregate KPI)
- `srs-v3.5/srs-fr-11-bao-cao.md:718-724` (FR-IX-15 §Output — aggregate tong_chi_phi/tong_ho_so/trung_binh ở đây)
- `srs-v3.5/srs-fr-11-bao-cao.md:1039-1054` (SCR-IX-01 thành phần màn hình — không có component KPI card)

**Kết quả verify UI hiện tại**

- Verify lại ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc).
- Mở URL `.../bao-cao?loai=chi-phi-theo-don-vi&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- UI hiển thị 2 thẻ Chỉ số tổng hợp: "Tổng hồ sơ = 1", "Tổng chi phí = 8,000,000" (env test ít data hơn đối tác) → **tái hiện đúng** hiện tượng đối tác báo.
- Chart Bar theo đơn vị + bảng "Đơn vị / Số hồ sơ / Tổng chi phí / TB chi phí" — đúng §Output FR-IX-16.
- Network: `GET /api/v1/bao-cao/chi-phi-theo-don-vi` trả `tongHoSo` + `tongChiPhi` ở top-level (BE chủ đích tính aggregate) → thẻ KPI không phải FE tự bịa.
- Evidence: `../../reverify-audit/CPCTHTTDVQL_03/web-kpi.png`

**Kết luận QA**

- `CPCTHTTDVQL_03`: actual đối tác **đúng thực tế** (app có hiển thị thẻ chỉ số tổng hợp), nhưng đây là bất đồng về **đặc tả** — SRS §Output FR-IX-16 không liệt kê thẻ chỉ số tổng hợp, cũng không cấm.
- Thẻ KPI hiển thị số liệu đúng (aggregate của bảng theo đơn vị, do BE tính). Không phải lỗi dữ liệu.
- Chưa đủ căn cứ Reject (đối tác quan sát đúng) hay Open (SRS không quy định rõ cấm).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: báo cáo "Chi phí theo đơn vị" (FR-IX-16) **có được phép** hiển thị thẻ chỉ số tổng hợp (Tổng hồ sơ + Tổng chi phí toàn phạm vi) không?

- Nếu BA đồng ý thẻ tổng hợp là hợp lệ/hữu ích → cập nhật expected của `CPCTHTTDVQL_03` (bỏ yêu cầu "không có chỉ số tổng hợp"); bổ sung §Output FR-IX-16 cho khớp implementation. Verdict: `Không phải bug theo SRS`.
- Nếu BA muốn giữ đúng thiết kế "FR-IX-16 không có KPI riêng" (chỉ FR-IX-15 mới có) → gửi Dev FE/BE bỏ thẻ chỉ số tổng hợp khỏi báo cáo này. Verdict: `Vẫn lỗi — owner: Dev FE/BE`.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt.

---

### CPCTHTTLHDN_03 — Đối tác cho rằng báo cáo "Chi phí theo loại hình DN" KHÔNG được có thẻ Chỉ số tổng hợp, nhưng app hiện 2 thẻ (Tổng hồ sơ + Tổng chi phí)

**Bối cảnh testcase**

- Dòng Excel: 255, mã TC `CPCTHTTLHDN_03`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ TW xem báo cáo "BC Chi phí theo loại hình DN" (UC141 / FR-IX-18), kiểm tra phần "Chỉ số tổng hợp".
- Expected trong file UAT: "Không có chỉ số tổng hợp riêng".
- Actual đối tác ghi: "Hệ thống hiển thị chỉ số tổng hợp" (2 thẻ: Tổng hồ sơ = 25, Tổng chi phí = 226.308.268).

**Đối chiếu SRS v3.5**

- FR-IX-18 §Output đặc thù chỉ liệt kê các trường **theo loại hình DN**: `loai_dn`, `ten_loai_dn`, `muc_ho_tro`, `so_ho_so`, `tong_chi_phi`, `tran_chi_phi`, `chenh_lech` — KHÔNG liệt kê thẻ chỉ số tổng hợp (aggregate Tổng hồ sơ / Tổng chi phí).
- Aggregate KPI (Tổng hồ sơ / Tổng chi phí) thuộc §Output của FR-IX-15 (BC Chi phí chi trả hỗ trợ), không phải FR-IX-18.
- SCR-IX-01 §Thành phần màn hình (dòng 1039–1054) không có component "Chỉ số tổng hợp / KPI card" riêng.
- SRS **không cấm rõ ràng** thẻ chỉ số tổng hợp ở FR-IX-18. Số liệu 2 thẻ đúng (aggregate của bảng theo loại hình, do BE tính).

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:831-839` (FR-IX-18 §Output — chỉ có trường theo loại hình, không có aggregate KPI)
- `srs-v3.5/srs-fr-11-bao-cao.md:718-724` (FR-IX-15 §Output — aggregate ở đây)
- `srs-v3.5/srs-fr-11-bao-cao.md:1039-1054` (SCR-IX-01 thành phần màn hình — không có component KPI card)

**Kết quả verify UI hiện tại**

- Verify lại ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` (Toàn quốc).
- Mở URL `.../bao-cao?loai=chi-phi-theo-loai-dn&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- UI hiển thị 2 thẻ Chỉ số tổng hợp "Tổng hồ sơ = 1", "Tổng chi phí = 8,000,000" (env test ít data hơn) → **tái hiện đúng** hiện tượng đối tác báo.
- Chart Grouped bar 6 metric + bảng "Quy mô DN / Số hồ sơ / Tổng chi phí / Mức hỗ trợ (%) / Trần/hồ sơ / Trần chi phí / Chênh lệch" — đúng §Output FR-IX-18.
- Network: `GET /api/v1/bao-cao/chi-phi-theo-loai-dn` trả `tongHoSo` + `tongChiPhi` ở top-level → thẻ KPI do BE cấp.
- Evidence: `../../reverify-audit/CPCTHTTLHDN_03/web-kpi.png`

**Kết luận QA**

- `CPCTHTTLHDN_03`: actual đối tác **đúng thực tế** (app có thẻ chỉ số tổng hợp), bất đồng về **đặc tả** — SRS §Output FR-IX-18 không liệt kê thẻ này, cũng không cấm.
- Cùng bản chất với `CPCTHTTDVQL_03` (cùng cụm "Chi phí — thẻ chỉ số tổng hợp") → nên chốt chung 1 hướng.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: các báo cáo Chi phí (FR-IX-16 / FR-IX-18) **có được phép** hiển thị thẻ chỉ số tổng hợp (Tổng hồ sơ + Tổng chi phí) không?

- Nếu đồng ý → cập nhật expected `CPCTHTTLHDN_03` + bổ sung §Output. Verdict: `Không phải bug theo SRS`.
- Nếu giữ thiết kế "chỉ FR-IX-15 có KPI tổng hợp" → gửi Dev bỏ thẻ. Verdict: `Vẫn lỗi — owner: Dev FE/BE`.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt.

---

### CPCTHTTLHDN_04 — Đối tác cho rằng biểu đồ "Chi phí theo loại hình DN" phải nhóm theo loại hình × mức hỗ trợ, nhưng app plot 6 metric số; đối tác còn báo "trục tung toàn bộ 0"

**Bối cảnh testcase**

- Dòng Excel: 256, mã TC `CPCTHTTLHDN_04`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ TW xem báo cáo "BC Chi phí theo loại hình DN" (UC141 / FR-IX-18), kiểm tra hiển thị **biểu đồ + bảng tổng hợp**.
- Expected trong file UAT: "Biểu đồ cột nhóm theo loại hình và mức hỗ trợ" + "Bảng tổng hợp: Loại hình, Mức hỗ trợ, Số hồ sơ, Tổng chi phí, Trần chi phí, Chênh lệch".
- Actual đối tác ghi (2 ý): (1) "Biểu đồ cột theo nhiều nhóm mà tài liệu không yêu cầu: Chênh lệch, Số hồ sơ, Trần / hồ sơ, Trần chi phí, Tổng chi phí"; (2) "Số liệu ở trục tung của biểu đồ hiển thị toàn bộ giá trị 0".

**Đối chiếu SRS v3.5**

- Mapping 23 loại BC (dòng 1077): `UC141 | BC Chi phí theo loại hình DN | Bộ lọc: Loại DN | Biểu đồ: Grouped bar`. SRS **chỉ ghi loại biểu đồ "Grouped bar" + bộ lọc "Loại DN"**, KHÔNG định nghĩa các series của biểu đồ là gì (không nói "nhóm theo mức hỗ trợ" như đối tác kỳ vọng, cũng không nói phải plot 6 metric như app).
- FR-IX-18 §Output (dòng 831-839) mô tả các cột **bảng** (loai_dn, ten_loai_dn, muc_ho_tro, so_ho_so, tong_chi_phi, tran_chi_phi, chenh_lech) — bảng app khớp §Output (thêm cột "Trần / hồ sơ" = tranChiPhiMoiHoSo, ngoài spec nhưng hợp lý). §Output KHÔNG mô tả series biểu đồ.
- SRS không quy định trục tung/thứ nguyên biểu đồ, cũng không yêu cầu tách trục phụ cho metric khác đơn vị.

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:1077` (Mapping UC141 — "Grouped bar", bộ lọc "Loại DN"; không định nghĩa series)
- `srs-v3.5/srs-fr-11-bao-cao.md:831-839` (FR-IX-18 §Output — cột bảng, không mô tả biểu đồ)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, `cbnv_tw` (Toàn quốc), URL `.../bao-cao?loai=chi-phi-theo-loai-dn&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- **Ý (1) — thành phần biểu đồ: TÁI HIỆN ĐÚNG.** Legend chart đủ 6 series: `Chênh lệch · Mức hỗ trợ (%) · Số hồ sơ · Trần / hồ sơ · Trần chi phí · Tổng chi phí`, nhóm theo loại hình DN. Đối tác kỳ vọng "nhóm theo loại hình và mức hỗ trợ" (1 chiều mức hỗ trợ) — app không làm vậy.
- **Ý (2) — "trục tung toàn bộ 0": KHÔNG tái hiện đúng theo nghĩa đen.** Nhóm "Siêu nhỏ" trên chart env test: bar **Tổng chi phí ≈8M (dương)**, **Trần/hồ sơ ≈30M (dương cao)**, **Trần chi phí ≈30M (dương cao)**, **Chênh lệch ≈-22M (âm)** — có giá trị rõ. Chỉ **Số hồ sơ (=1)** và **Mức hỗ trợ % (=100)** hiện ~0/vô hình vì được vẽ chung trục tung scale tiền (hàng chục triệu) → 1 và 100 quá nhỏ. Ảnh chính đối tác cũng có tooltip giá trị khác 0 (Chênh lệch -211M, Số hồ sơ 11...) → tự phủ định "toàn bộ 0".
- Network: `GET /api/v1/bao-cao/chi-phi-theo-loai-dn` (200) trả đủ 6 metric số per loại hình (`soHoSo`, `mucHoTroPhanTram`, `tongChiPhi`, `tranChiPhiMoiHoSo`, `tranChiPhi`, `chenhLech`) → chart plot 6 series là chủ đích, data không lỗi.
- Evidence: `../../reverify-audit/CPCTHTTLHDN_04/web-chart.png`

**Kết luận QA**

- Ý (1): actual đối tác đúng thực tế (chart plot 6 metric), nhưng đây là **bất đồng đặc tả** — SRS "Grouped bar" không định nghĩa series; không có dòng SRS để khẳng định app sai hay đối tác đúng. → không đủ căn cứ Open/Reject.
- Ý (2): claim "toàn bộ 0" **không đúng theo nghĩa đen** — bar tiền có giá trị; chỉ count/% bị nén thành 0 do trộn scale. Đây là **vấn đề legibility/thiết kế biểu đồ** (2 series không đọc được), SRS không quy định → cần design/BA quyết, không phải data bug.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt cho biểu đồ "Chi phí theo loại hình DN" (FR-IX-18, Grouped bar):

1. **Thành phần series biểu đồ:** giữ nguyên plot 6 metric số (như app), hay đổi sang "nhóm theo loại hình × mức hỗ trợ" (như đối tác kỳ vọng)? SRS Mapping chỉ ghi "Grouped bar" nên cần BA/design chốt.
2. **Xử lý metric khác đơn vị:** Số hồ sơ (đếm) và Mức hỗ trợ (%) đang dùng chung trục tung với tiền → hiện thành ~0, không đọc được. Có nên tách **trục phụ (secondary axis)** hoặc bỏ 2 metric này khỏi biểu đồ (chỉ để trong bảng) không?

- Nếu BA chấp nhận biểu đồ hiện tại → cập nhật expected `CPCTHTTLHDN_04`; làm rõ Mapping/§Output về series. Verdict: `Không phải bug theo SRS`.
- Nếu BA muốn theo kỳ vọng đối tác (nhóm theo mức hỗ trợ + tách trục cho count/%) → gửi Dev FE. Verdict: `Vẫn lỗi — owner: Dev FE`.
- Lưu ý riêng: claim "trục tung toàn bộ 0" của đối tác **không chính xác** — chỉ 2 series count/% hiện ~0 do scale, phần tiền vẫn đúng.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt.

---

### CPCTHTTTG_03 — Đối tác báo biểu đồ "Chi phí theo thời gian" có "trục tung toàn bộ 0"; thực tế điểm Tổng chi phí khác 0, chỉ Số hồ sơ hiện ~0 do trộn scale

**Bối cảnh testcase**

- Dòng Excel: 259, mã TC `CPCTHTTTG_03`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ TW xem báo cáo "BC Chi phí theo thời gian" (UC142 / FR-IX-19), kiểm tra hiển thị **biểu đồ + bảng tổng hợp**.
- Expected trong file UAT: "Biểu đồ đường thể hiện xu hướng chi phí" + "Bảng tổng hợp: Kỳ thời gian, Tổng chi phí, Số hồ sơ".
- Actual đối tác ghi: "Số liệu ở trục tung của biểu đồ hiển thị toàn bộ giá trị 0".

**Đối chiếu SRS v3.5**

- Mapping UC142 (dòng 1078): `BC Chi phí theo thời gian | Biểu đồ: Line chart trend`. SRS chỉ ghi loại biểu đồ, không định nghĩa trục/series.
- FR-IX-19 §Output (dòng 869): `trend_data[] = {ky_label, tong_chi_phi, so_ho_so}` (điều kiện "Luôn"), `chart_type = LINE`. → SRS §Output CÓ đưa cả `so_ho_so` + `tong_chi_phi` vào trend_data nên biểu đồ vẽ 2 series là khớp §Output. SRS **không quy định tách trục** cho metric đếm.
- AC (dòng 874): "12 tháng → line chart 12 điểm trend chi phí". Đối tác chọn Kỳ = Năm → chỉ 1 kỳ (2026) → 1 điểm là đúng filter (không phải lỗi).

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:1078` (Mapping UC142 — "Line chart trend")
- `srs-v3.5/srs-fr-11-bao-cao.md:869` (FR-IX-19 §Output — trend_data gồm cả so_ho_so + tong_chi_phi; không nêu tách trục)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, `cbnv_tw` (Toàn quốc), URL `.../bao-cao?loai=chi-phi-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- **"Trục tung toàn bộ 0": KHÔNG tái hiện đúng theo nghĩa đen.** Chart env test: trục tung auto-scale `0 / 2M / 4M / 6M / 8M`; điểm **Tổng chi phí (xanh lá) nằm ở đỉnh ≈8.000.000** (khác 0 rõ), điểm **Số hồ sơ (xanh dương, =1) ở đáy ≈0** vì bị vẽ chung trục tung scale tiền. Ảnh chính đối tác cũng cho thấy điểm Tổng chi phí ở đỉnh (~226M) → tự phủ định "toàn bộ 0".
- Network: `GET /api/v1/bao-cao/chi-phi-theo-thoi-gian` (200) trả `tongChiPhiToanKy:8000000, tongHoSoToanKy:1, data:[{kyLabel:"2026", soHoSo:1, tongChiPhi:8000000}], chartType:"LINE"` → BE trả số khác 0, data không lỗi.
- Evidence: `../../reverify-audit/CPCTHTTTG_03/web-chart.png`

**Kết luận QA**

- Claim "trục tung toàn bộ 0" **sai theo nghĩa đen** — series Tổng chi phí có giá trị, hiển thị ở đỉnh trục. Không phải data bug.
- Đây là **cùng bản chất với `CPCTHTTLHDN_04`**: biểu đồ trộn metric đếm (Số hồ sơ) và metric tiền (Tổng chi phí) trên cùng 1 trục tung → series đếm bị nén thành ~0, không đọc được. SRS không quy định trục phụ → vấn đề legibility/thiết kế, cần BA/design quyết.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt cho biểu đồ "Chi phí theo thời gian" (FR-IX-19, Line chart):

1. Series "Số hồ sơ" (đếm) dùng chung trục tung với "Tổng chi phí" (tiền) → hiện thành ~0, không đọc được. Có nên **tách trục phụ (secondary axis)** cho Số hồ sơ, hay chỉ vẽ trend chi phí (bỏ Số hồ sơ khỏi biểu đồ, giữ ở bảng) như expected đối tác ("biểu đồ đường thể hiện xu hướng chi phí")?

- Nếu BA chấp nhận biểu đồ hiện tại → cập nhật expected `CPCTHTTTG_03`. Verdict: `Không phải bug theo SRS`.
- Nếu BA muốn tách trục / bỏ Số hồ sơ khỏi biểu đồ → gửi Dev FE. Verdict: `Vẫn lỗi — owner: Dev FE`.
- Lưu ý riêng: claim "trục tung toàn bộ 0" của đối tác **không chính xác** — chỉ Số hồ sơ hiện ~0 do scale; Tổng chi phí đúng.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt.

> **Ghi chú cụm:** 3 case `CPCTHTTLHDN_04` + `CPCTHTTTG_03` (+ liên quan `CPCTHTTLHDN_03`/`CPCTHTTDVQL_03`) đều xoay quanh cùng 1 gốc: biểu đồ báo cáo Chi phí trộn nhiều metric khác đơn vị (tiền / đếm / %) trên 1 trục tung → metric đếm & % hiện ~0. Nên BA chốt CHUNG 1 nguyên tắc trục phụ cho toàn cụm báo cáo Chi phí.

---

## Nhóm 4 — Họ Chương trình HTPLDN

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** vì SRS chưa quy định rõ, cần BA quyết. Batch 4 verify 4 case (CTTDVQL_02, CTTDVQL_03, CTTLV_03, CTTLV_04); trong đó **CTTDVQL_02 + CTTLV_03** cần BA xác nhận (2 case này cùng 1 vấn đề: báo cáo có thẻ chỉ số tổng hợp mà §Output đặc thù không liệt kê). CTTDVQL_03 (Open) đã log ở `../../bug-reports/bctk/Pass-bug-report-bctk-batch4.md`; CTTLV_04 **đổi Reject → `BA confirm` (re-verify 22/07/2026)** — chi tiết ở `ba-confirm-CTTLV_04.md` + `../../reverify-audit/CTTLV_04/`.

> **Môi trường verify:** https://18.143.165.120.nip.io · Chrome DevTools MCP · tài khoản `cbnv_tw_01` (CB Nghiệp vụ - Trung ương) · kỳ Năm 2026 · đơn vị Toàn quốc · đã seed chương trình HTPLDN đã duyệt (được báo cáo đếm).

---

### CTTDVQL_02 (và CTTLV_03) — Báo cáo hiển thị thẻ chỉ số tổng hợp mà §Output đặc thù không liệt kê

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

---

## Nhóm 5 — BUTTON: nút "In báo cáo" không hiển thị

> **File này để làm gì:** gom 6 testcase batch 5 mà QA verify xong nhưng cần BA phản hồi đối tác. Cả 6 cùng 1 gốc: đối tác kỳ vọng có nút "In báo cáo" trên màn Báo cáo thống kê, nhưng SRS SCR-IX-01 KHÔNG quy định nút này (chỉ spec 4 nút). App hiện đúng SRS → bất đồng về **đặc tả**, không phải bug → BA chốt có bổ sung chức năng In không.

> **Quy tắc citation:** SRS v3.5 = `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`. Mọi khẳng định dẫn số dòng thực đã mở file kiểm.

> **Tài khoản verify:** `cbnv_tw_02` (CB Nghiệp vụ - Trung ương #02, CB_NV_TW, phạm vi Toàn quốc). Kỳ báo cáo = Năm 2026, đơn vị = Toàn quốc; cả 6 báo cáo đều có dữ liệu thực khi Xem báo cáo.

---

### SLHDVM_08 · VVDTN_08 · VVDHT_08 · VVDHTHT_08 · VVTTG_07 · CLDTBDDDR_08 — Đối tác kỳ vọng nút "In báo cáo" mà SRS không quy định (cụm 6 case cùng gốc)

**Bối cảnh testcase**

- 6 dòng Excel / mã TC:
  - Dòng 193 · `SLHDVM_08` — BC Số lượng hỏi đáp/vướng mắc pháp luật (FR-IX-01 / UC124).
  - Dòng 198 · `VVDTN_08` — BC Vụ việc đã tiếp nhận (FR-IX-02 / UC125).
  - Dòng 205 · `VVDHT_08` — BC Vụ việc đang hỗ trợ (FR-IX-03 / UC126).
  - Dòng 211 · `VVDHTHT_08` — BC Vụ việc đã hoàn thành (FR-IX-04 / UC127).
  - Dòng 218 · `VVTTG_07` — BC Vụ việc theo thời gian (FR-IX-05 / UC128).
  - Dòng 224 · `CLDTBDDDR_08` — BC Lớp đào tạo đang diễn ra (FR-IX-06 / UC129).
- Nội dung kiểm tra: Cán bộ nghiệp vụ mở màn Báo cáo thống kê (SCR-IX-01), tìm chức năng "In báo cáo".
- Expected trong file UAT (đối tác): có nút "In báo cáo" → mở xem trước + hộp thoại in của trình duyệt.
- Actual đối tác ghi: "Màn hình không hiển thị nút chức năng" (không tìm thấy nút In báo cáo).

**Đối chiếu SRS v3.5**

- SCR-IX-01 §Thành phần màn hình (bảng toolbar/action-bar) chỉ quy định **4 nút** trên màn Báo cáo thống kê:
  - Nút **Làm mới** (toolbar).
  - Nút **Xem báo cáo** (action-bar, primary).
  - Nút **Xuất Excel (.xlsx)** (action-bar, hiện sau khi Xem báo cáo).
  - Nút **Xuất PDF (.pdf)** (action-bar, hiện sau khi Xem báo cáo).
- SRS **KHÔNG có** component "In báo cáo" / nút In ở bất kỳ dòng nào của SCR-IX-01. Vậy app hiện (không có nút In) đúng SRS hiện tại.
- **Điểm quan trọng cho BA:** trên UI, khi bấm **Xuất PDF**, hệ thống mở hộp thoại tiêu đề **"Tùy chọn in báo cáo PDF"** — cho chọn Khổ giấy (A4 / A3 / Letter) + Hướng giấy (Dọc / Ngang) → tạo file PDF in được. Tức bản chất "in báo cáo" mà đối tác cần **đã được đáp ứng qua nút Xuất PDF** (tạo PDF theo tùy chọn in, người dùng in từ file PDF).

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:1042` (toolbar — Tiêu đề trang + Nút Làm mới)
- `srs-v3.5/srs-fr-11-bao-cao.md:1047-1049` (action-bar — Xem báo cáo / Xuất Excel / Xuất PDF; KHÔNG có nút In)
- `srs-v3.5/srs-fr-11-bao-cao.md:1037-1054` (toàn bảng §Thành phần màn hình SCR-IX-01 — không có component In báo cáo)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_02` (CB Nghiệp vụ - Trung ương, Toàn quốc), kỳ Năm 2026.
- Với mỗi loại báo cáo: chọn loại BC → Kỳ Năm → Xem báo cáo (ra dữ liệu) → liệt kê toàn bộ nút toolbar bằng `evaluate_script` + chụp full-res. **Cả 6 báo cáo đều chỉ có 4 nút: Làm mới, Xem báo cáo, Xuất Excel, Xuất PDF** (+ nút toggle "Ẩn biểu đồ"). Query text toàn trang không có chuỗi "in báo cáo" trên toolbar.

| Mã TC | Báo cáo | Dữ liệu khi Xem BC | Toolbar quan sát được | Có nút "In báo cáo"? | Evidence |
|---|---|---|---|:-:|---|
| `SLHDVM_08` | Số lượng hỏi đáp | Tổng hỏi đáp 11 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/SLHDVM_08/SLHDVM_08-toolbar.png` |
| `VVDTN_08` | VV đã tiếp nhận | Tổng vụ việc 14 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/VVDTN_08/VVDTN_08-toolbar.png` |
| `VVDHT_08` | VV đang hỗ trợ | Tổng vụ việc 7 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/VVDHT_08/VVDHT_08-toolbar.png` |
| `VVDHTHT_08` | VV đã hoàn thành | Tổng vụ việc 5 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/VVDHTHT_08/VVDHTHT_08-toolbar.png` |
| `VVTTG_07` | VV theo thời gian | Tổng vụ việc toàn kỳ 6 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/VVTTG_07/VVTTG_07-toolbar.png` |
| `CLDTBDDDR_08` | Lớp ĐT đang diễn ra | Tổng số 1 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/CLDTBDDDR_08/CLDTBDDDR_08-toolbar.png` |

- **Kiểm tra bổ sung nút Xuất PDF (CLDTBDDDR_08):** bấm Xuất PDF → mở hộp thoại **"Tùy chọn in báo cáo PDF"** (Khổ giấy A4/A3/Letter, Hướng Dọc/Ngang) → bấm "Xuất file" → `POST /api/v1/bao-cao/export` trả **200**, toast "Đang tạo file...", tạo PDF thành công (không lỗi trên env test).
  - Evidence: `../../reverify-audit/CLDTBDDDR_08/export-pdf-toast.png` (hộp thoại "Tùy chọn in báo cáo PDF") · `../../reverify-audit/CLDTBDDDR_08/export-pdf-result.png` (sau khi xuất, 200).

**Kết luận QA**

- Cả 6 case: actual đối tác **đúng thực tế** (màn Báo cáo thống kê không có nút "In báo cáo" riêng), nhưng đây là bất đồng về **đặc tả** — SRS SCR-IX-01 không quy định nút In. App hiện đúng SRS → **không phải bug (không Open)**, cũng **không Reject** (đối tác quan sát đúng, chỉ khác kỳ vọng spec).
- Chức năng in báo cáo mà đối tác cần thực chất **đã có phần đáp ứng** qua nút **Xuất PDF** — hộp thoại này được đặt tên "Tùy chọn in báo cáo PDF", tạo PDF theo khổ giấy/hướng giấy để in.
- Khác biệt còn lại so với kỳ vọng đối tác: đối tác muốn nút "In báo cáo" mở thẳng hộp thoại in của trình duyệt (in trực tiếp), còn app đang đi qua bước tạo file PDF rồi người dùng in từ file.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt cho cụm 6 case (`SLHDVM_08`, `VVDTN_08`, `VVDHT_08`, `VVDHTHT_08`, `VVTTG_07`, `CLDTBDDDR_08`):

1. Màn Báo cáo thống kê (SCR-IX-01) hiện **không có nút "In báo cáo" riêng** — đúng theo SRS v3.5 (SRS chỉ quy định Làm mới / Xem báo cáo / Xuất Excel / Xuất PDF). Có **bổ sung** một nút "In báo cáo" (mở xem trước + hộp thoại in trình duyệt) như kỳ vọng đối tác không, hay coi chức năng **Xuất PDF** (đã có hộp thoại "Tùy chọn in báo cáo PDF") là đủ đáp ứng nhu cầu in?
   - Nếu BA coi Xuất PDF là đủ → cập nhật expected 6 case (bỏ yêu cầu nút In riêng); verdict `Không phải bug theo SRS`. Hướng dẫn đối tác: bấm **Xuất PDF** → chọn khổ giấy/hướng → in từ file PDF.
   - Nếu BA muốn bổ sung nút "In báo cáo" in trực tiếp → gửi Dev FE bổ sung + cập nhật SRS SCR-IX-01; verdict `Vẫn lỗi — owner: Dev FE`.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận` (đã ghi Google Sheet cả 6 dòng: `BA confirm`), chưa gửi Dev tới khi BA chốt.

---

> **Ghi chú ngoài phạm vi (postmortem #3):** Ảnh bằng chứng đối tác (env `htpldn-uat.ospgroup.vn`) ở 4/6 case có toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." khi thao tác xuất file. Verify lại trên env test (`18.143.165.120.nip.io`): Xuất PDF `POST /api/v1/bao-cao/export` trả **200**, tạo file thành công — lỗi export **KHÔNG tái hiện**. Do 2 env cho kết quả khác nhau (candidate không tái hiện trên env test) nên **chưa log thành bug**; nếu lỗi export còn xảy ra trên env đối tác thì có thể là sự cố env/tạm thời của môi trường đó, đề nghị đối tác thử lại + báo lại nếu vẫn lỗi.

---

## Nhóm 6 — BUTTON: nút "Xóa bộ lọc" không hiển thị

> **File này để làm gì:** gom 6 testcase batch 6 (module Báo cáo Thống kê, cụm "nút Xóa bộ lọc không hiển thị") mà QA đối chiếu SRS xong nhưng khác biệt nằm ở **đặc tả** (kỳ vọng đối tác ≠ SRS) → cần BA chốt. Không phải bug app sai clause SRS nên KHÔNG log vào bug-report.
>
> **Vai trò verify:** `cbnv_tw_03` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc). Môi trường `https://18.143.165.120.nip.io/bao-cao`. Kỳ = Năm 2026, Đơn vị = Toàn quốc.
>
> **SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (= `input/srs-update-2026-5-5/srs-fr-11-bao-cao.md`, cùng nội dung dòng 1042).

---

### SLHDVM_09, VVDTN_09, VVDHT_09, VVDHTHT_09, VVTTG_08, CLDTBDDDR_09 — Đối tác kỳ vọng nút "Xóa bộ lọc", SRS spec "Nút Làm mới" (cùng 1 màn dùng chung SCR-IX-01)

**Bối cảnh testcase**

- 6 dòng Excel cùng bản chất — chỉ khác dropdown loại báo cáo:

  | Row | Mã TC | Loại báo cáo (FR-IX) | Evidence đối tác | Evidence QA (real-data) |
  |---|---|---|---|---|
  | 194 | `SLHDVM_09` | BC Số lượng hỏi đáp/vướng mắc PL (FR-IX-01) | `../../partner-evidence/SLHDVM_09.jpg` | `../../reverify-audit/SLHDVM_09/SLHDVM_09-before-lammoi.png` + `-after-lammoi.png` |
  | 199 | `VVDTN_09` | BC Vụ việc đã tiếp nhận (FR-IX-02) | `../../partner-evidence/VVDTN_09.jpg` | `../../reverify-audit/VVDTN_09/VVDTN_09-toolbar.png` |
  | 206 | `VVDHT_09` | BC Vụ việc đang hỗ trợ (FR-IX-03) | `../../partner-evidence/VVDHT_09.jpg` | `../../reverify-audit/VVDHT_09/VVDHT_09-toolbar.png` |
  | 212 | `VVDHTHT_09` | BC Vụ việc đã hoàn thành (FR-IX-04) | `../../partner-evidence/VVDHTHT_09.jpg` | `../../reverify-audit/VVDHTHT_09/VVDHTHT_09-toolbar.png` |
  | 219 | `VVTTG_08` | BC Vụ việc theo thời gian (FR-IX-05) | `../../partner-evidence/VVTTG_08.jpg` | `../../reverify-audit/VVTTG_08/VVTTG_08-before-lammoi.png` + `-after-lammoi.png` |
  | 225 | `CLDTBDDDR_09` | BC Lớp đào tạo đang diễn ra (FR-IX-06) | `../../partner-evidence/CLDTBDDDR_09.jpg` | `../../reverify-audit/CLDTBDDDR_09/CLDTBDDDR_09-toolbar.png` |

- Nội dung kiểm tra (chung): Cán bộ nghiệp vụ mở Báo cáo thống kê → chọn loại BC → nhập tiêu chí lọc → Xem báo cáo → **bấm "Xóa bộ lọc"** để đặt bộ lọc về mặc định.
- Expected trong file UAT (đối tác, `KQ mong đợi _09/_08`): "Hệ thống xóa toàn bộ giá trị đã nhập trong các trường lọc và đặt lại về giá trị mặc định (Kỳ = Tháng, Từ ngày = ngày đầu tháng hiện tại, Đến ngày = ngày hiện tại, Đơn vị = đơn vị đăng nhập, các trường khác = 'Tất cả'); khu vực kết quả không tự tải lại cho đến khi NSD bấm 'Xem báo cáo'."
- Actual đối tác ghi (cả 6): **"Màn hình không hiển thị nút chức năng"** (đối tác tìm nút tên "Xóa bộ lọc" nhưng không thấy).

**Đối chiếu SRS v3.5**

- SCR-IX-01 (màn Báo cáo thống kê dùng chung cho cả 23 loại BC) — bảng "Thành phần màn hình" chỉ spec **4 nút** ở toolbar/action-bar: **"Nút Làm mới"** (item 2), "Xem báo cáo" (item 7), "Xuất Excel (.xlsx)" (item 8), "Xuất PDF (.pdf)" (item 9).
- SRS **KHÔNG** có nút tên **"Xóa bộ lọc"** và **KHÔNG** có nút "In báo cáo" trong SCR-IX-01 — chức năng "đặt lại bộ lọc" mà đối tác mong muốn được SRS đặt tên là **"Làm mới"** (item 2).
- SRS **không quy định** giá trị mặc định cụ thể mà thao tác reset phải khôi phục (Kỳ=Tháng, ngày đầu tháng...) — mốc mặc định đó chỉ có trong KQMĐ của đối tác, không có trong SCR-IX-01 §Thành phần màn hình.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1042` — `| 2 | toolbar | Tiêu đề trang | label | "Báo cáo Thống kê" + Nút Làm mới | — | Luôn hiển thị |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1047-1049` — action-bar chỉ có "Xem báo cáo" / "Xuất Excel" / "Xuất PDF" (không có "Xóa bộ lọc").

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw_03` / CB_NV_TW (Toàn quốc). URL `https://18.143.165.120.nip.io/bao-cao`.
- Liệt kê toolbar bằng `evaluate_script` trên cả 6 loại BC → mỗi màn đúng **4 nút**: `["Làm mới","Xem báo cáo","Xuất Excel","Xuất PDF"]`. `hasXoaBoLoc=false` — **không có nút tên "Xóa bộ lọc"** (khớp evidence đối tác).
- **Test hành vi nút "Làm mới"** (test kỹ 2 đại diện: SLHDVM_09 + VVTTG_08):
  - Nhập bộ lọc khác mặc định (Kỳ=Năm, Lĩnh vực=Thuế) → Xem báo cáo (ra kết quả: SLHDVM Tổng hỏi đáp=11; VVTTG Tổng vụ việc toàn kỳ=6) → bấm **"Làm mới"**.
  - Kết quả: **xóa toàn bộ giá trị đã nhập** (Loại BC, Kỳ, Lĩnh vực, Thời gian về trống), Đơn vị về "Toàn quốc" (= đơn vị đăng nhập của TW); **khu vực kết quả bị xóa, KHÔNG tự tải lại** (nút "Xem báo cáo"/"Xuất" disabled trở lại). URL trả về `/bao-cao` (bỏ hết query params).
- Khác biệt duy nhất vs KQMĐ đối tác: sau reset, bộ lọc về **trống hoàn toàn** (Kỳ chưa chọn) — KHÔNG pre-fill Kỳ=Tháng + ngày đầu tháng như KQMĐ mô tả. Đây cũng là trạng thái mặc định khởi tạo của màn (khi mới mở, Loại BC + Kỳ đều trống).

**Kết luận QA**

- 6 case KHÔNG phải bug theo SRS v3.5: SRS SCR-IX-01 (dòng 1042) spec đúng **"Nút Làm mới"**, app hiển thị đúng nút này và nút này **thực hiện đúng chức năng reset bộ lọc** (xóa filter + xóa kết quả, không tự tải lại) — tức chức năng đối tác cần **CÓ tồn tại**, chỉ khác **TÊN** ("Làm mới" thay vì "Xóa bộ lọc") và khác **giá trị mặc định sau reset** (về trống thay vì Kỳ=Tháng).
- Đối tác quan sát ĐÚNG thực tế (không có nút tên "Xóa bộ lọc") nhưng kỳ vọng tên/hành vi khác SRS → bất đồng về **ĐẶC TẢ**, không phải app sai → `BA confirm` (QA không tự Reject).
- Ghi nhận thêm (không phải căn cứ verdict): màn danh sách khác trong app (vd Đào tạo → Chương trình đào tạo → Danh sách) dùng nút tên **"Xóa bộ lọc"**, trong khi màn Báo cáo thống kê dùng **"Làm mới"** → thiếu nhất quán đặt tên giữa các màn, có thể là lý do đối tác kỳ vọng "Xóa bộ lọc".

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt hướng xử lý cụm "nút Xóa bộ lọc" của màn Báo cáo thống kê (áp dụng chung cho cả 6 case):

- **Hướng 1 (giữ theo SRS):** màn dùng nút **"Làm mới"** (SCR-IX-01 item 2) để đặt lại bộ lọc → web hiện tại đúng SRS; cập nhật lại expected của 6 TC (đổi "Xóa bộ lọc" → "Làm mới", và mô tả reset về trạng thái khởi tạo trống).
- **Hướng 2 (chỉnh theo kỳ vọng đối tác):** (a) đổi tên nút "Làm mới" → "Xóa bộ lọc" cho nhất quán với các màn danh sách khác, và/hoặc (b) khi reset thì pre-fill giá trị mặc định (Kỳ=Tháng, Từ ngày=đầu tháng, Đến ngày=hôm nay) thay vì để trống → cần cập nhật SCR-IX-01 + gửi Dev FE bổ sung.
- Verdict QA đề xuất: **`Cần BA xác nhận`** (đặc tả kỳ vọng đối tác vs SRS lệch nhau về tên nút + giá trị mặc định sau reset). Chưa gửi Dev cho tới khi BA chốt source truth.
