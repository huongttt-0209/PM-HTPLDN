# Audit re-verify — QLNDTVVCG_24 (row 322, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Chức năng:** Chuyên gia chấp nhận phân công yêu cầu tư vấn chuyên sâu (PHAN_CONG → DANG_TU_VAN)
**Đối tác phản ánh:** Chuyên gia bấm "Chấp nhận" → Doanh nghiệp **và** Cán bộ nghiệp vụ đều KHÔNG nhận được thông báo
**Ngày verify:** 2026-08-03 · **Người verify:** QA (Claude Code) · **Env QA:** https://18.143.165.120.nip.io · **Bản dựng:** HTPLDN · V1.0.5

> 🔁 **Lượt đo này là LẦN CHẠY LẠI.** Lượt trước (cùng ngày, ~19:12 giờ VN) bị ngắt giữa chừng do **lỗi mạng của hạ tầng**, không phải do đo sai; transcript mất nên toàn bộ con số cũ bị coi là **không có giá trị chứng minh**. Yêu cầu `TVCS-20260803-0001` của lượt trước cũng đã bị tiêu (chuyên gia đã bấm Chấp nhận → nay `DANG_TU_VAN`), nên lượt này **seed một yêu cầu MỚI** `TVCS-20260803-0002` và đo lại từ đầu bằng tay. Ảnh của lượt trước (`QLNDTVVCG_24-01…-06`, `-seed-01…-04`) được giữ lại nhưng **không dùng làm căn cứ verdict**; căn cứ verdict là bộ ảnh có tiền tố `-R2-`.

---

## Note dev trước khi QA đè (2026-08-03 20:10 giờ VN)

Cột P (`Trạng thái dev fix 1`) = `dev done`
Cột R (`DEV phản hồi lần 1`) = **TRỐNG — không có note dev để lưu.**

Dev đánh dấu đã fix nhưng **không viết giải trình**, nên không có manh mối nào từ dev về chỗ đã sửa. QA verify hoàn toàn độc lập.

---

## CỔNG 1 — Bằng chứng đối tác

- File: `partner-evidence/QLNDTVVCG_24.webm` · Frames full-res: `frames/QLNDTVVCG_24/` (10 frame, đã mở đọc **từng ảnh** bằng Read tool, không đọc từ tên file)

### 3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Nguồn frame |
|---|---|---|
| (a) | **Mã bản ghi / URL:** `TVCS-20260803-0001`, doanh nghiệp **TKM Company**, lĩnh vực **Thuế**, chuyên gia **huongcg**. URL đối tác: `htpldn-uat.ospgroup.vn/tv-chuyen-sau/6eb2cc6a-4d10-4bc9-8bf2-b65fcfb47e1e` | `t000.00s.jpg` |
| (b) | **Trạng thái + vai:** stepper đứng ở bước **2 Phân công**, thẻ trạng thái "Phân công", thanh hành động có **[Chấp nhận] / [Từ chối nhiệm vụ]**. Người bấm = `huongcg`, vai trò **TVV · CG**, đơn vị **BTP · TW**, chuông đang có **29** thông báo chưa đọc. Sau khi bấm: khung thông báo **"Đã xác nhận"**, trạng thái sang **Đang tư vấn** | `t000.00s.jpg`, `t005.03s.jpg` |
| (c) | **Đối tác kiểm thông báo ở đâu / tài khoản nào / sau bao lâu:** ① đăng xuất → đăng nhập tài khoản **DN `0151554887` ("Tester TKM")** lúc ~t011-t013 (≈10 giây sau khi bấm) → mở chuông: **chỉ 1 mục** "Tài khoản vừa đăng nhập ở nơi khác" (vài giây trước), **không có** mục nào về việc chuyên gia xác nhận. ② đăng xuất → đăng nhập **`cbnv_tw`** ("Cán bộ NV Trung ương", CB_NV_TW, BTP·TW) lúc ~t025-t030 (≈25 giây sau khi bấm) → mở chuông (badge 99+): 4 mục "Tài khoản vừa đăng nhập ở nơi khác" (13 phút / 2 ngày / 3 ngày trước) + 1 mục "Hồ sơ TVV đã được phê duyệt" (3 ngày trước) — **không có** mục nào phát sinh trong vài giây vừa rồi | `t011.02s.jpg`, `t013.07s.jpg`, `t015.06s.jpg`, `t025.11s.jpg`, `t030.43s.jpg` |

