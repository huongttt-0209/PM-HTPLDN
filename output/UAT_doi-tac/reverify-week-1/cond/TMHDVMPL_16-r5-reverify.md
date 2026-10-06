# Bảng đối chiếu điều kiện — RE-VERIFY TMHDVMPL_16 (row 278) — sau khi dev báo đã sửa

**Kết luận:** Pass. Chốt kiểm **tổng dung lượng 100MB** đã tồn tại và chạy đúng ở đúng điểm giao trần: nạp 6 tệp (**95,6 MB**, dưới trần) → nhận bình thường; nạp tiếp **tệp thứ 7** (đưa tổng lên ~111,5 MB) → hệ thống **từ chối** kèm thông báo *"Tổng dung lượng tệp vượt quá giới hạn 100MB."*, danh sách **giữ nguyên 6 tệp**, chỉ số tổng **giữ nguyên 95,6 MB**. Giao diện nay **có** chỉ số *"Tổng dung lượng {total} / 100MB"* và dòng gợi ý **có** nêu trần tổng. Lưu hồ sơ rồi đọc lại: đúng **6 tệp**, không có tệp thứ 7.

Đo ngày 30/07/2026 23:15–23:25, bản **HTPLDN · V1.0.3**, tài khoản `cbnv_tw_03`.

| Điều kiện có thể đổi kết quả | Bug gốc (BUG-TMHDVMPL_16, Pass-bug-report-tuan-1-vong-dau.md) | Mình test lại (env nip.io, 30/07/2026 23:15–23:25) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — **CB Nghiệp vụ - Trung ương (CB_NV_TW)**, phạm vi **BTP · TW** | `cbnv_tw_03` — **CB Nghiệp vụ - Trung ương #03 (CB_NV_TW)**, phạm vi **BTP · TW**, đơn vị *Bộ Tư Pháp · Cục Bổ trợ tư pháp* | Không |
| Màn hình + thao tác kích hoạt | **Hỏi đáp pháp lý** → **[Thêm mới]** → mục **File đính kèm** (bước 2–5 của phiếu) | Đúng màn, đúng nút **[Thêm mới]**, đúng mục **File đính kèm** | Không |
| Cỡ từng tệp (phải dưới trần 20MB để cô lập đúng phép kiểm tổng) | 10 tệp `.docx`, **15,9 MB/tệp** — đều dưới trần 20MB/tệp | 7 tệp `.docx` **cùng cỡ 15,9 MB/tệp** (16 702 626 byte), dựng mới cho lượt đo này — đều dưới trần 20MB/tệp, nên nếu bị chặn thì chỉ có thể do phép kiểm **tổng** | Không |
| Mốc dưới trần (đối chứng ngược — phải nhận được) | Bước 3 của phiếu: 6 tệp = 95,4 MB → hệ thống im lặng, đúng | 6 tệp = **95,6 MB** → nhận đủ 6, không thông báo lỗi, chỉ số hiện *"Tổng dung lượng 95.6 MB / 100MB"*. Chứng minh chốt kiểm **so theo ngưỡng**, không chặn mù | Không |
| Mốc vượt trần (điểm phải bắt) | Bước 4: tệp thứ 7 → tổng **111,3 MB** ⇒ *không* dòng lỗi, *không* thông báo, **0 request** — chốt kiểm không tồn tại | Tệp thứ 7 → tổng sẽ là **~111,5 MB** ⇒ **bị từ chối**: thông báo *"Tổng dung lượng tệp vượt quá giới hạn 100MB."*, danh sách vẫn **6 tệp**, chỉ số vẫn **95.6 MB / 100MB** | Không |
| Ép sát đúng mốc 100MB (đo thêm, phiếu gốc không có) | Phiếu gốc chỉ đo 2 mốc cách trần khá xa: 95,4 MB (dưới) và 111,3 MB (trên) | Nạp thêm 1 tệp **4 MiB** → tổng **99.6 MB / 100MB**, **7 tệp vẫn được nhận**; nạp tiếp 1 tệp **1 MiB** (tổng ~100.6 MB) → **bị chặn**. Tệp thứ 8 này dưới cả trần 20MB/tệp lẫn trần 10 tệp ⇒ chỉ có thể do phép kiểm tổng, và ngưỡng nằm trong khoảng **~1 MiB quanh mốc 100MB** — không phải chặn ước lượng | Không |
| Chỉ số tổng dung lượng trên giao diện (`:1070` yêu cầu) | **Không có** chỗ nào hiển thị tổng; `coHienTongTren100 = false` | **Có**: dòng *"Tổng dung lượng {total} / 100MB"* ngay dưới danh sách tệp, cập nhật theo từng lần nạp (0 B → 31.9 MB → 95.6 MB) | Không |
| Dòng gợi ý hiển thị dưới ô tải tệp | *"Tối đa 10 tệp. Định dạng: … Dung lượng tối đa: 20MB/tệp."* — **không nhắc trần tổng 100MB** | *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp, **tổng 100MB**."* | Không |
| Đi hết luồng đến khi lưu + đọc lại hồ sơ | Bấm [Lưu] → hồ sơ `HD-20260730-002` lưu đủ **10 tệp**, tổng thật **167 015 490 byte** (~159 MB) | Bấm [Lưu] → hồ sơ **mới** `HD-20260730-006` lưu đúng **6 tệp** (16 311,2 KB/tệp), **không** có tệp thứ 7; tổng ~95,6 MB, dưới trần | Không |

