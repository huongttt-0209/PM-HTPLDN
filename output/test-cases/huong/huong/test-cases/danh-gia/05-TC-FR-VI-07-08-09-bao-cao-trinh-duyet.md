# TC FR-VI-07 + FR-VI-08 + FR-VI-09 — Lập BC (UC89) + Trình BC (UC90) + Duyệt BC (UC91) — Tab 4

> **SRS:** [`srs-fr-08-danh-gia.-v3.1.md`](../../../input/srs-v3/srs-fr-08-danh-gia.-v3.1.md) §FR-VI-07 (line 515-598) + §FR-VI-08 (line 602-662) + §FR-VI-09 (line 666-737) + §3 Tab 4 (line 864-875)
> **SCR:** SCR-VI-01 — Tab 4 Báo cáo + Action buttons phê duyệt BC
> **Actor:** CB NV (lập + trình BC) + CB PD (duyệt BC + từ chối BC)
> **Entity:** BAO_CAO_DANH_GIA (1:1 KE_HOACH, mẫu 21a/21b TT17/2025)
> **BR core:** BR-AUTH-05 (cùng cấp duyệt) + BR-FLOW-04 (lý do từ chối ≥10) + BR-NOTIF-01
> **SM transitions:** BAO_CAO → CHO_PHE_DUYET, CHO_PHE_DUYET → HOAN_THANH, CHO_PHE_DUYET → BAO_CAO
> **Total TC:** 14

---

