# Dev request — Module Chi trả (R7.7.12.2)

> **Mục đích:** Chỉ gửi Dev các vấn đề **nội bộ HTPLDN** cần Dev xử lý. Việc đồng bộ từ ngoài (DVC / Cổng PLQG / LGSP gateway) tách sang [`non-dev-followup-chi-tra.md`](non-dev-followup-chi-tra.md) (Infra + DVC sandbox).
>
> **Module:** Chi trả chi phí (FR-V.II / FR-06) — task R7.7.12.2 FR-V.II-14 DN bổ sung HS chi trả
> **Round:** R7 — R2 (2026-05-12 01:30:00)
> **Functional report:** [`functional-test-report-r7-7-12-2-fr14-bo-sung.md`](../../functional/chi-tra/functional-test-report-r7-7-12-2-fr14-bo-sung.md)
> **Bug report:** [`bug-report-r7-7-12-2-fr14-bo-sung.md`](bug-report-r7-7-12-2-fr14-bo-sung.md)

---

## Tóm tắt R2 — 2026-05-12 01:30:00

QA đã chạy được **9/18 TC** (8 PASS + 1 FAIL log BUG-010). Còn 9 TC chưa chạy được phân 2 nhóm:

| Nhóm | Số TC | Cần làm | File theo dõi |
|---|:-:|---|---|
| **Đồng bộ ngoài (DVC/PLQG/LGSP)** | 6 BLOCKED + 1 SKIP | Infra mở DVC sandbox + BE expose LGSP receiver | `non-dev-followup-chi-tra.md` |
| **Wording spec drift** | 1 SKIP | BA xoá row 841 "hoặc CB NV (thủ công)" | BA followup |
| **Cần Dev BE fix nội bộ** | 1 BLOCKED (CT-14-008) | **BUG-010 dưới đây** | file này |

→ **Dev cần xử lý 1 vấn đề nội bộ duy nhất** trong scope R7.7.12.2: BUG-CHITRA-010.

---

## P1 — BUG-CHITRA-010

**Loại:** Backend / Data — transition handler missing field set
**Severity:** Major
**Ảnh hưởng:** Block TC `CT-14-008` (ERR-CT-BS-03 "Quá hạn 5 ngày LV") + nghi vấn UI list cột SLA hiển thị sai semantic. Cascade vào BR-CHITRA-BS01 deadline tracking.

### Hiện tượng

Toàn bộ 6 HSCT state `YEU_CAU_BO_SUNG` (HSCT000004/011/012/013/014/200002) trả `ngayYeuCauBoSung = null` qua GET `/api/v1/ho-so-chi-tras/{id}` dù transition `DANG_KIEM_TRA → YEU_CAU_BO_SUNG` đã xảy ra (`soLanBoSung ≥ 1` cho 6/6, lichSu của HSCT000004 + HSCT200002 có entry "Kiểm tra → Yêu cầu bổ sung" @ 2026-05-10 11:17 by `cb_nv_dp_01`).

```
HSCT000004: YCBS soLan=1 ngayYCBS=null lichSu=2 entries
HSCT000011: YCBS soLan=3 ngayYCBS=null lichSu=0
HSCT000012: YCBS soLan=1 ngayYCBS=null lichSu=0
HSCT000013: YCBS soLan=2 ngayYCBS=null lichSu=0
HSCT000014: YCBS soLan=3 ngayYCBS=null lichSu=0
HSCT200002: YCBS soLan=1 ngayYCBS=null lichSu=2 entries
```

Đồng thời 4/6 HSCT (000011/012/013/014) có `soLanBoSung ≥ 1` nhưng `lichSu = []` — nghi vấn data seed ban đầu bypass lifecycle, BE chưa ghi `LICH_SU_XU_LY` entry khi advance state.

### Expected (theo SRS)

**FR-V.II-03 §Processing Bước 5** (`srs-fr-06-chi-tra.md` line ~267):

> Khi CB NV chuyển HSCT từ `DANG_KIEM_TRA` sang `YEU_CAU_BO_SUNG`, BE phải set `ngay_yeu_cau_bo_sung = NOW()` để khởi tạo countdown 5 ngày LV cho DN bổ sung. Sau 5 ngày LV không bổ sung, BE auto trả `ERR-CT-BS-03` + hệ thống cảnh báo SLA quá hạn.

**BR-CHITRA-BS01** (Business Rule "Bổ sung hồ sơ chi trả"):

- `so_lan_bo_sung` max 3 lần — ✅ PASS (giá trị 1-3 hiện có).
- `ngay_yeu_cau_bo_sung` ≠ NULL khi `trang_thai = YEU_CAU_BO_SUNG` — ❌ FAIL 6/6.
- Deadline = `ngay_yeu_cau_bo_sung + 5 ngày LV` — không tính được do NULL.

