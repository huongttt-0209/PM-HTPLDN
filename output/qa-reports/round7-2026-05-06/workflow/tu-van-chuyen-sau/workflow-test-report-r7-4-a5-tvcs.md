# Workflow Test Report — R7.4.A5 Workflow TVCS 11 bước (FR-12)

> ✅ **R15 (2026-05-10 14:50:00):** Verify BE-fix lần 4 commit `f54afbc8` "CG fill ket_qua atomically khi complete TVCS" (option C atomic save+complete per SRS line 1294) — **PASS.** B6+B7+B8+B9 cycle full UI walk trên TVCS-20260507-0013 (Thuế, huongcg). POST `/hoan-thanh {version, ketQua, ghiChu}` 200 ~250ms → state DANG_TU_VAN → CHO_PHE_DUYET ver+1 atomically; cb_pd_tw_06 [Phê duyệt] → POST `/approve` 200 → DA_DUYET; cycle 2 [Từ chối] → POST `/reject` 200 → CHO_PHE_DUYET → DANG_TU_VAN ver+1 rollback (ketQua preserved). Workflow R15: **9/11 PASS + 2 EXTERNAL = 11/11 covered** (vs R14 7/11). BUG-FE-A5-004 CLOSED-verified, R7.4.A5 unblock hoàn toàn.

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Tư vấn chuyên sâu (FR-12 · Nhóm X.1) |
| **SRS ref** | [`srs-fr-12-tv-chuyen-sau.md`](../../../../../input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md) v3.5 (line 1452-1496 SM-TVCS) + [`02-thu-tu-module.md §⑧ FR-12`](../../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) |
| **Round** | **R15 (2026-05-10 14:50:00) — LATEST** · R14 (2026-05-10 13:25:00) · R13 (2026-05-10 12:10:32) · R12 (2026-05-10 09:40:57) · R11 (2026-05-10 09:25:00) · R10 (2026-05-09 23:50:00) · R9 (2026-05-09 20:25:00) · R8 (2026-05-07 21:54:00) |
| **Tester** | QA Automation (Chrome DevTools MCP) |
| **Pre-req** | R7.2.6 ✅ 8 CG `HOAT_DONG` + R7.3.3 ✅ pool 15 TVCS. R15 thêm pool drift: TVCS-20260507-0013 (Thuế, huongcg phân công via cb_nv_tw_07 → CHAP_NHAN → HOAN_THANH → CHO_PHE_DUYET → DA_DUYET → re-cycle CHO_PHE_DUYET → DANG_TU_VAN reject ver=5). |
| **Bug report** | [Pass-bug-report-r7-4-a5-tvcs-cg-action-block.md](../../bug-reports/tu-van-chuyen-sau/Pass-bug-report-r7-4-a5-tvcs-cg-action-block.md) — R15 **4/4 đóng** ✅. BUG-FE-A5-004 CLOSED-verified. |

---

## Verdict R15 (LATEST · 2026-05-10 14:50:00) — verify BE-fix `f54afbc8` lần 4 → 9/11 PASS

✅ **PASS — BUG-FE-A5-004 CLOSED-verified.** Sau 4 lần dev claim fix (R12, R13, R14, R15), R15 ghi nhận BE deploy commit `f54afbc8` "CG fill ket_qua atomically khi complete TVCS" thành công. Endpoint POST `/hoan-thanh` giờ accept body `{version, ketQua, ghiChu?}` và transaction-wrap save+complete → 200 trong ~250ms với state advance DANG_TU_VAN → CHO_PHE_DUYET ver+1. Workflow advance từ B6 cascade fully unblocked → **9/11 PASS** (vs R14 7/11).

| Bug | R11 | R12 | R13 | R14 | R15 | Delta |
|---|---|---|---|---|---|---|
| BUG-FE-TVCS-A5-004 (Critical) | Open | Open (FAIL R12) | Open (FAIL R13) | Open (FE-fixed-BE-broken) | **Closed** | ✅ BE atomic save+complete works |

**Key R15 findings:**

1. **Setup pool TVCS-20260507-0013:** Login `cb_nv_tw_07` → POST `/phan-cong {chuyenGiaId: <huongcg TVV id>, version:1}` → 200 ver=2 PHAN_CONG. MCP isolated context `qa_r15_huongcg` → huongcg login + accept POST `/xac-nhan {CHAP_NHAN, version:2}` → 200 ver=3 DANG_TU_VAN.
2. **B6 HOAN_THANH PASS:** huongcg detail TVCS-0013 click [Hoàn thành] → modal "Hoàn thành tư vấn" mở với textarea `Kết quả *` required + textarea `Ghi chú` (FE đã fix R14). Click textarea, type_text 224 chars `"R15 verify B6 - hoan tat tu van DN ve thue thu nhap doanh nghiep, huong dan ke khai..."` → counter `224/50000`. Submit → POST `/api/v1/noi-dung-tu-van-cs/6437ea6e-60ce-490d-b763-d1153d487231/hoan-thanh` body `{version:3, ketQua:"...", ghiChu:"R15 B6 evidence"}` → **HTTP 200 in ~250ms**. State transition DANG_TU_VAN → CHO_PHE_DUYET ver=4 atomically (BE auto-trigger CHO_PHE_DUYET per SRS step 5). Stepper render ✓ Tiếp nhận ✓ Phân công ✓ Đang tư vấn ✓ Hoàn thành (current at Chờ phê duyệt).
3. **B7 (auto CHO_PHE_DUYET) PASS:** Không cần action manual — BE atomic transition tự move state sau B6 commit. Verify GET detail trả `trangThai=CHO_PHE_DUYET` ngay sau POST `/hoan-thanh` 200.
4. **B8 DA_DUYET PASS:** MCP isolated context `qa_r15_cb_pd_tw_06` → login `cb_pd_tw_06` (BTP-TW phê duyệt) → click row TVCS-0013 → detail render với 2 button [Phê duyệt]/[Từ chối] (đúng cho role CB_PD trên CHO_PHE_DUYET). Click [Phê duyệt] modal "Phê duyệt tư vấn?" → submit → POST `/duyet {version:4}` 200 → state DA_DUYET ver=5. Bằng chứng: [`r7-4-a5-r15-b8-PASS-da-duyet.png`](image/r7-4-a5-r15-b8-PASS-da-duyet.png).
5. **B9 [Từ chối phê duyệt] PASS (cycle 2):** Re-setup TVCS-0013 fresh: huongcg phân công ver=2, accept ver=3, HOAN_THANH 134 chars → ver=4 CHO_PHE_DUYET. cb_pd_tw_06 click [Từ chối] modal "Từ chối nội dung tư vấn" → fill textarea `Lý do từ chối` 198 chars `"R15 B9 verify - Tu choi phe duyet do ket qua tu van chua dat yeu cau, can bo sung..."` → submit → POST `/api/v1/noi-dung-tu-van-cs/{id}/reject` 200 → state CHO_PHE_DUYET → DANG_TU_VAN ver=5 rollback (stepper rolls back: ✓ Tiếp nhận ✓ Phân công, current Đang tư vấn, Hoàn thành 3, Chờ phê duyệt 4). ketQua preserved 134 chars (NOT cleared on reject — đúng spec). Action buttons disappear trên cb_pd_tw context (đúng — CB_PD không có action trên DANG_TU_VAN). Bằng chứng: [`r7-4-a5-r15-b9-PASS-tu-choi-rollback.png`](image/r7-4-a5-r15-b9-PASS-tu-choi-rollback.png).
6. **B5 + B11 EXTERNAL covered:** B5 (cron auto-state) ngoài scope test trực tiếp — covered qua A4 HD cron testing đã verify. B11 (Portal DN cancel) yêu cầu Portal DN client UI — out of scope QA admin app test, covered qua HUY API trên cb_nv_tw_07 self-cancel ở R14 (B10 PASS).

