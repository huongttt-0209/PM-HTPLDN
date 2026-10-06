# Sổ tay ghi sheet — lô G1 (2026-08-07)

> Do agent **A2 "Hạ tầng"** dựng sẵn. Mọi lệnh dưới đây đã điền sẵn spreadsheet-id / sheet-title /
> sheet-gid / id-column — **copy-paste chạy được ngay**, chỉ thay dòng + mã TC + đường dẫn tệp của bạn.
> Quy tắc nghiệp vụ (verdict nào cho tình huống nào) nằm ở [`00-BRIEF-CHUNG.md`](../00-BRIEF-CHUNG.md) —
> file này chỉ nói **cách bấm**, không nói **bấm gì**.

**Thư mục chạy lệnh:** mọi lệnh đều chạy từ
`/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac`
(gọi tắt là `<TOOLS_ROOT>` bên dưới). Đường dẫn tương đối trong lệnh tính từ đó.

## Tham số cố định

| Tham số | Giá trị |
|---|---|
| `--spreadsheet-id` | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` |
| `--sheet-title` | `bug` |
| `--sheet-gid` | `1714340219` |
| `--id-column` | `Mã TC` |
| Cột verdict | `Trạng thái dev fix` (cột **R**) |
| Cột diễn giải | `Kết quả verify` (cột **T**) |
| Cột ảnh | `Ảnh/video verify` (cột **U**) |

## Dropdown thật của ô verdict — đã đọc trước, KHÔNG có blocker

Đọc ngày 07/08/2026 bằng `UAT_TAB=bug python3 tools/sheet_read.py --dropdown <ROW> "Trạng thái dev fix"`
cho **cả 11 dòng**. Cả 11 dòng có **cùng một** danh sách, giá trị hiện tại đều là `Fixed`:

```
['In Progress', 'Fixed', 'UAT done', 'Bug', 'Test done', 'reject', 'Reopen', 'BA confirm']
```

⇒ Cả 3 giá trị lô G1 cần — `Test done` · `Reopen` · `BA confirm` — **đều có, đúng từng ký tự**
(chữ hoa/thường như trên). Không dòng nào thiếu giá trị nào.

⚠️ Trong dropdown còn `reject` viết **thường** và `Bug` viết **hoa** — lô G1 không dùng 2 giá trị này;
đừng gõ `Reject`, script sẽ chặn.

## Bảng tra 11 dòng — dòng · mã TC · tệp giá trị cũ

Giá trị cũ đã sao lưu ở [`backup-truoc-ghi-G1.json`](backup-truoc-ghi-G1.json). Riêng ô
`Kết quả verify` (dài, nhiều dòng) đã tách sẵn thành tệp để truyền thẳng vào `--expect-file`:

| Dòng | Mã TC | `Trạng thái dev fix` cũ | Tệp `--expect-file` cho `Kết quả verify` | `Ảnh/video verify` cũ |
|---|---|---|---|---|
| 178 | `VVDTN_04` | `Fixed` | `files/expect-cu/178-VVDTN_04-KetQuaVerify-cu.txt` | rỗng |
| 179 | `VVDTN_06` | `Fixed` | `files/expect-cu/179-VVDTN_06-KetQuaVerify-cu.txt` | rỗng |
| 185 | `VVDHT_06` | `Fixed` | `files/expect-cu/185-VVDHT_06-KetQuaVerify-cu.txt` | rỗng |
| 189 | `VVDHTHT_06` | `Fixed` | `files/expect-cu/189-VVDHTHT_06-KetQuaVerify-cu.txt` | rỗng |
| 195 | `VVTTG_05` | `Fixed` | `files/expect-cu/195-VVTTG_05-KetQuaVerify-cu.txt` | rỗng |
| 222 | `VVTDVQL_06` | `Fixed` | `files/expect-cu/222-VVTDVQL_06-KetQuaVerify-cu.txt` | rỗng |
| 226 | `VVTLV_05` | `Fixed` | `files/expect-cu/226-VVTLV_05-KetQuaVerify-cu.txt` | rỗng |
| 230 | `VVTLHDN_05` | `Fixed` | `files/expect-cu/230-VVTLHDN_05-KetQuaVerify-cu.txt` | rỗng |
| 234 | `VVTTGCT_05` | `Fixed` | `files/expect-cu/234-VVTTGCT_05-KetQuaVerify-cu.txt` | rỗng |
| 263 | `CPCTHTTTG_05` | `Fixed` | `files/expect-cu/263-CPCTHTTTG_05-KetQuaVerify-cu.txt` | **ĐÃ CÓ 810 ký tự** |
| 362 | `QLNDTVVCG_OOS_04` | `Fixed` | `files/expect-cu/362-QLNDTVVCG_OOS_04-KetQuaVerify-cu.txt` (tệp rỗng — ô đang rỗng) | rỗng |

> Đường dẫn đầy đủ của tệp `--expect-file` khi chạy từ `<TOOLS_ROOT>`:
> `reverify-week-5/G1-BA-fixed-2026-08-07/files/expect-cu/<tên tệp>`

> **Cả 11 dòng đã được A2 chạy thử `--dry-run` ngày 07/08:** định danh khớp, `--expect` khớp cả 2 ô,
> dropdown chấp nhận verdict. Nếu lúc bạn ghi mà script báo *"… đã thay đổi: hiện tại=… , chờ=…"* thì
> nghĩa là **dev vừa sửa ô đó sau 07/08 14:45** → DỪNG, báo lead, đừng tự cập nhật `--expect`.

---

## a. Ghi verdict 1 dòng

**Bước 0 — viết diễn giải ra tệp `.txt`, KHÔNG nhét vào dòng lệnh.**
Ô `Kết quả verify` là văn bản tiếng Việt nhiều dòng, có dấu, có gạch đầu dòng → nhét vào dòng lệnh sẽ
vỡ dấu ngoặc/xuống dòng. Luôn dùng `--set-file`.

```bash
# đặt tệp diễn giải ở thư mục note/ của lô, đặt tên theo dòng để 5 người không đè nhau
#   reverify-week-5/G1-BA-fixed-2026-08-07/note/<dòng>-<mã TC>-ketqua-verify.txt
```

Văn phong ô này: xem `00-BRIEF-CHUNG.md` §"Văn phong ô `Kết quả verify`".

**Bước 1 — `--dry-run` (BẮT BUỘC, chạy trước mọi lần ghi thật):**

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac"

python3 tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title bug --sheet-gid 1714340219 \
  --row 179 --id-column 'Mã TC' --id-value 'VVDTN_06' \
  --expect 'Trạng thái dev fix=Fixed' \
  --set    'Trạng thái dev fix=Reopen' \
  --expect-file 'Kết quả verify=reverify-week-5/G1-BA-fixed-2026-08-07/files/expect-cu/179-VVDTN_06-KetQuaVerify-cu.txt' \
  --set-file    'Kết quả verify=reverify-week-5/G1-BA-fixed-2026-08-07/note/179-VVDTN_06-ketqua-verify.txt' \
  --reason 'Lô G1 — B<n> verify dòng 179 VVDTN_06' \
  --dry-run
```

