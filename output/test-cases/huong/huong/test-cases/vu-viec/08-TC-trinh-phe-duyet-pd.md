# Test Cases — UC61 + UC62 + UC63: Trình PD + Thông báo KQ + Phê duyệt VV (FR-V.I-11 + FR-V.I-12 + FR-V.I-13)

> **SRS Ref**: FR-V.I-11 (srs-fr-05:841-888), FR-V.I-12 (srs-fr-05:892-940), FR-V.I-13 (srs-fr-05:944-1000), BR-AUTH-05 (srs-fr-05:2385-2389), BR-FLOW-04 (srs-fr-05:2439-2443), BR-NOTIF-01 (srs-fr-05:2499-2503)
> **Ngày tạo**: 2026-05-06 (BMAD A3) · **A7 filter applied**: 2026-05-06
> **Tài khoản chính**:
> - `cb_nv_tw_01..03` (CB NV TW trình PD)
> - `cb_pd_tw_01..03` (CB PD TW phê duyệt cùng cấp)
> - `cb_pd_bn_01` (CB PD BN khác cấp — test ERR-PD-02)
> - `nht_01..03` (NHT — nhận thông báo khi từ chối PD)
> **OTP**: `666666`
> **A7 note**: FR-V.I-12 (UC62 thông báo KQ) là auto trigger — verify gián tiếp qua `list_network_requests` (in-app + email + LGSP outbound) thay vì test API thuần.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-PD-UI-01 | FR-V.I-11 / SCR-V.I-03 action trình PD | Verify nút [Trình Phê duyệt] trên SCR-V.I-03 + form ghi chú trình | `cb_nv_tw_01`. VV-X đã kiểm tra đạt + đã phân công NHT (state DANG_XU_LY hoặc DA_PHAN_CONG đủ điều kiện). | — | 1. Mở SCR-V.I-03 chi tiết VV-X. 2. Quan sát action-bar. 3. Click [Trình Phê duyệt]. 4. Quan sát modal/form. | **UI**: (1) Action-bar có nút [Trình Phê duyệt] (xanh primary) bên cạnh [Cập nhật KQ]. (2) Click → modal "Trình phê duyệt VV-X" với 1 textarea `ghi_chu_trinh` (optional, srs-fr-05:858-859) + 2 nút [Hủy] [Xác nhận trình]. (3) Header modal hiển thị thông tin tóm tắt VV: Mã VV / Tên DN / NHT / Lĩnh vực. | Happy | P1 |
| TC-VV-PD-UI-02 | FR-V.I-13 / SCR-V.I-03 action PD | Verify CB PD thấy 2 nút [Phê duyệt] + [Từ chối] + textarea lý do (conditional ≥10 ký tự) | `cb_pd_tw_01`. VV-X ở CHO_PHE_DUYET. | — | 1. Login `cb_pd_tw_01`. 2. Mở SCR-V.I-03 VV-X. 3. Quan sát action-bar. 4. Click [Từ chối] → quan sát modal. | **UI**: (1) Action-bar 2 nút lớn: [Phê duyệt] (xanh) + [Từ chối] (đỏ). (2) Banner thông tin "VV này chờ phê duyệt từ CB NV TW 01 lúc dd/mm HH:mm" (srs-fr-05:867 BR-FLOW-03 cùng cấp). (3) Click [Từ chối] → modal "Lý do từ chối phê duyệt" với textarea bắt buộc + counter "0/10 ký tự tối thiểu" (srs-fr-05:998 AC3 ≥10 ký tự) + nút [Xác nhận từ chối] disable đến khi đủ 10. | Happy | P1 |
| TC-VV-PD-UI-03 | FR-V.I-13 / SCR-V.I-01 batch PD | Verify batch action-bar [Phê duyệt hàng loạt] khi check ≥2 VV ở CHO_PHE_DUYET | `cb_pd_tw_01`. ≥3 VV ở CHO_PHE_DUYET trong scope. | — | 1. SCR-V.I-01. 2. Filter trạng thái CHO_PHE_DUYET. 3. Check 3 VV. 4. Quan sát action-bar. | **UI**: Sau check ≥1 VV → action-bar sticky bottom "[Phê duyệt hàng loạt] [Từ chối hàng loạt] (3 VV đã chọn)" (srs-fr-05:946-947). Click [Phê duyệt hàng loạt] → confirm modal "Phê duyệt 3 vụ việc?" + DS preview Mã VV. Click [Từ chối hàng loạt] → modal lý do dùng chung cho tất cả. | Happy | P1 |