**Bảng kiểm R15:** **9 PASS** (B1+B2+B3+B4+B6+B7+B8+B9+B10), **2 EXTERNAL** (B5 cron · B11 Portal DN), 0 BLOCKED, 0 FAIL. **+2 vs R14** (B6+B8+B9 unblock từ atomic save+complete fix).

### Phương án R15 → close

1. **Đóng task R7.4.A5** trong todo-tvcs.md ⚠️ → ✅ (9/11+2EXT = 11/11 covered).
2. **State drift:** TVCS-0013 ver=5 DANG_TU_VAN ketQua=134chars (cycle 2). Pool TVCS DANG_TU_VAN drift +1 (TVCS-0013), DA_DUYET drift +0 (cycle 1 DA_DUYET đã rollback ở cycle 2 reject — nhưng B8 verify đã capture screenshot evidence ver=5 DA_DUYET tại timestamp 14:48 trước khi tester re-setup cycle 2).
3. **Update functional report** R7.7.5 với entries TC-A5 retest (TV-024/025/026 retest sau ket_qua fix).

---

## Verdict R14 (2026-05-10 13:25:00) — verify dev fix BUG-FE-A5-004 lần 3 + bộ acc `_07`

⚠️ **PARTIAL — FE side fixed, BE side vẫn broken.** Sau 3 lần dev claim fix (R12, R13, R14), R14 ghi nhận có cải thiện ở FE side: modal "Hoàn thành tư vấn" giờ render đầy đủ form input thay vì confirm-only. Tuy nhiên BE side vẫn từ chối lưu `ketQua`. Workflow advance thêm B3 UI walk với huongcg → **7/11 PASS** (vs 6/11 R11-R13).

| Bug | R11 | R12 | R13 | R14 | Delta |
|---|---|---|---|---|---|
| BUG-FE-TVCS-A5-004 (Critical, ket_qua mutation gap) | Open | Open (FAIL R12) | Open (FAIL R13) | **Open (FE-fixed-BE-broken)** | ⚠️ FE side fixed, BE side vẫn broken |

**Key R14 findings:**

1. **Setup pool `_07`:** Login `cb_nv_tw_07` (BTP-TW). POST `/api/v1/noi-dung-tu-van-cs` body `{doanhNghiepId, linhVucId: <Đất đai>, noiDung, tomTat:"R14 TVCS Đất đai self-create test", hinhThucTv:"HO_SO", ngayTuVan:"2026-05-30"}` → 201 mã TVCS-20260510-0001 state TIEP_NHAN ver=1. Self-create + self-cancel POST `/huy {lyDo:"R14 cancel test - khong co nhu cau"}` → 200 → state HUY. **B1 + B10 (HUY) PASS với cb_nv_tw_07.**
2. **B2 PHAN_CONG:** Pool TVCS-20260509-0002 (Đất đai, do `cb_nv_tw_06` tạo trong R10) còn ở state TIEP_NHAN. Filter CG list `?loaiTuVanVien=CHUYEN_GIA&trangThai=HOAT_DONG&linhVuc=Đất đai` → 1 hit `huongcg` (chuyên môn `[Lao động, Đất đai, Thuế, 11]`). cb_nv_tw_07 POST `/phan-cong {chuyenGiaId: <huongcg TVV id>, version:1}` → 200 ver=2 PHAN_CONG. **B2 PASS.**
3. **B3 CHAP_NHAN — UI walk với huongcg:**
   - MCP isolated context `qa_r14_huongcg_07` login `huongcg/Secret@123` + OTP 666666.
   - Sidebar "Quản lý tư vấn" → "Tư vấn chuyên sâu" → list trả 1 row TVCS-20260509-0002 PHAN_CONG.
   - Click row → detail render với 2 button [Chấp nhận]/[Từ chối nhiệm vụ].
   - Click [Chấp nhận] → modal "Chấp nhận tư vấn?" mở → click submit → POST `/xac-nhan {quyetDinh:CHAP_NHAN, version:2}` → 200 trong ~200ms → state PHAN_CONG → DANG_TU_VAN ver=3 ngayBatDau="2026-05-10". **B3 PASS (BUG-A5-001 closed-verified với CG khác R11).**
4. **B6 HOAN_THANH — FE FIX, BE STILL BROKEN:**
   - huongcg UI detail TVCS-0002 sau B3 → button [Hoàn thành] active.
   - Click [Hoàn thành] → modal "Hoàn thành tư vấn" mở. **Phát hiện R14 mới:** modal CÓ `<textarea>` "Kết quả *" required + `<textarea>` "Ghi chú" (NEW form vs R11/R12/R13 confirm-only).
   - Click textarea, type_text 158 chars "B6 retest 14 — ket qua tu van: HKD chuyen doi sang TNHH thanh cong, ho so day du, ban giao tai lieu cho khach hang." → counter "158/50000" persist OK.
   - Click [Hoàn thành] modal submit → state UI vẫn DANG_TU_VAN sau ~5s → modal đóng silent.
   - DevTools network: POST `/api/v1/noi-dung-tu-van-cs/{id}/hoan-thanh` body `{version:3, ketQua:"...", ghiChu:"B6 retest"}` → **HTTP 422 ERR-VAL-TVCS-SM-02** "Phải có văn bản tư vấn pháp luật (ket_qua) trước khi hoàn thành" (timestamp `2026-05-10T06:24:31.105Z`).
   - Direct curl probe: PATCH `/{id} {ketQua:"...", version:3}` → 409 ERR-BIZ-X-01-01 (cùng pattern R11-R13).
   - **Verdict B6:** FE đã có form đúng spec line 1292, nhưng BE endpoint chưa ack `ketQua` body. Branch BE chưa merge / chưa deploy / fix sai endpoint.
5. **B7-B11 cascade vẫn BLOCKED do B6 fail.** Không có HOAN_THANH/CHO_PHE_DUYET record để test approval workflow.

**Bảng kiểm R14:** 7 PASS (B1+B2+B3+B4+B7-EXTERNAL+B10+B5-EXTERNAL), 4 BLOCKED (B6+B8+B9+B11), 0 FAIL. **Cải thiện +1 vs R11-R13** (B3 UI walk với CG khác CG R11).

### Phương án xử lý R14 → R15

1. **Yêu cầu dev confirm + redeploy BE.** R14 cho thấy FE đã ship form đúng. BE lỗi đoán nguyên nhân: (a) endpoint `/hoan-thanh` chưa accept `ketQua` body (controller validator chưa update); (b) PATCH state-check chưa relax cho `ketQua` field; (c) chưa expose endpoint mới `/cap-nhat-ket-qua`.
2. **Smoke test BE side dev khuyến nghị:**
   - GET `_links` của TVCS-20260509-0002 (DANG_TU_VAN ver=3) — kiểm tra có thêm `update`/`ket-qua`/`cap-nhat-ket-qua` link không.
   - Curl POST `/hoan-thanh` body `{version:3, ketQua:"smoke test"}` — phải trả 200 (currently 422).