> ⚠️ Ghi chú trung thực về evidence: đối tác kiểm chuông cán bộ bằng `cbnv_tw`, nhưng frame **không** chứng minh được `cbnv_tw` có đúng là người **tạo / phân công** bản ghi `TVCS-20260803-0001` hay không. Vì vậy chiều "cán bộ nghiệp vụ" trong video chưa loại trừ hết khả năng kiểm nhầm tài khoản. Đây là lý do QA phải tự dựng bản ghi và dùng **đúng** tài khoản cán bộ đã tạo/phân công để đo lại.

## CỔNG 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `QLNDTVVCG_24.webm`; frame chứa LỖI = `t013.07s.jpg` / `t015.06s.jpg` (chuông DN chỉ có 1 mục đăng nhập, không có mục xác nhận tư vấn) và `t030.43s.jpg` (chuông cán bộ, 5 mục hiển thị đều cũ từ 13 phút → 3 ngày trước). Đây là lỗi loại **absence** — frame chứng minh sự VẮNG MẶT của thông báo.
2. **Đối tác phản ánh cụ thể:** sau khi chuyên gia được phân công bấm [Chấp nhận] và bản ghi đã chuyển sang "Đang tư vấn", **không có thông báo nào** xuất hiện trên chuông của **cả hai** người nhận — Doanh nghiệp của yêu cầu và Cán bộ nghiệp vụ.
3. **Data + bước tái hiện:** yêu cầu TVCS ở trạng thái `PHAN_CONG` đã phân công đúng chuyên gia đang đăng nhập, chuyên gia chưa xác nhận → đăng nhập chuyên gia → [Chấp nhận] → xác nhận trong hộp thoại → kiểm chuông của DN sở hữu yêu cầu và của cán bộ nghiệp vụ phụ trách.

---

## CỔNG 3 — Đối chiếu SRS vs thực tế web

**Nguồn SRS duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — đã **mở file đọc đúng dòng**, không quote số dòng theo trí nhớ.