---

## B. CRUD HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-PD-101 | FR-V.I-11 AC1 | Trình PD VV đủ điều kiện → CHO_PHE_DUYET | `cb_nv_tw_01`. VV-X đã kiểm tra đạt + đã phân công + đã có KQ NHT (state DANG_XU_LY). | ghi_chu_trinh="Đã review hoàn tất, trình duyệt" | 1. SCR-V.I-03 VV-X. 2. [Trình Phê duyệt]. 3. Nhập ghi chú. 4. [Xác nhận trình]. | **STATE**: Backend (1) check VV đủ ĐK: đã kiểm tra (PRE-02 srs-fr-05:851) + đã phân công NHT (srs-fr-05:865); (2) UPDATE VU_VIEC SET trang_thai='CHO_PHE_DUYET' (srs-fr-05:866); (3) gửi thông báo CB PD cùng cấp (BR-AUTH-05 srs-fr-05:867 + 2385-2389). **UI**: Toast success "Đã trình phê duyệt VV-X". Stepper bước "Chờ phê duyệt" active. Nút [Trình PD] biến mất. **PERSIST**: AUDIT_LOG TRINH_PD (BR-DATA-05 srs-fr-05:869). Verify network: POST `/vu-viec/{id}/trinh-pd` 200, GET `/notifications/recent` thấy in-app gửi `cb_pd_tw_01..03`. | Happy | P0 |
| TC-VV-PD-102 | FR-V.I-13 AC2 / single PHE_DUYET | CB PD phê duyệt single VV → DA_DUYET | `cb_pd_tw_01` (cùng cấp TW). VV-X ở CHO_PHE_DUYET. | quyet_dinh=PHE_DUYET | 1. Login `cb_pd_tw_01`. 2. SCR-V.I-03 VV-X. 3. [Phê duyệt]. 4. Confirm. | **STATE**: Backend (1) check BR-AUTH-05 cùng cấp (srs-fr-05:973 + 2385-2389); (2) UPDATE VU_VIEC SET trang_thai='DA_DUYET', nguoi_phe_duyet_id=`cb_pd_tw_01`, ngay_phe_duyet=NOW() (srs-fr-05:974). **UI**: Toast success. Stepper bước "Đã duyệt" active. Action-bar PD biến mất. **PERSIST**: AUDIT_LOG PHE_DUYET (BR-DATA-05 srs-fr-05:978). Verify network: POST `/vu-viec/{id}/phe-duyet` body `{quyet_dinh:'PHE_DUYET'}` 200, BR-NOTIF-01 → in-app + email gửi `cb_nv_tw_01` (người trình). | Happy | P0 |
| TC-VV-PD-103 | FR-V.I-13 AC3 / TU_CHOI → DANG_XU_LY (BR-FLOW-04) | CB PD từ chối với lý do ≥10 ký tự → VV quay về DANG_XU_LY (KHÔNG đóng VV) | `cb_pd_tw_01`. VV-Y ở CHO_PHE_DUYET. | quyet_dinh=TU_CHOI, ly_do="Cần bổ sung thêm chứng cứ pháp lý đoạn 3" (50 ký tự) | 1. Login `cb_pd_tw_01`. 2. SCR-V.I-03 VV-Y. 3. [Từ chối]. 4. Nhập lý do 50 ký tự. 5. [Xác nhận từ chối]. | **STATE**: Backend (1) check ly_do ≥10 ký tự (srs-fr-05:993 ERR-PD-03 + 998 AC3); (2) UPDATE VU_VIEC SET trang_thai='DANG_XU_LY' (KHÔNG TU_CHOI! BR-FLOW-04 quay về NHT sửa, srs-fr-05:975, 984, 2439-2443); (3) ghi `ly_do` vào LICH_SU_VU_VIEC (srs-fr-05:975); (4) gửi thông báo CB NV phụ trách + NHT (srs-fr-05:976, 985). **UI**: Toast success "Đã từ chối, VV quay về xử lý". Stepper rollback bước "Đang xử lý" active. Banner đỏ "VV bị CB PD từ chối — Lý do: '...'" hiển thị cho NHT khi vào VV-Y. **PERSIST**: AUDIT_LOG TU_CHOI_PD + ly_do (BR-DATA-05 + BR-FLOW-04). Verify network: BR-NOTIF-01 → 2 in-app (CB NV `cb_nv_tw_01` + NHT) + 2 email. | Happy | P0 |
| TC-VV-PD-104 | FR-V.I-13 / batch PHE_DUYET 5 VV uniform | CB PD phê duyệt hàng loạt 5 VV cùng CHO_PHE_DUYET | `cb_pd_tw_01`. 5 VV ở CHO_PHE_DUYET (cùng cấp TW). | — | 1. SCR-V.I-01. 2. Filter CHO_PHE_DUYET. 3. Check 5 VV. 4. [Phê duyệt hàng loạt]. 5. Confirm. | **STATE**: Backend loop từng VV transactional, mỗi VV → DA_DUYET, ngay_phe_duyet=NOW(). Atomic per-VV (1 fail không rollback toàn bộ). **UI**: Progress bar "Đang xử lý 1/5 ... 5/5". Toast success "Đã phê duyệt 5/5 vụ việc". 5 VV biến mất khỏi tab CHO_PHE_DUYET, xuất hiện tab "Đã duyệt". **PERSIST**: AUDIT_LOG 5 entry PHE_DUYET. Verify network: POST `/vu-viec/batch/phe-duyet` body `{ids:[5 ids]}` 200 với response per-VV result. BR-NOTIF-01 → 5 in-app + 5 email. | Happy | P0 |
| TC-VV-TB-105 | FR-V.I-12 / auto trigger sau PD | UC62 auto gửi thông báo KQ DN sau khi VV chuyển DA_DUYET | `cb_pd_tw_01`. VV-X ở DA_DUYET (sau TC-VV-PD-102). DN-X có email + chuyên trang DN active. | — | 1. Verify ngay sau TC-VV-PD-102 success. 2. Check DN inbox + chuyên trang DN. | **STATE**: Backend auto trigger (srs-fr-05:892, 894 — auto sau PD). (1) Tạo THONG_BAO in-app cho DN (srs-fr-05:917); (2) Gửi email DN (srs-fr-05:918); (3) Nếu HS qua DVC: gọi LGSP outbound (srs-fr-05:919). **UI**: — (verify gián tiếp qua DN-side). Verify network từ CB NV side: `list_network_requests` thấy POST `/notifications/dn` + (optional) POST `/lgsp/outbound`. **PERSIST**: THONG_BAO record cho DN. AUDIT_LOG entry. **SPEC-CLARIFY-VV-TB-01**: SRS srs-fr-05:892-940 không quote rõ trigger event chính xác (sau PD? sau kiểm tra? sau TU_CHOI?) — verify behavior thực tế. | Happy | P0 |

