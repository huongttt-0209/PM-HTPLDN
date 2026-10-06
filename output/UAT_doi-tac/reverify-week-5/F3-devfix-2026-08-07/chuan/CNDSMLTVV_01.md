# Chuẩn chấm đã khóa — CNDSMLTVV_01 (dòng 37)

> **Nguồn khóa chuẩn:** khối `── CÁCH VERIFY sau Dev fix ──` trong
> [`batch-B7-tuvan-mangluoi-2026-08-06/bug-report.md`](../../../batch-B7-tuvan-mangluoi-2026-08-06/bug-report.md)
> entry `BUG-TVV-CNDSMLTVV-01` (dòng 650–831, khối verify ở 794–831).
> Ô *Kết quả verify* trên bảng ([audit/CNDSMLTVV_01-ketqua-verify-CU.md](../audit/CNDSMLTVV_01-ketqua-verify-CU.md))
> là **bản rút gọn thiếu vế cốt lõi** — xem §9, **KHÔNG dùng làm chuẩn**.
> **Nguồn đặc tả duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.
> Mọi số dòng dưới đây đã **tự mở file đếm lại 2026-08-07**.

---

## 1. Lỗi gốc (Expected/Actual của phiếu)

**Case gộp 2 vế** (ô *Kết quả mong đợi* của phiếu có 2 gạch đầu dòng):

