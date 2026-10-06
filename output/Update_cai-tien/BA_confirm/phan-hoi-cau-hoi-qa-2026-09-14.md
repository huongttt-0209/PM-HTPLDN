# Phản hồi phiếu hỏi QA — đợt CR-GY-2026-09-13

| | |
|---|---|
| **Phiếu nguồn** | `docs/Reference/ba-confirmation-needed-cr-gy-2026-09-14.md` — 8 câu hỏi, 3 giả định |
| **Đối chiếu** | SRS v3.5 commit `01b0116`, cộng đợt sửa `[CR-DEV-2026-09-14]` chưa commit |
| **Kết luận chung** | **QA đúng sự thật ở cả 8 câu.** Không câu nào là hiểu nhầm. Bảy câu là lỗ hổng do đợt `[CR-GY-2026-09-13]` sinh ra; một câu (Q06) là quy tắc đã có sẵn nhưng bị chôn ở chỗ khó thấy |
| **Ba giả định G1–G3** | **Đều đúng**, QA viết testcase theo đó được |

---

## Q01 — Ba trường phân loại trên vụ việc sau khi chuyển luồng

**Chốt: Hướng 1 — vụ việc KHÔNG giữ riêng ba trường. Bỏ bước 7 của FR-II-11.**

QA đúng: bảng thuộc tính `VU_VIEC` không có ba cột đó ở bất kỳ tệp nào (kiểm lại: 0 kết quả). Bước 7 đang chép dữ liệu vào chỗ không tồn tại.

**Lý do chọn Hướng 1:**

Nguyên tắc ảnh chụp được đặt ra cho **hồ sơ hỏi đáp** vì hỏi đáp cho phép ẩn danh, có thể **không gắn doanh nghiệp nào** — không có nguồn để tra sau. Vụ việc thì khác: `doanh_nghiep_id` là **trường bắt buộc**, nên vụ việc luôn tra được quy mô, hình thức tổ chức và địa bàn qua hồ sơ doanh nghiệp, như mọi vụ việc khác.

Thêm ba cột vào `VU_VIEC` sẽ tạo **nguồn thứ hai** cho cùng một dữ liệu ở nhóm Vụ việc, trong khi báo cáo vụ việc hiện đọc thẳng từ hồ sơ doanh nghiệp. Đó là thay đổi vượt phạm vi phiếu góp ý.

**Trường hợp câu hỏi ẩn danh — chốt thêm:** khi cán bộ gắn hồ sơ doanh nghiệp lúc chuyển, hệ thống **ghi luôn doanh nghiệp đó vào hồ sơ hỏi đáp gốc** và **điền ba trường phân loại theo doanh nghiệp vừa gắn**, trước khi đóng hồ sơ. Nếu không làm vậy, hồ sơ hỏi đáp vĩnh viễn ở nhóm "Không xác định" trong báo cáo dù danh tính doanh nghiệp đã biết.

**Sửa trong SRS:** bỏ bước 7 FR-II-11 · thêm bước ghi doanh nghiệp và ba trường vào hồ sơ gốc khi câu hỏi ẩn danh · sửa `BR-FLOW-11` (a) bỏ vế "các trường phân loại" · bỏ câu "Ba trường phân loại mới của T3 cũng chép sang hồ sơ vụ việc" ở FR-II-11.

---

## Q02 — Sửa, xóa hồ sơ hỏi đáp đã chuyển luồng

**Chốt: Hướng 1 — chặn cả sửa lẫn xóa mềm.** QA nghiêng đúng.

Ghi chú máy trạng thái và `BR-FLOW-11` (d) đều nói hồ sơ đã chuyển là hồ sơ đóng, chỉ đọc. Ma trận phân quyền chưa cập nhật vì nó có từ trước đợt này.

**Lý do:** hồ sơ hỏi đáp đã chuyển là **bản gốc của một vụ việc đang chạy**. Cho sửa thì nội dung gốc lệch khỏi nội dung đã chép sang vụ việc, mất giá trị đối chiếu. Cho xóa thì vụ việc mất bản gốc, và liên kết truy nguồn trỏ vào chỗ trống.

