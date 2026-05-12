# Dev request — Module Vu viec (R7.7.3)

> **Muc dich:** Chi gui Dev cac van de can Dev xu ly. Cac viec Infra / Seed / BA da tach sang file rieng: [`non-dev-followup-vu-viec.md`](non-dev-followup-vu-viec.md).
>
> **Module:** Vu viec HTPL (FR-05 / R7.7.3)
> **Round:** R7 — 72 TC v3.5 · Latest R18 (2026-05-12): **33/72 TC da chay (~46%)**
> **Thoi diem tong hop:** 2026-05-12 01:15:00
> **Functional report:** [`functional-test-report-r7-7-3-vu-viec.md`](../../functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md)
> **Bug report:** [`bug-report-r7-7-3-functional-vu-viec.md`](bug-report-r7-7-3-functional-vu-viec.md)

---

## Tom tat R18 — 2026-05-12

Sau khi reverify 5 bug Open + chay them 3 TC unblock (`VV-013/013b/013c`):

| Bug | Trang thai sau R18 | Dev can lam |
|---|---|---|
| `BUG-VV-FN-POOL-CG-MISSING-01` | **Closed R18** — pool BE da bao gom CG | KHONG |
| `BUG-VV-FN-TVV-DETAIL-403-01` | **Closed R18** — route guard fix | KHONG |
| `BUG-VV-FN-PHANCONG-REVERT-01` | **Khong reproduce R18** — VV-013/013b/013c PASS (state `DA_PHAN_CONG` persist, lich su entry `PHAN_CONG_CA_NHAN` ghi) | Cho dong khi user manual verify lan cuoi |
| `BUG-VV-FN-TVV-PERMISSION-GAP-01` | **Open** — 4 core perm TVV con thieu | **P0 — can fix** |
| `BUG-VV-FN-LICHSU-01` | **Open partial** — 11/18 enum sau R18 | **P1 — can fix** |
| `BUG-VV-PC-WRN-01` (flow) | **Open Minor** — text fix OK nhung thieu nut override `[Tim thu cong]` | **P2 — can fix** |

Dev can xu ly 3 van de duoi day.

---

## P0 — BUG-VV-FN-TVV-PERMISSION-GAP-01

**Loai:** Permission / role-based access  
**Anh huong:** Block toan bo flow TVV xu ly + trinh duyet + hoan thanh VV. Block cac TC: `VV-015/017/019/020/021/022/023/035`.

### Hien tuong

Account TVV (`tvv_r11_mailfix` / role `TU_VAN_VIEN`) co the dang nhap, xem VV detail (sau khi fix `BUG-VV-FN-TVV-DETAIL-403-01`), nhung KHONG co cac permission cot loi de cap nhat ket qua + trinh phe duyet + hoan thanh VV.

Khi TVV mo VV detail (state `DA_PHAN_CONG` hoac `DANG_XU_LY`):

- UI khong hien nut `[Cap nhat ket qua]`, `[Trinh phe duyet]`, `[Hoan thanh]` mac du theo spec TVV phai co.
- API call PATCH `/api/v1/vu-viecs/{id}` voi field `ketQua...` tra 403 `Forbidden`.
- Backend response `permissions[]` cho user TVV khong chua:
  - `vu-viec:cap-nhat-ket-qua_create`
  - `vu-viec:cap-nhat-ket-qua_update`
  - `vu-viec:create_ket_qua_vu_viec`
  - `vu-viec:trinh-phe-duyet_create`
  - `vu-viec:hoan-thanh_create`

### Expected (theo SRS FR-V.I-12 + permission matrix)

Role `TU_VAN_VIEN` phai co cac perm sau cho entity `vu-viec`:

| Perm code | Mo ta |
|---|---|
| `vu-viec:cap-nhat-ket-qua_create` | Tao moi ket qua xu ly |
| `vu-viec:cap-nhat-ket-qua_update` | Cap nhat ket qua xu ly hien co |
| `vu-viec:create_ket_qua_vu_viec` | Tao record `KET_QUA_VU_VIEC` |
| `vu-viec:trinh-phe-duyet_create` | Trinh ket qua sang CB_PD/NHT phe duyet |
| `vu-viec:hoan-thanh_create` | Danh dau VV `HOAN_THANH` |

