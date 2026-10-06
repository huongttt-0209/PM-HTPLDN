# QLDXDTTH_13 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 137 · Verdict Verify 2: `Pass`
> Bug gốc: *"Thông báo **'Đề xuất đào tạo mới'** hiển thị bằng **biểu tượng báo lỗi (dấu X đỏ)** thay vì biểu tượng
> thông tin"* — nguyên văn phần kết quả thực tế: *"hiển thị biểu tượng dấu X trong vòng tròn màu đỏ, giống hệt biểu
> tượng báo lỗi. **Bốn dòng thông báo còn lại** trong cùng danh sách đều dùng dấu tích xanh. Cán bộ dễ hiểu nhầm là
> hệ thống đang có sự cố."*
> Kết quả mong đợi của phiếu: *"…nên dùng **biểu tượng trung tính hoặc biểu tượng thông tin**, không dùng biểu tượng báo lỗi."*
> Bug phụ thuộc **có thông báo thật vừa sinh ra + đúng người nhận + loại thông báo** ⇒ KHÔNG phải bug tĩnh
> (không thể chấm bằng cách ngồi nhìn danh sách thông báo cũ) ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Tiền đề 1 — **phải có đề xuất vừa được doanh nghiệp gửi** | *"Doanh nghiệp vừa gửi một đề xuất đào tạo"*; dữ liệu phiếu là đề xuất `QA-VERIFY-0803` gửi 16:22 ngày 03/08 | **Tự sinh thông báo thật** (không dùng lại thông báo cũ): đăng nhập tài khoản doanh nghiệp **`0311224477`** (`QA Kiem Chung`) → gửi đề xuất `QA-V2-0804-C` lĩnh vực `Lao động`, thời gian `quy 1/2027`, nơi `An Giang`, số lượng `15` lúc **17:49 ngày 04/08/2026**. Bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`) ghi **1 lần gọi máy chủ ↔ 1 khung thông báo** *"Đề xuất đào tạo đã được gửi thành công"* ⇒ đúng là có thông báo mới được đẩy đi | Không |
| Tiền đề 2 — **người xem phải là cán bộ nghiệp vụ của đơn vị tiếp nhận** | *"Đăng nhập tài khoản Cán bộ nghiệp vụ thuộc đơn vị tiếp nhận"* | **`cb_nv_dp_01`** — `CB NV DP 01 (AG)`, `CB_NV_DP`, cùng đơn vị `Sở Tư pháp An Giang` với đề xuất vừa gửi. Đúng 2 phút sau khi gửi, chuông của tài khoản này có dòng mới *"Đề xuất đào tạo mới — Có đề xuất đào tạo mới từ người dùng QA Kiem Chung — một phút trước"* ⇒ đúng cặp người gửi ↔ người nhận | Không |
| Thao tác quan sát | *"Bấm biểu tượng chuông thông báo trên thanh đầu trang"* rồi *"nhìn biểu tượng bên trái dòng 'Đề xuất đào tạo mới'"* | Làm đúng vậy: bấm chuông trên thanh đầu trang → đọc biểu tượng bên trái từng dòng bằng **2 phép đo độc lập**: (a) đọc tên biểu tượng + màu thực tế mà trình duyệt đang vẽ; (b) **chụp ảnh màn hình và mở ảnh ra xem bằng mắt**. Hai phép đo khớp nhau | Không |
| Biểu tượng của chính dòng bị than phiền | Dấu **X trong vòng tròn ĐỎ** (biểu tượng báo lỗi) | Dòng *"Đề xuất đào tạo mới"* nay là **biểu tượng chữ "i" trong vòng tròn** (biểu tượng thông tin), màu **xanh dương** `rgb(37, 99, 235)`. **Không còn** dấu X, không còn màu đỏ. Đúng như kết quả mong đợi của phiếu ("biểu tượng thông tin") | Không |
| So sánh với các dòng khác trong cùng danh sách | Phiếu nói **4 dòng còn lại** dùng dấu tích xanh ⇒ dòng đề xuất bị lạc lõng thành "báo lỗi" | Trong cùng danh sách của `cb_nv_dp_01`: **3 dòng "Đề xuất đào tạo mới"** đều là biểu tượng thông tin xanh dương giống hệt nhau, **2 dòng "Quá hạn nộp báo cáo…"** là **biểu tượng cảnh báo (tam giác) màu hổ phách** `rgb(217, 119, 6)` — hợp nghĩa vì đó đúng là cảnh báo quá hạn. Không dòng nào mang biểu tượng báo lỗi ⇒ dòng đề xuất **không còn lạc lõng** | Không |
| Loại thông báo (biến quyết định biểu tượng) | Phiếu không tách; dev khai đã đổi cho **mọi thông báo hệ thống** (đề xuất mới / kích hoạt tài khoản / đăng nhập / đổi mật khẩu) | Bản ghi thông báo vừa sinh mang đúng loại **hệ thống** mà dev khai đã sửa. Kiểm chéo thêm **tài khoản khác cấp** — `cbnv_tw` (`Cán bộ NV Trung ương`): 5 dòng mới nhất *"Tài khoản vừa đăng nhập ở nơi khác"* (cũng thuộc nhóm hệ thống, thuộc phần dev khai đã đổi) **đều là biểu tượng thông tin xanh dương**, 0 dòng đỏ ⇒ lời khai của dev đúng ở ít nhất 2 kiểu thông báo hệ thống, trên 2 tài khoản khác cấp | Không |
| Màn hình khác cùng chức năng (kiểm rộng hơn phiếu) | Phiếu chỉ nêu danh sách xổ xuống từ chuông | Mở thêm **trang "Xem tất cả thông báo"**: trang này **không vẽ biểu tượng nào** cho từng dòng — chỉ có **chấm tròn nhỏ** đánh dấu chưa đọc kèm **nhãn chữ** phân loại (`Hệ thống` / `Cảnh báo SLA`). Tức là **không có** biểu tượng báo lỗi ở đây, và cũng không mâu thuẫn với danh sách xổ xuống | Không |

## Đo được

- **Lúc gửi đề xuất** (bộ bắt thông báo bắt buộc, tự kiểm `soObserverDangSong = 1`):

```json
{"SO_REQUEST":1,"request":["POST /api/v1/de-xuat-dao-taos"],
 "SO_KHUNG_THONG_BAO":1,"chu":["Đề xuất đào tạo đã được gửi thành công"],
 "BI_LAP":false,"khoangCachMs":null}