## Test Cases

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-BC-001 | Mở Tab Báo cáo — auto tổng hợp 13 cột TT17 | Login `cb_nv_tw_01`. Đợt BAO_CAO (sau Hoàn tất chấm điểm). | 1. Mở chi tiết đợt<br>2. Tab "Báo cáo" | Tab hiển thị KPI cards + bảng tổng hợp + biểu đồ Radar/Bar + 13 cột BC theo template TT17 (auto fill từ system: TVV, KH tập huấn, hội nghị, VB, HS, KP TVPL) | Critical | UC89 process step 4, SCR row #46-48 |
| TC-DG-BC-002 | Auto fill — Số TVV / Số HS chi trả từ FR-04/FR-06 | Login. Đợt scope TW. | 1. Verify cột "Số TVV" và "Số HS giải quyết" | Cột 1 = đếm TVV active scope đơn vị. Cột 7 = đếm HS_CHI_TRA `DA_THANH_TOAN`. Khớp DB | High | UC89 13 cột table |
| TC-DG-BC-003 | Nhập kp_hoat_dong_khac (>=0) | Login. | 1. Nhập field `kp_hoat_dong_khac = 50,000,000`<br>2. Click [Lưu] | Lưu OK. Field định dạng money. Validate >= 0 | Medium | UC89 input #2 |
| TC-DG-BC-004 | Nhập kp_xa_hoi_hoa (>=0, validate âm) | Login. | 1. Nhập `kp_xa_hoi_hoa = -1000` | Inline error "Phải >= 0" | Medium | UC89 input #3 |
| TC-DG-BC-005 | Rich-text nhận xét tổng thể + kiến nghị | Login. | 1. Nhập rich text vào nhan_xet_tong_the (bold/italic/list)<br>2. Nhập kien_nghi<br>3. Lưu | Lưu OK. Rich-text format giữ nguyên | Medium | UC89 input #4-5 |
| TC-DG-BC-006 | Trình BC — happy path | Login `cb_nv_tw_01`. Đợt BAO_CAO + BC đầy đủ. | 1. Click [Trình duyệt BC]<br>2. Confirm | State BAO_CAO → CHO_PHE_DUYET. Toast success. BR-NOTIF-01 fire CB PD TW | Critical | UC90 happy, SM-DANHGIA #7, BR-NOTIF-01 |
| TC-DG-BC-007 | Trình BC — BC thiếu dữ liệu → WRN-DG-TR-01 (P0 F-004) | Login. nhan_xet_tong_the trống. | 1. Click [Trình duyệt BC] | Hiển thị WRN-DG-TR-01 NGUYÊN VĂN "Báo cáo thiếu thông tin: Nhận xét tổng thể" (chỉ WARNING, không phải ERROR). Hành vi xác định: cho phép trình sau khi user xác nhận | Medium | WRN-DG-TR-01 (FR-VI-08 E2 severity=WARNING) |
| TC-DG-BC-008 | CB PD duyệt BC — happy path | Login `cb_pd_tw_01`. Đợt CHO_PHE_DUYET. | 1. Mở chi tiết đợt<br>2. Tab Báo cáo<br>3. Click [Phê duyệt BC]<br>4. Confirm | State CHO_PHE_DUYET → HOAN_THANH. Auto-fill người duyệt + thời gian. Hiển thị màn kết quả: trạng thái + người duyệt + thời gian. BR-NOTIF-01 fire CB NV | Critical | UC91 happy, SM-DANHGIA #8, BR-AUTH-05, BR-NOTIF-01, AC §UC91 step 4 |
| TC-DG-BC-009 | CB PD từ chối BC — lý do bắt buộc ≥10 ký tự | Login `cb_pd_tw_01`. CHO_PHE_DUYET. | 1. Click [Từ chối BC]<br>2. Lý do "Sai" (4 ký tự)<br>3. Submit | Block + ERR-DG-PD-04 "Vui lòng nhập lý do từ chối (tối thiểu 10 ký tự)" | High | ERR-DG-PD-04, BR-FLOW-04 |
| TC-DG-BC-010 | CB PD từ chối BC — happy path | Login `cb_pd_tw_01`. | 1. [Từ chối BC]<br>2. Lý do "BC thiếu phần kiến nghị, vui lòng bổ sung"<br>3. Submit | State CHO_PHE_DUYET → BAO_CAO. Lý do lưu. BR-NOTIF-01 fire CB NV. CB NV thấy lý do trên Tab 4 | Critical | UC91 reject, SM-DANHGIA #9, BR-FLOW-04, BR-NOTIF-01 |
| TC-DG-BC-011 | BR-AUTH-05 — CB PD BN không duyệt được BC TW | Login `cb_pd_bn_01`. Đợt CHO_PHE_DUYET scope TW. | 1. Truy cập URL chi tiết đợt | 403 hoặc nút Phê duyệt ẩn. Force URL → "Bạn không có quyền duyệt đợt cấp này" | High | BR-AUTH-05, BR-AUTH-08 |
| TC-DG-BC-012 | Xuất XLSX theo mẫu 21a/21b TT17/2025 | Login `cb_nv_tw_01`. Đợt HOAN_THANH. | 1. Click [Xuất XLSX] | Tải `.xlsx`. Tên file format `BC-DG-{ma_dot}-{timestamp}.xlsx`. Nội dung 13 cột TT17 đúng | High | SCR row #53, FR-VI-07 output #2 |
| TC-DG-BC-013 | Xuất DOCX theo mẫu 21a/21b TT17/2025 | Login. | 1. Click [Xuất DOCX] | Tải `.docx`. Header tên đợt + kỳ + đơn vị. Bảng tổng hợp + nhận xét | Medium | SCR row #53 |
| TC-DG-BC-014 | Cycle đầy đủ — Trình → Từ chối → Sửa → Trình lại → Duyệt → HOAN_THANH | Login. Đợt BAO_CAO. | 1. cb_nv: Trình → CHO_PHE_DUYET<br>2. cb_pd: Từ chối → BAO_CAO<br>3. cb_nv: Sửa BC + Trình lại → CHO_PHE_DUYET<br>4. cb_pd: Duyệt → HOAN_THANH | Chuỗi state đúng. AUDIT_LOG có 4 entries. BR-NOTIF-01 fire 4 lần. Đợt cuối ở HOAN_THANH | High | Cycle BR-AUTH-05 + BR-FLOW-04 |

---

