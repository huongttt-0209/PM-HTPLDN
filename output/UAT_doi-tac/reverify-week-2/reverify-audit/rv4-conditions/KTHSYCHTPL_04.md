# Bang doi chieu dieu kien - KTHSYCHTPL_04 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 95, chot 16/07/2026): **LA LOI** - BA sua SRS roi chuyen Dev.
- Nhan "Deadline" vi pham quy uoc **UI-06 "tieng Viet la ngon ngu duy nhat", khong ngoai le** (srs-v3.5.md:573).
  Day la nhan tieng Anh duy nhat trong nhom (6 nhan con lai deu tieng Viet). **Doi thanh "Thoi han xu ly"**.
- DONG THOI sua SRS srs-fr-05:1637-1638 ("Deadline SLA" -> "Thoi han xu ly", "Canh bao SLA" -> "Canh bao thoi han")
  de ap thong nhat ca man danh sach lan man chi tiet - neu khong, BUG-QLTNVV_02 se keo Dev ve huong nguoc lai
  lam 2 man lech nhau.
- Verdict doi tu "BA confirm" sang Open.
- **Verify lai: man chi tiet vu viec hien "Thoi han xu ly"; man danh sach dung cung nhan.**

Case goc (sheet row 95): KQ mong doi = "He thong hien thi cac truong thong tin giong voi thiet ke, chi doc /
Du lieu hien thi dung dinh dang va truong thong tin / ... dong nhat ngon ngu hien thi".
KQ thuc te doi tac = 'Ten truong thong tin "Thoi han xu ly" dang la ngon ngu tieng Anh'.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo nghiep vu xem chi tiet vu viec | `cbnv_tw` "CB Nghiep vu - Trung uong", badge CB_NV_TW | Khong |
| Man hinh 1 | **Man chi tiet vu viec** - noi doi tac bao nhan tieng Anh | `/vu-viec/23892656-eec5-4f33-9340-3689fdd1c986` (VV-STP-AG-20260712-003), muc "Noi dung Yeu cau" | Khong |
| Man hinh 2 | **Man danh sach** phai dung **cung nhan** (BA yeu cau ap thong nhat 2 man) | `/vu-viec/danh-sach` - da doi chieu tieu de cot cua bang | Khong |
| Thao tac | Doc nhan truong thoi han o ca 2 man; kiem con sot chu tieng Anh khong | Quet chu hien thi + quet ca thuoc tinh `title` / `aria-label` / `placeholder` / `alt` cua **toan bo** phan tu DOM, sau khi **mo het 12 muc thu gon** cua man chi tiet | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Man chi tiet vu viec: DAT.**
- Muc "Noi dung Yeu cau" hien nhan **"Thoi han xu ly"** kem gia tri `31/07/2026`.
- Quet toan man (sau khi mo het 12 muc thu gon): **khong con chuoi "Deadline"** o bat ky dau -
  khong trong chu hien thi, khong trong `title` / `aria-label` / `placeholder` / `alt`.
- => Loi goc doi tac bao ("ten truong dang la tieng Anh") **DA HET**.

**Man danh sach vu viec: DAT (dung cung nhan).**
- Tieu de cot cua bang: `Ma vu viec | Ten doanh nghiep | Linh vuc phap luat | Kenh tiep nhan | Trang thai |
  Nguoi xu ly / To chuc | Ngay tiep nhan | **Thoi han xu ly** | **Canh bao thoi han** | Hanh dong`.
- Ca 2 nhan deu da doi dung theo SRS BA sua: "Deadline SLA" -> **"Thoi han xu ly"**,
  "Canh bao SLA" -> **"Canh bao thoi han"**.
- Khong con chu "Deadline" tren man danh sach.
- => 2 man **thong nhat cung mot nhan**, dung y BA lo (tranh BUG-QLTNVV_02 keo nguoc lam 2 man lech nhau).

Ket luan: ca 2 man deu dung "Thoi han xu ly", khong con nhan tieng Anh -> dung KQ mong doi + dung quy uoc UI-06
-> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-KTHSYCHTPL_04-chi-tiet-thoi-han-xu-ly.png` (man chi tiet: "Thoi han xu ly 31/07/2026")
- `../../bug-reports/ba-approved-batch/image/rv4-KTHSYCHTPL_04-danh-sach-cung-nhan.png` (man danh sach: cot "Thoi han xu ly" + "Canh bao thoi han")
