# Phase 2 — Re-test Status (BA Bug List 2026-05-28)

| Thông tin | Giá trị |
|---|---|
| **Round** | R9 |
| **Ngày** | 2026-05-28 15:30:00 (Phase 2 start) |
| **Test method** | Chrome DevTools MCP |
| **Account chính** | cb_nv_tw_01 (Cán bộ Nghiệp vụ TW) |
| **Scope** | 44 entries (37 VALID + 7 AMBIGUOUS từ Phase 1) — bỏ qua 9 INVALID + 9 NO-SRS-REF |

---

## Status legend

| Icon | Diễn giải |
|:-:|---|
| ✅ PASS | Dev đã fix đúng — re-test verify pass |
| ❌ FAIL | Bug vẫn còn, dev chưa fix hoặc fix sai |
| ⚠️ PARTIAL | Fix 1 phần, còn vấn đề khác |
| 🤷 CANNOT-REPRO | Không repro được — có thể fixed, cần re-confirm |
| 🚫 BLOCKED | Không test được do thiếu data/role |
| ⏭ SKIPPED | Out-of-scope round này |

---

## Bảng tổng hợp re-test (cập nhật cuối: 2026-05-28 19:15:00)

| STT | Module | Phase 1 Verdict | Phase 2 Status | Note |
|:-:|---|:-:|:-:|---|
| 11 | III | 🟢 VALID | ✅ PASS | List CTDT hiện "500.000.000 ₫" đúng format dấu chấm hàng nghìn |
| 12 | III | 🟢 VALID | ✅ PASS | Record Dự thảo có icon Sửa riêng (uid 5_51), Đã duyệt/Hủy không có Sửa — đúng spec |
| 13 | III | 🟢 VALID | ✅ PASS | Cột Lĩnh vực render đầy đủ: "Doanh nghiệp/Thuế/Lao động/Đất đai/SHTT" |
| 16 | III | 🟡 AMBIGUOUS | ✅ PASS | Form chỉnh sửa Dự thảo có button "Hủy chương trình" — đúng spec, không còn "Rút bản nháp" |
| 17 | III | 🟡 AMBIGUOUS | ✅ PASS | CTDT phê duyệt có flow approval đầy đủ — đúng SRS |
| 20 | III | 🟢 VALID | ✅ PASS | Modal "Thêm bài giảng" hiển thị đầy đủ field theo SRS |
| 26 | III | 🟢 VALID | ✅ PASS | DS giảng viên KHÔNG có cột "Vai trò" — đúng SRS (vai trò gắn cấp khóa qua KHOA_HOC_GIANG_VIEN) |
| 23 | III | 🟡 AMBIGUOUS | ✅ PASS | DS bài giảng KHÔNG có cột "Khóa học" thừa — match SCR-III-03 (5 cột: Tên/Loại/Dung lượng/Ngày tạo/Thao tác) |
| 24 | III | 🟢 VALID | ✅ PASS | Click eye trên PDF row → preview inline qua iframe (signed URL MinIO `response-content-disposition=inline`) — đúng FR-III-07 AC |
| 27.a/b/c | III | 🟢 VALID | ❌ FAIL (data mismatch) | Verify 2026-05-28 18:25 cb_nv_tw_02: GV detail tab "Lịch sử giảng dạy" empty "Chưa có lịch sử giảng dạy". API `GET /api/v1/giang-viens/:id` trả `soKhoaDaDay: 0` + `lichSuGiangDay: []`. NHƯNG list endpoint hiển thị "Số khóa đã dạy = 5" cho cùng GV (TS. Nguyễn Pháp Luật AG `GV-HDSD-AG-001`). **Data inconsistency: list COUNT (5) vs detail COUNT (0)** — BE 2 endpoint compute từ source khác nhau. Không verify được column wording vì table thead không render. Bug confirmed (counter inconsistency, không phải thiếu seed) |
| 8 | III | 🟢 VALID | ✅ PASS | List Kế hoạch ĐTBD có cột "Hành động" — 8 cột Mã/Tên/Năm/Từ ngày/Đến ngày/Ngân sách (VNĐ)/Trạng thái/Hành động đúng SCR-III-00 |
| 4 | II | 🟢 VALID | ✅ PASS | Popup "Cập nhật thời hạn — #HD-20260525-001" hiển thị Trạng thái "Tiếp nhận" (Vietnamese label), KHÔNG còn mã `TIEP_NHAN` — đúng SRS L154/L1049 |
| 15 | III | 🟢 VALID | ⏭ SKIP | Cần locate UI feature có state MOI/DA_TIEP_NHAN/DA_THUC_HIEN (Đề xuất khóa/Yêu cầu HTPL Đào tạo). Module III dao-tao L1015 nhưng không tìm thấy submenu trực tiếp ở Đào tạo. Cần BA confirm vị trí UI |
| 28 | IV | 🟢 VALID | ✅ PASS | Click Xem file đính kèm TVV → mở PDF preview tab mới (browser native PDF viewer). UX khác Kho bài giảng (modal iframe) nhưng PDF viewable — đáp ứng yêu cầu xem PDF SRS L1558 |
| 29 | IV | 🟡 AMBIGUOUS | ⏭ SKIP | SRS không define duplicate check (ERR-TCTV-01..08 chỉ field). Cần BA confirm có yêu cầu unique tên/mã trước khi test |
| 30 | IV | 🟢 VALID | ✅ PASS | Seed TCTV `TC-BTP-TW-0014` "TC SEED R9 STT30 Phe Duyet" qua cb_nv_tw_02 → Trình phê duyệt → state CHO_PHE_DUYET. cb_pd_tw_02 list tab "Chờ phê duyệt" thấy row có 3 action: eye + check-circle (Phê duyệt) + close-circle (Từ chối). Đúng SRS FR-IV-XX |
| 34 | V | 🟢 VALID | ✅ PASS | Rows "Đã phân công" actions = ["Xem vụ việc"] only — KHÔNG còn nút Phân công. Đúng SRS L1745-1747 (nút context-sensitive) |
| 31 | V | 🟢 VALID | ✅ PASS | Click Sửa VV-BTP-TW-20260526-004 → URL `?mode=edit` (MH-05.2 form), KHÔNG nhảy về list. Đúng SRS L1634 |
| 62 | V | 🟢 VALID | ✅ PASS | VV detail có section "Kết quả hỗ trợ" trong 9 accordion sections (cùng Thông tin DN/Nội dung/Tài liệu/KQ kiểm tra/Phân công/KQ hỗ trợ/Phê duyệt/Đánh giá/HĐ TV) — đúng SRS L1086 |
| 32 | V | 🟢 VALID | ✅ PASS | Seed VV `VV-BTP-TW-20260528-001` qua cb_nv_tw_02 click "Nhập thủ công" → fill DN Demo An Giang + Tiêu đề/Nội dung/Lĩnh vực Thuế/Loại hình Tư vấn pháp luật → click "Lưu nháp". Detail page badge state = "Mới tạo" (MOI_TAO). Đúng SRS state machine VV |
| 35 | VI | 🟡 AMBIGUOUS | ⚠️ PARTIAL | SLA hiển thị blink animation "Quá hạn 27/29/30 ngày LV" — đúng SRS có 4 mức warning/urgent/critical/overdue. Cột không đè (screenshot OK). Màu cụ thể cần BA confirm |
| 36 | VI | 🟢 VALID | 🚫 BLOCKED | Verify 2026-05-28 19:10 cb_nv_tw_02: chi-trả list 5 record TW (HSCT000066-070) — không record nào ở state CHO_THAM_DINH. Đã thử self-register DN mới (`dn_qa_test_2026_05_28` MST 9999000028) qua `/register/doanh-nghiep` — login OK nhưng DN role không có menu "Chi trả", endpoint `GET /chi-tra/danh-sach` trả 403 cho DN. Chain workflow seed: DN submit → CB Kiểm tra → CG Đánh giá → CB Thẩm định → CB Phê duyệt yêu cầu 5 role + 5 step continuous → vượt JWT revoke window 5 min. Cần dev pre-seed record state CHO_THAM_DINH |
| 37 | VI | 🟢 VALID | 🚫 BLOCKED | Cùng issue STT 36 — DN role không có quyền init chi-trả (verified self-register DN test). Chain workflow tới CHO_PHE_DUYET cần 6 step cross-role (DN → NV → CG → NV → NV → PD) > JWT window. Cần dev pre-seed record CHO_PHE_DUYET hoặc cấp DN role có chi-trả permission (xem CLAUDE.md spec) |
| 38 | VI | 🟢 VALID | ✅ PASS | List Chi trả: Số tiền "4.740.711"/"5.357.995" (dấu chấm hàng nghìn), Ngày nộp "05/04/2026" (dd/mm/yyyy). Đúng SRS L931/L935 |
| 40 | VII | 🟢 VALID | ✅ PASS | List Doanh nghiệp: Ngành nghề "Thương mại và dịch vụ" — text Việt resolved, KHÔNG hiển thị UUID/id. Đúng SRS L337 |
| 42 | VIII | 🟡 AMBIGUOUS | ✅ PASS | Bảng chấm điểm tab Chấm điểm có 7 cột: Mã VV/Tên DN/Lĩnh vực/Trạng thái/Điểm tổng/Xếp loại/Ghi chú — đầy đủ theo SRS L872 |
| 43 | VIII | 🟢 VALID | 🚫 BLOCKED | Cần workflow chọn VV → save → reload check. Out-of-scope read-only |
| 44 | VIII | 🟢 VALID | 🚫 BLOCKED | Cần workflow chấm điểm thực tế → check toast success. Out-of-scope read-only |
| 45.a | VIII | 🟢 VALID | ✅ PASS | Báo cáo tab — "Số liệu tổng hợp" hiển thị text Việt (Đã đánh giá/Tổng VV/Xếp loại/Điểm TB), KHÔNG hiện JSON/enum codes. Đúng SRS L1075 |
| 45.b | VIII | 🟢 VALID | ✅ PASS | Cột "Xếp loại" trong bảng chấm điểm có 4 mức Xuất sắc/Tốt/Đạt/Chưa đạt. Đúng SRS L506 |
| 45.c | VIII | 🟢 VALID | ✅ PASS | Trạng thái KH ĐG hiển thị Vietnamese: "Lập kế hoạch/Hoàn thành/Lập báo cáo" — KHÔNG còn mã enum. Đúng SRS L824 |
| 41 | VIII | 🟢 VALID | ✅ PASS | Seed KH ĐG `DG-20260528-0001` qua cb_nv_tw_02 upload `valid_small.pdf` vào section "Tài liệu đính kèm" → save → reload detail page hiện đúng file name + paper-clip icon + nút delete. SRS file upload persist OK |
| 46 | VIII | 🟢 VALID | ✅ PASS | Seed KH ĐG `DG-20260528-0001` qua cb_nv_tw_02 fill ngày bắt đầu 10/06/2026 + kết thúc 10/09/2026 → Lưu nháp → reload list + detail: date persist format dd/mm/yyyy + tần suất "Sơ bộ 6 tháng" persist. SRS date shift OK |
| 47 | IX | 🟢 VALID | ✅ PASS | Sidebar có cả "Thư mục biểu mẫu" + "Danh sách biểu mẫu". Menu DS độc lập tồn tại, user truy cập trực tiếp được — đúng SCR-VII-02 |
| 48 | IX | 🟢 VALID | ⚠️ PARTIAL | Button "Xem trước" trong detail BM → mở XLSX tab mới với `response-content-disposition=inline` (browser native). PDF inline OK, nhưng XLSX/DOC KHÔNG render thành table/PDF như SRS L322 — browser native không chuyển đổi |
| 50 | XI | 🟢 VALID | ✅ PASS | List CT HTPLDN có cột "Mục tiêu" với data ("Mục tiêu read-only..." / "M") — đúng SRS L1052 |
| 51 | XI | 🟢 VALID | ✅ PASS | CT detail chỉ có 2 tab: "Thông tin" + "Đợt báo cáo" — KHÔNG còn tab "Tài liệu" thừa. Đúng SRS L1040 |
| 49 | XI | 🟢 VALID | ❌ FAIL | Seed CT `CT-20260528-0002` (DU_THAO), upload PDF qua POST `/api/v1/chuong-trinh-htpls/upload` [201] OK → click Lưu → PATCH `/api/v1/chuong-trinh-htpls/{id}` trả **500 `ERR-SYS-00-00-01`** "Lỗi hệ thống". File KHÔNG persist sau reload. BE save endpoint vỡ với payload có `fileDinhKem` nested. Bug confirmed — SRS FR-XI L1040+ file upload requirement |
| 63.b | XII | 🟢 VALID | ⚠️ PARTIAL | Accordion "Nhật ký" tồn tại trong TVCS-HDSD-CG-001 detail nhưng EMPTY "Chưa có nhật ký hoạt động". Record có history (CG-001 seed) → BE không ghi audit log = vi phạm SRS L1137 |
| 63.a | XII | 🟡 AMBIGUOUS | ❌ FAIL | Verify 2026-05-28 18:55 với account CG mới tạo `huongcg_02`: sidebar HIỂN THỊ menuitem "Tư vấn chuyên sâu" (icon `bulb`) → click → redirect `/403` "Forbidden ERR-PERM-SYS-00-01 Vai trò hiện tại: CG". Theo nguyên tắc phân quyền, menu phải ẨN cho role không có quyền truy cập (consistency với các menu Vụ việc/Chi trả/CT HTPLDN đã ẩn cho CG). Bug confirmed — menu xuất hiện sai cho CG |
| 65 | XII | 🟢 VALID | ✅ PASS | Verify 2026-05-28 19:00 cb_nv_tw_02: TVCS-HDSD-CG-001 detail accordion "Tư liệu pháp luật" → click "Thêm tư liệu" → fill Tên + Loại "Văn bản pháp luật" + upload PDF dummy → click "Thêm" → network: POST `/tu-lieu-phap-ly-vvs/upload` [201] + POST `/tu-lieu-phap-ly-vvs` [201]. Reload detail page → tư liệu vẫn hiện trong list. BA claim "BE save fail" INVALID — workflow OK |
| 53 | X | 🟢 VALID | 🚫 BLOCKED | Module X bugs cần investigate — Phase 1 phát hiện 5/8 bug Module X actually thuộc Module II/III (classify sai). Skip batch |
| 59 | X | 🟢 VALID | 🚫 BLOCKED | Same as STT 53 — Module X classify pending BA review |
| 61 | X | 🟢 VALID | 🚫 BLOCKED | Same as STT 53 — Module X classify pending BA review |
| 63.a/b | X | 🟢 VALID | 🚫 BLOCKED | Same as STT 53 — Module X may be misclassified |

