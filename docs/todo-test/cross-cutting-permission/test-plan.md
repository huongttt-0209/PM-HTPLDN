# Kế Hoạch Kiểm Thử — Permission Cross-Cutting (BR-AUTH-01..11)

> **Phiên bản**: 1.1
> **Ngày tạo**: 2026-05-12 14:30:00 — **Revised 2026-05-12 13:30:00** (apply review.md REVISE — fix 10 gap + 8 suggestion, ≥80% áp dụng)
> **Nguồn dữ liệu**: LOCAL (`srs-v3/srs-v3.md` Phụ lục B + `srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md` + `_DELTA-MAP-FR05.md` cho BR-AUTH-08 v3.5 exception)
> **SRS Reference**: BR-AUTH-01..11 (Phụ lục B `srs-v3/srs-v3.md:3945-3966`), Permission Matrix (`output/permission-matrix.md` — 49 entity × 11 role, v3.5 updated 2026-05-09), v3.5 update (`srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md` + `_DELTA-MAP-FR05.md` cho exception "Cán bộ Trung ương"), §3.2.0.4 BR-DATA-02 + BR-AUTH-08/10/11 tổng hợp (`srs-v3/srs-v3.md:661-695`)
> **Module type**: Cross-cutting (M) — KHÔNG thuộc 1 FR đơn lẻ; áp dụng TOÀN HỆ THỐNG
> **SOURCE MODE**: LOCAL

> **Mục đích:** Test plan cross-cutting validate **phân quyền theo cấp + đơn vị + role × entity** trên toàn 49 entity × 11 role × {C,R,U,D,Approve,Export}. Áp dụng song song với mọi test plan module (`fr-02`..`fr-15`) — mỗi module có TC permission scope-local, plan này cover scope-cross-module + isolation cross-unit + ngoại lệ BR-AUTH-08 v3.5 (2-tier permission BN không có ĐP trực thuộc).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Cross-cutting validation:** 11 role × 49 entity × {C, R, U, D, Approve, Export} → max ≥ 6.474 ô lý thuyết, plan này sample ~30 TC cover các pattern chính.
- **Bảng dữ liệu chính:** TAI_KHOAN, VAI_TRO, QUYEN_HAN, DON_VI + 49 entity nghiệp vụ trong [`output/permission-matrix.md`](../../../output/permission-matrix.md).
- **Màn hình:** KHÔNG có SCR-XXX riêng — plan này cross-cutting, dùng SCR của module owning entity (vd VU_VIEC dùng SCR-V.I-01, BIEU_MAU dùng SCR-IX-01).

### 1.2 Phạm vi 6 nhóm test

| # | Nhóm | BR ref | Mô tả | TC file |
|---|------|--------|-------|---------|
| 1 | Auth Tier 1 (login + TOTP) | BR-AUTH-01, BR-AUTH-06, BR-AUTH-07 | Login user/pass + OTP 666666; session timeout 30 min idle; lock 5 sai liên tiếp | `01-TC-auth-tier1.md` |
| 2 | Phân cấp 3 tầng | BR-AUTH-02, BR-AUTH-03, BR-AUTH-04 | TW thấy con; BN không thấy ĐP (v3.5 2-tier — không có ĐP trực thuộc BN); ngang cấp không thấy nhau | `02-TC-scope-cap.md` |
| 3 | Phê duyệt cùng cấp | BR-AUTH-05 | CB_PD_TW không duyệt bản ghi BN/ĐP; CB_PD_BN không duyệt bản ghi ĐP | `03-TC-approve-same-level.md` |
| 4 | Data scope theo `don_vi_id` | BR-AUTH-08 | Mọi bảng có cột `don_vi_id` → filter; ngoại lệ QTHT (all) + AUDIT_LOG (immutable) + v3.5 "CB Trung ương" exception | `04-TC-don-vi-id-scope.md` |
| 5 | Lọc kép NHT/TVV/CG + DN API | BR-AUTH-10, BR-AUTH-11 | NHT/TVV chỉ thấy VV được phân công + DN chỉ thấy hồ sơ của mình qua API | `05-TC-double-filter-actor.md` |
| 6 | LGSP inbound + Cổng PLQG public | BR-AUTH-09 + v3.5 CR-01 5 trường công khai | mTLS verify + Guest đọc qua chuyên trang khi `cong_khai=1` | `06-TC-lgsp-mtls-public.md` |
| 7 | Permission matrix per role | Master `output/permission-matrix.md` | 1 file/role × ≥3 TC sample = 11×3 = 33 TC | `07-TC-role-{role}.md` (11 file) |
| 8 | Isolation cross-unit | BR-AUTH-03 + BR-AUTH-08 | DI-04 (BN ngang cấp) + DI-05 (ĐP ngang cấp) | `08-TC-isolation-cross-unit.md` |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Đơn vị | Dùng cho TC |
|------|-----|----------------------|--------|-------------|
| QTHT | — | `qtht_01` / `admin` | (root, all scope) | TC1-8 baseline (xem all) |
| CB_NV_TW | TW | `cb_nv_tw_01` | BTP-TW | TC2-4 scope con; TC3 không phải approver |
| CB_PD_TW | TW | `cb_pd_tw_01` | BTP-TW | TC3 approve TW; deny ĐP/BN |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH) / `cb_nv_bn_02` (BTC) | BKH/BTC | TC2 ngang cấp; TC8 isolation DI-04 |
| CB_PD_BN | BN | `cb_pd_bn_01` (BKH) | BKH | TC3 approve BN only |
| CB_NV_DP | ĐP | `cb_nv_dp_01` (AG) / `cb_nv_dp_02` (BG) / `cb_nv_dp_03` (BNI) | STP-AG/BG/BNI | TC2 ngang cấp; TC8 isolation DI-05 |
| CB_PD_DP | ĐP | `cb_pd_dp_01` (AG) | STP-AG | TC3 approve ĐP only |
| DN | ĐP | `dn_user_01` `[need: ≥1 DN HOAT_DONG (verify GET /doanh-nghieps?status=HOAT_DONG ≥1)]` | trực thuộc Sở TP | TC5 lọc API + chỉ hồ sơ của DN mình |
| NHT | ĐP | `nht_user_01` `[need: ≥1 NGUOI_HO_TRO DANG_HOAT_DONG mỗi cấp (verify GET /nguoi-ho-tros?trang_thai=DANG_HOAT_DONG GROUP BY don_vi_id ≥1)]` | Tổ chức HT PLDN dưới STP | TC5 lọc kép VV được phân công |
| TVV | ĐP | `tvv_user_01` `[need: ≥1 TU_VAN_VIEN DANG_HOAT_DONG (verify GET /tu-van-viens?trang_thai=DANG_HOAT_DONG ≥1)]` | MLTV dưới STP | TC5 lọc kép VV được phân công |
| CG | ĐP | `cg_user_01` `[need: ≥1 CG state HOAT_DONG có YEU_CAU_TU_VAN phân công (verify GET /yeu-cau-tu-vans?chuyen_gia_id=<user.id> ≥1)]` | Tổ chức HT PLDN dưới STP | TC5 lọc kép YEU_CAU_TU_VAN |

