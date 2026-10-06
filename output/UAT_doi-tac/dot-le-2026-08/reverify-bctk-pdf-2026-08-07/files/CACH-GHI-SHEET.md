# Cách ghi verdict 21 dòng lô BCTK-PDF vào tab `bug`

> Sinh tự động 2026-08-07. **Chỉ có lệnh sẵn — file này KHÔNG tự ghi gì.**
> Mọi lệnh chạy từ thư mục gốc repo:
> `cd '/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk'`

## Toạ độ đích (chốt cứng, đừng sửa)

| Mục | Giá trị |
|---|---|
| Spreadsheet | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` |
| Tab (`--sheet-title`) | `bug` — viết thường, đúng 3 ký tự, KHÔNG phải `UAT_TGPL Doanh Nghiệp-tuần 3` |
| gid (`--sheet-gid`) | `1714340219` — script tự đối chiếu, lệch là dừng |
| Cột định danh | `Mã TC` (cột `D`) |
| Ô ghi verdict | `Trạng thái dev fix` (cột `R`) |
| Ô ghi diễn giải | `Kết quả verify` (cột `T`) — **chỉ ghi khi verdict = Reopen** |
| Ô CẤM đụng | `N` Trạng thái · `L` Kết quả thực tế · `Q` TKM phản hồi lần 1 · `S` DEV phản hồi lần 1 |

## Luật dùng file này

1. **Luôn chạy bản `--dry-run` trước.** Chỉ khi dry-run in ra đúng cặp CŨ/MỚI mong đợi mới xoá cờ `--dry-run`.
2. `--expect-file` trỏ vào bản sao lưu giá trị CŨ chụp lúc 2026-08-07 18:28
   (`files/expect-cu/`). Nếu trong lúc đó dev/TKM sửa ô, script sẽ **dừng** với thông báo
   `'Trạng thái dev fix' dòng N đã thay đổi` — đó là hành vi đúng, KHÔNG được sửa file expect cho khớp,
   phải đọc lại sheet và xem ai vừa đổi gì.
3. Khối **Pass** chỉ set 1 cột `Trạng thái dev fix`. Không truyền `--set`/`--expect` cho `Kết quả verify`
   (script sẽ báo `có expectation cho cột không được sửa`).
4. Khối **Reopen** set 2 cột. File note `<MãTC>-ketqua-verify.txt` **phải tồn tại trước khi chạy** —
   `--set-file` không tìm thấy file là dừng ngay ở bước phân tích tham số.
5. Giá trị verdict phải là 1 trong 8 giá trị dropdown thật (xem `dropdown-cot-R.md`):
   `In Progress` · `Fixed` · `UAT done` · `Bug` · `Test done` · `reject` · `Reopen` · `BA confirm`.
   **Cấm giá trị ghép** kiểu `Reopen, BA confirm` — không thuộc danh sách, script chặn.
6. `--reason` chỉ vào audit log `tools/sheet_update_audit.jsonl`, không vào sheet. Sửa cho đúng nội dung lô.

## ⚠️ Cảnh báo trước khi bỏ `--dry-run`

Cả 21 dòng đang có `Trạng thái dev fix = UAT done`, **không phải `Fixed`**. Ghi `Test done` lên là **lùi**
trạng thái một bậc so với quy ước cũ (`Fixed` → `Test done` → `UAT done`). Xác nhận với chủ trì lô trước khi ghi thật.

---

## row 175 · `SLHDVM_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 175 --id-column 'Mã TC' --id-value 'SLHDVM_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/175-SLHDVM_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLHDVM_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 175 --id-column 'Mã TC' --id-value 'SLHDVM_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/175-SLHDVM_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLHDVM_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/SLHDVM_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 175 --id-column 'Mã TC' --id-value 'SLHDVM_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/175-SLHDVM_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/175-SLHDVM_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/SLHDVM_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLHDVM_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 175 --id-column 'Mã TC' --id-value 'SLHDVM_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/175-SLHDVM_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/175-SLHDVM_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/SLHDVM_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLHDVM_07: Reopen'
```

---

## row 180 · `VVDTN_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 180 --id-column 'Mã TC' --id-value 'VVDTN_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/180-VVDTN_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDTN_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 180 --id-column 'Mã TC' --id-value 'VVDTN_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/180-VVDTN_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDTN_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDTN_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 180 --id-column 'Mã TC' --id-value 'VVDTN_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/180-VVDTN_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/180-VVDTN_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDTN_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDTN_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 180 --id-column 'Mã TC' --id-value 'VVDTN_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/180-VVDTN_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/180-VVDTN_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDTN_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDTN_07: Reopen'
```

---

## row 186 · `VVDHT_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 186 --id-column 'Mã TC' --id-value 'VVDHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/186-VVDHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDHT_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 186 --id-column 'Mã TC' --id-value 'VVDHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/186-VVDHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDHT_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDHT_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 186 --id-column 'Mã TC' --id-value 'VVDHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/186-VVDHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/186-VVDHT_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDHT_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDHT_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 186 --id-column 'Mã TC' --id-value 'VVDHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/186-VVDHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/186-VVDHT_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDHT_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDHT_07: Reopen'
```

---

## row 190 · `VVDHTHT_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 190 --id-column 'Mã TC' --id-value 'VVDHTHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/190-VVDHTHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDHTHT_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 190 --id-column 'Mã TC' --id-value 'VVDHTHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/190-VVDHTHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDHTHT_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDHTHT_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 190 --id-column 'Mã TC' --id-value 'VVDHTHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/190-VVDHTHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/190-VVDHTHT_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDHTHT_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDHTHT_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 190 --id-column 'Mã TC' --id-value 'VVDHTHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/190-VVDHTHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/190-VVDHTHT_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVDHTHT_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVDHTHT_07: Reopen'
```

---

## row 196 · `VVTTG_06`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 196 --id-column 'Mã TC' --id-value 'VVTTG_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/196-VVTTG_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTTG_06: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 196 --id-column 'Mã TC' --id-value 'VVTTG_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/196-VVTTG_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTTG_06: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTTG_06-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 196 --id-column 'Mã TC' --id-value 'VVTTG_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/196-VVTTG_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/196-VVTTG_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTTG_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTTG_06: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 196 --id-column 'Mã TC' --id-value 'VVTTG_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/196-VVTTG_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/196-VVTTG_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTTG_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTTG_06: Reopen'
```

