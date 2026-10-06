# Bang doi chieu dieu kien - KTDGKQHT_08 (verify dev-fix 2026-07-16, lan dau)

Yeu cau BA (note sheet row 6, chot 16/07/2026): Xac nhan **Fail** - to kiem thu dung, day la loi.
Tra loi "Khong phai bug" cua Dev khong chinh xac. Chuyen Dev sua 2 loi.
- **Loi 1:** khong hien danh sach hoc vien khi khoa "Dang dien ra". BA chot: diem kiem tra duoc phep nhap khi khoa
  "Dang dien ra" HOAC "Da ket thuc" (UC24 khong kem rang buoc trang thai). Viec phan mem khoa tab "Ket qua" khi
  khoa dang dien ra la chan mot chuc nang ma baseline cho phep -> Dev bo chan.
- **Phan biet:** rang buoc "sau khi khoa hoc ket thuc" thuoc UC36 (trinh phe duyet ket qua), khong phai UC24.
  Nhap diem duoc tu khi khoa dang dien ra; trinh duyet ket qua thi van phai cho khoa ket thuc.
- **Loi 2:** nhap diem >10 tu keo ve 10. Theo SRS FR-III-05 muc Xu ly loi, ma **ERR-KQ-01**, he thong phai TU CHOI
  va hien "Diem kiem tra phai tu 0 den 10"; rang buoc du lieu la **chan ghi chu khong sua gia tri**. Tu keo ve 10
  khien loi go nham (go 15 thay vi 1.5) thanh diem 10 -> xep loai Gioi -> Dat -> cong bo ma khong ai phat hien.
- **Verify lai (5 y):**
  1. Khoa "Dang dien ra" -> tab Ket qua kiem tra: HIEN danh sach hoc vien va nhap duoc diem (nut Luu khong con bi khoa).
  2. Khoa chua ket thuc -> tab Ket qua kiem tra co nhan **"Ket qua tam tinh"**.
  3. Nhap 15 -> he thong TU CHOI + bao "Diem kiem tra phai tu 0 den 10" (ERR-KQ-01), o van giu nguyen 15 chu khong
     tu thanh 10. Nhap 1.5 -> luu binh thuong.
  4. Lap lai muc 3 voi duong nhap tu file Excel - cung phai tu choi + bao loi, khong tu keo ve 10.
  5. Khoa "Dang dien ra" -> nhap diem duoc NHUNG chua trinh phe duyet ket qua duoc; chi trinh duyet duoc khi khoa
     "Da ket thuc" (FR-III-17).

