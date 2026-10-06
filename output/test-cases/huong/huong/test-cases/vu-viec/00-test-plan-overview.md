# Kế Hoạch Kiểm Thử — Vụ việc Trợ giúp Pháp lý (FR-V.I, SCR-V.I-01..05)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-06
> **Nguồn dữ liệu**: SRS v3.5 ([srs-fr-05-vu-viec-v3.1.md](../../../input/srs-v3/srs-fr-05-vu-viec-v3.1.md), kèm [srs-v3.md](../../../input/srs-v3/srs-v3.md) cho BR Phụ lục B)
> **SRS Reference**: Nhóm V.I (FR-V.I-01..17 + 4 NEW/CROSS), SCR-V.I-01/02/03/04/05
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho module Vụ việc TGPL — module phức tạp nhất (15 bước SM-VUVIEC, 12 trạng thái workflow + cờ overlay cong_khai). FR-V.I-03 (UC53 LGSP API thuần inbound) **LOẠI** per A7. FR-V.I-CROSS-01 phần scheduled job auto **LOẠI** per A7 (giữ phần cấu hình QTHT có UI). FR-V.I-05 nhánh **API Inbound** LOẠI A7, nhánh **CMS** GIỮ.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **21 FR (UC51–UC67 + 4 NEW/CROSS)** trên 5 màn hình. **Sau A7 filter:** 19 FR active (loại FR-V.I-03 LGSP, gộp CROSS-01 scheduled vào QTHT cấu hình UI).
- **Entity owned (6):** VU_VIEC, HO_SO_VU_VIEC, KET_QUA_VU_VIEC, PHAN_CONG_VU_VIEC, DANH_GIA_VU_VIEC, LICH_SU_VU_VIEC
- **Entity referenced (11):** DOANH_NGHIEP, TU_VAN_VIEN, TO_CHUC_TU_VAN, NGUOI_HO_TRO, TAI_KHOAN, DON_VI, DANH_MUC, FILE_DINH_KEM, CAU_HINH_SLA, CAU_HINH_QUY_TRINH, THONG_BAO
- **Màn hình (5):**
  - SCR-V.I-01: Danh sách HS VV CMS (6 tab + 21 cột + batch action)
  - SCR-V.I-02: Form Thêm/Nhập thủ công (4 Accordion)
  - SCR-V.I-03: Chi tiết VV (Stepper 10 bước + 8 Accordion + Timeline + Action bar context-sensitive, 2 chế độ CMS/DN)
  - SCR-V.I-04: DS Vụ việc của tôi (DN — mobile-first)
  - SCR-V.I-05: DS Thông báo của tôi (DN)
- **State Machine:** SM-VUVIEC 12 trạng thái (MOI_TAO → CHO_TIEP_NHAN → DA_TIEP_NHAN → DANG_KIEM_TRA ⟷ YEU_CAU_BO_SUNG → DA_PHAN_CONG ⟷ DA_TIEP_NHAN → DANG_XU_LY → CHO_PHE_DUYET ⟷ DANG_XU_LY → DA_DUYET → HOAN_THANH → DA_DANH_GIA; nhánh phụ TU_CHOI). **CONG_KHAI là cờ overlay**, KHÔNG phải trạng thái workflow.
- **Đặc thù module:**
  - SLA 15 ngày làm việc (NĐ55/2019 Đ.8 K.1) — BR-SLA-01
  - BR-CALC-04 ưu tiên phân công NĐ55 Đ.4 (DN nữ làm chủ +3, LĐ nữ +2, LĐ KT +2, FIFO +1)
  - BR-EC-15 YCBS tối đa 3 lần (counter, lần 4 KHONG_DAT → auto TU_CHOI)
  - BR-EC-16 quá hạn bổ sung 5 ngày LV (cấu hình SLA) → auto TU_CHOI
  - BR-EC-20 KHÔNG flip cong_khai trước khi API Cổng PLQG OK (atomic)
  - BR-PUBLIC-04 whitelist 9 fields công khai (NĐ13/2023 BVDLCN)
  - 2 thẻ phân công (Cá nhân TVV/CG/NHT vs Tổ chức tư vấn — TVV thuộc TC)
  - 2 chế độ SCR-V.I-03 (CMS đầy đủ vs DN xem + bổ sung + đánh giá)

