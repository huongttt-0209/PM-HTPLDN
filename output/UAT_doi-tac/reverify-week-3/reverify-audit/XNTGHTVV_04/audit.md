# Audit — XNTGHTVV_04 (row 3) · Chấp nhận tham gia hỗ trợ vụ việc

## Cổng 1 — Bằng chứng (ĐÓNG)

- File: `partner-evidence/XNTGHTVV_04.webm` (9.79 MB), `fetch_evidence.py --row 3` exit 0.
- Frames full-res: `frames/t000.00s → t024.10s.jpg` (7 frame, đã mở đọc từng ảnh).
- Frame chứa LỖI: **t024.10s**.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị đọc từ frame |
|---|---|---|
| (a) | URL / ID bản ghi | `htpldn-uat.ospgroup.vn/vu-viec/9ed9d021-f308-40cc-b4d7-b60b80fbc1dd` — mã **VV-BTP-TW-20260709-001**, tiêu đề "TKM kiểm thử chức năng nhập thủ công", lĩnh vực Thuế, ngày tiếp nhận 10/07/2026 08:45, deadline 31/07/2026 |
| (b) | Trạng thái entity đối tác đang đứng | **Đã phân công** (t008, đủ 2 nút [Chấp nhận] [Từ chối]) → sau thao tác thành **Đang xử lý** (t012, xuất hiện [Cập nhật kết quả] [Trình phê duyệt]) |
| (c) | Dữ liệu tiền đề | Account `huongcg`, vai trò **TVV · CG**, đơn vị **BTP · TW**. Trường "Người tiếp nhận" = **Cán bộ NV Trung ương** — đối tác **bôi đen nhấn mạnh** (t008) để chỉ ra ai đáng lẽ phải nhận thông báo |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `XNTGHTVV_04.webm`, frame **t008.03s** (VV Đã phân công, con trỏ tiến về nút Chấp nhận, "Người tiếp nhận: Cán bộ NV Trung ương" được bôi đen) → **t012.04s** (chấp nhận xong, VV chuyển **Đang xử lý**, đối tác mở menu tài khoản → Đăng xuất) → **t016.05s** (đăng nhập lại bằng chính `cbnv_tw`) → frame chứa lỗi **t024.10s**: dashboard `cbnv_tw` (CB_NV_TW), mở chuông Thông báo — 5 mục mới nhất là "Tài khoản vừa đăng nhập ở nơi khác" ×2 và "Câu hỏi đã quá hạn xử lý" ×3, **không có mục nào về vụ việc vừa được chấp nhận**.
2. **Đối tác phản ánh CỤ THỂ:** thao tác Chấp nhận chạy đúng (state + bản ghi + Nhóm 6 đều OK), **nhưng cán bộ nghiệp vụ phụ trách hồ sơ KHÔNG nhận được thông báo**.
3. **Data + bước tái hiện:** login TVV được phân công → Vụ việc HTPL → mở VV trạng thái Đã phân công → [Chấp nhận] → xác nhận → đăng xuất → login CB NV phụ trách (`cbnv_tw`) → mở chuông Thông báo.

### Diễn biến theo timeline video

| Frame | Quan sát |
|---|---|
| t000.00s (08:48) | Danh sách VV của `huongcg` (TVV·CG, BTP·TW): "Tất cả 5", chuông 19. Cột Người xử lý = `huongcg` ở mọi dòng |
| t008.03s | Chi tiết VV-BTP-TW-20260709-001, **Đã phân công**, 2 nút [Chấp nhận] [Từ chối]. **"Người tiếp nhận: Cán bộ NV Trung ương" bị bôi đen** — đối tác chỉ đích danh người phải nhận thông báo |
| t012.04s | Sau chấp nhận: **Đang xử lý**, nút đổi thành [Cập nhật kết quả] [Trình phê duyệt] → thao tác THÀNH CÔNG. Mở menu tài khoản → Đăng xuất |
| t016.05s | Màn login, điền `cbnv_tw` |
| t020.07s | Nhập OTP gửi tới `cbn***@htpldn.gov.vn` |
| **t024.10s (08:48)** | **Dashboard `cbnv_tw` (CB_NV_TW), mở chuông: 5 mục mới nhất KHÔNG có thông báo nào về vụ việc** |

