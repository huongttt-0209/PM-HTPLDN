# Bug Report — R7.7.6 DT-031c FE thiếu button "Hủy công bố KQ"

> **Module:** Đào tạo / Khóa học HOAN_THANH / Tab "Kết quả" (FR-III-19 BR-FLOW-KQ-02)
> **Discovered:** 2026-05-12 R12.4 (sau verify DT-031b POST /publish PASS 202)
> **Reporter:** QA Automation Claude Code MCP

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 1     | 0      | 0     | 0       | 1      | 0    |

> **Quy tắc đếm:** Tổng = số dòng bug trong **Bug Summary Table**; 5 cột severity tổng = Tổng; Open ∈ {Open, Reopen}; Closed ∈ {Closed, ~~closed~~, WITHDRAWN}.

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| ~~BUG-DT-031c-FE-MISSING-UNPUBLISH-01~~ | Major | UI tab "Kết quả" KH HOAN_THANH thiếu button "Hủy công bố KQ" — BE endpoint `POST /unpublish` đã expose nhưng FE không trigger được | **Closed** (R13 2026-05-13 16:13 verified — FE đã add 3 elements đúng spec: button "stop Hủy công bố KQ" + indicator "Đã công bố lúc {thoiGianCongBo}" + modal "Hủy công bố kết quả" với textarea `lyDo` required max 2000 chars; conditional render đúng theo `congBo` state; R12.5 BE endpoint POST /unpublish 202 + state đổi đã verify; R13 parallel session đã submit full cycle thành công trên KH-001 (lyDo trail "QA R13 verify FE Hủy công bố KQ button — auto-restore sau test")) |

