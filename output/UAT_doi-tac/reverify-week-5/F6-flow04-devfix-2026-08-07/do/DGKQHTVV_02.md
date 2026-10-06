# Hồ sơ đo — DGKQHTVV_02 (dòng 65) — GIAI ĐOẠN B

**Chuẩn chấm đã khóa:** [`../chuan/DGKQHTVV_02.md`](../chuan/DGKQHTVV_02.md) — 6 vế: `C1` `C3` `C4` route TEST · `C2` `C3b` `C5` route BA.
**Ô "Kết quả verify" trước khi ghi:** RỖNG ([`../audit/DGKQHTVV_02-ketqua-verify-CU.md`](../audit/DGKQHTVV_02-ketqua-verify-CU.md)).
**Bằng chứng đối tác:** KHÔNG CÓ (cột "Ảnh/vieo 1" của dòng 65 rỗng cả chữ lẫn liên kết) ⇒ tiền đề tái hiện suy từ chính "Điều kiện" + "Các bước" ghi trên phiếu, khai rõ ở §2.

---

## 1. Môi trường · bản dựng · tài khoản

| Hạng mục | Giá trị đo được |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE lúc đo | **`assets/index-DsMHK7Dp.js`** · `last-modified Thu, 06 Aug 2026 18:51:25 GMT` · etag `W/"6a74d7ad-1127fb"` |
| Chuỗi chân sidebar | `HTPLDN · v1.0.9` — ⚠️ **không dùng làm vân tay**, xem [`../BAN-DUNG.md`](../BAN-DUNG.md) |
| Tài khoản | `cbnv_tw_04` / `Test@1234` → `vaiTros ["CB_NV_TW"]`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW` |
| Thời điểm đo | 07/08/2026 ~01:57 – 02:12 giờ VN |
| Khổ màn | 1440 × 741 (≥1280 theo chuẩn chấm §6.1 bẫy 5). Trang **không cuộn ngang**: `scrollWidth = clientWidth = 1440` |

## 2. Tiền đề đã dùng (tái dùng dữ liệu QA sẵn có — không tạo mới)

| | |
|---|---|
| Vụ việc | **`VV-BTP-TW-20260806-003`** (`fbf936fb-b605-4286-946b-f68ba1fd6e89`) |
| Trạng thái | `DA_DANH_GIA` — nhãn trên màn "Đã đánh giá" |
| Đơn vị | `00000000-0000-4000-8000-000000000001` — **trùng đơn vị tài khoản đo**, thoả `srs-fr-05-vu-viec.md:1216` |
| Đã có đánh giá loại `CB_NV` | Có — người đánh giá "CB Nghiệp vụ - Trung ương #01", ngày 06/08/2026 16:34 |

Xác minh trước khi tính là tiền đề: `GET /api/v1/vu-viecs?trangThai=DA_DANH_GIA` (đường dẫn lấy từ chính
lưu lượng của màn danh sách, không đoán) → bản ghi còn tồn tại, còn đúng trạng thái, còn đúng đơn vị.
**Không seed, không sửa dữ liệu nào.**

## 3. Đường đo (1 đường UI) + đối chứng độc lập (1 đường)

**UI:** đăng nhập → sidebar **Vụ việc HTPL** → mở chi tiết `VV-BTP-TW-20260806-003` → nhóm **Đánh giá** đã ở
trạng thái mở sẵn → chụp ảnh + đọc `innerText` (KHÔNG dùng `textContent`).

**Đối chứng:** `GET /api/v1/vu-viecs/{id}` bằng **chính phiên `cbnv_tw_04`** (đường dẫn lấy từ danh sách
đường dẫn mà hệ thống công bố tại `/api/docs-json`, không đoán). Không gọi bằng `admin`.

---

## 4. Số đo

### 4.1 `C1` — Nhóm 8 hiện đủ 5 trường bắt buộc → **ĐẠT**

`innerText` của vùng nhóm Đánh giá (đọc lúc 02:0x):

```
Điểm chất lượng tư vấn	9/10	Điểm đúng thời hạn	8/10	Điểm thái độ phục vụ	10/10
Điểm tổng (trung bình 3 điểm)	9/10	Người đánh giá	CB Nghiệp vụ - Trung ương #01	Ngày đánh giá	06/08/2026 16:34
Nhận xét	QA-DGKQ-20260806-1634
```

| Trường SRS (`:1734`) | Hiện trên màn | Nhãn thực tế | Kích thước ô | Đạt |
|---|---|---|---|---|
| `diem_chat_luong` | ✅ | "Điểm chất lượng tư vấn" = `9/10` | 230×61 / 65×61 | ✅ |
| `diem_thoi_gian` | ✅ | "Điểm đúng thời hạn" = `8/10` | 161×61 / 236×61 | ✅ |
| `diem_thai_do` | ✅ | "Điểm thái độ phục vụ" = `10/10` | 172×61 / 156×61 | ✅ |
| `diem_tong` | ✅ | "Điểm tổng (trung bình 3 điểm)" = `9/10` | 230×61 / **65×61** | ✅ (xem `C5`) |
| `nhan_xet` | ✅ | "Nhận xét" = `QA-DGKQ-20260806-1634` | 230×39 / 790×39 | ✅ |

14/14 ô đo được đều `visible = true` (rộng > 0, cao > 0) — không có trường nào ẩn. Đếm bằng mắt trên ảnh
[`../image/DGKQHTVV_02-nhom8-VV-BTP-TW-20260806-003.png`](../image/DGKQHTVV_02-nhom8-VV-BTP-TW-20260806-003.png) khớp số đo.

**2 trường ngoài bảng `:1734`:** "Người đánh giá", "Ngày đánh giá". Có căn cứ ở mô hình dữ liệu
`DANH_GIA_VU_VIEC` (`srs-fr-05-vu-viec.md:2115`, `:2122`) ⇒ theo **UI-12** (`srs-v3.5.md:584`) là
**bảng đặc tả bị sót, phần mềm ĐÚNG** — không chấm Fail, đưa vào câu hỏi BA (chuẩn chấm §6.1 bẫy 1).

### 4.2 `C3` — giá trị hiển thị đúng bằng bản ghi đã lưu → **ĐẠT**

`GET /api/v1/vu-viecs/fbf936fb-b605-4286-946b-f68ba1fd6e89` (HTTP 200) trả:

```json
{"maVuViec":"VV-BTP-TW-20260806-003","trangThai":"DA_DANH_GIA",
 "donViId":"00000000-0000-4000-8000-000000000001","diemDanhGia":9,
 "danhGia":{"diemChatLuong":9,"diemThoiGian":8,"diemThaiDo":10,"diemTong":9,
            "nhanXet":"QA-DGKQ-20260806-1634","ngayDanhGia":"2026-08-06T09:34:26.438Z",
            "nguoiDanhGia":"CB Nghiệp vụ - Trung ương #01"}}
