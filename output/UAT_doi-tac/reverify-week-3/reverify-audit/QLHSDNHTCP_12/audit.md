# Audit QLHSDNHTCP_12 — Nhóm 2 Thông tin tư vấn (màn Chi tiết)

- **Verdict:** Open (ghi sheet row 21, P21, 2026-07-20).
- **Tài khoản:** cbnv_tw (CB_NV_TW, BTP·TW). Env https://18.143.165.120.nip.io. Hồ sơ CT-SEED-103.

## Cổng 1 — Evidence đối tác
- Kết quả thực tế đối tác (sheet L21): "Hiển thị thiếu trường thông tin so với tài liệu mô tả và các không hiển thị các thông tin hiện có trên màn hình".
- Mô tả: "Nhóm 2 — Thông tin tư vấn (chỉ đọc, lấy từ Cổng DVC)".

## Cổng 3 — SRS vs Web (data thật)
| SRS SCR-V.II-02 #6 (`:982`, "Luôn") | Web (CT-SEED-103) | Đạt |
|---|---|:-:|
| Vụ việc vướng mắc | ~ (Mã vụ việc + Tiêu đề vụ việc, "—") | ~ |
| Thời điểm phát sinh | (không có nhãn) | ❌ thiếu |
| Tên tư vấn viên | Họ tên TVV ("—") | ✅ nhãn |
| Tổ chức hành nghề | (không có nhãn) | ❌ thiếu |
| Địa chỉ tư vấn viên | (không có nhãn) | ❌ thiếu |
| Số điện thoại tư vấn viên | (không có nhãn) | ❌ thiếu |
| Số ngày hợp đồng TVPL | (không có nhãn) | ❌ thiếu |
| Phí tư vấn | Hiển thị ở mục Thông tin DN (sai vị trí) | ~ |
| Số tiền đề nghị hỗ trợ | Hiển thị ở mục Thông tin DN (sai vị trí) | ~ |

## Phân biệt bug thật vs seed gap
- 10 hồ sơ seed đều `tuVanVienId`=null, `vuViecId`=null (verify CT-SEED-103/106/107/108) → giá trị TVV hiển thị "—" là do chưa gắn TVV (data gap cho phần GIÁ TRỊ).
- NHƯNG phần THIẾU NHÃN TRƯỜNG (Thời điểm phát sinh / Tổ chức hành nghề / Địa chỉ TVV / SĐT TVV / Số ngày HĐ TVPL) là **structural** — mục render 4 nhãn cố định, không phụ thuộc có/không TVV → lỗi thật, tái hiện độc lập dữ liệu.
- Phần "không hiển thị thông tin hiện có": hồ sơ có `soHopDongTvpl`, `ngayHopDong`, `noiDungDeNghiTt` (data tồn tại) nhưng màn không surface → lỗi thật (giống bản chất _11).

## Kết luận
- **Open** — mục Thông tin Tư vấn viên thiếu 5 nhãn trường SRS #6 yêu cầu ("Luôn") + không hiển thị thông tin hợp đồng/đề nghị đã có. Log BUG-QLHSDNHTCP_12 (Major).
- Giới hạn verify: phần TVV có GIÁ TRỊ (Tên/Tổ chức/Địa chỉ TVV populate khi gắn TVV) chưa test được do seed thiếu TVV linkage — nhưng không ảnh hưởng kết luận Open vì nhãn trường đã thiếu ở FE.
- Bug tĩnh (structural): thiếu nhãn không phụ thuộc vai trò/trạng thái → ghi sheet dùng `--static-bug`.
