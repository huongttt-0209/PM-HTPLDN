# Bảng đối chiếu điều kiện — PDHSTVV_05

**Evidence đã xem:** `partner-evidence/PDHSTVV_05.webm` → frames `reverify-audit/PDHSTVV_05/frames/`
- f009 (00:16): hộp thoại "Xác nhận phê duyệt" trên TVV-BTP-TW-0055 "Tester TKM" (Chờ phê duyệt), vai trò CB_PD_TW. Ô "Số quyết định công nhận" = **`A1000@`** (6/200) — KHÔNG đúng mẫu `QĐ-{số}/QĐ-{đơn vị}`. Ý kiến: "TKM test chức năng phê duyệt". Con trỏ đang bấm "Phê duyệt".
- f010 (00:18) — **frame chứa LỖI**: hiện toast xanh **"Phê duyệt TVV thành công"**, hồ sơ chuyển badge **"Chờ kích hoạt tài khoản"**, Ngày công nhận 08/07/2026.

**Đối tác phản ánh cụ thể:** nhập số quyết định công nhận **không hợp lệ** (`A1000@`) mà hệ thống vẫn phê duyệt thành công + đổi trạng thái hồ sơ, thay vì hiển thị thông báo lỗi.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ PD Trung ương (CB_PD_TW) | cbpd_tw (CB_PD_TW) | Không |
| Entity + trạng thái (state machine) | TVV-BTP-TW-0055 "Tester TKM", trạng thái **Chờ phê duyệt** trước thao tác | TVV-BTP-TW-0005 "QA TVV Trinh Duyet R17", trạng thái **Chờ phê duyệt** trước thao tác, cấp TW | Không |
| Input / giá trị nhập | Số quyết định = `A1000@` (sai mẫu QĐ-{số}/QĐ-{đơn vị}); Ý kiến phê duyệt có nhập | Số quyết định = **`A1000@`** (y hệt đối tác); Ý kiến phê duyệt = "QA test phe duyet so QD khong hop le" | Không |

**Kết quả verify trên web (cbpd_tw):**
- Bấm "Phê duyệt" với số QĐ `A1000@` → MutationObserver bắt được toast **"Phê duyệt TVV thành công"**; `.ant-form-item-explain-error` **rỗng** (không có thông báo lỗi nào).
- Hồ sơ chuyển trạng thái **"Chờ kích hoạt tài khoản"**, Ngày công nhận 12/07/2026, và **lưu luôn giá trị sai** vào hồ sơ: thẻ Hồ sơ hiển thị "Số quyết định: **A1000@**".
- API xác nhận: `{"trangThai":"CHO_KICH_HOAT","soQuyetDinh":"A1000@","ngayCongNhan":"2026-07-12"}`.
- → **TÁI HIỆN** đúng như đối tác.

**SRS:** FR-IV-07 (UC45) §Inputs #4 (`srs-fr-04-chuyen-gia-tvv.md` dòng 581): `so_quyet_dinh` — "Bắt buộc nếu PHE_DUYET. **Format: QĐ-{số}/QĐ-{đơn_vị}**, max 100 ký". Entity TU_VAN_VIEN (dòng 2025): `so_quyet_dinh_cong_nhan` — "Format QĐ-{số}/QĐ-{đơn_vị}".

**Verdict:** `Open`.

---
## Re-verify 2026-07-15 (sau dev fix — vòng 2)
CB_PD_TW `cbpd_tw`, hồ sơ "Chờ phê duyệt" TVV-BTP-TW-0010, nhập Số quyết định = `A1000@` (SAI mẫu, y hệt đối tác) → bấm "Phê duyệt" trong modal.
- Hệ thống CHẶN: hiện lỗi "Số quyết định phải theo mẫu QĐ-{số}/QĐ-{đơn vị}, VD: QĐ-123/QĐ-BTP"; modal không đóng; hồ sơ giữ nguyên "Chờ phê duyệt" (không đổi trạng thái, không lưu giá trị sai). **FIXED.**
⇒ PASS. Ảnh: `bug-reports/image/PDHSTVV_05-reverify-soqd-saimau-bi-tu-choi-validation.png`.
