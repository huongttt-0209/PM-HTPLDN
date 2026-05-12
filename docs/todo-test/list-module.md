# Danh sách module — PM HTPLDN

Nguồn: [input/srs-v3/](../../input/srs-v3/) + [input/srs-update-2026-5-5/](../../input/srs-update-2026-5-5/) (SRS v3.5).

| STT | Mã FR | Tên module | File SRS gốc (v3) | File SRS update (v3.5) |
|:-:|:-:|---|---|---|
| 1 | FR-01 | Dashboard / Tổng quan hệ thống | [srs-fr-01-dashboard.md](../../input/srs-v3/srs-fr-01-dashboard.md) | [srs-fr-01-dashboard.md](../../input/srs-update-2026-5-5/srs-fr-01-dashboard.md) |
| 2 | FR-02 | Hỏi đáp | [srs-fr-02-hoi-dap.md](../../input/srs-v3/srs-fr-02-hoi-dap.md) | [srs-fr-02-hoi-dap.md](../../input/srs-update-2026-5-5/srs-fr-02-hoi-dap.md) |
| 3 | FR-03 | Đào tạo | [srs-fr-03-dao-tao.md](../../input/srs-v3/srs-fr-03-dao-tao.md) | [srs-fr-03-dao-tao.md](../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md) |
| 4 | FR-04 | Chuyên gia / Tư vấn viên (CG/TVV) | [srs-fr-04-chuyen-gia-tvv.md](../../input/srs-v3/srs-fr-04-chuyen-gia-tvv.md) | [srs-fr-04-chuyen-gia-tvv.md](../../input/srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md) |
| 5 | FR-05 | Vụ việc | [srs-fr-05-vu-viec.md](../../input/srs-v3/srs-fr-05-vu-viec.md) | [srs-fr-05-vu-viec.md](../../input/srs-update-2026-5-5/srs-fr-05-vu-viec.md) |
| 6 | FR-06 | Chi trả | [srs-fr-06-chi-tra.md](../../input/srs-v3/srs-fr-06-chi-tra.md) | [srs-fr-06-chi-tra.md](../../input/srs-update-2026-5-5/srs-fr-06-chi-tra.md) |
| 7 | FR-07 | Doanh nghiệp | [srs-fr-07-doanh-nghiep.md](../../input/srs-v3/srs-fr-07-doanh-nghiep.md) | [srs-fr-07-doanh-nghiep.md](../../input/srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md) |
| 8 | FR-08 | Đánh giá | [srs-fr-08-danh-gia.md](../../input/srs-v3/srs-fr-08-danh-gia.md) | [srs-fr-08-danh-gia.md](../../input/srs-update-2026-5-5/srs-fr-08-danh-gia.md) |
| 9 | FR-09 | Biểu mẫu | [srs-fr-09-bieu-mau.md](../../input/srs-v3/srs-fr-09-bieu-mau.md) | [srs-fr-09-bieu-mau.md](../../input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md) |
| 10 | FR-10 | Quản trị hệ thống (QTHT) | [srs-fr-10-quan-tri.md](../../input/srs-v3/srs-fr-10-quan-tri.md) | [srs-fr-10-quan-tri.md](../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md) |
| 11 | FR-11 | Báo cáo | [srs-fr-11-bao-cao.md](../../input/srs-v3/srs-fr-11-bao-cao.md) | _(không có update v3.5)_ |
| 12 | FR-12 | Tư vấn chuyên sâu (TVCS) | [srs-fr-12-tv-chuyen-sau.md](../../input/srs-v3/srs-fr-12-tv-chuyen-sau.md) | [srs-fr-12-tv-chuyen-sau.md](../../input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md) |
| 13 | FR-13 | Tư vấn nhanh (TVN) | [srs-fr-13-tv-nhanh.md](../../input/srs-v3/srs-fr-13-tv-nhanh.md) | [srs-fr-13-tv-nhanh.md](../../input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md) |
| 14 | FR-14 | Hợp đồng tư vấn (HĐTV) | [srs-fr-14-hop-dong-tv.md](../../input/srs-v3/srs-fr-14-hop-dong-tv.md) | _(không có update v3.5)_ |
| 15 | FR-15 | Chương trình HTPLDN | [srs-fr-15-ct-htpldn.md](../../input/srs-v3/srs-fr-15-ct-htpldn.md) | _(không có update v3.5)_ |
| 16 | FR-16 | API / Tích hợp | [srs-fr-16-api.md](../../input/srs-v3/srs-fr-16-api.md) | _(không có update v3.5)_ |

## Module cross-cutting / phụ trợ

| Nhóm | Tên | File SRS |
|---|---|---|
| Hồ sơ cá nhân | Hồ sơ + đổi mật khẩu | [ho-so-doi-mat-khau.md](../../input/srs-update-2026-5-5/ho-so-doi-mat-khau.md) |
| Cross-cutting | Permission matrix + state machine | [_DELTA-MAP-CROSS-CUTTING.md](../../input/srs-update-2026-5-5/_DELTA-MAP-CROSS-CUTTING.md) |

## Ghi chú

- Tổng **16 module FR** chính + **2 nhóm phụ trợ** (hồ sơ/đổi mật khẩu, cross-cutting permission).
- SRS update batch 2026-05-05 đụng **11/16 module** (FR-01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 12, 13). FR-11/14/15/16 KHÔNG có file update v3.5 → giữ nguyên v3.
- State machine + thứ tự seed: xem [input/flow-module.md](../../input/flow-module.md) + [input/data/entity-map.md](../../input/data/entity-map.md).
- Phân nhóm test theo SRS update (A FULL / B DELTA+IMPACT / C IMPACT / D SKIP): xem [tasks/todo.md](../../tasks/todo.md) round hiện tại.
