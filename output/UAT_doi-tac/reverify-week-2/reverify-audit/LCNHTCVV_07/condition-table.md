# LCNHTCVV_07 — Bảng đối chiếu điều kiện

**Case:** Phân công vụ việc **không thuộc đơn vị người dùng** — thông báo từ chối (FR-V.I-09 UC59 §Error Handling E4).

**Evidence đối tác:** `partner-evidence/LCNHTCVV_07.jpg` — **CÓ khoảnh khắc lỗi**.
Full-res: URL `htpldn-uat.ospgroup.vn/vu-viec/aaff0000-...-000000000001`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"**.
Cửa sổ Phân công (thẻ "Tổ chức tư vấn"): đã chọn TC `TC-BTP-TW-0004 — Đoàn Luật sư Hà Nội` + TVV `huongcg (TVV-BTP-TW-0030)`, bấm Xác nhận.
Kết quả: **2 thông báo lỗi ĐỎ GIỐNG HỆT NHAU** xếp chồng: **"Đơn vị của người phê duyệt khác đơn vị của bản ghi"** (×2).

**Đối tác phản ánh:** (1) thông báo **không đúng thiết kế**; (2) thông báo **bị lặp (duplicate)**.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header ảnh "Cán bộ NV Trung ương / CB_NV_TW" | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" (đúng vai trò + cấp) | Không |
| Quan hệ đơn vị (điều kiện CỐT LÕI của case) | VV **KHÔNG thuộc đơn vị** của người đăng nhập (token `donViId` = đơn vị TW ≠ đơn vị của bản ghi) | `VV-STP-AG-20260712-001` thuộc **Sở Tư pháp An Giang**, người thao tác `cbnv_tw` thuộc **đơn vị Trung ương** (token `donViId=00000000-...-0001`, `capDonVi=TW`) ⇒ **VV thuộc đơn vị KHÁC** — đúng điều kiện case | Không |
| Entity + trạng thái (state machine) | VV ở trạng thái cho phép phân công (thanh hành động có [Phân công] + [Kiểm tra lại]) | `VV-STP-AG-20260712-001` — trạng thái **"Đang kiểm tra"**, checklist 6/6 ✓ ⇒ nút [Phân công] hiển thị, mở được cửa sổ | Không |
| Input (đã chọn đủ người rồi mới bấm Xác nhận) | Đã chọn Tổ chức + TVV cụ thể rồi mới Xác nhận | Đã chọn người được phân công (`[TVV] QA TVV Seed28 Active`) rồi mới bấm **[Xác nhận]** → có gọi API thật (không phải lỗi validate rỗng) | Không |

## Quan sát (real-data) — cbnv_tw phân công VV của Sở Tư pháp An Giang

**Vòng 1 (bug gốc):**
```json
{"so_toast_hien_ra": 2,
 "noi_dung_toast": "Đơn vị của người phê duyệt khác đơn vị của bản ghi (×2)"}
```

**Re-test 2026-07-15 (sau dev fix) — MutationObserver đếm .ant-message-notice-wrapper:**
```json
{"so_toast_hien_ra": 1,
 "toast_type": "error",
 "noi_dung_toast": "Bạn không có quyền phân công vụ việc của đơn vị khác",
 "trang_thai_VV_sau_thao_tac": "Đang kiểm tra (KHÔNG đổi — chặn đúng)"}
```
→ **PASS:** message đổi sang đúng thao tác (phân công vụ việc), tiếng Việt thuần, bỏ jargon "bản ghi"/"người phê duyệt"; và **chỉ hiện 1 lần**.

Log: `retest-observer-log.json` · Ảnh: `../../bug-reports/image/BUG-LCNHTCVV_07-retest-thongbao-dung-vaitro-1lan.png`

## Đối chiếu SRS (Cổng 3) — tách 2 ý

### Ý A — Nội dung thông báo sai so với SRS → Open

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:773` (FR-V.I-09 / UC59 §Error Handling, dòng E4): điều kiện *"VV không thuộc đơn vị user"* → hệ thống phải phản hồi: **"Bạn không có quyền phân công VV của đơn vị khác"** (severity ERROR).
- **Thực tế web:** thông báo là **"Đơn vị của người phê duyệt khác đơn vị của bản ghi"**.
- **Sai 2 điểm:**
  1. **Sai vai trò / sai nghiệp vụ:** thao tác đang thực hiện là **phân công** do **Cán bộ Nghiệp vụ** làm, KHÔNG phải phê duyệt — nhưng thông báo lại nói về *"người phê duyệt"* ⇒ cán bộ đọc không hiểu mình sai ở đâu.
  2. **Không nêu được yêu cầu nghiệp vụ:** SRS yêu cầu thông báo nói rõ *người dùng không có quyền phân công vụ việc của đơn vị khác*; câu hiện tại chỉ mô tả kỹ thuật ("đơn vị của bản ghi").

### Ý B — Thông báo lặp 2 lần → Open

- Cùng 1 lần bấm [Xác nhận] → **2 toast giống hệt nhau** hiện chồng lên nhau (xác nhận bằng MutationObserver: `so_toast_hien_ra = 2`), trong khi backend chỉ trả **1** response 403.
- Trùng khớp hiện tượng đối tác quay được (2 toast đỏ y hệt trong ảnh).

**Kết luận:** **Open** (cả 2 ý đều tái hiện). Phần **chặn** thao tác là **đúng** (trạng thái VV không đổi) — lỗi nằm ở **nội dung thông báo** và **hiển thị lặp**.

> **Cùng gốc với `BUG-KTHSYCHTPL_15`** (đã log ở lô trước: cán bộ khác đơn vị kiểm tra hồ sơ → thông báo cũng sai vai trò "người phê duyệt" + cũng lặp 2 lần). Đề nghị dev fix chung 1 lần cho toàn bộ thông báo chặn theo đơn vị (mã `ERR-AUTH-VPD-00-03`).
