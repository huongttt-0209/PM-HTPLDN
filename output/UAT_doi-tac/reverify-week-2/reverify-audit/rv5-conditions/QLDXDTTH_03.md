# Bang doi chieu dieu kien - QLDXDTTH_03 (re-verify VONG 2 sau dev fix, 2026-07-16 chieu)

Boi canh: vong re-verify truoc (rv4, sang 16/07) minh cham **Reopen** vi man chi tiet o vai tro DN van hien
nut thao tac cua CAN BO va **may chu KHONG chan** (DN bam [Tiep nhan] tren chinh de xuat cua minh -> he thong
bao "Da tiep nhan de xuat", trang thai doi Moi gui -> Da tiep nhan). Dev bao da fix -> chay lai vong nay.

Yeu cau BA (note sheet row 28, chot 15/07/2026): LA LOI - DN/NHT duoc xem de xuat dao tao cua minh, ca danh sach
lan chi tiet. Cach lam: them DN/NHT vao lam nguoi xem cua man chi tiet san co (SCR-III-01 Thanh phan 8) -
**chi doc**, chi thay de xuat cua minh. Owner: BA sua SRS (srs-fr-03:1017, :1800) -> Dev FE.
Verify lai: DN mo de xuat cua minh -> hien man chi tiet chi doc; khong xem duoc de xuat cua DN khac.

Luu y doc kem: "chi doc" o day = **khong cho thao tac XU LY cua can bo**. Khong the hieu la cam ca [Sua]/[Xoa],
vi QLDXDTTH_06 (row 29) BA chot **DN phai xoa duoc** de xuat cua chinh minh khi con trang thai Moi. Hai quyet
dinh cua BA phai doc cung nhau.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify vòng 2, 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | **Doanh nghiep (DN)** - dung vai tro BA noi den | `0109998887` / "QA UAT Kiem Thu DN", vai tro **DN** hien o header, thuoc DN-HNI-0001 (Ha Noi) | Khong |
| Du lieu tien de | Can de xuat cua CHINH DN nay + de xuat cua DN KHAC de doi chieu pham vi | Co 2 de xuat cua DN-HNI-0001: 1 trang thai **Moi gui** + 1 trang thai **Da tiep nhan** (chinh la ban ghi `d3e209a9-...` bi loi o vong truoc). Ngoai he thong con 3 de xuat cua DN An Giang | Khong |
| Trang thai doi chieu | Bug goc xay ra o de xuat trang thai **Moi gui** (khi do DN co nut [Tiep nhan]) | Da kiem **CA HAI** trang thai: ban ghi Moi gui (`350bdf68-...`) va ban ghi Da tiep nhan (`d3e209a9-...`) | Khong |
| Thao tac | (a) DN mo danh sach -> dem ban ghi; (b) DN mo chi tiet de xuat cua minh -> kiem con nut thao tac can bo khong | Da chay ca 2 nhanh tren ca 2 trang thai | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Nhanh (a) - pham vi danh sach: DAT (giu nguyen ket qua tot cua vong truoc).**
- DN thay **dung 2 ban ghi**, ca 2 deu la de xuat cua chinh DN-HNI-0001.
- **Khong** co de xuat nao cua DN An Giang lot sang. ✅

**Nhanh (b) - man chi tiet co con nut thao tac cua can bo khong: DAT - DA FIX.**
- Cot Hanh dong tren **danh sach**: ban ghi Moi gui nay hien **[Sua] [Xoa]** - **KHONG con [Tiep nhan]**.
  Ban ghi Da tiep nhan hien **"—"** (khong nut nao).
- **Man chi tiet ban ghi Moi gui** (`350bdf68-...`): nut tren man chi con
  **[Quay lai danh sach] [Chinh sua] [Xoa]**. **KHONG con [Tiep nhan] / [Bat dau xu ly] / [Tu choi]**.
  So o nhap duoc = **0** -> du lieu chi doc.
- **Man chi tiet ban ghi Da tiep nhan** (`d3e209a9-...` - dung ban ghi minh dung lam bang chung loi vong truoc):
  nut tren man **chi con [Quay lai danh sach]**. So o nhap duoc = **0**.
- => Bo nut cua vai tro DN **khong con bi gan nguoc**: het nut xu ly cua can bo, giu dung 2 thao tac cua chinh
  DN voi de xuat cua minh khi con Moi ([Chinh sua] / [Xoa] - dung theo QLDXDTTH_06 BA chot).
- => Loi vong truoc (DN tu tiep nhan/tu choi duoc de xuat cua chinh minh) **DA HET tren giao dien**.

**Gioi han da noi ro, khong giau:** o vong truoc minh chung minh duoc **may chu khong chan** bang cach bam that
nut [Tiep nhan] roi doc ket qua. Vong nay nut da bi go khoi giao dien nen **khong con duong nao qua giao dien
de thu thuc thi lai thao tac do** - ma yeu cau cua user la **khong verify qua API**. Vi vay ket luan "may chu
da chan chua" nam ngoai pham vi kiem duoc bang giao dien o vong nay. Neu can chac chan ve chan phia may chu,
de nghi cho phep goi truc tiep API hoac de dev cung cap bang chung kiem thu phia may chu.

Ket luan: ca 2 nhanh BA neu deu dat tren giao dien (chi thay de xuat cua minh + man chi tiet khong con thao tac
xu ly cua can bo) -> **Pass**, kem ghi chu gioi han ve kiem quyen phia may chu o tren.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv5-QLDXDTTH_03-dn-chi-tiet-het-nut-can-bo.png`
  (vai tro DN, de xuat cua chinh minh trang thai Moi gui: man chi tiet chi con [Quay lai danh sach] [Chinh sua] [Xoa])
