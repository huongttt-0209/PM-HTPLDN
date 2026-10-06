# Bảng đối chiếu điều kiện — CNTTTVV_07 (row 83)

**Claim đối tác:** "Khi chọn **'Ở lại'** hệ thống **không giữ nguyên thông tin đã nhập trước đó**" — màn Sửa hồ sơ TVV, bấm Hủy khi có thay đổi chưa lưu.

## ⚠️ Ghi chú về evidence đối tác (minh bạch — đã báo user)

`partner-evidence/CNTTTVV_07.webm` (21.19s) — đã trích **11 khung full-res** (`reverify-audit/CNTTTVV_07/frames/`, t=2…21s) và xem hết:
- Toàn bộ video chỉ ghi cảnh cuộn xem **màn "Chỉnh sửa hồ sơ TVV"** của TVV `a25d37d7-1f66-47cd-849d-76e1fe00f087` ("Lê Hà Giang"), role CB_NV_TW, các trường có dữ liệu (SĐT 0158878587, email lehagiang@gmail.com…).
- **KHÔNG có khung nào chứa thao tác bấm "Hủy", hộp thoại xác nhận, hay trạng thái form sau khi chọn "Ở lại"** — video kết thúc ở t=21s khi đối tác bấm "Dừng chia sẻ", form vẫn còn dữ liệu.
- ⇒ **Video KHÔNG chứa khoảnh khắc lỗi.** Verdict dưới đây **KHÔNG** dựa trên suy đoán từ video, mà dựa **hoàn toàn vào việc QA tự chạy lại đúng các bước đối tác mô tả trên web** (§GATE — artifact quan sát real-data do QA tự tạo).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence + mô tả case) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) — thấy rõ ở góc phải video | `cbnv_tw` — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái (state machine) | Tư vấn viên đang ở màn **Chỉnh sửa hồ sơ** (`/chuyen-gia-tvv/{id}/chinh-sua`), hồ sơ có dữ liệu sẵn | Tư vấn viên `TVV-BTP-TW-0002` (98cfd963…, Đang hoạt động) tại màn **Chỉnh sửa hồ sơ** `/chuyen-gia-tvv/98cfd963…/chinh-sua`, hồ sơ có dữ liệu sẵn | Không |
| Dữ liệu tiền đề | Biểu mẫu có **thay đổi chưa lưu** (đối tác "Nhập dữ liệu hợp lệ" theo Các bước thực hiện) | Đã nhập dữ liệu hợp lệ, **thay đổi 2 trường**: Số điện thoại `0912280028` → `0909111222`; Địa chỉ `28 QA Test, Ha Noi` → `99 Pho Moi, Ha Noi` | Không |
| Input / filter | Bấm **Hủy** → hộp thoại → chọn **"Ở lại"** | Bấm **Hủy** → hộp thoại "Bạn có thay đổi chưa được lưu" → chọn **"Ở lại"** | Không |

**Kết luận:** 0 GAP → đủ điều kiện chốt verdict (bằng tái hiện thực tế của QA).

## Cổng 3 — SRS vs web (dạng gạch đầu dòng)

- **SRS** `srs-fr-04-chuyen-gia-tvv.md:1512` — SCR-IV-02 (màn Thêm mới / **Sửa hồ sơ TVV**) cell 7 "2 nút Hủy / Lưu": *"**Hủy: nếu có thay đổi chưa lưu → MD-XOA xác nhận.**"* — nghĩa là phải có bước xác nhận **trước khi** bỏ thay đổi.
- **SRS** `:1404` — MD-XOA: hộp thoại xác nhận, hành động chính = xác nhận bỏ/xóa. Cùng quy ước ở SCR-IV-03 cell 20a (`:1562`): *"Nếu có thay đổi chưa lưu → MD-XOA xác nhận; **click 'Đồng ý' → bỏ thay đổi**"* ⇒ thay đổi **chỉ được bỏ khi người dùng XÁC NHẬN**; nhánh không xác nhận (ở lại màn nhập liệu) phải **giữ nguyên dữ liệu đang nhập dở**, nếu không thì hộp xác nhận mất hoàn toàn ý nghĩa.
- **Web (18.143.165.120) — 3 bước đo được:**
  - **B1** (sau khi nhập, trước khi bấm Hủy): Số điện thoại = `0909111222`, Địa chỉ = `99 Pho Moi, Ha Noi`.
  - **B2** (ngay khi hộp thoại "Bạn có thay đổi chưa được lưu" hiện, **chưa bấm nút nào**): các trường **ĐÃ bị đưa về giá trị cũ** — Số điện thoại = `0912280028`, Địa chỉ = `28 QA Test, Ha Noi`.
  - **B3** (sau khi chọn **"Ở lại"**): vẫn ở màn nhập liệu (đúng), nhưng dữ liệu vừa nhập **đã mất** — Số điện thoại = `0912280028`, Địa chỉ = `28 QA Test, Ha Noi`.