| # | SRS yêu cầu (dẫn `file.md:LINE` + trích nguyên văn) | Thực tế web (QA đo 2026-08-03) | Đạt? |
|---|---|---|:-:|
| 1 | `srs-fr-12-tv-chuyen-sau.md:86` — "### FR-X.1-01: Quản lý nội dung tư vấn với chuyên gia (UC147)" · `:88` — "**UC Reference:** UC 147" | Đúng chức năng đang verify | ✅ |
| 2 | `srs-fr-12-tv-chuyen-sau.md:1169` — "Xác nhận CG (gộp từ MH-12.5): khi user là CG được phân công, hiện [Chấp nhận] / [Từ chối] trên thanh hành động." | Thanh hành động của bản ghi `PHAN_CONG` hiện đúng **[Chấp nhận] [Từ chối nhiệm vụ]** khi đăng nhập bằng chính chuyên gia được phân công (ảnh `-R2-03`) | ✅ |
| 3 | `srs-fr-12-tv-chuyen-sau.md:184` — Processing bước 4: "\| 4 \| Cập nhật trạng thái → DANG_TU_VAN, ghi ngay_bat_dau = NOW() \| — \|" | Trạng thái chuyển **Phân công → Đang tư vấn** ngay sau khi xác nhận; `ngayBatDau` = `2026-08-03T13:00:31.695Z` = đúng giây bấm nút (ảnh `-R2-04`) | ✅ |
| 4 | `srs-fr-12-tv-chuyen-sau.md:185` — Processing bước 5: "\| 5 \| Tạo PHIEN_TU_VAN mới liên kết với bản ghi TVCS \| — \|" | Bản ghi phiên tư vấn mới đã sinh, liên kết đúng yêu cầu: 1 phiên, id `76556fee-2b22-4754-a97a-ed856f867778`, `ngayTao` = `13:00:31.683Z`, trạng thái `CHO_XAC_NHAN` | ✅ |
| 5 | `srs-fr-12-tv-chuyen-sau.md:186` — Processing bước 6: "\| 6 \| Gửi thông báo DN + CB NV: CG đã xác nhận \| BR-NOTIF-01 \|" — **chiều Doanh nghiệp**, kênh in-app | Chuông DN `0109998887` CÓ mục mới "**Chuyên gia đã xác nhận tư vấn: TVCS-20260803-0002**", nội dung "Mã: TVCS-20260803-0002. Chuyên gia đã nhận việc, nội dung đang được tư vấn.", `nguoiNhanId` = `996cc5db-…` (đúng userId của DN), `ngayTao` = `13:00:31.710Z`. Badge chuông 5 → 6 (ảnh `-R2-01` trước, `-R2-05` sau) | ✅ |
| 6 | `srs-fr-12-tv-chuyen-sau.md:186` — cùng dòng trên — **chiều Cán bộ nghiệp vụ**, kênh in-app | Chuông `cbnv_tw_04` CÓ mục mới cùng tiêu đề, nội dung "…nội dung chuyển sang trạng thái đang tư vấn.", `nguoiNhanId` = `9101c6bb-…` (đúng userId cán bộ đã tạo + phân công), `ngayTao` = `13:00:31.731Z`. Badge chuông 42 → 43 (ảnh `-R2-02` trước, `-R2-06` sau) | ✅ |
| 7 | `srs-fr-12-tv-chuyen-sau.md:1520` — bảng chuyển trạng thái: "\| PHAN_CONG \| DANG_TU_VAN \| CG xác nhận \| — \| Tạo phiên TV, TB DN \| FR-X.1-01 \| — \|" | Cả 2 hành động ở cột Action đều xảy ra (phiên tư vấn + thông báo DN). Bảng này **chỉ nêu "TB DN"**, không nhắc CB NV — hẹp hơn dòng `:186`; thực tế web đáp ứng **cả hai** cách đọc nên khác biệt này không đổi kết quả case | ✅ |
| 8 | `srs-v3.5.md:5611` — BR-NOTIF-01: "**Kênh:** in-app + email; SMS chỉ với case khẩn…" | ⚠️ **Chỉ có kênh in-app.** Hộp thư MailHog **không** có mail nào cho cả 2 người nhận ở thời điểm bấm; tìm toàn bộ hộp thư theo "TVCS" / "xác nhận tư vấn" / "tư vấn chuyên sâu" → **0 kết quả** (xem mục "Quan sát ngoài phạm vi case") | ⚠️ |

**Kết luận Cổng 3:** 7/8 đạt. Điểm ⚠️ duy nhất (kênh email) **nằm ngoài** triệu chứng đối tác mô tả và **không** phải thứ đối tác quan sát trong video — xử lý ở mục "Quan sát ngoài phạm vi case", không gộp vào verdict.

---

## Kết quả test thật trên env QA

### Cấu hình test (ai đóng vai gì)

| Vai | Tài khoản | Vai trò · cấp | Vai trong case |
|---|---|---|---|
| Người BẤM | `qa_tvvseed28` — "QA TVV Seed28 Active", userId `5432719c-c542-4a5d-8c3a-db1b8a918bbf`, chuyên môn Thương mại, email `qa.tvvseed28@htpldn-uat.local` | `TVV · CG` · TW · Cục Bổ trợ tư pháp | Chuyên gia được phân công, bấm [Chấp nhận] |
| Người NHẬN #1 — Doanh nghiệp | `0109998887` — "QA UAT Kiem Thu DN", userId `996cc5db-43c5-4903-b3d1-1c21adb2ece8`, email `qa.uat.dn.verify@test.htpldn.vn` | `DN` | DN sở hữu yêu cầu. Đối chiếu: hồ sơ doanh nghiệp của yêu cầu có `maSoThue` = `0109998887` = **chính tên đăng nhập** của tài khoản này → ràng buộc chứng minh bằng dữ liệu, không bằng lập luận |
| Người NHẬN #2 — Cán bộ nghiệp vụ | `cbnv_tw_04` — "CB Nghiệp vụ - Trung ương #04", userId `9101c6bb-6b1d-4f00-8c3c-2247f5b22e07`, email `cbnv_tw_04@htpldn.test` | `CB_NV_TW` · TW · BTP | **Chính tài khoản tạo yêu cầu và phân công chuyên gia** — `nguoiTaoId` của bản ghi = userId này → chắc chắn là cán bộ phụ trách |

