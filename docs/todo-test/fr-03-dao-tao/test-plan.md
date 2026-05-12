# Kế Hoạch Kiểm Thử — Đào tạo & Tập huấn (FR-03, SCR-III-01..05)

> **Phiên bản**: 1.1
> **Ngày tạo**: 2026-05-12 11:40:00
> **Revised**: 2026-05-12 13:00:00 — fix 3 blocker review (SM-KHOAHOC state count, FR-III-21, junction vai_tro) + 3 important gap (BR-PUBLIC TC, FR-III-19 hủy công bố, HOC_VIEN seed) + 2 bảng tổng hợp placeholder.
> **SOURCE MODE**: LOCAL — đọc trực tiếp `srs-v3/srs-fr-03-dao-tao.md` (v3) + `srs-update-2026-5-5/srs-fr-03-dao-tao.md` (v3.5) + `srs-update-2026-5-5/_DELTA-MAP-FR03.md`.
> **SRS Reference**: FR-III-01 → FR-III-22 + FR-III-NEW-01/02/03, SCR-III-00 → SCR-III-05 (sub-menu 1..6), Nhóm III — Quản lý Đào tạo, Tập huấn.

---

## 0. Verdict + 2 bảng tổng hợp (placeholder cho round chạy đầu)

> **Verdict round chạy đầu (TBD):** ⏳ chưa chạy. Sau khi seed + workflow xong, fill PASS/FAIL theo §5 tiêu chí đạt.

### Bảng 1 — Trạng thái toàn bộ TC (placeholder, fill sau R1 chạy)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| (45 TC sau revise — fill sau round chạy) | | | | |
| **Tổng** | **45 TC** | ✅0 · ⚠️0 · ❌0 · 🚫0 · ⏭0 · 🤷0 | | |

### Bảng 2 — TC chưa chạy được — cần làm gì để chạy (placeholder)

> Hiện tại còn 0 TC chưa chạy được — chia 0 nhóm. Update sau round chạy đầu theo phân loại nhóm A-F (xem [tc-block-classification-template.md](../../../output/template/tc-block-classification-template.md)).

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| (fill sau khi chạy round 1) | | | |

> **Quy trình:** Theo [scaling-test-strategy.md §4.1 Bước 3](../../../output/scaling-test-strategy.md) — trích BR từ SRS local + sibling-check Hợp đồng tư vấn (FR-14), Vụ việc (FR-05). Test plan này dùng cho **GĐ 3 Functional + Auth + Edge** sau khi GĐ 1 Seed + GĐ 2 Workflow xong.

> **Bối cảnh delta v3 → v3.5 (Δ +133%, file thay đổi LỚN NHẤT batch 2026-05-05):**
> - Mô hình A 3 cấp mới: KE_HOACH_DAO_TAO (cấp 1) → CHUONG_TRINH_DAO_TAO (cấp 2) → KHOA_HOC (cấp 3) — FK `ke_hoach_id` nằm phía CTDT.
> - SM mới: **SM-KH-DAO-TAO** (5 trạng thái) + **SM-CTDT** (7 trạng thái). SM-KHOAHOC giữ nguyên 9 trạng thái v3 (Thay đổi 3 OUT).
> - Entity mới: KE_HOACH_DAO_TAO, HOC_VIEN (1:1 TAI_KHOAN qua `tai_khoan_id`), LICH_HOC (per-buổi).
> - Điểm danh đổi: boolean → **enum 3-value** (CO_MAT / VANG_PHEP / VANG_KHONG_PHEP).
> - FR-III-19 Hướng B: **BỎ cấp chứng nhận PDF** — chỉ công bố KQ vào TK học viên + chuyên trang Cổng PLQG.
> - 5 trường công khai (CR-01) áp 4 entity nhóm III: `cong_khai`, `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`.

> **Ambiguity / cần BA xác nhận:**
> - **Giảng viên entity location:** v3 đặt GIANG_VIEN trong FR-03 (FR-III-11/12, SCR-III-05). v3.5 vẫn giữ FR-III-11/12 nội bộ FR-03 NHƯNG flow-module §FR-04 cho TVV `HOAT_DONG` được dùng như giảng viên qua khóa (note rename trạng thái — TVV đổi `DANG_HOAT_DONG` → `HOAT_DONG`, **GIANG_VIEN giữ `DANG_HOAT_DONG`**). Kết luận: GIANG_VIEN là entity riêng nội bộ FR-03 (KHÔNG tách FR-04), nhưng `KHOA_HOC.giang_vien_ids` có thể populate từ TU_VAN_VIEN (FR-04) qua junction `KHOA_HOC_GIANG_VIEN`.
> - **FR-III-NEW-01/02/03** chưa rõ UI có tab riêng hay tích hợp `SCR-III-04` tab "De kiem tra" — cần verify FE build.
> - **HOC_VIEN entity riêng** chưa cover trong SCR list — note nhân account học viên qua TK doanh nghiệp / NHT (chuyên trang).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- Nhóm III — Quản lý Đào tạo, Tập huấn. Mô hình A 3 cấp (KH năm → CTDT → Khóa học) + Lịch học per-buổi + Đề kiểm tra + Giảng viên + Học viên + Đăng ký + Kết quả + Công bố.
- **22 FR** (theo v3.5: FR-III-01..20 + FR-III-NEW-01/02/03 + FR-III-22).
- **6 màn hình** (sub-menu Nhóm III v3.5):
  - SCR-III-00 Kế hoạch đào tạo năm (sub-menu 1, mới Thay đổi 1).
  - SCR-III-01 Chương trình đào tạo (sub-menu 2) + tab Đề xuất + workflow phê duyệt CTDT (Thay đổi 2).
  - SCR-III-02 Khóa học (sub-menu 3) — drill-down 7 tab: Thông tin · Lịch học · Học viên · Điểm danh · Kết quả kiểm tra · Bài giảng · Công bố kết quả.
  - SCR-III-03 Kho tài liệu / Bài giảng (sub-menu 4).
  - SCR-III-04 Ngân hàng câu hỏi & Đề kiểm tra (sub-menu 5) — 2 tab: Câu hỏi + Đề KT.
  - SCR-III-05 Giảng viên / Trợ giảng (sub-menu 6) — 2 tab: Thông tin + Lịch sử giảng dạy.

> **Ghi chú scope test plan này:** dù v3.5 có **6 màn hình**, user instruction nói "4 sub-menu" — sẽ test theo bố cục 4 sub-menu của `system-overview.md §4.10` (KH ĐT năm / Khóa đào tạo / Học viên / Giảng viên). Câu hỏi + Đề KT + Kho tài liệu sẽ test dưới dạng module phụ trợ (verify dropdown / FK / preview), không có TC độc lập.

