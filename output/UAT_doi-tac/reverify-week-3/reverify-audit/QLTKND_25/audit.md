# Audit QLTKND_25 — Sắp xếp theo cột (màn Quản lý tài khoản, SCR-VIII-03)

- **Verdict:** BA confirm (row 170, P170, 2026-07-21).
- **Tài khoản:** admin (QTHT). Env https://18.143.165.120.nip.io. Màn `/quan-tri/tai-khoan`, 27 tài khoản thật.

## Cổng 1 — Evidence đối tác
- Kết quả thực tế đối tác: bấm tên cột KHÔNG sắp xếp (mặc định "Lần đăng nhập cuối" giảm dần).
- Kết quả mong đợi đối tác: bấm tên cột → danh sách sắp xếp theo cột đó, luân phiên tăng/giảm.

## Cổng 2 — Tái hiện (web, data thật, 2 method)
- **DOM inspect:** 10 header (`.ant-table-thead th`) — KHÔNG cột nào có `ant-table-column-has-sorters` / `.ant-table-column-sorter` / `[aria-sort]` (tất cả `hasSorter=false`, `hasSortCaret=false`, `ariaSort=null`).
- **Behavioral:** click header "Tên đăng nhập" → thứ tự dòng GIỮ NGUYÊN (qa_tvv_dp_r18 / qa_tvv_tw_r19 / qa_tvv_rv5_thamdinh / qa_tvv_rv4_thamdinh / qa_tvv_rvpd08_approve / cbpd_hn — trước = sau), KHÔNG có request `?sortBy=` (`sortRequests=[]`).
- ⇒ Xác nhận đúng: màn Tài khoản không hỗ trợ click-sort cột. Ảnh `web-cot-khong-sort.png`.

## Cổng 3 — SRS đối chiếu
| Nguồn SRS | Nội dung | Kết luận |
|---|---|---|
| SCR-VIII-03 bảng Thành phần màn hình cột 10–16 (`srs-fr-10-quan-tri.md:1636-1673`) | Cột "Hành vi": Username="click → chi tiết", Họ tên/Email/Đơn vị/Vai trò/Trạng thái="—" | Màn Tài khoản KHÔNG mô tả click-sort cột |
| SCR-VIII-01 danh mục (`srs-fr-10-quan-tri.md:1572`, `:1608`) | Cột **Tên** có sort (STT69), các cột khác không | Màn danh mục CÙNG module CÓ click-sort (chỉ cột Tên) |
| Vụ việc HTPL (`srs-fr-05:1654`) · Hỏi đáp (`srs-fr-02:1043`) | cột có hành vi sắp xếp | module sibling CÓ click-sort |

## Vì sao BA confirm (không Open, không Reject)
- Xét RIÊNG màn Tài khoản (SCR-VIII-03): SRS không mô tả click-sort ("Hành vi=—") → app đúng spec → không đủ căn cứ **Open**.
- KHÔNG thể **Reject** dứt khoát: sibling screens (danh mục SCR-VIII-01 cùng module, Vụ việc, Hỏi đáp) đều có click-sort → hệ thống không đồng nhất. Cần BA quyết click-sort là chuẩn chung hay chỉ áp cho màn có "Hành vi=sắp xếp".
- Bug tĩnh (behavior list-level, không phụ thuộc vai trò/trạng thái/seed) → ghi sheet dùng `--static-bug`.
- **Đồng nhất precedent QLHSDNHTCP_19 (row 23, BA confirm)** — cùng bản chất "màn không spec sort nhưng sibling có sort".

## Kết luận
- **BA confirm** — app khớp SRS màn Tài khoản (SCR-VIII-03 không yêu cầu click-sort) nhưng lệch chuẩn các màn sibling có click-sort → BA quyết phạm vi. Log §QLTKND_25 trong ../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch8.md.
