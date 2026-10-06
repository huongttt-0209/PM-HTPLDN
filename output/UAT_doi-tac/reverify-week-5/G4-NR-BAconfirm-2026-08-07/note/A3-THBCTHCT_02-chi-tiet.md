# A3 — dòng 344 — `THBCTHCT_02` — "Kiểm tra khi bấm nút Tổng hợp"

> **VERDICT: `Test done`** — chi tiết ở §10. Đo 07/08/2026 21:25→21:46 (giờ VN), bản dựng `index-BbPPdate.js`,
> tài khoản `cbnv_tw_05` (đoạn sau đổi `cbnv_tw_04` — xem §12.1). Điểm treo của lượt trước **đã hết treo bằng
> phép đo**: dựng tiền đề trên đợt dùng **cả hai** biểu mẫu, hộp tổng hợp ghi rõ "Biểu mẫu 21a + 21b/TP/HTPLDN",
> gợi ý số liệu đúng tổng **13/13** chỉ tiêu, và sửa/bổ sung được.

## 1. Bối cảnh phiếu (đọc từ `do/00-sheet-7-dong-goc.txt`, khối DÒNG 344)

| Cột | Nội dung |
|---|---|
| `[D]` Mã TC | `THBCTHCT_02` |
| `[G]` Mô tả | Kiểm tra khi bấm nút "Tổng hợp" |
| `[H]` Điều kiện | NSD là CB nghiệp vụ cấp TW + có ≥1 báo cáo từ Bộ/Ngành hoặc Địa phương **đã gửi lên** |
| `[J]` Các bước | 1. Chọn menu "Đợt báo cáo" · 2. Chọn các báo cáo cần tổng hợp trong bảng danh sách (ô chọn) và bấm nút "Tổng hợp" |
| `[K]` KQ mong đợi | (K1) **Gợi ý số liệu tổng hợp**: tính tổng các chỉ tiêu tương ứng theo **Biểu 21a và Biểu 21b** từ các báo cáo đã chọn · (K2) **Hiển thị biểu mẫu tổng hợp Biểu 21a, 21b toàn quốc** cho phép CB NV cấp TW **chỉnh sửa, bổ sung** |
| `[L]` KQ thực tế | **TRỐNG** |
| `[Q]` TKM phản hồi 1 | **TRỐNG** ⇒ bên nghiệm thu chưa chạy lượt nào, không có bằng chứng đối tác để so |
| `[R]` Trạng thái dev fix | `BA confirm` |
| `[S]` DEV phản hồi 1 | Dev tự fix theo SRS, BA không phải quyết. **Đã bổ sung: hệ thống gợi ý số liệu biểu 21a/21b trước khi lưu** và xuất Excel/Word theo mẫu TT 17/2025/TT-BTP |

**Phạm vi đo lượt này (user chốt):** chỉ (1) 2 bước ở `[J]` chấm theo `[K]`, và (2) vế Dev khai ở `[S]`
về **gợi ý số liệu 21a/21b**. Vế "xuất Excel/Word" thuộc phiếu `THBCTHCT_05` (dòng 345) — **không đo ở đây**.

**Điểm treo của lượt trước (ô `[T]`, chạy 13:18–13:29 trên bản dựng CŨ `index-eWHwDgt2.js`):**
gợi ý số liệu ĐÚNG TỔNG 13/13 chỉ tiêu và biểu mẫu SỬA ĐƯỢC — nhưng biểu chỉ hiện **21a**, vì đợt
`DOT-THBC01-UAT` và cả hai báo cáo nguồn đều dùng biểu 21a. Lượt đó không trả lời được câu hỏi
"có hiện đủ cả 21a **và** 21b không" nên chốt `BA confirm`.

**Cách lượt này định trả lời điểm treo đó:** dựng tiền đề trên đợt dùng biểu mẫu **CẢ HAI** (`CA_HAI`),
để chính dữ liệu quyết định thay vì hỏi BA — nếu báo cáo nguồn có đủ số liệu cả hai biểu mà màn tổng hợp
vẫn chỉ hiện một biểu thì đó là lỗi đo được, không còn là điểm đặc tả im lặng.

## 2. Môi trường · bản dựng · tài khoản

| Mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| **Bản dựng TRƯỚC lượt đo** (đo 21:25:38 giờ VN 07/08/2026) | `index-BbPPdate.js` — `last-modified Fri, 07 Aug 2026 06:47:57 GMT` = **13:47:57 giờ VN** |
| **Bản dựng SAU lượt đo** (đo 21:46:36) | `index-BbPPdate.js` — `06:47:57 GMT` = 13:47:57 giờ VN — **TRÙNG hai đầu** (§9) |
| Tài khoản ra verdict | `cbnv_tw_05` → **đổi `cbnv_tw_04`** từ 21:42 (phiên `_05` bị tiến trình khác chiếm — §12.1). Cả hai đều CB Nghiệp vụ Trung ương (`CB_NV_TW`), Cục Bổ trợ tư pháp |
| Nhãn phiên bản trên giao diện | `HTPLDN · V1.0.10` |
| Mốc giờ đo | **21:25 → 21:46** ngày 07/08/2026 (giờ VN) |
| Tài khoản chỉ dựng tiền đề, KHÔNG ra verdict | `cbnv_hn` + `cbpd_hn` (Sở TP Hà Nội) · `cbnv_dp_05` + `cbpd_dp_05` (Sở TP An Giang) — mỗi tài khoản một phiên cách ly riêng |

## 3. Tiền đề — tự dựng, chọn đợt dùng **CẢ HAI** biểu mẫu để trả lời điểm treo

**Vì sao không dùng lại tiền đề của lượt 13:18:** đợt `DOT-THBC01-UAT` mà lượt đó dùng đã bị lượt A2
(21:04) tổng hợp hết; quan trọng hơn, đợt đó áp dụng **MAU_21A** nên dù còn nguyên cũng **không trả lời
được** câu hỏi treo "có hiện đủ 21a **và** 21b không". Kiểm sống lúc 21:26 bằng phiên `cbnv_tw_05`:
3/4 đợt (`DOT-THBC01-UAT`, `DOT-SO_BO_NAM-2026-1`, `DOT-SO_BO_6_THANG-2026-1`) đều **`DA_TONG_HOP`** và
đều **`MAU_21A`**. Đợt duy nhất còn ở `TAO_DOT` là `DOT-TRON_NAM-2026-1` — và đợt này có
`bieuMauSuDung = CA_HAI`, đúng thứ cần.

| Thuộc tính đợt dùng cho lượt này | Giá trị |
|---|---|
| Mã / id | `DOT-TRON_NAM-2026-1` · `a63a3214-d1d3-421b-8c0c-cec5db419413` |
| Kỳ | `TRON_NAM` |
| **Biểu mẫu áp dụng** | **`CA_HAI`** (cả 21a và 21b) |
| Phạm vi nộp | đúng **2** đơn vị: Sở Tư pháp Hà Nội (`…8002-000000000001`) · Sở Tư pháp An Giang (`…8002-000000000006`) |
| Trạng thái đợt trước khi đo | `TAO_DOT` `version 1` |

**Đã dựng (đúng luật 5 của brief — thiếu thì tạo):** hai đơn vị lập → trình duyệt nội bộ → được duyệt →
gửi TW. Mỗi tài khoản chạy trong **một phiên cách ly riêng**, không đụng phiên `cbnv_tw_05`:

| Bước | Tài khoản (chỉ dựng tiền đề, KHÔNG ra verdict) | Kết quả |
|---|---|---|
| Nhập số liệu + trình duyệt BC Sở TP **Hà Nội** | `cbnv_hn` (CB NV ĐP, Sở TP Hà Nội) | 200 · `NHAP → CHO_PHE_DUYET` |
| Duyệt nội bộ BC Hà Nội | `cbpd_hn` (CB PD ĐP, Sở TP Hà Nội) | 200 · `DA_DUYET` |
| Gửi TW BC Hà Nội | `cbnv_hn` | 200 lúc **21:31:43** |
| Lập + nhập số liệu + trình duyệt BC Sở TP **An Giang** | `cbnv_dp_05` (CB NV ĐP, Sở TP An Giang) | 200 · `DU_THAO → CHO_PHE_DUYET` |
| Duyệt nội bộ BC An Giang | `cbpd_dp_05` (CB PD ĐP, Sở TP An Giang) | 200 · `DA_DUYET` |
| Gửi TW BC An Giang | `cbnv_dp_05` | 200 lúc **21:34:41** |

### 3.1 Số liệu gốc — đọc lại bằng **phiên của chính đơn vị sở hữu** (không đọc từ phiên TW)

Đọc lúc 21:35, mỗi con số lấy từ phiên đăng nhập của chính đơn vị đó:

