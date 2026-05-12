# Kế Hoạch Kiểm Thử — Báo cáo 23 loại (FR-11, SCR-IX-01)

> **Phiên bản**: 1.1 (revised 2026-05-12 — apply review feedback)
> **Ngày tạo**: 2026-05-12
> **Nguồn dữ liệu**: LOCAL — `srs-v3/srs-fr-11-bao-cao.md` (KHÔNG có file SRS update v3.5 riêng cho FR-11; v3.5 chỉ có CHANGELOG ở `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:508-602` ghi các thay đổi: (1) UC renumber +4 offset → UC124-146; (2) ĐỔI DOCX → PDF cho BC nhóm IX — KHÔNG phải thêm format hybrid; (3) Đổi tên "Hỏi đáp pháp lý" → "Hỏi đáp pháp luật"; (4) Đổi tên "Đợt đánh giá" → "Kế hoạch đánh giá"; (5) FR-IX-08 bỏ `dia_ban_id` + bỏ NHT khỏi `loai_tvv`).
> **SRS Reference**: FR-IX-01..23 (UC120-142 theo SRS v3 / UC124-146 theo v3.5), SCR-IX-01, TPL-REPORT-FULL.

> **Nhóm D — Không có SRS update v3.5 riêng cho module**: theo phân loại (CLAUDE.md §Rule 4) nhóm D smoke 5 phút + sample 5-8 loại BC đại diện thay vì test full 23 loại. Test plan này định nghĩa scope đầy đủ để dùng làm baseline; round QA cụ thể có thể sampling theo strategy §1.3.

> **⚠️ BA-Q gate đang treo (xem §2.7 BA-Q tracker):** 3 câu hỏi `BA-Q-FR11-001..003` đang chờ BA confirm — TC tương ứng mark 🚫 BLOCK cho tới khi có confirm. CẤM tự quyết PASS theo trigger force-deep-review `feedback_deep_review_before_ba_defer`.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Module:** FR-11 Báo cáo Thống kê (Nhóm IX) — 23 loại BC trên 1 màn hình duy nhất SCR-IX-01 (Unified Report Page).
- **UC range:** UC120-UC142 (SRS v3) / UC124-UC146 (SRS v3.5 sau renumber +4 offset, lý do: FR-VIII-22..25 DN module mới chiếm UC120-123 — cite `srs-v3/srs-fr-11-bao-cao.md:849`, `tasks/system-overview.md:849`).
- **Bảng dữ liệu chính:** `BAO_CAO` (18 trường, ~5,000 records/năm, growth 15%/năm — cite `srs-v3/srs-fr-11-bao-cao.md:1183-1209`).
- **Màn hình:** SCR-IX-01 — Trang Báo cáo Thống kê (UX-Spec MH-11.1, cite `srs-v3/srs-fr-11-bao-cao.md:1025-1052`).
- **Bản chất module:** Read-only — chỉ đọc dữ liệu đã `DA_DUYET`/`HOAN_THANH`/`DA_THANH_TOAN` từ các module upstream (HOI_DAP, VU_VIEC, TU_VAN_VIEN, KHOA_HOC, HO_SO_CHI_TRA, DOANH_NGHIEP, CHUONG_TRINH_HTPLDN, DOT_DANH_GIA). KHÔNG tạo entity nghiệp vụ mới (cite `srs-v3/srs-fr-11-bao-cao.md:47, 80`).
- **Lifecycle:** BAO_CAO có 3 state đơn giản `DANG_TAO → HOAN_THANH | LOI` (cite `srs-v3/srs-fr-11-bao-cao.md:1217`) — KHÔNG phải state machine workflow (xem §2.5). v3.5 (CHANGELOG, cite `tasks/system-overview.md:896-902`) thêm 5 state đợt BC: `NHAP → CHO_DUYET → DA_DUYET → DA_XUAT` (+ rejection NHAP). Test plan dùng lifecycle v3.5 vì SRS-v3 entity BAO_CAO 3-state là legacy.

### 1.2 Danh sách 23 loại BC / FR / UC

> Mapping UC v3 → v3.5 (cite `srs-v3/srs-fr-11-bao-cao.md:127-1022` + `tasks/system-overview.md:884, 849`):

| # | FR ID | UC v3 | UC v3.5 | Tên BC | Nhóm | Bộ lọc đặc thù | Biểu đồ |
|---|-------|:-----:|:-------:|--------|------|----------------|---------|
| 1 | FR-IX-01 | UC120 | UC124 | BC Số lượng hỏi đáp pháp luật/vướng mắc | Hỏi đáp | Lĩnh vực PL, Trạng thái HD | Donut + Trend |
| 2 | FR-IX-02 | UC121 | UC125 | BC Vụ việc đã tiếp nhận | Vụ việc | Kênh tiếp nhận, Lĩnh vực | Bar + Trend |
| 3 | FR-IX-03 | UC122 | UC126 | BC Vụ việc đang hỗ trợ | Vụ việc | NHT, Mức SLA | Bar snapshot |
| 4 | FR-IX-04 | UC123 | UC127 | BC Vụ việc đã hoàn thành | Vụ việc | Lĩnh vực, Kết quả | Bar + Donut |
| 5 | FR-IX-05 | UC124 | UC128 | BC Vụ việc theo thời gian | Vụ việc | — | Line trend |
| 6 | FR-IX-06 | UC125 | UC129 | BC Lớp đào tạo đang diễn ra | Đào tạo | Hình thức, Lĩnh vực | Bar snapshot |
| 7 | FR-IX-07 | UC126 | UC130 | BC Lớp đào tạo đã diễn ra | Đào tạo | Hình thức | Bar + Trend |
| 8 | FR-IX-08 | UC127 | UC131 | BC Số lượng CG/TVV | CG/TVV | Loại TVV (KHÔNG còn NHT v3.5), Lĩnh vực CM ⚠️ BA-Q-FR11-002 | Donut + Bar |
| 9 | FR-IX-09 | UC128 | UC132 | BC Đánh giá hiệu quả HTPL | Đánh giá | Kế hoạch đánh giá (v3.5 rename) | Bar + Radar |
| 10 | FR-IX-10 | UC129 | UC133 | BC Chất lượng đào tạo | Đánh giá | Khóa học | Bar + Line |
| 11 | FR-IX-11 | UC130 | UC134 | BC Vụ việc theo đơn vị quản lý | VV phân tích | — | Stacked bar |
| 12 | FR-IX-12 | UC131 | UC135 | BC Vụ việc theo lĩnh vực | VV phân tích | — | Grouped bar |
| 13 | FR-IX-13 | UC132 | UC136 | BC Vụ việc theo loại hình DN | VV phân tích | Loại DN | Grouped bar |
| 14 | FR-IX-14 | UC133 | UC137 | BC Vụ việc theo thời gian chi tiết | VV phân tích | — | Stacked trend |
| 15 | FR-IX-15 | UC134 | UC138 | BC Chi phí chi trả hỗ trợ | Chi phí | — | Bar + Summary |
| 16 | FR-IX-16 | UC135 | UC139 | BC Chi phí theo đơn vị | Chi phí | — | Bar cross-tab |
| 17 | FR-IX-17 | UC136 | UC140 | BC Chi phí theo lĩnh vực | Chi phí | Lĩnh vực | Bar |
| 18 | FR-IX-18 | UC137 | UC141 | BC Chi phí theo loại hình DN | Chi phí | Loại DN | Grouped bar |
| 19 | FR-IX-19 | UC138 | UC142 | BC Chi phí theo thời gian | Chi phí | — | Line trend |
| 20 | FR-IX-20 | UC139 | UC143 | BC Số lượng CT hỗ trợ | CT HTPLDN | Trạng thái CT | Bar + Trend |
| 21 | FR-IX-21 | UC140 | UC144 | BC CT theo đơn vị | CT HTPLDN | — | Bar cross-tab |
| 22 | FR-IX-22 | UC141 | UC145 | BC CT theo lĩnh vực | CT HTPLDN | Lĩnh vực | Bar |
| 23 | FR-IX-23 | UC142 | UC146 | BC CT theo thời gian | CT HTPLDN | — | Line trend |

