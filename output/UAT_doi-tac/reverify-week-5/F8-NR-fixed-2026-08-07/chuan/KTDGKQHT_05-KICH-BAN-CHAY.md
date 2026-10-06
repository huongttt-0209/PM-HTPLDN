# KỊCH BẢN CHẠY — KTDGKQHT_05 (dòng 10 tab `bug`, lô F8)

> **Đây là bản chạy lại khối `CÁCH VERIFY` đã có sẵn trong ô `Kết quả verify`** (QA viết 02:20 ngày 07/08/2026),
> theo Flow 04 BƯỚC 0 mục 2 — **không** chạy Flow 04 từ đầu.
> Chuẩn chấm + dòng SRS + bẫy: [`KTDGKQHT_05.md`](KTDGKQHT_05.md). Khối gốc:
> [`KTDGKQHT_05-ket-qua-verify-cu-va-CACH-VERIFY.txt`](KTDGKQHT_05-ket-qua-verify-cu-va-CACH-VERIFY.txt).
> Kịch bản này viết cho **người chưa từng chạm phiếu** — làm tuần tự từ trên xuống, không nhảy bước.

**Bug đang verify (một câu):** bấm "Xác nhận import (3 dòng hợp lệ)" sau khi nạp tệp điểm danh thì máy chủ
trả lỗi hệ thống và **không dòng nào được ghi**. Phần "tải mẫu → điền → tải lên" và "bản xem trước" ở lần đo
trước đã đạt — **nhưng vẫn phải đo lại cả ba**, vì bản dựng đã đổi và ô `Trạng thái dev fix` đang là `Fixed`.

---

## 0. Thẻ tóm tắt

| Hạng mục | Giá trị |
|---|---|
| **Môi trường** | `https://18.143.165.120.nip.io` (env **NỘI BỘ**, không phải env nghiệm thu của đối tác) |
| **Hộp thư lấy mã 6 số** | `http://18.143.165.120:8025` (MailHog, không cần đăng nhập) |
| **Tài khoản** | **`cbnv_tw_03`** / `Test@1234` — vai trò **Cán bộ Nghiệp vụ Trung ương** (`CB_NV_TW`) |
| **Fallback nếu khóa** | `cbnv_tw_04` → `cbnv_tw_05` (**cùng vai trò + cùng cấp**). 🔴 **CẤM** đổi sang vai trò/cấp khác. **Ghi rõ tài khoản thực dùng** trong `do/` và trong ô `Kết quả verify` |
| **`admin`** | Chỉ được dùng để **điều tra/dựng dữ liệu**, **KHÔNG** dùng để ra verdict |
| **Màn đo** | Đào tạo, tập huấn → Khóa học → *(mở khóa)* → **Tab "Điểm danh"** |
| **Công cụ** | Chrome DevTools MCP (`mcp__chrome-devtools__*`). 🔴 **Chỉ MỘT tác nhân dùng trình duyệt tại một thời điểm** — xác nhận trình duyệt đang rảnh trước khi bắt đầu |
| **Thời lượng ước tính** | ~35–45 phút nếu tiền đề còn nguyên |
| **Ghi kết quả** | Chỉ chạm **2 ô**: `Trạng thái dev fix` (R) + `Kết quả verify` (T). Ô `Trạng thái` (N), `Kết quả thực tế` (L), `TKM phản hồi lần 1` (Q), `DEV phản hồi lần 1` (S) là **chỉ đọc** |

**Ba vế phải trả lời (chi tiết chuẩn ĐẠT ở [`KTDGKQHT_05.md`](KTDGKQHT_05.md) §3):**

| Vế | Câu hỏi | Bước |
|---|---|---|
| **C3** | Nút "Tải mẫu điểm danh" có, bật đúng lúc, tệp sinh ra đúng bộ cột + có metadata buổi? | 4 |
| **C1** | Bản xem trước hiện TRƯỚC khi ghi, tách hợp lệ/lỗi, mỗi dòng lỗi có lý do + số dòng? | 6 |
| **C2** | Bấm xác nhận → có báo cáo kết quả nạp (số thành công + số không hợp lệ) **và** đúng 3 dòng được ghi thật? | 7 + 8 |

---

## 1. BƯỚC 0 — đọc lại dòng 10 trên bảng (trước khi đụng web)

Nguồn có thể đã đổi từ lúc chụp phạm vi (07/08 ~11:3x).

1. Mở tab `bug` (spreadsheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, gid `1714340219`), **dòng 10**.
2. Đọc và chép lại vào `do/KTDGKQHT_05.md`: ô `Trạng thái dev fix` (R), `DEV phản hồi lần 1` (S), `Kết quả verify` (T).
3. 🔴 **Lưu nguyên văn ô `T` hiện tại vào `audit/KTDGKQHT_05-ket-qua-verify-truoc-luot-F8.txt`** trước khi ghi đè.
   Ô này đang chứa khối `CÁCH VERIFY` — mất là mất bản giao việc cho dev.
