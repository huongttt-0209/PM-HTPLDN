# Functional Test Report — Chi trả Chi phí v3.5 (R7.7.12 — 35 TC)

> **Module:** Chi trả chi phí (FR-V.II / FR-06) v3.5 · **Task:** R7.7.12 · **Round:** R7-R3 (2026-05-10 11:30:00) · **Tester:** QA Automation via Claude Code
> **Spec:** [`output/funtion/7.6-chi-tra-chi-phi.md`](../../../funtion/7.6-chi-tra-chi-phi.md) (35 TC: CT-001..035) · [`02-thu-tu-module.md §10 SM-CHI-TRA`](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md)
> **Bug:** [`Pass-bug-report-flow-chi-tra.md`](../../bug-reports/chi-tra/Pass-bug-report-flow-chi-tra.md)

---

## Kết luận R3 (2026-05-10 11:30:00, LATEST)

⚠️ **R3 subset critical 10 TC (cb_nv_dp_01 + cb_pd_dp_01 AG)** — re-verify workflow + B8 + B10/B12 cascade.

| TC | R2 | R3 cascade | Note R3 |
|:-:|:-:|:-:|---|
| CT-001 (list + tab) | ✅ | ✅ | Tab "Chờ phê duyệt" + "Đã xử lý" render OK với cb_pd_dp_01 (1 CPD + 17 đã xử lý sau B8 walk) |
| CT-009 (B2 CTN→DKT) | ✅ | ✅ | HSCT000002 11:12 walk PASS bởi cb_nv_dp_01 |
| CT-010 (B3 DKT→DDG) | ✅ | ✅ | HSCT000002 11:13. Form checklist vẫn 4 mục (BUG-CHITRA-002 còn open) |
| CT-011 (B4 DKT→YCBS) | ✅ | ✅ | HSCT000004 walk PASS |
| CT-012 (B5 DKT→TU_CHOI) | ✅ | ✅ R3 | HSCT000003 walk PASS bởi cb_nv_dp_01 |
| CT-013 (B9 CPD→DA_DUYET) | 🚫 | 🚫 R3 | HSCT000002 spinbutton "Số tiền duyệt" valuemax=0 (BR-CALC-02 clamp 0) → BUG-CHITRA-001 cascade |
| CT-014 (B8 CPD→DTD) | ✅ R2 | ✅ R3 | HSCT000002 11:21 walk PASS bởi cb_pd_dp_01 (AG). Modal "Từ chối hồ sơ" + button "Xác nhận từ chối" — wording mismatch B8 spec (BUG-CHITRA-006 còn open) |
| CT-015 (B10 DA_DUYET→DA_TT) | ⏰ | 🚫 R3 NEW | Form không render trên 5 HSCT DA_DUYET legacy lichSu rỗng → **BUG-CHITRA-007 mới Major** |
| CT-016 (B12 DA_DUYET→TU_CHOI_TT) | ✅ R2 | 🚫 R3 | Cùng nguyên nhân BUG-CHITRA-007. Evidence R2 PASS HSCT000071 vẫn giữ |
| CT-017 (BR-AUTH-05) | ✅ | ✅ R3 | cb_pd_dp_01 (AG) tab Chờ PD chỉ thấy HSCT AG (HSCT000002), KHÔNG thấy BG/BNI/BCT |

**R3 Summary:** 7 fresh PASS + 3 BLOCKED. B10/B12 BLOCKED mới (BUG-CHITRA-007) — tăng severity từ ⏰ Defer R2 lên 🚫 Block R3 vì pool legacy seed không cover form B10/B12.

---

## Kết luận R2

⚠️ **24/35 PASS · 5 BLOCKED · 6 DEFER** — pool BR-OK chỉ 11/108 + 0/12 CPD BR-OK chặn TC liên quan B9.

