# Bảng đối chiếu điều kiện — QLHSTVV_06 (re-verify sau dev fix, 2026-07-15)

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — `cbnv_tw` | CB_NV_TW — `cbnv_tw`, banner BTP·TW | Không |
| Entity + trạng thái | TVV-BTP-TW-0002 (Đang hoạt động) có Bằng cấp + Chứng chỉ chi tiết đã lưu | TVV-BTP-TW-0002 — Bằng cấp (Dai hoc Luat Ha Noi / Luat Kinh te / 2010) + Chứng chỉ (Chung chi hanh nghe Luat su / Bo Tu phap / 15-03-2012) đã lưu | Không |
| Màn hình | Màn Chi tiết TVV → thẻ "Năng lực" | Đúng màn, thẻ "Năng lực" | Không |
| Thao tác kiểm | Xem cách hiển thị trường "Bằng cấp" + "Chứng chỉ" | Bằng cấp = "Luat Kinh te — Dai hoc Luat Ha Noi — Năm tốt nghiệp 2010" (định dạng đúng, KHÔNG còn JSON thô); Chứng chỉ = "Chung chi hanh nghe Luat su — Bo Tu phap — cấp 15/03/2012" (hiển thị, KHÔNG còn "—") | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix**. Thẻ "Năng lực" hiển thị Bằng cấp theo định dạng đọc được (tên trường / chuyên ngành / năm tốt nghiệp) thay vì JSON thô; Chứng chỉ hiển thị đúng dữ liệu đã lưu thay vì "—".