---

## C. NEGATIVE — VALIDATION ERRORS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-PD-201 | FR-V.I-11 / ERR-TR-01 | Trình PD khi chưa kiểm tra | `cb_nv_tw_01`. VV-A ở CHO_TIEP_NHAN (chưa kiểm tra). | — | 1. Mở SCR-V.I-03 VV-A. 2. Cố click [Trình Phê duyệt]. | **STATE**: Backend reject (srs-fr-05:865 + 881). **UI**: Hoặc nút [Trình PD] disable + tooltip "Hồ sơ chưa kiểm tra đạt"; hoặc click → toast error nguyên văn "Hồ sơ chưa kiểm tra đạt" (ERR-TR-01 srs-fr-05:881). **PERSIST**: KHÔNG có thay đổi. | Negative | P0 |
| TC-VV-PD-202 | FR-V.I-11 / ERR-TR-02 | Trình PD khi chưa phân công NHT | `cb_nv_tw_01`. VV-B đã kiểm tra đạt nhưng chưa phân công (state DANG_KIEM_TRA hoặc trở về DA_TIEP_NHAN sau từ chối). | — | 1. Mở SCR-V.I-03 VV-B. 2. Cố click [Trình Phê duyệt]. | **STATE**: Backend reject (srs-fr-05:865 + 882). **UI**: Toast error nguyên văn "Chưa phân công người hỗ trợ" (ERR-TR-02 srs-fr-05:882). Hoặc nút disable + tooltip. **PERSIST**: KHÔNG có thay đổi. | Negative | P0 |
| TC-VV-PD-203 | FR-V.I-13 / ERR-PD-01 | PD khi VV không ở CHO_PHE_DUYET | `cb_pd_tw_01`. VV-C ở DANG_XU_LY (chưa được trình). | quyet_dinh=PHE_DUYET | 1. Login `cb_pd_tw_01`. 2. Cố access URL `/vu-viec/{vv_c_id}/phe-duyet` trực tiếp. | **STATE**: Backend reject (srs-fr-05:991). **UI**: Hoặc redirect 404; hoặc toast error nguyên văn "Vụ việc không ở trạng thái chờ phê duyệt" (ERR-PD-01 srs-fr-05:991). **PERSIST**: KHÔNG có thay đổi. | Negative | P0 |
| TC-VV-PD-204 | FR-V.I-13 / ERR-PD-02 / BR-AUTH-05 | CB PD khác cấp cố phê duyệt (BN cố duyệt VV của TW) | `cb_pd_bn_01` (cấp BN). VV-X ở CHO_PHE_DUYET cấp TW. | quyet_dinh=PHE_DUYET | 1. Login `cb_pd_bn_01`. 2. Cố access SCR-V.I-03 VV-X (TW). 3. Cố click [Phê duyệt]. | **STATE**: Backend reject BR-AUTH-05 cùng cấp (srs-fr-05:973, 992, 2385-2389 nguyên văn "CB NV cấp nào tạo → CB PD cùng cấp duyệt. KHÔNG xuyên cấp"). **UI**: Hoặc `cb_pd_bn_01` không thấy VV-X trong DS; hoặc click → toast error nguyên văn "Bạn không có quyền phê duyệt vụ việc này" (ERR-PD-02 srs-fr-05:992). **PERSIST**: KHÔNG có thay đổi. AUDIT_LOG ghi attempt. | Negative | P0 |
| TC-VV-PD-205 | FR-V.I-13 / ERR-PD-03 / lý do <10 ký tự | TU_CHOI với ly_do chỉ 5 ký tự | `cb_pd_tw_01`. VV-Y ở CHO_PHE_DUYET. | quyet_dinh=TU_CHOI, ly_do="Sai" (3 ký tự) | 1. SCR-V.I-03 VV-Y. 2. [Từ chối]. 3. Nhập 3 ký tự. 4. [Xác nhận từ chối]. | **STATE**: BE/FE reject (srs-fr-05:993 + 998 AC3 ≥10 ký tự). **UI**: Hoặc client validate (counter "3/10 ký tự tối thiểu" + nút disable); hoặc submit → toast error nguyên văn "Lý do từ chối là bắt buộc" (ERR-PD-03 srs-fr-05:993). **SPEC-CLARIFY-VV-PD-01**: ERR-PD-03 message "Lý do từ chối là bắt buộc" không khớp với case <10 ký tự (đã có lý do nhưng quá ngắn) → mark gap-report nếu BE cần message riêng "Lý do tối thiểu 10 ký tự". **PERSIST**: KHÔNG có thay đổi. | Negative | P0 |
| TC-VV-PD-206 | FR-V.I-13 / TU_CHOI ly_do trống | TU_CHOI để trống ly_do | `cb_pd_tw_01`. VV-Y ở CHO_PHE_DUYET. | quyet_dinh=TU_CHOI, ly_do="" | 1. [Từ chối]. 2. Bỏ trống textarea. 3. [Xác nhận từ chối]. | **STATE**: BE/FE reject (srs-fr-05:967 conditional bắt buộc + 993). **UI**: Toast error nguyên văn "Lý do từ chối là bắt buộc" (ERR-PD-03 srs-fr-05:993) hoặc client inline error. Nút submit disable. **PERSIST**: KHÔNG có thay đổi. | Negative | P1 |
| TC-VV-PD-207 | FR-V.I-13 / batch mixed state | Batch PHE_DUYET với 5 VV mixed (3 CHO_PHE_DUYET + 2 DA_DUYET đã PD trước đó) | `cb_pd_tw_01`. Check 5 VV mixed (3 valid + 2 đã DA_DUYET). | — | 1. Filter "Tất cả". 2. Check 5 VV mixed. 3. [Phê duyệt hàng loạt]. | **STATE**: Backend per-VV transaction. 3 VV CHO_PHE_DUYET → DA_DUYET success; 2 VV DA_DUYET → reject ERR-PD-01. **UI**: Confirm modal "Phê duyệt 3/5 VV đủ điều kiện. 2 VV khác state sẽ bị bỏ qua" (tương tự pattern TC-VV-DS-303). Toast warning "Đã PD 3/5. 2 VV gặp lỗi (nhấn xem chi tiết)". Modal chi tiết list 2 VV fail + lý do "Vụ việc không ở trạng thái chờ phê duyệt". **PERSIST**: AUDIT_LOG 3 PHE_DUYET. | Negative | P0 |

