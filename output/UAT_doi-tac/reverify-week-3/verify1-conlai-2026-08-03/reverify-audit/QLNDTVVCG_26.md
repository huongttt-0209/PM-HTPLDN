# Audit re-verify — QLNDTVVCG_26 (row 323, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Chức năng:** Chuyên gia từ chối phân công yêu cầu tư vấn chuyên sâu (PHAN_CONG → TIEP_NHAN)
**Đối tác phản ánh:** Chuyên gia bấm "Từ chối phân công" → Cán bộ nghiệp vụ phụ trách KHÔNG nhận được thông báo kèm **lý do** từ chối
**Ngày verify:** 2026-08-03 · **Người verify:** QA (Claude Code) · **Env QA:** https://18.143.165.120.nip.io · **Bản dựng:** HTPLDN · V1.0.5 (đối tác quay trên V1.0.3)

> Case có **hai vế**, chấm riêng: (1) cán bộ nghiệp vụ phụ trách có nhận được thông báo không · (2) thông báo đó có kèm **lý do từ chối** không. Nhận được thông báo mà thiếu lý do thì vẫn tính là lỗi.

---

## Note dev trước khi QA đè (2026-08-03 20:35 giờ VN)

Cột P (`Trạng thái dev fix 1`) = `dev done`
Cột R (`DEV phản hồi lần 1`) = **TRỐNG — không có note dev để lưu.**

Dev đánh dấu đã fix nhưng **không viết giải trình**, nên không có manh mối nào từ dev về chỗ đã sửa. QA verify hoàn toàn độc lập, không dùng claim của dev làm căn cứ.

---

## CỔNG 1 — Bằng chứng đối tác

- File: `partner-evidence/QLNDTVVCG_26.webm` · Frames full-res: `frames/QLNDTVVCG_26/` (9 frame, đã mở đọc **từng ảnh** bằng Read tool, không suy từ tên file)

### 3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Nguồn frame |
|---|---|---|
| (a) | **Mã bản ghi / URL:** `TVCS-20260803-0001`, doanh nghiệp **TKM Company**, lĩnh vực **Thuế**, chuyên gia **huongcg**, tiêu đề "Test Quản lý tư vấn PL chuyên sâu". URL đối tác: `htpldn-uat.ospgroup.vn/tv-chuyen-sau/6eb2cc6a-4d10-4bc9-8bf2-b65fcfb47e1e`. Bản dựng góc trái: **HTPLDN · V1.0.3** | `t000.00s.jpg`, `t012.06s.jpg` |
| (b) | **Trạng thái + vai:** thẻ trạng thái "Phân công", hộp thoại **"Từ chối nhiệm vụ?"** có ô "Lý do từ chối" bắt buộc (validate "Lý do phải có ít nhất 10 ký tự"). Người bấm = `huongcg`, vai trò **TVV · CG**, đơn vị **BTP · TW**, chuông đang có **28**. Lý do gõ vào: "tkm kiểm thử chức năng từ chối" (30/1000). Sau khi bấm [Từ chối]: khung thông báo **"Đã xác nhận"**, bản ghi quay về bước **1 Tiếp nhận**, ô Chuyên gia đổi thành **"Chưa phân công"** | `t000.00s.jpg` → `t009.04s.jpg` → `t012.06s.jpg` |
| (c) | **Đối tác kiểm thông báo ở đâu / tài khoản nào / sau bao lâu:** đăng xuất lúc ~t015 → đăng nhập **`cbnv_tw`** ("Cán bộ NV Trung ương", CB_NV_TW, BTP · TW) lúc ~t018 → mở chuông lúc ~t021-t024 (≈21-24 giây sau khi bấm), badge **99+**: 5 mục hiển thị gồm 4 mục "Tài khoản vừa đăng nhập ở nơi khác" (9 phút / 2 ngày / 3 ngày / 3 ngày trước) + 1 mục "Hồ sơ TVV đã được phê duyệt" (3 ngày trước) — **không có** mục nào về việc chuyên gia từ chối, và **không có** mục nào phát sinh trong vài chục giây vừa rồi | `t015.07s.jpg`, `t018.08s.jpg`, `t021.09s.jpg`, `t024.10s.jpg` |

