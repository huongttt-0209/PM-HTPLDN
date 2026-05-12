# Bug Report — Chi trả chi phí (FR-V.II / FR-06)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation via Claude Code |
| **Ngày** | 2026-05-09 18:05:00 - 18:18:00 |
| **Loại test** | Workflow + Functional |
| **Round** | R7 — R1 task R7.6.1 |
| **Tài liệu tham chiếu** | [srs-fr-06-chi-tra.md](../../../../input/srs-update-2026-5-5/srs-fr-06-chi-tra.md) · [02-thu-tu-module.md §10 SM-CHI-TRA](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) · [workflow-test-report-r7-6-1-chi-tra-v3-5.md](../../workflow/chi-tra/workflow-test-report-r7-6-1-chi-tra-v3-5.md) |

---

## Tổng hợp

Phát hiện **7** lỗi có SRS reference cụ thể. **R3 2026-05-10 21:00:00 verify dev fix: 7/7 đóng (1 false-positive, 6 thực sự fix).**

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 7    | 1        | 1     | 2      | 3     | 0       | 7      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-CHITRA-001~~ | Critical | P1 | Data | R7.6.1-B9 + R7.E3-R3 | `BR-CALC-01` (FR-V.II §Business Rules + 02-thu-tu-module.md §10) | ~~Seed data **0/12 CHO_PHE_DUYET BR-OK** + **97/108 (89.8%) sai BR đầy đủ**~~ | Closed |
| ~~BUG-CHITRA-002~~ | Medium | P2 | UI/UX | R7.6.1-B3 | `FR-V.II-03 §Inputs row 5` | ~~Form kiểm tra hiển thị 4 checklist mục thay vì checklist 18 trường theo spec~~ | Closed |
| ~~BUG-CHITRA-003~~ | Medium | P2 | Workflow | R7.6.1-B7 | `FR-V.II-09 §Inputs` | ~~Form thẩm định có 3 outcome (Đạt / Không đạt / Cần bổ sung) thay vì 2 outcome~~ | Closed |
| ~~BUG-CHITRA-004~~ | Minor | P3 | UI/UX | R7.6.1-B7, B11 | `SCR-V.II-02 §Lịch sử xử lý` | ~~Lịch sử xử lý ghi enum code (`CAP_NHAT_THANH_TOAN`, `TRINH_PHE_DUYET`) thay vì tiếng Việt~~ | Closed |
| ~~BUG-CHITRA-005~~ | Minor | P3 | UI/UX | R7.6.1-B11 | `FR-V.II-13 §Inputs row "Số tiền thực trả"` | ~~Spinbutton "Số tiền thực trả" có `valuemin=1` + initial `value=0` — bound mâu thuẫn~~ | Closed |
| ~~BUG-CHITRA-006~~ | Minor | P3 | UI/UX | R7.7.12.3-B8 | `02-thu-tu-module.md §10 SM-CHI-TRA line 738` (B8 = trả về thẩm định) | ~~Endpoint `/tu-choi` + UI button "Từ chối — trả về thẩm định" + modal heading "Từ chối hồ sơ" mâu thuẫn spec B8~~ | Closed |
| ~~BUG-CHITRA-007~~ | **Major** | P1 | UI/UX | R7.6.1-R3 B10/B12 | `FR-V.II-13 §Inputs` + `02-thu-tu-module.md §10 SM-CHI-TRA line 740-741` (B10 + B12) | ~~Form "Cập nhật thanh toán" KHÔNG render với cb_pd_dp_01~~ — false positive R2 (sai role, B10/B12 actor là CB NV DP per spec) | Closed |

---

## ~~BUG-CHITRA-001~~ [CLOSED] — Seed data 97/108 record sai BR-CALC-01 đầy đủ (% + trần) — 0/12 CHO_PHE_DUYET BR-OK

