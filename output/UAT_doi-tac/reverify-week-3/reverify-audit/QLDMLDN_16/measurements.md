# Audit — QLDMLDN_16 (row 145) — Xóa DM Loại doanh nghiệp đang tham chiếu → nghi toast lặp

**Verdict:** `Reject` (không tái hiện double toast)
**Ngày verify:** 2026-07-21 · **Account:** `admin` (QTHT) · **Tool:** Chrome DevTools MCP + `tools/toast-capture.js`
**URL test:** https://18.143.165.120.nip.io/quan-tri/danh-muc/LOAI_DOANH_NGHIEP

## Cổng 1 — Evidence đối tác (ảnh full-res)
- File: `partner-evidence/QLDMLDN_16.jpg` (chụp 2026-07-14).
- Env đối tác: `htpldn-uat.ospgroup.vn/quan-tri/danh-muc/LOAI_DOANH_NGHIEP?page=1`, tab "Loại doanh nghiệp".
- Thao tác: bấm **Xóa** 1 record đang được tham chiếu.
- **2 khung toast KHÁC NỘI DUNG hiện cùng lúc (giống hệt QLDMLVPL_19, QLDMLHHT_16):**
  1. "Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác"
  2. "Danh mục đang được sử dụng, không thể xóa"
- → Đối tác báo lỗi cụ thể: **1 thao tác xóa sinh 2 thông báo (lặp)**. Cùng 1 bug gốc với cụm B5.

## Đo trên env được giao (toast-capture.js, observer self-check = 1)
| Lần | Record xóa | Có tham chiếu? | SO_REQUEST | SO_KHUNG_THONG_BAO | Nội dung toast |
|---|---|---|:-:|:-:|---|
| 1 | TNHH (Công ty trách nhiệm hữu hạn) | Có → xóa bị chặn | 1 (`DELETE …/07a9d620…`) | **1** | "Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác" |

**Kết quả:** `1 request → 1 toast`. Toast thứ 2 ("Danh mục đang được sử dụng, không thể xóa") KHÔNG xuất hiện → double toast KHÔNG tái hiện → `Reject`. Record TNHH vẫn còn trong danh sách (xóa bị chặn, không thay đổi data).

## Cụm chung
3/3 case duplicate-toast (QLDMLVPL_19, QLDMLHHT_16, QLDMLDN_16) đều: `1 request DELETE → 1 khung toast` khi xóa record tham chiếu. Toast dư thừa thứ 2 mà đối tác thấy đã biến mất → nghi dev đã bỏ handler toast trùng. Component form/list danh mục dùng chung → 1 bug gốc, nay đã hết.

## Evidence ảnh
- `reverify-audit/QLDMLDN_16/toast-tnhh.png` — env sau khi xóa TNHH bị từ chối. Toast tự tắt <3s; số khung lấy từ observer.