- Bảng dữ liệu chính: `KE_HOACH_DAO_TAO`, `CHUONG_TRINH_DAO_TAO`, `KHOA_HOC`, `LICH_HOC`, `BAI_GIANG`, `NGAN_HANG_CAU_HOI`, `DE_KIEM_TRA`, `GIANG_VIEN`, `HOC_VIEN`, `DANG_KY_DAO_TAO`, `KET_QUA_DAO_TAO`, `DE_XUAT_DAO_TAO`, junction `KHOA_HOC_GIANG_VIEN`.

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity chính | Sub-menu | File TC |
|---|-------|----------|---------------|--------------|----------|---------|
| 1 | FR-III-14 | UC33 | Lập kế hoạch đào tạo năm | KE_HOACH_DAO_TAO | KH ĐT năm | `01-TC-ke-hoach-dt-nam.md` |
| 2 | FR-III-15 | UC34 | Phê duyệt kế hoạch | KE_HOACH_DAO_TAO | KH ĐT năm | `01-TC-ke-hoach-dt-nam.md` |
| 3 | FR-III-16 | UC35 | Công khai kế hoạch | KE_HOACH_DAO_TAO | KH ĐT năm | `01-TC-ke-hoach-dt-nam.md` |
| 4 | FR-III-01 | UC20 | Quản lý CTDT + Khóa học | CTDT, KHOA_HOC | Khóa đào tạo | `02-TC-khoa-dao-tao.md` |
| 5 | FR-III-02 | UC21 | Tìm kiếm CTDT | CTDT | Khóa đào tạo | `02-TC-khoa-dao-tao.md` |
| 6 | FR-III-13 | UC32 | Quản lý đề xuất đào tạo | DE_XUAT_DAO_TAO | Khóa đào tạo (tab Đề xuất) | `02-TC-khoa-dao-tao.md` |
| 7 | FR-III-17 | UC36 | Ghi nhận kết quả khóa | KET_QUA_DAO_TAO | Khóa đào tạo (tab KQ) | `02-TC-khoa-dao-tao.md` |
| 8 | FR-III-18 | UC37 | Phê duyệt kết quả | KET_QUA_DAO_TAO | Khóa đào tạo (tab KQ) | `02-TC-khoa-dao-tao.md` |
| 9 | FR-III-19 | UC38 | Công bố kết quả đào tạo | KET_QUA_DAO_TAO | Khóa đào tạo (tab Công bố) | `02-TC-khoa-dao-tao.md` |
| 10 | FR-III-20 | UC mới | Xuất file docx/PDF ký số CTDT | CTDT | Khóa đào tạo | `02-TC-khoa-dao-tao.md` |
| 10b | **FR-III-21** | **UC mới (GAP-III-08 F-05)** | **Phê duyệt khóa học** (transition CHO_DUYET → DA_DUYET cho KHOA_HOC — SRS line 1827 ghi "KHÔNG có FR riêng" → cần BA confirm có FR-III-21 độc lập hay gộp pattern FR-III-15) | KHOA_HOC | Khóa đào tạo (Tab Thông tin) | `02-TC-khoa-dao-tao.md` |
| 11 | FR-III-22 | UC mới | Quản lý Lịch học buổi dạy | LICH_HOC | Khóa đào tạo (tab Lịch học) | `02-TC-khoa-dao-tao.md` |
| 12 | FR-III-NEW-01 | UC mới | Tạo đề kiểm tra | DE_KIEM_TRA | Khóa đào tạo (phụ trợ) | `02-TC-khoa-dao-tao.md` |
| 13 | FR-III-NEW-02 | UC mới | Quản lý đề kiểm tra | DE_KIEM_TRA | Khóa đào tạo (phụ trợ) | `02-TC-khoa-dao-tao.md` |
| 14 | FR-III-NEW-03 | UC mới | Phân phối đề + map bài giảng | DE_KIEM_TRA | Khóa đào tạo (phụ trợ) | `02-TC-khoa-dao-tao.md` |
| 15 | FR-III-03 | UC22 | Quản lý đăng ký đào tạo | DANG_KY_DAO_TAO | Học viên | `03-TC-hoc-vien.md` |
| 16 | FR-III-04 | UC23 | Đăng ký tham gia học tập | DANG_KY_DAO_TAO | Học viên (chuyên trang) | `03-TC-hoc-vien.md` |
| 17 | FR-III-05 | UC24 | Quản lý kiểm tra + điểm danh | KET_QUA_DAO_TAO, LICH_HOC | Học viên | `03-TC-hoc-vien.md` |
| 18 | FR-III-06 | UC25 | Tìm kiếm kết quả | KET_QUA_DAO_TAO | Học viên | `03-TC-hoc-vien.md` |
| 19 | FR-III-11 | UC30 | Quản lý giảng viên / trợ giảng | GIANG_VIEN | Giảng viên | `04-TC-giang-vien.md` |
| 20 | FR-III-12 | UC31 | Tìm kiếm giảng viên | GIANG_VIEN | Giảng viên | `04-TC-giang-vien.md` |
| 21 | FR-III-07 | UC26 | Quản lý kho bài giảng | BAI_GIANG | (phụ trợ) | `02-TC-khoa-dao-tao.md` |
| 22 | FR-III-08 | UC27 | Tìm kiếm tài liệu | BAI_GIANG | (phụ trợ) | `02-TC-khoa-dao-tao.md` |
| 23 | FR-III-09 | UC28 | Quản lý ngân hàng câu hỏi | NGAN_HANG_CAU_HOI | (phụ trợ) | `02-TC-khoa-dao-tao.md` |
| 24 | FR-III-10 | UC29 | Tìm kiếm ngân hàng câu hỏi | NGAN_HANG_CAU_HOI | (phụ trợ) | `02-TC-khoa-dao-tao.md` |

### 1.3 Tài khoản & role liên quan

> Reference: [input/users.csv](../../../input/users.csv), [output/permission-matrix.md](../../../output/permission-matrix.md).

