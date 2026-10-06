# Kế Hoạch Kiểm Thử — Quản lý Hỏi đáp, Vướng mắc Pháp luật (FR-II, SCR-II-01..03)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-10
> **Nguồn dữ liệu**: SRS v3.5 ([srs-fr-02-hoi-dap-v3.1.md](../../../input/srs-v3/srs-fr-02-hoi-dap-v3.1.md), kèm [srs-v3.md](../../../input/srs-v3/srs-v3.md) Phụ lục B/C cho BR + SM master)
> **SRS Reference**: Nhóm II (FR-II-01..10 + FR-II-NEW-02 + FR-II-CROSS-01), SCR-II-01/02/03, Entity HOI_DAP + PHAN_HOI + MAU_PHAN_HOI + AUDIT_LOG
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho module Quản lý Hỏi đáp. **FR-II-NEW-01 ĐÃ BỎ** (BA chốt 2026-05-07 Q11 — entity CAU_HINH_PHAN_CONG gỡ, FR-II-06 dùng auto-filter 4 tiêu chí). **FR-II-NEW-02 (Mẫu phản hồi) chuyển sang QTHT MH-10.7** — không thuộc scope W3.1, chỉ ref khi soạn phản hồi (FR-II-07). **FR-II-CROSS-01 (SLA scheduled job)** không có UI riêng — verify gián tiếp qua deadline calculation FR-II-03/04.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **10 FR (UC10–UC19)** trên 3 màn hình chính.
- **Entity owned**: `HOI_DAP`, `PHAN_HOI`, `MAU_PHAN_HOI` (referenced — quản lý ở FR-10 QTHT MH-10.7).
- **Entity referenced**: `TAI_KHOAN`, `DON_VI`, `DANH_MUC` (Lĩnh vực PL UC99), `CAU_HINH_SLA`, `DOANH_NGHIEP`, `FILE_DINH_KEM`, `TO_CHUC_TU_VAN`, `TU_VAN_VIEN`, `NGUOI_HO_TRO`, `TU_VAN_NHANH` (TVN_BRIDGE).
- **Màn hình**: SCR-II-01 (Danh sách 7 tabs + Form thêm/sửa drawer), SCR-II-02 (Chi tiết & Soạn phản hồi + 9 nút action-bar), SCR-II-03 (Phân công modal — auto-filter).
- **State Machine SM-HOIDAP**: 9 states + 12 transitions (gồm HUY + DA_TRA_LOI thoáng qua + CONG_KHAI ⟷ DA_DUYET).
- **Đặc thù**:
  - Auto-transition `DA_TRA_LOI → CHO_PHE_DUYET` (BR-FLOW-01).
  - 2 mức SLA `THUONG`/`PHUC_TAP` (15/30 ngày LV — NĐ55/2019 Đ.8 K.1).
  - API outbound Cổng PLQG có lock TTL 30s + idempotency (F-42, EC-04).
  - Phân công 2 nhánh: Cá nhân tự do hoặc Tổ chức tư vấn (NĐ77/2008 + NĐ55/2019 Đ.9).
  - Đóng hồ sơ THỦ CÔNG, không auto-close (BR-FLOW-06).
  - XSS sanitize 3-layer (client DOMPurify + server save + server pre-API).