## Cổng 3 — Đối chiếu SRS (v3.5)

| SRS yêu cầu (dẫn line) | Thực tế web đối tác | Đủ/Thiếu |
|---|---|:-:|
| `srs-fr-05-vu-viec.md:821` — FR-V.I-10 (UC 60) Processing bước 2: "Nếu CHAP_NHAN: chuyển VV → DANG_XU_LY" | VV chuyển đúng sang Đang xử lý (t012) | ✅ Đủ |
| `srs-fr-05-vu-viec.md:823` — Processing bước 4: "Cập nhật PHAN_CONG_VU_VIEC" | Bản ghi phân công cập nhật (kiểm trên env: trạng thái → CHAP_NHAN) | ✅ Đủ |
| `srs-fr-05-vu-viec.md:824` — Processing bước **5: "Gửi thông báo CB NV"** | Chuông `cbnv_tw` không có mục nào về vụ việc (t024) | ❌ **Thiếu** |
| `srs-fr-05-vu-viec.md:833` — Postconditions: "**CB NV nhận thông báo**" | Không nhận | ❌ **Thiếu** |
| `srs-fr-05-vu-viec.md:2455` — BR-NOTIF-01: "Mọi sự kiện workflow (phân công, **xác nhận**, từ chối, phê duyệt...) đều gửi thông báo cho người liên quan qua **2 kênh: in-app (THONG_BAO) + email**" (áp dụng FR-V.I-10 theo dòng 2326) | Không có cả in-app lẫn email | ❌ **Thiếu cả 2 kênh** |
| `srs-fr-05-vu-viec.md:844` — AC: "Given người được phân công xác nhận When chấp nhận Then VV → DANG_XU_LY" | Đạt | ✅ Đủ |

## Bảng đối chiếu điều kiện

→ [`../../cond/XNTGHTVV_04.md`](../../cond/XNTGHTVV_04.md) — **0 GAP**.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

Vụ việc **VV-BTP-TW-20260712-001**, tài khoản `qa_tvvseed28` (TVV·CG, BTP·TW), CB NV phụ trách `cbnv_tw`.

### Phần CHẠY ĐÚNG (khớp KQMĐ của đối tác)

| KQMĐ | Thực tế | Kết quả |
|---|---|:-:|
| Chuyển "Đã phân công" → "Đang xử lý" | `trangThai` = `DANG_XU_LY`, stepper bước 6 | ✅ |
| Cập nhật bản ghi phân công | `trangThai` = `CHAP_NHAN`, `ngayCapNhat` = 04:30:32Z | ✅ |
| Mở Nhóm 6 "Kết quả hỗ trợ" | Accordion "Kết quả hỗ trợ" xuất hiện + nút [Cập nhật kết quả] | ✅ |
| Hiển thị thông báo cho người thao tác | Toast "Đã chấp nhận phân công" | ✅ |

Ảnh: `11-truoc-khi-chap-nhan.png` · `13-modal-xac-nhan-chap-nhan.png` · `14-ngay-sau-xac-nhan-chap-nhan.png`.

### Phép đo (tools/toast-capture.js — không lọc trùng, đọc innerText, đếm request)

Tự kiểm observer: `soObserverDangSong = 1` → số liệu hợp lệ.

| Chỉ số | Giá trị |
|---|---|
| SO_REQUEST_GHI | **1** — `POST /api/v1/vu-viecs/{id}/nhan-phan-cong` |
| SO_KHUNG_THONG_BAO | **1** — "Đã chấp nhận phân công" |
| BI_LAP | false |

→ Thao tác gọi máy chủ đúng 1 lần, không lặp thông báo.

### Phần SAI — thông báo cho CB NV phụ trách