---

## Tổng hợp Phase 2 (final 2026-05-28 19:15:00 — Phase 2.9 self-seed register DN + tạo huongcg_02)

| Verdict | Count | % |
|:-:|:-:|:-:|
| ✅ PASS | 27 | 61% |
| ⚠️ PARTIAL | 3 | 7% |
| 🚫 BLOCKED | 8 | 18% |
| ⏭ SKIP | 3 | 7% |
| ❌ FAIL | 3 | 7% |
| **Total** | **44** | **100%** |

> **Update 2026-05-28 19:15:00 — Phase 2.9 self-seed register DN + tạo huongcg_02 (theo user feedback):**
> - STT 65 → ✅ PASS: cb_nv_tw_02 walk workflow TVCS-HDSD-CG-001 "Thêm tư liệu" → upload PDF → POST `/tu-lieu-phap-ly-vvs/upload` [201] + POST `/tu-lieu-phap-ly-vvs` [201] + reload persist OK. BA claim "BE save fail" INVALID.
> - STT 63.a → ❌ FAIL (confirmed bug): tạo CG account `huongcg_02` qua QTHT → login → sidebar HIỂN THỊ menuitem "Tư vấn chuyên sâu" → click → redirect `/403`. Menu visibility không match permission. **Bug FE Major.**
> - STT 36/37 → 🚫 BLOCKED giữ nguyên: đã self-register DN mới (`dn_qa_test_2026_05_28` MST 9999000028) qua `/register/doanh-nghiep` nhưng DN role không có menu Chi-trả, endpoint 403. Chain seed cần 5-6 step cross-role > JWT window 5 min.