---

## row 201 · `CLDTBDDDR_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 201 --id-column 'Mã TC' --id-value 'CLDTBDDDR_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/201-CLDTBDDDR_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CLDTBDDDR_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 201 --id-column 'Mã TC' --id-value 'CLDTBDDDR_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/201-CLDTBDDDR_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CLDTBDDDR_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CLDTBDDDR_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 201 --id-column 'Mã TC' --id-value 'CLDTBDDDR_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/201-CLDTBDDDR_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/201-CLDTBDDDR_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CLDTBDDDR_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CLDTBDDDR_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 201 --id-column 'Mã TC' --id-value 'CLDTBDDDR_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/201-CLDTBDDDR_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/201-CLDTBDDDR_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CLDTBDDDR_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CLDTBDDDR_07: Reopen'
```

---

## row 206 · `LDTBDDDR_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 206 --id-column 'Mã TC' --id-value 'LDTBDDDR_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/206-LDTBDDDR_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - LDTBDDDR_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 206 --id-column 'Mã TC' --id-value 'LDTBDDDR_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/206-LDTBDDDR_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - LDTBDDDR_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/LDTBDDDR_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 206 --id-column 'Mã TC' --id-value 'LDTBDDDR_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/206-LDTBDDDR_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/206-LDTBDDDR_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/LDTBDDDR_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - LDTBDDDR_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 206 --id-column 'Mã TC' --id-value 'LDTBDDDR_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/206-LDTBDDDR_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/206-LDTBDDDR_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/LDTBDDDR_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - LDTBDDDR_07: Reopen'
```

---

## row 211 · `CGTVPL_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 211 --id-column 'Mã TC' --id-value 'CGTVPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/211-CGTVPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CGTVPL_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 211 --id-column 'Mã TC' --id-value 'CGTVPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/211-CGTVPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CGTVPL_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CGTVPL_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 211 --id-column 'Mã TC' --id-value 'CGTVPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/211-CGTVPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/211-CGTVPL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CGTVPL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CGTVPL_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 211 --id-column 'Mã TC' --id-value 'CGTVPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/211-CGTVPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/211-CGTVPL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CGTVPL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CGTVPL_07: Reopen'
```

---

## row 215 · `DGHQHTPL_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 215 --id-column 'Mã TC' --id-value 'DGHQHTPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/215-DGHQHTPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - DGHQHTPL_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 215 --id-column 'Mã TC' --id-value 'DGHQHTPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/215-DGHQHTPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - DGHQHTPL_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/DGHQHTPL_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 215 --id-column 'Mã TC' --id-value 'DGHQHTPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/215-DGHQHTPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/215-DGHQHTPL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/DGHQHTPL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - DGHQHTPL_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 215 --id-column 'Mã TC' --id-value 'DGHQHTPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/215-DGHQHTPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/215-DGHQHTPL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/DGHQHTPL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - DGHQHTPL_07: Reopen'
```

---

## row 219 · `CLDTBDPL_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 219 --id-column 'Mã TC' --id-value 'CLDTBDPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/219-CLDTBDPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CLDTBDPL_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 219 --id-column 'Mã TC' --id-value 'CLDTBDPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/219-CLDTBDPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CLDTBDPL_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CLDTBDPL_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 219 --id-column 'Mã TC' --id-value 'CLDTBDPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/219-CLDTBDPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/219-CLDTBDPL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CLDTBDPL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CLDTBDPL_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 219 --id-column 'Mã TC' --id-value 'CLDTBDPL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/219-CLDTBDPL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/219-CLDTBDPL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CLDTBDPL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CLDTBDPL_07: Reopen'
```

---

## row 223 · `VVTDVQL_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 223 --id-column 'Mã TC' --id-value 'VVTDVQL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/223-VVTDVQL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTDVQL_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 223 --id-column 'Mã TC' --id-value 'VVTDVQL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/223-VVTDVQL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTDVQL_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTDVQL_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 223 --id-column 'Mã TC' --id-value 'VVTDVQL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/223-VVTDVQL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/223-VVTDVQL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTDVQL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTDVQL_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 223 --id-column 'Mã TC' --id-value 'VVTDVQL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/223-VVTDVQL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/223-VVTDVQL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTDVQL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTDVQL_07: Reopen'
```

---

## row 227 · `VVTLV_06`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 227 --id-column 'Mã TC' --id-value 'VVTLV_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/227-VVTLV_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTLV_06: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 227 --id-column 'Mã TC' --id-value 'VVTLV_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/227-VVTLV_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTLV_06: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTLV_06-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 227 --id-column 'Mã TC' --id-value 'VVTLV_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/227-VVTLV_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/227-VVTLV_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTLV_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTLV_06: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 227 --id-column 'Mã TC' --id-value 'VVTLV_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/227-VVTLV_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/227-VVTLV_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTLV_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTLV_06: Reopen'
```

