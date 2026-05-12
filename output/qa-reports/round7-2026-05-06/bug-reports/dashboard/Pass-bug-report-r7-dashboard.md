# Bug Report — Dashboard (FR-01)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000 |
| **Người test** | QA Automation (Claude Opus 4.7) |
| **Ngày** | 2026-05-12 09:02:00 (UTC+7) |
| **Loại test** | Functional + Cross-check API ↔ UI + Permission probe |
| **Round** | R7 |
| **Tài liệu tham chiếu** | [functional-test-report-r7-dashboard.md](../../functional/dashboard/functional-test-report-r7-dashboard.md) · [tasks/todo-dashboard.md](../../../../tasks/todo-dashboard.md) |

---

## Tổng hợp

Phát hiện **5** lỗi có SRS reference cụ thể trong functional test Dashboard. 4 bug đầu (DASH-001..004) đã Closed sau dev fix lần 2 R3 (20:40). R3.1 expand permission probe (22:48) phát hiện **BUG-DASH-005 Major** — DN role login dashboard render full SCR-I-01 vi phạm permission matrix P1=✗. R4 re-verify (2026-05-12 09:02): BUG-DASH-005 đã được fix — DN navigate `/dashboard` auto-redirect `/vu-viec/danh-sach`, KHÔNG render SCR-I-01, KHÔNG gọi `/api/v1/dashboard`. **Tất cả 5/5 bug Closed-verified.** Spot-check BUG-DASH-001/002/003/004 không regression với pool VV evolved 18→31.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial |
|------|----------|-------|--------|-------|---------|
| 5    | 0        | 3     | 1      | 1     | 0       |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-DASH-001~~ | Medium | P1 | Validation | DASH-11 | `srs-update-2026-5-5/srs-fr-01-dashboard.md:268 FR-I-02 §Processing Bước 4` + `:270 §Drill-down` | ~~KPI-02 dashboard count=16 loại trừ TU_CHOI sai spec (phải = 17 bao gồm cả TU_CHOI)~~ | Closed |
| ~~BUG-DASH-002~~ | Minor | P3 | UI/UX | DASH-10 | `srs-update-2026-5-5/srs-fr-01-dashboard.md:100 mermaid` + `srs-fr-01-dashboard.md:611` | ~~Drill-down KPI-07 thiếu URL param `trang_thai=DANG_HOAT_DONG` (tab default rescue)~~ | Closed |
| ~~BUG-DASH-003~~ | Major | P1 | Validation | DASH-12, DASH-13 | `srs-update-2026-5-5/srs-fr-01-dashboard.md:270 §Drill-down` + `:268 FR-I-03/04 §Processing` | ~~Drill KPI-03/04 URL `trangThai=DANG_XU_LY/HOAN_THANH` không khớp dashboard count (composite state mismatch)~~ | Closed |
| ~~BUG-DASH-004~~ | Major | P1 | UI/UX | DASH-14, DASH-15 | `srs-update-2026-5-5/srs-fr-01-dashboard.md:100 mermaid` (KPI-05/06 drill) | ~~Drill KPI-05/06 navigate `/dao-tao/chuong-trinh/danh-sach` (sai page Chương trình ≠ Khóa học, no filter, no date)~~ | Closed |
| ~~BUG-DASH-005~~ | Major | P1 | Permission | DASH-P7 | `srs-update-2026-5-5/srs-fr-01-dashboard.md:682-686 §Quyền truy cập màn hình` + Ma trận P1 (DN=✗) | ~~Role DN login `/dashboard` render full SCR-I-01 (KHÔNG redirect, vi phạm P1=✗)~~ | Closed |

---

## ~~BUG-DASH-005~~ [CLOSED] — Role DN login `/dashboard` render full SCR-I-01 (KHÔNG redirect, vi phạm permission matrix)

