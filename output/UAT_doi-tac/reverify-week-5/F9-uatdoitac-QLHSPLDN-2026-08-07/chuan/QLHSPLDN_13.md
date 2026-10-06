# QLHSPLDN_13 — Khoảng ngày không hợp lệ · GIAI ĐOẠN A (khóa phép thử)

**Dòng bảng:** 295 (tab `bug`) · **Flow:** [`flows/03-reverify-sau-dev-fix.md`](../../../../../flows/03-reverify-sau-dev-fix.md) nhánh 2
**Env đo:** `https://htpldn-uat.ospgroup.vn` (env nghiệm thu của đối tác) · **Tài khoản ra verdict:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`)
**Màn:** menu **Doanh nghiệp** → *Xem chi tiết* 1 DN → thẻ **Hồ sơ pháp lý doanh nghiệp** (`/doanh-nghiep/{id}?tab=ho-so-pl`)
**Nguồn canonical cách đo:** entry `BUG-HSPLDN-QLHSPLDN-13` trong [`F4-pilot/bug-report.md`](../../F4-pilot-QLHSPLDN-2026-08-07/bug-report.md) + vế C3 trong [`F4-pilot/bao-cao-lo`](../../F4-pilot-QLHSPLDN-2026-08-07/bao-cao-lo-2026-08-07.md)

> ⚠️ Mọi dòng SRS dưới đây đã **mở file đọc lại** trong lô này, không bê từ báo cáo cũ.

---

## 1. Ô phiếu đối tác (expected gốc — nguyên văn)

| Ô | Nội dung |
|---|---|
| **Mô tả** | Khoảng ngày không hợp lệ |
| **Bước 4** | *Ngày bắt đầu sau ngày kết thúc* |
| **Kết quả mong đợi** | *"Hệ thống hiển thị thông báo \"Ngày bắt đầu phải trước ngày kết thúc\"."* |
| **TKM phản hồi lần 1 (KQ thực tế phía đối tác)** | *"Không có trường thông tin tìm kiếm trên màn hình"* |

---

## 2. Bảng vế × quan hệ SRS

| Vế | Đối tác đòi gì | SRS `file:dòng` — quote nguyên văn | Quan hệ | Route |
|---|---|---|---|---|
| **C3a** — thẻ phải có bộ lọc khoảng ngày | Bước 4 đặt được ngày bắt đầu / ngày kết thúc | `srs-fr-12-tv-chuyen-sau.md:589` — "**Inputs -- Tìm kiếm:**"; `:596` — "\| 4 \| **tu_ngay / den_ngay** \| date \| N \| **tu_ngay <= den_ngay** \| — \| người dùng chọn \|" | **MATCH** | TEST |
| **C3b** — chặn + báo đúng câu khi ngày ngược | *"hệ thống hiển thị thông báo \"Ngày bắt đầu phải trước ngày kết thúc\""* | `srs-fr-12:700` — "\| E6 \| **tu_ngay > den_ngay (tìm kiếm)** \| **ERR-HSPL-06** \| \"**Ngày bắt đầu phải trước ngày kết thúc**\" \| ERROR \|" (bảng **Error Handling** mở ở `:691`) | **MATCH** — khớp **từng ký tự** với câu trong ô phiếu | TEST |
| **C3c** — chức năng thuộc đúng thẻ đang tranh chấp | Phiếu chỉ đích danh thẻ *Hồ sơ pháp lý* trong chi tiết DN | `srs-fr-12:560` — "**Màn hình:** ~~SCR-X1-03~~ (DEPRECATED v2.1 — chuyển sang tab trong MH-07.2 chi tiết DN)"; `:1205` — "> **Chuyển sang:** Tab \"Hồ sơ PL\" trong MH-07.2 chi tiết Doanh nghiệp (srs-fr-07-doanh-nghiep.md)."; `srs-fr-07-doanh-nghiep.md:455`, `:461` | **MATCH** | TEST |

**Vai trò được phép:** `srs-fr-12:565` — "**Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Người hỗ trợ".

### 2.1 Giải quyết điểm "hai nơi không khớp" — `srs-fr-12` ↔ `srs-fr-07:468` ("CRUD")

- `srs-fr-07:468` — "| 2 | tab | Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) | tab | **CRUD hồ sơ pháp lý DN**: … | — | Chỉ khi xem chi tiết |"
- `srs-fr-12:563` — "CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, xem chi tiết, thêm mới, chỉnh sửa, xóa mềm, **tìm kiếm**."

⇒ Bộ lọc khoảng ngày là **thành phần của chức năng tìm kiếm** (`:596`), mà "CRUD" tại `:468` là nhãn gọi tắt của FR-X.1-04 và FR-X.1-04 khai rõ CRUD của nó **bao gồm tìm kiếm**. Bảng thành phần `SCR-V.III-02` **không enumerate** nội dung bên trong thẻ 2/3/4 ⇒ **im lặng ở mức liệt kê, không phải phủ định**. Ngoài ra `ERR-HSPL-06` được `:700` quy định tường minh với mã lỗi riêng.

**Kết luận C3: `MATCH`** — được đo, được Pass nếu đạt. **Không có câu hỏi BA.**

### 2.2 Bẫy đã có tiền lệ — đã kiểm lại, xác nhận không áp

`srs-fr-07:523` ("Tab 2 — Hồ sơ pháp lý DN | **Read-only**") thuộc **`SCR-V.III-04`** (`:508`, URL `/doanh-nghiep/ho-so-cua-toi`), mà `:514` ghi "**Vai trò khác KHÔNG truy cập trang này.**" ⇒ **cấm dùng cho màn đang đo** (`SCR-V.III-02`).

---

## 3. Dòng khóa phép đo

```
C3 · không có bộ lọc khoảng ngày nên không kiểm được cảnh báo khi ngày bắt đầu sau ngày kết thúc
   · srs-fr-12-tv-chuyen-sau.md:700 (E6 · ERR-HSPL-06 · ERROR) + :596 (ràng buộc tu_ngay <= den_ngay)
     (neo màn :560, :1205)
   · MATCH
   · thao tác: cài bộ bắt thông báo (MutationObserver trên document.body) TRƯỚC khi bấm → đặt Từ ngày muộn hơn
              Đến ngày (vd 31/12/2026 và 01/01/2026) → bấm [Tìm kiếm] → bấm LẶP lần 2
   · PASS khi: mỗi lượt bấm hiện ĐÚNG 1 thông báo, nguyên văn "Ngày bắt đầu phải trước ngày kết thúc"
              (đọc innerText, khớp từng ký tự) · hệ thống KHÔNG trả về danh sách kết quả theo khoảng ngày ngược
              (bảng giữ nguyên tập trước đó hoặc không đổi theo cặp ngày sai) · lần bấm 2 vẫn đúng 1, không nhân đôi
   · FAIL khi: không hiện thông báo nào · câu lệch dù 1 ký tự · thông báo nhân đôi ở cùng 1 lượt bấm ·
              hoặc hệ thống vẫn chạy tìm kiếm và trả danh sách theo khoảng ngày ngược · hoặc trả 5xx
   · biến thể bắt buộc: 2 — (a) 1 cặp ngày ngược đúng Bước 4 của phiếu · (b) 1 lượt bấm LẶP để loại ca nhân đôi
