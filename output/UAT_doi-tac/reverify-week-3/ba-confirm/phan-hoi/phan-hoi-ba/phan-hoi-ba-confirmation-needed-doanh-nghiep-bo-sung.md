# Phản hồi BA — Doanh nghiệp bổ sung (phiếu ba-confirmation-needed-doanh-nghiep-bo-sung.md)

**Phiếu nguồn:** `ba-confirmation-needed-doanh-nghiep-bo-sung.md`
**Nguồn đối chiếu:** SRS v3.5 `srs-fr-07-doanh-nghiep.md` (SCR-V.III-02 màn Chi tiết DN, dòng 464–495; tab Lịch sử Hỗ trợ dòng 468; SCR-V.III-03 Form Thêm mới dòng 541–588) + baseline `srs-v3.5.md` + CSV `Danh sách transaction_v1.1_2026-03-27.csv`
**Ngày lập:** 23/07/2026.

---

## QLDNDHTPL_23 → _28 — Expected đối tác chấm theo bố cục "6 Nhóm" (thiết kế đối tác HTPLDN-PTYC-CT-v2.0) trong khi SRS v3.5 dùng danh sách trường phẳng

**Bối cảnh nghiệp vụ (chung cả cụm).** Màn Chi tiết Doanh nghiệp (SCR-V.III-02, FR-V.III-01, UC81) là màn để Cán bộ nghiệp vụ (TW/BN/ĐP) xem và sửa hồ sơ của một doanh nghiệp: thông tin định danh, số liệu lao động — tài chính, các tiêu chí được ưu tiên theo NĐ55/2019 Điều 4, cùng 4 tab (Thông tin cơ bản / Hồ sơ pháp lý DN / Lịch sử Hỗ trợ / Hồ sơ Chi trả). Đây là màn để tra cứu và làm việc, không phải màn nhập hồ sơ mới. Bên kiểm thử (KTĐL) chấm màn này dựa trên bản thiết kế riêng của họ (`HTPLDN-PTYC-CT-v2.0`), gom các trường thành "6 nhóm" và có thêm ô số tổng "Chỉ số tổng hợp". Còn SRS v3.5 — bản được giao để chấm — mô tả các trường theo kiểu **liệt kê thẳng thành một danh sách** (dòng 464–495), không gom "6 nhóm". File CSV gốc (`Danh sách transaction_v1.1_2026-03-27.csv`) chỉ chốt ai làm gì ở màn nào (CB NV mở UC81), không mô tả bày trí màn hình.

### QLDNDHTPL_23 — Bố cục trường màn Chi tiết DN: "6 Nhóm" hay danh sách phẳng
**(1) Phần mềm đúng SRS chưa?** ĐÚNG — SRS đặc tả trường màn Chi tiết dạng danh sách phẳng, gom 4 khối, đủ trường, không tràn/đè, đồng nhất ngôn ngữ; không quy định "6 Nhóm". `srs-fr-07-doanh-nghiep.md:464-495`.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — Đối tác chấm theo thiết kế riêng `HTPLDN-PTYC-CT-v2.0` gom thành "6 Nhóm"; SRS chỉ gom nhóm ở màn Thêm mới DN SCR-V.III-03 (`:552`, `:562`, `:572`), một màn khác.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến — gom 4 khối hay "6 Nhóm" đều là cách trình bày hợp lệ, không chặn luồng. Không sửa web; QA cập nhật Expected theo SRS v3.5; nếu muốn "6 Nhóm" thì đưa vào yêu cầu cải tiến.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: bố cục "6 Nhóm" ở màn Chi tiết DN (SRS dùng danh sách phẳng gom 4 khối).** **✅ BA duyệt 2026-07-24.**

> **Phản hồi gửi đối tác:** [Lý do] Tài liệu nghiệp vụ được giao để kiểm thử mô tả các trường ở màn Chi tiết doanh nghiệp theo danh sách gom 4 khối, đủ trường và dễ đọc, không quy định bố cục "6 Nhóm". Cách trình bày "6 Nhóm" thuộc bản thiết kế riêng của đối tác, không phải chuẩn để chấm kiểm thử; cả hai cách gom nhóm đều hợp lệ và không ảnh hưởng tới luồng nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

