# Test Cases — FR-IV-NEW-02 + FR-IV-NEW-04: Cập nhật trạng thái + Phê duyệt Tổ chức TV

> **SRS Ref**: FR-IV-NEW-02 + FR-IV-NEW-04, SCR-IV-NEW-01/03, Entity TO_CHUC_TU_VAN, SM-TCTV (full transitions)
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:1019-1075 + 1190-1257`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TCPD-UI-01 | FR-IV-NEW-04 / SCR-IV-NEW-03 / UI 3 nút action | Verify SCR-IV-NEW-03 có 3 nút action header (Trình duyệt / Phê duyệt / Từ chối) | cb_nv_tw_01 + cb_pd_tw_01 | TC-TW-002 mỗi state | 1. Mở chi tiết theo state<br>2. Verify action header | **MOI_DANG_KY**: nút "Trình duyệt" (chỉ CB NV); KHÔNG có Phê duyệt/Từ chối<br>**CHO_PHE_DUYET**: nút "Phê duyệt" + "Từ chối" (chỉ CB PD cùng cấp); CB NV không thấy<br>**HOAT_DONG**: nút "Tạm dừng" + "Vô hiệu hóa" + "Công khai/Hủy"<br>**TU_CHOI**: nút "Sửa rồi trình lại" (chỉ CB NV)<br>**VO_HIEU_HOA**: nút "Khôi phục" | Happy 🔴 |

## B. SM-TCTV transitions (FR-IV-NEW-02)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TCPD-001 | FR-IV-NEW-01 / MOI_DANG_KY → CHO_PHE_DUYET | Trình duyệt TC TV | cb_nv_tw_01, TC-TW-100 MOI_DANG_KY | — | 1. Click "Trình duyệt" → MD-TRINH-DUYET<br>2. Confirm | TO_CHUC_TU_VAN.trang_thai=CHO_PHE_DUYET; AUDIT_LOG; Notification cb_pd_tw_01 cùng cấp | Happy 🔴 |
| TC-TCPD-002 | FR-IV-NEW-02 / HOAT_DONG → TAM_DUNG | Tạm dừng TC TV | cb_nv_tw_01, TC-TW-101 HOAT_DONG | ly_do: "Tạm dừng do tổ chức xin nghỉ" | 1. Click "Tạm dừng"<br>2. Nhập lý do<br>3. Confirm | TO_CHUC_TU_VAN.trang_thai=TAM_DUNG; AUDIT_LOG; ERR-TT-TC-03 nếu thiếu lý do | Happy 🟡 |
| TC-TCPD-003 | FR-IV-NEW-02 / HOAT_DONG → VO_HIEU_HOA + GUARD | TC TV không có TVV liên kết → vô hiệu hóa OK | cb_nv_tw_01, TC-TW-102 HOAT_DONG, TVV_TO_CHUC count HOAT_DONG = 0 | ly_do: "Hết hạn hoạt động" | 1. Click Vô hiệu hóa<br>2. Confirm | trang_thai=VO_HIEU_HOA; nếu cong_khai=1 → API DELETE Cổng (BR-PUBLIC-02) | Happy 🔴 |
| TC-TCPD-004 | FR-IV-NEW-02 / E2 ERR-TT-TC-02 GUARD | TC TV có TVV liên kết HOAT_DONG → reject | cb_nv_tw_01, TC-TW-103 HOAT_DONG, có 2 TVV liên kết HOAT_DONG | — | 1. Click Vô hiệu hóa | "Tổ chức đang có 2 tư vấn viên đang hoạt động liên kết, không thể vô hiệu hóa" (NGUYÊN VĂN ERR-TT-TC-02 với count substitution); KHÔNG cập nhật | Negative 🔴 |
| TC-TCPD-005 | FR-IV-NEW-02 / VO_HIEU_HOA → HOAT_DONG | Khôi phục TC TV | cb_nv_tw_01, TC-TW-104 VO_HIEU_HOA | — | 1. Click "Khôi phục" | trang_thai=HOAT_DONG; AUDIT_LOG | Happy 🟡 |
| TC-TCPD-006 | FR-IV-NEW-02 / E1 ERR-TT-TC-01 | Transition không hợp lệ MOI_DANG_KY → HOAT_DONG | cb_nv_tw_01 | DevTools API tamper | 1. Force API call | "Không thể chuyển từ Mới đăng ký sang Đang hoạt động" (NGUYÊN VĂN ERR-TT-TC-01) — phải qua phê duyệt | Negative 🔴 |

## C. FR-IV-NEW-04 — Phê duyệt TC TV

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TCPD-101 | FR-IV-NEW-04 / AC1+AC2 Happy | Phê duyệt TC TV cùng cấp | cb_pd_tw_01, TC-TW-100 CHO_PHE_DUYET (cb_nv_tw_01 tạo) | so_quyet_dinh: "QĐ-002/QĐ-TW", y_kien: "Đạt" | 1. Mở chi tiết TC-TW-100<br>2. Click Phê duyệt → MD-PHE-DUYET<br>3. Nhập Số QĐ<br>4. Confirm | **STATE**: TO_CHUC_TU_VAN.trang_thai=HOAT_DONG, ngay_cong_nhan=NOW, thoi_gian_duyet=NOW, nguoi_duyet=cb_pd_tw_01.id, so_quyet_dinh="QĐ-002/QĐ-TW", version+1; AUDIT_LOG; Notification cb_nv_tw_01<br>**UI**: Toast "Phê duyệt thành công, TC TV đã được công bố vào MLTV"<br>**PERSIST**: TC TV xuất hiện ở tab "Đang hoạt động", có thể được công khai (FR-IV-08) + nhận phân công VV | Happy 🔴 |
| TC-TCPD-102 | FR-IV-NEW-04 / E1 BR-AUTH-05 ERR-PD-TC-02 | CB PD khác cấp → ERR-PD-TC-02 | cb_pd_tw_01, TC-DP-001 CHO_PHE_DUYET (cb_nv_dp_01 tạo) | — | 1. Cố mở TC-DP-001 → Phê duyệt | API 403 "Chỉ phê duyệt Tổ chức tư vấn cùng cấp" (NGUYÊN VĂN ERR-PD-TC-02); UI ẩn nút Phê duyệt | Negative 🔴 |
| TC-TCPD-103 | FR-IV-NEW-04 / E2 ERR-PD-TC-03 từ chối thiếu lý do | Từ chối thiếu lý do → ERR-PD-TC-03 | cb_pd_tw_01 | ly_do: "" | 1. Submit Từ chối lý do trống | "Lý do từ chối là bắt buộc (≥10 ký tự)" (NGUYÊN VĂN ERR-PD-TC-03) | Negative 🟡 |
| TC-TCPD-104 | FR-IV-NEW-04 / E3 ERR-PD-TC-04 OptLock | 2 CB PD duyệt cùng lúc → optimistic lock | cb_pd_tw_01 + cb_pd_tw_02, TC-TW-105 version=0 | — | 1. 2 tab cùng phê duyệt<br>2. Submit lần 2 | Lần 2 nhận "Tổ chức tư vấn đã được duyệt bởi {cb_pd_tw_01} lúc {time}, vui lòng tải lại trang" (NGUYÊN VĂN ERR-PD-TC-04) | Negative 🔴 |
| TC-TCPD-105 | FR-IV-NEW-04 / E4 ERR-PD-TC-05 | Phê duyệt thiếu Số QĐ → ERR-PD-TC-05 | cb_pd_tw_01 | so_quyet_dinh: "" | 1. Submit Phê duyệt không số QĐ | "Số quyết định công bố là bắt buộc khi phê duyệt" (NGUYÊN VĂN ERR-PD-TC-05) | Negative 🟡 |
| TC-TCPD-106 | FR-IV-NEW-04 / TU_CHOI → CHO_PHE_DUYET sửa lại | CB NV sửa rồi trình lại sau từ chối | cb_nv_tw_01, TC-TW-106 TU_CHOI | sửa nguoi_dai_dien | 1. Mở chi tiết<br>2. Sửa<br>3. Click "Trình lại" | TO_CHUC_TU_VAN.trang_thai=CHO_PHE_DUYET (chuyển từ TU_CHOI); guard updated_at > thoi_gian_tu_choi; AUDIT_LOG | Happy 🟡 |

---

## D. EDGE bổ sung (A4 inline merge — 1 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TCPD-501 | EDGE-A4-d / Concurrent SM-TCTV transition | 2 user đồng thời Tạm dừng vs Vô hiệu hóa cùng TC TV | cb_nv_tw_01 + cb_nv_tw_02 cùng TC-TW-150 HOAT_DONG, version=0 | — | 1. 2 tab submit cùng lúc | Race: 1 win (version 0→1), 1 fail "Tổ chức tư vấn đã được cập nhật bởi {user} lúc {time}" — optimistic lock; SPEC-CLARIFY-CGTVV-18 nếu SRS không có version cho FR-IV-NEW-02 | Edge 🔴 |

---

## E. A6 fill gap (Traceability matrix forward — 4 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TCPD-601 | A6-FILL / FR-IV-NEW-04 / TU_CHOI explicit | CB PD từ chối TC TV với lý do ≥10 ký → TU_CHOI | cb_pd_tw_01, TC-TW-110 CHO_PHE_DUYET | quyet_dinh=TU_CHOI, ly_do="Hồ sơ chưa đầy đủ minh chứng pháp lý" | 1. Click Từ chối<br>2. Modal nhập lý do<br>3. Confirm | TO_CHUC_TU_VAN.trang_thai=TU_CHOI, thoi_gian_tu_choi=NOW, nguoi_tu_choi=cb_pd_tw_01.id, ly_do_tu_choi cập nhật, version+1; AUDIT_LOG; Notification cb_nv_tw_01 (người tạo) | Happy 🔴 |
| TC-TCPD-602 | A6-FILL / SM-TCTV TAM_DUNG → VO_HIEU_HOA + guard | TC TV TAM_DUNG vô hiệu hóa với guard | cb_nv_tw_01, TC-TW-111 TAM_DUNG, không có TVV liên kết HOAT_DONG | ly_do | 1. Click Vô hiệu hóa | trang_thai=VO_HIEU_HOA; AUDIT_LOG; nếu cong_khai=1 → tự gỡ Cổng | Happy 🟡 |
| TC-TCPD-603 | A6-FILL / SM-TCTV TAM_DUNG → HOAT_DONG explicit | Kích hoạt lại TC TV TAM_DUNG | cb_nv_tw_01, TC-TW-112 TAM_DUNG | — | 1. Click "Kích hoạt lại" | trang_thai=HOAT_DONG; AUDIT_LOG | Happy 🟡 |
| TC-TCPD-604 | A6-FILL / ERR-TT-TC-03 thiếu lý do | Cập nhật trạng thái TC TV thiếu lý do → ERR-TT-TC-03 | cb_nv_tw_01 | ly_do: "" | 1. Submit Tạm dừng/VO_HIEU_HOA không lý do | "Lý do thay đổi là bắt buộc (≥ 10 ký tự)" (NGUYÊN VĂN ERR-TT-TC-03) | Negative 🟡 |

---

**Tổng số TC**: 18 (1 UI + 6 SM + 6 PD + 1 Edge A4 + 4 A6 fill)
