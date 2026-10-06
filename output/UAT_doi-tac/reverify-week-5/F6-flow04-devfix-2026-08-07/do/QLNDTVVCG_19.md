# Hồ sơ đo — QLNDTVVCG_19 (dòng 285) · FLOW 04 Giai đoạn B

> Chuẩn chấm đã khóa TRƯỚC khi mở màn: [`../chuan/QLNDTVVCG_19.md`](../chuan/QLNDTVVCG_19.md).
> **Không đổi quan hệ `MATCH/DIFF/GAP` của bất kỳ vế nào sau khi đo** (luật khóa 5) — 5/5 vế vào đo là `MATCH · TEST`,
> giữ nguyên như vậy.

## 1. Verdict

| | |
|---|---|
| **Verdict** | ✅ **Pass** |
| **Ô "Trạng thái dev fix"** | `Test done` |
| **Cơ sở** | 5/5 vế `MATCH` đều đạt; hai đường đo (giao diện + phản hồi máy chủ) khớp từng trường |
| **Vế `DIFF`/`GAP`** | Không có — case này không phát sinh câu hỏi BA |

---

## 2. Hoàn cảnh đo

| | |
|---|---|
| **Môi trường** | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu đối tác |
| **Bó mã FE** | **`index-D4Buvu4S.js`** (`last-modified` `06 Aug 2026 19:23:01 GMT` = 07/08 02:23 giờ VN, etag `W/"6a74df15-428"`). Env vừa deploy lần thứ 5 ngay trước case này ⇒ **đã tải lại trang bằng địa chỉ** rồi mới đo. Xem [`../BAN-DUNG.md`](../BAN-DUNG.md) |
| **Chuỗi chân sidebar** | `HTPLDN · V1.0.9` — **không dùng làm vân tay** (đứng yên qua 3 lần deploy) |
| **Tài khoản** | `cbnv_tw_04` / `Test@1234` — `GET /api/v1/auth/me` trả `vaiTro: ["CB_NV_TW"]`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`. **Không dùng `admin`** (bẫy PASS oan 6.2.6) |
| **Thời điểm** | 07/08/2026 **02:26 – 02:31** giờ VN |
| **Bản ghi đo** | `TVCS-QLND19-UAT` — id `19191919-0000-4000-8000-000000000019`, tiêu đề *"QLNDTVVCG_19 - Dữ liệu đánh giá chất lượng"*, trạng thái **Đã duyệt** (`DA_DUYET`), đơn vị `00000000-…-0001` = đúng đơn vị tài khoản đo |
| **Dữ liệu đã thay đổi** | **KHÔNG.** Toàn bộ phép đo là thao tác đọc (mở danh sách → mở chi tiết → mở khối). Không tạo, không sửa, không xóa bản ghi nào |

### 2.1 🔴 Tiền đề đã có sẵn — không phải do bên kiểm thử dựng

Chuẩn chấm §4.4 đã cảnh báo đây là nút thắt: bản ghi đánh giá **chỉ vào phần mềm qua API inbound Cổng PLQG**
(`srs-fr-12:1006`, `:1017`), đường dẫn **SRS chưa chốt** (`:1013` `[CẦN BA CHỐT — BA-22 tuần 4]`), lại thêm
xác thực mTLS (`:1015`) — nên kịch bản xấu là phải kết luận `Chưa chốt`.

Thực tế **không rơi vào kịch bản đó**: env đã sẵn một bản ghi TVCS được dựng riêng cho case này
(mã `TVCS-QLND19-UAT`, id có khuôn `19191919-…`, tiêu đề ghi thẳng `QLNDTVVCG_19`) kèm **2 bản ghi đánh giá**
(`ngayTao` lùi về 16/07/2026, `ngayCapNhat` **05/08/2026**). ⇒ Đúng cái mà ô TKM *"chưa có dữ liệu test"* nói
là còn thiếu, nay đã có. **Không cần seed, không cần gọi API inbound.**

---

## 3. Kết quả từng vế

| Vế | Nội dung | Đo được | Kết luận |
|---|---|---|---|
| **C1** | Màn chi tiết TVCS có khối *"Đánh giá chất lượng"* | Có. Dãy khối trên màn: `Thông tin cơ bản` → `Nội dung tư vấn` → `Tư liệu pháp lý liên kết` → **`Đánh giá chất lượng`** → `Nhật ký thao tác` → `Công khai chuyên trang` | ✅ Đạt |
| **C2** | Khối là **bảng liệt kê** các đánh giá của DN, mỗi đánh giá 1 dòng | Bảng có **2 dòng**, đúng bằng số bản ghi đánh giá của hồ sơ (phản hồi máy chủ `total: 2`) | ✅ Đạt |
| **C3** | Đủ 4 cột: Mã đánh giá · Điểm (thang 1-5) · Nhận xét của DN · Ngày đánh giá | Hàng tiêu đề đọc được: `Mã đánh giá` · `Điểm` · `Nhận xét của doanh nghiệp` · `Ngày đánh giá`. Cột Điểm hiện dạng `4.0 / 5`, `5.0 / 5` → đúng thang 1-5 | ✅ Đạt |
| **C4** | Có dòng tổng hợp: điểm trung bình + số lượng đánh giá | `Điểm trung bình: 4.5 / 5` · `Số lượng đánh giá: 2`. **Tự tính lại** từ chính 2 dòng đang hiển thị: (4.0 + 5.0) / 2 = **4.5** ✔ và đếm dòng = **2** ✔ | ✅ Đạt |
| **C5** | Toàn bộ dữ liệu của khối là chỉ đọc | **Đếm được 0** phần tử tương tác ghi bên trong khối (đã quét `input`, `textarea`, `select`, `button`, `[contenteditable]`, `[role=switch]`, `[role=checkbox]`, `.ant-upload`, `.ant-picker`, `.ant-select`, và cả thẻ `a`). Khớp ma trận quyền `srs-v3.5.md:1368` — không vai trò CMS nào có Create/Update/Delete trên thực thể này | ✅ Đạt |

### 3.1 Số liệu thô đọc từ giao diện

```
Đánh giá chất lượng
Mã đánh giá          | Điểm    | Nhận xét của doanh nghiệp          | Ngày đánh giá
UAT-QLND19-DG-02     | 4.0 / 5 | Kết quả hữu ích cho doanh nghiệp.  | 16/07/2026 10:05
UAT-QLND19-DG-01     | 5.0 / 5 | Tư vấn rõ ràng, đầy đủ.            | 16/07/2026 10:00
Điểm trung bình: 4.5 / 5     Số lượng đánh giá: 2
```

**Ảnh:** [`../image/QLNDTVVCG_19-khoi-danh-gia-chat-luong-TVCS-QLND19-UAT.png`](../image/QLNDTVVCG_19-khoi-danh-gia-chat-luong-TVCS-QLND19-UAT.png)
— bắt trọn tên khối + hàng tiêu đề + 2 dòng + dòng tổng hợp trong cùng một khung hình. Đã mở lại ảnh xác nhận đọc được.

---

## 4. Đối chứng độc lập — đúng MỘT đường (luật khóa 3)

**Đường đo 1 (giao diện):** đăng nhập sẵn → menu **Tư vấn → Tư vấn chuyên sâu** (breadcrumb `Trang chủ / Tư vấn
chuyên sâu / Chi tiết`, khớp `srs-fr-12:1116`) → thẻ **Hoàn thành** → nút **xem chi tiết** (biểu tượng con mắt)
tại dòng `TVCS-QLND19-UAT` → mở khối *Đánh giá chất lượng* → đọc bảng.

**Đường đo 2 (đối chứng):** đọc lại **phản hồi máy chủ của chính lời gọi mà màn vừa phát** — không tự đoán đường dẫn,
đường dẫn lấy từ danh sách lời gọi mạng của trang:

```
GET /api/v1/danh-gia-chat-luong-tvs?noiDungTvId=19191919-0000-4000-8000-000000000019&page=1&pageSize=100  → 200
```

| Trường trong phản hồi | Bản ghi 1 | Bản ghi 2 | Trên màn |
|---|---|---|---|
| `maDanhGiaCong` | `UAT-QLND19-DG-02` | `UAT-QLND19-DG-01` | khớp |
| `diem` | `4` | `5` | `4.0 / 5` · `5.0 / 5` — khớp |
| `nhanXet` | `Kết quả hữu ích cho doanh nghiệp.` | `Tư vấn rõ ràng, đầy đủ.` | khớp nguyên văn |
| `ngayDanhGia` | `2026-07-16T03:05:00.000Z` | `2026-07-16T03:00:00.000Z` | `16/07/2026 10:05` · `16/07/2026 10:00` — khớp (giờ VN = UTC+7) |
| `loaiDanhGia` | `DN` | `DN` | đúng *"do doanh nghiệp gửi"* của phiếu |
| `meta.total` | `2` | | `Số lượng đánh giá: 2` — khớp |
| trung bình tự tính | (4 + 5) / 2 = **4.5** | | `Điểm trung bình: 4.5 / 5` — khớp |

**Hai đường không mâu thuẫn** ⇒ đủ điều kiện chốt verdict.

**Không thử thao tác ghi** để "chứng minh chỉ đọc" — chuẩn chấm §5 cấm (SRS không đặc tả endpoint ghi nào cho
thực thể này, và đó là thao tác đổi môi trường ngoài vế `Cn`). C5 chấm bằng đếm phần tử + ma trận quyền.

---

## 5. Đã chủ động tránh các bẫy nào

### 5.1 Bẫy FAIL oan

- **Chấm theo số thứ tự "Nhóm 4"** (§6.1.2): đã chấm theo **tên khối**. Ghi nhận thêm cho người đọc phiếu:
  trên màn có 6 khối và *"Đánh giá chất lượng"* **đúng là khối thứ 4** — trùng với chữ "Nhóm 4" của phiếu,
  nhưng đó là trùng hợp, không phải căn cứ chấm.
- **Nhãn cột lệch chữ** (§6.1.3): `:1172` viết `Nhận xét DN` / `Ngày`, màn viết `Nhận xét của doanh nghiệp` /
  `Ngày đánh giá`. Cùng khái niệm → không Fail.
- **Cách vẽ điểm** (§6.1.4): `:1172` ghi *"Điểm (1-5 sao)"*; màn vẽ số `4.0 / 5` chứ không vẽ ngôi sao.
  `:1172` mô tả **thang điểm**, `:1488` chốt `CHECK BETWEEN 1 AND 5` → không Fail vì biểu tượng.
- **Vị trí dòng tổng hợp** (§6.1.5): SRS im lặng; màn đặt ngay dưới bảng — không chấm theo vị trí.
- **Cột "Mã đánh giá" hiện mã Cổng** (§6.1.6): màn hiện `maDanhGiaCong` (`UAT-QLND19-DG-0x`, `:1487`) chứ không
  phải `ma_danh_gia` "mã trong PM" (`:1063`). `:1172` **không chỉ định** dùng mã nào → không Fail.
- **Phân trang / sắp xếp / lọc**: bảng không có (đã kiểm: không có `.ant-pagination`, 4 cột đều không sắp xếp
  được). SRS im lặng, ngoài scope → không Fail.

### 5.2 Bẫy PASS oan

- **Thấy tiêu đề khối là Pass** (§6.2.1): đã đo đủ cả 5 vế, không dừng ở C1.
- **Chấm điểm trung bình bằng mắt** (§6.2.3): đã **tự tính lại** (4+5)/2 = 4.5. Bộ dữ liệu này có tính phân
  biệt: 4.5 **khác cả hai** điểm thành phần (4 và 5) ⇒ nếu giao diện lấy nhầm điểm của một dòng thì đã lộ ra.
- **Nhầm nguồn điểm trung bình** (§6.2.4): đã kiểm — hồ sơ TVCS có trường riêng `diemDanhGiaDn` thang **0-10**
  (`srs-fr-12:1355` `CHECK BETWEEN 0 AND 10`) và trường này đang giữ giá trị **4.5**. Vì 4.5 **trùng** với
  trung bình cộng thật nên **không phân biệt được** màn lấy số từ đâu. Điều này **không đổi kết luận** C4: cả
  hai giả thiết đều cho ra đúng con số đúng thang 1-5 mà `:1172` yêu cầu, và `:1172` không quy định cách tính.
  Ghi lại như một giới hạn của lượt đo (xem §6).
- **Bản dựng cũ trong tab** (§6.2.7): đã phát hiện env deploy lần 5 lúc 02:23 và **tải lại bằng địa chỉ**
  trước khi đo; bó mã sau khi tải lại đúng là `index-D4Buvu4S.js`.
- **Dùng `admin`** (§6.2.6): không dùng.
- **Nhầm env** (§6.2.8): đo trên env nội bộ, đối tác đo trên env nghiệm thu — đã khai ở §6.

---

## 6. Giới hạn hiệu lực của verdict

1. **Chỉ có hiệu lực cho env nội bộ `18.143.165.120.nip.io` + bó mã `index-D4Buvu4S.js`.** Đối tác đo trên env
   nghiệm thu `htpldn-uat.ospgroup.vn` (bộ tài khoản khác).
2. **Không có ảnh "lỗi cũ"** do chính bên kiểm thử chụp (phiếu không khai tệp ảnh/video cho case này, repo cũng
   không có tệp `QLNDTVVCG_19.*`) ⇒ **không kết luận được "bản sửa có tác dụng"**, chỉ kết luận được **hiện
   trạng đang đúng so với đặc tả**. Ca biên Flow 04.
3. **Không phân biệt được nguồn của số "Điểm trung bình"** (§5.2) vì giá trị lưu sẵn trùng với trung bình cộng.
   Muốn chốt thì cần một hồ sơ có `diemDanhGiaDn` lệch với trung bình các dòng — nằm ngoài vế `Cn` của dòng này.
4. **Chỉ đo trên một hồ sơ** (`TVCS-QLND19-UAT`, 2 đánh giá). Cách trình bày khi khối **không có đánh giá nào**
   nằm ngoài scope (chuẩn chấm §3 — SRS im lặng về trạng thái rỗng của khối này), không đo và không chấm.

---

## 7. Lỗi mới / ứng viên lỗi phát sinh

**Không có.** Trong suốt lượt đo không gặp mã lỗi 4xx/5xx, không gặp thao tác phải đi vòng, không gặp
hiện tượng bất thường nào ngoài vế đang verify.
