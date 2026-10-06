# Bảng đối chiếu điều kiện — QLKCHTV_10 (row 5) — Nhập Excel: nhãn cột Nguồn

**Kết luận:** Open, BA confirm.
- **Open** — nhãn nguồn hiển thị "Import" (tiếng Anh) trong khi 2 giá trị còn lại cùng cột đã Việt hoá ("Thủ công", "Tự động").
- **BA confirm** — đặc tả v3.5 KHÔNG quy định nhãn tiếng Việt cho `IMPORT`, chỉ quy định màu thẻ; cần BA chốt chữ hiển thị.
- Phần còn lại của kỳ vọng ĐẠT: bản ghi vào đúng trạng thái "Chờ duyệt".

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_10(1)-1.jpg`, `-2.jpg`) | Mình test (env nip.io, 27/07/2026 11:12) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", badge "BTP · TW" (đọc rõ góc phải trên cả 2 ảnh) | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP. Cũng là vai trò duy nhất có `CRUD*` trên `KHO_CAU_HOI` theo `srs-v3.5.md:1325` | Không |
| Entity + trạng thái (state machine) | Bản ghi mới sinh từ luồng import, hiển thị Trạng thái "Chờ duyệt" (QA-20260720-0007/-0003/-0006/-0005/-0008) | Bản ghi mới sinh từ luồng import: QA-20260727-0002/-0003/-0004, Trạng thái "Chờ duyệt" — TRÙNG KHỚP | Không |
| Dữ liệu tiền đề | Cần 1 file .xlsx đúng mẫu; đối tác nhập 12 dòng (7 thành công, 5 lỗi) | **Đã tự dựng tiền đề**: tải chính "File mẫu" của hệ thống rồi điền 5 dòng (3 hợp lệ + 2 mã lĩnh vực sai) để tái hiện đúng tình huống "có dòng hợp lệ, có dòng lỗi" | Không |
| Input / filter / giá trị nhập | Không lọc; đọc cột "Nguồn" trên bảng sau khi nhập xong | Không lọc; đọc cột "Nguồn" trên bảng **và** trên màn chi tiết **và** trên file Excel xuất ra — 3 nơi cùng cho "Import" | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render + Hành vi luồng)

- `bug-reports/image/BUG-QLKCHTV_10-preview-loi-ma-linh-vuc.png` — đã mở đọc: bước 2 "Xem trước", Tổng dòng 5 / Hợp lệ 3 / Lỗi 2, kèm bảng lỗi có lý do từng dòng.
- `bug-reports/image/BUG-QLKCHTV_10-ketqua-nhap.png` — đã mở đọc: bước 3 "Kết quả" — *"Đã nhập 3 câu hỏi"*, *"2 dòng bị bỏ qua do lỗi."*; phía sau hộp thoại đã thấy dòng mới có thẻ **"Import"** + **"Chờ duyệt"**.
- File nhập dùng làm bằng chứng: `reverify-audit/QLKCHTV_10/files/kho-cau-hoi-import-QA-tuan4.xlsx`.
- Đọc thẳng bảng sau khi nhập:
  `QA-20260727-0002 | ... | Import | Chờ duyệt`, `QA-20260727-0003 | ... | Import | Chờ duyệt`, `QA-20260727-0004 | ... | Import | Chờ duyệt`.

## Phương pháp thứ hai (bắt buộc)

- **Tầng dữ liệu (API) so với tầng hiển thị:** `GET /api/v1/kho-cau-hois` trả `"nguon":"IMPORT"` — đúng enum đặc tả (`srs-fr-13-tv-nhanh.md:102` và `:688` khai đúng 3 giá trị `TU_DONG / THU_CONG / IMPORT`). Vậy dữ liệu KHÔNG sai; sai lệch nằm ở chữ hiển thị.
- **Đối chứng nội bộ cùng một cột:** cùng cột "Nguồn", `TU_DONG` → hiển thị **"Tự động"**, `THU_CONG` → **"Thủ công"**, riêng `IMPORT` → giữ nguyên **"Import"**. Hai giá trị kia đã Việt hoá ⇒ đây là thiếu sót Việt hoá của riêng 1 giá trị, không phải quy ước "hiển thị enum thô".
- **Đối chiếu đặc tả:** `srs-fr-13-tv-nhanh.md:532` chỉ quy định **màu thẻ** — *"TU_DONG (xanh duong, ...) / THU_CONG (vang, ...) / IMPORT (tim, ...)"*. Ứng dụng đang hiển thị thẻ **màu tím** cho IMPORT ⇒ ĐÚNG phần màu. Đặc tả **im lặng** phần chữ ⇒ chữ cụ thể phải để BA chốt.
- **Đo bằng 3 bề mặt độc lập:** bảng danh sách, màn chi tiết, và file Excel xuất ra (`reverify-audit/QLKCHTV_12/files/lan1-kho-cau-hoi-20260727.xlsx`, cột E) — cả 3 đều "Import" ⇒ không phải lỗi render cục bộ 1 màn.
- **Phần kỳ vọng còn lại ĐẠT:** đặc tả `srs-fr-13-tv-nhanh.md:116` (*"Nguồn IMPORT: ... -> trạng thái = CHO_DUYET"*) và `:535` (*"Tat ca -> CHO_DUYET"*) — đo thực tế: cả 3 bản ghi đều "Chờ duyệt", thông báo *"Đã nhập 3 câu hỏi, chờ duyệt"*, đo bằng bộ bắt thông báo dùng chung: `SO_REQUEST = 1` (`POST /api/v1/kho-cau-hois/import/confirm`), `SO_KHUNG_THONG_BAO = 1`, không lặp.
