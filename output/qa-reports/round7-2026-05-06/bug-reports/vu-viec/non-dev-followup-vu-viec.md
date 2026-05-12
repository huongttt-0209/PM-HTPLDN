# Non-dev follow-up — Module Vu viec (R7.7.3)

> **Muc dich:** Tong hop cac viec khong nen dua vao request Dev BE. File Dev-only: [`dev-seed-request-vu-viec.md`](dev-seed-request-vu-viec.md).
>
> **Latest:** R16-P2 ngay 2026-05-11 · R7.7.3 dat **30/72 TC**, con **43 TC**.

---

## Infra / Integration

### VNeID Tier 2 + DN portal

**Owner:** Infra / Integration / Dev phu trach portal  
**Trang thai:** Chua test E2E duoc.

Can co:

- VNeID Tier 2 sandbox URL + token.
- It nhat 1-2 DN account verified Tier 2.
- Endpoint chuyen trang DN portal cho:
  - DN gui yeu cau VV.
  - DN bo sung ho so khi VV `YEU_CAU_BO_SUNG`.
  - DN xem VV cua minh.
  - DN cham diem UC67.

Block cac nhom TC DN/VNeID, gom Cluster 1, mot phan Cluster 4/5/6 va privacy DN view.

---

## QA seed / DBA

### Seed SLA backdated

**Owner:** QA seed / DBA  
**Trang thai:** Can tao data rieng, khong lam qua UI vi ngay tiep nhan auto now.

Can seed 3 VV:

| Muc SLA | Dieu kien data |
|---|---|
| `SAP_HET` | deadline con 1-3 ngay |
| `QUA_HAN` | deadline qua han 1-7 ngay |
| `QUA_HAN_NGHIEM_TRONG` | deadline qua han tren 7 ngay |

Dung de test 3 muc con lai cua `VV-022` / BR-SLA-02.

---

## BA confirm — đã chốt 2026-05-11

### C5-4 — Duplicate danh gia

**Thuc te:** Sau khi CB_NV danh gia lan 1, VV auto flip `HOAN_THANH -> DA_DANH_GIA`. Lan 2 bi chan bang state guard `ERR-STATE-VI-16-01`, khong den duplicate rule rieng.

**BA chot:** Bat buoc chan duplicate bang rule `(vu_viec_id, loai_nguoi_danh_gia)`, khong chi dua vao state `DA_DANH_GIA`. Ma loi duplicate dung la `ERR-DG-VV-03`; `ERR-DG-VV-04` la loi khong co quyen danh gia, khong phai duplicate.

### C6-4 — BR-CALC-04 fallback

**Thuc te:** Tao VV cho DN thieu cac field uu tien van thanh cong, he thong fallback priority 3 "Trung binh".

**BA chot:** Khong chap nhan fallback priority 3 am tham khi thieu field bat buoc. He thong phai canh bao/chan tao VV va yeu cau DN cap nhat du thong tin truoc. Priority 3 chi dung khi du du lieu nhung khong roi vao nhom uu tien cao hon.

---

## QA executable sau khi unblock

Sau khi Dev fix `PHANCONG-REVERT`, QA co the chay lai:

- Phan cong ca nhan/to chuc.
- Assignee chap nhan/tuchoi.
- Full lifecycle fresh VV.
- Lich su deep coverage.
- Public toggle tren VV moi.

Sau khi Infra co VNeID/DN portal:

- DN gui YC.
- DN bo sung ho so.
- DN xem VV cua minh.
- DN cham diem.
- Privacy DN khong thay VV cua DN khac.
