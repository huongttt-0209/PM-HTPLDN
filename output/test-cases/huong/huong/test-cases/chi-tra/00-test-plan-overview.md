# Kế Hoạch Kiểm Thử — Chi trả Chi phí Tư vấn (FR-V.II, SCR-V.II-01..02)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-10
> **Module**: W4.2 (FR-06 Chi trả)
> **Nguồn dữ liệu**: SRS v3.1 ([srs-fr-06-chi-tra-v3.1 md](../../../input/srs-v3/srs-fr-06-chi-tra-v3.1%20md), kèm [srs-v3.md](../../../input/srs-v3/srs-v3.md) cho BR Phụ lục B)
> **SRS Reference**: Nhóm V.II — UC68..UC80 + GAP-V.II-01 (FR-V.II-01..14), SCR-V.II-01/02
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho module Chi trả — nguồn HS DUY NHẤT từ DVC qua LGSP (CB NV KHÔNG nhập tay). 6-step stepper workflow trên SCR-V.II-02 (Tiếp nhận → Kiểm tra → Đánh giá → Thẩm định → Phê duyệt → Thanh toán). FR-V.II-01 (UC68 LGSP inbound API thuần) + FR-V.II-04 (UC71 LGSP outbound auto) + FR-V.II-07 (UC74 DN gửi đề nghị TT API thuần) → A7 LOẠI nhánh API thuần, GIỮ phần verify side-effect UI. FR-V.II-10 (UC77 in-app + email auto) → A7 verify in-app side-effect.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **14 FR (UC68..UC80 + GAP-V.II-01)** trên 2 màn hình. **Sau A7 filter:** 12 FR active (loại nhánh API thuần UC68/71/74, giữ verify side-effect UI; UC77 verify in-app; UC75 standalone notification).
- **Entity owned (4):** HO_SO_CHI_TRA, DANH_GIA_HO_SO_CHI_TRA, THAM_DINH_HO_SO, PHE_DUYET_CHI_TRA
- **Entity referenced (6):** VU_VIEC, TU_VAN_VIEN, DOANH_NGHIEP, TAI_KHOAN, DON_VI, THONG_BAO (polymorphic global)
- **Màn hình (2):**
  - SCR-V.II-01: Danh sách HS Chi trả (5 tab + 9 cột + filter quy mô/trạng thái/range ngày)
  - SCR-V.II-02: Chi tiết HS Chi trả (Stepper 6 bước + 8 sections + 5 conditional sections theo trạng thái + auto-calc BR-CALC-01/02)
- **State Machine:** SM-CHITRA 10 trạng thái (CHO_TIEP_NHAN → DANG_KIEM_TRA → {DANG_DANH_GIA | YEU_CAU_BO_SUNG | TU_CHOI} → DANG_THAM_DINH → CHO_PHE_DUYET → DA_DUYET → DA_THANH_TOAN; nhánh phụ HUY/TU_CHOI). **Edge case CB PD "Từ chối"** = TRẢ VỀ DANG_THAM_DINH (KHÔNG phải từ chối cuối) — CB NV điều chỉnh xong có thể Trình PD lại.
- **Đặc thù module:**
  - Nguồn HS DUY NHẤT: DVC qua LGSP — CB NV KHÔNG nhập tay
  - BR-CALC-01 mức hỗ trợ NĐ18/2026: Siêu nhỏ 100% (trần 3M), Nhỏ 30% (trần 5M), Vừa 10% (trần 10M)
  - BR-CALC-02 công thức `so_tien_duoc_duyet = MIN(so_tien_de_nghi, phi_tu_van × muc_ho_tro%, tran_ho_tro_nam − da_chi_trong_nam)`
  - Reset trần năm vào 01/01 hàng năm
  - `so_tien_thuc_tra ≤ so_tien_duoc_duyet`
  - DN bổ sung qua DVC trong 5 ngày LV kể từ `ngay_yeu_cau_bo_sung` (FR-V.II-14 PRE-02 + ERR-CT-BS-03)
  - UI counter "Lần bổ sung: {n}/3" (HO_SO_CHI_TRA.bo_sung_count CHECK BETWEEN 0 AND 3)
  - Quy mô DN snapshot tại thời điểm nộp HS (EC-04)
  - PHE_DUYET_CHI_TRA N:1 — ghi cả lịch sử DUYET + TU_CHOI trả về

