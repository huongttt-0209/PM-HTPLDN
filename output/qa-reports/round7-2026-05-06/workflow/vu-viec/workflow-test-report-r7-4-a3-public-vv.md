# Workflow Test Report — R7.4.A3-PUBLIC (FR-V.I-NEW-05)

> **Module:** Vụ việc HTPL — Quản lý công khai VV lên Cổng PLQG · **Round:** R13 · **Date:** 2026-05-10 03:00:00 → 03:10:00 · **Tester:** Claude Code (Opus 4.7)
> **Spec:** [`srs-update-2026-5-5/srs-fr-05-vu-viec.md`](../../../../input/srs-update-2026-5-5/srs-fr-05-vu-viec.md) §FR-V.I-NEW-05 (dòng 1357-1456) + SCR-V.I-03 dòng 1787-1788
> **Bug:** [`../../bug-reports/vu-viec/Pass-bug-report-r7-4-a3-public-vv.md`](../../bug-reports/vu-viec/Pass-bug-report-r7-4-a3-public-vv.md) — 0/1 đóng (Critical:1)

---

## Verdict

🚫 **BLOCKED** — Toàn bộ feature FR-V.I-NEW-05 chưa được implement (BE schema thiếu 5 columns CR-01 + 8 endpoint candidates đều 404 + UI no [Công khai] button).

## Accounts

- `cb_pd_tw_05` (CB_PD_TW cấp 05) — đúng role spec dòng 1787 "CB Phê duyệt cùng cấp".
- `cb_nv_tw_05` (CB_NV_TW cấp 05) — advance VV-008 đến DA_DUYET state.

## Pool VV target ngày 2026-05-10

| State | Count | Mã VV |
|-------|:-----:|-------|
| DA_DUYET | 1 (sau test) | VV-BTP-TW-20260509-008 (advanced R13 03:01) |
| HOAN_THANH | 0 | — |
| DA_DANH_GIA | 1 | VV-BTP-TW-20260509-009 (R12 ngoài scope test này) |

## Test scope (per todo R7.4.A3-PUBLIC)

| # | Test scenario | Status | Note |
|---|--------------|:------:|------|
| 1 | Self-loop **Công khai** trên `DA_DUYET` (cong_khai 0→1) | 🚫 BLOCKED | UI no button + BE 404 + schema missing |
| 2 | Self-loop **Hủy công khai** trên `DA_DUYET` (cong_khai 1→0, lý do ≥20 ký tự) | 🚫 BLOCKED | Cần (1) trước |
| 3 | Self-loop **Công khai** trên `HOAN_THANH` (cong_khai 0→1) | 🚫 BLOCKED | Cần VV HOAN_THANH state + (1) |
| 4 | Self-loop **Hủy công khai** trên `HOAN_THANH` (cong_khai 1→0) | 🚫 BLOCKED | Cần (3) trước |
| 5 | Whitelist BR-PUBLIC-04 (9 fields whitelist + 6 fields blocked NĐ13/2023) | 🚫 BLOCKED | Cần (1) trước |
| 6 | Badge "Đã công khai" hiển thị khi cong_khai=1 (header + table list) | 🚫 BLOCKED | Cần (1) trước |
| 7 | Permission BR-AUTH-05: chỉ CB_PD cùng cấp được phép | 🚫 BLOCKED | Cần feature build trước |
| 8 | Toast notification DN khi công khai/hủy công khai | 🚫 BLOCKED | Cần (1) trước |

## Walk path để có VV DA_DUYET

VV-008 walked qua đầy đủ B1-B5 R13:

| Bước | State trước | State sau | Method | Account |
|------|------------|-----------|--------|---------|
| Trình phê duyệt | DANG_XU_LY v6 (sau B5a) | CHO_PHE_DUYET v7 | UI MCP modal | cb_nv_tw_05 |
| Phê duyệt | CHO_PHE_DUYET v7 | **DA_DUYET v8** | UI MCP modal | cb_pd_tw_05 |

API verify final: `{trangThai:"DA_DUYET", version:8, nguoiDuyetId:"a0515759-...", ngayDuyet:"2026-05-09T20:01:43.531Z"}`.

## Probe BE endpoints (8 candidates)

| Endpoint name | Status | Response |
|---------------|:------:|----------|
| POST `/cong-khai` | 404 | ERR-SYS-00-04-01 "Cannot POST" |
| POST `/huy-cong-khai` | 404 | — |
| POST `/publish` | 404 | — |
| POST `/unpublish` | 404 | — |
| POST `/dang-tai` | 404 | — |
| POST `/mo-cong-khai` | 404 | — |
| POST `/go-cong-khai` | 404 | — |
| POST `/cong-bo` | 404 | — |

## Schema VU_VIEC fields gap

5 cột CR-01 (SRS dòng 2075-2079) đều thiếu:
- `cong_khai` boolean ✗
- `thoi_gian_dang_tai` datetime ✗
- `mo_ta_cong_khai` text long ✗
- `file_dinh_kem_cong_khai` file[] ✗
- `anh_dai_dien` ✗

Full key list: 45 keys, không có key nào match `cong_khai|thoi_gian_dang_tai|mo_ta_cong_khai|file_dinh_kem_cong_khai|anh_dai_dien`.

## Verify spec lock

NotebookLM HTPLDN id `a4ae45bf-cea0-4325-8fee-b1e0be702cf2` + grep SRS local đều confirm FR-V.I-NEW-05 trong v3.5 scope sync 2026-05-06:
- `srs-fr-05-vu-viec.md:7` "21 FR ... + FR-V.I-NEW-05"
- `srs-fr-05-vu-viec.md:1357-1456` full spec section
- `srs-v3.5.md:1475-1479` entity VU_VIEC 5 cols CR-01

→ Spec đã chốt R7. Feature gap = bug Critical, escalate dev.

## Đề xuất unlock

1. Dev BE migration thêm 5 columns CR-01 vào VU_VIEC schema.
2. Dev BE implement 2 endpoints `POST /cong-khai` + `POST /huy-cong-khai` theo spec dòng 1396-1419.
3. Dev FE thêm action button [Công khai] / [Hủy công khai] + 2 modals (form công khai + lý do hủy ≥20 ký tự).
4. QA re-test R14 sau dev confirm fix.

## Cascade impact

- **R7.4.A3-PUBLIC** todo: BLOCKED toàn task — không có UI/BE/schema để test.
- **R7.7.3-PRIVACY** todo: BLOCKED cascade — cần ≥1 VV cong_khai=1 cho 2 TC P0 privacy NĐ 13/2023.
- **R7.5.x dashboard/báo cáo** (nếu có metric "VV công khai"): false zero data.

*2026-05-10 03:10:00 — R7.4.A3-PUBLIC test BLOCKED, log BUG-VV-PUBLIC-01 Critical, escalate dev build feature.*
