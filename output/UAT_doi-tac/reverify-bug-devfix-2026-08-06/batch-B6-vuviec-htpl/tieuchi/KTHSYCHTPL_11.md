Mã case: KTHSYCHTPL_11 (dòng 45 tab `bug`)          Thời điểm viết: 2026-08-06 13:01
Môi trường verify: https://18.143.165.120.nip.io          Thời điểm đo: 2026-08-06 13:17 → 13:36 (giờ VN)

**Bản dựng đã đo (có dấu vân tay):**

| Nguồn | Giá trị |
|---|---|
| Chuỗi phiên bản in trong trang | **HTPLDN · V1.0.8** (chân sidebar — đối tác chụp bản ghi **V1.0**) |
| Dấu vân tay bó mã FE | `assets/index-CNwX9JjX.js` · CSS `assets/index-DVlgOkLg.css` (đọc bằng `evaluate_script` trên thẻ `<script src>` / `<link href>`) |
| Header phản hồi `GET /` | `last-modified: Thu, 06 Aug 2026 02:51:16 GMT` (= **09:51:16 giờ VN 06/08/2026**) · `etag: "6a73f6a4-428"` · `server: nginx/1.27.5` · `via: 1.1 Caddy` |
| Phiên bản API | `GET /api/docs-json` → `info.version = 1.0.0` ("HTPLDN API") |

> Chuỗi "V1.0.8" một mình **không đủ** để truy bản dựng (dự án deploy lại không đổi số) — cặp
> `index-CNwX9JjX.js` + `last-modified 06/08/2026 09:51:16` mới là mốc truy được.

> **Khai hồ sơ QA đợt trước đã đọc** (theo GIAI ĐOẠN A — chống kéo tiêu chí về vừa khít số đo cũ):
> `reverify-week-2/reverify-audit/KTHSYCHTPL_11/condition-table.md` ·
> `reverify-week-2/reverify-audit/rv3-conditions/KTHSYCHTPL_11.md` ·
> `reverify-week-2/ba-confirmation-needed-week-2.md` (mục KTHSYCHTPL_11) ·
> `reverify-week-2/phan-tich-tung-van-de-ba-confirmation-tuan-2.md` ·
> `flowtest-2026-08-05/tieuchi/KTHSYCHTPL_11.md`.
> Mục 4 dưới đây suy từ ĐẶC TẢ (srs-v3.5), **không** lấy số đo / ngưỡng của các file trên.
> (Riêng file `flowtest-2026-08-05` chốt `M = 1` — bản này **không** theo, xem mục 5.)

---

1. **Đối tác phản ánh** — tách 3 vế:

   - **(a) Trạng thái:** kết luận Đạt phải chuyển hồ sơ "Đang kiểm tra" → "Đã phân công".
   - **(b) Ghi nhận người + thời điểm:** hệ thống phải ghi **người kiểm tra** và **thời điểm kiểm tra**.
   - **(c) Lối vào thao tác:** màn không hiển thị nút "Hoàn tất kiểm tra", chỉ hiển thị "Kiểm tra lại".

   **Bằng chứng:** `partner-evidence/KTHSYCHTPL_11.jpg` — đã mở full-res.
   Thấy: màn chi tiết vụ việc **VV-QA-R7-SLA-QHNT** ("QA R7 — Vụ việc SLA QUA_HAN_NGHIEM_TRONG"),
   badge trạng thái **"Đang kiểm tra"**, thanh tiến trình dừng đúng bước "Đang kiểm tra";
   thanh hành động chỉ có **[Phân công]** + **[Kiểm tra lại]** — **không** có nút mang chữ "Hoàn tất kiểm tra";
   accordion "Kết quả kiểm tra" đang mở, bảng cột *Mã / Hạng mục / Đạt / Không đạt / Ghi chú*,
   dòng **C01 "Văn bản đề nghị hỗ trợ (Mẫu 01 NĐ55)"** chỉ thấy một dấu **"—"**, **không thấy dấu tick**.
   → **Ảnh KHỚP đúng case** (đúng màn + đúng triệu chứng vế (c)).
   ⚠️ Hạn chế của ảnh, ghi để không suy quá: khung ảnh **cắt ngang ở C01** nên **không chứng minh được**
   điều kiện "đã đánh dấu đủ 6 hạng mục"; ảnh chụp **trạng thái sau**, **không bắt được** thao tác chọn
   kết luận Đạt; ảnh **không cho thấy** vùng người kiểm tra / ngày kiểm tra (nằm ngoài khung) ⇒ vế (b)
   **không có bằng chứng ảnh**, phải tự dựng lại ở giai đoạn B.
   Vụ việc trong ảnh do **QA seed** (tên chứa "QA R7"), không phải dữ liệu đối tác tự tạo.

