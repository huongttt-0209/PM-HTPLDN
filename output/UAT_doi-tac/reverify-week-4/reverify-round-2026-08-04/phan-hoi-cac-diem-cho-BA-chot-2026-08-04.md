# Phản hồi các điểm chờ BA/CĐT chốt — đợt Tuần 5 (gộp 6 phiếu yêu cầu)

- **Ngày phản hồi:** 04/08/2026
- **Phiếu nguồn đã gộp:** `NHSYC_01-B-thang-diem-uu-tien.md` (DEV) · `ba-confirmation-needed-luong3-vu-viec-2026-08-03.md` · `ba-confirmation-needed-week-2-2026-08-03.md` · `T2-batch-tvv-labels-filter-BA-confirm.md` · `ba-confirmation-needed-bao-cao-thong-ke-xuat-file-2026-08-03.md` · `con-can-verify-tuan-3-2026-08-03.md`
- **Bản `.docx` đối chiếu:** `HTPLDN-PTYC-CT-v3.5.docx` — bản bàn giao có hiệu lực, là căn cứ duy nhất cho câu hỏi (1b) ở mọi mục
- **Bản chấm chuẩn:** SRS `.md` — `_bmad-output/planning-artifacts/srs-v3.5/`
- **Hai sổ, hai vai:** nội dung lỗi và minh chứng đọc từ **sổ nội bộ** `1OKBN2ot…`; **trạng thái đối tác thì chỉ lấy từ sổ KTĐL** `1dJat1cc…` tab `UAT_TGPL Doanh Nghiệp`. Ghi chú của Dev trên sổ nội bộ là **lời khai, không phải bằng chứng** — chưa QA đo lại thì chưa kết luận đã sửa.

**Trạng thái trên sổ KTĐL, bản tải 04/08/2026** — chưa dòng nào của phiếu này được Dev đánh dấu đã sửa, trừ nhóm báo cáo:

| Mục | Mã TC | Dòng | Trạng thái | Dev fix | Vòng 2 |
|---|---|:-:|:-:|:-:|:-:|
| Vấn đề 1–6 | `NHSYC_01` | 501 | Fail | *(trống)* | *(trống)* |
| Vấn đề 7 | `TKHSYCHTPL_03` | 539 | Fail | *(trống)* | *(trống)* |
| Vấn đề 8 | `KTDGKQHT_02` | 254 | Fail | *(trống)* | *(trống)* |
| Vấn đề 9 | `PDKHDTTH_04` | 352 | Fail | *(trống)* | *(trống)* |
| Vấn đề 10 | `QLDXDTTH_08` | 337 | **Pass** | *(trống)* | *(trống)* |
| Vấn đề 11 | `DKTGMLTVV_04` | 409 | Fail | *(trống)* | *(trống)* |
| Vấn đề 12 | `DKTGMLTVV_05` | 410 | Fail | *(trống)* | *(trống)* |
| Vấn đề 13 | `QLLSHTCTVV_03` | 471 | Fail | *(trống)* | *(trống)* |
| Vấn đề 14 | `QLLSHTCTVV_04` | 472 | Fail | *(trống)* | *(trống)* |
| Vấn đề 15 | — | — | **không có dòng** | — | — |
| Vấn đề 16–18 | `SLHDVM_07` và 22 phiếu Xuất PDF | 1222… | Fail | dev done | *(trống)* |

Cột "Dev fix" trống nghĩa là **đối tác chưa nhận được thông báo đã sửa**, không phải Dev chưa làm. Riêng nhóm báo cáo có `dev done` nhưng vòng 2 còn trống — tức chưa ai đo lại.
- **Ngoài phạm vi phiếu này:** `QLKTLBG_09-xem-inline-slide-pptx.md` đã có phiếu phản hồi riêng — `QLKTLBG_09-phan-hoi.md` cùng thư mục. Thư mục `Week5/Yêu cầu/` có 7 tệp; 6 tệp gộp ở đây, 1 tệp xử lý riêng.

**Ghi chú phương pháp:**
- Toàn bộ trích dẫn `file:dòng` trong 5 phiếu nguồn đã được mở kiểm lại từng dòng, không nhận nguyên si; sáu chỗ kết luận khác đề xuất của phiếu nguồn đều nêu rõ căn cứ tại chỗ (Vấn đề 2, 7, 8, 9, 10, 11).
- 4 mục trùng nhau giữa các phiếu (`DKTGMLTVV_05`, `QLLSHTCTVV_03`, `QLLSHTCTVV_04`, `TKHSYCHTPL_OOS_01`) đã gộp thành một mục duy nhất.
- Các bug đã chứng minh tái hiện trong cùng test case (6 bug ở phiếu tuần 2) không thuộc phạm vi phiếu này — Dev xử lý độc lập.

---

# A. Vụ việc hỗ trợ pháp lý

> **Sổ dùng cho phiếu này:** sổ nội bộ `1OKBN2ot…`, các tab `tuần 2` · `tuần 3` — số dòng, trạng thái và minh chứng dưới đây đều lấy từ đó (bản tải 04/08/2026).
>
> 🔴 **Cảnh báo về sổ bàn giao `1dJat1cc…` (tab `UAT_TGPL Doanh Nghiệp`) — việc riêng, cần xử lý.** Đối chiếu bản tải ngày 03/08 và 04/08 cho thấy **hai dòng đã bị xoá khỏi tab chính**: `NHSYC_09` (DN thiếu trường ưu tiên → tự gán mức thấp nhất) và `NHSYC_10` (tự động tính điểm ưu tiên theo NĐ 55/2019 Điều 4). Tra toàn tab hôm nay: **không còn dòng nào nhắc "điểm ưu tiên"**. Tab `Bản sao của UAT_TGPL Doanh Nghi` vẫn còn cả hai (dòng 518, 519) nên khôi phục được.
>
> Hệ quả: quyết định đã chốt ở Vấn đề 3 và 4 **hiện không còn phiếu nào để nghiệm thu**. Đề nghị khôi phục hai dòng này trước khi Dev bàn giao.
>
> Ô mã TC trên sổ vẫn là **công thức**, nên chèn/xoá dòng làm mã đánh số lại — số dòng trong phiếu này chốt theo bản tải **04/08/2026**, tra lại trước mỗi lần ghi.

**Bối cảnh nghiệp vụ (dùng chung cho vấn đề 1–6):** `VU_VIEC.uu_tien` là mức ưu tiên xử lý, hệ thống tự tính khi tạo hồ sơ theo tiêu chí ưu tiên DN tại **NĐ 55/2019 Điều 4 khoản 4**, cán bộ điều chỉnh được kèm lý do. Giá trị này dùng xếp thứ tự bảng gợi ý phân công người xử lý (FR-V.I-09). Vị trí: sổ nội bộ tab `tuần 2` dòng **127** (`Verify` = BA confirm). Cửa nghiệm thu là `NHSYC_09` · `NHSYC_10` — trên sổ nội bộ vẫn còn (tab `Trang tính6`, dòng 516–517, đều `N/R`); riêng **sổ bàn giao đã mất hai dòng này**, xem cảnh báo đầu phiếu.

## Vấn đề 1 — Nhãn mức ưu tiên hiển thị ngược chiều

**Vấn đề:** Hồ sơ của một doanh nghiệp không thuộc diện ưu tiên nào được hệ thống tính đúng mức **1** — mức thấp nhất — nhưng màn hình lại hiển thị chữ **"Rất cao"**. Bảng nhãn trong đặc tả quy định 1 là "Thấp". Ban đầu chỗ này được báo lên như một mâu thuẫn của đặc tả; tra ra thì đặc tả không mâu thuẫn, chữ "Rất cao" nằm trên giao diện.

**(1) Phần mềm đúng SRS chưa? → SAI, và sai ở phần mềm chứ không ở đặc tả.**
- Đặc tả nhất quán: `srs-fr-05-vu-viec.md:1526-1530` — *"`1` | Thấp"*, *"`3` | Bình thường"*, *"`5` | Khẩn cấp"*; `srs-v3.5.md:5559` — *"**DN cao điểm phân công trước.**"* Tra "Rất cao"/"Rất thấp" toàn `_bmad-output/` và `docs/`: **không có** ở bảng nhãn ưu tiên nào.
- Phần mềm thì hiển thị ngược. Nguyên văn ô phản hồi tại chính dòng 127, đo ngày 04/08 trên bản dựng V1.0.5: *"Hệ thống tính đúng: giá trị lưu là 1. Nhưng giao diện lại hiển thị **'Rất cao'**, trong khi bảng nhãn ở dòng 1526 quy định 1 là 'Thấp'."*
- ⇒ Bảng nhãn "1 = Rất cao" là **mô tả giao diện đang chạy**, bị gán nhầm cho đặc tả khi báo lỗi.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không.** Mục 4.5.4.2.2: *"Mức độ ưu tiên | Số | … Giá trị từ 1 đến 5. Hệ thống tự tính theo tiêu chí ưu tiên của doanh nghiệp"* — không nêu nhãn chữ nào, nên không bênh được cách hiển thị hiện tại.

**(2) Đối tác yêu cầu có khác SRS không? → Không.** Kết quả mong đợi `NHSYC_09`: *"Hệ thống tự gán **mức ưu tiên thấp nhất**"* — đúng bằng `uu_tien = 1`. (Trên sổ bàn giao dòng này đã bị xoá; sổ nội bộ vẫn còn.)

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Cán bộ đọc nhãn để biết hồ sơ nào làm trước. Hiển thị ngược chiều khiến hồ sơ ít ưu tiên nhất trông như khẩn nhất — sai đúng công dụng của cột này.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa nhãn hiển thị cho khớp bảng nhãn đặc tả. Phần tính toán đã đúng (lưu ra 1), chỉ sai chỗ dịch số sang chữ. Không sửa SRS. Dev action: Có → Sheet: Giữ xử lý.**

> **Từ ngữ nhãn cụ thể** lấy theo bảng chú giải đã chốt ở Vấn đề 2 — sửa một lượt, tránh sửa hai lần.

---

## Vấn đề 2 — Hiển thị mức ưu tiên bằng nhãn chữ hay bằng số

**Vấn đề:** Ô "Mức độ ưu tiên" hiện ra cho cán bộ dưới dạng con số 1–5, hay dưới dạng chữ (Thấp / Bình thường / Cao / Khẩn cấp)? Đặc tả để ngỏ và tự ghi là chờ chủ đầu tư xác nhận; phần mềm thì đang hiện chữ "Trung bình" trong khi đặc tả viết "Bình thường".

**(1) Phần mềm đúng SRS chưa? → SRS chưa chốt, nhưng dấu treo đặt sai cấp.** `srs-fr-05-vu-viec.md:1522` — *"Nhãn là **đề xuất, cần CĐT xác nhận** (hoặc chốt hiển thị số kèm tooltip)"*. Dấu này trong kho dùng cho hai nhóm: nội dung do **văn bản pháp quy** quy định (18 ô Mẫu 01 Phụ lục NĐ 18/2026 — `srs-fr-06-chi-tra.md:160`) và **quyết định thiết kế thuộc thẩm quyền CĐT** (template cột Excel — `srs-fr-14-hop-dong-tv.md:134`; siết quyền cấp thao tác — `srs-v3.5.md:1440`). Đặt tên nhãn hiển thị không thuộc nhóm nào: NĐ 55/2019 Đ.4 K.4 chỉ quy định **thứ tự ưu tiên**, không quy định cách gọi tên từng mức; còn quy ước hiển thị dùng chung thì `srs-v3.5.md:572-580` (UI-01…09) và `:954-961` (DG-01…08) đều do BA ban hành, không mục nào mang dấu chờ CĐT.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Đã chọn hiển thị số.** Mục 4.5.4.2.2 khai kiểu dữ liệu là **Số**, *"Giá trị từ 1 đến 5"*, không kèm nhãn chữ.

**(2) Đối tác yêu cầu có khác SRS không? → Không nêu.**

**(3) Có bắt buộc cho luồng nghiệp vụ không? → Không tự thân**, nhưng không tách rời được: nhãn là **hệ quả** của thang điểm chốt ở Vấn đề 3.

**→ Kết luận: Loại 2 kiểu dọn đặc tả — BA chốt, không cần CĐT. Gỡ cụm "cần CĐT xác nhận" tại `:1522`. Số 1–5 là giá trị hiển thị chính, nhãn chữ chuyển thành chú giải theo cách *xếp nhóm* đã chốt. Dev action: Không (đổi cách hiển thị nằm trong phần Dev của Vấn đề 3) → Sheet: theo trạng thái chung của case.**  **✅ BA duyệt 04/08/2026.**

### Phương án xử lý (cập nhật SRS)

**Vì sao số là giá trị chính, nhãn chữ chỉ là chú giải:** thang này không phải mức khẩn cấp do người dùng tự đặt mà là **nhóm đối tượng ưu tiên theo luật**. Con số cho biết thứ tự xử lý, chú giải cho biết căn cứ. Đây cũng là nhánh mà bản bàn giao đã chọn, nên chốt như vậy thì không phải sửa `.docx`.

**Từ ngữ chú giải theo cách *xếp nhóm* đã chốt ở Vấn đề 3.** Bảng nhãn hiện tại phải thay, vì mức 3 là nhóm ưu tiên cao nhất do hệ thống tự tính mà lại đang mang nhãn "Bình thường" — đọc ngược nghĩa. Chú giải đề xuất:

