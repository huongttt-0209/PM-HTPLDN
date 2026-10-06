# Bảng đối chiếu điều kiện — PDKQDTTH_01 (reverify R2 sau dev fix)

> Ghi chú: bug gốc test cấp TW (cbnv_tw + cbpd_tw); khóa TW có sẵn KQ đã Hoàn thành từ trước, không re-run được. Đã tạo cặp tài khoản Sở Tư pháp Hà Nội (cbnv_hn + cbpd_hn) chạy đúng thao tác duyệt KQ trên AAA-KH-DP. Cơ chế "Thông báo CB NV khi duyệt/từ chối KQ đào tạo" (UC37 §Processing) là handler dùng chung mọi cấp → cặp vai trò CB NV ↔ CB PD là điều kiện quyết định, đã test đúng.

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Cặp vai trò | CB Nghiệp vụ (trình duyệt) + CB Phê duyệt (duyệt KQ) | cbnv_hn (CB Nghiệp vụ) trình duyệt + cbpd_hn (CB Phê duyệt) duyệt KQ — cùng cặp vai trò nghiệp vụ | Không |
| State + thao tác | Khóa "Chờ duyệt KQ" → CB PD bấm Duyệt KQ → Hoàn thành | AAA-KH-DP: cbnv_hn trình duyệt → "Chờ duyệt KQ" → cbpd_hn Phê duyệt KQ → "Hoàn thành" | Không |
| Kết quả kỳ vọng | Sau khi duyệt, CB NV NHẬN được thông báo phê duyệt KQ | cbnv_hn nhận thông báo "Kết quả khóa học 'Đào tạo pháp lý Địa phương 2026' đã được phê duyệt. Mã: AAA-KH-DP" — 2 phút trước | Không |
