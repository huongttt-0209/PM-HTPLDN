# Test Cases — DM Cơ quan Đơn vị (FR-VIII-05, UC103) — Tree 2 tầng

> **Module:** QTHT — DM dùng chung · **FR:** FR-VIII-05 · **UC:** UC103
> **Màn hình:** SCR-VIII-01 — Sub-tab "Cơ quan ĐV" (đặc thù: tree-view + form chi tiết panel, KHÔNG dùng table chuẩn)
> **URL:** `/quan-tri/danh-muc/CO_QUAN_DON_VI` (hoặc tab thứ 5 trong sidebar SCR-VIII-01)
> **Entity:** DON_VI (riêng, không dùng DANH_MUC chung)
> **BR critical:** **BR-AUTH-02 cây 2 tầng** (TW root duy nhất → {BN, ĐP} ngang cấp song song dưới TW; BN không có ĐP trực thuộc)
> **Tổng số TC:** 38 (32 base + 3 edge A4 + 3 fill R2)

---

## A. Render tree 2-tầng

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CQDV-001 | qtht_01 đăng nhập, env có seed: 1 TW (Cục BLDS&KT) + 18 BN + 63 ĐP | Mở tab Cơ quan ĐV | Tree render với root TW expandable; click expand → 18 BN + 63 ĐP cấp con đều thuộc TW làm cha (KHÔNG có BN ↔ ĐP nested) | BR-AUTH-02, line 1475 |
| TC-CQDV-002 | tree mở | Click ĐP "Sở Tư pháp Hà Nội" | Form chi tiết bên phải hiển thị: ma_don_vi, ten_don_vi, cap=DP, don_vi_cha_id=TW (Cục BLDS&KT), dia_chi, dien_thoai, email, trang_thai | line 1476-1478, line 326-334 |
| TC-CQDV-003 | tree mở, chọn BN "Bộ Tài chính" | Click BN | Form bên phải: cap=BN, don_vi_cha_id=TW (Cục BLDS), KHÔNG có cấp con bên dưới (mô hình 2-tier) | BR-AUTH-02 |
| TC-CQDV-004 | tree mở, click TW Cục BLDS&KT | Verify TW root | Form TW: cap=TW, **don_vi_cha_id field hidden hoặc disabled** (entity DON_VI line 1967 nguyên văn "NULL khi cap=TW"); nếu user toggle cap → BN, field don_vi_cha_id phải bật + bắt buộc | line 1967 (don_vi_cha_id NULL khi cap=TW) |
| TC-CQDV-005 | tree mở, click TW expand/collapse 2 lần | Toggle | Cây thu/mở đúng; KHÔNG mất state form đang mở | — |
| TC-CQDV-006 | tree mở, BN "Bộ Tài chính" | Verify form: nút [+ Thêm đơn vị con] | **DISABLED hoặc HIDDEN cho BN/DP** — BR-AUTH-02 enforce 2-tier (BN không có cấp con; DP cũng không). Click nút (nếu có) phải reject hoặc không trigger modal tạo | BR-AUTH-02 line 2161, line 1477 |
| TC-CQDV-007 | tree mở, TW root | Form TW: nút [+ Thêm đơn vị con] | Cho phép tạo BN/DP trực tiếp dưới TW | line 1477 |

---

## B. Tạo mới đơn vị

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CQDV-008 | tree mở, click TW root → [+ Thêm đơn vị con] | Form mở: nhập ma_don_vi="TEST_BN_01", ten="Test BN 01", cap="BN", don_vi_cha_id auto-fill TW (readonly), dia_chi="Hà Nội", trang_thai=Hoạt động → Lưu | Tạo OK; cây refresh hiển thị BN mới dưới TW; audit INSERT | line 313-323, BR-AUTH-02 |
| TC-CQDV-009 | tree mở, [+ Thêm con] dưới TW | cap="DP", ten="Test DP 01" | Tạo DP OK; tree refresh; cây 2-tầng giữ nguyên | BR-AUTH-02 |
| TC-CQDV-010 | tạo mới với ma_don_vi="CỤC_BLDS" (đã có TW) | Submit | ERR-DV-01 "Mã đơn vị 'CỤC_BLDS' đã tồn tại" | E1 line 343 |
| TC-CQDV-011 | tạo mới cap="BN", quên chọn don_vi_cha_id | Submit (system bypass auto-fill) | ERR-DV-02 "Cấp BN phải có đơn vị cha" | E2 line 345, line 319 |
| TC-CQDV-012 | tạo mới cap="DP", chọn don_vi_cha_id = "Bộ Tài chính" (BN, không phải TW) | Submit | **Reject với "Đơn vị cha phải có cấp = TW"** — BR-AUTH-02 + line 319 nguyên văn "đơn vị cha phải có cap = TW (enforce mô hình 2-tier)". UI nên hide option non-TW khỏi dropdown don_vi_cha_id | BR-AUTH-02 line 2161, line 319 |
| TC-CQDV-013 | tạo mới cap="TW" trong env đã có 1 TW Cục BLDS&KT (cố tạo TW thứ 2) | Submit | **Reject vì model 2-tier chỉ có 1 TW root** — BR-AUTH-02 mô tả "TW (cấp 1, Cục BLDS&KT) → {BN, ĐP}" — TW là root duy nhất. UI nên disable option TW trong dropdown khi đã có 1 TW (hoặc backend reject với uniqueness constraint) | BR-AUTH-02 line 2161, line 293-294 (mô tả "1 TW") |
| TC-CQDV-014 | tạo mới cap="BN", ten= rỗng | Submit | Validation "Tên đơn vị là bắt buộc" | line 305 |
| TC-CQDV-015 | tạo mới với email="invalid-email" | Submit | Validation format email (nếu validate); spec không nguyên văn — verify | line 310 |
| TC-CQDV-016 | tạo mới cap="DP", chọn TW làm cha → Lưu | Submit | Tạo OK; record mới có don_vi_cha_id = TW (trực tiếp, KHÔNG qua BN) | BR-AUTH-02 line 320 |

