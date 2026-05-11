# Functional Test Report — Vụ việc HTPL (R7.7.3)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Module** | Vụ việc HTPL (FR-IV) |
| **Round** | R7 (R7.7.3) |
| **Ngày test** | 2026-05-09 13:15:00 → 13:30:00 |
| **Account chính** | `cb_nv_tw_03` (primary) · `cb_nv_dp_01 (AG)` · `cb_nv_bn_01 (BKH)` · `qtht_01` |
| **Tool** | Chrome DevTools MCP (UI click chain + API verify song song) |
| **Spec ref** | [output/funtion/7.5-vu-viec-htpl.md](../../../funtion/7.5-vu-viec-htpl.md) v3.5 (72 TC) · [SRS FR-IV](../../../../input/srs-update-2026-5-5/srs-fr-iv-vu-viec.md) |

---

## Verdict

⚠️ **PARTIAL PASS — 40/72 TC chạy (56%) — 33 PASS, 1 FAIL Major, 2 Partial, 1 Sai spec.** (R7+R8+R14+R15+R16-P2..P5+**R17 reverify+R18 cộng dồn**) · **PHANCONG-REVERT-01 đóng R17** · **+3 finding mới R18 (POOL-CG-MISSING + TVV-DETAIL-403 + TVV-PERMISSION-GAP)**.

Pool VV: 20 records (R16 stable — 18 BTP-TW + 2 STP-AG/cross-donVi).

---

## R18 — Phân công cascade + lifecycle DANG_XU_LY → CHO_PHE_DUYET (2026-05-11 17:10 → 17:30) (LATEST)

Tester: `cb_nv_tw_03` + `cb_nv_tw_02` (CB NV cấp TW) + `tvv_r11_mailfix` (TVV) isolatedContext `reverify_r17_2026_05_11`. Tool: Chrome DevTools MCP UI click chain + native value setter cho textarea AntD + API verify. Scope: TC unblock sau R17 reverify PHANCONG-REVERT đóng.

### Bảng trạng thái TC (snapshot R18 — LATEST 2026-05-11 17:30:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| VV-013 | Phân công cá nhân TVV (fresh) | ✅ Đạt | R17 reverify | hương tvv1 → DA_PHAN_CONG OK |
| VV-013b | Phân công cá nhân NHT | ✅ Đạt | R18 | NHT R11 BUG003 → state+LICHSU PHAN_CONG_CA_NHAN |
| VV-013c | Phân công Tổ chức TV | ✅ Đạt | R18 | TC Alpha + TVV R13 → loaiDoiTuong=TO_CHUC + LICHSU PHAN_CONG_TO_CHUC |
| VV-014 | TVV xác nhận phân công | ✅ Đạt | R18 | endpoint `/nhan-phan-cong` → state DANG_XU_LY + LICHSU XAC_NHAN_PHAN_CONG |
| VV-015/017 | Cập nhật kết quả VV | ✅ Đạt | R18 | CB NV submit → LICHSU CAP_NHAT_KQ |
| VV-033 | Trình phê duyệt → CHO_PHE_DUYET | ✅ Đạt | R18 | CB NV submit → state CHO_PHE_DUYET + LICHSU TRINH_PD (alias) |
| **Tổng R18 unblock** | **6 TC** | ✅ 6 / ⚠️ 0 / ❌ 0 | | LICHSU enum mới 5 (4 spec match + 1 alias) |

### Bảng TC chưa chạy được — cần làm gì để chạy (R18)

Hiện tại còn ~32 TC chưa chạy được — chia 3 nhóm: 1 chờ dev fix · 28 chờ external infra · 3 finding mới cần BA confirm + dev fix.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| Pool phân công cá nhân (multi-VV) | CG không hiển thị trong dropdown CÁ NHÂN dù khai báo LV match (nhóm B) | Dev BE: bỏ filter loại CG khỏi pool cá nhân theo spec FR-V.I-09 line 766 "TVV/CG hoặc NHT" | Dev BE |
| VV-014 native UI | TVV `/vu-viec/{id}` UI 403 dù được phân công VV (nhóm B) | Dev FE: cho TVV route view chi tiết VV được giao | Dev FE |
| VV-015/017 native TVV | TVV thiếu permission `cap-nhat-ket-qua` + `trinh-phe-duyet` (nhóm B) | BA confirm spec ai update KQ (TVV vs CB NV). Nếu TVV → BE add permission cho role TVV | BA + Dev BE |
| Cluster 1-2 privacy mTLS | Chờ infra mTLS PLQG cert (nhóm D) | Infra cấp cert + endpoint whitelist test client | Infra |
| ~28 TC còn (Cluster 2-8) | Đa số chờ DN VNeID Tier 2 sandbox (nhóm D) | Infra + Dev VNeID T2 sandbox | Infra |

### Method R18

1. **VV-013b** — `cb_nv_tw_03` walk VV-BTP-TW-20260511-002 (DA_TIEP_NHAN → DANG_KIEM_TRA → DA_PHAN_CONG) — pool dropdown 8 options (7 NHT + 1 TVV, **0 CG** dù `huongcg` LV Lao động active → finding POOL-CG-MISSING-01). Pick NHT R11 BUG003 → submit. GET sau 3s: state=DA_PHAN_CONG ✓ + version=3 + nguoiXuLyId=22fff56e ✓ + loaiDoiTuong=CA_NHAN ✓ + LICHSU=[PHAN_CONG_CA_NHAN, KIEM_TRA, TAO_VV] ✓.
2. **VV-013c** — `cb_nv_tw_03` walk VV-STP-AG-20260509-001 → switch radio "Tổ chức tư vấn" → dropdown 7 TC + dropdown TVV thuộc TC (4 TVV gồm cả CG `Hồ Văn Mười Tám`) — pick TC Alpha + TVV R13 A19 Gate. POST 201: state=DA_PHAN_CONG + loaiDoiTuong=**TO_CHUC** ✓ + toChucTuVanId=beb25e6f ✓ + LICHSU **`PHAN_CONG_TO_CHUC`** ✓. Mail UC62 deliver DN `phucanag@example.test` ✓.
3. **VV-014** — switch sang `tvv_r11_mailfix` (QA self-seed password reset lần 2 — Secret@123). Navigate `/vu-viec/{id}` → 403 (finding TVV-DETAIL-403). List page `/vu-viec/danh-sach` thấy VV-QA-R7-SLA-BT. Probe API `/nhan-phan-cong` (per permission `nhan-phan-cong_vu_viec`) → 201 state advance **DANG_XU_LY** + LICHSU **`XAC_NHAN_PHAN_CONG`** ✓ + phancong.trangThai=CHAP_NHAN.
4. **VV-015/017** — finding TVV thiếu permission `cap-nhat-ket-qua` (403 trên endpoint). Switch CB NV `cb_nv_tw_02` → UI [Cập nhật kết quả] modal → fill textarea native value setter → submit. LICHSU enum **`CAP_NHAT_KQ`** ✓.
5. **VV-033** — CB NV click [Trình phê duyệt] → modal confirm → submit. State=**CHO_PHE_DUYET** ✓ + version=5 + nguoiGuiDuyetId set + LICHSU enum **`TRINH_PD`** (alias mismatch vs spec `TRINH_PHE_DUYET`).

