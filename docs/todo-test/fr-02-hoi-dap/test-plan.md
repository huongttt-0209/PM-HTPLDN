# Kế Hoạch Kiểm Thử — Hỏi đáp (FR-02, SCR-II-01..03)

> **Phiên bản**: 1.1 — Revised 2026-05-12 13:00:00 (apply review.md REVISE — fix 3 Critical + bump SLA TC count + add Bảng 2 defer template)
> **Ngày tạo**: 2026-05-12
> **Module Layer:** L3 — GIAO DỊCH LÕI (LỚP 3, module #7 trong 18 đơn vị test)
> **Nguồn dữ liệu**: LOCAL — `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` (v3.5, 1652 dòng) + `srs-v3/srs-fr-02-hoi-dap.md` (v3.0 baseline) + `srs-v3/srs-v3.md` Phụ lục B (BR cross-cutting)
> **SRS Reference**: FR-II-01..10, FR-II-NEW-01 *(DEPRECATED Q11 2026-05-07)*, FR-II-NEW-02, FR-II-CROSS-01; SCR-II-01, SCR-II-02, SCR-II-03

> **SOURCE MODE:** LOCAL — mọi BR / TC cite đều dùng prefix path `srs-update-2026-5-5/...` cho update mới (auto-filter 4 tiêu chí FR-II-06, 5 trường công khai CR-01, Hybrid mẫu phản hồi 2 tầng, Đóng hồ sơ thủ công BR-FLOW-06) và `srs-v3/...` cho BR cross-cutting.

> **v3.0 (2026-04-23):** Test plan này dùng cho **GĐ 3 Functional + Auth + Edge**. GĐ 1 Seed + GĐ 2 Workflow là 2 phase riêng, output `seed-checklist-fr-02.md` + `workflow-test-report-fr-02.md`. Happy path đã cover ở GĐ 2 — TC ở đây chỉ còn **negative + edge + auth + cross-module**.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Module L (Hỏi đáp pháp lý)** — Nhóm II SRS, gồm 10 FR cốt lõi (FR-II-01..10) + 2 FR mới (FR-II-NEW-02 Mẫu phản hồi Hybrid 2 tầng; FR-II-NEW-01 **DEPRECATED** Q11 2026-05-07 — thay bằng auto-filter 4 tiêu chí trong FR-II-06 Step 5) + 1 FR cross-cutting SLA (FR-II-CROSS-01).
- **Phạm vi nghiệp vụ:** Tiếp nhận → Phân công → Soạn phản hồi → Phê duyệt (auto-transition BR-FLOW-01) → Công khai lên Cổng Pháp luật Quốc gia → Hủy công khai → Đóng hồ sơ thủ công (BR-FLOW-06).
- **Bảng dữ liệu chính:** `HOI_DAP` (owned, ~10k records/năm) + `PHAN_HOI` (owned, ~20k/năm) + `MAU_PHAN_HOI` (owned, ~500/năm, Mô hình B Hybrid 2 tầng) + `CAU_HINH_PHAN_CONG` *(DEPRECATED v3.5)*.
- **Màn hình:** SCR-II-01 (Danh sách + 7 tab trạng thái), SCR-II-02 (Chi tiết & Soạn phản hồi — toàn bộ workflow), SCR-II-03 (Modal phân công CA_NHAN/TO_CHUC).
- **Điểm nối tự động:**
  - DA_TRA_LOI → CHO_PHE_DUYET (auto, BR-FLOW-01, trigger từ checkbox "Đã trả lời" FR-II-07).
  - HOI_DAP → DA_DUYET → **auto-tạo bản ghi Kho QA (FR-13)** với `nguon=TU_DONG` để full-text search trên Cổng PLQG (LUỒNG A trong `01-tong-quan-nghiep-vu.md` dòng 87-97).
  - HOI_DAP → CONG_KHAI → **gọi API trực tiếp** sang Cổng Pháp luật Quốc gia (BR-FLOW-05, không qua LGSP).
  - HOI_DAP với `kenh_tiep_nhan='TVN_BRIDGE'` → escalate từ FR-13 Tư vấn nhanh + giữ `tu_van_nhanh_goc_id` FK phiên gốc.

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-II-01 | UC10 | Quản lý thông tin hỏi đáp (CRUD + Export Excel) | HOI_DAP | `01-TC-quan-ly-hoi-dap.md` |
| 2 | FR-II-02 | UC11 | Tìm kiếm hỏi đáp tổng hợp | HOI_DAP | `02-TC-tim-kiem-tong-hop.md` |
| 3 | FR-II-03 | UC12 | Tiếp nhận xử lý hỏi đáp (MOI → TIEP_NHAN) | HOI_DAP | `03-TC-tiep-nhan.md` |
| 4 | FR-II-04 | UC13 | Quản lý thông tin tiếp nhận xử lý (Cập nhật thời hạn + Xem lịch sử) | HOI_DAP, AUDIT_LOG | `04-TC-quan-ly-tiep-nhan.md` |
| 5 | FR-II-05 | UC14 | Tìm kiếm hỏi đáp đã tiếp nhận | HOI_DAP | `05-TC-tim-kiem-dang-xu-ly.md` |
| 6 | FR-II-06 | UC15 | Phân công xử lý (CA_NHAN / TO_CHUC) | HOI_DAP, TAI_KHOAN, TO_CHUC_TU_VAN | `06-TC-phan-cong.md` |
| 7 | FR-II-07 | UC16 | Phản hồi câu hỏi + auto-transition CHO_PHE_DUYET | PHAN_HOI, HOI_DAP, MAU_PHAN_HOI | `07-TC-phan-hoi.md` |
| 8 | FR-II-08 | UC17 | Phê duyệt / Từ chối / Công khai / Hủy CK / Đóng hồ sơ / Batch | HOI_DAP, PHAN_HOI | `08-TC-phe-duyet-cong-khai.md` |
| 9 | FR-II-09 | UC18 | Quản lý câu hỏi đã xử lý + Timeline | HOI_DAP, AUDIT_LOG | `09-TC-da-xu-ly.md` |
| 10 | FR-II-10 | UC19 | Tìm kiếm câu hỏi đã xử lý | HOI_DAP | `10-TC-tim-kiem-da-xu-ly.md` |
| 11 | FR-II-NEW-02 | UC mới (CĐT Q48) | Quản lý mẫu phản hồi — Hybrid 2 tầng (TW_QUOC_GIA / BN_RIENG / DP_RIENG) | MAU_PHAN_HOI | `11-TC-mau-phan-hoi-hybrid.md` |
| 12 | FR-II-CROSS-01 | FR-VIII-10 áp dụng | Cấu hình SLA + Cron 30 phút + ngày lễ FR-VIII-29 + notification toggle | HOI_DAP, CAU_HINH_SLA, NGAY_LE | `12-TC-sla-canh-bao.md` |

> **DEPRECATED Q11 2026-05-07:** FR-II-NEW-01 (Cấu hình lĩnh vực ↔ phân công) đã BỎ — thay bằng auto-filter 4 tiêu chí Step 5 trong FR-II-06: (1) lĩnh vực `linh_vuc_chuyen_mon`/`linh_vuc_ids[]` match; (2) đơn vị BR-AUTH-08 cùng cấp mạng lưới; (3) `workload ASC`; (4) `ho_ten ASC LIMIT 10`. Xem `02-thu-tu-module.md:86,116,138,370`.

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | `qtht_01` | Cấu hình SLA + Mẫu phản hồi (SCR-VIII-06 Tab SLA & Tab Mẫu) — không phải actor Hỏi đáp |
| CB_NV_TW | TW | `cb_nv_tw_01` | Functional CRUD scope TW + tạo Mẫu `TW_QUOC_GIA` (MPH_CREATE_TW) |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH) / `cb_nv_bn_02` (BTC) / `cb_nv_bn_03` (BCT) | CRUD scope Bộ ngành + tạo Mẫu `BN_RIENG` (MPH_CREATE_BN) |
| CB_NV_DP | ĐP | `cb_nv_dp_01` (AG) / `cb_nv_dp_02` (BG) / `cb_nv_dp_03` (BNI) | CRUD scope tỉnh + tạo Mẫu `DP_RIENG` (MPH_CREATE_DP) |
| CB_PD_TW | TW | `cb_pd_tw_01` | Phê duyệt + Công khai + Hủy CK + Đóng hồ sơ scope TW (BR-AUTH-05) |
| CB_PD_BN | BN | `cb_pd_bn_01` (BKH) / `cb_pd_bn_02` (BTC) | Phê duyệt + Công khai scope Bộ ngành cùng cấp |
| CB_PD_DP | ĐP | `cb_pd_dp_01` (AG) / `cb_pd_dp_02` (BG) | Phê duyệt + Công khai scope tỉnh cùng cấp |
| TVV | — | `huongcg` (CG TVV-BTP-TW-0030) | Nhận phân công (loại=CA_NHAN trong FR-II-06) |
| NHT | — | `nht_01` (AG) / `nht_02` (DN) | Nhận phân công (loại=CA_NHAN trong FR-II-06) |
| DN | — | `9999999990` (HN) / `9999999991` (BG) | Gửi câu hỏi qua Cổng PLQG → câu hỏi vào hệ thống với `kenh_tiep_nhan='CONG_PLQG'` |

