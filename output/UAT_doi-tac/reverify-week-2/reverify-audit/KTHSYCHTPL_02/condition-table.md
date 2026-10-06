# KTHSYCHTPL_02 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra hiển thị vùng tiêu đề và thanh tiến trình (SCR-V.I-03).
**Evidence đối tác:** `partner-evidence/KTHSYCHTPL_02.webm` — frame 00m25s (màn Chi tiết vụ việc `VV-QA-R9-DVC-001`, badge "Đã tiếp nhận", stepper 10 bước).
**Đối tác phản ánh 2 ý:**
1. Các bước đã hoàn thành không có dấu tích.
2. Mức cảnh báo quá hạn không giống với thiết kế — ghi chú của đối tác: *"cảnh báo quá hạn nhấp nháy và màu chữ gần như chìm vào nền, rất khó nhìn"*.

**Verdict tổng:** **Open** — cả 2 ý đều là lỗi thật (BUG-KTHSYCHTPL_02 + BUG-KTHSYCHTPL_02b).

---

## Ý 1 — Bước đã hoàn thành không có dấu ✓ → **Open**

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW — header hiện "Cán bộ NV Trung ương / CB_NV_TW" (frame 00m25s) | `cbnv_tw` — header hiện "CB Nghiệp vụ - Trung ương / CB_NV_TW" | Không |
| Entity + trạng thái (state machine) | VV-QA-R9-DVC-001 — trạng thái "Đã tiếp nhận"; stepper highlight bước 3 | VV-BTP-TW-20260712-003 — trạng thái "Đã tiếp nhận"; stepper highlight bước 3 | Không |
| Dữ liệu tiền đề (số bước đã hoàn thành trên stepper) | 2 bước trước ("Mới tạo", "Chờ tiếp nhận") ở trạng thái đã hoàn thành | 2 bước trước ("Mới tạo", "Chờ tiếp nhận") ở trạng thái đã hoàn thành (`ant-steps-item-finish`) | Không |

### Quan sát (real-data)

DOM stepper trên web QA — 2 bước đã hoàn thành có class `ant-steps-item-finish` nhưng ô icon RỖNG, không có `.ant-steps-finish-icon` / `.anticon-check` / `svg`:

```json
[{"title":"Mới tạo","state":"ant-steps-item-finish","iconOuter":"<div class=\"ant-steps-item-icon ant-wave-target\"></div>","hasCheckIcon":false},
 {"title":"Chờ tiếp nhận","state":"ant-steps-item-finish","iconOuter":"<div class=\"ant-steps-item-icon ant-wave-target\"></div>","hasCheckIcon":false},
 {"title":"Đã tiếp nhận","state":"ant-steps-item-process ant-steps-item-active","hasCheckIcon":false}]
```

Ảnh: `../../bug-reports/image/BUG-KTHSYCHTPL_02-web-stepper-buoc-hoan-thanh-khong-co-dau-tich.png`

### Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:1718` (SCR-V.I-03, Thành phần row 3 — Thanh tiến trình): "Bước hiện tại nổi bật, **hoàn thành có dấu ✓**".
- **Thực tế web** — bước hiện tại CÓ nổi bật; bước đã hoàn thành chỉ là chấm tròn, KHÔNG có dấu ✓.
- **Kết luận** — **THIẾU dấu ✓** → **Open** (BUG-KTHSYCHTPL_02).

---

