# Bảng đối chiếu điều kiện — QLTVV_12 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Thao tác | Danh sách TVV → áp bộ lọc có kết quả → "Xuất Excel" → mở file | Lọc từ khóa "Seed28" (còn 1 record TVV-BTP-TW-0002) → "Xuất Excel" → lấy file xlsx | Không |
| Dữ liệu tiền đề | TVV lọc ra có chứng chỉ | TVV-BTP-TW-0002 có Chứng chỉ hành nghề Luật sư (cấp 15/03/2012) | Không |
| Cột "Chứng chỉ (tên + ngày cấp)" | Vẫn chỉ có mã/số thẻ, thiếu ngày cấp | Cột 7 = "Chung chi hanh nghe Luat su (15/3/2012)" — có tên chứng chỉ + ngày cấp (kể cả khi có bộ lọc) | Không |