### 1.2 Danh sách FR / UC → TC file mapping

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-V.I-01 + FR-V.I-08 | UC51 + UC58 | Quản lý DS hồ sơ VV + Tìm kiếm (SCR-01) | VU_VIEC | `01-TC-quan-ly-vu-viec-DS.md` |
| 2 | FR-V.I-02 | UC52 | DN gửi HS HTPL qua chuyên trang (SCR-02 chế độ DN, auth Tier 2 VNeID) | VU_VIEC, DOANH_NGHIEP | `02-TC-tao-vu-viec-DN.md` |
| 3 | FR-V.I-04 | UC54 | CB NV nhập HS thủ công (SCR-02) — modal lookup/tạo DN | VU_VIEC, HO_SO_VU_VIEC | `03-TC-nhap-thu-cong-vv.md` |
| 4 | FR-V.I-05 (CMS) | UC55 | Tiếp nhận từ HT khác — CMS DS/search/delete (API Inbound LOẠI A7) | VU_VIEC | `04-TC-tiep-nhan-cms-ht-khac.md` |
| 5 | FR-V.I-06 | UC56 | Kiểm tra HS — checklist 6 hạng mục Mẫu 01 NĐ55 (Accordion 4) | VU_VIEC, LICH_SU_VU_VIEC | `05-TC-kiem-tra-hs.md` |
| 6 | FR-V.I-07 | UC57 | Quản lý HS VV (SCR-03 Accordion 1-3, edit, upload tài liệu bổ sung) | VU_VIEC, HO_SO_VU_VIEC | `06-TC-quan-ly-hs-vv.md` |
| 7 | FR-V.I-09 + FR-V.I-10 | UC59 + UC60 | Phân công xử lý (Cá nhân/Tổ chức) + NHT/TVV xác nhận tham gia | PHAN_CONG_VU_VIEC, VU_VIEC | `07-TC-phan-cong-xac-nhan.md` |
| 8 | FR-V.I-11 + FR-V.I-12 + FR-V.I-13 | UC61 + UC62 + UC63 | Trình PD + Thông báo KQ + CB PD phê duyệt/từ chối (single + batch) | VU_VIEC, THONG_BAO | `08-TC-trinh-phe-duyet-pd.md` |
| 9 | FR-V.I-15 + FR-V.I-16 | UC65 + UC66 | NHT cập nhật KQ + CB NV cập nhật KQ cuối → HOAN_THANH | KET_QUA_VU_VIEC, VU_VIEC | `09-TC-cap-nhat-ket-qua.md` |
| 10 | FR-V.I-17 | UC67 | Đánh giá VV (CB_NV/DN, 3 tiêu chí thang 0–10, duplicate guard) | DANH_GIA_VU_VIEC | `10-TC-danh-gia-vv.md` |
| 11 | FR-V.I-NEW-05 | CR-01 + Q-NEW-02 | Công khai/Hủy công khai VV — whitelist BR-PUBLIC-04, retry API atomic | VU_VIEC | `11-TC-cong-khai-vv.md` |
| 12 | FR-V.I-NEW-02 + FR-V.I-14 | — + UC64 | DN bổ sung HS (SCR-03 chế độ DN) + DN nhận thông báo (SCR-V.I-04/05) | VU_VIEC, HO_SO_VU_VIEC, THONG_BAO | `12-TC-DN-bo-sung-thong-bao.md` |
| 13 | FR-V.I-NEW-01 | UC mới | Cấu hình quy trình hỗ trợ TVPLDN (QTHT versioning) | CAU_HINH_QUY_TRINH | `13-TC-cau-hinh-quy-trinh.md` |
| 14 | — | — | Permission matrix cross-FR-V.I (BR-AUTH-01/03/04/05/08, 2-tier auth) | All | `14-TC-permission-matrix.md` |
| ~~15~~ | ~~FR-V.I-03~~ | ~~UC53~~ | ~~Tiếp nhận HS qua DVC (LGSP API thuần inbound)~~ — **LOẠI A7** | — | — |
| ~~16~~ | ~~FR-V.I-CROSS-01~~ | — | ~~Scheduled job SLA 30 phút (background, no UI feedback)~~ — **LOẠI A7** (cấu hình SLA UI gộp QTHT UC108, ngoài scope) | — | — |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | `qtht_01` | NEW-01 cấu hình quy trình + read-only verify (toàn HT) |
| CB_NV_TW | TW | `cb_nv_tw_01` (primary), `cb_nv_tw_02/03` (multi-user concurrent) | UC51/54/56/57/59/61/62/66 — CRUD + transitions chính (scope TW = toàn quốc) |
| CB_NV_BN | BN | (cần seed thêm — chưa có user CB_NV_BN trong CSV) | TC permission scope BN |
| CB_NV_DP | DP | (gợi ý dùng `cb_nv_tw_01` workaround vì chưa có _dp account) | TC permission scope DP — **SPEC-CLARIFY-VV-PERM-01**: cần BA seed user CB_NV_DP |
| CB_PD_TW | TW | `cb_pd_tw_01` (primary), `cb_pd_tw_02/03` | UC63 phê duyệt + NEW-05 công khai/hủy |
| NHT | DP scope | `nht_01` (AG), `nht_02` (BG), `nht_03` (BNI) | UC60 xác nhận, UC65 cập nhật KQ. Verify scope per đơn vị |
| TVV | DP/TW | `tvv_01..03` (DP), `tvv_tw_01..06` (TW) | UC60 xác nhận khi `loai='CA_NHAN'` hoặc `loai='TO_CHUC'` |
| DN | — | `dn_01` (AG) | UC52 gửi HS, NEW-02 bổ sung, UC64 nhận TB, UC67 đánh giá. Verify scope DN |
| Negative | — | `nht_01` (cross-role), `dn_01`, `tvv_01` | Verify 403 chặn khi truy cập VV của đơn vị/DN khác |

