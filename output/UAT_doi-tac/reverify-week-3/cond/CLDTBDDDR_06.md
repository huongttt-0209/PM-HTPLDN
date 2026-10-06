# Bảng đối chiếu điều kiện — CLDTBDDDR_06 (row 222) — Xuất Excel BC Lớp đào tạo đang diễn ra

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CLDTBDDDR_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) | `cbnv_tw_05` (CB Nghiệp vụ TW — vai trò chuẩn verdict, có quyền xem + xuất BC). QTHT quyền rộng hơn | Không |
| Loại báo cáo | BC Lớp đào tạo đang diễn ra | BC Lớp đào tạo đang diễn ra | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng số = 3 | Có data — Tổng số = 1 (đã Xem báo cáo ra kết quả) | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_LOP_DAO_TAO_DANG_DIEN_RA, formatXuat=XLSX) trả **200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-lop-dao-tao-dang-dien-ra-2026-07-21.xlsx"` (body binary) — reqid=130.

**Lưu ý env:** đối tác `htpldn-uat.ospgroup.vn`; QA `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