> **Permission test (TC permission-cross-unit):** dùng `_02`/`_03` fallback cho test cross-unit/cross-cap.
> Reference: [input/users.csv](../../../input/users.csv), [input/test-accounts-isolation.csv](../../../input/test-accounts-isolation.csv), [output/permission-matrix.md](../../../output/permission-matrix.md).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

#### 2.1.0 FR-II-NEW-01 Final Status — BA escalation required

> ⚠️ **SRS inconsistency chưa resolved** — test plan đang stance **DEPRECATED** nhưng SRS update vẫn còn reference. PHẢI BA confirm trước khi đóng TC liên quan auto-filter / phân công.

| SRS line | Nguyên văn (rút gọn) | Test plan stance | BA confirmation status |
|---|---|---|---|
| `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:449` | "FR-II-NEW-01 precondition: cấu hình lĩnh vực ↔ phân công đã tồn tại" | DEPRECATED (mâu thuẫn) | ❓ CHỜ BA — escalate Q11 follow-up |
| `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:829` | Bảng phụ lục FR — vẫn list FR-II-NEW-01 | DEPRECATED (mâu thuẫn) | ❓ CHỜ BA |
| `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1149,1174` | FR list tổng — vẫn còn FR-II-NEW-01 | DEPRECATED (mâu thuẫn) | ❓ CHỜ BA |
| `02-thu-tu-module.md:86,116,138,370` | "DEPRECATED Q11 2026-05-07 — thay bằng auto-filter Step 5 FR-II-06" | DEPRECATED ✅ | ✅ Derived doc xác nhận xóa |

**Action item:** TC-PERM-AUTO-FILTER + TC bất kỳ chạm "cấu hình lĩnh vực ↔ phân công" gán phân loại **C — Chờ BA confirm spec** (xem Bảng 2 §5) tới khi BA quote nguyên văn line "xóa hẳn FR-II-NEW-01 khỏi SRS v3.5".

#### 2.1.1 BR Table

