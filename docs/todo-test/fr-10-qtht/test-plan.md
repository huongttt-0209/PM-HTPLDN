# Kế Hoạch Kiểm Thử — Quản trị hệ thống (FR-10, SCR-VIII-01..10)

> **Revised 2026-05-12 12:35:00 — applied review.md feedback (≥80% gap)**: bổ sung BR-DATA-06 / BR-UX-01 / BR-EC-01 / BR-EC-13 vào §2.1; sửa SCR-VIII-08 21→18 trường; thêm Phụ lục C ERR codes missing (export 10K + Excel import); tách §2.3 Permission Matrix 2 sub-table + tách BN/DP; bổ sung mapping P0/P1/P2 §5; recount transitions SM-TAIKHOAN 8 cardinality / 9 trigger; bổ sung DM_LOAI_TK upstream dep; gộp GAP-VIII table vào Phụ lục C.

> **Phiên bản**: 1.1 (Revised)
> **Ngày tạo**: 2026-05-12
> **Nguồn dữ liệu**: LOCAL — `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md` (baseline v3.5) + `input/srs-v3/srs-fr-10-quan-tri.md` (lịch sử v3) + `input/srs-update-2026-5-5/_DELTA-MAP-FR10.md` (delta)
> **SRS Reference**: FR-VIII-01..30 (27 FR sau v3.5 update, bỏ FR-VIII-06), SCR-VIII-01..10 (10 màn hình)
> **Module class**: L (Large — 27 FR, 10 SCR, 4 BR mới, SM-TAIKHOAN 4 trạng thái, 14 tab DM)

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Module gốc Lớp 1 (dữ liệu nền)** — seed data toàn hệ thống. Login chính: `qtht_01` (CRUD toàn module).
- **Phạm vi 27 FR** chia 5 cụm:
  - **Quản lý danh mục dùng chung (TPL-DM-CRUD)** — FR-VIII-01..04, 07..09, 11..13, 18..19 (12 FR áp template chung) + FR-VIII-05 (Cơ quan ĐV tree 2 tầng) + FR-VIII-30 (Tỉnh/Thành 63 GSO) = 14 tab dọc bên trái SCR-VIII-01.
  - **Quản lý vai trò + tài khoản + phân quyền** — FR-VIII-14 (vai trò), FR-VIII-15 (tài khoản người dùng), FR-VIII-16 (phân quyền dữ liệu), FR-VIII-17 (phân quyền chức năng) → SCR-VIII-02..05.
  - **Cấu hình hệ thống** — FR-VIII-10 (SLA), `MAU_PHAN_HOI` Mô hình B → SCR-VIII-06 với 2 tab (Q11 bỏ tab Phân công + Quy trình).
  - **Đăng nhập / Đăng xuất / Đăng ký + VNeID** — FR-VIII-20 (đăng nhập + TOTP), FR-VIII-21 (đăng xuất), FR-VIII-22 (DN tự đăng ký MST), FR-VIII-23..25 (VNeID), FR-VIII-26 (quên MK / kích hoạt TK lần đầu) → SCR-VIII-07/08/09.
  - **Nhật ký + Ngày lễ** — FR-VIII-28 (audit log read-only, cap 90 ngày, export 10K) → SCR-VIII-10; FR-VIII-29 (NGAY_LE CRUD + Excel import) → MH riêng.
- **Bảng dữ liệu chính**: `DANH_MUC`, `DON_VI`, `TAI_KHOAN`, `VAI_TRO`, `QUYEN_HAN`, `TAI_KHOAN_VAI_TRO`, `CAU_HINH_SLA`, `MAU_PHAN_HOI`, `NGAY_LE`, `AUDIT_LOG` (đọc-only ở module này, được mọi module CUD ghi vào).
- **Màn hình**: SCR-VIII-01 (Quản lý DM 14 tab), SCR-VIII-02 (Vai trò), SCR-VIII-03 (Tài khoản NSD, 4 trạng thái), SCR-VIII-04 (Phân quyền chức năng), SCR-VIII-05 (Phân quyền dữ liệu 2 tầng), SCR-VIII-06 (Cấu hình HT 2 tab), SCR-VIII-07 (Đăng nhập 2 tab Tier1+Tier2), SCR-VIII-08 (Đăng ký DN), SCR-VIII-09 (Đăng xuất), SCR-VIII-10 (Nhật ký HT). **SCR-VIII-08a đã XÓA** sau Q3 (bỏ trạng thái CHO_PHAN_QUYEN).

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-VIII-01 | UC99 | DM Lĩnh vực Pháp luật | DANH_MUC `loai='LINH_VUC_PL'` | `01-TC-DM-linhvuc.md` |
| 2 | FR-VIII-02 | UC100 | DM Loại hình hỗ trợ | DANH_MUC `loai='LOAI_HINH_HT'` | `02-TC-DM-loaihinhht.md` |
| 3 | FR-VIII-03 | UC101 | DM Chương trình hỗ trợ | DANH_MUC `loai='CHUONG_TRINH_HT'` | `02-TC-DM-loaihinhht.md` |
| 4 | FR-VIII-04 | UC102 | DM Tình trạng vụ việc | DANH_MUC `loai='TINH_TRANG_VV'` | `02-TC-DM-loaihinhht.md` |
| 5 | FR-VIII-05 | UC103 | DM Cơ quan đơn vị (cây 2 tầng) | DON_VI | `03-TC-coquandonvi.md` |
| 6 | FR-VIII-06 | UC104 | (CHUYỂN sang FR-04 FR-IV-NEW-01) | TO_CHUC_TU_VAN | — (Out-of-scope, xem FR-04) |
| 7 | FR-VIII-07 | UC105 | DM Loại doanh nghiệp | DANH_MUC `loai='LOAI_DN'` | `04-TC-DM-loaidn.md` |
| 8 | FR-VIII-08 | UC106 | DM Hồ sơ đề nghị HT | DANH_MUC `loai='HO_SO_DE_NGHI_HT'` | `04-TC-DM-loaidn.md` |
| 9 | FR-VIII-09 | UC107 | DM Hồ sơ đề nghị TT | DANH_MUC `loai='HO_SO_DE_NGHI_TT'` | `04-TC-DM-loaidn.md` |
| 10 | FR-VIII-10 | UC108 | Cấu hình SLA | CAU_HINH_SLA | `05-TC-SLA.md` |
| 11 | FR-VIII-11 | UC109 | DM Tiêu chí ĐG hiệu quả (trọng số) | DANH_MUC `loai='TIEU_CHI_DG_HQ'` | `06-TC-DM-tieuchi.md` |
| 12 | FR-VIII-12 | UC110 | DM Tiêu chí ĐG chi phí | DANH_MUC `loai='TIEU_CHI_DG_CP'` | `06-TC-DM-tieuchi.md` |
| 13 | FR-VIII-13 | UC111 | DM Loại TK | DANH_MUC `loai='LOAI_TK'` | `02-TC-DM-loaihinhht.md` |
| 14 | FR-VIII-14 | UC112 | Vai trò | VAI_TRO | `07-TC-vaitro.md` |
| 15 | FR-VIII-15 | UC113 | Tài khoản NSD | TAI_KHOAN | `08-TC-taikhoan.md` |
| 16 | FR-VIII-16 | UC114 | Phân quyền dữ liệu | TAI_KHOAN_VAI_TRO + scope | `09-TC-phanquyen-data.md` |
| 17 | FR-VIII-17 | UC115 | Phân quyền chức năng | VAI_TRO × QUYEN_HAN | `10-TC-phanquyen-chucnang.md` |
| 18 | FR-VIII-18 | UC116 | DM Loại hình tiếp nhận | DANH_MUC `loai='LOAI_HINH_TIEP_NHAN'` | `02-TC-DM-loaihinhht.md` |
| 19 | FR-VIII-19 | UC117 | DM Kênh tiếp nhận | DANH_MUC `loai='KENH_TIEP_NHAN'` | `02-TC-DM-loaihinhht.md` |
| 20 | FR-VIII-20 | UC118 | Đăng nhập (Tier 1 + Tier 2) | TAI_KHOAN session | `11-TC-dangnhap.md` |
| 21 | FR-VIII-21 | UC119 | Đăng xuất | session + AUDIT_LOG | `11-TC-dangnhap.md` |
| 22 | FR-VIII-22 | UC120 | DN tự đăng ký (MST, 21 trường) | TAI_KHOAN + DOANH_NGHIEP | `12-TC-dangky-DN.md` |
| 23 | FR-VIII-23 | UC121 | Đăng nhập VNeID | OIDC | `13-TC-VNeID.md` |
| 24 | FR-VIII-24 | UC122 | Đăng xuất VNeID | OIDC logout | `13-TC-VNeID.md` |
| 25 | FR-VIII-25 | UC123 | Đồng bộ tài khoản VNeID | TAI_KHOAN x VNeID profile | `13-TC-VNeID.md` |
| 26 | FR-VIII-26 | — | Quên MK / Kích hoạt TK lần đầu | TAI_KHOAN.token_reset_mk | `14-TC-quenMK.md` |
| 27 | FR-VIII-28 | — | Nhật ký hệ thống (audit log) | AUDIT_LOG read-only | `15-TC-nhatky.md` |
| 28 | FR-VIII-29 | — | Quản lý ngày lễ | NGAY_LE | `16-TC-ngayle.md` |
| 29 | FR-VIII-30 | — | DM Tỉnh/Thành phố (63 GSO) | DANH_MUC `loai='TINH_THANH'` | `17-TC-tinhthanh.md` |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | `qtht_01` (primary), `qtht_02` (fallback), `qtht_03` (permission test), `qtht_04..10` | CRUD toàn module (P0). Account chính cho mọi happy path. |
| CB_NV_TW | TW | `cb_nv_tw_01..10` | Negative permission test (CB NV không được CRUD DM/TK/Vai trò) → mong đợi ERR-AUTH-01 |
| CB_NV_BN | BN | `cb_nv_bn_01..10` | Negative permission + cross-scope test BR-AUTH-03 |
| CB_NV_DP | DP | `cb_nv_dp_01..10` | Negative permission + cross-scope test (BN không thấy DP, DP không thấy BN) |
| CB_PD_TW/BN/DP | TW/BN/DP | `cb_pd_tw_01`, `cb_pd_bn_01`, `cb_pd_dp_01` | Negative permission (PD không CRUD QTHT) + verify BR-AUTH-09 không VNeID |
| DN | — | `9999999990`, `9999999991` | FR-VIII-22 self-reg verify + FR-VIII-23 đăng nhập VNeID (positive) + FR-VIII-26 reset MK |
| NHT | DP | `nht_01`, `nht_02`, `nht_btp_tw_audit_r30` | FR-VIII-23 VNeID (positive) + FR-VIII-26 kích hoạt TK lần đầu |
| CG | TW | `huongcg` | FR-VIII-26 kích hoạt TK lần đầu (TVV/CG dùng email local-part) |
| admin | root | `admin` | Out-of-scope (không fallback, không sibling) |

