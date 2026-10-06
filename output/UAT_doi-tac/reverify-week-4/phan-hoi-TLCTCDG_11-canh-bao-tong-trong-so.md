# TLCTCDG_11 — Cảnh báo tổng trọng số khi lưu bộ tiêu chí đánh giá

**Ngày phân tích:** 31/07/2026 · **Đợt:** UAT tuần 3 · **Dòng sheet:** 753 (tab `UAT_TGPL Doanh Nghiệp`, `gid=799081340`)
**Trạng thái sheet hiện tại:** `Trạng thái dev fix` = `Reopent` · `DEV phản hồi lần 1` đã có · `Trạng thái dev fix 2` = `InProcess` · `DEV phản hồi lần 2` trống — đây là **vòng phản hồi thứ hai**.

**Bối cảnh nghiệp vụ:** Cán bộ nghiệp vụ dựng bộ tiêu chí chấm điểm cho một đợt đánh giá hiệu quả hỗ trợ pháp lý (Tab Tiêu chí, đợt đang ở trạng thái "Lập kế hoạch"). Tổng trọng số các tiêu chí phải đủ 100% thì đợt mới đi tiếp được sang phân công người đánh giá. Trong lúc dựng dở, hệ thống vẫn cho lưu nhưng phải cảnh báo còn thiếu bao nhiêu.

**Phiếu này thay cho mục `TLCTCDG_11` trong `phan-hoi-27-bug-tranh-chap-srs.md` (30/07)** — nhãn loại giữ nguyên, nhưng mô tả hiện trạng ở phiếu cũ *"Hệ thống chỉ hiện thông báo thành công, không hiện cảnh báo"* **không đúng với ảnh minh chứng**, và phiếu cũ bỏ sót xung đột với BR-CALC-08 chốt cùng ngày.

---

## Bằng chứng đã gom

| Nguồn | Nội dung |
|---|---|
| Kết quả mong đợi (đối tác) | *"Hệ thống hiển thị thông điệp «Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100% trước khi trình phê duyệt»"* |
| Kết quả thực tế (đối tác) | *"Hệ thống hiển thị thông báo thành công"* |
| Ảnh `TLCTCDG_11.jpg` (đã mở xem) | Kế hoạch `DG-20260711-0001`, Tab Tiêu chí, 1 tiêu chí trọng số 50 / điểm tối đa 1. Thông báo nổi: **"Đã lưu tiêu chí đánh giá"**. Trên bảng: **"Tổng trọng số: 50% (Tổng trọng số phải bằng 100%)"** — chữ đỏ |
| Bản `.docx` đối tác cầm | `HTPLDN-PTYC-CT-v2.0.docx` · bàn giao 10/07/2026 · Zalo (4 bản v2.0 trong kho có cùng mã băm — không có dị bản) |
| Bản `.md` | `_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md` (FR-VI-02 / UC84, SCR-VI-01 Tab 1) |

**Đính chính hiện trạng:** phần mềm **có** cảnh báo trọng số — nhãn tổng đỏ kèm chú thích *"(Tổng trọng số phải bằng 100%)"*. Cái thiếu là **thông điệp đúng nội dung quy định**, nêu rõ tổng hiện tại và mốc phải đạt. Dev đừng hiểu thành "chưa có gì" mà dựng lại từ đầu.

---

## Vấn đề

Lưu bộ tiêu chí khi tổng trọng số chưa đủ 100%: hệ thống báo "Đã lưu tiêu chí đánh giá" như trường hợp bình thường, không đưa ra thông điệp cảnh báo nêu tổng hiện tại theo quy định.

**(1) Phần mềm đúng `.md` chưa? — SAI.**
- `srs-fr-08-danh-gia.md:202`: *"Kiểm tra tổng trọng số = 100% cho toàn đợt (cảnh báo nếu khác, cho phép lưu)"*
- `srs-fr-08-danh-gia.md:862` (SCR-VI-01 Tab 1, thành phần 31): *"Cảnh báo trọng số | Alert banner | «Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100%» | — | Khi SUM != 100%"* — nguyên văn tại thời điểm phân tích; mã cảnh báo và đuôi câu đã đổi ở đợt sửa 31/07
- Thành phần 30 (`:851`, nhãn tổng xanh/đỏ) phần mềm đã làm đúng. **Thành phần 31 chưa có.**

**(1b) Bản `.docx` đối tác cầm nói gì? — Cùng chiều, không tranh chấp.**
- Mục **4.8.2.2.3** STT 6 "Lưu": *"+ Trường hợp 2 (thành công, tổng trọng số khác 100%): Hệ thống hiển thị thông điệp «Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100% trước khi trình phê duyệt»"*
- Mục **4.8.2.2.2** mô tả nhãn tổng xanh/đỏ và cảnh báo *"Tổng trọng số phải bằng 100%"* cạnh trường Trọng số — phần này phần mềm đã làm đúng.