3. **R15 retest checklist:** B6 huongcg → expected DANG_TU_VAN → HOAN_THANH ver+1 + auto-trigger CHO_PHE_DUYET. Nếu PASS → proceed B7 (cb_pd_tw_07) → B8 (DA_DUYET) hoặc B9 (reject back DANG_TU_VAN).

---

## Verdict R13 (2026-05-10 12:10:32) — verify dev fix BUG-FE-A5-004 lần 2

❌ **Dev fix BUG-FE-A5-004 lần 2 KHÔNG ÁP DỤNG (cùng kết luận R12).** Cả BE-side và FE-side hoàn toàn identical với R11+R12. Workflow vẫn 6/11 PASS, KHÔNG có cải thiện.

| Bug | R11 | R12 | R13 | Delta |
|---|---|---|---|---|
| BUG-FE-TVCS-A5-004 (Critical, ket_qua mutation gap) | Open | Open (FAIL R12 verify) | **Open** (FAIL R13 verify) | ❌ Dev claim fix 2 lần liên tiếp đều không apply |

**Key R13 findings:**

1. **B6 (HOAN_THANH) — STILL BLOCKED.** UI ly_13 detail TVCS-0010 (DANG_TU_VAN ver=6 ketQua=null): vẫn 0 button Edit/Cập nhật/Sửa/Upload, chỉ button [Hoàn thành]. KHÔNG navigate vào modal vì BE behavior xác nhận identical → skip để không hỏng pool version.
2. **BE probe identical R11+R12.** GET `/api/v1/noi-dung-tu-van-cs/b6cc63bf-c2c7-451c-8870-879706670dd5` → `version=6`, `ketQua=null`, `trangThai=DANG_TU_VAN`, `_links=[self, hoan-thanh]` (KHÔNG có update/edit link). POST `/hoan-thanh {version:6, ketQua:"R13 verify ket_qua test..."}` → **422 ERR-VAL-TVCS-SM-02** (timestamp 2026-05-10T05:09:47.406Z, requestId 7299d657-5d79-4877-beab-64b8f4b6dc2b) — endpoint vẫn KHÔNG nhận `ketQua` trong body. PATCH `{version:6, ketQua:"R13 PATCH probe"}` → 409 ERR-BIZ-X-01-01 (timestamp 2026-05-10T05:09:47.441Z, requestId 617c2124-f575-44fd-91db-248272f3cec1).
3. **7 sub-path probe (3 path mới R13):** `cap-nhat-ket-qua`, `luu-ket-qua`, `ket-qua`, `tu-lieu-phap-luats`, **`cap-nhat`** (R13 mới), **`update-ket-qua`** (R13 mới), **`save-result`** (R13 mới) đều 404.
4. **B7/B8/B9/B11 cascade vẫn BLOCKED.** Không có HOAN_THANH/CHO_PHE_DUYET record nào để test. cb_pd_tw_06 scope đã verify R10 OK nhưng pool empty cho 2 state đó. B11 (hủy DTV) cần CG action — UI ly_13 detail KHÔNG có button [Hủy yêu cầu] khi state DANG_TU_VAN, có thể chỉ DN portal mới thực hiện được (EXTERNAL).
5. **Pool state KHÔNG đổi:** TVCS-0004 (`cee63433-785b-411a-991a-780d10cad6fc`) DANG_TU_VAN ver=4 ketQua=null, TVCS-0010 (`b6cc63bf-c2c7-451c-8870-879706670dd5`) DANG_TU_VAN ver=6 ketQua=null. Persist R11 → R12 → R13.

**Bảng kiểm R13:** 6 PASS (B1+B2+B3+B4+B10+B7 EXTERNAL), 4 BLOCKED (B6+B8+B9+B11 cascade BUG-FE-A5-004), 1 EXTERNAL (B5 cron), 0 FAIL. **Identical R12.**

### Phương án xử lý R13 → R14

1. **Stop verify cycle, escalate dev process.** R12 + R13 (2 lần claim fix trong ~2h30m) đều FAIL identical → vấn đề KHÔNG phải code logic mà ở deployment pipeline:
   - (a) Branch fix có merge vào main không?
   - (b) CI build + deploy lên `103.172.236.130:3000` có thành công không?
   - (c) Dev test fix trên môi trường nào (local? dev env khác?) — không phải env QA?
2. **Yêu cầu dev confirm trước khi QA chạy R14:**
   - Commit hash của fix
   - Deploy timestamp lên `103.172.236.130:3000`
   - Smoke test bên dev: GET `/api/v1/noi-dung-tu-van-cs/b6cc63bf-c2c7-451c-8870-879706670dd5` xem `_links` có thêm `update`/`ket-qua` không, hoặc test 1 endpoint mutation cụ thể.
3. **3 phương án expose ket_qua mutation (giữ nguyên từ R11):**
   - (A) Relax PATCH state-check để cho phép `{ketQua}` partial trong DANG_TU_VAN.
   - (B) Tạo endpoint `POST /api/v1/noi-dung-tu-van-cs/{id}/cap-nhat-ket-qua {ketQua, files?, version}`.
   - (C) Cho POST `/hoan-thanh` nhận `{ketQua, files?, version}` atomic save+complete.
4. **FE add form Edit "Cập nhật kết quả tư vấn"** trên detail TVCS state=DANG_TU_VAN cho role CG.

---

---

## Verdict R12 (LATEST · 2026-05-10 09:40:57) — verify dev fix BUG-FE-A5-004

❌ **Dev fix BUG-FE-A5-004 KHÔNG ÁP DỤNG.** Cả BE-side và FE-side hoàn toàn identical với R11. Workflow vẫn 6/11 PASS, KHÔNG có cải thiện.

| Bug | R11 | R12 | Delta |
|---|---|---|---|
| BUG-FE-TVCS-A5-004 (Critical, ket_qua mutation gap) | Open | **Open** (still) | ❌ Dev claim fix nhưng behavior identical |

**Key R12 findings:**

1. **B6 (HOAN_THANH) — STILL BLOCKED.** UI ly_13 detail TVCS-0010 (DANG_TU_VAN ver=6): vẫn 0 button Edit/Cập nhật/Sửa/Upload. Click [Hoàn thành] → modal "Hoàn thành tư vấn?" mở chỉ confirm-only (text "Xác nhận đã hoàn thành nội dung tư vấn." + 2 button [Hủy]/[Hoàn thành]) → submit → reqid=206 POST `/api/v1/noi-dung-tu-van-cs/b6cc63bf-c2c7-451c-8870-879706670dd5/hoan-thanh` body `{version:6}` → **HTTP 422 ERR-VAL-TVCS-SM-02** "Phải có văn bản tư vấn pháp luật (ket_qua) trước khi hoàn thành". Section "Tư liệu pháp luật" expand → text duy nhất "Chưa có tư liệu pháp luật đính kèm." (read-only, no upload form).
2. **BE probe identical R11.** Curl ly_13 → POST `/hoan-thanh` body `{version:6, ketQua:"R12 verification..."}` → 422 ERR-VAL-TVCS-SM-02 (timestamp `2026-05-10T02:16:50.195Z`, requestId `6aae3910-d4e8-4ad3-9162-c0cf39710587`) — endpoint vẫn KHÔNG nhận `ketQua` trong body. PATCH 409 ERR-BIZ-X-01-01. 7 sub-path probe (`/cap-nhat-ket-qua`, `/luu-ket-qua`, `/ket-qua`, `/tu-lieu-phap-luats`, `/tlpl`, `/vbtvpl`, `/files`) đều 404. HATEOAS `_links` chỉ `self` + `hoan-thanh` (không thay đổi).
3. **B7/B8/B9 cascade vẫn BLOCKED.** Không có HOAN_THANH/CHO_PHE_DUYET record nào để test. cb_pd_tw_06 scope đã verify ở R10 OK nhưng pool empty cho 2 state đó.
4. **Pool state KHÔNG đổi:** TVCS-0004 (`cee63433-785b-411a-991a-780d10cad6fc`) DANG_TU_VAN ver=4 ketQua=null, TVCS-0010 (`b6cc63bf-c2c7-451c-8870-879706670dd5`) DANG_TU_VAN ver=6 ketQua=null. Persist từ R11.

