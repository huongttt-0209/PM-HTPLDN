# Bàn giao lô F8 — `Dopai = N/R` + `Trạng thái dev fix = Fixed` · 2026-08-07

**Phạm vi:** 23 dòng tab `bug` của `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` (gid `1714340219`).
**Quy trình:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Đặc tả — nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Môi trường:** `https://18.143.165.120.nip.io` (nội bộ) · bó mã **`assets/index-eWHwDgt2.js`**, `GET /` last-modified **07/08 09:11 giờ VN**, etag `W/"6a753eb7-428"` — đo 11:49 và 12:40, **trùng khít**.
**Tài khoản:** bộ `_03`, **6/6 đăng nhập được**, không phải fallback.

---

## 1. 🔴 Tình trạng: 1/23 phiếu đã chốt — **lô DỪNG GIỮA CHỪNG**

**Nguyên nhân dừng:** cả đội chạm **giới hạn API theo tuần** (reset **10/08 21:00 giờ VN**). Ba tác nhân bị
ngắt phiên trong lúc đang làm. **Không phải blocker nghiệp vụ, không phải lỗi môi trường.**

| Giai đoạn | Trạng thái |
|---|---|
| **A — khóa chuẩn chấm** | ✅ **XONG 23/23 phiếu** (22 file `chuan/` + 2 bảng tổng hợp + kiểm kê tiền đề) |
| **B — đo trên web** | ⏸ **1/23** — chỉ `KTDGKQHT_05` chạy xong và đã ghi bảng |

### Phiếu đã chốt

| Dòng | Mã TC | Verdict | Ô `Trạng thái dev fix` | Giờ ghi | Tóm tắt |
|---|---|---|---|---|---|
| 10 | `KTDGKQHT_05` | **Cần BA** | `BA confirm` | 12:47 | Lỗi cũ (bấm xác nhận nạp trả lỗi hệ thống) **đã hết**; còn 1 vế đặc tả im lặng về câu chữ thông báo |

Đã ghi **đúng 2 ô** (`Trạng thái dev fix` + `Kết quả verify`) và **đọc lại xác nhận**.
4 ô chỉ đọc (`Trạng thái`, `Kết quả thực tế`, `TKM phản hồi lần 1`, `DEV phản hồi lần 1`) **nguyên vẹn**.
Nhật ký: `tools/sheet_update_audit.jsonl`, lọc `reason` = `FLOW04 lo F8 - KTDGKQHT_05`.
Chi tiết: [`do/KTDGKQHT_05.md`](do/KTDGKQHT_05.md) · nội dung ô: [`note/KTDGKQHT_05.txt`](note/KTDGKQHT_05.txt).

> ⚠️ Phần thao tác giao diện của phiếu này do một thành viên chạy lúc 12:04–12:06 rồi **bị ngắt phiên trước
> khi kịp viết nhật ký**. Điều phối đã **dựng lại từ hiện vật và xác minh lại độc lập** (mở 2 tệp xlsx bằng
> `openpyxl`, tự xem lại từng ảnh, **đọc lại bản ghi điểm danh qua API lúc 12:35**, đo lại vân tay bản dựng
> lúc 12:40). Cách dựng lại ghi minh bạch ở §0 của `do/KTDGKQHT_05.md`.

---

## 2. 🔴 Điểm quan trọng nhất của lô: 22/23 phiếu **không phải "bug dev đã fix"**

`Trạng thái` = `N/R`, `Kết quả thực tế` RỖNG, `Ảnh/vieo 1` RỖNG ⇒ **bên nghiệm thu chưa từng chạy** các
phiếu này. `Fixed` ở đây nghĩa là *"dev đã dựng xong, mời chạy"*, **không** phải *"đã sửa lỗi bạn báo"*.
⇒ `expected đối tác` lấy từ **cột `Kết quả mong đợi`**; không có triệu chứng cũ để đối chiếu.
Quy tắc viết ô `Kết quả verify` cho nhóm này: xem [`QUYET-DINH-DIEU-PHOI.md`](QUYET-DINH-DIEU-PHOI.md) QĐ-03.

---

## 3. Kết quả Giai đoạn A — **15/22 phiếu chắc chắn KHÔNG thể Pass**, biết trước khi đo

