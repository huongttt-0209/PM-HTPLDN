# Audit QLHSDNHTCP_19 — Sắp xếp theo cột (màn Danh sách)

- **Verdict:** BA confirm (ghi sheet row 23, P23, 2026-07-20).
- **Tài khoản:** cbnv_tw (CB_NV_TW, BTP·TW). Env https://18.143.165.120.nip.io. Màn `/chi-tra/danh-sach`, data thật CT-SEED-101→110.

## Cổng 1 — Evidence đối tác
- Kết quả thực tế đối tác (sheet): "Hệ thống không thực hiện sắp xếp khi nhấn vào tên cột".
- Kết quả mong đợi đối tác: "Hệ thống sắp xếp danh sách theo cột đó, luân phiên tăng dần / giảm dần qua mỗi lần bấm."

## Cổng 2 — Tái hiện (web, data thật)
- Bấm tên cột (Mã HS, Số tiền đề nghị, Trạng thái, Ngày nộp) → danh sách KHÔNG đổi thứ tự.
- DOM inspect: list render dạng div-grid (không phải `<table>` AntD). `any_sortable_marker`=0 → không phần tử nào có class `sort` / `[aria-sort]` / `.ant-table-column-sorter` / `.ant-table-column-has-sorters`.
- Behavioral test bấm header "Số tiền đề nghị": thứ tự dòng giữ nguyên (CT-SEED-108/109/110/101/102...), giá trị số tiền không sắp (8.000.000 / 7.000.000 / 8.500.000 / 6.000.000 / 9.000.000). `anySorterActive`=false.
- ⇒ Xác nhận đúng: app không hỗ trợ click-sort cột trên màn Chi trả.

## Cổng 3 — SRS đối chiếu
| Nguồn SRS | Nội dung | Kết luận |
|---|---|---|
| SCR-V.II-01 bảng cột (`srs-fr-06-chi-tra.md:918-938`) | Cột "Hành vi" mọi cột = "—" (không có tương tác click-sort) | Chi trả KHÔNG yêu cầu click-sort |
| SCR-V.II-01 (`:958`) | "Sắp xếp mặc định: ngày cập nhật DESC" | chỉ default sort, không click-sort |
| Vụ việc HTPL (`srs-fr-05:1654`) | cột có hành vi sắp xếp | module khác CÓ click-sort |
| Quản trị hệ thống (`srs-fr-10:1573`) | cột có hành vi sắp xếp | module khác CÓ click-sort |
| Hỏi đáp pháp lý (`srs-fr-02:1043`) | cột có hành vi sắp xếp | module khác CÓ click-sort |

## Vì sao BA confirm (không phải Open, không phải Reject)
- Xét RIÊNG module Chi trả: SRS SCR-V.II-01 không mô tả click-sort ("Hành vi=—"), nên app đúng spec → không đủ căn cứ Open.
- Nhưng KHÔNG thể Reject dứt khoát: các module sibling (Vụ việc, Quản trị, Hỏi đáp) đều có click-sort → hệ thống không đồng nhất. Đây là mâu thuẫn spec cấp cross-module cần BA chốt: click-sort là chuẩn chung hay chỉ áp cho màn có "Hành vi=sắp xếp".
- Bug tĩnh (behavior list-level, không phụ thuộc vai trò/trạng thái/seed) → ghi sheet dùng `--static-bug`.

## Kết luận
- **BA confirm** — hành vi app khớp SRS Chi trả nhưng lệch chuẩn sibling modules → cần BA quyết phạm vi yêu cầu click-sort. Log §QLHSDNHTCP_19 trong ../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md.
