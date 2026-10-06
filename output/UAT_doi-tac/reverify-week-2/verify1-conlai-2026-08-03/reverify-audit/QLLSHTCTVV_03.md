# QLLSHTCTVV_03 — evidence audit (verify vòng 1, 2026-08-03)

## 0. Note CŨ của dev ở cột R (backup TRƯỚC khi đè)

> **R125 (DEV phản hồi lần 1) — giá trị cũ:** (TRỐNG — dev không để lại note)
> **P125 (Trạng thái dev fix 1) — giá trị hiện tại:** `dev done` (KHÔNG đụng vào cột P)

---

## 1. Cổng 1 — Bằng chứng đối tác

**File:** `partner-evidence/QLLSHTCTVV_03.png` (md5 `74cc9277740a13bb45c264b58e866ce7`, 249.000 B — **không** trùng md5 với ảnh nào khác trong lô). Đã mở full-res bằng Read tool.

**3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết):**

| # | Dữ kiện | Giá trị đọc từ ảnh |
|---|---|---|
| a | URL / ID bản ghi | `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/06748bb5-e5d4-453f-9490-f07b17fd0a4a` — tư vấn viên `TVV-BTP-TW-0032` "TVV R11 Verify Mail Fix" |
| b | Trạng thái entity | Badge chấm xanh **"Đang hoạt động"**; điểm đầu trang **4.0/5**; ngày công nhận 08/05/2026. Vai trò đăng nhập: "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" |
| c | Dữ liệu tiền đề | Tab **"Lịch sử hỗ trợ (4)"** — có dữ liệu, không rỗng. Thống kê: "Đã hoàn thành 2", "Điểm trung bình **8.3**". Ảnh chụp 29/07/2026 15:42 |

## 2. Cổng 2 — Hiểu bug (3 dòng bắt buộc)

1. **Evidence đã xem:** `QLLSHTCTVV_03.png`, vùng đối tác **khoanh khung đỏ** ở mép phải bảng — bao trọn cột "Đánh giá". Trong khung đó thấy rõ dãy sao của mỗi dòng bị **tách làm 2 hàng**: 4 ngôi sao hàng trên, 1 ngôi sao hàng dưới.
2. **Đối tác phản ánh CỤ THỂ:** (1) cột "Đánh giá" bị tràn màn hình; (2) thiếu cột "Trạng thái". Danh sách cột họ nhìn thấy: Tên vụ việc · Doanh nghiệp · Lĩnh vực · Vai trò · Ngày phân công · Ngày hoàn thành · Kết quả · Đánh giá (cột đầu bị thanh điều hướng che).
3. **Data + bước tái hiện:** tư vấn viên Đang hoạt động có ≥1 vụ việc trong lịch sử hỗ trợ (họ có 4) → mở chi tiết → tab "Lịch sử hỗ trợ".

## 3. Cổng 3 — Bảng đối chiếu SRS vs web

