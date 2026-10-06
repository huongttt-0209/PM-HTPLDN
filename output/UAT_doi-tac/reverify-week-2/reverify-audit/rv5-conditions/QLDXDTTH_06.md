# Bang doi chieu dieu kien - QLDXDTTH_06 (re-verify VONG 2 sau dev fix, 2026-07-16 chieu)

Boi canh: vong re-verify truoc (rv4, sang 16/07) minh cham **Reopen (fix mot phan)**: thong bao xoa da co
(chung minh bang nhanh NHT) nhung **vai tro DN khong co nut [Xoa]** nen khong thuc hien duoc thao tac cua case.
Dev bao da fix -> chay lai vong nay o dung vai tro DN.

Yeu cau BA (note sheet row 29): LA LOI - chuyen Dev FE. Xoa de xuat thanh cong phai co thong bao.
Can cu: quy uoc UI-04 "thao tac thanh cong phai co thong bao" (srs-v3.5.md:571).
Verify lai: **DN** xoa 1 de xuat -> hien thong bao xoa thanh cong + danh sach cap nhat.

Case goc (sheet row 29): Mo ta = "Xoa de xuat o trang thai 'Moi' va do chinh **Doanh nghiep hoac Nguoi ho tro**
dang dang nhap da tao". KQ mong doi = "He thong hien thi hop xac nhan. He thong xoa mem de xuat va hien thi
thong bao 'Da xoa de xuat'."

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify vòng 2, 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Case neu **DN hoac NHT**; dong verify cua BA neu **dich danh DN**. Vong truoc DN la ve chua dat | `0109998887` / "QA UAT Kiem Thu DN", vai tro **DN** hien o header - dung ve con thieu cua vong truoc | Khong |
| Chu so huu ban ghi | De xuat do **chinh nguoi dang dang nhap tao** | De xuat "QA RV4 - de xuat dao tao tao moi de kiem thu chuc nang XOA (QLDXDTTH_06) - 16/07/2026" do chinh tai khoan DN nay tao o vong truoc | Khong |
| Trang thai de xuat | Trang thai **"Moi"** | Ban ghi dang o trang thai **"Moi gui"** (trang thai khoi tao cua de xuat) | Khong |
| Thao tac | Bam "Xoa" -> quan sat hop xac nhan + thong bao + danh sach | Da bam that; thong bao bat bang MutationObserver cai truoc cu bam (toast tu tat sau ~3s) va ghim lai de chup anh | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Nut [Xoa] o vai tro DN: DA CO - DA FIX.**
- Cot Hanh dong cua de xuat Moi gui do chinh DN tao nay hien **[Sua] [Xoa]** (vong truoc chi co [Tiep nhan] [Sua],
  khong he co [Xoa]).
- Man chi tiet cua ban ghi cung co nut **[Xoa]**.

**Luong xoa - DAT day du 3 y cua KQ mong doi:**
1. Bam **[Xoa]** -> hien hop thoai **"Xoa de xuat? / Hanh dong nay khong the hoan tac."** + [Huy] [Xoa].
   ✅ co hop xac nhan.
2. Xac nhan -> hien thong bao **"Da xoa de xuat"** - **dung NGUYEN VAN** chuoi trong KQ mong doi cua case goc.
   ✅ co thong bao.
3. Danh sach cap nhat ngay: **2 ban ghi -> con 1**, ban ghi vua xoa bien mat hoan toan khoi danh sach.
   ✅ danh sach cap nhat.

- => Luong xoa cua vai tro **DN** gio giong het luong cua **NHT** (vong truoc da dat) -> ve con thieu cua vong
  truoc **DA DUOC FIX**.

Ket luan: dung vai tro BA dich danh (DN), dung trang thai (Moi gui), dung chu so huu, va dat ca 3 y cua
KQ mong doi -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv5-QLDXDTTH_06-dn-xoa-duoc-toast-da-xoa.png`
  (vai tro DN: thong bao "Da xoa de xuat" da ghim lai + ban ghi da bien mat, danh sach con 1)
