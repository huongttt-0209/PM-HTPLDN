# State snapshot — entity state count thực tế trên BE

**Last updated:** 2026-05-09 07:55:03 (R7.4.A1.6 R11 fresh TVV walk gate verify — tạo TVV-BTP-TW-0033 "TVV R11 A16 Gate Test" qua UI cb_nv_tw_02 → Gửi KQ thẩm định → Trình duyệt → cb_pd_tw_02 Phê duyệt → CHO_KICH_HOAT (TK auto-tạo aec7096d-394c-4f68-b514-2d4e96bf6adb username `tvv_r11_a16` ngayTao 2026-05-09T00:54:44.991Z) → click mail link đặt MK → HOAT_DONG; 4/4 TC PASS: TC1 TK creation timing đúng moment CKH, TC2 negative login pre-CKH 401 ERR-AUTH-LOGIN-01, TC3 mail fire đúng state CKH, TC4 dual-state TVV.HOAT_DONG ↔ TK.HOAT_DONG sync; BUG-005 mail link missing :3000 reproduce R11; TVV total 16→17, HOAT_DONG 2→3, MDK 6→6 (R7.2.5 batch 2 unchanged), TK 91→92, HOAT_DONG ≥37→≥38) · 2026-05-09 04:25:00 (R7.4.A1 R11 verify dev fix BUG-002 mail trigger — tạo TVV-BTP-TW-0032 "TVV R11 Verify Mail Fix" qua UI cb_nv_tw_02 → walk full lifecycle MDK→CPD→CHO_KICH_HOAT (cb_pd_tw_02 Phê duyệt + TK auto-tạo b7a05555-ebbb-4369-8b60-0354cdf0e100) → click mail link đặt MK → HOAT_DONG; mail fire đúng pattern link token SRS line 589 ✅ BUG-002 CLOSED + log NEW BUG-005 Minor mail link thiếu port :3000; TVV total 15→16, HOAT_DONG 1→2, CHO_KICH_HOAT 4 unchanged, TK 90→91) · 2026-05-09 02:42:30 (R7.7.4.6 TC TV functional 8/10 đạt + 2 bug — BUG-001 Critical QTHT bypass DELETE thành công xóa TC-0009; BUG-002 Minor FE thiếu cross-cấp gate; pool 9→8 HOAT_DONG do TC-0009 bị xóa; 1 record DP mới TC-STP-AG-0001 ở CHO_PHE_DUYET) · 2026-05-09 02:21:00 (R7.4.A6 SM-TCTV — 8 transition PASS UI MCP: TC-0009 mới qua 4 trans (MDK→CPD→TC→CPD→HD), TC-0008 round trip TAM_DUNG, TC-0007 round trip VO_HIEU_HOA; pool 8→9 HOAT_DONG, version=5 cho 3 record test; 0 bug) · 2026-05-09 02:10:00 (R7.2.3 R8 UI re-test — TC-0006/0007/0008 MOI→CPD→HOAT qua UI cb_nv_tw_02 + cb_pd_tw_02; phe-duyet reqid 179/186/192 + trinh-phe-duyet 181/188/194 200 OK; pool TC TV 5→8 HOAT_DONG; method gap đóng) · 2026-05-09 01:35:00 (R7.4.A1 R10 BUG-002 end-to-end re-walk — tạo TVV-BTP-TW-0031 "TVV R10 Test BUG-002 Mail" qua UI cb_nv_tw_02 → MOI_DANG_KY → Trình duyệt → CHO_PHE_DUYET → cb_pd_tw_02 Phê duyệt → CHO_KICH_HOAT; TK 89→90 auto-tạo a1e91b13-9212-4fa1-a204-928cc7cc814f; mail vẫn KHÔNG fire — BUG-002 reproduced fresh data; TVV total 14→15) · 2026-05-09 01:15 (R7.7.8c/d/e ✅ re-verify spot — FR-VIII-26 3 endpoints persist + cross R7.2.9b; FR-VIII-28 audit 1468 entries + filter combo + Export POST 200; FR-VIII-14 VAI_TRO 12 records BUG-VT-001 closed persist; R7.7.8b ⚠️ re-verify Self-reg DN form structure + MST 13 inline error — BUG-FR22-001a + 002 closed persist; TC04 email trùng defer R8 do BE captcha invisible + rate-limit; R7.7.8a ✅ re-verify 6 tabs SCR-VIII-08 + BE counter reset post-unlock; TK pool 89 records HOAT_DONG:37/CHO_KICH_HOAT:52; BUG-TK-SM-002/003 vẫn Closed-verified persist; R7.5.5 ✅ Audit log 1468 entries / 20 action / 15 entity / 10+ user — vượt 14.68× ngưỡng ≥100; R7.2.9b NHT_04_UI full E2E mail flow ✅ — verify-email → forgot-password → reset-password form UI → login → sidebar SCR-IV-NHT 3 menu + URL force redirect; CG dinh_14 sidebar SCR-IV-CG 2 menu + URL force ×2 ✅; R7.2.9 re-verify 6 CG batch 1 + 3 NHT all HOAT_DONG, login probe dinh_14 fresh ✅ TK persist active; R7.1.6 re-verify 9 DM còn lại — DM2 CHUONG_TRINH_HT 2→3 sau R8 seed CT_HTPLDN qua API workaround; R7.1.5 re-verify NGAY_LE pool 4→5 sau API workaround Tết NĐ; R7.1.4 re-verify SLA 4 records; R7.1.2 re-verify DM LOAI_DOANH_NGHIEP 5 records; R7.1.3 re-verify DON_VI 84 records; R7.2.1 ✅ MPH seed 3→12 cover 6 LV × 2; R7.1.1 re-verify post BUG-DM-LVPL-001 close — DM master `LINH_VUC_PL` 10 LV SRS) · 2026-05-09 18:10 (R7.2.4 R8 verify pool drift 36→23 + seed 2 DN gap fill VUA×CN: DN-BGG-0001 5600000018 Vạn Lộc BG + Phú Cường BN 5700000029, pool 23→25, 9/9 combo cover) · 2026-05-09 00:38 (R7.4.A1 R9 BUG-002 verify — TVV-0016 CHO_PHE_DUYET → CHO_KICH_HOAT sau Phê duyệt cb_pd_tw_02; TK 88→89 auto-tạo cca7d919; mail KHÔNG fire — BUG-002 regressed; TVV/CG total 28 unchanged scope) · **Account verify:** cb_nv_tw_01/02 + cb_nv_bn_01/02 + cb_nv_dp_02/03 + cb_pd_tw_02 + qtht_01/02 (qtht_02 OTP bypass anomaly 2026-05-08) · **MCP:** chrome-devtools `list_network_requests` + `evaluate_script` + curl

