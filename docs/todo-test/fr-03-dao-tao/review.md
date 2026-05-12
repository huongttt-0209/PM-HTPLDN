# Review — FR-03 Đào tạo test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:42:00

## Gaps

- **SM-KHOAHOC drift v3 vs v3.5 chưa giải quyết.** Test plan §2.5 nói "9 trạng thái giữ nguyên v3 (Thay đổi 3 OUT)" và liệt kê 8 state (DU_THAO/CHO_DUYET/DA_DUYET/DANG_DIEN_RA/DA_KET_THUC/CHO_DUYET_KQ/HOAN_THANH/HUY = 8) — đếm thiếu 1 state. `_DELTA-MAP-FR03.md:22` lại nói 11 trạng thái (TU_CHOI + TU_CHOI_KQ added Cách 2). SRS body `srs-fr-03-dao-tao.md:1806-1825` mermaid chỉ có 9 state, transition `CHO_DUYET → DU_THAO khi từ chối` (KHÔNG có TU_CHOI). Mâu thuẫn nội bộ 3 nguồn — phải chốt và đếm lại state list cụ thể, không "9" suông.

- **FR-III-21 "Phê duyệt khóa học" hoàn toàn miss.** `_DELTA-MAP-FR03.md:31` liệt FR-III-21 là FR mới (GAP-III-08 F-05). Test plan §1.1 nói "FR-III-01..20 + FR-III-NEW-01/02/03 + FR-III-22" (22 FR), bảng §1.2 có 24 dòng nhưng KHÔNG có FR-III-21. Bug transition CHO_DUYET → DA_DUYET cho khóa học (SRS line 1827 ghi "KHÔNG có FR riêng cover transition CHO_DUYET → DA_DUYET cho Khóa học") cần TC riêng cho FR-III-21 nếu dev quyết FR.

- **Junction KHOA_HOC_GIANG_VIEN.vai_tro override không có TC.** SRS line 1714, 1784-1798 (Thay đổi 13) quy định junction có `vai_tro` per-khóa override `GIANG_VIEN.loai`, và tab "Lịch sử giảng dạy" hồ sơ GV phải derive từ junction (KHÔNG từ `GIANG_VIEN.loai`). TC-GV-01..06 hiện chỉ cover CRUD entity, không có TC verify cùng 1 GV có thể là TRO_GIANG khóa A nhưng GIANG_VIEN khóa B + verify tab Lịch sử hiển thị đúng vai trò per khóa.

- **Cross-link FR-04 TVV `HOAT_DONG` → `KHOA_HOC.giang_vien_ids` không có TC.** Test plan §0 ambiguity note có nêu junction populate từ TU_VAN_VIEN (FR-04) qua KHOA_HOC_GIANG_VIEN, và §1.3 dependency Tier 3 ghi "GIANG_VIEN DANG_GIANG_DAY (≥1) + FR-04 TVV junction" — nhưng KHÔNG có TC verify dropdown chọn GV khi tạo khóa hiển thị cả GIANG_VIEN nội bộ FR-03 + TVV `HOAT_DONG` từ FR-04. Đây là tích hợp cross-module quan trọng do v3.5 đổi trạng thái TVV `DANG_HOAT_DONG → HOAT_DONG` (FR-04 rename), nếu BE FE còn enum cũ → dropdown rỗng.

- **BR-PUBLIC-01..03 (5 trường công khai) không có TC riêng.** SRS line 1916 áp BR-PUBLIC cho 4 entity nhóm III (KH năm + CTDT + KH + BAI_GIANG). Test plan §2.4 chỉ liệt cross-cutting checkbox "5 trường công khai", không có TC verify switch `cong_khai`, upload `anh_dai_dien`, `file_dinh_kem_cong_khai`, `mo_ta_cong_khai`, timestamp `thoi_gian_dang_tai`. Vẫn nhớ BUG-BM-005 hôm 2026-05-10 (toast công khai BAI_GIANG flaky) → cần TC dedicate cho 4 entity × switch on/off.

- **FR-III-19 hủy công bố KQ không có TC.** ERR-CB-KQ-04 (lý do <10 ký) và ERR-CB-KQ-05 (chưa công bố mà hủy) có trong §2.2 nhưng không TC nào ở §4.1 trigger. TC-KDT-12/13 chỉ cover công bố happy + ERR-CB-KQ-01. Negative TC hủy công bố thiếu.

