# Kế Hoạch Kiểm Thử — SRS-FR-03: Quản lý Đào tạo, Tập huấn (FR-III-01 → FR-III-20 + 3 NEW)

> **Phiên bản:** 1.0 (Phase A re-run)
> **Ngày tạo:** 2026-05-09
> **Phase:** A (BMAD A1 → A7) + Codex review
> **Nguồn dữ liệu:** SRS local `input/srs-v3/srs-fr-03-dao-tao.md` (1267 dòng) + cross-ref `srs-v3.md` Phụ lục B (BR), Phụ lục C (SM-KHOAHOC), `02-thu-tu-module.md` §⑨ FR-03 (dòng 573-633)
> **Notebook secondary:** ID `4dd0675e-...` (cho VV transitions / quy trình chi tiết) — query khi spec mơ hồ.

> **MODE NOTE:** Local SRS ưu tiên (NotebookLM secondary cho clarification). Mọi BR/SM phải QUOTE SRS line. Permission TC tách file riêng theo pattern DN. SPEC-CLARIFY ticket khi gap.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **22 FR** thuộc nhóm FR-III (FR-III-01 → FR-III-20 + FR-III-NEW-01..03)
- **5 SCR:** SCR-III-01 (CTĐT) · SCR-III-02 (Chi tiết KH 6 tabs) · SCR-III-03 (Bài giảng) · SCR-III-04 (NHCH + Đề KT 2 tabs) · SCR-III-05 (GV)
- **State machine SM-KHOAHOC:** 9 trạng thái (DU_THAO, CHO_DUYET, DA_DUYET, DA_CONG_KHAI, DANG_DIEN_RA, DA_KET_THUC, CHO_DUYET_KQ, HOAN_THANH, HUY) + 11 transitions + AT-01/AT-02 (auto)
- **Cấu trúc 2 cấp:** CTĐT (parent) → KHOA_HOC (children) — soft-delete cascade rule, edit-after-approval rule
- **2 hình thức:** TRUC_TUYEN / TRUC_TIEP — quy trình tương đương
- **Luồng phê duyệt 2 lần:** (1) Duyệt KH/CTĐT trước thực thi · (2) Duyệt KQ sau thực thi — cùng cấp (BR-AUTH-05)
- **Entity:** 10 owned (CHUONG_TRINH_DAO_TAO, KHOA_HOC, BAI_GIANG, NGAN_HANG_CAU_HOI, DE_KIEM_TRA, KET_QUA_DAO_TAO, CHUNG_NHAN, GIANG_VIEN, DANG_KY_DAO_TAO, DE_XUAT_DAO_TAO) + 3 referenced (TAI_KHOAN, DON_VI, DANH_MUC)

### 1.2 Danh sách 13 file TC (mapping FR → file)

