# Bảng đối chiếu điều kiện — SLHDVM_06 (row 191)

**Case:** Xuất Excel — BC Số lượng hỏi đáp/vướng mắc pháp luật (FR-IX-01 / UC124).
**Đối tác báo:** bấm Xuất Excel → toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Reject — lỗi KHÔNG tái hiện (export trả 200 + file .xlsx tải về).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | admin (QTHT) — phạm vi Toàn quốc (thấy trong video, góc phải "Quản trị viên QTHT · BTP · TW") | `cbnv_tw_04` (CB Nghiệp vụ TW) — phạm vi Toàn quốc. Đây là đúng vai trò verdict của case (Tác nhân = Cán bộ nghiệp vụ); Xuất là chức năng dùng chung, vai trò chỉ đổi phạm vi data, cả 2 đều Toàn quốc + có data | Không |
| Entity + trạng thái | Báo cáo SLHDVM đã "Xem báo cáo" ra data (Tổng hỏi đáp = 8), nút Xuất Excel đã bật | Báo cáo SLHDVM đã "Xem báo cáo" ra data (Tổng hỏi đáp = 11), nút Xuất Excel đã bật | Không |
| Dữ liệu tiền đề | Kỳ = Năm 2026, Đơn vị = Toàn quốc, Lĩnh vực PL = Thuế → báo cáo CÓ data (8 hỏi đáp) | Kỳ = Năm 2026, Đơn vị = Toàn quốc, không lọc Lĩnh vực → báo cáo CÓ data (11 hỏi đáp, gồm Thuế 4). Tập data là superset của đối tác; đã có data để xuất | Không |
| Input / filter | Thao tác Xuất Excel (.xlsx) | Thao tác Xuất Excel (.xlsx) — cùng endpoint `POST /api/v1/bao-cao/export`, body `formatXuat: "XLSX"` | Không |

**Kết quả đóng GAP:** 0 GAP. Đã tái hiện đúng điều kiện đối tác (báo cáo có data + đúng cấp Toàn quốc + Xuất Excel). Kết quả: `POST /api/v1/bao-cao/export` trả **200**, header `content-disposition: attachment; filename="bao-cao-hoi-dap-2026-07-21.xlsx"`, body binary XLSX thật → file được tạo và tải về. Toast quan sát = "Đang tạo file..." (SRS item 14), KHÔNG có toast "Không thể tạo file xuất". Lỗi ERR-RPT-04 không xảy ra.

**Ghi chú env:** đối tác test trên `htpldn-uat.ospgroup.vn` (env đối tác), mình test trên `18.143.165.120.nip.io` (env được giao). Lỗi không tái hiện trên env mình → Reject + "Đối tác kiểm tra lại".