> **Note SRS ambiguity**: SRS v3 dùng UC120-142 (cite `srs-v3/srs-fr-11-bao-cao.md:6, 127, 1058-1080`). v3.5 CHANGELOG ghi rõ offset +4 → UC124-146 (cite `tasks/system-overview.md:849, 884`). Trong TC viết tay dưới đây dùng UC v3.5 để đồng bộ runtime UI. Bug log phải cite cả 2: `srs-v3/srs-fr-11-bao-cao.md:XXX (UC v3) → UC v3.5`.

### 1.3 Strategy sampling 8/23 loại BC đại diện (nhóm D)

Theo phân loại nhóm D (CLAUDE.md §Rule 4 + system-overview §4.17 không có SRS update v3.5 file riêng), KHÔNG test full 23 loại mỗi round. Sampling: 1 đại diện/8 nhóm (cover đủ Hỏi đáp / Vụ việc / Đào tạo / CG-TVV / Đánh giá / Chi phí / CT HTPLDN / **VV phân tích**) + 0 high-risk extra (drop slot 8 dồn cho VV phân tích):

| Slot | BC chọn | Lý do chọn |
|:-:|---|---|
| 1 | UC124 (FR-IX-01) BC Hỏi đáp pháp luật | Đại diện nhóm Hỏi đáp — đơn giản nhất, validate flow cơ bản + verify terminology v3.5 |
| 2 | UC126 (FR-IX-03) BC VV đang hỗ trợ | Đại diện SLA computation (BR-SLA-02) + snapshot logic |
| 3 | UC129 (FR-IX-06) BC Lớp ĐT đang diễn ra | Đại diện nhóm Đào tạo — verify upstream FR-03 data |
| 4 | UC131 (FR-IX-08) BC Số lượng CG/TVV | Đại diện nhóm CG/TVV — verify v3.5 đã bỏ NHT khỏi loai_tvv + bỏ dia_ban_id (BA-Q-FR11-002) |
| 5 | UC132 (FR-IX-09) BC ĐG hiệu quả HTPL | Đại diện nhóm Đánh giá — verify radar + bar combo + Kế hoạch đánh giá (rename) |
| 6 | UC134 (FR-IX-11) BC VV theo đơn vị quản lý | **Đại diện nhóm VV phân tích — Stacked bar chart cover UC134-137** |
| 7 | UC138 (FR-IX-15) BC Chi phí chi trả | Đại diện Chi phí — verify số tiền aggregation từ HO_SO_CHI_TRA + BR-DATA-06 limit (BA-Q-FR11-003) |
| 8 | UC146 (FR-IX-23) BC CT theo thời gian | Đại diện CT HTPLDN + high-risk: trend line edge case (no data, 1 kỳ, full kỳ) + chart degrade >100 buckets |

15 loại còn lại (UC125, UC127, UC128, UC130, UC133, UC135-137, UC139-142, UC144-145) chỉ smoke 5 phút/loại (render + filter + chart render) — KHÔNG retest functional + permission đầy đủ trừ khi sample loại đại diện cùng nhóm FAIL.

### 1.4 Tài khoản & role liên quan

| Role | Cấp | Username | Dùng cho TC loại |
|------|-----|----------|------------------|
| QTHT | — | qtht_01 | Permission test (bypass scope BR-AUTH-08) |
| CB_NV_TW | TW | cb_nv_tw_01 | Functional Tạo BC + Xem + Xuất, scope toàn quốc |
| CB_NV_BN | BN | cb_nv_bn_01 (BKH) | Functional + verify scope BN + ĐP trực thuộc |
| CB_NV_DP | ĐP | cb_nv_dp_01 (STP-AG) | Functional + verify scope ĐP đơn vị |
| CB_PD_TW | TW | cb_pd_tw_01 | Workflow [Duyệt] / [Từ chối] đợt BC v3.5 |
| CB_PD_BN | BN | cb_pd_bn_01 | Cùng cấp Phê duyệt (BR-AUTH-05) |
| CB_PD_DP | ĐP | cb_pd_dp_01 | Cùng cấp Phê duyệt cấp ĐP |
| NHT | ĐP | nht_01 | Negative — không có quyền xem BC |
| TVV/CG | — | huongcg | Negative — không có quyền xem BC |
| DN | — | 9999999990 | Negative — DN không thuộc tác nhân BC |
| Sibling fallback | — | *_02 / *_03 | Account lock fallback (CLAUDE.md §Shared Rule 7) |

