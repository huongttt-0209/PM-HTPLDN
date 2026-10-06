# Functional Test Report — Hỏi đáp pháp lý (FR-02) — rerun report-dot-3

**Verdict tổng (batch 1 + batch 2 + UI partial + API unblock + UI upload/empty-state):** Đã xử lý **99 / 163** testcase CHƯA CHẠY → **84 PASS · 15 FAIL**. Đánh dấu **6** case infra = "Chưa tích hợp". Còn **58** case runnable CHƯA CHẠY (cần UI-session / data đặc thù / cross-cấp / infra — xem Bảng 2).
**Ngày:** 2026-06-25 · **Tool:** Chrome DevTools MCP/CDP + injected fetch (Bearer token, login lập trình OTP 666666)
**Accounts:** `cb_nv_tw_01` (CB_NV_TW) · `cb_pd_tw_01` (CB_PD_TW) · `cb_nv_dp_01` (CB_NV_DP/AG) · `cb_nv_dp_02` (BG) · `9999999990` (DN) — pass `Secret@123`.
**Nguồn:** `report-dot-3.xlsx` sheet "03. Hỏi đáp pháp lý" (snapshot per-TC đầy đủ) · `srs-fr-02-hoi-dap.md` v3.5

> **Module 03 sau rerun:** 259 PASS · 15 FAIL · 84 CHƯA CHẠY (58 runnable còn lại + 26 "Chưa tích hợp"). PASS tăng 175 → 259.

> **Ghi chú kỹ thuật quan trọng (phát hiện trong rerun):**
> - Endpoint thật: list `GET /api/v1/hoi-daps` (số nhiều); workflow `POST /hoi-daps/{id}/{tiep-nhan|phan-cong|gui-duyet|phe-duyet|tu-choi|cong-khai|huy-cong-khai|dong-ho-so|huy|cap-nhat-thoi-han}`; phản hồi `POST /hoi-daps/{id}/phan-hois`; batch xóa = FE per-record DELETE.
> - Auth: access-token cookie ngắn hạn + interceptor **logout khi gặp 401**; token revoke nhanh → mỗi burst login lập trình + làm trọn trong 1 lần. Bearer token (`accessToken`) hợp lệ 30 ngày nhưng bị revoke khi login lại.
> - Optimistic locking (`version`) áp dụng cho mọi mutation; sai version → 409 ERR-STATE-LOCK-409.

---

## Bảng trạng thái TC (snapshot LATEST 2026-06-25 — theo cluster)

> Per-TC chi tiết: xem `report-dot-3.xlsx`. Bảng dưới tổng hợp theo cluster + liệt kê toàn bộ FAIL.

| Cluster | Đã chạy | ✅ PASS | ❌ FAIL | Ghi chú |
|---|:-:|:-:|:-:|---|
| C0 — Quản lý hỏi đáp (CRUD/Export/Batch) | 17 | 16 | 1 | FAIL: TC-HD-201 (emoji) |
| C0 — UI/export/upload bổ sung | 4 | 0 | 4 | FAIL: TC-HD-206/207/208 upload validation + TC-HD-211 export thiếu 19 cột + footer |
| C1 — Tìm kiếm tổng hợp | 13 | 12 | 1 | PASS mới: TC-HD-HDTK-021 read-only tab; FAIL: TC-HDTK-101 (empty-state); +TC-HD-210 (cùng gốc) |
| C2 — Tiếp nhận + Đổi hạn/mức độ | 30 | 24 | 6 | PASS mới: TC-DXL-003; FAIL: TC-TN-203 + TC-DXL-110/111/112/113/208 |
| C4 — Phân công | 5 | 5 | 0 | Negatives + happy CA_NHAN |
| C5 — Phản hồi | 7 | 7 | 0 | XSS sanitize OK, state-guard OK |
| C6 — Phê duyệt/công khai/đóng | 8 | 6 | 2 | PASS mới: TC-HD-PD-010; FAIL: TC-PD-030 CB_NV cùng đơn vị đóng hồ sơ bị 403; TC-PD-061 empty-state Hoàn thành |
| **Tổng** | **99** | **84** | **15** | (TC-HD-210 nằm trong C1 nhóm FAIL) |