| Số | Chú giải |
|:-:|---|
| 1 | Mức thường — xét theo thứ tự nộp hồ sơ |
| 2 | Doanh nghiệp có từ 30% lao động là người khuyết tật |
| 3 | Doanh nghiệp do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ |
| 4 · 5 | Cán bộ nâng mức, kèm lý do bắt buộc |

**Vị trí phải sửa:** `srs-fr-05-vu-viec.md:1522` (gỡ dấu treo, ghi rõ số là giá trị hiển thị) và `:1524-1530` (bảng chuyển thành bảng chú giải, nội dung theo hướng đã chốt). Chênh lệch "Trung bình" ↔ "Bình thường" tự khép theo đó.

> **Ô chốt của BA:** [ ] Xác nhận đây là quyết định của BA, gỡ dấu "cần CĐT xác nhận" tại `:1522` · [ ] Hiển thị **số 1–5** + nhãn chữ làm chú giải (khuyến nghị) · [ ] Giữ nhãn chữ làm giá trị hiển thị chính
> *(Bảng chú giải ở trên đi kèm cách xếp nhóm đã chốt — tick ô này là duyệt luôn bảng đó.)*
> **Người duyệt / ngày:** ……………

---

## Vấn đề 3 — Miền giá trị: cộng dồn cho ra tới 8, trường chỉ nhận 1–5

**Vấn đề:** Mỗi hồ sơ vụ việc có một ô "Mức độ ưu tiên" chỉ nhận số từ 1 đến 5, số càng cao càng được xử lý trước. Đặc tả bảo máy tự tính ô này bằng cách cộng điểm — doanh nghiệp do phụ nữ làm chủ cộng 3, nhiều lao động nữ cộng 2, có từ 30% lao động khuyết tật cộng 2, và mọi hồ sơ được cộng 1 — nên rất dễ ra con số lớn hơn 5, tức lớn hơn sức chứa của chính ô đó.

| Doanh nghiệp thuộc diện nào | Máy cộng ra | Ô chứa được không |
|---|:-:|---|
| Không thuộc diện ưu tiên nào | 1 | Được |
| Nhiều lao động nữ | 3 | Được |
| Từ 30% lao động khuyết tật | 3 | Được |
| Do phụ nữ làm chủ | 4 | Được |
| Phụ nữ làm chủ **+** nhiều lao động nữ | 6 | **Vượt** |
| Phụ nữ làm chủ **+** lao động khuyết tật | 6 | **Vượt** |
| Đủ cả ba diện | 8 | **Vượt** |

Nghĩa là **đúng những doanh nghiệp luật muốn ưu tiên nhất lại là những hồ sơ máy tính ra con số lưu không được** — hoặc báo lỗi không lưu được hồ sơ, hoặc bị cắt về 5 rồi không còn phân biệt với hồ sơ khác. Một dấu hiệu nữa cho thấy cách cộng không khớp thang 1–5: số **2** và số **5** không bao giờ xuất hiện.

**(1) Phần mềm đúng SRS chưa? → SRS tự mâu thuẫn, không chấm được.**
- `srs-fr-05-vu-viec.md:2037` và baseline `srs-v3.5.md:1537` — *"uu_tien | number | N | **CHECK BETWEEN 1 AND 5** | 3 |"*
- `srs-fr-05-vu-viec.md:196` và `:341` — *"Auto-calc `uu_tien` theo BR-CALC-07 (`la_nu_lam_chu` +3…; `so_lao_dong_nu` +2…; `so_lao_dong_khuyet_tat` +2…; FIFO +1)"*
- Vỡ ngay ở hai tiêu chí, không chỉ ở mức tối đa: phụ nữ làm chủ + ≥30% lao động khuyết tật = 3+2+1 = **6**.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → `.docx` KHÔNG mâu thuẫn, và đã tách sẵn hai đại lượng.** Đã rà toàn bộ chỗ nhắc "ưu tiên" trong bản v3.5:
- Mục **4.5.4.2.2** (hồ sơ vụ việc): *"**Mức độ ưu tiên** | Số | … | Do hệ thống tự tính | **Giá trị từ 1 đến 5**. Hệ thống tự tính theo tiêu chí ưu tiên của doanh nghiệp; cán bộ được điều chỉnh lại."*
- Mục **4.5.9.2.2** (bảng gợi ý phân công): cột *"**điểm ưu tiên**"*, và *"tính điểm ưu tiên của doanh nghiệp và sắp xếp theo thứ tự: ưu tiên doanh nghiệp giảm dần…"*
- Mục **4.7.4.2.2** và **4.10.21.2.2** chỉ đánh dấu ba trường DN là *"tiêu chí xét ưu tiên khi hỗ trợ pháp lý"*.

Bản bàn giao **không nơi nào** nêu công thức cộng điểm, không có `+3/+2/+2/+1`, không có trần 8. Nó dùng **hai tên gọi khác nhau** cho hai chỗ: "mức độ ưu tiên" lưu ở hồ sơ (miền 1–5) và "điểm ưu tiên" tính ra trong bảng gợi ý phân công.

**(2) Đối tác yêu cầu có khác SRS không? → Không.** Kết quả mong đợi `NHSYC_01` chỉ ghi *"Tự động tính điểm ưu tiên xử lý theo Nghị định 55/2019/NĐ-CP Điều 4"*.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Không chốt thì DN từ hai tiêu chí ưu tiên trở lên hoặc không lưu được hồ sơ, hoặc bị cắt cụt về 5 và mất thứ tự — đúng nhóm DN mà NĐ 55 Điều 4 muốn ưu tiên nhất.

**→ Kết luận: Loại 2 — SRS mâu thuẫn nội tại; chốt cách *xếp nhóm*, Dev tính lại theo đặc tả mới. Dev action: Có → Sheet: Giữ xử lý.**  **✅ BA duyệt 04/08/2026** (BA chốt trực tiếp trong phiên làm việc ngày 04/08/2026).

### Phương án xử lý (cập nhật SRS)

**Cách *xếp nhóm*:** số 1–5 chỉ **nhóm ưu tiên**, mỗi hồ sơ rơi vào một nhóm theo diện doanh nghiệp, không cộng điểm. Tách làm hai đại lượng đúng như bản bàn giao đã tách. Đặc tả `.md` cũng đã có sẵn tên gọi cho cả hai, chỉ là đang trộn vào một trường:

- `uu_tien` — mức lưu ở hồ sơ, miền 1–5, cán bộ điều chỉnh được, quy đổi theo ba bậc NĐ 55 Đ.4 K.4: **3** = DN do phụ nữ làm chủ hoặc dùng nhiều lao động nữ (điểm a) · **2** = DN có ≥30% lao động khuyết tật (điểm b) · **1** = còn lại (điểm c). Mức **4–5** dành cho cán bộ nâng khi khẩn, kèm lý do bắt buộc.
- `diem_uu_tien` — điểm thô cộng dồn, **tính lúc mở bảng gợi ý phân công**, chỉ dùng để xếp thứ tự, không lưu vào hồ sơ nên không vướng ràng buộc miền. Đặc tả đã có sẵn tên gọi và chỗ dùng: `srs-fr-05-vu-viec.md:765` khai nó là **dòng 9 bảng §Outputs của FR-V.I-09** — *"diem_uu_tien | number | Điểm ưu tiên tính toán"*. Đây là giá trị tính ra, không phải cột lưu trong entity.

**Không phải sửa `.docx`:** bản bàn giao đã chốt miền 1–5 và đã dùng hai tên gọi khác nhau cho hai chỗ — "mức độ ưu tiên" lưu ở hồ sơ, "điểm ưu tiên" tính khi gợi ý phân công. Phần bản bàn giao **không** nói là cách quy đổi ra 1–5 và ngưỡng "nhiều lao động nữ" (Vấn đề 4) — hai chỗ đó lấy theo phiếu này.

**Dọn kèm:** bỏ mặc định `uu_tien = 3` ở entity; ghi rõ "nộp trước hỗ trợ trước" là **quy tắc phá hòa** khi cùng mức, không phải điểm cộng — hiện "FIFO +1" cộng cho mọi vụ việc nên không phân biệt được gì.

**Vị trí phải sửa** — rà theo khái niệm, không chỉ theo dòng đã biết:

| Nhóm | File · dòng | Sửa gì |
|---|---|---|
| Phát biểu quy tắc | `srs-fr-05-vu-viec.md:2412` · baseline `srs-v3.5.md:5559` | Đổi sang mô hình xếp nhóm; ghi FIFO là quy tắc phá hoà |
| Tổng quan tiêu chí | `srs-fr-05-vu-viec.md:72-76` | Bốn dòng liệt kê "+3/+2/+2/+1 điểm" — giữ cho `diem_uu_tien` thô, **bỏ dòng "FIFO (+1 điểm)"** |
| Bước xử lý | `srs-fr-05-vu-viec.md:196` · `:341` · `:735` | Hai chỗ đầu: tính `uu_tien` theo bậc. `:735` là bảng gợi ý phân công — giữ cộng dồn nhưng bỏ "+1 FIFO" |
| Thực thể | `srs-fr-05-vu-viec.md:2037` · baseline `srs-v3.5.md:1537` | Bỏ mặc định 3 |
| Lý do override | baseline `srs-v3.5.md:1538` | Đang ghi *"Lý do ưu tiên (phụ nữ, KT...)"* — sửa thành: bắt buộc khi cán bộ nâng mức 4–5 |
| Bảng nhãn | `srs-fr-05-vu-viec.md:1524-1530` | Thay theo bảng chú giải ở Vấn đề 2 |
| Chú thích trường ở màn DN | `srs-fr-07-doanh-nghiep.md:582` · `:583` · `:584` | Ba chú thích còn ghi "+3 / +2" — sửa cả ba, không chỉ `:583` |
| Ghi chú FIFO ở màn DN | `srs-fr-07-doanh-nghiep.md:107` · `:570` | Còn ghi *"trả `uu_tien = 1` (FIFO)"* — giá trị 1 vẫn đúng, bỏ chữ FIFO |
| Màn DN tự quản | `srs-fr-10-quan-tri.md:1066` · `:1067` · `:1068` | Ba trường cùng ghi *"đầu vào chấm điểm ưu tiên"* — sửa cả ba |

**Dữ liệu cũ:** `uu_tien` lưu tại thời điểm tạo nên vụ việc cũ giữ giá trị cũ (phần lớn = 3). Không tính lại thì bảng gợi ý phân công trộn hai thang.

> **Còn chờ BA:** Dữ liệu vụ việc cũ: [ ] Tính lại theo thang mới · [ ] Giữ nguyên · **Người duyệt / ngày:** ……………

---

## Vấn đề 4 — Ngưỡng "doanh nghiệp sử dụng nhiều lao động nữ" chưa định lượng

**Vấn đề:** Một trong các diện được ưu tiên là "doanh nghiệp sử dụng nhiều lao động nữ", nhưng đặc tả không nói **nhiều là bao nhiêu** — trong khi diện kế bên thì ghi rõ "từ 30% lao động là người khuyết tật". Không có mốc thì không chấm được đúng sai, và mỗi lần triển khai lại ra kết quả khác. Đội phát triển đang tạm lấy một mốc duy nhất là 50% tổng số lao động; pháp luật về hỗ trợ doanh nghiệp nhỏ và vừa lại đặt **hai mốc theo quy mô**:

| Doanh nghiệp có | Theo pháp luật hỗ trợ doanh nghiệp nhỏ và vừa | Theo mốc 50% đang tạm dùng |
|---|---|---|
| 30 lao động nữ trên tổng 50 (60%) | Đạt — dưới 100 lao động thì cần từ 50% | Đạt |
| 40 lao động nữ trên tổng 90 (44%) | Không đạt | Không đạt |
| 45 lao động nữ trên tổng 120 (37,5%) | **Đạt** — từ 100 lao động trở lên chỉ cần từ 30% | **Không đạt** |
| 60 lao động nữ trên tổng 180 (33%) | **Đạt** | **Không đạt** |

Hai dòng cuối là chỗ mốc tạm dùng loại nhầm đúng những doanh nghiệp đông lao động nữ nhất trong phạm vi doanh nghiệp nhỏ và vừa.

**(1) Phần mềm đúng SRS chưa? → SRS thiếu, không chấm được.** Cụm "vượt ngưỡng" xuất hiện ở `srs-fr-05-vu-viec.md:196`, `srs-fr-07-doanh-nghiep.md:583`, `srs-fr-10-quan-tri.md:1066` — không nơi nào định nghĩa ngưỡng. Tiêu chí kế bên thì định lượng rõ (`≥30% so_lao_dong`).

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không.** Mục 4.5.4.2.2 chỉ ghi *"Hệ thống tự tính theo tiêu chí ưu tiên của doanh nghiệp"*.

**(2) Đối tác yêu cầu có khác SRS không? → Không nêu.** `NHSYC_10` chỉ chép lại tên điều luật, trạng thái `N/R`.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Không có ngưỡng thì mỗi lần triển khai ra kết quả khác và không kiểm thử được `NHSYC_10`.

**→ Kết luận: Loại 2 — SRS thiếu định lượng; lấy ngưỡng theo định nghĩa pháp quy sẵn có, Dev áp theo đặc tả mới. Dev action: Có → Sheet: Giữ xử lý.**  **✅ BA duyệt 04/08/2026** (BA chốt trực tiếp trong phiên làm việc ngày 04/08/2026).

### Phương án xử lý (cập nhật SRS)

