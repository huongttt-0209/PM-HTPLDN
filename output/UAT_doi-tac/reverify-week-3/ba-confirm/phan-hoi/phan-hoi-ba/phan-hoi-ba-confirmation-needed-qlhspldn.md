# Phản hồi BA — Quản lý hồ sơ pháp lý DN (phiếu ba-confirmation-needed-qlhspldn.md)

**Phiếu nguồn:** `ba-confirmation-needed-qlhspldn.md` (Tuần 3, verify 21/07/2026)
**Nguồn đối chiếu:**
- SRS v3.5 — `srs-fr-12-tv-chuyen-sau.md` FR-X.1-04 (UC150): §Inputs dòng 548-562, §Outputs dòng 642-656, entity HO_SO_PHAP_LY_DN dòng 1376-1402.
- SRS v3.5 baseline — `srs-v3.5.md` entity HO_SO_PHAP_LY_DN dòng 3561-3576.
- CSV baseline — `Danh sách transaction_v1.1_2026-03-27.csv` dòng 1339 (UC150).
**Ngày lập:** 23/07/2026.
**Evidence UAT:** Sheet `UAT_TGPL Doanh Nghiệp` dòng 1544 (QLHSPLDN_02) và 1545 (QLHSPLDN_03), cả hai trạng thái **Fail**, tệp minh chứng `QLHSPLDN_02.webm` / `QLHSPLDN_03.webm` (video — kiểm theo phần Kết quả thực tế + SRS, không xem được ảnh tĩnh). *(Đã đối chiếu evidence 2026-07-24 — Kết quả thực tế của đối tác nêu **nhiều điểm hơn** bản phiếu gốc; đã bổ sung các ý còn thiếu: cột "Có tệp đính kèm" ở QLHSPLDN_02; trường "Lĩnh vực pháp lý" và "Tệp đính kèm" ở biểu mẫu QLHSPLDN_03.)*

> **Kết quả thực tế đối tác ghi trong Sheet (nguyên văn):**
> - **QLHSPLDN_02 (bảng danh sách):** "Bảng danh sách thiếu các cột thông tin: Lĩnh vực pháp lý, Nguồn, Có tệp đính kèm" + "hiển thị trường Số/ký hiệu nhưng SRS không có trường này".
> - **QLHSPLDN_03 (biểu mẫu thêm/sửa):** "Biểu mẫu thêm mới thiếu các trường thông tin: Lĩnh vực pháp lý, Mô tả, Tệp đính kèm" + "hiển thị trường Số/ký hiệu nhưng SRS không có trường này".

---

### QLHSPLDN_02 (ý 1) & QLHSPLDN_03 (ý 1) — Cột/trường "Số/Ký hiệu" thừa
**(1) Phần mềm đúng SRS chưa?** SAI — web tự thêm cột/trường "Số/Ký hiệu" (`so_hieu`/`so_ky_hieu`) không có trong mô hình dữ liệu: entity 19 trường (`srs-fr-12-tv-chuyen-sau.md:1382-1402`; `srs-v3.5.md:3561-3576`), §Inputs biểu mẫu 11 trường (`srs-fr-12-tv-chuyen-sau.md:548-562`), §Outputs bảng danh sách 11 cột (`srs-fr-12-tv-chuyen-sau.md:642-656`) đều không có; thiết kế đối tác `HTPLDN-PTYC-CT-v2.0.docx §4.12.4.2.1` (10 cột) cũng không có.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác muốn bỏ cột/trường thừa, trùng đúng SRS (SRS vốn không có trường này).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa: Dev bỏ cột "Số/Ký hiệu" khỏi bảng danh sách và bỏ trường khỏi biểu mẫu Thêm/Sửa (nhập vào không có chỗ lưu). Không cần sửa SRS. Nếu sau này nghiệp vụ muốn lưu số/ký hiệu văn bản pháp lý thì bổ sung trường mới (entity + §Inputs + §Outputs) qua kênh yêu cầu cải tiến.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: bỏ cột/trường "Số/Ký hiệu" (thừa, không có trong mô hình dữ liệu) khỏi bảng danh sách và biểu mẫu Thêm/Sửa.** **✅ BA duyệt 2026-07-24.**

---