**Audit 2026-05-08:** 6 seed task ✅ (R7.2.4/R7.3.1/R7.3.2/R7.3.7/R7.3.8/R7.4.D1) reviewed — claim historical đúng tại thời điểm done. State drift hiện tại do workflow advance/cleanup downstream → markers downstream đã reflect đúng (R7.4.B5b/R7.4.D2/R7.7.10). KHÔNG flip ✅ → ⚠️ (vi phạm historical truth principle).
**Purpose:** Single source of truth state count → drive `(✓ N)` / `(✗ N)` markers trong [todo.md](todo.md) `[need: ...]` bracket.

## Cách dùng

1. Sau MỌI task ✅/⚠️ thay đổi state entity X → re-run verify query của X (cột "Verify").
2. Update count + state distribution + timestamp.
3. Grep `todo.md` `[need: ... <X> ...]` → đổi marker theo count mới (`(✓ N)` nếu thoả, `(✗ ...)` nếu thiếu).
4. Edit todo.md với marker mới → hook `auto-rescan-todo.py` tự flip ⏳→🟢 nếu dep đủ.
5. Workflow chi tiết trong [CLAUDE.md §State marker workflow](../CLAUDE.md).

---

## Bảng state thực tế (2026-05-07)

| Entity | Endpoint | Total | State distribution | Verify command (MCP/curl) |
|---|---|:-:|---|---|
| Hỏi đáp (HD) | `/api/v1/hoi-daps` | **7** | MOI:2 (HD-003/-007), DA_PHAN_CONG:3 (HD-001/-002/-006), HUY:2 (HD-004/-005) | `curl ".../hoi-daps?page=0&size=20"` |
| Vụ việc (VV) | `/api/v1/vu-viecs` | **5** | DA_TIEP_NHAN:1, DA_PHAN_CONG:3, DANG_KIEM_TRA:1 (re-verify 2026-05-08 18:42 UI MCP) | `curl ".../vu-viecs?page=1&pageSize=100"` |
| TVCS | `/api/v1/noi-dung-tu-van-cs` | **12** | TIEP_NHAN:5, PHAN_CONG:6, HUY:1 | `.../noi-dung-tu-van-cs?size=100` |
| Biểu mẫu (BM record) | `/api/v1/bieu-maus` | **0** | rỗng | `.../bieu-maus?size=100` |
| Thư mục BM | `/api/v1/thu-muc-bieu-maus` | **2** | NHAP:2 (Thuế, HĐ Lao động) | `.../thu-muc-bieu-maus` |
| MPH (Mẫu phản hồi) | `/api/v1/mau-phan-hois` | **12** | KICH_HOAT:12 cover 6 LV × 2 (DN/TM/LĐ/Thuế/SHTT/Đất đai) — 6 TW + 3 BN (BKH/BTC/BCT) + 3 DP (AG/BG/BNI). R8 seed +9 mẫu 2026-05-08 23:11 sau R7.1.1 close. | `.../mau-phan-hois?size=50` |
| TVV (loaiTvv=TVV) | `/api/v1/tu-van-viens?loaiTvv=TVV` | **17** | MOI_DANG_KY:6 (R7.2.5 batch 2 TVV-0017..0022), CHO_PHE_DUYET:0, TU_CHOI:3, HOAT_DONG:3 (vu_sau_06 = TVV-0014 + R11 TVV-0032 + R7.4.A1.6 R11 TVV-0033 sau first-login HOAT_DONG), CHO_KICH_HOAT:4 (Hoàng Văn Năm + Nguyễn Văn Tư Vấn + PD Batch Test 1 R7-7-2/TVV-0016 + R10 TVV-0031 9338c73e), YEU_CAU_BO_SUNG:1 (re-verify 2026-05-09 07:55:03 UI sau R7.4.A1.6 R11 walk TVV-0033 advance MDK→HOAT_DONG +1 HD) | `.../tu-van-viens?loaiTvv=TVV&pageSize=100` |
| CG (loaiTvv=CG) | `/api/v1/tu-van-viens?loaiTvv=CG` | **14** | HOAT_DONG:8 (incl. 6 batch 1 R7.2.9 ly_13..ho_18 — re-verify 2026-05-09 still active sau >2 ngày, login probe dinh_14 fresh ✅), MOI_DANG_KY:6 (R7.2.6 batch 2 CG-0023..0028 cover 6 LV DN/TM/LĐ/SHTT/ĐĐ/Thuế) | `.../tu-van-viens?loaiTvv=CG&size=100` |
| TC TV | `/api/v1/to-chuc-tu-vans` | **9** | HOAT_DONG:8 (TC-0001..0008 — TC-0009 đã bị BUG-001 R7.7.4.6 QTHT DELETE 2026-05-09 02:42), CHO_PHE_DUYET:1 (TC-STP-AG-0001 do cb_nv_dp_01 tạo R7.7.4.6 TC-002, blocked TC-010 cross-cấp 403). Total 9 records (8 TW HOAT_DONG + 1 DP CHO_PHE_DUYET). | `.../to-chuc-tu-vans` |
| DN | `/api/v1/doanh-nghieps` | **25** | byQuyMo: VUA:8/SIEU_NHO:10/NHO:7 · byNganh: CONG_NGHIEP:9/NONG_LAM:8/THUONG_MAI:8 · 9/9 combo cover (VUA×CN gap fill 0→2 R8 2026-05-09 self-reg DN-BGG-0001 + Phú Cường BN MST 5700000029) | `.../doanh-nghieps?size=100` |
| **DON_VI (Cơ quan đơn vị)** | `/api/v1/don-vi` | **84** | HOAT_DONG:84 (1 TW=BTP-TW + 20 BN incl. BKH/BTC/BCT/BNN/BGTVT/BXD/BTNMT/BTTTT/BGDDT/BYT/... + 63 DP incl. STP-AG/BG/BNI/HN/HCM/DN/HP/CT/...). 7 đơn vị bắt buộc R7.1.3 ✅ (re-verify 2026-05-08 23:25). | `.../don-vi?pageSize=100` |
| **DM LOAI_DOANH_NGHIEP** | `/api/v1/danh-muc?loaiDanhMuc=LOAI_DOANH_NGHIEP` | **5** | KICH_HOAT:5 (TNHH/CP/DNTN/HKD fixture + CTHD_TEST). Old quy_mo (DN_SIEU_NHO/NHO/VUA) đã được dev tách sang DM riêng theo Phương án A — BUG-LOAI-DN-002 closed R7 2026-05-07. R7.1.2 ✅ (re-verify 2026-05-08 23:30). | `.../danh-muc?loaiDanhMuc=LOAI_DOANH_NGHIEP&pageSize=100` |
| **Cấu hình SLA** | `/api/v1/cau-hinh/sla` | **4** | active:4 (HOI_DAP=10d / HO_SO_HT=15d / HO_SO_TT=10d / VU_VIEC=10d, cảnh báo 50/90%, hệ số 2.0, email+app=true). R7.1.4 ✅ (re-verify 2026-05-08 23:35). | `.../cau-hinh/sla` |
| **NGAY_LE 2026** | `/api/v1/ngay-le?nam=2026` | **5** | NGAY_LE:5 (Tết DL 01/01 + Tết NĐ 17/02 + 30/4 + 1/5 + Quốc khánh 02/09). R7.1.5 ⚠️ partial — pool reset từ 15→4, R8 lần 6 seed Tết NĐ qua API workaround (BUG-NGAY-LE-001 FE [Đồng ý] silent fail vẫn Open lần 6/6 sau dev fix lần 4). Re-verify 2026-05-08 23:38. | `.../ngay-le?nam=2026` |
| **DM 9 còn lại R7.1.6** | `/api/v1/danh-muc?loaiDanhMuc={DM}` | **9 DM × ≥3 record = 50 total** | DM1 LOAI_HINH_HT:6 / DM2 CHUONG_TRINH_HT:3 (sau R8 seed +CT_HTPLDN) / DM3 TINH_TRANG_VV:12 / DM4 HO_SO_DE_NGHI_HT:4 / DM5 HO_SO_DE_NGHI_TT:4 / DM6 TIEU_CHI_DG_HIEU_QUA:3 / DM7 TIEU_CHI_DG_CHI_PHI:3 / DM8 LOAI_HINH_TIEP_NHAN:5 / DM9 KENH_TIEP_NHAN:4. All KICH_HOAT. R7.1.6 ✅ 9/9 (re-verify 2026-05-08 23:52). | `.../danh-muc?loaiDanhMuc=<DM>&pageSize=100` |
| **Audit log** | `/api/v1/audit-logs` | **1468** | 20 action (CREATE 406 / LOGIN 293 / UPDATE 87 / THAM_DINH 58 / LOGOUT 51 / SUBMIT 33 / APPROVE 29 / PHE_DUYET 28 / DELETE 21 / PHAN_CONG 11 / TIEP_NHAN 11 / PUBLISH+UNPUBLISH 20 / ACTIVATE 8 / PASSWORD_CHANGE 8 / etc.) × 15 entityType (TAI_KHOAN:743 / TVV:139 / CHUONG_TRINH_HTPL:65 / DOT_BAO_CAO:48 / HO_SO_CHI_TRA:34 / HSPL_DN:29 / NHT:28 / etc.) × 10+ user (cb_nv_tw_02:457 / cb_nv_tw_01:253 / qtht_02:146 / cb_nv_dp_01:81 / qtht_03:76 / etc.). R7.5.5 ✅ verify 2026-05-09 00:38. | `.../audit-logs?page=N&pageSize=100` |
| KH năm | `/api/v1/ke-hoach-dao-taos` | **4** | NHAP:3 (KH-0004 TW + KH-0005 BN + KH-0006 DP — R8 2026-05-08), CHO_DUYET:1 (KH-0001 TW — R7) | `.../ke-hoach-dao-taos` |
| CTĐT | `/api/v1/chuong-trinh-dao-taos` | **0** | rỗng (endpoint OK) | `.../chuong-trinh-dao-taos` |
| Khóa học | `/api/v1/khoa-hocs` | **0** | rỗng | `.../khoa-hocs` |
| NHCH | `/api/v1/ngan-hang-cau-hois` | **6** | KICH_HOAT:6 (cover 5 LV: Hành chính/Lao động/Đất đai/SHTT/Thuế · 3 mức độ · 3 loại — R8 2026-05-08 19:35) | `.../ngan-hang-cau-hois` |
| ĐKT | `/api/v1/de-kiem-tras` | **4** | NHAP:4 (cover 4 LV: Hành chính/Lao động/Đất đai/Thuế — sau R7.4.B10 CRUD R8 xóa SHTT). Đất đai version=2 thoiGianLamBai=45 (edited). | `.../de-kiem-tras` |
| HSCT (Chi trả) | `/api/v1/ho-so-chi-tras` | **78** | DANG_THAM_DINH:13, DA_DUYET:8, DA_THANH_TOAN:14, DANG_DANH_GIA:4, CHO_TIEP_NHAN:8, YEU_CAU_BO_SUNG:6, CHO_PHE_DUYET:9, TU_CHOI_THANH_TOAN:3, TU_CHOI:3, DANG_KIEM_TRA:8, HUY:2 | `.../ho-so-chi-tras?size=200` |
| HĐ TV | `/api/v1/hop-dong-tu-vans` | **0** | rỗng | `.../hop-dong-tu-vans` |
| Giảng viên | `/api/v1/giang-viens` | **8** | DANG_HOAT_DONG:8 | `.../giang-viens` |
| Bài giảng | `/api/v1/bai-giangs` | **8** | active (BG không state machine — chỉ có `congKhai` boolean): VIDEO:5 + SLIDE:1 + PDF:2 cover 7 LV (Doanh nghiệp/Dân sự/Hành chính/Lao động/SHTT/Thuế/Đất đai). R8 2026-05-08 20:50. | `.../bai-giangs` |
| NHT | `/api/v1/nguoi-ho-tro` | **12** | CHO_KICH_HOAT:7 (NHT-BTP-TW-0002..0004 + NHT-BKH-0001 + NHT-BTC-0001 + NHT-STP-BG-0001 + NHT-STP-BNI-0001), HOAT_DONG:4 (nht_01/02/03 STP-AG/DN/HP + NHT-BTP-TW-0005 sau R7.7.4.5 NHT-012 khôi phục VHH→HOAT_DONG; nht_04_ui NHT-BTP-TW-0001 R7.2.9b activate full E2E mail flow 2026-05-09: verify-email + forgot-password + reset-password form UI + login + sidebar SCR-IV-NHT 3 menu), TAM_DUNG:1 (NHT-BTP-TW-0001 sau R7.7.4.5 NHT-009 HOAT_DONG→TAM_DUNG). Re-verify 2026-05-09 18:30 sau R7.7.4.5 R8 (NHT-006 LV update BTP-TW-0002 + NHT-009/010/012 state machine) | `.../nguoi-ho-tro?size=100` |
| TAI_KHOAN (TK) | `/api/v1/tai-khoan` (admin scope qtht_01) | **92** | HOAT_DONG: ≥38 (cb/qtht/admin/nht_01..03/6 CG batch 1 + 2 Probe + vu_sau_06 + R11 tvv_0032 + R7.4.A1.6 R11 tvv_r11_a16 cho TVV-0033 sau first-login 2026-05-09T00:56:35.336Z + …), CHO_KICH_HOAT: ≥54 (Hoàng Văn Năm + Nguyễn Văn Tư Vấn + PD Batch Test 1 R9 cca7d919 + R10 TVV-0031 a1e91b13-9212-4fa1-a204-928cc7cc814f + 2 Probe leftover + 8 NHT + 7 _04 + 28 _05..08 hot-role qtht_03 UI), MDK pool 12 (6 TVV + 6 CG batch 2) = **0 TK** (đúng FR-VIII-15) — total 92 sau R7.4.A1.6 R11 (TK aec7096d cho TVV-0033 + first-login HOAT_DONG verify 2026-05-09 07:55:03). SCR-VIII-08 6 tabs render đúng (R7.7.8a ✅ re-verify 2026-05-09 00:55). BUG-TK-SM-002/003 closed-verified persist (BE counter reset OK + tab Vô hiệu hóa visible). | UI `/quan-tri/tai-khoan` qtht_01 + `evaluate_script` page through `j.meta.totalPages` |
| Kho QA | `/api/v1/kho-cau-hois` | **14** | NHAP:2, CHO_DUYET:1 (QA-0508-0004 Đất đai), DA_DUYET:9 (+QA-0508-0005 **Hành chính** B1 ✅ 2026-05-08), HET_HIEU_LUC:2 | `.../kho-cau-hois?size=100` |
| Phiên TV nhanh | `/api/v1/tu-van-nhanhs` | **50** | MOI:8, DANG_TIM_KIEM:6+, DA_GOI_Y:5+ (sau R7.B2 -1), CB_TRA_LOI:1 (TVN-0019 ✅ R7.B2 T4) | `.../tu-van-nhanhs?size=100` |
| CT HTPLDN | `/api/v1/chuong-trinh-htpls` | **3** | DA_DUYET:1, DU_THAO:1, HUY:1 | `.../chuong-trinh-htpls` |
| Đợt Đánh giá | `/api/v1/ke-hoach-danh-gias` | **≥1** | CHO_DUYET_PC:1 (DG-20260506-0001 sau R7.4.D2 R7) — needs live re-verify | `.../ke-hoach-danh-gias` |
| Học viên | (404) | N/A | endpoint chưa deploy | — |
| Lịch học | (404/500) | N/A | endpoint chưa deploy | — |
| **DM LINH_VUC_PL** | `/api/v1/danh-muc?loaiDanhMuc=LINH_VUC_PL` | **10** | KICH_HOAT:10 (THUE/LAO_DONG/DAT_DAI/DAN_SU/**THUONG_MAI**/HINH_SU/HANH_CHINH/SHTT/**DOANH_NGHIEP**/**DAU_TU**) — match SRS line 204 100%; FE dropdown filter MPH sync 10 LV (re-verify 2026-05-08 22:55 sau BUG-DM-LVPL-001 R8 lần 4 close) | UI `/quan-tri/danh-muc/LINH_VUC_PL` table 10 mục + `/quan-tri/cau-hinh?tab=mau-phan-hoi` filter "Lĩnh vực PL" dropdown 10 options |