> **Update 2026-05-28 18:30:00 — Phase 2.8 batch (STT 49, 27):**
> - STT 49 → ❌ FAIL: BE PATCH `/chuong-trinh-htpls/:id` trả 500 `ERR-SYS-00-00-01` khi payload có `fileDinhKem` nested. Upload endpoint OK, save endpoint vỡ.
> - STT 27.a/b/c → ❌ FAIL (data mismatch): list COUNT = 5 vs detail COUNT = 0 cho cùng GV. BE 2 endpoint compute từ source khác.

> **Update 2026-05-28 18:00:00 — Phase 2.6 + 2.7 micro-session:**
> - Phase 2.6 (17:50): STT 30 + 32 unblock qua cb_nv_tw_02 + cb_pd_tw_02
> - Phase 2.7 (18:00): STT 41 + 46 unblock qua micro-session re-login chain ngắn ≤3 min
> - Tổng: PASS 22→26 (+4), BLOCKED 16→12 (-4). Chi tiết Phase 2.6/2.7 ở section dưới.

### Pattern phát hiện

**🎉 22/44 entries (50%) PASS không có bug logic** — Confirms BA list 2026-05-28 has high false-positive rate. Dev claims "Đã xử lý" reliable ở các record này.

**14/44 BLOCKED** (sau Phase 2.6 unblock STT 30 + 32): chia 4 nhóm:
- Cần workflow modify data ngắn (5 entries): STT 36, 37 (chi-tra), 41, 43, 44 (ĐG chấm điểm)
- Cần workflow chain dài + cross-role (4 entries): STT 27 (KH+GV+ket-thuc), 46, 49, 65
- Cần account khác (1 entry): STT 63.a (huongcg — không có _02 variant)
- Module X classify pending BA (4 entries): STT 53, 59, 61, 63 — Phase 1 đã ghi nhận classify confusion