`admin` **KHÔNG** được dùng ở bất kỳ bước nào. Mật khẩu cả 3 tài khoản: `Test@1234`, đăng nhập kèm OTP lấy từ MailHog. Không có login fail → không phải áp Rule 7.

### Yêu cầu MỚI đã seed để đo

`TVCS-20260803-0002` (id `73178d48-44d9-4198-87a9-5df4340c0736`) — DN "Cong ty TNHH QA UAT Kiem Thu", lĩnh vực **Thương mại**, tiêu đề "QLNDTVVCG_24 R2 - Kiem tra thong bao khi CG chap nhan phan cong".

Chuỗi seed do chính QA dựng bằng tài khoản nghiệp vụ (ảnh `-R2-seed-01` → `-R2-seed-04`, đều đã mở đọc pixel):

| Bước | Thời điểm (giờ VN) | Ai làm | Đo được (bộ đếm request + khung thông báo) |
|---|---|---|---|
| Tạo yêu cầu | 19:54 | `cbnv_tw_04` | **1 request** `POST /api/v1/noi-dung-tu-van-cs` + **1 khung thông báo** "Tạo nội dung tư vấn thành công" — không lặp |
| Phân công chuyên gia | 19:56 (`ngayPhanCong` = `2026-08-03T12:56:05.941Z`) | `cbnv_tw_04` → `qa_tvvseed28` | **1 request** `POST …/phan-cong` + **1 khung thông báo** "Đã phân công chuyên gia" — không lặp |

> Bước seed cũng được coi là bề mặt quan sát (postmortem 16/07 Tầng 3): đã cài `tools/toast-capture.js` + chụp ảnh + **mở ảnh đọc** ở cả 2 bước. Không phát hiện thông báo lặp.

### Thao tác chính

Chuyên gia đăng nhập, **tải lại trang** (`reload ignoreCache`) trước khi đo để chắc chắn không chạy JS của bản dựng cũ — bản dựng đọc được trên giao diện: **HTPLDN · V1.0.5**.

| Mục | Giá trị đo |
|---|---|
| Thao tác | [Chấp nhận] → hộp thoại "Chấp nhận tư vấn? / Bạn xác nhận chấp nhận nhiệm vụ tư vấn này." → [Chấp nhận] |
| Bộ đo | `tools/toast-capture.js` nguyên bản (không lọc trùng, đọc `innerText`, đếm request). **Tự kiểm `soObserverDangSong = 1` → hợp lệ** trước khi tin số liệu |
| Số request ghi dữ liệu | **1** — `POST /api/v1/noi-dung-tu-van-cs/73178d48-…/xac-nhan` → **200** |
| Số khung thông báo | **1** — "Đã xác nhận" (`khoangCachMs = null`, không có khung thứ 2) |
| Thời điểm máy chủ ghi nhận | `13:00:31Z` (= **20:00:31** giờ VN) |
| Kết quả trên màn | Trạng thái **Phân công → Đang tư vấn**, stepper nhảy sang bước 3 (ảnh `-R2-04`) |

### 🔢 Bảng số đo TRƯỚC → SAU, tách RIÊNG từng người nhận

**Người nhận #1 — Doanh nghiệp `0109998887` (userId `996cc5db-…`)**

| Phép đo | TRƯỚC (12:59Z / 19:59 VN) | SAU (13:01:15Z / 20:01 VN) | Kiểm lại phút 5 (13:05:43Z) |
|---|---:|---:|---:|
| Số bản ghi thông báo qua API (`/api/v1/thong-baos`, `total`) | **5** | **6** | **6** |
| Số chưa đọc trên chuông giao diện (badge) | **5** | **6** | 6 |
| Số thông báo nhắc tới `TVCS-20260803-0002` | **0** | **1** | **1** (không lặp, không mất) |

Bản ghi mới: tiêu đề "Chuyên gia đã xác nhận tư vấn: TVCS-20260803-0002" · `loai = PHAN_CONG` · `ngayTao = 2026-08-03T13:00:31.710Z` · `nguoiNhanId = 996cc5db-43c5-4903-b3d1-1c21adb2ece8`.

