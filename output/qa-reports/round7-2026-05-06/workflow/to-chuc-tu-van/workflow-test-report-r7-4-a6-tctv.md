# Workflow Test Report — R7.4.A6 — Tổ chức tư vấn (SM-TCTV)

**Ngày chạy:** 2026-05-09 02:14:00 → 02:21:00
**Verdict:** ✅ **PASS 8/8 transitions** (full coverage, UI-only via MCP)
**Accounts:** `cb_nv_tw_02` (CB Nghiệp vụ TW) + `cb_pd_tw_02` (CB Phê duyệt TW)
**Spec:** SM-TCTV (`srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md` line 2323-2422) + `flow-module §2b` (line 136-151)
**Method:** Chrome DevTools MCP — UI click chain isolated context per role.

## Pool sau test

| Mã | Tên | State cuối | Version | Số QĐ | Ngày CB |
|---|---|:-:|:-:|---|---|
| TC-BTP-TW-0007 | Van phong Luat su Iota R8 | HOAT_DONG | 5 | QD-TW-0007/2026 | 08/05/2026 |
| TC-BTP-TW-0008 | Trung tam TVPL Kappa Da Nang R8 | HOAT_DONG | 5 | QD-TW-0008/2026 | 08/05/2026 |
| TC-BTP-TW-0009 | Cong ty Luat TNHH Lambda R8 A6 | HOAT_DONG | 5 | QD-TW-0009/2026 | 08/05/2026 |

**Verify GET (2026-05-09 02:21):** `total=9, byState={HOAT_DONG:9}`. Pool tăng từ 8 → 9 do tạo TC-0009.

## Transition coverage matrix

3 record × 8 transitions = full SM-TCTV (excl `[*] → MOI_DANG_KY` đã test ở R7.2.2).

| # | Transition | Record | Account | Modal/Action | Kết quả |
|:-:|---|---|---|---|:-:|
| 1 | `MOI_DANG_KY → CHO_PHE_DUYET` | TC-0009 | cb_nv_tw_02 | Modal "Xác nhận trình phê duyệt" → [Trình duyệt] | ✅ |
| 2 | `CHO_PHE_DUYET → HOAT_DONG` | TC-0009 | cb_pd_tw_02 | Modal "Xác nhận phê duyệt và công bố" → fill Số QĐ + Ý kiến → [Phê duyệt] | ✅ |
| 3 | `CHO_PHE_DUYET → TU_CHOI` | TC-0009 | cb_pd_tw_02 | Modal "Xác nhận từ chối" → fill Lý do (≥10 ký) → [Từ chối] | ✅ |
| 4 | `TU_CHOI → CHO_PHE_DUYET` (resubmit) | TC-0009 | cb_nv_tw_02 | Modal "Xác nhận trình phê duyệt" → [Trình duyệt] | ✅ |
| 5 | `HOAT_DONG → TAM_DUNG` | TC-0008 | cb_nv_tw_02 | Modal "Xác nhận tạm dừng" → fill Lý do (≥10 ký) → [Đồng ý] | ✅ |
| 6 | `TAM_DUNG → HOAT_DONG` (kích hoạt lại) | TC-0008 | cb_nv_tw_02 | Modal "Xác nhận khôi phục" → fill Lý do → [Đồng ý] | ✅ |
| 7 | `HOAT_DONG → VO_HIEU_HOA` | TC-0007 | cb_nv_tw_02 | Modal "Xác nhận vô hiệu hóa" + alert "Sẽ tự động gỡ khỏi Cổng pháp luật quốc gia" → fill Lý do → [Đồng ý] | ✅ |
| 8 | `VO_HIEU_HOA → HOAT_DONG` (khôi phục) | TC-0007 | cb_nv_tw_02 | Modal "Xác nhận khôi phục" → fill Lý do → [Đồng ý] | ✅ |

## Lifecycle path TC-0009 (4 transition: 1+3+4+2)

```
[*] ──[create]──> MOI_DANG_KY (v=1)
         ──[trình duyệt]──> CHO_PHE_DUYET (v=2)        # Trans #1
         ──[từ chối]──>     TU_CHOI       (v=3)        # Trans #3
         ──[trình lại]──>   CHO_PHE_DUYET (v=4)        # Trans #4
         ──[phê duyệt]──>   HOAT_DONG     (v=5)        # Trans #2
```