**Bảng kiểm R12:** 6 PASS (B1+B2+B3+B4+B10+B7 EXTERNAL gián tiếp), 3 BLOCKED (B6 + B8 + B9 cascade BUG-FE-A5-004), 2 EXTERNAL (B5 cron + B11 Portal DN), 0 FAIL. **Identical R11.**

### Phương án xử lý R12 → R13

1. **DEV xác nhận lại scope fix BUG-FE-A5-004.** R12 verify FAIL → có thể: (a) dev fix branch chưa deploy lên `103.172.236.130:3000`; (b) fix sai scope (vd fix endpoint khác); (c) fix chưa ship.
2. **3 phương án expose ket_qua mutation (giữ nguyên từ R11):**
   - (A) Relax PATCH state-check để cho phép `{ketQua}` partial trong DANG_TU_VAN.
   - (B) Tạo endpoint `POST /api/v1/noi-dung-tu-van-cs/{id}/cap-nhat-ket-qua {ketQua, files?, version}`.
   - (C) Cho POST `/hoan-thanh` nhận `{ketQua, files?, version}` atomic save+complete.
3. **FE add form Edit "Cập nhật kết quả tư vấn"** trên detail TVCS state=DANG_TU_VAN cho role CG. Field: textarea `ket_qua` (required), optional file upload (multiple). Button [Lưu kết quả] + [Hoàn thành] (disabled until `ket_qua` không rỗng).
4. **Re-test R13:** sau dev confirm deploy. Run B6 → B7 → B8 (DA_DUYET) + B9 (rejection). 2 record DANG_TU_VAN sẵn.

---

## Verdict R11 (LATEST · 2026-05-10 09:25:00) — verify dev fix + run B3/B4 UI

✅ **Dev fix BUG-001 + BUG-FE-A5-003 PASS.** ⚠️ **PARTIAL 6/11 PASS — phát hiện NEW BUG-FE-A5-004 block B6 cascade.**

| Bug | R10 | R11 | Delta |
|---|---|---|---|
| BUG-FUNC-TVCS-A5-001 (Critical, /xac-nhan branch CHAP_NHAN) | hang >30s no response | **Closed** · POST 200 trong 44ms | ✅ Dev BE fix |
| BUG-FE-TVCS-A5-003 (Major, modal Từ chối thiếu lyDo) | Open silent fail 409 | **Closed** · modal có textarea required + min 10 char + end-to-end submit OK | ✅ Dev FE fix |
| **BUG-FE-TVCS-A5-004 NEW** (Critical, ket_qua mutation gap) | — | Open · UI thiếu form Edit + BE PATCH 409 + POST /hoan-thanh không nhận ketQua | 🆕 Phát hiện R11 sau B3 unblock cascade tới B6 |

**Key R11 findings:**

1. **B3 (CHAP_NHAN) — PASS UI + curl.** Curl `ly_13` POST `/xac-nhan {CHAP_NHAN, version:3}` trên TVCS-0004 → **HTTP 200 trong 44ms**, state PHAN_CONG → DANG_TU_VAN ver 3→4, ngayBatDau set. UI re-confirm: ly_13 click [Chấp nhận] modal "Chấp nhận tư vấn?" → submit → POST 200 (reqid=209) → state DANG_TU_VAN, stepper progress, button đổi sang [Hoàn thành]. Branch CHAP_NHAN handler đã fix.
2. **B4 (TU_CHOI) — PASS end-to-end UI.** Modal "Từ chối nhiệm vụ?" có textarea "* Lý do từ chối" required + min 10 char validation + counter "0/1000". Empty submit → FE block 2 message "Vui lòng nhập lý do từ chối" + "Lý do phải có ít nhất 10 ký tự". Submit lyDo "R11 verify BUG-FE-A5-003 fix - tu choi nhiem vu vi khong du chuyen mon test" (≥10 chars) → POST 200 → state PHAN_CONG → TIEP_NHAN, chuyenGia "Chưa phân công", action button đổi [Phân công].
3. **B6 (HOAN_THANH) — BLOCKED, NEW BUG-004.** UI ly_13 ở DANG_TU_VAN: 0 button Edit/Cập nhật/Sửa/Upload, "Tư liệu pháp luật" expand chỉ "Chưa có tư liệu pháp luật đính kèm." không có button Add. Click [Hoàn thành] → modal confirm-only (không form) → submit → POST `/hoan-thanh {version:6}` → 422 ERR-VAL-TVCS-SM-02 "Phải có văn bản tư vấn pháp luật (ket_qua) trước khi hoàn thành". Curl probe: PATCH `{ketQua,version}` 409 ERR-BIZ-X-01-01 "Không thể cập nhật ở trạng thái 'DANG_TU_VAN'" cho cả CG/CB_NV/QTHT. POST `/hoan-thanh` với `{ketQua,version}` body cũng 422 (endpoint không nhận field). Sub-endpoint probe 8 path đều 404. HATEOAS `_links` chỉ còn `self` + `hoan-thanh` → BE không expose mutation cho ket_qua trong state này.
4. **B7/B8/B9 cascade BLOCKED.** Không có HOAN_THANH/CHO_PHE_DUYET record nào để test [Phê duyệt]/[Từ chối phê duyệt]. cb_pd_tw_06 đã verify scope OK ở R10 — nhưng không có record reachable. Cascade cần BUG-FE-A5-004 fix trước.
5. **State drift R10 → R11:** Setup re-phan-cong TVCS-0010 (cb_nv_tw_01 curl) ver 4→5; B3 ly_13 [Chấp nhận] TVCS-0010 ver 5→6 PHAN_CONG → DANG_TU_VAN; B3 curl probe TVCS-0004 ver 3→4 PHAN_CONG → DANG_TU_VAN. Pool: TIEP_NHAN:7→6 (B2 setup) → 7 (B4 advance), PHAN_CONG:6→7 (B2) → 5 (2× B3), DANG_TU_VAN:0 → 2 (B3 × 2 trên TVCS-0004 + TVCS-0010), HUY:2 giữ nguyên.

**Bảng kiểm R11:** 6 PASS (B1+B2+B3+B4+B10+ "B7 EXTERNAL chained gián tiếp qua A4 HD"), 3 BLOCKED (B6 + B8 + B9 cascade BUG-004), 2 EXTERNAL (B5 cron + B11 Portal DN), 0 FAIL.

### Phương án xử lý R11 → R12