### LICHSU enum coverage cumulative sau R18

12/18 spec enum match: `TAO_VV` ✓ · `KIEM_TRA` ✓ · `PHAN_CONG_CA_NHAN` ✓ (R18 mới) · `PHAN_CONG_TO_CHUC` ✓ (R18 mới) · `XAC_NHAN_PHAN_CONG` ✓ (R18 mới) · `CAP_NHAT_KQ` ✓ (R18 mới) · `PHE_DUYET` ✓ · `HOAN_THANH` ✓ · `DANH_GIA` ✓ · `CONG_KHAI` ✓ · `HUY_CONG_KHAI` ✓ · `MO_LAI` ✓.

Alias spec mismatch (1): `TRINH_PD` thay vì `TRINH_PHE_DUYET`.

Miss 5 spec enum: `TIEP_NHAN` · `TU_CHOI` · `TU_CHOI_DUYET` · `YEU_CAU_BO_SUNG` · `DANH_GIA` chi tiết (đã có nhưng có thể có sub-enum).

Legacy extras (3): `CREATE` (VV cũ) · `UPDATE` (generic) · `APPROVE` (cũ).

→ LICHSU-01 progress: 10/18 → **12/18 spec match (67%)** + 1 alias + 3 legacy. Vẫn giữ Open Major cho miss 5 spec + alias.

---

## R16 Phase 3+4 — Cluster 1 Công khai PLQG + Multi-role permission + Immutability (2026-05-11 14:35 → 14:42)

Tester: `cb_pd_tw_05` (CB PD) isolatedContext `r16p3_cbpd_2026_05_11` + `huongcg` (CG) isolatedContext `r16p4_tvv_2026_05_11` + `cb_nv_tw_01` (CB NV+PD) isolatedContext `r16p2_2026_05_11`. Tool: Chrome DevTools MCP UI + API. Scope: chạy TC không phụ thuộc PHANCONG-REVERT fix.

### Bảng trạng thái TC (snapshot R16-P3+P4 — LATEST 2026-05-11 14:42:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| **C1-1** | Công khai DA_DANH_GIA happy path | ✅ Đạt | R16-P3 | POST /cong-khai 200 + `congKhai=true` + `thoiGianDangTai` + button flip. |
| **C1-2** | P0 Privacy whitelist 9 fields | 🚫 Không test được | R16-P3 | Endpoint `/api/v1/public/vu-viecs` 401 ERR-AUTH-MTLS-01 — cần mTLS T2 cert. |
| **C1-3** | Negative TU_CHOI ẩn nút Công khai | ✅ Đạt | R16-P3 | UI button hidden + force POST → 409 ERR-STATE-VI-CK-01. |
| **C1-7** | Hủy công khai + flip flag | ✅ Đạt | R16-P3 | POST /huy-cong-khai 200 + `congKhai=false` + `thoiGianDangTai=null`. |
| **VV-013d** | CG/non-actor 403 trên list+detail VV | ✅ Đạt | R16-P4 | huongcg GET /vu-viecs + detail random → 403 ERR-PERM-SYS-00-01. |
| **VV-023** | Immutability final state | ✅ Đạt | R16-P4 | PATCH DA_DANH_GIA + TU_CHOI → 409 ERR-STATE-VI-01-05. |
| **VV-026** | TVV scope filter | ✅ Đạt | R16-P5 | QA tự seed: forgot-password `tvv.r11.mailfix` → reset → login → GET /vu-viecs → 1/1 (chỉ VV-509-008 gán mình, KHÔNG thấy 20 VV như CB). |
| **C3-4/5/6/7** | Phân công negative ERR-PC-05/06/07 | 🚫 Không test được | R16-P4 | Block bởi BUG-PHANCONG-REVERT-01 (không có VV state DA_PHAN_CONG persist). |

### Bảng TC chưa chạy được — cần làm gì để chạy (R16-P3+P4+P5)

Hiện tại còn 37 TC chưa chạy được — chia 3 nhóm: 1 chờ mTLS PLQG sandbox (C1-2 P0) + 8 chờ dev fix PHANCONG-REVERT + 28 còn lại (VNeID T2 + LICHSU enum + SLA backdated).

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| C1-2 | Endpoint public PLQG yêu cầu mTLS T2 cert | Infra setup mTLS sandbox cert + cấu hình QA env | Infra |
| C3-4/5/6/7 | Phân công không persist (cascade PHANCONG-REVERT-01) | Dev BE fix transaction atomic | Dev BE |

### R16-P5 — QA seed TVV active + verify VV-026 scope (2026-05-11 15:15 → 15:18)

1. Login `qtht_01` → GET `/api/v1/tu-van-viens?trangThai=HOAT_DONG` → 8 TVV/CG HOAT_DONG, pick `tvv.r11.mailfix@test.htpldn.vn` (id 06748bb5...).
2. GET TVV detail → `taiKhoanId=b7a05555-ebbb-4369-8b60-0354cdf0e100`. GET `/api/v1/tai-khoan/{id}` → username thực tế là `tvv_r11_mailfix` (KHÔNG phải email), state `HOAT_DONG`, vai trò `TVV` cấp DP.
3. DELETE MailHog → POST `/api/v1/auth/forgot-password { email: tvv.r11.mailfix@test.htpldn.vn }` → 200 mail trong MailHog với token `add8c43f-297f-4f84-893c-cf912e8dc536`.
4. POST `/api/v1/auth/reset-password { token, newPassword: Secret@123, newPasswordConfirm: Secret@123 }` → 200 "Mật khẩu đã được đặt lại thành công".
5. POST `/api/v1/auth/login { username: tvv_r11_mailfix, password: Secret@123 }` → 200 trả `otpToken`. POST `/api/v1/auth/verify-otp { otpToken, otpCode: 666666 }` → 200 trả `accessToken`. (Schema discovery: field name là `otpCode` không phải `otp`/`code`.)
6. GET `/api/v1/auth/me` → 200 vai trò `TVV` ✓. GET `/api/v1/vu-viecs?page=1&size=100` → trả ĐÚNG **1 VV** (VV-BTP-TW-20260509-008, gán `nguoiXuLyId=tvv_r11_mailfix`). Compare CB scope = 20 VV → scope filter chính xác.
7. UI verify: navigate `/vu-viec` → tab "Tất cả (1)", "Hoàn thành (1)", các tab khác đều `(0)` ✓ → VV-026 PASS.

### Method R16-P3+P4

