# Audit — CBKQDTBD_01 (row 35) → BA confirm (chức năng công bố có sẵn; cert PDF khác SRS Hướng B → BA quyết)

> **Reclassify 2026-07-11:** Trước để `Reject`; đổi `BA confirm` theo rule verdict cập nhật — đối tác quan sát đúng (không có nút sinh chứng nhận) nhưng kỳ vọng (sinh chứng nhận PDF ký số) KHÁC SRS v3.5 Hướng B → bất đồng đặc tả, BA quyết. Entry đầy đủ: `ba-confirmation-needed-week-2.md`.

## Đối tác báo
- Chức năng "Công bố kết quả đào tạo bồi dưỡng". Bước: khóa "Hoàn thành" → chọn HV → bấm "Công bố và sinh chứng nhận".
- Expected: "Đã phát hành chứng nhận cho {N} học viên" + sinh chứng nhận điện tử PDF ký số.
- Actual: "Màn hình không có chức năng".
- Evidence CBKQDTBD_01.webm: role CB_NV_TW, khóa KH-HDSD-AG-003 "Pháp luật DN cơ bản An Giang Q1/2026 (hoàn thành)", đứng ở **tab "Thông tin"** — không thấy nút công bố.

## 3 dữ kiện neo
- (a) Khóa aaffaa02-...022 (An Giang), HOAN_THANH, 5 HV. Đối tác đứng tab "Thông tin".
- (b) State: HOAN_THANH; tab Thông tin không có action button công bố.
- (c) Kỳ vọng: nút "Công bố và sinh chứng nhận" + PDF ký số.

## SRS v3.5
- FR-III-19 (UC38) "Công bố kết quả đào tạo" — Màn SCR-III-02 **Tab "Công bố kết quả"** (không phải tab Thông tin).
- Processing: kiểm HOAN_THANH → lọc HV có KQ DA_DUYET → set cong_bo=true → đánh dấu cho Cổng PLQG kéo → thông báo HV → nhật ký.
- **Dòng 1278-1280 (Hướng B — Thay đổi 9):** "KHÔNG cấp chứng nhận PDF, KHÔNG sinh entity CHUNG_NHAN." Cơ sở pháp lý NĐ55/2019 không trao thẩm quyền cấp chứng nhận cho phần mềm.

## Verify trên env được giao (18.143.165.120)
- Account CB_NV_TW (`cbnv_tw`). Khóa AAA-KH-TW + AAA-KH-BN (HOAN_THANH), tab **"Kết quả"**:
  - Có nút **"Hủy công bố KQ"** + **"Xuất DOCX"** + alert "Kết quả đào tạo đã được phê duyệt" + bảng HV có điểm/kết quả.
  - Nút "Hủy công bố KQ" (trạng thái đã công bố) ⇒ chức năng **Công bố kết quả tồn tại** (toggle Công bố ↔ Hủy công bố). Khóa đang ở trạng thái đã công bố.
  - Dialog "Hủy công bố kết quả" xác nhận tích hợp Cổng PLQG ("gửi yêu cầu hủy công bố sang Cổng PLQG").
  - Ảnh: `web-ketqua-tab-cong-bo-ton-tai.png`.
- KHÔNG có nút/chức năng sinh chứng nhận PDF — ĐÚNG SRS Hướng B (cố ý bỏ).

## Bảng đối chiếu (Cổng 3)
| Yêu cầu partner | SRS v3.5 | Web | Verdict |
|---|---|---|---|
| Công bố kết quả | Có (FR-III-19, tab Kết quả) | Có (nút Công bố/Hủy công bố KQ) | Không thiếu |
| Sinh chứng nhận PDF ký số | KHÔNG (Hướng B bỏ, dòng 1278-1280) | Không có | Đúng spec — không phải lỗi |

→ Đối tác đứng nhầm tab (Thông tin thay vì Kết quả) + kỳ vọng cấp chứng nhận theo spec cũ (v3) đã bị bỏ ở v3.5.

## Quan sát phụ (ngoài scope — cần theo dõi, CHƯA log)
- Bấm "Hủy công bố KQ" trên AAA-KH-BN → nhập lý do → xác nhận → toast **"Khóa học không tồn tại"** (hủy công bố không thành công). Chỉ thử 1 lần trên 1 khóa seed; khác chức năng CBKQDTBD_01; chưa verify đủ (có thể transient / seed-specific). Đề xuất theo dõi riêng nếu cần.

## Verdict: BA confirm
Chức năng công bố kết quả tồn tại (tab Kết quả); sinh chứng nhận PDF ký số bị bỏ có chủ đích theo SRS v3.5 Hướng B (dòng 1278–1280, NĐ55/2019). Kỳ vọng đối tác (sinh chứng nhận) khác SRS → BA quyết có bổ sung ngoài Hướng B không. Sheet row 35: BA confirm (note giữ FR-III-19/UC38 + dòng — người đọc là BA).
