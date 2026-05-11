# BÁO CÁO TỔNG HỢP QA — 4 MODULE
**Phạm vi:** Đào tạo · Biểu mẫu · CT HTPLDN · QTHT
**Cập nhật:** 2026-05-11 19:30 (sau probe E2E chuyên trang DN/NHT)
**Tester:** QA Automation (Claude Code MCP)

---

## 1. TL;DR (1 phút đọc)

| Module | Sẵn sàng GA? | Pass rate task | Vấn đề chính |
|---|:-:|:-:|---|
| **CT HTPLDN** | ✅ GA-ready | 5/5 (100%) | Chỉ còn 3 observation Minor |
| **QTHT** | ✅ GA-ready | 14/16 (88%) | 1 method gap UI + 1 TVV login isolated env |
| **Biểu mẫu** | ✅ GA với note | 2/4 ✅ + 2/4 ⚠️ | 1 bug Medium UX (Switch không ẩn 3 trường) |
| **Đào tạo** | ❌ **Chưa GA** | 16/17 (94%) | **6 Major Open** chặn nhánh đăng ký HV + KQHT |

→ **3/4 module sẵn sàng release.** Đào tạo cần dev BE fix 6 bug Major trước GA.

---

## 2. Module nào chạy được full flow?

### ✅ Đã chạy được full flow

**CT HTPLDN** (5/5 task ✅)
- GĐ1: 11/11 transitions PASS (DU_THAO → CHO_PHE_DUYET → DA_DUYET → DA_CONG_BO → DANG_THUC_HIEN → HOAN_THANH/HUY)
- GĐ2 Đợt BC: 7/7 transitions hiệu lực qua 3 cấp TW/BN/ĐP
- Functional: 25/25 P0 PASS. End-to-end TW tổng hợp BC từ BN+ĐP đã chạy thành công (R4 11/05).

**QTHT** (14/16 task ✅)
- 14 DM CRUD: 25/25 PASS · TAI_KHOAN SM: 6/6 PASS · Self-reg DN: 8/8 PASS
- Reset MK + kích hoạt: 7/7 PASS · Audit log: 1468 entries · Vai trò: 11/11 PASS
- 2 task ⚠️: R7.2.9 (9 TK verify bằng API thay vì UI — data OK, method gap) + R7.2.9b (TVV login MK sau set MK fail 401 — token race / cần isolated env)

**Biểu mẫu** (2/4 ✅ + 2/4 ⚠️)
- CRUD + workflow công khai end-to-end PASS (BR-PUBLIC-01/02/03 enforce)
- Cumulative: 37/47 TC PASS+PARTIAL (79%), 0 FAIL, 0 BLOCKED
- 1 bug Medium còn open: Form Thêm BM — 3 trường công khai vẫn visible khi Switch OFF

### ⚠️ CHƯA chạy được full flow

**Đào tạo** — Block 2 nhánh:

| Nhánh | Bước vướng | Bug |
|---|---|---|
| **Đầu vào — DN/NHT đăng ký HV qua chuyên trang** | VPD chặn DN/NHT access KH `congKhai=true` cross-đơn-vị → 403 (NEW R11) | BUG-DT-CT-VPD-01 Major |
| **Đầu ra — Kết quả học tập + Cổng PLQG** | KQHT entity 404 (chưa deploy) + DIEM_DANH POST 404 + thiếu inbound endpoint | BUG-DT-031-KQHT-ENTITY-01 + BUG-DT-011-DD-ENDPOINT-01 + BUG-DT-CT-INBOUND-01 |
| **Gán Bài giảng** | UI thiếu nút "Gán bài giảng" + BE thiếu nested route | BUG-DT-038-ASSIGN-01 Major |
| **Cross-tenant** | GET `/ke-hoach-dao-taos` trả KH năm của mọi đơn vị (vi phạm BR-AUTH-08) | BUG-KH-001 Major (RE-CONFIRMED) |

---

## 3. Danh sách BLOCK (10 flow/TC)