- **Vế (1) — giao diện nhập.** Mong đợi: *"Hệ thống hiển thị cửa sổ nhập mô tả công khai (bắt buộc) áp cho các
  tư vấn viên đã chọn và xác nhận `Công khai {N} tư vấn viên đã chọn lên Cổng pháp luật quốc gia?`"*.
  Thực tế đối tác gặp: *"Hệ thống **không mở cửa sổ nhập** mà hiển thị thông báo `Mô tả công khai là bắt buộc
  trước khi đẩy lên Cổng pháp luật quốc gia`"*.
  → **Vòng 06/08: KHÔNG còn tái hiện** (3/3 lượt bấm đều mở đúng cửa sổ nhập, 0 thông báo chặn).
- **Vế (2) — kết quả nghiệp vụ.** Mong đợi: *"Lưu mô tả công khai, đặt cờ công khai, chuyển trạng thái công khai,
  ghi thời điểm."* (4 kết cục).
  → **Vòng 06/08: CÒN LỖI — đây là chỗ Reopen.** Hệ thống báo *"Đã công khai tư vấn viên thành công"* nhưng
  **tải lại trang thì hồ sơ vẫn "Chưa công khai"**, hỏng cả 4 kết cục. **Chỉ 1 hồ sơ trong lô bị máy chủ từ chối
  là cả lô bị hoàn tác**, kể cả hồ sơ mà chính máy chủ tự báo là thành công.
- **Dấu hiệu chung đã khoanh được:** hồ sơ **loại *Tư vấn viên* thiếu Số thẻ hành nghề** luôn bị máy chủ chặn
  (`CHK_tu_van_vien_tvv_so_the_hanh_nghe`); giao diện **không cảnh báo trước, không báo lỗi sau**, vỏ ngoài phản hồi
  vẫn là `HTTP 200 / success:true` trong khi bên trong `results[]` có phần tử `success:false`.
- **Ghi nhận phụ, KHÔNG kéo verdict:** câu thông báo thành công thực tế thiếu mã/tên đối tượng so với mẫu chuẩn
  (xem §2, dòng mẫu toast).

---

## 2. Dẫn đặc tả (đã tự mở đếm lại)

**Kết luận kiểm số dòng — 2 file, 2 kết quả khác nhau:**

- `srs-fr-04-chuyen-gia-tvv.md` (2542 dòng): **KHÔNG lệch**. Sửa gần nhất commit `9573284` **2026-08-04**;
  hai commit BA **2026-08-06** không chạm file này.
- 🔴 `srs-v3.5.md` (7012 dòng): **LỆCH +44**. BA sửa **2 lần ngày 2026-08-06** (`8641b8b` +19/−17, `2699898` +79/−35,
  net **+46 dòng**) ⇒ **mọi trích dẫn `srs-v3.5.md` trong hồ sơ cũ của case này đều SAI số dòng**.

| Trích dẫn cũ | Trích dẫn ĐÚNG hiện tại | Nguyên văn dòng (cắt ≤200 ký tự) |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:664` (§Processing bước 2) | ✅ **giữ nguyên `:664`** | `\| 2 \| Công khai: lưu mo_ta_cong_khai + file_dinh_kem_cong_khai (nếu có), đặt cong_khai = 1, chuyển trạng thái CONG_KHAI, auto fill thoi_gian_dang_tai. Cổng PLQG tự kéo … \| BR-PUBLIC-01 \|` |
| `:666` (§Processing bước 4) | ✅ **giữ nguyên `:666`** | `\| 4 \| Hỗ trợ thao tác hàng loạt \| — \|` |
| `:685` (§Postconditions) | ✅ **giữ nguyên `:685`** | `- TVV được đánh dấu công khai/ẩn (cong_khai = 1/0) + trạng thái CONG_KHAI/HUY_CONG_KHAI` |
| `:689` (AC1) | ✅ **giữ nguyên `:689`** | `- **Given** CB NV chọn TVV đang hoạt động **When** nhấn "Công khai" **Then** đặt cong_khai = 1 + trạng thái CONG_KHAI; Cổng PLQG tự kéo và hiển thị ở lần đồng bộ định kỳ kế tiếp` |
| `:1464` (SCR-IV-01 §Quy tắc tương tác) | ✅ **giữ nguyên `:1464`** | `- **Công khai hàng loạt** (tab "Đang hoạt động"): chọn nhiều dòng → nút "Công khai lên Cổng pháp luật quốc gia" → mở MD-CONG-KHAI → đặt \`cong_khai = 1\` + chuyển trạng thái Công khai cho các dòng đã chọn. Chỉ áp dụng cho dòng có trạng thái Đang hoạt động. …` |
| `:1406` (MD-CONG-KHAI) | ✅ **giữ nguyên `:1406`** | `\| MD-CONG-KHAI \| Công khai lên Cổng pháp luật quốc gia \| **Form nhập** trước khi xác nhận: (a) **Mô tả công khai** — text dài, **bắt buộc**, max 5000 ký tự …; (b) **File đính kèm** … tùy chọn …` |
| `:1564` (SCR-IV-03 tab Hồ sơ, nhóm (f)) | ✅ **giữ nguyên `:1564`** | `… (f) **Thông tin công khai** (chỉ hiển thị khi cong_khai=1: mô tả công khai + danh sách file đính kèm công khai + ngày đăng tải) \| — \| Luôn …` |
| `:645` (mô hình KÉO) | ✅ **giữ nguyên `:645`** | `**Mô tả:** Công khai / gỡ công khai TVV cá nhân VÀ Tổ chức tư vấn đã duyệt trên Cổng PLQG theo mô hình KÉO (PULL) … Phần mềm KHÔNG đẩy trực tiếp, KHÔNG gọi API ra Cổng. \`[CR-02]\`` |
| `:686` (Cổng kéo định kỳ) | ✅ **giữ nguyên `:686`** | `- Cổng PLQG hiển thị/ẩn TVV tương ứng sau lần kéo định kỳ kế tiếp` |
| `:681` (`ERR-CK-01`) | ✅ **giữ nguyên `:681`** | `\| E1 \| TVV không ở trạng thái CHO_KICH_HOAT/HOAT_DONG … \| ERR-CK-01 \| "Chỉ tư vấn viên đã được công nhận (Chờ kích hoạt hoặc Đang hoạt động) hoặc tổ chức đang hoạt động mới được công khai" \| ERROR \|` |
| `:682` (`ERR-CK-02`) | ✅ **giữ nguyên `:682`** | `\| E2 \| Thiếu mô tả công khai khi CONG_KHAI \| ERR-CK-02 \| "Mô tả công khai là bắt buộc trước khi công khai lên Cổng pháp luật quốc gia" \| ERROR \|` |
| `:647` · `:1420` (quyền CB NV) | ✅ **giữ nguyên** | `:647` `**Tác nhân:** CB NV (có quyền "Công khai mạng lưới tư vấn viên")` · `:1420` `- Cán bộ Nghiệp vụ: thêm/sửa/xóa, xuất Excel, công khai (TVV thuộc đơn vị)` |
| `:1465` (đường hoàn nguyên) | ✅ **giữ nguyên `:1465`** | `- **Hủy công khai hàng loạt** (tab "Đang hoạt động"): chọn dòng đã công khai → nút "Hủy công khai" → MD-HUY-CONG-KHAI → đặt \`cong_khai = 0\` + chuyển trạng thái Hủy công khai; Cổng tự ẩn ở lần kéo kế tiếp.` |
| `:1557` (nút Công khai màn chi tiết) | ✅ **giữ nguyên `:1557`** | `\| 10 \| header \| Nút **Công khai lên Cổng pháp luật quốc gia** … Click → MD-CONG-KHAI (form nhập mô tả + file đính kèm) → lưu mo_ta_cong_khai … đặt cong_khai = 1 + chuyển trạng thái Công khai, ghi thời g…` |
| `:1445` (ô chọn hàng loạt) | ✅ **giữ nguyên `:1445`** | `\| 17 \| bảng \| Ô chọn \| checkbox \| Chọn nhiều dòng cho thao tác hàng loạt \| — \|` |
| 🔴 `srs-v3.5.md:5685` (BR-PUBLIC-01) | 🔴 **`srs-v3.5.md:5729`** (tiêu đề mục ở `:5725`) | `\| BR-PUBLIC-01 \| Entity có quy trình (SM): chỉ bản ghi ở trạng thái cuối (Hoàn thành/Đã duyệt/Đã phản hồi/Đang hoạt động) mới được set cong_khai = 1. … Bản ghi bị Từ chối/Hủy: KHÔNG được công khai \|` |
| 🔴 `srs-v3.5.md:5697` (BR-PUBLIC-03) | 🔴 **`srs-v3.5.md:5741`** (tiêu đề mục ở `:5737`) | `\| BR-PUBLIC-03 \| Auto fill = thời điểm cuối cùng set cong_khai = 1. Không cho phép sửa tay \| CR-01 \| Tương tự BR-PUBLIC-01 \| — \| Test sửa tay thoi_gian_dang_tai = error \|` |
| 🔴 `srs-v3.5.md:6722` (mô hình KÉO C-INT-01) | 🔴 **`srs-v3.5.md:6766`** | `Áp dụng cho **mọi luồng công khai/hủy công khai** … **Mô hình KÉO (C-INT-01):** công khai = phần mềm đặt cờ \`cong_khai\`/\`la_cong_bo\` + trạng thái CONG_KHAI; Cổng PLQG tự kéo (PULL) định kỳ … Phần mềm KHÔNG gọi API đẩy/gỡ trực tiếp.` |
| 🔴 `srs-v3.5.md:6728` (mẫu toast công khai) | 🔴 **`srs-v3.5.md:6772`** | `\| Công khai thành công \| Toast success (auto-dismiss 4s) \| "Đã công khai {ten_doi_tuong} '{ma_hoac_ten}' lên Cổng Pháp luật Quốc gia." \| \`ten_doi_tuong\` …; \`ma_hoac_ten\` \|` |
| 🔴 `srs-v3.5.md:6729` (mẫu toast hủy công khai) | 🔴 **`srs-v3.5.md:6773`** | `\| Hủy công khai thành công \| Toast success (auto-dismiss 4s) \| "Đã hủy công khai {ten_doi_tuong} '{ma_hoac_ten}' khỏi Cổng Pháp luật Quốc gia." \| như trên \|` |
| — (**bổ sung mới đọc được, rất quan trọng**) | **`srs-fr-04-chuyen-gia-tvv.md:1507`** | `\| 3.5 \| nhóm 2 \| Số thẻ hành nghề \| ô văn bản \| Bắt buộc nếu Loại = Tư vấn viên (theo NĐ 77/2008 Đ.20) \| — \|` |
| — (bổ sung) | `srs-fr-04-chuyen-gia-tvv.md:663` | `\| 1 \| Kiểm tra đối tượng: TVV ở trạng thái CHO_KICH_HOAT HOẶC HOAT_DONG … \| SM-TVV, SM-TCTV \`[CR-02]\` \|` |
| — (bổ sung) | `srs-v3.5.md:5581` (BR-FLOW-02) | `\| BR-FLOW-02 \| **Phê duyệt hàng loạt:** CB PD có thể chọn nhiều bản ghi và phê duyệt hàng loạt (batch approve) \| … \| Từ chối phải từng bản ghi (yêu cầu lý do) \|` — **chỉ nói phê duyệt**, KHÔNG có quy tắc nguyên tử cho công khai hàng loạt |