> **🎯 R13 RE-VERIFY 2026-05-13 16:13 (sau kill orphan MCP Chrome + MCP browser recovered):**
>
> **Status:** ✅ **CLOSED** — FE đã FIX đầy đủ 3 elements theo recommend trong bug-report.
>
> | Layer | Evidence R13 | Status |
> |---|---|:-:|
> | **FE button render conditional** | KH-HDSD-AG-003 (HOAN_THANH, 5 KQ `congBo=true`): UI tab "Kết quả" hiển thị button "stop Hủy công bố KQ" (uid=50_65) thay vì "Công bố kết quả". KH-001 (HOAN_THANH, 1 KQ `congBo=false`): UI hiển thị "cloud-upload Công bố kết quả" (uid=47_33). Conditional render đúng theo state. | ✅ |
> | **FE indicator "Đã công bố lúc {timestamp}"** | KH-HDSD-AG-003 hiển thị "Đã công bố lúc 25/03/2026 22:32" (uid=50_66 + 50_67) cạnh button. | ✅ |
> | **Modal "Hủy công bố kết quả"** | Click button → modal opens (uid=51_0) với title "Hủy công bố kết quả" + description "Hệ thống sẽ gửi yêu cầu hủy công bố sang Cổng PLQG. Vui lòng nhập lý do hủy." + textarea `lyDo` required (uid=51_6) + counter "0 / 2000" (uid=51_7) + button "Hủy công bố" submit (uid=51_9) + button "Đóng" cancel (uid=51_8). | ✅ |
> | **POST /unpublish full cycle** | R13 parallel QA session (07:10) đã test full submit trên KH-001: lyDo trail = "QA R13 verify FE Hủy công bố KQ button — auto-restore sau test" → POST /unpublish 202 → `congBo: true → false` + `lyDoHuyCongBo` set. R12.5 14:42 cũng đã verify BE endpoint 100% functional với 3 KQDT KH-005 unpublished thành công. | ✅ |
>
> **Screenshots evidence R13:**
> - [r13-dt031c-fe-fixed-button-huy-cong-bo.png](image/r13-dt031c-fe-fixed-button-huy-cong-bo.png) — UI tab "Kết quả" KH-HDSD-AG-003 với button "stop Hủy công bố KQ" + indicator "Đã công bố lúc 25/03/2026 22:32"
> - [r13-dt031c-modal-huy-cong-bo-lydo.png](image/r13-dt031c-modal-huy-cong-bo-lydo.png) — Modal "Hủy công bố kết quả" với textarea `lyDo` required + counter 0/2000 + 2 buttons
>
> **R13 Net:** Bug DT-031c **FULLY CLOSED**. FE đã implement exact recommend trong bug-report Section "Recommend fix FE":
> 1. ✅ Conditional button render based on `record.congBo` state
> 2. ✅ Modal có textarea `lyDo` required max 2000 chars
> 3. ✅ Indicator "Đã công bố lúc {thoiGianCongBo}"
>
> **Side-effect R13:** Modal mở thử trên KH-HDSD-AG-003 (5 records `congBo=true`) → click "Đóng" cancel → KH-HDSD-AG-003 state preserved (vẫn 5 records congBo=true, không submit). KH-HDSD-AG-003 fixture không bị disturb.
>
> **🔁 R12.7 RE-VERIFY 2026-05-13 14:13 (user trigger "verify lại bug DT-031c"):**
>
> **Status:** ⏳ **Partial deferred — BE side CONFIRMED OK, FE side cần UI re-test.**
>
> | Layer | Probe / Evidence | R12.7 Result | Status |
> |---|---|---|:-:|
> | **BE endpoint exists** | `POST /api/v1/khoa-hocs/{id}/ket-quas/unpublish` | Route registered, validation OK (yêu cầu body `{lyDo: 1-2000 chars, hocVienIds?: []}`) — verified từ R12.4 + reconfirm R12.5 | ✅ |
> | **BE endpoint functional** | R12.5 probe trên KH-005 với body `{lyDo: 'verify probe R12.5'}` | **202 Accepted** + 3 records HV01/02/03 state đổi: `congBo: true → false` + `lyDoHuyCongBo='verify probe R12.5'` set (xem `tasks/state-snapshot.md` dòng "KQDT KH-005 congBo"). BE hoàn toàn functional. | ✅ |
> | **FE button render** | Tab "Kết quả" KH-001 HOAN_THANH (1 KQDT đang `congBo=true` post R12.4 publish) | ⏳ **CHƯA verify R12.7** — MCP browser locked bởi parallel QA session (Chrome processes started 14:08); không thể navigate UI để check button "Hủy công bố KQ" / per-row action. | ⏳ |
> | **FE state indicator** | Sau publish, check label button + indicator "Đã công bố lúc X" | ⏳ **CHƯA verify R12.7** — same reason. | ⏳ |
>
> **R12.7 Net:** Bug status giữ **Open** (chưa có evidence FE fix). BE side đã confirm 100% functional → bug ngữ nghĩa "FE missing button" vẫn valid pending FE binding to BE endpoint.
>
> **Recommend handoff cho next QA tester (khi MCP browser free):**
> 1. Login `cb_nv_tw_01` fresh, navigate `/dao-tao/khoa-hoc/19158f55-4f7a-404a-8ba9-a75de1130e57?tab=ket-qua-kiem-tra` (KH-001 HOAN_THANH, 1 KQDT congBo=true).
> 2. Quan sát buttons trên tab Kết quả — tìm "Hủy công bố KQ" / "Gỡ công bố" / per-row action.
> 3. Nếu thấy → click → modal có textarea `lyDo` không? → submit → verify network `POST /unpublish` body `{lyDo}` + state đổi sang `congBo: false`.
> 4. Nếu vẫn KHÔNG có button → giữ Open + ping dev FE (BE đã sẵn sàng từ R12.4, chỉ cần FE binding).
>
> **Side-effect cảnh báo:** Nếu test unpublish trên KH-001, sẽ flip KQDT.congBo về false. KH-001 HOAN_THANH có thể re-publish lại (POST /publish 202) vì state HOAN_THANH thoả guard ERR-BIZ-III-36-01. Khác với KH-005 DA_KET_THUC không re-publish được (xem state-snapshot row "KQDT KH-005 congBo").

---

## BUG-DT-031c-FE-MISSING-UNPUBLISH-01

### Mô tả

Sau khi click "Công bố kết quả" thành công (POST `/khoa-hocs/{id}/ket-quas/publish` → 202 Accepted), KQ chuyển sang `congBo=true` + `thoiGianCongBo` set. UI tuy nhiên không cung cấp button "Hủy công bố KQ" để trigger workflow huỷ. BE endpoint `POST /khoa-hocs/{id}/ket-quas/unpublish` đã tồn tại và validation OK (yêu cầu body `{lyDo: string, hocVienIds?: []}`), nhưng FE không có UI binding.

Plus minor UX: button "Công bố kết quả" giữ nguyên label sau khi đã công bố — user không có chỉ báo "Đã công bố ngày X".

### Bước tái hiện

