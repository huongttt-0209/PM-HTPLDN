# Kế Hoạch Kiểm Thử — Tư vấn nhanh (FR-13, SCR-X2-01/03)

> **Phiên bản**: 1.1 (Revised 2026-05-12 13:30:00 — apply review.md REVISE: +G3 upload boundary, +G4 cross-don_vi permission, +G2/G9 SPEC-CLARIFY, +S2/S5/S6 P0/P1 escalate)
> **Ngày tạo**: 2026-05-12
> **Nguồn dữ liệu**: LOCAL — `input/srs-v3/srs-fr-13-tv-nhanh.md` + `input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md` (SRS v3.5 cập nhật 2026-05-05 là authoritative)
> **SRS Reference**: FR-X.2-01..06 (UC154..158); SCR-X2-01 (Kho Q&A), SCR-X2-03 (Phiên TV nhanh)
> **SOURCE MODE**: LOCAL
> **Module**: Lớp 4 — 2 đơn vị test (M13 Phiên TV nhanh + M14 Kho Q&A) per `tasks/system-overview.md` §4.1 dòng 156-157.

> **v3.5 — 2026-05-05 CHANGE NOTES (so với v3.0):**
> 1. SM-TVNHANH rút gọn từ 6 → 4 state: bỏ `DANG_TIM_KIEM` + `DA_GOI_Y` (hệ thống không còn tự gợi ý TOP 5). Lifecycle mới: `MOI → CB_TRA_LOI → HOAN_THANH` (+ auto `HET_HAN` 30 ngày).
> 2. FR-X.2-02 cập nhật: **CB NV chủ động tra cứu kho** bằng từ khóa, không tự động tìm kiếm + không prefill câu hỏi DN; được phép soạn thủ công nếu không có Q&A phù hợp.
> 3. Thêm nút **"Đẩy sang Nhóm II"** trong phiên TV nhanh → tạo `HOI_DAP` với `kenh_tiep_nhan=TVN_BRIDGE` + `tu_van_nhanh_goc_id` (FR-X.2-02 step 9).
> 4. Thêm **FR-X.2-06 Công khai / Hủy công khai Q&A** (UC156) — gọi API ra Cổng PLQG (BR-FLOW-05); thêm state `CONG_KHAI` cho `KHO_CAU_HOI.trang_thai`; thêm field `cong_khai`, `anh_dai_dien`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`, `thoi_gian_dang_tai`.
> 5. FR-X.2-05 chuyển sang **API inbound** từ Cổng PLQG (Cổng PLQG gửi đánh giá thay DN, có `Idempotency-Key` chống ghi trùng 24h).
> 6. KHO_CAU_HOI `trang_thai` enum mở rộng: `CHO_DUYET / DA_DUYET / CONG_KHAI / HET_HIEU_LUC` (thêm `CONG_KHAI`).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

Module **FR-13 Tư vấn nhanh** (Nhóm X.2) gồm 6 FR (FR-X.2-01..06), 5 UC (UC154..158), 2 màn hình chính. Test plan này tách 2 đơn vị test:

- **M13 — Phiên TV nhanh** (SCR-X2-03, FR-X.2-02/03/05): Entity `TU_VAN_NHANH` + `DANH_GIA_TV`. **🚫 CHẶN nhập tay trên CMS** — phiên chỉ sinh khi DN gửi câu hỏi qua chuyên trang Cổng PLQG (FR-X.2-03 step 6 — API inbound). CB NV CHỈ xem/trả lời/đẩy sang Nhóm II — KHÔNG có nút "Thêm mới" (per `system-overview.md` §4.14 dòng 502 + `02-thu-tu-module.md` dòng 939).
- **M14 — Kho Q&A** (SCR-X2-01, FR-X.2-01/06): Entity `KHO_CAU_HOI`. 3 nguồn: `TU_DONG` (auto từ FR-02 `HOI_DAP` DA_DUYET — BR-FLOW-10), `THU_CONG` (CB NV nhập), `IMPORT` (xlsx). Có lifecycle phê duyệt cho `THU_CONG` + `IMPORT`. Có Công khai / Hủy công khai lên Cổng PLQG.

Phạm vi v3.5 mới thêm: tra cứu chủ động + Đẩy Nhóm II + 5 trường công khai (`anh_dai_dien`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`, `cong_khai`, `thoi_gian_dang_tai`) + Idempotency-Key cho đánh giá inbound.

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | Đơn vị test | File Test Case |
|---|--------|----------|--------------|--------|:-----------:|----------------|
| 1 | FR-X.2-01 | UC154/155/157 | Quản lý Kho Q&A (CRUD + duyệt + tìm kiếm) | KHO_CAU_HOI | M14 | `01-TC-kho-cau-hoi.md` |
| 2 | FR-X.2-02 | (ngoài CSV) | CB NV xử lý phiên TV nhanh (tra cứu kho + trả lời + đẩy Nhóm II) | TU_VAN_NHANH | M13 | `02-TC-phien-tv-nhanh.md` |
| 3 | FR-X.2-03 | (ngoài CSV) | DN gửi câu hỏi qua Cổng PLQG (API inbound) | TU_VAN_NHANH | M13 | `02-TC-phien-tv-nhanh.md` |
| 4 | FR-X.2-04 | (ngoài CSV) | DN tìm kiếm phản hồi qua Cổng PLQG (read-only) | KHO_CAU_HOI | M14 | `03-TC-cong-khai-search.md` |
| 5 | FR-X.2-05 | UC158 | Tiếp nhận đánh giá chất lượng TV nhanh (API inbound + Idempotency) | DANH_GIA_TV | M13 | `02-TC-phien-tv-nhanh.md` |
| 6 | FR-X.2-06 | UC156 | Công khai / Hủy công khai Q&A | KHO_CAU_HOI | M14 | `04-TC-cong-khai-q-and-a.md` |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | `qtht_01` | Permission negative (kỳ vọng READ-only — không phải owner module) |
| CB_NV_TW | TW | `cb_nv_tw_01` (fallback `_02`/`_03`) | CRUD Kho (THU_CONG), tra cứu kho trong phiên, đẩy Nhóm II, công khai/hủy công khai scope TW |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH) | CRUD Kho scope BN — verify phân quyền theo `don_vi_id` |
| CB_NV_DP | DP | `cb_nv_dp_01` (AG) | CRUD Kho scope DP — verify phân quyền dữ liệu |
| CB_PD_TW | TW | `cb_pd_tw_01` (fallback `_02`/`_03`) | Phê duyệt Q&A CHO_DUYET → DA_DUYET (đơn lẻ + hàng loạt) |
| CB_PD_BN | BN | `cb_pd_bn_01` | Phê duyệt scope BN |
| CB_PD_DP | DP | `cb_pd_dp_01` | Phê duyệt scope DP |

