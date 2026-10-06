# Bảng đối chiếu điều kiện — QLHSTVV_05 (re-verify sau dev fix, 2026-07-15)

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | NHT (Người hỗ trợ pháp lý) — `nht_qa_tw`, đơn vị Cục Bổ trợ tư pháp | NHT — `nht_qa_tw`, banner "QA NHT Trung uong / NHT" | Không |
| Entity + trạng thái | TVV **Mới đăng ký** (bug: TVV-BTP-TW-0003); ghi chú bug còn thấy tab (disabled) ở TVV Đang hoạt động | TVV-BTP-TW-0009 (**Mới đăng ký**, cùng đơn vị) + kiểm chéo TVV-BTP-TW-0002 (**Đang hoạt động**) | Không |
| Màn hình | Màn Chi tiết TVV → quan sát thanh thẻ | Đúng màn, quan sát thanh thẻ | Không |
| Thao tác kiểm | Thẻ "Thẩm định" có hiển thị / mở được với vai trò NHT không | Cả 2 trạng thái: thanh thẻ = [Hồ sơ, Năng lực, Lịch sử hỗ trợ, Đánh giá] — **KHÔNG có thẻ "Thẩm định"** (ẩn hoàn toàn); DOM `hasThamDinhTab=false` | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix**. Với vai trò NHT, thẻ "Thẩm định" bị ẩn hoàn toàn ở cả TVV "Mới đăng ký" (không còn mở được form chấm điểm) lẫn TVV "Đang hoạt động" (không còn hiện dạng disabled). Thẻ vẫn hiển thị đúng cho vai trò CB Nghiệp vụ (đã quan sát khi đăng nhập cbnv_tw).