**Danh sách 15 FAIL (đầy đủ):**

| TC ID | Tên | Lý do FAIL | Bug |
|---|---|---|---|
| TC-HD-201 | Strip emoji tên người gửi | BE+FE lưu nguyên emoji/ZWS, vi phạm SRS:1073 F-33 | BUG-HD-RR-001 |
| TC-HD-206 | Upload 11 file (vượt limit 10) | Chọn 11 file nhỏ làm app redirect về `/login`, không reject file thứ 11 và không có toast "Tối đa 10 file/lần upload" | BUG-HD-RR-007 |
| TC-HD-207 | Upload file 21MB (>20MB) | File bị loại khỏi file-list nhưng không hiển thị toast "Tệp tối đa 20MB" | BUG-HD-RR-007 |
| TC-HD-208 | Upload file 0 byte | File `hd-empty.pdf` được nhận vào file-list, không reject và không có toast "Tệp ... trống, không hợp lệ" | BUG-HD-RR-007 |
| TC-HDTK-101 | Không có kết quả (empty-state) | Hiện "Trống" generic, không đúng F-27 SRS:1057 | BUG-HD-RR-002 |
| TC-HD-210 | Empty-state filter no-match | Cùng gốc F-27 | BUG-HD-RR-002 |
| TC-TN-203 | ghi_chu_tiep_nhan 1001 ký | BE chấp nhận 201, không enforce max 1000 | BUG-HD-RR-003 |
| TC-HD-211 | Export Excel header/footer | File chỉ có 11 cột, thiếu 19 cột + footer 4 dòng theo SRS | BUG-HD-RR-005 |
| TC-DXL-110 | Đổi THUONG → PHUC_TAP | Endpoint đổi mức độ không tồn tại; PATCH 200 nhưng giữ `THUONG` | BUG-HD-RR-004 |
| TC-DXL-111 | Đổi PHUC_TAP → THUONG | Cùng gốc F-02 chưa wiring | BUG-HD-RR-004 |
| TC-DXL-112 | Đổi mức độ state CHO_PHE_DUYET → cấm | Không có endpoint để trả state-guard đúng; feature absent | BUG-HD-RR-004 |
| TC-DXL-113 | Đổi mức độ thiếu lý do | Không có endpoint/validation lý do; feature absent | BUG-HD-RR-004 |
| TC-DXL-208 | Đổi mức độ liên tục | Không có endpoint đổi mức độ; PATCH bỏ qua field | BUG-HD-RR-004 |
| TC-PD-030 | CB_NV cùng đơn vị đóng DA_DUYET | `cb_nv_dp_01` GET được record AG DA_DUYET nhưng `dong-ho-so` trả 403 | BUG-HD-RR-006 |
| TC-PD-061 | Empty state khi chưa có HD hoàn thành | Tab Hoàn thành rỗng chỉ hiển thị "Trống", thiếu "Chưa có hỏi đáp nào đã xử lý" | BUG-HD-RR-002 |

**Evidence bổ sung:** `ui-hoi-dap-list-20260625.png`, `ui-readonly-da-duyet-no-edit-delete.png`, `export-hoi-dap-ui-batch.xlsx`, `export-hoi-dap-ui-batch-evidence.json`, `remaining-probe-20260626.json`, `remaining-actions-20260626.json`, `remaining-actions-2-20260626.json`, `pd030-close-cbnvdp-20260626.json`, `ui-pd061-hoan-thanh-empty-20260626.png`, `ui-hd206-11files-redirect-login-20260626.png`, `ui-hd207-21mb-no-toast-20260626.png`, `ui-hd208-zero-byte-accepted-20260626.png`.