> Reference: [input/users.csv](../../../input/users.csv), [input/test-accounts-isolation.csv](../../../input/test-accounts-isolation.csv), [output/permission-matrix.md](../../../output/permission-matrix.md).
>
> **Lưu ý actor ngoài CMS:** DN (gửi câu hỏi + đánh giá) test qua API inbound mock — không dùng tài khoản CMS. Cổng PLQG đóng vai gateway.

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> Cite line theo `input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md` (UPDATE — authoritative) trừ khi note "v3.0" cho line cũ.

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|---------------------|---------------------|-----------|
| BR-AUTH-01 | Xác thực 2-tier: nội bộ user/pass + TOTP; DN qua VNeID SSO | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:854 | ✅ Yes | "API outbound không yêu cầu session (dùng JWT)" — line 857 | Precondition login mọi TC CMS; TC API inbound dùng JWT |
| BR-AUTH-02 | Phân cấp 2 tầng TW → (BN, ĐP cấp 2 song song); BN không có ĐP trực thuộc | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:772 | ✅ Yes | — | TC-KHO-PERM-01 (CB_NV_BN không thấy Q&A của BN khác) |
| BR-AUTH-03 | Ngang cấp KHÔNG thấy nhau | (theo Phụ lục B srs-v3.md) | ✅ Yes | "QTHT thấy tất cả" | TC-KHO-PERM-02 (cb_nv_bn_01 BKH không thấy của cb_nv_bn_02 BTC) |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | (theo Phụ lục B srs-v3.md) | ✅ Yes | — | TC-KHO-PERM-03 data isolation Q&A theo đơn vị |
| BR-DATA-05 | Audit trail CUD + phê duyệt + đăng nhập/xuất; immutable | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:863 | ✅ Yes | — | TC-KHO-018 verify AUDIT_LOG INSERT-only; TC-CK-005 audit hành động CONG_KHAI/HUY_CONG_KHAI |
| BR-DATA-06 | Export Excel max 10k rows | (default toàn dự án) | ✅ Yes | — | TC-KHO-019 export + 10k boundary |
| BR-DATA-07 | Pagination default 20, max 100 | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:546 + 577 ("20 muc/trang") | ✅ Yes | — | TC-KHO-020 + TC-TVN-006 pagination boundary |
| BR-DATA-08 | Tìm kiếm toàn văn GIN trên `cau_hoi + cau_tra_loi + tu_khoa` | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:873 | ✅ Yes | "Các entity khác: search by LIKE/index" — line 877 | TC-KHO-007 full-text search; TC-TVN-003 tra cứu kho trong phiên |
| BR-EC-01 | Optimistic Locking | (theo Phụ lục B srs-v3.md) | ✅ Yes | — | TC-KHO-EDGE-01 conflict UPDATE → ERR-SYS-02 |
| BR-EC-13 | Search sanitize max 200 ký tự | (theo Phụ lục B srs-v3.md) | ✅ Yes | — | TC-KHO-EDGE-02 SQL/XSS/long query 200+; TC-TVN-EDGE-01 ô tra cứu phiên |
| BR-FLOW-05 | Gọi API ra Cổng PLQG; nếu thất bại giữ trạng thái + thông báo lỗi, KHÔNG tự cập nhật trước khi xác nhận từ Cổng | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:894 | ✅ Yes | — | TC-CK-003 API fail → giữ trạng thái + ERR-TVN-CK-01 |
| BR-FLOW-10 | Kho Q&A: 3 nguồn `TU_DONG / THU_CONG / IMPORT` | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:884 | ✅ Yes | — | TC-KHO-001/002/003 tạo Q&A theo 3 nguồn |
| BR-PUBLIC-01 | Chỉ bản ghi `DA_DUYET` mới được công khai; CHO_DUYET / từ chối / hủy = KHÔNG | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:904 | ✅ Yes | — | TC-CK-002 chặn công khai CHO_DUYET → ERR-TVN-CK-03 |
| BR-PUBLIC-02 | Hủy công khai → `cong_khai=0`, `trang_thai` về DA_DUYET, xóa `thoi_gian_dang_tai`, gọi API gỡ | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:914 | ✅ Yes | — | TC-CK-004 hủy → verify `thoi_gian_dang_tai=NULL` |
| BR-PUBLIC-03 | `thoi_gian_dang_tai` auto-fill khi công khai thành công; không sửa tay; format `dd/mm/yyyy hh:mm` | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:924 | ✅ Yes | — | TC-CK-001 verify time set đúng thời điểm gọi API |
| BR-INTG-02 | mTLS + JWT Bearer RS256 cho API inbound | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:376 (FR-X.2-05 API spec) | ✅ Yes | — | TC-TVN-API-001 auth header bắt buộc; missing JWT → 401 |
| BR-IDEMPOTENT-01 | API inbound đánh giá dùng `Idempotency-Key` cache 24h; gửi lại cùng key → 409 Conflict trả kết quả cũ | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:380 + 426 | ✅ Yes | — | TC-TVN-API-002 idempotent gửi lại không tạo bản ghi 2 |

