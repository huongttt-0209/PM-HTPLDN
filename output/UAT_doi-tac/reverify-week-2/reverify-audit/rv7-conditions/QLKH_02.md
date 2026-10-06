# Bang doi chieu dieu kien - QLKH_02 (verify lan DAU sau khi dev bao fix, 2026-07-17 vong 7)

Boi canh: dong TC do **chinh QA mo them** o vong rv5 (dong 113). Bug goc **BUG-FE-TOAST-LAP**: bam [Them moi]
**mot lan** de tao khoa hoc -> hien **2 khung thong bao "Tao khoa hoc thanh cong" giong het nhau** xep chong,
trong khi chi gui may chu 1 lan va chi tao 1 ban ghi. Tai hien 3/3 lan tren build CU. Cot `Verify` **con TRONG**
(chua verify lan nao) - dev da danh dau `dev done`.

Can cu: quy uoc **UI-04** (`srs-v3.5.md:571`) - mot thao tac thanh cong thi hien **mot** thong bao.

| Điều kiện | Bug gốc (rv5) | Mình test (verify 2026-07-17 vòng 7) | GAP? |
|---|---|---|:-:|
| Vai tro | `cbnv_tw` (CB_NV_TW) tao khoa hoc | `cbnv_tw`, badge **CB_NV_TW** - dung vai tro bug goc | Không |
| Man hinh | Dao tao, tap huan -> Khoa hoc -> **[Them moi]** -> dien truong bat buoc -> bam **[Them moi]** | Dung man tao khoa hoc `/dao-tao/khoa-hoc/tao-moi`, dien du truong bat buoc | Không |
| Thao tac | Bam nut **[Them moi] MOT lan duy nhat** (bam nut that, khong dung phim Enter) | Bam **dung 1 lan** bang cong cu dieu khien chuot that | Không |
| Phep do | Dem **so khung thong bao** + **so lan goi may chu** + **so ban ghi tao ra** | Bo bat thong bao `tools/toast-capture.js` (KHONG loc trung, doc bang `innerText`) + doi chieu nhat ky mang that + dem ban ghi truoc/sau. **Da TU KIEM `soObserverDangSong = 1` truoc moi lan do** | Không |

## Ket qua quan sat (UI, khong dung API de ra verdict)

**DA FIX THAT.** Moi thao tac thanh cong chi hien **dung 1 khung thong bao**.

Phep do sach - tai lai trang hoan toan, cai bo do **DUNG 1 LAN**, tu kiem `soObserverDangSong = 1` truoc moi lan do:

- **Tao lan 1** (ngay sau tai lai trang): 1 × `POST /api/v1/khoa-hocs` -> **1 khung thong bao**.
- **Tao lan 2** (**cung phien trang**, khong tai lai): 1 × `POST /api/v1/khoa-hocs` -> **1 khung thong bao**.
- **Xoa khoa hoc** (cung phien trang): 1 × `DELETE /api/v1/khoa-hocs/ea1b027e-...` -> **1 khung thong bao**.

Ban ghi tao ra: danh sach 10 -> 11 -> 12, tang **dung 1 ban ghi moi lan bam** - khong trung.

## CANH BAO - vong nay tuyt bao "Reopen" NHAM, nguyen nhan la LOI BO DO cua QA

Ban dau vong rv7 ket luan **Reopen** kem "quy luat tai hien 100%": *lan tao dau sau khi tai lai trang -> 1 thong bao;
tu lan thu 2 tro di trong cung phien trang -> 2 thong bao; thao tac xoa -> 3 thong bao*. **Ket luan do SAI.**

**Nguyen nhan:** file `tools/toast-capture.js` (ban truoc 2026-07-17) cai `MutationObserver` moi **ma khong ngat
observer cu**, trong khi callback tra `window.__qa` **tai thoi diem chay**. Nen moi observer cu con song deu day
vao mang `__qa` MOI => **cai N lan trong cung phien trang thi 1 toast THAT bi dem N lan**. Tai lai trang thi xoa
sach observer => dem lai ve 1.

**"Quy luat" tren thuc chat la bieu do SO LAN QA CAI BO DO**, khong phai hanh vi cua app:
- Cai 1 lan (ngay sau tai lai trang) -> dem 1 -> tuong "dat".
- Cai lan 2 -> dem 2 -> tuong "lap khi tao".
- Cai lan 3 -> dem 3 -> tuong "xoa con nang hon, lap 3 lan".
- Tai lai trang -> ve 1 -> tuong "reset khi tai lai trang".

**Con so 1 request / 2 toast (bat doi xung) - thu tung duoc dung lam bang chung "loi that" - cung do chinh loi nay:**
lan cai thu 2 QA dung ban observer rut gon (chi co MutationObserver, **khong** bọc lai fetch/XHR). Nen observer thanh
2 (toast dem doi) nhung bo dem request van chi 1 (request dem don). => 1 request + 2 toast.

**Cac dau hieu da bo lo (nay dua vao file bo do lam co do):**
1. `khoangCachMs = 0.7ms` - hai observer chay trong **cung mot lo mutation**. React render lap that thi cach nhau
   nhieu mili-giay.
2. **Anh chup khong bao gio bat duoc toast thu 2** qua nhieu lan thu -> vi tren man hinh **chua tung co** toast thu 2.
   QA da do cho "toast tu tat ~3s, MCP tre hon" thay vi nghi ngo chinh bo do.
3. So lan lap **tang dan theo thoi gian phien** va **reset khi tai lai trang** - dung dac trung cua trang thai tich
   luy **phia bo do**, khong phai phia app.

**Da sua goc:** `tools/toast-capture.js` nay bat buoc idempotent (ngat observer cu, khoi phuc fetch/XHR goc) va
kem doan **TU KIEM `soObserverDangSong`** - phai = 1 thi so lieu moi hop le.

## Ngoai tieu chi - co thay gi bat thuong khong? KHONG

Thao tac **xoa khoa hoc** do lai bang bo do sach: **1 DELETE -> 1 thong bao**. Ghi nhan "xoa hien 3 thong bao" o
vong rv7 ban dau (va da chep sang QLKH_01) **la sai, do cung loi bo do tren** - da go bo.

## Ket luan

Bug **BUG-FE-TOAST-LAP da fix that** - moi thao tac thanh cong chi hien 1 thong bao, doi chieu 3 phep do sach
(tao lan 1, tao lan 2 cung phien, xoa) deu **1 request -> 1 thong bao**. => **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv7-QLKH_02-danh-sach-17-khoa-moi-lan-tao-1-ban-ghi.png`
  (da mo doc lai pixel: moi lan bam tao ra **dung 1 ban ghi**, khong trung -> du lieu khong bi anh huong)
- **So khung thong bao khong co anh chung minh** (toast tu tat ~3s, vong goi qua MCP tre hon cua so do).
  Con so lay bang bo bat thong bao **da tu kiem `soObserverDangSong = 1`** truoc moi lan do, lap lai 3 phep do
  doc lap deu ra 1 request -> 1 thong bao. **Khong dan anh nao lam bang chung "chi 1 toast" vi chua chup duoc.**
- Anh `rv5-BUG-FE-TOAST-LAP-2-thong-bao.png` (2 khung thong bao) la bang chung THAT nhung **cua build CU truoc khi
  fix** - **KHONG duoc dung** de chung minh loi con o build hien tai.