Đây là giá trị lớn nhất lô này để lại: chuẩn chấm đã khóa, đo xong là ra verdict ngay.

| Nhóm | Phiếu | Vế | MATCH | DIFF | GAP | Route BA | Route TEST thuần |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `QLHDTVVCG` (hợp đồng tư vấn) | 18 | 60 | 41 | 4 | 15 | **12** | 6 |
| Báo cáo chương trình | 4 | 17 | 13 | 2 | 2 | **3** | 1 |
| **Tổng** | **22** | **77** | **54** | **6** | **17** | **15** | **7** |

- **7 phiếu có thể Pass thẳng** nếu đo đạt: `QLHDTVVCG_03` · `_04` · `_05` · `_18` · `_19` · `_24` · `TPDBCKQTHCT_02`.
- **15 phiếu chắc chắn route BA** (≥1 vế `DIFF`/`GAP` ⇒ **cấm Pass toàn phiếu**, flow 04 luật khóa 5).
  Vẫn phải đo đủ 54 vế `MATCH`: vế `MATCH` nào sai thì kết quả là **Reopen + cần BA**.

### 6 vế `DIFF` — đặc tả nói **ngược** kỳ vọng phiếu (dev đúng SRS vẫn thuộc nhóm cần BA)

| Phiếu | Đối tác kỳ vọng | SRS quy định |
|---|---|---|
| `_15`, `_21` | Lưu xong **quay về danh sách** | Nhóm X.3 **không có màn danh sách độc lập**; trả về ngữ cảnh đã mở biểu mẫu (`srs-fr-14:175` `[BA chốt 2026-08-06]`, `:187`) |
| `_16` | Tên tệp `HDTV-danh-sach-{…}.xlsx` | Khuôn bắt buộc PascalCase, **bỏ mọi ký tự không phải chữ/số** (`srs-v3.5.md:6760`) |
| `_26` | Nhập Số tiền → **tự cộng dồn** thanh tiến trình | Thanh tiến trình = SUM(**đã thanh toán**)/giá trị HĐ; dòng mới mặc định chưa thanh toán (`srs-fr-14:301`, `:112`) |
| `THBCTHCT_05` C6 | Cuối trang có **chức danh người ký** | SRS nói ngược: *"không in sẵn dòng chức danh"* (`srs-fr-15:1017`, `srs-v3.5.md:6722`–`:6723`) |
| `THBCTHCT_05` C7 | `BaoCaoTongHop_CTHTPL_…` | SRS chốt `BaoCaoTongHopCTHTPL_…` (viết liền) |

### 17 vế `GAP` — nhóm đáng chú ý nhất

- **3 phiếu `_02`/`_08`/`_09` cùng dính một lỗ hổng tài liệu:** kỳ vọng *"hiển thị giống **thiết kế**"*, SRS trỏ
  sang `dac-ta-man-hinh-chuc-nang-v2.md — MH-14.1`, **tệp này không tồn tại trong nguồn chuẩn** (đã `find`
  toàn repo). ⇒ Không có mốc để chấm "giống thiết kế".
- `THBCTHCT_01` C2: đặc tả **tự mâu thuẫn** — đầu vào là danh sách báo cáo **theo đơn vị** nhưng lại bắt đổi
  trạng thái của **ĐỢT**, mà một đợt chỉ có một giá trị trạng thái trong khi phạm vi đợt là ~70–83 đơn vị;
  trục đơn vị **không có** giá trị `DA_TONG_HOP`.

---

## 4. 🔴 Ràng buộc bắt buộc cho người chạy tiếp Giai đoạn B

1. **Hợp đồng tư vấn: hệ thống đang có 0 bản ghi.** Quét vét cạn 111 lượt (44 TVV × 7 TCTV × 60 VV). ⇒ 13/18
   phiếu phải **seed trước**, và cần **2 hợp đồng khác nhau**: một **có** vụ việc liên kết (cho `_18`), một
   **không có** (cho `_17`). Seed = mutate môi trường chung ⇒ **khai vào báo cáo**.
