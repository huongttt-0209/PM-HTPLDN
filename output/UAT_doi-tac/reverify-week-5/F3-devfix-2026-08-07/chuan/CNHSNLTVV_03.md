# Chuẩn chấm đã khóa — CNHSNLTVV_03 (dòng 36)

> **Nguồn khóa chuẩn:** khối `── CÁCH VERIFY sau Dev fix ──` trong
> [`batch-B7-tuvan-mangluoi-2026-08-06/bug-report.md`](../../../batch-B7-tuvan-mangluoi-2026-08-06/bug-report.md)
> entry `BUG-TVV-CNHSNLTVV-03` (dòng 471–646, khối verify ở 617–646).
> Ô *Kết quả verify* trên bảng ([audit/CNHSNLTVV_03-ketqua-verify-CU.md](../audit/CNHSNLTVV_03-ketqua-verify-CU.md))
> là **bản rút gọn**, KHÔNG phải chuẩn — xem §9.
> **Nguồn đặc tả duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.
> Mọi số dòng dưới đây đã **tự mở file đếm lại 2026-08-07**, không bê từ hồ sơ cũ.

---

## 1. Lỗi gốc (Expected/Actual của phiếu)

- **Ô *Kết quả mong đợi* của đối tác:** *"Thực hiện lưu lại dữ liệu đã cập nhật"*.
- **Ô *Kết quả thực tế* của đối tác:** *"Hệ thống hiển thị thông báo \"Lỗi hệ thống, vui lòng thử lại sau.\""*
- **Ô *Các bước*:** 1. Menu "Mạng lướt tư vấn viên" → "Tư vấn viên/Chuyên gia"; 2. Nhập dữ liệu hợp lệ.
  Ô *Điều kiện*: "1. Đăng nhập tài khoản". **Đối tác KHÔNG nói rõ trường nào** — GAP đã được đóng bằng cách
  chạy đủ 5 nhánh của form (không phải đoán).
- **Hiện trạng chốt ở vòng 06/08 (căn cứ Reopen):** *fix một phần*. **4/4 lượt lưu KHÔNG đính tệp → chạy được**;
  **3/3 lượt CÓ đính tệp ở khối "Thêm chứng chỉ mới" → hỏng**, đúng câu chữ đối tác báo, máy chủ trả
  **HTTP 500** `ERR-SYS-00-00-01`. Tải lại trang: **không ghi được gì**. Tách biến đã loại trừ được
  *tên tệp* và *hồ sơ* làm nguyên nhân; bỏ đúng một trường mang tệp (`chungChiMoiIds`) khỏi cùng thân
  yêu cầu thì **HTTP 200**.
- **Hệ quả kèm theo đã ghi nhận (không mở phiếu riêng):** lượt lưu hỏng **không gỡ tệp đã tải lên** ⇒ mỗi lần
  bấm lại sinh thêm một bản ghi tệp thừa trên hồ sơ.

---

## 2. Dẫn đặc tả (đã tự mở đếm lại)

**Kết luận kiểm số dòng:** `srs-fr-04-chuyen-gia-tvv.md` (2542 dòng) **KHÔNG lệch** — lần sửa gần nhất là
commit `9573284` **2026-08-04**; hai commit BA ngày **2026-08-06** (`8641b8b`, `2699898`) **không chạm** file này
(chỉ chạm `srs-fr-08/10/11/12/13/14/15` + `srs-v3.5.md`). Mọi trích dẫn cũ của case này giữ nguyên giá trị.