### Can Dev fix

- BE: bo sung 5 perm tren vao role `TU_VAN_VIEN` trong permission seed/migration.
- FE: kiem tra logic an/hien nut theo permission claims (tranh hardcode role check).
- Backfill cac record TVV hien co neu dung perm runtime check.

### QA verify sau fix

1. Login `tvv_r11_mailfix`.
2. Mo VV state `DA_PHAN_CONG` (vd `VV-QA-R7-SLA-SH`) — bam `[Xac nhan phan cong]` -> `DANG_XU_LY`.
3. Bam `[Cap nhat ket qua]` -> form hien.
4. Nhap ket qua -> Luu -> verify GET `/vu-viecs/{id}/ket-qua` co record.
5. Bam `[Trinh phe duyet]` -> state `CHO_PHE_DUYET`.
6. Login CB_PD/NHT duyet -> verify state `DA_DUYET`.
7. Login lai TVV -> bam `[Hoan thanh]` -> state `HOAN_THANH`.

---

## P1 — BUG-VV-FN-LICHSU-01

**Loai:** Audit / history data  
**Trang thai R18:** 11/18 enum spec (`~61%`). Hom nay 2026-05-12 verify them thay co `PHAN_CONG_CA_NHAN` (subset `PHAN_CONG`). Nhung 5 enum sau van **chua thay ghi** trong `LICH_SU_VU_VIEC`.

### Hien tai da co (verified R18)

`TAO_VV`, `KIEM_TRA`, `PHAN_CONG`, `PHAN_CONG_CA_NHAN`, `XAC_NHAN_PHAN_CONG`, `CAP_NHAT_KQ`, `TRINH_PD`, `PHE_DUYET`, `HOAN_THANH`, `DANH_GIA`, `CONG_KHAI` / `HUY_CONG_KHAI`.

### Con thieu (chua thay ghi sau R18 walk lifecycle)

| # | Enum spec | Trigger |
|---|---|---|
| 1 | `TIEP_NHAN` | Khi CB_NV bam `[Tiep nhan]` -> state `DA_TIEP_NHAN` |
| 2 | `YEU_CAU_BO_SUNG` | Khi CB_NV ket luan kiem tra ho so = `Khong dat - YCBS` |
| 3 | `TU_CHOI` | Khi CB_NV tu choi VV trong giai doan kiem tra |
| 4 | `TU_CHOI_DUYET` | Khi CB_PD/NHT tu choi duyet ket qua |
| 5 | `MO_LAI` | Khi VV `HOAN_THANH` duoc mo lai cho buoc xu ly bo sung |

Spec SRS FR-V.I-08 §3.4.3.x liet ke day du 18 enum. R18 verify chi thay 11. Mat 5 enum tren = audit log khong tracking duoc cac transition state quan trong.

### Can Dev fix

- Audit code path tu cac handler API:
  - POST `/vu-viecs/{id}/tiep-nhan` -> ghi `TIEP_NHAN`.
  - POST `/vu-viecs/{id}/kiem-tra-ho-so` voi ketLuan `KHONG_DAT_YCBS` -> ghi `YEU_CAU_BO_SUNG`.
  - POST `/vu-viecs/{id}/tu-choi` -> ghi `TU_CHOI`.
  - PATCH `/vu-viecs/{id}/phe-duyet` voi verdict `TU_CHOI` -> ghi `TU_CHOI_DUYET`.
  - POST `/vu-viecs/{id}/mo-lai` (neu co endpoint) -> ghi `MO_LAI`.
- Dam bao writeLog goi cung transaction voi state change.

### QA verify sau fix

1. Chay 1 VV qua tat ca branch: tiep nhan -> kiem tra YCBS -> tu choi YCBS -> reset; phan cong -> trinh duyet -> tu choi duyet -> mo lai.
2. GET `/api/v1/vu-viecs/{id}/lich-su?pageSize=50`.
3. Distinct enum tra ve = 16+ (cong 5 enum thieu).
4. Filter `?loaiHanhDong=YEU_CAU_BO_SUNG` -> tra ≥1 record.