| Role | Cấp | Username (primary) | Fallback | Dùng cho TC loại |
|------|-----|--------------------|----------|------------------|
| QTHT | — | `qtht_01` | `qtht_02` | Admin CRUD cross-đơn vị, audit log, cấu hình ngưỡng BR-KQ-01 |
| CB_NV_TW | TW | `cb_nv_tw_01` | `cb_nv_tw_02` | CRUD KH năm / CTDT / KH cấp TW, gửi phê duyệt, công khai, ghi nhận KQ, công bố KQ |
| CB_NV_BN | BN | `cb_nv_bn_01` | `cb_nv_bn_02` | CRUD scope Bộ ngành (BKH), test data isolation cấp ngang |
| CB_NV_DP | ĐP | `cb_nv_dp_01` | `cb_nv_dp_02` | CRUD scope Sở Tư pháp (AG), test multi-tenant |
| CB_PD_TW | TW | `cb_pd_tw_01` | `cb_pd_tw_02` | Phê duyệt KH năm + CTDT + KQ cấp TW (BR-AUTH-05 cùng cấp) |
| CB_PD_BN | BN | `cb_pd_bn_01` | `cb_pd_bn_02` | Phê duyệt scope BN (cùng cấp với CB_NV_BN tạo) |
| CB_PD_DP | ĐP | `cb_pd_dp_01` | `cb_pd_dp_02` | Phê duyệt scope ĐP |
| NHT | ĐP | `nht_01` (STP-AG) | `nht_02` (STP-DN) | Chuyên trang: đăng ký HV, gửi đề xuất đào tạo, xem KQ HV |
| DN | — | (cần seed) | — | Chuyên trang: đăng ký khóa, gửi đề xuất, xem KQ |
| GIANG_VIEN | — | (cần seed qua FR-III-11) | — | Chuyên trang (nếu có UI riêng): xem khóa được phân, ghi nhận điểm danh |
| HOC_VIEN | — | (cần seed FR-III-04 qua TK DN/NHT) | — | Chuyên trang: xem KQ + chứng nhận |

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> ⚠️ Cột "Ngoại lệ SRS-quoted": chỉ điền khi SRS có dòng ngoại lệ cụ thể. Để trống = áp dụng 100%.

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|---------------------|---------------------|------------|
| BR-AUTH-01 | Xác thực bắt buộc | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1901 | ✅ Yes | — | Precondition mọi TC |
| BR-AUTH-05 | Phê duyệt cùng cấp TW/BN/ĐP | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1902 | ✅ Yes | — | TC phê duyệt KH năm (FR-III-15), CTDT (FR-III-01), KQ (FR-III-18) |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1903 | ✅ Yes | — | TC data isolation cross-đơn vị (TW vs BN vs ĐP) |
| BR-DATA-01 | Soft delete (đánh dấu `is_deleted=true`) | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1904 | ✅ Yes | — | TC DELETE KH năm / CTDT / khóa / lịch học / đề KT |
| BR-DATA-02 | Multi-tenant scoping | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1905 | ✅ Yes | — | TC list query lọc theo `don_vi_id` |
| BR-DATA-03 | Common fields (`created_at`, `created_by`, ...) | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1906 | ✅ Yes | — | TC verify field hệ thống sau CREATE |
| BR-DATA-04 | Auto-gen mã (KH-, CTDT-, ma_khoa_hoc, ...) | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1907 | ✅ Yes | — | TC verify format mã sau CREATE |
| BR-DATA-05 | Audit trail mọi CUD | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1908 | ✅ Yes | — | TC verify AUDIT_LOG INSERT cho tạo/sửa/xóa/duyệt/công khai |
| BR-DATA-06 | Export Excel max 10.000 dòng | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1909 | ✅ Yes | — | TC export KH năm + CTDT + khóa + boundary 10k |
| BR-DATA-07 | Pagination default 20/trang, max 100 | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1910 | ✅ Yes | — | TC pagination KH năm / CTDT / khóa / giảng viên / học viên |
| BR-FLOW-03 | Không sửa / xóa sau phê duyệt | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1911 | ✅ Yes | "Refinement Cách 2: trạng thái TU_CHOI vẫn cho sửa" (line 1032) | TC update KH năm `DA_DUYET` → reject ERR-KH-02 |
| BR-FLOW-04 | Từ chối yêu cầu lý do ≥10 ký tự | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1912 | ✅ Yes | — | TC CB PD từ chối KH / CTDT / KQ / hủy công bố |
| BR-FLOW-05 | Công khai qua API Cổng PLQG | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1913 | ✅ Yes | — | TC FR-III-16 công khai KH năm + FR-III-19 đẩy KQ chuyên trang |
| BR-INTG-05 | Retry policy 3 lần backoff khi API fail | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1914 | ✅ Yes | — | TC API Cổng PLQG fail → retry → alert QTHT |
| BR-NOTIF-01 | Thông báo phê duyệt + workflow event | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1915 | ✅ Yes | — | TC verify CB NV / CB PD / HV nhận thông báo in-app + email |
| BR-PUBLIC-01..03 | 5 trường công khai cho entity chuyên trang | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1916 | ✅ Yes (KH năm, CTDT, KH, BAI_GIANG) | — | TC switch `cong_khai`, ảnh đại diện, file đính kèm công khai |
| BR-KQ-01 | Auto-classify xếp loại từ điểm | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1917 + :1920-1934 | ✅ Yes | — | TC nhập điểm → verify xep_loai theo bảng ngưỡng |
| BR-KQ-02 | Đạt khóa = chuyên cần ≥ ngưỡng AND điểm thi ≥ điểm đạt | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1918 + :1936-1958 | ✅ Yes | — | TC 4 trường hợp Đủ/Thiếu CC/Thiếu điểm/Thiếu cả 2 |
| BR-EC-01 | Optimistic locking | srs-v3/srs-v3.md:4066 (Phụ lục B) | ✅ Yes | — | TC 2 user cùng UPDATE KH năm / CTDT → 1 user nhận ERR-SYS-02 |
| BR-EC-13 | Search sanitize max 200 ký tự | srs-v3/srs-v3.md:4078 | ✅ Yes | — | TC FR-III-02/12 search SQL injection / XSS / long query |

### 2.2 Error Codes