> **Note seed gap:** CSV hiện thiếu `cb_nv_bn_01`, `cb_nv_dp_01`, `cb_pd_bn_01`, `cb_pd_dp_01` — Phase B B-Seed cần verify và seed thêm hoặc mark **SPEC-CLARIFY-VV-PERM-01** (BA xác nhận chiến lược test 3-tier scope).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực 2-tier (Tier 1 nội bộ + Tier 2 VNeID) | srs-fr-05:2377 | ✅ | Precondition login mọi UC, đặc biệt FR-V.I-02 (DN Tier 2) |
| BR-AUTH-03/04 | Phân quyền TW/BN/ĐP (kiến trúc 2-tier BR-AUTH-02) | srs-fr-05:2469 | ✅ | TC permission scope (file 14) |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB PD ↔ CB NV) | srs-fr-05:2385 | ✅ | UC61 trình + UC63 PD + NEW-05 công khai |
| BR-AUTH-08 | Phân quyền theo đơn vị (don_vi_id NOT NULL) | srs-fr-05:2391 | ✅ | TC scope filter mọi DS |
| BR-DATA-01 | Soft delete | srs-fr-05:2397 | ✅ | UC55 CMS xóa CHO_TIEP_NHAN |
| BR-DATA-02 | Multi-tenant scoping | srs-fr-05:2403 | ✅ | UC51 DS filter |
| BR-DATA-03 | 7 common fields | srs-fr-05:2409 | ✅ | Verify schema mọi entity |
| BR-DATA-04 | Auto-gen mã VV-{TINH}-YYYYMMDD-SEQ | srs-fr-05:2415 | ✅ | UC52, UC54, UC55 verify mã |
| BR-DATA-05 | Audit trail immutable (LICH_SU_VU_VIEC + AUDIT_LOG) | srs-fr-05:2421 | ✅ | Verify mọi thao tác CUD + transition |
| BR-DATA-07 | Pagination 20 default, max 100 | srs-fr-05:2427 | ✅ | TC pagination |
| BR-FLOW-03 | Không sửa/xóa sau PD | srs-fr-05:2433 | ✅ | UC57 verify VV ở DA_DUYET/HOAN_THANH cấm edit |
| BR-FLOW-04 | Lý do từ chối ≥ 10 ký tự (PD), ≥ 20 ký tự (hủy công khai) | srs-fr-05:2439 | ✅ | UC63 từ chối + NEW-05 hủy công khai |
| BR-CALC-04 | Ưu tiên phân công NĐ55 Đ.4 (+3/+2/+2/+1) | srs-fr-05:2445 | ✅ | UC59 verify gợi ý NHT/TVV |
| BR-CALC-06 | Cập nhật điểm TVV TB (cross sang FR-IV) | srs-fr-05:2481 | ⚠️ | UC67 — verify trigger nhưng KHÔNG verify giá trị (ngoài scope FR-V.I) |
| BR-EC-15 | YCBS tối đa 3 lần (counter bo_sung_count) | srs-fr-05:2487 | ✅ | UC56 verify counter + auto TU_CHOI lần 4 |
| BR-EC-16 | Quá hạn bổ sung 5 ngày LV → auto TU_CHOI | srs-fr-05:2493 | ⚠️ (scheduled job — verify gián tiếp qua thời gian) | NEW-02 verify ERR-VV-BS-03 + manual time-shift |
| BR-EC-20 | KHÔNG set cong_khai trước khi API Cổng PLQG OK | srs-fr-05:2505 | ✅ | NEW-05 atomic + retry persistent toast |
| BR-PUBLIC-01 | Điều kiện công khai (DA_DUYET/HOAN_THANH/DA_DANH_GIA) | srs-fr-05:2511 | ✅ | NEW-05 verify trạng thái + clear khi hủy |
| BR-PUBLIC-04 | Whitelist 9 fields công khai (NĐ13/2023 BVDLCN) | srs-fr-05:2517 | ✅ | NEW-05 verify network payload không chứa 6 field nhạy cảm |
| BR-NOTIF-01 | Thông báo workflow (in-app + email + CC tổ chức) | srs-fr-05:2499 | ✅ | UC59/60/63/65/66 verify TB sent |
| BR-SLA-01 | SLA 15 ngày LV (NĐ55/2019 Đ.8 K.1) | srs-fr-05:2451 | ✅ | UC54 verify deadline calculation + UC51 cột Cảnh báo |
| BR-SLA-02 | 4 mức cảnh báo SLA (BINH_THUONG/SAP_HET/QUA_HAN/QUA_HAN_NGHIEM_TRONG) | srs-fr-05:2457 | ✅ | UC51 verify badge + filter |
| BR-EC-01 | Optimistic Locking | srs-v3.md | ✅ | UC57 verify conflict update 2 user |
| BR-EC-13 | XSS sanitize input rich-text + max 200 ký tự search | srs-v3.md | ✅ | UC52/54 noi_dung_yeu_cau + NEW-05 mo_ta_cong_khai |