---

## row 231 · `VVTLHDN_06`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 231 --id-column 'Mã TC' --id-value 'VVTLHDN_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/231-VVTLHDN_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTLHDN_06: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 231 --id-column 'Mã TC' --id-value 'VVTLHDN_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/231-VVTLHDN_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTLHDN_06: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTLHDN_06-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 231 --id-column 'Mã TC' --id-value 'VVTLHDN_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/231-VVTLHDN_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/231-VVTLHDN_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTLHDN_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTLHDN_06: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 231 --id-column 'Mã TC' --id-value 'VVTLHDN_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/231-VVTLHDN_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/231-VVTLHDN_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTLHDN_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTLHDN_06: Reopen'
```

---

## row 235 · `VVTTGCT_06`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 235 --id-column 'Mã TC' --id-value 'VVTTGCT_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/235-VVTTGCT_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTTGCT_06: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 235 --id-column 'Mã TC' --id-value 'VVTTGCT_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/235-VVTTGCT_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTTGCT_06: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTTGCT_06-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 235 --id-column 'Mã TC' --id-value 'VVTTGCT_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/235-VVTTGCT_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/235-VVTTGCT_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTTGCT_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTTGCT_06: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 235 --id-column 'Mã TC' --id-value 'VVTTGCT_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/235-VVTTGCT_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/235-VVTTGCT_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/VVTTGCT_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - VVTTGCT_06: Reopen'
```