4. **Ghi nhận mâu thuẫn** (xem [`KTDGKQHT_05.md`](KTDGKQHT_05.md) §4): ô R đang là `Fixed` dù QA kết luận
   **Reopen** lúc 02:20 cùng ngày. Không suy diễn — chỉ ghi nhận và **chạy lại thật**.
   - Ô S (`DEV phản hồi lần 1`) nếu **đã có nội dung mới** → đọc, nhưng **không** dùng làm căn cứ verdict
     (Flow 04: *"Dev mô tả fix ở chỗ khác với triệu chứng → vẫn chạy đủ luồng, đừng tin mô tả"*).

---

## 2. BƯỚC 1 — vân tay bản dựng (đầu phiên)

Env này deploy liên tục (V1.0.8 → V1.0.10 trong ~10 giờ ngày 06–07/08). Verdict chỉ có hiệu lực cho **đúng bản dựng đã đo**.

```bash
curl -skI https://18.143.165.120.nip.io/ | grep -i -E "last-modified|etag"
curl -sk  https://18.143.165.120.nip.io/ | grep -o 'assets/index-[A-Za-z0-9_-]*\.js'
```

Ghi cả 3 giá trị vào `do/`. **Đo lại y hệt ở cuối phiên (Bước 9).**

**Mốc lần đo trước (02:20 07/08) để so:** `Last-Modified: Thu, 06 Aug 2026 18:51:25 GMT` · `ETag: W/"6a74d7ad-428"` ·
bó mã `assets/index-DsMHK7Dp.js` · nhãn chân sidebar `HTPLDN · V1.0.9`.

⚠️ Nhãn `V1.0.x` ở chân thanh bên **KHÔNG** phải định danh bản dựng (đã có ca lùi nhãn: bó mã mới hơn mà nhãn lại là V1.0.9). Ghi cả nhãn lẫn bó mã.

---

## 3. BƯỚC 2 — đăng nhập bằng UI thật

Theo mẫu ở `docs/htpldn-mcp-patterns.md`. Tóm tắt:

1. `new_page` → `https://18.143.165.120.nip.io/login`.
2. `wait_for(["Nhập tên đăng nhập"])` (app render chậm, timeout ≥10000ms) → `take_snapshot` lấy `uid` mới.
3. `fill_form`: `input[placeholder="Nhập tên đăng nhập"]` = `cbnv_tw_03`, `input[placeholder="Nhập mật khẩu"]` = `Test@1234`.
   ⚠️ Form login hay giữ lại chữ cũ — **xóa sạch ô trước khi gõ**, đừng để nối chuỗi.
4. Bấm Đăng nhập → chờ màn mã xác thực → lấy mã 6 số:

```bash
curl -s "http://18.143.165.120:8025/api/v2/messages?limit=25" | python3 -c "
import sys,json,re
d=json.load(sys.stdin)
for m in d['items']:
    box=m['To'][0]['Mailbox'].lower()
    if box in ('cbnv_tw_03','cbnv.tw.03'):
        print(box, re.search(r'\b(\d{6})\b', m['Content']['Body']).group(1)); break
"
```

5. Gõ mã vào 6 ô `input[inputmode="numeric"][maxlength="1"]` → chờ vào được trang chủ.
6. **Điều hướng bằng CLICK sidebar**, KHÔNG `navigate_page` sau khi đăng nhập (reload = mất phiên, bị đá về `/login`).
   Sidebar đang thu gọn → bấm "Thu gọn menu" để mở rộng trước khi bấm submenu lần đầu.
7. Ghi vào `do/`: tài khoản thực dùng, vai trò hệ thống trả về, đơn vị.

**Nếu `cbnv_tw_03` không đăng nhập được** (toast "Tài khoản tạm khóa" / "Tên đăng nhập hoặc mật khẩu không đúng" / HTTP 401):
- Chụp màn + đọc lỗi + ghi mã lỗi vào `do/` **trước khi** đổi tài khoản.
- Đổi sang `cbnv_tw_04`, hết thì `cbnv_tw_05`. **Ghi rõ tài khoản thực dùng** vào `do/` **và** vào ô `Kết quả verify`.
- **Không** thử lại cùng tài khoản ≥3 lần (thêm khóa; env có chặn tần suất đăng nhập).
- Hết cả `_03/_04/_05` → **dừng, mark Chưa chốt**, báo điều phối, **không** đổi vai trò/cấp.

---

## 4. BƯỚC 3 — kiểm tiền đề (BẮT BUỘC, đừng tin ghi chép cũ)

**Khóa dự kiến:** `KH-QAW7-HOINGHI` — "QAW7 — Hội nghị đối thoại DN 2026"
`khoa_hoc_id = a7480002-0000-4000-8000-000000000002`
**Buổi dự kiến:** **Buổi 4** — 11/05/2026 · 14:00–16:00 — `lich_hoc_id = bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2`

Lấy token để đọc đối chứng (không thay thao tác UI, chỉ để đọc):

```bash
TOKEN=$(/tmp/login.sh cbnv_tw_03)        # in ra accessToken; phiên rảnh 30 phút
KH=a7480002-0000-4000-8000-000000000002
LH=bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2
BASE=https://18.143.165.120.nip.io/api/v1
```

