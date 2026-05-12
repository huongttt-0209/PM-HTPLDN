# TODO — Cross-cutting Permission (BR-AUTH-01..11)

> File todo module Cross-cutting Permission Matrix — test plan: [test-plan.md](test-plan.md) v1.1 (revised 2026-05-12 13:30:00).
>
> **Tham chiếu shared:** [`state-snapshot.md`](../../../tasks/state-snapshot.md) · [`permission-matrix.md`](../../../output/permission-matrix.md) · [`users.csv`](../../../input/users.csv)
>
> **Trạng thái icon:** 🟢 sẵn sàng · 🔵 đang làm · ✅ xong · ⚠️ partial · 🚫 block · ⏳ chờ upstream · ❌ FAIL
>
> **Tổng:** 25 task (P1 seed 4 + P2 BR-AUTH-01..11 11 task + P3 entity v3.5 mới 5 task + P4 isolation/bypass 3 task + P5 regression 2 task).
>
> **Method:** Chrome DevTools MCP `mcp__chrome-devtools__new_page({isolatedContext: "<role>_<don_vi_ma>_<idx>"})` per role/session — KHÔNG logout-login-lại (memory `qa_htpldn_round5_t01`). API direct probe ưu tiên trước UI cho permission TC (memory `qa_htpldn_qtht_permission_bypass`).

---

## Phase 1 — Seed account & data (P1, 4 task)

- 🟢 **T-PERM-001** Seed 11 role × 3 account (_01/_02/_03) state HOAT_DONG
  - **Kết quả:** 🟢 chờ chạy. Verify `SELECT vai_tro, COUNT(*) FROM TAI_KHOAN WHERE trang_thai='HOAT_DONG' GROUP BY vai_tro` ≥3/role × 11 role = 33 account.
  - **Cần có sẵn:** [need: DON_VI tree TW + 3 BN + 3 ĐP (verify GET /don-vis ≥7)]
  - **Output:** [tasks/state-snapshot.md](../../../tasks/state-snapshot.md) cập nhật TAI_KHOAN distribution.

- 🟢 **T-PERM-002** Seed DN self-reg ≥1 DN HOAT_DONG mỗi ĐP (BR-AUTH-11)
  - **Kết quả:** 🟢 chờ chạy. POST `/api/v1/auth/dn-register` self-reg API (FR-VIII-22), verify GET `/doanh-nghieps?trang_thai=HOAT_DONG GROUP BY don_vi_id` ≥1/ĐP.
  - **Cần có sẵn:** [need: ≥3 ĐP state HOAT_DONG (verify GET /don-vis?cap=ĐP ≥3)]

- 🟢 **T-PERM-003** Seed NHT/TVV/CG advance state DANG_HOAT_DONG (memory `feedback_seed_actor_state_gap`)
  - **Kết quả:** 🟢 chờ chạy. Walk workflow FR-04 tạo TC TV → tạo NHT/CG cho TC → advance state KICH_HOAT → DANG_HOAT_DONG. Verify GET `/nguoi-ho-tros?trang_thai=DANG_HOAT_DONG` + `/tu-van-viens?trang_thai=DANG_HOAT_DONG` + `/chuyen-gias?trang_thai=HOAT_DONG` ≥1/loại × 3 ĐP.
  - **Cần có sẵn:** [need: ≥1 TO_CHUC_TU_VAN DANG_HOAT_DONG mỗi ĐP (verify GET /to-chuc-tu-vans?trang_thai=DANG_HOAT_DONG ≥3)]

- 🟢 **T-PERM-004** Seed VV/YEU_CAU_TU_VAN phân công NHT+TVV+CG (test BR-AUTH-10 lọc kép)
  - **Kết quả:** 🟢 chờ chạy. Tạo ≥1 VV/cấp × 3 cấp (TW/BN/ĐP) phân công `nguoi_ho_tro_id`+`tu_van_vien_id` của user. Tạo ≥1 YEU_CAU_TU_VAN phân công `chuyen_gia_id`.
  - **Cần có sẵn:** [need: ≥1 DN HOAT_DONG mỗi ĐP từ T-PERM-002 (✗ chờ T-PERM-002)] + [need: NHT/TVV/CG state DANG_HOAT_DONG từ T-PERM-003 (✗ chờ T-PERM-003)]