**⇒ Nếu viết lại bug entry / ghi bảng: phải thay 5 số dòng `srs-v3.5.md` (5685→5729 · 5697→5741 · 6722→6766 ·
6728→6772 · 6729→6773). Nội dung các dòng KHÔNG đổi — chỉ dịch vị trí.**

---

## 3. Precondition + dữ liệu (vai trò / tài khoản / entity + trạng thái)

- **Môi trường:** `https://18.143.165.120.nip.io` (env **nội bộ**) — theo `F3-devfix-2026-08-07/TIEN-DO.md`.
- **Tài khoản:** `cbnv_tw_02` / `Test@1234` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), cấp **TW**,
  đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*. **Trùng khít vai trò + cấp + đơn vị đọc được trên ảnh đối tác,
  không nới chiều nào.** Quyền công khai theo `:647` + `:1420`.
  Dự phòng Rule 7 (cùng vai trò, cùng cấp): `cbnv_tw_03` / `Test@1234`.
- **Màn:** `/chuyen-gia-tvv/danh-sach` → tab **"Đang hoạt động"**.
- **Dữ liệu phải có sẵn — 3 hồ sơ *Đang hoạt động* + *Chưa công khai*, đủ 3 biến thể:**
  - (i) loại **Chuyên gia** — `CG-QLND38-UAT` (`38383838-…-038`).
  - (ii) loại **Tư vấn viên CÓ Số thẻ hành nghề** — `TVV-STP-AG-0001` (`4c1d3aab-db59-40f8-9a58-b8637c42d8ab`,
    số thẻ `THN-DP-2026-018`).
  - (iii) loại **Tư vấn viên KHÔNG có Số thẻ hành nghề** — `TVV-SEED-0001` (dự phòng `DDD-TVV-022`).
    **Biến thể quyết định.**
  - Thiếu biến thể nào → tự tạo qua [Thêm mới] → hồ sơ tối thiểu → đưa lên *Đang hoạt động*.
  - Hồ sơ nào đang *Công khai* → dùng chính nút **[Hủy công khai]** (`:1465`) đưa về *Chưa công khai* trước khi đo.
