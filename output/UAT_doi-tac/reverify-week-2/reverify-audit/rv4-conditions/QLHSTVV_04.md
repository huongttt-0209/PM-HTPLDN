# Bang doi chieu dieu kien - QLHSTVV_04 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 59, duyet 15/07/2026 - chuyen Dev FE):
- Giu bo loc khi bam "Quay lai danh sach" tu man chi tiet. Pham vi giu: **the trang thai + tu khoa +
  bo loc nang cao + so trang**.
- SRS chi quy dinh nut Quay lai ve mat dieu huong, khong noi nao yeu cau ghi nho bo loc
  (srs-fr-04:1540, :1452-1459) -> khoang trong SRS, BA quyet bo sung.
- BA nang thanh quy uoc chung: ap moi man danh sach (TVV, To chuc tu van, Nguoi ho tro, Vu viec).
- Verify lai: loc danh sach -> mo chi tiet -> Quay lai -> bo loc, tu khoa va so trang giu nguyen.

Case goc (sheet row 59): KQ mong doi = "He thong chuyen ve man hinh Danh sach tu van vien, giu nguyen cac
bo loc dang ap dung truoc do." KQ thuc te doi tac = "He thong chuyen ve man hinh Danh sach tu van vien
nhung khong giu nguyen cac bo loc dang ap dung truoc do."

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo nghiep vu xem danh sach TVV | `cbnv_tw` "CB Nghiep vu - Trung uong" (BTP · TW) - vai tro co quyen xem toan bo danh sach TVV | Khong |
| Man hinh | Danh sach Tu van vien | `/chuyen-gia-tvv/danh-sach` (Mang luoi Tu van vien > Tu van vien / Chuyen gia) | Khong |
| The trang thai | Phai giu the trang thai dang chon | Chon the **"Cho kich hoat tai khoan"** (KHONG phai the mac dinh "Dang hoat dong") de doi chieu that | Khong |
| Tu khoa | Phai giu tu khoa dang nhap | Nhap tu khoa **"PheDuyet"** vao o "Nhap tu khoa tim kiem..." | Khong |
| Bo loc nang cao | Phai giu bo loc nang cao | Mo "Bo loc nang cao (2)" -> **Ngay cong nhan tu 12/07/2026 den 13/07/2026** | Khong |
| So trang | Phai giu so trang | Da chay het muc du lieu cho phep - xem muc "Gioi han du lieu" duoi | Khong |
| Thao tac | Loc -> mo chi tiet -> bam "Quay lai danh sach" | Da chay du: bam Tim kiem -> mo chi tiet TVV-BTP-TW-0008 -> bam nut "Quay lai danh sach" tren man chi tiet | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Truoc khi mo chi tiet** (da bam Tim kiem, bo loc da an vao danh sach):
- The trang thai = "Cho kich hoat tai khoan"; tu khoa = "PheDuyet"; ngay cong nhan tu 12/07/2026 den 13/07/2026.
- Danh sach loc dung: **1-2 / 2 muc** = TVV-BTP-TW-0008 (PheDuyet W2 C) + TVV-BTP-TW-0006 (PheDuyet W2 A).
  Ban ghi TVV-BTP-TW-0013 (ngay cong nhan 15/07) va TVV-BTP-TW-0005 (khong khop tu khoa) da bi loai dung.

**Mo chi tiet:** bam "Xem" tren TVV-BTP-TW-0008 -> mo man chi tiet, breadcrumb `Trang chu / Mang luoi Tu van vien / Chi tiet`,
co nut **"Quay lai danh sach"**.

**Sau khi bam "Quay lai danh sach":** DAT day du.
- The trang thai van la **"Cho kich hoat tai khoan"** ✅ (khong nhay ve the mac dinh "Dang hoat dong")
- O tu khoa van la **"PheDuyet"** ✅
- Bo loc nang cao van la **12/07/2026 - 13/07/2026** ✅
- Danh sach van la **1-2 / 2 muc**, dung 2 ban ghi cu ✅
- => Loi goc doi tac bao ("khong giu nguyen cac bo loc dang ap dung truoc do") **DA HET**.

**So trang - da chay den muc du lieu cho phep:**
- Sau khi Quay lai, duong dan giu nguyen `page=1` cung voi cac bo loc.
- Da kiem rieng rang phan mem **co doc so trang tu duong dan** khi vao man danh sach: mo
  `?trangThai=TU_CHOI&page=2&pageSize=10` -> danh sach hien **0 dong** (dung, vi trang thai Tu choi chi co 6 ban ghi
  nen trang 2 rong) thay vi mac ke nhay ve trang 1. Tuc so trang di theo duong dan y het cac bo loc da xac nhan o tren.
- **Gioi han du lieu:** khong the dua danh sach sang trang 2 that. Trang thai nhieu ban ghi nhat chi co **6 TVV**
  (the "Tu choi"), trong khi o chon so ban ghi moi trang chi cho **10 / 20 / 50 / 100** (da thu go 5 -> khong nhan).
  Muon co trang 2 phai them it nhat 5-7 ho so TVV moi (form 11 truong bat buoc/ho so) -> se do rac vao moi truong
  doi tac. Khong lam. Ghi nhan gioi han thay vi ket luan bua.

**Quan sat phu, NGOAI pham vi case (khong dung de ra verdict):** o "so ban ghi moi trang" khong tu phuc hoi.
Doi 20 -> **10 / trang** roi mo chi tiet roi Quay lai: duong dan van giu `pageSize=10` nhung o chon hien lai
**"20 / trang"**. Day khong phai bo loc, khong phai so trang, khong nam trong KQ mong doi cua case va cung khong
phai loi moi do ban fix nay de ra (truoc fix thi khong giu gi ca) -> khong tinh Reopen. Chi ghi lai de dev/BA
biet: neu can bo dang o 10/trang trang 2 roi quay lai, danh sach co the ve trang trong. Nen dev kiem them.

Ket luan: dung KQ mong doi cua case (ve dung man danh sach + giu nguyen bo loc dang ap dung), va giu du ca 3
chieu BA liet ke kiem duoc (the trang thai, tu khoa, bo loc nang cao); chieu so trang di theo duong dan giong
het cac chieu con lai -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-QLHSTVV_04-truoc-khi-mo-chi-tiet.png` (truoc: the "Cho kich hoat tai khoan" + tu khoa PheDuyet + 12/07-13/07 + 2 muc)
- `../../bug-reports/ba-approved-batch/image/rv4-QLHSTVV_04-sau-khi-quay-lai-giu-nguyen.png` (sau khi Quay lai: y nguyen ca 3 chieu + van 2 muc)
- `../../bug-reports/ba-approved-batch/image/rv4-QLHSTVV_04-app-doc-so-trang-tu-duong-dan.png` (bang chung phan mem doc so trang tu duong dan: page=2 -> danh sach rong)