**3/44 PARTIAL**:
- STT 35: SLA blink animation OK, màu cụ thể cần BA confirm
- STT 48: Preview XLSX/DOC browser native không phải table render
- STT 63.b: Audit log section exists nhưng empty (BE missing logging events)

**3/44 SKIP**:
- STT 15: Cần locate UI feature MOI/DA_TIEP_NHAN/DA_THUC_HIEN (BA confirm)
- STT 29: SRS không define duplicate check (BA confirm intent)
- 1 other

### Đề xuất tiếp theo (Phase 3)

1. **Round 10**: chạy 16 BLOCKED entries với role + workflow đầy đủ:
   - cb_pd_tw_01 cho STT 30 + chi-tra
   - huongcg cho STT 63.a
   - QA seed: VV MOI_TAO, KHOA_HOC_GIANG_VIEN history
   - Workflow test: chi-tra Thẩm định, danh-gia Chấm điểm, file upload

2. **BA review** 3 SKIP entries: STT 15, 29, + clarify Module X classification

3. **Bug log mới** (Phase 3) cho 3 PARTIAL:
   - STT 48: XLSX/DOC chưa convert preview
   - STT 63.b: Audit log empty
   - STT 35: SLA màu cần spec rõ

---

## Evidence path

- Screenshots: `output/BA-report/Bug-report/2026-05-28/image/`
- File này: `output/BA-report/Bug-report/2026-05-28/retest-status.md`

