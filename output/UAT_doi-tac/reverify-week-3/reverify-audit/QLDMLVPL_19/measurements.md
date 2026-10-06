# Audit — QLDMLVPL_19 (row 126) — Xóa DM Lĩnh vực PL đang tham chiếu → nghi toast lặp

**Verdict:** `Reject` (không tái hiện double toast)
**Ngày verify:** 2026-07-21 · **Account:** `admin` (QTHT) · **Tool:** Chrome DevTools MCP + `tools/toast-capture.js`
**URL test:** https://18.143.165.120.nip.io/quan-tri/danh-muc/LINH_VUC_PL

## Cổng 1 — Evidence đối tác (đã mở full-res)
- File: `partner-evidence/QLDMLVPL_19.jpg`
- Env đối tác: `htpldn-uat.ospgroup.vn/quan-tri/danh-muc/LINH_VUC_PL`, tab "Lĩnh vực pháp lý".
- Thao tác: bấm **Xóa** 1 record đang được tham chiếu.
- **2 khung toast KHÁC NỘI DUNG hiện cùng lúc:**
  1. "Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác"
  2. "Danh mục đang được sử dụng, không thể xóa"
- → Đối tác báo lỗi cụ thể: **1 thao tác xóa sinh 2 thông báo (lặp/nhân đôi)**.

## Đo trên env được giao (vùng nóng — toast-capture.js, KHÔNG lọc trùng, đọc innerText)
Self-check observer: `soObserverDangSong = 1` → số liệu hợp lệ.

| Lần | Record xóa | SO_REQUEST | request | SO_KHUNG_THONG_BAO | Nội dung toast |
|---|---|:-:|---|:-:|---|
| 1 | DAN_SU (Dân sự) | 1 | `DELETE /api/v1/danh-muc/…010` | **1** | "Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác" |
| 2 | THUONG_MAI (Thương mại) | 1 | `DELETE /api/v1/danh-muc/…01c` | **1** | "Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác" |
| 3 | DAT_DAI (Đất đai) | 1 | `DELETE /api/v1/danh-muc/…014` | **1** (observer) | "Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác" |

**Kết quả:** Cả 3 lần đều `1 request → 1 khung toast`. Theo rule vùng nóng: `1 request + 1 toast = Reject` (không tái hiện lỗi FE hiển thị nhân đôi). Toast thứ 2 mà đối tác thấy ("Danh mục đang được sử dụng, không thể xóa") KHÔNG còn xuất hiện → nghi đã được dev fix (bỏ handler toast dư thừa).

Cả 3 lần xóa đều bị **từ chối** (record vẫn còn trong danh sách) → đúng ràng buộc ERR-DM-03 (bản ghi đang được tham chiếu, không xóa được). Không có dữ liệu bị thay đổi.

## Ghi chú incidental (ngoài tiêu chí)
- Nội dung toast app = "Không thể xóa. Danh mục đang được sử dụng bởi **bản ghi khác**".
- SRS ERR-DM-03 (srs-v3.5 dòng 160) = "Không thể xóa. Danh mục đang được sử dụng bởi **{N} bản ghi {entity}**" (có số lượng + tên entity cụ thể).
- App bỏ phần `{N}` + `{entity}` → thông báo kém chi tiết hơn spec. Đối tác KHÔNG phản ánh điểm này; là sai lệch nhỏ về mức chi tiết message → thiên `BA confirm` nếu muốn siết. Ghi nhận để báo cáo, không thuộc case duplicate.

## Evidence ảnh
- `reverify-audit/QLDMLVPL_19/toast-thuongmai.png` — màn danh mục sau khi xóa bị từ chối (record vẫn còn). Toast tự tắt <3s nên ảnh bắt sau thời điểm; số khung toast lấy từ observer (bắt tại thời điểm mutation).
- `bug-reports/image/BUG-QLDMLVPL_19-toast.png` — ảnh lần đo 1.