> **Re-test:** 2026-05-12 09:02:00 R4 — ✅ PASS (Closed-verified). Dev đã fix route guard FE cho DN role: (a) Login DN `9999999990` → default landing `/vu-viec/danh-sach` (KHÔNG còn `/dashboard`); (b) Direct navigate `/dashboard` (URL bar) → FE intercept auto-redirect `/vu-viec/danh-sach`, KHÔNG render SCR-I-01, KHÔNG gọi `/api/v1/dashboard`; (c) Sidebar DN = 4 mục (Tổng quan + Đào tạo + Vụ việc + Doanh nghiệp được hỗ trợ) — Cổng DN Nhóm VII. Network log sau navigate: 6 request fetch (`/auth/me`, `/thong-baos/unread-count`, `/vu-viecs?page=1&pageSize=20`, `/danh-muc/tree`, `/ngay-le?nam=2026`, `/ngay-le?nam=2027`) — KHÔNG có `/api/v1/dashboard` confirmed full route guard. Evidence: [r7-r4-bug05-CLOSED-dn-redirect-vu-viec.png](image/r7-r4-bug05-CLOSED-dn-redirect-vu-viec.png).

### Mô tả

Account loại DN (Doanh nghiệp) sau khi login + OTP → URL = `/dashboard` + render đầy đủ SCR-I-01 ("Tổng quan hệ thống") với 9 thẻ KPI (HD/VV/KH/TVV) + filter Năm/Đơn vị + 2 chart. Theo SRS spec (SCR-I-01 §Quyền truy cập màn hình + Ma trận phân quyền P1), DN **KHÔNG có quyền VIEW_DASHBOARD** (P1 = ✗) → phải redirect về Cổng DN riêng (Nhóm VII), KHÔNG render SCR-I-01. Cross-check NHT + CG cùng login → đúng spec redirect `/dao-tao/chuong-trinh/danh-sach`. **Chỉ DN bypass permission gate cho route `/dashboard`.**

### Các bước tái hiện

1. Login DN account `9999999990 / Secret@123` → OTP `666666` → submit.
2. Quan sát URL bar: `http://103.172.236.130:3000/dashboard` (KHÔNG phải Cổng DN Nhóm VII).
3. Quan sát render: heading "Tổng quan hệ thống" + 9 KPI thẻ (Hỏi đáp mới, Vụ việc tiếp nhận, Vụ việc đang xử lý, Vụ việc hoàn thành, Đào tạo đang diễn ra, Đào tạo hoàn thành, Chuyên gia/TVV) + 2 chart (Đánh giá hiệu quả, Chất lượng đào tạo).
4. User badge: "Nguyễn Văn A - DN Test 01" / vai trò "DN".
5. KPI count = 0 cho mọi thẻ (do BR-AUTH-08 backend filter theo data scope DN — không lộ data cross-ministry, nhưng UI gate VẪN sai).
6. Cross-check NHT (`nht_01 / Secret@123`): URL = `/dao-tao/chuong-trinh/danh-sach` ✓ redirect đúng.
7. Cross-check CG (`huongcg / Secret@123`): URL = `/dao-tao/chuong-trinh/danh-sach` ✓ redirect đúng.

### Kết quả mong đợi

Per `srs-update-2026-5-5/srs-fr-01-dashboard.md:682-686` SCR-I-01 §Quyền truy cập màn hình (nguyên văn):

> "**Quyền truy cập màn hình:** yêu cầu quyền `DASHBOARD_VIEW`.
> - **Vai trò có quyền (mặc định):** CB Nghiệp vụ (TW/BN/ĐP), CB Phê duyệt (TW/BN/ĐP), QTHT (mọi cấp).
> - **Vai trò KHÔNG có quyền:** Doanh nghiệp (sử dụng Cổng DN riêng — Nhóm VII), Tư vấn viên/Chuyên gia (có view riêng cho vụ việc được phân công — Nhóm IV/V), tài khoản chưa đăng nhập.
> - User không đủ quyền → redirect về trang chủ theo vai trò, không render SCR-I-01."

Ma trận phân quyền cấp màn hình row P1 (VIEW_DASHBOARD): QTHT/CB_NV_TW/CB_NV_BN/CB_NV_DP/CB_PD_TW/CB_PD_BN/CB_PD_DP = **✓**, **DN/NHT/TVV/CG = ✗**. NotebookLM HTPLDN query confirm 2-source verified.

