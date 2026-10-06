# DGKQHTVV_01 — Re-verify sau dev fix (dòng 64, tab `bug`)

**Ngày đo:** 2026-08-07 · **Verdict:** 🔁 REOPEN
**Môi trường:** https://18.143.165.120.nip.io — ứng dụng `HTPLDN · V1.0.10`, bó mã giao diện `index-BbPPdate.js`
(đã tải lại trang và đọc lại tên bó mã ngay trong tab trước khi đo — mới hơn bản QA đo lượt trước lúc 02:04 sáng nay).
**Vai trò đo:** Doanh nghiệp `0109998887` — "Cong ty TNHH QA UAT Kiem Thu" (DN-HNI-0001, Hà Nội).
Bộ tài khoản 02 không có tài khoản Doanh nghiệp nên dùng tài khoản DN sẵn có; các vai trò cán bộ dùng
`cbnv_tw_02` (bộ 02) và `cbnv_hn` (đúng đơn vị Sở Tư pháp Hà Nội của dữ liệu).

---

## Bối cảnh lượt trước

| | |
|---|---|
| Kết quả thực tế (đối tác) | Hệ thống không hiển thị nút chức năng mặc dù bản ghi ở trạng thái phù hợp |
| QA lượt 02:04 07/08 | Reopen — DN bị đẩy sang trang báo không có quyền khi mở chi tiết vụ việc của chính mình |
| Dev sau đó | Đặt lại `Trạng thái dev fix` = `Fixed` (nhật ký ghi sheet cho thấy QA đặt `Reopen` lúc 02:04, giá trị hiện tại là của dev) |

---

## Vế ĐÃ HẾT LỖI

### 1. DN mở được chi tiết vụ việc của chính mình

Bấm mã `VV-STP-HN-20260806-002` ngay trong danh sách → vào thẳng màn chi tiết, đọc được nội dung hồ sơ.
Không còn bị đẩy sang trang báo không có quyền truy cập.

![DN mở được chi tiết](image/DGKQHTVV_01-01-dn-mo-duoc-chi-tiet.png)

### 2. Hai nhóm thông tin nội bộ đã ẩn đúng với DN

Trên màn chi tiết, DN chỉ thấy: Thông tin Doanh nghiệp · Nội dung Yêu cầu · Tài liệu · Dòng thời gian.
Không thấy "Kết quả kiểm tra" và "Phân công xử lý" — khớp `srs-fr-05-vu-viec.md:1805` (Nhóm 4 Kết quả kiểm tra —
Ẩn hoàn toàn) và `:1806` (Nhóm 5 Phân công xử lý — Ẩn hoàn toàn).

> Đính chính so với ghi chép lượt trước: hai số dòng này bị ghi đảo tên nhóm. Đúng là **:1805 = Kết quả kiểm tra**,
> **:1806 = Phân công xử lý**. Nội dung yêu cầu không đổi, chỉ sửa cách gọi tên để không quote sai.

---

## Vế CÒN LỖI — DN không tới được vụ việc đã kết thúc của chính mình

Doanh nghiệp `0109998887` **có 2 vụ việc ở trạng thái "Đã đánh giá"** thuộc đúng doanh nghiệp này:

| Mã vụ việc | Trạng thái | Chủ sở hữu (doanhNghiepId) | Đơn vị xử lý |
|---|---|---|---|
| `VV-BTP-TW-20260806-004` | Đã đánh giá | `829abcac-…-ec51bc79014c` | Bộ Tư pháp (TW) |
| `VV-BTP-TW-20260806-003` | Đã đánh giá | `829abcac-…-ec51bc79014c` | Bộ Tư pháp (TW) |

`829abcac-…` chính là mã doanh nghiệp gắn với tài khoản đang đăng nhập (đọc từ hồ sơ phiên của chính DN đó).

**Triệu chứng đo được — hỏng ở cả 2 đường vào:**

1. **Danh sách của DN không hiện 2 vụ việc này.** Tab "Tất cả" chỉ 5 kết quả (đều là vụ việc do Sở Tư pháp
   Hà Nội xử lý), tab **"Hoàn thành" không có số đếm**. Lọc thẳng theo trạng thái "Hoàn thành" và "Đã đánh giá"
   đều trả về 0.

   ![Danh sách DN thiếu 2 vụ việc](image/DGKQHTVV_01-03-danh-sach-dn-thieu-2-vu-viec-hoan-thanh.png)

2. **Mở thẳng địa chỉ vụ việc thì báo "Không tìm thấy vụ việc."** — trong khi cùng phiên đó, vụ việc do
   Sở Tư pháp Hà Nội xử lý vẫn mở bình thường.

   ![Không tìm thấy vụ việc](image/DGKQHTVV_01-02-dn-khong-tim-thay-vu-viec-cua-minh.png)