> **Re-test:** 2026-05-10 21:00:00 R3 — ✅ PASS (Closed-verified). Dev re-seeded pool 108 → 40 record. API verify: **40/40 record đúng % + trần** (SIEU_NHO 100%/3M, NHO 30%/5M, VUA 10%/10M). State distribution: DTD 12, DA_DUYET 7, YCBS 5, DTT 4, HUY 3, TU_CHOI 3, DDG 3, CTN 2, CPD 1. Walk B9 unblock được. CMD verify: `GET /api/v1/ho-so-chi-tras?page=1&pageSize=100` + sample 8 detail OK.
>

### Mô tả

Khi CB Phê duyệt TW thực hiện B9 (CHO_PHE_DUYET → DA_DUYET) trên HSCT000068, BE từ chối với HTTP 422 `ERR-CT-PD-06`: hồ sơ vi phạm BR-CALC-01 (DN quy mô Nhỏ chỉ được mức HT 30% / 5.000.000 VND/năm, hồ sơ đang lưu 50% / 50.000.000 VND/năm). **R7.E3-R2 (2026-05-09 23:17) verify toàn pool 108 record qua API: 74/108 (68.5%) sai BR-CALC-01.** Phân bố sai theo 4 cluster:
- Cluster 1 — `HSCT000001..050` series: Nhỏ lưu 50% (cần 30%) + Vừa lưu 30% (cần 10%).
- Cluster 2 — `HSCT200001..030` series: Nhỏ lưu 60% + Vừa lưu 40% + Siêu nhỏ lưu 80% (toàn bộ sai khác value).
- Cluster 3 — `HSCT000066..070` (R6 walk): 4/5 lưu 50% Nhỏ (đã log R1).
- Cluster 4 — `HSCT000071..078` (R7 re-seed, 2026-05-09): đa số ĐÚNG BR ✅.

Logic transition đúng spec (BE chặn hợp lệ ở B9 ERR-CT-PD-06); lỗi nằm ở seed data lan rộng. Tác động lớn: KPI báo cáo + tổng tiền đã chi trong năm sai (nếu data đã DA_THANH_TOAN với mức sai BR), không chỉ block B9.

### Các bước tái hiện

1. Đăng nhập `cb_pd_tw_07` (CB Phê duyệt TW).
2. Vào Quản lý chi trả chi phí → danh sách HSCT.
3. Click "Phê duyệt" trên HSCT000068 (Chờ phê duyệt, Nhỏ, mức HT 50%).
4. Form Phê duyệt mở — số tiền duyệt = 5.975.278.
5. Click "Phê duyệt" submit.
6. Quan sát: BE trả 422, toast "Hồ sơ vi phạm BR-CALC-01: quyMoDn=NHO yêu cầu 30% / 5000000 VND/năm, hồ sơ đang lưu 50% / 50000000 VND/năm".

### Kết quả mong đợi

- Theo BR-CALC-01: DN Nhỏ → mức HT tối đa 30% phí tư vấn, trần 5.000.000 VND/năm. Seed data BẮT BUỘC tuân thủ BR ngay khi tạo HSCT.
- HSCT000068 ở trạng thái CHO_PHE_DUYET phải có mức HT 30% và số tiền đề nghị ≤ 5.000.000 → CB PD phê duyệt được.

### Kết quả thực tế

**R1 (2026-05-09 18:18 — pool 78):**
- Bảng danh sách 4/5 HSCT (000066, 000068, 000069, 000070) hiển thị cột "Mức HT %" = 50% cho DN Nhỏ. Chỉ HSCT000067 = 30% (đúng).
- HSCT000068 số tiền đề nghị 5.975.278 + mức 50% → vi phạm cả 2 chiều của BR-CALC-01 (% và trần năm).
- HSCT000070 đã DA_THANH_TOAN với 7.209.845 VND mức 50% → sai BR đã lọt qua nghiệp vụ trước khi seed.
- BE response B9: `{"success":false,"error":{"code":"ERR-CT-PD-06","message":"Hồ sơ vi phạm BR-CALC-01..."}}`

