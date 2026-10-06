# Bang doi chieu dieu kien - KTDGKQHT_08 (re-verify vong 6, 2026-07-16 - sau khi dev bao da fix)

Boi canh: vong truoc (RV5, 16/07) ket luan **Reopen - fix mot phan**: dat 3/5 y BA chot; **khong dat y 2**
(thieu nhan "Ket qua tam tinh"); **khong kiem duoc y 4** (nhap diem qua Excel - phan mem khong co duong nay).
Dev bao da fix -> chay lai y 2 + kiem cac y da dat xem co hong nguoc khong.

**Sheet KHONG co phan hoi moi cua dev** cho row 6 (cot "Trang thai dev fix 2" / "DEV phan hoi lan 2" deu
trong; cot P/Q van la "Reopen" tu vong truoc) -> khong biet dev sua cu the cai gi -> re-verify theo dung
cac y BA chot nhu vong truoc.

Can cu SRS (da mo file doc tan noi, khong trich tri nho):
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:534` - FR-III-05 **PRE-04**:
  *"**Nhap diem kiem tra:** khoa hoc o `DANG_DIEN_RA` **hoac** `DA_KET_THUC` `[BA chot 2026-07-16 - Phuong an A2]`"*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5759` - SM-KHOAHOC: *"Dong diem danh
  (FR-III-05 PRE-03). **Diem kiem tra VAN nhap/sua duoc** cho toi khi trinh duyet KQ (FR-III-05 PRE-04)"*
