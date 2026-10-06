# Functional Test Report — Đào tạo, tập huấn (dot-3 rerun)

**Ngày:** 2026-06-26 17:35:00 · **Môi trường:** http://103.172.236.130:3000/ · **Tool:** Chrome DevTools MCP
**Phạm vi:** Re-test batch dot-3 — 13 TC chạy nhanh (chưa-chạy/không-lý-do) + 15 TC FAIL (đối chiếu SRS v3.5 `srs-fr-03-dao-tao.md`). **KHÔNG** phải toàn bộ 471 TC module.

## Verdict

- **PASS 7** · **FAIL 5** · **Chờ BA 6** · **Thiếu seed/Block 8** · **Defer 2** (tổng 28 TC re-test).
- Đối chiếu SRS: **1 false-FAIL** (TC bắt wording) → PASS; **6 FAIL** test hành vi SRS không quy định → reclass Chờ BA; **5 FAIL thật** (2 bug: BUG-DT-RR-001 Hủy, BUG-DT-RR-002 Xuất); **3 FAIL** thực chất thiếu seed → reclass CHƯA CHẠY (nhóm A).
- Phát hiện hệ thống: **DB không có record DANG_KY_DAO_TAO** (0 học viên mọi khóa) → block toàn bộ TC điểm danh/điểm KT/duyệt đăng ký. Counter "12/25" ở list khóa lệch với đăng ký thực = 0 (Minor).

## Accounts

- `cb_nv_tw_01` (CB_NV_TW, BTP-TW) — quản lý Đào tạo. OTP `666666`.

---

