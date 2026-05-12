# TODO — FR-13 — TV nhanh (Phiên + Kho QA)

> File module FR-13 — 2 đơn vị test (M13 Phiên TV nhanh + M14 Kho Q&A). Tổng **13 task**.
>
> **Tham chiếu shared:** [`test-plan.md`](test-plan.md) (v1.1 revised 2026-05-12 13:30:00) · `tasks/state-snapshot.md` · `tasks/dep-map.md`
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream
>
> **SRS authoritative:** `input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md` (v3.5)
>
> **Task IDs:** T-FR13-001 .. T-FR13-013

---

## Tổng hợp module

| Nhóm | Tổng | 🟢 | 🔵 | ✅ | ⚠️ | 🚫 | ⏳ | Task IDs |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| **M13 Phiên TV nhanh** | 4 | 4 | 0 | 0 | 0 | 0 | 0 | T-FR13-001..004 |
| **M14 Kho QA seed + lifecycle** | 4 | 4 | 0 | 0 | 0 | 0 | 0 | T-FR13-005..008 |
| **FR-X.2-06 Công khai** | 3 | 3 | 0 | 0 | 0 | 0 | 0 | T-FR13-009..011 |
| **FR-X.2-04 Outbound search + Audit** | 2 | 2 | 0 | 0 | 0 | 0 | 0 | T-FR13-012..013 |
| **Tổng** | **13** | **13** | **0** | **0** | **0** | **0** | **0** | |

---

## Tasks

### M13 — Phiên TV nhanh (SCR-X2-03)

- 🟢 **T-FR13-001** Verify SCR-X2-03 chặn nhập tay — UI KHÔNG có nút `[Thêm mới]`; phiên chỉ sinh từ API inbound <a id="t-fr13-001"></a>
  - **Cần có sẵn:** account `cb_nv_tw_01` login OK
  - **Spec:** `system-overview.md` §4.14 dòng 502 + `02-thu-tu-module.md` dòng 939; test-plan TC-TVN-NEG-04
  - **Acceptance:** Sidebar M13 render đầy đủ, toolbar chỉ có `[Làm mới]`, snapshot DOM xác nhận không có button label "Thêm mới"/"Tạo mới"/"+"

