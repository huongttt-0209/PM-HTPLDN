# Bảng đối chiếu điều kiện — THDG_03

Loại bug: **Nhập điểm vượt điểm tối đa (max=10) — đối tác báo "tự nắn về max, không báo lỗi".** Verdict phụ thuộc: (1) đúng role/state chấm điểm, (2) nhập điểm > max, (3) hành vi chặn ở FE + BE.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò chấm điểm | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP Hà Nội) | Không |
| Trạng thái đợt | Đang chấm điểm | Đợt B2 DANG_DANH_GIA, tab Chấm điểm | Không |
| Giá trị nhập | Điểm > max (vd 15 > 10) | Nhập 15 vào ô tiêu chí max=10 | Không |
| Hành vi FE khi nhập vượt max | Đối tác báo: tự nắn về max, không báo lỗi | Tái hiện đúng: AntD InputNumber nắn `15 → 10.0` khi blur, KHÔNG toast/không error-message | Không |
| Hành vi BE khi nhận điểm vượt max (verify 2nd method) | (đối tác không kiểm) | curl `PUT /ket-quas` điểm=15 → **422 `ERR-DG-SC-06`** "Điểm cho tiêu chí '...' vượt quá điểm tối đa (10)"; data giữ nguyên 10/8/9/7 | Không |

**Kết luận: 0 GAP điều kiện.** Tái hiện đúng hiện tượng FE đối tác báo (nắn 15→10 im lặng). NHƯNG constraint 0..max **được enforce đúng cả 2 tầng**: FE chặn bằng clamp, BE reject bằng `ERR-DG-SC-06` với message rõ ràng. Điểm khác biệt duy nhất: khi FE clamp, không hiện message tường minh cho user (SRS FR-VI-06 E1 L517 mô tả `ERR-DG-DG-01` "Điểm phải từ 0 đến {max}"). Vì hệ thống KHÔNG chấp nhận điểm sai (không phải lỗi logic/data), việc FE clamp im lặng vs hiện message là quyết định UX — theo describe-not-prescribe QA không tự chốt. → **BA confirm** (FE silent clamp có phải defect vs SRS E1 hay không).