2. **Đặc tả nói gì** — nguồn duy nhất `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:

   - `srs-fr-05-vu-viec.md:514` — FR-V.I-06 PRE-02: *"VV ở trạng thái DA_TIEP_NHAN hoặc DANG_KIEM_TRA"*.
   - `srs-fr-05-vu-viec.md:522` — FR-V.I-06 Inputs #3: *"ket_luan | text | Y | DAT / KHONG_DAT / YEU_CAU_BO_SUNG"*.
   - `srs-fr-05-vu-viec.md:523` — Inputs #4: *"ly_do | text | Cond | Bắt buộc nếu KHONG_DAT hoặc YEU_CAU_BO_SUNG"*.
   - `srs-fr-05-vu-viec.md:541` — Processing bước 5: *"Nếu DAT: vụ việc sẵn sàng phân công, **giữ trạng thái
     DANG_KIEM_TRA** — chỉ chuyển DA_PHAN_CONG khi CB NV phân công người/tổ chức xử lý qua FR-V.I-09
     (khớp điều kiện bảng chuyển trạng thái "Đạt + chọn người/tổ chức xử lý")"*.
   - `srs-fr-05-vu-viec.md:550` — Postconditions: *"Kết quả kiểm tra được ghi nhận"*.
   - `srs-fr-05-vu-viec.md:564` — AC: *"**Given** CB NV kiểm tra xong **When** kết luận Đạt **Then** vụ việc sẵn
     sàng phân công, vẫn ở trạng thái DANG_KIEM_TRA; chỉ chuyển DA_PHAN_CONG khi CB NV phân công người/tổ chức
     xử lý (FR-V.I-09)"*.
   - `srs-fr-05-vu-viec.md:1730` — SCR-V.I-03 thành phần #7, Accordion 4 — Kết quả Kiểm tra:
     *"Checklist 6 hạng mục (ĐẠT/KHÔNG_ĐẠT) từ UC106 + kết luận + lý do + **người kiểm tra** + **ngày**.
     "Lần bổ sung: {n}/3"… | Điều kiện hiển thị: Khi VV đã qua DANG_KIEM_TRA"*.
   - `srs-fr-05-vu-viec.md:1744` — bảng nút hành động: *"DANG_KIEM_TRA | [Hoàn tất Kiểm tra] · [Kiểm tra lại] |
     CB NV | Kết luận: **Đạt → vụ việc sẵn sàng phân công, VẪN giữ trạng thái DANG_KIEM_TRA** (chưa chuyển
     DA_PHAN_CONG)… Nút [Kiểm tra lại] dùng khi cần sửa lại kết quả kiểm tra đã lưu"*.
   - `srs-fr-05-vu-viec.md:1745` — *"DANG_KIEM_TRA (kết luận Đạt) … [Phân công] … **Chỉ khi CB NV chọn được
     người/tổ chức xử lý và xác nhận thì vụ việc mới chuyển sang DA_PHAN_CONG.**"*.
   - `srs-fr-05-vu-viec.md:2288` — bảng chuyển trạng thái: *"DANG_KIEM_TRA | DA_PHAN_CONG | Đạt + chọn người/tổ
     chức xử lý | Đối tượng xử lý hợp lệ, đang hoạt động | Gửi TB người được phân công | FR-V.I-09"*.
   - `srs-fr-05-vu-viec.md:959` — AC FR-V.I-12: *"**Given** CB NV kết luận kiểm tra **Đạt** **When** vụ việc giữ
     nguyên DANG_KIEM_TRA **Then** FR này **không kích hoạt** — không gửi thông báo DN"*.

   🔴 **BA ĐÃ CHỐT ĐÚNG ĐIỂM TRANH CHẤP (vế a) — dẫn nguồn kèm ngày:**
   `srs-fr-05-vu-viec.md:22` (bảng Revision History, dòng **`2026-07-16 | BA + Claude`**):
   *"**Apply chốt UAT tuần 2:** … sửa nút "Đạt" khớp bảng chuyển trạng thái — **Đạt giữ DANG_KIEM_TRA, chỉ
   chuyển DA_PHAN_CONG khi phân công người xử lý (KTHSYCHTPL_11, đồng bộ FR-V.I-06)**…"*
   → BA nêu **đích danh mã case này**, ngày **2026-07-16**. Trước đó QA đã đưa lên BA vì SRS tự mâu thuẫn
   (`reverify-week-2/ba-confirmation-needed-week-2.md:1068`, 2 dòng SRS cũ `:1736` vs `:2280` ngược nhau);
   BA chốt phương án (A) và đã sửa SRS. ⇒ Vế (a) là **áp quyết định BA có sẵn**, KHÔNG phải QA tự bác đối tác,
   và KHÔNG cần hỏi BA lại.

   **IM LẶNG về:**
   - Nhãn chữ trên nút mở phiếu kiểm tra ở trạng thái "Đang kiểm tra" — `:1744` có liệt kê nhãn
     "[Hoàn tất Kiểm tra] · [Kiểm tra lại]" nhưng không quy định điều kiện ẩn/hiện giữa 2 nút này khi kết quả
     kiểm tra **đã được lưu** (chỉ nói [Kiểm tra lại] "dùng khi cần sửa lại kết quả kiểm tra đã lưu").
   - Định dạng hiển thị người kiểm tra (họ tên đầy đủ / tên đăng nhập / chức danh) và định dạng thời điểm
     (có giờ phút hay chỉ ngày).
   - Có phải ghi lại người/thời điểm của **từng lần** kiểm tra (lịch sử) hay chỉ giữ **lần gần nhất**.

3. **Precondition:**

   - **Tài khoản chấm verdict:** `cbnv_dp_01` / `Test@1234` (vai trò **CB_NV_DP** — cấp Địa phương, trùng vai trò
     trong ảnh đối tác "CB NV DP 01 (AG)"). Đăng nhập tại `https://18.143.165.120.nip.io/login`.
     *(Không dùng `cbnv_dp` — input.md ghi tài khoản này 401 từ 03/08/2026. Không dùng `admin` để ra verdict.)*
   - **Tài khoản phụ chỉ để dựng dạng D2** (mục 5): `cbnv_dp_02` / `Test@1234` — cùng vai trò CB_NV_DP, cùng
     đơn vị với `cbnv_dp_01`. Nếu tài khoản này khác đơn vị / không đăng nhập được → xem cách hạ cấp ở mục 5.
   - **Màn:** Vụ việc HTPL → danh sách → Xem chi tiết → `/vu-viec/{id}` (vùng thanh hành động + accordion
     "Kết quả kiểm tra").
   - **Dữ liệu tiền đề — tự seed bằng luồng chuẩn, trên vụ việc QA, KHÔNG đụng vụ việc của đối tác:**
     - **VV-1** (cho D1 + D2): 1 vụ việc thuộc đơn vị của `cbnv_dp_01`, đang ở **"Đã tiếp nhận"**, chưa có kết
       quả kiểm tra nào.
     - **VV-2** (cho D3): 1 vụ việc khác cùng đơn vị, đang ở **"Đã tiếp nhận"** hoặc **"Đang kiểm tra"**.
     - Tiền đề **tạo được mà không tạo → cấm mọi verdict** (kể cả ô trống).
   - **Ghi trước khi bấm:** thời điểm đồng hồ máy lúc bấm lưu kết luận (để đối chiếu P3), và tên hiển thị của
     tài khoản đang đăng nhập (đọc ở góc phải header).