### 1.2 Danh sách FR / UC → TC file mapping

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-V.II-02 + FR-V.II-06 | UC69 + UC73 | Quản lý DS HS Chi trả (SCR-01) + Tiếp nhận + DN rút HS | HO_SO_CHI_TRA | `01-TC-FR-V.II-02-quan-ly-HS-de-nghi.md` |
| 2 | FR-V.II-03 | UC70 | Kiểm tra HS — checklist 5 thành phần Mẫu 01 NĐ55 (SCR-02 section 3) | HO_SO_CHI_TRA | `02-TC-FR-V.II-03-kiem-tra-HS.md` |
| 3 | FR-V.II-05 | UC72 | Đánh giá tiêu chí + auto-calc BR-CALC-01/02 (SCR-02 section 4) | DANH_GIA_HO_SO_CHI_TRA | `03-TC-FR-V.II-05-danh-gia-tieu-chi.md` |
| 4 | FR-V.II-09 | UC76 | Thẩm định + đối chiếu 4 checklist (SCR-02 section 5) | THAM_DINH_HO_SO | `04-TC-FR-V.II-09-tham-dinh.md` |
| 5 | FR-V.II-11 + FR-V.II-12 | UC78 + UC79 | Trình PD + CB PD Phê duyệt/Trả về (SCR-02 section 5+6) | PHE_DUYET_CHI_TRA | `05-TC-FR-V.II-11-12-trinh-PD-phe-duyet.md` |
| 6 | FR-V.II-13 | UC80 | Cập nhật KQ thanh toán (SCR-02 section 7) | HO_SO_CHI_TRA | `06-TC-FR-V.II-13-cap-nhat-thanh-toan.md` |
| 7 | FR-V.II-14 | GAP-V.II-01 | DN bổ sung HS chi trả (qua DVC + verify side-effect UI) | HO_SO_CHI_TRA | `07-TC-FR-V.II-14-DN-bo-sung-HS.md` |
| 8 | FR-V.II-08 | UC75 | TVV nhận thông báo KQ thanh toán (DS thông báo) | THONG_BAO | `08-TC-FR-V.II-08-thong-bao-TVV.md` |
| 9 | FR-V.II-01/04/07/10 | UC68/71/74/77 | API LGSP inbound + outbound + in-app TB — verify side-effect UI | HO_SO_CHI_TRA, THONG_BAO | `09-TC-API-side-effect.md` |
| 10 | — | — | Permission matrix cross-FR-V.II (BR-AUTH-01/05/08, scope đơn vị, role-based) | All | `10-TC-permission-matrix.md` |
| ~~11~~ | ~~FR-V.II-01~~ | ~~UC68 nhánh API thuần~~ | ~~LGSP inbound JWT/mTLS validate~~ — **LOẠI A7** (giữ side-effect ở file 09) | — | — |
| ~~12~~ | ~~FR-V.II-04~~ | ~~UC71 nhánh API thuần~~ | ~~LGSP outbound auto trigger~~ — **LOẠI A7** (giữ side-effect ở file 09) | — | — |
| ~~13~~ | ~~FR-V.II-07~~ | ~~UC74 nhánh API thuần~~ | ~~DN gửi đề nghị TT qua DVC API~~ — **LOẠI A7** (giữ side-effect ở file 09) | — | — |
| ~~14~~ | ~~FR-V.II-10~~ | ~~UC77 nhánh email auto~~ | ~~Email backend trigger~~ — **LOẠI A7** nhánh email, GIỮ verify in-app TB ở file 09 | — | — |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | `qtht_01` | Read-only verify scope toàn HT |
| CB_NV_TW | TW | `cb_nv_tw_01` (primary), `cb_nv_tw_02/03` (concurrent) | UC69/70/72/76/78/80 — workflow chính (scope TW = toàn quốc) |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH), `cb_nv_bn_02` (BTC), `cb_nv_bn_03` (BCT) | TC permission scope BN |
| CB_NV_DP | DP | `cb_nv_dp_01` (AG), `cb_nv_dp_02` (BG), `cb_nv_dp_03` (BNI) | TC permission scope DP + verify HS DN cùng tỉnh |
| CB_PD_TW | TW | `cb_pd_tw_01` (primary), `cb_pd_tw_02/03` | UC79 phê duyệt + trả về thẩm định (BR-AUTH-05 cùng cấp) |
| CB_PD_BN | BN | `cb_pd_bn_01..03` | TC BR-AUTH-05 cùng cấp BN + negative xuyên cấp |
| CB_PD_DP | DP | `cb_pd_dp_01..03` | TC BR-AUTH-05 cùng cấp DP + negative xuyên cấp |
| TVV | DP | `tvv_01..03` | UC75 nhận TB KQ thanh toán (verify scope TVV gắn với HS) |
| DN | — | `dn_01` (AG) | UC69 DN rút HS, GAP-V.II-01 DN bổ sung qua DVC (verify side-effect UI), không thấy HS DN khác |
| Negative | — | role chéo | Verify 403 chặn khi truy cập HS đơn vị/DN khác |

