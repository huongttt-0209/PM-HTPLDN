# Bảng đối chiếu điều kiện — DGTVV_03 (row 79)

**Claim đối tác (3 ý):** (1) Lỗi hiển thị trường "Vụ việc"; (2) Thiếu trường "Điểm tổng"; (3) Thang điểm 1–10 thay vì 1–5 — tại **Danh sách đánh giá** (tab Đánh giá, chi tiết TVV).

**Evidence đã xem:** `partner-evidence/DGTVV_03.jpg` (full-res, cùng ảnh với DGTVV_02) — tab "Đánh giá" TVV `06748bb5…`, role CB_NV_TW. Frame chứa lỗi: bảng Danh sách đánh giá, cột "Vụ việc" hiển thị chuỗi `8d074115-4da5-427c-af55-3909f1e4e675` (mã định danh nội bộ); bảng không có cột "Điểm tổng"; các cột điểm render 10 sao + khối tổng hợp "8.3/10".

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | `cbnv_tw` — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái (state machine) | Tư vấn viên "Đang hoạt động", đã công nhận | Tư vấn viên `TVV-BTP-TW-0002` (98cfd963…), "Đang hoạt động", ngày công nhận 12/07/2026 | Không |
| Dữ liệu tiền đề | TVV có ≥1 đánh giá **đã liên kết vụ việc** (cột Vụ việc có giá trị) | Đã SEED đánh giá liên kết vụ việc `VV-BTP-TW-20260712-001` (id 8e259653-e0a5-49e8-ae7c-5fb07734ce09) → TVV có 2 đánh giá, 1 có vụ việc liên kết | Không |
| Input / filter | — (bug hiển thị danh sách) | — | Không |

**Ghi chú đóng GAP dữ liệu:** Dropdown "Vụ việc liên kết" trong form Gửi đánh giá **rỗng cho mọi TVV** (11/11 TVV có `lich-su-ho-tro` total = 0) → không tạo được đánh giá-có-vụ-việc bằng UI. Đã seed bản ghi đánh giá kèm `vuViecId` qua API (chỉ để tạo tiền đề), sau đó **quan sát kết quả trên UI thật** (reload trang → tab Đánh giá). 0 GAP.

**Kết luận:** 0 GAP → đủ điều kiện chốt verdict.

## Cổng 3 — SRS vs web (dạng gạch đầu dòng)

- **Ý 1 — cột "Vụ việc"** · SRS `srs-fr-04-chuyen-gia-tvv.md:1570` (SCR-IV-03 cell 23c): "Danh sách đánh giá: Người đánh giá + **Vụ việc** + Ngày + 3 điểm thành phần + Nhận xét". Quy ước nhận dạng vụ việc của hệ thống: `:1567` (cell 22, tab Lịch sử hỗ trợ) = "**Mã vụ việc (đường liên kết) + Tên vụ việc**".
  **Web:** cột "Vụ việc" hiển thị **mã định danh nội bộ** `8e259653-e0a5-49e8-ae7c-5fb07734ce09` thay cho mã vụ việc `VV-BTP-TW-20260712-001` / tên vụ việc → ❌ **Thiếu/Sai** → `Open` (BUG-DGTVV_03).
- **Ý 2 — thiếu cột "Điểm tổng"** · SRS `:1570` liệt kê đúng 7 thành phần của danh sách (Người đánh giá, Vụ việc, Ngày, 3 điểm thành phần, Nhận xét) — **KHÔNG** có cột "Điểm tổng". `diem_tong` chỉ được định nghĩa là field lưu trữ/đầu ra (`:706`, `:726`) và có hiển thị trong form Gửi đánh giá ("Điểm tổng (tính tự động) 0.0 / 5").
  **Web:** danh sách có đúng 7 cột như SRS, không có "Điểm tổng" → web **đúng SRS**; kỳ vọng đối tác **khác SRS** → `BA confirm` (không tự Reject).
- **Ý 3 — thang điểm 1–10** · SRS `:1570` "4.5/5 + 5 sao", `:703-706` thang 1–5.
  **Web:** khối tổng hợp "**4.2/5**", 3 tiêu chí 4.5/5 · 4.0/5 · 4.0/5, mọi widget = **5 sao**; điểm tổng bản ghi seed = 4.3 (AVG 5/4/4, thang 1–5) → **không tái hiện** thang 1–10.

**Verdict tổng:** có ≥1 ý `Open` → **Open** (theo QA_VERIFY_PROTOCOL §"1 case gộp nhiều lỗi con").

**Artifact quan sát:** `bug-reports/image/BUG-DGTVV_03-web-cot-vu-viec-hien-uuid-tho.png` (full-res — thấy rõ cột Vụ việc = UUID, 7 cột không có Điểm tổng, thang /5).

---

## RE-VERIFY 2026-07-15 (sau dev fix) — `Pass` (đúng phạm vi bug: ý 1 cột "Vụ việc")

**Điều kiện re-test khớp bug gốc (0 GAP):** `cbnv_tw` (CB_NV_TW) · TVV-BTP-TW-0002 "Đang hoạt động" · tiền đề đánh giá liên kết vụ việc `VV-BTP-TW-20260712-001` **vẫn còn** (2 đánh giá, 1 có vụ việc).

**Chạy trên web (tab Đánh giá, reload fresh):** cột **"Vụ việc"** nay hiển thị **đường liên kết `VV-BTP-TW-20260712-001` + tên "QA QLTVV28 - seed vu viec phan cong TVV"** (link tới `/vu-viec/8e259653…`) — đúng quy ước nhận dạng vụ việc `srs-fr-04:1567/1570`. Đánh giá **không** liên kết vụ việc hiển thị "—" (đúng, trường không bắt buộc).
- Không còn UUID thô `8e259653-…` như vòng 1.

**Evidence:** `bug-reports/image/BUG-DGTVV_03-reverify-pass-cot-vuviec-ma-ten.png`.

**Kết luận:** ý 1 (bug Open BUG-DGTVV_03) đã **Pass**. Ý 2 (thiếu "Điểm tổng") và ý 3 (thang 1–10) trước đã là `BA confirm` / không tái hiện — nằm ngoài phạm vi bug Open, không ảnh hưởng verdict Pass.
