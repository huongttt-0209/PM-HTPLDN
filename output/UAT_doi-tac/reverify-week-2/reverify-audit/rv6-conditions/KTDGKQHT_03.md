# Bang doi chieu dieu kien - KTDGKQHT_03 (re-verify vong 6, 2026-07-16 - sau khi dev bao da fix)

Boi canh: vong truoc (RV5, 16/07) ket luan **Reopen - fix mot phan**: dat 3/4 y BA chot, khong dat y 4
(khoa "Da ket thuc" van sua va luu duoc diem danh). Dev bao da fix -> chay lai y 4 + kiem 3 y da dat
xem co bi hong nguoc (regression) khong.

**Sheet KHONG co phan hoi moi cua dev** cho row 5 (cot "Trang thai dev fix 2" / "DEV phan hoi lan 2"
deu trong; cot P/Q van la "Reopen" tu vong truoc). Nen khong biet dev sua cu the cai gi -> re-verify
theo dung 4 y BA chot nhu vong truoc.

Can cu SRS (da mo file doc tan noi, khong trich tri nho):
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:533` - FR-III-05 **PRE-03**:
  *"**Nhap diem danh:** khoa hoc o `DANG_DIEN_RA`. Khi khoa chuyen `DA_KET_THUC` thi **diem danh dong**
  (theo SM-KHOAHOC, tac dong 'Dong diem danh')"*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5759` - SM-KHOAHOC, buoc chuyen
  `DANG_DIEN_RA -> DA_KET_THUC`, cot Tac dong: *"**Dong diem danh** (FR-III-05 PRE-03)"*
- Luu y: ban SRS BA sua 16/07 nam o `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`,
  KHONG phai `input/srs-update-2026-5-5/` (ban cu, chua co sua doi cua BA).

| Điều kiện | Bug gốc / yêu cầu BA (RV5) | Mình test (re-verify 2026-07-16 vòng 6) | GAP? |
|---|---|---|:-:|
| Vai tro | Can bo nghiep vu vao tab Diem danh | `cbnv_tw`, badge **CB_NV_TW** "CB Nghiep vu - Trung uong" (doc tren ảnh) | Không |
| Man hinh | Dao tao, tap huan -> Khoa hoc -> chi tiet -> tab **Diem danh** | Dung tab **Diem danh** cua man chi tiet khoa hoc | Không |
| Trang thai khoa (y 4) | Khoa **"Da ket thuc"** | Khoa **KH-SEED-0001** (`5eed0002-...-0001`), stepper **"Da ket thuc"** dang active (buoc 5) - dung state bug goc | Không |
| Du lieu tien de | Khoa co buoi hoc + hoc vien da duyet | 2 buoi seed cung ngay 20/02/2026 (SANG 08:00-11:00 / CHIEU 14:00-17:00) + 1 hoc vien "QA Import Reverify12 OK" da duyet - **y nguyen tien de RV5** | Không |
| Thao tac | Chon buoi -> doi trang thai -> Luu -> tai lai kiem may chu co ghi that khong | Da chay that: doi "Co mat" -> "Vang khong phep" -> Luu -> **tai lai trang hoan toan** roi doc lai | Không |

## Ket qua quan sat (UI, khong dung API de ra verdict - API chi de doi chieu)

**Y 1 - dong nhac khi chua chon buoi: VAN DAT (khong hong nguoc).**
- Tab Diem danh khi chua chon buoi -> hien dung dong **"Vui long chon buoi hoc de bat dau diem danh"**.

**Y 2 - bo chon la danh sach BUOI HOC: VAN DAT (khong hong nguoc).**
- Bo chon placeholder **"Chon buoi hoc de diem danh"**; kiem `.ant-picker` = **khong ton tai** -> khong con o chon ngay.
- Xo ra dung 2 dong, moi dong du **Ngay · Khung gio · Noi dung**:
  `20/02/2026 · 08:00:00-11:00:00 · QA seed KTDGKQHT_03 - buoi SANG`
  `20/02/2026 · 14:00:00-17:00:00 · QA seed KTDGKQHT_03 - buoi CHIEU`

**Y 4 - khoa "Da ket thuc" thi tab Diem danh chi doc: VAN KHONG DAT (y het vong truoc).**
- Truoc khi chon buoi: nut "Luu diem danh" **bi khoa** -> nhin qua tuong nhu chi doc.
- **Sau khi chon buoi SANG**: nut "Luu diem danh" **mo khoa** (`disabled: false`), 3 o radio trang thai
  va o "Ly do vang..." **deu sua duoc** (`disabled: false`, `readOnly: false`).
- **Da thuc thi that:** doi hoc vien "QA Import Reverify12 OK" tu **"Co mat" -> "Vang khong phep"** -> bam
  **Luu diem danh**.
  - Bo bat thong bao (`tools/toast-capture.js`, KHONG loc trung): **1 request / 1 khung thong bao**,
    chu = **"Da luu diem danh"** -> may chu **KHONG chan**, khong co thong bao tu choi nao.
  - Mang: `POST /api/v1/khoa-hocs/5eed0002-.../diem-danhs/batch-update` -> **HTTP 200** (reqid=137).
- **Tai lai trang hoan toan** (`reload`, `ignoreCache`) -> chon lai buoi SANG -> trang thai doc len van la
  **"Vang khong phep"** => du lieu **da bi ghi that xuong may chu**, khong phai chi doi tren giao dien.
- => Trai **PRE-03** (`srs-fr-03-dao-tao.md:533`) va trai tac dong **"Dong diem danh"** cua SM-KHOAHOC
  (`srs-v3.5.md:5759`). Can bo van sua + luu duoc diem danh sau khi khoa da dong.
- **Da khoi phuc du lieu seed ve "Co mat"** sau khi lay bang chung (kiem lai: radio "Co mat" checked).

## Ngoai tieu chi BA - co thay gi bat thuong khong?

Doc lai anh da chup: **khong phat hien them bat thuong nao** o tab Diem danh vong nay. Khong co toast lap
(1 request / 1 thong bao). Cac loi ghi nhan o RV5 (DDD-KH-011 hong, KH-20260716-001 ket "Cho duyet",
tab khong tu lam moi) khong nam trong pham vi thao tac vong nay nen khong do lai.

## Ket luan

Dat **3/4** y (giu nguyen thanh qua vong truoc, khong hong nguoc), **van khong dat y 4** - y het vong truoc,
hanh vi **khong doi chut nao**: khoa "Da ket thuc" van sua va luu duoc diem danh, may chu tra 200 va ghi that.
=> **Reopen** (lan 2).

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv6-KTDGKQHT_03-khoa-da-ket-thuc-van-sua-duoc.png`
  (da mo doc lai pixel: stepper "Da ket thuc" active · tab Diem danh · o chon buoi da chon buoi SANG ·
  nut [Luu diem danh] MO KHOA mau xanh · trang thai "Vang khong phep" dang duoc chon **sau khi tai lai trang**)
- `../../bug-reports/ba-approved-batch/image/rv6-KTDGKQHT_03-da-ket-thuc-luu-diem-danh.png`
  (chup ngay sau khi bam Luu)
