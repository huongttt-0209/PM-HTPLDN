# Test Cases — FR-IV-05 + FR-IV-10: Xem chi tiết TVV + Lịch sử hỗ trợ

> **SRS Ref**: FR-IV-05 (UC43), FR-IV-10 (UC48), SCR-IV-03 (5 tab), Entity LICH_SU_HO_TRO_TVV
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:432-481 + 750-805`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CT-UI-01 | FR-IV-05 / SCR-IV-03 / UI 5 tab | Verify SCR-IV-03 5 tab + header action conditional | qtht_01, TVV-TW-005 HOAT_DONG | URL `/chuyen-gia-tvv/chi-tiet/TVV-TW-005` | 1. Mở chi tiết<br>2. Verify 5 tab + header | **HEADER**: Breadcrumb + Tên TVV + Badge trạng thái (theo §3.0 màu) + Action buttons (Tạm dừng / Vô hiệu hóa / Công khai)<br>**TABS (5)**: Hồ sơ (default), Năng lực, Thẩm định (visible khi DANG_THAM_DINH/YEU_CAU_BO_SUNG/CHO_PHE_DUYET — ẩn khi HOAT_DONG/TAM_DUNG/VO_HIEU_HOA/MOI_DANG_KY/CHO_THAM_DINH), Lịch sử, Đánh giá<br>**NEGATIVE**: KHÔNG có nút "Tiếp nhận hồ sơ" header (D.2.1 OUT) | Happy 🔴 |
| TC-CT-UI-02 | FR-IV-10 / SCR-IV-03 Tab Lịch sử / UI | Verify Tab Lịch sử có 3 filter + table + thống kê + timeline | qtht_01, TVV-TW-006 có ≥3 VV | — | 1. Mở chi tiết → tab Lịch sử | **FILTERS (3)**: Từ ngày, Đến ngày, Trạng thái VV<br>**TABLE columns**: Mã VV, DN, Lĩnh vực, Trạng thái VV, Ngày phân công, Ngày HT, Điểm đánh giá (1.0-5.0)<br>**STATS card**: "Tổng VV: N", "Hoàn thành: M", "Điểm TB: X.X/5"<br>**TIMELINE**: Hiển thị mốc thời gian phân công + HT của từng VV | Happy 🔴 |

## B. Read chi tiết (FR-IV-05)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CT-001 | FR-IV-05 / AC1 | Tab Hồ sơ hiển thị đầy đủ | qtht_01, TVV-TW-005 đầy đủ field | — | 1. Mở chi tiết → tab Hồ sơ | Hiển thị: ho_ten, ngay_sinh dd/mm/yyyy, cccd, gioi_tinh label VN, dia_chi, email, sdt, trinh_do, chung_chi, so_the, anh_dai_dien (hoặc default), tổ chức (link), lĩnh vực (tags), files đính kèm (link tải) | Happy 🔴 |
| TC-CT-002 | FR-IV-05 / Tab Năng lực | Tab Năng lực hiển thị đủ field FR-IV-04 | qtht_01, TVV có HO_SO_TU_VAN_VIEN | — | 1. Click tab Năng lực | Hiển thị: trinh_do, so_nam_kinh_nghiem, chuyen_nganh, bang_cap_chi_tiet (JSON parsed), chung_chi_chi_tiet (JSON), so_the_hanh_nghe, mo_ta_kinh_nghiem, file_the_hanh_nghe (link tải) | Happy 🟡 |
| TC-CT-003 | FR-IV-05 / Tab Thẩm định visibility | Tab Thẩm định ẩn khi HOAT_DONG | qtht_01, TVV-TW-005 HOAT_DONG | — | 1. Mở chi tiết<br>2. Verify tab Thẩm định | Tab "Thẩm định" KHÔNG hiển thị (chỉ visible khi DANG_THAM_DINH/YEU_CAU_BO_SUNG/CHO_PHE_DUYET) | Happy 🟡 |
| TC-CT-004 | FR-IV-05 / E1 | TVV không tồn tại → ERR-HS-01 | qtht_01 | URL `/chuyen-gia-tvv/chi-tiet/99999` | 1. Direct URL ID không tồn tại | API 404 hoặc UI Error page "Hồ sơ tư vấn viên không tồn tại" (NGUYÊN VĂN ERR-HS-01) | Negative 🟡 |

## C. Lịch sử hỗ trợ (FR-IV-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-LS-001 | FR-IV-10 / AC1 | Hiển thị lịch sử VV + thống kê | qtht_01, TVV-TW-005 có 5 VV (3 HOAN_THANH, 2 DANG_XU_LY) | — | 1. Mở chi tiết → tab Lịch sử | **STATE**: Network call `/api/v1/tu-van-vien/{id}/lich-su?page=1&size=20` join PHAN_CONG_VU_VIEC<br>**UI**: Table 5 VV; Stats: "Tổng: 5 / HT: 3 / Điểm TB: 4.5/5"; Timeline 5 mốc thời gian sắp xếp DESC | Happy 🔴 |
| TC-LS-002 | FR-IV-10 / Filter time | Filter Từ-Đến ngày | qtht_01, TVV có VV khoảng 2025-10 đến 2026-04 | tu_ngay: 2026-01-01, den_ngay: 2026-03-31 | 1. Pick range<br>2. Verify | Table chỉ VV ngày phân công trong range; Stats cập nhật theo filter | Happy 🟡 |
| TC-LS-003 | FR-IV-10 / Pagination | Pagination 20/trang khi >20 VV | qtht_01, TVV có ≥25 VV | — | 1. Tab Lịch sử<br>2. Click page 2 | Page 1: 20 VV; Page 2: 5 VV; BR-DATA-07 | Happy 🟡 |
| TC-LS-004 | FR-IV-10 / Empty state | Tab Lịch sử khi TVV chưa có VV | qtht_01, TVV-TW-007 chưa có VV | — | 1. Mở tab Lịch sử | Empty state "Chưa có vụ việc nào"; Stats: "Tổng: 0 / HT: 0 / Điểm TB: —/5" (không hiển thị 0/5 theo BR-CALC-06 INF-TVV-DG-01) | Negative 🟡 |

---

## D. EDGE bổ sung (A4 inline merge — 1 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-LS-501 | EDGE-A4-q / Reversed date range Lịch sử | Tab Lịch sử filter tu_ngay > den_ngay → reject | qtht_01 | tu_ngay: 2026-05-09, den_ngay: 2026-05-01 | 1. Pick reversed | Inline error "Từ ngày ≤ Đến ngày" | Edge 🟡 |

---

## E. A6 fill gap (Traceability matrix forward — 1 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-LS-601 | A6-FILL / ERR-LS-01 explicit | Tab Lịch sử cho TVV không tồn tại → ERR-LS-01 | qtht_01 | URL `/chuyen-gia-tvv/chi-tiet/99999` rồi click tab Lịch sử | 1. Direct URL invalid ID<br>2. Click tab Lịch sử | API 404 hoặc UI Error "Tư vấn viên không tồn tại" (NGUYÊN VĂN ERR-LS-01); KHÔNG render table | Negative 🟡 |

---

**Tổng số TC**: 12 (2 UI + 4 Detail + 4 Lịch sử + 1 Edge A4 + 1 A6 fill)