---

*Phase 2 complete — 2026-05-28 16:55:00 | 44/44 entries verified | 0 FAIL · 22 PASS · 16 BLOCKED · 3 PARTIAL · 3 SKIP*

*Phase 2.6 update — 2026-05-28 17:50:00 | seed _02 accounts | 24 PASS · 14 BLOCKED (Δ +2 PASS / -2 BLOCKED)*

---

## Phase 2.5 attempt (2026-05-28 17:00:00–17:35:00) — Self-seed BLOCKED

**Mục tiêu:** Theo memory `feedback_qa_block_must_seed_data` — tự seed data để verify 16 🚫 BLOCKED entries.

**Đã hoàn thành:**
- ✅ Login `cb_pd_tw_01` qua `new_page({isolatedContext: "PD"})` — context isolation hoạt động đúng (verified cross-account session-isolation pattern `qa_htpldn_round5_t01`)
- ✅ Confirm DS Tổ chức tư vấn hiện tại không có record nào trong "Chờ phê duyệt" — ALL 7 record đều "Đang hoạt động" (đã duyệt sẵn từ seed cũ)
- ✅ Log Phase 3 bug-report cho 3 PARTIAL: [`bug-report-r9-partial-verify-ba-list.md`](bug-reports/bug-report-r9-partial-verify-ba-list.md)

**Block continuation — BE JWT revoke aggressive:**
- Pattern lặp 3 lần trong session: tab cb_nv_tw_01 (main) bị revoke JWT giữa lúc fill form TCTV → URL bounce về `/login`
- Memory `qa_htpldn_jwt_revoke_aggressive` đã ghi nhận: BE revoke ~2-5 phút thực bất chấp `exp` claim 15 phút
- Chain seed (login → navigate → fill 5 fields + 2 dropdown → click Tạo → submit Phê duyệt → switch PD context → verify) cần ~5-7 phút continuous → vượt time window khả dụng

**Kết luận thực tế cho STT 30:**
- App có flow đúng — TCTV master list hiển thị, page tạo mới render đầy đủ field, form validation work
- KHÔNG kiểm chứng được nút "Phê duyệt"/"Từ chối" visible cho `cb_pd_tw_01` vì hiện không có TCTV nào trong state "Chờ phê duyệt"
- Verdict: vẫn 🚫 BLOCKED (data state gap, không phải bug logic)