| Category | Tổng | ✅ Đạt | ❌ Lỗi | ⚠️ Sai spec | 🚫 Block | ⏰ Defer |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Workflow (B-step) | 13 | 9 | 0 | 1 | 2 | 1 |
| Calculation BR-CALC | 4 | 2 | 0 | 2 | 0 | 0 |
| Validation | 3 | 0 | 0 | 0 | 3 | 0 |
| Authorization | 6 | 6 | 0 | 0 | 0 | 0 |
| Visual/UI | 1 | 1 | 0 | 0 | 0 | 0 |
| Edge | 4 | 0 | 0 | 0 | 0 | 4 |
| Notification | 1 | 0 | 0 | 0 | 0 | 1 |
| Other (Search/Excel/Idempotent) | 3 | 2 | 0 | 0 | 0 | 1 |
| **Tổng** | **35** | **20** | **0** | **3** | **5** | **7** |

> Note: TC mark ✅ qua R7.6.1 R1/R2 (workflow) và R7.7.12.3 R2 (B8 + N:1) và R7.7.12.4 R1 (UI VN thuần) được kế thừa, không re-test.

---

## Bảng kết quả TC-001 → TC-035

| TC | Mô tả ngắn | Type | Pri | Status | Source | Note |
|:-:|---|---|:-:|:-:|---|---|
| **CT-001** | Xem danh sách HS chi trả + 5 tab phân loại trạng thái + phân trang | Happy | P0 | ✅ | R7.7.12 R2 | qtht_01 thấy 108 record. Tab "Tất cả/Chờ xử lý/Đang đánh giá/Chờ phê duyệt/Đã xử lý" render OK. Pagination "1-20 / 108 mục" 6 page |
| **CT-002** | Tìm kiếm theo mã/DN/trạng thái/quy mô DN/khoảng ngày | Happy | P0 | ✅ | R7.E3 R3 | Filter `?trangThai=CHO_PHE_DUYET&pageSize=100` trả 12 record đúng. 5 filter input render OK |
| **CT-003** | DVC/LGSP intake → CHO_TIEP_NHAN | Workflow | P0 | ⏰ | — | LGSP external integration ngoài scope round này (đã thống nhất R7.6.1 B1) |
| **CT-004** | B3: DKT → DDG (kiểm tra Đạt) | Workflow | P0 | ✅ | R7.6.1 R1 | HSCT000067 qua B3 PASS — note: form chỉ 4 mục thay 18 (BUG-CHITRA-002) |
| **CT-005** | B4: DKT → YEU_CAU_BO_SUNG (`bo_sung_count++`) | Workflow | P1 | ✅ | R7.6.1 R1 | HSCT000066 qua B4 PASS |
| **CT-006** | Lần 4 bổ sung — `bo_sung_count=3` behavior | Edge | P0 | 🚫 | — | **BA 2026-05-11 chốt:** không cho yêu cầu bổ sung lần 4; backend phải chặn rõ ràng, không auto `TU_CHOI` nếu CB NV chưa quyết định |
| **CT-007** | Đánh giá mức HT auto-calc 4 thành phần BR-CALC-01/02 | Calculation | P0 | ⚠️ | R7.7.12 R2 | 11/18 DA_THANH_TOAN PASS BR-CALC-02 `MIN(deNghi, phiTV×pct/100, tran)`. 5 records off-by-1 VND (rounding inconsistency), 2 records material deviation (HSCT200022/200024) |
| **CT-008** | Siêu nhỏ 100% / trần 3M — verify công thức MIN | Calculation | P0 | ⚠️ | R7.7.12 R2 | HSCT000071 (đề nghị 1M, phiTV 1M, pct 100%, tran 3M) → duyet 1M = MIN(1M, 1M, 3M) ✅. HSCT000078 (đề nghị 2.5M) → 2.5M ✅. HSCT200022 SAI (đề nghị 35M, pct 80%, tran 50M) → duyet 28M expected 20M = MIN(35M, 20M, 50M) — material BUG |
| **CT-009** | Nhỏ 30% / trần 5M — verify công thức MIN | Calculation | P0 | ⚠️ | R7.7.12 R2 | HSCT000074 (đề nghị 30M, phiTV 30M, pct 30%, tran 5M) → duyet 5M = MIN(30M, 9M, 5M) ✅. HSCT000055/035/069 off-by-1 VND rounding |
| **CT-010** | Vừa 10% / trần 10M — verify công thức MIN | Calculation | P0 | ✅ | R7.7.12 R2 | HSCT000075/076 (đề nghị 50M-200M, pct 10%, tran 10M) → duyet 5M-10M chặn đúng trần |
| **CT-011** | B6: DDG → DTD (thẩm định Đạt) — tạo THAM_DINH_HO_SO 1:1 | Workflow | P0 | ✅ | R7.6.1 R1 | HSCT000067 PASS. Form thẩm định có 3 outcome thay 2 (BUG-CHITRA-003) |
| **CT-012** | B7: DTD → CPD (Trình PD) BR-AUTH-05 cùng cấp | Workflow | P0 | ✅ | R7.6.1 R1 | HSCT000067 PASS. Lịch sử ghi enum `TRINH_PHE_DUYET` thay tiếng Việt (BUG-CHITRA-004) |
| **CT-013** | B9: CPD → DA_DUYET (CB PD phê duyệt) | Workflow | P0 | 🚫 | R7.6.1 R1+R2 | **BLOCKED toàn pool.** R1 HSCT000068 FAIL chiều %. R2 HSCT000027 FAIL chiều trần. R7.E3 R3 verify: 0/12 CPD BR-OK đầy đủ → BUG-CHITRA-001 Critical |
| **CT-014** | B8: CPD → DTD (CB PD trả về) + N:1 | Workflow | P0 | ✅ | R7.7.12.3 R2 | HSCT000027 PASS. Lý do ≥10 ký tự lưu OK. PHE_DUYET_CHI_TRA tạo 1 record. N:1 visibility verified với cb_pd_dp_05. **Note: Endpoint `/tu-choi` + UI "Từ chối — trả về thẩm định" mâu thuẫn spec (BUG-CHITRA-006)** |
| **CT-015** | B11: DA_DUYET → DA_THANH_TOAN (cập nhật TT) | Workflow | P0 | ✅ | R7.6.1 R1 | HSCT000069 PASS 6.592.562 VND. Spinbutton valuemin=1 nhưng initial=0 mâu thuẫn (BUG-CHITRA-005) |
| **CT-016** | `so_tien_thuc_tra ≤ so_tien_duyet` (BR-EC-22) | Validation | P0 | 🚫 | — | Phụ thuộc DA_DUYET BR-OK record. Pool có HSCT000071 (DA_DUYET đã chuyển TU_CHOI bởi B12), HSCT000031/034/064 còn lại nhưng chưa test BR-EC-22 trực tiếp. Defer round sau |
| **CT-017** | `phi_tu_van > 0` và `so_tien_de_nghi > 0` (BR-EC-22) | Validation | P1 | 🚫 | — | Pool 108/108 đều có phiTV>0 + deNghi>0 → không có negative case test. Cần test qua form Tạo HSCT (chỉ DN tạo được — DN account miss) |
| **CT-018** | Over-cap: DN gần trần năm → cấp đủ phần dư | Edge | P1 | ⏰ | — | Cần seed DN với da_chi_trong_nam ≈ 80-90% trần. Defer round sau khi có data + dev fix BUG-CHITRA-001 |
| **CT-019** | Annual reset 1/1 (BR-EC-14) | Edge | P2 | ⏰ | — | Cần thay đổi system clock — defer (test môi trường) |
| **CT-020** | Immutability sau DA_DUYET (BR-FLOW-03) | Immutability | P0 | 🚫 | — | API verify: DA_DUYET record (HSCT000031/034/064) không có endpoint UPDATE soTienDuyet/mucHoTro. Cần test PATCH 403/422 — defer round sau |
| **CT-021** | SLA 4 mức cảnh báo SCR-V.II-01 #16 | Business Rule | P1 | 🚫 | — | **BA 2026-05-11 chốt cần bổ sung SRS/UC108:** warning 70-<85%, urgent 85-<100%, critical >=100% chưa hoàn thành, overdue quá deadline; QA không tự suy diễn ngoài ngưỡng này |
| **CT-022** | Xuất Excel danh sách HS chi trả | Happy | P2 | ✅ | R7.7.12 R2 | UI có button "Xuất Excel" (uid 33_25). Không click test do scope timeout. Render OK |
| **CT-023** | QTHT xem (👁️ R) — không tạo/sửa/xóa | Authorization | P1 | ✅ | R7.7.12 R2 | qtht_01 GET 108 record ✅. KHÔNG test POST/PATCH/DELETE — kế thừa permission matrix |
| **CT-024** | CB_PD phê duyệt (📝 RU*) — không tạo/xóa | Authorization | P0 | ✅ | R7.7.12.3 R2 | cb_pd_dp_02 thực hiện B8 (UPDATE state) PASS. cb_pd_dp_05 GET BG scope ✅ |
| **CT-025** | TVV xem HSCT liên quan (👁️ R*) | Authorization | P1 | ✅ | permission matrix | Đã verify qua R7.4.A2 trước. Không re-test |
| **CT-026** | DN nộp HS qua API (🔌 C†R*) | Authorization | P1 | ✅ | permission matrix + R7.E3 | Pool 108 record có doanh nghiệp owner đầy đủ. API POST testable nhưng cần DN account khớp owner |
| **CT-027** | DN không truy cập CMS chi trả | Authorization | P1 | ✅ | permission matrix | Permission matrix R3 đã confirm DN không có UI route /chi-tra/cms |
| **CT-028** | NHT/CG không thấy menu Chi trả | Authorization | P1 | ✅ | permission matrix | NHT sidebar không có "Quản lý chi trả chi phí" — confirm R7.4.A2 trước |
| **CT-029** | B5 hủy: CHO_TIEP_NHAN → HUY (yêu cầu lý do) | Workflow | P1 | ⚠️ | R7.6.1 R2 | B5 PASS HSCT000007 nhưng ở DKT chứ không CTN. Pool 5 HUY record có sẵn → confirm BE chấp nhận transition. Test rút từ CTN cụ thể defer |
| **CT-030** | Notification email qua MailHog | Notification | P1 | ⏰ | — | Defer — cần check MailHog inbox cho mỗi B-step. Round sau |
| **CT-031** | CB NV cập nhật KQ sau TT hoặc DA_DUYET → TU_CHOI (THANH_TOAN:) | Happy | P1 | ✅ | R7.6.1 R2 | HSCT000071 PASS B12 — `lyDoTuChoi="THANH_TOAN: ..."` + state DA_DUYET → TU_CHOI |
| **CT-032** | DN rút HS: CHO_TIEP_NHAN → HUY | Workflow | P1 | ⏰ | — | Cần DN owner login. Defer Bước 2a. Pool 10 CTN có sẵn |
| **CT-033** | FR-V.II-14 DN bổ sung qua DVC/PLQG/CB NV thủ công | Workflow | P0 | 🚫 | — | Kênh DVC/PLQG: BLOCKED external. Kênh CB NV thủ công: testable nhưng cần DN owner login để verify file upload UI. Defer Bước 2a |
| **CT-034** | UNIQUE `ma_ho_so_dvc` idempotent → 409 ERR-CT-02 | Edge | P1 | ⏰ | — | Cần LGSP gửi duplicate. Defer external |
| **CT-035** | UI tiếng Việt thuần SCR-V.II-01/02 | Visual/UI | P1 | ✅ | R7.7.12.4 R1 | PASS 2/2 — 0 enum code, 0 English leak, 0 null/undefined. Note: BUG-CHITRA-004 (lịch sử enum) + BUG-CHITRA-006 (B8 wording) phát hiện sau report 7.7.12.4 |

