# QLDNDHTPL_OOS_01 — bản đo toast (R6, 2026-07-25)

**Bối cảnh:** cbnv_tw_02 (BTP · TW) mở deep-link `/doanh-nghiep/829abcac-b0af-4cde-9af9-ec51bc79014c/sua`
(DN-HNI-0001 — đơn vị khác), sửa **Ghi chú** → [Lưu] → [Lưu thay đổi].

**Lỗi gốc tuần 3:** hiện **2 khung thông báo** với 2 nội dung mâu thuẫn nhau sau 1 lần bấm lưu.

## 3 lần đo độc lập

| Lần | Phương pháp | Số request | Request | Số khung thông báo | Nội dung |
|---|---|---|---|---|---|
| 1 | MutationObserver (không lọc trùng, `innerText`) | 1 | `PATCH /api/v1/doanh-nghieps/829abcac-…` | **1** | `Không có quyền thao tác trên đơn vị khác` |
| 2 | MutationObserver (cài lại, self-check `soObserverDangSong=1`) | 1 | `PATCH /api/v1/doanh-nghieps/829abcac-…` | **1** | `Không có quyền thao tác trên đơn vị khác` |
| 3 | Đọc DOM sống `.ant-message-notice-wrapper` tại mốc +700 ms sau khi bấm | — | — | **1** | `Không có quyền thao tác trên đơn vị khác` |

`khoangCachMs = null` ở cả 2 lần đo observer (chỉ 1 khung nên không có khoảng cách giữa 2 khung).

## Vì sao không có ảnh chụp toast

Toast AntD tự tắt sau ~3 s. Độ trễ round-trip của `take_screenshot` qua MCP đo được ~2,5 s trở lên,
nên ảnh luôn rơi vào **trước** lúc toast hiện (chưa có phản hồi PATCH) hoặc **sau** lúc toast đã tắt —
4 lần thử đều không bắt được. Bản đo DOM ở trên là bằng chứng thay thế: nó đọc trực tiếp
node toast thật do ứng dụng render, và khớp nhau ở 3 lần đo bằng 2 phương pháp khác nhau.

## Ảnh kèm (phần quyền nút Sửa/Xóa)

- `image/R6-QLDNDHTPL_OOS_01-01-CBPD-danhsach-chi-co-Xem.png` — cbpd_tw_01: cả 9 dòng DN chỉ có nút Xem.
- `image/R6-QLDNDHTPL_OOS_01-02-CBPD-chitiet-khong-co-Chinh-sua.png` — cbpd_tw_01 mở chi tiết DN-HNI-0006: không có nút Chỉnh sửa.
- `image/R6-QLDNDHTPL_OOS_01-03-CBNV-an-Sua-Xoa-DN-don-vi-khac.png` — cbnv_tw_02: chỉ DN-07-0001 và DN-SEED-0001 (đơn vị mình) có Sửa/Xóa; 7 DN đơn vị khác chỉ có Xem.
