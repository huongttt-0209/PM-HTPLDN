# Nhật ký đo lại — CNHSNLTVV_03 (dòng 36) · R5 "lấp GAP" · 2026-08-07

**Chuẩn chấm:** [`chuan/CNHSNLTVV_03.md`](../chuan/CNHSNLTVV_03.md) — khối `✅ PASS khi / ❌ FAIL nếu` **KHÔNG sửa, không nới**.
**Phạm vi được giao:** đúng **4 lượt** lấp 3 GAP mà R4 để lại (GAP-1 · GAP-2 · GAP-3). **Không mở rộng biến thể.**
**Lượt đo trước:** [`do/CNHSNLTVV_03-R4-dobanmoi.md`](CNHSNLTVV_03-R4-dobanmoi.md) (R4, 2 lượt có tệp, cùng bó mã).

**Verdict đề xuất: ✅ PASS cho CẢ PHIẾU** — khối khóa nay đủ 6/6 lượt (R4 2 lượt + R5 4 lượt), không lượt nào FAIL. Chi tiết §7.

---

## 1. Vân tay bản dựng — ĐẦU và CUỐI phiên

| Hạng mục | **ĐẦU phiên** (2026-08-06 19:52:38 GMT) | **CUỐI phiên** (2026-08-06 20:02:13 GMT) | Đổi? |
|---|---|---|---|
| Bó mã `GET /` | `assets/index-D4Buvu4S.js` | `assets/index-D4Buvu4S.js` | **không** |
| Bó mã thực tải trong tab | `assets/index-D4Buvu4S.js` | `assets/index-D4Buvu4S.js` | **không** |
| CSS | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` | **không** |
| `last-modified` của `GET /` | `Thu, 06 Aug 2026 19:23:01 GMT` | `Thu, 06 Aug 2026 19:23:01 GMT` | **không** |
| `etag` của `GET /` | `W/"6a74df15-428"` | `W/"6a74df15-428"` | **không** |
| Nhãn chân sidebar | `HTPLDN · V1.0.9` | `HTPLDN · V1.0.9` | **không** |

### 🔴 Điều kiện tiên quyết — ĐÃ KIỂM TRƯỚC MỌI VIỆC KHÁC

Vân tay lấy ở **bước đầu tiên**, trước khi thao tác gì:

| | R4 (lượt trước) | **R5 (lượt này)** | Khớp? |
|---|---|---|---|
| Bó mã | `assets/index-D4Buvu4S.js` | `assets/index-D4Buvu4S.js` | ✅ |
| `last-modified` | `Thu, 06 Aug 2026 19:23:01 GMT` | `Thu, 06 Aug 2026 19:23:01 GMT` | ✅ |
| `etag` | `W/"6a74df15-428"` | `W/"6a74df15-428"` | ✅ |

➡️ **TRÙNG KHÍT R4 ⇒ được phép đo tiếp.** Đầu phiên = cuối phiên ⇒ **toàn bộ 4 lượt R5 và 2 lượt R4 thuộc CÙNG MỘT bó mã**
`index-D4Buvu4S.js` (19:23:01 GMT). Không có quan sát nào rơi trước/sau một mốc deploy nào ⇒ **ghép R4+R5 thành một verdict là hợp lệ**.

---

## 2. Tài khoản + hồ sơ đã dùng

- **Đăng nhập lại từ đầu bằng giao diện thật** `nht_qa_tw` / `Test@1234` (mã 6 số lấy ở MailHog `http://18.143.165.120:8025`,
  hộp thư `nht.qa.tw@htpldn.test`). Đã **đăng xuất + xóa `localStorage`/`sessionStorage`** phiên cũ trước khi đăng nhập
  để không thừa hưởng phiên của lượt đo trước. Không fallback tài khoản, **không dùng `admin`**.
- `GET /api/v1/auth/me` → `hoTen "QA NHT Trung uong"` · `vaiTro ["NHT"]` · `donViId 00000000-0000-4000-8000-000000000001`
  (Cục Bổ trợ tư pháp) · `capDonVi "TW"` · `userId a31689a8-019e-40ff-b084-58f55589b694` ⇒ trùng khít chuẩn chấm §3.
- Môi trường `https://18.143.165.120.nip.io` (env nội bộ) — **không đổi env**.
- **Điều hướng bằng click menu bên trái + click hàng trong danh sách** (không gõ thẳng URL), đúng thao tác người dùng.

**Trạng thái 3 hồ sơ lúc BẮT ĐẦU R5** (đọc từ máy chủ) — khớp y hệt trạng thái R4 để lại, không có ai đụng vào giữa 2 lượt đo:

| Hồ sơ | ID | Loại · Trạng thái | version | Số chứng chỉ | Số tệp đính kèm |
|---|---|---|---|---|---|
| `TVV-BTP-TW-0002` | `98cfd963-3cd3-4c8a-bfa9-625460824d6d` | CG · **Đang hoạt động** | 28 | 2 | 2 (`cc120.pdf`, `the-hanh-nghe-qa.pdf`) |
| `TVV-BTP-TW-0038` | `7c9107b3-9476-4aba-8225-3765ed848635` | TVV · Mới đăng ký | 6 | 2 | 2 |
| `TVV-BTP-TW-0037` | `f179382a-2033-48da-adcb-cd631179d0a3` | TVV · Mới đăng ký | 3 | 1 | 3 |

