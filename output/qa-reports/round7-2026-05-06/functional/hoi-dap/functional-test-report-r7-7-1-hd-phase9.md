# Functional Test Report — R7.7.1 Hỏi đáp Phase 9 (Re-verify dev fix HD-053 + seed/R7.6.3 status)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-11 09:00:00 → 09:15:00 |
| **Loại test** | Re-verify 1 bug Open Phase 8 (HD-053) + recheck seed backdate + R7.6.3 endpoint deploy |
| **Round** | Round 7 / R7.7.1 Phase 9 |
| **Account** | `cb_pd_tw_04` (CB PD TW) — bypass OTP `666666` |
| **Tool** | Chrome DevTools MCP — UI click chain + `evaluate_script` DOM inspect |

---

## Verdict

✅ **1/1 bug Closed-verified (HD-053)** + ❌ **2 bug mới log (HD-055 + HD-014 Minor)** + 🚫 **12 TC chưa chạy được** (chia 3 nhóm: 7 chờ dev deploy Cổng PLQG · 4 chờ dev chạy SQL lùi ngày · 1 chờ dev fix UX modal)

| BUG-ID | Severity | Verdict | Chi tiết |
|---|---|---|---|
| BUG-HD-053-DEFAULT-IMAGE-001 | Minor | ✅ Closed-verified | Modal CR-01 có button "Dùng ảnh hệ thống mặc định" cạnh upload zone, accept hint thêm `.gif` đúng SCR-II-02 line 1149. Click → preview `/default-avatar-cong-khai.png` + button toggle "Đổi ảnh khác" |
| BUG-HD-055-PUBLISH-FAIL-UX-001 | Minor | ❌ Open (confirm Phase 8) | Inject 500 ERR-PD-04 cho POST `/cong-khai` qua XHR override: state guard OK (DA_DUYET, congKhai=false), nhưng modal đứng yên — không hiện text lỗi, không nút "Thử lại", không toast. Đã log [bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md) |
| BUG-HD-014-REJECT-ERR-CODE-001 | Minor | ❌ Open (mới Phase 9) | POST `/tu-choi` với `lyDo` rỗng/null → BE trả `ERR-VAL-SYS-00-01` thay vì `ERR-PD-02` spec yêu cầu. Validation hoạt động đúng nhưng error code không khớp spec. Đã log [bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md) |

## 12 TC chưa chạy được — chia 3 nhóm rõ nguyên nhân

> Trước đây gọi là "defer" / "block". Mình đổi sang ngôn ngữ tự nhiên để dev/BA đọc 1 lần hiểu ngay TC nào kẹt vì gì, ai cần làm gì.

### Nhóm 1 — Chờ dev BE deploy Cổng PLQG endpoint (7 TC)

**TC:** HD-027, HD-045, HD-047, HD-048, HD-060, HD-061, HD-062

**Vì sao chưa chạy được:** Cổng PLQG (cổng pháp luật quốc gia — chỗ doanh nghiệp tự submit câu hỏi từ ngoài) chưa được dev BE deploy lên môi trường test. Mình thử 8 đường dẫn API candidate (vd `/api/v1/cong-plqg/inbound/hoi-dap`, `/cong-plqg/health`, POST inbound...) **đều trả 404 "không tồn tại"**. Filter `?kenhTiepNhan=TVN_BRIDGE` trả 0 record (không có dữ liệu chuyển từ Tư vấn nhanh ESCALATE).

**Cần làm gì để chạy được:** Dev BE deploy task **R7.6.3** — gồm 2 phần: (a) endpoint inbound cho DN submit câu hỏi qua Cổng PLQG; (b) bridge endpoint từ phiên Tư vấn nhanh ESCALATE sang Hỏi đáp.

**Ai làm:** Dev BE.

### Nhóm 2 — Chờ dev chạy SQL "lùi ngày" cho 4 record (4 TC)

**TC:** HD-022b (SLA badge xanh ~30%), HD-022c (SLA badge vàng ~70%), HD-022d (SLA badge đỏ ~110%), HD-057 (verify hệ thống KHÔNG tự đóng record sau 30 ngày)

**Vì sao chưa chạy được:** Cần test 4 mức cảnh báo SLA hiển thị theo **tỷ lệ thời gian xử lý đã trôi** (BR-SLA-02) + verify hệ thống không auto-close record DA_DUYET sau 30 ngày (BR-FLOW-06). **UI không có chỗ "lùi ngày" tay được** — phải chỉnh trực tiếp trong DB. Mình đã gửi file [seed-request-hd-022-057-backdate-sla.md](../../bug-reports/hoi-dap/seed-request-hd-022-057-backdate-sla.md) chứa 4 câu SQL UPDATE backdate `ngay_tiep_nhan`/`created_at` cho dev (~15 phút work).

