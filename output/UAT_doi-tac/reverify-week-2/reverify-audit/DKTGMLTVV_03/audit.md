# Audit verify vòng 2 — DKTGMLTVV_03 (row 53, tab tuần 2)

**Verdict tổng:** `Open, BA confirm` · **Bug ID:** `BUG-DKTGMLTVV_03` · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện (0 GAP):** [`../../cond/DKTGMLTVV_03-r2.md`](../../cond/DKTGMLTVV_03-r2.md)

> 2 trạng thái vì case có 2 phần tách bạch: phần đối tác phản ánh cần **BA chốt nguồn đặc tả**; phần QA phát hiện thêm trên cùng form là **lỗi thật, chuyển dev**.

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `DKTGMLTVV_03_v2.jpg` (206.323 byte, ảnh tĩnh 1 khung hình) |
| Nội dung thấy trong ảnh | Nhóm "Nghề nghiệp" của form Thêm mới TVV, hiện 6 trường: Trình độ học vấn * · Chuyên ngành · Chức vụ · Nơi công tác · Số năm kinh nghiệm · Mô tả kinh nghiệm. Vùng nhìn dừng ở "Mô tả kinh nghiệm" |
| Dữ kiện neo | (a) `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/tao-moi` · (b) vai trò NHT, badge "BTP · DP" · (c) 2026-07-25 15:20 |
| **Mâu thuẫn nội tại của chính đối tác** | Vòng 1 case này họ báo nhóm 2 **THIẾU** "Chứng chỉ hành nghề" và "Mô tả kinh nghiệm" → dev đã bổ sung → Verify Pass. Vòng 2 họ báo nhóm 2 **THỪA** trường. Hai phản ánh dựa trên 2 nguồn đặc tả khác nhau |

## Verdict từng ý

| # | Ý | Kết quả verify | Verdict ý |
|:-:|---|---|---|
| 1 | "SRS quy định nhóm 2 chỉ có 3 trường (Trình độ chuyên môn, Chuyên ngành đào tạo, Số năm kinh nghiệm)" | **Tiền đề không khớp srs-v3.5.** SCR-IV-02 nhóm 2 (`:1495-1504`) liệt kê **9 mục**; FR-IV-03 §Inputs (`:296-310`) còn quy định thêm `chuyen_nganh` và `so_nam_kinh_nghiem` là trường **NHT nhập bắt buộc**. Không có chỗ nào trong srs-v3.5 giới hạn nhóm 2 còn 3 trường | **`BA confirm`** |
| 2 | "Hệ thống hiển thị nhiều hơn" (quan sát thực tế) | **Đúng thực tế**: web hiện 11 trường ở nhóm 2, nhiều hơn 9 mục của SCR-IV-02. 2 trường dôi ra là Chuyên ngành + Số năm kinh nghiệm — nhưng cả hai **đều được SRS yêu cầu** ở FR-IV-03 §Inputs (`:304`, `:305`) ⇒ web đúng, bảng thành phần SCR-IV-02 thiếu | **`BA confirm`** |
| 3 | *(QA phát hiện thêm khi bấm Lưu trên form trống — không phải ý đối tác nêu)* | Trường **"Tổ chức hành nghề chính"** bị đặt **bắt buộc** ("Tổ chức chính là bắt buộc"), trong khi SRS nói **tùy chọn** ở 2 nơi: SCR-IV-02 mục 4.1 (`:1506`) "Tùy chọn — tư vấn viên tự do để trống" và FR-IV-03 §Inputs #14 (`:307`) `to_chuc_id \| identifier \| **N**` ⇒ chặn hẳn luồng đăng ký TVV tự do | **`Open`** |

