# Bảng đối chiếu điều kiện — QLTLPLCVV_09 (row 298) — Sửa tư liệu CONG_KHAI: message kỹ thuật lộ field

**Kết luận:** Open — Tái hiện đúng: sửa tư liệu ở trạng thái CONG_KHAI → hệ thống báo lỗi kỹ thuật **"Tư liệu đã công khai, chỉ cho phép cập nhật: moTa, fileDinhKemIds"** (lộ tên field API nội bộ) và từ chối mọi thao tác Lưu (kể cả chỉ đổi file). Message mâu thuẫn SRS dòng 888 (phải hướng dẫn "hủy công khai trước", không phải gợi ý cho sửa 1 phần).

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res `partner-evidence/QLTLPLCVV_09.jpg`) | Mình test (cbnv_tw / CB_NV_TW, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW (Cán bộ NV Trung ương — góc phải màn) | cbnv_tw (CB_NV_TW — đúng Tác nhân SRS dòng 806, CRUD đầy đủ) | Không |
| Entity + trạng thái | Tư liệu "tài liệu kiểm thử" ở trạng thái **Đã công khai (CONG_KHAI)**, có 1 file | Tư liệu seed **TL-BF-0721-CK** ở trạng thái **Đã công khai (CONG_KHAI)**, có 1 file (đã tự công khai) | Không |
| Dữ liệu tiền đề | Tư liệu CONG_KHAI thuộc 1 TVCS, có ≥1 file đính kèm | Tư liệu CONG_KHAI thuộc TVCS-SEED-0001, có 1 file (seed_clean.pdf) | Không |
| Input / thao tác | Mở "Sửa" tư liệu CONG_KHAI → nhập/không nhập → Lưu | Mở "Sửa" tư liệu CONG_KHAI → bấm Lưu (2 lần: không đổi gì; và chỉ đổi/thêm file) | Không |

**Artifact real-data (chạy trên data đã seed, đo bằng `tools/toast-capture.js` — không lọc trùng, `innerText`, đếm request):**
- Bấm Lưu (không đổi field): **1 toast** `"Tư liệu đã công khai, chỉ cho phép cập nhật: moTa, fileDinhKemIds"` · **1 request** `PATCH /api/v1/tu-lieu-phap-ly-vvs/172a8cfa-...` (bị từ chối, modal giữ nguyên). BI_LAP=false, soObserverDangSong=1.
- Bấm Lưu (chỉ thêm file mới): **1 toast** y hệt · **2 request** `POST .../upload` + `PATCH /api/v1/tu-lieu-phap-ly-vvs/172a8cfa-...` (PATCH từ chối) → file KHÔNG được lưu (row vẫn File=1). ⇒ Kể cả chỉ đổi file (mà message nói "fileDinhKemIds" được phép) vẫn bị chặn.
- Field trong modal Sửa (CONG_KHAI): Tên/Loại/Lĩnh vực **disabled**, **Mô tả disabled** (mâu thuẫn message inline "chỉ được cập nhật mô tả và file"), File **enabled**, nút Lưu enabled.
- Ảnh: `bug-reports/tvcs/image/BUG-QLTLPLCVV_09-modal-inline-msg-fields.png` (modal Sửa: message inline cam + Mô tả disabled), `BUG-QLTLPLCVV_09-edit-modal-fields.png`. Toast kỹ thuật: đo bằng observer (trên) + ảnh đối tác `partner-evidence/QLTLPLCVV_09.jpg` (toast y hệt).

**SRS:** `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:888` — "Kiểm tra trạng thái: nếu CONG_KHAI → **từ chối sửa (phải hủy công khai trước)**". Error Handling (dòng 950–957) KHÔNG có mã lỗi cho tình huống sửa tư liệu công khai → message hiện tại lộ field API + mâu thuẫn hướng dẫn SRS.

**Ghi chú env:** Đối tác test trên `htpldn-uat.ospgroup.vn` (Mô tả ENABLE trong ảnh); mình test trên env được giao `18.143.165.120.nip.io` (Mô tả DISABLE). Toast kỹ thuật + hành vi chặn Lưu **giống nhau trên cả 2 env** — lỗi tái hiện.