**Sửa trong SRS:** hai dòng ma trận phân quyền `HOI_DAP_UPDATE` và `HOI_DAP_DELETE` thêm `DA_CHUYEN_LUONG` vào danh sách trạng thái bị chặn · màn danh sách hỏi đáp đồng bộ điều kiện.

`ERR-CL-VV-01` giữ lại, chỉ còn phục vụ trường hợp dữ liệu hỏng.

---

## Q03 — Xóa vụ việc sinh từ cầu nối

**Chốt: tách hai việc vốn khác bản chất.** Không theo trọn Hướng 1 như QA nghiêng, vì chặn hết tạo ngõ cụt.

| Tình huống | Bản chất | Xử lý |
|---|---|---|
| **Vụ việc đã tiếp nhận** (`DA_TIEP_NHAN` trở đi) | Hồ sơ đã vào quy trình | **Chặn xóa.** Muốn dừng thì đi đường từ chối — có thông báo gửi doanh nghiệp kèm hướng dẫn gửi lại |
| **Vụ việc còn `CHO_TIEP_NHAN`** | **Sửa lỗi nội bộ** — hồ sơ tạo nhầm, chưa ai xem xét | **Cho xóa mềm**, đồng thời **mở lại hồ sơ hỏi đáp gốc**: trả về trạng thái trước khi chuyển, xóa liên kết truy nguồn để chuyển lại được |

**Vì sao không chặn hết.** Cán bộ có thể gắn nhầm doanh nghiệp hoặc chọn nhầm loại hình hỗ trợ lúc chuyển. Kiểm lại SRS: `FR-V.I-05` chỉ có xem, tìm kiếm và xóa — **không có thao tác sửa**; `FR-V.I-01` là màn danh sách và tìm kiếm. Nên nếu chặn xóa thì vụ việc tạo nhầm **không xóa được, không sửa được, không chuyển lại được** vì liên kết có ràng buộc duy nhất. Hồ sơ kẹt vĩnh viễn ở hàng chờ.

**Vì sao vẫn giữ nguyên quyết định "từ chối thì không mở lại hồ sơ gốc".** Hai việc khác bản chất: **từ chối là kết quả nghiệp vụ** — hồ sơ đã được cán bộ xem xét và kết luận; **xóa ở Chờ tiếp nhận là sửa lỗi nội bộ** — chưa ai xem xét, chưa có kết luận nào để bảo lưu.

**Doanh nghiệp đã nhận thông báo chuyển luồng ở bước 11**, nên khi xóa và mở lại hồ sơ gốc phải **gửi thông báo đính chính**: vướng mắc quay lại quy trình hỏi đáp, mã vụ việc trước đó không còn hiệu lực.

### Sáu điểm của đường hoàn tác — chốt rõ để viết được kết quả mong đợi