| Điều kiện | Yêu cầu BA / case gốc | Mình test (verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo nghiep vu | `cbnv_tw` "CB Nghiep vu - Trung uong", badge CB_NV_TW, don vi BTP · TW | Khong |
| Man hinh | Dao tao, tap huan -> Khoa hoc -> chi tiet -> tab **Ket qua kiem tra** | Dung tab **Ket qua** cua man chi tiet khoa hoc (ten tab tren phan mem la "Ket qua") | Khong |
| Trang thai khoa (y 1,2,3,5) | **"Dang dien ra"** (o Dieu kien case: "Dang dien ra" hoac "Da ket thuc"; BA giu nguyen o Dieu kien) | Khoa **KH-20260716-002** "QA RV5 - Khoa hoc test diem danh theo buoi", trang thai **"Dang dien ra"** (thanh buoc hien buoc 4 dang chay) - tu tao tien de | Khong |
| Trang thai khoa (kiem chung y 5) | Chi trinh duyet ket qua duoc khi **"Da ket thuc"** | Da bam **[Ket thuc]** that -> khoa chuyen **"Da ket thuc"** -> doc lai bo nut | Khong |
| Du lieu tien de | Khoa co hoc vien da duyet de cham diem | 2 hoc vien "QA HV RV5 Mot" / "QA HV RV5 Hai" da phe duyet dang ky, da co du lieu chuyen can (1/2) | Khong |
| Thao tac | Nhap diem khong hop le -> bam Luu | Da go **15** that vao o Diem kiem tra roi bam **[Luu ket qua]**; roi go **1.5** roi Luu; moi lan deu **tai lai trang hoan toan** de kiem may chu co ghi that khong | Khong |

Seed tien de: dung lai khoa **KH-20260716-002** da tao o case KTDGKQHT_03 (moi truong khong co khoa nao vua
"Dang dien ra" vua co lich hoc + hoc vien da duyet). Chi tiet quy trinh tao: xem `KTDGKQHT_03.md` cung thu muc.

Ket qua quan sat (UI, khong dung API de ra verdict):

**Y 1 - khoa "Dang dien ra" hien danh sach hoc vien + nhap duoc diem: DAT - DA FIX.**
- Tab **Ket qua** mo binh thuong khi khoa dang o **"Dang dien ra"** (khong con bi khoa).
- Bang hien **du 2 hoc vien** kem cot Ho ten / Email / So dien thoai / Don vi / Chuyen can / Diem kiem tra /
  Ket qua / Xep loai / Ghi chu. Khong con bang trong.
- O nhap diem **sua duoc** (khong disabled, khong readonly). Nut **[Luu ket qua]** ban dau xam (chua co thay doi),
  **mo khoa ngay khi go diem vao** -> dung y "nut Luu khong con bi khoa".
- Day la muc chinh cua Loi 1 -> **da fix**.

**Y 2 - nhan "Ket qua tam tinh" khi khoa chua ket thuc: KHONG DAT.**
- Khoa dang **"Dang dien ra"** (chua ket thuc) nhung tab **khong co** chu "tam tinh" o bat ky dau.
- Da quet **toan bo chu tren trang** (`/tạm tính/i`) = **khong tim thay**; quet ca cac bien the "tam thoi",
  "chua chinh thuc", "du kien" = cung khong co.
- Tieu de khu vuc chi la **"Ket qua"** tron. Ten tab cung chi la **"Ket qua"**.
- **Da tai lai trang hoan toan roi do lai** de tranh bao nham do render cham -> van khong co.
- => Y 2 BA chot **chua duoc lam**.

**Y 3 - nhap 15 phai tu choi, khong tu keo ve 10: DAT - DA FIX (ca 2 ve).**
- Go **15** vao o Diem kiem tra cua hoc vien "QA HV RV5 Hai" -> roi o (blur):
  o **van giu nguyen 15.0**, **KHONG tu keo ve 10**. ✅ (day la loi goc)
- Bam **[Luu ket qua]** -> he thong **tu choi**, hien thong bao nguyen van
  **"Diem kiem tra phai tu 0 den 10"** - **dung nguyen van** chuoi trong KQ mong doi cua case goc va dung
  ma **ERR-KQ-01** BA dan. ✅
- Sau khi bi tu choi: o **van giu 15.0**, cot Ket qua / Xep loai van la "—" -> **khong ghi gi vao du lieu**. ✅
- Ve con lai: go **1.5** -> bam Luu -> **"Da luu ket qua"**, cot Ket qua/Xep loai cap nhat.
  **Tai lai trang hoan toan** -> o van la **1.5** -> may chu **ghi dung 1.5**, khong bi lam tron thanh 10 hay 2. ✅
- => Kich ban nguy hiem BA lo (go nham 15 thay vi 1.5 -> thanh 10 -> Gioi/Dat) **da het**.

**Y 4 - lap lai y 3 qua duong nhap Excel: KHONG KIEM DUOC (phan mem khong co duong nay).**
- Ra soat **toan bo 7 tab** cua man chi tiet khoa hoc, nut "Import Excel" chi co o **2 cho**:
  - Tab **Hoc vien** -> import **danh sach dang ky** (khong phai diem).
  - Tab **Diem danh** -> import **diem danh**; mo hop thoai doc duoc mo ta mau file:
    *"Cot bat buoc: Ma hoc vien, Co mat (1/0)"* -> **khong co cot diem**.
- Tab **Ket qua** chi co **[Luu ket qua]** va **[Xuat DOCX]** - **khong co nut import/tai len nao**,
  trang khong co o chon file nao (`input[type=file]` = 0).
- => **Khong ton tai duong nhap diem kiem tra tu Excel** trong phan mem, nen khong co gi de kiem o y 4.
- **Khong ket luan day la loi**: KQ mong doi cua case goc khong doi hoi duong Excel; y 4 co ve la BA gia dinh
  duong Excel co san. **De nghi BA xac nhan**: hoac bo y 4, hoac neu thuc su can nhap diem tu Excel thi day la
  chuc nang **chua co** can Dev bo sung (viec khac, khong phai loi cua case nay).

**Y 5 - dang dien ra thi chua trinh phe duyet ket qua duoc: DAT.**
- Khi khoa **"Dang dien ra"**: bo nut cuoi man chi co **[Cong khai] [Ket thuc]** - **khong co** nut trinh/gui
  duyet ket qua nao. ✅ (nhap diem thi duoc - da chung minh o y 1/y 3)
- **Kiem chung nut bi chan theo trang thai chu khong phai khong ton tai:** bam **[Ket thuc]** -> hop thoai
  *"Ket thuc khoa hoc? Khoa hoc se chuyen sang trang thai Da ket thuc. **Sau buoc nay co the trinh duyet ket qua
  dao tao.**"* -> xac nhan -> khoa chuyen **"Da ket thuc"** va bo nut **doi thanh [Cong khai] [Gui duyet KQ]**.
- => Dung FR-III-17 / UC36: nhap diem duoc tu khi dang dien ra, con **gui duyet ket qua chi mo ra sau khi khoa
  ket thuc**. Hai viec da tach dung nhu BA phan biet. ✅

**Ghi nhan them - xac nhan lai BUG-KTDGKQHT_03 tren khoa THU HAI (khong phai seed):**
Khoa KH-20260716-002 vua chuyen **"Da ket thuc"** o y 5. Mo ngay tab **Diem danh**: nut "Luu diem danh"
**mo khoa sau khi chon buoi**, o chon trang thai **van sua duoc**. Doi "QA HV RV5 Mot" tu Co mat ->
**Vang khong phep** -> Luu -> **"Da luu diem danh"** -> **tai lai trang hoan toan** -> van la "Vang khong phep".
=> Loi "khoa Da ket thuc van sua duoc diem danh" **lap lai tren khoa thu hai**, khong phai loi rieng cua ban ghi
seed KH-SEED-0001. Cung co them cho BUG-KTDGKQHT_03 (row 5).

Ket luan: dat **3/5** y BA chot (y 1 - bo chan tab Ket qua khi dang dien ra; y 3 - tu choi diem 15 dung nguyen van
va khong keo ve 10; y 5 - chi gui duyet KQ sau khi ket thuc). **Khong dat y 2** (thieu nhan "Ket qua tam tinh").
**Y 4 khong kiem duoc** vi phan mem khong co duong nhap diem tu Excel -> **Reopen (fix mot phan)**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv5-KTDGKQHT_08-nhap-15-bi-tu-choi.png`
  (khoa dang o buoc 4 "Dang dien ra"; tab Ket qua hien du 2 hoc vien; o diem giu nguyen **15.0**;
  thong bao da ghim **"Diem kiem tra phai tu 0 den 10"**; tieu de chi la "Ket qua" - **khong co** chu "tam tinh";
  bo nut cuoi man chi co [Cong khai] [Ket thuc] - chua co nut gui duyet KQ)
- `../../bug-reports/ba-approved-batch/image/rv5-KTDGKQHT_08-da-ket-thuc-moi-hien-gui-duyet-kq.png`
  (sau khi bam Ket thuc: buoc 5 "Da ket thuc", nut doi thanh **[Gui duyet KQ]**; dong thoi thay tab Diem danh
  cua khoa da ket thuc **van sua va luu duoc** - "QA HV RV5 Mot = Vang khong phep" giu sau khi tai lai)
