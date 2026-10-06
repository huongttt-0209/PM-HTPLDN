# BÀN GIAO — nhóm "Báo cáo thực hiện Chương trình HTPL" (4 phiếu) — lô F8, 07/08/2026

> Tác nhân ĐO nhóm BCCT. Chạy **tuần tự** đúng thứ tự bắt buộc: **341 → 344 → 343 → 345**.
> Mỗi phiếu: đo → viết `do/` → ảnh + Drive → viết `note/` → dry-run → ghi bảng → đọc lại xác nhận,
> **rồi mới sang phiếu kế tiếp**.
> Bảng ghi: `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, tab `bug`. Mọi lượt ghi đều kèm `--expect-file`.

---

## 1. Kết quả 4 phiếu

| Dòng | Mã TC | Verdict | Ô `Trạng thái dev fix` (R) | Lý do một câu |
|---|---|---|---|---|
| **341** | `TPDBCKQTHCT_02` | ✅ **Pass** | **`Test done`** | 2/2 vế MATCH đều đạt — hệ thống chặn trình duyệt khi báo cáo còn chỉ tiêu bỏ trống và hiện đúng nguyên văn *"Vui lòng hoàn chỉnh báo cáo trước khi trình"*. |
| **344** | `THBCTHCT_02` | ⚠️ **Cần BA** | **`BA confirm`** | 2/2 vế MATCH đạt (gợi ý số liệu đúng bằng tổng 13/13 chỉ tiêu; biểu mẫu sửa và bổ sung được), còn vế C2b là **GAP** — đặc tả không quy định biểu mẫu tổng hợp có phải hiện đủ cả 21a lẫn 21b. |
| **343** | `THBCTHCT_01` | ⚠️ **Cần BA** | **`BA confirm`** | 3/3 vế MATCH đạt (lưu được bản ghi tổng hợp toàn quốc `TONG_HOP_TW`, có lưu vết, thông báo đúng nguyên văn), còn vế C2 là **GAP** — đặc tả tự mâu thuẫn về việc "cái gì" chuyển sang Đã tổng hợp. |
| **345** | `THBCTHCT_05` | ⚠️ **Cần BA** | **`BA confirm`** | 6/6 vế MATCH đạt trên **cả hai** định dạng (mở nội dung tệp bằng thư viện: A4, Times New Roman 13, quốc hiệu, tên cơ quan, ngày ký, 13/13 chỉ tiêu khớp), còn C6 (chức danh người ký) và C7 (khuôn tên tệp) là **DIFF**. |

**Không phiếu nào Chưa chốt. Không phiếu nào Reopen.**
**Không hạ `DIFF`/`GAP` xuống `MATCH`** ở bất kỳ phiếu nào — kể cả phiếu 345 nơi tên tệp thực tế **đúng
đặc tả** (luật khóa 5 vẫn cấm chấm).

## 2. Ô đã ghi — thời điểm + đọc lại

| Dòng | Ô R `Trạng thái dev fix` | Ô T `Kết quả verify` | Giờ ghi | Đọc lại xác nhận |
|---|---|---|---|---|
| 341 | `Fixed` → **`Test done`** | rỗng → `note/TPDBCKQTHCT_02.txt` (4.695 ký tự) | 13:07:19 | ✅ R + T |
| 344 | `Fixed` → **`BA confirm`** | rỗng → `note/THBCTHCT_02.txt` (6.298 ký tự) | 13:43:47 | ✅ R + T |
| 343 | `Fixed` → **`BA confirm`** | rỗng → `note/THBCTHCT_01.txt` (7.870 ký tự) | 13:54:01 | ✅ R + T |
| 345 | `Fixed` → **`BA confirm`** | rỗng → `note/THBCTHCT_05.txt` (7.865 ký tự) | 14:05:21 | ✅ R + T |

- Mọi lượt ghi đều qua `tools/sheet_bug_verify_write.py` với `--expect 'Trạng thái dev fix=Fixed'` +
  `--expect-file 'Kết quả verify=/tmp/f8_empty.txt'` (chặn ghi đè mù khi có phiên khác sửa cùng bảng).
  **Không lượt nào báo lệch giá trị cũ** ⇒ không có ai đụng 4 dòng này trong lúc đo.
- Nhật ký ghi: `tools/sheet_update_audit.jsonl` (4 mục, `verified: true`).
- 🔴 **4 ô chỉ-đọc không đụng tới:** `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` ·
  `DEV phản hồi lần 1`.
- Đọc lại lần cuối lúc 14:07 bằng phiên đọc riêng: 341 = `Test done`, 343/344/345 = `BA confirm`, cả 4 ô T
  đều có nội dung đúng.

## 3. 🔴 Dấu vân tay bản dựng — **ĐÃ ĐỔI GIỮA PHIÊN**

| Mốc | Bó mã giao diện | `last-modified` |
|---|---|---|
| **Đầu phiên** (12:40) + kiểm lại 13:15:28 | `assets/index-eWHwDgt2.js` | `Fri, 07 Aug 2026 02:11:03 GMT` = **09:11 giờ VN** |
| **13:55** và **cuối phiên 14:06:36** | **`assets/index-BbPPdate.js`** | **`Fri, 07 Aug 2026 06:47:57 GMT`** = **13:47:57 giờ VN** |

**Có một lượt lên bản mới lúc 13:47:57 giờ VN**, nằm **giữa** phiếu 343 và phiếu 345. Phân định:

| Phiếu | Mốc đo | Bản dựng khi đo |
|---|---|---|
| 341 `TPDBCKQTHCT_02` | 12:55–13:02 | `index-eWHwDgt2.js` (**cũ**) |
| 344 `THBCTHCT_02` | 13:18–13:29 | `index-eWHwDgt2.js` (**cũ**) |
| 343 `THBCTHCT_01` | 13:30–13:45 | `index-eWHwDgt2.js` (**cũ**) |
| 345 `THBCTHCT_05` | 13:56–13:57 | **`index-BbPPdate.js` (MỚI)** |

**Đối chứng ảnh hưởng:** tệp Excel xuất lúc **13:32** (bản cũ) và tệp xuất lúc **13:56** (bản mới) **trùng
khít từng ô nội dung** (đối chiếu chương trình 29×3 ô, 0 ô lệch) ⇒ lượt lên bản **không** làm đổi kết quả
quan sát của nhóm phiếu này. Đã khai trong `note/THBCTHCT_05.txt` để đối tác nắm.

⚠️ **Cảnh báo cho vòng sau:** nếu vòng verify tiếp theo chạy trên `index-BbPPdate.js` mà thấy khác kết quả
341/344/343, **không phải lỗi mới** — phải tính đến lượt lên bản này trước khi kết luận Reopen.

## 4. 🔴 Dữ liệu đã dựng / đã thay đổi trên môi trường nội bộ

**Chỉ hai phiếu ghi dữ liệu; hai phiếu còn lại thuần đọc.**

### 4.1 Phiếu 341 `TPDBCKQTHCT_02` — dựng tiền đề "báo cáo chưa đầy đủ"

| Đối tượng | Thay đổi | Trạng thái sau |
|---|---|---|
| Báo cáo của **Sở Tư pháp An Giang** trong đợt **`DOT-SO_BO_6_THANG-2026-1`** | Điền chỉ tiêu 12 "KP chi HĐ khác" = **40.000.000**, ghi chú mang mốc `QA-F8-341-20260807-1300`; **cố ý để trống** chỉ tiêu 13 "KP xã hội hóa"; bấm **Lưu nháp** | vẫn **bản nháp**, đơn vị vẫn `DANG_LAP`, **không** chuyển trạng thái |

### 4.2 Phiếu 343 `THBCTHCT_01` — thao tác bắt buộc của chính phiếu

| Đối tượng | Trước | Sau |
|---|---|---|
| Đợt **`DOT-THBC01-UAT`** (`d7a62f6e-a119-4582-8b08-f935d25c534b`) | `TAO_DOT`, `version 2` | **`DA_TONG_HOP`**, `version 3` (`daGuiTw` vẫn `false`) |
| Báo cáo `c4801d2d-dedc-4ffe-b5d2-44e9245fbedc` (Bộ KH&ĐT) | `DA_GUI_TW` | **`DA_TONG_HOP`** |
| Báo cáo `df6498aa-4ae4-4d59-ba3e-7c322e1f9a59` (Sở TP An Giang) | `DA_GUI_TW` | **`DA_TONG_HOP`** |
| **Bản ghi mới** `57d4ce85-03b6-4d62-8f76-bb7546bec5c5` | không tồn tại | **được tạo** — `TH-TW-1786084251126`, `loai TONG_HOP_TW`, `trangThai DA_DUYET`, nhận xét mang mốc `QA-F8-343-20260807-1330` |

**Trục ĐƠN VỊ không đổi:** cả hai đơn vị vẫn `DA_NOP`.

### 4.3 Phiếu 344 và 345 — **không ghi gì**

- **344:** hai lượt bấm [Tổng hợp] chỉ là bước gợi ý số liệu (chỉ đọc); giá trị gõ thử `13250807` và câu
  nhận xét chỉ nằm trên màn rồi bấm **Hủy**. Kiểm lại sau đó: đợt và hai báo cáo giữ nguyên.
- **345:** hai lượt `POST …/tong-hop/export` chỉ sinh tệp. Kiểm lại sau đó: đợt vẫn `DA_TONG_HOP`, ba dòng
  trên màn giữ nguyên nhãn.

### 4.4 ⚠️ Hệ quả cho lô sau — tiền đề đã tiêu thụ

Cặp báo cáo `DA_GUI_TW` của đợt `DOT-THBC01-UAT` **đã dùng hết**, không tổng hợp lại được (nút [Tổng hợp]
bị vô hiệu). Muốn dựng lại tiền đề tổng hợp:
- Bộ KH&ĐT còn 2 báo cáo `CHO_PHE_DUYET`: `c19b1bc2…` (đợt `DOT-SO_BO_NAM-2026-1`) và `a63bf70c…`
  (đợt `DOT-SO_BO_6_THANG-2026-1`) → `cbpd_bn_03` duyệt rồi `cbnv_bn_03` gửi TW.
- Báo cáo `4db99158…` (Sở TP Hà Nội, đợt `DOT-SO_BO_NAM-2026-1`) vẫn `DA_GUI_TW`, **chưa bị đụng**.

**Không đụng dữ liệu của đối tác. Không ghi thẳng cơ sở dữ liệu. Không ép trạng thái bằng đường dữ liệu.**

## 5. Tài khoản đã dùng — có một lần đổi phải khai

| Vai trò | Tài khoản | Dùng ở phiếu |
|---|---|---|
| CB Nghiệp vụ **Địa phương** (Sở TP An Giang) | `cbnv_dp_03` | 341 (ra verdict) |
| CB Nghiệp vụ **Trung ương** | **`cbnv_tw_05`** | 344 · 343 · 345 (ra verdict) |
| CB Nghiệp vụ Địa phương | `cbnv_dp_05` | 344 · 343 — **chỉ để đọc** số liệu nguồn / đọc lại trạng thái bằng phiên độc lập |
| 🔴 Quản trị hệ thống | `admin` | **343 — CHỈ để ĐỌC Nhật ký hệ thống** (vế C3), đúng ngoại lệ chuẩn cho phép. Không ra verdict, không thao tác gì khác. |

🔴 **Đổi tài khoản trong lúc chạy:** chuẩn chỉ định `cbnv_tw_03`, nhưng tài khoản này bị **thu hồi phiên hai
lần** (`ERR-AUTH-SYS-00-03`) do một tiến trình khác đăng nhập song song (hệ thống chỉ cho một phiên/tài
khoản). Theo Rule 7 (đổi trong **cùng vai trò + cùng cấp + cùng đơn vị**) đã chuyển sang **`cbnv_tw_05`** —
cùng `CB_NV_TW`, cùng cấp TW, cùng `donViId 00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp)
⇒ phạm vi dữ liệu không đổi. Đã khai trong `do/` và trong ô T của cả ba phiếu 344/343/345.
⚠️ Ghi nhận cho lô sau: `cbnv_tw_03` đang bị tranh chấp phiên — đừng dùng nếu có tiến trình khác chạy song song.

