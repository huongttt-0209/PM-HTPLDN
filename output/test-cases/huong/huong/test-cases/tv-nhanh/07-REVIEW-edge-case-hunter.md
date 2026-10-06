# A4 — Edge Case Hunter Audit Log (FR-13 TV Nhanh)

> **Phase:** A4 — bmad-review-edge-case-hunter
> **Ngày tạo:** 2026-05-10
> **Mục đích:** Audit log proposal + reasoning + merge mapping cho edge case TC. **TC mới đã merge inline vào file UC (Section "Edge bổ sung").** File này chỉ là history.

---

## 1. Tổng kết merge (cập nhật sau A6 + A7 + Codex)

| File UC | TC base (A3) | Edge A4 | Fill A6 | A7 LOẠI | Codex P1 | Total final |
|---------|--------------|---------|---------|---------|----------|-------------|
| 01-TC-FR-X2-01-quan-ly-kho-cau-hoi | 25 | +6 | +2 | 0 | 0 | 33 |
| 02-TC-FR-X2-02-quan-ly-phien-tu-van | 15 | +4 | 0 | 0 | 0 | 19 |
| 03-TC-FR-X2-03-04-DN-chuyen-trang-side-effect | 7 | +1 | +1 | 0 (P1 restore) | 0 | 9 |
| 04-TC-FR-X2-05-API-inbound-danh-gia | 11 | +3 | +1 | 0 | +2 | 17 |
| 05-TC-FR-X2-06-cong-khai-kho | 12 | +4 | 0 | 0 | 0 | 16 |
| 06-TC-permission-matrix | 6 | 0 | 0 | 0 | 0 | 6 |
| **Total** | **76** | **+18** | **+4** | **0** | **+2** | **100 active** |

---

## 2. Edge case proposal + reasoning + merge target

### File 01 — Kho Q&A

| # | Edge case | Reasoning | TC ID merged | Merge target |
|---|-----------|-----------|--------------|--------------|
| E1 | Boundary cau_hoi 5000 ký tự (max long text) | Long text textarea cần boundary, FR-II có cap 5000 cho noi_dung — sibling pattern | TC-KHO-200 | Section Edge file 01 |
| E2 | Upload anh_dai_dien 5MB exact + 5.1MB | BR-DATA-04 không nói rõ inclusive max — boundary phổ biến lỗi off-by-one | TC-KHO-201 | Section Edge file 01 |
| E3 | Upload file_dinh_kem_cong_khai 20MB exact + 20.1MB | Tương tự E2 | TC-KHO-202 | Section Edge file 01 |
| E4 | Upload file_dinh_kem_cong_khai sai extension (.exe, .zip) | Whitelist PDF/DOC/DOCX/XLS/XLSX — verify reject các extension khác | TC-KHO-203 | Section Edge file 01 |
| E5 | Concurrent edit Q&A — 2 tab cùng lúc | Optimistic lock pattern phổ biến (sibling FR-02 có) | TC-KHO-204 | Section Edge file 01 |
| E6 | tu_khoa boundary — 100 từ khóa phân cách dấu phẩy | Tag input có cap implicit, edge boundary | TC-KHO-205 | Section Edge file 01 |

### File 02 — Phiên TVN

| # | Edge case | Reasoning | TC ID merged | Merge target |
|---|-----------|-----------|--------------|--------------|
| E1 | TOP 5 chỉ trả 3 (kho có 3 Q&A liên quan) | Số lượng < 5 phải hiển thị tất cả, không lỗi | TC-PHIEN-200 | Section Edge file 02 |
| E2 | Concurrent CB NV trả lời cùng phiên | 2 CB NV cùng đơn vị mở chi tiết → cả 2 nhập + Gửi → optimistic lock | TC-PHIEN-201 | Section Edge file 02 |
| E3 | DA_GOI_Y → CB_TRA_LOI khi CB sửa drastic gợi ý | Verify nguon_tra_loi = THU_CONG nếu sửa nhiều, KHO nếu giữ nguyên (cần BA chốt threshold) | TC-PHIEN-202 | Section Edge file 02, kèm SPEC-CLARIFY-TVN-06 |
| E4 | thoi_gian_xu_ly_phut khi cross-day (DN gửi 23:50 + CB trả 00:10) | Tính chính xác phút qua midnight | TC-PHIEN-203 | Section Edge file 02 |

