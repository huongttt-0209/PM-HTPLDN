# QLBMHD_13 — Real-data DOM evidence (form Sửa, env 18.143.165.120.nip.io)

Tài khoản: `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP·TW). Ngày 2026-07-20.
Biểu mẫu: BM-20260715-001 "QA BM001 Hidden Parent 715" (Nháp, có file 943 B / file-word).
URL form Sửa: `/bieu-mau/28104008-7b0d-4783-9825-a188ad11a289/sua`.

## Kết quả `evaluate_script` trên form Sửa đang mở

```json
{
  "sectionText": "File biểu mẫu\n\nKéo thả hoặc click để chọn file\n\nChỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB",
  "uploadListItemCount": 0,
  "uploadListItems": [],
  "fileNameMatchesInForm": [" .doc", " .docx", " .xls", " .xlsx"],
  "hasDownloadLinkInForm": false
}
```

Diễn giải: vùng "File biểu mẫu" trong form Sửa chỉ chứa ô tải trống; KHÔNG có mục file đã tải (`uploadListItemCount = 0`), KHÔNG có tên file thực (các match chỉ là chuỗi gợi ý ".doc/.docx..." trong dòng "Chỉ chấp nhận"), KHÔNG có link tải file cũ. → Form Sửa không thể hiện file đang đính kèm dù biểu mẫu có file.

## Đối chiếu evidence đối tác
- `frames/t008.08s.jpg`: form Chỉnh sửa BM-20260713-001 "TKM test" (XLSX 52.2 KB) — vùng "File biểu mẫu" cũng là ô tải trống "Kéo thả hoặc click để chọn file". Khớp hành vi env mình.

## Chưa test được (env session TTL ngắn ~1-2 phút, không silent-refresh)
- Hành vi khi bấm "Lưu" mà KHÔNG upload file lại: có chặn "file bắt buộc" không / file cũ có được giữ không. → cần test bổ sung để xác định Open (functional break) vs BA confirm (display gap).
