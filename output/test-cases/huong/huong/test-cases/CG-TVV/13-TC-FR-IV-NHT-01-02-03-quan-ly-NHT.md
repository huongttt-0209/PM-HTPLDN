# Test Cases — FR-IV-NHT-01/02/03: Quản lý Người hỗ trợ pháp lý

> **SRS Ref**: FR-IV-NHT-01/02/03 (NĐ 55/2019 Đ.7), SCR-IV-NHT-01/02/03, Entity NGUOI_HO_TRO + NGUOI_HO_TRO_LINH_VUC, SM-NHT (CHO_KICH_HOAT → HOAT_DONG → TAM_DUNG → VO_HIEU_HOA)
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:1260-1373`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NHT-UI-01 | FR-IV-NHT-01 / SCR-IV-NHT-01 / UI DS | Verify SCR-IV-NHT-01 DS Người hỗ trợ pháp lý (3 tab + 4 filter + table) | qtht_01 | URL `/chuyen-gia-tvv/nguoi-ho-tro` | 1. Mở list NHT | **TABS (3)** (theo SRS line 1822-1824): "Đang hoạt động" (default), "Tạm dừng", "Vô hiệu hóa"<br>**FILTERS (4)** (SRS line 1825-1828): Ô tìm kiếm Placeholder "Tìm theo họ tên, email hoặc tên đăng nhập" (NGUYÊN VĂN), Đơn vị công tác (search dropdown), Lĩnh vực chuyên môn (multi-select), Trạng thái (multi 3 enum, ẩn khi tab cụ thể) + nút "Tìm kiếm" / "Xóa bộ lọc"<br>**TABLE columns** (SRS line 1830-1838): STT, Họ tên (link → SCR-IV-NHT-03), Tên đăng nhập, Đơn vị công tác (cắt 30 ký), Chức vụ, Lĩnh vực chuyên môn (tags max 3 + "+N"), Số VV đang phụ trách, Trạng thái (badge), Hành động (icon Xem/Sửa + dropdown "..." Cập nhật trạng thái + Xóa)<br>**Header**: "+ Thêm Người hỗ trợ"<br>**EMPTY STATE** (SRS line 1839): "Chưa có Người hỗ trợ pháp lý nào trong mục này" + nút "+ Thêm Người hỗ trợ" (chỉ tab Đang hoạt động) | Happy 🔴 |
| TC-NHT-UI-02 | FR-IV-NHT-01 / SCR-IV-NHT-02 / UI Form | Verify form Thêm/Sửa NHT (5 fields) | qtht_01 | URL `/nguoi-ho-tro/form` | 1. Click "+ Thêm" | **FIELDS (5)**: ho_ten*, email* (RFC 5322), username* (4-50 ký), don_vi_id (auto-set CB NV; QTHT chọn tự do), linh_vuc_ids* (multi ≥1)<br>**Buttons**: Lưu / Hủy | Happy 🔴 |
| TC-NHT-UI-03 | FR-IV-NHT-03 / SCR-IV-NHT-03 / UI 3 tab | Verify SCR-IV-NHT-03 chi tiết NHT 3 tab | qtht_01, NHT-TW-001 HOAT_DONG có ≥2 VV | — | 1. Mở chi tiết | **TABS (3)**: Thông tin (TK + đơn vị + chức vụ + lĩnh vực), Bồi dưỡng (lịch sử khóa bồi dưỡng theo NĐ 55/2019 Đ.7 — chung_chi_htpl JSON), Vụ việc đã hỗ trợ (lịch sử UC60/UC65 từ FR-V) | Happy 🔴 |

## B. CREATE NHT (auto cấp TK + gán vai trò + gửi mail kích hoạt)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NHT-001 | FR-IV-NHT-01 / AC1 | Happy path tạo NHT mới | cb_nv_tw_01, ≥1 lĩnh vực PL, MailHog UP | ho_ten: "Trần Thị B", email: "b@example.com", username: "tran_b", don_vi_id: TW (auto), linh_vuc: ["Lao động"] | 1. Click + Thêm<br>2. Nhập 5 fields<br>3. Lưu | **STATE**: TAI_KHOAN insert username="tran_b" trang_thai=CHO_KICH_HOAT password=NULL token kích hoạt; **NGUOI_HO_TRO insert** trang_thai=CHO_KICH_HOAT, tai_khoan_id link 1:1; junction NGUOI_HO_TRO_LINH_VUC insert; TAI_KHOAN_VAI_TRO insert vai trò "NHT"; AUDIT_LOG 4 entries; **Mail kích hoạt gửi b@example.com**<br>**UI**: Toast "Tạo NHT thành công, đã gửi mail kích hoạt"<br>**PERSIST**: List có NHT mới với badge "Chờ kích hoạt"; MailHog có mail | Happy 🔴 |
| TC-NHT-002 | FR-IV-NHT-01 / AC2 | NHT bấm link kích hoạt → đặt mật khẩu lần đầu → HOAT_DONG | NHT-TW-002 CHO_KICH_HOAT, mail có link | password: "Secret@123" | 1. Mở mail<br>2. Click link kích hoạt<br>3. Đặt mật khẩu<br>4. Submit | **STATE**: TAI_KHOAN.password=hash, trang_thai=HOAT_DONG; NGUOI_HO_TRO.trang_thai=HOAT_DONG (đồng thời)<br>**UI**: Redirect login với "Kích hoạt thành công"<br>**PERSIST**: NHT có thể login; xuất hiện trong UC59 phân công VV | Happy 🔴 |
| TC-NHT-003 | FR-IV-NHT-01 / E1 ERR-NHT-01 | Email/username trùng → ERR-NHT-01 | cb_nv_tw_01, đã có NHT email "b@example.com" | email trùng | 1. Submit | "Email hoặc tên đăng nhập đã được sử dụng" (NGUYÊN VĂN ERR-NHT-01) | Negative 🔴 |
| TC-NHT-004 | FR-IV-NHT-01 / E2 ERR-NHT-02 | CB NV ĐP cố tạo NHT cho đơn vị TW → ERR-NHT-02 | cb_nv_dp_01 (HN), DevTools tamper don_vi_id=TW | — | 1. Tamper don_vi_id<br>2. Submit | "Bạn không có quyền tạo NHT cho đơn vị này" (NGUYÊN VĂN ERR-NHT-02); BR-AUTH-08 | Negative 🔴 |
| TC-NHT-005 | FR-IV-NHT-01 / E3 ERR-NHT-03 | Thiếu lĩnh vực → ERR-NHT-03 | cb_nv_tw_01 | linh_vuc_ids: [] | 1. Submit | "Vui lòng chọn ít nhất 1 lĩnh vực chuyên môn" (NGUYÊN VĂN ERR-NHT-03) | Negative 🟡 |
| TC-NHT-006 | FR-IV-NHT-01 / Username 4-50 ký | Username boundary 3 ký → reject | cb_nv_tw_01 | username: "abc" (3 ký) | 1. Submit | API 400 "Tên đăng nhập 4-50 ký tự" — SPEC-CLARIFY-CGTVV-09 nếu SRS không có ERR code | Negative 🟡 |

## C. UPDATE / DELETE NHT

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NHT-101 | FR-IV-NHT-01 / AC3 Update LV | Sửa lĩnh vực chuyên môn | qtht_01, NHT-TW-003 HOAT_DONG có LV [Lao động] | linh_vuc_ids: [Lao động, Thuế] | 1. Sửa LV<br>2. Lưu | NGUOI_HO_TRO_LINH_VUC junction insert "Thuế"; AUDIT_LOG diff | Happy 🟡 |
| TC-NHT-102 | FR-IV-NHT-01 / E4 ERR-NHT-04 | Vô hiệu hóa NHT có VV đang phụ trách → ERR-NHT-04 | qtht_01, NHT-TW-004 HOAT_DONG có 2 VU_VIEC DANG_XU_LY | — | 1. Action Vô hiệu hóa | "NHT đang được phân công 2 vụ việc, vui lòng phân công lại trước khi vô hiệu hóa" (NGUYÊN VĂN ERR-NHT-04 với count substitution) | Negative 🔴 |
| TC-NHT-103 | FR-IV-NHT-01 / SM-NHT HOAT_DONG → TAM_DUNG | Tạm dừng NHT | qtht_01, NHT-TW-005 HOAT_DONG | — | 1. Action Tạm dừng + ly_do | NGUOI_HO_TRO.trang_thai=TAM_DUNG; AUDIT_LOG | Happy 🟡 |
| TC-NHT-104 | FR-IV-NHT-01 / SM-NHT TAM_DUNG → HOAT_DONG | Kích hoạt lại NHT | qtht_01, NHT-TW-006 TAM_DUNG | — | 1. Action Kích hoạt lại | trang_thai=HOAT_DONG | Happy 🟡 |

## D. SEARCH NHT (FR-IV-NHT-02 — phục vụ UC59)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NHT-201 | FR-IV-NHT-02 / AC1 | Tìm NHT theo lĩnh vực | cb_nv_tw_01, NHT đa lĩnh vực | linh_vuc_ids: ["Lao động"] | 1. Filter LV<br>2. Verify | Table chỉ NHT có lĩnh vực Lao động trong chuyên môn | Happy 🔴 |
| TC-NHT-202 | FR-IV-NHT-02 / AC2 | Tìm NHT theo đơn vị | qtht_01, NHT thuộc TW/HN/HP | don_vi_id: HN | 1. Filter Đơn vị HN<br>2. Verify | Table chỉ NHT thuộc HN | Happy 🟡 |
| TC-NHT-203 | FR-IV-NHT-02 / Multi filter | Filter LV + đơn vị + trạng thái | qtht_01 | LV [Lao động] + HN + HOAT_DONG | 1. Apply 3 filter | AND logic; Table chỉ NHT match TẤT CẢ | Happy 🟡 |
| TC-NHT-204 | FR-IV-NHT-02 / Pagination | 20/trang BR-DATA-07 | qtht_01, ≥25 NHT | — | 1. Verify pagination | Page 1: 20; Page 2: 5+ | Happy 🟡 |

## E. READ chi tiết NHT (FR-IV-NHT-03)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NHT-301 | FR-IV-NHT-03 / AC1 NHT self-view | NHT đăng nhập xem hồ sơ của mình | nht_01 | — | 1. Login nht_01<br>2. Profile/Hồ sơ của tôi | 3 tab visible: Thông tin (TK + đơn vị + LV) / Bồi dưỡng (chung_chi_htpl JSON list) / Vụ việc đã hỗ trợ (UC60/65 list) | Happy 🔴 |
| TC-NHT-302 | FR-IV-NHT-03 / AC2 CB NV xem NHT cùng đơn vị | cb_nv_dp_01 (HN) xem NHT thuộc HN | cb_nv_dp_01, NHT-HN-001 | — | 1. Mở chi tiết NHT-HN-001 | 3 tab full data | Happy 🟡 |
| TC-NHT-303 | FR-IV-NHT-03 / BR-AUTH-08 | CB NV ĐP HN cố xem NHT TW → reject | cb_nv_dp_01, NHT-TW-001 | — | 1. Direct URL `/nguoi-ho-tro/chi-tiet/NHT-TW-001` | API 403 hoặc redirect; không thấy trong list của HN | Negative 🟡 |

---

## F. EDGE bổ sung (A4 inline merge — 2 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NHT-401 | EDGE-A4-hh / Email cross-entity | NHT email trùng với TVV email (cross-entity uniqueness) | qtht_01, đã có TVV email "shared@example.com" | NHT email: "shared@example.com" | 1. Submit Create NHT | SPEC-CLARIFY-CGTVV-19: TAI_KHOAN.email UNIQUE — NHT email cũng phải tạo TK, sẽ conflict với TVV TK email; reject ERR-NHT-01 hoặc cho phép share TK? | Edge 🔴 |
| TC-NHT-402 | EDGE-A4-ii / NHT vô hiệu hóa giữa form | NHT đang đăng ký TVV mới (form FR-IV-03 mở) → admin vô hiệu hóa NHT đột ngột | nht_01 form FR-IV-03 đang mở, qtht_01 vô hiệu hóa nht_01 | — | 1. nht_01 đang nhập form<br>2. qtht_01 vô hiệu hóa<br>3. nht_01 click Submit | Submit fail với 401 hoặc 403 "Tài khoản của bạn vừa bị vô hiệu hóa, vui lòng liên hệ quản trị"; data form bị mất; SPEC-CLARIFY-CGTVV-20 nếu cần auto-save draft | Edge 🟡 |

---

## G. A6 fill gap (Traceability matrix forward — 1 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-NHT-501 | A6-FILL / SM-NHT VO_HIEU_HOA → HOAT_DONG | Khôi phục NHT VO_HIEU_HOA (admin) | qtht_01, NHT-TW-007 VO_HIEU_HOA | — | 1. Action "Khôi phục" (admin only) | NGUOI_HO_TRO.trang_thai=HOAT_DONG; TAI_KHOAN.trang_thai=HOAT_DONG (đồng bộ); AUDIT_LOG action=RESTORE; SPEC-CLARIFY-CGTVV-24 nếu SRS không cover transition này explicit | Happy 🟡 |

---

**Tổng số TC**: 23 (3 UI + 6 Create + 4 Update/SM + 4 Search + 3 Read + 2 Edge A4 + 1 A6 fill)
