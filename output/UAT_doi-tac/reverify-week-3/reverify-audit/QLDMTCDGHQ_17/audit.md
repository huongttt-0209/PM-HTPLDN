# Audit — QLDMTCDGHQ_17 (row 159) — Reject

**Verdict:** Reject. Verify 21/07/2026, Chrome DevTools MCP, `admin`/QTHT, env `18.143.165.120.nip.io`.

## Evidence đối tác đã xem
- File: `partner-evidence/QLDMTCDGHQ_17.webm` (env `htpldn-uat.ospgroup.vn`, clock 14/07/2026).
- Frame lỗi: `frames-QLDMTCDGHQ_17/t004.02s.jpg` + `t006.04s.jpg` — page 2 active, footer "21-21 / 21 mục" (đáng lẽ chỉ 1 record) NHƯNG bảng vẫn hiện ~20 record của trang 1 (TC-PL, TC-NL, TC-HQ, 9, 8, 7...). Tức click sang trang 2 → footer + page indicator đổi, bảng KHÔNG reload dữ liệu trang 2 → build cũ.
- t000: page 1 "1-20 / 21 mục", 21 record (nhiều junk seed: "1dsdsdsdsd", tên "1"/"2"), tổng trọng số 150%.

## Đối tác phản ánh
Lỗi phân trang khi tổng > 20 record.

## Kết quả verify web hiện tại (real-data)
- Env ban đầu chỉ 1 record → TỰ SEED 22 record (QTHTB6TC01-22, POST /api/v1/danh-muc, trọng số 1) → tổng 23 record, cảnh báo "Tổng trọng số: 122%" (khớp behavior 150% của đối tác).
- Trang 1: 20 record (QTHTB2TCHQ…QTHTB6TC19), "1-20 / 23 mục". `page1.png`.
- Trang 2: đúng 3 record (TC20, TC21, TC22), "21-23 / 23 mục", KHÔNG lặp trang 1, overlap rỗng. `page2.png`.
- Round-trip về trang 1: đúng 20 record lại. Bảng re-render đúng.
- Backend API `?page=2` trả 3 record riêng (total 23, totalPages 2).
- Dọn seed sau test: xóa 22 record → về 1 record (100%).

## SRS line
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:91` — phân trang mặc định 20/trang, tối đa 100/trang.
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1607` — SCR-VIII-01 §Quy tắc tương tác: phân trang 20 mục/trang.

## Kết luận
Phân trang hiện tại đúng SRS (20/trang), page 2 render đúng record trang 2, text từ-đến-tổng đúng, không trùng/sai đếm. Lỗi đối tác báo KHÔNG tái hiện — nghi build cũ. → Reject, đối tác kiểm tra lại.
