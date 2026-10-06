# Mục 4 + 5 DÙNG CHUNG — 3 case "Xuất Excel" của Báo cáo thống kê vụ việc

Áp dụng cho: **VVDTN_06** (dòng 179, màn BC Vụ việc đã tiếp nhận) · **VVDHT_06** (dòng 185, màn BC Vụ
việc đang hỗ trợ) · **VVTTG_05** (dòng 195, màn BC Vụ việc theo thời gian).

> 🔴 Ba case có **cùng một câu triệu chứng** nhưng **khác màn**. Cùng chữ không có nghĩa cùng nguyên nhân
> ⇒ **đo từng case trên đúng màn của nó**. File này chỉ dùng chung mục 4 + 5; **mục 1, mục 6 và bằng
> chứng phải riêng từng case** (xem `VVDTN_06.md`, `VVDHT_06.md`, `VVTTG_05.md`).

---

## 2. Đặc tả nói gì (chung)

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`.

- `:85` (TPL-REPORT-FULL, Processing chung bước 7) →
  `Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp {TenBaoCao}_{YYYYMMDD_HHmm}.xlsx — phần giờ-phút bắt buộc để xuất hai lần trong ngày không đè tệp [BA chốt 2026-08-04]`
- `:123` (Acceptance Criteria chung) →
  `**Given** CB nhấn "Xuất Excel" **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, tên tệp đúng khuôn {TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`
- `:1052` (SCR-IX-01 thành phần #8) →
  `action-bar | Nút Xuất Excel | button | "Xuất Excel (.xlsx)" → xuất theo format TT17/2025 | click → auto-download | Sau khi đã "Xem báo cáo"`
- `:1058` (SCR-IX-01 thành phần #14) →
  `content | Toast xuất file | toast | "Đang tạo file..." → "Xuất thành công" + auto-download | — | Khi nhấn xuất`
- `:1092` (Quy tắc tương tác) →
  `Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file.`
- `:87` (bước 9) → `Giới hạn tối đa 10.000 dòng xuất; nếu vượt thì cắt + cảnh báo` · `:114` E4 `WRN-RPT-01`
- **Tác nhân** `:192` / `:236` / `:325` → `CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)`. **QTHT không nằm
  trong tác nhân của bất kỳ FR-IX nào.**
- **Error Handling chung** (`:111`–`:119`), 2 mã liên quan trực tiếp:
  - `:116` → `| E6 | Lỗi xuất file | ERR-RPT-04 | "Không thể tạo file xuất. Vui lòng thử lại" | ERROR |`
  - `:117` → `| E7 | Không có quyền | ERR-RPT-05 | "Bạn không có quyền xem báo cáo này" | ERROR |`
  ⇒ Bảng E1–E9 liệt kê **đóng** tập phản hồi lỗi của luồng báo cáo, mọi dòng đều có **câu tiếng Việt cụ
  thể**. Không có mục nào cho phép trả chuỗi `Forbidden`.

**IM LẶNG về:** số dòng/số sheet cụ thể trong tệp · thứ tự cột trong tệp · có phải kèm biểu đồ vào tệp
không · nút Xuất có được hiển thị cho vai trò ngoài tác nhân hay không.

---

## 4. Tiêu chí chấm (dùng chung, chấm RIÊNG từng màn)

✅ **PASS khi ĐỦ cả 5:**

1. **Đăng nhập đúng tác nhân** (`cbnv_tw`), bấm "Xem báo cáo" ra dữ liệu, rồi bấm "Xuất Excel" →
   **tệp .xlsx thật sự về được máy người dùng**, không kèm thông báo lỗi nào.
2. **Mở đọc được nội dung tệp** (giải nén .xlsx, đọc ô) — không chấp nhận "200 + có bytes".
   Trong tệp phải đọc ra: **tên báo cáo** · **kỳ báo cáo** · **khoảng thời gian từ–đến** · **đơn vị** ·
   **ngày/thời điểm tạo** (`:1092`).
3. **Số liệu trong tệp khớp số liệu đang hiển thị trên màn** — ít nhất tổng chính của màn
   (`Tổng vụ việc` / `Tổng vụ việc toàn kỳ`) xuất hiện đúng trong tệp, và mọi chiều phân rã có trên màn
   thì cũng có trong tệp với đúng con số.
4. **Tệp áp đúng bộ lọc đang chọn** — đổi bộ lọc (đơn vị hoặc khoảng thời gian) rồi xuất lại thì nội
   dung tệp đổi theo; không trả về tập dữ liệu mặc định.
5. **Tên tệp đúng khuôn** `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (`:85`), trong đó `{TenBaoCao}` là tên loại
   báo cáo viết liền PascalCase, bỏ dấu tiếng Việt và bỏ ký tự không phải chữ/số (`:86`).

