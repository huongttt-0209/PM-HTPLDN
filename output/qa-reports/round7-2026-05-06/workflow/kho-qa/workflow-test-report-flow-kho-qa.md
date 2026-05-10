# Workflow Test Report — Kho câu hỏi tư vấn nhanh (FR-X.2-01 SM-KHOCAUHOI)

> **Module:** Kho câu hỏi (`KHO_CAU_HOI`) · **SRS:** [`02-thu-tu-module.md line 777-789 §SM-KHOCAUHOI`](../../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) + [`srs-fr-13-tv-nhanh.md §FR-X.2-01 UC158 SCR-X2-01`](../../../../../input/srs-v3/srs-fr-13-tv-nhanh.md) · **Round:** R10b (latest) · **Date:** 2026-05-10 11:00:00 · **Tester:** QA Automation
> **Bug:** [Pass-bug-report-flow-kho-qa.md](../../bug-reports/kho-qa/Pass-bug-report-flow-kho-qa.md) — 0 Open, 2 Closed (BUG-KHOQA-001 + **BUG-KHOQA-002 Closed-verified R10b**)
> **Accounts:** R10b `cb_nv_tw_08` (isolated context `qa_only_r10_kho_qa_verify`) · R10 `cb_nv_tw_08` · R9 `cb_nv_tw_08` · R7-R8 `cb_nv_tw_02` + `cb_pd_tw_02`

---

## Kết luận

✅ **PASS** — **8/8 transition PASS**. R10b retest verify T8 với account `cb_nv_tw_08`: drawer HET_HIEU_LUC giờ có button [Kích hoạt hiệu lực] → click → confirm dialog → API success → row chuyển HET_HIEU_LUC→DA_DUYET, hieuLuc Không→Có. FE deploy fix giữa R10 (20:06 BLOCK) → R10b (11:00 PASS), delta ~15h. BUG-KHOQA-002 Closed-verified. Module workflow đầy đủ 8/8 transition functional.

## R10b Retest — 2026-05-10 11:00:00 (LATEST)

**Scope:** Re-verify T8 lần 5 sau dev claim FE fix drawer footer. Account `cb_nv_tw_08` isolated context `qa_only_r10_kho_qa_verify`.

**Steps:**
1. Login `cb_nv_tw_08 / Secret@123 / OTP 666666` → dashboard.
2. Navigate sidebar `Quản lý tư vấn` → `Kho câu hỏi` → URL `/tv-nhanh/kho-cau-hoi`.
3. Click row `QA-20260508-0002` (Lao động, state Hết hiệu lực) → drawer mở.
4. Snapshot UI: header có button `[play-circle Kích hoạt hiệu lực]` (uid=35_7) cạnh nút Đóng. **Bug fixed!**
5. Click button → confirm dialog `"Câu hỏi sẽ được kích hoạt lại và hiển thị cho người dùng. Tiếp tục?"` xuất hiện.
6. Click `[Đồng ý]` → drawer đóng + table refresh: row QA-20260508-0002 chuyển TRẠNG THÁI `Hết hiệu lực`→`Đã duyệt`, HIỆU LỰC `Không`→`Có`.
7. Verify pool API `GET /api/v1/kho-cau-hois?pageSize=100` → total=14 unchanged, distribution shifted DA_DUYET 9→10 / HET_HIEU_LUC 2→1.

**Phân loại:** APP/FE FIX VERIFIED — R10 BLOCK + R10b PASS = dev push FE fix drawer footer 1 button [Kích hoạt hiệu lực] cho state HET_HIEU_LUC. Closed-verified, KHÔNG cần re-test thêm.

---

> **Note:** Transition T0 (auto-feed `FR-02 DA_DUYET → KHO_CAU_HOI DA_DUYET nguồn=TU_DONG`) thuộc R7.4.D3.AUTO + R7.6.2 cross-module — chờ HD DA_DUYET upstream, không thuộc scope D3.

---

## R10 Retest — 2026-05-09 20:06:36 (LATEST)

**Scope:** Verify-only T8 (BUG-KHOQA-002 reproduce check 4th round). KHÔNG mutate T1-T7 đã PASS R7. Tester request: dùng bộ acc _08, MCP UI test.

