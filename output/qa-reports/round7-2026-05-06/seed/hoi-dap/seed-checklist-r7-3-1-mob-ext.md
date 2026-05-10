# Seed Checklist — Mẫu Mô hình B (R7.3.1.MoB R8 extend)

> ✅ **R8 extend 2026-05-09 12:18:00:** Seed thêm 3 MPH Mô hình B qua **UI Modal SCR-II-NEW-02** với 3 acc cấp `_04` (cover thêm 3 LV chưa có Mẫu cấp Bộ ngành / Địa phương).
>
> **Phương thức:** UI thuần — `Click "+ Thêm mới"` → fill name + select Lĩnh vực + Loại mẫu = "Mẫu phản hồi" + textarea nội dung → click "Tạo mới". KHÔNG POST API direct.

**Ngày:** 2026-05-09 12:00:00 → 12:18:00 • **Tester:** QA huongttt
**Màn:** SCR-II-NEW-02 — Mẫu phản hồi (FR-II-NEW-02 Mô hình B Hybrid 2 tầng)
**SRS:** [srs-fr-02-hoi-dap.md FR-II-NEW-02](../../../../input/srs-update-2026-5-5/srs-fr-02-hoi-dap.md)

---

## Pre-flight: account state mismatch + reset

**Phát hiện:** CSV `input/users.csv` claim 3 acc `_04` mật khẩu `Secret@123 + HOAT_DONG`, nhưng BE login 401 cho cả `tw_04` + `bn_04` + `dp_04`. State acc HOAT_DONG đã verify qua QTHT search (8/8 acc `_04` HOAT_DONG, không phải CHO_KICH_HOAT). Root cause: BE password lưu reset từ Claude session trước, CSV chỉ là doc.

**Fix:** Reset cả 3 acc về `Secret@123` qua **MailHog UI** (http://103.172.236.130:8025) — KHÔNG curl.

| Acc | Forgot-pwd submit | Mail token | Reset link UI | Login verify |
|---|---|---|---|---|
| `cb_nv_tw_04` | 12:09:42 ✅ | `01f3577c-edc9-443f-b3fd-6bd95d2679b5` | `:3000/reset-password?token=...` (BUG-005 add :3000 manual) | 200 ✅ |
| `cb_nv_bn_04` | 12:11:14 ✅ | `39d52d6d-e41f-45b9-b862-69f8433cfd89` | `:3000/reset-password?token=...` | 200 ✅ |
| `cb_nv_dp_04` | 12:13:44 ✅ | `ce3ef0f9-8165-4a5f-a0e1-a1d09ab657cf` | `:3000/reset-password?token=...` | 200 ✅ |

---

## Seed result

| # | Mã / Tên mẫu | Lĩnh vực | Loại mẫu | Phạm vi (auto-fill) | Tác giả (auto) | Acc seed |
|---|---|---|---|---|---|---|
| 13 | Mẫu phản hồi HD - Hành chính (R8 ext TW) | Hành chính | Mẫu phản hồi | **Trung ương** | Cục Bổ trợ tư pháp - Bộ Tư pháp | `cb_nv_tw_04` |
| 14 | Mẫu phản hồi BN-BKH - Đầu tư (R8 ext) | Đầu tư | Mẫu phản hồi | **Bộ ngành** | Bộ Kế hoạch và Đầu tư | `cb_nv_bn_04` |
| 15 | Mẫu phản hồi DP-AG - Dân sự (R8 ext) | Dân sự | Mẫu phản hồi | **Địa phương** | Sở Tư pháp An Giang | `cb_nv_dp_04` |

**Pool tổng MPH:** 12 → **15** (KICH_HOAT). Cover thêm 3 LV: Hành chính / Đầu tư / Dân sự.

---

## Per-scope verify (BẮT BUỘC)

| Scope | Trước seed | Sau seed | Cover | OK |
|---|---:|---:|---|:--:|
| TW (`cb_nv_tw_04` view) | 7 | 8 | tất cả TW templates | ✅ |
| BN-BKH (`cb_nv_bn_04` view) | 8 (7 TW + 1 BN-BKH) | 9 (+ BN-BKH Đầu tư) | TW + own BN-BKH | ✅ |
| DP-AG (`cb_nv_dp_04` view) | 8 (7 TW + 1 DP-AG) | 9 (+ DP-AG Dân sự) | TW + own DP-AG | ✅ |

**FR-II-NEW-02 acceptance pass:** `pham_vi_ap_dung` auto-fill đúng cấp user (KHÔNG cho user override) — 3/3 record verify match SRS line 1042-1056.

---

## Ảnh chụp

- [r8-mob-ext-bn-dautu-9of9.png](r8-mob-ext-bn-dautu-9of9.png) — bn_04 view sau seed Đầu tư (top row)
- [r8-mob-ext-dp-danse-9of9.png](r8-mob-ext-dp-danse-9of9.png) — dp_04 view sau seed Dân sự (top row)
- [r8-mob-ext-acc04-state-verify.png](r8-mob-ext-acc04-state-verify.png) — QTHT verify 8/8 acc `_04` HOAT_DONG

---

## Bug observations (KHÔNG block task)

- **BUG-005 reproduce:** mail reset-password link thiếu `:3000` port (`http://103.172.236.130/reset-password?...` thay vì `:3000/`). Workaround: thêm `:3000` thủ công khi navigate. Đã log từ R11.

---

*2026-05-09 12:18:00 — QA chạy 100% UI MCP qua Chrome DevTools, KHÔNG dùng API POST direct.*
