# Bang doi chieu dieu kien - QLGVTG_06 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 21): LA LOI - danh sach giang vien dang sap theo ten A->Z, vi pham quy uoc
dung chung DG-06 "sap xep mac dinh theo thoi gian cap nhat moi nhat" (srs-v3.5.md:919). Verdict doi tu
"BA confirm" sang Open. Verify lai: them 1 giang vien -> ban ghi moi nam o dau danh sach.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu (quan ly giang vien) | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Khong |
| Man hinh | Dao tao, tap huan -> Giang vien / Tro giang -> Danh sach (thu tu mac dinh, khong bam sort) | `/dao-tao/giang-vien/danh-sach`, khong dung bo loc / khong bam tieu de cot | Khong |
| Du lieu tien de | Can >=2 ban ghi de phan biet thu tu; can ban ghi co ten xep CUOI bang chu cai de test co suc phan biet | Seed 5 giang vien qua UI. Chu y: ban ghi moi dat ten `ZZZ Cuoi Bang Chu Cai - GV Sort Test` - duoi sap A->Z se nam CUOI, duoi sap moi-nhat se nam DAU | Khong |
| Thao tac | (a) Them giang vien moi -> xem vi tri; (b) Sua ban ghi CU NHAT -> xem vi tri | Da chay ca 2 nhanh | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Nhanh (a) - them moi:** truoc khi them, thu tu la `QA RV4 GV SDT DiDong10` / `CoDinh11` / `Trong` /
`QA GV QLGVTG09` = dung thu tu tao nguoc (moi -> cu), KHONG phai A->Z (A->Z se cho `QA GV QLGVTG09` dau).
Sau khi them `ZZZ Cuoi Bang Chu Cai - GV Sort Test` (toast "Tao giang vien thanh cong"), ban ghi nay
nam **vi tri 1/5** du ten xep CUOI bang chu cai. => Ban ghi moi nam dau danh sach. ✅ DAT tieu chi BA.

**Nhanh (b) - phan biet "ngay tao" vs "ngay cap nhat"** (DG-06 ghi ro "thoi gian CAP NHAT moi nhat"):
mo Sua ban ghi CU NHAT `QA GV QLGVTG09` (dang o vi tri 5/5 - cuoi danh sach), doi truong To chuc thanh
`Cap nhat luc 18:22:58`, bam Luu -> toast "Cap nhat giang vien thanh cong". Quay lai danh sach: ban ghi
nay nhay len **vi tri 1/5**, thu tu moi la `QA GV QLGVTG09` / `ZZZ...` / `DiDong10` / `CoDinh11` / `Trong`.
=> Sap xep theo **thoi gian cap nhat** thuc su, khong phai chi theo ngay tao. ✅ DAT dung nguyen van DG-06.

Ket luan: 0 GAP. Dev da lam dung yeu cau BA (va dung ca y "cap nhat" chu khong chi "tao") -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_06-ban-ghi-moi-dau-danh-sach.png` (ban ghi ten ZZZ nam vi tri 1)
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_06-sua-ban-ghi-cu-nhay-len-dau.png` (ban ghi cu nhat nhay len vi tri 1 sau khi sua)