| # | Điểm | Chốt |
|---|---|---|
| 1 | **Trạng thái sau khi mở lại** | **Luôn về `TIEP_NHAN`**, không khôi phục `DANG_XU_LY` kể cả khi hồ sơ vốn ở trạng thái đó lúc chuyển. Lý do: người được phân công đã nhận thông báo hồ sơ chuyển đi (xem Q08), khôi phục `DANG_XU_LY` sẽ mâu thuẫn với thông báo đó. Cán bộ **phân công lại**. Chỉ một lối chuyển duy nhất `DA_CHUYEN_LUONG → TIEP_NHAN` |
| 2 | **Phân công cũ** | **Không khôi phục.** Xóa người được phân công, hồ sơ về hàng chờ phân công |
| 3 | **Ràng buộc duy nhất trên liên kết** | `VU_VIEC.hoi_dap_goc_id` UNIQUE **`WHERE is_deleted = 0`** — theo đúng khuôn đã dùng ở các bảng nối khác trong SRS. Vụ việc đã xóa mềm **giữ nguyên** `hoi_dap_goc_id` để truy vết, không cản việc chuyển lại |
| 4 | **Liên kết trên hồ sơ hỏi đáp** | **Xóa `vu_viec_dich_id`** khi mở lại, nếu không thì điều kiện chuyển ở PRE-03 chặn lần chuyển sau. Mã vụ việc đã xóa ghi vào **lịch sử xử lý** của hồ sơ hỏi đáp, không mất dấu |
| 5 | **Thời hạn xử lý** | **Khôi phục `deadline` và mức cảnh báo từ hai trường ảnh chụp** `deadline_luc_chuyen`, `muc_do_canh_bao_luc_chuyen`. **KHÔNG tính lại từ đầu** — nếu tính lại, cán bộ có thể kéo dài hạn xử lý bằng cách chuyển nhầm rồi xóa. Sau khi khôi phục, xóa ba trường `ngay_chuyen_luong`, `deadline_luc_chuyen`, `muc_do_canh_bao_luc_chuyen` để hồ sơ ở `TIEP_NHAN` không còn mang dấu đã chuyển |
| 6 | **Doanh nghiệp và ba trường phân loại** | **GIỮ NGUYÊN, không hoàn tác.** Với câu hỏi vốn ẩn danh, doanh nghiệp được gắn lúc chuyển (Q01) là **thông tin đã biết**, không phải thao tác nhầm cần gỡ. Hoàn tác sẽ làm hồ sơ quay về ẩn danh dù danh tính đã xác định |

**Sửa trong SRS:** `FR-V.I-05` bước 5 thêm điều kiện — vụ việc có `hoi_dap_goc_id` chỉ xóa được khi còn `CHO_TIEP_NHAN` · thêm mã lỗi chặn xóa khi đã tiếp nhận · `FR-II-11` thêm mục hoàn tác với sáu điểm trên · máy trạng thái Hỏi đáp thêm lối `DA_CHUYEN_LUONG → TIEP_NHAN` · ràng buộc duy nhất trên `hoi_dap_goc_id` thêm điều kiện `WHERE is_deleted = 0` ở cả hai nơi khai · thông báo đính chính gửi doanh nghiệp.

> **Lưu ý phạm vi:** đây là **lối chuyển trạng thái mới duy nhất** của đợt này, và chỉ cho nhóm Hỏi đáp. Máy trạng thái Vụ việc **không đổi** — vẫn không có lối từ `DA_PHAN_CONG` hay `DANG_XU_LY` sang `TU_CHOI`.

Điểm này cũng đóng phần còn thiếu của `BR-FLOW-11` (g): **nhận biết hồ sơ chuyển luồng theo liên kết truy nguồn, không theo kênh** — `FR-V.I-05` đang lọc theo kênh nên vụ việc từ cầu nối mới lọt vào màn hồ sơ từ hệ thống khác.

---

## Q04 — Kết luận kiểm tra hồ sơ với danh mục 7 hạng mục

**Chốt (a): Hướng 1 — hạng mục 1 không đạt thì ép kết luận Không đạt.**

Hạng mục 1 là kết luận về **phạm vi**, không phải giấy tờ. Vụ việc ngoài phạm vi hỗ trợ thì không thể kết luận Đạt, và cũng **không thể yêu cầu bổ sung** — nộp thêm giấy tờ không làm vụ việc trở thành trong phạm vi. Chỉ còn một kết luận hợp lý.

**Chốt (b): Hướng 2 — cho kết luận Không đạt, thêm loại lý do thứ ba "Lý do khác" bắt buộc ghi rõ.**

Bảy hạng mục **không phải toàn bộ căn cứ từ chối**. Có những ca hợp lệ vẫn phải từ chối dù hồ sơ đủ giấy tờ và trong phạm vi: yêu cầu trùng với hồ sơ đã nộp trước đó, sai tư cách phát hiện khi đối chiếu, xung đột lợi ích của người được phân công. Cấm kết luận Không đạt trong những ca này sẽ **nhốt cán bộ** — buộc họ hoặc tích sai một hạng mục để ép hệ thống, hoặc để hồ sơ treo.

