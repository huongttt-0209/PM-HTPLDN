# Audit — CVVDG_01 (BA confirm)

**Chức năng:** Chọn vụ việc đánh giá (FR-VI-05, UC87) — Tab Thực hiện.
**Đối tác báo:** Thông báo "Đã lưu {N} vụ việc" không giống thiết kế.
**Verdict:** BA confirm — lệch wording toast, SRS không quy định chuỗi cụ thể.

## Điều kiện tái hiện
- Account: `cbnv_hn` (CB_NV_DP, Sở Tư pháp Hà Nội) — CB NV + trưởng nhóm được phân công.
- Đợt: DGHQ-B1-20260720 (mã DG-20260720-0001), trạng thái THUC_HIEN.
- VV: EEE-VH-014 (HOAN_THANH, lĩnh vực Thương mại).

## Quan sát
1. Tab Thực hiện → section "Chọn vụ việc đánh giá" → tích EEE-VH-014 → nút "Xác nhận chọn".
2. Modal confirm "Xác nhận chọn vụ việc? Bạn sẽ chọn 1 vụ việc để đánh giá." → bấm "Xác nhận".
3. `POST /api/v1/ke-hoach-danh-gias/{id}/vu-viec-select` [200]. 1 request / 1 toast (không double).
4. Toast hiện: **"Đã chọn vụ việc đánh giá"** (bắt qua MutationObserver, innerText).
5. Đối tác kỳ vọng (theo thiết kế): **"Đã lưu {N} vụ việc"**.

## Đối chiếu SRS
- FR-VI-05 (`srs-fr-08-danh-gia.md:384-451`): bước 6 = "Lưu danh sách VV đánh giá" (mô tả xử lý). Không có chuỗi toast prescribe trong Outputs / Error Handling.
- Không nguồn SRS nào ép text "Đã lưu {N} vụ việc" → kỳ vọng đối tác là design-doc, SRS silent.

## Kết luận
Nghiệp vụ chạy đúng (lưu VV thành công). Chỉ lệch wording toast so với bản thiết kế; SRS không quy định. → **BA confirm** để BA chốt wording chuẩn.

**Evidence:** `toast-chon-vv.png` (app hiện "Đã chọn vụ việc đánh giá"), `../../partner-evidence/CVVDG_01.jpg` (bản đối tác cùng toast).