> **Bổ sung BR specific module:** BR-PUBLIC-01/02/03 + BR-IDEMPOTENT-01 + BR-FLOW-10 là BR riêng module X.2. Còn lại là BR cross-cutting áp dụng default.

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Severity |
|--------|-------------------|----------------------|----------|
| ERR-KHO-01 | Câu hỏi trống khi tạo/sửa Q&A | "Câu hỏi là bắt buộc" | ERROR |
| ERR-KHO-02 | Câu trả lời trống | "Câu trả lời là bắt buộc" | ERROR |
| ERR-KHO-03 | Lĩnh vực không hợp lệ (NULL hoặc FK sai) | "Lĩnh vực PL không hợp lệ" | ERROR |
| ERR-KHO-04 | File Excel sai format (không phải .xlsx hoặc cột sai) | "File không đúng định dạng. Tải mẫu Excel" | ERROR |
| ERR-TVN-TK-01 | Từ khóa tìm kiếm < 2 ký tự (FR-X.2-02 step 3 + FR-X.2-04) | "Từ khóa tìm kiếm phải có ít nhất 2 ký tự" | ERROR |
| INF-TVN-TK-01 | Không có kết quả tìm kiếm | "Không tìm thấy câu hỏi phù hợp" | INFO |
| ERR-TVN-02 | Nội dung trả lời rỗng khi gửi | "Nội dung trả lời là bắt buộc" | ERROR |
| ERR-TVN-03 | Đẩy Nhóm II khi phiên đã HOAN_THANH | "Phiên tư vấn đã kết thúc, không thể đẩy sang Nhóm II" | ERROR |
| ERR-TVN-DN-01 | Câu hỏi DN gửi rỗng (API inbound) | "Vui lòng nhập câu hỏi" | ERROR |
| ERR-DG-TVN-01 | Điểm ngoài [1..5] | "Điểm đánh giá phải từ 1 đến 5" | ERROR |
| ERR-DG-TVN-02 | `tu_van_nhanh_id` không tồn tại (API 404) | "Phiên tư vấn không tồn tại" | ERROR |
| ERR-TVN-CK-01 | API ra Cổng PLQG lỗi khi công khai | "Lỗi kết nối Cổng PLQG khi công khai. Vui lòng thử lại" | ERROR |
| ERR-TVN-CK-02 | API ra Cổng PLQG lỗi khi hủy công khai | "Lỗi kết nối Cổng PLQG khi hủy công khai. Vui lòng thử lại" | ERROR |
| ERR-TVN-CK-03 | Trạng thái không hợp lệ cho hành động công khai/hủy (vd CHO_DUYET) | "Không thể thực hiện. Trạng thái hiện tại không cho phép" | ERROR |
| ERR-SYS-02 | Optimistic lock conflict (BR-EC-01) | (theo Phụ lục B — quote khi viết TC detail) | ERROR |

> ⚠️ Message phải quote **nguyên văn** từ SRS lines trên khi test negative. Không chấp nhận "close enough".

### 2.3 Permission Matrix (module-specific)

| Entity / Action | QTHT | CB_NV_TW/BN/DP | CB_PD_TW/BN/DP | DN (qua Cổng) |
|-----------------|------|----------------|----------------|---------------|
| KHO_CAU_HOI — Create (THU_CONG) | R-only | **C** (CHO_DUYET) | R | — |
| KHO_CAU_HOI — Import xlsx | R-only | **C** (tất cả CHO_DUYET) | R | — |
| KHO_CAU_HOI — Auto từ HOI_DAP DA_DUYET | (system) | — (đọc) | — | — |
| KHO_CAU_HOI — Update | — | **U** (record của đơn vị mình) | — | — |
| KHO_CAU_HOI — Phê duyệt CHO_DUYET → DA_DUYET (đơn lẻ + hàng loạt) | — | — | **U** | — |
| KHO_CAU_HOI — Toggle hieu_luc | — | **U** | — | — |
| KHO_CAU_HOI — Công khai / Hủy công khai (FR-X.2-06) | — | **U** (theo phạm vi đơn vị) | — | — |
| KHO_CAU_HOI — Read (DA_DUYET + hieu_luc=true) qua Cổng | — | R | R | **R** (read-only API outbound) |
| TU_VAN_NHANH — Create (CMS UI) | 🚫 (chặn) | 🚫 **CHẶN** — chỉ system tạo từ API inbound | 🚫 | — |
| TU_VAN_NHANH — Create qua API inbound (Cổng PLQG) | — | — | — | **C** (API inbound) |
| TU_VAN_NHANH — Read / Reply / Đẩy Nhóm II | — | **R+U** | R | — |
| DANH_GIA_TV — Create | — | — | — | **C** (API inbound từ Cổng) |

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md). Phân biệt CMS UI vs API inbound — TU_VAN_NHANH chỉ có 1 entry point: API inbound từ Cổng PLQG.

### 2.4 UI Layout

> ⚠️ KHÔNG dùng absence (UI không list X) để khẳng định "module KHÔNG có X" — đối chiếu §2.1 BR table trước.

#### SCR-X2-01 — Quản lý Kho Câu hỏi (M14)

**Components** (trích từ `srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:524-547`):

- **Toolbar**: Breadcrumb "Trang chu > Tu van > Kho cau hoi" + Tiêu đề + nút `[+ Thêm câu hỏi]` `[Nhập Excel]` `[Làm mới]`.
- **Filter-bar**: 3 tabs (Tất cả / Đã duyệt / Chờ duyệt) badge đếm; filter Lĩnh vực + Nguồn + Trạng thái (NHAP/CHO_DUYET/DA_DUYET/CONG_KHAI/HET_HIEU_LUC) + Full-text search input.
- **Table**: Mã (QA-YYYYMMDD-SEQ) / Câu hỏi (cắt 100) / Câu trả lời (cắt 100) / Lĩnh vực / Từ khóa (tags, max 3 + "+N") / Nguồn (nhãn màu TU_DONG xanh / THU_CONG vàng / IMPORT tím) / Trạng thái / **Công khai** (badge "Chưa công khai" / "Đã công khai" + `thoi_gian_dang_tai` dd/mm/yyyy hh:mm) / Hiệu lực (toggle) / Điểm TB / Ngày tạo / Hành động (Xem / Sửa / **Công khai** / **Hủy công khai**).
- **Modal "Thêm câu hỏi"**: Câu hỏi (textarea, BB) / Câu trả lời (Rich Text C16, BB) / Lĩnh vực (dropdown, BB) / Từ khóa (tag input) / **Ảnh đại diện** (upload jpg/png/gif, max 5MB) / **Mô tả công khai** (textarea dài) / **File đính kèm công khai** (PDF/DOC/DOCX/XLS/XLSX, max 20MB/file, nhiều file) / `[Hủy]` `[Lưu nháp]` `[Gửi duyệt]`.
- **Modal "Nhập Excel"**: upload .xlsx → preview 10 dòng đầu → báo "N thành công / M lỗi".
- **Action Phê duyệt** (tab Chờ duyệt): `[Duyệt]` / `[Từ chối]` modal lý do BB / `[Duyệt hàng loạt]` checkbox ≥ 1 (không có "từ chối hàng loạt").
- **Action Công khai** (dòng Q&A `DA_DUYET`): nút `[Công khai]` → modal xác nhận hiện preview `anh_dai_dien` / `mo_ta_cong_khai` / `file_dinh_kem_cong_khai` → submit → gọi API ra Cổng PLQG. Dòng `CONG_KHAI`: nút `[Hủy công khai]`.
- **Footer**: Pagination 20/page.