> ⚠️ Ghi chú trung thực về evidence: đối tác kiểm chuông bằng `cbnv_tw`, nhưng frame **không** chứng minh được `cbnv_tw` có đúng là người **tạo / phân công** bản ghi `TVCS-20260803-0001` hay không. Vì vậy chiều "cán bộ nghiệp vụ phụ trách" trong video chưa loại trừ hết khả năng kiểm nhầm tài khoản. Đây là lý do QA phải tự dựng bản ghi và dùng **đúng** tài khoản cán bộ đã tạo + phân công để đo lại. Đây là lỗ hổng **giống hệt** case anh em QLNDTVVCG_24.

## CỔNG 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `QLNDTVVCG_26.webm`; frame chứa LỖI = `t021.09s.jpg` / `t024.10s.jpg` — chuông của `cbnv_tw` chỉ có 5 mục, tất cả đều cũ (9 phút → 3 ngày trước), không mục nào nói chuyên gia từ chối và không mục nào chứa lý do. Đây là lỗi loại **absence** — frame chứng minh sự VẮNG MẶT của thông báo.
2. **Đối tác phản ánh cụ thể:** sau khi chuyên gia được phân công bấm [Từ chối nhiệm vụ], nhập lý do bắt buộc và bản ghi đã quay về "Tiếp nhận", **Cán bộ nghiệp vụ phụ trách không nhận được thông báo nào**, do đó cũng không thấy lý do từ chối.
3. **Data + bước tái hiện:** yêu cầu TVCS ở trạng thái `PHAN_CONG` đã phân công đúng chuyên gia đang đăng nhập, chuyên gia chưa xác nhận → đăng nhập chuyên gia → [Từ chối nhiệm vụ] → nhập lý do → [Từ chối] → kiểm chuông của cán bộ nghiệp vụ phụ trách và kiểm nội dung thông báo có chứa lý do vừa nhập hay không.

---

## CỔNG 3 — Đối chiếu SRS vs thực tế web

**Nguồn SRS duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — đã **mở file đọc đúng dòng**, không quote số dòng theo trí nhớ. Đã **grep toàn module** `srs-fr-12-tv-chuyen-sau.md` cho từ khoá "Từ chối" + "BR-NOTIF-01" trước khi chốt, và đọc cả phần màn hình `SCR-X1-02`.