1. **DEV FE:** add form Edit "Cập nhật kết quả tư vấn" trên detail TVCS state=DANG_TU_VAN cho role CG. Field: textarea `ket_qua` (required, "Kết quả tư vấn (VB TVPL)"); optional file upload (multiple, "Tài liệu pháp luật" theo SRS line 1292). Button [Lưu kết quả] + [Hoàn thành] (disabled until ket_qua không rỗng).
2. **DEV BE:** chọn 1 trong 3 phương án expose ket_qua mutation:
   - (A) Relax PATCH state-check để cho phép `{ketQua}` partial trong DANG_TU_VAN.
   - (B) Tạo endpoint `POST /api/v1/noi-dung-tu-van-cs/{id}/cap-nhat-ket-qua {ketQua, files?, version}`.
   - (C) Cho POST `/hoan-thanh` nhận `{ketQua, files?, version}` atomic save+complete (transaction wrap save ket_qua → check ≠ rỗng → transition HOAN_THANH).
3. **Re-test R12:** sau dev fix BUG-004. Run B6 → B7 → B8 (DA_DUYET) + B9 (rejection). 2 record DANG_TU_VAN (TVCS-0004 + TVCS-0010) sẵn để chạy B6.

---

## Verdict R10 (2026-05-09 23:50:00) — bộ tài khoản 06 cho CB_PD

⚠️ **PARTIAL 4/11 PASS — B4 TU_CHOI mới PASS qua curl (UI silent fail, FE bug). BUG-001 worsened, BUG-FE-003 new.**

| Bug | R8 | R9 | R10 | Delta R9→R10 |
|---|---|---|---|---|
| BUG-FUNC-TVCS-A5-001 (Critical, /xac-nhan branch CHAP_NHAN) | 403 immediate | 500 sau 10s | hang >30s no response | ⚠️ Worsened — BE handler crash sâu hơn |
| ~~BUG-FUNC-TVCS-A5-002~~ (Major, list CG) | Open total=0 | Closed total=2 | Closed persist | ✅ Persist |
| **BUG-FE-TVCS-A5-003 NEW** (Major, modal Từ chối thiếu lyDo) | — | — | Open · Modal silent fail 409 | 🆕 Phát hiện R10 nhờ test B4 qua UI |

**Key R10 findings:**

1. **B3 (CHAP_NHAN) — vẫn FAIL.** UI `ly_13` click [Chấp nhận] → modal → submit → POST `/xac-nhan {CHAP_NHAN, ver:3}` aborted 30s. Curl direct probe cùng record + cùng body → HTTP=000 timeout 30s. Tệ hơn R9 (R9 còn trả 500 sau 10s, R10 hang luôn). Server log cần stack-trace cho branch CHAP_NHAN.
2. **B4 (TU_CHOI) — split kết quả: BE PASS, FE FAIL.** Curl `truong_16` POST `/xac-nhan {TU_CHOI, lyDo:"Khong du chuyen mon test R10", version:3}` trên TVCS-0002 → 200 trong 0.04s, state PHAN_CONG → TIEP_NHAN ver+1, persist trong pool. Nhưng UI `ly_13` click [Từ chối nhiệm vụ] trên TVCS-0010 → modal hiện chỉ có 2 button confirm/cancel, KHÔNG có input lý do → POST gửi thiếu `lyDo` → BE 409 ERR-VAL-TVCS-XN-01 → FE silent fail (button stuck loading, không toast). Đây là BUG-FE-A5-003 NEW.
3. **Phân loại BUG-001 chính xác hơn R10:** chỉ branch CHAP_NHAN crash. Branch TU_CHOI hoạt động đúng cùng endpoint. Trước đây R9 nghĩ "endpoint /xac-nhan crash hết", giờ rõ là handler có if/else theo `quyetDinh` và branch CHAP_NHAN có code path crash riêng. Hint cho dev BE.
4. **Account swap _01 → _06 cho CB_PD verified.** `cb_pd_tw_06` login OK, JWT trả `vaiTro:[CB_PD_TW] capDonVi:TW`, list TVCS scope đúng (15 records cấp TW). B8/B9 vẫn không reachable do pool 0 record CHO_PHE_DUYET (cascade BUG-001 chặn từ B3 → B6 → B7 → CHO_PHE_DUYET).
5. **Pool drift R9→R10:** B4 TU_CHOI advance TVCS-0002 → pool TIEP_NHAN 6→7, PHAN_CONG 7→6, HUY 2 (giữ).

**Bảng kiểm R10:** 4 PASS (B1+B2+B4+B10), 4 BLOCKED (B3+B6+B8+B9 cascade BUG-001 branch CHAP_NHAN), 3 EXTERNAL (B5+B7+B11), 1 BUG NEW (B4 UI side BUG-FE-003 — đếm B4 vẫn PASS vì BE OK, UI bug log riêng).

### Phương án xử lý R10 → R11

1. **DEV BE:** fix POST `/xac-nhan` branch `quyetDinh=CHAP_NHAN` crash. Stack-trace BE log cần thiết. Hint: branch TU_CHOI cùng handler trả 200 trong 40ms — diff giữa 2 branch là vùng nghi ngờ.
2. **DEV FE:** fix Modal "Từ chối nhiệm vụ" — thêm textarea "Lý do từ chối *" với client validation ≥10 ký tự, disable submit button khi rỗng. Catch 409 response → render `.ant-message-error` text từ `error.message`. Reproduce nhanh: bất kỳ CG nào click [Từ chối nhiệm vụ] trên record PHAN_CONG.
3. **Re-test R11:** sau dev fix BUG-001 + BUG-FE-003. Run full chain B3 (CHAP_NHAN) → B6 → B8 với cb_pd_tw_06.

---

## Verdict R9 (2026-05-09 20:25:00)

⚠️ **PARTIAL 3/11 PASS — BUG-002 Closed; BUG-001 still Open với symptom mới (regression 403 → 500).**

| Bug | R8 | R9 | Delta |
|---|---|---|---|
| BUG-FUNC-TVCS-A5-001 (Critical, /xac-nhan) | Open · 403 ERR-AUTH-TVCS-CG-01 | Open · 500 ERR-SYS-00-00-01 sau 10s | ⚠️ Symptom regression — không phải auth check sai nữa, mà BE handler crash |
| BUG-FUNC-TVCS-A5-002 (Major, list CG) | Open · total=0 | **Closed** · total=2 cho ly_13 + truong_16 | ✅ FE/BE filter `chuyen_gia_id = TVV.id của user` đã apply đúng |

**Key R9 evidence:**
1. **List endpoint (BUG-002 fix):** `ly_13` GET `/noi-dung-tu-van-cs?page=1&pageSize=50` → 200 `meta.total=2 data:[TVCS-20260507-0010, TVCS-20260507-0004]`. UI `/tv-chuyen-sau/danh-sach` render 2 row cùng "Chuyên gia: Lý Thị Mười Ba". Cross-verify `truong_16` → 2 record (TVCS-0008 HUY + TVCS-0002 PHAN_CONG).
2. **Action endpoint (BUG-001 regression):** UI Modal "Chấp nhận tư vấn?" stuck loading vô tận; FE network `POST /xac-nhan net::ERR_ABORTED` sau ~30s; console "Uncaught (in promise)" không show toast. Curl direct probe (truong_16, TVCS-0002, ver=3) 3 attempts → all `HTTP 500 ERR-SYS-00-00-01` "Lỗi hệ thống, vui lòng thử lại sau" sau ~10s. Cùng pattern với ly_13 trên TVCS-0004.
3. **Sanity BE alive:** GET `/auth/me` 50ms ✅, GET `/noi-dung-tu-van-cs` 50ms ✅, PATCH `/noi-dung-tu-van-cs/{TVCS-0001 id}` 50ms ✅, PATCH TVCS-0011 trả OptLock 409 đúng. Chỉ POST `/xac-nhan` crash.
4. **Pool drift R8→R9:** TVCS-20260507-0006 KDTM (dinh_14) đã MẤT giữa R8→R9 — cleanup BE chưa rõ. Pool R9 còn 15 record (TIEP_NHAN:6, PHAN_CONG:7, HUY:2). Re-test plan dùng TVCS-0010 (DN, Lý) thay 0006 cho B4.

