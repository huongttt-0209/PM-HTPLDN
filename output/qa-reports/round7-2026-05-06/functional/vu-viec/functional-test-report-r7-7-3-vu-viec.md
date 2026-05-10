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

⚠️ **PARTIAL PASS — 15/72 TC chạy (21%) — 9 PASS, 4 FAIL Major/Critical, 2 Partial.** (R7+R8 cộng dồn)

Pool VV: 14 records (13 BTP-TW + 1 STP-AG seed cross-donVi 13:27).

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
