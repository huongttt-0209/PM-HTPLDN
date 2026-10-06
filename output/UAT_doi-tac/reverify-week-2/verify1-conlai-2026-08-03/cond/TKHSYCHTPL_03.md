# Bảng đối chiếu điều kiện — TKHSYCHTPL_03 (row 129, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Tìm kiếm / bộ lọc hồ sơ vụ việc — FR-V.I-08 (UC58), màn SCR-V.I-01
**Loại bug:** bug FILTER — phụ thuộc vai trò + dữ liệu + giá trị lọc → BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG)
**Ngày verify:** 2026-08-03 · **Tài khoản QA dùng:** `cbnv_tw_03` (CB_NV_TW, đơn vị BTP · TW, bản dựng `HTPLDN · V1.0.5`)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res `frames/TKHSYCHTPL_03/t004.12s.jpg`) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — nhãn góc phải khung hình ghi "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" | `cbnv_tw_03` — nhãn góc phải "CB Nghiệp vụ - Trung ương #03 · CB_NV_TW", đơn vị "BTP · TW" (ảnh `image/BUG-TKHSYCHTPL_03-01-baseline-khong-loc-37-ket-qua.png`). `GET /auth/me` trả `vaiTro:["CB_NV_TW"], capDonVi:"TW", donViId:...0001` | Không |
| Màn hình + tab đang đứng | Màn "Vụ việc HTPL" (danh sách hồ sơ vụ việc), tab **Tất cả** đang chọn | Cùng màn "Vụ việc HTPL", tab **Tất cả** đang chọn | Không |
| Dữ liệu tiền đề (có bản ghi rơi vào nhóm "Sắp hết hạn" hay không) | Có — khung hình gốc `t000.00s.jpg` (trước khi lọc) hiện 3 dòng cột "Cảnh báo thời hạn" = "Sắp hết hạn · còn 1 ngày LV" / "còn 0 ngày LV"; tổng "Tất cả 56" | Có — 2 bản ghi mức "Sắp hết hạn" (`VV-BTP-TW-20260712-006`, `-005`), xác nhận 2 chiều: giao diện trả 2 dòng + `GET /api/v1/vu-viecs?mucSla=SAP_HET` trả `meta.total = 2`, mỗi bản ghi có `mucDoCanhBao:"SAP_HET"`. Tổng baseline "Tất cả 37" | Không |
| Input / filter / giá trị nhập | Ô từ khóa **trống** · Lĩnh vực PL **trống** · Đơn vị **trống** · Kênh tiếp nhận **trống** · **Mức SLA = "Sắp hết hạn"** · "Bộ lọc nâng cao (3)" đang thu gọn (để nguyên mặc định) | Ô từ khóa **trống** · Lĩnh vực PL **trống** · Đơn vị **trống** · Kênh tiếp nhận **trống** · **Mức SLA = "Sắp hết hạn"** · "Bộ lọc nâng cao (3)" để nguyên mặc định (đã mở ra kiểm chứng: Trạng thái = "Tất cả", Từ ngày / Đến ngày trống — ảnh `image/BUG-TKHSYCHTPL_03-08-bo-loc-nang-cao-mo-rong.png`) | Không |
| Cách kích hoạt bộ lọc | Chọn giá trị trong ô "Mức SLA" rồi để hệ thống chạy tìm kiếm (địa chỉ trang đổi thành `...?mucSla=SAP_HET_HAN&page=1`) | Chọn giá trị trong ô "Mức SLA" rồi bấm **[Tìm kiếm]** (địa chỉ trang đổi thành `...?mucSla=SAP_HET&page=1`) | Không |

## Ghi chú đóng GAP

- **Đã chạy đủ 4 giá trị của bộ lọc "Mức SLA" + 1 baseline** (phép đo phân biệt, xem `reverify-audit/TKHSYCHTPL_03.md`), không chỉ riêng giá trị đối tác phản ánh — nên loại trừ được cả 3 giả thuyết "chỉ hỏng ở Sắp hết hạn" / "hỏng toàn bộ bộ lọc" / "đã sửa".
- **Đã tái lập đúng giá trị đối tác gặp lỗi ở tầng máy chủ:** gọi thẳng danh sách với tham số `SAP_HET_HAN` (đúng giá trị bản dựng cũ của đối tác gửi lên) vẫn bị từ chối, thông báo trùng khít câu chữ trong khung hình bằng chứng. Tức không phải "không tái hiện vì máy chủ đã đổi hành vi" — mà là **giao diện nay gửi đúng giá trị**.
- **Bản dựng khác nhau nhưng KHÔNG phải GAP:** đối tác quay trên bản `HTPLDN · V1.0.2` (đọc được ở góc trái khung hình), QA test trên `HTPLDN · V1.0.5`. Đây chính là mục đích của vòng verify sau khi dev báo đã sửa — chênh bản dựng là điều kiện cần để kiểm tra bản vá, không phải điều kiện làm sai lệch kết quả.
- **Đã tải lại trang (bỏ qua bộ nhớ đệm) trước khi chốt kết luận** rồi lặp lại đúng thao tác "Sắp hết hạn" một lần nữa — loại trừ khả năng tab mở lâu còn chạy mã cũ.
- **Danh sách rỗng ≠ báo lỗi:** đã phân biệt rạch ròi. Giá trị "Quá hạn nghiêm trọng" trả **0 bản ghi kèm màn rỗng hợp lệ** ("Không tìm thấy hồ sơ phù hợp", không có khung thông báo lỗi nào) — khác hẳn tình huống đối tác gặp (có khung thông báo lỗi đỏ).

**Kết luận: 0 GAP** — mọi điều kiện của đối tác đã được tái lập bằng test thật trên đúng vai trò, đúng dữ liệu, đúng giá trị lọc.