| Trích dẫn cũ | Trích dẫn ĐÚNG hiện tại | Nguyên văn dòng (cắt ≤200 ký tự) |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:433` (AC2) | ✅ **giữ nguyên `:433`** | `- **Given** NHT cập nhật thông tin/chứng chỉ + upload file **When** lưu **Then** validate và lưu thành công` |
| `:388` (`chung_chi_moi`) | ✅ **giữ nguyên `:388`** | `\| 6 \| chung_chi_moi \| binary[] \| N \| PDF, max 10MB/file, tổng 50MB, max 10 files \| — \| user upload \|` |
| `:402`–`:403` (§Processing 4-5) | ✅ **giữ nguyên `:402`–`:403`** | `:402` `\| 4 \| Cập nhật thông tin năng lực trong HO_SO_TU_VAN_VIEN \| — \|` · `:403` `\| 5 \| Nếu có file mới: tạo bản ghi FILE_DINH_KEM \| — \|` |
| `:418` (§Postconditions) | ✅ **giữ nguyên `:418`** | `- Hồ sơ năng lực được cập nhật` |
| `:425`–`:429` (§Error Handling E1–E5) | ✅ **giữ nguyên `:425`–`:429`** | `:425` `ERR-NL-01` khác đơn vị · `:426` `ERR-NL-02` "File tải lên tối đa 10MB/file" · `:427` `ERR-NL-03` "Tổng dung lượng file tối đa 50MB" · `:428` `ERR-NL-04` "File {ten_file} chứa mã độc, bị từ chối" · `:429` `ERR-NL-05` "Hồ sơ đã bị vô hiệu hóa, không thể chỉnh sửa" |
| `:432` (AC1 — im lặng về nhãn nút/khung) | ✅ **giữ nguyên `:432`** | `- **Given** NHT xem chi tiết TVV cùng đơn vị **When** nhấn "Cập nhật năng lực" **Then** form inline edit mở` |
| `:1576` (SCR-IV-03 thành phần 21) | ✅ **giữ nguyên `:1576`** | `\| 21 \| tab 3 \| Tab "Năng lực" \| … Nút "Cập nhật năng lực" → form sửa nhanh \| … \| Vai trò = **Người hỗ trợ** (TVV cùng đơn vị) …` |
| `:375` (Tác nhân) | ✅ **giữ nguyên `:375`** | `**Tác nhân:** Người hỗ trợ pháp lý (NHT)` |
| `:414` (Outputs `tvv_data`) | ✅ **giữ nguyên `:414`** | `\| 3 \| tvv_data \| object \| — \| Trả về các field đã cập nhật (để FE refresh UI readonly confirm) \|` |
| — (bổ sung mới đọc được) | `:405` | `\| 7 \| **Nếu TVV đang ở YEU_CAU_BO_SUNG và có cập nhật hồ sơ** → chuyển trạng thái về DANG_THAM_DINH + thông báo CB NV \| SM-TVV \|` |
| — (bổ sung mới đọc được) | `:1590` | `- **Bổ sung hồ sơ** (Yêu cầu bổ sung → Đang thẩm định): tự động kích hoạt khi **Người hỗ trợ** lưu thông tin năng lực mới (FR-IV-04). …` |

**Không có trích dẫn nào của case này phải sửa số dòng.**

---

## 3. Precondition + dữ liệu (vai trò / tài khoản / entity + trạng thái)

- **Môi trường:** `https://18.143.165.120.nip.io` (env **nội bộ**, KHÔNG phải env nghiệm thu
  `htpldn-uat.ospgroup.vn`) — theo `F3-devfix-2026-08-07/TIEN-DO.md`.
- **Tài khoản:** `nht_qa_tw` / `Test@1234` — vai trò **NHT** (Người hỗ trợ pháp lý), đơn vị *Cục Bổ trợ tư pháp -
  Bộ Tư pháp* (`00000000-0000-4000-8000-000000000001`), cấp **TW**. Đây là vai trò trùng khít huy hiệu `NHT`
  trên ảnh đối tác **và** là vai trò duy nhất đặc tả cho phép thao tác (`:375`, `:1576`).
  Dự phòng Rule 7 (cùng vai trò): `nht_qa_01` — **nhưng đơn vị Sở Tư pháp An Giang có 0 TVV**, gần như không dùng được.
- **Màn:** Mạng lưới Tư vấn viên → **Tư vấn viên / Chuyên gia** → mở hồ sơ (`/chuyen-gia-tvv/{id}`) →
  tab **"Năng lực"** → nút **[Cập nhật năng lực]**.
- **Dữ liệu phải có sẵn — 2 hồ sơ TVV/CG cùng đơn vị với tài khoản đo, 2 trạng thái khác nhau:**
  - (i) 1 hồ sơ **Đang hoạt động** — `TVV-BTP-TW-0002` (`98cfd963-3cd3-4c8a-bfa9-625460824d6d`).
  - (ii) 1 hồ sơ **Mới đăng ký** — `TVV-BTP-TW-0038` (`7c9107b3-9476-4aba-8225-3765ed848635`), QA đã tạo sẵn ở lô B7,
    **giữ lại cho dev tái hiện** ⇒ dùng lại được. Thiếu thì tạo bằng luồng chuẩn [Thêm mới] → hồ sơ tối thiểu → lưu.
