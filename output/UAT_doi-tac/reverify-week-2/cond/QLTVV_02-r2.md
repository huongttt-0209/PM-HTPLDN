# Bảng đối chiếu điều kiện — QLTVV_02 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác (3 ý):** (1) dữ liệu cột Điểm ĐG bị tràn/đè lên cột Trạng thái; (2) cột Điểm ĐG hiển thị không đồng nhất — chưa có điểm thì hiện "-/5", có điểm thì hiện số sao; (3) các nút thao tác Xem, Sửa bị xuống dòng.

**Evidence:** `QLTVV_02_v2.png` (ảnh tĩnh full-res) — màn `chuyen-gia-tvv/danh-sach`, tab "Đang hoạt động", header hiện vai trò
"Cán bộ NV Trung ương CB_NV_TW", bảng đang cuộn ngang sang phải (3 cột đầu ngoài vùng nhìn), phân trang "1-10 / 10 mục".

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ NV Trung ương (CB_NV_TW), đơn vị BTP·TW — đọc ở góc phải header ảnh | `cbnv_tw` / CB_NV_TW, đơn vị BTP·TW (Cục Bổ trợ tư pháp) | Không |
| Màn hình + tab | `chuyen-gia-tvv/danh-sach`, tab "Đang hoạt động", bộ lọc mặc định "Bộ lọc nâng cao (2)" | Cùng màn `chuyen-gia-tvv/danh-sach`, cùng tab "Đang hoạt động", cùng bộ lọc mặc định "Bộ lọc nâng cao (2)" | Không |
| Mật độ dữ liệu (yếu tố ép chiều rộng cột) | Có dòng Tổ chức tên dài ("Công ty Luật TNHH Alpha Hà Nội"), Lĩnh vực 3 thẻ + "+1" (xuống 2 dòng), Họ tên xuống 2 dòng | **Đã seed cho khớp:** cập nhật 2 bản ghi thành Tổ chức "Công ty Luật TNHH Demo Kiểm Thử" + Lĩnh vực 4 giá trị → hiển thị "Đất đai · Lao động · Thuế +1" (2 dòng); Họ tên cũng xuống 2 dòng. Sau khi đo đã trả về nguyên trạng | Không |
| Có bản ghi ĐÃ có điểm đánh giá và bản ghi CHƯA có (để so 2 kiểu hiển thị) | Có cả 2 loại: dòng "—/5" và dòng có sao + số (3.7/5, 8.3/5) | Có cả 2 loại: 4 dòng "—/5" và 1 dòng "QA TVV Seed28 Active" = 4.2/5 (2 lượt đánh giá thật, `soLuongDanhGia=2`) | Không |
| Chiều rộng cửa sổ (yếu tố quyết định layout) | Vùng nội dung ứng dụng ≈ 1580 px (ảnh 1906 px trừ sidebar ≈ 320 px); bảng có thanh cuộn ngang | Đo ở **3 mức**: 1920 (vùng nội dung 1593 px — sát nhất với đối tác), 1440 và 1280 (đều có cuộn ngang như ảnh đối tác) | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng màn/tab/bộ lọc, đã seed cho khớp mật độ dữ liệu, có đủ 2 loại dòng (có điểm / chưa có điểm), và đo ở 3 chiều rộng phủ được chiều rộng của đối tác.

Đối chiếu SRS vs thực tế web + toàn bộ phép đo: xem [`../reverify-audit/QLTVV_02/audit.md`](../reverify-audit/QLTVV_02/audit.md).
