# Audit QLHSDNHTCP_11 — Nhóm 1 Thông tin doanh nghiệp (màn Chi tiết)

- **Verdict:** Open (ghi sheet row 20, P20, 2026-07-20).
- **Tài khoản:** cbnv_tw (CB_NV_TW, BTP·TW). Env https://18.143.165.120.nip.io. Data seed 10 hồ sơ CT-SEED-101→110.
- **Hồ sơ verify:** CT-SEED-103 (`/chi-tra/3cc417aa-...`), Yêu cầu bổ sung.

## Cổng 1 — Evidence đối tác
- Kết quả thực tế đối tác (sheet L20): "Hiển thị thiếu trường thông tin so với tài liệu mô tả".
- Mô tả: "Nhóm 1 — Thông tin doanh nghiệp (chỉ đọc, lấy từ Cổng Dịch vụ công)".

## Cổng 3 — SRS vs Web (data thật)
| SRS SCR-V.II-02 #5 (`:981`, "Luôn") | Web (CT-SEED-103) | Đạt |
|---|---|:-:|
| Tên doanh nghiệp | Công ty TNHH Seed Publishable | ✅ |
| Địa chỉ | (không hiển thị) | ❌ thiếu |
| Số điện thoại / Fax / Email | (không hiển thị) | ❌ thiếu |
| Mã số doanh nghiệp | Mã số thuế 0100000001 | ✅ |
| Giấy chứng nhận đăng ký kinh doanh | (không hiển thị) | ❌ thiếu |
| Ngành nghề | (không hiển thị) | ❌ thiếu |
| Người đại diện | (không hiển thị) | ❌ thiếu |
| Loại hình doanh nghiệp | (không hiển thị) | ❌ thiếu |
| Quy mô doanh nghiệp | Nhỏ | ✅ |

## Phân biệt bug thật vs seed gap (BẮT BUỘC — bug dạng "absence")
- Data nguồn ĐÃ CÓ: GET `/api/v1/doanh-nghieps/5eed0010-...` trả `diaChi`="So 10 Pho Test, Quan Ba Dinh, Ha Noi", `dienThoai`="0243777888", `email`="seed.publishable@test.htpldn.vn", `nganhNghe`="THUONG_MAI", `nguoiDaiDien`="Nguyen Van Seed", `loaiDnId` có giá trị.
- Nhưng GET `/api/v1/ho-so-chi-tras/{id}` (data màn chi tiết) chỉ project khối `doanhNghiep`={id, ten, maSoThue} → FE không có dữ liệu 6 trường để render.
- → **KHÔNG phải seed gap (nhóm A)**: dữ liệu tồn tại, chỉ là màn chi tiết chi trả không surface. Đây là lỗi thật (BE thiếu projection / FE thiếu field), tái hiện độc lập role/state/hồ sơ.
- Đã loại trừ: (1) đúng role có quyền xem chi tiết; (2) đúng màn (SCR-V.II-02); (3) state Yêu cầu bổ sung hợp lệ; (4) data có; (5) tái hiện đúng note đối tác. Retry method 2 (curl API) xác nhận data tồn tại nhưng không được trả trong response chi tiết.

## Kết luận
- **Open** — màn Chi tiết hồ sơ chi trả, mục Thông tin Doanh nghiệp thiếu 6 trường SRS component #5 yêu cầu ("Luôn") dù dữ liệu đã có. Log BUG-QLHSDNHTCP_11 (Major). Ghi chú thêm: các trường tiền (Số tiền đề nghị, Phí tư vấn) app đặt trong mục Thông tin DN nhưng theo SRS thuộc Accordion II (component #6) — lệch cấu trúc section, gộp mô tả không tách bug riêng.
- Bug tĩnh (static): thiếu trường không phụ thuộc vai trò/trạng thái/hồ sơ → ghi sheet dùng `--static-bug`.
