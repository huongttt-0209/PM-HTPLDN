# Rà soát strict 17 FAIL — Hợp đồng tư vấn

Nguyên tắc giữ FAIL: SRS 3.5 yêu cầu rõ, evidence rerun chứng minh sai, và case có giá trị nghiệm thu riêng.

## Kết quả

- Xóa thêm: 10 case FAIL
- Giữ lại: 7 case FAIL
- Tổng module: PASS 88, FAIL 7, CHƯA CHẠY 2, total 97

## Case FAIL xóa thêm

- TC-HDTV-028 — Xuất Excel HĐ tư vấn theo scope đơn vị user
- TC-MTD-010 — ten_moc trống
- TC-MTD-011 — ngay_du_kien trống
- TC-MTD-022 — Trạng thái mốc enum invalid — UI restrict
- TC-TTGD-011 — so_tien ≤ 0
- TC-TTGD-012 — giai_doan trống
- TC-TTGD-020 — Tất cả GĐ DA_THANH_TOAN, Σ=gia_tri → 100%
- TC-HDTV-HDTK-003 — Lọc HĐ theo khoảng thời gian trong ngữ cảnh SRS 3.5
- TC-HDTV-HDTK-021 — Combine keyword + TVV + khoảng ngày theo AND logic
- TC-HDTK-024 — Keyword chứa SQL injection payload — sanitize

## Case FAIL giữ lại

- TC-HDTV-010 — Tên HĐ trống
- TC-HDTV-023 — Bên A auto theo đơn vị CB NV khi tạo HĐ
- TC-MTD-001 — Thêm mốc tiến độ — happy
- TC-TTGD-001 — Thêm 1 giai đoạn TT — happy
- TC-TTGD-010 — Σ giai đoạn > giá trị HĐ
- TC-HDTV-HDTK-001 — Tìm theo keyword (tên HĐ)
- TC-HDTV-HDTK-011 — Không có kết quả