### 1.2 Danh sách FR / UC / TC file

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-II-01 | UC10 | Quản lý hỏi đáp (CRUD + Excel + Refresh + soft delete + batch xóa) | HOI_DAP, FILE_DINH_KEM | `01-TC-quan-ly-hoi-dap.md` |
| 2 | FR-II-02 + FR-II-05 + FR-II-10 | UC11+UC14+UC19 | Tìm kiếm tổng hợp / đang xử lý / đã xử lý | HOI_DAP | `02-TC-tim-kiem-tong-hop.md` |
| 3 | FR-II-03 | UC12 | Tiếp nhận xử lý (MOI → TIEP_NHAN, tính SLA 15/30 ngày LV) | HOI_DAP | `03-TC-tiep-nhan-xu-ly.md` |
| 4 | FR-II-04 | UC13 | Quản lý thông tin tiếp nhận (cập nhật thời hạn + đổi muc_do_phuc_tap + xem lịch sử) | HOI_DAP, AUDIT_LOG | `04-TC-quan-ly-tiep-nhan.md` |
| 5 | FR-II-06 | UC15 | Phân công xử lý (Cá nhân tự do / Tổ chức tư vấn — auto-filter 4 tiêu chí) | HOI_DAP, TAI_KHOAN, TO_CHUC_TU_VAN, TU_VAN_VIEN, NGUOI_HO_TRO | `05-TC-phan-cong-xu-ly.md` |
| 6 | FR-II-07 | UC16 | Phản hồi câu hỏi (Lưu nháp + Auto-save 60s + tích "Đã trả lời" auto-transition + chèn mẫu) | PHAN_HOI, FILE_DINH_KEM, MAU_PHAN_HOI | `06-TC-phan-hoi-cau-hoi.md` |
| 7 | FR-II-08 + FR-II-09 | UC17+UC18 | Phê duyệt / Từ chối / Công khai / Hủy CK / Đóng hồ sơ + Batch + Quản lý đã xử lý | HOI_DAP, PHAN_HOI | `07-TC-phe-duyet-cong-khai.md` |
| ~~8~~ | ~~FR-II-NEW-01~~ | — | ~~Cấu hình lĩnh vực ↔ phân công~~ | — | **ĐÃ BỎ** BA chốt 2026-05-07 Q11 |
| 9 | FR-II-NEW-02 | — | Mẫu phản hồi (Mô hình B Hybrid 2 tầng) | MAU_PHAN_HOI | **Chuyển sang FR-10 QTHT MH-10.7** — chỉ ref dropdown chèn mẫu trong file `06-TC-phan-hoi-cau-hoi.md` |
| 10 | FR-II-CROSS-01 | — | SLA scheduled job (4 mức cảnh báo + email/in-app) | HOI_DAP, CAU_HINH_SLA | **Không có UI riêng** — verify gián tiếp deadline calculation trong file `03-TC-tiep-nhan-xu-ly.md` + `04-TC-quan-ly-tiep-nhan.md` |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | qtht_01 | Read-only verify (toàn HT). Không CRUD HOI_DAP |
| CB_NV_TW | TW | cb_nv_tw_01 | CRUD primary (scope TW = toàn quốc). `_02` fallback, `_03` permission test |
| CB_NV_BN | BN | cb_nv_bn_01 (Bộ KH&ĐT) | CRUD scoped BN. Pattern test BR-AUTH-08 |
| CB_NV_DP | DP | cb_nv_dp_01 (Sở TP AG) | CRUD scoped ĐP. `_02` Sở TP BG cross-tenant |
| CB_PD_TW | TW | cb_pd_tw_01 | Phê duyệt / Công khai / Hủy CK scope TW (BR-AUTH-05 cùng cấp) |
| CB_PD_BN | BN | cb_pd_bn_01 | Phê duyệt scope BN |
| CB_PD_DP | DP | cb_pd_dp_01 | Phê duyệt scope ĐP |
| TVV | — | tvv_01..06 | Phân công TC TV (FR-II-06) — assigned worker. NHT/CG fallback |
| NHT | — | nht_01..04 | Phân công cá nhân (FR-II-06) — verify NHT.linh_vuc_ids[] N:N filter |
| CG | — | cg_01..06 | Phân công cá nhân (FR-II-06) — verify TVV.linh_vuc_chuyen_mon |
| DN/GV | — | dn_01, gv_01 | Negative — verify 403 chặn module HOI_DAP |

> **Source TK**: `c:/HoaAG/LuatDN5/Ver3.1/input/users.csv`. Password Secret@123 toàn bộ.

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR formal §6 + working labels)

