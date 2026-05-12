# Review — FR-09 Biểu mẫu test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 14:41:00

## Gaps

- **G1 — Version control TC thiếu hẳn nhưng plan ngầm yêu cầu retest "Upload version mới".** Plan line 217 + line 423 ghi rõ SRS v3.5 KHÔNG có entity `BIEU_MAU_VERSION` và defer SPEC-CLARIFY-09-V1. Tuy nhiên file [BIEU_MAU §3.4.3.37](`srs-update-2026-5-5/srs-fr-09-bieu-mau.md:755-779`) cũng không có cột `phien_ban` / `version_id` → quyết định defer ĐÚNG, nhưng nên thêm TC REG-006 chứng minh "Sửa biểu mẫu + upload file mới KHÔNG tạo version mới, ghi đè `duong_dan_file`" (currently chưa có TC test behavior này). Gap = chứng minh defer hợp lệ.

- **G2 — Thiếu TC verify file PDF KHÔNG được chấp nhận ở field `file` chính (chỉ chấp nhận PDF ở `file_dinh_kem_cong_khai`).** SRS line 300 ràng buộc `file_dinh_dang IN ('doc','docx','xls','xlsx')` cho field chính (KHÔNG có PDF), trong khi line 306 + 769 ràng buộc `file_dinh_kem_cong_khai IN ('PDF','DOC','DOCX','XLS','XLSX')` (CÓ PDF). TC BM-003 chỉ test PDF reject ở field chính — chưa có TC test "PDF accepted ở field công khai" để phân biệt 2 ràng buộc khác nhau. Risk: dev nhầm 1 enum chung → false positive.

- **G3 — Virus scan / MIME mismatch coverage thiếu chi tiết.** BM-009 chỉ test "macro virus → ClamAV reject" theo EC-02 (`srs-update-2026-5-5/srs-fr-09-bieu-mau.md:384`). Thiếu TC: (a) MIME spoof — file rename `.docx` nhưng magic bytes là EXE; (b) ZIP bomb (docx là ZIP container); (c) virus phát hiện ASYNC sau khi đã commit BIEU_MAU. SRS bước 5 line 316 "Quét virus file đính kèm" — không phân biệt trước/sau lưu storage.

- **G4 — CR-01 boundary cho `mo_ta_cong_khai` không có ràng buộc max length test.** SRS line 305 + 768 quy định `mo_ta_cong_khai` là `text (long)` KHÔNG nêu max ký tự cụ thể (khác `mo_ta` thư mục max 2000, plan line 171). BM-CR-001 happy không test biên — thiếu TC `mo_ta_cong_khai` 1MB / 100k ký tự → reject hay accept. SPEC-CLARIFY cần raise.

- **G5 — BR-PUBLIC-02 unpublish API failure rollback chưa có TC cứng.** BM-CR-008 ghi "Cổng PLQG 5xx → giữ trạng thái cũ + thông báo retry" nhưng SRS line 931 (BR-PUBLIC-02) yêu cầu 3 action atomic: `cong_khai=0` + `thoi_gian_dang_tai=NULL` + API gỡ Cổng. Nếu API gỡ fail, plan không nói rõ DB state nào (đã set `cong_khai=0` rồi nhưng Cổng vẫn còn record? hay rollback hoàn toàn?). EC-04 line 386 áp cho XÓA biểu mẫu, không áp cho TẮT Switch. Gap spec.

- **G6 — Soft-delete THU_MUC chứa BM CONG_KHAI không có TC.** ERR-TM-02 line 131 chỉ check "thư mục chứa N biểu mẫu" → reject. Nhưng SRS không phân biệt biểu mẫu state nào — nếu thư mục có 1 BM `is_deleted=1` (soft-deleted) thì xóa được không? TM-003 chỉ test "có 1 biểu mẫu" generic. Cần TC: thư mục có 0 BM active + N BM `is_deleted=1` → xóa OK hay FAIL.