> Reference: [input/users.csv](../../../input/users.csv), [output/permission-matrix.md](../../../output/permission-matrix.md). Tác nhân chính: `CB Nghiệp vụ (TW/BN/ĐP)` + `CB Phê duyệt (TW/BN/ĐP)` — cite `srs-v3/srs-fr-11-bao-cao.md:49, 60`.

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|---------------------|---------------------|-----------|
| BR-AUTH-01 | Mọi user phải xác thực trước khi truy cập | `srs-v3/srs-fr-11-bao-cao.md:1240` | Yes (toàn bộ FR-IX) | "API outbound không yêu cầu session" — FR-11 KHÔNG có API outbound, ngoại lệ không áp dụng | TC-FR11-AUTH-01 (Precondition login) |
| BR-AUTH-05 | Phê duyệt cùng cấp | `tasks/system-overview.md:899` (v3.5) | Yes (workflow CHO_DUYET → DA_DUYET) | — | TC-FR11-WF-01 [Duyệt] cùng cấp |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id`. TW thấy toàn quốc, BN thấy BN + ĐP trực thuộc, ĐP chỉ thấy ĐP | `srs-v3/srs-fr-11-bao-cao.md:1246` + `:42-45` | Yes (toàn bộ FR-IX) | "QTHT bypass" — `srs-v3/srs-fr-11-bao-cao.md:1246` | TC-FR11-PERM-01..05 data isolation |
| BR-DATA-05 | Audit trail mọi thao tác CUD + xem/xuất báo cáo | `srs-v3/srs-fr-11-bao-cao.md:1252` + `:86` (Processing step 10) | Yes | — | TC-FR11-AUDIT-01 verify AUDIT_LOG INSERT khi Xem + Xuất |
| BR-DATA-06 | Export limit rows/file ⚠️ **SRS contradict 50K vs 10K — BA-Q-FR11-003** | `srs-v3/srs-fr-11-bao-cao.md:85` (50K) + `:112` (50K WRN-RPT-01) + `:1088` (50K) + `:1258` (10K BR-DATA-06) | Yes — BLOCKED chờ BA confirm | Processing step 9 quote "Giới hạn tối đa 50.000 dòng xuất; nếu vượt thì cắt + cảnh báo" (`srs-v3/srs-fr-11-bao-cao.md:85`) vs BR cross-cutting `:1258` "10,000 rows". Test plan KHÔNG tự quyết 50K — escalate BA (`feedback_deep_review_before_ba_defer`) | TC-FR11-EXPORT-04 🚫 BLOCK BA-Q-FR11-003 |
| BR-DATA-07 | Pagination default 20, max 100 | `srs-v3/srs-v3.md` Phụ lục B (cross-cutting) | Conditional | BC là Dashboard query, KHÔNG phải list CRUD — pagination áp dụng cho bảng dữ liệu trong vùng kết quả nếu >20 rows | TC-FR11-UI-PAGI-01 |
| BR-RPT-01 | CHỈ truy vấn bản ghi đã duyệt (DA_DUYET / HOAN_THANH / DA_THANH_TOAN) | `srs-v3/srs-fr-11-bao-cao.md:80` (Processing step 4) + `:47` | Yes (toàn bộ FR-IX) | — | TC-FR11-DATA-SCOPE-01..03 verify exclude CHO_DUYET / NHAP / TU_CHOI |
| BR-SLA-02 | 4 mức SLA: Bình thường (>50%), Sắp hết hạn (<50%), Quá hạn (>100%), Quá hạn nghiêm trọng (>2x) | `srs-v3/srs-fr-11-bao-cao.md:1264` + `:249` (FR-IX-03 §Processing) | Yes — chỉ FR-IX-03 (BC VV đang hỗ trợ) | — | TC-FR11-IX03-SLA-01..04 |
| BR-RPT-FILTER-01 | tu_ngay ≤ den_ngay; khoảng <= 366 ngày (trừ kỳ NAM) | `srs-v3/srs-fr-11-bao-cao.md:78` (Processing step 2) + `:109-110` (ERR-RPT-01/02) | Yes | Kỳ NAM bypass 366 days check | TC-FR11-VAL-DATE-01..03 |
| BR-RPT-FORMAT-01 | format_xuat: v3 = {XLSX, DOCX} mặc định XLSX. **v3.5 ĐỔI DOCX → PDF (CHỈ FR-11)** — KHÔNG phải thêm format hybrid ⚠️ BA-Q-FR11-001 | `srs-v3/srs-fr-11-bao-cao.md:71, 84` + `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:569-580` (v3.5 CHANGELOG) | Yes | v3.5 FR-15 KHÔNG áp đổi format — chỉ FR-11. CHANGELOG §H.3 cờ "Cần BA xác nhận TT17/2025 yêu cầu PDF hay chấp nhận DOCX" → test plan dùng PDF làm primary, DOCX BLOCK chờ BA | TC-FR11-EXPORT-FMT-01 (XLSX) + TC-FR11-EXPORT-FMT-03 (PDF v3.5) |
| BR-RPT-TIMEOUT-01 | Timeout query > 30s → ERR-RPT-03 | `srs-v3/srs-fr-11-bao-cao.md:113` + `:1089` | Yes | — | TC-FR11-ERR-TIMEOUT-01 (edge case 50K rows + filter wide) |
| BR-EC-13 | Search/filter sanitize max 200 ký tự | `srs-v3/srs-v3.md` Phụ lục B | Yes (filter text input) | — | TC-FR11-VAL-SANITIZE-01 |

> **Bổ sung BR specific module:** BR-RPT-01 (data scope đã duyệt), BR-RPT-FILTER-01 (date range), BR-RPT-FORMAT-01 (XLSX/DOCX/PDF), BR-RPT-TIMEOUT-01 (30s) — trích từ TPL-REPORT-FULL §Processing/Error Handling.

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted nguyên văn) | Severity | Nguồn |
|--------|-------------------|----------------------------------|----------|-------|
| ERR-RPT-01 | tu_ngay > den_ngay | "Ngày bắt đầu phải trước hoặc bằng ngày kết thúc" | ERROR | `srs-v3/srs-fr-11-bao-cao.md:109` |
| ERR-RPT-02 | Khoảng > 366 ngày (trừ NAM) | "Khoảng thời gian tối đa 1 năm. Sử dụng kỳ 'NAM' cho BC dài hơn" | ERROR | `srs-v3/srs-fr-11-bao-cao.md:110` |
| INF-RPT-01 | Không có dữ liệu | "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" | INFO | `srs-v3/srs-fr-11-bao-cao.md:111` + `:1051` |
| WRN-RPT-01 | Export > 50,000 rows | "Dữ liệu vượt 50.000 dòng. Hệ thống xuất 50.000 dòng đầu tiên" | WARNING | `srs-v3/srs-fr-11-bao-cao.md:112` |
| ERR-RPT-03 | Query timeout > 30s | "Truy vấn quá thời gian. Vui lòng thu hẹp khoảng thời gian hoặc bộ lọc" | ERROR | `srs-v3/srs-fr-11-bao-cao.md:113` |
| ERR-RPT-04 | Lỗi xuất file | "Không thể tạo file xuất. Vui lòng thử lại" | ERROR | `srs-v3/srs-fr-11-bao-cao.md:114` |
| ERR-RPT-05 | Không có quyền | "Bạn không có quyền xem báo cáo này" | ERROR | `srs-v3/srs-fr-11-bao-cao.md:115` |
| ERR-RPT-06 | Format xuất không hợp lệ | "Định dạng xuất chỉ hỗ trợ XLSX hoặc DOCX" | ERROR | `srs-v3/srs-fr-11-bao-cao.md:116` |
| ERR-RPT-07 | Template báo cáo hỏng | "Mẫu báo cáo không khả dụng. Vui lòng liên hệ QTHT" | ERROR | `srs-v3/srs-fr-11-bao-cao.md:117` |
| ERR-RPT-IX01-01 | Lĩnh vực không tồn tại (FR-IX-01) | "Lĩnh vực PL không tồn tại" | ERROR | `srs-v3/srs-fr-11-bao-cao.md:171` |

### 2.3 Permission Matrix (FR-11 Báo cáo)

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md)

| Action / Role | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | DN | NHT | TVV | CG |
|---------------|:----:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--:|:---:|:---:|:--:|
| Xem dropdown loại BC | R (all) | R (all) | R (all) | R (all) | R (all) | R (all) | R (all) | ❌ | ❌ | ❌ | ❌ |
| Xem SCR-IX-01 + Chạy query | R (all) | R (all) | R (BN+ĐP trực thuộc) | R (ĐP) | R (all) | R (BN+ĐP) | R (ĐP) | ❌ | ❌ | ❌ | ❌ |
| Tạo đợt BC (NHAP) | ❌ | C (TW) | C (BN) | C (ĐP) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Trình duyệt [→ CHO_DUYET] | ❌ | U own | U own | U own | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Duyệt / Từ chối BC | ❌ | ❌ | ❌ | ❌ | U (TW) | U (BN) | U (ĐP) | ❌ | ❌ | ❌ | ❌ |
| Xuất XLSX (sau DA_DUYET) | R | R | R | R | R | R | R | ❌ | ❌ | ❌ | ❌ |
| Xuất PDF v3.5 (sau DA_DUYET) | R | R | R | R | R | R | R | ❌ | ❌ | ❌ | ❌ |
| Xuất DOCX (legacy v3) ⚠️ BA-Q-FR11-001 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| Xem AUDIT_LOG (xem + xuất) | R (all) | R (own) | R (own) | R (own) | R (own) | R (own) | R (own) | ❌ | ❌ | ❌ | ❌ |

> Cite: `srs-v3/srs-fr-11-bao-cao.md:49, 60` (tác nhân chính chỉ CB NV / CB PD); `tasks/system-overview.md:881-902` (v3.5 workflow 4 state); BR-AUTH-08 `srs-v3/srs-fr-11-bao-cao.md:1246`.

### 2.4 UI Layout (SCR-IX-01)

> ⚠️ Components trích từ `srs-v3/srs-fr-11-bao-cao.md:1037-1052` (14 thành phần).

**Components:**
- **Toolbar**: Breadcrumb "Trang chủ > Báo cáo thống kê" + Tiêu đề + Nút Làm mới (cite `:1039-1040`).
- **Filter-bar**:
  - Dropdown loại BC (searchable, grouped optgroup 7 nhóm × 23 option) — cite `:1041` + `:1056-1080`.
  - Bộ lọc kỳ BC: select (TUAN/THANG/QUY/NAM/KHOANG) + date-picker — cite `:1042` + `:67`.
  - Dropdown đơn vị: auto theo phân quyền (TW/BN/ĐP) — cite `:1043`.
  - Bộ lọc đặc thù: dynamic theo loại BC — cite `:1044, 1056-1080`.
- **Action-bar**: [Xem báo cáo] (primary) + [Xuất Excel (.xlsx)] + **v3.5: [Xuất PDF (.pdf)]** thay cho [Xuất Word (.docx)] — KHÔNG phải bổ sung format thứ 3 — cite `:1045-1047` + `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:569-580`. Trạng thái cuối DOCX vs PDF chờ BA-Q-FR11-001.
- **Content/Result area**:
  - Biểu đồ (Line/Bar/Stacked/Donut/Radar tùy loại BC, toggle Hiện/Ẩn) — cite `:1048` + `:1056-1080`.
  - Bảng dữ liệu: sticky header, hàng tổng cộng bold, sort cột — cite `:1049, 1085`.
  - Skeleton loading khi đang query — cite `:1050`.
  - Empty state "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" — cite `:1051`.
  - Toast xuất file: "Đang tạo file..." → "Xuất thành công" — cite `:1052`.

**Cross-cutting features:**
- ☐ Nút [Xuất Excel] / v3.5 [Xuất PDF thay DOCX] — BR-DATA-06 limit chờ BA-Q-FR11-003 (50K vs 10K contradict SRS).
- ☐ Pagination 20/page áp dụng cho bảng dữ liệu kết quả nếu >20 rows.
- ☐ Search/filter sanitize max 200 chars (BR-EC-13) — áp filter text input.
- ☐ URL sync filter (BR-UX-01) — verify deep-link tái tạo BC.
- ☐ Audit log mọi action xem/xuất (BR-DATA-05).
- ☐ Optimistic lock UPDATE (BR-EC-01) — áp dụng đợt BC v3.5 (state transition).

**Feature module KHÔNG có (SRS quote):**
- KHÔNG có SCR-IX-02 — toàn bộ thao tác xem/lọc/xuất trong SCR-IX-01 (cite `tasks/system-overview.md:885`).
- KHÔNG có chức năng tạo entity nghiệp vụ mới — read-only (cite `srs-v3/srs-fr-11-bao-cao.md:102, 1217`).

### 2.5 State Machine

**SRS v3 (legacy):** BAO_CAO có 3 state đơn giản `DANG_TAO → HOAN_THANH | LOI` — KHÔNG cần SM diagram (cite `srs-v3/srs-fr-11-bao-cao.md:1217`).

**SRS v3.5 (CHANGELOG, cite `tasks/system-overview.md:893-902`):** Đợt BC có 4 state + 1 export state:

```
— → NHAP                  (Tạo đợt BC, actor: cb_nv_<cap>_01)
NHAP → NHAP               (Chạy aggregation, actor: cb_nv_<cap>_01)
NHAP → CHO_DUYET          ([Trình duyệt], actor: cb_nv_<cap>_01, nhập Nhận xét + Kiến nghị)
CHO_DUYET → DA_DUYET      ([Duyệt] cùng cấp, actor: cb_pd_<cap>_01, BR-AUTH-05)
CHO_DUYET → NHAP          ([Từ chối], actor: cb_pd_<cap>_01, lý do ≥10 ký tự)
DA_DUYET → DA_XUAT        ([Xuất file] Word/Excel/PDF TT17/2025, actor: cb_nv_<cap>_01)
```

> **Note:** Workflow đợt BC v3.5 là superset của lifecycle BAO_CAO v3 3-state. Test plan này dùng v3.5 vì runtime UI dùng v3.5 (cite `tasks/system-overview.md:881-902`). v3 vẫn áp dụng cho aggregation engine (DANG_TAO/HOAN_THANH/LOI là transient state khi chạy query).

### 2.6 Data dependencies & Seed input

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| GĐ 1 Seed upstream | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | Tất cả entity variants cần state cuối (DA_DUYET/HOAN_THANH/DA_THANH_TOAN) |
| GĐ 1 click flow | [`input/flow-module.md`](../../../input/flow-module.md) | §M16 Báo cáo (chạy query 4 nhóm BC) |
| GĐ 2 Workflow | [`input/flow-module.md`](../../../input/flow-module.md) | §M16 transition NHAP → CHO_DUYET → DA_DUYET → DA_XUAT |
| Cross-module map | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | BAO_CAO read từ HOI_DAP / VU_VIEC / TU_VAN_VIEN / KHOA_HOC / HO_SO_CHI_TRA / DOANH_NGHIEP / CT_HTPLDN / DOT_DANH_GIA |

**Upstream dependencies (Tier check + per-filter coverage):**

| Entity nguồn | Tier | State cần | Module seed trước | Acceptance per-filter (CLAUDE.md §"Quy tắc seed task") | Cite |
|-------------|:----:|-----------|-------------------|--------------------------------------------------------|------|
| HOI_DAP | 3 | DA_TRA_LOI / CHO_TRA_LOI | FR-02 Hỏi đáp | ≥1 record/đơn vị {TW, BN×2 BKH+BTC, ĐP×2 STP-AG+STP-HN} × ≥3 lĩnh vực PL × ≥3 kỳ BC (THANG/QUY/NAM) | `srs-v3/srs-fr-11-bao-cao.md:147-148, 1103` |
| VU_VIEC | 3 | DA_TIEP_NHAN / DANG_XU_LY / HOAN_THANH | FR-05 Vụ việc | ≥1 record/state × ≥1 record/đơn vị (TW+BN+ĐP) × ≥3 lĩnh vực × ≥4 mức SLA (BR-SLA-02) | `srs-v3/srs-fr-11-bao-cao.md:201, 245, 290, 1104` |
| TU_VAN_VIEN | 2 | HOAT_DONG | FR-04 CG/TVV | ≥1 record/loại {CG, TVV} (NHT đã bỏ v3.5) × ≥3 lĩnh vực CM × ≥2 địa bàn (verify FR-IX-08 BA-Q-FR11-002) | `srs-v3/srs-fr-11-bao-cao.md:1105` + `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:542-549` |
| KHOA_HOC | 3 | DANG_DIEN_RA / HOAN_THANH | FR-03 Đào tạo | ≥1 record/state × ≥1 record/hình thức {OFFLINE, ONLINE} × ≥3 lĩnh vực | `srs-v3/srs-fr-11-bao-cao.md:1107` |
| HO_SO_CHI_TRA | 4 | DA_THANH_TOAN | FR-06 Chi trả | ≥3 record/đơn vị (TW+BN+ĐP) × ≥3 lĩnh vực × ≥3 kỳ + ≥1 case >50K rows aggregate (BA-Q-FR11-003) | `srs-v3/srs-fr-11-bao-cao.md:1108` |
| DOANH_NGHIEP | 1 | HOAT_DONG | FR-07 DN | ≥1 record/loại DN × ≥3 lĩnh vực kinh doanh × ≥3 quy mô | `srs-v3/srs-fr-11-bao-cao.md:1106` |
| BAO_CAO_DANH_GIA + KE_HOACH_DANH_GIA (v3.5 rename) | 4 | DA_DUYET | FR-08 ĐG HQ | ≥1 record/đợt × ≥3 lĩnh vực × ≥3 kỳ (CHANGELOG line 556-560 "Đợt đánh giá" → "Kế hoạch đánh giá") | `srs-v3/srs-fr-11-bao-cao.md:478` + `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:556-560` |
| CT_HTPLDN | 4 | DA_CONG_BO / DANG_THUC_HIEN | FR-15 CT HTPLDN | ≥1 record/state × ≥1 record/đơn vị × ≥3 lĩnh vực × ≥12 tháng (cho UC146 trend line) | `tasks/system-overview.md:888` |

> **Iron rule (CLAUDE.md §Rule 1 seed actor):** BAO_CAO read-only nên KHÔNG cần seed BAO_CAO entity. Phải verify per-filter query downstream TRƯỚC khi đóng task seed (vd `?lĩnh vực=PL_DAT_DAI&kỳ=THANG&donVi=BKH → ≥1` cho mỗi combo). Filter coverage không gộp tổng — tránh pattern A5 R5 fail.

### 2.7 BA-Q tracker (gate cho TC tương ứng — KHÔNG tự PASS)

> Theo `feedback_deep_review_before_ba_defer`: mọi spec contradiction → mark 🚫 BLOCK + escalate BA, KHÔNG tự quyết PASS hoặc mark Sai spec mà không retry.

| Q ID | Câu hỏi | Cite SRS | TC gate | Trạng thái |
|------|---------|----------|---------|:----------:|
| BA-Q-FR11-001 | v3.5 đã ĐỔI DOCX → PDF (CHỈ FR-11) hay giữ song song DOCX + PDF? TT17/2025 chấp nhận DOCX hay yêu cầu PDF? | `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:569-580` + §H.3 cờ "Cần BA xác nhận" | TC-FR11-EXPORT-FMT-02 (DOCX legacy), TC-FR11-EXPORT-FMT-03 (PDF v3.5) | 🚫 BLOCK |
| BA-Q-FR11-002 | FR-IX-08 v3.5 đã bỏ `dia_ban_id` Inputs + bỏ NHT khỏi `loai_tvv` (CHANGELOG line 542-549), nhưng Output `theo_dia_ban[]` + SCR optgroup vẫn nhắc "Địa bàn" — contradiction C.2. Spec cuối là bỏ hay giữ? | `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:542-549, 597` | TC-FR11-IX08-01, TC-FR11-IX08-02 | 🚫 BLOCK |
| BA-Q-FR11-003 | BR-DATA-06 export limit là 50K (Processing step 9 `:85`) hay 10K (BR `:1258` cross-cutting)? | `srs-v3/srs-fr-11-bao-cao.md:85, 112, 1088, 1258` (contradict 4 chỗ) | TC-FR11-EXPORT-04 (boundary) | 🚫 BLOCK |

**Action workflow khi BA confirm:**
1. Update spec quote vào dòng tương ứng §2.1 BR / §2.2 Error / §2.3 Permission.
2. Flip TC gate từ 🚫 → 🟢 trong todo.md.
3. Re-run TC theo spec confirmed.
4. Log decision vào `tasks/decisions/` nếu spec mâu thuẫn được giải quyết.

---

## 3. Cấu Trúc File Test Case

```
fr-11-bao-cao/
├── test-plan.md                          ← File này (overview)
├── todo.md                               ← Task tracker (auto-generated)
├── 01-TC-FR11-AUTH.md                    ← Auth + Permission TC (cross-role)
├── 02-TC-FR11-IX01-hoi-dap-PL.md         ← Functional UC124 BC Hỏi đáp pháp luật
├── 03-TC-FR11-IX03-vv-dang-ho-tro.md     ← Functional UC126 BC VV đang hỗ trợ + SLA
├── 04-TC-FR11-IX06-lop-dt-dang-dien-ra.md ← Functional UC129 BC Đào tạo
├── 05-TC-FR11-IX08-cg-tvv.md             ← Functional UC131 BC CG/TVV (🚫 BA-Q-002)
├── 06-TC-FR11-IX09-dg-hieu-qua.md        ← Functional UC132 BC ĐG hiệu quả (Kế hoạch ĐG)
├── 07-TC-FR11-IX15-chi-phi.md            ← Functional UC138 BC Chi phí
├── 08-TC-FR11-IX11-IX20-vv-phantich-ct.md ← Functional UC134 (VV phân tích) + UC143 (CT)
├── 09-TC-FR11-IX23-ct-theo-tg.md         ← Functional UC146 BC CT theo thời gian + chart perf
├── 10-TC-FR11-EXPORT.md                  ← Export XLSX/PDF/DOCX + 50K boundary (🚫 BA-Q-001/003)
├── 11-TC-FR11-WORKFLOW.md                ← Workflow đợt BC NHAP → DA_XUAT (v3.5)
├── 12-TC-FR11-EDGE-AUDIT.md              ← Edge cases + Audit log split (16 verify point)
├── 13-TC-FR11-SMOKE-15-loai-con-lai.md   ← Smoke 5 phút × 15 loại không sample
└── (14-REVIEW-edge-case-hunter.md)       ← Optional: review từ bmad-review-edge-case-hunter
```

### 3.1 Template Bảng 1 + Bảng 2 (round QA chạy update — không phải test-plan baseline)

> Theo CLAUDE.md §"Functional/Workflow report — 2 bảng tổng hợp BẮT BUỘC". Round QA chạy R{N} sẽ điền vào `output/qa-reports/round{N}-*/functional/fr-11-bao-cao/functional-test-report-r{N}-fr11.md`.

**Bảng 1 — Trạng thái toàn bộ TC (snapshot R{N} LATEST):** aggregate 51 TC × cột Status × Round phát hiện × Note ≤15 từ. Update sau MỖI round.

**Bảng 2 — TC chưa chạy được + cần làm gì:** aggregate TC non-PASS theo 6 nhóm A-F (xem [`output/template/tc-block-classification-template.md`](../../../output/template/tc-block-classification-template.md)). Cột "Vì sao" 1-20 từ, cột "Cần làm gì" ≤25 từ, cột "Ai làm" pick `Dev BE / Dev FE / QA seed / QA API / BA / Infra`.

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Tổng |
|------|:-----:|:--------:|:----:|:----:|
| 01 Auth + Permission | 2 | 7 | 0 | 9 |
| 02 FR-IX-01 Hỏi đáp pháp luật | 2 | 1 | 1 | 4 |
| 03 FR-IX-03 VV đang hỗ trợ + SLA | 2 | 1 | 1 | 4 |
| 04 FR-IX-06 Đào tạo | 1 | 1 | 0 | 2 |
| 05 FR-IX-08 CG/TVV (🚫 BLOCK BA-Q-002) | 1 | 1 | 0 | 2 |
| 06 FR-IX-09 ĐG hiệu quả (Kế hoạch ĐG) | 1 | 1 | 0 | 2 |
| 07 FR-IX-15 Chi phí | 1 | 1 | 0 | 2 |
| 08 FR-IX-11 + FR-IX-20 (VV phân tích + CT) | 2 | 0 | 0 | 2 |
| 09 FR-IX-23 CT theo TG (+ chart perf) | 1 | 0 | 2 | 3 |
| 10 Export (🚫 BLOCK BA-Q-001/003) | 2 | 1 | 2 | 5 |
| 11 Workflow đợt BC v3.5 | 3 | 2 | 1 | 6 |
| 12 Edge cases + Audit log | 2 | 3 | 5 | 10 |
| **TỔNG** | **20** | **19** | **12** | **51** |

> **Strategy sampling:** 23 loại BC × ~10 TC/loại = 230 TC nếu test full. Reduce theo nhóm D + sampling §1.3 còn ~51 TC chính + 15 smoke 5 phút (loại không sample) = 66 TC tổng — giảm 71% công sức.

**Phân bổ priority:**

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc — Auth + Permission + Workflow + 8 sample happy path + Export happy + Audit) | 27 | 53% |
| P1 (quan trọng — Negative + Edge SLA + date validation + Boundary reason) | 16 | 31% |
| P2 (nên có — Smoke 15 loại còn lại + Edge timeout + chart degrade) | 8 | 16% |

**TC đang 🚫 BLOCK BA-Q (xem §2.7):** 6 TC — TC-FR11-IX08-01/02 (BA-Q-002), TC-FR11-EXPORT-FMT-02/03 (BA-Q-001), TC-FR11-EXPORT-04 (BA-Q-003), TC-FR11-IX08-01 đếm 1 lần.

**Detailed TC list (43 TC):**

| TC ID | File | Tên | Type | Priority |
|---|---|---|---|:-:|
| TC-FR11-AUTH-01 | 01 | Login `cb_nv_tw_01` mở SCR-IX-01 thành công | Happy | P0 |
| TC-FR11-AUTH-02 | 01 | Login NHT nht_01 → menu BC ẩn (UI-level) | Negative | P0 |
| TC-FR11-AUTH-02b | 01 | NHT nht_01 deep-link `/bao-cao` → 403 ERR-RPT-05 (permission-level) | Negative | P0 |
| TC-FR11-AUTH-02c | 01 | TVV `huongcg` + CG cùng deep-link /bao-cao → 403 ERR-RPT-05 | Negative | P0 |
| TC-FR11-PERM-01 | 01 | `cb_nv_tw_01` chạy BC UC124 → thấy data toàn quốc (BR-AUTH-08) | Happy | P0 |
| TC-FR11-PERM-02 | 01 | `cb_nv_bn_01` (BKH) chạy BC UC124 → CHỈ thấy BN BKH + ĐP trực thuộc | Negative | P0 |
| TC-FR11-PERM-03 | 01 | `cb_nv_dp_01` (STP-AG) chạy BC UC124 → CHỈ thấy STP-AG, dropdown đơn vị locked | Negative | P0 |
| TC-FR11-PERM-04 | 01 | `dn_9999999990` truy cập SCR-IX-01 → 403 ERR-RPT-05 | Negative | P0 |
| TC-FR11-PERM-05 | 01 | `qtht_01` chạy BC UC124 → bypass scope, thấy all (ngoại lệ BR-AUTH-08) | Negative | P0 |
| TC-FR11-IX01-01 | 02 | UC124 "BC Hỏi đáp **pháp luật**" kỳ Quý + đơn vị TW → tổng HD, tỷ lệ trả lời, donut + trend + verify wording "pháp luật" (v3.5 rename, KHÔNG còn "pháp lý") | Happy | P0 |
| TC-FR11-IX01-02 | 02 | UC124 filter lĩnh vực PL cụ thể → chỉ HD thuộc lĩnh vực | Happy | P1 |
| TC-FR11-IX01-03 | 02 | UC124 với lĩnh vực_id không tồn tại → ERR-RPT-IX01-01 | Negative | P1 |
| TC-FR11-IX01-04 | 02 | UC124 với HD state CHO_DUYET (chưa duyệt) → KHÔNG đếm vào BC (BR-RPT-01) | Edge | P1 |
| TC-FR11-IX03-01 | 03 | UC126 snapshot VV đang xử lý + tổng theo SLA 4 mức | Happy | P0 |
| TC-FR11-IX03-02 | 03 | UC126 filter NHT cụ thể → chỉ VV phân công NHT đó | Happy | P1 |
| TC-FR11-IX03-03 | 03 | UC126 filter muc_sla = QUA_HAN → chỉ VV quá deadline | Negative | P1 |
| TC-FR11-IX03-04 | 03 | UC126 verify công thức BR-SLA-02: 4 mức (<50%, 50-100%, 100-200%, >200%) | Edge | P0 |
| TC-FR11-IX06-01 | 04 | UC129 snapshot lớp ĐT DANG_DIEN_RA | Happy | P0 |
| TC-FR11-IX06-02 | 04 | UC129 filter hình thức ONLINE → chỉ lớp online | Negative | P1 |
| TC-FR11-IX08-01 | 05 | UC131 BC số lượng CG/TVV theo loại × lĩnh vực CM (v3.5 bỏ địa bàn — BA-Q-FR11-002) — verify dropdown loai_tvv KHÔNG có NHT | Happy | P0 🚫 BLOCK BA-Q-FR11-002 |
| TC-FR11-IX08-02 | 05 | UC131 filter loại TVV = CG → chỉ CG (NHT đã bỏ — verify dropdown 2 option) | Negative | P1 🚫 BLOCK BA-Q-FR11-002 |
| TC-FR11-IX09-01 | 06 | UC132 BC ĐG hiệu quả với "Kế hoạch đánh giá" DA_DUYET (v3.5 rename) → Radar + Bar | Happy | P0 |
| TC-FR11-IX09-02 | 06 | UC132 "Kế hoạch đánh giá" state CHO_DUYET_BC → KHÔNG đếm (BR-RPT-01) | Negative | P1 |
| TC-FR11-IX15-01 | 07 | UC138 BC Chi phí với HSCT DA_THANH_TOAN → sum đúng | Happy | P0 |
| TC-FR11-IX15-02 | 07 | UC138 với HSCT CHO_DUYET → KHÔNG đếm (BR-RPT-01) | Negative | P1 |
| TC-FR11-IX11-01 | 08 | UC134 BC VV theo đơn vị quản lý — Stacked bar chart cover nhóm VV phân tích | Happy | P0 |
| TC-FR11-IX20-01 | 08 | UC143 BC số lượng CT hỗ trợ với CT DA_CONG_BO | Happy | P0 |
| TC-FR11-IX23-01 | 09 | UC146 BC CT theo thời gian, kỳ NAM 2025 → Line trend 12 tháng | Happy | P0 |
| TC-FR11-IX23-02 | 09 | UC146 với 0 CT trong kỳ → empty state INF-RPT-01 | Edge | P1 |
| TC-FR11-IX23-03 | 09 | UC146 kỳ NAM 2025 × 30 ngày = 365 buckets → verify chart render KHÔNG degrade (perf < 3s) | Edge | P2 |
| TC-FR11-EXPORT-FMT-01 | 10 | Sau Xem BC → [Xuất Excel] → download .xlsx TT17/2025 đúng format | Happy | P0 |
| TC-FR11-EXPORT-FMT-02 | 10 | [Xuất DOCX] legacy v3 → download .docx (CHỈ test nếu BA-Q-FR11-001 confirm DOCX giữ) | Negative | P1 🚫 BLOCK BA-Q-FR11-001 |
| TC-FR11-EXPORT-FMT-03 | 10 | v3.5 [Xuất PDF] → download .pdf (CHỈ FR-11, KHÔNG FR-15) | Happy | P0 🚫 BLOCK BA-Q-FR11-001 |
| TC-FR11-EXPORT-04 | 10 | BC > 50K rows → WRN-RPT-01 + xuất 50K đầu (50K vs 10K contradict) | Edge | P1 🚫 BLOCK BA-Q-FR11-003 |
| TC-FR11-EXPORT-05 | 10 | format_xuat invalid (CSV) → ERR-RPT-06 | Edge | P2 |
| TC-FR11-WF-01 | 11 | `cb_nv_tw_01` Tạo NHAP → Trình duyệt → CHO_DUYET → cb_pd_tw_01 [Duyệt] → DA_DUYET (BR-AUTH-05 cùng cấp) | Happy | P0 |
| TC-FR11-WF-02 | 11 | DA_DUYET → [Xuất file] → DA_XUAT | Happy | P0 |
| TC-FR11-WF-03 | 11 | CHO_DUYET → cb_pd_bn_01 [Duyệt] BC cấp TW → 403 (BR-AUTH-05 sai cấp) | Negative | P0 |
| TC-FR11-WF-04 | 11 | CHO_DUYET → [Từ chối] lý do < 10 ký tự → validation error | Negative | P1 |
| TC-FR11-WF-05 | 11 | CHO_DUYET → [Từ chối] lý do = 10 ký tự (boundary) → PASS chuyển NHAP | Happy | P1 |
| TC-FR11-WF-06 | 11 | CHO_DUYET → [Từ chối] lý do > 500 ký tự → sanitize cắt 500 (BR-EC-13) | Edge | P2 |
| TC-FR11-EDGE-01 | 12 | Validation tu_ngay > den_ngay → ERR-RPT-01 | Negative | P0 |
| TC-FR11-EDGE-02 | 12 | Validation khoảng 367 ngày (kỳ KHOANG) → ERR-RPT-02 | Negative | P0 |
| TC-FR11-EDGE-03 | 12 | Kỳ NAM với khoảng 2 năm → bypass ERR-RPT-02 (ngoại lệ) | Edge | P1 |
| TC-FR11-EDGE-04 | 12 | Query timeout > 30s → ERR-RPT-03 | Edge | P2 |
| TC-FR11-EDGE-05 | 12 | Filter text input > 200 ký tự → sanitize cắt còn 200 (BR-EC-13) | Edge | P2 |
| TC-FR11-EDGE-06 | 12 | Không có dữ liệu → INF-RPT-01 + empty state | Edge | P1 |
| TC-FR11-EDGE-07 | 12 | Template báo cáo hỏng → ERR-RPT-07 | Edge | P2 |
| TC-FR11-EDGE-08 | 12 | URL deep-link tái tạo BC: paste URL có filter → BC tự load đúng filter | Edge | P2 |
| TC-FR11-AUDIT-01 | 12 | 8 sample loại × 2 action (Xem + Xuất) = 16 verify point → AUDIT_LOG INSERT đầy đủ (curl API check) | Happy | P0 |
| TC-FR11-AUDIT-02 | 12 | Verify audit row: user_id + action + bao_cao_id + timestamp + ip_address (BR-DATA-05) | Happy | P1 |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md)

- ✅ **PASS:** 100% P0 (27 TC, exclude 🚫 BLOCK BA-Q) + 90% P1 (≥15/16 TC) pass. Sample 8 loại BC đều render + filter + xuất đúng format. Verify terminology v3.5 ("Hỏi đáp pháp luật", "Kế hoạch đánh giá") áp dụng đúng.
- ❌ **FAIL:** Bất kỳ P0 nào FAIL (exclude TC 🚫 BLOCK BA-Q), hoặc P1 pass rate < 90%. Đặc biệt FAIL cứng nếu:
  - BR-AUTH-08 data isolation broken (cấp dưới thấy data cấp trên).
  - BR-RPT-01 broken (BC đếm cả bản ghi CHO_DUYET / NHAP).
  - BR-AUTH-05 broken (PD cấp khác duyệt được BC cấp khác).
  - UC v3.5 không apply (UI vẫn dùng UC v3 → broken cross-link).
  - Terminology v3.5 không apply (vẫn hiện "Hỏi đáp pháp lý" / "Đợt đánh giá" — regression risk).
- 🚫 **BLOCK (KHÔNG kết luận PASS/FAIL):** 6 TC chờ BA-Q-FR11-001/002/003 confirm — mark BLOCK nhóm C (chờ BA spec) theo template.

**Sampling fallback:** Nếu 1 trong 8 loại sample FAIL functional → escalate test thêm 1 loại nữa cùng nhóm. Nếu cả nhóm FAIL → đẩy lên nhóm B/A → test full nhóm đó.

---

## 6. Tham chiếu

- [output/test-strategy.md](../../../output/test-strategy.md) — chiến lược tổng thể QA
- [output/scaling-test-strategy.md](../../../output/scaling-test-strategy.md) — quy trình 7 bước
- [input/srs-v3/srs-fr-11-bao-cao.md](../../../input/srs-v3/srs-fr-11-bao-cao.md) — SRS gốc 1268 dòng (cite path: `srs-v3/srs-fr-11-bao-cao.md`)
- [input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md](../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) — CHANGELOG line 508-602 cho FR-11
- [input/srs-v3/srs-v3.md Phụ lục B](../../../input/srs-v3/srs-v3.md) — BR cross-cutting
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md §⑭ FR-11](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — workflow đợt BC v3.5
- [tasks/system-overview.md §4.17 M16](../../../tasks/system-overview.md) — module overview + v3.5 CHANGELOG note
- [output/permission-matrix.md](../../../output/permission-matrix.md) — ma trận phân quyền
- [output/template/test-case-template.md](../../../output/template/test-case-template.md) — template TC field-level
- [output/template/bug-report-template.md](../../../output/template/bug-report-template.md) — template bug report
- [output/template/tc-block-classification-template.md](../../../output/template/tc-block-classification-template.md) — 6 nhóm A-F phân loại TC BLOCK

---

*Test plan v1.1 revised 2026-05-12 12:30:00. Nhóm D scope — sampling 8/23 loại BC + smoke 15 loại còn lại. UC numbering theo v3.5 (UC124-146) để đồng bộ runtime UI; SRS cite path dùng `srs-v3/srs-fr-11-bao-cao.md` vì KHÔNG có file SRS update v3.5 riêng cho FR-11 + `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` cho 5 thay đổi v3.5. 3 BA-Q gate đang treo (xem §2.7).*