**Vì sao là lỗi:** `srs-fr-05-vu-viec.md:1793` quy định phạm vi nhìn của DN theo **quyền sở hữu** —
"DN chỉ thấy vụ việc của DN mình", và chỉ chặn khi DN mở vụ việc **không phải** của mình. Hai vụ việc trên
đúng là của DN này. `:1792` cũng đặt màn này là "hồ sơ của tôi". Hiện tại phạm vi nhìn đang bị cắt theo
**đơn vị xử lý** thay vì theo chủ sở hữu, nên vụ việc do đơn vị Trung ương xử lý bị giấu khỏi chính DN gửi.

**Hệ quả đúng bằng triệu chứng gốc của phiếu:** `:1811` cho phép nút **[Đánh giá]** khi vụ việc ở
"Hoàn thành"/"Đã đánh giá" và DN chưa đánh giá; `:1809` cho DN nhập đánh giá ngay trên màn chi tiết ở 2 trạng thái đó.
Cả 2 vụ việc đủ điều kiện (mới chỉ có điểm của cán bộ, chưa có đánh giá loại doanh nghiệp — theo `:2108` mỗi vụ việc
được 1 đánh giá của cán bộ và 1 của doanh nghiệp). Nhưng vì DN không mở được bản ghi, **không có đường nào
tới chức năng đánh giá** → đúng câu "không hiển thị nút chức năng mặc dù bản ghi ở trạng thái phù hợp".

---

## Vế CHƯA ĐO ĐƯỢC (ghi rõ để không chấm oan)

Chưa đo được nút [Đánh giá] trên một vụ việc **hiển thị được** ở trạng thái "Hoàn thành", vì trong đơn vị
Sở Tư pháp Hà Nội **không dựng nổi vụ việc lên "Hoàn thành"**: đơn vị này không có tư vấn viên đang hoạt động,
không có người hỗ trợ và không có tổ chức tư vấn nào để phân công (danh sách đều trả về 0; tư vấn viên duy nhất
của đơn vị chưa gắn tài khoản nên hệ thống báo "Đối tượng được chọn đã bị vô hiệu hóa" — `ERR-PC-02`).
Cán bộ Trung ương không phân công thay được ("Bạn không có quyền phân công vụ việc của đơn vị khác").

Điều này **không đổi verdict**: vế "còn lỗi" ở trên đã đủ để chặn toàn bộ luồng đánh giá của DN. Nhưng sau khi
dev sửa phạm vi nhìn, **phải đo lại tiếp** phần nhập điểm để chốt trọn phiếu.

---

## Phạm vi đã đo

- 1 doanh nghiệp · 7 vụ việc thuộc doanh nghiệp đó (5 hiển thị + 2 bị giấu) · 2 đường vào (bấm trong danh sách,
  mở thẳng địa chỉ) · đối chứng bằng 2 vai trò cán bộ để xác nhận 2 vụ việc kia có thật và đúng chủ sở hữu.
- Chưa mở rộng sang doanh nghiệp thứ hai vì lỗi đã tái hiện chắc chắn ở doanh nghiệp thứ nhất.

---

## ── CÁCH VERIFY sau Dev fix ──

**Phạm vi:** DN phải thấy và mở được **mọi** vụ việc của chính mình, không phụ thuộc đơn vị nào xử lý; và trên
vụ việc "Hoàn thành"/"Đã đánh giá" chưa có đánh giá của doanh nghiệp thì phải nhập được đánh giá.

**Precondition:** tài khoản doanh nghiệp (tên đăng nhập là mã số thuế) có ≥1 vụ việc do **đơn vị Trung ương**
xử lý đã ở "Hoàn thành"/"Đã đánh giá", và ≥1 vụ việc do **đơn vị địa phương** của DN xử lý ở "Hoàn thành".
Chưa có vế địa phương thì phải dựng: đơn vị đó cần trước hết có ≥1 tư vấn viên đang hoạt động **đã gắn tài khoản**
(nếu không sẽ không phân công được), rồi đi luồng chuẩn: tiếp nhận → kiểm tra hồ sơ kết luận Đạt → phân công →
cập nhật kết quả → trình phê duyệt → phê duyệt (tài khoản khác) → hoàn thành.

1. Đăng nhập bằng **chính tài khoản doanh nghiệp**. Mở danh sách vụ việc, **không nhập từ khóa, không bật bộ lọc**.
   Đếm tổng số kết quả và số đếm ở tab "Hoàn thành".
   ✅ Phải bằng đúng tổng số vụ việc mà doanh nghiệp đó sở hữu (đối chiếu bằng vai trò cán bộ Trung ương).
