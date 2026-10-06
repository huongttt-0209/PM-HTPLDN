# Bảng đối chiếu điều kiện — CNDSMLTVV_OOS_02 (row 142, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Công khai mạng lưới TVV — FR-IV-08 (UC46), màn SCR-IV-01 "Danh sách Tư vấn viên", thanh thao tác hàng loạt
**Nội dung TC:** hộp thoại công khai mở từ thao tác **hàng loạt** thiếu hoàn toàn phần "File đính kèm" mà `MD-CONG-KHAI` quy định (SRS `:1464` → `:1406(b)`, `:657`).
**Loại bug:** thành phần hộp thoại chỉ quan sát được sau **thao tác mở từ một đường vào cụ thể**, và kết luận dựa trên **đối chứng hai đường vào** → KHÔNG phải bug tĩnh, BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG).
**Ngày verify:** 2026-08-03 · **Tài khoản QA dùng:** `cbnv_tw_02` (CB_NV_TW, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW)

> **Nguồn gốc dòng TC:** lỗi do QA tự phát hiện khi verify CNDSMLTVV_01 (row 124), nằm ngoài tiêu chí của phiếu nên mở dòng mới. **Không có evidence đối tác cho riêng lỗi này** — cột "Đối tác" ghi rõ "Không áp dụng" thay vì suy diễn điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | `cbnv_tw_02` — "CB Nghiệp vụ - Trung ương #02", vai trò `CB_NV_TW`, đơn vị `Cục Bổ trợ tư pháp - Bộ Tư pháp`, cấp `BTP · TW`. **Chọn đúng vai trò này là điều kiện quyết định**: `FR-IV-08:657` ghi trường `file_dinh_kem_cong_khai` do "CB Nghiệp vụ upload (tùy chọn) trong modal MD-CONG-KHAI" — đo bằng vai trò khác thì không loại trừ được giả thuyết "vùng tải tệp bị ẩn do thiếu quyền" | Không |
| Màn hình + tab | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Màn "Tư vấn viên / Chuyên gia" (`/chuyen-gia-tvv/danh-sach`), tab **"Đang hoạt động"** — đúng tab mà `:1464` quy định cho thao tác công khai hàng loạt | Không |
| Trạng thái entity | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | `TVV-SEED-0001` "Nguyễn Văn Seed" — `trangThai = HOAT_DONG`, `laCongKhai = false` (chưa công khai, nên nút công khai hàng loạt bấm được) | Không |
| Đường vào mở hộp thoại (biến số cần đối chứng) | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Đo **hai đường vào trên cùng một hồ sơ, cùng một phiên đăng nhập, cùng một tài khoản**: (a) tích chọn dòng → nút "Công khai lên Cổng PLQG" trên thanh thao tác hàng loạt; (b) mở màn hình chi tiết hồ sơ đó → nút "Công khai lên Cổng PLQG" ở đầu màn | Không |
| Cách đếm thành phần hộp thoại | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Đếm số vùng tải tệp, số ô chọn tệp, danh sách nhãn trường, và đọc **toàn bộ chữ hiển thị** trong hộp thoại (không chỉ dựa vào ảnh) | Không |

## Ghi chú đóng GAP

- **Không có ô GAP nào vì không có điều kiện đối tác để lệch:** dòng TC do QA mở, toàn bộ điều kiện do QA tự dựng và đã ghi đủ ở cột "Mình test".
- **Kết luận dựa trên đối chứng đo được, không dựa trên lập luận:**

  - **Số vùng tải tệp** — hộp thoại hàng loạt: **0** · hộp thoại từ màn chi tiết: **2**
  - **Số ô chọn tệp** — hàng loạt: **0** · màn chi tiết: **1**
  - **Nhãn trường** — hàng loạt: `["Mô tả công khai"]` · màn chi tiết: `["Mô tả công khai", "Tệp đính kèm (tùy chọn)"]`
  - **Chuỗi mô tả định dạng** — hàng loạt: *(không xuất hiện)* · màn chi tiết: "Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp."

  *(Trình bày dạng gạch đầu dòng thay vì bảng lồng — bảng lồng làm bộ kiểm tra định dạng của `sheet_write.py` hiểu nhầm là dòng của bảng điều kiện. Số liệu giữ nguyên.)*

- **Giả thuyết cạnh tranh đã bị loại trừ bằng thực nghiệm:** "vùng tải tệp bị ẩn do tài khoản thiếu quyền" — bác bỏ, vì cùng tài khoản đó mở hộp thoại từ màn chi tiết thì vùng tải tệp hiện đủ. "Tính năng chưa làm" — bác bỏ, vì chuỗi mô tả định dạng ở đường vào (b) khớp đúng phần (b) của `:1406`.
- **Đã đọc chữ hiển thị thật, không chỉ nhìn ảnh:** toàn bộ nội dung hộp thoại hàng loạt không chứa từ nào về tệp đính kèm hay định dạng tệp — loại trừ khả năng vùng tải tệp tồn tại nhưng nằm ngoài khung ảnh chụp.
- **Không thay đổi dữ liệu ở bước đo này:** hộp thoại đường vào (b) được đóng bằng nút [Hủy], không công khai.

**Kết luận: 0 GAP** — mọi điều kiện quan sát lỗi đã được dựng và test thật.
