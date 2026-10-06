# Bang doi chieu dieu kien - QLLKHDTBD_06 (re-verify 2026-07-15)

| Điều kiện | Bug gốc / bug reopen | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|:-:|
| Vai tro | CB Nghiep vu Trung uong, man Ke hoach dao tao - Them moi | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Khong |
| Thao tac | Tao moi Ke hoach dao tao, nhap du truong bat buoc, bo trong Ngan sach du kien | Tao `QA Reverify KH no budget 20260715 1784090136174`, nam 2026, thoi gian 01/05/2026-30/11/2026, noi dung + nguon luc, de trong Ngan sach | Khong |
| Ket qua ky vong | Truong Ngan sach khong bat buoc; bo trong van tao duoc ke hoach trang thai Nhap | POST `/api/v1/ke-hoach-dao-taos` tra 201, payload `nganSachDuKien: null`, tao `KH-20260715-0002`, danh sach hien Ngan sach `-` / `—`, trang thai Nhap | Khong |

Ket luan: 0 GAP. Bug da duoc fix, khong con tai hien loi 500 khi bo trong Ngan sach du kien.

Evidence: `output/UAT_doi-tac/reverify-week-2/bug-reports/image/rv3-QLLKHDTBD_06-reopen-bo-trong-ngan-sach.png`
