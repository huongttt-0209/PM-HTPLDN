# DANH SÁCH ITEM CẦN BA CONFIRM — 4 MODULE
**Phạm vi:** Đào tạo · Biểu mẫu · CT HTPLDN · QTHT
**Cập nhật:** 2026-05-11 19:45
**Nguồn:** Grep toàn bộ bug-reports + functional/workflow reports R7-R11 (4 module)

---

## Tổng quan

| Module | Số item cần BA | Mức độ block release |
|---|:-:|:-:|
| **Đào tạo** | 13 | 🔴 Block GA (3 spec contradiction lớn) |
| **Biểu mẫu** | 1 | 🟢 Không block (chỉ spec ambiguity) |
| **CT HTPLDN** | 5 | 🟡 Block 1 edge case (B10 "0/0 đợt BC") |
| **QTHT** | 8 | 🟡 Phần lớn cleanup spec/error code naming |
| **Cross-cutting** | 3 | 🟡 Pattern consistency |
| **TỔNG** | **30** | |

---

## 🔴 ƯU TIÊN P0 — Block release nếu không có quyết định BA

### #1 — VPD bypass cho dữ liệu `congKhai=true` (Đào tạo + cross-cutting)

**Vấn đề:** DN/NHT login CMS có permission `create_dang_ky_dao_tao` + `read_khoa_hoc` nhưng VPD guard chặn access KH `congKhai=true` cross-đơn-vị → 403 `ERR-AUTH-VPD-00-02`. Pool 7 KH (4 congKhai=true) → DN/NHT thấy `total=0`.

**Cần BA quyết:** BR-AUTH-08 có quy định **bypass VPD khi `congKhai=true`** không?
- (a) **Có bypass** → BE fix logic, DN/NHT thấy KH công khai cross-đơn-vị, đăng ký HV qua chuyên trang chạy được.
- (b) **Không bypass** → cần thiết kế lại flow FR-III-04 UC23 vì spec hiện tại không khả thi.

**Spec ref:** `FR-III-04 UC23` + `BR-PUBLIC-01` + `BR-AUTH-08` · **Bug:** BUG-DT-CT-VPD-01 Major Open · **Impact:** Block 9 TC HV-related

---

### #2 — Cross-tenant leak GET KH năm (Đào tạo)

**Vấn đề:** `GET /api/v1/ke-hoach-dao-taos` không filter `donViId` — TW/BN/ĐP đều thấy KH năm của tất cả đơn vị (3 user khác cấp đều thấy 7 record từ 3 donViId khác nhau). Vi phạm BR-AUTH-08 trực tiếp. RE-CONFIRMED qua R10 + R11.

**Cần BA quyết:** Phạm vi xem KH năm của CB NV/PD theo cấp là gì?
- CB NV/PD TW: thấy mọi cấp (TW+BN+ĐP) hay chỉ TW own?
- CB NV/PD BN: thấy BN own + DP scope dưới, hay chỉ BN own?
- CB NV/PD DP: chỉ DP own?

**Bonus:** R7.4.B0 R9 phát hiện `cb_pd_bn_02` thấy ALL 7 records TW+BN+DP — read scope rộng hơn approve scope → spec rule chưa rõ.

**Spec ref:** `BR-AUTH-08 line 1903` + `FR-III-14 Processing-Xem danh sách Bước 2 BR-DATA-02` · **Bug:** BUG-KH-001 Major Open

---

### #3 — Khóa học state machine spec vs impl (Đào tạo)

**Vấn đề:** Spec R7.4.B7 ghi 11 trạng thái + state "Từ chối" riêng, nhưng UI/BE thực tế ~6 trạng thái và "Từ chối" = quay về "Dự thảo" (không có state TU_CHOI độc lập).

**Cần BA quyết:** 
- (a) **Giữ spec 11-state** → dev phải add state TU_CHOI + 5 trạng thái còn thiếu
- (b) **Update SRS theo BE thực tế** (~6 state + reject về DU_THAO) → cleanup doc

**Spec ref:** R7.4.B7 SRS · **Note:** R7.4.B11 + B10 + B0 đều thấy pattern "reject → quay về NHAP/DU_THAO", không có state TU_CHOI riêng

---

### #4 — ĐKT (Đề kiểm tra) state machine 2-state vs spec (Đào tạo)