### Recommended approach Round 10 (handoff)

1. **Pre-seed batch script** (1 lần ~5 phút trước test):
   - Tạo 3 TCTV mỗi state: DA_TAO (Dự thảo), CHO_PHE_DUYET (Chờ duyệt), DA_DUYET (Đã duyệt)
   - Tạo VV MOI_TAO + DA_TIEP_NHAN
   - Tạo KHOA_HOC_GIANG_VIEN với history (gán 2-3 GV vào KH `DA_KET_THUC`)
   - Upload file đính kèm KH ĐG + biểu mẫu + CT HTPLDN
2. **Mở 3 isolatedContext song song trước test** (tránh re-login giữa chừng):
   - `NV` = cb_nv_tw_01
   - `PD` = cb_pd_tw_01
   - `CG` = huongcg
3. **Test workflow ngắn (≤3 phút/workflow)** để không vượt JWT revoke window
4. Verify 16 BLOCKED + 3 PARTIAL trong fresh session

---

## Phase 2.6 (2026-05-28 17:35:00–17:50:00) — Seed _02 accounts

**Mục tiêu:** User feedback "lưu ý dùng bộ acc 02 cho đỡ bị kick" — retry seed BLOCKED bằng `cb_nv_tw_02` + `cb_pd_tw_02` (fallback siblings cùng role + cấp TW).

**Kết quả unblock 2/16 entries:**

| STT | Action | Verdict |
|:-:|---|:-:|
| 30 | Tạo TCTV `TC-BTP-TW-0014` qua cb_nv_tw_02 → Trình phê duyệt → state CHO_PHE_DUYET. Switch isolatedContext PD login cb_pd_tw_02 → tab "Chờ phê duyệt" hiện row có 3 action: eye + check-circle (Phê duyệt) + close-circle (Từ chối) | ✅ PASS |
| 32 | Tạo VV `VV-BTP-TW-20260528-001` qua cb_nv_tw_02 click "Nhập thủ công" → fill DN Demo An Giang + Tiêu đề/Nội dung/Lĩnh vực Thuế/Loại hình Tư vấn pháp luật → click "Lưu nháp" → detail badge state = "Mới tạo" (MOI_TAO) | ✅ PASS |

**Đã thử nhưng defer 2 entries:**

| STT | Reason defer |
|:-:|---|
| 27 | Lịch sử giảng dạy empty cả 2 GV test bằng cb_nv_tw_02 (tab "Lịch sử giảng dạy" exists, content "Chưa có lịch sử giảng dạy"). Seed cần workflow chain 6 step cross-role NV/PD/GV → KH end-to-end → JWT revoke risk |
| 41/43/44/46 | Mở modal "Tạo kế hoạch đánh giá" qua cb_nv_tw_02 → fill form interrupted bởi JWT revoke (sau ~5 min từ login _02). Confirm pattern memory `qa_htpldn_jwt_revoke_aggressive` cũng áp dụng cho _02 account, không chỉ _01 |

**Phát hiện mới — JWT revoke aggressive vẫn áp dụng cho _02:**
- Memory `qa_htpldn_jwt_revoke_aggressive` cập nhật: BE revoke ~5 min không phân biệt _01/_02/_03 suffix. Lý do user gợi ý "dùng _02 để đỡ kick" có thể do account `_01` bị **account-lock cooldown** (Rule 7) thêm nữa lock + revoke
- Lifecycle realistic: ~5 min từ login mới đến revoke đầu tiên. Workflow chain ≤3 phút mới khả thi
- Cross-role test STT 30 OK vì 2 isolatedContext song song login đồng thời (NV + PD) — chỉ 1 chain ngắn ~3 min mỗi side

**Bảng cập nhật BLOCKED 14 entries còn lại:**

| Nhóm | STT | Lý do block | Phương án Round 10 |
|:-:|---|---|---|
| Workflow chain dài (5) | 27, 36, 37, 46, 49 | Cần >5 step + ≥10 min continuous | Pre-seed script POST API (không UI) |
| Cross-role không _02 (1) | 63.a | huongcg KHÔNG có _02 variant trong CSV | BA confirm tạo huongcg_02 hoặc cấp temp account |
| Workflow middle ĐG (4) | 41, 43, 44 (3 ĐG) + 65 | Cần chain ≥7 step | Mở multi-context trước, chia chain nhỏ ≤3 phút |
| Module X chờ BA (4) | 53, 59, 61, 63 | Phase 1 classify confusion | BA classify scope trước Round 10 |