- Nhan "Ket qua tam tinh": BA chot 16/07 (`phan-tich-KTDGKQHT-03-08.md` Buoc 3 muc 5 - *"Them nhan 'Ket qua
  tam tinh' khi khoa chua ket thuc"*, can cu SCR-III-02 Tab 5 + BR-KQ-02).
- Luu y: ban SRS BA sua 16/07 nam o `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`,
  KHONG phai `input/srs-update-2026-5-5/` (ban cu).

| Điều kiện | Bug gốc / yêu cầu BA (RV5) | Mình test (re-verify 2026-07-16 vòng 6) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu vao tab Ket qua cua khoa hoc (doi tac quay bang CB_NV_TW) | `cbnv_tw`, badge **CB_NV_TW** "CB Nghiep vu - Trung uong" (doc tren ảnh) | Không |
| Man hinh | Dao tao, tap huan -> Khoa hoc -> chi tiet -> tab **Ket qua** | Dung tab **Ket qua** cua man chi tiet khoa hoc | Không |
| Trang thai khoa (y 2) | Khoa **"Dang dien ra"** (chua ket thuc) - dung state doi tac quay va state y 2 yeu cau | Khoa **DDD-KH-011**, stepper **"Dang dien ra"** dang active (buoc 4) - **khoa khac voi vong truoc** (KH-20260716-002 da chuyen sang "Cho duyet KQ") nen day la lan xac nhan doc lap thu 2 | Không |
| Du lieu tien de | Khoa co hoc vien de bang Ket qua co dong du lieu | DDD-KH-011 co **1 hoc vien** "Nguyen Van Hoc Vien" - bang Ket qua render dong, o Diem kiem tra sua duoc | Không |
| Input (y 3 - kiem hong nguoc) | Nhap diem ngoai 0-10 (vd 15) -> phai tu choi + bao "Diem kiem tra phai tu 0 den 10" | Go **15** vao o Diem kiem tra roi bam **Luu ket qua** | Không |

## Ket qua quan sat (UI, khong dung API de ra verdict)

**Y 1 - khoa "Dang dien ra" mo duoc tab Ket qua + hien danh sach hoc vien: VAN DAT (khong hong nguoc).**
- Tab Ket qua mo binh thuong tren khoa DDD-KH-011 "Dang dien ra", hien du dong hoc vien kem cac cot
  (Chuyen can · Diem kiem tra · Ket qua · Xep loai · Ghi chu), o nhap diem sua duoc.
- Dung PRE-04 (`srs-fr-03-dao-tao.md:534`): nhap diem kiem tra duoc phep o `DANG_DIEN_RA`.

**Y 2 - nhan "Ket qua tam tinh" khi khoa chua ket thuc: VAN KHONG DAT (y het vong truoc).**
- Khoa **DDD-KH-011** dang **"Dang dien ra"** (chua ket thuc) nhung tab Ket qua **KHONG co chu "tam tinh"**
  o bat ky dau.
- Da quet **toan bo chu NHIN THAY duoc tren trang** (`innerText`, dung cach doc cua `tools/toast-capture.js` -
  khong dung `textContent` de tranh gom node an): `/tam tinh/i` -> **false**.
- Quet them **ca node AN trong DOM** (`textContent`) de chac chan khong phai loi an hien: `/tam tinh/i` ->
  **false** => nhan nay **khong ton tai**, khong phai bi an.
- Da thu ca cac bien the: "tam thoi", "chua chinh thuc", "du kien", "so bo" -> **deu khong co**.
- Moi cum chu co tu "Ket qua" tren trang: `Ket qua` (ten tab) · `Luu ket qua` (nut) · `Ket qua` (ten cot) ·
  `Ket qua` (bo loc) -> **khong cum nao kem "tam tinh"**.
- **Da tai lai trang hoan toan** (`reload`, `ignoreCache`) roi do lai lan 2 -> ket qua y het.
- => Trai y 2 BA chot (`phan-tich-KTDGKQHT-03-08.md` Buoc 3 muc 5).

**Y 3 - nhap >10 phai tu choi, khong tu keo ve 10: VAN DAT (khong hong nguoc).**
- Go **15** -> o **giu nguyen 15** (hien thi `15.0`), **khong** bi tu dong keo ve 10.
- Bam **Luu ket qua** -> bo bat thong bao (KHONG loc trung) ghi nhan **1 khung thong bao**, chu dung nguyen van
  **"Diem kiem tra phai tu 0 den 10"** (dung mo ta cua `ERR-KQ-01`).
- **So request ghi du lieu = 0** -> he thong chan ngay truoc khi gui di, **khong ghi gi xuong may chu**.
- Cot Ket qua / Xep loai van **"—"**; **tai lai trang hoan toan** -> o Diem kiem tra **rong** => xac nhan
  khong co gi bi ghi. Kich ban "go nham 15 thanh diem 10" da het.

**Y 4 - nhap diem qua Excel: VAN KHONG KIEM DUOC (giu nguyen ket luan vong truoc).**
- Khong do lai vong nay vi khong co thay doi ve pham vi. Vong truoc da ra soat ca 7 tab: nut "Import Excel"
  chi co o tab Hoc vien (import danh sach dang ky) va tab Diem danh (mau file ghi ro "Cot bat buoc:
  Ma hoc vien, Co mat (1/0)" - khong co cot diem). Tab Ket qua chi co [Luu ket qua] va [Xuat DOCX].
- **Khong ket luan day la loi** vi KQ mong doi cua case khong doi hoi duong Excel -> **de nghi BA xac nhan**:
  bo y 4, hoac neu that su can nhap diem tu Excel thi day la **chuc nang chua co**, can Dev bo sung (viec khac,
  khong phai loi cua case nay).

## Ngoai tieu chi BA - co thay gi bat thuong khong?

Doc lai 2 anh da chup vong nay: **khong phat hien them bat thuong nao** o tab Ket qua. Khong co toast lap
(1 thong bao / 0 request). Rieng mot diem **da co tu vong truoc, khong phai moi**: khoa "Da ket thuc" van sua
duoc tab **Diem danh** - da ghi o KTDGKQHT_03 (row 5), khong lap lai o day.

## Ket luan

Dat **3/5** y (y 1, 3, 5 giu nguyen thanh qua, khong hong nguoc), **van khong dat y 2** (thieu nhan "Ket qua
tam tinh" - do lai tren **khoa khac** va **tai lai trang** deu cho ket qua y het vong truoc), **y 4 van khong
kiem duoc** (can BA xac nhan). => **Reopen** (lan 2).

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv6-KTDGKQHT_08-thieu-nhan-ket-qua-tam-tinh.png`
  (da mo doc lai pixel: stepper **"Dang dien ra"** active buoc 4 · tab **Ket qua** dang mo · bang hien dong
  hoc vien · khu vuc dau tab chi co [Luu ket qua] [Xuat DOCX] + o tim kiem + bo loc - **khong co chu
  "tam tinh"** o bat ky dau)
- `../../bug-reports/ba-approved-batch/image/rv6-KTDGKQHT_08-diem-15-giu-nguyen-khong-keo-ve-10.png`
  (o Diem kiem tra giu **15.0** sau khi bam Luu, cot Ket qua/Xep loai van "—" -> khong keo ve 10, khong ghi gi.
  **Ten file da doi cho dung voi anh**: anh KHONG bat duoc khung thong bao vi toast tu tat ~3s, moi lan chup
  qua MCP deu tre; chu thong bao lay bang bo bat thong bao MutationObserver - dung phuong phap ma
  QA_VERIFY_PROTOCOL §GATE cho phep cho UI ephemeral)
