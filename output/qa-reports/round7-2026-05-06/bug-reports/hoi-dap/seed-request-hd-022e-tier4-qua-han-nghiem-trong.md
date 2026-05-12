# Seed Request — Backdate 1 record để verify tier 4 `QUA_HAN_NGHIEM_TRONG` (BR-SLA-02)

> **Người gửi:** QA Automation · **Ngày:** 2026-05-12 00:42:00 · **Module:** Hỏi đáp · **Round:** R7.7.1 Phase 9 R11
> **Loại yêu cầu:** Test data seed (KHÔNG phải bug, không cần fix code) · **Effort dev:** ~5 phút (1 câu SQL UPDATE)

## Bối cảnh

Sau khi dev FE fix logic map SLA badge color theo `muc_do_canh_bao` từ BE (đã verify R11 2026-05-12 00:27:19 — tier 1 BINH_THUONG, tier 2 SAP_HET, tier 3 QUA_HAN đều render đúng spec BR-SLA-02), còn **tier 4 `QUA_HAN_NGHIEM_TRONG` (>2x, đen)** chưa kiểm vì DB hiện không có record nào ratio >200%.

**Kiểm tra DB hiện tại (2026-05-12 00:35:00):**

| Tier | Spec ngưỡng | Record DB hiện tại | Verified |
|---|---|---|---|
| 1 — BINH_THUONG (xanh) | >50% còn lại (elapsed <50%) | 18 record | ✅ R11 |
| 2 — SAP_HET (vàng) | <50% còn lại (elapsed 50-100%) | HD-20260509-008 (ratio 77.8%) | ✅ R11 |
| 3 — QUA_HAN (đỏ) | >100% elapsed | HD-20260509-009 (ratio 117.8%) | ✅ R11 |
| 4 — QUA_HAN_NGHIEM_TRONG (đen) | >200% elapsed (>2x) | **0 record** | 🚫 Cần seed |

## TC sẽ unlock sau khi seed

| TC | Mô tả | Cần record ở state | Ratio mong đợi | Kỳ vọng FE/BE |
|---|---|---|---|---|
| **HD-022e** | SLA badge tier 4 đen "Quá hạn nghiêm trọng" (BR-SLA-02 — ratio >200%) | DANG_XU_LY | ~240% | BE `muc_do_canh_bao=QUA_HAN_NGHIEM_TRONG`; FE badge màu đen (class custom hoặc `color=#000` / `ant-tag-default` đen) |

## SQL cần chạy trên DB test

> **Môi trường:** http://103.172.236.130:3000/ test DB · **Bảng:** `hoi_dap`
> **Record chọn:** HD-20260507-007 (id `78557936-a6df-4530-b4fc-b02121f96fb4`) — đang DANG_XU_LY, span 5d nominal, hiện ratio chỉ 32% (BINH_THUONG). Backdate xuống >2x.

```sql
-- Backdate ngay_tiep_nhan + deadline cùng lúc để giữ span = 5d, đẩy ratio elapsed lên 240%
UPDATE hoi_dap
SET ngay_tiep_nhan = NOW() - INTERVAL '12 days',
    deadline       = NOW() - INTERVAL '7 days',
    muc_do_canh_bao = 'QUA_HAN_NGHIEM_TRONG'
WHERE id = '78557936-a6df-4530-b4fc-b02121f96fb4';
-- Mã: HD-20260507-007 (state DANG_XU_LY)
-- Sau update:
--   ngay_tiep_nhan = NOW - 12d
--   deadline       = NOW - 7d  (đã quá hạn 7 ngày)
--   span           = deadline - ngay_tiep_nhan = 5d (giữ nguyên span chuẩn 5 ngày làm việc)
--   elapsed        = NOW - ngay_tiep_nhan = 12d
--   ratio elapsed  = 12d / 5d = 240% → tier 4 "Quá hạn nghiêm trọng" (>2x, đen)
```

**Lý do force set `muc_do_canh_bao = 'QUA_HAN_NGHIEM_TRONG'` thay vì để scheduled job tự cập nhật:**

