# INDEX Verify Bug — 2026-06-02

**Nguồn:** [`Danh-sach-Bug-PM-HTPLDN-verify-2026-06-01.csv`](./Danh-sach-Bug-PM-HTPLDN-verify-2026-06-01.csv) (giữ làm source of truth)

**Tổng bug cần verify:** 92 | **Đã verify:** 92 | **Còn lại:** 0 — ✅ HOÀN TẤT

> **Re-test R-verify-2 (2026-06-05):** 4 bug Open re-test sau dev fix → STT 35 + 79 + 49 **Closed** (file đổi `Pass-`; STT 49 đóng 13:53 sau API re-check — file persist `entityType=CHUONG_TRINH_HTPL`, sync tài liệu SRS theo dõi tại SRS-C-006) · STT 63 còn lỗi (CG menu 403 dead-end).

## Tiến độ theo module

| Module | File | Tổng bug | Đã verify | Còn lại | Trạng thái |
|---|---|---:|---:|---:|:-:|
| bao-cao | [by-module/bao-cao.csv](./by-module/bao-cao.csv) | 26 | 26 | 0 | ✅ Xong (26/26 PASS — 15 false-block lật) |
| dao-tao | [by-module/dao-tao.csv](./by-module/dao-tao.csv) | 17 | 17 | 0 | ✅ Xong (17/17 PASS — STT22 chốt PASS theo bug gốc, đề xuất BA align SRS mo_ta Y→N) |
| vu-viec | [by-module/vu-viec.csv](./by-module/vu-viec.csv) | 8 | 8 | 0 | ✅ Xong (8/8 PASS) |
| danh-gia | [by-module/danh-gia.csv](./by-module/danh-gia.csv) | 6 | 6 | 0 | ✅ Xong (6/6 PASS — STT45 xếp loại lật) |
| doanh-nghiep | [by-module/doanh-nghiep.csv](./by-module/doanh-nghiep.csv) | 5 | 5 | 0 | ✅ Xong (5/5 PASS — STT30 test đúng role CB_PD) |
| chi-tra | [by-module/chi-tra.csv](./by-module/chi-tra.csv) | 4 | 4 | 0 | ✅ Xong (4/4 PASS — STT35 Closed 06-05, contrast 21:1) |
| ct-htpldn | [by-module/ct-htpldn.csv](./by-module/ct-htpldn.csv) | 4 | 4 | 0 | ✅ Xong (4/4 PASS — STT49 Closed 06-05, file persist; SRS sync → SRS-C-006) |
| qtht-cau-hinh-ht | [by-module/qtht-cau-hinh-ht.csv](./by-module/qtht-cau-hinh-ht.csv) | 4 | 4 | 0 | ✅ Xong (4/4 PASS) |
| hoi-dap | [by-module/hoi-dap.csv](./by-module/hoi-dap.csv) | 3 | 3 | 0 | ✅ Xong (3/3 PASS) |
| qtht-tai-khoan | [by-module/qtht-tai-khoan.csv](./by-module/qtht-tai-khoan.csv) | 3 | 3 | 0 | ✅ Xong (3/3 PASS — STT79 Closed 06-05, PUT 200) |
| qtht-vai-tro | [by-module/qtht-vai-tro.csv](./by-module/qtht-vai-tro.csv) | 3 | 3 | 0 | ✅ Xong (3/3 PASS — STT77 override 1c) |
| tu-van-chuyen-sau | [by-module/tu-van-chuyen-sau.csv](./by-module/tu-van-chuyen-sau.csv) | 3 | 3 | 0 | ❌ Xong (2 PASS · STT63 còn lỗi sau re-test 06-05 — CG menu 403 dead-end) |
| bm | [by-module/bm.csv](./by-module/bm.csv) | 2 | 2 | 0 | ✅ Xong (2/2 PASS) |
| qtht-danh-muc | [by-module/qtht-danh-muc.csv](./by-module/qtht-danh-muc.csv) | 2 | 2 | 0 | ✅ Xong (2/2 PASS — STT69 lật false-positive, SRS ko yêu cầu sortable) |
| qtht-nhat-ky | [by-module/qtht-nhat-ky.csv](./by-module/qtht-nhat-ky.csv) | 1 | 1 | 0 | ✅ Xong (1/1 PASS) |
| tu-van-vien-cg | [by-module/tu-van-vien-cg.csv](./by-module/tu-van-vien-cg.csv) | 1 | 1 | 0 | ✅ Xong (1/1 PASS) |
| **Tổng** | | **92** | **92** | **0** | |

## Cách dùng INDEX

1. Agent đọc file này → pick module đầu tiên có `Còn lại > 0`.
2. Mở `by-module/<module>.csv` → verify TỪNG bug (kể cả status PASS — verify lại để xác nhận).
3. Sau MỖI bug xong → update INDEX hàng module đó: `Đã verify +1`, `Còn lại -1`.
4. Sau khi module xong (Còn lại = 0) → đổi `Trạng thái` → `✅ Xong` | `⚠️ Còn chờ BA` | `🚫 Còn BLOCKED-D`.
5. Sang module kế tiếp.

## Convention

- File con CSV giữ schema gốc (6 cột) — agent update cột `Trạng thái` + `Ghi chú verify` per-bug.
- CSV gốc giữ nguyên làm reference.
- Evidence: `evidence/<module>/bug-<STT>-<slug>.png`.
- Báo cáo tổng: `verify-report-2026-06-02.md` (append per-bug từ bug đầu tiên).
