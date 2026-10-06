# Bảng đối chiếu điều kiện — CPCTHTTDVQL_06 (row 253) — Xuất Excel BC Chi phí theo đơn vị

**Verdict:** Reject — lỗi "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung đúng.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CPCTHTTDVQL_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT / admin) | `cbnv_tw_02` (CB Nghiệp vụ TW — vai trò chuẩn verdict §Nguyên tắc 3, có quyền xem + xuất BC). Role hẹp hơn admin: xuất chạy được cho role hẹp → admin (rộng hơn) cũng chạy | Không |
| Loại báo cáo | BC Chi phí theo đơn vị | BC Chi phí theo đơn vị | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng hồ sơ 25, Tổng chi phí 226.308.268 ₫ | Có data — Tổng hồ sơ 1, Tổng chi phí 8.000.000 ₫ (đã Xem báo cáo ra kết quả; 25 dòng vẫn xa dưới trần 10.000 dòng nên khối lượng không đổi kết quả xuất) | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** Thao tác thật (click nút Xuất Excel): toast "Đang tạo file..." (không có toast lỗi ERR-RPT-04) · `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_CHI_PHI_THEO_DON_VI, formatXuat=XLSX) trả **200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-chi-phi-theo-don-vi-2026-07-21.xlsx"` (6594 bytes) — reqid=175. Nội dung .xlsx: header TT17 đủ 4/4 (tiêu đề + Kỳ + Đơn vị + Ngày tạo) + bảng khớp số liệu web.

**Lưu ý env:** đối tác `htpldn-uat.ospgroup.vn`; QA `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