2. **`GET /api/v1/hop-dong-tu-vans` trả 403 nếu thiếu tham số ngữ cảnh** (`vuViecId`/`tuVanVienId`/
   `toChucTuVanId`), và **không có tham số từ khóa**. Việc đầu tiên phải làm là **xác định đường vào màn**;
   nếu không có màn danh sách độc lập thì **cả cụm 18 phiếu kẹt cùng lúc**. (Xem thêm vế `DIFF` của `_15`/`_21`
   — đặc tả cũng nói nhóm này không có màn danh sách độc lập. Hai manh mối này khớp nhau.)
3. **Nhóm `THBCTHCT` chỉ đo sạch được MỘT lượt** — tổng hợp xong là 2 báo cáo rời khỏi `DA_GUI_TW`.
   **Thứ tự bắt buộc: `THBCTHCT_02` → `THBCTHCT_01` → `THBCTHCT_05`.** Cặp báo cáo sạch cùng đợt/kỳ/biểu mẫu:
   `c4801d2d…` (Bộ KH&ĐT) + `df6498aa…` (Sở TP An Giang), thuộc `DOT-THBC01-UAT`.
   Dự phòng nếu mất: `cbpd_bn_03` duyệt + `cbnv_bn_03` gửi TW trên 2 đợt Bộ KH&ĐT đang `CHO_DUYET`.
4. **`TPDBCKQTHCT_02` không cần dựng gì** — 2 báo cáo `DU_THAO` của `cbnv_dp_03` mới có 3/13 chỉ tiêu, đúng
   nghĩa "báo cáo chưa đầy đủ". Đây là phiếu **dễ chốt nhất**, nên chạy đầu tiên.
5. **Khóa `KH-QAW7-HOINGHI` nay không còn buổi học nào sạch** (4/4 buổi đã có dữ liệu điểm danh, buổi 4 do
   chính lượt đo hôm nay ghi). Muốn đo lại `KTDGKQHT_05` phải **tạo buổi mới** hoặc dùng khóa khác `DANG_DIEN_RA`.
6. **Chỉ MỘT tác nhân dùng trình duyệt tại một thời điểm** — cả đội chung một phiên Chrome.
7. **Chụp giá trị ô trước khi ghi** đã có sẵn: [`audit/gia-tri-o-truoc-khi-ghi.md`](audit/gia-tri-o-truoc-khi-ghi.md).
   Luôn truyền `--expect` + `--expect-file`; lệch ⇒ có người vừa sửa dòng, đọc lại rồi mới ghi.

---

## 5. Dữ liệu đã thay đổi trên môi trường

| Đổi gì | Bản ghi | Do đâu |
|---|---|---|
| Ghi 3 bản ghi điểm danh (`CO_MAT`, `VANG_PHEP`, `VANG_KHONG_PHEP`) | Buổi 4 (`bd1cdf35…c8c2`) khóa `KH-QAW7-HOINGHI` | **Hệ quả trực tiếp của thao tác đang verify**, không phải seed thêm |

Ngoài ra **không seed, không sửa, không xóa gì**. Trinh sát chỉ gọi `GET`.

## 6. Bug mới / candidate

**Chưa mở dòng bug mới `_QA<n>` nào.** Hai candidate ghi nhận ở `do/KTDGKQHT_05.md` §6, **cả hai không phải lỗi**:
danh sách điểm danh không có cột mã học viên (**đúng ý nghiệp vụ đã chốt** `srs-fr-03:14` — không thêm trường),
và giao diện dùng từ "Import" trong nhãn tiếng Việt (không thuộc vế nào của phiếu).

## 7. Việc còn lại

22 phiếu chưa đo. Chuẩn chấm **đã khóa xong toàn bộ** ⇒ người chạy tiếp **không phải làm lại Giai đoạn A**,
chỉ cần: đọc `chuan/<MÃ>.md` → dựng tiền đề → đo → viết `do/` + `note/` → tải ảnh Drive → ghi 2 ô → đọc lại.
Thứ tự đề xuất: `TPDBCKQTHCT_02` → `THBCTHCT_02` → `THBCTHCT_01` → `THBCTHCT_05` → cụm `QLHDTVVCG`
(bắt đầu bằng việc xác định đường vào màn, rồi seed 2 hợp đồng).
