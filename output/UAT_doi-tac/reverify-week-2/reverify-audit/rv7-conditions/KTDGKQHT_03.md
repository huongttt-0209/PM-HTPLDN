# Bang doi chieu dieu kien - KTDGKQHT_03 (re-verify vong 7, 2026-07-17 - sau khi dev bao fix lan 3)

Boi canh: 2 vong truoc (rv5, rv6) deu **Reopen** - dat 3/4 y BA chot, khong dat y 4 (khoa "Da ket thuc" van sua
va luu duoc diem danh). Dev bao da fix -> chay lai y 4 + kiem 3 y da dat co hong nguoc khong.

**Lan nay dev CO deploy that** (khac 2 vong truoc): ma bang (hash) goi giao dien khoa hoc da doi
`use-khoa-hoc-queries-pqfbh4Ty.js` -> `use-khoa-hoc-queries-OBoex2nl.js`. Vong rv6 hash y nguyen nen
hanh vi khong doi; vong nay hash doi va hanh vi cung doi that.

Can cu SRS (da mo file doc tan noi):
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:533` - FR-III-05 **PRE-03**:
  *"**Nhap diem danh:** khoa hoc o `DANG_DIEN_RA`. Khi khoa chuyen `DA_KET_THUC` thi **diem danh dong**"*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5759` - SM-KHOAHOC: tac dong
  *"**Dong diem danh** (FR-III-05 PRE-03)"*

| Điều kiện | Bug gốc / yêu cầu BA | Mình test (re-verify 2026-07-17 vòng 7) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo nghiep vu vao tab Diem danh | `cbnv_tw`, badge **CB_NV_TW** "CB Nghiep vu - Trung uong" (doc tren ảnh) | Không |
| Man hinh | Dao tao, tap huan -> Khoa hoc -> chi tiet -> tab **Diem danh** | Dung tab **Diem danh** cua man chi tiet khoa hoc | Không |
| Trang thai khoa (y 4) | Khoa **"Da ket thuc"** | Khoa **KH-SEED-0001** (`5eed0002-...-0001`), stepper **"Da ket thuc"** active (buoc 5) - dung state bug goc | Không |
| Du lieu tien de | Khoa co buoi hoc + hoc vien da duyet | 2 buoi seed cung ngay 20/02/2026 (SANG 08:00-11:00 / CHIEU 14:00-17:00) + 1 hoc vien "QA Import Reverify12 OK" da duyet - y nguyen tien de 2 vong truoc | Không |
| Thao tac | Chon buoi -> thu sua trang thai -> thu Luu | Chon buoi SANG -> kiem tung o co sua duoc khong; kiem them tang may chu bang cach gui dung yeu cau ma man hinh tung gui | Không |

## Ket qua quan sat (UI la can cu ra verdict; tang may chu chi de dieu tra them)

**Y 1 - dong nhac khi chua chon buoi: DAT (khong hong nguoc).**
- Chua chon buoi -> hien dung dong **"Vui long chon buoi hoc de bat dau diem danh"**.

**Y 2 - bo chon la danh sach BUOI HOC: DAT (khong hong nguoc).**
- Placeholder **"Chon buoi hoc de diem danh"**; `.ant-picker` = khong ton tai (khong con o chon ngay).
- Xo ra 2 dong du **Ngay · Khung gio · Noi dung**, 2 buoi cung ngay hien thanh 2 dong rieng.

**Y 3 - 2 buoi cung ngay doc lap: DAT (kiem o muc doc).**
- Doc lai 2 buoi cua cung 1 hoc vien tren cung ngay 20/02/2026: buoi SANG = **Co mat**, buoi CHIEU = **khong co
  ban ghi** (may chu tra `id: ""`, `trangThai: null`) -> **2 buoi luu tach bach**, khong dinh nhau.