## 6. Bốn câu hỏi gửi nghiệp vụ (nguyên nhân 3 phiếu `BA confirm`)

| # | Phiếu | Vế | Câu hỏi tóm tắt | Hiện trạng web/dev đo được |
|---|---|---|---|---|
| 1 | 344 | C2b (GAP) | Biểu mẫu tổng hợp của TW có bắt buộc hiện **cả 21a lẫn 21b** không, hay chỉ hiện biểu mà các báo cáo được chọn thực sự dùng? | Chỉ hiện **21a** — đúng bằng biểu mà cả hai báo cáo nguồn và đợt đang dùng |
| 2 | 343 | C2 (GAP) | Sau khi TW lưu tổng hợp thì **cái gì** chuyển sang "Đã tổng hợp": cả đợt / từng bản nộp của đơn vị được chọn / chỉ bản ghi tổng hợp TW? Đợt có bắt buộc đi qua "Đã gửi TW" trước không? | Đợt `TAO_DOT` → `DA_TONG_HOP` (**không** qua `DA_GUI_TW`); đơn vị giữ `DA_NOP`; 2 báo cáo được chọn `DA_GUI_TW` → `DA_TONG_HOP` |
| 3 | 345 | C6 (DIFF) | Tệp xuất có phải **in sẵn dòng chức danh người ký** không, hay giữ ngoại lệ §D.2.4 (chỉ chừa chỗ trống)? Phiếu viết trước hay sau chốt 06/08/2026? | Khối cuối: ngày ký → "NGƯỜI XUẤT BÁO CÁO" → "(Ký, ghi rõ họ tên và đóng dấu)" → họ tên cán bộ xuất. **Không** có dòng chức danh in sẵn |
| 4 | 345 | C7 (DIFF) | Khuôn tên tệp chốt là `BaoCaoTongHopCTHTPL_…` (theo §H8) hay `BaoCaoTongHop_CTHTPL_…` (theo phiếu)? | `BaoCaoTongHopCTHTPL_20260807_1356.xlsx` / `…_1357.docx` — **viết liền**, đúng đặc tả, lệch phiếu đúng một dấu gạch dưới |