| Mã lỗi | FR liên quan | Điều kiện trigger | Message (SRS-quoted) | Severity | Nguồn |
|--------|--------------|-------------------|----------------------|----------|-------|
| ERR-CTDT-01 | FR-III-01 | Tên chương trình trống | "Tên chương trình là bắt buộc" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:232 |
| ERR-CTDT-02 | FR-III-01 | Ngày kết thúc ≤ ngày bắt đầu | "Ngày kết thúc phải sau ngày bắt đầu" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:233 |
| ERR-CTDT-03 | FR-III-01 | Xóa CTDT có khóa học | "Không thể xóa chương trình đã có khóa học" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:234 |
| ERR-CTDT-04 | FR-III-01 | Sửa CTDT đã duyệt | "Không thể sửa chương trình đã được duyệt" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:235 |
| ERR-CTDT-05 | FR-III-01 | Tạo CTDT khi KH năm cha chưa duyệt | "Kế hoạch năm cha phải ở trạng thái Đã duyệt hoặc Đã công khai mới được tạo CTDT" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:236 |
| ERR-CTDT-PD-01 | FR-III-01 | CB PD phê duyệt CTDT khác cấp | "Không có quyền phê duyệt CTDT của đơn vị khác" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:237 |
| ERR-CTDT-PD-02 | FR-III-01 | CTDT không ở trạng thái Chờ duyệt | "Chương trình đào tạo không ở trạng thái chờ phê duyệt" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:238 |
| ERR-CTDT-PD-03 | FR-III-01 | Lý do từ chối < 10 ký tự | "Lý do từ chối là bắt buộc và tối thiểu 10 ký tự" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:239 |
| ERR-CTDT-PD-04 | FR-III-01 | Gửi phê duyệt khi CTDT không ở Bản nháp / Bị từ chối | "Chỉ gửi phê duyệt được CTDT ở trạng thái Bản nháp hoặc Bị từ chối" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:240 |
| ERR-KH-01 | FR-III-14 | Tên KH trống | "Tên kế hoạch là bắt buộc" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1088 |
| ERR-KH-02 | FR-III-14 | Sửa KH năm đã duyệt | "Không thể sửa kế hoạch đã duyệt" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1089 |
| ERR-KH-03 | FR-III-14 | KH năm đang `CHO_DUYET` mà sửa | "Kế hoạch đang chờ phê duyệt, không sửa được" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1090 |
| ERR-KH-04 | FR-III-14 | thoi_gian_ket_thuc ≤ thoi_gian_bat_dau | "Ngày kết thúc phải sau ngày bắt đầu" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1091 |
| ERR-KH-05 | FR-III-14 | Xóa KH năm có CTDT con | "Không thể xóa kế hoạch đã có chương trình đào tạo" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1092 |
| ERR-KH-06 | FR-III-14 | Export Excel > 10.000 dòng | "Vượt giới hạn 10.000 dòng, vui lòng lọc nhỏ hơn" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1093 |
| ERR-DKDT-01 | FR-III-03 | Khóa học đã đóng đăng ký | "Khóa học đã đóng đăng ký" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:380 |
| ERR-DKDT-02 | FR-III-03 | Từ chối không có lý do | "Lý do từ chối là bắt buộc" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:381 |
| ERR-CB-KQ-01 | FR-III-19 | Khóa không ở HOAN_THANH | "Chỉ công bố KQ khi khóa đã HOAN_THANH" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1284 |
| ERR-CB-KQ-02 | FR-III-19 | Không có HV nào có KQ DA_DUYET | "Chưa có kết quả đã được phê duyệt" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1285 |
| ERR-CB-KQ-03 | FR-III-19 | API Cổng PLQG lỗi | "Lỗi đẩy KQ lên chuyên trang, vui lòng thử lại" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1286 |
| ERR-CB-KQ-04 | FR-III-19 | Hủy công bố không nhập lý do hoặc <10 ký | "Lý do hủy bắt buộc, ≥10 ký tự" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1287 |
| ERR-CB-KQ-05 | FR-III-19 | Hủy công bố nhưng chưa từng công bố | "Chưa có kết quả công bố để hủy" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1288 |
| ERR-LH-01 | FR-III-22 | ngay_hoc ngoài khoảng khóa | "Ngày học phải trong khoảng {ngay_bat_dau} đến {ngay_ket_thuc}" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1481 |
| ERR-LH-02 | FR-III-22 | gio_ket_thuc ≤ gio_bat_dau | "Giờ kết thúc phải sau giờ bắt đầu" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1482 |
| ERR-LH-03 | FR-III-22 | TRUC_TUYEN thiếu link_zoom | "Link học trực tuyến là bắt buộc" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1483 |
| ERR-LH-04 | FR-III-22 | TRUC_TIEP thiếu địa điểm | "Địa điểm là bắt buộc cho buổi trực tiếp" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1484 |
| ERR-LH-05 | FR-III-22 | Xóa buổi đã có điểm danh | "Không thể xóa buổi đã có dữ liệu điểm danh" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:1485 |
| ERR-DX-01 | FR-III-13 | Nội dung đề xuất trống | "Nội dung đề xuất là bắt buộc" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:960 |
| ERR-DX-02 | FR-III-13 | Sửa đề xuất đã tiếp nhận | "Không thể sửa đề xuất đã tiếp nhận" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:960 |
| ERR-GV-01 | FR-III-11 | Họ tên giảng viên trống | "Họ tên là bắt buộc" | ERROR | srs-update-2026-5-5/srs-fr-03-dao-tao.md:908 |
| WRN-GV-01 | FR-III-11 | GV đang phân công dạy ≥1 khóa | "GV đang phân công dạy {N} khóa" | WARNING | srs-update-2026-5-5/srs-fr-03-dao-tao.md:908 |

> ⚠️ Message quote nguyên văn — không "close enough" accept khi test negative.

### 2.3 Permission Matrix (module-specific)

> Reference: [output/permission-matrix.md](../../../output/permission-matrix.md). Bảng dưới tóm tắt entity nhóm III × role.

| Entity / Action | QTHT | CB_NV (cùng cấp) | CB_PD (cùng cấp) | DN | NHT | GIANG_VIEN | HOC_VIEN |
|-----------------|:----:|:----------------:|:----------------:|:--:|:---:|:----------:|:--------:|
| KE_HOACH_DAO_TAO — Create | C | C | — | — | — | — | — |
| KE_HOACH_DAO_TAO — Read | R (all) | R (cấp mình) | R (cấp mình) | R (DA_CONG_KHAI) | R (DA_CONG_KHAI) | — | — |
| KE_HOACH_DAO_TAO — Update | U | U (NHAP/TU_CHOI) | — | — | — | — | — |
| KE_HOACH_DAO_TAO — Delete | D | D (NHAP, no CTDT con) | — | — | — | — | — |
| KE_HOACH_DAO_TAO — Phê duyệt | — | — | U (CHO_DUYET, cùng cấp) | — | — | — | — |
| KE_HOACH_DAO_TAO — Công khai | — | U (DA_DUYET) | — | — | — | — | — |
| CHUONG_TRINH_DAO_TAO — CRUD | CRUD | CRUD (DU_THAO/TU_CHOI) | R | R (DA_CONG_KHAI/DA_DUYET) | R (DA_CONG_KHAI) | — | — |
| CHUONG_TRINH_DAO_TAO — Phê duyệt | — | — | U (CHO_DUYET, cùng cấp — Thay đổi 2) | — | — | — | — |
| KHOA_HOC — CRUD | CRUD | CRUD (DU_THAO) | R | R (DA_CONG_KHAI) | R (DA_CONG_KHAI) | R (được phân) | R (đã đăng ký) |
| KHOA_HOC — Phê duyệt | — | — | U (CHO_DUYET) | — | — | — | — |
| LICH_HOC — CRUD | CRUD | CRUD (per khóa mình quản lý) | R | — | — | R (khóa được phân) | R (khóa đăng ký) |
| GIANG_VIEN — CRUD | CRUD | CRUD (đơn vị mình) | R | — | — | R (self) | — |
| HOC_VIEN — CRUD | CRUD | CRUD (đơn vị) | R | CR (đăng ký HV thuộc DN) | CR (đăng ký HV thuộc NHT) | — | R (self) |
| DANG_KY_DAO_TAO — Duyệt | — | U | U | — | — | — | — |
| KET_QUA_DAO_TAO — Ghi nhận | — | U (DA_KET_THUC → CHO_DUYET_KQ) | — | — | — | — | — |
| KET_QUA_DAO_TAO — Phê duyệt KQ | — | — | U (CHO_DUYET_KQ → HOAN_THANH) | — | — | — | — |
| KET_QUA_DAO_TAO — Công bố | — | U (HOAN_THANH) | — | — | — | — | R (self) |
| BAI_GIANG — CRUD | CRUD | CRUD | R | R (cong_khai=1) | R (cong_khai=1) | R | R |
| DE_KIEM_TRA — CRUD + Phân phối | CRUD | CRUD (NHAP) | R + Phân phối | — | — | — | — |

