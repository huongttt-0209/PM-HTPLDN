# Kịch bản re-verify Mục B — 10 case không phải "Forbidden xuất file"

**Nguyên tắc:** chạy LẠI đủ luồng trên web bằng Chrome DevTools MCP, đúng vai trò/state/data như bug gốc.
Cấm Pass bằng quan sát tĩnh. Thiếu data → seed trước rồi verify trên dữ liệu MỚI.

Xong 1 case → `finish.py` (evidence → ghi sheet → cập nhật report) rồi mới sang case sau.

---

## 1. TDHSTVV_13 — T2 · dòng 67 — Thẩm định hồ sơ TVV, kết luận "Yêu cầu bổ sung"

| | |
|---|---|
| **Claim vòng 2** | TKM retest 25/7: **Người hỗ trợ không nhận được thông báo kèm lý do** |
| **KQ mong đợi** | Hồ sơ chuyển "Yêu cầu bổ sung" + gửi thông báo kèm lý do đến chủ hồ sơ + lưu vết + hiện toast thành công |
| **Căn cứ** | UI-04 toast (`srs-v3.5.md:571`) · FR-IV-06/UC44, SCR-IV-03 nút "Gửi kết quả thẩm định" (`srs-fr-04-chuyen-gia-tvv.md:519, :1564`) |

**Luồng phải chạy (2 tài khoản, dữ liệu MỚI):**
1. `cbnv_tw` → Mạng lưới tư vấn viên → Tư vấn viên/Chuyên gia → chọn hồ sơ trạng thái **Chờ thẩm định** (không có → seed hồ sơ mới).
2. Tab Thẩm định → Kết luận **"Yêu cầu bổ sung"** → nhập lý do (chuỗi mốc `RV2-0308-<hhmm>` để truy vết) → Gửi KQ.
3. Cài MutationObserver TRƯỚC khi bấm — bắt toast (không dedupe, dùng `outerHTML`).
4. Đọc lại chi tiết hồ sơ: trạng thái đã đổi chưa.
5. **Đăng xuất, đăng nhập bằng chính chủ hồ sơ (Người hỗ trợ)** → mở chuông thông báo → tìm thông báo mới có chứa lý do vừa nhập.

**Pass khi:** có toast + trạng thái đổi + chủ hồ sơ thấy thông báo **có kèm lý do**.
**Reopen khi:** thiếu bất kỳ ý nào (đặc biệt: thông báo không kèm lý do = fix một phần).

---

## 2. NHSYC_02 — T2 · dòng 88 — Form "Nhập thủ công" vụ việc HTPL

| | |
|---|---|
| **Claim vòng 2** | TKM retest 29/7: **Lỗi vẫn chưa được fix** (không nói rõ ý nào) |
| **Đã BA chốt 16/07** | 8 ý phụ đều KHÔNG phải lỗi Dev (SRS tự mâu thuẫn / danh mục cấu hình được) |
| **Ý DUY NHẤT dev nhận là bug** | Nhóm 4 thiếu trường **"Ngày tiếp nhận"** → bug-report cũ `BUG-NHSYC_02` đã [CLOSED] |

**Luồng phải chạy:**
1. `cbnv_tw` → Vụ việc HTPL → **Nhập thủ công**.
2. Chụp toàn bộ form, liệt kê ĐỦ 4 nhóm trường bằng `evaluate_script` (label + type + required).
3. Kiểm cụ thể: **có "Ngày tiếp nhận"** · **"Ghi chú tiếp nhận"** · Kênh tiếp nhận đếm giá trị · Loại hình hỗ trợ / Lĩnh vực pháp lý đếm giá trị (danh mục cấu hình — chỉ ghi nhận, không tính lỗi).
4. **Nhập đủ và Lưu thật một hồ sơ mới** (không dừng ở quan sát form) → xác nhận tạo được + hiển thị lại đúng giá trị "Ngày tiếp nhận" vừa nhập.

**Pass khi:** "Ngày tiếp nhận" có mặt, nhập-lưu-hiển thị lại đúng.
**Reopen khi:** trường vẫn thiếu, hoặc lưu xong không giữ giá trị.

---

## 3. TLCTCDG_11 — T3 · dòng 58 — Tiêu chí đánh giá, tổng trọng số ≠ 100%