1. Login `cb_nv_tw_01` / `Secret@123` / OTP `666666`.
2. Navigate `/dao-tao/khoa-hoc/19158f55-4f7a-404a-8ba9-a75de1130e57?tab=ket-qua-kiem-tra` (KH-20260509-001 "Pháp luật doanh nghiệp căn bản - R9", state HOAN_THANH, 1 KQDT).
3. Click button "Công bố kết quả" → modal "Công bố kết quả lên Cổng PLQG?" → click "Công bố".
4. Đợi 2s, reload tab Kết quả.
5. Quan sát buttons + per-row actions trên tab.

### Kết quả mong đợi (FR-III-19 + BR-FLOW-KQ-02)

Sau khi `congBo=true`, UI phải:
- Hiển thị button "Hủy công bố KQ" / "Gỡ công bố" để trigger `POST /unpublish` với body `{lyDo: ...}`.
- Hoặc per-row action "Hủy công bố" cho HV cụ thể (HV-level granularity).
- Indicator "Đã công bố lúc {thoiGianCongBo}" để user biết state.

### Kết quả thực tế

UI sau publish:
- Button "Công bố kết quả" giữ nguyên label (uid=34_65) — không có chỉ báo "Đã công bố".
- KHÔNG có button "Hủy công bố KQ" / "Gỡ công bố" / "Hủy" ở header tab Kết quả.
- KHÔNG có per-row action "Hủy công bố" (cột "Ghi chú" disabled, không có cột Action).
- Chỉ có "Gỡ công khai" ở header KH (uid=34_79) — nhưng đó là button KH-level (làm KH ẩn khỏi public catalog), KHÔNG phải KQ-level unpublish.

→ User KHÔNG thể trigger unpublish qua UI. Chỉ làm được qua API direct (curl / Postman).

### Bằng chứng

- Screenshot UI tab "Kết quả" sau publish: [image/r12-dt031c-fe-thieu-button-huy-cong-bo.png](image/r12-dt031c-fe-thieu-button-huy-cong-bo.png)
- Network log: `POST /api/v1/khoa-hocs/19158f55.../ket-quas/publish → 202` (reqid 5689)
- API verify state sau publish: `{congBo: true, thoiGianCongBo: "2026-05-12T11:12:53.056Z", lyDoHuyCongBo: null}`
- BE endpoint exists probe: `POST /api/v1/khoa-hocs/{id}/ket-quas/unpublish` → 422 ERR-VAL-SYS-00-01 "lyDo must be shorter than or equal to 2000 characters" (validation OK, route registered)
- BE endpoint NOT found: `POST .../ket-quas/huy-cong-bo` → 404 (sai naming, đúng path là `/unpublish`)

### So sánh

| Source | Trạng thái |
|---|---|
| **BE** (`unpublish` endpoint) | ✅ Đã expose, validation OK, cần body `{lyDo: string [1-2000 chars], hocVienIds?: []}` |
| **FE** (button trigger) | ❌ KHÔNG có button "Hủy công bố KQ" hay equivalent — không có UI flow |

**Spec ref:** `srs-update-2026-5-5/srs-fr-03-dao-tao.md` FR-III-19 (Công bố KQ + Hủy công bố KQ là 2 actions đối ngẫu lifecycle BR-FLOW-KQ-02).

**Impact:**
- Workflow "Công bố sai → cần hủy → fix → công bố lại" KHÔNG khả thi qua UI.
- CB NV phải gọi BE/dev mỗi khi cần hủy → ops cost cao, lỗi user.
- Không có chỉ báo "Đã công bố" → nguy cơ click "Công bố" nhiều lần (BE idempotent thì OK, nhưng UX confusing).

**Severity:** Major (block workflow chuẩn FR-III-19 BR-FLOW-KQ-02 + ảnh hưởng audit trail KQ).

**Recommend fix FE:**
1. Thêm conditional button render based on KQ state:
   - Nếu `record.congBo === false` → hiện button "Công bố kết quả" (current).
   - Nếu `record.congBo === true` → hiện button "**Hủy công bố KQ**" + indicator "Đã công bố lúc {thoiGianCongBo}".
2. Modal "Hủy công bố" có textarea `lyDo` (required, max 2000 chars) → POST `/unpublish` với body `{lyDo}`.
3. Cân nhắc per-row action button (HV-level granularity) thay vì batch toàn bộ KQ.
