# Bug Report — Vụ việc (đánh giá trùng)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-06-07 |
| **Loại test** | Regression (re-verify dev fix batch 2026-06-07) |
| **Round** | Verify batch 2026-06-07 |
| **Tài liệu tham chiếu** | FIXED-BUGS-SUMMARY.md #77 · srs-fr-05-vu-viec.md |

---

## Tổng hợp

Re-verify fix `vu-viec-already-rated-generic-409-not-vi-16-02` (#77, P2). Fix dev đã chuyển existence-check (đã đánh giá) **trước** state-guard nên hành vi/message đã đúng (trả "đã đánh giá" thay vì lỗi sai trạng thái). **Tuy nhiên** mã lỗi có cấu trúc `error.code` trả về client vẫn là mã generic `ERR-STATE-SYS-00-01`; mã nghiệp vụ `ERR-VAL-VI-16-02` chỉ nằm trong chuỗi `message`, không nằm ở trường `error.code`. Đây đúng là điều bug #77 yêu cầu sửa ("không-vi-16-02").

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 0     | 1      | 0     | 0       | 0      | 1    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-VERIFY-2026-06-07-77 | Medium | P2 | Negative | #77 | `srs-fr-05-vu-viec.md:1202`, `:1224` (FR-V.I-17 E3) | Đánh giá lại VV đã đánh giá: `error.code` vẫn generic, không phải mã nghiệp vụ already-rated | Open |

---

## BUG-VERIFY-2026-06-07-77 — Đánh giá lại vụ việc đã đánh giá trả `error.code` generic thay vì mã nghiệp vụ "đã đánh giá"

### Mô tả

Khi một cán bộ nghiệp vụ gửi đánh giá lần thứ 2 cho vụ việc đã được đánh giá (trạng thái `DA_DANH_GIA`), hệ thống trả HTTP 409 với `message` đúng ("...đã được đánh giá") nhưng trường `error.code` có cấu trúc lại là mã generic `ERR-STATE-SYS-00-01`. Mã nghiệp vụ already-rated (`ERR-VAL-VI-16-02`, logic SRS `ERR-DG-VV-03`) chỉ xuất hiện dưới dạng tiền tố trong chuỗi `message` ("ERR-VAL-VI-16-02: Vụ việc đã được đánh giá"), không phải ở trường `error.code` mà client/FE dùng để phân nhánh xử lý. Bug gốc #77 chính là yêu cầu mã trả về phải là mã already-rated chứ không phải mã generic.

### Các bước tái hiện

1. Đăng nhập role **`cb_nv_tw_01`** (CB Nghiệp vụ TW, quyền chấm đánh giá vụ việc theo FR-V.I-17), OTP 666666.
2. Chọn 1 vụ việc đã ở trạng thái `DA_DANH_GIA` (đã được CB NV chấm 1 lần) — ví dụ `dce4c308-b550-4823-af90-a2a13a387eaa` (VV-BTP-TW-20260510-002) hoặc `765920aa-43e4-47c0-a8ce-bf6e9c24e53e` (VV-BTP-TW-20260509-009).
3. Gọi `POST /api/v1/vu-viecs/{id}/danh-gia` (authenticated fetch, cookie JWT tự gửi) với body hợp lệ `{diemChatLuong, diemTienDo, diemThaiDo, nhanXet, version}`.
4. Quan sát `error.code` trong response so với `message`.

### Kết quả mong đợi

- Theo SRS `srs-fr-05-vu-viec.md:1202` ("Check duplicate: nếu đã tồn tại bản ghi DANH_GIA_VU_VIEC cho cùng VV và cùng loại người đánh giá → ERR-DG-VV-03") và `:1224` ("| E3 | Đã đánh giá | ERR-DG-VV-03 | 'Bạn đã đánh giá vụ việc này rồi' |"): điều kiện "đã đánh giá" phải phân biệt được bằng **mã lỗi riêng** của nghiệp vụ already-rated (mã hệ thống tương ứng `ERR-VAL-VI-16-02`), trả ở trường `error.code` để client định tuyến/log đúng — không dùng mã conflict generic.

### Kết quả thực tế

- HTTP **409** (đúng), nhưng `error.code = "ERR-STATE-SYS-00-01"` (generic), `message = "ERR-VAL-VI-16-02: Vụ việc đã được đánh giá"`.
- Tái hiện đồng nhất trên **2/2** vụ việc DA_DANH_GIA khác nhau → không phải fluke.
- Bản chất: exception được ném với body dạng chuỗi `"MÃ: message"` nên GlobalExceptionFilter không tách được mã vào `error.code` (rơi về mã 409 generic). Đây đúng là pattern mà dev đã sửa cho bug #2 (api-consumer-notfound, dùng object body `{code, message}`) nhưng **chưa áp dụng** cho đường này. Phần reorder existence-check trước state-guard đã đúng (message thể hiện nhánh already-rated), chỉ còn phần serialize mã chưa đạt.

### Bằng chứng

**API response (lần đánh giá thứ 2 trên VV `765920aa…` đã DA_DANH_GIA):**

```json
{
  "success": false,
  "error": {
    "code": "ERR-STATE-SYS-00-01",
    "message": "ERR-VAL-VI-16-02: Vụ việc đã được đánh giá",
    "timestamp": "2026-06-07T08:48:35.151Z",
    "requestId": "a5fee04f-4d79-4470-a493-1b43af3b4988"
  }
}
```

> Lặp lại trên VV `dce4c308…` cho cùng kết quả: HTTP 409, `error.code = "ERR-STATE-SYS-00-01"`, `message` chứa `ERR-VAL-VI-16-02`.

### So sánh (Comparison)

| Khía cạnh fix #77 | Trạng thái |
|---|---|
| Nhánh xử lý (existence-check trước state-guard) | ✅ Đã đúng (trả "đã được đánh giá", không còn lỗi sai trạng thái) |
| `message` nghiệp vụ | ✅ Đúng ("Vụ việc đã được đánh giá") |
| `error.code` có cấu trúc = mã already-rated | ❌ Vẫn là generic `ERR-STATE-SYS-00-01` (mã nghiệp vụ chỉ nằm trong message string) |
