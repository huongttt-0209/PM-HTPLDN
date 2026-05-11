# Dev request — Module Vu viec (R7.7.3)

> **Muc dich:** Chi gui Dev cac van de can Dev xu ly. Cac viec Infra / Seed / BA da tach sang file rieng: [`non-dev-followup-vu-viec.md`](non-dev-followup-vu-viec.md).
>
> **Module:** Vu viec HTPL (FR-05 / R7.7.3)
> **Round:** R7 — 72 TC v3.5 · Latest R16-P2: **30/72 TC da chay (~42%)** · con **43 TC**
> **Thoi diem tong hop:** 2026-05-11
> **Functional report:** [`functional-test-report-r7-7-3-vu-viec.md`](../../functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md)
> **Bug report:** [`bug-report-r7-7-3-functional-vu-viec.md`](bug-report-r7-7-3-functional-vu-viec.md)

---

## Tom tat cho Dev

Khong can fix `BUG-VV-FN-NOTIF-01` nua. Bug nay da **Closed R16-P2** sau khi test fresh trigger: phan cong VV gui du 2 mail (DN + TVV/NHT).

Dev can xu ly 2 van de:

| Uu tien | Bug | Owner | Trang thai |
|---|---|---|---|
| **P0** | `BUG-VV-FN-PHANCONG-REVERT-01` | Dev BE | Open — block fresh lifecycle |
| **P1** | `BUG-VV-FN-LICHSU-01` | Dev BE | Open partial — 11/18 enum |

---

## P0 — BUG-VV-FN-PHANCONG-REVERT-01

**Loai:** Data integrity / transaction atomicity  
**Anh huong:** Block full lifecycle fresh VV va cac TC: `VV-013/013b/013c/014/015/017/033` + Cluster phan cong.

### Hien tuong

POST phan cong tra **201** va response nhin nhu thanh cong:

- `trangThai = DA_PHAN_CONG`
- `version` tang
- `nguoiXuLyId` co gia tri
- `loaiDoiTuongXuLy = CA_NHAN`
- `ngayPhanCong` co gia tri
- Mail trigger OK: DN + TVV/NHT deu nhan mail

Nhung sau 3-5 giay, GET lai VV thi du lieu **khong persist**:

- `trangThai` van la `DANG_KIEM_TRA`
- `version` van version cu
- `nguoiXuLyId = null`
- `loaiDoiTuongXuLy = null`
- `ngayPhanCong = null`
- GET `/vu-viecs/{id}/phan-cong` tra `data: []`
- GET `/lich-su` khong co entry `PHAN_CONG`

Bug reproducible **2/2 lan** voi TVV va NHT tren VV fresh `VV-BTP-TW-20260511-001`.

### Expected

POST `/api/v1/vu-viecs/{id}/phan-cong` phai persist atomic:

1. Update `VU_VIEC.trang_thai = DA_PHAN_CONG`.
2. Update assignment fields tren `VU_VIEC`: `nguoiXuLyId`, `loaiDoiTuongXuLy`, `ngayPhanCong`.
3. Tao record `PHAN_CONG_VU_VIEC`.
4. Ghi `LICH_SU_VU_VIEC` entry phan cong.
5. Gui mail/notification sau khi transaction persist thanh cong.

Neu DB persist fail thi API khong duoc tra 201 thanh cong.

### Can Dev fix

- Kiem tra transaction cua endpoint `/phan-cong`.
- Dam bao state + assignment + `PHAN_CONG_VU_VIEC` + `LICH_SU` commit cung transaction.
- Neu mail/event dang fire truoc DB commit, can doi thu tu: commit DB truoc, event/mail sau.
- Tra error neu persist fail, khong tra optimistic response 201.

### QA verify sau fix

1. Lay VV `DA_TIEP_NHAN` moi.
2. Click `[Kiem tra ho so]` -> `DANG_KIEM_TRA`.
3. Click `[Phan cong]`, chon TVV/NHT.
4. Verify ngay sau POST va sau reload 3-5 giay:
   - GET detail = `DA_PHAN_CONG`.
   - Assignment fields khong null.
   - GET `/phan-cong` co record.
   - GET `/lich-su` co entry phan cong.
5. Login assignee chap nhan phan cong -> tiep tuc lifecycle.

---

## P1 — BUG-VV-FN-LICHSU-01

**Loai:** Audit / history data  
**Trang thai moi nhat:** R16 coverage **11/18 enum (~61%)**. Da co them `DANH_GIA`, nhung van chua du.

### Hien tai da co

Da thay trong pool:

- `CREATE` / `TAO_VV`
- `KIEM_TRA`
- `PHAN_CONG`
- `XAC_NHAN_PHAN_CONG`
- `TRINH_PD`
- `PHE_DUYET`
- `HOAN_THANH`
- `CONG_KHAI`
- `HUY_CONG_KHAI`
- `DANH_GIA`

Luu y: dang bi mix naming cu/moi: VV cu co `CREATE`, VV moi co `TAO_VV`.

### Con thieu / chua dung

Can ghi rieng cac hanh dong sau:

1. `TIEP_NHAN`
2. `CAP_NHAT_KQ`
3. `YEU_CAU_BO_SUNG`
4. `TU_CHOI`
5. `TU_CHOI_DUYET`
6. `PHAN_CONG_CA_NHAN`
7. `PHAN_CONG_TO_CHUC`

Ghi chu: `PHAN_CONG_CA_NHAN` va `PHAN_CONG_TO_CHUC` dang bi gom generic `PHAN_CONG`. Neu BA/dev quyet dinh chi giu generic `PHAN_CONG`, can cap nhat spec/test case tuong ung.

### Can Dev fix

- Ghi dung enum theo tung transition, khong gom tat ca vao `KIEM_TRA` hoac `PHAN_CONG`.
- Ghi entry khi cap nhat ket qua xu ly (`CAP_NHAT_KQ`).
- Ghi entry rieng cho verdict `YEU_CAU_BO_SUNG` va `TU_CHOI`.
- Ghi entry rieng khi CB_PD tu choi duyet (`TU_CHOI_DUYET`).
- Thong nhat naming enum: uu tien uppercase snake-case, tranh mix `CREATE` va `TAO_VV` neu spec da chot ten moi.

### QA verify sau fix

1. Chay 1 VV moi qua day du lifecycle + cac branch.
2. GET `/api/v1/vu-viecs/{id}/lich-su`.
3. Kiem tra distinct enum dat theo spec.
4. Kiem tra filter theo enum, vi du `loaiHanhDong=DANH_GIA`, `loaiHanhDong=CAP_NHAT_KQ`.

---

## Khong gui Dev xu ly trong request nay

Cac muc duoi day khong phai viec Dev BE trong request hien tai:

- `BUG-VV-FN-NOTIF-01`: da Closed R16-P2.
- VNeID Tier 2 / DN portal: chuyen Infra/Integration.
- Seed deadline backdated SLA: chuyen QA seed / DBA.
- C5-4 duplicate guard va C6-4 BR-CALC-04 fallback: cho BA confirm mechanism.
- UI CTA danh gia trong accordion: observation FE, khong block BE P0 hien tai.

---

## Tai lieu tham chieu

- [`bug-report-r7-7-3-functional-vu-viec.md`](bug-report-r7-7-3-functional-vu-viec.md)
- [`functional-test-report-r7-7-3-vu-viec.md`](../../functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md)
- [`todo-vu-viec.md`](../../../../../tasks/todo-vu-viec.md)