Câu hỏi #2 **cùng gốc** với câu hỏi ba-trục-trạng-thái đã gửi ở bàn giao lô F5 — **liên kết, không mở câu
hỏi trùng**.

## 7. Bug mới / ứng viên bug — **KHÔNG mở dòng bug mới nào**

Không dòng `<prefix>_QA<n>` nào được tạo. Các quan sát dưới đây **đều nằm ngoài vế của phiếu** hoặc **đặc tả
im lặng** ⇒ chỉ ghi nhận cho dev/BA, đúng luật "chỉ ghi lệch trong đúng màn/phản hồi/tệp đang quan sát,
không mở rộng case":

| # | Quan sát | Ở phiếu | Vì sao không log thành bug |
|---|---|---|---|
| 1 | Màn **"Tổng hợp báo cáo toàn quốc"** (`/ct-htpldn/tong-hop`) **không có lối vào trên menu**, cũng không có nút dẫn từ màn "Đợt báo cáo" — cán bộ chỉ vào được nếu biết sẵn đường dẫn | 344 | Phiếu không nhắc lối vào. **Ứng viên bug — mức nặng nhất trong danh sách này**, đề nghị điều phối cân nhắc mở phiếu riêng |
| 2 | **Hai nút cùng tên "Tổng hợp"** làm việc khác hẳn: nút ở màn chi tiết đợt hỏi xác nhận rồi chuyển trạng thái đợt ngay (không xem trước số liệu); nút ở màn tổng hợp toàn quốc mới là bước gợi ý cho sửa trước khi lưu | 344 | Phiếu không nhắc; rủi ro nhầm lẫn cho người dùng |
| 3 | **Không có đường đọc lại bản ghi tổng hợp** đã lưu; màn chi tiết đợt vẫn hiển thị số của **một đơn vị** (Bộ KH&ĐT: 8, 3, 2…) chứ không phải số tổng (12, 4, 3…). Cán bộ chỉ thấy số tổng qua tệp xuất | 343 · 345 | Phiếu không nhắc việc xem lại. Cũng là **giới hạn của phép đo** — đã khai thẳng trong `do/` |
| 4 | Mục nhật ký của thao tác tổng hợp để trống `ipAddress`, `endpoint`, `responseCode` | 343 | `:1007` chỉ đòi *"ghi nhật ký thao tác"*, không đòi các trường này |
| 5 | Hộp xác nhận **"Trình duyệt kết quả?"** không tự đóng sau khi máy chủ từ chối — người dùng thấy lỗi nhưng vẫn phải tự bấm "Hủy" | 341 | Đặc tả không quy định hành vi đóng hộp thoại |
| 6 | **Không có thông báo nào sau khi xuất tệp** | 345 | FR-XI-09 **không khai** mã thông báo cho thao tác xuất ⇒ vùng đặc tả im lặng |
| 7 | Tệp Word **không dùng phần đầu trang/chân trang** của văn bản; quốc hiệu nằm trong thân ⇒ tệp nhiều trang sẽ không lặp quốc hiệu | 345 | Đặc tả không quy định chỗ đặt |

