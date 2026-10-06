# Phản hồi BA — Quản lý DN được hỗ trợ (phiếu ba-confirmation-doanh-nghiep.md)

**Phiếu nguồn:** `ba-confirmation-doanh-nghiep.md` (Tuần 3, KTĐL, 2026-07-20)
**Nguồn đối chiếu:**
- `_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md` (FR-V.III-01/02/NEW-03; SCR-V.III-01/02/03)
- `_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md` (quy ước dùng chung UI-08…UI-11, DG-03/06/08; BR-AUTH-08)
- `docs/Input/Danh sách transaction_v1.1_2026-03-27.csv` (UC81 Thêm, UC82 Tìm kiếm DN)

**Ngày lập:** 23/07/2026.

> **Lưu ý số dòng:** phiếu KTĐL trích theo bản `Docs-PM-HTPLDN/...`; nội dung trùng khớp file SRS trong repo nhưng số dòng lệch. Mọi trích dẫn dưới đây dùng số dòng **thực tế trong repo** đã mở kiểm.

---

## QLDNDHTPL_05 và QLDNDHTPL_06 — Form Thêm mới DN gom 2 nhóm thay vì 3 nhóm A/B/C

**Loại quyết định:** **Loại 1 — Dev fix theo SRS.** ✅ Đã chốt (2026-07-23): tổ chức lại form Thêm mới thành 3 khối A/B/C theo §Bố cục form.

**Bối cảnh nghiệp vụ.** Cán bộ Nghiệp vụ (TW/BN/ĐP) mở form Thêm mới DN (SCR-V.III-03, UC81 "Thêm") để tự tạo hồ sơ DN. `_05` kiểm nhóm Định danh cơ bản, `_06` kiểm nhóm Địa lý + Phân loại.

**Đối tác phản ánh.** "Bố cục không giống thiết kế" — form chia 2 nhóm "Thông tin chung" + "Thông tin liên hệ" thay vì 3 nhóm A/B/C. QA xác nhận đủ trường Nhóm A và Nhóm B, chỉ khác cách gom nhóm.

**Đối chiếu SRS/CSV.** SCR-V.III-03 §Bố cục form quy định **rõ 3 nhóm**: "Nhóm A — Định danh cơ bản", "Nhóm B — Địa lý + Phân loại", "Nhóm C — Thông tin bổ sung", liệt kê đủ trường từng nhóm (`srs-fr-07-doanh-nghiep.md:550-586`). Chú thích "(sẽ bổ sung)" chỉ gắn với UX-Spec chi tiết MH-VII-03 (`:609`) — bản vẽ pixel còn để ngỏ, KHÔNG phải §Bố cục form. Nhận định QA "SRS không ràng buộc cứng cách gom nhóm" chưa chính xác: SRS đã ràng buộc 3 nhóm A/B/C; web gom 2 nhóm → lệch điều khoản SRS rõ ràng → lỗi (Cosmetic).

**Căn cứ pháp lý & nghiệp vụ.** Nhóm C chở các trường ưu tiên có gốc pháp lý: §Bố cục form xếp vào Nhóm C các trường #16 "DN do phụ nữ làm chủ", #17 "Số lao động nữ", #18 "Số lao động khuyết tật" (`:581-583`) — chính là tiêu chí quyết định **thứ tự ưu tiên hỗ trợ** tại **NĐ 55/2019/NĐ-CP Điều 4 Khoản 4** điểm a (DN do phụ nữ làm chủ / dùng nhiều lao động nữ được hỗ trợ trước) và điểm b (DN dùng ≥30% lao động là người khuyết tật) — đã verify văn bản gốc (https://vanban.vcci.com.vn/nghi-dinh-552019nd-cp-ve-ho-tro-phap-ly-cho-doanh-nghiep-nho-va-vua). Các trường này nuôi BR-CALC-07 (điểm ưu tiên khi phân công). Vì vậy để Nhóm C thành khối riêng có nhãn rõ là để cán bộ nhận diện đúng nhóm dữ liệu ưu tiên, không phải trang trí. (Lưu ý: văn bản gốc dùng "người khuyết tật ≥30%", KHÔNG có "DN xã hội".)

