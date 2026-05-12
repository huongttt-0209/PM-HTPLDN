# Kế Hoạch Kiểm Thử — Dashboard (FR-01, SCR-I-01)

> **Phiên bản**: 1.1 (revised post-review 2026-05-12 15:10:00 — fix 10 gap + apply 8 suggestion)
> **Ngày tạo**: 2026-05-12 14:30:00 · **Ngày sửa**: 2026-05-12 15:10:00
> **Nguồn dữ liệu**: LOCAL — `input/srs-v3/srs-fr-01-dashboard.md` (baseline 724 dòng) + `input/srs-update-2026-5-5/srs-fr-01-dashboard.md` (v3.5 delta 1167 dòng)
> **SRS Reference**: FR-I-01 đến FR-I-09 + FR-I-CROSS-02 + KPI-S-01/S-02 + TPL-DASH-KPI, SCR-I-01
> **Module classification**: M (Medium) — nhóm C (IMPACT only — read-only, 1 SCR). Phạm vi test: sample 2-3 KPI đại diện + 2 chart + permission + filter rules + auto-refresh + drill-down. KHÔNG retest module upstream (FR-02/05/03/04/06/08).
> **SOURCE MODE**: LOCAL — cite line cụ thể prefix `srs-v3/srs-fr-01-dashboard.md:NN` hoặc `srs-update-2026-5-5/srs-fr-01-dashboard.md:NN` (line đơn, không range).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Module:** FR-01 Dashboard (Nhóm I). 11 FR (FR-I-01 → FR-I-09 + FR-I-CROSS-02 + KPI bổ sung S-01/S-02) — UC1 đến UC9.
- **Đặc thù:** Read-only, không CUD. Scoped theo `don_vi_id` (BR-AUTH-08). Tự làm mới 60 giây + Page Visibility API (pause khi tab ẩn — `srs-update-2026-5-5/srs-fr-01-dashboard.md:114`). Click thẻ KPI → drill-down module chi tiết.
- **Bảng dữ liệu chính:** KHÔNG có entity riêng — đọc tổng hợp từ `HOI_DAP`, `VU_VIEC`, `KHOA_HOC`, `TU_VAN_VIEN`, `KET_QUA_DANH_GIA`, `KET_QUA_DAO_TAO`, `CAU_HINH_SLA`, `DON_VI`, `TAI_KHOAN`.
- **Màn hình:** SCR-I-01 — Tổng quan hệ thống. 5 vùng: Toolbar / Filter / KPI row 1 (4 thẻ) / KPI row 2 (5 thẻ) / Chart row (UC8 trái + UC8 phải + UC9).
- **Lớp test theo `02-thu-tu-module.md`:** LỚP 5 (tổng hợp & đầu ra). Login mọi role (theo BR-AUTH-08). Không có transition — chỉ đọc.
- **Tổng số thẻ widget:** 12 (9 KPI + 3 chart pane: UC8 trái, UC8 phải, UC9).

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity nguồn | File Test Case |
|---|--------|----------|--------------|--------------|----------------|
| 1 | FR-I-01 | UC1 | KPI-01 Hỏi đáp mới | HOI_DAP (state=`MOI`) | `01-TC-kpi-01.md` |
| 2 | FR-I-02 | UC2 | KPI-02 Vụ việc đã tiếp nhận | VU_VIEC (ngày tiếp nhận) | `02-TC-kpi-02.md` |
| 3 | FR-I-03 | UC3 | KPI-03 Vụ việc đang hỗ trợ (5 state sống) | VU_VIEC | `03-TC-kpi-03.md` |
| 4 | FR-I-04 | UC4 | KPI-04 Vụ việc hoàn thành | VU_VIEC (state=`HOAN_THANH`) | `04-TC-kpi-04.md` |
| 5 | FR-I-05 | UC5 | KPI-05 Khóa học đang diễn ra | KHOA_HOC (`DANG_DIEN_RA`) | `05-TC-kpi-05.md` |
| 6 | FR-I-06 | UC6 | KPI-06 Khóa học đã kết thúc | KHOA_HOC (`DA_KET_THUC`) | `06-TC-kpi-06.md` |
| 7 | FR-I-07 | UC7 | KPI-07 CG/TVV đang hoạt động | TU_VAN_VIEN (`DANG_HOAT_DONG`) | `07-TC-kpi-07.md` |
| 8 | FR-I-08 | UC8 | 2 biểu đồ cột song song (điểm ĐG + tỷ lệ SLA) | KET_QUA_DANH_GIA + VU_VIEC + CAU_HINH_SLA | `08-TC-chart-uc8.md` |
| 9 | FR-I-09 | UC9 | Biểu đồ vành chất lượng đào tạo | KET_QUA_DAO_TAO | `09-TC-chart-uc9.md` |
| 10 | KPI-S-01 | cross | Tỷ lệ vụ việc phải bổ sung | VU_VIEC (lịch sử state) | `10-TC-kpi-s-01.md` |
| 11 | KPI-S-02 | cross | Thời gian xử lý trung bình | VU_VIEC (ngày LV) | `11-TC-kpi-s-02.md` |
| 12 | FR-I-CROSS-02 | cross | Tự làm mới 60s + per-widget fail + Page Visibility | — | `12-TC-auto-refresh.md` |
| 13 | SCR-I-01 | cross | Filter Năm + Tháng + L1 + L2 (Áp dụng / Trở về mặc định) + DB rỗng + legacy URL | DON_VI | `13-TC-filter.md` |
| 14 | SCR-I-01 | cross | Drill-down 7 KPI → module chi tiết (giữ filter) + legacy URL deprecate | URL params | `14-TC-drill-down.md` |
| 15 | SCR-I-01 | cross | Permission matrix + chip phạm vi + scope data + BN/ĐP cross-block | DON_VI / TAI_KHOAN | `15-TC-permission.md` |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại | Negative — redirect/lock expected |
|------|-----|-----------------------|-------------------|-----------------------------------|
| QTHT | — | `qtht_01` (primary) · `qtht_02` fallback · `qtht_03` permission | DASHBOARD_VIEW + đổi L1/L2 tự do như TW | — |
| CB_NV_TW | TW | `cb_nv_tw_01` · `_02` · `_03` | Filter mở L1/L2 — scope all + cross-module integration | — |
| CB_PD_TW | TW | `cb_pd_tw_01` · `_02` · `_03` | Permission Phê duyệt TW xem all | — |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH) · `_02` (BTC) · `_03` (BCT) | Filter L1/L2 khóa = BN của user — verify BR-AUTH-08 | L1=DP khóa, dropdown disabled (TC-15.10) |
| CB_PD_BN | BN | `cb_pd_bn_01` (BKH) · `_02` (BTC) | Phê duyệt BN scope BN mình | L1=DP khóa |
| CB_NV_DP | ĐP | `cb_nv_dp_01` (AG) · `_02` (BG) · `_03` (BNI) | Filter L1/L2 khóa = ĐP của user — verify cross-unit = 0 rows | L1=BN khóa |
| CB_PD_DP | ĐP | `cb_pd_dp_01` (AG) · `_02` (BG) | Phê duyệt ĐP scope ĐP mình | L1=BN khóa |
| DN | — | `9999999990` (HN) · `9999999991` (BG) | Permission negative — không có quyền `DASHBOARD_VIEW` | Redirect `/cong-doanh-nghiep` (S3) |
| NHT | — | `nht_01` (AG) · `nht_02` (DN) | Permission negative — view riêng (Nhóm IV), không có `DASHBOARD_VIEW` | Redirect `/vu-viec/cua-toi` (S3) |
| TVV/CG | — | `huongcg` | Permission negative — view riêng vụ việc được phân (Nhóm IV/V) | Redirect `/vu-viec/cua-toi` (S3) |
| admin | root | `admin` | Smoke regression (không fallback, STOP nếu lock) | — |

