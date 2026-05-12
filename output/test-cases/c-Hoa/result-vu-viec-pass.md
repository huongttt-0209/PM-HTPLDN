# Test Cases PASS — vu-viec
> **Nguồn**: result-vu-viec-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | Tổng TC PASS |
|----------------|-------------:|
| 01-TC-quan-ly-vu-viec-DS | 6 |
| 07-TC-phan-cong-xac-nhan | 1 |
| **Tổng** | **7** |

## 01-TC-quan-ly-vu-viec-DS

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\vu-viec\01-TC-quan-ly-vu-viec-DS.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\vu-viec\report-01-quan-ly-vu-viec-DS\Tcs-report\01-TC-quan-ly-vu-viec-DS-execution-report-2026-05-10-round2.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|----------------------|----------|
| TC-VV-DS-101 | FR-V.I-01 AC1 | Hiển thị DS VV phân quyền theo đơn vị (CB NV TW xem toàn quốc) | `cb_nv_tw_01`. ≥20 VV thuộc nhiều đơn vị. | — | 1. Login `cb_nv_tw_01`. 2. Vào DS VV. | STATE: Backend filter is_deleted=0, không filter don_vi_id. UI: Bảng hiển thị tất cả VV. | Happy | PASS |  |
| TC-VV-DS-104 | FR-V.I-01 AC2 | Click vào dòng VV → mở SCR-V.I-03 chi tiết | `cb_nv_tw_01`. Có VV đang DANG_XU_LY. | — | 1. Click vào "Mã VV" (text link). | STATE: GET /vu-viec/{id}. UI: SCR-V.I-03 detail. | Happy | PASS |  |
| TC-VV-DS-203 | BR-EC-13 / search sanitize | XSS payload trong ô tìm kiếm | `cb_nv_tw_01`. | tu_khoa=`<script>alert('XSS-VV')</script>` | 1. Gõ XSS. 2. Click Tìm. | STATE: Sanitize. UI: No alert, no XSS execution. | Negative | PASS |  |
| TC-VV-DS-204 | BR-EC-13 / search boundary 200 | Từ khóa > 200 ký tự | `cb_nv_tw_01`. | tu_khoa = "A" × 201 | 1. Gõ 201 ký tự A. 2. Click Tìm. | STATE: Truncate hoặc reject. | Negative | PASS |  |
| TC-VV-DS-205 | BR-EC-13 / SQL LIKE escape | Từ khóa chứa `%` và `_` | `cb_nv_tw_01`. | tu_khoa = `100%`, `test_dn` | 1. Tìm với `100%`. 2. Tìm với `test_dn`. | STATE: Escape wildcards. | Negative | PASS |  |
| TC-VV-DS-206 | FR-V.I-08 / E1 INF-VV-TK-01 | UC58 Search có từ khóa 0 kết quả → INF-VV-TK-01 | `cb_nv_tw_01`. | tu_khoa="VV-NONEXIST-99999999-999" | 1. Nhập. 2. Click Tìm. | STATE: Empty. UI: INF-VV-TK-01 message. | Negative | PASS |  |

## 07-TC-phan-cong-xac-nhan

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\vu-viec\07-TC-phan-cong-xac-nhan.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\vu-viec\report-07-phan-cong-xac-nhan\Tcs-report\07-TC-phan-cong-execution-report-2026-05-10-round2.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|----------------------|----------|
| TC-VV-PC-101 | FR-V.I-09 AC1 / Cá nhân TVV | Phân công Cá nhân (TVV) → SET loai='CA_NHAN', to_chuc_tu_van_id=NULL | `cb_nv_tw_01`. VV-X ở DANG_KIEM_TRA. `tvv_01` (HOAT_DONG). | loai=CA_NHAN, nguoi_xu_ly_id=`tvv_01`, ghi_chu | 1-5. Mở modal. Cá nhân → search. Chọn. Nhập ghi chú. [Xác nhận]. | STATE: PHAN_CONG_VU_VIEC + UPDATE VV DA_PHAN_CONG + NOTIF. | Happy | PASS |  |

## Skipped

Các section sau KHÔNG có TC nào với Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}:

- **02-TC-tao-vu-viec-DN** (27 TC): toàn bộ BLOCKED do DN role yêu cầu VNeID Tier 2 OAuth, env không có VNeID stub.
- **03-TC-nhap-thu-cong-vv** (28 TC): 1 FAIL + 1 PARTIAL + 7 DEFERRED + 1 BLOCKED + 18 NOT-EXECUTED.
- **04-TC-tiep-nhan-cms-ht-khac** (16 TC): toàn bộ BLOCKED do env 0 VV kênh HE_THONG_KHAC.
- **05-TC-kiem-tra-hs** (20 TC): 1 FAIL + 1 PARTIAL + 2 BLOCKED + 16 NOT-EXECUTED.
- **06-TC-quan-ly-hs-vv** (21 TC): 1 PARTIAL + 20 NOT-EXECUTED.
- **08-TC-trinh-phe-duyet-pd** (21 TC): toàn bộ NOT-EXECUTED (chưa có Phase B execution report).
- **09-TC-cap-nhat-ket-qua** (21 TC): toàn bộ NOT-EXECUTED (chưa có Phase B execution report).
- **10-TC-danh-gia-vv** (19 TC): toàn bộ NOT-EXECUTED (chưa có Phase B execution report).
- **11-TC-cong-khai-vv** (27 TC): toàn bộ NOT-EXECUTED (chưa có Phase B execution report).
- **12-TC-DN-bo-sung-thong-bao** (29 TC): toàn bộ NOT-EXECUTED (chưa có Phase B execution report).
- **13-TC-cau-hinh-quy-trinh** (11 TC): toàn bộ NOT-EXECUTED (chưa có Phase B execution report).