**Người nhận #2 — Cán bộ nghiệp vụ `cbnv_tw_04` (userId `9101c6bb-…`)**

| Phép đo | TRƯỚC (12:58Z / 19:58 VN) | SAU (13:01:58Z / 20:02 VN) | Kiểm lại phút 5 (13:05:26Z) |
|---|---:|---:|---:|
| Số bản ghi thông báo qua API (`/api/v1/thong-baos`, `total`) | **43** | **44** | **44** |
| Số chưa đọc trên chuông giao diện (badge) | **42** | **43** | 43 |
| Số thông báo nhắc tới `TVCS-20260803-0002` | **0** | **1** | **1** (không lặp, không mất) |

Bản ghi mới: tiêu đề "Chuyên gia đã xác nhận tư vấn: TVCS-20260803-0002" · `loai = PHAN_CONG` · `ngayTao = 2026-08-03T13:00:31.731Z` · `nguoiNhanId = 9101c6bb-6b1d-4f00-8c3c-2247f5b22e07`.

> Cả 2 lần "kiểm lại" đều chạy **sau ≥ 70 giây** kể từ lúc bấm (thực tế +5 phút), đúng yêu cầu loại trừ khả năng "thông báo tới muộn" — và cũng loại luôn khả năng ngược lại là "tới rồi biến mất" hay "tới 2 bản trùng".

### Loại trừ đủ 3 khả năng, cho TỪNG người nhận

| Khả năng cần loại | Doanh nghiệp | Cán bộ nghiệp vụ |
|---|---|---|
| (a) **Không sinh thông báo** | Loại — số bản ghi tăng 5 → 6, có bản ghi mới nêu đúng mã yêu cầu | Loại — số bản ghi tăng 43 → 44, có bản ghi mới nêu đúng mã yêu cầu |
| (b) **Sinh nhưng gửi SAI người** | Loại — `nguoiNhanId` = `996cc5db-…` **trùng khớp** userId đọc từ phiên đăng nhập của chính DN; `ngayTao 13:00:31.710Z` khớp **giây** bấm nút (`ngayBatDau 13:00:31.695Z`) | Loại — `nguoiNhanId` = `9101c6bb-…` **trùng khớp** userId của cán bộ, và trùng `nguoiTaoId` của bản ghi; `ngayTao 13:00:31.731Z` khớp giây bấm nút |
| (c) **Sinh đúng nhưng giao diện không hiện** | Loại — badge chuông tự tăng 5 → 6, mở chuông thấy mục nằm trên cùng "…TVCS-20260803-0002 · một phút trước" (ảnh `-R2-05`, đã mở đọc pixel) | Loại — badge chuông tự tăng 42 → 43, mở chuông thấy mục trên cùng "…TVCS-20260803-0002 · 2 phút trước" (ảnh `-R2-06`, đã mở đọc pixel) |

### Phép thử thứ hai (bug candidate ≠ bug — postmortem C2)

| Chiều đo | Phương pháp 1 | Phương pháp 2 | Khớp? |
|---|---|---|:-:|
| Thông báo có tồn tại không | Đọc danh sách bản ghi qua API trong **chính phiên đăng nhập của người nhận** | Mở chuông trên giao diện + **chụp ảnh và đọc pixel** | ✅ khớp — cả 2 đều cho đúng 1 mục mới/người |
| Số đếm | `total` của API danh sách | Badge chuông trên thanh tiêu đề (đọc từ DOM **và** từ ảnh) | ✅ khớp (6/6 và 44/43+1 đã đọc) |
| Đúng người nhận | `nguoiNhanId` trên bản ghi thông báo | `userId` trả về từ phiên đăng nhập của chính người đó + `nguoiTaoId` / `maSoThue` trên bản ghi yêu cầu | ✅ khớp 3 nguồn |
| Thao tác có gây tác dụng phụ nào không | Bộ đếm request + khung thông báo của `toast-capture.js` | Danh sách request mạng của trình duyệt (`POST …/xac-nhan → 200`) | ✅ khớp — đúng 1 request, đúng 1 khung |

