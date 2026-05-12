# Review — FR-15 CT HTPLDN test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:18:42

> File reviewed: `/Users/teamai/Downloads/antigravity/QA/skilkk/docs/todo-test/fr-15-ct-htpldn/test-plan.md` (377 dòng, v1.0).
> Cross-checked: `input/srs-v3/srs-fr-15-ct-htpldn.md` (1313 dòng) + `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` §`srs-fr-15-ct-htpldn.md` (lines 2508-2640).

## Gaps

- **[Critical · header dòng 5-8] Phân nhóm C SAI — FR-15 thực tế là nhóm B (DELTA+IMPACT).** Test plan tuyên bố "KHÔNG có file SRS update v3.5 riêng cho FR-15". Thực tế CHANGELOG line 2508-2640 liệt kê **8 thay đổi nghiệp vụ** apply v3.5 cho FR-15 (A-ITEM-13, A-ITEM-09, B2d, 5×B1). Trong đó 5 thay đổi cấu trúc rõ rệt: rename module (Thay đổi 1), **re-numbering UC 164-172/195-196 → UC 160-170 contiguous** (Thay đổi 2), DOT_BAO_CAO thêm 5 audit fields + date type fix (Thay đổi 3), 6 lifecycle actions mới với sửa actor "Hoàn thành = CB PD" (Thay đổi 4), enum kỳ BC khớp TT17 (Thay đổi 7). Nhóm C "sample 18-22 TC" sẽ MISS regression nghiêm trọng.
- **[Critical · §1.2 bảng UC line 36-46] UC ID dùng numbering CŨ (164-172 + 195/196).** v3.5 CHANGELOG Thay đổi 2 đã ánh xạ UC164→UC160, UC165→UC161, ..., UC196→UC168, UC171→UC169, UC172→UC170. Test plan vẫn ghi UC164/195/196 — sẽ broken khi đối chiếu CSV transaction v1.1 hoặc dev SRS v3.5.
- **[Critical · §2.5 SM-KH-CTHTPL line 197-242] Transition Hoàn thành ghi actor "CB NV" — SAI v3.5.** CHANGELOG Thay đổi 4 Phần 2 sửa rõ: `DANG_THUC_HIEN → HOAN_THANH` trigger phải là **"CB PD hoàn thành"** với guard "Tất cả đợt BC đã hoàn thành" + Lỗi "Chỉ CB PD mới được hoàn thành". Bảng test plan line 240 vẫn ghi `CB NV` → bug ngược thẩm quyền.
- **[Critical · §2.5 SM line 242 + 197-225] Transition Rút trình SAI đích.** Test plan ghi `CHO_PHE_DUYET → HUY` (line 242). CHANGELOG Thay đổi 4 Phần 3 sửa rõ: rút trình về `DU_THAO` để sửa rồi trình lại, **KHÔNG về HUY**. ASCII diagram line 216 cũng vẽ sai cạnh.
- **[Important · §1.2 + §2.5] Thiếu 6 lifecycle actions Processing detail (`[GAP-XI-01]`).** v3.5 đã đặc tả đầy đủ 6 sub-section cho Kích hoạt/Tạm dừng/Tiếp tục/Hoàn thành/Hủy/Rút trình kèm Errors + Acceptance. Test plan §1.2 không có FR riêng cho 6 thao tác này (chỉ gộp vào FR-XI-01) → thiếu TC dedicated cho từng action + Errors mới.
- **[Important · §2.5 DOT_BAO_CAO entity] Thiếu test cho 5 audit fields + date type.** CHANGELOG Thay đổi 3 (`[SRS-FIX]`) yêu cầu DOT_BAO_CAO có `created_at/updated_at/created_by/updated_by/is_deleted` + 3 trường `han_nop/tu_ngay/den_ngay` đổi datetime→date. Test plan §1.2 / §2.4 không có TC verify schema/datepicker (không có giờ-phút) cho 3 trường này, không có TC verify audit fields ghi đúng người tạo/sửa.
- **[Important · §2.4 line 192-193] Hard-delete + Import Excel khẳng định "KHÔNG có" nhưng thiếu cite v3.5.** Test plan kết luận FR-15 giữ soft-delete v3 — đúng (CHANGELOG không có entry rename `la_cong_bo`/hard-delete cho FR-15). Tuy nhiên không cite line CHANGELOG cụ thể để chứng minh negative claim — cần thêm reference line 2585-2640 (8 thay đổi không bao gồm hard-delete + không bao gồm rename `la_cong_bo`→`cong_khai`).
- **[Important · §2.1 BR-XI-CT-STATE-DOT line 87] Cite thiếu Thay đổi 1 ITEM-13.** Module đổi tên "Quản lý kế hoạch thực hiện CT HTPLDN" (A-ITEM-13). Breadcrumb SCR-XI-01 + Tiêu đề trang phải verify đổi tên. §2.4 Breadcrumb line 149 vẫn ghi "CT HTPLDN > Quản lý chương trình" — chưa đồng bộ v3.5.
- **[Important · §2.1 BR `la_cong_bo` line 91] SPEC-CLARIFY rename quá nhẹ.** Test plan đặt SPEC-CLARIFY nhưng CHANGELOG line 2585-2640 KHÔNG list FR-15 rename `la_cong_bo`→`cong_khai`. Verdict đáng lẽ phải dứt khoát: **giữ `la_cong_bo` cho FR-15 entity CHUONG_TRINH_HTPL trong v3.5** (chỉ BIEU_MAU/HOI_DAP/VU_VIEC/etc rename). Test plan đang để mơ hồ → tester sau có thể log bug oan.
- **[Important · §2.6 enum ky_bao_cao] BAO_CAO_CT_HTPL enum mới `SO_BO_6_THANG/SO_BO_NAM/TRON_NAM` không xuất hiện trong test plan.** CHANGELOG Thay đổi 7 (`[GAP-XI-02]`) chốt enum mới. Test plan §1.2 TC-07 "Lập BC 21a/21b" không liệt kê verify dropdown kỳ BC + reject giá trị enum cũ (THANG/QUY/NAM/TONG_KET).
- **[Suggestion · §4 priority] 46 TC tự đánh giá P0=22/P1=18/P2=6 không trace UC↔TC.** Bảng line 326-338 gộp tổng theo file; thiếu mapping 1:1 TC↔UC↔FR-XI để verify cover hết 11 FR.
- **[Suggestion · §1.3 line 60] Account NHT/CG `huongcg` mismatch convention.** Convention `_01/_02/_03` không có `huongcg` (xem `qa_htpldn_accounts_convention`). Cần đổi `nht_01`/`tvv_01` hoặc thêm cite CSV row.

