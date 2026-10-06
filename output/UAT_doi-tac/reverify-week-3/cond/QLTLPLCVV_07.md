# Bảng đối chiếu điều kiện — QLTLPLCVV_07 (row 296) — Nút "Sửa" hiện + cho sửa (moTa/file) trên tư liệu CONG_KHAI

**Kết luận:** BA confirm — Tái hiện đúng phần đối tác thấy (nút **[Sửa] hiện + enable** trên tư liệu "Đã công khai"), **và** kiểm sâu phát hiện: bấm Sửa → hệ thống **cho phép sửa thật** `moTa` + `fileDinhKemIds` trên tư liệu CONG_KHAI (PATCH chỉ `{moTa,version}` trả **200**, version 3→4, giữ nguyên CONG_KHAI), chỉ **khóa** các field lõi (tên/loại/lĩnh vực → PATCH kèm chúng trả **400 `ERR-STATE-X1-06-01`**). Nhưng SRS dòng 888 nói CONG_KHAI → **từ chối sửa hoàn toàn** (phải hủy công khai trước), KHÔNG có carve-out "cho sửa moTa/file". App thực thi 1 rule khác có chủ đích (mã lỗi riêng liệt kê field cho phép) → xung đột spec-vs-implementation, cần BA chốt.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test (cbnv_tw_05 / CB_NV_TW, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB NV (không phải CG R-only) | cbnv_tw_05 (CB_NV_TW — CRUD đầy đủ, SRS dòng 806/812) | Không |
| Tư liệu state = **CONG_KHAI** | Nút Sửa hiện (đối tác: chỉ nên hiện khi Nháp) | Tư liệu `90268a74` "Đã công khai" → nút Sửa `visible:true, disabled:false` (đã tái hiện) | Không |
| Bấm Sửa → form ra sao | Đối tác chỉ nêu "nút hiện" | Modal "Sửa tư liệu pháp luật" mở, banner "Tư liệu đã công khai — chỉ được cập nhật mô tả và file đính kèm"; Tên/Loại/Lĩnh vực **disabled**; Mô tả **disabled** (dù banner nói được sửa); File đính kèm **enable**; [Lưu] enable | Không |
| Sửa có PERSIST không (điểm chốt) | Cần verify để chốt | PATCH `{moTa,version:3}` → **200 success**, `moTa` đổi, `version`→4, `trangThai` vẫn CONG_KHAI → **sửa thật được** (đã verify) | Không |
| Field lõi có bị chặn không | Cần verify | PATCH kèm `tenTuLieu/loaiTuLieu` → **400 `ERR-STATE-X1-06-01`** "chỉ cho phép cập nhật: moTa, fileDinhKemIds" (đã verify) | Không |

> **Lưu ý cột GAP = "Không" nghĩa là verify KHÔNG còn khoảng trống** (đã tái hiện nút + test persist bằng API). Điểm **app cho sửa moTa/file khi CONG_KHAI trái SRS 888** là **nội dung verdict** (BA confirm — xung đột spec vs implementation), không phải GAP verify — xem mục Kết luận.

**Artifact real-data (network + DOM, đọc trực tiếp):**
- Modal field state (`evaluate_script`): Tên/Loại/Lĩnh vực/Mô tả `disabled:true`; File đính kèm input `disabled:false`; [Lưu] `disabled:false`.
- FE bấm [Lưu] (payload gồm cả field khóa) → `PATCH /tu-lieu-phap-ly-vvs/90268a74` **400**, body `{"success":false,"error":{"code":"ERR-STATE-X1-06-01","message":"Tư liệu đã công khai, chỉ cho phép cập nhật: moTa, fileDinhKemIds"}}`.
- Test chốt (injected fetch, chỉ field cho phép): `PATCH {moTa:"...", version:3}` → **200**, `data.moTa` đổi, `data.version=4`, `data.trangThai="CONG_KHAI"`. (Đã khôi phục moTa gốc sau test — version=5.)
- Ảnh: `reverify-audit/QLTLPLCVV_07/tvcs-batchE-07-modal-sua-mo-tren-tu-lieu-cong-khai.png` (modal mở) + `...-luu-400-err-state.png` (toast 400 khi kèm field khóa).

**SRS (app diverge có chủ đích):**
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:888` — Processing Chỉnh sửa, step 3: "Kiểm tra trạng thái: nếu CONG_KHAI → **từ chối sửa (phải hủy công khai trước)**". Step 5 (dòng 890, cập nhật ten/loai/linh_vuc/mo_ta) chỉ chạy khi KHÔNG bị từ chối ở step 3 → SRS = chặn sửa toàn bộ khi CONG_KHAI.
- App: cho sửa `moTa` + `fileDinhKemIds` khi CONG_KHAI (mã `ERR-STATE-X1-06-01` chỉ chặn field lõi) → **khác** SRS 888. Đây là hành vi có chủ đích (không phải quên enforce) → BA chốt: SRS 888 (chặn toàn bộ, hủy công khai trước) hay rule app (cho sửa moTa/file) là chuẩn; và nút [Sửa] nên ẩn hay hiện-nhưng-hạn-chế trên CONG_KHAI.
