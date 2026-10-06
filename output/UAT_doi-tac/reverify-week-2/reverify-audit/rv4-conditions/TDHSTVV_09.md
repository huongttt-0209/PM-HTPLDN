# Bang doi chieu dieu kien - TDHSTVV_09 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 65, duyet 15/07/2026 - chuyen Dev FE):
- Mat ket noi khi bam "Luu nhap" phai bao loi. Hien he thong NUOT LOI IM LANG: khong bao gi, nut quay vong mai
  khong dung, ban nhap thuc ra da hong -> can bo tuong da luu. Nguy co mat trang du lieu.
- **Viec can lam: hien thong bao loi mat ket noi + DUNG spinner + co nut Thu lai.** Mau san co o module Vu viec:
  "Luu that bai, vui long kiem tra ket noi va thu lai" (srs-fr-05:1567, :1574).
- BA nang quy uoc bao loi mat ket noi cua module Vu viec thanh QUY UOC CHUNG, ap moi module
  (module IV hien chi liet ke 3 loi nghiep vu, srs-fr-04:539-541).
- Cung goc voi BUG-TDHSTVV_08.
- **Verify lai: ngat mang -> bam Luu nhap -> hien thong bao loi, spinner dung, co nut Thu lai.**

Case goc (sheet row 65): KQ mong doi = 'He thong hien thi thong bao "Khong the luu, vui long thu lai".'
KQ thuc te doi tac = "He thong khong hien thi thong bao loi".

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu Trung uong (vong truoc: badge CB_NV_TW, don vi BTP · TW) | `cbnv_tw` "CB Nghiep vu - Trung uong", badge CB_NV_TW, don vi BTP · TW | Khong |
| Man hinh | Tab "Tham dinh" cua ho so TVV, nut "Luu nhap" | Tab "Tham dinh" cua ho so TVV, nut "Luu nhap" (cung nut, cung man) | Khong |
| Trang thai ho so | **"Dang tham dinh"** (trang thai bug goc, vong truoc doc tu video doi tac) | Ho so **TVV-BTP-TW-0014 "QA TVV RV4 Tham Dinh Offline"**, trang thai **"Dang tham dinh"** - tu tao tien de vi the "Dang tham dinh" dang rong (xem muc Seed duoi) | Khong |
| Du lieu tien de | Bieu mau tham dinh da dien, Ket luan tham dinh = DAT | Da dien: Ket luan Phap ly = Dat, 3 o Nhan xet (Nhom 2/3/4) co noi dung, Ket luan tham dinh = **DAT** | Khong |
| Dieu kien mang | **Mat ket noi mang** roi bam "Luu nhap" | **Mat ket noi that**: bat che do Offline cua trinh duyet -> `navigator.onLine = false` va moi yeu cau ra may chu nem `TypeError: Failed to fetch` (da kiem chung trong cung phien) | Khong |
| Thao tac | Bam "Luu nhap" khi dang mat mang | Da bam that. Quan sat bang MutationObserver cai **truoc** cu bam (toast tu tat sau ~3s nen khong the poll sau) | Khong |

Seed tien de (theo nguyen tac "thieu tien de thi TU TAO"): the "Dang tham dinh" va "Cho tham dinh" deu **rong**,
2 ho so o "Yeu cau bo sung" thi tab Tham dinh bi **khoa**. Nen tu tao 1 ho so TVV moi qua nut "Them moi"
(11 truong bat buoc + file the hanh nghe PDF) -> ho so vao the "Moi dang ky" (TVV-BTP-TW-0014). Bam "Luu nhap"
lan dau **khi con mang** -> he thong bao "Da luu ket qua tham dinh" va chuyen ho so **Moi dang ky -> Dang tham dinh**.
Den day moi dung trang thai bug goc, roi moi ngat mang va chay lai dung thao tac "Luu nhap".

Ket qua quan sat (UI, khong dung API de ra verdict):

**Y 1 - hien thong bao loi mat ket noi: DAT.**
- Bam "Luu nhap" khi offline -> hien toast **"Khong ket noi duoc may chu."** (bat duoc bang MutationObserver,
  da ghim lai de chup anh vi toast tu tat sau ~3s).
- Truoc day: khong bao gi ca -> **loi goc "nuot loi im lang" DA HET**.

**Y 2 - dung spinner: DAT.**
- Sau cu bam, do lai toan bo nut trong `main`: **khong nut nao con trang thai dang tai** (`ant-btn-loading`).
  3 nut "Luu nhap" / "Gui KQ" / "Trinh duyet" deu nha ra, bam tiep duoc.
- Truoc day: ca 3 nut **ket spinner vo han** (trung khop frame 00:49 video doi tac) -> **DA HET**.

**Y 3 - co nut Thu lai: KHONG DAT.**
- Sau cu bam, quet toan trang: **khong co nut/lien ket nao co chu "Thu lai"**. Thong bao loi chi la 1 dong chu
  trong toast, khong kem thao tac nao.
- Toast **tu tat sau khoang 3 giay** (do lai sau 6s: khong con toast nao tren man) -> can bo nhin di cho khac
  vai giay la mat han dau vet, khong con gi nhac la vua luu hong.
- Mau BA dan (srs-fr-05-vu-viec.md:1574): *"Luu that bai. Vui long kiem tra ket noi va thu lai." + nut [Thu lai]*
  - phan mem chua co ve nut/thao tac thu lai nay.

**Diem giam nhe (ghi cho dev):** du lieu **khong mat**. Sau khi bao loi, 3 o Nhan xet + 2 radio ket luan van con
nguyen tren bieu mau; bat mang lai roi bam "Luu nhap" thi luu duoc ngay ("Da luu ket qua tham dinh"). Tuc chi
thieu duong dan thu lai ngay tai cho bao loi, khong phai mat trang du lieu.

Ket luan: dat 2/3 tieu chi BA chot (thong bao loi + dung spinner), thieu 1 tieu chi (cach thu lai ngay tai thong
bao loi) -> **Reopen (fix mot phan)**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-TDHSTVV_09-offline-bao-loi-khong-co-nut-thu-lai.png`
  (toast "Khong ket noi duoc may chu." da ghim lai + 3 nut Luu nhap/Gui KQ/Trinh duyet khong con quay vong +
  khong co nut Thu lai nao tren man)