Khái niệm này **đã có định nghĩa pháp quy ngay trong khung pháp luật hỗ trợ doanh nghiệp nhỏ và vừa** — không phải tự đặt, cũng không phải mượn từ ngành luật khác.

**Nghị định 80/2021/NĐ-CP Điều 3 khoản 8** (quy định chi tiết Luật Hỗ trợ doanh nghiệp nhỏ và vừa), nguyên văn:

> *"Doanh nghiệp nhỏ và vừa sử dụng nhiều lao động nữ là doanh nghiệp có số lao động nữ chiếm từ 50% trở lên trên tổng số lao động trong trường hợp doanh nghiệp sử dụng dưới 100 lao động; chiếm từ 30% trở lên trên tổng số lao động trong trường hợp doanh nghiệp sử dụng từ 100 lao động trở lên."*

Đây là văn bản đúng ngữ cảnh: NĐ 55/2019 về hỗ trợ pháp lý cho DNNVV nằm trong khung Luật Hỗ trợ DNNVV 2017, và NĐ 80/2021 là nghị định quy định chi tiết chính Luật đó. Phần mềm cũng đã dùng NĐ 80/2021 ở chỗ khác — quy tắc xác định quy mô doanh nghiệp (`srs-v3.5.md:5557`) cite đúng Điều 5 của nghị định này.

**Kèm theo, chốt luôn định nghĩa của diện ưu tiên đứng cạnh nó.** NĐ 55 Đ.4 K.4 điểm a gộp hai diện trong cùng một câu, diện còn lại cũng đã có định nghĩa pháp quy mà đặc tả đang bỏ trống: **Luật Hỗ trợ DNNVV 2017 Điều 3 khoản 1** — *"doanh nghiệp nhỏ và vừa do phụ nữ làm chủ là doanh nghiệp nhỏ và vừa có một hoặc nhiều phụ nữ sở hữu từ 51% vốn điều lệ trở lên, trong đó có ít nhất một người quản lý điều hành doanh nghiệp đó"*. Hiện đặc tả chỉ để ô đánh dấu "Doanh nghiệp do nữ làm chủ" không kèm căn cứ, nên mỗi cán bộ tick theo một cách hiểu.

**Nguồn đã kiểm chứng** (web-verify 04/08/2026, mỗi văn bản đối chiếu hai nguồn độc lập): NĐ 80/2021 Đ.3 K.8 và Luật Hỗ trợ DNNVV 2017 Đ.3 K.1 — bản toàn văn trên cổng văn bản VCCI (`vanban.vcci.com.vn`) và Cổng thông tin Hội Liên hiệp Phụ nữ Việt Nam (`hoilhpn.org.vn`). NĐ 80/2021 ban hành 26/8/2021, hiệu lực 15/10/2021, thay NĐ 39/2018 — **còn hiệu lực**.

*Lưu ý khi trình CĐT:* NĐ 55 Đ.4 K.4 điểm a dùng chữ *"nhiều lao động nữ **hơn**"* — nghĩa so sánh giữa các hồ sơ cùng đợt. Phần mềm chấm điểm ngay khi tạo hồ sơ nên buộc phải quy về ngưỡng tuyệt đối; NĐ 80/2021 là cách quy đổi có căn cứ nhất vì nó định nghĩa chính khái niệm đó trong cùng khung pháp luật.

**Vị trí phải sửa:**
- Phát biểu quy tắc: `srs-fr-05-vu-viec.md:2412` và baseline `srs-v3.5.md:5559` — ghi hai ngưỡng kèm cite.
- Chú thích trường ở màn Doanh nghiệp: `srs-fr-07-doanh-nghiep.md:582` (do phụ nữ làm chủ) · `:583` (số lao động nữ).
- **Thực thể `DOANH_NGHIEP` và bản sao ở baseline** — bốn dòng hiện chỉ ghi *"(NĐ55 Điều 4 ưu tiên)"*, chưa có ngưỡng lẫn định nghĩa: `srs-fr-07-doanh-nghiep.md:705` · `:707` và baseline `srs-v3.5.md:1666` · `:1668`. Bổ sung cite vào cột ràng buộc để người đọc thực thể không phải lần sang file khác.

> **Dòng liên đới trên sổ:** `QLDNDHTPL_25` dòng 697 — *"Kiểm tra hiển thị Nhóm 3 — Tiêu chí ưu tiên theo Nghị định 55/2019/NĐ-CP Điều 4"* trên màn Doanh nghiệp, đang `Fail` / `Reopent`, tranh chấp bố cục nhóm theo bản bàn giao 10/7. Đây chính là nhóm chứa ba trường đầu vào của quy tắc ưu tiên, nên khi BA sửa đặc tả theo quyết định trên thì rà luôn dòng này để không phải sửa hai lượt.

> **✅ BA chốt 04/08/2026:** ngưỡng "nhiều lao động nữ" theo **NĐ 80/2021 Điều 3 khoản 8**; định nghĩa "do phụ nữ làm chủ" theo **Luật Hỗ trợ DNNVV 2017 Điều 3 khoản 1**. Cả hai ghi kèm cite vào đặc tả theo danh sách vị trí ở trên.

---

## Vấn đề 5 — Luồng DN tự gửi hồ sơ chưa tự tính mức ưu tiên

**Vấn đề:** Hồ sơ do cán bộ nhập tay thì được máy tính mức ưu tiên, còn hồ sơ do doanh nghiệp tự gửi qua chuyên trang thì không — nằm mãi ở giá trị mặc định. Đội phát triển hỏi có mở rộng cách tính sang luồng doanh nghiệp không; phía kiểm thử nêu cùng điểm này dưới dạng "đặc tả liệt kê phạm vi áp dụng không thống nhất".

**(1) Phần mềm đúng SRS chưa? → SAI, và SRS đã quy định sẵn.** Luồng DN tự gửi là **FR-V.I-02 (UC52)**, không phải FR-V.I-01:
- `srs-fr-05-vu-viec.md:160-167` — *"FR-V.I-02: Gửi hồ sơ yêu cầu HTPL (UC52) … SCR-V.I-02 (form DN gửi HS qua chuyên trang) … **Tác nhân:** Doanh nghiệp"*
- `srs-fr-05-vu-viec.md:196` (Processing bước 4 của chính FR đó) — *"**Auto-calc `uu_tien` theo BR-CALC-07**… Tối thiểu `uu_tien=1` cho mọi VV"*
- FR-V.I-01 (UC51) là màn quản lý danh sách của CB NV, §Inputs chỉ có bộ lọc — không tạo hồ sơ.

Mục "Applied in" ở `:2414` chỉ ghi FR-V.I-09, nhưng bảng tổng quan `:2330` ghi đủ **FR-V.I-02, 04, 09** và Processing của chính hai FR kia yêu cầu tự tính. Mô tả hành vi trong Processing thắng một dòng chỉ mục.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không.** Mục 4.5.2.2.3 (DN gửi hồ sơ) mô tả hệ thống *"tự sinh"* các giá trị khi tiếp nhận, không loại trừ mức ưu tiên.

**(2) Đối tác yêu cầu có khác SRS không? → Không đặt ra**, ngoài phạm vi test case.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Hồ sơ DN tự gửi vào cùng hàng đợi phân công; để mặc định thì tiêu chí ưu tiên NĐ 55 Điều 4 mất tác dụng ở đúng kênh DN dùng nhiều nhất.

**→ Kết luận: Loại 1 — Lỗi phần mềm, không phải câu hỏi cho BA. Dev bổ sung cho cả hai luồng FR-V.I-02 và FR-V.I-04 theo cách *xếp nhóm* đã chốt ở Vấn đề 3. Đồng thời dọn `:2414` cho khớp `:2330`. Dev action: Có → Sheet: Giữ xử lý.**

> **Ô chốt của BA:** [ ] Xác nhận Dev bổ sung auto-calc cho FR-V.I-02, không tách yêu cầu cải tiến riêng · **Người duyệt / ngày:** ……………

---

## Vấn đề 6 — Ô "Độ ưu tiên" hiển thị mã quy tắc nội bộ, lại là mã đã lỗi thời

**Vấn đề:** Ô "Độ ưu tiên" trên biểu mẫu nhập tay đang hiện cho người dùng cuối nguyên dòng chữ "3 — Trung bình (mặc định BR-CALC-04)" — kèm cả mã quy tắc nội bộ, mà mã đó lại là mã cũ đã được đổi tên trong đặc tả.

**(1) Phần mềm đúng SRS chưa? → SAI.** `srs-fr-05-vu-viec.md:1492` (quy ước chung khi đọc Mục 3): *"Mã DB **không bao giờ** xuất hiện trên giao diện người dùng"* — quy ước viết cho mã enum, nhưng mã quy tắc nghiệp vụ càng không phải thứ người dùng cuối cần thấy. Mã `BR-CALC-04` nay thuộc nghiệp vụ khác ở `srs-fr-08` / `srs-fr-10` (`srs-fr-05-vu-viec.md:19` ghi lịch sử đổi mã).

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không.** Mục 4.5.4.2.2 mô tả ô này là *"Số … Do hệ thống tự tính"*, không có chuỗi mã nào.

**(2) Đối tác yêu cầu có khác SRS không? → Không nêu** — điểm do QA tự phát hiện.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ**, ở mức tối thiểu: mã sai dẫn người đọc tra nhầm quy tắc.

**→ Kết luận: Loại 1 — Lỗi phần mềm, gỡ chuỗi mã khỏi giao diện, không phải câu hỏi cho BA. Dev action: Có → Sheet: Giữ xử lý.**

### Tình trạng hiện nay

Ngày 03/08 tổ kiểm thử thấy **hai lỗi cùng nằm trong một dòng chữ** ở ô này. Phép đo mới nhất ngày 04/08 (bản dựng V1.0.5, ghi tại chính dòng 127) chỉ trả lời được một:

| | Lỗi quan sát ngày 03/08 | Theo phép đo 04/08 |
|---|---|---|
| a | Ô luôn hiện số **3** dù doanh nghiệp không thuộc diện ưu tiên nào — tức không tự tính, gán cứng | **Đã hết** — *"giá trị lưu là 1"* |
| b | Kèm chuỗi `(mặc định BR-CALC-04)` | **Chưa rõ** — phép đo không nhắc tới, không nói còn cũng không nói đã gỡ |

Đề nghị QA nhìn lại đúng ô đó một lần để xác nhận riêng phần (b). Nếu chuỗi mã đã hết thì mục này đóng cùng lượt với Vấn đề 1 — cả hai đều là sửa cách hiển thị trên cùng một ô, Dev làm một lần là xong.

---

## Vấn đề 7 — `TKHSYCHTPL_OOS_01`: cột "Cảnh báo thời hạn" hiện nhãn không có trong đặc tả

**Vấn đề:** Ở màn danh sách vụ việc, lọc "Sắp hết hạn" lại trả về hồ sơ đã đóng — một hồ sơ Từ chối, một hồ sơ Hoàn thành. Ngay trên hai dòng đó, cột "Cảnh báo thời hạn" lại hiện chữ "Đã hoàn thành". Bộ lọc và cột hiển thị nói hai điều khác nhau trên cùng một màn, người dùng dễ tưởng bộ lọc trả sai bản ghi. Sổ nội bộ tab `tuần 2` dòng **145** (`Verify` = BA confirm), do tổ kiểm thử mở khi verify `TKHSYCHTPL_03` (dòng 129, nay `Verify` = Pass). 

**(1) Phần mềm đúng SRS chưa? → Chỉ sai đúng một chỗ: nhãn hiển thị.**
- **Nhãn "Đã hoàn thành" sai đặc tả.** `srs-fr-05-vu-viec.md:1656` liệt kê cột này đúng **4 mức** *"🟢 BINH_THUONG / 🟡 SAP_HET / 🔴 QUA_HAN / ⚫ QUA_HAN_NGHIEM_TRONG"*, điều kiện hiển thị *"Luôn"* — danh sách đóng, giá trị thứ 5 không có căn cứ. Entity `:2031` cũng `CHECK IN` đúng 4 mã.
- **Hai phần còn lại thì đúng đặc tả.** Giữ nguyên mức cảnh báo của hồ sơ đã đóng là đúng `:1436` — công việc tự động chỉ *"Lấy danh sách VV đang hoạt động (DA_TIEP_NHAN, DANG_KIEM_TRA, DA_PHAN_CONG, DANG_XU_LY, CHO_PHE_DUYET)"*. Bộ lọc trả về hai hồ sơ đó cũng đúng, vì nó lọc theo giá trị đã lưu và giá trị đã lưu đang là "Sắp hết hạn".

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không.** Không mục nào của bản bàn giao định nghĩa mức thứ 5, cũng không nói bộ lọc loại trừ hồ sơ đã đóng.

**(2) Đối tác yêu cầu có khác SRS không? → Không đặt ra** — dòng do QA mở, không có Kết quả mong đợi của đối tác.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ, nhưng chỉ ở phần nhãn.** Cột đang hiện một giá trị không tồn tại trong hệ thống. Còn việc hồ sơ đã đóng có nên lọt bộ lọc hay không thì đặc tả **không cấm**, phần mềm đang chạy nhất quán với chính nó — đây là chuyện dễ chịu hơn khi dùng, không phải chuyện đúng sai.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev gỡ nhãn ngoài đặc tả, hiển thị đúng mức đã lưu trong bốn mức. **Không sửa SRS, không cần BA chốt.** Dev action: Có → Sheet: Giữ xử lý.**

### Việc Dev phải làm

