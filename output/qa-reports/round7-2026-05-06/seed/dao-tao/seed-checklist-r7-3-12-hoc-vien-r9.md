# Seed Checklist — Học viên (R7.3.12 — R9 probe)

**Ngày:** 2026-05-09 20:33 • **Tài khoản:** N/A (probe via curl) • **Trạng thái mong đợi:** `HOC_VIEN` entity tồn tại
**Màn:** SCR-III-NEW Học viên • **Đường dẫn:** `/dao-tao/hoc-vien/danh-sach` (chưa deploy)
**SRS:** [FR-III-NEW Mô hình A — Quản lý Học viên](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md) (entity HOC_VIEN tách riêng khỏi DANG_KY_DAO_TAO)
**Round:** R9 — probe BE endpoint, **BLOCKED do entity chưa deploy**.

---

## Kết quả: 🚫 BLOCKED — Entity HOC_VIEN chưa deploy

R9 probe BE endpoint cả 2 convention (plural + singular) đều trả 404. Entity HOC_VIEN chưa được implement migration + controller + route. Task BLOCKED chờ dev.

```
GET /api/v1/hoc-viens?page=1&pageSize=5  →  HTTP 404
GET /api/v1/hoc-vien?page=1&pageSize=5   →  HTTP 404
```

**Kết luận:** Cả plural và singular đều 404. Route chưa register, controller chưa code.

---

## Cần dev

- ☐ Migration tạo bảng `HOC_VIEN` với schema theo SRS FR-III-NEW (id, hoTen, email, soDienThoai, donVi, ngayDangKy, trangThai, ...)
- ☐ Entity + Repository + Service
- ☐ Controller + Route (chuẩn convention plural: `/api/v1/hoc-viens` — match các module khác như `khoa-hocs`, `bai-giangs`, `giang-viens`)
- ☐ FE form đăng ký học viên + danh sách
- ☐ Permission cho CB_NV_TW/BN/DP create/manage

---

## Impact downstream

| Task | Cascade |
|---|---|
| **R7.3.12** | BLOCKED trực tiếp — không seed được học viên |
| R7.4.B7 (workflow KH 12 bước) | Cascade — bước "Đăng ký học viên" cần HOC_VIEN entity |
| R7.4.B11 (Phê duyệt KQ) | Cascade — cần học viên để có kết quả |
| R7.7.6 (functional 40 TC) | Cascade — TC liên quan học viên block |

---

## Bug tracking

R9 không log bug formal — đây là missing feature (entity chưa code), không phải bug. Đã ghi escalation note ở [dev-escalation-r9-hoc-vien-lich-hoc.md](../../dev-escalation-r9-hoc-vien-lich-hoc.md).

---

*2026-05-09 20:33 — QA chạy bằng curl probe via Bash (không cần auth do endpoint chưa register)*