#### SCR-X2-03 — Quản lý Tư vấn Nhanh (M13)

**Components** (trích từ `srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:562-587`):

- **Toolbar**: Breadcrumb + Tiêu đề `[Làm mới]`. **🚫 KHÔNG có nút `[Thêm mới]`** — phiên chỉ tạo từ API inbound (FR-X.2-03 step 6 + `system-overview.md` §4.14 dòng 502).
- **Filter-bar v3.5**: 3 tabs (Tất cả / Chờ xử lý = MOI + CB_TRA_LOI / Hoàn thành = HOAN_THANH + HET_HAN). ⚠️ **Khác v3.0** vốn có 4 tab — v3.5 bỏ tab "Đã gợi ý" vì lifecycle rút gọn.
- **Table**: Mã phiên / Câu hỏi DN (cắt 100) / Kênh (TV_NHANH xanh / TV_THU_CONG vàng) / **CB xử lý** (mới v3.5 — thay "Số gợi ý") / Trạng thái SM-TVNHANH / Ngày gửi / **Ngày trả lời** / Ngày cập nhật / Hành động (Xem / Trả lời).
- **Layout trả lời 2 cột**:
  - **Cột trái (40%)**: Mã phiên + Trạng thái; Thông tin DN; Câu hỏi DN (card nền nhạt); Lịch sử trao đổi (chat bubbles).
  - **Cột phải (60%)** — **Khu vực "Tra cứu Kho câu hỏi"** (v3.5): search input rỗng (placeholder "Nhập từ khóa, nội dung câu hỏi hoặc cụm từ pháp lý") + nút `[Tìm kiếm]` + filter Lĩnh vực PL. **Không auto-search + không prefill câu hỏi DN.** Backend chỉ trả Q&A `trang_thai IN ('DA_DUYET','CONG_KHAI')` và `hieu_luc=true`. Mỗi kết quả: Mã / Câu hỏi (bold) / Câu trả lời rút gọn / Lĩnh vực / Từ khóa / Relevance (%) / `[Chọn]`. Click `[Chọn]` → copy `cau_tra_loi` vào ô soạn (Rich Text C16, cho chỉnh sửa). Nút `[Gửi trả lời]` + nút phụ **`[Đẩy sang Nhóm II]`** (warning color).
- **Section đánh giá** (tab Hoàn thành / chi tiết phiên): Điểm 1-5 sao + Nhận xét DN + Ngày đánh giá + thẻ tổng hợp (COUNT / AVG / phân bố bar chart) + `[Xuất Excel]`.
- **Footer**: Pagination 20/page.

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**
- ☐ Pagination 20/page default (BR-DATA-07) — verified ở §3 dòng 546, 577.
- ☐ Search sanitize max 200 ký tự (BR-EC-13) — áp dụng cả 2 màn.
- ☐ Audit log mọi CUD + phê duyệt + công khai/hủy (BR-DATA-05).
- ☐ Optimistic lock UPDATE/DELETE (BR-EC-01).
- ☐ Export Excel (BR-DATA-06) — verified với nút `[Xuất Excel]` section đánh giá; cần verify SCR-X2-01 (table Q&A) có nút Export không (UI spec không liệt kê → cần BA clarify hoặc SPEC-CLARIFY).

**Feature module KHÔNG có:**
- 🚫 **Nút "Thêm mới" trên SCR-X2-03 phiên TV nhanh** — QUOTE: `system-overview.md` §4.14 dòng 502 "🚫 KHÔNG có nút Thêm mới — DN gõ chat trên Cổng PLQG"; `02-thu-tu-module.md` dòng 939 "FR-13 TV Nhanh KHÔNG có API outbound riêng" và phiên chỉ sinh từ inbound.
- 🚫 **Auto-gợi ý TOP 5 trên phiên TV nhanh** (v3.0 cũ) — QUOTE: `srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:173` "Hệ thống không tự động tìm kiếm mặc định và không hiển thị gợi ý tự động". v3.0 → v3.5 thay đổi.
- 🚫 **State `DANG_TIM_KIEM` + `DA_GOI_Y`** (v3.0) — QUOTE: §5 SM-TVNHANH v3.5 chỉ còn 4 state (line 815-820).

### 2.5 State Machine

#### SM-TVNHANH (Phiên TV nhanh — M13)

```
[*] --DN gửi câu hỏi qua API inbound--> [MOI]
[MOI] --CB NV tiếp nhận / mở xử lý--> [CB_TRA_LOI]
[MOI] --auto 30 ngày không xử lý--> [HET_HAN]
[CB_TRA_LOI] --DN đánh giá (điểm 1-5 qua API inbound)--> [HOAN_THANH]
[CB_TRA_LOI] --CB NV Đẩy sang Nhóm II--> [HOAN_THANH] (ghi chú "Đã đẩy Nhóm II #ma_hoi_dap")
```

**Bảng transition** (cite `srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:823-829`):

| Từ | Đến | Trigger | Guard | Action | FR Ref |
|----|-----|---------|-------|--------|--------|
| [*] | MOI | DN gửi câu hỏi qua Cổng (API inbound) | — | Tạo `TU_VAN_NHANH` | FR-X.2-03 |
| MOI | CB_TRA_LOI | CB NV mở chi tiết / tiếp nhận | — | Set `cb_xu_ly_id` = current user; hiển thị khu vực Tra cứu Kho (không auto-search) | FR-X.2-02 |
| CB_TRA_LOI | HOAN_THANH | DN đánh giá (API inbound POST /api/v1/inbound/danh-gia-tv-nhanh) | `diem ∈ [1..5]` | Lưu DANH_GIA_TV; update `diem_tb` Q&A nếu có | FR-X.2-05 |
| CB_TRA_LOI | HOAN_THANH | CB NV/TVV click `[Đẩy sang Nhóm II]` | Phiên chưa HOAN_THANH | Tạo HOI_DAP `kenh_tiep_nhan=TVN_BRIDGE` + `tu_van_nhanh_goc_id`; đóng phiên ghi chú | FR-X.2-02 step 9 |
| MOI | HET_HAN | Auto batch job | `elapsed > 30 ngày` | TB CB NV | FR-X.2-02 |

