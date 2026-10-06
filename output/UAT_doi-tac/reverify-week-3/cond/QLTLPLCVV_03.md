# Bảng đối chiếu điều kiện — QLTLPLCVV_03 (row 295) — Nút "Thêm tư liệu" hiện khi TVCS ở "Đã duyệt" / "Hủy"

**Kết luận:** BA confirm — Tái hiện đúng: nút **[+ Thêm tư liệu] hiện + enable + mở được form thêm** trên TVCS ở cả **DA_DUYET ("Đã duyệt")** và **HUY ("Hủy")** (khớp phản ánh đối tác). Nhưng SRS mâu thuẫn/không quy định gating theo state như đối tác kỳ vọng: dòng 1144 ghi nút [+ Thêm tư liệu] "**luôn hiển thị**" (không gate state); dòng 1152 ghi "mode sửa chỉ khi TIEP_NHAN, DANG_TU_VAN" (gate 2 state — không phải 5 state đối tác muốn). Kỳ vọng đối tác (ẩn ở DA_DUYET+HUY, hiện ở 5 state còn lại) không khớp cả 1144 lẫn 1152 → cần BA chốt.

| Điều kiện có thể đổi kết quả | Đối tác kỳ vọng | Mình test (cbnv_tw_05 / CB_NV_TW, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB NV | cbnv_tw_05 (CB_NV_TW — CRUD đầy đủ tư liệu, SRS dòng 806) | Không |
| TVCS state = TIEP_NHAN (baseline hợp lệ) | Hiện nút | TVCS-20260721-0001 (TIEP_NHAN) → [+ Thêm tư liệu] hiện+enable | Không |
| TVCS state = **DA_DUYET** | Đối tác: **phải ẩn** | Record `5eed0008` (DA_DUYET) → nút **hiện, enable, mở form "Thêm tư liệu pháp luật" đủ field enable + [Thêm mới] enable** (đã verify tận nơi) | Không |
| TVCS state = **HUY** | Đối tác: **phải ẩn** | Record `758383f6` seed→huy (HUY) → nút **hiện, enable** (đã verify tận nơi) | Không |
| SRS có clause ẩn nút theo state DA_DUYET/HUY? | Kỳ vọng đối tác cần cơ sở SRS | Không tìm thấy clause ẩn; dòng 1144 = "luôn hiển thị" (đã tra SRS) | Không |

> **Lưu ý cột GAP = "Không" nghĩa là verify KHÔNG còn khoảng trống** (đã tái hiện đủ mọi state). Điểm **web hiện nút ở DA_DUYET/HUY còn đối tác muốn ẩn** là **nội dung verdict** (BA confirm), không phải GAP verify — xem mục Kết luận.

**Artifact real-data (đọc DOM `button.disabled` + `offsetParent`, mở form thực tế):**
- DA_DUYET: `themTuLieuButtons = [{text:"Thêm tư liệu", visible:true, disabled:false}]`; click → modal "Thêm tư liệu pháp luật" mở, các field Tên/Loại/Lĩnh vực/Mô tả/File đều `disabled:false`, nút [Thêm mới] `disabled:false` (đã Hủy, không seed).
- HUY: `themTuLieuButtons = [{text:"Thêm tư liệu", visible:true, disabled:false}]`; banner record "Nội dung tư vấn đã bị hủy".
- Seed HUY: POST `/api/v1/noi-dung-tu-van-cs` (201, TIEP_NHAN) → POST `/api/v1/noi-dung-tu-van-cs/{id}/huy` (200, HUY).
- Ảnh: `reverify-audit/QLTLPLCVV_03/tvcs-batchE-03-nut-them-tu-lieu-tren-TVCS-DADUYET.png` + `...-HUY.png`.

**SRS (mâu thuẫn / không quy định gating như đối tác):**
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1144` — Accordion Tư liệu PL, nút [+ Thêm tư liệu] inline, điều kiện hiển thị = "**luôn hiển thị**".
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1152` — "Mode sửa chỉ khi trạng thái IN (TIEP_NHAN, DANG_TU_VAN)".
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1156` — Tư liệu PL: "CRUD tư liệu inline" (không nêu gate CRUD theo state TVCS).

→ Web theo 1144 (luôn hiển thị). Đối tác muốn ẩn ở DA_DUYET+HUY (không có trong SRS). 1152 nếu áp cho CRUD tư liệu thì chỉ cho ở 2 state (mâu thuẫn cả web lẫn kỳ vọng đối tác). Cần BA chốt: CRUD tư liệu có bị gate theo state TVCS không, và state nào được phép Thêm.
