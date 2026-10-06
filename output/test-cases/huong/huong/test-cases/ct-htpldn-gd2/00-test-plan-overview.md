# Kế Hoạch Kiểm Thử — CT HTPLDN Giai đoạn 2 (FR-15, SCR-XI-01 — Tab "Đợt báo cáo")

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-10
> **Nguồn dữ liệu**: SRS v3.1 ([srs-fr-15-ct-htpldn-v3.1.md](../../../input/srs-v3/srs-fr-15-ct-htpldn-v3.1.md), kèm [srs-v3.md](../../../input/srs-v3/srs-v3.md) Phụ lục B/C)
> **SRS Reference**: Nhóm XI — UC165 (continuation) + UC166..UC170, SCR-XI-01 (Tab "Đợt báo cáo" + Drill-down Đợt BC)
>
> **Scope GĐ2:** Lifecycle Đợt báo cáo (SM-DOT-BC, 6 trạng thái — phần TAO_DOT → DA_TONG_HOP) + CRUD Báo cáo kết quả + Tổng hợp TW. **Cascade:** Phụ thuộc GĐ1 (CT phải DANG_THUC_HIEN/HOAN_THANH) + cascade gợi ý số liệu từ Vụ việc (W3.2) + Chi trả (W4.2) + Đánh giá (W4.4).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử (GĐ2)

- 6 FR (UC165 phần lifecycle + UC166..UC170) trên 1 màn hình tổng hợp SCR-XI-01 — Tab "Đợt báo cáo".
- Entity chính: `DOT_BAO_CAO` (owned, lifecycle DANG_LAP_BC → DA_TONG_HOP), `BAO_CAO_CT_HTPL` (owned, full CRUD lifecycle DU_THAO → DA_DUYET / TU_CHOI).
- State Machine bao quát:
  - **SM-DOT-BC** phần GĐ2 (5 transitions): TAO_DOT → DANG_LAP_BC → CHO_DUYET_KQ → DA_DUYET_KQ → DA_GUI_TW → DA_TONG_HOP + CHO_DUYET_KQ → DANG_LAP_BC (từ chối)
  - **BC sub-state machine** (chứa trong BAO_CAO_CT_HTPL.trang_thai): DU_THAO → CHO_PHE_DUYET → DA_DUYET / TU_CHOI
- Đặc thù:
  - Bắt đầu lập BC: trigger TAO_DOT → DANG_LAP_BC tạo BAO_CAO_CT_HTPL record (FR-XI-06 step 1)
  - Lập BC theo mẫu TT17/2025 (21a/21b) với gợi ý số liệu (đếm VV, tổng chi phí…)
  - Trình PD KQ — chuyển đợt BC + BC subordinate state (FR-XI-07)
  - Phê duyệt BC cùng cấp (BR-AUTH-05) + Từ chối có lý do (BR-FLOW-04)
  - Gửi lên TW (chỉ BN/ĐP) (FR-XI-08)
  - TW tổng hợp BC (chỉ TW) — chọn nhiều BC + auto-SUM + xuất Excel/Word (FR-XI-09)

### 1.2 Danh sách FR / UC GĐ2

| # | Mã FR | UC | Tên chức năng | Entity | File Test Case |
|---|-------|----|--------------|--------|----------------|
| 1 | FR-XI-05a (cont) + FR-XI-06 step 1 | UC165→UC166 | Bắt đầu lập BC (transition TAO_DOT → DANG_LAP_BC, tạo BAO_CAO_CT_HTPL) | DOT_BAO_CAO + BAO_CAO_CT_HTPL | `01-TC-bat-dau-lap-bc.md` |
| 2 | FR-XI-06 | UC166 | Lập BC kết quả thực hiện (form 21a/21b + gợi ý số liệu) | BAO_CAO_CT_HTPL | `02-TC-lap-bao-cao-kq.md` |
| 3 | FR-XI-07 | UC167 | Trình phê duyệt BC (đợt: DANG_LAP_BC → CHO_DUYET_KQ; BC: DU_THAO → CHO_PHE_DUYET) | DOT_BAO_CAO + BAO_CAO_CT_HTPL | `03-TC-trinh-phe-duyet-bc.md` |
| 4 | FR-XI-07a | UC168 | Phê duyệt / Từ chối BC kết quả (CB PD cùng cấp) | DOT_BAO_CAO + BAO_CAO_CT_HTPL | `04-TC-phe-duyet-bc.md` |
| 5 | FR-XI-08 | UC169 | Gửi BC lên TW (chỉ BN/ĐP, đợt: DA_DUYET_KQ → DA_GUI_TW) | DOT_BAO_CAO | `05-TC-gui-len-tw.md` |
| 6 | FR-XI-09 | UC170 | TW tổng hợp BC (chọn nhiều BC, gợi ý SUM, xuất Excel/Word) | BAO_CAO_CT_HTPL (loại TONG_HOP_TW) | `06-TC-tw-tong-hop-bc.md` |
| 7 | — | — | Permission matrix cross-FR-XI GĐ2 | All | `07-TC-permission-matrix.md` |