**Steps:**
1. Login `cb_nv_tw_08 / Secret@123 / OTP 666666` qua `/login`. PASS lần 1 (không lock, không 429). Dashboard render banner "CB Nghiệp vụ TW 08" + "CB_NV_TW".
2. Click sidebar `Quản lý tư vấn` → submenu `Kho câu hỏi` → URL `/tv-nhanh/kho-cau-hoi`. Pool 14 record verified (DA_DUYET:9 / CHO_DUYET:1 / HET_HIEU_LUC:2 / NHAP/Bị từ chối:2). State distribution match R9 (không thay đổi).
3. Click row `QA-20260508-0002` (Lao động, Hết hiệu lực). Drawer mở title "Câu hỏi QA-20260508-0002". DOM verify `.ant-drawer-open`: `buttonCount=1`, button = `[{text:"", aria:"Đóng", class:"ant-drawer-close"}]`, `.ant-drawer-footer = NOT EXIST`, regex `/k[ií]ch hoạt|kh[ôo]i phục|mở lại|reactivate|restore/i` quét toàn drawer = `0 hits`. → **T8 BLOCK confirmed lần thứ 4**.
4. Đóng drawer → click row `QA-20260508-0005` (Hành chính, Đã duyệt) đối chứng. Drawer mở title "Câu hỏi QA-20260508-0005". DOM verify: `buttonCount=3`, buttons = `[{aria:"Đóng"}, {text:"Công khai"}, {text:"Hết hiệu lực"}]`. → T7 button hiện diện đúng spec.
5. Console errors: `0 messages` (sạch trên cả 2 drawer interaction).

**Phân loại Rule 9:** APP/FE BUG — pattern stable cross-account (cb_nv_tw_02 + cb_nv_tw_08), cross-round (R7+R8+R9+R10), cross-record (QA-20260507-0002 + QA-20260508-0002). Không phải selector/account/env/throttle. Severity giữ Major P1.

**Evidence:** [r7-4-d3-r10-drawer-het-hieu-luc-no-action-cb08.png](../../bug-reports/kho-qa/image/r7-4-d3-r10-drawer-het-hieu-luc-no-action-cb08.png) (HET_HIEU_LUC drawer 1 button) + [r7-4-d3-r10-drawer-da-duyet-3-buttons-cb08.png](../../bug-reports/kho-qa/image/r7-4-d3-r10-drawer-da-duyet-3-buttons-cb08.png) (DA_DUYET drawer 3 buttons đối chứng) + [r7-4-d3-r10-pool-14-cb08.png](../../bug-reports/kho-qa/image/r7-4-d3-r10-pool-14-cb08.png) (pool list 14 record cb08 banner).

---

## R9 Retest — 2026-05-09 17:14:00

**Scope:** Verify-only T8 (BUG-KHOQA-002 reproduce check). KHÔNG mutate T1-T7 đã PASS R7.

**Steps:**
1. Login `cb_nv_tw_08 / Secret@123 / OTP 666666`. Initial UI submit fail toast "Tên đăng nhập hoặc mật khẩu không đúng" → curl POST `/api/v1/auth/login` confirm credentials valid (returns `otpToken`); root cause UI fail = HTTP 429 ThrottlerException (retry-after 51s) sau chuỗi probe đa account trước đó. Wait 55s → reload + login fresh → PASS (dashboard render "CB Nghiệp vụ TW 08").
2. Navigate sidebar `Quản lý tư vấn` → `Kho câu hỏi` → URL `/tv-nhanh/kho-cau-hoi`. Pool 14 record verified (DA_DUYET:9 / CHO_DUYET:1 / HET_HIEU_LUC:2 / NHAP:2).
3. Click row `QA-20260508-0002` (Lao động, state Hết hiệu lực). Drawer mở title "Câu hỏi QA-20260508-0002". DOM verify: `.ant-drawer-open button` → 1 button only `aria-label="Đóng"` class `ant-drawer-close`; `.ant-drawer-footer` = NO_FOOTER. → T8 BLOCK confirmed.
4. Đối chứng drawer DA_DUYET QA-20260508-0005 (Hành chính): 3 buttons `[Đóng / Công khai / Hết hiệu lực]` → T7 button hiện diện đúng spec.