1. **Phase 3 Cluster 1** — login `cb_pd_tw_05` fresh context → navigate VV-510-002 (DA_DANH_GIA cleaned) → click [Công khai] → fill mô tả công khai 339 ký tự → submit `POST /cong-khai` 200 (`moTaCongKhai` only). Verify `congKhai=true`, `thoiGianDangTai=2026-05-11T07:37:39.570Z`, timeline +1 "Công khai · 11/05/2026 14:37 · CB Phê duyệt TW 05", button flip [Hủy công khai].
2. **C1-7 huỷ** — click [Hủy công khai] → confirm dialog → `POST /huy-cong-khai` 200, body `{}`. Verify `congKhai=false`, `thoiGianDangTai=null`, state preserved DA_DANH_GIA, `moTaCongKhai` retained (observation).
3. **C1-3 negative** — navigate VV-507-004 (TU_CHOI) → verify NO [Công khai] button. Force `POST /cong-khai` → 409 ERR-STATE-VI-CK-01 "Chỉ vụ việc đã duyệt mới được công khai".
4. **C1-2 mTLS probe** — GET `/api/v1/public/vu-viecs` không cert → 401 ERR-AUTH-MTLS-01. Block.
5. **Phase 4 CG scope** — login `huongcg` fresh context → CG sidebar KHÔNG có module VV. Force `GET /api/v1/vu-viecs` list + 2 detail UUID → cả 3 đều 403 ERR-PERM-SYS-00-01.
6. **Phase 4 Immutability** — login `cb_nv_tw_01` (dual CB_NV+CB_PD) → PATCH VV-510-002 (DA_DANH_GIA) + VV-507-004 (TU_CHOI) → cả 2 đều 409 ERR-STATE-VI-01-05.

### Findings R16-P3+P4 (observations chưa log bug)

- **C1-Privacy CMS endpoint trả full record:** `POST /cong-khai` response (CMS) trả full entity gồm `moTa`, `ketQuaTomTat`, `diemDanhGia`, `nguoi*Id` — đây là OK cho FE refresh detail, KHÔNG vi phạm privacy. Privacy gate enforce ở `/api/v1/public/vu-viecs` mTLS endpoint (chưa test được).
- **C1-7 moTaCongKhai retained sau huỷ:** sau `POST /huy-cong-khai`, field `moTaCongKhai` vẫn giữ trong DB. Nếu user công khai lại sẽ thấy mô tả cũ. Observation, không phải bug (SRS không yêu cầu clear khi huỷ).
- **Hủy công khai không có textbox `ly_do_huy`:** modal chỉ là confirm 2 nút. BE accept body `{}`. Nếu SRS yêu cầu `ly_do_huy` required → đây là deviation. Cần BA confirm.

---

## R16 Phase 2 — Fresh-trigger retest NOTIF + LICHSU (2026-05-11 14:22 → 14:30 cb_nv_tw_03)

Tester: `cb_nv_tw_03` isolatedContext `r16p2_2026_05_11`. Tool: Chrome DevTools MCP UI + API. Scope: clear cache + DELETE MailHog + walk fresh VV-BTP-TW-20260511-001 từ DA_TIEP_NHAN qua đủ chuỗi để retest NOTIF-01 + LICHSU-01 đúng phương pháp (response to user feedback "đã clear cache trước verify chưa?").

### Bảng trạng thái TC (snapshot R16-P2 — LATEST 2026-05-11 14:30:00)

Tổng 72 TC. Chỉ liệt kê TC có thay đổi status hoặc TC mới chạy R16-P2.

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| **VV-007** | Kiểm tra DA_TIEP_NHAN→DANG_KIEM_TRA | ✅ Đạt | R16-P2 | Click [Kiểm tra hồ sơ] → state advance OK, lich-su +1 enum KIEM_TRA. |
| **VV-013/014/015/017/033** | Walk lifecycle sau Phân công | 🚫 Không test được | R16-P2 | Block bởi BUG-PHANCONG-REVERT-01 (state revert silent). |
| VV-031 | UC62 notification | ✅ Đạt | R16-P2 | Fresh trigger phân công → 2 mail (DN + TVV/NHT). BUG-NOTIF-01 Closed. |
| C8-3 | LICH_SU 18 enum | ⚠️ Partial | R16 | 11/18 ≈ 61% (+1 DANH_GIA từ R15 C5-1). 7 enum còn thiếu. |
| **NEW** | **POST /phan-cong state revert** | 🆕 ❌ Lỗi | R16-P2 | Mail bay OK nhưng VU_VIEC state không persist. Critical data integrity. → BUG-PHANCONG-REVERT-01. |
| **Tổng cộng** | **72 TC** | ✅ 23 · ⚠️ 3 · ❌ 4 · 🚫 8+ (mới block) · ⏭ 14 · 🤷 0 | | |

### Bảng TC chưa chạy được — cần làm gì để chạy (R16-P2)

Hiện tại còn 35 TC chưa chạy được — chia 4 nhóm: 8 chờ dev fix PHANCONG-REVERT mới + 16 chờ env VNeID + 3 cần seed backdated SLA + 8 LICHSU enum còn thiếu.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| VV-013/013b/013c | Phân công không persist (BUG-PHANCONG-REVERT-01) | Dev BE fix transaction để VU_VIEC state + PHAN_CONG_VU_VIEC record persist atomic với mail trigger | Dev BE |
| VV-014/015/017 | Cascade từ PHANCONG-REVERT — không có VV nào ở DANG_XU_LY/CHO_PHE_DUYET/DA_DUYET mới | Same as VV-013 | Dev BE |
| VV-033 | Cập nhật kết quả needs DA_PHAN_CONG → DANG_XU_LY persist | Same as VV-013 | Dev BE |
| C4-1/C4-2 | CB PD từ chối needs CHO_PHE_DUYET fresh | Same as VV-013 | Dev BE |
| C8-3 (deep) | 7 enum thiếu TIEP_NHAN/CAP_NHAT_KQ/YEU_CAU_BO_SUNG/TU_CHOI/PHAN_CONG_CA_NHAN/TO_CHUC/TU_CHOI_DUYET | Dev BE thêm enum log writer | Dev BE |
| Cluster 1-4-6-7 (16 TC) | DN VNeID T2 sandbox + DN verified | Infra setup | Infra |
| C3-1/2/3 (3 TC SLA backdated) | Pool chưa có VV deadline 11/16/21 ngày | Seed backdated | QA seed |

### Phương án test tiếp theo

| Nhóm | Áp dụng | Cần làm | Ưu tiên | Owner |
|---|---|---|---|---|
| Dev fix Critical | 7-8 TC | Fix BUG-PHANCONG-REVERT-01 (transaction atomicity giữa BE persist + mail) | **P0** | Dev BE |
| QA chạy tiếp khi unblock | VV-013/14/15/17/33/C4-1/C4-2 | Sau dev fix → walk fresh VV qua đủ chuỗi DA_PHAN_CONG → DANG_XU_LY → ... → DA_DANH_GIA, query LICH_SU cumulative cho VV đó | P0 | QA |
| QA test Cluster 1 (Công khai) | C1-1/2/3/7 | Test trên VV existing DA_DANH_GIA (VV-510-002/509-008/009) với `cb_pd_tw_05` — không chờ PHANCONG-REVERT fix | P1 | QA |
| BA confirm spec | C5-4 mechanism + C6-4 silent fallback | BA reply | P1 | BA |