| | |
|---|---|
| **Claim** | Hệ thống hiện toast **thành công**, không hiện cảnh báo tổng trọng số |
| **KQ mong đợi** | Hiện `Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100% trước khi trình phê duyệt` |
| **Căn cứ SRS** | `srs-fr-08-danh-gia.md:860, :862, :906` — **CHO PHÉP lưu** + hiện cảnh báo `WRN-DG-TC-01`. Chặn lưu mới là sai SRS. |

**Luồng phải chạy:**
1. Tài khoản có quyền đánh giá → Đánh giá hiệu quả → đợt trạng thái **Lập kế hoạch** (không có → tạo đợt mới).
2. Tab Tiêu chí → thêm/sửa tiêu chí sao cho **tổng trọng số ≠ 100%** (vd 90%).
3. Cài observer → bấm **Lưu** → bắt TẤT CẢ toast/alert (không lọc trùng).

**Pass khi:** lưu thành công **VÀ** xuất hiện cảnh báo nêu tổng trọng số hiện tại + yêu cầu đủ 100%.
**Reopen khi:** chỉ có toast thành công, không có cảnh báo nào (đúng như claim).

---

## 4. TKTMBMHD_07 — T3 · dòng 91 — Nút "Xóa bộ lọc" ở Thư mục biểu mẫu