- **G7 — Cascade publish thư mục lên 100+ biểu mẫu không có TC performance.** BR-FLOW-07 + FR-VII-03 bước 4 line 236 "đẩy thư mục + biểu mẫu lên Cổng" — API response time NFR <3s (`srs-update-2026-5-5/srs-fr-09-bieu-mau.md:544`) chỉ áp cho FR-VII-07 outbound, không cover thời gian publish cascade. TM-010 happy "3 BM" — không test boundary 100 BM. Nên có edge TC: publish thư mục 50/100 BM verify không timeout client.

- **G8 — `so_luot_tai` counter không có TC.** SRS field 14 line 770: `so_luot_tai NUMBER DEFAULT 0` increment khi TAI_BIEU_MAU. Plan có audit log TC (BR-DATA-05) nhưng KHÔNG có TC verify counter `so_luot_tai` increment đúng + concurrent download không bị race condition (lost update). Quan trọng cho báo cáo thống kê chuyên trang.

- **G9 — Permission row "TVV" trùng "TVV" sai context với users.csv.** Plan table line 127-138 cột "TVV" — nhưng `input/users.csv` (per CLAUDE.md) có CG + NHT + TVV là 3 entity khác nhau ở FR-04. Plan §1.3 line 60-62 không list TVV account. Trùng lặp với CG (cùng quyền R CONG_KHAI). Khuyến nghị bỏ cột TVV hoặc liệt kê account TVV dedicated trong §1.3.

- **G10 — REG-002 enum migration test không nêu cách verify.** "THU_MUC trạng thái `KICH_HOAT` cũ migration → phải migrate thành `NHAP`" cần `\sql` query trực tiếp DB (CHECK constraint chấp nhận giá trị nào). UI test không đủ — sẽ miss residual data. Thiếu method note: ai chạy SQL? QA-API? DBA?

- **G11 — `loai_hinh` field constraint khác SRS line 761.** SRS bảng BIEU_MAU line 761: `loai_hinh CHECK IN ('HOP_DONG','BIEU_MAU','MAU_DON','KHAC')` — 4 enum cố định. Plan line 189 + form field SRS line 297 ghi `loai_hinh = text (N), VD: HĐ lao động` (free-text). Plan chưa có TC test ràng buộc enum này — nếu BE thực thi check thì input "HĐ lao động" sẽ FAIL constraint. Cần TC verify form là dropdown 4 enum hay free text + cite line 761.

- **G12 — Cross-module FR-10 LINH_VUC_PL Tier dependency thiếu pre-flight check.** Plan §2.6 line 270 ghi FR-09 phụ thuộc FR-10 (QTHT seed DM). Nhưng KHÔNG có TC kiểm tra: nếu LINH_VUC_PL bị xóa SAU khi BIEU_MAU đã reference (`linh_vuc_id` orphan) — UI render gì? "Lĩnh vực không xác định"? Crash? ERR-TM-04 chỉ áp lúc TẠO/SỬA, không áp READ.

## Suggestions

- **S1 — Tách TC `cong_khai` toggle thành 2 module** (BIEU_MAU Switch + THU_MUC publish button). Plan đang trộn ở `03-TC-thu-muc-publish.md` (FR-VII-03 thư mục) + `05-TC-bieu-mau-cong-khai-cr01.md` (FR-VII-04 BIEU_MAU). Thêm note rõ cascade rule: nếu thư mục → CONG_KHAI, các BIEU_MAU bên trong tự động `cong_khai=1`? SRS line 367 "biểu mẫu mới tự động hiển thị trên Cổng (qua API sync)" mơ hồ — cần SPEC-CLARIFY.

- **S2 — Bug severity guideline thêm 1 case Critical CR-01.** "API outbound trả bản ghi `cong_khai=0`" line 396 chưa đủ — bổ sung "API outbound trả bản ghi `is_deleted=1`" (soft-deleted leak ra public chuyên trang) cũng là Critical. FR-VII-07 bước 2 line 540 `chỉ bản ghi chưa xóa` — verify filter `is_deleted=0 AND cong_khai=1`.

- **S3 — Format TC ID trộn 2 schema** `BM-001..010` + `BM-CR-001..009`. Khuyến nghị thống nhất `BM-001..019` hoặc `BM-CORE-001..010` + `BM-CR-001..009` để query/sort dễ. Hiện tại grep "BM-0" sẽ match cả 2.