Ba loại lý do — Ngoài phạm vi, Thiếu thành phần hồ sơ, Lý do khác — vẫn tách bạch được trong số liệu, không nhóm nào rỗng nghĩa. Riêng "Lý do khác" **bắt buộc ghi rõ nội dung**, tối thiểu 10 ký tự như quy định hiện hành.

**Thứ tự ưu tiên khi suy ra loại lý do — chốt để kết quả xác định:**

| Tình trạng danh mục | Loại lý do |
|---|---|
| Hạng mục 1 không đạt | `NGOAI_PHAM_VI` — hệ thống đặt, cán bộ không đổi được |
| Hạng mục 1 đạt, có hạng mục 2–7 không đạt | `THIEU_TAI_LIEU` — hệ thống đặt, cán bộ không đổi được |
| **Cả 7 hạng mục đều đạt** | `KHAC` — **chỉ trường hợp này mới chọn được**, kèm nội dung bắt buộc |

Nói cách khác: **`KHAC` không phải lựa chọn thay thế cho hai loại kia.** Còn hạng mục nào chưa đạt thì hệ thống suy ra loại lý do tương ứng, không mở ô chọn.

**Giữ nguyên quyền chọn "Yêu cầu bổ sung"** trong mọi trường hợp trừ khi hạng mục 1 không đạt — yêu cầu bổ sung không phải từ chối.

**Sửa trong SRS:** FR-V.I-06 Processing thêm nhánh ép kết luận khi hạng mục 1 không đạt · trường loại lý do thêm giá trị thứ ba `KHAC` kèm nhãn "Lý do khác" và ràng buộc bắt buộc ghi nội dung · thêm mã lỗi cho tổ hợp kết luận không khớp danh mục · bổ sung tiêu chí chấp nhận.

---

## Q05 — Hạng mục "thuộc phạm vi hỗ trợ" nằm ở đâu

**Chốt: Hướng 1 — cố định trong hệ thống, Quản trị hệ thống không sửa, không xóa, không đổi thứ tự.** QA nghiêng đúng.

Hạng mục 1 mang **quy tắc nghiệp vụ riêng** — không đạt thì ép kết luận Không đạt và đặt loại lý do Ngoài phạm vi. Một bản ghi danh mục do người dùng cấu hình không thể mang quy tắc như vậy. Ngoài ra danh mục UC106 (FR-VIII-08) chỉ có trường thành phần bắt buộc và tùy chọn, không có chỗ cho một hạng mục kết luận.

**Sửa trong SRS:** sửa câu "tải danh mục kiểm tra từ cấu hình UC106" thành: hạng mục 1 cố định trong hệ thống, hạng mục 2–7 lấy từ danh mục UC106 · ghi rõ ở FR-VIII-08 rằng danh mục này chỉ quản lý thành phần hồ sơ.

---

## Q06 — Quy mô doanh nghiệp lấy từ cột nào

**Chốt: Hướng 1 — `loai_dn_id` là nguồn chuẩn duy nhất. Và quy tắc này ĐÃ CÓ SẴN trong SRS.**

`srs-fr-07-doanh-nghiep.md:349` đã ghi: *"giá trị quy_mo (SIEU_NHO/NHO/VUA) ánh xạ về `DOANH_NGHIEP.loai_dn_id` FK lookup tới DANH_MUC… entity DOANH_NGHIEP §3.4.3.3 lưu cột `loai_dn_id` **chứ không có cột `quy_mo` riêng**; trường `quy_mo` ở Inputs/Outputs là **alias UI**"*.

