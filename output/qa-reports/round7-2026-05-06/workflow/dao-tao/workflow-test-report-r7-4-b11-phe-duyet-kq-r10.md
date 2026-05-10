# Workflow Test Report — Phê duyệt kết quả Khóa học (R7.4.B11 — R10)

> **Module:** Workflow Phê duyệt KQ Khóa học (FR-III-21) · **SRS:** [`02-thu-tu-module.md §SM-KHOAHOC`](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) · **Round:** R10 · **Date:** 2026-05-10 01:36-01:42 · **Tester:** QA Automation Claude Code MCP
> **Test mode:** UI click thực tế (per memory rule `feedback_qa_test_via_ui_not_api`).
> **Trigger:** User explicit "chạy R7.4.B11" sau R7.4.B7 R10 unblock — KH-001 hiện ở `CHO_DUYET_KQ` sẵn sàng test.

---

## 🎯 Tóm tắt nhanh (cho PM/BA)

**Kết quả: ✅ FULL PASS — cả 2 path (positive Duyệt KQ + negative Từ chối KQ) đều work qua UI.**

| Path | Bước | Account | Kết quả |
|---|---|---|:-:|
| 🟢 **Negative** (Từ chối) | KH-001 CHO_DUYET_KQ → click "Từ chối KQ" → modal nhập lý do → submit | `cb_pd_tw_01` | ✅ Rollback về `DA_KET_THUC` v13 |
| ✅ Resubmit | NV resubmit (Gửi duyệt KQ) → `DA_KET_THUC → CHO_DUYET_KQ` | `cb_nv_tw_02` | ✅ v14 |
| 🟢 **Positive** (Duyệt) | KH-001 CHO_DUYET_KQ → click "Duyệt KQ" → modal confirm | `cb_pd_tw_01` | ✅ Advance `HOAN_THANH` v15 |

**Chu trình full đã verified:**
```
DA_KET_THUC (v12) →[NV submit-result]→ CHO_DUYET_KQ (v13)
                  →[PD reject-result]→ DA_KET_THUC (v13)    ← negative path
                  →[NV submit-result]→ CHO_DUYET_KQ (v14)    ← resubmit OK
                  →[PD approve-result]→ HOAN_THANH (v15)     ← positive path
```

**Ý nghĩa team:**
- ✅ FR-III-21 (Phê duyệt KQ KH) đã chạy được full positive + negative round-trip
- ✅ Modal reject có required field "Lý do từ chối" + textarea max 2000 chars + validation `Vui lòng nhập lý do từ chối`
- ✅ Reject KQ rollback về `DA_KET_THUC` (không tạo state `TU_CHOI_KQ` riêng — consistent với pattern reject ở R7.4.B7 R9 reject = DU_THAO)
- ✅ NV có thể resubmit sau reject → loop về CHO_DUYET_KQ, không bị block 1 chiều
- ⚠️ **Spec drift Minor (cùng pattern R7.4.B0):** BE response GET KH-001 KHÔNG trả `lyDoTuChoiKQ / nguoiTuChoiKQId / ngayTuChoiKQ` fields — lý do từ chối có thể chỉ lưu trong audit log hoặc field `ghiChuPheDuyet` (mà field này vẫn giữ giá trị R9 cũ). Chờ BA confirm spec field naming + persist requirement.

---

## ✅ R10 UI test chain — KH-001 full round-trip

### Step 1 — Negative path: PD Từ chối KQ

| # | Action | Account | Kết quả |
|:-:|---|---|---|
| 1.1 | Login PD `cb_pd_tw_01` + navigate KH-001 detail | PD | ✅ View shows 2 buttons: "Duyệt KQ" + "Từ chối KQ" |
| 1.2 | Click "Từ chối KQ" → modal "Từ chối kết quả" mở | PD | ✅ Modal: title + description "Kết quả khóa học sẽ trở về Đã kết thúc để cán bộ chỉnh sửa và trình lại." + textarea required + counter "0 / 2000" |
| 1.3 | Click "Từ chối" mà không nhập lý do | PD | ✅ Validation: textarea invalid=true + error "Vui lòng nhập lý do từ chối" |
| 1.4 | Type lý do (158 chars) + click "Từ chối" | PD | ✅ `POST /reject-result` → 200 |
| 1.5 | Stepper: rollback từ 5 ✓ → 4 ✓ ("Đã kết thúc" no longer ✓) | — | ✅ State BE: `trangThai=DA_KET_THUC, version=13` |

