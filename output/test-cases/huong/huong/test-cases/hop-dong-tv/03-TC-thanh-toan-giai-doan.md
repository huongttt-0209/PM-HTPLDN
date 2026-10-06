# Test Cases — FR-X.3-01 (UC159): Thanh toán giai đoạn HĐ tư vấn

> **SRS Ref**: FR-X.3-01, SCR-X3-01 row#9 (Accordion "Thanh toán giai đoạn"), Entity HOP_DONG_TU_VAN.thanh_toan_giai_doan (JSON array)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Inline-edit table. Ràng buộc nghiệp vụ chính: **Σ so_tien giai đoạn ≤ gia_tri_hop_dong** (E3 ERR-HDTV-03). Trạng thái 2 giá trị: CHUA_THANH_TOAN / DA_THANH_TOAN. Progress bar % trên đầu accordion.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-X.3-01 / Thanh toán giai đoạn`
- **Pre-conditions mặc định**: cb_nv_tw_01 login, HĐ "HDTV-pay-01" gia_tri_hop_dong=100_000_000, đang Form Sửa.

---

## Trường input (Thanh toán giai đoạn — Accordion 4)

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hop_dong_id | Y (auto) | identifier | FK → HOP_DONG_TU_VAN |
| 2 | giai_doan | Y | text | — |
| 3 | so_tien | Y | money | > 0 |
| 4 | ngay_thanh_toan | N | date | — |
| 5 | trang_thai_tt | Y | enum | CHUA_THANH_TOAN / DA_THANH_TOAN (default CHUA_THANH_TOAN) |

**Ràng buộc tổng:** `SUM(so_tien) ≤ gia_tri_hop_dong` (Processing step 4, E3).

---

## A. THANH TOÁN — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-TTGD-001 | FR-X.3-01 / TT step 4-5 | Thêm 1 giai đoạn TT — happy | Form Sửa HĐ gia_tri=100tr, accordion TT rỗng. | giai_doan="GĐ1", so_tien=30_000_000, trang_thai_tt=CHUA_THANH_TOAN | 1. Mở accordion "Thanh toán giai đoạn". 2. [+ Thêm giai đoạn]. 3. Inline-edit nhập + Save row. 4. [Lưu] HĐ. | (1) JSON array `thanh_toan_giai_doan` thêm 1 entry. (2) Progress bar = 0% (chưa thanh toán). (3) Audit UPDATE. | Happy 🔴 |
| TC-TTGD-002 | FR-X.3-01 / Σ ≤ giá trị | Thêm 3 giai đoạn tổng = giá trị HĐ (boundary) | Form Sửa HĐ gia_tri=100tr. | GĐ1=30tr, GĐ2=40tr, GĐ3=30tr (Σ=100tr) | 1. Thêm 3 giai đoạn lần lượt + Save row mỗi lần. 2. [Lưu] HĐ. | (1) Σ=100tr = gia_tri (boundary inclusive PASS). (2) HĐ lưu OK. | Happy 🔴 |
| TC-TTGD-003 | FR-X.3-01 / progress bar | Đổi trạng thái GĐ1 → DA_THANH_TOAN, progress bar update | HĐ có 3 GĐ tổng=100tr (=gia_tri), GĐ1=30tr CHUA_THANH_TOAN. | trang_thai_tt=DA_THANH_TOAN, ngay_thanh_toan=2026-07-01 | 1. Inline-edit GĐ1: đổi trạng thái + ngày TT. 2. [Lưu] HĐ. | (1) JSON entry update. (2) Progress bar = 30% (30tr/100tr). (3) Cột "Tiến độ TT" trên list = 30%. | Happy 🟡 |

---

