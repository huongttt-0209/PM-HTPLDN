# Audit QLHSDNHTCP_04 — Số đếm trên thẻ phân loại trạng thái

- **Verdict:** Reject (ghi sheet row 17, P17, 2026-07-20).
- **Tài khoản:** cbnv_tw (CB_NV_TW), env 18.143.165.120, data 10 hồ sơ CT-SEED-101→110.

## Cổng 1 — Evidence đối tác
- `partner-evidence/QLHSDNHTCP_04.jpg` (ospgroup.vn, 07-10). Thẻ "Tất cả / Chờ xử lý / Đang đánh giá / Chờ phê duyệt / Đã xử lý" KHÔNG có số đếm dù có 5 hồ sơ.

## Cổng 3 — SRS vs Web
- SRS SCR-V.II-01 component #3 (`srs-fr-06-chi-tra.md:922`): "5 tab phân loại trạng thái ... **Số đếm trên mỗi tab**".
- Web hiện tại: thẻ hiển thị số đếm — Tất cả 10, Chờ xử lý 3, Đang đánh giá 2, Chờ phê duyệt 1, Đã xử lý 4 (DOM confirm + khớp API `meta.tabCounts`). Screenshot: `QLHSDNHTCP_04-web-tab-so-dem.png`.

## Kết luận
- Build hiện tại hiển thị số đếm ĐÚNG theo SRS. Lỗi đối tác báo (thiếu số đếm, build cũ) **không tái hiện** → **Reject**. Bảng điều kiện 0 GAP (`condition-table.md`): cùng vai trò + đều có data.