**Nội dung xử lý.** Dev FE tổ chức lại form Thêm mới thành **3 khối** theo §Bố cục form: (A) Định danh cơ bản, (B) Địa lý + Phân loại, (C) Thông tin bổ sung. Đây cũng là nơi bổ sung 11 trường Nhóm C đang thiếu (trùng gốc BUG-QLDNDHTPL_04). Chỉ đổi cách nhóm/nhãn khối, không đụng ràng buộc trường. Điểm đồng bộ SRS: `srs-fr-07-doanh-nghiep.md:550-586`, `:581-583`, `:609`.

**Phản hồi gửi đối tác.** Ghi nhận đúng: form phải gom theo 3 nhóm A/B/C như SCR-V.III-03. Chuyển 2 case sang `Open` mức Cosmetic (gộp cùng bổ sung Nhóm C ở BUG-QLDNDHTPL_04), owner Dev FE. Không cần sửa Kết quả mong đợi.

---

## QLDNDHTPL_13 — Form Thêm mới không điền sẵn Tỉnh/TP theo đơn vị cán bộ

**Loại quyết định:** **Loại 1 — Dev fix theo SRS.** ✅ Đã chốt (2026-07-23): điền sẵn Tỉnh/TP cho cán bộ BN/ĐP; TW để trống là đúng.

**Bối cảnh nghiệp vụ.** Cán bộ Nghiệp vụ mở form Thêm mới DN. Trường Tỉnh/TP kỳ vọng điền sẵn theo đơn vị cán bộ đăng nhập để đỡ thao tác và giảm nhập sai; cán bộ vẫn chỉnh được nếu DN ở tỉnh khác.

**Đối tác phản ánh.** Form không điền sẵn Tỉnh/TP. QA verify: `cbnv_tw` (TW) trống; `cbnv_hn` (ĐP Hà Nội) cũng trống.

**Đối chiếu SRS/CSV.** QA đóng khung "SRS tự mâu thuẫn UI vs backend". **Không đồng ý** — hai điều khoản bổ trợ nhau:
- SCR-V.III-03 Nhóm B #6: "Default tự suy diễn theo đơn vị CB NV đăng nhập (BR-AUTH-08), CB NV có thể chỉnh nếu DN ở tỉnh khác" (`srs-fr-07-doanh-nghiep.md:566`) → yêu cầu **điền sẵn ở giao diện**.
- FR-V.III-NEW-03 Xử lý bước 2: nếu `tinh_thanh_id` chưa nhập → gán mặc định lúc lưu (`:292`) → lưới an toàn backend cho kênh không qua form (API), không thay yêu cầu điền sẵn UI.
- BR-AUTH-08 (`srs-v3.5.md:5443`): TW xem toàn quốc (không gắn một tỉnh → để trống hợp lý); ĐP Hà Nội gắn đúng một tỉnh → phải điền sẵn "Hà Nội".
→ Web đúng ở TW, sai ở cán bộ địa phương (Hà Nội vẫn trống) — vi phạm dòng 566.

**Nội dung xử lý.** Dev FE: form Thêm mới điền sẵn Tỉnh/TP = tỉnh của đơn vị cán bộ đối với cán bộ BN/ĐP (chỉnh được); cán bộ TW để trống. Giữ lưới an toàn backend ở bước lưu (dòng 292). Điểm đồng bộ SRS: `srs-fr-07-doanh-nghiep.md:566`, `:292`; `srs-v3.5.md:5443`.

**Phản hồi gửi đối tác.** SRS không mâu thuẫn; nguồn chuẩn giao diện là dòng 566. Web `Vẫn lỗi` với cán bộ địa phương → `Open`, owner Dev FE. Với TW để trống là đúng — nếu test case kỳ vọng TW cũng điền sẵn thì cập nhật Kết quả mong đợi cho khớp phạm vi TW.

---

## QLDNDHTPL_17 — Danh sách DN không sắp xếp khi click tiêu đề cột

**Loại quyết định:** **Loại 3 — Không fix; đề nghị đối tác đưa vào yêu cầu cải tiến.** ✅ Đã chốt (2026-07-23): đồng ý, không mở lỗi.

