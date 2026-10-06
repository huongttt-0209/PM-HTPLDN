# Bang doi chieu dieu kien - QLGVTG_07 (re-verify dev-fix 2026-07-16)

Yeu cau BA (note sheet row 22, duyet bo sung 15/07/2026 - chuyen Dev FE): them nut 👁 Xem vao cot Hanh dong
man Giang vien (SCR-III-05, srs-fr-03:1852), mo man chi tiet 2 tab SAN CO. Chi la hien thi - du lieu va
man chi tiet da co. Verify lai: cot Hanh dong co 👁 Xem -> bam mo dung man chi tiet 2 tab.

| Điều kiện | Yêu cầu BA / bug gốc | Mình test (re-verify 2026-07-16) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu (quan ly giang vien) | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Khong |
| Man hinh | Dao tao, tap huan -> Giang vien / Tro giang -> Danh sach, cot Hanh dong | `/dao-tao/giang-vien/danh-sach`, cot "Hanh dong" | Khong |
| Du lieu tien de | Can >=1 giang vien de co dong co nut Hanh dong | 5 giang vien trong danh sach (seed rv4) | Khong |
| Thao tac | Bam nut 👁 Xem tren 1 dong -> quan sat man mo ra + so tab | Bam 👁 dong `QA GV QLGVTG09` -> mo man chi tiet, bam ca 2 tab | Khong |

Ket qua quan sat (UI, khong dung API de ra verdict):

- Cot **Hanh dong** co **3 nut**: 👁 (eye) · ✏️ (edit) · 🗑 (delete). Truoc day chi co Sua/Xoa.
- Bam **👁** dong `QA GV QLGVTG09` -> dieu huong `/dao-tao/giang-vien/fb261852-2362-4f0a-a540-215596fd521f`
  (man chi tiet), breadcrumb `Trang chu / Dao tao, tap huan / Giang vien / Tro giang / **Chi tiet**`,
  tieu de = ten giang vien `QA GV QLGVTG09`.
- Man chi tiet co **dung 2 tab**: **"Thong tin"** (mac dinh, hien du truong Ho ten / Chuyen nganh / Trinh do /
  To chuc / Email / Dien thoai / Mo ta nang luc / Linh vuc / Tep dinh kem / Trang thai) va
  **"Lich su giang day"**. Bam sang tab 2 -> nap va hien "Chua co lich su giang day" (empty state hop le,
  giang vien nay 0 khoa da day) -> tab hoat dong that, khong phai tab chet.

Ghi nhan them (KHONG anh huong verdict): man "Chi tiet" mo tu nut 👁 van la form co the sua, con nut
Luu/Huy - tuc nut Xem va nut Sua dung chung mot man, chi khac breadcrumb. Day dung la "man chi tiet SAN CO"
ma BA yeu cau tai dung ("Chi la hien thi - du lieu va man chi tiet da co"), nen KHONG tinh la lech yeu cau.
Neu BA muon che do Xem chi-doc thi do la yeu cau moi, can BA chot rieng.

Ket luan: 0 GAP. Dev da lam dung yeu cau BA -> **Pass**.

Evidence: `../../bug-reports/ba-approved-batch/image/rv4-QLGVTG_07-nut-xem-mo-chi-tiet-2tab.png`
