# Bảng đối chiếu điều kiện — DGHQHTPL_07 (row 234) — Xuất PDF BC Đánh giá hiệu quả HTPL

**Kết luận:** Open — ERR-RPT-04 KHÔNG tái hiện (Xuất PDF thành công, HTTP 200), NHƯNG file PDF thiếu 3/4 dòng header bắt buộc (Kỳ báo cáo / Đơn vị / Ngày tạo) — sai SRS `srs-fr-11-bao-cao.md:1088`. Bản Excel cùng báo cáo có đủ 4/4.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/DGHQHTPL_07.jpg`) | Mình test (cbnv_tw, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT/admin) | cbnv_tw (CB Nghiệp vụ TW — đúng Tác nhân SRS) | Không |
| Entity + trạng thái | Báo cáo Đánh giá HTPL có data | Báo cáo Đánh giá HTPL có data (2 đợt / 4 lượt) | Không |
| Dữ liệu tiền đề | Có đợt/lượt đánh giá | Có đợt/lượt đánh giá (3 đơn vị) | Không |
| Input / filter | loai=danh-gia-hieu-qua, Năm 2026, Toàn quốc, Đợt="TKM kiểm thử 2" | loai=danh-gia-hieu-qua, Năm 2026, Toàn quốc, không lọc đợt | Không* |
| Khổ giấy / hướng (chỉ ảnh hưởng PDF) | A4 mặc định | A4 / Dọc (portrait, dạng bảng) | Không |

\* Đợt "TKM kiểm thử 2" không seed trên env; bộ lọc đợt chỉ thu hẹp dòng data, không đổi việc header PDF bị thiếu (lỗi template PDF dùng chung, không phụ thuộc data rows). Không ảnh hưởng kết quả.

**Artifact real-data:** file `dghqhtpl_07.pdf` (PyMuPDF: chỉ "BC ĐÁNH GIÁ HIỆU QUẢ HTPL" → vào thẳng bảng; "Kỳ báo cáo"/"Đơn vị:"/"Ngày tạo" = MISSING), ảnh so sánh `bug-reports/bctk/image/BUG-DGHQHTPL-PDF-HEADER-compare.png`. Cùng lỗi template PDF dùng chung batch7/8.