- Theo SRS L978-988, tác vụ tự động kiểm tra mức cảnh báo SLA chạy mỗi 30 phút. Set field trực tiếp giúp QA test ngay sau khi dev chạy SQL, không phải chờ batch job.
- Nếu dev không muốn force field — có thể bỏ dòng `muc_do_canh_bao = ...` và chờ 30 phút cho scheduled job pick up.

## Nếu dev preferred trigger scheduled job manual

Thay 2 dòng `ngay_tiep_nhan` + `deadline` ở trên, KHÔNG cần set `muc_do_canh_bao` thủ công, sau đó:

```bash
# (nếu app có CLI/admin endpoint trigger tác vụ tự động)
# hoặc chờ đến mốc 30 phút kế tiếp
```

QA sẽ retest sau khi job chạy xong (verify qua API: `GET /api/v1/hoi-daps/78557936-a6df-4530-b4fc-b02121f96fb4` xem `mucDoCanhBao` đã = `QUA_HAN_NGHIEM_TRONG` chưa).

## Sau khi dev chạy xong → QA verify

1. Login `cb_pd_tw_04` (CB Phê duyệt TW 04) qua MCP UI → `/hoi-dap` → list view, tìm row HD-20260507-007.
2. Capture badge SLA ở cột "SLA / THỜI HẠN" — verify CSS class + text:
   - **Kỳ vọng tier 4:** class custom màu đen (vd `ant-tag-black`, `ant-tag-default` với style color đen, hoặc inline style `background: #000`/`#262626`).
   - Text: "Quá hạn 7 ngày LV" hoặc "Quá hạn nghiêm trọng" (tuỳ FE).
3. Mở detail record → verify badge SLA cạnh state badge "Đang xử lý" cũng render tier 4.
4. API check: `GET /api/v1/hoi-daps/78557936-a6df-4530-b4fc-b02121f96fb4` → `mucDoCanhBao = "QUA_HAN_NGHIEM_TRONG"`.
5. Update bug-report đóng caveat tier 4 + cập nhật todo R7.7.1 lên 49/60 PASS (nếu thêm 1 TC HD-022e).

## Rollback (sau khi QA test xong)

QA sẽ ping dev khi xong (ước ~15 phút). Dev có thể rollback bằng:

```sql
-- Trả về thời gian gốc
UPDATE hoi_dap
SET ngay_tiep_nhan = '2026-05-10T11:51:35.000Z',  -- hoặc thời điểm gốc dev có
    deadline       = '2026-05-15T11:51:35.000Z',
    muc_do_canh_bao = 'BINH_THUONG'
WHERE id = '78557936-a6df-4530-b4fc-b02121f96fb4';
```

> **Lưu ý:** Nếu rollback không quan trọng (record HD-20260507-007 là seed test, không có data production), có thể giữ nguyên state seed.

## Tại sao xin SQL thay vì xin dev viết tool admin

| Cách | Thời gian | Đánh giá |
|---|---|---|
| **SQL UPDATE 1 lần** (đề xuất) | 5 phút dev + 15 phút QA test + 2 phút rollback | Nhanh nhất, zero code change |
| Xin dev viết admin endpoint backdate | 1-2 ngày dev (code + test + deploy) | Overkill cho 1 TC, blocking sprint khác |
| Set system clock container BE | 30 phút devops | Risk break test parallel của module khác |
| Chờ data tự cũ | Không feasible — ratio 240% cần >10 ngày elapsed |

## Liên hệ

Nếu cần đổi record ID (vd record này đang dùng cho test khác), QA có thể đề xuất 1 trong các record DANG_XU_LY khác sau đây có span 5d sẵn:

| ID | Mã | Span | Current ratio |
|---|---|---|---|
| `78557936-a6df-4530-b4fc-b02121f96fb4` | HD-20260507-007 | 5d | 32.2% |
| `2606b003-1058-42db-8aa2-158eba17e33e` | HD-20260507-003 | 5d | 32.2% |

QA Automation sẽ standby — ping khi dev SQL xong là retest ngay.

---

*Generated: 2026-05-12 00:42:00 | QA Automation via Claude Code (Opus 4.7)*
