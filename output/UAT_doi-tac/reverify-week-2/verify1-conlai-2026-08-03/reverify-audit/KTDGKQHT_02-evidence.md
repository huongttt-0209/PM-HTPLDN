# KTDGKQHT_02 — Cổng 1 + Cổng 2 (AGENT-EVIDENCE, 2026-08-03)

> Sheet: `UAT_TGPL Doanh Nghiệp-tuần 2` row **116** · `fetch_evidence.py` **exit 0** (2 link Drive, tải được cả 2 file).
> Ô "Ảnh/video 2" (cột T) **trống** — chỉ có evidence vòng 1.

## Cổng 1 — 3 dữ kiện neo

**(a) URL / mã bản ghi đối tác đang đứng**
- Ảnh 1: `htpldn-uat.ospgroup.vn/dao-tao/khoa-hoc/0362c6e3-1968-4644-9001-d24b267e6b21?tab=lich-hoc-diem-danh`
- Ảnh 2: `htpldn-uat.ospgroup.vn/dao-tao/khoa-hoc/0362c6e3-1968-4644-9001-d24b267e6b21?tab=ket-qua-kiem-tra`
- Cùng **một khoá học**, id `0362c6e3-1968-4644-9001-d24b267e6b21`. Màn: Đào tạo, tập huấn → Khoá học → Chi tiết.
- **Tên/mã khoá học: KHÔNG ĐỌC ĐƯỢC** — cả 2 ảnh đối tác chụp ở tab con, không có tiêu đề khoá học trong khung hình.

**(b) Trạng thái entity**
- Stepper khoá học: `✓ Dự thảo — ✓ Chờ duyệt — ✓ Đã duyệt — **(4) Đang diễn ra** — 5 Đã kết thúc — 6 Chờ duyệt KQ — 7 Hoàn thành`.
- Đang ở bước **4 · Đang diễn ra**.
- Tab "Kết quả" có banner vàng: *"Kết quả tạm tính — Khoá học đang diễn ra — kết quả bên dưới là tạm tính, chưa phải kết quả chính thức. Kết quả được chốt khi trình phê duyệt."*

**(c) Dữ liệu tiền đề**
- Khoá học có **1 học viên**: `Hoàng Minh Đức` · `hoangminhduc@g…` · `0105545484`.
- Tab Điểm danh: buổi học đang chọn = `15/07/2026 · 14:00:00-15:00:00`; học viên được chấm **"Vắng có phép"** (nút đang active), ô "Lý do vắng…" để trống. Nút màn: `Lưu điểm danh`, `Import Excel`, `Xuất Excel`, `Công khai`, `Kết thúc`.
- Tab Kết quả: `Chuyên cần = 0/3 (33.33%)`, `Điểm kiểm tra = 10.0` (ô input), `Kết quả = Không đạt` (tag đỏ), `Xếp loại = Giỏi`, `Đơn vị = Cục Bổ trợ tư ph…`. Nút màn: `Lưu kết quả` (disabled), `Xuất DOCX`, ô tìm theo tên học viên, dropdown lọc `Kết quả`.
- Con số `0/3` cho thấy khoá có **3 buổi** trong lịch học.

## Cổng 2 — 3 dòng

**(1) Evidence đã xem + frame chứa LỖI**
`partner-evidence/KTDGKQHT_02_v2-2.jpg` (ảnh tĩnh full-res 1915×1036, chụp 05:02 PM 2026-07-24) — **đây là ảnh chứa lỗi**. Bảng tab "Kết quả" chỉ có đúng 9 cột `STT · Họ tên · Email · Số điện thoại · Đơn vị · Chuyên cần · Điểm kiểm tra · Kết quả · Xếp loại`; **không có** cột nào tên "Số buổi có mặt" / "Số buổi vắng có phép" / "Số buổi vắng không phép" / "Tổng số buổi" — thông tin chuyên cần bị gộp thành 1 ô `0/3 (33.33%)`.
Ảnh phụ `KTDGKQHT_02_v2-1.jpg` (05:01 PM 2026-07-24) là tab "Điểm danh" cùng khoá học, dùng để đối chiếu.

**(2) Đối tác phản ánh CỤ THỂ gì**
Tab **"Kết quả kiểm tra"** của màn Chi tiết khoá học **thiếu 4 trường**: `Số buổi có mặt`, `Số buổi vắng có phép`, `Số buổi vắng không phép`, `Tổng số buổi`. Đối tác **không** phàn nàn về sai số liệu hay tràn cột — chỉ là **thiếu trường hiển thị**. (Kết quả mong đợi ghi ở sheet: "Dữ liệu hiển thị đúng với trường thông tin và định dạng… không bị tràn/đè dữ liệu giữa các cột… đồng bộ căn lề".)

