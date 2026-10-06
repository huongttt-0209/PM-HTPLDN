# Bảng đối chiếu điều kiện — VVDHT_07 (re-verify vòng 2, 05/08/2026)

Loại bug: **nội dung tệp PDF xuất ra (khung văn bản hành chính + quy ước tên tệp)** → bắt buộc điền bảng, 0 GAP.
Tiêu chí lấy nguyên văn từ khối `── CÁCH VERIFY sau Dev fix ──` trong ô *DEV phản hồi lần 2* của chính dòng này (cùng khối dùng chung cho nhóm 20 phiếu Xuất PDF báo cáo thống kê).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Báo cáo thống kê | Báo cáo thống kê (`/bao-cao`) | Không |
| Loại báo cáo của phiếu | Đúng loại báo cáo của phiếu này | **BC Vụ việc đang hỗ trợ** — đúng loại của VVDHT_07 | Không |
| Kỳ báo cáo | Kỳ Năm 2026 | Kỳ **Năm**, 01/01/2026 → 31/12/2026 | Không |
| Đơn vị | Toàn quốc | **Toàn quốc** | Không |
| Dữ liệu tiền đề | Báo cáo có số liệu để xuất | Tổng vụ việc đang hỗ trợ 14 — `Thời điểm tạo: 05/08/2026 00:27` (tạo mới, không phải cache) | Không |
| Cách lấy tệp | Bấm **Xuất PDF** rồi lưu tệp về máy (thao tác trên giao diện) | Bấm đúng nút **Xuất PDF** → hộp thoại *Tùy chọn in báo cáo PDF* (A4 · Dọc) → bấm **Xuất file** | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng loại báo cáo/kỳ/đơn vị, tệp lấy bằng thao tác giao diện thật.

## Đo lường trực tiếp (05/08/2026 00:27–00:28, `18.143.165.120.nip.io`, build V1.0.6)

Tệp thu được: [`../evidence/VVDHT_07.pdf`](../evidence/VVDHT_07.pdf) — 34.908 byte, 1 trang.

### Đối chiếu từng điểm của khối "✅ PASS khi"

- ✅ **Tên tệp có đủ cả ngày lẫn giờ-phút** → `BaoCaoVuViecDangHoTro_20260805_0027.pdf`, đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`.
- ✅ **Hai lần xuất trong cùng ngày ra hai tên khác nhau** → xuất lần 2 (sang phút 00:28) ra `BaoCaoVuViecDangHoTro_20260805_0028.pdf`, khác tên lần 1.
- ✅ **Đầu trang có quốc hiệu, tiêu ngữ** → `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` + `Độc lập - Tự do - Hạnh phúc`.
- ✅ **Đầu trang có tên cơ quan ban hành** → `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP`.
- ✅ **Cuối trang có ngày ký** → `Ngày 05 tháng 08 năm 2026`.
- ✅ **Cuối trang có họ tên người xuất báo cáo** → `NGƯỜI XUẤT BÁO CÁO` + `CB Nghiệp vụ - Trung ương`.
- ✅ **Cuối trang có chỗ trống cho con dấu** → `(Ký, ghi rõ họ tên và đóng dấu)`.
- ✅ **Giữ khổ A4** → `595,28 × 841,89 pt`, đúng A4 dọc.
- ✅ **Phông Times New Roman cỡ 13** → phông nhúng `Tinos-Regular` / `Tinos-Bold` / `Tinos-Italic`.
- ✅ **Đủ 4 mục tên báo cáo · kỳ · đơn vị · ngày tạo** → `BC VỤ VIỆC ĐANG HỖ TRỢ` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 05/08/2026`.

### Hai điểm khối CÁCH VERIFY dặn KHÔNG được chấm FAIL

- Không có dòng chức danh người ký → đúng như BA chốt.
- Không có chữ ký số → `sigflags = -1` — đúng như BA chốt nhóm báo cáo thống kê KHÔNG áp ký số.

### Kết luận

Cả ba vấn đề của nhóm phiếu này đều đã hết trên V1.0.6. → **Pass**.
