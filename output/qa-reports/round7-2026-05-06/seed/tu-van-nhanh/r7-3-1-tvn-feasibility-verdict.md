# R7.3.1.TVN — Feasibility Verdict (Block + Recommend re-classify)

**Ngày:** 2026-05-09 12:48:00 → 12:55:00 • **Tester:** QA huongttt
**Account dùng:** `cb_nv_tw_02` (UI MCP login + OTP `666666`)
**SRS ref:** [srs-fr-13-tv-nhanh.md](../../../../../input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md) line 53, 263-264, 287-289, 802-805

---

## Verdict

🚫 **BLOCK theo SPEC** — R7.3.1.TVN không thể chạy đúng spec FR-13 trong build hiện tại. Cần Cổng PLQG endpoint deploy + DN-side UI button "Chuyển sang TV thủ công".

> **Cập nhật 2026-05-09 13:08:00 (after user prompt "kiểm tra trên web có data ko"):** Đã probe data trên web — kết luận giữ nguyên BLOCK theo spec, có thêm 1 candidate bug về form drawer expose option "Từ Tư vấn nhanh".

> **Re-test 2026-05-09 17:05:30 R8 (after dev fix claim):**
> - ✅ BUG-HD-FORM-001 đóng — form drawer chỉ còn 4 options (DVC + HE_THONG_KHAC + TRUC_TIEP + CONG_PLQG), KHÔNG còn TVN_BRIDGE. Filter list vẫn 5 options đúng spec line 1037.
> - 🚫 ESCALATE flow vẫn BLOCK — CB UI re-walk 2/2 state (Mới TVN-QA-20260506-0001 + Đã gợi ý TVN-QA-20260425-0021): vẫn 0 button ESCALATE. Action button duy nhất: "Quay lại danh sách" + "Gửi trả lời".
> - 🚫 Inbound data unchanged — `GET /api/v1/hoi-daps` 13 records, **0 TVN_BRIDGE**, 0 record có `tuVanNhanhGocId`. `GET /api/v1/tu-van-nhanhs` 50 phiên, **0 phiên có hoiDapId**. Cổng PLQG endpoint vẫn chưa active.
> - **Verdict:** R7.3.1.TVN vẫn 🚫 do thiếu Cổng PLQG endpoint deploy (R7.6.3 ⏳). Block list rút bớt 1 item (HD-FORM-001 đóng).

---

## Mô tả task gốc

> **R7.3.1.TVN 🆕** Seed phiên TV nhanh ESCALATE → HD `kenh=TVN_BRIDGE` qua UI FR-13.

Tester walk UI flow FR-13 trên Cổng PLQG / chuyên trang DN: chọn `kenh_tu_van=TV_THU_CONG` → hệ thống auto-tạo HD `kenh_tiep_nhan=TVN_BRIDGE` để CB tiếp nhận; phiên TVN giữ lịch sử AI gợi ý.

---

## 4 evidence point block

### 1. CB-side UI KHÔNG có button ESCALATE (xác minh UI MCP)

**State `Mới` (TVN-QA-20260506-0001)** — ảnh [r7-3-1-tvn-cb-detail-no-escalate.png](r7-3-1-tvn-cb-detail-no-escalate.png):
- Detail page chỉ có heading + stepper 5 state (Mới/Đang tìm kiếm/Đã gợi ý/CB trả lời/Hoàn thành) + info card (Mã phiên/Kênh/Câu hỏi).
- Action button duy nhất: **"Quay lại danh sách"**.
- DOM scan toàn body (811 chars): không có chuỗi `escalate`, `chuyển hỏi đáp`, `chuyển nhóm`, `chuyển sang TV thủ công`.

**State `Đã gợi ý` (TVN-QA-20260425-0020)** — ảnh [r7-3-1-tvn-cb-da-goi-y-only-gui-tra-loi.png](r7-3-1-tvn-cb-da-goi-y-only-gui-tra-loi.png):
- Detail có info DN + Top 5 gợi ý + textarea "Soạn trả lời".
- Action button duy nhất: **"Gửi trả lời"** (advance state DA_GOI_Y → CB_TRA_LOI theo SM-TVNHANH, không phải ESCALATE).

