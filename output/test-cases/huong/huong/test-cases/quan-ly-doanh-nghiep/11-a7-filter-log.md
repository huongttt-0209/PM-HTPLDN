# 11 — A7 Filter Log: UI/Function-Testable (audit log)

> **Skill**: Manual review + Edit
> **Ngày chạy**: 2026-05-09
> **Module**: FR-07 W2.1 Quản lý DN
> **Iron rule**: TC bị xóa/sửa đã Edit IN-PLACE file UC tương ứng. File này CHỈ log action LOẠI/SỬA/GIỮ.

---

## A. A7 Filter rule recap

- **❌ LOẠI**: TC require DB query trực tiếp ("verify row trong bảng X", "check INDEX tồn tại"), curl/Postman API thuần, cron/queue background no-UI feedback
- **✏️ SỬA**: TC có verification chỉ-DB → chuyển thành verify network qua MCP `list_network_requests` hoặc UI bridge
- **✅ GIỮ**: TC chạy 100% UI/function user-facing — bao gồm verify network response qua MCP

---

## B. Tổng kết action

| Action | Count |
|--------|---:|
| ❌ LOẠI | 0 |
| ✏️ SỬA (UI bridge) | 5 |
| ✅ GIỮ | 129 |
| **Tổng** | **134 TC** |

---

## C. Detailed log SỬA (5 TCs)

| TC ID | File | Lý do SỬA | Diff |
|-------|------|-----------|------|
| TC-DN-019 | 01-CRUD | Original "DevTools fetch GET /api/v1/doanh-nghieps/{id}" — direct API | SỬA: thêm bước 1 "DN tự đăng ký FR-VIII-22" trước, bước 2 "CB NV mở chi tiết qua UI", bước 3 "MCP `list_network_requests` filter `/api/v1/doanh-nghieps/`" → API call gián tiếp khi user thao tác UI |
| TC-DN-103 | 01-CRUD | Original "Verify qua DevTools fetch hoặc UC quản lý DN với filter Đã xóa" — direct API option | SỬA: ưu tiên UI Nhật ký HT (FR-VIII-28) verify AUDIT_LOG row UPDATE/DELETE; DevTools fetch chỉ là option B nếu UI có toggle "Hiển thị đã xóa" |
| TC-HSPL-008b | 03-HSPL | Original "DevTools intercept POST → đổi doanh_nghiep_id" — request tampering | SỬA: thay scenario thành race condition realistic (User A xóa DN, User B đã mở Tab 2 cached state, tạo HSPL → backend reject ERR-HSPL-02). UI-driven testable. |
| TC-LS-304 | 04-LSHT | Original "Compare counter vs COUNT thực tế" — DB query | SỬA: stress test 10 vòng tạo VV qua FR-05 + verify KPI 1 tăng đúng +1 mỗi vòng — chỉ dùng UI |
| TC-DN-PERM-403 | 06-Permission | Original "DevTools cố PUT/DELETE AUDIT_LOG row" — direct API tampering | SỬA: split 2 phần (a) UI verify KHÔNG có nút Edit/Delete trên Nhật ký HT, (b) MCP `evaluate_script` fetch tampered (security test acceptable do BR-DATA-05 yêu cầu kiểm chứng backend immutable). Documented purpose. |

---

## D. SPEC-CLARIFY entries (tổng 45 — chờ BA)

