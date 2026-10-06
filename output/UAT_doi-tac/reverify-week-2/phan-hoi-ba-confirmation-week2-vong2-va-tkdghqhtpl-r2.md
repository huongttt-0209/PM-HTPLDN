# Phản hồi BA — 2 phiếu QA: UAT tuần 2 vòng 2 (4 case) + `TKDGHQHTPL_02` r2 (2 case)

**Ngày lập:** 30/07/2026
**Phiếu nguồn:** `Week4/Yêu cầu/ba-confirmation-needed-week-2-vong2.md` (row 8, 53, 58, 68 + 1 câu hỏi xuyên suốt + 2 ghi nhận phụ lục) · `Week4/Yêu cầu/ba-confirmation-needed-TKDGHQHTPL_02-r2.md` (row 47, 276)
**Quy trình áp dụng:** `docs/Reference/Fix bug KTĐL/QUY-TRINH-phan-tich-bug-nghiep-vu.md`
**Bản chấm chuẩn (`.md`):** `_bmad-output/planning-artifacts/srs-v3.5/` — `srs-v3.5.md`, `srs-fr-01-dashboard.md`, `srs-fr-03-dao-tao.md`, `srs-fr-04-chuyen-gia-tvv.md`, `srs-fr-08-danh-gia.md`, `CHANGELOG-v3-to-v3.5.md`
**Bản thiết kế màn hình:** `_bmad-output/planning-artifacts/dac-ta-man-hinh-chuc-nang-v2.md`
**Bản bàn giao (`.docx`):** `HTPLDN-PTYC-CT-v2.0.docx` — bàn giao 10/07/2026. Bản tuần 2 (`7.BTP_CPLQG_S7_2025_PM_L4_PMHTPLDN.docx`) **không có trong kho**; các mục trích dưới đây đã đối chiếu là nội dung có sẵn từ v1.0, giữ nguyên qua v2.0
**Sheet theo dõi:** tab `UAT_TGPL Doanh Nghiệp-tuần 2` (row 8, 53, 58, 68) · tab tuần 1 (row 47, 276)

**Tình trạng duyệt:** BA đã duyệt 3 điểm của phương án `SCR-III-03` ngày 30/07/2026 (đóng dấu tại mục tương ứng). Các mục còn lại chờ duyệt. **Sửa SRS là đợt tách biệt — chưa thực hiện ở lượt này.**

---

## Ghi chú phương pháp

**Phiếu QA chỉ tra `.md`, không tra bản `.docx` bàn giao** — đúng cái bẫy Pha 4 mục 3(a). Tra bổ sung làm **3/6 case đổi kết luận**:

| Case | Kết luận QA | Sau khi tra `.docx` |
|---|---|---|
| `QLKTLBG_02` | Cần BA chọn bộ cột | `.docx` 4.3.7.2.2 liệt kê đủ 9 cột → **Loại 4B, Dev bổ sung** |
| `TDHSTVV_14` | Kỳ vọng ngoài đặc tả, sửa Expected | `.docx` 4.4.5.2.2 ghi nguyên văn *"gửi thông báo… đến Người hỗ trợ"* → **Loại 4B, Dev bổ sung** |
| `DKTGMLTVV_03b` | Cần BA chọn bắt buộc/tùy chọn | `.docx` 4.4.3.2.2 STT 9, 10 = "Có", khớp `.md` → **Loại 1, không phải câu hỏi** |

**Hai đính chính kỹ thuật với phiếu QA:**

1. Tệp thiết kế `dac-ta-man-hinh-chuc-nang-v2.md` QA ghi *"không có trong repo"* — **có**, ở `_bmad-output/planning-artifacts/`. Đây là tệp mà `SCR-III-03:1908` trỏ tới qua dòng "UX-Spec ref".
2. Số dòng nhóm FR-03 lệch **+4** (`:739`→`:743`, `:765`→`:769`, `:1904`→`:1908`, `:1906`→`:1910`); `BR-RPT-01` ở `srs-v3.5.md:5625` chứ không phải `:5608`. Các trích `srs-fr-04`, `srs-fr-08`, `srs-fr-01` đều đúng.

**Không case nào thuộc diện Reject.** Cả 6 case, đơn vị kiểm thử ghi nhận đúng theo tài liệu được giao.

---

## Câu hỏi xuyên suốt — bảng "Thành phần màn hình" là danh sách đóng hay mô tả tóm tắt?

QA xin chọn (A) danh sách ĐÓNG hoặc (B) MÔ TẢ TÓM TẮT. Cả hai đều sai nếu áp toàn cục:

- **(A) chặt** buộc gỡ `Chuyên ngành` và `Số năm kinh nghiệm` khỏi form Tư vấn viên, trong khi `FR-IV-03 §Inputs` đánh dấu bắt buộc và `§Processing` bước 7 ghi hệ thống lưu hai trường đó (`srs-fr-04-chuyen-gia-tvv.md:304`, `:305`, `:323`). Gỡ ô nhập thì không có gì để lưu.
- **(B)** mở cửa cho mọi trường trong mô hình dữ liệu được hiển thị tùy ý, kể cả trường quản trị nội bộ. Không đo được đúng/sai nữa.

**→ Chốt: bảng "Thành phần màn hình" là DANH SÁCH ĐÓNG, nhưng "đóng" ràng buộc BẢN ĐẶC TẢ chứ không ràng buộc màn hình.** Khi trên màn hình có mục không nằm trong bảng:

| Tình huống | Kết luận | Ai làm |
|---|---|---|
| Mục **có căn cứ** ở `§Inputs` / `§Processing` / `§Outputs` / mô hình dữ liệu của chính FR đang xét | Bảng thành phần **bị sót** — phần mềm đúng | BA bổ sung vào bảng |
| Mục **không có căn cứ** ở bất kỳ đâu trong `.md` | Phần mềm **thừa** — lỗi thật | Dev gỡ |

Đây không phải luật mới — đúng tầng 3 cây trọng tài (*"ô nhập chỉ tồn tại nếu có bước xử lý dùng tới"*), chỉ chưa ai phát biểu chiều ngược lại. Ghi thành một câu vào quy ước chung.

**Về vế "giống với thiết kế" trong Kết quả mong đợi:** giữ nguyên tắc BA chốt 15/07/2026 — `.md` là căn cứ nghiệm thu. Bằng chứng bản thiết kế nhóm IV đã lỗi thời: `dac-ta-man-hinh-chuc-nang-v2.md:2305` vẫn còn trường *"Địa bàn hoạt động \*"* bắt buộc, trong khi v3.1 đã bỏ hẳn với căn cứ NĐ 77/2008 Điều 19. **Ngoại lệ:** khi `.md` tự trỏ sang bản thiết kế bằng dòng "UX-Spec ref" thì phần được trỏ tới vẫn có hiệu lực — trường hợp `SCR-III-03` dưới đây.

---

## `QLKTLBG_02` (row 8) — thiếu 3 cột ở màn Kho tài liệu / Bài giảng *(BA-V2-1)*

**(1) Phần mềm đúng `.md` chưa?** **SAI.** `SCR-III-03` (`srs-fr-03-dao-tao.md:1904-1910`) không tự liệt kê cột nào — ghi *"Loại màn hình: Danh sách + Preview panel"* rồi ủy quyền ở `:1908`: **"UX-Spec ref: dac-ta-man-hinh-chuc-nang-v2.md — MH-03.3"**. Mở đúng chỗ được trỏ tới (§MH-03.3 Thành phần 3, dòng `1625-1637`) có **9 cột**: `col_anh_dai_dien` · `col_ten_bai_giang` · `col_loai` · `col_linh_vuc` · `col_kich_thuoc` · `col_cong_khai` · `col_nguoi_tao` · `col_ngay_tao` · `col_hanh_dong`. Web có 6, thiếu đúng **Ảnh xem trước · Lĩnh vực · Người tạo**.

**(1b) Bản `.docx` nói gì?** Trùng khớp — mục **4.3.7.2.2** bảng *"Cột dữ liệu trong bảng kết quả"* STT 5→13 liệt kê đúng 9 cột đó.

**(2) Đối tác yêu cầu khác gì?** Không khác gì. Cả 3 cột đều có sẵn trong mô hình dữ liệu `BAI_GIANG`: `anh_dai_dien` (`srs-v3.5.md:2477`), `linh_vuc_ids` (`:2482`), `created_by` (`:2486`).

**(3) Có bắt buộc không?** Có. Màn hình đã có bộ lọc "Lĩnh vực pháp lý" nhưng không có cột tương ứng — lọc xong không đọc được kết quả lọc theo tiêu chí gì. *Người tạo* cần cho phân định trách nhiệm giữa các đơn vị dùng chung kho.

