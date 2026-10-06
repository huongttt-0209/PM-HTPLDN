# Bảng đối chiếu điều kiện — CNTTHDCTVV_02 (row 84)

**Claim đối tác:** Vô hiệu hóa TVV đang có vụ việc/hỏi đáp chưa hoàn thành → hệ thống hiển thị **"Có lỗi xảy ra"** (thay vì thông báo nghiệp vụ "Tư vấn viên đang có {N} vụ việc và {M} hỏi đáp chưa hoàn thành, không thể vô hiệu hóa").

**Evidence đã xem:** `partner-evidence/CNTTHDCTVV_02.webm` (36.04s) — đã trích **13 khung full-res 1920×1080** (`reverify-audit/CNTTHDCTVV_02/frames/`).
- **Khung 00:31 (t=32s):** hộp thoại "Cập nhật trạng thái tư vấn viên" trên TVV `23afb884-ef4b-449b-b605-868db2659be6` ("huongcg", Đang hoạt động) — Trạng thái mới = **"Vô hiệu hóa"**, Lý do = "TKM test vô hiệu hóa khi đag xử lý vụ việc" (42/1000), con trỏ đang bấm **"Xác nhận"**. Role: CB_NV_TW.
- **Khung chứa LỖI: 00:35 (t=35.8s)** — sau khi bấm Xác nhận, hộp thoại hiện **banner đỏ "Có lỗi xảy ra"** ở đầu form; hộp thoại **không đóng**, trạng thái TVV không đổi.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | `cbnv_tw` — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái (state machine) | Tư vấn viên **"Đang hoạt động"** (TVV-BTP-TW-…, "huongcg") → chuyển sang **"Vô hiệu hóa"** | Tư vấn viên `TVV-BTP-TW-0002` (98cfd963…) **"Đang hoạt động"** → chọn **"Vô hiệu hóa"** (transition HOAT_DONG → VO_HIEU_HOA, đúng SM-TVV) | Không |
| Dữ liệu tiền đề | TVV **đang có vụ việc/hỏi đáp chưa hoàn thành** (theo Điều kiện của case + lý do đối tác nhập) | TVV **đang có 1 vụ việc chưa hoàn thành** — `VV-BTP-TW-20260712-001` (Đã phân công, chưa hoàn thành). **Backend tự xác nhận đếm được**: *"đang có **1 vụ việc và 0 hỏi đáp** chưa hoàn thành"* | Không |
| Input / filter | Trạng thái mới = "Vô hiệu hóa" + Lý do hợp lệ (42 ký tự ≥ 10) → bấm "Xác nhận" | Trạng thái mới = "Vô hiệu hóa" + Lý do hợp lệ (88 ký tự ≥ 10) → bấm "Xác nhận" | Không |

**Kết luận:** 0 GAP → đủ điều kiện chốt verdict.

## Cổng 3 — SRS vs web (dạng gạch đầu dòng)

- **SRS** `srs-fr-04-chuyen-gia-tvv.md:892` — FR-IV-12 (UC50) §Processing bước 2: khi vô hiệu hóa từ HOAT_DONG/TAM_DUNG → kiểm tra TVV **không còn vụ việc/hỏi đáp đang xử lý**.
- **SRS** `srs-fr-04-chuyen-gia-tvv.md:914` — FR-IV-12 §Error Handling **E2 (ERR-TT-02)**: *"Tư vấn viên đang có **{N} vụ việc và {M} hỏi đáp chưa hoàn thành, không thể vô hiệu hóa**"* (severity ERROR).
- **SRS** `:925` §Acceptance Criteria: *"**Given** CB NV chọn Vô hiệu hóa **When** TVV có vụ việc đang xử lý **Then** từ chối + cảnh báo (ERR-TT-02)"*.
- **Web (18.143.165.120):**
  - Hệ thống **CÓ từ chối đúng** thao tác (hộp thoại không đóng, trạng thái TVV giữ nguyên "Đang hoạt động") ✅.
  - **Backend trả về ĐÚNG thông báo nghiệp vụ theo SRS** — `POST /api/v1/tu-van-viens/{id}/cap-nhat-trang-thai` → **HTTP 422**, body: `{"code":"ERR-STATE-IV-TT-02","message":"**Tư vấn viên đang có 1 vụ việc và 0 hỏi đáp chưa hoàn thành, không thể vô hiệu hóa**"}` ✅.
  - ❌ **Giao diện KHÔNG hiển thị thông báo đó** — chỉ hiện banner đỏ chung chung **"Có lỗi xảy ra"** (`.ant-alert-error`, đo DOM). Cán bộ không biết vì sao bị từ chối và cần làm gì tiếp.
- ⇒ ❌ **Sai SRS** `:914` + `:925` ở **tầng hiển thị**: thông báo bắt buộc theo SRS bị thay bằng thông báo chung chung → `Open` (BUG-CNTTHDCTVV_02). **Tái hiện đúng claim đối tác.**
- **Ghi chú cho dev:** đây là lỗi **hiển thị phía giao diện** (không đọc `message` mà backend trả về), **không phải** lỗi nghiệp vụ — quy tắc chặn vô hiệu hóa đã chạy đúng.

**Artifact quan sát:** `bug-reports/image/BUG-CNTTHDCTVV_02-web-modal-hien-co-loi-xay-ra.png` (full-res — loại claim = Thao tác/state: chụp đúng kết quả của chính thao tác bấm "Xác nhận", banner "Có lỗi xảy ra" + hộp thoại còn mở) **kèm response 422 của chính lệnh gọi đó** (bằng chứng backend trả đúng message).

---

## RE-VERIFY 2026-07-15 (sau dev fix) — `Pass`

**Điều kiện re-test khớp bug gốc (0 GAP):** `cbnv_tw` (CB_NV_TW) · TVV-BTP-TW-0002 "Đang hoạt động" → chọn "Vô hiệu hóa" · TVV **đang có vụ việc chưa hoàn thành** (nay 2 vụ việc — backend tự đếm) · Lý do hợp lệ ≥10 ký tự.

**Chạy hết luồng trên web (Cập nhật trạng thái → Vô hiệu hóa → Xác nhận, bắt banner bằng MutationObserver + đọc live DOM):**
- ✅ Giao diện nay hiển thị **ĐÚNG thông báo nghiệp vụ**: **"Tư vấn viên đang có 2 vụ việc và 0 hỏi đáp chưa hoàn thành, không thể vô hiệu hóa"** — KHÔNG còn banner chung chung "Có lỗi xảy ra". (Số "2" đúng theo dữ liệu hiện tại: TVV có 2 vụ việc Đã phân công chưa hoàn thành.)
- Chặn thao tác đúng: `POST .../cap-nhat-trang-thai` → **422** (`ERR-STATE-IV-TT-02`), hộp thoại giữ nguyên, trạng thái TVV vẫn "Đang hoạt động".
- Giao diện nay đọc và hiển thị `message` từ response backend → đúng SRS `:914`/`:925`.

**Evidence:** `bug-reports/image/BUG-CNTTHDCTVV_02-reverify-pass-thongbao-nghiepvu-dung.png`.

**Kết luận:** lỗi tầng hiển thị đã khắc phục — giao diện hiển thị đúng thông báo nghiệp vụ ERR-TT-02 theo SRS → **Pass**.