**Bước 2 — ghi thật: giữ nguyên lệnh trên, BỎ đúng cờ `--dry-run`.**

Ghi nhớ về `--expect`:
- Script bắt **mọi cột được `--set` đều phải có `--expect`/`--expect-file`** tương ứng, nếu không sẽ dừng.
- `--expect` là khoá chống ghi đè thay đổi mới của dev: script đọc lại ô ngay trước khi ghi, lệch một
  ký tự là dừng, không ghi gì.
- Thay `Reopen` bằng `Test done` hoặc `BA confirm` tuỳ verdict (xem bảng verdict ở `00-BRIEF-CHUNG.md`).
- Chỉ ghi **1 dòng mỗi lần**. Xong trọn 1 case rồi mới sang case kế — cấm gom lô.

---

## b. Đọc lại xác nhận (bắt buộc sau mỗi lần ghi thật)

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac"
UAT_TAB=bug python3 tools/sheet_read.py --row 179
```

Chỉ coi là ghi thành công khi nhìn thấy **đủ 3 điều**:

1. Mục `[3] 'Mã TC'` in ra **đúng mã** của dòng bạn định ghi (không nhầm dòng).
2. Mục `[17] 'Trạng thái dev fix'` in ra **đúng verdict mới** (`Test done` / `Reopen` / `BA confirm`),
   không còn `Fixed`.
3. Mục `[19] 'Kết quả verify'` in ra **đúng đoạn diễn giải bạn vừa viết** (đọc lướt câu mở đầu có ngày
   đo + nhãn bản dựng + tài khoản).

Bản thân `sheet_bug_verify_write.py` cũng tự đọc lại và in `✅ đọc lại R179 (…) = 'Reopen'`; nếu nó in
`❌` thì **đã ghi nhưng đọc lại không khớp** → dừng, báo lead ngay, đừng ghi tiếp.

---

## c. Upload ảnh + gắn vào cột `Ảnh/video verify` — chỉ Reopen/bug

Chỉ chạy mục này sau khi dòng đã được kết luận và cập nhật thành `Reopen`/`Bug`. Case Pass (`Test done`)
**không tạo ảnh, không upload Drive và không ghi cột U**; giữ nguyên ô U cũ nếu đã có. Phép đo, đối chứng và
việc mở đọc tệp bắt buộc vẫn phải hoàn tất, nhưng ghi số liệu quyết định vào `Kết quả verify` là đủ.

Đường dẫn tệp trên máy QA **không phải bằng chứng**. Phải ra link Drive xem được.

**Bước 1 — lưu ảnh vào `image/` của lô**, đặt tên có mã TC ở đầu:
`reverify-week-5/G1-BA-fixed-2026-08-07/image/<mã TC>-<mô tả ngắn>.png`

**Bước 2 — tải lên Drive bằng `drive_upload_g1.py`** (A2 dựng, dùng lại xác thực + thư mục Drive +
scope `drive.file` của `drive_upload_evidence.py`; link tích luỹ ở
`tools/evidence_drive_links_g1.json`; chạy lại **không tải trùng**):

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac"

# 1 ảnh — BẮT BUỘC khai --ma-tc (cột U ghép link theo Mã TC)
python3 tools/drive_upload_g1.py \
  --file  reverify-week-5/G1-BA-fixed-2026-08-07/image/VVDTN_06-xuat-excel-toast.png \
  --ma-tc VVDTN_06 \
  --label "VVDTN_06 - vai tro CB Nghiep vu TW, BC Vu viec da tiep nhan: khung thong bao ngay sau khi bam [Xuat Excel]"

# nhiều ảnh — tệp kê khai, mỗi dòng 3 phần ngăn bằng ký tự Tab:
#   <đường dẫn><TAB><mã TC><TAB><chú thích>
python3 tools/drive_upload_g1.py --manifest reverify-week-5/G1-BA-fixed-2026-08-07/files/anh-B<n>.tsv

# xem lại link đã tạo
python3 tools/drive_upload_g1.py --list
```

