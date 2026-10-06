# Phản hồi hai điểm vướng Dev nêu ngày 14/09/2026

| | |
|---|---|
| **Nguồn** | `docs/Reference/bao-cao-gap-tai-lieu-va-cau-hoi-ba-2026-09-14.md` |
| **Đối chiếu** | SRS v3.5 sau đợt cập nhật `[CR-GY-2026-09-13]`, commit `01b0116` |
| **Kết luận chung** | Cả hai đều là lỗ hổng thật của đặc tả, phát sinh từ chính đợt sửa vừa rồi |
| **Bản này là bản 2** | Bản 1 có lập luận sai ở BA-R1, đã bị bác khi soi lại — xem mục "Đính chính" cuối tài liệu |

---

## BA-R1 — Quyền đọc hồ sơ liên kết khác đơn vị

### Câu hỏi

Hỏi đáp thuộc đơn vị A chuyển thành Vụ việc thuộc đơn vị B. Cán bộ B đọc được gì của A, cán bộ A đọc được gì của B, áp cho vai nào?

### Dữ kiện quyết định — đơn vị đích đã có đủ dữ liệu để xử lý

`FR-II-11` **chép sang hồ sơ vụ việc** những thứ sau:

| Nội dung | Vị trí |
|---|---|
| Tiêu đề, nội dung câu hỏi | `srs-fr-02-hoi-dap.md` §Inputs trường 5, 6 |
| Lĩnh vực pháp luật | §Sáu trường bắt buộc |
| **Tệp đính kèm** | §Processing bước 6 |
| Ba trường phân loại doanh nghiệp | §Processing bước 7 |

Nghĩa là **đơn vị B không cần đọc hồ sơ hỏi đáp gốc để làm việc.** Mọi thứ cần cho việc xử lý đã nằm trong hồ sơ vụ việc của chính B.

Thứ B **không** có là **lịch sử nội bộ chặng hỏi đáp**: ghi chú tiếp nhận của cán bộ A, nội dung phản hồi A đã soạn dở, ai tại A đã xử lý. Đây là dữ liệu nội bộ của A — đúng loại dữ liệu mà phân quyền theo đơn vị sinh ra để bảo vệ, và **không cần thiết** cho việc xử lý vụ việc.

### Quyết định đề xuất

**Đối xứng, và KHÔNG cần ngoại lệ nào cho `BR-AUTH-08`.**

| Trường hợp | Xử lý |
|---|---|
| **Đơn vị đích = đơn vị nguồn** (trường hợp thông thường) | Mở hồ sơ liên kết đầy đủ ở chế độ chỉ đọc. Vốn đã đúng `BR-AUTH-08`, không phát sinh gì |
| **Đơn vị đích ≠ đơn vị nguồn** | **Cả hai chiều chỉ thấy thông tin về việc chuyển, không mở được hồ sơ đối ứng.** Cụ thể: mã hồ sơ, trạng thái, ngày chuyển, người chuyển, lý do chuyển. **Không** nội dung, **không** tệp đính kèm, **không** lịch sử xử lý |

Khối "Nguồn gốc hồ sơ" ở `SCR-V.I-03` và nhãn trạng thái *Đã chuyển sang Vụ việc* ở `SCR-II-02` **ẩn đường dẫn mở hồ sơ đối ứng** khi khác đơn vị; các ô còn lại giữ nguyên vì đều là thông tin về thao tác chuyển, không phải nội dung hồ sơ.

**Vai áp dụng:** không mở rộng cho vai nào. Người được phân công xử lý (Người hỗ trợ pháp lý, Tư vấn viên, Chuyên gia) làm việc trên hồ sơ vụ việc vốn đã có đủ dữ liệu, nên cũng không phát sinh nhu cầu đọc chéo.

**Cán bộ Trung ương và Quản trị hệ thống** vốn đã thấy toàn quốc (`srs-v3.5.md:1407`, `BR-AUTH-04`), mở được cả hai hồ sơ trong mọi trường hợp. Không đổi.

**Hệ quả cần chấp nhận:** khi doanh nghiệp gọi lại đơn vị A hỏi về vụ việc, A chỉ trả lời được *"hồ sơ đã chuyển sang đơn vị B, mã {mã vụ việc}"* rồi chuyển tiếp liên hệ. A không tra được tiến độ xử lý của B. Đây là đánh đổi có chủ đích: giữ nguyên ranh giới dữ liệu giữa các đơn vị, đổi lấy một bước chuyển tiếp liên hệ.

### Vì sao không chọn hướng mở quyền đọc chéo

Ba lý do, xếp theo mức quyết định:

1. **Không có nhu cầu nghiệp vụ thật.** Dữ liệu cần cho việc xử lý đã được chép sang. Phần còn lại là lịch sử nội bộ của đơn vị kia.
2. **"Chỉ đọc" vẫn là lộ dữ liệu.** Phân quyền theo đơn vị bảo vệ cả thao tác đọc, không riêng thao tác ghi. Hồ sơ hỏi đáp và tệp đính kèm chứa thông tin doanh nghiệp và có thể chứa bí mật kinh doanh.
3. **Mở quyền đọc kéo theo phạm vi lớn hơn nhiều.** Tệp đính kèm là bảng riêng có phân quyền riêng — mở màn hình mà không mở đường tải tệp thì cán bộ bấm vào báo lỗi; mở cả hai thì phải viết ràng buộc riêng cho từng đường. Cộng thêm nhật ký đọc chéo, và câu hỏi ai được xem nhật ký đó.

