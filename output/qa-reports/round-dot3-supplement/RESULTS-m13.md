# QA bổ sung — report-dot-3.xlsx — Module 13 (Quản trị hệ thống)
Account: qtht_01 (QTHT) · Tool: Chrome DevTools MCP · App: http://103.172.236.130:3000

| ID | row | Verdict | Evidence / Note |
|---|---|---|---|
| TC-CH-SLA-001 | 441 | PASS | Màn Cấu hình SLA render OK, BE `GET /api/v1/cau-hinh/sla` 200, bảng 6 dòng seed, đủ cột (Loại YC, Tên loại, Thời hạn, Vùng cảnh báo, Hệ số quá hạn, Email, TB app, Hành động), pagination 1-6/6, nút Sửa/row. Note BA: hiển thị cột "Hệ số quá hạn"(=2) dù SRS §471/2165 ghi "không hiển thị UI"; 6 dòng vs tài liệu cũ ghi 4 (đã thêm HOI_DAP_PHUC_TAP, HO_SO_CHI_TRA). |
| TC-CH-SLA-002 | 442 | FAIL | Giá trị seed lệch SRS: VU_VIEC thoi_han=15 (SRS §2170 NĐ55 Đ9 = 10); HO_SO_CHI_TRA=10 (SRS=15). HOI_DAP=5✓, HO_SO_HT=15✓, HO_SO_TT=10✓. Evidence: API payload + srs-fr-10:2170. CAVEAT: dữ liệu config user-editable → có thể lệch do chỉnh tay trước đó; cần BA chốt VU_VIEC=10/15. |
| TC-CH-SLA-003 | 443 | PASS | Sửa Thời hạn VU_VIEC → 12: toast "Cập nhật cấu hình SLA thành công", API GET lại trả thoiHanNgay=12, version 5→6, ngayCapNhat mới → edit + persist OK. Phát hiện phụ: field Thời hạn nhận giá trị bất thường (1512) không chặn max → note dev (SRS không nêu max nên chưa kết luận bug). |
| TC-SLA-016 | 299 | PASS | POST trùng loai_yeu_cau=VU_VIEC → HTTP 409, record KHÔNG tạo, message "Cấu hình SLA cho loại yêu cầu 'VU_VIEC' đã tồn tại". Rule chống trùng (SRS §511) enforced. Note BA: mã lỗi thực tế ERR-VAL-VIII-108-01 (SRS ghi ERR-SLA-03) — lệch tên mã, hành vi đúng. |

## Phát hiện cấu trúc quan trọng (ảnh hưởng nhiều TC Cluster 1)
- Màn `/quan-tri/cau-hinh` (Cấu hình hệ thống) thực tế CHỈ có 3 tab: **Thời hạn xử lý (SLA)**, **Mẫu phản hồi**, **Quản lý ngày lễ**.
- Nhiều TC tham chiếu **"Tab 2 (Phân công)"**, **"Tab 4 (Quy trình hỗ trợ)"** (TC-QT-*, TC-PC-*), cấu hình **Hồ sơ đề nghị / Hồ sơ thanh toán** (TC-HSDN/HSTT) → các tab/màn này KHÔNG có ở đây. Cần xác định: chưa build / nằm màn khác / bỏ khỏi spec. → các TC này tạm chưa kết luận PASS/FAIL, cần điều tra thêm.
| TC-CH-NL-001 | 527 | PASS | Thêm ngày lễ 15/08/2026 "Lễ test QA dot3": toast "Thêm ngày lễ thành công", POST /api/v1/ngay-le, GET reload thấy record (persist qua F5). FE calendar input OK (BUG-NGAY-LE-001 không tái hiện). Note: model dùng 1 ngày đơn (single date). |
| TC-CH-NL-003 | 529 | PASS | Sửa tên ngày lễ → "...- SUA": modal load giá trị cũ đúng, PATCH /ngay-le/{id} 200, toast "Cập nhật ngày lễ thành công", API xác nhận tên mới. Note: modal Sửa KHÔNG cho đổi Ngày (chỉ tên/loại/ghi chú). |
| TC-CH-NL-004 | 530 | PASS | Xóa mềm: Popconfirm "Bạn có chắc...", DELETE /ngay-le/{id} 204, toast "Xóa ngày lễ thành công", row biến mất, GET reload count 9→8 (không hiện). |
| TC-CH-NL-012 | 535 | PASS | Thêm trùng ngày 01/01/2026 (đã có "Tết Dương lịch") → POST 409 "Ngày lễ với ngày này đã tồn tại trong năm", không tạo. Rule chống trùng enforced. Note SRS: model single-date (SRS NGAY_LE có bat_dau+ket_thuc+lap_lai_hang_nam = range) → lệch model, flag BA. |
| TC-CH-MPH-048 | 502 | PASS | QTHT KHÔNG tạo được mẫu phản hồi: UI ẩn nút Thêm (chỉ Làm mới/Tìm kiếm/Xóa lọc), API POST /mau-phan-hois → 403 ERR-PERM-SYS-00-01. Quyền view-only enforced 2 lớp. Note UX: ẩn nút thay vì disabled+tooltip "chỉ có quyền xem" như TC kỳ vọng. |