> **Cascade chú ý:** Một số TC happy-path GĐ2 cần dữ liệu downstream (vụ việc HOAN_THANH cho gợi ý số liệu, chi trả DA_DUYET cho tổng chi phí). Test plan thiết kế **2 nhánh:** (a) gợi ý số liệu **rỗng** — vẫn cho phép nhập tay (P0 happy path); (b) gợi ý số liệu **có sẵn** — cần seed cross-module (defer Phase B chờ W3.2/W4.2 cascade per [todo.md §480](../../../tasks/detailed-tc/todo.md)).

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|----------------------|-------------------|
| QTHT | — | qtht_01 | Read-only verify (toàn HT). `_02` fallback |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD BC TW + tổng hợp (FR-XI-09). `_02` fallback, `_03` permission test |
| CB_NV_BN | BN | cb_nv_bn_01 (Bộ KH&ĐT) | CRUD BC scoped BN + Gửi TW (FR-XI-08) |
| CB_NV_DP | DP | cb_nv_dp_01 (Sở TP AG) | CRUD BC scoped ĐP + Gửi TW. `_02` Sở TP BG (cùng cấp khác đơn vị) |
| CB_PD_TW | TW | cb_pd_tw_01 | Phê duyệt BC cùng cấp (TW). KHÔNG CRUD BC |
| CB_PD_BN | BN | cb_pd_bn_01 | Phê duyệt BC scoped BN |
| CB_PD_DP | DP | cb_pd_dp_01 | Phê duyệt BC scoped ĐP. `_02` cùng cấp khác đơn vị (test BR-AUTH-05) |
| NHT/TVV/CG/DN/GV | — | nht_01, tvv_01, cg_01, dn_01 | Negative — verify 403 chặn module |

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng GĐ2? | TC áp dụng |
|----|---------|-----------|--------------|------------|
| BR-AUTH-01 | Xác thực 2-tier (TOTP/SSO) | srs-fr-15:1419 | ✅ | Precondition mọi TC + TC-PERM-006 |
| BR-AUTH-05 | Phê duyệt cùng cấp | srs-fr-15:1428 | ✅ (core FR-XI-07a) | TC-PD-BC-005, TC-PERM-002 |
| BR-AUTH-08 | Phân quyền theo `don_vi_id` | srs-v3 Phụ lục B | ✅ | TC-LBC-006, TC-PERM-001/003, TC-GTW-005 |
| BR-DATA-01 | Soft delete (is_deleted=1) | srs-fr-15:1437 | (gián tiếp — BC không có delete API trong GĐ2; reset qua từ chối) | — |
| BR-DATA-05 | Audit trail INSERT-only | srs-fr-15:1444 | ✅ | TC-LBC-001, TC-TPD-001/004, TC-PD-BC-001/004, TC-GTW-001, TC-TH-001 |
| BR-DATA-06 | Export Excel max 10k rows | srs-v3:3977 | ✅ (Tổng hợp TW xuất file) | TC-TH-006 (xuất Excel TT17), TC-TH-007 (boundary >10k) |
| BR-DATA-07 | Pagination 20 default, max 100 | srs-fr-15:1453 | ✅ (DS BC trong tab Đợt BC + DS BC từ BN/ĐP cho TW) | TC-LBC-007, TC-TH-002 |
| BR-EC-01 | Optimistic Locking | srs-v3:4066 | ✅ (BC concurrent edit) | TC-LBC-009 (concurrent UPDATE BC) |
| BR-EC-12 | Pagination guard `[1,100]` | srs-v3:4077 | ✅ | TC-TH-008 (param boundary) |
| BR-EC-13 | Search sanitize max 200 ký tự + escape | srs-v3:4078 | ✅ (filter tổng hợp TW theo đơn vị/kỳ) | TC-TH-009 (XSS trong nhận xét) |
| BR-EC-19 | Batch ops max 100 records | srs-v3:4084 | ✅ (TW chọn nhiều BC) | TC-TH-010 (>100 BC chọn batch) |
| BR-FLOW-04 | Từ chối yêu cầu lý do | srs-fr-15:1467-1471 | ✅ (core FR-XI-07a TC) | TC-PD-BC-003, TC-PD-BC-004 |
| BR-FLOW-08 | BC CT HTPLDN: ĐP+BN → TW tổng hợp | srs-fr-15:1480 | ✅ (core FR-XI-08 + 09) | TC-GTW-001..005, TC-TH-001..005 |
| **SM-DOT-BC** | State machine 6 states + 6 transitions (GĐ2 phần 5 transitions sau TAO_DOT) | srs-fr-15:1371-1397 | ✅ (core) | All file 01-06 |
| **SM-BC sub** | Sub-state BAO_CAO_CT_HTPL.trang_thai (4 states: DU_THAO/CHO_PHE_DUYET/DA_DUYET/TU_CHOI) | srs-fr-15:1300 | ✅ | All file 01-04 |