> **Note seed gap (Phase B B-Seed):** HS Chi trả chỉ tạo qua DVC/LGSP API — **B-Seed BẮT BUỘC** dùng pattern memory `fr06_chi_tra_r7e3_finding.md` (env hiện có ~70 HSCT seed sẵn 8 state). Nếu thiếu state cụ thể → query NotebookLM SRS hoặc dùng admin endpoint trigger. KHÔNG nhập thủ công CMS.

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực truy cập | srs-fr-06:1376 | ✅ | Precondition login mọi UC |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB PD ↔ HS đơn vị) | srs-fr-06:1382 | ✅ | UC78 trình + UC79 PD (file 05+10) |
| BR-AUTH-08 | Phân quyền theo đơn vị (don_vi_id NOT NULL) | srs-fr-06:175 | ✅ | TC scope filter mọi DS (file 01+10) |
| BR-AUTH-09 | Xác thực LGSP inbound (JWT + mTLS) | srs-fr-06:1352 | ⚠️ side-effect verify only (A7 LOẠI nhánh API thuần) | File 09 — verify HS xuất hiện CHO_TIEP_NHAN sau LGSP push |
| BR-CALC-01 | Mức hỗ trợ NĐ18/2026 (Siêu nhỏ 100%/3M, Nhỏ 30%/5M, Vừa 10%/10M) | srs-fr-06:1358 | ✅ | UC72 đánh giá auto-calc (file 03) |
| BR-CALC-02 | `so_tien_duoc_duyet = MIN(so_tien_de_nghi, phi_tu_van × muc_ho_tro%, tran_ho_tro_nam − da_chi_trong_nam)` | srs-fr-06:1364 | ✅ | UC72 verify formula 3 thành phần MIN (file 03) |
| BR-CALC-03 | Deadline = ngày tiếp nhận + N ngày LV (từ CAU_HINH_SLA, trừ ngày lễ) | srs-fr-06:1370 | ✅ | UC68 verify SLA hiển thị cột (file 01+09) |
| BR-DATA-02 | Multi-tenant scoping | srs-fr-06:176 | ✅ | UC69 DS filter scope đơn vị (file 01+10) |
| BR-DATA-04 | Auto-gen mã CT-{YYYYMMDD}-{SEQ} | srs-fr-06:1388 | ✅ | UC68 verify mã sau LGSP inbound (file 09) |
| BR-DATA-05 | Audit trail immutable | srs-fr-06:1394 | ✅ | Verify mọi transition + thao tác CUD (mọi file) |
| BR-DATA-07 | Pagination 20 default, max 100 | srs-fr-06:1400 | ✅ | UC69 DS phân trang (file 01) |
| BR-FLOW-04 | Lý do từ chối ≥ 10 ký tự (UC79 CB PD) | srs-fr-06:1406 | ✅ | UC79 trả về (file 05) |
| BR-NOTIF-01 | Thông báo workflow (in-app + email) | srs-fr-06:213 | ✅ | UC75/77 verify TVV + DN nhận TB (file 08+09) |
| BR-RETRY-01 | LGSP retry 3 lần × 30s | srs-fr-06:324 | ⚠️ side-effect (A7 LOẠI nhánh job) | File 09 verify retry counter UI hoặc cảnh báo CB NV |

### 2.2 Error Codes — bảng tổng hợp

