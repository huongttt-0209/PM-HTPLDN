# Audit — XNTGHTVV_03 (row 2) · Từ chối tham gia hỗ trợ vụ việc

## Cổng 1 — Bằng chứng (ĐÓNG)

- File: `partner-evidence/XNTGHTVV_03.webm` (3.84 MB), fetch_evidence.py exit 0.
- Frames full-res: `frames/t000.00s → t031.04s.jpg` (11 frame, đã mở đọc từng ảnh).
- Frame chứa LỖI: **t012.09s** (và giữ nguyên ở t015.11s, t018.45s).

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị đọc từ frame |
|---|---|---|
| (a) | URL / ID bản ghi | `htpldn-uat.ospgroup.vn/vu-viec/ab08db14-4e92-48fe-8f2b-b2a0ad00b4a3` — mã `VV-BTP-TW-2…` (bị modal che), tiêu đề "Test file đính kèm vụ việc", lĩnh vực Thuế, ngày tiếp nhận 30/06/2026 10:28, deadline 21/07/2026 |
| (b) | Trạng thái entity đối tác đang đứng | **Đã phân công** — detail hiện đủ 2 nút `[✓ Chấp nhận]` `[✗ Từ chối]` + badge "Còn 7 ngày LV"; stepper 10 bước SM-VUVIEC |
| (c) | Dữ liệu tiền đề | Account `huongcg`, vai trò **TVV · CG**, đơn vị **BTP · TW**. Cột "Người xử lý / Tổ chức" = `huongcg` ở mọi dòng danh sách → VV phân công cho chính tài khoản đang đăng nhập |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `XNTGHTVV_03.webm`, frame **t009.07s** (modal "Từ chối phân công", lý do "TKM test từ chối thành công" 27/1000, con trỏ trên nút **Xác nhận**) → frame **t012.09s** chứa lỗi: ngay sau khi bấm Xác nhận, hệ thống điều hướng sang `/403` — "**Vụ việc không được phân công cho bạn**", Mã lỗi `ERR-AUTH-VPD-00-04`, "Vai trò hiện tại: TVV CG".
2. **Đối tác phản ánh CỤ THỂ:** (Ý 1) TVV được phân công bấm Từ chối → bị chặn 403 "không được phân công cho bạn" dù chính họ là người được phân công. (Ý 2) sau đó trạng thái bản ghi thành "**Chờ phê duyệt**" (thay vì "Đã tiếp nhận" theo KQMĐ).
3. **Data + bước tái hiện:** login TVV·CG được phân công → Vụ việc HTPL → mở VV trạng thái Đã phân công → [Từ chối] → nhập lý do ≥10 ký tự → Xác nhận.

### Diễn biến theo timeline video

| Frame | Quan sát |
|---|---|
| t006.05s (08:36) | Modal "Từ chối phân công", đang gõ lý do "TKM test từ chối t" (18/1000) |
| t009.07s | Lý do đủ "TKM test từ chối thành công" (27/1000), con trỏ trên **Xác nhận** |
| **t012.09s (08:37)** | **Màn `/403` — "Vụ việc không được phân công cho bạn", `ERR-AUTH-VPD-00-04`, Vai trò hiện tại: TVV CG** |
| t015.11s / t018.45s | Vẫn ở 403; đối tác bôi đen dòng chữ lỗi để nhấn mạnh |
| t021.46s | Quay lại `/vu-viec/danh-sach` (đang tải, trắng) |
| t024.95s | Danh sách "Tất cả **4**": VV-BKH-20260526-001 (Chờ phê duyệt) + 3 VV "Đã phân công". **VV vừa từ chối (30/06, VV-BTP-TW) KHÔNG còn trong danh sách** |
| t027.96s / t031.04s | Lọc tab "Chờ phê duyệt (1)" → chỉ **VV-BKH-20260526-001** (Cty TNHH Sông Hồng B…, Thuế, 26/05) |

### ⚠️ Phản biện ý 2 của đối tác (ghi lại, chưa kết luận)

Bản ghi đối tác vừa từ chối là **VV-BTP-TW-…** (id `ab08db14…`, DN "Test file đính kèm vụ việc", ngày 30/06). Bản ghi duy nhất ở tab "Chờ phê duyệt" là **VV-BKH-20260526-001** — **khác mã, khác DN, khác ngày (26/05)**. Video KHÔNG có frame "trước khi từ chối" của danh sách để chứng minh VV-BKH mới đổi trạng thái. → Ý 2 nhiều khả năng là **đọc nhầm sang bản ghi khác**, nhưng phải tự tái hiện mới kết luận.

## Cổng 3 — Đối chiếu SRS (v3.5)

| SRS yêu cầu (dẫn line) | Thực tế web đối tác | Đủ/Thiếu |
|---|---|:-:|
| `srs-fr-05-vu-viec.md:822` — FR-V.I-10 (UC 60) Processing bước 3: "Nếu TU_CHOI: chuyển VV → **DA_TIEP_NHAN** (phân công lại)" | Bị chặn 403, thao tác không hoàn tất | ❌ Thiếu |
| `srs-fr-05-vu-viec.md:845` — AC: "**Given** người được phân công từ chối **When** nhập lý do **Then** VV quay lại DA_TIEP_NHAN" | Không đạt | ❌ Thiếu |
| `srs-fr-05-vu-viec.md:806` — PRE-02: "VV ở trạng thái DA_PHAN_CONG, tài khoản hiện tại là `PHAN_CONG_VU_VIEC.nguoi_xu_ly_id`" | Đối tác thoả cả 2 (nút Chấp nhận/Từ chối được render + cột Người xử lý = huongcg) | ✅ Đủ tiền đề |
| `srs-fr-05-vu-viec.md:839` — E1 `ERR-XN-01` "Bạn không được phân công cho vụ việc này" **chỉ khi** tài khoản KHÔNG phải người được phân công | Web trả `ERR-AUTH-VPD-00-04` + điều hướng `/403` dù tài khoản ĐÚNG là người được phân công | ❌ Sai |
| `srs-fr-05-vu-viec.md:1735` — SCR-V.I-03: "DA_PHAN_CONG → [Chấp nhận] [Từ chối] · Người được phân công · Từ chối → DA_TIEP_NHAN" | Nút render đúng nhưng thao tác bị chặn | ❌ Thiếu |