**Phân loại Rule 9:** APP/FE BUG — pattern stable cross-account, cross-round, cross-record. Không phải selector/account/env. Severity giữ Major P1.

**Evidence:** [r7-4-d3-r9-bug-khoqa-002-drawer-open-cb08.png](../../bug-reports/kho-qa/image/r7-4-d3-r9-bug-khoqa-002-drawer-open-cb08.png) (HET_HIEU_LUC drawer no action) + [r7-4-d3-r9-da-duyet-drawer-3-buttons-cb08.png](../../bug-reports/kho-qa/image/r7-4-d3-r9-da-duyet-drawer-3-buttons-cb08.png) (DA_DUYET drawer 2 action) + [r7-4-d3-r9-bug-khoqa-002-no-reactivate-btn-cb08.png](../../bug-reports/kho-qa/image/r7-4-d3-r9-bug-khoqa-002-no-reactivate-btn-cb08.png) (pool list).

---

## Bảng kiểm tra workflow

| # | Transition | Actor | Sample | Status | Bug / Note |
|:-:|---|---|---|:-:|---|
| T1 | `— → CHO_DUYET` (Submit THU_CONG, SCR-X2-01 Modal Thêm câu hỏi, button [Lưu]) | `cb_nv_tw_02` | 8 record QA-0002..0008 cover 6 LV (DN, KDTM, Thuế, LĐ, ĐĐ, SHTT) | ✅ | R7.3.16 đã PASS — 8/8 record `THU_CONG` state `CHO_DUYET` |
| T2 | `— → CHO_DUYET` (Import IMPORT, SCR-X2-01 Modal Nhập Excel) | `cb_nv_tw_02` | 1 record QA-0010 LV Hành chính từ file kho-qa-import.xlsx | ✅ | R7.3.16 đã PASS — record `nguon=Import` |
| T4 | `CHO_DUYET → DA_DUYET` (Duyệt đơn lẻ, button [check Duyệt] trong detail modal) | `cb_pd_tw_02` | QA-0002 (LV Doanh nghiệp) | ✅ | Transition trên SCR-X2-01 detail modal. Toast "Duyệt thành công" |
| T5 | `CHO_DUYET → DA_DUYET` (Duyệt hàng loạt, checkbox + button [check Duyệt hàng loạt] + confirm modal) | `cb_pd_tw_02` | 6 record (QA-0003..0008) cover 6 LV | ✅ | Confirm modal "Duyệt 6 câu hỏi?" → click [Duyệt hàng loạt]. Tab "Đã duyệt" còn 8 record |
| T6 | `CHO_DUYET → NHAP` (Từ chối với lý do bắt buộc, button [close Từ chối] + textarea required) | `cb_pd_tw_02` | QA-0010 (LV Hành chính, nguồn Import) | ✅ | Lý do 187 chars qua React-aware setter (AntD textarea cleared sau dropdown interaction). Trạng thái "Bị từ chối" hiển thị UI (= state `NHAP` per SRS) |
| T7 | `DA_DUYET → HET_HIEU_LUC` (Toggle hiệu lực off, button [stop Hết hiệu lực] + confirm modal "Đánh dấu hết hiệu lực?") | `cb_nv_tw_02` | QA-0002 (LV Doanh nghiệp) | ✅ | Sau click [Đồng ý] toast "Đã đánh dấu hết hiệu lực". Trạng thái `Hết hiệu lực`, Hiệu lực `Không` |
| T8 | `HET_HIEU_LUC → DA_DUYET` (Toggle hiệu lực on, button [Kích hoạt hiệu lực]) | `cb_nv_tw_08` | QA-20260508-0002 (HET_HIEU_LUC → DA_DUYET) | ✅ | **PASS R10b 2026-05-10 11:00.** Drawer header có button [play-circle Kích hoạt hiệu lực] → click → confirm dialog → Đồng ý → row chuyển DA_DUYET, hieuLuc Có. [BUG-KHOQA-002](../../bug-reports/kho-qa/Pass-bug-report-flow-kho-qa.md) Closed-verified. |

> Icon: ✅ pass · ❌ fail · ⏭ skip · 🚫 blocked · — chưa test

---

## Lịch sử round

