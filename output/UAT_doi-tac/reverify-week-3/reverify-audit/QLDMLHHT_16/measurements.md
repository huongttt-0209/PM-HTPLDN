# Audit — QLDMLHHT_16 (row 131) — Xóa DM Loại hình HT đang tham chiếu → nghi toast lặp

**Verdict:** `Reject` (không tái hiện double toast)
**Ngày verify:** 2026-07-21 · **Account:** `admin` (QTHT) · **Tool:** Chrome DevTools MCP + `tools/toast-capture.js`
**URL test:** https://18.143.165.120.nip.io/quan-tri/danh-muc/LOAI_HINH_HO_TRO

## Cổng 1 — Evidence đối tác (video .webm, đã trích frame tới khoảnh khắc lỗi)
- File: `partner-evidence/QLDMLHHT_16.webm` → frame `reverify-audit/QLDMLHHT_16/frames/t004.04s.jpg` (video mốc 00:04).
- Env đối tác: `htpldn-uat.ospgroup.vn/quan-tri/danh-muc/LOAI_HINH_HO_TRO?page=1`, tab "Loại hình hỗ trợ".
- Thao tác: bấm **Xóa** 1 record đang được tham chiếu.
- **2 khung toast KHÁC NỘI DUNG hiện cùng lúc (giống hệt case QLDMLVPL_19):**
  1. "Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác"
  2. "Danh mục đang được sử dụng, không thể xóa"
- → Đối tác báo lỗi cụ thể: **1 thao tác xóa sinh 2 thông báo (lặp)**. Cùng 1 bug gốc với B5 (LVPL_19, LDN_16).

## Đo trên env được giao (toast-capture.js, observer self-check = 1)
| Lần | Record xóa | Có tham chiếu? | SO_REQUEST | SO_KHUNG_THONG_BAO | Nội dung toast |
|---|---|---|:-:|:-:|---|
| 1 | TU_VAN (Tư vấn pháp luật) | Có → xóa bị chặn | 1 (`DELETE …/4f09df19…`) | **1** | "Không thể xóa. Danh mục đang được sử dụng bởi bản ghi khác" |
| 2 | TO_TUNG (Tham gia tố tụng) | Không → xóa thành công | 1 (`DELETE …/cf05b16b…`) | **1** | "Xóa danh mục thành công" |

**Kết quả:**
- Lần 1 (đúng scenario đối tác — record tham chiếu bị từ chối): `1 request → 1 toast`. Toast thứ 2 ("Danh mục đang được sử dụng, không thể xóa") KHÔNG xuất hiện → double toast KHÔNG tái hiện → `Reject`.
- Lần 2 chỉ để đo thêm: TO_TUNG không tham chiếu nên xóa thành công thật (cũng chỉ 1 toast, không lặp). **Đã khôi phục ngay** record TO_TUNG (Thêm mới lại: Mã=TO_TUNG, Tên=Tham gia tố tụng, Thứ tự=2) → danh sách trở về 6 mục đúng thứ tự. Env không còn thay đổi.

## Evidence ảnh
- `reverify-audit/QLDMLHHT_16/frames/t004.04s.jpg` — frame đối tác (2 toast).
- `reverify-audit/QLDMLHHT_16/toast-tuvan.png` — env sau khi xóa TU_VAN bị từ chối. Toast tự tắt <3s; số khung toast lấy từ observer (bắt tại thời điểm mutation).