### 2.2 Error Codes — bảng tổng hợp

| Module/UC | Error Code | Message |
|-----------|-----------|---------|
| FR-V.I-02 (UC52 DN gửi) | ERR-GHS-01..04 | Nội dung trống / MST sai / DN thiếu BR-CALC-04 / File constraint |
| FR-V.I-04 (UC54 nhập thủ công) | ERR-NH-01..05 | Nội dung trống / MST sai / File constraint / DN thiếu BR-CALC-04 / uu_tien override thiếu lý do |
| FR-V.I-05 (UC55 CMS) | ERR-INTG-01..05, ERR-FILE-01..03, ERR-AUTH-01, ERR-VV-01 | HT chưa đăng ký / hồ sơ trùng / JSON sai / file vi phạm / xóa HS đã tiếp nhận |
| FR-V.I-06 (UC56 kiểm tra) | ERR-KT-01, ERR-KT-02 | VV không hợp lệ trạng thái / thiếu lý do |
| FR-V.I-07 (UC57 quản lý) | ERR-VV-02 | VV ở trạng thái không cho phép sửa |
| FR-V.I-08 (UC58 tìm kiếm) | INF-VV-TK-01, ERR-VV-TK-01 | Không có kết quả / tu_ngay > den_ngay |
| FR-V.I-09 (UC59 phân công) | ERR-PC-01..02, WRN-PC-01, ERR-PC-05..07 | VV không hợp lệ / đối tượng vô hiệu / không có đối tượng phù hợp / không cùng đơn vị / TVV không thuộc TC / loại='CA_NHAN' nhưng có TC |
| FR-V.I-10 (UC60 xác nhận) | ERR-XN-01, ERR-XN-02 | Không phải người được phân công / VV không ở DA_PHAN_CONG |
| FR-V.I-11 (UC61 trình PD) | ERR-TR-01, ERR-TR-02 | VV chưa kiểm tra / chưa phân công NHT |
| FR-V.I-12 (UC62 thông báo) | WRN-TB-01, WRN-TB-02 | Email fail / LGSP fail |
| FR-V.I-13 (UC63 PD) | ERR-PD-01..03 | VV không ở CHO_PHE_DUYET / không cùng cấp / thiếu lý do |
| FR-V.I-15 (UC65 cập nhật KQ NHT) | ERR-KQ-01, ERR-KQ-02 | Không phải người được phân công / VV không ở DANG_XU_LY |
| FR-V.I-16 (UC66 cập nhật KQ cuối) | ERR-KQ-03, ERR-KQ-04 | VV chưa có KQ NHT / VV không hợp lệ trạng thái |
| FR-V.I-17 (UC67 đánh giá) | ERR-DG-VV-01..04 | VV chưa hoàn thành / điểm ngoài 0-10 / đã đánh giá / không có quyền |
| FR-V.I-NEW-02 (DN bổ sung) | ERR-VV-BS-01..04 | VV không YEU_CAU_BO_SUNG / file constraint / quá hạn bổ sung / DN không phải chủ sở hữu |
| FR-V.I-NEW-05 (công khai) | ERR-CK-VV-01..10 (skip 06) | VV không hợp lệ / khác cấp / mô tả XSS / ảnh sai / file sai / API timeout / API 4xx / hủy khi cong_khai=0 / lý do < 20 ký tự |

