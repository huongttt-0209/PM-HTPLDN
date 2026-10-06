# Audit tab `bug` — header đầy đủ + 4 dòng FLOW 04 (2026-08-07)

- **Spreadsheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`
- **Tab:** `bug` (gid=1714340219)
- **Thời điểm ĐỌC:** 2026-08-07 01:53 (+07)
- **Công cụ:** `tools/sheet_dump_bug_rows_2026-08-07.py` (READ-ONLY — chỉ `get_all_values()`, không có lệnh ghi)
- **Phạm vi:** dòng 65 (`DGKQHTVV_02`) · 68 (`DGKQHTVV_04`) · 285 (`QLNDTVVCG_19`) · 288 (`QLNDTVVCG_38`)

## 🔴 Dòng cuối cùng CÓ DỮ LIỆU của tab `bug` = **375**

Dòng 375 = `BCTK_QA12` (Trạng thái `Fail`, Trạng thái dev fix `Fixed`).
→ **Dòng bug mới thêm sau này bắt đầu từ dòng 376.**
(API trả về đúng 375 dòng, không có dòng rỗng đuôi.)

---

## Bảng 1 — Header tab `bug` (26 cột)

| STT cột | Chữ cột A1 | Tên header nguyên văn |
|---:|:---:|---|
| 1 | A | `Tên` |
| 2 | B | `STT` |
| 3 | C | `Tuần` |
| 4 | D | `Mã TC` |
| 5 | E | `Tên chức năng` |
| 6 | F | `Tác nhân` + xuống dòng + `"cbnv_tw        Test@1234` / `cbnv_bn        Test@1234` / `cbnv_dp Test@1234` / `cbpd_tw Test@1234` / `cbpd_bn Test@1234` / `cbpd_dp Test@1234"` (ô nhiều dòng) |
| 7 | G | `Mô tả` |
| 8 | H | `Điều kiện` |
| 9 | I | `Dữ liệu đầu vào` |
| 10 | J | `Các bước thực hiện` |
| 11 | K | `Kết quả mong đợi` |
| 12 | L | `Kết quả thực tế` |
| 13 | M | `Ảnh/vieo 1` ← **thiếu chữ `d`**, đúng nguyên văn là "vieo" |
| 14 | N | `Trạng thái` |
| 15 | O | `Dopai` |
| 16 | P | `Loại vấn đề` |
| 17 | Q | `TKM phản hồi lần 1` |
| 18 | **R** | **`Trạng thái dev fix`** ← **KHÔNG có số "1" ở cuối** |
| 19 | S | `DEV phản hồi lần 1` |
| 20 | **T** | **`Kết quả verify`** ← **TỒN TẠI**, không có hậu tố số |
| 21 | U | `Ảnh/video verify` ← ở đây là `video` (có `d`), khác cột M |
| 22 | V | `Trạng thái 2` |
| 23 | W | `TKM phản hồi lần 2` |
| 24 | X | `Trạng thái dev fix 2` |
| 25 | Y | `DEV phản hồi lần 2` |
| 26 | Z | *(header RỖNG — cột không tên)* |

### Chốt 2 cột quan trọng

| Cột cần | Tồn tại? | Chữ cột A1 | Tên chính xác từng ký tự |
|---|---|---|---|
| "Trạng thái dev fix" | ✅ CÓ | **R** | `Trạng thái dev fix` (không có ` 1`, không có dấu cách thừa) |
| "Kết quả verify" | ✅ CÓ | **T** | `Kết quả verify` (chữ `v` thường, không có dấu cách thừa) |

> ⚠️ Cạm bẫy: tab này có **cả** `Trạng thái dev fix` (R) **và** `Trạng thái dev fix 2` (X).
> `sheet_read.py` mặc định tìm `"Trạng thái dev fix 1"` và `"Verify"` — **hai tên đó KHÔNG tồn tại**
> trong tab `bug`, nên chế độ dump mặc định của script đó in `col = None`. Phải dùng `--row` hoặc
> script dump này.

---

## Bảng 2 — 4 dòng trong phạm vi (chỉ liệt kê cột CÓ dữ liệu)

| Cột | Header | Dòng 65 | Dòng 68 | Dòng 285 | Dòng 288 |
|---|---|---|---|---|---|
| C | Tuần | Tuần 3 | Tuần 3 | Tuần 3 | Tuần 3 |
| D | Mã TC | `DGKQHTVV_02` | `DGKQHTVV_04` | `QLNDTVVCG_19` | `QLNDTVVCG_38` |
| E | Tên chức năng | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| G | Mô tả | Kiểm tra hiển thị các trường thông tin Nhóm 8 – Đánh giá | Tự động tính điểm tổng bằng trung bình cộng 3 điểm | Nhóm 4 — Đánh giá chất lượng | Phân công chuyên gia hàng loạt |
| H | Điều kiện | 1. Đăng nhập tài khoản · 2. Hồ sơ vụ việc ở trạng thái "Hoàn thành" hoặc "Đã đánh giá". | (giống dòng 65) | 1. Đăng nhập hệ thống thành công | 1. Đăng nhập hệ thống thành công |
| I | Dữ liệu đầu vào | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| J | Các bước thực hiện | 1. Chọn menu "Vụ việc HTPL" · 2. Tìm kiếm và nhấn Xem chi tiết · 3. Mở Nhóm 8 – Đánh giá | 1. Chọn menu "Vụ việc HTPL" · 2. Tìm kiếm và nhấn Xem chi tiết · 3. Mở Nhóm 8 – Đánh giá · 4. Bấm nút "Đánh giá" và nhấn "Lưu đánh giá" | 1. Chọn menu "Tư vấn" => "Tư vấn chuyên sâu" · 2. Nhấn "Xem chi tiết" tại bản ghi | 1. Chọn menu "Tư vấn" => "Tư vấn chuyên sâu" · 2. Chọn ít nhất 1 dòng bằng ô chọn; các dòng được chọn đều ở trạng thái "Tiếp nhận" · 3. Bấm nút Phân công hàng loạt |
| K | Kết quả mong đợi | - Hệ thống hiển thị các trường thông tin giống với thiết kế · - Dữ liệu hiển thị đúng định dạng và trường thông tin · - Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị | Tự động tính điểm tổng bằng trung bình cộng 3 điểm | Bảng liệt kê các đánh giá chất lượng tư vấn do doanh nghiệp gửi sau khi nhận kết quả. Các cột: Mã đánh giá, Điểm (1-5 sao), Nhận xét của doanh nghiệp, Ngày đánh giá. Tổng hợp ở cuối bảng: điểm trung bình và số lượng đánh giá. Toàn bộ dữ liệu chỉ đọc | Hệ thống mở cửa sổ phân công, áp dụng chuyên gia đã chọn cho tất cả yêu cầu được chọn đồng thời. |
| L | Kết quả thực tế | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| M | Ảnh/vieo 1 | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | `QLNDTVVCG_38.jpg` (hyperlink Drive) |
| N | Trạng thái | `Fail` | `Fail` | `Fail` | `Fail` |
| O | Dopai | `Open` | `Open` | `N/R` | `N/R` |
| P | Loại vấn đề | *(RỖNG)* | đối tác xóa và đánh lệch ID, chuyển lại ID 4 và 5 cho map với đối tác | *(RỖNG)* | *(RỖNG)* |
| Q | TKM phản hồi lần 1 | *(RỖNG)* | *(RỖNG)* | `chưa có dữ liệu test ` | `Hệ thống hiển thị popup "Phân công hàng loạt chưa được hỗ trợ"` |
| **R** | **Trạng thái dev fix** | `Fixed` | `Fixed` | `Fixed` | `Fixed` |
| S | DEV phản hồi lần 1 | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| **T** | **Kết quả verify** | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| U | Ảnh/video verify | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| V | Trạng thái 2 | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| W | TKM phản hồi lần 2 | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| X | Trạng thái dev fix 2 | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| Y | DEV phản hồi lần 2 | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |
| Z | *(không tên)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* | *(RỖNG)* |

Cột A (`Tên`), B (`STT`), F (`Tác nhân…`) **rỗng ở cả 4 dòng**.

---

## Ghi chú vận hành

- Cả 4 dòng đều **chưa có gì ở cột T "Kết quả verify"** → ghi lần đầu, không đè lên verdict cũ.
- Cả 4 dòng đều có **R = `Fixed`** → dev tuyên bố đã sửa; QA phải verify live.
- Sao lưu từng dòng: `DGKQHTVV_02-ketqua-verify-CU.md`, `DGKQHTVV_04-ketqua-verify-CU.md`,
  `QLNDTVVCG_19-ketqua-verify-CU.md`, `QLNDTVVCG_38-ketqua-verify-CU.md` (cùng thư mục `audit/`).
- Cache JSON của lượt đọc (tránh gọi lại API khi bị 429):
  `<scratchpad>/bug_dump_2026-08-07.json` — đọc lại bằng
  `python3 tools/sheet_dump_bug_rows_2026-08-07.py --rows 65 68 285 288 --from-json <path>`.