- **Hoàn nguyên bắt buộc:** mọi hồ sơ bị đổi cờ công khai phải gỡ về *Chưa công khai* bằng luồng [Hủy công khai],
  **làm từng hồ sơ một**, rồi tải lại trang đọc lại (cờ tắt + thời gian đăng tải rỗng).
  Chuỗi mô tả công khai QA nhập **sẽ còn lưu lại** — đúng `:1406` (*"mô tả + file vẫn được giữ lại để tái công khai sau"*),
  **không phải lỗi**, không gỡ được qua giao diện.
- **KHÔNG đo lượt công khai lại trên `TVV-BTP-TW-0002` / `DDD-TVV-021`** — sẽ ghi đè `thoi_gian_dang_tai` của bản ghi
  người khác đang giữ, mà BR-PUBLIC-03 (`srs-v3.5.md:5741`) cấm sửa tay ⇒ **không hoàn nguyên được**.

---

## 4. Các bước đo (đánh số, thao tác UI thật)

0. Đăng nhập UI thật `cbnv_tw_02` (mật khẩu → mã xác thực 6 số ở MailHog `http://18.143.165.120:8025`).
   Tải lại trang, ghi **bản dựng + bó mã FE + last-modified + etag**, so với `V1.0.8` /
   `assets/index-DIABnbIr.js` / `Thu, 06 Aug 2026 07:13:15 GMT`. **Trùng khít ⇒ báo điều phối trước khi chốt verdict.**
   Cài `tools/toast-capture.js` **TRƯỚC khi bấm**, tự kiểm `soObserverDangSong = 1`.
1. Tích **1 hồ sơ loại (iii)** (TVV không số thẻ) → **[Công khai lên Cổng PLQG]** → nhập mô tả bất kỳ → xác nhận.
   **Đọc NGUYÊN VĂN câu thông báo hiện ra**, rồi **TẢI LẠI TRANG** và đọc cột **"Công khai"** của đúng hồ sơ đó.
2. Tích **CÙNG LÚC 2 hồ sơ**: 1 cái loại (ii) + 1 cái loại (iii) → nhập mô tả → xác nhận → **tải lại trang** →
   **đếm xem MẤY TRÊN 2** hồ sơ thực sự chuyển sang *"Công khai"*.
3. Lặp bước 2 nhưng **chỉ tích riêng hồ sơ loại (ii)** — để biết hồ sơ đó tự nó có công khai được không.
4. Mở màn chi tiết **từng hồ sơ vừa thao tác** → tab **"Hồ sơ"** → đọc nhóm **"Thông tin công khai"**:
   phải có **đủ mô tả vừa nhập + thời gian đăng tải** (nhóm này chỉ hiện khi `cong_khai=1` — `:1564`).