→ CB-side KHÔNG bao giờ chủ động tạo HD `TVN_BRIDGE`. Vai trò ESCALATE thuộc DN-side per SRS.

### 2. SRS xác nhận ESCALATE = DN-side trên Cổng PLQG

- SRS line 53: `B -->|TV Thủ công| D[Chuyển Nhóm II UC12]` — flow DN-side bấm "TV Thủ công".
- SRS line 263-264:
  > Nếu TV thủ công -> chuyển nhóm II (UC12 tiếp nhận)
  > DN chuyển kênh: 'Chuyển sang TV thủ công' -> giữ toàn bộ lịch sử
- SRS line 287-289 (Acceptance Criteria): DN chọn TV thủ công trên Cổng PLQG → chuyển nhóm II.
- SRS SM-TVNHANH (line 802-805): 6 state `MOI / DANG_TIM_KIEM / DA_GOI_Y / CB_TRA_LOI / HOAN_THANH / HET_HAN` — KHÔNG có state `ESCALATE`.

### 3. DN-side không khả dụng — Cổng PLQG chưa deploy + không có DN account test

- `input/users.csv` (58 rows) chỉ có `loai_tai_khoan ∈ {CB, QTHT}`, KHÔNG có account DN.
- Cổng PLQG endpoint chờ deploy theo task `R7.6.3 ⏳` ([todo-tv-nhanh.md](../../../../tasks/todo-tv-nhanh.md#r7-6-3)).
- DN-side chuyên trang TVN với button "Chuyển sang TV thủ công" yêu cầu Cổng PLQG → unavailable.

### 4. 0 HD record với `kenh_tiep_nhan=TVN_BRIDGE` + 0 link TVN ↔ HD

Verify supporting evidence:
```
GET /api/v1/hoi-daps?pageSize=50            → 13 records
  kenhTiepNhan distribution: TRUC_TIEP=5, HE_THONG_KHAC=4, CONG_PLQG=2, DVC=2, TVN_BRIDGE=0
  HD model schema: id, maHoiDap, linhVucId/Ten, kenhTiepNhan, trangThai, tenNguoiGui,
                   nguoiPhanCongId, deadline, ngayTiepNhan, mucDoCanhBao, noiDungTomTat, ngayTao
                   → KHÔNG có field link đến TVN session

GET /api/v1/tu-van-nhanhs?pageSize=100      → 50 phiên
  kenhTuVan distribution: TV_NHANH=40, TV_THU_CONG=10
  trangThai distribution: MOI=8, DANG_TIM_KIEM=6, DA_GOI_Y=9, CB_TRA_LOI=11,
                          HOAN_THANH=12, HET_HAN=4
  hoiDapId field: 0/50 phiên có link → KHÔNG phiên nào đã ESCALATE
  HOAN_THANH state có hoiDapId: 0/12
  TV_THU_CONG state có hoiDapId: 0/10
```

Inbound flow chưa từng được kích hoạt trên môi trường này. 10 phiên `kenhTuVan=TV_THU_CONG` có sẵn nhưng **KHÔNG link đến HD**. Khẳng định 2 entity (TVN ↔ HD) hoàn toàn độc lập trong DB hiện tại.

### 5. Phát hiện thêm: HD form drawer expose option "Từ Tư vấn nhanh" — vi phạm smoke spec

UI `/hoi-dap` → button **[+ Thêm mới]** → drawer "Thêm mới hỏi đáp" → combobox "Kênh tiếp nhận" hiển thị **5 options** trong đó có **"Từ Tư vấn nhanh"** (= TVN_BRIDGE). Ảnh [r7-3-1-tvn-hd-form-tu-tvn-option.png](r7-3-1-tvn-hd-form-tu-tvn-option.png).

**Vi phạm spec:** [output/smoke/6.2-sm-hoidap.md line 121](../../../../smoke/6.2-sm-hoidap.md):
> Verify cán bộ KHÔNG nhập tay được kênh TVN_BRIDGE (dropdown form ẩn)

→ Đây là **bug candidate riêng** (UI form drawer không filter ẩn TVN_BRIDGE). Severity Major (cho phép CB tạo HD bypass FR-13 inbound). Log riêng — KHÔNG block task R7.3.1.TVN, mà thay đổi recommendation:

**Option Bypass (nếu user accept):** seed 1 HD `kenhTiepNhan=TVN_BRIDGE` qua form Thêm mới. Đáp ứng deliverable đếm số ≥1 HD TVN_BRIDGE, nhưng:
- ❌ KHÔNG đúng intent FR-13 ESCALATE (data không có link đến TVN session vì HD model thiếu field link)
- ❌ Tạo data unrealistic (CB tạo manual ≠ inbound từ Cổng PLQG)
- ❌ Đồng thời tester cần log bug "form không ẩn option"

---

## Khung quyết định (memory rule check)

| Rule | Áp dụng task này? |
|---|---|
| `feedback_qa_block_must_seed_data` (block do thiếu data → tự seed) | ❌ Không áp dụng — block do thiếu **UI feature DN-side + endpoint Cổng PLQG**, không phải thiếu data QA seed được. |
| `feedback_block_unlock_analysis` (phân tích root cause + chạy task unlock) | ✅ Đã làm — root cause = R7.6.3 (Cổng PLQG deploy + DN-side UI). Task unlock outside QA scope (dev/infra). |
| `feedback_test_method_ui_only` (UI MCP only) | ✅ Đã dùng UI MCP — login + navigate + click + DOM scan. API call chỉ supporting evidence (HD count). |

---

## Đề xuất update todo.md (chờ user approve)

```diff
- 🟢 **R7.3.1.TVN** 🆕 Seed phiên TV nhanh ESCALATE → HD `kenh=TVN_BRIDGE` qua UI FR-13 `[need: [R7.6.2](todo-tv-nhanh.md#r7-6-2) (tv-nhanh)]`
-   - **Cần:** [R7.6.2](todo-tv-nhanh.md#r7-6-2) (tv-nhanh) ⚠️ (walk UI FR-13 ESCALATE, không POST API)
+ 🚫 **R7.3.1.TVN** 🆕 Seed phiên TV nhanh ESCALATE → HD `kenh=TVN_BRIDGE` qua UI FR-13 `[block: Cổng PLQG endpoint chưa deploy]`
+   - **Cần:** Cổng PLQG endpoint deploy (R7.6.3 ⏳) · DN account test khả dụng · CB-side hoặc DN-side có UI ESCALATE
+   - **Kết quả:** 🚫 BLOCK — CB-side UI 2/2 state kiểm tra (Mới + DA_GOI_Y) không có button ESCALATE. 0 HD `TVN_BRIDGE`. [r7-3-1-tvn-feasibility-verdict.md](../output/qa-reports/round7-2026-05-06/seed/tu-van-nhanh/r7-3-1-tvn-feasibility-verdict.md)
```

---

## Ảnh chụp

- [r7-3-1-tvn-cb-detail-no-escalate.png](r7-3-1-tvn-cb-detail-no-escalate.png) — CB detail state `Mới`, chỉ có "Quay lại danh sách"
- [r7-3-1-tvn-cb-da-goi-y-only-gui-tra-loi.png](r7-3-1-tvn-cb-da-goi-y-only-gui-tra-loi.png) — CB detail state `Đã gợi ý`, chỉ có "Gửi trả lời"
- [r7-3-1-tvn-hd-form-tu-tvn-option.png](r7-3-1-tvn-hd-form-tu-tvn-option.png) — HD form drawer "Thêm mới hỏi đáp" combobox Kênh tiếp nhận hiển thị 5 options bao gồm "Từ Tư vấn nhanh" (vi phạm smoke 6.2 line 121)

---

*2026-05-09 12:55:00 — QA verify 100% UI MCP qua Chrome DevTools, 2 state CB-side + 1 API supporting evidence + 4 SRS line ref.*