> `/tmp/login.sh` là tệp tạm, có thể đã bị dọn. Không còn → dựng lại theo brief lô F8 §3
> (đăng nhập lấy `otpToken` → lấy mã 6 số ở MailHog → `verify-otp` → `accessToken`).
> Bearer trả 401 → token nằm ở cookie: đối chứng bằng `fetch(..., {credentials:'include'})` chạy trong chính tab đã đăng nhập.

### 4.1 — Khóa còn "Đang diễn ra"? (T1)

Mở khóa trên UI, đọc **thanh bước trạng thái** ở đầu màn chi tiết: bước "Đang diễn ra" phải đang sáng
(lớp `ant-steps-item-process ant-steps-item-active`).

| Kết quả | Xử lý |
|---|---|
| **Đang diễn ra** | ✅ chạy tiếp |
| **Đã kết thúc** | ⛔ **KHÔNG đo trên khóa này**, và **KHÔNG** chấm Fail vì bị chặn — đặc tả (`srs-fr-03-dao-tao.md:536`, `:640`, `:659`, `:1923`) **bắt buộc** đóng điểm danh khi khóa kết thúc. Chuyển sang khóa khác đang `DANG_DIEN_RA` (§4.5). **Cấm ép lùi trạng thái khóa** |
| Trạng thái khác (`DU_THAO`/`DA_CONG_KHAI`…) | ⛔ như trên — đổi khóa |

⚠️ Ô `Điều kiện` của phiếu đối tác ghi *"Đang diễn ra **hoặc Đã kết thúc**"* — vế "Đã kết thúc" **lệch đặc tả**.
Phải đo trên **Đang diễn ra**; ghi chênh lệch tiền đề này vào ô `Kết quả verify`.

### 4.2 — Còn ≥4 học viên "Đã duyệt"? (T3)

```bash
curl -sk -H "Authorization: Bearer $TOKEN" "$BASE/khoa-hocs/$KH/dang-ky-dao-taos" | python3 -m json.tool
```
Hoặc đọc trực tiếp tab **"Học viên"** trên UI.

- **Đủ ≥4 `Đã duyệt`** → chạy tiếp.
- **Thiếu** → vào tab "Học viên", bấm **"Phê duyệt"** các đăng ký đang `Chờ duyệt` cho đủ 4
  (lượt trước còn 2 đăng ký chờ: "Nguyễn Văn Ngọc", "QA Probe Email").
  🔴 **Đây là mutate môi trường chung ⇒ BẮT BUỘC khai vào `do/` và vào ô `Kết quả verify`:
  đổi bản ghi nào (id đăng ký + tên học viên) · đổi gì (`Chờ duyệt → Đã duyệt`) · trên env nào.**
- Không duyệt được và không có khóa nào khác đủ ≥4 HV → **Chưa chốt**, nêu rõ thiếu gì. **Cấm** kết luận "không phải lỗi".

### 4.3 — 🔴 Buổi đo còn SẠCH? (T5 — bước dễ bị bỏ nhất)

```bash
curl -sk -H "Authorization: Bearer $TOKEN" "$BASE/khoa-hocs/$KH/diem-danhs?lichHocId=$LH" | python3 -m json.tool
```

**Chép nguyên mốc gốc vào `do/` (tên học viên → `trangThai` → `id` bản ghi) TRƯỚC KHI NẠP.**

| Mốc gốc | Xử lý |
|---|---|
| **0 học viên có `trangThai`** (tất cả `trangThai = null`, `id = ""`) | ✅ Buổi sạch — dùng Buổi 4, chạy tiếp |
| **Có ≥1 học viên đã mang `trangThai`** | ⚠️ **Dữ liệu không còn sạch** (lượt đo trước lỗi 500 nên đáng lẽ không ghi gì; có `trangThai` nghĩa là đã có ai đó điểm danh sau đó). Theo thứ tự ưu tiên: **(a)** đổi sang **buổi khác của cùng khóa** đang sạch (Buổi 1/2/3) — tệp mẫu tải ở buổi nào thì tự mang `lich_hoc_id` buổi đó, **không phải sửa tay gì**; **(b)** hết buổi sạch → đổi **khóa khác** đủ điều kiện (§4.5); **(c)** hết cả hai → vẫn đo được nhưng **chấm bằng delta**: so từng học viên trước/sau, chỉ tính "3 học viên đổi trạng thái **mới**". 🔴 Không ghi mốc gốc trước khi bấm ⇒ **CẤM chốt** |

### 4.4 — Học viên của khóa KHÁC còn dùng được? (T4)

Dòng lỗi số 1 của fixture cần một `hoc_vien_id` **thuộc khóa khác** để ép `ERR-KQ-03`
(đặc tả `:592` đòi học viên phải **TỒN TẠI VÀ THUỘC** khóa đang thao tác).

