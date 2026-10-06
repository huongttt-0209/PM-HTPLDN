# Audit — QLDMHSDNTT_13 (row 151) — Verdict: BA confirm

**Cổng 1 — Bằng chứng đối tác:** `partner-evidence/QLDMHSDNTT_13.jpg` (full-res). Form "Chỉnh sửa danh mục" tab **Hồ sơ đề nghị thanh toán** — (1) trường **"Danh mục cha"** + (2) khối **"Thành phần hồ sơ"** bắt buộc ≥1.

**Cổng 2 — Bug đối tác:** (1) "Danh mục cha" thừa; (2) "Thành phần hồ sơ" bị bắt buộc.

**Cổng 3 — SRS vs web:**
| SRS | Web (21/07) | Kết luận |
|---|---|---|
| TPL-DM-CRUD Inputs (77-83): không có "Danh mục cha" | Form Sửa có "Danh mục cha" (tùy chọn) | Thừa → BA confirm |
| FR-VIII-09 dòng 442: `thanh_phan_ho_so` = N | Form Sửa ép ≥1 thành phần (cùng cơ chế form Thêm) | App enforce ≥1 trái SRS → BA confirm |

**Artifact real-data:** `web-sua-form.png` (form Sửa + Danh mục cha + khối Thành phần bắt buộc). Cơ chế chặn ≥1 thành phần đã chứng minh chi tiết ở QLDMHSDNTT_06 (`web-loi-thanh-phan-bat-buoc.png` — 0 request/0 toast khi lưu trống, dùng chung component).

**Verdict:** `BA confirm` (vừa lỗi-vs-SRS vừa cần BA chốt spec → cột trạng thái = BA confirm theo chỉ đạo). Chi tiết: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch2.md` Cụm 1 + Cụm 2.
