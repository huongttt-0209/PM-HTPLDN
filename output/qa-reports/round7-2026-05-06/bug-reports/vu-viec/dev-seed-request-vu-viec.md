# Dev / Seed / Infra request — Module Vụ việc (R7.7.3)

> **Mục đích:** Tổng hợp 43 TC còn lại của R7.7.3 KHÔNG chạy được hôm nay (2026-05-11), phân nhóm theo nguyên nhân để gửi dev / seed team / infra cùng action cần thiết.
>
> **Module:** Vụ việc HTPL (FR-IV / FR-V)
> **Round:** R7 — Vụ việc 72 TC v3.5 · Done 29/72 ≈ 40% · Pending 43/72 ≈ 60%
> **Tester:** QA · 2026-05-11 10:00:00 +07
> **Spec ref:** [`output/funtion/7.5-vu-viec-htpl.md`](../../../../funtion/7.5-vu-viec-htpl.md) v3.5 · [`input/srs-update-2026-5-5/srs-fr-iv-vu-viec.md`](../../../../../input/srs-update-2026-5-5/srs-fr-iv-vu-viec.md)
> **Functional report:** [`functional-test-report-r7-7-3-vu-viec.md`](../../functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md)
> **Bug-report ref:** [`bug-report-r7-7-3-functional-vu-viec.md`](bug-report-r7-7-3-functional-vu-viec.md)

---

## Tổng hợp 43 TC pending — chia 4 nhóm

| Nhóm | TC count | Owner | Trạng thái |
|:-:|:-:|---|---|
| **A — Chờ dev fix bug** | 8 | Dev BE | Có bug log NOTIF-01 + LICHSU-01 Open |
| **B — Chờ infra setup env** | 16 | Infra / Dev BE | VNeID T2 sandbox + DN T2 verified account |
| **C — Chờ seed data backdated** | 3 | QA seed / DBA | Pool VV deadline backdated 11/16/21 ngày |
| **D — Chờ BA confirm spec** | 2 | BA | C5-4 + C6-4 mechanism mismatch |
| **E — Out of scope round (defer)** | 14 | — | Test sau khi A/B/C/D xong |

---

## Nhóm A — Chờ dev fix bug (8 TC)

### A.1 — BUG-VV-FN-NOTIF-01 (Critical · Open) — UC62 trigger mail DN

**SRS ref:** `srs-fr-05-vu-viec.md §UC62 Outputs` · `BR-NOTIF-VV-TIEPNHAN`

**Yêu cầu dev:**
- Backend trigger event `MAIL_DN` cho mỗi state transition của VU_VIEC, target = DN.email.
- States cần trigger: `DA_TIEP_NHAN`, `DA_PHAN_CONG`, `YEU_CAU_BO_SUNG`, `TU_CHOI`, `DA_DUYET`, `CONG_KHAI`, `MO_LAI`, `HOAN_THANH`, `DA_DANH_GIA` (xem UC62 §Outputs cho subject/body từng case).
- Hiện tại: chỉ TVV/NHT nhận mail (UC61 phân công); DN 0 mail trong 177 mail MailHog suốt 19 VV pool.

**TC unblock khi fix:**

| TC ID | Mục tiêu | Verify command |
|---|---|---|
| **VV-031** | UC62 — Mail DN sau DA_TIEP_NHAN | Tạo VV mới → curl `:8025/api/v2/messages?query=<DN.email>` → expect ≥1 mail |
| **C2-1** | Mail DN sau DA_PHAN_CONG (advance state) | Walk DA_TIEP_NHAN → DA_PHAN_CONG → MailHog check DN |
| **C2-2** | Mail DN sau YEU_CAU_BO_SUNG | Walk Kiểm tra với verdict YCBS → MailHog DN |
| **C2-3** | Mail DN sau TU_CHOI | Walk Kiểm tra với verdict Từ chối → MailHog DN |
| **C2-4** | Mail DN sau DA_DUYET / HOAN_THANH | Walk full lifecycle → MailHog DN cho mỗi state |
| **C2-5** | Mail DN sau CONG_KHAI | Toggle CONG_KHAI → MailHog DN |

→ 6 TC unblock.

---

### A.2 — BUG-VV-FN-LICHSU-01 (Major · Open) — 8 enum còn thiếu

**SRS ref:** `LICH_SU_VU_VIEC` entity với 18 hành động ENUM · `BR-AUDIT-VV-01`