| # | Chỉ tiêu | Sở TP **Hà Nội** (`1b3085b8…`) | Sở TP **An Giang** (`b63fe4e2…`) |
|---|---|---:|---:|
| 1 | Số TVV kiện toàn | 11 | 5 |
| 2 | Số cuộc tập huấn | 6 | 2 |
| 3 | Số hội nghị đối thoại | 4 | 1 |
| 4 | VB trả lời UBND | 9 | 3 |
| 5 | VB TV mạng lưới TVV | 7 | 6 |
| 6 | HS tiếp nhận | 31 | 14 |
| 7 | HS giải quyết tổng | 23 | 10 |
| 8 | DN vừa | 8 | 4 |
| 9 | DN nhỏ | 12 | 5 |
| 10 | DN siêu nhỏ | 3 | 1 |
| 11 | KP hỗ trợ TVPL (NSNN) | 610.000.000 | 235.000.000 |
| 12 | KP chi HĐ khác (NSNN) | 145.000.000 | 60.000.000 |
| 13 | KP xã hội hóa | 22.000.000 | 18.000.000 |

Bộ số chọn có chủ đích: **13/13 chỉ tiêu của hai đơn vị đều khác nhau và đều khác 0**, và tổng của từng
cặp cũng khác cả hai số hạng — nên nếu hệ thống chỉ chép lại số của một đơn vị (hoặc hiện số cố định)
thì phép đối chiếu sẽ lộ ra ngay.

**Trạng thái ngay trước khi bấm (đọc bằng chính phiên `cbnv_tw_05`, 21:35):** cả hai bản ghi đều
`DA_GUI_TW`, `bieuMauSuDung = CA_HAI`; bảng tiến độ nộp: Hà Nội `DA_NOP`, An Giang `DA_NOP`; đợt vẫn
`TAO_DOT` `version 1`. Đợt chỉ có **đúng 2 đơn vị trong phạm vi** và **cả hai đều được chọn** ⇒ lỗi mà
phiếu A2 đã ghi nhận (đơn vị không chọn bị kéo theo) **không có đất phát sinh** ở lượt này, và lượt này
**không bấm [Lưu tổng hợp]** nên cũng không chạm tới nó.

## 4. Các bước của phiếu — đường đi thực tế

| Bước phiếu | Đã làm gì | Ghi nhận |
|---|---|---|
| **B1** "Chọn menu Đợt báo cáo" | Tải lại toàn bộ trang bằng địa chỉ lúc 21:36 (đọc `script[src]` tại trang xác nhận đang chạy `index-BbPPdate.js`), rồi **bấm mục "Đợt báo cáo"** trên thanh menu trái → bảng 4 đợt hiện đúng; đợt `DOT-TRON_NAM-2026-1` "Tròn năm · 2 đơn vị · Tạo đợt" | ✅ menu tồn tại, mở được — ảnh 01 |
| — | Vào màn có ô chọn + nút [Tổng hợp] = **"Tổng hợp báo cáo toàn quốc"** (`/ct-htpldn/tong-hop`). Màn này **không có mục trên menu trái và không có nút dẫn** từ màn Đợt báo cáo ⇒ phải gõ thẳng địa chỉ. Điểm này lượt 13:18 và phiếu A2 đều đã nêu — **nhắc lại, KHÔNG log trùng**; nó không chặn phép đo | — |
| **B2** "Chọn các báo cáo cần tổng hợp (ô chọn) + bấm nút Tổng hợp" | Cài bộ bắt thông báo `tools/toast-capture.js` **trước** khi bấm, tự kiểm `soObserverDangSong = 1` (hợp lệ). Tick **đúng 2 dòng** `DOT-TRON_NAM-2026-1` (An Giang + Hà Nội, đều "Đã gửi TW") → nút đổi thành **[Tổng hợp (2)]** → bấm lúc **21:38** | ảnh 02, 03, 04 |

**Bộ đếm sau khi bấm [Tổng hợp (2)]:** `SO_REQUEST = 1` → `POST /api/v1/dot-bao-caos/tong-hop/goi-y`; `SO_KHUNG_THONG_BAO = 0`.
⇒ 1 lượt bấm = 1 yêu cầu, và bước này **chỉ gợi ý số liệu (chỉ đọc)** — đúng bản chất "trước khi lưu".