| # | File | FR / UC chính | SCR / Entity | Estimate TC |
|---|------|---------------|--------------|------------:|
| 01 | `01-TC-KH-nam-dao-tao.md` | FR-III-14/15/16 (UC33/34/35 — Lập KH năm + Phê duyệt + Công khai) | SCR-III-01 Tab "Đề xuất" workflow + KE_HOACH_DAO_TAO | 27 |
| 02 | `02-TC-CTDT-quan-ly.md` | FR-III-01/02 (UC20/21 — CRUD + Search CTĐT) | SCR-III-01 main + CHUONG_TRINH_DAO_TAO | 30 |
| 03 | `03-TC-de-xuat-dao-tao.md` | FR-III-13 (UC32 — Đề xuất từ DN/NHT) | SCR-III-01 Tab "Đề xuất" + DE_XUAT_DAO_TAO | 14 |
| 04 | `04-TC-lich-hoc.md` | Tab "Lịch học & Điểm danh" SCR-III-02 + auto-transition KH theo ngày | SCR-III-02 Tab 3 + buổi học | 16 |
| 05 | `05-TC-khoa-hoc-quan-ly.md` | FR-III-05 KH part (UC24 phần KH) + SM-KHOAHOC 11 transitions + AT-01/02 | SCR-III-02 Tab Thông tin + KHOA_HOC | 31 |
| 06 | `06-TC-dang-ky-dao-tao.md` | FR-III-03/04 (UC22/23 — QL ĐK + ĐK tham gia) | SCR-III-02 Tab Học viên + DANG_KY_DAO_TAO | 18 |
| 07 | `07-TC-diem-danh-ket-qua.md` | FR-III-05 KQ part + FR-III-17 (UC36 — Ghi nhận KQ) | SCR-III-02 Tab Lịch học + Tab KQ kiểm tra + KET_QUA_DAO_TAO | 27 |
| 08 | `08-TC-cong-bo-ket-qua.md` | FR-III-18/19 (UC37/38 — Phê duyệt KQ + Công bố + cấp chứng nhận) | SCR-III-02 Tab Chứng nhận + CHUNG_NHAN | 19 |
| 09 | `09-TC-bai-giang-kho-tai-lieu.md` | FR-III-07/08 (UC26/27 — Quản lý + tìm kiếm Bài giảng) | SCR-III-03 + BAI_GIANG | 17 |
| 10 | `10-TC-NHCH-de-kiem-tra.md` | FR-III-09/10 (UC28/29) + FR-III-NEW-01/02/03 (Tạo + QL + Phân phối Đề KT) | SCR-III-04 2 tabs + NGAN_HANG_CAU_HOI + DE_KIEM_TRA | 27 |
| 11 | `11-TC-giang-vien.md` | FR-III-11/12 (UC30/31 — Quản lý + tìm kiếm GV) | SCR-III-05 + GIANG_VIEN | 13 |
| 12 | `12-TC-xuat-tai-lieu-ky-so.md` | FR-III-20 (UC mới — Xuất docx/PDF ký số CTDT) | SCR-III-01 action + Export | 7 |
| 13 | `13-TC-permission-matrix.md` | Permission matrix-driven (cross 4-cấp × 11 role × 13 entity owned) | Cross-screen | 17 |
| (audit) | `14-REVIEW-edge-case-hunter.md` | A4 output | — | +N edge |
| (audit) | `15-trace-matrix.md` | A5 output | BR/SM/AC/Error/Permission ↔ TC | — |
| (audit) | `16-quality-review.md` | A6 output | quality score + fill gap | — |
| (audit) | `17-a7-filter.md` | A7 output | LOẠI/SỬA TC theo môi trường thực | — |

**Tổng estimate sau A1-A3:** ~263 TC active. A4 thêm edge inline, A6 fill gap, A7 LOẠI/SỬA. Final dự kiến 260-265 TC.

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username | Dùng cho |
|------|-----|----------|----------|
| QTHT | — | qtht_01 | Read-only entity FR-03 (per Permission Matrix) |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD CTĐT/KH/Đề xuất/NHCH/GV scope TW + Trình duyệt + Ghi KQ |
| CB_NV_BN | BN | cb_nv_bn_01 | CRUD scope BN |
| CB_NV_DP | ĐP | cb_nv_dp_01 | CRUD scope ĐP |
| CB_PD_TW | TW | cb_pd_tw_01 | Phê duyệt KH/CTĐT + Phê duyệt KQ cùng cấp TW |
| CB_PD_BN | BN | cb_pd_bn_01 | Phê duyệt cùng cấp BN |
| CB_PD_DP | ĐP | cb_pd_dp_01 | Phê duyệt cùng cấp ĐP |
| TVV/CG | — | tvv_01 / cg_01 | Đăng ký KH (UC23) + Học viên |
| NHT | — | nht_01 | Đề xuất đào tạo (UC32) qua Cổng PLQG + Đăng ký KH |
| DN | — | dn_01 | Cử HV đăng ký KH (UC23) qua Cổng PLQG |
| Permission test | — | qtht_03 / cb_nv_*_03 | Negative permission (TC permission tách) |

> Reference: [input/users.csv](../../../input/users.csv), [output/permission-matrix.md](../../permission-matrix.md), [output/permission-matrix-by-fr.md](../../permission-matrix-by-fr.md)

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (14 BR liên quan — quote từ srs-fr-03 §6 dòng 1241-1262)