```

| Trường | Trên màn | Bản ghi máy chủ | Khớp |
|---|---|---|---|
| Điểm chất lượng tư vấn | `9/10` | `diemChatLuong = 9` | ✅ |
| Điểm đúng thời hạn | `8/10` | `diemThoiGian = 8` | ✅ |
| Điểm thái độ phục vụ | `10/10` | `diemThaiDo = 10` | ✅ |
| Điểm tổng | `9/10` | `diemTong = 9` | ✅ |
| Nhận xét | `QA-DGKQ-20260806-1634` | `nhanXet` cùng chuỗi | ✅ |
| Ngày đánh giá | `06/08/2026 16:34` | `2026-08-06T09:34:26.438Z` = 16:34 giờ VN | ✅ |

Mỗi điểm nằm trong 0–10 (`:1205`–`:1207`). Điểm tổng `9` = (9+8+10)/3 = 9 ✅.
⚠️ Bộ điểm 9·8·10 có trung bình **trùng** trung vị ⇒ **không dùng lượt này để kết luận công thức** —
việc đó thuộc dòng 68 (`DGKQHTVV_04`), đo bằng bộ điểm phân biệt.
**Hai đường khớp ⇒ dừng, không mở đường thứ ba.**

### 4.3 `C4` — tiếng Việt, không lộ mã kỹ thuật → **ĐẠT**

Soi `innerText` của vùng nhóm Đánh giá:

| Mẫu soi | Kết quả |
|---|---|
| `\b[a-z]+_[a-z_]+\b` (mã kỹ thuật snake_case) | **0 khớp** |
| `null` / `undefined` / `NaN` / `Invalid Date` | **0 khớp** |
| Chữ Latinh ≥3 ký tự | chỉ `trung` (trong "trung bình"), `Nghi`/`Trung` (trong "Nghiệp vụ - Trung ương"), `DGKQ` (trong chuỗi nhận xét do QA tự nhập) — **không có từ tiếng Anh lọt ra** |

### 4.4 `C2` — nhãn / bố cục "giống với thiết kế" → **GAP, chỉ ghi nhận, KHÔNG chấm**

Nhãn thực tế trên màn: "Điểm chất lượng tư vấn" · "Điểm đúng thời hạn" · "Điểm thái độ phục vụ" ·
"Điểm tổng (trung bình 3 điểm)" · "Người đánh giá" · "Ngày đánh giá" · "Nhận xét".
Bố cục: bảng nhãn–giá trị 3 cặp/hàng, tiêu đề nhóm ghi **"Đánh giá"** (SRS gọi cả "Accordion 8" `:1734`
lẫn "Nhóm 8" `:1809` — không phải tiêu chí chấm).

Không có chuẩn trong nguồn SRS để chấm (chuẩn chấm §2.4): `:1486` nói cột "Dữ liệu / Nội dung" là *chữ chính
xác user nhìn thấy*, nhưng ô `:1734` lại ghi mã kỹ thuật, còn `:1492` + `:1622` cấm mã kỹ thuật lên giao diện;
`ux-spec.md` mà `srs-v3.5.md:567` trỏ tới **không có** trong `_bmad-output/planning-artifacts/`.

### 4.5 `C3b` — số chữ số thập phân / làm tròn điểm tổng → **GAP, chỉ ghi nhận**

Chuỗi hiển thị: **`9/10`** (không phần thập phân). Lượt này 9+8+10 = 27 **chia hết cho 3** ⇒ **chưa lộ được**
quy tắc làm tròn. Dữ kiện làm tròn thật sự sẽ có ở dòng 68 (bộ 4·8·9 = 7, cũng chia hết) — nếu BA cần, phải
đo riêng bằng bộ điểm KHÔNG chia hết cho 3.

### 4.6 `C5` — "không bị tràn / đè lên nhau" → **GAP, nhưng hiện trạng CÓ khiếm khuyết**

| Phép đo | Kết quả |
|---|---|
| Chồng lấn giữa các ô cùng hàng | **0** cặp chồng lấn |
| Ô bị cắt nội dung (`scrollWidth > clientWidth`) | **0/14 ô** |
| Trang cuộn ngang | Không (`scrollWidth = clientWidth = 1440`) |
| **Số dòng thực tế của từng ô giá trị điểm** | `9/10` (chất lượng): **1 dòng** · `8/10`: **1 dòng** · `10/10`: **1 dòng** · **`9/10` (điểm tổng): 2 DÒNG** |

🔴 **Hiện tượng đo được:** ô giá trị của **"Điểm tổng"** rộng 65px, trừ đệm trái/phải 16px mỗi bên còn
**vùng chữ 32px**; giá trị được bọc trong thẻ in đậm (`<strong>`, `font-weight 700`) nên rộng **~34px** >
32px ⇒ chuỗi `9/10` **bị bẻ làm 2 dòng: `9/1` ở dòng trên, `0` ở dòng dưới** (đo bằng `Range.getClientRects()`:
2 mốc dòng `top = 921` và `943`). Trên bản ghi này, ô "Điểm chất lượng tư vấn" cùng bề rộng nhưng chữ thường
(`font-weight 400`, rộng 31px < 32px) vẫn nằm 1 dòng.

🔴 **ĐÍNH CHÍNH nguyên nhân — có bằng chứng mạnh hơn từ lượt đo dòng 68 (`VV-QAW7-DG01`, cùng màn, cùng bó mã):**
chẩn đoán "chỉ do chữ in đậm" là **chưa đủ**. Đo lại bảng nhóm Đánh giá trên `VV-QAW7-DG01`:

| Ô | Bề rộng ô | Vùng chữ | Bề rộng chuỗi | Đậm | Số dòng |
|---|---|---|---|---|---|
| Điểm chất lượng tư vấn = `4/10` | 64px | **31px** | 31px khi 1 dòng | Không | **2** |
| Điểm đúng thời hạn = `8/10` | 238px | 205px | 31px | Không | 1 |
| Điểm thái độ phục vụ = `9/10` | 152px | 119px | 31px | Không | 1 |
| Điểm tổng = `7/10` | 64px | **31px** | — | **Có** | **2** |

⇒ **Gốc vấn đề là bố cục cột lệch:** cột giá trị **thứ nhất** chỉ 64–65px (vùng chữ 31–32px) trong khi cột
giá trị thứ hai 238px và thứ ba 152px. Chuỗi `x/10` cần đúng ~31px — **sát ngưỡng**, nên chỉ cần in đậm
hoặc hụt 1px là vỡ dòng, kể cả chữ thường. Hướng sửa nằm ở cách chia bề rộng cột, không phải ở kiểu chữ.
Ô "Kết quả verify" của dòng 65 đã được **ghi lại** với chẩn đoán này (lần ghi thứ hai, cùng verdict).

Ảnh: [`../image/DGKQHTVV_02-diemtong-vo-chu-9-1-0.png`](../image/DGKQHTVV_02-diemtong-vo-chu-9-1-0.png) (ảnh đã mở lại xem, khớp mô tả).

**Vì sao vẫn là `GAP` chứ không phải Reopen:** đã đọc lại `srs-fr-05-vu-viec.md:1568`–`:1573` §C
"Quy ước cắt nội dung dài" — chỉ áp cho **cột text trong bảng danh sách** (cắt + `...` + tooltip cho tên/tiêu đề
>30 ký tự, mô tả >50 ký tự), không đặt tiêu chí bẻ dòng cho vùng nhóm chi tiết. `:1601`–`:1604` §F chỉ nói khổ
màn hỗ trợ và mâu thuẫn với `srs-v3.5.md:579`. ⇒ SRS **im lặng** về vế này.
**Ngoại lệ đã khóa ở chuẩn chấm không kích hoạt:** giá trị vẫn **đọc ra được** là `9/10` (không mất chữ số),
nên không rơi về `C1`.

🔴 **Hệ quả bắt buộc cho phần kết luận:** **KHÔNG** được ghi "web đúng y nguyên kỳ vọng đối tác" — vế
*"không bị tràn/đè lên nhau"* của phiếu đang **không** được đáp ứng trọn vẹn ở ô Điểm tổng.

---

## 5. Đối chiếu điều kiện với case đối tác

| Điều kiện có thể đổi kết quả | Đối tác | Lượt đo này | Ảnh hưởng |
|---|---|---|---|
| Vai trò | Không ghi rõ; bước 1 là menu CMS ⇒ cán bộ | `CB_NV_TW` | Khớp |
| Trạng thái vụ việc | "Hoàn thành" **hoặc** "Đã đánh giá" | "Đã đánh giá" | Khớp (phiếu ghi *hoặc*) |
| Dữ liệu nhóm 8 | Phải có để chấm "đúng định dạng" | Có đủ 5 giá trị | Khớp |
| Env / bản dựng | `htpldn-uat.ospgroup.vn` | nội bộ, `index-DsMHK7Dp.js` | **Khác** ⇒ verdict chỉ có hiệu lực cho env + bó mã đã đo |

## 6. Cổng chốt verdict

| Câu hỏi | Trả lời |
|---|---|
| Mỗi vế neo vào dòng nào của SRS prompt cấp? | `C1` `:1734`+`:1204`–`:1209`+`:2117`–`:2121` · `C3` `:1205`–`:1208`+`:2117`–`:2120` · `C4` `:1492`+`:1622`+`srs-v3.5.md:578` · `C2` `:1486`↔`:1734`↔`:1492`+`srs-v3.5.md:567` · `C3b` `:2462` · `C5` `:1568`–`:1573`+`:1601`–`:1604`↔`srs-v3.5.md:579` |
| Mọi thao tác có trả lời một vế Cn không? | Có — 1 đường UI + 1 đối chứng máy chủ; không mở thêm màn/role/bộ lọc |
| Vế `GAP` đã bị chặn Pass và có câu hỏi BA chưa? | Có — 3 câu hỏi ở §7 |
| Đã đọc đủ nội dung dòng 65 chưa? | Có — đọc trọn dòng qua bảng dump [`../audit/00-header-va-4-dong.md`](../audit/00-header-va-4-dong.md) |
| Điều kiện đo có khớp tiền đề case không? | Có, trừ env/bản dựng (đã khai giới hạn) |

## 7. Verdict logic — **CẦN BA**

Không vế `MATCH` nào hỏng ⇒ không Reopen. Còn 3 vế `GAP` ⇒ theo Flow 04 §Ca biên
(*"Không vế nào Reopen mà còn `DIFF/GAP` → **Cần BA**"*) ⇒ **Cần BA**, **cấm Pass**.

| Vế | Quan hệ | Kết quả đo |
|---|---|---|
| `C1` đủ 5 trường | MATCH | ✅ Đạt |
| `C3` giá trị khớp bản ghi | MATCH | ✅ Đạt |
| `C4` tiếng Việt, không lộ mã kỹ thuật | MATCH | ✅ Đạt |
| `C2` nhãn / bố cục "giống thiết kế" | GAP | Ghi nhận hiện trạng, không chấm |
| `C3b` làm tròn điểm tổng | GAP | Ghi nhận `9/10`; lượt này chia hết cho 3 nên chưa lộ |
| `C5` không tràn/đè | GAP | **Có khiếm khuyết**: ô Điểm tổng bẻ `9/1` ⏎ `0` |

**Câu hỏi BA (mục đích: bổ sung đặc tả — KHÔNG chặn bàn giao, trừ câu 3 có thể thành lỗi thật):**

1. Bộ nhãn tiếng Việt + bố cục của nhóm Đánh giá là gì? Bảng thành phần màn hình `:1734` ghi mã kỹ thuật,
   trong khi quy ước của chính mục đó (`:1486`) nói cột ấy là *chữ chính xác người dùng nhìn thấy*, còn
   `:1492`/`:1622` cấm mã kỹ thuật lên giao diện; tài liệu thiết kế mà `srs-v3.5.md:567` trỏ tới không có
   trong bộ SRS. *(Web hiện tại: 7 nhãn liệt kê ở §4.4.)*
2. Có bổ sung "Người đánh giá" và "Ngày đánh giá" vào bảng thành phần màn hình của nhóm Đánh giá không?
   Hai trường này có căn cứ ở `:2115`/`:2122` ⇒ theo UI-12 (`srs-v3.5.md:584`) là bảng bị sót.
   *(Web hiện tại: đã hiển thị cả hai.)*
3. 🔴 SRS có đặt tiêu chí hiển thị "không tràn / không bẻ vỡ giá trị" cho vùng nhóm chi tiết không?
   Hiện `:1570` chỉ áp cho cột text trong bảng danh sách. *(Web hiện tại: ô "Điểm tổng" bẻ `9/10` thành
   `9/1` và `0` — xem ảnh. Nếu BA xác nhận có tiêu chí thì đây là **lỗi cần dev sửa**, không phải chuyện đặc tả.)*
4. Điểm tổng hiển thị mấy chữ số thập phân, làm tròn theo quy tắc nào? `:2462` chỉ áp thang tư vấn viên 1–5
   và **loại trừ UC67** bằng chữ. *(Web hiện tại: `9/10`, lượt đo chia hết cho 3 nên chưa lộ quy tắc.)*

## 8. Bug mới / candidate

Không có bug mới tự lộ trong bước bắt buộc. Hiện tượng bẻ chữ ở ô Điểm tổng **không** log thành bug riêng
vì SRS im lặng (Flow 04 §Bug mới: *"SRS im lặng/mâu thuẫn → không log như bug đã xác nhận; ghi candidate/câu
hỏi BA"*) — đã đưa vào câu hỏi BA số 3.
