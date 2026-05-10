# Seed Checklist — Bài giảng (R7.3.10 — R9 light verify)

**Ngày:** 2026-05-09 20:08–20:15 • **Tài khoản:** `cb_nv_tw_02` (CB_NV_TW) • **Trạng thái mong đợi:** `congKhai=false`
**Màn:** SCR-III-07 — Kho tài liệu / Bài giảng • **Đường dẫn:** `/dao-tao/bai-giang/danh-sach`
**SRS:** [FR-III-07 — Quản lý bài giảng](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-07)
**Round:** R9 — light verify (state đã comprehensive R8, không add record mới).

---

## Kết quả: ✅ XONG 8/8 (verify state R8 stable, no R9 add)

R9 verify state R8 vẫn comprehensive. KHÔNG add record mới vì:
- R8 đã PASS 8/8 cover 3 loại + 8 LV — không có gap-fill cần thiết
- BG entity KHÔNG có state machine `KICH_HOAT/VO_HIEU_HOA` (chỉ có `congKhai` boolean), nên không cần re-test state transition
- R8 noted FE form schema drift (BE dùng `fileUrl + dungLuong` flat thay vì SRS `file_bai_giang` nested) — R9 không re-test FE form vì cần dev fix BE-spec mismatch trước (BUG-BG-001)

**State BE final R9:** 8 records — 5 VIDEO + 1 SLIDE + 2 PDF, cover 8 LV (Doanh nghiệp + Dân sự + Hành chính + Đất đai + SHTT + Thương mại + Lao động + Thuế). All `congKhai=false` (chưa publish).

---

## Bảng dữ liệu seed (R8 stable, R9 verify)

| # | Tên bài giảng | Loại | Dung lượng | LV inferred | congKhai | Round |
|:-:|---------------|------|:---:|------|:--:|:--:|
| 1 | Bài giảng 09 - Luật Doanh nghiệp 2020 cập nhật (PDF) | PDF | 5.4 MB | Doanh nghiệp | false | R8 |
| 2 | Bài giảng 08 - Bộ luật Dân sự 2015 (PDF) | PDF | 4.6 MB | Dân sự | false | R8 |
| 3 | Bài giảng 07 - Quản lý Hành chính DN (Slide) | SLIDE | 2.4 MB | Hành chính | false | R8 |
| 4 | Bài giảng 06 - Đất đai cơ bản | VIDEO | — | Đất đai | false | R7 |
| 5 | Bài giảng 05 - Sở hữu trí tuệ | VIDEO | — | SHTT | false | R7 |
| 6 | Bài giảng 04 - Hợp đồng thương mại | VIDEO | — | Thương mại | false | R7 |
| 7 | Bài giảng 02 - Luật Lao động cơ bản | VIDEO | — | Lao động | false | R7 |
| 8 | Bài giảng 03 - Thuế GTGT thực hành | VIDEO | — | Thuế | false | R7 |

**Tổng:** 8 records — 3 loại đầy đủ + 8 LV cover.

### Verify per-filter

| Filter | Expected | Actual |
|---|:--:|:--:|
| Total BG | ≥8 | ✅ 8 |
| Loại VIDEO | ≥1 | ✅ 5 |
| Loại SLIDE | ≥1 | ✅ 1 |
| Loại PDF | ≥1 | ✅ 2 |
| LV coverage | ≥5 | ✅ 8 |

---

## R9 verify steps

1. ✅ API GET `/api/v1/bai-giangs?pageSize=20` → 8 records, byLoai={PDF:2, SLIDE:1, VIDEO:5}
2. ✅ Navigate UI SCR-III-07 → list render 8 records đầy đủ (file icon + tên + dung lượng + ngày tạo) match API
3. ⏸ Skip create flow R9 — defer chờ dev fix BUG-BG-001 (BE schema mismatch) trước

---

## Issues encountered R9

**Login rate-limit:** Sau ~10 lần login switch account/relogin trong 15-20 phút (R7.4.B0 verify + R7.3.6/R7.3.5 seed + R7.3.8/R7.3.9), POST `/auth/login` trả `net::ERR_ABORTED` (BE ThrottlerException 429 cooldown 60s) khi cố session restore cho R7.3.10 phase 2. Match BUG-AUTH-OTP-02 R8 lần 2 confirmed by-design rate-limit. Workaround: chờ 60s + retry.

→ Không log bug mới. Document for memory.

---

## Bug tracking

- **BUG-BG-001** Major (R8 logged) — BE missing validation `fileBaiGiang/urlYoutube` theo `loaiTaiLieu` (vi phạm SRS FR-III-07 Inputs row 4 + Error E2). 0/1 đóng. R9 không re-test (cần dev fix trước).

---

## Ảnh chụp

- [List 8 BG R8 screenshot — vẫn match R9 state](r7-3-10-bai-giang-list-8-final.png) — R8 evidence reused, state không đổi R9.

---

*2026-05-09 20:15 — QA chạy bằng Chrome DevTools MCP via Claude Code*
