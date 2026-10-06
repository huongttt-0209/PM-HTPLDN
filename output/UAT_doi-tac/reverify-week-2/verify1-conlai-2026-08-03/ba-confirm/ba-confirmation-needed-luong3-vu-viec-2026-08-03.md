# BA confirmation needed — LUỒNG 3: Vụ việc HTPL (verify vòng 1, tab UAT tuần 2) — 2026-08-03

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được**, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report.

> **Phạm vi:** 2 nội dung — rows **127** và **145** của tab `UAT_TGPL Doanh Nghiệp-tuần 2`, sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`.
> **Cả 2 đều thuộc DẠNG B** (SRS tự mâu thuẫn / đặc tả silent → cần BA chốt source truth). **Không có TC dạng A.**
> **Môi trường verify:** `https://18.143.165.120.nip.io` · bản dựng **HTPLDN V1.0.5** · verify ngày **03/08/2026** qua Chrome DevTools MCP · tài khoản `cbnv_tw_03` (vai trò `CB_NV_TW`, đơn vị `BTP · TW`) — **không dùng `admin`**.
> **Nguồn SRS quote số dòng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` — đã mở file verify từng số dòng ngày 03/08/2026, không dùng số dòng từ trí nhớ.

> **⚠️ Lưu ý về tuần 3:** phần việc Luồng 3 ở tab tuần 3 chỉ có 1 case (`CNKQHT_07`, row 315) và đã verify `Pass` — **không phát sinh nội dung nào cần BA cho tuần 3**. Vì vậy không có file BA tương ứng trong `reverify-week-3/ba-confirm/vu-viec/`.

---

## NHSYC_01 (phần B của case) — Điểm ưu tiên hồ sơ vụ việc: thang cộng điểm, ngưỡng "nhiều lao động nữ", phạm vi áp dụng và nhãn hiển thị đều chưa chốt

> **Ranh giới với phần đã gửi Dev:** case `NHSYC_01` gộp 2 ý. Ý **(A)** — hồ sơ **có tệp đính kèm** thì bấm lưu không tạo được, hệ thống báo lỗi (`BUG-NHSYC_01`) — là lỗi kỹ thuật rõ ràng, **đã gửi Dev**, không nằm trong file này. Ý **(B)** dưới đây — điểm ưu tiên không tự tính (`BUG-NHSYC_01-B`) — **tạm dừng chờ BA**, chưa yêu cầu Dev sửa. Verdict `Reopen` đang ghi ở cột `Verify` của row 127 là do ý (A), không phải do ý (B).

**Bối cảnh testcase**

- Dòng Excel: **127**, mã TC `NHSYC_01`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ cấp Trung ương vào "Vụ việc HTPL" → "Nhập thủ công" → điền hồ sơ hợp lệ → bấm **[Lưu & Tiếp nhận]**.
- Expected trong file UAT (tiêu chí Output của phiếu): hồ sơ tạo xong phải có **điểm ưu tiên do hệ thống tự tính theo NĐ 55/2019 Điều 4**.
- Actual đối tác ghi: không quan sát được tiêu chí này vì hồ sơ chưa tạo được (đối tác dừng ở lỗi định dạng ngày tiếp nhận).

**Kết quả verify UI hiện tại**

- Verify ngày 03/08/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_03` (`CB_NV_TW`, đơn vị `BTP · TW`) — đúng vai trò + cấp của đối tác trong ảnh.
- Doanh nghiệp dùng để kiểm (`Cong ty TNHH QA UAT Kiem Thu`, DN-HNI-0001) **không** do phụ nữ làm chủ, **không** có số lao động nữ, **không** có số lao động khuyết tật ⇒ theo đặc tả thì mọi khoản cộng đều bằng 0, điểm phải là **1**.
- Hồ sơ tạo ra (`VV-BTP-TW-20260803-002`) hiển thị **"Ưu tiên: Trung bình"**, dữ liệu trả về `uuTien: 3`.
- Gọi lại chính dịch vụ tạo hồ sơ bằng phiên đăng nhập của `cbnv_tw_03` mà **không gửi** trường điểm ưu tiên → hệ thống vẫn trả **3** ⇒ đây là **hằng số mặc định, không phải kết quả tự tính**.
- Ô "Độ ưu tiên" trên form hiển thị nguyên văn `3 — Trung bình (mặc định BR-CALC-04)` ⇒ giao diện đang **lộ mã quy tắc nội bộ** ra người dùng cuối, và mã đó đã đổi thành `BR-CALC-07` từ SRS v3.5 rev. 3.
- Nhãn phần mềm dùng cho giá trị 3 là **"Trung bình"**, còn nhãn trong đặc tả là **"Bình thường"** — hai chữ khác nhau.
- Evidence:
  - `../bug-reports/vu-viec/image/BUG-NHSYC_01-tao-duoc-khi-bo-tep.png` (màn Chi tiết hồ sơ, dòng "Ưu tiên: Trung bình")
  - `../image/NHSYC_01-01-form-mac-dinh.png` (ô "Độ ưu tiên" mặc định kèm chuỗi `(mặc định BR-CALC-04)`)