---

## C. Cập nhật đơn vị

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CQDV-017 | "TEST_BN_01" tồn tại, click chọn → form mở | Đổi ten="Test BN 01 updated", dia_chi="Hà Nội updated" → Lưu | Lưu OK; tree refresh ten mới; audit UPDATE | — |
| TC-CQDV-018 | "TEST_BN_01" mở | Đổi ma_don_vi sang "BO_TAI_CHINH" (đã có) | ERR-DV-01 trùng | E1 |
| TC-CQDV-019 | TW Cục BLDS mở | Cố đổi cap TW → BN | Reject hoặc warning (vì TW có 18 BN + 63 DP làm con, đổi cap sẽ phá cây) `[SPEC-CLARIFY-DM-11]` | BR-AUTH-02 |
| TC-CQDV-020 | "TEST_BN_01" mở | Đổi cap BN → DP, vẫn cha=TW | Lưu OK (cả BN và DP đều cùng cấp 2, cha=TW); cây refresh hiển thị "TEST_BN_01" dưới nhánh ĐP | BR-AUTH-02 |
| TC-CQDV-021 | "TEST_BN_01" có 5 TAI_KHOAN don_vi_id tham chiếu | Đổi cap → DP | Lưu OK; audit UPDATE; **alert hiển thị** "Thay đổi cấp/đơn vị cha sẽ cập nhật chính sách phân quyền" (line 1478). Verify hành vi data scope của 5 TK liên kết — nếu spec không nói explicit thì log finding `[SPEC-CLARIFY-DM-29]` (không assume) | line 1478, BR-DATA-05 |
| TC-CQDV-022 | "TEST_BN_01" mở | Đổi trang_thai HOAT_DONG → TAM_DUNG | Lưu OK; tree hiển thị badge "Tạm dừng" cho BN này | line 311, line 1973 |

---

## D. Xóa đơn vị (soft delete + ràng buộc)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CQDV-023 | "TEST_BN_01" mới tạo, không có TK liên kết, không có dữ liệu nghiệp vụ | Click Xóa → confirm | Soft delete OK; cây refresh ẩn; audit DELETE | BR-DATA-01 |
| TC-CQDV-024 | BN "Bộ Tài chính" có 5 TAI_KHOAN don_vi_id tham chiếu | Xóa | Reject ERR-DV-03 "Không thể xóa. Đơn vị có 5 tài khoản liên kết" | E3 line 346 |
| TC-CQDV-025 | ĐP "Sở Tư pháp Hà Nội" có HOI_DAP/VU_VIEC don_vi_id tham chiếu | Xóa | Reject ERR-DV-04 "Không thể xóa. Đơn vị có N bản ghi dữ liệu" | E4 line 347 |
| TC-CQDV-026 | TW Cục BLDS root | Xóa | Reject (BLOCK xóa root, vì sẽ phá cây và mọi BN/DP đều mất cha) `[SPEC-CLARIFY-DM-18]` | BR-AUTH-02 |

---

## E. Edge case 2-tier guard

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CQDV-027 | Tạo mới với don_vi_cha_id trỏ chính nó (vòng lặp 1 cấp) | Submit | ERR-DV-05 "Không thể tạo vòng lặp phân cấp" | E5 line 348, line 320 |
| TC-CQDV-028 | Sửa BN "Bộ Tài chính" đổi don_vi_cha_id thành chính nó | Submit | ERR-DV-05 | E5 |
| TC-CQDV-029 | Mô hình 2-tier verify: cố tạo BN với cha là BN khác | Submit cap="BN", don_vi_cha_id=Bộ Tài chính | Reject: "Đơn vị cha phải có cap=TW" — nested BN không cho phép | BR-AUTH-02 line 319 |
| TC-CQDV-030 | Mô hình 2-tier: cố tạo DP với cha là DP khác | Submit cap="DP", don_vi_cha_id=Sở Tư pháp HN | Reject tương tự | BR-AUTH-02 |
| TC-CQDV-031 | Mô hình 2-tier: tạo BN với cha là DP | Submit cap="BN", don_vi_cha_id=Sở Tư pháp HN | Reject "Đơn vị cha phải có cap=TW" | BR-AUTH-02 |

