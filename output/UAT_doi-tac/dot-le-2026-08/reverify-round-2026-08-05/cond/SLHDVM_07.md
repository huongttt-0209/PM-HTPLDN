# Bảng đối chiếu điều kiện — SLHDVM_07 (re-verify vòng 2, 05/08/2026)

Loại bug: **nội dung tệp PDF xuất ra (khung văn bản hành chính + quy ước tên tệp)** → bắt buộc điền bảng, 0 GAP.
Tiêu chí lấy nguyên văn từ khối `── CÁCH VERIFY sau Dev fix ──` trong ô *DEV phản hồi lần 2* của chính dòng này.

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái), gói giao diện `index-CJp_EdxZ.js` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Báo cáo thống kê | Báo cáo thống kê (`/bao-cao`) | Không |
| Loại báo cáo của phiếu | Đúng loại báo cáo của phiếu này | **BC Số lượng hỏi đáp/vướng mắc pháp luật** — đúng loại của SLHDVM_07 | Không |
| Kỳ báo cáo | Kỳ Năm 2026 | Kỳ **Năm**, 01/01/2026 → 31/12/2026 | Không |
| Đơn vị | Toàn quốc | **Toàn quốc** | Không |
| Dữ liệu tiền đề | Báo cáo có số liệu để xuất | Tổng hỏi đáp 22 · Đã trả lời 11 · Chờ trả lời 11 · Tỷ lệ 50,0% — `Thời điểm tạo: 05/08/2026 00:13` (tạo mới, không phải cache) | Không |
| Cách lấy tệp | Bấm **Xuất PDF** rồi lưu tệp về máy (thao tác trên giao diện) | Bấm đúng nút **Xuất PDF** trên giao diện → hộp thoại *Tùy chọn in báo cáo PDF* (A4 · Dọc) → bấm **Xuất file**. Bắt được `POST /api/v1/bao-cao/export` + thẻ tải tệp | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng loại báo cáo/kỳ/đơn vị, tệp lấy bằng thao tác giao diện thật.

## Đo lường trực tiếp (05/08/2026 00:15–00:17, `18.143.165.120.nip.io`, build V1.0.6)

Tệp thu được: [`../evidence/SLHDVM_07.pdf`](../evidence/SLHDVM_07.pdf) — 34.313 byte, 1 trang.

### Đối chiếu từng điểm của khối "✅ PASS khi"

- ✅ **Tên tệp có đủ cả ngày lẫn giờ-phút** → `BaoCaoHoiDap_20260805_0015.pdf`, đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`.
- ✅ **Hai lần xuất trong cùng ngày ra hai tên khác nhau** → xuất 2 lần được `BaoCaoHoiDap_20260805_0016.pdf` và `BaoCaoHoiDap_20260805_0017.pdf`.
- ✅ **Đầu trang có quốc hiệu, tiêu ngữ** → `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` + `Độc lập - Tự do - Hạnh phúc`.
- ✅ **Đầu trang có tên cơ quan ban hành** → `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP`.
- ✅ **Cuối trang có ngày ký** → `Ngày 05 tháng 08 năm 2026`.
- ✅ **Cuối trang có họ tên người xuất báo cáo** → `NGƯỜI XUẤT BÁO CÁO` + `CB Nghiệp vụ - Trung ương` (họ tên tài khoản đang đăng nhập).
- ✅ **Cuối trang có chỗ trống cho con dấu** → `(Ký, ghi rõ họ tên và đóng dấu)`.
- ✅ **Giữ khổ A4** → `595,28 × 841,89 pt`, đúng A4 dọc.
- ✅ **Phông Times New Roman cỡ 13** → phông nhúng `Tinos-Regular` / `Tinos-Bold` / `Tinos-Italic`, bản tương thích số đo của Times New Roman (đúng như bản đo trước đã chấp nhận).
- ✅ **Đủ 4 mục tên báo cáo · kỳ · đơn vị · ngày tạo** → `BC SỐ LƯỢNG HỎI ĐÁP/VƯỚNG MẮC PHÁP LUẬT` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 05/08/2026`.

### Hai điểm khối CÁCH VERIFY dặn KHÔNG được chấm FAIL

- Không có dòng chức danh người ký → đúng như BA chốt (khối ký chỉ in ngày + họ tên + chỗ dấu).
- Không có chữ ký số → cờ chữ ký của tệp (`sigflags`) trả `-1`, tệp không có trường ký điện tử — đúng như BA chốt nhóm báo cáo thống kê KHÔNG áp ký số.

### Kết luận

Cả 3 vấn đề của nhóm phiếu này đều đã hết trên V1.0.6: khung văn bản hành chính (quốc hiệu + cơ quan ban hành + khối ký) đã có, tên tệp đã có giờ-phút và không đè nhau, ký số đúng chủ trương không áp. → **Pass**.

### Ghi nhận thêm khi đi qua màn Báo cáo thống kê

- Nút **Xuất PDF** mở hộp thoại *Tùy chọn in báo cáo PDF* (khổ giấy A4/A3/Letter · hướng Dọc/Ngang) rồi mới xuất ở nút **Xuất file** — khác bản đo trước (xuất thẳng). Không phải lỗi, nhưng cần biết để không kết luận nhầm "bấm Xuất PDF không có phản hồi".
- Bản xuất Excel cùng màn cũng đã theo đúng khuôn tên tệp: `BaoCaoHoiDap_20260805_0014.xlsx`.