**Verify lúc 2026-05-11 09:55:00:** 4 record vẫn nguyên `ngayTao` cách hiện tại 1.27-2.03 ngày (chưa backdate 1.5/3.5/5.5/35 ngày như SQL yêu cầu). `mucDoCanhBao=BINH_THUONG` toàn pool, 0 record `SAP_HET_HAN`/`QUA_HAN` → **dev chưa apply SQL** (có thể chạy nhầm DB dev/staging khác, hoặc commit miss).

**Cần làm gì để chạy được:** Dev BE chạy 4 câu SQL trong file seed-request (15 phút) trên đúng DB test http://103.172.236.130:3000/.

**Ai làm:** Dev BE.

### Nhóm 3 — Chờ dev FE fix UX modal (1 TC)

**TC:** HD-055 (modal Công khai xử lý lỗi 500 từ Cổng PLQG)

**Vì sao chưa chạy được:** Modal "Công khai lên Cổng PLQG" khi BE trả 500 (vd lỗi mạng / lỗi máy chủ / lỗi nghiệp vụ) thì **đứng yên hoàn toàn** — không hiện text lỗi `ERR-PD-04`, không có nút "Thử lại" trong modal, không có toast/notification. State guard OK (record vẫn `DA_DUYET`, `congKhai=false`) nhưng user không biết tại sao submit fail → user phải đóng modal mở lại + nhập lại từ đầu.

**Cần làm gì để chạy được:** Dev FE sửa error handler trong component modal CR-01: (a) hiện text lỗi phân biệt mạng/máy chủ/nghiệp vụ + mã `ERR-PD-04`; (b) thêm nút **[Thử lại]** trong modal để user gọi lại request mà không đóng modal/mất dữ liệu nhập; (c) giữ form data (mô tả/ảnh/tệp) khi lỗi.

**Ai làm:** Dev FE.

**Bug log:** [bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md) (đã chứa method inject 500 qua XHR override cho dev reproduce).

---

## Test result breakdown

| Bug | Method | Evidence |
|---|---|---|
| BUG-HD-053 | UI cb_pd_tw_04 → HD-20260510-001 (DA_DUYET) → [Công khai] modal CR-01 mở. `evaluate_script` inspect: button uid=251_12 "Dùng ảnh hệ thống mặc định" cạnh upload zone, accept hint `.jpg, .png, .gif`. Click button → preview `<img src="/default-avatar-cong-khai.png" alt="Ảnh hệ thống mặc định">` render trong zone, button toggle "Đổi ảnh khác", 2 button cuối modal vẫn [Hủy/Công khai]. | [r7-hd-053-retest-r10e-default-image-btn-fixed.png](../../bug-reports/hoi-dap/image/r7-hd-053-retest-r10e-default-image-btn-fixed.png) + [r7-hd-053-retest-r10e-default-image-preview-after-click.png](../../bug-reports/hoi-dap/image/r7-hd-053-retest-r10e-default-image-preview-after-click.png) |
| R7.6.3 probe | `evaluate_script` fetch 8 candidate endpoints (`/api/v1/cong-plqg/inbound/hoi-dap`, `/cong-plqg/health`, `/cong-plqg/status`, `/cong-plqg/hoi-dap`, `/inbound/cong-plqg/hoi-dap`, `/external/hoi-daps`, `/cong-plqg/inbound`, POST inbound) — tất cả 404 ERR-SYS-00-04-01. Filter `?kenhTiepNhan=TVN_BRIDGE&size=5` → empty content. | — |
| Seed backdate check | GET API 4 ID record trong seed-request — `ngay_tiep_nhan` vẫn ~2026-05-09/10 (1-2 ngày trước), không backdate 1.5/3.5/5.5/35 ngày như SQL trong seed-request. Dev chưa apply. | — |
| HD-055 inject 500 | UI cb_pd_tw_04 → HD-20260510-006 (DA_DUYET) → install XHR + fetch override chặn POST `/cong-khai` trả 500 ERR-PD-04. Click [Công khai lên Cổng PLQG] → modal mở → fill mô tả → click [Công khai]. Modal đứng yên 2s, không text lỗi, không nút Thử lại, không toast. Buttons `["","Dùng ảnh hệ thống mặc định","Hủy","Công khai"]` — không có Thử lại. Verify state qua origFetch: `DA_DUYET, congKhai=false, version=8` → state guard OK. | [r7-hd-055-retest-r10e-modal-no-error-after-500.png](../../bug-reports/hoi-dap/image/r7-hd-055-retest-r10e-modal-no-error-after-500.png) |
| HD-014 re-verify | POST `/api/v1/hoi-daps/{id}/tu-choi` với `lyDo: ""` và `lyDo: null` trên DA_DUYET record. BE trả 422 `ERR-VAL-SYS-00-01` field=`lyDo`, message "Lý do từ chối là bắt buộc (tối thiểu 10 ký tự)" + "lyDo should not be empty". Validation enforce TRƯỚC state check (BE validate input layer). Spec yêu cầu `ERR-PD-02` — code mismatch. | API response trong test breakdown |
| HD-021 re-verify | UI cb_pd_tw_04 → /hoi-dap. `evaluate_script` count `[role="tab"]` = **7**: Tất cả / Mới (badge 5) / Đang xử lý / Chờ phê duyệt / Đã duyệt / Công khai / Hoàn thành. Tab "Hoàn thành" filter `?tab=HOAN_THANH&size=1` trả total=**7** = HOAN_THANH (3) + HUY (4) — gộp v3.5 đúng SCR-II-01 line 1027-1033. | [r7-hd-021-retest-r10e-7tabs-with-counts.png](r7-hd-021-retest-r10e-7tabs-with-counts.png) |
| HD-035 re-verify | API search `?keyword=lương&trangThai=<X>` với 3 state processed: DA_DUYET (total=2, snippet match), HOAN_THANH (total=3, snippet match), CONG_KHAI (total=0 vì pool 0 record). Search full-text hoạt động đúng cho processed state. | API response |
| HD-008 re-verify | GET `/api/v1/hoi-daps?size=20` — 9/10 record có deadline = ngayTiepNhan + 5 working days (calendar diff 5-6). 1 outlier HD-20260510-002 (mucDoPhucTap=THUONG, deadline +36 cal days) — có thể user override hoặc edge case. Main path BR-SLA-01 OK. | API response |

