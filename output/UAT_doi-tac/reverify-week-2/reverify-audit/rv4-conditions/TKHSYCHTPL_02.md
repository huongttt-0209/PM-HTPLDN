# Bang doi chieu dieu kien - TKHSYCHTPL_02 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 105, duyet 16/07/2026 - chuyen Dev):
- Bo sung bo loc **"Don vi"** vao man danh sach vu viec, **CHI HIEN voi cap Trung uong**. Ly do: cho quyen xem
  toan quoc ma khong cho cong cu loc la thiet ke chua tron; CB Bo nganh / Dia phuong da bi gioi han 1 don vi
  nen voi ho truong loc nay vo nghia.
- Hien thanh tim kiem co 6 truong (tu khoa, Linh vuc PL, Kenh tiep nhan, Muc SLA, Trang thai, Tu-Den ngay)
  - dung SRS (srs-fr-05:1622-1628, :645-652) nen truoc day khong tinh la loi; nay BA quyet bo sung.
- Owner: BA bo sung don_vi_id vao SCR-V.I-01 (:1622-1628) va FR-V.I-08 §Dau vao (:645-652) -> Dev FE + BE.
- **Verify lai: dang nhap cap TW -> co bo loc Don vi, loc ra dung vu viec theo don vi;
  dang nhap Bo nganh/Dia phuong -> khong thay bo loc nay.**

Case goc (sheet row 105): KQ mong doi = "He thong hien thi cac truong thong tin giong voi thiet ke / Trang thai
mac dinh cho phep chon/nhap / Textbox rong, Danh sach chon mac dinh la Tat ca".
KQ thuc te doi tac = 'Khong hien thi truong thong tin tim kiem theo "Don vi" doi voi nguoi dung cap Trung uong'.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro 1 - cap TW | Cap **Trung uong** phai **CO** bo loc Don vi + loc ra dung vu viec theo don vi | `cbnv_tw` "CB Nghiep vu - Trung uong", badge **CB_NV_TW**, don vi **BTP · TW** | Khong |
| Vai tro 2 - cap Bo nganh | Cap **Bo nganh** phai **KHONG** thay bo loc nay | `cbnv_bn` "CB Nghiep vu - Bo nganh", badge **CB_NV_BN**, don vi **BTP · BN** | Khong |
| Vai tro 3 - cap Dia phuong | Cap **Dia phuong** phai **KHONG** thay bo loc nay | `cbnv_dp` "CB Nghiep vu - Dia phuong", badge **CB_NV_DP**, don vi **BTP · DP** | Khong |
| Man hinh | Man **danh sach vu viec** | `/vu-viec/danh-sach` (Vu viec HTPL) - cung mot man cho ca 3 vai tro | Khong |
| Thao tac | Kiem co bo loc Don vi khong; voi cap TW thi **chon 1 don vi va kiem ket qua loc** | Da chay: doc thanh tim kiem cua ca 3 vai tro (**co mo ca "Bo loc nang cao"** de bo loc khong nap trong do); rieng TW thi chon that 1 don vi + bam Tim kiem + dem ket qua | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Vai tro 1 - cap Trung uong (`cbnv_tw`): DAT - CO bo loc va loc DUNG.**
- Thanh tim kiem co bo loc **"Don vi"** (canh Linh vuc PL / Kenh tiep nhan / Muc SLA).
- Danh sach don vi nap duoc (Bo Cong an, Bo Cong Thuong, Bo Giao duc va Dao tao, ... + So Tu phap cac tinh),
  co tim kiem trong dropdown.
- **Loc that:** chon **"So Tu phap An Giang"** -> bam [Tim kiem] -> danh sach **tu 17 xuong dung 3 ket qua**,
  ca 3 deu la **VV-STP-AG-20260712-001 / -002 / -003** (dung tien to STP-AG = So Tu phap An Giang).
  => bo loc **loc ra dung vu viec theo don vi**, khong phai chi hien cho co.
- => Loi goc doi tac bao ("khong hien thi truong tim kiem theo Don vi doi voi nguoi dung cap Trung uong") **DA HET**.

**Vai tro 2 - cap Bo nganh (`cbnv_bn`): DAT - KHONG thay bo loc.**
- Thanh tim kiem chi con: Linh vuc PL / Kenh tiep nhan / Muc SLA / Trang thai. **Khong co "Don vi"**.
- Da mo ca "Bo loc nang cao" de chac chan bo loc khong nap trong do -> van khong co.
- Danh sach: 4 ket qua (pham vi don vi cua chinh minh).

**Vai tro 3 - cap Dia phuong (`cbnv_dp`): DAT - KHONG thay bo loc.**
- Thanh tim kiem chi con: Linh vuc PL / Kenh tiep nhan / Muc SLA / Trang thai. **Khong co "Don vi"**.
- Da mo ca "Bo loc nang cao" -> van khong co.
- Danh sach: 3 ket qua (pham vi don vi cua chinh minh).

Ket luan: dung ca 3 vai tro theo dong verify BA ghi - TW co bo loc va loc ra dung vu viec theo don vi;
Bo nganh va Dia phuong deu khong thay bo loc nay -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-TKHSYCHTPL_02-tw-co-bo-loc-don-vi-loc-dung.png`
  (CB_NV_TW: co bo loc Don vi, chon So Tu phap An Giang -> 3 ket qua, ca 3 deu ma VV-STP-AG)
- `../../bug-reports/ba-approved-batch/image/rv4-TKHSYCHTPL_02-bo-nganh-khong-co-bo-loc-don-vi.png`
  (CB_NV_BN: thanh tim kiem khong co Don vi)
- `../../bug-reports/ba-approved-batch/image/rv4-TKHSYCHTPL_02-dia-phuong-khong-co-bo-loc-don-vi.png`
  (CB_NV_DP: thanh tim kiem khong co Don vi)
