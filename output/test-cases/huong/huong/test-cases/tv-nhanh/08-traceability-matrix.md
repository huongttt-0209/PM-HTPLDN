# A5 — Traceability Matrix (FR-13 TV Nhanh)

> **Phase:** A5 — bmad-testarch-trace
> **Ngày tạo:** 2026-05-10
> **Mục đích:** Map BR / AC / Permission / Error code / SM transition / Entity attribute ↔ TC. **KHÔNG sinh TC mới** — gap phát hiện forward sang A6 fix.

---

## 1. Tổng kết coverage

| Loại trace | Tổng | Cover | % | Gap forward A6 |
|-----------|-----|-------|---|-----------------|
| BR formal §6 | 8 | 8 | 100% | 0 |
| AC SRS | 13 | 12 | 92.3% | 1 (AC FR-X.2-04 chỉ search) |
| Permission Matrix cells | 10 | 10 | 100% | 0 |
| Error codes | 13 | 11 | 84.6% | 2 (ERR-DG-TVN HTTP 400/404 chỉ trong API spec) |
| SM-TVNHANH transitions | 8 | 8 | 100% | 0 |
| KHO_CAU_HOI state lifecycle | 5 | 5 | 100% | 0 |
| Entity attribute (KHO_CAU_HOI key fields) | 13 | 12 | 92.3% | 1 (so_luot_xem counter chưa cover) |

---

## 2. BR Trace

| BR | TC ref | Coverage |
|----|--------|----------|
| BR-AUTH-01 | TC-KHO-001 (precondition login), TC-PHIEN-001, TC-CK-001, TC-PERM-001..006 | ✅ |
| BR-AUTH-05 | TC-KHO-105, TC-PERM-005, TC-PERM-006 | ✅ |
| BR-AUTH-08 | TC-KHO-104, TC-PHIEN-101, TC-PERM-004 | ✅ |
| BR-DATA-01 | TC-KHO-007 (soft delete) | ✅ |
| BR-DATA-04 | TC-KHO-017 (auto-gen QA-YYYYMMDD-SEQ) | ✅ |
| BR-DATA-05 | TC-KHO-018, TC-CK-008 | ✅ |
| BR-DATA-07 | TC-KHO-016, TC-PHIEN-012 | ✅ |
| BR-DATA-08 | TC-KHO-014, TC-PHIEN-005, TC-DN-004 | ✅ |
| BR-FLOW-05 | TC-CK-001, TC-CK-100, TC-CK-101 | ✅ |
| BR-FLOW-10 | TC-KHO-009 (TU_DONG), TC-KHO-013 (IMPORT), TC-KHO-003 (THU_CONG) | ✅ |
| BR-PUBLIC-01 | TC-CK-102 (block CHO_DUYET công khai) | ✅ |
| BR-PUBLIC-02 | TC-CK-004 (clear thoi_gian_dang_tai) | ✅ |
| BR-PUBLIC-03 | TC-CK-005 (format dd/mm/yyyy hh:mm + disabled) | ✅ |

**BR Coverage:** 13/13 = **100%** (8 BR formal §6 + 5 BR working labels từ master srs-v3.md).

---

## 3. AC Trace