## Phát hiện cấu trúc #2 — TC lỗi thời theo SRS (BA chốt 2026-05-07 "Hướng A")
- SRS srs-fr-10:20 + 1728: **ĐÃ BỎ Tab 4 "Quy trình hỗ trợ"** + **Tab 2 "Phân công mặc định"** khỏi màn Cấu hình (4→3 tab). Entity CAU_HINH_QUY_TRINH + CAU_HINH_PHAN_CONG bỏ.
- App hiện 3 tab (SLA / Mẫu phản hồi / Quản lý ngày lễ) = **ĐÚNG SRS**. API quy trình config → 404 (đúng, đã bỏ).
- ⇒ Các TC trong report tham chiếu 2 tab này (TC-QT-*, TC-CH-QT-*, TC-PC-*) là **TC LỖI THỜI** — test feature đã bị bỏ. KHÔNG phải lỗi app. Đề xuất: retire khỏi test plan, KHÔNG đổi PASS/FAIL (giữ CHƯA CHẠY, ghi chú lỗi thời).

## Batch 2 — SLA validation + Ngày lễ validation (2026-06-25, qtht_01, BE API verify)
| ID | row | Verdict | Evidence |
|---|---|---|---|
| TC-CH-SLA-010 | 429 | PASS | PATCH thoiHanNgay=0 → 422 "Thời hạn xử lý phải là số nguyên dương" (reject) |
| TC-CH-SLA-011 | 430 | PASS | PATCH thoiHanNgay=-1 → 422 same (reject) |
| TC-CH-SLA-012 | 431 | PASS | PATCH CB1=80,CB2=70 → 422 "Ngưỡng cảnh báo 2 phải lớn hơn ngưỡng cảnh báo 1" |
| TC-CH-SLA-013 | 432 | PASS | PATCH CB1=CB2=50 → 422 same (CB1<CB2 enforced, ERR-SLA-02) |
| TC-CH-SLA-014 | 433 | FAIL | PATCH CB2=100 → **200 (chấp nhận)**. SRS srs-fr-10:469/481/1752 = CB1<CB2<**100** (default 90). App nhận CB2=100 + seed mặc định CB2=100 (sai default 90). Note: SRS ERD :2164 mâu thuẫn (CHECK 0..100) → cần BA chốt + sửa validation/seed. |
| TC-CH-SLA-015 | 434 | PASS | PATCH thoiHanNgay="abc" → 422 (type reject) |
| TC-CH-SLA-041 | 442 | PASS | PATCH thoiHanNgay=999 → 200 (giá trị lớn hợp lệ; note: chưa có chặn max) |
| TC-CH-SLA-042 | 443 | PASS | PATCH thoiHanNgay=1 → 200 (min hợp lệ) |
| TC-CH-NL-006 | 497 | PASS | Ghi chú (mo_ta) lưu + hiển thị — xác nhận qua NL-001 (record có ghiChu hiện trong bảng) |
| TC-CH-NL-013 | 499 | PASS | POST tenNgayLe="" → 422 "tenNgayLe should not be empty" |
| TC-CH-NL-014 | 500 | PASS | POST ngay="" → 422 "ngay should not be empty" |

> Lưu ý: VU_VIEC SLA đã restore về 15 sau các probe validation. Không để lại side-effect.

## Đã XÓA 37 TC lỗi thời khỏi report-dot-3.xlsx (theo yêu cầu user 2026-06-25)
- 33 TC Tab Quy trình/Phân công (đã bỏ theo SRS BA 2026-05-07): TC-PC-017/018, TC-QT-001→019, TC-CH-QT-001/002/003/004/010/011/020/021/022/030/031/032.
- 4 TC NGAY_LE range-model (app single-date): TC-CH-NL-002/005/010/011.
- GIỮ: TC-CH-NL-012 (PASS), TC-CH-NL-014 (PASS — "Ngày" trống vẫn test được).
- Module 13 total: 997 → 960. Grand total: 4675 → 4638.