**Điểm mạnh đã verify PASS (evidence thật):** state-machine đầy đủ (MOI→TIEP_NHAN→DANG_XU_LY→CONG_KHAI→HOAN_THANH + HUY); validation create (trống/min20/max5000/email/sdt/FK lĩnh vực ERR-HD-03); state-guard sửa/xóa DA_DUYET (409); optimistic locking (409); XSS sanitize phản hồi (script/onclick/javascript: đều bị loại); phân quyền (CB_PD/DN/cross-tenant/IDOR 403-404); batch delete per-record report; search (SQLi-safe, tiếng Việt NFC/NFD, full-text, filter combo AND, page_size, tab counts); cập nhật thời hạn (boundary/state/version); timeline lichSu.

## Bảng TC chưa chạy được — cần làm gì để chạy (58 case runnable + 26 "Chưa tích hợp")

> Hiện còn **58 case runnable** chưa chạy — chia 4 nhóm: phần còn lại cần **UI-session** (modal/editor/visual) · **data đặc thù** (batch đủ số lượng, phản hồi đã duyệt để công khai) · **cross-cấp/account đúng đơn vị** · **infra/time/concurrent**. Cộng 26 case đã đánh "Chưa tích hợp" (hạ tầng/cổng ngoài).

| Nhóm | Vì sao chưa chạy được | TC tiêu biểu | Cần làm gì để chạy | Ai làm |
|:-:|---|---|---|:-:|
| **D-Env** | Cần ClamAV / mock backend / scheduled job / email gateway thật | TC-HD-205, TC-HD-209, TC-TN-204/207, TC-DXL-205/211 (đã đánh "Chưa tích hợp") | Bật ClamAV + mock 503 + trigger SLA job + MailHog | Infra |
| **F-Khác** | Data-volume / time-dependent lớn | TC-HD-105 (12K rows), TC-PD-032 (6 tháng), TC-DXL-207 (≥100 entries) | Seed khối lượng lớn / mock thời gian | QA seed |
| **B-Dev fix** | Nhóm đổi mức độ đã có verdict FAIL, không còn nằm trong CHƯA CHẠY | TC-DXL-110/111/112/113/208 | Dev xác nhận endpoint đổi mức độ / wiring nút F-02 trước khi re-test | Dev BE |
| **A-Seed** | Thiếu record CHO_PHE_DUYET/DA_DUYET thuộc TW để test duyệt/từ chối/công khai batch (bị chặn bởi gap "đánh dấu Đã trả lời" trước gui-duyet) | TC-HD-PD-010, TC-PD-040/041/042/043/050/051/052/068/071, TC-HD-PD-024/025 | Dev/BA làm rõ bước finalize phản hồi (set ngay_tra_loi) để walk →CHO_PHE_DUYET; hoặc seed | QA seed/BA |
| **A-Account** | Cần account cross-cấp/cross-bộ (CB_PD_DP, CB_PD_BN) + data đúng cấp | TC-PD-100/033/076 | Dùng cb_pd_dp/cb_pd_bn + record đúng đơn vị | QA API |
| **UI** | Hành vi modal/editor/visual chỉ verify qua UI-session | TC-PC-200..213, TC-PH-202/205/206/208-212, TC-PD-060/066/070/072, TC-HD-232/235, TC-HDTK-206, TC-TN-201/208, TC-PC-102/104/106/108 | Chạy batch UI riêng (Chrome MCP click/screenshot) | QA UI |

> **Lưu ý:** TC-HD-HDTK-003 (filter TVN_BRIDGE) cần record escalate từ Tư vấn nhanh (cross-module); tạo trực tiếp `kenhTiepNhan=TVN_BRIDGE` qua API → BE trả 500 (cần `tuVanNhanhGocId`). TC-HDTK-206 cần 1 lĩnh vực `is_deleted=1` (hệ thống hiện không có lĩnh vực vô hiệu nào).