### QLDNDHTPL_24 — Có tách "Người đại diện" thành nhóm riêng không
**(1) Phần mềm đúng SRS chưa?** ĐÚNG — "Người đại diện"/"Chức vụ ĐD" nằm trong khối chung đúng SRS, không phải nhóm riêng. `srs-fr-07-doanh-nghiep.md:483-484`.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — Thiết kế đối tác tách "Người đại diện" thành một nhóm riêng; SRS để chung trong danh sách phẳng.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến — không ràng buộc luồng. Không sửa web; QA cập nhật Expected.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: tách "Người đại diện" thành nhóm riêng (SRS để chung trong danh sách phẳng).** **✅ BA duyệt 2026-07-24.**

> **Phản hồi gửi đối tác:** [Lý do] Theo tài liệu nghiệp vụ, thông tin người đại diện và chức vụ đại diện nằm trong khối chung của danh sách trường ở màn Chi tiết, không tách thành nhóm riêng. Phần mềm đang hiển thị đúng, không thiếu trường; việc tách nhóm chỉ là cách trình bày, không ràng buộc luồng nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

### QLDNDHTPL_25 — Có tách "Tiêu chí ưu tiên" (NĐ55) thành nhóm riêng không
**(1) Phần mềm đúng SRS chưa?** ĐÚNG — 3 trường ưu tiên NĐ55 hiển thị đủ, liệt kê phẳng đúng SRS. `srs-fr-07-doanh-nghiep.md:488-490`.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — Thiết kế đối tác gom 3 trường thành "Nhóm 3" riêng; SRS liệt kê phẳng.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến — **Nghị định 55/2019/NĐ-CP, Điều 4 Khoản 4** chỉ yêu cầu 3 trường hiển thị đủ và đọc được để cán bộ nhận ra DN thuộc diện ưu tiên (DNNVV do phụ nữ làm chủ / dùng nhiều lao động nữ / dùng từ 30% lao động là người khuyết tật), không bắt tách thành "Nhóm 3". Không sửa web; QA cập nhật Expected.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: gom 3 trường ưu tiên NĐ55 thành "Nhóm 3" riêng (SRS liệt kê phẳng, đã đủ 3 trường).** **✅ BA duyệt 2026-07-24.**

> **Phản hồi gửi đối tác:** [Lý do] Nghị định 55/2019 chỉ yêu cầu hiển thị đủ 3 tiêu chí ưu tiên (doanh nghiệp do phụ nữ làm chủ / sử dụng nhiều lao động nữ / sử dụng từ 30% lao động là người khuyết tật) để cán bộ nhận diện được diện ưu tiên, không bắt gom nhóm. Phần mềm hiện đã hiển thị đủ 3 tiêu chí này nên đáp ứng đúng quy định. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

### QLDNDHTPL_26 — Trường "File đính kèm" ở khối "Thông tin khác"
**(1) Phần mềm đúng SRS chưa?** SAI (riêng phần "File đính kèm") — SRS `:493` quy định trường "File đính kèm" (`file_dinh_kem`, file-upload) **"Luôn hiển thị"** trên tab Thông tin cơ bản; đối chiếu ảnh UAT (`_26.jpg`, `_27.jpg`) khối "Thông tin khác" khi bung ra chỉ hiện đúng 1 trường "Ghi chú", KHÔNG có "File đính kèm". Theo thứ tự SRS (`:492` Ghi chú → `:493` File đính kèm) trường này phải nằm ngay dưới Ghi chú → app đang thiếu trường `file_dinh_kem`. (Phần gom khối "Thông tin khác" thì đúng SRS, không sửa web.)
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác đòi đúng trường "File đính kèm" mà **chính SRS v3.5 quy định**; app mới là bên lệch SRS. Trường này khác với tab "Hồ sơ pháp lý DN" (entity `HO_SO_PHAP_LY_DN`: giấy phép/hợp đồng/giấy CN…). SRS hiện liệt kê `file_dinh_kem` ở cả bảng trường FR-V.III-01 (`:118`), inputs Thêm mới (`:285`, `:586`) và màn Chi tiết (`:493`).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa — Dev khôi phục trường "File đính kèm" (`file_dinh_kem`) ở khối "Thông tin khác" tab Thông tin cơ bản theo SRS `:493`, đặt ngay sau "Ghi chú" (chế độ xem: liệt kê/tải file đã đính kèm; chế độ sửa: upload nhiều file). Nếu CĐT/BA muốn chính thức bỏ/di dời khỏi màn Chi tiết → làm sạch SRS đồng bộ `:118`, `:285`, `:493`, `:586` (hướng thay thế, chỉ áp dụng khi CĐT/BA xác nhận).
**→ Kết luận: Loại 1 (Dev khôi phục — phương án A đã xác nhận) — Lỗi phần mềm, Dev sửa theo SRS: khôi phục trường "File đính kèm" (`file_dinh_kem`) ở khối "Thông tin khác" tab Thông tin cơ bản, đặt ngay sau "Ghi chú".** *(Đã đối chiếu evidence 2026-07-24)* **✅ BA duyệt 2026-07-24.**

