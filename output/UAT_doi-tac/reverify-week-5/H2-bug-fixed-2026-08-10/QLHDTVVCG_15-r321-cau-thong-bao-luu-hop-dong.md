# QLHDTVVCG_15 (sheet `bug` dòng 321) — Câu thông báo sau khi lưu hợp đồng

- Môi trường: https://18.143.165.120.nip.io — bản dựng **HTPLDN · V1.0.11**
- Tài khoản: `cbnv_tw_03` / `Test@1234` (CB Nghiệp vụ Trung ương, Cục Bổ trợ tư pháp - Bộ Tư pháp) — đúng Precondition
- Thời điểm: 2026-08-10 ~21:45–21:48
- Đường vào (đúng lối còn hiệu lực): Vụ việc HTPL → chi tiết `VV-BTP-TW-20260804-002` → mục **HĐ tư vấn liên kết** → **[+ Tạo hợp đồng]**
- Bản ghi dựng để đo: `HDTV-20260810-0002` — "Hợp đồng tư vấn kiểm tra câu thông báo lưu QA-R321-20260810"

## Làm đúng 5 bước trong ô "CÁCH VERIFY"

| Bước | Thao tác | Đo được |
|---|---|---|
| 1 | Nhập tên HĐ · bên B `Doanh nghiệp QA-R321-20260810` · giá trị `120.000.000` · thời gian 10/08/2026 → 31/12/2026 · TVV `TVV-BTP-TW-0002 — QA TVV Seed28 Active` → bấm **Thêm mới** | biểu mẫu nhận, không còn lỗi trường |
| 2 | Đọc TRỌN câu thông báo (MutationObserver cài TRƯỚC khi bấm, KHÔNG lọc trùng, đọc `innerText` + `innerHTML`) | **"Đã lưu hợp đồng"** — 1 toast (2 node wrapper + notice `ant-message-notice-success` cùng mốc ms, đúng cấu trúc AntD v5, không phải double toast) |
| 3 | Quan sát màn hình dừng ở đâu | hộp thoại đóng, URL vẫn `/vu-viec/6bf98a2e-…` — **quay về đúng mục HĐ tư vấn liên kết của vụ việc**, bảng tự tải lại (`GET /hop-dong-tu-vans?vuViecId=…` → 200) và hợp đồng mới nằm đầu bảng |
| 4 | Mở lại hợp đồng vừa tạo → **Sửa** (ô Ghi chú) → **Lưu**; làm 2 lượt | **"Đã lưu hợp đồng"** cả 2 lượt (mốc 1786373198622 và 1786373260304) — **CÙNG MỘT CÂU** với luồng thêm mới |
| 5 | Đọc mã + trạng thái | mã **`HDTV-20260810-0002`** đúng khuôn `HDTV-{YYYYMMDD}-{số thứ tự}`; trạng thái **"Đang thực hiện"** (`DANG_THUC_HIEN`) |

Phản hồi của chính lượt lưu (đọc trong trang, không dùng công cụ ngoài):
- Thêm mới: `POST /api/v1/hop-dong-tu-vans` → **201**, `maHopDong: "HDTV-20260810-0002"`, `trangThai: "DANG_THUC_HIEN"`, `soVuViecLienKet: 1`
- Chỉnh sửa: `PATCH /api/v1/hop-dong-tu-vans/9ac875a3-…` → **200**

## Chấm theo đúng mốc ✅ PASS trong ô Kết quả verify

| Việc | Yêu cầu | Đo được | Kết |
|---|---|---|---|
| (a) | Câu thông báo ở CẢ HAI luồng đều mang nghĩa "đã lưu hợp đồng", là MỘT câu dùng chung, không còn "Tạo… thành công" / "Cập nhật… thành công" | thêm mới = `Đã lưu hợp đồng`; sửa (2 lượt) = `Đã lưu hợp đồng`. Không xuất hiện chữ "thành công" ở bất kỳ lượt nào | ✅ |
| (b) | Sau khi lưu quay về đúng ngữ cảnh đã mở biểu mẫu | thêm mới → về mục HĐ tư vấn liên kết của `VV-BTP-TW-20260804-002`; sửa → về màn chi tiết hợp đồng (nơi mở biểu mẫu sửa), có nút "Quay lại" | ✅ |
| (c) | Mã đúng khuôn + trạng thái "Đang thực hiện" | `HDTV-20260810-0002` · "Đang thực hiện" | ✅ |

## Bẫy đã tôn trọng

- **Bẫy 1** — thanh bên KHÔNG có menu "Hợp đồng Tư vấn", vào bằng chi tiết vụ việc → KHÔNG log lại chuyện thiếu menu.
- **Bẫy 2** — KHÔNG chấm Fail vì "không quay về danh sách"; nhóm này không có màn danh sách độc lập.
- **Bẫy 3** — không bắt bẻ câu chữ từng ký tự; chỉ đòi MỘT câu dùng chung cho cả hai luồng — đã thoả.
- **Bẫy 4** — phần **tệp đính kèm** còn chờ BA nên KHÔNG chấm. Ghi lại quan sát trung tính: biểu mẫu tạo hiện dòng "Vui lòng lưu hợp đồng trước khi đính kèm tài liệu." ⇒ đính kèm là bước riêng sau khi sinh mã. Không kết luận đúng/sai.

## Ghi nhận thêm (không đổi verdict)

Nhãn nút submit khác nhau giữa 2 luồng: thêm mới = **[Thêm mới]**, sửa = **[Lưu]**. Đây là nhãn nút, không phải câu thông báo sau khi lưu — nằm ngoài phạm vi vấn đề BA chốt 06/08 (chỉ chốt câu thông báo).

## Bằng chứng

- [image/QLHDTVVCG_15-r321-toast-da-luu-hop-dong-luong-sua.png](image/QLHDTVVCG_15-r321-toast-da-luu-hop-dong-luong-sua.png) — bản ghi sau lượt sửa lần 1: mã, "Đang thực hiện", Ghi chú đã đổi
- [image/QLHDTVVCG_15-r321-toast-da-luu-hop-dong.png](image/QLHDTVVCG_15-r321-toast-da-luu-hop-dong.png) — sau lượt sửa lần 2 (Ghi chú "lan 2")
- [image/QLHDTVVCG_15-r321-hop-dong-moi-trong-muc-HD-tu-van-lien-ket.png](image/QLHDTVVCG_15-r321-hop-dong-moi-trong-muc-HD-tu-van-lien-ket.png) — hợp đồng mới nằm trong mục HĐ tư vấn liên kết của vụ việc (ngữ cảnh đã mở biểu mẫu)
- Câu toast tự tắt nhanh nên ảnh trượt 2 lượt; giữ bằng chứng bằng DOM bắt được (`innerText` + `innerHTML` có class `ant-message-notice-success`) và phản hồi 201/200 của chính lượt lưu.