**Điểm mâu thuẫn trong SRS v3.5**

1. **Thang cộng điểm có thể vượt trần cho phép của trường dữ liệu.**
   - Cách chấm điểm cộng dồn tối đa: `+3` (phụ nữ làm chủ) `+2` (nhiều LĐ nữ) `+2` (≥30% LĐ khuyết tật) `+1` (FIFO) = **8**.
   - Nhưng trường `uu_tien` bị ràng buộc **`BETWEEN 1 AND 5`**.
   - Đặc tả chỉ chốt **sàn** ("tối thiểu `uu_tien=1` cho mọi VV"), **không chốt trần** cũng không nói cách quy đổi 8 → thang 1–5.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:196`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2412`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:326`

2. **Ngưỡng "nhiều lao động nữ" không định lượng, trong khi tiêu chí kế bên thì định lượng.**
   - Tiêu chí lao động khuyết tật ghi rõ **`≥30% so_lao_dong`**.
   - Tiêu chí lao động nữ chỉ ghi **"nếu vượt ngưỡng"** (dòng 196) và **"DN nhiều LĐ nữ"** (dòng 2412) — không có con số, không trỏ tới bảng cấu hình nào.
   - ⇒ Không thể chấm đúng/sai phần mềm ở tiêu chí này vì không có mốc để so.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:196`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2412`

3. **Phạm vi áp dụng của quy tắc chấm điểm: hai chỗ trong SRS nói khác nhau.**
   - Mục "Applied in" ngay dưới thân quy tắc chỉ liệt kê **FR-V.I-09** (gợi ý người xử lý khi phân công).
   - Nhưng bảng tổng quan quy tắc lại liệt kê **FR-V.I-02, 04, 09**, và §Processing bước 6 của chính FR-V.I-04 (nhập thủ công — đúng chức năng đang kiểm) yêu cầu tự tính điểm ưu tiên.
   - ⇒ Chưa rõ **ngay lúc nhập hồ sơ thủ công** có phải tự tính điểm hay không, hay điểm chỉ được tính khi sang bước phân công.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2414`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2330`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:341`

4. **Nhãn hiển thị của thang điểm — chính SRS ghi là chưa chốt.**
   - Đặc tả nói nguyên văn: nhãn hiển thị là **"đề xuất, cần CĐT xác nhận"**.
   - Bảng nhãn đặt giá trị `3` = **"Bình thường"**, còn phần mềm đang hiển thị **"Trung bình"**.
   - ⇒ Chưa có căn cứ để chấm phần mềm sai nhãn, vì bản thân bảng nhãn chưa được chốt.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1522`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1528`

**Câu hỏi cần BA xác nhận**