- **BR-INTG-05 Cổng PLQG retry policy không có TC.** ERR-CB-KQ-03 + BR-INTG-05 (retry 3 lần backoff) áp cả FR-III-16 (công khai KH năm) lẫn FR-III-19 (đẩy KQ chuyên trang). Không TC nào verify retry 3 lần fail → alert QTHT. Nhóm F (lý do khác) khả năng cần mock sandbox Cổng PLQG; nếu env down phải mark BLOCKED nhóm D, không skip âm thầm.

- **HOC_VIEN entity riêng — TC seed account học viên qua TK DN/NHT không có.** §0 ambiguity ghi "HOC_VIEN entity riêng chưa cover trong SCR list — note nhân account học viên qua TK doanh nghiệp / NHT". `_DELTA-MAP-FR03.md:42` liệt HOC_VIEN là entity Mới owned 1:1 TAI_KHOAN qua `tai_khoan_id`. Không có TC verify khi DN đăng ký HV qua FR-III-04, hệ thống có auto-tạo TK + HOC_VIEN record link `tai_khoan_id` đúng hay không. TC-HV-01 chỉ test đăng ký DANG_KY_DAO_TAO.

- **TC-HV-05 "Điểm danh 2-value (boolean cũ) → reject hoặc tự động convert" mơ hồ.** SRS v3.5 nói enum 3-value `CO_MAT/VANG_PHEP/VANG_KHONG_PHEP` THAY THẾ boolean — KHÔNG có spec "fallback convert". TC verify "reject hoặc convert" là spec mâu thuẫn → STOP hỏi BA trước viết, không "verify SRS" generic. Cần xóa TC hoặc đổi thành "API POST giá trị boolean cũ → 400 invalid enum".

- **TC-KH-07 walks 6 transitions trong 1 TC.** "NHAP → CHO_DUYET → TU_CHOI → CHO_DUYET → DA_DUYET → DA_CONG_KHAI → DA_DUYET" — quá nhiều assertion, fail 1 step không xác định được state nào hỏng. Split thành 3 TC: refinement Cách 2 (TU_CHOI → CHO_DUYET), happy approve (CHO_DUYET → DA_DUYET), công khai/hủy công khai (DA_DUYET ↔ DA_CONG_KHAI).

- **HOC_VIEN role + GIANG_VIEN role chuyên trang chưa có TC permission độc lập.** §1.3 ghi 2 role này "(cần seed qua FR-III-04 / FR-III-11)", §2.3 permission matrix có row HOC_VIEN nhưng TC-HV-08 chỉ test "không thấy KQ HV khác" không cover full matrix (HOC_VIEN.KE_HOACH_DAO_TAO=—, HOC_VIEN.LICH_HOC=R khóa đăng ký, v.v.). Cũng không có TC GIANG_VIEN xem khóa được phân + xem GV self profile.

- **SCR-III-00 KH năm v3.5 mới — chỉ 9 TC, ít vs phạm vi 3 FR + workflow + permission + filter.** TC-KH-01..09 (9 TC) cover 3 FR (FR-III-14/15/16) + SM-KH-DAO-TAO 5 state + 2 BR-AUTH. Tỷ lệ TC/FR = 3 — quá thấp vs phụ lục B BR (BR-DATA-01..07 7 BR + BR-FLOW + BR-PUBLIC). Đặc biệt thiếu: TC filter `nam`+`trang_thai`+đơn vị (SCR-III-00 toolbar), TC drawer "Lịch sử workflow" tab 3, TC pagination 20/100/10000 boundary export BR-DATA-06/07.

## Suggestions

- **Tách bảng FR-ID vs SCR-ID trong §1.2 thành 2 view.** Hiện gộp cột "Sub-menu" + "File TC" gây khó trace ngược "FR nào ở SCR nào". Thêm cột "SCR-ID" riêng + footnote map SCR-III-00→sub-menu 1, ..., SCR-III-05→sub-menu 6.

