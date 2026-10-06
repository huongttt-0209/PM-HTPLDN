# Bảng đối chiếu điều kiện — DGTVV_05 (row 80)

**Claim đối tác:** "Không hiển thị thông báo lỗi khi bỏ trống **Vụ việc liên kết**" (case: kiểm tra thông báo lỗi khi bỏ trống trường bắt buộc, hộp thoại Gửi đánh giá).

**Evidence đã xem:** `partner-evidence/DGTVV_05.jpg` (full-res) — hộp thoại "Gửi đánh giá tư vấn viên" trên TVV `e4403bbf-7754-4ecf-a25f-59d6e4a39d4f` ("hương tv…", Đang hoạt động, **Chưa có đánh giá**), role CB_NV_TW. Frame chứa lỗi: sau khi bấm gửi với biểu mẫu trống, hiện **3 lỗi đỏ** — "Vui lòng chấm điểm chuyên môn / thái độ / đúng hạn"; ô "Vụ việc liên kết" (giá trị "Không có vụ việc liên kết") **KHÔNG có thông báo lỗi** và không có dấu `*`.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | `cbnv_tw` — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái (state machine) | Tư vấn viên "Đang hoạt động", **Chưa có đánh giá** | Tư vấn viên `TVV-SEED-0001` (5eed0003…), "Đang hoạt động", **Chưa có đánh giá** (0 đánh giá, khối tổng hợp "—/5") | Không |
| Dữ liệu tiền đề | Hộp thoại Gửi đánh giá mở từ thẻ Đánh giá; dropdown Vụ việc rỗng ("Không có vụ việc liên kết") | Giống hệt — dropdown Vụ việc rỗng ("Không có vụ việc liên kết") | Không |
| Input / filter | Bấm "Gửi đánh giá" khi **để trống toàn bộ** biểu mẫu | Bấm "Gửi đánh giá" khi **để trống toàn bộ** biểu mẫu | Không |

**Kết luận:** 0 GAP → đủ điều kiện chốt verdict.

## Cổng 3 — SRS vs web (dạng gạch đầu dòng)

- **SRS** `srs-fr-04-chuyen-gia-tvv.md:702` — FR-IV-09 (UC47) §Inputs #2: `vu_viec_id` | identifier | **Bắt buộc = N** | "Vụ việc liên kết" | user input. ⇒ Vụ việc liên kết là trường **KHÔNG bắt buộc**.
- **SRS** `srs-fr-04-chuyen-gia-tvv.md:1573` — SCR-IV-03 cell 24 (Form đánh giá mới): "**Tư vấn viên \*** (tự điền), **Vụ việc liên kết (chọn)**, 3 ô chấm sao 1–5: Chuyên môn / Thái độ / Đúng hạn…" ⇒ chỉ "Tư vấn viên" có dấu `*`; "Vụ việc liên kết" **không** có dấu bắt buộc.
- **SRS** `:703-705` — 3 điểm (diem_chuyen_mon / diem_thai_do / diem_thoi_gian): **Bắt buộc = Y**.
- **Web (18.143.165.120):** bấm gửi khi biểu mẫu trống → hệ thống **CHẶN gửi** (hộp thoại giữ nguyên) và hiển thị **đúng 3 thông báo lỗi** cho 3 trường bắt buộc: "Vui lòng chấm điểm chuyên môn" · "Vui lòng chấm điểm thái độ" · "Vui lòng chấm điểm đúng hạn". Kiểm tra DOM: "Vụ việc liên kết" có `required = false`, 3 trường điểm `required = true`.
- ⇒ **Web ĐÚNG SRS**: có hiển thị thông báo lỗi cho các trường bắt buộc (đáp ứng "Kết quả mong đợi" của case là "Hệ thống hiển thị thông báo lỗi"); không báo lỗi cho "Vụ việc liên kết" vì trường này **không bắt buộc** theo SRS.
- ⇒ Đối tác **quan sát đúng thực tế** (web không báo lỗi ở Vụ việc liên kết) nhưng **kỳ vọng trường này là bắt buộc** — trái SRS → bất đồng **ĐẶC TẢ** → `BA confirm` (KHÔNG Reject, theo bảng Verdict).

**Artifact quan sát:** `reverify-audit/DGTVV_05/web-modal-3-loi-bat-buoc-vuviec-khong-bat-buoc.png` (full-res — loại claim = Validation: input trống → rule → message; thấy rõ 3 message lỗi + ô Vụ việc liên kết không có `*` và không có lỗi).
