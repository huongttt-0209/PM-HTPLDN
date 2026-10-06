# NHSYC_OOS_01 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 131 · Verdict Verify 2: `Pass`
> **Bug gốc:** trên màn "Thêm mới Hồ sơ Vụ việc", **một** lần bấm [Lưu & Tiếp nhận] rơi vào nhánh lỗi thì hệ thống hiện
> **HAI** khung thông báo cùng lúc với hai câu chữ khác nhau — *"Lỗi hệ thống, vui lòng thử lại sau."* và *"Có lỗi xảy
> ra. Vui lòng thử lại sau."* — trong khi chỉ có **một** lần gửi dữ liệu lên máy chủ. Tái hiện 3/3 lần trên bản V1.0.5
> (môi trường cũ), nhánh lỗi được kích hoạt bằng hồ sơ **có tệp đính kèm**.
> **Kết quả mong đợi:** một thao tác chỉ sinh **một** thông báo kết quả.
> **Loại bug:** số lượng thông báo phụ thuộc **thao tác + nhánh lỗi + dữ liệu tiền đề** ⇒ KHÔNG phải bug tĩnh ⇒ bắt
> buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**
(đây là môi trường dev vừa dựng bản vá, **khác** môi trường đo bug gốc — chênh môi trường chính là thứ cần kiểm).

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw_03` — vai trò `CB_NV_TW` ("CB Nghiệp vụ - Trung ương #03"), đơn vị BTP · TW | **`cbnv_tw`** — `CB_NV_TW`, `capDonVi TW`, `donViId 00000000-0000-4000-8000-000000000001` (đọc từ phiên đăng nhập thực), thanh trên hiện `BTP · TW` ⇒ **trùng đúng** vai trò + cấp + đơn vị của tài khoản bug gốc. `cbnv_tw_03` không tồn tại trên môi trường này nên dùng tài khoản gốc cùng vai trò/cấp/đơn vị (Rule 7) | Không |
| Màn hình + trạng thái entity | Màn "Thêm mới Hồ sơ Vụ việc" (`/vu-viec/tao-moi`); VU_VIEC **chưa tồn tại** (chưa sinh mã); sau khi bấm, màn hình đứng nguyên tại đây | **Đúng cùng màn** `/vu-viec/tao-moi`, VU_VIEC chưa tồn tại. Ở mọi lượt đo nhánh lỗi, sau khi bấm màn hình **đứng nguyên** tại đây, không sinh mã | Không |
| Dữ liệu tiền đề | Hồ sơ điền đủ trường bắt buộc, doanh nghiệp có sẵn trong phần mềm, kênh tiếp nhận Trực tiếp, ngày tiếp nhận mặc định, **có 1 tệp PDF đính kèm** (~614 B) | Hồ sơ điền đủ trường bắt buộc, doanh nghiệp **Công ty TNHH Mẫu Test** (MST 0101234567, mã DN-XX-0005) chọn từ ô "Tìm doanh nghiệp", kênh **Trực tiếp**, ngày tiếp nhận mặc định 04/08/2026, **cũng có 1 tệp PDF đính kèm** (`NHSYC_OOS_01-v2-tep-dinh-kem.pdf`, 1.2 KB) | Không |
| Thao tác + **nhánh lỗi được đo** | Bấm **[Lưu & Tiếp nhận]** đúng 1 lần; nhánh lỗi kích hoạt bằng **tệp đính kèm** (máy chủ trả lỗi hệ thống) | Bấm **[Lưu & Tiếp nhận]**; nhánh lỗi cũ (tệp đính kèm) **đã hết** — cùng dữ liệu nay **tạo được** hồ sơ `VV-BTP-TW-20260804-003` (ảnh `…-v2-01`). Vì vậy đo trên **5 nhánh lỗi khác của chính màn đó**: ① thiếu trường bắt buộc ② tệp sai định dạng ③ tệp vượt 20MB ④ tiêu đề vượt 500 ký tự ⑤ **lệnh gửi thất bại giữa chừng** (ngắt kết nối máy chủ ngay trước khi bấm) — nhánh ⑤ chính là nhánh "catch" đã sinh câu *"Lỗi hệ thống, vui lòng thử lại sau."* của bug gốc. Thêm nhánh ⑥ tải tệp thất bại | Không |
| Phép đo (số thông báo ↔ số lệnh gửi) | Bộ bắt thông báo dùng chung (không lọc trùng, đọc `innerText`, tự kiểm 1 bộ đo) — bug gốc đo được **1 lệnh gửi → 2 khung thông báo** | Đúng bộ đo đó (`tools/toast-capture.js` nguyên văn), **tự kiểm `soObserverDangSong = 1`** trước mỗi loạt đo; mỗi lượt đối chiếu **số lệnh gửi** ↔ **số khung thông báo**; có loạt **9 lượt bấm cách nhau 3,5 giây** để chứng minh không có 2 khung nào sinh từ cùng 1 lượt bấm | Không |

## Kết quả đo — từng nhánh lỗi (đều trên màn "Thêm mới Hồ sơ Vụ việc")

- **① Bỏ trống toàn bộ trường bắt buộc rồi bấm lưu** → **0** lệnh gửi, **0** khung thông báo nổi, và **5 dòng lỗi —
  mỗi trường đúng 1 dòng**, không dòng nào lặp nghĩa (ảnh `…-v2-02`).
- **② Đính kèm tệp `.txt` (định dạng không được hỗ trợ)** → 0 lệnh gửi, **đúng 1** khung:
  *"…: Định dạng không được hỗ trợ. Chấp nhận: .pdf, .doc, .docx, .xls, .xlsx, .jpg, .png"*.
- **③ Đính kèm tệp PDF 21 MB (vượt 20MB/tệp)** → 0 lệnh gửi, **đúng 1** khung:
  *"…: Kích thước vượt quá giới hạn 20MB."*
- **④ Tiêu đề 600 ký tự (vượt giới hạn 500)** → 0 lệnh gửi, 0 khung nổi, **đúng 1 dòng**
  *"Tiêu đề không quá 500 ký tự"* dưới đúng ô nhập.
- **⑤ Lệnh lưu thất bại (mất kết nối máy chủ) — 3 lượt rời rạc** → mỗi lượt **1 lệnh gửi → đúng 1 khung**:
  *"Không kết nối được máy chủ."* (ảnh `…-v2-03` bắt đúng khoảnh khắc chỉ có **một** khung trên màn hình).
- **⑤' Cùng nhánh ⑤, loạt 9 lượt bấm cách nhau 3,5 giây** → **9 lệnh gửi → đúng 9 khung**, cùng một câu; khoảng cách
  giữa 2 khung liên tiếp = **3505 / 3494 / 3504 / 3506 / 3499 / 3478 / 3507 / 3507 ms** = đúng nhịp bấm
  ⇒ **không có cặp khung nào sinh ra từ cùng một lượt bấm**.
- **⑥ Tải tệp thất bại (mất kết nối khi đang tải tệp đính kèm)** → 1 lệnh gửi → **đúng 1** khung: *"Tải file thất bại"*.
- **Nhánh lỗi của bug gốc (hồ sơ có tệp đính kèm)** → 1 lệnh gửi → **đúng 1** khung
  *"Đã tiếp nhận — VV-BTP-TW-20260804-003"*: nhánh này **đã hết lỗi**, hồ sơ tạo được kèm tệp (ảnh `…-v2-01`).

**Không lượt nào ra >1 khung thông báo.** Hai câu chữ của bug gốc (*"Lỗi hệ thống, vui lòng thử lại sau."* và *"Có lỗi
xảy ra. Vui lòng thử lại sau."*) **không xuất hiện ở bất kỳ nhánh nào**.

## Đã cố BÁC BỎ kết luận `Pass` bằng những cách nào

1. **Nghi "nhánh lỗi cũ hết lỗi nên không đo được gì, Pass là Pass oan"** → **BÁC**: không dừng ở đó, đã tìm và đo **6 nhánh lỗi khác** của chính màn hình đó, trong đó nhánh ⑤ là đúng nhánh "lệnh gửi đi rồi thất bại" đã sinh ra câu *"Lỗi hệ thống…"* của bug gốc.
2. **Nghi "chỉ hết lặp ở nhánh máy chủ trả lỗi, còn nhánh mất kết nối vẫn lặp"** → **BÁC**: nhánh mất kết nối đo 3 lượt rời rạc + 1 loạt 9 lượt, đều **1 lệnh gửi → 1 khung**.
3. **Nghi "hai khung sinh cùng lúc nhưng bộ đo gộp làm một"** → **BÁC**: bộ đo dùng đúng tệp dùng chung, **không lọc trùng** (trùng chính là dữ liệu cần đo); loạt 9 lượt cho ra **9** khung với **9** câu giống hệt nhau ⇒ bộ đo hoàn toàn ghi nhận được khung trùng nội dung.
4. **Nghi "bộ đo bị nhân bản nên đếm sai"** → **BÁC**: tự kiểm chèn node giả trước mỗi loạt, `soObserverDangSong = 1`; khoảng cách giữa các khung là 3,5 giây (đúng nhịp bấm) chứ không phải dưới 1 ms — loại đúng cờ đỏ "lỗi do bộ đo".
5. **Nghi "khung thứ hai bị dời xuống thành dòng lỗi trong biểu mẫu"** (giấu chứ không bỏ) → **BÁC**: nhánh ① và ④ cho thấy mỗi trường chỉ có **đúng 1 dòng lỗi**, không dòng nào lặp nghĩa.
6. **Nghi "hết lặp vì thao tác không còn gửi lệnh nào"** → **BÁC**: nhánh ⑤/⑤'/⑥ đếm được **đúng số lệnh gửi bằng số lượt bấm** — lệnh vẫn đi, vẫn thất bại, vẫn báo lỗi, chỉ khác là báo **một** lần.
7. **Nghi "bản vá chỉ có trên môi trường đo vòng trước"** → **BÁC**: lần này đo trên **môi trường khác** (`htpldn-uat.ospgroup.vn`, gói giao diện `index-DpIXRGaI.js`) chứ không phải môi trường của vòng trước, kết quả vẫn 1-lệnh-1-thông-báo.
8. **Nghi "tab mở lâu còn chạy mã cũ"** → **BÁC**: trong lượt đo có một lần phiên bị đăng xuất và đăng nhập lại (tải lại toàn bộ trang), sau đó đo lại vẫn ra kết quả như trên.

**Kết luận: 0 GAP** — đúng vai trò/đơn vị, đúng màn hình, đúng dữ liệu tiền đề (có tệp đính kèm), đúng phép đo của bug
gốc; nhánh kích hoạt lỗi phải đổi vì nhánh cũ đã hết lỗi, và việc đổi đã khai báo rõ ở trên kèm 6 nhánh thay thế.