Điểm ưu tiên của hồ sơ vụ việc tại màn **nhập hồ sơ thủ công** cần được hiểu theo hướng nào?

1. **Hướng 1 — có tự tính ngay khi nhập thủ công.** Hồ sơ vừa tạo phải mang điểm tính từ thông tin doanh nghiệp; doanh nghiệp không có trường ưu tiên nào thì điểm phải là **1 ("Thấp")**. Kèm theo, BA cần chốt thêm 3 điểm:
   - (a) Quy đổi tổng điểm cộng dồn (tối đa 8) về thang 1–5 theo cách nào — cắt trần tại 5, hay quy đổi theo khoảng?
   - (b) "Nhiều lao động nữ" là bao nhiêu — một con số cố định, một tỷ lệ (tương tự ≥30% của lao động khuyết tật), hay lấy từ bảng cấu hình?
   - (c) Nhãn hiển thị cho từng mức chốt là gì — giữ "Bình thường" theo bảng nhãn đề xuất, hay dùng "Trung bình" như phần mềm đang chạy?
2. **Hướng 2 — chỉ tính khi sang bước phân công.** Lúc nhập thủ công hồ sơ được đặt một giá trị mặc định, cán bộ tự chỉnh nếu cần. Khi đó phần mềm hiện đang **đúng**, và cần bổ sung vào đặc tả: giá trị mặc định là bao nhiêu, hiển thị nhãn gì, thời điểm nào điểm mới được tính lại.

**Đề xuất QA tạm thời**

