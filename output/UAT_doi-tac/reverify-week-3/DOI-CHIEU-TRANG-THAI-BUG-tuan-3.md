# Đối chiếu trạng thái bug — TUẦN 3 (DRIVE ↔ ĐỐI TÁC)

**309 bug · 162 khớp · 135 lệch · 10 không tìm thấy · 0 trừ** (thêm 2 dòng ❔ map không chắc)

> 🔴 **40 dòng đối tác đang để `Reopent` trong khi DRIVE coi như đã xong.** Đây là nhóm cần xử trước.

> **Chỉ đọc.** Không ghi/sửa bất kỳ ô nào trên 2 spreadsheet.

## ⚠️ Đính chính so với bản đầu

Bản đầu chỉ so 2 cặp `Trạng thái 1 ↔ Trạng thái` và `Trạng thái 2 ↔ Trạng thái 2` đúng như đặc tả nhận được, và ra `275 khớp`. **Con số đó sai lệch bản chất.** Lý do: bên DRIVE `Trạng thái 1` = `Fail` ở 309/309 dòng và `Trạng thái 2` trống ở 309/309 dòng — hai cột đó gần như là hằng số, so chúng không phát hiện được gì. Toàn bộ tín hiệu thật nằm ở cột `Trạng thái dev fix` và `Verify`.

Ví dụ do người kiểm bắt được: **`QLBMHD_03`** — DRIVE `Reopen, dev done` + `Verify = Pass`, đối tác `Reopent`. Bản đầu xếp ✅ Khớp vì `Fail = Fail`. Bản này xếp ⚠️ Lệch.

Bản này so **đủ 4 cặp**: `Trạng thái 1↔Trạng thái`, `Trạng thái 2↔Trạng thái 2`, `Trạng thái dev fix 1↔Trạng thái dev fix`, `Trạng thái dev fix 2↔Trạng thái dev fix 2`.

---

## Bức tranh trục `dev fix` vòng 1 — 299 dòng map được

| Số dòng | DRIVE `dev fix 1` | DRIVE `Verify` | ĐỐI TÁC `dev fix` | Đọc là gì |
|---|---|---|---|---|
| 182 | `dev done` | `Pass` | `dev done` | ✅ Hai bên khớp hoàn toàn |
| 45 | `Reject` | `Resolved` | `Resoved` | ⚠️ Tính là lệch khi so chặt từng cột (`Reject` ≠ `Resoved`), nhưng đây là **quy ước đã dùng** — `Reject` ở cột dev fix + `Resolved` ở cột Verify ≡ `Resoved` bên đối tác. Về thực chất hai bên đồng ý. Xem mục riêng cuối bảng lệch. |
| 30 | `Reject` | `Reject` | `Resoved` | ⚠️ Lệch nhãn — cùng kết luận **đóng**, nhưng DRIVE ghi `Reject` còn đối tác đã chuyển `Resoved` |
| 19 | `Reopen, dev done` | `Pass` | `Reopent` | 🔴 DRIVE đã ghi nhận reopen + dev fix lại + QA verify Pass; **đối tác chưa cập nhật** ← `QLBMHD_03` ở nhóm này |
| 18 | `Reject` | `Reject` | `Reopent` | 🔴 **Đối đầu thật** — DRIVE khẳng định không phải lỗi, đối tác mở lại |
| 3 | `dev done` | `Pass` | `Reopent` | 🔴 DRIVE **chưa hề ghi nhận** việc đối tác mở lại |
| 2 | `Reject` | `Reject` | `Reject` | ✅ Khớp |

**Cộng 🔴 = 40 dòng** đối tác còn để `Reopent` trong khi DRIVE coi như xong.

## Hai trục vòng 2

- `Trạng thái 2`: 22 dòng lệch — DRIVE trống, đối tác đã chấm (20 `Pass`, 2 `Fail`).
- `Trạng thái dev fix 2`: 16 dòng lệch — DRIVE trống, đối tác ghi `Resoved`.
- Cả hai đều là **DRIVE chưa chấm vòng 2**, không phải hai bên bất đồng.

---

## Nguồn & cách map