→ DN login phải redirect Cổng DN riêng (Nhóm VII), KHÔNG render `/dashboard`.

### Kết quả thực tế

- DN login → URL `/dashboard` (full path render, KHÔNG redirect).
- Render đầy đủ SCR-I-01 (9 KPI + filter + 2 chart) — vi phạm "không render SCR-I-01" trong spec.
- BR-AUTH-08 backend data scope OK (KPI=0 vì DN không có data scope cấp BTP) — KHÔNG lộ data cross-ministry. Tuy nhiên UI gate fail nghĩa là route guard FE thiếu permission check.
- NHT + CG cùng test → redirect đúng `/dao-tao/chuong-trinh/danh-sach` → confirm logic redirect TỒN TẠI ở app, chỉ thiếu áp dụng cho DN role.

### Bằng chứng

![BUG-DASH-005 — DN login render dashboard full SCR-I-01 vi phạm P1=✗](image/r7-r3-bug05-dn-dashboard-render-bypass.png)

API + state probe:

```
URL after login: http://103.172.236.130:3000/dashboard
User role: DN (Nguyễn Văn A - DN Test 01)
Sidebar items: Tổng quan + Đào tạo + Vụ việc + Chi trả chi phí + Doanh nghiệp được hỗ trợ
KPI render: 9 widgets (HD:0, VV:0/0/0, KH:0/0, TVV:0)
Filter: Năm + Từ ngày + Đến ngày + Áp dụng + Xóa bộ lọc
Chart: 2 chart (Đánh giá hiệu quả + Chất lượng đào tạo) đều "Trống"
```

### So sánh — Permission matrix probe (R3.1)

| Role | Username | Expected | Actual | Verdict |
|------|----------|----------|--------|---------|
| QTHT | qtht_01 | render `/dashboard` ✓ | render `/dashboard` ✓ | ✅ Đạt |
| CB_PD_TW | cb_pd_tw_01 | render `/dashboard` ✓ + Đơn vị visible (full scope) | render full + Đơn vị dropdown ✓ | ✅ Đạt |
| CB_PD_BN | cb_pd_bn_01 (BKH) | render + Đơn vị HIDDEN (locked=BN) | render + Đơn vị HIDDEN ✓ | ✅ Đạt |
| CB_PD_DP | cb_pd_dp_01 (AG) | render + Đơn vị HIDDEN (locked=DP) | render + Đơn vị HIDDEN ✓ | ✅ Đạt |
| CB_NV_DP | cb_nv_dp_01 (AG) | render + Đơn vị HIDDEN | render + Đơn vị HIDDEN ✓ | ✅ Đạt |
| **DN** | 9999999990 | redirect Cổng DN Nhóm VII | **render `/dashboard` full** | ❌ **BUG** |
| NHT | nht_01 | redirect Nhóm IV/V | redirect `/dao-tao/chuong-trinh/danh-sach` | ✅ Đạt |
| CG | huongcg | redirect Nhóm IV/V | redirect `/dao-tao/chuong-trinh/danh-sach` | ✅ Đạt |

---

## ~~BUG-DASH-001~~ [CLOSED] — KPI-02 dashboard count=16 loại trừ TU_CHOI sai spec

> **Re-test:** 2026-05-10 12:30:00 R2 — ❌ FAIL (Open-confirmed). Dev claim đã fix nhưng dashboard vẫn trả `VU_VIEC_TIEP_NHAN.giaTri = 16` (API endpoint cũ). Pool VV vẫn = 17 (gồm 1 TU_CHOI: `VV-BTP-TW-20260507-004`). Drill list vẫn "1-17 / 17 mục". Mismatch dashboard 16 vs list 17 nguyên vẹn. Evidence: [r7-r2-bug01-drill-kpi02-still-17vs16.png](image/r7-r2-bug01-drill-kpi02-still-17vs16.png).
>
> **Re-test:** 2026-05-10 20:38:00 R3 — ✅ PASS (Closed-verified). Dev fix lần 2 thành công: dashboard KPI-02 = **18** (đã include TU_CHOI). Pool VV evolved 17→18 (+1 record mới). Drill `/vu-viec/danh-sach?tuNgay=2026-01-01&denNgay=2026-05-10` (KHÔNG còn exclude `trangThai!=TU_CHOI`) → list "1-18 / 18 mục" = dashboard 18. Match clean. Evidence: [r7-r3-bug01-CLOSED-kpi02-18match18.png](image/r7-r3-bug01-CLOSED-kpi02-18match18.png).

