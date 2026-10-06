# Bảng đối chiếu điều kiện — PDHSTVV_03

**Evidence đã xem:** `partner-evidence/PDHSTVV_03.jpg` (ảnh full-res)
- Hộp thoại "Xác nhận phê duyệt" trên hồ sơ TVV-BTP-TW-0055 "Tester TKM" (Chờ phê duyệt), vai trò **Cán bộ PD Trung ương (CB_PD_TW)**.
- Ô "Số quyết định công nhận" (bắt buộc) có bộ đếm **"0 / 200"** → giới hạn 200 ký tự.
- Ô "Ý kiến phê duyệt (tùy chọn)" bộ đếm "0 / 2000" → đúng SRS.

**Đối tác phản ánh cụ thể:** Số quyết định công nhận cho phép tối đa **200** ký tự, trong khi SRS quy định **tối đa 100** ký tự.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ PD Trung ương (CB_PD_TW) — header ảnh evidence | cbpd_tw (CB_PD_TW) | Không |
| Entity + trạng thái (state machine) | TVV-BTP-TW-0055 "Tester TKM", trạng thái **Chờ phê duyệt** | TVV-BTP-TW-0005 "QA TVV Trinh Duyet R17", trạng thái **Chờ phê duyệt**, cấp TW | Không |
| Input / giá trị nhập | Ô "Số quyết định công nhận" để trống (0/200) — đối tác chỉ phản ánh giới hạn ký tự hiển thị trên bộ đếm | Nhập chuỗi 150 ký tự (`QĐ-` + 140 ký tự + `/QĐ-BTP`) vào đúng ô đó | Không |

**Kết quả verify trên web (cbpd_tw, hộp thoại "Xác nhận phê duyệt"):**
- Thuộc tính `maxlength` của ô "Số quyết định công nhận" = **200**; bộ đếm hiển thị **"0 / 200"** → **TÁI HIỆN** đúng như đối tác.
- Nhập 150 ký tự → ô nhận đủ **150 ký tự**, bộ đếm "150 / 200", **không có thông báo lỗi**, nút "Phê duyệt" vẫn bật → hệ thống chấp nhận giá trị vượt giới hạn 100 ký tự của SRS.
- Ô "Ý kiến phê duyệt": `maxlength` = 2000 → đúng SRS (FR-IV-07 §Inputs #5, dòng 582).

**SRS:** FR-IV-07 (UC45) §Inputs #4 (`srs-fr-04-chuyen-gia-tvv.md` dòng 581): `so_quyet_dinh` — "Bắt buộc nếu PHE_DUYET. Format: QĐ-{số}/QĐ-{đơn_vị}, **max 100 ký**".

**Verdict:** `Open`.

---
## Re-verify 2026-07-15 (sau dev fix — vòng 2)
CB_PD_TW `cbpd_tw`, hồ sơ "Chờ phê duyệt" TVV-BTP-TW-0010, mở modal "Xác nhận phê duyệt".
- Ô "Số quyết định công nhận": `maxlength=100`, bộ đếm "0 / 100" (bug gốc: 200). Ô Ý kiến: `maxlength=2000`. **FIXED.**
⇒ PASS. Ảnh: `bug-reports/image/PDHSTVV_03-reverify-modal-soqd-maxlength-100.png`.
