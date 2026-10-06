# Bang doi chieu dieu kien - QLGVTG_05 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 20, duyet bo sung 15/07/2026): bo sung kiem tra dinh dang SDT giang vien,
VAN de khong bat buoc. Chuan: bat dau bang 0, 10 chu so (di dong) hoac 11 chu so (co dinh) -> ^0\d{9,10}$.
BA canh bao ro: KHONG bat "dung 10 so" vi so co dinh 11 so se bi loai nham.
Verify lai: nhap SDT sai (khong bat dau bang 0 / sai do dai) -> bao loi; de trong -> van luu duoc.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu (quan ly giang vien) | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Khong |
| Man hinh | Dao tao, tap huan -> Giang vien / Tro giang -> Them moi | `/dao-tao/giang-vien/tao-moi`, form "Them giang vien moi" | Khong |
| Truong SDT bat buoc? | Phai VAN de khong bat buoc | Nhan "Dien thoai" KHONG co dau `*` -> khong bat buoc | Khong |
| Input / gia tri nhap | 5 nhanh: khong bat dau 0 / qua ngan / de trong / 10 so / 11 so | Da chay du 5 nhanh, moi lan set gia tri bang native setter + dispatch input (fill_form cua MCP NOI THEM chu khong thay the -> phai xoa sach truoc) | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

1. **`1234567890`** (10 so, khong bat dau bang 0) — ky vong bao loi, khong tao.
   Thuc te: toast **"So dien thoai khong hop le (bat dau bang 0, 10 chu so di dong hoac 11 chu so co dinh)"**,
   khong co request POST nao gui di, van o lai form. ✅ DAT
2. **`01234`** (bat dau bang 0 nhung qua ngan) — ky vong bao loi, khong tao.
   Thuc te: cung toast tren, khong tao, van o `/dao-tao/giang-vien/tao-moi`. ✅ DAT
3. **(de trong)** — ky vong VAN luu duoc (truong khong bat buoc).
   Thuc te: toast **"Tao giang vien thanh cong"**, chuyen ve danh sach, ban ghi `QA RV4 GV SDT Trong` xuat hien. ✅ DAT
4. **`0912345678`** (10 so di dong hop le) — ky vong luu duoc.
   Thuc te: toast "Tao giang vien thanh cong", ban ghi `QA RV4 GV SDT DiDong10` xuat hien. ✅ DAT
5. **`02412345678`** (11 so co dinh hop le) — ky vong luu duoc, KHONG bi loai nham.
   Thuc te: toast "Tao giang vien thanh cong", ban ghi `QA RV4 GV SDT CoDinh11` xuat hien. ✅ DAT

=> Dev implement dung `^0\d{9,10}$`: chan ca nhanh "khong bat dau bang 0" lan "sai do dai", chap nhan
ca 10 so di dong lan 11 so co dinh (dung canh bao cua BA), va giu truong khong bat buoc (de trong luu duoc).

Ket luan: 0 GAP. Dev da lam dung yeu cau BA -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_05-sdt-sai-bao-loi.png` (form con SDT `1234567890` + toast loi da ghim lai)
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_05-sdt-hople-va-trong-luu-duoc.png` (danh sach co du 3 ban ghi seed: trong / 10 so / 11 so)