- DRIVE `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` tab `UAT_TGPL Doanh Nghiệp-tuần 3` — 309 dòng.
- ĐỐI TÁC `1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c` tab `UAT_TGPL Doanh Nghiệp` (gid 799081340) — 1671 dòng, lọc `Tuần` = `Tuần 3` → 961 dòng.
- Loại trừ: `reverify-week-4/DANH-SACH-BA-CONFIRM-va-COMMIT-SAU-MOC.md` — 30 mã, **không mã nào thuộc tuần 3** → 0 dòng trừ.
- Map bằng nội dung `Mô tả + Kết quả mong đợi` (chuẩn hoá khoảng trắng + lowercase, `difflib.SequenceMatcher`, chỉ trong cùng tiền tố module, ghép 1-1 theo similarity giảm dần). Khoá phụ: mã TC parse từ tên file cột `Ảnh/vieo 1` bên đối tác. Không dùng chuỗi Mã TC làm khoá chính, không dùng `id-crosswalk.csv`.
- **0 dòng lệch mã TC** — 299 dòng map được đều trùng `Mã TC` hai bên. Tuần 3 không bị đánh số lại như tuần 1.
- Tab tuần 3 bên DRIVE **không có cột `Verify 2`** → ghi `(không có cột Verify 2)`, phân biệt với ô rỗng thật.
- So trạng thái theo **tập token** (tách dấu phẩy), chuẩn hoá chính tả khi so: `Resoved`→`resolved`, `Reopent`→`reopen`. Dữ liệu gốc giữ nguyên văn trong bảng.
- `Reopen, dev done` vs `Reopent` → **lệch** (DRIVE có thêm token `dev done`), không gộp thành khớp.

---

## ⚠️ Lệch — 135 dòng

### 🔴 Đối đầu — DRIVE `Reject`, đối tác `Reopent` — 18 dòng

DRIVE khẳng định không phải lỗi; đối tác không chấp nhận và mở lại. Cần trả lời đối tác.

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 32 | `QLDNDHTPL_17` | Sắp xếp theo cột | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 34 | `QLDNDHTPL_23` | Kiểm tra hiển thị Nhóm 1 — Thông tin doanh nghiệp (thẻ "Thông tin cơ bản") | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 35 | `QLDNDHTPL_24` | Kiểm tra hiển thị Nhóm 2 — Người đại diện | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 36 | `QLDNDHTPL_25` | Kiểm tra hiển thị Nhóm 3 — Tiêu chí ưu tiên theo Nghị định 55/2019/NĐ-CP Điều 4 | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 38 | `QLDNDHTPL_27` | Kiểm tra hiển thị Nhóm 5 — Chỉ số tổng hợp (chỉ hiển thị ở chế độ xem chi tiết) | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 39 | `QLDNDHTPL_28` | Kiểm tra hiển thị Nhóm 6 — Danh sách vụ việc liên kết (thẻ "Lịch sử hỗ trợ") | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 58 | `TLCTCDG_11` | Kiểm tra lưu thành công, tổng trọng số khác 100% | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent` | – |
| 139 | `QLDMCQDVQL_05` | Tìm kiếm không có kết quả | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 167 | `QLTKND_06` | Tìm kiếm không có kết quả | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 194 | `SLHDVM_09` | Kiểm tra chức năng Xóa bộ lọc | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 199 | `VVDTN_09` | Kiểm tra chức năng Xóa bộ lọc | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 206 | `VVDHT_09` | Kiểm tra chức năng Xóa bộ lọc | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 212 | `VVDHTHT_09` | Kiểm tra chức năng Xóa bộ lọc | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 214 | `VVTTG_02` | Kiểm tra hiển thị Chỉ số tổng hợp nhanh | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 219 | `VVTTG_08` | Kiểm tra chức năng Xóa bộ lọc | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 225 | `CLDTBDDDR_09` | Kiểm tra chức năng Xóa bộ lọc | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 256 | `CPCTHTTLHDN_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → Resoved | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent`; `Trạng thái dev fix 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Resoved` | – |
| 259 | `CPCTHTTTG_03` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Reopent` | – |

### 🔴 DRIVE chưa ghi nhận đối tác mở lại — 3 dòng