**Modal text exact:**
- Title: `Từ chối kết quả`
- Description: `Kết quả khóa học sẽ trở về Đã kết thúc để cán bộ chỉnh sửa và trình lại.`
- Field: `Lý do từ chối *` (textarea, max 2000 chars)
- Validation: `Vui lòng nhập lý do từ chối` (khi submit empty)
- Buttons: `Quay lại / Từ chối`

### Step 2 — Resubmit: NV gửi duyệt KQ lại

| # | Action | Account | Kết quả |
|:-:|---|---|---|
| 2.1 | Logout PD + Login NV `cb_nv_tw_02` + navigate KH-001 | NV | ✅ View shows 2 buttons: "Gỡ công khai" + "Gửi duyệt KQ" |
| 2.2 | Click "Gửi duyệt KQ" → modal "Trình duyệt kết quả?" mở | NV | ✅ Modal description "Kết quả của khóa học sẽ được gửi cho lãnh đạo phê duyệt." + buttons "Hủy / Trình duyệt" |
| 2.3 | Click "Trình duyệt" | NV | ✅ `POST /submit-result` → 200, state `CHO_DUYET_KQ, version=14` |

→ **Resubmit pattern OK** — không có block "đã từ chối thì không submit lại được". Workflow loop khả dụng.

### Step 3 — Positive path: PD Duyệt KQ

| # | Action | Account | Kết quả |
|:-:|---|---|---|
| 3.1 | Logout NV + Login PD `cb_pd_tw_01` + navigate KH-001 | PD | ✅ View shows 2 buttons: "Duyệt KQ" + "Từ chối KQ" |
| 3.2 | Click "Duyệt KQ" → modal "Phê duyệt kết quả?" mở | PD | ✅ Modal description "Kết quả đào tạo sẽ được phê duyệt và khóa học chuyển sang Hoàn thành." + buttons "Hủy / Phê duyệt KQ" |
| 3.3 | Click "Phê duyệt KQ" | PD | ✅ `POST /approve-result` → 200, state `HOAN_THANH, version=15` |
| 3.4 | Stepper: 6 ✓ — terminal state | — | ✅ `_links: ["self"]` only — no more transitions |

---

## API endpoint discovered R10 — full set FR-III-21

| State from | State to | Endpoint | Method | Required role | Required body | R10 status |
|---|---|---|---|---|---|:-:|
| CHO_DUYET_KQ | HOAN_THANH | `/khoa-hocs/{id}/approve-result` | POST | CB_PD_TW | `{version}` (suspected) | ✅ 200 (KH-001 + KH-007 R7.4.B7 R10) |
| CHO_DUYET_KQ | DA_KET_THUC | `/khoa-hocs/{id}/reject-result` | POST | CB_PD_TW | `{version, lyDo}` | ✅ 200 (KH-001 R10 negative) |
| DA_KET_THUC | CHO_DUYET_KQ | `/khoa-hocs/{id}/submit-result` | POST | CB_NV_TW | `{version}` (suspected) | ✅ 200 (resubmit verified) |

**Pattern:** Reject KQ trả về DA_KET_THUC (không phải TU_CHOI_KQ separate state). Consistent với pattern R7.4.B7 R9 reject KH = DU_THAO (không phải TU_CHOI). BE design: phase reject = previous-state rollback + lý do field.

---

## Bằng chứng

### Network log
```
POST /api/v1/khoa-hocs/19158f55-4f7a-404a-8ba9-a75de1130e57/reject-result   → 200  (negative path)
POST /api/v1/khoa-hocs/19158f55-4f7a-404a-8ba9-a75de1130e57/submit-result   → 200  (resubmit)
POST /api/v1/khoa-hocs/19158f55-4f7a-404a-8ba9-a75de1130e57/approve-result  → 200  (positive path)
```

### Screenshots
- [r7-4-b11-r10-kh001-cho-duyet-kq-pd-view.png](r7-4-b11-r10-kh001-cho-duyet-kq-pd-view.png) — KH-001 CHO_DUYET_KQ trên PD view (2 button)
- [r7-4-b11-r10-kh001-hoan-thanh-after-approve.png](r7-4-b11-r10-kh001-hoan-thanh-after-approve.png) — Sau approve, KH-001 stepper full 6 ✓

### State BE final R10 (sau B7+B11)
```json
GET /api/v1/khoa-hocs?pageSize=20  total=7

KH-20260509-007: HOAN_THANH      v15  (R7.4.B7 R10)
KH-20260509-006: DA_DUYET        v7
KH-20260509-005: DA_DUYET        v7
KH-20260509-004: DA_DUYET        v7
KH-20260509-003: DA_DUYET        v7
KH-20260509-002: DA_DUYET        v7
KH-20260509-001: HOAN_THANH      v15  (R7.4.B11 R10 — đi qua đủ reject + resubmit + approve)
```