## Bằng chứng đã mở đọc

- `bug-reports/image/BUG-TMHDVMPL_16-r5-doi-chung-6tep-95.6MB-duoc-nhan.png` — form *Thêm mới hỏi đáp* ở **mốc dưới trần**: 6 tệp `QA-r5-tong-01…06.docx` mỗi tệp *(15.9 MB)*, dòng **"Tổng dung lượng 95.6 MB / 100MB"** hiện rõ, dòng gợi ý đã nêu *"20MB/tệp, tổng 100MB"*. Đây cũng là **trạng thái sau khi tệp thứ 7 bị từ chối** — danh sách và chỉ số không đổi.
- `bug-reports/image/BUG-TMHDVMPL_16-r5-PASS-ban-ghi-moi-chi-luu-6tep-duoi-tran.png` — hồ sơ `HD-20260730-006` sau khi lưu: mục **File đính kèm** đúng **6 tệp**, không có tệp thứ 7; góc phải **CB Nghiệp vụ - Trung ương #03 · CB_NV_TW · BTP · TW**; thanh bên **HTPLDN · V1.0.3**.

## Phương pháp thứ hai (bắt buộc)

- **Đo tăng dần qua đúng điểm giao trần** thay vì chỉ đo một mốc: 2 tệp (31.9 MB) → 6 tệp (95.6 MB) → thử tệp 7 (~111.5 MB). Chốt kiểm bật đúng ở bước cuối ⇒ đây là **phép so ngưỡng thật**, không phải trùng hợp.
- **Đọc lại hồ sơ sau khi lưu** (phép thử quyết định của phiếu, vì bug gốc là *"lưu được 159 MB xuống máy chủ"*): `HD-20260730-006` chỉ có 6 tệp.
- **Bắt thông báo hiển thị** (bộ bắt cài trước thao tác, không lọc trùng): *"Tổng dung lượng tệp vượt quá giới hạn 100MB."* ⇒ hệ thống **nêu rõ lý do**, đúng yêu cầu phiếu.
- **Ép sát mốc thay vì đo mốc xa**: 95.6 MB (nhận) → 99.6 MB (nhận) → ~100.6 MB (chặn). Khoảng bất định của ngưỡng thu hẹp còn ~1 MiB, nên khẳng định "chốt kiểm đặt đúng ở 100MB" là đo được chứ không suy đoán.
- **Đo lại trên màn Chỉnh sửa** (bề mặt thứ hai của cùng ô File đính kèm): hồ sơ đang có 95,6 MB, nạp thêm tệp thứ 7 → cũng **bị từ chối**, thông báo *"Tổng dung lượng tệp đính kèm vượt quá giới hạn 100MB"* ⇒ chốt kiểm không chỉ có ở form Thêm mới.
- **Đối chiếu đặc tả** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md`):
  - `:1070` (SCR-II-01, thành phần 45 *File đính kèm*) — *"Tối đa 10 file/lần, **tổng tối đa 100MB**, mỗi file tối đa 20MB … **Tổng dung lượng hiển thị "{total} / 100MB"**"* ⇒ cả phép chặn lẫn chỉ số hiển thị nay đều khớp.

## Pass đối kháng (tự bác trước khi ghi sheet)

1. *"Có thể tệp thứ 7 bị chặn vì lý do khác (cỡ tệp, số tệp), không phải vì tổng."* — Bác: mỗi tệp **15,9 MB** (dưới trần 20MB/tệp, và 6 tệp cùng cỡ đó vừa được nhận), số tệp mới là **7** (dưới trần 10 tệp). Chỉ còn phép kiểm tổng. Câu thông báo cũng nói thẳng *"Tổng dung lượng…"*.
2. *"Có thể dev chặn mù mọi lần nạp thêm tệp."* — Bác bằng **đối chứng ngược**: 6 lần nạp liên tiếp trước đó đều được nhận, chỉ số tổng tăng đúng từng bước.
3. *"Có thể chỉ giao diện chặn, còn máy chủ vẫn nhận."* — Đã đo hết mức mà **đường giao diện** cho phép: tệp thứ 7 không rời được trình duyệt, và hồ sơ lưu xuống đọc lại chỉ có 6 tệp. Xem §Giới hạn để biết phần chưa đo.
4. *"Có thể chỉ hiển thị con số cho có, chốt kiểm vẫn hổng."* — Bác: chỉ số **và** phép chặn khớp nhau tại đúng ngưỡng, và hồ sơ lưu xuống phản ánh đúng.

## Giới hạn còn lại (khai báo minh bạch — không giấu)

- **Chưa đo riêng phần kiểm ở máy chủ.** Lượt re-verify này chạy hoàn toàn bằng thao tác thật trên giao diện theo yêu cầu, nên không gọi thẳng dịch vụ để thử vượt trần khi bỏ qua giao diện. Kết luận vì vậy nói về **luồng người dùng thật**: qua giao diện thì không còn lưu được hồ sơ vượt 100MB. Nếu cần chốt thêm lớp máy chủ thì phải mở một lượt kiểm riêng.
- **Chưa chụp được ảnh khung thông báo từ chối** (tự tắt rất nhanh, không lọt vào ảnh chụp dù thử nhiều cách). Bù lại: **nguyên văn câu thông báo** do bộ bắt sự kiện ghi lại, **danh sách giữ nguyên 6 tệp**, **chỉ số tổng không đổi**, và **hồ sơ lưu xuống chỉ 6 tệp**.

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Màn *Chỉnh sửa hỏi đáp* thiếu chỉ số tổng dung lượng.** Ở form Chỉnh sửa, mục **File đính kèm** **không** hiển thị dòng *"Tổng dung lượng {total} / 100MB"* (form Thêm mới thì có), và dòng gợi ý ở đó vẫn là bản cũ *"… Dung lượng tối đa: 20MB/tệp."* — thiếu cả trần tổng lẫn việc đã bỏ `.jpg, .png`. **Hành vi chặn thì đúng** (tệp thứ 7 vẫn bị từ chối). Cùng một chỗ sót với ghi nhận ở [TMHDVMPL_12-r5-reverify.md](TMHDVMPL_12-r5-reverify.md) §Ngoài tiêu chí phiếu ⇒ đề xuất gộp thành **một phiếu riêng cho màn Chỉnh sửa**, không dùng để mở lại 2 phiếu đã Pass.
- **Bản ghi tạo trong phiên này:** `HD-20260730-006` (*Mới*, 6 tệp `.docx`, ~95,6 MB). Tạo có chủ đích để verify trên dữ liệu mới; giữ lại làm vết kiểm chứng. Bảy tệp nguồn đặt ở `evidence-input/r5/tmhdvmpl16/`.