2. Bấm mã của vụ việc do **đơn vị Trung ương** xử lý. Phải mở được nội dung hồ sơ, không báo "Không tìm thấy vụ việc",
   không bị đẩy sang trang báo không có quyền.
3. Mở lại đúng vụ việc đó bằng cách **dán thẳng địa chỉ** vào thanh địa chỉ (không dùng lại màn cũ) — vẫn phải mở được.
4. Trên vụ việc "Hoàn thành"/"Đã đánh giá" mà doanh nghiệp chưa chấm: đếm số phần tử tương tác dẫn tới việc đánh giá
   (nhìn thấy bằng mắt trong khung nhìn). Kích hoạt, nhập 9 · 8 · 10 và một chuỗi nhận xét có mốc giờ duy nhất dạng
   `QA-DGKQ-<YYYYMMDD-HHMM>`, gửi. Cài bộ bắt thông báo **trước khi** bấm và đếm cả số lời gọi kèm theo.
5. **Tải lại trang bằng địa chỉ**, mở lại phần Đánh giá và đọc nội dung.
6. Đo bằng đường thứ hai: bằng chính phiên của doanh nghiệp, đọc lại bản ghi đánh giá của vụ việc đó từ máy chủ,
   đối chiếu từng trường với những gì màn hình hiển thị ở bước 5.
7. Chứng âm: cùng tài khoản đó, thử mở và thử đánh giá một vụ việc **của doanh nghiệp khác** → phải bị từ chối.
8. Kiểm trùng: đánh giá lần thứ hai cùng vụ việc → phải bị từ chối, đọc lại vẫn đúng 1 bộ điểm của loại doanh nghiệp,
   nhận xét cũ không bị ghi đè.

**✅ PASS khi:** số vụ việc doanh nghiệp thấy đúng bằng số vụ việc nó sở hữu (kể cả vụ việc do đơn vị khác xử lý);
mở được cả 2 đường ở bước 2–3; đếm được ≥1 phần tử dẫn tới việc đánh giá; sau khi tải lại trang đọc đúng 3 điểm đã nhập
+ đúng chuỗi nhận xét + điểm tổng bằng trung bình 3 điểm (`srs-fr-05-vu-viec.md:1220`); đường đo thứ hai trùng khít và
ghi loại người đánh giá là doanh nghiệp; chứng âm bước 7 và kiểm trùng bước 8 đều bị từ chối.

**❌ FAIL nếu:** doanh nghiệp vẫn không thấy hoặc không mở được vụ việc của chính mình ở bất kỳ đơn vị nào;
hoặc mở được nhưng không có phần tử nào để bắt đầu đánh giá; hoặc gửi được và báo thành công nhưng sau khi tải lại
trang phần đánh giá vẫn rỗng / thiếu ≥1 trong 3 điểm / nhận xét khác chuỗi đã nhập / điểm tổng khác trung bình 3 điểm;
hoặc hai đường đo lệch nhau; hoặc doanh nghiệp đánh giá được vụ việc của doanh nghiệp khác. Sửa được một vế vẫn là FAIL.

**⚠️ Đừng chấm FAIL vì:** nhãn / vị trí / kiểu hiển thị của đường vào đánh giá; nguyên văn chữ thông báo thành công;
cách làm tròn hay định dạng điểm tổng (9 vs 9.0 vs 9,0); không có chức năng sửa/xoá đánh giá đã gửi; thứ tự – màu –
bố cục trình bày lại 3 điểm; không ai nhận được thông báo sau khi đánh giá. Doanh nghiệp **không** được thấy phần
phân công xử lý và phần kết quả kiểm tra — thiếu 2 phần này là **đúng** đặc tả, không phải lỗi.

**⚠️ Đừng chấm PASS vì:** thấy nhãn trạng thái đã đổi sang "Đã đánh giá", thấy nhật ký đã có mục đánh giá, hay thấy
thông báo báo thành công — cả ba dấu hiệu này đã từng đúng trong khi lỗi còn nguyên. Cũng đừng chấm PASS vì hệ thống
nhận được lệnh đánh giá gửi thẳng, vì bản ghi đánh giá có sẵn từ bản dựng cũ, hay vì nhánh cán bộ chạy được — phải đo
lại đúng nhánh doanh nghiệp, đi từ bước 1. **Và đừng chấm PASS chỉ vì mở được vụ việc do đơn vị địa phương xử lý** —
đúng chỗ hỏng lần này là vụ việc do đơn vị Trung ương xử lý.
