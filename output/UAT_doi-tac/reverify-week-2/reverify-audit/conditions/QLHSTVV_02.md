# Bảng đối chiếu điều kiện — QLHSTVV_02 (thẻ giới thiệu TVV ở đầu trang Chi tiết)

Evidence đối tác: partner-evidence/QLHSTVV_02.jpg (full-res).

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — "Cán bộ NV Trung ương", badge CB_NV_TW, đơn vị BTP·TW | CB_NV_TW — `cbnv_tw`, badge CB_NV_TW, đơn vị Cục Bổ trợ tư pháp - BTP (TW) | Không |
| Entity + trạng thái | TVV `TVV-BTP-TW-0030` (huongcg) — Đang hoạt động, ĐÃ công khai (header có nút "Hủy công khai") | Test 2 TVV: TVV-BTP-TW-0002 (Đang hoạt động, chưa công khai) + TVV-SEED-0001 (Đang hoạt động, ĐÃ công khai — header có nút "Hủy công khai", khớp đối tác). Thẻ đầu trang giống nhau ở cả 2 ⇒ trạng thái công khai không đổi kết quả | Không |
| Dữ liệu tiền đề | TVV có Loại, có Ngày công nhận; các trường Tổ chức/Lĩnh vực nằm trong hồ sơ | TVV-BTP-TW-0002 CÓ đủ dữ liệu 3 trường tranh chấp: Loại = Tư vấn viên, Tổ chức chính = Trung tâm Tư vấn Pháp luật Seed, Lĩnh vực = Thương mại (kiểm qua API + thẻ Hồ sơ) ⇒ thiếu là do màn không render, không phải thiếu dữ liệu | Không |
| Input / màn hình | Màn Chi tiết TVV `/chuyen-gia-tvv/:id`, vùng thẻ giới thiệu đầu trang | Màn Chi tiết TVV `/chuyen-gia-tvv/:id`, vùng thẻ giới thiệu đầu trang (cùng màn) | Không |

Kết luận: 0 GAP — tái hiện đúng: thẻ đầu trang KHÔNG hiển thị Loại / Tổ chức tư vấn / Lĩnh vực pháp luật (dù dữ liệu có đủ).
Đối chiếu SRS: SCR-IV-03 cell 3 (srs-fr-04-chuyen-gia-tvv.md dòng 1541) quy định thẻ thông tin chính gồm: Ảnh chân dung + Họ tên + Mã TVV + Trạng thái (badge) + Điểm đánh giá TB + Ngày công nhận — KHÔNG có Loại / Tổ chức / Lĩnh vực. Web đúng SRS; kỳ vọng đối tác lấy từ bản thiết kế → cần BA chốt.
