# Audit re-verify — CNKQHT_07 (row 315, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Chức năng:** Cập nhật kết quả hỗ trợ của vụ việc HTPL
**Đối tác phản ánh:** Cập nhật kết quả hỗ trợ → CBNV phụ trách không nhận được thông báo
**Ngày verify:** 2026-08-03 · **Người verify:** QA (Claude Code) · **Env QA:** https://18.143.165.120.nip.io

---

## Note dev trước khi QA đè (2026-08-03)

Cột P (`Trạng thái dev fix 1`) = `dev done`
Cột R (`DEV phản hồi lần 1`) — chép NGUYÊN VĂN:

> Đã fix (BUG thật, SRS FR-V.I-15/UC65): capNhatKetQua emit event → listener gửi thông báo (in-app+email) cho CBNV phụ trách (nguoiTiepNhanId). Commit d394652e1. Verify unit test (pattern y hệt 5 handler đang chạy prod); e2e runtime N/A do cbnv_tw TW khác đơn vị assignee.

🔴 Dev TỰ KHAI chưa chạy e2e runtime. QA phải dựng đúng cặp đơn vị và chạy thật.

---

## CỔNG 1 — Bằng chứng đối tác

- File: `partner-evidence/CNKQHT_07.webm` (13.8 MB, ~51 giây, quay 30/07/2026 09:54-09:55)
- Frames full-res: `frames/CNKQHT_07/` (11 frame /5s + 13 frame /1s ở 2 đoạn then chốt)

### 3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Nguồn frame |
|---|---|---|
| (a) | **Mã vụ việc / URL:** `VV-BTP-TW-20260511-001` — tiêu đề `INVESTIGATE-NOTIF-01-170214`, nội dung yêu cầu "Probe NOTIF-01 listener at 170214 UTC for hypothesis test on UC62". URL đối tác: `htpldn-uat.ospgroup.vn/vu-viec/fa942aa3-e2a4-4608-be31-ec55a1f1cef9` | `t000.00s.jpg`, `t015.04s.jpg` |
| (b) | **Trạng thái + vai:** VV ở bước 6 **Đang xử lý** (`DANG_XU_LY`), badge "Quá hạn nghiêm trọng · 41 ngày LV". **Người bấm cập nhật** = `huongcg`, vai trò **TVV · CG**, đơn vị **BTP · TW** = người được phân công. **CB NV phụ trách** = tài khoản `cb_nv_tw_03@htpldn.test` — suy ra từ mail MailHog "Người hỗ trợ đã xác nhận tham gia vụ việc - VV-BTP-TW-20260511-001" gửi tới chính địa chỉ này (14 phút trước). Toast sau khi lưu: **"Đã cập nhật kết quả"** (1 khung) | `t000.00s.jpg`, `t015.04s.jpg`, `t025.10s.jpg` |
| (c) | **Đối tác kiểm tra thông báo ở đâu / tài khoản nào / sau bao lâu:** ① **MailHog** `htpldn-uat.ospgroup.vn/mailhog/` lúc 00:25-00:27 (~10 giây sau khi lưu) — inbox 205 mail, mail mới nhất là "Mã xác thực đăng nhập" (vài giây trước), **KHÔNG có mail nào về cập nhật kết quả**. ② Đăng xuất `huongcg` → **đăng nhập `cbnv_tw`** (OTP gửi `cbn***@htpldn.gov.vn`) → mở **chuông Thông báo** lúc 00:35 (~20 giây sau khi lưu): 4 mục "Tài khoản vừa đăng nhập ở nơi khác" + 1 mục "CT HTPL ... 2 ngày trước" — **KHÔNG có mục cập nhật kết quả** | `t022.05s.jpg`, `t026.44s.jpg`, `t027.46s.jpg`, `t030.10s.jpg`, `t035.10s.jpg` |