**Coverage GĐ2:** 13 BR áp dụng trực tiếp + 2 SM (loại BR-DATA-01 vì BC không có delete trong GĐ2; BR-FLOW-03/05 không áp — không công bố BC).

### 2.2 Error Codes / Warnings

**FR-XI-05a (continuation TAO_DOT → DANG_LAP_BC):**
- (Không có ERR code riêng cho transition này trong SRS — guard "Đợt đã hoàn chỉnh thông tin" — log SPEC-CLARIFY-CT-GD2-01 nếu thiếu)

**FR-XI-06 (Lập BC):**
- ERR-XI-06-01 (thiếu số liệu bắt buộc)

**FR-XI-07 (Trình PD BC):**
- ERR-XI-07-01 (BC chưa hoàn chỉnh)

**FR-XI-07a (Phê duyệt BC):**
- ERR-XI-07a-01 (BC không ở CHO_DUYET_KQ)
- ERR-XI-07a-02 (Từ chối thiếu lý do)
- ERR-XI-07a-03 (CB PD khác cấp)

**FR-XI-08 (Gửi TW):**
- ERR-XI-08-01 (Đợt BC không ở DA_DUYET_KQ)
- ERR-XI-08-02 (User không phải BN/ĐP)

**FR-XI-09 (TW tổng hợp):**
- ERR-XI-09-01 (Không chọn BC nào)
- ERR-XI-09-02 (User không phải TW)
- WRN-XI-09-01 (BC schema khác version — mẫu cũ)

**Coverage Error Code:** 9/9 ERR + 1/1 WRN = 100%.

### 2.3 Permission Matrix (GĐ2)

| Action | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | NHT/TVV/CG/DN/GV |
|--------|------|----------|----------|----------|----------|----------|----------|-----------------|
| Tab "Đợt BC" — đọc | 👁️ R | 👁️ R | 👁️ R | 👁️ R | 👁️ R | 👁️ R | 👁️ R | ❌ |
| BC — Lập (UC166) | ❌ | ✅ scope TW | ✅ scope BN | ✅ scope ĐP | ❌ | ❌ | ❌ | ❌ |
| BC — Trình PD KQ (UC167) | ❌ | ✅ scope TW | ✅ scope BN | ✅ scope ĐP | ❌ | ❌ | ❌ | ❌ |
| BC — Phê duyệt KQ (UC168) | ❌ | ❌ | ❌ | ❌ | ✅ cùng cấp TW | ✅ cùng cấp BN | ✅ cùng cấp ĐP | ❌ |
| BC — Từ chối KQ (UC168) | ❌ | ❌ | ❌ | ❌ | ✅ cùng cấp TW | ✅ cùng cấp BN | ✅ cùng cấp ĐP | ❌ |
| Đợt BC — Gửi TW (UC169) | ❌ | ❌ (TW không gửi cho chính mình) | ✅ scope BN | ✅ scope ĐP | ❌ | ❌ | ❌ | ❌ |
| BC — Tổng hợp TW (UC170) | ❌ | ✅ TW only | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| BC — Xuất Excel/Word TT17 (UC170) | ❌ | ✅ TW only | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

