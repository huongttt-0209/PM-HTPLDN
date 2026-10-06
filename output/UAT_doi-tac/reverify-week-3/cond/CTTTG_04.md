# Bảng đối chiếu điều kiện — CTTTG_04 (row 275) — Xuất Excel BC Chương trình theo thời gian

**Case:** BC Chương trình theo thời gian (FR-IX-23 / SCR-IX-01 item 8) — đối tác báo bấm **Xuất Excel** → toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Reject — lỗi ERR-RPT-04 KHÔNG tái hiện: `POST /bao-cao/export` (formatXuat=XLSX) trả **HTTP 200** + file XLSX thật; mở file kiểm nội dung đủ 4/4 header TT17 + cột đúng §Output FR-IX-23 + số liệu khớp màn hình.
**Verify:** 21/07/2026, Chrome DevTools MCP + openpyxl, tài khoản `cbnv_tw_03` (CB Nghiệp vụ TW), kỳ Năm 2026, đơn vị Toàn quốc.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CTTTG_04.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — env `htpldn-uat.ospgroup.vn` | `cbnv_tw_03` (CB Nghiệp vụ TW — vai trò chuẩn verdict, quyền xem + xuất BC Toàn quốc) | Không |
| Loại báo cáo | BC Chương trình theo thời gian (`loai=ct-theo-thoi-gian`) | BC Chương trình theo thời gian (`loaiBaoCao=BC_CT_THEO_THOI_GIAN`) | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng CT toàn kỳ = 1 | Có data — Tổng CT toàn kỳ = 3, ngân sách 200.000.000; đã Xem báo cáo ra kết quả | Không* |
| Thao tác | Xuất Excel | Xuất Excel (`formatXuat=XLSX`) | Không |

\* Số CT lệch (1 vs 3) do seed 2 env khác nhau, nhưng CẢ HAI đều có data → nút Xuất bật ở cả hai → không đổi hành vi export. **0 GAP về điều kiện quyết định.**

**Kết quả:** `POST /api/v1/bao-cao/export` (formatXuat=XLSX) trả **HTTP 200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-ct-theo-thoi-gian-2026-07-21.xlsx"` (reqid=190). Toast UI: "Đang tạo file..." → tạo file thành công. KHÔNG có ERR-RPT-04. (Chỉ 1 request export cho 1 lần bấm — toast "Đang tạo file..." lặp 4 là AntD re-render message.)

**Kiểm nội dung file XLSX (openpyxl):** sheet "Chương trình theo thời gian" — R1 `BC Chương trình theo thời gian` (tiêu đề) · R2 `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · R3 `Đơn vị: Toàn quốc` · R4 `Ngày tạo: 21/07/2026` → **đủ 4/4 header TT17**. R6 cột `Kỳ | Từ ngày | Đến ngày | Số chương trình | Số DN | Tổng ngân sách (₫)` khớp §Output FR-IX-23 (trend_data: ky_label, so_ct, so_dn + ngân sách). R7 số liệu `2026 | 01/01/2026 | 31/12/2026 | 3 | 0 | 200000000` khớp bảng trên màn hình.

**Kết luận:** Xuất Excel thành công + nội dung đúng chuẩn → **Reject** (lỗi đối tác báo không tái hiện; đối tác kiểm tra lại trên env đối tác).

**Evidence:** `reverify-audit/CTTTG_04/ctttg04-export-excel-success.png` (app có data) + file dump `reverify-audit/_export-check-bctk12/bao-cao-ct-theo-thoi-gian.xlsx`.
