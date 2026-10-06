# BA confirmation needed — Doanh nghiệp — Bổ sung UAT tuần 3 — 2026-07-20

> Nội dung được tách theo module từ file BA confirm đa module của UAT tuần 3. Các section đối chiếu SRS, evidence và câu hỏi BA được giữ nguyên.

## QLDNDHTPL_23 → _28 — Expected đối tác chấm theo bố cục "6 Nhóm" (thiết kế đối tác `HTPLDN-PTYC-CT-v2.0`) trong khi SRS v3.5 dùng danh sách trường phẳng ở màn Chi tiết DN

**Bối cảnh testcase**

- Dòng Excel: 34–39; mã TC `QLDNDHTPL_23` / `_24` / `_25` / `_26` / `_27` / `_28`.
- Nội dung kiểm tra: CB Nghiệp vụ mở màn Chi tiết DN qua nút "Xem" (SCR-V.III-02, FR-V.III-01, UC81) → kiểm tra hiển thị từng nhóm thông tin.
- Expected trong file UAT (đối tác chấm theo thiết kế `HTPLDN-PTYC-CT-v2.0`, mỗi nhóm phải "giống thiết kế", đúng định dạng, không tràn/đè, đồng nhất ngôn ngữ):
  - `_23` — Nhóm 1 Thông tin DN; `_24` — Nhóm 2 Người đại diện; `_25` — Nhóm 3 Tiêu chí ưu tiên NĐ55 Điều 4.
  - `_26` — Nhóm 4 Thông tin khác; `_27` — Nhóm 5 Chỉ số tổng hợp (kỳ vọng có mục này); `_28` — Nhóm 6 Lịch sử hỗ trợ (kỳ vọng có cột "Lĩnh vực" + "Tư vấn viên").
- Actual đối tác ghi: các nhóm "không giống với thiết kế" (khác cách gom nhóm); Nhóm 5 "Chỉ số tổng hợp" không hiển thị; Nhóm 6 thiếu cột "Lĩnh vực" + "Tư vấn viên".

**Đối chiếu SRS v3.5**

- Màn Chi tiết DN (SCR-V.III-02) đặc tả các trường dưới dạng **danh sách phẳng** (bảng thành phần), **KHÔNG** gom thành "6 Nhóm". Bố cục gom nhóm trong SRS ("Nhóm A/B/C") **chỉ tồn tại ở màn THÊM MỚI DN** (SCR-V.III-03), không phải màn Chi tiết → "6 Nhóm" là cấu trúc của thiết kế đối tác, không có trong SRS được giao chấm.
- SRS **không có** mục "Chỉ số tổng hợp" ở màn Chi tiết DN — chỉ có 3 KPI (Tổng VV / VV hoàn thành / Tổng chi phí) ở tab Lịch sử Hỗ trợ.
- Tab Lịch sử Hỗ trợ chỉ được đặc tả là "Danh sách VV liên kết + 3 KPI" — SRS **không quy định** danh sách cột (không nêu cột "Lĩnh vực" hay "Tư vấn viên").
- Trường "File đính kèm" thuộc nhóm cuối màn Chi tiết ("Luôn hiển thị") — cần xác nhận đã dời sang tab "Hồ sơ pháp lý" (gộp theo v2.1) hay chưa.

Bảng đối chiếu chi tiết theo từng case:

| Case | Đối tác kỳ vọng (theo thiết kế) | App thực tế | SRS v3.5 |
|---|---|---|---|
| _23 | Nhóm 1 gom đúng thiết kế | Trường cơ bản đủ, gom trong "Thông tin chung" + "Thông tin liên hệ", không tràn/đè | Danh sách phẳng, không quy định "6 Nhóm" (dòng 464–495) |
| _24 | Nhóm 2 "Người đại diện" riêng | "Người đại diện" + "Chức vụ đại diện" nằm trong "Thông tin chung" | Liệt kê phẳng, không tách nhóm riêng (dòng 483–484) |
| _25 | Nhóm 3 "Tiêu chí ưu tiên NĐ55" riêng | Phụ nữ làm chủ / Số LĐ nữ / Số LĐ khuyết tật nằm chung khối "Thông tin lao động & tài chính" | 3 trường NĐ55 liệt kê phẳng, không tách nhóm (dòng 488–490) |
| _26 | Nhóm 4 "Thông tin khác" đúng thiết kế | Khối "Thông tin khác" = Ghi chú; **chưa thấy** "File đính kèm" trên tab này | Nhóm cuối = Ghi chú (dòng 492) + File đính kèm (dòng 493, "Luôn hiển thị") |
| _27 | Nhóm 5 "Chỉ số tổng hợp" hiển thị | **Không có** mục "Chỉ số tổng hợp"; chỉ có 3 KPI ở tab Lịch sử hỗ trợ | **Không có** mục "Chỉ số tổng hợp" ở SCR-V.III-02 (dòng 464–495) |
| _28 | Nhóm 6 danh sách VV có cột "Lĩnh vực" + "Tư vấn viên" | Danh sách VV 4 cột: Mã / Tiêu đề / Trạng thái / Ngày tiếp nhận + 3 KPI; **không có** 2 cột đó | Tab Lịch sử Hỗ trợ = "Danh sách VV liên kết + 3 KPI", **không quy định cột** (dòng 468) |

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:464-495` (SCR-V.III-02 — bảng thành phần màn Chi tiết, danh sách trường phẳng)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:468` (tab Lịch sử Hỗ trợ = "Danh sách VV liên kết + 3 KPI", không quy định cột)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:483-484` (Người đại diện + Chức vụ ĐD) · `:488-490` (3 trường NĐ55) · `:492-493` (Ghi chú + File đính kèm)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:552` · `:562` · `:572` (bố cục "Nhóm A/B/C" — CHỈ ở màn Thêm mới SCR-V.III-03, không phải Chi tiết)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:79` (UC Reference UC81 cho FR-V.III-01)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, dùng tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/doanh-nghiep/5eed0010-0000-4000-8000-000000000001` (DN-SEED-0001 "Công ty TNHH Seed Publishable").
- Tab "Thông tin": 4 khối (Thông tin chung / Thông tin liên hệ / Thông tin lao động & tài chính / Thông tin khác), 23 trường — đủ trường cơ bản + đủ 3 trường NĐ55 (Phụ nữ làm chủ, Số LĐ nữ, Số LĐ khuyết tật); tìm toàn trang KHÔNG có mục "Chỉ số tổng hợp".
- Tab "Lịch sử hỗ trợ": danh sách VV 4 cột (Mã / Tiêu đề / Trạng thái / Ngày tiếp nhận) + 3 KPI (Tổng VV 14 / VV hoàn thành 5 / Tổng chi phí 0₫) — không có cột "Lĩnh vực" / "Tư vấn viên".
- Đối chiếu: app hiển thị đủ mọi trường/thành phần SRS v3.5 yêu cầu; khác biệt với đối tác chỉ ở cách gom nhóm/có mục "Chỉ số tổng hợp"/có 2 cột — đều là những thứ SRS v3.5 không quy định.
- Evidence: `../../reverify-audit/QLDNDHTPL_23/thong-tin-tab-full.png` (dùng chung _23–_27) · `../../reverify-audit/QLDNDHTPL_28/lich-su-ho-tro-columns.png` (_28).