| Kênh | Trước thao tác (baseline 04:28:38Z) | Sau thao tác (04:33Z) | Kết quả |
|---|---|---|:-:|
| In-app (THONG_BAO) của `cbnv_tw` | 117 thông báo · 0 mục loại `VU_VIEC` | **117** thông báo · **0** mục loại `VU_VIEC` · **0** mục tạo sau 04:30:00Z | ❌ Không gửi |
| Email (MailHog) | 311 thư, thư mới nhất 04:29:04Z (OTP) | 312 thư, thư mới nhất **vẫn là** OTP 04:29:04Z — không thư nào sau mốc chấp nhận 04:30:32Z | ❌ Không gửi |

Ảnh: `bug-reports/image/BUG-XNTGHTVV_04-chuong-thong-bao-cbnv.png` — chuông `cbnv_tw` sau thao tác, 5 mục mới nhất đều "Tài khoản vừa đăng nhập ở nơi khác" (41 phút trước / 3 ngày trước), không có mục vụ việc.

**Loại trừ khả năng sai người nhận:** `VU_VIEC.nguoiTiepNhanId` = `f2e93500-f6dd-4660-a3f6-de7326acffd1`, trùng đúng `nguoiNhanId` trên các thông báo của chính tài khoản `cbnv_tw` → `cbnv_tw` ĐÚNG là CB NV phụ trách hồ sơ.

**Loại trừ khả năng hệ thống thông báo hỏng toàn cục:** cùng phiên, sự kiện **phân công** (FR-V.I-09 bước 7) gửi email thành công tới `qa.tvvseed28@htpldn-uat.local` lúc 04:27:03. Vậy hạ tầng gửi thông báo/email vẫn chạy; chỉ sự kiện **xác nhận tham gia** không phát thông báo.

## Verdict

**`Open`** — tái hiện đúng điểm đối tác báo, thiếu cả 2 kênh mà `srs-fr-05-vu-viec.md:2455` yêu cầu, vi phạm Processing bước 5 (dòng 824) + Postcondition (dòng 833).

Bug ID: `BUG-XNTGHTVV_04` → [`../../bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md`](../../bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md)

## Bất thường ngoài tiêu chí BA (postmortem 16/07 mục C1)

Phát hiện trong lúc dựng tiền đề cho case này, đã tái hiện có chủ đích, log thành bug riêng:

1. **`BUG-VV-PHANCONGLAI`** — vụ việc bị TVV từ chối quay về "Đã tiếp nhận" nhưng KHÔNG phân công lại được: màn chi tiết chỉ có nút [Kiểm tra hồ sơ], không có [Phân công]; gọi API trực tiếp cũng bị chặn 409 `ERR-STATE-VI-PC-01`. Trái `srs-fr-05-vu-viec.md:1734` (bảng nút: "DA_TIEP_NHAN (phân công lại sau khi bị từ chối) → [Phân công]") + dòng 832.
2. **`BUG-VV-LICHSU-THATBAI`** — request phân công **thất bại** vẫn ghi thêm bản ghi vào Dòng thời gian / lịch sử vụ việc. Tái hiện có kiểm soát: gọi POST phân công khi VV đang ở `DA_PHAN_CONG` → HTTP **409**, nhưng số bản ghi lịch sử tăng **19 → 20**, bản ghi mới `hanhDong: PHAN_CONG`, `duLieuMoi: null`. Trái `srs-fr-05-vu-viec.md:750` (ghi lịch sử là bước 8, sau khi tạo bản ghi + đổi trạng thái thành công) — hệ quả là dòng thời gian của vụ việc này có 14 mục "Phân công" trong khi chỉ 1 lần phân công thật sự thành công.

3. Nghi vấn ở case trước ("Lưu vai trò" bấm lần đầu không ăn) — phiên này gặp lại đúng hiện tượng khi tôi dùng `.click()` DOM lên option của Ant Design Select: React không nhận sự kiện. Khi chuyển sang click thật qua công cụ thì ăn ngay. → **Kết luận: KHÔNG phải lỗi ứng dụng**, là hạn chế của cách tôi thao tác. Đóng nghi vấn, không log bug.