**R2 (2026-05-09 23:17 — pool 108, mở rộng scope qua API):**
- API `GET /api/v1/ho-so-chi-tras` (page 1+2, pageSize=100) trả 108 record. Filter `mucHoTroPhanTram !== expected[quyMoDn]`:
  - **74/108 record vi phạm** (68.5%) — Nhỏ lưu 50%/60% (spec 30%), Vừa lưu 30%/40% (spec 10%), Siêu nhỏ lưu 80% (spec 100%).
  - **34/108 record đúng %** — đa số là HSCT000071..078 (R7 re-seed) + một số rải rác HSCT000004/007/010/011/014/020/027/030/031/034/061-064 (BR-OK list cho test).
- 18 record DA_THANH_TOAN trong pool có ~12 sai BR → tổng tiền đã chi trong năm sai → KPI báo cáo FR-11 đếm sai theo `BR-CALC-02` (`tran_ho_tro_nam − da_chi_trong_nam`).
- Pool CHO_PHE_DUYET 12 record: 9 vi phạm BR % → khi CB PD bấm Phê duyệt sẽ liên tục bị BE chặn ERR-CT-PD-06 → bottleneck workflow.

**R3 (2026-05-09 23:40 — deep BR check % + trần qua API detail):**
- B9 retry HSCT000027 (R2 đánh BR-OK theo %, SIEU_NHO/100%) FAIL 422: `"yêu cầu 100% / 3000000 VND/năm, hồ sơ đang lưu 100% / 100000000 VND/năm"`. → BR-CALC-01 có **2 chiều**: % và `tranHoTroNam` (R2 chỉ check chiều %).
- Fetch detail `/api/v1/ho-so-chi-tras/{id}` cho 34 record OK-%: **23/34 SAI trần** (lưu `tranHoTroNam=100,000,000` thay vì `3,000,000` cho SIEU_NHO — sai 33×). Cluster lan AG/BG/BN/BCT.
- **Toàn pool BR đầy đủ OK = 11/108 (10.2%)**:
  - DANG_THAM_DINH (8): HSCT000001/017/072/073/074/075/076/077
  - DA_DUYET (1): HSCT000071 (AG)
  - DA_THANH_TOAN (1): HSCT000078 (AG)
  - TU_CHOI (1): HSCT000067 (Cục BTTP)
- **Critical: 0/12 CHO_PHE_DUYET BR-OK** → B9 phê duyệt **BLOCKED toàn pool**, không có record nào CB PD bấm phê duyệt được. HSCT000027/030/063 (R2 nghĩ BR-OK) → đều sai trần.
- B-step gate BR: chỉ B9 (CPD→DA_DUYET) gate cứng. B5/B7/B8/B12 là state transition + reason → chạy được trên record sai BR. Đã PASS HSCT000007 R2 (B5 DKT→TU_CHOI), HSCT000031 (B12 DA_DUYET→TU_CHOI_TT) khả thi vì rejection.

### Bằng chứng

![BUG-CHITRA-001 — Pool 5 HSCT cột Mức HT %, 4/5 sai 50% cho DN Nhỏ](image/bug-chitra-001-pool-50pct-violation.png)

```text
HTTP 422 từ POST /api/v1/chi-tra/{id}/phe-duyet (HSCT000068, R1 chiều %)
{
  "success": false,
  "error": {
    "code": "ERR-CT-PD-06",
    "message": "Hồ sơ vi phạm BR-CALC-01: quyMoDn=NHO yêu cầu 30% / 5000000 VND/năm, hồ sơ đang lưu 50% / 50000000 VND/năm"
  }
}

HTTP 422 từ POST /api/v1/chi-tra/{id}/phe-duyet (HSCT000027, R3 chiều trần)
{
  "success": false,
  "error": {
    "code": "ERR-CT-PD-06",
    "message": "Hồ sơ vi phạm BR-CALC-01: quyMoDn=SIEU_NHO yêu cầu 100% / 3000000 VND/năm, hồ sơ đang lưu 100% / 100000000 VND/năm",
    "timestamp": "2026-05-09T16:30:51.408Z",
    "requestId": "3c4313ec-b739-4cd8-96b4-3b1cb79dac80"
  }
}

API detail HSCT000027 (cb_pd_dp_02 token, GET /api/v1/ho-so-chi-tras/<id>):
{
  "phiTuVan": 38333309, "soTienDeNghi": 38333309,
  "quyMoDn": "SIEU_NHO", "mucHoTroPhanTram": 100,
  "tranHoTroNam": 100000000,    // BR-CALC-01 yêu cầu 3000000
  "soTienDuocDuyet": null, "trangThai": "CHO_PHE_DUYET",
  "donVi": { "ten": "Sở Tư pháp Bắc Giang", "cap": "DP" }
}
```