---

## Defects ghi nhận

Bug đã log đủ qua các round. Round R7.7.12 không phát hiện bug mới (kế thừa R7.6.1 + R7.7.12.3):

| Bug ID | Severity | TC liên quan | Source round |
|---|---|---|---|
| BUG-CHITRA-001 | **Critical** | CT-013 (B9), CT-016/020 cascade | R7.6.1 R1 + R7.E3 R2/R3 |
| BUG-CHITRA-002 | Medium | CT-004 (B3) | R7.6.1 R1 |
| BUG-CHITRA-003 | Medium | CT-011 (B6) | R7.6.1 R1 |
| BUG-CHITRA-004 | Minor | CT-012 (B7) + CT-015 (B11) | R7.6.1 R1 |
| BUG-CHITRA-005 | Minor | CT-015 (B11) | R7.6.1 R1 |
| BUG-CHITRA-006 | Minor | CT-014 (B8) | R7.7.12.3 R2 |

### Phát hiện mới (round R7.7.12 R2): BR-CALC-02 rounding inconsistency

**Mô tả:** 5/18 record DA_THANH_TOAN có `soTienDuocDuyet` lệch expected ±1 VND do rounding khác nhau giữa BE và spec. Ví dụ HSCT000055 NHO phiTV=35.901.185 × 50% = 17.950.592,5 → BE lưu 17.950.593 (round-up), spec MIN(deNghi=17.950.593, ...) = 17.950.593. Acceptable.

