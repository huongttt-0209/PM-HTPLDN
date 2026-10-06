# Bảng đối chiếu điều kiện — LDTBDDDR_06 (row 227) — Xuất Excel BC Lớp đào tạo đã diễn ra

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công.

> ⚠️ **Ảnh evidence đối tác gán nhầm:** cột "Ảnh/vieo 1" của row 227 dùng lại đúng file `CLDTBDDDR_06.jpg` (báo cáo "Lớp đào tạo ĐANG diễn ra"), không phải ảnh của báo cáo "Lớp đào tạo ĐÃ diễn ra". KQ thực tế đối tác ghi vẫn là "Không thể tạo file xuất" (ERR-RPT-04). QA verify đúng báo cáo LDTBDDDR (đã diễn ra).

| Điều kiện có thể đổi kết quả | Đối tác (KQ thực tế sheet + ảnh CLDTBDDDR_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) | `cbnv_tw_05` (CB Nghiệp vụ TW — vai trò chuẩn verdict). QTHT quyền rộng hơn | Không |
| Loại báo cáo | BC Lớp đào tạo đã diễn ra (theo mã TC + KQMĐ) | BC Lớp đào tạo đã diễn ra | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có dữ liệu thống kê (điều kiện case) | Có data — Tổng khóa học = 5, Tổng học viên = 11 | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (loaiBaoCao=BC_LOP_DAO_TAO_DA_DIEN_RA, formatXuat=XLSX) trả **200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-lop-dao-tao-da-dien-ra-2026-07-21.xlsx"` (body binary) — reqid=139.

**Lưu ý env:** đối tác `htpldn-uat.ospgroup.vn`; QA `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