### QLHSPLDN_02 (ý 2) — Bảng danh sách thiếu cột "Lĩnh vực pháp lý"
**(1) Phần mềm đúng SRS chưa?** SRS thiếu/mâu thuẫn — trường Lĩnh vực pháp lý (`linh_vuc_id`, tra DANH_MUC) đã có trong entity (`srs-fr-12-tv-chuyen-sau.md:1389`; `srs-v3.5.md:3568`) và §Inputs biểu mẫu (`srs-fr-12-tv-chuyen-sau.md:556`), nhưng danh sách cột §Outputs (`srs-fr-12-tv-chuyen-sau.md:642-656`) bỏ sót — nơi nhập có, nơi hiển thị thiếu.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác muốn thêm cột "Lĩnh vực pháp lý" trên bảng danh sách, khác §Outputs hiện tại (nhưng khớp entity/§Inputs).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG bắt buộc theo luật — Nghị định 55/2019/NĐ-CP Điều 5-9 sắp xếp CSDL hỗ trợ pháp lý theo loại/nguồn văn bản (văn bản quy phạm; vụ việc, vướng mắc; bản án, quyết định tòa án; văn bản trả lời cơ quan nhà nước; văn bản tư vấn), không chia theo lĩnh vực pháp luật; việc hồ sơ phần này có vào CSDL theo NĐ55 hay không: **cần CĐT xác nhận**. Nhưng cần để đồng bộ nơi nhập ↔ nơi hiển thị và tiện lọc theo mảng (lao động, thuế, đất đai…). Hành động: bổ sung §Outputs FR-X.1-04 (`srs-fr-12-tv-chuyen-sau.md:642-656`) trường đầu ra `linh_vuc`/`ten_linh_vuc` (text, điều kiện "luôn", lấy tên từ DANH_MUC theo `linh_vuc_id`) + web thêm cột (gạch khi trống vì không bắt buộc). PA rút gọn: đưa lĩnh vực thành bộ lọc/nhãn phụ nếu bảng tràn ngang.
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: bổ sung trường đầu ra "Lĩnh vực pháp lý" vào §Outputs FR-X.1-04, rồi web thêm cột.** **✅ BA chốt 2026-07-24: giữ Loại 2** — đồng bộ §Outputs (trường đã bắt nhập thì phải cho hiển thị lại).
> **Phương án xử lý (cập nhật SRS):** `srs-fr-12-tv-chuyen-sau.md:642-656` (§Outputs FR-X.1-04) — thêm trường đầu ra `linh_vuc`/`ten_linh_vuc` (text, điều kiện "luôn", lấy tên từ DANH_MUC theo `linh_vuc_id`). Sau đó Dev thêm cột "Lĩnh vực pháp lý" vào bảng danh sách (gạch khi trống vì không bắt buộc).

---

### QLHSPLDN_02 (ý 3) — Bảng danh sách thiếu cột "Nguồn"
**(1) Phần mềm đúng SRS chưa?** SRS thiếu/mâu thuẫn — trường Nguồn (`nguon`, hai giá trị Thủ công / Cổng PLQG, mặc định Thủ công) đã có trong entity (`srs-fr-12-tv-chuyen-sau.md:1395`; `srs-v3.5.md:3574`) nhưng danh sách cột §Outputs (`srs-fr-12-tv-chuyen-sau.md:642-656`) bỏ sót.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác muốn thêm cột "Nguồn" (Thủ công / Cổng PLQG), khác §Outputs hiện tại; lưu ý cần chốt cột lấy dữ liệu từ đâu.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG bắt buộc theo luật nhưng hợp hướng khung pháp lý — Nghị định 55/2019/NĐ-CP Điều 5-9 phân biệt CSDL theo nguồn/loại văn bản; giá trị Cổng PLQG gắn Cổng Pháp luật quốc gia, còn CSDL quốc gia về pháp luật thuộc Nghị định 52/2015/NĐ-CP, việc Cổng PLQG trỏ đến hệ thống nào (CSDL quốc gia theo NĐ 52/2015 hay cổng khác): **cần CĐT xác nhận**. Cần để truy gốc hồ sơ (nhập tay UC150 vs tự nhận UC151, `srs-fr-12-tv-chuyen-sau.md:529` trở lên; CSV dòng 1356) và tránh sửa nhầm hồ sơ đồng bộ từ Cổng. Hành động: bổ sung §Outputs FR-X.1-04 (`srs-fr-12-tv-chuyen-sau.md:642-656`) trường `nguon` (text, "luôn", `THU_CONG`/`CONG_PLQG`, lấy trực tiếp từ entity) + web hiển thị nhãn "Thủ công" / "Cổng Pháp luật quốc gia" (nhãn chính thức & cách viết tắt nếu cần rút gọn: **cần CĐT xác nhận**). PA rút gọn: dùng biểu tượng/nhãn màu khi bảng tràn ngang (đánh đổi: phụ thuộc chú giải, kém rõ khi in/xuất báo cáo).
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: bổ sung trường đầu ra "Nguồn" vào §Outputs FR-X.1-04, rồi web thêm cột.** ✅ BA chốt 2026-07-24: nhãn "Thủ công" / "Cổng Pháp luật quốc gia" (nguồn từ chuyên trang HTPLDN); giữ Loại 2.
> **Phương án xử lý (cập nhật SRS):** `srs-fr-12-tv-chuyen-sau.md:642-656` (§Outputs FR-X.1-04) — thêm trường đầu ra `nguon` (text, điều kiện "luôn", giá trị `THU_CONG`/`CONG_PLQG`, lấy trực tiếp từ entity). Sau đó Dev thêm cột "Nguồn", hiển thị nhãn "Thủ công" / "Cổng Pháp luật quốc gia".