> **Lưu ý:** Không có transition `HOAN_THANH → *` (terminal state). Đẩy Nhóm II từ trạng thái HOAN_THANH bị chặn → ERR-TVN-03.

#### SM-KHOCAUHOI (Kho Q&A — M14)

```
                  ┌──── (auto FR-02 HOI_DAP=DA_DUYET) ────┐
                  │      → nguồn=TU_DONG                  ▼
[FR-02 DA_DUYET] ─────────────────────────────────────► [DA_DUYET]
                                                        │
                                                        │ CB NV [Công khai] + API thành công
                                                        ▼
[—] ──CB NV nhập THU_CONG / IMPORT──> [CHO_DUYET]      [CONG_KHAI]
[CHO_DUYET] ──CB PD [Duyệt]──────────► [DA_DUYET]      │
[CHO_DUYET] ──CB PD [Từ chối]────────► [NHAP] (lý do bắt buộc)
[CONG_KHAI] ──CB NV [Hủy công khai] + API gỡ thành công─► [DA_DUYET]
[DA_DUYET] / [CONG_KHAI] ──CB NV toggle hieu_luc=0───► (vẫn DA_DUYET/CONG_KHAI nhưng ẩn khỏi Cổng)
[*] ──CB NV "Hết hiệu lực"──> [HET_HIEU_LUC]
```

**Bảng transition** (cite `srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:457-477` + `02-thu-tu-module.md:781-785`):

| Từ | Đến | Actor | Trigger | Guard | Action | FR Ref |
|----|-----|-------|---------|-------|--------|--------|
| (FR-02 DA_DUYET) | DA_DUYET | System | Auto feed khi HOI_DAP → DA_DUYET | — | Tạo Q&A `nguon=TU_DONG` + `hoi_dap_goc_id` | FR-X.2-01 step 2 |
| — | CHO_DUYET | CB NV | Nhập THU_CONG (modal Thêm câu hỏi) | Câu hỏi + trả lời + lĩnh vực BB | INSERT Q&A `nguon=THU_CONG` | FR-X.2-01 step 3 |
| — | CHO_DUYET | CB NV | Upload xlsx (modal Nhập Excel) | File hợp lệ | INSERT batch `nguon=IMPORT` | FR-X.2-01 step 4 |
| CHO_DUYET | DA_DUYET | CB PD | `[Duyệt]` đơn lẻ | — | `hieu_luc=1`; TB CB NV | UC155 |
| CHO_DUYET | DA_DUYET | CB PD | `[Duyệt hàng loạt]` | ≥ 1 checkbox | Batch update | UC155 |
| CHO_DUYET | NHAP | CB PD | `[Từ chối]` | Lý do BB | Modal lý do → set NHAP | UC155 |
| DA_DUYET | CONG_KHAI | CB NV | `[Công khai]` (BR-PUBLIC-01) | trạng thái = DA_DUYET; API Cổng PLQG thành công | Set `cong_khai=1` + `thoi_gian_dang_tai = NOW()` (BR-PUBLIC-03) | FR-X.2-06 |
| CONG_KHAI | DA_DUYET | CB NV | `[Hủy công khai]` | API Cổng PLQG thành công | `cong_khai=0` + xóa `thoi_gian_dang_tai` (BR-PUBLIC-02) | FR-X.2-06 |
| any | HET_HIEU_LUC | CB NV | Toggle hieu_luc off + đánh dấu | — | Ẩn khỏi Cổng + khỏi kết quả tra cứu | FR-X.2-01 step 6 |

> **Lưu ý fail-API:** Khi gọi API ra Cổng PLQG **thất bại**, hệ thống **giữ trạng thái cũ** (BR-FLOW-05) → DA_DUYET vẫn DA_DUYET, CONG_KHAI vẫn CONG_KHAI; chỉ hiển thị toast lỗi ERR-TVN-CK-01/02.

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| GĐ 1 Seed | (TBD `input/data/seed-fixture.yaml` — entity `kho_cau_hoi`, `tu_van_nhanh`, `danh_gia_tv` — chưa có ở v3.0; cần update fixture cho 5 trường công khai v3.5) | Variants theo Lĩnh vực × Nguồn × Trạng thái |
| GĐ 1 click flow | [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) §⑫ FR-13 dòng 746-790 | Workflow nhập tay THU_CONG + Import xlsx |
| GĐ 2 Workflow | `02-thu-tu-module.md` §⑫ + Phụ lục troubleshooting | Full lifecycle CHO_DUYET → DA_DUYET → CONG_KHAI |
| Cross-module map | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | KHO_CAU_HOI tạo tại M14 / đọc tại phiên M13 + Cổng PLQG; TU_VAN_NHANH tạo tại API inbound / đọc tại M13 |

**Upstream dependencies (Tier check):**

| Entity của module | Tier | Phụ thuộc upstream | Seed trước tại module |
|-------------------|:----:|--------------------|-----------------------|
| KHO_CAU_HOI (TU_DONG) | 3 | `HOI_DAP` ở DA_DUYET | M7 FR-02 Hỏi đáp |
| KHO_CAU_HOI (THU_CONG/IMPORT) | 3 | `DANH_MUC` Lĩnh vực PL | M1 FR-10 QTHT |
| KHO_CAU_HOI (anh_dai_dien / file_dinh_kem) | 3 | (Không có upstream — upload trực tiếp) | — |
| TU_VAN_NHANH | 4 | `DOANH_NGHIEP` (DN gửi câu hỏi) + `KHO_CAU_HOI` DA_DUYET ≥ 1 record (để CB NV tra cứu) | M2 FR-07 DN + M14 (TU_DONG hoặc THU_CONG đã duyệt) |
| DANH_GIA_TV | 4 | `TU_VAN_NHANH` ở CB_TRA_LOI | M13 sau khi CB NV trả lời |
| KHO_CAU_HOI → CONG_KHAI | 4 | Q&A đã DA_DUYET + Cổng PLQG sandbox up (mTLS endpoint) | M14 (sau duyệt) + Infra (Cổng PLQG mock) |