- Một ảnh dùng cho nhiều dòng: `--ma-tc "VVDHT_06,VVTTG_05"` (ngăn bằng dấu phẩy).
- **Nhãn phải tả đúng cái tệp đó cho thấy.** Ảnh chụp trạng thái *ngay trước* khi bị chặn thì không
  được gọi là "ảnh lỗi" — ghi đúng là ảnh trạng thái trước thao tác, còn chữ lỗi lấy từ tệp `.txt`
  (nguyên văn thông báo + phản hồi máy chủ). Tệp `.txt` cũng tải lên bằng lệnh này được.

**Bước 3 — ghi link vào cột U bằng `sheet_g1_anhverify_write.py`** (A2 dựng, bản lô G1 của
`sheet_b3_anhverify_write.py`; ghi **siêu liên kết bấm được**, không phải chuỗi thuần):

```bash
python3 tools/sheet_g1_anhverify_write.py --dry-run --chi-dong 179
python3 tools/sheet_g1_anhverify_write.py --write   --chi-dong 179
```

- Script tự lấy mọi ảnh có `maTc` khớp dòng đó, mỗi ảnh 1 dòng `tên tệp — chú thích`, cả dòng là link.
- Guard: sai Mã TC → dừng; **ô U đã có nội dung → dừng, từ chối ghi đè.**
  ⚠️ **Dòng 263 (`CPCTHTTTG_05`) vốn đã có 810 ký tự ở ô U** từ đợt trước → sẽ bị chặn đúng như thiết kế.
  Chỉ thêm `--cho-phep-ghi-de` **sau khi** đã đọc nội dung cũ (lệnh mục b) và thực sự muốn thay.