---

## Phase 2 — BR-AUTH-01..11 functional test (P2, 11 task)

- 🟢 **T-PERM-005** BR-AUTH-01 Login Tier 1 user/pass + TOTP 666666
  - **Kết quả:** 🟢 chờ chạy. TC1.1 login OK + TC1.2 missing OTP fail + TC1.3 reject VNeID cho CB nội bộ.
  - **Cần có sẵn:** [need: ≥11 account HOAT_DONG (✗ chờ T-PERM-001)]
  - **Output:** [01-TC-auth-tier1.md](01-TC-auth-tier1.md)

- 🟢 **T-PERM-006** BR-AUTH-02/03/04 Phân cấp 3 tầng + v3.5 2-tier reaffirm
  - **Kết quả:** 🟢 chờ chạy. TC2.1 TW xem all + TC2.2 BN-A vs BN-B = 0 + TC2.3 TW cross-cấp + TC2.4 BN cố xem ĐP = empty (v3.5 reaffirm BN không có ĐP trực thuộc; cite `srs-v3/srs-v3.md:3952` + `permission-matrix.md:4`).
  - **Cần có sẵn:** [need: ≥1 record/đơn vị cho HOI_DAP+VU_VIEC mỗi BN/ĐP (✗ chờ T-PERM-001+T-PERM-004)]
  - **Output:** [02-TC-scope-cap.md](02-TC-scope-cap.md)

- 🟢 **T-PERM-007** BR-AUTH-05 Phê duyệt cùng cấp (CB_PD deny cross-cấp)
  - **Kết quả:** 🟢 chờ chạy. TC3.1 CB_PD_TW deny bản ghi BN; TC3.2 CB_PD_BN deny ĐP; TC3.3 state CHO_PHE_DUYET → DA_DUYET only cùng cấp.
  - **Cần có sẵn:** [need: ≥1 HOI_DAP state CHO_PHE_DUYET mỗi cấp (verify GET /hoi-daps?trang_thai=CHO_PHE_DUYET GROUP BY don_vi_id)]
  - **Output:** [03-TC-approve-same-level.md](03-TC-approve-same-level.md)

- 🟢 **T-PERM-008** BR-AUTH-06 Session timeout 30min idle + token refresh 15min
  - **Kết quả:** 🟢 chờ chạy. TC1.4 idle 30min → redirect /login; TC1.5 refresh token after 15min.
  - **Cần có sẵn:** [need: ≥1 account HOAT_DONG (✗ chờ T-PERM-001)]
  - **Output:** [01-TC-auth-tier1.md](01-TC-auth-tier1.md)

- 🟢 **T-PERM-009** BR-AUTH-07 Lock 5 sai liên tiếp + auto-unlock 30min
  - **Kết quả:** 🟢 chờ chạy. TC1.6 brute-force 5 sai → TAM_KHOA; TC1.7 auto-unlock 30min OR QTHT manual UC113.
  - **Cần có sẵn:** [need: ≥1 throw-away account HOAT_DONG (✗ chờ T-PERM-001)]
  - **Output:** [01-TC-auth-tier1.md](01-TC-auth-tier1.md)

- 🟢 **T-PERM-010** BR-AUTH-08 `don_vi_id` scope + ngoại lệ QTHT/AUDIT_LOG/CB_TW v3.5
  - **Kết quả:** 🟢 chờ chạy. TC4.1 cross-unit isolation; TC4.2 QTHT bypass; TC4.3 v3.5 CB_NV_TW exception VU_VIEC.cong_khai cross-don_vi (cite `srs-update-2026-5-5/_DELTA-MAP-FR05.md:58`).
  - **Cần có sẵn:** [need: ≥1 VU_VIEC cong_khai=1 state HOAN_THANH mỗi ĐP (verify GET /vu-viecs?cong_khai=1&trang_thai=HOAN_THANH ≥1)]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md)

