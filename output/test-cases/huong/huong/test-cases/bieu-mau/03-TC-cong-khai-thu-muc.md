# Test Cases — UC94: Công khai Thư mục Biểu mẫu (FR-VII-03)

> **SRS Ref**: FR-VII-03 (srs-fr-09:208-273), SCR-VII-01, Entity THU_MUC_BIEU_MAU + BIEU_MAU
> **Ngày tạo**: 2026-05-06 (BMAD A3)
> **Tài khoản chính**: `cb_nv_tw_01` (có quyền "Công khai biểu mẫu" — srs-fr-09:219)

---

## A. PUBLISH HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-301 | FR-VII-03 AC1 / BR-FLOW-07 | Công khai thư mục có ≥1 biểu mẫu | `cb_nv_tw_01`. Thư mục "HĐ Lao động" trạng thái NHAP, chứa 3 BM. | hanh_dong=CONG_KHAI | 1. Hover dòng thư mục → click [Công khai]. 2. Confirm dialog "Công khai thư mục? KHÔNG cần phê duyệt." 3. Click [Xác nhận]. | **STATE**: Backend UPDATE trang_thai=CONG_KHAI (srs-fr-09:235), gọi API outbound `/api/v1/bieu-mau` push thư mục + 3 BM lên Cổng PLQG (BR-FLOW-05, srs-fr-09:236). KHÔNG có bước phê duyệt CB_PD (BR-FLOW-07, srs-fr-09:919). **UI**: Toast success "Đã công khai lên Cổng PLQG". Badge trạng thái đổi sang CONG_KHAI (xanh lá, srs-fr-09:605). Tab "Đã công khai" badge +1. **PERSIST**: Reload → trạng thái CONG_KHAI. AUDIT_LOG hành động='PUBLISH' (srs-fr-09:237). Verify `list_network_requests` thấy POST/PUT outbound thành công 200. | Happy | P0 |
| TC-BM-302 | FR-VII-03 AC2 | Hủy công khai (Ẩn) thư mục | TC-BM-301 done (thư mục đang CONG_KHAI). | hanh_dong=AN | 1. Click [Ẩn] trên dòng thư mục CONG_KHAI. 2. Confirm. | **STATE**: Backend UPDATE trang_thai=AN (srs-fr-09:243), gọi API outbound gỡ thư mục khỏi Cổng (srs-fr-09:245). **UI**: Toast success "Đã gỡ khỏi Cổng PLQG". Badge AN (đen). Thư mục biến khỏi tab "Đã công khai", xuất hiện tab "Đã ẩn". **PERSIST**: Reload → AN. AUDIT_LOG hành động='UNPUBLISH' (srs-fr-09:246). Verify network DELETE/PATCH thành công. | Happy | P0 |
| TC-BM-303 | FR-VII-03 AC4 | Xem danh sách "Đã công khai" | `cb_nv_tw_01`. ≥3 thư mục CONG_KHAI tồn tại. | — | 1. Click tab "Đã công khai". | **UI**: Bảng filter chỉ thư mục trang_thai=CONG_KHAI (srs-fr-09:272). Số đếm trên tab khớp số dòng hiển thị. **PERSIST**: — | Happy | P1 |
| TC-BM-308 | FR-VII-03 / SM-BIEUMAU AN→CONG_KHAI (A4 merged) | Re-publish thư mục đã ẨN: AN → CONG_KHAI | TC-BM-302 done (TM trạng thái AN, có ≥1 BM). | hanh_dong=CONG_KHAI | 1. Click [Công khai] trên TM trạng thái AN. 2. Confirm. | **STATE**: Backend UPDATE trang_thai=CONG_KHAI (SM-BIEUMAU srs-fr-09:826 nguyên văn "AN → CONG_KHAI"), gọi API outbound đẩy lại lên Cổng PLQG. **UI**: Toast success. Badge AN → CONG_KHAI. TM xuất hiện lại tab "Đã công khai". **PERSIST**: AUDIT_LOG hành động='REPUBLISH' (hoặc 'PUBLISH' — SRS Gap, mark gap-report). Verify network outbound 200. | Happy | P0 |

---