## Cổng 3 — đối chiếu SRS vs thực tế web (loại bug: Hiển thị + Ràng buộc nhập liệu)

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:1495-1504` — SCR-IV-02 nhóm 2 gồm 9 mục: Chức vụ (3.0a) · Nơi công tác (3.0b) · Trình độ * (3.1) · Chứng chỉ hành nghề (3.2) · Bằng cấp chi tiết (3.3) · Chứng chỉ chi tiết (3.4) · Số thẻ hành nghề (3.5) · File thẻ hành nghề (3.6) · Mô tả kinh nghiệm (3.7) | Web có **đủ cả 9**, cộng thêm **Chuyên ngành** và **Số năm kinh nghiệm** = 11 trường | Đủ 9/9, **dôi 2** |
| `srs-fr-04-chuyen-gia-tvv.md:304` + `:305` — FR-IV-03 (UC41, màn hình SCR-IV-02) §Inputs #11 `chuyen_nganh \| text \| **Y** \| NHT nhập`; #12 `so_nam_kinh_nghiem \| number \| **Y** \| NHT nhập`. Củng cố tại `:323`: "Tạo bản ghi TU_VAN_VIEN với đầy đủ các trường nhập (… trinh_do, chuyen_nganh, so_nam_kinh_nghiem, …)" | Web CÓ 2 trường này ⇒ **đúng FR**. Nhưng web để **không bắt buộc**, còn FR ghi Y (bắt buộc) | **Mâu thuẫn nội bộ SRS** (SCR không liệt kê / FR bắt buộc) |
| `srs-fr-04-chuyen-gia-tvv.md:1476` — "Biểu mẫu chia **5 nhóm** thu gọn được: Thông tin cá nhân, Thông tin nghề nghiệp, Tổ chức & Mạng lưới, File đính kèm, Ghi chú" (lặp lại ở `:1467`) | Web có **6 nhóm** — thêm nhóm **"Quyết định công bố"** (Số QĐ công bố, Ngày QĐ công bố). 2 trường này có trong entity TU_VAN_VIEN (`:155`, `:156`) và trong mẫu xuất Phụ lục 1 (`:2212`, `:2213`) | **Mâu thuẫn nội bộ SRS** |
| `srs-fr-04-chuyen-gia-tvv.md:1506` — SCR-IV-02 mục 4.1: "Tổ chức chính \| dropdown có tìm kiếm \| **Tùy chọn — tư vấn viên tự do để trống**" · `:307` — FR-IV-03 §Inputs #14: `to_chuc_id \| identifier \| **N**` | Bấm Lưu trên form trống → web báo **"Tổ chức chính là bắt buộc"** ⇒ không thể đăng ký tư vấn viên tự do | **Thiếu** |

## Phép đo đã chạy (artifact QUAN SÁT trên data thật)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Mở `/chuyen-gia-tvv/tao-moi` bằng NHT (badge "BTP · DP"), mở hết nhóm thu gọn, đọc **toàn bộ nhãn theo nhóm** bằng DOM | **6 nhóm**. Nhóm 2 "Nghề nghiệp" có **11 trường**: Trình độ học vấn * · Chuyên ngành · Chức vụ · Nơi công tác · Số năm kinh nghiệm · Mô tả kinh nghiệm · Chứng chỉ hành nghề · Số thẻ hành nghề · File thẻ hành nghề (PDF) · Bằng cấp chi tiết · Chứng chỉ chi tiết | `DKTGMLTVV_03-r2-nhom2-nghe-nghiep-phan-duoi.png` |
| 2 | Liệt kê nhóm 3 (không có trong ảnh đối tác) | Nhóm **"Quyết định công bố"**: Số QĐ công bố · Ngày QĐ công bố — nhóm này không nằm trong danh sách 5 nhóm của SRS `:1476` | `BUG-DKTGMLTVV_03-to-chuc-chinh-bat-buoc.png` (phần trên ảnh) |
| 3 | **Bấm Lưu trên form TRỐNG** để đọc đúng bộ ràng buộc bắt buộc mà web đang áp (không tạo bản ghi nào) | **10 trường báo lỗi bắt buộc**: Họ tên · Ngày sinh · Giới tính · Số CMND/CCCD · Email · Số điện thoại · Địa chỉ · Trình độ học vấn · **Tổ chức hành nghề chính** · Lĩnh vực pháp luật | `BUG-DKTGMLTVV_03-to-chuc-chinh-bat-buoc.png` |
| 4 | Đọc nguyên văn thông báo của trường Tổ chức | `"Tổ chức chính là bắt buộc"` — mâu thuẫn trực tiếp với `:1506` "Tùy chọn — tư vấn viên tự do để trống" | như trên |
| 5 | Đối chiếu chiều ngược lại: Chuyên ngành + Số năm kinh nghiệm có bị bắt buộc không | **Không** báo lỗi khi để trống ⇒ web coi là tùy chọn, còn FR-IV-03 `:304`/`:305` ghi **Y** | — |

**Vì sao ý 1-2 KHÔNG phải `Reject`:** đối tác quan sát đúng thực tế (web đúng là hiện nhiều trường hơn tài liệu họ cầm).
Bất đồng ở đây là **nguồn đặc tả** — họ đối chiếu bản thiết kế màn hình, QA đối chiếu srs-v3.5. Theo QA_VERIFY_PROTOCOL §Verdict,
"bất đồng kỳ vọng vs SRS (dù web đúng SRS)" → `BA confirm`, **cấm** `Reject`.

**Vì sao ý 3 là `Open` chứ không phải `BA confirm`:** SRS nêu **rõ ràng và nhất quán ở 2 chỗ** rằng trường này tùy chọn, còn web bắt buộc —
đúng định nghĩa `Open` ("actual sai rule SRS, dẫn line rõ" + "hệ thống chặn luồng hợp lệ dù đủ điều kiện"), không có chỗ nào để BA diễn giải khác.

## Ngoài tiêu chí BA — có thấy gì bất thường không?

**Có, đã gộp vào ý 3 và vào câu hỏi BA:**
- Chiều ngược lại của ý 3: FR-IV-03 ghi `chuyen_nganh` và `so_nam_kinh_nghiem` là **bắt buộc (Y)** nhưng web để tùy chọn. Không log thành bug riêng vì
  bảng thành phần màn hình SCR-IV-02 lại không hề liệt kê 2 trường này — tức SRS tự mâu thuẫn, phải để BA chốt trước rồi mới kết luận web đúng/sai.
- Nhóm "Quyết định công bố" nằm ngoài danh sách 5 nhóm của `:1476` nhưng có đủ căn cứ entity + mẫu xuất Phụ lục 1 ⇒ nhiều khả năng SRS thiếu cập nhật, không phải web sai. Đưa vào câu hỏi BA.

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- **Không tạo dữ liệu:** phép đo 3 bấm Lưu trên form TRỐNG nên toàn bộ dừng ở kiểm tra phía giao diện, không có request tạo bản ghi, không phát sinh TVV rác.
- **Liên đới case 8 (QLHSTVV_03, row 58):** đối tác cũng phản ánh "thẻ Hồ sơ thừa trường Số quyết định (công nhận)" — cùng gốc với nhóm "Quyết định công bố" ở đây.
  Khi verify case 8 cần dùng lại kết luận này để tránh trả lời lệch nhau.
- **Bản thiết kế đối tác dẫn:** vòng 1 của case DKTGMLTVV_02 đã ghi nhận bản thiết kế **HTPLDN-041** lệch SRS và BA đã chốt 15/07/2026 theo hướng "SRS > bản thiết kế".
  Câu hỏi BA lần này là mở rộng của đúng vấn đề đó sang bộ trường nhóm 2.
