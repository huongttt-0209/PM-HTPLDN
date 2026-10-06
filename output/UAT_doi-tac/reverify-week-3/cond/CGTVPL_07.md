# Bảng đối chiếu điều kiện — CGTVPL_07 (row 231) — Xuất PDF BC Số lượng CG/TVV

**Kết luận:** Open — lỗi đối tác báo (ERR-RPT-04 "Không thể tạo file xuất") KHÔNG tái hiện (Xuất PDF thành công, HTTP 200), NHƯNG file PDF xuất ra thiếu 3/4 dòng header bắt buộc (Kỳ báo cáo / Đơn vị / Ngày tạo) — sai SRS `srs-fr-11-bao-cao.md:1088`. Bản Excel cùng báo cáo có đủ 4/4.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res `partner-evidence/CGTVPL_07.jpg`) | Mình test (cbnv_tw, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT/admin) | cbnv_tw (CB Nghiệp vụ TW — đúng Tác nhân SRS) | Không |
| Entity + trạng thái | Báo cáo CG/TVV đã "Xem báo cáo" ra dữ liệu | Báo cáo CG/TVV đã "Xem báo cáo" ra dữ liệu (Tổng 2) | Không |
| Dữ liệu tiền đề | Có CG/TVV đang hoạt động | Có CG/TVV đang hoạt động (2 TVV) | Không |
| Input / filter | loai=so-luong-cg-tvv, Kỳ Năm 2026, Đơn vị Cục Bổ trợ tư pháp (BTP-TW), Lĩnh vực CM=Thuế | Y HỆT | Không |
| Khổ giấy / hướng (chỉ ảnh hưởng PDF) | (đối tác không ghi) A4 mặc định | A4 / Dọc (portrait — mặc định, dạng bảng) | Không |

**Artifact real-data:** file `cgtvpl_07.pdf` (PyMuPDF text: chỉ "BC SỐ LƯỢNG CG/TVV" → vào thẳng bảng; grep "Kỳ báo cáo"/"Đơn vị:"/"Ngày tạo" = MISSING), ảnh so sánh `bug-reports/bctk/image/BUG-CGTVPL-PDF-HEADER-compare.png`. Cùng lỗi template PDF dùng chung đã xác nhận batch7/8 (7 loại BC) → nay +CG/TVV.