> ⚠️ **Quy định điền bảng:** Cột "Ngoại lệ SRS-quoted" chỉ điền khi SRS có dòng ngoại lệ cụ thể (quote nguyên văn). Trống = BR áp dụng 100%.

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|---------------------|---------------------|-----------|
| BR-AUTH-01 | Xác thực bắt buộc (Tier 1 username/password + TOTP 2FA email) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1566-1570` | ✅ Yes | "API outbound không yêu cầu session" | Precondition mọi TC; TC-AUTH-01 |
| BR-AUTH-02 | Phân cấp 2 tầng TW → {BN, ĐP} ngang cấp song song (v3.5) | `srs-v3/srs-v3.md:3950` + `02-thu-tu-module.md:88` | ✅ Yes | — | TC-PERM-01 (login + scope) |
| BR-AUTH-05 | CB PD chỉ phê duyệt bản ghi cùng cấp đơn vị | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1574-1576` | ✅ Yes | — | TC-PERM-04, TC-PERM-05 |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1546` + `srs-v3/srs-v3.md:3958` | ✅ Yes | MAU_PHAN_HOI override (Hybrid 2 tầng — `TW_QUOC_GIA` đọc cross-cap) | TC-PERM-02, TC-PERM-06, TC-PERM-MPH |
| BR-AUTH-10 | Phân quyền lọc kép cho TVV/NHT/CG (data scope + chỉ thấy bản ghi được phân công) | `01-tong-quan-nghiep-vu.md:195-197` | ✅ Yes | — | TC-PERM-07 (TVV chỉ thấy HOI_DAP được phân công) |
| BR-DATA-01 | Soft delete (set `is_deleted=1`) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1580-1582` | ✅ Yes | AUDIT_LOG: không xóa | TC-FUNC-DEL-01 |
| BR-DATA-03 | Common fields (`created_at`, `created_by`, `updated_at`, `updated_by`, `is_deleted`) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1548` | ✅ Yes | — | TC-FUNC-CRUD verify schema |
| BR-DATA-04 | Auto-gen mã `HD-YYYYMMDD-SEQ` | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1586-1588` | ✅ Yes | — | TC-FUNC-CRUD-02 (uniqueness + format) |
| BR-DATA-05 | Audit trail mọi CUD + phê duyệt + chuyển trạng thái | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1592-1594` | ✅ Yes | — | TC-AUDIT-01..05 |
| BR-DATA-06 | Export Excel tối đa 10.000 dòng theo filter hiện tại + cảnh báo WRN-HD-01 | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:127-129` + `srs-v3/srs-v3.md:3977` | ✅ Yes | — | TC-EXP-01 happy + TC-EXP-02 boundary 10k + TC-EXP-03 filter-aware |
| BR-DATA-07 | Pagination mặc định 20, max 100 | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:323-324` + `srs-v3/srs-v3.md:3978` | ✅ Yes | — | TC-PAG-01..04 |
| BR-DATA-08 | Full-text search trên `noi_dung` + `ma_hoi_dap` + người gửi (tsvector) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:201-202` | ✅ Yes | — | TC-FUNC-SEARCH-01 |
| BR-FLOW-01 | **Tích "Đã trả lời" → AUTO chuyển CHO_PHE_DUYET** (không cần bước "Trình") | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1598-1600` + line 559-562 | ✅ Yes | — | TC-WF-AUTO-01 |
| BR-FLOW-02 | Phê duyệt hàng loạt (batch approve, max 100/batch) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1604-1606` + EC-02 | ✅ Yes | Từ chối phải từng bản ghi (yêu cầu lý do) | TC-WF-BATCH-01..03 |
| BR-FLOW-03 | Không sửa/xóa bản ghi ở `DA_DUYET / CONG_KHAI / HOAN_THANH`; bản ghi đã từng CK không xóa được dù đã Hủy CK | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1610-1612` + line 119 | ✅ Yes | QTHT force-edit (audit đặc biệt) | TC-FUNC-DEL-02, TC-NEG-EDIT-DA-DUYET |
| BR-FLOW-04 | Từ chối BẮT BUỘC nhập lý do ≥10 ký tự | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1616-1618` + `01-tong-quan-nghiep-vu.md:188` | ✅ Yes | — | TC-WF-REJECT-01, TC-NEG-REJECT-NO-REASON |
| BR-FLOW-05 | Công khai qua **API trực tiếp Cổng PLQG** (không qua LGSP); chỉ CB PD cùng cấp được Công khai/Hủy CK | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1622-1624` | ✅ Yes | — | TC-WF-PUBLISH, TC-PERM-PUBLISH-CB-NV-BLOCKED |
| BR-FLOW-06 | **Đóng hồ sơ thủ công** — hệ thống KHÔNG tự đóng (BA chốt 2026-05-05) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1626-1630` | ✅ Yes | QTHT force SET HOAN_THANH (migration) | TC-WF-CLOSE-01 + TC-EC-NO-AUTOCLOSE |
| BR-CALC-03 | Deadline = `ngay_tiep_nhan` + N ngày làm việc (trừ ngày lễ FR-VIII-29) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1634-1636` | ✅ Yes | — | TC-SLA-DEADLINE-01 |
| BR-SLA-01 | SLA mặc định Hỏi đáp = 10 ngày LV (theo cấu hình `CAU_HINH_SLA.loai_yeu_cau='HOI_DAP'`) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:265` + `01-tong-quan-nghiep-vu.md:180` | ✅ Yes | QTHT chỉnh được qua SCR-VIII-06 Tab SLA | TC-SLA-DEFAULT-01 |
| BR-SLA-02 | 4 mức cảnh báo: BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG (BA Q5 đề xuất BỎ "Quá hạn nghiêm trọng" — đang theo SRS hiện tại còn 4 mức) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:992-998,1640-1642` + `02-thu-tu-module.md:114` | ✅ Yes | BA Q5 conflict: SCR-VIII-06 chỉ còn 2 ngưỡng — **cần BA xác nhận** | TC-SLA-LEVEL-01..04 (test 4 mức) |
| BR-SLA-03 | Khi chuyển mức cảnh báo → gửi notification in-app + email (CB NV + CB PD) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1646-1648` | ✅ Yes | Chỉ gửi khi BẬT cấu hình | TC-SLA-NOTIF-01 |
| BR-SLA-04 | Ngày làm việc: Thứ 2-6, trừ ngày lễ FR-VIII-29 schema 5 trường | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:986` + `02-thu-tu-module.md:139` | ✅ Yes | — | TC-SLA-WORKDAY-01 |
| BR-EC-01 | Optimistic locking (version field) mọi UPDATE/DELETE | `srs-v3/srs-v3.md:4066` + `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:332-342,1532` | ✅ Yes | — | TC-EC-CONFLICT-01 (UPDATE), TC-EC-CONFLICT-02 (thời hạn — ERR-TH-CONFLICT) |
| BR-EC-13 | Search input sanitize max 200 ký tự | `srs-v3/srs-v3.md:4078` + `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:318` | ✅ Yes | — | TC-NEG-SEARCH-XSS, TC-NEG-SEARCH-LONG |
| BR-EC-19 | Batch action max 100 records/batch | `srs-v3/srs-v3.md` + `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1056` | ✅ Yes | — | TC-WF-BATCH-LIMIT |
| BR-EC-20 | KHÔNG set `CONG_KHAI` trước khi API Cổng PLQG thành công (EC-04) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:722,1057` | ✅ Yes | — | TC-EC-PUBLISH-API-FAIL |
| BR-ROUTE-HD-01 | Cơ quan tiếp nhận `don_vi_id` theo nguồn: Cổng PLQG → DN chọn (mặc định Sở TP tỉnh DN); cán bộ nhập tay → đơn vị cán bộ đăng nhập | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:99,1519` `[CR-06]` | ✅ Yes | — | TC-ROUTE-CONG-PLQG, TC-ROUTE-CB-MANUAL |
| CR-01 | 5 trường công khai chuẩn (`cong_khai`, `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`) | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1238-1243,1351-1355` + `01-tong-quan-nghiep-vu.md:232` | ✅ Yes | — | TC-WF-PUBLISH-FIELDS, TC-WF-UNPUBLISH-FIELDS |

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted nguyên văn) | Severity |
|--------|-------------------|----------------------------------|----------|
| ERR-HD-01 | Nội dung câu hỏi trống | "Nội dung câu hỏi là bắt buộc" | ERROR |
| ERR-HD-02 | Nội dung > 5000 ký tự | "Nội dung câu hỏi tối đa 5000 ký tự" | ERROR |
| ERR-HD-03 | Lĩnh vực không tồn tại | "Lĩnh vực pháp luật không tồn tại" | ERROR |
| ERR-HD-04 | Sửa/xóa bản ghi ở trạng thái cấm | "Không thể sửa/xóa bản ghi đã duyệt/công khai/hoàn thành. Cần Hủy công khai (nếu đang ở trạng thái Công khai) trước, nhưng vẫn không xóa được do quy định lưu vết" | ERROR |
| WRN-HD-01 | Export vượt 10.000 rows | "Hệ thống sẽ xuất 10.000 dòng đầu tiên" | WARNING |
| ERR-DELETE-STATE | Xóa hàng loạt: bản ghi ở trạng thái cấm | "Bản ghi #{ma_hoi_dap} ở trạng thái '{tt}' không thể xóa (đã duyệt/công khai/hoàn thành)" | ERROR (per-record) |
| ERR-AUTH-DEL | Xóa hàng loạt: khác đơn vị | "Không có quyền xóa bản ghi #{ma_hoi_dap} (thuộc đơn vị khác)" | ERROR (per-record) |
| ERR-BATCH-CONFLICT | Bị cán bộ khác cập nhật giữa chừng | "Bản ghi #{ma_hoi_dap} đã được {tên cán bộ} cập nhật lúc {thời gian}, đã bỏ qua trong lần xử lý này. Vui lòng tải lại danh sách và thử lại" | ERROR (per-record) |
| ERR-TN-01 | Trạng thái không phải MOI khi Tiếp nhận | "Hỏi đáp đã được tiếp nhận bởi {người khác}" | ERROR |
| ERR-TN-02 | Bản ghi không tồn tại | "Hỏi đáp không tồn tại hoặc đã bị xóa" | ERROR |
| ERR-TN-03 | Concurrency lock: 2 CB tiếp nhận cùng lúc | "Bản ghi đã được tiếp nhận bởi người khác" | ERROR |
| ERR-DXL-01 | `tu_ngay > den_ngay` | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |
| ERR-AUTH-DXL-01 | Không có quyền truy cập đơn vị | "Bạn không có quyền xem danh sách đơn vị này" | ERROR |
| ERR-TH-CONFLICT | Cập nhật thời hạn — version mismatch | "Thời hạn đã bị thay đổi bởi {tên cán bộ} lúc {thời gian} thành {thời hạn mới}. Vui lòng Tải lại hoặc Ghi đè" | ERROR (HTTP 409) |
| ERR-TH-01 | `thoi_han_moi <= ngày hiện tại` | "Thời hạn mới phải sau ngày hiện tại" | ERROR |
| ERR-TH-02 | Lý do thay đổi < 10 hoặc > 500 ký tự | "Lý do thay đổi phải từ 10 đến 500 ký tự" | ERROR |
| ERR-TH-03 | Bản ghi không ở trạng thái cho cập nhật thời hạn | "Không thể cập nhật thời hạn cho bản ghi ở trạng thái '{tt}'" | ERROR |
| ERR-PC-01 | NHT/TVV cá nhân không còn hoạt động | "Người được chọn đã bị vô hiệu hóa" | ERROR |
| WRN-PC-01 | Khối lượng vượt ngưỡng | "Cán bộ {tên} đang xử lý {N} yêu cầu. Xác nhận phân công?" | WARNING |
| ERR-PC-02 | Trạng thái không hợp lệ khi phân công | "Hỏi đáp ở trạng thái '{tt}' không thể phân công" | ERROR |
| ERR-PC-03 | Tổ chức tư vấn không còn hoạt động | "Tổ chức tư vấn '{tên}' đã bị vô hiệu hóa hoặc tạm dừng hoạt động" | ERROR |
| ERR-PC-04 | Loại=TO_CHUC thiếu Tổ chức hoặc TVV | "Phân công cho Tổ chức tư vấn phải chọn đủ 2 thông tin: Tổ chức + Tư vấn viên thuộc tổ chức" | ERROR |
| ERR-PC-05 | Loại=TO_CHUC nhưng TVV không thuộc TC | "Tư vấn viên '{tên}' không thuộc Tổ chức '{tên TC}'. Vui lòng chọn lại" | ERROR |
| ERR-PC-06 | Loại=CA_NHAN truyền thừa Tổ chức | "Phân công cá nhân không cần chọn Tổ chức tư vấn" | ERROR |
| ERR-PH-01 | Nội dung phản hồi trống | "Nội dung phản hồi là bắt buộc" | ERROR |
| ERR-PH-02 | Trạng thái không cho phản hồi | "Hỏi đáp ở trạng thái '{tt}' không thể phản hồi" | ERROR |
| WRN-PH-01 | Không phải người được phân công | "Bạn không phải người được phân công. Vẫn muốn phản hồi?" | WARNING |
| ERR-PD-01 | CB PD khác cấp | "Bạn không có quyền phê duyệt bản ghi thuộc đơn vị khác cấp" | ERROR |
| ERR-PD-02 | Từ chối thiếu lý do | "Vui lòng nhập lý do từ chối" | ERROR |
| ERR-PD-03 | Trạng thái không hợp lệ khi phê duyệt | "Hỏi đáp không ở trạng thái chờ phê duyệt" | ERROR |
| ERR-PD-04 | API Cổng PLQG lỗi (Công khai) | "Lỗi kết nối Cổng PLQG. Vui lòng thử công khai lại" | ERROR |
| WRN-PD-01 | Batch: 1+ lỗi | "{N} duyệt thành công, {M} lỗi" | WARNING |
| ERR-PD-05 | Batch quá 100 bản ghi | "Tối đa 100 bản ghi/batch" | ERROR |
| ERR-PD-06 | API Cổng PLQG lỗi (Hủy CK) | "Lỗi gỡ Cổng PLQG. Vui lòng thử lại" | ERROR |
| ERR-MPH-01..06 | Quản lý Mẫu phản hồi (xem FR-II-NEW-02) | (theo SRS line 935-940) | ERROR |
| INF-HD-TK-01..03 | Tìm kiếm không có kết quả | "Không tìm thấy hỏi đáp phù hợp" (variants) | INFO |