> **🔴 Note đặc biệt — Phiên TV nhanh KHÔNG nhập tay:** TC tạo dữ liệu test cho M13 BẮT BUỘC gọi API inbound `POST /api/v1/inbound/tu-van-nhanh` (mock từ Cổng PLQG). KHÔNG có UI tạo phiên trên CMS. QA seed dùng curl hoặc Postman mock body theo FR-X.2-03 Inputs (`cau_hoi`, `kenh_tu_van`, `doanh_nghiep_id`).

---

## 3. Cấu Trúc File Test Case

```
fr-13-tv-nhanh/
├── test-plan.md                       ← File này (overview)
├── 01-TC-kho-cau-hoi.md                ← M14 — CRUD Q&A + 3 nguồn + phê duyệt + tìm kiếm + permission
├── 02-TC-phien-tv-nhanh.md             ← M13 — API inbound + tra cứu kho + trả lời + đẩy Nhóm II + đánh giá inbound
├── 03-TC-cong-khai-search.md           ← FR-X.2-04 — DN tìm kiếm phản hồi qua Cổng PLQG (read-only)
├── 04-TC-cong-khai-q-and-a.md          ← FR-X.2-06 — Công khai / Hủy công khai + BR-PUBLIC-01/02/03
└── (05-REVIEW-edge-case-hunter.md)     ← Optional review
```

---

## 4. Tổng Quan Test Cases

### 4.1 Bảng TC chi tiết (≥20 TC)

> P0 = bắt buộc PASS để release; P1 = quan trọng (≥90% PASS); P2 = nên có.

#### M14 — Kho Q&A (SCR-X2-01) — 14 TC

| TC ID | Tên | Loại | Priority | FR / BR ref | File |
|---|---|:-:|:-:|---|---|
| TC-KHO-001 | Tạo Q&A THU_CONG hợp lệ → CHO_DUYET | Happy | P0 | FR-X.2-01, BR-FLOW-10 | 01 |
| TC-KHO-002 | Auto-feed Q&A TU_DONG khi HOI_DAP→DA_DUYET | Happy | P0 | FR-X.2-01 step 2, BR-FLOW-10 | 01 |
| TC-KHO-003 | Import xlsx → preview 10 dòng → tạo CHO_DUYET batch | Happy | P0 | FR-X.2-01 step 4 | 01 |
| TC-KHO-004 | Phê duyệt đơn lẻ CHO_DUYET → DA_DUYET | Happy | P0 | UC155 | 01 |
| TC-KHO-005 | Phê duyệt hàng loạt ≥ 1 checkbox | Happy | P1 | UC155 | 01 |
| TC-KHO-006 | Từ chối CHO_DUYET → NHAP (lý do BB) | Happy | P1 | UC155 | 01 |
| TC-KHO-007 | Full-text search GIN `cau_hoi + cau_tra_loi + tu_khoa` | Happy | P0 | BR-DATA-08 | 01 |
| TC-KHO-008 | Toggle hieu_luc OFF → ẩn Cổng + ẩn kết quả tra cứu phiên | Happy | P1 | FR-X.2-01 step 6 | 01 |
| TC-KHO-NEG-01 | Tạo Q&A câu hỏi rỗng → ERR-KHO-01 | Negative | P0 | ERR-KHO-01 | 01 |
| TC-KHO-NEG-02 | Tạo Q&A câu trả lời rỗng → ERR-KHO-02 | Negative | P0 | ERR-KHO-02 | 01 |
| TC-KHO-NEG-03 | Tạo Q&A lĩnh vực NULL → ERR-KHO-03 | Negative | P1 | ERR-KHO-03 | 01 |
| TC-KHO-NEG-04 | Import xlsx sai format → ERR-KHO-04 | Negative | P1 | ERR-KHO-04 | 01 |
| TC-KHO-PERM-01 | CB_NV_BN BKH KHÔNG thấy Q&A của BTC (BR-AUTH-03) | Permission | P0 | BR-AUTH-03 | 01 |
| TC-KHO-PERM-02 | DN qua Cổng chỉ thấy Q&A DA_DUYET/CONG_KHAI + hieu_luc=true | Permission | P0 | FR-X.2-04 step 2 | 03 |

#### M13 — Phiên TV nhanh (SCR-X2-03) — 6 TC

| TC ID | Tên | Loại | Priority | FR / BR ref | File |
|---|---|:-:|:-:|---|---|
| TC-TVN-001 | API inbound `POST /tu-van-nhanh` tạo phiên MOI | Happy | P0 | FR-X.2-03 step 6 | 02 |
| TC-TVN-002 | CB NV mở phiên MOI → chuyển CB_TRA_LOI; khu vực Tra cứu rỗng (không auto-search) | Happy | P0 | FR-X.2-02 step 2 + AC line 232 | 02 |
| TC-TVN-003 | CB NV nhập từ khóa ≥ 2 ký tự + nhấn Tìm kiếm → trả Q&A `DA_DUYET/CONG_KHAI + hieu_luc=true`, relevance DESC | Happy | P0 | FR-X.2-02 step 4 | 02 |
| TC-TVN-004 | CB NV click `[Chọn]` → copy `cau_tra_loi` vào ô soạn → chỉnh sửa → `[Gửi trả lời]` → lưu `noi_dung_tra_loi` + `cb_xu_ly_id` + `ngay_tra_loi` + `thoi_gian_xu_ly_phut` | Happy | P0 | FR-X.2-02 step 6-7 | 02 |
| TC-TVN-005 | CB NV soạn thủ công (không chọn Q&A) → gửi trả lời thành công | Happy | P1 | FR-X.2-02 step 6 | 02 |
| TC-TVN-006 | CB NV click `[Đẩy sang Nhóm II]` → modal xác nhận → tạo HOI_DAP `kenh_tiep_nhan=TVN_BRIDGE` + `tu_van_nhanh_goc_id`; phiên → HOAN_THANH ghi chú | Happy | P0 | FR-X.2-02 step 9 | 02 |
| TC-TVN-NEG-01 | Từ khóa tìm kiếm < 2 ký tự → ERR-TVN-TK-01 | Negative | P1 | ERR-TVN-TK-01 | 02 |
| TC-TVN-NEG-02 | Gửi trả lời nội dung rỗng → ERR-TVN-02 | Negative | P0 | ERR-TVN-02 | 02 |
| TC-TVN-NEG-03 | Đẩy Nhóm II khi phiên đã HOAN_THANH → ERR-TVN-03 | Negative | P1 | ERR-TVN-03 | 02 |
| TC-TVN-NEG-04 | SCR-X2-03 UI **không có nút `[Thêm mới]`** (verify chặn nhập tay) | Negative | P0 | system-overview §4.14 dòng 502 | 02 |
| TC-TVN-API-001 | API inbound đánh giá thiếu JWT/mTLS → 401 (BR-INTG-02) | Negative | P0 | BR-INTG-02 | 02 |
| TC-TVN-API-002 | API inbound đánh giá idempotent: gửi lại cùng `Idempotency-Key` → 409 trả kết quả cũ, KHÔNG tạo bản ghi 2 | Edge | P0 | BR-IDEMPOTENT-01 | 02 |
| TC-TVN-API-003 | API inbound đánh giá `tu_van_nhanh_id` không tồn tại → 404 ERR-DG-TVN-02 | Negative | P1 | ERR-DG-TVN-02 | 02 |
| TC-TVN-API-004 | API inbound đánh giá điểm ngoài [1..5] → 400 ERR-DG-TVN-01 | Negative | P1 | ERR-DG-TVN-01 | 02 |