| | |
|---|---|
| **Claim vòng 2** | Hệ thống **không trả về danh sách mặc định** |
| **Căn cứ SRS** | `srs-fr-09-bieu-mau.md:622` (SCR-VII-01 #7 — xóa từ khóa + mọi trường lọc + **đưa tab về "Tất cả"** + về sắp xếp mặc định), `:623` (tab: Tất cả / Đã công khai / Nháp / Đã ẩn) |

**Luồng phải chạy:**
1. Biểu mẫu → Thư mục biểu mẫu. Ghi lại **số bản ghi mặc định** + thứ tự 5 dòng đầu.
2. Nhập từ khóa + chọn lĩnh vực + chọn trạng thái + khoảng ngày, **đồng thời chuyển tab sang "Nháp"** (hoặc tab khác "Tất cả").
3. Bấm **Xóa bộ lọc**.
4. Đọc lại: các ô lọc đã trống chưa · **tab đang đứng là gì** · số bản ghi + thứ tự 5 dòng đầu có bằng bước 1 không.

**Pass khi:** ô lọc trống + tab về "Tất cả" + danh sách bằng mặc định bước 1.
**Reopen khi:** tab còn đứng ở tab cũ, hoặc danh sách khác mặc định.
*(Sắp xếp mặc định không được SRS định nghĩa rõ → nếu chỉ lệch thứ tự thì ghi nhận, không tính lỗi chính.)*

---

## 5. QLCHTHXLHS_02 — T3 · dòng 152 — Số thẻ màn Cấu hình hệ thống

| | |
|---|---|
| **Claim vòng 2** | TKM retest 31/7: Lỗi chưa được fix (đối tác chờ **4 thẻ**) |
| **Căn cứ SRS** | `srs-fr-10-quan-tri.md:1784`, `:1803` — đặc tả **3 thẻ**: Thời hạn xử lý/SLA · Mẫu phản hồi · Quản lý ngày lễ. "Phân công mặc định" + "Quy trình hỗ trợ" **đã bỏ 07/05/2026**. |

**Luồng phải chạy:** `admin` → Quản trị hệ thống → Cấu hình hệ thống → đếm thẻ, đọc tên từng thẻ, **bấm lần lượt từng thẻ** xác nhận mở đúng nội dung (không chỉ nhìn tiêu đề).

**Pass khi:** đúng 3 thẻ theo SRS và mỗi thẻ mở được nội dung tương ứng.
**Reopen khi:** thiếu/dư thẻ so với SRS, hoặc bấm thẻ không ra nội dung.

---

## 6. QLCHTHXLHS_03 — T3 · dòng 153 — Bảng cấu hình SLA (⚠️ nhiều khả năng Reopen)

| | |
|---|---|
| **Claim vòng 2** | (a) SRS có **2 cột riêng Cảnh báo mức 1 / mức 2** nhưng hệ thống gộp thành "Vùng cảnh báo" · (b) **Thiếu cột Quá hạn (%)** · (c) Loại yêu cầu **tràn dữ liệu** sang cột Tên loại |
| **Căn cứ SRS** | `srs-fr-10-quan-tri.md:1809-1816` — bảng có **2 cột cảnh báo riêng**, **có cột Quá hạn (%) = 100**, Loại yêu cầu **6 giá trị** hiển thị |

**Luồng phải chạy:** `admin` → Cấu hình hệ thống → thẻ SLA → `evaluate_script` đọc **toàn bộ `<th>`** + 1 hàng mẫu; đo `scrollWidth > clientWidth` của ô "Loại yêu cầu" để xác nhận tràn; chụp màn.

**Pass khi:** đủ 2 cột cảnh báo riêng + có cột Quá hạn (%) + không tràn.
**Reopen khi:** còn bất kỳ ý nào — ghi rõ ý nào đã fix, ý nào chưa (fix một phần vẫn là Reopen).

---

## 7. QLCHTHXLHS_07 — T3 · dòng 156 — Modal "Chỉnh sửa cấu hình SLA"

| | |
|---|---|
| **Claim vòng 2** | TKM retest 31/7: **Thiếu trường "Số ngày bổ sung tối đa"** |
| **Căn cứ SRS** | `srs-fr-10-quan-tri.md:1817` — modal **phải có** "Số ngày BS tối đa"; `:474`, `:1819` — **"Hệ số quá hạn" KHÔNG được xuất hiện** trên giao diện |
| **Bug-report cũ** | `Pass-bug-report-qtht-batch7.md` + `bug-report-qtht.md` → `~~BUG-QLCHTHXLHS_07~~ [CLOSED]` (phải cập nhật lại theo kết quả lần này) |

**Luồng phải chạy:**
1. `admin` → Cấu hình hệ thống → thẻ SLA → bấm **Sửa** ở dòng **"Vụ việc hỗ trợ pháp lý"**.
2. Liệt kê mọi label trong modal → kiểm "Số ngày bổ sung tối đa" **có**, "Hệ số quá hạn" **không**.
3. **Lưu thật:** đổi giá trị (vd 5 → 7) → Đồng ý → toast → đóng/mở lại modal xác nhận giá trị mới **được giữ**.
4. Kiểm dòng **"Hỏi đáp pháp luật"**: theo dev, dòng này **không** có ô đó.

**Pass khi:** có trường + lưu và giữ được giá trị mới + không còn "Hệ số quá hạn".
**Reopen khi:** thiếu trường, hoặc lưu không ăn.

---

## 8. QLTKND_03 — T3 · dòng 166 — Thẻ tab màn Tài khoản & Phân quyền

| | |
|---|---|
| **Claim vòng 2** | **Thiếu thẻ "Vô hiệu hóa"**, thẻ "Chờ kích hoạt" **chưa có màu nhấn** |
| **Bug gốc** | Hiện **6 thẻ**, dư "Chờ phân quyền" (trạng thái đã bỏ) |
| **Căn cứ SRS** | `srs-fr-10-quan-tri.md:1713` (SCR-VIII-03) — đúng **4 thẻ**: Tất cả / Hoạt động / Chờ kích hoạt / Tạm khóa. **Không có** thẻ "Vô hiệu hóa"; **không quy định màu** cho thẻ tab (màu vàng chỉ áp cho badge trạng thái ở cột danh sách). |

**Luồng phải chạy:** `admin` → Quản trị hệ thống → Tài khoản & Phân quyền → `evaluate_script` đọc danh sách tab (text + số đếm + class/màu) → **bấm từng tab**, đối chiếu danh sách trả về có đúng lọc theo trạng thái đó không.

**Quyết định:** bug gốc = "dư thẻ Chờ phân quyền". Hết dư + đúng 4 thẻ SRS → **Pass**, đồng thời ghi rõ trong note: 2 ý mới của đối tác (thẻ "Vô hiệu hóa" + màu nhấn) **vượt ngoài đặc tả**.
Nếu vẫn còn thẻ "Chờ phân quyền" → **Reopen**.

---

## 9. QLDX_03 — T3 · dòng 184 — Cảnh báo sắp hết phiên (⚠️ đã có dấu hiệu bất thường)

| | |
|---|---|
| **Claim vòng 2** | TKM retest 31/7: **Không hiện hộp thoại**, hệ thống nhảy thẳng về màn Đăng nhập kèm "Đăng xuất thành công" |
| **Căn cứ SRS** | `srs-fr-10-quan-tri.md:1958` (SCR-VIII-09) — cảnh báo ở **25 phút**, hết phiên ở **30 phút**. Nhãn nút trên hộp thoại **không được đặc tả** ở bất kỳ bản SRS nào → chỉ xét "có hộp thoại cảnh báo + cho phép gia hạn". |
| **Quan sát đã có** | Trong phiên làm việc trước, phiên chết ở **~7-10 phút** và **không có hộp thoại nào** — khớp triệu chứng đối tác, ngược với kết luận "không tái hiện được" của dev. |

**Luồng phải chạy (2 phép đo tách bạch):**
- **(A) Kiểm logic cảnh báo phía giao diện — không phải chờ 25 phút:** đăng nhập mới → đẩy lùi `localStorage['auth-last-activity']` về `Date.now() - 24.5*60*1000` → chờ ~60-90s **không thao tác** → quan sát DOM (observer) xem hộp thoại cảnh báo có bật ở mốc 25 phút không.
- **(B) Kiểm phiên chết sớm:** đăng nhập mới, ghi mốc thời gian, **không thao tác gì**, chỉ đọc DOM định kỳ → ghi lại thời điểm bị đẩy về `/login`. So với mốc 30 phút.

**Pass khi:** (A) hộp thoại cảnh báo bật đúng mốc 25' **VÀ** (B) phiên sống đến 30'.
**Reopen khi:** không có hộp thoại, hoặc phiên chết sớm hơn 30' — mô tả rõ số phút đo được.

---

## 10. VVDTN_04 — T3 · dòng 195 — BC Vụ việc đã tiếp nhận, biểu đồ tròn theo lĩnh vực

| | |
|---|---|
| **Claim vòng 2** | TKM retest 31/7: **Không hiển thị biểu đồ tròn theo lĩnh vực** |
| **Bug gốc** | Thiếu cả bảng lẫn biểu đồ "theo lĩnh vực" (BE đã trả data, FE không dựng) |
| **Căn cứ SRS** | `srs-fr-11-bao-cao.md:1065, :1067` — UC125 quy định **biểu đồ cột + biểu đồ xu hướng**; **biểu đồ tròn thuộc UC127**, không thuộc UC125 |
| **Bug-report cũ** | `Pass-bug-report-bctk-batch1.md` + `Pass-bug-report-bctk.md` → `~~BUG-VVDTN_04~~ [CLOSED]` |

**Luồng phải chạy:** `cbnv_tw` → Báo cáo thống kê → Loại BC = **Vụ việc đã tiếp nhận** → Kỳ Năm 2026 → Xem báo cáo → `evaluate_script` liệt kê **mọi khối biểu đồ + mọi bảng** (tiêu đề + loại chart) → xác nhận có phần **"theo lĩnh vực"** (bảng và/hoặc biểu đồ).

**Pass khi:** phần "theo lĩnh vực" đã hiển thị (bug gốc = thiếu hẳn phần này).
Yêu cầu "phải là biểu đồ **tròn**" **vượt ngoài UC125** → ghi rõ trong note, không tính là lỗi.
**Reopen khi:** vẫn không có phần "theo lĩnh vực" nào.

---

## Ghi chú chung khi chạy

- Mỗi case mở **tab mới** rồi đóng khi xong (tránh giới hạn 1 tải-tự-động/tab của Chrome và tránh state rơi rớt).
- Cài `MutationObserver` **trước** khi bấm nút, **cấm lọc trùng**, dùng `outerHTML` (node ẩn của AntD không có `textContent`).
- Mọi `evaluate_script` phải **tự chứa**: có sẵn khối đăng nhập lại nếu bị đẩy về `/login`.
- Đóng case: `python3 finish.py --ma-tc … --tab … --row … --verdict … --cond "…|…|…" …`
  Reopen bắt buộc `--note-file` (tiếng Việt có dấu, gạch đầu dòng, chỉ tả triệu chứng đang thấy).