### Method R16-P2

1. `curl -X DELETE http://103.172.236.130:8025/api/v1/messages` → MailHog 0 mail (clear cache evidence).
2. Browser logout `/api/v1/auth/logout` + `localStorage.clear()` + `sessionStorage.clear()`.
3. `mcp__chrome-devtools__new_page` isolatedContext `r16p2_2026_05_11` → login `cb_nv_tw_03` fresh.
4. Walk VV-BTP-TW-20260511-001 (DA_TIEP_NHAN, lich-su 1 enum TAO_VV) → click [Kiểm tra hồ sơ] → state DANG_KIEM_TRA ✓ + lich-su +1 KIEM_TRA ✓.
5. Click [Phân công] → modal → pick TVV hương tvv1 → submit. POST 201 với response DA_PHAN_CONG. **MailHog +2 mail (DN-r14 + TVV)** — UC62 + UC61 deliver.
6. GET VV detail 5s sau → state vẫn DANG_KIEM_TRA + version cũ + nguoiXuLyId NULL + PHAN_CONG_VU_VIEC array rỗng + LICH_SU 2 enum (không có PHAN_CONG).
7. Lặp với NHT → 201 + 2 mail mới + state vẫn revert. → BUG-PHANCONG-REVERT-01 reproducible 2/2.

---

## R15 Round (2026-05-11 09:19:00 → 09:50:00) — Audit post-fix + Cluster 5 UC67 + Cluster 6 BR-CALC-04

Tester: `cb_nv_tw_03` (CB NV) + `cb_pd_tw_05` (CB PD). Tool: Chrome DevTools MCP UI + API. Scope: skill `qa-bugfix-reverify-audit` audit 2 Open bug (NOTIF-01 + LICHSU-01) + chạy 5 TC chạy được không phụ thuộc env (Cluster 5 P0 + Cluster 6 P1).

### Bảng trạng thái TC (snapshot R15 — LATEST 2026-05-11 09:50:00)

Tổng 72 TC. Chỉ liệt kê TC ĐÃ CHẠY (29 TC) — TC chưa chạy gộp ở Bảng 2.

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| VV-001 | List + filter trạng thái | ✅ Đạt | R7 | Filter trangThai PASS. 3 obs minor defer. |
| VV-002 | Search keyword | ✅ Đạt | R13 | BE đổi `tuKhoa`→`keyword`. BUG-SEARCH-01 closed. |
| VV-003 | Tạo VV nhập tay | ✅ Đạt | R7 | Multi-channel TRUC_TIEP/DIEN_THOAI OK. |
| VV-004 | Validation required | ✅ Đạt | R13 | DN field nay required. BUG-VALIDATION-01 closed. |
| VV-006 | SLA 15 ngày LV | ✅ Đạt | R13 | Deadline +15 LV (NĐ55 Đ.8 K.1). BUG-SLA-01 closed. |
| VV-022 | SLA 4 mức cảnh báo | ⚠️ Sai spec | R7 | 1/4 mức verify (BINH_THUONG). 3 mức cần backdated. |
| VV-024 | Xuất Excel | ✅ Đạt | R7 | POST `/export` 200 + xlsx blob 8052 bytes. |
| VV-028 | QTHT view-only | ⚠️ Sai spec | R7 | UI ẩn OK; BE không 403 cho POST/PATCH/DELETE. |
| VV-031 | UC62 notification | ❌ Lỗi | R7 | 0 mail DN trong 177 mail MailHog. BUG-NOTIF-01 Open. |
| C8-1 | DON_VI scope ĐP/BN | ✅ Đạt | R7 | total=0 cho cross-donVi. |
| C8-2 | TW exception toàn quốc | ✅ Đạt | R7 | total=14 (13 TW + 1 STP-AG cross). |
| C8-3 | LICH_SU 18 enum | ❌ Lỗi | R7 | 10/18 enum (56%). BUG-LICHSU-01 Open. |
| W-Phase1 | Full lifecycle 7/8 transition | ✅ Đạt | R14 | DA_TIEP_NHAN→...→HOAN_THANH→DA_DANH_GIA. |
| W-Phase2a | Branch YEU_CAU_BO_SUNG | ✅ Đạt | R14 | VV-003 advance YCBS. |
| W-Phase2b | Branch TU_CHOI + mở lại | ✅ Đạt | R14 | VV-STP-AG-001 reopen + deadline reset. |
| W-Phase3 | Public toggle ON+OFF | ✅ Đạt | R14 | cong_khai flip 2 lần. |
| W-Phase4 | Regression smoke | ✅ Đạt | R14 | Search/Validation/Export/Permission/SLA 5/5. |
| **C5-1** | **CB_NV chấm điểm 3 tiêu chí 0-10** | **✅ Đạt** | **R15** | POST `/danh-gia` 201, diemTong=9 (AVG 8+9+10), VV-002 flip DA_DANH_GIA. |
| **C5-3** | **CB_PD KHÔNG được chấm** | **✅ Đạt** | **R15** | POST 403 ERR-PERM-SYS-00-01 (BE block). |
| **C5-4** | **Duplicate UNIQUE per loại** | **⚠️ Sai spec** | **R15** | Duplicate chặn qua state guard (ERR-STATE-VI-16-01) thay vì UNIQUE (ERR-DG-VV-04). Mechanism khác spec. |
| **C5-5** | **Validation thang 0-10** | **✅ Đạt** | **R15** | 11/-1/missing/string đều 422. Decimal accepted. |
| **C6-4** | **BR-CALC-04 lookup pre-check** | **⚠️ Sai spec** | **R15** | BE KHÔNG block DN thiếu fields. VV-002 tạo OK với default priority 3. Spec yêu cầu ERR-NH-03/warning, thực tế silent fallback. |

**Phụ:** Input field `diemTienDo` vs output `diemThoiGian` — naming inconsistency POST request body vs response (Minor observation, not bug). VV-001 fresh hôm nay lich-su dùng `TAO_VV` enum thay `CREATE` ✓.

### Bảng TC chưa chạy được — cần làm gì để chạy (R15)