> ⚠️ Message phải quote **nguyên văn** từ SRS. Khi test negative, expected message match exact → không được "close enough" accept.

### 2.3 Permission Matrix (module-specific)

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md). Bảng dưới gom 11 role × 8 action chính của Hỏi đáp.

| Entity / Action | admin | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | TVV | NHT | CG | DN |
|-----------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **HOI_DAP — List/Read** (SCR-II-01 tab Tất cả) | R\* | R\* | R(TW) | R(BN) | R(DP) | R(TW) | R(BN) | R(DP) | R(filtered BR-AUTH-10) | R(filtered BR-AUTH-10) | R(filtered BR-AUTH-10) | R(own questions via Cổng PLQG, không UI nội bộ) |
| **HOI_DAP — Create** (Thêm mới Drawer) | C | — | C(TW) | C(BN) | C(DP) | — | — | — | — | — | — | C(via Cổng PLQG inbound, kênh=CONG_PLQG) |
| **HOI_DAP — Update** (`trang_thai NOT IN (DA_DUYET, CONG_KHAI, HOAN_THANH)`) | U\* | — | U(TW) | U(BN) | U(DP) | — | — | — | — | — | — | — |
| **HOI_DAP — Delete** (`trang_thai NOT IN (DA_DUYET, CONG_KHAI, HOAN_THANH)`, không xóa bản ghi đã từng CK) | D\* | — | D(TW, same don_vi) | D(BN, same don_vi) | D(DP, same don_vi) | — | — | — | — | — | — | — |
| **Tiếp nhận** (MOI → TIEP_NHAN, FR-II-03) | ✅ | — | ✅(TW) | ✅(BN) | ✅(DP) | — | — | — | — | — | — | — |
| **Phân công CA_NHAN / TO_CHUC** (FR-II-06) | ✅ | — | ✅(TW) | ✅(BN) | ✅(DP) | — | — | — | — | — | — | — |
| **Soạn phản hồi + tích "Đã trả lời"** (FR-II-07, BR-FLOW-01) | ✅ | — | ✅(TW) | ✅(BN) | ✅(DP) | — | — | — | ✅ (nếu được phân công, WRN-PH-01 nếu khác) | ✅ (nếu được phân công) | ✅ (nếu được phân công) | — |
| **Phê duyệt / Từ chối** (CHO_PHE_DUYET → DA_DUYET / DANG_XU_LY) | ✅ | — | — | — | — | ✅(TW cùng cấp) | ✅(BN cùng cấp) | ✅(DP cùng cấp) | — | — | — | — |
| **Công khai / Hủy công khai** (DA_DUYET ↔ CONG_KHAI, BR-FLOW-05) | ✅ | — | — | — | — | ✅(TW cùng cấp) | ✅(BN cùng cấp) | ✅(DP cùng cấp) | — | — | — | — |
| **Đóng hồ sơ** (DA_DUYET/CONG_KHAI → HOAN_THANH, BR-FLOW-06 thủ công) | ✅ | force-only (audit) | ✅(TW same don_vi) | ✅(BN same don_vi) | ✅(DP same don_vi) | ✅(TW cùng cấp) | ✅(BN cùng cấp) | ✅(DP cùng cấp) | — | — | — | — |
| **MAU_PHAN_HOI — CREATE** (Hybrid 2 tầng, FR-II-NEW-02) | C\* | C(toàn quyền) | C `pham_vi=TW_QUOC_GIA` (MPH_CREATE_TW) | C `pham_vi=BN_RIENG` (MPH_CREATE_BN) | C `pham_vi=DP_RIENG` (MPH_CREATE_DP) | — | — | — | — | — | — | — |
| **MAU_PHAN_HOI — READ** (dropdown chèn mẫu SCR-II-02) | R\* | R\* | R(TW + own) | R(TW_QUOC_GIA + own BN) | R(TW_QUOC_GIA + own DP) | R(TW + own) | R(TW_QUOC_GIA + own BN) | R(TW_QUOC_GIA + own DP) | — | — | — | — |
| **Export Excel** (BR-DATA-06, max 10K) | ✅ | — | ✅(TW filter) | ✅(BN filter) | ✅(DP filter) | ✅(TW filter) | ✅(BN filter) | ✅(DP filter) | — | — | — | — |

**Ký hiệu:** C/R/U/D = Create/Read/Update/Delete; `*` = toàn hệ thống; `(TW)/(BN)/(DP)` = giới hạn scope theo cấp; `(filtered BR-AUTH-10)` = thêm filter "bản ghi được phân công" (TVV/NHT/CG).

### 2.4 UI Layout (SCR-II-01 + SCR-II-02 + SCR-II-03)

> ⚠️ **CẢNH BÁO:** Đây là visual spec components từ SRS SCR-II. KHÔNG dùng absence để khẳng định "module KHÔNG có X". Mọi feature không có trên UI phải đối chiếu §2.1 BR table + SRS Phụ lục B trước.

#### SCR-II-01 — Danh sách Hỏi đáp (trang chính)