> ⚠️ Ghi chú trung thực về evidence: đối tác kiểm chuông **in-app** bằng `cbnv_tw`, trong khi mail xác nhận tham gia của chính VV đó lại gửi tới `cb_nv_tw_03` → hai tài khoản khác nhau. Chiều **in-app** trong video vì thế chưa loại trừ hết khả năng "kiểm nhầm tài khoản". Nhưng chiều **email** thì bằng chứng vắng mặt vẫn hợp lệ, vì MailHog là inbox CHUNG toàn hệ thống — không có mail gửi tới BẤT KỲ địa chỉ nào. Vì vậy QA vẫn phải tự dựng lại đủ 3 chiều trên env QA.

## CỔNG 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `CNKQHT_07.webm`, frame lỗi = `t025.10s.jpg` + `t026.44s.jpg` (MailHog rỗng mail cập nhật kết quả) và `t035.10s.jpg` (chuông Thông báo của CB NV không có mục mới) — đây là lỗi loại **absence**, frame chứng minh sự VẮNG MẶT.
2. **Đối tác phản ánh cụ thể:** sau khi người được phân công lưu "Cập nhật kết quả hỗ trợ" cho VV đang xử lý, hệ thống **không phát sinh thông báo nào** cho CB NV phụ trách — cả kênh in-app lẫn kênh email.
3. **Data + bước tái hiện:** VV `DANG_XU_LY` đã phân công, người phụ trách ≠ người thao tác → đăng nhập bằng người được phân công → Accordion 6 → [Cập nhật kết quả] → nhập nội dung → Đồng ý → kiểm chuông Thông báo của CB NV phụ trách + kiểm MailHog.

---

## CỔNG 3 — Đối chiếu SRS vs thực tế web