> Reference: [input/users.csv](../../../input/users.csv), [output/permission-matrix.md](../../../output/permission-matrix.md), [output/permission-matrix-by-fr.md](../../../output/permission-matrix-by-fr.md). Convention `_01` primary, `_02` fallback, `_03` permission test (xem CLAUDE.md §Shared Rule 7).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> ⚠️ **Quy định điền bảng:** Cột "Ngoại lệ SRS-quoted" chỉ điền khi SRS có dòng ngoại lệ — quote nguyên văn. Để trống = BR áp dụng 100%.

| Mã | Quy tắc (quote SRS) | Nguồn (file:line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------------------|-------------------|--------------------|---------------------|------------|
| BR-AUTH-01 | "Mọi user phải xác thực trước khi truy cập hệ thống. **Mô hình 2-tier:** Tier 1 (nội bộ qua mạng kín) = Username/password + TOTP 2FA qua email, áp cho cán bộ nội bộ. Tier 2 (Internet-facing) = SSO VNeID qua OIDC Authorization Code flow (NĐ69/2024/NĐ-CP), áp cho tác nhân bên ngoài (DN, TVV, CG, NHT). **Không có VNPT eKYC.**" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2164` | ✅ Yes | "API outbound không yêu cầu session" | TC-11 Đăng nhập Tier 1 (TOTP) + TC-13 SSO VNeID |
| BR-AUTH-02 | "Cấu trúc **2 tầng**: TW (cấp 1, Cục BLDS&KT) → {BN, ĐP} (cấp 2, ngang cấp song song). BN và ĐP là 2 loại đơn vị độc lập, KHÔNG có quan hệ cha-con giữa BN và ĐP" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2170` | ✅ Yes | — | TC-03 tạo DP với cha=BN → ERR-DV-02; verify cây seed |
| BR-AUTH-03 | "BN chỉ thấy dữ liệu BN mình. ĐP chỉ thấy dữ liệu ĐP mình. BN không thấy ĐP và ngược lại" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2176` | ✅ Yes | "QTHT thấy tất cả" | TC-09 cross-unit query = 0 rows; TC-08 SCR-VIII-03 list filter `don_vi_id` |
| BR-AUTH-04 | "**Chỉ TW thấy cấp con.** TW thấy toàn bộ dữ liệu TW + BN + ĐP. BN không có cấp con trực thuộc (mô hình 2-tier — BN và ĐP ngang cấp song song)" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2182` | ✅ Yes (FR-VIII-14 trực tiếp; FR-VIII-16 cross-FR inference) | "SRS authoritative chỉ map FR-VIII-14 Vai trò. FR-VIII-16 Phân quyền dữ liệu suy luận do scope chồng entity VAI_TRO" | TC-09 permission tree QTHT thấy all vs CB NV TW thấy TW+BN+DP |
| BR-AUTH-06 | "Session CMS: 30 phút idle timeout. API JWT: TTL 15 phút, refresh token 24 giờ" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2188` | ✅ Yes | — | TC-11 idle 30' → modal cảnh báo + auto logout |
| BR-AUTH-07 | "Khóa tài khoản sau 5 lần đăng nhập sai liên tiếp. Tự mở khóa sau 30 phút HOẶC QTHT mở khóa thủ công qua UC113" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2194` | ✅ Yes | — | TC-11 brute force 5 fail → ERR-DN-04; TC-08 QTHT mở khóa |
| BR-AUTH-08 | "chính sách phân quyền dữ liệu áp dụng cho MỌI bảng có cột `don_vi_id`" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2200` | ✅ Yes | "AUDIT_LOG không có phân quyền" | TC-09 + TC-15 nhật ký bypass `don_vi_id` |
| BR-AUTH-09 | "Cán bộ nội bộ (Cán bộ Nghiệp vụ, Cán bộ Phê duyệt, Quản trị Hệ thống) chỉ đăng nhập bằng Tier 1 (tên đăng nhập + mật khẩu + mã xác thực 2 lớp) qua mạng kín. KHÔNG đăng nhập qua VNeID, KHÔNG đồng bộ tài khoản với VNeID qua UC123" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2206` | ✅ Yes | "DN/NHT/TVV/CG vẫn được dùng VNeID bình thường" | TC-13 CB nội bộ click VNeID → ERR-VN-04 |
| BR-AUTH-USERNAME-01 | "Quy ước sinh `TAI_KHOAN.username` theo loại tài khoản: (1) DN tự đăng ký (FR-VIII-22) → username auto = `ma_so_thue` (10 chữ số, readonly). (2) Cán bộ nội bộ — QTHT/CB NV/CB PD (FR-VIII-15) → QTHT nhập tay. (3) TVV/CG (FR-IV-07) → username auto = local-part email. (4) NHT (FR-IV-NHT-01) → CB NV nhập tay. Mọi username UNIQUE. Regex chung: `^[a-z0-9_]{4,50}$`" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2212` | ✅ Yes | "TVV/CG trùng local-part → append seq `.2`, `.3`" | TC-12 DN đăng ký → username=MST; TC-08 QTHT tạo TK CB nội bộ regex check |
| BR-AUTH-EMAIL-01 | "Phân biệt 2 trường email: (a) `TAI_KHOAN.email` = email cá nhân login, UNIQUE; (b) `DOANH_NGHIEP.email` = email liên hệ tổ chức, KHÔNG UNIQUE. Khi DN tự đăng ký: UI 1 ô email duy nhất, hệ thống lưu vào CẢ 2 cột. Sau đăng ký 2 trường đổi độc lập không cần OTP" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2218` | ✅ Yes | — | TC-12 đăng ký DN: 1 ô → 2 cột giá trị giống nhau |
| BR-DATA-01 | "Mọi thao tác xóa đều là soft delete (set `is_deleted = 1`)" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2224` | ✅ Yes | "AUDIT_LOG: không xóa" | TC-01..04, 07, 08: DELETE = UPDATE is_deleted; TC-15 audit không có DELETE |
| BR-DATA-02 | "Mọi bản ghi nghiệp vụ PHẢI có `don_vi_id` NOT NULL" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2230` | ✅ Yes | "DANH_MUC dùng chung: NULL cho DM hệ thống" | TC-01..04 verify NOT NULL constraint riêng entity nghiệp vụ |
| BR-DATA-03 | "Mọi entity đều có 7 common fields (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id)" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2236` | ✅ Yes | "AUDIT_LOG: chỉ có id, thoi_gian, entity fields" | TC schema verify (defer DBA) |
| BR-DATA-05 | "Mọi thao tác CUD + phê duyệt + đăng nhập/xuất đều ghi vào AUDIT_LOG. Immutable" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2242` | ✅ Yes | — | TC-15 verify INSERT-only sau mỗi action C/U/D ở SCR-VIII-01..05 + login/logout |
| BR-DATA-07 | "Default: 20 rows/page, max: 100 rows/page" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2248` | ✅ Yes | "Dashboard: không phân trang" | TC-01..09 boundary 20/100/101 rows; TC-15 audit log 50/trang đặc thù |
| BR-SLA-01 | "SLA mặc định vụ việc HTPL = 10 ngày làm việc (NĐ55/2019 Điều 9)" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2254` | ✅ Yes | "Có thể cấu hình khác tại UC108" | TC-05 verify seed `deadline_vu_viec=10` |
| BR-SLA-02 | "4 mức (mã DB → nhãn hiển thị): `BINH_THUONG` → 'Trong hạn' (>50% còn lại, xanh lá), `SAP_HET_HAN` → 'Sắp hết hạn' (<50% còn lại, vàng), `QUA_HAN` → 'Quá hạn' (>100%, đỏ), `QUA_HAN_NGHIEM_TRONG` → 'Quá hạn nghiêm trọng' (>2x, hồng tím/đen)" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2260` | ✅ Yes | — | TC-05 cấu hình 2 ngưỡng cảnh báo + verify mock SLA mỗi mức |
| BR-SLA-04 | "Thứ 2-6 (trừ ngày lễ quốc gia + ngày nghỉ bù). Danh sách ngày lễ quản lý tại entity NGAY_LE" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2266` | ✅ Yes | — | TC-16 verify deadline qua ngày lễ trừ NGAY_LE |
| BR-CALC-03 | "Deadline = ngày tiếp nhận + N ngày làm việc. N lấy từ CAU_HINH_SLA" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2272` | ✅ Yes | — | TC-05 verify deadline math |
| BR-CALC-04 | "Tổng trọng số các tiêu chí = 100%. Điểm tổng = SUM(diem_i * trong_so_i / 100)" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2278` | ✅ Yes | — | TC-06 tổng trọng số tiêu chí HQ ≠ 100% → cảnh báo đỏ |
| BR-INTG-06 | "Mô hình 2-tier: Tier 1 (nội bộ qua mạng kín) = username/password + TOTP 2FA. Tier 2 (Internet-facing) = SSO VNeID qua OIDC Authorization Code flow (NĐ69/2024/NĐ-CP). Không có VNPT eKYC" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2284` | ✅ Yes | "Tier 1 là fallback mặc định cho nội bộ" | TC-13 SSO VNeID OIDC happy + ERR-VN-01..04 |
| BR-DATA-06 | "Mọi danh sách bảng có nút **[Xuất Excel]** trên toolbar. Cap mặc định 10.000 dòng (xem `:1355`). Audit log export cap riêng 10K (`:1843`)" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1355` | ✅ Yes | "Dashboard / Empty list: không xuất" | Áp dụng DM (14 tab) / DON_VI / VAI_TRO / TAI_KHOAN / NGAY_LE / AUDIT_LOG → TC-01..04, 07, 08, 15, 16 verify nút + cap 10K |
| BR-EC-01 | "Optimistic locking: mọi UPDATE/DELETE phải kèm `version` (hoặc `updated_at`). Nếu version mismatch → ERR-LOCK-01 'Bản ghi đã được người khác cập nhật, vui lòng reload'" | `srs-v3/srs-fr-10-quan-tri.md` Phụ lục B (BR-EC-01) | ✅ Yes | "INSERT race không apply optimistic lock — apply unique constraint thay thế" | TC-01..04, 07, 08: 2 QTHT đồng thời edit cùng record → 1 thành công + 1 ERR-LOCK-01 |
| BR-EC-13 | "Search input phải sanitize input: tối đa 200 ký tự, strip HTML tag, escape SQL/regex meta chars" | `srs-v3/srs-fr-10-quan-tri.md` Phụ lục B (BR-EC-13) | ✅ Yes | — | TC-01..09: nhập 201 ký tự → cắt 200; nhập `<script>` → strip; nhập `' OR 1=1` → escape |
| BR-UX-01 | "Filter state đồng bộ qua URL query params (deep-link reproducible). Reload page giữ filter" | `srs-v3/srs-fr-10-quan-tri.md` Phụ lục B (BR-UX-01) | ✅ Yes | — | TC-01..09 + TC-15: apply filter → URL update → reload → filter giữ |
| BR-DATA-07-OVERRIDE-AUDIT | "AUDIT_LOG override BR-DATA-07: phân trang 50/trang (không 20/trang default)" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1843` | ✅ Yes | — | TC-15 verify mặc định 50/page, đổi 100/page OK, 20/page deprecated cho audit |

> **Module-specific BR bổ sung:** 4 BR cross-cutting Phụ lục B (BR-DATA-06 / BR-EC-01 / BR-EC-13 / BR-UX-01) đã pull vào bảng trên (theo review feedback — không defer xuống TC detail).

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Nguồn | Severity |
|--------|-------------------|----------------------|-------|----------|
| ERR-AUTH-01 | User không có quyền QTHT | "Bạn không có quyền thực hiện chức năng này" | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:153` | ERROR |
| ERR-AUTH-02 | Session hết hạn | "Redirect về trang đăng nhập" | `:154` | ERROR |
| ERR-DM-01 | Mã danh mục trùng | "Mã '{ma}' đã tồn tại trong danh mục {loai}" | `:155` | ERROR |
| ERR-DM-02 | Tên danh mục trống | "Tên danh mục là bắt buộc" | `:156` | ERROR |
| ERR-DM-03 | Bản ghi đang được tham chiếu | "Không thể xóa. Danh mục đang được sử dụng bởi {N} bản ghi {entity}" | `:157` | ERROR |
| ERR-DM-04 | Bản ghi không tồn tại | "Bản ghi không tồn tại hoặc đã bị xóa" | `:158` | ERROR |
| ERR-DM-05 | Mã vượt quá 20 ký tự | "Mã danh mục tối đa 20 ký tự" | `:159` | ERROR |
| ERR-DV-01 | Mã đơn vị trùng | "Mã đơn vị '{ma}' đã tồn tại" | `:348` | ERROR |
| ERR-DV-02 | Cấp BN/DP thiếu đơn vị cha | "Cấp {cap} phải có đơn vị cha" | `:349` | ERROR |
| ERR-DV-03 | Đơn vị có TK liên kết | "Không thể xóa. Đơn vị có {N} tài khoản liên kết" | `:350` | ERROR |
| ERR-DV-04 | Đơn vị có dữ liệu nghiệp vụ | "Không thể xóa. Đơn vị có {N} bản ghi dữ liệu" | `:351` | ERROR |
| ERR-DV-05 | Vòng lặp cây đơn vị | "Không thể tạo vòng lặp phân cấp" | `:352` | ERROR |
| ERR-SLA-01 | `thoi_han_ngay <= 0` | "Thời hạn xử lý phải là số nguyên dương" | `:504` | ERROR |
| ERR-SLA-02 | `canh_bao_1 >= canh_bao_2` | "Mức cảnh báo 1 phải nhỏ hơn mức cảnh báo 2" | `:505` | ERROR |
| ERR-SLA-03 | `loai_yeu_cau` trùng | "Loại yêu cầu đã có cấu hình SLA" | `:506` | ERROR |
| ERR-TC-01 | `thang_diem_min >= thang_diem_max` | "Điểm tối thiểu phải nhỏ hơn điểm tối đa" | `:554` | ERROR |
| ERR-VT-01 | Mã vai trò trùng | "Mã vai trò '{ma}' đã tồn tại" | `:647` | ERROR |
| ERR-VT-02 | Vai trò đang gán cho TK | "Không thể xóa. Vai trò đang gán cho {N} tài khoản" | `:648` | ERROR |
| ERR-TK-01 | Username trùng | "Username '{username}' đã tồn tại" | `:722` | ERROR |
| ERR-TK-02 | Email trùng | "Email '{email}' đã được sử dụng" | `:723` | ERROR |
| ERR-TK-03 | Mật khẩu yếu | "Mật khẩu phải >= 8 ký tự, chứa chữ hoa, chữ thường, số và ký tự đặc biệt" `[GAP-VIII-04]` | `:724` | ERROR |
| ERR-TK-04 | Username chứa ký tự đặc biệt | "Username chỉ chấp nhận chữ cái, số và dấu gạch dưới" | `:725` | ERROR |
| ERR-TK-05 | Đơn vị không tồn tại | "Đơn vị không tồn tại hoặc đã bị vô hiệu hóa" | `:726` | ERROR |
| ERR-TK-06 | Vai trò không tồn tại | "Vai trò ID {id} không tồn tại" | `:727` | ERROR |
| ERR-PQ-01 | Vi phạm quy tắc ngang cấp | "Không thể gán quyền xem đơn vị {A} cho vai trò thuộc đơn vị {B} (ngang cấp)" | `:785` | ERROR |
| ERR-PQ-02 | Vai trò không tồn tại | "Vai trò không tồn tại" | `:786` | ERROR |
| ERR-PQ-03 | Đơn vị không tồn tại | "Đơn vị ID {id} không tồn tại" | `:787` | ERROR |
| ERR-PQ-04 | Quyền không tồn tại | "Quyền chức năng ID {id} không tồn tại" | `:839` | ERROR |
| ERR-DN-01 | Username/password sai | "Đăng nhập không thành công. Vui lòng kiểm tra lại thông tin" | `:946` | ERROR |
| ERR-DN-02 | TK tạm khóa | "Tài khoản đã bị tạm khóa. Vui lòng liên hệ QTHT" | `:947` | ERROR |
| ERR-DN-03 | TK vô hiệu hóa | "Tài khoản đã bị vô hiệu hóa" | `:948` | ERROR |
| ERR-DN-04 | Login sai ≥ 5 lần | "Tài khoản đã bị tạm khóa do đăng nhập sai quá 5 lần" | `:949` | ERROR |
| ERR-DN-07 | Session hết hạn | "Phiên làm việc hết hạn" | `:950` | INFO |
| ERR-DN-08 | Mã TOTP sai/hết hạn | "Mã xác thực không đúng hoặc đã hết hạn" | `:951` | ERROR |
| ERR-REG-01a | MST sai định dạng | "Mã số thuế phải đúng 10 chữ số (theo TT 105/2020/TT-BTC). Chi nhánh không tự đăng ký riêng." | `:1074` | ERROR |
| ERR-REG-01 | MST đã tồn tại | "Mã số thuế này đã đăng ký trong hệ thống" | `:1075` | ERROR |
| ERR-REG-02 | Email trùng `TAI_KHOAN.email` | "Email đã được sử dụng" | `:1076` | ERROR |
| ERR-REG-04 | Mật khẩu yếu (DN reg) | "Mật khẩu chưa đủ mạnh" | `:1077` | ERROR |
| ERR-REG-05 | Confirm MK không khớp | "Mật khẩu xác nhận không khớp" | `:1078` | ERROR |
| ERR-REG-06 | Chưa tích cam kết | "Vui lòng tích cam kết thông tin đúng sự thật để tiếp tục" | `:1079` | ERROR |
| ERR-VN-01 | VNeID OIDC lỗi | "Đăng nhập VNeID thất bại. Vui lòng thử lại hoặc sử dụng tài khoản nội bộ" | `:1142` | ERROR |
| ERR-VN-02 | Chưa có TK trong hệ thống | "Tài khoản chưa được tạo hoặc chưa đồng bộ VNeID. Vui lòng đăng ký (DN) hoặc liên hệ quản trị viên (vai trò khác)" | `:1143` | ERROR |
| ERR-VN-03 | Tier 2 chưa triển khai | "Nút Đăng nhập VNeID ẩn (feature flag off)" | `:1144` | — |
| ERR-VN-04 | CB nội bộ cố login VNeID | "Tài khoản nội bộ không được phép đăng nhập qua VNeID. Vui lòng dùng tên đăng nhập + mật khẩu" | `:1145` | ERROR |
| ERR-PWD-01 | Email không tồn tại (quên MK) | "Nếu email đã đăng ký, link đặt mật khẩu sẽ được gửi đến hộp thư của bạn" (chống enumerate) | `:1297` | INFO |
| ERR-PWD-02 | TK đang TAM_KHOA / VO_HIEU_HOA | "Tài khoản đã bị khóa hoặc vô hiệu hóa. Liên hệ quản trị viên để được hỗ trợ" | `:1298` | ERROR |
| ERR-PWD-03 | Token hết hạn (reset 30 phút) | "Link đặt mật khẩu đã hết hạn. Vui lòng yêu cầu link mới" | `:1299` | ERROR |
| ERR-PWD-04 | Token đã sử dụng | "Link đặt mật khẩu đã được sử dụng. Vui lòng yêu cầu link mới" | `:1300` | ERROR |
| ERR-PWD-05 | Mật khẩu yếu (reset) | "Mật khẩu chưa đủ mạnh" | `:1301` | ERROR |
| ERR-PWD-06 | Confirm MK không khớp (reset) | "Mật khẩu xác nhận không khớp" | `:1302` | ERROR |
| ERR-LOG-01 | Không có quyền QTHT (audit) | "Bạn không có quyền truy cập nhật ký hệ thống" | `:1369` | ERROR |
| ERR-LOG-02 | Khoảng thời gian > 90 ngày | "Khoảng thời gian tối đa là 90 ngày" | `:1370` | WARNING |
| ERR-NL-01 | Không có quyền QTHT (ngày lễ) | "Bạn không có quyền quản lý ngày lễ" | `:1430` | ERROR |
| ERR-NL-02 | Trùng `(ngay, nam)` | "Ngày {ngay} năm {nam} đã tồn tại trong danh sách" | `:1431` | ERROR |
| ERR-NL-03 | Loại không thuộc enum | "Loại ngày nghỉ phải là NGAY_LE / NGHI_BU / NGHI_KHAC" | `:1432` | ERROR |

> ⚠️ Khi test negative, expected message phải match **nguyên văn** SRS — không "close enough" accept.

### 2.3 Permission Matrix (module-specific)

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md) (49 entity × 11 role). Bảng dưới là subset cho 10 entity FR-10, **tách 2 sub-table** theo review feedback.