Nghĩa là **không có hai cột**. Chỉ có một cột lưu thật là `loai_dn_id`; `quy_mo` là tên gọi ở tầng giao diện và đầu vào, giá trị chính là mã của bản ghi danh mục. Báo cáo FR-IX-13 và FR-IX-18 lọc theo `SIEU_NHO / NHO / VUA` là lọc theo **mã danh mục**, cùng một dữ liệu. **Không có nguy cơ hai báo cáo ra số khác nhau.**

Quy tắc này chỉ nằm ở một dòng trong một tệp nhóm, không nhìn thấy được từ bảng thuộc tính lẫn từ các FR báo cáo — nên QA đọc thành hai cột là hợp lý.

**Một rủi ro lệch số liệu KHÁC, không phải chuyện hai cột — bổ sung sau khi rà lại:** báo cáo hỏi đáp `FR-IX-01` gom theo **ảnh chụp tại thời điểm tiếp nhận**, còn báo cáo vụ việc `FR-IX-13` đọc **hồ sơ doanh nghiệp hiện tại**. Một yêu cầu đi qua cầu nối có thể được xếp vào hai mức quy mô khác nhau ở hai báo cáo, nếu doanh nghiệp đổi quy mô trong thời gian đó. **Đây là thiết kế có chủ đích, không phải lỗi đối soát** — hai báo cáo trả lời hai câu hỏi khác nhau về hai mốc thời gian khác nhau. Phải ghi rõ vào đặc tả để người đọc báo cáo không đi tìm nguyên nhân lệch.

**Sửa trong SRS:** ghi chú quan hệ alias vào bảng thuộc tính `DOANH_NGHIEP` ở tệp nền · ghi chú nguồn dữ liệu ở FR-IX-13 và FR-IX-18 · ghi chú hai mốc thời gian khác nhau ở FR-IX-01 và FR-IX-13.

**Dọn kèm — một mâu thuẫn thật QA chỉ ra:** `loai_dn_id` ghi **không bắt buộc** ở FR-V.III-01 (`srs-fr-07:106`) nhưng **bắt buộc** ở cả hai bảng thuộc tính (`srs-v3.5.md:1746`, `srs-fr-07:695`). Theo chốt của BA ngày 30/05/2026 — kênh cán bộ nhập và kênh đầu nối chỉ bắt buộc hai trường định danh — thì **bảng thuộc tính sai**. Sửa hai bảng thành không bắt buộc, kèm ghi chú bắt buộc khi doanh nghiệp tự đăng ký.

---

## Q07 — Số thẻ tư vấn viên ở luồng cán bộ nhập tay (FR-IV-01)

**Chốt: Hướng 1 — áp ràng buộc như hai luồng kia.** QA nghiêng đúng.

FR-IV-01 dùng chung màn `SCR-IV-02`, mà màn đó đã ghi bắt buộc khi loại là Tư vấn viên. Để FR-IV-01 không bắt buộc thì cán bộ có một đường vòng để tạo hồ sơ tư vấn viên thiếu thẻ — đúng cái mà đợt sửa vừa rồi đi bịt.

QA còn chỉ ra một lỗi có sẵn: trường 12 của FR-IV-01 tên là **`so_the`**, trong khi cột thật đã đổi thành `so_the_hanh_nghe` và chuyển sang hồ sơ tư vấn viên. Tên cũ trỏ vào cột không còn tồn tại.

**Sửa trong SRS:** FR-IV-01 trường 12 đổi tên thành `so_the_hanh_nghe`, ràng buộc thành bắt buộc có điều kiện, trỏ mã lỗi · bổ sung trường tệp thẻ · tiêu chí chấp nhận nêu rõ.

**Không hồi tố vẫn giữ nguyên:** ràng buộc chỉ chặn tại thời điểm lưu. Hồ sơ cũ thiếu thẻ mà không ai mở ra sửa thì vẫn hợp lệ.

---

## Q08 — Thông báo khi chuyển hồ sơ hỏi đáp sang vụ việc

**Chốt: định nghĩa đủ ba người nhận.**

