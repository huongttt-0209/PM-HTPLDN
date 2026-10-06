# Bảng đối chiếu điều kiện — QLHSTVV_05 (thẻ "Thẩm định" phải ẩn với Người hỗ trợ)

Evidence đối tác: partner-evidence/QLHSTVV_05.jpg (full-res) — banner "hương 3 NHT / NHT", TVV-STP-HN-0003 (Đào Minh Quân), trạng thái "Mới đăng ký", thẻ "Thẩm định" đang ACTIVE và hiển thị form chấm điểm Nhóm 1 — Pháp lý.

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | NHT (Người hỗ trợ pháp lý) — "hương 3 NHT", badge NHT | NHT — `nht_qa_tw` (tự tạo qua admin), badge NHT, TVV cùng đơn vị | Không |
| Entity + trạng thái | TVV `TVV-STP-HN-0003` — trạng thái **Mới đăng ký** | TVV `TVV-BTP-TW-0003` — trạng thái **Mới đăng ký** (trùng state đối tác); kiểm chéo thêm TVV Đang hoạt động | Không |
| Dữ liệu tiền đề | TVV chưa thẩm định (Chưa có đánh giá, Ngày công nhận —) | TVV mới seed, chưa thẩm định (Chưa có đánh giá, Ngày công nhận —) — tương đương | Không |
| Input / màn hình | Màn Chi tiết TVV → bấm vào thẻ "Thẩm định" | Màn Chi tiết TVV → bấm vào thẻ "Thẩm định" (cùng thao tác) | Không |

Kết luận: 0 GAP — tái hiện đúng: với vai trò NHT, thẻ "Thẩm định" KHÔNG bị ẩn; ở TVV trạng thái Mới đăng ký thẻ này còn mở được và hiện đầy đủ form chấm điểm 4 nhóm + Kết luận thẩm định (nội dung nội bộ).
Đối chiếu SRS: SCR-IV-03 cell 13 (srs-fr-04-chuyen-gia-tvv.md dòng 1555) — Điều kiện hiển thị thẻ "Thẩm định": vai trò = Cán bộ Nghiệp vụ HOẶC Cán bộ Phê duyệt cùng đơn vị, VÀ trạng thái ∈ {Đang thẩm định, Chờ phê duyệt}. Vai trò NHT không thuộc danh sách ⇒ phải ẩn. Trạng thái Mới đăng ký cũng không thuộc danh sách.