- ⇒ ❌ **Sai SRS** `:1512` + `:1562`: thay đổi bị hủy **trước khi người dùng xác nhận**, và nhánh "Ở lại" không giữ được dữ liệu đang nhập ⇒ **tái hiện đúng claim đối tác** → `Open` (BUG-CNTTTVV_07).
- **Phát hiện thêm (quan trọng cho dev):** dữ liệu bị mất **ngay tại thời điểm bấm "Hủy"** (bước B2), **không phải** do nhánh "Ở lại" — nên dù người dùng chọn nhánh nào cũng đã mất dữ liệu. Trùng root cause với **BUG-QLTVV_22** (màn Thêm mới TVV) và **BUG-DKTGMLTVV_14** (màn Đăng ký tham gia mạng lưới).

**Artifact quan sát (do QA tự chạy trên data thật):**
- `bug-reports/image/BUG-CNTTTVV_07-web-01-da-nhap-du-lieu-truoc-khi-bam-huy.png` (B1 — thấy rõ `0909111222` + `99 Pho Moi, Ha Noi`).
- `bug-reports/image/BUG-CNTTTVV_07-web-02-hopthoai-hien-nhung-du-lieu-da-bi-revert.png` (B2 — hộp thoại đang mở, các trường đã về giá trị cũ).
- `bug-reports/image/BUG-CNTTTVV_07-web-03-sau-khi-bam-o-lai-mat-du-lieu.png` (B3 — sau "Ở lại", dữ liệu vừa nhập đã mất).

---

## RE-VERIFY 2026-07-15 (sau dev fix) — `Pass`

**Điều kiện re-test khớp bug gốc (0 GAP):** `cbnv_tw` (CB_NV_TW) · màn Chỉnh sửa TVV-BTP-TW-0002 `/chuyen-gia-tvv/98cfd963…/chinh-sua` · thay đổi 2 trường (SĐT `0912280028`→`0909111222`, Địa chỉ `28 QA Test, Ha Noi`→`99 Pho Moi, Ha Noi`).

**Chạy hết luồng trên web (đọc value input từng bước):**
- **B1** (sau nhập, trước Hủy): SĐT = `0909111222`, Địa chỉ = `99 Pho Moi, Ha Noi`.
- **B2** (ngay khi hộp thoại "Bạn có thay đổi chưa được lưu" hiện, CHƯA bấm nút nào): ✅ các trường **VẪN GIỮ** giá trị mới (`0909111222` / `99 Pho Moi, Ha Noi`) — **KHÔNG còn bị revert ngay** như vòng 1.
- **B3** (sau khi chọn **"Ở lại"**): ✅ vẫn ở màn nhập liệu, dữ liệu vừa nhập **CÒN NGUYÊN** (`0909111222` / `99 Pho Moi, Ha Noi`).

**Evidence:** `bug-reports/image/BUG-CNTTTVV_07-reverify-pass-o-lai-giu-du-lieu.png`.

**Kết luận:** thay đổi chỉ bị bỏ khi người dùng xác nhận; nhánh "Ở lại" giữ nguyên dữ liệu đang nhập — đúng SRS `:1512`/`:1562` → **Pass**. (Cùng root cause với BUG-QLTVV_22 / BUG-DKTGMLTVV_14 đã Pass — dev xử lý chung.)