---

## ~~BUG-CHITRA-002~~ [CLOSED] — Form kiểm tra hiển thị 4 mục checklist thay vì checklist 18 trường

> **Re-test:** 2026-05-10 20:32:00 R3 — ✅ PASS (Closed-verified). Walk HSCT200001 B3 (Bình Minh AG SN1, cb_nv_dp_01). Form kiểm tra render đúng 18 trường: Tên DN, Mã số DN, Địa chỉ DN, SĐT/Fax/Email, Giấy CNĐKKD, Ngành nghề, Người đại diện, Loại hình DN, Quy mô DN, Vụ việc vướng mắc, Thời điểm phát sinh, Tên TVV, Tổ chức hành nghề, Địa chỉ TVV, SĐT TVV, Số ngày hợp đồng TVPL, Phí tư vấn, Số tiền đề nghị + 3 radio outcome (Đạt/Yêu cầu bổ sung/Không đạt). Submit Đạt → state CTN→DDG OK.


### Mô tả

Tại B3 (DKT → DDG, kiểm tra hồ sơ Đạt), form kiểm tra hồ sơ chỉ hiển thị 4 mục checklist tham khảo (Mã số thuế hợp lệ, Hồ sơ đầy đủ chữ ký, Mẫu 01 đính kèm, Hợp đồng tư vấn đính kèm). Theo SRS FR-V.II-03 §Inputs row 5, form phải có "checklist 18 trường" tương ứng với 18 trường dữ liệu cần kiểm tra của Mẫu 01.

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_07`.
2. Vào Quản lý chi trả chi phí.
3. Click "Kiểm tra" trên HSCT (state DKT, ví dụ HSCT000067 R1).
4. Quan sát section "Kiểm tra hồ sơ" trong form drawer.

### Kết quả mong đợi

- Form kiểm tra hiển thị checklist 18 trường theo SRS FR-V.II-03 §Inputs row 5 — mỗi trường 1 dòng có check "Đạt / Không đạt".

### Kết quả thực tế

- Form chỉ hiển thị 4 checkbox mức tổng quát (Số liệu khớp Mẫu 01 / Phí tư vấn hợp lý / Quy mô DN đúng / Chưa vượt trần năm). Đây là gộp khoảng cấp cao, không phải 18 trường chi tiết.

### Bằng chứng

![BUG-CHITRA-002 — Form kiểm tra chỉ 4 mục checklist](image/bug-chitra-002-form-kiemtra-checklist.png)

---

## ~~BUG-CHITRA-003~~ [CLOSED] — Form thẩm định có 3 outcome thay vì 2 theo spec

> **Re-test:** 2026-05-10 20:33:00 R3 — ✅ PASS (Closed-verified). Walk HSCT200001 B7 (cb_nv_dp_01, sau B-Đánh giá). Form thẩm định chỉ render 2 radio outcome: "Đạt" + "Không đạt" (radio "Cần bổ sung" đã loại bỏ). Submit Đạt + spinbutton số tiền đề xuất → state DTD → CPD OK qua nút Trình PD.


### Mô tả

Tại B7/B8 (form Thẩm định, DTD → CPD hoặc DTD → TU_CHOI), form hiển thị 3 radio kết quả thẩm định: "Đạt", "Không đạt", "Cần bổ sung". Theo SRS FR-V.II-09 §Inputs, form thẩm định chỉ có 2 outcome: "Đạt" → CPD và "Không đạt" → TU_CHOI. Trạng thái "Cần bổ sung" thuộc B4 (kiểm tra hồ sơ ở DKT), không phải thẩm định.

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_07`.
2. Vào HSCT trạng thái DTD (Đang thẩm định) — ví dụ HSCT000067.
3. Click "Thẩm định".
4. Quan sát section "Kết quả thẩm định" trong form.