- Mặc định: `cccccccc-0000-4000-8000-000000000001` — "Nguyễn Văn Học Viên", khóa `DDD-KH-011`, `DA_DUYET`.
- Kiểm bằng cách đọc danh sách học viên của khóa đó (endpoint `…/khoa-hocs/{id}/dang-ky-dao-taos` — **đã lộ trên màn**, không phải đoán).
- Không còn → lấy `hoc_vien_id` khác từ một khóa bất kỳ **khác** khóa đang đo, truyền vào script bằng `--hv-khoa-khac`.
- ⚠️ Dùng UUID bịa cũng ra `ERR-KQ-03`, **nhưng chỉ chứng minh "không tồn tại"**, không chứng minh được ràng buộc
  "phải THUỘC khóa". Ưu tiên học viên thật của khóa khác.

### 4.5 — Nếu phải đổi khóa

Khóa thay thế phải đồng thời: `DANG_DIEN_RA` · có ≥1 buổi học · có **≥4 học viên `Đã duyệt`** · nằm trong phạm vi đơn vị của tài khoản đang dùng.
Ghi rõ khóa mới (mã + `khoa_hoc_id`) và buổi mới (`lich_hoc_id`) vào `do/` — mọi số dòng/ID trong kịch bản này phải đổi theo.
**Cấm đụng dữ liệu của đối tác** (khóa `0aad5545-9361-4fe4-854a-18e3fdce5862` trong ảnh đối tác nằm trên env khác, không có ở đây).

---

## 5. BƯỚC 4 — vế **C3**: tải tệp mẫu điểm danh

1. Trong màn chi tiết khóa → bấm tab **"Điểm danh"**.
2. **Trước khi chọn buổi**, ghi nhận: nút "Tải mẫu điểm danh" có mặt không, có đang **tắt** không.
   Đọc trạng thái nút bằng `evaluate_script` (chỉ trả đúng thứ cần, không dump DOM):

```js
() => [...document.querySelectorAll('button')]
  .filter(b => b.innerText.includes('Tải mẫu'))
  .map(b => ({ chu: b.innerText.trim(), tat: b.disabled }))
```

3. Chọn buổi ở ô **"Chọn buổi học để điểm danh"** → chọn đúng buổi đã chốt ở Bước 3.
4. Chạy lại đoạn script trên → nút phải chuyển sang **bật** (`tat: false`).
   *(Điều kiện bật theo `srs-fr-03-dao-tao.md:577`: đã chọn buổi + khóa `DANG_DIEN_RA` + khóa có ≥1 buổi + có quyền.)*
5. **Bấm nút "Tải mẫu điểm danh"** — bấm thật bằng UI, không gọi API.
6. Tìm tệp vừa tải. Lượt trước tệp về `~/Downloads/mau-diem-danh-<khoa_hoc_id>.xlsx`.

```bash
ls -lt ~/Downloads/*.xlsx | head -5
```

⚠️ Chrome của MCP chạy hồ sơ tách biệt (`--isolated`) nên **có thể không đổ tệp về `~/Downloads`**.
Không thấy tệp → xem `chrome://downloads` trong chính tab đó để lấy đường dẫn thật.

7. **Lưu bản gốc nguyên trạng** (để truy lại nội dung về sau):

```bash
cp <tệp vừa tải> "output/UAT_doi-tac/reverify-week-5/F8-NR-fixed-2026-08-07/files/mau-goc-KTDGKQHT_05-<mốc giờ>.xlsx"
```

8. **Đọc nội dung tệp thật** (đây là đối chứng độc lập của C3, không phải nhìn màn hình):

```bash
cd "output/UAT_doi-tac/reverify-week-5/F8-NR-fixed-2026-08-07"
python3 chuan/KTDGKQHT_05-dien-file-mau.py <tệp mẫu vừa tải> --chi-doc
```

**C3 đạt khi in ra đủ:** 2 sheet (`_HTPLDN_META` ẩn + sheet dữ liệu) · `template_type = DIEM_DANH` ·
`lich_hoc_id` **khớp đúng buổi vừa chọn** · bộ cột `hoc_vien_id · Họ tên · Email · Đơn vị · Trạng thái điểm danh · Ghi chú`
đúng thứ tự · `hoc_vien_id` **điền sẵn** đủ học viên · cột "Trạng thái điểm danh" **rỗng 100%**.
Script tự in "✅/❌" cho từng mục — **chép nguyên phần in ra vào `do/`**.

**Quan sát bắt buộc ghi nhận (không mở thêm phép đo):** cột trạng thái phải là **3 giá trị**
Có mặt / Vắng có phép / Vắng không phép. Nếu quay lại dạng nhị phân `Co mat (1/0)` như ảnh đối tác 24/07
→ đó là **một phần của C3 không đạt**, ghi vào chính vế C3, **không** tách thành bug riêng.

📸 **Ảnh cần chụp:** (1) tab Điểm danh khi **chưa chọn buổi** (nút tắt); (2) sau khi **đã chọn buổi** (nút bật, thấy rõ thanh bước "Đang diễn ra" + nhãn phiên bản ở chân sidebar).

---

## 6. BƯỚC 5 — dựng tệp fixture (3 hợp lệ + 2 cố ý sai)