> **Phiếu A3 dừng ở đây.** Bước [Lưu tổng hợp] thuộc phiếu A2 (`THBCTHCT_01`) nên **không bấm**; đã bấm
> **[Hủy]**. Kiểm chứng ngay sau đó (§7): 0 yêu cầu ghi dữ liệu, đợt và 2 báo cáo giữ nguyên trạng thái cũ.

## 5. Chấm ý (K1) — "Gợi ý số liệu tổng hợp: tính tổng các chỉ tiêu tương ứng theo Biểu 21a và Biểu 21b từ các báo cáo đã chọn" → ✅ ĐẠT

Hộp hiện ra ghi rõ **"Số liệu dưới đây do hệ thống gợi ý — Hệ thống đã cộng các chỉ tiêu tương ứng từ báo
cáo của những đơn vị được chọn. Cán bộ có thể chỉnh sửa, bổ sung trước khi lưu."**, kèm **Số đơn vị: 2**.

### 5.1 Bảng đối chiếu — tự cộng tay từng chỉ tiêu

| # | Chỉ tiêu | Hà Nội (a) | An Giang (b) | **Cộng tay a+b** | **Hệ thống gợi ý** | Khớp |
|---|---|---:|---:|---:|---:|:--:|
| 1 | Số TVV kiện toàn | 11 | 5 | **16** | 16 | ✅ |
| 2 | Cuộc tập huấn | 6 | 2 | **8** | 8 | ✅ |
| 3 | Hội nghị đối thoại | 4 | 1 | **5** | 5 | ✅ |
| 4 | VB trả lời UBND | 9 | 3 | **12** | 12 | ✅ |
| 5 | VB TV mạng lưới TVV | 7 | 6 | **13** | 13 | ✅ |
| 6 | HS tiếp nhận | 31 | 14 | **45** | 45 | ✅ |
| 7 | HS giải quyết tổng | 23 | 10 | **33** | 33 | ✅ |
| 8 | DN vừa | 8 | 4 | **12** | 12 | ✅ |
| 9 | DN nhỏ | 12 | 5 | **17** | 17 | ✅ |
| 10 | DN siêu nhỏ | 3 | 1 | **4** | 4 | ✅ |
| 11 | KP hỗ trợ TVPL (NSNN) | 610.000.000 | 235.000.000 | **845.000.000** | 845000000 | ✅ |
| 12 | KP chi HĐ khác | 145.000.000 | 60.000.000 | **205.000.000** | 205000000 | ✅ |
| 13 | KP xã hội hóa | 22.000.000 | 18.000.000 | **40.000.000** | 40000000 | ✅ |

**13/13 khớp khít.** Giá trị đọc từ chính ô nhập trên hộp (đọc `input.value`, không đọc từ chữ trang trí).

### 5.2 Phép thử quyết định — đổi bộ chọn, số phải đổi theo

Bấm [Hủy], **bỏ chọn An Giang, chỉ để lại Hà Nội**, bấm lại [Tổng hợp (1)] lúc **21:44**:
hộp đổi thành **Số đơn vị: 1** và **cả 13 giá trị đổi đúng thành số riêng của Hà Nội**
(11 · 6 · 4 · 9 · 7 · 31 · 23 · 8 · 12 · 3 · 610.000.000 · 145.000.000 · 22.000.000) — ảnh 06.

⇒ Hệ thống **cộng thật theo bộ chọn**, không hiện số cố định, không giữ số của lượt trước.

