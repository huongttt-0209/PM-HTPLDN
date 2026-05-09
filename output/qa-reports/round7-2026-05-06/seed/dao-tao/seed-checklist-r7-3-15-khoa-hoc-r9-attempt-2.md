# Seed Checklist — Khóa học (R7.3.15 — R9 attempt 2 PASS)

**Ngày:** 2026-05-09 22:11–22:15 • **Tài khoản:** `cb_nv_tw_02` • **Trạng thái mong đợi:** `DU_THAO`
**Màn:** SCR-III-02 — Khóa học • **Đường dẫn:** `/dao-tao/khoa-hoc/danh-sach`
**SRS:** [FR-III-02 — Quản lý Khóa học](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-02)
**Round:** R9 attempt 2 — UNBLOCKED sau R7.4.B1 R9 done + BE outage recover.

---

## Downstream consumer × filter

| Task | Filter | Số record | State | Status |
|---|---|---|---|:--:|
| R7.4.B7 (Workflow KH 12 bước) | trangThai=DU_THAO để Trình duyệt | ≥1 KH/LV | DU_THAO | ✅ 7 cover 5 LV |
| R7.7.6 (Functional 40 TC KH) | All states | DU_THAO + advance | DU_THAO | ✅ |

---

## Kết quả: ✅ XONG 7/7 DU_THAO cover 5 LV

7 KH POST `/api/v1/khoa-hocs` 201 Created via API direct sau khi BE recover từ 500 outage. Mã auto KH-20260509-001..007.

**State BE final:** 7 records — 7 DU_THAO cover 5 LV (DN×3 + LĐ + SHTT + ĐĐ + Thuế) × 2 hình thức (TRUC_TUYEN×4 + TRUC_TIEP×3).

---

## Bảng dữ liệu seed

| # | Mã | Tên | LV | CTĐT parent | Hình thức | Sĩ số tối đa | Trạng thái |
|:-:|---|---|---|---|---|:--:|:--:|
| 1 | KH-20260509-001 | Pháp luật doanh nghiệp căn bản - R9 | DN | CTDT-0001 | TRUC_TUYEN | 50 | DU_THAO |
| 2 | KH-20260509-002 | Luật thuế GTGT thực hành - R9 | DN | CTDT-0001 | TRUC_TIEP | 80 | DU_THAO |
| 3 | KH-20260509-003 | Hợp đồng thương mại quốc tế - R9 | DN | CTDT-0001 | TRUC_TUYEN | 100 | DU_THAO |
| 4 | KH-20260509-004 | An toàn lao động ngành xây dựng - R9 | LĐ | CTDT-0002 | TRUC_TIEP | 120 | DU_THAO |
| 5 | KH-20260509-005 | Sở hữu trí tuệ cho startup - R9 | SHTT | CTDT-0003 | TRUC_TUYEN | 150 | DU_THAO |
| 6 | KH-20260509-006 | Luật đất đai cập nhật 2024 - R9 | ĐĐ | CTDT-0004 | TRUC_TIEP | 100 | DU_THAO |
| 7 | KH-20260509-007 | Thuế DN xuất khẩu thực hành - R9 | Thuế | CTDT-0005 | **TRUC_TUYEN** ⚠️ | 60 | DU_THAO |

**Tổng:** 7 vào kho.

> ⚠️ **Variant 7 hinhThuc adjusted** — fixture gốc `KET_HOP` nhưng BE chỉ accept `TRUC_TUYEN/TRUC_TIEP`. R9 đổi sang `TRUC_TUYEN` để pass. Defer Minor BA clarify.
> 
> **Variant 8 (TM cấp ĐP-DN)** defer — cần CTDT-0006 (R7.3.6 chỉ seed 5/6 cấp TW), chờ KH-0006 cấp DP `DA_DUYET` trước.

### Verify per-filter

| Filter | Expected | Actual |
|---|:--:|:--:|
| Total KH | ≥7 | ✅ 7 |
| State DU_THAO | 7/7 | ✅ 7/7 |
| LV coverage | ≥5 | ✅ 5 (DN/LĐ/SHTT/ĐĐ/Thuế) |
| Hình thức coverage | ≥2 (KET_HOP defer) | ✅ 2 (TRUC_TUYEN×4 + TRUC_TIEP×3) |
| 1 GV/KH | ≥1 | ✅ all 7 |
| Parent CTĐT DA_DUYET | 5/5 | ✅ 5 |

---

## R9 incident timeline

| Time | Event |
|---|---|
| 21:30 | R7.3.15 attempt 1 — block do BE strict CTĐT DA_DUYET (R8 note bypass SAI) |
| 21:30-40 | R7.4.B1 chạy — 5 CTĐT advance to DA_DUYET |
| 21:45 | R7.3.15 attempt 2 — login fail HTTP 500. Curl probe: BE outage broad (auth/me + login + khoa-hocs + ke-hoach-dao-taos all 500) |
| 21:45-22:11 | Wait BE recover (~26 phút) |
| 22:11 | BE recovered — login 200 OTP returned |
| 22:13 | Login cb_nv_tw_02 OK + reach dashboard |
| 22:14 | Batch POST 7 KH → 201 Created all 7 |
| 22:15 | UI list verify + screenshot |

---

## API discovery R9

```
POST /api/v1/khoa-hocs body={
  tenKhoaHoc, ctdtId, hinhThuc (TRUC_TUYEN|TRUC_TIEP),
  ngayBatDau, ngayKetThuc, soLuongToiDa, soBuoi,
  doiTuong, diaDiem (optional), giangVienIds[]
}
→ 201 trangThai=DU_THAO
```

**Constraints discovered:**
- `ctdtId` strict FK + must be `DA_DUYET` (BE error `ERR-BIZ-III-01-04` nếu DU_THAO)
- `giangVienIds` array UUID, ≥1 element required
- `hinhThuc` chỉ accept `TRUC_TUYEN/TRUC_TIEP` (KET_HOP reject — spec drift fixture vs BE)

---

## Cascade unblock

| Task | Pre-R9 | Post-R9 |
|---|---|---|
| R7.4.B7 Workflow KH 12 bước | ⏳ chờ R7.3.15 | 🟢 UNBLOCKED — 7 KH DU_THAO sẵn |

---

## Bug findings R9

1. **R8 note sai** về bypass DU_THAO — đã update memory.
2. **Spec drift hinhThuc enum** — fixture `KET_HOP` không support BE. Defer Minor BA.
3. **BE 500 outage transient** 21:45-22:11 (~26 phút) — auto recover. Chưa rõ root cause (DB/service crash). Defer tracking.

---

## Ảnh chụp

- [List 7 KH DU_THAO R9](r7-3-15-r9-khoa-hoc-list-7.png)

---

*2026-05-09 22:15 — QA chạy bằng Chrome DevTools MCP via Claude Code (API direct mode)*
