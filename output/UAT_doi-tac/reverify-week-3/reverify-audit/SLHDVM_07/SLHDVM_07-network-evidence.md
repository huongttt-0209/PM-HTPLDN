# Network evidence — SLHDVM_07 (Xuất PDF)

**Env:** https://18.143.165.120.nip.io · **Account:** cbnv_tw_04 (CB Nghiệp vụ TW, Toàn quốc) · **Ngày:** 2026-07-21 15:36

## Luồng
- Bấm "Xuất PDF" → app mở dialog "Tùy chọn in báo cáo PDF" (khổ giấy A4/A3/Letter, hướng Dọc/Ngang; mặc định A4 + Dọc).
- Bấm "Xuất file" → `POST /api/v1/bao-cao/export` → **200**.
- Request body: `{"loaiBaoCao":"BC_HOI_DAP","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"PDF","khoGiay":"A4","huongGiay":"portrait"}`
- Response headers: `content-disposition: attachment; filename="bao-cao-hoi-dap-2026-07-21.pdf"` · `content-type: application/pdf` · body `<binary data>` (file PDF thật).

## Toast (tools/toast-capture.js — không lọc trùng, self-check soObserverDangSong=1)
- SO_REQUEST = 1 → `POST /api/v1/bao-cao/export`
- SO_KHUNG_THONG_BAO = 1 → "Đang tạo file..." (SRS item 14 dòng 1054). KHÔNG có toast ERR-RPT-04.

## Kết luận
Export PDF hoạt động đúng (200 + file .pdf auto-download). Lỗi ERR-RPT-04 KHÔNG tái hiện → Reject.

## Evidence đối tác (đã xem full-res)
- Video `partner-evidence/SLHDVM_07.webm` — frame `frames/t006.07s.jpg` bắt toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." trên env `htpldn-uat.ospgroup.vn`, login admin QTHT, báo cáo SLHDVM có data (Tổng 8, Lĩnh vực Thuế).
- Ảnh web env mình: `SLHDVM_07-web-pdf-click.png` (dialog tùy chọn PDF), `SLHDVM_07-web-pdf-xuat-file.png` (sau xuất, không toast lỗi).