#### 2.3.1 Sub-table A — Entity × Role (module-specific)

> Tách `CB_NV_BN` vs `CB_NV_DP` (không gộp như cũ) — verify BR-AUTH-03 "BN không thấy DP và ngược lại" tường minh.

| Entity / Action | QTHT | admin | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | LD_BTP | DN | NHT | TVV/CG |
|-----------------|:----:|:-----:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:------:|:--:|:---:|:------:|
| DANH_MUC (14 tab DM) | CRUD | CRUD | R | R | R | R | R | R | R | — | — | — |
| DON_VI (cây 2 tầng) | CRUD | CRUD | R (TW+BN+DP) | R (own BN) | R (own DP) | R | R | R | R | — | — | — |
| TAI_KHOAN | CRUD | CRUD | — | — | — | — | — | — | R | self-reg (FR-VIII-22) | — | — |
| VAI_TRO | CRUD | CRUD | — | — | — | — | — | — | R | — | — | — |
| QUYEN_HAN × VAI_TRO (UC114/115) | CRUD | CRUD | — | — | — | — | — | — | — | — | — | — |
| CAU_HINH_SLA | CRUD | CRUD | R | R | R | R | R | R | R | — | — | — |
| MAU_PHAN_HOI (Mô hình B) | R | R | CRUD (TW_QUOC_GIA) | CRUD (own BN_RIENG) | CRUD (own DP_RIENG) | R | R | R | R | — | — | — |
| NGAY_LE | CRUD | CRUD | R | R | R | R | R | R | R | — | — | — |
| AUDIT_LOG | R (90 ngày + export 10K) | R | — | — | — | — | — | — | R *[GAP-AUDIT-ROLE]* | — | — | — |
| Đăng nhập (FR-VIII-20) | Tier 1 | Tier 1 | Tier 1 (BR-AUTH-09) | Tier 1 | Tier 1 | Tier 1 | Tier 1 | Tier 1 | Tier 1 | Tier 2 VNeID | Tier 2 VNeID | Tier 2 VNeID |
| Đăng ký DN (FR-VIII-22) | — | — | — | — | — | — | — | — | — | self-reg | — | — |

