# Bảng đối chiếu điều kiện — KHTHCTHTPLDN_08 (row 30) — Hành động nhanh trên dòng

**Kết luận:** **BA confirm** — sửa từ `Reject` ngày 27/07/2026 sau audit ([AUDIT-reject-tuan-4.md](../reverify-audit/audit-reject-2026-07-27/AUDIT-reject-tuan-4.md)). Quan sát của phiếu đúng; **SRS im lặng đúng chỗ đang tranh chấp** (nút nằm trên dòng hay ở trang chi tiết) nên không đủ căn cứ nói phiếu hiểu sai.

Phiếu mong trên **dòng của bảng danh sách** có: [Tạm dừng] khi Đang thực hiện, [Kích hoạt] khi Đã duyệt / Đã công bố, [Sửa] khi Dự thảo. Thực tế cột "Hành động" chỉ có 1 nút Xem — **đúng như phiếu mô tả**.

Về **chức năng nghiệp vụ**: không thiếu. `srs-fr-15-ct-htpldn.md` mô tả các nút vòng đời ở **thanh hành động của trang Chi tiết CT** — `:1136` [Kích hoạt], `:1138` [Tạm dừng], `:1132` nhóm nút khi Dự thảo — và QA đã kiểm **các nút đó có đủ, đúng theo từng trạng thái và đúng theo vai trò** tại trang chi tiết.

**Nhưng KHÔNG kết luận Reject được — kỳ vọng của phiếu lấy từ CHÍNH đặc tả:** bảng `#### Bang hanh dong theo trang thai CT` (`:1193`–`:1207`) map trạng thái → nút mà **không nói nút nằm ở đâu**:

- `:1202` `DA_DUYET | [Kich hoat] | DANG_THUC_HIEN` · `:1204` `DA_CONG_BO | [Kich hoat]` → khớp ý 2 của phiếu.
- `:1205` `DANG_THUC_HIEN | [Tam dung] | TAM_DUNG | Modal ly do` → khớp ý 1 của phiếu.
- `:1211` *"Sua/Xoa CT: chi khi DU_THAO"* → khớp ý 3 của phiếu.

Cột Hành động của bảng chỉ được mô tả là *"Hanh dong (conditional)"* (`:1113`) — **không liệt kê tập nút, không nói "conditional" theo tiêu chí gì**. Không có dòng nào trong v3.5 nói các nút này **không được** nằm trên dòng danh sách. ⇒ protocol §Ca biên: *"SRS chỉ nêu nghiệp vụ chung, app đáp ứng cách khác → `BA confirm`"*. Đã mở **BA-24**.