- **Tệp:** 2 tệp PDF nhỏ (<1 MB) đã có sẵn trong
  [`batch-B7-tuvan-mangluoi-2026-08-06/seed-files/`](../../../batch-B7-tuvan-mangluoi-2026-08-06/seed-files/):
  `2K15 T3 (4.8) & CN (9.8).pdf` (tên có dấu cách + ngoặc đơn + `&`) và `B7-CNHSNLTVV03-chungchi-A.pdf`
  (+ `-chungchi-B.pdf`) (tên chỉ chữ/số/gạch nối).
- **Hoàn nguyên bắt buộc:** đo xong trả `TVV-BTP-TW-0002` về mốc gốc (Cử nhân · số năm trống · `STHN-QA-28` ·
  1 bằng cấp · 1 chứng chỉ nơi cấp "Bo Tu phap" · 4 lĩnh vực Thương mại/Thuế/Lao động/Đất đai · chỉ còn tệp
  `the-hanh-nghe-qa.pdf`) và **xóa mọi tệp thừa** do lượt lưu hỏng sinh ra.

---

## 4. Các bước đo (đánh số, thao tác UI thật)

0. Đăng nhập UI thật `nht_qa_tw` (mật khẩu → mã xác thực 6 số ở MailHog `http://18.143.165.120:8025`).
   **Tải lại trang** rồi ghi **bản dựng + bó mã FE** (chuỗi ở chân sidebar, `assets/index-*.js`,
   `GET /` last-modified + etag). So với `V1.0.8` / `assets/index-DIABnbIr.js` / `Thu, 06 Aug 2026 07:13:15 GMT`.
   **Trùng khít ⇒ báo điều phối TRƯỚC khi chốt verdict** (TIEN-DO.md §Cảnh báo 1: 6/6 dòng bị lật `Reopen → Fixed`
   mà 5/6 ô *DEV phản hồi lần 1* trống).
1. **Hồ sơ (i)** `TVV-BTP-TW-0002` → tab **Năng lực** → [Cập nhật năng lực] → **KHÔNG đính tệp**, chỉ sửa
   **Trình độ** + **Kinh nghiệm chi tiết** → [Lưu]. *(Lượt đối chứng — phải lưu được.)*
2. **Hồ sơ (i)** → mở lại form → khối **"Thêm chứng chỉ mới"** đính **tệp tên có ký tự đặc biệt**
   (`2K15 T3 (4.8) & CN (9.8).pdf`), ô **Ghi chú cập nhật = `a`** → [Lưu]. **Đọc nguyên văn thông báo hiện ra.**
3. **Hồ sơ (i)** → lặp bước 2 với **tệp tên thường** (`B7-CNHSNLTVV03-chungchi-A.pdf`).
4. **Hồ sơ (ii)** `TVV-BTP-TW-0038` → lặp **bước 1**, rồi **bước 2**, rồi **bước 3** (tệp `-chungchi-B.pdf`).
   ⇒ **Tổng 6 lượt bấm [Lưu]: 2 lượt không tệp + 4 lượt có tệp** (2 hồ sơ × 2 kiểu tên tệp).
5. **Sau MỖI lượt:** tải lại trang → mở lại tab **"Năng lực"** → đọc lại dữ liệu trên màn, đặc biệt khối
   **"Chứng chỉ hiện có"** (tệp vừa đính phải có mặt, đúng tên).
6. **Đếm thông báo:** cài `tools/toast-capture.js` **TRƯỚC khi bấm**, tự kiểm `soObserverDangSong = 1`;
   đếm theo **mốc giờ khác nhau** (không đếm số phần tử), **CẤM lọc trùng**, đếm **request ghi song song** số thông báo.
7. **Kiểm tệp thừa:** trước và sau mỗi lượt bấm, mở tab **"Hồ sơ"** → khối **"File đính kèm"** → đếm số tệp.

---

## 5. Đường đo thứ hai (đối chứng độc lập — không phải bấm lại cùng nút)

1. **Phản hồi máy chủ của chính lượt bấm [Lưu]** — `PATCH /api/v1/tu-van-viens/{id}/nang-luc`: đọc mã trạng thái
   + thân phản hồi. Vòng trước bắt được `500` / `{"success":false,"error":{"code":"ERR-SYS-00-00-01", …}}`.
