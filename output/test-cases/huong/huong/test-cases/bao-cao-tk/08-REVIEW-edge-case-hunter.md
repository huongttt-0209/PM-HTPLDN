# A4 — Edge Case Hunter Review (Báo cáo Thống kê FR-11)

> **BMAD step**: A4 (`bmad-review-edge-case-hunter`)
> **Ngày**: 2026-05-10
> **Mục đích**: Audit log đề xuất edge case mới + mapping đã merge inline vào file UC. Các TC dưới đây ĐÃ được merge vào file `01-..05-TC-*.md` per Iron Rule §3.1 todo.md.

---

## Phương pháp

Quét 5 file UC (01-05) tìm gap edge case theo các trục:

1. **Boundary**: số lượng record (0, 1, 2, max-1, max, max+1), độ dài text, ngày boundary.
2. **Concurrent**: 2 tab cùng xuất, refresh giữa query, hủy giữa query.
3. **Data integrity**: rounding, locale, timezone (UTC+7 VN), null/undefined.
4. **Network**: timeout, 5xx mid-flight, slow 3G.
5. **State**: persistent filter qua reload, deep-link URL, browser back/forward.
6. **Special chars**: tên đơn vị Unicode, emoji, dấu câu trong filter search.

---

## Đề xuất Edge Case (đã merge inline)

| # | Edge case proposal | Severity | Merge target | TC ID merged | Reasoning |
|---|--------------------|----------|--------------|--------------|-----------|
| E1 | BC kỳ THANG đúng cuối tháng có ngày 31 (vd 31/01, 31/03) — auto fill den_ngay | 🟡 | 01-TC | TC-BC-REP-049 | Auto fill kỳ THANG cần verify boundary ngày cuối tháng (28/29/30/31) |
| E2 | BC kỳ THANG tháng 2 năm nhuận (29/02/2024) | 🟢 | 01-TC | TC-BC-REP-050 | Leap year edge — Date picker phải accept 29/02 không bị skip |
| E3 | Refresh trang giữa khi đang [Xem] BC slow query | 🟡 | 01-TC | TC-BC-REP-051 | Verify state recovery sau F5 — filter giữ qua URL hoặc reset |
| E4 | Cancel/Đóng tab giữa query | 🟢 | 01-TC | TC-BC-REP-052 | Verify request cancel BE-side, không leak resource |
| E5 | Concurrent xuất 2 tab cùng BC | 🟡 | 04-TC | TC-BC-EXP-024 | Verify 2 file unique tên (timestamp khác), không lock |
| E6 | Tên BC chứa ký tự đặc biệt → filename slug | 🟢 | 04-TC | TC-BC-EXP-025 | "BC Số lượng hỏi đáp/vướng mắc" có dấu / → filename phải sanitize |
| E7 | Tổng cộng row vs sum chi tiết — rounding mismatch | 🟡 | 01-TC | TC-BC-REP-053 | tỷ lệ % rounding 2 chữ số → tổng có thể ≠ 100% (do rounding) — verify hành vi |
| E8 | Don_vi_ten dài 200+ ký tự trong dropdown | 🟢 | 02-TC | TC-BC-SM-XC-09 | Truncate hoặc tooltip — verify không vỡ layout |
| E9 | Search dropdown loại BC với ký tự dấu (vd "đào tạo") | 🟢 | 02-TC | TC-BC-SM-XC-10 | Search Vietnamese accent-aware (matches "dao tao") |
| E10 | Deep-link URL với pre-filled filter (vd `/bao-cao?loai=HOI_DAP&ky=THANG`) | 🟡 | 01-TC | TC-BC-REP-054 | Verify URL deep-link auto chọn dropdown + filter |
| E11 | BR-DATA-07 pagination — data table BC nhiều rows có pagination 20/page hay show all? | 🟢 | 01-TC | TC-BC-REP-055 | TPL không nói rõ — verify thực tế + log SPEC-CLARIFY-BC-10 |
| E12 | Multi-locale number format (1,000.50 vs 1.000,50) | 🟢 | 04-TC | TC-BC-EXP-026 | XLSX + PDF: locale VN phải là "1.000,50" hoặc "1,000.50" — verify consistent |
| E13 | Snapshot BC (UC126/129/131) — refresh giữa lần [Xem] có thay đổi data không? | 🟡 | 02-TC | TC-BC-SM-03c | UC126 snapshot — verify 2 lần [Xem] cách nhau 1 phút có thể trả khác (data thay đổi giữa) |
| E14 | Timezone UTC+7 Vietnam — datetime trong export | 🟡 | 04-TC | TC-BC-EXP-027 | Header file có ngay_tao_bc đúng UTC+7, không UTC |
| E15 | Pre-filter "Đợt đánh giá" KE_HOACH_DG_ID đã bị xóa | 🟢 | 02-TC | TC-BC-SM-09b | FR-IX-09 filter dot — nếu đợt đã soft-delete, dropdown có hiện hay ẩn? |