- **S4 — Bổ sung TC PERM-007 verify QTHT KHÔNG bypass được BR-PUBLIC-01.** PERM-005 nói "QTHT override scope cross-đơn vị" — nhưng BR-PUBLIC-01 line 925 nói "bản ghi bị Từ chối/Hủy KHÔNG được công khai" — QTHT có override được ràng buộc này không? SRS không nêu rõ — cần test + log SPEC-CLARIFY.

- **S5 — TC outbound API thêm test pagination boundary** (page_size=21 → BR-DATA-07 max=100; page_size=101 reject). API-001 chỉ test happy. SRS line 533 cho page_size default 20.

- **S6 — Đổi cite line `bug-report` cho BR-EC-01/13/DATA-06.** Plan cite `srs-v3/srs-v3.md:4066/4078/3977` (line cross-cutting). Nhưng v3.5 có thể đã shift line numbers. Verify line numbers còn đúng — nếu BA build srs-v3.5 từ CHANGELOG, line offset có thể shift. Recommended: cite section ID (`§3.B.X`) thay vì line raw.

- **S7 — TC BM-CR-009 logic chuyên trang render — cần endpoint test.** Plan ghi "render chuyên trang chỉ thấy `mo_ta_cong_khai`" — nhưng chuyên trang dùng API FR-VII-07 hay public web `/chuyen-trang`? SRS không định nghĩa endpoint chuyên trang. Note dependency rõ + escalate BA.

- **S8 — `thu_tu_hien_thi` defer (REG-005 + line 374 DELTA-MAP §6 T8).** Khuyến nghị log SPEC-CLARIFY-09-V2 NGAY trong test plan version 1.0 thay vì viết TC verify gap — saving 1 cycle. Nếu BA OK, xóa REG-005 + đợi BA response.

- **S9 — Bổ sung TC TM-014 verify `cong_khai` boolean cho THU_MUC** (DELTA-MAP §6 D.2 chốt KHÔNG có 4 fields mở rộng cho thư mục). Plan line 424 đã note nhưng không có TC verify. Nên có 1 TC negative: API/UI thêm field `mo_ta_cong_khai` vào THU_MUC payload → BE reject 400/ignore.

- **S10 — Section 5 Tiêu chí PASS/FAIL bổ sung CR-01 critical gate.** "100% P0" hiện tại không đặc biệt với CR-01. Khuyến nghị "ngoài 100% P0, BM-CR-001..004 (toggle Switch + auto timestamp) PASS clean" là gate cứng — nếu CR-01 core fail thì release block.

## Verdict

**REVISE** — Plan đã cover tốt CR-01 rename + 4 trường công khai (BM-CR-001..009) + tách HĐ TV (REG-003) + enum THU_MUC migration (REG-002) + permission matrix 11 role × 6 action — đủ chiều rộng. Tuy nhiên 5 gap quan trọng cần fix trước khi BA sign-off:

1. **G2** (PDF accept ở `file_dinh_kem_cong_khai` nhưng không ở field chính) — risk dev nhầm enum.
2. **G5** (BR-PUBLIC-02 atomic unpublish khi Cổng PLQG fail) — spec gap, escalate BA TRƯỚC khi viết TC.
3. **G11** (`loai_hinh` enum constraint khác form free-text) — verify SRS bảng entity vs form spec.
4. **G3** (virus scan MIME mismatch / async detection) — security critical.
5. **G8** (`so_luot_tai` counter race condition) — data integrity.

Sau khi fix 5 gap trên + adopt S2 (Critical severity), S4 (QTHT bypass BR-PUBLIC-01), S10 (CR-01 gate) — plan có thể move to BA sign-off và viết TC detail 01-10. Đề xuất bump version 1.0 → 1.1 với changelog ghi rõ delta.

---

*Review based on:*
- `srs-update-2026-5-5/srs-fr-09-bieu-mau.md` (v3.5, 941 lines)
- `srs-v3/srs-fr-09-bieu-mau.md` (v3 baseline)
- `srs-update-2026-5-5/_DELTA-MAP-FR09.md` (6 changes A=1 + B1=5)
- `docs/todo-test/fr-09-bieu-mau/test-plan.md` v1.0 (429 lines)