**Điểm bất đối xứng đưa kèm câu hỏi BA:** `:1211` gộp *"Sửa/Xóa CT: chỉ khi DU_THAO"*, mà ảnh đối tác cho thấy dòng Dự thảo **có** biểu tượng xóa nhưng **không có** Sửa. Env QA hiện không còn bản ghi Dự thảo nên chỉ ghi nhận từ ảnh đối tác, **chưa re-verify được → không dùng làm căn cứ chấm lỗi**, chỉ nêu để BA chốt cùng lúc.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/KHTHCTHTPLDN_08.jpg`) | Mình test (env nip.io, 27/07/2026 14:50–15:15) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Ảnh cho thấy `CB_NV_TW` ("Cán bộ NV Trung ương"), đơn vị BTP · TW | Đo **hai vai trò**: `cbnv_tw` (CB Nghiệp vụ - TW) và `cbpd_tw` (CB Phê duyệt - TW). Cần cả hai vì đặc tả phân quyền khác nhau cho từng nút | Không |
| Entity + trạng thái (state machine) | Ảnh có dòng ở Dự thảo (2 nút: xem + xóa), Đang thực hiện, Tạm dừng, Chờ phê duyệt, Đã công bố, Đã hủy, Hoàn thành — mỗi dòng chỉ 1 nút xem trừ dòng Dự thảo | 8 chương trình ở 4 trạng thái: **Đã duyệt** (5), **Đã công bố** (1), **Đang thực hiện** (1), **Hoàn thành** (1). Mở trang chi tiết của từng trạng thái để đọc thanh hành động | Không |
| Dữ liệu tiền đề | Danh sách có bản ghi ở nhiều trạng thái để so nút | Đủ bản ghi cho 3 trong 4 trạng thái mà phiếu nhắc: Đã duyệt và Đã công bố (phiếu mong [Kích hoạt]), Đang thực hiện (phiếu mong [Tạm dừng]). Trạng thái Dự thảo không có sẵn — đã đối chiếu bằng chính ảnh đối tác, ảnh đó cho thấy dòng Dự thảo có thêm nút xóa ⇒ cột này **có** thay đổi theo trạng thái | Không |
| Input / filter / giá trị nhập | Mở màn danh sách rồi đọc cột Hành động | Đọc nút trên từng dòng bằng mã lệnh (lấy cả nhãn trợ năng, không chỉ chữ hiện ra), rồi mở trang chi tiết từng trạng thái và đọc **toàn bộ nút trên trang** — kể cả nút nằm ở thanh cố định dưới đáy, ngoài vùng nội dung chính | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Nút hành động theo trạng thái)

- `partner-evidence/KHTHCTHTPLDN_08.jpg` — đã mở đọc: cột "Hành động" của đối tác, dòng Đang thực hiện / Tạm dừng / Chờ phê duyệt / Đã công bố / Đã hủy / Hoàn thành đều chỉ có biểu tượng con mắt; riêng 2 dòng **Dự thảo** có thêm biểu tượng thùng rác đỏ. Đây là bằng chứng chính cột này đã "conditional" theo trạng thái.
- `bug-reports/image/BUG-CT-danh-sach-thieu-loc-donvi-trangthai-va-cot-linhvuc.png` — đã mở đọc: cột Hành động trên môi trường QA, mọi dòng đúng 1 biểu tượng con mắt.
- `bug-reports/image/BUG-CT-chi-tiet-dau-trang-va-thanh-tien-trinh.png` — đã mở đọc: trang chi tiết `CT-20260721-0002` (Đang thực hiện), thấy rõ nút **[Tạm dừng]** ở thanh cố định góc dưới bên phải.

## Phương pháp thứ hai (bắt buộc)

- **Đọc nút ở phạm vi toàn trang, không chỉ vùng nội dung chính — đây là bước suýt dẫn tới kết luận sai.** Lần đọc đầu chỉ quét trong vùng nội dung và trả về 0 nút, dễ kết luận nhầm là "mất hết chức năng". Quét lại toàn trang thì thấy nút nằm trong thanh cố định dưới đáy màn hình. Ghi lại đây để dev và đối tác không lặp lại nhầm lẫn này.
- **Đối chiếu nút theo từng trạng thái — phép thử quyết định.** Mở trang chi tiết của 4 trạng thái, đọc thanh hành động:

  - **Đã duyệt** → thực tế [Công bố lên Cổng PLQG] · [Bắt đầu thực hiện]; đặc tả yêu cầu [Công bố] · [Kích hoạt] ⇒ khớp.
  - **Đã công bố** → thực tế [Hủy công bố] · [Bắt đầu thực hiện]; đặc tả yêu cầu [Hủy công bố] · [Kích hoạt] ⇒ khớp.
  - **Đang thực hiện** → thực tế [Tạm dừng] với tài khoản CB NV, [Tạm dừng] + [Hoàn thành] với tài khoản CB PD; đặc tả yêu cầu [Tạm dừng] · [Hoàn thành] ⇒ khớp.
  - **Hoàn thành** → thực tế không có nút; đặc tả không quy định nút nào vì đây là trạng thái kết thúc ⇒ khớp.

  ⇒ Khớp đủ. "Bắt đầu thực hiện" chính là [Kích hoạt] — `:1136` ghi nguyên văn nhãn nút là *"Bat dau thuc hien"*.
- **Đo lại bằng vai trò thứ hai để loại một kết luận sai suýt xảy ra.** Với `cbnv_tw`, chương trình Đang thực hiện chỉ có [Tạm dừng], thiếu [Hoàn thành] — thoạt nhìn giống lỗi. Nhưng `:264` bước 1 ghi *"Kiểm tra quyền **CB PD**"* (sửa 27/07: trước ghi `:262` — đó là dòng tiêu đề bảng) và `:274` ghi mã lỗi *"Chỉ CB Phê duyệt mới được hoàn thành CT"* ⇒ đây là hành động dành riêng cho Cán bộ phê duyệt. Đăng nhập `cbpd_tw` kiểm lại: nút **[Hoàn thành] xuất hiện đúng như đặc tả**. Hệ thống làm đúng, không có lỗi.
- **Đối chiếu đặc tả về vị trí nút — trích nguyên văn:** `srs-fr-15-ct-htpldn.md:1136` — *"| 24 | **action-bar** | [DA_DUYET/DA_CONG_BO] Kich hoat (gop tu MH-15.4) | button + modal | "Bat dau thuc hien" -> modal ... -> SET DANG_THUC_HIEN |"*; `:1138` — *"| 26 | **action-bar** | [DANG_THUC_HIEN] Tam dung | button (warning) + modal | Modal ly do -> SET TAM_DUNG |"*. Cả hai thuộc bảng *"Thanh phan man hinh -- **Trang Chi tiet CT**: Tab "Thong tin""*, không thuộc bảng danh sách.
- **Đối chiếu mô tả cột Hành động của bảng:** `:1113` chỉ ghi *"Hanh dong (conditional)"*, không liệt kê nút cụ thể. Ảnh của chính đối tác cho thấy dòng Dự thảo có thêm nút xóa ⇒ tính "conditional" đang hoạt động. Không có căn cứ nào trong v3.5 buộc các nút vòng đời phải nằm trên dòng.