Bỏ nhãn "Đã hoàn thành" khỏi cột "Cảnh báo thời hạn". Với hồ sơ đã đóng, cột hiển thị đúng mức đang lưu — trong trường hợp hai hồ sơ QA quan sát là **"Sắp hết hạn"**.

> **Lưu ý cho vòng kiểm thử sau:** sửa xong thì hồ sơ Hoàn thành sẽ hiện "Sắp hết hạn" ở cột này. Đó là **kết quả đúng theo đặc tả hiện hành**, không phải lỗi mới — mức cảnh báo được giữ nguyên tại thời điểm hồ sơ đóng.

**Nếu BA thấy cách hiển thị đó vẫn gây hiểu nhầm** thì đây là **yêu cầu cải tiến**, không phải lỗi: khi hồ sơ đóng thì xoá mức cảnh báo, bộ lọc "Mức SLA" loại trừ trạng thái kết thúc, cột để trống. Đã kiểm sẵn tác động nếu sau này BA muốn làm: báo cáo nhóm IX dùng chiều SLA (`srs-fr-11-bao-cao.md:245-260`) chỉ *"Đếm số vụ việc **đang xử lý** (snapshot tại thời điểm query)"* và tự tính mức từ deadline, **không đọc giá trị đã lưu** — nên xoá đi không làm hỏng báo cáo nào.

*(Mục này là lỗi phần mềm thuần — Dev sửa, không có ô chốt. Phần loại trừ hồ sơ đã đóng khỏi bộ lọc nếu muốn làm thì mở phiếu yêu cầu cải tiến riêng.)*

---

# B. Đào tạo, tập huấn

## Vấn đề 8 — `KTDGKQHT_02`: bốn trường số buổi không có ở đâu trên giao diện

**Vấn đề:** Khi chấm kết quả học tập, hệ thống phải cho biết mỗi học viên có mặt mấy buổi, vắng có phép mấy buổi, vắng không phép mấy buổi trên tổng bao nhiêu buổi. Bốn con số này là căn cứ tính tỷ lệ chuyên cần, mà tỷ lệ chuyên cần lại quyết định học viên Đạt hay Không đạt. Đối tác báo màn hình không có bốn con số đó. Thực tế:

| Con số | Hiện ở đâu trên phần mềm |
|---|---|
| Số buổi có mặt | Gộp trong ô "Chuyên cần" dạng x/y |
| Tổng số buổi | Gộp trong ô "Chuyên cần" dạng x/y |
| Số buổi vắng có phép | **Không có ở đâu** |
| Số buổi vắng không phép | **Không có ở đâu** |

Buổi vắng có phép **không** bị trừ chuyên cần, buổi vắng không phép thì bị trừ — thiếu hai con số này thì cán bộ lẫn học viên không kiểm chứng được vì sao ra kết quả Đạt hay Không đạt. Sổ nội bộ tab `tuần 2` dòng **116** (`Verify` = BA confirm).

**(1) Phần mềm đúng SRS chưa? → SAI.** Bốn trường là §Outputs của chính FR-III-05 (UC24): `srs-fr-03-dao-tao.md:600-603`. Chúng không phải dữ liệu trang trí — `:604` quy định *"% chuyên cần = (so_buoi_co_mat + **so_buoi_vang_phep**) / tong_buoi × 100"*, và tỷ lệ này quyết định Đạt/Không đạt theo BR-KQ-02 (`:607`). Phần mềm hiện chỉ gộp 2 trong 4 trường vào ô "Chuyên cần" và **không có** hai trường vắng ở bất kỳ đâu ⇒ người dùng không kiểm chứng được con số quyết định kết quả học tập.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → `.docx` đứng về phía "phải có".** Mục **4.3.5.2.2** liệt kê đủ bốn dòng *"Số buổi có mặt | Chỉ đọc"*, *"Số buổi vắng có phép | Chỉ đọc"*, *"Số buổi vắng không phép | Chỉ đọc"*, *"Tổng số buổi | Chỉ đọc"* và *"Tỷ lệ chuyên cần … bằng tổng số buổi có mặt cộng số buổi vắng có phép, chia cho tổng số buổi, nhân 100"*.

**(2) Đối tác yêu cầu có khác SRS không? → Không.** Kỳ vọng của đối tác khớp §Outputs và khớp bản bàn giao. Chỗ thiếu nằm ở **bảng cột SCR** trong `.md` (`:1896` tab Điểm danh, `:1901` tab Kết quả) — cả hai đều không liệt kê, đây là chỗ đặc tả `.md` chưa đồng bộ.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Ba trong bốn trường là đầu vào của công thức xét Đạt/Không đạt.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev bổ sung. Không cần 4 cột rời: bản bàn giao khai đây là thông tin chỉ đọc trên màn hình. Giữ ô "Chuyên cần" nhưng ghi rõ tử số gồm cả buổi vắng có phép, và bổ sung hai số buổi vắng. Kèm Loại 2 nhỏ: bổ sung 4 trường vào bảng cột `.md` `:1901` cho hết lệch. Dev action: Có → Sheet: Giữ xử lý.**  **✅ BA duyệt 04/08/2026.**

> ⚠️ **Một điểm lệch chưa ai nêu, đề nghị QA đo lại:** theo bảng cột QA ghi nhận, web có cột **"Chuyên cần"** (không có trong `:1901`) và **không có** cột **"Đề kiểm tra"** (có trong `:1901`). Nếu đúng thì đây là điểm lệch thứ hai của cùng bảng, cần xử lý một lượt.

### Phương án xử lý (cập nhật SRS)

Phần Dev là bổ sung hai số buổi vắng lên giao diện. Phần đặc tả là dọn bảng cột của tab, hiện đang thiếu chính những gì màn hình phải hiện.

**Sửa `srs-fr-03-dao-tao.md:1901` (SCR-III-02, Tab 5 "Kết quả kiểm tra").** Danh sách cột hiện tại: *STT · Họ tên · Email · Số điện thoại · Đơn vị · Đề kiểm tra · Điểm · Xếp loại · Kết quả · Ghi chú*. Bổ sung **một cột "Chuyên cần"** đặt trước cột "Đề kiểm tra", ghi rõ cách trình bày: hiện `{số buổi tính chuyên cần}/{tổng số buổi}` kèm tỷ lệ phần trăm, và **rê chuột hiện tách bạch ba con số**: số buổi có mặt, số buổi vắng có phép, số buổi vắng không phép. Ghi kèm công thức đã có sẵn ở `:604` — *"% chuyên cần = (so_buoi_co_mat + so_buoi_vang_phep) / tong_buoi × 100"* — để người đọc biết vì sao buổi vắng có phép vẫn nằm ở tử số.

**Không bổ sung bốn cột rời**, vì bản bàn giao mục 4.3.5.2.2 khai bốn con số này là **thông tin chỉ đọc trên màn hình**, không khai là cột của bảng. Một ô gộp kèm chú giải đáp ứng đủ mà không kéo bảng dài thêm bốn cột.

**Không đụng §Outputs** (`:600-603`) — bốn trường ở đó vốn đã đúng và đang là đầu vào của công thức xét Đạt/Không đạt. Không đụng baseline, không phát sinh mã BR/FR mới.

> ⚠️ **Một điểm lệch thứ hai cần QA xác nhận trước khi sửa:** theo bảng cột tổ kiểm thử ghi nhận, màn hình đang có cột **"Chuyên cần"** (chưa có trong `:1901`) nhưng **thiếu cột "Đề kiểm tra"** (có trong `:1901`). Nếu đúng thì phải sửa một lượt: thêm "Chuyên cần" vào đặc tả và trả lại "Đề kiểm tra" trên giao diện.

> **Ô chốt của BA:** [ ] Bổ sung hai số buổi vắng vào ô Chuyên cần + cập nhật `:1901` (khuyến nghị) · [ ] Hiển thị đủ 4 cột rời · [ ] Giữ nguyên, sửa Expected của test case · **Người duyệt / ngày:** ……………

---

## Vấn đề 9 — `PDKHDTTH_04`: chặn duyệt kế hoạch khác đơn vị mà không báo lý do

**Vấn đề:** Cán bộ phê duyệt của đơn vị khác mở một kế hoạch đào tạo đang chờ duyệt thì không thấy nút Phê duyệt và Từ chối, cũng không có thông báo nào cho biết vì sao. Đối tác cho rằng hệ thống phải hiện một câu giải thích là không có quyền. Sổ nội bộ tab `tuần 2` dòng **120** (`Verify` = BA confirm).

**(1) Phần mềm đúng SRS chưa? → ĐÚNG.** Chặn là đúng BR-AUTH-05 (`srs-v3.5.md:5480` — *"Phê duyệt cùng đơn vị (strict) … Áp dụng cho mọi action duyệt"*) và đúng Preconditions FR-III-15 (`srs-fr-03-dao-tao.md:1217`). FR-III-15 không có mục Error Handling nào — đã đọc trọn mục `:1208-1231`, đi thẳng từ Postconditions sang Acceptance Criteria.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → `.docx` nói thẳng là ẩn nút.** Mục **4.3.15.2.3 STT 1 "Phê duyệt kế hoạch năm"**: *"**Điều kiện hiển thị**: kế hoạch ở trạng thái 'Chờ duyệt', **người sử dụng là CB PD cùng đơn vị**"*. Cùng khuôn với khóa học ở mục 4.3.1.2.3 STT 10. Vậy không cần viện tới quy ước M-05 (`srs-v3.5.md:683` — vốn chỉ viết cho **menu item**): bản bàn giao đã quy định điều kiện hiển thị của chính nút này.

**(2) Đối tác yêu cầu có khác SRS không? → CÓ.** Đối tác đòi một thông báo mà cả `.md` lẫn `.docx` đều không quy định.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → KHÔNG.** Nút không hiện thì người dùng không thao tác nhầm; đây là mong muốn về trải nghiệm.

**→ Kết luận: Loại 3 — Phần mềm đúng đặc tả. Đề nghị đối tác cập nhật Kết quả mong đợi. Dev action: Không → Sheet: Reject. Kèm một việc của BA: sửa `srs-fr-03-dao-tao.md:1774` bổ sung điều kiện cùng đơn vị cho nút Phê duyệt/Từ chối, vì dòng này đang chỉ ghi trạng thái + vai trò, lệch BR-AUTH-05 và lệch bản bàn giao.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Theo tài liệu bàn giao, nút Phê duyệt và Từ chối của kế hoạch đào tạo chỉ hiển thị với cán bộ phê duyệt **cùng đơn vị** với kế hoạch. Cán bộ khác đơn vị không nhìn thấy nút nên không phát sinh thao tác, do đó cũng không có thông báo từ chối quyền. Phần mềm đang chạy đúng như vậy.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật lại Kết quả mong đợi của phiếu này cho khớp tài liệu.

> **Ô chốt của BA:** [ ] Xác nhận giữ cách ẩn nút + sửa `:1774` cho khớp (khuyến nghị) · [ ] Đổi sang hiện nút và báo lỗi khi bấm · **Người duyệt / ngày:** ……………

---

## Vấn đề 10 — `QLDXDTTH_11`: cán bộ có tiếp nhận được đề xuất đào tạo không `[CẦN ĐO LẠI]`

**Vấn đề:** Tổ kiểm thử nội bộ báo doanh nghiệp gửi đề xuất đào tạo xong thì hồ sơ nằm mãi ở trạng thái "Mới gửi" — cán bộ mở lên không có nút Tiếp nhận, cột Hành động chỉ là dấu gạch ngang. Nhưng **trên sổ chính, chính chức năng đó đã kiểm và Pass**:

| Nguồn | Đo trên | Kết quả |
|---|---|---|
| Sổ chính, **`QLDXDTTH_08` dòng 337** — *"Cán bộ nghiệp vụ Tiếp nhận đề xuất"* | môi trường bàn giao | **Pass** — *"Cập nhật trạng thái đề xuất: 'Mới' → 'Đã tiếp nhận'. Gửi thông báo cho người gửi. Lưu vết thao tác. Hệ thống hiển thị thông báo 'Đã tiếp nhận đề xuất'."* |
| Phiếu re-verify của tổ kiểm thử (dòng tự mở, không có trên sổ chính) | bản dựng V1.0.5, máy chủ khác | Không thấy nút Tiếp nhận |

Nút "Gửi đề xuất mới" hiện với cán bộ cũng chỉ tổ nội bộ ghi nhận, sổ chính không có phiếu nào.

⇒ **Trước khi kết luận, phải đo lại trên đúng môi trường bàn giao.** Cùng một chức năng mà hai nơi cho kết quả ngược nhau thì nhiều khả năng khác nhau ở bản dựng, ở vai trò đăng nhập, hoặc ở đường đi vào màn hình — `QLDXDTTH_08` đi theo đường *Chương trình đào tạo → tab "Đề xuất đào tạo" → nút "Tiếp nhận" trên dòng*.