> **Account suffix convention:** `_01` primary session 1, `_02` session 2 (parallel), `_03` permission test dedicated (CUD scoping), `_04` buffer. Source: [`input/test-accounts-isolation.csv`](../../../input/test-accounts-isolation.csv) §SESSION PIN.
> **State marker workflow (Gap #9 review fix):** Mọi account dùng cho TC §4 BẮT BUỘC verify state qua `[need: ≥N entity state X (verify query)]` per CLAUDE.md §State marker workflow Rule 2. Single source: [`tasks/state-snapshot.md`](../../../tasks/state-snapshot.md). Hook `auto-rescan-todo.py` tự flip ⏳→🟢 khi marker `(✓ N)`.
> **Multi-role isolation pattern (MCP):** dùng `mcp__chrome-devtools__new_page({isolatedContext: "<role>_<don_vi_ma>_<session_idx>"})` per role + session — KHÔNG logout-login-lại (BE httpOnly cookie + localStorage sticky cross-session = role contamination). Vd: `cb_nv_bn_BKH_s1` + `cb_nv_bn_BTC_s1` cho TC isolation DI-04. Source: memory `qa_htpldn_round5_t01`.

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR-AUTH-01..11 + impact entity v3.5)

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|----------------|---------------------|------------|
| BR-AUTH-01 | Mọi user phải xác thực trước khi truy cập. Tier 1 (MVP) user/pass + TOTP 2FA qua email; Tier 2 VNPT eKYC; Tier 3 SSO VNeID OIDC (NĐ69/2024). VNeID chỉ áp dụng TVV/CG/NHT bên ngoài. Cán bộ nội bộ luôn user/pass + TOTP. | `srs-v3/srs-v3.md:3949` | Toàn bộ | "API outbound không yêu cầu session (dùng token xác thực)" | TC1.1 login Tier 1; TC1.2 missing OTP; TC1.3 reject VNeID cho CB nội bộ |
| BR-AUTH-02 | Phân cấp 3 tầng TW → BN/ĐP. TW là cấp cao nhất (Cục BLDS&KT). | `srs-v3/srs-v3.md:3950` | Toàn bộ | — | TC2.1 verify cây đơn vị seed |
| BR-AUTH-03 | **Ngang cấp KHÔNG thấy nhau.** BN chỉ thấy dữ liệu BN mình; ĐP chỉ thấy ĐP mình; BN không thấy ĐP và ngược lại. | `srs-v3/srs-v3.md:3951` | Toàn bộ FR có phân quyền | "QTHT thấy tất cả" | TC2.2 BN A query data BN B → 0 row; TC8 DI-04/DI-05 |
| BR-AUTH-04 | **Cấp cha thấy cấp con.** TW thấy TW+BN+ĐP. BN chỉ thấy BN mình (KHÔNG thấy ĐP trực thuộc BN). | `srs-v3/srs-v3.md:3952` | Toàn bộ FR scoped | "**BN KHÔNG thấy ĐP**" (v3.5 reaffirm — 2-tier permission, BN không có ĐP trực thuộc theo FR-V.I refactor) | TC2.3 TW xem cross-cấp; TC2.4 BN cố xem ĐP → empty |
| BR-AUTH-05 | **Phê duyệt cùng cấp.** CB NV cấp nào tạo → CB PD cùng cấp duyệt. KHÔNG xuyên cấp. | `srs-v3/srs-v3.md:3955` | FR-II-08, FR-III-15/18, FR-IV-07, FR-V.I-13, FR-V.II-12, FR-VI-04/09, FR-XI-04 | — | TC3.1 CB_PD_TW deny BN; TC3.2 CB_PD_BN deny ĐP |
| BR-AUTH-06 | Session CMS: 30 phút idle timeout. API token TTL 15 phút, refresh 24 giờ. Hết hạn → redirect login. | `srs-v3/srs-v3.md:3956` | FR-VIII-20/21 | — | TC1.4 idle 30min → kick login; TC1.5 refresh token after 15min |
| BR-AUTH-07 | Khóa tài khoản sau 5 lần sai mật khẩu liên tiếp. Auto-unlock sau 30 phút HOẶC QTHT mở thủ công qua UC113. | `srs-v3/srs-v3.md:3957` | FR-VIII-20 | — | TC1.6 brute-force 5 sai → TAM_KHOA; TC1.7 auto-unlock 30min |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` áp dụng cho MỌI bảng có cột `don_vi_id`. Không exception ngoại trừ QTHT. | `srs-v3/srs-v3.md:3958` + tổng hợp `srs-v3/srs-v3.md:661-695` (§3.2.0.4) | Toàn bộ | "AUDIT_LOG không có phân quyền theo đơn vị (immutable)"; **v3.5 ngoại lệ mới:** "ngoại trừ QTHT và **Cán bộ Trung ương**" — fix V4-CHƯA-SỬA #1 cite chính xác `srs-update-2026-5-5/_DELTA-MAP-FR05.md:58` + `output/permission-matrix.md:4` (KHÔNG phải `_DELTA-MAP-CROSS-CUTTING.md` — file đó chỉ chứa C1/C2/C3, exception nằm trong delta FR-05) | TC4.1 cross-unit isolation; TC4.2 QTHT bypass scope; TC4.3 v3.5 CB_NV_TW exception VU_VIEC.cong_khai |
| BR-AUTH-09 | mTLS LGSP inbound: token + mTLS cert. Verify issuer/audience/expiry. | `srs-v3/srs-v3.md:3959` | FR-V.I (UC53), FR-V.II (UC68) | — | TC6.1 missing mTLS → 401; TC6.2 expired token → 401 |
| BR-AUTH-10 | **Lọc kép NHT/TVV/CG (NĐ77/2008):** Lớp 1 don_vi_id (Sở TP) + Lớp 2 nguoi_ho_tro_id/tu_van_vien_id = current user (NHT/TVV) hoặc chuyen_gia_id = current user (CG). Áp cho entity VV/yêu cầu TV, KHÔNG áp dữ liệu chung. | `srs-v3/srs-v3.md:3963` | FR-IV (UC41-42), FR-V.I (UC60, UC65), FR-X.1 (UC147-153) | "Dữ liệu chung (UC21, UC27): chỉ Lớp 1" | TC5.1 NHT chỉ thấy VV phân công; TC5.2 TVV; TC5.3 CG YEU_CAU_TU_VAN; **TC5.6 NHT/TVV xem tài liệu ĐT/CTĐT chung (UC21/UC27) — chỉ áp Lớp 1, KHÔNG filter `nguoi_ho_tro_id`** |
| BR-AUTH-11 | **Lọc API cho DN (Cổng PLQG):** DN KHÔNG đăng nhập CMS. API filter `don_vi_id` (Sở TP) + `doanh_nghiep_id` (token DN). | `srs-v3/srs-v3.md:3964` | FR-V.I (UC52, UC64, UC67), FR-X.1 (UC147, UC153), FR-X.2 (UC160-162), FR-III (UC23) | — | TC5.4 DN chỉ thấy hồ sơ của mình qua API |
| **v3.5 CR-01** | 5 trường công khai chuẩn (`cong_khai`, `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`) áp HOI_DAP/PHAN_HOI/VU_VIEC/BIEU_MAU/TVCS/TLPL → Guest read qua Cổng PLQG khi `cong_khai=1`. | `srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md` + permission-matrix line 4 | FR-02/FR-05/FR-09/FR-12 | Chỉ visible khi `cong_khai=1` AND state=`DA_DUYET`/`HOAN_THANH` | TC6.3 Guest đọc public; TC6.4 deny khi `cong_khai=0` |
| **v3.5 C1 Hard-delete** | Bỏ trạng thái DA_XOA. DELETE = hard delete khỏi DB. | `srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md` §C1 | Toàn bộ 12 file SRS impact | "AUDIT_LOG INSERT-only — vẫn ghi action DELETE" (BR-DATA-05) | TC4.4 DELETE → GET 404 / record không trong list |

> **Bổ sung BR specific cross-cutting v3.5 — 9 entity mới (apply matrix all roles):** NGUOI_HO_TRO, TO_CHUC_TU_VAN, NGAY_LE, PHAN_CONG_VU_VIEC, DANH_GIA_VU_VIEC, LICH_SU_VU_VIEC, HO_SO_PHAP_LY_DN, TU_LIEU_PHAP_LY_VV, DANH_GIA_CHAT_LUONG_TV, THAM_DINH_HO_SO, PHE_DUYET_CHI_TRA, DOT_BAO_CAO, DOANH_NGHIEP_LINH_VUC, DANH_GIA_SAU_VU_VIEC. Cite: `output/permission-matrix.md` lines 9-17 + delta-map cross-cutting line 167.

### 2.2 Error Codes (Auth + Permission)

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Severity |
|--------|-------------------|----------------------|----------|
| HTTP 401 | Token thiếu / expired / signature sai | (HTTP standard) | ERROR |
| HTTP 403 | User authenticated nhưng vi phạm scope (BR-AUTH-03/04/05/08/10/11) | (HTTP standard, app trả message tùy module) | ERROR |
| ERR-SYS-02 | Conflict update đồng thời | "Bản ghi đã bị thay đổi bởi người khác. Vui lòng tải lại trang" (`srs-v3/srs-v3.md:690`) | ERROR |
| ERR-PARAM-01 | Pagination ngoài [1,100] | "Tham số phân trang không hợp lệ" (`srs-v3/srs-v3.md:692`) | ERROR |
| (ERR-AUTH-LOCKED-01) | Login khi state TAM_KHOA | "Tài khoản tạm khóa" (UI toast, cite memory `qa_htpldn_round5_t01`) | ERROR |
| (ERR-AUTH-INVALID-01) | Sai mật khẩu/username | "Invalid credentials" / "Sai tên đăng nhập hoặc mật khẩu" | ERROR |

> ⚠️ Message phải quote nguyên văn từ SRS. ERR-AUTH-* mã ngoặc chưa có SRS spec cụ thể — verify message thực tế từ UI khi log bug.

### 2.3 Permission Matrix master (11 role × ≥15 entity sample — bổ sung 5 entity v3.5 mới)

> **Reference đầy đủ:** [`output/permission-matrix.md`](../../../output/permission-matrix.md) — 11 role × 49 entity. Bảng dưới sample ≥15 entity high-impact (gồm toàn bộ entity v3.5 NEW/CHANGED) để verify trong TC §4. Cột **v3.5 status**: `LEGACY` (không đổi v3 → v3.5), `CHANGED` (entity cũ đổi quyền), `NEW` (entity mới hoàn toàn v3.5).

| Entity | **v3.5 status** | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | DN | NHT | TVV | CG |
|--------|:---------------:|:----:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--:|:---:|:---:|:--:|
| HOI_DAP (FR-02) | CHANGED (+5 cong_khai + `don_vi_id` CR-06) | 👁️ R | ✅ CRU*D | ✅ CRU*D | ✅ CRU*D | ✅ R*+Approve | ✅ R*+Approve | ✅ R*+Approve | 🔌 C† | ❌ | ❌ | ❌ |
| MAU_PHAN_HOI (FR-02 v3.5 Hybrid Model B) | CHANGED (action-level perm) | 👁️ R | `MPH_CREATE_TW` | `MPH_CREATE_BN` | `MPH_CREATE_DP` | 👁️ R* | 👁️ R* | 👁️ R* | ❌ | ❌ | ❌ | ❌ |
| TU_VAN_VIEN (FR-04) | LEGACY | 👁️ R | ✅ CRU*D | ✅ CRU*D | ✅ CRU*D | 👁️ R*+Approve | 👁️ R*+Approve | 👁️ R*+Approve | ❌ | ❌ | (self R) | ❌ |
| NGUOI_HO_TRO `[v3.5 BA 2026-05-09]` | CHANGED (QTHT ✅→👁️ R) | 👁️ R | ✅ CRU*D | ✅ CRU*D | ✅ CRU*D | 👁️ R* | 👁️ R* | 👁️ R* | ❌ | (self R) | ❌ | ❌ |
| TO_CHUC_TU_VAN | NEW | 👁️ R | ✅ CRU*D | ✅ CRU*D | ✅ CRU*D | 👁️ R* | 👁️ R* | 👁️ R* | ❌ | ❌ | ❌ | ❌ |
| VU_VIEC (FR-05) | CHANGED (+ exception CB_TW BR-AUTH-08 + cong_khai public) | 👁️ R | ✅ CRU*D (+TW exception cross-don_vi) | ✅ CRU*D | ✅ CRU*D | 👁️ R*+Approve | 👁️ R*+Approve | 👁️ R*+Approve | 🔌 C†R* | 📝 RU* (BR-AUTH-10) | 📝 RU* (BR-AUTH-10) | ❌ |
| PHAN_CONG_VU_VIEC | NEW | 👁️ R | ✅ CRU* | ✅ CRU* | ✅ CRU* | 👁️ R* | 👁️ R* | 👁️ R* | ❌ | 📝 RU* | 📝 RU* | 📝 RU* |
| DANH_GIA_VU_VIEC | NEW | 👁️ R | ✅ CRU*D | ✅ CRU*D | ✅ CRU*D | 👁️ R* | 👁️ R* | 👁️ R* | 🔌 C† (own VV) | 📝 RU* | 📝 RU* | ❌ |
| LICH_SU_VU_VIEC `[v3.5 NEW]` | NEW (immutable audit-like) | 👁️ R | 👁️ R* | 👁️ R* | 👁️ R* | 👁️ R* | 👁️ R* | 👁️ R* | 👁️ R* (own VV) | 👁️ R* (scoped) | 👁️ R* (scoped) | ❌ |
| DOANH_NGHIEP (FR-07) | CHANGED (CB_NV bỏ Create, DN self-reg API) | 👁️ R | 👁️ R (no C v3.5) | 👁️ R | 👁️ R | 👁️ R*+Approve | 👁️ R*+Approve | 👁️ R*+Approve | 🔌 C† self-reg | ❌ | ❌ | ❌ |
| BIEU_MAU (FR-09) | CHANGED (+5 cong_khai CR-01) | 👁️ R | ✅ CRU*D | ✅ CRU*D | ✅ CRU*D | 👁️ R*+Approve | 👁️ R*+Approve | 👁️ R*+Approve | 👁️ R* khi `cong_khai=1` | 👁️ R* | 👁️ R* | ❌ |
| TAI_KHOAN (FR-10) | LEGACY | ✅ CRUD | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| DON_VI (FR-10) | CHANGED (v3.5 2-tier TW + BN/ĐP ngang cấp) | ✅ CRUD | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| AUDIT_LOG (FR-10) | LEGACY (no scope filter) | 👁️ R (no `don_vi_id` filter) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| TU_VAN_CHUYEN_SAU (FR-12 v3.5 rename) | CHANGED (rename NOI_DUNG_TU_VAN_CS → TVCS + cong_khai) | 👁️ R | ✅ CRU*D | ✅ CRU*D | ✅ CRU*D | 👁️ R*+Approve | 👁️ R*+Approve | 👁️ R*+Approve | 🔌 R public | 📝 RU* (BR-AUTH-10) | 📝 RU* (BR-AUTH-10) | 📝 RU* (BR-AUTH-10 CG) |
| HO_SO_PHAP_LY_DN `[v3.5 NEW]` | NEW (FR-X.1-46) | 👁️ R | ✅ CRUD* | ✅ CRUD* | ✅ CRUD* | 👁️ R* | 👁️ R* | 👁️ R* | 👁️ R* (own) | 📝 RU* (scoped VV) | ❌ | ❌ |
| TU_LIEU_PHAP_LY_VV `[v3.5 NEW]` | NEW (FR-X.1-47, BR-FLOW-07 không cần PD) | 👁️ R | ✅ CRUD* + công khai trực tiếp | ✅ CRUD* + công khai trực tiếp | ✅ CRUD* + công khai trực tiếp | 👁️ R* | 👁️ R* | 👁️ R* | 👁️ R* khi `cong_khai=1` (Cổng PLQG) | ❌ | ❌ | ❌ |
| DANH_GIA_CHAT_LUONG_TV `[v3.5 NEW]` | NEW (FR-X.1-48) | 👁️ R | 👁️ R | 👁️ R | 👁️ R | 👁️ R* | 👁️ R* | 👁️ R* | 🔌 C† (own VV qua API BR-AUTH-11) | ❌ | ❌ | ❌ |
| THAM_DINH_HO_SO `[v3.5 NEW FR-06]` | NEW (FR-06 chi-tra) | 👁️ R | ✅ CRU*D | ✅ CRU*D | ✅ CRU*D | 👁️ R*+Approve | 👁️ R*+Approve | 👁️ R*+Approve | ❌ | ❌ | ❌ | ❌ |
| PHE_DUYET_CHI_TRA `[v3.5 NEW FR-06]` | NEW (FR-06 chi-tra) | 👁️ R | 👁️ R* | 👁️ R* | 👁️ R* | ✅ R*+Approve | ✅ R*+Approve | ✅ R*+Approve | ❌ | ❌ | ❌ | ❌ |

> Ghi chú ký hiệu xem [permission-matrix.md §Ký hiệu](../../../output/permission-matrix.md#ký-hiệu) lines 21-37.
>
> **Bổ sung TC §4 cho 5 entity v3.5 mới** (Gap #3 review fix):
> - **TC4.6** LICH_SU_VU_VIEC read scope per role × cấp (immutable audit-like, không CUD).
> - **TC4.7** TU_LIEU_PHAP_LY_VV — CB NV công khai trực tiếp (BR-FLOW-07 không cần PD); DN guest qua `cong_khai=1`.
> - **TC4.8** DANH_GIA_CHAT_LUONG_TV — DN 🔌 C† qua API self-reg BR-AUTH-11 (DN không đăng nhập CMS).
> - **TC4.9** THAM_DINH_HO_SO — FR-06 chi-tra CB NV/PD scoped `don_vi_id`.
> - **TC4.10** PHE_DUYET_CHI_TRA — CB PD cùng cấp duyệt (BR-AUTH-05); CB NV chỉ 👁️ R*.
>
> **Bổ sung TC action-level MPH_CREATE (Suggestion #3):**
> - **TC4.11** MPH_CREATE_TW: CB_NV_TW POST `/mau-phan-hois` với `pham_vi_ap_dung=TW_QUOC_GIA` → 201; CB_NV_BN/CB_NV_DP POST same → 403.
> - **TC4.12** MPH_CREATE_BN: CB_NV_BN POST `pham_vi_ap_dung=BN_<X>` → 201; CB_NV_TW/CB_NV_DP POST → 403.
> - **TC4.13** MPH_CREATE_DP: CB_NV_DP POST `pham_vi_ap_dung=DP_<Y>` → 201; CB_NV_TW/CB_NV_BN POST → 403.
> - **TC4.14** MPH read scope Hybrid Model B: ĐP đọc cross-don_vi mẫu `TW_QUOC_GIA`; BN KHÔNG thấy mẫu TW (FR-II-NEW-02). Cite `permission-matrix.md:4` v3.5 FR-02 item (4).

### 2.4 UI Layout

> ⚠️ **N/A — Cross-cutting plan KHÔNG có SCR-XXX riêng.** Phân quyền là layer ngang (ai có quyền), KHÔNG có UI riêng. UI test theo từng module owning entity:
> - HOI_DAP → SCR-II-01..04
> - VU_VIEC → SCR-V.I-01..05 (v3.5 thêm 04 + 05 cho DN)
> - BIEU_MAU → SCR-IX-01..03
> - TAI_KHOAN → SCR-VIII-02
>
> Cross-cutting plan này KHÔNG test layout. Test scope: menu visibility (hide menu cho role không có quyền) + button visibility (hide Create/Edit/Delete khi không có quyền) + record list filtered scope + 403 redirect khi truy cập deep link.

### 2.5 State Machine

> ⚠️ **N/A — Cross-cutting plan KHÔNG có state machine riêng.** Mỗi entity có SM riêng (SM-HOIDAP 9 state, SM-VUVIEC, SM-TVV, ...). Plan này chỉ test **state-gated permission** (vd CB_PD cùng cấp duyệt = chuyển state CHO_PHE_DUYET → DA_DUYET, role khác không trigger được transition).

State transitions liên quan BR-AUTH-05 (verified `srs-v3/srs-v3.md:4143-4408`):

| Transition | Trigger role required | Entity | TC |
|------------|------------------------|--------|----|
| CHO_PHE_DUYET → DA_DUYET | CB PD cùng cấp | HOI_DAP, BIEU_MAU, CTĐT, VU_VIEC, CHI_TRA, KE_HOACH_DANH_GIA, CT_HTPL | TC3.3 |
| CHO_KICH_HOAT → HOAT_DONG | QTHT only | TAI_KHOAN | TC4.5 |
| HOAT_DONG → TAM_KHOA | Auto (5 sai) / QTHT manual | TAI_KHOAN | TC1.6 |
| TAM_KHOA → HOAT_DONG | QTHT manual OR auto 30 min | TAI_KHOAN | TC1.7 |

### 2.6 Data dependencies & Seed

| Phase | Input | Section dùng |
|-------|-------|--------------|
| **Account seed (P1)** | [`input/users.csv`](../../../input/users.csv) (154 row, schema mới) | 4 replica/role+cấp × 11 role = ≥34 account |
| **DN/NHT/TVV/CG seed (P2)** | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) + [`input/flow-module.md`](../../../input/flow-module.md) §FR-04 + §FR-07 | DN self-reg API (BR-AUTH-11) + advance NHT/TVV state to DANG_HOAT_DONG (memory `feedback_seed_actor_state_gap` R1) |
| **VU_VIEC seed (P3)** | flow-module §FR-05 + permission-matrix v3.5 update FR-05 | ≥1 VV/cấp × 3 cấp (TW/BN/ĐP) phân công NHT+TVV để test BR-AUTH-10 lọc kép |
| **Cross-unit data (P4)** | DI-04 (BN BKH ↔ BTC ↔ BCT) + DI-05 (ĐP AG ↔ BG ↔ BNI) | Seed data ≥1 record/đơn vị cho HOI_DAP/VU_VIEC/BIEU_MAU |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | 18 entity × tạo tại/đọc tại |

**Upstream dependencies (Tier check):**

| Entity | Tier | Phụ thuộc upstream | Seed trước tại module |
|--------|:----:|--------------------|----------------------|
| TAI_KHOAN (11 role × 4 replica) | 1 | DON_VI tree (TW + 3 BN + 3 ĐP) | FR-10 §Quản trị TK |
| DN | 2 | DON_VI ĐP + self-reg API | FR-07 self-reg |
| NHT/TVV/CG | 2 | TO_CHUC_TU_VAN (NHT/CG) / MLTV (TVV) state DANG_HOAT_DONG | FR-04 walk workflow |
| VU_VIEC | 3 | DN + NHT (phân công nguoi_ho_tro_id) + TVV (tu_van_vien_id) | FR-05 workflow |
| YEU_CAU_TU_VAN | 4 | VU_VIEC + CG (phân công chuyen_gia_id) | FR-12 workflow |

> **Single source state count:** [`tasks/state-snapshot.md`](../../../tasks/state-snapshot.md). Trước mỗi TC mark ⏳/🟢/✅, re-run verify command per BR-AUTH dep marker `[need: ...]` (format Rule 2 §State marker workflow CLAUDE.md).

---

## 3. Cấu Trúc File Test Case

```
docs/todo-test/cross-cutting-permission/
├── test-plan.md                        ← File này (overview)
├── 01-TC-auth-tier1.md                 ← Login + TOTP + lock + idle timeout (BR-AUTH-01/06/07)
├── 02-TC-scope-cap.md                  ← Phân cấp TW/BN/ĐP (BR-AUTH-02/03/04 + v3.5 2-tier)
├── 03-TC-approve-same-level.md         ← Phê duyệt cùng cấp (BR-AUTH-05)
├── 04-TC-don-vi-id-scope.md            ← don_vi_id filter + ngoại lệ QTHT/AUDIT_LOG/CB_TW v3.5 (BR-AUTH-08) + Hard-delete v3.5
├── 05-TC-double-filter-actor.md        ← Lọc kép NHT/TVV/CG (BR-AUTH-10) + DN API (BR-AUTH-11)
├── 06-TC-lgsp-mtls-public.md           ← mTLS LGSP inbound (BR-AUTH-09) + Cổng PLQG public CR-01
├── 07-TC-role-qtht.md                  ← Role QTHT — sample 3 TC × 5 entity high-impact
├── 07-TC-role-cb_nv_tw.md              ← Role CB_NV_TW
├── 07-TC-role-cb_nv_bn.md              ← Role CB_NV_BN
├── 07-TC-role-cb_nv_dp.md              ← Role CB_NV_DP
├── 07-TC-role-cb_pd_tw.md              ← Role CB_PD_TW
├── 07-TC-role-cb_pd_bn.md              ← Role CB_PD_BN
├── 07-TC-role-cb_pd_dp.md              ← Role CB_PD_DP
├── 07-TC-role-dn.md                    ← Role DN (API only)
├── 07-TC-role-nht.md                   ← Role NHT
├── 07-TC-role-tvv.md                   ← Role TVV
├── 07-TC-role-cg.md                    ← Role CG
└── 08-TC-isolation-cross-unit.md       ← DI-04 BN ngang cấp + DI-05 ĐP ngang cấp
```

**Tổng:** 1 overview + 6 BR-AUTH TC file + 11 role TC file + 1 isolation = **19 file**. (v1.1: bổ sung 5 entity v3.5 NEW + 4 MPH action + C1 audit log + C2 upload security + QTHT bypass + API double-wrap regression — inline trong `04-TC-don-vi-id-scope.md` + `07-TC-role-*.md` để tránh thêm file mới.)

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Tổng | Priority dominant |
|------|------:|---------:|-----:|-----:|-------------------|
| 01-TC-auth-tier1.md | 2 (login OK + OTP OK) | 3 (sai pass / sai OTP / no OTP) | 2 (lock 5 sai + idle 30min) | **7** | P0 |
| 02-TC-scope-cap.md | 1 (TW xem all) | 3 (BN xem ĐP=0, ĐP xem BN=0, BN-A xem BN-B=0) | 1 (v3.5 BN không có ĐP trực thuộc) | **5** | P0 |
| 03-TC-approve-same-level.md | 1 (CB_PD_TW duyệt TW) | 2 (CB_PD_TW deny BN, CB_PD_BN deny ĐP) | 1 (TW state CHO_PHE_DUYET) | **4** | P0 |
| 04-TC-don-vi-id-scope.md (v1.1 +5 entity v3.5 + MPH action + C1 audit + C2 upload + QTHT bypass) | 4 (QTHT bypass + 5 entity v3.5 TC4.6-4.10 happy read) | 6 (AUDIT_LOG no scope + cross-unit isolation + MPH_CREATE 403 cross-cấp ×3 + DELETE→audit log INSERT verify) | 5 (v3.5 CB_TW exception + Hard-delete C1 + C2 ClamAV `.exe` upload + QTHT probe API DELETE TU_VAN_VIEN + API double-wrap dropdown DON_VI) | **15** | P0 |
| 05-TC-double-filter-actor.md (v1.1 +Lớp 1 only) | 3 (NHT/TVV/CG thấy VV phân công) | 2 (NHT cross-unit + TVV không phân công=empty) | 3 (DN API filter + DN không thấy DN khác + TC5.6 NHT/TVV xem tài liệu ĐT chung Lớp 1 only) | **8** | P0 |
| 06-TC-lgsp-mtls-public.md | 1 (LGSP mTLS valid) | 2 (no mTLS + expired token) | 2 (Guest read public + deny cong_khai=0) | **5** | P0 |
| 07-TC-role-{role}.md (11 file × ~5 TC entity high-risk v1.1) | 11 (menu visible) | 22 (button hide + action POST 403) | 22 (deep link 403 + entity NEW v3.5 sample) | **55** | P0+P1 |
| 08-TC-isolation-cross-unit.md | — | 4 (BN×BN DI-04 + ĐP×ĐP DI-05 cho HOI_DAP/VU_VIEC) | 1 (QTHT sees both) | **5** | P0 |
| **TỔNG** | **23** | **44** | **37** | **104** | — |

**Phân bổ priority (v1.1 — chuyển menu visibility P0→P1 per Gap #8 review):**

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc — block release nếu fail) | ~55 | 53% |
| P1 (quan trọng — fix sớm; bao gồm menu visibility per role) | ~38 | 37% |
| P2 (nên có — defer OK) | ~11 | 10% |

> **Lưu ý:** ≥30 TC requirement đạt — actual ≥104 TC (v1.1 tăng từ 71 do +5 entity v3.5 + 4 MPH action + audit log + ClamAV + QTHT bypass + API double-wrap). Có thể trim ưu tiên thấp P2 nếu thời gian eo hẹp.

---

## 5. Tiêu chí đạt/không đạt

> Reference: [`output/test-strategy.md §10`](../../../output/test-strategy.md), [`output/permission-matrix.md`](../../../output/permission-matrix.md)

- ✅ **PASS** (v1.1 — tách 5 metric riêng per Suggestion #7 review):
  - 100% P0 pass (gồm tất cả TC BR-AUTH-01..11 + isolation cross-unit DI-04/DI-05 + 5 entity v3.5 NEW TC4.6-4.10 + 4 MPH action TC4.11-4.14).
  - ≥90% P1 pass.
  - **Metric 1 — Menu visibility match per role: 100%** — mỗi role thấy đúng menu/sidebar item theo `permission-matrix-by-role.md`; KHÔNG có menu ngoài quyền.
  - **Metric 2 — Button visibility match per role: 100%** — button [Thêm mới] / [Sửa] / [Xóa] / [Phê duyệt] / [Công khai] hide đúng khi role không có quyền tương ứng.
  - **Metric 3 — Record scope match per query: 100%** — list/detail API trả record đúng scope (`don_vi_id` theo role+cấp; v3.5 exception CB_NV_TW VU_VIEC.cong_khai cross-don_vi).
  - **Metric 4 — 0 leak cross-unit:** mọi cross-unit query trả `[]` hoặc 403 (KHÔNG được trả 200 + data của đơn vị khác).
  - **Metric 5 — 0 deep-link bypass:** truy cập deep link URL trực tiếp khi không có quyền → 403/redirect login (KHÔNG render thành công).
- ❌ **FAIL:** bất kỳ điều kiện nào:
  - 1 P0 TC fail (vd BN-A query HOI_DAP của BN-B → trả 1 row).
  - P1 pass rate < 90%.
  - Có leak cross-unit (false positive ô permission trên matrix).
  - QTHT bypass permission gate sai (vd QTHT delete TU_VAN_VIEN bypass ô `👁️ R` matrix — memory `qa_htpldn_qtht_permission_bypass`).

**Pattern phải log Critical (BLOCK release):**
- Role thấy data role khác (data leak cross-unit / cross-role).
- Role có button Create/Edit/Delete mà matrix nói `👁️ R` only.
- Deep link không 403 cho role không có quyền (vd CB_NV_DP truy cập `/quan-tri/danh-muc` → render thành công thay vì 403).
- LGSP endpoint không yêu cầu mTLS (BR-AUTH-09 fail).

---

## 6. Tham chiếu

### SRS local
- [`input/srs-v3/srs-v3.md` Phụ lục B §B.1 BR-AUTH (lines 3945-3966)](../../../input/srs-v3/srs-v3.md) — BR-AUTH-01..11 source of truth
- [`input/srs-v3/srs-v3.md §3.2.0.4 Quy tắc phân quyền dữ liệu (lines 661-695)`](../../../input/srs-v3/srs-v3.md) — Tổng hợp BR-DATA-02 + BR-AUTH-08/10/11
- [`input/srs-v3/srs-v3.md §State machine (lines 4143-4578)`](../../../input/srs-v3/srs-v3.md) — Transitions có BR-AUTH-05 gate
- [`input/srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md`](../../../input/srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md) — 3 cross-cutting update v3.5 (C1 Hard-delete + C2 ClamAV remove + C3 Lưu nháp HẸP)
- [`input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md`](../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) — Full v3 → v3.5 diff

### QA reference
- [`output/permission-matrix.md`](../../../output/permission-matrix.md) — Master matrix 49 entity × 11 role (v3.5 updated 2026-05-09)
- [`output/test-strategy.md §5 Ma trận phân quyền`](../../../output/test-strategy.md) — Chiến lược permission test toàn dự án
- [`output/scaling-test-strategy.md §4.1 Bước 3`](../../../output/scaling-test-strategy.md) — Quy trình 7 bước onboard module
- [`output/template/permission-matrix-test-report-template.md`](../../../output/template/permission-matrix-test-report-template.md) — Template execution report (1 file/section matrix)
- [`output/template/test-case-template.md`](../../../output/template/test-case-template.md) — Template TC field-level
- [`output/template/bug-report-template.md`](../../../output/template/bug-report-template.md) — Template bug report 6 sections strict

### Account & data
- [`input/users.csv`](../../../input/users.csv) — Single source 154 row × 11 role × 4 replica
- [`input/test-accounts-isolation.csv`](../../../input/test-accounts-isolation.csv) — Usage guide DI-04/DI-05 + session pin
- [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) — 6 variants/entity per tier
- [`input/data/entity-map.md`](../../../input/data/entity-map.md) — 18 entity × tạo tại / đọc tại
- [`input/flow-module.md`](../../../input/flow-module.md) — State machine 14 module + Hub Tier + Seed Presets

### Test method (multi-role)
- Memory `qa_htpldn_round5_t01` — MCP `new_page({isolatedContext: "<role>_<unit>"})` per role; **KHÔNG** logout-login-lại (BE httpOnly cookie sticky cross-session).
- Memory `qa_htpldn_api_wrap_bug` — Dropdown/list empty dù network 200 có bytes → verify response shape qua `list_network_requests` (BE có thể wrap envelope 2 lần).
- Memory `qa_htpldn_qtht_permission_bypass` — BE pass DELETE/PATCH/POST cho QTHT thay vì 403; ưu tiên probe API trước UI khi test permission TC.
- CLAUDE.md §Chrome DevTools MCP — PATTERNS BẮT BUỘC (MCP-Rule 1..8) — primary tool 2026-04-21+.

---

*Test plan generated 2026-05-12 — cross-cutting permission module M (cross-cutting). Source mode: LOCAL. BR row count: 13 (BR-AUTH-01..11 + v3.5 CR-01 + v3.5 C1 Hard-delete). TC count target: ≥30. Permission matrix sample: 11 role × 14 entity. Account method: MCP isolated context per role.*

*Revised 2026-05-12 13:30:00 — apply review.md REVISE (≥80% gap + suggestion). Fixed: Gap #3 (+5 entity v3.5 NEW TC4.6-4.10), Gap #4 (Lớp 1 only TC5.6), Gap #5 (BR-AUTH-08 cite chuyển sang `_DELTA-MAP-FR05.md:58`), Gap #6 (audit INSERT verify TC4.4 extend), Gap #7 (C2 ClamAV upload `.exe`), Gap #8 (priority menu P0→P1), Gap #9 (account `[need: ...]` state marker), Gap #10 (QTHT bypass probe API TC4.x). Suggestion #1 (cột v3.5 status), #2 (split role TC theo entity high-risk), #3 (TC4.11-4.14 MPH_CREATE action), #4 (cite §3.2.0.4 661-695), #5 (isolated context naming `<role>_<don_vi_ma>_<idx>`), #6 (API double-wrap regression), #7 (5 metric PASS tách). TC count: 71 → 104. Skipped: Suggestion #8 dep marker per file §3 (defer cho từng TC file sau khi tạo, không inline trong overview).*