## Bảng trạng thái TC (snapshot dot-3 rerun — LATEST 2026-06-26 17:35:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| TC-KH-NAM-N-007 | Tên KH năm trống → ERR-KH-01 | ✅ Đạt | dot-3-RR | Validation chặn; wording "Vui lòng nhập…" ≈ ERR-KH-01 (Minor) |
| TC-DEXUAT-H-005 | Truncate cột Nội dung | ✅ Đạt | dot-3-RR | `ant-table-cell-ellipsis` + title tooltip verified |
| TC-DT-DK-UI-01 | Tab Học viên layout | ✅ Đạt | dot-3-RR | Bảng+filter trạng thái+nút Thêm/Import; 0 dòng (empty hợp lệ) |
| TC-KQ-UI-02 | Tab KQ kiểm tra form | ✅ Đạt | dot-3-RR | Cột Chuyên cần/Điểm/Kết quả/Ghi chú + Lưu KQ |
| TC-BG-UI-01 | Kho tài liệu SCR-III-03 | ✅ Đạt | dot-3-RR | List+preview "Xem trước"+filter Loại+Công khai |
| TC-GV-004 | Tab Lịch sử giảng dạy | ✅ Đạt | dot-3-RR | List khóa đã dạy + cột Vai trò |
| TC-GV-012 | Lịch sử GD aggregate vai_tro | ✅ Đạt | dot-3-RR | Vai trò "Giảng viên" per khóa (Minor: counter 2 vs 1 dòng) |
| TC-KH-H-015 | Hủy KH DU_THAO → DA_HUY | ❌ Lỗi | dot-3-RR | Không có nút Hủy, chỉ Xóa hard-delete — BUG-DT-RR-001 |
| TC-KH-S-026 | DU_THAO → DA_HUY (re-state) | ❌ Lỗi | dot-3-RR | Duplicate TC-KH-H-015 — BUG-DT-RR-001 |
| TC-XUAT-H-003 | Xuất DOCX CTĐT DA_DUYET | ❌ Lỗi | dot-3-RR | CTĐT detail thiếu nút Xuất — BUG-DT-RR-002 |
| TC-XUAT-H-004 | Xuất DOCX CTĐT DA_CONG_KHAI | ❌ Lỗi | dot-3-RR | Thiếu nút Xuất — BUG-DT-RR-002 |
| TC-XUAT-H-006 | Xuất PDF CTĐT DA_DUYET | ❌ Lỗi | dot-3-RR | Thiếu nút Xuất — BUG-DT-RR-002 |
| TC-GV-002 | Filter LV + vai_tro=TRO_GIANG | 🤷 Chờ BA | dot-3-RR | UI bỏ filter vai_tro theo STT26; FR-III-12 chưa update |
| TC-CTDT-E-030 | Optimistic lock CTĐT | 🤷 Chờ BA | dot-3-RR | SRS không quy định optimistic-lock/ERR-SYS-02 |
| TC-KH-E-038 | Optimistic lock KH | 🤷 Chờ BA | dot-3-RR | SRS không quy định |
| TC-GV-022 | Optimistic lock rename GV | 🤷 Chờ BA | dot-3-RR | SRS không quy định |
| TC-DEXUAT-E-015 | Double-click idempotency | 🤷 Chờ BA | dot-3-RR | SRS không quy định debounce/idempotency |
| TC-NHCH-008 | Sửa câu hỏi đã phân phối → cảnh báo | 🤷 Chờ BA | dot-3-RR | WRN-NHCH-01 chỉ áp cho XÓA, không cho SỬA |
| TC-KQ-N-001 | Điểm KT = -1 → ERR-KQ-01 | 🚫 Block | dot-3-RR | Thiếu seed HV để nhập điểm; TC đúng SRS:600 |
| TC-KQ-N-002 | Điểm KT = 11 → ERR-KQ-01 | 🚫 Block | dot-3-RR | Thiếu seed HV; TC đúng SRS:600 |
| TC-DK-H-006 | Duyệt ĐK CHO_DUYET → DA_DUYET | 🚫 Block | dot-3-RR | Không có đăng ký CHO_DUYET; TC đúng SRS:430 |
| TC-DK-N-001 | Đăng ký vượt số lượng | 🚫 Block | dot-3-RR | Không có lớp đầy thật (đăng ký=0) |
| TC-KQ-UI-01 | Lịch học & Điểm danh matrix | 🚫 Block | dot-3-RR | Cần HV+buổi cho ma trận điểm danh + % chuyên cần |
| TC-CB-H-002 | CB PD từ chối KQ ≥10 ký tự | 🚫 Block | dot-3-RR | Thiếu seed CHO_DUYET_KQ + cần CB_PD |
| TC-CB-N-003 | CB PD từ chối KQ <10 ký tự | 🚫 Block | dot-3-RR | Thiếu seed CHO_DUYET_KQ + cần CB_PD |
| TC-LICH-H-002 | Lịch học read-only DA_CONG_KHAI | 🚫 Block | dot-3-RR | Không có khóa DA_CONG_KHAI (đếm=0) |
| TC-DK-H-005 | Import Excel danh sách HV | ⏭ Hoãn | dot-3-RR | Cần file Excel mẫu — defer |
| TC-KQ-P-001 | CB PD không quyền nhập điểm | ⏭ Hoãn | dot-3-RR | Cần login CB_PD + seed HV — defer |
| **Tổng** | **28 TC** | ✅7 · 🤷6(Chờ BA) · ❌5 · 🚫8 · ⏭2 | | |

---

## Bảng TC chưa chạy được — cần làm gì để chạy (dot-3 rerun)