- **Chưa gửi Dev ý (B) này** cho tới khi BA chốt source truth. Ý (A) — lỗi không tạo được hồ sơ khi có tệp đính kèm — vẫn giữ nguyên ở Dev, không chờ BA.
- Tạm verdict cho phần điểm ưu tiên của `NHSYC_01`: **`Cần BA xác nhận`**.
- Nếu BA chọn **hướng 1**: phần mềm hiện `Vẫn lỗi` (trả 3 thay vì 1), owner dự kiến **Dev BE**; đồng thời cần sửa nhãn ô "Độ ưu tiên" trên form cho khớp nhãn đã chốt.
- Nếu BA chọn **hướng 2**: điểm ưu tiên **không phải lỗi**, cần cập nhật lại tiêu chí Output của phiếu `NHSYC_01` cho khớp đặc tả.
- **Không phụ thuộc hướng nào — vẫn cần sửa:** chuỗi `(mặc định BR-CALC-04)` hiển thị trên form là mã quy tắc nội bộ, lại là **mã đã lỗi thời** (v3.5 rev. 3 đã đổi `BR-CALC-04` → `BR-CALC-07`; hiện `BR-CALC-04` đang thuộc nghiệp vụ khác ở `srs-fr-08` / `srs-fr-10`). Người dùng cuối không cần thấy mã quy tắc. Owner dự kiến **Dev FE**.
  - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:19`

---

## TKHSYCHTPL_OOS_01 — Hồ sơ đã kết thúc vẫn lọt bộ lọc "Sắp hết hạn", cột "Cảnh báo thời hạn" hiển thị nhãn không có trong đặc tả

> **Nguồn phát hiện:** đây là quan sát do tổ kiểm thử tự ghi nhận khi verify case `TKHSYCHTPL_03` ngày 03/08/2026, **không bắt nguồn từ phiếu của đối tác** (phiếu `TKHSYCHTPL_03` chỉ nói bộ lọc báo lỗi, không có dòng nào cho phần hiển thị cột này) ⇒ đã mở dòng mới trên sheet.

**Bối cảnh testcase**

- Dòng Excel: **145**, mã TC `TKHSYCHTPL_OOS_01` (dòng mở mới, ngoài phạm vi phiếu gốc).
- Nội dung kiểm tra: Cán bộ nghiệp vụ cấp Trung ương mở "Vụ việc HTPL / Danh sách" → đặt bộ lọc **"Mức SLA" = "Sắp hết hạn"** → đọc cột **"Cảnh báo thời hạn"** của các dòng trả về.
- Không có expected của đối tác cho nội dung này.

**Kết quả verify UI hiện tại**

- Mở đúng màn "Vụ việc HTPL / Danh sách", URL `/vu-viec/danh-sach?mucSla=SAP_HET&page=1`, tab **Tất cả**; các ô lọc khác để trống.
- Hệ thống trả về đúng **2 hồ sơ**: `VV-BTP-TW-20260712-006` và `VV-BTP-TW-20260712-005` (chân bảng ghi "Hiển thị 1-2 / 2 kết quả").
- Cả 2 hồ sơ **đều đã kết thúc**: một ở trạng thái **"Từ chối"**, một ở trạng thái **"Hoàn thành"**. Cùng tiếp nhận 12/07/2026, thời hạn xử lý 31/07/2026 — mốc này **đã trôi qua** so với ngày kiểm 03/08/2026; lần cập nhật cuối lần lượt là 29/07/2026 và 24/07/2026, tức trước cả mốc thời hạn.
- Ngay trên 2 dòng đó, cột **"Cảnh báo thời hạn"** hiển thị **"Đã hoàn thành"** — trong khi chính chúng vừa được bộ lọc **"Sắp hết hạn"** chọn ra. Người dùng nhìn màn hình sẽ thấy bộ lọc và cột hiển thị nói hai điều khác nhau, dễ hiểu nhầm là bộ lọc trả về sai bản ghi.
- Đo lại bằng phương pháp thứ hai — gọi chính dịch vụ danh sách bằng phiên đăng nhập của `cbnv_tw_03`: HTTP 200, tổng 2 bản ghi, cả 2 mang mức cảnh báo lưu trữ là **`SAP_HET`** (đúng lý do lọt bộ lọc), trạng thái là `TU_CHOI` / `HOAN_THANH`. ⇒ Giao diện và dữ liệu trả về **khớp nhau**: mức cảnh báo cũ được giữ nguyên từ lúc hồ sơ đóng, còn "Đã hoàn thành" là nhãn giao diện hiển thị đè lên.
- **Phân biệt 2 cột dễ nhầm:** cột **"Trạng thái"** hiện "Từ chối" / "Hoàn thành"; cột **"Cảnh báo thời hạn"** đứng sau cột "Thời hạn xử lý" và hiện "Đã hoàn thành". Ảnh bằng chứng chụp ở bề rộng 1920px lấy trọn dải bảng nên không cột nào bị khuất ngoài khung.
- **Không phải hồi quy do bản vá:** cách hiển thị này đã có từ trước lần sửa bộ lọc "Mức SLA".
- Evidence: `../bug-reports/vu-viec/image/BUG-TKHSYCHTPL_OOS_01-cot-canh-bao-thoi-han-hien-da-hoan-thanh.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **FR-V.I-CROSS-01** và **BR-CALC-03**, việc giữ nguyên mức cảnh báo cũ của hồ sơ đã đóng là **đúng phạm vi** đã mô tả:
   - Công việc tự động chạy mỗi 30 phút chỉ lấy **danh sách VV đang hoạt động** (`DA_TIEP_NHAN`, `DANG_KIEM_TRA`, `DA_PHAN_CONG`, `DANG_XU_LY`, `CHO_PHE_DUYET`) ⇒ hồ sơ `HOAN_THANH` / `TU_CHOI` **không nằm trong phạm vi rà**, nên mức cảnh báo của chúng không bao giờ được cập nhật lại.
   - Quy tắc tính chỉ nêu công thức và chu kỳ 30 phút, **không nói phải xử lý ra sao** với mức cảnh báo còn sót lại của hồ sơ đã đóng.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1436`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2442`