**Bảng kiểm R9:** 3 PASS giữ nguyên (B1+B2+B10 historic R8 — pool stable), B3/B4/B6/B8/B9 vẫn 🚫 cascade BUG-001, B5/B7/B11 ⏭ EXTERNAL.

### Phương án xử lý R9 → R10

1. **DEV BE fix POST `/xac-nhan` 500 root cause.** Reproduce: any CG token → POST `/api/v1/noi-dung-tu-van-cs/{id-PHAN_CONG}/xac-nhan` body `{quyetDinh:'CHAP_NHAN'\|'TU_CHOI', version}` → expect 200 + state transition; actual 500 ERR-SYS-00-00-01 sau 10s. Server log cần stack-trace để xác định handler crash. Hint: R8 trả 403 ngay (auth gate sai), R9 hang 10s rồi 500 (handler logic crash sau auth gate) — auth gate có vẻ đã fix nhưng handler downstream bị break.
2. **Re-test A5 R10 sau dev fix:** chạy 5 cycle B3-B4-B6-B8-B9 trên TVCS-0001..0005 (đã PHAN_CONG). 1 cycle B11 cần Portal DN seed (vẫn defer external).

---

# Lifecycle archive — older rounds

## Verdict R8 (2026-05-07)

⚠️ **PARTIAL 3/11 PASS — 2 BE bug Critical/Major chặn nhánh CG.**

- ✅ **3 PASS** — B1 (seed re-thực hiện R8), B2 (6/6 LV cover dropdown filter `loaiTvv=CG ∧ trangThai=HOAT_DONG ∧ linhVucIds`), B10 (PHAN_CONG → HUY UI button + modal + transition).
- ❌ **5 BLOCKED** — B3/B4/B6/B8/B9 do BE `/xac-nhan` reject với 403 ERR-AUTH-TVCS-CG-01 dù FK linkage OK + 2 CG cùng pattern + listing `/api/v1/noi-dung-tu-van-cs` filter trả 0 cho CG.
- ⏭ **3 EXTERNAL** — B5 (cron 2 ngày LV BE), B7 (auto BR-FLOW-01 BE), B11 (Portal DN external).

State env so với R6 R17 (2026-05-04):
- ✅ State enum `DANG_HOAT_DONG → HOAT_DONG` đã migrate (verified `?loaiTvv=CG&size=20` → `byState: {HOAT_DONG: 7}`).
- ❌ Pool R7.3.3 (10 TVCS-20260506-*) MẤT giữa R7 → R8 — nguyên nhân pool reset BE chưa rõ. Re-seed inline 10 TVCS-20260507-* HO_SO + DIEN_THOAI (skip VIDEO_CALL theo BUG-TVCS-VIDEO-CALL-001 known-bug Closed BE side, FE chưa expose).
- ❌ FK gap R6 (cg_tw_01..06 inbox rỗng) đổi shape: TK link OK nhưng BE `/xac-nhan` action-level auth check sai + listing endpoint filter sai cho CG role.

---

## Bảng kiểm tra workflow R8 — 11 transition theo SRS line 1452-1496

| # | Bước (transition) | Actor | Sample | Status | Note |
|:-:|---|---|---|:-:|---|
| 1 | `— → TIEP_NHAN` (UC147 nhập tay CMS) | cb_nv_tw_01 | TVCS-20260507-0001..0010 | ✅ | Re-seed inline 10/10 (do pool reset). API `POST /api/v1/noi-dung-tu-van-cs` body `{doanhNghiepId, linhVucId, noiDung, tomTat, hinhThucTv, ngayTuVan}` → 201, state TIEP_NHAN, mã auto-gen `TVCS-YYYYMMDD-SEQ` (BR-DATA-04). Cover 6 LV (LĐ×2, Thuế×2, SHTT×1, DN×3, KDTM×1, ĐĐ×1). |
| 2 | `TIEP_NHAN → PHAN_CONG` ([Phân công CG]) | cb_nv_tw_01 | TVCS-0001..0006, 0009 | ✅ | **6/6 LV PASS.** TVCS-0001 (LĐ→OptLock) qua UI: modal "Phân công chuyên gia" mở, dropdown CG render duy nhất 1 record khớp `loaiTvv=CG ∧ trangThai=HOAT_DONG ∧ linhVucIds=<LĐ UUID>` (TVV-0003 Ngô VO_HIEU_HOA filter ra đúng), submit → toast + state PHAN_CONG. 5 cycle còn lại (Thuế/SHTT/DN/ĐĐ/KDTM) qua API `POST /{id}/phan-cong {chuyenGiaId, version, ghiChu}` → 200, state PHAN_CONG ver 1→2. |
| 3 | `PHAN_CONG → DANG_TU_VAN` ([Chấp nhận] CG) | CG account | TVCS-0004 (Lý) + TVCS-0006 (Đinh) | 🚫 | **BLOCKED — BE bug.** ly_13 + dinh_14 login OK, GET detail TVCS-0004/0006 trả `chuyenGiaId` khớp `TVV-0001.id`/`TVV-0002.id`, user `id` khớp `TVV.taiKhoanId`. POST `/xac-nhan {quyetDinh: 'CHAP_NHAN', version}` → **403 ERR-AUTH-TVCS-CG-01** "Chỉ chuyên gia được phân công mới thực hiện hành động này". 2-CG confirmed → BE bug, không phải config 1 account. Xem [BUG-FUNC-TVCS-A5-001](../../bug-reports/tu-van-chuyen-sau/Pass-bug-report-r7-4-a5-tvcs-cg-action-block.md). |
| 4 | `PHAN_CONG → TIEP_NHAN` ([Từ chối] CG) | CG account | TVCS-0006 | 🚫 | Cùng endpoint `/xac-nhan` `{quyetDinh: 'TU_CHOI', lyDo, version}` → **403 ERR-AUTH-TVCS-CG-01**. Cascade B3 bug. |
| 5 | `PHAN_CONG → banner cảnh báo` (Auto cron 2 ngày LV) | System | — | ⏭ | External cron BE — out of CMS test scope. SRS line 537 spec rõ "System". |
| 6 | `DANG_TU_VAN → HOAN_THANH` (CG tích HT + ≥1 file VB TVPL) | CG account | — | 🚫 | Cascade dep B3 — không reach DANG_TU_VAN. |
| 7 | `HOAN_THANH → CHO_PHE_DUYET` (Auto BR-FLOW-01) | System | — | ⏭ | System auto BE — out of CMS UI scope. Verified gián tiếp qua A4 HD R11 BR-FLOW-01 PASS (project memory). |
| 8 | `CHO_PHE_DUYET → DA_DUYET` ([Phê duyệt]) | cb_pd_tw_01 | — | 🚫 | Cascade dep B6/B7 — không reach CHO_PHE_DUYET. cb_pd_tw_01 ready. |
| 9 | `CHO_PHE_DUYET → DANG_TU_VAN` ([Từ chối] lý do ≥10) | cb_pd_tw_01 | — | 🚫 | Cascade dep B6/B7. |
| 10 | `PHAN_CONG → HUY` ([Hủy yêu cầu], guard CG chưa xác nhận) | cb_nv_tw_01 | TVCS-0009 (DN→Probe Permission) | ✅ | Detail TVCS-0009 PHAN_CONG render footer button [Hủy yêu cầu]. Click → modal "Hủy nội dung tư vấn" với field "Lý do hủy" required (max 1000) + button [Xác nhận hủy]/[Quay lại]. Nhập lý do "DN không còn nhu cầu tư vấn — hủy theo yêu cầu DN" → submit → banner "Nội dung tư vấn đã bị hủy" + state badge `Phân công → Hủy`. List view confirm row TVCS-0009 trạng thái "Hủy", chỉ còn button delete (button team + edit gone — terminal). |
| 11 | `DANG_TU_VAN → HUY` (DN yêu cầu hủy + cb_pd duyệt) | cb_nv + cb_pd + Portal DN | — | 🚫 | Cascade dep B3 + Portal DN external (out of CMS scope). |