| # | SRS yêu cầu (dẫn `file.md:LINE` + trích nguyên văn) | Thực tế web (QA đo 2026-08-03) | Đạt? |
|---|---|---|:-:|
| 1 | `srs-fr-12-tv-chuyen-sau.md:86` — "### FR-X.1-01: Quản lý nội dung tư vấn với chuyên gia (UC147)" · `:88` — "**UC Reference:** UC 147" | Đúng chức năng đang verify | ✅ |
| 2 | `srs-fr-12-tv-chuyen-sau.md:1169` — "Xác nhận CG (gộp từ MH-12.5): khi user là CG được phân công, hiện [Chấp nhận] / [Từ chối] trên thanh hành động." | Thanh hành động của bản ghi `PHAN_CONG` hiện đúng **[Chấp nhận] [Từ chối nhiệm vụ]** khi đăng nhập bằng chính chuyên gia được phân công (ảnh `-02`) | ✅ |
| 3 | `srs-fr-12-tv-chuyen-sau.md:195` — Processing "CG từ chối" bước 3: "\| 3 \| Yêu cầu lý do từ chối (bắt buộc) \| — \|" | Hộp thoại "Từ chối nhiệm vụ?" bắt buộc nhập "Lý do từ chối"; đã nhập 75/1000 ký tự (ảnh `-03`) | ✅ |
| 4 | `srs-fr-12-tv-chuyen-sau.md:196` — bước 4: "\| 4 \| Xóa liên kết chuyen_gia_id, trạng thái → TIEP_NHAN \| — \|" | Sau khi bấm: `trangThai = TIEP_NHAN`, `chuyenGiaId = null`, giao diện hiện "Tiếp nhận" + "Chưa phân công", stepper lùi về bước 1 (ảnh `-04`) | ✅ |
| 5 | `srs-fr-12-tv-chuyen-sau.md:197` — bước 5: "\| 5 \| Gửi thông báo CB NV: CG từ chối, cần phân công lại \| BR-NOTIF-01 \|" — **vế 1: có thông báo tới CB NV phụ trách** | Chuông `cbnv_tw_04` CÓ mục mới "**Chuyên gia từ chối phân công: TVCS-20260803-0003**", `nguoiNhanId = 9101c6bb-…` (đúng userId cán bộ đã tạo + phân công), `ngayTao = 2026-08-03T13:24:57.605Z` = đúng giây bấm nút. Badge chuông 43 → 44 (ảnh `-01` trước, `-05` sau) | ✅ |
| 6 | `srs-fr-12-tv-chuyen-sau.md:197` — cùng dòng trên — **vế 2: thông báo phải cho cán bộ biết CG từ chối, cần phân công lại; đối tác kỳ vọng thêm phần lý do** | Nội dung thông báo: "Mã: TVCS-20260803-0003. Chuyên gia đã từ chối, **cần phân công lại**. **Lý do:** QA-LY-DO-TU-CHOI-20260803-1325Z chuyen gia ban lich khong nhan nhiem vu nay" — chứa **đúng chuỗi lý do QA vừa nhập**, hiển thị đầy đủ trên màn "Thông báo" (ảnh `-06`, đã mở đọc pixel) | ✅ |
| 7 | `srs-fr-12-tv-chuyen-sau.md:1521` — bảng chuyển trạng thái: "\| PHAN_CONG \| TIEP_NHAN \| CG từ chối \| Có lý do \| Quay lại chọn CG khác \| FR-X.1-01 \| — \|" | Đúng: điều kiện "Có lý do" được cưỡng chế; sau từ chối bản ghi về TIEP_NHAN và thanh hành động của cán bộ hiện lại nút [Phân công] để chọn CG khác (ảnh `-05`) | ✅ |
| 8 | `srs-fr-12-tv-chuyen-sau.md:198` — bước 6: "\| 6 \| Ghi nhật ký thao tác (kèm lý do từ chối) \| BR-DATA-05 \|" | ⚠️ Nhật ký thao tác của bản ghi ghi dòng "03/08/2026 20:24 · **Cập nhật** · QA TVV Seed28 Active" — **không có cột/ô nào chứa lý do từ chối**, và hành động hiển thị là "Cập nhật" chứ không nêu là từ chối (ảnh `-07`). Xem mục "Quan sát ngoài phạm vi case" — **KHÔNG** gộp vào verdict | ⚠️ |

**Kết luận Cổng 3:** 7/8 đạt. Cả **hai vế** của case (có thông báo · thông báo kèm lý do) đều ĐẠT. Điểm ⚠️ duy nhất (lý do trong nhật ký thao tác) **nằm ngoài** triệu chứng đối tác mô tả — đối tác nói về **thông báo trên chuông**, không nói về nhật ký — nên xử lý riêng ở mục cuối.

---

## Kết quả test thật trên env QA

### Cấu hình test (ai đóng vai gì)

