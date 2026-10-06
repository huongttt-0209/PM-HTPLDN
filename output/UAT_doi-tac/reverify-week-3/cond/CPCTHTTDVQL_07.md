# Bảng đối chiếu điều kiện — CPCTHTTDVQL_07 (row 254) — Xuất PDF BC Chi phí theo đơn vị

**Verdict:** Open — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện (file PDF tạo được, HTTP 200), NHƯNG file PDF xuất ra **thiếu 3/4 dòng header bắt buộc** (Kỳ báo cáo / Đơn vị / Ngày tạo) — bản Excel cùng báo cáo có đủ → vi phạm SCR-IX-01 §Quy tắc tương tác (dòng 1088). Bug: BUG-EXPORT-PDF-HEADER.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CPCTHTTDVQL_07.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT / admin) | `cbnv_tw_02` (CB Nghiệp vụ TW — vai trò chuẩn verdict §Nguyên tắc 3). Header do BE dựng, không phụ thuộc role | Không |
| Loại báo cáo | BC Chi phí theo đơn vị | BC Chi phí theo đơn vị | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc (khớp đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng hồ sơ 25, Tổng chi phí 226.308.268 ₫ | Có data — Tổng hồ sơ 1, Tổng chi phí 8.000.000 ₫ (đã Xem báo cáo ra kết quả) | Không |
| Thao tác | Xuất PDF (.pdf), khổ A4 dọc | Xuất PDF (.pdf), khổ A4 dọc (mặc định hộp thoại) | Không |

**0 GAP.** Thao tác thật (Xuất PDF → hộp thoại "Tùy chọn in báo cáo PDF" A4/Dọc → Xuất file): toast "Đang tạo file..." (không có toast lỗi ERR-RPT-04) · `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_CHI_PHI_THEO_DON_VI, formatXuat=PDF, khoGiay=A4, huongGiay=portrait) trả **200** + `content-type: application/pdf` + `content-disposition: attachment; filename="bao-cao-chi-phi-theo-don-vi-2026-07-21.pdf"` (16610 bytes). Nội dung .pdf (PyMuPDF): A4 210×297mm, font Tinos (Times New Roman-compatible) 13 — chỉ có tiêu đề "BC CHI PHÍ THEO ĐƠN VỊ" rồi vào thẳng bảng; **thiếu** "Kỳ báo cáo", "Đơn vị: Toàn quốc", "Ngày tạo". Bản Excel cùng báo cáo (đối chứng) có đủ 4/4.

**Lưu ý env:** đối tác `htpldn-uat.ospgroup.vn`; QA `18.143.165.120.nip.io`. Lỗi "không thể tạo file" không tái hiện, nhưng lỗi thiếu header PDF là bug thật (khác lỗi đối tác báo) → Open.
