# Audit verify vòng 2 — QLGVTG_07 (row 22, tab tuần 2)

**Verdict:** `Open` · **Bug ID:** `BUG-QLGVTG_07` · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện (0 GAP):** [`../../cond/QLGVTG_07-r2.md`](../../cond/QLGVTG_07-r2.md)

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `QLGVTG_07_v2.jpg` (211.970 byte, ảnh tĩnh) |
| Nội dung lỗi thấy trong ảnh | Màn chi tiết giảng viên "Hoàng Minh Đức", breadcrumb dừng ở **"Chi tiết"** (chế độ Xem), nhưng tab "Thông tin" hiển thị **form nhập** — Họ và tên, Chuyên ngành, Trình độ, Tổ chức, Email, Điện thoại đều là ô nhập viền đầy đủ, có dấu `*` bắt buộc |
| Dữ kiện neo | (a) `htpldn-uat.ospgroup.vn/dao-tao/giang-vien/bc2ea722-eb29-4b46-b2a6-7afa55fcbf85` — **không** có `/chinh-sua` · (b) vai trò CB_NV_TW, đơn vị BTP·TW · (c) 2026-07-25 09:27 |

## Cổng 3 — đối chiếu SRS vs thực tế web (loại bug: Nghiệp vụ / phân tách chế độ màn hình)

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| `srs-fr-03-dao-tao.md:1924` — SCR-III-05 §Cột Hành động: "Xem (👁 — mở màn chi tiết 2 tab Thông tin + Lịch sử giảng dạy) · Sửa (✏) · Xóa (🗑)"; ghi chú nguồn: `[QLGVTG_07 UAT 2026-07-16 — bổ sung nút "Xem" riêng **cho nhất quán với các màn danh sách khác**]` ⇒ Xem và Sửa là hai hành động khác nhau, và chuẩn tham chiếu là các màn danh sách khác trong cùng phần mềm | Bấm 👁 Xem → màn "Chi tiết" mở **đúng form sửa**: 8 ô nhập + 1 ô mô tả đều mở khóa, có nút **Hủy** và **Lưu**. Bấm Lưu ghi thật vào máy chủ (`PATCH /api/v1/giang-viens/{id}`, toast "Cập nhật giảng viên thành công", dữ liệu đổi) ⇒ Xem và Sửa không khác nhau về khả năng ghi | **Thiếu** |
| `srs-fr-03-dao-tao.md:1926` — "Nhãn breadcrumb / tiêu đề màn theo chế độ: … khi **Xem** hiển thị 'Chi tiết'; khi **Sửa** hiển thị 'Chỉnh sửa' (**theo tiền lệ module Tư vấn viên**)" | Nhãn đúng (Chi tiết / Chỉnh sửa) nhưng **tiền lệ bị làm sai bản chất**: `srs-fr-04-chuyen-gia-tvv.md:1556` quy định tab "Hồ sơ" của màn chi tiết Tư vấn viên là "6 nhóm thu gọn được, **chỉ đọc**" | **Thiếu** |
| Chuẩn "nhất quán với các màn danh sách khác" (đo trực tiếp trên chính phần mềm, xem phép đo 5) | Màn Tư vấn viên: Xem → `/chuyen-gia-tvv/{id}`, breadcrumb "Chi tiết", **0 ô nhập / 0 ô mô tả**, có nút riêng "Sửa hồ sơ" để chuyển chế độ. Màn Giảng viên: cùng vị trí, **9 ô mở khóa + nút Lưu** | **Thiếu** |

⇒ **Quan sát của đối tác là ĐÚNG**, và không chỉ đúng ở mức hiển thị: chế độ Xem thực sự **ghi được dữ liệu**.

## Phép đo đã chạy (artifact QUAN SÁT trên data thật)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Mở màn chi tiết qua nút 👁 Xem — bản ghi `TS. Lê Hoàng Thái` (`f0fafafa-…-001`) | URL `/dao-tao/giang-vien/f0fafafa-…-001`, breadcrumb `… / Chi tiết`, tab `Thông tin` + `Lịch sử giảng dạy`; **10 ô nhập, tất cả `disabled=false`** (chỉ `trangThai` là `readOnly`); nút `Quay lại · Hủy · Lưu` | `BUG-QLGVTG_07-man-chi-tiet-sua-duoc.png` |
| 2 | Lặp lại trên bản ghi thứ 2 `QA GV QLGVTG09` (`fb261852-…`) để loại trừ yếu tố bản ghi | Giống hệt: breadcrumb `Chi tiết`, 8 ô nhập + 1 ô mô tả (`moTaNangLuc`) đều mở khóa, nút `Quay lại · Hủy · Lưu` | — |
| 3 | **Phép thử quyết định** — sửa ô "Chuyên ngành" ngay tại màn Xem rồi bấm **Lưu** (đo bằng `tools/toast-capture.js`, `soObserverDangSong=1`) | `SO_REQUEST=1` → `PATCH /api/v1/giang-viens/fb261852-…` · `SO_KHUNG_THONG_BAO=1` → chữ **"Cập nhật giảng viên thành công"** | log dưới đây |
| 4 | Đọc lại bản ghi sau khi Lưu để xác nhận dữ liệu đổi thật (không chỉ đổi trên màn) | `chuyenNganh` = `"Luat kinh te - QA sua tu man XEM"` ⇒ **ghi thật vào máy chủ từ chế độ Xem**. Đã khôi phục về `"Luật kinh tế"` ngay sau đó | log dưới đây |
| 5 | **Đối chứng nội bộ** — cùng phần mềm, mở màn chi tiết module Tư vấn viên (module mà SRS `:1926` chỉ định làm tiền lệ) bằng nút "Xem" | URL `/chuyen-gia-tvv/{id}`, breadcrumb `… / Chi tiết`, **soInput = 0, soTextarea = 0**, nút `Quay lại danh sách · Sửa hồ sơ · Cập nhật trạng thái · …` ⇒ chế độ Xem là chỉ đọc, muốn sửa phải bấm "Sửa hồ sơ" | `QLGVTG_07-r2-doi-chung-TVV-chi-doc.png` |
| 6 | Kiểm chế độ Sửa của chính màn Giảng viên có tồn tại riêng không | Có: `/dao-tao/giang-vien/{id}/chinh-sua`, breadcrumb `… / Chi tiết / Chỉnh sửa`, 9 ô nhập, nút `Quay lại · Hủy · Lưu` ⇒ hai chế độ **chỉ khác nhau ở đường dẫn và nhãn**, giống nhau về khả năng ghi | — |

