# Bảng đối chiếu điều kiện — CTTTG_05 (row 276) — Xuất PDF BC Chương trình theo thời gian

**Case:** BC Chương trình theo thời gian (FR-IX-23 / SCR-IX-01 item 9) — đối tác báo bấm **Xuất PDF** → toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Open — lỗi ERR-RPT-04 KHÔNG tái hiện (export 200, tạo file OK), NHƯNG kiểm nội dung file PDF phát hiện **thiếu 3/4 header bắt buộc** (Kỳ báo cáo / Đơn vị / Ngày tạo) → vi phạm SRS dòng 1088. Bug khác lỗi đối tác báo → BUG-EXPORT-PDF-HEADER.
**Verify:** 21/07/2026, Chrome DevTools MCP + PyMuPDF, tài khoản `cbnv_tw_03` (CB Nghiệp vụ TW), kỳ Năm 2026, đơn vị Toàn quốc.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CTTTG_05.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — env `htpldn-uat.ospgroup.vn` | `cbnv_tw_03` (CB Nghiệp vụ TW — vai trò chuẩn verdict, quyền xem + xuất BC Toàn quốc) | Không |
| Loại báo cáo | BC Chương trình theo thời gian (`loai=ct-theo-thoi-gian`) | BC Chương trình theo thời gian (`loaiBaoCao=BC_CT_THEO_THOI_GIAN`) | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng CT toàn kỳ = 1 | Có data — Tổng CT toàn kỳ = 3, ngân sách 200.000.000; đã Xem báo cáo ra kết quả | Không* |
| Thao tác | Xuất PDF (A4, Dọc) | Xuất PDF (`formatXuat=PDF`, khoGiay=A4, huongGiay=portrait) | Không |

\* Số CT lệch (1 vs 3) do seed 2 env khác nhau, nhưng CẢ HAI đều có data → nút Xuất bật → không đổi hành vi export. **0 GAP về điều kiện quyết định.**

**Kết quả:** `POST /api/v1/bao-cao/export` (formatXuat=PDF, khoGiay=A4, huongGiay=portrait) trả **HTTP 200** + `content-type: application/pdf` (size 15.503 bytes). KHÔNG có ERR-RPT-04.

**Kiểm nội dung file PDF (PyMuPDF):** trang A4 dọc (595.28×841.89pt ✓). Text theo thứ tự: `BC CHƯƠNG TRÌNH THEO THỜI GIAN` → nhảy thẳng vào bảng (`Kỳ` / `Từ ngày` / `Đến ngày` / `Số chương trình` / `Số DN` / `Tổng ngân sách (₫)` / `2026` `01/01/2026` `31/12/2026` `3` `0` `200.000.000`). Lưu ý "Kỳ" ở đây là **cột bảng**, KHÔNG phải header field "Kỳ báo cáo". **THIẾU 3 dòng header: "Kỳ báo cáo: Năm...", "Đơn vị: Toàn quốc", "Ngày tạo: 21/07/2026".** Bản Excel cùng báo cáo (CTTTG_04 đối chứng) CÓ đủ 4 trường → BE có sẵn data header, chỉ luồng dựng PDF bỏ khối header.

**Kết luận:** ERR-RPT-04 không tái hiện, nhưng file PDF xuất ra sai chuẩn TT17 (thiếu header) → **Open** (BUG-EXPORT-PDF-HEADER, lỗi template PDF dùng chung toàn module Báo cáo thống kê — đồng nhất batch 7/8 + CTTDVQL_05 + CTTLV_06).

**Evidence:** `bug-reports/bctk/image/BUG-EXPORT-PDF-HEADER-CTTTG-pdf-no-header.png` (render PDF) + file dump `reverify-audit/_export-check-bctk12/bao-cao-ct-theo-thoi-gian.pdf` (+ .xlsx đối chứng).