- **Đặt bảng "TC chưa chạy được" placeholder ngay sau Verdict** theo rule CLAUDE.md §"Functional/Workflow report — 2 bảng tổng hợp BẮT BUỘC". Test plan thiếu hoàn toàn — phải có template Bảng 1 + Bảng 2 sẵn sàng cho round chạy đầu tiên.

- **Thêm row matrix cho ENUM điểm danh 3-value** trong §2.3 permission. Hiện chỉ có row "LICH_HOC — CRUD" — thiếu row "Điểm danh — Write" mà CB NV cùng đơn vị mới được điểm danh.

- **Note ngày `2026-05-12` thiếu HH:MM:SS** theo rule memory `feedback_date_include_time` (2026-05-09). Đổi thành `2026-05-12 HH:MM:SS` ở header §0 ngày tạo.

- **Cap upper limit TC vs lower bound coverage**: 39 TC / 24 FR ≈ 1.6 TC/FR rất ít. Add expected TC tier guidance: P0 happy + P0 negative chính + P0 auth ≥ 3 TC/FR cho FR Essential — sẽ ra ~70 TC. Nếu giữ 39 phải note explicit "TC scope GĐ 3 này CHỈ cover smoke + critical negative, full functional defer round sau".

- **Reference path PREFIX bắt buộc**: SRS ref ở §2.1 + §2.2 đã dùng `srs-update-2026-5-5/srs-fr-03-dao-tao.md:NNNN` ✓. Nhưng §2 còn trỏ `srs-v3/srs-v3.md:4066` (BR-EC-01 Phụ lục B) — verify line number BR-EC-01 trong v3 master còn đúng sau update v3.5 (NotebookLM query xác nhận).

- **Bổ sung TC bốc câu hỏi đề kiểm tra FR-III-NEW-01 NGAU_NHIEN vs THU_CONG**. Hiện 3 TC NEW-01/02/03 gộp vào file 02 "phụ trợ" không có TC detail. Nếu test plan giữ 4 sub-menu thì viết rõ ≥2 TC cho NEW-01 (bốc ngẫu nhiên N câu theo độ khó + verify duplicate) để tránh skip.

- **Thêm preset seed cho HOC_VIEN trong §2.6**. Bảng hiện ghi "(cần bổ sung — xem DELTA-MAP §4)" — phải nêu explicit task seed `hoc_vien_variants` 6 variants/entity theo rule actor entity (`feedback_seed_actor_state_gap`): split 2 task seed-create + advance-state cho HV.

- **Verify ambiguity §0 trước khi viết TC detail, không sau.** 3 ambiguity (GV entity location, NEW-01/02/03 UI, HOC_VIEN account) là blocker BA — sign off trước Bước 4 viết file 01-04, theo rule scaling-test-strategy §4.1.

- **Cross-link permission-matrix.md cập nhật.** `_DELTA-MAP-FR03.md:84` ghi "permission-matrix.md cần thêm KE_HOACH_DAO_TAO + HOC_VIEN + LICH_HOC entity mới". §2.3 test plan đã copy local nhưng nguồn chưa update — phải đồng bộ trước round chạy.

## Verdict

**REVISE** — 3 blocker critical: SM-KHOAHOC state count drift 9 vs 11 chưa giải quyết (test sẽ FAIL hoặc Sai spec random), FR-III-21 hoàn toàn miss (transition CHO_DUYET → DA_DUYET cho khóa học không có TC), junction KHOA_HOC_GIANG_VIEN.vai_tro override không có TC. Cộng 3 important miss (BR-PUBLIC switch, FR-III-19 hủy công bố, BR-INTG-05 retry). Test plan có cấu trúc tốt (6 section đầy đủ, BR/error/permission/UI/SM/data dep) nhưng coverage 39 TC quá ít cho 24 FR + v3.5 mới (+133%). Cần fix 3 blocker + add ≥15 TC trước khi BA sign-off.

Tóm tắt: Đã review test plan FR-03 đào tạo 411 dòng vs SRS v3.5 + delta map. Verdict REVISE — 3 blocker critical (SM state drift, FR-III-21 miss, junction vai_tro không test) + 9 gap quan trọng khác. File output: `/Users/teamai/Downloads/antigravity/QA/skilkk/docs/todo-test/fr-03-dao-tao/review.md`.
