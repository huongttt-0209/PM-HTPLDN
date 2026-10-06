# Bang doi chieu dieu kien - TDHSTVV_09 (re-verify VONG 2 sau dev fix, 2026-07-16 chieu)

Boi canh: vong re-verify truoc (rv4, sang 16/07) minh cham **Reopen (fix mot phan, 2/3)**: da co thong bao loi
va spinner da dung, nhung **khong co cach thu lai ngay tai cho bao loi** va thong bao lai **tu tat sau ~3 giay**.
Dev bao da fix -> chay lai vong nay.

Yeu cau BA (note sheet row 65, duyet 15/07/2026 - chuyen Dev FE):
**Viec can lam: hien thong bao loi mat ket noi + DUNG spinner + co nut Thu lai.** Mau san co o module Vu viec:
"Luu that bai, vui long kiem tra ket noi va thu lai" (srs-fr-05:1567, :1574).
**Verify lai: ngat mang -> bam Luu nhap -> hien thong bao loi, spinner dung, co nut Thu lai.**

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify vòng 2, 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu Trung uong | `cbnv_tw` "CB Nghiep vu - Trung uong", badge CB_NV_TW, don vi BTP · TW | Khong |
| Man hinh | Tab "Tham dinh" cua ho so TVV, nut "Luu nhap" | Tab "Tham dinh" cua ho so TVV, nut "Luu nhap" (cung nut, cung man) | Khong |
| Trang thai ho so | **"Dang tham dinh"** (trang thai bug goc) | Ho so **TVV-BTP-TW-0015 "QA TVV RV5 Tham Dinh Offline 2"**, trang thai **"Dang tham dinh"** - tu tao lai tien de vi the "Dang tham dinh" lai rong (ho so RV4 vong truoc da di tiep sang Cho kich hoat) | Khong |
| Du lieu tien de | Bieu mau tham dinh da dien, Ket luan tham dinh = DAT | Da dien: Ket luan Phap ly = Dat, 3 o Nhan xet (Nhom 2/3/4) co noi dung, Ket luan tham dinh = **DAT** | Khong |
| Dieu kien mang | **Mat ket noi mang** roi bam "Luu nhap" | **Mat ket noi that**: bat che do Offline cua trinh duyet -> `navigator.onLine = false`, moi yeu cau ra may chu nem `TypeError: Failed to fetch` (da kiem chung trong cung phien) | Khong |
| Thao tac | Bam "Luu nhap" khi dang mat mang | Da bam that. Quan sat bang MutationObserver cai **truoc** cu bam. Sau do **bam chinh nut [Thu lai]** de kiem no co chay that khong | Khong |

Seed tien de: the "Dang tham dinh" rong -> tao 1 ho so TVV moi qua nut [Them moi] (11 truong bat buoc + file the
hanh nghe PDF) -> vao the "Moi dang ky" (TVV-BTP-TW-0015); bam [Luu nhap] lan dau **khi con mang** -> he thong bao
"Da luu ket qua tham dinh" va chuyen ho so **Moi dang ky -> Dang tham dinh**. Den day moi dung trang thai bug goc.

Ket qua quan sat (UI, khong dung API de ra verdict):

**Y 1 - hien thong bao loi mat ket noi: DAT (va tot hon vong truoc).**
- Bam "Luu nhap" khi offline -> hien thong bao **"Luu that bai" / "Luu that bai. Vui long kiem tra ket noi va
  thu lai."** - **DUNG NGUYEN VAN mau BA dan** o srs-fr-05-vu-viec.md:1574.
- Vong truoc chi la "Khong ket noi duoc may chu." (dung y nhung khac cau chu mau).

**Y 2 - dung spinner: DAT (giu nguyen ket qua tot cua vong truoc).**
- Sau cu bam, **khong nut nao** con trang thai dang tai (`ant-btn-loading`).

**Y 3 - co nut Thu lai: DAT - DA FIX (day la ve thieu cua vong truoc).**
- Thong bao hien **kem nut [Thu lai]** ngay trong khung bao loi.
- **Da doi kieu thong bao:** vong truoc dung toast (`ant-message`, tu tat ~3 giay); vong nay dung
  **notification** (`ant-notification-topRight`) - **do lai sau 11 giay: thong bao VAN CON tren man, nut [Thu lai]
  van con**. Dung y phan nan cua vong truoc ("can bo nhin di cho khac vai giay la mat han dau vet").
- **Kiem nut co chay that khong (khong chi co ve nut):** bat mang lai -> bam **chinh nut [Thu lai]** ->
  he thong bao **"Da luu ket qua tham dinh"**, khung bao loi **bien mat**, 3 o Nhan xet van con nguyen du lieu.
  => Nut Thu lai **thuc su thuc thi lai thao tac**, khong phai nut trang tri.

Ket luan: dat **ca 3/3** tieu chi BA chot (thong bao loi dung nguyen van mau + spinner dung + co nut Thu lai chay
that), va khac phuc dung diem minh neu o vong truoc (thong bao khong con tu tat) -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv5-TDHSTVV_09-bao-loi-co-nut-thu-lai.png`
  (mat mang bam Luu nhap: khung "Luu that bai. Vui long kiem tra ket noi va thu lai." + nut [Thu lai];
  3 nut Luu nhap/Gui KQ/Trinh duyet khong con quay vong)