→ 2 KH HOAN_THANH (KH-001 + KH-007), 5 KH DA_DUYET dự phòng cho test khác.

---

## Findings R10

### 1. ✅ Workflow round-trip Reject → Resubmit → Approve hoạt động đầy đủ

KH-001 đã đi qua đủ vòng tròn `DA_KET_THUC → CHO_DUYET_KQ → DA_KET_THUC → CHO_DUYET_KQ → HOAN_THANH` qua 3 lần API call POST. Version tăng tuần tự 12 → 13 → 14 → 15 (4 mutations). Optimistic lock `version` field ổn định, không có conflict.

### 2. ⚠️ Spec drift Minor — Reject reason persist (giống pattern R7.4.B0)

GET KH-001 sau reject KHÔNG trả các field:
- `lyDoTuChoiKQ`
- `nguoiTuChoiKQId`
- `ngayTuChoiKQ`

Field `ghiChuPheDuyet` tồn tại nhưng giữ giá trị cũ từ R9 ("R9 workflow test - withdraw to add operational fields..."). Lý do từ chối R10 đã gửi qua request body — có thể BE persist trong audit log hoặc field khác không expose qua GET.

→ **Cần BA confirm:** spec FR-III-21 yêu cầu lưu `lyDoTuChoiKQ` riêng hay tái sử dụng `ghiChuPheDuyet`? Nếu cần riêng, BE phải add field. Nếu tái sử dụng, BE phải overwrite ghiChuPheDuyet. **Severity Minor** — defer Bug riêng.

### 3. ⚠️ FE button "Gửi duyệt KQ" hiển thị cho cả PD ở state DA_KET_THUC (chỉ verified visible, chưa test functional)

Khi PD ở KH-001 state DA_KET_THUC sau reject (chưa logout), FE render button "Gửi duyệt KQ" trong PD view (uid 41_1 trong snapshot R10 sau reject). Theo workflow design `submit-result` thuộc role CB_NV_TW, không phải PD. FE có thể đang render button theo state thay vì role permission.

**Test mode hiện tại:** Chỉ verified button rendered, KHÔNG click test (chuyển sang NV để giữ workflow đúng role). Nếu PD click submit-result, có thể trả 403 hoặc 200 (cần test sau).

→ **Severity Minor** — UX issue + potential authorization bug. Defer test riêng.

### 4. ✅ Modal Từ chối có UX tốt

Modal có:
- Title rõ
- Description giải thích destination state
- Field `Lý do từ chối *` required
- Counter chars `0 / 2000` real-time
- Validation `Vui lòng nhập lý do từ chối` khi empty
- Buttons "Quay lại" + "Từ chối" (Quay lại đóng modal, Từ chối submit)
- Close button ❌ ở góc

→ Không cần BA review.

### 5. ⚠️ AntD textarea quirk — fill_form không bind value

MCP `fill_form` không inject text vào `textarea` của AntD modal (textarea vẫn 0 chars + invalid=true sau fill). Workaround: click textbox → `type_text(...)`. Same issue như AntD DatePicker noted ở R7.4.B12 R9.

→ Tester technique note, không phải app bug.

---

## Cascade impact (post-R10 update)

| Task | Pre-R10 status | Post-R10 status | Reason |
|---|---|---|---|
| **R7.4.B11 Phê duyệt KQ KH** | 🟢 sẵn sàng (sau B7 R10) | ✅ FULL PASS positive + negative | Both paths verified qua UI |
| **R7.7.6 Functional 40 TC** | 🟢 sẵn sàng | 🟢 vẫn sẵn sàng | Không thay đổi |

---

## Lịch sử round

| Round | Date | Kết quả |
|---|---|---|
| R6-R8 | 2026-04 — 2026-05-08 | Block do KH chưa CHO_DUYET_KQ (cascade từ R7.4.B7 block) |
| R9 | 2026-05-09 | 🚫 BLOCKED do R7.4.B7 chưa unblock 4 runtime states |
| **R10** | **2026-05-10** | **✅ FULL PASS** — both positive (Duyệt KQ → HOAN_THANH) + negative (Từ chối KQ → DA_KET_THUC) đã verify qua UI sau R7.4.B7 R10 unblock |

---

*R10 verify | QA Automation via Claude Code MCP | 2026-05-10 01:42 — UI mode (per `feedback_qa_test_via_ui_not_api`)*