Đặc tả: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1002`
= `| 4 | Hệ thống gợi ý số liệu: tính tổng các cột tương ứng 21a/21b | — |`
và tiêu chí chấp nhận `:1037` = `- **Given** CB NV TW chọn các BC **When** nhấn "Tổng hợp" **Then** gợi ý số liệu + form tổng hợp theo TT17`
(đã mở file đọc, không quote từ trí nhớ).

⇒ **Điểm Dev khai ở ô `[S]` — "hệ thống gợi ý số liệu biểu 21a/21b trước khi lưu" — ĐÚNG.**

## 6. Chấm ý (K2) — "Hiển thị biểu mẫu tổng hợp Biểu 21a, 21b toàn quốc cho phép CB NV TW chỉnh sửa, bổ sung" → ✅ ĐẠT

### 6.1 Có hiện đủ **cả hai** biểu không → CÓ

Dòng "Biểu mẫu" trên đầu hộp ghi nguyên văn: **`Biểu mẫu 21a + 21b/TP/HTPLDN`** (ảnh 03) — đọc bằng
`innerText` của chính hộp, không suy từ ảnh. Đây chính là điểm mà lượt 13:18 **không** kết luận được:
lượt đó đợt và cả hai báo cáo nguồn đều dùng **MAU_21A** nên hộp chỉ ghi "Biểu mẫu 21a/TP/HTPLDN", và
lượt đó phải treo câu hỏi cho nghiệp vụ. Lượt này dựng tiền đề trên đợt **CA_HAI** ⇒ **dữ liệu tự trả lời**.

### 6.2 Kiểm lại bằng đường thứ hai — nguồn số liệu trả về, không qua giao diện

Gọi thẳng nguồn gợi ý của chính chức năng này lúc **21:45:41** trên cùng bản dựng, hai bộ chọn khác nhau:

| Bộ báo cáo chọn | Trường biểu mẫu nguồn trả về | 13 chỉ tiêu |
|---|---|---|
| 2 BC của `DOT-TRON_NAM-2026-1` (Hà Nội + An Giang) | **`CA_HAI`** | 16 · 8 · 5 · 12 · 13 · 45 · 33 · 12 · 17 · 4 · 845.000.000 · 205.000.000 · 40.000.000 — **trùng khít** bảng §5.1 |
| 2 BC của `DOT-SO_BO_NAM-2026-1` (đợt cũ, biểu 21a) | **`MAU_21A`** | (số của đợt đó) |

⇒ (a) Số trên giao diện và số ở nguồn **khớp nhau**, không phải hiển thị suông. (b) Nhãn biểu mẫu trên hộp
**bám theo biểu mà các báo cáo được chọn thực sự dùng**: chọn báo cáo dùng cả hai biểu → hộp ghi "21a + 21b";
chọn báo cáo chỉ dùng 21a → nguồn trả `MAU_21A` (và lượt 13:18 đã thấy hộp ghi "Biểu mẫu 21a/TP/HTPLDN").
**Đây là câu trả lời đo được cho đúng câu hỏi mà lượt trước phải treo.**

### 6.3 Có sửa / bổ sung được không → ĐƯỢC

- Gõ **bằng bàn phím** vào ô chỉ tiêu 13 "KP xã hội hóa" giá trị mốc giờ **21550807**: ô nhận giá trị,
  **12 ô còn lại giữ nguyên** (đọc lại toàn bộ 13 ô sau khi gõ để chắc chắn) — ảnh 05.
- Ô "Nhận xét, kiến nghị" gõ được chữ và đọc lại **đúng nguyên văn** ⇒ đáp ứng cả vế "bổ sung".
- Kiểm bằng đường thứ hai: đọc thuộc tính của cả 13 ô → **không ô nào** `disabled`, **không ô nào** `readOnly`.

Đặc tả: `srs-fr-15-ct-htpldn.md:1003` = `| 5 | CB NV TW chỉnh sửa/bổ sung trên form tổng hợp | — |`.

### 6.4 Một điểm về **cách trình bày** — khai đủ, nhưng không chấm thành lỗi

Hộp tổng hợp của cấp TW hiển thị **một bảng duy nhất 13 chỉ tiêu** mang nhãn chung
"Biểu mẫu 21a + 21b/TP/HTPLDN", **không tách thành hai bảng riêng** 21a và 21b (đã cuộn hết hộp để kiểm:
sau dòng chỉ tiêu 13 là ô "Nhận xét, kiến nghị" rồi tới hai nút — ảnh 04). **Không chấm là "thiếu biểu"** vì:

1. Đặc tả màn hình cho **màn tổng hợp của TW** (`:1175`) mô tả đúng **một** biểu:
   `... -> [Tong hop] -> tu tinh tong hop mau 21a/21b -> form editable -> [Luu] ...`, và bước xử lý `:1002`
   cũng viết gộp "21a/21b" — không có dòng nào đòi hai bảng tách rời ở màn này.
2. Tập chỉ tiêu của 21b trong đặc tả màn hình (`:1168` — `| 38 | form | Bieu mau 21b (TT17/2025) | ... | Tuong tu 21a | ...`)
   là **"tương tự 21a"** ⇒ không có chỉ tiêu nào của 21b bị bỏ sót trong bảng đang hiển thị.
3. Việc Phụ lục D của tài liệu tổng (`srs-v3.5.md:6601` §D.1.3 và `:6692` §D.2.2) mô tả 21b là **bảng tổng hợp
   cấp tỉnh, mỗi dòng một Sở/ban ngành + cột Ghi chú** — khác cấu trúc bảng đang hiển thị — là **mâu thuẫn nội bộ
   giữa hai tầng của chính tài liệu** (đặc tả màn hình vs mẫu văn bản xuất). Điểm này **đã được nêu cho BA ở phiếu
   `LBCKQTHCT_04`** (đợt `DOT-TRON_NAM-2026-1` chính là dữ liệu QA dựng cho phiếu đó) và được xếp là **đề nghị bổ
   sung đặc tả, không chặn bàn giao**. **Không mở trùng ở phiếu này.**

## 7. Dữ liệu — lượt đo của phiếu A3 **không ghi gì xuống môi trường**

| Kiểm chứng | Kết quả |
|---|---|
| Bộ đếm yêu cầu ghi (khác GET) trong suốt lượt đo | **1** — đúng `POST .../tong-hop/goi-y` (bước gợi ý, chỉ đọc). Bấm [Hủy] → **0** yêu cầu |
| Trạng thái đợt `DOT-TRON_NAM-2026-1` sau lượt đo (đọc 21:46) | **`TAO_DOT` `version 1`** — y như trước khi bấm |
| Hai báo cáo trong đợt (đọc 21:46) | **vẫn `DA_GUI_TW`** (An Giang `14:34:41Z`, Hà Nội `14:31:43Z`) — chưa bị tổng hợp |
| Giá trị gõ thử (21550807) và câu nhận xét | chỉ nằm trên màn, đã [Hủy] ⇒ không lưu |

**Dữ liệu do lượt này TẠO RA — là tiền đề, khai đủ:** hai báo cáo của đợt `DOT-TRON_NAM-2026-1` được đưa từ
`NHAP`/`CHUA_NOP` lên `DA_GUI_TW` (Hà Nội `1b3085b8…`, An Giang `b63fe4e2…` — bản ghi An Giang là **mới tạo**).
Đợt vẫn `TAO_DOT` nên **vẫn dùng được cho phiếu sau** (`THBCTHCT_05` — xuất Excel/Word) mà không phải dựng lại.
Không đụng dữ liệu của bên nghiệm thu, không ghi thẳng cơ sở dữ liệu, không ép trạng thái bằng đường dữ liệu.

## 8. Quote đặc tả — đã mở file đọc, xác minh từng số dòng

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

| File : dòng | Nguyên văn |
|---|---|
| `srs-fr-15-ct-htpldn.md:1002` | `\| 4 \| Hệ thống gợi ý số liệu: tính tổng các cột tương ứng 21a/21b \| — \|` |
| `srs-fr-15-ct-htpldn.md:1003` | `\| 5 \| CB NV TW chỉnh sửa/bổ sung trên form tổng hợp \| — \|` |
| `srs-fr-15-ct-htpldn.md:1037` | `- **Given** CB NV TW chọn các BC **When** nhấn "Tổng hợp" **Then** gợi ý số liệu + form tổng hợp theo TT17` |
| `srs-fr-15-ct-htpldn.md:1167` | `\| 37 \| form \| Bieu mau 21a (TT17/2025) \| form (editable table, C23) \| Chi tieu / So lieu ky truoc / Ky nay / Ghi chu... \|` |
| `srs-fr-15-ct-htpldn.md:1168` | `\| 38 \| form \| Bieu mau 21b (TT17/2025) \| form (editable table, C23) \| Tuong tu 21a \| input \| khi bieu mau ap dung va dot o DANG_LAP_BC \|` |
| `srs-fr-15-ct-htpldn.md:1175` | `\| 45 \| content \| [TW] Tong hop (gop tu MH-15.8) \| form (editable) \| Chon BC (checkbox) -> [Tong hop] -> tu tinh tong hop mau 21a/21b -> form editable -> [Luu] -> tao ban ghi bao cao tong hop TW... \|` |
| `srs-fr-15-ct-htpldn.md:710` | `... Đơn vị nộp tự chọn 'bieu_mau_su_dung' (MAU_21A / MAU_21B / CA_HAI)...` |
| `srs-v3.5.md:6601` | `### D.1.3 Mẫu 21b/TP/HTPLDN — BC STP (tổng hợp từ Sở/ban ngành)` (chỉ dùng để nêu mâu thuẫn nội bộ ở §6.4, không dùng làm căn cứ chấm) |

