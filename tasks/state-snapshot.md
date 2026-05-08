# State snapshot — entity state count thực tế trên BE

**Last updated:** 2026-05-09 00:38 (R7.5.5 ✅ Audit log 1468 entries / 20 action / 15 entity / 10+ user — vượt 14.68× ngưỡng ≥100; R7.2.9b NHT_04_UI full E2E mail flow ✅ — verify-email → forgot-password → reset-password form UI → login → sidebar SCR-IV-NHT 3 menu + URL force redirect; CG dinh_14 sidebar SCR-IV-CG 2 menu + URL force ×2 ✅; TVV blocked R7.4.A1 BUG-002; R7.2.9 re-verify 6 CG batch 1 + 3 NHT all HOAT_DONG, login probe dinh_14 fresh ✅ TK persist active; R7.1.6 re-verify 9 DM còn lại — DM2 CHUONG_TRINH_HT 2→3 sau R8 seed CT_HTPLDN qua API workaround [Antd DatePicker programmatic setter chưa fire React onChange]; R7.1.5 re-verify NGAY_LE pool 4→5 sau API workaround Tết NĐ — BUG-NGAY-LE-001 FE silent fail vẫn Open lần 6/6; R7.1.4 re-verify SLA 4 records — HOI_DAP/HO_SO_HT/HO_SO_TT/VU_VIEC, cảnh báo 50/90%, hệ số 2.0; R7.1.2 re-verify DM LOAI_DOANH_NGHIEP 5 records — 4 fixture + CTHD_TEST KICH_HOAT, BUG-LOAI-DN-002 closed; R7.1.3 re-verify DON_VI 84 records — 7 đơn vị bắt buộc HOAT_DONG; R7.2.1 ✅ MPH seed 3→12 cover 6 LV × 2 sau R7.1.1 unblock; R7.1.1 re-verify post BUG-DM-LVPL-001 close — Layer 1 DM master `LINH_VUC_PL` 10 LV SRS + Layer 2 dropdown MPH sync 10 LV; pre-existing snapshot R7.3.10 R8 BG seed — 5 VIDEO → 8 (5 VIDEO + 1 SLIDE + 2 PDF) cover 7 LV; R7.2.7 R8 retry seed +5 NHT qua UI `/nguoi-ho-tro` — pool 4→11, CHO_KICH_HOAT:8 cover BTP-TW + BKH + BTC + STP-BG + STP-BNI, LV DN/Thuế/LĐ/SHTT) · **Account verify:** cb_nv_tw_01/02 + cb_nv_bn_01/02 + cb_nv_dp_02/03 + cb_pd_tw_02 + qtht_02 · **MCP:** chrome-devtools `list_network_requests` + `evaluate_script` + curl

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
| TVV (loaiTvv=TVV) | `/api/v1/tu-van-viens?loaiTvv=TVV` | **14** | MOI_DANG_KY:6 (R7.2.5 batch 2 TVV-0017..0022), CHO_PHE_DUYET:1, TU_CHOI:3, HOAT_DONG:1, CHO_KICH_HOAT:2, YEU_CAU_BO_SUNG:1 (re-verify 2026-05-08 UI tab MDK) | `.../tu-van-viens?loaiTvv=TVV&pageSize=100` |
| CG (loaiTvv=CG) | `/api/v1/tu-van-viens?loaiTvv=CG` | **14** | HOAT_DONG:8 (incl. 6 batch 1 R7.2.9 ly_13..ho_18 — re-verify 2026-05-09 still active sau >2 ngày, login probe dinh_14 fresh ✅), MOI_DANG_KY:6 (R7.2.6 batch 2 CG-0023..0028 cover 6 LV DN/TM/LĐ/SHTT/ĐĐ/Thuế) | `.../tu-van-viens?loaiTvv=CG&size=100` |
| TC TV | `/api/v1/to-chuc-tu-vans` | **5** | HOAT_DONG:5 | `.../to-chuc-tu-vans` |
| DN | `/api/v1/doanh-nghieps` | **23** | (mixed) | `.../doanh-nghieps?size=100` |
| **DON_VI (Cơ quan đơn vị)** | `/api/v1/don-vi` | **84** | HOAT_DONG:84 (1 TW=BTP-TW + 20 BN incl. BKH/BTC/BCT/BNN/BGTVT/BXD/BTNMT/BTTTT/BGDDT/BYT/... + 63 DP incl. STP-AG/BG/BNI/HN/HCM/DN/HP/CT/...). 7 đơn vị bắt buộc R7.1.3 ✅ (re-verify 2026-05-08 23:25). | `.../don-vi?pageSize=100` |
| **DM LOAI_DOANH_NGHIEP** | `/api/v1/danh-muc?loaiDanhMuc=LOAI_DOANH_NGHIEP` | **5** | KICH_HOAT:5 (TNHH/CP/DNTN/HKD fixture + CTHD_TEST). Old quy_mo (DN_SIEU_NHO/NHO/VUA) đã được dev tách sang DM riêng theo Phương án A — BUG-LOAI-DN-002 closed R7 2026-05-07. R7.1.2 ✅ (re-verify 2026-05-08 23:30). | `.../danh-muc?loaiDanhMuc=LOAI_DOANH_NGHIEP&pageSize=100` |
| **Cấu hình SLA** | `/api/v1/cau-hinh/sla` | **4** | active:4 (HOI_DAP=10d / HO_SO_HT=15d / HO_SO_TT=10d / VU_VIEC=10d, cảnh báo 50/90%, hệ số 2.0, email+app=true). R7.1.4 ✅ (re-verify 2026-05-08 23:35). | `.../cau-hinh/sla` |
| **NGAY_LE 2026** | `/api/v1/ngay-le?nam=2026` | **5** | NGAY_LE:5 (Tết DL 01/01 + Tết NĐ 17/02 + 30/4 + 1/5 + Quốc khánh 02/09). R7.1.5 ⚠️ partial — pool reset từ 15→4, R8 lần 6 seed Tết NĐ qua API workaround (BUG-NGAY-LE-001 FE [Đồng ý] silent fail vẫn Open lần 6/6 sau dev fix lần 4). Re-verify 2026-05-08 23:38. | `.../ngay-le?nam=2026` |
| **DM 9 còn lại R7.1.6** | `/api/v1/danh-muc?loaiDanhMuc={DM}` | **9 DM × ≥3 record = 50 total** | DM1 LOAI_HINH_HT:6 / DM2 CHUONG_TRINH_HT:3 (sau R8 seed +CT_HTPLDN) / DM3 TINH_TRANG_VV:12 / DM4 HO_SO_DE_NGHI_HT:4 / DM5 HO_SO_DE_NGHI_TT:4 / DM6 TIEU_CHI_DG_HIEU_QUA:3 / DM7 TIEU_CHI_DG_CHI_PHI:3 / DM8 LOAI_HINH_TIEP_NHAN:5 / DM9 KENH_TIEP_NHAN:4. All KICH_HOAT. R7.1.6 ✅ 9/9 (re-verify 2026-05-08 23:52). | `.../danh-muc?loaiDanhMuc=<DM>&pageSize=100` |
| **Audit log R7.5.5** | `/api/v1/audit-logs` | **1468** | 20 action (CREATE 406 / LOGIN 293 / UPDATE 87 / THAM_DINH 58 / LOGOUT 51 / SUBMIT 33 / APPROVE 29 / PHE_DUYET 28 / DELETE 21 / PHAN_CONG 11 / TIEP_NHAN 11 / PUBLISH+UNPUBLISH 20 / ACTIVATE 8 / PASSWORD_CHANGE 8 / etc.) × 15 entityType (TAI_KHOAN:743 / TVV:139 / CHUONG_TRINH_HTPL:65 / DOT_BAO_CAO:48 / HO_SO_CHI_TRA:34 / HSPL_DN:29 / NHT:28 / etc.) × 10+ user (cb_nv_tw_02:457 / cb_nv_tw_01:253 / qtht_02:146 / cb_nv_dp_01:81 / qtht_03:76 / etc.). R7.5.5 ✅ verify 2026-05-09 00:38. | `.../audit-logs?page=N&pageSize=100` |
| KH năm | `/api/v1/ke-hoach-dao-taos` | **4** | NHAP:3 (KH-0004 TW + KH-0005 BN + KH-0006 DP — R8 2026-05-08), CHO_DUYET:1 (KH-0001 TW — R7) | `.../ke-hoach-dao-taos` |
| CTĐT | `/api/v1/chuong-trinh-dao-taos` | **0** | rỗng (endpoint OK) | `.../chuong-trinh-dao-taos` |
| Khóa học | `/api/v1/khoa-hocs` | **0** | rỗng | `.../khoa-hocs` |
| NHCH | `/api/v1/ngan-hang-cau-hois` | **6** | KICH_HOAT:6 (cover 5 LV: Hành chính/Lao động/Đất đai/SHTT/Thuế · 3 mức độ · 3 loại — R8 2026-05-08 19:35) | `.../ngan-hang-cau-hois` |
| ĐKT | `/api/v1/de-kiem-tras` | **4** | NHAP:4 (cover 4 LV: Hành chính/Lao động/Đất đai/Thuế — sau R7.4.B10 CRUD R8 xóa SHTT). Đất đai version=2 thoiGianLamBai=45 (edited). | `.../de-kiem-tras` |
| HSCT (Chi trả) | `/api/v1/ho-so-chi-tras` | **78** | DANG_THAM_DINH:13, DA_DUYET:8, DA_THANH_TOAN:14, DANG_DANH_GIA:4, CHO_TIEP_NHAN:8, YEU_CAU_BO_SUNG:6, CHO_PHE_DUYET:9, TU_CHOI_THANH_TOAN:3, TU_CHOI:3, DANG_KIEM_TRA:8, HUY:2 | `.../ho-so-chi-tras?size=200` |
| HĐ TV | `/api/v1/hop-dong-tu-vans` | **0** | rỗng | `.../hop-dong-tu-vans` |
| Giảng viên | `/api/v1/giang-viens` | **8** | DANG_HOAT_DONG:8 | `.../giang-viens` |
| Bài giảng | `/api/v1/bai-giangs` | **8** | active (BG không state machine — chỉ có `congKhai` boolean): VIDEO:5 + SLIDE:1 + PDF:2 cover 7 LV (Doanh nghiệp/Dân sự/Hành chính/Lao động/SHTT/Thuế/Đất đai). R8 2026-05-08 20:50. | `.../bai-giangs` |
| NHT | `/api/v1/nguoi-ho-tro` | **12** | CHO_KICH_HOAT:8, HOAT_DONG:4 (nht_01/02/03 STP-AG/DN/HP + nht_04_ui NHT-BTP-TW-0001 R7.2.9b activate full E2E mail flow 2026-05-09: verify-email + forgot-password + reset-password form UI + login + sidebar SCR-IV-NHT 3 menu) | `.../nguoi-ho-tro?size=100` |
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
| NHT HOAT_DONG count | **3** | Đủ ≥3 cho R7.4.A3 workflow VV. CHO_KICH_HOAT:8 sẵn sàng activate (R7.2.9 mail flow) |
| TC TV HOAT_DONG count | **5** | Đủ ≥1 cho R7.4.A3 workflow VV |

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
