# Audit — CTTDVQL_04 (row 268) — Xuất Excel BC Chương trình theo đơn vị — Verdict: Reject

## 3 CỔNG
- **Cổng 1 (bằng chứng):** `partner-evidence/CTTDVQL_04.jpg` (228379 bytes), full-res đã mở. Neo: (a) URL `htpldn-uat.ospgroup.vn/bao-cao?loai=ct-theo-don-vi&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`; (b) trạng thái: báo cáo CÓ data (Tổng CT=5, ngân sách=0), toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." hiển thị; (c) role QTHT, ngày 16/07/2026.
- **Cổng 2 (hiểu bug):** đối tác bấm **Xuất Excel** trên báo cáo CT theo đơn vị (có data) → nhận toast lỗi ERR-RPT-04, không tải được file. Frame lỗi rõ trong ảnh.
- **Cổng 3 (đối chiếu):** SCR-IX-01 item 8 (dòng 1048) "Xuất Excel → click → auto-download, sau khi đã Xem báo cáo"; AC "Given CB nhấn Xuất Excel When click Then tải file .xlsx theo TT17/2025" (dòng 124). §Quy tắc tương tác dòng 1088: header file gồm tiêu đề + kỳ + đơn vị + ngày tạo.

## Kết quả verify (env nip.io, cbnv_tw_03)
- Tiền đề đủ: đã Xem báo cáo ra data (Tổng CT=4, ngân sách 300.000.000) → nút Xuất Excel bật.
- Bấm Xuất Excel: `POST /api/v1/bao-cao/export` (reqid=96) → **200**, content-type xlsx, filename `bao-cao-ct-theo-don-vi-2026-07-21.xlsx`.
- Toast UI (toast-capture.js, observer=1): "Đang tạo file..." → **"Tạo file thành công."** (xanh). KHÔNG có ERR-RPT-04.
- Nội dung file (openpyxl) đúng: 4/4 header TT17 + cột §Output FR-IX-21 + data khớp màn hình.

## Kết luận
Lỗi cụ thể đối tác báo ("Không thể tạo file xuất") **KHÔNG tái hiện** trên env QA — export chạy đúng, file .xlsx tạo được và nội dung chính xác → **Reject** (bất đồng về THỰC TẾ, khả năng lỗi env/thời điểm bên đối tác). → Đối tác kiểm tra lại.

## Evidence
- `cttdvql04-export-excel-success.png` — toast "Tạo file thành công" + báo cáo có data.
- `../_export-check-bctk12/bao-cao-ct-theo-don-vi.xlsx` — file thật dump từ response, nội dung đủ header + cột + data.