## B. THANH TOÁN — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-TTGD-010 | FR-X.3-01 / E3 ERR-HDTV-03 | Σ giai đoạn > giá trị HĐ | Form Sửa HĐ gia_tri=100tr. | GĐ1=60tr, GĐ2=50tr (Σ=110tr > 100tr) | 1. Thêm GĐ1+GĐ2. 2. [Lưu] HĐ. | (1) Reject: **"Tổng thanh toán vượt giá trị hợp đồng"** (ERR-HDTV-03). (2) HĐ KHÔNG lưu (hoặc reject ngay tại Save row thứ 2). | Negative 🔴 |
| TC-TTGD-011 | FR-X.3-01 / TT Inputs#3 | so_tien ≤ 0 | Form Sửa HĐ. | so_tien=0 | 1. Thêm GĐ với so_tien=0. 2. Save. | (1) Reject: "Số tiền phải lớn hơn 0" hoặc UI block. | Negative 🟡 |
| TC-TTGD-012 | FR-X.3-01 / TT Inputs#2 | giai_doan trống | Form Sửa HĐ. | giai_doan="" | 1. Thêm GĐ bỏ trống tên. 2. Save row. | Inline error "Giai đoạn là bắt buộc". | Negative 🟡 |

---

## C. THANH TOÁN — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-TTGD-020 | FR-X.3-01 / progress bar 100% | Tất cả GĐ DA_THANH_TOAN, Σ=gia_tri → 100% | HĐ 3 GĐ tổng=gia_tri=100tr, all CHUA_THANH_TOAN. | All trang_thai_tt=DA_THANH_TOAN | 1. Đổi 3 GĐ sang DA_THANH_TOAN. 2. [Lưu]. | (1) Progress bar = 100%. (2) Cột "Tiến độ TT" hiển thị 100%. | Edge 🟡 |
| TC-TTGD-021 | FR-X.3-01 / Σ giảm sau xóa GĐ | Xóa 1 GĐ → Σ giảm, có thể thêm GĐ mới | HĐ gia_tri=100tr, đã có GĐ1=100tr. | Xóa GĐ1, thêm GĐ2=80tr | 1. Xóa GĐ1 (Σ=0). 2. Thêm GĐ2=80tr. 3. [Lưu]. | (1) JSON array có 1 entry GĐ2=80tr. (2) Σ=80tr ≤ 100tr OK. | Edge 🟡 |
| TC-TTGD-022 | FR-X.3-01 / Σ + sửa giá trị HĐ (A4 merged) | Giảm gia_tri_hop_dong xuống dưới Σ giai đoạn | HĐ gia_tri=100tr, GĐ1=30tr+GĐ2=40tr=70tr Σ. | Sửa gia_tri = 60tr (< 70tr) | 1. Form Sửa HĐ. 2. Đổi giá trị HĐ từ 100tr → 60tr. 3. [Lưu]. | (1) Reject ERR-HDTV-03: "Tổng thanh toán (70tr) vượt giá trị hợp đồng (60tr)". (2) HĐ KHÔNG cập nhật. | Edge 🔴 |
| TC-TTGD-023 | FR-X.3-01 / Σ Edge boundary (A4 merged) | Σ = gia_tri exact (boundary) khi all DA_THANH_TOAN | HĐ gia_tri=100tr, 4 GĐ × 25tr = 100tr. | All trang_thai_tt=DA_THANH_TOAN | 1. Đổi 4 GĐ sang DA_THANH_TOAN. 2. [Lưu]. | (1) PASS (boundary inclusive). (2) Progress bar 100%. | Edge 🟡 |
| TC-TTGD-024 | FR-X.3-01 / progress bar partial (A4 merged) | Progress bar tính chỉ trên Σ DA_THANH_TOAN, không phải Σ tổng GĐ | HĐ gia_tri=100tr, GĐ1=40tr DA_TT, GĐ2=30tr CHUA_TT, GĐ3=30tr CHUA_TT. | — | 1. Xem progress bar trên accordion + cột "Tiến độ TT" trên list. | (1) Progress bar = 40% (40tr DA_TT / 100tr gia_tri). (2) KHÔNG phải 100% (Σ tổng GĐ) hay 70% (40+30). | Edge 🔴 |

---

## Tổng kết file 03-TC

- **Tổng số TC: 11** (3 Happy + 3 Negative + 5 Edge — A4 +3)
- **Critical TC (🔴)**: TC-TTGD-001, 002, 010, 022, 024
- **A4 merged 2026-05-10**: TC-TTGD-022, 023, 024

*Generated 2026-05-10 — Phase A step A3*