**Bối cảnh nghiệp vụ.** Cán bộ Nghiệp vụ xem danh sách DN (SCR-V.III-01), muốn click tiêu đề cột để sắp xếp tăng/giảm luân phiên.

**Đối tác phản ánh.** Click tiêu đề cột không sắp xếp. QA verify: bảng không cấu hình sắp xếp tương tác — tái hiện đúng.

**Đối chiếu SRS/CSV.** SCR-V.III-01 §Quy tắc tương tác chỉ quy định "Sắp xếp mặc định: ngày cập nhật mới nhất trước" (`srs-fr-07-doanh-nghiep.md:448`); bảng thành phần cột (`:436-443`) không định nghĩa hành vi sắp-xếp-khi-click. Quy ước dùng chung DG-06 (`srs-v3.5.md:956`) chỉ có sắp xếp mặc định, không bắt buộc click-sort. Web đã đúng phần "sắp xếp mặc định"; sắp xếp tương tác theo cột là chức năng ngoài đặc tả.

**Nội dung xử lý.** Không fix. Liệt kê sắp-xếp-khi-click-cột vào **danh mục yêu cầu cải tiến** để BA/CĐT cân nhắc bổ sung. Đối tác cập nhật Kết quả mong đợi test case.

**Phản hồi gửi đối tác.** Phần mềm đúng SRS (SRS/DG-06 chỉ yêu cầu sắp xếp mặc định — đã có). Sắp xếp khi click tiêu đề cột là chức năng mới → liệt kê vào yêu cầu cải tiến.

---

## TKDNHTPL_02 — Bộ lọc / tìm kiếm danh sách DN khác thiết kế (5 ý con)

**Loại quyết định (theo từng ý):** ý 1/5/2/3 = **Loại 1 — Dev fix theo SRS**; ý 4 = **Loại 3 — Không fix (giữ theo SRS)**. ✅ Đã chốt (2026-07-23).

**Bối cảnh nghiệp vụ.** Cán bộ Nghiệp vụ / Phê duyệt lọc danh sách DN (UC82). CSV UC82 tiêu chí lọc: từ khóa (tên/MST), lĩnh vực kinh doanh, thời gian; không có "Ngành nghề" hay "Đơn vị" (`Danh sách transaction_v1.1_2026-03-27.csv:689-696`). SRS filter-bar định nghĩa 6 trường: Từ khóa, Quy mô, Tỉnh thành, Lĩnh vực KD (multi-select VSIC cấp 4), Từ ngày, Đến ngày (`srs-fr-07-doanh-nghiep.md:427-434`, Lĩnh vực KD `:430`).

**Đối tác phản ánh.** 5 ý: (1) nhãn "Lĩnh vực KD" đang hiện "Ngành nghề"; (2) không đặt default "Tất cả" cho Quy mô/Tỉnh/Lĩnh vực KD; (3) Lĩnh vực KD chỉ chọn 1 giá trị; (4) không có field "Đơn vị" cho cấp TW; (5) ô "Ngành nghề" thừa "không có ý nghĩa".

**Đối chiếu SRS/CSV + căn cứ.**
- UI-11 (`srs-v3.5.md:580`): mọi ô lọc chọn nhiều phải có mục "Tất cả" → áp cho ô Lĩnh vực KD (multi-select).
- Chuẩn dữ liệu Lĩnh vực KD: `linh_vuc_ids` **Multi-select** (Inputs FR-V.III-02 row 4) + junction `DOANH_NGHIEP_LINH_VUC` M-N (baseline §3.4.3.3a "một DN có thể thuộc nhiều lĩnh vực"); nguồn VSIC 2025 cấp 4 (QĐ 36/2025/QĐ-TTg) đồng bộ chuẩn ĐKKD **NĐ 168/2025/NĐ-CP** — một DN đăng ký nhiều ngành nghề → ô lọc phải multi-select.
- SRS filter-bar (`:427-434`) + CSV UC82 (`:689-696`) chỉ có 6 trường, không có "Đơn vị" và không có "Ngành nghề" riêng.
- Filter-bar thuần trải nghiệm, không có điều khoản luật ràng buộc cách bố trí.

