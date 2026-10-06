# SRS Re-sync Log — Plan Test Chi Tiết 16 Module

> **Mục đích:** Track mọi event Phase C re-sync (SRS update → TC + bug re-validate + re-test). Mỗi file SRS update mới landing trong `input/srs-update-05-05-2026/` = 1 row mới ở bảng "Sync events log".
>
> **Reference:** [`tasks/detailed-tc/plan.md` §4 Phase C](../../tasks/detailed-tc/plan.md) — 5 step C1 Detect → C2 Impact → C3 Re-write → C4 Re-test → C5 Log.
>
> **Mode mặc định:** `auto-c3-checkpoint` — auto C1-C3, pause sau C3 chờ confirm C4, scope C4.2 = 100% TC trong file affected (Option 1 full regression).

**Status icons:**
- 📭 chờ trigger · 🔵 đang sync · ⏸️ paused (chờ user resume) · ✅ done · ⚠️ partial (bug Open mới chặn) · 🚫 block (cascade upstream)

**Last step values:** C1 / C2 / C3 / C4.1 / C4.2 / C5

---

## Sync events log

| # | Date | SRS file | FR | Version | TC affected | Bug delta | Re-test | Last step | Phase C status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-05-06 | `srs-fr-07-doanh-nghiep-v3.1.md` | FR-07 | v3.1 | 5 file: 00, 01, 03 (DEPRECATE), 06, 99 (review) | _(pending C4.1)_ | _(pending C4.2)_ | C3 | ⏸️ paused — chờ user confirm proceed C4 |
| 2 | 2026-05-07 | `srs-fr-10-quan-tri-v3.1.md` | FR-10 | v3.1 | 10 file: 4 overview + 4 TC affected + 2 TC NEW (xem chi tiết §C2 dưới) | _(pending C4.1)_ | _(pending C4.2)_ | C3 | ⏸️ paused — chờ user confirm proceed C4 |

---

## Module Phase C status snapshot (mirror từ todo.md để cross-reference nhanh)

| FR | Module | Phase A | Phase C | Last sync version |
|---|---|---|---|---|
| FR-07 | Doanh nghiệp | ✅ | ⏸️ | v3.1 (2026-05-06) |
| FR-04 | CG/TVV | ✅ | 📭 | — |
| FR-10 | QTHT (4 sub) | ✅ | ⏸️ | v3.1 (2026-05-07) |
| _(other modules: 📭 chờ trigger)_ | | | | |

---

## C2 Impact Detail — FR-10 v3.1 (2026-05-07)

### A. BR thay đổi (modified)

| BR ID | v3 | v3.1 | Tác động |
|---|---|---|---|
| BR-AUTH-01 | "Tier 1 = U/P + TOTP. Tier 2 = VNPT eKYC. Tier 3 = SSO VNeID OIDC" | "Mô hình **2-tier**: Tier 1 (nội bộ qua mạng kín) = U/P + TOTP cho CB nội bộ; Tier 2 (Internet-facing) = SSO VNeID OIDC cho DN/TVV/CG/NHT. **Không có VNPT eKYC**" | TC login phải theo 2-tier, bỏ test VNPT eKYC |
| BR-AUTH-02 | "Phân cấp **3 tầng**: TW → BN / ĐP" | "Cấu trúc **2 tầng**: TW (cấp 1) → {BN, ĐP} (cấp 2, ngang cấp song song). BN/ĐP độc lập, KHÔNG cha-con" | Cây đơn vị seed test đổi: ĐP.don_vi_cha_id phải trỏ trực tiếp TW |
| BR-AUTH-04 | "TW thấy toàn bộ. BN chỉ thấy BN mình (không thấy ĐP trực thuộc BN)" | "**Chỉ TW thấy cấp con.** TW thấy toàn bộ. BN không có cấp con trực thuộc (mô hình 2-tier — BN/ĐP ngang cấp)" | TC phân quyền dữ liệu BN không còn test "BN thấy ĐP trực thuộc" |
| BR-INTG-06 | "VNeID tích hợp 3 Tier" | "Mô hình 2-tier (nội bộ / Internet)" | TC tích hợp đổi mô hình |
| BR-SLA-02 | "Bình thường (>50%)" | "`BINH_THUONG` → nhãn FE 'Trong hạn'" — đổi nhãn theo BA 2026-05-04 | TC SLA badge text "Bình thường" → "Trong hạn" |

### B. BR thêm mới

| BR ID | Phát biểu | Áp dụng FR |
|---|---|---|
| BR-AUTH-09 | Cán bộ nội bộ (CB Nghiệp vụ, CB Phê duyệt, QTHT) chỉ Tier 1, KHÔNG đăng nhập VNeID, KHÔNG đồng bộ VNeID UC123 | FR-VIII-23, FR-VIII-25 |

### C. FR thêm mới

| FR ID | Tên | Note |
|---|---|---|
| FR-VIII-26 | Quên mật khẩu / Kích hoạt tài khoản lần đầu | Workflow chung TVV/CG/NHT/DN/CB. Token vĩnh viễn (kích hoạt) vs 30 phút (reset). Trigger SM-TVV/SM-NHT đồng thời chuyển HOAT_DONG. |
| FR-VIII-28 | Nhật ký hệ thống (MH-10.10) `[GAP-VIII-02]` | Formalize SCR-VIII-10. Khoảng thời gian max 90 ngày. Excel max 10K dòng (KHÁC current TC nhat-ky-he-thong ghi 50K). |
| FR-VIII-29 | Quản lý ngày lễ `[GAP-VIII-05]` | CRUD NGAY_LE, import Excel, lap_lai_hang_nam, calendar view. Hỗ trợ tính SLA (BR-CALC-03). |