| Vai | Tài khoản | Vai trò · cấp | Vai trong case |
|---|---|---|---|
| Người BẤM | `qa_tvvseed28` — "QA TVV Seed28 Active", userId `5432719c-c542-4a5d-8c3a-db1b8a918bbf`, chuyên môn Thương mại, email `qa.tvvseed28@htpldn-uat.local` | `TVV · CG` · TW · Cục Bổ trợ tư pháp | Chuyên gia được phân công, bấm [Từ chối nhiệm vụ] |
| Người NHẬN — Cán bộ nghiệp vụ phụ trách | `cbnv_tw_04` — "CB Nghiệp vụ - Trung ương #04", userId `9101c6bb-6b1d-4f00-8c3c-2247f5b22e07` | `CB_NV_TW` · TW · BTP | **Chính tài khoản tạo yêu cầu và phân công chuyên gia** — `nguoiTaoId` của bản ghi = userId này, và nhật ký thao tác ghi hành động "Phân công" do `cbnv_tw_04` thực hiện lúc 20:21 → chắc chắn là cán bộ phụ trách |

`admin` **KHÔNG** được dùng ở bất kỳ bước nào. Mật khẩu `Test@1234`. Không có login fail → không phải áp Rule 7.

### Yêu cầu MỚI đã seed để đo

`TVCS-20260803-0003` (id `099a739d-02f6-4823-b2f8-1ac9cd2b60e6`) — DN "Cong ty TNHH QA UAT Kiem Thu" (mã số thuế `0109998887` = chính tên đăng nhập tài khoản DN), lĩnh vực **Thương mại**, tiêu đề "QLNDTVVCG_26 - Kiem tra thong bao khi CG tu choi phan cong".

Yêu cầu `TVCS-20260803-0001` (lượt đo cũ) và `-0002` (case QLNDTVVCG_24) đều đã bị tiêu → **không tái sử dụng**, seed hoàn toàn mới.

| Bước | Thời điểm (giờ VN) | Ai làm | Đo được (bộ đếm request + khung thông báo) |
|---|---|---|---|
| Tạo yêu cầu | 20:19 (`13:19:47.404Z`) | `cbnv_tw_04` | **1 request** `POST /api/v1/noi-dung-tu-van-cs` + **1 khung thông báo** "Tạo nội dung tư vấn thành công" — không lặp |
| Phân công chuyên gia | 20:21 (`ngayPhanCong = 2026-08-03T13:21:08.187Z`) | `cbnv_tw_04` → `qa_tvvseed28` | **1 request** `POST …/phan-cong` + **1 khung thông báo** "Đã phân công chuyên gia" — không lặp |

> Bước seed cũng là bề mặt quan sát (postmortem 16/07 Tầng 3): đã cài `tools/toast-capture.js` + chụp ảnh + **mở ảnh đọc** ở cả 2 bước. Không phát hiện thông báo lặp.

### Thao tác chính

Chuyên gia **tải lại trang** trước khi đo để chắc chắn không chạy JS bản dựng cũ — bản dựng đọc được trên giao diện: **HTPLDN · V1.0.5**.

| Mục | Giá trị đo |
|---|---|
| Thao tác | [Từ chối nhiệm vụ] → hộp thoại "Từ chối nhiệm vụ? / Lý do từ chối (bắt buộc)" → nhập chuỗi nhận dạng → [Từ chối] |
| Chuỗi lý do dùng để truy vết | `QA-LY-DO-TU-CHOI-20260803-1325Z chuyen gia ban lich khong nhan nhiem vu nay` (75/1000 ký tự) |
| Bộ đo | `tools/toast-capture.js` nguyên bản (không lọc trùng, đọc `innerText`, đếm request). **Tự kiểm `soObserverDangSong = 1` → hợp lệ** trước khi tin số liệu |
| Số request ghi dữ liệu | **1** — `POST /api/v1/noi-dung-tu-van-cs/099a739d-…/xac-nhan` → **200** |
| Số khung thông báo | **1** — "Đã xác nhận" (`khoangCachMs = null`, không có khung thứ 2) |
| Thời điểm bấm (đồng hồ trình duyệt) | `2026-08-03T13:24:57.477Z` (= **20:24:57** giờ VN) |
| Thời điểm máy chủ ghi nhận | `13:24:57.592Z` (nhật ký) · thông báo sinh lúc `13:24:57.605Z` |
| Kết quả trên màn | Trạng thái **Phân công → Tiếp nhận**, chuyên gia **→ "Chưa phân công"**, stepper lùi về bước 1 (ảnh `-04`) |
| Lý do có được lưu vào bản ghi không | CÓ — trường `ghiChu` của bản ghi = đúng chuỗi lý do vừa nhập |

