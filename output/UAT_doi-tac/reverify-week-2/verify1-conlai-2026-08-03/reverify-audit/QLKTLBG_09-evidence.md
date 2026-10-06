# QLKTLBG_09 — Cổng 1 + Cổng 2 (AGENT-EVIDENCE, 2026-08-03)

> Sheet: `UAT_TGPL Doanh Nghiệp-tuần 2` row **117** · `fetch_evidence.py` **exit 0** (1 link Drive, tải được `QLKTLBG_09_v2.webm`, 1.968.889 bytes).
> Ô "Ảnh/video 2" (cột T) **trống**. Video dài **~6,2 giây**, đã trích 13 frame mỗi 0,5s + 3 frame mỗi 3s.

## Cổng 1 — 3 dữ kiện neo

**(a) URL / mã bản ghi đối tác đang đứng**
- `htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` — màn `Đào tạo, tập huấn → Kho tài liệu / Bài giảng → Danh sách`.
- Bản ghi thao tác: dòng đầu bảng, tên **`TKM thêm mới slide bài giảng`**. **Không có mã bản ghi hiển thị** trên màn danh sách (bảng chỉ có Tên bài giảng / Loại tài liệu / Dung lượng / ngày / Thao tác).
- File thật phía sau bản ghi: **`10.2. Tia, đoạn thẳng.pptx`** (đọc từ hộp thoại Save As, frame `t004.14s`).

**(b) Trạng thái entity**
- Modal xem trước hiển thị: `Công khai = **Đã công khai**` (tag xanh), `Ngày công khai = **23/07/2026 16:01**`.
- Trên danh sách: `Loại tài liệu = **Slide**` (tag xanh), `Dung lượng = **2.2 MB**`.

**(c) Dữ liệu tiền đề**
- Kho tài liệu đang có ≥8 bản ghi nhiều loại: Slide (1 — bản ghi test), Video (`Test video 2`, `testvideo 1`, `sdsdsd` — cột Dung lượng đều `–`), PDF (`sdsdsdsss11` 329 B, `Bài giảng số 10 – Giới thiệu chung` 28.7 KB, `Bài giảng 09 – Luật Doanh nghiệp 2020 cập nhật (PDF)` 5.4 MB, `Bài giảng 08 – Bộ luật Dâ…`).
- Thanh lọc đang bật **`Bộ lọc nâng cao (2)`** (2 điều kiện lọc nâng cao đang áp) — các ô `Tìm theo tên bài giảng`, `Loại tài liệu`, `Lĩnh vực pháp lý`, `Công khai` đều để trống.
- Bản ghi đích là **loại `Slide`** — đây là tiền đề then chốt của case.

## Cổng 2 — 3 dòng

**(1) Evidence đã xem + frame chứa LỖI**
`partner-evidence/QLKTLBG_09_v2.webm`. Chuỗi frame chứa lỗi:
- `t003.10s` — rê chuột lên icon con mắt của dòng `TKM thêm mới slide bài giảng`, tooltip hiện chữ **"Xem trước"**.
- `t003.62s` — modal **"Xem trước: TKM thêm mới slide bài giảng"** mở ra nhưng **chỉ có 3 dòng metadata**: `Công khai / Ngày công khai`, `Ảnh đại diện` (1 ảnh thumbnail tĩnh), `Mô tả công khai` = `—`. **Không có khung trình chiếu slide, không có nút chuyển trang, không có iframe/viewer nào.**
- **`t004.14s` (và giữ nguyên tới `t006.19s`, hết video) = FRAME LỖI:** hộp thoại **Windows "Save As"** bật lên đè lên modal, `File name: 10.2. Tia, đoạn thẳng.pptx`, `Save as type: Microsoft PowerPoint Presentation (*.pptx)` → trình duyệt đang **tải file .pptx xuống máy** ngay sau khi bấm "Xem trước".
- 1 câu tả lỗi: *bấm "Xem trước" một bài giảng loại Slide, hệ thống mở modal chỉ chứa metadata + ảnh đại diện rồi bung hộp thoại tải file .pptx về máy, không trình chiếu nội dung slide trong trang.*

**(2) Đối tác phản ánh CỤ THỂ gì**
Với bài giảng/tài liệu **loại `Slide`**, hệ thống **tải file xuống** thay vì mở khu vực xem trước **trình chiếu inline**. Kết quả mong đợi ghi ở sheet: *"Hệ thống mở khu vực xem trước nội dung với Slide: trình chiếu inline"*. Đối tác **không** nói lỗi ở loại PDF/Video — chỉ nói loại Slide.