### 2.3 Permission Matrix (cross-FR — chi tiết file 14)

| Entity / Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | NHT/TVV | DN |
|-----------------|------|-------------------|-------------------|---------|-----|
| Xem DS VV (UC51, SCR-01) | 👁 R toàn HT | ✅ R scope đơn vị | 👁 R scope đơn vị | ❌ | ❌ |
| Gửi HS qua chuyên trang (UC52) | ❌ | ❌ | ❌ | ❌ | ✅ scope DN mình |
| Nhập thủ công (UC54) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Kiểm tra HS (UC56) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Phân công NHT/TVV (UC59) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| NHT xác nhận tham gia (UC60) | ❌ | ❌ | ❌ | ✅ chỉ VV được phân công | ❌ |
| Trình phê duyệt (UC61) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Phê duyệt VV (UC63) | ❌ | ❌ | ✅ cùng cấp đơn vị | ❌ | ❌ |
| Cập nhật KQ NHT (UC65) | ❌ | ❌ | ❌ | ✅ chỉ VV được phân công | ❌ |
| Cập nhật KQ cuối (UC66) | ❌ | ✅ scope đơn vị | ❌ | ❌ | ❌ |
| Đánh giá VV (UC67) | ❌ | ✅ scope đơn vị (1 lần) | ❌ | ❌ | ✅ chỉ VV của DN mình (1 lần) |
| Công khai/Hủy CK (NEW-05) | ❌ | ❌ | ✅ cùng cấp đơn vị | ❌ | ❌ |
| Bổ sung HS (NEW-02) | ❌ | ❌ | ❌ | ❌ | ✅ chỉ VV của DN mình + state YEU_CAU_BO_SUNG |
| Cấu hình quy trình (NEW-01) | ✅ | ❌ | ❌ | ❌ | ❌ |
| DS Thông báo (UC64) | ❌ | ❌ | ❌ | ❌ | ✅ scope DN mình |

### 2.4 State Machine — SM-VUVIEC (chi tiết)

```
[*] → MOI_TAO → CHO_TIEP_NHAN → DA_TIEP_NHAN → DANG_KIEM_TRA
                                                    ├→ DA_PHAN_CONG (đạt + NHT chọn)
                                                    │     ├→ DANG_XU_LY (NHT xác nhận)
                                                    │     │     └→ CHO_PHE_DUYET (CB NV trình)
                                                    │     │           ├→ DA_DUYET → HOAN_THANH → DA_DANH_GIA
                                                    │     │           └→ DANG_XU_LY (CB PD từ chối, BR-FLOW-04)
                                                    │     └→ DA_TIEP_NHAN (NHT từ chối, phân công lại)
                                                    ├→ YEU_CAU_BO_SUNG (thiếu HS) ⟷ DANG_KIEM_TRA (DN bổ sung NEW-02)
                                                    │     └→ TU_CHOI (auto khi quá hạn BR-EC-16, hoặc lần 4 KHONG_DAT BR-EC-15)
                                                    └→ TU_CHOI (không đạt)

Self-loop overlay (NEW-05):
  DA_DUYET ⟷ DA_DUYET (cong_khai 0↔1)
  HOAN_THANH ⟷ HOAN_THANH (cong_khai 0↔1)
```

**Transitions chính (15 transitions):**