> Reference: `input/users.csv` (66 account, schema 11 cột), `input/test-accounts-isolation.csv`, `output/permission-matrix.md`.

### 1.4 Test data prerequisite checklist (S5 — onboard guide)

Trước khi run bất kỳ TC nào, verify 9 entity upstream × state — query qua MCP `list_network_requests` hoặc curl BE:

- ☐ ≥1 `HOI_DAP` state=`MOI` ĐP-AG (FR-02 task seed HD-001) — phục vụ TC-01.x.
- ☐ ≥3 `VU_VIEC` `ngay_tiep_nhan` trong kỳ filter ĐP-AG (FR-05 workflow R-VV-001) — TC-02.x.
- ☐ ≥1 `VU_VIEC` state ∈ {`DA_TIEP_NHAN`, `DANG_KIEM_TRA`, `YEU_CAU_BO_SUNG`, `DA_PHAN_CONG`, `DANG_XU_LY`} ĐP-AG (FR-05 R-VV-002) — TC-03.x. **Nếu thiếu state nào → split sub-task, không gộp.**
- ☐ ≥3 `VU_VIEC` `HOAN_THANH` BN-BKH với `ngay_hoan_thanh` trong kỳ (FR-05 R-VV-003) — TC-04.x + TC-10.x + TC-11.x.
- ☐ ≥4 `KHOA_HOC` `DANG_DIEN_RA` ĐP-AG (FR-03 R-DT-001) — TC-05.x.
- ☐ ≥3 `KHOA_HOC` `DA_KET_THUC` `ngay_ket_thuc` trong kỳ ĐP-AG (FR-03 R-DT-002) — TC-06.x.
- ☐ ≥4 `TU_VAN_VIEN` `DANG_HOAT_DONG` + ≥2 `TAM_DUNG` ĐP-AG (FR-04 R-TVV-001) — TC-07.x.
- ☐ ≥5 `KET_QUA_DANH_GIA` với `diem_tong` 0-100 cho VV `HOAN_THANH` (FR-08 R-DG-001) — TC-08.x.
- ☐ ≥12 `KET_QUA_DAO_TAO` với `xep_loai`+`diem_kiem_tra` (FR-03 R-DT-003) — TC-09.x.
- ☐ `CAU_HINH_SLA` config thời hạn ngày LV cho ≥1 LV (FR-10 QTHT R-SLA-001) — TC-08.2 + TC-11.x.
- ☐ DON_VI tree 3 cấp (TW + ≥1 BN + ≥1 ĐP, đã có sẵn FR-10) — TC-13/15.x.
- ☐ Audit log lịch sử state cho VV Y-1 tháng 12 (cần FR-05 seed historical) — TC-01.3 + TC-03.4 trend chéo năm (G9).

