# Giá trị các ô SẼ BỊ GHI — chụp lại TRƯỚC khi ghi (2026-08-07)

Nguồn: `sheet_read.py --row ...` trên tab `bug` (gid=1714340219), workbook
`1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, đọc lúc bắt đầu phiên 2026-08-07.

Mục đích: 2 ô đích của prompt (`Trạng thái dev fix` cột R · `Kết quả verify` cột T) sẽ bị ĐÈ.
File này giữ nguyên văn giá trị cũ để khôi phục được nếu ghi nhầm.

| Dòng | Mã TC | `Trạng thái dev fix` (R) — giá trị CŨ | `Kết quả verify` (T) — giá trị CŨ |
|---|---|---|---|
| 335 | LBCKQTHCT_01 | `Fixed` | `Hệ thống không chuyển trạng thái thành "Đang lập"` |
| 336 | LBCKQTHCT_03 | `Fixed` | *(rỗng)* |
| 337 | LBCKQTHCT_04 | `Fixed` | *(rỗng)* |
| 338 | LBCKQTHCT_05 | `Fixed` | *(rỗng)* |
| 339 | LBCKQTHCT_06 | `Fixed` | *(rỗng)* |
| 340 | TPDBCKQTHCT_01 | `Fixed` | *(rỗng)* |
| 342 | GKQTHCTHTPL_01 | `Fixed` | *(rỗng)* |

## ⚠️ Dòng 335 khác 6 dòng còn lại — đã ở VÒNG 2

Ngoài 2 ô trên, dòng 335 còn mang dữ liệu vòng 2 do đối tác + dev ghi. **Không ghi đè các ô này:**

| Cột | Header | Giá trị hiện tại |
|---|---|---|
| U | `Ảnh/video verify` | `LBCKQTHCT_01(2).jpg` · `LBCKQTHCT_01_v2.webm` |
| V | `Trạng thái 2` | `Fail` |
| X | `Trạng thái dev fix 2` | `dev done` |

⇒ Ô `Kết quả verify` (T335) đang chứa **kết luận vòng 2 của đối tác**, không phải ô trống.
Ghi verdict vòng này vào T335 = xoá câu đó. Đã giữ nguyên văn ở bảng trên; nội dung ghi mới
phải nhắc lại triệu chứng đó để dev không mất dấu vết.

## Ô CHỈ ĐỌC theo prompt — cấm ghi đè trong mọi trường hợp

`Trạng thái` (N) · `Kết quả thực tế` (L) · `TKM phản hồi lần 1` (Q) · `DEV phản hồi lần 1` (S)

## Dropdown thật của cột `Trạng thái dev fix` (đọc ngày 2026-08-07 tại R335)

`['In Progress', 'Fixed', 'UAT done', 'Bug', 'Test done', 'reject', 'Reopen', 'BA confirm']`

⇒ 3 giá trị prompt yêu cầu (`Test done` / `Reopen` / `BA confirm`) đều hợp lệ. Cột `Kết quả verify`
KHÔNG có dropdown (free text).