**→ Kết luận: Loại 4B — `.md` bị sót bảng cột, phần mềm thiếu 3 cột. Dev bổ sung 3 cột. Dev action: Có. Sheet: Giữ xử lý. Không phản hồi đối tác** (lỗi thật sẽ sửa đúng điều họ yêu cầu).

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v2.0.docx`, bàn giao 10/07/2026 (nội dung có từ v1.0) |
| Trích `.docx` | **4.3.7.2.2** — bảng "Cột dữ liệu trong bảng kết quả", STT 5 *Ảnh xem trước*, STT 8 *Lĩnh vực*, STT 11 *"Người tạo — Họ tên người tạo bản ghi"* |
| Trích `.md` | `srs-fr-03-dao-tao.md:1904-1910` — **không có bảng cột**, ủy quyền qua "UX-Spec ref" sang `dac-ta-man-hinh-chuc-nang-v2.md:1625-1637` (9 cột) |
| Hướng | **B** — yêu cầu còn giá trị, bản gốc thiếu. Cây trọng tài: mục được `.md` tự trỏ tới vẫn hiệu lực; 3 trường đều có trong thực thể |
| Dev action | **Có** — bổ sung 3 cột |
| Doc action | BA nội hóa bảng cột vào thân `SCR-III-03` (phương án dưới) |
| Sheet | **Giữ xử lý** |

> **Đính chính nhận định QA:** phiếu QA xếp *Lĩnh vực* và *Người tạo* là "SRS im lặng". Cả hai đều có quy định, chỉ nằm ở tệp được `SCR-III-03` trỏ tới.

**Trường "Khóa học liên kết" (`:769`):** QA hỏi có thành cột không — **không**. Không có ở MH-03.3 lẫn `.docx`. Bài giảng dùng lại ở nhiều khóa, một ô cột không chứa nổi.

### Phương án cập nhật SRS — `SCR-III-03`

**Vì sao nội hóa thay vì chỉ sửa dòng "UX-Spec ref":** mục MH-03.3 đã bị bản thiết kế đánh dấu **DEPRECATED v2.1** (*"/dao-tao/bai-giang → REDIRECT /dao-tao/khoa-hoc"*), trong khi SRS v3.5 (chốt 2026-07-25, mới hơn) vẫn giữ là sub-menu 4 và phần mềm vẫn có màn này.

**Vị trí:** thay toàn bộ `srs-fr-03-dao-tao.md:1904-1910` (7 dòng). Viết theo khuôn "Thành phần N — …" của `SCR-III-01` / `SCR-III-02` kề bên. Nội dung `[STT66 UAT 2026-06-02]` hòa vào bảng, giữ nhãn xuất xứ từng dòng. Sửa luôn phần chữ không dấu ở tiêu đề và 3 dòng đầu.

**Nội dung đề xuất:**

> `### SCR-III-03: Kho tài liệu / Bài giảng (sub-menu 4)` `[v3.5 — đẩy số sub-menu do SCR-III-00 thêm mới]` `[BA chốt 2026-07-30 — QLKTLBG_02: nội hóa bảng cột từ MH-03.3, bổ sung 3 cột Ảnh đại diện · Lĩnh vực · Người tạo]`
>
> **Loại màn hình:** Danh sách + Bảng xem trước. 3 loại tài liệu: Slide (PPTX), PDF, Video (nhúng YouTube)
> **FR sử dụng:** FR-III-07 (thêm/sửa/xóa bài giảng), FR-III-08 (tìm kiếm và lọc)
> **UX-Spec ref:** `dac-ta-man-hinh-chuc-nang-v2.md` — MH-03.3 *(mục đã ngừng dùng ở bản thiết kế; giữ làm tham chiếu lịch sử — khi hai bên khác nhau thì lấy mục này)*
>
> **Thành phần 1 — Đường dẫn điều hướng:** "Trang chủ › Đào tạo, tập huấn › Kho tài liệu"
>
> **Thành phần 2 — Tiêu đề + Hành động chính:** Tiêu đề "Kho tài liệu & bài giảng" · Nút "+ Thêm mới" (chính) · Nút "Xuất Excel" (phụ — xuất theo bộ lọc hiện tại, tối đa 10.000 dòng theo BR-DATA-06)
>
> **Thành phần 3 — Thanh lọc và tìm kiếm:** Ô từ khóa "Tìm theo tên bài giảng" · Lọc Loại tài liệu (Tất cả / Slide / PDF / Video) · Lọc Lĩnh vực pháp luật (chọn nhiều, nguồn DANH_MUC loại LINH_VUC_PL) · Lọc Công khai (Tất cả / Đã / Chưa) `[STT66]` · Lọc Từ ngày / Đến ngày theo ngày tạo · Nút "Tìm kiếm" (chính) · "Xóa bộ lọc" (mờ)
>
> **Thành phần 4 — Bảng tài liệu (9 cột):**
>
> | Cột | Nguồn | Mô tả |
> |-----|-------|-------|
> | Ảnh đại diện | `anh_dai_dien` | Ảnh thu nhỏ. Rỗng hoặc tải lỗi → biểu tượng mặc định theo loại tài liệu (S3-9) |
> | Tên bài giảng | `ten_bai_giang` | Liên kết — mở Bảng xem trước |
> | Loại tài liệu | `loai` | Nhãn màu: Slide · PDF · Video |
> | Lĩnh vực | `linh_vuc_ids` → DANH_MUC | Dạng thẻ, tối đa 3 thẻ + "+N"; rỗng → "—" |
> | Dung lượng | `kich_thuoc_file` | Định dạng KB/MB; loại Video → "—" |
> | Công khai | `cong_khai` | **Badge** "Đã công khai" / "Chưa công khai" — chỉ hiển thị, không bật tắt tại dòng `[STT66]` |
> | Người tạo | `created_by` → TAI_KHOAN | Họ tên người tạo; rỗng → "—" |
> | Ngày tạo | `created_at` | dd/mm/yyyy; sắp xếp được, mặc định mới nhất trước |
> | Hành động | — | Xem trực tuyến · Tải về (chỉ Slide/PDF) · Sửa · Xóa (xóa mềm, có hộp xác nhận) |
>
> **Thành phần 5 — Phân trang:** mặc định 20 dòng/trang; cho phép 10/20/50/100.
>
> **Thành phần 6 — Bảng xem trước:** Slide/PDF xem trực tiếp trong trình duyệt; Video nhúng khung YouTube; định dạng không xem được → "Không thể xem trực tuyến" + nút "Tải về". Khối thông tin kèm theo hiển thị **Ảnh đại diện**, **Ngày công khai** (`thoi_gian_dang_tai`, theo BR-PUBLIC-03), Mô tả công khai, Tệp đính kèm công khai `[STT66]`.
>
> **Quy tắc nghiệp vụ:** lọc theo đơn vị sở hữu `don_vi_id` theo BR-AUTH-08 · công khai theo BR-PUBLIC-01..03, thao tác bật/tắt ở biểu mẫu thêm/sửa chứ không tại dòng danh sách · **không** đưa "Khóa học liên kết" thành cột.

**Ba điểm — ✅ BA DUYỆT 30/07/2026 theo đúng đề xuất ở cột cuối:**

| # | Điểm | Hai nguồn nói gì | Chốt |
|---|---|---|---|
| 1 | Nhãn cột ảnh | `.docx` STT 5 và Expected của đối tác gọi *"Ảnh xem trước"*; MH-03.3 và `.md` gọi trường là `anh_dai_dien` | **"Ảnh đại diện"** — đồng bộ tên trường và nhãn ở Bảng xem trước. Mô tả trong `.docx` chỉ tả trường hợp dự phòng nên kém chính xác. Đổi lại: đưa `QLKTLBG_02` vào danh sách mã cần sửa Expected khi bàn giao `.docx` mới |
| 2 | Cột Công khai là badge hay ô chuyển | `.docx` 4.3.7.2.3 STT 6 và MH-03.3 nói **ô chuyển tại dòng**; `.md` STT66 (chốt sau) nói **badge** | **Badge** — chốt sau đè chốt trước. Nêu rõ để Dev không dựng công tắc tại dòng. Cập nhật `.docx` STT 6 |
| 3 | Nút "Xuất Excel" | Có ở MH-03.3 và `.docx` STT 7; `.md` **không** nhắc | Đưa vào đặc tả, nhưng **tách khỏi phạm vi sửa lỗi `QLKTLBG_02`** |

> **Lưu ý điểm 3:** nút "Xuất Excel" **chưa có** trong `.md` — đưa vào là **bổ sung nội dung mới**, không phải chép lại thứ `.md` đã có. Nếu phần mềm chưa có nút thì đây là **việc mới cho Dev**. Phải kiểm phần mềm rồi tách thành mục riêng khi giao việc, để tiến độ sửa 3 cột không bị kéo theo.

**Việc kèm — lệch tên trường dung lượng:** `FR-III-07 §Outputs` mục 6 (`:771`) gọi `dung_luong`, thực thể `BAI_GIANG` (`srs-v3.5.md:2475`) gọi `kich_thuoc_file`. Thống nhất theo tên thực thể, nhãn hiển thị giữ "Dung lượng". Không mở việc cho Dev.

**Phát hiện kèm — cơ chế "UX-Spec ref" nhóm III hỏng rộng hơn:** `SCR-III-00` (`:1796`), `SCR-III-01` (`:1804`), `SCR-III-02` (`:1898`) đều trỏ sang `dac-ta-man-hinh-chuc-nang-v3.5.md` — **tệp không tồn tại** (kho chỉ có bản `v2`). Ba mục đó tự viết đủ nên chưa gãy, nhưng dòng tham chiếu là chỉ dẫn sai. Đề nghị rà cả 6 dòng "UX-Spec ref" của tệp trong cùng đợt.

---

## `DKTGMLTVV_03` (row 53) — bộ trường nhóm "Nghề nghiệp" form Tư vấn viên *(BA-V2-2)*

### Bối cảnh — `.docx` mô tả HAI màn hình, `.md` gộp làm MỘT

Vòng 1 đối tác báo nhóm 2 **THIẾU** 2 trường, Dev bổ sung, kiểm lại Đạt. Vòng 2 cũng người đó báo ngược lại — **THỪA** trường. Web thực tế có 11 trường. Nguyên nhân:

| | Bản `.docx` | Bản `.md` |
|---|---|---|
| Cán bộ thêm / sửa Tư vấn viên | **4.4.1.3.2** — 5 nhóm, nhóm 2 có **12 trường** (STT 11→22) | `SCR-IV-02` — 5 nhóm, nhóm 2 có **9 mục** (3.0a→3.7) |
| Người hỗ trợ đăng ký ứng viên | **4.4.3.2.2** — màn **riêng**, 4 nhóm, nhóm 2 chỉ **3 trường** | Không có màn riêng — `FR-IV-03` dùng chung `SCR-IV-02` |

Đối tác kiểm với vai trò Người hỗ trợ nên đối chiếu 4.4.3.2.2 và thấy 3 trường; web phục vụ Người hỗ trợ bằng đúng form cán bộ nên ra 11. **Cả hai vòng họ đều trích đúng**, chỉ là trích hai mục khác nhau.

Thêm một chi tiết: `.docx` 4.4.3.2.1 tự ghi *"Hiện chưa có nguyên mẫu giao diện (prototype) cho màn hình này. Bản mô tả… được lập theo đặc tả yêu cầu phần mềm (SRS)."* — vế *"giống với thiết kế"* trong Expected không có đối tượng để đối chiếu.

### `DKTGMLTVV_03a` — bộ trường nhóm "Nghề nghiệp" lấy theo nguồn nào?

**(1) Phần mềm đúng `.md` chưa?** **ĐÚNG.** 9 trường theo `SCR-IV-02` mục 3.0a→3.7 (`:1495-1504`); 2 trường còn lại theo `FR-IV-03 §Inputs` `:304`, `:305` và `§Processing` bước 7 `:323`.