### 🔢 Bảng số đo TRƯỚC → SAU — Cán bộ nghiệp vụ `cbnv_tw_04` (userId `9101c6bb-…`)

| Phép đo | TRƯỚC (13:22:18Z / 20:22 VN) | SAU (13:25:57Z / 20:25 VN, +60s) | Kiểm lại +230s (13:28:47Z) | Kiểm lại +374s (13:31:11Z) |
|---|---:|---:|---:|---:|
| Số bản ghi thông báo qua API (`/api/v1/thong-baos`, `meta.total`) | **44** | **45** | **45** | **45** |
| Số chưa đọc (đếm từ danh sách + `/thong-baos/unread-count`) | **43** | **44** | **44** | **44** |
| Số hiển thị trên chuông giao diện (badge, đọc từ DOM **và** từ ảnh) | **43** | **44** | 44 | 44 |
| Số thông báo nhắc tới `TVCS-20260803-0003` | **0** | **1** | **1** | **1** (không lặp, không mất) |
| Trong đó, số thông báo chứa **đúng chuỗi lý do** vừa nhập | **0** | **1** | **1** | **1** |

Bản ghi thông báo mới (đọc trong chính phiên đăng nhập của cán bộ):

- `id` = `d22f8079-f625-4cee-b0a3-527828d56e55`
- `tieuDe` = "Chuyên gia từ chối phân công: TVCS-20260803-0003"
- `noiDung` = "Mã: TVCS-20260803-0003. Chuyên gia đã từ chối, cần phân công lại. **Lý do: QA-LY-DO-TU-CHOI-20260803-1325Z chuyen gia ban lich khong nhan nhiem vu nay**"
- `loai` = `PHAN_CONG` · `entityId` = `099a739d-02f6-4823-b2f8-1ac9cd2b60e6` (đúng bản ghi vừa thao tác)
- `nguoiNhanId` = `9101c6bb-6b1d-4f00-8c3c-2247f5b22e07` · `ngayTao` = `2026-08-03T13:24:57.605Z`

> Hai lần "kiểm lại" đều chạy **sau ≥ 70 giây** kể từ lúc bấm (thực tế +230s và +374s), đúng yêu cầu loại trừ khả năng "thông báo tới muộn" — đồng thời loại luôn khả năng ngược lại là "tới rồi biến mất" hay "tới 2 bản trùng".

### ✅ Kết quả kiểm riêng vế "có lý do từ chối hay không"

| Bề mặt kiểm | Có chứa chuỗi `QA-LY-DO-TU-CHOI-20260803-1325Z` không? | Nằm ở trường nào |
|---|:-:|---|
| Bản ghi thông báo qua API (phiên của chính cán bộ) | **CÓ** | trường `noiDung` của thông báo, sau tiền tố "Lý do: " |
| Màn "Thông báo" trên giao diện của cán bộ (`/thong-baos`) | **CÓ** | dòng nội dung dưới tiêu đề "Chuyên gia từ chối phân công: TVCS-20260803-0003", hiển thị **đầy đủ**, không bị cắt (ảnh `-06`, đã mở đọc pixel) |
| Bản thân bản ghi tư vấn chuyên sâu | **CÓ** | trường `ghiChu` |
| Hộp xổ nhanh của chuông (dropdown 5 mục) | Không đủ chỗ | dropdown cắt ngắn ở "…cần phân công…" — đây là hành vi cắt chuỗi xem trước chung cho **mọi** loại thông báo, mở màn "Xem tất cả thông báo" là thấy đủ. Không tính là thiếu lý do |
| Nhật ký thao tác của bản ghi | **KHÔNG** | không có ô nào chứa lý do — xem mục "Quan sát ngoài phạm vi case" |