#### FR-X.2-06 — Công khai Q&A — 9 TC (revised 2026-05-12 13:30:00 — +G3 upload boundary, +G4 permission, +S2/S6)

| TC ID | Tên | Loại | Priority | FR / BR ref | File |
|---|---|:-:|:-:|---|---|
| TC-CK-001 | Công khai Q&A DA_DUYET → API thành công → CONG_KHAI + `thoi_gian_dang_tai` set (BR-PUBLIC-03) | Happy | P0 | FR-X.2-06 + BR-PUBLIC-03 | 04 |
| TC-CK-002 | Cố công khai Q&A CHO_DUYET → ERR-TVN-CK-03 + chặn (BR-PUBLIC-01) | Negative | P0 | BR-PUBLIC-01 + ERR-TVN-CK-03 | 04 |
| TC-CK-003 | Công khai khi API Cổng PLQG fail → giữ DA_DUYET + ERR-TVN-CK-01 (BR-FLOW-05) | Negative | P0 | BR-FLOW-05 + ERR-TVN-CK-01 | 04 |
| TC-CK-004 | Hủy công khai CONG_KHAI → DA_DUYET + `thoi_gian_dang_tai=NULL` (BR-PUBLIC-02) | Happy | P0 | BR-PUBLIC-02 | 04 |
| TC-CK-005 | Audit log ghi action `CONG_KHAI` + `HUY_CONG_KHAI` + người thực hiện | Happy | P1 | BR-DATA-05 | 04 |
| **TC-CK-CR01-01** | **Validate `anh_dai_dien` upload 5MB jpg/png/gif OK + boundary 5.1MB → reject + MIME deep check (rename `.exe` → `.jpg` reject)** | Edge | **P0** | CR-01 SRS line 105/704 | 04 |
| **TC-CK-CR01-02** | **Validate `file_dinh_kem_cong_khai` upload 20MB PDF OK + boundary 20.1MB reject + sai mime (PDF/DOC/DOCX/XLS/XLSX only — .zip/.exe reject) + 0-byte file reject** | Edge | **P0** | CR-01 SRS line 107/705 | 04 |
| **TC-CK-PERM-01** | **CB_NV_BN BKH KHÔNG được công khai Q&A của đơn vị BTC (BR-AUTH-08 + BR-PUBLIC) — nút `[Công khai]` ẩn HOẶC click → 403; verify scope `don_vi_id` filter SRS line 461** | Permission | **P0** | FR-X.2-06 + BR-AUTH-08 + BR-PUBLIC-01 | 04 |
| **TC-CK-PERM-02** | **CB_NV_DP AG KHÔNG thấy Q&A DP khác (vd CTKH) trong list công khai — same scope `don_vi_id`** | Permission | P1 | BR-AUTH-03 + BR-AUTH-08 | 04 |

#### Edge / Cross-cutting — 4 TC

| TC ID | Tên | Loại | Priority | FR / BR ref | File |
|---|---|:-:|:-:|---|---|
| TC-KHO-EDGE-01 | Optimistic lock: 2 user sửa cùng Q&A → 2nd → ERR-SYS-02 | Edge | P1 | BR-EC-01 | 01 |
| TC-KHO-EDGE-02 | Search SQL injection / XSS / query 201 ký tự → sanitize (BR-EC-13) | Edge | P1 | BR-EC-13 | 01 |
| TC-KHO-018 | AUDIT_LOG INSERT-only verify (sau CUD Q&A + duyệt + công khai) | Cross-cutting | P1 | BR-DATA-05 | 01 |
| TC-KHO-020 | Pagination boundary 20 default / 100 max / vượt trang cuối | Edge | P2 | BR-DATA-07 | 01 |

**Tổng: 37 TC** (M14: 14 + M13: 14 + CK: 9 + 4 edge cross-cutting; nằm trong scope ≥20 TC, ≥6 Phiên, ≥14 Kho Q&A). _Revised 2026-05-12 13:30:00: +4 TC nhóm CK (CR-01 upload boundary x2 + permission cross-don_vi x2)._

### 4.2 Phân bổ theo loại

| File | Happy | Negative | Edge | Permission | Tổng |
|------|:-----:|:--------:|:----:|:----------:|:----:|
| 01-TC-kho-cau-hoi.md (M14) | 8 | 4 | 2 | 1 | 15 |
| 02-TC-phien-tv-nhanh.md (M13) | 6 | 4 | 1 | — | 11 |
| 03-TC-cong-khai-search.md | 1 | — | — | 1 | 2 |
| 04-TC-cong-khai-q-and-a.md (FR-X.2-06) | 3 | 2 | 2 | 2 | 9 |
| **TỔNG** | **18** | **10** | **5** | **4** | **37** |