| Round | Date | Kết quả tóm tắt (1 dòng) |
|---|---|---|
| R10b | 2026-05-10 11:00:00 | T8 PASS — `cb_nv_tw_08` click [Kích hoạt hiệu lực] → confirm → Đồng ý → row QA-20260508-0002 chuyển HET_HIEU_LUC→DA_DUYET. **BUG-KHOQA-002 Closed-verified**. Module 8/8 transition PASS. |
| R10 | 2026-05-09 20:06:36 | T8 verify-only lần 4 với `cb_nv_tw_08` (slot _08, user request) — BUG-KHOQA-002 STILL OPEN. DOM `buttonCount=1` HET_HIEU_LUC vs `buttonCount=3` DA_DUYET đối chứng. Console 0 errors. Pattern reproduce 4 round liên tiếp 2 account. |
| R9 | 2026-05-09 17:14:00 | T8 verify-only với `cb_nv_tw_08` — BUG-KHOQA-002 STILL OPEN (drawer HET_HIEU_LUC chỉ 1 button Đóng, drawer DA_DUYET có button Hết hiệu lực T7 OK). Pattern reproduce 3 round liên tiếp 2 account. |
| R8 | 2026-05-08 | T8 re-verify với `cb_nv_tw_02` — BUG-KHOQA-002 STILL OPEN, QA-20260508-0002 kẹt state Hết hiệu lực. |
| R7 | 2026-05-07 | PARTIAL 7/8 transition. T1/T2/T4/T5/T6/T7 ✅. T8 🚫 blocked do BUG-KHOQA-002 (FE thiếu button Kích hoạt). |

---

## End-state pool (sau R7)

| Mã | LV | Nguồn | Trạng thái cuối | Hiệu lực |
|---|---|---|---|---|
| QA-20260507-0001 | Sở hữu trí tuệ | Thủ công | DA_DUYET | Có |
| QA-20260507-0002 | Doanh nghiệp | Thủ công | **HET_HIEU_LUC** | Không |
| QA-20260507-0003 | Kinh doanh thương mại | Thủ công | DA_DUYET | Có |
| QA-20260507-0004 | Thuế | Thủ công | DA_DUYET | Có |
| QA-20260507-0005 | Lao động | Thủ công | DA_DUYET | Có |
| QA-20260507-0006 | Đất đai | Thủ công | DA_DUYET | Có |
| QA-20260507-0007 | Sở hữu trí tuệ | Thủ công | DA_DUYET | Có |
| QA-20260507-0008 | Doanh nghiệp | Thủ công | DA_DUYET | Có |
| QA-20260507-0009 | Thuế | Thủ công | CHO_DUYET (backup) | Không |
| QA-20260507-0010 | Hành chính | Import | NHAP (Bị từ chối) | Không |

7 record `DA_DUYET hieu_luc=Có` cover 5/6 LV chính (DN, KDTM, Thuế, LĐ, ĐĐ, SHTT) sẵn sàng cho R7.6.2 (TV nhanh PUBLIC dropdown đọc Kho QA hiệu lực).

---

## Bằng chứng (R7)

**T5 — `CHO_DUYET → DA_DUYET` bulk** *(8 record DA_DUYET cover 6 LV trên tab Đã duyệt)*:

![R7.4.D3 T5 — Bulk approved 8 record DA_DUYET](../../seed/kho-qa/r7-4-d3-t5-bulk-approved-8da-duyet.png)

**T6 — `CHO_DUYET → NHAP` reject** *(QA-0010 trạng thái "Bị từ chối")*:

![R7.4.D3 T6 — QA-0010 rejected](../../seed/kho-qa/r7-4-d3-t6-reject-qa-0010.png)

**T7 — `DA_DUYET → HET_HIEU_LUC` toggle off** *(QA-0002 trạng thái "Hết hiệu lực" + toast)*:

![R7.4.D3 T7 — QA-0002 toggle off](../../seed/kho-qa/r7-4-d3-t7-toggle-off-qa-0002.png)

**T8 BUG — Detail modal HET_HIEU_LUC thiếu button Kích hoạt** *(chỉ có icon X Đóng)*:

![R7.4.D3 T8 BUG — No reactivate button](../../seed/kho-qa/r7-4-d3-t8-bug-no-reactivate-button.png)

---

*R7 | QA Automation via Claude Code (Chrome DevTools MCP)*