- **Toolbar:** Breadcrumb "Trang chủ > Hỏi đáp > Quản lý hỏi đáp" + nút [+ Thêm mới] (mở Drawer) + nút [Xuất Excel] (max 10K, WRN-HD-01) + nút [Làm mới] (AJAX, giữ filter/scroll).
- **7 tab trạng thái:** Tất cả (mặc định) / Mới (badge đỏ 24h) / Đang xử lý (`TIEP_NHAN + DANG_XU_LY`) / Chờ phê duyệt (badge đỏ) / Đã duyệt / Công khai / Hoàn thành (read-only, gồm cả `HUY`).
- **Filter-bar:** Search full-text (tsvector) + Lĩnh vực PL (searchable) + Trạng thái (9 SM-HOIDAP) + Kênh tiếp nhận (5: DVC/CONG_PLQG/TRUC_TIEP/HE_THONG_KHAC/TVN_BRIDGE) + DatePicker Từ/Đến + [Tìm kiếm] + [Xóa bộ lọc].
- **Table columns:** Checkbox / Mã HD / Nội dung (truncate 200, tooltip 500) / Lĩnh vực / Người gửi / Kênh (5 badge màu, TVN_BRIDGE click → tooltip phiên gốc FR-13) / Trạng thái / Thời hạn (4 mức cảnh báo) / Ngày tạo (desc default) / Hạn xử lý / Hành động (Xem/Sửa/Xóa).
- **Form Drawer Thêm mới:** Mã HD (readonly auto) / Nội dung* (max 5000, counter) / Lĩnh vực* (searchable) / Tên-Email-SĐT người gửi / Doanh nghiệp (searchable) / Kênh tiếp nhận* (4 options, **TVN_BRIDGE KHÔNG hiển thị** — chỉ hệ thống ghi) / **Cơ quan tiếp nhận*** (gom nhóm TW/BN/DP, condition theo kênh — `[CR-06]`) / File đính kèm (max 20MB, virus scan) / [Hủy] + [Lưu — "Đồng ý"].
- **Action-bar batch:** Chọn tất cả + label "Đã chọn N" + [Xóa hàng loạt] (tab Tất cả/Mới/Đang xử lý) + [Phê duyệt hàng loạt] (tab Chờ PD, max 100) + [Công khai hàng loạt] (tab Đã duyệt, chỉ CB PD cùng cấp).
- **Pagination:** 20/trang default + "Hiển thị 1-20 / {total}".

#### SCR-II-02 — Chi tiết & Soạn phản hồi (toàn bộ workflow)

- **Toolbar:** Breadcrumb + [← Quay lại] + Tiêu đề "Chi tiết Hoi đáp #{ma_hoi_dap}" + Badge trạng thái + Badge SLA.
- **Stepper 6 bước:** Mới → Tiếp nhận → Đang xử lý → Chờ duyệt → Đã duyệt → Công khai/Hoàn thành (DA_TRA_LOI không hiển thị, thoáng qua).
- **2 Accordion read-only:** Thông tin câu hỏi (mặc định mở) + Approval Fields (người tiếp nhận/phân công/duyệt + lý do từ chối highlight đỏ).
- **Action bar — 10 nút context-sensitive:** [Tiếp nhận] (MOI) / [Phân công] (TIEP_NHAN/DANG_XU_LY) / [Soạn phản hồi] (DANG_XU_LY) / [Hủy yêu cầu] (MOI, không có PHAN_HOI con) / [Cập nhật thời hạn] (TIEP_NHAN/DANG_XU_LY) / [Phê duyệt] (CHO_PHE_DUYET, CB PD cùng cấp) / [Từ chối] (CHO_PHE_DUYET, modal lý do ≥10) / [Công khai] (DA_DUYET, modal 4 trường CR-01) / [Hủy công khai] (CONG_KHAI) / [Đóng hồ sơ] (DA_DUYET/CONG_KHAI, BR-FLOW-06 manual).
- **Form soạn phản hồi (DANG_XU_LY):** Dropdown Mẫu phản hồi (grouped 2 nhóm: "Mẫu khung quốc gia (TW)" + "Mẫu của đơn vị bạn" theo MPH_READ Hybrid) → prefill / Rich-text Nội dung phản hồi* / Văn bản pháp luật / Gợi ý cho DN / File đính kèm / **Checkbox "Đã trả lời"** (cảnh báo trước khi tick → auto BR-FLOW-01) / [Lưu nháp] + [Gửi phản hồi].
- **Modal Công khai** (mở từ nút [Công khai]): Upload ảnh đại diện (max 5MB) + "Dùng ảnh mặc định" / Textarea Mô tả công khai (max 2000, counter) / File đính kèm công khai (PDF/DOC/XLS, max 20MB/file, max 10 files, virus scan) / Khung preview phải / [Hủy] + [Xác nhận công khai] → gọi API Cổng PLQG → nếu OK: SET CONG_KHAI; nếu fail: giữ DA_DUYET + nút "Thử lại".
- **Accordion Lịch sử xử lý (timeline AUDIT_LOG, mặc định thu gọn).**
- **Card list phản hồi cũ** (nếu từ chối + soạn lại, mới nhất trên).

#### SCR-II-03 — Phân công xử lý (Modal trên SCR-II-02)

- **Tabs:** [Cá nhân tự do] (mặc định active) — CB/TVV/NHT cá nhân / [Tổ chức tư vấn] — Cty Luật / VP LS / TT TVPL → sau khi chọn TC mở bảng 4c chọn TVV thuộc TC.
- **Bảng gợi ý (auto-filter 4 tiêu chí FR-II-06 Step 5):** Radio / Họ tên / Đơn vị / Lĩnh vực chuyên môn / Workload hiện tại / Mức ưu tiên *(đã bỏ Q11 2026-05-07 — column này KHÔNG còn)*. **Cite SRS gốc Step 5 ở `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:470-473`** chỉ mô tả "Tải danh sách gợi ý...khớp lĩnh vực" — KHÔNG có thứ tự sort/LIMIT. Cite "workload ASC + ho_ten ASC LIMIT 10" duy nhất ở derived doc `02-thu-tu-module.md:86,116,138,370` → cần BA confirm. **TC liên quan gán nhóm C — Chờ BA confirm spec.**
- **Form:** Dropdown Tổ chức TV* (chỉ tab Tổ chức) / Dropdown Người xử lý* (2 tab) / Ghi chú / Thời hạn xử lý (override SLA mặc định).
- **Nút:** [Hủy] + [Phân công] → validate theo loại, ERR-PC-04 thiếu thông tin, ERR-PC-05 TVV không thuộc TC.

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**
- ☑ Nút [Xuất Excel] toolbar (BR-DATA-06, max 10K, WRN-HD-01).
- ☑ Pagination 20/page default, page_size IN (10, 20, 50, 100) (BR-DATA-07).
- ☑ Search sanitize max 200 ký tự (BR-EC-13).
- ☑ URL sync filter (sibling-check với FR-05 Vụ việc, FR-04 TVV).
- ☑ Audit log mọi CUD + chuyển trạng thái (BR-DATA-05).
- ☑ Optimistic lock mọi UPDATE/DELETE (BR-EC-01, BR-EC-19 batch).
- ☑ 5 trường công khai CR-01 áp dụng cả HOI_DAP + PHAN_HOI.

**Feature module KHÔNG có (cần QUOTE SRS line):**
- ❌ "Phân công mặc định" / `CAU_HINH_PHAN_CONG` Tab UI — **DEPRECATED Q11 2026-05-07** thay bằng auto-filter (`02-thu-tu-module.md:86,116,138`).
- ❌ Auto-close hồ sơ sau N ngày — BR-FLOW-06 BA chốt 2026-05-05 (`srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1626-1630`).
- ❌ Từ chối hàng loạt batch — BR-FLOW-02 nói "Từ chối phải từng bản ghi (yêu cầu lý do)".