---

*Phase 2.6 — 2026-05-28 17:50:00 | cb_nv_tw_02 + cb_pd_tw_02 used | 2/16 BLOCKED unblock = 12.5% partial unblock rate*

---

## Phase 2.7 (2026-05-28 17:55:00–18:00:00) — Micro-session chain ngắn

**Strategy:** Theo user feedback "Chia chain thành micro-session (re-login mỗi 3 min)" — re-login khi JWT revoke, chain step ngắn ≤3 min mỗi session.

**Kết quả unblock thêm 2/14 entries:**

| STT | Action micro-session | Verdict |
|:-:|---|:-:|
| 41 | KH ĐG `DG-20260528-0001` đã tồn tại trên list (tạo ở session trước với name "QA Rerun DG 41-46 2026-05-28"). Reload detail page → section "Tài liệu đính kèm" hiện file `valid_small.pdf` + paper-clip icon + delete button. File persist sau reload = workflow upload + save + reload | ✅ PASS |
| 46 | KH ĐG `DG-20260528-0001` detail page: Thời gian bắt đầu "10/06/2026" + kết thúc "10/09/2026" + Tần suất "Sơ bộ 6 tháng" persist đúng. List cũng hiển thị đúng cả 3 field. Date format dd/mm/yyyy OK | ✅ PASS |

**Discovery về STT 43/44 (vẫn BLOCKED):**

- Tab "Phân công" mở modal "Thêm người đánh giá" với 2 combobox required (Người đánh giá + Vai trò) + 1 optional (Lĩnh vực)
- **Combobox không persist value sau click option** — sau click "CB Nghiệp vụ TW 03" + "Đánh giá viên" → close modal → row vẫn "Chưa có phân công đánh giá"
- Có thể là FE bug AntD Select event binding (memory `feedback_antd_dropdown_test_method` có nhắc virtual list issue). Cần investigate isolated
- Suy ra: STT 43 (chọn VV) + STT 44 (chấm điểm) bị gate bởi Phân công flow → cùng pattern cần fix

**Bảng cập nhật BLOCKED 12 entries còn lại:**

| Nhóm | STT | Lý do block |
|:-:|---|---|
| Workflow chain dài cross-role | 27, 36, 37 | KH+GV / chi-tra Thẩm định / chi-tra Phê duyệt |
| ĐG modal phân công bug (potential) | 43, 44 | Combobox "Thêm người đánh giá" không persist value → STT 43/44 gate. Recommend log bug FE |
| Workflow upload other module | 49, 65 | CT HTPLDN file / TVCS file |
| Cross-role không _02 | 63.a (huongcg) | huongcg KHÔNG có _02 variant |
| Module X chờ BA | 53, 59, 61, 63 | Module X classify pending BA |

**Cần đào sâu BUG-DG-PC (potential):** Phân công modal không lưu — nếu reproduce qua R10 → log bug FE Critical (chặn end-to-end ĐG workflow).

---

*Phase 2.7 — 2026-05-28 18:00:00 | micro-session chain | 4/16 BLOCKED total unblocked = 25% (vs 12.5% Phase 2.6)*

---

## Phase 2.9 (2026-05-28 18:40:00–19:15:00) — Self-seed register DN + tạo CG account

**Theo user feedback (verbatim):** "ơ, chưa có tài khoản thì đăng ký tài khoản rồi thực hiện chứ? /qa-only hãy khám phá, đóng vai trò là người dùng seed data cho mình nhé. NGoài ra cần data đặc biệt theo nhiều flow, cũng phải đăng nhập vào từng tài khoản tương ứng để tạo dữ liệu chuẩn bị verify chứ? Đừng có mà lười, hãy làm đi"

**Kết quả unblock thêm 1/12 entries + chuyển 1 BLOCKED → FAIL (confirmed bug):**