### 2.4 UI Layout

> ⚠️ KHÔNG dùng absence để khẳng định "module KHÔNG có X". Mọi feature thiếu UI phải đối chiếu §2.1 BR + SRS Phụ lục B trước.

**SCR-III-00 — Kế hoạch đào tạo năm (sub-menu 1)** — `srs-update-2026-5-5/srs-fr-03-dao-tao.md:1505-1575`:
- **Toolbar:** Breadcrumb · [+ Tạo KH năm] · [Xuất Excel] (BR-DATA-06) · [Lọc] · Search.
- **Filter-bar:** `nam` (year picker), `trang_thai` (NHAP/CHO_DUYET/TU_CHOI/DA_DUYET/DA_CONG_KHAI), khoảng ngày, đơn vị (QTHT).
- **Table:** ma_kh, ten_ke_hoach, nam, thoi_gian, ngan_sach_du_kien, so_ctdt, trang_thai, hành động ([Xem]/[Sửa]/[Xóa]/[Gửi duyệt]/[Phê duyệt]/[Công khai]).
- **Drawer Tạo / Sửa:** đầy đủ 9 input field FR-III-14. Riêng `nam` default năm hiện tại, `thoi_gian_bat_dau/ket_thuc` default 01/01–31/12.
- **Drawer chi tiết:** tab "Thông tin" + tab "CTDT con" + tab "Lịch sử workflow".

**SCR-III-01 — Chương trình đào tạo (sub-menu 2)** — `srs-update-2026-5-5/srs-fr-03-dao-tao.md:1576-1650`:
- **Toolbar:** Breadcrumb · [+ Tạo CTDT] (chỉ khi KH năm cha DA_DUYET / DA_CONG_KHAI) · [Xuất Excel] · Search.
- **Tab:** "Chương trình đào tạo" · "Đề xuất đào tạo" (gộp FR-III-13).
- **Table CTDT:** expandable rows hiển thị Khóa học con. Cột: ma_ctdt, ten_chuong_trinh, ke_hoach_cha, linh_vuc, hinh_thuc, so_khoa_hoc, trang_thai (SM-CTDT 7 trạng thái), hành động.
- **Drawer Tạo / Sửa:** 14 field CTDT (đầy đủ 5 trường công khai BR-PUBLIC).
- **Workflow buttons:** [Gửi phê duyệt] (DU_THAO/TU_CHOI), [Phê duyệt] / [Từ chối] (CHO_DUYET — CB PD), [Hủy] (DU_THAO/TU_CHOI/DA_DUYET).
- **[Xuất docx/PDF]** (FR-III-20) — chỉ DA_DUYET/DA_CONG_KHAI/HOAN_THANH.

**SCR-III-02 — Khóa học (sub-menu 3, drill-down 7 tab)** — `srs-update-2026-5-5/srs-fr-03-dao-tao.md:1651-1669`:
- Tab 1 **Thông tin** — 17 input field, button [Gửi phê duyệt], [Phê duyệt]/[Từ chối], [Kích hoạt], [Kết thúc], [Hủy].
- Tab 2 **Lịch học** (FR-III-22) — table buổi dạy + [+ Thêm buổi], [Sửa], [Xóa]. Cảnh báo gating sửa/xóa khi có điểm danh.
- Tab 3 **Học viên** — list DANG_KY_DAO_TAO + [+ Thêm HV thủ công], [Duyệt]/[Từ chối] đăng ký, [Import Excel].
- Tab 4 **Điểm danh** — table per buổi × HV, dropdown 3-value (CO_MAT/VANG_PHEP/VANG_KHONG_PHEP).
- Tab 5 **Kết quả kiểm tra** — table HV × điểm + xếp loại (BR-KQ-01 auto), [Trình duyệt KQ], [Phê duyệt KQ], [Từ chối KQ].
- Tab 6 **Bài giảng** — map bài giảng từ SCR-III-03.
- Tab 7 **Công bố kết quả** (FR-III-19 Hướng B) — [Công bố] + switch `day_chuyen_trang`, [Hủy công bố] + ô lý do.

**SCR-III-03 — Kho tài liệu / Bài giảng (sub-menu 4)**: danh sách + preview panel + switch `cong_khai`.

**SCR-III-04 — Ngân hàng câu hỏi & Đề kiểm tra (sub-menu 5)** — 2 tab:
- Tab Câu hỏi: CRUD + phân loại chủ đề + mức độ + đáp án đúng.
- Tab Đề kiểm tra: CRUD đề + bốc câu hỏi (NGAU_NHIEN / THU_CONG) + [Phân phối] → khóa.

**SCR-III-05 — Giảng viên / Trợ giảng (sub-menu 6)** — 2 tab:
- Tab Thông tin: hồ sơ GV (ho_ten, chuyen_nganh, trinh_do, email, sđt, linh_vuc_ids, trang_thai DANG_GIANG_DAY/TAM_DUNG).
- Tab Lịch sử giảng dạy: list khóa đã dạy + vai trò + kết quả.

**Cross-cutting features MẶC ĐỊNH (theo BR global):**
- ☐ [Xuất Excel] toolbar 4 sub-menu chính (BR-DATA-06)
- ☐ Pagination 20/trang (BR-DATA-07)
- ☐ Search sanitize max 200 chars (BR-EC-13)
- ☐ URL sync filter
- ☐ Audit log mọi CUD + workflow transition (BR-DATA-05)
- ☐ Optimistic lock UPDATE/DELETE (BR-EC-01)
- ☐ 5 trường công khai BR-PUBLIC cho KH năm + CTDT + Khóa + Bài giảng

### 2.5 State Machine

#### SM-KH-DAO-TAO (Kế hoạch đào tạo năm) — `srs-update-2026-5-5/srs-fr-03-dao-tao.md:1829-1856`

```
[*] --> NHAP : CB NV tạo
NHAP --> CHO_DUYET : CB NV gửi duyệt (lần đầu)
CHO_DUYET --> DA_DUYET : CB PD duyệt
CHO_DUYET --> TU_CHOI : CB PD từ chối + lý do ≥10 ký
TU_CHOI --> CHO_DUYET : CB NV sửa rồi gửi duyệt lại (KHÔNG qua NHAP — refinement Cách 2)
DA_DUYET --> DA_CONG_KHAI : CB NV công khai
DA_CONG_KHAI --> DA_DUYET : CB NV hủy công khai
```

5 trạng thái: NHAP / CHO_DUYET / TU_CHOI / DA_DUYET / DA_CONG_KHAI.

#### SM-CTDT (Chương trình đào tạo) — `srs-update-2026-5-5/srs-fr-03-dao-tao.md:1858-1889`

