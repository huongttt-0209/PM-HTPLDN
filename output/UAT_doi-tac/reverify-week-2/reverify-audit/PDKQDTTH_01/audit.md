# Audit — PDKQDTTH_01 (row 33) + PDKQDTTH_05 (row 34) → Open (thông báo CB NV thiếu)

## Đối tác báo
- PDKQDTTH_01: CB PD phê duyệt kết quả → khóa "Hoàn thành" OK, nhưng **CB NV không nhận thông báo**. Evidence PDKQDTBD_01.webm (env ospgroup, khóa KH-20260509-005 "SHTT cho startup - R9").
- PDKQDTTH_05: CB PD từ chối kết quả (lý do "TKM test từ chối") → khóa "Đã kết thúc", **CB NV không nhận thông báo**. Evidence PDKQDTBD_05.webm (khóa "An toàn lao động ngành xây dựng - R9").

## SRS
- FR-III-18 (UC37) §Processing (dòng 1261): "...→ Duyệt: HOAN_THANH / Từ chối: DA_KET_THUC → **Thông báo CB NV** → Ghi nhật ký."
- §Postconditions (dòng 1265): "Khóa học HOAN_THANH (duyệt) hoặc DA_KET_THUC (từ chối). **CB NV nhận thông báo**." → yêu cầu chung cho cả 2 nhánh.

## Real-data test trên env được giao (18.143.165.120)
### PDKQDTTH_01 (phê duyệt) — reproduce ĐẦY ĐỦ
1. Baseline: CB_NV_TW (`cbnv_tw`, id f2e93500) — `GET /thong-baos`, thông báo mới nhất 2026-07-10, KHÔNG có loại "phê duyệt kết quả".
2. CB_NV_TW: khóa AAA-KH-TW (Đã kết thúc, KQ seed sẵn) → "Gửi duyệt KQ" → "Đã trình duyệt kết quả thành công" → CHO_DUYET_KQ.
3. CB_PD_TW (`cbpd_tw`, cùng đơn vị TW): "Duyệt KQ" → `POST /khoa-hocs/{id}/approve-result` → **200**, khóa → HOAN_THANH.
4. CB_NV_TW: `GET /thong-baos` (cache-bust, 20 mục, server date 2026-07-11 14:46) → **0 thông báo "phê duyệt kết quả"**. UI chuông: mọi mục "một ngày trước", không có mục mới.
- CB_NV_TW là người submit (Gửi duyệt KQ) + cùng đơn vị khóa (TW 8000-001); pipeline thông báo tới CB_NV_TW hoạt động (nhận thông báo đăng ký khóa khác) → xác nhận thiếu riêng thông báo phê duyệt kết quả.
- Ảnh: `bug-reports/image/BUG-PDKQDTTH_01-cbnv-notif-thieu-phe-duyet-kq.png`.

### PDKQDTTH_05 (từ chối) — seed BLOCKER cho reproduce trực tiếp
- Cần 1 khóa TW ở CHO_DUYET_KQ để bấm "Từ chối KQ". Khóa AAA-KH-TW (KQ seed sẵn) đã dùng cho test phê duyệt (giờ HOAN_THANH). AAA-KH-DP (Đã kết thúc) thuộc đơn vị 8002-001 — KHÔNG có account login (cbnv_dp/cbpd_dp ở 8002-006, khác đơn vị → không thao tác được).
- Thử walk KH-SEED-0001 (TW, Đã duyệt): Khai giảng → Kết thúc OK, nhưng "Gửi duyệt KQ" báo `ERR-VAL-III-15-03: Số kết quả (0) không khớp số HV (1)`. Tab Kết quả rỗng, không có row nhập (khóa thiếu buổi học/điểm danh). `POST/PUT /ket-quas` → 404 (endpoint lưu KQ khác, không dựng được payload). → không seed được KQ để trình duyệt.
- **Kết luận Open dựa trên:** cùng cơ chế "Thông báo CB NV" (SRS Postcondition dòng 1265 chung cho cả duyệt/từ chối) đã chứng minh KHÔNG hoạt động ở nhánh phê duyệt (real-data) + CB NV không có bất kỳ thông báo quyết-định-kết-quả nào + evidence đối tác cho luồng từ chối.

## Side effect (env UAT)
- KH-SEED-0001: state đổi DA_DUYET → DA_KET_THUC (walk test, không revert được — không có action un-finish). Chấp nhận trên UAT.
- AAA-KH-TW: DA_KET_THUC → HOAN_THANH (đã phê duyệt trong test PDKQDTTH_01).

## Verdict
- PDKQDTTH_01 → **Open** (BUG-PDKQDTTH_01, Medium). Sheet row 33.
- PDKQDTTH_05 → **Open** (BUG-PDKQDTTH_05, Medium, cùng root cause). Sheet row 34.