```

> ⚠️ Chọn cặp ngày **thực sự ngược** (`tu_ngay` > `den_ngay`). **Không** dùng cặp bằng nhau: `:596` cho phép `tu_ngay <= den_ngay`, nên hai ngày bằng nhau là **hợp lệ**, không thuộc nhánh E6.

---

## 4. Đối chứng độc lập bắt buộc

🔴 **CẤM Pass bằng quan sát tĩnh.** Thấy 2 ô ngày hiện trên màn **không phải** bằng chứng cho C3.

| # | Việc phải làm | Vì sao tính là độc lập |
|---|---|---|
| 1 | **Cài `MutationObserver` trên `document.body` TRƯỚC khi bấm**, capture `addedNodes` 2–5s. **CẤM lọc trùng** (dedupe che double-toast → Pass oan). **CẤM `textContent`** (bắt node ẩn AntD → bug ma) — đọc **`innerText`** | Thông báo tự tắt < 5s; poll DOM sau khi bấm sẽ trượt và kết luận sai "im lặng" |
| 2 | **Tự kiểm bộ bắt còn sống** sau lượt đo (đếm số observer đang hoạt động) | Số "0 thông báo" chỉ có nghĩa khi chứng minh được bộ bắt không chết giữa chừng |
| 3 | **So từng ký tự** chuỗi bắt được với `Ngày bắt đầu phải trước ngày kết thúc` ở `:700`; ghi `exactMatch` + vị trí ký tự lệch nếu có | So bằng mắt bỏ sót lệch dấu / khoảng trắng |
| 4 | **Đếm lượt gọi máy chủ phát sinh do cú bấm** (bọc **cả `fetch` lẫn `XMLHttpRequest`**), ghi rõ 0 lượt (chặn ở giao diện) hay có lượt (chặn ở máy chủ) | Đây là **chẩn đoán để mô tả cho dev**, và là đối chứng độc lập cho mệnh đề *"hệ thống từ chối tìm kiếm"*. **Không** phải tiêu chí Pass/Fail — xem §6 |
| 5 | Nếu **có** lượt gọi phát sinh: đọc phản hồi của chính lượt đó — phải là **từ chối**, không được trả danh sách kết quả theo khoảng ngày ngược | Loại ca "hiện cảnh báo cho có nhưng vẫn truy vấn và đổi bảng" |
| 6 | **Bấm lặp lần 2** (giữ nguyên cặp ngày) và đếm lại | Đối chứng cho mệnh đề "đúng 1 thông báo"; đây là biến thể bắt buộc, không phải "bấm lại để săn ảnh" |
| 7 | Ghi lại có/không lỗi hiển thị kèm ô nhập (`.ant-form-item-explain-error`) | Dữ kiện cho dev; không dùng chấm |

**Ghi lại tối thiểu:** ảnh 2 ô ngày đang là cặp ngược + thông báo · số thông báo bắt được lượt 1 và lượt 2 · kết quả so ký tự · số lượt gọi máy chủ · vân tay bản dựng ở **đầu và cuối** case.

---

## 5. Tiền đề dữ liệu trên env đối tác

**KHÔNG seed gì.** Case này chỉ đọc; nhánh đo là nhánh **từ chối trước khi truy vấn** — không cần bản ghi nào khớp.

| Hạng mục | Nội dung |
|---|---|
| DN dùng để đo | **`DN-XX-0005`** (`1a715c55-bc31-46de-ae07-56dd4f403ce5`) — dùng chung phiên với `QLHSPLDN_11` / `_12` |
| Tiền đề duy nhất | Thẻ mở được và có 2 ô ngày (*Từ ngày* · *Đến ngày*) |
| Cặp ngày an toàn | **`Từ ngày = 31/12/2026`** · **`Đến ngày = 01/01/2026`** — **không phụ thuộc dữ liệu đối tác**, chắc chắn ngược, và nằm ngoài mọi khoảng ngày cấp thực tế nên không vô tình khớp bản ghi nào |
| Dọn trạng thái trước khi đo | **Clear ô từ khóa và các bộ lọc còn sót từ case trước** (hoặc bấm [Xóa bộ lọc]) rồi mới đặt cặp ngày | 
| 🔴 Cấm | **KHÔNG sửa, KHÔNG xoá** `DN-XX-0005`, `HSPL-20260803-0001`, `HSPL-20260731-0002` và mọi bản ghi QA không tự tạo |

**Nếu DN đang xem không có hồ sơ nào:** vẫn đo được C3 (nhánh này không cần dữ liệu khớp), nhưng nên chạy trên DN có ≥1 hồ sơ để quan sát được mệnh đề *"không trả danh sách theo khoảng ngày ngược"*. Không DN nào có hồ sơ → theo §5 của [`QLHSPLDN_11.md`](QLHSPLDN_11.md).

---

## 6. Chuẩn chấm

### ✅ PASS khi (phải đủ **tất cả**)
1. Trên thẻ có 2 ô ngày và đặt được cặp ngày ngược.
2. Bấm [Tìm kiếm] → bắt được **đúng 1** thông báo.
3. Chuỗi bắt được khớp **từng ký tự** với `Ngày bắt đầu phải trước ngày kết thúc` (`:700`), đọc bằng `innerText`.
4. Hệ thống **không** trả về danh sách kết quả theo khoảng ngày ngược (bảng không đổi theo cặp ngày sai; nếu có lượt gọi máy chủ thì lượt đó bị từ chối).
5. Bấm lặp lần 2 → vẫn **đúng 1** thông báo, không nhân đôi.
6. Bộ bắt thông báo tự kiểm còn sống.
7. Vân tay bản dựng đầu case = cuối case.

### ❌ FAIL khi (chỉ cần **một**)
- Thẻ không có ô ngày ⇒ đúng triệu chứng đối tác báo, Reopen ngay.
- Bấm [Tìm kiếm] với cặp ngày ngược mà **không** hiện thông báo nào (đã chứng minh bộ bắt còn sống).
- Câu hiện ra **lệch dù 1 ký tự** so với `:700`.
- **Nhân đôi thông báo** trong cùng một lượt bấm.
- Hệ thống vẫn chạy tìm kiếm và trả danh sách theo khoảng ngày ngược.
- Lượt gọi máy chủ (nếu có) trả 5xx.

### 🚫 KHÔNG được chấm **Fail** vì
- **Có lượt gọi máy chủ phát sinh** (tức chặn ở máy chủ chứ không ở giao diện). `:700` chỉ quy định **điều kiện lỗi → phản hồi → mức ERROR**, **không** quy định chặn ở tầng nào. Ghi lại số lượt để dev biết, không chấm lỗi.
- **Không thấy mã `ERR-HSPL-06`** trên giao diện — mã là định danh nội bộ của đặc tả.
- Thông báo hiện dạng thanh đỏ đầu trang thay vì lỗi gắn dưới ô nhập (hoặc ngược lại) — SRS không quy định kênh.
- Ô ngày **không chặn nhập** cặp ngược (cho gõ vào rồi mới báo khi bấm) — SRS quy định phản hồi ở nhánh lỗi, không quy định phải khoá ô.
- Cặp ngày **bằng nhau** không báo lỗi — `:596` cho phép `tu_ngay <= den_ngay`, đó là hợp lệ. Ngoài phạm vi phiếu, **không** log, **không** đẩy BA.
- Bảng trên màn có 10 cột — thuộc phạm vi ghi nhận của `QLHSPLDN_14`.

### 🚫 KHÔNG được chấm **Pass** vì
- **Chỉ nhìn thấy 2 ô ngày đã hiện trên màn** (quan sát tĩnh) — cấm tuyệt đối.
- Bắt thông báo bằng cách poll DOM sau khi bấm, hoặc cài bộ bắt **sau** cú bấm.
- Bộ bắt có **lọc trùng** ⇒ không loại được ca nhân đôi ⇒ **Chưa chốt**.
- Đọc bằng `textContent` hoặc so bằng mắt.
- Bỏ lượt bấm lặp lần 2 — thiếu biến thể bắt buộc ⇒ **Chưa chốt**.
- Chỉ chứng minh "có thông báo" mà không chứng minh "không trả kết quả theo khoảng ngày ngược".
- Lấy kết quả Pass ở env nội bộ (bản dựng `V1.0.9`) làm căn cứ.

---

## 7. Câu hỏi BA

**Không có.** Cả 3 vế con đều `MATCH` (xem §2.1); câu chữ ở `:700` trùng khít **từng ký tự** với ô phiếu đối tác. Case này đi thẳng **TEST**.

> Ghi nhận (không thuộc phạm vi phiếu, **không** đẩy BA): `:596` ràng buộc `tu_ngay <= den_ngay` (cho phép bằng nhau) trong khi câu chữ `:700` nói *"phải trước"*. Phiếu chỉ đo nhánh **ngày bắt đầu sau ngày kết thúc**, nên chênh này không chạm phép đo.