**Log phép đo 3-4 (nguyên văn giá trị trả về):**

```
Phep do 3 — bam Luu tai man XEM:
{"giaTriTruoc":"Luật kinh tế","giaTriMoi":"Luat kinh te - QA sua tu man XEM",
 "SO_REQUEST":1,"request":["PATCH /api/v1/giang-viens/fb261852-2362-4f0a-a540-215596fd521f"],
 "SO_KHUNG_THONG_BAO":1,"chu":["Cập nhật giảng viên thành công"]}

Phep do 4 — doc lai ban ghi:
{"chuyenNganh_sauKhiLuuTuManXem":"Luat kinh te - QA sua tu man XEM"}
Sau khi khoi phuc: {"chuyenNganhHienTai":"Luật kinh tế"}
```

**Vì sao KHÔNG phải `Reject`:** đối tác quan sát đúng thực tế, tái hiện được 100% trên môi trường test với cùng vai trò và cùng chế độ màn hình. Không có dấu hiệu thao tác sai (URL trong ảnh không có `/chinh-sua` ⇒ họ không vô tình mở chế độ Sửa).

**Vì sao KHÔNG phải `BA confirm`:** ban đầu tôi nghiêng về `BA confirm` vì SRS không có câu chữ trực tiếp "màn Xem phải chỉ đọc". Nhưng phép đo 5 lật lại kết luận đó: SRS `:1924` nêu rõ mục đích của nút 👁 là **"cho nhất quán với các màn danh sách khác"**, `:1926` chỉ định **tiền lệ là module Tư vấn viên**, và `srs-fr-04-chuyen-gia-tvv.md:1556` quy định màn chi tiết TVV **chỉ đọc** — chuẩn này đã được chính phần mềm hiện thực đúng ở module TVV. Có chuẩn SRS, có mốc so sánh trong cùng sản phẩm, và web lệch khỏi cả hai ⇒ đủ căn cứ `Open`.

## Ngoài tiêu chí BA — có thấy gì bất thường không?

**Có, 1 điểm đã gộp vào cùng bug entry vì cùng một thao tác:** chế độ Xem không chỉ *nhìn như* form sửa mà **ghi được thật** — người chỉ định xem hồ sơ có thể vô tình sửa và lưu đè dữ liệu giảng viên. Đây là phần nghiêm trọng hơn hẳn so với claim ban đầu của đối tác (họ mới dừng ở mức "cho phép chỉnh sửa" trên giao diện).

**Điểm thứ hai, chưa đủ căn cứ log bug riêng:** `PATCH /api/v1/giang-viens/{id}` gọi trực tiếp (ngoài giao diện) trả **422** khi thân yêu cầu chỉ có trường cần đổi — nhiều khả năng thiếu trường `version` (khóa chống ghi đè đồng thời), giống các module khác. Chỉ ghi nhận, không log vì đây là cách gọi ngoài luồng người dùng.

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- **Dữ liệu test đã khôi phục:** bản ghi `QA GV QLGVTG09` (`fb261852-…`) từng bị đổi `chuyenNganh` trong phép đo 3, đã trả về `"Luật kinh tế"` và xác nhận lại bằng phép đọc — không để lại rác dữ liệu.
- **Đường dẫn danh sách TVV:** menu "Tư vấn viên / Chuyên gia" trỏ tới `/chuyen-gia-tvv/danh-sach`; các đường đoán `/mang-luoi/tu-van-vien/danh-sach` trả 404. Ghi lại để lần sau khỏi dò.
- **Phiên đăng nhập bị đá về `/login`** thêm 1 lần nữa trong lúc thao tác (không idle), `GET /api/v1/auth/me` → 401. Tổng cộng đã gặp ~4 lần trong đợt verify này. Chưa đủ căn cứ kết luận là lỗi sản phẩm hay nhiễu môi trường/công cụ — ghi nhận để theo dõi tần suất.
