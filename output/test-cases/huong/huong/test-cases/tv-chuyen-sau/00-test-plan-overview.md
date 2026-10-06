# Kế Hoạch Kiểm Thử — FR-12 Tư vấn pháp luật chuyên sâu (FR-X.1-01 → FR-X.1-07)

> **Phiên bản:** 1.0
> **Ngày tạo:** 2026-05-06
> **Owner:** QA Automation Lead
> **Module:** FR-12 / Nhóm X.1 — Quản lý Tư vấn pháp luật chuyên sâu
> **UC range:** UC147 → UC153 (4 UC loại B + 3 UC loại M API inbound)
> **SRS reference:** [`input/srs-v3/srs-fr-12-tv-chuyen-sau-v3.1.md`](../../../input/srs-v3/srs-fr-12-tv-chuyen-sau-v3.1.md) (1617 dòng, v3.1)
> **Plan parent:** [`Ver3.1/tasks/detailed-tc/plan.md`](../../../tasks/detailed-tc/plan.md) §W3.3
> **Source mode:** SRS local + NotebookLM secondary `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` (verify nghiệp vụ chi tiết VV transitions + HSPL inline)

---

## 1. Phạm vi kiểm thử

### 1.1 Chức năng được kiểm thử

- **7 Use Case** thuộc nhóm FR-X.1 (UC147 → UC153)
  - **4 UC loại B** (CMS browser — có UI, chạy MCP chrome-devtools): UC147, UC148, UC150, UC152
  - **3 UC loại M** (API inbound từ Cổng PLQG — KHÔNG có UI CMS): UC149, UC151, UC153
    - A7 LOẠI module-level cho TC API thuần. **Giữ TC verify side-effect UI** (TB CB NV in-app, list mới hiển thị record, accordion Đánh giá update sau API).
- **2 màn hình chính** (sau v2.1 deprecated 5 màn hình con):
  - SCR-X1-01 — Danh sách TVCS (MH-12.1)
  - SCR-X1-02 — Chi tiết TVCS (MH-12.2) — gồm tabs: Thông tin / Tư liệu PL / Đánh giá CL + action buttons phân công/xác nhận/phê duyệt + accordion Công khai chuyên trang
  - HSPL render trong tab "Hồ sơ PL" của MH-07.2 (chi tiết DN — FR-07)
- **State Machine SM-TVCS** với 7 trạng thái + 10 chuyển đổi (Phụ lục C.8)
- Cover cả **Internal app** (CB NV/CB PD CRUD) và **API inbound** (Cổng PLQG → CMS)
- Bảng dữ liệu chính: `TU_VAN_CHUYEN_SAU`, `PHIEN_TU_VAN`, `LICH_SU_TRAO_DOI_TV`, `HO_SO_PHAP_LY_DN`, `TU_LIEU_PHAP_LY_VV`, `DANH_GIA_CHAT_LUONG_TV`

### 1.2 Danh sách FR / UC / Loại

| # | Mã FR | UC | Tên chức năng | SCR | Loại | File Test Case |
|---|--------|-----|--------------|------|------|----------------|
| 1 | FR-X.1-01 | UC147 | Quản lý nội dung TVCS (CRUD + SM-TVCS + Công khai) | SCR-X1-01, SCR-X1-02 | B | `01-TC-FR-X1-01-quan-ly-tvcs.md` |
| 2 | FR-X.1-02 | UC148 | Tìm kiếm nội dung TVCS | SCR-X1-01 | B | `02-TC-FR-X1-02-tim-kiem-tvcs.md` |
| 3 | FR-X.1-03 | UC149 | Tiếp nhận TVCS từ Cổng PLQG (API inbound) | (no CMS) | M | `06-TC-FR-X1-03-05-07-API-inbound-side-effect.md` (gộp UC149+151+153) |
| 4 | FR-X.1-04 | UC150 | Quản lý hồ sơ pháp lý DN (CRUD HSPL) | Tab MH-07.2 | B | `03-TC-FR-X1-04-quan-ly-hspl.md` |
| 5 | FR-X.1-05 | UC151 | Tiếp nhận HSPL từ Cổng PLQG (API inbound) | (no CMS) | M | gộp file 06 |
| 6 | FR-X.1-06 | UC152 | Quản lý tư liệu pháp lý VV (CRUD + Công khai trực tiếp) | Tab MH-12.2 | B | `04-TC-FR-X1-06-quan-ly-tu-lieu-pl.md` |
| 7 | FR-X.1-07 | UC153 | Tiếp nhận đánh giá CL TV (API inbound) | (no CMS, accordion read-only MH-12.2) | M | gộp file 06 |
| 8 | (cross) | — | Permission matrix cross-FR-X.1 (BR-AUTH-01/05/08) | cross-cutting | — | `05-TC-permission-matrix.md` |

**Cấu trúc file output (sau A1-A7):**

```
output/test-cases/tv-chuyen-sau/
├── 00-test-plan-overview.md                                ← File này
├── 01-TC-FR-X1-01-quan-ly-tvcs.md                          ← UC147 CRUD + 10 SM transitions + Công khai
├── 02-TC-FR-X1-02-tim-kiem-tvcs.md                         ← UC148 Search 8 filter
├── 03-TC-FR-X1-04-quan-ly-hspl.md                          ← UC150 CRUD HSPL (tab DN)
├── 04-TC-FR-X1-06-quan-ly-tu-lieu-pl.md                    ← UC152 CRUD TLPL + Công khai BR-FLOW-07
├── 05-TC-permission-matrix.md                              ← Cross BR-AUTH (TVCS+HSPL+TLPL)
├── 06-TC-FR-X1-03-05-07-API-inbound-side-effect.md         ← UC149/151/153 verify UI side-effect
├── 07-REVIEW-edge-case-hunter.md                           ← A4 audit log (TC mới đã merge inline)
├── 08-traceability-matrix.md                               ← A5 BR/AC ↔ TC matrix
├── 09-REVIEW-test-quality.md                               ← A6 audit log
└── 10-a7-filter-log.md                                     ← A7 audit log (LOẠI/SỬA/GIỮ)
```