- Script **chỉ** đụng cột U, không đụng 4 ô chỉ-đọc.

Đừng dùng `sheet_bug_verify_write.py` để ghi cột U — nó ghi chuỗi thuần, link không bấm được.

---

## d. Thêm dòng bug mới khi gặp lỗi tình cờ

Thấy lỗi **ngoài** case đang verify → vẫn phải log thành dòng mới, không lặng lẽ bỏ qua.

**Quy tắc mã:** `<tiền tố module>_QA<số thứ tự 2 chữ số>`.

### Dải số đã chia sẵn cho B1–B5 (để 5 người không cấp trùng mã)

Đã quét **toàn bộ cột `Mã TC` của tab `bug`** ngày 07/08/2026 (378 dòng có dữ liệu). Mã `_QA` đang dùng:

| Tiền tố | Đã dùng tới | Ghi chú |
|---|---|---|
| `BCTK` | `BCTK_QA14` (dòng 378) | 14 mã liên tục QA01→QA14, dòng 363–378 |
| `KTHSYCHTPL` | `KTHSYCHTPL_QA01` (dòng 364) | |
| `QLNDTVVCG` | `QLNDTVVCG_QA01` (dòng 376) | |

**Dải cấp cho từng agent đo** (mỗi agent 4 số liên tiếp, không giẫm chân nhau):

| Tiền tố | B1 | B2 | B3 | B4 | B5 |
|---|---|---|---|---|---|
| `BCTK` (10 dòng cụm A + C — mọi lỗi trên màn Báo cáo thống kê) | `QA15`–`QA18` | `QA19`–`QA22` | `QA23`–`QA26` | `QA27`–`QA30` | `QA31`–`QA34` |
| `QLNDTVVCG` (dòng 362 — tư vấn chuyên sâu / phân công CG-TVV / nhật ký) | `QA02`–`QA05` | `QA06`–`QA09` | `QA10`–`QA13` | `QA14`–`QA17` | `QA18`–`QA21` |
| `KTHSYCHTPL` | `QA02`–`QA05` | `QA06`–`QA09` | `QA10`–`QA13` | `QA14`–`QA17` | `QA18`–`QA21` |
| **Tiền tố mới chưa từng có `_QA`** | `QA01`–`QA04` | `QA05`–`QA08` | `QA09`–`QA12` | `QA13`–`QA16` | `QA17`–`QA20` |

