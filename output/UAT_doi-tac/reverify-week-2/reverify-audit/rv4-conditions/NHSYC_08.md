# Bang doi chieu dieu kien - NHSYC_08 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 92, duyet 16/07/2026 - chuyen Dev FE):
- Bo sung **hop thoai xac nhan khi roi form con du lieu chua luu**. Hien bam "Huy" la ve danh sach ngay,
  khong hoi gi, du lieu form 4 nhom mat luon.
- Can cu: SRS im lang o module Vu viec (:1695), nhung hai module cung san pham dang hanh xu KHAC NHAU o cung
  mot thao tac - module Tu van vien DA CO hop thoai xac nhan ("O lai"), module Vu viec thi chua.
- BA chuan hoa thanh QUY UOC CHUNG trong SRS (canh UI-04), ap moi module.
- **Verify lai: nhap do form -> bam Huy -> hien hop thoai xac nhan, chon o lai thi giu nguyen du lieu.**

Case goc (sheet row 92): KQ mong doi = 'He thong hien thi xac nhan "Ban co chac chan muon huy? Du lieu da nhap
se khong duoc luu". Neu nguoi dung dong y, he thong chuyen trang; neu khong, giu nguyen man hinh.'
KQ thuc te doi tac = "He thong khong hien thi xac nhan".

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo nghiep vu nhap thu cong vu viec | `cbnv_tw` "CB Nghiep vu - Trung uong", badge CB_NV_TW | Khong |
| Man hinh | Form **Nhap thu cong** vu viec | `/vu-viec/tao-moi` - mo tu nut **[Nhap thu cong]** tren man Vu viec HTPL | Khong |
| Du lieu tien de | Form **con du lieu chua luu** (nhap do) | Da nhap 2 truong: Tieu de vu viec = "QA RV4 - vu viec nhap do de kiem thu nut Huy (NHSYC_08) 16/07", Noi dung yeu cau = "Noi dung nhap do - dung de kiem thu hop thoai xac nhan khi bam Huy." | Khong |
| Thao tac | Bam **[Huy]** -> quan sat hop thoai; roi thu **ca 2 nhanh** (o lai / dong y roi di) | Da chay ca 2 nhanh that + them 1 nhanh doi chieu (form TRONG) | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Nhanh 1 - bam Huy khi form con du lieu: DAT.**
- Hien hop thoai **"Xac nhan huy"** / *"Ban co chac chan muon huy? Du lieu da nhap se khong duoc luu."*
  + 2 nut **[Tiep tuc nhap]** / **[Hủy bỏ]**.
- Cau chu **trung khop nguyen van** voi KQ mong doi cua case goc.
- Truoc day: **khong hoi gi**, ve thang danh sach -> **loi goc DA HET**.

**Nhanh 2 - chon o lai ("Tiep tuc nhap"): DAT.**
- Hop thoai dong, van o lai `/vu-viec/tao-moi`.
- **Du lieu giu nguyen 100%**: Tieu de va Noi dung yeu cau van con nguyen van chuoi da nhap.
- Dung ve "neu khong [dong y], he thong giu nguyen man hinh".

**Nhanh 3 - chon dong y ("Hủy bỏ"): DAT.**
- Chuyen ve `/vu-viec/danh-sach` (man Vu viec HTPL). Dung ve "neu nguoi dung dong y, he thong chuyen trang".

**Nhanh doi chieu - form TRONG (chua nhap gi) bam Huy:** ve thang danh sach, **khong hoi**. Dung logic BA neu
("hop thoai xac nhan khi roi form **con du lieu chua luu**") - hop thoai khong bi bat mu quang moi lan bam Huy.

Ket luan: dung KQ mong doi ca 2 nhanh (hien xac nhan + o lai giu du lieu + dong y thi chuyen trang), va dung
pham vi BA neu (chi hoi khi con du lieu chua luu) -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-NHSYC_08-hop-thoai-xac-nhan-huy.png`
  (form Nhap thu cong da nhap do + hop thoai "Xac nhan huy" voi cau chu dung nguyen van + 2 nut
  [Tiep tuc nhap] / [Hủy bỏ])