4. **✅ PASS khi — đủ cả 4 (đo trên VV-1, dạng D1):**

   - **P1.** Với vụ việc ở trạng thái **"Đang kiểm tra"** thuộc đơn vị của `cbnv_dp_01`, tài khoản này **mở lại
     được** phiếu kiểm tra bằng một thao tác có sẵn ngay trên màn chi tiết (không cần đổi vai trò, không cần
     gọi API tay). Trong phiếu **đếm được đủ 6 dòng hạng mục** (C01→C06) và ô kết luận **có đủ 3 lựa chọn**
     tương ứng Đạt / Không đạt / Yêu cầu bổ sung.
     *(Không quy định nhãn chữ của nút — nhãn nào cũng được, miễn có đường vào.)*
   - **P2.** Đánh dấu 6/6 hạng mục Đạt + chọn kết luận **Đạt** + xác nhận → hệ thống **chấp nhận** (không toast
     lỗi, không thông báo từ chối). **Tải lại trang** rồi đọc lại: vùng "Kết quả kiểm tra" hiển thị kết luận
     **đúng bằng chữ "Đạt"** — **không** phải chuỗi giữ chỗ (ví dụ "đã có dữ liệu"), **không** rỗng, **không**
     `null` / `undefined`.
   - **P3.** Cùng vùng đó, sau khi tải lại trang, đọc được **thành chữ đủ 2 thông tin**:
     - **người kiểm tra** = đúng người vừa bấm lưu (khớp tên hiển thị của `cbnv_dp_01` đã ghi ở mục 3);
     - **thời điểm kiểm tra** = ngày (và giờ nếu có), **lệch ≤ 1 ngày** so với đồng hồ lúc bấm lưu.
     Cả 2 **vẫn còn sau khi tải lại trang** (không phải chỉ hiện thoáng rồi mất).
   - **P4.** Ngay sau khi lưu kết luận Đạt (chưa làm gì thêm): badge trạng thái + thanh tiến trình **vẫn là
     "Đang kiểm tra"**; trên màn **tồn tại một thao tác phân công riêng**; chỉ khi chọn được người/tổ chức xử
     lý và xác nhận thì badge + thanh tiến trình **mới** đổi sang **"Đã phân công"** (đọc lại sau khi tải lại
     trang).

   **❌ FAIL nếu (bất kỳ điều nào):**

   - **F1.** Ở trạng thái "Đang kiểm tra", `cbnv_dp_01` **không còn đường nào** trên màn chi tiết để mở phiếu
     ghi/sửa kết luận kiểm tra (mọi lối vào biến mất, hoặc bấm vào không mở, hoặc mở ra nhưng không có ô kết
     luận / không đủ 6 hạng mục).
   - **F2.** Bấm lưu kết luận Đạt bị từ chối (báo lỗi), **hoặc** lưu xong nhưng tải lại trang thì kết luận biến
     mất / quay về giá trị cũ.
   - **F3.** Vùng "Kết quả kiểm tra" **thiếu ít nhất 1 trong 3**: kết luận thực · người kiểm tra · thời điểm
     kiểm tra — hoặc in ra chuỗi giữ chỗ / rỗng / `null` / `undefined` ở các ô đó.
   - **F4.** Người kiểm tra hiển thị **sai người** (không phải tài khoản vừa lưu), hoặc thời điểm kiểm tra lệch
     **> 1 ngày** so với lúc thao tác.
   - **F5.** Kết luận Đạt làm vụ việc **tự nhảy sang "Đã phân công"** khi chưa chọn người/tổ chức xử lý (ngược
     `:541` / `:2288`), **hoặc** đã chọn người xử lý + xác nhận thành công mà trạng thái **không** đổi sang
     "Đã phân công".
   - **F6.** Ở dạng D2 (mục 5): lưu lại kết luận lần 2 thành công nhưng **người kiểm tra / thời điểm kiểm tra
     không đổi theo lần lưu mới nhất** (đóng băng ở lần đầu).
   - **F7.** Ở dạng D3 (mục 5): kết luận "Yêu cầu bổ sung" lưu thành công nhưng vùng "Kết quả kiểm tra"
     **không** ghi người kiểm tra và/hoặc thời điểm kiểm tra.

   **KHÔNG được chấm Fail vì (đã có quyết định / đặc tả nói rõ ngược lại, hoặc đặc tả im lặng):**

   - Vụ việc **vẫn ở "Đang kiểm tra"** sau khi kết luận Đạt → **BA chốt 2026-07-16** (`srs-fr-05-vu-viec.md:22`,
     nêu đích danh KTHSYCHTPL_11) + `:541` + `:564` + `:2288`. Kỳ vọng "→ Đã phân công" của đối tác (vế a) đã bị
     BA bác từ tuần 2. **Vòng verify trước đã chấm sai đúng điểm này** ("Hệ thống không chuyển trạng thái hồ
     sơ") — không lặp lại.
   - Nút **không mang đúng chữ "Hoàn tất kiểm tra"** (vế c) → nhãn là cách hiện thực; `:1744` không quy định
     điều kiện ẩn/hiện giữa 2 nút khi kết quả đã lưu. Chênh nhãn chỉ **ghi chú**, không Fail.
   - Vùng "Kết quả kiểm tra" **không hiện ô "lý do"** khi kết luận Đạt → `:523` chỉ bắt buộc lý do khi
     Không đạt / Yêu cầu bổ sung.
   - **Không có thông báo gửi doanh nghiệp** khi kết luận Đạt → `:959` nói rõ FR-V.I-12 không kích hoạt ở nhánh Đạt.
   - Người kiểm tra hiển thị dạng **chức danh / tên đăng nhập** thay vì họ tên đầy đủ, hoặc thời điểm **chỉ có
     ngày, không có giờ** → đặc tả im lặng về định dạng (miễn truy được đúng người + đúng ngày).
   - Chỉ giữ **lần kiểm tra gần nhất**, không có lịch sử nhiều lần → đặc tả im lặng.

5. **Dạng dữ liệu phải phủ — M = 3** *(bug thuộc nhóm "trường hiển thị dữ liệu" ⇒ bắt buộc ≥ 2 dạng)*:

   - **D1 — Kiểm tra lần đầu, kết luận Đạt:** VV-1 từ **"Đã tiếp nhận"** → mở phiếu kiểm tra → 6/6 Đạt →
     kết luận **Đạt**. Đây là luồng chính của case.
   - **D2 — Kiểm tra lại (ghi đè kết quả đã lưu), kết luận Đạt:** vẫn VV-1, giờ đã ở **"Đang kiểm tra"** và đã
     có kết quả từ D1 → **`cbnv_dp_02`** mở lại phiếu và lưu lại kết luận **Đạt**. Kiểm: người kiểm tra +
     thời điểm phải **phản ánh lần lưu gần nhất** (đổi sang `cbnv_dp_02`, giờ mới), không đóng băng ở D1.
     *Hạ cấp nếu `cbnv_dp_02` khác đơn vị hoặc không đăng nhập được:* dùng lại `cbnv_dp_01`, chờ ≥ 2 phút rồi
     lưu lại → khi đó chỉ chấm được **thời điểm** có cập nhật; ghi rõ trong báo cáo là đã hạ cấp và **không**
     kết luận gì về trường "người kiểm tra" ở dạng này.
   - **D3 — Kết luận khác Đạt:** VV-2 → kết luận **"Yêu cầu bổ sung"** (nhập lý do theo `:523`) → vùng
     "Kết quả kiểm tra" vẫn phải ghi đủ **người kiểm tra + thời điểm**. Dạng này chứng minh 2 trường không phải
     chỉ tồn tại ở nhánh Đạt.

   **Nguồn xác định M:** ① `srs-fr-05-vu-viec.md:514` (PRE-02 — chức năng kiểm tra chạy được từ **2 trạng thái
   nguồn** DA_TIEP_NHAN và DANG_KIEM_TRA ⇒ 2 đường sinh dữ liệu) · ② `:522` (enum `ket_luan` **3 giá trị**
   DAT / KHONG_DAT / YEU_CAU_BO_SUNG) · ③ `:1744` (nút [Kiểm tra lại] — đường **ghi đè** kết quả đã lưu).
   Nhánh **KHONG_DAT** cố ý để ngoài M: nó đẩy vụ việc sang TU_CHOI (`:2290`) — trạng thái kết thúc, gây nhiễu
   cho các dạng còn lại; D3 đã đủ chứng minh nhánh "khác Đạt".

6. **Bảng điều kiện** — cột "Đối tác" điền NGAY (từ bằng chứng); 2 cột sau điền ở giai đoạn B:

   | Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
   |---|---|---|:-:|
   | Vai trò / tài khoản | "CB NV DP 01 (AG)" · mã vai trò **CB_NV_DP** · banner "BTP · DP" (cấp Địa phương, đơn vị An Giang) | **Trùng khít.** `cbnv_dp_01` — `hoTen` "CB Nghiệp vụ - Địa phương #01", `vaiTro ["CB_NV_DP"]`, `capDonVi "DP"`, `donViId 00000000-0000-4000-8002-000000000006`, banner "BTP · DP" (đọc `GET /api/v1/auth/me`). Có quyền `kiem-tra_vu_viec`. D2 dùng thêm `cbnv_dp_02` — **CÙNG vai trò CB_NV_DP, CÙNG `donViId` ...8002-000000000006**, không phải nới chiều mà là yêu cầu của dạng D2 (cần người thứ hai để đo trường "người kiểm tra" có đổi không) | **Không** |
   | Entity + trạng thái | Vụ việc **VV-QA-R7-SLA-QHNT** ("QA R7 — Vụ việc SLA QUA_HAN_NGHIEM_TRONG"), badge **"Đang kiểm tra"**, thanh tiến trình dừng ở bước "Đang kiểm tra"; thanh hành động chỉ có [Phân công] + [Kiểm tra lại] | **Tái hiện đúng trạng thái đó bằng luồng chuẩn.** Sau khi lưu kết luận Đạt, cả 3 vụ việc QA đều rơi vào **đúng** trạng thái đối tác chụp: badge "Đang kiểm tra", thanh tiến trình dừng bước 4, thanh hành động **chỉ còn [Phân công] + [Kiểm tra lại]** (ảnh `...-03-...png`). ⇒ trạng thái trong ảnh đối tác chính là trạng thái **sau khi kiểm tra đã lưu thành công**, không phải màn bị thiếu nút | **Không** |
   | Dữ liệu tiền đề | Accordion "Kết quả kiểm tra" đang mở, cột *Mã / Hạng mục / Đạt / Không đạt / Ghi chú*; chỉ nhìn được **dòng C01** "Văn bản đề nghị hỗ trợ (Mẫu 01 NĐ55)" với dấu **"—"**, C02→C06 bị cắt khỏi khung ⇒ **KHÔNG chứng minh được** điều kiện "đã đánh dấu đủ 6 hạng mục"; vụ việc do **QA seed**. Vùng người kiểm tra / ngày kiểm tra **nằm ngoài khung ảnh** | **Tự dựng, phủ cả nhánh đối tác không chứng minh được.** Đánh dấu **đủ 6/6 hạng mục** bằng thao tác thật (bấm từng radio, đếm `.ant-radio-wrapper-checked` = 6). Đọc lại sau tải lại trang: C01→C06 đều **✓ ở cột "Đạt"**, dấu **"—" nằm ở cột "Ghi chú"** — đúng thứ đối tác nhìn thấy ở C01, tức "—" trong ảnh đối tác **không** phải dấu hiệu chưa đánh dấu. Vùng người/ngày kiểm tra (ngoài khung ảnh đối tác) đã đo trực tiếp ở P3 | **Không** |
   | Input / filter / giá trị nhập | Theo mô tả case: chọn kết luận **Đạt**. Ảnh chụp **trạng thái sau**, **không bắt được** thao tác chọn kết luận, cũng không thấy toast/thông báo nào | **Bắt được cả thao tác lẫn thông báo.** Ô kết luận có **đúng 3 lựa chọn** (`Đạt — chuyển sang phân công` · `Không đạt — từ chối hồ sơ` · `Yêu cầu bổ sung`, ảnh `...-02-...png`). Đo cả 2 giá trị: **Đạt** (D1/D2) và **Yêu cầu bổ sung** (D3). Bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1` trước mỗi lần bấm) ghi nhận mỗi lần lưu = **1 request + 1 khung thông báo + 1 mốc giờ** — không lặp, không nuốt: Đạt → *"Kiểm tra hồ sơ đạt — sẵn sàng phân công"*; Yêu cầu bổ sung → *"Đã yêu cầu bổ sung"*; Phân công → *"Đã phân công vụ việc cho QA NHT An Giang UAT2. Hệ thống đã gửi thông báo."* | **Không** |
   | Độ phủ biến thể (N bản ghi, M dạng) | **N = 1 bản ghi, 1 dạng** — 1 ảnh tĩnh, 1 vụ việc, 1 vai trò, 1 lần thao tác | **N = 3 bản ghi · M = 3/3 dạng.** VV-STP-AG-20260806-**001** (D1 kiểm tra lần đầu kết luận Đạt + P4 phân công) · **-002** (D3 kết luận Yêu cầu bổ sung) · **-003** (D2 kiểm tra lại, ghi đè bằng `cbnv_dp_02`). 2 vai trò-người khác nhau cùng vai trò CB_NV_DP, 4 lần lưu kiểm tra, 2 giá trị kết luận | **Không** |

   **Kết luận mục 6: 0/5 GAP còn hở** — đủ điều kiện ra verdict (không phải ô trống).
   Không nới chiều tài khoản nào: `cbnv_dp_01` trùng khít vai trò + cấp của đối tác và **có** dữ liệu để đo
   (tự dựng). `cbnv_dp_02` không phải nới chiều — nó là **biến đo** bắt buộc của dạng D2.

   **3 dữ kiện neo của đối tác:**
   `https://htpldn-uat.ospgroup.vn/vu-viec/aadd0022-0000-4000-8000-000000000004` ·
   trạng thái **"Đang kiểm tra"** (nút hiện: [Phân công] + [Kiểm tra lại]) ·
   vai trò **CB_NV_DP** ("CB NV DP 01 (AG)"), env **htpldn-uat.ospgroup.vn**, chuỗi bản dựng chân sidebar
   **"HTPLDN · V1.0"**, đồng hồ máy trong ảnh **09/07/2026 15:34**.

   **Lệch env / bản dựng so với đối tác — giới hạn hiệu lực của verdict (không phải GAP):**
   đối tác chụp trên **htpldn-uat.ospgroup.vn** bản **V1.0** (09/07/2026); vòng này đo trên **env dev
   https://18.143.165.120.nip.io** với bản dựng ghi ở đầu file. Verdict chỉ có hiệu lực cho bản dựng đã đo;
   phải re-verify khi bản đó lên env nghiệm thu của đối tác.

---

7. **Sửa đổi tiêu chí giữa chừng**

   > **2026-08-06 13:31 — đổi bản ghi mang dạng D2 (VV-1 → VV-3). Mục 4 và 5 KHÔNG đổi.**
   >
   > Mục 5 viết D2 chạy **trên chính VV-1**. Khi đo thực tế, P4 (đo "chỉ khi phân công mới chuyển
   > DA_PHAN_CONG") **tiêu mất** trạng thái DANG_KIEM_TRA của VV-1: sau khi phân công, VV-1 sang
   > DA_PHAN_CONG nên nút [Kiểm tra lại] không còn.
   > **Xử lý:** dựng thêm **VV-3** (`VV-STP-AG-20260806-003`) bằng đúng luồng chuẩn, đưa về DANG_KIEM_TRA
   > có sẵn kết quả kiểm tra do `cbnv_dp_01` lưu, rồi mới chạy D2 bằng `cbnv_dp_02` trên VV-3.
   > **Vì sao không làm hỏng phép đo:** D2 chỉ cần "một vụ việc ở DANG_KIEM_TRA đã có kết quả kiểm tra do
   > người khác lưu" — VV-3 thoả đúng điều kiện đó; danh tính bản ghi không phải biến của D2.
   > Hệ quả: N tăng 2 → 3 bản ghi, M vẫn = 3 dạng.

---

8. **Kết quả đo — 2026-08-06 (bản dựng `index-CNwX9JjX.js`)**

   **Tài khoản THỰC đã đăng nhập:** `cbnv_dp_01` (ra verdict) + `cbnv_dp_02` (chỉ để dựng dạng D2).
   Không dùng `admin`. Không tài khoản nào bị khoá → **không kích hoạt Rule 7**.

   | Tiêu chí | Kết quả | Bằng chứng |
   |---|:-:|---|
   | **P1** — mở lại được phiếu kiểm tra ở "Đang kiểm tra", đủ 6 hạng mục, đủ 3 lựa chọn kết luận | ✅ | Ở "Đã tiếp nhận" nút tên **[Kiểm tra hồ sơ]**; sau khi đã lưu kết quả, ở "Đang kiểm tra" nút tên **[Kiểm tra lại]** — bấm mở **cùng một phiếu** "Kiểm tra hồ sơ" (6 hạng mục C01→C06 + ô kết luận 3 lựa chọn) và lưu được. Ảnh `...-02-...png` |
   | **P2** — lưu kết luận Đạt được chấp nhận, đọc lại sau tải lại trang ra đúng chữ "Đạt" | ✅ | 1 request `POST /vu-viecs/{id}/kiem-tra` + 1 thông báo *"Kiểm tra hồ sơ đạt — sẵn sàng phân công"*; tải lại trang → vùng "Kết quả kiểm tra" hiện **Kết luận: Đạt** (thẻ xanh), không rỗng/`null`/chuỗi giữ chỗ. Ảnh `...-05-...png` |
   | **P3** — đọc được thành chữ **người kiểm tra** + **thời điểm kiểm tra**, đúng người, lệch ≤ 1 ngày, bền sau tải lại | ✅ | **Người kiểm tra: "CB Nghiệp vụ - Địa phương #01"** (khớp tên hiển thị `cbnv_dp_01`) · **Ngày kiểm tra: 06/08/2026 13:23**. Đồng hồ ghi trước khi bấm lưu = **13:23:05**, máy chủ trả `ngayKiemTra 2026-08-06T06:23:09.360Z` = 13:23:09 → **lệch 4 giây**. Vẫn còn sau tải lại trang. Ảnh `...-05-...png` |
   | **P4** — sau khi lưu Đạt vẫn là "Đang kiểm tra"; có thao tác phân công riêng; chỉ khi chọn người xử lý + xác nhận mới sang "Đã phân công" | ✅ | Ngay sau khi lưu Đạt: badge **"Đang kiểm tra"**, thanh tiến trình dừng bước 4, thanh hành động **[Phân công] + [Kiểm tra lại]** (ảnh `...-03-...png`); máy chủ `trangThai: DANG_KIEM_TRA`. Sau khi bấm [Phân công] → chọn NHT "QA NHT An Giang UAT2" → Xác nhận: badge đổi **"Đã phân công"**, tiến trình bước 5, `trangThai: DA_PHAN_CONG` (ảnh `...-06-...png`) |

   **Không điều nào trong F1→F7 xảy ra.** Riêng:
   - **F5** (Đạt tự nhảy sang "Đã phân công") — **không xảy ra**, đúng `:541` / `:564` / `:2288` và đúng quyết định BA 2026-07-16.
   - **F6** (người/thời điểm đóng băng ở lần lưu đầu) — **không xảy ra**: D2 trên VV-3, lần lưu đầu `cbnv_dp_01` **13:31**, sau khi `cbnv_dp_02` bấm [Kiểm tra lại] và lưu lại kết luận Đạt thì vùng "Kết quả kiểm tra" đổi sang **"CB Nghiệp vụ - Địa phương #02" / 06/08/2026 13:32** (ảnh `...-08-...png`). Máy chủ: `nguoiKiemTraId` đổi `e81aa51b…` → `7a4e1b00…`.
   - **F7** (nhánh khác Đạt không ghi người/thời điểm) — **không xảy ra**: D3 trên VV-2, kết luận **Yêu cầu bổ sung** + lý do, vùng "Kết quả kiểm tra" vẫn ghi đủ **Người kiểm tra "CB Nghiệp vụ - Địa phương #01"** + **Ngày kiểm tra 06/08/2026 13:28** (ảnh `...-07-...png`).

   **Ghi chú không chấm Fail (đã chốt trước ở mục 4, đo xong vẫn giữ nguyên):** nút mở phiếu **không**
   mang chữ "Hoàn tất kiểm tra" như `:1744` liệt kê, mà là **[Kiểm tra hồ sơ]** (ở "Đã tiếp nhận") /
   **[Kiểm tra lại]** (ở "Đang kiểm tra"). Nhãn là cách hiện thực; yêu cầu nghiệp vụ "có đường vào để CB NV
   ghi/sửa kết luận kiểm tra" **đã được đáp ứng** ⇒ chỉ ghi chú.