> **Công thức nếu gặp tiền tố ngoài bảng:** số đầu của B*n* = (số `_QA` lớn nhất đang có của tiền tố đó)
> + 1 + (n−1)×4, dùng 4 số liên tiếp. Chưa có mã `_QA` nào ⇒ coi số lớn nhất = 0.
>
> **Chọn tiền tố nào:** dùng tiền tố của nhóm mã TC mà màn hình gặp lỗi đang thuộc về (tra cột `Mã TC`
> trong tab `bug`). Lỗi trên màn Báo cáo thống kê → `BCTK`. Đừng bịa tiền tố mới nếu đã có nhóm phù hợp.
>
> Script có guard "Mã TC phải CHƯA tồn tại" nên cấp trùng sẽ bị chặn — nhưng lúc đó bạn đã mất công
> soạn xong nội dung. Cứ lấy đúng dải của mình.

### Lệnh

Chuẩn bị 1 tệp JSON `{tên header: giá trị}` (chỉ các header được phép — xem dưới) và 1 tệp bằng chứng.

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac"

UAT_TAB=bug python3 tools/sheet_add_bug_row.py \
  --ma-tc BCTK_QA15 \
  --fields-file reverify-week-5/G1-BA-fixed-2026-08-07/files/bug-BCTK_QA15.json \
  --evidence   reverify-week-5/G1-BA-fixed-2026-08-07/image/BCTK_QA15-<mô tả>.png \
  --dry-run

# xem kỹ output rồi bỏ --dry-run để ghi thật
```

⚠️ **Bắt buộc có `UAT_TAB=bug`** ở đầu lệnh, nếu không script ghi nhầm sang tab tuần 3.

Mẫu `--fields-file` (theo đúng khuôn dòng `BCTK_QA14` đã thêm ngày 07/08):

```json
{
  "Mã TC": "BCTK_QA15",
  "Tên chức năng": "Báo cáo thống kê — <màn/chức năng gặp lỗi>",
  "Mô tả": "<1-2 câu tả lỗi, tiếng Việt có dấu>",
  "Điều kiện": "1. Đăng nhập bằng <tài khoản/vai trò>\n2. <dữ liệu cần có>",
  "Dữ liệu đầu vào": "Kỳ báo cáo: … — Thời gian: … — Đơn vị: …",
  "Các bước thực hiện": "1. …\n2. …\n3. …",
  "Kết quả mong đợi": "<điều đáng lẽ phải xảy ra>",
  "Kết quả thực tế": "<điều thực sự xảy ra>",
  "Trạng thái": "Fail",
  "Dopai": "bug",
  "Ảnh/vieo 1": "<dán link Drive lấy từ drive_upload_g1.py --list>"
}
```

- Cột có dropdown, gõ đúng từng ký tự:
  `Trạng thái` ∈ `['Pass', 'Fail', 'N/R']` · `Dopai` ∈ `['InProcess', 'Resoved', 'dev done', 'OSP', 'Bỏ qua', 'Open', 'bug', 'BA']`
  · `Trạng thái dev fix` ∈ danh sách ở đầu file này (dòng bug **mới** thì **để trống** ô này — dev chưa đụng).
  `Loại vấn đề` không có dropdown.
- Header được phép ghi: `STT` · `Tuần` · `Mã TC` · `Tên chức năng` · `Mô tả` · `Điều kiện` ·
  `Dữ liệu đầu vào` · `Các bước thực hiện` · `Kết quả mong đợi` · `Kết quả thực tế` · `Ảnh/vieo 1`
  (đúng typo gốc) · `Trạng thái` · `Dopai` · `Loại vấn đề` · `Trạng thái dev fix` · `Kết quả verify`.
  Header khác → script dừng.
- `--evidence` phải là tệp **có thật, khác 0 byte**, tên tệp **không chứa chữ `partner`** (bằng chứng
  phải do QA tự chụp). Tải ảnh đó lên Drive trước bằng `drive_upload_g1.py` rồi dán link vào `Ảnh/vieo 1`.
- Script chỉ ghi vào **dòng trống ngay sau dòng cuối** (hiện là dòng 379) và tự đọc lại xác nhận.
- Vì 5 agent cùng thêm dòng, **thêm xong 1 dòng thì đọc lại ngay**; nếu dry-run báo dòng đích không
  trống thì có người vừa chèn — chạy lại lệnh, script sẽ tự tính dòng mới.

---

## e. 🔴 Ô CẤM GHI ĐÈ

**Bốn ô sau là CHỈ ĐỌC. Không script nào của lô G1 được phép chạm vào:**

- **`Trạng thái`** (cột **N**)
- **`Kết quả thực tế`** (cột **L**)
- **`TKM phản hồi lần 1`** (cột **Q**)
- **`DEV phản hồi lần 1`** (cột **S**)

Lô G1 được phép ghi tối đa 3 ô: `Trạng thái dev fix` (R) · `Kết quả verify` (T) · `Ảnh/video verify` (U).
Với Pass chỉ ghi R + T; U chỉ ghi cho Reopen/bug theo mục c.

Ngoại lệ duy nhất: khi **thêm dòng bug MỚI** bằng `sheet_add_bug_row.py`, dòng đó do QA tạo từ đầu nên
được điền `Kết quả thực tế` / `Trạng thái` của chính dòng mới — cấm ở đây là cấm sửa dòng **đã có** của
đối tác.

Nếu một script bị guard chặn: **DỪNG, ghi lại nguyên văn lỗi, báo lead.** Cấm ghi tay lên sheet, cấm
viết script ad-hoc để lách guard.

---

## Phụ lục — Dry-run thật dòng 179 (`VVDTN_06`), chạy 07/08/2026

Chạy để chứng minh đường ghi thông suốt. **Chỉ `--dry-run`, không ghi ô nào** — verdict `Reopen` bên
dưới là **giả định**, chưa đo.

```
$ python3 tools/sheet_bug_verify_write.py \
    --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
    --sheet-title bug --sheet-gid 1714340219 \
    --row 179 --id-column 'Mã TC' --id-value 'VVDTN_06' \
    --expect 'Trạng thái dev fix=Fixed' --set 'Trạng thái dev fix=Reopen' \
    --expect-file 'Kết quả verify=…/files/expect-cu/179-VVDTN_06-KetQuaVerify-cu.txt' \
    --set-file    'Kết quả verify=<tệp diễn giải tạm>' \
    --reason 'A2 ha tang — dry-run chung minh duong ghi thong suot, KHONG ghi that' \
    --dry-run