| # | From | To | Trigger | UC |
|---|------|-----|---------|-----|
| 1 | [*] | MOI_TAO | DN gửi HS qua chuyên trang | UC52 |
| 2 | [*] | CHO_TIEP_NHAN | API HT khác / nhập thủ công | UC55/54 |
| 3 | CHO_TIEP_NHAN | DA_TIEP_NHAN | CB NV tiếp nhận | UC51 (action) |
| 4 | DA_TIEP_NHAN | DANG_KIEM_TRA | CB NV mở Accordion 4 kiểm tra | UC56 |
| 5 | DANG_KIEM_TRA | DA_PHAN_CONG | Đạt + chọn NHT/TVV | UC56 → UC59 |
| 6 | DANG_KIEM_TRA | YEU_CAU_BO_SUNG | Thiếu HS (counter++) | UC56 |
| 7 | DANG_KIEM_TRA | TU_CHOI | Không đạt | UC56 |
| 8 | YEU_CAU_BO_SUNG | DANG_KIEM_TRA | DN bổ sung trong hạn | NEW-02 |
| 9 | DA_PHAN_CONG | DANG_XU_LY | NHT xác nhận | UC60 |
| 10 | DA_PHAN_CONG | DA_TIEP_NHAN | NHT từ chối + lý do | UC60 |
| 11 | DANG_XU_LY | CHO_PHE_DUYET | CB NV trình + có KQ NHT | UC61 |
| 12 | CHO_PHE_DUYET | DA_DUYET | CB PD duyệt cùng cấp | UC63 |
| 13 | CHO_PHE_DUYET | DANG_XU_LY | CB PD từ chối + lý do ≥10 ký tự | UC63 (BR-FLOW-04) |
| 14 | DA_DUYET | HOAN_THANH | CB NV cập nhật KQ cuối | UC66 |
| 15 | HOAN_THANH | DA_DANH_GIA | CB NV/DN đánh giá | UC67 |

**Auto-transitions (no manual trigger):**

| # | From | To | Trigger | BR |
|---|------|-----|---------|-----|
| AT-01 | YEU_CAU_BO_SUNG | TU_CHOI | Quá hạn 5 ngày LV | BR-EC-16 |
| AT-02 | DANG_KIEM_TRA | TU_CHOI | Lần 4 KHONG_DAT (counter ≥ 3) | BR-EC-15 |
| AT-03 | DANG_XU_LY → CHO_PHE_DUYET | "Trình phê duyệt" → auto chuyển + TB CB PD | UC61 |

**Self-loop CONG_KHAI (cờ overlay, NOT trạng thái):**

| State workflow | Trigger | Effect |
|----------------|---------|--------|
| DA_DUYET (cong_khai=0) | CB PD click [Công khai] + API Cổng OK | SET cong_khai=1 + thoi_gian_dang_tai=NOW() (BR-EC-20 atomic) |
| DA_DUYET (cong_khai=1) | CB PD click [Hủy công khai] + lý do ≥20 + API Cổng OK | SET cong_khai=0 + clear cột công khai |
| HOAN_THANH | Tương tự | Tương tự |

---

## 3. Cấu Trúc File Test Case

```
vu-viec/
├── 00-test-plan-overview.md
├── 01-TC-quan-ly-vu-viec-DS.md          ← FR-V.I-01 + FR-V.I-08 (UC51 + UC58, ~16 TC)
├── 02-TC-tao-vu-viec-DN.md              ← FR-V.I-02 (UC52, ~10 TC)
├── 03-TC-nhap-thu-cong-vv.md            ← FR-V.I-04 (UC54, ~12 TC)
├── 04-TC-tiep-nhan-cms-ht-khac.md       ← FR-V.I-05 CMS (UC55 phần CMS, ~8 TC)
├── 05-TC-kiem-tra-hs.md                 ← FR-V.I-06 (UC56, ~12 TC)
├── 06-TC-quan-ly-hs-vv.md               ← FR-V.I-07 (UC57, ~10 TC)
├── 07-TC-phan-cong-xac-nhan.md          ← FR-V.I-09 + FR-V.I-10 (UC59 + UC60, ~16 TC)
├── 08-TC-trinh-phe-duyet-pd.md          ← FR-V.I-11 + 12 + 13 (UC61 + 62 + 63, ~12 TC)
├── 09-TC-cap-nhat-ket-qua.md            ← FR-V.I-15 + FR-V.I-16 (UC65 + 66, ~10 TC)
├── 10-TC-danh-gia-vv.md                 ← FR-V.I-17 (UC67, ~8 TC)
├── 11-TC-cong-khai-vv.md                ← FR-V.I-NEW-05 (~12 TC)
├── 12-TC-DN-bo-sung-thong-bao.md        ← FR-V.I-NEW-02 + FR-V.I-14 (~8 TC)
├── 13-TC-cau-hinh-quy-trinh.md          ← FR-V.I-NEW-01 (~6 TC)
├── 14-TC-permission-matrix.md           ← Cross-FR-V.I permission (~10 TC)
├── 08-REVIEW-edge-case-hunter.md        ← A4 audit log
├── 09-traceability-matrix.md            ← A5 BR/AC ↔ TC matrix
├── 10-REVIEW-test-quality.md            ← A6 quality score
└── 11-a7-filter-log.md                  ← A7 filter log (UC53 LGSP + CROSS-01 scheduled LOẠI)
```

