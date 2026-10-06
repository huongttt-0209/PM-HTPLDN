# Bảng đối chiếu điều kiện — QLBMHD_13 (form Sửa không hiển thị file đính kèm)

Loại bug: **Hiển thị nội dung form Sửa phụ thuộc việc biểu mẫu ĐÃ CÓ file.** Đối tác kỳ vọng form Sửa hiển thị file đang đính kèm; thực tế vùng "File biểu mẫu" chỉ có ô tải trống. Verdict phụ thuộc: role + biểu mẫu thực sự có file + mở đúng form Sửa.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLBMHD_13.webm, frame t08.08s) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Biểu mẫu có file đính kèm | BM-20260713-001 "TKM test" — **có file XLSX 52.2 KB** (frame detail t14/t16) | BM-20260715-001 "QA BM001 Hidden Parent 715" — **có file** (943 B, icon file-word, có nút Tải về) | Không |
| Trạng thái biểu mẫu | Đã ẩn (partner) | Nháp (mình) — form Sửa dùng chung một component, không phụ thuộc state | Không |
| Màn kiểm | Form Chỉnh sửa (`/bieu-mau/<id>/sua`) | Form Chỉnh sửa (`/bieu-mau/28104008.../sua`) | Không |

**Kết luận: 0 GAP.** Tái hiện đúng: form Sửa của biểu mẫu ĐÃ CÓ file hiển thị vùng "File biểu mẫu" là **ô tải trống** ("Kéo thả hoặc click để chọn file"), KHÔNG thể hiện file hiện đang đính kèm.
- Xác minh real-data (`evaluate_script`): section "File biểu mẫu" = chỉ dropzone trống; `uploadListItemCount = 0`; không có link tải file cũ trong form (`hasDownloadLinkInForm = false`). Screenshot form Sửa: `reverify-audit/QLBMHD_13/QLBMHD_13-edit-form-no-file.png`.

Đối chiếu SRS:
- SRS `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:652` (SCR-VII-02 #15 — File đính kèm, "khi tạo/**sửa**", Bắt buộc).
- SRS `:372` (FR-VII-04 AC): chỉnh sửa = "cập nhật + **upload lại file (nếu cần)**" → tái upload là TÙY CHỌN, hàm ý file cũ được giữ lại.

→ SRS **không có clause minh thị** yêu cầu form Sửa phải hiển thị/preview file hiện tại. Mẫu "ô upload trống = giữ file cũ" là pattern hợp lệ phổ biến. Chưa test được hành vi Lưu (env session TTL ngắn) để phân biệt "giữ file" vs "chặn/mất file". → **`BA confirm`** (KHÔNG Reject — hành vi tái hiện đúng; KHÔNG Open — chưa chứng minh vi phạm clause SRS / functional break). Nếu BA yêu cầu form phải hiển thị file hiện tại, HOẶC nếu Lưu-không-upload bị chặn/mất file → chuyển Open (Dev FE).

Chi tiết: [`../ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-batch5.md`](../ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-batch5.md) (QLBMHD_13).