**(1) Phần mềm đúng SRS chưa? → SAI.** `srs-fr-03-dao-tao.md:1045` — *"DN/NHT gửi đề xuất đào tạo. **CB NV tiếp nhận**"*; SCR-III-01 Thành phần 8 (`:1875`) khai cột *"Hành động (Xem · **Tiếp nhận** · **Đánh dấu thực hiện**)"*; §Outputs của chính FR-III-13 khai enum 3 trạng thái `MOI/DA_TIEP_NHAN/DA_THUC_HIEN` và Error Handling có `ERR-DX-02` *"Không thể sửa đề xuất đã tiếp nhận"* — tức hai trạng thái sau bắt buộc phải có đường đi tới.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → `.docx` khẳng định mạnh hơn cả `.md`.** Mục **4.3.13.1**: *"Người sử dụng là **CB NV cùng đơn vị tiếp nhận: xem, tiếp nhận và đánh dấu đã thực hiện** đề xuất"*; mục **4.3.13.2.3** có hẳn **STT 4 "Tiếp nhận đề xuất"** và **STT 5 "Đánh dấu đã thực hiện"**, điều kiện hiển thị *"người sử dụng là cán bộ nghiệp vụ"*. Cùng mục, **STT 1 "Gửi đề xuất đào tạo"** ghi rõ người gửi là *"doanh nghiệp hoặc người hỗ trợ pháp lý"*.

**(2) Đối tác yêu cầu có khác SRS không? → Không.** Kết quả mong đợi của `QLDXDTTH_08` trùng đúng những gì `.md` và `.docx` mô tả.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ, nếu tái hiện được.** Không có bước tiếp nhận thì đề xuất không bao giờ rời trạng thái đầu tiên. Nhưng sổ chính đang nói chức năng chạy được.

**→ Kết luận: Chưa chốt được — chờ đo lại. Phần đặc tả thì đã rõ và không phải hỏi BA: quyền tiếp nhận thuộc CB NV, cả `.md` lẫn `.docx` đều nói vậy. Nếu đo lại vẫn thiếu nút thì là Loại 1, Dev bổ sung. Nếu chạy đúng như `QLDXDTTH_08` thì đóng, không có việc cho Dev. Dev action: Chưa xác định → Sheet: giữ nguyên `QLDXDTTH_08` = `Pass`, không mở lại khi chưa tái hiện được.**

### Việc cần dọn bất kể kết quả đo lại

**Ma trận phân quyền `srs-v3.5.md:1309` sai so với chính đặc tả chức năng.** Dòng `DE_XUAT_DAO_TAO` chỉ cấp `R`/`R*` cho mọi vai trò cán bộ — không có quyền sửa. Nhưng "Tiếp nhận" là thao tác đổi trạng thái, tức phải có quyền sửa; và `QLDXDTTH_08` đã Pass nghĩa là phần mềm **đang** cho cán bộ làm việc đó. Ma trận đang mô tả sai hệ thống thật.

> **Ô chốt của BA:** [ ] Bổ sung quyền `U` cho CB NV trên `DE_XUAT_DAO_TAO` tại ma trận `:1309` cho khớp đặc tả chức năng (khuyến nghị) · [ ] Giữ ma trận và sửa đặc tả chức năng theo hướng ngược lại · **Người duyệt / ngày:** ……………

---

# C. Mạng lưới tư vấn viên

## Vấn đề 11 — `DKTGMLTVV_04`: nhóm 3 form Thêm mới TVV có 3 trường hay 2 trường

**Vấn đề:** Ở biểu mẫu thêm mới tư vấn viên, nhóm "Tổ chức & Mạng lưới" đang có ba ô: Tổ chức hành nghề chính, Tổ chức đối tác, Lĩnh vực pháp luật. Đối tác cho rằng nhóm này chỉ được có hai ô và dẫn bản tài liệu bàn giao ngày 10/7. Sổ nội bộ tab `tuần 2` dòng **122** (`Verify` = BA confirm).

**(1) Phần mềm đúng SRS chưa? → ĐÚNG, đủ 3 trường.** `srs-fr-04-chuyen-gia-tvv.md:1515` Tổ chức chính (tùy chọn) · `:1516` **Tổ chức đối tác** (chọn nhiều, N:N) · `:1517` Lĩnh vực pháp luật (bắt buộc ≥ 1).

**(1b) Bản `.docx` đối tác cầm có nói khác không? → KHÔNG.** Bản bàn giao v3.5 mục **4.4.1.2.2** liệt kê đủ, trong đó có *"Tổ chức đối tác | Danh sách chọn nhiều | Không | — | Một tư vấn viên có thể liên kết với nhiều tổ chức đối tác"*. Không có bản bàn giao nào chỉ hai trường.

**(2) Đối tác yêu cầu có khác SRS không? → CÓ**, lệch cả `.md` lẫn bản bàn giao v3.5. Tên trường họ ghi trong phiếu (*"Lĩnh vực pháp luật đăng ký"*, *"Tổ chức tư vấn chủ quản"*) cũng không khớp tên trong bản bàn giao.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → Không** — gỡ trường sẽ mất quan hệ N:N đã có dữ liệu, đồng thời đảo một quyết định BA vừa ra ngày 30/07 (CHANGELOG sửa mục 4.1 cùng nhóm mà giữ nguyên mục 4.2).

**→ Kết luận: Loại 3 — Phần mềm đúng cả bản gốc lẫn bản bàn giao. Đề nghị đối tác cập nhật Kết quả mong đợi. Dev action: Không → Sheet: Reject.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Nhóm "Tổ chức & Mạng lưới" gồm ba trường: Tổ chức hành nghề chính, Tổ chức đối tác và Lĩnh vực pháp luật. Trường "Tổ chức đối tác" có trong tài liệu bàn giao hiện hành, phục vụ trường hợp một tư vấn viên cộng tác với nhiều tổ chức. Phần mềm đang hiển thị đúng ba trường này.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật lại Kết quả mong đợi cho khớp bản bàn giao hiện hành.

> **Ô chốt của BA:** [ ] Xác nhận giữ 3 trường theo v3.5 (khuyến nghị) · [ ] Gỡ "Tổ chức đối tác" khỏi form Thêm mới · **Người duyệt / ngày:** ……………

---

## Vấn đề 12 — `DKTGMLTVV_05`: "File thẻ hành nghề" được đặc tả ở cả nhóm 2 lẫn nhóm 4

**Vấn đề:** Ô tải "File thẻ hành nghề" đang nằm ở nhóm "Thông tin nghề nghiệp" của biểu mẫu tư vấn viên. Nhưng đặc tả lại liệt kê chính ô đó ở **cả hai** nhóm — nhóm nghề nghiệp và nhóm hồ sơ đính kèm — mà không câu nào nói ô này xuất hiện hai lần. Đối tác báo nhóm hồ sơ đính kèm bị thiếu. Sổ nội bộ tab `tuần 2` dòng **123** (`Verify` = BA confirm).

**(1) Phần mềm đúng SRS chưa? → SRS tự mâu thuẫn.** `srs-fr-04-chuyen-gia-tvv.md:1508` (mục 3.6, nhóm 2) — *"File thẻ hành nghề | tải file | PDF, tối đa 10MB; **bắt buộc nếu Loại = Tư vấn viên**"*; `:1520` (mục 5.2, nhóm 4) — *"File thẻ hành nghề | tải 1 file | PDF, tối đa 10MB"*, ô ràng buộc để trống. Không câu nào nói trường xuất hiện ở cả hai chỗ.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → `.docx` chỉ khai MỘT lần, kèm ràng buộc của nhóm 2.** Bản v3.5 mục 4.4.1.2.2 khai đúng **một lần**: *"Tệp thẻ hành nghề | Tệp | **Có khi loại là Tư vấn viên**"*, kèm ràng buộc trùng với `:1508` của `.md`.

**(2) Đối tác yêu cầu có khác SRS không? → Đối tác quan sát đúng** (nhóm 4 không có trường), chỉ kỳ vọng vị trí khác.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → Không** — chức năng vẫn dùng được, chỉ là bố cục và là lỗi đặc tả.

**→ Kết luận: Loại 2 kiểu dọn đặc tả — giữ trường ở nhóm 2 như phần mềm đang làm, **xoá mục 5.2 tại `:1520`**, giữ nguyên ràng buộc "bắt buộc nếu Loại = Tư vấn viên". Riêng ý này Dev action: Không. Nhưng test case còn 2 bug khác đã chứng minh tái hiện (`BUG-DKTGMLTVV_05`, `-05-B`) → **Sheet: Giữ xử lý** theo phần Dev thực tế.**  **✅ BA duyệt 04/08/2026.**

### Phương án xử lý (cập nhật SRS)

**Chỉ có một tệp thẻ hành nghề, không phải hai.** Mô hình dữ liệu đã xác nhận: entity chỉ khai đúng một trường `file_the_hanh_nghe` — `srs-fr-04-chuyen-gia-tvv.md:314` (§Inputs FR-IV-03) và `:390` (§Outputs), baseline `srs-v3.5.md:1745` cũng chỉ trỏ về một trường của `HO_SO_TU_VAN_VIEN`. Nên việc bảng màn hình liệt kê hai lần là **lỗi chép đặc tả**, không phải hai ô tải tệp khác nhau. Đây cũng là căn cứ chọn hướng giữ một chỗ thay vì hiển thị ở cả hai nhóm.

**Sửa đúng ba chỗ trong `srs-fr-04-chuyen-gia-tvv.md`, bảng SCR-IV-02:**

| Dòng | Hiện tại | Sửa thành |
|:-:|---|---|
| `:1508` | `3.6 \| nhóm 2 \| File thẻ hành nghề \| tải file \| PDF, tối đa 10MB; bắt buộc nếu Loại = Tư vấn viên` | **Giữ nguyên** — đây là chỗ ở lại, và là chỗ duy nhất ghi ràng buộc bắt buộc |
| `:1520` | `5.2 \| nhóm 4 \| File thẻ hành nghề \| tải 1 file \| PDF, tối đa 10MB` | **Xoá cả dòng** |
| `:1521` | `5.3 \| nhóm 4 \| Danh sách file đã tải` | Đánh số lại thành **`5.2`** cho liền mạch |

**Không đụng baseline và không đụng entity** — cả hai vốn đã đúng, chỉ bảng màn hình sai. Cũng không phát sinh mã BR/FR mới nên không cần grep ID.

**Kiểm sau khi sửa:** nhóm 4 còn đúng hai mục (Bằng cấp/Chứng chỉ, Danh sách file đã tải); toàn file chỉ còn **một** dòng "File thẻ hành nghề"; ràng buộc *"bắt buộc nếu Loại = Tư vấn viên"* vẫn còn nguyên ở `:1508` — nếu ràng buộc này mất theo thì thành lỗi mới, vì phần mềm đang áp và đã chặn đúng.

> **Ô chốt của BA:** [ ] Giữ ở nhóm 2, xoá `:1520` (khuyến nghị) · [ ] Chuyển xuống nhóm 4 · [ ] Hiển thị ở cả hai nhóm · **Người duyệt / ngày:** ……………

---

## Vấn đề 13 — `QLLSHTCTVV_03`: bảng "Lịch sử hỗ trợ" có bổ sung cột "Trạng thái vụ việc" không

**Vấn đề:** Trong hồ sơ tư vấn viên, bảng "Lịch sử hỗ trợ" liệt kê các vụ việc người đó đã tham gia nhưng không có cột nào cho biết vụ việc đang ở trạng thái gì — dù ngay phía trên vẫn có ô lọc theo trạng thái. Người dùng lọc ra được nhưng không đọc được trạng thái của từng dòng kết quả. Sổ nội bộ tab `tuần 2` dòng **125** (`Verify` = BA confirm).

**(1) Phần mềm đúng SRS chưa? → ĐÚNG đặc tả màn hình.** `srs-fr-04-chuyen-gia-tvv.md:1578` liệt kê đúng 9 cột *"Mã vụ việc + Tên vụ việc + Doanh nghiệp + Lĩnh vực + Vai trò + Ngày phân công + Ngày hoàn thành + Kết quả + Đánh giá"* — không có Trạng thái. `trang_thai` có ở §Outputs `:792` và bộ lọc `:773`, nhưng đó là tầng dữ liệu và tầng lọc.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không, cùng 9 cột.** Mục 4.4.5.2.2 thẻ "Lịch sử hỗ trợ": *"Bảng gồm: mã vụ việc, tên vụ việc, doanh nghiệp, lĩnh vực, vai trò tham gia, ngày phân công, ngày hoàn thành, kết quả và điểm đánh giá"*.

**(2) Đối tác yêu cầu có khác SRS không? → CÓ**, đòi thêm một cột không có ở cả hai bản tài liệu.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → Không.** Có bất tiện thật — lọc theo trạng thái mà không đọc được trạng thái từng dòng — nhưng không hỏng luồng.

**→ Kết luận: Loại 3 — Phần mềm đúng cả hai bản tài liệu; đề nghị đưa việc thêm cột vào danh sách yêu cầu cải tiến. Riêng ý này Dev action: Không. Test case còn 2 bug hiển thị khác → **Sheet: Giữ xử lý**.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Bảng "Lịch sử hỗ trợ" trong hồ sơ tư vấn viên được thiết kế gồm chín cột: mã vụ việc, tên vụ việc, doanh nghiệp, lĩnh vực, vai trò tham gia, ngày phân công, ngày hoàn thành, kết quả và điểm đánh giá. Cột trạng thái vụ việc không nằm trong thiết kế của bảng này ở cả tài liệu bàn giao lẫn bản gốc; ô lọc theo trạng thái vẫn giữ để thu hẹp danh sách.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật lại Kết quả mong đợi. Nếu vẫn cần đọc trạng thái ngay trên bảng, đề nghị đưa vào danh sách yêu cầu cải tiến.

> **Ô chốt của BA:** [ ] Giữ 9 cột, ghi nhận yêu cầu cải tiến (khuyến nghị) · [ ] Bổ sung cột "Trạng thái vụ việc" ngay, cập nhật `:1578` và bản bàn giao · **Người duyệt / ngày:** ……………