## Bảng đối chiếu điều kiện

→ [`../../cond/XNTGHTVV_03.md`](../../cond/XNTGHTVV_03.md) — **0 GAP**, đã đóng GAP vai trò bằng test thật (gán vai trò CG cho `qa_tvvseed28`, đăng nhập lại, `auth/me` = `["TVV","CG"]`).

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

| Lần | Vai trò khi test | Vụ việc | Kết quả |
|:-:|---|---|---|
| 1 | TVV | VV-BTP-TW-20260712-001 | ❌ Điều hướng `/403` — "Vụ việc không được phân công cho bạn", `ERR-AUTH-VPD-00-04` |
| 2 | **TVV · CG** (khớp đối tác) | VV-BTP-TW-20260712-005 | ❌ Y hệt; màn 403 in "Vai trò hiện tại: TVV CG" |

**Tái hiện 2/2.** Ảnh: `04-ngay-sau-khi-bam-xac-nhan.png` (lần 1) · `07-tvv-cg-ngay-sau-xac-nhan.png` (lần 2).

### Phép đo (tools/toast-capture.js — không lọc trùng, đọc innerText, đếm request)

Tự kiểm observer: `soObserverDangSong = 1` → số liệu hợp lệ.

| Chỉ số | Giá trị |
|---|---|
| SO_REQUEST_GHI | **1** — `POST /api/v1/vu-viecs/{id}/tu-choi-phan-cong` |
| SO_KHUNG_THONG_BAO | **1** — "Đã từ chối phân công" |
| BI_LAP | false |

→ Không phải gửi 2 lần, không phải thông báo lặp. Thao tác **thành công** nhưng người dùng bị đẩy sang màn 403.

### Kiểm chứng bằng phương pháp thứ hai (API trực tiếp)

`POST /api/v1/vu-viecs/d7b6cdf8-…/tu-choi-phan-cong` (VV-BTP-TW-20260712-003) → **HTTP 201**:
- `trangThai`: `DA_PHAN_CONG` → **`DA_TIEP_NHAN`** ✅ đúng `srs-fr-05-vu-viec.md:822` + AC dòng 845
- `nguoiXuLyId` / `nguoiHoTroId` / `ngayPhanCong` = null (clear để phân công lại) ✅

→ **Backend ĐÚNG.** Lỗi ở giao diện: sau khi từ chối, tài khoản không còn là người được phân công nên lần đọc lại chi tiết trả 403 (đo được: `GET /vu-viecs/{id}` = 403), giao diện điều hướng sang màn 403 thay vì quay về danh sách.

### Ý 2 của đối tác — "trạng thái thành Chờ phê duyệt": KHÔNG tái hiện

| Mốc | Số VV ở CHO_PHE_DUYET |
|---|---|
| Baseline trước test (2026-07-20 03:47 UTC, admin) | **0** |
| Sau khi từ chối (tài khoản `cbnv_tw`, ảnh `05-cbnv-trang-thai-sau-tu-choi.png`) | **0** — tab "Chờ phê duyệt" không badge |

Trạng thái thực sau từ chối: VV-…-001 = "Đã tiếp nhận", -003 = "Đã tiếp nhận", cột Người xử lý = "—" → đúng SRS.

**Nhận định:** video đối tác — bản ghi bị từ chối là `VV-BTP-TW-…` (id `ab08db14…`, "Test file đính kèm vụ việc", 30/06) nhưng bản ghi duy nhất ở tab "Chờ phê duyệt" là `VV-BKH-20260526-001` (khác mã / khác DN / 26/05). Nhiều khả năng đối tác **đọc nhầm sang bản ghi khác**.

## Verdict

**`Open`** — theo §"1 case gộp nhiều lỗi con": ý 1 Open (tái hiện 2/2, sai `srs-fr-05-vu-viec.md:822/839/845`), ý 2 không tái hiện → verdict tổng lấy Open.

Bug ID: `BUG-XNTGHTVV_03` → [`../../bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md`](../../bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md)

## Bất thường ngoài tiêu chí BA (postmortem 16/07 mục C1)

Dựa trên ảnh đã mở đọc trong phiên này:

1. **Hộp thoại "Quản lý vai trò" (Quản trị hệ thống → Tài khoản & phân quyền) — bấm "Lưu vai trò" khi dropdown còn mở thì KHÔNG lưu và KHÔNG báo gì.** Lần bấm đầu không phát sinh request ghi nào (network chỉ có GET), vai trò giữ nguyên `["TVV"]`, không có thông báo lỗi/thành công. Phải đóng dropdown rồi bấm lại mới lưu được. **Chưa log thành bug** vì nằm ngoài luồng case tuần 3 và mới đo 1 lần — cần tái hiện lại có chủ đích trước khi mở dòng TC mới (§C2 "bug candidate ≠ bug"). Ghi lại ở đây để không rơi khỏi tầm nhìn.
2. Không phát hiện thêm bất thường nào khác trên các màn đã đi qua (danh sách VV, chi tiết VV, modal Từ chối, màn 403, danh sách tài khoản).