| Người nhận | Nhận gì | Vì sao |
|---|---|---|
| **Doanh nghiệp** | Vướng mắc đã được chuyển sang quy trình vụ việc hỗ trợ pháp lý, kèm mã vụ việc mới, đơn vị thụ lý, và lưu ý **cần bổ sung hồ sơ theo Mẫu 01** để cơ quan tiếp tục xử lý | Doanh nghiệp phải biết hồ sơ đi đâu và còn phải làm gì. Không báo thì họ tưởng câu hỏi bị bỏ quên |
| **Cán bộ Nghiệp vụ của đơn vị thụ lý có quyền tiếp nhận vụ việc** — cùng tập người nhận mà `FR-V.I-02` đang dùng, không định nghĩa tập mới | Có hồ sơ mới chờ tiếp nhận, kèm mã vụ việc và mã hỏi đáp gốc | Hồ sơ vào hàng chờ của họ |
| **Người đang được phân công xử lý hồ sơ hỏi đáp** — Người hỗ trợ pháp lý hoặc Tư vấn viên | Hồ sơ đang xử lý đã được chuyển sang nhóm Vụ việc, không cần xử lý tiếp | QA phát hiện đúng: hồ sơ ở trạng thái Đang xử lý **luôn đã được phân công**. Không báo thì người đó vẫn đang soạn trả lời cho một hồ sơ đã đóng |

**Doanh nghiệp chưa có tài khoản** — áp **đúng quy tắc đã có** tại `BR-NOTIF-01`, không đặt cách xử lý riêng: chỉ gửi **thư điện tử** tới địa chỉ liên hệ của doanh nghiệp; hệ thống vẫn tạo bản ghi thông báo để lưu vết nhưng **không hiển thị trong ứng dụng**; **thiếu địa chỉ thư thì ghi cảnh báo để cán bộ liên hệ ngoài hệ thống**, không chặn luồng nghiệp vụ. `[BA chốt 06/08/2026]`

**Chống gửi trùng:** một người có thể thuộc nhiều nhóm người nhận cùng lúc — ví dụ cán bộ vừa là người được phân công hồ sơ hỏi đáp, vừa thuộc nhóm tiếp nhận vụ việc của đơn vị thụ lý. **Mỗi người chỉ nhận một thông báo cho một lần chuyển**, nội dung theo vai ưu tiên cao hơn là người được phân công.

**Sửa trong SRS:** thêm sự kiện chuyển luồng vào danh sách kích hoạt của `BR-NOTIF-01` · FR-II-11 bước 11 liệt đủ ba người nhận, cách xác định tập người nhận, nội dung và quy tắc chống gửi trùng · nêu cách xử lý khi doanh nghiệp chưa có tài khoản.

---

## Ba giả định của QA — đều đúng

| # | Giả định | Xác nhận |
|---|---|---|
| **G1** | Tiếp nhận hồ sơ chưa có lĩnh vực mà không chọn → hệ thống chặn | **Đúng.** FR-II-03 trường 3 bắt buộc khi hồ sơ chưa có lĩnh vực. SRS không đặt mã lỗi riêng, dùng thông báo bắt buộc chung của biểu mẫu — QA không kiểm mã là hợp lý |
| **G2** | `KPI-S-03` hiểu "vụ việc đóng trong kỳ" giống `KPI-S-02` | **Đúng.** `KPI-S-03` §Processing bước 1 dùng đúng tập đó |
| **G3** | `FR-II-12` chỉ chạy ở màn tiếp nhận và màn soạn phản hồi, chỉ khi hồ sơ đã có lĩnh vực | **Đúng.** PRE-02 của FR-II-12 yêu cầu hồ sơ đã có lĩnh vực; lĩnh vực là điều kiện lọc cứng nên không có lĩnh vực thì không gợi ý được |

---

## Tổng hợp

