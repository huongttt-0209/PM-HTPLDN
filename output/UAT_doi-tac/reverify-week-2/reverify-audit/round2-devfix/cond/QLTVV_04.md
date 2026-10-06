# Bảng đối chiếu điều kiện — QLTVV_04 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Màn hình | Chi tiết TVV, tab "Hồ sơ" | /chuyen-gia-tvv/:id tab Hồ sơ (TVV-BTP-TW-0002, có đánh giá 4.2) | Không |
| Nhóm Thông tin cá nhân | Thiếu "Loại" + "Đơn vị quản lý" | Có "Loại"=Tư vấn viên + "Đơn vị quản lý"=Cục Bổ trợ tư pháp | Không |
| Nhóm Nghề nghiệp | Thiếu "Chứng chỉ hành nghề", "Mô tả kinh nghiệm", "Chức vụ", "Nơi công tác" | Cả 4 trường đều render (Chứng chỉ hành nghề, Mô tả kinh nghiệm, Chức vụ, Nơi công tác) | Không |
| Điểm ĐG header | Thang /10 (đối tác "8.3/10") | Header hiển thị "4.2/5" (đúng thang /5 + sao) | Không |
