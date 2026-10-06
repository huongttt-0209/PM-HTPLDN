# Bảng đối chiếu điều kiện — VVDHTHT_07 (row 210)

**Case:** Xuất PDF — BC Vụ việc đã hoàn thành (FR-IX-04 / UC127).
**Đối tác báo:** bấm Xuất → toast "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Open — lỗi đối tác báo (ERR-RPT-04 "không tạo được file") KHÔNG tái hiện (export 200 + file .pdf tải về). NHƯNG kiểm tra **nội dung** file PDF phát hiện lỗi khác: **thiếu 3/4 header bắt buộc** (Kỳ báo cáo / Đơn vị / Ngày tạo) theo SRS `srs-fr-11-bao-cao.md:1088` — bản Excel có đủ. → **Open** (BUG-EXPORT-PDF-HEADER, xem `bug-reports/bctk/Pass-bug-report-bctk-batch7-export.md`).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | admin (QTHT) — phạm vi Toàn quốc | `cbnv_tw_04` (CB Nghiệp vụ TW) — Toàn quốc. Đúng vai trò verdict; Xuất là chức năng dùng chung | Không |
| Entity + trạng thái | BC VVDHTHT đã "Xem báo cáo" ra data (Tổng vụ việc = 4), nút Xuất bật | BC VVDHTHT đã "Xem báo cáo" ra data (Tổng vụ việc = 5), nút Xuất bật | Không |
| Dữ liệu tiền đề | Kỳ Năm 2026, Đơn vị Cục Bổ trợ tư pháp (BTP-TW) → CÓ data (4) | Kỳ Năm 2026, Đơn vị Toàn quốc (bao gồm Cục Bổ trợ) → CÓ data (5). Có data để xuất | Không |
| Input / filter | Xuất PDF (.pdf) | Xuất PDF (.pdf) — dialog tùy chọn (A4/Dọc) → Xuất file → `POST /api/v1/bao-cao/export` body `formatXuat: PDF, khoGiay: A4, huongGiay: portrait` | Không |

**Kết quả đóng GAP:** 0 GAP. `POST /api/v1/bao-cao/export` trả **200**, `content-disposition: attachment; filename="bao-cao-vu-viec-hoan-thanh-2026-07-21.pdf"`, `content-type: application/pdf`, body binary PDF → file tải về. Toast = "Đang tạo file...", KHÔNG có ERR-RPT-04. Đối tác test env `htpldn-uat.ospgroup.vn`, mình test `18.143.165.120.nip.io` → lỗi không tái hiện → Reject.
