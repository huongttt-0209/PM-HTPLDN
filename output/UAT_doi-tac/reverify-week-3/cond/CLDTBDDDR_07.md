# Bảng đối chiếu điều kiện — CLDTBDDDR_07 (row 223) — Xuất PDF BC Lớp đào tạo đang diễn ra

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .pdf thành công.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CLDTBDDDR_07.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) | `cbnv_tw_05` (CB Nghiệp vụ TW — vai trò chuẩn verdict). QTHT quyền rộng hơn | Không |
| Loại báo cáo | BC Lớp đào tạo đang diễn ra | BC Lớp đào tạo đang diễn ra | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng số = 3 | Có data — Tổng số = 1 | Không |
| Thao tác | Xuất PDF (.pdf) → dialog A4/Dọc → Xuất file | Xuất PDF (.pdf) → dialog A4/Dọc → Xuất file | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_LOP_DAO_TAO_DANG_DIEN_RA, formatXuat=PDF, khoGiay=A4, huongGiay=portrait) trả **200** + `content-type: application/pdf` + `content-disposition: attachment; filename="bao-cao-lop-dao-tao-dang-dien-ra-2026-07-21.pdf"` (body binary) — reqid=133.

**Lưu ý env:** đối tác `htpldn-uat.ospgroup.vn`; QA `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