- **Han che da khai bao:** khoa nay nay **chi doc** (dung y 4) nen **khong ghi lai duoc** de kiem duong ghi tren
  build moi. Duong ghi da duoc chung minh day du o vong rv5 (build cu, ghi that + tai lai trang). Moi truong
  hien **khong co khoa nao vua "Dang dien ra" vua co buoi hoc** (DDD-KH-011 "Dang dien ra" nhung 0 buoi va
  **khong them buoi duoc** - xem muc Ghi nhan them) nen chua kiem lai duong ghi tren build moi.

**Y 4 - khoa "Da ket thuc" thi tab Diem danh chi doc: DAT — DA FIX THAT.**
- Bo nut da doi: chi con **[Xuat Excel]**; **mat han [Luu diem danh] va [Import Excel]**.
- Sau khi chon buoi SANG: **ca 3 o trang thai** (Co mat / Vang co phep / Vang khong phep) deu `disabled: true`,
  o **"Ly do vang..."** cung `disabled: true` -> **khong sua duoc gi**. Gia tri da luu ("Co mat") van hien dung.
- **Kiem them tang may chu** (dieu tra, khong dung ra verdict): gui dung yeu cau ghi diem danh ma man hinh
  tung gui hoi truoc -> may chu tra **HTTP 403** `ERR-BIZ-III-05-01: "Chi diem danh duoc khi khoa hoc dang dien ra"`.
  -> Fix **dung bai**: chan o **ca giao dien lan may chu**, khong phai chi an nut. Khong co du lieu nao bi ghi.
- => Dung **PRE-03** (`srs-fr-03-dao-tao.md:533`) va dung tac dong **"Dong diem danh"** (`srs-v3.5.md:5759`).

## Ngoai tieu chi BA - co thay gi bat thuong khong? CO - 1 loi MOI

**LOI MOI (ngoai pham vi case, da mo dong TC rieng):** buoi hoc **chua he diem danh** thi giao dien lai tick san
**"Vang khong phep"**.
- Buoi CHIEU cua KH-SEED-0001: may chu tra `id: ""`, `trangThai: **null**`, `coMat: false` (= chua co ban ghi
  diem danh nao) nhung giao dien **tick san "Vang khong phep"**.
- Da loai tru kha nang doc nham truong: doc **nguyen van** phan hoi may chu (khong qua bo loc cua minh).
- Da loai tru kha nang "dinh trang thai tu buoi truoc": **tai lai trang hoan toan** roi chon **thang buoi CHIEU**
  (khong he dung buoi SANG) -> van tick "Vang khong phep".
- Nghi nguyen nhan: giao dien suy ra o chon tu `coMat: false` thay vi tu `trangThai: null` - ma `coMat` mac dinh
  `false` khi **chua co ban ghi**.
- **La loi MOI do build vua deploy**: vong rv5 ghi ro buoi chua diem danh thi *"bang chua chon gi"*.
- Chi tiet + danh gia muc do: xem dong TC moi **QLKH_03** (bug `BUG-DD-VANG-MA`).

**Loi cu VAN CON (da ghi tu rv5):** ban ghi seed **DDD-KH-011** hong - "Dang dien ra" nhung bam "Them buoi hoc"
bao **"Khoa hoc khong ton tai"** (1 request `POST .../lich-hocs`, 1 thong bao loi). Chinh vi loi nay ma moi truong
khong con khoa nao vua "Dang dien ra" vua co buoi hoc.

## Ket luan

Dat **4/4** y BA chot -> **Pass**. Y 4 (thu cuoi cung con lai sau 2 vong Reopen) da fix that, chan o ca giao dien
lan may chu. Khong y nao hong nguoc.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv7-KTDGKQHT_03-da-ket-thuc-chi-doc-PASS.png`
  (da mo doc lai pixel: stepper **"Da ket thuc"** active · tab Diem danh · da chon buoi SANG ·
  **chi con nut [Xuat Excel]**, mat [Luu diem danh] · **ca 3 o trang thai + o Ghi chu deu xam mo** ·
  gia tri "Co mat" van hien dung)
- `../../bug-reports/ba-approved-batch/image/rv7-BUG-DD-VANG-MA-buoi-chua-diem-danh.png` (loi moi phat hien them)