```

- **Biểu tượng trong danh sách thông báo của `cb_nv_dp_01`** (đo bằng tên biểu tượng + màu trình duyệt đang vẽ):
  `info-circle` `rgb(37, 99, 235)` ×3 (cả 3 dòng "Đề xuất đào tạo mới", gồm dòng vừa sinh lúc 17:49) ·
  `warning` `rgb(217, 119, 6)` ×2 (2 dòng quá hạn nộp báo cáo) · **`close-circle` (dấu X): 0 dòng** · **màu đỏ: 0 dòng**.
- **Kiểm chéo tài khoản `cbnv_tw`:** 5/5 dòng mới nhất là `info-circle` `rgb(37, 99, 235)`, **0** dòng `close-circle`.
- **Trang "Xem tất cả thông báo":** 0 biểu tượng trạng thái được vẽ cho từng dòng (chỉ chấm chưa đọc + nhãn chữ).

## Đã cố BÁC BỎ kết luận `Pass` cũ bằng những cách nào

1. **Không chấm bằng thông báo cũ.** Tự chạy trọn luồng sinh thông báo mới (đăng nhập doanh nghiệp → gửi đề xuất) rồi mới đi soi biểu tượng — đúng yêu cầu "phải sinh thông báo thật".
2. **Dùng đúng người nhận**, cán bộ **cùng đơn vị** với đề xuất, chứ không lấy bừa một cán bộ khác đơn vị (lấy sai thì thông báo không tới, sẽ ra kết luận sai).
3. **Đo hai cách độc lập**: đọc tên biểu tượng + màu thật trình duyệt đang vẽ, **và** mở ảnh chụp ra nhìn bằng mắt — để loại khả năng "tên biểu tượng đã đổi nhưng mắt vẫn thấy đỏ" hoặc ngược lại.
4. **Truy đúng cái phiếu than phiền là "màu đỏ"**: quét toàn bộ danh sách tìm bất kỳ biểu tượng dấu X hoặc bất kỳ dòng nào màu đỏ — **không còn dòng nào**.
5. **Đối chiếu với các dòng khác trong cùng danh sách** (điểm mấu chốt của phiếu: dòng đề xuất trông "lạc lõng" giữa các dòng khác). Nay các dòng khác là cảnh báo hổ phách đúng nghĩa, dòng đề xuất là thông tin xanh — không còn lạc lõng.
6. **Kiểm chéo tài khoản khác cấp + kiểu thông báo khác** để thử lật lời khai "đã sửa cho mọi thông báo hệ thống" — không lật được.
7. **Kiểm thêm màn hình phiếu không nêu** ("Xem tất cả thông báo") phòng trường hợp sửa được chỗ này lại sót chỗ kia — chỗ đó không vẽ biểu tượng nào nên cũng không có biểu tượng báo lỗi.

**Kết luận: 0 GAP.** Đã dựng lại đủ tiền đề (đề xuất mới do doanh nghiệp gửi, cán bộ đúng đơn vị tiếp nhận), làm đúng thao tác của phiếu, và triệu chứng cũ (dấu X đỏ) **không tái hiện** trên bản dựng hiện tại ⇒ verdict `Pass`.
