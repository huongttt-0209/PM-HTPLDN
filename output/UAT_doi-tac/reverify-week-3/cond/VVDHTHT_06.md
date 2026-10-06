# Bảng đối chiếu điều kiện — VVDHTHT_06 (row 209)

**Case:** Xuất Excel — BC Vụ việc đã hoàn thành (FR-IX-04 / UC127).
**Đối tác báo:** bấm Xuất → toast "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Reject — lỗi KHÔNG tái hiện (export trả 200 + file .xlsx tải về).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | admin (QTHT) — phạm vi Toàn quốc | `cbnv_tw_04` (CB Nghiệp vụ TW) — Toàn quốc. Đúng vai trò verdict; Xuất là chức năng dùng chung | Không |
| Entity + trạng thái | BC VVDHTHT đã "Xem báo cáo" ra data (Tổng vụ việc = 4), nút Xuất bật | BC VVDHTHT đã "Xem báo cáo" ra data (Tổng vụ việc = 5), nút Xuất bật | Không |
| Dữ liệu tiền đề | Kỳ Năm 2026, Đơn vị Cục Bổ trợ tư pháp (BTP-TW) → CÓ data (4) | Kỳ Năm 2026, Đơn vị Toàn quốc (bao gồm Cục Bổ trợ) → CÓ data (5, Lĩnh vực Thương mại 5). Có data để xuất | Không |
| Input / filter | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) — `POST /api/v1/bao-cao/export` body `loaiBaoCao: BC_VU_VIEC_HOAN_THANH, formatXuat: XLSX` | Không |

**Kết quả đóng GAP:** 0 GAP. `POST /api/v1/bao-cao/export` trả **200**, `content-disposition: attachment; filename="bao-cao-vu-viec-hoan-thanh-2026-07-21.xlsx"`, body binary XLSX → file tải về. Toast = "Đang tạo file...", KHÔNG có ERR-RPT-04. Đối tác test env `htpldn-uat.ospgroup.vn`, mình test `18.143.165.120.nip.io` → lỗi không tái hiện → Reject.
