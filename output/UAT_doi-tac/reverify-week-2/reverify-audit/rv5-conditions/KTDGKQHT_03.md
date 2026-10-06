# Bang doi chieu dieu kien - KTDGKQHT_03 (verify dev-fix 2026-07-16, lan dau)

Yeu cau BA (note sheet row 5, chot 16/07/2026): Giu Fail mot phan - khong phai bug o phan chinh, co 2 viec chuyen Dev.
- Bang danh sach hoc vien trong khi CHUA CHON BUOI la **dung thiet ke** (FR-III-05: diem danh gan voi lich_hoc_id).
- Chuyen Dev: (a) doi bo chon tu O CHON NGAY sang **danh sach BUOI HOC (Ngay · Khung gio · Noi dung)** - vi 1 ngay
  co the co 2 buoi sang/chieu, chon theo ngay se ghi sai buoi -> sai chuyen can -> sai ket qua Dat/Khong dat;
  (b) bo sung dong **"Vui long chon buoi hoc de bat dau diem danh"** khi chua chon buoi.
- **Verify lai (4 y):**
  1. Mo tab Diem danh khi chua chon buoi -> hien dong "Vui long chon buoi hoc de bat dau diem danh", khong con bang trong tron.
  2. Bo chon la danh sach BUOI HOC, moi buoi hien Ngay · Khung gio · Noi dung - khong con la o chon ngay.
  3. Khoa co 2 buoi cung 1 ngay (sang/chieu): chon tung buoi -> diem danh doc lap, 1 hoc vien ghi duoc Co mat buoi sang
     + Vang buoi chieu, luu thanh cong ca 2 (khong con loi "can truyen lichHocId").
  4. Khoa o trang thai **"Da ket thuc"** -> tab Diem danh **chi doc**, khong luu duoc diem danh nua.