🔴 **CẤM tự tạo tệp từ đầu và CẤM viết chuỗi ký tự rồi đổi đuôi `.xlsx`.**
Tệp phải bắt nguồn từ chính tệp mẫu vừa tải, vì `lich_hoc_id` nằm ở sheet metadata `_HTPLDN_META`;
tệp tự dựng sẽ bị `ERR-KQ-09` (đặc tả `:583`, `:590`, `:643`) → **FAIL oan**.

```bash
cd "output/UAT_doi-tac/reverify-week-5/F8-NR-fixed-2026-08-07"
python3 chuan/KTDGKQHT_05-dien-file-mau.py <tệp mẫu vừa tải>
# học viên khóa khác khác mặc định:
#   ... <tệp mẫu> --hv-khoa-khac <uuid> --ten-hv-khoa-khac "<họ tên>"
```

Script tự làm: kiểm metadata + bộ cột → điền 3 dòng hợp lệ → chèn 2 dòng sai → ghi ra
`files/fixture-KTDGKQHT_05-3hople-2loi-<mốc giờ>.xlsx` → **mở lại tệp vừa ghi và in toàn bộ để tự kiểm**.

**Bố cục fixture sinh ra:**

| Dòng Excel | Nội dung | Kỳ vọng |
|---:|---|---|
| 2 | học viên 1 của khóa · `Có mặt` | hợp lệ |
| 3 | học viên 2 của khóa · `Vắng có phép` | hợp lệ |
| 4 | học viên 3 của khóa · `Vắng không phép` | hợp lệ |
| 5 | **học viên của KHÓA KHÁC** · `Có mặt` | **lỗi `ERR-KQ-03`** (`:592`, `:637`) |
| 6 | học viên 4 của khóa · **`XYZ`** | **lỗi `ERR-KQ-04`** (`:638`) |

**Vì sao 3 hợp lệ / 2 lỗi (không phải 1/1 hay 2/2):** hai con số **khác nhau** ⇒ bắt được lỗi hoán vị
(in số lỗi vào ô số thành công); mỗi nhóm **≥2** ⇒ bắt được số đếm cứng; tổng **5** ⇒ kiểm được phép cộng khớp.

🔴 **CẤM dùng "Vắng có phép" làm dòng lỗi cố ý** — đó là giá trị **hợp lệ** theo `:549`, dùng làm dòng lỗi sẽ phá thiết kế đếm 3/2.

**Script dừng và báo lỗi trong các ca sau — làm đúng lời nó bảo:**
- Tệp mẫu **< 4 học viên** → quay lại §4.2 duyệt thêm đăng ký, tải lại mẫu, chạy lại.
- `template_type` **≠ `DIEM_DANH`** → đang cầm nhầm mẫu điểm kiểm tra; tải lại ở Tab 4.
- **Bộ cột lệch đặc tả** → đây là số đo của C3: **ghi lệch đó vào `do/` trước**, rồi mới cân nhắc `--bo-qua-kiem-cot`.

---

## 7. BƯỚC 6 — vế **C1**: bản xem trước

1. Ở tab Điểm danh (vẫn đúng buổi đã chọn) → bấm **"Import Excel"** → hộp thoại **"Import điểm danh từ Excel"**.
2. **Ghi lại nguyên văn dòng chú thích trong hộp thoại** (nó cho biết hệ thống đang đòi định dạng nào).
   Lượt trước: *"File .xlsx, tối đa 5MB. Chỉ dùng tệp từ nút Tải mẫu điểm danh. Hệ thống chỉ ghi dữ liệu sau khi bạn xem trước và xác nhận."*
3. `upload_file` **tệp fixture** vào vùng thả tệp.
4. Bấm **"Kiểm tra tệp"**. 🔴 **DỪNG LẠI — chưa bấm xác nhận.**
5. Đọc khối xem trước bằng **`innerText`** (KHÔNG `textContent` — gom cả node ẩn của AntD → số ma):

```js
() => {
  const d = document.querySelector('.ant-modal-body, .ant-drawer-body');
  return d ? d.innerText : '(không thấy hộp thoại)';
}
```

6. **Đối chứng độc lập:** `list_network_requests` → `get_network_request` lấy **response body** của chính
   request xem trước (lượt trước: `POST /api/v1/khoa-hocs/{KH}/diem-danhs/import/preview`, multipart `file` + `lichHocId`).
   Ghi lại `sessionId` trả về — bước xác nhận dùng nó.

**C1 đạt khi:**
- Khối xem trước hiện ra **TRƯỚC** khi ghi dữ liệu (có nút xác nhận riêng, ví dụ *"Xác nhận import (3 dòng hợp lệ)"*).
- Tách rõ **nhóm hợp lệ vs nhóm lỗi**, đếm được cả hai.
- **Mỗi dòng lỗi** có mã lỗi/lý do **kèm số dòng**, và **2 lý do KHÁC NHAU**: dòng 5 → học viên không thuộc khóa
  (`ERR-KQ-03`), dòng 6 → giá trị điểm danh không hợp lệ (`ERR-KQ-04`).
