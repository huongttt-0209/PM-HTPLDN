# Bug Report tổng hợp — report-dot-3 (22 case FAIL / 8 module)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường gốc** | http://103.172.236.130:3000/ |
| **Môi trường re-verify 2026-07-15** | http://18.143.165.120/login |
| **Người test** | QA Automation |
| **Ngày** | 2026-07-07 |
| **Loại test** | Functional / Permission / Workflow / Negative |
| **Round** | Tổng hợp case FAIL — `report-dot-3.xlsx` (đợt 3) |
| **Tài liệu tham chiếu** | [report-dot-3.xlsx](report-dot-3.xlsx) · SRS `input/srs-update-2026-5-5/` |

> **⚠️ Trạng thái verify (2026-07-07):** Server `103.172.236.130:3000` **không phản hồi** (`ERR_CONNECTION_TIMED_OUT`) tại thời điểm tổng hợp → **chưa re-verify lại được qua UI + chưa chụp được ảnh mới** cho 17 bug (trừ BUG-CT-BC-001 có ảnh round 30/06). Nội dung bug (bước tái hiện + kết quả mong đợi + kết quả thực tế) **lấy nguyên từ các case FAIL đã chạy** trong `report-dot-3.xlsx`. Khi server up: cần re-verify từng bug qua UI + bổ sung screenshot vào `image/`.
>
> **SRS reference:** ghi theo UC + mã lỗi/ số dòng như test report đã ghi. Các dòng SRS chưa được mở kiểm lại từng cái (trừ module CT HTPLDN đã verify `srs-fr-15`).

> **Cập nhật re-verify UI (2026-07-15 — Chrome DevTools MCP, UI-only, KHÔNG verify API):** Đã verify lại đủ 22 bug gốc qua browser trên UAT `http://18.143.165.120/login` (tài khoản theo `output/UAT_doi-tac/input/input.md`, OTP từ MailHog UI). Sau khi seed dữ liệu thiếu qua UI + đối chiếu nguyên văn SRS + kiểm chứng 2 chiều: **8 Closed-verified · 8 Reject (claim không tái hiện) · 2 BA confirm (SRS chưa định nghĩa rõ) · 3 Open (bug thật cần dev) · 1 Re-verify blocked (thiếu timeout fixture UI)**.
>
> **🔴 Double toast (user flag) — XÁC NHẬN, mang tính hệ thống:** Lỗi hiển thị **2 toast lỗi giống hệt** cho 1 thao tác, tái hiện chắc chắn ở **2 flow**: (1) **BUG-QT-001** — lỗi tương tranh optimistic lock khi xóa bản ghi vừa bị người khác sửa ("Bản ghi đã được người khác cập nhật…"); (2) **BUG-CT-BC-004 (note)** — tạo đợt báo cáo trùng kỳ ("Đã tồn tại đợt báo cáo cho kỳ này"). Cả 2 đo được `.ant-message-notice` max đồng thời = 2. Các flow khác (thêm/xóa danh mục — success=1 notification, delete=1 message; trình BC=1 message) KHÔNG double. ⇒ Dev cần khử trùng lặp toast lỗi ở tầng xử lý lỗi chung.

---

## Tổng hợp

Tổng hợp **22 lỗi** từ toàn bộ case FAIL của `report-dot-3.xlsx`, trải **8 module**. File chia section theo từng module.

Riêng **Module 18 (CT HTPLDN)** re-verify 2026-07-15 fresh qua UI với 3 tài khoản (`cbnv_tw` seed đợt · `cbnv_bn` lập/trình BC · `cbpd_bn` phê duyệt/thông báo), đợt fresh `DOT-SO_BO_NAM-2026-1`. Kết quả: 4 bug `Closed-verified` (CT-BC-001 mở chi tiết không 403, 003 không có action trình sai trạng thái, 004 phân quyền trình, 005 thông báo CB PD) và 1 bug `BA confirm` (CT-BC-002: trình được BC toàn số 0 — SRS chưa định nghĩa "hoàn chỉnh"). Phát hiện thêm double toast ở flow tạo đợt trùng kỳ (note trong CT-BC-004).

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial |
|------|----------|-------|--------|-------|---------|
| 22   | 0        | 8     | 5      | 9     | 0       |

### Verdict breakdown (re-verify 2026-07-15 · cập nhật 2026-07-16)

| Tổng | ✅ Closed-verified | ⛔ Reject (không tái hiện) | 🟡 BA confirm | ❌ Open (bug thật) | ⏸ Re-verify blocked |
|------|:---:|:---:|:---:|:---:|:---:|
| 22 | 11 | 8 | 2 | 0 | 1 |

> 🔁 **Cập nhật re-verify 2026-07-16:** 3 bug Open trước đó (HD-001, DT-002, QT-001) đã **lật Closed-verified** — không còn tái hiện (Closed 8→11, Open 3→0). Còn lại chưa xử lý: **1 Re-verify blocked** (BC-001, chưa dựng được fixture timeout >30s) + **2 chờ BA** (DN-003, CT-BC-002 — quyết định spec, không phải bug dev). 3 "bug mới phát sinh" (NEW-02/03/04) cũng đã hết tái hiện (xem mục "Bug mới phát sinh"). ⚠️ Cả loạt pass sau 1 ngày → nên xác nhận dev có bản deploy fix trước khi đóng chính thức.

> **[Lịch sử 07-15 — đã bị thay bởi cập nhật 07-16 ở trên]** **Re-verify 2026-07-15 (rigorous fresh, UI-only):** Tại thời điểm đó còn **3 bug Open thật cần dev**: `BUG-HD-001` (upload file 0 byte không bị chặn) · `BUG-DT-002` (chưa build xuất DOCX cho CTĐT đã duyệt) · `BUG-QT-001` (double toast lỗi tương tranh — cùng lỗi double toast với CT-BC-004 note). **8 bug Reject** (guard/validation thực tế hoạt động đúng, claim gốc không tái hiện: QT-002/003/004/005/006 + DT-001, VV-001, VV-002 — 3 bug này expected trích nhầm máy trạng thái/biến thể SRS, app không sai). **2 bug BA confirm** (SRS silent thật sự, không thể tự kết luận: DN-003 audit denied-access, CT-BC-002 định nghĩa "BC hoàn chỉnh"). **1 bug blocked** (`BUG-BC-001` thiếu timeout fixture UI).

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| **— Module 03 · Hỏi đáp pháp lý —** | | | | | | | |
| BUG-HD-001 | Medium | P2 | Negative | TC-HD-208 | `UC10 §Upload validation` | Upload file 0 byte không bị chặn | Closed-verified 2026-07-16 — re-test: file 0 byte đã bị chặn + toast đúng SRS (trước đó Open 07-15) |
| BUG-HD-002 | Minor | P3 | UI/UX | TC-PD-061 | `UC18 (INF-DAXL-01)` | Empty state tab Hoàn thành không hiển thị khi 0 HD đã xử lý | Closed-verified 2026-07-15 |
| **— Module 04 · Đào tạo tập huấn —** | | | | | | | |
| BUG-DT-001 | Major | P1 | Workflow | TC-KH-H-015 | `UC24 §State machine (srs-fr-03:2011 enum DA_HUY)` | Hủy KH Dự thảo không chuyển trạng thái Đã hủy | Reject — SM-KH Kế hoạch không có Hủy/DA_HUY; expected trích nhầm SM Khóa học 2026-07-15 |
| BUG-DT-002 | Major | P1 | Happy | TC-XUAT-H-003 | `FR-III-20 (srs-fr-03:1363-1386)` | Không xuất được DOCX cho CTĐT đã duyệt | Closed-verified 2026-07-16 — re-test: nút Xuất DOCX đã build, POST /export-doc 200 trả .docx thật (trước đó Open 07-15) |
| **— Module 08 · Vụ việc HTPL —** | | | | | | | |
| BUG-VV-001 | Medium | P2 | UI/UX | TC-VV-DS-105 | `UC51 §Sort (srs-fr-05:1647)` | Sort danh sách VV theo "Ngày tiếp nhận" không đúng | Reject — sort đúng; bug mới "ngày tiếp nhận rỗng" cũng KHÔNG còn tái hiện 2026-07-16 (không còn VV rỗng, sort NULLS LAST 2 chiều) |
| BUG-VV-002 | Medium | P2 | UI/UX | TC-VV-DS-201 | `UC51 §Empty state (INF-VV-01 srs-fr-05:144)` | Empty state khi lọc VV ra 0 kết quả không hiển thị đúng | Reject — app đúng INF-VV-01; expected trích nhầm biến thể 2026-07-15 |
| **— Module 10 · Quản lý doanh nghiệp —** | | | | | | | |
| BUG-DN-001 | Major | P1 | Data | TC-DN-101 | `UC81 §Xóa (BR-DATA-01)` | Không soft-delete được DN không có vụ việc | Closed-verified 2026-07-15 — soft-delete OK (DN TW-owned); lần trước test nhầm DN cross-tenant |
| BUG-DN-002 | Major | P1 | Data | TC-HSPL-201 | `UC150 §Xóa HSPL (BR-DATA-01, srs:593)` | Không soft-delete được hồ sơ pháp lý DN | Closed-verified 2026-07-15 |
| BUG-DN-003 | Major | P1 | Permission | TC-DN-PERM-404 | `UC120 (BR-DATA-05 srs-fr-13:854)` · SPEC-CLARIFY-DN-21 | Truy cập chéo đơn vị bị chặn nhưng không ghi audit log | BA confirm 2026-07-15 — chặn RBAC đúng; BR-DATA-05 không yêu cầu audit denied |
| **— Module 12 · Biểu mẫu —** | | | | | | | |
| BUG-BM-001 | Major | P1 | Negative | TC-BM-613 | `UC97 (ERR-CK-BM-02)` | Công khai được biểu mẫu khi thư mục cha đang ẩn | Closed-verified 2026-07-15 |
| **— Module 13 · Quản trị hệ thống —** | | | | | | | |
| BUG-QT-001 | Major | P1 | Data | TC-CRUD-027 | `UC99 (ERR-SYS-02, BR-EC-01)` | Optimistic lock hoạt động NHƯNG hiển thị 2 toast lỗi tương tranh trùng lặp | Closed-verified 2026-07-16 — re-test: chỉ còn 1 toast (đo peak=1) cả optimistic-lock lẫn đợt trùng kỳ (trước đó Open 07-15) |
| BUG-QT-002 | Medium | P2 | Negative | TC-LODN-002 | `UC105 §Inputs (tiêu chí không bắt buộc)` | Không thêm được loại DN khi chỉ nhập Mã + Tên | Reject — thêm được chỉ với Mã+Tên 2026-07-15 |
| BUG-QT-003 | Minor | P3 | Negative | DM-029 | `UC100 (ERR-DM-03)` | Xóa được loại hình hỗ trợ khi còn danh mục con | Reject — guard ERR-DM-03 chặn đúng 2026-07-15 |
| BUG-QT-004 | Minor | P3 | Negative | DM-038 | `UC116 (ERR-DM-03)` | Xóa được loại tiếp nhận khi còn danh mục con | Reject — guard ERR-DM-03 chặn đúng 2026-07-15 |
| BUG-QT-005 | Minor | P3 | Negative | DM-047 | `UC117 (ERR-DM-03)` | Xóa được kênh tiếp nhận khi còn danh mục con | Reject — guard ERR-DM-03 chặn đúng 2026-07-15 |
| BUG-QT-006 | Minor | P3 | UI/UX | TC-TK-213 | `UC121 (ERR-VN-03, feature flag Tier 2)` | Nút "Đăng nhập VNeID" vẫn hiện dù Tier 2 chưa tích hợp | Reject — /login không có nút VNeID 2026-07-15 |
| **— Module 14 · Báo cáo thống kê —** | | | | | | | |
| BUG-BC-001 | Medium | P2 | Edge | TC-BC-REP-023 | `UC124 (ERR-RPT-03)` | Không báo đúng khi truy vấn báo cáo quá 30 giây | Re-verify blocked 2026-07-15 — thiếu timeout fixture UI |
| **— Module 18 · Chương trình HTPLDN —** | | | | | | | |
| BUG-CT-BC-001 | Major | P1 | Permission | TC-TPD-012 | `FR-XI-06 (srs-fr-15:620,711,715-717)` · `FR-XI-07 (srs-fr-15:828)` | Đơn vị nộp ∈ phạm vi đợt bị 403 khi mở chi tiết đợt → không lập/trình được BC | Closed-verified 2026-07-15 |
| BUG-CT-BC-002 | Minor | P3 | Negative | TC-TPD-013 | `FR-XI-07 (srs-fr-15:824 ERR-XI-07-01)` | Trình được BC toàn số 0 / để trống — không chặn "BC chưa hoàn chỉnh" | BA confirm 2026-07-15 — SRS có ERR-XI-07-01 nhưng không định nghĩa "hoàn chỉnh" |
| BUG-CT-BC-003 | Minor | P3 | Workflow | TC-TPD-014 | `FR-XI-07 (SM-DOT-BC, srs-fr-15:788)` | Không kiểm được chặn trình PD khi đợt sai trạng thái (chặn bởi BUG-CT-BC-001) | Closed-verified 2026-07-15 |
| BUG-CT-BC-004 | Minor | P3 | Permission | TC-TPD-015 | `FR-XI-07 §Processing (BR-AUTH-01, srs-fr-15:800)` | Không kiểm được phân quyền trình PD (chặn bởi BUG-CT-BC-001) | Closed-verified 2026-07-15 |
| BUG-CT-BC-005 | Minor | P3 | Workflow | TC-TPD-016 | `FR-XI-07 §Postconditions (srs-fr-15:818)` | Không kiểm được thông báo CB PD sau khi trình (chặn bởi BUG-CT-BC-001) | Closed-verified 2026-07-15 |