**Ghi nhận tích cực (đã xử lý so với đợt trước):** mã lỗi khi trình báo cáo chưa đầy đủ nay đúng đặc tả
(`ERR-XI-07-01`, trước là `ERR-VAL-XI-07-02`), và danh sách "chỉ tiêu còn thiếu" nay chỉ liệt kê đúng ô cán
bộ bỏ trống, không còn kéo theo các chỉ tiêu do hệ thống tự tính — thông tin này liên quan phiếu
`TPDBCKQTHCT_01`, đề nghị bên đó kiểm lại.

## 8. Sản phẩm bàn giao

```
F8-NR-fixed-2026-08-07/
├── BAN-GIAO-BCCT.md                     ← tệp này
├── do/   TPDBCKQTHCT_02.md · THBCTHCT_02.md · THBCTHCT_01.md · THBCTHCT_05.md
├── note/ TPDBCKQTHCT_02.txt · THBCTHCT_02.txt · THBCTHCT_01.txt · THBCTHCT_05.txt   (= nội dung ô T)
├── image/ 8 ảnh (3 + 3 + 2 + 2), tất cả đã mở xem lại bằng mắt trước khi dùng, tất cả đã lên Drive
└── files/ BaoCaoTongHopCTHTPL_20260807_1356.xlsx · BaoCaoTongHopCTHTPL_20260807_1357.docx
          (+ BaoCaoTongHopCTHTPL_20260807_1332.xlsx — tệp bản dựng cũ, giữ để đối chứng §3)
```