> ⚠️ `LD_BTP` quyền R AUDIT_LOG là **[GAP-AUDIT-ROLE]** — SRS `:1369` ERR-LOG-01 "Bạn không có quyền..." implies role check nhưng KHÔNG list cụ thể role nào có quyền. Defer escalate BA.

#### 2.3.2 Sub-table B — BR-AUTH cross-cutting × Role × Cite

| BR | Trigger / nội dung | SRS cite | Áp dụng role |
|----|--------------------|---------|---------------|
| BR-AUTH-01 | 2-tier login (Tier1 + Tier2 VNeID) | `:2164` | Tier 1: QTHT/admin/CB_NV_*/CB_PD_*/LD_BTP · Tier 2: DN/NHT/TVV/CG |
| BR-AUTH-03 | BN ≠ DP scope; BN không thấy DP và ngược lại | `:2176` | CB_NV_BN vs CB_NV_DP — verify cross-unit query 0 rows |
| BR-AUTH-04 | TW thấy cấp con (BN + DP); BN/DP không thấy nhau | `:2182` | CB_NV_TW (thấy all) vs BN/DP (thấy own) — exception QTHT |
| BR-AUTH-08 | Phân quyền data áp cho mọi bảng có `don_vi_id` | `:2200` | Mọi role + mọi entity nghiệp vụ; **AUDIT_LOG ngoại lệ** (không có phân quyền per row) |
| BR-AUTH-09 | CB nội bộ KHÔNG đăng nhập VNeID | `:2206` | QTHT/CB_NV_*/CB_PD_*/LD_BTP/admin (Tier 1 only). DN/NHT/TVV/CG vẫn dùng VNeID |