> **Footnote convention**:
> - **BR formal §6 srs-fr-02**: BR khai báo trong SRS FR-II §6 (lines 1568-1670). 17 BR sử dụng (10 owned + 7 inherited).
> - **BR working labels (srs-v3.md inline)**: BR codes ref nhưng source ở master `srs-v3.md` Phụ lục B (BR-EC-19, BR-EC-20...).
> - **Inline rule labels**: Working labels gán cho rule trong prose SRS srs-fr-02 (vd. F-42 lock TTL 30s, F-38 XSS policy, F-19 delete state). KHÔNG phải BR formal — dùng cho traceability nội bộ.

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực bắt buộc Tier 1 (username/pwd + TOTP 2FA) | srs-fr-02:1597 | ✅ | Precondition login mọi UC |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB PD cấp = đơn vị tạo) | srs-fr-02:1603 | ✅ | TC phê duyệt + công khai (file 07) |
| BR-AUTH-08 | Phân quyền dữ liệu theo đơn vị (`don_vi_id`) | srs-fr-02:1572 | ✅ | TC scope đơn vị mọi list/detail |
| BR-DATA-01 | Soft delete (is_deleted=1, không xóa vật lý) | srs-fr-02:1609 | ✅ | TC DELETE (file 01) |
| BR-DATA-03 | Common fields (created_at/by, updated_at/by, is_deleted) | srs-v3.md Phụ lục B | ✅ | Verify schema |
| BR-DATA-04 | Auto-gen mã `HD-YYYYMMDD-SEQ` | srs-fr-02:1615 | ✅ | TC tạo mới + uniqueness |
| BR-DATA-05 | Audit trail (immutable, INSERT-only) | srs-fr-02:1621 | ✅ | TC CUD + state transition mọi file |
| BR-DATA-06 | Export Excel max 10,000 rows | srs-fr-02:1577 + srs-v3.md | ✅ | TC Export (file 01) |
| BR-DATA-07 | Pagination default 20, options 10/20/50/100 | srs-fr-02:1578 | ✅ | TC pagination (file 01, 02, 04, 07) |
| BR-DATA-08 | Full-text search (tsvector trên noi_dung) | srs-fr-02:1579 | ✅ | TC search keyword (file 02) |
| BR-FLOW-01 | Auto-transition Đã trả lời → Chờ PD | srs-fr-02:1627 | ✅ (core) | TC tích "Đã trả lời" (file 06) |
| BR-FLOW-02 | Phê duyệt hàng loạt (batch approve) | srs-fr-02:1633 | ✅ | TC batch (file 07) |
| BR-FLOW-03 | Không sửa/xóa sau DA_DUYET/CONG_KHAI/HOAN_THANH | srs-fr-02:1639 | ✅ | TC negative state cấm (file 01) |
| BR-FLOW-04 | Từ chối yêu cầu lý do (≥10 ký tự) | srs-fr-02:1645 | ✅ | TC reject (file 07) |
| BR-FLOW-05 | Công khai qua API trực tiếp Cổng PLQG (không LGSP) | srs-fr-02:1651 | ✅ (core) | TC công khai + hủy CK (file 07) |
| BR-FLOW-06 | Đóng hồ sơ THỦ CÔNG, không auto-close | srs-fr-02:1657 | ✅ (BA 2026-05-05) | TC nút "Đóng hồ sơ" (file 07) |
| BR-CALC-03 | Deadline 2 mức 15/30 ngày LV theo `muc_do_phuc_tap` | srs-fr-02:1663 | ✅ (core) | TC tiếp nhận + cập nhật thời hạn (file 03, 04) |
| BR-CALC-04 | Đổi `muc_do_phuc_tap` sau tiếp nhận → tính lại deadline | srs-fr-02:1664 | ✅ | TC nút "Đổi mức độ phức tạp" (file 04) |
| BR-SLA-01 | SLA mặc định | srs-fr-02:1588 + master | ✅ | TC tiếp nhận tính SLA (file 03) |
| BR-SLA-02 | 4 mức cảnh báo SLA (BINH_THUONG/SAP_HET_HAN/QUA_HAN/QUA_HAN_NGHIEM_TRONG) | srs-fr-02:1670 | ✅ | TC badge cảnh báo cột 26 SCR-II-01 (file 01, 04) |
| BR-SLA-03 | Thông báo cảnh báo SLA (in-app + email) | srs-fr-02:1676 | ✅ | TC notification trigger (file 04) |
| BR-SLA-04 | Ngày làm việc (Thứ 2-6, trừ ngày lễ) | srs-fr-02:1591 + master | ✅ | TC boundary cuối tuần/lễ (file 03) |
| BR-EC-19 | Batch tối đa 100 records | srs-v3.md + srs-fr-02:1612/742 | ✅ | TC batch >100 (file 07) |
| BR-EC-20 | Công khai chỉ set CONG_KHAI sau API thành công | srs-v3.md + srs-fr-02:1101/1168 | ✅ | TC API outbound (file 07) |