---

## P2 — BUG-VV-PC-WRN-01

**Loai:** UX / fallback action  
**Trang thai R18:** Text empty state da match spec. Nhung **van thieu nut override `[Tim thu cong]`** cho phep CB_NV mo rong scope khi pool goi y = 0.

### Hien tuong

Khi CB_NV mo modal `[Phan cong]` → tab `Ca nhan` → combobox `Chon nguoi duoc phan cong` filter theo linh vuc VV. Neu pool = 0 (vi du VV LV Thue + chua co TVV/NHT nao co LV Thue), modal hien empty state dung spec:

> "Trong. Khong tim thay doi tuong phu hop linh vuc. Lien he QTHT de mo rong linh vuc TVV/NHT, hoac chon vu viec khac."

Nhung KHONG co nut/CTA giup CB_NV:

- Mo rong scope tim kiem (vd loai bo filter linh vuc, tim toan bo TVV/NHT).
- Chuyen sang dang phan cong `To chuc tu van` neu Ca nhan empty.
- Yeu cau QTHT mo rong linh vuc (vd link sang trang quan ly TVV de them LV cho TVV co san).

Theo SRS §3.4.3.18 step 4: "Neu khong tim thay TVV/NHT phu hop, cho phep CB_NV chuyen sang lua chon thu cong hoac mo rong tieu chi."

### Expected

Modal empty state co ≥1 nut override:

- `[Tim thu cong]` — bo filter LV, hien toan bo TVV/NHT con HOAT_DONG.
- HOAC `[Chuyen sang To chuc tu van]` — auto switch tab segmented.
- HOAC link `[Yeu cau QTHT mo rong linh vuc]` -> dieu huong sang admin.

### Can Dev fix

- FE: them nut override trong empty state component cua modal phan cong (file goc cua `<PhanCongModal />`).
- BE: optional support API `?bypassFilter=true` cho endpoint `/api/v1/vu-viecs/goi-y-tvv` neu QTHT chua co perm rieng.

### QA verify sau fix

1. Login `cb_nv_tw_03`.
2. Mo VV LV it pho bien (vd `Thue` neu pool < 5) -> bam `[Phan cong]` -> `Ca nhan`.
3. Combobox empty -> verify nut `[Tim thu cong]` hien.
4. Bam `[Tim thu cong]` -> verify pool show toan bo TVV/NHT (≥10 record).
5. Chon 1 record -> Xac nhan -> verify phan cong thanh cong.

---

## Khong gui Dev xu ly trong request nay

Cac muc duoi day khong phai viec Dev BE/FE trong request hien tai:

- `BUG-VV-FN-NOTIF-01`: da Closed R16-P2.
- `BUG-VV-FN-POOL-CG-MISSING-01`: da Closed R18.
- `BUG-VV-FN-TVV-DETAIL-403-01`: da Closed R18.
- `BUG-VV-FN-PHANCONG-REVERT-01`: R18 verify khong reproduce — dong sau manual confirm.
- **VNeID Tier 2 sandbox** (cho DN/TVV/CG/NHT login full lifecycle): chuyen Infra/Integration team. Day la phu thuoc API ngoai he thong (VNeID = Vietnam eID provider). Khong tao file rieng vi Dev BE/FE khong fix duoc.
- Cong PLQG / mTLS integration: Infra.
- Seed deadline backdated SLA: QA seed / DBA.
- C5-4 duplicate guard / C6-4 BR-CALC-04: BA 2026-05-11 da chot — khong cung trong request nay.

---

## Tai lieu tham chieu

- [`bug-report-r7-7-3-functional-vu-viec.md`](bug-report-r7-7-3-functional-vu-viec.md)
- [`bug-report-flow-vu-viec.md`](bug-report-flow-vu-viec.md)
- [`functional-test-report-r7-7-3-vu-viec.md`](../../functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md)
- [`todo-vu-viec.md`](../../../../../tasks/todo-vu-viec.md)