| Mã | Chốt | Số chỗ sửa SRS |
|---|---|---|
| **Q01** | Hướng 1 — bỏ bước 7; ẩn danh thì ghi doanh nghiệp và ba trường vào hồ sơ gốc trước khi đóng | 4 |
| **Q02** | Hướng 1 — chặn sửa và xóa hồ sơ đã chuyển | 3 |
| **Q03** | Tách hai việc — chặn xóa sau khi tiếp nhận; cho xóa khi còn Chờ tiếp nhận kèm mở lại hồ sơ gốc, chốt 6 điểm của đường hoàn tác | 7 |
| **Q04** | (a) Hướng 1 ép Không đạt · (b) **Hướng 2** — thêm loại lý do "Lý do khác" | 4 |
| **Q05** | Hướng 1 — hạng mục 1 cố định trong hệ thống | 2 |
| **Q06** | Hướng 1 — `loai_dn_id` là nguồn chuẩn. Kèm dọn mâu thuẫn bắt buộc và ghi rõ hai báo cáo dùng hai mốc thời gian | 5 |
| **Q07** | Hướng 1 — áp ràng buộc cho FR-IV-01, sửa tên trường lỗi thời | 3 |
| **Q08** | Ba người nhận kèm cách xác định tập, chống gửi trùng; doanh nghiệp chưa có tài khoản áp đúng `BR-NOTIF-01` sẵn có | 4 |

**Tổng 32 chỗ sửa.** Chưa sửa dòng SRS nào, chờ BA duyệt.

**Một ghi nhận về chất lượng phiếu:** QA dẫn chứng từng dòng và mở tệp kiểm lại, nên tám câu đều trúng. Riêng Q06 là trường hợp quy tắc đã có nhưng bị chôn ở một dòng giữa tệp nhóm — lỗi trình bày của SRS, không phải QA đọc sót.


---

## Đính chính so với bản 1

Bản 1 của tài liệu này sai ba chỗ, phát hiện khi soi lại:

| Câu | Bản 1 | Bản 2 | Vì sao |
|---|---|---|---|
| **Q08** | "Không có địa chỉ thư thì chỉ ghi thông báo trong hệ thống, doanh nghiệp xem khi đăng ký" | Áp đúng `BR-NOTIF-01` sẵn có | Quy tắc đã tồn tại và BA đã chốt ngày 06/08/2026. Bản 1 tự đặt cách xử lý riêng mà không tra quy ước chung |
| **Q04(b)** | Cấm kết luận Không đạt khi bảy hạng mục đều đạt | Cho phép, thêm loại lý do "Lý do khác" | Bảy hạng mục không phải toàn bộ căn cứ từ chối. Quy tắc cũ nhốt cán bộ khi gặp ca trùng yêu cầu, sai tư cách hay xung đột lợi ích |
| **Q03** | Chặn xóa mọi vụ việc có liên kết truy nguồn | Chặn sau khi tiếp nhận; cho xóa khi còn Chờ tiếp nhận kèm mở lại hồ sơ gốc | `FR-V.I-05` và `FR-V.I-01` đều **không có thao tác sửa**, nên chặn xóa làm vụ việc tạo nhầm kẹt vĩnh viễn — không xóa, không sửa, không chuyển lại được |

Bổ sung thêm một điểm bỏ sót ở **Q06**: rủi ro lệch số liệu thật không nằm ở chuyện hai cột, mà ở chỗ báo cáo hỏi đáp dùng ảnh chụp còn báo cáo vụ việc đọc dữ liệu hiện tại.


## Đính chính so với bản 2

Bản 2 mở đường hoàn tác ở Q03 nhưng để trống sáu điểm, khiến QA không viết được kết quả mong đợi. Bản 3 chốt cả sáu — quan trọng nhất là **khôi phục thời hạn từ ảnh chụp thay vì tính lại**, để đường hoàn tác không trở thành cách kéo dài hạn xử lý.

Bổ sung hai chỗ khác cũng chưa đủ xác định để viết testcase: **thứ tự ưu tiên của loại lý do `KHAC`** ở Q04(b), và **cách xác định tập người nhận cùng quy tắc chống gửi trùng** ở Q08.