**Bộ đếm thông báo:** dán `tools/toast-capture.js` **TRƯỚC MỖI lượt bấm [Lưu]**, tự kiểm `soObserverDangSong`
(**4/4 lượt đều = 1**), **KHÔNG lọc trùng**, đọc bằng `innerText`, đếm **request ghi song song** số thông báo.

---

## 3. Bốn lượt đo (quan sát thô từng lượt)

> Mỗi lượt: cài bộ đếm → tự kiểm → bấm [Lưu] → đọc thông báo + mã phản hồi → **tải lại trang** → mở tab "Năng lực"
> đọc dòng **"Chứng chỉ chi tiết"** → **bấm lại [Cập nhật năng lực]** xem form có mở lại được không.

### 3.1 Lượt 1 — `TVV-BTP-TW-0002` · **KHÔNG đính tệp** *(lấp GAP-1a **và** GAP-3)*

Hồ sơ **Đang hoạt động** — đây chính là trục N1 mà R4 mới chỉ *mở* được form, chưa từng bấm [Lưu].

| Bước | Quan sát thô |
|---|---|
| Bấm [Cập nhật năng lực] | ✅ form inline **MỞ RA**; "Chứng chỉ hiện có": `cc120.pdf [Xóa]`; URL giữ `/chuyen-gia-tvv/98cfd963-…`, **không** đá `/403` |
| Sửa **Trình độ** `Cử nhân` → `Thac si`; **Kinh nghiệm chi tiết** thêm `QA R5 GAP-1a khong dinh tep tren ho so Dang hoat dong 2026-08-07`; **Ghi chú cập nhật** = `a`. **Không đính tệp nào.** | vùng "Thêm chứng chỉ mới" để trống |
| `soObserverDangSong` | **1** ✅ |
| Bấm **[Lưu]** | `SO_REQUEST = 1` → `PATCH /api/v1/tu-van-viens/98cfd963-…/nang-luc` → **200** (reqid 256)<br>`SO_KHUNG_THONG_BAO = 1` · `khoangCachMs = null` · `BI_LAP = false`<br>**Nguyên văn thông báo: "Cập nhật năng lực thành công"** (loại: toast tự tắt ~3s) |
| **Tải lại trang** → tab "Năng lực" | `Trình độ  Thac si` ✅ đã ghi<br>`Chứng chỉ chi tiết:` `Chung chi hanh nghe Luat su — Bo Tu phap — cấp 15/03/2012` + **`cc120.pdf`** ⇒ **tệp cũ CÒN NGUYÊN** |
| Bấm lại [Cập nhật năng lực] | ✅ **form MỞ LẠI ĐƯỢC**; "Chứng chỉ hiện có" vẫn liệt kê `cc120.pdf [Xóa]` |
| Số tệp trước/sau lượt | **2 → 2** (không mất, không sinh tệp thừa) |

➡️ **Lượt đối chứng ĐẠT trên hồ sơ *Đang hoạt động*: lưu được, và KHÔNG làm mất tệp đang có.**

### 3.2 Lượt 2 — `TVV-BTP-TW-0038` · **KHÔNG đính tệp** *(lấp GAP-1b)*

| Bước | Quan sát thô |
|---|---|
| Bấm [Cập nhật năng lực] | ✅ form MỞ RA; "Chứng chỉ hiện có": `2K15 T3 (4.8) & CN (9.8).pdf [Xóa]` · `B7-CNHSNLTVV03-chungchi-B.pdf [Xóa]` |
| Sửa **Trình độ** `Thạc sĩ` → `Tien si`; **Kinh nghiệm chi tiết** → `QA R5 GAP-1b khong dinh tep tren ho so Moi dang ky 2026-08-07`; **Ghi chú** = `a`. **Không đính tệp.** | — |
| `soObserverDangSong` | **1** ✅ |
| Bấm **[Lưu]** | `SO_REQUEST = 1` → `PATCH /api/v1/tu-van-viens/7c9107b3-…/nang-luc` → **200** (reqid 396)<br>`SO_KHUNG_THONG_BAO = 1` · `khoangCachMs = null` · `BI_LAP = false`<br>**Nguyên văn: "Cập nhật năng lực thành công"** |
| **Tải lại trang** → tab "Năng lực" | `Trình độ  Tien si` ✅<br>`Chứng chỉ chi tiết:` `2K15 T3 (4.8) & CN (9.8).pdf` + `B7-CNHSNLTVV03-chungchi-B.pdf` ⇒ **2 tệp cũ CÒN NGUYÊN** |
| Bấm lại [Cập nhật năng lực] | ✅ **form MỞ LẠI ĐƯỢC**, liệt kê đủ 2 tệp kèm [Xóa] |
| Số tệp trước/sau lượt | **2 → 2** |

➡️ **Lượt đối chứng thứ 2 ĐẠT. Đủ 2/2 lượt "không đính tệp" mà khối khóa đòi.**

### 3.3 Lượt 3 — `TVV-BTP-TW-0038` · đính tệp **tên CÓ KÝ TỰ ĐẶC BIỆT** *(lấp GAP-2a — bắt chéo)*

R4 đã chạy 0038 với tên **thường**; nay đảo lại thành tên **có ký tự đặc biệt** trên chính hồ sơ đó.

