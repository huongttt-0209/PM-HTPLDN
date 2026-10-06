# Bảng đối chiếu điều kiện — SLHDVM_07 (row 192)

**Case:** Xuất PDF — BC Số lượng hỏi đáp/vướng mắc pháp luật (FR-IX-01 / UC124).
**Đối tác báo:** bấm Xuất PDF → toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04).
**Verdict:** Open — lỗi đối tác báo (ERR-RPT-04 "không tạo được file") KHÔNG tái hiện (export 200 + file .pdf tải về). NHƯNG kiểm tra **nội dung** file PDF phát hiện lỗi khác: **thiếu 3/4 header bắt buộc** (Kỳ báo cáo / Đơn vị / Ngày tạo) theo SRS `srs-fr-11-bao-cao.md:1088` — bản Excel có đủ. → **Open** (BUG-EXPORT-PDF-HEADER, xem `bug-reports/bctk/Pass-bug-report-bctk-batch7-export.md`).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | admin (QTHT) — phạm vi Toàn quốc (video, góc phải "Quản trị viên QTHT · BTP · TW") | `cbnv_tw_04` (CB Nghiệp vụ TW) — phạm vi Toàn quốc. Đúng vai trò verdict của case; Xuất là chức năng dùng chung, cả 2 đều Toàn quốc + có data | Không |
| Entity + trạng thái | Báo cáo SLHDVM đã "Xem báo cáo" ra data (Tổng hỏi đáp = 8), nút Xuất PDF đã bật | Báo cáo SLHDVM đã "Xem báo cáo" ra data (Tổng hỏi đáp = 11), nút Xuất PDF đã bật | Không |
| Dữ liệu tiền đề | Kỳ = Năm 2026, Đơn vị = Toàn quốc, Lĩnh vực PL = Thuế → báo cáo CÓ data (8) | Kỳ = Năm 2026, Đơn vị = Toàn quốc, không lọc Lĩnh vực → báo cáo CÓ data (11, gồm Thuế 4). Superset của đối tác | Không |
| Input / filter | Thao tác Xuất PDF (.pdf) | Thao tác Xuất PDF (.pdf) — mở dialog "Tùy chọn in báo cáo PDF" (khổ giấy A4, hướng Dọc mặc định) → bấm "Xuất file" → `POST /api/v1/bao-cao/export` body `formatXuat: "PDF", khoGiay: "A4", huongGiay: "portrait"` | Không |

**Kết quả đóng GAP:** 0 GAP. Đã tái hiện đúng điều kiện đối tác (báo cáo có data + cấp Toàn quốc + Xuất PDF). Kết quả: `POST /api/v1/bao-cao/export` trả **200**, header `content-disposition: attachment; filename="bao-cao-hoi-dap-2026-07-21.pdf"`, `content-type: application/pdf`, body binary PDF thật → file được tạo và tải về. Toast quan sát = "Đang tạo file..." (SRS item 14), KHÔNG có toast "Không thể tạo file xuất". Lỗi ERR-RPT-04 không xảy ra.

**Ghi chú:** app env mình mở thêm dialog chọn khổ giấy/hướng giấy trước khi xuất PDF (không có trong SRS nhưng không phải lỗi — vẫn ra file đúng). Đối tác test trên `htpldn-uat.ospgroup.vn`, mình test trên `18.143.165.120.nip.io`. Lỗi không tái hiện → Reject + "Đối tác kiểm tra lại".