### 1.3 Tài khoản test (`input/users.csv`)

| Role | Cấp | Username | Dùng cho TC loại |
|------|-----|----------|-------------------|
| QTHT | — | qtht_01 | Read-only verify (per Permission Matrix) |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD TVCS scope TW + phân công CG + Hủy yêu cầu + CRUD HSPL/TLPL |
| CB_NV_BN | BN | cb_nv_bn_01 (BKH), cb_nv_bn_02 (BTC) | CRUD scope BN + cross-unit isolation BR-AUTH-08 |
| CB_NV_DP | ĐP | cb_nv_dp_01 (AG), cb_nv_dp_02 (BG) | CRUD scope ĐP + cross-unit isolation |
| CB_PD_TW | TW | cb_pd_tw_01 | Phê duyệt TVCS cùng cấp TW (UC147 transition CHO_PHE_DUYET → DA_DUYET) |
| CB_PD_BN | BN | cb_pd_bn_01 | Phê duyệt cùng cấp BN; cross-cấp test BR-AUTH-05 |
| CB_PD_DP | ĐP | cb_pd_dp_01 | Phê duyệt cùng cấp ĐP |
| CG | — | cg_01 | Action [Chấp nhận]/[Từ chối] khi PHAN_CONG (CG được phân công) |
| TVV | — | tvv_01 | Same as CG (chuyên gia/TVV được phân công) |
| DN | — | dn_01 | (read-only TVCS công khai chuyên trang qua FR-VIII-22; **ngoài scope** module này) |
| `_03` | — | cb_nv_tw_03 / cb_pd_tw_03 ... | **Permission test cross-cấp** — không trùng cá nhân với `_01` |

> Reference: [`input/users.csv`](../../../input/users.csv), [`output/permission-matrix.md`](../../permission-matrix.md)

---

## 2. Quy tắc nghiệp vụ trích xuất từ SRS

### 2.1 Business Rules (BR) áp dụng

