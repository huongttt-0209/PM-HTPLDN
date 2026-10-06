# Bảng đối chiếu điều kiện — CTTLV_05 (row 273) — Xuất Excel BC Chương trình theo lĩnh vực

**Case:** BC Chương trình theo lĩnh vực (FR-IX-22 / SCR-IX-01 item 8) — đối tác báo bấm **Xuất Excel** → toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Reject — lỗi ERR-RPT-04 KHÔNG tái hiện: `POST /bao-cao/export` (formatXuat=XLSX) trả **HTTP 200** + file XLSX thật; mở file kiểm nội dung đủ 4/4 header TT17 + cột đúng §Output FR-IX-22 + số liệu khớp màn hình.
**Verify:** 21/07/2026, Chrome DevTools MCP + openpyxl, tài khoản `cbnv_tw_03` (CB Nghiệp vụ TW), kỳ Năm 2026, đơn vị Toàn quốc.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CTTLV_05.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — env `htpldn-uat.ospgroup.vn` | `cbnv_tw_03` (CB Nghiệp vụ TW — vai trò chuẩn verdict, quyền xem + xuất BC Toàn quốc) | Không |
| Loại báo cáo | BC Chương trình theo lĩnh vực (`loai=ct-theo-linh-vuc`) | BC Chương trình theo lĩnh vực (`loaiBaoCao=BC_CT_THEO_LINH_VUC`) | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Lĩnh vực (filter đặc thù) | Trống ("Chọn Lĩnh vực" — tất cả) | Trống (`filterDacThu:{}` — tất cả) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng CT = 5 | Có data — Tổng CT = 4 (Không xác định 3, Thương mại 1); đã Xem báo cáo ra kết quả | Không* |
| Thao tác | Xuất Excel | Xuất Excel (`formatXuat=XLSX`) | Không |

\* Số CT lệch (5 vs 4) do seed 2 env khác nhau, nhưng CẢ HAI đều có data → nút Xuất bật ở cả hai → không đổi hành vi export. **0 GAP về điều kiện quyết định.**

**Kết quả:** `POST /api/v1/bao-cao/export` (formatXuat=XLSX) trả **HTTP 200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-ct-theo-linh-vuc-2026-07-21.xlsx"` (reqid=174). Toast UI: "Đang tạo file..." → tạo file thành công. KHÔNG có ERR-RPT-04. (Chỉ 1 request export cho 1 lần bấm — toast "Đang tạo file..." lặp 4 là AntD re-render message, không phải 4 request.)

**Kiểm nội dung file XLSX (openpyxl):** sheet "Chương trình theo lĩnh vực" — R1 `BC Chương trình theo lĩnh vực` (tiêu đề) · R2 `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · R3 `Đơn vị: Toàn quốc` · R4 `Ngày tạo: 21/07/2026` → **đủ 4/4 header TT17**. R6 cột `Lĩnh vực PL | Số chương trình | Số DN tham gia` khớp §Output FR-IX-22 (ten_linh_vuc, so_ct, so_dn_tham_gia). R7-R8 số liệu `Không xác định 3 / 0` · `Thương mại 1 / 0` khớp bảng trên màn hình.

**Kết luận:** Xuất Excel thành công + nội dung đúng chuẩn → **Reject** (lỗi đối tác báo không tái hiện; đối tác kiểm tra lại trên env đối tác).

**Evidence:** `reverify-audit/CTTLV_05/cttlv05-export-excel-success.png` (app có data) + file dump `reverify-audit/_export-check-bctk12/bao-cao-ct-theo-linh-vuc.xlsx`.