### D. FR sửa đổi đáng kể

| FR ID | v3 | v3.1 |
|---|---|---|
| FR-VIII-22 | UC191 — Đăng ký TK chung (mọi role) | UC120 — **Chỉ DN tự đăng ký**, form 22 trường (19 DN + 3 TK), TK ở `CHO_KICH_HOAT` đã gán vai trò DN sẵn (KHÔNG qua CHO_PHAN_QUYEN), auto-pass không validate cơ quan ngoài |
| FR-VIII-23 | Login VNeID tổng quát | Phân biệt **VNeID Tổ chức (DN)** / **VNeID Cá nhân (TVV/CG/NHT)**, KHÔNG tự tạo TK qua VNeID lần đầu, ERR-VN-04 chặn CB nội bộ |
| FR-VIII-25 | Đồng bộ VNeID tổng quát | KHÔNG áp dụng CB nội bộ (BR-AUTH-09) |

### E. SM-TAIKHOAN thay đổi

- **Thêm trạng thái:** `CHO_PHAN_QUYEN` (awaiting_role) `[GAP-VIII-01]` — sau kích hoạt email, chờ QTHT gán vai trò + đơn vị
- **Thêm transitions:**
  - `CHO_KICH_HOAT → CHO_PHAN_QUYEN` (trigger: User kích hoạt qua email self-reg cũ)
  - `CHO_PHAN_QUYEN → HOAT_DONG` (trigger: QTHT duyệt + gán vai trò + đơn vị, guard: vai_tro+don_vi đã gán)

### F. TC files affected (10 file)

**4 sub-module overview (UPDATE in-place — sync BR/FR table v3.1):**
1. `QTHT/Cau-hinh-he-thong/00-test-plan-overview.md`
2. `QTHT/DM_dung-chung/00-test-plan-overview.md`
3. `QTHT/Nhat-ky-he-thong/00-test-plan-overview.md`
4. `QTHT/Tai-khoan-phan-quyen/00-test-plan-overview.md`

**4 TC content files (UPDATE in-place — sửa expected/AC theo BR mới):**
5. `Cau-hinh-he-thong/01-TC-SLA.md` — BR-SLA-02 nhãn "Bình thường" → "Trong hạn"; link với FR-VIII-29 ngày lễ
6. `DM_dung-chung/04-TC-co-quan-don-vi.md` — BR-AUTH-02 cây đơn vị 3 tầng → 2 tầng (ĐP.don_vi_cha_id trỏ TW)
7. `Nhat-ky-he-thong/01-TC-nhat-ky-he-thong.md` — formalize FR-VIII-28: max 90 ngày, Excel 10K dòng (đổi từ 50K), 2 ERR mới
8. `Tai-khoan-phan-quyen/02-TC-quan-ly-tai-khoan.md` — SM-TAIKHOAN thêm CHO_PHAN_QUYEN + 2 transition mới

**2 TC files NEW (CREATE):**
9. `Cau-hinh-he-thong/05-TC-ngay-le.md` — FR-VIII-29 mới
10. `Tai-khoan-phan-quyen/05-TC-quen-mk-kich-hoat.md` — FR-VIII-26 mới

**TC files KHÔNG affected (giữ nguyên):**
- DM_dung-chung: 01..03, 05..10 (TPL CRUD + 8 DM riêng — BR không đổi)
- Cau-hinh-he-thong: 02..04 (phân công, mẫu phản hồi, quy trình — không liên quan BR thay đổi)
- Tai-khoan-phan-quyen: 01 (vai trò — UC112 không đổi BR), 03 (phân quyền dữ liệu — BR-AUTH-02/04 đổi gián tiếp, sẽ verify ở C4 nếu user trigger), 04 (phân quyền chức năng — UC115 không reference BR đổi)

> **Note:** Per Rule cứng C2.3 "100% TC file chứa TC affected → mark whole file affected, KHÔNG cherry-pick". Các file 03 (phan-quyen-du-lieu) và 01 (quan-ly-vai-tro) sẽ được scan lại trong C4.2 nếu user proceed — nếu reference BR-AUTH-02/03/04 đổi cây đơn vị thì cũng phải re-test.

### G. Bug delta forecast (sẽ confirm ở C4.1)

Hiện tại bug-report FR-10 (4 sub-module) chưa có bug Open. Forecast bug delta = 0 VALID giữ, 0 transition.

---

## Notes

- **Format ngày:** YYYY-MM-DD (chuẩn ISO).
- **TC affected count:** đếm file (không cherry-pick TC riêng lẻ — per Rule cứng C2.3).
- **Bug delta format:** `<N> VALID giữ, <M> VALID→INVALID, <K> GAP→VALID, ...` — chỉ điền sau C4.1.
- **Resume rule:** Khi pause giữa chừng, dùng `Resume Phase C FR-XX vN` để continue từ step kế tiếp (mapping ở `plan.md` §4 Phase C Resume rule).