**Vấn đề:** ĐKT thực tế 2-state (`NHAP` → `DA_PHAN_PHOI`). Spec FR-III-NEW-02 không quote rule duyệt nên BE implement không có CHO_DUYET / DA_DUYET. R7.4.B10 R9-R10 bị block khi muốn test "Trình duyệt" + "Phê duyệt".

**Cần BA quyết:** 
- (a) ĐKT có cần workflow duyệt như CTĐT/Khóa học không?
- (b) Định nghĩa "chưa sử dụng" để DELETE (FR-III-NEW-02 line 1354): là "state ≠ DA_PHAN_PHOI" hay "chưa link KQHT"?

**Spec ref:** `FR-III-NEW-02 line 1354` · **Impact:** R7.4.B10 verify rule "Xóa chỉ khi chưa sử dụng"

---

### #5 — CT HTPLDN B10 HOAN_THANH "0/0 đợt BC" edge case

**Vấn đề:** BE chặn `POST /complete` với code `ERR-VAL-XI-06-10` khi count(ĐBC where state != DA_TONG_HOP) > 0. Edge case: CT không có ĐBC nào (count=0) → BE vẫn 409 message "0/0 đợt BC chưa DA_TONG_HOP" (count contradictory). Pre-condition không document trong SRS.

**Cần BA quyết:**
- (a) CT TW không có ĐBC (vd CT chỉ thực hiện, không cần báo cáo định kỳ) có được phép HOAN_THANH không?
- (b) Logic "ALL ĐBC = DA_TONG_HOP" hiện BE đang enforce — có đúng business sense không?
- (c) Spec line 903 (cột Điều kiện = `-`) cần update để document rõ pre-condition.

**Spec ref:** `srs-fr-15-ct-htpldn.md line 903` + `srs-v3.5.md §3.4.3.10` · **Bug:** BUG-CTHTPLDN-B10-001 Major Open

---

## 🟡 ƯU TIÊN P1 — Cleanup spec / chuẩn hoá

### Đào tạo (8 items P1)