> **Phase B B-block ref CHỈ 14 file UC (01-14)**, total ~150 TC. File 08/09/10/11 là audit log không phải TC source.

---

## 4. Phân loại Test Case (chuẩn 4-section)

Mỗi file TC sử dụng cấu trúc 4 section như BM model:

| Section | Loại | Mục đích |
|---------|------|----------|
| **A. UI FIELD VERIFICATION** | UI | Verify form field, default value, conditional show/hide, badge, dropdown source |
| **B. CRUD HAPPY PATH** | Happy | Create / Read / Update / Delete / Transition flow chuẩn |
| **C. NEGATIVE — VALIDATION** | Negative | Error code, validation, file constraint, XSS sanitize, MST format |
| **D. EDGE CASES** | Edge | Concurrent UPDATE, optimistic lock, race condition, network fail, partial failure |

**Priority:**
- **P0** (Critical path): Login, transitions chính SM-VUVIEC, CRUD, công khai whitelist BR-PUBLIC-04, BR-EC-20 atomic
- **P1** (Standard): Filter, search, edge cases, error messages, audit log
- **P2** (Cosmetic): Tooltip, breadcrumb, responsive, sort

---

## 5. Cross-cutting concerns

### 5.1 SLA + Cảnh báo (BR-SLA-01..03)

- Mọi TC tạo VV → verify deadline = `ngay_tiep_nhan + 15 ngày làm việc` (NĐ55/2019 Đ.8 K.1)
- Mọi TC DS (UC51) → verify cột "Cảnh báo SLA" 4 màu (🟢/🟡/🔴/⚫)
- Scheduled job CROSS-01 30 phút LOẠI A7 — KHÔNG verify trực tiếp (verify gián tiếp qua badge khi VV vượt 50%/100%/200% deadline — manual time-shift hoặc seed VV ngày-tiếp-nhận lùi)

### 5.2 Audit trail (BR-DATA-05)

Mọi UC có CUD hoặc state transition phải verify entry mới trong `LICH_SU_VU_VIEC` với:
- `hanh_dong` IN (TAO_VV, TIEP_NHAN, KIEM_TRA, YEU_CAU_BO_SUNG, BO_SUNG_HS, PHAN_CONG, XAC_NHAN_PHAN_CONG, TU_CHOI_PHAN_CONG, CAP_NHAT_KQ, TRINH_PD, PHE_DUYET, TU_CHOI_PD, HOAN_THANH, DANH_GIA, MO_LAI, TU_CHOI_AUTO_QUA_HAN, CONG_KHAI, HUY_CONG_KHAI)
- `vai_tro` IN (CB_NV, CB_PD, NHT, DN, HE_THONG)
- `trang_thai_truoc` + `trang_thai_sau` chính xác
- Verify qua Timeline (SCR-V.I-03 sidebar) + DB query gián tiếp qua `list_network_requests` GET LICH_SU_VU_VIEC

### 5.3 Notification (BR-NOTIF-01)

- CB NV nhận: tiếp nhận DVC/HT khác, NHT xác nhận/từ chối, CB PD từ chối
- CB PD nhận: trình PD (UC61)
- NHT nhận: phân công (UC59), CB PD từ chối (cascade BR-FLOW-04)
- DN nhận: tiếp nhận, kết quả kiểm tra, hoàn thành, công khai, hủy công khai
- Verify in-app + email (mock SMTP) + nếu `loai='TO_CHUC'` → CC `TO_CHUC_TU_VAN.email_lien_he`

### 5.4 File Upload (cross-cutting)

Mọi TC có upload file phải test:
- Format: PDF/DOC/DOCX/XLS/XLSX (+ JPG/PNG cho file_scan UC54, NEW-02)
- Size: max 20MB/file, tổng 100MB, max 10 files
- Virus scan: ClamAV (EICAR test file)
- Boundary: 20MB exact (PASS), 21MB (FAIL)
- Concurrent: upload bị ngắt (network throttle Offline) → cleanup blob orphan

---

## 6. Test Data — Pre-seed yêu cầu

Phase B B-Seed sẽ tạo các record sau:

