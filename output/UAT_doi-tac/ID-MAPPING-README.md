# Ánh xạ Mã TC: file log bug ↔ sheet đối tác

> **Chốt 2026-07-27.** Hai file dùng hai hệ số hiệu khác nhau và **không bên nào đổi lại ID**.
> Cầu nối là bảng ánh xạ [`id-crosswalk.csv`](id-crosswalk.csv), dựng bằng [`tools/build_id_crosswalk.py`](tools/build_id_crosswalk.py).

## Vấn đề

Đối tác chèn case mới vào giữa rồi **đánh số lại** (không cấp mã mới ở cuối). Hệ quả: **144/628 dòng** có cùng Mã TC nhưng là hai nghiệp vụ khác nhau ở hai file.

Ví dụ nguy hiểm nhất: `QLTVV_22` bên đối tác là "Sửa dữ liệu hợp lệ", nhưng bên file log bug lại là "Hủy có thay đổi chưa lưu". Map bằng chuỗi mã TC = dán kết quả của case này sang case khác mà không ai phát hiện.

Tuần 1 lệch gần như toàn bộ (đối tác chèn 1 case "mô tả tổng quan" lên đầu mỗi module → dịch 1 bậc). Tuần 2 lệch không đều 1–3 bậc.

## Cách map — hai khoá bù nhau

| Khoá | Nội dung | Phủ |
|---|---|---|
| **A — tên file bằng chứng** | Mã TC parse từ cột `Ảnh/vieo 1` bên đối tác. Đối tác xác nhận 2026-07-27: *"Mã TC theo Ảnh/video lần 1 vẫn giữ nguyên là mã TC cũ"* | 132/141 dòng lệch (94%) |
| **B — nội dung case** | `Mô tả` + `Kết quả mong đợi` (chuẩn hoá khoảng trắng/hoa-thường) + cùng tiền tố module | bắt nốt 9 dòng khoá A không giúp được (ảnh mang mã mới, vd `TKHDVMTH_08` ↔ `TKHDVMTH_11`) |

Mức tin cậy ghi ở cột `confidence` của bảng:

| Mức | Nghĩa | Số dòng | Script sync |
|---|---|---|---|
| **CAO** | Hai khoá cùng chỉ về một dòng | 525 | dùng mặc định |
| **TRUNG** | Chỉ một khoá match (khoá kia trống / đối tác đã sửa nội dung) | 62 | cần cờ `--allow-trung` |
| **THẤP** | Hai khoá chỉ về hai dòng khác nhau | 11 | luôn bỏ qua, người quyết |
| **KHÔNG** | Không map được — case QA tự thêm (`*_OOS_*`, `QLKH_*`…) | 30 | bỏ qua |

**Quy tắc cho 11 dòng THẤP: ưu tiên khoá NỘI DUNG.** Tên file có thể đặt nhầm (đã gặp `CLDTBDDDR_04.jpg` cho case `LDTBDDDR_04`), nội dung nghiệp vụ thì không. Bảng hiện đã chọn theo nội dung cho các dòng này, nhưng vẫn đánh dấu THẤP để người xem duyệt.

## Quy trình

**Trước mỗi đợt sync** — dựng lại bảng (đối tác sửa sheet liên tục, bảng cũ sẽ stale):

```bash
python3 "output/UAT_doi-tac/tools/build_id_crosswalk.py"
```

**Sync đối tác → file log bug** (kết quả verify vòng 2):

```bash
python3 "output/UAT_doi-tac/tools/sheet_copy_round2_fail.py" --dry-run   # xem trước
python3 "output/UAT_doi-tac/tools/sheet_copy_round2_fail.py"             # ghi thật
python3 "output/UAT_doi-tac/tools/sheet_copy_round2_fail.py" --status Pass   # đồng bộ cả case Pass
```

Script map qua bảng ánh xạ, giữ hyperlink Drive của ô ảnh, không đè ô đã có dữ liệu, đọc lại xác nhận, ghi audit vào `tools/sheet_copy_round2.log`.

**Sync file log bug → đối tác** (verdict `Trạng thái dev fix` + `DEV phản hồi`): `tools/sheet_copy_to_partner.py` — ⚠️ **script này vẫn map bằng mã TC, chưa chuyển sang bảng ánh xạ.** Chưa sửa xong thì đừng chạy tiếp.

## Việc còn tồn

1. **18 verdict đã ghi vào sai case bên sheet đối tác** (do `sheet_copy_to_partner.py` map bằng mã TC trước khi có bảng này): `QLGVTG_09`, `QLHSTVV_04/05/06`, `QLLKHDTBD_06`, `QLTVV_10/12/13/18/20/21/22/23/24`, `TDHSTVV_09/12/13/14`. Cần dựng bảng đối chiếu → chuyển verdict về đúng case → xoá ở case bị ghi nhầm. **Chờ duyệt trước khi ghi lên file đối tác.**
2. Chuyển `sheet_copy_to_partner.py` sang dùng bảng ánh xạ.
3. Duyệt 11 dòng THẤP trong `id-crosswalk.csv`.

## Đề nghị với đối tác (chặn tái diễn)

Case mới thì **cấp mã mới ở cuối module**, không đánh số lại case cũ. Nếu buộc phải renumber, giữ nguyên tên file bằng chứng theo mã cũ — như cách đang làm — vì đó chính là thứ cứu được 94% mapping lần này.