---

## Vấn đề 14 — `QLLSHTCTVV_04`: tập giá trị bộ lọc trạng thái và nhãn "Đã hủy"

**Vấn đề:** Ô lọc "Trạng thái vụ việc" ở bảng Lịch sử hỗ trợ chỉ có ba lựa chọn — Đang xử lý, Hoàn thành, Từ chối — trong khi vụ việc thực tế đi qua 12 trạng thái. Đo trên một hồ sơ tư vấn viên có 6 vụ việc:

| Chọn giá trị nào | Số vụ việc lọc ra |
|---|:-:|
| Không lọc | 6 |
| Đang xử lý | 1 |
| Hoàn thành | 1 |
| Từ chối | 0 |

Tức **4 trong 6 vụ việc không lựa chọn nào chạm tới được**. Ngoài ra đặc tả còn ghi một lựa chọn tên "Đã hủy" — trạng thái này không tồn tại trong hệ thống. Sổ nội bộ tab `tuần 2` dòng **126** (`Verify` = BA confirm).

**(1) Phần mềm đúng SRS chưa? → Đúng ở nhãn, sai ở độ phủ.**
- Nhãn: bảng ánh xạ `srs-fr-05-vu-viec.md:1498-1509` có 12 trạng thái, **không có "Đã hủy"**; giá trị gần nhất là `TU_CHOI` → "Từ chối". Web hiển thị "Từ chối" ⇒ **web đúng hơn `.md`**; `srs-fr-04-chuyen-gia-tvv.md:1578` đang chứa một nhãn mồ côi.
- Độ phủ: `:1578` quy định tập rút gọn 4 giá trị, nhưng không định nghĩa mỗi giá trị gom những trạng thái nào. Hệ quả đo được: 4/6 vụ việc (`DA_DUYET`, `DA_DANH_GIA` ×2, `DA_PHAN_CONG`) không giá trị nào lọc ra được.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không quy định.** Mục 4.4.5.2.2 chỉ ghi *"Bộ lọc gồm khoảng ngày và trạng thái vụ việc"*, không liệt kê giá trị.

**(2) Đối tác yêu cầu có khác SRS không? → CÓ.** Đối tác đòi đủ 12 trạng thái; `.md` cố ý quy định tập rút gọn cho riêng tab này.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ, phần độ phủ.** Bộ lọc bỏ sót 2/3 dữ liệu mà chính tab đó đang hiển thị là hỏng công dụng của bộ lọc.

**→ Kết luận: Loại 2 — Giữ tập rút gọn (không mở ra 12 giá trị), nhưng phải bổ sung định nghĩa mỗi nhãn gom những trạng thái nào; đồng thời sửa nhãn "Đã hủy" → "Từ chối". Dev action: Có → Sheet: Giữ xử lý.**  **✅ BA duyệt 04/08/2026.**

### Phương án xử lý (cập nhật SRS)

- Định nghĩa ánh xạ tại `:1578`, phủ đủ **12/12** trạng thái ở `srs-fr-05-vu-viec.md:1498-1509`: **Đang xử lý** = `MOI_TAO` · `CHO_TIEP_NHAN` · `DA_TIEP_NHAN` · `DANG_KIEM_TRA` · `YEU_CAU_BO_SUNG` · `DA_PHAN_CONG` · `DANG_XU_LY` · `CHO_PHE_DUYET` · `DA_DUYET` (9 trạng thái) · **Hoàn thành** = `HOAN_THANH` · `DA_DANH_GIA` · **Từ chối** = `TU_CHOI`. Không còn bản ghi lọt lưới.
- Sửa nguyên văn nhãn thứ ba từ **"Đã hủy"** thành **"Từ chối"** cho khớp bảng ánh xạ `:1509`.
- Bỏ mục **"Tất cả"** khỏi `:1578`: với ô lọc chọn-nhiều, để trống đã có nghĩa là tất cả, và phần mềm đã có nút xoá bộ lọc.
- **Áp cho hai màn:** cụm này được lặp nguyên văn ở `:1856` (tab "Vụ việc đã hỗ trợ" màn Người hỗ trợ pháp lý) — sửa đồng thời.

> **Ô chốt của BA:** [ ] Giữ tập rút gọn + bổ sung ánh xạ nhóm + sửa nhãn thành "Từ chối" (khuyến nghị) · [ ] Mở đủ 12 trạng thái · Mục "Tất cả": [ ] bỏ khỏi đặc tả · [ ] giữ và yêu cầu Dev bổ sung · **Người duyệt / ngày:** ……………

---

## Vấn đề 15 — `DKTGMLTVV_OOS_02`: nhãn "Số CMND/CCCD" hay "Số Căn cước công dân"

**Vấn đề:** Ô nhập giấy tờ tùy thân của tư vấn viên đang gắn nhãn "Số CMND/CCCD", trong khi đặc tả ghi "Số Căn cước công dân". Khác nhau không chỉ ở chữ mà ở **loại giấy tờ được chấp nhận**: một bên nhận cả chứng minh nhân dân cũ, một bên chỉ nhận căn cước.

**(1) Phần mềm đúng SRS chưa? → SAI.** `srs-fr-04-chuyen-gia-tvv.md:1495` — *"Số Căn cước công dân \* | ô văn bản | Tối đa 12 ký tự, duy nhất toàn hệ thống"*. Độ dài 12 ký tự cũng là độ dài số căn cước, không phải số chứng minh nhân dân 9 số.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không, bản bàn giao đứng về phía SRS.** Bản v3.5 dùng nhất quán *"Số căn cước công dân"* ở cả ô tìm kiếm lẫn ô nhập (mục 4.4.1.2.2).

**(2) Đối tác yêu cầu có khác SRS không? → Không nêu** — điểm do đội thẩm định phát hiện.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Theo **Luật Căn cước 2023**, chứng minh nhân dân chỉ có giá trị sử dụng đến hết **31/12/2024**; từ 01/01/2025 không còn là giấy tờ hợp lệ để nhập mới. Giữ nhãn "CMND/CCCD" là mời người dùng nhập một loại giấy tờ đã hết hiệu lực.

**→ Kết luận: Loại 1 — Lỗi phần mềm, đổi nhãn về "Số Căn cước công dân" theo đặc tả. Dev action: Có → Sheet: chưa có dòng trên sổ KTĐL để cập nhật (xem dưới).**

> **Không có dòng nào trên sổ KTĐL cho lỗi này.** Đã rà toàn tab: không dòng nào nhắc "CMND" hay nhãn trường. Dòng gần nhất là **`DKTGMLTVV_03` dòng 408** — *"Kiểm tra hiển thị Nhóm 2 Thông tin nghề nghiệp"*, nhưng lỗi đối tác ghi ở đó là *"thiếu trường Chứng chỉ hành nghề, Mô tả kinh nghiệm"*, **không phải nhãn giấy tờ tùy thân**. Vậy điểm này do đội thẩm định tự phát hiện, chưa vào sổ đối tác.
>
> **Chưa kết luận được Dev đã sửa hay chưa.** Sổ nội bộ có ghi chú *"Đã kiểm tra lại — lỗi không còn, chuyển Pass"* (đo 03/08 lúc 21:05, bản dựng V1.0.5), nhưng đó là **lời khai trong ô phản hồi**, không phải kết quả QA đo lại độc lập. Theo quy trình, nhãn `dev done` và ghi chú của Dev không dùng làm bằng chứng. Đề nghị QA đo lại và mở dòng trên sổ KTĐL nếu lỗi còn.

---

# D. Báo cáo thống kê (nhóm FR-IX)

## Vấn đề 16 — Tệp PDF của Báo cáo thống kê thiếu khung văn bản hành chính TT 17/2025

**Vấn đề:** Báo cáo thống kê có phải trình bày như một văn bản hành chính chính thức không — tức có quốc hiệu và tên cơ quan ở đầu trang, ngày ký và chức danh người ký ở cuối trang? Đối tác ghi yêu cầu này vào Kết quả mong đợi của **toàn bộ 22 phiếu "Kiểm tra chức năng Xuất PDF"** (sổ nội bộ tab `tuần 3`: SLHDVM_07 dòng 192 · CGTVPL_07 dòng 231 …), nguyên văn:

> *"Hệ thống tạo tệp PDF theo đúng mẫu biểu Thông tư số 17/2025/TT-BTP — khổ A4, phông chữ Times New Roman cỡ 13, **đầu trang có quốc hiệu và tên cơ quan, cuối trang có ngày ký và chức danh người ký**."*

Đối chiếu tệp thật:

| Thành phần của khung văn bản hành chính | Tệp hiện có |
|---|---|
| Khổ A4, phông Times New Roman cỡ 13 | Có |
| Tên báo cáo, kỳ báo cáo, đơn vị, ngày tạo | Có |
| Quốc hiệu, tên cơ quan ban hành | **Không** |
| Ngày ký, chức danh người ký | **Không** |

> **Hiện trạng trên sổ nội bộ tab `tuần 3`:** cả 22 phiếu đã qua vòng verify đầu — `Verify` = Pass, lỗi "Forbidden" đối tác báo trước đây đã hết, tệp tải về được và số liệu khớp màn hình. Vòng hai ghi **`Verify 2` = BA confirm cho 21 phiếu**, 1 phiếu `Reopen`. Bảng đối chiếu ở trên là kết quả tổ QA mở tệp thật ngày 03/08 trên bản dựng V1.0.4.
>
> ⚠️ **Sổ bàn giao đang lệch một nhịp:** ở đó cùng nhóm phiếu này vẫn ghi lỗi cũ *"Không thể tạo file xuất"*, chưa cập nhật kết quả vòng sau.
**(1) Phần mềm đúng SRS chưa? → THIẾU.** Tệp PDF hiện có khổ A4, phông Times New Roman cỡ 13 và bốn mục đầu tệp, nhưng **không có quốc hiệu, tên cơ quan ban hành, ngày ký và chức danh người ký**. Đặc tả nhóm IX chỉ mô tả phần đầu tệp ở mức tối thiểu — `srs-fr-11-bao-cao.md:1092`: *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"* — trong khi `srs-fr-11-bao-cao.md:86` · `:124` · `:1052-1053` đều buộc xuất *"theo Thông tư 17/2025"*, và khung của Thông tư được khai tại `srs-v3.5.md:6669-6673`: *"Header: Quốc hiệu + Tên cơ quan ban hành"* · *"Footer: Ngày ký + Chức danh người ký + Con dấu (nếu in chính thức)"*.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không mở rộng khung hành chính cho nhóm IX**, nhưng cũng không loại trừ — bản bàn giao chỉ nhắc khổ giấy và phông chữ.

**(2) Đối tác yêu cầu có khác SRS không? → Không.** Kết quả mong đợi của 22 phiếu Xuất PDF ghi đúng khung mà `srs-v3.5.md:6669-6673` định nghĩa. Riêng phiếu "In báo cáo" (`SLHDVM_08`) chỉ đòi khổ giấy và phông — bản in màn hình không phải văn bản phát hành nên không mâu thuẫn.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Báo cáo thống kê nhóm IX được dùng làm tài liệu trình lãnh đạo và gửi kèm khi báo cáo công tác hỗ trợ pháp lý; không có quốc hiệu và khối ký thì tệp không dùng được như một văn bản chính thức, cán bộ phải dựng lại bằng tay.

**→ Kết luận: Loại 1 — Phần mềm thiếu khung văn bản hành chính, Dev bổ sung. Kèm Loại 2: đặc tả nhóm IX mô tả phần đầu tệp chưa đủ, phải bổ sung cho khớp. Dev action: Có → Sheet: 22 phiếu Xuất PDF giữ nguyên trạng thái đang xử lý, không chuyển Pass.**  **✅ BA duyệt 04/08/2026 — chốt theo yêu cầu của đối tác.**

### Phương án xử lý

**Phần Dev — bổ sung vào bản dựng PDF của nhóm IX:**

| Vị trí trên tệp | Nội dung |
|---|---|
| Đầu trang | Quốc hiệu, tiêu ngữ · Tên cơ quan ban hành |
| Thân | Giữ nguyên bốn mục đang có: tên báo cáo · kỳ báo cáo · đơn vị · ngày tạo |
| Cuối trang | Ngày ký · **Họ tên người xuất báo cáo** · chừa chỗ con dấu khi in chính thức |

Giữ nguyên khổ A4 và Times New Roman cỡ 13 — hai phần này đã đạt.

**Phần đặc tả — sửa hai chỗ:**
- `srs-fr-11-bao-cao.md:1092`: bổ sung quốc hiệu, tên cơ quan ban hành và khối ký vào mô tả, thay vì chỉ bốn mục như hiện nay.
- `srs-fr-11-bao-cao.md:86` (bước xuất PDF) và `:124` (tiêu chí chấp nhận): hiện chỉ nêu khổ A4 và phông chữ — bổ sung đủ bốn thành phần khung, và ghi rõ khối ký gồm ngày ký + họ tên, không có chức danh.
- `srs-v3.5.md` bảng **D.2.3** (Export format): hiện chỉ liệt kê **Excel (.xlsx)** và **Word (.docx)** — bổ sung dòng **PDF**.
- Ba chỗ khác ở baseline còn mô tả nhóm IX xuất Word, phải đồng bộ sang PDF: `srs-v3.5.md:4912` (traceability FR-IX-01, ghi *"export Excel/Word"*) · `:5524` (BR-DATA-06, ghi *"Báo cáo nhóm IX có xuất Word"*) · `:4630` (PRT-03, danh mục định dạng chuẩn mở).
- `srs-v3.5.md:6673` — khung chung vẫn ghi *"Footer: Ngày ký + Chức danh người ký + Con dấu"*. **Không sửa khung chung** (nó còn phục vụ Mẫu 21a/21b nhóm XI), chỉ thêm một câu trỏ ngoại lệ của nhóm IX để lần sau không ai báo thiếu.

