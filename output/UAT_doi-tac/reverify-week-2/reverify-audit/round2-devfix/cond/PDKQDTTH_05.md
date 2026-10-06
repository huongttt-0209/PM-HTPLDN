# Bảng đối chiếu điều kiện — PDKQDTTH_05 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò từ chối | CB Phê duyệt (cbpd_tw — CB_PD_TW) | CB Phê duyệt cùng đơn vị khóa học (cbpd_hn — CB_PD_DP, Sở Tư pháp Hà Nội) | Không |
| Trạng thái khóa tiền đề | Khóa học ở "Chờ duyệt kết quả" | Seed DDD-KH-012: Đang diễn ra → Kết thúc → Trình duyệt kết quả → "Chờ duyệt KQ" (do cbnv_hn trình) | Không |
| Thao tác | Bấm "Từ chối KQ", nhập lý do → xác nhận → khóa về "Đã kết thúc" | Bấm "Từ chối KQ" → nhập lý do 182 ký tự → "Từ chối" → toast "Đã từ chối kết quả" → khóa về "Đã kết thúc" | Không |
| Người nhận thông báo kỳ vọng | CB Nghiệp vụ (người trình duyệt kết quả) nhận thông báo kèm lý do | cbnv_hn (người trình DDD-KH-012) — kiểm chuông + trang /thong-baos | Không |
| KQ mong đợi: CB NV nhận thông báo từ chối kèm lý do (SRS FR-III-18 UC37 §Processing dòng 1261 + §Postconditions dòng 1265) | Bug gốc: KHÔNG nhận thông báo nào (suy luận từ nhánh phê duyệt PDKQDTTH_01 do không seed được khóa "Chờ duyệt KQ" thứ 2) | ✅ ĐÃ chạy trực tiếp nhánh từ chối: cbnv_hn NHẬN thông báo "Kết quả khóa học "Khóa học pháp luật doanh nghiệp seed" bị từ chối — Mã: DDD-KH-012. Lý do: Kết quả đào tạo chưa đạt yêu cầu: thiếu dữ liệu điểm danh và điểm kiểm tra... trình duyệt lại." (14/07/2026 23:35, "2 phút trước") | Không |
