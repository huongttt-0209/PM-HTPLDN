# Bảng đối chiếu điều kiện — TKNHCH_05 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Dữ liệu tiền đề | Tab Câu hỏi có ≥1 câu hỏi | 1 câu hỏi "QA UAT QLNHCH_08..." trong danh sách | Không |
| Input tìm kiếm | Từ khóa chắc chắn không khớp | "zzzznomatch123khongtontai" | Không |
| Kết quả kỳ vọng | Danh sách rỗng 0 kết quả (không trả toàn bộ) | FE gửi param `keyword`, list còn 0 dòng + "Không có câu hỏi nào phù hợp" | Không |