### 2.4 UI Layout per SCR

> ⚠️ KHÔNG dùng absence để khẳng định "module KHÔNG có X". Mọi feature không list phải đối chiếu §2.1 trước.

**SCR-VIII-01 — Quản lý Danh mục (14 tab dọc)** (`srs-update-2026-5-5/srs-fr-10-quan-tri.md:1485-1539`)
- Sidebar trái: 14 tab (Lĩnh vực PL / Loại hình HT / Chương trình HT / Tình trạng VV / **Cơ quan ĐV** [tree 2 tầng] / Loại DN / Hồ sơ đề nghị HT / Hồ sơ đề nghị TT / Tiêu chí ĐG HQ [trọng số %] / Tiêu chí ĐG CP / Loại TK / Loại hình tiếp nhận / Kênh tiếp nhận / **Tỉnh/Thành** [NEW Q9]). **Bỏ Tổ chức TV** (đã chuyển FR-04).
- Toolbar: Breadcrumb + [+ Thêm mới] + [Tìm kiếm] + [Xuất Excel] (BR-DATA-06 default).
- Filter-bar: Tìm theo mã/tên (sanitize 200 chars BR-EC-13).
- Content/Table: cột Mã / Tên / Mô tả / Thứ tự / Trạng thái + Hành động (Sửa/Xóa = `<a>` tag).
- Drawer form (NOT Modal — app quirk): Mã / Tên / Mô tả / Thứ tự / Trạng thái (radio Kích hoạt/Vô hiệu hóa) + [Đồng ý]/[Hủy] (NOT [Lưu]).
- Tab Cơ quan ĐV: tree-view + form chi tiết bên phải + nút [+ Thêm đơn vị con] trên TW (BN không có cấp con per BR-AUTH-02).
- Tab Tiêu chí ĐG HQ: cột bổ sung Trọng số (%), Thang điểm min/max. **Tổng trọng số phải = 100%** (cảnh báo đỏ nếu ≠).
- Tab Tỉnh/Thành: read-only seed (63 GSO QĐ 124/2004), QTHT chỉ chỉnh `trang_thai`, KHÔNG Add/Delete.

**SCR-VIII-02 — Quản lý Vai trò** (`:1540-1562`)
- List: Mã / Tên / Mô tả / Số TK gán / Số quyền / Trạng thái (toggle) + Sửa/Xóa.
- Modal CRUD: Mã / Tên / Mô tả / Trạng thái.

**SCR-VIII-03 — Quản lý Tài khoản NSD** (`:1563-1604`)
- **4 tab trạng thái** (Q3 bỏ CHO_PHAN_QUYEN): Tất cả / Hoạt động / Chờ kích hoạt / Tạm khóa.
- Filter: Username/Họ tên/Email + Vai trò + Đơn vị + Loại TK + Trạng thái (enum 4: `CHO_KICH_HOAT, HOAT_DONG, TAM_KHOA, VO_HIEU_HOA`).
- Cột: Username / Họ tên / Email / Đơn vị / Vai trò (tag) / Trạng thái (badge) / Hành động (Xem/Sửa/Mở khóa/Khóa/Gửi lại email/Đổi MK). **KHÔNG có nút Phân quyền** (Q3 deprecate).
- Form: Username / Email / Họ tên / MK (≥8 ký tự, hoa+thường+số+**ký tự đặc biệt**) / Vai trò (multi-select) / Đơn vị (tree) / Loại TK / CCCD.

**SCR-VIII-04 — Phân quyền Chức năng** (`:1605-1631`)
- Dropdown chọn vai trò + cây menu × cột (Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất) + checkbox + logic cha-con.
- [Lưu] / [Reset mặc định].

**SCR-VIII-05 — Phân quyền Dữ liệu** (`:1632-1649`)
- Tree đơn vị 2 tầng + checkbox multi-select + validate ngang cấp (BR-AUTH-03 → ERR-PQ-01) + tag list.
- [Lưu] phân quyền theo vai trò.

**SCR-VIII-06 — Cấu hình Hệ thống (2 tab)** (`:1650-1724`) — Q11 BỎ Tab Phân công mặc định + Tab Quy trình hỗ trợ.
- **Tab 1 SLA:** bảng 4 loại yêu cầu (Hỏi đáp / Vụ việc / Hồ sơ HT / Hồ sơ TT) × thời hạn (ngày) + 2 ngưỡng cảnh báo % + toggle Email/In-app. Q5 BỎ ngưỡng "Quá hạn nghiêm trọng" (nội bộ DB).
- **Tab 2 Mẫu phản hồi:** Tên / Lĩnh vực / Nội dung Rich Text / Trạng thái / **Phạm vi áp dụng** (TW_QUOC_GIA / BN_RIENG / DP_RIENG — Mô hình B Hybrid 2 tầng) / Đơn vị. Quyền: QTHT chỉ R; CB_NV CRUD theo cấp.

**SCR-VIII-07 — Đăng nhập (2 tab)** (`:1725-1751`)
- Tab 1 Tài khoản: Username + Mật khẩu + OTP 6 số (Tier 1 TOTP).
- Tab 2 VNeID: button OIDC redirect (Tier 2, ẩn nếu feature flag off → ERR-VN-03).
- Modal cảnh báo session 25' idle → force logout 30' (BR-AUTH-06).