- **Cộng khớp:** hợp lệ + bỏ qua + lỗi = **5** = tổng dòng fixture. Không khớp ⇒ **số đang sai, chưa được chốt** — đo lại.
- Chữ trên màn và response body **khớp nhau**. Mâu thuẫn ⇒ **chưa chốt**, ghi cả hai, hỏi điều phối.

📸 **Ảnh cần chụp:** khối xem trước đầy đủ (dải số + thẻ "Lỗi/Bỏ qua" mở ra thấy cả 2 dòng lỗi + nút xác nhận).

⚠️ **Chặn FAIL oan:** đặc tả `:593` **không** đòi in con số tổng — nếu vẫn đếm được hai nhóm từ danh sách dòng thì **không** chấm Fail chỉ vì thiếu con số tổng.

---

## 8. BƯỚC 7 — vế **C2** (phần đang tranh chấp): bấm xác nhận nạp

🔴 **Đây là bước quyết định. Bắt buộc bấm bằng UI thật, không gọi API thay.**

1. **Cài bộ bắt thông báo TRƯỚC khi bấm** (thông báo AntD tự tắt <5s). **CẤM lọc trùng.**

```js
() => {
  window.__bat = [];
  const t0 = performance.now();
  new MutationObserver(ms => {
    for (const m of ms) for (const n of m.addedNodes) {
      if (n.nodeType !== 1) continue;
      const cls = n.className && n.className.toString ? n.className.toString() : '';
      if (/ant-message|ant-notification|ant-alert/.test(cls) || n.getAttribute?.('role') === 'alert') {
        window.__bat.push({ dt: Math.round(performance.now() - t0), cls, chu: n.innerText });
      }
    }
  }).observe(document.body, { childList: true, subtree: true });
  return 'da-cai';
}
```

2. Bấm **"Xác nhận import (…)"**.
3. Sau 2–5 giây, đọc `window.__bat`:

```js
() => window.__bat
```

4. **Đếm số thông báo theo MỐC GIỜ khác nhau**, không theo độ dài mảng — một thông báo AntD thường sinh
   2 node (thẻ bọc `.ant-message` + thẻ con `.ant-message-notice-wrapper`) cùng `dt`, đó vẫn là **1** thông báo.
5. `list_network_requests` → lấy request xác nhận nạp (lượt trước: `POST …/diem-danhs/import/confirm`,
   body `{lichHocId, sessionId}`). **Ghi lại mã HTTP + response body nguyên văn.**
   Đếm luôn số request phát sinh kèm cú bấm (để loại trừ double-submit).

📸 **Ảnh cần chụp:** một khung chứa đồng thời khối xem trước + nút xác nhận + thông báo hiện ra.
Thông báo tự tắt rất nhanh → **hẹn giờ bấm rồi mới chụp** (bấm sau ~2500ms, gọi chụp trước). Trượt ảnh thì
**response body là bằng chứng mạnh hơn ảnh** — đừng bấm lại lần nữa chỉ để chụp (bấm lại = ghi dữ liệu thêm lần nữa).

---

## 9. BƯỚC 8 — đường đo thứ hai (bắt buộc): đọc lại dữ liệu điểm danh của **đúng buổi**

Không có bước này thì **cấm chốt** — thông báo trên màn không chứng minh được dữ liệu đã ghi.

```bash
curl -sk -H "Authorization: Bearer $TOKEN" "$BASE/khoa-hocs/$KH/diem-danhs?lichHocId=$LH" | python3 -m json.tool
```

**và** đối chiếu trên UI: tải lại tab "Điểm danh", chọn lại **đúng buổi đó**, đếm số học viên đã có trạng thái.

**So với mốc gốc đã ghi ở §4.3:**

| Học viên | trạng thái **trước** | trạng thái **sau** | kỳ vọng |
|---|---|---|---|
| HV1 (dòng 2) | *(mốc gốc)* | | **Có mặt** |
| HV2 (dòng 3) | *(mốc gốc)* | | **Vắng có phép** |
| HV3 (dòng 4) | *(mốc gốc)* | | **Vắng không phép** |
| HV4 (dòng 6, `XYZ`) | *(mốc gốc)* | | **KHÔNG đổi** (dòng lỗi bị bỏ qua, `:594`) |
| HV khóa khác (dòng 5) | — | | **KHÔNG có mặt trong buổi này** |

⚠️ Đếm bằng số thô trước, đừng lọc/gộp rồi mới nhìn. Đếm dòng bảng dễ **nhân đôi** vì thẻ bọc lồng thẻ con —
ưu tiên con số từ dữ liệu máy chủ trả về.

---

## 10. BƯỚC 9 — vân tay bản dựng (cuối phiên)

Chạy lại đúng 2 lệnh ở Bước 1. Khác đầu phiên ⇒ **có deploy giữa lượt**: ghi rõ quan sát nào rơi trước, quan sát nào rơi sau mốc deploy, và cân nhắc đo lại phần bị ảnh hưởng.

---

## 11. Chấm điểm