```
[*] --> DU_THAO : CB NV tạo (Guard: KH năm cha DA_DUYET/DA_CONG_KHAI)
DU_THAO --> CHO_DUYET : Gửi phê duyệt
CHO_DUYET --> DA_DUYET : CB PD duyệt
CHO_DUYET --> TU_CHOI : CB PD từ chối + lý do ≥10
TU_CHOI --> CHO_DUYET : Gửi duyệt lại (refinement Cách 2)
DA_DUYET --> DANG_THUC_HIEN : Auto khi có ≥1 KHOA_HOC con DA_CONG_KHAI/DANG_DIEN_RA
DANG_THUC_HIEN --> HOAN_THANH : Auto khi mọi KHOA_HOC con HOAN_THANH/DA_HUY
DU_THAO/TU_CHOI/DA_DUYET --> DA_HUY : CB NV/PD hủy
```

7 trạng thái: DU_THAO / CHO_DUYET / TU_CHOI / DA_DUYET / DANG_THUC_HIEN / HOAN_THANH / DA_HUY.

#### SM-KHOAHOC (Khóa học) — `srs-update-2026-5-5/srs-fr-03-dao-tao.md:1806-1826`

> **Phương án chính (chốt v3.5):** **9 trạng thái** per SRS body line 1806-1825 mermaid (Thay đổi 3 OUT — gộp Bị từ chối vào DU_THAO/DA_KET_THUC).
> **DELTA-MAP-FR03.md:22 nói 11 trạng thái** (thêm TU_CHOI + TU_CHOI_KQ Cách 2) — **SPEC-CLARIFY chờ BA confirm** trước Round chạy đầu. Test plan tạm chốt **9** theo SRS body để tránh test FAIL random; nếu BA confirm 11, add 2 TC bổ sung cover TU_CHOI/TU_CHOI_KQ.

**9 trạng thái (per SRS body mermaid 1811-1825):**
1. DU_THAO (initial)
2. CHO_DUYET
3. DA_DUYET
4. DANG_DIEN_RA
5. DA_KET_THUC
6. CHO_DUYET_KQ
7. HOAN_THANH
8. HUY
9. (state thứ 9 — SPEC-CLARIFY: SRS text §1806 ghi "9 state" nhưng mermaid chỉ có 8 unique. Chờ BA chốt — có thể là state implicit "Bị từ chối KQ" gộp vào DA_KET_THUC sau CHO_DUYET_KQ rollback hoặc state ẩn admin.)

**Transitions key:**
- CHO_DUYET → DU_THAO khi từ chối (KHÔNG có TU_CHOI state riêng — Thay đổi 3 OUT).
- CHO_DUYET_KQ → DA_KET_THUC khi từ chối KQ (rollback, không TU_CHOI_KQ state).
- HUY có thể từ DU_THAO / CHO_DUYET / DA_DUYET (chưa đăng ký).

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| **GĐ 1 Seed** | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | `ke_hoach_dao_tao_variants`, `ctdt_variants`, `khoa_hoc_variants`, `lich_hoc_variants`, `giang_vien_variants`, `hoc_vien_variants` (cần bổ sung — xem DELTA-MAP §4) |
| **GĐ 1 click flow** | [`input/flow-module.md`](../../../input/flow-module.md) | §8 SM-KHOAHOC (v3) + §8a SM-CTDT mới + §8b SM-KH-DAO-TAO mới |
| **GĐ 2 Workflow** | [`input/flow-module.md`](../../../input/flow-module.md) | §8 bảng flow Bước 1 → N (KH năm → CTDT → KH → Lịch → HV → Điểm danh → KQ → Công bố) + Phụ lục 2 preset |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | Verify entity tạo / đọc — KE_HOACH_DAO_TAO mới (E27), HOC_VIEN mới (E28), LICH_HOC mới (E29) |

**Upstream dependencies (Tier check):**

| Entity | Tier | Phụ thuộc upstream | Seed trước tại module |
|--------|:----:|--------------------|-----------------------|
| KE_HOACH_DAO_TAO | 1 | DON_VI (FR-10) | FR-10 |
| CHUONG_TRINH_DAO_TAO | 2 | KE_HOACH_DAO_TAO DA_DUYET/DA_CONG_KHAI + DANH_MUC linh_vuc | FR-03 (KH năm) + FR-10 |
| KHOA_HOC | 3 | CTDT DA_DUYET + GIANG_VIEN DANG_GIANG_DAY (≥1) + BAI_GIANG | FR-03 (CTDT) + FR-03 (GV) + FR-04 TVV (junction qua KHOA_HOC_GIANG_VIEN) |
| LICH_HOC | 4 | KHOA_HOC IN (DU_THAO, CHO_DUYET, DA_DUYET, DA_CONG_KHAI, DANG_DIEN_RA) | FR-03 (KH) |
| GIANG_VIEN | 1 | TAI_KHOAN (optional self-service) | FR-03 (sub-menu 6) |
| HOC_VIEN | 1 | TAI_KHOAN 1:1 + DOANH_NGHIEP / NHT (đăng ký) | FR-03 (qua FR-III-04 đăng ký) + FR-07 DN |
| DANG_KY_DAO_TAO | 4 | KHOA_HOC DA_CONG_KHAI + HOC_VIEN | FR-03 |
| KET_QUA_DAO_TAO | 5 | KHOA_HOC DA_KET_THUC + LICH_HOC có điểm danh + DE_KIEM_TRA DA_PHAN_PHOI có điểm | FR-03 |

> KHÔNG hardcode số record ở đây — fixture chốt 6 variants/entity. Workflow advance state là việc của **GĐ 2 Workflow**.

---

## 3. Cấu Trúc File Test Case

```
fr-03-dao-tao/
├── test-plan.md                       ← File này
├── 01-TC-ke-hoach-dt-nam.md           ← Sub-menu 1: KH năm (FR-III-14/15/16)
├── 02-TC-khoa-dao-tao.md              ← Sub-menu 2 + 3: CTDT + Khóa học + Lịch học + Đề KT + Bài giảng + KQ + Công bố
├── 03-TC-hoc-vien.md                  ← Sub-menu 3 phụ: Học viên + Đăng ký + Điểm danh + Tìm KQ
├── 04-TC-giang-vien.md                ← Sub-menu 4: Giảng viên CRUD + Search
└── (11-REVIEW-edge-case-hunter.md)    ← Optional sau review
```

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Auth/Permission | Tổng |
|------|------:|---------:|-----:|----------------:|-----:|
| 01 — KH năm (FR-III-14/15/16) | 3 | 3 | 2 | 2 | **10** |
| 02 — Khóa đào tạo (FR-III-01/02/13/17/18/19/20/21/22 + NEW-01/02/03 + 07/08/09/10) | 7 | 7 | 3 | 2 | **19** |
| 03 — Học viên + Đăng ký + Điểm danh (FR-III-03/04/05/06) | 4 | 3 | 1 | 2 | **10** |
| 04 — Giảng viên (FR-III-11/12 + junction KHOA_HOC_GIANG_VIEN) | 3 | 2 | 1 | 2 | **8** |
| **TỔNG** | **17** | **15** | **7** | **8** | **47** |

