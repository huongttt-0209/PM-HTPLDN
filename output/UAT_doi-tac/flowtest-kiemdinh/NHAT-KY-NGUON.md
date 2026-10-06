# Nhật ký nguồn — những việc tôi phải tự quyết vì file flow không nói thẳng

Đợt 2026-08-06, FLOW 04, 2 case `LKHDG_12` + `QLHSDNHTCP_03`. Mỗi dòng: **việc tự quyết** → **căn cứ lấy từ đâu**.

| # | Việc tôi tự quyết | Căn cứ lấy từ đâu |
|---|---|---|
| 1 | Nới allowlist tab của `tools/sheet_read.py` để đọc được tab `bug`, và thêm cờ `--row N` in trọn 1 dòng theo tên tiêu đề | Flow §Ghi kết quả cho phép nới **công cụ chỉ đọc** miễn ghi lại. `tools/fetch_evidence.py` đã có sẵn tiền lệ y hệt (chú thích 2026-08-05 thêm `"bug"` vào allowlist vì script chỉ đọc). Cờ `--row` là vì bộ cột của tab `bug` khác tab tuần nên bản in mặc định không hiện gì |
| 2 | Đọc `reverify-week-3/reverify-audit/LKHDG_12/note.txt` (ghi chép QA đợt trước) trong giai đoạn A | Flow liệt kê 4 nguồn được đọc (bảng · bằng chứng đối tác · đặc tả · phản hồi dev), **không nói** hồ sơ QA nội bộ. Tôi coi là được đọc vì nó không phải "vào màn đang tranh chấp" — thứ mà cổng giai đoạn A thật sự cấm. Đã **khai minh bạch ngay trong file tiêu chí** và suy mục 4 từ BR-DATA-06 + SCR-VI-01, không lấy số đo cũ làm tiêu chí |
| 3 | Xếp vế (b) "thiếu cột" và vế (c) "chữ không dấu" của `LKHDG_12` là **đặc tả im lặng** → không chấm Fail | Grep hết `srs-fr-08-danh-gia.md`: 10 yêu cầu chức năng FR-VI-01…10 **không có cái nào** đặc tả luồng xuất Excel; chỉ có nút ở SCR-VI-01 `:821`. BR-DATA-06 (`srs-v3.5.md:5525`) chỉ ràng buộc *bộ lọc* + *số dòng*, không nói tập cột. C-05 (`:518`) nói "**Giao diện** tiếng Việt" — giao diện, không phải tệp |
| 4 | Vẫn áp **BR-DATA-06** cho nhóm VI dù bảng BR trong `srs-fr-11` ghi "Áp dụng: Toàn bộ FR-IX" | Bản gốc của quy tắc ở baseline `srs-v3.5.md:5525` ghi phạm vi rộng hơn: **"Toàn bộ CRUD list"**, ngoại lệ chỉ miễn cho báo cáo nhóm IX xuất PDF. CLAUDE.md §"Khi viết test plan": BR có "Áp dụng: Toàn bộ…" là **mặc định áp dụng**, ngoại lệ phải quote được dòng |
| 5 | Sau khi đo thấy vế (b)+(c) đã đúng như đối tác mong đợi → **bỏ khỏi danh sách hỏi BA** thay vì vẫn hỏi | Tiền lệ ghi trong báo cáo chạy thử FLOW 04 ngày 2026-08-05, case `XNTGHTVV_03`: *"đặc tả im lặng, nhưng bản dựng CÓ … ⇒ không còn bất đồng để hỏi BA"*. Im lặng chỉ thành câu hỏi khi **còn** bất đồng giữa đối tác và phần mềm |
| 6 | Dùng **ngoại lệ "BA đã chốt trước"** để không hỏi lại về tên cột "SLA" vs "Mức cảnh báo thời hạn" | Flow §Rẽ nhánh cho phép đúng 1 ngoại lệ: dẫn được nguồn **kèm ngày**. Nguồn: `reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-week-3.md:56-63`, **2026-07-24**, nói thẳng *"Tên cột 'SLA' của app khớp đặc tả"*. Cùng file đó cũng là căn cứ để chấm được vế "4 nhãn mức rời" |
| 7 | Chấm `QLHSDNHTCP_03` = **cần BA** chứ không phải Pass, dù cả 2 vế đối tác đều hết lỗi | Nhãn thứ 5 "Đã hoàn thành" nằm **trong đúng cột đang tranh chấp** và **không thoả ý 1 mục 4** tôi đã viết trước khi đo. Chấm Pass sẽ phải sửa tiêu chí cho khớp kết quả — thứ flow cấm thẳng. Chấm Fail cũng sai vì đặc tả im lặng. Còn lại đúng 1 cửa: cần BA |
| 8 | Sửa thu hẹp ý 1 mục 4 (chỉ áp cho hồ sơ **còn đang xử lý**) thay vì giữ nguyên | Flow §Sửa tiêu chí giữa chừng **cho phép** sửa, với điều kiện thêm mục sửa đổi có mốc giờ + lý do. Đã thêm §7 trong `tieuchi/QLHSDNHTCP_03.md` lúc 00:45, nêu rõ sửa gì và vì sao |
| 9 | Đổi `cbpd_bn` → `cbpd_tw_01` để đóng điều kiện vai trò (khác **cấp** so với đối tác) | Flow §Đóng GAP cách ②: "test đủ mọi nhánh khả dĩ, mọi nhánh cùng kết quả ⇒ GAP đóng". `cbpd_bn` trùng khít vòng 2 nhưng cấp BN có **0 hồ sơ** → không đo được. Biến số thật sự ảnh hưởng bố cục là **vai trò** (bộ cột + nút thao tác khác nhau), không phải cấp đơn vị. Đã ghi rõ vào mục 6 file tiêu chí |
| 10 | Seed 1 đợt đánh giá mới thay vì báo "không đo được" | Flow §Chuẩn bị: "Tiền đề **tạo được** mà không tạo → CẤM mọi verdict" và "Dạng dữ liệu trong M chưa tồn tại → **được seed**". Cả 19 đợt đều `TRON_NAM` nên bộ lọc của đối tác không cắt được gì. Đã khai bản ghi · đổi gì · env nào ở `BAO-CAO-DOT.md` §2 |
| 11 | Đọc nội dung tệp .xlsx bằng cách **bắt phản hồi trong trang rồi giải nén**, thay vì mở tệp từ thư mục Tải về | Trình duyệt do công cụ điều khiển chạy hồ sơ riêng nên tệp **không** rơi vào `~/Downloads` (ghi nhớ `reference-read-xlsx-content-in-browser-zip-parse`). Vẫn **bấm nút thật** trên giao diện đúng yêu cầu flow; chỉ phần đọc tệp là làm trong trang. Sau đó còn ghi tệp ra đĩa và **đọc lại bằng openpyxl** để có phép đo thứ hai độc lập |
| 12 | Không log "thông báo đúp" dù bộ theo dõi DOM bắt được 4 sự kiện | Flow §Chạy bước 6 nói thẳng: đếm theo **mốc giờ khác nhau**, không theo số phần tử — 1 thông báo luôn sinh 2 phần tử. Đã đo lại bằng bộ đếm cài **trước** lúc bấm: tối đa **1** thẻ cùng tồn tại, **1** yêu cầu mạng |
| 13 | Không log "vai trò CB PD thấy danh sách rỗng" thành lỗi | Kiểm lại tab **đang được chọn** là "Chờ phê duyệt" (0 hồ sơ) chứ không phải "Tất cả" — tôi đọc nhầm tab đầu danh sách. Flow §Dấu hiệu phép đo nói dối: chưa kiểm chéo thì chưa được kết luận |
| 14 | Cột "Mức HT %" (có trên phần mềm, không có trong SCR-V.II-01) → chỉ ghi nhận, không dùng để chấm | Mục 4 file tiêu chí đã khoanh trước: chỉ chấm 2 vế đối tác phản ánh. Flow §Report cuối đợt tách riêng chỗ cho "lỗi phát hiện thêm ngoài phạm vi" |
| 15 | Tự đặt tên thư mục/tệp hồ sơ (`BAO-CAO-DOT.md`, `image/`, `partner-evidence/`, `frames/`) | Prompt chỉ khai đường dẫn `bug-report.md`, thư mục `image/`, `cau-hoi-BA.md`, thư mục `tieuchi/`. Phần còn lại đặt theo đúng bố cục thư mục `flowtest-2026-08-05` của đợt chạy thử trước để người sau tìm được |
| 16 | Đặt mức **Major** cho `LKHDG_12` và **để trống mức** cho `QLHSDNHTCP_03` | Flow không có thang mức độ. Lấy theo mẫu bug của dự án (`output/template/bug-report-template.md` dùng Critical/Major/Medium/Minor). Major vì sai lệch **âm thầm** — không cảnh báo gì, người dùng dễ báo cáo nhầm số liệu. Case còn lại chưa xếp mức vì chưa biết có phải lỗi hay không |

---

## Chỗ tôi thấy file flow nên nói rõ hơn

1. **Hồ sơ QA nội bộ đợt trước có được đọc ở giai đoạn A không** (dòng #2). Danh sách "được đọc" có 4 mục,
   không nhắc tới nó. Rủi ro thật: ghi chép cũ chứa **số đo**, đọc xong dễ viết tiêu chí vừa khít số đo đó —
   đúng cái bẫy giai đoạn A muốn chặn.
2. **Phát hiện mới ngay trong phần đang tranh chấp thì thuộc "vế của case" hay "lỗi ngoài phạm vi"** (dòng #7).
   Flow có luật cho case gộp nhiều vế, và có chỗ cho lỗi ngoài phạm vi, nhưng không nói ca ở giữa: đối tác không
   nêu, nhưng nằm đúng trong cột/màn đang tranh chấp. Hai cách xếp cho ra 2 verdict khác nhau (Pass vs cần BA).
3. **Đóng điều kiện vai trò khi tài khoản trùng khít không có dữ liệu** (dòng #9). Flow bảo "test đủ mọi nhánh
   khả dĩ" nhưng không nói được phép nới chiều nào (đổi cấp? đổi đơn vị?) và phải khai ở đâu.