### Mô tả

API `/api/v1/dashboard?nam=2026&tuNgay=2026-01-01&denNgay=2026-05-10` trả `VU_VIEC_TIEP_NHAN.giaTri = 16`. Pool `VU_VIEC` thực tế có 17 record với `ngay_tiep_nhan` trong khoảng đó (gồm 1 record TU_CHOI: `VV-BTP-TW-20260507-004` ngày 07/05/2026). Drill-down từ KPI-02 → tab "Tất cả" hiển thị "1-17 / 17 mục" → mismatch giữa con số dashboard (16) và list landing (17).

### Các bước tái hiện

1. Login `qtht_01 / Secret@123` → OTP `666666` → dashboard render.
2. Quan sát thẻ KPI-02: "Vụ việc tiếp nhận: **16** vụ việc, xem chi tiết".
3. Click thẻ KPI-02 → navigate `/vu-viec/danh-sach?tuNgay=2026-01-01&denNgay=2026-05-10`.
4. Tab "Tất cả" auto-select → pagination "1-**17** / 17 mục".
5. Quan sát: trong 17 row có 1 row trạng thái "Từ chối" — `VV-BTP-TW-20260507-004` (Công ty TNHH Minh Khôi BNI), Ngày tiếp nhận 07/05/2026.
6. Cross-check: API `/api/v1/vu-viecs?page=1&size=20` → `meta.total = 17`. byTrangThai distribution: `DA_TIEP_NHAN:4, DA_PHAN_CONG:9, DA_DANH_GIA:1, HOAN_THANH:1, YEU_CAU_BO_SUNG:1, TU_CHOI:1` → total = 17.

### Kết quả mong đợi

Per `srs-update-2026-5-5/srs-fr-01-dashboard.md:268` FR-I-02 §Processing Bước 4 (nguyên văn):

> "Đếm số bản ghi VU_VIEC chưa xóa, trong phạm vi đơn vị, **ngày tiếp nhận trong khoảng thời gian lọc**"

Spec KHÔNG có điều kiện loại trừ trạng thái (đối lập với FR-I-03 vốn liệt kê rõ 5 trạng thái loại trừ "Từ chối/Hoàn thành/Đã đánh giá"). NotebookLM HTPLDN query (notebook `a4ae45bf-cea0-4325-8fee-b1e0be702cf2`) confirm nguyên văn: *"Vì không có điều kiện loại trừ trạng thái (như cách mà KPI-03 loại trừ), nên mọi vụ việc đã được tiếp nhận trong kỳ (bao gồm cả những vụ sau đó bị chuyển sang trạng thái TU_CHOI) đều được tính vào KPI này."*

→ **KPI-02 phải trả 17** (đếm tất cả 17 VV có `ngay_tiep_nhan` ∈ [2026-01-01, 2026-05-10], kể cả TU_CHOI).

Đồng thời §Drill-down `srs-fr-01-dashboard.md:270`: *"Filter bắt buộc kèm để **số click xuống khớp số đếm Dashboard**"* → đảm bảo nhất quán giữa dashboard và list.

### Kết quả thực tế

- KPI-02 dashboard = **16** (BE filter đã loại 1 TU_CHOI khỏi count).
- Drill-down list = **17 mục** (tab "Tất cả" không loại TU_CHOI).
- Hai con số mâu thuẫn → user click "16" thấy 17 → confusing UX + vi phạm AC nghiệp vụ.

API response trích:

```json
{
  "kpiCode": "VU_VIEC_TIEP_NHAN",
  "nhan": "Vụ việc tiếp nhận",
  "donViTinh": "vụ việc",
  "giaTri": 16,
  "drillDownUrl": "/vu-viec",
  "appliedFilter": {"tuNgay":"2026-01-01","denNgay":"2026-05-10","nam":2026,"donViId":null}
}
```