### QLDNDHTPL_27 — Mục "Chỉ số tổng hợp"
**(1) Phần mềm đúng SRS chưa?** ĐÚNG — tìm cả file không thấy mục "Chỉ số tổng hợp" ở màn Chi tiết; màn Chi tiết chỉ có 3 ô số thống kê ở tab Lịch sử Hỗ trợ (`:468`, `:502`). App không hiển thị mục này là đúng SRS.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — Thiết kế đối tác thừa ô số tổng "Chỉ số tổng hợp"; SRS không có.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến — không ràng buộc luồng. Không sửa web; QA bỏ tiêu chí khỏi Expected; muốn thêm thì đưa vào yêu cầu cải tiến.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: mục "Chỉ số tổng hợp" ở màn Chi tiết DN (SRS không có, không hiển thị là đúng).** **✅ BA duyệt 2026-07-24.**

> **Phản hồi gửi đối tác:** [Lý do] Tài liệu nghiệp vụ không có mục "Chỉ số tổng hợp" ở màn Chi tiết doanh nghiệp — màn này chỉ có 3 ô số thống kê ở tab Lịch sử Hỗ trợ. Ô số tổng "Chỉ số tổng hợp" thuộc bản thiết kế riêng của đối tác, không phải chuẩn để chấm kiểm thử; việc phần mềm không hiển thị mục này là đúng thiết kế. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

### QLDNDHTPL_28 — Thiếu 2 cột "Lĩnh vực"/"Tư vấn viên" ở tab Lịch sử Hỗ trợ
**(1) Phần mềm đúng SRS chưa?** SRS thiếu — SRS `:468` để trống danh sách cột tab Lịch sử Hỗ trợ; app hiển thị "Danh sách VV + 3 KPI" nên không phải bug.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — Đối tác đòi thêm 2 cột "Lĩnh vực" và "Tư vấn viên"; SRS im lặng về danh sách cột.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến — 2 cột hữu ích tra cứu (vụ việc thuộc lĩnh vực nào, ai phụ trách) nhưng không chặn luồng. Không sửa web; BA bổ sung SRS `:468` chốt danh sách cột (ví dụ Mã VV / Tiêu đề / **Lĩnh vực** / **Tư vấn viên phụ trách** / Trạng thái / Ngày tiếp nhận, giữ nguyên 3 KPI); cân nhắc nhận 2 cột như cải tiến. Nếu không duyệt thì chốt SRS giữ bộ cột hiện tại để QA sửa Expected.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: thêm 2 cột "Lĩnh vực"/"Tư vấn viên" ở tab Lịch sử Hỗ trợ (SRS im lặng về danh sách cột, app hiện đủ dùng).** **✅ BA duyệt 2026-07-24.**

> **Phản hồi gửi đối tác:** [Lý do] Tài liệu nghiệp vụ hiện chưa chốt danh sách cột cho tab Lịch sử Hỗ trợ, nên việc phần mềm hiển thị danh sách vụ việc kèm 3 ô số thống kê không trái đặc tả. Hai cột "Lĩnh vực" và "Tư vấn viên" tuy hữu ích cho tra cứu nhưng không chặn luồng nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.