(Scope = bị giới hạn theo `don_vi_id` của user, BR-AUTH-08)

> **Footnote scope BR-AUTH-05 cho FR-XI-07a:**
> - CB_PD_DP cùng cấp ĐP nhưng **khác đơn vị** (Sở TP BG vs Sở TP AG) — SRS srs-fr-15:1428-1435 + srs-fr-15:884 không nói rõ "cùng đơn vị" hay chỉ "cùng cấp".
> - Áp dụng cùng cách giải thích SPEC-CLARIFY-CT-01 GĐ1 (cùng cấp ĐP cross-đơn vị) — log lại thành SPEC-CLARIFY-CT-GD2-02 cross-link.

### 2.4 State Machine — SM-DOT-BC (full 6 states)

```
[*] → TAO_DOT  ← (GĐ1 chỉ test transition này)
TAO_DOT → DANG_LAP_BC  ← (GĐ2 file 01: bắt đầu lập BC + tạo BAO_CAO_CT_HTPL record)
DANG_LAP_BC ↔ CHO_DUYET_KQ  ← (Trình PD ↔ Từ chối — file 03 + 04)
CHO_DUYET_KQ → DA_DUYET_KQ  ← (PD duyệt — file 04)
DA_DUYET_KQ → DA_GUI_TW  ← (BN/ĐP gửi TW — file 05)
DA_GUI_TW → DA_TONG_HOP  ← (TW tổng hợp — file 06)
```

**5 transitions chính (GĐ2):**

| # | Transition | Trigger | Guard | File TC |
|---|-----------|---------|-------|---------|
| 1 | TAO_DOT → DANG_LAP_BC | CB NV "Bắt đầu lập BC" | Đợt đã hoàn chỉnh thông tin | 01 |
| 2 | DANG_LAP_BC → CHO_DUYET_KQ | CB NV "Trình duyệt KQ" | BC đầy đủ số liệu | 03 |
| 3 | CHO_DUYET_KQ → DA_DUYET_KQ | CB PD "Phê duyệt" | Cùng cấp (BR-AUTH-05) | 04 |
| 4 | CHO_DUYET_KQ → DANG_LAP_BC | CB PD "Từ chối" | Có lý do (BR-FLOW-04) | 04 |
| 5 | DA_DUYET_KQ → DA_GUI_TW | CB NV BN/ĐP "Gửi TW" | Chỉ BN/ĐP | 05 |
| 6 | DA_GUI_TW → DA_TONG_HOP | CB NV TW "Tổng hợp" | TW + chọn ≥1 BC | 06 |

### 2.5 BC Sub-state Machine (BAO_CAO_CT_HTPL.trang_thai)

```
[*] → DU_THAO  ← (FR-XI-06 step 5: Lưu bản ghi BC khi lập)
DU_THAO → CHO_PHE_DUYET  ← (FR-XI-07: Trình duyệt KQ)
CHO_PHE_DUYET → DA_DUYET  ← (FR-XI-07a: Duyệt KQ)
CHO_PHE_DUYET → TU_CHOI  ← (FR-XI-07a: Từ chối)
TU_CHOI → DU_THAO  ← (CB NV chỉnh sửa + trình lại; SRS không gọi explicit transition nhưng implicit qua FR-XI-07a postcondition "CB NV chỉnh sửa + trình lại")
```

> **Liên kết 2 SM:** Dot BC `trang_thai` và BC `trang_thai` là 2 SM song hành, đồng bộ qua các transition trong UC167/UC168. File TC phải verify CẢ HAI state cùng lúc (vd Trình PD: đợt BC `DANG_LAP_BC → CHO_DUYET_KQ` ↔ BC `DU_THAO → CHO_PHE_DUYET`).

