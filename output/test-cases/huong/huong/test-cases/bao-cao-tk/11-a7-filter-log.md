# A7 — Manual UI/Function-Testable Filter Log (Báo cáo Thống kê FR-11)

> **BMAD step**: A7 (Manual review + Edit IN-PLACE)
> **Ngày**: 2026-05-10
> **Mục đích**: Loại / sửa TC chỉ test được DB / API thuần — Edit IN-PLACE file UC. File này CHỈ là audit log (LOẠI / SỬA / GIỮ).

---

## Phương pháp A7

Quét 5 file UC (`01..05-TC-*.md`) tìm TC vi phạm:
1. Verify DB row trực tiếp (vd "verify INSERT bảng X").
2. Curl/Postman API thuần không qua UI.
3. Cron job / background worker không có UI bridge.
4. Check index, trigger DB, schema migration.

→ Loại hoặc rewrite thành verify qua UI bridge: badge, audit log entry, danh sách reload, network request via `mcp__chrome-devtools__list_network_requests`.

---

## Action log per TC

| ID | TC | Action | Reason |
|----|-----|--------|--------|
| 1 | TC-BC-REP-010 | **GIỮ** | Verify audit log qua UI Nhật ký HT (`/quan-tri/audit-log`) — UI bridge OK. |
| 2 | TC-BC-REP-011 | **GIỮ** | Như TC-BC-REP-010. |
| 3 | TC-BC-REP-023 (E5 timeout) | **GIỮ + ANNOTATE** | Manual injection — đã ghi rõ trong TC. UI bridge: Toast error visible. |
| 4 | TC-BC-REP-024 (E6 export error) | **GIỮ + ANNOTATE** | Như REP-023. Toast UI verify được. |
| 5 | TC-BC-REP-027 (E9 template hỏng) | **GIỮ + ANNOTATE** | Manual injection BE. UI bridge: Toast. SPEC-CLARIFY-BC-02 đã rõ. |
| 6 | TC-BC-REP-028 (ERR-RPT-IX01-01 lĩnh vực invalid) | **GIỮ + REWRITE** | Đã rewrite thành "DevTools modify request" — manual API via UI DevTools, OK. |
| 7 | TC-BC-REP-052 (Đóng tab + verify resource leak) | **SỬA** | Original có "verify qua DB nếu UI bridge có" — sửa thành: `verify qua UI Nhật ký HT entry XEM_BC start có nhưng entry hoàn thành không có`. |
| 8 | TC-BC-EXP-021 (BE inject lỗi tạo file) | **GIỮ + ANNOTATE** | Manual injection BE. UI bridge: Toast ERR-RPT-04 visible. |
| 9 | TC-BC-PERM-012 (Cross-attempt API) | **GIỮ** | DevTools modify request → verify response qua UI (Toast hoặc data scope override). UI bridge OK. |
| 10 | TC-BC-PERM-040 (QTHT bypass) | **GIỮ + SPEC-CLARIFY** | Verify behavior qua UI [Xem] data scope. SPEC-CLARIFY-BC-03 pending BA. |
| 11 | TC-BC-EXP-004 (50K boundary) | **GIỮ + SPEC-CLARIFY** | Manual seed 50K rows nguồn. SPEC-CLARIFY-BC-07 môi trường test pending. UI verify file download → mở Excel count rows. |
| 12 | TC-BC-EXP-005 (50K+1 cap warning) | **GIỮ** | Như EXP-004. UI bridge: Toast WRN-RPT-01 + count rows trong file. |
| 13 | TC-BC-EXP-011 (PDF font verify) | **GIỮ + ANNOTATE** | Verify qua "PDF reader → File Info / Embedded fonts". Đây là property của file, không phải DB. Acceptable cho A7 vì user mở file qua UI download. |
| 14 | TC-BC-EXP-026 (locale number format) | **GIỮ** | Verify qua UI mở Excel → cell format. OK. |
| 15 | TC-BC-EXP-027 (timezone UTC+7) | **GIỮ** | Verify qua UI mở file header. OK. |
| 16 | (Gap A5 G4 BAO_CAO entity trang_thai) | **LOẠI (no TC)** | Không có UI bridge cho BAO_CAO trang_thai DANG_TAO/HOAN_THANH/LOI — không có màn hình "Lịch sử BC" trong SCR-IX-01. Verify gián tiếp qua: (a) BC chạy thành công → trang_thai=HOAN_THANH (implicit), (b) TC-BC-REP-027 ERR-RPT-07 → trang_thai=LOI. KHÔNG cần TC riêng verify entity field. |

---

## Kết quả A7

- **Total TC trước A7**: 128
- **LOẠI**: 0 (không có TC nào require pure DB/API access)
- **SỬA in-place**: 1 (TC-BC-REP-052 — đã edit verify qua audit log thay vì DB)
- **GIỮ**: 128
- **GIỮ + ANNOTATE manual**: 7 (REP-023, 024, 027, 028, EXP-004, 005, 021 — đã ghi rõ "manual injection / manual seed / manual API via DevTools")

**Final TC count: 128 TC** (không thay đổi sau A7).

---

## Iron Rule check

✅ KHÔNG có TC pure DB/API access còn sót.
✅ File 11 này CHỈ là audit log. TC sống đầy đủ trong file UC.
✅ Mọi TC manual injection/seed đều có UI bridge verify (Toast / Audit log entry / Mở file download).

---

## Verify TC nằm đầy đủ trong file UC (Iron Rule §3.1)

```
File 01: 39 TC trong sections A-E (KHÔNG có TC nào ở file phụ 08/10/11)
File 02: 40 TC trong sections A-G (KHÔNG có TC nào ở file phụ)
File 03: 18 TC trong sections A-E (KHÔNG có TC nào ở file phụ)
File 04: 19 TC trong sections A-D (KHÔNG có TC nào ở file phụ)
File 05: 12 TC trong sections A-C (KHÔNG có TC nào ở file phụ)
```

✅ Iron Rule §3.1 PASS — Phase B B-block sẽ chạy đầy đủ 128 TC.

---

*Generated 2026-05-10 — Phase A step A7 (Manual UI/function-testable filter)*