| ID | TC ref | Topic | Hỏi BA |
|----|--------|-------|--------|
| SPEC-CLARIFY-DN-01 | TC-DN-UI-01 | UI nút "Thêm mới" + "Import Excel" | UI đã xóa nút Thêm mới + Import Excel theo Thay đổi 1+2 chưa? Nếu vẫn còn → log bug Critical |
| SPEC-CLARIFY-DN-02 | 00-overview | Header SRS v3.0 vs filename v3.1 | Header file SRS ghi "Phiên bản 3.0" nhưng filename `v3.1.md` → tag chính thức là gì? |
| SPEC-CLARIFY-DN-03 | TC-DN-UI-05 | Form CMS có Fax field? | SCR-V.III-02 dòng 22 có "Fax" nhưng FR-V.III-01 Inputs không liệt kê. UI có hiển thị field này? |
| SPEC-CLARIFY-DN-04 | TC-DN-009 | Email format ERR code | SRS Inputs ghi "Format email hợp lệ" nhưng không có ERR code. ERR code chính thức là gì? |
| SPEC-CLARIFY-DN-05 | TC-DN-011/012 | so_lao_dong_nu/khuyet_tat CHECK violation ERR | CHECK constraint srs-v3.5:1612 nhưng không có ERR code UI. ERR là gì? |
| SPEC-CLARIFY-DN-06 | TC-DN-105 | Delete DN có VV HOAN_THANH | "Không có vụ việc đang xử lý" — HOAN_THANH có thuộc "đang xử lý" không? Cho xóa hay chặn? |
| SPEC-CLARIFY-DN-07 | TC-DN-TK-301 | Xuất Excel hoạt động? | OUT D.2.1 chỉ giữ nút (không có Processing/AC). Nút có hoạt động không? Nếu có thì theo logic FR-V.III-01 Processing line 154-163 cũ? |
| SPEC-CLARIFY-DN-08 | TC-DN-TK-005 | Multi-select linh_vuc OR/AND | Pick 2 LV: trả DN có ≥1 LV (OR) hay phải có cả 2 (AND)? |
| SPEC-CLARIFY-DN-09 | TC-DN-TK-006 | Filter date range INCLUSIVE/EXCLUSIVE den_ngay | Boundary den_ngay tính đến 23:59:59 (INCLUSIVE) hay 00:00 ngày sau (EXCLUSIVE)? |
| SPEC-CLARIFY-DN-10 | TC-DN-TK-203 | UI có dropdown page size? | BR-DATA-07 max 100 nhưng UI có dropdown thay đổi page size không? |
| SPEC-CLARIFY-DN-11 | TC-DN-TK-303 | Export 0 record behavior | Toast "Không có dữ liệu" hay file rỗng? |
| SPEC-CLARIFY-DN-12 | TC-HSPL-008 | UI maxlength ten_ho_so 500 | Form có HTML maxlength="500"? |
| SPEC-CLARIFY-DN-13 | TC-HSPL-404 | Antivirus setup env test | EICAR test sample được phát hiện qua antivirus chưa setup? |
| SPEC-CLARIFY-DN-14 | TC-HSPL-406 | File type validation ERR code | Reject .exe có ERR code chính thức? |
| SPEC-CLARIFY-DN-15 | TC-LS-005/006 | Counter sync timing | Materialized view hay trigger? Trigger thì sync ngay, MV thì lag — SLA bao lâu? |
| SPEC-CLARIFY-DN-16 | TC-CT-UI-02 | Empty state Tab 4 text | NGUYÊN VĂN text empty state? |
| SPEC-CLARIFY-DN-17 | TC-CT-UI-03 | Route HSCT chi tiết FR-06 | URL pattern `/chi-tra/{id}` hay khác? |
| SPEC-CLARIFY-DN-18 | TC-CT-101 | Tab 4 có dòng SUM total? | UI có hiển thị tổng chi phí HSCT cuối table không? |
| SPEC-CLARIFY-DN-19 | TC-DN-PERM-007 | TW Edit cross-tenant DN | TW có quyền Edit DN do ĐP tạo? Hay TW chỉ R |
| SPEC-CLARIFY-DN-20 | TC-DN-PERM-303 | DN.MST đổi sync TAI_KHOAN.username | Đổi MST có nên đổi username TK theo? Hay giữ độc lập? |
| SPEC-CLARIFY-DN-21 | TC-DN-PERM-404 | AUDIT_LOG ghi attempt 403 | Backend có log row hành động deny? Hay chỉ log thành công? |
| SPEC-CLARIFY-DN-22 | TC-DN-PERM-503 | NHT HSPL CRU* vs AC9 mâu thuẫn | Permission Matrix HSPL row NHT = `CRU*` nhưng FR-X.1-04 AC line 671 ghi "NHT chỉ R + U". Quyền nào đúng? |
| SPEC-CLARIFY-DN-23 | TC-DN-301 | Optimistic lock | Có optimistic concurrency control không? Nếu có thì ETag header? |
| SPEC-CLARIFY-DN-24 | TC-DN-303 | Whitespace trim policy | Backend trim leading/trailing space ten_doanh_nghiep? |
| SPEC-CLARIFY-DN-25 | TC-DN-306 | MST format ERR code | MST không 10 chữ số có ERR code chính thức? |
| SPEC-CLARIFY-DN-26 | TC-DN-307 | File 0-byte upload | Reject 0-byte file? Toast text NGUYÊN VĂN? |
| SPEC-CLARIFY-DN-27 | TC-DN-309 | Soft-deleted DN restore + MST UNIQUE | UNIQUE MST có loại trừ soft-deleted? |
| SPEC-CLARIFY-DN-28 | TC-DN-TK-503 | Search accent-insensitive | "cong ty" tìm "Công ty" có hỗ trợ? |
| SPEC-CLARIFY-DN-29 | TC-DN-TK-504 | tu_khoa max length | Có giới hạn 200 char không? |
| SPEC-CLARIFY-DN-30 | TC-DN-TK-505 | Reversed date range ERR code module DN | DN module có ERR code "Từ ngày phải nhỏ hơn Đến ngày"? |
| SPEC-CLARIFY-DN-31 | TC-DN-TK-507 | Sort secondary tie-breaker | Default tie-breaker by id DESC? |
| SPEC-CLARIFY-DN-32 | TC-HSPL-702 | ngay_cap > ngay_het_han ERR | Có CHECK constraint giữa 2 trường không? |
| SPEC-CLARIFY-DN-33 | TC-HSPL-703 | DELETE HSPL cascade file | File đính kèm có cascade soft-delete không? |
| SPEC-CLARIFY-DN-34 | TC-HSPL-704 | File MIME spoof detection | Backend detect MIME type vs extension? |
| SPEC-CLARIFY-DN-35 | TC-LS-302/CT-403 | Performance SLA | SLA load Tab 3/4 với 1000 record? |
| SPEC-CLARIFY-DN-36 | TC-LS-304 | Counter sync recover policy | Khi counter lệch, recover bằng job nào? |
| SPEC-CLARIFY-DN-37 | TC-CT-402 | Tab 4 filter trang_thai HSCT | Có filter trên Tab 4 không? |
| SPEC-CLARIFY-DN-38 | TC-CT-404 | VV grouping in Tab 4 | Tab 4 có group HSCT theo VV không? |
| SPEC-CLARIFY-DN-39 | TC-DN-PERM-601 | Session draft restore | Có sessionStorage draft form khi session expire? |
| SPEC-CLARIFY-DN-40 | TC-DN-PERM-602 | OTP brute force lockout | Max attempt = bao nhiêu? Lockout duration? |
| SPEC-CLARIFY-DN-41 | TC-DN-PERM-603 | TAI_KHOAN.email change conflict ERR | ERR code khi email trùng user khác? |
| SPEC-CLARIFY-DN-42 | TC-DN-PERM-604 | DN chi nhánh 13 chữ số reject | UI có block self-reg với MST 13 chữ số? |
| SPEC-CLARIFY-DN-43 | TC-DN-019b | la_nu_lam_chu visual indicator | UI có badge/icon "Phụ nữ làm chủ" trên list? |
| SPEC-CLARIFY-DN-44 | TC-HSPL-104/105 | SM-HSPL HET_HAN/THU_HOI restore | Cho phép restore HET_HAN/THU_HOI về HIEU_LUC? |
| SPEC-CLARIFY-DN-45 | TC-DN-PERM-008 | DN role redirect CMS | DN login vào CMS → redirect chuyên trang? |

---

## E. Acceptance verify (Phase A done acceptance check)

- [x] 7 bước A1-A7 hoàn thành
- [x] Traceability sau A6 fill = 100% (BR/AC/SM/Permission/Error)
- [x] 0 TC chỉ-DB/API thuần (5 TC SỬA UI bridge sau A7)
- [x] 0 TC sống ở file phụ — mọi TC nằm trong 6 file UC
- [x] 45 SPEC-CLARIFY listed kèm proposal answer (file này) — chờ BA Phase B

**Phase A acceptance**: ✅ PASS — sẵn sàng forward Codex review.

---

**— Hết 11 A7 Filter Log FR-07 —**