---

## 3. Cấu Trúc File Test Case (dự kiến — sau A4/A6/A7 inline merge)

```
ct-htpldn-gd2/
├── 00-test-plan-overview.md           ← (file này)
├── 01-TC-bat-dau-lap-bc.md            ← FR-XI-05a→06 transition TAO_DOT → DANG_LAP_BC + tạo BAO_CAO_CT_HTPL (~5 TC)
├── 02-TC-lap-bao-cao-kq.md            ← FR-XI-06 UC166 form 21a/21b + gợi ý số liệu (~10 TC)
├── 03-TC-trinh-phe-duyet-bc.md        ← FR-XI-07 UC167 (~6 TC)
├── 04-TC-phe-duyet-bc.md              ← FR-XI-07a UC168 (~10 TC)
├── 05-TC-gui-len-tw.md                ← FR-XI-08 UC169 (~6 TC)
├── 06-TC-tw-tong-hop-bc.md            ← FR-XI-09 UC170 (~10 TC)
├── 07-TC-permission-matrix.md         ← Permission cross-FR-XI GĐ2 (~6 TC)
├── 08-REVIEW-edge-case-hunter.md      ← A4 audit log (đã merge edge case vào 01-07)
├── 09-traceability-matrix.md          ← A5 BR/AC ↔ TC matrix
├── 10-REVIEW-test-quality.md          ← A6 6-axis quality score
└── 11-a7-filter-log.md                ← A7 filter log
```

> **Phase B B-block ref CHỈ 7 file UC (01-07)**, dự kiến **~53 TC sau A3** + thêm sau A4/A6 → ~65 TC. File 08-11 là audit log (KHÔNG phải TC source — lesson learned 2026-05-06 W2.3 inline merge rule).

---

## 4. Strategy đặc thù module

- **Cascade dữ liệu thật vs nhập tay:** Nhánh "gợi ý số liệu rỗng" (P0 happy path) đảm bảo Phase A có thể done **không cần** wait W3.2/W4.2 cascade. Nhánh "có gợi ý" (P1) defer Phase B (đã ghi trong todo.md §480).
- **Approval cross-cấp ĐP cùng cấp khác đơn vị:** Cần TK fallback `cb_pd_dp_02` (Sở TP BG) — log SPEC-CLARIFY-CT-GD2-02 chờ BA xác nhận behavior.
- **Drill-down navigate:** Tab "Đợt báo cáo" → click row đợt BC → drill-down màn hình lập BC. MCP test phải `wait_for(text)` chờ form 21a/21b render rồi mới `take_snapshot`.
- **Form 21a/21b editable table:** SRS (line 1097-1098) định nghĩa form là `editable table` — TC phải verify tính editable từng cell + lưu nháp + retry.
- **Số liệu JSON storage:** `BAO_CAO_CT_HTPL.so_lieu_tong_hop` là `text (long)` JSON — verify roundtrip qua MCP (tạo → lưu → reload page → render lại đúng).
- **Tổng hợp TW (UC170) auto-SUM:** TC phải verify công thức cộng dồn các cột BC (vd "Cột 3: Số DN tham gia tư vấn" = SUM của tất cả BC ĐP+BN cùng kỳ). Test với 2-3 BC mock để verify SUM logic.
- **Xuất Excel/Word theo mẫu TT17:** Verify file outbound qua MCP `list_network_requests` + tải về kiểm tra cột/sheet name khớp mẫu TT17.
- **Filter A7 dự kiến:** Toàn bộ TC chạy qua UI SCR-XI-01 Tab Đợt BC + drill-down + verify network qua MCP → 0 TC chỉ-DB/API thuần. AC liên quan email notification (FR-XI-07/07a/08 step 5 "Gửi thông báo CB PD/CB NV") verify gián tiếp qua MCP `list_network_requests` xem POST `/notifications` outbound — vẫn UI-driven.

---

## 5. Acceptance Phase A