**Audit trail evidence:**
- TC-0009 detail UI sau Trans #4 (CHO_PHE_DUYET) vẫn hiện `Lý do từ chối: "Ho so chua dat yeu cau spec — test workflow A6"` — BE giữ history.
- TC-0009 detail UI sau Trans #2 (HOAT_DONG) ẩn dòng "Lý do từ chối" + render `Số QĐ công bố: QD-TW-0009/2026`, `Ngày QĐ công bố: 08/05/2026`.

## Lifecycle path TC-0008 (2 transition: 5+6)

```
HOAT_DONG (v=3)  ──[tạm dừng]────> TAM_DUNG  (v=4)     # Trans #5
                  ──[kích hoạt]──> HOAT_DONG (v=5)     # Trans #6
```

**Sau Trans #5:** UI render `Lý do tạm dừng: "Tam dung de re-cap nhat ho so phap ly noi bo"` + thao tác chỉ còn `[Kích hoạt lại]`, `[Vô hiệu hóa]`.
**Sau Trans #6:** UI ẩn `Lý do tạm dừng`, thao tác đầy đủ trở lại (`Tạm dừng`, `Vô hiệu hóa`, switch Công khai).

## Lifecycle path TC-0007 (2 transition: 7+8)

```
HOAT_DONG (v=3)  ──[vô hiệu hóa]─> VO_HIEU_HOA (v=4)   # Trans #7
                  ──[khôi phục]──> HOAT_DONG   (v=5)   # Trans #8
```

**Guard verify:** `Số TVV liên kết: 0` ở TC-0007 → cho phép vô hiệu hóa (đúng spec FR-IV-NEW-04 — guard: KHÔNG có TVV liên kết).
**Sau Trans #7:** UI hiện cảnh báo "Sẽ tự động gỡ khỏi Cổng pháp luật quốc gia nếu đã công khai" trong modal + render `Lý do vô hiệu hóa` ở detail. Thao tác chỉ còn `[Khôi phục]`.

## FE/BE validations xác minh

| Validation | Spec | Kết quả |
|---|---|:-:|
| Số QĐ rỗng → button [Phê duyệt] disabled | FR-IV-NEW-04 | ✅ Disabled |
| Lý do từ chối <10 ký → button [Từ chối] disabled | SM-TCTV | ✅ Disabled |
| Lý do tạm dừng <10 ký → button [Đồng ý] disabled | SM-TCTV | ✅ Disabled |
| Lý do vô hiệu hóa <10 ký → button [Đồng ý] disabled | SM-TCTV | ✅ Disabled |
| Lý do khôi phục <10 ký → button [Đồng ý] disabled | SM-TCTV | ✅ Disabled |
| Modal vô hiệu hóa cảnh báo gỡ Cổng pháp luật | flow-module §2b | ✅ Alert hiện |
| Audit version tăng 1 mỗi transition | SM-TCTV | ✅ v=1→5 (TC-0009 4 trans) |

## Evidence (screenshots)

- [r7-4-a6-trans1-tc09-cpd.png](image/r7-4-a6-trans1-tc09-cpd.png) — Trans #1 sau trình duyệt
- [r7-4-a6-trans3-tc09-tu-choi.png](image/r7-4-a6-trans3-tc09-tu-choi.png) — Trans #3 sau từ chối
- [r7-4-a6-trans2-tc09-hoat-dong.png](image/r7-4-a6-trans2-tc09-hoat-dong.png) — Trans #2 sau phê duyệt
- [r7-4-a6-trans56-tc08-tamdung-roundtrip.png](image/r7-4-a6-trans56-tc08-tamdung-roundtrip.png) — Trans #5+6 round trip
- [r7-4-a6-trans78-tc07-vhh-roundtrip.png](image/r7-4-a6-trans78-tc07-vhh-roundtrip.png) — Trans #7+8 round trip

## Bug count

**0 bug.** Toàn bộ 8 transition + 7 validation đúng spec, audit trail chuẩn, modal đúng template.

## Downstream

- ✅ R7.4.A6 ✓ — TC TV state machine verified.
- ⏩ Unblock R7.7.4.6 functional (10 TC) — pool 9 HOAT_DONG + 0 TAM_DUNG/VO_HIEU_HOA/TU_CHOI hiện tại (test đã rollback về HOAT_DONG hết).
- Note: nếu R7.7.4.6 cần record state khác HOAT_DONG, walk lại transition trên 1 TC fresh.