## Ý 2 — Mức cảnh báo quá hạn (nhấp nháy + chữ chìm vào nền) → **Open**

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ (evidence KTHSYCHTPL_11 cùng lô: "CB NV DP 01 (AG) / CB_NV_DP") | `cbnv_dp` — header "CB Nghiệp vụ - Địa phương / CB_NV_DP" | Không |
| Entity + trạng thái (state machine) | Vụ việc **chưa kết thúc** (còn đang chạy SLA) — `VV-QA-R7-SLA-QHNT` | VV-STP-AG-20260712-002 ("Đã tiếp nhận") + VV-STP-AG-20260712-001 ("Đang kiểm tra") — đều chưa kết thúc | Không |
| Dữ liệu tiền đề (**mức cảnh báo SLA**) | Mức **Quá hạn nghiêm trọng** — tên vụ việc đối tác dùng là `...SLA-QHNT` (Quá Hạn Nghiêm Trọng) | Đã đạt **307% thời hạn đã dùng** ⇒ đúng mức "Quá hạn nghiêm trọng" (>200%). Bổ sung mốc 167% để đối chiếu mức "Quá hạn" (>100%) | Không |
| Màn hình quan sát | Cột cảnh báo thời hạn | Cột **"Cảnh báo thời hạn"** màn Danh sách vụ việc (SCR-V.I-01 cell 20) | Không |

### Ghi chú minh bạch về cách tạo tiền đề "quá hạn"

Đã dò **toàn bộ** đường tạo dữ liệu và **không có bất kỳ đường nào** cho phép tạo vụ việc quá hạn:

- **Form "Nhập thủ công" trên web** → không có trường "Ngày tiếp nhận" (đã log riêng: BUG-NHSYC_02).
- **`POST /api/v1/vu-viecs/manual`** → hợp đồng API (`CreateVuViecThuCongDto`) **không có** `ngayTiepNhan` / `deadline`. Gửi kèm 2 trường này → BE bỏ qua, luôn tự tính = NOW + N ngày làm việc.
- **`PATCH /api/v1/vu-viecs/{id}`** → `UpdateVuViecDto` chỉ nhận `tieuDe` / `moTa` / `vuViecVuongMac` / `version` — **không có** trường ngày.
- **`POST /vu-viecs/{id}/tiep-nhan` · `tiep-nhan-dvc` · `tiep-nhan-he-thong`** → đều **không có** trường ngày trong hợp đồng API.
- **`POST /vu-viecs/{id}/mo-lai`** (mở lại VV đã kết thúc, hạn cũ đã quá) → bị chặn: *"Chỉ có thể mở lại vụ việc ở trạng thái TU_CHOI"*.
- **Đổi cấu hình SLA** (Cấu hình hệ thống → Thời hạn xử lý) → ràng buộc `thoiHanNgay ≥ 1` ⇒ hạn luôn ở **tương lai**. Đổi cấu hình **không** tính lại hạn của bản ghi đã có (đã thử 15 → 14 → hạn cũ giữ nguyên; đã khôi phục về **15**).
- **Bản ghi sẵn có trong env** → 16 vụ việc: 4 bản quá hạn nhưng **đã kết thúc** (hiện "Đã hoàn thành"), 3 bản đang xử lý nhưng **chưa có hạn** (`deadline: null`) ⇒ không bản nào rơi vào mức "Quá hạn".

⇒ **Phương án đã dùng:** giữ nguyên **bản ghi thật** và **hạn thật do máy chủ sinh** (12/07/2026 → 31/07/2026), chỉ **tua đồng hồ của trình duyệt** tới 14/08/2026 rồi 15/09/2026. Mức cảnh báo được giao diện tính **hoàn toàn từ giờ máy trạm**, nên đây đúng là những gì người dùng thật thấy khi mở màn hình vào ngày đó — không sửa dữ liệu, không giả lập phản hồi API. Sau khi chụp xong đã **tải lại trang, đồng hồ về thực** (thẻ trở lại "Còn 15 ngày LV", nền xanh).

### Quan sát (real-data) — cột "Cảnh báo thời hạn", VV-STP-AG-20260712-001/-002

