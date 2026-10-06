# Bảng đối chiếu điều kiện — CTTDVQL_05 (row 269) — Xuất PDF BC Chương trình theo đơn vị

**Case:** BC Chương trình theo đơn vị (FR-IX-21 / UC144) — đối tác báo bấm **Xuất PDF** → toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Open — lỗi ERR-RPT-04 KHÔNG tái hiện (export 200, tạo file OK), NHƯNG kiểm nội dung file PDF phát hiện **thiếu 3/4 header bắt buộc** (Kỳ báo cáo / Đơn vị / Ngày tạo) → vi phạm SRS dòng 1088. Bug khác lỗi đối tác báo → BUG-EXPORT-PDF-HEADER.
**Verify:** 21/07/2026, Chrome DevTools MCP + PyMuPDF, tài khoản `cbnv_tw_03` (CB Nghiệp vụ TW), kỳ Năm 2026, đơn vị Toàn quốc.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CTTDVQL_05.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — env `htpldn-uat.ospgroup.vn` | `cbnv_tw_03` (CB Nghiệp vụ TW — vai trò chuẩn verdict, quyền xem + xuất BC Toàn quốc) | Không |
| Loại báo cáo | BC Chương trình theo đơn vị (`loai=ct-theo-don-vi`) | BC Chương trình theo đơn vị (`loaiBaoCao=BC_CT_THEO_DON_VI`) | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng CT = 5 | Có data — Tổng CT = 4, ngân sách 300.000.000 (đã Xem báo cáo ra kết quả) | Không |
| Thao tác | Xuất PDF (A4, Dọc) | Xuất PDF (A4/portrait, qua dialog "Tùy chọn in báo cáo PDF") | Không |

**0 GAP.** Đã tái hiện đúng điều kiện đối tác.

**Kết quả:** `POST /api/v1/bao-cao/export` (formatXuat=PDF, khoGiay=A4, huongGiay=portrait) trả **HTTP 200** + `content-type: application/pdf` + `content-disposition: attachment; filename="bao-cao-ct-theo-don-vi-2026-07-21.pdf"` (reqid=130). Toast UI: "Đang tạo file..." → tạo file thành công. KHÔNG có ERR-RPT-04.

**Kiểm nội dung file PDF (PyMuPDF):** trang A4 dọc (595.28×841.89pt ✓), font Tinos-Bold/Regular (Times New Roman-tương thích ✓). NHƯNG nội dung chỉ có: tiêu đề "BC CHƯƠNG TRÌNH THEO ĐƠN VỊ" → nhảy thẳng vào bảng (Đơn vị / Cấp đơn vị / Số chương trình / Tổng ngân sách / Cục Bổ trợ tư pháp / TW / 4 / 300.000.000). **THIẾU 3 dòng header: "Kỳ báo cáo: Năm...", "Đơn vị: Toàn quốc", "Ngày tạo: 21/07/2026".** Bản Excel cùng báo cáo (đối chứng) CÓ đủ 4 trường → BE có sẵn data header, chỉ luồng dựng PDF bỏ khối header.

**Kết luận:** ERR-RPT-04 không tái hiện, nhưng file PDF xuất ra sai chuẩn TT17 (thiếu header) → **Open** (BUG-EXPORT-PDF-HEADER, lỗi template PDF dùng chung toàn module Báo cáo thống kê).

**Evidence:** `bug-reports/bctk/image/BUG-EXPORT-PDF-HEADER-CTTDVQL-pdf-no-header.png` + file dump `reverify-audit/_export-check-bctk12/bao-cao-ct-theo-don-vi.pdf` (+ .xlsx đối chứng).
