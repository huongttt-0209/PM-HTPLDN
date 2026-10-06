# Audit — QLDMLDN_13 (row 144) — Verdict: BA confirm

**Cổng 1 — Bằng chứng đối tác:** `partner-evidence/QLDMLDN_13.jpg` (full-res). Form "Chỉnh sửa danh mục" (record TKM) — có "Danh mục cha" + `* Tiêu chí doanh thu` (dấu * đỏ, đã điền value NĐ80/2021).

**Cổng 2 — Bug đối tác:** (1) "Danh mục cha" thừa; (2) "Doanh thu" bị đánh bắt buộc.

**Cổng 3 — SRS vs web:**
| SRS | Web (21/07) | Kết luận |
|---|---|---|
| TPL-DM-CRUD Inputs (77-83): không có "Danh mục cha" | Form Sửa có "Danh mục cha" (tùy chọn) | Thừa → BA confirm |
| FR-VIII-07 dòng 402: doanh thu = N | Không dấu *, placeholder "(tùy chọn)", PATCH lưu OK khi trống | Đúng SRS → không tái hiện |

**Artifact real-data:** `web-sua-form.png` (form Sửa TNHH — Tiêu chí doanh thu không có *). Test edit-save Doanh thu trống → 1 PATCH `/api/v1/danh-muc/<id>` → toast "Cập nhật thành công".

**Verdict:** `BA confirm`. Chi tiết: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch2.md` Cụm 1 + Ghi chú.