### Kết quả mong đợi

- Form thẩm định chỉ có 2 radio: "Đạt" (→ CPD) và "Không đạt" (→ TU_CHOI) theo SRS FR-V.II-09 §Inputs.
- Yêu cầu bổ sung là chức năng B4 ở DKT (CB Nghiệp vụ ở khâu kiểm tra hồ sơ), không xuất hiện ở khâu thẩm định.

### Kết quả thực tế

- Form thẩm định có 3 radio: "Đạt", "Không đạt", "Cần bổ sung". Việc bổ sung outcome "Cần bổ sung" gây nhầm vai trò DKT vs DTD và mở thêm SM transition không có trong spec (DTD → ?).

### Bằng chứng

![BUG-CHITRA-003 — Form thẩm định có 3 radio outcome](image/bug-chitra-003-form-thamdinh-3-radio.png)

---

## ~~BUG-CHITRA-004~~ [CLOSED] — Lịch sử xử lý ghi enum code thay vì tiếng Việt

> **Re-test:** 2026-05-10 20:33:00 R3 — ✅ PASS (Closed-verified). HSCT200001 walk B2/B3/B-Đánh-giá/B7/Trình-PD. Lịch sử xử lý ghi tiếng Việt thuần: "Tiếp nhận / Đang kiểm tra", "Kiểm tra / Đang đánh giá", "Đánh giá / Đang thẩm định", "Thẩm định / Đang thẩm định", "Trình phê duyệt / Chờ phê duyệt". 0 enum leak (KHÔNG còn `CAP_NHAT_THANH_TOAN`, `TRINH_PHE_DUYET`).


### Mô tả

Trong section "Lịch sử xử lý" của HSCT, có 2 dòng ghi nguyên enum code thay vì label tiếng Việt: dòng B7 ghi `TRINH_PHE_DUYET` và dòng B11 ghi `CAP_NHAT_THANH_TOAN`. Các dòng khác (Tiếp nhận, Đánh giá, Thẩm định, Từ chối) đều đúng tiếng Việt. Vi phạm SCR-V.II-02 §Lịch sử xử lý yêu cầu hiển thị label tiếng Việt cho mọi action.

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_07`.
2. Walk HSCT000067 qua các bước: B2 → B3 → B6 → B7 → B10 → B8.
3. Walk HSCT000069 qua B11.
4. Vào trang chi tiết, scroll xuống "Lịch sử xử lý".

### Kết quả mong đợi

- Mọi dòng lịch sử hiển thị label tiếng Việt theo SCR-V.II-02 §Lịch sử xử lý: "Trình phê duyệt", "Cập nhật thanh toán" (không in hoa, không gạch dưới).

### Kết quả thực tế

- Dòng tương ứng B7 ghi: `TRINH_PHE_DUYET` (raw enum).
- Dòng tương ứng B11 ghi: `CAP_NHAT_THANH_TOAN` (raw enum).
- Các dòng khác đã dịch đúng — chỉ 2 transition này lọt enum mapping.

### Bằng chứng

![BUG-CHITRA-004 — Lịch sử có dòng "CAP_NHAT_THANH_TOAN"](image/bug-chitra-004-history-enum-leak.png)

---

## ~~BUG-CHITRA-005~~ [CLOSED] — Spinbutton "Số tiền thực trả" bound mâu thuẫn (min=1, value=0)

> **Re-test:** 2026-05-10 20:43:00 R3 — ✅ PASS (Closed-verified). HSCT000034 (DA_DUYET, cb_nv_dp_01, `?action=cap-nhat-thanh-toan`). Form B11 spinbutton "Số tiền thực trả" render `valuemin="0" valuemax="46975280" value="0" valuetext=""` — bound consistent. Field "Ngày thanh toán" prefilled `2026-05-10`. Form đầy đủ: 2 radio outcome (Đã thanh toán / Từ chối thanh toán), số biên nhận, ghi chú, button "Cập nhật thanh toán".


### Mô tả

Tại form B11 (Cập nhật thanh toán), spinbutton "Số tiền thực trả" khi mở mặc định có `value=0` nhưng `valuemin=1`. Tức field bắt buộc nhập (* required) đã ở trạng thái invalid ngay khi load form, dù chưa có thao tác user. Vi phạm FR-V.II-13 §Inputs row "Số tiền thực trả" yêu cầu hợp lệ giữa min/value/max.

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_07`.
2. Vào HSCT trạng thái DA_DUYET (HSCT000069).
3. Click "Cập nhật TT".
4. Quan sát thuộc tính spinbutton "Số tiền thực trả" qua DevTools / accessibility tree.