- 🟢 **T-PERM-011** BR-AUTH-09 LGSP mTLS inbound
  - **Kết quả:** 🟢 chờ chạy. TC6.1 missing mTLS → 401; TC6.2 expired token → 401.
  - **Cần có sẵn:** [need: mTLS cert sandbox LGSP active (✗ chờ Infra cấp cert)]
  - **Output:** [06-TC-lgsp-mtls-public.md](06-TC-lgsp-mtls-public.md)

- 🟢 **T-PERM-012** BR-AUTH-10 Lọc kép NHT/TVV/CG + Lớp 1 only dữ liệu chung
  - **Kết quả:** 🟢 chờ chạy. TC5.1 NHT chỉ thấy VV phân công; TC5.2 TVV; TC5.3 CG YEU_CAU_TU_VAN; TC5.6 (Gap #4 review fix) NHT/TVV xem tài liệu ĐT/CTĐT chung Lớp 1 only — KHÔNG filter `nguoi_ho_tro_id`.
  - **Cần có sẵn:** [need: ≥1 VV phân công NHT+TVV (✗ chờ T-PERM-004)] + [need: ≥1 DE_XUAT_DAO_TAO/CHUONG_TRINH_DAO_TAO chung (verify GET /chuong-trinh-dao-taos ≥1)]
  - **Output:** [05-TC-double-filter-actor.md](05-TC-double-filter-actor.md)

- 🟢 **T-PERM-013** BR-AUTH-11 DN API filter (Cổng PLQG)
  - **Kết quả:** 🟢 chờ chạy. TC5.4 DN chỉ thấy hồ sơ của mình qua API `/api/v1/cong-plqg/...`; DN khác → 403/empty.
  - **Cần có sẵn:** [need: ≥2 DN HOAT_DONG khác nhau cho cross-DN test (✗ chờ T-PERM-002)]
  - **Output:** [05-TC-double-filter-actor.md](05-TC-double-filter-actor.md)

- 🟢 **T-PERM-014** v3.5 CR-01 5 trường công khai (HOI_DAP/PHAN_HOI/VU_VIEC/BIEU_MAU/TVCS/TLPL)
  - **Kết quả:** 🟢 chờ chạy. TC6.3 Guest đọc Cổng PLQG khi `cong_khai=1` + state=DA_DUYET; TC6.4 deny khi `cong_khai=0`.
  - **Cần có sẵn:** [need: ≥1 record/entity với `cong_khai=1` (verify GET /entities?cong_khai=1 ≥1 mỗi loại)]
  - **Output:** [06-TC-lgsp-mtls-public.md](06-TC-lgsp-mtls-public.md)

- 🟢 **T-PERM-015** v3.5 C1 Hard-delete + AUDIT_LOG INSERT-only
  - **Kết quả:** 🟢 chờ chạy. TC4.4 DELETE → GET 404 + record không trong list + verify AUDIT_LOG có row action=DELETE (BR-DATA-05, cite `srs-v3/srs-v3.md:3976` — Gap #6 review fix).
  - **Cần có sẵn:** [need: ≥1 record disposable mỗi entity HOI_DAP/BIEU_MAU/VU_VIEC]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md)

---

## Phase 3 — 9 entity mới v3.5 permission (P3, 5 task)

- 🟢 **T-PERM-016** Entity v3.5 NEW: LICH_SU_VU_VIEC read scope
  - **Kết quả:** 🟢 chờ chạy. TC4.6 — 11 role × read scope (immutable audit-like, không CUD). QTHT 👁️ R, CB_NV/PD 👁️ R* scoped, DN 👁️ R* own VV, NHT/TVV 👁️ R* scoped phân công.
  - **Cần có sẵn:** [need: ≥1 VU_VIEC có ≥3 LICH_SU entry (✗ chờ T-PERM-004 + state transitions)]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md) §TC4.6