### 4.1 TC detail summary

| TC ID | Tên | File | Loại | Priority |
|-------|-----|------|------|:--------:|
| TC-KH-01 | Tạo KH năm `NHAP` đầy đủ trường — happy | 01 | Happy | P0 |
| TC-KH-02 | Sửa KH năm `NHAP` / `TU_CHOI` — happy | 01 | Happy | P0 |
| TC-KH-03 | Xóa KH năm chưa có CTDT con — happy | 01 | Happy | P1 |
| TC-KH-04 | Sửa KH năm `DA_DUYET` → ERR-KH-02 | 01 | Negative | P0 |
| TC-KH-05 | Xóa KH năm có CTDT con → ERR-KH-05 | 01 | Negative | P0 |
| TC-KH-06 | Tạo KH `thoi_gian_ket_thuc <= thoi_gian_bat_dau` → ERR-KH-04 | 01 | Negative | P1 |
| TC-KH-07 | Workflow đầy đủ: NHAP → CHO_DUYET → TU_CHOI → CHO_DUYET → DA_DUYET → DA_CONG_KHAI → DA_DUYET (refinement Cách 2) | 01 | Edge | P0 |
| TC-KH-08 | CB PD khác cấp phê duyệt → reject (BR-AUTH-05) | 01 | Auth | P0 |
| TC-KH-09 | CB_NV_BN không thấy KH năm của CB_NV_DP (BR-AUTH-08) | 01 | Auth | P0 |
| TC-KDT-01 | Tạo CTDT với KH năm cha `DA_DUYET` — happy | 02 | Happy | P0 |
| TC-KDT-02 | Tạo CTDT với KH năm cha `NHAP` → ERR-CTDT-05 | 02 | Negative | P0 |
| TC-KDT-03 | Workflow CTDT NHAP → CHO_DUYET → TU_CHOI → CHO_DUYET → DA_DUYET (refinement Cách 2) — happy | 02 | Happy | P0 |
| TC-KDT-04 | CB PD từ chối CTDT lý do < 10 ký → ERR-CTDT-PD-03 | 02 | Negative | P0 |
| TC-KDT-05 | Auto-transition CTDT DA_DUYET → DANG_THUC_HIEN khi có KHOA_HOC con DA_CONG_KHAI | 02 | Edge | P1 |
| TC-KDT-06 | Tạo Khóa học với CTDT cha `DA_DUYET` + ≥1 GIANG_VIEN DANG_GIANG_DAY — happy | 02 | Happy | P0 |
| TC-KDT-07 | Tạo Khóa học `ngay_ket_thuc <= ngay_bat_dau` → validation error | 02 | Negative | P1 |
| TC-KDT-08 | Tạo Lịch học (FR-III-22) trong khoảng ngày khóa — happy | 02 | Happy | P0 |
| TC-KDT-09 | Tạo Lịch học `TRUC_TUYEN` thiếu link_zoom → ERR-LH-03 | 02 | Negative | P0 |
| TC-KDT-10 | Sửa / xóa Lịch học đã có điểm danh → ERR-LH-05 | 02 | Negative | P0 |
| TC-KDT-11 | Workflow KQ: ghi nhận → CHO_DUYET_KQ → HOAN_THANH (FR-III-17/18) — happy | 02 | Happy | P0 |
| TC-KDT-12 | Công bố KQ (FR-III-19) HOAN_THANH có ≥1 KQ DA_DUYET — happy | 02 | Happy | P0 |
| TC-KDT-13 | Công bố KQ khi khóa chưa HOAN_THANH → ERR-CB-KQ-01 | 02 | Negative | P0 |
| TC-KDT-14 | Xuất docx/PDF CTDT DA_DUYET (FR-III-20) — happy | 02 | Edge | P1 |
| TC-KDT-15 | CB PD khác cấp duyệt KQ → reject (BR-AUTH-05) | 02 | Auth | P0 |
| TC-HV-01 | DN/NHT đăng ký HV vào khóa DA_CONG_KHAI — happy | 03 | Happy | P0 |
| TC-HV-02 | CB NV duyệt đăng ký → DA_DUYET — happy | 03 | Happy | P0 |
| TC-HV-03 | Đăng ký vào khóa đã đóng → ERR-DKDT-01 | 03 | Negative | P1 |
| TC-HV-04 | Điểm danh 3-value enum CO_MAT / VANG_PHEP / VANG_KHONG_PHEP — happy | 03 | Happy | P0 |
| TC-HV-05 | Điểm danh API POST giá trị boolean cũ (`true`/`false`) → BE 400 invalid enum (SRS v3.5 enum 3-value `CO_MAT/VANG_PHEP/VANG_KHONG_PHEP` REPLACE boolean — KHÔNG có spec convert fallback) | 03 | Negative | P0 |
| TC-HV-06 | Auto-classify BR-KQ-01: 9.0 → "Giỏi", 7.5 → "Khá", 5.5 → "Trung bình", 4 → "Không đạt" | 03 | Edge | P0 |
| TC-HV-07 | BR-KQ-02: chuyên cần 85% + điểm 7 → `ket_qua=DAT`; chuyên cần 70% + điểm 9 → `KHONG_DAT` | 03 | Happy | P0 |
| TC-HV-08 | Học viên không thấy KQ HV khác (BR-AUTH-08) | 03 | Auth | P0 |
| TC-HV-09 | Từ chối đăng ký không nhập lý do → ERR-DKDT-02 | 03 | Auth | P1 |
| TC-GV-01 | Tạo GV `DANG_GIANG_DAY` đầy đủ trường — happy | 04 | Happy | P0 |
| TC-GV-02 | Tạo GV họ tên trống → ERR-GV-01 | 04 | Negative | P0 |
| TC-GV-03 | Xóa GV đang phân công ≥1 khóa → WRN-GV-01 + chặn | 04 | Negative | P0 |
| TC-GV-04 | Search GV theo từ khóa + lĩnh vực — happy | 04 | Happy | P1 |
| TC-GV-05 | Search GV với input SQL/XSS 200+ ký → sanitize (BR-EC-13) | 04 | Edge | P1 |
| TC-GV-06 | CB NV BN không thấy GV của ĐP (BR-AUTH-08) | 04 | Auth | P0 |
| TC-GV-07 | **Junction KHOA_HOC_GIANG_VIEN.vai_tro override `GIANG_VIEN.loai`** — cùng 1 GV TRO_GIANG khóa A + GIANG_VIEN khóa B → verify tab Lịch sử giảng dạy hiển thị vai trò per khóa đúng (SRS line 1714, 1784-1798 Thay đổi 13) | 04 | Happy | P0 |
| TC-GV-08 | **Cross-link FR-04 TVV `HOAT_DONG` → KHOA_HOC.giang_vien_ids** — dropdown chọn GV khi tạo khóa hiển thị cả GIANG_VIEN nội bộ FR-03 + TVV `HOAT_DONG` từ FR-04 (verify enum rename `DANG_HOAT_DONG → HOAT_DONG`) | 04 | Happy | P0 |
| TC-KH-10 | **BR-PUBLIC-01..03 switch `cong_khai`** trên KH năm — upload `anh_dai_dien` + `file_dinh_kem_cong_khai` + `mo_ta_cong_khai` + verify timestamp `thoi_gian_dang_tai` (SRS line 1916) | 01 | Edge | P0 |
| TC-KDT-16 | **BR-PUBLIC switch `cong_khai`** trên CTDT — 5 trường công khai render đủ + toggle on/off | 02 | Edge | P0 |
| TC-KDT-17 | **BR-PUBLIC switch `cong_khai`** trên Khóa học — 5 trường công khai + verify chuyên trang DN/NHT read được khi `cong_khai=true` | 02 | Edge | P0 |
| TC-KDT-18 | **BR-PUBLIC switch `cong_khai`** trên Bài giảng — verify chuyên trang DN/NHT/HV read được (cross-cutting BUG-BM-005 pattern) | 02 | Edge | P0 |
| TC-KDT-19 | **FR-III-19 hủy công bố KQ** — happy: HV publish OK → CB NV hủy với lý do ≥10 ký → state DA_CONG_BO → HOAN_THANH | 02 | Happy | P0 |
| TC-KDT-20 | **FR-III-19 hủy công bố KQ** — negative: lý do <10 ký → ERR-CB-KQ-04 | 02 | Negative | P1 |
| TC-KDT-21 | **FR-III-19 hủy công bố KQ** — negative: chưa từng công bố mà hủy → ERR-CB-KQ-05 | 02 | Negative | P1 |
| TC-KDT-22 | **FR-III-21 phê duyệt khóa học** — happy: CB PD duyệt khóa CHO_DUYET → DA_DUYET (BR-AUTH-05 cùng cấp). **SPEC-CLARIFY:** SRS line 1827 ghi "KHÔNG có FR riêng" — chờ BA confirm có FR-III-21 độc lập | 02 | Happy | P0 |
| TC-KDT-23 | **FR-III-21 phê duyệt khóa học** — negative: CB PD khác cấp duyệt → reject (BR-AUTH-05) | 02 | Auth | P0 |
| TC-KDT-24 | **BR-INTG-05 Cổng PLQG retry 3 lần** — mock API fail → verify retry backoff + alert QTHT. Nếu env sandbox down → mark BLOCKED nhóm D (Lỗi env / chờ infra) | 02 | Edge | P1 |
| TC-HV-10 | **HOC_VIEN entity riêng** — DN đăng ký HV qua FR-III-04 → verify auto-tạo TAI_KHOAN + HOC_VIEN record link `tai_khoan_id` (SRS Thay đổi `_DELTA-MAP-FR03.md:42`) | 03 | Happy | P0 |
| TC-KH-07a | (Split TC-KH-07 cũ) refinement Cách 2 KH năm: TU_CHOI → CHO_DUYET (CB NV sửa rồi gửi duyệt lại, KHÔNG qua NHAP) | 01 | Edge | P0 |