### Kết quả mong đợi

- Khi load form, spinbutton có giá trị mặc định ≥ valuemin (ví dụ value=0 + min=0, hoặc value=null + min=1 + cho phép trống).
- Form không ở trạng thái invalid mặc định trước khi user nhập.

### Kết quả thực tế

- Snapshot a11y: `spinbutton "* Số tiền thực trả" value="0" valuemax="6592562" valuemin="1" valuetext=""` — value=0 < valuemin=1.
- User vẫn nhập giá trị hợp lệ và submit được, nhưng trạng thái form ban đầu sai semantic.

### Bằng chứng

```text
A11y snapshot tại GET /chi-tra/{id}?action=cap-nhat-thanh-toan:
spinbutton "* Số tiền thực trả question-circle" value="0" valuemax="6592562" valuemin="1" valuetext=""
```

(Khung form B11 xem ở `bug-chitra-004-history-enum-leak.png` cùng folder — section "Số tiền thực trả".)

---

## ~~BUG-CHITRA-006~~ [CLOSED] — Wording mâu thuẫn spec B8 ("trả về thẩm định" hay "từ chối")

> **Re-test:** 2026-05-10 20:40:00 R3 — ✅ PASS (Closed-verified). cb_pd_dp_01, HSCT000023 form Phê duyệt → click "Trả về thẩm định" (button label đã đổi từ "Từ chối — trả về thẩm định"). Modal heading: "Trả về thẩm định" (đã đổi từ "Từ chối hồ sơ"). Submit lý do + Xác nhận trả về → endpoint `POST /api/v1/ho-so-chi-tras/{id}/tra-ve-tham-dinh` (đã đổi từ `/tu-choi`) → 200 OK → state CPD → DTD. **3/3 layer wording sửa đúng spec.** Residual cosmetic: lịch sử action label vẫn "Từ chối" (uid=131_0) thay vì "Trả về thẩm định" — không gây nhầm lẫn nghiệp vụ vì state hiển thị "Đang thẩm định".
![BUG-CHITRA-006 R3 — endpoint + button + modal đã đổi sang "Trả về thẩm định"](image/r3-bug006-after-fix-tra-ve-tham-dinh.png)


### Mô tả

CB PD thực hiện B8 (CHO_PHE_DUYET → DANG_THAM_DINH — "trả về thẩm định") qua form Phê duyệt hồ sơ. UI/API có 3 layer wording mâu thuẫn spec:
1. Endpoint URL: `POST /api/v1/ho-so-chi-tras/{id}/tu-choi` (gọi là "tu-choi" / từ chối).
2. UI button trong form Phê duyệt: "Từ chối — trả về thẩm định" (kết hợp 2 khái niệm).
3. Modal heading sau khi click: "Từ chối hồ sơ" (chỉ "từ chối").

Theo spec `02-thu-tu-module.md` line 738 (SM-CHI-TRA): B8 là `CHO_PHE_DUYET → DANG_THAM_DINH`, nghĩa là "trả về thẩm định" để CB nghiệp vụ thẩm định lại — KHÔNG phải "từ chối hồ sơ" (TU_CHOI là state cuối, terminal). Wording "Từ chối" gây nhầm lẫn với B5 (DKT → TU_CHOI) và B12 (DA_DUYET → TU_CHOI), cả hai đều là từ chối thật sự.

