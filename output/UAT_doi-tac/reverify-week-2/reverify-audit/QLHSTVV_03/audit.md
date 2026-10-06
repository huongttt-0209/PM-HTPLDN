# Audit verify vòng 2 — QLHSTVV_03 (row 58, tab tuần 2)

**Verdict tổng:** `Open, BA confirm` · **Bug ID:** `BUG-QLHSTVV_03` · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện (0 GAP):** [`../../cond/QLHSTVV_03-r2.md`](../../cond/QLHSTVV_03-r2.md)

> 2 trạng thái vì 2 mục đối tác nêu có bản chất khác nhau: "Địa bàn" là trường **đặc tả đã khai tử** (lỗi thật → dev);
> "Số quyết định (công nhận)" là trường **có thật trong đặc tả** nhưng không nằm trong danh sách thành phần màn hình → cần BA chốt nguồn.

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `QLHSTVV_03_v2.jpg` (259.319 byte, ảnh tĩnh 1 khung hình) |
| Chất lượng bằng chứng | **Tốt** — đọc rõ cả nhãn lẫn giá trị của 2 nhóm đang tranh luận, có breadcrumb + vai trò + thời điểm |
| Nội dung thấy trong ảnh | Nhóm "Nghề nghiệp" 12 mục (có **"Số quyết định (công nhận)" = —**) và nhóm "Tổ chức & Mạng lưới" 3 mục (có **"Địa bàn" = —**) |
| Dữ kiện neo | (a) `…/chuyen-gia-tvv/b88271a7-…`; (b) vai trò **CB_NV_TW**, badge "BTP · TW"; (c) 25/07/2026 16:19 |
| Ghi chú | Cả 2 mục đều đang rỗng (`—`) ⇒ chúng **hiện ra không phụ thuộc dữ liệu**, tức là do bố cục màn hình chứ không do bản ghi |

## Verdict từng ý

| # | Ý | Kết quả verify | Verdict ý |
|:-:|---|---|---|
| 1 | Nhóm "Tổ chức" thừa mục **"Địa bàn"** | **Đối tác ĐÚNG về mặt đặc tả.** srs-v3.5 **khai tử** khái niệm địa bàn cho tư vấn viên: `:46` "**bỏ field `dia_ban_ids[]`** và bảng junction TVV_DIA_BAN — Thẻ TVV có hiệu lực **toàn quốc** (NĐ 77/2008 Điều 19)"; `:153` entity dòng 19 gạch ngang `~~dia_ban_ids~~` kèm "**Bỏ field này**". Ảnh của đối tác cho thấy mục này vẫn hiển thị trên màn chi tiết ⇒ trái đặc tả, **có dẫn line rõ, không có khoảng cho BA diễn giải khác**. QA kiểm lại theo đúng các bước thì **không thấy** mục này (6 tổ hợp — xem phép đo) | **`Open`** |
| 2 | Nhóm "Nghề nghiệp" thừa mục **"Số quyết định (công nhận)"** | **Quan sát đúng, nhưng kết luận "thừa" thì chưa chắc.** Trường này **có thật** trong đặc tả: `:583`/`:604` (FR-IV-07 — bắt buộc nhập `so_quyet_dinh` khi phê duyệt), `:616` ERR-PD-05, `:2027` Phụ lục "so_quyet_dinh_cong_nhan — Số QĐ công nhận (FR-IV-07)". Danh sách thành phần thẻ Hồ sơ `:1556` **không liệt kê** nó — nhưng danh sách đó cũng không liệt kê Chuyên ngành / Số QĐ công bố / Ngày QĐ công bố / Mô tả kinh nghiệm, tức là **viết tóm tắt** chứ không phải danh sách đóng. Đây đúng loại bất đồng nguồn đặc tả đã ghi ở DKTGMLTVV_03 | **`BA confirm`** |

## Cổng 3 — đối chiếu SRS vs thực tế web

