# BA confirmation needed — BCTK Batch 2 (DISPLAY họ Đào tạo / CG-TVV / Đánh giá) — 2026-07-21

> **File này để làm gì:** gom các testcase batch 2 (module Báo cáo Thống kê, cụm hiển thị chỉ số/biểu đồ/bảng — họ Đào tạo / CG-TVV / Đánh giá) mà QA đối chiếu SRS xong nhưng khác biệt nằm ở **đặc tả** (kỳ vọng đối tác ≠ SRS, hoặc SRS silent về chi tiết chiều biểu đồ) → cần BA chốt. Bug có SRS reference rõ (app sai clause SRS) đã log vào `../../bug-reports/bctk/Pass-bug-report-bctk-batch2.md`.
>
> **Vai trò verify:** `cbnv_tw` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc). Môi trường `https://18.143.165.120.nip.io`. Kỳ = Năm 2026, Đơn vị = Toàn quốc.
>
> **SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`.

---

## CLDTBDDDR_04 — Biểu đồ cột hiển thị theo Đơn vị (đối tác kỳ vọng theo Hình thức) + không có biểu đồ đường xu hướng

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

## LDTBDDDR_04 — Biểu đồ cột (BC Lớp đào tạo đã diễn ra) hiển thị theo Đơn vị (đối tác kỳ vọng theo Hình thức)

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

## CGTVPL_04 — Biểu đồ tròn (BC Số lượng CG/TVV) theo Đơn vị (đối tác kỳ vọng theo Loại TVV/CG); biểu đồ cột "không hiển thị" KHÔNG tái hiện

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

## CLDTBDPL_04 — Biểu đồ (BC Chất lượng đào tạo) nhãn trục theo Đơn vị (đối tác kỳ vọng theo Khóa học); "thiếu đường điểm TB" KHÔNG tái hiện

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