**Nguồn SRS duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` (đã mở file xác nhận số dòng, không quote theo trí nhớ).

| # | SRS yêu cầu (dẫn `file.md:LINE` + trích nguyên văn) | Thực tế web (QA đo 2026-08-03) | Đạt? |
|---|---|---|:-:|
| 1 | `srs-fr-05-vu-viec.md:1075` — "### FR-V.I-15: Người được phân công cập nhật kết quả hỗ trợ (UC65)" · `:1077` — "**UC Reference:** UC 65" | Đúng chức năng đang verify: người được phân công (`qa_tvvseed28`, TVV·CG) cập nhật kết quả hỗ trợ VV `VV-BTP-TW-20260803-001` | ✅ |
| 2 | `srs-fr-05-vu-viec.md:1078` — "**Màn hình:** SCR-V.I-03 (Accordion 6 — Kết quả Hỗ trợ, phần người được phân công)" · `:1732` — "\| 9 \| content \| Accordion 6 — Kết quả Hỗ trợ (gộp MH-05.7) \| C23 \| noi_dung_ket_qua (người được phân công)… \| Khi VV đã qua DANG_XU_LY" · `:1747` — "\| DANG_XU_LY \| [Cập nhật Kết quả] \| Người được phân công/CB NV \| Mở Accordion 6 để cập nhật" | Nút **[Cập nhật kết quả]** hiện ở thanh hành động khi VV ở `DANG_XU_LY`; bấm → mở form "Cập nhật kết quả hỗ trợ"; nội dung đã lưu hiện ở Accordion 6 "Kết quả hỗ trợ" (ảnh `-06`, `-07`, snapshot uid 38_109/38_110) | ✅ |
| 3 | `srs-fr-05-vu-viec.md:1106` — Processing bước 5: "\| 5 \| Gửi thông báo CB NV \| — \|" | Sau khi lưu, hệ thống sinh thông báo gửi CB NV phụ trách trên **cả 2 kênh** (chi tiết ở mục 5 + 6 dưới) | ✅ |
| 4 | `srs-fr-05-vu-viec.md:1114` — Postconditions: "- CB NV nhận thông báo để review" · `:1125` — AC: "**Given** người được phân công nhập nội dung + upload tài liệu **When** lưu **Then** cập nhật, thông báo CB NV" | CB NV phụ trách (`cbnv_tw_03`, `nguoiTiepNhanId` = `9b557200-be4b-46ac-b84b-fe6c154dc65f`) nhận được thông báo; nội dung mời "đăng nhập hệ thống để xem xét và chuẩn bị trình phê duyệt" → đúng mục đích review | ✅ |
| 5 | `srs-fr-05-vu-viec.md:2466` — **BR-NOTIF-01**: "Mọi sự kiện workflow … đều gửi thông báo cho người liên quan qua 2 kênh: **in-app (THONG_BAO) + email**. Người nhận xác định theo loại sự kiện." · `:2468` — "**Applied in (nhóm V.I):** … FR-V.I-15 …" — **kênh in-app** | Chuông Thông báo của `cbnv_tw_03` CÓ mục mới, tiêu đề đầy đủ (đọc qua `GET /api/v1/thong-baos`): **"Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260803-001"**, nội dung: "Người được phân công đã cập nhật kết quả hỗ trợ vụ việc: - Mã vụ việc: VV-BTP-TW-20260803-001 - Doanh nghiệp: Cong ty TNHH QA UAT Kiem Thu…", `nguoiNhanId` = `9b557200-…` (đúng CB NV phụ trách), `taoLuc` = `2026-08-03T10:23:11.932Z` (ảnh `-08`) | ✅ |
| 6 | `srs-fr-05-vu-viec.md:2466` — BR-NOTIF-01, **kênh email** | MailHog CÓ mail `To: cbnv_tw_03@htpldn.test`, `Date: Mon, 03 Aug 2026 10:23:11 +0000`, subject **"Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260803-001"**, thân mail nêu đúng mã vụ việc + tên doanh nghiệp (ảnh `-09`, đọc thêm bằng MailHog API) | ✅ |
| 7 | `srs-fr-05-vu-viec.md:1087` — PRE-02: "VV ở trạng thái DANG_XU_LY, tài khoản hiện tại là `PHAN_CONG_VU_VIEC.nguoi_xu_ly_id` của phân công đã chấp nhận" | API `GET /api/v1/vu-viecs/{id}` trả `trangThai = DANG_XU_LY`, `nguoiXuLyId = 5432719c-…` = tài khoản đang thao tác `qa_tvvseed28` → đúng tiền đề | ✅ |

**Kết luận Cổng 3:** 7/7 đạt. Không còn clause SRS nào bị vi phạm ở chức năng này.

---

## Kết quả test thật trên env QA

### Cấu hình test (ai đóng vai gì)

| Vai | Tài khoản | Vai trò · cấp | Vai trong case |
|---|---|---|---|
| Người phụ trách vụ việc (người PHẢI nhận thông báo) | `cbnv_tw_03` — "CB Nghiệp vụ - Trung ương #03", email `cbnv_tw_03@htpldn.test`, userId `9b557200-be4b-46ac-b84b-fe6c154dc65f` | `CB_NV_TW` · TW · BTP | Tạo VV → tiếp nhận → kiểm tra hồ sơ → phân công. API xác nhận `nguoiTiepNhanId` = userId này |
| Người thao tác (bấm Cập nhật kết quả) | `qa_tvvseed28` — "QA TVV Seed28 Active", userId `5432719c-c542-4a5d-8c3a-db1b8a918bbf` | `TVV · CG` · TW · Cục Bổ trợ tư pháp | Được phân công + đã chấp nhận. `nguoiXuLyId` = `nguoiHoTroId` = userId này |

`admin` **KHÔNG** được dùng ở bất kỳ bước nào (kể cả prep data). Mật khẩu cả 2 tài khoản: `Test@1234`. Không có login fail → không phải áp Rule 7.

### Vụ việc dùng để đo

`VV-BTP-TW-20260803-001` (id `8351c342-aba0-454b-9913-30cbd78ac714`) — trạng thái `DANG_XU_LY` (stepper bước 6), doanh nghiệp "Cong ty TNHH QA UAT Kiem Thu".

Chuỗi seed (ảnh `CNKQHT_07-seed-01` → `-seed-06`, khớp Dòng thời gian trên web):
`15:47 Tạo vụ việc` (cbnv_tw_03) → `17:02 Kiểm tra` (cbnv_tw_03) → `17:04 Phân công` (cbnv_tw_03 → qa_tvvseed28) → `17:06 Xác nhận phân công` (qa_tvvseed28) → `DANG_XU_LY`.

### 2 lần chạy thao tác chính

| Lần | Thời điểm | Ai bấm | Nội dung nhập | Đo được |
|---|---|---|---|---|
| Run 1 | 03/08/2026 **17:09** | `qa_tvvseed28` | "R14 QA re-verify CNKQHT_07 ngay 03/08/2026 - TVV cap nhat ket qua…" | Lưu OK (ảnh `-01`, `-03`) |
| Run 2 | 03/08/2026 **17:23** | `qa_tvvseed28` | "R15 QA re-verify CNKQHT_07 lan 2 ngay 03/08/2026 - do lai thong bao in-app va email…" | **1 request** `POST /api/v1/vu-viecs/8351c342-…/cap-nhat-ket-qua` + **1 khung thông báo** "Đã cập nhật kết quả" · `BI_LAP = false` (ảnh `-06`, `-07`) |

> Run 2 chạy **sau khi tải lại trang** (`reload ignoreCache`) trên cả 2 tab, đúng kỷ luật "tab MCP mở lâu vẫn chạy JS cũ". Bộ đo dùng nguyên `tools/toast-capture.js` (không lọc trùng, `innerText`, đếm request) — **tự kiểm `soObserverDangSong = 1`, hợp lệ** trước khi tin số liệu.
>
> Ghi chú kỹ thuật (KHÔNG phải lỗi app): lần bấm [Xác nhận] đầu tiên của run 2 bị form chặn với "Vui lòng nhập kết quả" vì công cụ MCP `fill` gán value vào DOM mà không kích hoạt state của React (bộ đếm ký tự vẫn `0 / 10000`). Gõ lại bằng `type_text` → bộ đếm nhảy `104 / 10000`, hết lỗi validate. Đây là hạn chế của công cụ đo, đã đo lại bằng đường gõ phím thật.

### Kết quả 3 chiều

| # | Chiều | Kết quả | Bằng chứng |
|:-:|---|---|---|
| 1 | **In-app** — chuông Thông báo mở bằng **chính** tài khoản CB NV phụ trách | ✅ **CÓ mục mới, ĐÚNG nội dung.** Tiêu đề đầy đủ "Kết quả hỗ trợ đã được cập nhật - **VV-BTP-TW-20260803-001**", nội dung "Người được phân công đã cập nhật kết quả hỗ trợ vụ việc: - Mã vụ việc: VV-BTP-TW-20260803-001 - Doanh nghiệp: Cong ty TNHH QA UAT Kiem Thu / Vui lòng đăng nhập hệ thống để xem xét và chuẩn bị trình phê duyệt". Badge chuông tăng 31 → 32. Dropdown hiện **2** mục cùng tiêu đề ("một phút trước" = run 2, "14 phút trước" = run 1) — khớp đúng 2 lần bấm, không phải nhân bản | Ảnh `CNKQHT_07-08-run2-inapp-chuong-cbnv-tw-03.png` (đã mở đọc pixel) + `GET /api/v1/thong-baos?pageSize=5` |
| 2 | **Email** — MailHog | ✅ **CÓ mail**, gửi tới **`cbnv_tw_03@htpldn.test`** (đúng địa chỉ CB NV phụ trách), phát sinh **SAU** thời điểm bấm lưu: run 1 → `2026-08-03T10:09:39Z`, run 2 → `2026-08-03T10:23:11Z`. Thân mail nêu đúng mã vụ việc + tên doanh nghiệp | Ảnh `CNKQHT_07-09-run2-mailhog-mail-gui-cbnv-tw-03.png` (đã mở đọc pixel) + MailHog API `search?kind=to` và `messages/{id}` |
| 3 | **Đúng người nhận** | ✅ Người nhận = **CB NV phụ trách**, KHÔNG phải người vừa bấm cập nhật, KHÔNG phải Doanh nghiệp. `thong-baos.nguoiNhanId` = `9b557200-be4b-46ac-b84b-fe6c154dc65f` **trùng khớp** `vu-viecs.nguoiTiepNhanId` = `9b557200-…` (CB Nghiệp vụ - Trung ương #03); người bấm là `5432719c-…` (QA TVV Seed28 Active) — hai id khác nhau | `GET /api/v1/vu-viecs/8351c342-…` + `GET /api/v1/auth/me` + `GET /api/v1/thong-baos` |

**Đo bằng phương pháp thứ hai (bug candidate ≠ bug):** chiều in-app đo trên UI (chuông) **và** đọc lại full payload qua API danh sách thông báo — 2 phương pháp **khớp nhau**, không mâu thuẫn. Chiều email đo trên UI MailHog **và** MailHog REST API — cũng khớp. Chiều người nhận đối chiếu chéo 3 endpoint.

### Kết luận

Đủ **3/3 chiều** → lỗi đối tác phản ánh **KHÔNG còn tái hiện** trên bản hiện tại; dev claim đã được kiểm chứng bằng **e2e runtime thật** (cái mà dev tự khai là "N/A"). Cái cớ "cbnv_tw TW khác đơn vị assignee" là tiền đề tạo được — QA đã dựng xong bằng `cbnv_tw_03` (BTP·TW) + `qa_tvvseed28` (Cục Bổ trợ tư pháp, TW) và chạy thông.

> Đồng thời khép lại lỗ hổng của evidence đối tác: họ kiểm chuông bằng `cbnv_tw` trong khi mail lại gửi `cb_nv_tw_03`. QA kiểm bằng **đúng** tài khoản phụ trách nên chiều in-app lần này là kết luận chắc chắn.

**Verdict:** `Pass` (ghi cột **Verify (Q)**, giữ nguyên cột **P = `dev done`** của dev).

---

## Quan sát ngoài phạm vi case (postmortem 16/07 — mục "Lỗi phát hiện thêm")

**Có 1 phát hiện, đã log thành dòng TC riêng.**

**Nhãn phân loại thông báo ghi sai bản chất sự kiện.** Thông báo "Kết quả hỗ trợ đã được cập nhật" và "Người hỗ trợ đã xác nhận tham gia vụ việc" đều bị gán `loaiThongBao = PHAN_CONG`, nên tiêu đề trong **thân email** hiển thị thành **"📋 Phân công: Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260803-001"** — người nhận đọc dòng đầu sẽ tưởng đây là thông báo phân công, trong khi sự kiện thật là cập nhật kết quả.

- Đo bằng 2 phương pháp: đọc nội dung hiển thị trên MailHog UI (a11y tree của iframe preview) **và** đọc thẳng phần thân mail qua MailHog API trên 3 mail khác nhau. Kết quả khớp.
- Đối chứng: mail thuộc nhóm khác (`Phản hồi đã được phê duyệt`) **không** có tiền tố nào → tiền tố "📋 Phân công:" đúng là suy ra từ `loai`, không phải chuỗi cố định của template chung.
- Mức độ: **Minor** (chữ hiển thị sai bản chất, không ảnh hưởng dữ liệu/luồng). SRS `srs-fr-05-vu-viec.md:1056` chỉ khai `loai_thong_bao` kiểu `text`, **không** quy định bộ nhóm → phần "nhóm nào là đúng" cần BA chốt; phần "tiêu đề mail nói sai loại sự kiện" thì quan sát được rõ ràng.
- Không trùng 3 lỗi đã log trước đó (`NHSYC_OOS_01`, `BUG-NHSYC_01-B`, `QLHSVV_OOS_01`).
- **Đã đưa tới dev:** dòng TC mới `CNKQHT_OOS_01` — tab `UAT_TGPL Doanh Nghiệp-tuần 2` **row 141** (`Trạng thái 1 = Fail`, `Verify = Open`, `DEV phản hồi lần 1` đã điền) + bug-report [`bug-reports/vu-viec/bug-report-vu-viec.md`](../bug-reports/vu-viec/bug-report-vu-viec.md) (Bug ID `BUG-CNKQHT_OOS_01`, Minor/P3).

---

## Ghi sheet

| Mục | Giá trị |
|---|---|
| Tab · row | `UAT_TGPL Doanh Nghiệp-tuần 3` · **315** |
| Mode | `qaverdict` (chỉ ghi Q + R, **KHÔNG** đụng P) |
| `Q315` "Verify" | `''` → **`Pass`** (đọc lại khớp) |
| `R315` "DEV phản hồi lần 1" | đè note dev cũ → note partner-facing 2255 ký tự ([notes/CNKQHT_07.txt](../notes/CNKQHT_07.txt)) |
| `P315` "Trạng thái dev fix 1" | **giữ nguyên `dev done`** |
| Evidence nộp kèm | `image/CNKQHT_07-08-run2-inapp-chuong-cbnv-tw-03.png` |
| Bảng điều kiện | [cond/CNKQHT_07.md](../cond/CNKQHT_07.md) — 7 dòng, 0 GAP |
| Log | `tools/sheet_write.log` ts `2026-08-03T17:31:18` |

Đã đọc lại `Q315` ngay trước khi ghi (vẫn rỗng) để tránh đè verdict của phiên QA khác đang chạy song song trên cùng sheet.

## Danh mục ảnh của case (đều đã mở đọc pixel)

| File | Nội dung |
|---|---|
| `CNKQHT_07-seed-01…-seed-06` | Chuỗi seed: đã tiếp nhận → kiểm tra hồ sơ → sau kiểm tra → modal phân công → đã phân công → TVV chấp nhận sang Đang xử lý |
| `CNKQHT_07-01-form-cap-nhat-ket-qua-truoc-khi-luu.png` | Run 1 — form đã nhập, bộ đếm `116 / 10000`, tài khoản "QA TVV Seed28 Active · TVV·CG" |
| `CNKQHT_07-02-toast-da-cap-nhat-ket-qua.png` | ⚠️ **Tên file lệch pixel** — ảnh chụp sau khi khung thông báo đã tắt, KHÔNG có toast trong khung hình. Không dùng làm bằng chứng toast; đã thay bằng `-07` + số liệu observer |
| `CNKQHT_07-03-accordion6-da-luu-ket-qua.png` | Run 1 — Accordion 6 đã lưu nội dung kết quả |
| `CNKQHT_07-04-inapp-chuong-cbnv-tw-03-co-thong-bao-moi.png` | Run 1 — chuông của `cbnv_tw_03`: mục đầu "Kết quả hỗ trợ đã được cập nhật - VV-BT…" (3 phút trước) |
| `CNKQHT_07-05-mailhog-tim-cbnv-tw-03-truoc-khi-loc.png` | Run 1 — hộp thư: mail "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260803-001" tới `cbnv_tw_03@htpldn.test` (4 phút trước) |
| `CNKQHT_07-06-run2-form-truoc-khi-luu.png` | Run 2 — form đã nhập; bộ đếm còn `0 / 10000` → dấu hiệu công cụ `fill` chưa kích hoạt state React (đã xử lý bằng `type_text`) |
| `CNKQHT_07-07-run2-toast-da-cap-nhat-ket-qua.png` | Run 2 — bắt được khung thông báo "Đã cập nhật kết quả" đang mờ dần ở đỉnh trang |
| `CNKQHT_07-08-run2-inapp-chuong-cbnv-tw-03.png` | Run 2 — chuông `cbnv_tw_03`: 2 mục "Kết quả hỗ trợ đã được cập nhật" (một phút trước / 14 phút trước), badge 32 |
| `CNKQHT_07-09-run2-mailhog-mail-gui-cbnv-tw-03.png` | Run 2 — hộp thư: mail mới 2 phút trước tới `cbnv_tw_03@htpldn.test` |
| `CNKQHT_OOS_01-01-email-tieu-de-ghi-sai-loai-su-kien.png` | Nội dung thư: `To cbnv_tw_03@htpldn.test`, Subject đúng, nhưng tiêu đề thân thư "📋 Phân công: Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260803-001" |

