# Bang doi chieu dieu kien - PDHSTVV_06 (re-verify VONG 2 sau dev fix, 2026-07-16 chieu)

Boi canh: vong re-verify truoc (rv4, sang 16/07) minh cham **Reopen - 0/2**: mail kich hoat khong co ma so TVV,
va thong bao van la "Phe duyet TVV thanh cong". Dev bao da fix -> chay lai vong nay.

Yeu cau BA (note sheet row 74) - phan chuyen Dev (2 dieu chinh nho):
1. **Bo sung MA SO TVV vao noi dung mail kich hoat.**
2. **Doi cau chu thong bao thanh "Da cong nhan tu van vien"** cho khop tai lieu ban giao.
- Chi gui chu ho so - PDHSTVV_08 da chot khong them nguoi nhan.
(Y chinh cua case - ho so chuyen "Cho kich hoat tai khoan" sau phe duyet - BA da chot **khong phai loi**.)

Case goc (sheet row 74) - KQ mong doi phan lien quan: 'Gui thong bao den ... chu ho so voi noi dung
"Ho so cua ban da duoc cong nhan, ma so tu van vien: {ma}"' + 'Hien thi thong bao "Da cong nhan tu van vien"'.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify vòng 2, 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo Phe duyet (thao tac phe duyet ho so TVV) | `cbpd_tw` "CB Phe duyet - Trung uong", badge **CB_PD_TW** | Khong |
| Entity + trang thai | Ho so TVV o trang thai **"Cho phe duyet"** | Ho so **TVV-BTP-TW-0015 "QA TVV RV5 Tham Dinh Offline 2"**, trang thai **"Cho phe duyet"** - tu tao lai tien de (ho so RV4 vong truoc da phe duyet roi, khong dung lai duoc) | Khong |
| Thao tac | Bam **Phe duyet** -> quan sat (a) cau chu thong bao tren man, (b) mail gui cho chu ho so | Da chay ca 2 nhanh: bam Phe duyet that (So quyet dinh `QĐ-1607b/QĐ-BTP`) + mo hop thu MailHog doc mail thuc te | Khong |
| Nguoi nhan mail | Chi gui **chu ho so** | Mail gui toi dung `qa.tvv.rv5.thamdinh@htpldn.test` = email cua chinh ho so TVV-BTP-TW-0015 | Khong |

Seed tien de: `cbnv_tw` tao ho so TVV moi -> Luu nhap (chuyen Dang tham dinh) -> **[Trinh duyet]** ->
"Da trinh ho so len cap phe duyet", ho so chuyen **Cho phe duyet**. Roi dang nhap `cbpd_tw` o phien rieng.

Ket qua quan sat (UI + hop thu, khong dung API de ra verdict):

**Dieu chinh 1 - MA SO TVV trong mail kich hoat: DAT - DA FIX.**
- Mail gui dung chu ho so, tieu de **"Ho so TVV da duoc phe duyet - kich hoat tai khoan"**.
- Noi dung mail nay co dong: **"Ho so cua ban da duoc cong nhan, ma so tu van vien: TVV-BTP-TW-0015."**
  -> **dung NGUYEN VAN** cau trong KQ mong doi cua case goc, va **ma so dung** ma cua ho so vua phe duyet.
- Vong truoc: mail chi co loi chao + cau bao da phe duyet + link kich hoat, **khong co ma so nao**.

**Dieu chinh 2 - cau chu thong bao "Da cong nhan tu van vien": DAT - DA FIX.**
- Bam Phe duyet -> thong bao hien ra nguyen van la **"Da cong nhan tu van vien"** (bat bang MutationObserver
  cai truoc cu bam, da ghim lai de chup anh).
- Vong truoc: "Phe duyet TVV thanh cong".

**Cac y khac (dung, khong phai loi - trung ket luan BA, giu nguyen so voi vong truoc):** ho so chuyen
**"Cho kich hoat tai khoan"** + ghi nhan **Ngay cong nhan 16/07/2026** + tu tao tai khoan va gui mail kich hoat
cho chu ho so.

Ket luan: **ca 2/2** dieu chinh BA chuyen Dev deu da lam dung -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv5-PDHSTVV_06-thong-bao-da-cong-nhan-tvv.png`
  (vai tro CB_PD_TW, ho so TVV-BTP-TW-0015: thong bao da ghim "Da cong nhan tu van vien")
- `../../bug-reports/ba-approved-batch/image/rv5-PDHSTVV_06-mail-co-ma-so-tvv.png`
  (mail kich hoat gui chu ho so, co dong "Ho so cua ban da duoc cong nhan, ma so tu van vien: TVV-BTP-TW-0015.")