### Loại trừ đủ 3 khả năng

| Khả năng cần loại | Kết quả |
|---|---|
| (a) **Không sinh thông báo** | Loại — số bản ghi tăng 44 → 45, có bản ghi mới nêu đúng mã yêu cầu `TVCS-20260803-0003` |
| (b) **Sinh nhưng gửi SAI người** | Loại — `nguoiNhanId` = `9101c6bb-…` **trùng khớp** userId đọc từ phiên đăng nhập của chính cán bộ, đồng thời trùng `nguoiTaoId` của bản ghi và trùng người thực hiện hành động "Phân công" trong nhật ký; `ngayTao 13:24:57.605Z` khớp **giây** bấm nút (`13:24:57.477Z`) |
| (c) **Sinh đúng nhưng giao diện không hiện** | Loại — badge chuông tự tăng 43 → 44 (không cần tải lại trang), mở chuông thấy mục trên cùng "Chuyên gia từ chối phân công: TVCS-20260803-0003 · 2 phút trước" (ảnh `-05`), mở màn "Thông báo" thấy đủ cả lý do (ảnh `-06`) — cả 2 ảnh đều đã mở đọc pixel |

### Phép thử thứ hai (bug candidate ≠ bug — postmortem C2)

| Chiều đo | Phương pháp 1 | Phương pháp 2 | Khớp? |
|---|---|---|:-:|
| Thông báo có tồn tại không | Đọc danh sách bản ghi qua API trong **chính phiên đăng nhập của người nhận** | Mở chuông + mở màn "Thông báo" trên giao diện, **chụp ảnh và đọc pixel** | ✅ khớp — cả 2 đều cho đúng 1 mục mới |
| Có kèm lý do không | Chuỗi `QA-LY-DO-TU-CHOI-20260803-1325Z` tìm thấy trong trường `noiDung` của bản ghi thông báo | Chuỗi đó đọc được **bằng mắt** trên màn "Thông báo" (đọc DOM bằng `innerText`, không dùng `textContent`) + đọc lại từ ảnh chụp | ✅ khớp 3 nguồn |
| Số đếm | `meta.total` + `/thong-baos/unread-count` của API | Badge chuông trên thanh tiêu đề (đọc từ DOM **và** từ ảnh) | ✅ khớp (45/44 và 44 badge) |
| Đúng người nhận | `nguoiNhanId` trên bản ghi thông báo | `userId` trả về từ phiên đăng nhập của chính cán bộ + `nguoiTaoId` của bản ghi + người thực hiện "Phân công" trong nhật ký | ✅ khớp 4 nguồn |
| Thao tác có gây tác dụng phụ nào không | Bộ đếm request + khung thông báo của `toast-capture.js` | Danh sách request mạng của trình duyệt (`POST …/xac-nhan → 200`) | ✅ khớp — đúng 1 request, đúng 1 khung |

**Không có mâu thuẫn giữa hai phương pháp ở bất kỳ chiều nào** → đủ điều kiện chốt verdict.

### Kết luận

Cả hai vế của case đều ĐẠT trên bản dựng V1.0.5: cán bộ nghiệp vụ phụ trách **có** nhận được thông báo, và thông báo **có** kèm nguyên văn lý do từ chối. Triệu chứng đối tác phản ánh **không tái hiện**.

