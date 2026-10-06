# Bang doi chieu dieu kien - QLDXDTTH_03 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 28, chot 15/07/2026): LA LOI - DN/NHT duoc xem de xuat dao tao cua minh, ca
danh sach lan chi tiet. Can cu: CSV baseline dong 287-288 tach "xem danh sach" va "xem chi tiet" thanh
2 thao tac rieng cua DN (SRS FR-III-13 ghi thieu so voi CSV). Cach lam: them DN/NHT vao lam nguoi xem cua
man chi tiet san co (SCR-III-01 Thanh phan 8) - **chi doc**, chi thay de xuat cua minh. Khong dung man moi.
Owner: BA sua SRS (srs-fr-03:1017, :1800) -> Dev FE.
Verify lai: DN mo de xuat cua minh -> hien man chi tiet chi doc; khong xem duoc de xuat cua DN khac.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | **Doanh nghiep (DN)** - dung vai tro BA noi den | `0109998887` / "QA UAT Kiem Thu DN", vai tro **DN** hien o header, thuoc DN-HNI-0001 (Ha Noi). Tai khoan da co san trong he thong (phien truoc tao), mat khau Test@1234 | Khong |
| Du lieu tien de | Can de xuat cua CHINH DN nay + de xuat cua DN KHAC de doi chieu pham vi | Co san 4 de xuat: 1 cua DN-HNI-0001 ("QA UAT verify - de xuat dao tao kiem thu chuc nang Xem chi tiet va Xoa (row28/29)", Ha Noi) + 3 cua DN An Giang | Khong |
| Thao tac | (a) DN mo danh sach de xuat -> dem so ban ghi thay duoc; (b) DN mo chi tiet de xuat cua minh -> kiem co CHI DOC khong | Da chay ca 2 nhanh + thu thuc thi nut thao tac de kiem quyen that o may chu | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Nhanh (a) - pham vi danh sach:** DAT.
- DN mo tab "De xuat dao tao" -> thay **dung 1 ban ghi** = de xuat cua chinh DN-HNI-0001.
- Doi chieu: `cbnv_tw` (CB Trung uong) thay **4 ban ghi**. 3 de xuat cua DN An Giang KHONG hien voi DN Ha Noi.
- => DN chi thay de xuat cua minh, khong xem duoc de xuat DN khac. ✅

**Nhanh (b) - man chi tiet co chi doc khong:** **KHONG DAT**.
- DN bam vao noi dung de xuat -> mo `/dao-tao/de-xuat/d3e209a9-12b9-4adf-8f7d-5adac62c6a91`,
  breadcrumb `Trang chu / Dao tao, tap huan / De xuat dao tao / Chi tiet`. Man chi tiet MO DUOC ✅.
- Cac truong du lieu hien dang chu tinh, **0 o nhap duoc** -> chi doc ve mat DU LIEU ✅.
- NHUNG man con hien **nut thao tac cua CAN BO**: **[Chinh sua]** va **[Tiep nhan]**. ❌
- Thu thuc thi that: DN bam **[Tiep nhan]** -> hien hop thoai "Tiep nhan de xuat? De xuat se chuyen sang
  trang thai Da tiep nhan" -> xac nhan -> toast **"Da tiep nhan de xuat"**, trang thai doi
  **"Moi gui" -> "Da tiep nhan"**. **May chu KHONG chan.**
- Sau do man hien tiep **[Bat dau xu ly]** va **[Tu choi]** -> DN co the tu tu choi de xuat cua chinh minh.
- => Man chi tiet o vai tro DN **KHONG chi doc** nhu BA chot. DN thuc hien duoc thao tac xu ly cua can bo.

Ket luan: 2/3 y dat, 1 y KHONG dat -> **Reopen** (fix mot phan + de ra loi moi cung luong).

Luu y trang thai du lieu: de xuat `d3e209a9-12b9-4adf-8f7d-5adac62c6a91` da bi doi tu "Moi gui" sang
"Da tiep nhan" trong luc verify (day chinh la bang chung loi). Neu dev can test lai tu trang thai goc
thi phai reset trang thai ban ghi nay.

Evidence: `../../bug-reports/ba-approved-batch/image/rv4-QLDXDTTH_03-dn-tu-tiep-nhan-de-xuat.png`
(header ghi ro "QA UAT Kiem Thu DN" + vai tro "DN"; trang thai "Da tiep nhan"; nut "Bat dau xu ly"/"Tu choi" dang hien)
