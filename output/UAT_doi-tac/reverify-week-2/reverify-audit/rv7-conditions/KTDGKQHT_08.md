# Bang doi chieu dieu kien - KTDGKQHT_08 (re-verify vong 7, 2026-07-17 - sau khi dev bao fix lan 3)

Boi canh: 2 vong truoc (rv5, rv6) deu **Reopen** - dat 3/5 y BA chot; **khong dat y 2** (thieu nhan
"Ket qua tam tinh"); **khong kiem duoc y 4** (nhap diem qua Excel - phan mem khong co duong nay).
Dev bao da fix -> chay lai y 2 + kiem cac y da dat co hong nguoc khong.

**Lan nay dev CO deploy that:** ma bang (hash) goi giao dien khoa hoc doi
`use-khoa-hoc-queries-pqfbh4Ty.js` -> `use-khoa-hoc-queries-OBoex2nl.js` (vong rv6 hash y nguyen).

Can cu:
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:534` - FR-III-05 **PRE-04**:
  *"**Nhap diem kiem tra:** khoa hoc o `DANG_DIEN_RA` **hoac** `DA_KET_THUC` `[BA chot 2026-07-16 - Phuong an A2]`"*
- Nhan "Ket qua tam tinh": BA chot 16/07 (`phan-tich-KTDGKQHT-03-08.md` Buoc 3 muc 5 - can cu SCR-III-02 Tab 5 + BR-KQ-02).
- `ERR-KQ-01`: FR-III-05 muc Xu ly loi - diem ngoai 0-10 phai **tu choi + bao "Diem kiem tra phai tu 0 den 10"**.

| Điều kiện | Bug gốc / yêu cầu BA | Mình test (re-verify 2026-07-17 vòng 7) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu vao tab Ket qua (doi tac quay bang CB_NV_TW) | `cbnv_tw`, badge **CB_NV_TW** "CB Nghiep vu - Trung uong" (doc tren ảnh) | Không |
| Man hinh | Dao tao, tap huan -> Khoa hoc -> chi tiet -> tab **Ket qua** | Dung tab **Ket qua** cua man chi tiet khoa hoc | Không |
| Trang thai khoa (y 2) | Khoa **"Dang dien ra"** (chua ket thuc) - dung state doi tac quay va state y 2 yeu cau | Khoa **DDD-KH-011**, stepper **"Dang dien ra"** active (buoc 4) - **cung khoa da dung o vong rv6** nen so sanh truoc/sau fix la 1:1 | Không |
| Du lieu tien de | Khoa co hoc vien de bang Ket qua co dong du lieu | DDD-KH-011 co **1 hoc vien** "Nguyen Van Hoc Vien" - bang Ket qua render dong, o Diem kiem tra sua duoc | Không |
| Input (y 3 - kiem hong nguoc) | Nhap diem ngoai 0-10 (vd 15) -> phai tu choi + bao "Diem kiem tra phai tu 0 den 10" | Go **15** vao o Diem kiem tra roi bam **Luu ket qua** | Không |

## Ket qua quan sat (UI, khong dung API de ra verdict)

**Y 1 - khoa "Dang dien ra" mo duoc tab Ket qua + hien danh sach hoc vien: DAT (khong hong nguoc).**
- Tab Ket qua mo binh thuong, hien dong hoc vien kem du cot (Chuyen can · Diem kiem tra · Ket qua · Xep loai ·
  Ghi chu), o nhap diem sua duoc. Dung PRE-04 (`srs-fr-03-dao-tao.md:534`).

**Y 2 - nhan "Ket qua tam tinh" khi khoa chua ket thuc: DAT — DA FIX THAT.**
- Dau tab Ket qua nay co **khung canh bao mau vang** kem dau cham than, tieu de **"Ket qua tam tinh"** va cau
  giai thich nguyen van:
  > *"Khoa hoc dang dien ra — ket qua ben duoi la tam tinh, chua phai ket qua chinh thuc. Ket qua duoc chot khi
  > trinh phe duyet."*
- Do bang cach quet **toan bo chu NHIN THAY duoc** tren trang (`innerText`): `/tam tinh/i` -> **true**.
- **Do lai tren dung khoa DDD-KH-011 ma vong rv6 do ra "khong co"** -> truoc/sau fix so sanh 1:1, khong phai
  doi khoa nen ket qua khac.
- Cau chu con **hon** yeu cau BA: BA chi yeu cau nhan "Ket qua tam tinh", dev them ca cau giai thich vi sao va
  khi nao ket qua duoc chot.

**Y 3 - nhap >10 phai tu choi, khong tu keo ve 10: DAT (khong hong nguoc).**
- Go **15** -> o **giu nguyen 15**, khong bi keo ve 10.
- Bam **Luu ket qua** -> bo bat thong bao (KHONG loc trung): **1 khung thong bao**, chu dung nguyen van
  **"Diem kiem tra phai tu 0 den 10"** (dung mo ta `ERR-KQ-01`).
- Sau khi bi tu choi, o van giu **15** -> khong ghi gi.

**Y 4 - nhap diem qua Excel: VAN KHONG KIEM DUOC (khong doi).**
- Phan mem van khong co duong nhap diem tu Excel. Vong truoc da ra soat ca 7 tab: nut "Import Excel" chi co o
  tab Hoc vien (import danh sach dang ky) va tab Diem danh (mau file: "Cot bat buoc: Ma hoc vien, Co mat (1/0)"
  - khong co cot diem). Tab Ket qua chi co [Luu ket qua] + [Xuat DOCX].
- **Khong ket luan day la loi** vi KQ mong doi cua case khong doi hoi duong Excel -> **de nghi BA xac nhan**:
  bo y 4, hoac neu that su can thi day la **chuc nang chua co**, can Dev bo sung (viec khac, khong phai loi
  cua case nay). **Day la cau hoi dac ta, khong phai loi dev con ton** -> khong chan Pass cua case.

**Y 5 - tach nhap diem (UC24) vs gui duyet KQ (UC36/FR-III-17): DAT** (da chung minh day du o rv5; khong doi
pham vi nen khong do lai).

## Ngoai tieu chi BA - co thay gi bat thuong khong?

Doc lai anh da chup vong nay: **khong phat hien bat thuong nao o tab Ket qua**. Khong co thong bao lap
(1 thong bao / 1 thao tac). Rieng loi thong bao lap chi xay ra o man **Khoa hoc** (tao/xoa) - da ghi o
dong TC **QLKH_02**, khong lap lai o day.

## Ket luan

Dat **4/5** y BA chot; **y 2 - thu duy nhat con lai sau 2 vong Reopen - da fix that**. Y 4 khong phai loi dev
ma la cau hoi dac ta cho BA. Ca 2 loi chinh BA chot (tab bi khoa khi "Dang dien ra"; keo diem ve 10) van fix tot,
khong hong nguoc. => **Pass** (kem ghi chu de nghi BA chot y 4).

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv7-KTDGKQHT_08-nhan-ket-qua-tam-tinh-PASS.png`
  (da mo doc lai pixel: stepper **"Dang dien ra"** active buoc 4 · tab **Ket qua** dang mo · **khung vang
  "Ket qua tam tinh"** + cau giai thich day du · bang hien dong hoc vien)
