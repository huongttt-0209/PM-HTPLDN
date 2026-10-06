# Bảng đối chiếu điều kiện — QLCHTHXLHS_02 (số thẻ tab màn Cấu hình hệ thống)

- **Ngày verify:** 2026-07-21 · **Tool:** Chrome DevTools MCP · **Account:** `admin` / QTHT
- **URL:** https://18.143.165.120.nip.io/quan-tri/cau-hinh
- **Loại claim:** Hiển thị (số tab) — đối tác kỳ vọng 4 tab, hệ thống hiện 3 tab, SRS v3.5 = 2 tab.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT (video/ảnh header "QTHT", "Quản trị viên") | `admin` — vai trò QTHT (Tab 1 SLA chỉ QTHT truy cập, SRS dòng 1731). Đúng vai trò duy nhất có quyền Tab SLA. | Không |
| Entity + trạng thái | Màn Cấu hình hệ thống, Tab "Thời hạn xử lý (SLA)" active | Cùng màn, cùng tab active | Không |
| Dữ liệu tiền đề | 6 dòng SLA seed sẵn (HOI_DAP … VU_VIEC) | Cùng 6 dòng SLA seed sẵn | Không |
| Input / filter | Không có filter ảnh hưởng số tab | Không có filter | Không |

**Kết luận:** 0 GAP. Số tab **không phụ thuộc** role/state/data — mọi QTHT vào `/quan-tri/cau-hinh` đều thấy đúng 3 tab (Thời hạn xử lý (SLA) / Mẫu phản hồi / Quản lý ngày lễ). Env đối tác (`htpldn-uat.ospgroup.vn`) và env verify (`18.143.165.120.nip.io`) hiển thị giống hệt.

**Verdict:** `BA confirm` — bất đồng ĐẶC TẢ 3 chiều (SRS 2 tab · thực tế 3 tab · kỳ vọng đối tác 4 tab). Xem `../ba-confirm/qtht/ba-confirmation-needed-qtht-batch7.md`.
