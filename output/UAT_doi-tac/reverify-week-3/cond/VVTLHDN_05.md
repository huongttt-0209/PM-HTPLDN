# Bảng đối chiếu điều kiện — VVTLHDN_05 (row 246) — Xuất Excel BC Vụ việc theo loại hình DN

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung đúng chuẩn TT17.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res VVTLHDN_05.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_01` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict, có quyền xem + xuất BC). Xuất thành công với vai trò nghiệp vụ đã bao phủ; QTHT quyền rộng hơn nên không thể là lý do đối tác lỗi mà mình pass | Không |
| Loại báo cáo | BC Vụ việc theo loại hình DN | BC Vụ việc theo loại hình DN | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc | Không |
| Bộ lọc Loại DN (đặc thù, tùy chọn) | Để trống (Chọn Loại DN) | Để trống (không lọc) — khớp đối tác | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — đã Xem báo cáo ra biểu đồ | Có data — Nhỏ 3 + Siêu nhỏ 14 (Tổng 17), đã Xem báo cáo trước khi Xuất | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (formatXuat=XLSX, reqid=110) trả **200** + `content-disposition: attachment; filename="bao-cao-vu-viec-theo-loai-dn-2026-07-21.xlsx"`. Toast = "Đang tạo file...", KHÔNG phải ERR-RPT-04.

**Kiểm nội dung file (openpyxl):** header TT17 ĐỦ 4/4 (tiêu đề + Kỳ + Đơn vị: Toàn quốc + Ngày tạo: 21/07/2026) + số liệu khớp màn hình (Nhỏ 3, Siêu nhỏ 14). File gốc: `reverify-audit/_export-check/VVTLHDN_05.xlsx`.

**Lưu ý env:** đối tác test `htpldn-uat.ospgroup.vn`; QA verify `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
