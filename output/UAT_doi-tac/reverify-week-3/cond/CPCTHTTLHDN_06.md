# Bảng đối chiếu điều kiện — CPCTHTTLHDN_06 (row 257) — Xuất Excel BC Chi phí theo loại hình DN

**Verdict:** Reject — lỗi "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung đúng.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CPCTHTTLHDN_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT / admin) | `cbnv_tw_02` (CB Nghiệp vụ TW — vai trò chuẩn verdict §Nguyên tắc 3; role hẹp hơn admin, xuất chạy được → admin cũng chạy) | Không |
| Loại báo cáo | BC Chi phí theo loại hình DN | BC Chi phí theo loại hình DN | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Bộ lọc Loại DN | Không chọn (tất cả) | Không chọn (tất cả) — filterDacThu:{} | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng hồ sơ 25, Tổng chi phí 226.308.268 ₫ | Có data — Tổng hồ sơ 1, Tổng chi phí 8.000.000 ₫ (đã Xem báo cáo ra kết quả) | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** Thao tác thật (click Xuất Excel): toast "Đang tạo file..." (không có toast lỗi ERR-RPT-04) · `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_CHI_PHI_THEO_LOAI_DN, formatXuat=XLSX) trả **200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-chi-phi-theo-loai-dn-2026-07-21.xlsx"` (6712 bytes). Nội dung .xlsx: header TT17 đủ 4/4 (tiêu đề + Kỳ + Đơn vị + Ngày tạo) + bảng 7 cột (Quy mô DN, Số hồ sơ, Tổng chi phí, Mức hỗ trợ %, Trần/hồ sơ, Trần chi phí, Chênh lệch) khớp số liệu web (Siêu nhỏ · 1 · 8.000.000 · 100 · 30.000.000 · 30.000.000 · -22.000.000).

**Lưu ý env:** đối tác `htpldn-uat.ospgroup.vn`; QA `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