Hiện tại còn 43 TC chưa chạy được — chia 3 nhóm: 24 chờ dev fix (NOTIF + LICHSU 8 enum) · 16 chờ env (VNeID T2 sandbox + DN T2 verified) · 3 cần seed backdated SLA.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| C1-1..6 | DN chưa có Tier 2 VNeID account verified | Infra setup VNeID T2 sandbox + DN T2 verified | Infra |
| C2-1..5 | Endpoint mail DN UC62 chưa hoạt động (BUG-NOTIF-01) | Dev BE fix UC62 trigger mail DN sau state transition | Dev BE |
| C3-1..3 | Pool VV chưa có deadline backdated 11/16/21 ngày | Seed VV với deadline custom (DB-level) hoặc time-travel | QA seed |
| C4-1..6 | Cần DN VNeID T2 để DN tự gửi YC | Same as C1 | Infra |
| C5-2 | DN cần VNeID T2 chấm điểm | Same as C1 | Infra |
| C6-2, C6-3 | DN session/MST lookup cần VNeID T2 | Same as C1 | Infra |
| C7-1..7 | LICH_SU 8 enum còn thiếu (TIEP_NHAN/CAP_NHAT_KQ/DANH_GIA/YEU_CAU_BO_SUNG/TU_CHOI*/PHAN_CONG_*) | Dev BE bổ sung 8 enum khi state transition | Dev BE |
| C8-3 (deep) | Verify đủ 18/18 enum xuất hiện | Same as C7 (BUG-LICHSU-01 fix) | Dev BE |
| R7.7.3-PRIVACY-1/2 | Cần VV cross-DN scope + DN test có VV | Run R7.4.A3 multi-DN test data | QA seed |

### Pool R15 update (snapshot 09:50:00)

```
Total VV = 20 (18 BTP-TW + 2 STP-AG)
States:
  DA_TIEP_NHAN: 5 (incl VV-BTP-TW-20260511-002 vừa tạo C6-4)
  YEU_CAU_BO_SUNG: 2
  DA_PHAN_CONG: 9
  HOAN_THANH: 0 (VV-002 flip → DA_DANH_GIA via C5-1)
  DA_DANH_GIA: 3 (VV-008/009 R14 sớm + VV-002 R15 C5-1)
  TU_CHOI: 1
```

### R15 evidence — screenshot index (`image/`)

| Screenshot | TC |
|---|---|
| [r15-c64-vv002-tao-thanh-cong-no-warning-2026-05-11.png](image/r15-c64-vv002-tao-thanh-cong-no-warning-2026-05-11.png) | C6-4 BE silent fallback |

API evidence (in-line):
- C5-1 POST: 201 `{diemChatLuong:8, diemThoiGian:9, diemThaiDo:10, diemTong:9, ngayDanhGia:'2026-05-11T02:45:43Z'}` + VV state `DA_DANH_GIA`
- C5-3 POST: 403 `{code:'ERR-PERM-SYS-00-01', message:'Forbidden'}` (cb_pd_tw_05)
- C5-4 POST duplicate: 409 `{code:'ERR-STATE-VI-16-01', message:'Vụ việc không ở trạng thái HOAN_THANH'}` (state guard, không phải UNIQUE)
- C5-5 validation: over_10/negative/missing/string đều 422 `ERR-VAL-SYS-00-01` với details `field, message`; decimal pass validation
- C6-4 POST VV: 201 → VV-BTP-TW-20260511-002 created với priority default 3, lich-su 1 entry `TAO_VV` ✓

---

## R14 Round (2026-05-10 21:30:00 → 21:45:00) — End-to-end lifecycle + 3 branches + regression

Tester: `cb_nv_tw_03` (CB NV) + `cb_pd_tw_05` (CB PD). Tool: Chrome DevTools MCP UI click chain. Scope user: 4 task — happy path, 2 branch, public toggle, regression smoke.

### Phase 1 — Happy path full lifecycle (VV-002)

| Transition | Trigger | Verdict | Network |
|---|---|:------:|---------|
| DA_TIEP_NHAN → DANG_KIEM_TRA | cb_nv_tw_01 click [Kiểm tra hồ sơ] (R13) | ✅ PASS | (R13 LICHSU `Kiểm tra` 17:13) |
| DANG_KIEM_TRA → DA_PHAN_CONG | cb_nv_tw_01 [Phân công] (R13) | ✅ PASS | (R13 LICHSU `Phân công` 20:21) |
| DA_PHAN_CONG → DANG_XU_LY | NHT [Xác nhận phân công] auto | ✅ PASS | (R13 LICHSU `XAC_NHAN_PHAN_CONG` 20:25 — new enum) |
| DANG_XU_LY → CHO_PHE_DUYET | cb_nv_tw_03 [Cập nhật kết quả] + [Trình phê duyệt] | ✅ PASS | POST `/cap-nhat-ket-qua` 201 + POST `/trinh-phe-duyet` 201 21:32 (LICHSU `TRINH_PD`) |
| CHO_PHE_DUYET → DA_DUYET | cb_pd_tw_05 [Phê duyệt] | ✅ PASS | POST `/phe-duyet` 201 21:33 (LICHSU `Phê duyệt`) |
| DA_DUYET → HOAN_THANH → DA_DANH_GIA | DN POST `/danh-gia` (R14 sớm verify DANHGIA-01) | ✅ PASS | POST `/danh-gia` 201 + auto SM HOAN_THANH→DA_DANH_GIA + diem 8.3 AVG |

→ 7/8 transition verified UI · DA_DANH_GIA endpoint verified độc lập (DANHGIA-01 retest closed).

### Phase 2a — Branch YEU_CAU_BO_SUNG (VV-003)

| Step | Trigger | Verdict | Network |
|---|---|:------:|---------|
| DA_TIEP_NHAN → DANG_KIEM_TRA | cb_nv_tw_03 [Kiểm tra hồ sơ] [Xác nhận] | ✅ PASS | POST `/kiem-tra` 201 21:36 |
| DANG_KIEM_TRA → YEU_CAU_BO_SUNG | cb_nv_tw_03 [Yêu cầu bổ sung] + Lý do | ✅ PASS | POST `/kiem-tra` 201 (verdict YCBS) — banner "Yêu cầu bổ sung — Yêu cầu doanh nghiệp bổ sung hồ sơ trước khi tiếp tục." |

DN respond side cần DN portal account (out of scope role test này — defer round sau với cấu hình DN VNeID).

### Phase 2b — Branch TU_CHOI + Mở lại hồ sơ (VV-STP-AG-20260509-001)

| Step | Trigger | Verdict | Network |
|---|---|:------:|---------|
| DA_TIEP_NHAN → DANG_KIEM_TRA | cb_nv_tw_03 [Kiểm tra hồ sơ] [Xác nhận] | ✅ PASS | POST `/kiem-tra` 201 21:37 |
| DANG_KIEM_TRA → TU_CHOI | cb_nv_tw_03 [Không đạt] + Lý do | ✅ PASS | POST `/kiem-tra` 201 (verdict TU_CHOI) — banner "Từ chối — Vụ việc đã bị từ chối — xem chi tiết trong dòng thời gian." |
| TU_CHOI → DA_TIEP_NHAN (mở lại) | cb_nv_tw_03 [Mở lại hồ sơ] + Lý do | ✅ PASS | POST `/mo-lai` 200 21:38 — deadline reset 02/06/2026 (15 ngày LV) — LICHSU `MO_LAI` enum mới |

### Phase 3 — Public CMS toggle (VV-002 DA_DUYET)