### Các bước tái hiện

1. Đăng nhập `cb_pd_dp_02` (CB PD BG).
2. Sidebar "Quản lý chi trả chi phí" → tab "Chờ phê duyệt".
3. Click "Phê duyệt" trên HSCT bất kỳ ở CHO_PHE_DUYET.
4. Quan sát form Phê duyệt hồ sơ → 2 button: "Phê duyệt" và **"Từ chối — trả về thẩm định"**.
5. Click button thứ 2 → modal mở với heading **"Từ chối hồ sơ"**.
6. Submit → Network tab: `POST /api/v1/ho-so-chi-tras/{id}/`**`tu-choi`**.
7. Response `trangThai: "DANG_THAM_DINH"` (KHÔNG phải TU_CHOI).

### Kết quả mong đợi

- Theo spec line 738 SM-CHI-TRA: B8 là "trả về thẩm định". Wording UI/API NÊN dùng "Trả về" / "Trả về thẩm định" / "Yêu cầu thẩm định lại".
- Endpoint NÊN đổi tên: `POST /api/v1/ho-so-chi-tras/{id}/tra-ve-tham-dinh` (hoặc `/yeu-cau-tham-dinh-lai`).
- UI button đơn nghĩa: "Trả về thẩm định" (bỏ "Từ chối —").
- Modal heading: "Trả về thẩm định" (bỏ "Từ chối hồ sơ").

### Kết quả thực tế

- Endpoint `/tu-choi` + button "Từ chối — trả về thẩm định" + modal "Từ chối hồ sơ" — 3 layer dùng từ "từ chối" gây nhầm với TU_CHOI thực sự.
- Tester (và end-user CB PD) phải tự suy luận "đây không phải TU_CHOI thật sự, mà là trả về thẩm định" qua doc spec → khó training cho user.

### Bằng chứng

![BUG-CHITRA-006 — Form Phê duyệt + button Từ chối trả về + modal Từ chối](../../workflow/chi-tra/evidence/r2-b8-after-hsct000027-DTD.png)

```text
POST /api/v1/ho-so-chi-tras/f0000000-0000-4000-8000-000000000027/tu-choi
Body: {"lyDoTuChoi":"CB PD trả về thẩm định: phí tư vấn 38.333.309 vượt trần năm SIEU_NHO 3M, đề nghị thẩm định lại","version":1}
Response: {"success":true,"data":{"trangThai":"DANG_THAM_DINH",...}}
```

→ State `DANG_THAM_DINH` confirm là B8 spec đúng (không phải TU_CHOI). URL endpoint + UI wording sai spec.

---

## ~~BUG-CHITRA-007~~ [CLOSED — false positive] — Form Cập nhật/Từ chối thanh toán không render trên DA_DUYET HSCT

> **Re-test:** 2026-05-10 20:43:00 R3 — ✅ PASS (Closed-verified, false-positive). R2 reproduce sai role: cb_pd_dp_01 (CB Phê duyệt) không có quyền B10/B12 → form ẩn đúng spec. Re-test với cb_nv_dp_01 (CB Nghiệp vụ — actor đúng B10/B12 per SM-CHI-TRA line 740-741): form RENDER đầy đủ trên HSCT000034 `?action=cap-nhat-thanh-toan`. Form components: heading "Cập nhật thanh toán" + radio "Kết quả thanh toán" (Đã thanh toán / Từ chối thanh toán) + spinbutton "Số tiền thực trả" valuemax=46.9M + Ngày thanh toán prefilled + Số biên nhận + Ghi chú + button "Cập nhật thanh toán". **Không phải bug — R2 reproduce sai role**.
![BUG-CHITRA-007 R3 — form B10/B12 render đầy đủ với cb_nv_dp_01 (correct actor per spec)](image/r3-bug007-form-renders-cb-nv-dp.png)


### Mô tả