2. Nhưng **đặc tả màn hình SCR-V.I-01** và **bảng mã trạng thái** lại không có chỗ cho những gì đang hiển thị:
   - Cột "Cảnh báo thời hạn" được đặc tả đúng **4 mức**: 🟢 `BINH_THUONG` / 🟡 `SAP_HET` / 🔴 `QUA_HAN` / ⚫ `QUA_HAN_NGHIEM_TRONG`, và **luôn hiển thị**. Nhãn **"Đã hoàn thành" không nằm trong 4 mức này**; tra toàn file đặc tả không có chỗ nào định nghĩa nhãn đó.
   - Bảng mã của trường mức cảnh báo cũng chỉ có đúng 4 mã trên.
   - Bộ lọc "Mức SLA" ở thanh lọc cũng chỉ có đúng 4 lựa chọn, **không nêu có loại trừ hồ sơ đã kết thúc hay không**; chức năng tìm kiếm FR-V.I-08 cũng không nói.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1656`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1511`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1644`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:636`

**Câu hỏi cần BA xác nhận**

Với hồ sơ đã kết thúc (Hoàn thành / Từ chối), cột **"Cảnh báo thời hạn"** và bộ lọc **"Mức SLA"** trên màn danh sách vụ việc cần được hiểu theo hướng nào?

1. **Hướng 1 — mức cảnh báo là dữ liệu lịch sử, giữ nguyên tại thời điểm đóng hồ sơ.** Hồ sơ đã kết thúc vẫn được phép lọt bộ lọc "Sắp hết hạn" vì đó là mức của nó khi đóng; cột hiển thị cần thể hiện đúng mức đã lưu (Sắp hết hạn), không đè bằng nhãn khác.
2. **Hướng 2 — mức cảnh báo chỉ có nghĩa với hồ sơ đang xử lý.** Hồ sơ kết thúc thì mức cảnh báo được đặt lại/xoá, bộ lọc "Mức SLA" phải **loại trừ** các trạng thái kết thúc, và cột này để trống hoặc hiển thị dấu "—".
3. **Hướng 3 — bổ sung "Đã hoàn thành" thành một mức hiển thị chính thức** (mức thứ 5) trong đặc tả, kèm quy định hồ sơ mang nhãn này có lọt bộ lọc 4 mức kia hay không.

Kèm theo, BA cần chốt 3 điểm cụ thể:
- (a) Khi hồ sơ đóng, mức cảnh báo thời hạn có được đặt lại/xoá không, hay giữ nguyên giá trị tại thời điểm đóng?
- (b) Hồ sơ đã kết thúc có được phép xuất hiện trong kết quả lọc "Mức SLA = Sắp hết hạn" không?
- (c) Nhãn "Đã hoàn thành" ở cột "Cảnh báo thời hạn" có được bổ sung chính thức vào đặc tả không, hay với hồ sơ đã kết thúc thì cột này phải để trống / hiển thị "—"?

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho `TKHSYCHTPL_OOS_01`: **`Cần BA xác nhận`** (đã ghi `BA confirm` ở cột `Verify` row 145). QA **không kết luận `Open`** vì đã tra đủ 4 chỗ trong đặc tả (FR-V.I-08, FR-V.I-CROSS-01, SCR-V.I-01 cột 21, BR-CALC-03) và **không trích được điều khoản nào bị vi phạm**.
- Nếu BA chọn **hướng 1**: phần hiển thị hiện tại `Vẫn lỗi` ở chỗ đè nhãn "Đã hoàn thành" lên mức đã lưu, owner dự kiến **Dev FE**; phần bộ lọc trả về 2 hồ sơ là **đúng**.
- Nếu BA chọn **hướng 2**: cần sửa cả bộ lọc lẫn cột hiển thị, owner dự kiến **Dev BE** (loại trừ trạng thái kết thúc khỏi bộ lọc) + **Dev FE** (cột để trống/"—").
- Nếu BA chọn **hướng 3**: phần mềm hiện **không phải lỗi**, chỉ cần **cập nhật đặc tả** SCR-V.I-01 + bảng mã mức cảnh báo cho khớp thực tế; QA sẽ đóng dòng này.