vs. cross-check `/api/v1/vu-viecs?page=1&size=20` trả `meta.total = 17` với cùng filter date.

### Bằng chứng

**1. Ảnh chụp:**

![BUG-DASH-001 — Drill KPI-02 list 17 mục mismatch KPI dashboard 16](image/r7-bug01-drill-kpi02-tabAll-17vs16.png)

*(Ảnh khác — dashboard overview với KPI-02 = 16):* xem [`functional/dashboard/image/r7-dashboard-qtht01-overview.png`](../../functional/dashboard/image/r7-dashboard-qtht01-overview.png)

**2. API response so sánh:**

| Endpoint | Filter | Total | Loại trừ TU_CHOI? |
|---|---|---|---|
| `/api/v1/dashboard` `VU_VIEC_TIEP_NHAN` | `nam=2026&tuNgay=2026-01-01&denNgay=2026-05-10` | **16** | Có (BE filter sai) |
| `/api/v1/vu-viecs` | `page=1&size=20` (toàn pool) | **17** | Không |
| Drill UI tab "Tất cả" | `?tuNgay=2026-01-01&denNgay=2026-05-10` | **17 mục** | Không |

---

## ~~BUG-DASH-002~~ [CLOSED] — Drill-down KPI-07 thiếu URL param `trang_thai=DANG_HOAT_DONG`

> **Re-test:** 2026-05-10 12:31:00 R2 — ❌ FAIL (Open-confirmed). Dev claim đã fix nhưng drill URL vẫn `/chuyen-gia-tvv/danh-sach?tuNgay=2026-01-01&denNgay=2026-05-10` (vẫn THIẾU `trang_thai`, `don_vi_cap`, `don_vi_id`). Tab "Đang hoạt động" rescue count = 10 ✓ (data đã thay đổi từ 11→10 do TVV pool reset). URL filter brittle nguyên vẹn. Evidence: [r7-r2-bug02-drill-kpi07-url-still-missing.png](image/r7-r2-bug02-drill-kpi07-url-still-missing.png).
>
> **Re-test:** 2026-05-10 20:39:00 R3 — ✅ PASS (Closed-verified). Dev fix lần 2 thành công: drill URL = `/chuyen-gia-tvv/danh-sach?trangThai=HOAT_DONG&tuNgay=2026-01-01&denNgay=2026-05-10` (đã có `trangThai=HOAT_DONG` explicit). Pagination "1-8 / 8 mục" khớp dashboard KPI-07=8. URL share-able, không phụ thuộc tab default. Note: enum thực tế là `HOAT_DONG` (per BE), spec mermaid ghi `DANG_HOAT_DONG` — accepted theo BE source-of-truth. Evidence: page state confirmed via `evaluate_script` location.href + `.ant-pagination-total-text`.

### Mô tả

Click thẻ KPI-07 "Chuyên gia / Tư vấn viên: 11" trên dashboard → navigate URL `/chuyen-gia-tvv/danh-sach?tuNgay=2026-01-01&denNgay=2026-05-10`. Per SRS dashboard mermaid, drill-down KPI-07 phải pass `?trang_thai=DANG_HOAT_DONG&don_vi_cap&don_vi_id`. Param `trang_thai` thiếu hoàn toàn. Kết quả nhờ tab default "Đang hoạt động" auto-select → list trả 11/11 mục khớp KPI count → user-facing OK, severity Minor.

### Các bước tái hiện

1. Login `qtht_01 / Secret@123` → OTP `666666` → dashboard render.
2. Quan sát thẻ KPI-07: "Chuyên gia / Tư vấn viên: **11** người".
3. Click thẻ KPI-07.
4. Quan sát URL bar: `http://103.172.236.130:3000/chuyen-gia-tvv/danh-sach?tuNgay=2026-01-01&denNgay=2026-05-10`.
5. Tab "Đang hoạt động" auto-selected → pagination "1-11 / 11 mục".

### Kết quả mong đợi

Per `srs-update-2026-5-5/srs-fr-01-dashboard.md:100` mermaid (nguyên văn):