```json
{"mốc thật (12/07/2026, 0% thời hạn)":
   {"nhãn":"Còn 15 ngày LV","nền":"rgb(35,120,4)","nhấp nháy":"none"},
 "mốc 14/08/2026 (167% — mức Quá hạn)":
   {"nhãn":"Quá hạn 10 ngày LV","nền":"rgb(207,19,34)","chữ":"rgb(255,255,255)","nhấp nháy":"none"},
 "mốc 15/09/2026 (307% — mức Quá hạn nghiêm trọng)":
   {"nhãn":"Quá hạn 31 ngày LV","nền":"rgb(0,0,0)","chữ":"rgb(255,255,255)",
    "nhấp nháy":"sla-blink 1s ease-in-out infinite",
    "keyframes":"0%,100% { opacity: 1 }  50% { opacity: 0.2 }"}}
```

Đo độ đậm (opacity) thực tế của thẻ trong 1,2 giây — 13 mẫu cách nhau 100ms:

```json
[1.00, 0.96, 0.80, 0.53, 0.30, 0.20, 0.24, 0.40, 0.69, 0.91, 1.00, 0.96]
```

⇒ Thẻ dao động **1.0 → 0.20 → 1.0 mỗi giây, không dừng**. Tại đáy nhịp, thẻ chỉ còn ~20% độ đậm → **chữ trắng gần như chìm hẳn vào nền trang**.

Ảnh:
- Đáy nhịp (chữ chìm vào nền): `../../bug-reports/image/BUG-KTHSYCHTPL_02b-web-canhbao-quahan-nghiemtrong-nhapnhay-chim-vao-nen.png`
- Pha hiện rõ (nền đen) để đối chiếu: `../../bug-reports/image/BUG-KTHSYCHTPL_02b-web-canhbao-quahan-nghiemtrong-pha-hien-ro.png`

> **Ghi chú về cách chụp:** ảnh được chụp bằng cách **tạm dừng chính hiệu ứng nhấp nháy của sản phẩm** tại 2 pha (đáy 0.216 và đỉnh 0.993) — không chỉnh sửa màu, không thêm/bớt style. Không tạm dừng thì mỗi ảnh rơi vào một pha ngẫu nhiên và không thể hiện được biên độ nháy.

### Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:1494-1501` (§Mức cảnh báo thời hạn) định nghĩa 4 mức và **chỉ phân biệt bằng MÀU**: `BINH_THUONG` Xanh lá · `SAP_HET` Vàng · `QUA_HAN` **Đỏ** · `QUA_HAN_NGHIEM_TRONG` **Đen**. `:1638` (SCR-V.I-01 cell 20 — cột "Cảnh báo SLA") cũng chỉ ghi "4 mức màu 🟢/🟡/🔴/⚫". `BR-SLA-02` (`:2416`) định nghĩa 4 mức theo % thời hạn. **Không dòng SRS nào quy định hiệu ứng nhấp nháy / làm mờ.**
- `:1646` — "SLA cảnh báo tính realtime... **Ngưỡng cấu hình qua MH-10.7 tab SLA (UC108)**" ⇒ ngưỡng phải đọc từ cấu hình SLA.
- **Thực tế web:**
  1. Mức **Quá hạn** (167%): nền đỏ `rgb(207,19,34)`, không nhấp nháy → **đúng thiết kế**.
  2. Mức **Quá hạn nghiêm trọng** (307%): nền đen (màu đúng) nhưng **bị gắn thêm hiệu ứng nhấp nháy vô hạn**, đáy nhịp mờ còn ~20% ⇒ **chữ chìm vào nền, rất khó đọc** — đúng hiện tượng đối tác phản ánh. Đây là thứ SRS **không** yêu cầu, và nó phá yêu cầu cơ bản là cảnh báo phải đọc được.
  3. **Ngưỡng cảnh báo bị cố định trong giao diện** (50% / 100% / 200%) thay vì đọc từ cấu hình SLA ⇒ quản trị viên đổi "Ngưỡng cảnh báo 1/2" hoặc "Hệ số quá hạn" thì giao diện **không đổi theo**, trái `:1646`.

**Kết luận ý 2:** **Open** (BUG-KTHSYCHTPL_02b). Phản ánh của đối tác **chính xác**, không phải tranh chấp đặc tả.