---

## row 239 · `CPHTCT_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 239 --id-column 'Mã TC' --id-value 'CPHTCT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/239-CPHTCT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPHTCT_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 239 --id-column 'Mã TC' --id-value 'CPHTCT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/239-CPHTCT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPHTCT_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPHTCT_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 239 --id-column 'Mã TC' --id-value 'CPHTCT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/239-CPHTCT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/239-CPHTCT_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPHTCT_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPHTCT_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 239 --id-column 'Mã TC' --id-value 'CPHTCT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/239-CPHTCT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/239-CPHTCT_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPHTCT_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPHTCT_07: Reopen'
```

---

## row 244 · `CPCTHTTDVQL_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 244 --id-column 'Mã TC' --id-value 'CPCTHTTDVQL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/244-CPCTHTTDVQL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPCTHTTDVQL_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 244 --id-column 'Mã TC' --id-value 'CPCTHTTDVQL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/244-CPCTHTTDVQL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPCTHTTDVQL_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPCTHTTDVQL_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 244 --id-column 'Mã TC' --id-value 'CPCTHTTDVQL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/244-CPCTHTTDVQL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/244-CPCTHTTDVQL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPCTHTTDVQL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPCTHTTDVQL_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 244 --id-column 'Mã TC' --id-value 'CPCTHTTDVQL_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/244-CPCTHTTDVQL_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/244-CPCTHTTDVQL_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPCTHTTDVQL_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPCTHTTDVQL_07: Reopen'
```

---

## row 259 · `CPCTHTTLHDN_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 259 --id-column 'Mã TC' --id-value 'CPCTHTTLHDN_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/259-CPCTHTTLHDN_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPCTHTTLHDN_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 259 --id-column 'Mã TC' --id-value 'CPCTHTTLHDN_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/259-CPCTHTTLHDN_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPCTHTTLHDN_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPCTHTTLHDN_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 259 --id-column 'Mã TC' --id-value 'CPCTHTTLHDN_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/259-CPCTHTTLHDN_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/259-CPCTHTTLHDN_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPCTHTTLHDN_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPCTHTTLHDN_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 259 --id-column 'Mã TC' --id-value 'CPCTHTTLHDN_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/259-CPCTHTTLHDN_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/259-CPCTHTTLHDN_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CPCTHTTLHDN_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CPCTHTTLHDN_07: Reopen'
```

---

## row 268 · `SLCTHT_07`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 268 --id-column 'Mã TC' --id-value 'SLCTHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/268-SLCTHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLCTHT_07: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 268 --id-column 'Mã TC' --id-value 'SLCTHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/268-SLCTHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLCTHT_07: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/SLCTHT_07-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 268 --id-column 'Mã TC' --id-value 'SLCTHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/268-SLCTHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/268-SLCTHT_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/SLCTHT_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLCTHT_07: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 268 --id-column 'Mã TC' --id-value 'SLCTHT_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/268-SLCTHT_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/268-SLCTHT_07-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/SLCTHT_07-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLCTHT_07: Reopen'
```

---

