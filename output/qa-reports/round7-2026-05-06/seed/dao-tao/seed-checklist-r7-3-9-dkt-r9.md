# Seed Checklist — Đề kiểm tra (R7.3.9 — R9 re-run gap-fill)

**Ngày:** 2026-05-09 19:58–20:05 • **Tài khoản:** `cb_nv_tw_02` (CB_NV_TW) • **Trạng thái mong đợi:** `NHAP`
**Màn:** SCR-III-09 tab "Đề kiểm tra" • **Đường dẫn:** `/dao-tao/ngan-hang-cau-hoi/danh-sach?tab=de-kiem-tra`
**SRS:** [FR-III-NEW-01 line 1324 — Tạo đề kiểm tra](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-new-01)
**Round:** R9 — gap-fill SHTT (R8 đã xoá ĐKT SHTT do FR-III-NEW-02 CRUD test trong R7.4.B10).

---

## Downstream consumer × filter

| Task downstream | Filter | Số record cần | State | Status |
|---|---|---|---|:--:|
| R7.4.B10 — Workflow ĐKT FR-III-NEW-02 CRUD | NHAP để CRUD | ≥1 NHAP | NHAP | ✅ |
| R7.4.B10 — FR-III-NEW-03 phân phối ĐKT vào KH | ≥1 ĐKT match LV của KH | NHAP/DA_DUYET | ✅ 5 LV |
| R7.7.6 — Functional 40 TC ĐKT | All states cover | NHAP cover 5 LV | ✅ |

---

## Kết quả: ✅ XONG 5/5 NHAP cover 5 LV (R9 add 1 SHTT)

R9 add 1 ĐKT THU_CONG mode cấp SHTT (link 1 NHCH SHTT-Trung bình-TN nhiều R9 từ R7.3.8). POST `/api/v1/de-kiem-tras` 201 Created.

**State BE final:** 5 records — 5 NHAP cover 5 LV (Hành chính + Lao động + Đất đai + SHTT + Thuế). 1 NHCH/đề.

---

## Bảng dữ liệu seed

| # | Tên đề | LV | Số câu | Thời gian (phút) | Trạng thái | Round |
|:-:|--------|----|:--:|:--:|:--:|:--:|
| 1 | ĐKT cuối khóa - Pháp luật Hành chính 2026 | Hành chính | 1 | 30 | NHAP | R8 |
| 2 | ĐKT cuối khóa - Pháp luật Lao động 2026 | Lao động | 1 | 30 | NHAP | R8 |
| 3 | ĐKT cuối khóa - Luật Đất đai 2026 (R8 edited) | Đất đai | 1 | 45 | NHAP | R8 (edited R7.4.B10) |
| 4 | ĐKT cuối khóa - Luật Quản lý thuế 2026 | Thuế | 1 | 30 | NHAP | R8 |
| **5** | **ĐKT cuối khóa - Sở hữu trí tuệ 2026 - R9** | **SHTT** | **1** | **30** | **NHAP** | **R9 ✨** |

**Tổng:** 5 NHAP cover 5/10 LV (Hành chính + Lao động + Đất đai + SHTT + Thuế).

### Verify per-filter

| Filter | Expected | Actual |
|---|:--:|:--:|
| Total NHAP | ≥5 | ✅ 5 |
| LV coverage | 5/10 | ✅ 5 (Hành chính + Lao động + Đất đai + SHTT + Thuế) |
| 1 NHCH/đề | ≥1 câu | ✅ all 5 đề có 1 câu |
| State 100% NHAP | 5/5 | ✅ 5/5 |

---

## R9 form flow notes

**Form pattern:** Tạo đề kiểm tra modal yêu cầu:
- Tên đề (required)
- Cách tạo (THU_CONG hoặc TU_DONG)
- Thời gian làm bài (1-480 phút)
- Điểm đạt (0-10)
- Sau chọn THU_CONG → render section "Danh sách câu hỏi (ID)" với UUID input picker

**Issues phát hiện R9:**

1. **UI thiếu picker chọn câu hỏi từ list:** Modal yêu cầu paste UUID câu hỏi raw vào input field thay vì có dropdown/picker từ danh sách NHCH KICH_HOAT. → User experience kém: cần biết UUID câu hỏi từ trước hoặc copy từ NHCH list. Đề xuất defer log Minor (FE enhancement). Workaround: dùng API GET `/ngan-hang-cau-hois` để lấy id rồi paste.
2. **DOM setter quirk persist** — same issue với R7.3.8: `fill_form` MCP tool không persist value khi form re-render do combobox change. Workaround dùng `evaluate_script` setter pattern + dispatch input event.

---

## Bug tracking

- **BUG-DKT-FE-01** R7-R8 — Closed FE side 2026-05-07 (form save state đúng).
- R9 không log bug mới (UI UX picker UUID là enhancement, defer).

---

## Ảnh chụp

- [List 5 ĐKT NHAP cover 5 LV — R9](r7-3-9-r9-dkt-list-5.png)

---

*2026-05-09 20:05 — QA chạy bằng Chrome DevTools MCP via Claude Code*
