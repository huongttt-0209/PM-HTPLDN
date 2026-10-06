# Bang doi chieu dieu kien - QLGVTG_08 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 23, duyet 15/07/2026 - chuyen Dev FE): bam "Sua" thi breadcrumb/tieu de phai
ghi "Chinh sua", phan biet voi "Chi tiet" (xem). Tien le: module Tu van vien da lam dung - bam Sua ghi
"Chinh sua [Ho ten]" (srs-fr-04:1480). Verify lai: bam Sua -> breadcrumb "Chinh sua"; bam ten giang vien
-> breadcrumb "Chi tiet".

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu (quan ly giang vien) | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Khong |
| Man hinh | Dao tao, tap huan -> Giang vien / Tro giang -> Danh sach | `/dao-tao/giang-vien/danh-sach` | Khong |
| Du lieu tien de | Can >=1 giang vien de mo duoc 2 che do | Dong `QA GV QLGVTG09` (id fb261852-2362-4f0a-a540-215596fd521f) | Khong |
| Thao tac | 2 nhanh: (a) bam TEN giang vien -> xem breadcrumb; (b) bam nut Sua -> xem breadcrumb | Da chay ca 2 nhanh tren CUNG 1 ban ghi de so sanh truc tiep | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Nhanh (a) - bam TEN giang vien** `QA GV QLGVTG09`:
- URL: `/dao-tao/giang-vien/fb261852-2362-4f0a-a540-215596fd521f`
- Breadcrumb: `Trang chu / Dao tao, tap huan / Giang vien / Tro giang / **Chi tiet**` ✅ DAT

**Nhanh (b) - bam nut Sua** cung ban ghi do:
- URL: `/dao-tao/giang-vien/fb261852-2362-4f0a-a540-215596fd521f/**chinh-sua**`
- Breadcrumb: `Trang chu / Dao tao, tap huan / Giang vien / Tro giang / Chi tiet / **Chinh sua**` ✅ DAT

=> Hai che do co breadcrumb KHAC nhau va dung nhan BA yeu cau: che do xem ket thuc bang "Chi tiet",
che do sua ket thuc bang "Chinh sua". Phan biet duoc ro rang tren cung mot ban ghi.

Ghi nhan them (KHONG anh huong verdict): breadcrumb che do sua la chuoi `... / Chi tiet / Chinh sua`
(giu ca cap "Chi tiet" lam nut cha dieu huong) chu khong thay the han. BA chi yeu cau "breadcrumb/tieu de
phai ghi Chinh sua, phan biet voi Chi tiet" - dieu nay dat. Tien le TVV (srs-fr-04:1480) ghi
"Chinh sua [Ho ten]" kem ten; o day ten giang vien hien o TIEU DE man (`QA GV QLGVTG09`) chu khong ghep
vao breadcrumb - van truyen dat du thong tin, khong tinh lech yeu cau.

Ket luan: 0 GAP. Dev da lam dung yeu cau BA -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_08-breadcrumb-chi-tiet.png` (bam ten -> "Chi tiet")
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_08-breadcrumb-chinh-sua.png` (bam Sua -> "Chinh sua")