## Suggestions

- Đổi phân nhóm header sang **Nhóm B — DELTA+IMPACT** + ghi rõ 8 thay đổi v3.5 từ CHANGELOG line 2508-2640. Re-scope: test full UC re-numbered (10 UC) + DOT_BAO_CAO audit fields + 6 lifecycle actions + enum kỳ BC + đổi tên module; sample happy path cho phần KHÔNG đổi.
- Cập nhật bảng §1.2 UC theo ánh xạ v3.5 (UC164→UC160 ... UC172→UC170). Giữ comment "v3 cũ: UC164" sau dấu `~~` để trace.
- Bổ sung 1 file TC riêng `12-TC-lifecycle-actions.md` cover 6 action Kích hoạt/Tạm dừng/Tiếp tục/Hoàn thành/Hủy/Rút trình theo `[GAP-XI-01]` — kèm permission check (Hoàn thành = CB PD).
- Bổ sung 1 file TC riêng `13-TC-dot-bc-audit-fields.md` verify `created_at/updated_at/created_by/updated_by/is_deleted` ghi đúng + verify datepicker chỉ ngày (không giờ phút) cho `han_nop/tu_ngay/den_ngay`.
- Sửa §2.5 bảng transition: actor Hoàn thành = "CB PD" + Rút trình `CHO_PHE_DUYET → DU_THAO` (không phải HUY). Vẽ lại ASCII line 197-225.
- §2.1 line 91 thay SPEC-CLARIFY bằng kết luận chắc chắn: "FR-15 GIỮ `la_cong_bo` v3 — CHANGELOG line 2585-2640 không list rename." Cite line.
- §1.2 + §2.6 thêm TC verify enum kỳ BC mới (3 giá trị TT17) + negative test gửi enum cũ → ERR validate.
- §2.4 line 149 cập nhật Breadcrumb "Quản lý kế hoạch thực hiện CT HTPLDN" theo Thay đổi 1.
- Thêm trace matrix UC↔TC↔file ở phần đầu §3 hoặc §4 — verify cover hết 10 UC v3.5 (UC160-UC170, trừ UC163 Phê duyệt CT đã có TC-04 → đảm bảo không miss UC nào).
- §1.3 thay `huongcg` bằng username convention `_01/_02/_03` từ `input/users.csv`, hoặc thêm cite row CSV cụ thể.

## Verdict

**REVISE (REQUEST CHANGES).** Test plan có structure tốt (GĐ1/GĐ2 split rõ, BR table chi tiết, SM diagram + transition đầy đủ) nhưng **phân loại nhóm SRS sai cốt lõi** (gán nhóm C IMPACT-only, thực tế là nhóm B DELTA+IMPACT có 8 thay đổi v3.5). Hệ quả: 2 transition SM-KH-CTHTPL ghi sai (Hoàn thành actor + Rút trình đích), UC numbering toàn bảng dùng range cũ 164-172/195-196 thay vì 160-170 v3.5, DOT_BAO_CAO audit fields + datepicker không test, 6 lifecycle actions mới không cover dedicated. Cần edit lại §header + §1.2 + §2.5 + bổ sung 2 file TC mới trước khi execute round QA. Phần làm tốt: BR table cite line SRS đầy đủ, permission matrix split TW/BN/ĐP theo BR-AUTH-05 chính xác, §5 có rule "CẤM kết luận" tránh false negative dropdown rỗng.