### 2.5 State Machine SM-HOIDAP

> **Source of truth:** `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1477-1532` + `01-tong-quan-nghiep-vu.md:71-97` (LUỒNG A).

**10 trạng thái** (9 chính + HUY) — bổ sung `DA_PHAN_CONG` theo SRS `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:474,498,502,509,511` FR-II-06 Step 9 + Outputs row 5:

| # | Trạng thái | Mã | Mô tả | Badge màu |
|---|------------|-----|-------|-----------|
| 1 | Mới | `MOI` | Yêu cầu mới từ Cổng/DVC/nhập tay/TVN_BRIDGE | Xanh dương |
| 2 | Tiếp nhận | `TIEP_NHAN` | CB NV đã tiếp nhận, deadline SLA tính xong | Xanh lá |
| 3 | Đã phân công | `DA_PHAN_CONG` | CB NV đã phân công NHT/TVV/Tổ chức (FR-II-06 Step 9) — chờ người được phân công xác nhận / bắt đầu soạn | Xanh lá nhạt |
| 4 | Đang xử lý | `DANG_XU_LY` | Người được phân công đang soạn phản hồi | Vàng |
| — | (Đã trả lời) | `DA_TRA_LOI` | **Thoáng qua** — không hiển thị stepper | — |
| 5 | Chờ phê duyệt | `CHO_PHE_DUYET` | **Auto-transition từ DA_TRA_LOI (BR-FLOW-01)**, CB PD nhận thông báo | Cam |
| 6 | Đã duyệt | `DA_DUYET` | CB PD đã duyệt, sẵn sàng công khai + **auto-tạo bản ghi FR-13 Kho QA `nguon=TU_DONG`** | Xanh lá đậm |
| 7 | Công khai | `CONG_KHAI` | API push lên Cổng PLQG thành công + 5 trường CR-01 đầy đủ | Tím |
| 8 | Hoàn thành | `HOAN_THANH` | Đóng hồ sơ thủ công (BR-FLOW-06) — KHÔNG auto | Xám |
| 9 | Hủy | `HUY` | CB NV hủy ở trạng thái MOI | Đỏ |

**Transitions chính (13):**

| Từ | Đến | Trigger | Guard | Action | FR Ref | BR Ref |
|----|-----|---------|-------|--------|--------|--------|
| [*] | `MOI` | DN gửi qua Cổng / CB NV nhập tay / **TVN_BRIDGE escalate từ FR-13** | Theo nguồn: TVN_BRIDGE → ghi `kenh_tiep_nhan='TVN_BRIDGE'` + `tu_van_nhanh_goc_id` | Tạo bản ghi, sinh mã HD-YYYYMMDD-SEQ | FR-II-01, FR-13 | BR-DATA-04, BR-ROUTE-HD-01 |
| `MOI` | `TIEP_NHAN` | CB NV nhấn "Tiếp nhận" | CB NV cùng đơn vị | Ghi audit, tính deadline SLA = `ngay_tiep_nhan` + N ngày LV | FR-II-03 | BR-SLA-01, BR-CALC-03 |
| `MOI` | `HUY` | CB NV cùng đơn vị hủy yêu cầu | Không có phản hồi đang soạn | Soft delete, ghi audit | FR-II-01 | BR-DATA-01, BR-DATA-05 |
| `TIEP_NHAN` | `DA_PHAN_CONG` | CB NV phân công NHT/TVV/Tổ chức (FR-II-06 Step 9) | NHT/TVV đang HOAT_DONG (auto-filter 4 tiêu chí — cần BA confirm sort/LIMIT) | SET `trang_thai='DA_PHAN_CONG'` + `nguoi_xu_ly_id`/`to_chuc_tv_id`, gửi thông báo, ghi audit | FR-II-06 (line 474, 498, 502, 509, 511) | BR-AUTH-08, BR-DATA-05 |
| `DA_PHAN_CONG` | `DANG_XU_LY` | Người được phân công bắt đầu soạn phản hồi | NHT/TVV/CG là `nguoi_xu_ly` | Ghi audit | FR-II-07 | BR-AUTH-10 |
| `DANG_XU_LY` | `DA_TRA_LOI` | CB NV/TVV tích "Đã trả lời" | Phản hồi không rỗng | Lưu PHAN_HOI | FR-II-07 | — |
| `DA_TRA_LOI` | `CHO_PHE_DUYET` | **AUTO (hệ thống tự chuyển)** | — | Gửi thông báo CB PD cùng cấp | FR-II-07 | **BR-FLOW-01** |
| `CHO_PHE_DUYET` | `DA_DUYET` | CB PD phê duyệt (đơn / batch) | CB PD cùng cấp (BR-AUTH-05) | Ghi audit + **auto-tạo bản ghi FR-13 Kho QA** | FR-II-08 | BR-AUTH-05, BR-FLOW-02 |
| `CHO_PHE_DUYET` | `DANG_XU_LY` | CB PD từ chối | Lý do ≥10 ký tự (BR-FLOW-04) | Trả lại CB NV kèm lý do, gửi thông báo | FR-II-08 | BR-FLOW-04 |
| `DA_DUYET` | `CONG_KHAI` | CB PD cùng cấp nhấn "Công khai" | `user.role IN (CB_PD_*) AND user.don_vi.cap = record.don_vi.cap`; API Cổng PLQG OK (idempotency key) | Set `cong_khai=1` + `thoi_gian_dang_tai=NOW()` + 5 trường CR-01 | FR-II-08 | BR-FLOW-05, BR-AUTH-05, BR-EC-20 |
| `CONG_KHAI` | `DA_DUYET` | CB PD cùng cấp nhấn "Hủy công khai" | Như trên; API gỡ Cổng OK | Set `cong_khai=0`, **xóa `thoi_gian_dang_tai`** (NULL) | FR-II-08 | BR-FLOW-05 |
| `DA_DUYET` | `HOAN_THANH` | **Thủ công** click "Đóng hồ sơ" (BR-FLOW-06) | CB NV cùng don_vi HOẶC CB PD cùng cấp | Ghi audit | FR-II-08 | BR-FLOW-06, BR-AUTH-05 |
| `CONG_KHAI` | `HOAN_THANH` | **Thủ công** click "Đóng hồ sơ" (BR-FLOW-06) | Như trên | Ghi audit | FR-II-08 | BR-FLOW-06 |

> **Auto-transition annotation:** chỉ DA_TRA_LOI → CHO_PHE_DUYET là **AUTO** (BR-FLOW-01). Mọi transition khác là thủ công. **KHÔNG có auto-close HOAN_THANH** (BR-FLOW-06, BA chốt 2026-05-05).

> **Optimistic locking + Crash recovery:** mọi transition kiểm tra version field (BR-EC-01). Scheduled job mỗi 5 phút detect bản ghi trung gian > 5 phút và retry (`srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1532`). TC-EC-CRASH-RECOVERY-01 verify scheduled job 5 phút.

> **FR-13 Kho QA auto-create caveat:** Action "auto-tạo bản ghi FR-13 Kho QA" ở transition `CHO_PHE_DUYET → DA_DUYET` hiện chỉ có cite ở derived doc `01-tong-quan-nghiep-vu.md:87-97`. SRS FR-II-08 Processing line 617 chỉ ghi "Cập nhật trạng thái = DA_DUYET, người duyệt, ngày duyệt" — KHÔNG có step "INSERT INTO KHO_QA". **TC-XMOD-FR13-KHO-QA gán nhóm C — Chờ BA confirm spec** (cần grep SRS FR-13 module — `srs-fr-13-kho-qa.md` field-level contract).