Tài khoản dùng: **`cbnv_tw_02`** (CB Nghiệp vụ - Trung ương #02, `CB_NV_TW`, BTP·TW). Không dùng admin. Bản dựng **HTPLDN · V1.0.5**, ngày test 03/08/2026.
Bản ghi test: **`TVV-BTP-TW-0002`** "QA TVV Seed28 Active", Đang hoạt động, tab **"Lịch sử hỗ trợ (6)"**.

### Ý (2) — "thiếu cột Trạng thái" (đo cấu trúc)

SRS `SCR-IV-03` dòng **1578** mục (b) liệt kê bảng gồm 9 cột. Web đo được **9 cột**, đọc bằng `innerText`:

| # | SRS `:1578` yêu cầu | Web thực tế | Khớp? |
|:-:|---|---|:-:|
| 1 | Mã vụ việc (đường liên kết) | Mã vụ việc | ✅ |
| 2 | Tên vụ việc | Tên vụ việc | ✅ |
| 3 | Doanh nghiệp | Doanh nghiệp | ✅ |
| 4 | Lĩnh vực | Lĩnh vực | ✅ |
| 5 | Vai trò | Vai trò | ✅ |
| 6 | Ngày phân công | Ngày phân công | ✅ |
| 7 | Ngày hoàn thành | Ngày hoàn thành | ✅ |
| 8 | Kết quả | Kết quả | ✅ |
| 9 | Đánh giá (sao) | Đánh giá | ✅ |
| — | *(SRS `:1578` KHÔNG liệt kê cột "Trạng thái")* | *(web cũng không có)* | ✅ |

**→ Web khớp `SCR-IV-03:1578` 9/9 cột, không thiếu cột nào SRS liệt kê.** Nên ý này **không phải `Open`**.

**Nhưng SRS tự mâu thuẫn:**
- `FR-IV-10 (UC48)` §Outputs dòng **792**: `| 5 | trang_thai | text | — | Trạng thái vụ việc |` → khai `trang_thai` là **dữ liệu đầu ra** của chức năng.
- `FR-IV-10` §Inputs dòng **773**: `| 4 | trang_thai_vv | text | N | Lọc trạng thái vụ việc | — | user input |` → cho **lọc** theo trạng thái.
- `SCR-IV-03:1578` mục (a) cũng có bộ lọc "Trạng thái vụ việc" — và bộ lọc này **đang hiện thật trên web**.

**Kiểm chứng dữ liệu:** bản ghi trả về cho tab này **có sẵn** trường trạng thái vụ việc, với 5 giá trị khác nhau trong 6 dòng: `DA_DUYET`, `DA_DANH_GIA`, `DA_PHAN_CONG`, `DANG_XU_LY`, `HOAN_THANH`, `DA_DANH_GIA`. Tức **dữ liệu đã có, lọc được, chỉ không được trình bày thành cột**.

→ Bất đồng nằm ở **ĐẶC TẢ** (đặc tả màn hình vs đặc tả chức năng của cùng một FR), không phải phần mềm làm sai. **Verdict ý (2): `BA confirm`.**

### Ý (1) — "cột Đánh giá tràn màn hình" (đo bố cục)

SRS không quy định bề rộng/bố cục cột → căn cứ là tiêu chí chung ở cột "Kết quả mong đợi" của phiếu: *"Dữ liệu hiển thị không bị tràn/đè lên nhau"*.

| Phép đo | 1440×900 (chuẩn dự án) | 1600×900 | 1920×1000 |
|---|---|---|---|
| Số dòng có dãy sao vỡ 2 hàng | **6/6** | **6/6** | 0/6 |
| Toạ độ đỉnh 5 sao (dòng 1) | `[616,616,616,616,637]` | vỡ | 1 hàng |
| Chiều cao khung sao | **41px** | **41px** | 21px |
| Bề rộng ô "Đánh giá" | **140px** | **140px** | 162px |

**Nguyên nhân đo được:** dãy 5 sao cần **132px** (5×20px + 4×8px khoảng cách). Ô rộng 140px trừ đệm 8px mỗi bên → còn **124px** khả dụng → **thiếu 8px** → ngôi sao thứ 5 xuống dòng.

**Loại trừ cách hiểu khác của chữ "tràn":**
- Bảng **có** thanh cuộn ngang hoạt động bình thường (`.ant-table-content` `overflow-x: auto`, scrollWidth 1390 > clientWidth 1128) — đây là mẫu chuẩn cho bảng nhiều cột, **không tính là lỗi**.
- Trang **không** tràn ngang: `document.scrollWidth` = `clientWidth` = 1432.
- Chữ **không** tràn ra ngoài ô: `saoVuotKhoiO = false`, `td.scrollWidth = td.clientWidth = 140`.
- Lỗi thật nằm ở: **ô quá hẹp làm vỡ dãy sao xuống 2 hàng** — đúng hiện tượng đối tác khoanh đỏ.

→ **Verdict ý (1): `Open`** (`BUG-QLLSHTCTVV_03`).

### Ý (1b) — phát hiện thêm TRONG chính cột "Đánh giá"

- Ô "Điểm trung bình" hiện **8.9**; cùng trang, đầu hồ sơ hiện **4.1/5** → mâu thuẫn thang ngay trên một màn.
- SRS `:1578` mục (c) quy định *"Điểm trung bình: {X}**/5**"*; `FR-IV-10` §Outputs dòng **795** quy định `diem_danh_gia` định dạng **"1.0–5.0"**.
- Dữ liệu nguồn của tab: điểm từng bản ghi là `"9.0"` và `"8.7"`, thống kê `diemTrungBinh: 8.9` → **thang 10**.
- Hệ quả trên giao diện: 2 vụ việc điểm khác nhau (9.0 vs 8.7) **đều hiện 5/5 sao đầy** (`saoDay:5, saoNua:0, saoRong:0`) → mất khả năng phân biệt chất lượng.
- Ảnh đối tác cũng có dấu hiệu này (đầu trang 4.0/5 nhưng ô Điểm trung bình 8.3) — họ không nêu thành ý riêng.

→ **Verdict ý (1b): `Open`** (`BUG-QLLSHTCTVV_03-B`).

## 4. Verdict tổng

| Ý | Nội dung | Verdict |
|---|---|---|
| (1) | Cột "Đánh giá" vỡ 2 dòng ở khung nhìn ≤1600px | **Open** |
| (1b) | Cột "Đánh giá" luôn 5/5 sao + "Điểm trung bình" 8.9 — sai thang | **Open** |
| (2) | Thiếu cột "Trạng thái" | **BA confirm** |

**Verdict tổng = `Open`** (protocol §"1 case gộp nhiều lỗi con": `Open` nếu ≥1 ý Open). P125 giữ nguyên `dev done` của dev, chỉ set Q125.

**Về claim của dev:** dev ghi `dev done` mà **không để lại giải trình nào** ở cột R. Tự test lại thì cả 2 ý đối tác nêu **đều chưa được xử lý**: lỗi bố cục vẫn tái hiện 6/6 dòng ở khung nhìn chuẩn, và cột "Trạng thái" vẫn chưa có (dù đây là điểm cần BA chốt chứ không phải lỗi). Không có bằng chứng nào cho thấy đã có thay đổi.

## 5. Ảnh đã chụp và ĐÃ MỞ ĐỌC

| Ảnh | Nội dung đọc được |
|---|---|
| `image/QLLSHTCTVV_03-web-cot-danhgia-vo-2-dong.png` | Khung nhìn 1440. Bảng 9 cột, không có cột Trạng thái. Cột "Đánh giá" mép phải: mọi dòng có 4 sao hàng trên + 1 sao hàng dưới (cả sao xám lẫn sao vàng). Có thanh cuộn ngang của bảng. |
| `image/QLLSHTCTVV_03-web-diem-8.9-va-sao-day.png` | Khối thống kê "6 · 3 · **8.9**" (không kèm mẫu số). Hai dòng có đánh giá đều 5 sao vàng đầy. Bộ lọc "Trạng thái vụ việc" hiện diện. |

Cả 2 ảnh đã copy sang `bug-reports/mang-luoi-tvv/image/` với tên theo Bug ID.

## 6. Ngoài tiêu chí BA — quan sát thêm

- **502 thoáng qua:** console có 1 lỗi `502` (×4 lần), truy ra là `thong-baos/unread-count` ×3 và 1 lần `lich-su-ho-tro`; lần gọi lại ngay sau đó trả 200. **Không** nằm trong luồng render bảng (các request dựng màn đều 200). Xếp loại: gián đoạn gateway của môi trường, **không** phải lỗi chức năng — không log.
- Bảng "Hợp đồng tư vấn" nằm ngay dưới trong cùng trang **có** cột "Trạng thái" — cho thấy cột trạng thái là mẫu quen thuộc của hệ thống, củng cố cho câu hỏi BA ở ý (2).
- Không có hiện tượng thông báo lặp trong phiên này (tab read-only, không có thao tác ghi).
