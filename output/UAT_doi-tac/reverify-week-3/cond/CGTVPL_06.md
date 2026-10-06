# Bảng đối chiếu điều kiện — CGTVPL_06 (row 230) — Xuất Excel BC Số lượng CG/TVV

**Kết luận:** Reject — lỗi đối tác báo (ERR-RPT-04 "Không thể tạo file xuất") KHÔNG tái hiện. Xuất Excel thành công (HTTP 200), nội dung file đúng.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res `partner-evidence/CGTVPL_06.jpg`) | Mình test (cbnv_tw, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT/admin) | cbnv_tw (CB Nghiệp vụ TW — đúng Tác nhân SRS; admin có quyền ⊇ cbnv_tw nên không thể là nguyên nhân fail export) | Không |
| Entity + trạng thái | Báo cáo CG/TVV đã "Xem báo cáo" ra dữ liệu (Tổng TVV 9) | Báo cáo CG/TVV đã "Xem báo cáo" ra dữ liệu (Tổng TVV 2) | Không |
| Dữ liệu tiền đề | Có CG/TVV đang hoạt động | Có CG/TVV đang hoạt động (2 TVV, 0 CG) | Không |
| Input / filter | loai=so-luong-cg-tvv, Kỳ Năm 2026 (01/01–31/12), Đơn vị Cục Bổ trợ tư pháp (BTP-TW, donViId ...001), Lĩnh vực CM=Thuế (...018) | Y HỆT (URL trùng: donViId ...001, fd_linhVucCm ...018) | Không |

**Artifact real-data:** `reverify-audit/_export-check-batch9/cgtvpl-export-success-toast.png` (toast "Tạo file thành công"), network `POST /api/v1/bao-cao/export` [200], file `cgtvpl_06.xlsx` (đủ 4/4 header TT17 + số liệu 2/0/2 khớp màn hình).