### 2.6 Data dependencies & Seed / Workflow input (v3.0)

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| **GĐ 1 Seed (pure entry state)** | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | `hoi_dap_variants[1..6]` (6 variants: state × kênh × lĩnh vực) |
| **GĐ 1 click flow** | [`input/flow-module.md`](../../../input/flow-module.md) | §M7 Hỏi đáp Bước 1 (thủ công) |
| **GĐ 2 Workflow** | [`input/flow-module.md`](../../../input/flow-module.md) | §M7 Hỏi đáp Bước 1 → 12 + Phụ lục 2 preset SLA + Phụ lục 3 troubleshooting BR-FLOW-01 |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | HOI_DAP "Tạo tại SCR-II-01" "Đọc tại SCR-X2-01 Kho QA + SCR-IX báo cáo" |

**Upstream dependencies (Tier check):**

| Entity của module | Tier | Phụ thuộc entity nào (upstream) | Seed trước tại module |
|-------------------|:----:|----------------------------------|-----------------------|
| `HOI_DAP` | 3 | `DON_VI` (cây 2 tầng TW/BN/ĐP), `DANH_MUC LINH_VUC_PL`, `TAI_KHOAN` (CB NV/PD/TVV/NHT), `DOANH_NGHIEP` (optional), `CAU_HINH_SLA` | FR-10 QTHT (L1), FR-07 DN (L2), FR-04 TVV/CG/NHT (L2) |
| `PHAN_HOI` | 3 | `HOI_DAP` (parent), `MAU_PHAN_HOI` (optional, Hybrid 2 tầng), `TAI_KHOAN` (nguoi_tra_loi) | Trong cùng FR-02 |
| `MAU_PHAN_HOI` | 3 | `DANH_MUC LINH_VUC_PL`, `DON_VI`, `TAI_KHOAN` (created_by) — auto-fill `pham_vi_ap_dung` theo cấp user | FR-10 QTHT (DANH_MUC + DON_VI) + Login từng cấp |

**Cross-module impact downstream:**
- `HOI_DAP.trang_thai=DA_DUYET` → auto-tạo `KHO_QA` FR-13 (`nguon=TU_DONG`).
- `HOI_DAP.trang_thai=CONG_KHAI` → push lên Cổng PLQG qua REST API (không qua LGSP).
- Kênh `TVN_BRIDGE` → có FK `tu_van_nhanh_goc_id` về FR-13 Phiên Tư vấn nhanh.

> **Lưu ý:** KHÔNG hardcode `N records, states X/Y` ở đây — fixture đã chốt 6 variants/entity. Workflow advance state là việc của **GĐ 2 Workflow** (`workflow-test-report-fr-02.md`), không phải precondition của test plan.

---

## 3. Cấu Trúc File Test Case

```
fr-02-hoi-dap/
├── test-plan.md                              ← File này (00-test-plan-overview)
├── 01-TC-quan-ly-hoi-dap.md                  ← FR-II-01 CRUD HOI_DAP + Export
├── 02-TC-tim-kiem-tong-hop.md                ← FR-II-02 Search full-text
├── 03-TC-tiep-nhan.md                        ← FR-II-03 MOI → TIEP_NHAN + Concurrency
├── 04-TC-quan-ly-tiep-nhan.md                ← FR-II-04 Cập nhật thời hạn + Lịch sử
├── 05-TC-tim-kiem-dang-xu-ly.md              ← FR-II-05 Filter cứng TIEP_NHAN/DANG_XU_LY
├── 06-TC-phan-cong.md                        ← FR-II-06 SCR-II-03 CA_NHAN/TO_CHUC + ERR-PC-04/05/06
├── 07-TC-phan-hoi.md                         ← FR-II-07 Soạn + checkbox "Đã trả lời" BR-FLOW-01
├── 08-TC-phe-duyet-cong-khai.md              ← FR-II-08 Duyệt/Từ chối/CK/Hủy CK/Đóng/Batch
├── 09-TC-da-xu-ly.md                         ← FR-II-09 Timeline + DA_DUYET/CONG_KHAI/HOAN_THANH
├── 10-TC-tim-kiem-da-xu-ly.md                ← FR-II-10 Search trong kho đã xử lý
├── 11-TC-mau-phan-hoi-hybrid.md              ← FR-II-NEW-02 Hybrid 2 tầng TW/BN/DP scope
├── 12-TC-sla-canh-bao.md                     ← FR-II-CROSS-01 SLA 4 mức + tác vụ tự động 30 phút
├── 13-TC-permission-cross-cap.md             ← Cross-cutting: 11 role × 8 action
├── 14-TC-audit-trail.md                      ← BR-DATA-05 verify INSERT-only AUDIT_LOG
└── (15-REVIEW-edge-case-hunter.md)           ← Optional: edge case review
```

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Tổng |
|------|------:|---------:|-----:|-----:|
| 01 — Quản lý hỏi đáp (CRUD + Export) | 4 | 5 | 3 | 12 |
| 02 — Tìm kiếm tổng hợp | 2 | 3 | 2 | 7 |
| 03 — Tiếp nhận (MOI → TIEP_NHAN) | 2 | 2 | 2 | 6 |
| 04 — Quản lý tiếp nhận (cập nhật thời hạn) | 2 | 4 | 1 | 7 |
| 05 — Tìm kiếm đang xử lý | 1 | 1 | 1 | 3 |
| 06 — Phân công CA_NHAN / TO_CHUC | 4 | 6 | 2 | 12 |
| 07 — Phản hồi + BR-FLOW-01 auto-transition | 3 | 3 | 2 | 8 |
| 08 — Phê duyệt / Từ chối / CK / Hủy CK / Đóng / Batch | 6 | 6 | 4 | 16 |
| 09 — Đã xử lý + Timeline | 1 | 1 | 1 | 3 |
| 10 — Tìm kiếm đã xử lý | 1 | 1 | 1 | 3 |
| 11 — Mẫu phản hồi Hybrid 2 tầng | 3 | 4 | 2 | 9 |
| 12 — SLA 4 mức cảnh báo + cron 30 phút + ngày lễ + notification | 3 | 2 | 5 | 10 |
| 13 — Permission cross-cap (matrix 11×8) | 3 | 6 | 1 | 10 |
| 14 — Audit trail INSERT-only | 1 | 1 | 1 | 3 |
| **TỔNG** | **36** | **45** | **28** | **109** |

> Đếm trên cover ≥20 TC theo acceptance — bảng trên có **109 TC** cho 12 FR + 2 cross-cutting (bump file 12 SLA 6→10 theo review).

**Chi tiết SLA TC bump (file 12):**

| TC ID | Mô tả | Method |
|---|---|---|
| TC-SLA-DEFAULT-01 | SLA mặc định 10 ngày LV khi không cấu hình | UI |
| TC-SLA-LEVEL-01..04 | 4 mức cảnh báo BINH_THUONG/SAP_HET/QUA_HAN/QUA_HAN_NGHIEM_TRONG | Time-travel DB |
| TC-SLA-CRON-TRIGGER | Cron 30 phút trigger update `muc_do_canh_bao` | Cron simulation + curl |
| TC-SLA-CRON-SKIP-OFFHR | Cron skip ngoài giờ làm việc (nếu cấu hình OFF) | Cron simulation |
| TC-SLA-WORKDAY-01 | Ngày làm việc trừ ngày lễ FR-VIII-29 (schema 5 trường) | Time-travel DB |
| TC-SLA-NOTIF-TOGGLE | BR-SLA-03 notification on/off toggle | UI + email/in-app verify |
| TC-SLA-LEVEL-04-DEFER | "Quá hạn nghiêm trọng" — BR-SLA-02 conflict 2 vs 4 mức SCR-VIII-06 | C — Chờ BA confirm |

