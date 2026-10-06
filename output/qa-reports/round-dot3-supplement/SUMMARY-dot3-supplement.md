# Tổng hợp QA bổ sung — report-dot-3.xlsx
**Phạm vi phiên này:** Module 13 — Quản trị hệ thống, **cụm "Cấu hình hệ thống" (Cluster 1)**
**Account:** qtht_01 (QTHT) · **Tool:** Chrome DevTools MCP · **Chuẩn đối chiếu:** SRS v3.5 (input/srs-update-2026-5-5/)
**Ngày:** 2026-06-25

## Số liệu
- **Tổng case đã xử lý (chạy ra verdict):** 9
- **PASS mới:** 8 — TC-CH-SLA-001, TC-CH-SLA-003, TC-SLA-016, TC-CH-NL-001, TC-CH-NL-003, TC-CH-NL-004, TC-CH-NL-012, TC-CH-MPH-048
- **FAIL mới:** 1 — TC-CH-SLA-002
- **CHƯA CHẠY còn lại (module 13):** 635 (619 trống Lý do + 16 đã có Lý do)
- Cập nhật xlsx: sheet "13. Quản trị hệ thống" (9 dòng) + sheet "Tổng hợp" (PASS 353→361, FAIL 0→1).

## Danh sách FAIL theo module
**Module 13 — Quản trị hệ thống:**
- **TC-CH-SLA-002** — Giá trị seed SLA lệch SRS. API `/api/v1/cau-hinh/sla`: VU_VIEC thoiHanNgay=**15** (SRS srs-fr-10:2170 = **10**, NĐ55 Điều 9); HO_SO_CHI_TRA=**10** (SRS=**15**). HOI_DAP=5✓, HO_SO_HT=15✓, HO_SO_TT=10✓. → Dev/BA chốt + sửa seed theo SRS.

## Case block do thiếu data/account/env
- Không có trong cụm này (toàn bộ phần runnable đã chạy được với qtht_01; có self-seed: tạo/sửa/xóa ngày lễ).

## Case hạ tầng/tích hợp ngoài phát hiện thêm
- Không có trong cụm này (cụm Cấu hình HT không phụ thuộc cổng tích hợp ngoài).

## Phát hiện cấu trúc cần xử lý (KHÔNG đổi PASS/FAIL — chờ BA/PO)
1. **TC LỖI THỜI theo SRS — đề xuất RETIRE khỏi test plan:** SRS srs-fr-10:20 + 1728 (BA chốt 2026-05-07 "Hướng A") đã **bỏ Tab 4 "Quy trình hỗ trợ" + Tab 2 "Phân công"** khỏi màn Cấu hình (4→3 tab). App hiện 3 tab = ĐÚNG SRS; API quy trình config → 404 (đúng). Các TC tham chiếu 2 tab này: **TC-QT-001/003/004/007/008/010/013/015/019, TC-CH-QT-001, TC-PC-*** → test feature đã bỏ, không phải lỗi app. Để CHƯA CHẠY + ghi chú lỗi thời.
2. **Model NGAY_LE single-date vs SRS range:** App dùng 1 ngày đơn; SRS NGAY_LE có bat_dau+ket_thuc+lap_lai_hang_nam (range, lặp năm). Ngày lễ nhiều ngày (Tết) không cấu hình được dạng range → flag BA.
3. **UX nhỏ:** (a) cột "Hệ số quá hạn" hiển thị trên bảng SLA dù SRS §471/2165 ghi "không hiển thị UI"; (b) QTHT bị ẩn hẳn nút Thêm mẫu phản hồi thay vì disabled+tooltip "chỉ có quyền xem"; (c) field Thời hạn SLA nhận giá trị bất thường (1512) không chặn max.

## Ghi chú dữ liệu
- Đã khôi phục VU_VIEC SLA về 15 (giá trị as-found) sau khi test edit; ngày lễ test đã xóa mềm. Hệ thống để lại sạch.