> Nếu task gốc upstream chưa PASS, mark TC tương ứng = 🚫 nhóm E (`[need: ≥N entity state X]` per Rule 2).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|-------|---------------------|---------------------|-----------|
| BR-AUTH-01 | Xác thực bắt buộc. **v3.5 đổi 3-tier → 2-tier:** Tier 1 nội bộ (TOTP qua email) cho QTHT/CB; Tier 2 SSO VNeID OIDC cho DN/TVV/CG/NHT. KHÔNG còn VNPT eKYC. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:1133` | ✅ Yes | "API outbound không yêu cầu session" | TC-15.1 precondition login |
| BR-AUTH-03 | BN chỉ thấy dữ liệu BN mình. ĐP chỉ thấy dữ liệu ĐP mình. BN ↔ ĐP không thấy nhau. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:1139` | ✅ Yes | "QTHT thấy tất cả" | TC-15.2/15.3 cross-unit |
| BR-AUTH-04 | **v3.5 chốt 2-tier ngang cấp song song:** Chỉ TW thấy cấp con. BN/ĐP không có cấp con trực thuộc. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:1145` | ✅ Yes | — | TC-15.4 TW aggregate + TC-15.10 BN/ĐP cross-block (G10) |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` cho MỌI bảng có cột này. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:1151` | ✅ Yes | "QTHT exception. AUDIT_LOG không phân quyền" | TC-15.5/15.6 isolation |
| BR-SLA-05 | **v3.5 sửa công thức tránh tỷ lệ ảo:** Tỷ lệ tuân thủ = "Hoàn thành đúng hạn" ÷ ("Hoàn thành" + "Đang xử lý đã quá hạn") × 100%. Mẫu số gồm cả vụ tồn đọng đã quá hạn để tránh hiển thị 100% khi đơn vị có nhiều vụ quá hạn chưa đóng. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:1157` | ✅ Yes (cho UC8 biểu đồ phải) | — | TC-08.2/08.3 SLA formula |
| BR-CALC-03 | Deadline = ngày tiếp nhận + N ngày làm việc (Thứ 2-6, trừ lễ). N lấy từ `CAU_HINH_SLA`. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:1163` | ✅ Yes (KPI-S-02) | — | TC-11.1/11.2 ngày LV |
| BR-DATA-07 | Pagination default 20, max 100. | `srs-v3/srs-v3.md:3978` | ⚠️ KHÔNG áp dụng trực tiếp | "Dashboard read-only, không list pagination" | — (skip) |
| BR-EC-13 | Search sanitize max 200 ký tự. | `srs-v3/srs-v3.md:4078` | ⚠️ KHÔNG áp dụng | "Dashboard không có search input" | — (skip) |
| BR-DATA-05 | Audit trail CUD. | `srs-v3/srs-v3.md:3976` | ⚠️ KHÔNG áp dụng | "Read-only, không CUD" | — (skip) |
| BR-FILTER-TIME (module-specific) | **v3.5 mới:** Filter thời gian = Năm (bắt buộc, ∈ [năm bắt đầu sử dụng, năm hiện tại]) + Tháng (NULL "Tất cả" hoặc 1-12). Tháng tương lai làm mờ khi Năm = năm hiện tại. URL param không hợp lệ → tự đổi về mặc định ngầm. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:740` | ✅ Yes | — | TC-13.1/13.2/13.3 filter validation + TC-13.7 DB rỗng (G2) |
| BR-FILTER-DONVI (module-specific) | **v3.5 mới:** Filter đơn vị 2 cấp: L1 `don_vi_cap` ∈ {DP, BN} (bắt buộc) + L2 `don_vi_id` (NULL = "Tất cả [cấp L1]"). User TW/QTHT đổi L1/L2 tự do. User BN/ĐP khóa = đơn vị user. KHÔNG có trạng thái trộn cấp DP + BN cùng lúc. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:192` | ✅ Yes | — | TC-13.4/13.5/13.6 + TC-15 perm |
| BR-KPI-CLASSIFY (module-specific) | **v3.5 mới:** Phân biệt 2 loại KPI: (a) **Phát sinh trong kỳ** (KPI-01/02/04/06, S-01, S-02) — đếm bản ghi có trường ngày nằm trong khoảng đầu kỳ–cuối kỳ; (b) **Ảnh chụp tại cuối kỳ** (KPI-03/05/07) — đếm trạng thái sống tại mốc cuối kỳ. KHÔNG dùng khoảng thời gian cho ảnh chụp. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:193` | ✅ Yes | — | TC-03.x/05.x/07.x snapshot semantics |
| BR-TREND (module-specific) | **v3.5 mới:** Xu hướng so kỳ trước theo lịch hành chính. Tháng > 1 → cùng năm tháng N-1. Tháng = 1 → năm Y-1 tháng 12 (chéo năm). Tháng "Tất cả" → cả năm Y-1. Kỳ trước = 0 và kỳ này > 0 → "—". Cả hai = 0 → "—". Nhật ký lịch sử không đủ → "—" + tooltip "Chưa đủ dữ liệu lịch sử để so sánh". | `srs-update-2026-5-5/srs-fr-01-dashboard.md:195` | ✅ Yes | — | TC-01.3/03.4 trend chéo năm + TC-01.4 audit-log insufficient (G9) |
| BR-REFRESH-WIDGET (module-specific) | **v3.5 mới:** Per-widget fail isolation. 12 nguồn gọi song song. Timeout 30s/widget → trạng thái lỗi cục bộ (28/29). ≥50% widget lỗi 3 chu kỳ liên tiếp → banner Trạng thái 30 + dòng phụ retry message. Kỳ đã đóng (`is_qua_khu_dong=true`) → tạm dừng + ẩn cả nút "Làm mới" và nhãn cập nhật. Tab ẩn (Page Visibility) → pause auto-refresh, resume khi tab active. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:648` + `:114` | ✅ Yes | — | TC-12.x auto-refresh + TC-12.5 Page Visibility (G5) |
| BR-DRILLDOWN (module-specific) | **v3.5 mới:** Click thẻ KPI → drill-down giữ filter `nam`, `thang`, `don_vi_cap`, `don_vi_id`. Module target tự suy ra boundary từ `nam`+`thang`. URL spec rõ ràng cho 7 KPI có drill-down (KPI-01..07). KPI-S-01/S-02 không có drill-down. Legacy URL `?tu_ngay=...&den_ngay=...` → auto-default. | `srs-update-2026-5-5/srs-fr-01-dashboard.md:246` + `:768` | ✅ Yes | KPI-S-01/S-02 không drill-down (SRS quote line 585 + 614) | TC-14.x drill-down + TC-14.5 legacy URL deprecate (G7) |
| BR-SAMPLE-SMALL (module-specific) | **v3.5 mới:** Cột/lát N<10 phải kèm dấu `*` + tooltip "Lưu ý: mẫu nhỏ (< 10 {tên đối tượng}) — kết quả tham khảo". Áp dụng cho UC8 trái (đánh giá), UC8 phải (SLA — vụ việc), UC9 (đào tạo — học viên). | `srs-update-2026-5-5/srs-fr-01-dashboard.md:487` | ✅ Yes | — | TC-08.4 UC8 trái N<10 + TC-08.5 UC8 phải N<10 + TC-09.2 UC9 N<10 (G6) |

> **Bổ sung BR specific module:** v3.5 (13 thay đổi nội dung B1+B2d) đã tách rõ KPI phát sinh vs ảnh chụp, filter 2 cấp đơn vị, công thức trend chéo năm, công thức SLA non-inflated. KHÔNG có thay đổi loại A (Thay đổi đối tác).

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Severity |
|--------|-------------------|----------------------|----------|
| INFO-DASH-01 | KPI không có dữ liệu trong kỳ + phạm vi | "Chưa có dữ liệu trong kỳ" (v3.5 đổi từ "Chưa có dữ liệu" v3) | INFO |
| INFO-DASH-02 | UC8 không có dữ liệu đánh giá | "Chưa có dữ liệu trong kỳ" + biểu đồ trống | INFO |
| INFO-DASH-03 | UC9 không có dữ liệu đào tạo | "Chưa có dữ liệu trong kỳ" + donut trống | INFO |
| INFO-TREND-INSUFFICIENT | Audit log lịch sử Y-1 không đủ | "Chưa đủ dữ liệu lịch sử để so sánh" (tooltip — `srs-update-2026-5-5/...:195`) | INFO |
| ERR-DASH-01 | (Đã loại bỏ v3.5 — filter v3.5 không còn tu_ngay/den_ngay) | — | — |
| ERR-DASH-02 | Lỗi truy vấn widget | "Lỗi tải dữ liệu" (trạng thái 28/29 per widget) | ERROR |
| ERR-DASH-30 | ≥50% widget lỗi trong 3 chu kỳ | "Đã thử lại 3 lần không thành công. Liên hệ quản trị viên nếu vấn đề tiếp diễn." | ERROR |

> ⚠️ Message phải quote nguyên văn `srs-update-2026-5-5/srs-fr-01-dashboard.md:221, :464, :540, :654`. Khi test negative, expected match exact.

### 2.3 Permission Matrix (module-specific)

> Reference: `output/permission-matrix.md` + `srs-update-2026-5-5/srs-fr-01-dashboard.md:682` (quyền `DASHBOARD_VIEW`).

| Role / Quyền | DASHBOARD_VIEW | Đổi L1/L2 | Scope data hiển thị | Chip phạm vi (label cần verify trên UI) |
|--------------|:--:|:--:|---|---|
| QTHT | ✅ | ✅ tự do | Toàn quốc (giống TW) | ⚠️ G4: label không quote rõ trong SRS — verify UI exact text (suy luận = "Tất cả địa phương" giống TW; BA confirm) |
| CB_NV_TW | ✅ | ✅ tự do | Toàn quốc TW + BN + ĐP | "Phạm vi: Tất cả địa phương" (default L1=DP) (`srs-update-2026-5-5/...:686`) |
| CB_PD_TW | ✅ | ✅ tự do | Toàn quốc TW + BN + ĐP | Giống CB_NV_TW |
| CB_NV_BN | ✅ | 🚫 khóa | Chỉ BN của user (BR-AUTH-08) | "Phạm vi: {tên BN của user}" |
| CB_PD_BN | ✅ | 🚫 khóa | Chỉ BN của user | "Phạm vi: {tên BN của user}" |
| CB_NV_DP | ✅ | 🚫 khóa | Chỉ ĐP của user | "Phạm vi: {tên ĐP của user}" |
| CB_PD_DP | ✅ | 🚫 khóa | Chỉ ĐP của user | "Phạm vi: {tên ĐP của user}" |
| DN | 🚫 | — | Redirect `/cong-doanh-nghiep` (Nhóm VII) (S3) | — |
| TVV | 🚫 | — | Redirect `/vu-viec/cua-toi` (Nhóm IV/V) (S3) | — |
| CG | 🚫 | — | Redirect `/vu-viec/cua-toi` (S3) | — |
| NHT | 🚫 | — | Redirect `/vu-viec/cua-toi` (Nhóm IV) (S3) | — |
| Chưa đăng nhập | 🚫 | — | Redirect `/login` (BR-AUTH-01) | — |

### 2.4 UI Layout (SCR-I-01)

**Components (trích từ `srs-update-2026-5-5/srs-fr-01-dashboard.md:697` đến `:883`):**

- **Vùng 1 — Toolbar:** Breadcrumb "Trang chủ > Tổng quan" + Tiêu đề "Tổng quan hệ thống" + Nút "Làm mới" (có chỉ dấu loading) + Nhãn "Cập nhật lúc HH:mm" + Chip phạm vi.
- **Vùng 2 — Bộ lọc:** Dropdown Năm (#6, bắt buộc) + Dropdown Tháng (#7, "Tất cả" hoặc 1-12) + Dropdown Cấp đơn vị L1 (#8, {DP, BN}) + Dropdown Đơn vị L2 (#9) + Nút "Áp dụng" (#10) + Nút "Trở về mặc định" (#11). **Không auto-apply — phải nhấn "Áp dụng".**
- **Vùng 3 — KPI hàng 1 (4 thẻ):** KPI-01 Hỏi đáp mới · KPI-02 VV tiếp nhận · KPI-03 VV đang hỗ trợ · KPI-04 VV hoàn thành.
- **Vùng 4 — KPI hàng 2 (5 thẻ):** KPI-S-01 Tỷ lệ HS bổ sung · KPI-S-02 Thời gian xử lý TB · KPI-07 Tổng CG/TVV · KPI-05 ĐT đang diễn ra · KPI-06 ĐT đã kết thúc. (Thứ tự v3.5: chất lượng VV → người xử lý → đào tạo người xử lý.)
- **Vùng 5 — Khu biểu đồ:** UC8 trái (biểu đồ cột — Điểm đánh giá HQ thang 0-100) · UC8 phải (biểu đồ cột — Tỷ lệ tuân thủ thời hạn %) · UC9 (biểu đồ vành — Đạt/Không đạt + nhãn trung tâm "Điểm trung bình: X.X/10" + chú thích "Dựa trên N học viên").
- **Trạng thái đặc biệt:**
  - Skeleton loading (đang tải).
  - Trạng thái 28/29: lỗi cục bộ widget (timeout 30s hoặc gọi fail).
  - Trạng thái 30: banner toàn dashboard khi ≥50% widget lỗi.
  - Trạng thái trống: "Chưa có dữ liệu trong kỳ".
  - Tab ẩn (Page Visibility) → pause auto-refresh (`srs-update-2026-5-5/...:114`).

**Cross-cutting features MẶC ĐỊNH (theo BR global) — VERIFY có/không:**
- ☐ Nút [Xuất Excel] — **KHÔNG có** (Dashboard read-only, không phải CRUD list — SRS không nhắc).
- ☐ Pagination — **KHÔNG có** (không phải list).
- ☐ Search box — **KHÔNG có** (không phải module CRUD).
- ☐ URL sync filter — **CÓ** theo BR-FILTER-TIME + BR-FILTER-DONVI (params `nam`, `thang`, `don_vi_cap`, `don_vi_id`).
- ☐ Audit log CUD — **KHÔNG có** (read-only).

**Feature module KHÔNG có (cần QUOTE SRS):**
- KPI-S-01 / KPI-S-02 không có drill-down — SRS `srs-update-2026-5-5/srs-fr-01-dashboard.md:585` + `:614` quote: "Drill-down: không có (chỉ số tổng hợp, không có danh sách chi tiết tương ứng)".
- Nút "Xóa bộ lọc" v3 đã được v3.5 đổi tên thành **"Trở về mặc định"** + xác nhận ngay (không cần bấm "Áp dụng").

### 2.5 State Machine (nếu có)

**Không có state machine owned bởi Dashboard** (`srs-update-2026-5-5/srs-fr-01-dashboard.md:1099`). Dashboard read-only — không thực hiện chuyển trạng thái. Module đọc lifecycle entity upstream:

- SM-HOIDAP (9 trạng thái) — đếm `MOI` cho KPI-01.
- SM-VUVIEC (12 trạng thái) — đếm 5 state sống cho KPI-03 (`DA_TIEP_NHAN`, `DANG_KIEM_TRA`, `YEU_CAU_BO_SUNG`, `DA_PHAN_CONG`, `DANG_XU_LY`) (`srs-update-2026-5-5/...:293`); state `HOAN_THANH` cho KPI-04 và KPI-S-01/S-02; state `MOI_TAO`+`CHO_TIEP_NHAN` không tính (chưa vào quy trình sống). **G1 note: v3 baseline (`srs-v3/srs-fr-01-dashboard.md:423`) chỉ quote tập 3 state qua URL drill-down `?trang_thai=DANG_XU_LY` (single state), KHÔNG quote nguyên văn 3-state set — plan suy luận từ context UC3. v3.5 quote rõ 5 state → MARK delta CHECKED (interpret v3, exact v3.5). BA confirm Q3 dưới.**
- SM-KHOAHOC (9 trạng thái) — đếm `DANG_DIEN_RA` (KPI-05), `DA_KET_THUC` (KPI-06) v3.5 đổi naming từ `KET_THUC` v3.
- SM-TVV (9 trạng thái) — đếm `DANG_HOAT_DONG` (KPI-07).

> ⚠️ v3.5 ngừng đặc tả state list cho `KET_QUA_DANH_GIA` / `KET_QUA_DAO_TAO` — đây là entity data record, không có lifecycle state (chỉ có `diem_tong`, `xep_loai`).

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| GĐ 1 Seed (pure entry state) | `input/data/seed-fixture.yaml` | KHÔNG có entity riêng cho Dashboard. Test dùng data sinh từ module upstream. |
| GĐ 2 Workflow | `input/flow-module.md` §FR-01 + §4.18 system-overview | "Read-only — không seed riêng. Seed xong các module upstream là Dashboard tự có số." (`tasks/system-overview.md:560`) |
| Cross-module map | `input/data/entity-map.md` | Verify entity nguồn đọc tại SCR-I-01 |

**Upstream dependencies (Tier check — theo `02-thu-tu-module.md:967`):**

| Entity nguồn | Tier (LỚP) | Phụ thuộc entity nào | Seed trước tại module |
|--------------|:----:|----------------------|-----------------------|
| HOI_DAP | 3 | DOANH_NGHIEP + TAI_KHOAN | FR-02 (Hỏi đáp) — state `MOI` |
| VU_VIEC | 3 | DOANH_NGHIEP + TU_VAN_VIEN + CAU_HINH_SLA | FR-05 (Vụ việc) — 5 state sống cho KPI-03 + `HOAN_THANH` cho KPI-04/S-01/S-02 |
| KHOA_HOC | 3 | CHUONG_TRINH_DAO_TAO + GIANG_VIEN | FR-03 (Đào tạo) — `DANG_DIEN_RA` + `DA_KET_THUC` |
| TU_VAN_VIEN | 2 | DON_VI + DANH_MUC LV | FR-04 (CG/TVV) — `DANG_HOAT_DONG` |
| KET_QUA_DANH_GIA | 4 | VU_VIEC=`HOAN_THANH` + KE_HOACH_DANH_GIA | FR-08 (Đánh giá HQ — đã rename "Theo dõi Đánh giá HQ HTPL") — có `diem_tong` 0-100 |
| KET_QUA_DAO_TAO | 4 | KHOA_HOC + TAI_KHOAN học viên | FR-03 (Đào tạo) — có `xep_loai` + `diem_kiem_tra` |
| CAU_HINH_SLA | 1 | — | FR-10 (QTHT) — config thời hạn ngày LV |
| DON_VI tree 3 cấp | 1 | — | FR-10 (QTHT) — TW + ≥1 BN + ≥1 ĐP để filter L1/L2 có option |
| AUDIT_LOG / lịch sử state VU_VIEC | — | VU_VIEC + actions | FR-05 + FR-10 — Y-1 tháng 12 data cho TC trend chéo năm |

> **Lưu ý:** Mỗi entity upstream phải đạt **state cuối** theo cột "Đọc tại Dashboard" (xem §4 entity SRS line 1008-1095). KHÔNG hardcode `N records` ở đây — workflow advance state là việc của module upstream test plan. Dashboard chỉ verify data hiển thị đúng theo state đã có.

---

## 3. Cấu Trúc File Test Case

```
fr-01-dashboard/
├── test-plan.md                         ← File này
├── 01-TC-kpi-01.md                      ← KPI-01 Hỏi đáp mới (UC1, FR-I-01)
├── 02-TC-kpi-02.md                      ← KPI-02 Vụ việc tiếp nhận (UC2, FR-I-02)
├── 03-TC-kpi-03.md                      ← KPI-03 VV đang hỗ trợ 5 state (UC3, FR-I-03)
├── 04-TC-kpi-04.md                      ← KPI-04 VV hoàn thành (UC4, FR-I-04)
├── 05-TC-kpi-05.md                      ← KPI-05 ĐT đang diễn ra (UC5, FR-I-05)
├── 06-TC-kpi-06.md                      ← KPI-06 ĐT đã kết thúc (UC6, FR-I-06)
├── 07-TC-kpi-07.md                      ← KPI-07 CG/TVV (UC7, FR-I-07)
├── 08-TC-chart-uc8.md                   ← UC8 2 biểu đồ cột (FR-I-08)
├── 09-TC-chart-uc9.md                   ← UC9 donut (FR-I-09)
├── 10-TC-kpi-s-01.md                    ← Tỷ lệ HS bổ sung (KPI-S-01)
├── 11-TC-kpi-s-02.md                    ← Thời gian xử lý TB (KPI-S-02)
├── 12-TC-auto-refresh.md                ← Tự làm mới 60s + fail per-widget + Page Visibility (FR-I-CROSS-02)
├── 13-TC-filter.md                      ← Filter Năm/Tháng/L1/L2 + URL sync + DB rỗng
├── 14-TC-drill-down.md                  ← Click KPI giữ filter → module chi tiết + legacy URL
├── 15-TC-permission.md                  ← 11 role × scope data + chip phạm vi + BN/ĐP cross-block
└── (16-REVIEW-edge-case-hunter.md)      ← Optional review
```

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Tổng |
|------|------:|---------:|-----:|-----:|
| 01-TC-kpi-01 (FR-I-01 + trend audit-log G9) | 1 | 1 | 2 | 4 |
| 02-TC-kpi-02 (FR-I-02) | 1 | 0 | 1 | 2 |
| 03-TC-kpi-03 (FR-I-03 — 5 state sống + trend chéo năm G9) | 1 | 1 | 2 | 4 |
| 04-TC-kpi-04 (FR-I-04) | 1 | 0 | 1 | 2 |
| 05-TC-kpi-05 (FR-I-05) | 1 | 0 | 1 | 2 |
| 06-TC-kpi-06 (FR-I-06) | 1 | 0 | 1 | 2 |
| 07-TC-kpi-07 (FR-I-07 — snapshot) | 1 | 0 | 2 | 3 |
| 08-TC-chart-uc8 (2 biểu đồ + BR-SLA-05 + N<10 UC8 trái & phải G6) | 2 | 1 | 3 | 6 |
| 09-TC-chart-uc9 (donut + N<10) | 1 | 1 | 1 | 3 |
| 10-TC-kpi-s-01 (no-drill, mẫu số 0) | 1 | 1 | 1 | 3 |
| 11-TC-kpi-s-02 (BR-CALC-03 ngày LV) | 1 | 0 | 2 | 3 |
| 12-TC-auto-refresh (60s + per-widget + kỳ đóng + Page Visibility G5 + banner-30 G8) | 2 | 2 | 4 | 8 |
| 13-TC-filter (Năm/Tháng/L1/L2 + URL invalid + Trở về mặc định + DB rỗng G2) | 2 | 2 | 4 | 8 |
| 14-TC-drill-down (7 KPI giữ filter + URL params + legacy URL G7) | 3 | 2 | 1 | 6 |
| 15-TC-permission (11 role + 4 scope state + chip phạm vi + BN/ĐP cross-block G10) | 4 | 5 | 1 | 10 |
| **TỔNG** | **23** | **16** | **27** | **66** |

**Phân bổ priority:**

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc) | 32 | 48% |
| P1 (quan trọng) | 24 | 36% |
| P2 (nên có) | 10 | 15% |

### 4.1 Cross-module integration TC — bảng riêng (S1)

> Trace dep theo Rule 2 CLAUDE.md `[need: ≥N entity state X]`. Khi block → mark nhóm E (dependency upstream) trong Bảng 2 report.

| TC ID | Module phụ thuộc | Upstream task ID gốc (dep) | Data state needed | Verify acceptance |
|-------|------------------|-----------------------------|-------------------|-------------------|
| TC-01.1 KPI-01 ↔ FR-02 | FR-02 (Hỏi đáp) | `[need: ≥5 HOI_DAP state=MOI ĐP-AG]` | 5 `HOI_DAP` `MOI` ngay_tao trong kỳ | Login `cb_nv_dp_01` → KPI-01 = 5 |
| TC-04.1 KPI-04 ↔ FR-05 | FR-05 (Vụ việc) | `[need: ≥3 VU_VIEC HOAN_THANH BN-BKH ngay_hoan_thanh trong kỳ]` | 3 `VU_VIEC` `HOAN_THANH` | Filter Năm=2026/Tháng=4 → KPI-04 = 3 |
| TC-05.1 KPI-05 ↔ FR-03 (S2 mới) | FR-03 (Đào tạo) | `[need: ≥4 KHOA_HOC DANG_DIEN_RA ĐP-AG mốc cuối kỳ]` | 4 `KHOA_HOC` `DANG_DIEN_RA` | Filter ĐP-AG → KPI-05 = 4 (snapshot) |
| TC-06.1 KPI-06 ↔ FR-03 (S2 mới) | FR-03 (Đào tạo) | `[need: ≥3 KHOA_HOC DA_KET_THUC ngay_ket_thuc trong kỳ ĐP-AG]` | 3 `KHOA_HOC` `DA_KET_THUC` | Filter ĐP-AG → KPI-06 = 3 |
| TC-07.1 KPI-07 ↔ FR-04 | FR-04 (CG/TVV) | `[need: ≥4 TU_VAN_VIEN DANG_HOAT_DONG + ≥2 TAM_DUNG ĐP-AG]` | 4 `DANG_HOAT_DONG` + 2 `TAM_DUNG` | KPI-07 = 4 (chỉ active). Đổi 1 → `TAM_DUNG`, reload 60s → KPI-07 = 3 |
| TC-08.2 UC8 SLA ↔ FR-05+SLA | FR-05 + FR-10 SLA | `[need: 5 đúng hạn + 2 trễ + 3 DANG_XU_LY quá hạn]` | 10 `VU_VIEC` mix | Công thức v3.5: 5÷(5+2+3)×100 = 50% (≠ v3 71%) |
| TC-09.1 UC9 ↔ FR-03 | FR-03 (Đào tạo) | `[need: ≥12 KET_QUA_DAO_TAO ĐP-AG (8 đạt + 4 không đạt)]` | 12 records | Donut 66.7%, "Điểm TB: 7.1/10", "12 học viên" |
| TC-10.1 KPI-S-01 ↔ FR-05 history | FR-05 (Vụ việc) | `[need: 10 VU_VIEC HOAN_THANH + 3 từng qua YEU_CAU_BO_SUNG (audit log)]` | 10 + 3 history | KPI-S-01 = 30% |

**Cross-module total = 8 TC** (tăng từ 6 sau S2). Exit criteria §5 cập nhật ≥7/8 PASS (S6).

---

## 5. Tiêu chí đạt/không đạt

> Reference: `output/test-strategy.md §10`

- ✅ **PASS:** 100% P0 + ≥90% P1 pass + cross-module integration ≥7/8 PASS (S6) + **ZERO TC permission scope FAIL** (extend từ TC-15.x sang mọi P0 có scope check).
- ❌ **FAIL:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%, hoặc bất kỳ TC permission scope FAIL (data leak cross-unit là Critical).

**Module nhóm C đặc thù — exit criteria bổ sung:**
- Filter v3.5 (Năm + Tháng + L1 + L2) phải PASS 100% — đây là delta lớn nhất v3 → v3.5.
- Công thức BR-SLA-05 v3.5 (mẫu số gồm "Đang xử lý đã quá hạn") phải PASS TC-08.2.
- Drill-down 7 KPI giữ filter phải PASS 100% (TC-14.x) — số click xuống khớp số đếm Dashboard.
- Auto-refresh per-widget fail isolation (FR-I-CROSS-02 bước 7) phải PASS TC-12.4 (1 widget fail không kéo theo toàn dashboard).
- Page Visibility (TC-12.5) phải PASS — pause khi tab ẩn, resume khi tab active.
- Legacy URL deprecate (TC-14.5) phải PASS — `?tu_ngay=...` → auto-default Năm/Tháng v3.5.

---

## 6. Tham chiếu

- `output/test-strategy.md` — chiến lược tổng thể QA HTPLDN.
- `output/scaling-test-strategy.md` — quy trình 7 bước onboard module mới.
- `input/srs-v3/srs-fr-01-dashboard.md` — SRS v3 baseline (724 dòng).
- `input/srs-update-2026-5-5/srs-fr-01-dashboard.md` — SRS v3.5 delta đã merge IN (1167 dòng; 13 thay đổi B1+B2d, không có loại A).
- `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` §srs-fr-01 — chi tiết 13 thay đổi.
- `tasks/system-overview.md §4.18` — M17 Dashboard (SCR-I-01) layout 5 vùng + bullet auto-refresh.
- `input/quy-trinh-nghiep-vu/02-thu-tu-module.md §⑮ FR-01` — LỚP 5, mọi role login, scope BR-AUTH-08, không transition.
- `input/data/entity-map.md` — bảng "Tạo tại / Đọc tại" 9 entity nguồn dashboard.
- `output/permission-matrix.md` — 49 entity × 11 role permission matrix.
- `output/template/test-case-template.md` — field-level TC template.
- `output/template/test-case-execution-report-template.md` — execution report.
- `output/template/bug-report-template.md` — bug report 6 sections.
- `output/template/tc-block-classification-template.md` — 6 nhóm A-F lý do block cho Bảng 2 report.
- `input/users.csv` — 66 account schema 11 cột (suffix `_01` primary, `_02` fallback, `_03` permission test per Rule 7).

---

## 7. Ambiguity / Note ngày 2026-05-12 15:10:00

**KPI definition v3 vs v3.5 — delta 13 item × coverage (S8):**

| # | Delta v3 → v3.5 | TC coverage | Trạng thái |
|:-:|---|---|:-:|
| 1 | Filter thời gian: Năm + Từ/Đến → Năm + Tháng | TC-13.1/13.2/13.3 + TC-14.5 legacy URL | ✅ covered (G7 + main) |
| 2 | Filter đơn vị: đơn cấp → 2 cấp L1+L2 | TC-13.4/13.5/13.6 + TC-15.10 cross-block | ✅ covered (G10) |
| 3 | KPI-03: 3 state → 5 state sống | TC-03.1/03.2/03.3 | ⚠️ covered (G1 — cần BA confirm Q3) |
| 4 | UC8: combo bar+line → 2 biểu đồ cột song song | TC-08.1 layout | ✅ covered |
| 5 | BR-SLA-05: mẫu số gồm "đang xử lý quá hạn" | TC-08.2/08.3 | ✅ covered |
| 6 | BR-AUTH-01: 3-tier → 2-tier (bỏ eKYC) | TC-15.1 precondition | ✅ covered |
| 7 | BR-AUTH-04: BN/ĐP ngang cấp (không trực thuộc) | TC-15.4 + TC-15.10 (G10) | ✅ covered |
| 8 | Auto-refresh: per-widget fail + banner-30 | TC-12.1..12.4 + TC-12.6 banner-30 (G8) | ✅ covered |
| 9 | KPI bổ sung đổi tên KPI-03/04 → KPI-S-01/S-02 | TC-10.x + TC-11.x | ✅ covered |
| 10 | Drill-down URL: giữ filter v3.5 | TC-14.1..14.4 + TC-14.5 legacy (G7) | ✅ covered |
| 11 | Naming: `KET_THUC` → `DA_KET_THUC` (KHOA_HOC) | TC-06.1 + TC-14.2 URL | ✅ covered |
| 12 | QTHT permission ngang TW | TC-15.7 QTHT scope | ⚠️ covered (G4 — chip label cần verify UI) |
| 13 | N<10 chú giải mẫu nhỏ | TC-08.4 UC8 trái + TC-08.5 UC8 phải (G6) + TC-09.2 UC9 | ✅ covered |
| extra | Page Visibility API pause | TC-12.5 (G5) | ✅ covered |
| extra | Trend chéo năm + audit-log insufficient | TC-01.3/01.4 + TC-03.4 (G9) | ✅ covered |

**Item cần BA confirm trước khi viết TC detail:**
- **Q1:** "Năm bắt đầu sử dụng phần mềm" được lấy động từ năm nhỏ nhất của `ngay_tao` các nhóm dữ liệu nguồn (`srs-update-2026-5-5/srs-fr-01-dashboard.md:740`). Cần BA confirm logic chính xác — nếu DB chưa có data nào thì option Năm hiển thị gì? (Mặc định = năm hiện tại?). **TC-13.7 sẽ test DB rỗng — defer thực thi nếu env không reset được (nhóm F).**
- **Q2:** Khi user TW switch L1 từ "Địa phương" → "Bộ ngành" và đang đứng ở "Tất cả ĐP" → L2 reset về "Tất cả BN" (pending). Test cần verify chính xác behavior khi user vừa switch L1 vừa đổi Năm trong cùng 1 batch trước khi nhấn "Áp dụng".
- **Q3 (G1):** v3 baseline `srs-v3/srs-fr-01-dashboard.md:423` chỉ quote URL drill-down `?trang_thai=DANG_XU_LY` (single state) cho KPI-03 — KHÔNG quote nguyên văn 3-state set. v3.5 (`:293`) quote đầy đủ 5 state. Plan đánh dấu Δ3 = "interpret v3 — exact v3.5" cho tới khi BA confirm v3 baseline state set. Trong khi đó, **TC-03.x test theo v3.5 5-state** (current spec). Nếu tester thấy mismatch khi seed FR-05 chỉ có 3 state cũ → mark ⚠️ "Cần BA confirm Δ3 v3 baseline" (nhóm C) thay vì ❌ Fail.
- **Q4 (G4):** Chip phạm vi cho QTHT — SRS v3.5 `:682` đến `:686` quote chip label cho CB role nhưng KHÔNG quote nguyên văn label cho QTHT. Cần BA confirm label = "Tất cả địa phương" hay text khác. **TC-15.7 verify UI exact text + log Δ vào bug nhóm C nếu mismatch.**

### 7.1 Risk register (S7 — input cho Bảng 2 report khi test)

| Risk | Likelihood | Impact | Mitigation / Cần làm gì |
|------|:----------:|:------:|--------------------------|
| BE chưa expose endpoint trend chéo năm (Y-1 audit log) | High | TC-01.3/01.4/03.4 block | Confirm BE expose query lịch sử state VU_VIEC qua AUDIT_LOG. Nếu chưa → nhóm B (chờ dev) hoặc nhóm F (defer) |
| Mock server timeout 30s × 3 chu kỳ cho TC-12.6 banner-30 | Medium | TC-12.6 cần ~3 phút setup mock | Infra confirm cách throttle 6/12 widget. Nếu không có → MCP `evaluate_script` mock fetch reject. Nhóm D nếu không khả thi |
| DB rỗng cho TC-13.7 (Năm dropdown) | Low | UAT đầu / env reset trigger | Tạo env clone trống + verify dropdown default. Nếu không thể reset → defer + ghi giả định BA (nhóm F) |
| Audit log lịch sử Y-1 tháng 12 cho TC trend | High | False pass nếu data thiếu | Seed Y-1 historical qua FR-05 backdate. Nếu BE không cho backdate → tooltip "Chưa đủ dữ liệu lịch sử" assert (nhóm A) |
| Chip phạm vi QTHT label không quote SRS | Low | False negative khi exact match | TC-15.7 verify UI live + log nhóm C "BA confirm chip text" |
| FR-08 rename "Theo dõi Đánh giá HQ HTPL" làm gãy link | Low | TC-08.x assert tên module | Verify mọi link drill-down KPI-08 → label mới (CR-01 batch) |

---

*Test plan revised 2026-05-12 15:10:00 — based on SRS v3 + v3.5 delta. Module FR-01 phân loại nhóm C (IMPACT only) theo Rule 4 ~/.claude/CLAUDE.md. Apply ≥80% review feedback: G1+G2+G3+G4+G5+G6+G7+G8+G9+G10 (10 gap fix) + S1+S2+S3+S4+S5+S6+S7+S8 (8 suggestion). Sau khi BA sign-off Q1/Q2/Q3/Q4 — viết TC detail từng file 01-15 theo template `output/template/test-case-template.md`.*