### 4.3 Phân bổ priority (revised 2026-05-12)

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc) | 21 | 57% |
| P1 (quan trọng) | 13 | 35% |
| P2 (nên có) | 3 | 8% |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md).

- ✅ **PASS:** 100% P0 + ≥ 90% P1 PASS. Bug Major/Critical đều có evidence + cite SRS line.
- ❌ **FAIL:** bất kỳ P0 nào FAIL, hoặc P1 PASS rate < 90%.
- ⚠️ **PARTIAL:** một số TC `🚫 Không test được` do thiếu seed (vd Cổng PLQG sandbox down) → log nhóm D (`output/template/tc-block-classification-template.md`) + đề xuất unblock cụ thể (Infra / BA / QA seed).

**Đặc biệt cho v3.5:**
- TC-TVN-NEG-04 (verify chặn nhập tay) là P0 — fail = SCR sai spec dòng 502 system-overview.
- TC-CK-003 (API fail giữ trạng thái) là P0 — quan trọng vì BR-FLOW-05 chống "tự cập nhật trước khi xác nhận".
- TC-TVN-API-002 (Idempotency) là P0 — chống ghi đè sai lệch CSV UC158.

---

## 6. Tham chiếu

- [input/srs-v3/srs-fr-13-tv-nhanh.md](../../../input/srs-v3/srs-fr-13-tv-nhanh.md) — SRS v3.0 (reference cũ)
- [input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md](../../../input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md) — **SRS v3.5 authoritative**
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) §⑫ FR-13 dòng 746-790
- [tasks/system-overview.md](../../../tasks/system-overview.md) §4.14 (M13) + §4.15 (M14)
- [input/users.csv](../../../input/users.csv) — 9 CB_NV (TW/BN/DP × 3) + 9 CB_PD + QTHT
- [output/permission-matrix.md](../../../output/permission-matrix.md) — ma trận phân quyền 49 entity × 11 role
- [output/test-strategy.md](../../../output/test-strategy.md)
- [output/template/test-case-template.md](../../../output/template/test-case-template.md)
- [output/template/bug-report-template.md](../../../output/template/bug-report-template.md)
- [output/template/tc-block-classification-template.md](../../../output/template/tc-block-classification-template.md)

---

## 7. Ambiguity / SPEC-CLARIFY cần BA xác nhận

| # | Vấn đề | Tham chiếu | Đề xuất |
|---|--------|-----------|---------|
| 1 | UI spec SCR-X2-01 không liệt kê nút `[Xuất Excel]` cho table Q&A — chỉ có ở section đánh giá M13 | BR-DATA-06 default vs §3 dòng 535 không có nút | Hỏi BA: kho có export Excel không? Nếu có, đặt ở đâu? |
| 2 | FR-X.2-04 (DN tìm kiếm qua Cổng) read-only Q&A `DA_DUYET` (v3.5 line 314) — nhưng FR-X.2-02 step 4 (CB NV tra cứu) chấp `DA_DUYET + CONG_KHAI` — không nhất quán | line 199 vs line 314 | Hỏi BA: DN qua Cổng có thấy CONG_KHAI khác DA_DUYET không, hay chỉ CONG_KHAI? |
| 3 | Endpoint API outbound search cho Cổng PLQG chưa có ở FR-16 | `02-thu-tu-module.md` dòng 939 "TODO UNVERIFIED" | Hỏi CĐT spec endpoint outbound search Kho QA |
| 4 | API inbound DN gửi câu hỏi `POST /api/v1/inbound/tu-van-nhanh` chưa có spec endpoint chi tiết trong SRS FR-13 | line 273 (chỉ mô tả "qua API inbound") | Hỏi BA endpoint path + payload schema |
| 5 | `kenh_tu_van` enum trong TU_VAN_NHANH = `'NHANH'/'THU_CONG'` (line 719) nhưng FR-X.2-03 input ghi `TV_NHANH/TV_THU_CONG` (line 262) | mâu thuẫn naming | Hỏi BA chốt enum values |
| 6 | "Đẩy sang Nhóm II" — phân biệt actor "CB NV/TVV chủ động" (FR-X.2-02 step 9) vs "DN chuyển kênh giữa chừng" (FR-X.2-03 step 5) — cả 2 tạo HOI_DAP TVN_BRIDGE | line 204 + line 272 | Verify có 2 entry point khác nhau (CB NV button + DN button trên Cổng); BA confirm |
| 7 | SM-TVNHANH transition `CB_TRA_LOI → HOAN_THANH` qua "Đẩy Nhóm II" — có cần điểm đánh giá DN không? | line 216 + AC line 236 | Nếu Đẩy Nhóm II không yêu cầu đánh giá DN, lifecycle phải document rõ "đóng phiên không qua đánh giá" |
| **8 (G2 — review 2026-05-12)** | **State `NHAP` UI/Inputs có (line 103/537/543) NHƯNG CHECK constraint entity line 697 KHÔNG có `NHAP`** — mâu thuẫn nội bộ SRS. Từ chối CHO_DUYET → set `trang_thai='NHAP'` sẽ violate CHECK constraint. | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:103, 537, 543 vs 697 | Hỏi BA: (a) CHECK constraint thiếu `NHAP` — fix migration, hoặc (b) từ chối → xóa record, không set state, hoặc (c) state name khác (`TU_CHOI`?). Chốt enum + cập nhật ER. |
| **9 (G9 — review 2026-05-12)** | **Transition `CB_TRA_LOI → HOAN_THANH` qua "Đẩy Nhóm II" có ở FR-X.2-02 step 9 + AC line 236 nhưng KHÔNG có trong bảng SM-TVNHANH chính thức (line 823-829)** — plan §2.5 extrapolate từ business logic. | srs-update-2026-5-5/srs-fr-13-tv-nhanh.md:204, 236 vs 823-829 | Hỏi BA: cập nhật SM table thêm row `CB_TRA_LOI → HOAN_THANH` trigger "CB NV/TVV click Đẩy Nhóm II" + action "Tạo HOI_DAP TVN_BRIDGE + đóng phiên ghi chú". |

---

*Template generated 2026-05-12 — Plan Drafter agent. SRS v3.5 authoritative; v3.0 chỉ tham chiếu lifecycle cũ. Cần BA sign-off Section 7 trước khi viết TC detail.*