| Step | Trigger | Verdict | Network |
|---|---|:------:|---------|
| Toggle ON | cb_pd_tw_05 [Công khai] + Mô tả công khai | ✅ PASS | POST `/cong-khai` 200 21:34 — button đổi [Công khai] → [Hủy công khai] · LICHSU `CONG_KHAI` enum |
| Toggle OFF | cb_pd_tw_05 [Hủy công khai] | ✅ PASS | POST `/huy-cong-khai` 200 21:35 — button đổi lại [Công khai] |

### Phase 4 — Regression smoke (Search + Validation + Export + Permission + SLA)

| TC | Verdict | Note |
|---|:------:|------|
| **VV-002 R14 Search** | ✅ PASS | Keyword `VV-BTP-TW-20260510-002` → 1/1 match. Improvement vs R7 R8 (BUG-VV-FN-SEARCH-01 closed). |
| **VV-004 R14 Validation** | ✅ PASS | Empty form submit → 5 required errors: "Vui lòng chọn doanh nghiệp" + "Tiêu đề vụ việc là bắt buộc" + "Nội dung yêu cầu là bắt buộc" + "Lĩnh vực pháp luật là bắt buộc" + "Loại hình hỗ trợ là bắt buộc". DN field nay có required (improvement vs BUG-VV-FN-VALIDATION-01 closed). |
| **VV-024 R14 Export** | ✅ PASS | POST `/vu-viecs/export` 200 OK với keyword filter `?keyword=VV-BTP-TW-20260510-002`. |
| **C8-Permission R14** | ✅ PASS | cb_nv_tw_03 chỉ thấy [Cập nhật kết quả] + [Trình phê duyệt] ở DANG_XU_LY · cb_pd_tw_05 chỉ thấy [Phê duyệt] + [Từ chối] ở CHO_PHE_DUYET (separation of duty enforced). |
| **VV-022 R14 SLA** | ✅ PASS | All VV mới tạo deadline +14 ngày (15 ngày LV). VV mở lại auto-reset deadline +15 ngày từ ngày mở lại. BR-SLA-01 NĐ55/2019 Đ.8 K.1 enforced. |

### Pool R14 update (snapshot 21:45:00)

```
Total VV = 18 (17 BTP-TW + 1 STP-AG)
States:
  DA_TIEP_NHAN: 4 (incl VV-STP-AG mở lại 21:38)
  DANG_KIEM_TRA: 0
  DA_PHAN_CONG: 7
  DANG_XU_LY: 0
  CHO_PHE_DUYET: 0
  DA_DUYET: 1 (VV-002 sau Phase 1)
  HOAN_THANH: 0
  DA_DANH_GIA: 2 (VV-008/VV-009 từ R14 sớm)
  YEU_CAU_BO_SUNG: 2 (VV-509-002, VV-003 21:36)
  TU_CHOI: 1 (VV-507-004 R8)
```

### R14 evidence — screenshot index (`image/`)

| Screenshot | Phase |
|---|---|
| [r14-vv002-da-duyet-pd-tw-05-2026-05-10.png](image/r14-vv002-da-duyet-pd-tw-05-2026-05-10.png) | Phase 1 DA_DUYET reached |
| [r14-vv002-public-toggle-on-off-2026-05-10.png](image/r14-vv002-public-toggle-on-off-2026-05-10.png) | Phase 3 toggle ON+OFF |
| [r14-vv003-yeu-cau-bo-sung-2026-05-10.png](image/r14-vv003-yeu-cau-bo-sung-2026-05-10.png) | Phase 2a YCBS |
| [r14-vv001-tuchoi-molai-2026-05-10.png](image/r14-vv001-tuchoi-molai-2026-05-10.png) | Phase 2b TU_CHOI + mở lại |
| [r14-validation-empty-form-2026-05-10.png](image/r14-validation-empty-form-2026-05-10.png) | Phase 4 validation 5/5 |

---

# Lifecycle archive — older rounds

### Bug summary

→ Chi tiết 4 bug ở [bug-report-r7-7-3-functional-vu-viec.md](../../bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md):

| Bug ID | Severity | Title |
|--------|:--------:|-------|
| BUG-VV-FN-SEARCH-01 | Major | Search keyword `tuKhoa` BE ignore — trả full pool |
| BUG-VV-FN-VALIDATION-01 | Major | Form thiếu required validation cho DN — VV orphan |
| BUG-VV-FN-NOTIF-01 | Critical | UC62 violation — tạo VV không gửi mail |
| BUG-VV-FN-LICHSU-01 | Major | LICH_SU chỉ ghi 2 enum (CREATE/UPDATE), miss ~16 enum spec |

---

## Cluster 0 — Base TC (8 TC chạy)