5. Đo bằng **đường thứ hai** (xem §5).
6. **Đếm thông báo theo mốc giờ khác nhau** (không đếm số phần tử), **CẤM lọc trùng**, đếm **request ghi song song**.
   So nguyên văn chữ với ① `:682` (ca thiếu mô tả) ② mẫu `srs-v3.5.md:6772` ③ ô *Kết quả mong đợi* của đối tác.
7. **Hoàn nguyên** mọi hồ sơ đã đổi cờ (từng hồ sơ một, qua [Hủy công khai]) → tải lại trang đọc lại.

> *(Biến thể (i) Chuyên gia: dùng khi cần dựng tiền đề sạch cho nhánh "chọn hồ sơ ĐÃ công khai" — vòng trước
> phải đổi sang `CG-QLND38-UAT` vì hồ sơ TVV thiếu số thẻ làm nhiễu kết quả.)*

---

## 5. Đường đo thứ hai (đối chứng độc lập — không phải bấm lại cùng nút)

1. **Phản hồi máy chủ của chính lượt bấm xác nhận** — 🔴 **phải đọc TỪNG PHẦN TỬ trong danh sách kết quả
   `data.results[]`, không chỉ nhìn trạng thái chung**. Vòng 06/08 vỏ ngoài là `HTTP 200 / success:true`
   trong khi bên trong có `{"success":false,"error":"… violates check constraint
   \"CHK_tu_van_vien_tvv_so_the_hanh_nghe\""}`.
