# Roadmap chạy nốt 58 testcase Hỏi đáp pháp lý

Nguồn: `report-dot-3.xlsx` sheet `03. Hỏi đáp pháp lý`, lọc `Kết quả = CHƯA CHẠY` và `Lý do` trống sau rerun 2026-06-26.

| Nhóm | Số TC | Cách xử triệt để |
|---|---:|---|
| F-Volume/concurrent fixture | 5 | Seed volume/batch fixture and controlled concurrent runner. |
| UI/data special | 4 | Stable UI session or cross-module seed (inactive field / TVN_BRIDGE). |
| F-Time fixture | 3 | Clock/mock-time or historical seed matching exact date condition. |
| UI/assignment modal | 18 | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| UI/response editor | 11 | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| Approval/publication data | 17 | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |

## F-Volume/concurrent fixture (5)

| TC | Tên TC | Cần chuẩn bị |
|---|---|---|
| TC-HD-105 | Export > 10,000 rows | Seed volume/batch fixture and controlled concurrent runner. |
| TC-HD-234 | Batch DELETE 100 records ALL conflict | Seed volume/batch fixture and controlled concurrent runner. |
| TC-DXL-207 | Lịch sử có ≥100 entries | Seed volume/batch fixture and controlled concurrent runner. |
| TC-PD-041 | Batch >100 records | Seed volume/batch fixture and controlled concurrent runner. |
| TC-PD-067 | Batch >100 với optimistic locking concurrent | Seed volume/batch fixture and controlled concurrent runner. |

## UI/data special (4)

| TC | Tên TC | Cần chuẩn bị |
|---|---|---|
| TC-HD-232 | Browser back sau khi Lưu drawer | Stable UI session or cross-module seed (inactive field / TVN_BRIDGE). |
| TC-HD-235 | Refresh button trong khi filter đang load (concurrent) | Stable UI session or cross-module seed (inactive field / TVN_BRIDGE). |
| TC-HD-HDTK-003 | Filter Kênh tiếp nhận = TVN_BRIDGE | Stable UI session or cross-module seed (inactive field / TVN_BRIDGE). |
| TC-HDTK-206 | Filter Lĩnh vực vô hiệu (URL bypass) | Stable UI session or cross-module seed (inactive field / TVN_BRIDGE). |

## F-Time fixture (3)

| TC | Tên TC | Cần chuẩn bị |
|---|---|---|
| TC-TN-201 | Tiếp nhận trước ngày lễ 30/4-1/5 | Clock/mock-time or historical seed matching exact date condition. |
| TC-TN-208 | Tiếp nhận lúc 23:59:59 cuối ngày → deadline tính từ ngày kế | Clock/mock-time or historical seed matching exact date condition. |
| TC-PD-032 | Bản ghi DA_DUYET 6 tháng không click "Đóng hồ sơ" → vẫn DA_DUYET | Clock/mock-time or historical seed matching exact date condition. |

## UI/assignment modal (18)

| TC | Tên TC | Cần chuẩn bị |
|---|---|---|
| TC-PC-102 | TC TV vô hiệu | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-104 | TVV không thuộc TC (UI bypass via API) | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-106 | Workload quá tải — cảnh báo không block | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-108 | HD chưa nhập lĩnh vực → modal cần fallback | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-200 | Bảng 4a có ≥15 TVV match → chỉ 10 đầu | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-201 | CB NV (không có linh_vuc_chuyen_mon) hiển thị bất kể lĩnh vực HD | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-202 | Không có TVV/NHT/CG khớp lĩnh vực | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-203 | TC-A có 0 TVV HOAT_DONG | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-204 | Override thoi_han khác SLA mặc định | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-205 | Bảng 4a chỉ TK cùng đơn vị | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-206 | Verify CC email tổ chức khi phân công TO_CHUC | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-207 | Đổi tab Cá nhân ↔ Tổ chức → reset radio | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-208 | TVV `to_chuc_chinh_id` inconsistent (data corruption edge) | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-209 | TVV vừa bị TAM_DUNG giữa lúc bảng 4a load | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-210 | Click radio nhiều lần liên tiếp trên bảng 4a | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-211 | HD chưa có deadline (NULL) khi mở modal | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-212 | Tab Tổ chức + chọn TC + Hủy modal → không có dirty state | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |
| TC-PC-213 | Composition test: lĩnh vực + đơn vị + workload + tiebreaker ho_ten | Stable UI session plus assignment seed: TVV/NHT/TC active/inactive/workload variants. |

## UI/response editor (11)

| TC | Tên TC | Cần chuẩn bị |
|---|---|---|
| TC-PH-201 | 2 user cùng nguoi_phan_cong (hiếm) sửa đồng thời → conflict | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-202 | Upload 5 file pdf phản hồi | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-203 | DA_TRA_LOI thoáng qua — user không thấy state này | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-205 | Mẫu KICH_HOAT=VO_HIEU_HOA không xuất hiện dropdown | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-206 | Session expired giữa lúc soạn → auto-save draft localStorage | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-207 | User bị admin revoke quyền giữa chừng (HTTP 403) | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-208 | Auto-save trigger trong khi user đang gõ | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-209 | Switch tab browser → quay lại sau 5 phút | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-210 | Chèn mẫu khi editor đã có content → overwrite hay append? | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-211 | Tích "Đã trả lời" rồi UNCheck → modal F-18? | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |
| TC-PH-212 | Reload SCR-II-02 trong khi đang upload file | Stable UI session plus DANG_XU_LY assigned record; verify editor/upload/autosave/template. |

## Approval/publication data (17)

| TC | Tên TC | Cần chuẩn bị |
|---|---|---|
| TC-PD-100 | CB PD khác cấp attempt phê duyệt | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-HD-PD-024 | 2 user concurrent Công khai vs Hủy CK trên cùng record | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-HD-PD-025 | mo_ta_cong_khai paste `<script> | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-033 | CB PD khác cấp attempt đóng hồ sơ | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-040 | Phê duyệt batch 5 records OK | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-042 | Batch partial fail (mix lỗi) | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-043 | Concurrent edit version mismatch trong batch | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-050 | Công khai batch 3 records DA_DUYET cùng cấp | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-051 | Tick records nhiều cấp khác nhau | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-052 | Batch CK với 1 record API fail | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-060 | Tab Hoàn thành hiển thị danh sách read-only + chi tiết timeline | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-066 | Bản ghi HUY hiển thị banner thay stepper | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-068 | CB PD review HD có draft chưa gửi (ngay_tra_loi NULL) | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-070 | Đóng hồ sơ rồi không undo được | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-071 | Batch CK records mix DA_DUYET + state khác (auto-skip) | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-072 | Modal Công khai upload ảnh > 5MB → reject | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
| TC-PD-076 | CB_PD_BN từ Bộ A approve record của Bộ B (cùng cap=BN) → PASS | Seed CHO_PHE_DUYET/DA_DUYET/CONG_KHAI records with approved response and correct unit/cap. |
