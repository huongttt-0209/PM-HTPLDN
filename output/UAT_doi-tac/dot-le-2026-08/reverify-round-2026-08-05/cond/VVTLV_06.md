# Bảng đối chiếu điều kiện — VVTLV_06 (re-verify vòng 2, lượt đo 05/08/2026 08:37–08:40)

Loại bug: **nội dung tệp PDF xuất ra của Báo cáo thống kê** → phụ thuộc mẫu trình bày dùng chung, không phụ thuộc dữ liệu ⇒ đo trực tiếp trên tệp thật.
Tiêu chí lấy từ ô *DEV phản hồi lần 2* của chính dòng này (3 mục "Còn thiếu"), đối chiếu lại với đặc tả
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:86` và `:124` (mục `[BA chốt 2026-08-04]`).

| Điều kiện | Bug gốc (note vòng 2, 04/08) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu, bản dựng đang chạy | `https://18.143.165.120.nip.io` — nhãn bản dựng **HTPLDN · V1.0.6** (trùng nhãn lần đo 04/08, nhãn không tăng theo lần triển khai) | Không |
| Vai trò | Cán bộ nghiệp vụ TW | `cbnv_tw` · CB_NV_TW · `donViId 00000000-0000-4000-8000-000000000001` · cấp TW | Không |
| Màn hình | Báo cáo thống kê → BC Vụ việc theo lĩnh vực | Đúng màn đó, đi bằng menu bên trái | Không |
| Tiêu chí lọc | Kỳ Năm 2026, đơn vị Toàn quốc | Kỳ **Năm** · 01/01/2026 → 31/12/2026 · **Toàn quốc** | Không |
| Dữ liệu không bị bộ đệm cũ | — | "Thời điểm tạo: 05/08/2026 08:37" (mới sinh trong phiên đo, không phải bản đệm 04/08) | Không |
| Thao tác xuất | Bấm nút Xuất PDF trên giao diện | Bấm thật qua trình duyệt → hộp thoại tùy chọn in (A4 · Dọc) → **Xuất file**; `POST /api/v1/bao-cao/export` trả **200**, `content-type: application/pdf` | Không |

**Kết luận: 0 GAP** — đo được đúng kịch bản của cả 3 mục còn lỗi.

## Đo từng ý (05/08/2026, tệp `BaoCaoVuViecTheoLinhVuc_20260805_0839.pdf`, 31.831 byte)

### Ý 1 — Đầu trang: quốc hiệu, tiêu ngữ, tên cơ quan ban hành → ✅ ĐÃ CÓ

Đọc thẳng nội dung tệp:

- Tên cơ quan ban hành: `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP` (góc trái)
- Quốc hiệu: `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` (góc phải)
- Tiêu ngữ: `Độc lập - Tự do - Hạnh phúc`

Đúng `srs-fr-11-bao-cao.md:86` — *"**đầu trang** có quốc hiệu, tiêu ngữ và tên cơ quan ban hành"*.

### Ý 2 — Cuối trang: ngày ký, họ tên người xuất, chỗ đóng dấu → ✅ ĐÃ CÓ

- Ngày ký: `Ngày 05 tháng 08 năm 2026`
- Nhãn khối ký: `NGƯỜI XUẤT BÁO CÁO`
- Chỗ trống con dấu: `(Ký, ghi rõ họ tên và đóng dấu)` + khoảng trắng bên dưới
- Họ tên cán bộ xuất: `CB Nghiệp vụ - Trung ương` (lấy từ trường họ tên của tài khoản đang đăng nhập)
- **Không có dòng chức danh** — đúng ràng buộc *"Không in dòng chức danh người ký"* ở cùng dòng đặc tả.

### Ý 3 — Tên tệp có giờ-phút, xuất 2 lần trong ngày không đè nhau → ✅ ĐÃ SỬA

Xuất 3 lần trong cùng phiên, đọc `content-disposition` của từng phản hồi (nguồn chuẩn, không phụ thuộc trình duyệt có lưu tệp hay không):

- Lần 1 — giờ máy chủ `01:39:17 GMT` (08:39 giờ VN) → `BaoCaoVuViecTheoLinhVuc_20260805_0839.pdf`
- Lần 3 — giờ máy chủ `01:40:18 GMT` (08:40 giờ VN) → `BaoCaoVuViecTheoLinhVuc_20260805_0840.pdf`

⇒ Hai lần xuất trong **cùng một ngày** ra **hai tên tệp khác nhau**, không còn đè lên nhau.
Đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` tại `srs-fr-11-bao-cao.md:86`.

### Kiểm lại 2 mục vòng trước đã đạt (không suy diễn, đo lại)

- **Khổ giấy:** trang đo được `595.3 × 841.9` pt = **A4 dọc**. ✅
- **Phông chữ:** tệp nhúng họ `Tinos` (bộ chữ tương thích số đo với Times New Roman, thay thế chuẩn trên máy chủ Linux). Cỡ: khối quốc hiệu/tên cơ quan **13**, tiêu đề báo cáo 14, dòng kỳ/đơn vị/ngày tạo 12, bảng số liệu 11, khối ký 13 nghiêng.
- **Bốn mục nhận dạng:** tên báo cáo `BC VỤ VIỆC THEO LĨNH VỰC` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 05/08/2026`. ✅
- **Số liệu khớp giao diện:** Dân sự 13 · Lao động 11 · Thuế 5 · Thương mại 17 · tổng 46 — trùng khít bảng trên màn hình. ✅

Ảnh: [`../image/VVTLV_06-r3-pdf-du-quoc-hieu-tieu-ngu-va-khoi-ky.png`](../image/VVTLV_06-r3-pdf-du-quoc-hieu-tieu-ngu-va-khoi-ky.png)

## Kết luận

**PASS** — cả 3 mục mở lại ngày 04/08 đều đã được khắc phục, đo trực tiếp trên tệp thật, không suy diễn từ quan sát tĩnh.

> Ghi nhận thêm, KHÔNG chấm là lỗi và KHÔNG mở lại:
> - Tên tệp dùng `BaoCao...` trong khi đặc tả mô tả `{TenBaoCao}` là tên loại báo cáo (`BC ...`) viết liền — tức chữ `BC` được viết đủ thành `BaoCao`. Phần bắt buộc (giờ-phút, bỏ dấu, bỏ ký tự đặc biệt) đều đúng.
> - Cỡ chữ trong tệp chạy 11–14 tuỳ khối thay vì đồng loạt 13; khối quốc hiệu và khối ký đúng 13. Mục này đã được chấm đạt ở vòng trước nên không lật lại ở vòng này.