2. **Đọc lại bản ghi qua máy chủ** (GET hồ sơ / danh sách tệp) rồi **so với những gì màn hình đang hiện**.
   Hai đường mâu thuẫn ⇒ **chưa được chốt**, phải ghi cả hai vào bug entry.
3. **Phép thử tách biến đã có tiền lệ (dùng khi vẫn còn hỏng):** gửi lại **đúng thân yêu cầu** của lượt hỏng
   nhưng **bỏ trường `chungChiMoiIds`**, giữ nguyên mọi trường khác, cùng bản ghi/cùng phiên → so mã phản hồi.
   Vòng 06/08: có trường → `500`; bỏ trường → `200`.
4. **Tách bước tải tệp khỏi bước lưu:** `POST /api/v1/tu-van-viens/{id}/files` vốn đã trả `201` — **không**
   dùng mã này để kết luận đã fix (xem §8).

---

## 6. ✅ PASS khi / ❌ FAIL nếu

> Chép **NGUYÊN VĂN** từ khối `── CÁCH VERIFY sau Dev fix ──` của entry `BUG-TVV-CNHSNLTVV-03`.

```
✅ PASS khi: đủ 6/6 lượt đều báo thành công VÀ sau khi tải lại trang, tệp vừa đính hiện trong khối
   "Chứng chỉ hiện có" của đúng hồ sơ đó với đúng tên tệp, VÀ phản hồi máy chủ của cả 6 lượt đều là
   thành công, VÀ mỗi lượt chỉ sinh đúng 1 thông báo (đếm theo mốc giờ khác nhau, không đếm số phần tử).
❌ FAIL nếu: bất kỳ lượt nào trong 6 lượt báo lỗi hoặc máy chủ trả lỗi — kể cả khi chỉ hỏng ở 1 trong 2
   kiểu tên tệp, hoặc chỉ hỏng ở 1 trong 2 hồ sơ. Cũng FAIL nếu báo thành công nhưng tải lại trang thì
   tệp không có trong "Chứng chỉ hiện có" (fix bề mặt).
```

---

## 7. Độ phủ biến thể bắt buộc (N bản ghi × M dạng, liệt kê từng dạng)

**Đã tra theo thứ tự bắt buộc:**
① **Chuẩn PASS đã khóa** — khối CÁCH VERIFY chốt cứng **6 lượt = 2 lượt không tệp + 4 lượt có tệp**, và câu
`❌ FAIL nếu` nêu đích danh 2 trục *"1 trong 2 kiểu tên tệp"* + *"1 trong 2 hồ sơ"*.
② **Mục SRS nói về nguồn dữ liệu** — `FR-IV-04 §Inputs :383`–`:393`: **11 trường, TẤT CẢ `Bắt buộc = N`**;
trường quyết định là `chung_chi_moi` (`:388`, PDF ≤10MB/tệp, tổng ≤50MB, ≤10 tệp). §Processing tách rõ 2 việc:
`:402` cập nhật `HO_SO_TU_VAN_VIEN` và `:403` *"Nếu có file mới: tạo bản ghi FILE_DINH_KEM"* — đúng ranh giới nhánh hỏng.
③ **Bộ lọc + enum trên màn** — tab "Năng lực" chỉ mở với vai trò **Người hỗ trợ** cùng đơn vị (`:1576`);
trạng thái hồ sơ là biến có thật vì `:405`/`:1590` cho phép lưu năng lực **đổi trạng thái** `Yêu cầu bổ sung → Đang thẩm định`.

**⇒ N = 2 bản ghi × M = 3 dạng = 6 lượt bấm [Lưu] (khớp đúng con số đã khóa):**

| Trục | Biến thể | Vì sao bắt buộc |
|---|---|---|
| N1 | Hồ sơ **Đang hoạt động** (`TVV-BTP-TW-0002`) | hồ sơ dev khai đã verify |
| N2 | Hồ sơ **Mới đăng ký** (`TVV-BTP-TW-0038`) | loại trừ "chỉ hỏng trên hồ sơ dev đã đụng" |
| M1 | **Không đính tệp** (sửa Trình độ + Kinh nghiệm chi tiết) | lượt đối chứng — nhánh vốn đã chạy, phải không bị fix làm hỏng |
| M2 | **Đính tệp tên có ký tự đặc biệt** (`2K15 T3 (4.8) & CN (9.8).pdf`) + ghi chú `a` | trùng khít cảnh trên ảnh đối tác |
| M3 | **Đính tệp tên thường** (`B7-CNHSNLTVV03-chungchi-A/B.pdf`) | tách biến tên tệp khỏi biến "có tệp" |