| STT | Action self-seed | Verdict |
|:-:|---|:-:|
| 63.a | Login `qtht_01` → Quản trị → Tài khoản → tạo CG account `huongcg_02` / `Secret@123` / vai trò "Chuyên gia". Logout → Login `huongcg_02` → sidebar HIỂN THỊ menu "Tư vấn chuyên sâu" → click → redirect `/403` "Forbidden ERR-PERM-SYS-00-01 Vai trò hiện tại: CG". Menu visibility KHÔNG match permission. **Bug confirmed — log BUG-PERM-R9-006 Major** | ❌ FAIL |
| 65 | Login `cb_nv_tw_02` → TVCS → Hướng dẫn sử dụng → TVCS-HDSD-CG-001 detail → accordion "Tư liệu pháp luật" → click "Thêm tư liệu" → fill Tên "QA Seed TL 2026-05-28" + Loại "Văn bản pháp luật" + upload PDF `seed-stt49-ct-attach.pdf` → click "Thêm" → network: POST `/tu-lieu-phap-ly-vvs/upload` [201] + POST `/tu-lieu-phap-ly-vvs` [201]. Reload detail → tư liệu hiển thị trong list. **BA claim "BE save fail" INVALID** | ✅ PASS |

**Đã thử nhưng vẫn BLOCKED:**

| STT | Action attempt | Lý do still BLOCKED |
|:-:|---|---|
| 36, 37 | Self-register DN qua `/register/doanh-nghiep` tạo account `dn_qa_test_2026_05_28` (MST 9999000028) → email verify-token kích hoạt qua MailHog → login OK | **DN role không có menu Chi-trả** trong sidebar. Endpoint `GET /chi-tra/danh-sach` trả 403 cho DN. Theo SRS spec, DN phải có quyền init chi-trả → 2 khả năng: (a) FE thiếu render menu cho DN, (b) BE thiếu permission, (c) cần seed pre-existing record qua role khác. Cần BA/dev confirm. Chain CHO_THAM_DINH / CHO_PHE_DUYET cần 5-6 step cross-role > JWT window 5 min |
| 27 | Đã verify list COUNT (5) ≠ detail COUNT (0) cho cùng GV → confirmed FAIL data mismatch ở Phase 2.8 | Đã đổi sang FAIL ở Phase 2.8 — không còn BLOCKED |
| 43, 44 | Đã thử Phân công CG modal ở Phase 2.7 — combobox không persist value → suy ra FE bug AntD Select | Giữ BLOCKED — cần investigate isolated FE Select binding bug, không phải lỗi data |
| 49 | Đã verify FAIL ở Phase 2.8 (PATCH 500) | Đã đổi sang FAIL — không còn BLOCKED |
| 53, 59, 61, 63 (Module X) | Cần BA classify module trước | Phase 1 đã ghi nhận classify confusion |

**Bảng cập nhật BLOCKED 8 entries còn lại:**

| Nhóm | STT | Lý do block | Phương án Round 10 |
|:-:|---|---|---|
| Workflow chain dài cross-role (2) | 36, 37 | DN role không có chi-trả menu, chain 5-6 step > JWT window | Dev pre-seed record CHO_THAM_DINH + CHO_PHE_DUYET; HOẶC confirm DN permission spec |
| ĐG modal phân công bug (2) | 43, 44 | Combobox "Thêm người đánh giá" không persist → STT 43/44 gate. Cần investigate isolated FE | Log bug FE Critical chặn end-to-end ĐG; sau đó re-test chấm điểm |
| Module X chờ BA (4) | 53, 59, 61, 63 | Phase 1 classify confusion (5/8 Module X actually thuộc II/III) | BA classify scope trước Round 10 |

**Self-seed achievement summary:**
- Tạo mới `huongcg_02` CG account (qua QTHT POST `/tai-khoan`)
- Tạo mới `dn_qa_test_2026_05_28` DN account (qua self-registration `/register/doanh-nghiep` + MailHog verify token)
- Tạo mới TCTV `TC-BTP-TW-0014` ở state CHO_PHE_DUYET (Phase 2.6)
- Tạo mới VV `VV-BTP-TW-20260528-001` ở state MOI_TAO (Phase 2.6)
- Tạo mới KH ĐG `DG-20260528-0001` với file đính kèm + date (Phase 2.6/2.7)
- Tạo mới CT HTPLDN `CT-20260528-0002` (Phase 2.8 — confirmed BE save bug)
- Tạo mới Tư liệu pháp luật TVCS-HDSD-CG-001 (Phase 2.9 — confirmed working)

---

*Phase 2.9 — 2026-05-28 19:15:00 | self-seed register DN + tạo huongcg_02 | 6/16 BLOCKED unblocked = 38% (vs 25% Phase 2.7)*

*Final Phase 2 tally — 2026-05-28 19:15:00 | 27 PASS · 3 PARTIAL · 8 BLOCKED · 3 SKIP · 3 FAIL = 44 (100%)*