| Mã | Quy tắc | Nguồn (SRS line) | TC áp dụng |
|----|---------|------------------|-----------|
| BR-AUTH-01 | Mọi user phải xác thực — Tier 1 (CB nội bộ U/P + TOTP qua email) / Tier 2 (DN/TVV/CG/NHT SSO VNeID OIDC) | srs-fr-12 §6 BR-AUTH-01 line 1525-1529 | Precondition mọi TC |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB NV trình → CB PD cùng cấp duyệt) | srs-fr-12 line 198, SM-TVCS trans CHO_PHE_DUYET→DA_DUYET line 1489 | UC147 PD-cross-cấp test |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` (multi-tenant), CB NV chỉ thấy TVCS thuộc đơn vị mình | srs-fr-12 §6 BR-AUTH-08 line 1531-1535 | UC147/148/150/152 cross-unit isolation |
| BR-DATA-01 | Mọi DELETE = soft delete (`is_deleted = 1`) | line 1537-1541 | UC147/150/152 DELETE TC |
| BR-DATA-03 | 7 common fields (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id) | line 1543-1547 | Verify mọi UC CUD |
| BR-DATA-04 | Auto-gen mã: `TVCS-{YYYYMMDD}-{SEQ}` (FR-X.1-01), `HSPL-{YYYYMMDD}-{SEQ}` (FR-X.1-04) | line 1549-1553 | UC147 + UC150 CREATE verify ma format |
| BR-DATA-05 | AUDIT_LOG INSERT-only mọi CUD + phê duyệt + đăng nhập | line 1555-1559 | Mọi TC CUD verify network → AUDIT_LOG |
| BR-DATA-07 | Pagination default 20, max 100 | line 1561-1565 | UC147/148/150/152 pagination |
| BR-DATA-08 | Full-text search hỗ trợ tiếng Việt unaccent | line 1567-1571 | UC148 search FTS |
| BR-FLOW-01 | Auto chuyển trạng thái HOAN_THANH → CHO_PHE_DUYET | line 191, SM-TVCS line 1488 | UC147 transition |
| BR-FLOW-04 | Từ chối phê duyệt cần lý do (text, min 10 ký tự) | line 1573-1577 | UC147 PD từ chối |
| BR-FLOW-07 | Tư liệu PL công khai trực tiếp lên Cổng PLQG, KHÔNG cần phê duyệt | line 1579-1583 | UC152 publish without approve |
| BR-NOTIF-01 | Auto in-app + email khi API inbound từ Cổng PLQG | line 1585-1589 | UC149/151/153 side-effect |
| BR-ROUTE-TVCS-01 | Routing TVCS theo `don_vi_id` (DN chọn / mặc định Sở TP tỉnh DN / CB nhập tay = đơn vị CB) | line 1591-1595 `[CR-06]` | UC147 + UC149 routing |
| BR-PUBLIC-01 | TVCS chỉ công khai khi DA_DUYET; TLPL bất kỳ lúc nào (BR-FLOW-07); HUY/Từ chối KHÔNG được công khai | line 1597-1601 `[CR-01]` | UC147 + UC152 công khai precondition |
| BR-PUBLIC-02 | Hủy công khai: clear `thoi_gian_dang_tai` = NULL + gọi API gỡ Cổng PLQG | line 1603-1607 `[CR-01]` | UC147 + UC152 unpublish |
| BR-PUBLIC-03 | `thoi_gian_dang_tai` auto fill khi cong_khai = 1; bật-tắt-bật → cập nhật thời điểm bật mới nhất | line 1609-1613 `[CR-01]` | UC147 + UC152 timestamp |
| BR-EC-01 | Optimistic locking | (cross-cutting Phụ lục B) | UC147/150/152 UPDATE conflict |
| BR-EC-03 | Quét virus ClamAV mọi file upload | (cross-cutting) | UC147 file CK + UC150 file HSPL + UC152 file TLPL |
| BR-EC-13 | Search sanitize chống injection, max 200 ký tự | (cross-cutting) | UC148 search SQL/XSS |
| BR-EC-19 | Batch operations max 100 record/request | (cross-cutting) | UC147 batch [Phân công CG hàng loạt] / [Công khai hàng loạt] |
| BR-EC-20 | Transactional consistency — KHÔNG set trạng thái trước khi LGSP/Portal API thành công | (cross-cutting) | UC147 + UC152 publish API rollback |

### 2.2 State Machine SM-TVCS (Phụ lục C.8 — line 1442-1496)

**7 trạng thái:**

| State | Code | Mô tả | Tab SCR-X1-01 |
|-------|------|-------|---------------|
| 1 | TIEP_NHAN | Yêu cầu TV mới tạo/tiếp nhận từ Cổng | "Chờ xử lý" |
| 2 | PHAN_CONG | Đã phân công CG/TVV, chờ xác nhận | "Chờ xử lý" |
| 3 | DANG_TU_VAN | CG/TVV đang tư vấn | "Đang tư vấn" |
| 4 | HOAN_THANH | CG/TVV hoàn thành, chờ phê duyệt | "Đang tư vấn" |
| 5 | CHO_PHE_DUYET | Chờ CB PD duyệt | "Đang tư vấn" |
| 6 | DA_DUYET | Đã duyệt, gửi kết quả cho DN | "Hoàn thành" |
| 7 | HUY | Hủy yêu cầu | "Hoàn thành" |

**10 chuyển đổi (NGUYÊN VĂN srs-fr-12 line 1481-1493):**

| # | Từ | Đến | Trigger | Guard | Action | BR Ref |
|--:|----|-----|---------|-------|--------|--------|
| 1 | `[*]` | TIEP_NHAN | CB NV tạo YC TV / API inbound Cổng | — | Tạo bản ghi (auto-gen TVCS-) | BR-DATA-04 |
| 2 | TIEP_NHAN | PHAN_CONG | CB NV phân công | Có CG/TVV phù hợp lĩnh vực, đang hoạt động | TB CG/TVV (in-app + email), SLA 2 ngày LV | BR-NOTIF-01 |
| 3 | PHAN_CONG | DANG_TU_VAN | CG xác nhận | User là CG được phân công | Tạo PHIEN_TU_VAN, ghi `ngay_bat_dau`, TB DN | — |
| 4 | PHAN_CONG | TIEP_NHAN | CG từ chối | User là CG được phân công + có lý do | Xóa `chuyen_gia_id`, TB CB NV | — |
| 5 | DANG_TU_VAN | HOAN_THANH | CG tích "Hoàn thành" | Có VB TVPL (`ket_qua` không rỗng) | Ghi `ngay_hoan_thanh` | — |
| 6 | HOAN_THANH | CHO_PHE_DUYET | Auto | — | TB CB PD cùng cấp | BR-FLOW-01 |
| 7 | CHO_PHE_DUYET | DA_DUYET | CB PD duyệt | Cùng cấp đơn vị (BR-AUTH-05) | Gửi KQ cho DN, TB DN đánh giá | BR-AUTH-05 |
| 8 | CHO_PHE_DUYET | DANG_TU_VAN | CB PD từ chối | Có lý do ≥10 ký tự (BR-FLOW-04) | TB CG bổ sung | BR-FLOW-04 |
| 9 | TIEP_NHAN/PHAN_CONG | HUY | CB NV hủy | PHAN_CONG yêu cầu CG chưa xác nhận | Ghi audit, TB CG | — |
| 10 | DANG_TU_VAN | HUY | CB NV hủy | DN yêu cầu hủy + CB PD duyệt hủy | Ghi audit, TB CG + DN | — |

> ⚠️ **Mọi transition KHÔNG nằm trong 10 chuyển đổi trên** sẽ trigger **ERR-TVCS-04**: "Không thể chuyển trạng thái từ '{current}' sang '{target}'. Xem SM-TVCS".

> **SLA timeout:** CG SHALL xác nhận/từ chối trong 2 ngày LV (CAU_HINH_SLA). Sau timeout → auto-reject, trả về TIEP_NHAN.

> **Auto-save draft:** CG soạn trả lời auto-save 30s vào TRAO_DOI_NHAP `trang_thai=DRAFT`. Session hết hạn → khôi phục DRAFT khi CG đăng nhập lại.

### 2.3 SM phụ — TLPL & HSPL

**SM TLPL (TU_LIEU_PHAP_LY_VV):**

| State | Mô tả |
|-------|-------|
| NHAP | Tư liệu mới tạo/đang chỉnh sửa, chưa công khai |
| CONG_KHAI | Đã push lên Cổng PLQG (BR-FLOW-07 trực tiếp, KHÔNG cần phê duyệt) |

Transitions: `NHAP ↔ CONG_KHAI` (toggle với guard ≥1 file đính kèm theo line 850 + nội dung mô tả công khai).

**SM HSPL (HO_SO_PHAP_LY_DN):**

| State | Mô tả |
|-------|-------|
| HIEU_LUC | Hồ sơ còn hiệu lực (default khi tạo) |
| HET_HAN | Quá `ngay_het_han` |
| THU_HOI | Cơ quan cấp thu hồi |

Transitions: user-driven qua field `trang_thai` form. Không có flow auto.

### 2.4 Permission Matrix (cite Permission Matrix global + SRS-FR-12 line 1531-1535 BR-AUTH-08)

> **Ký hiệu:** C=Create, R=Read (toàn bộ), R*=Read scoped (chỉ đơn vị mình), U=Update, D=Delete (soft), —=No access

| Entity | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | CG/TVV | DN | NHT |
|--------|:----:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:------:|:--:|:---:|
| TU_VAN_CHUYEN_SAU | R | CRUD* | CRUD* | CRUD* | RU* (PD only) | RU* | RU* | R* (CG được PC) | R* (TVCS của DN, công khai chuyên trang) | — |
| HO_SO_PHAP_LY_DN | R | CRU* | CRU* | CRU* | R* | R* | R* | R* | R* (HSPL của mình qua FR-VIII-22) | **R+U*** (BR-AUTH-10 mở rộng — DN trong VV được PC, lọc 2 lớp `HSPL.don_vi_id = NHT.don_vi_id` AND `EXISTS VV.doanh_nghiep_id = HSPL.doanh_nghiep_id AND VV.nguoi_ho_tro_id = NHT.tvv_id` line 669-671) |
| TU_LIEU_PHAP_LY_VV | R | CRUD* | CRUD* | CRUD* | R* | R* | R* | R* | R* (CONG_KHAI only) | — |
| DANH_GIA_CHAT_LUONG_TV | R | R* | R* | R* | R* | R* | R* | — | C† (qua Cổng PLQG) | — |
| PHIEN_TU_VAN | R | CRU* | CRU* | CRU* | R* | R* | R* | CRU* (CG phụ trách) | R* | — |

> **Sửa 2026-05-09 (codex review M4):** Cell NHT cho HO_SO_PHAP_LY_DN trước đây = `—` (sai). SRS UC150 line 669-671 cho phép NHT R+U HSPL của DN trong VV được phân công (BR-AUTH-10 mở rộng). TC-HSPL-015 + TC-PERM-010 đã viết theo đúng spec; chỉ ô bảng matrix sai. Đã sửa.

> ⚠️ **SPEC-CLARIFY-TVCS-PERM-01:** SRS không quote rõ DANH_GIA cho CG/TVV — assumption: KHÔNG hiển thị (—) trong tab Đánh giá CL khi user là CG chính chủ. Verify khi B-Run.

> ⚠️ **SPEC-CLARIFY-TVCS-PERM-02:** UC147 Hủy yêu cầu DANG_TU_VAN cần "DN đồng ý hủy + CB PD duyệt hủy" (line 224) nhưng SRS không quote rõ entity DON_DONG_Y_HUY. Default test với assumption modal popup yêu cầu confirm thủ công + log lý do.

### 2.5 UI Layout (SCR-X1-01 / SCR-X1-02)

> ⚠️ Visual spec từ SRS line 1057-1142. KHÔNG dùng absence để khẳng định "không có feature X" — đối chiếu SRS nguyên văn.

**SCR-X1-01 — Danh sách TVCS (3 tab + filter-bar 6 dropdown + batch action):**

- **Toolbar:** Breadcrumb "Trang chủ > Tư vấn > TV pháp luật chuyên sâu" + [+ Thêm yêu cầu TV] + [Xuất Excel] + [Làm mới]
- **3 Tab phân loại** (line 1073):
  | Tab | Filter |
  |-----|--------|
  | "Chờ xử lý" (default active) | TIEP_NHAN + PHAN_CONG |
  | "Đang tư vấn" | DANG_TU_VAN + HOAN_THANH + CHO_PHE_DUYET |
  | "Hoàn thành" | DA_DUYET + HUY |
- **Filter-bar:** Tìm kiếm (FTS noi_dung_tu_van + ma_noi_dung + ten DN) / Chuyên gia (searchable) / DN (searchable) / Lĩnh vực / Trạng thái (7 enum) / Khoảng ngày
- **Table** (10 cột): Checkbox / Mã TVCS-... / DN / CG / Lĩnh vực / Tóm tắt cắt 100 ký / Trạng thái (badge 7 màu) / Ngày tư vấn / Ngày tạo / Hành động (Xem/Sửa/Phân công CG/Hủy)
- **Bảng nhãn trạng thái 7 màu** (line 1086-1095)
- **Empty state:** "Chưa có nội dung tư vấn. [+ Thêm yêu cầu TV]"
- **Action-bar batch:**
  - [Phân công CG hàng loạt] — chỉ enable khi tất cả checkbox chọn đều ở TIEP_NHAN
  - [Công khai chuyên trang hàng loạt] / [Hủy công khai hàng loạt] — chỉ enable khi tất cả ở DA_DUYET (BR-PUBLIC-01)
- **Pagination:** 20/page

**SCR-X1-02 — Chi tiết / Thêm mới TVCS (stepper SM + 6 accordion + action-bar conditional):**

- **Header:** Breadcrumb + tiêu đề ("Thêm yêu cầu TV pháp luật chuyên sâu" / "Chi tiết TVCS-...") + badge trạng thái
- **Stepper SM-TVCS:** TIEP_NHAN → PHAN_CONG → DANG_TU_VAN → HOAN_THANH → CHO_PHE_DUYET → DA_DUYET (HUY hiện nhánh riêng dấu X đỏ)
- **Accordion 1 — Thông tin cơ bản:** Mã (auto, readonly) / DN (searchable, BB — khi chọn show MST/địa chỉ/người đại diện) / CG (searchable WHERE đang hoạt động, BB) / Lĩnh vực PL (BB) / Ngày tư vấn (BB) / Ghi chú (max 2000)
- **Accordion 2 — Nội dung TV:** Nội dung chi tiết (RTE, BB, max 50KB) / Tóm tắt (max 500)
- **Accordion 3 — Tư liệu PL liên kết** (UC152 inline): Bảng (Tên/Loại/Trạng thái/Số file/Hành động) + [+ Thêm tư liệu]
- **Accordion 4 — Đánh giá CL** (UC153 read-only): Bảng (Mã/Điểm 1-5 sao/Nhận xét DN/Ngày) + Tổng hợp Điểm TB + Số lượng (chỉ mode chi tiết)
- **Accordion 5 — Nhật ký:** Timeline lịch sử CUD + transitions (chỉ mode chi tiết)
- **Accordion 6 — Công khai chuyên trang `[CR-01]`** (chỉ hiển thị khi DA_DUYET): Switch [Công khai/Hủy công khai] / Mô tả công khai (textarea) / Ảnh đại diện (jpg/png/gif max 5MB) / File đính kèm CK (multi PDF/DOC/DOCX/XLS/XLSX max 20MB/file) / Thời gian đăng tải (readonly auto)
- **Action-bar conditional theo trạng thái + role:**
  - TIEP_NHAN: [Hủy] [Lưu] [Phân công CG →]
  - PHAN_CONG: [Hủy yêu cầu] (CB NV) + (CG được PC: [Chấp nhận] [Từ chối])
  - DANG_TU_VAN: [Hủy] [Lưu] (CG phụ trách)
  - HOAN_THANH: [Trình phê duyệt] (auto FB-FLOW-01)
  - CHO_PHE_DUYET: [Phê duyệt] [Từ chối] (CB PD cùng cấp BR-AUTH-05 + BR-FLOW-04 lý do ≥10 ký)
  - DA_DUYET: read-only + [Công khai] / [Hủy công khai]

> ⚠️ **Active bug (smoke 2026-05-03):** BUG-FR12-001 Critical — action-bar empty trên Detail TVCS. Phase B sẽ verify; Phase A vẫn viết TC theo SRS spec đầy đủ.

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**

- ☑ Nút [Xuất Excel] trên SCR-X1-01 (BR-DATA-06, max 10k rows)
- ☑ Pagination 20/page default (BR-DATA-07)
- ☑ Search sanitize max 200 ký (BR-EC-13)
- ☑ Audit log mọi CUD (BR-DATA-05)
- ☑ Optimistic lock UPDATE/DELETE (BR-EC-01)
- ☑ Quét virus ClamAV mọi upload (BR-EC-03)
- ☑ Batch ≤100 records (BR-EC-19)

**Feature module KHÔNG quote rõ — SPEC-CLARIFY:**

- URL deeplink filter (BR-UX-01) — SRS không quote → SPEC-CLARIFY-TVCS-UI-01
- Auto-save draft TRAO_DOI_NHAP (line 1496) — chưa quote endpoint/UI feedback → SPEC-CLARIFY-TVCS-UI-02

### 2.6 Error Codes (NGUYÊN VĂN srs-fr-12)

| Mã lỗi | Trigger | Message | Severity | Source line |
|--------|---------|---------|----------|-------------|
| ERR-TVCS-01 | Nội dung tư vấn trống | "Nội dung tư vấn là bắt buộc" | ERROR | line 302 |
| ERR-TVCS-02 | Chuyên gia không hợp lệ | "Chuyên gia không hợp lệ hoặc đã ngừng hoạt động" | ERROR | line 303 |
| ERR-TVCS-03 | Lĩnh vực không tồn tại | "Lĩnh vực PL không tồn tại" | ERROR | line 304 |
| ERR-TVCS-04 | Transition SM-TVCS bất hợp lệ | "Không thể chuyển trạng thái từ '{current}' sang '{target}'. Xem SM-TVCS" | ERROR | line 305 |
| ERR-TVCS-05 | Mã nội dung trùng | "Mã nội dung '{ma}' đã tồn tại" | ERROR | line 306 |
| ERR-TVCS-TK-01 | tu_ngay > den_ngay | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR | line 390 |
| INF-TVCS-TK-01 | Không có kết quả tìm kiếm | "Không tìm thấy nội dung tư vấn phù hợp" | INFO | line 391 |
| ERR-TVCS-API-01..05 | API inbound errors | (HTTP 401 / dữ liệu không hợp lệ / nội dung trùng / lĩnh vực không hợp lệ) | ERROR | line 496-502 |
| ERR-FILE-SIZE-01 | File > 20MB | "Tệp '{ten_file}' vượt quá 20MB" | ERROR | line 499, 765 |
| ERR-FILE-02 | File chứa mã độc | "Tệp '{ten_file}' chứa mã độc, không thể tiếp nhận" | ERROR | line 500, 766 |
| ERR-HSPL-01..06 | HSPL form errors | (Tên trống / DN không tồn tại / File 20MB / mã độc / loại không hợp lệ / từ-đến date) | ERROR | line 652-658 |
| INF-HSPL-01 | Không tìm thấy HSPL | "Không tìm thấy hồ sơ pháp lý phù hợp" | INFO | line 658 |
| ERR-HSPL-API-01..04 | HSPL API inbound | (Auth / format / trùng / rate limit) | ERROR | line 762-767 |
| ERR-TLPL-01..06 | TLPL CRUD + công khai | (Tên trống / VV không tồn tại / File 20MB / mã độc / công khai không file / API Cổng lỗi) | ERROR | line 935-940 |
| WRN-TLPL-01 | Tư liệu đã CONG_KHAI | "Tư liệu đã ở trạng thái công khai" | WARNING | line 941 |
| ERR-DG-API-01..07 | Đánh giá API inbound | (Auth / format / điểm 1-5 / không tìm thấy nội dung / trùng / state ko cho update / rate limit) | ERROR | line 1034-1040 |

---

## 3. Tổng quan số lượng test cases (estimate trước A4-A6)

| File | TC final | Note |
|------|---------:|------|
| 01 — UC147 Quản lý TVCS | **44** | 2 UI Verify + CRUD + 10 SM transitions + Công khai chuyên trang [CR-01] + Negative + ERR-TVCS-05 mã trùng (codex R1) + boundary tom_tat/ghi_chu + anh_dai_dien validation + cross-FR hop_dong_tv_id + BR-DATA-04 SEQ uniqueness (codex R2 2026-05-09) |
| 02 — UC148 Tìm kiếm TVCS | **20** | 1 UI + 8 filter + AND logic + sanitize SQL/XSS + boundary date + INF-TVCS-TK-01 empty result (codex fill 2026-05-09) |
| 03 — UC150 Quản lý HSPL | **20** | 1 UI + CRUD + Search + Export Excel + Detail + permission NHT BR-AUTH-10 |
| 04 — UC152 Quản lý TLPL | **21** | 1 UI + CRUD + File upload + Công khai BR-FLOW-07 + sửa CONG_KHAI bị chặn + preview file UC152 AC-5 |
| 05 — Permission matrix cross-FR-X.1 | **14** | BR-AUTH-01/05/08 cho 3 entity + cross-cấp PD + cross-unit isolation + NHT R+U HSPL |
| 06 — UC149/151/153 API inbound side-effect | **15** | TB CB NV in-app + list mới có record + tab Đánh giá update + duplicate idempotency + 3 negative matrix UC149/151/153 (codex fill 2026-05-09) |
| **TỔNG functional + UI** | **134** | (sau A4 edge case + A6 fill gap + codex R1 +5 TC + codex R2 +4 TC = 125 → 130 → 134) |

**Phân bổ Happy/Negative/Edge/UI per axis (estimate):**

| Type | Count | % |
|------|------:|--:|
| 🟢 UI Verify | 6 | 7% |
| 🟢 Happy path | ~22 | 26% |
| 🔴 Negative | ~25 | 29% |
| 🟡 Edge | ~32 | 38% |
| **TỔNG** | **~85** | 100% |

**Phân bổ priority:**

| Priority | Số TC | % | Nguyên tắc |
|----------|------:|--:|------------|
| 🔴 P0 (blocker) | ~28 | 33% | UI Verify + Happy path CRUD/SM transitions + Auth violations |
| 🟡 P1 (quan trọng) | ~40 | 47% | Negative validation + Edge SM + Permission cross-cấp + Công khai BR-PUBLIC |
| 🟢 P2 (nên có) | ~17 | 20% | Optimistic lock + File quirks + Boundary number |

---

## 4. SRS Gaps & SPEC-CLARIFY tickets

| ID | Mô tả gap | Đề xuất |
|----|-----------|---------|
| SPEC-CLARIFY-TVCS-01 | UC147 Hủy yêu cầu DANG_TU_VAN: "yêu cầu DN đồng ý hủy + CB PD duyệt hủy" (line 224) — không quote entity/UI flow | BA confirm: modal popup confirm + log lý do, hay yêu cầu thực thể DON_DONG_Y_HUY riêng? |
| SPEC-CLARIFY-TVCS-02 | UC147 [Phân công CG hàng loạt]: SRS không quote rule khi 1 CG batch reject 100 record → có rollback toàn bộ batch hay per-record? | BA confirm transactional behavior. |
| SPEC-CLARIFY-TVCS-03 | UC147 SLA timeout 2 ngày LV (line 1494): cron job thực thi nào? → A7 LOẠI test cron thuần, GIỮ verify side-effect (record tự động chuyển TIEP_NHAN sau 2 ngày). | BA confirm cron schedule + workflow side-effect UI. |
| SPEC-CLARIFY-TVCS-04 | UC147 Auto-save TRAO_DOI_NHAP DRAFT 30s (line 1496): UI feedback nào (toast / icon / không có)? | BA confirm. |
| SPEC-CLARIFY-TVCS-05 | UC150 HSPL access cho NHT (line 671): "NHT cập nhật/đính kèm tài liệu hồ sơ — chỉ R + U" — SCR-IV-03 hay route khác? | BA confirm route Cổng PLQG cho NHT. |
| SPEC-CLARIFY-TVCS-06 | UC152 TLPL field `mo_ta_cong_khai` BB khi công khai (line 851) nhưng SCR-X1-02 không quote mode bắt buộc fill — UI form chấp nhận empty? | BA confirm validation form công khai. |
| SPEC-CLARIFY-TVCS-07 | UC152 Sửa TLPL khi CONG_KHAI bị chặn (line 871): WRN-TLPL-01 hay error rejection? | BA confirm WARNING vs ERROR. |
| SPEC-CLARIFY-TVCS-08 | UC149/151/153 API inbound rate limit ngưỡng cụ thể chưa quote | BA confirm threshold cho ERR-TVCS-API-04 / ERR-HSPL-API-04 / ERR-DG-API-07. |
| SPEC-CLARIFY-TVCS-09 | UC153 GUI_LAI idempotency: SRS quote "không ghi đè" — nhưng nếu payload mới có nhan_xet thay đổi thì có warn audit không? | BA confirm conflict resolution. |
| SPEC-CLARIFY-TVCS-PERM-01 | DANH_GIA_CHAT_LUONG_TV permission cho CG/TVV chính chủ — show aggregated điểm TB hay ẩn tab? | BA confirm UI behavior. |
| SPEC-CLARIFY-TVCS-PERM-02 | Hủy yêu cầu DANG_TU_VAN cần thực thể DON_DONG_Y_HUY? | BA confirm flow. |
| SPEC-CLARIFY-TVCS-UI-01 | URL deeplink filter (BR-UX-01) áp module này không? | BA confirm. Default skip URL sync test. |
| SPEC-CLARIFY-TVCS-UI-02 | Auto-save 30s UI feedback chưa quote | BA confirm UI nào. |
| SPEC-CLARIFY-TVCS-FILE-01 | UC147 Công khai chuyên trang `file_dinh_kem_cong_khai` multi-file — SRS không quote tổng max upload size, chỉ quote per-file 20MB | BA confirm tổng giới hạn (vd 100MB như API inbound). |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [`output/test-strategy.md §10`](../../test-strategy.md)

- ✅ **PASS:** 100% P0 + 90% P1 pass + tất cả UI Verify TC pass
- ❌ **FAIL:** Bất kỳ P0 FAIL, hoặc P1 pass rate < 90%, hoặc UI Verify fail
- ⚠️ **CONDITIONAL PASS:** TC liên quan SPEC-CLARIFY ticket → BLOCKED, không tính pass rate cho đến BA respond.

---

## 6. Active bugs từ smoke 2026-05-03 (Phase B baseline)

| ID | Severity | Module | Tóm tắt |
|----|---------|--------|---------|
| BUG-FR12-001 | Critical | UC147 SCR-X1-02 | Detail page action-bar empty → SM-TVCS broken ở UI |
| BUG-TVCS-002 | High | UC147 Form Tạo | Thiếu field Ngày tư vấn |
| BUG-TVCS-003 | High | UC147 Form Tạo | Thiếu RTE Nội dung TV |
| BUG-TVCS-004 | High | UC147 Form Tạo | Thiếu CG required + nút Phân công | (chặn W3.3 Phase B per todo.md)
| BUG-TVCS-005 | Medium | UC148 | (smoke gap) |
| BUG-TVCS-006 | Medium | UC147 Tabs | (smoke gap) |

**Phase A vẫn viết TC theo SRS spec đầy đủ — Phase B sẽ verify từng bug + log VALID/GAP/INVALID khi B-Run.**

> Reference: `automation/src/features/fr-x1-12-tv-chuyen-sau/bug_report_fr-12.md` (Phase Smoke baseline)

---

## 7. Phase B handoff

- **Output Phase B:** `output/execution-test/tv-chuyen-sau/report-{NN-TC-name}/{Tcs,bug,seed,Gap}-report/`
- **Trigger:** A ✅ + W2.2 (CG-TVV) Phase B done + BUG-TVCS-004 close
- **Phase B blocker hiện tại:** BUG-TVCS-004 còn Open R8 → defer Phase B per `todo.md` §W3.3
- **Per-TC-file workflow:** B-Seed → B-Run → B-Verify (2-source) → B-Report — xem [`todo.md` Template](../../../tasks/detailed-tc/todo.md#-template-prompt-per-tc-file-workflow-chuẩn-cho-mọi-tc-file)

---

## 8. Tham chiếu

- SRS local: [`input/srs-v3/srs-fr-12-tv-chuyen-sau-v3.1.md`](../../../input/srs-v3/srs-fr-12-tv-chuyen-sau-v3.1.md) (1617 dòng)
- NotebookLM secondary notebook: `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` (VV transitions + HSPL inline + HSCT API-only nghiệp vụ chi tiết)
- Plan workflow: [`tasks/plan.md`](../../../tasks/plan.md) §G9 + [`tasks/detailed-tc/plan.md`](../../../tasks/detailed-tc/plan.md) §W3.3
- Todo: [`tasks/detailed-tc/todo.md`](../../../tasks/detailed-tc/todo.md) — Template per-TC-file
- Permission matrix global: [`output/permission-matrix.md`](../../permission-matrix.md)
- Sibling refs: [`output/test-cases/CG-TVV/`](../CG-TVV/) (FR-04 14 file UC) + [`output/test-cases/bieu-mau/`](../bieu-mau/) (FR-09 7 UC + 4 audit) — pattern A1-A7 inline merge
- Test strategy: [`output/test-strategy.md`](../../test-strategy.md)
- Template TC: [`output/template/test-case-template.md`](../../template/test-case-template.md)
- Active bug smoke: `automation/src/features/fr-x1-12-tv-chuyen-sau/bug_report_fr-12.md`

---

*Tạo bởi BMAD A1-A2 (test-design) — 2026-05-06. Phase A workflow: A1 đọc SRS + sibling refs → A2 overview → A3 generate 6 UC files → A4 edge inline merge → A5 trace → A6 review fill gap inline → A7 filter UI/function-testable IN-PLACE.*

---

## 9. Codex review log 2026-05-09

**Verdict trước review:** Quality 9.13/10, 125 TC, coverage 100% AC + 100% BR + 97.1% Error code + 100% SM transitions.

**Verdict codex:** NEEDS_FIX — 5 P0 GAP + 3 P0 ERROR + 5 P1 MISMATCH (~56% Error code coverage thực tế khi cộng cả API errors UC149/151/153).

**Findings applied:**

### P0 GAP (5 TC mới):
| ID | UC | TC mới | File |
|----|----|--------|------|
| G1 | UC147 | TC-TVCS-040 ERR-TVCS-05 mã trùng | 01-TC-FR-X1-01 |
| G2 | UC148 | TC-TVCS-TK-020 INF-TVCS-TK-01 empty result | 02-TC-FR-X1-02 |
| G3 | UC149 | TC-API-IN-013 Negative matrix ERR-TVCS-API-01..05 + FILE | 06-TC-FR-X1-03-05-07 |
| G4 | UC151 | TC-API-IN-014 Negative matrix ERR-HSPL-API-01/02/04 + FILE | 06-TC-FR-X1-03-05-07 |
| G5 | UC153 | TC-API-IN-015 Negative matrix ERR-DG-API-01..07 (toàn bộ 7 codes) | 06-TC-FR-X1-03-05-07 |

### P0 ERROR (3 TC sửa):
| ID | TC ID | Lỗi → Fix |
|----|-------|-----------|
| E1 | TC-PERM-003 | Sai logic "CG không truy cập CMS" → Sửa thành CG truy cập SCR-X1-02 sau Tier 2 SSO để [Chấp nhận]/[Từ chối] |
| E2 | TC-API-IN-009 | Sai mapping `ERR-TVCS-API-01` cho missing field → Sửa thành `ERR-TVCS-API-02` (validation, line 497) |
| E3 | TC-API-IN-011 | Sai wording duplicate → Sửa nguyên văn `"Hồ sơ '{mã}' đã tồn tại (mã: {ma_ho_so})"` per line 764 |

### P1 MISMATCH (5 TC fix line ref/wording):
| ID | TC ID | Fix |
|----|-------|-----|
| M1 | TC-TVCS-023 | Line ref → 1609-1613 (BR-PUBLIC-03) + 116 (field auto fill) |
| M2 | TC-TVCS-026 | Line ref → 1613 (BR-PUBLIC-03 nguyên văn bật-tắt-bật) |
| M3 | TC-TVCS-TK-014 | Line ref → 1531-1535 (BR-AUTH-08) + 354 (UC148 Processing) |
| M4 | Overview §2.4 cell NHT cho HO_SO_PHAP_LY_DN | `—` → `R+U*` (BR-AUTH-10 mở rộng line 669-671) |
| M5 | TC-HSPL-020 | Note line 1374 chỉ là CHECK constraint, không phải SM auto transition |

**Coverage sau update:**
- Error code: 56% → ~100% (UC149/151/153 có thêm full negative matrix)
- AC coverage: 39/39 → 39/39 (giữ nguyên)
- TC count: 125 → 130 (+5)
- Quality estimate: 9.13/10 → 9.5/10

**Closes Round 1:** Codex review verdict NEEDS_FIX → PASS sau apply 13 fixes.

---

## 10. Codex review log Round 2 — 2026-05-09 (post-fix verify + new gap hunt)

**Verdict trước Round 2:** Quality 9.5/10, 130 TC.

**Verdict codex Round 2:** NEEDS_R3 — 11/13 Round 1 fixes VERIFIED_OK, 2 NEEDS_FURTHER_FIX (minor wording), 0 P0 mới, 4 P1 mới (field constraint boundary chưa cover).

**Findings applied:**

### Round 1 fixes verified: 11/13 OK + 2 cần sửa thêm:
| TC ID | R1 Status | R2 Verdict | Fix R2 |
|-------|-----------|------------|--------|
| TC-TVCS-040, TC-TVCS-TK-020, TC-API-IN-013, TC-PERM-003, TC-API-IN-009, TC-API-IN-011, TC-TVCS-023, TC-TVCS-026, TC-TVCS-TK-014, Overview NHT, TC-HSPL-020 | OK | VERIFIED_OK | — |
| TC-API-IN-014 | OK | NEEDS_FURTHER_FIX | Wording placeholder `{ten}` → `{ten_file}` (line 765-766 nguyên văn) |
| TC-API-IN-015 | OK | NEEDS_FURTHER_FIX | Steps `C1-C7` → `C1-C8` để execute ERR-DG-API-07 rate limit |

### P1 GAP mới (4 TC thêm vào file 01):
| ID | UC | TC mới | SRS line |
|----|----|--------|----------|
| New-1 | UC147 | TC-TVCS-041 boundary `tom_tat` 500 + `ghi_chu` 2000 | line 109, 112 |
| New-2 | UC147 | TC-TVCS-042 validate `anh_dai_dien` jpg/png/gif × 5MB | line 115, 1129, 1300 |
| New-3 | UC147 cross-FR-14 | TC-TVCS-043 link `hop_dong_tv_id` → FR-14 navigation | line 1297, 1305 (GAP-X.1-06) |
| New-4 | UC147 / BR-DATA-04 | TC-TVCS-044 SEQ uniqueness 5 TVCS cùng ngày | line 1553, 136, 1284 |

**Coverage sau Round 2:**
- Round 1+2 combined: 9 TC mới + 5 fixes
- TC count: 130 → 134
- Field constraint coverage: thiếu (chỉ field length cốt lõi) → đầy đủ tom_tat/ghi_chu/anh_dai_dien
- Cross-FR coverage: thiếu hop_dong_tv_id → cover
- BR-DATA-04 verify: chỉ format → thêm SEQ uniqueness
- Quality estimate: 9.5/10 → 9.7/10

**Closes Round 2:** Verdict NEEDS_R3 → expected PASS sau apply 6 fixes (2 wording + 4 P1 TC mới).

**Phase B status:** Vẫn 🚫 chờ BUG-TVCS-004 close + W2.2 done. Round 1+2 chỉ cải thiện chất lượng A, không unblock B.
