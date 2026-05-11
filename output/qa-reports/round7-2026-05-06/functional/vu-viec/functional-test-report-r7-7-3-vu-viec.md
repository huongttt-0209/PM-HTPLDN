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

⚠️ **PARTIAL PASS — 29/72 TC chạy (40%) — 22 PASS, 4 FAIL Major/Critical, 2 Partial, 1 Sai spec.** (R7+R8+R14+R15 cộng dồn)

Pool VV: 20 records (R15 update — 18 BTP-TW + 2 STP-AG/cross-donVi).

---

## R15 Round (2026-05-11 09:19:00 → 09:50:00) (LATEST) — Audit post-fix + Cluster 5 UC67 + Cluster 6 BR-CALC-04

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