Đồng thời khép được lỗ hổng của evidence đối tác: họ kiểm chuông bằng `cbnv_tw` — một tài khoản mà video không chứng minh được là người phụ trách bản ghi đó. QA đo bằng **đúng** tài khoản đã tạo + phân công nên kết luận lần này là chắc chắn. Vì đây chỉ là **khả năng** kiểm nhầm chứ QA **không chứng minh được** đối tác thao tác sai, nên **không** dùng `Reject`.

**Verdict:** `Pass` (ghi cột **Verify (Q)**, giữ nguyên cột **P = `dev done`** của dev).

---

## Quan sát ngoài phạm vi case

**Có 2 phát hiện — MÔ TẢ cho người phụ trách, KHÔNG tự log lên sheet** (theo yêu cầu của lượt chạy này).

### 1. Nhật ký thao tác không lưu lý do từ chối, và ghi hành động là "Cập nhật" — hai chỗ trong SRS nói khác nhau ⇒ ca `BA confirm`

- Đo được: nhật ký thao tác của `TVCS-20260803-0003` chỉ có 3 dòng — "20:19 Tạo mới", "20:21 Phân công", "20:24 **Cập nhật** — QA TVV Seed28 Active". Dòng ứng với thao tác từ chối ghi hành động là **"Cập nhật"** chứ không phải "Từ chối", và **không có** ô nào chứa lý do (ảnh `-07`, đã mở đọc pixel). Đọc thẳng dữ liệu nhật ký cũng không có trường nào mang nội dung lý do.
- Mâu thuẫn trong chính SRS: `srs-fr-12-tv-chuyen-sau.md:198` yêu cầu "Ghi nhật ký thao tác **(kèm lý do từ chối)**"; nhưng phần đặc tả màn hình `srs-fr-12-tv-chuyen-sau.md:1160` lại định nghĩa vùng "Nhật ký thao tác" chỉ gồm "dd/mm/yyyy HH:mm -- {User} -- {Hành động}" — **không có chỗ cho lý do**. Hai chỗ không thống nhất ⇒ theo quy trình đây là ca **`BA confirm`**, không phải `Open`.
- Không gộp vào verdict case này vì: đối tác phản ánh về **thông báo trên chuông**, không hề nhắc nhật ký; và lý do vẫn được lưu đầy đủ (trường `ghiChu` của bản ghi + nội dung thông báo) nên không mất dấu vết.
- Đề xuất câu hỏi BA: "Nhật ký thao tác của TVCS có bắt buộc hiển thị lý do từ chối và tên hành động riêng (Từ chối) không, hay chỉ cần lưu ở thông báo + trường ghi chú của bản ghi?"

### 2. Khung thông báo sau khi TỪ CHỐI vẫn ghi "Đã xác nhận"

- Đo được: bấm [Từ chối] → khung thông báo hiện chữ **"Đã xác nhận"** — giống hệt khung khi bấm [Chấp nhận] ở case QLNDTVVCG_24. Bắt bằng `toast-capture.js` (`innerText`), 1 request + 1 khung, không lặp.
- Xuất hiện **cả trong video đối tác** (bản dựng V1.0.3, frame `t012.06s.jpg`) lẫn trên env QA (V1.0.5) ⇒ không phải khác biệt môi trường.
- SRS không quy định câu chữ của khung thông báo cho thao tác này, nên đây là **gợi ý cải thiện trải nghiệm** (dễ gây nhầm cho người dùng vừa bấm Từ chối lại thấy "Đã xác nhận"), không phải vi phạm đặc tả.

**Không phát hiện thêm gì khác** trên các ảnh đã mở đọc: không có thông báo lặp ở bất kỳ thao tác nào (3/3 thao tác đều 1 request + 1 khung), không có chữ lạ / rỗng / dựng dở trên các màn đã đi qua.

---

## Ghi sheet