| Mã | Quy tắc | Áp dụng FR | TC áp dụng |
|----|---------|-----------|-----------|
| BR-AUTH-01 | Xác thực bắt buộc | Toàn nhóm III | Precondition mọi TC |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB NV trình → CB PD cùng cấp duyệt) | FR-III-15, FR-III-18 | UC34/UC37 negative cross-cấp |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | FR-III-01, FR-III-02, FR-III-06 | UC20/21/25 cross-unit isolation |
| BR-DATA-01 | Soft delete (`is_deleted = 1`) | FR-III-01, FR-III-09, FR-III-NEW-02 | UC20/UC28 DELETE |
| BR-DATA-02 | Multi-tenant scoping | FR-III-01 | UC20 list scope |
| BR-DATA-03 | 7 common fields | FR-III-01, FR-III-07, FR-III-09 | Verify created_at/updated_at... mọi UC CUD |
| BR-DATA-04 | Auto-gen mã (CTDT-{DON_VI}-{YYYY}-{SEQ}, KH-{YYYYMMDD}-{SEQ}) | FR-III-01, FR-III-19 | UC20/UC38 verify auto-code format |
| BR-DATA-05 | Audit trail không xóa/sửa | Toàn nhóm III (CUD) | Mọi TC CUD verify AUDIT_LOG |
| BR-DATA-06 | Export Excel max 10k rows | FR-III-01 | UC20 export boundary |
| BR-DATA-07 | Pagination default 20, max 100 | FR-III-01, FR-III-02, FR-III-06 | UC20/21/25 pagination |
| BR-FLOW-03 | Không sửa/xóa sau phê duyệt | FR-III-01, FR-III-15, FR-III-18 | UC20 UPDATE/DELETE khi DA_DUYET |
| BR-FLOW-04 | Từ chối bắt buộc nhập lý do (≥10 ký tự) | FR-III-15, FR-III-18 | UC34/UC37 negative TU_CHOI no reason |
| BR-FLOW-05 | Công khai qua API Cổng PLQG | FR-III-16 | UC35 verify endpoint outbound |
| BR-NOTIF-01 | Thông báo phê duyệt (email + in-app) | FR-III-14 | UC33/UC34 notification check |

### 2.2 State Machine SM-KHOAHOC (9 state, 11 transitions)

> Source: srs-fr-03 §5 dòng 1218-1237 + 02-thu-tu-module.md §⑨ dòng 619-631 (table)

```
[*] → DU_THAO        : CB NV tạo mới
DU_THAO → CHO_DUYET  : CB NV [Gửi duyệt] (guard: ≥1 bài giảng)
CHO_DUYET → DA_DUYET : CB PD cùng cấp [Duyệt] (BR-AUTH-05)
CHO_DUYET → DU_THAO  : CB PD [Từ chối] (BR-FLOW-04, ly_do ≥10 ký tự)
DA_DUYET → DA_CONG_KHAI : CB NV toggle la_cong_khai (per 02-thu-tu-module dòng 617 — fix mâu thuẫn nội bộ SRS)
DA_CONG_KHAI → DANG_DIEN_RA : AT auto khi đến ngay_bat_dau hoặc CB NV [Bắt đầu]
DANG_DIEN_RA → DA_KET_THUC : AT auto khi qua ngay_ket_thuc hoặc CB NV [Kết thúc]
DA_KET_THUC → CHO_DUYET_KQ : CB NV [Trình KQ] (AT-02; guard: điểm danh + điểm KT đầy đủ)
CHO_DUYET_KQ → HOAN_THANH : CB PD [Duyệt KQ + Cấp chứng nhận]
CHO_DUYET_KQ → DA_KET_THUC : CB PD [Từ chối KQ] (BR-FLOW-04)
DU_THAO|CHO_DUYET|DA_DUYET → HUY : CB NV (guard: chưa có HV / chưa diễn ra)
```

> ⚠️ **SPEC-CLARIFY-DT-01:** SRS Phụ lục C.2 (srs-v3.md dòng 4178-4193) **thiếu** transition `DA_DUYET → DA_CONG_KHAI` — diagram skip thẳng `DA_DUYET → DANG_DIEN_RA`. Theo logic nghiệp vụ + schema (`la_cong_khai` flag) + 02-thu-tu-module dòng 617, transition đúng: `DA_DUYET → DA_CONG_KHAI` do CB NV kích hoạt. Cần BA xác nhận.

**Auto-transition (per srs-fr-03 §1 dòng 62-63):**
- AT-01: CB NV [Gửi phê duyệt] → DU_THAO → CHO_DUYET (manual trigger nhưng hệ thống tự đổi state)
- AT-02: CB NV [Trình duyệt KQ] → DA_KET_THUC → CHO_DUYET_KQ

### 2.3 Error Codes (trích từ srs-fr-03 §2 cho 22 FR)

Mỗi UC có Error Handling table riêng. Tổng quan:

