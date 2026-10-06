# Bang doi chieu dieu kien - QLGVTG_12 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 25): LA LOI - phan mem dang so khop don vi bang nhau tuyet doi nen chan
CB Trung uong xoa giang vien tinh. Can cu: giang vien CO phan quyen theo don vi (srs-v3.5.md:2534, :1256),
NHUNG can bo Trung uong la NGOAI LE duoc thao tac toan quoc (BR-AUTH-08, srs-fr-05:2350). Viec can lam:
bo so khop don vi tuyet doi; khi giang vien dang duoc phan cong thi hien canh bao WRN-GV-01 "dang day N khoa"
(srs-fr-03:973, :967) va bat xac nhan truoc khi xoa.
Verify lai: CB Trung uong xoa giang vien tinh khac -> khong bao loi don vi; neu dang day N khoa thi hien
canh bao WRN-GV-01 + hoi xac nhan.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro thao tac | CB Nghiep vu **Trung uong** (ngoai le BR-AUTH-08 toan quoc) | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Khong |
| Don vi cua giang vien bi xoa | Giang vien thuoc **tinh khac** (khong phai TW) | Seed `QA RV4 GV Tinh An Giang` bang tai khoan `cbnv_dp` (CB_NV_DP - So Tu phap An Giang) trong context trinh duyet rieng. Xac nhan scoping that: `cbnv_dp` chi thay 1 GV nay, `cbnv_tw` thay ca 6 | Khong |
| Trang thai phan cong (nhanh WRN-GV-01) | Giang vien **dang duoc phan cong day N khoa** | Seed khoa hoc `KH-20260716-001` ("QA RV4 Khoa hoc de test WRN-GV-01", 01/09-30/09/2026) voi giang vien phu trach `GV-BTP-TW-0007 - ZZZ Cuoi Bang Chu Cai - GV Sort Test` | Khong |
| Thao tac | Bam Xoa -> quan sat co bao loi don vi khong / co canh bao WRN-GV-01 khong | Da chay ca 2 nhanh | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

**Nhanh (a) - CB TW xoa giang vien TINH khac:**
- `cbnv_tw` NHIN THAY `QA RV4 GV Tinh An Giang` trong danh sach (dung BR-AUTH-08 - TW pham vi toan quoc).
- Bam Xoa -> hop thoai `Xac nhan xoa` / "Ban co chac chan muon xoa giang vien "QA RV4 GV Tinh An Giang"?".
- Bam Xoa -> toast **"Da xoa giang vien"**, ban ghi bien mat khoi danh sach.
- **KHONG co bat ky thong bao loi don vi nao.** ✅ DAT - da bo so khop don vi tuyet doi.

**Nhanh (b) - canh bao WRN-GV-01 khi giang vien dang duoc phan cong:**
- Bam Xoa giang vien `ZZZ Cuoi Bang Chu Cai - GV Sort Test` (dang phu trach khoa `KH-20260716-001`).
- Buoc 1: hop thoai `Xac nhan xoa` thong thuong.
- Buoc 2 (sau khi xac nhan): hien hop thoai **`Canh bao`** voi noi dung
  **"Giang vien dang duoc phan cong day 1 khoa. Ban van muon xoa?"** + 2 nut **[Huy]** / **[Xac nhan xoa]**.
  => Dung noi dung WRN-GV-01 BA yeu cau, dem N=1 CHINH XAC (giang vien nay phu trach dung 1 khoa),
  va CO bat xac nhan truoc khi xoa. ✅ DAT
- Bam **[Huy]** -> giang vien VAN CON trong danh sach, khong co request xoa nao duoc gui.
  => Nhanh huy hoat dong dung, canh bao khong phai chi la thong bao trang tri.

Ghi nhan them (KHONG anh huong verdict): cot "So khoa da day" cua giang vien nay van hien `0` vi khoa
`KH-20260716-001` dien ra 01/09-30/09/2026 (tuong lai, chua day). Nhung canh bao van dem dung "1 khoa" -
tuc canh bao dem theo PHAN CONG chu khong theo khoa da day xong. Day la hanh vi DUNG theo yeu cau BA
("khi giang vien dang duoc phan cong").

Ket luan: 0 GAP, ca 2 nhanh deu dat. Dev da lam dung yeu cau BA -> **Pass**.

Evidence:
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_12-tw-xoa-gv-tinh-xacnhan.png` (hop thoai xac nhan xoa GV tinh)
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_12-tw-xoa-gv-tinh-thanhcong.png` (xoa thanh cong, khong loi don vi)
- `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_12-canh-bao-wrn-gv-01-dang-day-1-khoa.png` (canh bao "dang duoc phan cong day 1 khoa" + bat xac nhan)
