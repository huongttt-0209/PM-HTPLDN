# Quan sát real-data — NHSYC_02 (form Nhập thủ công, gộp 8 ý con)

Case gộp nhiều lỗi con → tách từng ý, ra verdict riêng, rồi lấy verdict tổng.

## Form thực tế trên web (`/vu-viec/tao-moi`, vai trò cbnv_tw)

- **Nhóm 1 "Thông tin Doanh nghiệp"** — **0 trường nhập**. Chỉ có nút "Tìm doanh nghiệp". Sau khi chọn DN → hiện thẻ chỉ-đọc ("Công ty TNHH Seed Publishable · MST: 0100000001 · Mã: DN-SEED-0001") + nút "Bỏ chọn". Vẫn 0 trường nhập.
- **Nhóm 2 "Nội dung Yêu cầu"** — 8 trường: Tiêu đề vụ việc*, Nội dung yêu cầu* (maxlength **50000**), Lĩnh vực pháp luật*, Loại hình hỗ trợ*, Vướng mắc, Độ ưu tiên*, Lý do ưu tiên, Ghi chú.
- **Nhóm 3 "Tài liệu Đính kèm"** — vùng kéo thả. Chú thích: "Tối đa 10 tệp. Định dạng: .doc, .docx, .xls, .xlsx, .pdf, .jpg, .png, .gif. Dung lượng tối đa: 20MB."
- **Nhóm 4 "Thông tin Tiếp nhận"** — **chỉ 2 trường**: Kênh tiếp nhận* (mặc định "Trực tiếp"), Người tiếp nhận (khóa, auto-fill "CB Nghiệp vụ - Trung ương"). **KHÔNG có "Ngày tiếp nhận".**

## Giá trị thực của các danh sách chọn

- **Lĩnh vực pháp luật — 10 giá trị:** Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư. (Không có "Khác".)
- **Loại hình hỗ trợ — 6 giá trị:** Tư vấn pháp luật, Tham gia tố tụng, Đại diện ngoài tố tụng, Hòa giải, Đào tạo/bồi dưỡng, Trợ giúp khác.
- **Kênh tiếp nhận — 3 giá trị:** Trực tiếp, Điện thoại, Bưu chính.
- **Độ ưu tiên — 5 giá trị:** 1 Rất cao … 5 Rất thấp.

## Verdict từng ý

| # | Ý đối tác phản ánh | Thực tế web | Đối chiếu SRS | Verdict |
|---|---|---|---|---|
| 1 | Nhóm 1 Thông tin DN "không giống thiết kế" | 0 trường nhập; DN chọn qua modal; modal "Tạo DN mới" có **đúng 2 trường bắt buộc** (Tên DN + MST) | **SRS mâu thuẫn nội bộ.** SCR-V.I-02 rows 5-17 (dòng 1666-1678) vẫn liệt kê 13 trường DN inline; NHƯNG FR-V.I-04 §Inputs #1 (dòng 312) + SCR-V.I-02 dòng 1668 ghi rõ *"BA chốt 2026-05-30: modal chỉ cần 2 trường định danh (ma_so_thue + ten_doanh_nghiep); 15 trường khác tùy chọn; CB NV bổ sung sau qua SCR-V.III-02"*. Web làm **đúng quyết định BA mới nhất** | **BA confirm** |
| 2 | "Loại hình hỗ trợ" thiết kế 4, web 6 | 6 giá trị | SRS nêu 3 giá trị ví dụ (Tư vấn / Đại diện / Hỗ trợ khác — dòng 176, 1683) nhưng khai là **FK → DANH_MUC (UC100/UC105)** = danh mục cấu hình được, không cứng trong code | **BA confirm** |
| 3 | "Lĩnh vực pháp lý" thiết kế 8, web 7, thiếu "Khác" | **10 giá trị**, không có "Khác" | SRS khai **FK → DANH_MUC (loai='LINH_VUC_PHAP_LY')** (dòng 316, 1682), **không liệt kê giá trị** → nội dung danh mục do cấu hình, không phải lỗi code | **BA confirm** |
| 4 | Nội dung vụ việc/vướng mắc đang 2 trường, "theo thiết kế là 1 trường" | 2 trường riêng: "Nội dung yêu cầu" + "Vướng mắc" | SRS quy định **ĐÚNG 2 trường riêng**: `noi_dung_yeu_cau` (dòng 1681) + `vu_viec_vuong_mac` (dòng 1684); FR-V.I-04 §Inputs #6, #7 (dòng 317-318). Web **đúng SRS**; kỳ vọng đối tác trái SRS | **BA confirm** |
| 5 | Thiếu trường "Thời điểm phát sinh" | Không có | SRS **không có** trường này ở SCR-V.I-02 lẫn FR-V.I-04 §Inputs → SRS im lặng | **BA confirm** |
| 6 | Nhóm 3 thiếu "Hướng dẫn hồ sơ cần nộp" | Không có | SRS accordion-3 chỉ có `file_dinh_kem` + bảng file đã upload (dòng 1686-1688) → SRS im lặng | **BA confirm** |
| 7 | **Nhóm 4 thiếu "Ngày tiếp nhận"** | **Không có trường này** | **SCR-V.I-02 row 30 (dòng 1691): `ngay_tiep_nhan` \| C11 DatePicker \| BẮT BUỘC \| Mặc định ngày hiện tại \| Điều kiện hiển thị: Luôn** → web thiếu trường SRS bắt buộc | **🔴 OPEN** |
| 8 | Nhóm 4 thiếu "Ghi chú tiếp nhận" + "Kênh tiếp nhận" giá trị sai thiết kế | Không có "Ghi chú tiếp nhận" (nhưng có "Ghi chú" ở nhóm 2). Kênh tiếp nhận = 3 giá trị | "Ghi chú tiếp nhận" **không có trong SRS** (SRS chỉ có `ghi_chu` ở accordion-2, dòng 1685) → im lặng. Kênh tiếp nhận: **SRS mâu thuẫn** — FR-V.I-04 §Inputs #8 (dòng 319) `CHECK IN ('TRUC_TIEP','DIEN_THOAI','BUU_CHINH')` = **3 giá trị** (web khớp) ↔ SCR-V.I-02 row 29 (dòng 1690) = **5 giá trị** (thêm DVC, HE_THONG_KHAC) | **BA confirm** |

## Verdict tổng

**OPEN** — theo quy tắc "≥1 ý Open → verdict tổng Open". Ý Open duy nhất: **thiếu trường "Ngày tiếp nhận"** (ý 7). 7 ý còn lại là bất đồng đặc tả / khoảng trống SRS / SRS mâu thuẫn nội bộ → chuyển BA.

Bug log: `BUG-NHSYC_02` (chỉ ý 7).
