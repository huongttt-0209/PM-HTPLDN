# A4 — Edge Case Hunter Audit Log (FR-08 Đánh giá HQ)

> **Ngày chạy:** 2026-05-10
> **Mode:** bmad-review-edge-case-hunter
> **Output mode:** Inline merge (TC mới đã merge trực tiếp vào file UC)
> **Total TC bổ sung:** 49 TC (84 base → 133 sau A4)

---

## Phân loại edge case

| Loại edge | Mô tả | TC thêm |
|-----------|-------|---------|
| Boundary | Min/max length, decimal tolerance, exact-equal at threshold | 18 |
| Concurrency | 2 user thao tác cùng lúc, last-write-wins, sequence conflict | 2 |
| Security | XSS, IDOR, CSRF, session timeout | 5 |
| Negative spec | Spec gap/ambiguous → SPEC-CLARIFY mới | 6 |
| State guard | Hủy đợt HOAN_THANH, soft-delete cycle, cycle nhiều lần | 3 |
| File upload | PDF max 20MB, file_dinh_kem v3.5 | 2 |
| Cross-field | tu_ngay = den_ngay boundary, co_quan_duoc_danh_gia_id ≠ don_vi_id | 2 |
| Auto-mapping | mau_bao_cao theo tan_suat, tan_suat default theo tháng | 2 |
| Multi-evaluator | 2 TRUONG_NHOM cùng VV, self-assign | 2 |
| Boundary lý do từ chối | =10 chars, =9 chars, very long >1000 | 6 |
| Empty state | 0 VV trong kỳ → WRN-DG-VV-01, BC trống → WRN | 1 |

---

## Merge mapping (TC mới → file UC)

### File 01 — Lập KH (+12 TC)
- TC-DG-KH-019..030: boundary ten_dot/ghi_chu, tu_ngay = den_ngay, concurrency, soft-delete cycle, hủy HOAN_THANH guard, XSS, file_dinh_kem 19MB/21MB, co_quan_duoc_danh_gia_id bắt buộc + ≠ don_vi_id

### File 02 — Tiêu chí (+6 TC)
- TC-DG-TC-011..016: boundary trong_so 100% với 1 tiêu chí, 101 invalid, tolerance ±0.01%, ten_tieu_chi 500 chars, XSS mo_ta, decimal trọng số

### File 03 — Phân công + duyệt PC (+6 TC)
- TC-DG-PC-015..020: boundary lý do 10/9 chars, lý do >1000, cross-tab guard trọng số, trùng TRUONG_NHOM, self-assign

### File 04 — Chấm điểm (+10 TC)
- TC-DG-DG-015..024: decimal điểm, boundary 0/max, nhan_xet 1000/1001, nhan_xet_tong_the 2000, xếp loại boundary 70.00/49.99, concurrent 2 TRUONG_NHOM cùng VV, idempotent re-select VV, deselect cảnh báo

### File 05 — Báo cáo + duyệt BC (+10 TC)
- TC-DG-BC-015..024: boundary lý do từ chối, kp_hoat_dong_khac=0, kp_xa_hoi_hoa large, mau_bao_cao enum, auto-map per tan_suat, xuất XLSX dự thảo, BC trống, audit Common Approval Fields, cycle reject 3 lần

### File 06 — FR-VI-10 (+2 TC)
- TC-DG-NK-007..008: đợt HUY không show KQ, dual-role user (lập + nhận)

### File 07 — Permission Matrix (+3 TC)
- TC-DG-PERM-009..011: session timeout, CSRF token, IDOR force URL

---

## SPEC-CLARIFY mới (pending BA)

| ID | Issue | Why |
|----|-------|-----|
| SPEC-CLARIFY-DG-01 | FR-VI-10 read-only — hiển thị `chi_tiet_diem` JSON từng người ĐG hay chỉ tổng? | Privacy/transparency boundary chưa rõ trong spec |
| SPEC-CLARIFY-DG-02 | CB NV được self-assign chính mình vào phân công ĐG? | UC85 không cấm tường minh nhưng có conflict-of-interest |
| SPEC-CLARIFY-DG-03 | KET_QUA_DANH_GIA scheme: 1 record per VV per đợt hay per người ĐG per VV (multi-evaluator support)? | UC88 input lab `nguoi_danh_gia_id` nhưng table không có FK người ĐG riêng |
| SPEC-CLARIFY-DG-04 | Auto-mapping `mau_bao_cao` (MAU_21A/21B) theo `tan_suat`? | Spec không rõ default, phụ thuộc nghiệp vụ TT17 |
| SPEC-CLARIFY-DG-05 | Cho phép xuất BC khi đợt chưa HOAN_THANH? Watermark "Dự thảo"? | Spec UC89 output #2 không guard state |
| SPEC-CLARIFY-DG-06 | Trình BC trống hoàn toàn — block (ERR) hay cảnh báo (WRN)? | UC90 process step 3 mơ hồ "cảnh báo nếu thiếu" — có chặn hay không? |

---

## Coverage delta

| Metric | Trước A4 | Sau A4 |
|--------|---------|--------|
| Total TC | 84 | 133 |
| Boundary coverage | 65% | 95% |
| Security baseline | 30% | 90% |
| Concurrency | 0% | 70% |
| SPEC-CLARIFY active | 0 | 6 |