> **Phản hồi gửi đối tác:**
> **[Lý do]** Tệp báo cáo sẽ được bổ sung quốc hiệu và tên cơ quan ở đầu trang, ngày ký và họ tên cán bộ xuất báo cáo ở cuối trang, kèm chỗ trống cho con dấu khi in chính thức — đúng như Quý đơn vị nêu. Riêng dòng chức danh người ký thì phần mềm chưa in được: hồ sơ tài khoản người dùng hiện không lưu thông tin chức vụ, nên không có nguồn dữ liệu để điền. Người ký có thể ghi tay chức danh khi ký.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật lại Kết quả mong đợi cho phần chức danh. Nếu cần in sẵn chức danh, đề nghị đưa vào danh sách yêu cầu cải tiến, vì việc này phải bổ sung thông tin chức vụ vào hồ sơ tài khoản của toàn hệ thống.

**Khối ký in ngày ký và họ tên người xuất báo cáo, bỏ dòng chức danh** — BA chốt 04/08/2026. Người đó ký tay lên trên sau khi in; không ký số (Vấn đề 18).

**Vì sao bỏ chức danh:** hồ sơ tài khoản không lưu thông tin này. Entity `TAI_KHOAN` (`srs-v3.5.md:2057`) có đúng 14 trường — username · email · mật khẩu · họ tên · điện thoại · loại tài khoản · trạng thái · bộ đếm đăng nhập sai · lần đăng nhập cuối · định danh VNeID · số căn cước · khoá OTP · token đặt lại mật khẩu · hạn token — **không có trường chức vụ**. Trong toàn mô hình dữ liệu, `chuc_vu` chỉ có ở `TU_VAN_VIEN` (`:1732`) và `HOC_VIEN` (`:3511`), đều không phải cán bộ xuất báo cáo. In chức danh sẽ phải bổ sung trường vào hồ sơ tài khoản, sửa màn quản trị tài khoản và làm sạch dữ liệu cũ — chạm phạm vi ngoài nhóm IX, không tương xứng với một dòng trên khối ký.

**Ghi rõ ngoại lệ trong đặc tả, đừng bỏ lặng.** Khung chung tại `srs-v3.5.md:6673` ghi *"Footer: Ngày ký + Chức danh người ký + Con dấu"*. Nhóm IX bỏ phần chức danh, nên `srs-fr-11-bao-cao.md:1092` phải nói thẳng: khối ký gồm ngày ký và họ tên người xuất báo cáo, **không có dòng chức danh vì hồ sơ tài khoản không lưu**. Không ghi thì vòng kiểm thử sau lại báo thiếu so với khung chung.


## Vấn đề 17 — Quy ước đặt tên tệp xuất của nhóm IX

**Vấn đề:** Tệp tải về từ Báo cáo thống kê nên đặt tên theo khuôn nào? Cùng ô Kết quả mong đợi của 22 phiếu Xuất PDF, đối tác ghi thêm: *"Đặt tên tệp theo định dạng **BaoCaoHoiDap_{YYYYMMDD_HHmm}.pdf**"*. Đặc tả không quy định tên tệp cho nhóm báo cáo này, còn các nhóm khác thì mỗi nơi một kiểu:

| Nơi dùng | Khuôn tên tệp |
|---|---|
| Hỏi đáp · Chương trình hỗ trợ pháp lý | `TenBaoCao_{ngày_giờphút}` |
| Tư vấn chuyên sâu | `TVCS-danh-sach-{YYYYMMDD-HHmm}.xlsx` — chữ thường, gạch nối |
| Báo cáo thống kê (đang chạy) | `bao-cao-<tên>-{ngày}` — **không có giờ phút** |

Không có giờ phút thì xuất hai lần trong ngày sẽ đè lên nhau. Khuôn đối tác nêu trùng khuôn ở dòng đầu bảng.

> **Phạm vi hẹp hơn phiếu QA nêu:** yêu cầu tên tệp **chỉ nằm ở phiếu Xuất PDF**. Kết quả mong đợi của các phiếu "Kiểm tra chức năng Xuất excel" chỉ ghi *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng"* — không có chữ nào về tên tệp. Trên sổ nội bộ, 26 phiếu Xuất Excel của tuần 3 đã đóng (22 `Verify 2` = Pass, 4 `Verify` = Pass). Khoanh phạm vi chỉ `.pdf` nên **không phiếu Excel nào phải mở lại** — đó cũng là lý do chọn phạm vi hẹp thay vì áp chung cho mọi định dạng.

**(1) Phần mềm đúng SRS chưa? → SRS không quy định cho nhóm IX**, nên không chấm sai được. Nhưng hệ thống **đã có khuôn chung**: `srs-fr-02-hoi-dap.md:151` — *"Tên file: `HoiDap_{YYYYMMDD_HHmm}.xlsx`"*, và `srs-fr-15-ct-htpldn.md:397` dùng lại kèm viện dẫn *"theo khuôn đã dùng ở `srs-fr-02-hoi-dap.md:151`; phần giờ phút là bắt buộc để xuất 2 lần trong ngày không đè tệp"*. Chỗ lệch khuôn là `srs-fr-12-tv-chuyen-sau.md:162` — *"Tạo file .xlsx tên `TVCS-danh-sach-{YYYYMMDD-HHmm}.xlsx` (có giờ-phút)"*.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không quy định tên tệp cho nhóm IX.**

**(2) Đối tác yêu cầu có khác SRS không? → Đối tác đòi một quy ước SRS chưa có**, nhưng khuôn họ nêu trùng khuôn nội bộ đã dùng ở 2 module.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → Có ở mức tối thiểu:** phần giờ-phút cần thiết để xuất hai lần trong ngày không đè tệp — lý do này đã được ghi ngay trong `srs-fr-15:397`.

**→ Kết luận: Loại 2 — SRS thiếu quy ước chung, đã chốt, Dev áp.  **✅ BA duyệt 04/08/2026.** Chuẩn hoá theo khuôn đã có: `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`, áp cho **mọi định dạng xuất** của nhóm IX. Dev action: Có → Sheet: 22 phiếu Xuất PDF theo Vấn đề 16.**

> **26 phiếu Xuất Excel đã đóng — không mở lại.** Kết quả mong đợi của nhóm đó không nhắc tên tệp nên phần mềm không sai gì tại thời điểm kiểm thử; chúng Pass đúng theo đặc tả lúc đó. Việc áp khuôn mới cho `.xlsx` là **thay đổi đặc tả**, xử lý thành hạng mục Dev riêng và QA kiểm ở vòng sau — không quy ngược thành lỗi của lượt đã qua.

### Phương án xử lý (cập nhật SRS)