**Không có mâu thuẫn giữa hai phương pháp ở bất kỳ chiều nào** → đủ điều kiện chốt verdict.

### Kết luận

Cả **hai** người nhận đều nhận được thông báo, kiểm riêng từng người, không gộp. Ba khả năng (a)(b)(c) đều bị loại cho **từng** người. Triệu chứng đối tác phản ánh **không tái hiện** trên bản dựng V1.0.5.

Đồng thời khép được lỗ hổng của evidence đối tác: họ kiểm chuông cán bộ bằng `cbnv_tw` — một tài khoản mà video không chứng minh được là người phụ trách bản ghi đó. QA đo bằng **đúng** tài khoản đã tạo + phân công nên chiều cán bộ lần này là kết luận chắc chắn. Vì đây chỉ là **khả năng** kiểm nhầm chứ QA **không chứng minh được** đối tác thao tác sai, nên **không** dùng `Reject`.

**Verdict:** `Pass` (ghi cột **Verify (Q)**, giữ nguyên cột **P = `dev done`** của dev).

---

## Quan sát ngoài phạm vi case

**Có 1 phát hiện — báo cho người phụ trách, KHÔNG tự log lên sheet** (theo yêu cầu của lượt chạy này).

**Sự kiện tư vấn chuyên sâu không phát sinh email, trong khi các nhóm nghiệp vụ khác thì có.**

- Đo được: sau khi bấm [Chấp nhận] lúc `13:00:31Z`, hộp thư MailHog **không** có mail nào gửi tới `qa.uat.dn.verify@test.htpldn.vn` hay `cbnv_tw_04@htpldn.test`. Tìm toàn bộ hộp thư theo 3 từ khoá "TVCS", "xác nhận tư vấn", "tư vấn chuyên sâu" → **0 kết quả**, tức chưa từng có mail nào của nhóm tư vấn chuyên sâu.
- Đối chứng loại trừ "hộp thư hỏng": cùng ngày, cùng hộp thư, các nhóm khác **vẫn gửi bình thường** — "Vụ việc đã được tiếp nhận - VV-BTP-TW-20260803-004" (10:57Z, tới chính địa chỉ DN này), "Báo cáo đánh giá chờ phê duyệt - DG-20260725-0001" (11:45Z, tới 6 tài khoản CB PD), "Câu hỏi đã quá hạn xử lý" (10:30Z, tới chính `cbnv_tw_04@htpldn.test`). ⇒ kênh email của hệ thống hoạt động, chỉ riêng nhóm tư vấn chuyên sâu không dùng.
- Bước phân công chuyên gia (19:56) cũng **không** sinh mail cho chuyên gia, dù `srs-fr-12-tv-chuyen-sau.md:174` ghi rõ kênh: "\| 5 \| Gửi thông báo CG/TVV **(in-app + email)**: nội dung yêu cầu + SLA 2 ngày LV xác nhận \| BR-NOTIF-01 \|".
- **Vì sao KHÔNG gộp vào verdict case này:** ① đối tác không hề nhắc email, video của họ chỉ mở chuông in-app — chấm Reopen vì một chiều họ không quan sát là chấm sai phạm vi; ② căn cứ SRS cho **riêng bước "CG xác nhận"** thì mập mờ: dòng `:186` chỉ ghi "Gửi thông báo DN + CB NV" **không** nêu kênh, trong khi các bước lân cận (`:174`, `:499`, `:768`) đều ghi rõ "(in-app + email)"; kênh 2 chiều chỉ suy ra gián tiếp từ BR-NOTIF-01 ở `srs-v3.5.md:5611`. Hai chỗ trong chính SRS không thống nhất ⇒ theo quy trình, đây là ca **`BA confirm`**, không phải `Open`.
- Đề xuất: hỏi BA "bước CG xác nhận TVCS có bắt buộc kênh email không, hay chỉ in-app?" trước khi mở dòng TC mới cho dev. Nếu BA chốt bắt buộc thì phạm vi lỗi rộng hơn 1 bước — nên rà cả nhóm tư vấn chuyên sâu (phân công CG, CG từ chối, trình/phê duyệt) vì hiện chưa bước nào gửi mail.

