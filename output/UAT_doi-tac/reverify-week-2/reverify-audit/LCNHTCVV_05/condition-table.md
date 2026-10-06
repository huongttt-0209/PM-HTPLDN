# LCNHTCVV_05 — Bảng đối chiếu điều kiện

**Case:** Giới hạn số ký tự tối đa của trường "Ghi chú" trong cửa sổ Phân công (FR-V.I-09 UC59 §Inputs).

**Evidence đối tác:** `partner-evidence/LCNHTCVV_05.jpg` — **CÓ khoảnh khắc lỗi**.
Full-res: URL `htpldn-uat.ospgroup.vn/vu-viec/71cb2ab1-...`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"**.
Cửa sổ **"Phân công tư vấn viên"**, thẻ **"Tổ chức tư vấn"** đang chọn (có 2 trường: "Tổ chức tư vấn" + "Tư vấn viên của tổ chức").
Ô **"Ghi chú"** đã nhập chuỗi dài lặp lại; nội dung **bị cắt cụt giữa chừng** ("... Xem chi tiếtdd"), không có bộ đếm ký tự.

**Đối tác phản ánh:** Ghi chú phân công phải cho **tối đa 1.000 ký tự**, nhưng hệ thống **giới hạn 500 ký tự**.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header ảnh "Cán bộ NV Trung ương / CB_NV_TW" | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" (đúng vai trò + cấp) | Không |
| Entity + trạng thái (state machine) | VV có nút [Phân công] + [Kiểm tra lại] ⇒ **"Đang kiểm tra"** (đã kết luận Đạt) | `VV-BTP-TW-20260712-005` (cùng đơn vị TW) — seed sang **"Đang kiểm tra"** (Kiểm tra hồ sơ 6/6 Đạt) ⇒ mở đúng cửa sổ Phân công | Không |
| Thẻ đang chọn trong cửa sổ (Cá nhân vs Tổ chức) | Thẻ **"Tổ chức tư vấn"** | Đã đo **CẢ 2 thẻ**: thẻ "Cá nhân" **và** thẻ "Tổ chức tư vấn" (thẻ trong ảnh đối tác) — cùng 1 ô Ghi chú, cùng giới hạn | Không |
| Input / cách nhập (gõ vs dán) | Nhập chuỗi dài lặp lại vào ô Ghi chú | Dán **700 ký tự** rồi gõ thêm **400 ký tự** nữa (đường đi của gõ/dán thật — trình duyệt áp `maxlength`) | Không |

## Quan sát (real-data) — cbnv_tw, ô "Ghi chú" trong cửa sổ Phân công

**Vòng 1 (bug gốc):**
```json
{"maxlength": 500, "bo_dem_ky_tu": "KHÔNG có", "ket_luan": "chặn cứng 500 ký tự"}
```

**Re-test 2026-07-15 (sau dev fix):**
```json
{"thuoc_tinh_maxlength": 1000,
 "bo_dem_ky_tu": "CÓ — hiển thị '0 / 1000'",
 "thu_nghiem_go_that": "Gõ bằng bàn phím 570 ký tự → ô nhận đủ 570 (>500), counter '570 / 1000' → cap 500 đã bỏ",
 "ket_luan": "nhận tối đa 1000 ký tự + có bộ đếm"}
```
→ **PASS:** Ghi chú phân công nay tối đa 1000 ký tự (maxlength=1000) + có counter; gõ thật vượt 500 OK.

Ảnh: `../../bug-reports/image/BUG-LCNHTCVV_05-retest-ghichu-1000-kytu-co-counter.png`

## Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:720` (FR-V.I-09 / UC59 §Inputs, dòng 5): trường **`ghi_chu_phan_cong`** — ràng buộc: ***"max 1000 ký tự**, lưu vào PHAN_CONG_VU_VIEC.ghi_chu"*.
- **Thực tế web:** ô "Ghi chú" đặt `maxlength = 500` ⇒ chặn cứng ở **500 ký tự** (dán 700 → còn 500; gõ thêm → không nhận). Áp dụng cho **cả 2 thẻ** "Cá nhân" và "Tổ chức tư vấn".
- **Đối chiếu:** SRS nêu **RÕ con số giới hạn** (1000) mà web đặt **đúng một nửa** (500) ⇒ vi phạm ràng buộc Inputs → **Open** (không phải BA confirm — SRS không im lặng, đã ghi rõ số).

**Kết luận:** **Open**. Web giới hạn Ghi chú phân công **500 ký tự** thay vì **1.000 ký tự** theo SRS dòng 720. Kỳ vọng của đối tác **trùng khớp SRS**.

> Ghi nhận thêm (không tách bug riêng, gộp vào bug này): ô "Ghi chú" **không có bộ đếm ký tự**, nên khi bị cắt ở 500 người dùng không nhận được phản hồi nào — chính là hiện tượng "chữ bị cắt cụt giữa chừng" trong ảnh đối tác.
