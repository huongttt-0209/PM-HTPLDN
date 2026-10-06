# Bang doi chieu dieu kien - QLKH_01 (verify lan DAU sau khi dev bao fix, 2026-07-17 vong 7)

Boi canh: dong TC nay do **chinh QA mo them** o vong rv5 (dong 112) khi phat hien tinh co luc dinh don du lieu test.
Bug goc **BUG-KH-XOA-500**: xoa khoa hoc **luon that bai** - may chu tra loi he thong `ERR-SYS-00-00-01`
("Loi he thong, vui long thu lai sau"), khoa hoc van con nguyen trong danh sach. Tai hien 2/2 lan.
Cot `Verify` cua dong nay **con TRONG** (chua verify lan nao) - dev da danh dau `dev done`.

Can cu: quy uoc **UI-04** (`srs-v3.5.md:571`) - thao tac hop le phai cho ket qua dung; xoa duoc thi bao thanh cong
va ban ghi bien mat. `ERR-SYS-00-00-01` la ma loi he thong chung (ngoai le chua bat), khong phai loi nghiep vu
co kiem soat.

| Điều kiện | Bug gốc (rv5) | Mình test (verify 2026-07-17 vòng 7) | GAP? |
|---|---|---|:-:|
| Vai tro | `cbnv_tw` (CB_NV_TW) xoa khoa hoc do chinh minh tao | `cbnv_tw`, badge **CB_NV_TW** - dung vai tro bug goc | Không |
| Man hinh | Dao tao, tap huan -> **Khoa hoc** -> nut thung rac tren dong | Dung man **Khoa hoc** -> danh sach -> nut thung rac cot Hanh dong | Không |
| Trang thai ban ghi | Khoa **Du thao**, do chinh minh vua tao, **chua co hoc vien** | Khoa **KH-20260717-004** "QA RV7 - Do lan 4..." trang thai **Du thao**, `cbnv_tw` vua tao, chua co hoc vien - **dung y het tien de bug goc** | Không |
| Thao tac | Bam thung rac -> hop thoai "Xoa khoa hoc?" -> bam [Xoa] | Da chay that: bam thung rac -> hop thoai **"Xoa khoa hoc? Hanh dong nay khong the hoan tac."** -> bam **[Xoa]** | Không |

## Ket qua quan sat (UI, khong dung API de ra verdict)

**DA FIX THAT.**
- Bam thung rac tren dong **KH-20260717-004** -> hien dung hop thoai xac nhan **"Xoa khoa hoc? Hanh dong nay khong
  the hoan tac."** voi 2 nut [Huy] [Xoa].
- Bam **[Xoa]** -> hien thong bao **"Xoa khoa hoc thanh cong"** (khong con "Loi he thong, vui long thu lai sau").
- Danh sach **17 -> 16 ket qua**; dong KH-20260717-004 **bien mat** khoi danh sach.
- Tang mang (doi chieu, khong dung ra verdict): dung **1** yeu cau `DELETE /api/v1/khoa-hocs/d1d58622-...`
  -> **HTTP 204** (thanh cong). Truoc day la **500 `ERR-SYS-00-00-01`**.

**Kiem lai dien rong - 8 lan xoa lien tiep, 8/8 thanh cong:**
- Da xoa tiep 8 khoa rac Du thao: KH-20260717-003 / -002 / -001 va KH-20260716-007 / -006 / -005 / -004 / -003.
- **Ca 8 deu "da xoa OK"**, danh sach 16 -> **8 ket qua**. Khong lan nao that bai.
- Trong 8 khoa nay co **dung 5 khoa rac ma vong rv5 KHONG xoa noi** vi chinh bug nay (KH-20260716-003/004/005/006/007)
  -> vua la bang chung fix, vua **don sach du lieu rac** ma rv5 phai de lai nho Dev/DBA xoa giup. **Khong con
  can Dev/DBA can thiep.**
- Tong cong **9/9 lan xoa thanh cong** (1 lan do chinh + 8 lan don dep).

## Ngoai tieu chi - co thay gi bat thuong khong? KHONG

**Da RUT ghi nhan sai (2026-07-17):** ban dau vong nay ghi *"xoa khoa hoc hien 3 khung thong bao 'Xoa khoa hoc
thanh cong' giong het nhau"* va suy ra loi thong bao lap **lan ra ca thao tac XOA**. **Ghi nhan do SAI.**

Nguyen nhan: bo do `tools/toast-capture.js` (ban truoc 2026-07-17) cai `MutationObserver` moi **ma khong ngat
observer cu** -> cai N lan trong cung phien trang thi 1 toast THAT bi dem N lan. Luc do bo do da duoc cai 3 lan
=> "3 thong bao". Do lai bang bo do sach (**da tu kiem `soObserverDangSong = 1`**): xoa khoa hoc =
**1 `DELETE` -> dung 1 khung thong bao**. Khong co loi lap.

Chi tiet nguyen nhan + cac dau hieu da bo lo: xem `QLKH_02.md` §CANH BAO. Bo do da duoc va idempotent.

## Ket luan

Bug **BUG-KH-XOA-500 da fix that** - xoa khoa hoc chay dung: bao thanh cong, ban ghi bien mat, may chu tra 204.
Tai hien 9/9 lan tren 9 khoa khac nhau. => **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv7-QLKH_01-xoa-khoa-hoc.png`
  (da mo doc lai pixel: danh sach khoa hoc sau khi xoa - **"Hien thi 1-16 / 16 ket qua"** (truoc do 17),
  dong KH-20260717-004 khong con; cac dong Du thao con lai van co nut thung rac mau do)
  **Luu y ve anh:** anh KHONG bat duoc khung thong bao "Xoa khoa hoc thanh cong" vi toast tu tat ~3s, vong goi
  qua MCP tre hon cua so do. Chu thong bao lay bang **bo bat thong bao MutationObserver** - dung phuong phap
  QA_VERIFY_PROTOCOL §GATE cho phep voi UI ephemeral. Bang chung ket qua (17->16, ban ghi bien mat) la thu
  chung minh chac chan nhat va **co day du tren pixel**.
