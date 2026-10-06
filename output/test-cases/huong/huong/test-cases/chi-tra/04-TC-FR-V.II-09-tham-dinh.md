# TC — FR-V.II-09: Thẩm định Hồ sơ Chi trả

> **UC ref**: UC76 | **Screen**: SCR-V.II-02 section 5 (Thẩm định) | **SRS**: srs-fr-06:552-616 + 987-991
> **Roles**: CB_NV (TW/BN/DP) only
> **Mục tiêu**: Verify đối chiếu 4 checklist (Số liệu khớp Mẫu 01 / Phí TV hợp lý / Quy mô DN đúng / Chưa vượt trần năm) + 3 kết quả (Đạt/Không đạt/Cần bổ sung) + nhận xét bắt buộc khi KHONG_DAT + so_tien_de_xuat input + transition state.

## Preconditions

- HS X đang ở DANG_THAM_DINH (đã qua đánh giá — TC-CT-DG-002)
- Login `cb_nv_tw_01`
- HS X có DANH_GIA_HO_SO_CHI_TRA gắn (so_tien_duoc_duyet đã tính)

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-TD-001 | HS X DANG_THAM_DINH, ket_qua_tham_dinh chưa có | 1. Vào /chi-tra/:id 2. Verify section "Thẩm định" hiện | Section 5 hiện 4 checkbox đối chiếu: ☐ Số liệu khớp Mẫu 01 / ☐ Phí TV hợp lý / ☐ Quy mô DN đúng / ☐ Chưa vượt trần năm. Radio "Đạt / Không đạt". Textarea "Lý do không đạt" + Field input "Số tiền đề xuất" | AC#1, srs-fr-06:988-991 | P0 |
| TC-CT-TD-002 | HS X DANG_THAM_DINH | 1. Tick 4/4 checkbox 2. Chọn "Đạt" 3. Nhập số tiền đề xuất 2.500.000đ 4. Click "Lưu" hoặc tương đương | HS X giữ DANG_THAM_DINH, `ket_qua_tham_dinh = DAT`, `so_tien_de_xuat = 2500000`. Nút "Trình phê duyệt" mở (FR-V.II-11). Tạo bản ghi THAM_DINH_HO_SO (1:1, nguoi_tham_dinh_id, ngay_tham_dinh=NOW()). | SM-CHITRA, srs-fr-06:585, srs-fr-06:1208-1226 | P0 |
| TC-CT-TD-003 | HS X DANG_THAM_DINH | 1. Tick 1/4 checkbox 2. Chọn "Không đạt" 3. Để Nhận xét trống 4. Click "Lưu" | Validation error inline "Nhận xét là bắt buộc khi không đạt" (ERR-CT-TD-02). KHÔNG submit | ERR-CT-TD-02, srs-fr-06:610 | P0 |
| TC-CT-TD-004 | HS X DANG_THAM_DINH | 1. Tick 1/4 2. Chọn "Không đạt" 3. Nhập Nhận xét "Số liệu phí tư vấn không khớp với HĐ TVPL kèm theo" (≥10 ký tự) 4. Submit | HS X → TU_CHOI. `ly_do_tu_choi = "THAM_DINH: Số liệu phí tư vấn..."`, `thoi_gian_tu_choi = NOW()`, `nguoi_tu_choi_id = cb_nv_tw_01.id`. Tạo bản ghi THAM_DINH_HO_SO (ket_qua_tham_dinh=KHONG_DAT, nhan_xet). TB DN/TVV. | SM-CHITRA, srs-fr-06:587 | P0 |
| TC-CT-TD-005 | HS X DANG_THAM_DINH | 1. Chọn "Cần bổ sung" 2. Nhập nhận xét "Cần bổ sung biên nhận thanh toán phí TV" 3. Submit | HS X giữ DANG_THAM_DINH, `ket_qua_tham_dinh = CAN_BO_SUNG`. Gửi TB DN/TVV bổ sung tài liệu (KHÔNG chuyển state). Nút Trình PD KHÔNG mở | srs-fr-06:586 | P0 |
| TC-CT-TD-006 | HS X DANG_THAM_DINH với ket_qua_tham_dinh=CAN_BO_SUNG (đã bổ sung) | 1. Vào /chi-tra/:id 2. Tick 4/4 3. Chọn "Đạt" 4. Submit | Cập nhật THAM_DINH_HO_SO (UPDATE 1:1), ket_qua_tham_dinh=DAT. Nút Trình PD mở | srs-fr-06:1208 (1:1 UNIQUE) | P1 |
| TC-CT-TD-007 | HS Y DANG_DANH_GIA (chưa qua đánh giá) | 1. Force POST API thẩm định Y | ERR-CT-TD-01 "Hồ sơ không ở trạng thái chờ thẩm định" — HTTP 400 | ERR-CT-TD-01, srs-fr-06:609 | P0 |
| TC-CT-TD-008 | HS X DANG_THAM_DINH, đã có ket_qua=DAT | 1. Vào /chi-tra/:id 2. Verify section 6 "Phê duyệt" KHÔNG hiện vẫn (chưa CHO_PHE_DUYET) | Stepper [Thẩm định] đang highlight, nút "Trình phê duyệt" hiện. Section 6 ẩn (conditional render — srs-fr-06:992) | AC#1, srs-fr-06:992 | P1 |
| TC-CT-TD-009 (Codex FINDING-CT-05 fix) | HS X DANG_THAM_DINH, so_tien_de_xuat = 0đ (allowed CHECK ≥ 0 — srs-fr-06:1219) | 1. Tick 4/4 2. Chọn "Đạt" 3. Nhập 0đ 4. Submit | Cho phép lưu so_tien_de_xuat=0. **HS giữ nguyên DANG_THAM_DINH** (Đạt KHÔNG transition state, chỉ ghi `ket_qua_tham_dinh=DAT` và mở nút "Trình phê duyệt" — srs-fr-06:585). DANH_GIA_HO_SO_CHI_TRA đã có so_tien_duoc_duyet=0 từ EC-01 | srs-fr-06:585, srs-fr-06:1219 | P1 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-TD-010 | HS X DANG_THAM_DINH, so_tien_duoc_duyet=2.500.000đ | 1. Tick 4/4 2. Đạt 3. Nhập so_tien_de_xuat = 5.000.000đ (vượt số duyệt) 4. Submit | **SPEC-CLARIFY-CT-04**: SRS không quy định ràng buộc so_tien_de_xuat ≤ so_tien_duoc_duyet (chỉ ≥0 — srs-fr-06:1219). Cho phép nhưng UI nên cảnh báo "Vượt số tiền được duyệt từ đánh giá". CB PD ở UC79 sẽ lấy quyết định cuối | **SPEC-CLARIFY-CT-04**, srs-fr-06:1219 | P1 |
| TC-CT-TD-011 | HS X DANG_THAM_DINH, đã có THAM_DINH_HO_SO ket_qua=DAT (thẩm định lần 1) | 1. Sửa Đối chiếu 2. Click Lưu lần 2 | Backend UPDATE bản ghi THAM_DINH_HO_SO 1:1 (UNIQUE ho_so_chi_tra_id — srs-fr-06:1216). KHÔNG tạo bản ghi mới. AUDIT_LOG ghi sửa | srs-fr-06:1216 | P1 |
| TC-CT-TD-012 | HS X DANG_THAM_DINH | 1. Tick 0/4 2. Chọn Đạt 3. Submit | UI rule mâu thuẫn nội bộ: chưa đối chiếu mà vẫn Đạt. **SPEC-CLARIFY-CT-05**: SRS chỉ định 4 checklist là "đối chiếu" (srs-fr-06:988) nhưng KHÔNG bắt buộc tick all → UC76 step 3 "Xem toàn bộ thông tin HS + chứng từ + kết quả đánh giá" gợi ý CB NV review trước. UI nên có warning nhưng không block | **SPEC-CLARIFY-CT-05** | P1 |
| TC-CT-TD-013 | HS X DANG_THAM_DINH | 1. Nhận xét chứa XSS payload 2. Submit | Backend sanitize. Display plain text Timeline | BR-EC-13 | P0 |

## Tổng số TC: 13 (sau A4: +4 edge)

**P0: 7** | P1: 6

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-04)