**SCR-VIII-08 — Đăng ký Tài khoản DN** (`:1752-1795`)
- **Form 18 trường** (FR-VIII-22 đại tu, BA Q8 chốt 2026-05-07 "19 DN → 18 DN" theo changelog `:21`): MST (readonly auto username 10 chữ số) / Tên DN / Giấy ĐKKD / Ngày cấp / Tỉnh/TP (FK FR-VIII-30) / Loại DN / Quy mô / Người đại diện / Email (1 ô — Phương án B → lưu cả `TAI_KHOAN.email` + `DOANH_NGHIEP.email`) / SĐT / Mật khẩu (≥8 + ký tự đặc biệt) / Confirm MK / **Checkbox cam kết thông tin đúng sự thật** (bắt buộc) / CAPTCHA. (Field count chính thức 18 — tester verify khi viết TC-12.)
- Tạo TK state `CHO_KICH_HOAT` + email kích hoạt 7 ngày (bypass CHO_PHAN_QUYEN per Q3).

**SCR-VIII-08a — ĐÃ XÓA** (`:1796-1801`) — BA Q3+Q10 chốt bỏ.

**SCR-VIII-09 — Đăng xuất** (`:1802-1814`)
- Avatar dropdown → Đăng xuất → Modal xác nhận → hủy JWT.
- Auto logout 25' idle (cảnh báo) → 30' (force).
- Đăng xuất VNeID: hủy JWT + gọi VNeID OIDC logout.

**SCR-VIII-10 — Nhật ký Hệ thống** (`:1815-1847`)
- Read-only. Filter: từ-đến ngày (cap 90 ngày → ERR-LOG-02) / Người dùng / Module (12 module) / Loại thao tác / Entity.
- Cột: Thời gian (sortable) / Người / Đơn vị / Module / Entity / Mã bản ghi / Loại thao tác / Chi tiết JSON diff.
- Phân trang **50/trang** (đặc thù module này, khác BR-DATA-07 default 20) · retention 5 năm · immutable · export Excel cap **10.000 dòng**.

**FR-VIII-29 MH Ngày lễ riêng** (`:1383-1444`) — không thuộc SCR-VIII-06.
- Calendar view + List view. Form: ngay (UNIQUE per năm) / nam (≥2024) / ten_ngay_le / loai (enum NGAY_LE/NGHI_BU/NGHI_KHAC) / ghi_chu.
- Import Excel (mỗi ngày 1 dòng, Tết 7 ngày → 7 dòng).

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**
- ☑ Nút [Xuất Excel] toolbar (BR-DATA-06) — có ở DM/DV/Vai trò/TK/NGAY_LE/AUDIT_LOG (cap 10K riêng audit).
- ☑ Pagination 20/page default (BR-DATA-07) — TRỪ audit log 50/trang.
- ☑ Search sanitize 200 chars (BR-EC-13).
- ☑ URL sync filter (BR-UX-01).
- ☑ Audit log mọi CUD (BR-DATA-05).
- ☑ Optimistic lock mọi UPDATE/DELETE (BR-EC-01) — verify khi 2 QTHT đồng thời edit cùng record.

**Feature module KHÔNG có:**
- Tab Phân công mặc định ở SCR-VIII-06 — Q11 deprecate, thay bằng auto-filter 4 tiêu chí FR-II-06 Step 5 (quote `srs-update-2026-5-5/srs-fr-10-quan-tri.md` Lịch sử thay đổi).
- SCR-VIII-08a (QTHT duyệt TK) — XÓA hẳn sau Q3+Q10, không còn UC duyệt thủ công.

### 2.5 State Machine — SM-TAIKHOAN

Source: `srs-update-2026-5-5/srs-fr-10-quan-tri.md:2089-2126`

**4 trạng thái (Q3 bỏ CHO_PHAN_QUYEN):**

| Trạng thái | Mã | Mô tả |
|------------|-----|-------|
| CHO_KICH_HOAT | pending | Mới tạo, chưa kích hoạt (vai trò đã gán sẵn) |
| HOAT_DONG | active | Đang dùng bình thường |
| TAM_KHOA | locked | Bị khóa tạm (5 lần sai MK hoặc QTHT khóa) |
| VO_HIEU_HOA | disabled | Bị vô hiệu hóa bởi QTHT |

**Bảng chuyển trạng thái — 8 transition cardinality / 9 trigger source** (HOAT_DONG → TAM_KHOA có 2 trigger độc lập: auto 5-fail và QTHT khóa thủ công — đếm là 1 transition cardinality):

| Từ | Đến | Trigger | Guard | FR Ref | BR Ref |
|----|-----|---------|-------|--------|--------|
| `[*]` | CHO_KICH_HOAT | QTHT tạo TK / User đăng ký (vai trò gán sẵn) | — | FR-VIII-15, FR-VIII-22 | — |
| CHO_KICH_HOAT | HOAT_DONG | User kích hoạt qua email + đặt MK lần đầu | Token hợp lệ + MK đủ độ mạnh | FR-VIII-15, FR-VIII-22, FR-VIII-26 | — |
| HOAT_DONG | TAM_KHOA | 5 lần đăng nhập sai (auto) | `so_lan_sai >= 5` | FR-VIII-20 | BR-AUTH-07 |
| HOAT_DONG | TAM_KHOA | QTHT khóa thủ công | — | FR-VIII-19 | — |
| TAM_KHOA | HOAT_DONG | QTHT mở khóa | — | FR-VIII-19 | BR-AUTH-07 |
| TAM_KHOA | HOAT_DONG | Sau 30 phút (auto) | `elapsed >= 30 phút` | FR-VIII-20 | BR-AUTH-07 |
| HOAT_DONG | VO_HIEU_HOA | QTHT vô hiệu hóa | — | FR-VIII-19 | — |
| VO_HIEU_HOA | HOAT_DONG | QTHT khôi phục | — | FR-VIII-19 | — |
| CHO_KICH_HOAT | VO_HIEU_HOA | Auto: quá 7 ngày token hết hạn | `activation_token_expired` | — | — |

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| **GĐ 1 Seed** | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | `danh_muc_variants`, `don_vi_variants`, `tai_khoan_variants`, `vai_tro_variants`, `ngay_le_variants` (cần bổ sung Tết/30-4/1-5/2-9), `cau_hinh_sla_variants` |
| **GĐ 1 click flow** | [`input/quy-trinh-nghiep-vu/flow-module.md`](../../../input/quy-trinh-nghiep-vu/flow-module.md) | §FR-10 thứ tự seed Lớp 1 |
| **GĐ 2 Workflow** | [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) | §① FR-10 — bảng SM-TAIKHOAN + 14 tab DM + 2 tab SCR-VIII-06 |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | Entity DANH_MUC/DON_VI/TAI_KHOAN/VAI_TRO/NGAY_LE: "Tạo tại / Đọc tại" |

**Upstream dependencies (Tier check):**

| Entity của module | Tier | Phụ thuộc entity nào (upstream) | Seed trước tại module |
|-------------------|:----:|----------------------------------|-----------------------|
| DANH_MUC (14 loại) | 1 | — (gốc) | FR-10 |
| DON_VI (cây 2 tầng) | 1 | DM TINH_THANH (FR-VIII-30 seed 63 GSO) | FR-10 |
| VAI_TRO | 1 | — | FR-10 |
| QUYEN_HAN | 1 | — (system seed) | FR-10 |
| TAI_KHOAN | 1 | VAI_TRO, DON_VI, **DANH_MUC LOAI_TK** (FR-VIII-13 — FK `loai_tk`) | FR-10 |
| CAU_HINH_SLA | 1 | DANH_MUC LOAI_HINH_HT | FR-10 |
| MAU_PHAN_HOI | 1 | DANH_MUC LINH_VUC_PL | FR-10 |
| NGAY_LE | 1 | — | FR-10 |
| AUDIT_LOG | — (read-only) | mọi entity CUD | — |

> **Lưu ý:** FR-VIII-30 Tab Tỉnh/Thành seed lúc deploy (63 record GSO QĐ 124/2004) — QA verify count = 63, không tạo tay.

---

## 3. Cấu Trúc File Test Case

> ⚠️ **Note (review feedback):** FR-VIII-06 (Tổ chức Tư vấn) đã chuyển sang FR-04 (`FR-IV-NEW-01`) — **KHÔNG có file TC** trong folder này. Tester KHÔNG search FR-VIII-06 trong fr-10-qtht/. Reference: §1.2 row 6.

