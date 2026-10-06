# Từ vựng dropdown thật của ô cột `R` (Trạng thái dev fix) — 21 dòng tab `bug`

> Nguồn: `spreadsheets.get` READ-ONLY, 1 request gộp 21 range `bug!R{row}`,
> `fields=sheets(data(rowData(values(dataValidation,formattedValue))))`. Đọc lúc **2026-08-07 ~18:29**.
> Spreadsheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` · gid `1714340219` · cột R = index cột 17 (0-based) — API trả `startColumn=17` cho cả 21 ô, khớp header `Trạng thái dev fix`.

## Kết luận nhanh

- **Cả 21/21 ô R dùng CHUNG một danh sách dropdown, không có dòng nào lệch.**
- Loại validation: `ONE_OF_LIST`, `strict=true` (nhập ngoài danh sách sẽ bị Sheet từ chối).
- Danh sách thật, đúng 8 giá trị, đúng thứ tự API trả về:
  `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm`
- ✅ `Test done` HỢP LỆ ở cả 21/21 dòng. ✅ `Reopen` HỢP LỆ ở cả 21/21 dòng. **Không có blocker.**
- ⚠️ Giá trị R **hiện tại của cả 21 dòng đều là `UAT done`** (không phải `Fixed`) — xem mục Rủi ro ở cuối.

## Bảng chi tiết từng dòng

| row | Mã TC | R hiện tại | Danh sách dropdown thật | `Test done` OK? | `Reopen` OK? |
|----:|-------|------------|--------------------------|:---:|:---:|
| 175 | SLHDVM_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 180 | VVDTN_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 186 | VVDHT_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 190 | VVDHTHT_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 196 | VVTTG_06 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 201 | CLDTBDDDR_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 206 | LDTBDDDR_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 211 | CGTVPL_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 215 | DGHQHTPL_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 219 | CLDTBDPL_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 223 | VVTDVQL_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 227 | VVTLV_06 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 231 | VVTLHDN_06 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 235 | VVTTGCT_06 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 239 | CPHTCT_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 244 | CPCTHTTDVQL_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 259 | CPCTHTTLHDN_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 268 | SLCTHT_07 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 273 | CTTDVQL_05 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 278 | CTTLV_06 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |
| 282 | CTTTG_05 | `UAT done` | `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm` | ✅ | ✅ |

## Blocker

**KHÔNG có blocker.** Không dòng nào thiếu `Test done` hoặc thiếu `Reopen`.

Đối chiếu với tiền lệ `'Reopen, BA confirm' không thuộc dropdown thật của ô R72`: chuỗi ghép
nhiều trạng thái (`Reopen, BA confirm`, `Reopen, dev done`…) KHÔNG có trong danh sách 8 giá trị
này, nên **cấm ghi giá trị ghép** vào 21 ô R này — script sẽ dừng ở bước `validate_literal_dropdown`.

## Rủi ro cần biết trước khi ghi thật

1. **Cả 21 dòng đang là `UAT done`, không phải `Fixed`.** `UAT done` đứng SAU `Test done` trong quy trình
   (tiền lệ `sheet_bug_uatdone_2026-08-05.py`: chỉ ghi `UAT done` khi dòng đang `Fixed`, và `NOOP_IF={'UAT done'}`).
   Ghi `Test done` đè lên `UAT done` là **lùi trạng thái**. Cần chủ trì xác nhận đây đúng là điều mong muốn
   trước khi bỏ cờ `--dry-run`.
2. **Cột T (`Kết quả verify`) của cả 21 dòng đang RỖNG** (đã kiểm live 2026-08-07 ~18:29, không chỉ dựa cache).
   Nên kịch bản Reopen sẽ ghi mới, không đè mất chữ của ai.
3. Cột `N` (`Trạng thái`) của cả 21 dòng = `Fail` — chỉ đọc, không đụng tới.
