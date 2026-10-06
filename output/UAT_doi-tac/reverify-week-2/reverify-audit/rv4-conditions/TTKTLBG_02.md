# Bang doi chieu dieu kien - TTKTLBG_02 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 12, duyet bo sung 15/07/2026): bo sung bo loc "Linh vuc phap ly" vao man
tim kho tai lieu / bai giang. Verify lai: thanh tim kiem co bo loc Linh vuc phap ly -> loc ra dung
bai giang theo linh vuc.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu (quan ly kho bai giang) | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Khong |
| Man hinh | Dao tao, tap huan -> Kho tai lieu / Bai giang -> Danh sach (thanh tim kiem) | `/dao-tao/bai-giang/danh-sach`, thanh tim kiem 5 truong + Bo loc nang cao | Khong |
| Du lieu tien de | Bai giang co gan Linh vuc (de chung minh loc ra dung ban ghi) | Seed qua UI Sua: `QLKTLBG_08b` = Thue, `QLKTLBG_08` = Lao dong, `QLKTLBG_08c` de trong. PATCH `/bai-giangs/{id}` tra 200 | Khong |
| Input / filter | Chon tung gia tri Linh vuc phap ly roi bam Tim kiem | Loc Thue -> 1 ket qua; loc Lao dong -> 1 ket qua; loc Hinh su -> 0 ket qua | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

- Thanh tim kiem CO bo loc **"Linh vuc phap ly"** (dropdown 10 gia tri: Thue, Lao dong, Dat dai, Dan su,
  Thuong mai, Hinh su, Hanh chinh, So huu tri tue, Doanh nghiep, Dau tu).
- Loc **Thue** -> URL `?linhVucId=bbbbbbbb-0000-4000-8000-000000000018`, bang hien **dung 1 dong**
  `QA UAT Bai giang Cong khai QLKTLBG_08b` (ban ghi da gan Thue). "Hien thi 1-1 / 1 ket qua".
- Loc **Lao dong** -> URL `?linhVucId=bbbbbbbb-0000-4000-8000-000000000013`, bang hien **dung 1 dong khac**
  `QA UAT Bai giang Test QLKTLBG_08` (ban ghi da gan Lao dong). "Hien thi 1-1 / 1 ket qua".
- Loc **Hinh su** (khong ban ghi nao) -> **0 dong**.

=> Bo loc khong chi ton tai ma con loc DUNG theo linh vuc: 2 gia tri khac nhau tra 2 tap ket qua khac
nhau, gia tri khong co du lieu tra rong. Khong phai Pass bang quan sat tinh.

Ket luan: 0 GAP. Dev da lam dung yeu cau BA -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-TTKTLBG_02-loc-thue-1ketqua.png`
- `../../bug-reports/ba-approved-batch/image/rv4-TTKTLBG_02-loc-laodong-1ketqua.png`
