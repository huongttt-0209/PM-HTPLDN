# Bảng đối chiếu điều kiện — NHSYC_01 (kiểm lại trên môi trường UAT mới)

**Loại bug:** phụ thuộc **thao tác + dữ liệu nhập** (tạo hồ sơ có tệp đính kèm) ⇒ **KHÔNG phải bug tĩnh** → bắt buộc điền bảng này.
**Bối cảnh:** dev báo đã dựng bản vá lên môi trường `https://htpldn-uat.ospgroup.vn`. Bản dựng ghi ở thanh bên: **HTPLDN · V1.0.5**.

| Điều kiện có thể đổi kết quả | Điều kiện gốc của phiếu | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương (`CB_NV_TW`) — người được phép nhập hồ sơ thủ công | `cbnv_tw`, vai trò `CB_NV_TW`, đơn vị hiển thị "Bộ Tư Pháp · Cục Bổ trợ tư pháp", `donViId` `00000000-0000-4000-8000-000000000001` | Không |
| Màn hình / thao tác | Vụ việc HTPL → **[Nhập thủ công]** → điền hồ sơ → **[Lưu & Tiếp nhận]** | Đúng đường đi đó, đi bằng giao diện (không gọi API tắt) | Không |
| Có tệp đính kèm hay không | **CÓ** tệp đính kèm — đây là điều kiện tạo ra lỗi ở lượt trước | CÓ. Lần 1: `uat-dinh-kem-nhsyc01.pdf` (402 B). Lần 2: `QLKTLBG_10-pdf-that-QA-retest0804.pdf` (1.6 KB) | Không |
| Định dạng / dung lượng tệp | Trong giới hạn biểu mẫu công bố: PDF, ≤ 20MB/tệp, tổng ≤ 100MB | Cả 2 tệp đều là PDF thật, 402 B và 1.6 KB — thừa sức trong giới hạn | Không |
| Doanh nghiệp gắn vào hồ sơ | DN có sẵn trong hệ thống (đủ mã số thuế + tên) | `Công ty TNHH Mẫu Test`, MST `0101234567`, mã `DN-XX-0005`, `id` `1a715c55-bc31-46de-ae07-56dd4f403ce5` | Không |
| Trường Độ ưu tiên | **Để trống** để hệ thống tự tính (phần B của phiếu) | Để trống ở cả 2 lần | Không |
| Hồ sơ doanh nghiệp dùng để tự tính ưu tiên | DN không có dữ liệu ưu tiên ⇒ theo đặc tả phải ra mức thấp nhất | Đã mở hồ sơ DN kiểm từng ô: Quy mô, Số lao động, Số lao động nữ, Số lao động khuyết tật đều **trống**; công tắc "Nữ làm chủ" **tắt** | Không |
| Số lần đo | — | **2 lần độc lập**, 2 hồ sơ khác nhau (`VV-BTP-TW-20260804-001`, `VV-BTP-TW-20260804-002`), 2 tệp khác nhau, kết quả trùng khớp | Không |

**Số ô GAP còn lại: 0** → đủ điều kiện chốt verdict.

---

## Loại trừ khả năng "do môi trường / kho lưu trữ hỏng"

Trước khi kết luận, đã kiểm chứng ngay trên **cùng môi trường, cùng phiên**: hồ sơ `VV-BTP-TW-20260803-002` có 4 tài liệu, tất cả đều hiện **đúng tên gốc** (`2K15 T3 (4.8) & CN (9.8).pdf`, `Báo cáo mẫu.docx`...), **đúng định dạng** (PDF, DOCX), **đúng dung lượng** (264.361 B, 19.725 B) và **tải về được** (máy chủ trả 200).

⇒ Kho lưu trữ và phần hiển thị tài liệu đều hoạt động bình thường. Lỗi chỉ xảy ra với tệp được đính kèm **ngay tại biểu mẫu tạo hồ sơ mới**.

---

## Đối chiếu SRS

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

**1. Tên tài liệu là trường bắt buộc.**
- Đặc tả `srs-fr-05-vu-viec.md:2057` — `ten_tai_lieu` · text · Bắt buộc **Y** · "Tên tài liệu".
- Phần mềm: hiện `File đính kèm 3131f695` / `File đính kèm f71dff61` — chuỗi máy sinh từ mã tệp, không phải tên người dùng tải lên.

**2. Tên tệp gốc phải được giữ.**
- Đặc tả `srs-fr-05-vu-viec.md:2223` — `ten_file` · text · Bắt buộc **Y** · "**Tên file gốc**".
- Phần mềm: máy chủ nhận đúng `uat-dinh-kem-nhsyc01.pdf` ở bước tải lên, nhưng bảng tài liệu của hồ sơ không dùng tên đó.

**3. Bảng tài liệu phải nêu tên + kích thước.**
- Đặc tả `srs-fr-05-vu-viec.md:1695` — "Danh sách file đã upload · Table nhỏ · **Tên file, Kích thước, Ngày upload**, Nút [Xóa]".
- Phần mềm: cột Định dạng để trống, cột Kích thước hiện `—`.

**4. Đường dẫn tệp là bắt buộc.**
- Đặc tả `srs-fr-05-vu-viec.md:2059` — `duong_dan_file` · text · Bắt buộc **Y** · "Đường dẫn file".
- Phần mềm: đường dẫn hệ thống trả về trỏ tới một khóa không tồn tại trong kho ⇒ bấm Xem / Tải đều thất bại.

**5. Ưu tiên tự tính khi DN không có dữ liệu ưu tiên.**
- Đặc tả `srs-fr-05-vu-viec.md:196` — "Nếu trường nào NULL/0 thì điểm tương ứng = 0 (không chặn). **Tối thiểu `uu_tien=1` (FIFO)** cho mọi VV".
- Phần mềm: lưu `uuTien = 1` — **đúng đặc tả**.

**6. Nhãn hiển thị ứng với giá trị 1.**
- Đặc tả `srs-fr-05-vu-viec.md:1526` — giá trị `1` → nhãn UI "**Thấp**", màu xám nhạt.
- Phần mềm: giao diện hiển thị "**Rất cao**".

> Lưu ý về mức độ ràng buộc của dòng 1526: `srs-fr-05-vu-viec.md:1522` ghi bảng nhãn là "**đề xuất, cần CĐT xác nhận**". Vì vậy phần *chọn chữ nào* thuộc thẩm quyền BA/CĐT. Nhưng *chiều* của thang thì không mơ hồ: 1 là đầu **thấp nhất** của thang 1–5 (`srs-fr-05-vu-viec.md:326` — `uu_tien` … BETWEEN 1 AND 5), trong khi phần mềm đang gắn cho nó nhãn nghe **cao nhất**. Đây là đảo chiều, không phải khác biệt cách gọi tên.