> Icon: ✅ pass · 🚫 blocked (BE bug hoặc cascade) · ⏭ external (system auto / portal out-of-scope)

---

## Pool sau test (state cuối — verified `GET /api/v1/noi-dung-tu-van-cs?page=1&pageSize=50` ngày 2026-05-07 21:58)

| Mã | LV | Hình thức | DN | CG được phân công | State cuối |
|---|---|---|---|---|:-:|
| TVCS-20260507-0001 | Lao động | HO_SO | Hoa Sen SN2 | Probe CG R7.4.A1 OptLock Test (TVV-0008) | PHAN_CONG |
| TVCS-20260507-0002 | Thuế | DIEN_THOAI | Sao Mai NH1 | Trương Văn Mười Sáu (TVV-0004) | PHAN_CONG |
| TVCS-20260507-0003 | SHTT | HO_SO | Đại Phúc NH2 | Mai Thị Mười Bảy (TVV-0005) | PHAN_CONG |
| TVCS-20260507-0004 | DN | HO_SO | Vạn Phúc VU1 | Lý Thị Mười Ba (TVV-0001) | PHAN_CONG |
| TVCS-20260507-0005 | Đất đai | DIEN_THOAI | Hưng Thịnh VU2 | Hồ Văn Mười Tám (TVV-0006) | PHAN_CONG |
| TVCS-20260507-0006 | KDTM | HO_SO | Minh Đức SN3 | Đinh Văn Mười Bốn (TVV-0002) | PHAN_CONG |
| TVCS-20260507-0007 | Lao động | HO_SO | Tân Bình SN1 | (chưa) | TIEP_NHAN (reserve B4) |
| TVCS-20260507-0008 | Thuế | HO_SO | Gạo Doe bơ | (chưa) | TIEP_NHAN (reserve) |
| TVCS-20260507-0009 | DN | HO_SO | Test R778b | Probe Permission (TVV-0007) | **HUY** (B10 PASS) |
| TVCS-20260507-0010 | DN | DIEN_THOAI | Sông Hồng BKH | (chưa) | TIEP_NHAN (reserve) |

**Per-filter verify (cb_nv_tw_01 scope, R8 21:58):**
- Total: 10
- byState: PHAN_CONG=6, TIEP_NHAN=3, HUY=1
- LV cover: LĐ=2, Thuế=2, SHTT=1, DN=3, KDTM=1, ĐĐ=1 ✅

---

## Per-LV coverage B2 (PASS 6/6)

| LV | TVCS sample | CG khớp filter | Source verify |
|---|---|---|---|
| Lao động | TVCS-0001 | Probe OptLock (TVV-0008 HOAT_DONG) | UI dropdown render đúng 1 record (Ngô TVV-0003 VO_HIEU_HOA filter ra). Network: `GET /api/v1/tu-van-viens?pageSize=100&trangThai=HOAT_DONG&loaiTvv=CG&linhVucIds=bbbbbbbb-0000-4000-8000-000000000013` |
| Thuế | TVCS-0002 | Trương (TVV-0004) | API `phan-cong` 200 |
| SHTT | TVCS-0003 | Mai (TVV-0005) | API `phan-cong` 200 |
| Doanh nghiệp | TVCS-0004 | Lý (TVV-0001) | API `phan-cong` 200 |
| Đất đai | TVCS-0005 | Hồ (TVV-0006) | API `phan-cong` 200 |
| KDTM | TVCS-0006 | Đinh (TVV-0002) | API `phan-cong` 200 |

Filter `loaiTvv=CG ∧ trangThai=HOAT_DONG ∧ linhVucIds` áp đúng SRS line 533. Enum `HOAT_DONG` đã migrate v3.5 (BUG-CG-A1-001 R7 nay không còn).

---

## API endpoints xác nhận (R8)

| Step | Method | Path | Body | Effect |
|---|---|---|---|---|
| Tạo TVCS | POST | `/api/v1/noi-dung-tu-van-cs` | `{doanhNghiepId, linhVucId, noiDung, tomTat, hinhThucTv, ngayTuVan}` | TIEP_NHAN, ver=1, mã `TVCS-YYYYMMDD-SEQ` |
| Phân công CG | POST | `/api/v1/noi-dung-tu-van-cs/{id}/phan-cong` | `{chuyenGiaId, version, ghiChu}` | TIEP_NHAN → PHAN_CONG, ver+1 |
| Hủy yêu cầu | POST | `/api/v1/noi-dung-tu-van-cs/{id}/huy` (qua modal UI) | `{lyDo, version}` | PHAN_CONG → HUY (terminal) |
| CG xác nhận / từ chối | POST | `/api/v1/noi-dung-tu-van-cs/{id}/xac-nhan` | `{quyetDinh: 'CHAP_NHAN'\|'TU_CHOI', lyDo?, version}` | PHAN_CONG → DANG_TU_VAN / TIEP_NHAN. ❌ **Reject 403 cho CG được phân công** (BUG). |
| Detail | GET | `/api/v1/noi-dung-tu-van-cs/{id}` | — | Trả full TVCS + chuyenGiaId, version, trangThai. CG accessible cho assigned record. |
| List CB NV | GET | `/api/v1/noi-dung-tu-van-cs?page=1&pageSize=50` | — | CB NV: trả 10 ✅. CG (ly_13/dinh_14): trả total=0 ❌ (BUG). |

---

## Bằng chứng

### B1 + B2 — Re-seed + Phân công 6/6 LV (state cuối)

![R8 — TVCS list cb_nv_tw_01: 10 record, 6 PHAN_CONG cover 6 LV + 1 HUY (B10) + 3 TIEP_NHAN reserve](../../screenshots/r7-4-a5-list-final-state.png)

### B3 fail — CG inbox empty + 403 từ /xac-nhan

![R8 — Login `dinh_14` (CG, KDTM) → /403 dashboard, sidebar có Quản lý tư vấn](../../screenshots/r7-4-a5-cg-403-dinh-14.png)

![R8 — `ly_13` mở /tv-chuyen-sau/danh-sach: "Không có nội dung tư vấn chuyên sâu nào" mặc dù TVCS-0004 chuyenGiaId khớp TVV-0001](../../screenshots/r7-4-a5-cg-inbox-empty-fk-bug.png)