| Bước | Quan sát thô |
|---|---|
| Đính `2K15 T3 (4.8) & CN (9.8).pdf` (dấu cách + ngoặc đơn + `&`) vào khối **"Thêm chứng chỉ mới"**, **Ghi chú = `a`** | vùng chọn tệp hiện `2K15 T3 (4.8) & CN (9.8).pdf (638 B) · Xem · Xóa`; `POST /api/v1/tu-van-viens/7c9107b3-…/files` → **201** (reqid 499) |
| `soObserverDangSong` | **1** ✅ |
| Bấm **[Lưu]** | `SO_REQUEST = 1` → `PATCH /api/v1/tu-van-viens/7c9107b3-…/nang-luc` → **200** (reqid 501)<br>`SO_KHUNG_THONG_BAO = 1` · `khoangCachMs = null` · `BI_LAP = false`<br>**Nguyên văn: "Cập nhật năng lực thành công"** |
| **Tải lại trang** → tab "Năng lực" | `Chứng chỉ chi tiết:`<br>`2K15 T3 (4.8) & CN (9.8).pdf`<br>`B7-CNHSNLTVV03-chungchi-B.pdf`<br>**`2K15 T3 (4.8) & CN (9.8).pdf`** ← tệp vừa đính, **đúng tên**, giữ nguyên dấu cách/ngoặc/`&` |
| Bấm lại [Cập nhật năng lực] | ✅ **form MỞ LẠI ĐƯỢC**; "Chứng chỉ hiện có" liệt kê đủ **3** tệp kèm [Xóa] |
| Số tệp trước/sau lượt | **2 → 3** (đúng **+1**, không sinh tệp thừa) |

### 3.4 Lượt 4 — `TVV-BTP-TW-0037` · đính tệp **tên THƯỜNG** *(lấp GAP-2b — bắt chéo)*

R4 đã chạy 0037 với tên **đặc biệt**; nay đảo lại thành tên **thường** trên chính hồ sơ đó.

| Bước | Quan sát thô |
|---|---|
| Bấm [Cập nhật năng lực] | ✅ form MỞ RA; "Chứng chỉ hiện có": `2K15 T3 (4.8) & CN (9.8).pdf [Xóa]` |
| Đính `B7-CNHSNLTVV03-chungchi-A.pdf` (chỉ chữ/số/gạch nối), **Ghi chú = `a`** | vùng chọn tệp hiện `B7-CNHSNLTVV03-chungchi-A.pdf (624 B) · Xem · Xóa`; `POST /api/v1/tu-van-viens/f179382a-…/files` → **201** (reqid 637) |
| `soObserverDangSong` | **1** ✅ |
| Bấm **[Lưu]** | `SO_REQUEST = 1` → `PATCH /api/v1/tu-van-viens/f179382a-…/nang-luc` → **200** (reqid 639)<br>`SO_KHUNG_THONG_BAO = 1` · `khoangCachMs = null` · `BI_LAP = false`<br>**Nguyên văn: "Cập nhật năng lực thành công"** |
| **Tải lại trang** → tab "Năng lực" | `Chứng chỉ chi tiết:`<br>`2K15 T3 (4.8) & CN (9.8).pdf`<br>**`B7-CNHSNLTVV03-chungchi-A.pdf`** ← tệp vừa đính, **đúng tên** |
| Bấm lại [Cập nhật năng lực] | ✅ **form MỞ LẠI ĐƯỢC**; "Chứng chỉ hiện có" liệt kê đủ 2 tệp kèm [Xóa] |
| Số tệp trước/sau lượt | **3 → 4** (đúng **+1**) |

### 3.5 Bảng gộp 4 lượt

| Lượt | Hồ sơ | Trạng thái hồ sơ | Đính tệp? | Kiểu tên tệp | Thông báo (nguyên văn) | `SO_REQUEST` | `SO_KHUNG_THONG_BAO` | Mã phản hồi máy chủ |
|---|---|---|---|---|---|---|---|---|
| 1 | `TVV-BTP-TW-0002` | **Đang hoạt động** | **không** | — | "Cập nhật năng lực thành công" | 1 | 1 | `PATCH …/nang-luc` **200** |
| 2 | `TVV-BTP-TW-0038` | Mới đăng ký | **không** | — | "Cập nhật năng lực thành công" | 1 | 1 | `PATCH …/nang-luc` **200** |
| 3 | `TVV-BTP-TW-0038` | Mới đăng ký | **có** | **ký tự đặc biệt** | "Cập nhật năng lực thành công" | 1 | 1 | `POST …/files` **201** + `PATCH …/nang-luc` **200** |
| 4 | `TVV-BTP-TW-0037` | Mới đăng ký | **có** | **thường** | "Cập nhật năng lực thành công" | 1 | 1 | `POST …/files` **201** + `PATCH …/nang-luc` **200** |

**4/4 lượt:** `soObserverDangSong = 1` · `BI_LAP = false` · `khoangCachMs = null` (không có khung thông báo thứ 2).
**0/4 lượt** tái hiện `500 ERR-SYS-00-00-01` hay câu *"Lỗi hệ thống, vui lòng thử lại sau."*
**Nhật ký trình duyệt cả phiên: 0 dòng lỗi, 0 dòng cảnh báo.**

---

## 4. Quan sát sau khi tải lại trang (tổng hợp)