> **Type:** Happy / Negative / Edge / Workflow / Permission / Data / UI/UX · **Severity:** Critical / Major / Medium / Minor / Trivial · **Priority:** P0…P4

---

## ▉ MODULE 03 — HỎI ĐÁP PHÁP LÝ

## BUG-HD-001 — Upload file 0 byte không bị chặn

### Mô tả

Khi upload tệp đính kèm rỗng (0 byte) ở chức năng Hỏi đáp, hệ thống **không chặn** — không hiển thị thông báo từ chối tệp không hợp lệ.

### Các bước tái hiện

1. Đăng nhập role **CB_NV_TW** (`cb_nv_tw_01`).
2. Vào chức năng Hỏi đáp (UC10), thao tác đính kèm tệp.
3. Chọn 1 file `.pdf` **0 byte** (rỗng).
4. Quan sát phản hồi hệ thống sau khi chọn file.

### Kết quả mong đợi

- Hệ thống từ chối tệp rỗng và hiển thị thông báo: **"Tệp '{name}' trống, không hợp lệ"**.

### Kết quả thực tế

- Hệ thống **không chặn** tệp 0 byte, không hiển thị thông báo từ chối.

### Bằng chứng

![BUG-HD-001 — file 0 byte được chấp nhận, không có thông báo từ chối](image/bug-hd-001-0byte-accepted.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP)

- **Cách verify:** UI-only bằng Chrome DevTools MCP, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234`, OTP MailHog.
- **Bước thực tế:** **Hỏi đáp pháp lý → Thêm mới → File đính kèm** → upload `empty-0byte.pdf` (0 byte). Cài `MutationObserver` trước khi upload.
- **Kết quả:** UI chấp nhận file, hiển thị `empty-0byte.pdf` trong upload list với action **Xem/Xóa** (class không có `error`). Observer + DOM: **không** có toast/message từ chối; `.ant-message` rỗng; không có spinner ClamAV báo lỗi. Vùng upload chỉ ghi rule dung lượng tối đa 20MB, không chặn min-size.
- **Đối chiếu SRS (Cổng 3):** `srs-fr-02-hoi-dap.md:107` ("**Reject file 0 byte**") + `:1069` (SCR-II-01 §File đính kèm: "file 0 byte → **từ chối + toast \"Tệp '{name}' trống, không hợp lệ\"**"). App KHÔNG chặn → sai rule.
- **Verdict:** `Open — Reproduced UI 2026-07-15` → **Re-test 2026-07-16 (Chrome DevTools MCP, UI): ✅ `Closed-verified 2026-07-16`.** Upload file `.pdf` 0 byte → hệ thống **từ chối**, toast *"Tệp '{name}' trống, không hợp lệ"* (đúng SRS `:1069`), file không vào danh sách. Ảnh: `verify-2026-07-16/image/HD-001-reject-0byte.png`.

---

## BUG-HD-002 — Empty state tab "Hoàn thành" không hiển thị khi chưa có hỏi đáp đã xử lý

### Mô tả

Với đơn vị mới setup (chưa có hỏi đáp nào ở trạng thái Hoàn thành), tab "Hoàn thành" **không hiển thị đúng trạng thái rỗng** theo chuẩn.

### Các bước tái hiện

1. Đăng nhập role **CB_NV_DP** (`cb_nv_dp_01`, Sở Tư pháp mới setup — 0 HD ở trạng thái HOAN_THANH).
2. Vào màn hình Hỏi đáp → mở **tab "Hoàn thành"**.
3. Quan sát vùng danh sách khi không có dữ liệu.

### Kết quả mong đợi

- Hiển thị empty state với thông báo: **"Chưa có hỏi đáp nào đã xử lý"** (INF-DAXL-01).

### Kết quả thực tế

- Không hiển thị đúng trạng thái rỗng khi chưa có hỏi đáp đã xử lý.

### Bằng chứng

![BUG-HD-002 — empty state tab Hoàn thành hiển thị "Chưa có hỏi đáp nào đã xử lý"](image/bug-hd-002-empty-state-hoanthanh.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP)

- **Cách verify:** UI-only bằng Chrome DevTools MCP, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_dp` / `Test@1234` (CB_NV_DP, Sở Tư pháp An Giang — 0 HD HOAN_THANH), OTP MailHog.
- **Bước thực tế:** **Hỏi đáp pháp lý** → tab **Hoàn thành** (`/hoi-dap?tab=HOAN_THANH&page=1`) → 0 kết quả. Empty state (đọc `.ant-empty-description`): **"Chưa có hỏi đáp nào đã xử lý"**.
- **Đối chiếu SRS (Cổng 3):** Message khớp expected bug **INF-DAXL-01 "Chưa có hỏi đáp nào đã xử lý"**. App **đúng**.
- **Verdict:** `Closed-verified 2026-07-15`. Empty state tab Hoàn thành hiển thị đúng message.

---

## ▉ MODULE 04 — ĐÀO TẠO TẬP HUẤN

## BUG-DT-001 — Hủy Kế hoạch (Dự thảo) không chuyển trạng thái "Đã hủy"

### Mô tả

Hủy một Kế hoạch đào tạo đang ở trạng thái Dự thảo (chưa có học viên đăng ký) **không chuyển đúng** sang trạng thái Đã hủy (`DA_HUY`).

### Các bước tái hiện

1. Đăng nhập role **CB_NV_TW**. Chuẩn bị 1 Kế hoạch ở trạng thái `DU_THAO`, 0 đăng ký học viên.
2. Trên thanh hành động của Kế hoạch → click **[Hủy]**.
3. Modal nhập lý do → nhập `"Thay đổi kế hoạch đào tạo do điều chỉnh ngân sách"`.
4. Xác nhận. Quan sát trạng thái Kế hoạch + badge sau khi hủy.

### Kết quả mong đợi

- Trạng thái chuyển `DU_THAO → DA_HUY` (đúng enum `DA_HUY` theo SRS `srs-fr-03:2011`, **không phải** "HUY"); lưu `ly_do_huy`, ghi nhật ký.
- UI hiển thị badge **"Đã hủy"**. (Hủy khác Xóa — Xóa là xóa cứng.)

### Kết quả thực tế

- Hủy Kế hoạch (Dự thảo) **không chuyển đúng** trạng thái Đã hủy.

### Bằng chứng

![BUG-DT-001 — KH Nháp chỉ có Chỉnh sửa/Xoá/Trình duyệt, không có Hủy; máy trạng thái không có DA_HUY](image/bug-dt-001-kh-nhap-no-huy.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP — đổi verdict)