## 9. Bản dựng SAU lượt đo

`curl` lúc **21:46:36** ngày 07/08/2026 → `index-BbPPdate.js`, `last-modified Fri, 07 Aug 2026 06:47:57 GMT`
= **13:47:57 giờ VN** — **TRÙNG** nhãn đo trước lượt (21:25:38). Toàn bộ lượt đo nằm trọn trên **một** bản
dựng, và đúng là bản mới (lượt cũ ở ô `[T]` chạy trên `index-eWHwDgt2.js` — bản 09:11). Tab đo đã được **tải
lại toàn bộ trang** trước khi verify; `script[src]` đọc tại trang lúc 21:36 và 21:43 đều là `index-BbPPdate.js`.

## 10. Tổng kết từng ý → verdict

| Ý | Nguồn | Kết quả đo |
|---|---|---|
| **K1** Gợi ý số liệu = **tổng** các chỉ tiêu tương ứng 21a/21b của các BC đã chọn | phiếu `[K]` + `:1002`, `:1037` | ✅ **ĐẠT** — 13/13 khớp phép cộng tay; đổi bộ chọn thì số đổi theo đúng |
| **K2a** Hiển thị biểu mẫu tổng hợp **Biểu 21a, 21b** toàn quốc | phiếu `[K]` + `:1175`, `:1168` | ✅ **ĐẠT** — hộp ghi rõ "Biểu mẫu 21a + 21b/TP/HTPLDN" khi các BC chọn dùng cả hai biểu |
| **K2b** Cho phép CB NV TW **chỉnh sửa, bổ sung** | phiếu `[K]` + `:1003` | ✅ **ĐẠT** — gõ tay đổi được ô chỉ tiêu, ô khác giữ nguyên; nhập được nhận xét; 13/13 ô không khóa |
| **S** Dev khai "bổ sung gợi ý số liệu biểu 21a/21b **trước khi lưu**" | ô `[S]` | ✅ **ĐÚNG như Dev khai** — bước bấm [Tổng hợp] chỉ gọi nguồn gợi ý (chỉ đọc), số liệu hiện ra trước [Lưu tổng hợp] |
| *(ngoài phạm vi — không đo)* Xuất Excel/Word theo TT 17/2025 | ô `[S]` | ⏭ thuộc phiếu `THBCTHCT_05` (dòng 345) |