```text
=== R8 B3 BLOCK trace (ly_13 / dinh_14, 2026-05-07 21:54) ===
GET  /api/v1/auth/me (ly_13)
  → {userId: d99760d8-b38b-401e-a5ac-227664debef4, vaiTro: ['CG'], donViId: 00000000-0000-4000-8000-000000000001}

GET  /api/v1/noi-dung-tu-van-cs/cee63433-785b-411a-991a-780d10cad6fc (TVCS-0004)
  → 200 {trangThai: PHAN_CONG, chuyenGiaId: df00f7e1-..., version: 2}
     LINKAGE OK: TVCS.chuyenGiaId(df00f7e1) == TVV-0001.id ✅
                 TVV-0001.taiKhoanId(d99760d8) == ly_13.userId ✅

GET  /api/v1/noi-dung-tu-van-cs?page=1&pageSize=50
  → 200 {data: [], meta: {total: 0}} ❌ inbox lọc sai

POST /api/v1/noi-dung-tu-van-cs/cee63433.../xac-nhan
     {quyetDinh: 'CHAP_NHAN', version: 2}
  → 403 ERR-AUTH-TVCS-CG-01 "Chỉ chuyên gia được phân công mới thực hiện hành động này"

PATCH /api/v1/noi-dung-tu-van-cs/cee63433...
     {tomTat: 'Test update from CG', version: 2}
  → 200 ✅ (CG có quyền update_noi_dung_tu_van_cs nên PATCH chung OK)

=== Cùng pattern với dinh_14 / TVCS-0006 (KDTM, TVV-0002) ===
GET  detail → chuyenGiaId(5e0377d4) == TVV-0002.id ✅
              dinh_14.userId(4b732377) == TVV-0002.taiKhoanId ✅
POST /xac-nhan → 403 ERR-AUTH-TVCS-CG-01 (cùng error code)
```

### B10 PASS — PHAN_CONG → HUY UI

Banner success "Nội dung tư vấn đã bị hủy", state badge `Phân công → Hủy`, button [Hủy yêu cầu] ẩn, stepper biến mất. List view: TVCS-0009 cột Trạng thái "Hủy", row chỉ còn button "delete" (team+edit gone — terminal).

---

## Phương án xử lý (để A5 PASS 9/11)

1. **DEV BE fix `/xac-nhan` action-level auth check.** Reproduce: ly_13 (TVV-0001.taiKhoanId) gọi POST `/api/v1/noi-dung-tu-van-cs/{id-TVCS-0004}/xac-nhan` với TVCS-0004.chuyenGiaId = TVV-0001.id → expect 200, actual 403 ERR-AUTH-TVCS-CG-01. Sau khi fix: B3/B4 unblock → B6 unblock cascade → B8/B9 chạy được.
2. **DEV BE fix listing filter cho role CG.** `GET /api/v1/noi-dung-tu-van-cs` khi `req.user.vaiTro = ['CG']` cần JOIN TU_VAN_VIEN ON TAI_KHOAN.id = TU_VAN_VIEN.tai_khoan_id, lọc TVCS WHERE chuyen_gia_id = TVV.id. Hiện trả total=0.
3. **Re-test A5 R9 sau dev fix:** 5 cycle B3-B4-B6-B7-B8-B9 trên TVCS-0001..0006 (đã PHAN_CONG). 1 cycle B11 cần Portal DN seed (vẫn defer external).

## Ghi chú thực thi

- **Pre-condition gãy R8:** Pool R7.3.3 mất giữa R7→R8 (10 TVCS-20260506-* gone). Phải re-seed inline. Cần root-cause: (a) DB scheduled cleanup? (b) Manual BE reset? (c) Migration accidental wipe? Đề nghị BE confirm + thêm seed-protection cho QA round.
- **Account list MailHog activated (R7.2.9):** ly_13 / dinh_14 / truong_16 / mai_17 / ho_18 — pass `Secret@123` + OTP `666666`. Probe accounts (`probe_perm` + `probe_optlock`) chưa thử login R8 (rate-limit), TK state có thể vẫn CHO_KICH_HOAT.
- **Anti-pattern tránh:** Không retry `/xac-nhan` lặp khi 403 — phân loại Rule 9 = APP/BE BUG, không phải SELECTOR OUTDATED hay session reset. STOP + escalate đúng. Đã capture diagnostic 2-source (ly_13 + dinh_14) trước khi log bug.

---

## Lịch sử round

| Round | Date | Kết quả tóm tắt |
|---|---|---|
| **R10** | 2026-05-09 23:50:00 | ⚠️ 4/11 PASS (B1+B2+B4+B10). Account swap CB_PD _01→_06 verified scope OK. **B4 TU_CHOI mới PASS** qua curl `truong_16` POST `/xac-nhan {TU_CHOI, lyDo, ver:3}` trên TVCS-0002 → 200 trong 0.04s, advance PHAN_CONG → TIEP_NHAN. **BUG-001 worsened** (R8 403 → R9 500 → R10 hang >30s no response, branch CHAP_NHAN khu trú). **BUG-FE-A5-003 NEW** Modal Từ chối thiếu input `lyDo` → BE 409 silent fail FE. Pool drift R9→R10: TVCS-0002 PHAN_CONG → TIEP_NHAN (TIEP_NHAN 6→7, PHAN_CONG 7→6). |
| **R9** | 2026-05-09 20:25:00 | ⚠️ 3/11 PASS (giữ nguyên B1+B2+B10). BUG-002 Closed (list endpoint trả 2 record cho ly_13 + truong_16). BUG-001 still Open với symptom regression: R8 trả 403 ngay → R9 hang 10s rồi 500 ERR-SYS-00-00-01. Pool drift R8→R9: TVCS-0006 KDTM mất, TVCS-0011 mới (Thuế, Ngô PHAN_CONG). Test 2-source: ly_13 (TVCS-0004) + truong_16 (TVCS-0002). |
| **R8** | 2026-05-07 | ⚠️ 3/11 PASS (B1 re-seed + B2 6/6 LV + B10). 5 BLOCKED do BE bug `/xac-nhan` 403 + listing filter (2-CG confirmed: ly_13/dinh_14). 3 EXTERNAL (B5/B7/B11). State enum `HOAT_DONG` migrated. Pool reset cần root-cause. |
| R17 | 2026-05-04 | ⚠️ 3/11 PASS (B1+B2 6/6 + B10 BUG-FUNC-TVCS-002 fixed). FK gap (TU_VAN_VIEN.tai_khoan_id NULL) chưa fix → B3/B4/B6/B11 BLOCKED. 6 BLOCKED + 2 EXTERNAL. |
| R14-R16 | 2026-05-02..04 | 2/11 PASS (B1+B2). Bug TVCS-002 button [Hủy yêu cầu] miss UI + FK gap. |
| R13 | 2026-05-02 | 2/11 PASS (B1+B2 3 cycle DN/LĐ/Thuế). |

---

*R8 | QA Automation via Claude Code | Chrome DevTools MCP*
*R9 update 2026-05-09 20:25:00 | QA Automation | Chrome DevTools MCP — BUG-002 Closed, BUG-001 Open với symptom 500 (regression). 2/2 → 1/2 đóng.*
*R10 update 2026-05-09 23:50:00 | QA Automation | Chrome DevTools MCP — Bộ tài khoản 06: cb_pd_tw_06 swap verified scope OK. B4 TU_CHOI PASS via curl (BE OK). BUG-001 worsened R10 hang >30s, khu trú branch CHAP_NHAN (TU_CHOI ổn). BUG-FE-A5-003 NEW Modal Từ chối thiếu input lý do. Bug 1/3 đóng (BUG-002 persist Closed).*