| AC | FR | Mô tả | TC ref | Coverage |
|----|-----|------|--------|----------|
| AC1 | FR-X.2-01 | CB NV truy cập "Kho câu hỏi" → DS Q&A + phân trang | TC-KHO-001 | ✅ |
| AC2 | FR-X.2-01 | CB NV thêm mới → validate + lưu CHO_DUYET | TC-KHO-003 | ✅ |
| AC3 | FR-X.2-01 | Q&A nhóm II đã duyệt → tự động thêm vào kho | TC-KHO-009 | ✅ |
| AC4 | FR-X.2-01 | Q&A hết hiệu lực → CB NV đánh dấu → ẩn khỏi Cổng | TC-KHO-008 + TC-DN-005 | ✅ |
| AC1 | FR-X.2-02 | DN gửi câu hỏi → keyword search kho → gợi ý trả lời | TC-DN-001 + TC-PHIEN-005 | ✅ |
| AC2 | FR-X.2-02 | CB NV xem câu hỏi chờ → chọn → hiển thị gợi ý + chỉnh sửa → gửi | TC-PHIEN-006 + TC-PHIEN-007 | ✅ |
| AC1 | FR-X.2-03 | DN nhập câu hỏi + chọn TV nhanh → phân luồng keyword search | TC-DN-001 | ✅ |
| AC2 | FR-X.2-03 | DN chọn TV thủ công → chuyển nhóm II | TC-DN-002 | ✅ |
| AC3 | FR-X.2-03 | DN chuyển kênh → giữ toàn bộ lịch sử | TC-DN-003 | ✅ |
| AC1 | FR-X.2-04 | DN nhập từ khóa → search Q&A phù hợp | TC-DN-004 | ⚠️ Partial (chỉ verify backend filter, KHÔNG verify UI Cổng PLQG vì ngoài CMS) |
| AC1 | FR-X.2-05 | DN xem câu trả lời → đánh giá → lưu | TC-DGTV-001 | ✅ |
| AC2 | FR-X.2-05 | Cổng PLQG gửi lại đánh giá cùng Idempotency-Key → trả kết quả lần đầu | TC-DGTV-004 | ✅ |
| AC1-4 | FR-X.2-06 | CK / Hủy CK / API fail / CK CHO_DUYET block | TC-CK-001/004/100/102 | ✅ |

**AC Coverage:** 12.5/13 = **96.2%** (1 partial AC1 FR-X.2-04 — UI Cổng PLQG ngoài scope CMS).

**Gap A5 → forward A6:**
- **GAP-AC-01:** AC1 FR-X.2-04 chỉ verify backend search filter (TC-DN-004). UI search Cổng PLQG ngoài scope CMS module → A7 sẽ filter tagged "side-effect verify only".

---

## 4. Permission Matrix Trace

| Action / Role × Cell | TC ref | Coverage |
|----------------------|--------|----------|
| QTHT Read-only Kho | TC-PERM-001 | ✅ |
| QTHT Read-only phiên TVN | TC-PERM-001 | ✅ |
| CB_NV CRUD Kho cùng đơn vị | TC-KHO-003/006/007 | ✅ |
| CB_NV cross-tenant block | TC-KHO-104, TC-PERM-004 | ✅ |
| CB_PD phê duyệt cùng cấp | TC-KHO-010 | ✅ |
| CB_PD cross-cấp block | TC-KHO-105, TC-PERM-005, TC-PERM-006 | ✅ |
| CB_NV CK/Hủy CK | TC-CK-001, TC-CK-004 | ✅ |
| CB_NV trả lời phiên TVN | TC-PHIEN-007 | ✅ |
| TVV/CG/NHT 403 | TC-PERM-002 | ✅ |
| DN 403 CMS | TC-PERM-003 | ✅ |

**Permission Coverage:** 10/10 = **100%**.

---

## 5. Error Code Trace