## Batch 3
| ID | row | Verdict | Evidence |
|---|---|---|---|
| TC-CH-SLA-004 | 423 | PASS | PATCH HOI_DAP CB1=40+CB2=85 đồng thời → 200, persist (cb1=40,cb2=85), đã restore 50/100 |
| TC-CH-SLA-006 | 425 | FAIL | qua_han_he_so HIỂN THỊ trong UI (cột "Hệ số quá hạn"=2 + spinbutton sửa được trong modal) → vi phạm SRS srs-fr-10:471/2165 "không hiển thị UI, dùng nội bộ" (BA chốt 2026-05-07 Q5). |
| TC-CH-NL-030 | 507 | PASS | Click [Lịch] → calendar view render (84 ô lịch). Toggle OK. |

## Tổng kết phiên (cụm Cấu hình hệ thống)
- **Đã chạy: 23 TC** → **PASS 20, FAIL 3** (SLA-002 seed lệch SRS · SLA-014 CB2=100 lọt validation · SLA-006 hiện qua_han_he_so trên UI).
- **Đã xóa 37 TC lỗi thời.**
- Module 13 hiện: PASS 373 / FAIL 3 / CHƯA CHẠY 584 / total 960.

## Batch 4 — Role-switch (CB_NV_TW) — UI-driven
| ID | row | Verdict | Evidence |
|---|---|---|---|
| TC-CH-MPH-010 | 456 | PASS | CB_NV_TW (cb_nv_tw_01) thấy 15 mẫu đủ 3 phạm vi: Trung ương (Cục BTTP), Bộ ngành (Bộ KH&ĐT/Công Thương/Tài chính), Địa phương (Sở TP An Giang/Bắc Ninh/Bắc Giang). Nút Sửa/Xóa CHỈ hiện trên mẫu TW của mình; mẫu BN/DP chỉ có "eye" (view) → cross-scope edit chặn đúng ở UI. |

## ⚠️ Rào cản môi trường — token rotation (ảnh hưởng cách test role-switch)
App dùng **refresh-token rotation + reuse-detection**: khi injected `fetch` (qua evaluate_script) chạy đồng thời với auto-refresh của app → bị "Token đã bị thu hồi" (ERR-AUTH-SYS-00-03) → **revoke cả token family → app văng ra /login**. Với QTHT session ổn định lâu thì injected fetch may mắn chạy được; với role mới (logout→login) thì chết ngay.
**⇒ Cách test role-switch ĐÚNG cho phiên sau:** KHÔNG dùng injected fetch. Verify READ qua đọc response request của chính app (`list_network_requests` + `get_network_request`) hoặc đọc DOM bảng; verify WRITE qua form UI (app tự gửi token hợp lệ). Mỗi lần đổi role = logout (chỉ `localStorage.clear()` + navigate /login) + login OTP 666666.

## Trạng thái role-switch (64 TC MPH+PERM)
- Đã verify: TC-CH-MPH-010 (PASS). Quan sát hỗ trợ: cross-scope edit chặn đúng (nền cho MPH-020/035-038).
- Còn lại 63 TC: ver/được nhưng phải UI-only (token rotation cấm API batch) → khối lượng lớn, nên tách phiên riêng để không tràn context.

## Batch 4 (tiếp) — Chẩn đoán môi trường role-switch (QUAN TRỌNG cho phiên sau)
- **`cb_nv_tw_01` session CHẾT trong ~15-60s** sau login (revoke token), thử 5 lần / nhiều cách (API, sidebar click, navigate). Nguyên nhân khả dĩ nhất: **single-active-session eviction — account `_01` đang bị dùng ở nơi khác** (tester khác / process nền) → ping-pong revoke.
- **`cb_nv_tw_02` session ỔN ĐỊNH** (sống >1 phút, qua được nhiều thao tác). ⇒ **Phiên sau chạy role-batch DÙNG account `_02` (hoặc sibling chưa ai dùng), KHÔNG dùng `_01`.**
- Tương tác form AntD (Select 2 cấp) qua DOM events KHÔNG ổn (đóng modal). ⇒ Dùng MCP UI tools (take_snapshot + click) cho Select; hoặc chỉ verify các case READ (đọc lưới/flag canUpdate/canDelete) cho nhanh.
- TUYỆT ĐỐI KHÔNG dùng injected `fetch` (evaluate_script gọi API) trên session role-switch → kích reuse-detection → revoke cả family.

## Trạng thái role-batch (kết phiên này)
- Verify xong: **TC-CH-MPH-010 PASS** (CB_NV_TW thấy đủ 3 phạm vi; nút Sửa/Xóa chỉ trên mẫu TW của mình).
- 63 TC MPH+PERM còn lại: chưa chạy — cần phiên riêng với account `_02` ổn định + MCP UI tools (đã ghi method ở trên). Để CHƯA CHẠY (KHÔNG mark sai).