### VERDICT: `Test done`

Theo bảng chốt verdict của brief: mọi ý chấm được đều **ĐẠT**, và **điểm treo của lượt trước đã hết treo
bằng phép đo chứ không phải bằng suy luận** — lượt 13:18 phải hỏi BA *"biểu mẫu tổng hợp có hiện đủ cả 21a
và 21b không"* chỉ vì dữ liệu lúc đó không có đợt nào dùng cả hai biểu; lượt này dựng đúng tiền đề đó và hộp
tổng hợp **ghi rõ cả hai biểu**, số liệu đúng tổng, sửa được. Vì vậy **không giữ `BA confirm`**.

Phần còn lại (màn TW gộp một bảng thay vì hai bảng như màn của đơn vị; cấu trúc 21b ở Phụ lục D khác đặc tả
màn hình) là **điểm hoàn thiện đặc tả đã được mở ở phiếu khác**, không quyết định đạt/không đạt của phiếu này
và **không chặn bàn giao** — đã ghi rõ ở ô Kết quả verify để hai bên cùng nắm.

> **Không lấn sang phiếu A2.** Lỗi A2 đã log (đơn vị không được chọn vẫn bị đóng dấu "Đã tổng hợp") chỉ phát
> sinh **khi bấm [Lưu tổng hợp]**; phiếu A3 dừng trước bước đó nên không chạm tới, và đợt dùng lượt này chỉ có
> đúng 2 đơn vị — cả hai đều được chọn. **Không log trùng.**

## 11. Ảnh bằng chứng

