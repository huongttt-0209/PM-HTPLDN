# Bug Report — R7.7.6 DT-031c FE thiếu button "Hủy công bố KQ"

> **Module:** Đào tạo / Khóa học HOAN_THANH / Tab "Kết quả" (FR-III-19 BR-FLOW-KQ-02)
> **Discovered:** 2026-05-12 R12.4 (sau verify DT-031b POST /publish PASS 202)
> **Reporter:** QA Automation Claude Code MCP

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| BUG-DT-031c-FE-MISSING-UNPUBLISH-01 | Major | UI tab "Kết quả" KH HOAN_THANH thiếu button "Hủy công bố KQ" — BE endpoint `POST /unpublish` đã expose nhưng FE không trigger được | Open |

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