**KHÔNG mở rộng biến thể sang:** định dạng ngoài PDF (.doc/.xls/.jpg/.png) hay ngưỡng 20MB mà vùng kéo thả
đang khai — lệch `:388` thật, nhưng **đối tác không nêu** ⇒ ca biên, xử riêng, không kéo verdict case này.

---

## 8. ⚠️ Bẫy / rule chống kết luận oan

> 3 khối ⚠️ dưới đây chép **nguyên văn** từ khối CÁCH VERIFY:

```
⚠️ Đừng chấm Fail vì nhãn nút là "Lưu" thay vì "Đồng ý", vì form là inline thay vì hộp thoại, hay vì câu
   chữ cụ thể của thông báo THÀNH CÔNG — đặc tả srs-fr-04-chuyen-gia-tvv.md:432 không chốt những thứ đó.
   Cũng đừng chấm Fail khi hệ thống từ chối ĐÚNG theo :425-:429 (tệp quá 10MB, tổng quá 50MB, có mã độc,
   khác đơn vị, hồ sơ đã vô hiệu hóa) — đó là hành vi đúng.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy lượt lưu KHÔNG đính tệp chạy được — đó chính là hiện trạng đang
   Reopen, 4/4 lượt không tệp vốn đã chạy được từ trước. Phép đo quyết định là lượt CÓ đính tệp trong khối
   "Thêm chứng chỉ mới". Cũng đừng kết luận từ việc bước tải tệp lên trả về thành công: bước đó vốn đã chạy
   được, chỗ hỏng là lượt lưu ngay sau nó.
⚠️ Kiểm thêm sau khi fix: bấm lưu hỏng (nếu còn) không được để lại tệp thừa trên hồ sơ. Cách đọc: mở tab
   "Hồ sơ" → khối "File đính kèm", đếm số tệp trước và sau lượt bấm.
```

**Bẫy bổ sung (không nới điều kiện, chỉ chống đo sai):**

- **Không dùng `admin`** ra verdict (quyền rộng che lỗi phân quyền) — chỉ `nht_qa_tw`.
- **Trạng thái hồ sơ (ii) có thể tự đổi sau lượt lưu đầu tiên**: `:405`/`:1590` cho phép
  `Yêu cầu bổ sung → Đang thẩm định`. Nếu hồ sơ đang ở *Yêu cầu bổ sung* mà đổi trạng thái sau khi lưu ⇒
  **hành vi ĐÚNG**, không phải lỗi.
- **`TVV-BTP-TW-0002` từng bị QA đổi `loaiTvv` TVV→CG** (ghi ở `input/input.md:115-117`). Nếu case cần đúng
  loại TVV thuần thì phải kiểm lại trước khi kết luận về loại hồ sơ.
- **Đừng chấm bằng quan sát tĩnh** ("thấy thông báo xanh rồi") — mọi lượt phải **tải lại trang** đọc lại.

---

## 9. Đối chiếu khối note ↔ bug entry: GIỐNG / LỆCH (chi tiết)

**Kết luận: LỆCH ở mức RÚT GỌN — không mâu thuẫn, nhưng thiếu 3 điều kiện PASS và toàn bộ ⚠️ ⇒ đo theo note
có thể ra verdict khác ở ca biên. Chuẩn chấm = khối trong bug entry.**