| Hồ sơ | Dòng "Chứng chỉ chi tiết" đọc được sau khi tải lại (nguyên văn) | Form mở lại được? |
|---|---|---|
| `TVV-BTP-TW-0002` | `Chung chi hanh nghe Luat su — Bo Tu phap — cấp 15/03/2012` · `cc120.pdf` | ✅ |
| `TVV-BTP-TW-0038` | `2K15 T3 (4.8) & CN (9.8).pdf` · `B7-CNHSNLTVV03-chungchi-B.pdf` · `2K15 T3 (4.8) & CN (9.8).pdf` | ✅ |
| `TVV-BTP-TW-0037` | `2K15 T3 (4.8) & CN (9.8).pdf` · `B7-CNHSNLTVV03-chungchi-A.pdf` | ✅ |

- **Hiện TÊN TỆP** ở mọi hồ sơ. Không hồ sơ nào còn in chuỗi kỹ thuật `{"fileDinhKemId":"…"}` (cảnh gãy của R3).
- **4/4 lượt bấm lại [Cập nhật năng lực] đều mở được form.** Kiểm bằng biểu thức `/không có quyền truy cập/i`
  trên `document.body.innerText` → **false 4/4 lượt**; URL không lần nào đổi sang `/403`.

### Kiểm tệp thừa (vế ⚠️ thứ 3 của khối CÁCH VERIFY)

| Hồ sơ | Số tệp trước | Số tệp sau | Chênh | Đúng kỳ vọng? |
|---|---|---|---|---|
| `TVV-BTP-TW-0002` (lượt 1, không đính) | 2 | 2 | +0 | ✅ |
| `TVV-BTP-TW-0038` (lượt 2, không đính) | 2 | 2 | +0 | ✅ |
| `TVV-BTP-TW-0038` (lượt 3, đính 1 tệp) | 2 | 3 | +1 | ✅ |
| `TVV-BTP-TW-0037` (lượt 4, đính 1 tệp) | 3 | 4 | +1 | ✅ |

**Không lượt nào sinh tệp thừa.** (Lưu ý: phép kiểm này vốn chỉ có tiền đề khi có lượt lưu **hỏng** — R5 không có lượt hỏng nào,
nên đây là số liệu bổ sung, không phải điều kiện quyết định.)

---

## 5. Đường đo thứ hai (cùng phiên đăng nhập, `fetch(url,{credentials:'include'})`)

### 5.1 Đọc lại bản ghi từ máy chủ — so với màn hình

| Hồ sơ | `version` (trước → sau) | `hoSo.chungChiChiTiet` (nguyên văn máy chủ trả) | Số tệp |
|---|---|---|---|
| `TVV-BTP-TW-0002` | 28 → **29** | `[{"noiCap":"Bo Tu phap","ngayCap":"2012-03-15","tenChungChi":"Chung chi hanh nghe Luat su"},{"fileDinhKemId":"dac3cbb9-…"}]` — **KHÔNG đổi** so với trước lượt 1 | 2 |
| `TVV-BTP-TW-0038` | 6 → **7** (hồ sơ năng lực 7 → **8**) | `[{"fileDinhKemId":"80ae5609-…"},{"fileDinhKemId":"47afd6d2-…"},{"fileDinhKemId":"bd7c8ea0-…"}]` — **+1 mục** do lượt 3 | 3 |
| `TVV-BTP-TW-0037` | 3 → 3 (hồ sơ năng lực đổi) | `[{"fileDinhKemId":"61aa4cef-…"},{"fileDinhKemId":"c7686836-…"}]` — **+1 mục** do lượt 4 | 4 |

- **Trường ngoài tệp cũng ghi được:** máy chủ trả `trinhDo: "Thac si"` (0002, lượt 1) và `trinhDo: "Tien si"` (0038, lượt 2)
  — khớp đúng những gì màn hình hiện sau khi tải lại.
- **2 lượt không đính tệp KHÔNG chạm vào `chungChiChiTiet`**: mảng giữ nguyên từng phần tử ⇒ chứng cứ máy-chủ cho việc
  *lượt lưu không tệp không làm mất tệp đang có*.
- **Hai đường (giao diện ↔ máy chủ) KHÔNG mâu thuẫn** ở cả 4 lượt.

### 5.2 Mở tệp vừa đính qua đường đọc tệp — `GET /api/v1/files/{id}`

| Tệp | ID | Lượt sinh ra | Kết quả |
|---|---|---|---|
| `2K15 T3 (4.8) & CN (9.8).pdf` | `bd7c8ea0-21e9-43d5-b231-6487a2be59bd` | **R5 lượt 3** (mới) | ✅ **200** · `tenFile: "2K15 T3 (4.8) & CN (9.8).pdf"` |
| `B7-CNHSNLTVV03-chungchi-A.pdf` | `c7686836-f2c3-447d-a2e9-c4da1681cd32` | **R5 lượt 4** (mới) | ✅ **200** · `tenFile: "B7-CNHSNLTVV03-chungchi-A.pdf"` |
| `2K15 T3 (4.8) & CN (9.8).pdf` | `80ae5609-a269-4bf3-a7b1-8c33942462c9` | R3 (cũ, từng 403) | ✅ **200** |
| `B7-CNHSNLTVV03-chungchi-B.pdf` | `47afd6d2-475a-48ef-8425-b31bfefe1572` | R4 | ✅ **200** |
| `2K15 T3 (4.8) & CN (9.8).pdf` | `61aa4cef-a4ec-4464-bdd1-3c3d1f16358d` | R4 | ✅ **200** |