### Phương án thay thế nếu BA muốn đơn vị đích đọc được lịch sử chặng hỏi đáp

Thay vì mở quyền đọc chéo, **chép thêm lịch sử trao đổi sang hồ sơ vụ việc** tại thời điểm chuyển, cùng cách đang chép nội dung và tệp. Dữ liệu thành của B, không phát sinh quyền đọc chéo, không đụng `BR-AUTH-08`. Chi phí: thêm một bước chép ở `FR-II-11`.

### Sửa gì trong SRS

| # | Nội dung | Tệp |
|---|---|---|
| 1 | `FR-V.I-18` bước 3: đường dẫn mở hồ sơ hỏi đáp gốc **chỉ hiện khi cùng đơn vị**; khác đơn vị thì chỉ hiện thông tin về việc chuyển | `srs-fr-05-vu-viec.md` |
| 2 | `FR-II-11` §Postconditions: nêu rõ phạm vi đơn vị nguồn thấy được sau khi chuyển | `srs-fr-02-hoi-dap.md` |
| 3 | `SCR-V.I-03` khối "Nguồn gốc hồ sơ" và `SCR-II-02` nhãn trạng thái: điều kiện hiển thị đường dẫn | Hai tệp nhóm |

**Không sửa `BR-AUTH-08`.** Đây là điểm khác hẳn bản 1.

---

## BA-R2 — Áp dụng danh mục kiểm tra mới cho hồ sơ đã kiểm tra

### Câu hỏi

Vụ việc đã kết luận Đạt theo danh mục 6 hạng mục, nay danh mục có 7. Có bắt kiểm bổ sung hạng mục "phạm vi hỗ trợ" không?

### Dữ kiện đã rà

| Nội dung | Vị trí | Ghi nhận |
|---|---|---|
| Danh mục kiểm tra lưu dạng danh sách `{hang_muc_id, dat, ghi_chu}` | `srs-fr-05-vu-viec.md:521` | Số phần tử theo danh mục tại thời điểm kiểm |
| Lối tới Từ chối | §Máy trạng thái | `DANG_KIEM_TRA → TU_CHOI`, và `YEU_CAU_BO_SUNG → TU_CHOI` (tự động khi quá hạn bổ sung). **Không có lối nào từ `DA_PHAN_CONG` hoặc `DANG_XU_LY`** |
| Hồ sơ có thể quay lui | §Máy trạng thái | `DA_PHAN_CONG → DA_TIEP_NHAN` khi người được phân công từ chối |
| `YEU_CAU_BO_SUNG` | `srs-fr-05-vu-viec.md:522` | Là **một giá trị kết luận kiểm tra**, không phải "chưa kết luận" |

### Quyết định đề xuất

**Chia theo hành vi tại bước kiểm tra, không chia theo trạng thái và không chia theo ngày.**

| Tình huống | Xử lý |
|---|---|
| **Hồ sơ đi vào bước kiểm tra `FR-V.I-06`** — dù lần đầu, sau bổ sung, hay sau khi quay lui từ phân công | Hệ thống nạp **danh mục 7 hạng mục** hiện hành. Nếu hồ sơ đã có kết quả kiểm tra cũ với ít phần tử hơn, giữ nguyên các hạng mục đã tích và **bổ sung hạng mục còn thiếu ở trạng thái chưa tích**; cán bộ tích nốt rồi kết luận lại |
| **Hồ sơ không đi vào bước kiểm tra** — đang ở `DA_PHAN_CONG`, `DANG_XU_LY` và các trạng thái sau | **Giữ nguyên kết quả cũ. Không kiểm lại, không chặn xử lý tiếp** |

Cách này tự xử đúng cả ba ca mà cách chia theo trạng thái làm sai:

- Hồ sơ ở `YEU_CAU_BO_SUNG` **đã có kết luận** nhưng sẽ quay lại bước kiểm tra sau khi doanh nghiệp bổ sung — lúc đó áp danh mục 7 hạng mục, đúng.
- Hồ sơ từ `DA_PHAN_CONG` quay về `DA_TIEP_NHAN` do người được phân công từ chối — nếu cán bộ mở lại bước kiểm tra thì áp danh mục mới, nếu chỉ phân công lại thì không đụng.
- Hồ sơ `TU_CHOI` được mở lại bằng quyền quản trị — quay về `DA_TIEP_NHAN`, xử lý như trên.

**Ba lý do không bắt kiểm lại hồ sơ đang ở `DA_PHAN_CONG` trở đi:**