| Error code | TC ref | Coverage |
|------------|--------|----------|
| ERR-KHO-01 (cau_hoi trống) | TC-KHO-100 | ✅ |
| ERR-KHO-02 (cau_tra_loi trống) | TC-KHO-101 | ✅ |
| ERR-KHO-03 (linh_vuc invalid) | TC-KHO-102 | ✅ |
| ERR-KHO-04 (file Excel sai format) | TC-KHO-103 | ✅ |
| ERR-TVN-01 (kho rỗng — WARNING) | TC-PHIEN-010 | ✅ |
| ERR-TVN-02 (noi_dung_tra_loi trống) | TC-PHIEN-100 | ✅ |
| ERR-TVN-DN-01 (DN cau_hoi trống) | TC-DN-100 (active sau Codex P1-001 fix) | ✅ |
| ERR-TVN-TK-01 (DN search < 2 ký tự) | TC-DN-101 (active sau Codex P1-002 fix) | ✅ |
| ERR-DG-TVN-01 (điểm ngoài 1-5) | TC-DGTV-100, TC-DGTV-101 | ✅ |
| ERR-DG-TVN-02 (phiên không tồn tại) | TC-DGTV-102 | ✅ |
| HTTP 400 Bad Request | TC-DGTV-100/101 (gián tiếp) | ⚠️ Gián tiếp (chưa có TC riêng test malformed JSON) |
| HTTP 404 (`tu_van_nhanh_id` không tồn tại) | TC-DGTV-102 | ✅ |
| HTTP 409 Conflict Idempotency | TC-DGTV-004 | ✅ |
| HTTP 401 Unauthorized | TC-DGTV-103 | ✅ |
| ERR-TVN-CK-01 (API CK fail) | TC-CK-100 | ✅ |
| ERR-TVN-CK-02 (API Hủy CK fail) | TC-CK-101 | ✅ |
| ERR-TVN-CK-03 (state không cho phép) | TC-CK-102 | ✅ |
| INF-TVN-TK-01 (no results DN search) | (chưa cover trực tiếp) | ❌ GAP |

**Error Code Coverage:** 16/18 = **88.9%**.

**Gap A5 → forward A6:**
- **GAP-ERR-01:** INF-TVN-TK-01 (no results DN search) chưa có TC riêng — cần thêm TC trong file 03 verify side-effect "không kết quả" hiển thị Cổng.
- **GAP-ERR-02:** HTTP 400 Bad Request (malformed JSON, missing required field tu_van_nhanh_id) chưa cover riêng — cần TC test API inbound malformed payload.

---

## 6. SM-TVNHANH Transition Trace

| # | Transition | Trigger | TC ref | Coverage |
|---|-----------|---------|--------|----------|
| 1 | [*] → MOI | DN gửi câu hỏi (FR-X.2-03) | TC-DN-001 | ✅ |
| 2 | MOI → DANG_TIM_KIEM | HT nhận câu hỏi | TC-DN-001 (verify gián tiếp) | ✅ |
| 3 | DANG_TIM_KIEM → DA_GOI_Y | Có kết quả search | TC-PHIEN-005 (verify trạng thái khi mở phiên) | ✅ |
| 4 | DANG_TIM_KIEM → CB_TRA_LOI | Kho rỗng / không match | TC-PHIEN-010 | ✅ |
| 5 | DA_GOI_Y → CB_TRA_LOI | DN chưa hài lòng, CB NV trả lời | TC-PHIEN-007 | ✅ |
| 6 | DA_GOI_Y → HOAN_THANH | DN hài lòng + đánh giá | TC-PHIEN-008 + TC-DGTV-006 | ✅ |
| 7 | CB_TRA_LOI → HOAN_THANH | DN đánh giá | TC-PHIEN-009 + TC-DGTV-006 | ✅ |
| 8 | MOI → HET_HAN | Auto 30 ngày | TC-PHIEN-011 | ✅ |

**SM Coverage:** 8/8 = **100%**.

---

## 7. KHO_CAU_HOI State Lifecycle

| State | TC ref vào state | TC ref ra state | Coverage |
|-------|------------------|------------------|----------|
| NHAP | TC-KHO-005 (Lưu nháp) | TC-KHO-006 (Sửa) / TC-KHO-007 (Xóa) | ✅ |
| CHO_DUYET | TC-KHO-003 (THU_CONG) / TC-KHO-013 (IMPORT) | TC-KHO-010 (DA_DUYET) / TC-KHO-011 (NHAP do từ chối) | ✅ |
| DA_DUYET | TC-KHO-009 (TU_DONG auto) / TC-KHO-010 (CB PD duyệt) | TC-CK-001 (CONG_KHAI) / TC-KHO-008 (HET_HIEU_LUC) | ✅ |
| CONG_KHAI | TC-CK-001 | TC-CK-004 (DA_DUYET) | ✅ |
| HET_HIEU_LUC | TC-KHO-008 | (re-enable hieu_luc — chưa cover) | ⚠️ Partial |