➡️ **0/5 tệp trả 403 `ERR-PERM-FILE-03`.** Tên tệp có ký tự đặc biệt được máy chủ trả về **nguyên vẹn**.
Xác nhận thêm bằng lời gọi của **chính giao diện** (không phải QA gọi tay): reqid 641
`GET /api/v1/files/c7686836-…` → **200** ngay sau lượt 4, và reqid 604-606 → **200** khi dựng lại trang 0038.

---

## 6. Dẫn đặc tả (tự mở file đếm lại 2026-08-07)

Nguồn duy nhất `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`. File `srs-fr-04-chuyen-gia-tvv.md` — **2542 dòng**,
đã tự mở đếm lại từng dòng dưới đây (không bê từ hồ sơ cũ, không lấy từ trí nhớ). **Không dòng nào lệch so với chuẩn chấm §2.**

| Dòng | Nguyên văn (cắt) | Liên quan lượt nào |
|---|---|---|
| `:375` | `**Tác nhân:** Người hỗ trợ pháp lý (NHT)` | vai trò đo — cả 4 lượt |
| `:388` | `\| 6 \| chung_chi_moi \| binary[] \| N \| PDF, max 10MB/file, tổng 50MB, max 10 files \| — \| user upload \|` | lượt 3, 4 (có tệp) |
| `:402` | `\| 4 \| Cập nhật thông tin năng lực trong HO_SO_TU_VAN_VIEN \| — \|` | lượt 1, 2 (không tệp) |
| `:403` | `\| 5 \| Nếu có file mới: tạo bản ghi FILE_DINH_KEM \| — \|` | lượt 3, 4 (có tệp) |
| `:414` | `\| 3 \| tvv_data \| object \| — \| Trả về các field đã cập nhật (để FE refresh UI readonly confirm) \|` | §5.1 đọc lại bản ghi |
| `:418` | `- Hồ sơ năng lực được cập nhật` | cả 4 lượt |
| `:432` | `- **Given** NHT xem chi tiết TVV cùng đơn vị **When** nhấn "Cập nhật năng lực" **Then** form inline edit mở` | mở/mở lại form — 8/8 lượt bấm |
| `:433` | `- **Given** NHT cập nhật thông tin/chứng chỉ + upload file **When** lưu **Then** validate và lưu thành công` | **dòng quyết định** — lượt 3, 4 |
| `:1576` | `\| 21 \| tab 3 \| Tab "Năng lực" \| tab + nội dung \| Bằng cấp chi tiết, Chứng chỉ chi tiết, Kinh nghiệm chi tiết. Nút "Cập nhật năng lực" → form sửa nhanh \| …` | màn đo |

`:405` và `:1590` (Yêu cầu bổ sung → Đang thẩm định) **không kích hoạt** ở R5: 3 hồ sơ đo đều ở `HOAT_DONG` / `MOI_DANG_KY`,
không hồ sơ nào ở `YEU_CAU_BO_SUNG` ⇒ không có chuyển trạng thái nào cần diễn giải. Đã kiểm sau mỗi lượt: `trangThai` giữ nguyên.

---

## 7. Đối chiếu TỔNG HỢP R4 + R5 với TỪNG gạch đầu dòng của khối khóa

> Khối khóa (chép nguyên văn, **KHÔNG sửa, không nới**):
> ```
> ✅ PASS khi: đủ 6/6 lượt đều báo thành công VÀ sau khi tải lại trang, tệp vừa đính hiện trong khối
>    "Chứng chỉ hiện có" của đúng hồ sơ đó với đúng tên tệp, VÀ phản hồi máy chủ của cả 6 lượt đều là
>    thành công, VÀ mỗi lượt chỉ sinh đúng 1 thông báo (đếm theo mốc giờ khác nhau, không đếm số phần tử).
> ❌ FAIL nếu: bất kỳ lượt nào trong 6 lượt báo lỗi hoặc máy chủ trả lỗi — kể cả khi chỉ hỏng ở 1 trong 2
>    kiểu tên tệp, hoặc chỉ hỏng ở 1 trong 2 hồ sơ. Cũng FAIL nếu báo thành công nhưng tải lại trang thì
>    tệp không có trong "Chứng chỉ hiện có" (fix bề mặt).
> ```

### 7.1 Sáu lượt đã khóa — lượt nào do vòng nào chứng minh

Khối khóa chốt **6 lượt = 2 lượt không tệp + 4 lượt có tệp (2 hồ sơ × 2 kiểu tên)**:

| # | Lượt theo khối khóa | Vòng chứng minh | Hồ sơ · kiểu tên | Kết |
|---|---|---|---|---|
| L1 | không tệp — lượt đối chứng 1 | **R5 lượt 1** | `TVV-BTP-TW-0002` (Đang hoạt động) | ✅ |
| L2 | không tệp — lượt đối chứng 2 | **R5 lượt 2** | `TVV-BTP-TW-0038` (Mới đăng ký) | ✅ |
| L3 | có tệp — hồ sơ A × tên thường | **R4** | `TVV-BTP-TW-0038` · `B7-…-chungchi-B.pdf` | ✅ |
| L4 | có tệp — hồ sơ A × tên đặc biệt | **R5 lượt 3** | `TVV-BTP-TW-0038` · `2K15 T3 (4.8) & CN (9.8).pdf` | ✅ |
| L5 | có tệp — hồ sơ B × tên đặc biệt | **R4** | `TVV-BTP-TW-0037` · `2K15 T3 (4.8) & CN (9.8).pdf` | ✅ |
| L6 | có tệp — hồ sơ B × tên thường | **R5 lượt 4** | `TVV-BTP-TW-0037` · `B7-…-chungchi-A.pdf` | ✅ |