**Tổng đề xuất**: 15 edge → ALL merged inline.

---

## Reasoning per proposal

### E1-E2: Date boundary
SRS srs-fr-11:67-69 nói tu_ngay/den_ngay datetime, "Chọn / Auto" — không nói rõ behavior auto fill. Edge case: kỳ THANG khi tháng có 31 ngày, năm nhuận 29/02. **Risk**: Frontend Date library có thể ép về 30 ngày → mất data ngày 31.

### E3-E4: Network resilience
Long query 30s timeout (E5 ERR-RPT-03). User F5 hoặc đóng tab — verify BE clean up. **Risk**: BE leak query resource.

### E5-E6: Concurrent + filename
Edge classic: 2 tab cùng user xuất file → name conflict? Filename slug: BC tên có `/` (vd "hỏi đáp/vướng mắc") → bị stripe.

### E7: Rounding
ty_le_tra_loi % — output#4 FR-IX-01. Nếu 1/3 = 33.33%, 1/3 = 33.33%, 1/3 = 33.33% → tổng 99.99% không = 100%. **Risk**: User hiểu nhầm.

### E8-E9: Dropdown UX
DON_VI có thể có tên dài. SCR-IX-01 row#3 nói "searchable" → verify search Vietnamese (NFD/NFC, accent-insensitive).

### E10: Deep-link
Pattern phổ biến — share link BC với pre-filter qua email. **Risk**: Filter không persist qua URL → mất khả năng share.

### E11: Pagination
TPL không nói rõ. BR-DATA-07 (master srs-v3.md) nói pagination default 20/page max 100 — áp dụng cho mọi danh sách. BC bảng dữ liệu có phải "danh sách" không? Mark SPEC-CLARIFY-BC-10.

### E12: Locale
Format số tiền VND vs xuất Excel — phải nhất quán format VN ("1.000.000 ₫" hoặc "1,000,000 VND").

### E13: Snapshot consistency
UC126/129/131 là snapshot tại thời điểm query. 2 lần [Xem] cách 1 phút có thể trả khác data. **Risk**: User không biết đó là snapshot, nghĩ BC sai.

### E14: Timezone
VN UTC+7. Server có thể lưu UTC. Export file phải convert UTC+7. **Risk**: Ngày tạo BC bị lệch 7h.

### E15: Soft-deleted filter option
KE_HOACH_DG có thể bị soft-delete. Dropdown FR-IX-09 hiện đợt đó? Behavior depends on BR-DATA-01.

---

## Iron Rule check (todo.md §3.1)

✅ Mọi 15 TC mới đã merged inline vào file UC tương ứng (`01-TC-tpl-report-full-representative.md`, `02-TC-smoke-23-loai-bc.md`, `04-TC-export-xlsx-pdf-tt17.md`).
✅ File 08 này CHỈ là audit log (proposal + reasoning + merge mapping). KHÔNG chứa TC source.

*Generated 2026-05-10 — Phase A step A4 (BMAD edge-case-hunter)*