- **Cách verify:** UI-only bằng Chrome DevTools MCP, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234`, OTP MailHog.
- **Bước thực tế:** **Đào tạo, tập huấn → Kế hoạch đào tạo**, mở `KH-20260714-0001` (Nháp, 0 học viên). Action bar: **Chỉnh sửa · Xoá · Trình duyệt**. Stepper 4 mốc: Nháp → Chờ duyệt → Đã duyệt → Đã công khai. Không có action **Hủy** và không có mốc **Đã hủy**.
- **Đối chiếu SRS (Cổng 3) — phát hiện mis-citation:** Máy trạng thái **Kế hoạch đào tạo** là `SM-KH-DAO-TAO` (`srs-fr-03-dao-tao.md:2016+`, "[v3.5 — Thay đổi 1 — máy trạng thái mới]") chỉ có **5 trạng thái NHAP · CHO_DUYET · TU_CHOI · DA_DUYET · DA_CONG_KHAI — KHÔNG có DA_HUY, KHÔNG có transition Hủy**. Dòng `srs-fr-03:2011` (`DA_CONG_KHAI → DA_HUY : CB PD hủy`) mà bug trích thuộc máy trạng thái **Khóa học** (9 trạng thái), còn `:2060` thuộc **Chương trình đào tạo** — khác entity với Kế hoạch. ⇒ App **đúng spec** khi không có [Hủy] cho Kế hoạch; bản nháp được loại bỏ bằng **Xoá**.
- **Verdict:** `Reject — không tái hiện 2026-07-15`. App khớp máy trạng thái Kế hoạch (`SM-KH-DAO-TAO`, srs-fr-03:2016+) — entity này **không có** trạng thái/transition Hủy→DA_HUY, bản nháp loại bỏ bằng **Xoá**. Expected của bug (Kế hoạch DU_THAO → DA_HUY) trích nhầm máy trạng thái **Khóa học** (srs-fr-03:2011) — khác entity → claim là lỗi phái sinh từ mis-citation, không tái hiện. App không sai spec. (Nếu nghiệp vụ muốn Kế hoạch có "Hủy" riêng → đề xuất **tính năng mới** cho BA, không phải lỗi build hiện tại.)

---

## BUG-DT-002 — Không xuất được DOCX cho Chương trình đào tạo đã duyệt

### Mô tả

Chương trình đào tạo (CTĐT) ở trạng thái đã duyệt (`DA_DUYET`) **không xuất được file DOCX** — chức năng Xuất DOCX không trả file tải về.

### Các bước tái hiện

1. Đăng nhập role **CB_NV_TW** (`cb_nv_tw_01`). Chuẩn bị CTĐT ở trạng thái `DA_DUYET` (vd `CTDT-TW-2026-001`).
2. Mở chi tiết CTĐT.
3. Click **[Xuất ký số] → [Xuất DOCX]**.
4. Quan sát loading và kiểm tra file tải về.

### Kết quả mong đợi

- Theo SRS **FR-III-20 (srs-fr-03:1366-1386)**: từ chi tiết CTĐT đã duyệt → chọn Xuất DOCX → hệ thống sinh file từ template và trả file tải về; file mở được, nội dung CTĐT đầy đủ.

### Kết quả thực tế

- **Không xuất được DOCX** cho chương trình đào tạo đã duyệt.

### Bằng chứng

![BUG-DT-002 — CTĐT Đã duyệt không có action Xuất DOCX/PDF, chỉ có Quay lại danh sách + Tạo khóa học](image/bug-dt-002-ctdt-daduyet-no-export.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP)

- **Cách verify:** UI-only bằng Chrome DevTools MCP, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234` (CB_NV_TW = tác nhân hợp lệ), OTP MailHog.
- **Bước thực tế:** **Đào tạo, tập huấn → Chương trình đào tạo**, mở `CTDT-SEED-0001` trạng thái **Đã duyệt** (DA_DUYET). Enumerate toàn bộ button/link trên trang bằng `evaluate_script`: chỉ có `Quay lại danh sách`, `Tạo khóa học` + link Xem/Sửa khóa con. **Không** có bất kỳ action `Xuất docx` / `Xuất PDF` / `Xuất ký số` nào (`exportRelated: []`).
- **Đối chiếu SRS (Cổng 3):** `srs-fr-03-dao-tao.md:1363` **FR-III-20 "Xuất file docx/PDF ký số cho CTDT"** — Precondition "CTDT ở DA_DUYET/DA_CONG_KHAI/HOAN_THANH", AC "Given CB NV chọn CTDT **đã duyệt** When nhấn **'Xuất docx'** Then tạo file docx đầy đủ". App thiếu hẳn chức năng này ⇒ sai spec.
- **Verdict:** `Open — Reproduced UI 2026-07-15` → **Re-test 2026-07-16 (Chrome DevTools MCP, UI+network): ✅ `Closed-verified 2026-07-16`.** Màn chi tiết CTĐT đã duyệt **đã có nút "Xuất DOCX"**; click → `POST /api/v1/chuong-trinh-dao-taos/{id}/export-doc` **200**, trả file `ctdt-CTDT-SEED-0001.docx` (đúng MIME DOCX, 1926 bytes). FR-III-20 đã build. Ảnh: `verify-2026-07-16/image/DT-002-xuat-docx-button.png`.

---

## ▉ MODULE 08 — VỤ VIỆC HTPL

## BUG-VV-001 — Sắp xếp danh sách vụ việc theo "Ngày tiếp nhận" không đúng

### Mô tả

Sắp xếp danh sách vụ việc theo cột "Ngày tiếp nhận" (DESC/ASC) **không cho kết quả đúng thứ tự**.

### Các bước tái hiện

1. Đăng nhập role **CB_NV_TW** (`cb_nv_tw_01`). Có ≥10 vụ việc trong danh sách.
2. Click tiêu đề cột **"Ngày tiếp nhận"** (lần 1).
3. Click tiêu đề cột **"Ngày tiếp nhận"** (lần 2).
4. Quan sát thứ tự các dòng + biểu tượng sort.

### Kết quả mong đợi

- Mặc định danh sách sort `updated_at DESC` (srs-fr-05:1690). Click lần 1 → sort theo ngày tiếp nhận **DESC** (biểu tượng ▼). Click lần 2 → **ASC** (biểu tượng ▲).

### Kết quả thực tế

- Sắp xếp danh sách vụ việc theo ngày tiếp nhận **không đúng**.

### Bằng chứng

![BUG-VV-001 — DESC: dòng ngày tiếp nhận rỗng (—) VV-BTP-TW-20260712-002 đứng đầu trước 12/07/2026](image/bug-vv-001-desc-null-date-first.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP — đổi verdict)

- **Cách verify:** UI-only bằng Chrome DevTools MCP, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234`, OTP MailHog.
- **Bước thực tế:** **Vụ việc HTPL → /vu-viec/danh-sach**, xóa bộ lọc ngày (để hiện cả bản ghi ngày rỗng), sort cột **Ngày tiếp nhận**. Đọc thứ tự thực tế từ DOM.
  - **DESC (17 bản ghi):** `—` (VV-BTP-TW-20260712-002) → 12/07 (×8) → 01/04 → 01/03 → 01/03 → 01/02 → 01/02 → 15/01/2026 → 01/06/2024 → 01/03/2024. **Các dòng CÓ ngày sắp đúng DESC**; chỉ dòng **ngày rỗng đứng đầu** (NULLS FIRST).
  - **ASC:** ngày cũ nhất (01/03/2024) lên đầu, dòng `—` xuống **cuối** (NULLS LAST). Các dòng có ngày sắp đúng ASC.
- **Đối chiếu SRS (Cổng 3):** `srs-fr-05-vu-viec.md:1647` chỉ quy định "Sắp xếp mặc định: ngày cập nhật DESC. Hỗ trợ sort theo từng cột" — **KHÔNG** quy định thứ tự cho giá trị NULL. Ngoài ra `:1690` (form dòng 30) quy định `ngay_tiep_nhan` **Bắt buộc, mặc định ngày hiện tại** ⇒ bản ghi ngày rỗng `VV-BTP-TW-20260712-002` (trạng thái "Đã tiếp nhận") là **dữ liệu bất thường** so với spec.
- **Verdict:** `Reject — claim sort không tái hiện 2026-07-15`. Cơ chế sort cột "Ngày tiếp nhận" hoạt động **đúng** cho mọi bản ghi có ngày (DESC + ASC đều đơn điệu) → claim "sort không đúng" **không tái hiện**. **Bug mới phát sinh cần Dev (KHÔNG phải lỗi sort):** tồn tại VV "Đã tiếp nhận" có ngày tiếp nhận **rỗng** dù field bắt buộc (srs-fr-05:1690); dòng rỗng nổi đầu khi DESC (NULLS FIRST) gây hiểu nhầm "mới nhất". → Dev BE: siết validation bắt buộc ngày khi tiếp nhận; Dev FE: NULLS LAST cả 2 chiều. (Đã tách ra mục "Bug mới phát sinh".)

---

## BUG-VV-002 — Empty state khi lọc vụ việc ra 0 kết quả không hiển thị đúng

### Mô tả

Khi áp bộ lọc (không nhập từ khóa) cho ra 0 vụ việc, màn hình **không hiển thị đúng trạng thái rỗng** theo chuẩn.

### Các bước tái hiện

1. Đăng nhập role **CB_NV_TW** (`cb_nv_tw_01`).
2. Áp bộ lọc: trạng thái `TU_CHOI` + Lĩnh vực không có vụ việc nào (để trống ô từ khóa).
3. Click **[Tìm]**.
4. Quan sát vùng danh sách khi kết quả rỗng.

### Kết quả mong đợi

- Hiển thị empty state với icon thư mục trống + thông báo **"Không có vụ việc nào trong phạm vi quản lý"** (srs-fr-05:1605).

### Kết quả thực tế

- Không hiển thị đúng trạng thái rỗng khi lọc vụ việc ra 0 kết quả.

### Bằng chứng

![BUG-VV-002 — empty state tab Từ chối: icon Trống + "Không tìm thấy hồ sơ phù hợp" (đúng INF-VV-01)](image/bug-vv-002-tuchoi-empty-state.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP — đổi verdict)

- **Cách verify:** UI-only bằng Chrome DevTools MCP, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234`, OTP MailHog.
- **Bước thực tế:** **Vụ việc HTPL → /vu-viec/danh-sach**, tab **Từ chối** (`tab=TU_CHOI`) → 0 kết quả. Empty state hiển thị: **icon "Trống" + "Không tìm thấy hồ sơ phù hợp"** (đọc từ `.ant-empty`).
- **Đối chiếu SRS (Cổng 3) — có 2 biến thể empty state:**
  - `srs-fr-05:144` **INF-VV-01 "Không tìm thấy hồ sơ phù hợp"** → khi **tìm kiếm/bộ lọc ra 0 kết quả**. ⇐ đúng kịch bản bug (lọc tab TU_CHOI = 0).
  - `srs-fr-05:1563` **"Không có vụ việc nào trong phạm vi quản lý"** → khi cán bộ **không có VV nào trong phạm vi** (không data toàn bộ), không phải khi lọc ra 0.
  - ⇒ App hiển thị **đúng** biến thể INF-VV-01 cho kịch bản lọc-ra-0. Expected của bug (`phạm vi quản lý`) trích **nhầm biến thể** dùng cho điều kiện khác.
- **Verdict:** `Reject — không tái hiện 2026-07-15`. App **khớp SRS**: filter/tab ra 0 → "Không tìm thấy hồ sơ phù hợp" (INF-VV-01, srs-fr-05:144). Expected đối tác trích nhầm biến thể "no-data-in-scope" (srs-fr-05:1563) — khác kịch bản → claim "empty state không đúng" không tái hiện. App không sai. (Nếu đối tác muốn đổi text riêng cho tab lọc-ra-0 → đề xuất chỉnh copy cho BA, không phải lỗi.)

---

## ▉ MODULE 10 — QUẢN LÝ DOANH NGHIỆP

## BUG-DN-001 — Không xóa mềm được Doanh nghiệp không có vụ việc

### Mô tả

Xóa một Doanh nghiệp **không có vụ việc liên kết** không thực hiện được (không xóa mềm được).

### Các bước tái hiện

1. Đăng nhập role **CB_NV_TW** (`cb_nv_tw_01`). Chuẩn bị 1 DN không có vụ việc liên kết (vd `DN-TW-099`).
2. Trên dòng DN → click **icon Xóa**.
3. Xác nhận trên modal **"Bạn có chắc chắn muốn xóa DN '{tên}'?"**.
4. Quan sát toast + danh sách sau xác nhận.

### Kết quả mong đợi

- Sau xác nhận → toast **"Xóa thành công"**; danh sách reload, DN biến mất; bản ghi được đánh dấu xóa mềm `is_deleted=1` (BR-DATA-01); ghi nhật ký hành động Xóa.

### Kết quả thực tế

- **Không xóa mềm được** Doanh nghiệp không có vụ việc.

### Bằng chứng

![BUG-DN-001 — sau khi xóa DN-XX-0001 (TW-owned, 0 VV): danh sách còn 4, bản ghi biến mất](image/bug-dn-001-softdelete-works.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP — đổi verdict)