**⇒ 6/6 lượt đã chạy, trên cùng một bó mã `index-D4Buvu4S.js`.** Ma trận 2 hồ sơ × 2 kiểu tên tệp **đã bắt chéo đủ 4 ô**.

### 7.2 Từng gạch đầu dòng

| # | Điều kiện trong khối khóa | Bằng chứng | Do lượt nào chứng minh | Kết |
|---|---|---|---|---|
| **P1** | **đủ 6/6 lượt** đều báo thành công | 6/6 lượt hiện **"Cập nhật năng lực thành công"**; 0/6 lượt hiện thông báo lỗi | R4 (2) + **R5 lượt 1·2·3·4** | ✅ **thoả** |
| **P2** | sau khi tải lại trang, tệp vừa đính **hiện trong khối "Chứng chỉ hiện có" của đúng hồ sơ đó với đúng tên tệp** | 4/4 lượt có tệp: tải lại → mở form → "Chứng chỉ hiện có" liệt kê **đúng tệp vừa đính, đúng tên**, kể cả tên có dấu cách/ngoặc/`&`. 2 lượt không tệp: tệp cũ **còn nguyên**, không mất | R4 (L3, L5) + **R5 lượt 3 (L4), lượt 4 (L6)**; vế "không mất tệp" do **R5 lượt 1, 2** | ✅ **thoả** |
| **P3** | **phản hồi máy chủ** của cả 6 lượt đều thành công | 6/6 `PATCH …/nang-luc` → **200**. 4 lượt có tệp kèm `POST …/files` → **201** | R4 (2) + **R5 lượt 1·2·3·4** | ✅ **thoả** |
| **P4** | **mỗi lượt chỉ sinh đúng 1 thông báo** (đếm theo mốc giờ, không đếm số phần tử) | 6/6 lượt: `SO_KHUNG_THONG_BAO = 1` · `SO_REQUEST = 1` · `khoangCachMs = null` · `BI_LAP = false`; `soObserverDangSong = 1` ở **cả 6 lượt** | R4 (2) + **R5 lượt 1·2·3·4** | ✅ **thoả** |
| **F1** | FAIL nếu **bất kỳ lượt nào báo lỗi hoặc máy chủ trả lỗi** | 0/6 lượt báo lỗi; 0/6 lượt máy chủ trả lỗi. **Không tái hiện** `500 ERR-SYS-00-00-01` / *"Lỗi hệ thống, vui lòng thử lại sau."* Nhật ký trình duyệt R5: 0 lỗi | R4 (2) + **R5 lượt 1·2·3·4** | ✅ **không kích hoạt** |
| **F2** | FAIL nếu hỏng ở **1 trong 2 kiểu tên tệp** | tên **thường**: OK trên 0038 (R4) **và** 0037 (R5 lượt 4). tên **đặc biệt**: OK trên 0037 (R4) **và** 0038 (R5 lượt 3). **Đã bắt chéo** ⇒ kết quả không phụ thuộc cặp hồ sơ↔kiểu tên | R4 + **R5 lượt 3, 4** | ✅ **không kích hoạt** |
| **F3** | FAIL nếu hỏng ở **1 trong 2 hồ sơ** | Trục trạng thái nay đủ: **Đang hoạt động** (`0002`, R5 lượt 1 — bấm [Lưu] thật, không chỉ mở form) và **Mới đăng ký** (`0038`, `0037`). 3 hồ sơ, 0 hồ sơ hỏng | **R5 lượt 1** (lấp GAP-3) + R4 + R5 lượt 2·3·4 | ✅ **không kích hoạt** |
| **F4** | FAIL nếu **báo thành công nhưng tải lại trang thì tệp không có trong "Chứng chỉ hiện có"** (fix bề mặt) | 6/6 lượt: tải lại trang → tệp **CÓ** trong "Chứng chỉ hiện có", đúng tên; đọc lại từ máy chủ khớp màn hình. **Đây chính là vế đã làm R3 FAIL — nay không kích hoạt** | R4 (2) + **R5 lượt 1·2·3·4** | ✅ **không kích hoạt** |

### 7.3 Ba vế ⚠️ của khối CÁCH VERIFY

| ⚠️ | Đã tuân thủ thế nào |
|---|---|
| Đừng Fail vì nhãn nút "Lưu" thay vì "Đồng ý", form inline thay vì hộp thoại, hay câu chữ thông báo **thành công** (`:432` im lặng) | **Không** chấm Fail vì các điểm này. Ghi nhận: nút thật là **[Lưu]**, form là **inline**, câu thông báo là *"Cập nhật năng lực thành công"* — đều **không** dùng làm căn cứ Fail |
| Đừng Fail khi hệ thống từ chối ĐÚNG theo `:425`–`:429` | Không lượt nào bị từ chối; **không mở rộng** sang tệp >10MB / tổng >50MB / mã độc / khác đơn vị / hồ sơ vô hiệu hóa |
| Đừng kết luận "đã fix" khi **chỉ** thấy lượt không tệp chạy được, hoặc **chỉ** từ bước tải tệp trả 201 | Verdict dựa trên **4 lượt CÓ đính tệp** (L3–L6). 2 lượt không tệp (L1, L2) chỉ ghi là **đối chứng chống hồi quy**, không dùng làm căn cứ "đã fix". `POST …/files` → 201 ghi riêng, **không** dùng để kết luận |

