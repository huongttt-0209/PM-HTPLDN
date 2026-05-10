# Seed Checklist — Khóa học (R7.3.15 — R9 BLOCKED)

**Ngày:** 2026-05-09 21:30 • **Tài khoản:** `cb_nv_tw_02` • **Trạng thái mong đợi:** `DU_THAO`
**Màn:** SCR-III-02 — Khóa học • **Đường dẫn:** `/dao-tao/khoa-hoc/danh-sach`
**SRS:** [FR-III-02 — Quản lý Khóa học](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-02)
**Round:** R9 — **BLOCKED do BE strict enforce CTĐT DA_DUYET**.

---

## Kết quả: 🚫 BLOCKED — Cần CTĐT DA_DUYET (hiện 0)

**R8 note "BE strict FK ctdtId nhưng bypass workflow OK" SAI.** R9 verify thực tế:
- FE form filter strict — combobox "Chương trình đào tạo" empty với note "Chỉ hiển thị các chương trình đã được phê duyệt" + msg "Không có chương trình phù hợp"
- BE direct API POST cũng reject 422 với code `ERR-BIZ-III-01-04: Chương trình đào tạo chưa được duyệt`

→ Cả FE lẫn BE đều enforce CTĐT phải `DA_DUYET`. Không thể bypass.

```
POST /api/v1/khoa-hocs body={ctdtId: "<DU_THAO>", giangVienIds: [...]}
→ 422 ERR-BIZ-III-01-04: Chương trình đào tạo chưa được duyệt
```

**State BE final:** 0 records.

---

## Dependency cascade (true block chain)

```
R7.4.B0 (KH năm DA_DUYET) ✅ R9 done — 2 KH cấp TW DA_DUYET
        ↓
R7.3.6 (CTĐT DU_THAO) ✅ R9 done — 5 CTĐT cấp TW DU_THAO
        ↓
R7.4.B1 (Workflow CTĐT advance DU_THAO→CHO_DUYET→DA_DUYET) ⏳ chưa chạy
        ↓
R7.3.15 (Khóa học) 🚫 BLOCKED chờ B1 advance ≥1 CTĐT
        ↓
R7.4.B7 (Workflow KH 12 bước) ⏳ chờ R7.3.15
        ↓
R7.4.B11 (Phê duyệt KH) ⏳ chờ B7
        ↓
R7.7.6 (Functional 40 TC) ⏳ chờ all
```

→ Phải chạy **R7.4.B1 trước** để advance ≥1 CTĐT cấp TW lên `DA_DUYET`.

---

## Cần làm tiếp

1. **Chạy R7.4.B1** trước R7.3.15 — advance ≥1 CTĐT DU_THAO → CHO_DUYET (cb_nv_tw_02) → DA_DUYET (cb_pd_tw_01)
2. **Sau khi có ≥1 CTĐT DA_DUYET** → re-run R7.3.15 seed Khóa học
3. **R7.3.15 cần update fixture:** `hinhThuc=KET_HOP` → BE 422 (`hinhThuc must be one of TRUC_TUYEN, TRUC_TIEP`). Spec drift fixture line 2580 (variant 7) — phải đổi `KET_HOP` → `TRUC_TUYEN` hoặc `TRUC_TIEP`. Khả năng BE chưa support KET_HOP enum cho khóa học. Đề xuất defer log Minor (BA verify spec).

---

## Verify per-filter (defer)

Tất cả filter defer cho đến khi R7.3.15 unblock và có data:
- Total KH ≥7 — defer
- Cover 5 LV (DN/LD/SHTT/DD/THUE) — defer
- 3 hình thức (TRUC_TUYEN/TRUC_TIEP/KET_HOP nếu BE support) — defer
- Variant 8 (ĐP-DN) — defer xa hơn (cần KH năm cấp DP DA_DUYET → CTĐT cấp DP DA_DUYET)

---

## Bug findings R9

1. **R8 note sai về bypass** — Cập nhật todo task R7.3.15 từ 🟢 → 🚫. Memory `qa_htpldn_*` cần update.
2. **Spec drift `hinhThuc` enum** — fixture có KET_HOP nhưng BE chỉ accept TRUC_TUYEN/TRUC_TIEP. Cần BA clarify hoặc dev mở rộng enum. Defer log Minor.

---

*2026-05-09 21:30 — QA chạy bằng Chrome DevTools MCP via Claude Code*
