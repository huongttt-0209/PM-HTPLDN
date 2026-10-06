# Tệp test NHSYC_06 (tệp đính kèm vi phạm quy định)

Các tệp **lớn đã bị xóa** khỏi repo (25MB + 6×18MB = 133MB) để không phình git. Tệp nhỏ giữ lại.

Sinh lại tệp lớn khi cần re-test:

```bash
python3 - <<'PY'
# vượt 20MB/tệp
with open("qua-dung-luong-25mb.pdf","wb") as f:
    f.write(b"%PDF-1.4\n"); f.write(b"0" * (25*1024*1024))
# vượt tổng 100MB: 6 tệp x 18MB = 108MB (mỗi tệp <20MB)
for i in range(1, 7):
    with open(f"tong-18mb-{i}.pdf","wb") as f:
        f.write(b"%PDF-1.4\n"); f.write(b"0" * (18*1024*1024))
PY
```

Tệp còn giữ trong thư mục này:
- `sai-dinh-dang.txt`, `sai-dinh-dang.exe` — nhánh sai định dạng
- `hople-01..11.pdf` — nhánh vượt số lượng 10 tệp (tải tệp thứ 11)