**Yêu cầu dev:**
- BE ghi đủ 18 enum vào `lich_su_vu_viec.loai_hanh_dong` khi state transition tương ứng.
- Hiện tại đã có 10/18 enum: `TAO_VV, CREATE` (legacy), `KIEM_TRA, PHAN_CONG, XAC_NHAN_PHAN_CONG, TRINH_PD, PHE_DUYET, HOAN_THANH, CONG_KHAI, HUY_CONG_KHAI, MO_LAI`.
- **Còn thiếu 8 enum:**
  1. `TIEP_NHAN` — VV chuyển từ `MOI_TAO` → `DA_TIEP_NHAN` (hiện tại merge vào `TAO_VV/CREATE`).
  2. `PHAN_CONG_CA_NHAN` — Phân công CG/TVV cá nhân (hiện tại generic `PHAN_CONG`).
  3. `PHAN_CONG_TO_CHUC` — Phân công TCTV (hiện tại generic `PHAN_CONG`).
  4. `CAP_NHAT_KQ` — CB_NV/TVV nhập kết quả xử lý (hiện tại không ghi entry).
  5. `DANH_GIA` — POST `/danh-gia` chấm điểm UC67 (R14 verified 0 entry mới sau POST 201).
  6. `YEU_CAU_BO_SUNG` — Verdict YCBS (hiện tại ghi qua `KIEM_TRA` enum).
  7. `TU_CHOI` — Verdict TU_CHOI khi kiểm tra (hiện tại ghi qua `KIEM_TRA` enum).
  8. `TU_CHOI_DUYET` — CB_PD reject không đồng ý phê duyệt.

**Khuyến nghị enum naming convention:** thống nhất uppercase snake-case (`TAO_VV/KIEM_TRA/...`) cho TẤT CẢ 18 entries. Hiện UI mix Vietnamese display ("Tạo mới", "Kiểm tra", "Phân công", "Phê duyệt") + uppercase ("XAC_NHAN_PHAN_CONG", "TRINH_PD") — cần consistency.

**TC unblock khi fix:**

| TC ID | Mục tiêu | Verify command |
|---|---|---|
| **C8-3 (deep)** | Verify đủ 18/18 enum xuất hiện sau full lifecycle | Walk VV mới qua mọi transition + GET `/lich-su` count distinct enum |
| **C7-3** | Filter LICH_SU theo loaiHanhDong enum cụ thể | GET `/lich-su?loaiHanhDong=DANH_GIA` → expect ≥1 record sau chấm điểm |

→ 2 TC unblock (plus regression của các TC khác đã PASS nay cần re-verify enum coverage).

---

## Nhóm B — Chờ infra setup env (16 TC)

### B.1 — VNeID Tier 2 sandbox

**Spec ref:** `srs-fr-05-vu-viec.md §BR-AUTH-01` (Tier 2 SSO VNeID cho DN/TVV/CG/NHT — bỏ VNPT eKYC từ update 2026-05-06)

**Yêu cầu infra / dev:**
1. **VNeID Tier 2 sandbox URL + API token** — đặt biến môi trường `VNEID_SANDBOX_URL` + `VNEID_SANDBOX_TOKEN` trên BE.
2. **≥1 DN test account verified Tier 2** — tạo DN với:
   - `maSoThue` hợp lệ (10 chữ số) đã `vneid_verified=true` ở sandbox.
   - `email` hoạt động (gửi mail thật được).
   - `nguoiDaiDien` có VNeID profile T2.
3. **DN-portal endpoint chuyên trang** — endpoint `/cong-dan-doanh-nghiep/vu-viecs/*` cho DN tự gửi YC + bổ sung HS qua chuyên trang. Hiện tại 14 endpoint probe (R7.4.A3-DN-BS) toàn 403/404.
4. **Optional:** Mock VNeID service nếu sandbox down (verify DN session cookie sau OAuth callback).

**TC unblock khi setup:**