## row 273 · `CTTDVQL_05`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 273 --id-column 'Mã TC' --id-value 'CTTDVQL_05' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/273-CTTDVQL_05-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTDVQL_05: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 273 --id-column 'Mã TC' --id-value 'CTTDVQL_05' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/273-CTTDVQL_05-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTDVQL_05: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTDVQL_05-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 273 --id-column 'Mã TC' --id-value 'CTTDVQL_05' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/273-CTTDVQL_05-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/273-CTTDVQL_05-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTDVQL_05-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTDVQL_05: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 273 --id-column 'Mã TC' --id-value 'CTTDVQL_05' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/273-CTTDVQL_05-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/273-CTTDVQL_05-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTDVQL_05-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTDVQL_05: Reopen'
```

---

## row 278 · `CTTLV_06`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 278 --id-column 'Mã TC' --id-value 'CTTLV_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/278-CTTLV_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTLV_06: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 278 --id-column 'Mã TC' --id-value 'CTTLV_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/278-CTTLV_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTLV_06: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTLV_06-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 278 --id-column 'Mã TC' --id-value 'CTTLV_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/278-CTTLV_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/278-CTTLV_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTLV_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTLV_06: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 278 --id-column 'Mã TC' --id-value 'CTTLV_06' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/278-CTTLV_06-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/278-CTTLV_06-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTLV_06-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTLV_06: Reopen'
```

---

## row 282 · `CTTTG_05`

R hiện tại: `UAT done` · T hiện tại: *(rỗng)*

### Pass — chỉ đổi `Trạng thái dev fix` → `Test done`

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 282 --id-column 'Mã TC' --id-value 'CTTTG_05' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/282-CTTTG_05-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTTG_05: Pass' \
  --dry-run

# 2) ghi thật (chỉ chạy sau khi dry-run in đúng cặp CŨ/MỚI)
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 282 --id-column 'Mã TC' --id-value 'CTTTG_05' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/282-CTTTG_05-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTTG_05: Pass'
```

### Reopen — đổi `Trạng thái dev fix` → `Reopen` **và** ghi `Kết quả verify`

Viết note vào `output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTTG_05-ketqua-verify.txt` trước, rồi:

```bash
# 1) thử khô
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 282 --id-column 'Mã TC' --id-value 'CTTTG_05' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/282-CTTTG_05-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/282-CTTTG_05-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTTG_05-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTTG_05: Reopen' \
  --dry-run

# 2) ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 282 --id-column 'Mã TC' --id-value 'CTTTG_05' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/282-CTTTG_05-R-cu.txt' \
  --set 'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/282-CTTTG_05-T-cu.txt' \
  --set-file 'Kết quả verify=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/note/CTTTG_05-ketqua-verify.txt' \
  --reason 'Lo BCTK-PDF 2026-08-07 - CTTTG_05: Reopen'
```

---


## Bằng chứng chuỗi lệnh chạy được — dry-run thật row 175 (`SLHDVM_07`)

Chạy lúc 2026-08-07 ~18:30, từ thư mục gốc repo. Đúng khối "Pass · 1) thử khô" ở trên, không sửa gì.

Lệnh:

```bash
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title 'bug' --sheet-gid 1714340219 \
  --row 175 --id-column 'Mã TC' --id-value 'SLHDVM_07' \
  --expect-file 'Trạng thái dev fix=output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07/files/expect-cu/175-SLHDVM_07-R-cu.txt' \
  --set 'Trạng thái dev fix=Test done' \
  --reason 'Lo BCTK-PDF 2026-08-07 - SLHDVM_07: Pass' \
  --dry-run
```

Kết quả in ra (nguyên văn):

```
=== spreadsheet=1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s · tab='bug' · gid=1714340219 · row=175 ===
  identity: Mã TC='SLHDVM_07'
  'Trạng thái dev fix' (R175)
      CŨ : 'UAT done'
      MỚI: 'Test done'

🔎 DRY-RUN — chưa ghi gì.
```

Đọc kết quả:

- Script **không chặn gì**: qua hết 4 chốt an toàn — gid khớp `1714340219`, `Mã TC` dòng 175 đúng `SLHDVM_07`,
  giá trị cũ khớp file expect (`UAT done`), và `Test done` thuộc dropdown thật của chính ô `R175`.
- Không có dòng `ℹ️ ... có validation ...` nghĩa là ô đúng kiểu `ONE_OF_LIST` và đã được đối chiếu danh sách thật.
- Thoát ở nhánh dry-run trước mọi lệnh ghi: **không ghi ô nào, không thêm dòng nào vào `sheet_update_audit.jsonl`.**
