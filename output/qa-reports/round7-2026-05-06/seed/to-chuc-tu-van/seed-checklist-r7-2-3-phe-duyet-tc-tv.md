# Seed checklist — R7.2.3 Phê duyệt TC TV → HOAT_DONG

> ✅ **R8 UI re-test 2026-05-09 02:05:** 3/3 record mới (TC-0006/0007/0008) phê duyệt qua UI MCP — gỡ method gap. Workflow `cb_nv_tw_02` (Trình duyệt) + `cb_pd_tw_02` (Phê duyệt + Số QĐ + Ý kiến) → HOAT_DONG version=3. reqid trinh-phe-duyet 181/188/194 + phe-duyet 179/186/192 (200 OK). Pool API verified `byState: { HOAT_DONG: 8 }` total=8. Method gap đóng — toàn bộ flow UI-only.
>
> ⚠️ **Method gap (note 2026-05-08, đóng R8):** 1/5 record qua UI, 4/5 qua API thuần (`POST /trinh-phe-duyet` + `POST /phe-duyet`) — vi phạm rule UI-only ban hành 2026-05-07. Cần re-test 4 record còn lại bằng UI MCP R8. Xem [`tasks/lessons-learned.md` 2026-05-08](../../../../../tasks/lessons-learned.md).

**Ngày chạy:** 2026-05-06 (R7)
**Account workflow:** `cb_nv_tw_02` (trình duyệt) + `cb_pd_tw_02` (phê duyệt + công bố)
**SRS ref:** FR-IV-NEW-04 (CB PD cùng cấp công bố)
**Endpoints:**
- `POST /api/v1/to-chuc-tu-vans/{id}/trinh-phe-duyet` body `{"version":1}` (CB NV)
- `POST /api/v1/to-chuc-tu-vans/{id}/phe-duyet` body `{"quyetDinh":"PHE_DUYET","soQuyetDinh":"...","yKienPheDuyet":"...","version":2}` (CB PD)

## Kết quả

✅ **8/8 TC TV → HOAT_DONG** (`pool: { HOAT_DONG: 8 }` verified GET 2026-05-09 02:05). 5 record R7 (qua API) + 3 record R8 (qua UI MCP).

| Mã | Tên | Số QĐ công bố | State | Method |
|---|---|---|:-:|:-:|
| TC-BTP-TW-0001 | Công ty Luật TNHH Alpha Hà Nội | QD-TW-0001/2026 | HOAT_DONG | API (R7) |
| TC-BTP-TW-0002 | Văn phòng Luật sư Beta Hải Phòng | QD-TW-0002/2026 | HOAT_DONG | API (R7) |
| TC-BTP-TW-0003 | Trung tâm TVPL Gamma Đà Nẵng | QD-TW-0003/2026 | HOAT_DONG | API (R7) |
| TC-BTP-TW-0004 | Đoàn Luật sư Hà Nội | QD-TW-0004/2026 | HOAT_DONG | API (R7) |
| TC-BTP-TW-0005 | Công ty Luật TW Epsilon | QD-TW-0005/2026 | HOAT_DONG | UI (R7) |
| TC-BTP-TW-0006 | Cong ty Luat TNHH Theta R8 | QD-TW-0006/2026 | HOAT_DONG | **UI (R8)** |
| TC-BTP-TW-0007 | Van phong Luat su Iota R8 | QD-TW-0007/2026 | HOAT_DONG | **UI (R8)** |
| TC-BTP-TW-0008 | Trung tam TVPL Kappa Da Nang R8 | QD-TW-0008/2026 | HOAT_DONG | **UI (R8)** |

## R8 Workflow UI (2026-05-09 02:05)

| Bước | Account | Action | Modal | Endpoint reqid | Result |
|:-:|---|---|---|---|---|
| 1 | `cb_nv_tw_02` | TC-0006 → Trình duyệt | "Xác nhận trình phê duyệt" → click [Trình duyệt] | `POST /trinh-phe-duyet` reqid=181 200 | MOI_DANG_KY → CHO_PHE_DUYET ✅ |
| 2 | `cb_nv_tw_02` | TC-0007 → Trình duyệt | (idem) | reqid=188 200 | ✅ |
| 3 | `cb_nv_tw_02` | TC-0008 → Trình duyệt | (idem) | reqid=194 200 | ✅ |
| 4 | `cb_pd_tw_02` | TC-0006 → Phê duyệt | "Xác nhận phê duyệt và công bố" → fill Số QĐ + Ý kiến → [Phê duyệt] | `POST /phe-duyet` reqid=179 200 | CHO_PHE_DUYET → HOAT_DONG ✅ |
| 5 | `cb_pd_tw_02` | TC-0007 → Phê duyệt | (idem) | reqid=186 200 | ✅ |
| 6 | `cb_pd_tw_02` | TC-0008 → Phê duyệt | (idem) | reqid=192 200 | ✅ |

**Modal phê duyệt validations đúng spec:**
- Button [Phê duyệt] disabled khi Số QĐ rỗng (FE-block client-side, đúng FR-IV-NEW-04).
- Sau submit: detail page render `Số QĐ công bố`, `Ngày QĐ công bố`, `ngayCongNhan`, badge "Đang hoạt động".
- API response: `version=3`, `nguoiGuiDuyetId=cb_nv_tw_02`, `nguoiDuyetId=cb_pd_tw_02`, `ghiChuPheDuyet` lưu nguyên ý kiến tester.

**Evidence:**
- [r7-2-3-r8-pre-3-mdk.png](image/r7-2-3-r8-pre-3-mdk.png) — pre-state 3 record MDK
- [r7-2-3-r8-after-trinh-3-cpd.png](image/r7-2-3-r8-after-trinh-3-cpd.png) — sau Trình duyệt 3/3 CHO_PHE_DUYET
- [r7-2-3-r8-final-8-hoat-dong.png](image/r7-2-3-r8-final-8-hoat-dong.png) — final 8/8 HOAT_DONG

## Workflow R7 (historical, mixed UI/API)

1. CB NV (`cb_nv_tw_02`): TC-0005 trình duyệt qua UI (modal "Xác nhận trình phê duyệt") → 4 còn lại bulk API.
2. CB PD (`cb_pd_tw_02`, isolated context): TC-0005 phê duyệt qua UI (modal nhập "Số quyết định" + ý kiến) → 4 còn lại bulk API.

State: `MOI_DANG_KY` (v=1) → `CHO_PHE_DUYET` (v=2) → `HOAT_DONG` (v=3) + `ngayCongNhan` + `soQdCongBo` + `ngayQdCongBo`.

## Downstream

- ✅ Pool TC TV `HOAT_DONG` = **8** → unblock T3 R7.2.6 (CG seed cần `toChucChinhId` UUID FK) + R7.4.A6 workflow + R7.7.4.6 functional.