| TC ID | Mục tiêu | Account cần |
|---|---|---|
| **C1-1** | DN gửi YC qua chuyên trang VNeID T2 | DN T2 verified |
| **C1-2** | DN bổ sung HS sau YEU_CAU_BO_SUNG | DN T2 verified |
| **C1-3** | DN view chi tiết VV của mình | DN T2 verified |
| **C1-4** | DN nhận thông báo trạng thái VV (cross UC62) | DN T2 verified + NOTIF-01 fix |
| **C1-5** | DN từ chối bổ sung → VV `BO_SUNG_THIEU` | DN T2 verified |
| **C1-6** | DN export chi tiết VV PDF | DN T2 verified |
| **C4-1** | NHT phân công CG cross-donVi qua DN portal | DN T2 + NHT pool ≥3 |
| **C4-2** | TVV nhận VV qua mobile app (VNeID T2) | TVV T2 verified |
| **C4-3** | CG đồng ý/từ chối nhận VV | CG T2 verified |
| **C4-4** | TCTV accept VV organization-mode | TCTV T2 verified |
| **C4-5** | NHT reassign khi TVV/CG decline | DN T2 + NHT pool |
| **C4-6** | Workflow chuyển CG sang CG khác giữa chừng | CG T2 ≥2 |
| **C5-2** | DN auth T2 chấm điểm UC67 | DN T2 verified |
| **C6-2** | DN auth T2 gửi YC (negative: chưa VNeID → ERR-VN-02) | DN T2 + DN không-T2 |
| **C6-3** | Lookup DN từ session/MST (7 fields refactor) | DN T2 verified |
| **R7.7.3-PRIVACY-1** | NĐ 13/2023 — DN chỉ thấy VV của mình, không thấy DN khác | DN T2 ≥2 |

→ 16 TC unblock.

---

## Nhóm C — Chờ seed data backdated SLA (3 TC)

### C.1 — Pool VV với deadline backdated

**Spec ref:** `srs-fr-05-vu-viec.md §BR-SLA-02` — 4 mức cảnh báo: `BINH_THUONG / SAP_HET (≤3 ngày) / QUA_HAN (overdue) / QUA_HAN_NGHIEM_TRONG (overdue >7 ngày)`

**Yêu cầu QA seed / DBA:**
- Seed ≥1 VV cho mỗi mức cảnh báo:
  - **Mức `SAP_HET`:** VV với `ngayTiepNhan` backdate sao cho `deadline = today + 1-3 ngày`.
  - **Mức `QUA_HAN`:** VV với `deadline < today` (overdue 1-7 ngày).
  - **Mức `QUA_HAN_NGHIEM_TRONG`:** VV với `deadline < today - 7 ngày` (overdue >7 ngày).
- Cách seed (preferred): **time-travel API** hoặc **DBA backdated INSERT** với `ngay_tiep_nhan` set trong quá khứ.
- Lý do không seed qua UI: form `Ngày tiếp nhận` field disabled (auto-set `now()`) — không thể tự tạo backdated qua UI.

**TC unblock khi seed:**

| TC ID | Mục tiêu | Verify |
|---|---|---|
| **VV-022 (mức 2)** | SLA `SAP_HET` hiển thị banner vàng | List VV → cột "Cảnh báo thời hạn" = "Sắp hết hạn" |
| **VV-022 (mức 3)** | SLA `QUA_HAN` hiển thị banner đỏ | Cột "Cảnh báo" = "Quá hạn" |
| **VV-022 (mức 4)** | SLA `QUA_HAN_NGHIEM_TRONG` escalate | Cột "Cảnh báo" = "Quá hạn nghiêm trọng" + có notification escalate |

→ 3 TC unblock.

---

## Nhóm D — Chờ BA confirm spec (2 TC mechanism mismatch)

### D.1 — C5-4 Duplicate UNIQUE per loại — mechanism mismatch

**Spec C5-4:** "ERR-DG-VV-04 duplicate per loại — CB_NV chấm cùng VV lần 2 → UNIQUE(`vu_viec_id`, `loai_nguoi_danh_gia`) chặn → 'Bạn đã đánh giá vụ việc này rồi'"

**Reality (R15 verified):** Sau POST `/danh-gia` lần 1 → VV auto flip `HOAN_THANH → DA_DANH_GIA`. POST lần 2 → BE trả 409 `ERR-STATE-VI-16-01` "Vụ việc không ở trạng thái HOAN_THANH" (state guard) thay vì UNIQUE constraint.

**Câu hỏi cho BA:**
1. Mechanism state guard (current) có acceptable không, hay BẮT BUỘC UNIQUE constraint với error code `ERR-DG-VV-04`?
2. Nếu BA giữ UNIQUE: dev cần thêm logic check UNIQUE TRƯỚC state guard (currently state guard ưu tiên).
3. Nếu BA chấp nhận state guard: cần cập nhật spec C5-4 wording.

---

### D.2 — C6-4 BR-CALC-04 lookup pre-check — silent fallback