| # | Tệp trong `image/` | Chứng minh điều gì |
|---|---|---|
| 01 | `THBCTHCT_02-01-menu-dot-bao-cao-dot-CA-HAI.png` | **Bước 1 của phiếu**: bấm menu "Đợt báo cáo" mở được; đợt `DOT-TRON_NAM-2026-1` (Tròn năm · 2 đơn vị · "Tạo đợt") — tiền đề trước khi đo |
| 02 | `THBCTHCT_02-02-da-tick-2-bao-cao-CA-HAI.png` | **Bước 2 (trước khi bấm)**: đã tick **đúng 2** báo cáo của đợt đó, cả hai "Đã gửi TW"; nút đổi thành **[Tổng hợp (2)]** |
| 03 | `THBCTHCT_02-03-sau-bam-tong-hop-bieu-mau-goi-y.png` | **Ảnh chốt K2a + K1**: ngay sau khi bấm [Tổng hợp (2)] — dòng **"Biểu mẫu: Biểu mẫu 21a + 21b/TP/HTPLDN"**, "Số đơn vị: 2", câu "Hệ thống đã cộng các chỉ tiêu tương ứng…", và các số 16 · 8 · 5 · 12 · 13 · 45 đúng bằng tổng hai báo cáo nguồn |
| 04 | `THBCTHCT_02-04-cuoi-bieu-13-chi-tieu-nut-luu.png` | Cuộn hết hộp: chỉ tiêu 8→13 (12 · 17 · 4 · 845.000.000 · 205.000.000 · 40.000.000), ô "Nhận xét, kiến nghị", nút [Hủy] / [Lưu tổng hợp] ⇒ biểu chỉ có **một bảng 13 chỉ tiêu**, kết thúc ở dòng 13 (căn cứ cho §6.4) |
| 05 | `THBCTHCT_02-05-sua-duoc-o-so-lieu-va-nhan-xet.png` | **Ảnh chốt K2b**: ô chỉ tiêu 13 nhận giá trị gõ tay **21550807**, ô nhận xét nhập được chữ, **12 ô còn lại giữ nguyên** |
| 06 | `THBCTHCT_02-06-doi-bo-chon-1-don-vi-so-doi-dung.png` | **Phép thử quyết định**: bỏ chọn An Giang → "Số đơn vị: 1" và 13 giá trị đổi đúng thành số riêng của Hà Nội (11 · 6 · 4 · 9 · 7 · 31 · 23…) ⇒ hệ thống cộng thật theo bộ chọn |

> Đã đối chiếu mã băm (md5) cả 6 ảnh — **không có hai ảnh trùng nhau**.

## 12. Ngoài tiêu chí đang chấm — có gì bất thường?

1. **Phiên đăng nhập `cbnv_tw_05` bị thu hồi giữa lượt đo** (lúc 21:41, ngay sau khi bấm [Hủy]) — máy chủ trả
   "Token đã bị thu hồi". Tra hộp thư giả lập thấy có **một tiến trình khác xin mã xác thực cho chính
   `cbnv_tw_05` lúc 21:40:44** (và `cbnv_tw_01` lúc 21:40:34) — tức tài khoản bị dùng song song, không phải lỗi
   phần mềm. Theo đúng luật fallback: **đổi sang `cbnv_tw_04`** — **cùng vai trò Cán bộ Nghiệp vụ Trung ương,
   cùng cấp TW, cùng đơn vị Cục Bổ trợ tư pháp** nên phạm vi dữ liệu không đổi. Phần đo trước 21:41 (§4, §5.1,
   §6.1, §6.3 — ảnh 01→05) do `cbnv_tw_05` thực hiện; phần đo lại và phép thử đổi bộ chọn (§5.2, §6.2 — ảnh 06)
   do `cbnv_tw_04` thực hiện, kết quả trùng khớp nhau.
2. **Hai lần gọi máy chủ trả 502 rỗng lúc 21:33** (khi dựng tiền đề, tài khoản `cbpd_dp_05`), gọi lại sau ~5 giây
   thì bình thường. Không tái hiện lần nào nữa trong suốt lượt đo ⇒ ghi nhận là **trục trặc nhất thời của môi
   trường**, không log thành lỗi phần mềm.
3. **Nút [Tổng hợp] bị khóa khi chỉ chọn báo cáo đã ở trạng thái "Đã tổng hợp"** — thử chọn 1 dòng của đợt
   `DOT-THBC01-UAT` thì nút hiện "Tổng hợp (1)" nhưng **mờ, không bấm được**. Đây là hành vi **hợp lý** (không
   cho tổng hợp lại), ghi nhận để khỏi hiểu nhầm là lỗi.
4. Các điểm đã nêu ở lượt 13:18 và ở phiếu A2 — màn "Tổng hợp báo cáo toàn quốc" không có lối vào trên menu;
   hai nút cùng tên "Tổng hợp" ở hai màn nhưng hành vi khác hẳn; nhãn đường dẫn "Tong Hop" không dấu — **vẫn còn
   nguyên** trên bản dựng này. **Chỉ nhắc, không mở trùng.**
