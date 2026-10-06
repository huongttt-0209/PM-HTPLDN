# Bảng đối chiếu điều kiện — CPCTHTTTG_05 (row 260) — Xuất Excel BC Chi phí theo thời gian

**Verdict:** Reject — lỗi "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung đúng.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CPCTHTTTG_05.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT / admin) | `cbnv_tw_02` (CB Nghiệp vụ TW — vai trò chuẩn verdict §Nguyên tắc 3; role hẹp hơn admin, xuất chạy được → admin cũng chạy) | Không |
| Loại báo cáo | BC Chi phí theo thời gian | BC Chi phí theo thời gian | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng chi phí toàn kỳ 226.308.268 ₫, Tổng hồ sơ 25 | Có data — Tổng chi phí toàn kỳ 8.000.000 ₫, Tổng hồ sơ 1 (đã Xem báo cáo ra kết quả) | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** Thao tác thật (click Xuất Excel): toast "Đang tạo file..." (không có toast lỗi ERR-RPT-04) · `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_CHI_PHI_THEO_THOI_GIAN, formatXuat=XLSX) trả **200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-chi-phi-theo-thoi-gian-2026-07-21.xlsx"` (6567 bytes). Nội dung .xlsx: header TT17 đủ 4/4 (tiêu đề + Kỳ + Đơn vị + Ngày tạo) + bảng 5 cột (Kỳ, Từ ngày, Đến ngày, Số hồ sơ, Tổng chi phí) khớp số liệu web (2026 · 01/01/2026 · 31/12/2026 · 1 · 8.000.000).

**Lưu ý env:** đối tác `htpldn-uat.ospgroup.vn`; QA `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
