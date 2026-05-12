# Kế Hoạch Kiểm Thử — Vụ việc TGPL (FR-05, SCR-V.I-01..03)

> **Phiên bản**: 1.1
> **Ngày tạo**: 2026-05-12
> **Revised 2026-05-12 13:00:00 — apply ≥80% review.md feedback** (4 blocker + 8 suggestion).
> **Nguồn dữ liệu**: SOURCE MODE = **LOCAL** (`srs-v3/srs-fr-05-vu-viec.md` + `srs-update-2026-5-5/srs-fr-05-vu-viec.md`)

## SPEC-CLARIFY tickets (BA confirm trước R1)

| # | Vấn đề | Nguồn mâu thuẫn | Câu hỏi BA | Block TC |
|:-:|---|---|---|---|
| SC-01 | **Soft-delete vs Hard-delete cho VU_VIEC** — BR-DATA-01 (`srs-update-2026-5-5/srs-fr-05-vu-viec.md:2397-2401`) ghi "Mọi thao tác xóa là soft delete `is_deleted=1`". Cross-cutting C1 (`input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md:229`) ghi "Hard-delete toàn dự án, bỏ DA_XOA". 2 nguồn nói khác nhau cho cùng entity VU_VIEC. | SRS FR-05 vs tổng quan §6.3 (1) | VU_VIEC xóa = soft (`is_deleted=1`) hay hard (`DELETE FROM`)? Áp dụng cho cả CB NV TW xóa lẫn purge admin? | TC-DELETE-01..02 + TC25 migration |
| SC-02 | **BR-AUTH-10 áp dụng cho FR-05 nguồn gốc** — `srs-update-2026-5-5/srs-fr-05-vu-viec.md` KHÔNG nhắc BR-AUTH-10 lần nào, CHANGELOG dòng 17 ghi "BR-AUTH-10 OUT". Cite hiện chỉ ở `01-tong-quan-nghiep-vu.md:194-197`. | Tổng quan vs SRS FR-05 | BR-AUTH-10 (lọc kép TVV/NHT/CG) còn áp dụng cho FR-05 phân công UC59 hay đã out? Owner FR nào? | TC-NHT-01..03 |
| SC-03 | **3 placeholder transition không có FR formal** — T15 auto-return NHT timeout, T21 mở lại từ TU_CHOI, T12 auto 3 lần YCBS (`_DELTA-MAP-FR05.md` §3 Findings #7). Test plan §2.5 hiện ghi "(placeholder dev impl UI v3)". | Thay đổi 5/6/7 OUT | Behavior chính thức UI/BR cho 3 transition này? Defer hay test theo v3? | TC-PLACEHOLDER-01..03 |
| SC-04 | **UC106 checklist versioning** — Checklist 6 hạng mục là configurable (UC106 thuộc FR-10). QTHT thay đổi UC106 sau khi VV đã DANG_KIEM_TRA — VV xài checklist nào? Có versioning giống FR-V.I-NEW-01 không? | SRS:516-523 + cross FR-10 | VV `DANG_KIEM_TRA` đã snapshot checklist tại `ngay_bat_dau_kt` hay đọc realtime? | TC-KT-04 |
| SC-05 | **NĐ55 Đ.8 K.1 SLA 15 ngày** — chưa web-verify với văn bản pháp lý gốc (`_DELTA-MAP-FR05.md` §6 Open issues). BE có thể deploy theo SLA cũ NĐ55 Đ.9 (10 ngày). | NĐ55 Đ.8 K.1 vs Đ.9 | SLA chính thức 15 hay 10 ngày LV? Cite văn bản nguồn? | TC-SLA-04 |
| SC-06 | **DN account auth trên QA env** — VNeID Tier 2 sandbox NĐ 69/2024 chưa wire. Account `9999999990` là MST DN, không phải VNeID user thật. | NĐ 69/2024 sandbox | DN test login thế nào ở QA (mock cookie/role overlay/sandbox VNeID đã có)? | TC FR-V.I-02/04/14, TC24 |

> Mỗi SC ticket trên là **gate blocker** TC liên quan — không log bug nếu BA chưa confirm. Khi BA reply, update test-plan và remove ticket.


> **SRS Reference**:
> - FR-V.I-01 → FR-V.I-17, FR-V.I-NEW-01, FR-V.I-NEW-02, FR-V.I-NEW-05, FR-V.I-CROSS-01
> - SCR-V.I-01 (Danh sách), SCR-V.I-02 (Thêm/Nhập thủ công), SCR-V.I-03 (Chi tiết — chế độ CB + DN), SCR-V.I-04 (DN — Danh sách của tôi), SCR-V.I-05 (DN — Thông báo)
> - UC51-UC67 + UC mới (UC106 checklist 6 hạng mục, UC108 cấu hình SLA)
> - State Machine SM-VUVIEC (12 state)
> - Delta v3.5 (2026-05-06): 14 thay đổi IN + 1 V4-CHƯA-SỬA — xem [`_DELTA-MAP-FR05.md`](../../../input/srs-update-2026-5-5/_DELTA-MAP-FR05.md)

> **Quy trình:** Theo [scaling-test-strategy.md §4.1 Bước 3](../../../output/scaling-test-strategy.md) — trích BR từ SRS + sibling-check FR-02 / FR-12 (cùng nhóm xử lý lifecycle có CB NV / CB PD / TVV) + BA sign-off.
>
> **v3.0:** Test plan này dùng cho **GĐ 3 Functional + Auth + Edge + Cross-module**. GĐ 1 Seed + GĐ 2 Workflow là 2 phase riêng, output `seed-checklist-fr-05.md` + `workflow-test-report-fr-05.md`. Happy path đã cover ở GĐ 2 — TC ở đây chỉ còn **negative + edge + auth + cross-module + công khai + DN bổ sung**.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

Module FR-05 (Nhóm V.I) **Quản lý Vụ việc Trợ giúp Pháp lý** — entity trung tâm, core nhất hệ thống (tag ⭐ CORE trong [`02-thu-tu-module.md:33`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md)).

- **UC range:** UC 51 → UC 67 + 3 UC mới (UC NEW-01 Cấu hình quy trình, UC NEW-02 DN bổ sung HS, UC NEW-05 Công khai VV) — 21 FR tổng (`srs-update-2026-5-5/srs-fr-05-vu-viec.md:7`).
- **Entity chính (owned 6):** `VU_VIEC`, `HO_SO_VU_VIEC`, `KET_QUA_VU_VIEC`, **`PHAN_CONG_VU_VIEC`** (mới v3.5), **`DANH_GIA_VU_VIEC`** (mới v3.5), **`LICH_SU_VU_VIEC`** (mới v3.5 — audit trail neutral 18 hành động).
- **Entity referenced (11):** `DOANH_NGHIEP`, `TU_VAN_VIEN` (loai `TVV`/`CG`), `NGUOI_HO_TRO` (NĐ55 Đ.7), `TO_CHUC_TU_VAN` (Cty Luật / VP LS / TT TVPL), `TAI_KHOAN`, `DON_VI` (2 tầng: TW + BN/ĐP ngang cấp), `DANH_MUC`, `FILE_DINH_KEM`, `CAU_HINH_SLA`, `CAU_HINH_QUY_TRINH`, `THONG_BAO`.
- **State Machine:** SM-VUVIEC — **12 trạng thái, 21 transition + 3 self-loop** (SL1 công khai DA_DUYET / SL2 công khai HOAN_THANH / SL3 hủy công khai) — khớp §2.5 đếm 21 transition + 3 self-loop.
- **Màn hình:** 5 SCR
  - SCR-V.I-01 Danh sách HS (CB) — 6 tab + 23 component (`srs-update-2026-5-5/srs-fr-05-vu-viec.md:1652-1693`)
  - SCR-V.I-02 Thêm/Nhập thủ công (CB) — 4 accordion + 34 component (`:1695-1747`)
  - SCR-V.I-03 Chi tiết (CB + DN) — 8 accordion + Stepper + action context-sensitive 13 row (`:1750-1847`)
  - SCR-V.I-04 Danh sách VV của tôi (DN, mobile-first) — 15 component (`:1850-1887`)
  - SCR-V.I-05 Thông báo của tôi (DN, polling 30s) — 7 component (`:1889-1917`)

**Scope v3.5 delta (mới so v3):**
- 5 trường công khai CR-01 (`cong_khai`, `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`) — `srs-update-2026-5-5/srs-fr-05-vu-viec.md:2074-2079`.
- 3 cột phân công mới (`loai_doi_tuong_xu_ly`, `nguoi_xu_ly_id`, `to_chuc_tu_van_id`) thay `nguoi_ho_tro_id` — `srs-update-2026-5-5/srs-fr-05-vu-viec.md:2059-2062`.
- SLA 15 ngày LV (NĐ55 Đ.8 K.1) thay 10 ngày (NĐ55 Đ.9) — `srs-update-2026-5-5/srs-fr-05-vu-viec.md:43`.
- CB PD từ chối → DANG_XU_LY (KHÔNG TU_CHOI đóng VV) — `srs-update-2026-5-5/srs-fr-05-vu-viec.md:975-998` + BR-FLOW-04.
- DN auth Tier 2 VNeID + lookup DN từ session/MST (FR-V.I-02/04/14) — `srs-update-2026-5-5/srs-fr-05-vu-viec.md:157, 1014`.
- BR-PUBLIC-04 whitelist 9 fields công khai + ẩn 6 nhạy cảm (NĐ 13/2023) — `srs-update-2026-5-5/srs-fr-05-vu-viec.md:2517-2521`.
- UC67 chỉ {CB_NV, DN} (loại CB_PD), thang 0-10, UNIQUE(`vu_viec_id`, `loai_nguoi_danh_gia`) — `srs-update-2026-5-5/srs-fr-05-vu-viec.md:1163-1227`.
- Hard-delete toàn dự án (bỏ DA_XOA): cross-cutting C1 — không có row "DA_XOA" trong CHECK trạng thái.

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|---------------|--------|----------------|
| 1 | FR-V.I-01 | UC51 | Quản lý hồ sơ yêu cầu HTPL (danh sách + filter + SLA) | VU_VIEC | `01-TC-list-filter.md` |
| 2 | FR-V.I-02 | UC52 | DN gửi HS qua chuyên trang (auth Tier 2 VNeID) | VU_VIEC, HO_SO_VU_VIEC | `02-TC-dn-gui-hs.md` |
| 3 | FR-V.I-03 | UC53 | Tiếp nhận HS qua DVC (LGSP inbound) | VU_VIEC | `03-TC-dvc-inbound.md` |
| 4 | FR-V.I-04 | UC54 | CB NV nhập HS thủ công (TRỰC_TIẾP/ĐIỆN_THOẠI/BƯU_CHÍNH) | VU_VIEC | `04-TC-nhap-tay.md` |
| 5 | FR-V.I-05 | UC55 | Tiếp nhận từ HT khác (REST API trực tiếp) | VU_VIEC | `05-TC-htk-inbound.md` |
| 6 | FR-V.I-06 | UC56 | Kiểm tra HS — checklist 6 hạng mục UC106 + BR-EC-15 (≤3 lần) | VU_VIEC, LICH_SU_VU_VIEC | `06-TC-kiem-tra.md` |
| 7 | FR-V.I-07 | UC57 | Quản lý HS vụ việc (xem/sửa/upload bổ sung) | VU_VIEC, HO_SO_VU_VIEC | `07-TC-chi-tiet.md` |
| 8 | FR-V.I-08 | UC58 | Tìm kiếm + lọc HS (AND) | VU_VIEC | `01-TC-list-filter.md` (gộp) |
| 9 | FR-V.I-09 | UC59 | Phân công xử lý — modal 2 thẻ Cá nhân/Tổ chức + BR-CALC-04 | PHAN_CONG_VU_VIEC, VU_VIEC | `09-TC-phan-cong.md` |
| 10 | FR-V.I-10 | UC60 | NHT/TVV/CG xác nhận tham gia hoặc từ chối | PHAN_CONG_VU_VIEC | `10-TC-xac-nhan.md` |
| 11 | FR-V.I-11 | UC61 | Trình phê duyệt (AT-03 auto-transition) | VU_VIEC | `11-TC-trinh-pd.md` |
| 12 | FR-V.I-12 | UC62 | Thông báo kết quả tiếp nhận (in-app + email + LGSP) | THONG_BAO | `12-TC-thong-bao.md` |
| 13 | FR-V.I-13 | UC63 | CB PD phê duyệt / từ chối (→ DANG_XU_LY, không TU_CHOI) + batch PD | VU_VIEC | `13-TC-phe-duyet.md` |
| 14 | FR-V.I-14 | UC64 | DN nhận thông báo (Tier 2 VNeID) | THONG_BAO | `14-TC-dn-thong-bao.md` |
| 15 | FR-V.I-15 | UC65 | NHT cập nhật kết quả hỗ trợ | KET_QUA_VU_VIEC | `15-TC-cap-nhat-kq.md` |
| 16 | FR-V.I-16 | UC66 | CB NV đóng hồ sơ (→ HOAN_THANH) | VU_VIEC | `16-TC-dong-hs.md` |
| 17 | FR-V.I-17 | UC67 | Đánh giá VV (chỉ {CB_NV, DN}, thang 0-10, UNIQUE per loại) | DANH_GIA_VU_VIEC | `17-TC-danh-gia.md` |
| 18 | FR-V.I-NEW-01 | UC mới | QTHT cấu hình quy trình + versioning | CAU_HINH_QUY_TRINH | `18-TC-cau-hinh-quy-trinh.md` |
| 19 | FR-V.I-NEW-02 | UC mới | **DN bổ sung HS (YEU_CAU_BO_SUNG → DANG_KIEM_TRA)** | VU_VIEC, HO_SO_VU_VIEC | `19-TC-dn-bo-sung.md` |
| 20 | FR-V.I-NEW-05 | UC mới | **Công khai VV lên Cổng PLQG + Hủy công khai (CB PD)** | VU_VIEC (5 cột CR-01) | `20-TC-cong-khai.md` |
| 21 | FR-V.I-CROSS-01 | — | Scheduled job SLA + auto-reject quá hạn bổ sung | VU_VIEC, CAU_HINH_SLA | `21-TC-sla-cross.md` |

### 1.3 Tài khoản & role liên quan

> Reference: [`input/users.csv`](../../../input/users.csv), [`output/permission-matrix.md`](../../../output/permission-matrix.md)

| Role | Cấp | Username primary (users.csv) | Fallback / Permission test | Dùng cho TC loại |
|------|-----|------------------------------|----------------------------|-------------------|
| QTHT | — | `qtht_01` | `qtht_02` / `qtht_03..10` | Cấu hình quy trình (UC NEW-01), cấu hình SLA UC108, mở lại HS từ TU_CHOI |
| CB_NV_TW | TW | `cb_nv_tw_01` | `cb_nv_tw_02` / `cb_nv_tw_03..10` | Tiếp nhận/kiểm tra/phân công/trình PD/đóng HS phạm vi toàn quốc |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH) | `cb_nv_bn_02` (BTC) / `cb_nv_bn_03..10` | Test scope BN (đơn vị mình) + BR-AUTH-03/04 cross-unit |
| CB_NV_DP | ĐP | `cb_nv_dp_01` (Sở TP AG) | `cb_nv_dp_02` (BG) / `cb_nv_dp_03..10` | Test scope ĐP + sibling-DP isolation |
| CB_PD_TW | TW | `cb_pd_tw_01` | `cb_pd_tw_02..10` | Phê duyệt TW + công khai/hủy công khai (BR-AUTH-05) |
| CB_PD_BN | BN | `cb_pd_bn_01` | `cb_pd_bn_02..10` | Phê duyệt BN cùng cấp + BR-AUTH-05 |
| CB_PD_DP | ĐP | `cb_pd_dp_01` (AG) | `cb_pd_dp_02` (BG) / `cb_pd_dp_03..10` | Phê duyệt ĐP cùng cấp + công khai VV ĐP |
| NHT | ĐP | `nht_01` (AG) | `nht_02` (Đà Nẵng) / `nht_btp_tw_audit_r30` | Xác nhận/từ chối phân công, cập nhật KQ (UC60/UC65), lọc kép BR-AUTH-10 |
| TVV | — | (cần seed riêng — không có trong users.csv hiện tại) | — | Xác nhận phân công loại CA_NHAN, cập nhật KQ |
| CG | TW | `huongcg` (Đoàn LS Hà Nội) | — | Xác nhận phân công CA_NHAN loại CG (cá nhân ngoài) |
| DN | — | `9999999990` (HN), `9999999991` (BG) | — | Gửi HS qua chuyên trang (UC52), bổ sung HS (UC NEW-02), đánh giá (UC67), xem SCR-V.I-04/05 |