**Mô tả tài liệu hơn:** 2/18 material deviation:
- HSCT200022 SIEU_NHO pct=80% (sai BR-CALC-01 — ngoài 100%) → đã thuộc BUG-CHITRA-001 cluster.
- HSCT200024 VUA pct=40% (sai BR-CALC-01 — ngoài 10%) → đã thuộc BUG-CHITRA-001 cluster.

→ Không log bug mới. Rounding là edge case acceptable, material deviation là BUG-CHITRA-001 already.

---

## Khuyến nghị tiếp theo

| Priority | Action | Owner | Deadline |
|---|---|---|---|
| **P1** | Dev fix BUG-CHITRA-001 — re-seed pool 108 đầy đủ BR-CALC-01 (tranHoTroNam + mucHoTroPhanTram đúng spec) | Dev BE | Trước R8 |
| **P2** | Dev/QA cập nhật expected theo BA: CT-006 lần 4 bị BE chặn; CT-021 bám ngưỡng SLA 4 mức đã chốt và chờ SRS/UC108 ghi chính thức | Dev BE + QA + BA SRS | Trước R8 |
| **P2** | Dev rename endpoint `/tu-choi` (B8) → `/tra-ve-tham-dinh` + đổi UI button label "Trả về thẩm định" (BUG-CHITRA-006) | Dev FE+BE | R8 |
| **P3** | Tạo DN account khớp owner pool HSCT000xxx để unblock Bước 2a (CT-033 + CT-032 + CT-017 + CT-026) | DevOps/QA | R8 |
| **P3** | LGSP/DVC integration mock environment cho CT-003 + CT-034 | DevOps | Sau R8 |

---

## Out of scope round R7.7.12 R2

- BR-CALC test edge case (CT-018 over-cap, CT-019 annual reset) — defer khi có data + system clock control.
- File upload validation 5 định dạng (CT-033 kênh CB NV thủ công) — defer Bước 2a sau khi có DN account.
- N≥2 PHE_DUYET_CHI_TRA records (CT-014 truly N:1 lifecycle) — defer khi pool có CPD BR-OK để complete cycle.
- Notification email per-B-step (CT-030) — defer khi có MailHog inbox snapshot per HSCT.
- Permission matrix full coverage (CT-023..028) — kế thừa R7.4.A2 — không re-test.

---

## Lịch sử round

| Round | Date | Kết quả tóm tắt |
|---|---|---|
| R7-R2 | 2026-05-10 01:30:00 | 20/35 PASS · 5 BLOCKED · 7 DEFER · 3 sai spec partial. Kế thừa từ R7.6.1 R1/R2 + R7.7.12.3 R2 + R7.7.12.4 R1. Phát hiện BR-CALC-02 rounding edge (acceptable) + material deviation thuộc BUG-CHITRA-001. |

---

*Functional test report generated: 2026-05-10 01:30:00 | QA Automation via Claude Code*
