# Audit QLHSDNHTCP_13 — Nhóm 8 Thông tin phê duyệt & Lịch sử (màn Chi tiết)

- **Verdict:** Open (ghi sheet row 22, P22, 2026-07-20).
- **Tài khoản:** cbnv_tw (CB_NV_TW, BTP·TW). Env https://18.143.165.120.nip.io.
- **Hồ sơ verify:** CT-SEED-107 (`/chi-tra/07e3d4df-...`), trạng thái **Đã duyệt** (chọn hồ sơ đã duyệt để chắc chắn có dữ liệu phê duyệt).

## Cổng 1 — Evidence đối tác
- Kết quả thực tế đối tác (sheet L22): "Màn hình không có trường Thông tin phê duyệt".
- Mô tả: "Nhóm 8 — Thông tin phê duyệt và Lịch sử xử lý".

## Cổng 3 — SRS vs Web (data thật)
| SRS SCR-V.II-02 #35 (`:1011`, "Luôn") | Web (CT-SEED-107 Đã duyệt) | Đạt |
|---|---|:-:|
| Section "Thông tin phê duyệt & Lịch sử": Ngày tiếp nhận, Người tiếp nhận, Thời gian phê duyệt, Người phê duyệt, Thời gian/Người/Lý do từ chối, Lý do hủy | KHÔNG có section — mục cuối là Cập nhật thanh toán → Lịch sử xử lý | ❌ thiếu section |
| #36 Timeline "Lịch sử xử lý" (`:1012`) | Có section nhưng trống ("Chưa có lịch sử xử lý", lichSu=[]) | ~ (seed gap AUDIT_LOG) |

## Phân biệt bug thật vs seed/state gap
- Chọn hồ sơ **Đã duyệt** CT-SEED-107 để loại trừ "chưa duyệt nên chưa có data".
- Data phê duyệt ĐÃ CÓ: GET `/api/v1/ho-so-chi-tras/07e3d4df-...` trả `ngayTiepNhan`="2026-06-26", `nguoiTiepNhanId` set, `nguoiDuyetId`="4101cf26-...", `ngayDuyet`="2026-07-03", `nguoiGuiDuyetId` set, `ngayGuiDuyet`="2026-07-01".
- Màn chi tiết vẫn không có section "Thông tin phê duyệt" → **KHÔNG phải state/seed gap** cho phần section này: dữ liệu có, section vắng mặt hoàn toàn → lỗi thật.
- Section "Thông tin phê duyệt" cũng vắng mặt trên hồ sơ khác (CT-SEED-103) → structural, không phụ thuộc trạng thái.

## Kết luận
- **Open** — màn Chi tiết hồ sơ chi trả thiếu hẳn section "Thông tin phê duyệt" (component #35, "Luôn") dù dữ liệu tiếp nhận/phê duyệt đã có. Log BUG-QLHSDNHTCP_13 (Major).
- Phần "Lịch sử xử lý" trống là seed gap AUDIT_LOG (component #36) — không thuộc bug này, không log riêng (đúng phân loại: empty state hợp lệ khi thiếu seed).
- Bug tĩnh (structural): section vắng mặt không phụ thuộc vai trò/trạng thái → ghi sheet dùng `--static-bug`.
