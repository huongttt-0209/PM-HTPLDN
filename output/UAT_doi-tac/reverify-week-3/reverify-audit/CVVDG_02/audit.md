# Audit — CVVDG_02 (BA confirm)

**Chức năng:** Danh sách "Chọn vụ việc đánh giá" (FR-VI-05 / SCR-VI-01 Tab 3 item 41).
**Đối tác báo:** Thiếu cột Tên doanh nghiệp, Ngày hoàn thành, Cảnh báo trùng đợt.
**Verdict:** BA confirm — SRS mô tả chọn VV là C10 Multi-select, không prescribe danh sách cột.

## Điều kiện tái hiện
- Account `cbnv_hn` (CB_NV_DP Hà Nội), đợt DGHQ-B1 ở THUC_HIEN, Tab Thực hiện.

## Quan sát
- Bảng "Chọn vụ việc đánh giá" có 5 cột: **Mã vụ việc · Tên vụ việc · Lĩnh vực · Trạng thái · Đã chọn?**
- Thiếu đúng 3 cột đối tác nêu: Tên doanh nghiệp, Ngày hoàn thành, Cảnh báo trùng đợt.
- Khớp y hệt bản đối tác chụp (CVVDG_02.jpg cùng 5 cột).

## Đối chiếu SRS
- SCR item 41 (`srs-fr-08-danh-gia.md:872`): chọn VV = **C10 Multi-select**, filter HOAN_THANH/trong kỳ/đúng đơn vị. Không liệt kê cột.
- "Tên DN" là cột của **bảng chấm điểm** (item 42 `:873`) + **báo cáo** (item 47 `:883`), không phải bảng chọn VV.
- "Ngày hoàn thành" không có trong SCR như cột bắt buộc.
- "Cảnh báo trùng đợt": hành vi bắt buộc (AC 449) nhưng không quy định dạng cột → kiểm hành vi ở CVVDG_03.

## Kết luận
SRS silent về cột bảng chọn VV. Không đủ căn cứ khẳng định app SAI. → **BA confirm** để BA chốt bộ cột chuẩn cho danh sách chọn VV.

**Evidence:** `chon-vv-columns.png` (app, 5 cột) · `../../partner-evidence/CVVDG_02.jpg` (đối tác cùng 5 cột).