| TC | Tên | Verdict | Note |
|----|-----|:------:|------|
| **VV-001** | List + filter trạng thái | ✅ PASS | Filter `trangThai=DA_PHAN_CONG` → 6 records · Tab "Đang xử lý" → 0 (no DANG_XU_LY) · Tab "Từ chối" → 0 (VV-003 reopened R9b). 3 observation (xem dưới). |
| **VV-002** | Search theo mã / tên DN / lĩnh vực | ⚠️ FAIL | BE ignore `tuKhoa` — trả full 11 records bất kể keyword. Filter LV/kênh/trạng thái OK. → BUG-VV-FN-SEARCH-01. |
| **VV-003** | Tạo VV nhập tay (kênh DIEN_THOAI) | ✅ PASS | VV-BTP-TW-20260509-007 tạo OK 13:17:00, deadline +14d (23/05). DN=DN-AG-003 (DNTN Hoàng Gia AG), LV=Doanh nghiệp, Loại hình=Tư vấn pháp luật. |
| **VV-004** | Tạo VV thiếu trường bắt buộc → validation | ⚠️ FAIL | 4 trường nội dung (Tiêu đề/Nội dung/LV/Loại hình) có required PASS. **DN field KHÔNG có validation** → VV-008 orphan tạo được không có doanhNghiepId. → BUG-VV-FN-VALIDATION-01. |
| **VV-022** | SLA 4 mức cảnh báo (BR-SLA-02) | ⚠️ Partial | 14/14 record = `BINH_THUONG`. 3 mức còn lại (CHU_Y / CANH_BAO / QUA_HAN) cần data deadline backdated — không có trong pool hiện tại. Verify mức 1 OK + enum exists. |
| **VV-024** | Xuất Excel danh sách VV | ✅ PASS | `POST /api/v1/vu-viecs/export` → 200, content-type `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, filename `vu-viec-export-1778307709776.xlsx`, blob 8052 bytes. |
| **VV-028** | QTHT view-only (BR-AUTH-01) | ⚠️ Partial | UI: ẩn "Nhập thủ công" + "Xuất Excel" + "Sửa" + Select all checkbox ✓. **BE: KHÔNG trả 403** cho POST/PATCH/DELETE (trả 422/409/500 do app errors), `POST /export` trả 200 — potential permission bypass. |
| **VV-031** | Notification kết quả tiếp nhận (UC62 + MailHog) | ❌ FAIL | Tạo VV-007 13:17:00 → MailHog 0 email "vụ việc" / "VV-BTP-TW". 10 mail gần nhất toàn reset password / hồ sơ TVV. → BUG-VV-FN-NOTIF-01. |

### VV-001 observations (chưa log bug — chờ deep review)

1. **List KHÔNG có cột `cong_khai` badge** — FR-V.I-NEW-05 spec yêu cầu hiển thị badge "Công khai" / "Riêng" trên list. Cần verify với BA xem có phải cần cột mới hay tooltip ẩn.
2. **Dropdown Trạng thái chỉ 10/12 enum** — thiếu `TU_CHOI` + `DA_DANH_GIA`. Cần verify với BA: filter chỉ cho 10 state có trong workflow active hay là bug.
3. **Tab "Đang xử lý" map single state DANG_XU_LY** — name suggests aggregate (DANG_KIEM_TRA + DA_PHAN_CONG + DANG_XU_LY) nhưng API filter `tab=DANG_XU_LY` chỉ map 1 state → 0 row hiển thị dù có 6 DA_PHAN_CONG + 3 DANG_KIEM_TRA. Potential bug name vs behavior mismatch.

---

## Cluster 8 — Permission/Audit (3 TC chạy)

| TC | Tên | Verdict | Note |
|----|-----|:------:|------|
| **C8-1** | BR-AUTH-03/04 DON_VI 2 tầng scope ĐP/BN | ✅ PASS | `cb_nv_dp_01 (AG)`: dashboard widget = 0 / API list `total=0` (KHÔNG thấy 13 BTP-TW). `cb_nv_bn_01 (BKH)`: dashboard widget = 0 / API list `total=0`. Scope filter active đúng. |
| **C8-2** | BR-AUTH-08 exception TW (toàn quốc) | ✅ PASS | Seed VV-STP-AG-20260509-001 qua `cb_nv_dp_01 (AG)` (donViId=00000000-0000-4000-8002-000000000006). `cb_nv_tw_03` re-list → `total=14` (13 BTP-TW + 1 STP-AG visible). TW exception cross-donVi active. |
| **C8-3** | LICH_SU_VU_VIEC ghi 18 hành động ENUM | ❌ FAIL | API `/lich-su` cả VV-002 (3 transition) + VV-006 (3 transition) đều chỉ trả 2 enum: `CREATE` + `UPDATE`. Distinct hanhDong = 2/18 (~11% coverage). → BUG-VV-FN-LICHSU-01. |

---

## TC chưa chạy (61 TC remaining)

Cluster 0 còn 25 TC base · Cluster 1-7 còn 36 TC mới. Phụ thuộc data:

| Cluster | TC chưa chạy | Phụ thuộc data còn thiếu |
|---|---|---|
| Cluster 0 (33 base, 8 chạy) | 25 TC còn | Cần ≥1 VV mỗi state lifecycle (PHAN_HOI / HOAN_THANH / DA_DUYET / DA_DANH_GIA) |
| Cluster 1 (DN flow VNeID) | toàn cluster | Cần DN VNeID Tier 2 sandbox (BLOCK upstream R7.4.A3-DN-BS) |
| Cluster 2 (Reopen) | toàn cluster | Pool có VV-003 reopened R9b ✓ — TESTABLE |
| Cluster 3 (SLA negative + counter) | toàn cluster | Cần data deadline backdated (BLOCK BE seed) |
| Cluster 4 (Phân công) | toàn cluster | TVV/CG/NHT pool đã có ✓ — TESTABLE |
| Cluster 5 (Cong khai PLQG) | toàn cluster | Cần VV `cong_khai=1` + state DA_DUYET (BLOCK upstream R7.4.A3-PUBLIC) |
| Cluster 6 (Notification + email) | toàn cluster | BLOCK chờ BUG-VV-FN-NOTIF-01 fix (UC62 chưa active) |
| Cluster 7 (Cross-module) | toàn cluster | DN/HoiDap/HopDong tab cross-link — TESTABLE phần |
| Cluster 8 (Permission, 3 TC chạy) | 0 TC còn | DONE |

**Đề xuất:** Cluster 2 (reopen) + Cluster 4 (phân công) + Cluster 7 (cross-module) testable ngay, ~12-15 TC.

---

## Round tiếp theo (2026-05-09 13:40:00) — 🚫 BLOCKED ENV DOWN

Tester resume Cluster 2/4/7 sau khi đóng Cluster 0+8 → **BE crash toàn bộ endpoint**. Probe:

| Endpoint | Method | Status |
|---|---|---|
| `/api/v1/auth/login` | POST | **500** |
| `/api/v1/auth/me` | GET | **500** |
| `/api/v1/danh-muc?loaiDanhMuc=LINH_VUC_PL` | GET | **500** |
| `/api/v1/vu-viecs?size=1` | GET | **500** |
| `/` (FE root) | GET | 200 |
| `:8025/api/v2/messages` (MailHog) | GET | 200 |

Console errors: `Failed to load resource: 500 (Internal Server Error)` ×2. Probe matrix sau 30s wait không recover. Phân loại Rule 9 = **ENV DOWN** — STOP, không retry, escalate infra.

**Evidence:** [r7-7-3-be-500-env-down-2026-05-09-1340.png](screenshots/r7-7-3-be-500-env-down-2026-05-09-1340.png)

61 TC còn (Cluster 2/4/7 + 25 base) defer round sau khi BE up lại.

---

## Round R8 (2026-05-09 17:00:00 → 17:15:00) — sau dev fix BE 500

Dev báo BE đã fix. Probe `POST /auth/login = 200` ✅, protected endpoints `401` (đúng — chưa login). Resume test với `cb_nv_tw_03`. JWT TTL ~2 phút (memory `qa_htpldn_jwt_revoke_aggressive`) → re-login giữa các TC.

| TC | Tên | Verdict | Note |
|----|-----|:------:|------|
| **VV-019** | DKT → TUCHOI yêu cầu lý do (BR-FLOW-04) | ✅ PASS | VV-507-004 SHTT chuyển DKT→TUCHOI 17:08. Empty submit → "Vui lòng nhập lý do". Submit "Sai HS" (6 char) → "Tối thiểu 10 ký tự" — **BR-FLOW-04 enforced**. Submit valid >10 char → state badge "Từ chối" + banner "Vụ việc đã bị từ chối" + nút [Mở lại hồ sơ] thay 3 action button. |
| **C3-1** | Modal phân công 2 thẻ Cá nhân + Tổ chức tư vấn | ✅ PASS | VV-005 click [Phân công] → modal "Phân công tư vấn viên" hiển thị field "Đối tượng xử lý" segmented control 2 radio: `Cá nhân` (default checked) + `Tổ chức tư vấn`. Field `loai_doi_tuong_xu_ly` ENUM('CA_NHAN','TO_CHUC') refactor thoả spec. |
| **C3-8** | Modal phân công KHÔNG còn dropdown "Địa bàn" | ✅ PASS | Modal phân công VV-005 chỉ có 3 field: Đối tượng xử lý radio + Chọn người được phân công combobox + Ghi chú textarea. **KHÔNG có dropdown "Địa bàn"** (NĐ77/2008 Đ.19 — TVV scope toàn quốc). Bỏ thoả Thay đổi 8. |
| **C7-6** | Dropdown phân công KHÔNG hiện TVV `loai_tvv='NHT'` | ✅ PASS | API probe `GET /api/v1/tu-van-viens?loaiTvv=NHT` → `total=0` (BE bỏ enum NHT khỏi TU_VAN_VIEN). API `loaiTvv=TVV` → 20, `loaiTvv=CG` → 15. NHT entries trong dropdown phân công đến từ NGUOI_HO_TRO entity (tách table riêng) đúng spec FR-04 Thay đổi 9. |
| **VV-025** | Upload `file_dinh_kem` formal | ⏰ Defer | Session JWT 2-phút revoke interfere upload multi-step flow. Defer round sau với account fresh + chunked upload test. |

**Pool change R8:**
- VV-507-004 SHTT: `DANG_KIEM_TRA` → `TU_CHOI` (R7.7.3 R8 17:08:00)
- VV-005 Đất đai: `DANG_KIEM_TRA` → `DA_PHAN_CONG` (advance ngoài QA scope — phát hiện khi navigate detail. TVV "Đào Thị NHT Hải Phòng" assigned `Chờ xác nhận` 09/05/2026 17:10. Có thể là dev seed manual hoặc auto-process khi BE restart fix 500.)
- TVV total: 18 → 20 (+2 mới — verify R8 API `loaiTvv=TVV total=20`)
- CG total: 14 → 15 (+1 mới)
- NHT (loaiTvv=NHT): 0 (spec compliance)

### Observation R8 — VV-005 state advance ngoài scope test

VV-005 ban đầu `DANG_KIEM_TRA` (per pool snapshot 13:30:00), sau BE 500 down → fix → re-login phát hiện state đã `DA_PHAN_CONG` với TVV-BTP-TW-0014 Vũ Văn Sáu? KHÔNG — actually shown "Đào Thị NHT Hải Phòng (NHT-STP-HP-0001)" assigned Chờ xác nhận. Cần BA verify auto-process / dev manual seed. Không log bug (chưa có evidence corruption).

---

## Pool state sau test (snapshot 13:30:00)

```
Total VV = 14 (13 BTP-TW + 1 STP-AG cross-donVi seed)
States:
  DA_TIEP_NHAN: 4 (VV-003, VV-007, VV-008 orphan, VV-STP-AG-001)
  DANG_KIEM_TRA: 3 (VV-005, VV-507-004, VV-507-006)
  DA_PHAN_CONG: 6 (VV-001, VV-004, VV-006, VV-507-001, VV-507-002, VV-507-005)
  YEU_CAU_BO_SUNG: 1 (VV-002)
  TU_CHOI: 0
  Other states (DANG_XU_LY/CHO_PHE_DUYET/DA_DUYET/HOAN_THANH/DA_DANH_GIA): 0