---

## D. EDGE CASES

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-PD-301 | BR-EC-01 / Optimistic lock 2 tab | CB PD mở 2 tab cùng phê duyệt 1 VV | Tab1 + Tab2 cùng `cb_pd_tw_01`. VV-X ở CHO_PHE_DUYET. | — | 1. Tab1 [Phê duyệt] VV-X. 2. Tab2 (chưa reload) [Phê duyệt] VV-X. | **STATE**: Tab1 SUCCESS — VV-X → DA_DUYET. Tab2 FAIL ERR-PD-01 (vì state đã đổi) hoặc optimistic lock conflict. **UI**: Tab1 toast success. Tab2 modal "Vụ việc đã được CB PD TW 01 cập nhật lúc dd/mm HH:mm. Vui lòng tải lại" (BR-EC-01) hoặc toast "Vụ việc không ở trạng thái chờ phê duyệt". **PERSIST**: AUDIT_LOG 1 entry PHE_DUYET. | Edge | P0 |
| TC-VV-PD-302 | FR-V.I-13 / cycle TU_CHOI → sửa → trình lại | NHT sửa KQ sau PD từ chối → CB NV trình lại → CB PD duyệt thành công | Sau TC-VV-PD-103 (VV-Y ở DANG_XU_LY do PD từ chối). | — | 1. Login `nht_01`. 2. Cập nhật KQ VV-Y (UC65 — sang file 09). 3. Login `cb_nv_tw_01`. 4. [Trình PD] lần 2. 5. Login `cb_pd_tw_01`. 6. [Phê duyệt]. | **STATE**: Cycle: DANG_XU_LY → CHO_PHE_DUYET (lần 2) → DA_DUYET. LICH_SU_VU_VIEC tích lũy: TU_CHOI_PD lần 1 + TRINH_PD lần 2 + PHE_DUYET. **UI**: Stepper bình thường. Tab "Lịch sử" Accordion 7 hiện đầy đủ 3 entry mới. **PERSIST**: AUDIT_LOG 3 entry. KHÔNG có giới hạn số lần cycle (**SPEC-CLARIFY-VV-PD-02** nếu cần policy giới hạn). | Edge | P1 |
| TC-VV-TB-303 | FR-V.I-12 / WRN-TB-01 email fail | Gửi email DN fail (SMTP timeout) → WRN-TB-01 + queue retry | `cb_pd_tw_01`. Mock SMTP server trả timeout. VV-X chuẩn bị PD. | — | 1. PD VV-X như TC-VV-PD-102. 2. Verify outbox + log. | **STATE**: Backend (1) PD success → DA_DUYET (KHÔNG rollback do email fail); (2) auto trigger UC62 → email SMTP timeout → log WARNING; (3) queue retry. **UI**: CB PD vẫn thấy toast "PD success". Trên log/admin có entry "Gửi email thất bại, thử lại sau" (WRN-TB-01 srs-fr-05:933). DN có thể chưa nhận email lúc t0 nhưng nhận in-app ngay (in-app không phụ thuộc SMTP). **PERSIST**: VV-X = DA_DUYET. THONG_BAO in-app present. Email queue có retry entry. **SPEC-CLARIFY-VV-TB-02**: SRS không quote rõ retry policy (interval/max attempt) → mark gap-report. | Edge | P1 |
| TC-VV-TB-304 | FR-V.I-12 / WRN-TB-02 LGSP fail | HS qua DVC + LGSP fail → WRN-TB-02 + queue retry | `cb_pd_tw_01`. VV-Z (kênh DVC). Mock LGSP endpoint trả 500. | — | 1. PD VV-Z. 2. Verify log. | **STATE**: Backend (1) PD success; (2) trigger gửi LGSP outbound (srs-fr-05:919); (3) LGSP 500 → log WARNING. **UI**: Toast PD success vẫn hiện. Admin/Audit log thấy WRN-TB-02 "Không thể đồng bộ với HT TTHC BTP" (srs-fr-05:934). **PERSIST**: VV-Z = DA_DUYET. LGSP queue có retry entry. Verify network: POST `/lgsp/outbound` 500 trong list_network_requests. | Edge | P1 |
| TC-VV-PD-305 | FR-V.I-11 / Trình lại sau khi NHT cập nhật KQ mới | CB NV trình lần 2 sau khi NHT update KQ (TC tổng hợp với UC65 file 09) | Sau TC-VV-PD-103 + NHT đã update KQ. | ghi_chu_trinh="Đã sửa theo góp ý PD" | 1. SCR-V.I-03 VV-Y (DANG_XU_LY sau PD từ chối). 2. [Trình Phê duyệt] lần 2. | **STATE**: Backend cho phép trình lại (KHÔNG có giới hạn số lần srs-fr-05:865-870). UPDATE VV → CHO_PHE_DUYET. **UI**: Toast success. Lịch sử Accordion thấy 2 entry TRINH_PD. **PERSIST**: AUDIT_LOG TRINH_PD lần 2. | Edge | P1 |
| TC-VV-PD-306 | FR-V.I-13 / batch lock - 1 VV bị optimistic lock giữa batch | Batch PD 3 VV nhưng 1 VV bị CB PD khác đã duyệt vài giây trước | Tab1 `cb_pd_tw_01` check 3 VV. Tab2 `cb_pd_tw_02` đã duyệt 1 trong 3 VV xong. | — | 1. Tab1 trễ 30s sau Tab2 đã PD VV-A. 2. Tab1 [Phê duyệt hàng loạt] (3 VV gồm VV-A). | **STATE**: Backend per-VV transaction. VV-A FAIL (đã DA_DUYET, ERR-PD-01). 2 VV còn lại SUCCESS. **UI**: Toast warning "Đã PD 2/3 VV. 1 VV gặp lỗi (đã được CB PD TW 02 duyệt trước đó)". **PERSIST**: AUDIT_LOG 2 PHE_DUYET (Tab1) + 1 PHE_DUYET (Tab2 từ trước). | Edge | P1 |