**Phân bổ priority:**

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc — happy path + BR core + permission) | 42 | 40% |
| P1 (quan trọng — negative + edge auto-transition + batch) | 45 | 43% |
| P2 (nên có — SLA tác vụ tự động + audit + UI quirks) | 18 | 17% |

**Phân bổ scenario coverage:**

| Scenario class | Số TC | Ghi chú |
|----------------|------:|---------|
| Workflow state machine (12 transitions) | 18 | Cover toàn bộ SM-HOIDAP including auto BR-FLOW-01 |
| Permission (11 role × 8 action) | 18 | Tập trung 13-TC-permission-cross-cap + 06 (Tổ chức) + 11 (Mẫu Hybrid) |
| CR-01 5 trường công khai | 6 | TC-WF-PUBLISH-FIELDS, TC-WF-UNPUBLISH-FIELDS |
| BR-FLOW-01 auto-transition | 3 | TC-WF-AUTO-01..03 |
| BR-FLOW-05 API Cổng PLQG + idempotency | 5 | TC-EC-PUBLISH-API-FAIL, TC-IDEM-RETRY |
| BR-FLOW-06 đóng hồ sơ thủ công | 4 | TC-WF-CLOSE-01 + TC-EC-NO-AUTOCLOSE (6 tháng test) |
| Concurrency (optimistic lock) | 6 | TC-EC-CONFLICT, ERR-TN-03, ERR-TH-CONFLICT, ERR-BATCH-CONFLICT |
| Cross-module (FR-13 auto-tạo Kho QA, TVN_BRIDGE) | 5 | TC-XMOD-FR13-KHO-QA, TC-XMOD-TVN-BRIDGE |
| SLA 4 mức + ngày làm việc | 6 | TC-SLA-LEVEL-01..04, TC-SLA-WORKDAY |
| Audit trail INSERT-only | 3 | TC-AUDIT-01..03 |
| Hybrid mẫu phản hồi 2 tầng | 9 | TC-MPH-CREATE-TW/BN/DP + TC-MPH-READ-SCOPE |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md)

- ✅ **PASS:** 100% P0 (42/42) + ≥90% P1 (≥41/45) pass.
- ❌ **FAIL:** Bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%, hoặc bất kỳ TC nào vi phạm BR-FLOW-01 (auto-transition) / BR-FLOW-05 (API Cổng PLQG) / BR-FLOW-06 (đóng hồ sơ thủ công) / BR-AUTH-05 (cùng cấp) → fail toàn module vì là core business rule.

**Status icon convention** (terminology Việt):
- ✅ Đạt · ⚠️ Sai spec (PASS but log Minor) · ❌ Lỗi · 🚫 Không test được · ⏭ Hoãn · 🤷 Không xác định (force retry method)

### 5.1 Bảng 2 — TC defer template (gom sẵn từ test plan)

> Bảng này gom các TC dự kiến defer ngay từ test plan để tester không gặp giờ chạy mới ngỡ ngàng. Update sau MỖI round → re-evaluate.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm | Nhóm |
|---|---|---|:-:|:-:|
| TC-PERM-AUTO-FILTER | Sort/LIMIT auto-filter 4 tiêu chí chỉ cite derived doc, SRS gốc FR-II-06 Step 5 (line 470-473) không nêu | BA quote nguyên văn SRS update sort+LIMIT, hoặc xác nhận `02-thu-tu-module.md:86,116,138,370` là authoritative | BA | C |
| TC-XMOD-FR13-KHO-QA | SRS FR-II-08 Processing (line 617) không có step "INSERT INTO KHO_QA" — cite chỉ ở derived doc | Grep SRS `srs-fr-13-kho-qa.md` field-level contract `kho_qa.nguon=TU_DONG` | QA seed + BA | C |
| TC-SLA-LEVEL-04 | BR-SLA-02 conflict — 4 mức SRS line 992-998 vs SCR-VIII-06 chỉ 2 ngưỡng `02-thu-tu-module.md:114` | BA chốt 2 hay 4 mức cảnh báo | BA | C |
| TC-EC-NO-AUTOCLOSE | BR-FLOW-06 đóng hồ sơ thủ công — test "6 tháng không click vẫn không auto-close" cost cao | Time-travel DB manipulation `ngay_tiep_nhan` -180 ngày + verify state = DA_DUYET/CONG_KHAI giữ nguyên | QA API | F |
| TC-FR-II-NEW-01-CONFIG | FR-II-NEW-01 status inconsistency — line 449/829/1149/1174 vẫn reference | BA quote nguyên văn line "xóa hẳn FR-II-NEW-01 khỏi SRS v3.5" | BA | C |
| TC-WF-PUBLISH-RETRY | Idempotency key retry sau timeout — chưa có sandbox API Cổng PLQG | Infra deploy mock Cổng PLQG hoặc dev expose retry endpoint | Infra / Dev BE | D |
| TC-WF-CRASH-RECOVERY | Scheduled job 5 phút detect bản ghi trung gian — cần force crash mid-transition | Dev BE expose endpoint mô phỏng crash, hoặc DBA query trực tiếp | Dev BE + DBA | D |
| TC-XMOD-TVN-BRIDGE-INBOUND | TVN_BRIDGE inbound từ FR-13 chưa unblock (Cổng PLQG endpoint) | Cổng PLQG endpoint deploy (R7.6.3 ⏳) | Infra | D |

**Nhóm phân loại** (theo CLAUDE.md §"Phân loại 6 nhóm nguyên nhân"):
- **A** Thiếu seed data · **B** Chờ dev fix bug · **C** Chờ BA confirm spec · **D** Lỗi env/chờ infra · **E** Dependency upstream chưa xong · **F** Lý do khác (cost cao / DB-only / out-of-scope)

---

## 6. Tham chiếu

- [output/test-strategy.md](../../../output/test-strategy.md) — chiến lược tổng thể
- [output/scaling-test-strategy.md](../../../output/scaling-test-strategy.md) — quy trình 7 bước onboard
- [input/srs-update-2026-5-5/srs-fr-02-hoi-dap.md](../../../input/srs-update-2026-5-5/srs-fr-02-hoi-dap.md) — SRS v3.5 (1652 dòng)
- [input/srs-v3/srs-fr-02-hoi-dap.md](../../../input/srs-v3/srs-fr-02-hoi-dap.md) — SRS v3.0 baseline
- [input/srs-v3/srs-v3.md Phụ lục B](../../../input/srs-v3/srs-v3.md) — BR cross-cutting (line 3939-4088)
- [input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md](../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) — Thay đổi v3.5
- [input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md](../../../input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md) — LUỒNG A Hỏi đáp (dòng 71-97)
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — Thứ tự seed module + dropdown source
- [tasks/system-overview.md §4.8](../../../tasks/system-overview.md) — Module 7 Hỏi đáp (3 màn SCR-II)
- [output/permission-matrix.md](../../../output/permission-matrix.md) — Ma trận phân quyền 49 entity × 11 role
- [output/template/test-case-template.md](../../../output/template/test-case-template.md) — Template TC field-level
- [output/template/bug-report-template.md](../../../output/template/bug-report-template.md) — Template bug report
- [input/users.csv](../../../input/users.csv) — Tài khoản test (suffix `_01`/`_02`/`_03`)

---

*Test plan generated 2026-05-12 theo template `test-plan-overview-template.md` v3.0 (2026-04-23) — áp dụng quy ước **SOURCE MODE: LOCAL** với cite prefix bắt buộc (`srs-update-2026-5-5/...` cho v3.5, `srs-v3/...` cho baseline). BR table 28 row, TC bảng §4 105 TC across 14 file, permission matrix 11 role × 13 action, state machine 9 trạng thái + 12 transition + auto BR-FLOW-01 annotation.*
