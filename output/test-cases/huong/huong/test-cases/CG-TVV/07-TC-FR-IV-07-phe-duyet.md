# Test Cases — FR-IV-07: Phê duyệt TVV (Optimistic Lock + Auto cấp TK + Mail kích hoạt)

> **SRS Ref**: FR-IV-07 (UC45), SCR-IV-03 (header + modal MD-PHE-DUYET) + SCR-IV-01 batch, Entity TU_VAN_VIEN, SM-TVV (CHO_PHE_DUYET → CHO_KICH_HOAT / TU_CHOI), SM-TAIKHOAN (CHO_KICH_HOAT mới)
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:555-628`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PD-UI-01 | FR-IV-07 / SCR-IV-03 / UI Modal MD-PHE-DUYET | Verify modal Phê duyệt có 2 field bắt buộc | cb_pd_tw_01, TVV-TW-500 CHO_PHE_DUYET (cb_nv_tw_01 thẩm định) | — | 1. Login cb_pd_tw_01<br>2. Mở chi tiết TVV-TW-500<br>3. Click "Phê duyệt" header → Modal MD-PHE-DUYET | **MODAL fields**: so_quyet_dinh* (text input format `QĐ-{số}/QĐ-{đơn_vị}`, max 100 ký), y_kien_phe_duyet (textarea max 2000 ký, optional), Confirm/Cancel buttons<br>**Modal title**: "Xác nhận phê duyệt và công bố?"<br>**Body**: "Bạn đang công bố **{tên TVV-TW-500}** vào mạng lưới tư vấn viên pháp luật. Vui lòng nhập Số quyết định công bố." | Happy 🔴 |
| TC-PD-UI-02 | FR-IV-07 / SCR-IV-01 batch | Verify tab "Chờ phê duyệt" có batch action "Phê duyệt hàng loạt" | cb_pd_tw_01, ≥3 TVV CHO_PHE_DUYET TW | — | 1. Login cb_pd_tw_01<br>2. Mở SCR-IV-01 tab "Chờ phê duyệt"<br>3. Verify | Tab visible chỉ cho CB PD; Checkbox cột đầu mỗi row; Action bar "Phê duyệt hàng loạt" / KHÔNG có "Từ chối hàng loạt" (BR-FLOW-02 — chỉ batch approve, reject từng record) | Happy 🔴 |

## B. Phê duyệt happy path

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PD-001 | FR-IV-07 / AC1+AC2 | Happy path Phê duyệt → CHO_KICH_HOAT + auto cấp TK + mail kích hoạt | cb_pd_tw_01, TVV-TW-500 CHO_PHE_DUYET (email a@example.com chưa có TK) | so_quyet_dinh: "QĐ-001/QĐ-TW", y_kien: "Đạt yêu cầu" | 1. Click Phê duyệt<br>2. Modal nhập so_quyet_dinh<br>3. Confirm<br>4. Verify network + DB + mail | **STATE**: TU_VAN_VIEN.trang_thai=CHO_KICH_HOAT, ngay_cong_nhan=NOW, thoi_gian_duyet=NOW, nguoi_duyet=cb_pd_tw_01.id, so_quyet_dinh="QĐ-001/QĐ-TW", version+1; **TAI_KHOAN insert mới** với username từ email a@example.com, password=NULL, trang_thai=CHO_KICH_HOAT, link tới TVV qua tai_khoan_id; **TAI_KHOAN_VAI_TRO insert** vai trò "TVV" (theo loai_tvv); AUDIT_LOG INSERT 3 entries (UPDATE TVV + INSERT TK + INSERT VAI_TRO)<br>**UI**: Toast "Phê duyệt thành công, đã gửi mail kích hoạt cho tư vấn viên"; Badge "Chờ kích hoạt tài khoản" xanh dương<br>**PERSIST**: MailHog kiểm tra inbox a@example.com có mail "Kích hoạt tài khoản" với link `/kich-hoat?token=...` (1 lần dùng); TVV-TW-500 biến mất khỏi tab "Chờ phê duyệt", xuất hiện ở tab "Chờ kích hoạt" (nếu có) hoặc badge tổng | Happy 🔴 |
| TC-PD-002 | FR-IV-07 / AC5 + SM-TVV CHO_KICH_HOAT→HOAT_DONG | TVV bấm link kích hoạt + đặt mật khẩu → TVV và TK đồng thời HOAT_DONG | TVV-TW-500 CHO_KICH_HOAT, mail kích hoạt đã gửi | password mới: "Secret@123" | 1. TVV mở mail kích hoạt<br>2. Click link `/kich-hoat?token=...`<br>3. Form đặt mật khẩu lần đầu<br>4. Submit | **STATE**: TAI_KHOAN.password = hash("Secret@123"), trang_thai=HOAT_DONG; TU_VAN_VIEN.trang_thai = HOAT_DONG (đồng thời); AUDIT_LOG INSERT<br>**UI**: Redirect login page với message "Kích hoạt thành công, vui lòng đăng nhập"<br>**PERSIST**: TVV có thể login bằng email + Secret@123 vào chuyên trang | Happy 🔴 |

## C. Optimistic Lock (FR-IV-07 step 0)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PD-101 | FR-IV-07 / E3 ERR-PD-04 | 2 CB PD duyệt cùng lúc → optimistic lock conflict | cb_pd_tw_01 + cb_pd_tw_02 cùng cấp, TVV-TW-501 CHO_PHE_DUYET version=0 | so_quyet_dinh different | 1. Mở 2 browser tab cùng TVV-TW-501<br>2. cb_pd_tw_01 click Phê duyệt + submit<br>3. cb_pd_tw_02 click Phê duyệt (vẫn dùng version=0)<br>4. Verify | **STATE**: cb_pd_tw_01 PASS (version 0→1, trạng thái CHO_KICH_HOAT); cb_pd_tw_02 fail vì version mismatch<br>**UI cb_pd_tw_02**: Toast "Tư vấn viên đã được duyệt bởi {tên cb_pd_tw_01} lúc {time}, vui lòng tải lại trang để xem trạng thái mới" (NGUYÊN VĂN ERR-PD-04)<br>**PERSIST**: Reload TVV-TW-501 → trạng thái CHO_KICH_HOAT, KHÔNG ghi đè | Negative 🔴 |

## D. BR-AUTH-05 cùng cấp

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PD-201 | FR-IV-07 / E1 BR-AUTH-05 ERR-PD-02 | CB PD khác cấp (TW duyệt hồ sơ ĐP) → ERR-PD-02 | cb_pd_tw_01, TVV-DP-001 CHO_PHE_DUYET (cb_nv_dp_01 thẩm định) | — | 1. Login cb_pd_tw_01<br>2. Cố mở chi tiết TVV-DP-001 → click Phê duyệt | API 403 "Chỉ phê duyệt hồ sơ cùng cấp" (NGUYÊN VĂN ERR-PD-02); UI ẩn nút Phê duyệt (TVV-DP-001 không hiện trong tab "Chờ phê duyệt" của cb_pd_tw_01 vì BR-AUTH-08 + BR-AUTH-05) | Negative 🔴 |
| TC-PD-202 | FR-IV-07 / Cùng cấp ĐP (NĐ 121/2025) | cb_pd_dp_01 (HN) duyệt hồ sơ TVV cb_nv_dp_01 (HN) thẩm định | cb_pd_dp_01, TVV-HN-001 CHO_PHE_DUYET | so_quyet_dinh: "QĐ-001/QĐ-STP-HN" | 1. Login cb_pd_dp_01<br>2. Phê duyệt | PASS — UBND tỉnh có thẩm quyền theo NĐ 121/2025 Đ.39-40; trạng thái → CHO_KICH_HOAT | Happy 🟡 |

## E. Từ chối + lý do

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PD-301 | FR-IV-07 / AC4 | CB PD từ chối + lý do ≥10 ký | cb_pd_tw_01, TVV-TW-502 CHO_PHE_DUYET | quyet_dinh=TU_CHOI, ly_do="Hồ sơ chưa đầy đủ minh chứng kinh nghiệm" | 1. Click Từ chối<br>2. Modal MD-TU-CHOI nhập lý do<br>3. Confirm | **STATE**: TU_VAN_VIEN.trang_thai=TU_CHOI, thoi_gian_tu_choi=NOW, nguoi_tu_choi=cb_pd_tw_01.id, ly_do_tu_choi cập nhật, version+1; AUDIT_LOG<br>**UI**: Toast "Đã từ chối"; Badge "Đã từ chối" đỏ<br>**PERSIST**: Email gửi TVV/CG (chủ hồ sơ) với lý do; TVV-TW-502 biến mất khỏi tab "Chờ phê duyệt" | Happy 🔴 |
| TC-PD-302 | FR-IV-07 / E2 ERR-PD-03 | Từ chối thiếu lý do → ERR-PD-03 | cb_pd_tw_01 | ly_do: "" | 1. Submit TU_CHOI lý do trống | Inline error "Lý do từ chối là bắt buộc (≥10 ký tự)" (NGUYÊN VĂN ERR-PD-03) | Negative 🟡 |
| TC-PD-303 | FR-IV-07 / Lý do <10 ký | Từ chối lý do <10 ký → ERR-PD-03 | cb_pd_tw_01 | ly_do: "thieu" | 1. Submit | Inline error "Lý do từ chối là bắt buộc (≥10 ký tự)" (NGUYÊN VĂN ERR-PD-03 — SRS line 611) | Negative 🟡 |

## F. ERR-PD-05 missing số QĐ + WRN-PD-01 mail fail

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PD-401 | FR-IV-07 / E4 ERR-PD-05 | Phê duyệt thiếu so_quyet_dinh → ERR-PD-05 | cb_pd_tw_01 | so_quyet_dinh: "" | 1. Submit Phê duyệt không nhập số QĐ | Inline error "Số quyết định công nhận là bắt buộc khi phê duyệt" (NGUYÊN VĂN ERR-PD-05) | Negative 🟡 |
| TC-PD-402 | FR-IV-07 / W1 WRN-PD-01 | Mail kích hoạt fail → vẫn duyệt + warning | cb_pd_tw_01, MailHog DOWN, TVV-TW-503 CHO_PHE_DUYET | — | 1. Stop MailHog<br>2. Phê duyệt TVV-TW-503<br>3. Verify | **STATE**: TVV → CHO_KICH_HOAT; TK đã tạo CHO_KICH_HOAT (vẫn thành công); chỉ mail send fail<br>**UI**: Warning toast "Hồ sơ đã được duyệt, tài khoản đã tạo ở trạng thái Chờ kích hoạt. Mail kích hoạt gửi không thành công. Tư vấn viên có thể dùng chức năng 'Quên mật khẩu' với email đã đăng ký để nhận lại link" (NGUYÊN VĂN WRN-PD-01)<br>**PERSIST**: Audit log có entry mail fail; TVV có thể dùng FR-VIII-26 Quên mật khẩu để đặt lại | Edge 🔴 |

## G. Batch approve (BR-FLOW-02)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PD-501 | FR-IV-07 / BR-FLOW-02 batch | Phê duyệt hàng loạt 3 TVV cùng cấp | cb_pd_tw_01, 3 TVV-TW-510/511/512 CHO_PHE_DUYET | so_quyet_dinh per record | 1. Tab "Chờ phê duyệt" check 3 row<br>2. Click "Phê duyệt hàng loạt"<br>3. Modal MD-PHE-DUYET-HANG-LOAT bảng nhập so_quyet_dinh per record<br>4. Confirm | **STATE**: 3 TVV chuyển CHO_KICH_HOAT đồng loạt, mỗi TVV có so_quyet_dinh riêng; 3 TK insert; 3 mail gửi<br>**UI**: Toast "Đã phê duyệt 3 hồ sơ thành công" | Happy 🔴 |
| TC-PD-502 | FR-IV-07 / BR-FLOW-02 negative | KHÔNG có "Từ chối hàng loạt" trên UI | cb_pd_tw_01 | — | 1. Tab "Chờ phê duyệt" check 3 row<br>2. Verify action bar | Action bar có "Phê duyệt hàng loạt" + "Bỏ chọn", KHÔNG có "Từ chối hàng loạt" (BR-FLOW-02) | Negative 🔴 |
| TC-PD-503 | FR-IV-07 / Batch partial fail | 3 TVV batch — 2 PASS 1 FAIL (1 mail server fail) | cb_pd_tw_01, MailHog flaky | — | 1. Batch 3 record<br>2. Mock 1 mail fail<br>3. Verify | UI hiển thị "2 thành công, 1 cảnh báo (mail fail)"; SPEC-CLARIFY-CGTVV-05 nếu SRS không define partial behavior chi tiết | Edge 🟡 |

---

## H. EDGE bổ sung (A4 inline merge — 6 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PD-601 | EDGE-A4-cc / Batch size limit | Batch approve ≥50 record (max?) | cb_pd_tw_01, ≥50 TVV CHO_PHE_DUYET | — | 1. Check 50 row<br>2. Phê duyệt hàng loạt | SPEC-CLARIFY-CGTVV-13 nếu SRS không define batch size limit; default UI cho phép max 50? | Edge 🟡 |
| TC-PD-602 | EDGE-A4-dd / Batch mixed cấp | Batch trên list mixed cấp (TW+ĐP cùng tab) → chỉ approve cùng cấp | cb_pd_tw_01, batch 3 TVV-TW + 2 TVV-ĐP | — | 1. Batch 5 row<br>2. Submit | 3 TVV-TW PASS, 2 TVV-ĐP fail ERR-PD-02 (BR-AUTH-05); UI report "3 thành công, 2 thất bại (khác cấp)" | Edge 🔴 |
| TC-PD-603 | EDGE-A4-ee / Reload sau OptLock | Reload sau OptLock conflict → version refresh → retry PASS | cb_pd_tw_01, TVV-TW-501 đã được duyệt bởi cb_pd_tw_02 | — | 1. Reload page sau ERR-PD-04<br>2. Verify version mới<br>3. KHÔNG còn nút Phê duyệt vì state đã CHO_KICH_HOAT | UI cập nhật state mới; KHÔNG có action Phê duyệt nữa | Edge 🟡 |
| TC-PD-604 | EDGE-A4-ff / Token kích hoạt expired | TVV bấm link kích hoạt sau 30 ngày (giả định expired) | TVV-TW-500 CHO_KICH_HOAT, mail kích hoạt 30+ days ago | — | 1. Click link expired | Trang lỗi "Link đã hết hạn"; gợi ý dùng FR-VIII-26 Quên mật khẩu để nhận link mới; SPEC-CLARIFY-CGTVV-14 expiry duration | Edge 🟡 |
| TC-PD-605 | EDGE-A4-j / Sanitize SQL trong so_quyet_dinh | so_quyet_dinh chứa SQL injection | cb_pd_tw_01 | so_quyet_dinh: `QĐ-001'; DROP TABLE--` | 1. Submit Phê duyệt | Sanitize PASS — query parameterized; lưu literal value; KHÔNG execute SQL | Edge 🔴 |
| TC-PD-606 | EDGE-A4-x / Mail server fail giữa batch | Batch 5 TVV — mail server fail cho 2 TVV (verify qua UI report) | cb_pd_tw_01, MailHog flaky | — | 1. Batch 5<br>2. 2 mail send fail<br>3. **Verify qua UI batch result modal + check trạng thái TVV trên list** (KHÔNG verify queue trực tiếp) | UI MD-CONG-KHAI-PARTIAL-FAIL hoặc tương đương "3 thành công, 2 cảnh báo (mail fail)"; 5 TVV vẫn → CHO_KICH_HOAT (state success — verify qua list reload); 2 mail có thể retry qua FR-VIII-26 (verify qua chức năng Quên MK) — **A7 SỬA: bỏ verify queue trực tiếp, dùng list reload + chức năng FR-VIII-26 làm UI bridge** | Edge 🟡 |

---

**Tổng số TC**: 24 (2 UI + 2 Happy + 1 OptLock + 2 BR-AUTH-05 + 3 Reject + 2 ERR-PD-05/WRN-PD-01 + 3 Batch + 3 misc + 6 Edge A4) — A6 sẽ điều chỉnh