- 🟢 **T-PERM-017** Entity v3.5 NEW: TU_LIEU_PHAP_LY_VV (BR-FLOW-07 không cần phê duyệt)
  - **Kết quả:** 🟢 chờ chạy. TC4.7 — CB NV ✅ CRUD* + công khai trực tiếp (BR-FLOW-07); CB PD 👁️ R*; DN guest qua `cong_khai=1` Cổng PLQG. Cite §3.4.3.47 + Thay đổi 5+7+8.
  - **Cần có sẵn:** [need: ≥1 VU_VIEC HOAN_THANH (verify GET /vu-viecs?trang_thai=HOAN_THANH ≥1)]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md) §TC4.7

- 🟢 **T-PERM-018** Entity v3.5 NEW: DANH_GIA_CHAT_LUONG_TV (DN 🔌 C† qua API BR-AUTH-11)
  - **Kết quả:** 🟢 chờ chạy. TC4.8 — DN POST `/api/v1/cong-plqg/danh-gia-chat-luong-tv` (own VV); DN khác → 403; CB NV/PD 👁️ R only.
  - **Cần có sẵn:** [need: ≥1 VV HOAN_THANH có CG phân công của DN (✗ chờ T-PERM-004)]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md) §TC4.8

- 🟢 **T-PERM-019** Entity v3.5 NEW: THAM_DINH_HO_SO + PHE_DUYET_CHI_TRA (FR-06 chi-tra)
  - **Kết quả:** 🟢 chờ chạy. TC4.9 THAM_DINH — CB NV ✅ CRU*D scoped `don_vi_id`; CB PD 👁️ R*+Approve cùng cấp. TC4.10 PHE_DUYET_CHI_TRA — CB PD cùng cấp duyệt (BR-AUTH-05); CB NV chỉ 👁️ R*.
  - **Cần có sẵn:** [need: ≥1 CHI_TRA state CHO_THAM_DINH mỗi cấp (verify GET /chi-tras?trang_thai=CHO_THAM_DINH GROUP BY don_vi_id)]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md) §TC4.9-4.10

- 🟢 **T-PERM-020** FR-02 v3.5 MAU_PHAN_HOI Hybrid Model B — action-level MPH_CREATE_TW/BN/DP
  - **Kết quả:** 🟢 chờ chạy. TC4.11 MPH_CREATE_TW: CB_NV_TW POST `pham_vi_ap_dung=TW_QUOC_GIA` → 201; CB_NV_BN/DP → 403. TC4.12 MPH_CREATE_BN. TC4.13 MPH_CREATE_DP. TC4.14 read scope Hybrid (ĐP đọc cross-don_vi mẫu TW_QUOC_GIA; BN KHÔNG thấy mẫu TW). Cite `permission-matrix.md:4` v3.5 FR-02 item (4).
  - **Cần có sẵn:** [need: 1 acc per role CB_NV_TW/BN/DP HOAT_DONG (✗ chờ T-PERM-001)]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md) §TC4.11-4.14

---

## Phase 4 — Isolation cross-unit + QTHT bypass + cross-module leak (P4, 3 task)

- 🟢 **T-PERM-021** Cross-unit isolation DI-04 (BN ngang cấp) + DI-05 (ĐP ngang cấp)
  - **Kết quả:** 🟢 chờ chạy. CB_NV_BN BKH ↔ BTC: HOI_DAP/VU_VIEC query → 0 row hoặc 403. CB_NV_DP AG ↔ BG ↔ BNI: tương tự. MCP isolated context 2 session parallel: `cb_nv_bn_BKH_s1` + `cb_nv_bn_BTC_s2`.
  - **Cần có sẵn:** [need: ≥1 HOI_DAP+VU_VIEC mỗi BN khác nhau + mỗi ĐP khác nhau (✗ chờ T-PERM-001+T-PERM-004)]
  - **Output:** [08-TC-isolation-cross-unit.md](08-TC-isolation-cross-unit.md)