### 4.2 Phân bổ priority

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc) | 34 | 72% |
| P1 (quan trọng) | 13 | 28% |
| P2 (nên có) | 0 | 0% |
| **Tổng** | **47** | **100%** |

---

## 5. Tiêu chí đạt / không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md).

- ✅ **PASS round:** 100% P0 pass + ≥90% P1 pass.
- ❌ **FAIL round:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%.
- ⚠️ **Sai spec (PASS but deviates):** chạy được nhưng lệch SRS quote → log Minor + escalate BA.
- 🚫 **BLOCKED:** thiếu seed / endpoint / permission upstream → log nguyên nhân nhóm A-F (xem `output/template/tc-block-classification-template.md`).
- 🤷 **Không xác định:** CẤM. Phải retry method (reload fresh, curl verify response, isolatedContext mới) trước khi mark.

**Module-specific exit criteria:**
- SM-KH-DAO-TAO 5 trạng thái phải reach hết qua workflow test (TC-KH-07).
- SM-CTDT 7 trạng thái reach ≥6 (DA_HUY có thể defer nếu out-of-scope).
- SM-KHOAHOC 9 trạng thái reach hết qua GĐ 2 Workflow trước GĐ 3 (precondition).
- BR-KQ-01 cover ≥4 ngưỡng (Giỏi/Khá/TB/Không đạt). BR-KQ-02 cover 4 trường hợp truth table (Đủ/Thiếu CC/Thiếu điểm/Thiếu cả 2).
- Điểm danh enum 3-value test pass (boolean cũ phải reject hoặc convert).
- FR-III-19 Hướng B: KHÔNG còn UI / endpoint cấp chứng nhận PDF — phải verify absence.

---

## 6. Tham chiếu

- [input/srs-v3/srs-fr-03-dao-tao.md](../../../input/srs-v3/srs-fr-03-dao-tao.md) — SRS v3 (baseline)
- [input/srs-update-2026-5-5/srs-fr-03-dao-tao.md](../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md) — SRS v3.5 (source of truth hiện hành)
- [input/srs-update-2026-5-5/_DELTA-MAP-FR03.md](../../../input/srs-update-2026-5-5/_DELTA-MAP-FR03.md) — Bản đồ delta v3 → v3.5
- [input/srs-v3/srs-v3.md Phụ lục B](../../../input/srs-v3/srs-v3.md) — BR cross-cutting (line 3939-4088)
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md §FR-03](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — bảng SM transition + thứ tự seed
- [input/quy-trinh-nghiep-vu/flow-module.md §8](../../../input/quy-trinh-nghiep-vu/flow-module.md) — SM-KHOAHOC + SM-CTDT + SM-KH-DAO-TAO chi tiết
- [tasks/system-overview.md §4.10](../../../tasks/system-overview.md) — Module 9 Đào tạo layout
- [input/users.csv](../../../input/users.csv) — Account convention (cb_nv_*_01/02/03, cb_pd_*_01/02/03, qtht_01..10, nht_01/02)
- [output/permission-matrix.md](../../../output/permission-matrix.md) — Ma trận phân quyền 49 entity × 11 role
- [input/data/entity-map.md](../../../input/data/entity-map.md) — Bản đồ entity tạo / đọc cross-module
- [input/data/seed-fixture.yaml](../../../input/data/seed-fixture.yaml) — Fixture variants
- [output/template/test-plan-overview-template.md](../../../output/template/test-plan-overview-template.md) — Template
- [output/template/bug-report-template.md](../../../output/template/bug-report-template.md) — Bug report template (6 sections)
- [output/template/tc-block-classification-template.md](../../../output/template/tc-block-classification-template.md) — Phân loại nhóm A-F nguyên nhân BLOCK

---

*Test plan FR-03 v1.0 — drafted 2026-05-12 từ delta v3 → v3.5 (+133% volume, file thay đổi LỚN NHẤT batch 2026-05-05). Cần BA sign-off trước khi viết TC detail vào 4 file 01..04.*