CB PD click "Cập nhật TT" trên row HSCT state DA_DUYET trong tab "Đã xử lý". Page navigate sang `/chi-tra/{id}?action=cap-nhat-thanh-toan` đúng convention, GET `/ho-so-chi-tras/{id}` 200 OK trả về data, nhưng main page chỉ render thông tin DN + "Lịch sử xử lý / Chưa có lịch sử xử lý". KHÔNG có form input "Số tiền thực trả", "Mã chuyển khoản", "Ngày thanh toán", KHÔNG có button "Cập nhật" / "Từ chối thanh toán". Block B10 (DA_DUYET → DA_THANH_TOAN) + B12 (DA_DUYET → TU_CHOI_THANH_TOAN) cho toàn pool DA_DUYET legacy.

### Các bước tái hiện

1. Đăng nhập `cb_pd_dp_01` (CB PD DP AG) — Secret@123 + OTP 666666.
2. Sidebar "Quản lý chi trả chi phí" → tab "Đã xử lý".
3. Tìm HSCT state "Đã duyệt" (vd HSCT000034 — Hộ kinh doanh Đại Việt AG, Siêu nhỏ, 46.975.278 ₫).
4. Click button "Cập nhật TT" cuối row.
5. Quan sát page navigate `/chi-tra/f0000000-0000-4000-8000-000000000034?action=cap-nhat-thanh-toan`.
6. Wait page render. Inspect main element.

### Kết quả mong đợi

- Theo spec FR-V.II-13 §Inputs: form B10 có "Số tiền thực trả" (spinbutton min=1, max=duyệt), "Mã chuyển khoản", "Ngày thanh toán", textbox ghi chú, button "Cập nhật thanh toán" + "Từ chối thanh toán".
- Theo SM-CHI-TRA line 740-741: B10 transition DA_DUYET → DA_THANH_TOAN; B12 transition DA_DUYET → TU_CHOI_THANH_TOAN. Cả 2 cần form input.

### Kết quả thực tế

- Main page: thông tin DN + spec pipeline + Lịch sử xử lý ("Chưa có lịch sử xử lý") + KHÔNG form / input / button action.
- `evaluate_script` xác nhận: `headings: []`, `forms: 0`, `inputs: []`, `buttons: ["Quay lại danh sách"]`.
- Lặp 5 record (HSCT000031, 000033, 000034, 200019, plus snapshot 4 record khác cùng pool) — toàn bộ cùng pattern. Tất cả 5 record có "Chưa có lịch sử xử lý" → giả thuyết form B10/B12 conditional render khi `lichSu.length > 0` chứ không phải state DA_DUYET. Pool seed legacy không tạo lichSu khi insert thẳng DA_DUYET → form không xuất hiện.
- Cb_pd_dp_01 hold đúng role + scope AG + permission BR-AUTH-05 (đã verified click button row OK + GET API 200) → loại bỏ giả thuyết permission gate.

### Bằng chứng

![BUG-CHITRA-007 — HSCT000034 DA_DUYET form B10 không render](../../workflow/chi-tra/evidence/r3-b10-form-missing-hsct000034.png)

```text
URL: http://103.172.236.130:3000/chi-tra/f0000000-0000-4000-8000-000000000034?action=cap-nhat-thanh-toan
GET /api/v1/ho-so-chi-tras/f0000000-0000-4000-8000-000000000034 → 200 OK
evaluate_script ghi nhận:
  forms: 0
  inputs: []
  buttons: ["Quay lại danh sách"]   # KHÔNG có "Cập nhật thanh toán" / "Từ chối thanh toán"
  text snippet: "Lịch sử xử lý / Chưa có lịch sử xử lý"
```

→ Form B10/B12 missing trên detail page DA_DUYET. Bug có thể do conditional render dựa lichSu, hoặc form chỉ render khi mount từ workflow walker (không phải từ row action). Block B10/B12 walk + R7.6.1 R3 cascade BLOCKED.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT + OTP (localStorage `auth-store` + HttpOnly refresh cookie) |
| Tool test | Chrome DevTools MCP |
| Account | `cb_nv_tw_07`, `cb_pd_tw_07` (Secret@123) |

---

*Bug report generated: 2026-05-09 18:18:00 | QA Automation via Claude Code*