| Loại data | Số lượng | Trạng thái | Mục đích |
|-----------|---------:|-----------|----------|
| DOANH_NGHIEP đủ field BR-CALC-04 | 5 (1 phụ nữ làm chủ, 1 LĐ nữ ≥30%, 1 LĐ KT ≥30%, 2 thường) | HOAT_DONG | UC52, UC54 |
| DOANH_NGHIEP thiếu field BR-CALC-04 | 1 | HOAT_DONG | UC52 ERR-GHS-03 verify |
| TU_VAN_VIEN cá nhân | 5 (TVV/CG mỗi loại 2-3) | HOAT_DONG, đã CONG_KHAI | UC59 thẻ "Cá nhân" |
| TO_CHUC_TU_VAN + TVV thuộc tổ chức | 2 TC + 4 TVV (mỗi TC 2 TVV) | HOAT_DONG | UC59 thẻ "Tổ chức tư vấn" |
| NGUOI_HO_TRO | 3 | HOAT_DONG | UC59 thẻ "Cá nhân" → loại Người hỗ trợ |
| VU_VIEC mỗi state SM-VUVIEC | 12 (mỗi state 1 record min) | tương ứng | UC51 filter + UC56-67 transition |
| VU_VIEC qua thuần test cong_khai 0/1 | 4 (DA_DUYET cong_khai=0, DA_DUYET cong_khai=1, HOAN_THANH cong_khai=0, HOAN_THANH cong_khai=1) | tương ứng | NEW-05 |
| VU_VIEC YEU_CAU_BO_SUNG counter 0/1/2 | 3 | YEU_CAU_BO_SUNG | UC56 BR-EC-15 verify counter |
| HOP_DONG_TV_KE_HOACH (referenced) | 1 | DA_DUYET | Test field hop_dong_tv_id |

**Iron rule B-Seed:** Check existing trước khi tạo (KHÔNG tạo trùng). Query NotebookLM SRS (id `4dd0675e-...`) cho nghiệp vụ tạo data, KHÔNG đọc file local.

---

## 7. SPEC-CLARIFY backlog (gửi BA Phase B)

| ID | Nội dung |
|----|----------|
| SPEC-CLARIFY-VV-PERM-01 | CSV thiếu user CB_NV_BN/DP và CB_PD_BN/DP — cần xác nhận chiến lược test 3-tier scope: (a) tạm dùng `cb_nv_tw_01` workaround, (b) seed thêm user, (c) defer 3-tier permission tới sau |
| SPEC-CLARIFY-VV-NEW-01 | FR-V.I-NEW-01 cấu hình quy trình QTHT — SRS không spec màn hình UI cụ thể, giả định reuse SCR QTHT chung. Cần BA confirm SCR ID + URL truy cập |
| SPEC-CLARIFY-VV-CROSS-01 | BR-EC-16 timeout `cau_hinh_sla.bo_sung_timeout` mặc định 5 ngày LV — UC108 cấu hình chỗ nào? Test verify config UI nằm ở module QTHT (FR-VIII-06) hay FR-V.I-NEW-01? |
| SPEC-CLARIFY-VV-MO-LAI | UC "Mở lại hồ sơ" (TU_CHOI → DA_TIEP_NHAN) — SRS line 2334 placeholder "FR-V.I-xx", chưa có FR formal. Có nên test hay defer? |
| SPEC-CLARIFY-VV-DEEPLINK | URL deeplink chi tiết VV (vd `/vu-viec/{id}` vs `/ho-so-cua-toi/vu-viec/{id}` cho DN) — backend tự định tuyến theo phiên hay bind URL prefix? |

---

## 8. Output kỳ vọng

```
output/test-cases/vu-viec/
├── 00-test-plan-overview.md               (file này)
├── 01..14-TC-*.md                         (14 file UC, ~150 TC)
├── 08-REVIEW-edge-case-hunter.md          (A4 log audit)
├── 09-traceability-matrix.md              (A5)
├── 10-REVIEW-test-quality.md              (A6)
└── 11-a7-filter-log.md                    (A7 — track UC53 LGSP + CROSS-01 LOẠI)
```

---

## 9. Liên kết

- SRS Source of Truth: [`srs-fr-05-vu-viec-v3.1.md`](../../../input/srs-v3/srs-fr-05-vu-viec-v3.1.md)
- BR Phụ lục B: [`srs-v3.md` line 3939-4088](../../../input/srs-v3/srs-v3.md)
- Permission matrix tổng: [`permission-matrix.md`](../../permission-matrix.md)
- Template TC: [`output/template/`](../../template/)
- Plan tổng: [`tasks/detailed-tc/plan.md`](../../../tasks/detailed-tc/plan.md)
- Todo W3.2: [`tasks/detailed-tc/todo.md`](../../../tasks/detailed-tc/todo.md) §Wave 3 → W3.2