Link Drive tích luỹ ở `tools/evidence_drive_links_f8.json`. **Trong ô T của bảng chỉ dùng link Drive xem
được, không có đường dẫn tệp trên máy.**

## 9. Kỷ luật đo đã giữ

- **Mọi thao tác tranh chấp bấm bằng giao diện thật:** [Trình duyệt KQ] · [Tổng hợp] · [Lưu tổng hợp] ·
  [Xuất Excel] · [Xuất Word]. Đường dẫn máy chủ chỉ dùng để **dựng tiền đề** và **đối chứng**.
- **Không Pass bằng quan sát tĩnh:** mỗi vế có **1 đường giao diện + 1 đường đối chứng độc lập**; không vế
  nào có hai đường mâu thuẫn.
- **Phiếu 345 mở nội dung tệp bằng thư viện** (`openpyxl` 3.1.5 / `python-docx`), **không** chấm bằng ảnh.
- **Bắt thông báo:** bộ theo dõi cài **trước** thao tác, đọc bằng `innerText`, **không lọc trùng**; đếm cả
  số yêu cầu gửi đi. Ở 341 và 343 đều ra **1 thông báo / 1 yêu cầu** (hai nút DOM lệch vài mili-giây là
  khung ngoài + phần thân của cùng một thông báo).
- **Không dùng `admin` để ra verdict** — chỉ đọc nhật ký ở 343, đúng ngoại lệ chuẩn cho phép.
- **Mỗi bước chuyển trạng thái đều `GET` lấy `version` trước** — không lần nào gặp lỗi xung đột phiên bản.
- **Đo dấu vân tay bản dựng đầu và cuối phiên** — phát hiện lượt lên bản 13:47:57 và đã phân định (§3).
