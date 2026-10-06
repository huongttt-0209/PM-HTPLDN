# Bảng đối chiếu điều kiện — QLTLPLCVV_11 (row 299) — Xóa tư liệu CONG_KHAI: nút Xóa bị disable

**Kết luận:** Open — Tái hiện đúng: tư liệu ở trạng thái CONG_KHAI ("Đã công khai") → nút **"Xóa" bị disable** (thuộc tính `disabled=true`, class `ant-btn-dangerous` xám). SRS dòng 899 quy định xóa mềm tư liệu CONG_KHAI VẪN được (hệ thống tự set cong_khai=0 trước rồi soft-delete) — KHÔNG disable nút Xóa.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res `partner-evidence/QLTLPLCVV_11.jpg`) | Mình test (cbnv_tw / CB_NV_TW, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW (Cán bộ NV Trung ương) | cbnv_tw (CB_NV_TW — đúng Tác nhân SRS dòng 806, CRUD đầy đủ) | Không |
| Entity + trạng thái | Tư liệu "tài liệu kiểm thử" **Đã công khai (CONG_KHAI)** → nút Xóa xám/disable; tư liệu "TKM..." **Nháp (NHAP)** → nút Xóa đỏ/enable | Tư liệu seed **TL-BF-0721-CK** **Đã công khai** → Xóa disabled; cùng tư liệu lúc **Nháp** (trước công khai) → Xóa enabled (baseline) | Không |
| Dữ liệu tiền đề | Tư liệu CONG_KHAI có ≥1 file, thuộc 1 TVCS | Tư liệu CONG_KHAI có 1 file, thuộc TVCS-SEED-0001 | Không |
| Input / thao tác | Quan sát nút Xóa trên hàng tư liệu CONG_KHAI | `evaluate_script` đọc `button.disabled` + class của nút Xóa hàng CONG_KHAI | Không |

**Artifact real-data (đọc DOM trực tiếp, chạy trên data đã seed):**
- Khi CONG_KHAI: `evaluate_script` trả `{t:"Xóa", disabled:true, cls:"...ant-btn-dangerous...ant-btn-variant-outlined ant-btn-sm"}`. Các nút cùng hàng: Xem tệp/Sửa/Hủy công khai đều `disabled:false`.
- Khi NHAP (baseline, cùng tư liệu trước khi công khai): nút Xóa `disabled:false` (đỏ, enable).
- Ảnh: `bug-reports/tvcs/image/BUG-QLTLPLCVV_11-xoa-disabled.png` (hàng "Đã công khai" — nút **Xóa** xám mờ cạnh Sửa/Hủy công khai enable).

**SRS:** `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:899` — Processing Xóa mềm tư liệu, step 3: "Nếu trạng thái = CONG_KHAI: set `cong_khai = 0` trên CSDL CMS trước (hủy CK); … " → xóa được, tự hủy công khai trước; dòng 901 soft delete. KHÔNG có quy định disable nút Xóa. Thao tác nội bộ CMS (BR-FLOW-07) → INTERNAL, verify trực tiếp trên CMS (không phụ thuộc Cổng PLQG).
