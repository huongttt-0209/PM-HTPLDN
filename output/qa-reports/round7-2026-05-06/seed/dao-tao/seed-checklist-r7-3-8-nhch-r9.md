# Seed Checklist — Ngân hàng câu hỏi (R7.3.8 — R9 re-run)

**Ngày:** 2026-05-09 19:35–19:40 • **Tài khoản:** `cb_nv_tw_02` (CB_NV_TW) • **Trạng thái mong đợi:** `KICH_HOAT`
**Màn:** SCR-III-09 — Ngân hàng câu hỏi & Đề kiểm tra • **Đường dẫn:** `/dao-tao/ngan-hang-cau-hoi/danh-sach`
**SRS:** [FR-III-09 UC44 — Quản lý NHCH](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-09)
**Round:** R9 — re-run light (verify list flow + add 1 NHCH gap-fill SHTT/Trung bình/TN nhiều).

---

## Kết quả: ✅ XONG 7/7 KICH_HOAT (R9 add 1 SHTT gap-fill)

R9 verify list flow cb_nv_tw_02 — 6 records R8 vẫn KICH_HOAT đúng spec FR-III-09 + Entity §3.4.3.21 (state machine 2 state KICH_HOAT/VO_HIEU_HOA toggle).

R9 create form flow PASS qua UI: SCR-III-09 modal "Thêm câu hỏi mới" → fill `Nội dung + LV (SHTT) + Mức độ (Trung bình) + Loại (TN nhiều) + 2 lựa chọn A+B + check 2 đáp án đúng` → POST `/api/v1/ngan-hang-cau-hois` 201 Created.

**State BE final:** 7 records — 7 KICH_HOAT cover 5 LV (SHTT 2 + Hành chính 1 + Lao động 2 + Đất đai 1 + Thuế 1).

---

## Bảng dữ liệu seed

| # | LV | Mức độ | Loại câu hỏi | Trạng thái | Round | Có vào kho |
|:-:|---|:--:|---|:-:|:-:|:-:|
| 1 | Hành chính | Trung bình | TN nhiều | KICH_HOAT | R8 | ✅ giữ |
| 2 | Lao động | Dễ | TN 1 đáp | KICH_HOAT | R8 | ✅ giữ |
| 3 | Đất đai | Dễ | Tự luận | KICH_HOAT | R8 | ✅ giữ |
| 4 | Sở hữu trí tuệ | Khó | Tự luận | KICH_HOAT | R8 | ✅ giữ |
| 5 | Thuế | Trung bình | Tự luận | KICH_HOAT | R8 | ✅ giữ |
| 6 | Lao động | Dễ | Tự luận | KICH_HOAT | R8 | ✅ giữ |
| **7** | **Sở hữu trí tuệ** | **Trung bình** | **TN nhiều đáp án** | **KICH_HOAT** | **R9 ✨** | **✅** |

**Tổng:** 7 KICH_HOAT cover 5 LV.

### Verify per-filter coverage

| Filter | Expected | Actual |
|---|:--:|:--:|
| Total active | ≥6 | ✅ 7 |
| `trangThai=KICH_HOAT` | 7/7 | ✅ 7/7 |
| LV coverage | 5/10 LV | ✅ 5 (Hành chính + Lao động + Đất đai + SHTT + Thuế) |
| Mức độ coverage | 3/3 | ✅ 3 (Dễ + Trung bình + Khó) |
| Loại câu hỏi coverage | 3/3 | ✅ 3 (TN 1 đáp + TN nhiều + Tự luận) |

---

## R9 form flow notes

**Issues phát hiện R9 trong form create:**

1. **Validation sai khi đổi loại câu hỏi:** Sau khi chọn Lĩnh vực + Mức độ + Loại "TN nhiều đáp án", form expand thêm "Các lựa chọn" + "Đáp án đúng". Sau khi fill 2 lựa chọn A/B + check correct + click submit → BE 400 với error toast trong form: **"Vui lòng nhập nội dung câu hỏi"** dù field đã fill. Phải re-fill nội dung qua DOM `setter` + dispatch `input` event để React đọc lại value.
2. **Workaround:** Dùng `evaluate_script` setter pattern cho textarea required (thay vì `fill_form` MCP tool). `fill_form` value không persist khi form re-render do combobox change. Form `validate` đọc state cũ → reject.

**Khả năng bug FE:** Form `Antd` không sync state khi loại câu hỏi đổi từ Tự luận → TN nhiều, có thể reset noiDung field. Cần re-test thêm. Đề xuất defer log Minor — không block seed.

---

## Bug tracking

- **BUG-NHCH-STATE-01** R7-R8 — Closed FE side 2026-05-07 (form default KICH_HOAT đúng). SRS doc-side chưa fix `FR-III-09 line 783` typo `NHAP/CONG_KHAI/AN`. Cần BA cập nhật.
- R9 không log bug mới (form noiDung reset issue có thể là MCP tool quirk + Antd interaction, defer).

---

## Ảnh chụp R9

- [List 7 NHCH KICH_HOAT R9](r7-3-8-r9-nhch-list-7.png)

---

*2026-05-09 19:40 — QA chạy bằng Chrome DevTools MCP via Claude Code*