## Edge bổ sung (A4 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-BC-015 | Boundary lý do từ chối BC = 10 ký tự | Login. CHO_PHE_DUYET. | 1. Lý do "1234567890" | Cho phép từ chối | Medium | BR-FLOW-04 boundary |
| TC-DG-BC-016 | Boundary lý do = 9 ký tự → block | Login. | 1. Lý do "123456789" | Block + ERR-DG-PD-04 | Medium | BR-FLOW-04 |
| TC-DG-BC-017 | Boundary `kp_hoat_dong_khac` = 0 (allowed) | Login. | 1. Nhập = 0 | Lưu OK | Low | UC89 input #2 >=0 |
| TC-DG-BC-018 | `kp_xa_hoi_hoa` very large 999,999,999,999 | Login. | 1. Nhập 999tỷ | Lưu OK (số nguyên 12 chữ số) | Low | UC89 input #3 |
| TC-DG-BC-019 | `mau_bao_cao` enum MAU_21A vs MAU_21B | Login. | 1. Chọn dropdown mẫu | 2 option: MAU_21A (sơ bộ 6 tháng) / MAU_21B (tròn năm) | Medium | BAO_CAO_DANH_GIA col #8 |
| TC-DG-BC-020 | Auto chọn `mau_bao_cao` theo `tan_suat` | Login. tan_suat=SO_BO_6_THANG. | 1. Mở Tab BC | mau_bao_cao default = MAU_21A | Low | SPEC-CLARIFY-DG-04 (BA xác nhận mapping) |
| TC-DG-BC-021 | Xuất XLSX khi đợt chưa HOAN_THANH | Login. Đợt BAO_CAO. | 1. Click [Xuất XLSX] | Tải OK với watermark "DỰ THẢO" hoặc cho phép thường (per BA decision) | Low | SPEC-CLARIFY-DG-05 |
| TC-DG-BC-022 | Trình BC khi BC trống hoàn toàn → WRN-DG-TR-01 (P0 F-004) | Login. BC chưa nhập gì. | 1. Click [Trình duyệt BC] | WRN-DG-TR-01 NGUYÊN VĂN "Báo cáo thiếu thông tin: {danh sách trường}" (Severity = WARNING). Cho phép confirm trình per spec FR-VI-08 E2. KHÔNG dùng ERR-DG-TR-01 (dành riêng cho sai state) | Medium | WRN-DG-TR-01 (FR-VI-08 E2) |
| TC-DG-BC-023 | Common Approval Fields — người duyệt + thời gian + lý do (P1 F-019) | Login. Đợt HOAN_THANH. | 1. Mở chi tiết đợt → tab BC | Hiển thị per FR-VI-09 Outputs #3: trạng thái + người duyệt (nguoi_duyet=cb_pd_tw_01) + thời gian + lý do (nếu từ chối). KHÔNG yêu cầu ip_dia_chi (không có trong SRS) | Medium | FR-VI-09 Outputs #3, AC §UC91 step 4 |
| TC-DG-BC-024 | Cycle nhiều lần Từ chối liên tục — không auto-cancel | Login. CHO_PHE_DUYET. | 1. Từ chối 3 lần liên tiếp | State quay BAO_CAO 3 lần. KHÔNG auto chuyển HUY | Low | SM-DANHGIA |

