# Bang doi chieu dieu kien - PDHSTVV_06 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 74):
- ❌ Y CHINH: **KHONG phai loi** - sau phe duyet, ho so chuyen "Cho kich hoat tai khoan" la DUNG co che
  (he thong tu tao tai khoan + gui mail kich hoat; TVV kich hoat xong moi sang "Dang hoat dong").
  Dac ta xu ly da ghi dung (srs-fr-04:591, :619-620). SRS tu mau thuan o 2 dong mo ta man hinh
  (:1545, :1582) con ghi "Dang hoat dong" - **BA sua SRS**, khong phai viec Dev.
- ✅ **Kem 2 dieu chinh nho CHUYEN DEV** (day la phan can re-verify):
  1. **Bo sung MA SO TVV vao noi dung mail kich hoat.**
  2. **Doi cau chu thong bao thanh "Da cong nhan tu van vien"** cho khop tai lieu ban giao.
  - Chi gui chu ho so - PDHSTVV_08 da chot khong them nguoi nhan.

Case goc (sheet row 74): KQ mong doi (phan lien quan 2 dieu chinh) = 'Gui thong bao den ... chu ho so voi noi dung
"Ho so cua ban da duoc cong nhan, ma so tu van vien: {ma}"' + 'Hien thi thong bao "Da cong nhan tu van vien"'.
KQ thuc te doi tac = "Khong gui thong bao den chu ho so" + "Thong bao hien thi khong giong voi thiet ke".

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo Phe duyet (thao tac phe duyet ho so TVV) | `cbpd_tw` "CB Phe duyet - Trung uong", badge **CB_PD_TW** hien tren header | Khong |
| Entity + trang thai | Ho so TVV o trang thai **"Cho phe duyet"** de bam duoc nut Phe duyet | Ho so **TVV-BTP-TW-0014 "QA TVV RV4 Tham Dinh Offline"**, trang thai **"Cho phe duyet"** - tu tao tien de (xem muc Seed duoi) | Khong |
| Thao tac | Bam **Phe duyet** -> quan sat (a) cau chu thong bao tren man, (b) mail gui cho chu ho so | Da chay ca 2 nhanh: bam Phe duyet that (dien So quyet dinh `QĐ-1607/QĐ-BTP`) + mo hop thu MailHog doc mail thuc te gui ra | Khong |
| Nguoi nhan mail | Chi gui **chu ho so** | Mail gui toi dung `qa.tvv.rv4.thamdinh@htpldn.test` = email cua chinh ho so TVV-BTP-TW-0014 | Khong |

Seed tien de: the "Cho phe duyet" chi co 1 ban ghi seed san co (giu nguyen, khong dung). Thay vao do dung ho so
TVV-BTP-TW-0014 do chinh minh tao o case TDHSTVV_09: `cbnv_tw` bam **Trinh duyet** tren tab Tham dinh
(ket luan DAT) -> hien hop xac nhan "Trinh phe duyet ho so tham dinh?" -> xac nhan -> toast
"Da trinh ho so len cap phe duyet", ho so chuyen **Dang tham dinh -> Cho phe duyet**. Sau do dang nhap `cbpd_tw`
o phien rieng (isolatedContext) de phe duyet.

Ket qua quan sat (UI + hop thu, khong dung API de ra verdict):

**Dieu chinh 1 - MA SO TVV trong mail kich hoat: KHONG DAT.**
- Sau khi phe duyet, he thong co gui mail toi dung chu ho so: tieu de **"Ho so TVV da duoc phe duyet - kich hoat tai khoan"**.
- Noi dung mail: *"Xin chao QA TVV RV4 Tham Dinh Offline, / Ho so tu van vien cua ban da duoc phe duyet va tai khoan
  dang nhap da duoc tao. / Link kich hoat: ... / Bam vao link de dat mat khau lan dau va dang nhap."*
- **Khong co ma so TVV**. Quet ca ban HTML lan ban Plain text/Source cua mail: khong co chuoi `TVV-BTP-TW-0014`,
  khong co bat ky ma dang `TVV-xxx-xx-nnnn` nao, cung khong co cum tu "ma so".
- KQ mong doi cua case: *"Ho so cua ban da duoc cong nhan, ma so tu van vien: {ma}"* -> chua co.

**Dieu chinh 2 - cau chu thong bao "Da cong nhan tu van vien": KHONG DAT.**
- Bam Phe duyet -> thong bao hien ra nguyen van la **"Phe duyet TVV thanh cong"** (bat bang MutationObserver cai
  truoc cu bam, da ghim lai de chup anh).
- BA chot doi thanh **"Da cong nhan tu van vien"** -> chua doi.

**Cac y khac (dung, khong phai loi - trung voi ket luan BA):** ho so chuyen sang **"Cho kich hoat tai khoan"** va
ghi nhan **Ngay cong nhan: 16/07/2026**; he thong tu tao tai khoan va gui mail kich hoat cho chu ho so. Dung co che
BA da xac nhan, khong tinh loi.

Ket luan: 2/2 dieu chinh BA chuyen Dev **deu chua duoc lam** -> **Reopen**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-PDHSTVV_06-thong-bao-phe-duyet.png`
  (vai tro CB_PD_TW + ho so TVV-BTP-TW-0014 + thong bao da ghim: "Phe duyet TVV thanh cong", khong phai
  "Da cong nhan tu van vien")
- `../../bug-reports/ba-approved-batch/image/rv4-PDHSTVV_06-mail-kich-hoat-khong-co-ma-tvv.png`
  (mail kich hoat gui dung chu ho so nhung toan bo noi dung khong co ma so TVV)
