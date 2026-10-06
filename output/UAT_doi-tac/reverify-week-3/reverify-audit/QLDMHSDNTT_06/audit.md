# Audit — QLDMHSDNTT_06 (row 149) — Verdict: BA confirm

**Cổng 1 — Bằng chứng đối tác:** `partner-evidence/QLDMHSDNTT_06.jpg` (full-res). Form "Thêm mới danh mục" tab **Hồ sơ đề nghị thanh toán** — (1) trường **"Danh mục cha"** + (2) khối **"Thành phần hồ sơ"** bị đánh bắt buộc ≥1.

**Cổng 2 — Bug đối tác:** (1) "Danh mục cha" thừa; (2) "Thành phần hồ sơ" bị bắt buộc (SRS: không bắt buộc).

**Cổng 3 — SRS vs web:**
| SRS | Web (21/07) | Kết luận |
|---|---|---|
| TPL-DM-CRUD Inputs (77-83): không có "Danh mục cha" | Form có "Danh mục cha" (tùy chọn) | Thừa → BA confirm |
| FR-VIII-09 dòng 442: `thanh_phan_ho_so` = N (không bắt buộc) | Form ép ≥1 thành phần; nút xóa Thành phần 1 bị vô hiệu; lưu trống → chặn | App enforce ≥1 trái SRS → BA confirm |

**Artifact real-data:**
- `web-luu-thanh-phan-trong.png` (form với Thành phần 1 bắt buộc + Danh mục cha).
- `web-loi-thanh-phan-bat-buoc.png` (bấm Đồng ý khi thành phần trống → **0 request, 0 toast**, dialog vẫn mở, lỗi inline "Mã thành phần là bắt buộc" + "Tên thành phần là bắt buộc").

**Verdict:** `BA confirm` (case vừa là lỗi-vs-SRS vừa cần BA chốt spec → ghi cột trạng thái = BA confirm theo chỉ đạo). Chi tiết: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch2.md` Cụm 1 + Cụm 2.