**(2) Đối tác yêu cầu có khác đặc tả không? — Không.** Cả hai bản đều buộc phải có thông điệp nêu tổng hiện tại. Đối tác **không** đòi chặn lưu; phản biện của họ ở cột "TKM phản hồi lần 1" nói đúng điểm đó.

**(3) Có bắt buộc cho luồng nghiệp vụ không? — Có.** Nhãn tổng đỏ chỉ nói "phải bằng 100%", không nói **đang thiếu bao nhiêu** và **chặn ở bước nào**. Cán bộ lưu xong tưởng đã xong, sang Tab Phân công mới thấy nút thêm người đánh giá bị khoá (`:863`) mà không hiểu lý do.

> Trả lời của đội phát triển ở vòng 1 đúng về quy tắc (cho lưu, chỉ chặn ở bước sau) nhưng **lệch trọng tâm** — điều đơn vị kiểm thử ghi nhận là *thông điệp không đúng nội dung quy định*, không phải chuyện có chặn lưu hay không.

**→ Kết luận: Loại 1 — phần mềm sai đặc tả. Dev bổ sung thông điệp cảnh báo nêu tổng trọng số hiện tại khi tổng khác 100%, giữ nguyên việc cho phép lưu. Dev action: Có → Sheet: Giữ xử lý (`InProcess` hiện tại là đúng, không đổi, không điền "DEV phản hồi lần 2").**  **✅ BA duyệt 31/07/2026.**

---

## Việc của Dev

Bổ sung thành phần 31 của Tab Tiêu chí: dải cảnh báo hiển thị khi tổng trọng số khác 100%, nội dung nêu **tổng hiện tại** và mốc **100%** cần đạt trước khi trình phê duyệt. Giữ nguyên nhãn tổng xanh/đỏ và việc cho phép lưu.

Đặc tả `.md` quy định đây là **dải cảnh báo thường trực trên màn hình** (hiện suốt khi tổng khác 100%), còn `.docx` mô tả là thông điệp trả về sau khi bấm Lưu. Lấy theo `.md` — dải thường trực bao trùm cả tình huống của `.docx` và hữu ích hơn. Kết quả mong đợi của đối tác chỉ ghi *"hiển thị thông điệp"*, không ràng buộc hình thức, nên làm theo `.md` là đạt.

---

## Phương án xử lý (cập nhật SRS) — BR-CALC-08 kiểm tại cổng, không chặn lưu ✅ BA duyệt 31/07/2026

**Chốt:** Tab Tiêu chí **luôn cho lưu**, tổng trọng số và chuẩn thang điểm chỉ cảnh báo. BR-CALC-08 được kiểm ở **cùng cổng với BR-CALC-04 hiện có**: khi thêm/lưu người đánh giá và khi trình phê duyệt phân công.

**Căn cứ:** với điểm tối đa để mặc định 100, tích (100 × trọng số ÷ 100) cộng lại chỉ bằng 100 khi tổng trọng số đúng 100%. Giữ "chặn lưu" thì mọi cấu hình dở dang đều bị chặn — cán bộ không lưu được khi mới nhập vài tiêu chí, và dải cảnh báo vừa yêu cầu bổ sung không bao giờ hiện ra. Chính dữ liệu trong ảnh minh chứng (1 tiêu chí, trọng số 50) cũng không lưu được. Chuyển về cổng không làm mất hiệu lực BR-CALC-08: cấu hình vi phạm chỉ tồn tại ở dạng nháp, không đi tới được bước chấm điểm nên không sinh ra điểm tổng lệch thang.

**Đã áp vào SRS ngày 31/07/2026** — 17 mục gốc + **7 mục bổ sung sau vòng soi Codex**, ghi ở `CHANGELOG-v3-to-v3.5.md` Phase 13. Bảng dưới là danh sách gốc; số dòng ghi theo bản trước khi sửa.

Vòng soi Codex bắt đúng chỗ đợt sửa gốc bỏ lọt: **máy trạng thái SM-DANHGIA** vẫn cho chuyển `PHAN_CONG → CHO_DUYET_PC` chỉ với điều kiện *"Có danh sách PC"*, tức mở một đường hợp lệ vòng qua chính cổng vừa dựng; và **bảng truy vết** chưa có `BR-CALC-08`. Đã bổ sung điều kiện vào cả hai bước chuyển trạng thái, thêm bước kiểm lại ở FR-VI-04 khi CB PD duyệt, và sửa cột "FR áp dụng" của BR-CALC-08 vốn ghi nhầm FR-VI-06 là "cấu hình tiêu chí".