**Bổ sung quy ước tên tệp vào `srs-fr-11-bao-cao.md:85` và `:86`** — bước 7 (xuất Excel) và bước 8 (xuất PDF) của Processing chung nhóm IX. Dòng hiện tại: *"Nếu xuất PDF: tạo file .pdf giữ nguyên định dạng trình bày theo Thông tư 17/2025 (khổ A4, font Times New Roman cỡ 13)"*. Sửa thành: **giữ nguyên** cụm *"theo Thông tư 17/2025"* (Vấn đề 16 đã chốt áp khung này), và **thêm câu đặt tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`, trong đó phần giờ-phút là bắt buộc để xuất hai lần trong ngày không đè tệp**.

Khuôn này không phải tự đặt — nó đã dùng ở hai module và có dòng viện dẫn lẫn nhau: `srs-fr-02-hoi-dap.md:151` (*"Tên file: `HoiDap_{YYYYMMDD_HHmm}.xlsx`"*) và `srs-fr-15-ct-htpldn.md:397` (*"theo khuôn đã dùng ở `srs-fr-02-hoi-dap.md:151`; phần giờ phút là bắt buộc để xuất 2 lần trong ngày không đè tệp"*).

**Áp cho mọi định dạng xuất của nhóm IX** — BA chốt 04/08/2026. Sửa cả bước 7 (`:85`, xuất Excel) theo cùng khuôn: `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`. Lý do chọn phạm vi rộng: cùng một màn báo cáo mà hai nút xuất ra hai kiểu tên tệp thì người dùng khó xếp tệp, và quy ước nửa vời sẽ lại lệch ở lần bổ sung định dạng sau.

Sửa kèm hai chỗ nữa của cùng nhóm IX, nếu không thì quy ước có mà không có cửa nghiệm thu: `srs-fr-11-bao-cao.md:1092` (quy tắc tương tác Export XLSX/PDF) và `:124` (tiêu chí chấp nhận — bổ sung kiểm tên tệp).

**Không đụng baseline**, không phát sinh mã BR/FR mới. Chỗ lệch khuôn ở `srs-fr-12-tv-chuyen-sau.md:162` thuộc nhóm XII, ngoài phạm vi phiếu này — ghi nhận để dọn ở đợt đồng bộ quy ước sau.



---

## Vấn đề 18 — Báo cáo nhóm IX có cần ký số điện tử không

**Vấn đề:** Câu cuối cùng trong Kết quả mong đợi của 22 phiếu Xuất PDF ghi: *"Tệp hỗ trợ ký số điện tử **khi có yêu cầu**"* — tức phần mềm phải gắn được chữ ký điện tử của cơ quan vào tệp trước khi trả về máy người dùng.

**(1) Phần mềm đúng SRS chưa? → ĐÚNG.** Ký số chỉ được đặc tả cho một chức năng duy nhất: `srs-fr-03-dao-tao.md:1437` — *"FR-III-20: Xuất file docx/PDF **ký số** cho CTDT"*. Toàn nhóm IX không có yêu cầu nào.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không nêu ký số cho nhóm IX.**

**(2) Đối tác yêu cầu có khác SRS không? → CÓ**, đòi thêm ngoài đặc tả — nhưng chính họ viết kèm điều kiện *"khi có yêu cầu"*, tức không đòi ký số mặc định cho mọi lần xuất.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → KHÔNG.** Danh sách UC/Transaction — trọng tài về phạm vi chức năng — có **34 UC thuộc nhóm báo cáo và thống kê, không UC nào yêu cầu ký số**. Vấn đề 16 chốt tệp có khối ngày ký và chức danh, nhưng đó là **chỗ để ký tay sau khi in**, không kéo theo nghĩa vụ ký số điện tử.

**→ Kết luận: Loại 3 — Không áp ký số cho nhóm IX. Tệp PDF chừa khối ngày ký và chức danh để ký tay sau khi in; phần mềm không gắn chữ ký điện tử. Dev action: Không → Sheet: theo Vấn đề 16.**  **✅ BA duyệt 04/08/2026.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Danh sách chức năng đã thống nhất không có yêu cầu ký số điện tử cho nhóm báo cáo thống kê; trong toàn bộ tài liệu, ký số chỉ đặt ra cho một chức năng duy nhất là xuất hồ sơ chương trình đào tạo. Tệp báo cáo sẽ có sẵn khối ngày ký và chức danh người ký ở cuối trang để ký tay sau khi in.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật lại Kết quả mong đợi cho khớp. Nếu sau này vẫn cần ký số, đề nghị đưa vào danh sách yêu cầu cải tiến.



---

# E. Tổ chức tư vấn — ba mục tuần 3

Ba mục dưới đây do tổ kiểm thử tự phát hiện khi verify màn Tổ chức tư vấn (sổ nội bộ tab `tuần 3`, dòng 331 · 332 · 339, đều `Verify` = BA confirm). **Đã tra nội dung toàn bộ sổ KTĐL — không dòng nào của đối tác nêu ba điểm này**, kể cả dưới mã khác; các phiếu `QLDMTCTV_*` của đối tác báo lỗi khác (thiếu ô chọn và số thứ tự, thẻ không hiện số đếm, thiếu Số quyết định công bố). Nên ba mục này không có trạng thái đối tác để cập nhật.

## Vấn đề 19 — Bảng danh sách Tổ chức tư vấn có thêm một cột không nằm trong thiết kế

**Vấn đề:** Bảng danh sách Tổ chức tư vấn đang có **11 cột**, thừa cột "Đơn vị quản lý" đặt giữa "Lĩnh vực" và "Người đại diện". Không thiếu thông tin gì, nhưng bảng rộng thêm nên phải cuộn ngang mới thấy ba cột cuối là Trạng thái, Công khai và Hành động.

**(1) Phần mềm đúng SRS chưa? → SAI.** `srs-fr-04-chuyen-gia-tvv.md:1637-1646` liệt kê bảng đúng **10 thành phần**: Ô chọn · Số thứ tự · Mã tổ chức · Tên tổ chức · Loại hình · Người đại diện · Lĩnh vực · Trạng thái · Công khai · Hành động. "Đơn vị quản lý" có xuất hiện ở màn này nhưng ở dòng `:1634` — **là bộ lọc, không phải cột bảng**.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không đụng tới.** Mục 4.4.15.2.2 mô tả các trường thông tin của tổ chức, không liệt kê danh sách cột của bảng danh sách nên không bênh mà cũng không bác.

**(2) Đối tác yêu cầu có khác SRS không? → Không nêu.** Phiếu `QLDMTCTV_02` (sổ KTĐL dòng 961) kiểm đúng bảng này nhưng báo lỗi khác: *"Thiếu ô chọn và trường STT"*.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → Không, nhưng có hại thấy được.** Cột thừa đẩy ba cột cuối ra ngoài khung nhìn, trong đó có "Hành động" — chỗ người dùng thao tác nhiều nhất.

**→ Kết luận: Loại 1 — Phần mềm thừa một cột so với đặc tả, Dev gỡ để bảng về đúng 10 cột. Nhu cầu xem đơn vị quản lý đã có bộ lọc riêng ở `:1634` phục vụ. Dev action: Có → Sheet: chưa có dòng trên sổ KTĐL để cập nhật.**  **✅ BA duyệt 04/08/2026.**

> **Ô chốt của BA:** [ ] Gỡ cột, giữ 10 cột theo đặc tả (khuyến nghị) · [ ] Giữ cột và bổ sung vào `:1637-1646` — khi đó phải xử lý luôn việc bảng phải cuộn ngang · **Người duyệt / ngày:** ……………

---

## Vấn đề 20 — Số thẻ trạng thái: đặc tả nói 6 chỗ này, 3 chỗ kia

**Vấn đề:** Màn danh sách Tổ chức tư vấn có bao nhiêu thẻ lọc theo trạng thái? Đặc tả nói **6** ở phần màn hình nhưng nói **3** ở phần tiêu chí chấp nhận của chính chức năng đó. Phần mềm đang làm 6.

**(1) Phần mềm đúng SRS chưa? → SRS tự mâu thuẫn, nhưng nghiêng hẳn về phía 6.**
- `srs-fr-04-chuyen-gia-tvv.md:1610` — *"Loại màn hình: **Danh sách 6 tab** + thao tác hàng loạt…"*
- `:1625-1630` — liệt kê rời từng thẻ, mỗi thẻ một dòng kèm hành vi: Đang hoạt động · Tạm dừng · Mới đăng ký · Chờ phê duyệt · Đã từ chối · Vô hiệu hóa.
- Nhưng `:1129` (Tiêu chí chấp nhận của FR-IV-NEW-01) — *"…danh sách TC TV thuộc đơn vị, **3 tab trạng thái**"*.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Bản bàn giao chốt 6.** Mục 4.4.15.2.2: *"Trạng thái | Nhãn | … Gồm: **Mới đăng ký, Chờ phê duyệt, Đã từ chối, Đang hoạt động, Tạm dừng, Vô hiệu hóa**"* — đúng 6 giá trị, trùng khít danh sách thẻ ở `:1625-1630`. Mục 4.4.16 còn nhắc *"thẻ 'Chờ phê duyệt' trên màn hình danh sách"*.

**(2) Đối tác yêu cầu có khác SRS không? → Không nêu.** `QLDMTCTV_05` (dòng 964) kiểm thẻ trạng thái nhưng báo lỗi khác: thẻ không hiện số đếm, thẻ "Mới đăng ký" thiếu chấm đỏ, thẻ "Chờ phê duyệt" hiện cả với cán bộ nghiệp vụ.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Quy trình công bố tổ chức đi qua Mới đăng ký → Chờ phê duyệt → Đã từ chối hoặc Đang hoạt động. Ba thẻ không đủ chỗ cho vòng đời đó, cán bộ phê duyệt sẽ không có thẻ để mở danh sách chờ duyệt.

**→ Kết luận: Loại 2 kiểu dọn đặc tả — phần mềm đang ĐÚNG với 6 thẻ. Dòng `:1129` là chỗ sai. Dev action: Không → Sheet: chưa có dòng trên sổ KTĐL để cập nhật.**  **✅ BA duyệt 04/08/2026.**

### Phương án xử lý (cập nhật SRS)

Sửa `srs-fr-04-chuyen-gia-tvv.md:1129`: đổi *"3 tab trạng thái"* thành *"6 thẻ trạng thái"*, liệt kê đúng sáu giá trị như `:1625-1630`.

Cụm "3 tab" là tàn dư của bản cũ và **còn ở một chỗ nữa phải sửa cùng lượt**: `srs-fr-04-chuyen-gia-tvv.md:212` — tiêu chí chấp nhận của màn Quản lý tư vấn viên, cũng ghi *"3 tab trạng thái"* trong khi bảng thành phần của màn đó liệt kê nhiều hơn. Không sửa thì tranh chấp này lặp lại nguyên vẹn ở nhóm phiếu `QLTVV_*`.

> **Ô chốt của BA:** [ ] Sửa `:1129` thành 6 thẻ (khuyến nghị) · [ ] Rút xuống 3 thẻ và sửa cả phần màn hình lẫn bản bàn giao · **Người duyệt / ngày:** ……………

---

## Vấn đề 21 — Giấy tờ hành nghề của tổ chức: ba tên gọi, hai mức bắt buộc trái ngược

**Vấn đề:** Giấy tờ mà tổ chức tư vấn phải có để được hành nghề đang được đặc tả gọi bằng **hai tên khác nhau** và ghi **hai mức bắt buộc trái ngược** — chỗ thì bắt buộc nhập, chỗ thì không.

| Chỗ trong đặc tả | Gọi là | Bắt buộc |
|---|---|:-:|
| `srs-fr-04:1681-1682` (biểu mẫu thêm/sửa) | Giấy đăng ký **hành nghề** | Có |
| `srs-fr-04:1073` · `:1130` · `:1200` · `:1719` (xử lý, tiêu chí) | Giấy đăng ký **hoạt động** Sở Tư pháp | Có |
| `srs-fr-04:2216-2217` (thực thể) | Giấy ĐKHĐ | **Y — bắt buộc** |
| `srs-fr-04:1052` (§Inputs của FR-IV-NEW-01) | `so_giay_dkhd` | **N — không bắt buộc** |

**(1) Phần mềm đúng SRS chưa? → Không chấm được, vì đặc tả tự mâu thuẫn** ở cả tên gọi lẫn tính bắt buộc.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Bản bàn giao chốt cả hai điểm.** Mục **4.4.15.2.2**: *"**Số giấy đăng ký hoạt động** | Văn bản | **Có** | — | Số giấy đăng ký hoạt động do Sở Tư pháp cấp. Đây là điều kiện hành nghề bắt buộc của tổ chức tư vấn pháp luật"* và *"Ngày cấp giấy đăng ký hoạt động | Ngày | **Có**"*. Mục **4.4.15.1** dẫn thẳng căn cứ: *"Tổ chức tư vấn phải có giấy đăng ký hoạt động do Sở Tư pháp cấp theo Nghị định số 77/2008/NĐ-CP … Điều 13"*.

**(2) Đối tác yêu cầu có khác SRS không? → Không nêu.** Tra nội dung toàn sổ KTĐL: không dòng nào nhắc giấy đăng ký hoạt động hay đăng ký hành nghề.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Đây là điều kiện hành nghề theo luật; thiếu thì tổ chức không đủ tư cách vào mạng lưới. Đặc tả để "không bắt buộc" ở một chỗ là mở đường cho hồ sơ thiếu điều kiện lọt vào.

**→ Kết luận: Loại 2 — SRS mâu thuẫn nội tại, chốt một tên gọi và một mức bắt buộc. Dev action: Có nếu phần mềm đang cho lưu hồ sơ trống giấy này — cần QA đo lại. Sheet: chưa có dòng trên sổ KTĐL để cập nhật.**  **✅ BA duyệt 04/08/2026.**

### Phương án xử lý (cập nhật SRS)

**Tên gọi chuẩn: "Giấy đăng ký hoạt động".** Căn cứ pháp luật: NĐ 77/2008/NĐ-CP **Điều 13** quy định Trung tâm tư vấn pháp luật **đăng ký hoạt động** tại Sở Tư pháp và được Sở cấp **Giấy đăng ký hoạt động** — không có khái niệm "giấy đăng ký hành nghề" cho tổ chức (thẻ hành nghề là giấy tờ của **cá nhân** tư vấn viên, theo Điều 19 cùng nghị định). Tên trường trong mô hình dữ liệu `so_giay_dkhd` và bản bàn giao đều dùng "hoạt động".

**Bắt buộc: Có.** Theo thực thể `:2216-2217`, bản bàn giao mục 4.4.15.2.2, và chính bước xử lý `:1073` — *"Kiểm tra điều kiện hành nghề: TC TV phải có Giấy đăng ký hoạt động Sở TP"*.

**Sửa tên gọi ở hai chỗ:**
- `srs-fr-04-chuyen-gia-tvv.md:1681-1682`: đổi *"Số/Ngày cấp Giấy đăng ký hành nghề"* → *"Số/Ngày cấp **Giấy đăng ký hoạt động**"*, sửa luôn câu báo lỗi kèm theo.
- `srs-fr-04-chuyen-gia-tvv.md:1739`: quy tắc tương tác còn gọi *"Giấy đăng ký hành nghề Sở Tư pháp"*.

**Sửa mức bắt buộc ở bốn chỗ** — hiện file FR và baseline đang chọi nhau sẵn, thực thể ở `:2216-2217` ghi **Y** còn ba chỗ dưới ghi **N**:
- `srs-fr-04-chuyen-gia-tvv.md:1052` (`so_giay_dkhd`) và `:1053` (`ngay_cap_dkhd`) — §Inputs FR-IV-NEW-01.
- baseline `srs-v3.5.md:1818` · `:1819` — bản sao thực thể `TO_CHUC_TU_VAN`, cũng đang **N**.

> ⚠️ **Hệ quả cần BA cân trước khi chốt bắt buộc:** hồ sơ tổ chức đã tạo trước đây có thể đang trống hai trường này. Khi siết thành bắt buộc, mở hồ sơ cũ ra sửa bất kỳ thông tin gì cũng sẽ bị chặn cho tới khi nhập đủ giấy tờ. Cần chốt cách xử lý: chỉ áp bắt buộc với hồ sơ tạo mới, hay buộc bổ sung cho toàn bộ hồ sơ cũ kèm một đợt làm sạch dữ liệu.

> **Ô chốt của BA:** Tên gọi: [ ] "Giấy đăng ký hoạt động" theo NĐ 77/2008 Đ.13 (khuyến nghị) · [ ] Giữ "Giấy đăng ký hành nghề"
> Bắt buộc: [ ] Có, áp cho cả hồ sơ cũ (kèm đợt làm sạch dữ liệu) · [ ] Có, chỉ áp với hồ sơ tạo mới (khuyến nghị) · [ ] Không bắt buộc
> **Người duyệt / ngày:** ……………

---

**Ghi chú sổ sách của tuần 3, không cần BA quyết:** cột "Mô tả" của hai dòng 332 và 339 trên sổ nội bộ còn ghi tiêu đề cũ (nói về *thứ tự* thẻ và *thứ tự* trường) sau khi tổ kiểm thử đã rút hai ý đó ngày 03/08 — câu hỏi còn hiệu lực là **số lượng** thẻ và **tên gọi** giấy tờ, đúng như hai mục trên. Dòng 330 `QLDMTCTV_OOS_04` đã đóng (`Reject`), không còn trong danh sách chưa đóng.

---

**Không còn mục nào chặn Dev.** Nhóm báo cáo (Vấn đề 16–18) đã chốt đủ để Dev dựng lại tệp PDF và đặt tên tệp; nhóm vụ việc (Vấn đề 1–6) đã chốt thang ưu tiên và ngưỡng. Vấn đề 10 rút khỏi diện ưu tiên vì sổ KTĐL cho thấy chức năng đã Pass — chờ đo lại trước.

**Việc không chờ BA, làm ngay:** khôi phục `NHSYC_09` · `NHSYC_10` cho **sổ bàn giao** (lấy từ tab `Bản sao` của chính sổ đó); đo lại chức năng tiếp nhận đề xuất đào tạo trên môi trường bàn giao (Vấn đề 10).

**Đã chốt tính đến 04/08/2026:**
- **Vấn đề 3** — thang ưu tiên theo cách *xếp nhóm*. Còn một điểm chờ: dữ liệu vụ việc cũ có tính lại không.
- **Vấn đề 4** — ngưỡng "nhiều lao động nữ" theo NĐ 80/2021 Đ.3 K.8; định nghĩa "do phụ nữ làm chủ" theo Luật Hỗ trợ DNNVV 2017 Đ.3 K.1.
- **Vấn đề 16** — tệp PDF nhóm IX **áp khung văn bản hành chính TT 17/2025** theo đúng yêu cầu đối tác. Khối ký in ngày ký và **họ tên** người xuất báo cáo; **bỏ dòng chức danh** vì hồ sơ tài khoản không lưu chức vụ — đã ghi ngoại lệ vào đặc tả và có phản hồi gửi đối tác.
- **Vấn đề 17** — quy ước tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`, áp cho mọi định dạng xuất của nhóm IX.
- **Vấn đề 18** — **không áp ký số** cho nhóm IX; chừa khối ký để ký tay sau khi in. Căn cứ: danh sách UC/Transaction có 34 UC nhóm báo cáo, không UC nào yêu cầu ký số.

⇒ Hai mục này đủ để Dev tính lại mức ưu tiên cho cả hai luồng (Vấn đề 5), sau khi BA cập nhật đặc tả theo danh sách vị trí đã nêu ở từng mục. `NHSYC_09` · `NHSYC_10` trên sổ nội bộ vẫn còn và đang `N/R` — chạy được ngay sau khi Dev sửa. Riêng sổ bàn giao đã mất hai dòng này, cần khôi phục để hai bên soi cùng một thước.
