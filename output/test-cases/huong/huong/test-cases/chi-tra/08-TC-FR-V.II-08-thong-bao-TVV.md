# TC — FR-V.II-08: TVV Nhận Thông Báo Kết Quả Thanh Toán

> **UC ref**: UC75 | **Screen**: Trang DS Thông báo TVV | **SRS**: srs-fr-06:509-549
> **Roles**: TVV
> **Mục tiêu**: Verify TVV truy cập DS TB KQ thanh toán + xem chi tiết + tải file đính kèm (QĐ phê duyệt, biên nhận) + scope đúng (TVV chỉ thấy TB của HS gắn với mình).

## Preconditions

- HS X DA_THANH_TOAN gắn với `tvv_01`, đã sinh THONG_BAO khi UC79 phê duyệt và UC80 cập nhật TT
- Login `tvv_01`
- HS Y gắn với `tvv_02` (để verify scope negative)

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-TB-001 | login `tvv_01`, có TB KQ thanh toán cho HS X | 1. Vào trang Thông báo (TVV) | DS hiển thị TB KQ thanh toán, sắp xếp mới nhất trước (ngay_gui DESC). Phân trang 20/trang. Cột: Tiêu đề, Ngày gửi, Đã đọc | AC#1, BR-DATA-07, srs-fr-06:530-543 | P0 |
| TC-CT-TB-002 | TB chưa đọc cho HS X | 1. Click TB X | Mở chi tiết: Nội dung KQ + file đính kèm (QĐ phê duyệt + biên nhận). Đánh dấu `da_doc=true`. Có nút "Tải file đính kèm" | AC#2, srs-fr-06:547 | P0 |
| TC-CT-TB-003 | TB X đã đọc | 1. Click "Tải file đính kèm" QĐ phê duyệt | File QĐ download thành công (PDF). Header content-disposition đúng | srs-fr-06:540-542 | P1 |
| TC-CT-TB-004 | login `tvv_02`, HS X gắn `tvv_01` | 1. Vào trang Thông báo | DS KHÔNG chứa TB của HS X. Chỉ thấy TB của HS gắn `tvv_02` (scope theo TVV) | BR-AUTH-08 (TVV scope) | P0 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-TB-005 | login `tvv_03` (BNI) — không có HS gắn TVV này | 1. Vào trang Thông báo | DS empty với INF-TB "Bạn chưa có thông báo nào" hoặc placeholder. KHÔNG crash | AC#1 (empty state) | P1 |
| TC-CT-TB-006 | login `tvv_01`, > 100 TB | 1. Vào trang Thông báo 2. Scroll/Pagination | Pagination 20/trang. Total count đúng. Sort newest first | BR-DATA-07 | P1 |

## Tổng số TC: 6 (sau A4: +2 edge)

**P0: 3** | P1: 3

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-08)