**Kết luận QA**

- Cả 6 case `_23` → `_28` **không phải bug theo SRS v3.5**: app đủ trường/đủ thành phần đặc tả, đúng định dạng, không tràn/đè, đồng nhất ngôn ngữ.
- Web hiện tại **đúng SRS v3.5**; điểm đối tác phản ánh là khác biệt so với **thiết kế đối tác** (`HTPLDN-PTYC-CT-v2.0`), không phải khác biệt so với SRS:
  - `_23`/`_24`/`_25`/`_26`: chỉ khác **cách gom nhóm** — SRS dùng danh sách phẳng, không ép "6 Nhóm";
  - `_27`: mục "Chỉ số tổng hợp" **không có trong SRS** (app khớp SRS, thiết kế đối tác thừa mục này);
  - `_28`: SRS **silent về cột** danh sách VV (app đủ "Danh sách VV + 3 KPI").
- QA **không tự Reject** vì chưa rõ thiết kế đối tác có phải nguồn ràng buộc bổ sung không → cần BA chốt (không tự chốt được phần "thiết kế đối tác có hiệu lực trên SRS hay không").

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận với đối tác 4 điểm để chốt hướng xử lý:

1. **Bố cục màn Chi tiết DN** — bắt buộc theo "6 Nhóm" của thiết kế đối tác, hay danh sách trường phẳng theo SRS v3.5 (đủ trường, gom 4 khối) là đạt? (áp cho `_23`/`_24`/`_25`/`_26` — cùng 1 quyết định).
2. **Trường "File đính kèm"** (SRS `:493`, "Luôn hiển thị") — đặt ngay tab Thông tin hay đã chuyển hẳn sang tab "Hồ sơ pháp lý" (gộp v2.1)? (`_26`).
3. **Mục "Chỉ số tổng hợp"** (Nhóm 5) — bắt buộc bổ sung vào màn Chi tiết theo thiết kế đối tác, hay theo SRS v3.5 (không có mục này) là đạt? (`_27`).
4. **Cột danh sách VV tab Lịch sử hỗ trợ** — bắt buộc thêm "Lĩnh vực" + "Tư vấn viên" theo thiết kế đối tác, hay bộ 4 cột hiện tại là đạt? (`_28`).

- Verdict QA đề xuất: `Cần BA xác nhận` cho cả 6 case (`_23`→`_28`) — **chưa gửi Dev** cho tới khi BA chốt thiết kế đối tác có ràng buộc hay không.
- Nếu BA chốt **theo SRS v3.5**: cả 6 case đóng "Không phải bug theo SRS", QA cập nhật lại expected testcase của đối tác.
- Nếu BA chốt **theo thiết kế đối tác** (bắt buộc "6 Nhóm" / có "Chỉ số tổng hợp" / có 2 cột): chuyển thành yêu cầu bổ sung, owner `Dev FE` (bố cục/cột/mục hiển thị).
- Chi tiết note từng case: `../../reverify-audit/QLDNDHTPL_23..28/note.txt`.

---

> **QLDKTK_03 (BA confirm)** — đã tách sang file riêng: [`../qldktk/ba-confirmation-needed-week-3-QLDKTK.md`](../qldktk/ba-confirmation-needed-week-3-QLDKTK.md) (theo yêu cầu gửi riêng cho BA).

---

*(Các mục BA khác sẽ bổ sung khi phát sinh trong quá trình verify các case còn lại.)*