DonViId distribution:
  BTP-TW (00000000-0000-4000-8000-000000000001): 13
  STP-AG (00000000-0000-4000-8002-000000000006): 1
```

---

## Bằng chứng — screenshot index

| Screenshot | TC ref |
|------------|--------|
| [r7-7-3-vv-002-search-keyword-no-filter.png](screenshots/r7-7-3-vv-002-search-keyword-no-filter.png) | VV-002 search FAIL |
| [r7-7-3-vv-002-filter-lv-laodong-2-rows.png](screenshots/r7-7-3-vv-002-filter-lv-laodong-2-rows.png) | VV-002 filter LV WORK |
| [r7-7-3-vv-003-create-dien-thoai-success.png](screenshots/r7-7-3-vv-003-create-dien-thoai-success.png) | VV-003 PASS |
| [r7-7-3-vv-004-validation-empty-form.png](screenshots/r7-7-3-vv-004-validation-empty-form.png) | VV-004 4 error |
| [r7-7-3-vv-004-bug-no-dn-validation-still-creates.png](screenshots/r7-7-3-vv-004-bug-no-dn-validation-still-creates.png) | VV-004 DN no validation |
| [r7-7-3-vv-004-bug-vv008-detail-no-dn.png](screenshots/r7-7-3-vv-004-bug-vv008-detail-no-dn.png) | VV-008 orphan |
| [r7-7-3-vv-022-sla-mucdo-binhthuong-only.png](screenshots/r7-7-3-vv-022-sla-mucdo-binhthuong-only.png) | VV-022 SLA mức 1 only |
| [r7-7-3-vv-028-qtht-list-view-only.png](screenshots/r7-7-3-vv-028-qtht-list-view-only.png) | VV-028 QTHT UI view-only |
| [r7-7-3-c8-1-cb-nv-bn-bkh-zero-scope.png](screenshots/r7-7-3-c8-1-cb-nv-bn-bkh-zero-scope.png) | C8-1 BN scope=0 |
| [r7-7-3-c8-2-tw-cross-donvi-stp-ag-visible.png](screenshots/r7-7-3-c8-2-tw-cross-donvi-stp-ag-visible.png) | C8-2 TW thấy STP-AG |
| [r7-7-3-c8-3-lich-su-only-2-enum.png](screenshots/r7-7-3-c8-3-lich-su-only-2-enum.png) | C8-3 LICH_SU 2 enum |
| [r7-7-3-be-500-env-down-2026-05-09-1340.png](screenshots/r7-7-3-be-500-env-down-2026-05-09-1340.png) | BE 500 ENV DOWN evidence |
| [r7-7-3-vv-019-min-10-char-validation.png](screenshots/r7-7-3-vv-019-min-10-char-validation.png) | VV-019 R8 BR-FLOW-04 min 10 char |
| [r7-7-3-vv-019-tuchoi-success.png](screenshots/r7-7-3-vv-019-tuchoi-success.png) | VV-019 R8 DKT→TUCHOI PASS |
| [r7-7-3-c3-1-modal-phan-cong-2-the.png](screenshots/r7-7-3-c3-1-modal-phan-cong-2-the.png) | C3-1 R8 modal 2 thẻ Cá nhân/Tổ chức |
| [r7-7-3-c3-1-dropdown-cá-nhân-2-options.png](screenshots/r7-7-3-c3-1-dropdown-cá-nhân-2-options.png) | C3-1 R8 dropdown 2 options [TVV+NHT] |

---

*Functional report generated: 2026-05-09 13:30:00 | QA Automation via Claude Code*
*R8 update: 2026-05-09 17:15:00 — sau dev fix BE 500 — 4 TC mới PASS (VV-019/C3-1/C3-8/C7-6)*