#### #6 — Reject reason field naming (xuất hiện 4 task: R7.4.B0, B7, B11, ĐKT)
- **Vấn đề:** Spec dùng `lyDoTuChoi/thoiGianTuChoi/nguoiTuChoiId`, BE lưu vào `ghiChuPheDuyet` (single field)
- **Cần BA chốt:** Có 4 field riêng (`lyDoTuChoi` + `thoiGianTuChoi` + `nguoiTuChoiId` + `ngayTuChoi`) hay tái sử dụng `ghiChuPheDuyet`?
- **Pattern:** Apply nhất quán cho cả CT HTPLDN (#16 dưới)

#### #7 — Reject KQ field naming (R7.4.B11 KH duyệt KQ)
- **Vấn đề:** BE GET không trả `lyDoTuChoiKQ / nguoiTuChoiKQId / ngayTuChoiKQ` (lý do từ chối KQ học tập)
- **Cần BA chốt:** FR-III-21 yêu cầu lưu fields riêng cho reject KQ, hay tái sử dụng `ghiChuPheDuyet` chung với reject KH?

#### #8 — Error code drift `ERR-CTDT-04` vs `ERR-STATE-III-01-01`
- **Vấn đề:** Test plan DT-029 ghi `ERR-CTDT-04`, BE thực tế trả `ERR-STATE-III-01-01`
- **Cần BA chốt:** Update spec hoặc dev rename code cho consistent

#### #9 — NHCH state machine spec drift
- **Vấn đề:** `FR-III-09 line 783` ghi `NHAP/CONG_KHAI/AN` (3 state) nhưng `Entity §3.4.3.21 row 9` + BE impl = `KICH_HOAT/VO_HIEU_HOA` (2 state) — line 783 typo copy-paste từ SM-BIEUMAU
- **Cần BA chốt:** Sync FR-III-09 line 783 với Entity §3.4.3.21 (source-of-truth là Entity)

#### #10 — HV ↔ TAI_KHOAN link `taiKhoanId` [REOPEN R12.4 2026-05-12 — withdrawal R12 SAI]
- **Vấn đề:** HV entity thiếu field `tai_khoan_id` link TAI_KHOAN — BE GET không trả, schema migration chưa add.
- **Cross-check 5 SRS sources (R12.4):** **4/5 confirm `tai_khoan_id` REQUIRED**:
  - `input/srs-update-2026-5-5/srs-v3.5.md §3.4.3.53` line 3349-3368 — entity HOC_VIEN có 11 fields, field 11 = `tai_khoan_id` (identifier, nullable, FK → TAI_KHOAN)
  - `input/srs-update-2026-5-5/srs-v3.5.md:2623` (master entity matrix row 10) — "có `tai_khoan_id` link TK nếu có"
  - `input/srs-update-2026-5-5/_DELTA-MAP-FR03.md:42` — "1:1 với TAI_KHOAN qua `tai_khoan_id`"
  - `input/srs-update-2026-5-5/_DELTA-MAP-FR03.md:73` — "khi seed học viên, tạo TK đồng thời"
  - **Outlier 1/5:** `input/srs-update-2026-5-5/srs-fr-03-dao-tao.md:1711` (description ngắn, lower authority) ghi "Thay đổi 12 OUT" → mâu thuẫn nội tại với `§3.4.3.53` cùng file
- **Cần BA chốt:** Spec authority — master entity spec `srs-v3.5.md §3.4.3.53` (definitive 11-field schema) thắng module file description `srs-fr-03:1711` (legacy "4 trường") không? Nếu master thắng → BE add `tai_khoan_id` nullable FK. Nếu module description thắng → cập nhật `§3.4.3.53` + DELTA-MAP để xoá field 11 + dòng matrix 2623.
- **Bug:** BUG-DT-052-HV-TAIKHOAN-01 RE-OPEN (Minor)

#### #11 — HV master entry-point
- **Vấn đề:** FR-III-04 UC23 quy định "DN/NHT đăng ký qua chuyên trang". Hiện BE expose `POST /hoc-viens` với guard 403 cho CB NV — endpoint này dành cho ai?
- **Cần BA chốt:** HV master tạo qua FR-III-04 chuyên trang là duy nhất, hay admin-only POST cho seed/backup cũng được expose?

#### #12 — Khóa học hình thức "Kết hợp"
- **Vấn đề:** R7.3.15 seed Khóa học fixture có hình thức "Kết hợp" (online+offline) → BE từ chối, chỉ accept "Trực tuyến/Trực tiếp"
- **Cần BA chốt:** Mở rộng enum thêm `KET_HOP` không?

#### #13 — Khóa học sĩ số min validation
- **Vấn đề:** "Sĩ số tối đa" + "Số buổi học" default value=0 nhưng KHÔNG required (UI không enforce). Spec ghi min=1
- **Cần BA chốt:** Có enforce required + min=1 không?

#### #14 — Modal "Công khai khóa học" thiếu 5 CPF fields
- **Vấn đề:** Spec BR-PUBLIC-01 yêu cầu modal nhập `moTaCongKhai` (max 5000 chars) + `fileDinhKemCongKhai` (PDF/DOC/DOCX/XLS/XLSX, max 20MB). UI hiện chỉ confirm Y/N
- **Cần BA chốt:** Giữ spec 5 CPF (FE bổ sung form) hay drop xuống simple confirm?

#### #15 — Lịch học BR-LH-CONFLICT-01 spec line số
- **Vấn đề:** R7.4.B12 R10 BE đã add validation conflict thời gian (commit `af8276fd`), nhưng spec không explicit line số cho BR-LH-CONFLICT-01
- **Cần BA chốt:** Bổ sung BR-LH-CONFLICT-01 vào FR-III-22 hoặc SRS chương Lịch học

#### #16 — Cổng PLQG mTLS contract cho đào tạo
- **Vấn đề:** Pattern inbound chuẩn hoá đã có cho `hoi-daps/inbound`, `tu-van-chuyen-saus/inbound`, `ho-so-pl-dns/inbound` (3 entity) — thiếu cho `dang-ky-dao-taos/inbound` + `hoc-viens/inbound`
- **Cần BA chốt:** Spec bỏ sót hay intentional (DN/NHT chỉ đăng ký qua CMS internal, không qua Cổng PLQG)?
- **Bug:** BUG-DT-CT-INBOUND-01 Major Open

---

### CT HTPLDN (4 items P1)

#### #17 — TW CT transition DA_DUYET_KQ → DA_TONG_HOP
- **Vấn đề:** Spec line 875 ghi `DA_GUI_TW → DA_TONG_HOP | cb_nv_tw_01 | [Tổng hợp]`. Nhưng CT cấp TW không qua DA_GUI_TW. R4 BE đã thêm sub-resource `/{id}/tong-hop` cho TW direct path nhưng spec chưa update.
- **Cần BA chốt:** Đối với TW CT, auto-skip DA_GUI_TW có đúng spec không? Update SRS line 874-875

#### #18 — Field naming reject Đợt BC (`lyDo` vs `lyDoTuChoi` vs `ghiChuPheDuyet`)
- **Vấn đề:** API contract reject DOT BC dùng input field `lyDo`. BE error message text "Ly do tu choi". DB column `ghiChuPheDuyet`. → 3 tên khác nhau cho cùng 1 concept
- **Cần BA chốt:** Standardize tên field. Recommend `lyDoTuChoi` (consistency FR-XI-04 CT cha)

#### #19 — BE accept `soLieuTongHop:{fields:{}}` rỗng cho `/start` Đợt BC
- **Vấn đề:** Theo UC169 "Lập BC theo mẫu 21a: nhập số liệu các cột chỉ tiêu" — minimum 1 cột chỉ tiêu cần có. BE hiện chấp nhận rỗng
- **Cần BA chốt:** BR-XI-06-02 validate `soLieuTongHop.fields` không rỗng — bổ sung guard hay không?

#### #20 — Response `POST /tong-hop` design (R4 OBS-F)
- **Vấn đề:** Response chỉ expose `dotBaoCaoId` singular (single ID), nên trả array vì có thể gộp nhiều DOT
- **Cần BA chốt:** Update API response design (low priority — chỉ design clean)

---

### Biểu mẫu (1 item P1)

#### #21 — NHT permission scope cho BIEU_MAU
- **Vấn đề:** [permission-matrix.md line 534](../../../permission-matrix.md) ghi NHT BIEU_MAU = `R` (no asterisk, implication "read-all cross-unit"). Impl thực tế NHT scope = own-unit (chỉ thấy TM cùng đơn vị)
- **Cần BA chốt:** 
  - (a) Intent = own-unit → update matrix với asterisk `R*`
  - (b) Intent = read-all → dev fix BE cho NHT thấy cross-unit
- **R7.7.10 + R7.7.10b + R8 lần 10 đều log lại** — observation persistent qua 3 round, chưa resolve

---

### QTHT (8 items P1)

#### #22 — FR-VIII-22 message "hiệu lực 24 giờ" vs "vĩnh viễn" (BUG-FR22-001b)
- **Vấn đề:** UI hiện "Link kích hoạt có hiệu lực 24 giờ". SRS line 1280 ghi "vĩnh viễn nếu là kích hoạt lần đầu"
- **Cần BA chốt:** Token hiệu lực bao lâu? 24 giờ hay vĩnh viễn?
- **Status:** Open chờ BA chốt spec

#### #23 — FR-VIII-15 §Inputs row 5 — Form `mat_khau` field
- **Vấn đề:** SRS spec form Add TK có field `mat_khau`. Logic chốt 2026-05-07: hệ thống tự sinh MK tạm + gửi email + user đổi MK lần đầu (qua FR-VIII-26) → field không cần nhập
- **Cần BA chốt:** Remove field `mat_khau` khỏi SRS FR-VIII-15 §Inputs row 5 (cleanup doc)

#### #24 — LOAI_DOANH_NGHIEP spec contradiction FR-10 vs FR-VIII-07
- **Vấn đề:** SRS gộp 2 concept vào cùng DM `LOAI_DOANH_NGHIEP`:
  - Quy mô (NĐ 39/2018): DN_SIEU_NHO/NHO/VUA
  - Loại hình pháp lý (Luật DN 2020): TNHH/CP/DNTN/HKD
  - 2 concept độc lập, mâu thuẫn FR-VIII-07 line 393, 399
- **Cần BA chốt:** Tách thành 2 DM riêng (`QUY_MO_DN` + `LOAI_HINH_PHAP_LY_DN`) hay giữ gộp?
- **Spec ref:** Bug-report-seed-r7-1-2-loai-dn.md

#### #25 — R7.8.4 Profile đổi MK — "ký tự đặc biệt" required?
- **Vấn đề:** Spec/BE/UI conflict về việc password có required ký tự đặc biệt không
- **Cần BA chốt:** Định nghĩa chính xác rule password complexity (uppercase + lowercase + digit + special char + min length)

#### #26 — R7.8.4 "Phiên đăng nhập" tab extra
- **Vấn đề:** UI có tab "Phiên đăng nhập" trong Profile — KHÔNG có trong SRS
- **Cần BA chốt:** 
  - (a) Keep + update spec (BA bổ sung doc)
  - (b) Remove FE feature

#### #27 — VAI_TRO read permission cho non-QTHT
- **Vấn đề:** BE design granular permission (cấp `read_vai_tro` cho CB NV để chọn assign khi tạo TK). SRS Preconditions ghi "QTHT-only"
- **Cần BA chốt:** Keep BE design (defensive cần thiết) + update SRS, hay enforce strict QTHT-only?

#### #28 — Vai trò + Reset MK errCode convention
- **Vấn đề:** Code mismatch giữa spec (`ERR-VT-01`, `ERR-PWD-04/05/06`) và BE (`ERR-VAL-VIII-111-01`, etc.). Message text đúng, chỉ code khác. R8 dev đã đổi 1 số code → match. Còn lại đợi BA + dev align convention chung
- **Cần BA chốt:** Convention chuẩn cho errCode toàn hệ thống (vd: `ERR-<module>-<func>-<seq>` hay `ERR-VAL-<X>-<Y>-<Z>`)

#### #29 — TVV login MK sau form first-login-password fail 401 (R7.2.9b)
- **Vấn đề:** Login `Secret@123` sau set MK qua form fail 401 (token consumed parallel race HOẶC FE silent fail bug)
- **Cần BA quyết:** Cung cấp isolated test env hoặc dev seed pool TVV fresh để distinguish 2 nguyên nhân
- **Note:** Đây không hẳn là spec issue — gần như infrastructure decision

---

## 🟢 ƯU TIÊN P2-P3 — Theme cross-cutting

#### #30 — Vietnamese diacritics trong BE messages
- **Vấn đề:** BE messages "Ly do tu choi", "So lieu", "Khong the hoan thanh" thiếu dấu — pattern xuất hiện xuyên suốt FR-XI BE messages (CT HTPLDN). Một số đã fix R3 (B10 message R3 đã có dấu)
- **Cần BA chốt:** Standard i18n cho BE messages — đảm bảo full Vietnamese diacritics
- **Impact:** UX minor — message vẫn đọc được nhưng không chuyên nghiệp

---

## Tóm tắt — Cần BA quyết theo ưu tiên

### 🔴 P0 — Block GA (5 items)
| # | Item | Module | Bug ref |
|:-:|---|:-:|---|
| 1 | VPD bypass cho `congKhai=true` | Đào tạo | BUG-DT-CT-VPD-01 |
| 2 | Cross-tenant leak KH năm + Read scope CB PD | Đào tạo | BUG-KH-001 |
| 3 | Khóa học state machine 11-state vs ~6-state | Đào tạo | R7.4.B7 |
| 4 | ĐKT state machine 2-state vs spec workflow duyệt | Đào tạo | R7.4.B10 |
| 5 | CT B10 "0/0 đợt BC" edge case + pre-condition | CT HTPLDN | BUG-CTHTPLDN-B10-001 |

### 🟡 P1 — Cleanup chuẩn hoá (16 items)
- Đào tạo: #6-16 (8 items)
- CT HTPLDN: #17-20 (4 items)
- Biểu mẫu: #21 (1 item)
- QTHT: #22-29 (8 items)

### 🟢 P2-P3 — Theme cross-cutting
- #30 — Vietnamese diacritics consistency

---

## Reference

- [Báo cáo tổng hợp 4 module](BAO-CAO-TONG-HOP-4-MODULE-2026-05-11.md)
- [Bug report mới — Chuyên trang VPD + Inbound](../bug-reports/dao-tao/bug-report-r7-7-6-chuyen-trang-vpd-inbound.md)
- [permission-matrix.md](../../../permission-matrix.md) — line 534 NHT BIEU_MAU
- [SRS v3.5](../../../../input/srs-update-2026-5-5/srs-v3.5.md) · [SRS v3 base](../../../../input/srs-v3/)

---

*BA confirm list 4 module · 2026-05-11 19:45 · QA Automation Claude Code MCP*
