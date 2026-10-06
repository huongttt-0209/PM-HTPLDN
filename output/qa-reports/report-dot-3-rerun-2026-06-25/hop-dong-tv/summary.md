# QA bổ sung report-dot-3 — Hợp đồng tư vấn

Nguồn: `output/bao-cao-tong-hop-qa/report-dot-3.xlsx`, sheet `17. Hợp đồng tư vấn`

SRS đối chiếu: `input/srs-update-2026-5-5`

Ngày cập nhật: 2026-06-25

## Kết quả cuối sau rà soát strict

| Chỉ số | Số lượng |
|---|---:|
| FAIL cũ đã verify/rerun theo SRS mới | 44 |
| Case đổi từ FAIL sang PASS sau rerun | 8 |
| Case FAIL đã xóa qua 2 lượt trim | 29 |
| FAIL giữ lại trong report chính | 7 |
| Tổng PASS trong module | 88 |
| Tổng FAIL trong module | 7 |
| CHƯA CHẠY còn lại trong module | 2 |
| Tổng testcase còn lại trong module | 97 |

Quy ước trạng thái trong Excel: chỉ dùng `PASS`, `FAIL`, hoặc `CHƯA CHẠY` với `Lý do = Chưa tích hợp`. Các dòng `PASS`/`FAIL` để trống cột `Lý do`.

## Evidence chính

- `evidence/rerun-44-2026-06-25.json`
- `evidence/rerun-44-roles-2026-06-25.json`
- `evidence/rerun-44-unlink-audit-2026-06-25.json`
- `fail-cause-srs-audit.md`
- `fail-trim-audit-2026-06-25.md`
- `fail-strict-review-2026-06-25.md`

## FAIL giữ lại

- TC-HDTV-010 — Tên HĐ trống
- TC-HDTV-023 — Bên A auto theo đơn vị CB NV khi tạo HĐ
- TC-MTD-001 — Thêm mốc tiến độ — happy
- TC-TTGD-001 — Thêm 1 giai đoạn TT — happy
- TC-TTGD-010 — Σ giai đoạn > giá trị HĐ
- TC-HDTV-HDTK-001 — Tìm theo keyword (tên HĐ)
- TC-HDTV-HDTK-011 — Không có kết quả

## CHƯA CHẠY do chưa tích hợp

- TC-HDTV-PERM-013 — Chưa tích hợp
- TC-PERM-026 — Chưa tích hợp
