# Bảng đối chiếu điều kiện — CBKQDTBD_01 (vòng soát lại 2, 2026-08-04)

> Bug phụ thuộc **vai trò + trạng thái khóa học + dữ liệu kết quả đã duyệt** ⇒ KHÔNG phải bug tĩnh → bắt buộc điền bảng.
> Cột giữa = điều kiện của **BUG GỐC** (đối tác chụp 28/07/2026 + bảng điều kiện vòng 1).
> Cột phải = điều kiện **thực tế test lại** 04/08/2026 trên `https://htpldn-uat.ospgroup.vn`.
> Môi trường lần này **chính là môi trường đối tác chụp ảnh** — khóa học đối tác phản ánh (UUID
> `0aad5545-9361-4fe4-854a-18e3fdce5862`) vẫn còn nguyên nên dựng lại được ĐÚNG bản ghi gốc.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ Trung ương — mã vai trò `CB_NV_TW`, đơn vị `BTP · TW` (đọc góc phải ảnh đối tác) | Đúng vai trò + đúng đơn vị: **`cbnv_tw`** — "Cán bộ NV Trung ương", `CB_NV_TW`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`, hiển thị "Bộ Tư Pháp · Cục Bổ trợ tư pháp". Không dùng `admin` ra verdict | Không |
| Entity + trạng thái (state machine) | Khóa học UUID `0aad5545-9361-4fe4-854a-18e3fdce5862`, stepper bước 7 "Hoàn thành" đang đứng ⇒ `HOAN_THANH` | **Chính khóa đó** — `KH-20260703-005` "test thêm mới khóa học", stepper bước 7 "Hoàn thành" | Không |
| Dữ liệu tiền đề (kết quả đã được phê duyệt) | Bảng 2 học viên có Điểm 5.0 / 10.0, Kết quả Đạt / Không đạt ⇒ có ≥1 kết quả đã duyệt (PRE-03) | Đúng 2 học viên đó — Hoàng Minh Đức (5.0 · Đạt) và tester tkm (10.0 · Không đạt); cả 2 ở "Chưa công bố" trước khi đo | Không |
| Thao tác của case (chọn danh sách học viên → bấm Công bố) | Bước 4 của phiếu: "Chọn danh sách học viên và bấm nút **Công bố**"; kỳ vọng hiện thông báo "Đã công bố kết quả cho {số lượng} học viên" | Đã thử **đủ 3 đường**: (1) tích ô chọn từng dòng + tích "chọn tất cả"; (2) bấm nút "Công bố" trên từng dòng học viên; (3) bấm "Công bố tất cả" ở đầu bảng. Đo bằng bộ bắt thông báo `tools/toast-capture.js` (tự kiểm 1 observer) + đếm request | Không |
| Nhánh phủ định — khóa chưa đủ điều kiện | Không có trong phiếu gốc; bổ sung ở vòng soát lại để chứng minh hệ thống chặn đúng | Đo 2 nhánh: khóa **Đang diễn ra** `KH-20260509-006` (6 học viên, 2 có điểm) và khóa **Hoàn thành nhưng chưa có kết quả duyệt** `KH-20260803-001` | Không |

**Số ô GAP còn lại: 0** → đủ điều kiện chốt verdict.

> Dòng "Input / bộ lọc" không ghi vì tab không có ô nhập / bộ lọc chi phối kết quả; ô nhập duy nhất là "Lý do hủy công bố" — đã đưa vào phần đo dưới.

---

## Kết quả đo (bản dựng V1.0.5 · gói giao diện `index-DpIXRGaI.js`, khối màn khóa học `index-DdmY6P8Q.js`, đã tải lại trang bỏ bộ nhớ đệm trước khi chốt)

### A. Phần ĐÃ hết lỗi

- **Bấm "Công bố tất cả" → hộp thoại xác nhận → "Công bố":** 1 request (`POST .../ket-quas/publish`) · 1 khung thông báo — *"Đã gửi yêu cầu công bố. Hệ thống sẽ đẩy sang Cổng PLQG."* → 2/2 học viên chuyển **Đã công bố** + Thời điểm công bố **04/08/2026 16:47**; máy chủ lưu `congBo=true`.
- **Bấm "Hủy công bố tất cả" + lý do 3 ký tự:** 0 request · 0 thông báo · báo lỗi ngay tại ô nhập *"Lý do phải có tối thiểu 10 ký tự"* → không đổi trạng thái, chặn đúng.
- **Bấm "Hủy công bố tất cả" + lý do 61 ký tự:** 1 request (`POST .../ket-quas/unpublish`) · 1 khung thông báo — *"Đã gửi yêu cầu hủy công bố."* → 2/2 học viên về **Chưa công bố**; máy chủ lưu `congBo=false` + lý do hủy.
- **Khóa Đang diễn ra (`KH-20260509-006`):** đầu tab hiện bảng thông báo *"Chưa thể công bố kết quả — Chỉ có thể công bố/hủy công bố kết quả khi khóa học đã ở trạng thái Hoàn thành."*, toàn bộ nút + công tắc bị vô hiệu hóa. Gọi thẳng máy chủ cũng bị từ chối (422): *"Chỉ công bố KQ khi khóa đã HOAN_THANH"*.
- **Khóa Hoàn thành nhưng chưa có kết quả duyệt (`KH-20260803-001`):** 1 request · 1 thông báo — *"Không có kết quả nào ở trạng thái DA_DUYET để công bố"* → từ chối, không đổi dữ liệu.

Tab "Công bố kết quả" **đã tồn tại** — 8 tab: Thông tin · Học viên · Lịch học · Điểm danh · Kết quả · **Công bố kết quả** · Bài giảng đã gán · Đề kiểm tra.
1 thao tác ↔ 1 request ↔ 1 thông báo ở cả 2 lệnh, không có thông báo lặp.

### B. Phần CÒN lỗi — đúng bước 4 của phiếu

Bước 4 của phiếu là **"Chọn danh sách học viên và bấm nút Công bố"**. Trên bản dựng hiện tại **không thực hiện được**:

1. **Nút "Công bố" / "Hủy" ở cột Hành động của từng học viên luôn ở trạng thái mờ, bấm không được** (thuộc tính `disabled` = true trên mọi dòng, mọi khóa học đã kiểm: `KH-20260703-005` 2 dòng, `KH-20260509-005` 5 dòng, `KH-20260509-006` 6 dòng). Rê chuột lên nút, phần mềm **tự hiện chú thích**: *"Công bố/hủy theo từng học viên sẽ khả dụng khi hệ thống hỗ trợ (hiện chỉ công bố cấp khóa)."* — ảnh `evidence/CBKQDTBD_01-v2-05-nut-cong-bo-tung-hoc-vien-bi-vo-hieu-hoa.png`.
2. **Ô tích chọn dòng không có tác dụng:** tích 1 dòng, tích "chọn tất cả" đều không mở khóa nút nào, không hiện thanh "đã chọn N", và lệnh gửi đi vẫn là lệnh **cấp khóa** (không kèm danh sách học viên).
3. Vì vậy chỉ có đường **"Công bố tất cả"** — không thể công bố / hủy công bố cho **một phần** danh sách học viên.

**Đặc tả đối chiếu:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1932` (FR-III-19 / UC38 §Đặc tả màn hình SCR-III-02 — Tab 8): *"Bảng HV có kết quả: Cột Chọn dòng · Họ tên · Email · Số điện thoại · Đơn vị · Đề kiểm tra · Điểm · Kết quả · Trạng thái công bố · Thời điểm công bố · **Hành động (Công bố/Hủy công bố cá nhân)**"*, và `:1394` (Inputs — Công bố: `hoc_vien_ids` *"mặc định = tất cả học viên có KQ DA_DUYET trong khóa"*) + `:1402` (Inputs — Hủy công bố: `hoc_vien_ids` *"Mặc định = tất cả HV đã được công bố"*) ⇒ đặc tả **cho phép chọn một phần danh sách học viên**, cấp khóa chỉ là giá trị mặc định.

