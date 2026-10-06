# Bảng đối chiếu điều kiện — CTTDVQL_04 (row 268) — Xuất Excel BC Chương trình theo đơn vị

**Case:** BC Chương trình theo đơn vị (FR-IX-21 / UC144) — đối tác báo bấm **Xuất Excel** → toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Reject — lỗi ERR-RPT-04 KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung file đúng.
**Verify:** 21/07/2026, Chrome DevTools MCP, tài khoản `cbnv_tw_03` (CB Nghiệp vụ TW — vai trò chuẩn verdict), kỳ Năm 2026, đơn vị Toàn quốc.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CTTDVQL_04.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — env `htpldn-uat.ospgroup.vn` | `cbnv_tw_03` (CB Nghiệp vụ TW — vai trò chuẩn verdict, có quyền xem + xuất BC phạm vi Toàn quốc). QTHT quyền rộng hơn | Không |
| Loại báo cáo | BC Chương trình theo đơn vị (`loai=ct-theo-don-vi`) | BC Chương trình theo đơn vị (`loaiBaoCao=BC_CT_THEO_DON_VI`) | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng CT = 5, ngân sách = 0 | Có data — Tổng CT = 4, ngân sách = 300.000.000 (đã Xem báo cáo ra kết quả) | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** Đã tái hiện đúng điều kiện đối tác (CT theo đơn vị, Năm 2026, Toàn quốc, báo cáo có data → bấm Xuất Excel).

**Kết quả:** `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_CT_THEO_DON_VI, formatXuat=XLSX) trả **HTTP 200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-ct-theo-don-vi-2026-07-21.xlsx"` (reqid=96). Toast trên UI: "Đang tạo file..." → **"Tạo file thành công."** (xanh). KHÔNG có toast ERR-RPT-04.

**Kiểm nội dung file (openpyxl):** đủ 4/4 header TT17 (tiêu đề BC + Kỳ báo cáo + Đơn vị + Ngày tạo) + cột đúng §Output FR-IX-21 (Đơn vị · Cấp đơn vị · Số chương trình · Tổng ngân sách) + data khớp màn hình (Cục Bổ trợ tư pháp - Bộ Tư pháp · TW · 4 · 300000000).

**Lưu ý env:** đối tác env `htpldn-uat.ospgroup.vn` (build khác), QA env `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.

**Evidence:** `reverify-audit/CTTDVQL_04/cttdvql04-export-excel-success.png` + file dump `reverify-audit/_export-check-bctk12/bao-cao-ct-theo-don-vi.xlsx`.