---

## F. Cảnh báo phân quyền

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CQDV-032 | "TEST_BN_01" có TK liên kết, mở Sửa | Đổi cap BN → DP | Alert hiển thị "Thay đổi cấp/đơn vị cha sẽ cập nhật chính sách phân quyền" trước khi lưu | line 1478 |

---

## G. Edge case bổ sung (A4 inline merge)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CQDV-EDGE-001 | TW Cục BLDS có 18 BN + 63 DP children | Mở Sửa TW, đổi cap TW → BN | Reject với reasoning "TW có {N} đơn vị con — không thể đổi cấp"; hoặc cascade prompt confirmation `[SPEC-CLARIFY-DM-22]` | BR-AUTH-02 |
| TC-CQDV-EDGE-002 | TW có 50+ BN/DP children (env stress) | Click expand TW root | Tree expand <2s; KHÔNG block UI; verify lazy load hoặc virtualize (NFR performance) | NFR perf |
| TC-CQDV-EDGE-003 | cb_nv_dp_05 đang đăng nhập với don_vi_id = "Sở TP Hà Nội" | qtht_01 đổi trạng thái Sở TP Hà Nội từ HOAT_DONG → TAM_DUNG | Spec không nói rõ session impact — verify hành vi observed: cb_nv_dp_05 thử thao tác list VV/HD → log response (200 OK với scope cũ / 403 invalidate / login redirect). Mark `[SPEC-CLARIFY-DM-23]` chờ BA quyết định session lifecycle khi đơn vị TAM_DUNG | line 1973 (TAM_DUNG state), `[SPEC-CLARIFY-DM-23]` |

---

## H. Fill gap (R2 Codex review — required negative + enum guard)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-CQDV-FILL-001 | qtht_01 mở [+ Thêm], cap = "FAKE_CAP" (giá trị ngoài enum TW/BN/DP) | Submit | Reject với validation "Cấp phải thuộc TW/BN/DP" hoặc dropdown chỉ cho 3 giá trị nên không submit được | line 306, line 318 (CHECK constraint enum) |
| TC-CQDV-FILL-002 | [+ Thêm] cap="BN", chọn don_vi_cha_id = `999999` (UUID/id không tồn tại trong DB DON_VI) | Submit | Reject với "Đơn vị cha không tồn tại" hoặc dropdown chỉ cho phép chọn TW có thật → không submit được id rác | line 319 (kiểm tra đơn vị cha tồn tại) |
| TC-CQDV-FILL-003 | [+ Thêm] cap="TW", don_vi_cha_id = `<TW Cục BLDS id>` (cố ép TW có cha) | Submit | Reject với "TW không được có đơn vị cha" — BR-AUTH-02 enforce TW root duy nhất, don_vi_cha_id phải NULL khi cap=TW | BR-AUTH-02, line 1967 ("NULL khi cap=TW") |

---

**Tổng số TC:** 38 (32 base + 3 edge A4 + 3 fill R2)
**Đặc thù vs TPL chung:**
1. Entity DON_VI riêng, không dùng DANH_MUC
2. Tree-view UI thay table
3. BR-AUTH-02 enforce 2-tier (TW → BN/DP, không BN→DP nested, không multi-TW)
4. ERR-DV-01..05 (5 error codes riêng, đặc thù)
5. Trạng thái HOAT_DONG/TAM_DUNG (text) thay boolean

**SPEC-CLARIFY mới phát hiện (sau R4 cleanup):**
- ~~DM-10~~ resolved R4: TW có don_vi_cha_id NULL theo entity DON_VI line 1967 → form ẩn/disable field (expected explicit, không cần BA)
- ~~DM-15~~ resolved R4: BR-AUTH-02 nói BN/DP không có cấp con → nút disabled/hidden cho BN/DP (expected explicit)
- ~~DM-16~~ resolved R4: BR-AUTH-02 + line 319 nói cha của BN/DP phải = TW → reject DP/cha=BN (expected explicit)
- ~~DM-17~~ resolved R4: BR-AUTH-02 mô hình 2-tier 1 TW root duy nhất → reject TW thứ 2 (expected explicit)
- DM-18: Xóa TW root có guard không? (vẫn pending — spec im lặng về "delete TW root")
