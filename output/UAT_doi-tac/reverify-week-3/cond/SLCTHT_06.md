# Bảng đối chiếu điều kiện — SLCTHT_06 (row 264) — Xuất Excel BC Số lượng chương trình hỗ trợ

**Verdict:** Reject — lỗi "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung khớp màn hình.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res SLCTHT_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT / admin) | `cbnv_tw_02` (CB Nghiệp vụ TW — vai trò chuẩn verdict §Nguyên tắc 3; role hẹp hơn admin, xuất chạy được → admin cũng chạy) | Không |
| Loại báo cáo | BC Số lượng chương trình hỗ trợ | BC Số lượng chương trình hỗ trợ | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Bộ lọc Trạng thái CT | Không chọn (tất cả) | Không chọn (tất cả) — filterDacThu:{} | Không |
| Dữ liệu tiền đề (phải có ≥1 CT mới bật nút Xuất) | Có data — Tổng chương trình 5 | Có data — Tổng chương trình 4 (ĐPD 2, ĐTH 1, HT 1; đã Xem báo cáo ra kết quả) | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** Thao tác thật (click Xuất Excel): toast "Đang tạo file..." (không có toast lỗi ERR-RPT-04) · `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_SO_LUONG_CT_HO_TRO, formatXuat=XLSX) trả **200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-so-luong-ct-ho-tro-2026-07-21.xlsx"` (6624 bytes). Nội dung .xlsx: header TT17 đủ 4/4 (tiêu đề + Kỳ + Đơn vị + Ngày tạo) + bảng (Trạng thái, Số chương trình): Đã phê duyệt 2 · Đang thực hiện 1 · Hoàn thành 1 — khớp màn hình.

**Ghi chú:** cấu trúc bảng chỉ theo trạng thái (thiếu chiều đơn vị/kỳ) là lỗi hiển thị đã log riêng batch 3 (`BUG-SLCTHT_04`), KHÔNG thuộc phạm vi case xuất file này. Case xuất Excel (SLCTHT_06) chỉ xét thao tác Xuất — thao tác chạy đúng, file nội dung khớp màn hình → Reject.

**Lưu ý env:** đối tác `htpldn-uat.ospgroup.vn`; QA `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