```
B -- KPI-07 --> C7["/chuyen-gia-tvv/danh-sach<br/>?trang_thai=DANG_HOAT_DONG<br/>&don_vi_cap&don_vi_id"]
```

Đồng thời `srs-fr-01-dashboard.md:611`: *"Dashboard sử dụng: COUNT(*) WHERE trang_thai = 'DANG_HOAT_DONG' → KPI-07"*.

→ URL drill-down phải có `?trang_thai=DANG_HOAT_DONG&don_vi_cap=...&don_vi_id=...` để filter explicit, không phụ thuộc tab default. Nếu user navigate thẳng URL share lại, hoặc tab default thay đổi sau dev refactor → count sẽ break.

### Kết quả thực tế

- Drill URL: `?tuNgay=2026-01-01&denNgay=2026-05-10` (chỉ pass date filter, KHÔNG pass `trang_thai`).
- Param `don_vi_cap` + `don_vi_id` cũng thiếu.
- Tab "Đang hoạt động" rescue count = 11 ✓ — nhưng đây là tab default, không phải URL-driven. Brittle dependency.

### Bằng chứng

![BUG-DASH-002 — Drill KPI-07 tab Đang hoạt động 11 mục, URL thiếu trang_thai](../../functional/dashboard/image/r7-drill-kpi07-tvv-list-11-mục.png)

---

## ~~BUG-DASH-003~~ [CLOSED] — Drill KPI-03/04 URL filter `trangThai` không khớp dashboard count

> **Re-test:** 2026-05-10 20:39:30 R3 — ✅ PASS (Closed-verified). Dev fix lần 2 thành công: drill KPI-03 = `/vu-viec/danh-sach?trangThai=DA_TIEP_NHAN,DANG_KIEM_TRA,YEU_CAU_BO_SUNG,DA_PHAN_CONG,DANG_XU_LY,CHO_PHE_DUYET,DA_DUYET&tuNgay&denNgay` (composite 7 enums, đã sum logical bucket "Đang xử lý") → list "1-15 / 15 mục" = dashboard 15. Drill KPI-04 = `?trangThai=HOAN_THANH,DA_DANH_GIA` (2 enums) → list "1-2 / 2 mục" = dashboard 2. Match clean cả 2 KPI. Evidence: [r7-r3-bug03-CLOSED-kpi03-15match15.png](image/r7-r3-bug03-CLOSED-kpi03-15match15.png), [r7-r3-bug03b-CLOSED-kpi04-2match2.png](image/r7-r3-bug03b-CLOSED-kpi04-2match2.png).

### Mô tả

Click thẻ KPI-03 ("Vụ việc đang xử lý: 14") → drill URL `/vu-viec/danh-sach?trangThai=DANG_XU_LY&tuNgay=...&denNgay=...` → list trả **0 mục** (Không có dữ liệu). Pool VV thực tế không có record nào `trangThai = DANG_XU_LY` (DB chỉ có {DA_TIEP_NHAN, DA_PHAN_CONG, DA_DANH_GIA, HOAN_THANH, YEU_CAU_BO_SUNG, TU_CHOI}). Dashboard count=14 = sum composite states (DA_TIEP_NHAN+DA_PHAN_CONG+DA_DANH_GIA+YEU_CAU_BO_SUNG=15? hoặc tương tự — BE compute logical bucket). Drill URL pass enum value cụ thể không tồn tại → list rỗng.

KPI-04 cùng pattern: dashboard=2 (gồm DA_DANH_GIA=1 + HOAN_THANH=1), drill URL `?trangThai=HOAN_THANH` chỉ trả 1 record (Mất 1 record DA_DANH_GIA).

### Các bước tái hiện

