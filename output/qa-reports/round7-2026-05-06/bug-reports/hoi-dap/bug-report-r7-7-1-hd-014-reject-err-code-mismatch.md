# Bug Report — R7.7.1 HD-014 Reject empty lyDo trả ERR-VAL-SYS-00-01 thay vì spec-required ERR-PD-02

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người log** | QA Automation (Claude Code) |
| **Ngày log** | 2026-05-11 10:00:00 |
| **TC liên quan** | HD-014 — CB PD từ chối không nhập lý do → expect ERR-PD-02 |
| **Tài liệu spec** | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` FR-II-08 + bảng Error Code `ERR-PD-02` ("Lý do từ chối là bắt buộc") |
| **Round** | Round 7 / R7.7.1 Phase 9 |
| **Account** | `cb_pd_tw_04` (CB Phê duyệt TW 04) — bypass OTP `666666` |

## Bug Summary

| BUG-ID | Severity | Component | Title | Status |
|---|---|---|---|---|
| BUG-HD-014-REJECT-ERR-CODE-001 | Minor | BE — validation error code mapping | POST `/tu-choi` empty lyDo trả `ERR-VAL-SYS-00-01` thay vì spec-required `ERR-PD-02` | Open |

---

## BUG-HD-014-REJECT-ERR-CODE-001 — Empty lyDo trả generic ERR-VAL-SYS thay vì business ERR-PD-02

### Mô tả

CB Phê duyệt TW gọi POST `/api/v1/hoi-daps/{id}/tu-choi` với `lyDo=""` hoặc `lyDo=null`. BE validate input layer (Nest pipe / class-validator) trước business rule check → trả 422 với code `ERR-VAL-SYS-00-01` (generic validation system error). Spec FR-II-08 + bảng Error Code yêu cầu `ERR-PD-02` ("Lý do từ chối là bắt buộc"). Mismatch giữa BE generic code và business code spec quy định.

### Các bước tái hiện

1. Login `cb_pd_tw_04` → /hoi-dap → tìm record DA_DUYET (hoặc CHO_PHE_DUYET nếu pool có).
2. Mở DevTools console (hoặc dùng `evaluate_script`):
   ```js
   await fetch('/api/v1/hoi-daps/3577bfb6-ec53-4a0c-8858-b0507afb3472/tu-choi', {
     method:'POST', credentials:'include',
     headers:{'Content-Type':'application/json'},
     body: JSON.stringify({lyDo: '', version: 11})
   }).then(r => r.json());
   ```
3. Quan sát response code field.

### Kết quả mong đợi

Theo `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` bảng Error Code (FR-II-08):

- HTTP 400 hoặc 422
- `error.code = "ERR-PD-02"` (business-specific code cho "Lý do từ chối là bắt buộc")
- `error.field = "lyDo"`
- `error.message = "Lý do từ chối là bắt buộc"`

UI hiện toast/inline lỗi với message rõ cho user.

### Kết quả thực tế

Response:

```json
{
  "success": false,
  "error": {
    "code": "ERR-VAL-SYS-00-01",
    "field": "lyDo",
    "message": "Lý do từ chối là bắt buộc (tối thiểu 10 ký tự)",
    "details": [
      {"field":"lyDo","message":"Lý do từ chối là bắt buộc (tối thiểu 10 ký tự)"},
      {"field":"lyDo","message":"lyDo should not be empty"}
    ]
  }
}
```

- Code = `ERR-VAL-SYS-00-01` (generic validation system) thay vì `ERR-PD-02` (business spec)
- Message thừa "(tối thiểu 10 ký tự)" — spec không nêu min length yêu cầu (info ok nhưng có thể che mất ý chính khi i18n)
- `details[1].message` còn raw English "lyDo should not be empty" — leak class-validator default message

### Bằng chứng

```
[2026-05-11 02:53:55] POST /api/v1/hoi-daps/3577bfb6-ec53-4a0c-8858-b0507afb3472/tu-choi
Request body: {"lyDo":"","version":11}
Response status: 422
Response body code: ERR-VAL-SYS-00-01 (expected ERR-PD-02)
requestId: 51b352a3-1282-47d5-ad5e-d3071e39f27b
```

Đã verify cả 2 trường hợp `lyDo=""` và `lyDo=null` — đều trả `ERR-VAL-SYS-00-01` thay vì `ERR-PD-02`.

---

*Bug report generated: 2026-05-11 10:00:00 | QA Automation via Claude Code (Opus 4.7)*
