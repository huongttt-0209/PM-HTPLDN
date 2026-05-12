# Review — FR-02 Hỏi đáp test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:42:00

## Gaps

- **State machine bỏ sót `DA_PHAN_CONG`** (Critical). Test plan §2.5 SM table liệt kê 9 trạng thái nhưng KHÔNG có `DA_PHAN_CONG`, trong khi SRS `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:474,498,502,509,511` ghi rõ FR-II-06 Step 9 set `trang_thai = DA_PHAN_CONG` và Outputs row 5 = `'DA_PHAN_CONG'`. Bảng transition test plan lại đi thẳng `TIEP_NHAN → DANG_XU_LY` qua "phân công" — sai SM thực tế. Nếu BA chốt bỏ DA_PHAN_CONG khỏi SM-HOIDAP v3.5, cần QUOTE line SRS xác nhận; nếu không → phải bổ sung trạng thái 10 + transition `TIEP_NHAN → DA_PHAN_CONG → DANG_XU_LY`.
- **"Auto-filter 4 tiêu chí FR-II-06 Step 5" thiếu nguồn SRS gốc** (Critical). Test plan §1.2 + §2.4 SCR-II-03 + §4 ghi `workload ASC + ho_ten ASC LIMIT 10` cite `02-thu-tu-module.md:86,116,138,370` nhưng **FR-II-06 Step 5 trong SRS chính** (`srs-update-2026-5-5/srs-fr-02-hoi-dap.md:470-473`) chỉ mô tả "Tải danh sách gợi ý...khớp lĩnh vực" — KHÔNG có thứ tự sort/LIMIT. Cite duy nhất ở `02-thu-tu-module.md` là **derived doc**, không phải SRS gốc. TC-PERM-AUTO-FILTER có thể đo sai expected. Cần BA confirm hoặc grep nguyên văn ở srs-update khác.
- **FR-II-NEW-01 status inconsistency** (Critical). Test plan §1.2 marks "**DEPRECATED Q11**" + dòng 213 "❌ KHÔNG có" nhưng SRS `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:449,829,1149,1174` VẪN tham chiếu FR-II-NEW-01 làm precondition + bảng phụ lục FR. Hai nguồn xung đột mà test plan chốt một chiều — phải BA confirm + cite line "xóa hẳn" mới đóng được TC.
- **Auto-tạo bản ghi FR-13 Kho QA — không cite SRS field-level** (Important). §1.1 + §2.5 transition `CHO_PHE_DUYET → DA_DUYET` ghi "auto-tạo bản ghi FR-13 Kho QA `nguon=TU_DONG`" nhưng chỉ cite `01-tong-quan-nghiep-vu.md:87-97`. SRS FR-II-08 Processing (line 617) chỉ ghi "Cập nhật trạng thái = DA_DUYET, người duyệt, ngày duyệt" — KHÔNG có step "INSERT INTO KHO_QA". Thiếu cite SRS field-level `kho_qa.nguon`, field map FR-13 source, contract API → TC-XMOD-FR13-KHO-QA expected behavior chưa định nghĩa được. Cần grep SRS FR-13 module.
- **BR-SLA-02 2 mức vs 4 mức conflict — chưa defer rõ ràng** (Important). §2.1 ghi "BA Q5 đề xuất BỎ Quá hạn nghiêm trọng — đang theo SRS hiện tại còn 4 mức" và TC-SLA-LEVEL-01..04 test 4 mức. Nhưng `02-thu-tu-module.md:114` đã chốt SCR-VIII-06 chỉ còn 2 ngưỡng (`canh_bao_muc_1` + `canh_bao_muc_2`). Test 4 mức trong khi cấu hình UI chỉ 2 ngưỡng → TC-SLA-LEVEL-03/04 sẽ FAIL hoặc 🤷. Phải pick nhóm "C — Chờ BA confirm spec" trong Bảng 2 ngay từ test plan, không để tester gặp giờ chạy mới ngỡ ngàng.
- **Hủy công khai → DA_DUYET test coverage không thấy TC riêng** (Important). §4 phân bổ scenario chỉ có "CR-01 5 trường công khai: 6 TC (TC-WF-PUBLISH-FIELDS, TC-WF-UNPUBLISH-FIELDS)" gộp PUBLISH + UNPUBLISH. SRS line 658 nói rõ Hủy CK phải `set thoi_gian_dang_tai = NULL` + `cong_khai=0` + giữ 4 trường còn lại — cần TC riêng verify field-level state sau hủy CK + TC ERR-PD-06 API gỡ Cổng PLQG fail. Tổng `08-TC-phe-duyet-cong-khai.md` = 16 TC cover 6 flow (Duyệt/Từ chối/CK/Hủy CK/Đóng/Batch) → mỗi flow trung bình 2.6 TC, mỏng.
- **TC count cho file 12 SLA hơi mỏng** (Important). §4 ghi 12-TC-sla-canh-bao = 6 TC (2 happy + 1 neg + 3 edge) cover 4 mức cảnh báo + tác vụ tự động 30 phút + 4 BR (BR-SLA-01..04) + ngày làm việc trừ ngày lễ FR-VIII-29. 4 mức × 1 TC = 4 TC đã chiếm hết, không còn TC cho cron 30 phút trigger/skip, BR-SLA-03 notification, BR-SLA-04 ngày lễ + nghỉ bù. Đề xuất bump lên 9-10 TC.
- **BR-FLOW-02 batch reject ambiguity** (Important). §2.1 ghi BR-FLOW-02 ngoại lệ "Từ chối phải từng bản ghi (yêu cầu lý do)" + §2.4 dòng 215 "❌ Từ chối hàng loạt batch". Nhưng §4 TC-WF-BATCH-01..03 chỉ liệt kê batch approve, không có TC negative "Batch reject blocked" verify UI ẩn nút Batch Reject. Thiếu enforcement TC.
- **TVN_BRIDGE cross-module cover yếu** (Important). §1.1 + transition `[*] → MOI` đề cập kênh TVN_BRIDGE + FK `tu_van_nhanh_goc_id` nhưng §4 chỉ 1 TC TC-XMOD-TVN-BRIDGE trong nhóm "Cross-module (5 TC)". SRS line 170 + 1046 yêu cầu badge click → tooltip phiên gốc + cán bộ thấy được lịch sử trao đổi gốc — cần ít nhất 3 TC: (1) inbound từ FR-13 → MOI có đủ FK, (2) click badge mở lịch sử FR-13, (3) cán bộ KHÔNG nhập tay được TVN_BRIDGE trong dropdown form (verify line 1071).
- **EC-PUBLISH-API-FAIL idempotency key chưa cụ thể** (Important). §4 scenario "BR-FLOW-05 API Cổng PLQG + idempotency: 5 TC" nhưng SRS line 637 nói "Dùng idempotency key để tránh duplicate khi retry". TC test idempotency phải có scenario double-click + retry sau timeout — không thấy spelled out. Cũng thiếu TC scheduled job 5 phút detect bản ghi trung gian (`srs-update:1532`) retry crash recovery.
- **Permission matrix dòng "Xóa" có thể vượt scope SRS** (Suggestion). §2.3 cho QTHT cột "Xóa" = "—" nhưng row "Đóng hồ sơ" = "force-only (audit)". SRS line 1530 + BR-FLOW-03 cho QTHT force-edit (audit đặc biệt) — cần TC riêng verify QTHT force path tạo audit special.
- **Account list thiếu CB_PD_BN_03 / CB_PD_DP_03 cho permission fallback** (Suggestion). §1.3 chỉ liệt `cb_pd_bn_01`/`_02` + `cb_pd_dp_01`/`_02`, không có `_03`. Rule 7 fallback cần ≥3 siblings cùng role+cấp khi `_01` lock. Đối chiếu users.csv để xác nhận có suffix `_03` không.