| Module/UC | Error Code | Message |
|-----------|-----------|---------|
| FR-V.II-01 (UC68 LGSP inbound) | ERR-CT-AUTH-01, ERR-CT-01..03 | JWT không hợp lệ / thiếu trường / trùng mã DVC / LGSP timeout (chỉ verify side-effect ở file 09) |
| FR-V.II-02 (UC69 quản lý) | INF-CT-01, ERR-CT-TN-01, ERR-CT-RUT-01 | Không tìm thấy / HS không CHO_TIEP_NHAN khi tiếp nhận / HS không CHO_TIEP_NHAN khi rút |
| FR-V.II-03 (UC70 kiểm tra) | ERR-CT-KT-01, ERR-CT-KT-02 | HS không DANG_KIEM_TRA / yêu cầu bổ sung không có ghi chú |
| FR-V.II-04 (UC71 outbound) | ERR-CT-LGSP-01, ERR-CT-LGSP-02 | LGSP timeout / LGSP reject (verify side-effect file 09) |
| FR-V.II-05 (UC72 đánh giá) | ERR-CT-DG-01, ERR-CT-DG-02 | HS không DANG_DANH_GIA / quy mô DN không hợp lệ |
| FR-V.II-09 (UC76 thẩm định) | ERR-CT-TD-01, ERR-CT-TD-02 | HS không DANG_THAM_DINH / không đạt mà không có nhận xét |
| FR-V.II-11 (UC78 trình PD) | ERR-CT-TRINH-01 | HS chưa thẩm định xong hoặc `ket_qua_tham_dinh ≠ DAT` |
| FR-V.II-12 (UC79 PD) | ERR-CT-PD-01..03 | HS không CHO_PHE_DUYET / từ chối không lý do / duyệt không số tiền |
| FR-V.II-13 (UC80 cập nhật TT) | ERR-CT-TT-01..03 | HS không DA_DUYET / số tiền vượt duyệt / thiếu ngày TT |
| FR-V.II-14 (DN bổ sung) | ERR-CT-BS-01..03 | Trạng thái ≠ YEU_CAU_BO_SUNG / file không hợp lệ / quá hạn 5 ngày LV |

### 2.3 Permission Matrix (cross-FR — chi tiết file 10)

| Entity / Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | TVV | DN |
|-----------------|------|-------------------|-------------------|-----|-----|
| Xem DS HS Chi trả (UC69, SCR-01) | 👁 R toàn HT | ✅ R scope đơn vị | 👁 R scope đơn vị | ❌ | 👁 R chỉ HS DN mình (qua chuyên trang) |
| Tiếp nhận HS (UC69 action) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Kiểm tra HS (UC70) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Đánh giá tiêu chí (UC72) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Thẩm định (UC76) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Trình PD (UC78) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Phê duyệt / Trả về (UC79) | ❌ | ❌ | ✅ cùng cấp đơn vị (BR-AUTH-05) | ❌ | ❌ |
| Cập nhật KQ TT (UC80) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| DN bổ sung HS (GAP-V.II-01 qua DVC) | ❌ | ❌ | ❌ | ❌ | ✅ chỉ HS DN mình + state YEU_CAU_BO_SUNG |
| DN rút HS (UC69 action) | ❌ | ❌ | ❌ | ❌ | ✅ chỉ HS DN mình + state CHO_TIEP_NHAN |
| TVV nhận TB KQ TT (UC75) | ❌ | ❌ | ❌ | ✅ chỉ HS gắn với TVV mình | ❌ |

### 2.4 State Machine — SM-CHITRA (10 trạng thái)

```
[*] → CHO_TIEP_NHAN (DN nộp qua DVC, FR-V.II-01 UC68)
CHO_TIEP_NHAN → DANG_KIEM_TRA (CB NV tiếp nhận, FR-V.II-02 UC69)
DANG_KIEM_TRA → DANG_DANH_GIA (Đạt, FR-V.II-03 UC70)
DANG_KIEM_TRA → YEU_CAU_BO_SUNG (Cần bổ sung, counter++, FR-V.II-03 UC70)
DANG_KIEM_TRA → TU_CHOI (Không đạt, FR-V.II-03 UC70)
YEU_CAU_BO_SUNG → DANG_KIEM_TRA (DN bổ sung qua DVC, FR-V.II-14 GAP-V.II-01)
DANG_DANH_GIA → DANG_THAM_DINH (Đánh giá xong, FR-V.II-05 UC72)
DANG_THAM_DINH → CHO_PHE_DUYET (CB NV trình + KQ thẩm định Đạt, FR-V.II-11 UC78)
DANG_THAM_DINH → TU_CHOI (Thẩm định Không đạt, FR-V.II-09 UC76)
CHO_PHE_DUYET → DA_DUYET (CB PD duyệt cùng cấp, FR-V.II-12 UC79)
CHO_PHE_DUYET → DANG_THAM_DINH (CB PD từ chối — TRẢ VỀ CB NV sửa, FR-V.II-12 UC79, BR-FLOW-04)
DA_DUYET → DA_THANH_TOAN (CB NV cập nhật TT, FR-V.II-13 UC80)
DA_DUYET → TU_CHOI (CB NV từ chối TT, ly_do = "THANH_TOAN", FR-V.II-13 UC80)
CHO_TIEP_NHAN → HUY (DN rút / CB NV hủy, FR-V.II-02 UC69 [GAP-V.II-03])
```