## B. NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-304 | ERR-CK-01 / BR-BM-05 | Công khai thư mục rỗng — chặn | `cb_nv_tw_01`. Thư mục "Empty" trạng thái NHAP, 0 BM bên trong. | — | 1. Click [Công khai] trên thư mục rỗng. 2. Confirm. | **STATE**: Backend reject (count BM=0, srs-fr-09:233-234). **UI**: Toast error nguyên văn "Thư mục chưa có biểu mẫu, không thể công khai" (srs-fr-09:252 ERR-CK-01). **PERSIST**: trang_thai vẫn NHAP. KHÔNG gọi API outbound (verify `list_network_requests`). | Negative | P0 |
| TC-BM-305 | ERR-CK-02 / SPEC-CLARIFY-BM-15 (Codex fix 2026-05-09) | API Cổng PLQG fail — rollback transactional behavior | `cb_nv_tw_01`. Mock Cổng PLQG endpoint trả 500 (qua DevTools network throttle hoặc env staging có Cổng down). | — | 1. Click [Công khai]. 2. Confirm. 3. Backend gọi API → 500. | **STATE**: BE behavior **SRS Gap** (srs-fr-09:236 BR-FLOW-07 chỉ định "gọi API trực tiếp", srs-fr-09:253 chỉ quote message ERR-CK-02 — KHÔNG quote rollback rule). 2 case có thể: (a) Backend rollback transactional KHÔNG set trang_thai=CONG_KHAI trước khi API success (consistency); (b) Set trang_thai=CONG_KHAI trước, sau đó queue retry sync (eventual consistency, sync_status=PENDING). **UI**: Toast error nguyên văn "Lỗi kết nối Cổng PLQG. Vui lòng thử lại sau" (srs-fr-09:253 ERR-CK-02). **PERSIST**: Verify reload behavior thực tế — mark **SPEC-CLARIFY-BM-15** rollback policy. AUDIT_LOG ghi attempt fail. | Negative | P0 |
| TC-BM-309 | ERR-CK-02 / network timeout (A4 merged) | API Cổng PLQG timeout vs 500 — distinguish error path | `cb_nv_tw_01`. DevTools Network throttle = "Slow 3G" (60s+ delay). | — | 1. Click [Công khai]. 2. Backend gọi API → request hang >timeout policy. | **STATE**: Backend timeout sau N giây (timeout policy — SRS Gap, mark **SPEC-CLARIFY-BM-13**), rollback transactional như 500 (BR-EC-20). **UI**: Toast error tương đương ERR-CK-02 hoặc message phân biệt timeout — verify behavior thực tế. **PERSIST**: trang_thai vẫn NHAP. Verify retry queue có entry timeout (nếu có policy retry). | Negative | P1 |

---

## C. EDGE / WARNING

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-306 | WRN-CK-01 | Click Công khai trên thư mục đã CONG_KHAI | `cb_nv_tw_01`. Thư mục "Folder X" đã CONG_KHAI (do batch hoặc race). User mở 2 tab. | — | 1. Tab1 đã công khai. 2. Tab2 chưa refresh, click [Công khai]. | **STATE**: Backend trả warning, không thay đổi state. **UI**: Toast warning nguyên văn "Thư mục đã ở trạng thái công khai" (srs-fr-09:254 WRN-CK-01). **PERSIST**: trang_thai giữ CONG_KHAI. AUDIT_LOG không ghi PUBLISH duplicate. | Edge | P1 |
| TC-BM-307 | FR-VII-03 / BR-EC-19 | Batch công khai hàng loạt — boundary 100 record | `cb_nv_tw_01`. Đã có 105 thư mục NHAP có ≥1 BM. | Chọn 105 checkbox | 1. Tích checkbox header "Chọn tất cả". 2. Click [Công khai hàng loạt] (srs-fr-09:607). 3. Confirm. | **STATE**: Backend chia batch (BR-EC-19 max 100/request). **UI**: Hoặc 100 thành công + 5 yêu cầu re-submit; hoặc toast warning "Tối đa 100 record/lần" (SRS Gap message → mark **SPEC-CLARIFY-BM-02**). **PERSIST**: 100 record state CONG_KHAI; 5 vẫn NHAP. | Edge | P1 |

---

## Tổng số TC: 9 (4 Happy + 3 Negative + 2 Edge) — A3 base 7 + A4 merged 2
**Priority**: P0=5 / P1=4 / P2=0

**Coverage:**
- BR (formal SRS §6): BR-FLOW-05, BR-FLOW-07
- BR (working labels srs-v3.md inline): BR-EC-19 (batch 100), BR-BM-05/06/11 (publish guards) — see 00-test-plan §2.1 footnote
- Error codes: ERR-CK-01, ERR-CK-02, WRN-CK-01
- AC SRS: 4/4 (srs-fr-09:269-272)
- SM-BIEUMAU (THU_MUC scope): NHAP→CONG_KHAI (TC-301), CONG_KHAI→AN (TC-302), AN→CONG_KHAI (TC-308 sau A4 merged)
- A4 merged 2026-05-06: TC-BM-308 (re-publish AN→CONG_KHAI), TC-BM-309 (timeout vs 500)
- Codex review 2026-05-09: Fix TC-BM-305 — bỏ giả định BR-EC-20 rollback (không có trong srs-fr-09 §6), đổi thành SPEC-CLARIFY-BM-15 verify behavior thực tế.
- SPEC-CLARIFY: BM-02 (batch boundary message), BM-13 (timeout policy interval), BM-15 (rollback policy ERR-CK-02)