### 2.2 Error Codes

**FR-II-01 (HOI_DAP CRUD):** ERR-HD-01 (nội dung trống), ERR-HD-02 (>5000 ký), ERR-HD-03 (lĩnh vực invalid), ERR-HD-04 (sửa/xóa state cấm), WRN-HD-01 (export >10K), ERR-DELETE-STATE (batch xóa state cấm), ERR-AUTH-DEL (batch xóa khác đơn vị), ERR-BATCH-CONFLICT (optimistic lock conflict).

**FR-II-02/05/10 (Tìm kiếm):** ERR-HD-TK-01 (tu_ngay > den_ngay), ERR-HD-TK-02 (đã xử lý — date range), ERR-AUTH-TK-01 (scope đơn vị), INF-HD-TK-01/02/03 (no results).

**FR-II-03 (Tiếp nhận):** ERR-TN-01 (state ≠ MOI), ERR-TN-02 (record không tồn tại / soft-deleted), ERR-TN-03 (concurrent — version mismatch).

**FR-II-04 (Cập nhật thời hạn):** ERR-TH-01 (thời hạn <= hôm nay), ERR-TH-02 (lý do <10 hoặc >500 ký), ERR-TH-03 (state ngoài TIEP_NHAN/DANG_XU_LY), ERR-TH-CONFLICT (HTTP 409 version mismatch), ERR-DXL-01 (date range), ERR-AUTH-DXL-01 (scope), INF-DXL-01 (no results).

**FR-II-06 (Phân công):** ERR-PC-01 (cá nhân vô hiệu), ERR-PC-02 (state cấm phân công), ERR-PC-03 (TC TV vô hiệu), ERR-PC-04 (TO_CHUC thiếu 2 thông tin), ERR-PC-05 (TVV không thuộc TC), ERR-PC-06 (CA_NHAN truyền TC TV thừa), WRN-PC-01 (workload quá tải).

**FR-II-07 (Phản hồi):** ERR-PH-01 (nội dung trống), ERR-PH-02 (state cấm phản hồi), WRN-PH-01 (không phải người được phân công).

**FR-II-08 (Phê duyệt + Công khai):** ERR-PD-01 (CB PD khác cấp), ERR-PD-02 (từ chối thiếu lý do), ERR-PD-03 (state ≠ CHO_PHE_DUYET), ERR-PD-04 (API Cổng PLQG fail công khai), ERR-PD-05 (batch >100), ERR-PD-06 (API fail hủy CK), ERR-PD-07 (lock conflict outbound), WRN-PD-01 (batch partial fail).

**FR-II-09 (Đã xử lý):** INF-DAXL-01 (no results), ERR-AUTH-DAXL-01 (scope), ERR-DAXL-01 (record không tồn tại).

### 2.3 Permission Matrix

| Action / Role | QTHT | CB_NV_{TW/BN/DP} | CB_PD_{TW/BN/DP} | NHT/TVV/CG (assigned) | DN/GV |
|---------------|------|-------------------|-------------------|----------------------|-------|
| Xem danh sách HOI_DAP (scope đơn vị) | 👁️ R toàn HT | ✅ scope `don_vi_id` | ✅ scope cùng cấp | ✅ chỉ assigned (HOI_DAP_READ_ASSIGNED) | ❌ |
| Tạo mới HOI_DAP (UC10) | ❌ | ✅ cùng đơn vị | ❌ | ❌ | ❌ |
| Sửa/Xóa HOI_DAP (state hợp lệ) | ❌ (force-edit audit đặc biệt) | ✅ cùng đơn vị | ❌ | ❌ | ❌ |
| Tiếp nhận (UC12 — MOI → TIEP_NHAN) | ❌ | ✅ cùng đơn vị | ❌ | ❌ | ❌ |
| Phân công (UC15) | ❌ | ✅ cùng đơn vị (HOI_DAP_ASSIGN) | ❌ | ❌ | ❌ |
| Soạn phản hồi (UC16) | ❌ | ✅ cùng đơn vị HOẶC được phân công | ❌ | ✅ chỉ khi nguoi_phan_cong_id = user.id | ❌ |
| Phê duyệt / Từ chối (UC17) | ❌ | ❌ | ✅ cùng cấp (BR-AUTH-05) | ❌ | ❌ |
| Công khai / Hủy công khai (UC17) | ❌ | ❌ | ✅ cùng cấp + đơn vị (BR-AUTH-05 + F-20) | ❌ | ❌ |
| Đóng hồ sơ (UC17 — DA_DUYET/CONG_KHAI → HOAN_THANH) | ❌ | ✅ cùng đơn vị | ✅ cùng cấp | ❌ | ❌ |
| Hủy yêu cầu (MOI → HUY) | ❌ | ✅ cùng đơn vị, chưa có PHAN_HOI | ❌ | ❌ | ❌ |
| Cập nhật thời hạn / Đổi mức độ (UC13) | ❌ | ✅ cùng đơn vị, state TIEP_NHAN/DANG_XU_LY | ❌ | ❌ | ❌ |
| Xuất Excel (UC10) | ❌ | ✅ scope filter | ✅ scope filter | ❌ | ❌ |

