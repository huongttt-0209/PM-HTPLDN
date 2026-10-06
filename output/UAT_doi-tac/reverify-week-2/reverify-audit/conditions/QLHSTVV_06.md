# Bảng đối chiếu điều kiện — QLHSTVV_06 (chuyển thẻ nội dung: lỗi Bằng cấp + thiếu số đếm)

Evidence đối tác: partner-evidence/QLHSTVV_06.webm — frame 00:04 thẻ "Năng lực" của TVV-BTP-TW-0032, trường "Bằng cấp" in JSON thô `{"tenTruong":"Đại học Bách Khoa","chuyenNganh":"CNTT","namTotNghiep":2000}`; frame 00:08 thẻ "Đánh giá" có 2 đánh giá (8.3/10) nhưng tên thẻ không có số đếm; frame 00:14 thiết kế yêu cầu thẻ "Lịch sử hỗ trợ" và "Đánh giá" hiển thị số đếm bản ghi cạnh tên thẻ.

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — "Cán bộ NV Trung ương", banner BTP·TW | CB_NV_TW — `cbnv_tw`, banner BTP·TW, cùng đơn vị TVV | Không |
| Entity + trạng thái | TVV `TVV-BTP-TW-0032` — Đang hoạt động | TVV `TVV-BTP-TW-0002` — Đang hoạt động (trùng state) | Không |
| Dữ liệu tiền đề (ý 1 — Bằng cấp) | TVV CÓ dữ liệu Bằng cấp chi tiết (Đại học Bách Khoa / CNTT / 2000) | Đã seed Bằng cấp chi tiết qua màn Sửa hồ sơ (Dai hoc Luat Ha Noi / Luat Kinh te / 2010) + Chứng chỉ chi tiết (Chung chi hanh nghe Luat su / 15-03-2012 / Bo Tu phap) — xác nhận đã lưu qua API `hoSo.bangCapChiTiet`, `hoSo.chungChiChiTiet` | Không |
| Dữ liệu tiền đề (ý 2 — số đếm) | TVV CÓ 2 đánh giá (8.3/10, "(2 đánh giá)") | Đã seed 1 đánh giá thật qua nút "Gửi đánh giá" (4 sao × 3 tiêu chí) → thẻ Đánh giá hiển thị "(1 đánh giá)", header hiện 4.0/5 ⇒ TVV thực sự CÓ bản ghi để đếm | Không |
| Input / màn hình | Màn Chi tiết TVV → chuyển giữa 5 thẻ | Màn Chi tiết TVV → chuyển giữa 5 thẻ (cùng thao tác) | Không |

Kết luận: 0 GAP.
- Ý 1 (Open): thẻ Năng lực in "Bằng cấp" dưới dạng JSON thô; "Chứng chỉ" hiển thị "—" dù DB đã có chungChiChiTiet. Sai SRS: SCR-IV-03 dòng 1566 (thẻ Năng lực gồm Bằng cấp chi tiết / Chứng chỉ chi tiết) + SCR-IV-02 dòng 1498-1499 (bằng cấp/chứng chỉ chi tiết là bảng lặp dòng: tên trường, năm tốt nghiệp, chuyên ngành / tên chứng chỉ, ngày cấp, nơi cấp).
- Ý 2 (BA confirm): tên thẻ "Lịch sử hỗ trợ" và "Đánh giá" không có số đếm bản ghi — SRS SCR-IV-03 cell 22/23 (dòng 1567, 1570) chỉ quy định thống kê BÊN TRONG thẻ ("Tổng vụ việc: {N}", "({N} đánh giá)"), KHÔNG quy định số đếm cạnh tên thẻ. Kỳ vọng này đến từ bản thiết kế → BA chốt.