DRIVE ghi `dev done` + `Verify Pass`, không có token `Reopen` nào — tức phản hồi reopen của đối tác chưa vào sheet DRIVE.

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 13 | `CNKQVV_02` | Kiểm tra hiển thị các trường thông tin Nhóm 6 – Kết luận cuối | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 160 | `QLDMTCDGHTCP_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 161 | `QLDMTCDGHTCP_12` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `dev done` ≠ ĐỐI TÁC `Reopent` | – |

### 🔴 DRIVE đã fix lại, đối tác chưa cập nhật — 19 dòng

DRIVE `Reopen, dev done` + `Verify Pass`. Cần báo đối tác đổi trạng thái.

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 3 | `XNTGHTVV_04` | Xác nhận thành công | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 7 | `PDHSVV_02` | Phê duyệt thành công | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 11 | `CNKQHT_03` | Kiểm tra hiển thị các trường thông tin Nhóm 6 – Kết quả hỗ trợ | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 15 | `DGKQHTVV_01` | Cung cấp chức năng để CB Nghiệp vụ hoặc DNNVV đánh giá chất lượng của quá trình hỗ trợ và… | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 62 | `PCNTHDG_11` | Trình phê duyệt thành công | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 63 | `PDPCDG_01` | Lãnh đạo CQQLNN phê duyệt danh sách người thực hiện đánh giá. | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 64 | `PDPCDG_05` | Từ chối thành công | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 78 | `PDBCDG_01` | Lãnh đạo CQQLNN xem xét và phê duyệt báo cáo đánh giá. | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 79 | `PDBCDG_04` | Từ chối báo cáo thành công | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 97 | `QLBMHD_02` | Kiểm tra hiển thị các trường thông tin | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 98 | `QLBMHD_03` | Kiểm tra nút chức năng "+ Thêm mới" | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 182 | `QLDX_01` | Quản lý quy trình kết thúc phiên làm việc của người dùng. | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 183 | `QLDX_02` | Kiểm tra Hộp thoại xác nhận đăng xuất | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 185 | `QLDKTK_02` | Kiểm tra Thông tin doanh nghiệp | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 186 | `QLDKTK_03` | Kiểm tra Thông tin tài khoản | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 200 | `VVDHT_01` | Thống kê số lượng vụ việc đang được xử lý theo đơn vị, chuyên gia. | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 213 | `VVTTG_01` | Thống kê diễn biến số lượng vụ việc theo các mốc thời gian (ngày, tuần, tháng, quý). | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 241 | `VVTLV_01` | Thống kê số lượng vụ việc theo từng lĩnh vực pháp lý (Lao động, Thuế, Đất đai...). | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |
| 270 | `CTTLV_01` | Thống kê số lượng chương trình hỗ trợ theo lĩnh vực pháp lý. | V1: Fail → Reopen, dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Reopent<br>V2: (trống) → (trống) | 🔴 ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reopen, dev done` ≠ ĐỐI TÁC `Reopent` | – |

### ⚠️ Lệch nhãn — DRIVE `Reject`, đối tác đã chuyển `Resoved` — 30 dòng

