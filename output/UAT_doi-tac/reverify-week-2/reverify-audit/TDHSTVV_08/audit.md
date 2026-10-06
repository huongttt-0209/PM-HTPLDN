# Audit verify vòng 2 — TDHSTVV_08 (row 64, tab tuần 2)

**Verdict tổng:** `Open` · **Bug ID:** `BUG-TDHSTVV_08` · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện (0 GAP):** [`../../cond/TDHSTVV_08-r2.md`](../../cond/TDHSTVV_08-r2.md)

> Đối tác nêu 2 ý gộp trong 1 câu. Ý "đổi trạng thái sang Đang thẩm định" **đúng đặc tả cấm** → `Open`.
> Ý "không lưu nháp" thì chính video của đối tác lại cho thấy nội dung nháp **có được lưu** → không phải lỗi.
> Ngoài ra QA phát hiện 3 sai lệch máy trạng thái khác trên cùng màn, gộp vào cùng bug.

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `TDHSTVV_08_v2.webm` — video 57 giây |
| Chất lượng bằng chứng | **Tốt** — đọc rõ nút được bấm, chữ trong hộp thông báo, badge trạng thái trước/sau, và số đếm tab danh sách |
| Nút được bấm | t≈21,0 s + t≈21,7 s: con trỏ **nằm đúng trên nút "Lưu nháp"**, nút có viền tiêu điểm. Không khung nào cho thấy con trỏ chạm "Gửi KQ"/"Trình duyệt" |
| Kết quả quan sát được | t≈22,7 s hộp thông báo **"Đã lưu kết quả thẩm định"** → t≈36 s tab "Mới đăng ký" từ **27 → 26** bản ghi → t≈48 s chi tiết `TVV-BTP-TW-0058` hiển thị **"Đang thẩm định"** |
| Dữ kiện neo | (a) `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/39f6910f-…`; (b) vai trò **CB_NV_TW**, badge "BTP · TW"; (c) 25/07/2026 16:58–16:59 |
| Ghi chú | t≈54 s: mở lại thẻ Thẩm định, dữ liệu đã nhập (Nhóm 1, Kết luận Pháp lý "Đạt", điểm 3, nhận xét "tốt") **vẫn còn** ⇒ phần "lưu" hoạt động |

## Verdict từng ý

| # | Ý | Kết quả verify | Verdict ý |
|:-:|---|---|---|
| 1 | Bấm "Lưu nháp" nhưng hệ thống **đổi trạng thái sang "Đang thẩm định"** | **Đối tác ĐÚNG về mặt đặc tả.** `srs-fr-04-chuyen-gia-tvv.md:1565` quy định nút "Lưu nháp" = "Lưu kết quả thẩm định tạm, **không chuyển trạng thái**". Video cho thấy đúng nút "Lưu nháp" được bấm và trạng thái đổi từ "Mới đăng ký" → "Đang thẩm định" (đối chiếu chéo bằng số đếm tab danh sách 27→26). Đây là **cấm rõ ràng trong đặc tả**, không có khoảng cho diễn giải khác. QA chạy lại đúng kịch bản trên 2 bản ghi thì **không tái hiện** — trạng thái giữ nguyên "Mới đăng ký" | **`Open`** |
| 2 | "Hệ thống **không lưu nháp**" | **Không chính xác.** Chính video của đối tác (t≈54 s) cho thấy sau khi rời màn và quay lại, toàn bộ nội dung nháp vẫn còn. Bản QA kiểm cũng lưu và nạp lại đúng. Không log thành lỗi | **Không phải lỗi** |
| 3 | *(QA phát hiện thêm)* Màn chi tiết ở trạng thái "Mới đăng ký" **không có nút "Bắt đầu thẩm định"** | `:1545` quy định nút "Bắt đầu thẩm định" hiển thị khi vai trò = Cán bộ Nghiệp vụ cùng đơn vị **và** trạng thái ∈ {Mới đăng ký, Chờ thẩm định}, bấm vào thì ngầm chuyển sang "Đang thẩm định". Thực tế màn chỉ có "Quay lại danh sách" + "Sửa hồ sơ" | **`Open`** (gộp bug) |
| 4 | *(QA phát hiện thêm)* Thẻ **"Thẩm định" hiển thị ngay khi hồ sơ còn "Mới đăng ký"** | `:1557` quy định thẻ Thẩm định chỉ hiển thị khi trạng thái ∈ {Đang thẩm định, Chờ phê duyệt} | **`Open`** (gộp bug) |
| 5 | *(QA phát hiện thêm)* Bấm **"Gửi KQ"** với kết luận "ĐẠT" thì hồ sơ **nhảy thẳng "Mới đăng ký" → "Chờ phê duyệt"**, thông báo "Đã trình hồ sơ lên cấp phê duyệt" | `:1566` quy định "Gửi kết quả" chỉ đổi trạng thái khi kết luận là "Yêu cầu bổ sung" hoặc "Không đạt"; `:1581` nói rõ nếu "Đạt" thì chỉ **bật nút "Trình phê duyệt"**; `:1567` mới là nút đặt trạng thái "Chờ phê duyệt". Thực tế 2 nút bị gộp làm 1 và hồ sơ **không bao giờ đi qua "Đang thẩm định"** | **`Open`** (gộp bug) |