**(1b) Bản `.docx` nói gì?** Nói **ít hơn** `.md` — ngược chiều so với ~60 ca tuần 2–3. Mục 4.4.3.2.2 nhóm 2 chỉ có *Trình độ chuyên môn · Chuyên ngành đào tạo · Số năm kinh nghiệm*.

**(2) Đối tác yêu cầu khác gì?** Rút nhóm 2 còn 3 trường.

**(3) Có bắt buộc không?** **Không — và làm theo thì vi phạm quy định pháp luật đã ghi trong đặc tả.** `SCR-IV-02` mục 3.5: *"Số thẻ hành nghề — Bắt buộc nếu Loại = Tư vấn viên (theo NĐ 77/2008 Đ.20)"*. Rút còn 3 trường sẽ gỡ ô này khỏi màn Người hỗ trợ đăng ký, tức hồ sơ ứng viên Tư vấn viên nộp lên không có số thẻ — cán bộ không có gì để kiểm nhóm tiêu chí Pháp lý. Cùng lý do với *Tệp thẻ hành nghề* (`FR-IV-03 §Inputs` #18). Thêm nữa, rút trường lúc này là đảo ngược đúng việc Dev vừa làm ở vòng 1.

**→ Kết luận: Loại 4A — `.docx` mô tả thiếu so với bản gốc, phần mềm đúng. Dev action: Không (riêng ý này). Sheet: Giữ xử lý (case lai, xem tổng hợp cuối mục).**

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v2.0.docx`, bàn giao 10/07/2026 |
| Trích `.docx` | **4.4.3.2.2** Nhóm 2 "Thông tin chuyên môn" — chỉ STT 8 *Trình độ chuyên môn*, 9 *Chuyên ngành đào tạo*, 10 *Số năm kinh nghiệm* |
| Trích `.md` | `srs-fr-04-chuyen-gia-tvv.md:1495-1504` (9 mục) + `:304`, `:305`, `:323` (2 trường nữa) |
| Hướng | **A** — `.docx` mô tả thiếu; `.md` đầy đủ và có căn cứ pháp lý cho phần dôi ra |
| Dev action | **Không** |
| Doc action | Bên soạn tài liệu bàn giao cập nhật 4.4.3.2.2 |
| Sheet | Giữ xử lý (do ý 2b, 2c còn việc Dev) |

**Việc kèm cho BA:** bảng `SCR-IV-02` nhóm 2 đang **sót** `Chuyên ngành` và `Số năm kinh nghiệm` — bổ sung vào `:1495-1504`.

**Phản hồi gửi đối tác:** *"Về bộ trường nhóm Thông tin nghề nghiệp: các trường đang hiển thị đều thuộc phạm vi hồ sơ ứng viên tư vấn viên theo đặc tả, trong đó Số thẻ hành nghề và Tệp thẻ hành nghề là thành phần bắt buộc đối với ứng viên Tư vấn viên theo Điều 20 Nghị định số 77/2008/NĐ-CP. Xác nhận bản mô tả trong tài liệu bàn giao đang thiếu so với đặc tả, sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần."*

### `DKTGMLTVV_03b` — "Chuyên ngành" và "Số năm kinh nghiệm": bắt buộc hay tùy chọn?

**(1) Phần mềm đúng `.md` chưa?** **SAI.** `FR-IV-03 §Inputs` — đúng chức năng Người hỗ trợ đăng ký — đánh dấu cả hai là bắt buộc: `:304` (`chuyen_nganh | text | Y`), `:305` (`so_nam_kinh_nghiem | number | Y`). QA bấm Lưu trên form trống: phần mềm **không** báo thiếu, tức đang coi là tùy chọn.

**(1b) Bản `.docx` nói gì?** **Y hệt `.md`.** Mục 4.4.3.2.2 STT 9 và 10, cột Bắt buộc đều ghi **"Có"**. Không có tranh chấp tài liệu.

QA tưởng `.md` tự mâu thuẫn. Bốn nguồn xếp cạnh nhau cho thấy không:

| Nguồn | Ngữ cảnh | Chuyên ngành | Số năm kinh nghiệm |
|---|---|---|---|
| `.md` `FR-IV-03 §Inputs` `:304`, `:305` | **Người hỗ trợ đăng ký ứng viên mới** | Bắt buộc | Bắt buộc |
| `.docx` 4.4.3.2.2 STT 9, 10 | **Người hỗ trợ đăng ký ứng viên mới** | Bắt buộc | Bắt buộc |
| `.md` `FR-IV-04 §Inputs` `:382` | Cập nhật năng lực hồ sơ đã có | Tùy chọn | — |
| `.docx` 4.4.1.3.2 STT 12 | Cán bộ sửa hồ sơ đã có | — | Tùy chọn |

Hai dòng đầu đúng ngữ cảnh test case và khớp nhau. Hai dòng cuối thuộc ngữ cảnh khác nên tùy chọn là hợp lý. Bảng `SCR-IV-02` không liệt kê hai trường chỉ vì bị sót — đã xử ở 2a.

**(2) Đối tác yêu cầu khác gì?** Đối tác không nêu ý này; QA phát hiện khi kiểm ràng buộc.

**(3) Có bắt buộc không?** **Có.** Hai trường là căn cứ để cán bộ chấm nhóm tiêu chí *Năng lực chuyên môn* ở bước thẩm định (`SCR-IV-03` mục 15). Thiếu thì cán bộ phải trả về yêu cầu bổ sung — thêm một vòng cho cả hai bên.

**→ Kết luận: Loại 1 — phần mềm sai đặc tả. Dev đặt hai trường là bắt buộc trên luồng Người hỗ trợ đăng ký ứng viên mới; giữ tùy chọn trên luồng cán bộ sửa hồ sơ đã có. Dev action: Có. Sheet: Giữ xử lý. Không phản hồi.**

> **Chặn Dev — mô hình dữ liệu thiếu hẳn trường `chuyen_nganh`.** `FR-IV-03 §Processing` bước 7 (`:323`) ghi hệ thống lưu nó, `FR-IV-04` (`:382`) cho cập nhật — nhưng bảng thực thể `TU_VAN_VIEN` (`:134-157`, đủ 23 dòng) **không có dòng nào tên `chuyen_nganh`**. **Phải sửa SRS trước khi giao việc cho Dev.**

### Phương án cập nhật SRS — bổ sung trường `chuyen_nganh`

**Không phải đề xuất mới — bốn nơi đang dùng mà không có chỗ lưu:**

| Nơi dùng | Trích dẫn | Dùng thế nào |
|---|---|---|
| `FR-IV-03 §Inputs` mục 11 | `srs-fr-04-chuyen-gia-tvv.md:304` | Người hỗ trợ nhập, bắt buộc |
| `FR-IV-03 §Processing` bước 7 | `:323` | Ghi vào bản ghi `TU_VAN_VIEN` khi tạo hồ sơ |
| `FR-IV-04 §Inputs` mục 3 | `:382` | Cập nhật năng lực, tùy chọn |
| Nhóm XII tiêu thụ ngược | `srs-fr-12-tv-chuyen-sau.md:1168` | Ô "Chuyên môn" — *"ưu tiên `chuyen_nganh`; nếu trống thì ghép tên các lĩnh vực"* |

Dòng cuối đáng lưu ý: một nhóm FR khác đã **đọc** trường này. Không có chỗ lưu thì ô "Chuyên môn" của nhóm XII vĩnh viễn rơi vào nhánh dự phòng, không ai phát hiện vì nhánh đó vẫn hiển thị được.

**Thực thể `TU_VAN_VIEN` có 3 bản chép trong kho, không phải 1:**

| # | Tệp | Vị trí | Việc |
|---|---|---|---|
| 1 | `srs-fr-04-chuyen-gia-tvv.md` | Bảng thực thể `§Inputs`, giữa `:144` (`trinh_do`) và `:145` (`chung_chi`) | Chèn dòng, đánh số **`10a`** |
| 2 | `srs-fr-04-chuyen-gia-tvv.md` | Khối sơ đồ quan hệ `:1913-1926` (đã có `so_nam_kinh_nghiem`, `chuc_vu`, `noi_cong_tac`) | Chèn `text chuyen_nganh` |
| 3 | `srs-fr-04-chuyen-gia-tvv.md` | Mục `### TU_VAN_VIEN (owned)` `:2001+`, sau `noi_cong_tac` (`:2019`) | Chèn dòng |
| 4 | `srs-v3.5.md` | `§3.4.3.4` `:1700+`, sau `noi_cong_tac` (`:1719`) — **baseline cũng thiếu** | Chèn dòng |
| 5 | `srs-fr-04-chuyen-gia-tvv.md` | Bảng Lịch sử thay đổi đầu tệp (`:19-25`) | Thêm dòng nhật ký 30/07/2026 |

**Hai chỗ KHÔNG đụng, đã dò ngược tiêu đề để xác định chủ sở hữu:**
- `srs-v3.5.md:2588` và `:3874` có chuỗi `chuyen_nganh` nhưng thuộc **`§3.4.3.25 GIANG_VIEN`**.
- Sơ đồ quan hệ `srs-v3.5.md:3748` chỉ liệt kê 6 trường khóa, vốn không có cả `chuc_vu` lẫn `noi_cong_tac` — giữ nguyên.

**Định nghĩa trường đề xuất** — bám khuôn ba trường nghề nghiệp đã có:

| Thuộc tính | Giá trị | Vì sao |
|---|---|---|
| Tên | `chuyen_nganh` | Đúng tên ba nơi đang gọi |
| Kiểu | text | Theo `:304` |
| Bắt buộc ở thực thể | **N** | Đúng tiền lệ `so_nam_kinh_nghiem`: thực thể **N**, `FR-IV-03 §Inputs` **Y**. Ràng buộc bắt buộc gắn vào luồng Người hỗ trợ đăng ký, không gắn vào chỗ lưu — để Y ở thực thể sẽ chặn mọi hồ sơ cán bộ tạo trực tiếp qua FR-IV-01/02 |
| Ràng buộc | Max 200 ký | Cho khớp `chuc_vu`. **Điểm tôi tự chọn** — không nguồn nào nêu độ dài; BA muốn bỏ như `GIANG_VIEN.chuyen_nganh` cũng được |
| Mô tả | *"Chuyên ngành đào tạo theo bằng cấp — bắt buộc nhập khi Người hỗ trợ đăng ký ứng viên (FR-IV-03), tùy chọn khi cán bộ sửa hồ sơ đã có (FR-IV-04)"* | Ghi thẳng khác biệt hai luồng để lần sau không ai tưởng `.md` tự mâu thuẫn |
| Nhãn xuất xứ | `` `[BA chốt 2026-07-30 — DKTGMLTVV_03 UAT tuần 2 vòng 2]` `` | Theo khuôn nhãn ngày tháng của tệp |

Dùng số **`10a`** thay vì chèn số nguyên mới để không phải đánh số lại 13 dòng phía sau — tệp đã dùng cách này ở `1b` và ở `12a/12b/12c` của `BAI_GIANG`; giữ số cũ thì mọi trích dẫn `file:dòng` hiện có vẫn trỏ đúng.

**Không kéo theo việc khác:** không đụng Phụ lục 1 (mẫu xuất QĐ 1322/QĐ-BTP không có cột Chuyên ngành), không đụng `.docx` (4.4.3.2.2 STT 9 đã có), không đổi mã lỗi.

### `DKTGMLTVV_03c` — form có 5 nhóm hay 6 nhóm?

**(1) Phần mềm đúng `.md` chưa?** **SAI ở bố cục, ĐÚNG ở trường.** Hai trường `Số QĐ công bố` / `Ngày QĐ công bố` hợp lệ — có trong thực thể `TU_VAN_VIEN` (`:155`, `:156`, `[CR-03]`) và mẫu xuất Phụ lục 1 (`:2212`, `:2213`). Nhưng web dựng thành **nhóm thứ 6 riêng**, còn `SCR-IV-02:1476` ghi **5 nhóm**.

**(1b) Bản `.docx` nói gì?** Trả lời dứt điểm — mục **4.4.1.3.2** đặt cả hai trường vào **Nhóm 2 Thông tin nghề nghiệp**, STT 21 và 22, ngay sau *Chức vụ hiện tại* / *Nơi công tác hiện tại*. Giữ đúng 5 nhóm.

**(2) Đối tác yêu cầu khác gì?** Đối tác không nêu; QA phát hiện khi kiểm.

**(3) Có bắt buộc không?** Có — hai trường phục vụ cột 11 của mẫu xuất theo Phụ lục 1 QĐ 1322/QĐ-BTP.

**→ Kết luận: Loại 1 — giữ hai trường, chuyển vào Nhóm 2; form về đúng 5 nhóm. Dev action: Có (gộp nhóm, không gỡ trường). Sheet: Giữ xử lý. Không phản hồi.**

**Việc kèm cho BA:** bổ sung hai trường vào bảng `SCR-IV-02` nhóm 2 (`:1495-1504`), đặt sau mục 3.7. Tiền lệ trong cùng tệp: `SCR-IV-NEW-02` mục 5.1 (`:1683`) đã đặt *"Số quyết định công bố — Tùy chọn"* cho màn Tổ chức tư vấn.

### Tổng hợp `DKTGMLTVV_03`

Case lai: **2a Loại 4A** (không sửa) · **2b Loại 1** (Dev sửa) · **2c Loại 1** (Dev gộp nhóm). Còn việc cho Dev → **Sheet: Giữ xử lý.** Phản hồi chỉ viết cho ý 2a.

Ý `Open` sẵn có (*"Tổ chức hành nghề chính" bị đặt bắt buộc*) — xem mục "Phát hiện thêm", có tình tiết QA chưa nắm.

---

## `QLHSTVV_03` (row 58) — thành phần thẻ "Hồ sơ" màn chi tiết Tư vấn viên *(BA-V2-3)*

### `QLHSTVV_03a` — thẻ "Hồ sơ" là danh sách đóng hay mô tả tóm tắt? Số nhóm là 5 hay 6?

**(1) Phần mềm đúng `.md` chưa?** **ĐÚNG.** Áp quy tắc đã chốt ở Câu hỏi xuyên suốt: dòng `:1556` viết trong **một ô bảng**, dạng liệt kê rút gọn `(a)…(f)`, khác hẳn dạng bảng đánh số từng phần tử của `SCR-IV-02`. Bằng chứng nằm trong chính nó: nhóm (b) chỉ ghi *"chức vụ + nơi công tác + trình độ, chứng chỉ, số thẻ, kinh nghiệm"*, bỏ qua `Bằng cấp chi tiết` và `Chứng chỉ chi tiết` — hai mục `SCR-IV-02` mục 3.3, 3.4 quy định có trong hồ sơ và không ai coi là thừa.

Về số nhóm: `:1556` ghi **6 nhóm**, trong đó *"(f) Thông tin công khai — chỉ hiển thị khi `cong_khai=1`"*.

**(1b) Bản `.docx` nói gì?** Mục **4.4.11.2.2** ghi *"Thẻ 'Hồ sơ' — nội dung chỉ xem, tổ chức thành **5 nhóm** thu gọn"* rồi liệt kê đúng 5, **thiếu hẳn nhóm (f)**.

**(2) Đối tác yêu cầu khác gì?** Expected ghi *"hiển thị 5 nhóm giống với thiết kế"* — đúng theo `.docx` họ cầm. Giả thuyết của QA (*"5 nhóm là trường hợp hồ sơ chưa công khai"*) hợp lý nhưng không phải nguyên nhân chính.

**(3) Có bắt buộc không?** Nhóm (f) cần cho việc theo dõi trạng thái công khai trên Cổng pháp luật quốc gia — giữ.

**→ Kết luận: Loại 4A cho vế số nhóm — phần mềm đúng, `.docx` cần bổ sung nhóm "Thông tin công khai". Đồng thời BA ghi rõ `:1556` là mô tả rút gọn ở cấp NHÓM, không phải danh sách đóng ở cấp trường. Dev action: Không (riêng ý này). Sheet: Giữ xử lý (case lai).**

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v2.0.docx`, bàn giao 10/07/2026 |
| Trích `.docx` | **4.4.11.2.2** — *"Thẻ 'Hồ sơ' — nội dung chỉ xem, tổ chức thành 5 nhóm thu gọn"*, liệt kê Thông tin cá nhân · Nghề nghiệp · Tổ chức · Lĩnh vực · Tệp đính kèm |
| Trích `.md` | `srs-fr-04-chuyen-gia-tvv.md:1556` — *"6 nhóm thu gọn được, chỉ đọc"*, thêm *"(f) Thông tin công khai — chỉ hiển thị khi `cong_khai=1`"* |
| Hướng | **A** — `.docx` chưa theo kịp `.md`; phần mềm đúng |
| Dev action | **Không** |
| Doc action | Bên soạn tài liệu bàn giao bổ sung nhóm (f) vào 4.4.11.2.2 |
| Sheet | Giữ xử lý (do ý 3b, 3c còn việc Dev) |

**Về mục "Số quyết định (công nhận)" đối tác báo thừa — chưa kết luận được.** Cả `.md` `:1556` lẫn `.docx` đều không đặt mục này trong nhóm Nghề nghiệp, nên đối tác ghi nhận đúng. Nhưng bản QA kiểm lại **không thấy mục đó ở đâu cả**, kể cả trên bản ghi có số quyết định thật (`QĐ-8017/QĐ-BTP`). Chênh lệch giữa ảnh đối tác và bản QA kiểm là **lệch bản triển khai giữa hai môi trường** — cùng gốc bệnh với `QLKTLBG_03` và `DKTGKH_07` ở `phan-hoi-27-bug-reopent-lo-2.md`. Chờ môi trường kiểm thử chạy đúng bản bàn giao.

### `QLHSTVV_03b` — không hiển thị ở thẻ Hồ sơ thì tra "Số quyết định công nhận" ở đâu?

**(1) Phần mềm đúng `.md` chưa?** **`.md` bỏ trống.** Trường bắt buộc nhập khi Cán bộ Phê duyệt duyệt hồ sơ (`FR-IV-07 §Inputs` `:583`, mã lỗi `ERR-PD-05` `:616`), có tên trong Phụ lục 1 (`:2027`) — nhưng không mục nào của màn chi tiết hiển thị nó.

**(1b) Bản `.docx` nói gì?** Cũng không nêu. Không có tranh chấp tài liệu.

**(2) Đối tác yêu cầu khác gì?** Đối tác không nêu; QA đặt câu hỏi.

**(3) Có bắt buộc không?** Có — dữ liệu pháp lý của quyết định công nhận, không tra được thì không đối chiếu được hồ sơ.

**→ Kết luận: Loại 2 — bổ sung đặc tả rồi Dev làm theo. Dev action: Có. Sheet: Giữ xử lý. Không phản hồi.**

**Phương án xử lý (cập nhật SRS):** đưa "Số quyết định công nhận" vào **thẻ thông tin chính ở đầu trang**, không đưa vào thẻ "Hồ sơ". `SCR-IV-03` mục 3 (`:1543`) đã quy định thẻ đầu trang hiển thị *Ảnh chân dung + Họ tên + Mã tư vấn viên + Trạng thái + Điểm đánh giá trung bình + **Ngày công nhận***. Số quyết định và ngày công nhận là hai vế của cùng một quyết định — tách ra hai chỗ là vô lý. Hiển thị khi hồ sơ đã qua phê duyệt, để trống ở các trạng thái trước.

Lý do không đưa vào thẻ "Hồ sơ": thẻ đó phản chiếu **hồ sơ ứng viên tự khai**, còn số quyết định là **kết quả xử lý của cơ quan** — trộn hai loại dữ liệu sẽ khiến người đọc tưởng ứng viên tự khai số quyết định.

### `QLHSTVV_03c` — xác nhận nguyên tắc bỏ địa bàn của Tư vấn viên

**(1)** `.md` thống nhất ở ba chỗ: `:46` (ghi chú v3.1 bỏ `TVV_DIA_BAN`, căn cứ NĐ 77/2008 Điều 19 — thẻ Tư vấn viên hiệu lực toàn quốc), `:153` (thực thể gạch bỏ `dia_ban_ids`), `:233` (bộ lọc "địa bàn" hiểu là lọc theo đơn vị công nhận).

**(1b)** `.docx` 4.4.11.2.2 nhóm 3 "Tổ chức" cũng chỉ có *Tổ chức chủ quản* và *Tổ chức đối tác*, không có Địa bàn.

**(2)(3)** Không tranh cãi — QA chỉ xin xác nhận để Dev gỡ dứt điểm.

**→ Kết luận: xác nhận nguyên tắc còn nguyên hiệu lực ở v3.5. Dev gỡ mục "Địa bàn" theo `BUG-QLHSTVV_03` đã chuyển. Dev action: Có. Sheet: Giữ xử lý.**

Chỗ duy nhất còn sót là bản thiết kế `dac-ta-man-hinh-chuc-nang-v2.md:2305` — vẫn còn *"Địa bàn hoạt động \*"* bắt buộc. Bằng chứng cụ thể cho nguyên tắc "`.md` > bản thiết kế".

### Tổng hợp `QLHSTVV_03`

Case lai: **3a Loại 4A** (không sửa, cập nhật `.docx`) · **phần "Số quyết định" chưa kết luận** vì lệch môi trường · **3b Loại 2** (Dev bổ sung vào thẻ đầu trang) · **3c** xác nhận, Dev gỡ Địa bàn. → **Sheet: Giữ xử lý.**

**Phản hồi gửi đối tác:** *"Về số nhóm của thẻ Hồ sơ: hồ sơ tư vấn viên gồm sáu nhóm thông tin, trong đó nhóm Thông tin công khai chỉ hiển thị với hồ sơ đã được công khai lên Cổng pháp luật quốc gia. Xác nhận bản SRS docx đang outdate, sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần. Về mục Địa bàn và mục Số quyết định: ghi nhận là lỗi, sẽ khắc phục."*

---

## `TDHSTVV_14` (row 68) — ai nhận thông báo khi thẩm định kết luận "Không đạt" *(BA-V2-4)*

**(1) Phần mềm đúng `.md` chưa?** **ĐÚNG.** `FR-IV-06 §Processing` bước 6 (`:522`), `§Postconditions` (`:548`), bảng chuyển trạng thái `SM-TVV` (`:2325`) đều chỉ nêu người nhận là **TVV/CG (chủ hồ sơ)**, kênh gửi là email đã khai trên hồ sơ (`:595`). QA đo đúng như vậy.

**(1b) Bản `.docx` nói gì?** **Nói KHÁC, và nói đúng điều đối tác ghi nhận** — mục **4.4.5** *"PM04.TVV.TD. Thẩm định hồ sơ Tư vấn viên"*, ba chỗ độc lập:

| Vị trí | Nguyên văn |
|---|---|
| **4.4.5.1** Mục đích | *"…gửi thông báo cho **Người hỗ trợ (NHT)** khi có kết quả"* |
| **4.4.5.2.1** dòng "Lý do bổ sung / từ chối" | *"Mô tả rõ nội dung **Người hỗ trợ** cần bổ sung hoặc lý do không đạt để **Người hỗ trợ** nắm được"* |
| **4.4.5.2.2** nút "Gửi kết quả thẩm định", Trường hợp 2 | *"Kết luận 'Không đạt': …**gửi thông báo kèm lý do đến Người hỗ trợ**, lưu vết thao tác, hiển thị thông báo **'Đã từ chối hồ sơ'**."* |

Expected của đối tác là bản chép nguyên văn dòng cuối. Nhận định của QA — *"kỳ vọng nằm ngoài đặc tả"* — không đứng được.

**(2) Đối tác yêu cầu khác gì?** Yêu cầu Người hỗ trợ nhận thông báo kèm lý do. Đúng theo `.docx`, khác `.md`.

**(3) Có bắt buộc không?** **Bắt buộc.** Ba căn cứ:

1. **Người nhận theo `.md` không nhận được gì trong phần mềm.** Ứng viên bị từ chối ở bước thẩm định **chưa có tài khoản** — tài khoản chỉ được cấp khi Cán bộ Phê duyệt duyệt (`:2326`). Nên "thông báo chủ hồ sơ" chỉ tồn tại qua thư điện tử; trong phần mềm **không vai trò nào** nhìn thấy kết quả từ chối.
2. **Người phải hành động sau khi bị từ chối là Người hỗ trợ.** Ứng viên không có tài khoản để sửa hồ sơ; `SCR-IV-02` cho Người hỗ trợ *"cập nhật thông tin TVV/CG cùng đơn vị"*, `FR-IV-03` đặt Người hỗ trợ là người nộp. Gửi kết quả cho người không thao tác được, bỏ qua người phải thao tác — quy trình đứt.
3. **Chiều ngược đã có sẵn.** `FR-IV-03 §Processing` bước 8 quy định khi Người hỗ trợ nộp hồ sơ thì hệ thống báo Cán bộ Nghiệp vụ cùng đơn vị. Chiều về thiếu hẳn.

Cùng lỗ hổng áp cho kết luận **"Yêu cầu bổ sung"** (`§Processing` bước 5, `:521`) — `.docx` cũng ghi gửi Người hỗ trợ. Sửa một chỗ mà bỏ chỗ kia thì vòng sau đối tác log lại.

**→ Kết luận: Loại 4B — `.md` bị sót người nhận thông báo. Bổ sung Người hỗ trợ đã nộp hồ sơ vào danh sách người nhận cho cả "Không đạt" và "Yêu cầu bổ sung"; giữ nguyên thư gửi chủ hồ sơ. Dev action: Có. Sheet: Giữ xử lý. Không phản hồi đối tác** (bug thật, sẽ sửa đúng điều họ yêu cầu).

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v2.0.docx`, bàn giao 10/07/2026 |
| Trích `.docx` | **4.4.5.1**, **4.4.5.2.1**, **4.4.5.2.2** — ba chỗ đều ghi người nhận là *Người hỗ trợ*; 4.4.5.2.2 còn quy định câu thông báo *"Đã từ chối hồ sơ"* |
| Trích `.md` | `srs-fr-04-chuyen-gia-tvv.md:521`, `:522`, `:548`, `:595`, `:2325` — chỉ nêu *TVV/CG (chủ hồ sơ)*; không quy định câu thông báo |
| Hướng | **B** — `.md` bị sót. Người nhận theo `.md` chưa có tài khoản (`:2326`), người phải hành động lại không được báo |
| Dev action | **Có** — thêm người nhận + sửa câu thông báo |
| Doc action | Không (bản `.docx` đã đúng) |
| Sheet | **Giữ xử lý** |

**Bốn câu QA hỏi — chốt:**

| # | Câu hỏi | Chốt |
|---|---|---|
| 1 | Người hỗ trợ đã nộp hồ sơ có phải nhận thông báo kèm lý do không? | **Có** |
| 2 | Đi kênh nào? | **Cả hai** — thông báo trong phần mềm và thư điện tử, đúng quy ước `BR-NOTIF-01` (`srs-v3.5.md:5591`: *"in-app + email"*) |
| 3 | Có cần hiện ở thông báo trong phần mềm cho vai trò nào không? | **Có — Người hỗ trợ**, vai trò duy nhất có tài khoản và có việc phải làm tiếp. Ứng viên vẫn chỉ nhận thư điện tử |
| 4 | Câu chữ thông báo sau khi bấm "Gửi KQ" | Theo `.docx`: Không đạt → **"Đã từ chối hồ sơ"**; Yêu cầu bổ sung → **"Đã gửi yêu cầu bổ sung đến Người hỗ trợ"**. BA bổ sung vào `SCR-IV-03` mục 20c (`:1566`) |

Lỗi phụ `BUG-TDHSTVV_14` (thân thư từ chối mang tiêu đề *"✅ Phê duyệt: Hồ sơ bị từ chối"*) giữ nguyên với Dev, không liên quan phần trên.

---

## `TKDGHQHTPL_02` (row 47) — thẻ điểm đánh giá dán nhãn "/100" nhưng trần thực là 10

> **Thay quyết định ngày 30/07 ở `phan-hoi-27-bug-tranh-chap-srs.md`.** Phiếu đó chốt *"Loại 1 — Dev ràng buộc điểm tổng 0–100"*. Kiểm lại vòng 2: triệu chứng vượt trần **đã hết** (thẻ hiển thị 8.2/100), nhưng lỗi thật là **trần cấu hình chỉ tới 10 trong khi nhãn ghi /100**, và **vị trí sửa nằm ở nhóm VI Đánh giá chứ không phải Dashboard**. Phải báo Dev trước khi họ động vào Dashboard.

**(1) Phần mềm đúng `.md` chưa?** **`.md` tự mâu thuẫn.** Hai vế đều có văn bản đỡ lưng:

| Vế | Trích dẫn |
|---|---|
| Thang **0–100** | `srs-fr-01-dashboard.md:416` (*"thang 0-100 theo `KET_QUA_DANH_GIA.diem_tong`"*) · `:450` · `:823` (*"Phạm vi giá trị trục Y: 0-100"*) · `srs-fr-08-danh-gia.md:1049` (`diem_tong` CHECK BETWEEN 0 AND 100) |
| Trần thực là **10** | `srs-fr-08-danh-gia.md:1100` (`diem_toi_da` mặc định **10**) · `:479` (`0 ≤ diem ≤ diem_toi_da`) · `:1239` BR-CALC-04 (`Điểm tổng = SUM(diem_i × trong_so_i / 100)`, tổng trọng số = 100%) |

Với `diem_toi_da = 10` và tổng trọng số ép bằng 100%, trần của `diem_tong` chỉ là 10. Số liệu QA đo khớp: 6 kết quả 10,00 / 9,50 / 8,90 / 8,00 / 7,90 / 5,00 → trung bình 8,216, đúng con số 8.2 trên thẻ. Kết quả 10,00 được hệ thống xếp loại "Xuất sắc" — đạt trần tuyệt đối — vẫn bị thẻ hiển thị như chỉ đạt một phần mười.

**Chỗ đặc tả bỏ trống hẳn:** không dòng nào ràng buộc **tổng** của `diem_toi_da`. `:191` chỉ ghi *"> 0, số nguyên dương"*, màn cấu hình `:850` cũng chỉ ghi *"number > 0"* — trong khi trọng số thì đã bị ép bằng 100%.

**(1b) Bản `.docx` nói gì?** **Đứng cùng phía thang 0–100 và cũng bỏ trống ràng buộc tổng** — không có tranh chấp tài liệu, đây là lỗi nội bộ đặc tả. Bảng thành phần Dashboard STT 16: *"biểu đồ trái… (thang 0–100)"*. Mục cấu hình tiêu chí: *"Tổng trọng số… phải bằng 100%"* nhưng *"Điểm tối đa… Số nguyên dương, lớn hơn 0"*.

**(2) Đối tác yêu cầu khác gì?** Chỉ số phải nằm trong thang 0–100 — không khác đặc tả.

**(3) Có bắt buộc không? Chọn hướng nào?** Bắt buộc. Ba hướng QA sàng, đã kiểm lại từng vế:

- **(a) Dashboard quy đổi sang phần trăm — LOẠI.** Màn chi tiết hiển thị cột *"Điểm tổng (tự tính = tổng điểm × trọng số / 100)"* dạng **số thô** (`:873`). Quy đổi sẽ cho Dashboard 86 còn màn chi tiết 8,6 cho cùng một đợt — đúng lỗi mà `CHANGELOG` Thay đổi 5 đã chủ động sửa khi nâng v3 → v3.5.
- **(b) Giữ số thô, mỗi kế hoạch một mẫu số riêng — LOẠI.** Không cộng trung bình chéo kế hoạch được, mà đó là việc chính của thẻ.
- **(c) Ràng buộc cấu hình để trần luôn bằng 100 — CHỌN.** Khi trần bằng 100 thì điểm thô, phần trăm và nhãn "/100" trùng nhau làm một; cả bốn quy định đang chọi nhau tự khớp. Củng cố: dữ liệu đời trước (`KHDG-SEED-0001`) mang điểm 80 / 60 / 90 — đã ở thang 0–100 từ đầu.

> **Một lập luận của QA không dùng được:** phiếu QA nêu *"bằng chứng tự tố cáo — thẻ Chất lượng đào tạo cùng màn hiển thị 7.3/10"*. Hai thẻ đo hai thứ khác nhau: thẻ đào tạo hiển thị **điểm kiểm tra học viên**, `FR-III-05` quy định thang **0–10** (*"ngoài 0–10 → ERR-KQ-01"*), `.docx` STT 17 cũng ghi *"/10"*. Hai thang khác nhau ở đây là **cố ý và đúng**. Kết luận (c) vẫn vững nhờ ba căn cứ còn lại.

**→ Kết luận: Loại 2 — bổ sung ràng buộc còn thiếu vào đặc tả rồi Dev làm theo. Vị trí sửa ở nhóm VI Đánh giá (cấu hình tiêu chí), Dashboard GIỮ NGUYÊN. Dev action: Có. Sheet: Giữ xử lý. Không phản hồi.**

**Phương án xử lý (cập nhật SRS) — trả lời câu 1 của QA:** chốt quy tắc mới, mã **BR-CALC-08** (đã kiểm `BR-CALC-01`→`07` đang dùng, `08` còn trống):

> **BR-CALC-08 — Chuẩn thang điểm của một đợt đánh giá:** trong mỗi kế hoạch đánh giá, tổng điểm tối đa có trọng số của các tiêu chí phải bằng 100 — tức tổng của (điểm tối đa của tiêu chí × trọng số tiêu chí ÷ 100) bằng 100. Ràng buộc này bảo đảm điểm tổng của mọi đợt nằm trên cùng thang 0–100, cộng trung bình chéo đợt được, và trùng với tỷ lệ phần trăm dùng để xếp loại. Hệ thống chặn lưu cấu hình tiêu chí vi phạm, kèm thông báo nêu rõ tổng hiện tại.

Kèm theo:
- Đổi mặc định `diem_toi_da` từ **10** thành **100** (`srs-fr-08-danh-gia.md:1100`) — với tổng trọng số 100%, mọi tiêu chí để mặc định là thỏa BR-CALC-08 ngay.
- Bổ sung ràng buộc tổng vào `:191` (bảng trường tiêu chí) và `:850` (màn cấu hình), đặt cạnh cảnh báo tổng trọng số đã có.
- Bịt luôn **lỗ hổng QA phát hiện kèm**: `diem_toi_da` để tự do trong khi `diem_tong` bị chặn `CHECK BETWEEN 0 AND 100`. QA đã dựng thử kế hoạch `diem_toi_da = 200` và hệ thống **chấp nhận** — chấm 150 sẽ sinh `diem_tong = 150`, vi phạm chính ràng buộc đó. BR-CALC-08 chặn luôn, không cần quy tắc riêng.
- **Không đụng gì ở Dashboard** — `srs-fr-01-dashboard.md:416` / `:450` / `:823` giữ nguyên.

**Trả lời câu 2 của QA — dữ liệu đã chấm thì quy đổi hay để lệch? Không quy đổi, cấu hình lại kế hoạch và chấm lại.** Toàn bộ dữ liệu đang có nằm trên môi trường kiểm thử và môi trường được giao, không phải dữ liệu nghiệp vụ thật — chính phiếu QA ghi kế hoạch `DG-20260727-0001` là do QA tự tạo. Quy đổi dữ liệu thử nghiệm là việc thừa mà lại đụng vào kết quả đã chấm.

*Điều kiện kèm theo:* nếu tới thời điểm vận hành thật đã phát sinh đợt đánh giá **đã chấm xong trên thang cũ** thì quy đổi theo tỷ lệ trần của chính đợt đó (điểm mới = điểm cũ × 100 ÷ trần cũ), giữ nguyên xếp loại đã công bố, ghi việc quy đổi vào nhật ký của đợt. Thuộc hạng mục di trú dữ liệu `INS-06` đang chờ khảo sát.

---

## `TKDGHQHTPL_OOS_01` (row 276) — thẻ điểm gộp cả kết quả chưa chấm và kế hoạch đã hủy

Test case do QA tự mở, ngoài phạm vi phiếu đối tác.

**(1) Phần mềm đúng `.md` chưa?** **`.md` bỏ trống.** `FR-I-08 §Processing` bước 2 (`srs-fr-01-dashboard.md:441`) chỉ ghi *"Tính điểm… trung bình từ kết quả đánh giá thuộc phạm vi"*; `§Outputs` `so_luong_danh_gia` (`:452`) ghi *"tổng số đánh giá trong kỳ + phạm vi đã lọc"*; `§Preconditions` (`:425`) ghi *"Có dữ liệu đánh giá trong kỳ"*. Không dòng nào nêu điều kiện lọc trạng thái.

Nhóm VI thì nói rõ bản ghi chưa chấm chưa phải đánh giá đã hoàn tất (`srs-fr-08-danh-gia.md:1052` — `CHECK IN ('CHUA_DANH_GIA','DA_DANH_GIA')`, mặc định `CHUA_DANH_GIA`), và đợt đánh giá chuyển `HUY` là **xóa mềm** (`:1183`, `:1168`).

Số liệu QA đo: thẻ hiển thị 29.5/100 kèm *"Dựa trên 14 đánh giá"* trong khi chỉ 11 kết quả đã chấm. Ba bản ghi dôi ra còn `CHUA_DANH_GIA` nhưng đã có điểm (80 / 60 / 90) và là ba cột cao nhất biểu đồ. Kết quả 100,00 của kế hoạch `DG-20260727-0001` ở trạng thái **Hủy** làm cột 07/2026 tăng gấp đôi (16.6 thay vì 8,24).

**(1b) Bản `.docx` nói gì?** Không nói gì về điều kiện lọc của thẻ này. Không có tranh chấp tài liệu.

**(2) Đối tác yêu cầu khác gì?** Không có — QA tự mở.

**(3) Có bắt buộc không?** Có — số liệu sai lệch làm hỏng chỉ số đánh giá hiệu quả.

**→ Kết luận: Loại 2 — bổ sung điều kiện lọc vào `FR-I-08`, KHÔNG mở rộng `BR-RPT-01`. Dev action: Có (`BUG-TKDGHQ-KPI-LOC` đã log). Sheet: Giữ xử lý. Không phản hồi** (dòng QA tự mở).

**Vì sao bác cách QA đề xuất** (thêm `FR-I-08` vào phạm vi `BR-RPT-01`) — làm theo sẽ hỏng:

1. **Áp `BR-RPT-01` vào `FR-I-08` cho kết quả rỗng.** Quy tắc (`srs-v3.5.md:5625`) liệt kê tập trạng thái hợp lệ là `DA_DUYET / HOAN_THANH / DA_CONG_BO / CONG_KHAI / DA_CHI_TRA` — **không có `DA_DANH_GIA`**, tức trạng thái cuối của `KET_QUA_DANH_GIA`. Áp máy móc thì không bản ghi nào lọt.
2. **Dashboard vốn nêu tập trạng thái tại từng thẻ, không dùng quy tắc chung.** Đã kiểm cả bảy thẻ còn lại: KPI-01 lọc `MOI`, KPI-03 lọc 5 trạng thái đang sống, KPI-04 lọc `HOAN_THANH` + `DA_DANH_GIA`, KPI-05 `DANG_DIEN_RA`, KPI-06 `DA_KET_THUC`, KPI-07 `DANG_HOAT_DONG`. Nhiều thẻ **cố ý đếm bản ghi chưa ở trạng thái cuối** — kéo `BR-RPT-01` vào Dashboard sẽ đá nhau với KPI-01 và KPI-03.

Vậy `FR-I-08` không "cố ý tính mọi bản ghi" — nó là thẻ **duy nhất** quên nêu tập trạng thái của mình. Đây là **bị sót**.

**Phương án xử lý (cập nhật SRS):**
- `§Processing` bước 2 (`:441`) và `§Outputs` `so_luong_danh_gia` (`:452`): chỉ tính **kết quả đánh giá ở trạng thái "Đã đánh giá"**, thuộc **kế hoạch đánh giá không ở trạng thái "Hủy"**. Áp cho **cả con số trung bình lẫn cỡ mẫu** — hai chỗ phải cùng một tập bản ghi, nếu không thì chú thích "Dựa trên N đánh giá" tiếp tục nói dối.
- `§Preconditions` (`:425`): sửa *"Có dữ liệu đánh giá trong kỳ"* → *"Có kết quả đánh giá đã chấm trong kỳ"*.
- `BR-RPT-01` **giữ nguyên phạm vi** `FR-IX-01..23`.
- Nhãn cỡ mẫu *"Dựa trên N đánh giá"* sau khi lọc là đúng nghĩa, không cần đổi câu chữ.

> **Ghi chú cho Dev khi kiểm lại:** lỗi chỉ lộ khi trong kỳ có đồng thời một kết quả còn "Chưa đánh giá" nhưng đã có điểm, và một kế hoạch "Hủy" mà kết quả đã có điểm. Môi trường đối tác `htpldn-uat.ospgroup.vn` tại 27/07 **không** thỏa điều kiện này — mở Dashboard ở đó không thấy lỗi, và **đó không phải bằng chứng đã sửa**.

**Chung cho cả hai case Dashboard:** `srs-fr-01-dashboard.md:410` vẫn ghi `FR-I-08` có *"công thức tính chờ CĐT review"*. Hai quyết định trên là quyết định của BA về ràng buộc dữ liệu và điều kiện lọc, **không** thay thế lần review công thức của CĐT — đề nghị gộp vào lần trình CĐT gần nhất.

---

## Phụ lục — 2 ghi nhận QA nêu ngoài phạm vi 4 case

**P1 — mâu thuẫn về luồng nhập tệp Excel danh sách đăng ký** *(gắn `DKTGKH_12` row 3)*. Đã được quyết định khác bao trùm, QA không cần theo dõi tiếp: quyết định 30/07 (`phan-hoi-27-bug-tranh-chap-srs.md`) đã **gỡ hẳn** luồng nhập tay và nhập tệp Excel, căn cứ CSV baseline UC22/UC23 không có giao dịch tạo/nhập/import. SRS đã sửa 13 mục trong ngày. Sáu test case `DKTGKH_07`→`_12` nằm trong diện đề nghị đối tác hủy. Lỗi đọc sai ô Email không cần sửa nữa vì chức năng bị gỡ.

**P2 — nhãn "Đơn vị quản lý" có dấu sao bắt buộc nhưng web không có** *(gắn `DKTGMLTVV_02` row 52)*. `SCR-IV-02` mục 2.11 (`:1494`) ghi nhãn *"Đơn vị quản lý \*"* nhưng cùng dòng mô tả *"ô văn bản (chỉ đọc) — hệ thống tự gán… không sửa được"*. Dấu sao báo cho người dùng biết **họ phải nhập**; đặt trên ô họ không nhập được là gây nhiễu. `.docx` 4.4.3.2.2 STT 2 xử lý gọn hơn: cột Bắt buộc ghi **"Có (tự gán)"**.

**→ Chốt quy ước: dấu sao trên nhãn chỉ dùng cho trường người dùng tự nhập. Trường chỉ đọc / hệ thống tự gán thì không gắn dấu sao, dù dữ liệu bắt buộc phải có.** Web đang làm đúng. BA rà lại các nhãn chỉ đọc còn gắn dấu sao khi sửa SRS đợt tới. `DKTGMLTVV_02` giữ nguyên `Reject`.

---

## Phát hiện thêm khi kiểm — 3 điểm QA chưa nêu

**1. `Tổ chức hành nghề chính` — mô hình dữ liệu chọi lại chính lỗi QA đã chuyển Dev.** QA log `BUG-DKTGMLTVV_03` với lý do web đặt trường này bắt buộc trong khi SRS nói tùy chọn, dẫn `:1506` và `:307`. Hai chỗ đó đúng là tùy chọn, và **baseline `srs-v3.5.md:1710` cũng ghi N** kèm chú thích *"optional — TVV tự do có thể NULL `[CR-02]`"*. Chỉ **`srs-fr-04-chuyen-gia-tvv.md:150` ghi Y**. Ba chỗ nói tùy chọn, một chỗ nói bắt buộc.

Chốt theo nghiệp vụ: **tùy chọn**. Tư vấn viên tự do là hình thức hành nghề hợp pháp, `SCR-IV-02` mục 4.1 ghi thẳng *"tư vấn viên tự do để trống"*, `SCR-IV-03` tab Hồ sơ nhóm (c) có sẵn cách hiển thị *"Tự do"*. **BA sửa `:150` từ Y sang N.** Không sửa thì Dev gỡ ràng buộc ở giao diện xong phần xử lý phía sau vẫn từ chối, phiếu bị mở lại.

**2. Mô hình dữ liệu thiếu hẳn trường `chuyen_nganh`.** Xem phương án ở mục `DKTGMLTVV_03b`. Là việc BA phải làm **trước** khi Dev đặt ràng buộc bắt buộc.

**3. `.docx` 4.3.7.2.2 STT 15 ghi trường "Mô tả" của bài giảng là bắt buộc.** `.md` đã chuyển tùy chọn theo `STT22 UAT 2026-06-02` (`srs-fr-03-dao-tao.md:739`) — đúng yêu cầu đối tác đợt trước. Chưa có test case nào chạm vào; đưa vào danh sách rà `.docx` để đợt sau không phát sinh phiếu mới.

---

## Cập nhật sheet theo dõi

✅ **Đã ghi 30/07/2026 — 5 ô, đã verify Mã TC tại từng dòng sau khi ghi.**

**Sheet:** `1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c` · tab **`UAT_TGPL Doanh Nghiệp`** (`gid=799081340`).

| Mã | Dòng thật | Khối | `V` Trạng thái dev fix 2 | `W` DEV phản hồi lần 2 |
|---|---:|---|---|---|
| `TKDGHQHTPL_02` | **47** | Tuần 1 | `InProcess` — đã có sẵn, không đụng | Không điền |
| `QLKTLBG_02` | **274** | Tuần 2 | Ghi `InProcess` (đang trống) | Không điền |
| `DKTGMLTVV_03` | **416** | Tuần 2 | Ghi `InProcess` (đang trống) | ✅ Đã ghi — phản hồi ý 2a, 392 ký tự |
| `QLHSTVV_03` | **432** | Tuần 2 | `InProcess` — đã có sẵn, không đụng | ✅ Đã ghi — phản hồi 3 ý, 335 ký tự |
| `TDHSTVV_14` | **450** | Tuần 2 | Ghi `InProcess` (đang trống) | Không điền |
| `TKDGHQHTPL_OOS_01` | — | — | **Không có dòng nào trong sheet** | — |

**Không dòng nào chuyển `Resoved` hay `Reject`** — cả năm còn ít nhất một ý con Dev phải sửa.

### Bốn điều lệch so với dự kiến, ghi lại để đợt sau không mắc lại

**1. Số dòng trong phiếu QA không phải dòng thật.** QA ghi row 8 / 53 / 58 / 68; dòng thật là **274 / 416 / 432 / 450**. Đó là số dòng của bản Excel xuất theo từng khối tuần, không phải dòng trên sheet. Riêng `TKDGHQHTPL_02` trùng (47) vì khối Tuần 1 nằm đầu bảng. Đã dò lại toàn bộ theo **Mã TC**, mỗi mã xuất hiện đúng một lần, không trùng.

**2. Không có tab `-tuần 1` / `-tuần 2`.** Sheet chỉ có **một** tab dữ liệu `UAT_TGPL Doanh Nghiệp`, các tuần là **khối trong cùng tab** (cột `C` = Tuần). Tab `Bản sao của UAT_TGPL Doanh Nghiệp` là bản nhân đôi — **không ghi vào đó**.

**3. Chữ cái cột lệch một bậc so với phiếu QA.** QA ghi *"cột W Trạng thái dev fix 2 / X DEV phản hồi lần 2"*. Thực tế theo dòng tiêu đề: **`V` = Trạng thái dev fix 2, `W` = DEV phản hồi lần 2**. Ghi theo phiếu QA sẽ đổ nội dung sang cột trống bên phải. Đây đúng là lý do quy trình bắt xác định cột theo **tên tiêu đề**.

**4. `TKDGHQHTPL_OOS_01` không tồn tại trên sheet.** Đã quét cả 1.552 ô Mã TC, không mã nào chứa "OOS". Đúng bản chất — đây là test case QA tự mở ngoài phạm vi phiếu đối tác, chưa từng đưa vào bảng theo dõi. **Không tạo dòng mới** (thêm dòng vào bảng đối tác là việc phải có thoả thuận riêng). Nếu muốn theo dõi thì đề nghị QA đăng ký mã với đơn vị kiểm thử trước.

### Hai điểm còn treo, cần BA quyết riêng

**`QLKTLBG_02` (dòng 274) — phản hồi vòng 1 của Dev đang sai và vẫn nằm đó.** Cột `Q` ghi *"Đã kiểm tra lại, không tái hiện được lỗi…"* và cột `P` để `Resoved`. Kết luận phiếu này ngược lại: **thiếu 3 cột là lỗi thật**. Theo quy tắc "bug thật sẽ sửa thì không cần phản hồi" nên `W` để trống — nhưng như vậy đối tác đọc sheet vẫn thấy câu phủ nhận của vòng 1 mà không có đính chính. Đề nghị BA cho ghi một câu vào `W`, chẳng hạn: *"Ghi nhận của Quý đơn vị là đúng. Ba cột Ảnh đại diện, Lĩnh vực, Người tạo sẽ được bổ sung; phản hồi lần 1 không tái hiện được lỗi xin được rút lại."*

**Ba ô `V` đang trống đã được ghi `InProcess`.** Phiếu chốt "Giữ xử lý", nhưng ô trống không thể hiện được điều đó, trong khi hai dòng còn lại đã sẵn `InProcess`. Ghi `InProcess` là cách thể hiện đúng trạng thái đang xử lý và đồng bộ với các dòng cùng đợt. Nếu BA muốn để trống thì báo, tôi xoá lại.

---

## Việc sửa SRS — BA xác nhận phương án 30/07/2026, đang thực hiện theo pha

Gom theo tệp, mỗi pha một tệp, verify xong mới sang pha sau.

| Pha | Tệp | Mục | Trạng thái |
|---|---|---|---|
| **1** | `srs-fr-04-chuyen-gia-tvv.md` | 4→11 | ✅ **Xong 30/07/2026** — 9 thay đổi, đã soát cột bảng và dò chỗ sót |
| **3** | `srs-fr-04` (phần `FR-IV-07`) · `srs-fr-08-danh-gia.md` · `srs-fr-01-dashboard.md` · `srs-v3.5.md` | 12→18 + phương án B | ✅ **Xong 30/07/2026** — 13 thay đổi trên 4 tệp |
| **2** | `srs-fr-03-dao-tao.md` | 1→3 | ✅ **Xong 30/07/2026** — 3 thay đổi |
| 4 | Bản `.docx` | 19→23 | Việc của bên soạn tài liệu bàn giao — **chưa làm** |

**Toàn bộ phần sửa SRS đã hoàn tất: 5 tệp, 25 thay đổi.** Đã chạy kiểm tự động so số cột từng dòng thêm mới với dòng kề trên toàn bộ khác biệt — 0 dòng lệch, không bảng nào gãy.

**`srs-fr-03-dao-tao.md` — ✅ PHA 2 XONG 30/07/2026**
1. ✅ `SCR-III-03` — thay toàn bộ khối 7 dòng bằng mục viết đủ Thành phần 1→6 + bảng 9 cột + quy tắc nghiệp vụ, theo đúng 3 điểm BA duyệt (nhãn "Ảnh đại diện" · badge chứ không ô chuyển · có nút Xuất Excel). Sửa luôn phần chữ không dấu ở tiêu đề và 3 dòng đầu.
2. ✅ `FR-III-07 §Outputs` mục 6 — đổi `dung_luong` → `kich_thuoc_file` cho khớp thực thể (`srs-v3.5.md:2475`); nhãn hiển thị giữ "Dung lượng". Đã quét toàn thư mục, không còn chỗ nào gọi `dung_luong` cho `BAI_GIANG`.
3. ✅ Rà 6 dòng "UX-Spec ref" — **chú thích chứ không xóa**, để không mất dấu vết bản thiết kế v3.5 còn nợ:

| Dòng | Trỏ tới | Thực trạng | Đã làm |
|---|---|---|---|
| `:1796` `:1804` `:1898` | `dac-ta-man-hinh-chuc-nang-v3.5.md` MH-03.0 / 03.1 / 03.2 | **Tệp không tồn tại** — kho chỉ có bản `v2` | Chú thích "tệp chưa có trong kho, mục SCR này tự mô tả đủ và là căn cứ nghiệm thu" |
| `:1908` | `…-v2.md` MH-03.3 | Mục **đã đánh dấu DEPRECATED v2.1** | Chú thích tham chiếu lịch sử (làm ở mục 1) |
| `:1954` `:1962` | `…-v2.md` MH-03.4 / MH-03.6 | **Bình thường, còn hiệu lực** | Không đụng |

> **Tự đính chính:** bản phiếu trước ghi *"ba dòng sau trỏ mục đã ngừng dùng"*. **Sai** — chỉ MH-03.3 bị ngừng dùng; MH-03.4 (Ngân hàng câu hỏi) và MH-03.6 (Giảng viên) là mục bình thường. Phát hiện khi mở bản thiết kế kiểm lại trước lúc ghi chú thích, đã gỡ hai chú thích đặt nhầm.

> **Nguồn thứ ba xác nhận bộ 9 cột:** bản thiết kế đời trước `dac-ta-man-hinh-nhom-III-IV.md` §MH-03.3 cũng liệt kê đúng `col_anh_dai_dien` · `col_ten_bai_giang` · `col_loai` · `col_linh_vuc` · `col_kich_thuoc` · `col_cong_khai` · `col_nguoi_tao` · `col_ngay_tao` · `col_hanh_dong`. Vậy bộ cột này thống nhất qua **cả ba đời tài liệu thiết kế lẫn bản `.docx`** — kết luận `QLKTLBG_02` không còn chỗ tranh cãi.

**`srs-fr-04-chuyen-gia-tvv.md` — ✅ PHA 1 XONG 30/07/2026**
4. ✅ Thực thể `to_chuc_chinh_id` đổi Y → N. *Ghi nhận khi làm: bản chép `### TU_VAN_VIEN (owned)` trong cùng tệp **đã** ghi N từ trước, nên thực tế là 4 nguồn nói tùy chọn / 1 nguồn nói bắt buộc, không phải 3/1 như phiếu ước lượng ban đầu.*
5. ✅ Bổ sung `chuyen_nganh` — 3 vị trí trong tệp này (thực thể dòng `10a` · khối sơ đồ quan hệ · mục `TU_VAN_VIEN (owned)`). Vị trí thứ 4 ở `srs-v3.5.md` thuộc Pha 3.
6. ✅ `SCR-IV-02` nhóm 2 — bổ sung 4 mục `3.8`→`3.11`: Chuyên ngành \*, Số năm kinh nghiệm \*, Số quyết định công bố, Ngày quyết định công bố. Form giữ đúng **5 nhóm**, đã kiểm không phát sinh nhóm thứ 6.
7. ✅ `SCR-IV-02` mục 2.11 — bỏ dấu sao nhãn "Đơn vị quản lý", ghi ràng buộc dạng "bắt buộc có giá trị — hệ thống tự gán".
8. ✅ `SCR-IV-03` thẻ thông tin chính — bổ sung "Số quyết định công nhận" cạnh "Ngày công nhận".
9. ✅ `SCR-IV-03` tab Hồ sơ — ghi rõ là mô tả rút gọn ở cấp nhóm, không phải danh sách đóng ở cấp trường.
10. ✅ `SCR-IV-03` mục 20c — bổ sung câu thông báo và người nhận.
11. ✅ `FR-IV-06` Processing bước 5 + 6, Postconditions, bảng `SM-TVV` — bổ sung Người hỗ trợ vào người nhận thông báo. **Thêm ngoài danh sách:** Tiêu chí chấp nhận của chính `FR-IV-06` còn một dòng ghi *"thông báo TVV/CG (chủ hồ sơ)"* — đã sửa đồng bộ và bổ sung một dòng cho nhánh "Không đạt" vốn chưa có tiêu chí chấp nhận nào.

**`FR-IV-07` (Phê duyệt) — ✅ BA CHỐT PHƯƠNG ÁN B 30/07/2026, đã áp trong Pha 3**

Phát sinh khi làm Pha 1, không nằm trong 2 phiếu QA. Khác `FR-IV-06` ở chỗ **bản `.docx` mục 4.4.6 KHÔNG nhắc Người hỗ trợ** — nó ghi người nhận là *"Cán bộ nghiệp vụ đã thẩm định và tư vấn viên / chuyên gia là chủ hồ sơ"*. Nên đây là **quyết định mới của BA**, không phải chép lại tài liệu bàn giao.

Hai lỗi được vá cùng lúc:

| Lỗi | Trước | Sau |
|---|---|---|
| Ba nguồn nói ba kiểu về cùng sự kiện "CB PD từ chối" | `§Processing` bước 4 và Tiêu chí chấp nhận chỉ ghi *chủ hồ sơ*; `SM-TVV` và `.docx` ghi *CB NV + chủ hồ sơ* | Cả bốn nguồn thống nhất: **CB NV đã thẩm định + chủ hồ sơ + Người hỗ trợ đã nộp hồ sơ** |
| `SCR-IV-03` Quy tắc tương tác ghi *"chủ hồ sơ tự nộp lại"* sau khi bị từ chối | Việc không ai làm được — ứng viên bị từ chối chưa có tài khoản | Sửa thành **Người hỗ trợ đã nộp hồ sơ** sửa và nộp lại |

Đã sửa 6 chỗ: `§Processing` bước 4 · `§Postconditions` · Tiêu chí chấp nhận nhánh từ chối · `SM-TVV` dòng `CHO_PHE_DUYET → TU_CHOI` · `SCR-IV-03` nút Phê duyệt và nút Từ chối (trước đây **không nhắc thông báo gì cả**) · `SCR-IV-03` quy tắc nộp lại sau từ chối.

**Doc action phát sinh:** bản `.docx` mục **4.4.6** phải bổ sung Người hỗ trợ vào người nhận thông báo ở cả nhánh phê duyệt lẫn nhánh từ chối — thêm vào danh sách việc của bên soạn tài liệu bàn giao (mục 23).

**`srs-fr-08-danh-gia.md` — ✅ PHA 3 XONG 30/07/2026**
12. ✅ Thực thể `diem_toi_da` mặc định **10 → 100**, thêm ràng buộc BR-CALC-08.
13. ✅ Bảng trường tiêu chí và màn cấu hình tiêu chí — bổ sung ràng buộc tổng điểm tối đa có trọng số bằng 100, chặn lưu khi vi phạm, mặc định 100.

**`srs-fr-01-dashboard.md` — ✅ PHA 3 XONG**
14. ✅ `§Preconditions` đổi thành *"Có kết quả đánh giá đã chấm trong kỳ"*; `§Processing` bước 2 nêu đủ hai điều kiện lọc; `§Outputs` `so_luong_danh_gia` ràng buộc đếm đúng tập bản ghi đã dùng tính trung bình.

**`srs-v3.5.md` — ✅ PHA 3 XONG**
15. ✅ Thêm **BR-CALC-08** vào mục B.6 BR-CALC, đặt sau BR-CALC-07 đúng thứ tự.
16. ✅ `§3.4.3.4` — bổ sung `chuyen_nganh` (vị trí thứ 4 của mục 5, hoàn tất).
17. ✅ Thêm **UI-12** (bảng Thành phần màn hình là danh sách đóng ở cấp đặc tả) và **UI-13** (dấu sao chỉ dùng cho trường người dùng tự nhập) vào bảng quy ước giao diện — đã kiểm hai mã còn trống.
18. ✅ `BR-RPT-01` — **giữ nguyên**, không mở rộng phạm vi (không cần sửa gì).

**Bản `.docx` — việc của bên soạn tài liệu bàn giao**
19. Mục 4.3.7.2.2 — nhãn cột ảnh đổi theo `.md`; STT 6 cột Công khai đổi từ ô chuyển sang badge; STT 15 trường "Mô tả" chuyển bắt buộc → tùy chọn.
20. Mục 4.4.3.2.2 — bổ sung bộ trường nhóm 2 cho khớp `.md` (hiện thiếu 6 trường, và thiếu cả Ngày sinh / Giới tính / Ảnh chân dung ở nhóm 1).
21. Mục 4.4.11.2.2 — bổ sung nhóm thứ 6 "Thông tin công khai" vào thẻ Hồ sơ.
22. Mục 4.4.1.3.2 — rà lại sau khi `SCR-IV-02` bổ sung `Chuyên ngành`.
23. Mục **4.4.6** (Phê duyệt công nhận Tư vấn viên) — bổ sung Người hỗ trợ đã nộp hồ sơ vào người nhận thông báo ở **cả nhánh phê duyệt lẫn nhánh từ chối** (theo phương án B BA chốt 30/07). Hiện `.docx` chỉ ghi *"Cán bộ nghiệp vụ đã thẩm định và tư vấn viên / chuyên gia là chủ hồ sơ"*.

**Kèm khi bàn giao bản `.docx` mới:** danh sách mã test case cần sửa Kết quả mong đợi, hiện có `QLKTLBG_02` (nhãn cột "Ảnh đại diện") và `DKTGMLTVV_03` (bộ trường nhóm 2).