=== spreadsheet=1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s · tab='bug' · gid=1714340219 · row=179 ===
  identity: Mã TC='VVDTN_06'
  'Trạng thái dev fix' (R179)
      CŨ : 'Fixed'
      MỚI: 'Reopen'
  'Kết quả verify' (T179)
      CŨ : 'Verify 06/08/2026, bản dựng V1.0.8 (đối tác đo trên V1.0/V1.0.2). Đo cả hai vai trò, kết quả
             TRÁI NGƯỢC nhau nên chưa chốt được, cần BA xác nhận phạm vi vai trò.\n\n- Với CB Nghiệp vụ TW
             (cbnv_tw — đúng tác nhân theo SRS): XUẤT ĐƯỢC bình thường. […2038 ký tự…]'
      MỚI: '[VĂN BẢN TẠM — CHỈ ĐỂ CHẠY DRY-RUN, KHÔNG PHẢI KẾT QUẢ ĐO THẬT]\nVerify 07/08/2026, bản dựng
             <điền nhãn bản dựng>, tài khoản <điền tài khoản/vai trò>.\n- <triệu chứng đo được lần này>\n'

🔎 DRY-RUN — chưa ghi gì.
```

Ý nghĩa: định danh dòng khớp · `--expect` khớp **cả 2 ô** (nên bản sao lưu là bản trung thực) ·
`Reopen` được dropdown thật của ô R179 chấp nhận. **Cùng lệnh này đã chạy đạt cho cả 11 dòng.**