---

## Filter coverage (cho dep yêu cầu per-LV / per-state)

| Filter group | Coverage | Note |
|---|---|---|
| **DM LINH_VUC_PL match SRS** | **10/10** (Thuế/Lao động/Đất đai/Dân sự/**Thương mại**/Hình sự/Hành chính/SHTT/**Doanh nghiệp**/**Đầu tư**) | ✅ R7.1.1 re-verify 2026-05-08 22:55 sau BUG-DM-LVPL-001 R8 lần 4 close. Bỏ 3 non-SRS (HON_NHAN_GIA_DINH/KINH_DOANH_TM/KHIEU_NAI_TO_CAO), thêm THUONG_MAI. Cascade unblock R7.2.1 (12 MPH cover 6 LV × 2). |
| Kho QA `state=DA_DUYET hieu_luc=1` per LV | **6/7** (DN/SHTT/Đất đai/Lao động/Thuế/**Hành chính** ✅ B1) | Thiếu KDTM (chưa seed bao giờ). Đủ proceed B2 R7.6.2 với 6 LV chính. |
| NHCH `KICH_HOAT` per LV (R7.3.9 dep) | **5/5** (Hành chính + Lao động + Đất đai + SHTT + Thuế) | ✅ R8 2026-05-08 — Lao động ×2, các LV khác ×1. Đủ proceed R7.3.9 seed ĐKT. |
| Kho QA `state=DA_DUYET` count | **9** | Đủ ≥1 cho 6/7 LV |
| TVCS state distribution | 3 state (TIEP_NHAN/PHAN_CONG/HUY) | Đủ ≥10 record cho R7.7.5 functional 44 TC |
| CT HTPLDN state distribution | 3 state (DA_DUYET/DU_THAO/HUY) | Đủ ≥3 cho R7.7.15 functional 42 TC |
| NHT HOAT_DONG count | **4** | Đủ ≥3 cho R7.4.A3 workflow VV. CHO_KICH_HOAT:8 sẵn sàng activate qua mail flow (verified 2026-05-09 — workaround host → IP, BE consume token OK) |
| TC TV HOAT_DONG count | **9** | Đủ ≥1 cho R7.4.A3 workflow VV. R7.4.A6 add TC-0009 + round trip 0007/0008 về HOAT_DONG. |

---

## Re-verify checklist sau mỗi task ✅

Task ảnh hưởng entity X → re-run query X → update bảng + downstream marker:

| Task type ✅ | Re-verify entity |
|---|---|
| Seed (R7.2.x / R7.3.x) | Entity vừa seed + entity FK reference |
| Workflow advance (R7.4.x) | Entity vừa advance state + downstream consumer |
| Functional CRUD (R7.7.x) | Entity bị CRUD + audit log |
| Tier 0 DM (R7.1.x) | DM table + entity dùng FK đến DM đó |

Nếu count thay đổi → grep `[need: .*<entity>` trong todo.md → flip marker `(✗ N)` ↔ `(✓ N)`.