**(3) Data + bước tái hiện chính xác**
1. Đăng nhập vai trò **Cán bộ nghiệp vụ Trung ương** (`CB_NV_TW`, đơn vị `BTP · TW`).
2. Menu `Đào tạo, tập huấn` → `Khoá học`.
3. Mở chi tiết một khoá học đang ở state **Đang diễn ra**, có **≥1 học viên** và **≥3 buổi trong lịch học**, đã điểm danh ít nhất 1 buổi (đối tác chấm "Vắng có phép" buổi 15/07/2026 14:00–15:00).
4. Mở tab `Điểm danh` (URL `?tab=lich-hoc-diem-danh`) → sau đó tab `Kết quả` (URL `?tab=ket-qua-kiem-tra`).
5. Đọc danh sách cột của bảng ở tab Kết quả, **kéo hết thanh cuộn ngang** rồi đối chiếu với 4 trường đối tác nêu.

## Vai trò / tài khoản đối tác dùng

`Cán bộ NV Trung ương` — mã hiển thị **`CB_NV_TW`**, đơn vị **`BTP · TW`** (đọc từ header phải cả 2 ảnh). Badge thông báo `99+`. Tài khoản tương ứng trong sheet: nhóm `cbnv_tw`.

## Ghi chú cho người verify

- **Tiền đề bắt buộc dựng lại:** khoá học **state `Đang diễn ra`** (không phải `Đã kết thúc`/`Hoàn thành`) + có học viên + lịch học ≥3 buổi + đã điểm danh ≥1 buổi. Đứng ở state khác thì tab Kết quả đổi banner (hết "Kết quả tạm tính") và **có thể đổi bộ cột** → verify sai điều kiện.
- **Cẩn thận nhãn tab:** UI hiển thị tab tên **"Kết quả"**, còn tham số URL là `ket-qua-kiem-tra`. Đối tác + sheet gọi là "Kết quả kiểm tra". Cùng 1 tab, đừng nhầm sang tab khác.
- **Phản hồi dev (đã ghi ở sheet, cột R) khẳng định 4 cột đó "thuộc Tab Điểm danh".** Ảnh `KTDGKQHT_02_v2-1.jpg` của chính đối tác cho thấy tab Điểm danh chỉ có `STT · Họ tên · Email · Số điện thoại · Đơn vị · Trạng thái · Ghi chú` — **cũng không có 4 cột đó**; thanh cuộn ngang ở tab này gần như full width nên khả năng cột bị ẩn là rất thấp. Người verify nên **kiểm cả 2 tab + kéo hết cuộn ngang** rồi mới đối chiếu SRS (SCR-III-02 / phần màn hình chi tiết khoá học).
- Đây là **bug hiển thị (bug tĩnh)** — đối tác không tranh chấp state machine, nên trọng tâm verify là danh sách cột SRS vs web.

## File evidence + frame đã dùng

| Loại | Đường dẫn tuyệt đối |
|---|---|
| Ảnh gốc 1 (tab Điểm danh) | `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/partner-evidence/KTDGKQHT_02_v2-1.jpg` |
| Ảnh gốc 2 (tab Kết quả — **ảnh lỗi**) | `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/partner-evidence/KTDGKQHT_02_v2-2.jpg` |
| Crop bảng tab Kết quả (zoom ×2) | `…/verify1-conlai-2026-08-03/frames/KTDGKQHT_02/crop-ketqua-table.png` |
| Crop bảng tab Điểm danh (zoom ×2) | `…/verify1-conlai-2026-08-03/frames/KTDGKQHT_02/crop-diemdanh-table.png` |
| Crop header user (zoom ×3) | `…/verify1-conlai-2026-08-03/frames/KTDGKQHT_02/crop-user.png` |

## Ngoài lỗi đối tác nêu, trong ảnh còn thấy gì bất thường? (dựa trên ảnh ĐÃ ĐỌC)

1. **`Chuyên cần = 0/3 (33.33%)` — tử số và phần trăm mâu thuẫn.** 0/3 phải là 0%, không phải 33.33% (33.33% ứng với 1/3). Đọc rõ ở crop `crop-ketqua-table.png`.
2. **`Kết quả = Không đạt` (tag đỏ) nhưng `Xếp loại = Giỏi`** trên cùng 1 dòng học viên, với `Điểm kiểm tra = 10.0`. Hai ô này nghịch nhau.
3. **Cột `Đơn vị` trống ở tab Điểm danh** nhưng cùng học viên đó lại có `Cục Bổ trợ tư ph…` ở tab Kết quả — không đồng bộ dữ liệu giữa 2 tab (liên quan trực tiếp tới Kết quả mong đợi "dữ liệu đồng nhất" của chính TC này).
4. Tab Kết quả có ô nhập `Điểm kiểm tra` sửa được (10.0) trong khi banner ghi "kết quả là tạm tính, chốt khi trình phê duyệt" — nút `Lưu kết quả` lại đang **disabled** (xám). Không rõ có phải trạng thái mong muốn không.

*(Cả 4 điểm đều đọc trực tiếp từ pixel ảnh, không suy đoán. Chưa log bug — thuộc quyền người verify.)*
