# Bảng đối chiếu điều kiện — QLKCHTV_37 (row 19) — Thiếu chức năng "Xuất Excel" đánh giá + thẻ tổng hợp

**Kết luận:** Open.
- Tái hiện đúng: khu vực **Đánh giá** không có nút **[Xuất Excel]**, và cũng thiếu luôn **thẻ tổng hợp** (Tổng đánh giá / Điểm TB / Phân bố).
- Căn cứ đặc tả rõ ràng: `srs-fr-13-tv-nhanh.md:574`, §3 SCR-X2-03 dòng 10 — *"Danh gia (v2.1 gop tu MH-13.4) | section/column | Diem (1-5 sao) / Nhan xet DN / Ngay danh gia. **The tong hop: Tong danh gia (COUNT) / Diem TB (AVG) / Phan bo (bar chart mini). [Xuat Excel]** | -- | hien thi trong tab Hoan thanh hoac chi tiet phien"*.
- Đã kiểm **cả hai nơi** mà đặc tả nêu (thẻ "Hoàn thành" và màn chi tiết phiên) — đều không có.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_37.jpg`) | Mình test (env nip.io, 27/07/2026 12:03) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Phiên `TVN-20260511-0002` — Kênh "Thủ công", Trạng thái **"Hoàn thành"** | Phiên `TVN-20260727-0002` — Trạng thái **"Hoàn thành"**. (Kênh "TV Nhanh" thay vì "Thủ công" — khác biệt này không ảnh hưởng: `:574` đặt điều kiện hiển thị theo **thẻ Hoàn thành / màn chi tiết phiên**, không theo kênh) | Không |
| Dữ liệu tiền đề | Phiên **đã có bản ghi đánh giá** từ doanh nghiệp: 5 sao, nhận xét "Test TC-DGTV-001 PASS", ngày 11/05/2026 | Phiên **đã có bản ghi đánh giá**: **5 sao**, nhận xét "QA tuần 4 — nội dung tư vấn rõ ràng, phản hồi nhanh.", ngày 27/07/2026. QA tự dựng: `POST …/tra-loi` rồi `POST …/danh-gia/cms-proxy` (điểm 5) → phiên tự chuyển sang "Hoàn thành". **Đúng điều kiện tiên quyết mà phiếu test yêu cầu** | Không |
| Input / filter / giá trị nhập | Mở màn chi tiết phiên, tìm nút "Xuất Excel" | Mở màn chi tiết phiên **và** mở thẻ "Hoàn thành" ở danh sách — liệt kê toàn bộ nút bằng mã lệnh ở cả hai nơi | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-TVN-danh-gia-thieu-xuat-excel.png` — đã mở đọc: khối **"Đánh giá"** chỉ có 3 dòng `Điểm đánh giá (5 sao)` · `Ngày đánh giá 27/07/2026` · `Nhận xét`. Không có nút nào trong khối, không có thẻ tổng hợp nào.
- Đo tại **màn chi tiết phiên** bằng mã lệnh:
  - tiêu đề các khối: `["TVN-20260727-0002", "Thông tin phiên tư vấn", "Đánh giá"]`
  - toàn bộ nút: `["Quay lại danh sách"]`
  - `coXuatExcel = false`
  - thẻ tổng hợp: `Tổng đánh giá = false`, `Điểm TB = false`, `Phân bố = false`
- Đo tại **thẻ "Hoàn thành"** của danh sách (địa chỉ `?tab=HOAN_TAT`):
  - toàn bộ nút: `["Thêm mới", "Làm mới", "Xóa bộ lọc", "Tìm kiếm", "TVN-20260727-0002"]`
  - `coXuatExcel = false`; thẻ tổng hợp: cả 3 đều `false`
  - tiêu đề cột bảng không đổi (8 cột), không có vùng thống kê nào phía trên/dưới bảng

## Phương pháp thứ hai (bắt buộc)

- **Đo ở cả hai vị trí mà đặc tả cho phép** (nêu ở trên) — đây là phép thử quyết định, loại trừ khả năng "nút có nhưng đặt ở chỗ khác". Phiếu test của đối tác chỉ đi theo đường "bấm Trả lời" (`:574` không đặt nút ở đó), nên QA đã bổ sung kiểm đúng 2 vị trí đặc tả nêu — kết quả vẫn không có.
- **Kiểm tầng máy chủ xem chức năng đã có chưa:** đọc danh mục giao diện lập trình (`/api/docs-json`) — nhóm tư vấn nhanh có 10 đường dẫn, **không có đường nào cho xuất tệp** (không có `export`, không có `xuat-excel`). Đối chiếu: kho câu hỏi **có** `POST /api/v1/kho-cau-hois/export` và chạy được (đã kiểm ở QLKCHTV_12). ⇒ Với Tư vấn nhanh, chức năng chưa được dựng ở cả giao diện lẫn máy chủ.
- **Xác nhận dữ liệu đánh giá thật sự tồn tại** (loại trừ "không có nút vì không có dữ liệu để xuất"): `GET /api/v1/tu-van-nhanhs/{id}` trả `"danhGiaTv": {"id": "20ec737d-…", "diem": "5", "nhanXet": "QA tuần 4 — nội dung tư vấn rõ ràng, phản hồi nhanh.", "ngayDanhGia": "2026-07-27T05:03:10.078Z"}` ⇒ đủ dữ liệu, vẫn không có nút.
- **Ghi nhận cho BA/dev về quy tắc đặt tên tệp:** phiếu test kỳ vọng tên tệp dạng `danh-gia-tv-nhanh-{mã phiên}{YYYYMMDD-HHmm}.xlsx`. Đã tìm toàn bộ `srs-v3.5/` — **không có** quy tắc đặt tên nào cho tệp này (`:574` chỉ ghi `[Xuat Excel]`). Khi dev dựng chức năng, cần BA chốt tên tệp và tập cột (gộp chung với BA-03 về tên tệp/tập cột của Kho câu hỏi).