## Suggestions

- Bổ sung 1 bảng "FR-II-NEW-01 final status" đầu §2.1 với 3 cột (SRS file line cite | Test plan stance | BA confirmation status) — rõ ràng inconsistency trước khi tester chạy.
- Thêm cột "Test method" vào §4 (UI / API / Cron simulation / Time-travel) — TC SLA 30 phút + TC BR-FLOW-06 "6 tháng không click Đóng hồ sơ" cần đánh dấu method "Time-travel manipulation DB ngay_tiep_nhan" vì không thể chạy realtime.
- Bổ sung TC test `tu_van_nhanh_goc_id` FK integrity khi xóa phiên FR-13 gốc — orphan handling.
- Bump 12-TC-sla-canh-bao lên 9-10 TC: tách 4 mức × 1 TC + 2 TC cron 30 phút (trigger + skip ngoài giờ làm việc) + 1 TC BR-SLA-04 ngày lễ + 1 TC BR-SLA-03 notification toggle.
- Bổ sung TC "Hủy CK → DA_DUYET field reset" riêng (verify `thoi_gian_dang_tai = NULL`, 4 trường công khai còn lại giữ giá trị, không re-upload khi CK lại) — cite SRS line 658.
- Đề xuất gộp TC-PERM-PUBLISH-CB-NV-BLOCKED + TC-PERM-04 + TC-PERM-05 thành matrix 6 ô (CB_NV × {Công khai, Hủy CK, Phê duyệt}) trong 13-TC-permission — hiện đang tản mác.
- Cite `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:1532` (scheduled job 5 phút crash recovery) ngay trong §2.5 transition table để TC crash recovery có anchor SRS.
- Thêm TC negative "Xóa bản ghi đã từng CK (sau khi Hủy CK về DA_DUYET) vẫn fail" — SRS line 119 quote rõ rule lưu vết. TC này tách khỏi BR-FLOW-03 base TC.
- Đề xuất define rõ Bảng 2 "TC chưa chạy được" template ngay trong §5 — gom sẵn 4 TC defer khả năng cao: TC-SLA-LEVEL-04 (Quá hạn nghiêm trọng, chờ BA), TC-EC-NO-AUTOCLOSE 6 tháng (cost cao, defer hoặc time-travel), TC-PERM-AUTO-FILTER (chờ BA confirm SRS), TC-XMOD-FR13-KHO-QA (chờ grep SRS FR-13).
- Đổi cite §2.1 BR-FLOW-01 "line 559-562" sang range chính xác (file dài 1652 dòng, BR statement chính ở line 1596-1600, processing step ở line 560-583) — hiện cite không khớp khi mở file.

## Verdict

**REVISE.** Test plan structure tốt (BR table 28 row, permission matrix 11×13, SM chi tiết, scenario class breakdown), nhưng 3 vấn đề Critical chặn approve:

1. SM bỏ sót `DA_PHAN_CONG` — sai SRS Output FR-II-06 (line 498) → mọi TC chạm "Phân công" sẽ fail.
2. Auto-filter 4 tiêu chí chỉ cite derived doc `02-thu-tu-module.md`, không cite SRS gốc → expected behavior TC-PERM-AUTO-FILTER chưa verified.
3. FR-II-NEW-01 status xung đột nội tại SRS update (line 449 dùng làm precondition, line 1149/1174 vẫn list FR) — test plan đơn phương chốt DEPRECATED chưa đủ thuyết phục để skip.

Sau khi fix 3 Critical + bổ sung Bảng 2 defer + bump SLA TC count → re-review để APPROVE.