| # | TC / Flow | Block tại | Nguyên nhân | Người fix |
|:-:|---|---|---|---|
| 1 | DN/NHT đăng ký HV (FR-III-04 UC23) | GET KH + POST DKDT | VPD filter không bypass `congKhai=true` | Dev BE |
| 2 | DT-011 Điểm danh | POST `/diem-danhs` | Endpoint 404 + schema `coMat boolean` vs enum 3 trị | Dev BE |
| 3 | DT-031b/c/d Công bố KQ + Cổng PLQG | KQHT + push API | Entity KET_QUA_HOC_TAP 404 (5 routes chưa deploy) | Dev BE |
| 4 | DT-054 Auto xếp loại điểm | Tính Giỏi/Khá/TB | Cascade #3 | Dev BE |
| 5 | DT-055 HV đạt khóa | Verify chuyên cần + điểm | Cascade #2 + #3 | Dev BE |
| 6 | DT-038 Gán Bài giảng | UI assign | UI thiếu nút + BE thiếu nested route | Dev FE+BE |
| 7 | Cổng PLQG đẩy đăng ký về CMS | POST inbound | Thiếu `/public/dang-ky-dao-taos/inbound` + `/public/hoc-viens/inbound` | Dev BE |
| 8 | KH năm cross-tenant leak | GET list | BE không filter `donViId` | Dev BE |
| 9 | TVV login MK sau set MK | UI login | Token race / FE silent fail (cần isolated env) | Dev BE + QA |
| 10 | R7.2.9 9 TK verify UI E2E mail | UI E2E re-run | Method gap (curl API thay vì click mail UI) | QA re-run |

---

## 4. Kết nối / đồng bộ ngoài hệ thống

| Hệ thống ngoài | Trạng thái | Ảnh hưởng |
|---|---|---|
| **Cổng PLQG** (Pháp luật Quốc gia) | ❌ Chưa setup mock + thiếu 2 inbound endpoint cho đào tạo | Block DT-031b/c/d + luồng đăng ký HV external |
| **MinIO** (file storage) | ✅ Đã fix `MINIO_PUBLIC_HOST` (R8 lần 8) | OK |
| **MailHog** (SMTP) | ✅ Hoạt động, mail TVV/NHT/CG/DN đúng SRS pattern | OK |
| **Chuyên trang DN/NHT** | ⚠️ **Đã rõ R11:** KHÔNG phải subdomain riêng — là CMS internal với role-based filter. Bị chặn bởi BUG-DT-CT-VPD-01 | Chờ dev BE fix VPD bypass |
| **mTLS sandbox** | ⏭ Defer | Block 1 TC bulk import Biểu mẫu |
| **VNeID** | Chưa test trong scope 4 module | N/A |

---

## 5. Tổng quan từng module

### 5.1 CT HTPLDN — ✅ Hoàn thiện nhất

- **Phạm vi:** Quản lý Chương trình HTPLDN 2 giai đoạn — CT cha (8-state SM) + Đợt BC (6-state SM) qua 3 cấp TW/BN/ĐP
- **Trạng thái:** 5/5 ✅, 25/25 P0 PASS, UI Story 13.6 build đủ, BE end-to-end TW tổng hợp BC từ BN+ĐP đã PASS
- **Còn lại:** 3 OBS Minor (wording, field naming inconsistency, response design). Sẵn sàng GA.

### 5.2 QTHT — ✅ Core đầy đủ

- **Phạm vi:** 14 DM + TAI_KHOAN SM + Vai trò + Audit log + Self-reg DN + Reset MK
- **Trạng thái:** 14/16 ✅. Pool TK 89 records, audit 1468 entries (14.68× ngưỡng)
- **Còn lại:** R7.2.9 method gap (verify bằng API curl thay UI) + R7.2.9b TVV login chờ isolated env. Sẵn sàng GA.

### 5.3 Biểu mẫu — ✅ Gần hoàn thiện

- **Phạm vi:** TM/BM CRUD + workflow công khai (BR-PUBLIC-01/02/03) + bulk import + MinIO preview/download
- **Trạng thái:** 79% PASS+PARTIAL (37/47 TC), 0 FAIL, 0 BLOCKED. 8 bug đã closed.
- **Còn lại:** 1 bug Medium (BUG-BM-010 — Switch không ẩn 3 trường) + 4 TC pending test files + 5 TC defer external. Sẵn sàng GA với note.

### 5.4 Đào tạo — ❌ Chưa GA

- **Phạm vi:** KH năm 3 cấp → CTĐT → Khóa học → NHCH → ĐKT → Bài giảng → Giảng viên → Học viên → Lịch học → Điểm danh → KQHT
- **Trạng thái:** 16/17 task ✅ workflow chính, nhưng **block nhánh đăng ký HV + KQHT**
- **6 bug Major Open:**
  1. BUG-DT-CT-VPD-01 (NEW R11) — VPD chặn DN/NHT access KH công khai
  2. BUG-DT-CT-INBOUND-01 (NEW R11) — Thiếu inbound endpoint Cổng PLQG cho đăng ký + HV
  3. BUG-DT-031-KQHT-ENTITY-01 — KQHT entity 404 chưa deploy
  4. BUG-DT-011-DD-ENDPOINT-01 — DIEM_DANH POST 404 + schema sai
  5. BUG-DT-038-ASSIGN-01 — KH↔BG N-N relation chưa implement
  6. BUG-KH-001 — Cross-tenant data leak KH năm (RE-CONFIRMED R10+R11)
