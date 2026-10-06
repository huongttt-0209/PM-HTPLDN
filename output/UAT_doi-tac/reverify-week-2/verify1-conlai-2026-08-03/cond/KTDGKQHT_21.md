# Bảng đối chiếu điều kiện — KTDGKQHT_21

> Lỗi do QA tự phát hiện khi verify KTDGKQHT_02 ngày 03/08/2026 (không có phản ánh đối tác) → cột giữa ghi **điều kiện lúc phát hiện lỗi**, không phải điều kiện đối tác.
> Nghi vấn khi phát hiện: *"cột Đề kiểm tra có thể chỉ render khi khóa học ĐÃ được gán đề"* — vòng đo này dựng đúng tiền đề đó để loại trừ.

| Điều kiện có thể đổi kết quả | Điều kiện khi phát hiện lỗi | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ đúng đơn vị khóa học (`CB_NV_TW`, Cục Bổ trợ tư pháp, `donViId 00000000-0000-4000-8000-000000000001`) | Chính vai trò + đơn vị đó — `cbnv_tw_05` (`cbnv_tw` bị phiên QA khác đăng nhập chiếm, fallback đúng Rule 7: cùng vai trò `CB_NV_TW` + cùng đơn vị TW) | Không |
| Entity + trạng thái | Khóa học ở trạng thái cho hiển thị bảng kết quả (`DANG_DIEN_RA` hoặc `DA_KET_THUC` trở đi — PRE-04 FR-III-05, `srs-fr-03-dao-tao.md:534`) | Đo trên **2 khóa, 2 trạng thái khác nhau**: `KH-QAW7-HOINGHI` (Đang diễn ra) và `AAA-KH-TW` (Hoàn thành) | Không |
| Dữ liệu tiền đề — **khóa ĐÃ gán đề kiểm tra** (đây chính là GAP của lần đo trước) | Lần đo trước: cả 3 khóa **chưa** gán đề → chưa loại trừ được "cột render có điều kiện" | Đã tạo đề `QA-DEKT-0803` (trạng thái **Kích hoạt**) và **gán vào cả 2 khóa** qua Tab "Đề kiểm tra"; đo lại cột ở cả 2 khóa **trước** và **sau** khi gán | Không |
| Dữ liệu tiền đề — **bản ghi kết quả đã trỏ tới đề** | Chưa kiểm | Đã nhập điểm 9.0 / 4.0 trên `KH-QAW7-HOINGHI` sau khi gán đề → máy chủ trả `tenDeKiemTra = "QA-DEKT-0803 — Đề kiểm tra pháp lý DN (QA seed 03/08)"` cho cả 2 bản ghi; đo lại cột lần nữa | Không |
| Input / filter | Không có bộ lọc — chỉ mở tab và đọc tiêu đề cột | Như vậy; thêm thao tác **cuộn ngang hết cỡ** để loại trừ cột bị che | Không |

**Kết luận: 0 GAP.**

**Ba phương pháp đo độc lập, khớp nhau:**
1. Đọc DOM tiêu đề cột kèm kiểm node ẩn (`display:none` / `offsetWidth === 0`) và số phần tử `<colgroup><col>` → **10 cột, 0 cột ẩn, colgroup = 10** ở mọi lần đo.
2. Ảnh chụp full-res sau khi **cuộn ngang hết cỡ sang phải** — nhìn tận mắt nhóm cột cuối: `Email · Số điện thoại · Đơn vị · Chuyên cần · Điểm kiểm tra · Kết quả · Xếp loại · Ghi chú`, không có cột nào tên "Đề kiểm tra".
3. Đối chứng dương tính trên **cùng bản dựng, cùng khóa học**: tab "Công bố kết quả" **CÓ** cột "Đề kiểm tra" và hiển thị đúng tên đề vừa gán ⇒ dữ liệu đề đã tới giao diện, chỉ riêng tab "Kết quả" không dựng cột.

**Loại trừ giả thuyết "render có điều kiện":** cột `Đề kiểm tra` **không xuất hiện** ở cả 4 tình huống — (a) khóa chưa gán đề, (b) khóa đã gán đề, (c) khóa đã gán đề + bản ghi kết quả đã trỏ tới đề, (d) hai trạng thái khóa khác nhau. Máy chủ có trả trường `tenDeKiemTra` trong `GET /api/v1/khoa-hocs/{id}/ket-quas`.

**Phạm vi cố ý loại khỏi lỗi này:** cột **"Chuyên cần"** mà bản dựng thêm vào tab (SRS `:1901` không liệt kê) **KHÔNG** tính là lỗi ở dòng này — việc gộp `số buổi có mặt / tổng buổi (tỷ lệ %)` vào một ô đang là **câu hỏi chờ BA** ở dòng 116 `KTDGKQHT_02`. Không log trùng.