| Mã | Mô tả | Severity | UC nguồn |
|----|-------|----------|----------|
| ERR-CTDT-01 | Tên CTĐT trống | ERROR | UC20 |
| ERR-CTDT-02 | Ngày KT ≤ ngày BĐ | ERROR | UC20 |
| ERR-CTDT-03 | Xóa CTĐT có khóa học | ERROR | UC20 |
| ERR-CTDT-04 | Sửa CTĐT đã duyệt | ERROR | UC20 |
| ERR-KH-01 | Tên KH trống | ERROR | UC24 |
| ERR-KH-02 | Ngày KT ≤ ngày BĐ KH | ERROR | UC24 |
| ERR-KH-03 | KH thiếu CTĐT cha (FK fail) | ERROR | UC24 |
| ERR-KH-04 | Sửa KH đã DA_DUYET | ERROR | UC24 |
| ERR-KH-05 | Trình duyệt KH không có bài giảng | ERROR | SM-KHOAHOC guard |
| ERR-DK-01 | ĐK quá so_luong_toi_da | ERROR | UC23 |
| ERR-DK-02 | ĐK trùng (same hoc_vien_id + khoa_hoc_id) | ERROR | UC23 |
| ERR-DK-03 | ĐK khi KH chưa DA_CONG_KHAI | ERROR | UC23 PRE-02 |
| ERR-KQ-01 | Điểm KT ngoài 0-10 | ERROR | UC36 |
| ERR-KQ-02 | Trình duyệt KQ thiếu điểm danh | ERROR | UC36 SM guard |
| ERR-PD-01 | Phê duyệt khác cấp (BR-AUTH-05 vi phạm) | ERROR | UC34/UC37 |
| ERR-PD-02 | Từ chối thiếu lý do (BR-FLOW-04 vi phạm) | ERROR | UC34/UC37 |
| ERR-BG-01 | Upload bài giảng > 20MB | ERROR | UC26 |
| ERR-BG-02 | Loại file không hợp lệ (chỉ PPTX/PDF + link YouTube) | ERROR | UC26 |
| ERR-NHCH-01 | Câu hỏi thiếu đáp án đúng | ERROR | UC28 |
| ERR-DEKT-01 | Đề KT 0 câu | ERROR | UC NEW-01 |
| ERR-GV-01 | GV không có chuyên môn | ERROR | UC30 |
| ERR-EXP-01 | Export > 10k rows | WARNING | UC20 |
| ERR-EXP-02 | Xuất ký số fail (BHXH/CA service down) | ERROR | UC mới FR-III-20 |

> Chi tiết error code per-UC ở từng file 01..13.

---

## 3. Permission Matrix (cross-cấp × 11 role)

> Source: [output/permission-matrix.md](../../permission-matrix.md) — section "Đào tạo, Tập huấn"

| Entity | Action | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | TVV | NHT | DN |
|--------|--------|------|----------|----------|----------|----------|----------|----------|-----|-----|----|
| CTDT | Create | — | TW | BN | ĐP | — | — | — | — | — | — |
| CTDT | Read | RW | scope-TW | scope-BN | scope-ĐP | scope-TW | scope-BN | scope-ĐP | public | public | public |
| CTDT | Update | — | scope-own | scope-own | scope-own | — | — | — | — | — | — |
| CTDT | Delete (soft) | — | scope-own | scope-own | scope-own | — | — | — | — | — | — |
| KHOA_HOC | Create | — | TW | BN | ĐP | — | — | — | — | — | — |
| KHOA_HOC | Approve | — | — | — | — | TW | BN | ĐP | — | — | — |
| KHOA_HOC | Public_view | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| DANG_KY | Create (self) | — | — | — | — | — | — | — | self | self | self (DN cử HV) |
| DANG_KY | Approve | — | scope-own | scope-own | scope-own | — | — | — | — | — | — |
| KET_QUA | Create | — | scope-own | scope-own | scope-own | — | — | — | — | — | — |
| KET_QUA | Approve | — | — | — | — | TW | BN | ĐP | — | — | — |
| BAI_GIANG | CRUD | — | TW | BN | ĐP | — | — | — | — | — | — |
| NHCH/Đề KT | CRUD | — | TW | BN | ĐP | — | — | — | — | — | — |
| GV | CRUD | — | TW | BN | ĐP | — | — | — | — | — | — |
| DE_XUAT | Create | — | — | — | — | — | — | — | — | ✓ (NHT) | ✓ (DN) |
| DE_XUAT | Receive | — | scope-own | scope-own | scope-own | — | — | — | — | — | — |

> Negative TC test ở `13-TC-permission-matrix.md`.

---

## 4. Test Strategy

### 4.1 Phân loại TC