Expected payload sau khi transition DKT → YCBS:

```json
{
  "maHoSo": "HSCT000011",
  "trangThai": "YEU_CAU_BO_SUNG",
  "soLanBoSung": 1,
  "ngayYeuCauBoSung": "2026-05-10T11:17:00Z"
}
```

### Cần Dev BE fix

1. **Fix transition handler `DANG_KIEM_TRA → YEU_CAU_BO_SUNG`:**
   - Trong service layer xử lý action "Yêu cầu bổ sung" (CB NV gọi từ B2 SM-CHITRA), set `ho_so_chi_tra.ngay_yeu_cau_bo_sung = NOW()` cùng transaction update trạng thái.
   - Đồng thời insert row `lich_su_xu_ly` (`ho_so_chi_tra_id`, `trang_thai_truoc = DANG_KIEM_TRA`, `trang_thai_sau = YEU_CAU_BO_SUNG`, `nguoi_xu_ly_id`, `thoi_diem = NOW()`, `ghi_chu` từ form CB NV).

2. **Backfill 6 record YCBS hiện có:**
   - Với 2 record có lichSu R3 đầy đủ (HSCT000004 + HSCT200002): UPDATE `ngay_yeu_cau_bo_sung` lấy từ entry "Kiểm tra → Yêu cầu bổ sung" trong `lich_su_xu_ly` (giá trị 2026-05-10 11:17).
   - Với 4 record không có lichSu (HSCT000011/012/013/014): UPDATE `ngay_yeu_cau_bo_sung = ngay_nop_ho_so + 1 ngày` (best-effort, vì seed bypass lifecycle) + insert 1-2 `lich_su_xu_ly` entry retro để cột "Lịch sử xử lý" UI không trống.

3. **Verify UI list cột SLA:**
   - Hiện UI hiển thị "Quá hạn 5-57 ngày LV" cho 6 record — kiểm tra FE dùng field nào (`ngayNopHoSo` hay `ngayYeuCauBoSung`). Nếu dùng `ngayNopHoSo` → fix sang `ngayYeuCauBoSung` để đúng semantic BR-CHITRA-BS01 (deadline 5 ngày LV tính từ thời điểm YCBS, KHÔNG phải thời điểm DN nộp gốc).

### QA verify sau fix

1. Login `cb_nv_dp_01` (AG).
2. Fetch GET `/api/v1/ho-so-chi-tras/{id}` cho 6 HSCT YCBS — expect `ngayYeuCauBoSung != null` cho toàn bộ 6/6.
3. Mở detail HSCT000011/012/013/014 — expect cột "Lịch sử xử lý" hiển thị ≥1 entry (không còn "Chưa có lịch sử xử lý").
4. Check UI list cột SLA — verify công thức `ngày hôm nay - ngayYeuCauBoSung` (LV days), không phải từ `ngayNopHoSo`.
5. **Test cascade CT-14-008** (ERR-CT-BS-03): backdate `ngay_yeu_cau_bo_sung` cho 1 HSCT seed cách hôm nay 7 ngày LV → trigger BE batch/cron deadline check → expect HSCT đó được flag "Quá hạn" + có thể trả error code ERR-CT-BS-03 ở 1 endpoint validation nào đó.

---

## Out of scope file này (đẩy sang non-dev-followup)

- **BUG-CHITRA-008** (Major, LGSP gateway receiver thiếu): chờ Infra mở DVC sandbox staging. KHÔNG fix nội bộ trước vì caller là DVC LGSP external, không phải CB NV manual.
- **BUG-CHITRA-009** (Minor, wording drift row 841): BA xoá phần "hoặc CB NV (thủ công)" để align spec DVC-only. KHÔNG phải dev work.
- **CT-14-002/003/004/005/006/007/009**: cần đồng bộ từ DVC qua LGSP → tách `non-dev-followup-chi-tra.md`.

---

## Snapshot TC R2 (18 TC tổng)

| Status | Count | TC IDs |
|---|:-:|---|
| ✅ PASS | 8 | CT-14-010, CT-14-R-002, R-003, R-004, R-005, R-006, R-007, R-008 |
| ❌ FAIL | 1 | CT-14-R-001 (BUG-010 ngayYeuCauBoSung null 6/6) |
| 🚫 BLOCKED — đồng bộ DVC | 6 | CT-14-002, 003, 004, 005, 006, 007 |
| 🚫 BLOCKED — cascade BUG-010 | 1 | CT-14-008 (sẽ test được sau fix dev) |
| ⏭ SKIP | 2 | CT-14-001 (wording drift), CT-14-009 (DVC out-of-env) |
