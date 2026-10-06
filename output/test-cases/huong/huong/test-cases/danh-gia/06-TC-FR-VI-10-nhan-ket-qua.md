# TC FR-VI-10 — Nhận kết quả đánh giá (read-only) — `[GAP-VI-04][CR-10][Q-06]`

> **SRS:** [`srs-fr-08-danh-gia.-v3.1.md`](../../../input/srs-v3/srs-fr-08-danh-gia.-v3.1.md) §FR-VI-10 (line 741-778)
> **SCR:** SCR-VI-01 — Tab 4 Báo cáo (chế độ read-only)
> **Actor:** CB NV thuộc `co_quan_duoc_danh_gia_id` (KHÔNG phải `don_vi_id` của user lập đợt)
> **Entity:** KE_HOACH_DANH_GIA + BAO_CAO_DANH_GIA (read-only)
> **BR core:** BR-AUTH-01 + BR-AUTH-08 (custom check theo `co_quan_duoc_danh_gia_id`)
> **Total TC:** 6

---

## Test Cases

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-NK-001 | CB NV thuộc cơ quan được ĐG xem KQ — happy path | Login `cb_nv_bn_01` (BKH). Đợt HOAN_THANH với `don_vi_id`=TW + `co_quan_duoc_danh_gia_id`=BKH. | 1. Mở danh sách đợt<br>2. Click mã đợt | Hiển thị chi tiết đợt 4 tabs read-only. Tab Báo cáo show toàn bộ thông tin BC | Critical | UC FR-VI-10 happy, AC-1 |
| TC-DG-NK-002 | Read-only mode — KHÔNG có button CRUD | Login. Đợt HOAN_THANH `co_quan_duoc_danh_gia_id`=user. | 1. Mở từng tab | Tất cả input disabled. Nút [+ Thêm], [Sửa], [Xóa], [Hủy đợt], [Trình duyệt], [Phê duyệt] đều ẩn | High | UC FR-VI-10 read-only mode |
| TC-DG-NK-003 | CB NV thuộc đơn vị khác → 403 | Login `cb_nv_dp_01` (AG). Đợt HOAN_THANH `co_quan_duoc_danh_gia_id`=BKH. | 1. Truy cập trực tiếp URL `/danh-gia/ke-hoach/{id}/chi-tiet` | 403 + ERR-DG-10 "Bạn không có quyền xem kết quả đánh giá này" | Critical | ERR-DG-10, AC-2 (cơ quan khác → từ chối) |
| TC-DG-NK-004 | KH chưa HOAN_THANH → ERR-DG-11 | Login `cb_nv_bn_01`. Đợt CHO_PHE_DUYET, `co_quan_duoc_danh_gia_id`=BKH. | 1. Truy cập URL chi tiết | Block + ERR-DG-11 "Kết quả đánh giá chưa hoàn thành" | High | ERR-DG-11 |
| TC-DG-NK-005 | Xuất XLSX/DOCX — chế độ read (P1 F-018) | Login. Đợt HOAN_THANH user thuộc cơ quan ĐG. | 1. Mở Tab Báo cáo<br>2. Click [Xuất XLSX] | Tải file XLSX. Nội dung 13 cột TT17 đầy đủ + read-only metadata. KHÔNG yêu cầu watermark "Bản nhận từ cơ quan đánh giá" (không có trong SRS) | Medium | FR-VI-10 Outputs |
| TC-DG-NK-006 | Tab Phân công + Thực hiện — toàn bộ thông tin read-only (P1 F-017) | Login. | 1. Mở Tab Phân công<br>2. Mở Tab Thực hiện | Per FR-VI-10 Outputs "Toàn bộ thông tin KH đánh giá + báo cáo kết quả, chế độ read-only": Tab Phân công hiển thị toàn bộ DS người ĐG (read-only). Tab Thực hiện hiển thị toàn bộ bảng điểm + chi_tiet_diem từng người ĐG (read-only) | Medium | FR-VI-10 Outputs (toàn bộ thông tin) |

---

## Edge bổ sung (A4 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-NK-007 | Đợt HUY → user thuộc cơ quan ĐG xem được? | Login `cb_nv_bn_01`. Đợt HUY `co_quan_duoc_danh_gia_id`=BKH. | 1. Truy cập URL chi tiết | ERR-DG-11 (KH chưa HOAN_THANH) — đợt HUY KHÔNG show | High | ERR-DG-11 (HUY != HOAN_THANH) |
| TC-DG-NK-008 | Search trong list — đợt user nhận KQ + đợt user lập | Login `cb_nv_bn_01`. user là cơ quan được ĐG đợt A (HOAN_THANH) + user lập đợt B (LAP_KE_HOACH). | 1. Mở list | Cả A + B đều hiển thị (2 vai trò khác nhau). Đợt A read-only, B full edit | Medium | BR-AUTH-08 + FR-VI-10 |

## Tổng số TC: 8 (6 base + 2 edge A4)

> **A4 done 2026-05-10** — 2 TC mới merge inline.
> **A6 placeholder — Fill GAP-A5.**
> **A7 placeholder — LOẠI/SỬA log.**
> **SPEC-CLARIFY-DG-01:** ~~Mức độ chi tiết hiển thị (chi_tiet_diem JSON từng người ĐG hay chỉ KQ tổng hợp) cho FR-VI-10 read-only — pending BA xác định privacy boundary.~~ **RESOLVED 2026-05-10 (Codex F-017):** Per FR-VI-10 Outputs "Toàn bộ thông tin KH đánh giá + báo cáo kết quả, chế độ read-only" → hiển thị TOÀN BỘ thông tin (bao gồm chi_tiet_diem). Áp dụng feedback memory `business_spec_priority` (mâu thuẫn UI vs business → theo business).