### ✅ PASS (cả 3 vế) khi đủ **tất cả**:
1. **C3** — nút "Tải mẫu điểm danh" tắt khi chưa chọn buổi, bật sau khi chọn; tệp tải về mở được, đúng 6 cột `:581`, `hoc_vien_id` điền sẵn, cột trạng thái rỗng, `lich_hoc_id` nằm ở metadata và khớp buổi đang chọn.
2. **C1** — bản xem trước hiện **trước** khi ghi; tách hợp lệ/lỗi; **3 hợp lệ · 2 lỗi · tổng 5**; 2 dòng lỗi có **2 lý do khác nhau gắn đúng số dòng**; màn và response body khớp nhau.
3. **C2** — bấm xác nhận **không còn báo lỗi hệ thống**; hệ thống hiển thị **báo cáo kết quả nạp có nêu số bản ghi nạp thành công và số bản ghi không hợp lệ**; và ở Bước 8 đếm được **ĐÚNG 3 học viên có trạng thái điểm danh mới**, đúng 3 giá trị đã điền, còn **2 học viên ở 2 dòng lỗi KHÔNG được ghi**.

### ❌ FAIL khi bất kỳ điều nào sau xảy ra:
- Bấm xác nhận vẫn trả lỗi hệ thống (lượt trước: HTTP 500, `ERR-SYS-00-00-01`).
- Báo cáo hiện ra nhưng **số học viên thực sự được ghi khác 3** — **kể cả ca "đúng một phần"**: ghi 1–2 dòng, hoặc ghi luôn cả dòng lỗi thành 4–5 dòng.
- Báo cáo **không cho biết** số nạp thành công và số không hợp lệ.
- Bản xem trước không tách được hợp lệ/lỗi, hoặc 2 dòng lỗi gộp chung một lý do, hoặc không gắn số dòng.
- Không có nút "Tải mẫu điểm danh", hoặc tệp mẫu thiếu `hoc_vien_id` điền sẵn / thiếu metadata buổi / sai bộ cột.

### ⏸ CHƯA CHỐT khi:
- Hai phép đo **mâu thuẫn** (màn nói 3, dữ liệu đọc lại nói khác) → ghi cả hai, hỏi điều phối, **không** tự chọn bên nào.
- Không dựng được tiền đề (không có khóa `DANG_DIEN_RA` nào đủ ≥4 học viên `Đã duyệt`).
- Không đăng nhập được bằng cả `cbnv_tw_03/_04/_05`.
- 🔴 **Không ghi mốc gốc trước khi nạp** → không chứng minh được "3 trạng thái MỚI" → chưa được chốt.

---

## 12. Bẫy chấm oan — đọc lại trước khi viết verdict

### Chặn **FAIL oan**
1. **Đừng** chấm Fail vì **câu chữ** thông báo khác chuỗi trong phiếu — đặc tả `:595` chỉ ghi *"Trả về báo cáo import"*, bảng lỗi `:633–643` **không có** thông báo thành công nào. Chấm theo **2 con số** và theo **số bản ghi thực ghi**.
2. **Đừng** chấm Fail nếu thao tác bị chặn khi khóa đã **Đã kết thúc** — `:536`, `:640`, `:659`, `:1923` bắt buộc đóng điểm danh khi khóa kết thúc. Phải đo trên khóa **Đang diễn ra**.
3. **Đừng** chấm Fail vì tab Điểm danh **không có cột "Mã học viên"** — `:1919` chốt bộ cột không có nó; `:14` và `srs-v3.5.md:75` chốt **không** thêm `ma_hoc_vien` vào học viên. Đề xuất "thêm cột MHV" của TKM **đã được BA trả lời** bằng chính cơ chế tệp mẫu.
4. **Đừng** chấm Fail vì bản xem trước không in con số tổng, nếu vẫn đếm được hai nhóm.
5. **Đừng** chấm Fail vì tên tệp mẫu không theo khuôn đặt tên chung — `srs-v3.5.md:6760` loại trừ tường minh tệp mẫu nhập liệu.
6. **Đừng** chấm Fail vì `hoc_vien_id` là chuỗi UUID khó đọc — `:581` quy định đúng là "ID nội bộ opaque, cán bộ không sửa", khoá/ẩn là **đúng**.

### Chặn **PASS oan**
7. **Đừng** chấm Pass chỉ vì thấy bản xem trước ra đủ 3/2 — phần đó lượt trước **đã đạt sẵn**; lỗi nằm ở bước **SAU** khi bấm xác nhận. Bắt buộc **bấm xác nhận thật** rồi **đọc lại dữ liệu buổi học**.
8. **Đừng** chấm Pass bằng quan sát tĩnh ("thấy nút rồi", "màn trông đúng").
9. Chữ người dùng nhìn thấy đọc bằng **`innerText`**; bộ bắt thông báo **cấm lọc trùng**; đếm thông báo theo **mốc giờ**.
10. **Tab mở lâu vẫn chạy mã cũ** → tải lại trang trước lô đo, ghi nhãn phiên bản ở chân thanh menu + bó mã.
11. Các chiều số **phải cộng khớp** (3 + 0 + 2 = 5). Không khớp ⇒ số đang sai.