```
fr-10-qtht/
├── test-plan.md                          ← File này (overview)
├── 01-TC-DM-linhvuc.md                   ← FR-VIII-01 Lĩnh vực PL (CRUD chuẩn TPL-DM-CRUD)
├── 02-TC-DM-loaihinhht.md                ← FR-VIII-02/03/04/13/18/19 (gom 6 DM dùng TPL)
├── 03-TC-coquandonvi.md                  ← FR-VIII-05 Cơ quan ĐV (tree 2 tầng + BR-AUTH-02/04)
├── 04-TC-DM-loaidn.md                    ← FR-VIII-07/08/09 (DM Loại DN + Hồ sơ HT/TT)
├── 05-TC-SLA.md                          ← FR-VIII-10 Cấu hình SLA (BR-SLA-01/02/04 + BR-CALC-03)
├── 06-TC-DM-tieuchi.md                   ← FR-VIII-11/12 (Tiêu chí ĐG HQ trọng số + CP)
├── 07-TC-vaitro.md                       ← FR-VIII-14 Vai trò
├── 08-TC-taikhoan.md                     ← FR-VIII-15 TK NSD + SM-TAIKHOAN 4 trạng thái
├── 09-TC-phanquyen-data.md               ← FR-VIII-16 Phân quyền DL (BR-AUTH-03/04 + ERR-PQ-01)
├── 10-TC-phanquyen-chucnang.md           ← FR-VIII-17 Phân quyền CN
├── 11-TC-dangnhap.md                     ← FR-VIII-20/21 (Tier 1 TOTP + đăng xuất + BR-AUTH-06/07)
├── 12-TC-dangky-DN.md                    ← FR-VIII-22 DN self-reg (MST + email Phương án B + cam kết)
├── 13-TC-VNeID.md                        ← FR-VIII-23/24/25 (VNeID 3 luồng + BR-AUTH-09)
├── 14-TC-quenMK.md                       ← FR-VIII-26 Quên MK / Kích hoạt TK (chống enumerate)
├── 15-TC-nhatky.md                       ← FR-VIII-28 Audit log (cap 90d, export 10K)
├── 16-TC-ngayle.md                       ← FR-VIII-29 NGAY_LE CRUD + Excel import
├── 17-TC-tinhthanh.md                    ← FR-VIII-30 DM Tỉnh/Thành 63 GSO (read-only seed)
└── (18-REVIEW-edge-case-hunter.md)       ← Optional: review bmad-review-edge-case-hunter
```

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Permission | Tổng |
|------|------:|---------:|-----:|-----------:|-----:|
| 01 - DM Lĩnh vực PL | 4 | 5 | 2 | 1 | 12 |
| 02 - 6 DM dùng TPL (Loại HT / CT HT / TT VV / Loại TK / LH TN / Kênh TN) | 6 | 6 | 2 | 1 | 15 |
| 03 - Cơ quan ĐV (tree 2 tầng) | 4 | 6 | 3 | 2 | 15 |
| 04 - DM Loại DN + Hồ sơ HT/TT | 3 | 4 | 1 | 1 | 9 |
| 05 - Cấu hình SLA | 3 | 4 | 2 | 1 | 10 |
| 06 - Tiêu chí ĐG HQ/CP (trọng số 100%) | 3 | 4 | 2 | 1 | 10 |
| 07 - Vai trò | 3 | 4 | 1 | 1 | 9 |
| 08 - TK NSD + SM 4 trạng thái | 5 | 8 | 4 | 2 | 19 |
| 09 - Phân quyền dữ liệu | 3 | 3 | 2 | 2 | 10 |
| 10 - Phân quyền chức năng | 3 | 3 | 2 | 1 | 9 |
| 11 - Đăng nhập / Đăng xuất (Tier 1) | 4 | 6 | 3 | 1 | 14 |
| 12 - DN self-reg MST | 3 | 7 | 3 | 1 | 14 |
| 13 - VNeID (3 luồng + BR-AUTH-09) | 3 | 5 | 2 | 2 | 12 |
| 14 - Quên MK / Kích hoạt TK | 3 | 6 | 3 | 1 | 13 |
| 15 - Nhật ký HT (cap 90d + export 10K) | 3 | 3 | 3 | 1 | 10 |
| 16 - Ngày lễ (CRUD + Excel import) | 3 | 4 | 2 | 1 | 10 |
| 17 - Tỉnh/Thành 63 GSO (read-only seed) | 2 | 2 | 1 | 1 | 6 |
| **TỔNG** | **58** | **80** | **38** | **21** | **197** |

**Tổng số TC: 197.** Phân bổ priority:

| Priority | Số TC | % | Quy tắc mapping (enforceable) |
|----------|------:|--:|---|
| P0 (bắt buộc) | ≈98 | 50% | (a) Happy path CRUD chính · (b) Auth/login/security/permission positive · (c) SM-TAIKHOAN transition · (d) BR-AUTH-* / BR-DATA-01 / BR-SLA-01 verify |
| P1 (quan trọng) | ≈79 | 40% | (a) Negative ERR-* validation (ERR-DM/DV/TK/PQ/VT/SLA/TC/DN/REG/VN/PWD/LOG/NL) · (b) Permission negative (role không có quyền → ERR-AUTH-01) · (c) BR business rule edge (BR-SLA-02 mức, BR-CALC-04 trọng số 100%) |
| P2 (nên có) | ≈20 | 10% | (a) Edge boundary (regex username 4/50 chars, search sanitize 200) · (b) UX (BR-UX-01 URL sync filter) · (c) Race condition / idempotency / optimistic lock |

> **Mapping rule áp dụng khi viết TC detail:** mỗi TC ID phải có cột `priority: P0/P1/P2` chốt theo bảng trên. Hook validate khi viết file `0X-TC-*.md`.

---

## 5. Tiêu chí PASS/FAIL

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md)

- ✅ **PASS module:** 100% P0 pass + ≥90% P1 pass + ≥70% P2 pass. SM-TAIKHOAN **8 transition cardinality / 9 trigger source** đều cover **bằng evidence screenshot** (không chỉ count). 4 BR mới (BR-AUTH-09 / BR-AUTH-USERNAME-01 / BR-AUTH-EMAIL-01 / BR-INTG-06) đều có ≥1 TC PASS. 4 BR cross-cutting bổ sung §2.1 (BR-DATA-06 / BR-EC-01 / BR-EC-13 / BR-UX-01) đều có ≥1 TC PASS.
- ❌ **FAIL module:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%, hoặc ≥1 BR mới / cross-cutting không có TC verify.
- 🚫 **BLOCKED:** không seed được NGAY_LE 2026 (→ TC-05/16 SLA qua ngày lễ không test được) HOẶC Tier 2 VNeID feature flag off (→ TC-13 happy path defer).
   - **Defer owner cho VNeID feature flag:** BA (chốt yêu cầu) + Infra (bật flag); ngày dự kiến enable: TBD (escalate). Khi flag chưa bật, log Phụ lục C `[GAP-VNEID-FLAG]`.

---

## 6. Tham chiếu

- **SRS baseline (v3.5 update):** [`input/srs-update-2026-5-5/srs-fr-10-quan-tri.md`](../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md) (2.288 dòng)
- **SRS lịch sử (v3):** [`input/srs-v3/srs-fr-10-quan-tri.md`](../../../input/srs-v3/srs-fr-10-quan-tri.md) (1.975 dòng)
- **Delta map:** [`input/srs-update-2026-5-5/_DELTA-MAP-FR10.md`](../../../input/srs-update-2026-5-5/_DELTA-MAP-FR10.md) (14 thay đổi + 5 fix V4-CHƯA-SỬA)
- **Changelog v3 → v3.5:** [`input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md`](../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) line 1129-1318
- **Thứ tự module + transition:** [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) §① FR-10
- **System overview:** [`tasks/system-overview.md`](../../../tasks/system-overview.md) §4.2 Module 1 — Quản trị hệ thống (line 165-234)
- **Accounts:** [`input/users.csv`](../../../input/users.csv) — `qtht_01..10`, `cb_*_01..10`, `9999999990/91`, `nht_01..02`, `huongcg`
- **Permission matrix:** [`output/permission-matrix.md`](../../../output/permission-matrix.md), [`output/permission-matrix-by-fr.md`](../../../output/permission-matrix-by-fr.md)
- **BA decisions (Q1-Q11 chốt 2026-05-07):** [`output/BA-report/ba-answers-fr10-2026-05-07.md`](../../../output/BA-report/ba-answers-fr10-2026-05-07.md)
- **Template:** [`output/template/test-plan-overview-template.md`](../../../output/template/test-plan-overview-template.md)
- **CLAUDE.md project rules:** §Tool routing MCP-first, §MCP-Rule 1-8, §Rule 7 Account lock fallback, §Rule 9 phân loại lỗi, §Rule 11 selector library.