---

## 8. Bảng GAP còn lại

| GAP | Trạng thái |
|---|---|
| **GAP-1** — 2 lượt "không đính tệp" | ✅ **ĐÃ LẤP** — R5 lượt 1 (`0002`) + lượt 2 (`0038`). Cả 2 lưu được, không làm mất tệp đang có |
| **GAP-2** — bắt chéo kiểu tên tệp | ✅ **ĐÃ LẤP** — R5 lượt 3 (`0038` × tên đặc biệt) + lượt 4 (`0037` × tên thường). Ma trận 2×2 đủ 4 ô |
| **GAP-3** — bấm [Lưu] trên hồ sơ *Đang hoạt động* | ✅ **ĐÃ LẤP** — R5 lượt 1 bấm [Lưu] thật trên `TVV-BTP-TW-0002`, `PATCH` → 200 |
| **GAP-4** (R4) — đếm tệp thừa | ✅ **Hết tiền đề** — R5 không có lượt lưu hỏng nào. Vẫn đã đếm trước/sau cả 4 lượt: **0 tệp thừa** (§4) |
| **GAP-5** (R4) — hoàn nguyên dữ liệu | ⏳ **CHƯA LÀM** — ngoài phạm vi 4 lượt được giao; **điều phối quyết**. Xem §10 |

**GAP chặn verdict: TRỐNG.** Không còn lượt nào của khối khóa chưa đo.

---

## 9. Phát hiện ngoài lề — xếp loại **candidate**, KHÔNG dùng làm căn cứ verdict

**Tab "Hồ sơ" hiển thị dòng "Chứng chỉ chi tiết" là `—` với chứng chỉ chỉ-có-tệp.**

- Trên `TVV-BTP-TW-0037` (2 chứng chỉ, cả 2 đều dạng `{"fileDinhKemId":…}`): tab **"Hồ sơ"** đọc được
  `Chứng chỉ chi tiết  —`, trong khi tab **"Năng lực"** cùng lúc đọc được đủ
  `2K15 T3 (4.8) & CN (9.8).pdf` · `B7-CNHSNLTVV03-chungchi-A.pdf`, và khối "File đính kèm" liệt kê đủ 4 tệp.
- Trên `TVV-BTP-TW-0002` (1 chứng chỉ có `tenChungChi` + 1 chứng chỉ chỉ-có-tệp): tab "Hồ sơ" chỉ hiện mục có tên,
  **không** hiện `cc120.pdf`; tab "Năng lực" hiện đủ cả hai.
- Ảnh: `CNHSNLTVV_03-R5-08-candidate-tab-HoSo-chungchi-chi-tiet-hien-gach-ngang.png`.

**Vì sao KHÔNG kéo vào verdict:** khối khóa chỉ nói tới khối **"Chứng chỉ hiện có"** (nằm trong form [Cập nhật năng lực])
và màn tab **"Năng lực"** — cả hai đều **hiện đúng tên tệp** ở 6/6 lượt. Tab "Hồ sơ" **không** nằm trong bất kỳ gạch đầu dòng nào
của khối khóa, và `:1576` cũng chỉ đặc tả tab "Năng lực". Kéo mục này vào = **nới khối khóa** ⇒ cấm.
Ghi lại để điều phối quyết có mở phiếu riêng hay không.

---

## 10. Dữ liệu để lại trên env (chưa hoàn nguyên)

| Hồ sơ | Thay đổi do R5 gây ra | Trạng thái cuối |
|---|---|---|
| `TVV-BTP-TW-0002` | `trinhDo` `Cử nhân` → **`Thac si`**; `kinhNghiemChiTiet` nối thêm chuỗi `…QA R5 GAP-1a khong dinh tep tren ho so Dang hoat dong 2026-08-07`. **Không thêm/bớt tệp nào** | version 29 · 2 chứng chỉ · 2 tệp (`cc120.pdf`, `the-hanh-nghe-qa.pdf`) |
| `TVV-BTP-TW-0038` | `trinhDo` `Thạc sĩ` → **`Tien si`**; `kinhNghiemChiTiet` thay bằng `QA R5 GAP-1b khong dinh tep tren ho so Moi dang ky 2026-08-07`; **+1 tệp** `2K15 T3 (4.8) & CN (9.8).pdf` (`bd7c8ea0-…`) | version 7 · 3 chứng chỉ · 3 tệp |
| `TVV-BTP-TW-0037` | **+1 tệp** `B7-CNHSNLTVV03-chungchi-A.pdf` (`c7686836-…`). Trình độ/kinh nghiệm **không đổi** | version 3 · 2 chứng chỉ · 4 tệp |

**Chưa hoàn nguyên.** Chuẩn chấm §3 đòi trả `TVV-BTP-TW-0002` về mốc gốc (Cử nhân · số năm trống · `STHN-QA-28` ·
1 bằng cấp · 1 chứng chỉ nơi cấp "Bo Tu phap" · 4 lĩnh vực · chỉ còn tệp `the-hanh-nghe-qa.pdf`). Hai mục còn lệch so với mốc gốc:
`trinhDo` = `Thac si` (gốc `Cử nhân`) và tệp `cc120.pdf` + chuỗi `"Kiem thu CNHSNLTVV_03 tren 120 v1.0.9"` **do vòng trước để lại**.
Nút **[Xóa]** trong khối "Chứng chỉ hiện có" nay bấm được ⇒ hoàn nguyên khả thi khi điều phối yêu cầu.
**Không tự hoàn nguyên** vì nằm ngoài 4 lượt được giao và sẽ phá tiền đề nếu điều phối muốn đo lại.