**Spec C6-4:** "Negative: tạo VV cho DN có hồ sơ thiếu field BR-CALC-04 (`gioi_tinh_chu_dn`, `so_lao_dong_nu`, `so_lao_dong_kt`) → ERR-NH-03 hoặc warning 'DN cần cập nhật hồ sơ trước khi tạo VV' → CB NV chuyển hướng cập nhật DN"

**Reality (R15 verified):** DN "Demo An Giang" có `gioiTinhChuDn=null + soLaoDongNu=null + soLaoDongKhuyetTat=null`. CB_NV submit form → VV-BTP-TW-20260511-002 tạo OK với priority default 3 ("Trung bình"). Form helper text hiển thị "3 — Trung bình (mặc định BR-CALC-04)" — suggest silent fallback to default là design intentional.

**Note BE schema:** field tên là `soLaoDongKhuyetTat`, KHÔNG phải `soLaoDongKt` (spec viết tắt).

**Câu hỏi cho BA:**
1. Silent fallback to priority 3 (current) có acceptable không, hay BẮT BUỘC warning/error chặn submit?
2. Nếu chặn: dev thêm validator pre-check + endpoint suggest cập nhật DN.
3. Nếu fallback: cập nhật spec C6-4 wording + bỏ ERR-NH-03 expected error.

---

## Nhóm E — Out of scope round 7 (14 TC defer)

Các TC này không phải block hard — chỉ defer sang round sau khi A/B/C/D resolved hoặc theo priority project.

| Cluster | TC count | Lý do defer |
|---|:-:|---|
| **Cluster 0** (base) | 25 TC chưa chạy | Cần ≥1 VV mỗi state lifecycle (PHAN_HOI/HOAN_THANH/DA_DUYET đã có 1 VV mỗi state, còn TU_CHOI/MO_LAI partial pool — testable nhưng low priority). |
| **Cluster 3** (SLA negative) | 3 TC | Phụ thuộc C above + counter scheduler trigger (time-driven test khó setup). |
| **Cluster 7** (cross-module) | 4 TC | DN/HoiDap/HopDong tab cross-link — partial test possible nhưng chờ HopDong module ready. |

**Tổng E:** Khoảng 14 TC core có thể defer / test sau khi unblock A+B+C.

---

## Action plan để hoàn tất 72/72 TC

| Step | Owner | Trigger | Output |
|---|---|---|---|
| 1 | Dev BE | Fix BUG-VV-FN-NOTIF-01 + LICHSU-01 | A nhóm unblock 8 TC |
| 2 | Infra | Setup VNeID T2 sandbox + DN T2 verified | B nhóm unblock 16 TC |
| 3 | QA seed / DBA | Seed 3 VV deadline backdated | C nhóm unblock 3 TC |
| 4 | BA | Confirm C5-4 + C6-4 design | D nhóm xác định bug-or-not |
| 5 | QA | Run remaining 14 TC E sau khi 1-4 done | Coverage 72/72 |

---

## Phụ lục — Observation Minor (không block, không bug)

1. **Field naming inconsistency POST `/danh-gia`:** Request body field `diemTienDo` ≠ Response body field `diemThoiGian`. Tester phải dùng `diemTienDo` cho POST nhưng GET/list trả `diemThoiGian`. → Khuyến nghị: BE rename alias để unified naming (cả 2 hướng dùng cùng tên).
2. **`diemTong` display format:** R15 C5-1 POST `{8, 9, 10}` → `diemTong: 9` (integer). Spec example C5-5 nói "vd: 8+9+10 → 9.0, không phải 9". Nếu spec strict format `X.Y` → BE cần format response `diemTong: 9.0` (1 decimal).
3. **`Đánh giá` accordion UI:** VV-002 HOAN_THANH detail page có accordion "Đánh giá" expanded nhưng hiển thị "image Trống + Chưa có thông tin" — KHÔNG có button [Chấm điểm]/[Đánh giá] visible. CB_NV phải gọi API trực tiếp để chấm. FE cần thêm CTA button trong accordion này khi state = `HOAN_THANH` AND role ∈ {CB_NV, DN}.
4. **Field tên BE schema:** `soLaoDongKhuyetTat` (đầy đủ), không phải `soLaoDongKt` như spec viết tắt. Cần align spec wording với BE schema.

---

> **Liên hệ:** QA Team · gửi đính kèm bug-report files trong cùng folder `bug-reports/vu-viec/` để dev cross-reference.