> **Cross-tenant test pattern**: cb_nv_dp_01 (Sở TP AG) tạo HOI_DAP X → cb_nv_dp_02 (Sở TP BG) attempt access → 404 IDOR block (BR-AUTH-08).
> **Cross-cấp test pattern**: HOI_DAP cấp ĐP → cb_pd_tw_01 phê duyệt → ERR-PD-01 (BR-AUTH-05).

### 2.4 State Machine — SM-HOIDAP

```
[*] → MOI → TIEP_NHAN → DANG_XU_LY → DA_TRA_LOI (thoáng qua) → CHO_PHE_DUYET → DA_DUYET → CONG_KHAI ⟷ DA_DUYET
                                                                                  └→ HOAN_THANH (thủ công) ←┘
       └→ HUY                CHO_PHE_DUYET → DANG_XU_LY (từ chối, BR-FLOW-04)
```

**12 transitions** (xem chi tiết srs-fr-02:1539-1552):
1. `[*] → MOI` (DN gửi qua Cổng / CB nhập / TVN escalate)
2. `MOI → TIEP_NHAN` (CB NV nhấn Tiếp nhận)
3. `MOI → HUY` (CB NV cùng đơn vị, chưa có PHAN_HOI)
4. `TIEP_NHAN → DANG_XU_LY` (Phân công)
5. `DANG_XU_LY → DA_TRA_LOI` (CB NV/NHT tích "Đã trả lời" + Gửi)
6. `DA_TRA_LOI → CHO_PHE_DUYET` **AUTO** (BR-FLOW-01)
7. `CHO_PHE_DUYET → DA_DUYET` (CB PD phê duyệt)
8. `CHO_PHE_DUYET → DANG_XU_LY` (CB PD từ chối, BR-FLOW-04)
9. `DA_DUYET → CONG_KHAI` (CB PD cùng cấp + API Cổng OK + lock TTL 30s)
10. `CONG_KHAI → DA_DUYET` (CB PD cùng cấp + API gỡ OK + lock TTL 30s)
11. `DA_DUYET → HOAN_THANH` (CB NV cùng đơn vị HOẶC CB PD cùng cấp click Đóng hồ sơ — BR-FLOW-06)
12. `CONG_KHAI → HOAN_THANH` (như #11)

**Optimistic locking** áp dụng mọi transition. **Crash recovery** scheduled job 5 phút retry trans middle.

### 2.5 Kênh tiếp nhận (5 enum)

| Mã DB | Nhãn hiển thị | Source |
|-------|---------------|--------|
| `DVC` | Dịch vụ công | API DVC inbound |
| `CONG_PLQG` | Cổng Pháp luật Quốc gia | API Cổng inbound |
| `TRUC_TIEP` | Trực tiếp | CB nhập tay tại quầy |
| `HE_THONG_KHAC` | Hệ thống khác | API hệ thống bên thứ 3 |
| `TVN_BRIDGE` | Từ Tư vấn nhanh | **Auto-set** khi escalate từ FR-13, kèm `tu_van_nhanh_goc_id` |

### 2.6 muc_do_phuc_tap (2 enum) + SLA

| Mã DB | Nhãn | SLA (ngày LV) | Căn cứ |
|-------|------|----------------|--------|
| `THUONG` | Thường | 15 | NĐ55/2019 Đ.8 K.1 |
| `PHUC_TAP` | Phức tạp | 30 | NĐ55/2019 Đ.8 K.1 |

> Đổi mức độ trong `{TIEP_NHAN, DANG_XU_LY}` → tính lại deadline (BR-CALC-04). Đổi outside scope → button disabled.

### 2.7 loai_doi_tuong_xu_ly (Phân công 2 nhánh)

| Mã DB | Nhãn | Validation cờ |
|-------|------|----------------|
| `CA_NHAN` | Cá nhân tự do | `nguoi_phan_cong_id` REQUIRED, `to_chuc_tu_van_id` PHẢI NULL |
| `TO_CHUC` | Tổ chức tư vấn | `to_chuc_tu_van_id` + `nguoi_phan_cong_id` REQUIRED, TVV phải thuộc TC (`TU_VAN_VIEN.to_chuc_chinh_id = to_chuc_tu_van_id`) |

> Auto-filter 4 tiêu chí (BA chốt 2026-05-07 Q11): lĩnh vực + đơn vị + workload ASC + FIFO (ho_ten ASC), LIMIT 10.

---

## 3. Cấu Trúc File Test Case

```
hoi-dap/
├── 00-test-plan-overview.md            ← THIS FILE
├── 01-TC-quan-ly-hoi-dap.md            ← FR-II-01 UC10 CRUD + Excel + Refresh + batch xóa
├── 02-TC-tim-kiem-tong-hop.md          ← FR-II-02 + FR-II-05 + FR-II-10 (3 search variants)
├── 03-TC-tiep-nhan-xu-ly.md            ← FR-II-03 UC12 (MOI → TIEP_NHAN, SLA 15/30)
├── 04-TC-quan-ly-tiep-nhan.md          ← FR-II-04 UC13 (cập nhật thời hạn + đổi muc_do + lịch sử)
├── 05-TC-phan-cong-xu-ly.md            ← FR-II-06 UC15 (CA_NHAN/TO_CHUC + auto-filter 4 tiêu chí)
├── 06-TC-phan-hoi-cau-hoi.md           ← FR-II-07 UC16 (soạn + lưu nháp + auto-save 60s + tích "Đã trả lời")
├── 07-TC-phe-duyet-cong-khai.md        ← FR-II-08 + FR-II-09 (phê duyệt/từ chối/công khai/hủy CK/đóng HS + batch)
├── 08-REVIEW-edge-case-hunter.md       ← A4 audit log (proposal + merge mapping)
├── 09-traceability-matrix.md           ← A5 BR/AC ↔ TC matrix
├── 10-REVIEW-test-quality.md           ← A6 6-axis quality score
└── 11-a7-filter-log.md                 ← A7 filter log (loại/sửa TC chỉ-DB/API thuần)
```

### 3.1 Convention TC ID

- Prefix theo file: `TC-HD-XXX` (file 01) · `TC-HDTK-XXX` (file 02) · `TC-TN-XXX` (file 03) · `TC-DXL-XXX` (file 04) · `TC-PC-XXX` (file 05) · `TC-PH-XXX` (file 06) · `TC-PD-XXX` (file 07).
- Range: 001-099 Happy · 100-199 Negative · 200-299 Edge · 300+ Codex review additions.
- TraceID format: `FR-II-XX / {section}` hoặc `FR-II-XX / E{N}` cho error codes.

---

## 4. Đặc Thù Cần Lưu Ý Khi Viết TC

### 4.1 SCR-II-01 đa tab

7 tabs: Tất cả · Mới · Đang xử lý · Chờ phê duyệt · Đã duyệt · Công khai · Hoàn thành. Mỗi tab có filter cứng `trang_thai`. Action-bar đổi theo tab (Xóa hàng loạt cho Tab Mới/Đang xử lý/Tất cả · Phê duyệt hàng loạt cho Chờ PD · Công khai hàng loạt cho Đã duyệt). Tab "Chờ phê duyệt" mặc định active cho CB PD (gộp MH-02.4 v2.1).

### 4.2 SCR-II-02 action-bar 9 nút

Nút hiển thị/ẩn theo `trang_thai` + role + đơn vị (BR-AUTH-05/08 expression). Mỗi state có set nút khác nhau:
- `MOI`: Tiếp nhận, Hủy yêu cầu (chưa có PHAN_HOI)
- `TIEP_NHAN/DANG_XU_LY`: Phân công, Cập nhật thời hạn, Đổi mức độ phức tạp, Soạn phản hồi
- `CHO_PHE_DUYET`: Phê duyệt, Từ chối (CB PD only)
- `DA_DUYET`: Công khai, Đóng hồ sơ
- `CONG_KHAI`: Hủy công khai, Đóng hồ sơ
- `HOAN_THANH/HUY`: chỉ đọc

### 4.3 Test data seeding pattern

- **State coverage**: cần ≥1 record mỗi state (9 states × 3 cấp đơn vị = ~15-20 record seed).
- **Cross-tenant**: cần ≥2 record cùng cấp khác đơn vị (verify BR-AUTH-08).
- **Cross-cấp**: cần ≥1 record TW + 1 BN + 1 ĐP (verify BR-AUTH-05).
- **muc_do_phuc_tap mix**: 50% THUONG + 50% PHUC_TAP để verify SLA 15/30 ngày LV.
- **TVN_BRIDGE**: cần ≥1 record `kenh_tiep_nhan='TVN_BRIDGE'` + `tu_van_nhanh_goc_id NOT NULL` (verify FR-13 cross-ref).
- **Phân công TO_CHUC**: cần ≥1 TC TV HOAT_DONG + ≥2 TVV thuộc TC đó (verify auto-filter cấp 2).

### 4.4 SLA 4 mức cảnh báo

Test cần seed deadline strategic để cover 4 mức:
- BINH_THUONG: deadline > 50% còn lại
- SAP_HET_HAN: deadline ≤ 50% còn lại
- QUA_HAN: đã quá hạn ≤ 200%
- QUA_HAN_NGHIEM_TRONG: > 200%

### 4.5 API outbound Cổng PLQG (mock pattern)

Module `07-TC-phe-duyet-cong-khai.md`:
- API Cổng OK → set CONG_KHAI
- API Cổng fail → giữ DA_DUYET + ERR-PD-04
- Lock TTL 30s + flag `api_in_progress` → ERR-PD-07 nếu user khác concurrent
- Idempotency key chống duplicate khi retry

### 4.6 XSS sanitize 3-layer

Áp dụng cho `noi_dung` (rich-text), `mo_ta_cong_khai`. Whitelist: `<p>, <br>, <b>, <strong>, <i>, <em>, <u>, <ul>, <ol>, <li>, <a>, <h3>, <h4>, <blockquote>, <code>`. Reject `<script>, <iframe>, event handlers, javascript:`.

### 4.7 Optimistic locking + concurrency

Mọi UPDATE dùng `version` field. Conflict → HTTP 409 + toast "Tải lại / Ghi đè". Test edge `concurrent edit 2 tab` cho:
- Tiếp nhận (ERR-TN-03)
- Cập nhật thời hạn (ERR-TH-CONFLICT)
- Phê duyệt batch (ERR-BATCH-CONFLICT)
- Lưu nháp PHAN_HOI

---

## 5. Out-of-Scope (cần xác nhận BA / chuyển module khác)

| Item | Lý do |
|------|-------|
| FR-II-NEW-01 (Cấu hình lĩnh vực ↔ phân công) | **ĐÃ BỎ** BA chốt 2026-05-07 Q11 |
| FR-II-NEW-02 (Mẫu phản hồi MAU_PHAN_HOI CRUD) | Chuyển sang FR-10 QTHT MH-10.7 — tested ở Phase B QTHT W1.2/W1.3 |
| FR-II-CROSS-01 SLA scheduled job (logic 30 phút auto-scan) | Backend cron job — không có UI riêng. Test gián tiếp qua badge cảnh báo cột SCR-II-01 row 26 |
| API outbound Cổng PLQG (request/response thực tế) | Black-box — chỉ verify trạng thái local sau API call. Mock backend response cho test isolation |
| Email notification (BR-SLA-03) | Black-box — verify in-app notification trên UI; email send-and-forget (verify qua MailHog nếu env có) |
| Crash recovery scheduled job | Khó test trong UI (hệ thống tự retry mỗi 5 phút). Chỉ verify gián tiếp khi state stuck > 5 phút |

---

*Generated 2026-05-10 — Phase A step A2 (00-test-plan-overview)*