- ✅ 7 bước A1-A7 done
- ✅ Traceability ≥95% BR (loại BR-DATA-01 vì BC không có delete trong GĐ2; BR-FLOW-03/05 không áp) + 100% AC
- ✅ 0 TC chỉ-DB/API thuần (A7 verified)
- ✅ 0 TC sống ở file phụ 08-11 (mọi TC inline trong file UC 01-07)
- ✅ SPEC-CLARIFY listed (gửi BA Phase B)
- ✅ Codex review 2026-05-10 GATE — chờ /codex run sau A7

## 6. SPEC-CLARIFY pending BA sign-off (final sau A1-A7 + Codex)

| # | ID | Mô tả | TC liên quan | Nguồn |
|---|----|-------|--------------|-------|
| 1 | SPEC-CLARIFY-CT-GD2-01 | Guard "Đợt đã hoàn chỉnh thông tin" cho transition TAO_DOT → DANG_LAP_BC — UI mapping | TC-LBC-002 | srs-fr-15:1391-1392 |
| 2 | SPEC-CLARIFY-CT-GD2-02 | BR-AUTH-05 cùng cấp ĐP cross-đơn vị (Sở TP AG vs Sở TP BG) cho FR-XI-07a phê duyệt BC | TC-PD-BC-013 | srs-fr-15:1428-1435 + srs-fr-15:884 |
| 3 | SPEC-CLARIFY-CT-GD2-03 | "Số liệu hệ thống gợi ý" — danh sách cột nào lấy từ entity nào (vụ việc, chi trả, đánh giá) — chưa có mapping rõ | TC-BC-005 | srs-fr-15:728 |
| 4 | SPEC-CLARIFY-CT-GD2-04 | Schema versioning BC (WRN-XI-09-01) — định nghĩa "mẫu cũ" + cơ chế nhận diện | TC-TH-012 | srs-fr-15:1013 |
| 5 | SPEC-CLARIFY-CT-GD2-05 | Auto-SUM tổng hợp TW — danh sách cột cần SUM + xử lý BC trùng kỳ + xử lý BC schema khác | TC-TH-003 | srs-fr-15:984 |
| 6 | SPEC-CLARIFY-CT-GD2-06 (A4) | Guard CT TAM_DUNG có cho phép lập BC trên đợt đã có không | TC-LBC-013 | srs-fr-15:1346-1347 (SM-KH-CTHTPL TAM_DUNG state) |
| 7 | SPEC-CLARIFY-CT-GD2-07 (A4) | ly_do_tu_choi FR-XI-07a max length — SRS chỉ nói `text (long)` | TC-PD-BC-015 | srs-fr-15:843 |
| 8 | SPEC-CLARIFY-CT-GD2-08 (A4) | Tổng hợp BC cross-kỳ — block hay cho phép | TC-TH-015 | srs-fr-15:984 |
| 9 | SPEC-CLARIFY-CT-GD2-09 (Codex) | `loai` field gap entity BAO_CAO_CT_HTPL — SRS Output table FR-XI-09 (line 998) ghi `BAO_CAO_CT (loai = TONG_HOP_TW)` nhưng entity columns (1293-1300) KHÔNG có column `loai` | TC-TH-019 | srs-fr-15:998 vs 1293-1300 |

## 7. Final TC count breakdown

| File | A3 base | A4 | A6 | Codex | Final |
|------|--------:|---:|---:|------:|------:|
| 01 - Bắt đầu lập BC | 5 | +2 | 0 | 0 | 7 |
| 02 - Lập BC | 8 | +4 | 0 | 0 | 12 |
| 03 - Trình PD BC | 6 | +2 | 0 | 0 | 8 |
| 04 - Phê duyệt BC | 9 | +3 | 0 | 0 (rename) | 12 |
| 05 - Gửi TW | 6 | +2 | 0 | 0 | 8 |
| 06 - Tổng hợp TW | 11 | +3 | +2 | 0 (sửa) | 16 |
| 07 - Permission matrix | 6 | +3 | +1 | +1 | 11 |
| **TỔNG** | **51** | **+19** | **+3** | **+1** | **74** |

---

*Generated 2026-05-10 — Phase A step A2 (bmad-testarch-test-design) · Updated 2026-05-10 sau Codex review (+1 TC, +1 SPEC-CLARIFY).*