**13 transitions** (đồng bộ srs-fr-06:1313-1327):
- Nguồn duy nhất: DVC qua LGSP — CB NV KHÔNG nhập tay HS
- Edge: CB PD "Từ chối" = trả về DANG_THAM_DINH (KHÔNG phải TU_CHOI cuối) — PHE_DUYET_CHI_TRA ghi nhiều bản ghi lịch sử
- Edge: Reset trần năm 01/01 hàng năm (BR-CALC-01)
- Edge: Quá hạn bổ sung 5 ngày LV → ERR-CT-BS-03 (FR-V.II-14)

---

## 3. Phương Pháp Kiểm Thử

### 3.1 Loại test áp dụng

- **Functional happy path** — mỗi UC có ≥1 TC P0 walking-skeleton
- **Negative / state guard** — chuyển trạng thái sai → ERR-CT-*-* (mọi UC)
- **Auth / Permission** — BR-AUTH-01/05/08 cho mọi role × scope (file 10)
- **Business calc** — BR-CALC-01/02 với 9 case (3 quy mô × 3 boundary trần năm) (file 03)
- **State workflow E2E** — đi xuyên 6-step stepper, verify timeline + audit (file 01-06)
- **Edge case** — A4 cover (phí 0 / hết trần / số tiền vượt duyệt / quá hạn bổ sung / số lần bổ sung 0→3 → lần 4 KHÔNG cho phép)
- **Side-effect API** — verify UI sau LGSP inbound/outbound + in-app TB (file 09)

### 3.2 Trace BR/AC vs TC

- File `09-traceability-matrix.md` map BR/AC ↔ TC ID. Mục tiêu ≥ 95% BR + 100% AC explicit.

### 3.3 Tools

- **MCP chrome-devtools** — execute UI flow, take_snapshot, fill_form, list_network_requests, list_console_messages
- **/qa-only** — drive Phase B mỗi TC file
- **NotebookLM SRS** (id `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264`) — query khi gặp ambiguity (B-Verify 2-source check)

---

## 4. Tiêu chí Hoàn thành

### 4.1 Phase A (TC writing)
- [ ] 10 file TC `01..10-TC-*.md` đầy đủ section: Mục tiêu / Preconditions / Scenarios (table TC ID, Preconditions, Steps, Expected, BR/AC ref, Severity, Edge bổ sung) / Tổng số TC footer
- [ ] BR/AC Coverage ≥ 95% explicit (file 09)
- [ ] 0 TC chỉ-DB/API thuần (A7 verified, file 11)
- [ ] SPEC-CLARIFY-CT-* listed (forward BA Phase B)
- [ ] 0 TC sống ở file phụ (08/10/11) — mọi TC inline merged vào file UC `NN-TC-*.md`

### 4.2 Phase B (execution — defer)
- [ ] B-Seed pre-check (~70 HSCT env hiện có theo memory `fr06_chi_tra_r7e3_finding.md`)
- [ ] B-Run /qa-only mỗi file
- [ ] B-Verify NotebookLM + grep SRS local (2-source)
- [ ] B-Report 4-folder structure

---

## 5. Tham chiếu

- SRS chính: [`srs-fr-06-chi-tra-v3.1 md`](../../../input/srs-v3/srs-fr-06-chi-tra-v3.1%20md) (1414 dòng)
- BR Phụ lục B: [`srs-v3.md`](../../../input/srs-v3/srs-v3.md)
- SCR-V.II-01: srs-fr-06:898-952
- SCR-V.II-02: srs-fr-06:954-1034
- SM-CHITRA: srs-fr-06:1268-1328
- Entity HO_SO_CHI_TRA schema: srs-fr-06:1152-1187
- Memory: `fr06_chi_tra_r7e3_finding.md`, `fr06_chi_tra_execution_sequence.md`, `fr06_wave2_progress_2026-05-07.md`

---

**— Tổng số TC dự kiến (A3 baseline): 81 TC** (file 01: 12 + file 02: 10 + file 03: 12 + file 04: 9 + file 05: 10 + file 06: 7 + file 07: 5 + file 08: 4 + file 09: 4 + file 10: 8). A4 sẽ +edge, A6 fill gap, A7 lọc, codex review delta.
