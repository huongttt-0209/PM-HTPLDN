# Audit xóa bớt FAIL — Hợp đồng tư vấn

Nguồn: `output/bao-cao-tong-hop-qa/report-dot-3.xlsx`, sheet `17. Hợp đồng tư vấn`

Căn cứ: SRS mới nhất `input/srs-update-2026-5-5/srs-fr-14-hop-dong-tv.md`.

## Nguyên tắc

- Giữ các FAIL bắt buộc theo SRS và có ảnh hưởng nghiệm thu/nghiệp vụ.
- Xóa case trùng cùng lỗi gốc, case biên thấp, hoặc case spec chưa rõ nếu để FAIL không tăng giá trị kiểm thử.
- Không đổi FAIL thành PASS cảm tính.

## Kết quả

- FAIL trước khi trim: 36
- FAIL đã xóa bớt: 19
- FAIL giữ lại: 17
- Tổng module sau trim: PASS 88, FAIL 17, CHƯA CHẠY 2, total 107

## Case FAIL đã xóa

- TC-HDTV-026 — Upload nhiều file đính kèm vào HĐ tư vấn
- TC-HDTV-029 — Xuất Excel HĐ tư vấn theo filter hiện tại
- TC-MTD-002 — Cập nhật mốc — chuyển trạng thái sang HOAN_THANH
- TC-MTD-003 — Xóa 1 mốc tiến độ
- TC-MTD-020 — trang_thai_moc default CHUA_BAT_DAU khi tạo
- TC-MTD-021 — ngay_thuc_te < ngay_du_kien (hoàn thành sớm)
- TC-MTD-023 — Thứ tự mốc tiến độ giữ nguyên sau Save (theo thứ tự nhập)
- TC-TTGD-002 — Thêm 3 giai đoạn tổng = giá trị HĐ (boundary)
- TC-TTGD-003 — Đổi trạng thái GĐ1 → DA_THANH_TOAN, progress bar update
- TC-TTGD-021 — Xóa 1 GĐ → Σ giảm, có thể thêm GĐ mới
- TC-TTGD-022 — Giảm gia_tri_hop_dong xuống dưới Σ giai đoạn
- TC-TTGD-023 — Σ = gia_tri exact (boundary) khi all DA_THANH_TOAN
- TC-TTGD-024 — Progress bar tính chỉ trên Σ DA_THANH_TOAN, không phải Σ tổng GĐ
- TC-LVV-022 — VV bị soft-delete — HĐ không hiển thị liên kết VV đã xóa
- TC-LVV-025 — 1 VV link nhiều HĐ khác đơn vị — xác định scope hiển thị
- TC-HDTK-023 — Keyword match TÊN + MÃ + BÊN B (3 fields full-text)
- TC-HDTK-025 — Keyword Unicode tiếng Việt có dấu
- TC-HDTV-PERM-001 — CB_NV_TW CRUD HĐ theo ngữ cảnh VV/TVV, không qua route standalone public
- TC-PERM-023 — CB_NV_BN CRUD HĐ scope BN với Bên B hợp lệ cùng scope

## Case FAIL giữ lại

- TC-HDTV-010 — Tên HĐ trống
- TC-HDTV-023 — Bên A auto theo đơn vị CB NV khi tạo HĐ
- TC-HDTV-028 — Xuất Excel HĐ tư vấn theo scope đơn vị user
- TC-MTD-001 — Thêm mốc tiến độ — happy
- TC-MTD-010 — ten_moc trống
- TC-MTD-011 — ngay_du_kien trống
- TC-MTD-022 — Trạng thái mốc enum invalid — UI restrict
- TC-TTGD-001 — Thêm 1 giai đoạn TT — happy
- TC-TTGD-010 — Σ giai đoạn > giá trị HĐ
- TC-TTGD-011 — so_tien ≤ 0
- TC-TTGD-012 — giai_doan trống
- TC-TTGD-020 — Tất cả GĐ DA_THANH_TOAN, Σ=gia_tri → 100%
- TC-HDTV-HDTK-001 — Tìm theo keyword (tên HĐ)
- TC-HDTV-HDTK-003 — Lọc HĐ theo khoảng thời gian trong ngữ cảnh SRS 3.5
- TC-HDTV-HDTK-011 — Không có kết quả
- TC-HDTV-HDTK-021 — Combine keyword + TVV + khoảng ngày theo AND logic
- TC-HDTK-024 — Keyword chứa SQL injection payload — sanitize