---

### QLHSPLDN_02 (ý 4) — Bảng danh sách thiếu cột "Có tệp đính kèm"
**(1) Phần mềm đúng SRS chưa?** SAI — §Outputs FR-X.1-04 đã có trường đầu ra `co_file` kiểu boolean, điều kiện "luôn" (`srs-fr-12-tv-chuyen-sau.md:654`), là cờ suy ra từ danh sách file đính kèm (§Xem chi tiết bước 4-5, `srs-fr-12-tv-chuyen-sau.md:629-630`), nhưng web chưa hiển thị cột.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác muốn cột đã quy định sẵn trong §Outputs, trùng SRS. (Kết quả thực tế nêu đủ ba cột thiếu: Lĩnh vực pháp lý, Nguồn, Có tệp đính kèm; bản phiếu gốc chỉ nêu hai cột đầu, cột này bổ sung theo evidence.)
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa: Dev thêm cột "Có tệp đính kèm" đọc từ trường đầu ra `co_file` (hiển thị Có/Không hoặc biểu tượng kẹp giấy). Không cần sửa SRS.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: thêm cột "Có tệp đính kèm" (đọc trường đầu ra `co_file` §Outputs đã có) vào bảng danh sách.** **✅ BA duyệt 2026-07-24.**

---

### QLHSPLDN_03 (ý 2) — Trường "Mô tả" đang hiển thị dưới nhãn "Ghi chú"
**(1) Phần mềm đúng SRS chưa?** SAI — §Inputs biểu mẫu chỉ có đúng một ô văn bản dài không bắt buộc tên "Mô tả" (`srs-fr-12-tv-chuyen-sau.md:560`; entity dòng 1393); web đặt ô này sai nhãn "Ghi chú" (trường vẫn có, chỉ sai tên nhãn).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác báo "thiếu Mô tả" (thực ra ô "Ghi chú" trên web chính là ô "Mô tả" bị sai nhãn); yêu cầu khớp SRS.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa: Dev đổi nhãn ô văn bản dài từ "Ghi chú" thành "Mô tả", không thêm/bớt trường (tránh trùng ô). Không cần sửa SRS. *(Evidence là video, không xem được ảnh tĩnh; chi tiết "web đang có ô nhãn Ghi chú" lấy từ phiếu gốc. Dù web sai nhãn hay thực sự thiếu ô, hướng xử lý đều là bảo đảm biểu mẫu có đúng một ô văn bản dài mang nhãn "Mô tả" — Dev kiểm lại trên màn hình thật.)*
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: đổi nhãn ô văn bản dài "Ghi chú" → "Mô tả" (bảo đảm biểu mẫu có đúng một ô mang nhãn "Mô tả").** **✅ BA duyệt 2026-07-24.**

---

### QLHSPLDN_03 (ý 3) — Biểu mẫu thêm/sửa thiếu trường "Lĩnh vực pháp lý"
**(1) Phần mềm đúng SRS chưa?** SAI — `linh_vuc_id` (Lĩnh vực pháp lý) đã có trong §Inputs biểu mẫu Thêm/Sửa — FK sang DANH_MUC, không bắt buộc (`srs-fr-12-tv-chuyen-sau.md:556`; entity dòng 1389) — nhưng web chưa hiển thị ô.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — trùng SRS. (Kết quả thực tế nêu biểu mẫu thêm mới thiếu ba trường: Lĩnh vực pháp lý, Mô tả, Tệp đính kèm; bản phiếu gốc chỉ xử lý "Mô tả", hai trường còn lại bổ sung theo evidence.)
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa: Dev thêm ô chọn "Lĩnh vực pháp lý" (dropdown tra DANH_MUC, không bắt buộc) vào biểu mẫu Thêm mới/Chỉnh sửa. Không cần sửa SRS. *(Phân biệt với QLHSPLDN_02 ý 2: ở đó là cột trên bảng danh sách — §Outputs chưa có nên cần bổ sung SRS; ở đây là ô nhập trên biểu mẫu — §Inputs đã có sẵn, chỉ Dev bổ sung màn hình.)*
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: thêm ô chọn "Lĩnh vực pháp lý" (dropdown tra DANH_MUC, không bắt buộc, `linh_vuc_id` §Inputs đã có) vào biểu mẫu Thêm/Sửa.** **✅ BA duyệt 2026-07-24.**

---