> **Lưu ý seed TVV/Tổ chức TV:** Chưa có TVV/CG dedicated trong `users.csv`. Cần seed song song với GĐ 1 Workflow (`seed-checklist-fr-05.md`) — đẩy state `TU_VAN_VIEN.trang_thai='HOAT_DONG'` cho ≥3 TVV/cấp ĐP + ≥1 CG/TW + ≥1 TC TV `HOAT_DONG` với ≥2 TVV thuộc tổ chức. Verify query: `?loai_tvv=TVV&trang_thai=HOAT_DONG`, `?loai_tvv=CG&trang_thai=HOAT_DONG`, `TO_CHUC_TU_VAN?trang_thai=HOAT_DONG`. KHÔNG fallback "đủ count" mà không đủ filter (rule [feedback_seed_acceptance_strict_split](../../../tasks/lessons-learned.md)).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> ⚠️ **Quy định điền bảng:**
> - Cột "**Ngoại lệ SRS-quoted**": chỉ điền khi SRS có dòng ngoại lệ cụ thể (quote nguyên văn + link line).
> - Để trống nếu không có ngoại lệ SRS — nghĩa là **BR áp dụng 100%** cho module này.
> - **KHÔNG** viết "KHÔNG áp dụng cho module X" nếu không có SRS quote → thay bằng SPEC-CLARIFY ticket.

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|---------------------|---------------------|-----------|
| BR-AUTH-01 | Xác thực 2-tier: Tier 1 nội bộ (user/pass + TOTP) cho cán bộ, Tier 2 VNeID SSO cho DN/TVV/CG | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2378-2383 | ✅ Yes (mọi FR) | — | TC-AUTH-01..05 cross-cutting |
| BR-AUTH-02 | Phân cấp 2 tầng — TW cấp 1; BN/ĐP cấp 2 ngang cấp (KHÔNG còn cha-con BN→ĐP) | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2229-2236 | ✅ Yes | — | TC-PERM-01..03 (BN ≠ ĐP scope) |
| BR-AUTH-03/04 | TW xem toàn quốc; BN/ĐP chỉ xem `don_vi_id` mình; BN và ĐP ngang cấp KHÔNG thấy nhau | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2469-2473 | ✅ Yes | "QTHT thấy tất cả" (BR-AUTH-08 exception line 2393) | TC-PERM-04..08 (cross-unit, cross-cap) |
| BR-AUTH-05 | Phê duyệt cùng cấp — CB PD chỉ duyệt VV trong cùng `don_vi_id` với CB NV trình | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2385-2389 | ✅ Yes | — | TC-PD-01..04, TC-CK-01 (công khai cũng theo cùng cấp) |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` cho mọi entity có cột — ngoại trừ QTHT và CB TW | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2391-2395 | ✅ Yes | "QTHT và Cán bộ Trung ương" — line 2393 | TC-PERM-09..12 (data isolation) |
| BR-AUTH-10 | TVV/NHT/CG lọc kép — Lớp 1 data scope + Lớp 2 phân công đích danh | `input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md:194-197` (cite chỉ tong-quan; CHANGELOG-v3-to-v3.5:17 ghi "BR-AUTH-10 OUT") | ⚠️ **SPEC-CLARIFY SC-02** — nguồn chính thức cho FR-05? | — | TC-NHT-01..03 **chờ BA confirm SC-02 trước log bug** |
| BR-DATA-01 | Soft delete (`is_deleted=1`) — KHÔNG xóa vật lý ngoài purge | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2397-2401 | ⚠️ **SPEC-CLARIFY SC-01** — mâu thuẫn C1 hard-delete | `input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md:229` "Hard-delete toàn dự án" — XUNG ĐỘT với BR-DATA-01 cho cùng entity VU_VIEC | TC-DELETE-01..02 **BLOCKED chờ BA confirm SC-01** |
| BR-DATA-02 | Multi-tenant scoping — mọi bản ghi nghiệp vụ có `don_vi_id` NOT NULL + filter query | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2403-2407 | ✅ Yes | — | TC-DATA-01 (check don_vi_id NOT NULL) |
| BR-DATA-03 | Common fields (7) — id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2409-2413 | ✅ Yes | — | TC-DATA-02 (verify 7 cột common) |
| BR-DATA-04 | Auto-gen mã `PREFIX-{TINH}-YYYYMMDD-SEQ` (VV-HCM-20260325-001) | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2415-2419 | ✅ Yes | — | TC-CREATE-01 (verify mã format + unique) |
| BR-DATA-05 | Audit trail mọi CUD + login + chuyển trạng thái → AUDIT_LOG immutable | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2421-2425 | ✅ Yes | — | TC-AUDIT-01..04 (LICH_SU_VU_VIEC 18 hành động) |
| BR-DATA-06 | Export Excel max 10k rows | srs-v3.md Phụ lục B (cross-cut) | ✅ Yes (default) | — | TC-EXPORT-01..02 (toolbar [Xuất Excel] line 1663) |
| BR-DATA-07 | Pagination default 20/page, max 100 | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2427-2431 | ✅ Yes | — | TC-PAGE-01 (verify SCR-V.I-01 line 1684 "Mặc định 20/trang") |
| BR-FLOW-03 | KHÔNG sửa/xóa sau "Đã duyệt" hoặc "Hoàn thành" (QTHT force-edit audit) | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2433-2437 | ✅ Yes | — | TC-LOCK-01 (verify VV đã duyệt KHÔNG sửa được) |
| BR-FLOW-04 | Từ chối phê duyệt BẮT BUỘC lý do ≥10 ký tự + lưu audit + thông báo CB NV | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2439-2443 + line 975-998 + line 1784 | ✅ Yes | — | TC-PD-02 (verify message line 1816 "quay về Đang xử lý") |
| BR-CALC-03 | Tính % SLA theo công thức `(NOW() - ngay_tiep_nhan) / deadline × 100` — job CROSS-01 30 phút | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2475-2479 | ✅ Yes | — | TC-SLA-01..03 (verify 4 mức cảnh báo BR-SLA-02) |
| BR-CALC-04 | Ưu tiên phân công NĐ55 Đ.4 — (1) +3 phụ nữ làm chủ, (2) +2 nhiều LĐ nữ, (3) +2 ≥30% LĐ KT, (4) +1 FIFO | srs-update-2026-5-5/srs-fr-05-vu-viec.md:65-70, 2445-2449, FR-V.I-09 line 718-724 | ✅ Yes | — | TC-PC-01..04 (verify thứ tự gợi ý + override + ly_do_uu_tien) |
| BR-CALC-06 | Cập nhật `TU_VAN_VIEN.diem_danh_gia_tb` từ DANH_GIA_SAU_VU_VIEC (FR-IV-CROSS-01) — thang 1-5 round-half-up | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2481-2485 + line 2070 | ✅ Yes (cross-ref FR-IV) | "UC67 chỉ tạo DANH_GIA_VU_VIEC (thang 0-10); trigger cập nhật điểm TVV ở FR-IV-CROSS-01" line 2483 | TC-EVAL-04 (verify thang 0-10 VV ≠ thang 1-5 TVV) |
| BR-EC-01 | Optimistic Locking (mọi UPDATE/DELETE) | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2340 "optimistic locking" + line 1623 modal | ✅ Yes | — | TC-CONFLICT-01 (verify modal "đã được {user} cập nhật lúc {time}") |
| BR-EC-13 | Search sanitize max 200 ký tự | srs-v3.md Phụ lục B (cross-cut) | ✅ Yes (default) | — | TC-SEARCH-01..02 (filter line 1665 + SQL/XSS) |
| BR-EC-15 | YCBS tối đa 3 lần — sau lần 3 nếu vẫn KHONG_DAT → auto TU_CHOI | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2487-2491 + line 1801 | ✅ Yes | — | TC-YCBS-01..03 (verify counter, highlight đỏ ≥2, auto TU_CHOI lần 3) |
| BR-EC-16 | Quá hạn bổ sung auto-reject — `NOW() - ngay_yeu_cau_bo_sung > cau_hinh_sla.bo_sung_timeout` (mặc định 5 ngày LV) | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2493-2497 + line 1319 + line 1803 | ✅ Yes | — | TC-NEW02-04 (verify ERR-VV-BS-03 quá hạn + auto reject job) |
| BR-EC-20 | KHÔNG set `cong_khai=1/0` trước khi API Cổng PLQG OK — fail thì giữ state cũ + toast retry | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2505-2509 + line 1399-1402 | ✅ Yes | — | TC-CK-04..05 (mock API fail → verify state KHÔNG flip) |
| BR-PUBLIC-01 | Điều kiện công khai: chỉ bản ghi state cuối (Đã duyệt / Hoàn thành / Đã đánh giá); TU_CHOI/Hủy KHÔNG được công khai | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2511-2515 | ✅ Yes | — | TC-CK-01 (verify chặn công khai từ DANG_XU_LY / TU_CHOI) |
| BR-PUBLIC-04 | Whitelist 9 fields công khai VU_VIEC + ẩn 6 nhạy cảm (tên DN, người đại diện, CCCD/MST, mô tả nội bộ, file nghiệp vụ, noi_dung_tu_van, SĐT/email/địa chỉ) — NĐ 13/2023 + NQ 03/2017 | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2517-2523 + line 1398 | ✅ Yes | — | TC-CK-02..03 (verify API payload outbound chỉ 9 fields) |
| BR-NOTIF-01 | Mọi event workflow → thông báo in-app + email; TO_CHUC kèm CC email tổ chức | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2499-2503 | ✅ Yes | — | TC-NOTIF-01..06 (verify từng event sends notif) |
| BR-SLA-01 | SLA mặc định VV HTPL = **15 ngày làm việc** (NĐ55/2019 Đ.8 K.1 — DNNVV) | srs-update-2026-5-5/srs-fr-05-vu-viec.md:43, 2451-2455 + line 334 step 8 | ⚠️ **SPEC-CLARIFY SC-05** — NĐ55 Đ.8 K.1 chưa web-verify | "Có thể cấu hình khác tại UC108" line 2453. ⚠️ Nếu BE trả deadline = 10 ngày LV (NĐ55 Đ.9 cũ) → verify BA trước khi log bug | TC-SLA-04 |
| BR-SLA-02 | 4 mức cảnh báo SLA — BINH_THUONG (>50% còn) / SAP_HET (≤50%) / QUA_HAN (>100%) / QUA_HAN_NGHIEM_TRONG (>200%) | srs-update-2026-5-5/srs-fr-05-vu-viec.md:1481-1488, 2457-2461 | ✅ Yes | — | TC-SLA-02 (verify 4 mức badge SCR-V.I-01 cột 20) |
| BR-SLA-03 | Cảnh báo SLA gửi TB theo mức — SAP_HET→CB NV / QUA_HAN→CB NV+CB PD / NGHIEM_TRONG→escalate cấp trên | srs-update-2026-5-5/srs-fr-05-vu-viec.md:2463-2467 | ✅ Yes | — | TC-SLA-05..06 (verify notif gửi đúng người theo mức) |
| BR-LEGAL-02 | Checklist UC106 — 6 hạng mục (Mẫu 01 NĐ55, ĐKKD, Quy mô DN, HĐ TV, VB TV đầy đủ, VB TV loại BMKD) | srs-update-2026-5-5/srs-fr-05-vu-viec.md:516-523 + line 2322 | ✅ Yes | — | TC-KT-01..03 (verify 6 hạng mục từ UC106 config) |
| BR-NĐ77-19 | TVV PL hiệu lực toàn quốc — KHÔNG dùng "địa bàn" làm lọc, dùng "đơn vị quản lý" | srs-update-2026-5-5/srs-fr-05-vu-viec.md:751, 1766, 2208 | ✅ Yes | — | TC-PC-05 (verify SCR-V.I-03 Accordion 5 label "đơn vị quản lý") |

> **Bổ sung BR specific module FR-05** (≥3 BR riêng): BR-EC-15 / BR-EC-16 / BR-EC-20 / BR-PUBLIC-01 / BR-PUBLIC-04 / BR-LEGAL-02 / BR-NĐ77-19 / BR-SLA-01 + 2 BR liên quan SM (CB PD từ chối → DANG_XU_LY không TU_CHOI, đánh giá UNIQUE per loai_nguoi_danh_gia).

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Severity |
|--------|-------------------|----------------------|----------|
| ERR-GHS-01 | Nội dung yêu cầu trống (UC52) | "Nội dung yêu cầu là bắt buộc" | ERROR |
| ERR-GHS-02 | MST không hợp lệ (UC52) | "Mã số thuế không hợp lệ" | ERROR |
| ERR-GHS-03 | DN thiếu BR-CALC-04 (UC52) | "Vui lòng cập nhật thông tin DN (lao động, doanh thu, ngành nghề, quy mô) trước khi gửi yêu cầu" | ERROR |
| ERR-GHS-04 | File vi phạm constraint (UC52) | "File vượt quá dung lượng/số lượng cho phép hoặc sai định dạng" | ERROR |
| ERR-NH-01 | Nội dung trống (UC54) | "Nội dung yêu cầu là bắt buộc" | ERROR |
| ERR-NH-02 | MST format lỗi (UC54) | "Mã số thuế không hợp lệ" | ERROR |
| ERR-NH-04 | DN thiếu thông tin BR-CALC-04 (UC54) | "DN thiếu thông tin bắt buộc (lao động/doanh thu/ngành nghề/quy mô). Cập nhật DN trước" | ERROR |
| ERR-NH-05 | `uu_tien` override thiếu `ly_do_uu_tien` | "Phải nhập lý do ưu tiên khi override giá trị hệ thống" | ERROR |
| ERR-DVC-01 | JSON LGSP không hợp lệ | "Cấu trúc dữ liệu không hợp lệ" | ERROR |
| ERR-DVC-02 | Mã HS DVC trùng | "Hồ sơ đã tiếp nhận trước đó" | ERROR |
| ERR-INTG-01 | HT nguồn chưa đăng ký (UC55) | "Hệ thống chưa được đăng ký" | ERROR |
| ERR-INTG-02 | Hồ sơ trùng (ma_ho_so_nguon + he_thong_nguon) | "Hồ sơ đã tồn tại" | ERROR |
| ERR-FILE-01 | File ≥20MB | "Tệp vượt quá 20MB" | ERROR |
| ERR-FILE-02 | File chứa mã độc | "Tệp chứa mã độc, không thể tiếp nhận" | ERROR |
| ERR-KT-01 | VV không ở DA_TIEP_NHAN/DANG_KIEM_TRA | "Vụ việc không ở trạng thái cho phép kiểm tra" | ERROR |
| ERR-KT-02 | Thiếu lý do bổ sung/từ chối | "Lý do là bắt buộc" | ERROR |
| ERR-VV-02 | Sửa VV ở HOAN_THANH/DA_DANH_GIA | "Không thể chỉnh sửa vụ việc đã hoàn thành" | ERROR |
| ERR-PC-01 | VV không ở DANG_KIEM_TRA hoặc DA_TIEP_NHAN | "Vụ việc không ở trạng thái cho phép phân công" | ERROR |
| ERR-PC-02 | Cá nhân/TC bị vô hiệu hóa | "Đối tượng được chọn đã bị vô hiệu hóa" | ERROR |
| ERR-PC-05 | VV không thuộc đơn vị user | "Bạn không có quyền phân công VV của đơn vị khác" | ERROR |
| ERR-PC-06 | TVV được chọn KHÔNG thuộc TC TV được chọn | "Tư vấn viên '{ten_tvv}' không thuộc Tổ chức '{ten_tc}'. Vui lòng chọn lại" | ERROR |
| ERR-PC-07 | `loai='CA_NHAN'` nhưng có truyền `to_chuc_tu_van_id` | "Phân công cá nhân không cần chọn Tổ chức tư vấn" | ERROR |
| WRN-PC-01 | Không có đối tượng phù hợp lĩnh vực | "Không tìm thấy đối tượng phù hợp lĩnh vực" | WARNING |
| ERR-XN-01 | NHT không phải người được phân công | "Bạn không được phân công cho vụ việc này" | ERROR |
| ERR-XN-02 | VV không ở DA_PHAN_CONG | "Vụ việc không ở trạng thái chờ xác nhận" | ERROR |
| ERR-TR-01 | VV chưa kiểm tra | "Hồ sơ chưa kiểm tra đạt" | ERROR |
| ERR-TR-02 | Chưa phân công NHT | "Chưa phân công người hỗ trợ" | ERROR |
| ERR-PD-01 | VV không ở CHO_PHE_DUYET | "Vụ việc không ở trạng thái chờ phê duyệt" | ERROR |
| ERR-PD-02 | CB PD không cùng cấp | "Bạn không có quyền phê duyệt vụ việc này" | ERROR |
| ERR-PD-03 | Thiếu lý do từ chối | "Lý do từ chối là bắt buộc" | ERROR |
| ERR-KQ-01 | NHT không phải người được phân công | "Bạn không được phân công cho vụ việc này" | ERROR |
| ERR-KQ-02 | VV không ở DANG_XU_LY | "Vụ việc không ở trạng thái đang xử lý" | ERROR |
| ERR-KQ-03 | VV chưa có kết quả NHT | "Vụ việc chưa có kết quả hỗ trợ từ NHT" | ERROR |
| ERR-DG-VV-01 | VV chưa hoàn thành | "Vụ việc chưa hoàn thành" | ERROR |
| ERR-DG-VV-02 | Điểm ngoài 0-10 | "Điểm phải từ 0 đến 10" | ERROR |
| ERR-DG-VV-03 | Đã đánh giá cùng `loai_nguoi_danh_gia` | "Bạn đã đánh giá vụ việc này rồi" | ERROR |
| ERR-DG-VV-04 | Không có quyền đánh giá (DN khác/đơn vị khác) | "Bạn không có quyền đánh giá vụ việc này (DN khác/đơn vị khác)" | ERROR |
| ERR-VV-BS-01 | Trạng thái ≠ YEU_CAU_BO_SUNG | "Hồ sơ không ở trạng thái yêu cầu bổ sung" | ERROR |
| ERR-VV-BS-02 | File vi phạm constraint (UC NEW-02) | "File không hợp lệ. Chấp nhận PDF/DOC/DOCX/XLS/XLSX/JPG/PNG, max 20MB/file, tổng 100MB, max 10 file" | ERROR |
| ERR-VV-BS-03 | Quá hạn bổ sung (BR-EC-16) | "Đã quá thời hạn bổ sung hồ sơ ({cau_hinh_sla.bo_sung_timeout} ngày làm việc theo cấu hình nội bộ)" | ERROR |
| ERR-VV-BS-04 | DN không phải chủ sở hữu VV | "Bạn không có quyền bổ sung hồ sơ vụ việc này" | ERROR |
| ERR-CK-VV-01 | VV không ở DA_DUYET/HOAN_THANH | "Vụ việc phải ở trạng thái Đã duyệt hoặc Hoàn thành mới có thể công khai" | ERROR |
| ERR-CK-VV-02 | CB PD khác cấp | "Bạn không có quyền công khai vụ việc thuộc đơn vị khác cấp" | ERROR |
| ERR-CK-VV-03 | `mo_ta_cong_khai` chứa HTML ngoài whitelist | "Mô tả công khai chứa định dạng không cho phép" | ERROR |
| ERR-CK-VV-04 | Ảnh đại diện > 5MB / sai định dạng | "Ảnh đại diện không vượt 5MB và chỉ chấp nhận jpg/png/gif" | ERROR |
| ERR-CK-VV-05 | File đính kèm vượt limit / virus | "Tệp '{name}' [vượt dung lượng / sai định dạng / chứa mã độc], đã bị từ chối" | ERROR |
| ERR-CK-VV-07 | API Cổng PLQG timeout/5xx | "Cổng Pháp luật Quốc gia tạm thời không phản hồi. Vụ việc giữ ở trạng thái cũ. Vui lòng thử lại sau ít phút" | ERROR |
| ERR-CK-VV-08 | API Cổng PLQG trả 4xx | "Cổng Pháp luật Quốc gia từ chối yêu cầu: {api_message}" | ERROR |
| ERR-CK-VV-09 | Hủy khi `cong_khai=0` | "Vụ việc chưa được công khai, không thể hủy công khai" | ERROR |
| ERR-CK-VV-10 | `ly_do_huy` < 20 ký tự | "Lý do hủy công khai phải tối thiểu 20 ký tự" | ERROR |
| INF-VV-01 | Không có kết quả tìm kiếm | "Không tìm thấy hồ sơ phù hợp" | INFO |

> ⚠️ Message phải quote **nguyên văn** từ SRS. Khi test negative, expected message match exact — KHÔNG được "close enough" accept.

### 2.3 Permission Matrix (module-specific)

> Reference đầy đủ: [`output/permission-matrix.md`](../../../output/permission-matrix.md) (49 entity × 11 role).

Permission chính cho 4 entity owned mới + VU_VIEC:

| Entity / Action | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | DN | NHT | TVV | CG |
|-----------------|:----:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--:|:---:|:---:|:--:|
| **VU_VIEC** danh sách (R) | All | TW scope | BN scope | DP scope | TW scope | BN scope | DP scope | own DN | own assign | own assign | own assign |
| **VU_VIEC** tạo thủ công UC54 (C) | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **VU_VIEC** DN gửi UC52 (C) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ (Tier 2 VNeID) | ❌ | ❌ | ❌ |
| **VU_VIEC** kiểm tra UC56 (U) | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **VU_VIEC** phân công UC59 (U) | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **VU_VIEC** trình PD UC61 (U) | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **VU_VIEC** phê duyệt UC63 (U) | ❌ | ❌ | ❌ | ❌ | ✅ same level | ✅ same level | ✅ same level | ❌ | ❌ | ❌ | ❌ |
| **VU_VIEC** đóng HS UC66 (U) | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **VU_VIEC** mở lại từ TU_CHOI | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **VU_VIEC** xóa (BR-DATA-01) | ✅ all | TW scope | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **VU_VIEC** công khai/hủy (FR-V.I-NEW-05) | ❌ | ❌ | ❌ | ❌ | ✅ same level | ✅ same level | ✅ same level | ❌ | ❌ | ❌ | ❌ |
| **PHAN_CONG_VU_VIEC** xác nhận/từ chối UC60 (U) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ self | ✅ self | ✅ self |
| **KET_QUA_VU_VIEC** cập nhật UC65 (CU) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ self | ✅ self | ✅ self |
| **DANH_GIA_VU_VIEC** chấm UC67 (C) | ❌ | ✅ scope | ✅ scope | ✅ scope | ❌ (CSV UC67 exclude) | ❌ | ❌ | ✅ own DN | ❌ | ❌ | ❌ |
| **LICH_SU_VU_VIEC** xem (R) | ✅ all | TW scope | BN scope | DP scope | TW scope | BN scope | DP scope | own DN | own assign | own assign | own assign |
| **HO_SO_VU_VIEC** bổ sung UC NEW-02 (C) | ❌ | ✅ (CB NV thay DN) | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ own VV (Tier 2 VNeID) | ❌ | ❌ | ❌ |
| **CAU_HINH_QUY_TRINH** CRUD UC NEW-01 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

> **Note:**
> - CB_PD KHÔNG chấm DANH_GIA_VU_VIEC (CSV UC67 ENUM chỉ {CB_NV, DN} — `srs-update-2026-5-5/srs-fr-05-vu-viec.md:1177, 2151`).
> - **QTHT KHÔNG chấm UC67** — không nằm trong CSV `{CB_NV, DN}` (`srs-update-2026-5-5/srs-fr-05-vu-viec.md:1177`). Tester P0 không nhầm QTHT có quyền chấm.
> - Công khai/hủy công khai là quyền **chỉ CB PD cùng cấp** — đặc thù FR-V.I-NEW-05 (`srs-update-2026-5-5/srs-fr-05-vu-viec.md:1364, 1373`).
> - **"All" vs "TW scope"** — QTHT="All" nghĩa thấy toàn quốc **KHÔNG filter `don_vi_id`** (BR-AUTH-08 exception line 2393). CB_NV_TW="TW scope" thấy toàn quốc nhưng vẫn có thể filter theo `don_vi_id` để truy vấn từng đơn vị (UC58). 2 phạm vi khác nhau khi test cross-unit isolation — TC-PERM-09..12 cần verify rõ.

### 2.3.1 Mapping cross-cutting TC-ID → file structure

> ⚠️ §2.1 cite ~62 cross-cutting TC-ID nhưng §3 chỉ list 23 file. Bảng này map mỗi TC-ID → file viết detail TC.

| TC-ID prefix | Số lượng | File chứa | Lý do |
|---|---:|---|---|
| TC-AUTH-01..05 | 5 | `22-TC-perm-cross-unit.md` (gộp auth scope) hoặc `23-TC-perm-role.md` (role-based auth) | Auth Tier 1 vs Tier 2 thuộc permission cross-cutting |
| TC-PERM-01..12 | 12 | `22-TC-perm-cross-unit.md` (PERM-01..08 cross-unit/cap) + `23-TC-perm-role.md` (PERM-09..12 data isolation) | Tách scope (cross-unit) vs role-based |
| TC-SLA-01..06 | 6 | `21-TC-sla-cross.md` | Scheduled job + 4 mức cảnh báo BR-SLA-02 |
| TC-NOTIF-01..06 | 6 | `12-TC-thong-bao.md` (CB) + `14-TC-dn-thong-bao.md` (DN) — split 3+3 | Notif theo channel CB vs DN |
| TC-AUDIT-01..04 | 4 | `07-TC-chi-tiet.md` (Timeline + LICH_SU 18 hành động) | Audit hiển thị qua Timeline SCR-V.I-03 |
| TC-DATA-01..02 | 2 | `04-TC-nhap-tay.md` (don_vi_id NOT NULL + 7 cột common khi tạo VV) | Verify entity field invariant |
| TC-DELETE-01..02 | 2 | `25-TC-data-migration.md` (BLOCKED SC-01) hoặc `23-TC-perm-role.md` (verify QTHT/TW xóa) | Xóa = hard hay soft (chờ SC-01) |
| TC-EXPORT-01..02 | 2 | `01-TC-list-filter.md` (toolbar [Xuất Excel] line 1663) | Export là tính năng SCR-V.I-01 |
| TC-PAGE-01 | 1 | `01-TC-list-filter.md` (pagination 20/page line 1684) | Pagination SCR-V.I-01 |
| TC-CONFLICT-01 | 1 | `07-TC-chi-tiet.md` (modal optimistic lock line 1623) | Optimistic lock trigger ở chi tiết |
| TC-CK-01..05 | 5 | `20-TC-cong-khai.md` | Công khai toàn bộ |
| TC-YCBS-01..03 | 3 | `06-TC-kiem-tra.md` (counter + highlight n≥2 + auto TU_CHOI lần 3) | BR-EC-15 thuộc UC56 kiểm tra |
| TC-EVAL-04 | 1 | `17-TC-danh-gia.md` (thang 0-10 VV ≠ thang 1-5 TVV BR-CALC-06) | Thuộc UC67 đánh giá |
| TC-LOCK-01..03 | 3 | `07-TC-chi-tiet.md` (BR-FLOW-03 lock đã duyệt + QTHT force-edit + audit `is_force_edit`) | Lock thuộc chi tiết |
| TC-NEW02-04 | 1 | `19-TC-dn-bo-sung.md` (BR-EC-16 quá hạn auto reject) | Thuộc UC NEW-02 |
| TC-SEARCH-01..02 | 2 | `01-TC-list-filter.md` (SQL/XSS injection + 200 char limit BR-EC-13) | Search thuộc filter SCR-V.I-01 |
| TC-KT-01..04 | 4 | `06-TC-kiem-tra.md` (6 hạng mục UC106 + checklist versioning SC-04) | Thuộc UC56 |
| TC-PC-01..05 | 5 | `09-TC-phan-cong.md` (BR-CALC-04 priority + ly_do_uu_tien + NĐ77-19 label) | Thuộc UC59 |
| TC-PD-01..04 | 4 | `13-TC-phe-duyet.md` | Thuộc UC63 |
| TC-NHT-01..03 | 3 | `10-TC-xac-nhan.md` (BR-AUTH-10 lọc kép, BLOCKED SC-02) | Thuộc UC60 |
| TC-CREATE-01 | 1 | `04-TC-nhap-tay.md` (BR-DATA-04 mã VV-{TINH}-YYYYMMDD-SEQ) | Tạo VV nhập tay |
| TC-PLACEHOLDER-01..03 | 3 | `21-TC-sla-cross.md` (T15 auto-return) + `25-TC-data-migration.md` (T21 mở lại) + `06-TC-kiem-tra.md` (T12 auto 3 lần) **BLOCKED chờ SC-03** | 3 transition không có FR formal |

> Tổng cross-cutting **~72 TC** đã map vào 23 file gốc — không cần thêm file mới. Tester R1 đọc bảng này biết viết detail TC vào file nào.

### 2.4 UI Layout (SCR-V.I-01 / -02 / -03 / -04 / -05)

> ⚠️ **CẢNH BÁO:** Đây là visual spec components từ SRS SCR-V.I-XX. **KHÔNG dùng absence để khẳng định module KHÔNG có X.** Mọi feature không có trên UI phải đối chiếu §2.1 BR table + SRS Phụ lục B trước.

#### SCR-V.I-01 — Danh sách Hồ sơ (CB CMS)

- **Breadcrumb:** "Trang chủ > Vụ việc > Danh sách hồ sơ" (line 1662)
- **Toolbar:** Tiêu đề "Quản lý Vụ việc HTPL" + [+ Thêm mới] + [+ Nhập thủ công] + [Xuất Excel] + [Làm mới] (line 1663)
- **6 tab trạng thái** với số đếm realtime: Tất cả / Chờ tiếp nhận / Đang xử lý (DA_TIEP_NHAN → DANG_XU_LY) / Chờ PD / Hoàn thành (DA_DUYET + HOAN_THANH + DA_DANH_GIA) / Từ chối (line 1664)
- **Filter-bar:** Tìm kiếm (mã/tên DN) / Lĩnh vực PL / Trạng thái / Kênh tiếp nhận / Mức SLA / Khoảng ngày + [Tìm] + [Xóa bộ lọc] (line 1665-1671)
- **Table 11 cột:** Checkbox / Mã VV / Tên DN / Lĩnh vực / Kênh / **Trạng thái badge (12 màu)** / **Người xử lý / Tổ chức** (đổi label v3.5) / Ngày tiếp nhận / Deadline / **Cảnh báo SLA 4 mức màu** / Hành động (line 1672-1682)
- **Action hàng loạt:** [Trình PD hàng loạt] + [Xóa hàng loạt] — chỉ áp dụng VV ở DANG_XU_LY cho batch PD (line 1683)
- **Pagination:** "Hiển thị 1-20 / N kết quả" (line 1684)

#### SCR-V.I-02 — Thêm/Nhập thủ công (CB CMS)

- **4 accordion** (line 1707-1739):
  1. **Thông tin DN** — [Tìm DN] modal lookup MST + 13 trường (ten_doanh_nghiep / ma_so_thue / dia_chi / tinh_thanh / loai_dn / quy_mo / nganh_nghe / so_lao_dong / doanh_thu_nam / nguoi_dai_dien / chuc_vu_dd / email / SDT) + **3 trường BR-CALC-04 (la_nu_lam_chu / so_lao_dong_nu / so_lao_dong_khuyet_tat)**
  2. **Nội dung Yêu cầu** — tieu_de + noi_dung_yeu_cau Rich Text 10k ký tự + linh_vuc_id + loai_hinh_ht_id + vu_viec_vuong_mac + ghi_chu
  3. **Tài liệu Đính kèm** — kéo thả + ClamAV scan, max 20MB/file
  4. **Thông tin Tiếp nhận** — kenh_tiep_nhan (default TRUC_TIEP) + ngay_tiep_nhan + nguoi_tiep_nhan auto-fill + ma_ho_so_dvc (khi DVC) + he_thong_nguon (khi HE_THONG_KHAC)
- **Action bar fixed:** [Hủy] / [Lưu nháp] (→ MOI_TAO) / [Lưu & Gửi duyệt] (→ CHO_TIEP_NHAN). UC54 nhập tay → trang_thai = DA_TIEP_NHAN bỏ qua 2 state đầu (line 1743)

#### SCR-V.I-03 — Chi tiết (CB + DN 2 chế độ)

- **Stepper 10 bước** + **2 badge phụ** "Yêu cầu bổ sung" (kèm "Lần bổ sung: {n}/3") + "Từ chối" — line 1761
- **Header:** Mã VV + tiêu đề + **3 badge** (Trạng thái + SLA + **"Đã công khai"** khi `cong_khai=1`) — line 1760
- **8 accordion:** Thông tin DN (read-only + link FR-07) / Nội dung yêu cầu / Tài liệu đính kèm / **Kết quả Kiểm tra (6 hạng mục UC106 + counter YCBS n/3 highlight đỏ n≥2)** / **Phân công xử lý (2 thẻ Cá nhân/Tổ chức + label "đơn vị quản lý")** / Kết quả Hỗ trợ / Phê duyệt / **Đánh giá (3 tiêu chí 0-10, UNIQUE per loại)** — line 1762-1769
- **Timeline sidebar:** lịch sử LICH_SU_VU_VIEC theo `dd/mm HH:mm — {ho_ten} {hanh_dong}` — line 1770
- **Action bar context-sensitive 13 row** theo trạng thái + vai trò — line 1775-1789, bao gồm:
  - DANG_KIEM_TRA → [Hoàn tất Kiểm tra] (3 nhánh DAT/YCBS/KHONG_DAT)
  - DA_PHAN_CONG → [Phân công] modal **2 thẻ**: Cá nhân (TVV/CG/NHT) hoặc Tổ chức (Cty Luật/VP LS/TT TVPL)
  - DA_PHAN_CONG → [Chấp nhận] / [Từ chối] (NHT/TVV/CG)
  - CHO_PHE_DUYET → [Phê duyệt] / [Từ chối] (CB PD) — **Từ chối → DANG_XU_LY** (line 1784), không TU_CHOI
  - DA_DUYET / HOAN_THANH (cong_khai=0) → **[Công khai]** (CB PD cùng cấp)
  - DA_DUYET / HOAN_THANH (cong_khai=1) → **[Hủy công khai]** (modal lý do ≥20 ký tự)
- **Quy ước hiển thị nút (line 1793-1795):** sai vai trò → ẩn; vai trò đúng nhưng trạng thái không khớp → mờ + tooltip giải thích.

#### SCR-V.I-04 — Danh sách VV của tôi (DN, mobile-first)

- **3 tab DN:** Tất cả / Đang xử lý / Đã kết thúc (line 1865) — KHÁC 6 tab CB.
- **Cột:** Mã VV / Tiêu đề / Lĩnh vực / Trạng thái / **Đơn vị xử lý** (tên đơn vị Sở TP/Bộ, KHÔNG tên cá nhân — NĐ 13/2023, line 1873) / Ngày tiếp nhận / **Công khai badge** / Hành động.
- **Bảo mật cán bộ:** không hiển thị cá nhân CB (line 1884).
- **Responsive:** mobile-first, table → card khi <768px (line 1885).

#### SCR-V.I-05 — Thông báo của tôi (DN, polling 30s)

- **Filter:** Trạng thái đọc (3) / Loại thông báo (6) / Khoảng ngày (line 1903-1905).
- **Card list:** icon loại + tiêu đề + trích 150 ký tự + thời gian + badge "Mới" (line 1906).
- **Polling 30s** mặc định (line 1915).

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**
- ☑ Nút [Xuất Excel] toolbar SCR-V.I-01 (BR-DATA-06) — đã quote line 1663
- ☑ Pagination 20/page default SCR-V.I-01, SCR-V.I-04, SCR-V.I-05 (BR-DATA-07) — line 1684, 1877, 1907
- ☑ Search sanitize max 200 chars (BR-EC-13) — toolbar line 1665
- ☑ URL sync filter (BR-UX-01) — tab + filter-bar SCR-V.I-01
- ☑ Audit log mọi CUD (BR-DATA-05) — entity LICH_SU_VU_VIEC + 18 hành động
- ☑ Optimistic lock mọi UPDATE/DELETE (BR-EC-01) — line 1623 modal + line 2340 "optimistic locking"
- ☑ Badge "Đã công khai" + tooltip thời gian đăng tải (CR-01) — line 1760, 1835

**Feature module KHÔNG có (cần QUOTE SRS line):**
- Tab "DA_XOA" — bỏ theo C1 cross-cutting v3.5 hard-delete (`01-tong-quan-nghiep-vu.md` §6.3 (1) line 229). Nếu UI render tab DA_XOA → bug.
- Cột "Địa bàn TVV" — bỏ theo NĐ 77/2008 Đ.19, đổi thành "Đơn vị quản lý" (line 751, 1766, 2208).
- Trường `nguoi_ho_tro_id` cũ — bỏ theo Thay đổi 8, thay 3 cột phân công mới (`_DELTA-MAP-FR05.md` line 29).
- Heading nhóm h1/h2 trong table bug-report — feedback rule `feedback_bug_report_ordering`.

### 2.5 State Machine (SM-VUVIEC) — FULL 12 state + 18+ transition

#### Bảng trạng thái

| # | Trạng thái | Mã | Mô tả | Màu badge |
|---|-----------|-----|-------|-----------|
| 1 | Mới tạo | `MOI_TAO` | HT tự tạo từ DVC/HT khác (thoáng qua) | Xám nhạt |
| 2 | Chờ tiếp nhận | `CHO_TIEP_NHAN` | VV chờ CB NV tiếp nhận | Xanh dương |
| 3 | Đã tiếp nhận | `DA_TIEP_NHAN` | CB NV đã tiếp nhận, chưa kiểm tra | Xanh lá |
| 4 | Đang kiểm tra | `DANG_KIEM_TRA` | CB NV đối chiếu checklist UC106 | Vàng |
| 5 | Yêu cầu bổ sung | `YEU_CAU_BO_SUNG` | Hồ sơ thiếu, chờ DN bổ sung (BR-EC-15 ≤3 lần) | Cam |
| 6 | Từ chối | `TU_CHOI` | Hồ sơ không đạt / quá hạn bổ sung (BR-EC-16) | Đỏ |
| 7 | Đã phân công | `DA_PHAN_CONG` | Đã phân công CA_NHAN hoặc TO_CHUC, chờ xác nhận | Xanh dương đậm |
| 8 | Đang xử lý | `DANG_XU_LY` | TVV/CG/NHT đang tư vấn | Vàng đậm |
| 9 | Chờ phê duyệt | `CHO_PHE_DUYET` | CB NV trình KQ, chờ CB PD duyệt cùng cấp (BR-AUTH-05) | Cam đậm |
| 10 | Đã duyệt | `DA_DUYET` | CB PD đã phê duyệt | Xanh lá đậm |
| 11 | Hoàn thành | `HOAN_THANH` | CB NV đóng hồ sơ | Xám |
| 12 | Đã đánh giá | `DA_DANH_GIA` | UC67 chấm xong | Tím |

> **Overlay flag CONG_KHAI:** Không phải state riêng — `VU_VIEC.cong_khai ∈ {0,1}` overlay trên DA_DUYET / HOAN_THANH (`srs-update-2026-5-5/srs-fr-05-vu-viec.md:2295`).

#### Bảng chuyển trạng thái (18 transition + 3 self-loop)

| # | Từ | Đến | Trigger | Guard | Action | FR Ref | BR Ref |
|---|----|-----|---------|-------|--------|--------|--------|
| T01 | [*] | `MOI_TAO` | HT tự tạo từ DVC/HT khác | — | Sinh mã VV-{TINH}-YYYYMMDD-SEQ | FR-V.I-03/04/05 | BR-DATA-04 |
| T02 | `MOI_TAO` | `CHO_TIEP_NHAN` | Auto hoặc CB NV xử lý | — | Tính deadline 15 ngày LV | FR-V.I-03/04/05 | BR-SLA-01 |
| T03 | [*] | `CHO_TIEP_NHAN` | DVC / HT khác / Trực tiếp | — | Sinh mã, tính deadline, TB CB NV | FR-V.I-03/04/05 | BR-SLA-01, BR-NOTIF-01 |
| T04 | [*] | `DA_TIEP_NHAN` | **CB NV nhập tay UC54** (kênh TRUC_TIEP/BUU_CHINH/DIEN_THOAI) | CB NV có quyền | Bỏ qua 2 state đầu | FR-V.I-04 | BR-SLA-01 |
| T05 | `CHO_TIEP_NHAN` | `DA_TIEP_NHAN` | CB NV [Tiếp nhận] | CB NV cùng đơn vị | Audit, TB DN (nếu DVC) | FR-V.I-01 | BR-AUTH-03/04 |
| T06 | `DA_TIEP_NHAN` | `DANG_KIEM_TRA` | CB NV [Bắt đầu kiểm tra] | — | Mở checklist UC106 | FR-V.I-06 | BR-LEGAL-02 |
| T07 | `DANG_KIEM_TRA` | `DA_PHAN_CONG` | CB NV kết luận Đạt + phân công | Modal 2 thẻ — Cá nhân/Tổ chức HOAT_DONG; constraint TVV ∈ TC TV nếu loại='TO_CHUC' | Gửi TB cá nhân được phân công (+ CC email TC nếu TO_CHUC) | FR-V.I-06, FR-V.I-09 | BR-CALC-04, BR-NOTIF-01, BR-NĐ77-19 |
| T08 | `DANG_KIEM_TRA` | `YEU_CAU_BO_SUNG` | CB NV kết luận thiếu HS | `bo_sung_count < 3` | Set `ngay_yeu_cau_bo_sung=NOW()`, counter++, TB DN | FR-V.I-06, FR-V.I-NEW-02 | BR-EC-15, BR-EC-16 |
| T09 | `DANG_KIEM_TRA` | `TU_CHOI` | CB NV kết luận Không đạt | — | TB DN kết quả, ghi audit | FR-V.I-06, FR-V.I-12 | BR-FLOW-04 |
| T10 | `YEU_CAU_BO_SUNG` | `DANG_KIEM_TRA` | **DN bổ sung HS (auth Tier 2 VNeID)** | DN là chủ sở hữu VV (`doanh_nghiep_id` match session), file constraint OK, chưa quá hạn `bo_sung_timeout` | Lưu file HO_SO_VU_VIEC, TB CB NV, audit `BO_SUNG_HS` | **FR-V.I-NEW-02** | BR-EC-16, BR-NOTIF-01, BR-DATA-05 |
| T11 | `YEU_CAU_BO_SUNG` | `TU_CHOI` | **Auto job** quá hạn bổ sung | `NOW() - ngay_yeu_cau_bo_sung > cau_hinh_sla.bo_sung_timeout` | TB DN, audit `TU_CHOI_AUTO_QUA_HAN` | FR-V.I-CROSS-01 | BR-EC-16 |
| T12 | `DANG_KIEM_TRA` (lần 3 + KHONG_DAT) | `TU_CHOI` | **Auto** quá 3 lần YCBS | `bo_sung_count >= 3 AND ket_luan='KHONG_DAT'` | TB DN, audit `TU_CHOI_AUTO_QUA_HAN`, lý do "Đã bổ sung 3 lần không đạt" | FR-V.I-06 | BR-EC-15 |
| T13 | `DA_PHAN_CONG` | `DANG_XU_LY` | NHT/TVV/CG [Chấp nhận] | PHAN_CONG_VU_VIEC.trang_thai='CHO_XAC_NHAN'; người đăng nhập = nguoi_xu_ly_id | Update PCVV trang_thai='CHAP_NHAN', ngay_xac_nhan=NOW(), audit | FR-V.I-10 | — |
| T14 | `DA_PHAN_CONG` | `DA_TIEP_NHAN` | NHT/TVV/CG [Từ chối] | Có lý do | Update PCVV trang_thai='TU_CHOI', ly_do_tu_choi; quay lại chọn người khác | FR-V.I-10 | BR-FLOW-04 |
| T15 | `DA_PHAN_CONG` | `DA_TIEP_NHAN` | **Auto job** NHT không phản hồi > 3 ngày LV | elapsed > `cau_hinh_sla.xac_nhan_timeout` | TB CB NV, audit | (placeholder dev impl theo UI v3) | — |
| T16 | `DANG_XU_LY` | `CHO_PHE_DUYET` | CB NV [Trình duyệt] | Cá nhân được phân công đã cập nhật KQ (KET_QUA_VU_VIEC tồn tại) | TB CB PD cùng cấp | FR-V.I-11 | BR-AUTH-05, BR-NOTIF-01 |
| T17 | `CHO_PHE_DUYET` | `DA_DUYET` | CB PD [Duyệt] | Cùng cấp (`don_vi_id` match) | Set `nguoi_phe_duyet_id`, `ngay_phe_duyet`, audit | FR-V.I-13 | BR-AUTH-05 |
| T18 | `CHO_PHE_DUYET` | `DANG_XU_LY` | **CB PD [Từ chối]** (v3.5 — KHÔNG còn → TU_CHOI) | `ly_do ≥ 10 ký tự` | TB CB NV + NHT, audit `TU_CHOI_PD` ghi ly_do | **FR-V.I-13** (v3.5) | **BR-FLOW-04** |
| T19 | `DA_DUYET` | `HOAN_THANH` | CB NV [Đóng hồ sơ] | — | Set `ngay_hoan_thanh=NOW()`, TB DN | FR-V.I-16 | BR-NOTIF-01 |
| T20 | `HOAN_THANH` | `DA_DANH_GIA` | CB NV hoặc DN chấm UC67 (CSV exclude CB_PD) | `loai_nguoi_danh_gia` UNIQUE per (`vu_viec_id`, `loai_nguoi_danh_gia`); 3 điểm 0-10 | Tạo DANH_GIA_VU_VIEC, audit (chỉ flip state lần đầu) | FR-V.I-17 | — |
| T21 | `TU_CHOI` | `DA_TIEP_NHAN` | QTHT/CB NV [Mở lại HS] | Admin override + lý do | Audit `MO_LAI` | (placeholder FR-V.I-xx, dev impl UI v3) | — |
| **SL1** | `DA_DUYET` ↻ | `DA_DUYET` (cong_khai 0→1) | CB PD [Công khai] + API Cổng PLQG OK | CB PD cùng cấp; mo_ta_cong_khai ≤2000; whitelist 9 fields | SET cong_khai=1, thoi_gian_dang_tai=NOW(), TB DN, audit `CONG_KHAI` | **FR-V.I-NEW-05** | BR-PUBLIC-01, BR-PUBLIC-04, BR-EC-20 |
| **SL2** | `HOAN_THANH` ↻ | `HOAN_THANH` (cong_khai 0→1) | Tương tự SL1 | Tương tự | Tương tự | FR-V.I-NEW-05 | BR-PUBLIC-01 |
| **SL3** | `DA_DUYET`/`HOAN_THANH` (cong_khai 1→0) | (giữ state) | CB PD [Hủy công khai] + API OK | `cong_khai=1`; `ly_do_huy ≥ 20 ký tự` | SET cong_khai=0, clear 4 cột công khai, TB DN, audit `HUY_CONG_KHAI` | FR-V.I-NEW-05 | BR-FLOW-04 |

**Lưu ý SM-VUVIEC:**
- Tối đa **3 lần bổ sung** (BR-EC-15). Sau lần 3 + KHONG_DAT → auto TU_CHOI.
- Quá hạn bổ sung (mặc định 5 ngày LV — UC108 cấu hình) → auto TU_CHOI (BR-EC-16).
- CB PD từ chối → quay về **DANG_XU_LY** (v3.5 fix — KHÔNG đóng VV như v3).
- Mọi transition dùng **optimistic locking** (BR-EC-01).
- `cong_khai` là **cờ overlay**, không phải state — giữ trạng thái chính DA_DUYET/HOAN_THANH.
- Hard-delete: bỏ DA_XOA toàn dự án (C1 cross-cutting v3.5).

### 2.6 Data dependencies & Seed / Workflow input (v3.0)

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| **GĐ 1 Seed (pure entry state)** | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | `vu_viec_variants[1..6]` + `phan_cong_vu_viec_variants[1..6]` + `danh_gia_vu_viec_variants[1..6]` |
| **GĐ 1 click flow** | [`input/quy-trinh-nghiep-vu/flow-module.md`](../../../input/quy-trinh-nghiep-vu/flow-module.md) | §3 SM-VUVIEC bước 1 nhập tay UC54 |
| **GĐ 2 Workflow** | [`input/quy-trinh-nghiep-vu/flow-module.md`](../../../input/quy-trinh-nghiep-vu/flow-module.md) + [`02-thu-tu-module.md` §⑥ FR-05](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) | Bảng flow 18 transition + Phụ lục 2 preset (cần TVV/CG/NHT/DN ≥3 mỗi role) + Phụ lục 3 troubleshooting |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | VU_VIEC tạo tại SCR-V.I-02 (UC54) hoặc DN qua SCR-V.I-04; đọc tại FR-06/FR-08/FR-11/FR-14 |

**Upstream dependencies (Tier check):**

| Entity của module | Tier | Phụ thuộc entity nào (upstream) | Seed trước tại module |
|-------------------|:----:|----------------------------------|-----------------------|
| VU_VIEC | 3 (LỚP GIAO DỊCH LÕI) | DOANH_NGHIEP (FR-07 — đủ field BR-CALC-04) + TU_VAN_VIEN+CG (FR-04, state HOAT_DONG) + NGUOI_HO_TRO (FR-04, state HOAT_DONG) + TO_CHUC_TU_VAN (FR-04, state HOAT_DONG) + DANH_MUC linh_vuc_id + loai_hinh_ht_id (FR-10) + CAU_HINH_SLA bo_sung_timeout (FR-10) | FR-10 → FR-07 → FR-04 → FR-05 |
| PHAN_CONG_VU_VIEC | 3 | VU_VIEC (state DANG_KIEM_TRA đạt) + TAI_KHOAN (HOAT_DONG) + TO_CHUC_TU_VAN (HOAT_DONG nếu loại TO_CHUC) | FR-05 (sau khi VV qua kiểm tra) |
| DANH_GIA_VU_VIEC | 3 | VU_VIEC (state HOAN_THANH/DA_DANH_GIA) | FR-05 (sau khi VV đóng HS) |
| LICH_SU_VU_VIEC | 3 | VU_VIEC (mọi event) | Auto-write theo BR-DATA-05 |

> **Lưu ý:** KHÔNG hardcode "N records, states X/Y" ở đây. Acceptance theo filter — verify per query downstream (`?loaiTvv=CG`, `?loaiTvv=TVV`, `?loaiDoiTuongXuLy=CA_NHAN`, `?loaiDoiTuongXuLy=TO_CHUC`, `?trang_thai=HOAT_DONG`). Chi tiết seed split combinatorial: rule [`feedback_seed_acceptance_strict_split`](../../../tasks/lessons-learned.md) + CLAUDE.md "Quy tắc seed task" line ~30.

---

## 3. Cấu Trúc File Test Case

```
fr-05-vu-viec/
├── test-plan.md                        ← File này
├── 01-TC-list-filter.md                ← FR-V.I-01 + 08 — Danh sách + filter + tab + search + export
├── 02-TC-dn-gui-hs.md                  ← FR-V.I-02 — DN gửi HS chuyên trang (auth Tier 2)
├── 03-TC-dvc-inbound.md                ← FR-V.I-03 — LGSP inbound + idempotent + retry
├── 04-TC-nhap-tay.md                   ← FR-V.I-04 — UC54 form 4 accordion + BR-CALC-04
├── 05-TC-htk-inbound.md                ← FR-V.I-05 — HT khác inbound + 13 edge case EC-V.I-05-01..13
├── 06-TC-kiem-tra.md                   ← FR-V.I-06 — UC56 checklist 6 hạng mục + BR-EC-15 (3 lần)
├── 07-TC-chi-tiet.md                   ← FR-V.I-07 — Stepper + 8 accordion + Timeline
├── 09-TC-phan-cong.md                  ← FR-V.I-09 — UC59 modal 2 thẻ + BR-CALC-04 + 6 mã lỗi PC
├── 10-TC-xac-nhan.md                   ← FR-V.I-10 — UC60 NHT/TVV/CG chấp nhận/từ chối
├── 11-TC-trinh-pd.md                   ← FR-V.I-11 — UC61 AT-03 auto-transition
├── 12-TC-thong-bao.md                  ← FR-V.I-12 — UC62 in-app + email + LGSP outbound
├── 13-TC-phe-duyet.md                  ← FR-V.I-13 — UC63 từ chối → DANG_XU_LY (KHÔNG TU_CHOI) + batch PD
├── 14-TC-dn-thong-bao.md               ← FR-V.I-14 — UC64 DN thông báo + polling 30s
├── 15-TC-cap-nhat-kq.md                ← FR-V.I-15 — UC65 NHT cập nhật KQ
├── 16-TC-dong-hs.md                    ← FR-V.I-16 — UC66 đóng HS → HOAN_THANH
├── 17-TC-danh-gia.md                   ← FR-V.I-17 — UC67 thang 0-10 + UNIQUE per loại + CSV exclude CB_PD
├── 18-TC-cau-hinh-quy-trinh.md         ← FR-V.I-NEW-01 — QTHT cấu hình + versioning
├── 19-TC-dn-bo-sung.md                 ← FR-V.I-NEW-02 — DN bổ sung HS + BR-EC-16 quá hạn + 4 mã lỗi BS
├── 20-TC-cong-khai.md                  ← FR-V.I-NEW-05 — Công khai/hủy + BR-PUBLIC-01/04 + 9 mã lỗi CK
├── 21-TC-sla-cross.md                  ← FR-V.I-CROSS-01 — Scheduled job 30 phút + 4 mức cảnh báo
├── 22-TC-perm-cross-unit.md            ← Permission BR-AUTH-03/04/08 — TW/BN/ĐP isolation
├── 23-TC-perm-role.md                  ← Permission matrix 11 role × actions
├── 24-TC-dn-scr04-05.md                ← SCR-V.I-04/05 chế độ DN (mobile + bảo mật cán bộ NĐ 13/2023)
├── 25-TC-data-migration.md             ← Edge: VV cũ có `nguoi_ho_tro_id` migrate sang `nguoi_xu_ly_id`
└── (26-REVIEW-edge-case-hunter.md)     ← Optional: review từ bmad-review-edge-case-hunter
```

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Tổng |
|------|------:|---------:|-----:|-----:|
| 01-TC-list-filter | 2 | 3 | 2 | 7 |
| 02-TC-dn-gui-hs | 1 | 4 | 1 | 6 |
| 03-TC-dvc-inbound | 1 | 3 | 1 | 5 |
| 04-TC-nhap-tay | 1 | 4 | 2 | 7 |
| 05-TC-htk-inbound | 1 | 2 | 3 | 6 |
| 06-TC-kiem-tra | 2 | 3 | 2 | 7 |
| 07-TC-chi-tiet | 1 | 1 | 1 | 3 |
| 09-TC-phan-cong | 2 | 5 | 2 | 9 |
| 10-TC-xac-nhan | 1 | 2 | 1 | 4 |
| 11-TC-trinh-pd | 1 | 2 | 1 | 4 |
| 12-TC-thong-bao | 1 | 1 | 1 | 3 |
| 13-TC-phe-duyet | 2 | 3 | 2 | 7 |
| 14-TC-dn-thong-bao | 1 | 1 | 1 | 3 |
| 15-TC-cap-nhat-kq | 1 | 2 | 1 | 4 |
| 16-TC-dong-hs | 1 | 1 | 1 | 3 |
| 17-TC-danh-gia | 2 | 4 | 2 | 8 |
| 18-TC-cau-hinh-quy-trinh | 1 | 1 | 1 | 3 |
| 19-TC-dn-bo-sung | 1 | 4 | 2 | 7 |
| 20-TC-cong-khai | 2 | 5 | 3 | 10 |
| 21-TC-sla-cross | 1 | 1 | 2 | 4 |
| 22-TC-perm-cross-unit | 2 | 3 | 1 | 6 |
| 23-TC-perm-role | 2 | 3 | 1 | 6 |
| 24-TC-dn-scr04-05 | 2 | 2 | 1 | 5 |
| 25-TC-data-migration | 1 | 3 | 4 | **8** |
| **TỔNG** | **33** | **63** | **39** | **~135** (±10%) |

> ⚠️ Số TC là **ước lượng** — sẽ refine khi viết detail TC. Có thể phát sinh edge case mới (vd EC-V.I-05-01..13 inbound UC55 — `srs-update-2026-5-5:469-481`).

**TC25 detail bump (3 → 8 TC) — schema migration risk cao (`_DELTA-MAP-FR05.md` §6 Open issues):**

| TC25.X | Tên | Loại | Mô tả |
|---|---|:-:|---|
| TC25-H1 | Migration script chạy backfill `loai_doi_tuong_xu_ly + nguoi_xu_ly_id` từ `nguoi_ho_tro_id` cũ | Happy | Verify VV có `nguoi_ho_tro_id` cũ → script set `loai_doi_tuong_xu_ly='CA_NHAN'` + `nguoi_xu_ly_id = nguoi_ho_tro_id` + `to_chuc_tu_van_id=NULL`. Run migration script dry-run + commit, compare row count |
| TC25-N1 | VV cũ migrate hiển thị Accordion 5 SCR-V.I-03 | Negative | Verify FE đọc 3 cột mới (KHÔNG còn `nguoi_ho_tro_id`). VV pre-migration mở chi tiết → Accordion "Phân công xử lý" render đủ 2 thẻ + label "đơn vị quản lý" |
| TC25-N2 | Migration miss khi `nguoi_ho_tro_id NULL` (VV chưa phân công cũ) | Negative | Verify VV `nguoi_ho_tro_id=NULL` script SET cả 3 cột mới = NULL, KHÔNG default 'CA_NHAN'. Tránh FE render "Đã phân công" sai |
| TC25-N3 | FR-11 báo cáo đọc trường cũ vs mới | Negative | Verify report đọc `nguoi_xu_ly_id` mới (không break "Người xử lý" column). Cross-module impact FR-11 |
| TC25-E1 | Audit log LICH_SU_VU_VIEC cho migration event | Edge | Verify mỗi VV migrated có 1 row LICH_SU `hanh_dong='MIGRATION_NGUOI_HO_TRO_TO_PHAN_CONG'` + `created_by='SYSTEM'` + `chi_tiet` JSON ghi old/new value |
| TC25-E2 | Rollback migration | Edge | Verify nếu rollback script chạy được — restore `nguoi_ho_tro_id` từ audit log JSON |
| TC25-E3 | Idempotent — chạy migration 2 lần | Edge | Verify chạy lần 2 KHÔNG duplicate audit row + KHÔNG overwrite VV đã có 3 cột mới (skip nếu `loai_doi_tuong_xu_ly IS NOT NULL`) |
| TC25-E4 | Soft-delete vs hard-delete cho VV migrated | Edge | **BLOCKED chờ SC-01** — verify VV cũ DA_XOA pre-migration xử lý ra sao (hard purge hay giữ `is_deleted=1`) |

**Phân bổ priority:**

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc — core workflow + permission + công khai + DN bổ sung) | 78 | 60% |
| P1 (quan trọng — edge case 18 transition + error handling + audit) | 38 | 29% |
| P2 (nên có — UI/UX polish + responsive + tooltip + i18n) | 14 | 11% |

**Phân bổ theo loại bug có thể phát hiện:**
- **Workflow / SM transition:** TC 06/09/10/11/13/15/16/19/20 — P0 chủ lực (≥40 TC)
- **Permission isolation BR-AUTH-03/04/08:** TC 22/23 — P0 (12 TC)
- **Công khai BR-PUBLIC-01/04 + BR-EC-20:** TC 20 — P0 (10 TC, gồm mock API fail)
- **DN bổ sung BR-EC-16:** TC 19 — P0 (7 TC)
- **Schema migration `nguoi_ho_tro_id` → 3 cột mới:** TC 25 — P1 (3 TC edge cao rủi ro)
- **SLA + scheduled job:** TC 21 — P1 (4 TC, cần mock time)

---

## 5. Tiêu chí đạt/không đạt

> Reference: [`output/test-strategy.md §10`](../../../output/test-strategy.md)

- ✅ **PASS:** 100% P0 + 90% P1 + 70% P2 pass; KHÔNG có Critical/Major bug Open ở các luồng core (T07 phân công, T17/T18 phê duyệt, SL1-3 công khai, T10 DN bổ sung).
- ❌ **FAIL:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%, hoặc bất kỳ Critical bug nào Open trên 4 entity owned mới (PHAN_CONG_VU_VIEC, DANH_GIA_VU_VIEC, LICH_SU_VU_VIEC) — vì entity mới = rủi ro schema migration cao.

**Test priority gate đặc thù FR-05 (core module):**
- Round 1 (Smoke + workflow happy path): ≥80% P0 PASS trước khi vào round 2.
- Round 2 (Negative + edge case): ≥90% P0 + ≥80% P1.
- Round 3 (Permission matrix + cross-module + công khai + DN bổ sung): 100% P0 + ≥90% P1.
- Round 4+ (re-verify bug fix): re-test toàn bộ bug đã đóng + smoke 30 phút workflow chính.

---

## 6. Tham chiếu

### SRS gốc + delta
- [`input/srs-v3/srs-fr-05-vu-viec.md`](../../../input/srs-v3/srs-fr-05-vu-viec.md) — v3.0 baseline (1891 dòng)
- [`input/srs-update-2026-5-5/srs-fr-05-vu-viec.md`](../../../input/srs-update-2026-5-5/srs-fr-05-vu-viec.md) — v3.5 (2527 dòng, +25%)
- [`input/srs-update-2026-5-5/_DELTA-MAP-FR05.md`](../../../input/srs-update-2026-5-5/_DELTA-MAP-FR05.md) — 14 thay đổi IN
- [`input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md`](../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) — line 177-345 (FR-05)
- [`input/srs-v3/srs-v3.md` Phụ lục B](../../../input/srs-v3/srs-v3.md) — BR cross-cutting (line 3939-4088)

### Quy trình nghiệp vụ
- [`input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md` §LUỒNG B](../../../input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md) — flow FR-05 → FR-14 → FR-06 → FR-08
- [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md` §⑥ FR-05](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — SM transition table + accordion SCR-V.I-03
- [`tasks/system-overview.md` §4.7 M6 Vụ việc](../../../tasks/system-overview.md) — 3 SCR overview
- [`input/quy-trinh-nghiep-vu/flow-module.md` §3 SM-VUVIEC](../../../input/quy-trinh-nghiep-vu/flow-module.md) — state machine + seed preset

### Test infra
- [`output/test-strategy.md`](../../../output/test-strategy.md) — chiến lược tổng thể
- [`output/scaling-test-strategy.md`](../../../output/scaling-test-strategy.md) — quy trình 7 bước onboard
- [`output/permission-matrix.md`](../../../output/permission-matrix.md) — 49 entity × 11 role
- [`output/template/test-case-template.md`](../../../output/template/test-case-template.md) — TC field-level
- [`output/template/test-case-execution-report-template.md`](../../../output/template/test-case-execution-report-template.md) — execution report
- [`output/template/bug-report-template.md`](../../../output/template/bug-report-template.md) — bug report 6 sections
- [`output/template/tc-block-classification-template.md`](../../../output/template/tc-block-classification-template.md) — 6 nhóm phân loại block A-F

### Seed + data
- [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) — 6 variant per entity
- [`input/data/entity-map.md`](../../../input/data/entity-map.md) — VU_VIEC "Tạo tại / Đọc tại"
- [`input/users.csv`](../../../input/users.csv) — 154 dòng tài khoản
- [`input/test-accounts-isolation.csv`](../../../input/test-accounts-isolation.csv) — permission test usage guide

### Pháp lý
- NĐ 55/2019/NĐ-CP — HTPL DNNVV (Điều 4 BR-CALC-04, Điều 7 NHT, Điều 8 K.1 SLA 15 ngày, Điều 9 mạng lưới TVV)
- NĐ 13/2023/NĐ-CP — Bảo vệ dữ liệu cá nhân (BR-PUBLIC-04, ẩn cán bộ SCR-V.I-04)
- NQ 03/2017/NQ-HĐTP — Pattern anonymize danh tính
- NĐ 77/2008/NĐ-CP Điều 19 — TVV PL hiệu lực toàn quốc (BR-NĐ77-19)
- NĐ 39/2018/NĐ-CP — Quy mô DNNVV (SIEU_NHO / NHO / VUA)
- NĐ 69/2024/NĐ-CP — SSO VNeID (BR-AUTH-01 Tier 2 — chưa web-verify, defer) — **SPEC-CLARIFY SC-06**

---

## 7. Test method + tool routing

**Mặc định cho mọi TC** (theo `CLAUDE.md` "Tool routing — BẮT BUỘC từ 2026-05-05" + memory `feedback_test_method_ui_only`):

- **Tool:** Chrome DevTools MCP (`mcp__chrome-devtools__*`) cho mọi UI test. **Cấm** gstack `$B` ngoài fallback (memory `feedback_test_method_ui_only`).
- **OTP bypass:** `666666` cho mọi role Tier 1 (cán bộ). DN auth Tier 2 VNeID — **SPEC-CLARIFY SC-06** chờ BA confirm cách auth trên QA env (mock cookie hay sandbox VNeID).
- **Auth pattern:** Template login MCP (CLAUDE.md §"Template login MCP — verified 2026-04-21") — `new_page` → `wait_for("Nhập tên đăng nhập")` → `fill_form` → `click submit` → `wait_for("Nhập mã xác thực")` → `type_text "666666"` → `wait_for("Tổng quan hệ thống")`.
- **Multi-role isolation:** `mcp__chrome-devtools__new_page({isolatedContext: true})` per role per scenario (memory `qa_htpldn_round5_t01`). KHÔNG logout-login lại vì BE httpOnly cookie sticky.
- **Verify API only via** `list_network_requests` — supporting evidence cho UI behavior. **CẤM** bulk POST `/api/v1` để pass nhanh.
- **Verify ephemeral toast:** `MutationObserver` install BEFORE click (CLAUDE.md MCP-Rule 8), KHÔNG polling DOM.
- **Verify dropdown AntD:** scroll `rc-virtual-list-holder` top→mid→bottom (memory `feedback_antd_dropdown_test_method`).
- **Verify seed coverage:** `list_network_requests` filter URL pattern, đếm count realtime per filter. Vd `?loai_tvv=TVV&trang_thai=HOAT_DONG&linh_vuc_id=X` mỗi LV ≥1. KHÔNG fallback "đủ count tổng".
- **App URL:** http://103.172.236.130:3000/ — **MailHog (OTP inbox):** http://103.172.236.130:8025

### 7.1 DN auth convention (chờ SC-06)

§1.3 ghi DN `9999999990` (HN), `9999999991` (BG) — **MST DN**, không phải VNeID username Tier 2 thật. QA env chưa wire VNeID sandbox NĐ 69/2024.

- Pre-condition: chờ BA SC-06 confirm cách bypass (mock cookie / role overlay theo memory `qa_htpldn_round5_t01` / sandbox VNeID).
- Defer mọi DN-related TC nếu SC-06 chưa confirm — mark nhóm D (Lỗi env) trong Bảng 2 execution report.

---

## 8. Cross-module downstream impact

> Sau khi FR-05 PASS, smoke verify 1 màn hình mỗi module downstream để chắc KHÔNG break luồng đọc data từ FR-05.

| Module downstream | Entity FR-05 đọc | Field/State trigger | Smoke TC verify | Ai chịu test |
|---|---|---|---|:-:|
| **FR-06 Chi trả** | `vu_viec_id` + `trang_thai='HOAN_THANH'` | DN bổ sung HSCT (FR-V.II-14) cross-ref — `_DELTA-MAP-FR05.md` Findings | **TC-CROSS-FR06-01**: VV HOAN_THANH → mở FR-06 SCR Chi trả → DN bổ sung HSCT → state HSCT chuyển đúng. **Defer chi tiết sang FR-06 plan** | QA FR-06 |
| **FR-08 Đánh giá tổng hợp** | `DANH_GIA_VU_VIEC` (UC67 thang 0-10) | KPI tổng hợp đọc điểm UC67 | **TC-CROSS-FR08-01**: DN chấm UC67 8/10 → mở FR-08 dashboard → KPI VV có điểm cập nhật trong ≤30s | QA FR-08 |
| **FR-11 Báo cáo** | `nguoi_xu_ly_id` (3 cột mới thay `nguoi_ho_tro_id`) + `cong_khai=1` filter | Report đọc field migrated | **TC-CROSS-FR11-01**: Report "VV theo người xử lý" — verify column "Người xử lý" đọc `nguoi_xu_ly_id` (KHÔNG 'N/A' cho VV migrated). **TC-CROSS-FR11-02**: filter `cong_khai=1` ra đúng VV đã công khai | QA FR-11 |
| **FR-14 Thông báo** | `THONG_BAO` từ event workflow VV | Mỗi transition T05/T06/T08/T09/T13/T16/T17/T18/T19/T20/SL1-3 sinh notif | **TC-CROSS-FR14-01**: Sau T17 (CB PD duyệt) → CB NV nhận notif in-app trong ≤30s + email gửi đến mailhog. **TC-CROSS-FR14-02**: SL1 (Công khai) → DN nhận notif "Vụ việc đã được công khai" | QA FR-14 |
| **FR-IV-CROSS-01 TVV rating** | `BR-CALC-06` — UC67 trigger cập nhật `TU_VAN_VIEN.diem_danh_gia_tb` | UC67 sinh DANH_GIA_VU_VIEC (thang 0-10) → cross-job tính diem TVV (thang 1-5 round-half-up) | **TC-CROSS-FR04-01**: Sau UC67, verify `TU_VAN_VIEN.diem_danh_gia_tb` cập nhật đúng round-half-up. Defer chi tiết sang FR-04 cross plan | QA FR-04 |

> **Defer policy:** Smoke TC trên là **trigger trigger** cho QA module downstream. FR-05 plan KHÔNG viết detail TC cross-module — chỉ note out-of-scope với marker "defer FR-06/FR-08/FR-11/FR-14 plan". Memory `feedback_test_method_ui_only` áp dụng — smoke phải UI click chain, không API direct.

---

## 9. Execution report template — BẮT BUỘC dùng 2 bảng

> CLAUDE.md "Functional/Workflow report — 2 bảng tổng hợp BẮT BUỘC sau mỗi round (enforced 2026-05-10)" yêu cầu mọi file `functional-test-report-fr-05-*.md` chứa:

- **Bảng 1** — Snapshot toàn bộ ~135 TC × status latest × Note ≤15 từ. Đặt ngay sau Verdict + Accounts.
- **Bảng 2** — TC non-PASS × Vì sao chưa chạy được × Cần làm gì × Ai làm. 6 nhóm phân loại A-F (xem `output/template/tc-block-classification-template.md`).

Template chuẩn: [`output/template/test-case-execution-report-template.md`](../../../output/template/test-case-execution-report-template.md).

---

*Test plan generated from SRS v3.5 (2026-05-06) delta — apply 14 IN + 1 V4-CHƯA-SỬA. Module XL — core nhất hệ thống. Revised 2026-05-12 13:00:00 apply ≥80% review.md (4 blocker + 8 suggestion). Bug report theo template 6 sections; CẤM Tác động / Đề xuất fix / SRS verification heading (rule `feedback_bug_report_template_strict`). Seed acceptance phải split combinatorial — KHÔNG gộp scope (rule `feedback_seed_acceptance_strict_split`).*
