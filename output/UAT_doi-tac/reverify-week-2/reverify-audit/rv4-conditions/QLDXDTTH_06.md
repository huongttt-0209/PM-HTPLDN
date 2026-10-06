# Bang doi chieu dieu kien - QLDXDTTH_06 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 29): LA LOI - chuyen Dev FE. Xoa de xuat thanh cong phai co thong bao.
Can cu: quy uoc UI-04 "thao tac thanh cong phai co thong bao" (srs-v3.5.md:571). Luong tao de xuat da co
thong bao, luong xoa thi khong. Verdict doi tu "BA confirm" sang Open.
Verify lai: **DN** xoa 1 de xuat -> hien thong bao xoa thanh cong + danh sach cap nhat.

Case goc (sheet row 29): Mo ta = "Xoa de xuat o trang thai 'Moi' va do chinh **Doanh nghiep hoac Nguoi ho tro**
dang dang nhap da tao". KQ mong doi = "He thong hien thi hop xac nhan. He thong xoa mem de xuat va hien thi
thong bao 'Da xoa de xuat'." KQ thuc te doi tac = "He thong khong hien thi thong bao xoa thanh cong".

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Case neu **DN hoac NHT**; dong verify cua BA neu dich danh **DN** | Test CA HAI: `0109998887` "QA UAT Kiem Thu DN" (vai tro DN) va `nht_qa_tw` "QA NHT Trung uong" (vai tro NHT) | Khong |
| Chu so huu ban ghi | De xuat do **chinh nguoi dang dang nhap tao** | Moi vai tro tu tao de xuat rieng qua nut "Gui de xuat moi" ngay truoc khi test xoa | Khong |
| Trang thai de xuat | Trang thai **"Moi"** | Ca 2 de xuat vua tao deu o trang thai **"Moi gui"** (trang thai khoi tao cua de xuat; tab loc chi co Moi gui / Da tiep nhan / Dang xu ly / Da xu ly / Tu choi - khong co "Du thao") | Khong |
| Thao tac | Bam nut "Xoa" -> quan sat hop xac nhan + thong bao + danh sach | Da chay voi NHT; voi DN thi KHONG bam duoc vi khong co nut Xoa | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Nhanh NHT (chu so huu la NHT):** DAT day du.
- Tao de xuat "QA RV4 - de xuat DO CHINH NHT tao - kiem thu nut Xoa (QLDXDTTH_06) 16/07", linh vuc Thue,
  trang thai **Moi gui** -> cot Hanh dong hien **3 nut: [Tiep nhan] [Sua] [Xoa]**.
- Bam **[Xoa]** -> hien hop thoai **"Xoa de xuat? Hanh dong nay khong the hoan tac."** + [Huy] [Xoa]. ✅ co hop xac nhan
- Xac nhan -> toast **"Da xoa de xuat"** (dung NGUYEN VAN chuoi trong KQ mong doi cua case goc). ✅ CO thong bao
- Ban ghi bien mat khoi danh sach (con 5 dong). ✅ danh sach cap nhat
- => Loi goc doi tac bao ("khong hien thi thong bao xoa thanh cong") **DA HET**.

**Nhanh DN (chu so huu la DN) - vai tro BA neu DICH DANH trong dong verify:** **KHONG DAT**.
- Tao de xuat "QA RV4 - de xuat dao tao tao moi de kiem thu chuc nang XOA (QLDXDTTH_06) - 16/07/2026"
  bang tai khoan DN, trang thai **Moi gui**, do CHINH DN nay tao.
- Cot Hanh dong chi co **2 nut: [Tiep nhan] [Sua]** -> **KHONG co nut [Xoa]**.
- Kiem them man chi tiet de xuat: chi co [Quay lai danh sach] [Chinh sua] [Tiep nhan] -> khong co Xoa.
- Kiem them form "Cap nhat de xuat dao tao": chi co [Huy] [Luu] -> khong co Xoa.
- => DN **khong xoa duoc de xuat cua chinh minh** o trang thai Moi, trai voi Mo ta cua case
  ("do chinh Doanh nghiep ... da tao") va khong thuc hien duoc dong verify BA ghi ("DN xoa 1 de xuat").

**Bat nhat dang chu y (lien quan BUG-QLDXDTTH_03):** cung mot de xuat, cung trang thai Moi gui, cung la
chu so huu — DN co nut **[Tiep nhan]** (thao tac cua CAN BO, khong thuoc DN) nhung KHONG co nut **[Xoa]**
(thao tac cua chinh DN). Bo nut cua vai tro DN dang bi gan NGUOC.

Ket luan: thong bao xoa DA duoc fix (chung minh bang nhanh NHT), nhung vai tro DN — vai tro BA neu dich danh —
khong co nut Xoa nen khong thuc hien duoc thao tac cua case -> **Reopen** (fix mot phan).

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-QLDXDTTH_06-toast-da-xoa-de-xuat.png` (NHT: toast "Da xoa de xuat" da ghim lai + ban ghi da bien mat)
- `../../bug-reports/ba-approved-batch/image/rv4-QLDXDTTH_06-dn-khong-co-nut-xoa.png` (DN: de xuat cua chinh minh trang thai Moi gui chi co [Tiep nhan] [Sua])