- 🟢 **T-PERM-022** QTHT permission bypass probe API (memory `qa_htpldn_qtht_permission_bypass`)
  - **Kết quả:** 🟢 chờ chạy. Probe API trực tiếp trước UI: QTHT DELETE/PATCH/POST `/api/v1/tu-van-viens` + `/api/v1/nguoi-ho-tros` (matrix v3.5: 👁️ R only sau BA chốt 2026-05-09) → expect 403, KHÔNG 200. Lặp cho TAI_KHOAN, DON_VI, AUDIT_LOG (matrix CRUD/R cụ thể).
  - **Cần có sẵn:** [need: QTHT acc HOAT_DONG (✗ chờ T-PERM-001)] + [need: ≥1 TU_VAN_VIEN + NGUOI_HO_TRO record (✗ chờ T-PERM-003)]
  - **Output:** [07-TC-role-qtht.md](07-TC-role-qtht.md)

- 🟢 **T-PERM-023** Deep-link bypass 11 role × 5 module
  - **Kết quả:** 🟢 chờ chạy. Truy cập deep link URL không có quyền per role: vd CB_NV_DP → `/quan-tri/danh-muc` (FR-10) → expect 403/redirect, KHÔNG render thành công. 11 role × 5 module high-risk = 55 deep-link probe.
  - **Cần có sẵn:** [need: 11 role × ≥1 acc HOAT_DONG (✗ chờ T-PERM-001)]
  - **Output:** [07-TC-role-*.md](.) (inline trong 11 file role)

---

## Phase 5 — Regression API/UI quirks (P5, 2 task)

- 🟢 **T-PERM-024** API double-wrap regression (memory `qa_htpldn_api_wrap_bug`)
  - **Kết quả:** 🟢 chờ chạy. Verify dropdown DON_VI + VAI_TRO render khi BE wrap envelope 2 lần. curl response shape: `{"data": {"data": [...]}}` → check FE unwrap đúng. Permission test thường gặp dropdown rỗng do double-wrap → false negative "role không có quyền".
  - **Cần có sẵn:** [need: QTHT acc HOAT_DONG cho UI test (✗ chờ T-PERM-001)]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md) §TC4.x regression

- 🟢 **T-PERM-025** C2 ClamAV remove — file upload security regression
  - **Kết quả:** 🟢 chờ chạy. Upload `.exe`/`.bat`/`.docm`/`.zip` → BE behavior verify (extension whitelist + magic-byte check). Cite `srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md` §C2 lines 81-84. Verify R7.8.2 đã PASS — extension whitelist + magic-byte FIXED R9 commit c304b8fc, không regression.
  - **Cần có sẵn:** [need: 1 acc CB_NV HOAT_DONG có quyền upload (✗ chờ T-PERM-001)]
  - **Output:** [04-TC-don-vi-id-scope.md](04-TC-don-vi-id-scope.md) §TC4.x security

---

## Bug-report tracking (placeholder — chưa có bug)

Khi gặp bug trong run, log vào `output/qa-reports/round{N}/bug-reports/cross-cutting/bug-report-r{N}-T-PERM-{XXX}-<slug>.md` theo template 6 sections strict (CLAUDE.md §Bug-report folder discipline + memory `feedback_bug_report_template_strict`).

---

## Note tracking

> **Note 2026-05-12 13:30:00 — todo.md generated** từ test-plan.md v1.1 revised. 25 task chia 5 phase. Method: MCP isolated context per role (`<role>_<don_vi_ma>_<idx>`); API probe trước UI cho permission TC (memory `qa_htpldn_qtht_permission_bypass`); seed actor 2 task tách create + advance state (memory `feedback_seed_actor_state_gap`); dep `[need: state ...]` format Rule 2 CLAUDE.md.
