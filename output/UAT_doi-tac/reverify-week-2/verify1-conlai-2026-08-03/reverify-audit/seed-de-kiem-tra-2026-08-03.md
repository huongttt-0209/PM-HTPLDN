# Audit — Seed đề kiểm tra + chốt 3 nghi vấn treo của luồng Đào tạo, tập huấn

| Mục | Giá trị |
|---|---|
| **Ngày đo** | 2026-08-03, 19:45 – 20:20 (giờ VN) |
| **Môi trường** | `https://18.143.165.120.nip.io` — bản dựng **V1.0.5** |
| **Gói mã giao diện lúc đo** | `/assets/index-RAuQ-eDH.js` — máy chủ ghi `Last-Modified: Mon, 03 Aug 2026 12:51:29 GMT` (= 19:51 giờ VN) |
| **Tài khoản ra verdict** | **`cbnv_tw_05`** — CB Nghiệp vụ Trung ương (`CB_NV_TW`), đơn vị **Cục Bổ trợ tư pháp** (`donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`) |
| **Vì sao không dùng `cbnv_tw`** | `cbnv_tw` bị **một phiên QA khác đăng nhập chiếm** giữa chừng (MailHog ghi nhận một yêu cầu OTP cho `cbnv_tw` lúc `12:53:39 GMT` không phải do phiên này gửi) → đẩy phiên này về `/login`. Fallback đúng **Rule 7**: cùng vai trò `CB_NV_TW`, cùng đơn vị, cùng cấp TW. Không dùng `admin` để ra verdict. |
| **Chống lẫn phiên** | Mở trang trong ngữ cảnh cookie/bộ nhớ riêng (`isolatedContext: "qa-dekt-0803"`); **trước MỖI phép đo quyết định** đều đọc lại `localStorage['auth-store'].state.userInfo` để xác nhận đang là `cbnv_tw_05`, và ảnh chụp nào cũng thấy dòng tiêu đề *"CB Nghiệp vụ - Trung ương #05 · CB_NV_TW"*. Không dùng con số nào đo trong lúc còn nghi ngờ danh tính phiên. |
| **Đặc tả tham chiếu** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` (bản v3.5 — nguồn duy nhất) |

> `GET /api/v1/auth/me` trả **502** trên môi trường này (không phải endpoint hợp lệ) nên danh tính phiên được đọc từ `localStorage['auth-store']` thay vì gọi API.

---

## 0. Vì sao phải seed — và đã seed cái gì

Cả 3 nghi vấn treo lại từ vòng đo 17:00 đều vướng **cùng một khoảng trống**: lúc đó hệ thống **chưa có bất kỳ đề kiểm tra nào**, nên không khóa học nào được gán đề, nên không loại trừ được giả thuyết *"cột Đề kiểm tra chỉ render khi khóa đã gán đề"*. Theo **Nguyên tắc 4** của `QA_VERIFY_PROTOCOL.md` (thiếu tiền đề thì phải dựng, không được coi là blocker), vòng này dựng đủ tiền đề rồi mới đo.

**Nhật ký seed** (mọi bước đều chụp màn hình và **đã mở ảnh đọc lại** để đối chiếu tên file với nội dung pixel):

| # | Thao tác | Kết quả máy chủ | Ảnh |
|:-:|---|---|---|
| 1 | `Đào tạo, tập huấn → Ngân hàng câu hỏi & Đề kiểm tra → Đề kiểm tra` — danh sách **0 đề** (đúng lý do các khóa không gán được đề) | — | — |
| 2 | `Tạo đề kiểm tra`: tên **"QA-DEKT-0803 — Đề kiểm tra pháp lý DN (QA seed 03/08)"**, cách tạo **Thủ công**, chọn 1 câu hỏi từ ngân hàng, thời gian làm bài 30 phút, **điểm đạt 5.0** | `POST /api/v1/de-kiem-tras` → tạo thành công | [`SEED-DEKT-01`](../bug-reports/dao-tao/image/SEED-DEKT-01-form-tao-de-kiem-tra-truoc-khi-luu.png) |
| 3 | Kích hoạt đề (bắt buộc, vì `:1908` ghi rõ danh sách gán chỉ liệt kê đề `trang_thai = 'KICH_HOAT'`) | `POST /api/v1/de-kiem-tras/{id}/kich-hoat` → trạng thái **Kích hoạt** | [`SEED-DEKT-02`](../bug-reports/dao-tao/image/SEED-DEKT-02-de-kiem-tra-da-kich-hoat.png) |
| 4 | Gán đề vào **`AAA-KH-TW`** ("Tập huấn pháp lý cấp Trung ương 2026", **Hoàn thành**, 4 học viên đã duyệt kết quả) qua tab "Đề kiểm tra" | `POST /api/v1/khoa-hocs/{id}/de-kiem-tras/{deId}` | [`SEED-DEKT-03`](../bug-reports/dao-tao/image/SEED-DEKT-03-modal-gan-de-dropdown-1-de-KICH-HOAT.png) · [`SEED-DEKT-04`](../bug-reports/dao-tao/image/SEED-DEKT-04-AAA-KH-TW-da-gan-de-tab7.png) |
| 5 | Gán cùng đề vào **`KH-QAW7-HOINGHI`** ("QAW7 — Hội nghị đối thoại DN 2026", **Đang diễn ra**, 2 học viên) | `POST /api/v1/khoa-hocs/{id}/de-kiem-tras/{deId}` | — |
| 6 | Nhập điểm **9.0** và **4.0** cho 2 học viên của `KH-QAW7-HOINGHI` → `Lưu kết quả` (để bản ghi kết quả **thực sự trỏ tới đề**) | `POST /api/v1/khoa-hocs/{id}/ket-quas/batch-update` → sau đó `GET .../ket-quas` trả `tenDeKiemTra = "QA-DEKT-0803 — …"` cho cả 2 bản ghi | [`SEED-DEKT-05`](../bug-reports/dao-tao/image/SEED-DEKT-05-QAW7-tab5-truoc-khi-luu-diem.png) |

**Đo thông báo bằng `tools/toast-capture.js`** (bản dùng chung, không tự viết observer, không lọc trùng, không đọc `textContent`; mỗi lần cài đều tự kiểm `soObserverDangSong === 1` và tiêm 1 node giả để chắc chắn observer còn sống). Kết quả: **mỗi thao tác đúng 1 request ↔ 1 khung thông báo** — không có lỗi thông báo lặp ở luồng seed này.

| Thao tác | Số request (khác GET) | Số khung thông báo | Nội dung |
|---|:-:|:-:|---|
| Tạo đề kiểm tra | 1 | 1 | "Tạo đề kiểm tra thành công" |
| Kích hoạt đề | 1 | 1 | "Đã kích hoạt đề kiểm tra" |
| Gán đề vào `AAA-KH-TW` | 1 | 1 | "Đã gán đề kiểm tra" |
| Gán đề vào `KH-QAW7-HOINGHI` | 1 | 1 | "Đã gán đề kiểm tra" |
| Lưu điểm (2 học viên) | 1 | 1 | "Đã lưu kết quả" |

---

## 1. Nghi vấn 1 — Tab "Kết quả" thiếu cột "Đề kiểm tra" → **LÀ BUG** ✅

**Đặc tả:** `srs-fr-03-dao-tao.md:1901` — `SCR-III-02` Tab 5 *"Kết quả kiểm tra"* liệt kê: *STT · Họ tên · Email · Số điện thoại · Đơn vị · **Đề kiểm tra** · Điểm · Xếp loại (auto BR-KQ-01) · Kết quả (auto BR-KQ-02) · Ghi chú*. Bảng Inputs của chính `FR-III-05` (`:550`) quy định `de_kiem_tra_id` *"đề kiểm tra ứng với điểm — **bắt buộc khi nhập điểm kiểm tra**"*.

**Kết quả đo — 10 cột, GIỐNG HỆT NHAU ở cả 4 tình huống, trên cùng một bản dựng:**

| # | Tình huống | Khóa học · trạng thái | Dãy cột đo được | Số cột | Có "Đề kiểm tra"? |
|:-:|---|---|---|:-:|:-:|
| a | **Chưa** gán đề (đối chứng) | `KH-QAW7-HOINGHI` · Đang diễn ra | STT · Họ tên · Email · Số điện thoại · Đơn vị · **Chuyên cần** · Điểm kiểm tra · Kết quả · Xếp loại · Ghi chú | 10 | ❌ |
| b | **Chưa** gán đề (đối chứng) | `AAA-KH-TW` · Hoàn thành | y hệt (a) | 10 | ❌ |
| c | **ĐÃ** gán đề | `AAA-KH-TW` · Hoàn thành | y hệt (a) | 10 | ❌ |
| d | **ĐÃ** gán đề **+ điểm đã lưu, bản ghi trỏ đúng đề** | `KH-QAW7-HOINGHI` · Đang diễn ra | y hệt (a) | 10 | ❌ |

⇒ **Giả thuyết "render có điều kiện" bị loại trừ**: gán đề không làm cột xuất hiện; kể cả khi bản ghi kết quả đã mang `tenDeKiemTra`, cột vẫn không có.

**Ba phương pháp đo độc lập, khớp nhau:**
1. **Đọc DOM** kèm quét node ẩn: `thead th` = **10**, `<colgroup><col>` = **10**, không phần tử nào `display:none` hay `offsetWidth === 0` ⇒ **không có cột bị ẩn**.
2. **Đọc bằng mắt trên ảnh full-res sau khi cuộn ngang hết cỡ sang phải** (bảng có cuộn ngang thật: `scrollWidth 1315` vs `clientWidth 1128`) — nhóm cột cuối đúng như trên, không có cột nào tên "Đề kiểm tra".
3. **Đối chứng dương tính cùng bản dựng, cùng khóa học**: tab "Công bố kết quả" **CÓ** cột "Đề kiểm tra" và hiển thị đúng `QA-DEKT-0803 — …` ⇒ dữ liệu đã tới được giao diện; đây là lỗi **không dựng cột** ở tab "Kết quả", không phải thiếu dữ liệu.

**Ảnh:** [đối chứng (a)](../bug-reports/dao-tao/image/BUG-KTDGKQHT_21-doichung-01-tab5-khoa-CHUA-gan-de-QAW7.png) · [lỗi (c)](../bug-reports/dao-tao/image/BUG-KTDGKQHT_21-02-tab5-AAA-KH-TW-DA-gan-de-van-thieu-cot-DeKiemTra-cuon-het-phai.png) · [lỗi (d)](../bug-reports/dao-tao/image/BUG-KTDGKQHT_21-03-tab5-QAW7-da-gan-de-va-da-nhap-diem-van-thieu-cot-DeKiemTra.png) · [đối chứng dương tính](../bug-reports/dao-tao/image/CBKQDTBD_02-retest-02-tab8-QAW7-DA-gan-de-hien-ten-de-kiem-tra.png)

**Xử lý:** mở dòng mới **`KTDGKQHT_21`** (dòng **147**, tab `UAT_TGPL Doanh Nghiệp-tuần 2`) — `Trạng thái 1 = Fail`, `Trạng thái dev fix 1 = Open`, `Verify = Open`. Bug ID **`BUG-KTDGKQHT_21`** (Medium/P2) trong [`bug-report-dao-tao.md`](../bug-reports/dao-tao/bug-report-dao-tao.md). Bảng điều kiện 0 GAP: [`cond/KTDGKQHT_21.md`](../cond/KTDGKQHT_21.md).

> **Cố ý loại khỏi phạm vi:** cột **"Chuyên cần"** mà bản dựng thêm vào (SRS `:1901` không liệt kê) — việc gộp `số buổi có mặt / tổng buổi (tỷ lệ %)` vào một ô đang là **câu hỏi chờ BA** ở dòng 116 `KTDGKQHT_02`. Không log trùng.

---

## 2. Nghi vấn 2 — "Xếp loại có giá trị trong khi Điểm kiểm tra trống" → **KHÔNG PHẢI BUG** ❌

**Bản chất: đây là lỗi của phép đo, không phải lỗi của phần mềm.** Ô "Điểm kiểm tra" ở tab "Kết quả" là một `<input>`; đọc bằng `td.innerText` **luôn trả về chuỗi rỗng** dù ô đang hiển thị số. Nghi vấn hình thành vì lần đo trước đọc theo cách đó.

**Đo lại bằng 2 phương pháp độc lập trên dữ liệu CŨ (`AAA-KH-TW`, 4 học viên):**

| Học viên | Giao diện — đọc `input.value` | Máy chủ — `GET /api/v1/khoa-hocs/{id}/ket-quas` | Xếp loại hiển thị | BR-KQ-01 (`:2230`) |
|---|:-:|:-:|---|:-:|
| 1 | `9.0` | `diemKiemTra: 9.0` | Giỏi | ≥ 8.5 → Giỏi ✅ |
| 2 | `8.0` | `diemKiemTra: 8.0` | Khá | ≥ 7.0 → Khá ✅ |
| 3 | `6.5` | `diemKiemTra: 6.5` | Trung bình | ≥ điểm đạt → Trung bình ✅ |
| 4 | `4.0` | `diemKiemTra: 4.0` | Không đạt | < điểm đạt → Không đạt ✅ |

**Đo trên DỮ LIỆU HOÀN TOÀN MỚI do chính tổ kiểm thử tạo (`KH-QAW7-HOINGHI`, 2 học viên):**
- **Trước khi nhập điểm:** cả "Kết quả" và "Xếp loại" đều hiển thị `—`. Đúng BR-KQ-01 (`:2230`) *"Chưa nhập điểm → Chưa chấm"* — **không có** chuyện xếp loại tự có giá trị khi chưa có điểm.
- **Sau khi lưu:** `9.0` → Xếp loại **Giỏi**, Kết quả **Đạt**; `4.0` → Xếp loại **Không đạt**, Kết quả **Không đạt**. Máy chủ trả `xepLoai: GIOI / KHONG_DAT` khớp giao diện.

⇒ Hai phương pháp **không mâu thuẫn**, cùng bác bỏ nghi vấn. **Không mở dòng TC.** (Trường `xepLoai` do máy chủ trả sẵn trong `ket-quas`, không phải giao diện tự suy diễn.)

---

## 3. Nghi vấn 3 — Tab "Công bố kết quả" thiếu 5 cột (dòng 146 `CBKQDTBD_02`) → **lỗi CÓ THẬT nhưng ĐÃ ĐƯỢC SỬA** ⇒ đính chính dòng 146

**Điều còn treo:** liệu cột "Đề kiểm tra"/"Điểm" có phải chỉ render khi khóa đã gán đề? Nếu đúng thì dòng 146 đang liệt kê sai danh sách cột thiếu và **phải sửa** — một dòng bug sai còn tệ hơn không có bug.

**Đo lại lúc 20:00 trên đúng khóa `AAA-KH-TW`, tải lại trang bỏ bộ nhớ đệm:** bảng có **đủ 12 cột** — `(chọn dòng) · STT · Họ tên · Email · Số điện thoại · Đơn vị · Đề kiểm tra · Điểm · Kết quả · Trạng thái công bố · Thời điểm công bố · Hành động`, đúng `:1909`; `<colgroup><col>` = 12, không cột nào ẩn. Ảnh: [`CBKQDTBD_02-retest-01`](../bug-reports/dao-tao/image/CBKQDTBD_02-retest-01-tab8-AAA-KH-TW-CHUA-gan-de-du-12-cot.png).

**Cột "Đề kiểm tra" hiển thị VÔ ĐIỀU KIỆN** (đây là câu trả lời cho điểm treo): khóa chưa gán đề thì ô hiện `—`; khóa đã gán đề + đã nhập điểm (`KH-QAW7-HOINGHI`) thì ô hiện đúng `QA-DEKT-0803 — Đề kiểm tra pháp lý DN (QA seed 03/08)`. Ảnh: [`CBKQDTBD_02-retest-02`](../bug-reports/dao-tao/image/CBKQDTBD_02-retest-02-tab8-QAW7-DA-gan-de-hien-ten-de-kiem-tra.png).

**Vì sao khác lần đo 17:55 — giao diện đã được triển khai lại 3 lần trong ngày:**

| Mốc | Gói mã giao diện | Bằng chứng |
|---|---|---|
| 07:59:38 GMT (14:59 VN) | `index-DeoB6dQU.js` | ghi trong [`QLDXDTTH_01.md`](QLDXDTTH_01.md) |
| lần đo bug gốc 17:55 VN | `index-bJhJGCw4.js` | ghi trong [`CBKQDTBD_01.md`](CBKQDTBD_01.md) + ảnh `../image/CBKQDTBD_01-F-sau-congbo-thanhcong.png` chụp **7 cột** trên chính khóa đó ⇒ **bug gốc là thật, không phải đo sai** |
| 12:51:29 GMT (19:51 VN) | `index-RAuQ-eDH.js` | header `Last-Modified` của gói lúc đo lại |

Dòng 146 được tạo lúc 18:00:50 và ghi P/Q lúc 18:56 (theo `tools/sheet_add_bug_row.log` + `sheet_write.log`) — tức **trước** bản triển khai 19:51.

**Xử lý:** `sheet_write.py --mode reverify --row 146 --ma-tc CBKQDTBD_02 --status Pass --pass-ghi-de-note` → `[Q146] 'Open' → 'Pass'`, `[R146]` thay bằng note đính chính (mở đầu `☑️ Đã kiểm tra lại — lỗi không còn, chuyển Pass.`). **P146 giữ nguyên `Open`** (cột P là của dev, mode `reverify` cố ý không đụng). Đã cập nhật [`cond/CBKQDTBD_02.md`](../cond/CBKQDTBD_02.md) + [`notes/CBKQDTBD_02.txt`](../notes/CBKQDTBD_02.txt).

Dùng `Pass` chứ **không** dùng `Resolved` vì đây đúng nghĩa *"dev đã sửa, QA test lại chạy đúng"* — có bằng chứng bản dựng thay đổi giữa 2 lần đo, không phải *"không tái hiện được mà không giải thích nổi"*.

---

## 4. Phát hiện thêm trong lúc đo (ghi nhận, chưa mở dòng mới)

1. **Dòng 130 `KTDGKQHT_20` (chuyên cần) vẫn tái hiện** trên bản dựng mới: khóa `KH-QAW7-HOINGHI` có **3** buổi trong `lich-hocs` nhưng `GET .../ket-quas` trả `tongBuoi = 1`; một học viên `soBuoiCoMat = 0` vẫn nhận `tyLeChuyenCan = "100.00"` và Kết quả **"Đạt"** — trái **BR-KQ-02** (`srs-fr-03-dao-tao.md:2246`, điều kiện AND cứng giữa chuyên cần và điểm). Dòng 130 đã có, không mở trùng.
2. **Tab "Đề kiểm tra" (Tab 7) chỉ có 5/8 cột** theo `:1908`: đang có *Tên đề · Số câu hỏi · Trạng thái · Thời điểm thêm · Hành động*; **thiếu** *STT · Mã đề · Lĩnh vực · Người thêm*, **thừa** *Trạng thái*. Phát hiện ngoài phạm vi 3 nghi vấn, **chưa log** — đề nghị QA lead quyết có mở dòng riêng hay không (theo C1 của postmortem thì nên log).

---

## 5. Dữ liệu seed để lại cho dev tái hiện

| Loại | Mã / tên | Trạng thái | Ghi chú |
|---|---|---|---|
| Đề kiểm tra | `QA-DEKT-0803 — Đề kiểm tra pháp lý DN (QA seed 03/08)` | Kích hoạt | 1 câu hỏi, 30 phút, điểm đạt 5.0 — **đề đầu tiên của hệ thống** |
| Khóa học | `KH-QAW7-HOINGHI` — "QAW7 — Hội nghị đối thoại DN 2026" | Đang diễn ra | đã gán đề trên; 2 học viên có điểm 9.0 (Đạt/Giỏi) và 4.0 (Không đạt) |
| Khóa học | `AAA-KH-TW` — "Tập huấn pháp lý cấp Trung ương 2026" | Hoàn thành | đã gán đề trên; 4 học viên đã duyệt + đã công bố kết quả |

---

*Audit generated: 2026-08-03 20:20:00 | QA Automation via Claude Code*