**Gap A5 → forward A6:**
- **GAP-STATE-01:** Re-enable hieu_luc (HET_HIEU_LUC → DA_DUYET) chưa có TC riêng — cần TC trong file 01.

---

## 8. Entity KHO_CAU_HOI Attribute Coverage

| Attribute | TC ref | Coverage |
|-----------|--------|----------|
| ma_cau_hoi | TC-KHO-017 | ✅ |
| cau_hoi | TC-KHO-003, TC-KHO-100, TC-KHO-200 | ✅ |
| cau_tra_loi | TC-KHO-003, TC-KHO-101 | ✅ |
| linh_vuc_id | TC-KHO-003, TC-KHO-102 | ✅ |
| nguon | TC-KHO-009 (TU_DONG), TC-KHO-013 (IMPORT), TC-KHO-003 (THU_CONG) | ✅ |
| hoi_dap_goc_id | TC-KHO-009 | ✅ |
| trang_thai | TC-KHO-008, TC-CK-001/004 | ✅ |
| diem_danh_gia_tb | TC-DGTV-002, TC-DGTV-003 | ✅ |
| so_luot_xem | (counter chưa cover) | ❌ GAP |
| tu_khoa | TC-KHO-003, TC-KHO-205 | ✅ |
| cong_khai (boolean cờ UI) | TC-CK-006 | ✅ |
| anh_dai_dien | TC-KHO-004, TC-KHO-201, TC-CK-203 | ✅ |
| thoi_gian_dang_tai | TC-CK-005, TC-CK-001 | ✅ |
| mo_ta_cong_khai | TC-KHO-004, TC-CK-002, TC-CK-003 | ✅ |
| file_dinh_kem_cong_khai | TC-KHO-004, TC-KHO-202, TC-KHO-203, TC-CK-002, TC-CK-003 | ✅ |
| hieu_luc | TC-KHO-008 | ✅ |

**Attribute Coverage:** 15/16 = **93.75%**.

**Gap A5 → forward A6:**
- **GAP-ATTR-01:** so_luot_xem (counter lượt xem) chưa có TC verify increment khi DN view Q&A trên Cổng PLQG. Cần TC trong file 03 hoặc 01 verify counter.

---

## 9. Cross-FR Integration Trace

| Integration | TC ref | Coverage |
|-------------|--------|----------|
| FR-13 ↔ FR-02 (HOI_DAP DA_DUYET → KHO_CAU_HOI TU_DONG) | TC-KHO-009 | ✅ |
| FR-13 ↔ FR-02 (DN chọn TV_THU_CONG → tạo HOI_DAP) | TC-DN-002 | ✅ |
| FR-13 ↔ FR-10 W1.1 (AUDIT_LOG) | TC-CK-008, TC-KHO-018 | ✅ |
| FR-13 ↔ FR-11 (Báo cáo điểm TB) | (ngoài scope W4.3, chuyển W5.2) | OOS |

---

## 10. Tổng kết Gap forward sang A6

| Gap ID | Mô tả | TC mới cần thêm |
|--------|-------|------------------|
| GAP-AC-01 | UI Cổng PLQG search ngoài scope CMS | A7 sẽ filter — không cần TC mới |
| GAP-ERR-01 | INF-TVN-TK-01 chưa cover riêng | TC-DN-300 (no results side-effect) |
| GAP-ERR-02 | HTTP 400 malformed JSON API inbound DG | TC-DGTV-300 (malformed payload) |
| GAP-STATE-01 | Re-enable hieu_luc HET_HIEU_LUC → DA_DUYET | TC-KHO-300 (toggle hieu_luc back ON) |
| GAP-ATTR-01 | so_luot_xem counter chưa cover | TC-KHO-301 (verify counter increment khi DN xem) |

**Total gap:** 5 gap → A6 sẽ fill 4 TC mới (GAP-AC-01 không cần — A7 filter).

---

*Generated 2026-05-10 — Phase A step A5 (bmad-testarch-trace) — KHÔNG sinh TC mới, gap forward A6*
