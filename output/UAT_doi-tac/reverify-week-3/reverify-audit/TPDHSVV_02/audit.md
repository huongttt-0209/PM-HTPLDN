# Audit — TPDHSVV_02 (row 4) · Trình phê duyệt khi chưa có kết quả hỗ trợ — "thông báo duplicate"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File: `partner-evidence/TPDHSVV_02.jpg` (275 KB, `fetch_evidence.py --row 4` exit 0). 1 ảnh chụp màn.
- Frame chứa LỖI đối tác báo: chính ảnh này — **2 khung thông báo** "ERR-VAL-VI-TD-02: Chưa có kết quả xử lý từ tư vấn viên" chồng nhau ở góc trên.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị đọc từ ảnh |
|---|---|---|
| (a) | URL / ID vụ việc | `htpldn-uat.ospgroup.vn/vu-viec/9ed9d021-f308-40cc-b4d7-b60b80fbc1dd` — **VV-BTP-TW-20260709-001**, "Đang xử lý", "Còn 15 ngày LV", lĩnh vực Thuế |
| (b) | Trạng thái + hiện tượng | Vụ việc **Đang xử lý** (stepper "Đang xử lý" active), có nút [Cập nhật kết quả] [Trình phê duyệt]. **2 toast lỗi** "ERR-VAL-VI-TD-02: Chưa có kết quả xử lý từ tư vấn viên" xếp chồng |
| (c) | Vai trò người thao tác | Header: **Cán bộ NV Trung ương · CB_NV_TW** · BTP·TW · chuông 96 |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `TPDHSVV_02.jpg` — CB_NV_TW đứng ở vụ việc VV-BTP-TW-20260709-001 (Đang xử lý, chưa có kết quả hỗ trợ), sau khi bấm Trình phê duyệt hiện **2 khung thông báo lỗi giống hệt nhau** "Chưa có kết quả xử lý từ tư vấn viên".
2. **Đối tác phản ánh CỤ THỂ (cột "Kết quả thực tế"):** "**Thông báo bị duplicate**". Tức: hệ thống chặn đúng (không cho trình phê duyệt khi chưa có kết quả) nhưng **thông báo hiện 2 lần**. KQ mong đợi của đối tác: chỉ 1 thông báo.
3. **Data + bước tái hiện:** login CB_NV_TW → Vụ việc HTPL → mở vụ việc "Đang xử lý" **chưa có kết quả hỗ trợ** → bấm [Trình phê duyệt] → xác nhận → quan sát số thông báo.

## Bảng đối chiếu điều kiện

→ [`../../cond/TPDHSVV_02.md`](../../cond/TPDHSVV_02.md) — **0 GAP**.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

Tài khoản `cbnv_tw` (CB_NV_TW, BTP·TW — đúng người tiếp nhận hồ sơ), vụ việc **VV-BTP-TW-20260712-001** ở trạng thái **Đang xử lý**, **chưa có kết quả hỗ trợ** (`coKetQua=false`, nhóm "Kết quả hỗ trợ" hiện "Tư vấn viên chưa cập nhật kết quả").

### Phép đo — 4 lần chạy (tools/toast-capture.js, không lọc trùng, innerText, tự kiểm observer=1)

| Lần | SO_REQUEST | request | SO_KHUNG_THONG_BAO | Nội dung thông báo | BI_LAP |
|:-:|:-:|---|:-:|---|:-:|
| 1 | 1 | `POST .../trinh-phe-duyet` | **1** | "ERR-VAL-VI-TD-02: Chưa có kết quả xử lý từ tư vấn viên" | false |
| 2 | 1 | `POST .../trinh-phe-duyet` | **1** | (như trên) | false |
| 3 | 1 | `POST .../trinh-phe-duyet` | **1** | (như trên) | false |
| 4 | 1 | `POST .../trinh-phe-duyet` | **1** | (như trên) | false |

**Đếm DOM trực tiếp `.ant-message-notice-wrapper` suốt vòng đời toast** (lần 3), tại 7 mốc 150 / 300 / 500 / 800 / 1200 / 1800 / 2600 ms → **tất cả = 1**. Tức không có thời điểm nào tồn tại 2 khung thông báo cùng lúc.

Tự kiểm bộ đo: `soObserverDangSong = 1` (chèn node giả, đếm đúng 1 lần) → số liệu hợp lệ, không bị nhân bản observer.