Hai bên cùng coi là **đóng**, chỉ khác chữ. DRIVE có thể cân nhắc đồng bộ nhãn.

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 6 | `TBKQTNHS_01` | Cung cấp chức năng gửi thông báo kết quả kiểm tra hồ sơ (Đạt/Không đạt) cho DNNVV. | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 65 | `CVVDG_01` | Lựa chọn các vụ việc cụ thể để tiến hành kiểm tra, đánh giá chất lượng. | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 66 | `CVVDG_02` | Kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá (tab Thực hiện — chế đ… | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 82 | `QLTMBMHD_10` | Kiểm tra hiển thị nút chức năng Sửa" thư mục | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 84 | `QLTMBMHD_17` | Kiểm tra hiển thị nút chức năng Xóa hàng loạt | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 105 | `QLBMHD_12` | Kiểm tra hiển thị nút chức năng Sửa biểu mẫu | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 116 | `IBMHD_02` | Kiểm tra hiển thị các trường thông tin | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 117 | `IBMHD_03` | Kiểm tra chức năng "Tải mẫu Excel" | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 164 | `QLVT_14` | Sắp xếp theo cột | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 170 | `QLTKND_25` | Sắp xếp theo cột | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 171 | `QLTKND_27` | Gửi liên kết đặt lại mật khẩu | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 190 | `SLHDVM_03` | Kiểm tra hiển thị Biểu đồ và bảng kết quả | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 193 | `SLHDVM_08` | Kiểm tra chức năng In báo cáo | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 198 | `VVDTN_08` | Kiểm tra chức năng In báo cáo | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 201 | `VVDHT_03` | Kiểm tra hiển thị Chỉ số tổng hợp nhanh | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 205 | `VVDHT_08` | Kiểm tra chức năng In báo cáo | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 211 | `VVDHTHT_08` | Kiểm tra chức năng In báo cáo | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 218 | `VVTTG_07` | Kiểm tra chức năng In báo cáo | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 221 | `CLDTBDDDR_04` | Kiểm tra hiển thị cột kết quả | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 224 | `CLDTBDDDR_08` | Kiểm tra chức năng In báo cáo | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 226 | `LDTBDDDR_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 229 | `CGTVPL_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 252 | `CPCTHTTDVQL_03` | Kiểm tra hiển thị Chỉ số tổng hợp | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 255 | `CPCTHTTLHDN_03` | Kiểm tra hiển thị Chỉ số tổng hợp | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 266 | `CTTDVQL_02` | Kiểm tra hiển thị Chỉ số tổng hợp | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 271 | `CTTLV_03` | Kiểm tra hiển thị Chỉ số tổng hợp | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 279 | `QLNDTVVCG_06` | Nhóm 1 — Thông tin cơ bản | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 285 | `QLNDTVVCG_20` | Nhóm 5 — Nhật ký thao tác | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 295 | `QLTLPLCVV_03` | Kiểm tra điều kiện hiển thị nút chức năng Thêm mới | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 301 | `QLTLPLCVV_16` | Xóa tệp đính kèm thành công | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |

### ⚠️ Lệch còn lại — hai bên cùng coi là đóng — 21 dòng

Phần lớn là DRIVE chưa chấm vòng 2 (`Trạng thái 2` / `dev fix 2` trống trong khi đối tác đã điền).

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 2 | `XNTGHTVV_03` | Từ chối thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Fail → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Fail` | – |
| 4 | `TPDHSVV_02` | Kiểm tra hồ sơ chưa có kết quả hỗ trợ của người hỗ trợ | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 5 | `TPDHSVV_04` | Trình phê duyệt thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 8 | `PDHSVV_03` | Cán bộ phê duyệt không cùng đơn vị với đơn vị hồ sơ | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 9 | `PDHSVV_04` | Từ chối | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 10 | `PDHSVV_05` | Từ chối thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 12 | `CNKQHT_06` | Hồ sơ đã được người khác cập nhật trong lúc đang sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 14 | `CNKQVV_05` | Hồ sơ đã được người khác cập nhật trong lúc đang thao tác | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 16 | `QLHSDNHTCP_03` | Kiểm tra Cột dữ liệu trong bảng kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Fail → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Fail` | – |
| 18 | `QLHSDNHTCP_09` | Kiểm tra hiển thị thanh tiến trình và tiêu đề trang | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 19 | `QLHSDNHTCP_10` | Nhóm 0 — Thanh thông tin tổng quan hồ sơ | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 20 | `QLHSDNHTCP_11` | Nhóm 1 — Thông tin doanh nghiệp (chỉ đọc, lấy từ Cổng Dịch vụ công) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 21 | `QLHSDNHTCP_12` | Nhóm 2 — Thông tin tư vấn (chỉ đọc, lấy từ Cổng Dịch vụ công) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 22 | `QLHSDNHTCP_13` | Nhóm 8 — Thông tin phê duyệt và Lịch sử xử lý | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 24 | `QLDNDHTPL_02` | Cột dữ liệu trong bảng kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 26 | `QLDNDHTPL_05` | Kiểm tra hiển thị Nhóm A — Định danh cơ bản (bắt buộc) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 27 | `QLDNDHTPL_06` | Kiểm tra hiển thị Nhóm B — Địa lý và phân loại (tùy chọn, có gợi ý mặc định) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 28 | `QLDNDHTPL_07` | Kiểm tra hiển thị Nhóm C — Thông tin bổ sung (tùy chọn) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 29 | `QLDNDHTPL_10` | Kiểm tra trùng mã số thuế | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 48 | `LKHDG_10` | Lưu nháp thành công | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Pass → Reject<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái 1`: DRIVE `Fail` ≠ ĐỐI TÁC `Pass` | – |
| 141 | `QLDMTCTV_01` | Quản lý danh sách các Tổ chức tư vấn tham gia mạng lưới. | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Pass → Reject<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái 1`: DRIVE `Fail` ≠ ĐỐI TÁC `Pass` | – |

### ⚠️ Lệch hình thức theo quy ước `Reject` + `Verify Resolved` ↔ `Resoved` — 44 dòng

**Nhóm này gần như chắc chắn KHÔNG cần xử.** So chặt từng cột thì `Reject` ≠ `Resoved` nên bị đánh ⚠️, nhưng cột `Verify` bên DRIVE ghi `Resolved` — trùng kết luận với `Resoved` bên đối tác. Đây là quy ước đã dùng nhất quán. Liệt kê ra để người kiểm tự quyết, không tự gộp thành ✅.

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 17 | `QLHSDNHTCP_04` | Chọn thẻ phân loại trạng thái | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: Pass → (trống) | ⚠️ Lệch — `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass`; `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 57 | `TLCTCDG_09` | Lưu khi thiếu trường bắt buộc | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 61 | `PCNTHDG_10` | Trình phê duyệt trùng người | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 76 | `TPDBC_02` | Kiểm tra hiển thị nút chức năng Trình phê duyệt | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 80 | `QLTMBMHD_07` | Thêm mới trùng tên | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 103 | `QLBMHD_10` | Thêm mới biểu mẫu công khai | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 104 | `QLBMHD_11` | Thêm mới khi thư mục đã ở trạng thái "Công khai" | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 107 | `QLBMHD_14` | Sửa thành công | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 108 | `QLBMHD_15` | Kiểm tra nút chức năng "Xem" | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 120 | `IBMHD_10` | Vượt tổng dung lượng | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 126 | `QLDMLVPL_19` | Xóa Mục danh mục đang được tham chiếu | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 127 | `QLDMLVPL_21` | Sắp xếp theo cột | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 131 | `QLDMLHHT_16` | Xóa Mục danh mục đang được tham chiếu | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 132 | `QLDMLHHT_18` | Sắp xếp theo cột | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 145 | `QLDMLDN_16` | Xóa Mục danh mục đang được tham chiếu | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 159 | `QLDMTCDGHQ_17` | Chuyển trang | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 169 | `QLTKND_17` | Kiểm tra trùng thư điện tử | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 184 | `QLDX_03` | Tự động đăng xuất khi hết phiên | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 189 | `QLDKTK_09` | Kích hoạt và đặt mật khẩu lần đầu | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 191 | `SLHDVM_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 196 | `VVDTN_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 203 | `VVDHT_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 209 | `VVDHTHT_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 216 | `VVTTG_05` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 222 | `CLDTBDDDR_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 227 | `LDTBDDDR_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 230 | `CGTVPL_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 233 | `DGHQHTPL_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 237 | `CLDTBDPL_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 239 | `VVTDVQL_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 243 | `VVTLV_05` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 246 | `VVTLHDN_05` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 248 | `VVTTGCT_05` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 250 | `CPHTCT_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 253 | `CPCTHTTDVQL_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 257 | `CPCTHTTLHDN_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 260 | `CPCTHTTTG_05` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 264 | `SLCTHT_06` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 268 | `CTTDVQL_04` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 273 | `CTTLV_05` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 275 | `CTTTG_04` | Kiểm tra chức năng Xuất excel | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 277 | `QLNDTVVCG_03` | Cột dữ liệu trong bảng kết quả | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 282 | `QLNDTVVCG_11` | Kiểm tra hiển thị chức năng Chỉnh sửa | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |
| 287 | `QLNDTVVCG_23` | Phân công thành công | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: (trống) → (trống) | ⚠️ Lệch — `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |

## 🚫 Không tìm thấy bên đối tác — 10 dòng

9/10 là mã QA tự mở (`_OOS_`, `_LINHVUC`, `_CONGKHAI`) — đúng như dự kiến. Dòng còn lại `QLHSDNHTCP_19`: module `QLHSDNHTCP` bên đối tác dừng ở `_19` = "Chọn số bản ghi mỗi trang", không có case "Sắp xếp theo cột". Các dòng similarity cao đều là module khác (mô tả chung chung trùng chữ).

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 23 | `QLHSDNHTCP_19` | Sắp xếp theo cột | V1: Fail → Reject / Reject<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.990 là `QLTNVV_08` (Tuần 2) nhưng khác module/khác case | – |
| 302 | `QLTMBMHD_OOS_01` | Thông báo lỗi trùng tên không chèn tên thư mục cụ thể theo mẫu ERR-TM-01 | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.372 là `TBKQTNHS_03` (Tuần 3) nhưng khác module/khác case | – |
| 303 | `XNTGHTVV_OOS_01` | Vụ việc bị tư vấn viên từ chối, quay về 'Đã tiếp nhận' để phân công lại, nhưng KHÔNG phân… | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.256 là `QLNHCH_14` (Tuần 2) nhưng khác module/khác case | – |
| 304 | `XNTGHTVV_OOS_02` | Yêu cầu phân công bị máy chủ từ chối (HTTP 409, không lưu thay đổi) nhưng vẫn ghi thêm 1 … | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.276 là `TKHDVMTH_01` (Tuần 1) nhưng khác module/khác case | – |
| 305 | `CGTVPL_LINHVUC` | BC Số lượng CG/TVV (UC131) không hiển thị mục thống kê "theo lĩnh vực chuyên môn" dù back… | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.346 là `CGTVPL_01` (Tuần 3) nhưng khác module/khác case | – |
| 306 | `QLNDTVVCG_CONGKHAI` | Màn Chi tiết TVCS (SCR-X1-02): nhóm accordion "Trạng thái công khai" (Công khai chuyên tr… | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.245 là `QLNDTVVCG_29` (Tuần 3) nhưng khác module/khác case | – |
| 307 | `QLDNDHTPL_OOS_01` | Chỉnh sửa Doanh nghiệp — QA phát hiện ngoài phạm vi (không thuộc các case đối tác), phát … | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.186 là `PDNDCHTV_02` (Tuần 4) nhưng khác module/khác case | – |
| 308 | `QLTLPLCVV_OOS_01` | Sửa tư liệu pháp lý trong Tư vấn chuyên sâu — QA phát hiện ngoài phạm vi (không thuộc các… | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.171 là `QLLKHDTBD_06` (Tuần 2) nhưng khác module/khác case | – |
| 309 | `QLBMHD_OOS_01` | Chỉnh sửa biểu mẫu — QA phát hiện ngoài phạm vi (không thuộc case nào của đối tác), phát … | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.277 là `CNTTTVV_04` (Tuần 2) nhưng khác module/khác case | – |
| 310 | `IBMHD_OOS_01` | Nhập biểu mẫu hàng loạt — QA phát hiện ngoài phạm vi (không thuộc case nào của đối tác), … | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | (không tìm thấy) | 🚫 Không tìm thấy bên đối tác — đã quét toàn bộ 1671 dòng tab đối tác; gần nhất sim=0.272 là `QLCKCHTV_05` (Tuần 4) nhưng khác module/khác case | – |

## ❔ Map không chắc — 2 dòng

Trùng `Mã TC` + trùng tên file ảnh hai bên; similarity thấp chỉ vì một bên đã sửa text `Kết quả mong đợi`. Nhiều khả năng map đúng, vẫn để ❔ để người kiểm mắt.

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 25 | `QLDNDHTPL_04` | Kiểm tra Cấu trúc màn hình | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: Pass → (trống) | ❔ Map không chắc — sim=0.856; đối tác row 688 mã `QLDNDHTPL_04`; `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass` | – |
| 115 | `CKBMHDLCTT_01` | Đăng tải các biểu mẫu/hợp đồng đã được phê duyệt lên Cổng. | V1: Fail → Reject / Resolved<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → Resoved<br>V2: Pass → (trống) | ❔ Map không chắc — sim=0.798; đối tác row 866 mã `CKBMHDLCTT_01`; `Trạng thái 2`: DRIVE `(trống)` ≠ ĐỐI TÁC `Pass`; `Trạng thái dev fix 1`: DRIVE `Reject` ≠ ĐỐI TÁC `Resoved` | – |

## ✅ Khớp — 162 dòng

Khớp trên cả 4 cặp cột.

| Dòng (drive) | Mã TC (drive) | Mô tả | Trạng thái ở DRIVE | Trạng thái ở ĐỐI TÁC | Khớp? | Trừ? |
|---|---|---|---|---|---|---|
| 30 | `QLDNDHTPL_13` | Thêm mới Nếu trường Tỉnh/Thành phố chưa nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 31 | `QLDNDHTPL_14` | "Hủy" khi có thay đổi chưa lưu | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 33 | `QLDNDHTPL_21` | Xem | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 37 | `QLDNDHTPL_26` | Kiểm tra hiển thị Nhóm 4 — Thông tin khác | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 40 | `QLDNDHTPL_31` | Kiểm tra nút chức năng Sửa tại màn hình xem chi tiết | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 41 | `TKDNHTPL_02` | Kiểm tra Điều kiện tìm kiếm / bộ lọc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 42 | `TKDNHTPL_03` | Tìm kiếm không có kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 43 | `LKHDG_02` | Kiểm tra hiển thị các trường thông tin trong danh sách | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 44 | `LKHDG_03` | Kiểm tra Điều kiện tìm kiếm / bộ lọc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 45 | `LKHDG_04` | Tìm kiếm có kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 46 | `LKHDG_07` | Kiểm tra nút chức năng Thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 47 | `LKHDG_08` | Thiếu trường bắt buộc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 49 | `LKHDG_12` | Xuất Excel | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 50 | `LKHDG_16` | "Sửa" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 51 | `LKHDG_19` | Kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá (tab Kế hoạch) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 52 | `LKHDG_20` | Kiểm tra nút chức năng "Hủy" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 53 | `LKHDG_21` | Kiểm tra chức năng "Lưu nháp" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 54 | `LKHDG_22` | Kiểm tra chức năng "Lưu & Chuyển tiêu chí" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 55 | `TLCTCDG_07` | Kiểm tra nút chức năng "Sửa tiêu chí" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 56 | `TLCTCDG_08` | Kiểm tra nút chức năng "Xóa tiêu chí" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 59 | `TLCTCDG_12` | "Lưu & Quay lại Kế hoạch" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 60 | `PCNTHDG_06` | Kiểm tra nút chức năng "Hủy" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 67 | `CVVDG_03` | Tích chọn vụ việc đã thuộc đợt đánh giá khác | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 68 | `CVVDG_04` | Không có vụ việc trong kỳ | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 69 | `THDG_02` | Kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá (tab Thực hiện — chế đ… | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 70 | `THDG_03` | Lưu kết quả khi điểm vượt | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 71 | `THDG_04` | Tự động tính lại điểm tổng hợp và xếp loại | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 72 | `THDG_05` | Lưu kết quả thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 73 | `LBCDG_02` | Kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá (tab Báo cáo) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 74 | `LBCDG_04` | Kiểm tra nút chức năng "Xuất Excel" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 75 | `LBCDG_05` | "Xuất Word" thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 77 | `TPDBC_03` | Đợt không ở trạng thái "Báo cáo" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 81 | `QLTMBMHD_08` | Thêm mới tên quá dài | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 83 | `QLTMBMHD_13` | Kiểm tra hiển thị nút chức năng Xóa thư mục | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 85 | `QLTMBMHD_19` | Xóa hàng loạt thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 86 | `QLTMBMHD_20` | Xóa hàng loạt một phần thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 87 | `QLTMBMHD_23` | Xuất Excel | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 88 | `TKTMBMHD_02` | Kiểm tra hiển thị danh sách kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 89 | `TKTMBMHD_04` | Kiểm tra Điều kiện tìm kiếm / bộ lọc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 90 | `TKTMBMHD_06` | Tìm kiếm không có kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 91 | `TKTMBMHD_07` | Xóa bộ lọc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 92 | `CKTMBMHDLCTT_02` | Kiểm tra hiển thị nút chức năng công khai | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 93 | `CKTMBMHDLCTT_07` | Công khai hàng loạt thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 94 | `CKTMBMHDLCTT_08` | Công khai hàng loạt một phần thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 95 | `CKTMBMHDLCTT_10` | Ẩn hàng loạt thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 96 | `CKTMBMHDLCTT_11` | Ẩn hàng loạt một phần thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 99 | `QLBMHD_06` | Kiểm tra kích thước tệp không vượt 20 MB. | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 100 | `QLBMHD_07` | Tệp hỏng | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 101 | `QLBMHD_08` | Có mã độc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 102 | `QLBMHD_09` | Tải tệp bị gián đoạn | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 106 | `QLBMHD_13` | Kiểm tra nút chức năng "Sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 109 | `QLBMHD_16` | Kiểm tra nút chức năng Tải về trong màn hình chi tiết biểu mẫu | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 110 | `QLBMHD_17` | Kiểm tra nút chức năng "Xem trước" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 111 | `QLBMHD_18` | Xem trước tệp DOC hoặc DOCX | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 112 | `QLBMHD_19` | Xem trước tệp XLS hoặc XLSX | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 113 | `TKBMHD_03` | Kiểm tra Điều kiện tìm kiếm / bộ lọc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 114 | `TKBMHD_04` | Tìm kiếm không có kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 118 | `IBMHD_04` | Kiểm tra chức năng "Chọn tệp" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 119 | `IBMHD_07` | Một số lỗi | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 121 | `IBMHD_11` | "Hủy" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 122 | `QLDMLVPL_02` | Kiểm tra hiển thị Danh sách loại danh mục (cột tab bên trái) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 123 | `QLDMLVPL_09` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 124 | `QLDMLVPL_14` | Hủy thêm mới khi đang nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 125 | `QLDMLVPL_16` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 128 | `QLDMLHHT_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 129 | `QLDMLHHT_11` | Hủy thêm mới khi đang nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 130 | `QLDMLHHT_13` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 133 | `QLDMCTHT_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 134 | `QLDMCTHT_11` | Hủy thêm mới khi đang nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 135 | `QLDMCTHT_13` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 136 | `QLDMTTVV_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 137 | `QLDMTTVV_11` | Hủy thêm mới khi đang nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 138 | `QLDMTTVV_13` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 140 | `QLDMCQDVQL_12` | Hủy thêm mới khi đang nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 142 | `QLDMLDN_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 143 | `QLDMLDN_11` | Hủy thêm mới khi đang nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 144 | `QLDMLDN_13` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 146 | `QLDMHSDNHT_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 147 | `QLDMHSDNHT_11` | Hủy thêm mới khi đang nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 148 | `QLDMHSDNHT_13` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 149 | `QLDMHSDNTT_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 150 | `QLDMHSDNTT_11` | Hủy thêm mới khi đang nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 151 | `QLDMHSDNTT_13` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 152 | `QLCHTHXLHS_02` | Kiểm tra hiển thị Thanh thẻ (tab) ở đầu trang | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 153 | `QLCHTHXLHS_03` | Kiểm tra hiển thị Bảng cấu hình SLA (thẻ "Thời hạn xử lý / SLA") | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 154 | `QLCHTHXLHS_05` | Bật/tắt gửi thư điện tử | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 155 | `QLCHTHXLHS_06` | Bật/tắt gửi thông báo trong hệ thống | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 156 | `QLCHTHXLHS_07` | Kiểm tra màn hình/popup chỉnh sửa khi nhấn vàp biểu tượng chỉnh sửa tại dòng | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 157 | `QLDMTCDGHQ_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 158 | `QLDMTCDGHQ_12` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 162 | `QLDMLTK_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 163 | `QLDMLTK_12` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 165 | `QLTKND_02` | Kiểm tra Điều kiện tìm kiếm / bộ lọc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 166 | `QLTKND_03` | Kiểm tra Thẻ trạng thái (tab nhanh) | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 168 | `QLTKND_15` | Kiểm tra trùng tên đăng nhập | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 172 | `QLPQTCDL_06` | Chọn/Bỏ chọn đơn vị | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 173 | `QLPQCN_02` | Kiểm tra Bộ chọn vai trò | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 174 | `QLPQCN_03` | Kiểm tra Ma trận Phân quyền | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 175 | `QLLHTNHS_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 176 | `QLLHTNHS_12` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 177 | `QLDMKTNHS_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 178 | `QLDMKTNHS_12` | Kiểm tra các trường thông tin trên màn hình/popup sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 179 | `QLDN_07` | Mã sai hoặc hết hiệu lực | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 180 | `QLDN_10` | Tài khoản "Vô hiệu hóa" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 181 | `QLDN_12` | Tài khoản "Tạm khóa" do quản trị viên cật nhật trạng thái Tạm khóa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 187 | `QLDKTK_04` | Mã số thuế đã tồn tại trong hệ thống | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 188 | `QLDKTK_08` | Kiểm tra các trường bắt buộc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 192 | `SLHDVM_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 195 | `VVDTN_04` | Kiểm tra hiển thị Biểu đồ và bảng kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 197 | `VVDTN_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 202 | `VVDHT_04` | Kiểm tra hiển thị Biểu đồ và bảng kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 204 | `VVDHT_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 207 | `VVDHTHT_03` | Kiểm tra hiển thị Chỉ số tổng hợp nhanh | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 208 | `VVDHTHT_04` | Kiểm tra hiển thị Biểu đồ và bảng kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 210 | `VVDHTHT_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 215 | `VVTTG_03` | Kiểm tra hiển thị Biểu đồ và bảng kết quả | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 217 | `VVTTG_06` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 220 | `CLDTBDDDR_03` | Kiểm tra hiển thị Chỉ số tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 223 | `CLDTBDDDR_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 228 | `LDTBDDDR_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 231 | `CGTVPL_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 232 | `DGHQHTPL_03` | Kiểm tra hiển thị Chỉ số tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 234 | `DGHQHTPL_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 235 | `CLDTBDPL_03` | Kiểm tra hiển thị Chỉ số tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 236 | `CLDTBDPL_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 238 | `CLDTBDPL_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 240 | `VVTDVQL_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 242 | `VVTLV_03` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 244 | `VVTLV_06` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 245 | `VVTLHDN_03` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 247 | `VVTLHDN_06` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 249 | `VVTTGCT_06` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 251 | `CPHTCT_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 254 | `CPCTHTTDVQL_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 258 | `CPCTHTTLHDN_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 261 | `CPCTHTTTG_06` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 262 | `SLCTHT_03` | Kiểm tra hiển thị Chỉ số tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 263 | `SLCTHT_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 265 | `SLCTHT_07` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 267 | `CTTDVQL_03` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 269 | `CTTDVQL_05` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 272 | `CTTLV_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 274 | `CTTLV_06` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 276 | `CTTTG_05` | Kiểm tra chức năng Xuất PDF | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 278 | `QLNDTVVCG_04` | Chọn thẻ phân loại trạng thái | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 280 | `QLNDTVVCG_07` | Kiểm tra thông tin hiển thị sau khi chọn Doanh nghiệp, Chuyên gia / Tư vấn viên | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 281 | `QLNDTVVCG_08` | Nhóm 2 — Nội dung tư vấn | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 283 | `QLNDTVVCG_15` | Cấu trúc màn hình | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 284 | `QLNDTVVCG_17` | Nhóm 1 — Thông tin cơ bản Nhóm 2 — Nội dung tư vấn | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 286 | `QLNDTVVCG_22` | Kiểm tra màn hình chức năng Phân công chuyên gia | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 288 | `QLNDTVVCG_27` | Kiểm tra nút chức năng Hoàn thành tư vấn | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 289 | `QLNDTVVCG_36` | Xác nhận hủy Với trạng thái "Đang tư vấn" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 290 | `QLNDTVVCG_40` | Xuất Excel | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 291 | `TKNDTVVCG_03` | Tìm kiếm theo tên DN | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 292 | `QLHSPLDN_02` | Bảng danh sách hồ sơ pháp lý | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 293 | `QLHSPLDN_03` | Biểu mẫu thêm mới / chỉnh sửa hồ sơ pháp lý | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 294 | `QLTLPLCVV_02` | Bảng danh sách tư liệu pháp lý | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 296 | `QLTLPLCVV_07` | Kiểm tra điều kiện hiển thị nút chức năng Sửa | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 297 | `QLTLPLCVV_08` | Sửa thành công | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 298 | `QLTLPLCVV_09` | Sửa tư liệu đã chuyển sang "Công khai" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 299 | `QLTLPLCVV_11` | Xóa tư liệu đang ở trạng thái "Công khai" | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |
| 300 | `QLTLPLCVV_15` | Tải lên tệp đính kèm chứa mã độc | V1: Fail → dev done / Pass<br>V2: (trống) → (trống) / (không có cột Verify 2) | V1: Fail → dev done<br>V2: (trống) → (trống) | ✅ Khớp | – |