| Mục | Giá trị |
|---|---|
| Tab · row | `UAT_TGPL Doanh Nghiệp-tuần 3` · **323** |
| Mode | `qaverdict` (chỉ ghi Q + R, **KHÔNG** đụng P) |
| `Q323` "Verify" | `''` → **`Pass`** |
| `R323` "DEV phản hồi lần 1" | `''` (trống, không có note dev bị mất) → note partner-facing ([notes/QLNDTVVCG_26.txt](../notes/QLNDTVVCG_26.txt)) |
| `P323` "Trạng thái dev fix 1" | **giữ nguyên `dev done`** |
| Evidence nộp kèm | `image/QLNDTVVCG_26-06-SAU-trang-thong-bao-co-ly-do.png` |
| Bảng điều kiện | [cond/QLNDTVVCG_26.md](../cond/QLNDTVVCG_26.md) — 7 dòng, 0 GAP |

Verdict là `Pass` nên **không** mở bug-report; ảnh của case nằm ở `image/`.

## Danh mục ảnh của case (đều đã mở đọc pixel)

| File | Nội dung |
|---|---|
| `QLNDTVVCG_26-seed-01-form-tao-moi.png` | Form thêm mới đã nhập đủ, tiêu đề `58 / 500`, tài khoản "CB Nghiệp vụ - Trung ương #04", chuông 43 |
| `QLNDTVVCG_26-seed-02-da-tao-tiep-nhan.png` | `TVCS-20260803-0003` vừa tạo, stepper bước 1 "Tiếp nhận", chuyên gia "Chưa phân công" |
| `QLNDTVVCG_26-seed-03-modal-phan-cong.png` | Hộp thoại "Phân công chuyên gia": chọn "QA TVV Seed28 Active — Thương mại", cảnh báo SLA 2 ngày làm việc |
| `QLNDTVVCG_26-seed-04-da-phan-cong.png` | Sau phân công: stepper bước 2 "Phân công", chuyên gia "QA TVV Seed28 Active", chuông vẫn 43 |
| `QLNDTVVCG_26-01-TRUOC-chuong-cbnv-tw-04.png` | **TRƯỚC** — chuông cán bộ badge **43**, mục trên cùng là "…TVCS-20260803-0002 · 22 phút trước", không có mục nào của `-0003` |
| `QLNDTVVCG_26-02-TRUOC-man-chuyen-gia.png` | Màn chuyên gia trước khi bấm: stepper bước 2, thanh hành động **[Sửa] [Chấp nhận] [Từ chối nhiệm vụ]**, chuông 27 |
| `QLNDTVVCG_26-03-modal-tu-choi-da-nhap-ly-do.png` | Hộp thoại "Từ chối nhiệm vụ?" đã nhập chuỗi lý do nhận dạng, `75 / 1000` |
| `QLNDTVVCG_26-04-sau-bam-tu-choi-toast.png` | **SAU** — bản ghi về "Tiếp nhận", chuyên gia "Chưa phân công", stepper lùi bước 1 (khung thông báo đã tự tắt trước khi ảnh kịp chụp; nội dung khung đã bắt được bằng bộ đo) |
| `QLNDTVVCG_26-05-SAU-chuong-cbnv-tw-04-co-thong-bao.png` | **SAU** — chuông cán bộ badge **44**, mục trên cùng "Chuyên gia từ chối phân công: TVCS-202… · 2 phút trước" |
| `QLNDTVVCG_26-06-SAU-trang-thong-bao-co-ly-do.png` | **SAU** — màn "Thông báo" của cán bộ, hiển thị đủ: "Mã: TVCS-20260803-0003. Chuyên gia đã từ chối, cần phân công lại. Lý do: QA-LY-DO-TU-CHOI-20260803-1325Z chuyen gia ban lich khong nhan nhiem vu nay" |
| `QLNDTVVCG_26-07-nhat-ky-thao-tac-khong-co-ly-do.png` | Nhật ký thao tác của bản ghi: 3 dòng, dòng 20:24 ghi hành động "Cập nhật", không có ô nào chứa lý do từ chối |
