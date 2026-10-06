# QLTVV_02 (sheet `bug` dòng 32) — Thứ tự mặc định danh sách Tư vấn viên / Chuyên gia

- Môi trường: https://htpldn-uat.ospgroup.vn — bản dựng **HTPLDN · V1.0.11**
- Tài khoản: **`cbnv_tw` / `Test@1234`** (Cán bộ Nghiệp vụ Trung ương) — đúng Precondition của tiêu chí
- Thời điểm: 2026-08-11 ~10:00 – 10:06
- Đường vào: Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia, tab **"Đang hoạt động"**. KHÔNG đụng bộ lọc, KHÔNG bấm tiêu đề cột.

## Làm đúng 4 bước trong ô "CÁCH VERIFY"

| Bước | Thao tác | Đo được |
|---|---|---|
| 1 | Mở danh sách ở trạng thái mặc định, ghi thứ tự mã TVV trang 1 | 11 bản ghi ("1-11 / 11 mục"), thứ tự ban đầu: `0030 · 0063 · 0034 · MOCK-999 · 0029 · HDSD-AG-01 · 0032 · 0035 · 0006 · 0002` và `0004` ở **cuối** |
| 2 | Đọc ngày cập nhật từng dòng | Mở lần lượt từng hồ sơ trong chính phiên đang đăng nhập; xem bảng dưới |
| 3 | Chọn hồ sơ đang nằm CUỐI trang 1 → sửa một trường vô hại → Lưu | `TVV-BTP-TW-0004`, "Sửa hồ sơ" → ô "Thông tin bổ sung" → **Lưu** → thông báo "Cập nhật hồ sơ TVV thành công", `PATCH /api/v1/tu-van-viens/5775298e-…` → **200** |
| 4 | Quay lại danh sách, tải lại, KHÔNG đụng bộ lọc | `TVV-BTP-TW-0004` lên **dòng 1**; thứ tự trên giao diện trùng khít thứ tự dữ liệu |

## Thứ tự sau bước 4 và ngày cập nhật tương ứng

| # | Mã TVV | Ngày cập nhật | Ngày tạo | Ngày công nhận |
|---|---|---|---|---|
| 1 | TVV-BTP-TW-0004 | **2026-08-11 03:01:30** | 2026-05-06 | 06/05/2026 |
| 2 | TVV-BTP-TW-0030 | 2026-08-08 02:11:17 | 2026-05-08 | 08/05/2026 |
| 3 | TVV-BTP-TW-0063 | 2026-08-07 11:55:35 | **2026-08-03** | 03/08/2026 |
| 4 | TVV-BTP-TW-0034 | 2026-08-04 11:03:11 | 2026-05-09 | 09/05/2026 |
| 5 | TVV-MOCK-999 | 2026-07-29 09:01:08 | 2026-06-29 | — |
| 6 | TVV-BTP-TW-0029 | 2026-07-25 10:35:49 | 2026-05-08 | 09/05/2026 |
| 7 | TVV-HDSD-AG-01 | 2026-07-08 08:49:10 | 2026-05-12 | **2024-09-01** |
| 8 | TVV-BTP-TW-0032 | 2026-07-07 07:27:06 | 2026-05-08 | 08/05/2026 |
| 9 | TVV-BTP-TW-0035 | 2026-05-25 16:25:38 | 2026-05-09 | 09/05/2026 |
| 10 | TVV-BTP-TW-0006 | 2026-05-07 17:05:43 | 2026-05-06 | 06/05/2026 |
| 11 | TVV-BTP-TW-0002 | 2026-05-07 11:54:37 | 2026-05-06 | 06/05/2026 |

## Chấm theo đúng mốc ✅ PASS trong ô Kết quả verify

| Việc | Yêu cầu | Đo được | Kết |
|---|---|---|---|
| (a) | Thứ tự trang 1 giảm dần theo ngày cập nhật, không dòng nào mới hơn dòng trên nó | Kiểm từng cặp liền kề: **0 vi phạm**. Cũng không phải sắp theo ngày tạo (0063 tạo mới nhất 03/08 nhưng đứng thứ 3) và không phải theo ngày công nhận (HDSD-AG-01 công nhận 2024 đứng thứ 7, còn 0004 công nhận 06/05/2026 đứng thứ 1) | ✅ |
| (b) | Sau bước 3, hồ sơ vừa sửa nhảy lên DÒNG ĐẦU TIÊN | `TVV-BTP-TW-0004` từ cuối trang lên **dòng 1** ngay sau khi lưu | ✅ |
| (c) | Mặc định vẫn đúng 20 bản ghi/trang | Ô chọn số dòng hiện **"20 / trang"**, chân bảng "1-11 / 11 mục" | ✅ |

## Bẫy đã tôn trọng

- **Bẫy 1** — KHÔNG chấm theo "ngày công nhận". Bảng trên cho thấy nếu sắp theo ngày công nhận thì HDSD-AG-01 (2024) phải nằm cuối, thực tế nó ở giữa ⇒ phần mềm không sắp theo cột đó.
- **Bẫy 2** — không có hồ sơ nào "chưa từng cập nhật" trong 11 bản ghi (mọi bản ghi đều có ngày cập nhật), nên không phát sinh nhóm xen kẽ theo ngày tạo.
- **Bẫy 3** — chỉ chấm vế thứ tự sắp xếp; bốn vế đã đóng ở lượt 06/08 không mở lại.

## Bằng chứng

- [image/QLTVV_02-r32-uat-ban-ghi-vua-sua-len-dong-1-20-tren-trang.png](image/QLTVV_02-r32-uat-ban-ghi-vua-sua-len-dong-1-20-tren-trang.png) — `TVV-BTP-TW-0004` ở dòng 1, ô "20 / trang", "1-11 / 11 mục"
- Danh sách trên giao diện KHÔNG có cột "Ngày cập nhật" (chỉ có "Ngày công nhận"), nên ngày cập nhật phải đọc từ dữ liệu của chính phiên đang đăng nhập — đó là đúng cách tiêu chí bước 2 cho phép ("lấy ở phản hồi của lượt tải danh sách, hoặc mở lần lượt hồ sơ để đối chiếu").
