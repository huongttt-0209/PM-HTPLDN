# Bang doi chieu dieu kien - QLKH_03 (verify lan DAU sau khi dev bao fix, 2026-07-17 vong 8)

Boi canh: dong TC nay do **chinh QA mo them** (dong 114) khi verify lai KTDGKQHT_03 ngay 17/07.
Bug goc: buoi hoc **CHUA diem danh lan nao** thi man hinh **tu tick san "Vang khong phep"** cho hoc vien,
trong khi du lieu da luu la RONG. Cot `Verify` cua dong nay **con TRONG** (chua verify lan nao).

Can cu: KHONG co dong SRS nao quy dinh gia tri mac dinh khi chua diem danh (da tra v3.5 + v3 legacy).
Cho dung vung cua bug la **man hinh phai phan anh dung du lieu da luu**: may chu tra `trangThai` rong
(chua co ban ghi KET_QUA_DAO_TAO cho buoi do) thi man hinh khong duoc hien nhu da co gia tri.

| Điều kiện | Bug gốc (rv7, 17/07) | Mình test (verify 2026-07-17 vòng 8) | GAP? |
|---|---|---|:-:|
| Vai tro | `cbnv_tw` (CB_NV_TW) mo tab Diem danh | `cbnv_tw`, badge **CB_NV_TW** - dung vai tro bug goc | Không |
| Man hinh | Dao tao, tap huan -> Khoa hoc -> chi tiet -> tab **Diem danh** | Dung tab **Diem danh** cua chi tiet khoa hoc | Không |
| Khoa hoc | **KH-SEED-0001** "Khoa hoc phap luat doanh nghiep seed", trang thai **Da ket thuc** | Dung khoa **KH-SEED-0001** (id `5eed0002-0000-4000-8000-000000000001`), trang thai **Da ket thuc** - dung ban ghi bug goc | Không |
| Buoi hoc | 2 buoi cung ngay **20/02/2026**: SANG 08:00-11:00 (da diem danh "Co mat") + CHIEU 14:00-17:00 (**CHUA diem danh**) | Dung 2 buoi **20/02/2026**: SANG 08:00-11:00 + CHIEU 14:00-17:00 - chon **buoi CHIEU** la buoi chua diem danh | Không |
| Hoc vien | **"QA Import Reverify12 OK"** | Dung hoc vien **"QA Import Reverify12 OK"** (`qa.import.reverify12ok@test.htpldn.vn`) | Không |
| Thao tac | Chon buoi CHIEU -> quan sat cot Trang thai | Da chay that: chon buoi CHIEU tu bo chon buoi -> doc trang thai that cua cac o chon | Không |
| Tien de "khong dinh trang thai buoi truoc" | Bug goc da tai lai trang roi chon THANG buoi CHIEU | Da dang nhap lai tu dau bang phien sach, vao thang tab Diem danh, chon **thang buoi CHIEU** (khong mo buoi SANG truoc) | Không |

## Ket qua quan sat (UI, khong dung API de ra verdict)

**DA FIX THAT.**
- Chon buoi **CHIEU 20/02/2026 (14:00-17:00)** - buoi chua tung diem danh - thi hoc vien
  "QA Import Reverify12 OK" co cot Trang thai **KHONG o nao duoc chon**: ca 3 o "Co mat" /
  "Vang co phep" / "Vang khong phep" deu **rong**. Truoc day o "Vang khong phep" bi to xanh dam.
- **Doi chung buoi SANG** (da diem danh "Co mat"): van hien **dung "Co mat"**. => man hinh doc dung
  du lieu da luu, rong o buoi CHIEU la **do fix dung**, khong phai component chet.
- Khoa "Da ket thuc" nay **mat han nut "Luu diem danh" + "Import Excel"** (chi con "Xuat Excel"),
  ca 3 o chon deu khoa mo - khop luon voi fix cua KTDGKQHT_03.

## Ngoai tieu chi - co thay gi bat thuong khong? CO 2 diem, deu la QA tu dinh chinh

1. **Ghi nhan cu "sai ty le chuyen can / BR-KQ-02" la SAI.** BR-KQ-02 (`srs-fr-03-dao-tao.md:2126`)
   tinh `ty_le_chuyen_can = (Co mat + Vang co phep) / TONG SO BUOI`. Mau so la *tong so buoi*, nen buoi
   "chua diem danh" va buoi "vang khong phep" cho ra **cung mot ty le**. Loi nay **khong anh huong**
   chuyen can. Tac hai that chi la **ghi sai su that vao ho so hoc vien**.
2. **Ghi nhan cu "khoa DDD-KH-011 ban ghi seed hong" la SAI.** Du lieu **khong hong**: dang nhap dung
   don vi so huu (`cbnv_bn`) thi doc lich hoc **binh thuong** va **them buoi thanh cong**. Nguyen nhan
   that: khoa thuoc don vi khac, can bo khong co quyen, nhung he thong bao **"Khoa hoc khong ton tai"**
   thay vi bao khong co quyen -> gay chan doan nham. **De nghi tach thanh muc rieng (Minor).**

## Phan CHUA kiem duoc (khai bao ro, khong ket luan thay)

Nhanh khoa **"Dang dien ra"** (tab con sua duoc, bam Luu khi chua chon ai): **chua kiem duoc doc lap**.
Da thu dung data moi nhung tac o luat nghiep vu - them hoc vien vao khoa dang dien ra bi tu choi
**"Chi co the dang ky khoa hoc da duyet"**. Y nay hien **chi co xac nhan tu Dev**.
Luu y: bug goc duoc log tren chinh khoa **"Da ket thuc"** nay, nen TC QLKH_03 da duoc verify **1:1 dung
tien de goc**; nhanh "Dang dien ra" la he qua phu, khong thuoc TC.

## Ket luan

Bug **da fix that** - buoi chua diem danh nay de trong dung nhu ky vong, doi chung buoi da diem danh van
dung. Verify tren **dung khoa / dung buoi / dung hoc vien** cua bug goc. => **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv8-QLKH_03-PASS-buoi-chieu-radio-rong.png`
  (da mo doc lai pixel: bo chon buoi hien **"20/02/2026 - 14:00:00-17:00:00 - QA seed KTDGKQHT_03 - buoi CHIEU"**;
  dong hoc vien "QA Import Reveri..." co 3 o "Co mat" / "Vang co phep" / "Vang khong phep" deu **xam mo,
  khong o nao duoc to xanh**; thanh cong cu chi con **"Xuat Excel"**, khong con "Luu diem danh"/"Import Excel")