| SRS yêu cầu (dẫn line) | Thực tế | Đủ/Thiếu |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:46` — "**Ghi chú v3.1 — bỏ TVV_DIA_BAN:** Theo NĐ 77/2008 Điều 19, Thẻ TVV có hiệu lực **toàn quốc** — pháp luật không giới hạn TVV theo địa bàn. Hệ thống **bỏ field `dia_ban_ids[]`** và bảng junction TVV_DIA_BAN"; `:153` — entity dòng 19: `~~dia_ban_ids~~` … "**Bỏ field này**" | Ảnh đối tác: thẻ Hồ sơ nhóm "Tổ chức & Mạng lưới" **có mục "Địa bàn"** | **Thiếu** (mục không được phép tồn tại) |
| `srs-fr-04-chuyen-gia-tvv.md:1556` — SCR-IV-03 thẻ "Hồ sơ", nhóm (b) Nghề nghiệp = "(**chức vụ + nơi công tác** + trình độ, chứng chỉ, số thẻ, kinh nghiệm)" | Web (cả ảnh đối tác lẫn bản QA kiểm) hiển thị nhiều hơn: thêm Chuyên ngành, Số QĐ công bố, Ngày QĐ công bố, Số năm kinh nghiệm, Chứng chỉ chi tiết, Mô tả kinh nghiệm — và trong ảnh đối tác còn có Số quyết định (công nhận) | **Mâu thuẫn nội bộ SRS** — danh sách `:1556` viết tóm tắt, không đóng |
| `srs-fr-04-chuyen-gia-tvv.md:583` + `:604` + `:2027` — `so_quyet_dinh` là trường bắt buộc khi Cán bộ Phê duyệt duyệt hồ sơ, và có trong mẫu xuất Phụ lục 1 ("Số QĐ công nhận") | Trường có dữ liệu thật (`TVV-BTP-TW-0016` → `QĐ-8017/QĐ-BTP`) nhưng bản QA kiểm **không hiển thị** nó ở bất kỳ nhóm nào của thẻ Hồ sơ | **Chưa rõ** — đưa vào câu hỏi BA |
| `srs-fr-04-chuyen-gia-tvv.md:1556` — nhóm (c) Tổ chức = "(tổ chức chính link hoặc 'Tự do', đối tác dạng thẻ)" | Bản QA kiểm: đúng 2 mục Tổ chức chính + Đối tác | **Đủ** |

## Phép đo đã chạy (artifact QUAN SÁT trên data thật)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Đăng nhập `cbnv_tw` (**CB_NV_TW**, badge "BTP · TW" — trùng vai trò trong ảnh đối tác), mở chi tiết `TVV-BTP-TW-0016` (Chờ kích hoạt tài khoản, **đã phê duyệt**), đọc **toàn bộ nhãn** thẻ Hồ sơ bằng DOM | Nhóm Nghề nghiệp **11 mục**, **KHÔNG có** "Số quyết định (công nhận)". Nhóm Tổ chức & Mạng lưới đúng **2 mục** Tổ chức chính + Đối tác, **KHÔNG có** "Địa bàn" | `QLHSTVV_03-r2-the-ho-so-QA-kiem-lai.png` |
| 2 | Kiểm dữ liệu bản ghi trên để loại trừ "ẩn vì rỗng" | Bản ghi **có** số quyết định công nhận thật (`soQuyetDinh = QĐ-8017/QĐ-BTP`) mà màn vẫn không hiển thị mục nào cho nó ⇒ không phải chuyện ẩn khi rỗng | — |
| 3 | Lặp lại với bản ghi khác trạng thái + khác đơn vị: `TVV-STP-AG-0001` (Đang hoạt động, Sở Tư pháp An Giang), xem bằng cả `cbnv_dp` và `cbnv_tw` | Kết quả **giống hệt**: không có "Số quyết định (công nhận)", không có "Địa bàn" | — |
| 4 | Đối chiếu trực tiếp ảnh đối tác vs bản QA kiểm (cùng vai trò CB_NV_TW, cùng màn, cùng thẻ) | Ảnh đối tác **có 2 mục dôi ra**; bản QA kiểm **không có** | `BUG-QLHSTVV_03-the-ho-so-co-muc-dia-ban.jpg` (ảnh đối tác) |
| 5 | Tra đặc tả về "địa bàn" cho tư vấn viên | `:46` và `:153` — field bị **bỏ hẳn** vì thẻ TVV có hiệu lực toàn quốc (NĐ 77/2008 Đ.19). Ngoài ra `:233` nói rõ bộ lọc "địa bàn" ở màn danh sách phải lọc theo **đơn vị công nhận**, không phải theo địa bàn của TVV | — |
| 6 | Tra đặc tả về "số quyết định (công nhận)" | `:583` (FR-IV-07 §Inputs #4, bắt buộc khi phê duyệt) · `:604` (Outputs) · `:616` (ERR-PD-05) · `:2027` (Phụ lục 1 — "Số QĐ công nhận") ⇒ trường **hợp lệ**, chỉ là không có tên trong danh sách thành phần thẻ Hồ sơ | — |

**Vì sao ý 1 vẫn là `Open` dù QA không tái hiện được:** theo QA_VERIFY_PROTOCOL, `Reject` chỉ dùng khi chứng minh được đối tác thao tác/hiểu sai
hoặc báo cáo vô hiệu. Ở đây ảnh của đối tác **đọc rõ ràng** nhãn "Địa bàn" trên đúng màn, đúng vai trò, và đặc tả **cấm** field này tồn tại —
tức là hiện tượng họ chụp được **là lỗi thật**. Việc QA không quan sát lại được chỉ nói lên rằng ở lần kiểm này màn hình không dựng mục đó,
không đủ để kết luận đối tác sai. Chuyển dev kèm cả hai ảnh để dev đối chiếu trên bản build của mình.

**Vì sao ý 2 là `BA confirm` chứ không phải `Open`/`Reject`:** đối tác quan sát đúng (mục đó có trên màn của họ), nhưng "thừa hay không"
phụ thuộc vào việc danh sách `:1556` là **danh sách đóng** hay chỉ là mô tả tóm tắt — đúng loại bất đồng nguồn đặc tả, QA không tự quyết.

## Câu hỏi gửi BA

1. Danh sách thành phần thẻ "Hồ sơ" của màn chi tiết tư vấn viên (`:1556`) là **danh sách đóng** (chỉ được hiển thị đúng các mục liệt kê)
   hay là **mô tả tóm tắt** (được hiển thị thêm các trường khác của hồ sơ)? Hiện web hiển thị thêm 6 mục ngoài danh sách.
2. Nếu là danh sách đóng: **"Số quyết định (công nhận)"** (`so_quyet_dinh`, bắt buộc nhập khi phê duyệt theo `:583`, có trong mẫu xuất Phụ lục 1 `:2027`)
   có được hiển thị trên thẻ Hồ sơ không? Nếu **không**, người dùng tra số quyết định công nhận của một tư vấn viên ở đâu?
   (Bản QA kiểm hiện **không** hiển thị trường này ở bất kỳ nhóm nào, dù dữ liệu có thật.)
3. Xin BA xác nhận lại nguyên tắc "bỏ địa bàn của tư vấn viên" (`:46`, `:153`) vẫn giữ nguyên ở v3.5, để dev gỡ dứt điểm mọi chỗ còn hiển thị.
4. **(bổ sung 27/07 khi kiểm lại số dòng)** Số nhóm chuẩn của thẻ "Hồ sơ" là **6** hay **5**? Kết quả mong đợi của phiếu ghi "hiển thị **5 nhóm**"
   (vòng 1 actual cũng ghi "5 nhóm"), nhưng `:1556` viết rõ **"6 nhóm thu gọn được, chỉ đọc"** — (a) Thông tin cá nhân · (b) Nghề nghiệp ·
   (c) Tổ chức · (d) Lĩnh vực · (e) File đính kèm · **(f) Thông tin công khai — "chỉ hiển thị khi `cong_khai=1`"**.
   Nhóm (f) có điều kiện ⇒ hồ sơ chưa công khai chỉ thấy 5 nhóm, nên nhiều khả năng **không bên nào sai**; cần BA xác nhận
   để hai bên không đếm lệch qua từng vòng.

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- **Không tạo dữ liệu:** toàn bộ phép đo chỉ đọc màn hình, không tạo/sửa bản ghi nào.
- **Liên đới DKTGMLTVV_03 (row 53):** câu hỏi BA số 1 ở đây là **cùng một câu hỏi** với DKTGMLTVV_03 (bộ trường nhóm Nghề nghiệp lấy theo SRS hay theo bản thiết kế màn hình), chỉ khác là ở màn xem thay vì màn nhập. Giữ nguyên hướng trả lời để hai case không đá nhau.
- **Chênh lệch quan sát:** đây là case thứ hai trong đợt mà ảnh/video của đối tác cho thấy thành phần giao diện mà bản QA kiểm không dựng (case trước: CNHSNLTVV_02 ngược lại — QA tái hiện được). Nếu còn lặp lại, cần đặt vấn đề đồng bộ phiên bản triển khai với dev **ở kênh nội bộ**, không nêu trong ghi chú gửi đối tác.