**Nội dung xử lý.**
- **Ý 1 + 5 (Loại 1):** Dev fix theo SRS — **bỏ ô "Ngành nghề"** (ngoài 6 trường SRS + CSV UC82); nhãn/placeholder ô lọc phải **khớp tên trường SRS** ("Lĩnh vực KD").
- **Ý 2 (Loại 1):** Ô **Lĩnh vực KD (multi-select) BẮT BUỘC có mục "Tất cả"** theo UI-11 → Dev bổ sung. Ô **Quy mô / Tỉnh (chọn đơn):** SRS không quy định default "Tất cả" → giữ theo SRS (để trống = không lọc), Dev không cần thêm.
- **Ý 3 (Loại 1):** Lĩnh vực KD = **multi-select** theo SRS + NĐ 168/2025. Nếu app đang chỉ cho chọn 1 → Dev fix thành multi; nếu app đã multi → đối tác sửa Kết quả mong đợi.
- **Ý 4 (Loại 3):** **Theo SRS — KHÔNG bổ sung** field "Đơn vị" (SRS + CSV UC82 chỉ có 6 trường); không phải lỗi.
- Sau khi Dev fix, cập nhật SCR-V.III-01 §filter-bar cho khớp. Điểm đồng bộ SRS: `srs-fr-07-doanh-nghiep.md:427-434`, `:430`; `srs-v3.5.md:580`; `csv:689-696`.

**Phản hồi gửi đối tác.**
- Ý 3: Lĩnh vực KD là chọn-nhiều (đúng SRS + luật ĐKKD NĐ 168/2025); app single → Dev fix, app đã multi → sửa Kết quả mong đợi.
- Ý 2: ô Lĩnh vực KD phải có "Tất cả" theo UI-11 (Dev fix); ô Quy mô/Tỉnh giữ theo SRS.
- Ý 1/5: bỏ ô "Ngành nghề" thừa + chuẩn nhãn theo SRS (Dev fix).
- Ý 4: giữ theo SRS, không thêm field "Đơn vị".

---

## TKDNHTPL_03 — Tìm không ra kết quả: hiển thị "Trống" thay vì thông báo cụ thể

**Loại quyết định:** **Loại 1 — Dev fix theo SRS.** ✅ Đã chốt (2026-07-23): hiện INF-DN-TK-01 "Không tìm thấy doanh nghiệp phù hợp".

**Bối cảnh nghiệp vụ.** Cán bộ Nghiệp vụ nhập tiêu chí tìm DN không khớp bản ghi nào; kỳ vọng thông báo rõ nghĩa thay vì trạng thái rỗng chung chung.

**Đối tác phản ánh.** Hệ thống hiển thị "Trống". QA verify: vùng kết quả 0 dòng hiện "Trống" (mặc định của thành phần rỗng) — tái hiện đúng.

**Đối chiếu SRS/CSV.** QA kết luận "SRS không quy định câu chữ empty-state" (chỉ trích phần Màn hình). **Không đồng ý** — QA bỏ sót bảng Xử lý lỗi: FR-V.III-02 §Error Handling E1 "Không có kết quả" → mã `INF-DN-TK-01` → **"Không tìm thấy doanh nghiệp phù hợp"**, mức INFO (`srs-fr-07-doanh-nghiep.md:260`). Web hiện "Trống" là không đúng thông báo đặc tả → lỗi.

**Nội dung xử lý.** Dev FE: khi tìm kiếm/lọc trả về 0 bản ghi, vùng kết quả hiển thị đúng `INF-DN-TK-01` "Không tìm thấy doanh nghiệp phù hợp" (thay chuỗi "Trống" mặc định). Điểm đồng bộ SRS: `srs-fr-07-doanh-nghiep.md:260`.

**Phản hồi gửi đối tác.** Ghi nhận đúng: SRS đã đặc tả thông báo (INF-DN-TK-01, FR-V.III-02 E1). Chuyển `Open` mức Minor, owner Dev FE. Không sửa Kết quả mong đợi (kỳ vọng đối tác trùng đặc tả).