---

## Phụ lục A — Ambiguity / Open issues phát hiện khi viết plan

1. **Tab Tỉnh/Thành VS DM TINH_THANH** — `02-thu-tu-module.md:185` cảnh báo file QA list 15 tab (giữ cả "Loại hình Tiếp nhận" + "Kênh tiếp nhận" — có thể trùng) trong khi SRS authoritative ghi 14 tab. Cần đối chiếu UI khi test sprint thực để xác nhận.
2. **TT 105/2020/TT-BTC Điều 5 + QĐ 124/2004/QĐ-TTg** — cite ở FR-VIII-22 + FR-VIII-30 nhưng chưa web-verify còn hiệu lực (xem delta map §D.1). Defer khi test thực — nếu MST 10 chữ số format match thực tế DN thì OK.
3. **SCR-VIII-04 vs SCR-VIII-05 ranh giới phân quyền** — SRS có riêng FR-VIII-16 (data) và FR-VIII-17 (chức năng) nhưng entity scope chồng lấn (cả 2 đều thao tác `VAI_TRO`). Khi test phân quyền dữ liệu BR-AUTH-03/04 cross-unit, cần thận trọng matrix `vai_tro × don_vi` riêng với mapping `vai_tro × quyen_han`.
4. **Tập ký tự đặc biệt cụ thể trong policy mật khẩu** — `[GAP-VIII-04]` mở. SRS không quote regex cụ thể (vd `!@#$%^&*()_+-=[]{}|;:,.<>?`). Khi test TC mật khẩu yếu, dùng test data `Abc12345` (thiếu special) vs `Abc@1234` (đủ) — BA chốt regex khi log bug nếu UI accept khác.
5. **`MAU_PHAN_HOI` thuộc SCR-VIII-06 hay FR-02** — SRS update 2026-05-02 BA chốt Mô hình B Hybrid với 3 phạm vi (TW_QUOC_GIA / BN_RIENG / DP_RIENG). Quyền QTHT chỉ R, CB_NV CRUD. Cross-ref FR-II-NEW-02 ở `srs-fr-02-hoi-dap.md` — chờ Pha 3 cross-file consistency check (delta map §D.2 Q5).
6. **SLA Cấu hình "4 loại yêu cầu"** — `02-thu-tu-module.md:208` ghi "Hỏi đáp / Vụ việc / Hồ sơ HT / Hồ sơ TT". Tuy nhiên `_DELTA-MAP-FR10.md` line 156 BR-SLA-01 nhắc thêm "**FR-12 Tư vấn chuyên sâu**". Loại thứ 4 thực sự là Hồ sơ TT hay TV chuyên sâu — cần verify khi test UI thực.
7. **CHO_PHAN_QUYEN còn dùng cho ai sau Q3?** — Delta map §D.2 Q1 mở. Test plan này giả định SM 4 trạng thái (theo BA chốt 2026-05-07 Q3). Nếu thực tế DB có TK ở state cũ, log thành bug data migration.
8. **CHO_KICH_HOAT → VO_HIEU_HOA auto 7-ngày** SRS `:2125` FR Ref trống. Ai own cron job auto-expire? Defer escalate BA — nếu không có FR ref → không TC ownership.
9. **Password regex tập ký tự đặc biệt** `[GAP-VIII-04]` — Phụ lục A §4 đề xuất test data `Abc@1234` vs `Abc12345` chưa có BA sign-off. **Hành động:** escalate BA chốt regex TRƯỚC khi viết TC `08-TC-taikhoan.md`. CẤM log bug FE password validation khi BA chưa chốt.
10. **AUDIT_LOG role check** `:1369` ERR-LOG-01 implies có check role nhưng SRS không list role cụ thể có quyền R. `LD_BTP` quyền R audit là suy luận từ ngữ nghĩa "lãnh đạo BTP" — chờ BA chốt.

---

## Phụ lục B — File naming consistency (suggestion)

> Suggestion từ review: hiện tại file có prefix lẫn lộn `0X-TC-DM-<entity>` (DM=danh mục) vs `0X-TC-<entity-slug>` (vaitro, taikhoan). Defer rename khi viết TC detail — giữ tên hiện tại trong §3 để tránh broken link cross-file. Sau khi viết hết 17 file, batch rename + update todo.md ref.

---

## Phụ lục C — GAP register + Missing ERR codes + Defer owners

### C.1 GAP register (consolidate `[GAP-VIII-*]` rải rác)

| GAP ID | Mô tả | Owner | Dự kiến chốt |
|--------|-------|-------|---------------|
| GAP-VIII-02 | Audit log role check role nào có quyền R (SRS ERR-LOG-01 implies role nhưng không list) | BA | Trước TC-15 |
| GAP-VIII-04 | Password regex tập ký tự đặc biệt cụ thể (SRS không quote regex) | BA | Trước TC-08 |
| GAP-VIII-05 | NGAY_LE Excel import file schema + row corrupt error code | BA + Dev BE | Trước TC-16 |
| GAP-AUDIT-ROLE | LD_BTP có quyền R AUDIT_LOG hay không (Sub-table A §2.3.1) | BA | Trước TC-15 |
| GAP-CHO-PQ-MIGRATION | TK ở state CHO_PHAN_QUYEN cũ (pre-Q3) còn không sau migration | Dev BE + DBA | Trước TC-08 |
| GAP-AUTO-EXPIRE-OWNER | Cron job auto VO_HIEU_HOA sau 7-ngày token expire — FR ref nào? | BA | Trước TC-08 |
| GAP-VNEID-FLAG | Tier 2 VNeID feature flag chưa bật. Owner enable: BA + Infra | BA + Infra | TBD |
| GAP-EXPORT-10K-ERR | SRS không define error code khi export Excel vượt 10K | BA + Dev BE | Trước TC-15 (audit) + TC-01..09 (DM/DV export) |
| GAP-EXCEL-IMPORT-SCHEMA-ERR | SRS FR-VIII-29 không define error code khi Excel import file sai schema / row corrupt | BA + Dev BE | Trước TC-16 |

### C.2 Missing ERR codes — escalate BA

Theo review feedback, các edge case sau hứa test §4 NHƯNG SRS không define error code:

| TC liên quan | Edge case | Missing ERR | Hành động |
|---|---|---|---|
| TC-15 (audit export) | Export Excel vượt 10.000 dòng | KHÔNG có ERR-LOG-03 / WARN | Escalate BA, defer assert cụ thể message tới khi BA chốt |
| TC-16 (NGAY_LE import) | Excel import file sai schema (column mismatch) | KHÔNG có ERR-NL-04 | Escalate BA + Dev BE |
| TC-16 (NGAY_LE import) | Excel import có row corrupt (`ngay` not date, `nam` not int) | KHÔNG có ERR-NL-05 | Escalate BA + Dev BE |
| TC-01..09 (DM export) | Mọi DM export vượt 10K | KHÔNG có | Escalate BA |

**CẤM tester tự nghĩ ERR code mới.** Mark TC defer + log GAP-EXPORT-10K-ERR / GAP-EXCEL-IMPORT-SCHEMA-ERR.

### C.3 Cross-module workflow dependency (Phase 3)

Phase 3 workflow integration test cross-module (review suggestion §2.6):

| Cross-FR scenario | Trigger module | Verify ở FR-10 |
|---|---|---|
| FR-IV-07 tạo TVV → auto-tạo TAI_KHOAN | FR-04 | TAI_KHOAN row mới + username = local-part email + state CHO_KICH_HOAT |
| FR-IV-NHT-01 tạo NHT → auto-tạo TAI_KHOAN | FR-04 | Tương tự, username CB NV nhập tay |
| FR-VIII-22 DN self-reg → audit log entry | FR-10 self | AUDIT_LOG INSERT row `entity=TAI_KHOAN`, `action=CREATE` |
| FR-IV/V/VI mọi CUD → audit log | FR-04/05/06 | AUDIT_LOG INSERT mọi action ở mọi module |

> Phase 3 test depend FR-04 test plan ready. Trigger khi FR-04 test plan sign-off.