1. Kết luận kiểm tra hồ sơ là quyết định hành chính đã ban hành, doanh nghiệp đã được thông báo và hồ sơ đã vào quy trình.
2. Hạng mục mới không thêm điều kiện pháp lý mới — nó làm tường minh một điều vốn ngầm định.
3. **Không có đường xử lý hệ quả.** Máy trạng thái không có lối từ `DA_PHAN_CONG` hay `DANG_XU_LY` sang `TU_CHOI`. Bắt kiểm lại mà không mở lối chuyển mới sẽ tạo hồ sơ kẹt: biết ngoài phạm vi nhưng không đóng được.

### Rủi ro còn lại — nêu rõ để BA biết mà chấp nhận

Nếu một hồ sơ cũ **thật sự ngoài phạm vi** mà đã sang `DA_PHAN_CONG` hoặc `DANG_XU_LY`, hệ thống **không có cách dừng nó** cho tới khi hoàn thành. Hai lựa chọn:

- **Chấp nhận.** Cửa sổ hữu hạn, chỉ gồm số hồ sơ đang dở tại thời điểm áp dụng, và các hồ sơ này đều đã qua kiểm tra nội dung của cán bộ. *Khuyến nghị.*
- **Mở lối chuyển mới** từ `DA_PHAN_CONG` và `DANG_XU_LY` sang `TU_CHOI`. Giải quyết triệt để nhưng là thay đổi máy trạng thái, phạm vi lớn hơn hẳn phiếu góp ý đang áp, và ảnh hưởng mọi vụ việc chứ không riêng hồ sơ cũ.

### Hiển thị hạng mục thiếu

Hồ sơ kiểm tra theo danh mục cũ lưu ít phần tử hơn 7. Khi mở lại màn chi tiết mà **không** đi vào bước kiểm tra, hạng mục thiếu hiển thị nhãn **"Không áp dụng — hồ sơ kiểm tra theo danh mục trước đây"**, ô tích để trống và khóa.

Báo cáo thống kê lý do từ chối xếp hồ sơ này vào nhóm **"Không xác định"**, không suy đoán ngược.

> Đặc tả viết theo **số phần tử thực tế của bản ghi**, không viết theo ngày áp dụng. Như vậy quy tắc đúng cho mọi bản ghi thiếu hạng mục, bất kể vì sao thiếu, và không phụ thuộc việc có chạy chuyển đổi dữ liệu hay không.

### Sửa gì trong SRS

| # | Nội dung | Tệp |
|---|---|---|
| 1 | `FR-V.I-06` §Processing: quy tắc nạp danh mục — giữ hạng mục đã tích, bổ sung hạng mục còn thiếu ở trạng thái chưa tích | `srs-fr-05-vu-viec.md` |
| 2 | `FR-V.I-06` quy định hiển thị hạng mục thiếu khi không đi vào bước kiểm tra | `srs-fr-05-vu-viec.md` |
| 3 | `SCR-V.I-03` Accordion 4: nhãn "Không áp dụng" và trạng thái khóa | `srs-fr-05-vu-viec.md` |
| 4 | Báo cáo lý do từ chối: nhóm "Không xác định" cho hồ sơ thiếu hạng mục | `srs-fr-11-bao-cao.md` |

---

## Tổng hợp

| Mã | Quyết định đề xuất | Số chỗ sửa | Chờ |
|---|---|---|---|
| **BA-R1** | Khác đơn vị thì cả hai chiều chỉ thấy thông tin về việc chuyển, không mở được hồ sơ đối ứng. **Không sửa `BR-AUTH-08`** | 3 | **BA duyệt** |
| **BA-R2** | Chia theo hành vi tại bước kiểm tra, không theo trạng thái. Hồ sơ vào bước kiểm tra thì áp danh mục 7 hạng mục; hồ sơ không vào thì giữ nguyên | 4 | **BA duyệt** |

Chưa sửa dòng SRS nào.

---

## Đính chính so với bản 1

Bản 1 của tài liệu này đề xuất **mở quyền đọc chéo đơn vị** cho BA-R1, lập luận rằng *"không có nội dung câu hỏi và tài liệu thì đơn vị đích không xử lý được, doanh nghiệp phải nộp lại từ đầu"*.

**Lập luận đó sai.** `FR-II-11` §Processing bước 6 đã chép tệp đính kèm, Inputs 5–6 đã chép tiêu đề và nội dung sang hồ sơ vụ việc. Đơn vị đích có đủ dữ liệu để làm việc mà không cần đọc hồ sơ gốc. Bản 1 vì thế đề xuất mở một ngoại lệ phân quyền không có nhu cầu nghiệp vụ đỡ lưng.

Hai chỗ sai nhỏ hơn cũng đã sửa:

- Bản 1 viết *"chỉ có một lối tới Từ chối"*. Thực tế còn lối `YEU_CAU_BO_SUNG → TU_CHOI` tự động khi quá hạn bổ sung. Phát biểu đúng là: không có lối nào từ `DA_PHAN_CONG` hoặc `DANG_XU_LY` sang `TU_CHOI`.
- Bản 1 xếp `YEU_CAU_BO_SUNG` vào nhóm "chưa có kết luận". Sai — đó là một giá trị kết luận kiểm tra. Bản 2 bỏ hẳn cách chia theo trạng thái.