### QLHSPLDN_03 (ý 4) — Biểu mẫu thêm/sửa thiếu trường "Tệp đính kèm"
**(1) Phần mềm đúng SRS chưa?** SAI — `file_dinh_kem` (Tệp đính kèm) đã có trong §Inputs biểu mẫu Thêm/Sửa — kiểu file, không bắt buộc, ràng buộc "PDF/image, max 20MB" (`srs-fr-12-tv-chuyen-sau.md:562`); Processing Thêm mới bước 5 ghi "Upload file nếu có (max 20MB, quét virus)" (`srs-fr-12-tv-chuyen-sau.md:592`) — nhưng web chưa hiển thị ô.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — trùng SRS (cùng nhóm với Lĩnh vực pháp lý, Mô tả).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa: Dev thêm ô "Tệp đính kèm" (upload PDF/ảnh, tối đa 20MB, quét virus theo EC-FILE-01) vào biểu mẫu Thêm mới/Chỉnh sửa. Không cần sửa SRS.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: thêm ô "Tệp đính kèm" (upload PDF/ảnh ≤20MB, quét virus, `file_dinh_kem` §Inputs đã có) vào biểu mẫu Thêm/Sửa.** **✅ BA duyệt 2026-07-24.**

---

## Tổng kết cho BA (các kết luận đã duyệt 2026-07-24)

- **Hướng Dev sửa theo SRS (SRS đã đúng/đủ, web lệch):** 6 ý —
  - Bỏ cột "Số/Ký hiệu" ở bảng danh sách (QLHSPLDN_02 ý 1);
  - Bỏ trường "Số/Ký hiệu" ở biểu mẫu (QLHSPLDN_03 ý 1);
  - Thêm cột "Có tệp đính kèm" ở bảng danh sách — trường `co_file` §Outputs đã có (QLHSPLDN_02 ý 4);
  - Đổi nhãn "Ghi chú" → "Mô tả" ở biểu mẫu (QLHSPLDN_03 ý 2);
  - Thêm trường "Lĩnh vực pháp lý" ở biểu mẫu — `linh_vuc_id` §Inputs đã có (QLHSPLDN_03 ý 3);
  - Thêm trường "Tệp đính kèm" ở biểu mẫu — `file_dinh_kem` §Inputs đã có (QLHSPLDN_03 ý 4).
- **Hướng cập nhật SRS + Dev thêm cột:** 2 ý — thêm cột "Lĩnh vực pháp lý" và "Nguồn" vào §Outputs FR-X.1-04 (dòng 642-656) và web (QLHSPLDN_02 ý 2, ý 3).
- **Hướng không sửa (cải tiến ngoài phạm vi):** không có.

**Điểm cần sửa SRS (nếu BA duyệt):** `srs-fr-12-tv-chuyen-sau.md:642-656` — bổ sung hai trường đầu ra `linh_vuc` và `nguon` vào §Outputs FR-X.1-04. (Cả hai đã tồn tại trong entity nên không phát sinh trường dữ liệu mới, chỉ đồng bộ danh sách đầu ra với entity/§Inputs.) Ba trường web còn thiếu (`co_file`, `linh_vuc_id`, `file_dinh_kem`) **đã có sẵn** trong SRS (§Outputs/§Inputs) nên không sửa SRS, chỉ Dev bổ sung màn hình.

---

## Đối chiếu Kết quả thực tế (Sheet) ↔ hướng xử lý

| Case | Đối tác nêu (Kết quả thực tế) | SRS | Hướng |
|------|-------------------------------|-----|-------|
| QLHSPLDN_02 | Bảng thiếu cột "Lĩnh vực pháp lý" | §Outputs chưa có (entity/§Inputs có) | Sửa SRS + web |
| QLHSPLDN_02 | Bảng thiếu cột "Nguồn" | §Outputs chưa có (entity có) | Sửa SRS + web |
| QLHSPLDN_02 | Bảng thiếu cột "Có tệp đính kèm" | §Outputs đã có `co_file` (dòng 654) | Dev thêm theo SRS |
| QLHSPLDN_02 | Thừa cột "Số/ký hiệu" | Không có trong SRS | Dev bỏ |
| QLHSPLDN_03 | Biểu mẫu thiếu "Lĩnh vực pháp lý" | §Inputs đã có `linh_vuc_id` (dòng 556) | Dev thêm theo SRS |
| QLHSPLDN_03 | Biểu mẫu thiếu "Mô tả" | §Inputs đã có `mo_ta` (dòng 560) | Dev sửa nhãn/bảo đảm có ô |
| QLHSPLDN_03 | Biểu mẫu thiếu "Tệp đính kèm" | §Inputs đã có `file_dinh_kem` (dòng 562) | Dev thêm theo SRS |
| QLHSPLDN_03 | Thừa trường "Số/ký hiệu" | Không có trong SRS | Dev bỏ |