**Không phát hiện thêm gì khác** trên các ảnh đã mở đọc: không có thông báo lặp ở bất kỳ thao tác nào (3/3 thao tác đều 1 request + 1 khung), không có chữ lạ / rỗng / dựng dở trên các màn đã đi qua.

---

## Ghi sheet

| Mục | Giá trị |
|---|---|
| Tab · row | `UAT_TGPL Doanh Nghiệp-tuần 3` · **322** |
| Mode | `qaverdict` (chỉ ghi Q + R, **KHÔNG** đụng P) |
| `Q322` "Verify" | `''` → **`Pass`** |
| `R322` "DEV phản hồi lần 1" | `''` (trống, không có note dev bị mất) → note partner-facing ([notes/QLNDTVVCG_24.txt](../notes/QLNDTVVCG_24.txt)) |
| `P322` "Trạng thái dev fix 1" | **giữ nguyên `dev done`** |
| Evidence nộp kèm | `image/QLNDTVVCG_24-R2-05-SAU-chuong-doanh-nghiep-co-thong-bao.png` |
| Bảng điều kiện | [cond/QLNDTVVCG_24.md](../cond/QLNDTVVCG_24.md) — 7 dòng, 0 GAP |

Verdict là `Pass` nên **không** mở bug-report; toàn bộ ảnh của case đã chuyển từ `bug-reports/tvcs/image/` về `image/`, thư mục `bug-reports/tvcs/` đã xoá vì rỗng.

## Danh mục ảnh của case (đều đã mở đọc pixel)

| File | Nội dung |
|---|---|
| `QLNDTVVCG_24-R2-seed-01-form-tao-moi.png` | Form thêm mới đã nhập đủ, tiêu đề `63 / 500`, tài khoản "CB Nghiệp vụ - Trung ương #04", chuông 42 |
| `QLNDTVVCG_24-R2-seed-02-da-tao-tiep-nhan.png` | `TVCS-20260803-0002` vừa tạo, stepper bước 1 "Tiếp nhận", chuyên gia "Chưa phân công" |
| `QLNDTVVCG_24-R2-seed-03-modal-phan-cong-chuyen-gia.png` | Hộp thoại "Phân công chuyên gia": chọn "QA TVV Seed28 Active — Thương mại", chuyên môn Thương mại, cảnh báo SLA 2 ngày làm việc |
| `QLNDTVVCG_24-R2-seed-04-da-phan-cong-chuyen-gia.png` | Sau phân công: stepper bước 2 "Phân công", chuyên gia "QA TVV Seed28 Active" |
| `QLNDTVVCG_24-R2-01-TRUOC-chuong-doanh-nghiep.png` | **TRƯỚC** — chuông DN badge **5** |
| `QLNDTVVCG_24-R2-02-TRUOC-chuong-cbnv-tw-04.png` | **TRƯỚC** — chuông cán bộ badge **42**, bản ghi vẫn "Phân công" |
| `QLNDTVVCG_24-R2-03-TRUOC-chuyen-gia-man-chap-nhan.png` | Màn chuyên gia trước khi bấm: stepper bước 2, thanh hành động **[Sửa] [Chấp nhận] [Từ chối nhiệm vụ]**, chuông 26 |
| `QLNDTVVCG_24-R2-04-sau-chap-nhan-dang-tu-van.png` | **SAU** — stepper bước 3 "Đang tư vấn", thẻ trạng thái "Đang tư vấn", nút đổi thành [Hoàn thành] |
| `QLNDTVVCG_24-R2-05-SAU-chuong-doanh-nghiep-co-thong-bao.png` | **SAU** — chuông DN badge **6**, mục trên cùng "Chuyên gia đã xác nhận tư vấn: TVCS-20…0002 · một phút trước" |
| `QLNDTVVCG_24-R2-06-SAU-chuong-cbnv-tw-04-co-thong-bao.png` | **SAU** — chuông cán bộ badge **43**, mục trên cùng "Chuyên gia đã xác nhận tư vấn: TVCS-20…0002 · 2 phút trước" |
| `QLNDTVVCG_24-01…-06`, `-seed-01…-04` (không có `R2`) | Ảnh **lượt chạy trước bị ngắt** — lưu để tra cứu, **không** dùng làm căn cứ verdict lần này |