Hiện còn **21 TC chưa PASS** — chia 4 nhóm: **5 chờ dev fix (2 bug)** · **6 chờ BA chốt spec** · **8 chờ seed dữ liệu học viên** · **2 hoãn (cần file/role)**.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| TC-KH-H-015 / S-026 | Khóa DU_THAO không có nút Hủy (→DA_HUY), chỉ có Xóa vĩnh viễn | Bổ sung hành động "Hủy" cho khóa DU_THAO theo SRS SM-KHOAHOC:2011 (BUG-DT-RR-001) | Dev FE |
| TC-XUAT-H-003 / 004 / 006 | Trang chi tiết CTĐT không có nút Xuất DOCX/PDF | Bổ sung chức năng Xuất file theo FR-III-20:1366 (BUG-DT-RR-002) | Dev FE |
| TC-GV-002 | SRS FR-III-12 còn filter vai_tro nhưng STT26 đã chuyển vai_tro xuống cấp buổi | BA chốt: bỏ filter vai_tro khỏi FR-III-12 hay giữ | BA |
| TC-CTDT-E-030 / KH-E-038 / GV-022 | TC test optimistic-lock mà SRS không quy định | BA chốt có yêu cầu optimistic-lock khi 2 user sửa đồng thời không | BA |
| TC-DEXUAT-E-015 | TC test idempotency double-click mà SRS không quy định | BA chốt có yêu cầu chống double-submit không | BA |
| TC-NHCH-008 | TC test cảnh báo khi SỬA câu hỏi đã phân phối — SRS chỉ quy định cho XÓA | BA chốt có cần cảnh báo khi sửa không | BA |
| TC-KQ-N-001 / N-002 | DB không có học viên nào để nhập điểm | Seed DANG_KY_DAO_TAO (HV đã duyệt) cho 1 khóa DANG_DIEN_RA | QA seed |
| TC-DK-H-006 | Không có đăng ký trạng thái CHO_DUYET để duyệt | Seed đăng ký CHO_DUYET vào 1 khóa DA_CONG_KHAI | QA seed |
| TC-DK-N-001 | Không có lớp đầy học viên thật (đăng ký=0) | Seed đủ HV cho lớp đạt số_lượng_tối_đa | QA seed |
| TC-KQ-UI-01 | Cần học viên + buổi học cho ma trận điểm danh | Seed HV + LICH_HOC cho 1 khóa | QA seed |
| TC-CB-H-002 / N-003 | Thiếu khóa CHO_DUYET_KQ + cần role CB_PD | Seed khóa CHO_DUYET_KQ có KQ + chạy với CB_PD | QA seed |
| TC-LICH-H-002 | Không có khóa trạng thái DA_CONG_KHAI | Seed/đưa 1 khóa lên DA_CONG_KHAI | QA seed |
| TC-DK-H-005 | Cần file Excel mẫu danh sách HV để test import | Chuẩn bị file .xlsx đúng template import | QA seed |
| TC-KQ-P-001 | Cần login CB_PD + seed HV để verify read-only | Đăng nhập CB_PD trên khóa có HV, kiểm nhập điểm bị khóa | QA API |

---

## Chi tiết đối chiếu SRS (FAIL reconcile)

Xem đầy đủ tại [FAIL-reconcile-srs-dao-tao.md](../dao-tao/FAIL-reconcile-srs-dao-tao.md). Tóm tắt:

**Nhóm A — TC đúng SRS, FAIL thật / cần seed:**
- TC-KH-NAM-N-007: validation đúng → PASS (FAIL gốc do bắt wording literal ERR-KH-01).
- TC-KH-H-015/S-026, TC-XUAT-H-003/004/006: chức năng thiếu trên UI → FAIL thật (2 bug).
- TC-KQ-N-001/002, TC-DK-H-006: TC đúng SRS nhưng thiếu seed HV → CHƯA CHẠY.

**Nhóm B — TC sai SRS (đã sửa TC trong xlsx):**
- TC-XUAT-H-003/004/006: bỏ kỳ vọng ký số outbound (`/ky-so/sign-doc`, EXPORT_SIGNED, chữ ký nhúng) — SRS FR-III-20 chỉ yêu cầu sinh file từ template → download.
- TC-KH-H-015/S-026: sửa enum `HUY` → `DA_HUY` (SRS:2011).

**Nhóm C — TC test hành vi SRS không quy định → Chờ BA:**
- TC-CTDT-E-030, TC-KH-E-038, TC-GV-022 (optimistic-lock), TC-DEXUAT-E-015 (idempotency), TC-NHCH-008 (cảnh báo sửa), TC-GV-002 (filter vai_tro vs STT26).

---

## Bug liên quan

[bug-report-dao-tao-rerun.md](../bug-reports/dao-tao/bug-report-dao-tao-rerun.md) — BUG-DT-RR-001 (Hủy DU_THAO), BUG-DT-RR-002 (Xuất CTĐT). Cả 2 Major/P1, Open.