---

## Tổng kết file

**Tổng TC: 21** (3 UI + 5 Happy + 7 Negative + 6 Edge) — ổn định sau Codex review 2026-05-09

| Section | TC IDs | Count |
|---------|--------|------:|
| A. UI verification | PD-UI-01, PD-UI-02, PD-UI-03 | 3 |
| B. Happy | PD-101, PD-102, PD-103, PD-104, TB-105 | 5 |
| C. Negative | PD-201, 202, 203, 204, 205, 206, 207 | 7 |
| D. Edge | PD-301, PD-302, TB-303, TB-304, PD-305, PD-306 | 6 |

**Priority**: P0=11 / P1=10 / P2=0

> **Changelog 2026-05-06:**
> - **A3 base** — UI 3 + Happy 5 + Negative 7 + Edge 6 = 21 TC.
>
> **Codex review 2026-05-09:**
> - File coverage đã đầy đủ — 3 UC (UC61+UC62+UC63) + 7 ERR codes + 4 SPEC-CLARIFY + cycle test + BR-AUTH-05 + BR-FLOW-04 + batch action + 2 WARNING paths (SMTP/LGSP fail)
> - KHÔNG thêm TC mới — file là một trong những file mature nhất

**Coverage:**
- BR: BR-AUTH-01, **BR-AUTH-05 (cùng cấp — TC-204 explicit)**, BR-DATA-05, BR-EC-01 (TC-301/306), BR-FLOW-03, **BR-FLOW-04 (TU_CHOI → DANG_XU_LY KHÔNG TU_CHOI close — TC-103 explicit)**, BR-NOTIF-01 (TC-103 dual notify CB NV + NHT)
- Error codes: ERR-TR-01/02 (UC61), WRN-TB-01/02 (UC62), ERR-PD-01/02/03 (UC63) — **full coverage 3 UC, 7/7 errors + 2/2 warnings**
- AC SRS: 2/2 UC61 (srs-fr-05:884-886) + 2/2 UC62 (srs-fr-05:936-938) + 3/3 UC63 (srs-fr-05:995-998)
- Batch flow: TC-104 (uniform 5/5) + TC-207 (mixed state 3 valid + 2 reject) + TC-306 (concurrent batch lock)
- SPEC-CLARIFY: VV-TB-01 (UC62 trigger event), VV-TB-02 (retry policy interval/max), VV-PD-01 (ERR-PD-03 message cho <10 ký tự), VV-PD-02 (giới hạn cycle TU_CHOI ↔ TRINH lại)