| Điều kiện | Yêu cầu BA / case gốc | Mình test (verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo nghiep vu vao tab Diem danh cua khoa hoc | `cbnv_tw` "CB Nghiep vu - Trung uong", badge CB_NV_TW | Khong |
| Man hinh | Dao tao, tap huan -> Khoa hoc -> chi tiet -> tab **Diem danh** | Dung tab **Diem danh** cua man chi tiet khoa hoc | Khong |
| Trang thai khoa (y 1-3) | **"Dang dien ra"** va **da co lich hoc** (dieu kien case; BA da chot bo "Da ket thuc" khoi dieu kien) | Khoa **KH-20260716-002** "QA RV5 - Khoa hoc test diem danh theo buoi", trang thai **"Dang dien ra"**, co **2 buoi hoc** - tu tao tien de (xem muc Seed) | Khong |
| Trang thai khoa (y 4) | **"Da ket thuc"** | Khoa **KH-SEED-0001** "Khoa hoc phap luat doanh nghiep seed", trang thai **"Da ket thuc"**, co san 2 buoi seed (sang/chieu 20/02/2026) + 1 hoc vien da duyet | Khong |
| Du lieu tien de | Khoa co **2 buoi cung 1 ngay** (sang/chieu) + hoc vien da duyet | 2 buoi **cung ngay 20/09/2026**: SANG 08:00-11:30 va CHIEU 13:30-17:00; 2 hoc vien "QA HV RV5 Mot" / "QA HV RV5 Hai" da phe duyet dang ky | Khong |
| Thao tac | Chon tung buoi -> ghi trang thai -> Luu -> tai lai kiem con giu khong | Da chay that ca 4 y, moi lan luu deu **tai lai trang hoan toan** roi doc lai de kiem may chu co ghi that khong | Khong |

Seed tien de (theo nguyen tac "thieu tien de thi TU TAO"): moi truong khong co khoa nao vua "Dang dien ra" vua co
lich hoc. Khoa DDD-KH-011 tuy "Dang dien ra" nhung **khong them duoc buoi hoc** (bao "Khoa hoc khong ton tai" -
ban ghi seed hong, xem muc Ghi nhan them). Nen tu di het quy trinh: tao khoa moi (dien du thong tin van hanh) ->
them 2 buoi cung ngay -> Trinh phe duyet -> `cbpd_tw` Phe duyet -> them 2 hoc vien -> Phe duyet dang ky ->
**Khai giang** -> khoa vao **"Dang dien ra"**.

Ket qua quan sat (UI, khong dung API de ra verdict):

**Y 1 - dong nhac khi chua chon buoi: DAT.**
- Mo tab Diem danh, chua chon buoi -> bang hien dong **"Vui long chon buoi hoc de bat dau diem danh"**,
  khong con la bang trong tron. ✅

**Y 2 - bo chon la danh sach BUOI HOC: DAT.**
- Bo chon co placeholder **"Chon buoi hoc de diem danh"**, la o **chon tu danh sach** (khong phai o chon ngay -
  kiem bang `.ant-picker` = khong ton tai). ✅
- Moi lua chon hien **du 3 phan: Ngay · Khung gio · Noi dung**, vi du:
  `20/09/2026 · 08:00:00-11:30:00 · Buoi SANG - QA RV5 KTDGKQHT_03`
  `20/09/2026 · 13:30:00-17:00:00 · Buoi CHIEU - QA RV5 KTDGKQHT_03`
- 2 buoi **cung mot ngay** hien thanh **2 dong rieng** -> phan biet duoc sang/chieu, dung y BA lo. ✅

**Y 3 - 2 buoi cung ngay diem danh doc lap: DAT.**
- Chon buoi **SANG** -> ghi ca 2 hoc vien = **Co mat** -> Luu -> thong bao **"Da luu diem danh"**
  (dung nguyen van KQ mong doi cua case goc). ✅
- Chuyen sang buoi **CHIEU** -> bang **chua chon gi** (khong bi keo theo trang thai buoi sang) -> ghi
  "QA HV RV5 Mot" = **Vang khong phep**, "QA HV RV5 Hai" = **Vang co phep** -> Luu -> **"Da luu diem danh"**. ✅
- **Tai lai trang hoan toan** roi doc lai ca 2 buoi:
  - Buoi SANG: Mot = **Co mat**, Hai = **Co mat**
  - Buoi CHIEU: Mot = **Vang khong phep**, Hai = **Vang co phep**
  - => 2 buoi cung 1 ngay ghi **hoan toan doc lap**; cung 1 hoc vien **Co mat buoi sang + Vang buoi chieu**,
    luu thanh cong ca 2, **khong con loi "can truyen lichHocId"**. Dung nguyen van y 3 cua BA. ✅

**Y 4 - khoa "Da ket thuc" thi tab Diem danh chi doc: KHONG DAT.**
- Khoa **KH-SEED-0001** dang **"Da ket thuc"**.
- Truoc khi chon buoi: nut "Luu diem danh" **bi khoa** -> nhin qua tuong nhu chi doc.
- **Nhung sau khi chon buoi thi nut "Luu diem danh" MO KHOA**, cac o chon trang thai va o Ghi chu **van sua duoc**.
- **Da thu thuc thi that:** doi hoc vien "QA Import Reverify12 OK" tu **"Co mat" -> "Vang khong phep"** ->
  bam Luu -> he thong bao **"Da luu diem danh"**. **May chu KHONG chan.**
- **Tai lai trang hoan toan** -> trang thai van la **"Vang khong phep"** => du lieu **da bi ghi that**, khong phai
  chi doi tren giao dien.
- => Tab Diem danh cua khoa **"Da ket thuc"** **KHONG chi doc**; can bo van sua va luu duoc diem danh sau khi khoa
  da dong. Trai voi y 4 BA chot ("tab Diem danh chi doc, khong luu duoc diem danh nua").
- **Da khoi phuc du lieu seed ve "Co mat"** sau khi lay bang chung.

**Ghi nhan them (ngoai pham vi case, de dev biet):**
1. **Ban ghi seed DDD-KH-011 hong:** khoa nay "Dang dien ra" nhung bam "Them buoi hoc" thi bao
   **"Khoa hoc khong ton tai"** (lap lai 2 lan, ke ca sau khi tai lai trang). Cung thao tac do chay **binh thuong**
   tren khoa khac -> loi thuoc ban ghi seed, khong phai chuc nang.
2. **Khoa "Cho duyet" bi ket:** khoa da trinh duyet nhung thieu thong tin van hanh thi **khong sua duoc**
   ("ERR-STATE-III-01-01: Khong the sua khoa hoc da duoc duyet") ma **cung khong duyet duoc**
   ("ERR-VAL-III-15-04: Khoa hoc thieu thong tin van hanh truoc khi phe duyet: doiTuong, diaDiem, soLuong").
   Khoa KH-20260716-001 hien dang ket o trang thai nay.
3. **Tab Diem danh khong tu lam moi:** sau khi phe duyet dang ky hoc vien, tab Diem danh van bao "Chua co hoc vien
   da duyet cho buoi hoc nay" cho den khi tai lai trang.

Ket luan: dat **3/4** y BA chot (dong nhac chon buoi + bo chon la danh sach buoi hoc + 2 buoi cung ngay doc lap),
**khong dat y 4** (khoa "Da ket thuc" van sua va luu duoc diem danh, may chu khong chan) -> **Reopen (fix mot phan)**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv5-KTDGKQHT_03-bo-chon-la-danh-sach-buoi-hoc.png`
  (bo chon "Chon buoi hoc de diem danh" xo ra 2 buoi cung ngay dang Ngay · Khung gio · Noi dung + dong
  "Vui long chon buoi hoc de bat dau diem danh")
- `../../bug-reports/ba-approved-batch/image/rv5-KTDGKQHT_03-hai-buoi-cung-ngay-doc-lap.png`
  (sau khi tai lai: buoi CHIEU giu dung Vang khong phep / Vang co phep, doc lap voi buoi SANG)
- `../../bug-reports/ba-approved-batch/image/rv5-KTDGKQHT_03-khoa-da-ket-thuc-van-sua-duoc-diem-danh.png`
  (khoa KH-SEED-0001 "Da ket thuc": sau khi tai lai, diem danh da bi doi thanh "Vang khong phep" va luu duoc)