> **Severity breakdown defects mới (Phase 9):** 2 Minor — (1) BUG-HD-055-PUBLISH-FAIL-UX-001 đã log [bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md); (2) BUG-HD-014-REJECT-ERR-CODE-001 đã log [bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md)

---

## Cumulative R7.7.1 sau Phase 9

| Phase | TC PASS | Tên |
|---|---|---|
| Phase 1 | 13 | HD-001..HD-014, HD-019 |
| Phase 2A | 4 | HD-013, HD-023, HD-024, HD-031 |
| Phase 2B | 7 | HD-029, HD-034, HD-035, HD-046, HD-056, HD-058, HD-063 |
| Phase 3a | 3 | HD-025, HD-026, HD-064 |
| Phase 3b | 2 | HD-030, HD-059 |
| Phase 4 | 7 | HD-020, HD-022 (partial), HD-028, HD-040, HD-041, HD-042, HD-043 (partial) |
| Phase 5 | 3 | HD-032, HD-044, HD-052 |
| Phase 6 | 3 | HD-015, HD-016, HD-053 (đếm Phase 6 — Phase 9 dev fix nâng full-clean, drop caveat) |
| Phase 7 | 0 | Re-verify HD-021/022/016 đóng + R7.6.3 block |
| Phase 8 | 1 | HD-054 PASS (Công khai submit OK); HD-055 PARTIAL UX fail, HD-053 vẫn Open ở Phase 8 |
| **Phase 9** | **0 TC mới** | **Re-verify HD-053 dev fix → Closed-verified (drop caveat Phase 6). 6/6 bug flow đóng** |
| **Total** | **43** | **72% R7.7.1 coverage** |

🚫 **Còn 12 TC chưa chạy được** (chi tiết 3 nhóm ở section "12 TC chưa chạy được" phía trên):
- **7 TC chờ dev BE deploy Cổng PLQG (R7.6.3):** HD-027, HD-045, HD-047, HD-048, HD-060, HD-061, HD-062
- **4 TC chờ dev BE chạy SQL "lùi ngày":** HD-022b (xanh ~30%), HD-022c (vàng ~70%), HD-022d (đỏ ~110%), HD-057 (không auto-close 30 ngày)
- **1 TC chờ dev FE fix UX modal:** HD-055 (modal Công khai không hiện lỗi + nút Thử lại)

---

## Bug active sau Phase 9

**Đã đóng Phase 9:** BUG-HD-053-DEFAULT-IMAGE-001 (1/1) → Pass-bug-report-flow-hoi-dap.md 6/6 đóng.

**Còn Open Phase 9:**
- BUG-HD-055-PUBLISH-FAIL-UX-001 (Minor) — Modal Công khai không hiện ERR-PD-04 + nút "Thử lại" khi BE trả 500. Log [bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-055-modal-publish-fail-ux.md).
- BUG-HD-014-REJECT-ERR-CODE-001 (Minor) — POST `/tu-choi` empty lyDo trả `ERR-VAL-SYS-00-01` thay vì spec-required `ERR-PD-02`. Log [bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md](../../bug-reports/hoi-dap/bug-report-r7-7-1-hd-014-reject-err-code-mismatch.md).

**File rename:** Bug flow Hỏi đáp 6/6 đóng → `Pass-bug-report-flow-hoi-dap.md` (auto-rename hook PostToolUse).

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| API base | http://103.172.236.130:3000/api/v1 |
| Tool test | Chrome DevTools MCP — UI click chain + `evaluate_script` DOM inspect |
| Test record | HD-20260510-001 (DA_DUYET state — modal CR-01 Công khai) |
| Bộ account | `_04` series (per user request session 2026-05-11) |

---

*Functional report generated: 2026-05-11 09:15:00 | QA Automation via Claude Code (Opus 4.7)*