- **Functional / Happy path:** Mỗi UC có TC nominal flow, các trường nhập đầy đủ, role đúng → kết quả thành công.
- **Negative / Error:** Trigger mỗi error code (ERR-*) qua input invalid hoặc precondition vi phạm.
- **Boundary (BVA):** Số ký tự min/max, ngày BĐ/KT, số HV tối đa, file size 20MB.
- **State Machine:** Mọi transition + invalid transition (state hiện tại không cho action) cho SM-KHOAHOC.
- **Permission:** Role mismatch + cấp mismatch (BR-AUTH-05/08) + scope cross-unit isolation.
- **Cross-module:** CTĐT cha bị xóa → KH con; Lĩnh vực PL từ FR-10; GV từ FR-04; DN cử HV từ FR-07.
- **Edge case:** A4 bổ sung — concurrency (2 CB NV cùng sửa CTĐT), upload file đặc biệt (file Unicode tên, file 20MB), DA_CONG_KHAI sau ngày BĐ, cancel KH đã có ĐK.

### 4.2 Naming convention

```
TC-{FR}-{type}-{seq:03d}: {tên ngắn}
```

- FR: `CTDT`, `KH`, `DK`, `KQ`, `BG`, `NHCH`, `DEKT`, `GV`, `KH-NAM`, `DEXUAT`, `XUAT`, `PERM`
- Type: `H` (happy), `N` (negative), `B` (boundary), `S` (state), `P` (permission), `X` (cross-module), `E` (edge — A4 added)

Ví dụ: `TC-CTDT-H-001`, `TC-KH-S-007`, `TC-DK-N-003`.

### 4.3 Test data

- **CTĐT seed:** 3 record DA_DUYET ở 3 cấp (TW/BN/ĐP), 1 DU_THAO TW
- **Khóa học seed:** Mỗi state SM-KHOAHOC có ≥1 record (9 state × 1) + thêm 1 KH DANG_DIEN_RA có ≥3 HV để test điểm danh
- **Bài giảng seed:** 5 PPTX + 3 PDF + 2 YouTube (đa Lĩnh vực PL)
- **NHCH seed:** 50 câu hỏi (đa loại), 3 Đề KT (10/20/30 câu)
- **GV seed:** 5 GV TVV active (từ FR-04)
- **HV seed:** 10 DN (FR-07) × ≥1 HV → 10+ DANG_KY
- **Đề xuất seed:** 3 đề xuất MOI (NHT 1 + DN 2)

> Setup seed cụ thể tại `input/data/seed-fixture.yaml` section dao-tao + flow-module.md §Phụ lục 2.

---

## 5. Risk & Assumption

| Risk | Mitigation |
|------|-----------|
| SPEC-CLARIFY-DT-01 SM transition `DA_DUYET → DA_CONG_KHAI` | Test theo logic + flag `la_cong_khai`; ghi SPEC-CLARIFY ticket |
| Mâu thuẫn nội bộ SRS (DA_CONG_KHAI vắng trong Phụ lục C) | Quote 02-thu-tu-module dòng 617 + schema flag |
| AT-01/AT-02 manual hay auto thực sự? | Per SRS dòng 62-63 — manual trigger nhưng state đổi tự động |
| FR-III-20 Xuất ký số (BHXH/CA service) | Mock + verify outbound API call |
| 5 SCR consolidation v2.1 (12→5) | TC tham chiếu MH-03.* gốc nếu cần |

**Assumption:**
- OTP login `666666` cho mọi role
- Permission Matrix đã verified (output/permission-matrix.md)
- BR-DATA-06 cap 10k rows áp dụng mọi export

---

## 6. Liên kết

- SRS chính: [`srs-fr-03-dao-tao.md`](../../../input/srs-v3/srs-fr-03-dao-tao.md)
- Cross-ref: [`srs-v3.md`](../../../input/srs-v3/srs-v3.md) Phụ lục B (BR), Phụ lục C (SM-KHOAHOC)
- Thứ tự nghiệp vụ: [`02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) §⑨ dòng 573-633
- Permission: [`permission-matrix.md`](../../permission-matrix.md), [`permission-matrix-by-fr.md`](../../permission-matrix-by-fr.md)
- Sibling references: [`output/test-cases/CG-TVV/`](../CG-TVV/), [`output/test-cases/QTHT/`](../QTHT/), [`output/test-cases/doanh-nghiep/`](../doanh-nghiep/)
- Plan tổng: [`tasks/detailed-tc/plan.md`](../../../tasks/detailed-tc/plan.md), [`tasks/detailed-tc/todo.md`](../../../tasks/detailed-tc/todo.md)