⇒ **Fix một phần: tab đã có + công bố cấp khóa chạy đúng, nhưng công bố/hủy công bố theo từng học viên (bước 4 của phiếu) chưa dùng được → Reopen.**

## Đã cố bác bỏ kết luận Pass vòng trước bằng 5 hướng

1. Không chấm tĩnh: chạy trọn công bố → kiểm trạng thái đổi + máy chủ lưu → hủy công bố → kiểm trạng thái quay lại.
2. Kiểm chặn đầu vào: lý do hủy 3 ký tự bị chặn, 0 request gửi đi.
3. Kiểm nhánh phủ định 2 kiểu khóa (chưa Hoàn thành / chưa có kết quả duyệt), đo cả trên giao diện lẫn gọi thẳng máy chủ.
4. Kiểm nút từng dòng trên **3 khóa học khác nhau**, ở **cả 2 trạng thái công bố** (Chưa công bố → nút "Công bố"; Đã công bố → nút "Hủy") — luôn mờ.
5. Loại trừ lỗi phía máy đo: tải lại trang bỏ bộ nhớ đệm rồi đo lại (cùng gói giao diện `index-DpIXRGaI.js`), tự kiểm bộ bắt thông báo cho `soObserverDangSong = 1` trước mỗi lần đo.

**Vòng 1 kết luận Pass vì chỉ ghi nhận "có nút Công bố/Hủy từng dòng" mà không thử bấm** — đó chính là quan sát tĩnh mà vòng soát lại này phải bác.

