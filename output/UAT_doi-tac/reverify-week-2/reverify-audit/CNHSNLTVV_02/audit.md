# Audit verify vòng 2 — CNHSNLTVV_02 (row 56, tab tuần 2)

**Verdict tổng:** `Open` · **Bug ID:** `BUG-CNHSNLTVV_02` (nội dung vòng 2) · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện:** [`../../cond/CNHSNLTVV_02-r2.md`](../../cond/CNHSNLTVV_02-r2.md)

> Verdict `Open` theo QA_VERIFY_PROTOCOL §87 (đa ý → tổng là `Open` nếu ≥1 ý Open).
> Ý (b) của đối tác **không tái hiện**, nhưng video của họ ghi được một lỗi **nặng hơn** trên đúng màn đó, và QA đã tái hiện lại được.

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `CNHSNLTVV_02_v2.webm` — 2.031.568 byte, dài ~8,2 giây |
| Trích khung hình | `tools/extract_frames.py … --every 1` → 11 khung (`t000.00s` … `t008.19s`); trích dày thêm 0,25 s đoạn 6,0–8,3 s để bắt thời điểm chuyển màn |
| Diễn biến | Chương trình đào tạo → menu "Tư vấn viên / Chuyên gia" → danh sách tab "Mới đăng ký" (3 bản ghi) → mở chi tiết `TVV-STP-HN-0004 — NHT TKM` (t≈6,1 s, màn chi tiết render đủ) → **t≈6,3 s tự nhảy `/403`** (`ERR-PERM-SYS-00-01`, "Vai trò hiện tại: NHT") → giữ nguyên tới hết video |
| Dữ kiện neo | (a) `htpldn-uat.ospgroup.vn`; (b) vai trò **NHT**, header "BTP · DP · hương 3 NHT"; (c) 25/07/2026 16:01 |
| **Khoảng trống của bằng chứng** | Video **không** tới form "Cập nhật năng lực" ⇒ **không** chứa hình ảnh của ý (a) và (b). Nhưng nó chứa **nguyên nhân**: vai trò NHT bị đẩy khỏi màn chi tiết |

## Verdict từng ý

| # | Ý | Kết quả verify | Verdict ý |
|:-:|---|---|---|
| 1 | "Trường Mô tả kinh nghiệm không hiển thị giá trị hiện tại mặc dù tồn tại dữ liệu" | **KHÔNG tái hiện.** Nạp dữ liệu mới rồi mở lại form: ô "Mô tả kinh nghiệm" nạp đúng giá trị đang lưu. Đúng với **cả hai** đường ghi (lưu từ form Năng lực, lưu từ màn Sửa hồ sơ) — xem phép đo 5→8 | Không phải lỗi (không Reject — xem cuối trang) |
| 2 | "Màn hình chi tiết hiển thị các trường thông tin không giống với màn hình cập nhật" | **Đúng một phần.** Thẻ "Năng lực" hiển thị mục **"Tóm tắt năng lực"** nhưng form cập nhật **không có** ô tương ứng ⇒ mục này vĩnh viễn "—", không ai nhập được. Ngoài ra 3 mục đổi tên giữa 2 chế độ ("Kinh nghiệm"↔"Mô tả kinh nghiệm", "Bằng cấp"↔"Bằng cấp chi tiết", "Chứng chỉ"↔"Chứng chỉ chi tiết") | `Open` (gộp vào bug) |
| 3 | *(QA tái hiện từ chính video của đối tác)* | Vai trò **NHT — đúng tác nhân mà đặc tả giao cho chức năng "Cập nhật năng lực"** — mở chi tiết tư vấn viên **cùng đơn vị** thì bị đẩy sang `/403`. Vai trò duy nhất còn mở được màn (CB Nghiệp vụ) thì **bị từ chối khi bấm Lưu**. ⇒ Chức năng FR-IV-04 hiện **không vai trò nào dùng được qua giao diện** | **`Open`** |