❌ **FAIL nếu bất kỳ:** bấm Xuất Excel mà không có tệp nào về máy · có thông báo lỗi thay cho tệp
(`Không thể tạo file xuất...`, `Forbidden`, hoặc bất kỳ câu nào khác) · tệp về được nhưng mở ra hỏng /
rỗng / không đọc được · tệp thiếu bất kỳ mục nào trong 5 mục header ở tiêu chí 2 · số trong tệp lệch số
trên màn · tệp không đổi khi đổi bộ lọc · tên tệp lệch khuôn `:85`.

⛔ **KHÔNG được chấm Fail vì:**
- Tệp không kèm **biểu đồ** — đặc tả im lặng.
- Thứ tự cột / số sheet trong tệp khác hình dung của mình — đặc tả im lặng.
- Font trong tệp không phải Times New Roman 13: `:85` **có** quy định, nhưng đây là **phát hiện ngoài vế
  đối tác nêu** (đối tác chỉ nêu "không tạo được tệp") ⇒ xử theo §"Phát hiện mới", **không kéo verdict**.
- Vai trò **QTHT** bị chặn xuất tệp: QTHT không thuộc tác nhân `:192`/`:236`/`:325`, việc **chặn** là hợp
  lý. Nhưng **chữ** của thông báo chặn thì `:117` có quy định — xem tiêu chí đối chứng dưới đây.

**Tiêu chí đối chứng vai trò (bắt buộc chạy, để đóng GAP vai trò — KHÔNG kéo verdict case):**
Đăng nhập đúng vai trò đối tác đã dùng (**QTHT**), lặp lại đúng thao tác. Ghi nhận:
(i) màn có cho xem báo cáo không · (ii) nút Xuất Excel có hiện không · (iii) bấm vào thì **nguyên văn**
thông báo là gì · (iv) mã lỗi + phản hồi máy chủ. Nếu bị chặn mà chữ **không phải** câu `:117`
(`"Bạn không có quyền xem báo cáo này"`) → đó là **lỗi riêng về phản hồi lỗi**, log thành phiếu riêng
theo §"Bug phát sinh thêm ngoài phạm vi", không gộp vào 3 case này.

---

## 5. Dạng dữ liệu phải phủ (dùng chung)

**M = 3 dạng**, mỗi dạng đo trên **đúng màn của case đó**:

| # | Dạng | Vì sao phải có |
|---|---|---|
| 1 | Vai trò **CB Nghiệp vụ TW** (`cbnv_tw`) + kỳ **có** dữ liệu | Đúng tác nhân `:192`/`:236`/`:325` — đây là dạng ra verdict |
| 2 | Vai trò **QTHT** (`admin`) + kỳ **có** dữ liệu | Trùng khít điều kiện đối tác (bằng chứng cho thấy đối tác dùng QTHT) — dạng này đóng GAP vai trò |
| 3 | Vai trò **CB Nghiệp vụ TW** + **đổi bộ lọc** (khác đơn vị hoặc khác khoảng thời gian) | Chứng minh tệp áp đúng bộ lọc hiện tại (tiêu chí 4), không phải tệp mặc định |

**Nguồn xác định M:** ① tác nhân khai trong SRS (`:192` / `:236` / `:325`) · ② vai trò đọc được từ bằng
chứng đối tác (QTHT, góc phải màn) · ③ tiêu chí 4 ở mục 4 đòi phép thử đổi bộ lọc.

Không tính "xuất PDF" vào M — 3 case này chỉ nêu Excel; PDF nếu có lỗi thì xử theo §"Phát hiện mới".