## Cổng 3 — đối chiếu SRS vs thực tế web

| SRS yêu cầu (dẫn line) | Thực tế | Đủ/Thiếu |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:1565` — SCR-IV-03 dòng 20b, nút **Lưu nháp**: "Lưu kết quả thẩm định tạm, **không chuyển trạng thái**" | **Bản đối tác:** bấm Lưu nháp → trạng thái đổi Mới đăng ký → Đang thẩm định. **Bản QA kiểm:** trạng thái giữ nguyên `MOI_DANG_KY` (phiên bản 1→2), thông báo "Đã lưu nháp kết quả thẩm định" | **Thiếu** (trên bản đối tác) |
| `srs-fr-04-chuyen-gia-tvv.md:1545` — SCR-IV-03 dòng 6, nút **Bắt đầu thẩm định**: "Click → ngầm chuyển trạng thái Mới đăng ký/Chờ thẩm định → Đang thẩm định + chuyển sang tab Thẩm định"; điều kiện hiển thị: vai trò = Cán bộ Nghiệp vụ cùng đơn vị, trạng thái ∈ {Mới đăng ký, Chờ thẩm định} | Màn chi tiết ở trạng thái "Mới đăng ký", vai trò CB_NV_TW cùng đơn vị: danh sách nút chỉ có `["Quay lại danh sách","Sửa hồ sơ"]` — **không có** nút "Bắt đầu thẩm định" | **Thiếu** |
| `srs-fr-04-chuyen-gia-tvv.md:1557` — SCR-IV-03 dòng 13, thẻ **Thẩm định**: "Hiển thị khi … trạng thái ∈ {Đang thẩm định, Chờ phê duyệt}" | Thẻ Thẩm định hiển thị và thao tác được ngay khi hồ sơ còn **"Mới đăng ký"** | **Thiếu** |
| `srs-fr-04-chuyen-gia-tvv.md:1566` — dòng 20c, nút **Gửi kết quả**: "nếu 'Yêu cầu bổ sung' → Yêu cầu bổ sung; nếu 'Không đạt' → Đã từ chối" (không nêu chuyển trạng thái khi "Đạt") + `:1581` "nếu 'Đạt' → **bật nút 'Trình phê duyệt'**" + `:1567` dòng 20d, nút **Trình phê duyệt**: "Click → MD-TRINH-DUYET → **đặt trạng thái Chờ phê duyệt**" | Bấm "Gửi KQ" với kết luận ĐẠT: trạng thái nhảy thẳng `MOI_DANG_KY` → `CHO_PHE_DUYET` (phiên bản 2→3), thông báo "Đã trình hồ sơ lên cấp phê duyệt". Không có hộp thoại xác nhận MD-TRINH-DUYET | **Thiếu** |
| `srs-fr-04-chuyen-gia-tvv.md:2283`–`:2286` + `:2321`–`:2324` — máy trạng thái SM-TVV: `CHO_THAM_DINH → DANG_THAM_DINH → CHO_PHE_DUYET` | Bản ghi đi thẳng `MOI_DANG_KY → CHO_PHE_DUYET`, **không bao giờ** ở `DANG_THAM_DINH` | **Thiếu** |
| `srs-fr-04-chuyen-gia-tvv.md:1565` (dòng 20b, điều kiện hiển thị chỉ ghi "Tab Thẩm định") vs `:1566` (dòng 20c ghi rõ "Tab Thẩm định, **kết luận đã chọn**") | "Lưu nháp" bị chặn khi chưa chọn Kết luận Pháp lý / Kết luận thẩm định (biểu mẫu báo "Vui lòng chọn kết quả pháp lý", "Vui lòng chọn kết luận"), tức áp cùng điều kiện với "Gửi KQ" | **Thiếu** (ý phụ, mức Nhẹ) |

## Phép đo đã chạy (artifact QUAN SÁT trên data thật)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Trích khung video đối tác, thêm dải 0,5 s/khung cho đoạn 20–30 s để xác định **nút nào được bấm** | t≈21,0 s và t≈21,7 s con trỏ nằm đúng trên nút "Lưu nháp", nút hiện viền tiêu điểm | `frames-fine/t021.03s.jpg`, `frames-fine/t021.68s.jpg` |
| 2 | Đọc chữ trong hộp thông báo + badge trạng thái sau đó | t≈22,7 s "Đã lưu kết quả thẩm định"; t≈48 s badge "Đang thẩm định"; t≈36 s tab "Mới đăng ký" 27 → 26 | `frames-fine/t022.71s.jpg`, `frames/t048.85s.jpg`, `frames/t036.78s.jpg` |
| 3 | Tạo bản ghi sạch `TVV-BTP-TW-0019` (`MOI_DANG_KY`, phiên bản 1), mở màn chi tiết bằng `cbnv_tw` | Danh sách nút = `["Quay lại danh sách","Sửa hồ sơ"]` — **không có "Bắt đầu thẩm định"**; danh sách thẻ = `["Hồ sơ","Thẩm định","Năng lực","Lịch sử hỗ trợ (0)","Đánh giá (0)"]` — **thẻ Thẩm định hiện ngay ở "Mới đăng ký"** | `TDHSTVV_08-r2-luu-nhap-giu-nguyen-trang-thai.png` |
| 4 | Bấm "Lưu nháp" khi chưa chọn kết luận | Biểu mẫu chặn: `["Vui lòng chọn kết quả pháp lý","Vui lòng chọn kết luận"]`, **0 lời gọi** rời trình duyệt, trạng thái không đổi | — |
| 5 | Chọn Kết luận Pháp lý "Đạt" + Kết luận thẩm định "ĐẠT" + nhận xét, bấm **"Lưu nháp"** (bản ghi `TVV-BTP-TW-0019`) | `POST …/tham-dinh` → 200; trạng thái **`MOI_DANG_KY` → `MOI_DANG_KY`** (phiên bản 1 → 2); thông báo **"Đã lưu nháp kết quả thẩm định"** | — |
| 6 | Tải lại trang, mở lại thẻ Thẩm định | Nội dung nháp nạp lại đầy đủ; badge vẫn **"Mới đăng ký"** | `TDHSTVV_08-r2-luu-nhap-giu-nguyen-trang-thai.png` |
| 7 | **Lặp lại với bộ dữ liệu y hệt video đối tác** trên bản ghi thứ hai `TVV-BTP-TW-0020` (Nhóm 1 đủ + Pháp lý "Đạt", Nhóm 2 điểm 3 + "tốt", Nhóm 3 "tốt", Nhóm 4 tích, Kết luận "ĐẠT") | Kết quả **giống hệt**: `POST …/tham-dinh` 200, trạng thái giữ `MOI_DANG_KY` (phiên bản 1 → 2), thông báo "Đã lưu nháp kết quả thẩm định" | — |
| 8 | Bấm **"Gửi KQ"** với kết luận "ĐẠT" (bản ghi `TVV-BTP-TW-0019`) | Trạng thái **`MOI_DANG_KY` → `CHO_PHE_DUYET`** (phiên bản 2 → 3), thông báo "Đã trình hồ sơ lên cấp phê duyệt", **không** qua `DANG_THAM_DINH`, **không** có hộp thoại xác nhận | `TDHSTVV_08-r2-gui-kq-nhay-thang-cho-phe-duyet.png` |
| 9 | **Phòng bug ma — kiểm hộp thông báo có bị nhân đôi không.** Bộ bắt ghi 2 lần cùng một câu chữ, nên đếm số hộp đang sống trong trang mỗi 200 ms suốt 2,4 s | Số hộp cùng lúc **luôn = 1** ⇒ chỉ 1 hộp thông báo thật, 2 lần ghi là do khung chứa bị gắn lại. **Đã loại giả thuyết "thông báo nhân đôi"** | — |

## Vì sao ý 1 vẫn là `Open` dù QA không tái hiện

Theo QA_VERIFY_PROTOCOL, `Reject` chỉ dùng khi chứng minh được đối tác thao tác/hiểu sai hoặc báo cáo vô hiệu. Ở đây:
- Video xác định được **đúng nút "Lưu nháp"** (2 khung liên tiếp, nút có viền tiêu điểm) — không phải bấm nhầm "Gửi KQ".
- Trạng thái đổi được **kiểm chéo bằng 2 nguồn độc lập trong cùng video**: badge ở màn chi tiết và số đếm tab danh sách 27 → 26.
- Đặc tả `:1565` **cấm rõ** việc chuyển trạng thái ở nút này.

⇒ hiện tượng đối tác ghi lại là lỗi thật. Việc bản QA kiểm không dựng lại được chỉ nói lên rằng ở lần kiểm này nút hoạt động đúng, không đủ để kết luận đối tác sai.
Thêm nữa, QA kiểm chính màn đó thì phát hiện **3 sai lệch máy trạng thái khác** (ý 3, 4, 5) — cùng một gốc: luồng "Mới đăng ký → Đang thẩm định → Chờ phê duyệt" chưa được dựng đúng. Vì vậy chuyển dev là hợp lý cả khi bỏ qua chênh lệch quan sát.

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- **Dữ liệu QA tạo:** `TVV-BTP-TW-0019` (`6e8a996a-434a-4ece-9a3a-aeaae715cc1d`, hiện `CHO_PHE_DUYET`) và `TVV-BTP-TW-0020` (`de22ef5c-5358-418a-a0e4-ca4d06c37393`, hiện `MOI_DANG_KY` có nháp). Không đụng bản ghi nào của đối tác.
- **Chênh lệch bản triển khai:** chữ trong hộp thông báo khác nhau — bản đối tác "Đã lưu kết quả thẩm định", bản QA kiểm "Đã lưu **nháp** kết quả thẩm định". Đây là dấu hiệu 2 bản dựng khác nhau (nhiều khả năng dev đã sửa đúng chỗ này sau khi đối tác quay video). Đây là case thứ ba trong đợt có chênh lệch bản dựng (trước đó: QLHSTVV_03, CNHSNLTVV_02) → nên đặt vấn đề đồng bộ phiên bản triển khai với dev **ở kênh nội bộ**, không nêu trong ghi chú gửi đối tác.
- **Nhiễu môi trường:** phiên đăng nhập bị thu hồi 3 lần giữa chừng (văng về `/login`), phải đăng nhập lại. Không ảnh hưởng kết quả đo vì mỗi phép đo đều đọc lại trạng thái bản ghi ngay trước và ngay sau thao tác.
- **Ý phụ mức Nhẹ (dòng cuối Cổng 3):** "Lưu nháp" đòi chọn kết luận trước mới cho lưu. Đặc tả không ghi điều kiện đó cho dòng 20b (chỉ ghi cho 20c), nhưng cũng không nói rõ các trường là tùy chọn khi lưu nháp → đưa vào bug ở mức ghi nhận, không đẩy severity.