## Fill GAP A5 (A6 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-BC-025 | Hủy đợt từ BAO_CAO → HUY (GAP-A5-03) | Login `cb_nv_tw_01`. Đợt BAO_CAO. | 1. [Hủy đợt]<br>2. Lý do "Số liệu BC sai, hủy lập lại"<br>3. Confirm | State BAO_CAO → HUY. BC giữ trạng thái (soft delete) | High | SM-DANHGIA #13 |
| TC-DG-BC-026 | Lập BC khi đợt KHÔNG ở BAO_CAO → ERR-DG-BC-01 (GAP-A5-06) | Login. Đợt THUC_HIEN. | 1. Mở Tab Báo cáo (force) | Tab disabled HOẶC API trả ERR-DG-BC-01 "Đợt chưa hoàn thành đánh giá" | High | ERR-DG-BC-01 |
| TC-DG-BC-027 | Trình BC khi state != BAO_CAO → ERR-DG-TR-01 (GAP-A5-07) | Login. Đợt LAP_KE_HOACH. | 1. Force trigger trình BC qua URL | API trả ERR-DG-TR-01 "Đợt không ở trạng thái đã lập BC" | Medium | ERR-DG-TR-01 |
| TC-DG-BC-028 | Duyệt BC khi state != CHO_PHE_DUYET → ERR-DG-PD-03 (GAP-A5-08) | Login `cb_pd_tw_01`. Đợt BAO_CAO (chưa trình). | 1. Force trigger phê duyệt qua URL/API | ERR-DG-PD-03 "Đợt không ở trạng thái chờ duyệt BC". Nút [Phê duyệt BC] cũng ẩn trong UI | Medium | ERR-DG-PD-03 |
| TC-DG-BC-029 | DELETE / Cancel BAO_CAO_DANH_GIA — verify spec (GAP-A5-10) | Login. | 1. Tìm action xóa BC | Spec UC89/90/91 KHÔNG đặc tả DELETE BC explicit. Workflow: Reject → BAO_CAO (BC giữ + sửa). KHÔNG có nút xóa BC standalone. Verify UI absent | Low | SPEC-CLARIFY-DG-07 (BA xác nhận BC chỉ soft-delete khi đợt HUY?) |

## Codex Review apply (2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-BC-030 | Auto fill 13 cột BC TT17 — verify cột 2-6 + 8-13 (P1 F-016) | Login. Đợt BAO_CAO. Seed: 2 KHOA_HOC tập huấn + 1 hội nghị + 3 VV trả lời UBND + 2 VV TV mạng lưới + 5 HSCT (3 DN vừa, 1 DN nhỏ, 1 DN siêu nhỏ) trong kỳ. | 1. Mở Tab BC<br>2. Verify từng cột | Cột 2 = 2 (tập huấn), Cột 3 = 1 (hội nghị), Cột 4 = 3 (VB UBND), Cột 5 = 2 (VB TV mạng lưới), Cột 6 = 5 (HS tiếp nhận), Cột 8 = 3 (DN vừa), Cột 9 = 1 (DN nhỏ), Cột 10 = 1 (DN siêu nhỏ), Cột 11 = SUM(số tiền thực trả), Cột 12 = giá trị nhập tay, Cột 13 = giá trị nhập tay | High | FR-VI-07 Bảng "Các cột chính BC" 13 cột |
| TC-DG-BC-031 | Force submit `quyet_dinh` invalid enum — Duyệt BC (P1 F-012) | Login `cb_pd_tw_01`. CHO_PHE_DUYET. | 1. Force POST `/api/danh-gia/duyet-bc` body `quyet_dinh = "MAYBE"` | 400/422 + lỗi enum constraint per FR-VI-09 input #2 (`DUYET / TU_CHOI`) | High | FR-VI-09 input #2 enum, security |
| TC-DG-BC-032 | Rich-text BC — boundary 100KB + XSS sanitize (P2 F-029) | Login. | 1. Nhập nhan_xet_tong_the 100KB rich-text<br>2. Nhập kien_nghi với `<script>alert(1)</script>` payload<br>3. Save | Boundary: lưu OK hoặc reject với inline error nếu > giới hạn. XSS: HTML escape — text hiển thị literal, KHÔNG execute script | High | FR-VI-07 input #4-5, Security baseline |

## Tổng số TC: 32 (14 base + 10 edge A4 + 5 fill A6 + 3 Codex apply)

> **SPEC-CLARIFY-DG-07:** BAO_CAO_DANH_GIA — chỉ soft-delete khi parent KH HUY hay có DELETE action riêng? — pending BA.

> **A4 done 2026-05-10** — 10 TC mới merge inline.
> **A6 placeholder — Fill GAP-A5.**
> **A7 placeholder — LOẠI/SỬA log.**
> **SPEC-CLARIFY-DG-04:** Auto-mapping `mau_bao_cao` theo `tan_suat` — pending BA.
> **SPEC-CLARIFY-DG-05:** Cho phép xuất BC khi đợt chưa HOAN_THANH? — pending BA.
> **SPEC-CLARIFY-DG-06:** Trình BC trống hoàn toàn — block hay cảnh báo? — pending BA.