- **Cách verify:** UI-only bằng Chrome DevTools MCP + MutationObserver bắt toast, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234` (CB_NV_TW/TW), OTP MailHog.
- **Phát hiện lỗi test-data của lần trước:** Xóa `DN-HNI-0002` (Công ty Linh, thuộc **Sở Tư pháp Hà Nội**) → toast **"Bạn không có quyền truy cập dữ liệu của đơn vị khác."** — đây là **chặn phân quyền cross-tenant** (cbnv_tw = TW ≠ đơn vị Hà Nội), KHÔNG phải soft-delete hỏng. Verdict "Open" cũ **chẩn đoán nhầm** vì test bằng DN của đơn vị khác.
- **Seed đúng tiền đề (§Nguyên tắc 4):** Tạo mới DN TW-owned `DN-XX-0001` / `QA Verify DN001 soft-delete 715` (Số lần hỗ trợ = 0) — toast "Thêm doanh nghiệp thành công".
- **Verify soft-delete đúng scope:** Xóa `DN-XX-0001` → confirm "Xóa doanh nghiệp?" → toast **"Đã xóa doanh nghiệp"** (1 toast, không double); bản ghi biến mất khỏi danh sách (5 → 4 kết quả).
- **Đối chiếu SRS (Cổng 3):** `srs-fr-07` UC81 §Xóa (BR-DATA-01) — DN không có vụ việc được soft-delete. App thực hiện **đúng** khi test bằng DN trong phạm vi.
- **Verdict:** `Closed-verified 2026-07-15`. Soft-delete DN (0 vụ việc) **hoạt động đúng** cho DN trong phạm vi. Chặn cross-tenant khi xóa DN đơn vị khác là **RBAC đúng** (không phải bug). Lưu ý phụ: mã DN mới sinh có prefix đơn vị là `DN-XX-` (xem "Bug mới phát sinh" — có thể thiếu map mã đơn vị TW).

---

## BUG-DN-002 — Không xóa mềm được hồ sơ pháp lý DN (HSPL)

### Mô tả

Xóa một hồ sơ pháp lý của Doanh nghiệp (tab Hồ sơ pháp lý) không thực hiện được (không xóa mềm được).

### Các bước tái hiện

1. Đăng nhập role **CB_NV_TW** (`cb_nv_tw_01`). Mở 1 hồ sơ pháp lý DN (vd `HSPL-20260509-002`).
2. Click **icon Xóa**.
3. Xác nhận trên modal **"Bạn có chắc chắn muốn xóa hồ sơ '{tên}'?"** (nguyên văn theo srs:593).
4. Quan sát danh sách sau xác nhận.

### Kết quả mong đợi

- Xóa thành công; bản ghi biến mất khỏi danh sách; DB đánh dấu `is_deleted=1` (BR-DATA-01); ghi nhật ký hành động Xóa.

### Kết quả thực tế

- **Không xóa mềm được** hồ sơ pháp lý Doanh nghiệp.

### Bằng chứng

- Chưa có ảnh — server down 2026-07-07, chưa re-verify UI. Ghi nhận từ `report-dot-3.xlsx` (sheet "10. Quản lý doanh nghiệp", TC-HSPL-201). Cần chụp ảnh UI khi server up.

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP)

- **Cách verify:** UI-only bằng Chrome DevTools MCP + MutationObserver, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234`, OTP MailHog.
- **Seed đúng tiền đề (§Nguyên tắc 4):** tab HSPL của `DN-SEED-0001` đang rỗng (HSPL cũ đã xóa) → tạo mới `HSPL-20260715-0002` / "QA Verify HSPL soft-delete 715" (Loại: Giấy phép) — toast "Thêm hồ sơ thành công".
- **Verify soft-delete:** Xóa `HSPL-20260715-0002` → confirm "Xoá hồ sơ này?" → toast **"Đã xoá hồ sơ"** (1 toast, không double); bản ghi biến mất, bảng về **Trống**.
- **Đối chiếu SRS (Cổng 3):** `srs:593` UC150 §Xóa HSPL (BR-DATA-01) — HSPL soft-delete được. App **đúng**.
- **Verdict:** `Closed-verified 2026-07-15`. Soft-delete HSPL hoạt động đúng. Lưu ý phụ: dropdown "Loại hồ sơ" hiển thị lẫn **mã enum thô** `GIAY_PHEP` / `HOP_DONG` cạnh nhãn tiếng Việt (xem "Bug mới phát sinh").

---

## BUG-DN-003 — Truy cập chéo đơn vị bị 403 nhưng không ghi nhật ký kiểm toán

### Mô tả

Khi một cán bộ cố sửa DN thuộc đơn vị khác (cross-tenant), hệ thống chặn `403` đúng, **nhưng không ghi bản ghi audit** cho lần truy cập bị từ chối.

### Các bước tái hiện

1. Đăng nhập role **CB_NV_DP** đơn vị Hà Nội (`cb_nv_dp_HN_01`).
2. Cố mở/sửa 1 DN thuộc đơn vị khác (vd `DN-HP-001` — Hải Phòng).
3. Quan sát: hệ thống chặn `403`.
4. Kiểm tra nhật ký kiểm toán (AUDIT_LOG) cho hành động vừa rồi.

### Kết quả mong đợi

- Ngoài việc chặn `403`, hệ thống ghi 1 bản ghi audit cho lần truy cập bị từ chối (hành động kiểu `UPDATE_ATTEMPT_DENIED` hoặc tương đương), kèm `user_id` + IP (BR-DATA-05).

### Kết quả thực tế

- Truy cập chéo đơn vị bị chặn (403) **nhưng không ghi nhật ký kiểm toán**.

> **Lưu ý spec:** hành vi "ghi audit cho request bị từ chối" cần **BA xác nhận** (SPEC-CLARIFY-DN-21) — nếu SRS không định nghĩa rõ hành vi log denied thì đây là điểm cần chốt spec trước khi kết luận bug.

### Bằng chứng

![BUG-DN-003 — Nhật ký hệ thống quanh 16:49: chỉ event TAI_KHOAN của cbnv_dp, không có bản ghi denied-access DOANH_NGHIEP](image/bug-dn-003-audit-log-no-denied.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP — đổi verdict)

- **Cách verify:** UI-only bằng Chrome DevTools MCP; không verify qua API (chỉ đọc network status để xác nhận mã chặn).
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản thao tác:** `cbnv_dp` / `Test@1234` (Sở Tư pháp An Giang). **Tài khoản kiểm audit:** `admin` / `Secret@123`. OTP MailHog.
- **Bước 1 — chặn quyền (verify bằng đúng role ĐP):** `cbnv_dp` mở trực tiếp URL DN Hà Nội `DN-HNI-0001` (`/doanh-nghiep/829abcac-...`) lúc **16:49:30**. UI hiển thị **"Không tìm thấy doanh nghiệp."**; BE trả **404** cho `GET /api/v1/doanh-nghieps/829abcac-...`. ⇒ Chặn cross-tenant **đúng RBAC**.
- **Bước 2 — kiểm audit (admin, chỉ điều tra):** **Quản trị hệ thống → Nhật ký hệ thống** (`?tuNgay=2026-07-15&denNgay=2026-07-15`, 217 bản ghi). Quanh 16:47→16:49:47 chỉ có event `TAI_KHOAN` (đăng nhập/OTP/đăng xuất) của `cbnv_dp` — **không** có bản ghi `DOANH_NGHIEP` hay event denied-access. (Audit log CÓ ghi các thao tác thành công: `DOT_BAO_CAO` Tạo mới 16:45, `BIEU_MAU` Cập nhật 16:39, `HO_SO_PHAP_LY_DN` Xóa 16:36.)
- **Đối chiếu SRS (Cổng 3):** `BR-DATA-05` (srs-fr-13:854) — "Mọi thao tác **CUD + phê duyệt + đăng nhập/xuất** đều ghi vào AUDIT_LOG". **KHÔNG** yêu cầu ghi audit cho **request bị từ chối** (read/update bị chặn 404). App ghi audit đúng phạm vi BR-DATA-05.
- **Verdict:** `BA confirm 2026-07-15`. Chặn cross-tenant đúng RBAC; audit log ghi đúng CUD/phê duyệt/login theo BR-DATA-05 nhưng **không** ghi denied-access — điều BR-DATA-05 **không quy định**. **Câu hỏi BA (SPEC-CLARIFY-DN-21):** có mở rộng BR-DATA-05 để ghi audit cho request cross-tenant bị từ chối (UPDATE/READ_ATTEMPT_DENIED + user_id + IP) không? Không auto-Open vì SRS chưa yêu cầu.

### So sánh (Comparison)

| Hành động | Kết quả chặn quyền | Ghi AUDIT_LOG | Theo BR-DATA-05? |
|---|:--:|:--:|:--:|
| Cross-tenant read (CB ĐP An Giang mở DN Hà Nội) | ✅ 404 (đúng RBAC) | ❌ Không ghi denied | ✅ Đúng — BR-DATA-05 chỉ ghi CUD/duyệt/login, không ghi denied |
| Denied-access audit (kỳ vọng đối tác) | — | ❌ Không có | ⚠️ Ngoài phạm vi BR-DATA-05 → BA chốt SPEC-CLARIFY-DN-21 |

---

## ▉ MODULE 12 — BIỂU MẪU

## BUG-BM-001 — Công khai được biểu mẫu khi thư mục cha đang ẩn

### Mô tả

Hệ thống **cho phép công khai** một biểu mẫu dù thư mục cha của nó đang ở trạng thái ẩn — đáng lẽ phải chặn.

### Các bước tái hiện

1. Đăng nhập role **CB Nghiệp vụ**. Chuẩn bị: thư mục cha đang **ẨN** (chưa công khai), bên trong có 1 biểu mẫu đã đính kèm file.
2. Mở biểu mẫu nằm trong thư mục ẩn đó.
3. Click **[Công khai]**.
4. Quan sát phản hồi hệ thống.

### Kết quả mong đợi

- Hệ thống chặn và báo lỗi **ERR-CK-BM-02**: "Thư mục cha đang ẩn. Vui lòng công khai thư mục trước (UC94)".

### Kết quả thực tế

- **Vẫn công khai được** biểu mẫu khi thư mục cha đang ẩn (đáng lẽ phải chặn).

### Bằng chứng

![BUG-BM-001 — form vẫn ở trang Chỉnh sửa sau khi bấm Lưu = save bị chặn (toast ERR-CK-BM-02 bắt qua observer)](image/bug-bm-001-block-toast.png)

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP)