## Cổng 3 — đối chiếu SRS vs thực tế web

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:368` — FR-IV-04 **Màn hình: SCR-IV-03 (Tab Năng lực)**; `:372` **Tác nhân: Người hỗ trợ pháp lý (NHT)**; `:374` Preconditions "TVV cùng đơn vị với NHT"; `:429` Acceptance "Given NHT xem chi tiết TVV cùng đơn vị **When** nhấn 'Cập nhật năng lực' **Then** form inline edit mở" | NHT mở chi tiết TVV **cùng đơn vị** → trang tự chuyển `/403`, không bao giờ thấy thẻ Năng lực | **Thiếu** |
| `srs-fr-04-chuyen-gia-tvv.md:1572` — SCR-IV-03 thẻ "Đánh giá ({N})", cột *Điều kiện hiển thị* = **"Luôn"** (không giới hạn vai trò) | Lời gọi lấy số đếm đánh giá của màn chi tiết bị từ chối khi vai trò là NHT → kéo theo cả trang bị đẩy sang `/403` | **Thiếu** |
| `srs-fr-04-chuyen-gia-tvv.md:1568` — SCR-IV-03 thẻ "Năng lực": nội dung = **"Bằng cấp chi tiết, Chứng chỉ chi tiết, Kinh nghiệm chi tiết"** + nút "Cập nhật năng lực" → form sửa nhanh | Thẻ hiển thị thêm mục **"Tóm tắt năng lực"** không có trong danh sách này và **không có** ô nhập tương ứng ở form ⇒ luôn "—" | **Thiếu** (mục thừa, không nhập được) |
| `srs-fr-04-chuyen-gia-tvv.md:422` — bảng mã lỗi FR-IV-04: **ERR-NL-01 = "NHT không cùng đơn vị với TVV"**, thông báo "Bạn không có quyền cập nhật hồ sơ tư vấn viên này (khác đơn vị)" | Web trả **ERR-NL-01** kèm nội dung **"Chỉ Người hỗ trợ pháp lý mới được cập nhật hồ sơ năng lực"** — khác hẳn nghĩa mà đặc tả gán cho mã này | **Sai lệch** (ghi kèm trong bug, không tách bug riêng) |
| `srs-fr-04-chuyen-gia-tvv.md:376-390` — FR-IV-04 §Inputs: 11 trường (trinh_do, so_nam_kinh_nghiem, chuyen_nganh, bang_cap_chi_tiet, chung_chi_chi_tiet, chung_chi_moi, so_the_hanh_nghe, file_the_hanh_nghe, linh_vuc_ids, mo_ta_kinh_nghiem, ghi_chu_cap_nhat) | Form có **11 ô**: Trình độ · Số năm kinh nghiệm · Mô tả kinh nghiệm · Chuyên ngành · Số thẻ hành nghề · Bằng cấp chi tiết · Chứng chỉ chi tiết · Lĩnh vực pháp luật · Chứng chỉ hiện có · Thêm chứng chỉ mới (PDF) · Ghi chú cập nhật | **Đủ** — bug vòng 1 (form chỉ 6 ô) đã được sửa thật |

## Phép đo đã chạy (artifact QUAN SÁT trên data thật)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Đăng nhập `nht_qa_01` (NHT) → mở danh sách Tư vấn viên | Thấy **2** tư vấn viên, đều thuộc Sở Tư pháp An Giang | — |
| 2 | Đối chiếu đơn vị: `donViId` của NHT vs của TVV `TVV-STP-AG-0001` | **Trùng khít** `…8002-000000000006` ⇒ **cùng đơn vị**, đúng precondition `:374` | — |
| 3 | NHT bấm mở chi tiết TVV cùng đơn vị | Màn chi tiết chớp hiện rồi trang tự chuyển **`/403` — `ERR-PERM-SYS-00-01` — "Vai trò hiện tại: NHT"** (giống hệt video đối tác) | `BUG-CNHSNLTVV_02-nht-mo-chi-tiet-bi-403.png` |
| 4 | Đọc nhật ký mạng của lần mở đó | `…/tu-van-viens/{id}` **200** · `…/lich-su-ho-tro` **200** · `…/danh-gia?page=1&pageSize=1` **403 `ERR-PERM-SYS-00-01`** → ngay sau đó tải `/403`. Cùng bản ghi, đăng nhập **CB Nghiệp vụ** thì `…/danh-gia` trả **200** ⇒ chặn theo **vai trò**, không theo trạng thái hồ sơ | — |
| 5 | CB Nghiệp vụ cùng đơn vị mở chi tiết → thẻ Năng lực → "Cập nhật năng lực" | Form mở được, **11 ô**; ô "Mô tả kinh nghiệm" trống — nhưng lúc này dữ liệu đang lưu **thật sự rỗng** ⇒ trống là **đúng** | — |
| 6 | Bấm Lưu trên form (bộ đo thông báo tự kiểm: `soObserverDangSong = 1`) | **1 request** `PATCH …/nang-luc` · **1 thông báo**: "Chỉ Người hỗ trợ pháp lý mới được cập nhật hồ sơ năng lực". Gọi thẳng cùng thao tác: **403**, `ERR-NL-01` | `BUG-CNHSNLTVV_02-cbnv-luu-nang-luc-bi-tu-choi.png` |
| 7 | **Nạp dữ liệu MỚI** cho đúng trường (bằng vai trò NHT — vai trò duy nhất được phép lưu năng lực) rồi đọc lại | Lưu **thành công**; đọc lại thấy đúng nội dung vừa nhập ⇒ trường này **có** lưu được | — |
| 8 | Mở lại form "Cập nhật năng lực" trên dữ liệu mới | Ô "Mô tả kinh nghiệm" **nạp đúng** giá trị đang lưu. Làm lại lần 2 với dữ liệu ghi từ **màn Sửa hồ sơ** (đường ghi khác): thẻ Hồ sơ, thẻ Năng lực và form **cùng hiển thị một giá trị** ⇒ ý (b) **không tái hiện ở cả hai đường ghi** | `CNHSNLTVV_02-r2-form-cap-nhat-mo-ta-da-nap.png` |
| 9 | Liệt kê nhãn 3 chế độ của cùng bản ghi | **Thẻ Hồ sơ** (nhóm Nghề nghiệp): Trình độ · Chuyên ngành · Chức vụ · Nơi công tác · Số thẻ hành nghề · Số QĐ công bố · Ngày QĐ công bố · Số năm kinh nghiệm · Chứng chỉ hành nghề · Chứng chỉ chi tiết · Mô tả kinh nghiệm. **Thẻ Năng lực**: Tóm tắt năng lực · Trình độ · Số năm kinh nghiệm · Bằng cấp · Chứng chỉ · Số thẻ hành nghề · Kinh nghiệm · Chuyên ngành · Lĩnh vực pháp luật. **Form cập nhật**: 11 ô (xem Cổng 3). ⇒ "Tóm tắt năng lực" chỉ có ở chế độ xem, không có ô nhập | `CNHSNLTVV_02-r2-tab-nang-luc-xem.png` |

**Vì sao ý 1 KHÔNG phải `Reject`:** theo QA_VERIFY_PROTOCOL, `Reject` chỉ dùng khi chứng minh được đối tác thao tác/hiểu sai hoặc báo cáo vô hiệu.
Ở đây bằng chứng của đối tác **có ghi được một lỗi thật** (bị đẩy sang `/403` trên đúng màn họ phản ánh), và QA đã tái hiện lỗi đó.
Việc ô "Mô tả kinh nghiệm" trống nhiều khả năng là do bản ghi họ mở **chưa có dữ liệu ở trường này** — không đủ căn cứ để kết luận họ sai, nên không Reject.

**Vì sao verdict tổng là `Open`:** ý 3 (và một phần ý 2) sai rule SRS có dẫn line rõ, đồng thời hệ thống **chặn hẳn một luồng hợp lệ**
(NHT không thao tác được chức năng mà `:372` giao cho chính vai trò này) — đúng định nghĩa `Open`.

## Ngoài tiêu chí BA — có thấy gì bất thường không?

**Có, đã gộp vào bug:**
- Mã lỗi `ERR-NL-01` bị dùng cho một tình huống khác nghĩa với `:422` (đặc tả gán mã này cho "khác đơn vị"). Không tách bug riêng vì cùng gốc với ý 3, sửa ý 3 sẽ đụng chỗ này.
- Không log thành bug riêng: bảng "Quyền truy cập" của SCR-IV-03 (`:1530-1533`) **không liệt kê NHT**, trong khi `:368`/`:372`/`:429` bắt buộc NHT phải vào được thẻ Năng lực của chính màn này — đặc tả tự lệch. Đã diễn đạt bug theo **yêu cầu nghiệp vụ** ("NHT phải thao tác được chức năng cập nhật năng lực") để dev tự chọn cách sửa, không quy định phải mở/đóng quyền ở đâu.

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- **Dữ liệu để lại:** bản ghi `TVV-STP-AG-0001` (do QA tạo 12/07) nay có "Mô tả kinh nghiệm" / "Số năm kinh nghiệm" / "Chuyên ngành" mang nhãn "QA verify R2 (27/07)". Đây là bản ghi QA, không phải dữ liệu đối tác. Hai đường ghi đã được đưa về **cùng một giá trị** trước khi kết thúc.
- **Phòng bug ma:** lần đo đầu tiên tôi gửi sai tên trường nên tưởng "hệ thống không lưu Mô tả kinh nghiệm". Tra lại mô tả API mới thấy trường đúng tên khác → đo lại thì lưu bình thường. **Đã loại** giả thuyết sai này, không đưa vào bug.
- **Liên đới case 8 (QLHSTVV_03):** danh sách nhãn thẻ Hồ sơ ở phép đo 9 dùng lại được cho case 8 (thừa "Số QĐ công bố" / "Ngày QĐ công bố") — giữ kết luận thống nhất với audit DKTGMLTVV_03.