**(3) Data + bước tái hiện chính xác**
1. Đăng nhập **Cán bộ nghiệp vụ Trung ương** (`CB_NV_TW`, `BTP · TW`).
2. Menu `Đào tạo, tập huấn` → `Kho tài liệu / Bài giảng`.
3. Tìm/dựng 1 bài giảng **`Loại tài liệu = Slide`**, file đính kèm **`.pptx`** (đối tác dùng file `10.2. Tia, đoạn thẳng.pptx` ~2.2 MB), trạng thái **Đã công khai**.
4. Ở cột `Thao tác`, bấm **icon con mắt (tooltip "Xem trước")** của dòng đó.
5. Quan sát: modal "Xem trước: …" có khung trình chiếu slide không, và trình duyệt có kích hoạt download `.pptx` không.

## Vai trò / tài khoản đối tác dùng

`Cán bộ NV Trung ương` — mã **`CB_NV_TW`**, đơn vị **`BTP · TW`** (đọc ở header phải, frame `t000.00s`/`t003.10s`). Nhóm tài khoản sheet: `cbnv_tw`. Thời điểm quay: **04:04 PM 2026-07-23** (đồng hồ Windows).

## Ghi chú cho người verify

- **Tiền đề bắt buộc:** phải là bản ghi **loại `Slide`** với file **`.pptx`** thật. Nếu test bằng bản ghi PDF (`Bài giảng 09 …`) thì hành vi khác hẳn → không phải điều kiện đối tác.
- Nút cần bấm là **icon con mắt trong cột `Thao tác`**, tooltip **"Xem trước"** (không phải icon bút Sửa / thùng rác Xoá).
- Muốn bắt được hành vi tải file trên môi trường MCP isolated: hộp thoại Save As của OS **không** xuất hiện; hãy đo bằng **network request tới endpoint download + header `Content-Disposition: attachment`**, hoặc bằng việc modal không render viewer. Đừng kết luận "không tải" chỉ vì không thấy hộp thoại.
- Đối tác **đã bật `Bộ lọc nâng cao (2)`** khi thao tác — bộ lọc này không ảnh hưởng hành vi xem trước, nhưng nếu list không ra bản ghi Slide thì nhớ `Xoá bộ lọc` trước.
- Sheet **chưa có phản hồi dev** (cột P/Q/R trống) cho case này — khác 4 case còn lại.

## File evidence + frame đã dùng

| Loại | Đường dẫn tuyệt đối |
|---|---|
| Video gốc | `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/partner-evidence/QLKTLBG_09_v2.webm` |
| Frame danh sách (baseline) | `…/frames/QLKTLBG_09/dense/t000.00s.jpg` |
| Frame tooltip "Xem trước" | `…/frames/QLKTLBG_09/dense/t003.10s.jpg` |
| Frame modal xem trước (không có viewer) | `…/frames/QLKTLBG_09/dense/t003.62s.jpg` |
| **Frame LỖI — hộp thoại Save As .pptx** | `…/frames/QLKTLBG_09/dense/t004.14s.jpg` (lặp lại ở `t004.65s`, `t005.17s`, `t005.68s`, `t006.19s`) |

*(Thư mục gốc frame: `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/frames/QLKTLBG_09/`)*

## Ngoài lỗi đối tác nêu, trong frame còn thấy gì bất thường? (dựa trên ảnh ĐÃ ĐỌC)

1. **Cột `Thao tác` (sticky bên phải) đè lên cột ngày.** Ở mọi frame danh sách, giá trị ngày chỉ đọc được `23/`, `30/(`, `04/(`, `25/(`, `08/(` — phần còn lại bị khối `Thao tác` che. Chính là lỗi "tràn/đè dữ liệu giữa các cột" mà bộ TC hay soi.
2. **Cột `Dung lượng` = `–` cho toàn bộ bản ghi loại `Video`** (`Test video 2`, `testvideo 1`, `sdsdsd`), trong khi Slide/PDF đều có số. Không rõ do chưa lưu dung lượng video hay do thiết kế.
3. **Modal "Xem trước" chỉ có 3 dòng metadata** (Công khai / Ảnh đại diện / Mô tả công khai) — **không hiển thị tên file, định dạng, dung lượng, lĩnh vực pháp lý, người tạo**. Với 1 màn tên là "Xem trước" thì lượng thông tin này rất mỏng; đáng để người verify đối chiếu SRS phần màn xem trước bài giảng.
4. Dữ liệu rác lẫn trong kho tài liệu môi trường UAT (`sdsdsdsss11`, `sdsdsd`, `testvideo 1`) — chỉ là data bẩn, không phải bug.

*(Tất cả đọc trực tiếp từ pixel frame, không suy đoán. Chưa log bug — thuộc quyền người verify.)*