---

## 11. Verdict đề xuất

### ✅ PASS — cho **cả phiếu CNHSNLTVV_03**

Căn cứ, theo đúng câu chữ khối khóa (§7.2), **không nới một chữ nào**:

1. **Đủ 6/6 lượt** (R4 2 lượt + R5 4 lượt), **cùng một bó mã** `index-D4Buvu4S.js` — vân tay đầu phiên = cuối phiên = R4 (§1).
2. **6/6 lượt báo thành công**, nguyên văn *"Cập nhật năng lực thành công"*; **0 lượt** báo lỗi.
3. **6/6 lượt máy chủ trả thành công**: `PATCH …/nang-luc` → **200** (4 lượt có tệp kèm `POST …/files` → **201**).
   **Không tái hiện** `500 ERR-SYS-00-00-01` — chính là lỗi gốc của phiếu.
4. **6/6 lượt đúng 1 thông báo**, `SO_REQUEST = 1`, `soObserverDangSong = 1`, `BI_LAP = false`.
5. **Tải lại trang, tệp vừa đính hiện trong "Chứng chỉ hiện có" đúng tên** ở 4/4 lượt có tệp ⇒ vế *fix bề mặt* **không kích hoạt**.
6. **Cả 2 trục mà câu FAIL nêu đích danh đều đã bắt chéo**: 2 kiểu tên tệp × 2 hồ sơ (§7.1), cộng trục trạng thái
   **Đang hoạt động** nay đã có lượt [Lưu] thật (GAP-3).
7. Đường đo thứ hai khớp: đọc lại bản ghi từ máy chủ **không mâu thuẫn** màn hình; `GET /api/v1/files/{id}` **200 · 0/5 tệp còn 403**.

### Điểm cần biết khi đọc verdict (quan sát, không phải căn cứ Fail)

- Máy chủ **vẫn lưu** `chungChiChiTiet` dạng `{"fileDinhKemId":"…"}` không kèm tên tệp; màn hình hiện được tên là nhờ
  đường đọc tệp đã thôi trả 403. Khối khóa **không nói gì** về hình dạng dữ liệu lưu ⇒ **không** dùng để Fail.
- Mục §9 (tab "Hồ sơ" hiện `—`) là **candidate**, đã tách khỏi verdict.
- 2 lượt không đính tệp chỉ là **đối chứng chống hồi quy** — verdict dựa trên 4 lượt **CÓ** đính tệp, đúng vế ⚠️ thứ 3.

---

## 12. Ảnh (8 tấm) — `output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/image/`

| Tệp | Bắt được gì |
|---|---|
| `CNHSNLTVV_03-R5-01-luot1-TVV0002-khong-tep-thong-bao.png` | **Lượt 1** — `0002` *Đang hoạt động*, lượt [Lưu] không đính tệp (GAP-1a + GAP-3) |
| `CNHSNLTVV_03-R5-02-luot1-TVV0002-sau-tai-lai-form-mo-lai-con-tep.png` | **Lượt 1 sau tải lại** — Trình độ đã thành `Thac si`, form mở lại được, `cc120.pdf` còn nguyên trong "Chứng chỉ hiện có" |
| `CNHSNLTVV_03-R5-03-luot2-TVV0038-khong-tep-thong-bao.png` | **Lượt 2** — `0038`, lượt [Lưu] không đính tệp (GAP-1b) |
| `CNHSNLTVV_03-R5-04-luot3-TVV0038-tep-ten-dac-biet-thong-bao.png` | **Lượt 3** — `0038` × tệp tên **có ký tự đặc biệt** (GAP-2a, bắt chéo) |
| `CNHSNLTVV_03-R5-05-luot3-TVV0038-sau-tai-lai-3-tep-dung-ten.png` | **Lượt 3 sau tải lại** — "Chứng chỉ hiện có" liệt kê đủ **3** tệp đúng tên, form mở lại được |
| `CNHSNLTVV_03-R5-06-luot4-TVV0037-tep-ten-thuong-thong-bao.png` | **Lượt 4** — `0037` × tệp tên **thường** (GAP-2b, bắt chéo) |
| `CNHSNLTVV_03-R5-07-luot4-TVV0037-sau-tai-lai-2-tep-dung-ten.png` | **Lượt 4 sau tải lại** — "Chứng chỉ hiện có" liệt kê đủ 2 tệp đúng tên, form mở lại được |
| `CNHSNLTVV_03-R5-08-candidate-tab-HoSo-chungchi-chi-tiet-hien-gach-ngang.png` | **§9 candidate** — tab "Hồ sơ" hiện `Chứng chỉ chi tiết —` dù tab "Năng lực" hiện đủ 2 tên tệp |

*(Thông báo dạng toast tự tắt ~3s: bấm [Lưu] được hẹn giờ +2500ms rồi mới gọi chụp ảnh. Nguyên văn từng câu thông báo
lấy từ `tools/toast-capture.js` (`innerText`, không lọc trùng) + mã phản hồi máy chủ, đã ghi ở §3.)*