## Ngoài phạm vi lỗi này (ghi nhận, không tính vào verdict)

- Sau khi hủy công bố, cột "Thời điểm công bố" vẫn giữ mốc thời gian cũ trong khi cột trạng thái đã về "Chưa công bố" (thấy ở `KH-20260703-005` và `KH-20260509-005`).
- Thông báo từ chối khi khóa chưa có kết quả duyệt hiện chuỗi mã nội bộ `DA_DUYET` cho người dùng cuối.

---

## Đo lại LẦN 2 độc lập trong cùng vòng soát lại (17:05–17:10, tài khoản `cbnv_tw`, đã tải lại trang bỏ bộ nhớ đệm — gói giao diện `index-DpIXRGaI.js`, bản dựng V1.0.5)

Mục đích: kiểm tra xem kết luận **Reopen** ở phần trên có bị bác được không (đề phòng Reopen oan).

1. **Nút của từng học viên vẫn mờ** — đọc trực tiếp thuộc tính trên mã trang của khóa `KH-20260703-005`:
   2/2 dòng có đúng 1 nút "Công bố" với `disabled = true`. Nút "Hủy công bố tất cả" cũng mờ vì cả 2 học viên
   đang ở "Chưa công bố" (đúng logic).
2. **Ô tích chọn vẫn vô tác dụng:** bấm ô "chọn tất cả" → 4/4 ô tích chuyển sang trạng thái đã chọn, nhưng
   KHÔNG có thanh "đã chọn N", KHÔNG nút nào được mở khóa (nút từng dòng vẫn `disabled = true`), và hộp thoại
   xác nhận vẫn ghi nguyên văn *"Hệ thống sẽ đẩy kết quả đào tạo của **toàn khóa** sang Cổng PLQG qua hàng đợi"*
   — tức là lệnh gửi đi vẫn ở cấp khóa, không hề nhận danh sách học viên được tích.
   Ảnh: `evidence/CBKQDTBD_01-v2-09-chon-tat-ca-van-hoi-cong-bo-toan-khoa.png`.
3. **Thêm triệu chứng MỚI ở lần đo này — không công bố lại được:** sau khi khóa đã trải qua 1 lượt
   công bố → hủy công bố (16:47), bấm "Công bố tất cả" lần nữa thì hệ thống **từ chối**:
   1 lệnh gửi đi ↔ 1 khung thông báo (bộ bắt thông báo tự kiểm `soObserverDangSong = 1`), nội dung
   *"Đang có yêu cầu PUBLISH đang chờ xử lý cho khóa học này"* (máy chủ trả 409, mã `ERR-INT-III-15-01`).
   Ảnh: `evidence/CBKQDTBD_01-v2-10-thong-bao-sau-khi-cong-bo-lan-2.png`. Nghĩa là yêu cầu công bố lần trước
   vẫn nằm chờ trong hàng đợi và chặn mọi lần công bố sau — cán bộ không có cách nào biết hay xử lý hàng đợi đó
   trên giao diện. Thông báo còn hiện chuỗi mã nội bộ `PUBLISH` cho người dùng cuối.

⇒ Không bác được kết luận **Reopen**; lần đo thứ hai còn phát hiện thêm 1 triệu chứng nặng hơn (mục 3).

> **Lưu ý số dòng SRS:** tệp `srs-fr-03-dao-tao.md` được sửa ngay trong ngày 04/08/2026 (bổ sung phần BA chốt cho `KTDGKQHT_02`/`KTDGKQHT_05`) nên số dòng dịch **+23** so với lúc đo đầu giờ chiều. Số dòng trong file này đã cập nhật theo bản mới nhất: Tab 8 = 1932, Inputs Công bố = 1394, Inputs Hủy công bố = 1402.
