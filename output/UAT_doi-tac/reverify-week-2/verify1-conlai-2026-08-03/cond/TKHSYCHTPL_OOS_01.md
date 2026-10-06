# Bảng đối chiếu điều kiện — TKHSYCHTPL_OOS_01 (row 145, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Danh sách hồ sơ vụ việc — cột "Cảnh báo thời hạn" + bộ lọc "Mức SLA" — FR-V.I-08 (UC58), màn SCR-V.I-01; quy tắc liên quan FR-V.I-CROSS-01 + BR-CALC-03
**Loại bug:** bug HIỂN THỊ phụ thuộc trạng thái entity + giá trị lọc → BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG)
**Verdict:** `BA confirm` — đặc tả silent, không trích được điều khoản bị vi phạm
**Ngày verify:** 2026-08-03 · **Tài khoản QA dùng:** `cbnv_tw_03` (CB_NV_TW, đơn vị BTP · TW, bản dựng `HTPLDN · V1.0.5`), đăng nhập lần đầu OK, không phải fallback

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Không áp dụng — lỗi do QA phát hiện ngoài phạm vi case, không có evidence đối tác | `cbnv_tw_03` — nhãn góc phải "CB Nghiệp vụ - Trung ương #03 · CB_NV_TW", đơn vị "BTP · TW" (đọc từ ảnh `image/BUG-TKHSYCHTPL_OOS_01-cot-canh-bao-thoi-han-hien-da-hoan-thanh.png`) | Không |
| Màn hình + tab đang đứng | Không áp dụng — lỗi do QA phát hiện ngoài phạm vi case, không có evidence đối tác | Màn "Vụ việc HTPL / Danh sách" (`/vu-viec/danh-sach?mucSla=SAP_HET&page=1`), tab **Tất cả** đang chọn | Không |
| Entity + **trạng thái** (state machine) | Không áp dụng — lỗi do QA phát hiện ngoài phạm vi case, không có evidence đối tác | 2 hồ sơ đều ở trạng thái KẾT THÚC: `VV-BTP-TW-20260712-006` = "Từ chối" (`TU_CHOI`), `VV-BTP-TW-20260712-005` = "Hoàn thành" (`HOAN_THANH`) — đọc 2 chiều: cột "Trạng thái" trên ảnh + `trangThai` trong dữ liệu danh sách trả về | Không |
| Dữ liệu tiền đề (mốc thời hạn so với ngày kiểm) | Không áp dụng — lỗi do QA phát hiện ngoài phạm vi case, không có evidence đối tác | Cả 2 hồ sơ: ngày tiếp nhận 12/07/2026, thời hạn xử lý 31/07/2026 — **đã trôi qua** so với ngày kiểm 03/08/2026. Lần cập nhật cuối dừng ở 29/07/2026 (`-006`) và 24/07/2026 (`-005`), tức trước cả mốc thời hạn | Không |
| Input / filter / giá trị nhập | Không áp dụng — lỗi do QA phát hiện ngoài phạm vi case, không có evidence đối tác | Ô từ khóa **trống** · Lĩnh vực PL **trống** · Đơn vị **trống** · Kênh tiếp nhận **trống** · **Mức SLA = "Sắp hết hạn"** · "Bộ lọc nâng cao (3)" để nguyên mặc định | Không |

## Ghi chú đóng GAP

- **Ô "Đối tác" không áp dụng cho mọi dòng:** đây là lỗi tổ kiểm thử tự phát hiện khi verify case `TKHSYCHTPL_03` ngày 03/08/2026, KHÔNG bắt nguồn từ phiếu đối tác nên không có evidence đối tác để đối chiếu. Vì vậy không tồn tại khái niệm "lệch điều kiện với đối tác" ở dòng nào → mọi ô GAP = **Không**.
- **Tiền đề tạo được đều đã có sẵn, không phải seed:** 2 hồ sơ ở trạng thái kết thúc + thời hạn đã qua vốn có sẵn trong dữ liệu môi trường, đúng tổ hợp cần để quan sát hiện tượng. Không có tiền đề nào bị bỏ qua bằng lập luận.
- **Đo bằng 2 phương pháp độc lập, KHÔNG mâu thuẫn:**
  1. *Giao diện* — ảnh full-res `image/BUG-TKHSYCHTPL_OOS_01-cot-canh-bao-thoi-han-hien-da-hoan-thanh.png` (1920×1080, đã mở đọc pixel): cột "Mã vụ việc" và cột "Cảnh báo thời hạn" **cùng lọt trong một khung hình**, cả 2 dòng đều hiện "Đã hoàn thành" ở cột "Cảnh báo thời hạn"; chân bảng ghi "Hiển thị 1-2 / 2 kết quả".
  2. *Dữ liệu danh sách trả về* — gọi lại chính dịch vụ danh sách bằng phiên đăng nhập của `cbnv_tw_03`: HTTP 200, `meta.total = 2`, cả 2 bản ghi mang mức cảnh báo `SAP_HET` (đúng lý do lọt bộ lọc), `trangThai` là `TU_CHOI` / `HOAN_THANH`.
  ⇒ Giao diện và dữ liệu trả về khớp nhau: bản ghi lọt bộ lọc vì mức cảnh báo lưu trữ vẫn là "Sắp hết hạn", còn nhãn "Đã hoàn thành" là cách giao diện hiển thị đè khi hồ sơ đã đóng.
- **Phân biệt rõ 2 cột dễ nhầm** (đây là chỗ đã suýt kết luận sai ở lượt trước): cột **"Trạng thái"** hiện "Từ chối" / "Hoàn thành"; cột **"Cảnh báo thời hạn"** đứng sau "Thời hạn xử lý" và hiện "Đã hoàn thành". Hai cột khác nhau, hai nhãn khác nhau — ảnh bằng chứng lần này lấy đủ cả dải bảng ở bề rộng 1920px nên không còn cột nào bị khuất ngoài khung.
- **Không kết luận `Open`:** đã tự mở `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` kiểm 4 chỗ (dòng 636 FR-V.I-08, dòng 1436 FR-V.I-CROSS-01, dòng 1656 SCR-V.I-01 cột 21, dòng 2442 BR-CALC-03) + `grep "Đã hoàn thành"` toàn file → **0 kết quả**; `grep` các cụm "đặt lại / xoá cảnh báo" → **0 kết quả**. Không trích được điều khoản nào bị vi phạm ⇒ theo §Tự vấn bắt buộc, verdict phải là `BA confirm`, không phải `Open`.
- **Không phải hồi quy do bản vá:** cách hiển thị này đã có từ trước lần sửa bộ lọc "Mức SLA", không phải hiện tượng mới phát sinh trên bản dựng hiện tại.

**Kết luận: 0 GAP** — mọi điều kiện quan sát được đã ghi bằng dữ kiện thật từ ảnh đã đọc pixel + dữ liệu danh sách trả về, không dòng nào để `...`.
