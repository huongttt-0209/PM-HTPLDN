# Bảng đối chiếu điều kiện — QLTVV_10 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Thao tác | Danh sách TVV → bấm "Xuất Excel" (KHÔNG lọc) → mở file | Bấm "Xuất Excel" trên danh sách (không lọc), lấy file xlsx export | Không |
| Dữ liệu tiền đề | TVV có chứng chỉ/số thẻ | TVV-BTP-TW-0002 có "Chứng chỉ chi tiết" (Chứng chỉ hành nghề Luật sư, cấp 15/03/2012) | Không |
| Cột "Chứng chỉ (tên + ngày cấp)" | Chỉ có mã/số thẻ, THIẾU ngày cấp | Cột 7 "Chứng chỉ (tên + ngày cấp)" = "Chung chi hanh nghe Luat su (15/3/2012)" — có tên chứng chỉ + ngày cấp | Không |