| Hạng mục | Bug entry (chuẩn) | Ô *Kết quả verify* trên bảng | Đánh giá |
|---|---|---|---|
| Vai trò | NHT | NHT | **GIỐNG** |
| Tài khoản + mật khẩu + đơn vị | `nht_qa_tw` / `Test@1234`, Cục Bổ trợ tư pháp, cấp TW | *(không ghi)* | **LỆCH — thiếu**, không đổi verdict |
| Số lượt + cơ cấu | 6 lượt = 2 không tệp + 4 có tệp, đủ 2 kiểu tên tệp, 2 hồ sơ (Đang hoạt động / Mới đăng ký) | y hệt | **GIỐNG** |
| Điều kiện PASS "tệp hiện ở Chứng chỉ hiện có sau khi tải lại" | có | có | **GIỐNG** |
| Điều kiện PASS "phản hồi **máy chủ** của cả 6 lượt đều thành công" | có | *(không ghi)* | 🔴 **LỆCH — đổi được verdict**: fix bề mặt (UI xanh, máy chủ vẫn lỗi) sẽ Pass oan nếu chỉ theo note |
| Điều kiện PASS "mỗi lượt đúng 1 thông báo, đếm theo mốc giờ" | có | *(không ghi)* | 🔴 **LỆCH — đổi được verdict** (double-toast / gửi 2 lần lọt lưới) |
| Cảnh báo "chỉ lượt không tệp chạy được ⇒ chưa đạt" | có, kèm cả vế "đừng kết luận từ bước tải tệp trả 201" | có vế đầu, **thiếu** vế bước tải tệp | **LỆCH — thiếu một nửa** |
| ⚠️ Không Fail vì nhãn nút / form inline / câu chữ thông báo thành công (`:432`) | có | *(không ghi)* | 🔴 **LỆCH — đổi được verdict** theo hướng **Fail oan** |
| ⚠️ Không Fail khi hệ thống từ chối ĐÚNG theo `:425`–`:429` | có | *(không ghi)* | 🔴 **LỆCH — đổi được verdict** theo hướng **Fail oan** |
| ⚠️ Kiểm tệp thừa sau lượt lưu hỏng | có | *(không ghi)* | **LỆCH — thiếu**, là phép kiểm bổ sung |
| Bước 5 — đường đo thứ hai (đọc lại bản ghi qua máy chủ) | có | *(không ghi)* | **LỆCH — thiếu** |

**Ô "DEV phản hồi lần 1" trên bảng (chụp lúc bắt đầu lô):** dev khai *"ĐÃ VERIFY E2E PASS local + server 120
V1.0.6 (04/08/2026) … Không cần code/commit mới: happy-path đã được khắc phục bởi nhóm CNHSNLTVV_02"*.
Nội dung này **đề ngày 04/08 — TRƯỚC lượt Reopen 06/08**, và mô tả đúng nhánh **không đính tệp** (nhánh vốn đã
chạy). ⇒ **Không phải bằng chứng đã fix nhánh có tệp**, không được dùng để kế thừa verdict.

---

## 10. Cảnh báo cho agent đo

1. 🔴 **Đo bản dựng TRƯỚC TIÊN.** Nếu bó mã FE vẫn là `assets/index-DIABnbIr.js` / last-modified
   `Thu, 06 Aug 2026 07:13:15 GMT` thì **FE chưa deploy lại kể từ lượt Reopen 06/08** → **báo điều phối trước
   khi chốt verdict**. Lỗi này là **BE** (`PATCH …/nang-luc` → 500), nên FE-không-đổi *không* tự động kết luận
   được; vẫn phải đo thật, nhưng phải ghi rõ dấu vân tay vào báo cáo.
2. **Không đổi env.** Chuẩn này khóa cho `https://18.143.165.120.nip.io` (env nội bộ). Trên env nghiệm thu
   `htpldn-uat.ospgroup.vn`, tài khoản `nht_qa_tw` **không tồn tại / không dùng `Test@1234`**
   (`input/input.md:126-132`); vai trò NHT ở đó là `nht_04_ui`.
3. **Phép đo quyết định là lượt CÓ đính tệp.** 2 lượt không tệp chỉ là đối chứng chống hồi quy.
4. **Đủ 4 lượt có tệp** (2 hồ sơ × 2 kiểu tên) — bước 3 trong khối gốc viết tắt *"lặp cả bước 1 và bước 2 trên
   hồ sơ (ii)"*, nhưng tổng đã chốt là **6 lượt: 2 không tệp + 4 có tệp** và câu FAIL nêu cả 2 trục ⇒ hồ sơ (ii)
   cũng phải chạy **cả hai kiểu tên tệp**. Đừng dừng ở 5 lượt.
5. **Hoàn nguyên + dọn tệp thừa** trước khi đóng lượt đo, rồi **đọc lại bằng cả giao diện lẫn máy chủ**.
6. **Không quote số dòng từ hồ sơ cũ.** Số dòng `srs-fr-04-chuyen-gia-tvv.md` đã kiểm 2026-08-07 và **không lệch**;
   nếu cần trích thêm dòng khác thì **tự mở file đếm lại**.
