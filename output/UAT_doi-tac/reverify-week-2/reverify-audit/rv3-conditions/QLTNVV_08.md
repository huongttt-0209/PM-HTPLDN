# Bang doi chieu dieu kien - QLTNVV_08 (re-verify 2026-07-15)

| Điều kiện | Bug gốc / bug reopen | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW, danh sách Vụ việc HTPL | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Không |
| Màn hình | Vụ việc HTPL - Danh sách, tab Tất cả, có nhiều bản ghi | `/vu-viec/danh-sach`, tab Tất cả có 17 bản ghi | Không |
| Thao tác | Bấm tiêu đề cột để sắp xếp; bug gốc không có icon sort/không đổi thứ tự | Cột `Mã VV` và các cột dữ liệu có class `ant-table-column-has-sorters`; bấm `Mã VV` gửi request `sortBy=maVuViec&sortOrder=DESC/ASC`, thứ tự danh sách đổi | Không |
| Evidence kết quả | Cần có cơ chế sort trên bảng danh sách | Header có icon caret, `aria-sort` trên cột đang sort; danh sách đổi từ nhóm `VV-STP.../VV-BTP...` sang `DDD.../EEE...` khi sort ASC | Không |

Ket luan: 0 GAP. Bug da duoc fix: danh sach Vu viec HTPL da co sort theo cot va request sort duoc gui len API.

Evidence:
- `output/UAT_doi-tac/reverify-week-2/bug-reports/image/rv3-QLTNVV_08-before-sort.png`
- `output/UAT_doi-tac/reverify-week-2/bug-reports/image/rv3-QLTNVV_08-sort-ma-vv-asc.png`
- `output/UAT_doi-tac/reverify-week-2/bug-reports/image/rv3-QLTNVV_08-sort-ma-vv-desc.png`