**Kết luận đo:** máy chủ được gọi đúng 1 lần, hệ thống hiển thị đúng **1 thông báo duy nhất** — **KHÔNG nhân đôi**. Vụ việc giữ nguyên "Đang xử lý" (chặn trình phê duyệt đúng vì chưa có kết quả).

Ảnh: `toast-single.png` — vụ việc sau thao tác vẫn "Đang xử lý", nhóm "Kết quả hỗ trợ" = "Tư vấn viên chưa cập nhật kết quả" (chặn đúng).

> Ghi chú kỹ thuật: trên env này khung thông báo render sát mép trên viewport (`getBoundingClientRect().top ≈ -32`, chỉ ~8px lọt vào vùng nhìn) nên ảnh chụp không bắt trọn toast; số liệu tin cậy lấy từ observer + đếm DOM (chuẩn theo `tools/toast-capture.js`), không phụ thuộc ảnh.

## Verdict

**`Open`** — verdict đổi từ `Reject` → `Open` (cập nhật 2026-07-20 theo chỉ đạo: chính toast đối tác báo đang lộ mã lỗi kỹ thuật = bug thật, phải log + chuyển dev, KHÔNG để Reject).

- **Ý đối tác báo "thông báo nhân đôi / duplicate" — KHÔNG tái hiện:** đúng vai trò (CB_NV_TW), đúng trạng thái (Đang xử lý), đúng tiền đề (chưa có kết quả), hệ thống chặn đúng và chỉ hiển thị **1 thông báo duy nhất** (đo lặp 4 lần + đếm DOM 7 mốc). Ghi rõ để dev **không phải sửa** phần "nhân đôi".
- **NHƯNG chính thông báo đó lộ mã lỗi kỹ thuật ra người dùng** — nguyên văn "**ERR-VAL-VI-TD-02:** Chưa có kết quả xử lý từ tư vấn viên". Vi phạm quy tắc hệ thống: thông báo (toast) chỉ hiển thị nội dung văn bản dễ hiểu, **KHÔNG kèm mã lỗi** — quy tắc do product owner xác nhận 2026-07-20, **áp dụng toàn hệ thống**. → Lỗi thật trên chính thao tác/màn hình đối tác báo → `Open`.
- Bug: `BUG-VV-MALOI-LO-UI` → [`../../bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md`](../../bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md). Đề nghị dev bỏ tiền tố mã lỗi khỏi mọi thông báo hiển thị cho người dùng.

## Bất thường ngoài tiêu chí BA (postmortem 16/07 mục C1)

- **🔴 Đã log bug riêng — `BUG-VV-MALOI-LO-UI` (Minor):** thông báo hiển thị cho người dùng bị **lẫn mã lỗi kỹ thuật nội bộ** ở đầu câu — nguyên văn "**ERR-VAL-VI-TD-02:** Chưa có kết quả xử lý từ tư vấn viên". Theo cách SRS đặc tả mọi thông báo (cột "Message" các bảng Error Handling), người dùng chỉ nên thấy câu dễ hiểu, không kèm mã. Hiện tượng có tính hệ thống (cũng gặp `ERR-AUTH-VPD-00-04` ở màn 403 case XNTGHTVV_03). Xác nhận DOM 6 lần + `outerHTML`; ảnh `../../bug-reports/image/BUG-VV-MALOI-LO-UI-toast-ma-loi.png` (freeze node do ứng dụng render vì toast tự tắt trước khi MCP chụp kịp). → **Cập nhật 2026-07-20:** lỗi lộ mã lỗi này chính là căn cứ để đổi verdict TPDHSVV_02 thành `Open` (product owner xác nhận quy tắc "toast chỉ hiển thị text, không kèm mã lỗi" áp dụng toàn hệ thống). Khiếu nại "nhân đôi" của đối tác vẫn KHÔNG tái hiện, nhưng thao tác này có bug thật khác (lộ mã lỗi) → không còn là `Reject`.
- **Vị trí toast:** đo lại rõ — khung thông báo trượt vào từ trên (`top≈-32` lúc animation) rồi **dừng ở `top:8, bottom:64` (hiển thị đầy đủ)**. Vậy KHÔNG có lỗi "toast bị che" như nghi ban đầu; ghi chú "-32" trước đây chỉ là khung hình giữa animation. Ảnh chụp bị trễ so với vòng đời toast là do độ trễ công cụ MCP, không phải app.
- Ngoài mã lỗi lộ ra, chức năng chặn trình phê duyệt khi chưa có kết quả hoạt động đúng (không cho chuyển trạng thái, giữ "Đang xử lý").
