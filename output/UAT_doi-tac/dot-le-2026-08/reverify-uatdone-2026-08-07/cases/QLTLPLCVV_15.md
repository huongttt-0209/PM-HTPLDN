# QLTLPLCVV_15 — Tải lên tệp đính kèm chứa mã độc (sheet `bug` row 299)

**Đợt:** re-verify trên MÔI TRƯỜNG NGHIỆM THU `https://htpldn-uat.ospgroup.vn`
**Ngày đo:** 2026-08-07
**Bản dựng:** V1.0.10 · bó mã `index-Bd1akG3f.js`
**Tài khoản:** `cbnv_tw` — Cán bộ Nghiệp vụ Trung ương
**Bản ghi:** TVCS-20260806-0001 (TKM Company, Tiếp nhận) → tư liệu "TKM kiểm thử chức năng" (Nháp)

## Verdict: ✅ PASS → `Trạng thái dev fix` = `UAT done`

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Bug gốc (phiếu đối tác) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ đăng nhập hệ thống | `cbnv_tw` — Cán bộ Nghiệp vụ Trung ương | Không |
| Màn + thao tác | Tư vấn chuyên sâu → Chi tiết → Nhóm 3 Tư liệu pháp lý liên kết → cửa sổ chỉnh sửa → Tải tệp | Đúng y luồng đó (cửa sổ "Sửa tư liệu pháp luật") | Không |
| Dữ liệu tiền đề | Tư liệu có thể chỉnh sửa | Tư liệu "TKM kiểm thử chức năng" trạng thái Nháp | Không |
| Input (tệp nạp lên) | Tệp chứa mã độc | PDF hợp lệ 732 byte nhúng chữ ký thử mã độc chuẩn EICAR | Không |

0 GAP → đủ điều kiện chốt verdict.

## Kết quả đo

**Thao tác chính — nạp tệp chứa mã độc:**

Thông báo hiện trên màn: **"Tệp «A-eicar-nhung-trong-pdf-hop-le.pdf» chứa mã độc, không thể tải lên"**
→ **khớp nguyên văn** "Kết quả mong đợi" của phiếu. Triệu chứng cũ ("Tải file thất bại") đã hết.

- **1 request / 1 khung thông báo** (không lặp) — đo bằng `tools/toast-capture.js`, đã tự kiểm `soObserverDangSong = 1` trước khi tin số liệu.
- Tệp **không** được thêm vào danh sách đính kèm sau khi bị chặn.
- Lặp lại **3 lượt độc lập** (2 lượt qua hộp chọn tệp thật, 1 lượt qua sự kiện chọn tệp) — cả 3 cho kết quả giống hệt nhau.

**Bằng chứng cứng — phản hồi máy chủ của chính thao tác đó** (`POST /api/v1/tu-lieu-phap-ly-vvs/upload`):

```
HTTP 400
{"success":false,"error":{"code":"ERR-TLPL-04",
 "message":"Tệp «A-eicar-nhung-trong-pdf-hop-le.pdf» chứa mã độc, không thể tải lên", ...}}
```

Phần thân request bắt được nguyên chữ ký `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*`
→ chứng minh tệp gửi lên đúng là tệp mang chữ ký thử mã độc, không phải chặn nhầm vì lý do khác.

**Phép thử đối chứng — tệp sạch không bị chặn oan:** nạp PDF sạch cùng cấu trúc → 1 request, **0 thông báo lỗi**,
tệp vào danh sách đính kèm bình thường. Bộ quét phân biệt được sạch/bẩn, không chặn tất cả.

Bằng chứng ảnh: [image/QLTLPLCVV_15-toast-chan-ma-doc-uat.png](../image/QLTLPLCVV_15-toast-chan-ma-doc-uat.png)
(bắt trạng thái sau khi bị chặn: tệp mã độc KHÔNG có trong danh sách đính kèm).

## Đối chiếu SRS

| SRS yêu cầu | Dẫn nguồn | Thực tế |
|---|---|---|
| Bước 3 của luồng tải lên là "Quét virus" | `srs-fr-12-tv-chuyen-sau.md:885` | Có — bị chặn ở đúng bước quét |
| Tệp chứa mã độc → mã lỗi `ERR-TLPL-04`, thông báo nêu tên tệp | `srs-fr-12-tv-chuyen-sau.md:982` | **Khớp mã lỗi `ERR-TLPL-04`** + có tên tệp |
| Ràng buộc định dạng PDF/DOCX/XLS/ảnh, tối đa 20MB | `srs-fr-12-tv-chuyen-sau.md:856` | Khớp (form ghi rõ, tệp thử là PDF hợp lệ) |
| Mọi tệp nạp lên phải quét antivirus trước khi lưu | `srs-v3.5.md:865` (EC-FILE-SCAN) · `srs-v3.5.md:5701` (BR-EC-03) | Khớp |

UC: `srs-fr-12-tv-chuyen-sau.md:824` — **UC 152** (FR-X.1-06).

> **Ghi chú về câu chữ thông báo:** SRS có 3 biến thể câu chữ cho cùng hành vi này
> (`:982` "File '{ten_file}' chứa mã độc" · `:540`/`:810` "Tệp '{ten_file}' chứa mã độc, không thể tiếp nhận"
> · `srs-v3.5.md:865` "Tệp chứa mã độc, không thể upload"). Phần mềm dùng câu trùng khít kỳ vọng của phiếu
> và đúng mã lỗi mà FR sở hữu màn này quy định → không có mâu thuẫn ảnh hưởng verdict.

## Ngoài phiếu này, có thấy gì bất thường không?

Có 1 điểm nghi vấn đã **kiểm tra và loại trừ**: tư liệu đang có sẵn tệp đính kèm tên `eicar.pdf` (3.235 byte,
tạo 06/08/2026). Tên gọi dễ khiến hiểu là mã độc đã lọt vào hệ thống. Đã tải tệp đó về đọc nội dung:
là PDF sạch do Word sinh (`%PDF-1.5`), **không chứa chữ ký EICAR** → chỉ là tên tệp gây hiểu nhầm,
không phải mã độc tồn kho. Không log bug.

Không phát hiện thêm điểm bất thường nào khác.

> Dữ liệu đối tác không bị thay đổi: đã bấm Hủy, kiểm lại tư liệu vẫn `version 1` với đúng 2 tệp cũ.