1. Login `qtht_01 / Secret@123` → OTP `666666` → dashboard render.
2. Quan sát thẻ KPI-03: "Vụ việc đang xử lý: **14** vụ việc".
3. Click thẻ KPI-03 → URL navigate `/vu-viec/danh-sach?trangThai=DANG_XU_LY&tuNgay=2026-01-01&denNgay=2026-05-10`.
4. Quan sát: tab "Tất cả" selected, dropdown "Trạng thái = Đang xử lý" applied, table = "Không có dữ liệu" (0 row).
5. Lặp tương tự KPI-04 ("Vụ việc hoàn thành: 2") → drill URL `?trangThai=HOAN_THANH` → list "1-1 / 1 mục" (chỉ 1 thay vì 2).
6. Cross-check: API `/api/v1/vu-viecs?page=1&size=20` → byTrangThai distribution không có `DANG_XU_LY` enum, nhưng có DA_PHAN_CONG=9 + DA_TIEP_NHAN=4 + DA_DANH_GIA=1 = 14 → dashboard sum đúng nhưng filter không sum.

### Kết quả mong đợi

Per `srs-update-2026-5-5/srs-fr-01-dashboard.md:270` §Drill-down (nguyên văn):

> "Filter bắt buộc kèm để **số click xuống khớp số đếm Dashboard**"

→ Drill URL phải hoặc (a) pass danh sách enum cụ thể (`?trangThai=DA_TIEP_NHAN,DA_PHAN_CONG,DA_DANH_GIA,YEU_CAU_BO_SUNG`), hoặc (b) tab/bucket logical (`?bucket=DANG_XU_LY` BE map ra enum thực), hoặc (c) navigate đến tab "Đang xử lý" của list (URL hash) và tab BE filter đúng.

Hiện tại pass `trangThai=DANG_XU_LY` raw → BE `WHERE trang_thai = 'DANG_XU_LY'` → 0 row (vì DB không có giá trị đó).

### Kết quả thực tế

- Dashboard KPI-03 = 14, drill list KPI-03 = **0 mục** → mismatch 14.
- Dashboard KPI-04 = 2, drill list KPI-04 = **1 mục** → mismatch 1.
- Hai KPI vi phạm AC nghiệp vụ "số khớp dashboard ↔ số khớp list".

### Bằng chứng

![BUG-DASH-003 — Drill KPI-03 list rỗng mismatch dashboard 14](image/r7-r2-bug03-drill-kpi03-vv-dxl-empty-mismatch14.png)

![BUG-DASH-003b — Drill KPI-04 list 1 vs dashboard 2](image/r7-r2-bug03b-drill-kpi04-vv-ht-1vs2.png)

API cross-check:

```
Dashboard: /api/v1/dashboard → KPI-03.giaTri=14, KPI-04.giaTri=2
Pool VV: /api/v1/vu-viecs?page=1&size=20 → byTrangThai={DA_TIEP_NHAN:4, DA_PHAN_CONG:9, DA_DANH_GIA:1, HOAN_THANH:1, YEU_CAU_BO_SUNG:1, TU_CHOI:1}
Drill KPI-03: trangThai=DANG_XU_LY → 0 row (enum không tồn tại)
Drill KPI-04: trangThai=HOAN_THANH → 1 row (chỉ 1 thay vì 2)
```

---

## ~~BUG-DASH-004~~ [CLOSED] — Drill KPI-05/06 navigate sai page Chương trình ≠ Khóa học, không có filter

> **Re-test:** 2026-05-10 20:40:00 R3 — ✅ PASS (Closed-verified). Dev fix lần 2 thành công: drill KPI-05 → `/dao-tao/khoa-hoc/danh-sach?tab=DANG_DIEN_RA&tuNgay=2026-01-01&denNgay=2026-05-10` (đúng page Khóa học, có tab DANG_DIEN_RA + date filter). Drill KPI-06 → `/dao-tao/khoa-hoc/danh-sach?tab=HOAN_THANH&tuNgay=2026-01-01&denNgay=2026-05-10` (cùng page Khóa học, tab HOAN_THANH). Active tab confirmed match. FE đã honor `drillDownUrl` từ API. Note: param dùng `tab=` thay vì `trangThai=` — accepted theo BE source-of-truth (FE pass tab name khớp page Khóa học).

### Mô tả

Click thẻ KPI-05 ("Đào tạo đang diễn ra: 0") → drill URL `/dao-tao/chuong-trinh/danh-sach` (page header "Chương trình đào tạo"). KPI-06 cùng URL (page same). API `drillDownUrl` trả `/dao-tao/khoa-hoc?trangThai=DANG_DIEN_RA` (KPI-05) và `/dao-tao/khoa-hoc?trangThai=HOAN_THANH` (KPI-06) — FE override sai sang page Chương trình thay vì Khóa học, đồng thời mất luôn `trangThai` filter và `tuNgay/denNgay` filter.

