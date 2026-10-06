# Network evidence — SLHDVM_06 (Xuất Excel)

**Env:** https://18.143.165.120.nip.io · **Account:** cbnv_tw_04 (CB Nghiệp vụ TW, Toàn quốc) · **Ngày:** 2026-07-21 15:30

## Request xuất
- `POST /api/v1/bao-cao/export` → **200**
- Request body: `{"loaiBaoCao":"BC_HOI_DAP","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}`
- Response headers:
  - `content-disposition: attachment; filename="bao-cao-hoi-dap-2026-07-21.xlsx"`
  - `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
  - Response body: `<binary data>` (file XLSX thật)

## Toast quan sát (tools/toast-capture.js — không lọc trùng, self-check soObserverDangSong=1)
- SO_REQUEST = 1 → `POST /api/v1/bao-cao/export`
- SO_KHUNG_THONG_BAO = 1 → chữ = "Đang tạo file..." (SRS SCR-IX-01 item 14, dòng 1054 — toast loading khi nhấn xuất)
- KHÔNG có toast "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04)

## Kết luận
Export Excel hoạt động đúng: server tạo file .xlsx và trả về auto-download (200 + attachment). Lỗi ERR-RPT-04 mà đối tác báo KHÔNG tái hiện trên env được giao → Reject.

## Evidence đối tác (đã xem full-res)
- Video: `partner-evidence/SLHDVM_06.webm` — frame `reverify-audit/SLHDVM_06/frames/t016.16s.jpg` bắt toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." trên env `htpldn-uat.ospgroup.vn`, login admin QTHT, báo cáo SLHDVM có data (Tổng 8).
- Ảnh web env mình: `SLHDVM_06-web-excel-dang-tao-file.png` (report có data 11, nút Xuất bật, không toast lỗi).
