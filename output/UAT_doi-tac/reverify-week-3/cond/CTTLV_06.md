# Bảng đối chiếu điều kiện — CTTLV_06 (row 274) — Xuất PDF BC Chương trình theo lĩnh vực

**Case:** BC Chương trình theo lĩnh vực (FR-IX-22 / SCR-IX-01 item 9) — đối tác báo bấm **Xuất PDF** → toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Open — lỗi ERR-RPT-04 KHÔNG tái hiện (export 200, tạo file OK), NHƯNG kiểm nội dung file PDF phát hiện **thiếu 3/4 header bắt buộc** (Kỳ báo cáo / Đơn vị / Ngày tạo) → vi phạm SRS dòng 1088. Bug khác lỗi đối tác báo → BUG-EXPORT-PDF-HEADER.
**Verify:** 21/07/2026, Chrome DevTools MCP + PyMuPDF, tài khoản `cbnv_tw_03` (CB Nghiệp vụ TW), kỳ Năm 2026, đơn vị Toàn quốc.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CTTLV_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — env `htpldn-uat.ospgroup.vn` | `cbnv_tw_03` (CB Nghiệp vụ TW — vai trò chuẩn verdict, quyền xem + xuất BC Toàn quốc) | Không |
| Loại báo cáo | BC Chương trình theo lĩnh vực (`loai=ct-theo-linh-vuc`) | BC Chương trình theo lĩnh vực (`loaiBaoCao=BC_CT_THEO_LINH_VUC`) | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Lĩnh vực (filter đặc thù) | Trống ("Chọn Lĩnh vực" — tất cả) | Trống (`filterDacThu:{}` — tất cả) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng CT = 5 | Có data — Tổng CT = 4 (Không xác định 3, Thương mại 1); đã Xem báo cáo ra kết quả | Không* |
| Thao tác | Xuất PDF (A4, Dọc) | Xuất PDF (`formatXuat=PDF`, khoGiay=A4, huongGiay=portrait) | Không |

\* Số CT lệch (5 vs 4) do seed 2 env khác nhau, nhưng CẢ HAI đều có data → nút Xuất bật → không đổi hành vi export. **0 GAP về điều kiện quyết định.**

**Kết quả:** `POST /api/v1/bao-cao/export` (formatXuat=PDF, khoGiay=A4, huongGiay=portrait) trả **HTTP 200** + `content-type: application/pdf` (size 16.576 bytes). KHÔNG có ERR-RPT-04.

**Kiểm nội dung file PDF (PyMuPDF):** trang A4 dọc (595.28×841.89pt ✓). Text theo thứ tự: `BC CHƯƠNG TRÌNH THEO LĨNH VỰC` → nhảy thẳng vào bảng (`Lĩnh vực PL` / `Số chương trình` / `Số DN tham gia` / `Không xác định` `3` `0` / `Thương mại` `1` `0`). **THIẾU 3 dòng header: "Kỳ báo cáo: Năm...", "Đơn vị: Toàn quốc", "Ngày tạo: 21/07/2026".** Bản Excel cùng báo cáo (CTTLV_05 đối chứng) CÓ đủ 4 trường → BE có sẵn data header, chỉ luồng dựng PDF bỏ khối header.

**Kết luận:** ERR-RPT-04 không tái hiện, nhưng file PDF xuất ra sai chuẩn TT17 (thiếu header) → **Open** (BUG-EXPORT-PDF-HEADER, lỗi template PDF dùng chung toàn module Báo cáo thống kê — đồng nhất batch 7/8 + CTTDVQL_05).

**Evidence:** `bug-reports/bctk/image/BUG-EXPORT-PDF-HEADER-CTTLV-pdf-no-header.png` (render PDF) + file dump `reverify-audit/_export-check-bctk12/bao-cao-ct-theo-linh-vuc.pdf` (+ .xlsx đối chứng).