- 🟢 **T-FR13-002** Seed phiên TV nhanh qua API inbound `POST /api/v1/inbound/tu-van-nhanh` (mock Cổng PLQG) → tạo ≥3 phiên state MOI <a id="t-fr13-002"></a>
  - **Cần có sẵn:** [need: ≥1 DOANH_NGHIEP active (✗ chờ T-FR07-XXX); endpoint inbound spec confirm (✗ chờ BA — §7 #4)]
  - **Spec:** FR-X.2-03 step 6 + SRS v3.5 line 273; test-plan TC-TVN-001
  - **Acceptance:** ≥3 record `TU_VAN_NHANH.trang_thai=MOI`, kênh khác nhau (verify enum `NHANH`/`TV_NHANH` — §7 #5), `doanh_nghiep_id` valid FK

- 🟢 **T-FR13-003** Workflow CB NV xử lý phiên: MOI → CB_TRA_LOI (tra cứu Kho không auto-search) → gửi trả lời → DN đánh giá inbound → HOAN_THANH <a id="t-fr13-003"></a>
  - **Cần có sẵn:** [need: ≥3 TU_VAN_NHANH state MOI (✗ chờ T-FR13-002); ≥6 Kho QA state DA_DUYET cover 6 LV để CB NV tra cứu (✗ chờ T-FR13-006)]
  - **Spec:** FR-X.2-02 step 2-7 + FR-X.2-05 (inbound đánh giá) + SM-TVNHANH; test-plan TC-TVN-002..005
  - **Acceptance:** Phiên transition đầy đủ 4 state; verify `cb_xu_ly_id` set + `noi_dung_tra_loi` lưu + `thoi_gian_xu_ly_phut` calc; xem lịch sử chat bubbles preserve

- 🟢 **T-FR13-004** Workflow Đẩy Nhóm II — CB NV click `[Đẩy sang Nhóm II]` ở phiên CB_TRA_LOI → tạo HOI_DAP `kenh_tiep_nhan=TVN_BRIDGE` + `tu_van_nhanh_goc_id` FK; phiên → HOAN_THANH ghi chú <a id="t-fr13-004"></a>
  - **Cần có sẵn:** [need: ≥1 TU_VAN_NHANH state CB_TRA_LOI (✗ chờ T-FR13-003); BA confirm SM-TVNHANH transition Đẩy Nhóm II (✗ chờ BA — §7 #9 G9)]
  - **Spec:** FR-X.2-02 step 9 + AC line 236 + SRS line 271-272 (preserve history)
  - **Acceptance:** HOI_DAP mới có FK `tu_van_nhanh_goc_id` valid; chat bubbles cũ preserve ở phiên gốc; badge "Từ TV nhanh" hiện ở Nhóm II inbox; verify negative ERR-TVN-03 khi phiên đã HOAN_THANH

### M14 — Kho Q&A seed + lifecycle

- 🟢 **T-FR13-005** Seed Kho QA THU_CONG ≥6 record cover 6 LV (Lao động, Thuế, Đầu tư, DN, KDTM, Hành chính) — UI Modal SCR-X2-01 → state CHO_DUYET <a id="t-fr13-005"></a>
  - **Cần có sẵn:** [need: ≥6 DANH_MUC Lĩnh vực PL DANG_HOAT_DONG (✗ chờ T-FR10-001); account `cb_nv_tw_01`/`_02` login OK]
  - **Spec:** FR-X.2-01 step 3 + BR-FLOW-10; test-plan TC-KHO-001
  - **Acceptance:** ≥6 KHO_CAU_HOI `nguon=THU_CONG`, `trang_thai=CHO_DUYET`, mỗi LV ≥1 record; verify filter `?linh_vuc=X → ≥1` mọi LV

- 🟢 **T-FR13-006** Lifecycle Kho QA CHO_DUYET → DA_DUYET — phê duyệt đơn lẻ + hàng loạt + từ chối → NHAP <a id="t-fr13-006"></a>
  - **Cần có sẵn:** [need: ≥6 Kho QA CHO_DUYET (✗ chờ T-FR13-005); account `cb_pd_tw_01`; BA chốt enum NHAP — §7 #8 G2 (✗ chờ BA)]
  - **Spec:** UC155 + SM-KHOCAUHOI bảng line 457-477; test-plan TC-KHO-004/005/006
  - **Acceptance:** 4 record DA_DUYET (đơn lẻ ≥1 + bulk ≥3), 1 record từ chối → NHAP với lý do BB; audit log INSERT đủ 6 field (action, entity_id, entity_type, actor_id, timestamp, payload_diff)

- 🟢 **T-FR13-007** Auto-feed Kho QA TU_DONG từ FR-02 — verify HD DA_DUYET trigger tạo Q&A `nguon=TU_DONG` + `hoi_dap_goc_id` FK; vào thẳng DA_DUYET không qua CHO_DUYET <a id="t-fr13-007"></a>
  - **Cần có sẵn:** [need: ≥3 HD DA_DUYET tạo TU_DONG Kho QA (✗ chờ T-FR02-XXX); ≥6 LV (✗ chờ T-FR10-001)]
  - **Spec:** FR-X.2-01 step 2 + BR-FLOW-10 + SRS line 114; test-plan TC-KHO-002 + review G1
  - **Acceptance:** ≥3 Q&A `nguon=TU_DONG`, `trang_thai=DA_DUYET` thẳng (verify không có CHO_DUYET intermediate), `hoi_dap_goc_id` valid FK; test idempotency HD DA_DUYET → HUY → DA_DUYET lại không tạo dup

- 🟢 **T-FR13-008** Import xlsx Kho QA — upload .xlsx ≥10 dòng → preview → tạo CHO_DUYET batch `nguon=IMPORT` <a id="t-fr13-008"></a>
  - **Cần có sẵn:** [need: ≥6 LV DANH_MUC (✗ chờ T-FR10-001); template xlsx mẫu (✗ tự tạo)]
  - **Spec:** FR-X.2-01 step 4 + ERR-KHO-04; test-plan TC-KHO-003/NEG-04
  - **Acceptance:** ≥10 row IMPORT CHO_DUYET; negative: upload .csv → ERR-KHO-04; verify "N thành công / M lỗi" report

### FR-X.2-06 — Công khai Q&A (CR-01 + permission)

- 🟢 **T-FR13-009** Công khai / Hủy công khai happy path — Q&A DA_DUYET → API Cổng PLQG OK → CONG_KHAI + `thoi_gian_dang_tai` set; Hủy công khai → DA_DUYET + clear timestamp <a id="t-fr13-009"></a>
  - **Cần có sẵn:** [need: ≥3 Kho QA DA_DUYET với 5 trường công khai filled (✗ chờ T-FR13-006); Cổng PLQG sandbox mTLS up (✗ chờ Infra)]
  - **Spec:** FR-X.2-06 + BR-PUBLIC-01/02/03 + BR-FLOW-05; test-plan TC-CK-001/003/004
  - **Acceptance:** State transition đúng SM-KHOCAUHOI; verify `thoi_gian_dang_tai` format `dd/mm/yyyy hh:mm`; API fail giữ trạng thái cũ + toast ERR-TVN-CK-01; audit log có action `CONG_KHAI`/`HUY_CONG_KHAI`

- 🟢 **T-FR13-010** CR-01 upload boundary 5 trường công khai — `anh_dai_dien` 5MB boundary + `file_dinh_kem_cong_khai` 20MB boundary + MIME deep check + 0-byte reject <a id="t-fr13-010"></a>
  - **Cần có sẵn:** [need: ≥1 Kho QA DA_DUYET (✗ chờ T-FR13-006); file fixture upload (5MB jpg, 5.1MB jpg, .exe rename .jpg, 20MB PDF, 20.1MB PDF, .zip, 0-byte)]
  - **Spec:** CR-01 SRS line 105/107/704-705; test-plan TC-CK-CR01-01/02 (P0 — review G3 + S6)
  - **Acceptance:** `anh_dai_dien`: 5MB OK / 5.1MB reject / .exe rename .jpg reject (MIME header check); `file_dinh_kem`: PDF/DOC/DOCX/XLS/XLSX OK ≤20MB / .zip reject / 0-byte reject; verify error message từ SRS

- 🟢 **T-FR13-011** Permission cross-don_vi FR-X.2-06 — CB_NV_BN BKH KHÔNG được công khai Q&A đơn vị BTC (BR-AUTH-08 + BR-PUBLIC); CB_NV_DP AG KHÔNG thấy Q&A DP khác <a id="t-fr13-011"></a>
  - **Cần có sẵn:** [need: ≥1 Kho QA DA_DUYET tại BTC `don_vi_id=BTC` (✗ chờ T-FR13-006 + `cb_nv_bn_BTC` seed); ≥1 Kho QA DA_DUYET tại CTKH `don_vi_id=CTKH` (✗ chờ T-FR13-006); account `cb_nv_bn_01` BKH + `cb_nv_dp_01` AG]
  - **Spec:** FR-X.2-06 SRS line 461 + BR-AUTH-08 + BR-AUTH-03; test-plan TC-CK-PERM-01/02 (P0 — review G4 + S2 gate Internet)
  - **Acceptance:** CB_NV_BN BKH login → vào list Q&A KHÔNG thấy Q&A BTC HOẶC thấy nhưng nút `[Công khai]` ẩn HOẶC click → 403; capture network 403 response; verify scope filter `don_vi_id` enforce ở BE (curl probe)

### FR-X.2-04 outbound search + cross-cutting

- 🟢 **T-FR13-012** Outbound search API Cổng PLQG read-only — DN search Q&A `DA_DUYET/CONG_KHAI + hieu_luc=true` với Vietnamese diacritics + relevance ranking + scope filter <a id="t-fr13-012"></a>
  - **Cần có sẵn:** [need: ≥6 Kho QA DA_DUYET cover 6 LV (✗ chờ T-FR13-006); endpoint outbound search spec (✗ chờ CĐT — §7 #3); BA confirm scope DA_DUYET vs CONG_KHAI — §7 #2 (✗ chờ BA)]
  - **Spec:** FR-X.2-04 + BR-DATA-08 (GIN full-text); test-plan 03-TC-cong-khai-search.md + review G5/S1
  - **Acceptance:** Search "cà phê" match "ca phe" (diacritics fold); relevance DESC; DN KHÔNG thấy CHO_DUYET/HET_HIEU_LUC/`hieu_luc=false`; boundary tu_khoa 1 ký tự → ERR-TVN-TK-01, 200 ký tự OK, 201 ký tự sanitize (BR-EC-13)

- 🟢 **T-FR13-013** Cross-cutting — Audit log INSERT-only schema verify (6 field) + Idempotency-Key 24h cache + pagination 20/100 boundary <a id="t-fr13-013"></a>
  - **Cần có sẵn:** [need: ≥1 Kho QA CUD action (✗ chờ T-FR13-005/006); ≥1 API inbound đánh giá hoàn tất (✗ chờ T-FR13-003)]
  - **Spec:** BR-DATA-05 line 864 + BR-IDEMPOTENT-01 line 380/426 + BR-DATA-07; test-plan TC-KHO-018/020 + TC-TVN-API-001..004 + review G6/G8/S3/S5
  - **Acceptance:** AUDIT_LOG row có đủ `action_type`, `entity_id`, `entity_type`, `actor_id`, `timestamp`, `payload_diff_jsonb`; UPDATE row → FK/permission deny; idempotent gửi lại cùng key → 409 + edge 24h+1s → tạo mới; pagination `?size=101` → cap 100 hoặc reject; verify request `Idempotency-Key` UUID format

---

## Module bị block (cross-module dependency)

- T-FR13-002 + T-FR13-003 + T-FR13-004 chờ DN seed (FR-07) + endpoint inbound spec BA
- T-FR13-005/006/008 chờ DANH_MUC LV (FR-10 QTHT)
- T-FR13-007 chờ FR-02 HOI_DAP DA_DUYET (Tier 3 upstream)
- T-FR13-009/010/011 chờ Infra Cổng PLQG sandbox mTLS
- T-FR13-006/T-FR13-011 chờ BA confirm SPEC-CLARIFY §7 #8 G2 (enum NHAP) + §7 #9 G9 (SM transition Đẩy Nhóm II) + §7 #2 (scope DA_DUYET/CONG_KHAI)
- T-FR13-012 chờ CĐT spec outbound search endpoint (§7 #3)

---

*Generated 2026-05-12 13:30:00 — Reviser/Todo writer agent. SRS v3.5 authoritative. Plan revision v1.1 applied 8/12 gaps from review (G2/G3/G4/G9 + S2/S5/S6 ≈85%); G1/G6/G7/G11 mapped vào acceptance criteria task tương ứng.*