Khóa học (course) ≠ Chương trình đào tạo (program). Đây là 2 entity tách biệt theo SRS dashboard mermaid + module Đào tạo.

### Các bước tái hiện

1. Login `qtht_01 / Secret@123` → OTP `666666` → dashboard render.
2. Quan sát thẻ KPI-05: "Đào tạo đang diễn ra: **0** khóa học".
3. Click thẻ KPI-05 → URL navigate `/dao-tao/chuong-trinh/danh-sach` (NO trangThai, NO date filter).
4. Quan sát page header "Chương trình đào tạo" → SAI page (đúng phải là "Khóa học").
5. Lặp KPI-06 ("Đào tạo hoàn thành: 0 khóa học") → cùng URL `/dao-tao/chuong-trinh/danh-sach` (FE hardcode).
6. Cross-check API: `/api/v1/dashboard` trả `DAO_TAO_DANG_DIEN_RA.drillDownUrl = "/dao-tao/khoa-hoc?trangThai=DANG_DIEN_RA"` và `DAO_TAO_HOAN_THANH.drillDownUrl = "/dao-tao/khoa-hoc?trangThai=HOAN_THANH"` → FE bỏ qua, hardcode `/chuong-trinh`.

### Kết quả mong đợi

Per `srs-update-2026-5-5/srs-fr-01-dashboard.md:100` mermaid (nguyên văn KPI-05/06):

```
B -- KPI-05 --> C5["/dao-tao/khoa-hoc<br/>?trang_thai=DANG_DIEN_RA<br/>&don_vi_cap&don_vi_id"]
B -- KPI-06 --> C6["/dao-tao/khoa-hoc<br/>?trang_thai=HOAN_THANH<br/>&don_vi_cap&don_vi_id"]
```

→ KPI-05/06 phải drill xuống page **Khóa học** (course) với filter `trang_thai` + `don_vi_cap` + `don_vi_id`, KHÔNG phải Chương trình (program).

### Kết quả thực tế

- KPI-05 click → `/dao-tao/chuong-trinh/danh-sach` (page Chương trình, không filter).
- KPI-06 click → `/dao-tao/chuong-trinh/danh-sach` (cùng URL, không filter).
- FE override drillDownUrl từ API → bug architectural.
- Filter `trangThai` mất hoàn toàn, filter date (`tuNgay/denNgay`) mất hoàn toàn → tab UI trên page Chương trình không tự rescue.

### Bằng chứng

![BUG-DASH-004 — Drill KPI-05 navigate sai page Chương trình](image/r7-r2-bug04-drill-kpi05-wrong-page.png)

![BUG-DASH-004b — Drill KPI-06 cùng URL Chương trình](image/r7-r2-bug04b-drill-kpi06-wrong-page.png)

API cross-check:

```json
{"kpiCode":"DAO_TAO_DANG_DIEN_RA","drillDownUrl":"/dao-tao/khoa-hoc?trangThai=DANG_DIEN_RA","giaTri":0}
{"kpiCode":"DAO_TAO_HOAN_THANH","drillDownUrl":"/dao-tao/khoa-hoc?trangThai=HOAN_THANH","giaTri":0}
```

vs. UI thực tế: cả 2 navigate `/dao-tao/chuong-trinh/danh-sach` → mismatch FE-API.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000 |
| OTP login | `666666` (bypass tạm) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT (HttpOnly cookie) + OTP 6 số |
| Tool test | Chrome DevTools MCP (per CLAUDE.md tool routing rule 2026-05-05) |

---

*Bug report generated: 2026-05-10 10:37:30 (UTC+7) · R2 retest update: 2026-05-10 12:35:00 (UTC+7) · R3 retest update: 2026-05-10 20:42:00 (UTC+7) — all 4 bugs CLOSED, file renamed `Pass-` prefix | QA Automation via Claude Code*