### Ghi nhận, **không** mở phép đo
12. Nếu bảng điểm danh hiện **bảng trống không chú thích** khi chưa chọn buổi (đặc tả `:660`, `:1921` đòi dòng *"Vui lòng chọn buổi học để bắt đầu điểm danh"*) → đó là vế của phiếu **KTDGKQHT_03**, ghi **candidate một dòng**, không điều tra, không đổi verdict phiếu này.
13. **Bug mới tự lộ:** chỉ ghi sai lệch trong chính màn/phản hồi/tệp đang quan sát. Cả phiếu chỉ được thêm **tối đa 1 phép xác nhận**; không đủ căn cứ → ghi **candidate**, dừng.

---

## 13. Sau khi đo — viết hồ sơ và ghi bảng

| Thứ tự | Việc | Tệp / nơi |
|---|---|---|
| 1 | Nhật ký đo: tài khoản thực dùng · vân tay bản dựng đầu+cuối · tiền đề (ID khóa/buổi/học viên) · **mốc gốc trước khi nạp** · số đo từng vế · response body · dữ liệu đã seed/mutate · kết luận từng vế | `do/KTDGKQHT_05.md` |
| 2 | Ảnh bằng chứng, mỗi ảnh nêu rõ **nó chứng minh điều gì** + mốc giờ; **mở lại xem** trước khi gắn link | `image/KTDGKQHT_05-<số>-<mô-tả>.png` |
| 3 | Tải ảnh lên Drive lấy link xem được | `python3 tools/drive_upload_f8.py --file <ảnh> --label "<mã TC + vế + chứng minh gì>"` |
| 4 | Soạn nội dung ô `Kết quả verify` | `note/KTDGKQHT_05.txt` |
| 5 | Ghi bảng: `--dry-run` trước, đọc kỹ old→new, rồi ghi thật, rồi **đọc lại xác nhận** | lệnh `tools/sheet_bug_verify_write.py` ở brief lô F8 §5 |

**Nội dung ô `Kết quả verify` bắt buộc có:**
- Đo trên **env nội bộ** `https://18.143.165.120.nip.io` + **bó mã bản dựng** + thời điểm đo.
- **Tài khoản đã dùng** (`cbnv_tw_03` hay bản fallback).
- Tiền đề: khóa nào, buổi nào, mấy học viên.
- Dữ liệu đã seed/mutate (nếu có duyệt thêm học viên).
- Câu giới hạn hiệu lực: verdict chỉ áp cho env + bản dựng đã đo; đối tác đo trên `htpldn-uat.ospgroup.vn` bản V1.0 ngày 24/07/2026.
- Chênh lệch tiền đề: phiếu ghi điều kiện *"Đang diễn ra hoặc Đã kết thúc"* nhưng đặc tả chỉ cho **Đang diễn ra**.
- Tiếng Việt cho người đọc nghiệp vụ; **không** thuật ngữ Anh, **không** đường dẫn tệp trên máy QA.

**Ánh xạ ô `Trạng thái dev fix` (R):** `Pass → Test done` · `Reopen → Reopen` · `Cần BA → BA confirm` ·
`Không phải lỗi → Test done` + ô T mở đầu `❌ Không phải lỗi` · `Chưa chốt → KHÔNG ghi ô R`, chỉ ghi ô T nêu blocker rồi báo điều phối.

**Verdict `Reopen` bắt buộc kèm khối `── CÁCH VERIFY sau Dev fix ──` cập nhật trong ô T** (mẫu ở Flow 04 §Hồ sơ tái hiện).

### 🔴 Điểm phải hỏi điều phối TRƯỚC khi ghi ô R (nếu C1+C2+C3 đều đạt)

Đặc tả **im lặng về câu chữ** của thông báo kết quả nạp, trong khi đối tác kỳ vọng đúng chuỗi
*"Đã nạp {số thành công} bản ghi thành công, {số lỗi} bản ghi không hợp lệ"*
(`:595` chỉ ghi "Trả về báo cáo import"; bảng lỗi `:633–643` không có thông báo thành công nào).
Đây là vế **`GAP`** (`G1` ở [`KTDGKQHT_05.md`](KTDGKQHT_05.md) §3), mà theo Flow 04 §Verdict thì còn `GAP` là
**không được Pass sạch**. Lần đo 02:20 xếp nó là "ghi chú mềm" vì lúc đó C2 hỏng nên verdict đằng nào cũng là `Reopen`.
Lần này nếu C2 đạt thì **phải quyết**, mà ô R chỉ nhận một giá trị.
⇒ **Hỏi điều phối chọn `Test done` (kèm nêu điểm cần BA trong ô T) hay `BA confirm`.**
**Cấm** tự hạ `G1` từ `GAP` xuống `MATCH` để lấy `Test done`.

---

## 14. Nếu gặp blocker

Ghi **Chưa chốt**, nêu **đúng** dữ kiện còn thiếu, **không dừng chờ** — báo lại ở bàn giao cuối
(`BAN-GIAO-<mã lô con>.md`). Đừng kết luận "không phải lỗi" chỉ vì không tái hiện được.