| # | Vị trí | Sửa thành |
|---|---|---|
| 1 | `srs-v3.5.md:5559` (BR-CALC-08) | Bỏ *"Hệ thống chặn lưu cấu hình tiêu chí vi phạm"* → kiểm tra tại cổng thêm/lưu người đánh giá và trình phê duyệt phân công; tại Tab Tiêu chí chỉ cảnh báo. Giữ nguyên phần mục đích và công thức |
| 2 | `srs-fr-08-danh-gia.md:850` (SCR-VI-01 Tab 1, thành phần 29 — cột Điểm tối đa) | Bỏ *"chặn lưu"*, giữ highlight đỏ + thông báo nêu tổng hiện tại |
| 3 | `srs-fr-08-danh-gia.md:852` (thành phần 31) | Bổ sung đuôi *"trước khi trình phê duyệt"* vào nội dung cảnh báo trọng số (xem Doc action mục 1) |
| 4 | `srs-fr-08-danh-gia.md` — thành phần mới sau `:852` | Dải cảnh báo chuẩn thang điểm, hiện khi tổng (điểm tối đa × trọng số ÷ 100) khác 100, nêu tổng hiện tại |
| 5 | `srs-fr-08-danh-gia.md:191` (Input `diem_toi_da` của FR-VI-02) | Diễn đạt lại: ràng buộc BR-CALC-08 được kiểm tại cổng, không chặn thao tác lưu tiêu chí |
| 6 | `srs-fr-08-danh-gia.md:863`, `:864` (FR-VI-03 — nút Thêm người đánh giá, nút Trình phê duyệt) | Thêm điều kiện BR-CALC-08 bên cạnh điều kiện tổng trọng số 100% đang có |
| 7 | `srs-fr-08-danh-gia.md:302` (FR-VI-03 Error Handling) | Thêm dòng lỗi cho vi phạm BR-CALC-08 tại cổng phân công — mã **`ERR-DG-PC-06`** (đã kiểm `ERR-DG-PC-01`→`05` đang dùng, `06` còn trống) |
| 8 | `srs-fr-08-danh-gia.md:895` (Quy tắc tương tác) | Nêu rõ Tab Tiêu chí cho lưu với cả hai loại cảnh báo; hai ràng buộc cùng chặn ở Tab Phân công |
| 9 | `srs-fr-08-danh-gia.md:1100` (thực thể `TIEU_CHI_DANH_GIA`) | Đồng bộ diễn đạt với mục 5 |
| 10 | `CHANGELOG-v3-to-v3.5.md` + header `srs-fr-08-danh-gia.md` | Ghi quyết định 31/07/2026 — TLCTCDG_11 UAT tuần 3 vòng 2 |

**Việc kèm cho Dev:** không áp ràng buộc thang điểm vào thao tác Lưu ở Tab Tiêu chí; khoá thao tác ở Tab Phân công như đang làm với tổng trọng số.

`TKDGHQHTPL_02` không bị ảnh hưởng — điểm tổng chỉ sinh ra sau khi chấm, mà chấm chỉ mở sau khi qua cổng.

---

## Doc action — bên soạn tài liệu bàn giao

Hai điểm lệch câu chữ giữa `.md` và `.docx` — **cả hai đã xử lý ở phía `.md` ngày 31/07/2026**, `.docx` không phải sửa:

1. **Đuôi câu cảnh báo.** `.docx` 4.8.2.2.3 có *"…Cần đảm bảo = 100% **trước khi trình phê duyệt**"* mà `.md` thiếu. Đuôi này mô tả đúng cổng chặn thật → đã bổ sung vào `.md` thay vì gỡ khỏi `.docx`. Nhờ vậy Kết quả mong đợi của `TLCTCDG_11` khớp nguyên văn, đối tác không phải sửa test case.
2. **Mã cảnh báo dùng trùng.** `WRN-TC-01` từng gắn cho hai nội dung khác nhau ở `srs-fr-08-danh-gia.md` (đợt đánh giá) và `srs-fr-10-quan-tri.md:566` (*"…trước khi sử dụng"*, danh mục tiêu chí dùng chung). Đã tách: `srs-fr-08` dùng **`WRN-DG-TC-01`** (trọng số) và **`WRN-DG-TC-02`** (thang điểm), `WRN-TC-01` để lại cho `srs-fr-10`.

**Còn lại một việc cho bản bàn giao kế tiếp:** `.docx` 4.8.2.2.3 mô tả cảnh báo là thông điệp trả về **sau khi bấm Lưu**, còn `.md` quy định **dải cảnh báo thường trực**. Không đổi kết quả nghiệm thu (Kết quả mong đợi chỉ ghi *"hiển thị thông điệp"*), nhưng nên đồng bộ để lần sau khỏi phải truy ngược.

---

## Cập nhật sheet

**Không ghi gì.** Loại 1, Dev action Có → giữ trạng thái đang xử lý; `Trạng thái dev fix 2` = `InProcess` đã đúng. Không điền `DEV phản hồi lần 2` — phần mềm sẽ được sửa đúng theo yêu cầu của đối tác nên không có gì để giải trình.

Kết quả mong đợi của `TLCTCDG_11` **giữ nguyên**, không đưa vào danh sách test case cần sửa Expected khi bàn giao bản `.docx` mới.
