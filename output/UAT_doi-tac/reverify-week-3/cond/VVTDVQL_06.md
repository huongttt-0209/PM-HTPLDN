# Bảng đối chiếu điều kiện — VVTDVQL_06 (row 239) — Xuất Excel BC Vụ việc theo đơn vị quản lý

**Kết luận:** Reject — ERR-RPT-04 "Không thể tạo file xuất" KHÔNG tái hiện. Xuất Excel thành công (HTTP 200), nội dung file đúng (4/4 header + 4 đơn vị khớp màn hình).

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/VVTDVQL_06.jpg`) | Mình test (cbnv_tw, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT/admin) | cbnv_tw (CB Nghiệp vụ TW — đúng Tác nhân SRS; admin quyền ⊇) | Không |
| Entity + trạng thái | BC Vụ việc theo đơn vị quản lý đã "Xem báo cáo" ra data | BC Vụ việc theo đơn vị quản lý đã "Xem báo cáo" ra data (4 đơn vị) | Không |
| Dữ liệu tiền đề | Có vụ việc phân theo đơn vị quản lý | Có vụ việc: BKHĐT 4, Cục BTTP 8, An Giang 3, Hà Nội 2 (theo state) | Không |
| Input / filter | loai=vu-viec-theo-don-vi, Kỳ Năm 2026, ĐV Toàn quốc | loai=vu-viec-theo-don-vi, Kỳ Năm 2026, ĐV Toàn quốc, filterDacThu rỗng | Không |

**Artifact real-data:** `reverify-audit/_export-check-batch9/vvtdvql-excel-success-toast.png` (report có data), network `POST /api/v1/bao-cao/export` [200] `content-disposition: ...vu-viec-theo-don-vi-2026-07-21.xlsx`, file `vvtdvql_06.xlsx` (đủ 4/4 header: `BC Vụ việc theo đơn vị quản lý` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 21/07/2026` + 4 dòng đơn vị khớp màn hình: 0/0/2/2/4, 1/2/2/2/8, 0/1/1/0/3, 0/0/1/1/2).
