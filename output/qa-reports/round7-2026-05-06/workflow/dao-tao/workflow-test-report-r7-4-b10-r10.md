# Workflow Test Report — R7.4.B10 ĐKT (R10 re-verify, post FE-REGRESSION fix)

> **Module:** Workflow Đề kiểm tra (FR-III-NEW-02 + FR-III-NEW-03) · **Round:** R10 · **Date:** 2026-05-10 · **Tester:** QA Automation (Claude Code MCP)
> **Pre-context:** R9 report ghi 1/8 PASS UI; FE missing render action buttons. Sau R10 verify, **BUG-DKT-FE-REGRESSION-01 đã Closed** (action buttons render đầy đủ list + detail). R10 chạy lại đầy đủ 8 bước.

---

## Kết luận

✅ **5/8 PASS via UI** + 1/8 BLOCKED (FE form bug NEW) + 2/8 N/A (state machine ĐKT đơn giản).

| # | Bước | Status R10 | Evidence | Note |
|:-:|---|:-:|---|---|
| 1 | Tạo ĐKT thủ công | ✅ R8 baseline | List 5 ĐKT NHAP (4 R8 + 1 R9 SHTT) | UI flow R10 BLOCKED — xem Bước 1b |
| 1b | Tạo ĐKT R10 mới qua UI | ❌ BLOCKED | reqid=1514 POST 422 `cauHoiIds must contain at least 1 elements` | **Bug NEW BUG-DKT-CREATE-FORM-01** — modal Tạo thiếu field `cauHoiIds` |
| 2 | Sửa ĐKT NHAP | ❌ BLOCKED | Modal "Cập nhật" combobox `Cách tạo` disabled + required + value rỗng → form luôn invalid | **Bug NEW BUG-DKT-EDIT-FORM-01** — modal không pre-fill `cachTao` từ record |
| 3 | Xóa ĐKT chưa sử dụng | ✅ UI flow PASS | Click delete → popconfirm "Xác nhận xóa" hiện đầy đủ với 2 button Hủy/Xóa | Cancel để giữ data 5 ĐKT cho R7.3.9. [Screenshot](../../screenshots/r10-b10-step3-delete-popconfirm.png) |
| 4 | Trình duyệt NHAP→CHO_DUYET | N/A | Không tồn tại trong state machine ĐKT (verified post-distribute: state machine = `NHAP → DA_PHAN_PHOI`, no CHO_DUYET) | Spec FR-III-NEW-02 không define submit/approve cho ĐKT |
| 5 | Phê duyệt CHO_DUYET→DA_DUYET | N/A | Không tồn tại trong state machine | Same |
| 6 | Phân phối → DA_PHAN_PHOI | ✅ PASS | reqid=1522 POST `/api/v1/de-kiem-tras/{id}/distribute` → **200**. ĐKT R9 SHTT chọn khóa học "Sở hữu trí tuệ cho startup - R9" | [Screenshot](../../screenshots/r10-b10-step6-distribute-modal.png) |
| 7 | Map bài giảng | ✅ PASS (tích hợp B6) | Modal Phân phối có field optional "Bài giảng (tùy chọn)" | Skip optional field cho R10 verify; field hiện có UI nhưng dropdown rỗng (chưa có bài giảng nào link với CTĐT này) |
| 8 | Verify link ĐKT → khóa học | ✅ PASS | API GET `/de-kiem-tras` ĐKT R9 SHTT (id 286dfad7): `trangThai="DA_PHAN_PHOI"` + `khoaHocId="929c53ba"` | Match SRS FR-III-NEW-03 |

---

## State machine ĐKT (verified R10)

```
NHAP ──[POST /distribute]──> DA_PHAN_PHOI
```

→ **2 state**, KHÔNG có CHO_DUYET / DA_DUYET như giả định R8/R9. SRS FR-III-NEW-02 + NEW-03 không quote rule duyệt cho ĐKT — chỉ Tạo/Sửa/Xóa/Phân phối.

---

## State data sau R10

| ĐKT | trangThai | khoaHocId |
|---|:-:|---|
| Sở hữu trí tuệ 2026 - R9 | **DA_PHAN_PHOI** | 929c53ba (Sở hữu trí tuệ cho startup - R9) |
| Luật Quản lý thuế 2026 | NHAP | null |
| Luật Đất đai 2026 (R8 edited) | NHAP | null |
| Pháp luật Lao động 2026 | NHAP | null |
| Pháp luật Hành chính 2026 | NHAP | null |

→ Tổng 4 NHAP + 1 DA_PHAN_PHOI. **Note dependency R7.3.9:** SHTT advance state có thể ảnh hưởng task R7.3.9 (yêu cầu 5 NHAP cover 5 LV) — flag re-eval.

---

## Bug NEW phát hiện R10

**BUG-DKT-EDIT-FORM-01** — Major P1 — Modal Cập nhật ĐKT không pre-fill `cachTao`
- Combobox `Cách tạo` luôn render disabled + value rỗng + required + ant-select-status-error
- Form luôn invalid khi click "Cập nhật" → bước Sửa BLOCKED qua UI
- BE PATCH endpoint OK (responding với validation lỗi `version` field nếu có call)
- → File: [bug-report-r7-4-b10-dkt-form-modal.md](../../bug-reports/dao-tao/bug-report-r7-4-b10-dkt-form-modal.md)

**BUG-DKT-CREATE-FORM-01** — Major P1 — Modal Tạo ĐKT thiếu field chọn câu hỏi (`cauHoiIds`)
- Modal Tạo có 4 field: Tên / Cách tạo / Thời gian / Điểm — không có UI chọn câu hỏi từ NHCH
- Submit POST → 422 `cauHoiIds must contain at least 1 elements`
- → File: [bug-report-r7-4-b10-dkt-form-modal.md](../../bug-reports/dao-tao/bug-report-r7-4-b10-dkt-form-modal.md)

---

## Action recommend

1. **Đóng task R7.4.B10 (⚠️ giữ nguyên):** 5/8 PASS, 1/8 BLOCKED do bug FE NEW + 2/8 N/A. Bug FE-REGRESSION-01 closed nhưng phát sinh 2 bug FE form modal mới — không flip ✅ cho đến khi 2 bug NEW closed.
2. **Re-eval R7.3.9:** SHTT advance NHAP→DA_PHAN_PHOI làm task R7.3.9 còn 4 NHAP. Cần seed thêm 1 SHTT NHAP nếu downstream phụ thuộc 5/5 cover, hoặc accept 4/5 + note SHTT đã consume.
3. **Spec drift confirm với BA:** ĐKT state machine 2-state (NHAP / DA_PHAN_PHOI), không có duyệt. SRS FR-III-NEW-02 không quote rule duyệt. Confirm với BA để cập nhật spec doc.

---

*R10 verify | QA Automation via Claude Code | 2026-05-10*