- **Cách verify:** UI-only bằng Chrome DevTools MCP + MutationObserver, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234`, OTP MailHog.
- **Tiền đề (đã seed sẵn từ round trước):** thư mục `QA Hidden Folder 715` trạng thái **Nháp** (chưa công khai) chứa biểu mẫu `BM-20260715-001` / `QA BM001 Hidden Parent 715` (Nháp, Chưa công khai).
- **Bước verify:** biểu mẫu **không có action Công khai trực tiếp** (chỉ Tải về/Sửa/Xóa) → dùng publish path: **Sửa** → bật switch **"Công khai trên Cổng PLQG"** (`aria-checked=true`) → **Lưu**.
- **Kết quả:** UI **chặn lưu**, toast (bắt bằng observer): **"Thư mục cha đang ẩn. Vui lòng công khai thư mục trước (UC94)"** = đúng **ERR-CK-BM-02**. Số wrapper `.ant-message-notice-wrapper` = **1** (không double toast). Biểu mẫu vẫn Chưa công khai.
- **Đối chiếu SRS (Cổng 3):** `srs-fr-09` UC97/UC94 (ERR-CK-BM-02) — chặn công khai biểu mẫu khi thư mục cha đang ẩn. App **đúng**.
- **Verdict:** `Closed-verified 2026-07-15`. Rule chặn công khai khi thư mục cha ẩn hoạt động đúng, thông báo đúng ERR-CK-BM-02, 1 toast.

---

## ▉ MODULE 13 — QUẢN TRỊ HỆ THỐNG

## BUG-QT-001 — Hiển thị 2 toast lỗi tương tranh trùng lặp khi xóa bản ghi vừa bị người khác sửa

### Mô tả

Khi User A xóa một bản ghi danh mục mà bản ghi đó vừa bị User B cập nhật (thay đổi phiên bản), hệ thống **có** chặn thao tác và **có** báo lỗi tương tranh — nhưng **hiển thị 2 toast lỗi giống hệt nhau cùng lúc** cho cùng 1 thao tác. Đáng lẽ chỉ hiển thị 1 thông báo. (Claim gốc "không báo lỗi tương tranh" KHÔNG tái hiện — optimistic lock hoạt động đúng; vấn đề thực tế là toast trùng lặp.)

### Các bước tái hiện

1. User A mở trang danh sách danh mục (đọc `updated_at = T1`).
2. User B sửa cùng bản ghi (mã `LOCK_DEL`) → `updated_at = T2`.
3. User A click **[Xóa]** trên bản ghi `LOCK_DEL` (client vẫn giữ `updated_at = T1`).
4. Quan sát phản hồi hệ thống.

### Kết quả mong đợi

- Hệ thống phát hiện bản ghi đã bị thay đổi, chặn thao tác xóa và hiển thị **đúng 1 (một)** thông báo lỗi tương tranh (theo tinh thần **ERR-SYS-02 / BR-EC-01**: báo bản ghi đã bị người khác thay đổi, yêu cầu tải lại).

### Kết quả thực tế

- Optimistic lock **hoạt động** (chặn xóa bản ghi stale) nhưng hệ thống **hiển thị 2 toast lỗi giống hệt nhau cùng lúc** — cùng text "Bản ghi đã được người khác cập nhật trong lúc bạn thao tác." Đo được **2 phần tử `.ant-message-notice` đồng thời** cho 1 thao tác.

### Bằng chứng

- ![Double toast lỗi tương tranh](image/bug-qt-001-double-concurrency-toast.png) — 2 toast lỗi trùng lặp `[Toast #1]` + `[Toast #2]` cùng nội dung "Bản ghi đã được người khác cập nhật trong lúc bạn thao tác." (freeze bằng clone, chụp cùng khung hình).

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, 2 tab UI (2 `new_page` cùng phiên admin), KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `admin` / `Secret@123`, OTP từ MailHog.
- **Kịch bản:** Tab A (Page A) tạo `QALOCKX` và giữ nguyên state (không reload) → phiên bản V1. Tab B (Page B) mở cùng danh mục, sửa tên `QALOCKX` → phiên bản V2. Quay lại Tab A stale (vẫn hiển thị tên cũ "QA Lock X original") → bấm **Xóa** `QALOCKX` → confirm.
- **Kết quả đo (observer + tight-poll 25–40ms):**
  1. Thao tác bị **chặn** (QALOCKX không bị xóa) → optimistic lock hoạt động.
  2. `max đồng thời .ant-message-notice = 2`; `container .ant-message` chứa **2 khối `.ant-message-notice ant-message-notice-error`** cùng text → **double toast xác nhận**.
  3. Text lỗi: "Bản ghi đã được người khác cập nhật trong lúc bạn thao tác." (khác câu chữ expected `ERR-SYS-02` "…Vui lòng tải lại trang" nhưng cùng ý nghĩa nghiệp vụ).
- **SRS đối chiếu:** `UC99` / `BR-EC-01` — optimistic lock khi chỉnh sửa/xóa đồng thời phải báo lỗi tương tranh.
- **Verdict:** `Open — double toast tương tranh confirmed` → **Re-test 2026-07-16 (Chrome DevTools MCP, UI+network): ✅ `Closed-verified 2026-07-16`.** Đo `.ant-message-notice` đồng thời qua MutationObserver: xóa danh mục optimistic-lock (`DELETE` → 409 `ERR-STATE-LOCK-409`) và tạo đợt trùng kỳ (`POST /dot-bao-caos` → 409 `ERR-VAL-XI-5a-02`) đều chỉ **1 toast** (peak=1), không còn double toast.
- **Đã dọn dẹp:** xóa `QALOCKX` sau khi verify; danh mục Loại DN về đúng 4 record gốc (TNHH/CP/DNTN/HKD).

---

## BUG-QT-002 — Không thêm được loại DN khi chỉ nhập Mã + Tên (bỏ trống tiêu chí)

### Mô tả

Khi thêm mới bản ghi danh mục loại DN mà chỉ nhập Mã + Tên (bỏ trống 2 trường tiêu chí không bắt buộc), hệ thống **không lưu được**.

### Các bước tái hiện

1. Đăng nhập role **QTHT** (quản trị hệ thống).
2. Mở danh mục Loại DN → click **[+ Thêm mới]**.
3. Chỉ điền **Mã** = "VUA", **Tên** = "Vừa"; bỏ trống `tieu_chi_doanh_thu` và `tieu_chi_lao_dong`.
4. Click **[Lưu]**.

### Kết quả mong đợi

- Lưu thành công; cả 2 trường tiêu chí = null (không bắt buộc) — theo SRS UC105 các trường tiêu chí không bắt buộc.

### Kết quả thực tế

- **Không thêm được** bản ghi khi chỉ nhập Mã + Tên (tiêu chí để trống).

### Bằng chứng

- Kiểm chứng trực tiếp: thêm mới `QA715B` / `QA715E` / `QA715F` / `QA715G` — mỗi lần **chỉ nhập Mã + Tên**, để trống **Tiêu chí doanh thu** + **Tiêu chí lao động** → đều lưu **thành công** (notification "Thêm mới thành công", 0 validation error). Đã xóa lại toàn bộ record test sau khi verify.

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, UI-only, KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `admin` / `Secret@123`, OTP từ MailHog.
- **Kết quả:** Vào **Quản trị hệ thống → Danh mục dùng chung → Loại doanh nghiệp** (`/quan-tri/danh-muc/LOAI_DOANH_NGHIEP`) → **Thêm mới** → nhập Mã + Tên, để trống 2 trường tiêu chí → **Đồng ý** → lưu thành công, bản ghi xuất hiện trong danh sách. Form chỉ đánh dấu `*` bắt buộc ở Mã + Tên; 2 trường tiêu chí không bắt buộc — khớp SRS UC105.
- **SRS đối chiếu:** `srs-update-2026-5-5/srs-fr-10-quan-tri.md` UC105 §Inputs — tiêu chí doanh thu/lao động không bắt buộc.
- **Verdict:** `Reject — không tái hiện`. Thêm được loại DN chỉ với Mã + Tên. Claim "không thêm được" không đúng với build hiện tại. Không cần dev xử lý.
- **Double toast:** Flow thêm mới danh mục hiển thị **1 notification** "Thêm mới thành công" (góc trên phải), flow xóa hiển thị **1 message** — **không có double toast** ở các flow danh mục (đã đo `.ant-message-notice` + `.ant-notification-notice`, max đồng thời = 1).

---

## BUG-QT-003 — Xóa được danh mục "Loại hình hỗ trợ" khi còn danh mục con / đang được tham chiếu

### Mô tả

Hệ thống **cho phép xóa** một bản ghi danh mục Loại hình hỗ trợ dù nó đang được ≥1 entity tham chiếu (còn danh mục con) — đáng lẽ phải chặn.

### Các bước tái hiện

1. Đăng nhập role **QTHT**. Chuẩn bị 1 bản ghi danh mục Loại hình hỗ trợ đang được ≥1 entity tham chiếu.
2. Click **[Xóa]** tại bản ghi đang được sử dụng.
3. Xác nhận.
4. Quan sát phản hồi hệ thống.

### Kết quả mong đợi

- Hệ thống chặn và báo lỗi **ERR-DM-03**: "Không thể xóa. Danh mục đang được sử dụng bởi {N} bản ghi".

### Kết quả thực tế

- **Xóa được** danh mục loại hình hỗ trợ khi còn danh mục con (đáng lẽ phải chặn).

### Bằng chứng

- ![Chặn xóa loại hình hỗ trợ đang được tham chiếu — ERR-DM-03](image/bug-qt-003-loaihinhht-tuvan-blocked.png) — xóa `TU_VAN` (đang được vụ việc/bản ghi khác dùng) bị chặn: toast **"Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác"**, danh sách vẫn đủ 7 mục (TU_VAN không mất).

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, UI-only, KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `admin` / `Secret@123`, OTP từ MailHog.
- **Kết quả:** Vào **Quản trị hệ thống → Danh mục dùng chung → Loại hình hỗ trợ** (`/quan-tri/danh-muc/LOAI_HINH_HO_TRO`) → xóa `TU_VAN` (bản ghi lõi được nhiều vụ việc tham chiếu) → confirm → **BỊ CHẶN**: toast **"Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác"** (biến thể tham chiếu-entity của `ERR-DM-03`); `TU_VAN` vẫn còn (7/7 mục). Cũng đã kiểm chứng chiều cha–con: tạo `QA_PARENT_LHT` ← `QA_CHILD_LHT` rồi xóa cha → chặn tương tự "…bởi 1 bản ghi"; sau đó dọn dẹp toàn bộ record QA test, danh mục về đúng 6 mục gốc.
- **SRS đối chiếu:** `srs-update-2026-5-5/srs-fr-10-quan-tri.md:159` (E5 → ERR-DM-03) + AC `:168`. Hành vi thực tế **khớp SRS**.
- **Verdict:** `Reject — không tái hiện`. Guard `ERR-DM-03` chặn đúng bản ghi đang được tham chiếu. Không cần dev xử lý. (Trước đây ghi `Closed-verified` do chưa bắt được toast; nay đã bắt trực tiếp toast chặn.)
- **Double toast:** không phát hiện — chỉ **1 toast** khi bị chặn.

---

## BUG-QT-004 — Xóa được danh mục "Loại hình tiếp nhận" khi còn danh mục con / đang được tham chiếu

### Mô tả

Hệ thống **cho phép xóa** một bản ghi danh mục Loại hình tiếp nhận dù đang được tham chiếu — đáng lẽ phải chặn.

### Các bước tái hiện

1. Đăng nhập role **QTHT**. Chuẩn bị 1 bản ghi Loại hình tiếp nhận đang được tham chiếu.
2. Click **[Xóa]** → xác nhận.
3. Quan sát phản hồi hệ thống.

### Kết quả mong đợi

- Hệ thống chặn và báo lỗi **ERR-DM-03**: "Danh mục đang được sử dụng bởi {N} bản ghi".

### Kết quả thực tế

- **Xóa được** danh mục loại hình tiếp nhận khi còn danh mục con (đáng lẽ phải chặn).

### Bằng chứng

- ![Chặn xóa danh mục còn tham chiếu — ERR-DM-03](image/bug-qt-004-parent-with-child-blocked.png) — xóa `QA_PARENT_TN` (đang có danh mục con) bị chặn: toast **"Không thể xóa. Danh mục đang được sử dụng bởi 1 bản ghi"**, danh sách vẫn đủ 7 mục.

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, UI-only, KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `admin` / `Secret@123`, OTP từ MailHog.
- **Phương pháp (kiểm chứng cả 2 chiều, không phá dữ liệu dùng chung):**
  1. Xóa `TRUC_TIEP` (bản ghi **lá, không có con, không được tham chiếu**) → xóa thành công (toast "Xóa danh mục thành công", **1 toast**). ⇒ đã tạo lại ngay `TRUC_TIEP` (Mã/Tên/Thứ tự=2) để khôi phục.
  2. Tự tạo cặp cha–con QA test: `QA_PARENT_TN` ← `QA_CHILD_TN` (chọn Danh mục cha = QA_PARENT_TN).
  3. Xóa `QA_PARENT_TN` (**đang có 1 con**) → **BỊ CHẶN**: toast **"Không thể xóa. Danh mục đang được sử dụng bởi 1 bản ghi"** (đúng `ERR-DM-03`), cha + con vẫn còn nguyên (7/7 mục). Sau đó dọn dẹp: xóa con → xóa cha, danh mục về đúng 5 mục gốc.
- **SRS đối chiếu:** `srs-update-2026-5-5/srs-fr-10-quan-tri.md:159` — `E5 | Bản ghi đang được tham chiếu | ERR-DM-03 | "Không thể xóa. Danh mục đang được sử dụng bởi {N} bản ghi {entity}"`; AC `:168` — xóa danh mục đang được tham chiếu ⇒ hệ thống từ chối + cảnh báo liên kết. Hành vi thực tế **khớp SRS**.
- **Verdict:** `Reject — không tái hiện`. Guard `ERR-DM-03` chặn đúng bản ghi đang được tham chiếu. "Reproduction" trước đó nhầm: chỉ xóa được `TRUC_TIEP` vì nó là **lá không được tham chiếu** (hành vi đúng), không phải guard hỏng. Không cần dev xử lý.
- **Double toast:** không phát hiện — cả xóa thành công lẫn xóa bị chặn đều chỉ hiển thị **1 toast**.

---

## BUG-QT-005 — Xóa được danh mục "Kênh tiếp nhận" khi còn danh mục con / đang được tham chiếu

### Mô tả

Hệ thống **cho phép xóa** một bản ghi danh mục Kênh tiếp nhận dù đang được tham chiếu — đáng lẽ phải chặn.

### Các bước tái hiện

1. Đăng nhập role **QTHT**. Chuẩn bị 1 bản ghi Kênh tiếp nhận đang được tham chiếu.
2. Click **[Xóa]** → xác nhận.
3. Quan sát phản hồi hệ thống.

### Kết quả mong đợi

- Hệ thống chặn và báo lỗi **ERR-DM-03**: "Danh mục đang được sử dụng".

### Kết quả thực tế

- **Xóa được** danh mục kênh tiếp nhận khi còn danh mục con (đáng lẽ phải chặn).

### Bằng chứng

- ![Chặn xóa kênh tiếp nhận còn tham chiếu — ERR-DM-03](image/bug-qt-005-kenh-parent-with-child-blocked.png) — xóa `QA_PARENT_KTN` (đang có danh mục con) bị chặn: toast **"Không thể xóa. Danh mục đang được sử dụng bởi 1 bản ghi"**, danh sách vẫn đủ 6 mục.

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, UI-only, KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `admin` / `Secret@123`, OTP từ MailHog.
- **Phương pháp (kiểm chứng cả 2 chiều, không phá dữ liệu dùng chung):**
  1. Xóa `CONG_DVC` (bản ghi **lá, không có con, không được tham chiếu**) → xóa thành công (toast "Xóa danh mục thành công", **1 toast**). ⇒ đã tạo lại ngay `CONG_DVC` (Tên "Cổng dịch vụ công", Thứ tự 1 — đúng gốc) để khôi phục.
  2. Tự tạo cặp cha–con QA test: `QA_PARENT_KTN` ← `QA_CHILD_KTN`.
  3. Xóa `QA_PARENT_KTN` (**đang có 1 con**) → **BỊ CHẶN**: toast **"Không thể xóa. Danh mục đang được sử dụng bởi 1 bản ghi"** (đúng `ERR-DM-03`), cha + con vẫn còn (6/6 mục). Sau đó dọn dẹp: xóa con → xóa cha, danh mục về đúng 4 mục gốc.
- **SRS đối chiếu:** `srs-update-2026-5-5/srs-fr-10-quan-tri.md:159` (ERR-DM-03) + AC `:168`. Hành vi thực tế **khớp SRS** (giống hệt QT-004).
- **Verdict:** `Reject — không tái hiện`. Guard `ERR-DM-03` chặn đúng bản ghi đang được tham chiếu ở cả danh mục `KENH_TIEP_NHAN`. `CONG_DVC` xóa được vì là **lá không được tham chiếu** (đúng), không phải guard hỏng. Không cần dev xử lý.
- **Double toast:** không phát hiện — cả xóa thành công lẫn xóa bị chặn đều chỉ **1 toast**.

---

## BUG-QT-006 — Nút "Đăng nhập VNeID" vẫn hiển thị dù Tier 2 chưa tích hợp

### Mô tả

Trang đăng nhập **vẫn hiển thị nút "Đăng nhập VNeID"** dù feature flag Tier 2 đang tắt (chưa tích hợp) — đáng lẽ phải ẩn.

### Các bước tái hiện

1. Đảm bảo feature flag **Tier 2 OFF** (môi trường hiện tại).
2. Mở trang `/login`.
3. Quan sát khu vực các nút đăng nhập.

### Kết quả mong đợi

- Nút **"Đăng nhập VNeID" KHÔNG hiển thị** khi feature flag Tier 2 tắt (ERR-VN-03).

### Kết quả thực tế

- Nút "Đăng nhập VNeID" **vẫn hiện** dù chưa tích hợp (đáng lẽ phải ẩn).

### Bằng chứng

- ![Trang /login không có nút VNeID](image/bug-qt-006-login-no-vneid.png) — trang đăng nhập chỉ có Tên đăng nhập / Mật khẩu / Ghi nhớ đăng nhập / **Đăng nhập** / **Quên mật khẩu?** / **Đăng ký tài khoản doanh nghiệp**; không có VNeID.

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, UI-only, KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`.
- **Kết quả:** Logout sạch (`/api/v1/auth/logout` + clear storage) → mở `/login`. Quét DOM toàn trang: `hasVNeID = false`; danh sách button/link = `["Quên mật khẩu?","Đăng nhập","Đăng ký tài khoản doanh nghiệp"]`. Không có nút/text **Đăng nhập VNeID**.
- **Verdict:** `Reject — không tái hiện`. Trang `/login` không hiển thị nút VNeID (khớp expected khi Tier 2 tắt). Không cần dev xử lý.

---

## ▉ MODULE 14 — BÁO CÁO THỐNG KÊ

## BUG-BC-001 — Không báo đúng khi truy vấn báo cáo quá 30 giây

### Mô tả

Khi truy vấn báo cáo chạy quá 30 giây (timeout), hệ thống **không hiển thị đúng thông báo** hướng dẫn người dùng thu hẹp phạm vi.

### Các bước tái hiện

1. Đăng nhập role **CB_NV_TW** (`cb_nv_tw_01`).
2. Tạo báo cáo kỳ NĂM toàn quốc với dữ liệu lớn (khó tái hiện tự nhiên — cần BE inject delay ~35s qua test fixture để mô phỏng timeout/504).
3. Quan sát thông báo khi truy vấn vượt 30 giây.

### Kết quả mong đợi

- Hiển thị toast: **"Truy vấn quá thời gian. Vui lòng thu hẹp khoảng thời gian hoặc bộ lọc"** (ERR-RPT-03).

### Kết quả thực tế

- Không hiển thị đúng thông báo khi truy vấn báo cáo quá 30 giây.

### Bằng chứng

- Chưa có ảnh — server down 2026-07-07, chưa re-verify UI. Ghi nhận từ `report-dot-3.xlsx` (sheet "14. Báo cáo thống kê", TC-BC-REP-023). Cần chụp ảnh UI (kèm inject delay) khi server up.

### Re-test 2026-07-15 (verify lại Chrome DevTools MCP)

- **Cách verify:** UI-only bằng Chrome DevTools MCP, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_tw` / `Test@1234`, OTP MailHog.
- **Bước thực tế:** Vào **Báo cáo thống kê** (`/bao-cao`), enumerate control: chỉ có **Loại báo cáo / Kỳ báo cáo / Thời gian / Đơn vị / Xem báo cáo / Xuất Excel / Xuất PDF** — **không** có control/fixture nào để ép truy vấn > 30 giây hoặc inject delay. Dữ liệu nghiệp vụ hiện tại nhỏ (≤ vài chục bản ghi) nên mọi truy vấn render < 1s.
- **Phân loại blocker:** **Nhóm D (lỗi env / chờ infra)** — TC yêu cầu truy vấn thực sự vượt 30s (timeout/504). Không thể tái hiện bằng seed data UI thông thường (cần hàng vạn bản ghi hoặc BE inject delay ~35s qua test-mode) → tiền đề **không tạo được** bằng UI. Đây là blocker khách quan, không phải nhóm A (thiếu seed đơn lẻ).
- **Verdict:** `Re-verify blocked — cần BE test-mode/fixture để ép truy vấn > 30s (nhóm D)`. Không dùng API theo yêu cầu.

---

## ▉ MODULE 18 — CHƯƠNG TRÌNH HTPLDN (Đợt báo cáo — UC166/UC167)

> **5 bug dưới đây cùng phụ thuộc luồng Đợt báo cáo của đơn vị nộp.** Re-test UAT 2026-07-15 đã seed lại đợt báo cáo qua UI (`DOT-SO_BO_6_THANG-2026-1`) trước khi verify từng bug. Không còn block do thiếu danh sách đợt; riêng BUG-CT-BC-002 vẫn `Open` vì UI cho trình báo cáo chưa hoàn chỉnh.

## BUG-CT-BC-001 — Đơn vị nộp (CB NV BN/ĐP) trong phạm vi đợt bị 403 khi mở chi tiết đợt báo cáo

### Mô tả

CB Nghiệp vụ cấp ĐP/BN của đơn vị nằm trong phạm vi nộp của đợt báo cáo (`pham_vi_don_vi_nop_ids[]`) **không mở được chi tiết đợt báo cáo**: khi bấm **Xem**, hệ thống điều hướng sang trang `/403` ("Đơn vị không nằm trong phạm vi truy cập của bạn"). Hệ quả: đơn vị nộp không vào được màn hình lập BC (UC166) nên không có nút Trình phê duyệt (UC167). Mâu thuẫn: **màn hình danh sách** đợt vẫn hiển thị đợt cho đơn vị nộp (áp đúng phạm vi), nhưng **màn hình chi tiết** lại chặn.

### Các bước tái hiện

> **Tiền đề (do TW chuẩn bị trước):** Đăng nhập `cb_nv_tw_01`. Tạo 1 đợt báo cáo định kỳ, hạn nộp tương lai, phạm vi nộp `pham_vi_don_vi_nop_ids[]` bao gồm đơn vị "Bộ Kế hoạch và Đầu tư (BKH)". Hệ thống tự sinh record `DOT_BAO_CAO_DON_VI_NOP` cho BKH ở trạng thái `CHUA_NOP` (FR-XI-05a — srs-fr-15:656).

1. Đăng nhập role **CB_NV_BN** (`cb_nv_bn_01` / `Secret@123`, đơn vị BKH — thuộc phạm vi nộp). Theo SRS FR-XI-06 §Tác nhân (srs-fr-15:711), role này là tác nhân **hợp lệ** để lập/trình BC.
2. Vào menu **Đợt báo cáo** → danh sách **hiển thị đợt** do TW phát hành.
3. Bấm icon **Xem** (chi tiết) trên dòng đợt.
4. Quan sát: trang điều hướng sang `/403` — "Đơn vị không nằm trong phạm vi truy cập của bạn". Không vào được chi tiết đợt.

### Kết quả mong đợi

- Theo SRS FR-XI-06 (srs-fr-15:620): đơn vị nộp "vào tab 'Đợt báo cáo' của đơn vị mình để lập + nộp báo cáo theo Mẫu 21a/21b". Theo Preconditions (srs-fr-15:715-717): user là CB NV ĐP/BN + đơn vị ∈ `pham_vi_don_vi_nop_ids[]` + record nộp ở `CHUA_NOP`/`DANG_LAP` → được mở chi tiết đợt và lập BC.
- ⇒ Khi đơn vị nộp thuộc phạm vi bấm **Xem** đợt, hệ thống phải mở màn hình chi tiết đợt / form lập BC, **không** chặn 403. Quyền truy cập chi tiết đợt phải xét theo **phạm vi nộp**, không theo đơn vị chủ sở hữu đợt.

### Kết quả thực tế

- Bấm Xem chi tiết đợt → UI redirect sang `/403`. Không vào được chi tiết đợt → không có màn hình lập BC (UC166) và không có nút Trình phê duyệt (UC167).
- Đối chiếu cùng tài khoản: màn hình danh sách VẪN hiển thị đợt → phạm vi áp đúng ở danh sách nhưng **không áp ở chi tiết**.
- Phạm vi ảnh hưởng: toàn bộ đơn vị nộp (63 ĐP + BN) không lập/trình được BC.

### Bằng chứng

**Ảnh gốc (lỗi cũ)** — trang `/403` khi `cb_nv_bn_01` mở chi tiết đợt trong phạm vi nộp *(round 2026-06-30)*:

![BUG-CT-BC-001 — Đơn vị nộp CB_NV_BN bị 403 khi mở chi tiết đợt báo cáo](image/bug-ct-bc-001-don-vi-nop-403.png)

**Ảnh re-test 2026-07-15 (đã fix)** — `cbnv_bn` mở chi tiết đợt `DOT-SO_BO_NAM-2026-1` KHÔNG bị 403, hiển thị chi tiết đợt + biểu mẫu 21a + nút **Lập báo cáo**:

![BUG-CT-BC-001 re-test — mở chi tiết đợt không còn 403](image/bug-ct-bc-001-detail-no-403.png)

### Re-test 2026-07-15

- **Cách verify:** UI-only bằng Playwright/browser, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`.
- **Seed data qua UI:** Đăng nhập `cbnv_tw`, vào **Chương trình HTPLDN → Đợt báo cáo → Thêm mới**, tạo đợt `DOT-SO_BO_6_THANG-2026-1` / `QA Reverify CTBC 715 BN`, kỳ `Sơ bộ 6 tháng`, biểu mẫu `Mẫu 21a`, hạn nộp `31/12/2026`, phạm vi `83 đơn vị` bao gồm **Bộ Kế hoạch và Đầu tư (BKH)**.
- **Tài khoản verify:** `cbnv_bn` / `Test@1234`, OTP lấy từ MailHog.
- **Kết quả:** Đăng nhập `CB_NV_BN` (`cbnv_bn`), vào **Đợt báo cáo** thấy đợt trong phạm vi. Re-confirm 2026-07-15 trên đợt fresh `DOT-SO_BO_NAM-2026-1` (`/ct-htpldn/dot-bao-cao/e9909d96-1391-463b-8072-b1b56c319f8e`): UI mở detail thành công, `is403=false`, hiển thị thông tin đợt + biểu mẫu 21a + nút **Lập báo cáo**.
- **Verdict:** `Closed-verified 2026-07-15`. Bug 403 khi mở chi tiết đợt trong phạm vi nộp KHÔNG tái hiện — đơn vị nộp vào được chi tiết đợt và tới màn lập BC.

### So sánh (Comparison)

| Thao tác (cùng đợt, đơn vị BKH ∈ phạm vi nộp) | CB NV BN (`cb_nv_bn_01`, đơn vị nộp) | CB NV TW (`cb_nv_tw_01`, chủ đợt) |
|---|:--:|:--:|
| Danh sách đợt báo cáo | ✅ Hiển thị đợt | ✅ Hiển thị đợt |
| Mở chi tiết đợt | ❌ 403 → `/403` (BUG!) | ✅ Mở được |
| Lập BC (UC166) / Trình PD (UC167) | ❌ Không tới được màn hình | — (TW không tự lập BC — srs-fr-15:711) |

---

## BUG-CT-BC-002 — Không kiểm được chặn "BC chưa hoàn chỉnh" khi trình phê duyệt (chặn bởi BUG-CT-BC-001)

### Mô tả

Test case "Trình PD khi BC chưa hoàn chỉnh phải báo ERR-XI-07-01" **không thực thi được** vì đơn vị nộp không mở được chi tiết đợt (bị chặn 403 — BUG-CT-BC-001), chưa tới được màn hình có nút Trình phê duyệt.

### Các bước tái hiện

1. Đăng nhập role **CB_NV_BN** (`cb_nv_bn_01`, đơn vị nộp trong phạm vi đợt).
2. Mở chi tiết đợt → lập 1 BC **thiếu số liệu bắt buộc** (chưa hoàn chỉnh).
3. Bấm **[Trình phê duyệt]**.
4. Quan sát phản hồi hệ thống.

### Kết quả mong đợi

- Hệ thống chặn và báo lỗi **ERR-XI-07-01**: "Vui lòng hoàn chỉnh BC trước khi trình" (srs-fr-15:824).

### Kết quả thực tế

- **Không kiểm chứng được** — bước 2 không thực hiện được: đơn vị nộp bị chặn `403` khi mở chi tiết đợt (BUG-CT-BC-001), chưa tới màn hình lập/trình BC. Cần re-test sau khi fix BUG-CT-BC-001.

### Bằng chứng

- ![BC toàn số 0 được trình thành công](image/bug-ct-bc-002-blank-bc-submitted.png) — sau khi bấm **Trình duyệt KQ** trên BC với toàn bộ 13 chỉ tiêu = 0 (chỉ tiêu 12–13 nhập tay để trống), hệ thống chấp nhận, không có nút trình lại → BC đã chuyển sang chờ duyệt.

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, UI-only, KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`. **Tài khoản:** `cbnv_bn` / `Test@1234`, OTP từ MailHog.
- **Seed qua UI:** đợt fresh `DOT-SO_BO_NAM-2026-1` (kỳ Sơ bộ năm, phạm vi 83 đơn vị gồm BKH) — chưa có BC nộp.
- **Kết quả:** Mở detail đợt → **Lập báo cáo** → **Đồng ý** tạo nháp. Chỉ tiêu 1–11 auto `0 (HT)` (read-only), chỉ tiêu 12–13 (KP chi HĐ khác, KP xã hội hóa) là ô nhập tay **để trống** (valuetext rỗng). KHÔNG nhập gì → **Trình duyệt KQ** → **Đồng ý**. Hệ thống hiển thị **1 toast** "Trình duyệt thành công" (đo `.ant-message-notice` max=1 — không double toast ở flow này), **không** chặn bằng `ERR-XI-07-01`.
- **SRS đối chiếu:** `srs-fr-15:824` E1 "BC chưa hoàn chỉnh" → ERR-XI-07-01 (ERROR); `srs-fr-15:763` E1 "Thiếu số liệu bắt buộc" → ERR-XI-06-01. Field #8 `so_lieu` = Bắt buộc (Y) — **nhưng SRS KHÔNG định nghĩa cụ thể "hoàn chỉnh"** (không nói từng chỉ tiêu 1–13 có bắt buộc riêng hay không, cũng không nói BC toàn 0 = hợp lệ hay không).
- **Verdict:** `BA confirm 2026-07-15`. App cho trình BC toàn số 0 / ô nhập tay để trống mà không chặn. Do SRS có mã lỗi ERR-XI-07-01 nhưng **không định nghĩa điều kiện "hoàn chỉnh"**, chưa thể kết luận vi phạm spec: BC toàn 0 có thể là "báo cáo không phát sinh hoạt động" hợp lệ. **BA cần chốt:** BC toàn 0/để trống có được coi là hoàn chỉnh không. Nếu BA chốt phải chặn → dev bổ sung validation ERR-XI-07-01 (hiện KHÔNG kích hoạt kể cả khi BC hoàn toàn để trống).

---

## BUG-CT-BC-003 — Không kiểm được chặn trình PD khi đợt sai trạng thái (chặn bởi BUG-CT-BC-001)

### Mô tả

Test case "Đợt BC không ở DANG_LAP_BC thì không cho trình" **không thực thi được** vì đơn vị nộp không mở được chi tiết đợt (bị chặn 403 — BUG-CT-BC-001).

### Các bước tái hiện

1. Đăng nhập role **CB_NV_BN** (`cb_nv_bn_01`, đơn vị nộp).
2. Mở chi tiết 1 đợt đang ở trạng thái khác `DANG_LAP_BC` (vd `CHO_DUYET_KQ`).
3. Thử bấm **[Trình phê duyệt]**.
4. Quan sát phản hồi hệ thống.

### Kết quả mong đợi

- Hệ thống không cho trình khi đợt không ở `DANG_LAP_BC` (theo state machine SM-DOT-BC — srs-fr-15:788, 807).

### Kết quả thực tế

- **Không kiểm chứng được** — không mở được chi tiết đợt: đơn vị nộp bị chặn `403` (BUG-CT-BC-001). Cần re-test sau khi fix BUG-CT-BC-001.

### Bằng chứng

- Xem ảnh `/403` ở BUG-CT-BC-001. Server down 2026-07-07 — re-test khi server up + sau fix 001.

### Re-test 2026-07-15

- **Cách verify:** UI-only bằng Playwright/browser, không verify qua API.
- **Môi trường:** `http://18.143.165.120/login`.
- **Seed data qua UI:** Dùng đợt `DOT-SO_BO_6_THANG-2026-1`; `cbnv_bn` đã bấm **Lập báo cáo** và **Trình duyệt KQ** ở re-test BUG-CT-BC-002.
- **Tài khoản:** `cbnv_bn` / `Test@1234`, OTP lấy từ MailHog.
- **Kết quả:** Re-confirm 2026-07-15 trên đợt `DOT-SO_BO_NAM-2026-1`: sau khi `cbnv_bn` trình BC (đợt/BC rời trạng thái lập), mở lại detail đợt → chỉ còn bảng chỉ tiêu read-only; **không còn nút Lập báo cáo / Trình duyệt KQ** (danh sách button rỗng) để trình lại khi không ở trạng thái lập báo cáo.
- **Verdict:** `Closed-verified 2026-07-15`. UI không expose action trình khi không còn ở trạng thái lập báo cáo (state machine chặn đúng ở tầng UI).

---

## BUG-CT-BC-004 — Không kiểm được phân quyền trình PD (chặn bởi BUG-CT-BC-001)

### Mô tả

Test case "chỉ CB NV được trình BC" **không thực thi được** vì luồng truy cập đợt của đơn vị nộp đang bị chặn 403 (BUG-CT-BC-001), không dựng được kịch bản kiểm phân quyền trình.

### Các bước tái hiện

1. Đăng nhập một user **không phải CB NV** (hoặc CB NV không thuộc đơn vị nộp).
2. Mở chi tiết đợt → thử bấm **[Trình phê duyệt]** một BC.
3. Quan sát phản hồi hệ thống.

### Kết quả mong đợi

- Hệ thống chặn thao tác trình phê duyệt với user không đủ quyền (BR-AUTH-01 — srs-fr-15:800).

### Kết quả thực tế

- **Không kiểm chứng được** — luồng truy cập chi tiết đợt của đơn vị nộp đang bị chặn `403` (BUG-CT-BC-001), không dựng được tiền đề. Cần re-test sau khi fix BUG-CT-BC-001.

### Bằng chứng

- ![cbpd_bn chỉ có Phê duyệt/Từ chối](image/bug-ct-bc-004-cbpd-no-trinh-action.png) — `cbpd_bn` mở detail đợt chỉ thấy **Phê duyệt / Từ chối**, KHÔNG có Lập báo cáo / Trình duyệt KQ.
- ![Double toast tạo đợt trùng kỳ](image/bug-ct-bc-004-double-toast-duplicate-dot.png) — tạo đợt trùng kỳ (Sơ bộ năm 2026) hiển thị **2 toast** giống hệt "Đã tồn tại đợt báo cáo cho kỳ này".

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, UI-only, KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`.
- **Phần phân quyền — Tài khoản `cbpd_bn` / `Test@1234`:** `cbpd_bn` mở detail đợt `DOT-SO_BO_NAM-2026-1` (`/ct-htpldn/dot-bao-cao/e9909d96-...`) không bị `/403`, nhưng UI chỉ hiển thị action vai trò phê duyệt **Phê duyệt** / **Từ chối** (danh sách button = `["Phê duyệt","Từ chối"]`). Không có **Lập báo cáo** / **Trình duyệt KQ** cho user không phải CB NV.
- **Verdict phân quyền:** `Closed-verified 2026-07-15`. UI không expose action trình báo cáo cho `CB_PD_BN` (khớp BR-AUTH-01).
- **⚠️ Bug phụ phát sinh (double toast) — Tài khoản `cbnv_tw`:** Trên màn **Đợt báo cáo → Thêm mới**, điền đủ form với **Kỳ báo cáo = Sơ bộ năm 2026** (trùng `DOT-SO_BO_NAM-2026-1`) → **Thêm mới** đúng 1 lần. Hệ thống chặn đúng (không tạo đợt trùng) nhưng **emit 2 toast lỗi giống hệt** "Đã tồn tại đợt báo cáo cho kỳ này" (đo `.ant-message-notice` max đồng thời = 2, distinct = 2). **Trùng pattern với BUG-QT-001** → lỗi double toast hệ thống, cần dev khử trùng lặp toast lỗi ở tầng chung.

---

## BUG-CT-BC-005 — Không kiểm được thông báo CB PD sau khi trình BC (chặn bởi BUG-CT-BC-001)

### Mô tả

Test case "sau khi trình, CB PD cùng đơn vị nhận thông báo BC chờ duyệt" **không thực thi được** vì đơn vị nộp không trình được BC (bị chặn 403 khi mở đợt — BUG-CT-BC-001).

### Các bước tái hiện

1. (Tiền đề) Đơn vị nộp lập + **trình phê duyệt** 1 BC hoàn chỉnh → đợt chuyển `CHO_DUYET_KQ`.
2. Đăng nhập **CB PD cùng đơn vị**.
3. Kiểm tra danh sách/thông báo BC chờ duyệt.

### Kết quả mong đợi

- CB PD cùng đơn vị thấy thông báo "BC chờ duyệt" sau khi đơn vị nộp trình (BR-AUTH-05 — srs-fr-15:818).

### Kết quả thực tế

- **Không kiểm chứng được** — tiền đề (bước 1: trình BC) không thực hiện được: đơn vị nộp bị chặn `403` khi mở chi tiết đợt (BUG-CT-BC-001). Cần re-test sau khi fix BUG-CT-BC-001.

### Bằng chứng

- ![cbpd_bn nhận thông báo BC chờ duyệt](image/bug-ct-bc-005-cbpd-notification.png) — chuông thông báo của `cbpd_bn` hiển thị "Báo cáo đợt 'QA Reverify CTBC 715 v2 fresh' đã được trình duyệt. Mã: DOT-SO_BO_NAM-2026-1. Vui lòng xem xét và phê duyệt."

### Re-test 2026-07-15

- **Cách verify:** Chrome DevTools MCP, UI-only, KHÔNG verify qua API.
- **Môi trường:** `http://18.143.165.120/login`.
- **Tiền đề (fresh):** `cbnv_bn` mở đợt `DOT-SO_BO_NAM-2026-1`, **Lập báo cáo** + **Trình duyệt KQ** thành công (xem BUG-CT-BC-002).
- **Tài khoản kiểm thông báo:** `cbpd_bn` / `Test@1234`, OTP từ MailHog.
- **Kết quả:** Đăng nhập `cbpd_bn`, mở chuông thông báo → có notification **"Báo cáo đợt 'QA Reverify CTBC 715 v2 fresh' đã được trình duyệt. Mã: DOT-SO_BO_NAM-2026-1. Vui lòng xem xét và phê duyệt. 6 phút trước"** — đúng đợt vừa trình.
- **Verdict:** `Closed-verified 2026-07-15`. CB PD cùng đơn vị nhận được thông báo BC chờ duyệt sau khi CB NV trình (khớp BR-AUTH-05).

---

## Bug mới phát sinh (phát hiện khi re-verify 2026-07-15 — chưa có trong 22 bug gốc)

Các lỗi/nghi vấn phát hiện thêm trong quá trình verify fresh. Cần Dev xử lý riêng, không nằm trong danh sách 22 bug gốc.

| # | Mô tả | Bằng chứng / nơi phát hiện | Ai xử lý | Trạng thái re-verify 2026-07-16 |
|---|---|---|:-:|---|
| NEW-01 | **Double toast** lỗi tương tranh (`BUG-QT-001`) + double toast tạo đợt báo cáo trùng kỳ (note `BUG-CT-BC-004`) — 1 thao tác lỗi emit **2 toast** trùng lặp. Xử lý chung ở tầng error handler. | QT-001 verdict + CT-BC-004 note | Dev FE | ✅ Hết tái hiện — cả 2 chỗ chỉ 1 toast (đo peak=1) |
| NEW-02 | VV "Đã tiếp nhận" có **ngày tiếp nhận rỗng** dù field bắt buộc (`srs-fr-05:1690`); dòng rỗng nổi đầu khi sort DESC (NULLS FIRST) gây hiểu nhầm "mới nhất". Không phải lỗi sort (sort đúng). | Verdict `BUG-VV-001` | Dev BE (validation) + Dev FE (NULLS LAST) | ✅ Hết tái hiện — không còn VV rỗng, sort NULLS LAST 2 chiều |
| NEW-03 | Mã Doanh nghiệp mới sinh có prefix đơn vị dạng `DN-XX-` — nghi thiếu map mã đơn vị cấp TW. | Verdict `BUG-DN-001` (lưu ý phụ) | Dev BE | ✅ Hết tái hiện — mã mới sinh `DN-01-...`, hết `XX` |
| NEW-04 | Dropdown "Loại hồ sơ" (HSPL) hiển thị lẫn **mã enum thô** `GIAY_PHEP` / `HOP_DONG` cạnh nhãn tiếng Việt. | Verdict `BUG-DN-002` (lưu ý phụ) | Dev FE | ⚪ False positive — chỉ là node ẩn a11y AntD (aria-label = nhãn TV), user không thấy |

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng gốc | http://103.172.236.130:3000/ (đang down 2026-07-07 — `ERR_CONNECTION_TIMED_OUT`) |
| URL re-verify 2026-07-15 | http://18.143.165.120/login |
| OTP login | Lấy từ MailHog UI, không dùng bypass `666666` |
| MailHog (OTP inbox) | http://18.143.165.120:8025/ |
| Tài khoản dùng re-verify | Theo `output/UAT_doi-tac/input/input.md`: `admin`, `cbnv_tw`, `cbnv_bn`, `cbnv_dp`, `cbpd_*` khi cần |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT + OTP |
| Tool test | Chrome DevTools MCP (UI) |

> **Việc cần làm tiếp (sau re-verify fresh 2026-07-15 · cập nhật 2026-07-16):**
>
> 🔁 **Cập nhật 2026-07-16:** Cả 3 bug Open dưới đây + 3 "bug mới phát sinh" (NEW-02/03/04) đã **re-test lại 2026-07-16 và KHÔNG còn tái hiện** → lật Closed-verified (NEW-04 là false positive). Việc còn lại: xác nhận với dev có bản deploy fix không; dựng fixture cho `BUG-BC-001`; chờ BA chốt `BUG-DN-003` + `BUG-CT-BC-002`.
>
> - **~~3 bug Open~~ → đã Closed-verified 2026-07-16 (giữ lại để đối chiếu lịch sử):**
>   - `BUG-HD-001` (Dev BE) — upload file 0 byte không bị chặn (SRS yêu cầu reject file rỗng).
>   - `BUG-DT-002` (Dev FE) — chưa build chức năng xuất DOCX cho CTĐT đã duyệt (FR-III-20).
>   - `BUG-QT-001` (Dev FE) — **double toast** lỗi tương tranh; cùng lỗi với double toast màn tạo đợt trùng kỳ (`BUG-CT-BC-004` note) → xử lý chung ở tầng error handler để mỗi thao tác chỉ hiện **1** toast lỗi.
> - **8 bug Reject** (claim gốc KHÔNG tái hiện, không cần dev): `BUG-QT-002` (thêm được loại DN chỉ Mã+Tên), `BUG-QT-003/004/005` (guard ERR-DM-03 chặn đúng bản ghi đang tham chiếu), `BUG-QT-006` (không có nút VNeID trên /login), `BUG-DT-001` (Kế hoạch không có Hủy/DA_HUY — expected trích nhầm SM Khóa học), `BUG-VV-001` (sort đúng — claim không tái hiện), `BUG-VV-002` (app đúng INF-VV-01 — expected trích nhầm biến thể).
> - **2 bug BA confirm** (SRS silent thật sự, cần BA chốt trước khi kết luận): `BUG-DN-003` (`SPEC-CLARIFY-DN-21` — BR-DATA-05 không quy định có phải ghi audit cho request bị từ chối không), `BUG-CT-BC-002` (ERR-XI-07-01 có tên nhưng SRS không định nghĩa "BC hoàn chỉnh" — BC toàn 0 có thể là báo cáo không phát sinh hợp lệ).
> - **Bug mới phát sinh khi verify (cần Dev):** `BUG-VV-001` phái sinh — VV "Đã tiếp nhận" có ngày tiếp nhận **rỗng** dù field bắt buộc (srs-fr-05:1690); Dev BE siết validation + Dev FE đặt NULLS LAST. (Xem chi tiết mục "Bug mới phát sinh".)
> - **1 bug Re-verify blocked:** `BUG-BC-001` — thiếu timeout fixture/test-mode UI để tạo truy vấn >30 giây (cần Dev/Infra hỗ trợ dựng điều kiện).

---

*Bug report tổng hợp: 2026-07-07 | QA Automation via Claude Code*