- **Đánh giá:** ~70% hoàn thiện. Workflow chính OK, cần dev BE fix 6 bug để hoàn thiện 2 nhánh chính.

---

## 6. TOP 5 ưu tiên xử lý

| # | Action | Effort | Unblock |
|:-:|---|:-:|---|
| 1 | **Fix BUG-DT-CT-VPD-01** — VPD bypass cho KH `congKhai=true` | 1-2 ngày | 9 TC HV-related + luồng đăng ký HV qua chuyên trang |
| 2 | **Deploy KET_QUA_HOC_TAP + DIEM_DANH POST endpoint** | 3-5 ngày | 6 TC nhánh kết quả học tập |
| 3 | **Fix BUG-KH-001 cross-tenant leak** | 1-2 ngày | Tuân thủ BR-AUTH-08 phân quyền dữ liệu |
| 4 | **Add inbound endpoint Cổng PLQG đào tạo** + setup mTLS sandbox | 1 tuần | External flow Cổng PLQG đẩy đăng ký về CMS |
| 5 | **Build FE assign Bài giảng + BE nested route** (DT-038) | 2-3 ngày | N-N relation KH↔BG |

---

## 7. Cần BA xác nhận thêm

1. **VPD bypass cho `congKhai=true`** — BR-AUTH-08 có quy định rõ phải bypass cho dữ liệu công khai không? Hiện DN/NHT bị reject 403 dù spec FR-III-04 UC23 ngụ ý KH công khai phải accessible.
2. **Cổng PLQG inbound cho đào tạo** — Pattern inbound đã chuẩn hoá cho hỏi-đáp/TVCS/HSPL-DN. Có phải spec bỏ sót cho đăng ký đào tạo + HV, hay intentional (chỉ qua CMS internal)?
3. **B10 CT HTPLDN wording edge case** — Khi CT không có Đợt BC nào, có cho phép HOAN_THANH không?
4. **Đào tạo spec drift:**
   - Error code `ERR-CTDT-04` (spec) vs `ERR-STATE-III-01-01` (BE)
   - Reject field `lyDoTuChoi` (spec) vs `ghiChuPheDuyet` (BE)
   - ĐKT state machine 2-state (NHAP/DA_PHAN_PHOI) — không có CHO_DUYET như spec
   - NHCH state machine `KICH_HOAT/VO_HIEU_HOA` (BE) vs `NHAP/CONG_KHAI/AN` (spec line 783)
   - HV ↔ TAI_KHOAN field `taiKhoanId` MUST hay OPTIONAL?

---

## 8. Reference

- **Bug reports mới R11 19:23:** [bug-report-r7-7-6-chuyen-trang-vpd-inbound.md](../bug-reports/dao-tao/bug-report-r7-7-6-chuyen-trang-vpd-inbound.md)
- **Todo modules:** [todo-dao-tao.md](../../../tasks/todo-dao-tao.md) · [todo-bieu-mau.md](../../../tasks/todo-bieu-mau.md) · [todo-ct-htpldn.md](../../../tasks/todo-ct-htpldn.md) · [todo-qtht.md](../../../tasks/todo-qtht.md)
- **Functional reports gần nhất:**
  - Đào tạo: [functional-test-report-r7-7-6-khoa-hoc-r10.md](../functional/dao-tao/functional-test-report-r7-7-6-khoa-hoc-r10.md)
  - Biểu mẫu: [functional-test-report-r7-7-10-bm-r8-lan-8.md](../functional/bieu-mau/functional-test-report-r7-7-10-bm-r8-lan-8.md)
  - CT HTPLDN: [workflow-test-report-r7-6-4-cthtpldn-gd1.md](../workflow/ct-htpldn/workflow-test-report-r7-6-4-cthtpldn-gd1.md) · [workflow-test-report-r7-6-5-cthtpldn-gd2.md](../workflow/workflow-test-report-r7-6-5-cthtpldn-gd2.md)
  - QTHT: [functional-test-report-QTHT-14DM.md](../functional/qtht-danh-muc/functional-test-report-QTHT-14DM.md)

---

*Báo cáo gộp 4 module · Cập nhật 2026-05-11 19:30 sau probe E2E chuyên trang DN/NHT · QA Automation Claude Code MCP*