### File 03 — DN chuyên trang side-effect

| # | Edge case | Reasoning | TC ID merged | Merge target |
|---|-----------|-----------|--------------|--------------|
| E1 | DN gửi cùng câu hỏi 2 lần liên tiếp (duplicate prevention) | UX edge — có chống duplicate không? | TC-DN-200 | Section Edge file 03, kèm SPEC-CLARIFY-TVN-07 |

### File 04 — API inbound đánh giá

| # | Edge case | Reasoning | TC ID merged | Merge target |
|---|-----------|-----------|--------------|--------------|
| E1 | Idempotency cache TTL boundary 24h00m + 24h01m | TTL boundary kiểm tra exact 24h | TC-DGTV-200 | Section Edge file 04 |
| E2 | API inbound DG cho phiên đã HET_HAN | Có cho phép DG cho phiên hết hạn không? Cần BA chốt | TC-DGTV-201 | Section Edge file 04, kèm SPEC-CLARIFY-TVN-08 |
| E3 | Idempotency-Key body khác nhưng same key → 409 hay 422 | Edge case phổ biến API idempotency | TC-DGTV-202 | Section Edge file 04 |

### File 05 — Công khai/Hủy

| # | Edge case | Reasoning | TC ID merged | Merge target |
|---|-----------|-----------|--------------|--------------|
| E1 | Concurrent CK 2 CB NV cùng QA — race condition | Cần verify lock TTL pattern (giống FR-02 BUG-EC-04) | TC-CK-200 | Section Edge file 05 |
| E2 | API outbound timeout 30s → ERR-TVN-CK-01 + retry button | Verify timeout handling | TC-CK-201 | Section Edge file 05 |
| E3 | thoi_gian_dang_tai khi server timezone khác client | Format dd/mm/yyyy hh:mm — verify timezone | TC-CK-202 | Section Edge file 05 |
| E4 | CK Q&A nguon=TU_DONG (không có anh_dai_dien custom) | TU_DONG kế thừa từ HOI_DAP, có anh_dai_dien mặc định không? | TC-CK-203 | Section Edge file 05, kèm SPEC-CLARIFY-TVN-09 |

### File 06 — Permission

| # | Edge case | Reasoning | TC ID merged |
|---|-----------|-----------|--------------|
| — | Không có edge thêm — Permission đã cover BR-AUTH 1/5/8 + 6 role | — | — |

---

## 3. Merge action — lưu ý implementer

> **Iron Rule:** TC mới (TC-XXX-2NN) merge vào Section "Edge bổ sung" cuối mỗi file UC. KHÔNG để TC sống trong file 07 này.

Sau A4, file 01-06 cần thêm Section "Edge bổ sung A4" với 18 TC mới. Steps tự động trong Phase A6 sẽ điền chi tiết steps + expected; A4 chỉ propose ID + name + reasoning.

---

## 4. SPEC-CLARIFY phát sinh từ A4

| ID | Câu hỏi BA | File ảnh hưởng |
|----|-----------|----------------|
| SPEC-CLARIFY-TVN-06 | Threshold "sửa drastic" để xác định nguon_tra_loi = KHO vs THU_CONG (% delta string)? | file 02 TC-PHIEN-202 |
| SPEC-CLARIFY-TVN-07 | DN gửi câu hỏi duplicate trong N giây có chặn không? Hay cho phép tạo 2 phiên? | file 03 TC-DN-200 |
| SPEC-CLARIFY-TVN-08 | API inbound DG cho phiên HET_HAN có chấp nhận hay reject? | file 04 TC-DGTV-201 |
| SPEC-CLARIFY-TVN-09 | TU_DONG nguồn auto từ HOI_DAP có anh_dai_dien default không? Hay không có ảnh? | file 05 TC-CK-203 |

---

*Generated 2026-05-10 — Phase A step A4 (bmad-review-edge-case-hunter)*