2. **Đọc lại từng bản ghi qua máy chủ** (`cong_khai`, `trang_thai`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`)
   rồi so với những gì màn hình đang hiện. **Hai đường mâu thuẫn ⇒ chưa được chốt.**
3. **Phép thử tách lô đã có tiền lệ:** chạy riêng từng hồ sơ trong lô (M2b = hồ sơ máy chủ báo thành công,
   M2c = hồ sơ máy chủ báo thất bại) để tách *"lỗi thuộc bản ghi"* khỏi *"lỗi thuộc cơ chế lô"*.
4. **Đối chứng mô tả:** mỗi lượt nhập **một chuỗi mô tả riêng** (có mốc giờ) — nếu đọc lại thấy chuỗi của lượt
   TRƯỚC thì đó là bằng chứng lô đã bị hoàn tác, không phải "chưa kịp cập nhật".

---

## 6. ✅ PASS khi / ❌ FAIL nếu

> Chép **NGUYÊN VĂN** từ khối `── CÁCH VERIFY sau Dev fix ──` của entry `BUG-TVV-CNDSMLTVV-01`.

```
✅ PASS khi: (a) với hồ sơ không đủ điều kiện, hệ thống báo TỪ CHỐI rõ hồ sơ nào không đạt và vì sao
   (KHÔNG được báo thành công), VÀ (b) với lô có lẫn hồ sơ hỏng, những hồ sơ hợp lệ còn lại vẫn phải
   được công khai đủ (hoặc hệ thống chặn cả lô nhưng NÓI RÕ là không hồ sơ nào được công khai), VÀ
   (c) mọi hồ sơ báo thành công đều đủ 4 kết cục sau khi tải lại: mô tả đúng nguyên văn · cờ công khai bật ·
   nhóm "Thông tin công khai" hiện ra · thời gian đăng tải bám đúng thời điểm bấm, VÀ (d) số hồ sơ chuyển
   sang "Công khai" sau khi tải lại đúng bằng số hồ sơ mà thông báo nói là đã công khai.
❌ FAIL nếu: báo thành công mà tải lại trang hồ sơ vẫn "Chưa công khai" — kể cả khi chỉ sai 1 hồ sơ trên 2;
   hoặc 1 hồ sơ hỏng vẫn kéo đổ những hồ sơ hợp lệ khác mà người dùng không được báo; hoặc người dùng
   không biết hồ sơ nào không đạt và vì sao; hoặc thời gian đăng tải trống dù cờ công khai đã bật.
```

---

## 7. Độ phủ biến thể bắt buộc (N bản ghi × M dạng, liệt kê từng dạng)

**Đã tra theo thứ tự bắt buộc:**
① **Chuẩn PASS đã khóa** — khối CÁCH VERIFY chốt **3 biến thể hồ sơ (i)(ii)(iii)** + **3 lượt bấm** (riêng (iii) ·
lô [(ii)+(iii)] · riêng (ii)), và ⚠️ cuối khối nêu đích danh *"Biến thể dễ bị bỏ sót: hồ sơ loại Tư vấn viên
KHÔNG có Số thẻ hành nghề"*.
② **Mục SRS nói về nguồn dữ liệu** — `FR-IV-08 §Inputs :653`–`:657`: `ref_type` ∈ {`TU_VAN_VIEN`, `TO_CHUC_TU_VAN`}
(**TO_CHUC_TU_VAN nằm ở màn khác, ngoài phiếu ⇒ không mở biến thể**); `hanh_dong` ∈ {`CONG_KHAI`, `HUY_CONG_KHAI`}
(HUY chỉ dùng để hoàn nguyên); `mo_ta_cong_khai` **bắt buộc nếu CONG_KHAI** (`:656`); `:663` trạng thái hợp lệ là
`CHO_KICH_HOAT` **HOẶC** `HOAT_DONG`.
③ **Bộ lọc + enum trên màn `SCR-IV-01`** — badge **Loại** chỉ có 2 giá trị *"Tư vấn viên"* / *"Chuyên gia"* (`:1449`);
ô chọn hàng loạt (`:1445`) + nút công khai hàng loạt **chỉ ở tab "Đang hoạt động"** (`:1464` — *"Chỉ áp dụng cho
dòng có trạng thái Đang hoạt động"*); cỡ lô: **1 dòng** và **≥2 dòng**.

**⇒ 3 dạng hồ sơ × 2 cỡ lô, gói vào 3 lượt bấm tối thiểu:**

| # | Biến thể bắt buộc | Bản ghi mẫu | Vì sao bắt buộc |
|---|---|---|---|
| V1 | **Chuyên gia**, *Đang hoạt động* + *Chưa công khai* | `CG-QLND38-UAT` | Loại KHÔNG dính ràng buộc số thẻ ⇒ tiền đề sạch, đối chứng "loại nào cũng chạy" |
| V2 | **Tư vấn viên CÓ Số thẻ hành nghề** | `TVV-STP-AG-0001` (`THN-DP-2026-018`) | Hồ sơ tự nó công khai được ⇒ chứng minh nó chỉ hỏng khi **đứng chung lô** |
| V3 | 🔴 **Tư vấn viên KHÔNG có Số thẻ hành nghề** | `TVV-SEED-0001` / `DDD-TVV-022` | **Biến thể quyết định** — chỉ đo V1/V2 sẽ thấy "chạy được" và **bỏ lọt toàn bộ lỗi** |
| L1 | Lô **1 dòng** (áp riêng V3, rồi riêng V2) | — | Tách *"lỗi thuộc bản ghi"* khỏi *"lỗi thuộc cơ chế lô"* |
| L2 | Lô **2 dòng lẫn hợp lệ + hỏng** (V2 + V3) | — | Ca "1 hồ sơ hỏng kéo đổ cả lô" |

**Nhánh ngược đặc tả nêu đích danh (đo để KHÔNG chấm oan, không phải để bắt lỗi):**
bỏ trống mô tả → phải bị chặn (`:682` `ERR-CK-02`); chọn hồ sơ **đã công khai** (`:1557` *AND chưa công khai*);
chọn hồ sơ **không ở "Đang hoạt động"** (`:681` `ERR-CK-01`, `:1464`).

---

## 8. ⚠️ Bẫy / rule chống kết luận oan

> 4 khối ⚠️ dưới đây chép **nguyên văn** từ khối CÁCH VERIFY:

```
⚠️ Đừng chấm Fail vì không thấy phần mềm gọi sang Cổng pháp luật quốc gia, hay vì Cổng chưa hiển thị
   ngay: đặc tả srs-fr-04-chuyen-gia-tvv.md:645 và :686 chốt mô hình KÉO — phần mềm chỉ đặt cờ, Cổng tự
   kéo định kỳ. Cũng đừng chấm Fail vì câu chữ của cửa sổ xác nhận hay nhãn nút, và đừng chấm Fail khi
   hệ thống từ chối ĐÚNG lúc bỏ trống mô tả (:682) hay khi hồ sơ không ở trạng thái cho phép (:681).
⚠️ Đừng kết luận "đã fix" khi chỉ thấy cửa sổ nhập mô tả mở ra được — phần đó vốn đã chạy đúng từ lượt đo
   06/08. Cũng đừng kết luận từ thông báo thành công, và đừng kết luận từ trạng thái chung của phản hồi
   máy chủ — hiện nay phản hồi báo "thành công" ở vỏ ngoài trong khi bên trong có hồ sơ thất bại.
   Phép đo quyết định là: TẢI LẠI TRANG rồi ĐẾM số hồ sơ thực sự đã chuyển sang "Công khai".
⚠️ Biến thể dễ bị bỏ sót: hồ sơ loại Tư vấn viên KHÔNG có Số thẻ hành nghề. Chỉ đo hồ sơ Chuyên gia hoặc
   hồ sơ có số thẻ thì sẽ thấy "chạy được" và bỏ lọt toàn bộ lỗi này.
⚠️ Kiểm thêm sau khi fix: lượt bấm hỏng (nếu còn) không được ghi đè mô tả công khai cũ của hồ sơ.
```

**Bẫy bổ sung (không nới điều kiện, chỉ chống đo sai / chấm oan):**

- 🔴 **KHÔNG được đòi hệ thống phải công khai được hồ sơ V3.** `srs-fr-04-chuyen-gia-tvv.md:1507` ghi
  *"Số thẻ hành nghề — Bắt buộc nếu Loại = Tư vấn viên (theo NĐ 77/2008 Đ.20)"* ⇒ ràng buộc phía máy chủ là
  **đúng đặc tả**. Vế FAIL của case **không phải** "chặn V3", mà là **báo thành công sai** + **không cho người
  dùng biết hồ sơ nào không đạt và vì sao** + **kéo đổ hồ sơ hợp lệ trong cùng lô**. Đọc kỹ vế (a) của ✅ PASS.
- **SRS IM LẶNG về tính nguyên tử của lô công khai.** `BR-FLOW-02` (`srs-v3.5.md:5581`) chỉ nói *phê duyệt* hàng loạt;
  `:666` chỉ ghi *"Hỗ trợ thao tác hàng loạt"*. Vì thế vế (b) của ✅ PASS **cố ý mở 2 nhánh** (công khai đủ phần hợp lệ,
  **hoặc** chặn cả lô nhưng nói rõ). **Không được siết về một nhánh**, cũng không được nới bỏ vế "nói rõ".
- **Câu thông báo thành công thiếu mã/tên đối tượng** so với mẫu `srs-v3.5.md:6772` — **ghi nhận, KHÔNG kéo verdict**
  (đối tác không nêu vế này).
- **Câu xác nhận `"Công khai {N} tư vấn viên đã chọn…?"`** — đặc tả chỉ dùng `{N}` ở `MD-PHE-DUYET-HANG-LOAT`
  (`:1412`), không có mẫu riêng cho công khai hàng loạt. Chỉ đo *có phản ánh đúng tập dòng đã chọn hay không*;
  **cấm** Fail vì không trùng từng chữ.
- **Tab khác không có ô chọn / không có nút công khai hàng loạt là ĐÚNG** `:1464`, dù `:663` cho phép cả
  `CHO_KICH_HOAT` — giới hạn nằm ở luồng hàng loạt của màn danh sách.
- **Không dùng `admin`** ra verdict.

---

## 9. Đối chiếu khối note ↔ bug entry: GIỐNG / LỆCH (chi tiết)

**Kết luận: 🔴 LỆCH NẶNG — ô *Kết quả verify* trên bảng thiếu vế cốt lõi (a) của điều kiện PASS và 2/3 lượt bấm.
Đo theo note sẽ Pass oan. Chuẩn chấm = khối trong bug entry, note chỉ là tóm tắt gửi dev.**

| Hạng mục | Bug entry (chuẩn) | Ô *Kết quả verify* trên bảng | Đánh giá |
|---|---|---|---|
| Tài khoản + vai trò + đơn vị | `cbnv_tw_02` / `Test@1234`, CB_NV_TW, Cục Bổ trợ tư pháp | *(không ghi)* | **LỆCH — thiếu** |
| Biến thể (i) **Chuyên gia** | có | *(không ghi)* | **LỆCH — thiếu**, mất đối chứng tiền đề sạch |
| Biến thể (ii) TVV có số thẻ · (iii) TVV không số thẻ | có | có (*"1 có số thẻ, 1 không"*) | **GIỐNG** |
| Bước 1 — tích **riêng** hồ sơ loại (iii) | có | *(không ghi)* | 🔴 **LỆCH — đổi được verdict**: không tách được *lỗi bản ghi* vs *lỗi cơ chế lô* |
| Bước 2 — lô 2 hồ sơ lẫn (ii)+(iii), đếm mấy/2 | có | có | **GIỐNG** |
| Bước 3 — tích **riêng** hồ sơ loại (ii) | có | *(không ghi)* | **LỆCH — thiếu**, mất phép đối chứng "hồ sơ tự nó hợp lệ" |
| Bước 4 — mở chi tiết đọc nhóm **"Thông tin công khai"** (mô tả + thời gian đăng tải) | có | *(không ghi)* | 🔴 **LỆCH — đổi được verdict**: cột "Công khai" bật mà mô tả rỗng / ngày đăng tải trống vẫn lọt |
| Bước 5 — đường đo thứ hai, đọc **từng phần tử** `results[]` | có | *(không ghi)* | 🔴 **LỆCH — đổi được verdict** |
| PASS (a) — **hồ sơ không đủ điều kiện phải bị báo TỪ CHỐI rõ hồ sơ nào + vì sao, KHÔNG được báo thành công** | có | 🔴 **KHÔNG có** | 🔴🔴 **LỆCH NẶNG — đây là vế cốt lõi của bug.** Bản fix chỉ "im lặng bỏ qua hồ sơ hỏng" sẽ **Pass oan** theo note |
| PASS (b) — hồ sơ hợp lệ trong lô lẫn vẫn phải công khai đủ, hoặc chặn cả lô **nhưng nói rõ** | có | *(không ghi, chỉ "đếm số hồ sơ")* | 🔴 **LỆCH — đổi được verdict** |
| PASS (c) — đủ **4 kết cục** sau khi tải lại | có | *(chỉ đếm cột "Công khai")* | 🔴 **LỆCH — đổi được verdict** |
| PASS (d) — số hồ sơ chuyển Công khai **đúng bằng** số thông báo nói đã công khai | có | *(không ghi)* | **LỆCH — thiếu** |
| "không tin thông báo, phải tải lại trang và đếm" | có | có | **GIỐNG** — vế duy nhất note giữ đúng |
| ⚠️ mô hình KÉO (`:645`/`:686`) · không Fail vì câu chữ · không Fail khi từ chối đúng `:681`/`:682` | có | *(không ghi)* | 🔴 **LỆCH — rủi ro Fail oan** |
| ⚠️ không ghi đè mô tả công khai cũ | có | *(không ghi)* | **LỆCH — thiếu** |

**Ô "DEV phản hồi lần 1" trên bảng:** **TRỐNG** ⇒ **không có mô tả fix nào của dev để kế thừa hay để đối chiếu**.
Trạng thái bảng vẫn bị lật `Reopen → Fixed`.

---

## 10. Cảnh báo cho agent đo

1. 🔴 **Đo bản dựng TRƯỚC TIÊN.** Nếu bó mã FE vẫn `assets/index-DIABnbIr.js` / last-modified
   `Thu, 06 Aug 2026 07:13:15 GMT` ⇒ **FE chưa deploy lại kể từ lượt Reopen 06/08** → **báo điều phối trước khi
   chốt verdict**. Case này có cả vế FE (bỏ qua `results[]` thất bại, vẫn báo thành công) lẫn vế BE (ràng buộc
   số thẻ / cơ chế lô) ⇒ FE-không-đổi là tín hiệu mạnh, nhưng **vẫn phải đo thật**, ghi rõ vân tay.
2. 🔴 **Số dòng `srs-v3.5.md` trong hồ sơ cũ đã SAI (+44).** Dùng `5729` (BR-PUBLIC-01) · `5741` (BR-PUBLIC-03) ·
   `6766` (mô hình KÉO) · `6772` (mẫu toast công khai) · `6773` (mẫu toast hủy công khai).
   Số dòng `srs-fr-04-chuyen-gia-tvv.md` **không lệch**, dùng nguyên.
3. **Phép đo quyết định:** TẢI LẠI TRANG rồi ĐẾM số hồ sơ thật sự chuyển *"Công khai"* — **cộng với** vế (a):
   người dùng có được cho biết hồ sơ nào không đạt và vì sao hay không.
4. **Không đòi công khai được hồ sơ V3** (TVV thiếu số thẻ) — `:1507` cho thấy ràng buộc là đúng đặc tả.
   Đòi sai chỗ = bug invalid, talk-past với dev.
5. **Không đổi env, không đổi vai trò/cấp/đơn vị.** Vòng 06/08 trùng khít 3 chiều với ảnh đối tác — nới chiều nào
   cũng làm mất giá trị đối chiếu. Dự phòng duy nhất: `cbnv_tw_03` (cùng vai trò + cấp).
6. **Hoàn nguyên từng hồ sơ một** qua [Hủy công khai] (`:1465`), tải lại trang đọc lại. Chuỗi mô tả công khai còn
   lưu lại là **đúng `:1406`**, đừng log thành bug.
