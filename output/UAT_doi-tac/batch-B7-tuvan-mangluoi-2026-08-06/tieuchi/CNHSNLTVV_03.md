# Tiêu chí chấm — CNHSNLTVV_03

```
Mã case: CNHSNLTVV_03 (tab `bug`, dòng 36 · Tuần 2)
Thời điểm viết: 2026-08-06 16:45   (viết TRƯỚC khi mở màn đang tranh chấp)
Môi trường verify: https://18.143.165.120.nip.io   (env NỘI BỘ, không phải env nghiệm thu của đối tác)
Bản dựng: HTPLDN · V1.0.8 · bó mã FE `assets/index-DIABnbIr.js` (+ `assets/index-DVlgOkLg.css`)
          · `GET /` last-modified `Thu, 06 Aug 2026 07:13:15 GMT` (14:13:15 giờ VN) · etag `W/"6a74340b-428"`
          (đọc lại SAU khi tải lại trang, đầu giai đoạn B — KHÁC V1.0.6/04-08 mà dev khai đã verify,
           và KHÁC V1.0.3 trong ảnh của đối tác)
```

> **Hồ sơ QA nội bộ đã đọc trước khi viết file này (khai theo flow 04 §Giai đoạn A):**
> `output/UAT_doi-tac/bug-con-fail-doi-tac-2026-07-31.md:341` (dòng tổng hợp cũ của chính case này) ·
> `output/UAT_doi-tac/input/input.md` (danh sách tài khoản) ·
> `output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/bug-report.md` (3 entry lô B7).
> **KHÔNG** lấy số đo cũ trong các file đó làm ngưỡng — mục 4 dưới đây suy từ đặc tả `srs-v3.5`.
> Ghi chú: hồ sơ cũ 31/07 mô tả case này bằng một câu **khác** ("màn chi tiết và màn cập nhật chưa đồng bộ
> dữ liệu"); bảng hiện tại (đọc 06/08) ghi triệu chứng là **"Lỗi hệ thống, vui lòng thử lại sau."** và
> ảnh của đối tác chụp 03/08 khớp câu mới ⇒ **chấm theo triệu chứng trên bảng + ảnh hiện tại**.

---

## 1. Đối tác phản ánh

**Một vế duy nhất (a):** Ở màn hồ sơ chi tiết tư vấn viên, khi người hỗ trợ pháp lý (NHT) **nhập dữ liệu
hợp lệ vào khối cập nhật năng lực rồi bấm lưu**, hệ thống **không lưu** mà hiện thông báo lỗi
*"Lỗi hệ thống, vui lòng thử lại sau."*

- Ô *Kết quả mong đợi* của phiếu: *"Thực hiện lưu lại dữ liệu đã cập nhật"*.
- Ô *Kết quả thực tế* của phiếu: *"Hệ thống hiển thị thông báo \"Lỗi hệ thống, vui lòng thử lại sau.\""*
- Ô *Các bước thực hiện*: 1. Chọn menu "Mạng lướt tư vấn viên" → "Tư vấn viên/Chuyên gia"; 2. Nhập dữ liệu
  hợp lệ. Ô *Điều kiện*: "1. Đăng nhập tài khoản".
- **Đối tác KHÔNG nói rõ "dữ liệu hợp lệ" là trường nào** ⇒ GAP phải đóng theo flow 04 §Đóng GAP:
  ① suy từ ảnh → ② test đủ mọi nhánh khả dĩ (mục 5).

**Bằng chứng đã mở XEM full-res:** [`partner-evidence/CNHSNLTVV_03.jpg`](../partner-evidence/CNHSNLTVV_03.jpg)
(1 ảnh tĩnh, không phải video). Đọc được trên ảnh:

| Vị trí trên ảnh | Nội dung đọc được |
|---|---|
| Thanh địa chỉ | `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/b88271a7-34a4-4c43-9133-71342ba73d3e` |
| Breadcrumb | `Trang chủ / Mạng lưới Tư vấn viên / Chi tiết` |
| Thông báo (đỏ, giữa trên) | **"Lỗi hệ thống, vui lòng thử lại sau."** |
| Nhãn khối đang mở | `Lĩnh vực pháp luật` → 9 thẻ đã chọn: Thuế · Lao động · Đất đai · Dân sự · Thương mại · Hành chính · Sở hữu trí tuệ · Doanh nghiệp · Đầu tư |
| Khối kế | `Chứng chỉ hiện có` → *"Chưa có chứng chỉ nào."* |
| Khối kế | `Thêm chứng chỉ mới (PDF, tối đa 10 file)` + vùng kéo thả ghi *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx, .jpg, .png. Dung lượng tối đa: 20MB/tệp."* |
| Hàng tệp đã đính | `2K15 T3 (4.8) & CN (9.8).pdf` — `(258.2 KB)` — 2 điều khiển `Xem` / `Xóa` |
| Khối kế | `Ghi chú cập nhật` = **`a`**, bộ đếm `1 / 2000` |
| Cuối form | 2 nút: `Làm lại` · **`Lưu`** |
| Góc phải trên | `BTP · DP` · chuông 4 thông báo · `hương 3 NHT` · huy hiệu **`NHT`** |
| Sidebar (chân logo) | `HTPLDN · V1.0.3`; menu đang ở `Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên ...` |
| Đồng hồ máy | `03:42 PM · 2026-08-03` |

⇒ **Màn tranh chấp xác định từ chính ảnh (không chỉ từ mô tả):** `SCR-IV-03` — *Hồ sơ chi tiết Tư vấn viên*,
đường dẫn `/chuyen-gia-tvv/:id`, **tab "Năng lực" / form Cập nhật năng lực** (`FR-IV-04`). Ảnh khớp mã case
`CNHSNLTVV` = *Cập nhật hồ sơ năng lực tư vấn viên* ⇒ **bằng chứng đúng case này**.

**3 dữ kiện neo của đối tác:**
`/chuyen-gia-tvv/b88271a7-34a4-4c43-9133-71342ba73d3e` (bản ghi trên env nghiệm thu) ·
hồ sơ **chưa có chứng chỉ nào**, đang chọn **9 lĩnh vực**, đang đính **1 tệp PDF 258,2 KB tên có dấu cách +
ngoặc đơn + dấu `&`**, ghi chú `a` ·
vai trò **NHT** (*hương 3 NHT*, đơn vị hiện `BTP · DP`) · env **`htpldn-uat.ospgroup.vn`** ·
bản dựng **`HTPLDN · V1.0.3`** · 03/08/2026 15:42.

---

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` (đã **mở file
đọc từng dòng**, không lấy số dòng từ trí nhớ).

| Dòng | Nguyên văn (trích) |
|---|---|
| `:367` | `### FR-IV-04: Cập nhật năng lực (UC42)` |
| `:371` | `**Màn hình:** SCR-IV-03 (Tab Năng lực)` |
| `:373` | `**Mô tả:** Người hỗ trợ pháp lý (NHT — cán bộ HTPL theo NĐ 55/2019 Đ.7) cập nhật thông tin năng lực của TVV/CG thuộc đơn vị mình. TVV/CG có thể đăng nhập chuyên trang xem hồ sơ của mình ở chế độ chỉ đọc, không sửa được.` |
| `:375` | `**Tác nhân:** Người hỗ trợ pháp lý (NHT)` |
| `:377` | `**Preconditions:** TVV tồn tại; NHT có quyền theo phân công vai trò + đơn vị (TVV cùng đơn vị với NHT).` |
| `:383`–`:393` | §Inputs — **11 trường, TẤT CẢ đều `Bắt buộc = N`**: `trinh_do` · `so_nam_kinh_nghiem` (>= 0) · `chuyen_nganh` · `bang_cap_chi_tiet` (JSON array) · `chung_chi_chi_tiet` (JSON array) · `chung_chi_moi` (`binary[]`, *PDF, max 10MB/file, tổng 50MB, max 10 files*) · `so_the_hanh_nghe` · `file_the_hanh_nghe` · `linh_vuc_ids` (*≥ 1 nếu thay đổi*) · `mo_ta_kinh_nghiem` (max 5000 ký) · `ghi_chu_cap_nhat` (max 2000 ký) |
| `:399`–`:406` | §Processing 8 bước: kiểm quyền NHT (BR-AUTH-01) → **xác nhận dữ liệu đầu vào** → quét virus ClamAV → **cập nhật `HO_SO_TU_VAN_VIEN`** → tạo `FILE_DINH_KEM` nếu có file mới → cập nhật `TVV_LINH_VUC` nếu đổi lĩnh vực → chuyển `YEU_CAU_BO_SUNG → DANG_THAM_DINH` nếu đang ở trạng thái đó → ghi nhật ký (BR-DATA-05) |
| `:412`–`:415` | §Outputs: `success` · `updated_at` · **`tvv_data` — "Trả về các field đã cập nhật (để FE refresh UI readonly confirm)"** · `trang_thai_moi` |
| `:418`–`:419` | §Postconditions: **"Hồ sơ năng lực được cập nhật"** · "Nhật ký thao tác ghi nhận thay đổi" |
| `:425`–`:429` | §Error Handling — **5 điều kiện lỗi ĐƯỢC PHÉP**, đều là lỗi *dữ liệu/quyền*: `ERR-NL-01` khác đơn vị · `ERR-NL-02` file > 10MB · `ERR-NL-03` tổng > 50MB · `ERR-NL-04` phát hiện mã độc · `ERR-NL-05` hồ sơ đã vô hiệu hóa |
| `:432` | AC1 — `**Given** NHT xem chi tiết TVV cùng đơn vị **When** nhấn "Cập nhật năng lực" **Then** form inline edit mở` |
| `:433` | AC2 — **`**Given** NHT cập nhật thông tin/chứng chỉ + upload file **When** lưu **Then** validate và lưu thành công`** ← **đúng điểm tranh chấp** |
| `:1576` | `SCR-IV-03` thành phần 21 — Tab "Năng lực": *"Bằng cấp chi tiết, Chứng chỉ chi tiết, Kinh nghiệm chi tiết. Nút 'Cập nhật năng lực' → form sửa nhanh"*; **Điều kiện hiển thị: `Vai trò = Người hỗ trợ (TVV cùng đơn vị)`** |
| `:1590` | §Quy tắc tương tác — *"**Bổ sung hồ sơ** (Yêu cầu bổ sung → Đang thẩm định): tự động kích hoạt khi **Người hỗ trợ** lưu thông tin năng lực mới (FR-IV-04)."* |

**Rẽ nhánh (flow 04 §Rẽ nhánh):** đặc tả **NÓI RÕ** và **KHỚP** kỳ vọng đối tác — `:433` yêu cầu *lưu thành
công*, `:418` yêu cầu *hồ sơ năng lực được cập nhật*; và bộ lỗi cho phép ở `:425`–`:429` **không có** ca
"lỗi hệ thống chung chung khi dữ liệu hợp lệ". ⇒ **Không phải nhánh cần BA. Viết mục 4 rồi đo bình thường.**

**IM LẶNG về:**
- Nhãn nút lưu (`Lưu` / `Đồng ý` / `Cập nhật`), dạng khung form (inline / drawer / hộp thoại) — `:432` chỉ
  nói *"form inline edit mở"*, không chốt nhãn nút hay kiểu khung.
- Nội dung chữ của **thông báo thành công** (đặc tả không quy định câu chữ nào cho ca lưu thành công).
- Việc giao diện có nhận thêm định dạng ngoài PDF hay không (nhãn vùng kéo thả trên ảnh của đối tác ghi
  `.doc/.docx/.xls/.xlsx/.jpg/.png` và `20MB/tệp`, lệch `:388` *PDF, max 10MB/file*) — **đối tác KHÔNG nêu
  vế này**, nên theo flow 04 §Ca biên phải xử **riêng**, không kéo verdict của case.

---

## 3. Precondition

- **Tài khoản:** `nht_qa_tw` / `Test@1234` — vai trò **NHT** (Người hỗ trợ pháp lý), đơn vị *Cục Bổ trợ tư
  pháp - Bộ Tư pháp*, cấp TW. Đây là **vai trò trùng khít đối tác** (ảnh: huy hiệu `NHT`) và cũng là vai trò
  DUY NHẤT đặc tả cho phép mở tab Năng lực (`:1576`) / thao tác FR-IV-04 (`:375`). *Lệch cấp/đơn vị so với
  đối tác (`BTP · DP`) — khai ở mục 6.*
  Dự phòng theo Rule 7 nếu đăng nhập fail: `nht_qa_01` (NHT, Sở Tư pháp An Giang) — nhưng đơn vị đó có 0 TVV.
- **Màn:** `https://18.143.165.120.nip.io/chuyen-gia-tvv/{id}` → tab **"Năng lực"** → nút *Cập nhật năng lực*.
- **Dữ liệu tiền đề:** ≥ **2 hồ sơ TVV/CG cùng đơn vị với `nht_qa_tw`**:
  (i) 1 hồ sơ **có sẵn** — ưu tiên `TVV-BTP-TW-0002` (chính hồ sơ dev khai đã verify);
  (ii) 1 hồ sơ **QA tự tạo mới** qua luồng chuẩn (Đăng ký TVV vào mạng lưới), để loại trừ khả năng "chỉ hồ
  sơ dev đụng vào thì mới lưu được".
- **Tệp dùng để tải lên:** ≥ 2 tệp PDF QA tự tạo, trong đó **1 tệp đặt tên có ký tự đặc biệt giống kiểu tên
  tệp của đối tác** (dấu cách, ngoặc đơn, dấu `&`, dấu chấm giữa tên).

---

## 4. Tiêu chí chấm

**✅ PASS khi — thoả ĐỦ 5 điều, ở MỌI lượt lưu dữ liệu hợp lệ (đủ M dạng × N hồ sơ):**

1. **Không có lượt hợp lệ nào bị hệ thống từ chối.** Không xuất hiện thông báo báo lỗi cho thao tác lưu dữ
   liệu hợp lệ; đặc biệt không xuất hiện câu *"Lỗi hệ thống, vui lòng thử lại sau."* hay bất kỳ câu lỗi chung
   chung nào không nêu lý do. (Đặc tả `:425`–`:429` chỉ cho phép từ chối trong 5 ca dữ liệu/quyền cụ thể.)
2. **Đếm theo mốc giờ khác nhau: đúng 1 thông báo cho 1 lượt bấm lưu**, và thông báo đó thuộc loại **thành
   công**; **1 request ghi** cho 1 lượt bấm (số request đếm song song số thông báo).
3. **Phản hồi máy chủ của chính lượt bấm đó là thành công** (không phải mã lỗi máy chủ 5xx / không phải phản
   hồi lỗi nghiệp vụ).
4. 🔴 **Tải lại trang rồi đọc lại**: mọi giá trị vừa nhập ở lượt đó **hiện đúng nguyên giá trị đã nhập** trên
   màn (trường chữ ra đúng chữ; lĩnh vực ra đúng tập đã chọn; tệp chứng chỉ mới có mặt trong danh sách chứng
   chỉ với đúng tên). — `:414` đòi trả về field đã cập nhật, `:418` đòi hồ sơ năng lực **được cập nhật**.
   **Chỉ thấy thông báo thành công thì CHƯA đủ để Pass.**
5. **Đường đo thứ hai khớp**: đọc lại bản ghi qua máy chủ cho ra đúng các giá trị đang hiển thị ở điều 4.
   Hai đường mâu thuẫn ⇒ chưa được chốt.

**❌ FAIL nếu — chỉ cần 1 trong các điều sau ở BẤT KỲ lượt hợp lệ nào:**

- Hiện thông báo lỗi (kể cả chỉ 1/N lượt) khi dữ liệu nhập hợp lệ theo ràng buộc `:383`–`:393`.
- Phản hồi máy chủ là lỗi (5xx hoặc lỗi nghiệp vụ) cho lượt bấm lưu hợp lệ.
- Báo thành công nhưng **tải lại trang thì dữ liệu không đổi / mất** ⇒ fix bề mặt, vẫn là FAIL.
- Lưu được nhánh này nhưng **hỏng nhánh khác** trong cùng form (vd chỉ hỏng khi có tệp đính kèm) — đây chính
  là ca "fix một phần".

**KHÔNG được chấm Fail vì (đặc tả im lặng / ngoài vế đối tác nêu):**

- Nút mang nhãn `Lưu` hay `Đồng ý`; form là inline hay drawer (`:432` không chốt).
- Câu chữ cụ thể của thông báo **thành công** (đặc tả không quy định).
- Hệ thống **từ chối đúng** khi dữ liệu KHÔNG hợp lệ (file > 10MB, sai đơn vị, hồ sơ đã vô hiệu hóa…) —
  đó là `:425`–`:429`, là hành vi đúng.
- Vùng kéo thả nhận thêm định dạng ngoài PDF / ghi 20MB thay vì 10MB — **vế đối tác không nêu**, xử riêng
  theo flow 04 §Ca biên, không kéo verdict.
- Trạng thái hồ sơ tự chuyển `Yêu cầu bổ sung → Đang thẩm định` sau khi lưu — đó là hành vi **đúng** `:405`.

---

## 5. Dạng dữ liệu phải phủ

**Nguồn xác định M** (theo flow 04 §Xác định M, tra theo thứ tự): ① `FR-IV-04 §Inputs` `:383`–`:393` liệt kê
**đóng 11 trường** — đây là toàn bộ nguồn dữ liệu mà thao tác này nhận; ② bộ điều khiển thật trên màn (đọc từ
ảnh đối tác: multi-select lĩnh vực · danh sách chứng chỉ · vùng tải tệp · ô ghi chú). Không cần tới ③ (hỏi dev).

**M = 5 dạng thao tác lưu** (mỗi dạng là một nhánh khả dĩ của cụm chữ mơ hồ *"nhập dữ liệu hợp lệ"*):

| # | Dạng | Trường tương ứng §Inputs |
|---|---|---|
| M1 | Chỉ sửa **trường chữ / số**, không đụng tệp, không đổi lĩnh vực | `trinh_do` · `so_nam_kinh_nghiem` · `chuyen_nganh` · `so_the_hanh_nghe` · `mo_ta_kinh_nghiem` · `ghi_chu_cap_nhat` |
| M2 | **Đổi lĩnh vực pháp luật** (thêm + bớt thẻ) | `linh_vuc_ids` (`:391`) |
| M3 | **Danh sách chi tiết** — thêm / sửa / xoá mục bằng cấp & chứng chỉ | `bang_cap_chi_tiet` · `chung_chi_chi_tiet` (`:386`, `:387`) |
| M4 | **Tải lên tệp chứng chỉ mới** — trong đó **≥1 lượt dùng tên tệp có ký tự đặc biệt** giống kiểu tên tệp đối tác dùng (`2K15 T3 (4.8) & CN (9.8).pdf`) | `chung_chi_moi` (`:388`) |
| M5 | **Kết hợp đồng thời đúng như ảnh đối tác**: 9 lĩnh vực + 1 tệp PDF chứng chỉ + ghi chú ngắn `a` | `linh_vuc_ids` + `chung_chi_moi` + `ghi_chu_cap_nhat` |

**N = 2 hồ sơ:** (i) hồ sơ **có sẵn** `TVV-BTP-TW-0002` · (ii) hồ sơ **QA tự tạo mới** qua luồng chuẩn.
Mọi nhánh cùng kết quả ⇒ GAP *"dữ liệu hợp lệ là trường nào"* được coi là **đóng**, và phải ghi rõ đã thử
những nhánh nào.

---

## 6. Bảng điều kiện — đóng GAP

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Vai trò **NHT** (*hương 3 NHT*), đơn vị hiển thị `BTP · DP` | `nht_qa_tw` — **NHT** (trùng khít vai trò; `/auth/me` trả `vaiTro ["NHT"]`), đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*, cấp **TW**. **Đã nới cấp/đơn vị, giữ nguyên vai trò** — lý do: `:1576` cho phép mở tab Năng lực theo *vai trò* (Người hỗ trợ, TVV cùng đơn vị), còn cấp chỉ quyết định phạm vi dữ liệu; env nội bộ **không có** TVV nào thuộc đơn vị cấp ĐP để đo. Không có lượt đăng nhập fail, không phải fallback Rule 7 | **Không** — vai trò quyết định bộ nút + luồng xử lý đã trùng khít; lỗi tái hiện ở chính vai trò đối tác dùng |
| Entity + trạng thái | Hồ sơ TVV/CG `b88271a7-…` trên env nghiệm thu; tab Năng lực; **chưa có chứng chỉ nào** | 2 hồ sơ, cùng đơn vị với tài khoản đo, cùng tab Năng lực, cả hai đều **"Chứng chỉ hiện có → Chưa có chứng chỉ nào."** giống ảnh đối tác: (i) `TVV-BTP-TW-0002` *Đang hoạt động* — hồ sơ CÓ SẴN, đúng hồ sơ dev khai đã verify; (ii) `TVV-BTP-TW-0038` *Mới đăng ký* — hồ sơ **QA tự tạo mới** | **Không** — phủ cả 2 trạng thái hồ sơ, kết quả giống hệt nhau |
| Dữ liệu tiền đề | 9 lĩnh vực đã chọn sẵn; 1 tệp PDF 258,2 KB đang đính; ghi chú `a` | Dựng lại đúng cảnh đó: lĩnh vực đã chọn sẵn (5 thẻ) + **1 tệp PDF đính trong vùng "Thêm chứng chỉ mới"** + ghi chú `a`. Tệp dùng đúng tên đối tác `2K15 T3 (4.8) & CN (9.8).pdf`; thêm 2 tệp tên thường để tách biến | **Không** — tiền đề tạo được và đã tạo bằng chính luồng chuẩn |
| Input / filter / giá trị nhập | **Không nói rõ trường nào** — chỉ ghi *"Nhập dữ liệu hợp lệ"*; ảnh cho thấy có đổi lĩnh vực + đính tệp + ghi chú | Đã **test đủ 5 nhánh khả dĩ** của cụm chữ mơ hồ đó (M1 trường chữ/số · M2 lĩnh vực · M3 bằng cấp+chứng chỉ chi tiết · M4 tải tệp chứng chỉ mới · M5 kết hợp như ảnh) trên 2 hồ sơ = **7 lượt bấm [Lưu] thật**. Kết quả **tách bạch**: 4/4 lượt KHÔNG đính tệp → lưu được; **3/3 lượt CÓ đính tệp → hỏng**. Tách thêm biến tên tệp: tên có ký tự đặc biệt và tên thường đều hỏng như nhau | **Không** — GAP đóng bằng test đủ nhánh, không đoán. Nhánh gây lỗi xác định được đích danh: **đính tệp chứng chỉ mới** |
| Độ phủ biến thể (N bản ghi, M dạng) | 1 lần bấm lưu, 1 hồ sơ | **N = 2 hồ sơ × M = 5 dạng = 7 lượt bấm [Lưu] thật** + 1 lượt đối chứng máy chủ (gửi lại đúng thân yêu cầu nhưng bỏ trường tệp → 200). Mọi lượt đều tải lại trang đọc lại dữ liệu, không chấm bằng quan sát tĩnh | **Không** |

**3 dữ kiện neo của đối tác:** `/chuyen-gia-tvv/b88271a7-34a4-4c43-9133-71342ba73d3e` ·
hồ sơ chưa có chứng chỉ, 9 lĩnh vực, 1 tệp PDF 258,2 KB tên có ký tự đặc biệt, ghi chú `a` ·
vai trò **NHT** · env **`htpldn-uat.ospgroup.vn`** · bản dựng **`HTPLDN · V1.0.3`** · 03/08/2026 15:42.

**Giới hạn hiệu lực (KHÔNG phải GAP):** đo trên env **nội bộ** `18.143.165.120.nip.io` và bản dựng ghi ở đầu
file — **khác env + khác bản dựng** với ảnh của đối tác (`htpldn-uat.ospgroup.vn`, `V1.0.3`). Dev khai verify
trên **V1.0.6 ngày 04/08**, cũng khác bản dựng đang đo ⇒ **không kế thừa kết quả của dev**, đo lại từ đầu.

---

## 7. Sửa đổi tiêu chí (ghi bổ sung nếu có, kèm mốc giờ)

**2026-08-06 17:35 — bổ sung nhánh M4b, KHÔNG nới lỏng mục 4.**
Mục 5 bản gốc gộp *"tải tệp chứng chỉ mới, ≥1 lượt dùng tên tệp có ký tự đặc biệt"* thành một dạng
(M4). Khi đo thấy M4 hỏng, nếu dừng ở đó thì không phân biệt được *"hỏng vì tên tệp"* với
*"hỏng vì có tệp"* — mà hai kết luận này dẫn dev đi sửa hai chỗ khác nhau. Vì vậy tách M4 thành
**M4** (tên tệp có ký tự đặc biệt, trùng khít đối tác) và **M4b** (tên tệp chỉ chữ/số/gạch nối),
chạy cả hai. Đây là **thêm phép đo**, ngưỡng PASS/FAIL ở mục 4 giữ nguyên từng chữ.

**2026-08-06 17:35 — kết quả chấm.** Mục 4 đòi thoả ĐỦ 5 điều ở MỌI lượt lưu hợp lệ.
Điều 1 (không lượt hợp lệ nào bị từ chối) **không thoả** ở 3/7 lượt; điều 3 (phản hồi máy chủ
thành công) **không thoả** ở đúng 3 lượt đó (HTTP 500); điều 4 (tải lại trang đọc lại dữ liệu)
**không thoả** ở 3 lượt đó (không có gì được ghi). Điều 2 và 5 thoả ở mọi lượt.
⇒ Rơi đúng dòng `❌ FAIL nếu` ca **"lưu được nhánh này nhưng hỏng nhánh khác trong cùng form"**
= *fix một phần* ⇒ **Reopen**.
