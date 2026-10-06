# QLHSDNHTCP_03 (dòng 72) — Chi trả chi phí · Cột dữ liệu trong bảng kết quả

**Verdict logic: Reopen + Cần BA** → ô "Trạng thái dev fix" = `Reopen, BA confirm`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:42–10:58 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (đo lại lúc 10:41, không đổi so với đầu phiên) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `cbnv_tw` (CB_NV_TW / TW) — khớp ảnh vòng 1 · `cbpd_tw_01` (CB_PD_TW / TW) — thế cho `cbpd_bn` |
| Màn | `/chi-tra/danh-sach?tab=TAT_CA&page=1`, không nhập từ khoá, không bật bộ lọc |
| Khung nhìn | 1440 × 736 (hẹp hơn khung đối tác ⇒ phép đo ngặt hơn) |
| Chuẩn đã khoá | [`../chuan/chuan-QLHSDNHTCP_03.md`](../chuan/chuan-QLHSDNHTCP_03.md) |

## Kết quả từng vế

| Vế | Nội dung | Nguồn | Kết quả |
|---|---|---|---|
| **C1c** | Ô cột SLA có nhãn mức rời + số ngày | `srs-fr-06-chi-tra.md:1058` · `:1514-1523` | ✅ **ĐẠT** |
| **C2b** | SLA không đè `Ngày nộp`; ngày đọc đủ `dd/mm/yyyy` | `:1059` điều kiện `Luôn` | ✅ **ĐẠT** |
| **C3** | Nhãn tiếng Việt, không lộ mã kỹ thuật | `srs-v3.5.md:518` · `:4703` | ✅ **ĐẠT** |
| **C4b** | Mặc định 20 bản ghi/trang | `:1061` · `srs-v3.5.md:861` | ✅ **ĐẠT** |
| **C4a** | Mặc định sắp xếp **ngày cập nhật** mới nhất trước | `:1081` | ❌ **KHÔNG ĐẠT** |
| **C5** | Nhãn thứ 5 `Đã hoàn thành` ngoài BR-SLA-02 | SRS im lặng — **GAP** | ⚠️ **treo BA** |

## Hai vế đối tác nêu — đã hết lỗi

### Vế vòng 1 (`L72`) — cột SLA thiếu nhãn mức: ĐÃ SỬA

Ảnh vòng 1 chỉ có đếm ngày trần (`Quá hạn 58 ngày LV`…). Nay mọi hồ sơ đang xử lý đều hiện **nhãn mức
kèm số ngày**: `Bình thường · còn 9 ngày LV` · `Sắp hết hạn · còn 5 ngày LV` · `Quá hạn · 7 ngày LV` ·
`Quá hạn nghiêm trọng · 54 ngày LV`. Đủ **4/4 mức** BR-SLA-02 trong cùng một lần đo.

### Vế vòng 2 (`T72`) — SLA tràn/đè `Ngày nộp`: ĐÃ SỬA

**28 lượt đo dòng** (14 dòng × 2 vai trò), đo ở vị trí đã **cuộn hết sang phải** để cột `SLA` và cột
`Ngày nộp` cùng nằm trong tầm nhìn:

| Số đo | Ngưỡng đạt | `cbnv_tw` | `cbpd_tw_01` |
|---|---|---|---|
| `maxOverlapPx` — chồng lấn ngang lớn nhất | = 0 | **0** | **0** |
| `soDongTran` — số dòng có chồng lấn | = 0 | **0** | **0** |
| `soDongNgayBiChe` — Ngày nộp bị che / thiếu ký tự | = 0 | **0** | **0** |
| `soDongThieuNhan` — dòng thiếu nhãn mức | = 0 | **0** | **0** |
| `soDongBiCat` — nội dung bị cắt ngầm | = 0 | **0** | **0** |

`spillRight` âm ở cả 14 dòng (−8 px với nhãn dài, −40 px với `Đã hoàn thành`) ⇒ nội dung nằm **trọn
trong ô của nó**. Thẻ nhãn dài nhất `Quá hạn nghiêm trọng · 54 ngày LV` **xuống dòng trong ô** thay vì
kéo dài sang cột bên — đó là cách sửa. Giá trị `Ngày nộp` đọc đủ 10 ký tự ở **14/14** dòng.

Ảnh: [`../image/QLHSDNHTCP_03-cbnv_tw-2026-08-07-SLA-va-Ngay-nop-khong-de.png`](../image/QLHSDNHTCP_03-cbnv_tw-2026-08-07-SLA-va-Ngay-nop-khong-de.png) ·
[`../image/QLHSDNHTCP_03-cbpd_tw_01-2026-08-07-SLA-va-Ngay-nop-khong-de.png`](../image/QLHSDNHTCP_03-cbpd_tw_01-2026-08-07-SLA-va-Ngay-nop-khong-de.png)

> ⚠️ **Bẫy đã tránh:** ở vị trí cuộn mặc định, phép chạm điểm giữa ô `Ngày nộp` trả `dateCovered = true`
> cho **cả 14 dòng**. Kiểm bằng `elementsFromPoint` thì thấy nguyên nhân là ô nằm **ngoài vùng cuộn
> ngang** (`x` 1360–1470 so với khung 1440), **không có phần tử nào phủ lên**. Sau khi cuộn phải và cuộn
> từng dòng vào giữa màn thì cả 14 dòng đều `dateCovered = false`. Nếu đọc số đo ở vị trí cuộn mặc định
> sẽ ra kết luận Reopen sai hoàn toàn.

## Vế KHÔNG đạt — C4a, thứ tự sắp xếp mặc định

Ô "Kết quả mong đợi" (`K72`) ghi nguyên văn:

> *"Mặc định: hệ thống sắp xếp theo **ngày cập nhật mới nhất trước**, 20 bản ghi mỗi trang."*

`srs-fr-06-chi-tra.md:1081` (SCR-V.II-01 §Quy tắc tương tác) ghi cùng nội dung:

> *"- Sắp xếp mặc định: ngày cập nhật DESC"*

**Đo được:** yêu cầu mà chính giao diện gửi là
`GET /api/v1/ho-so-chi-tras?tab=TAT_CA&page=1&pageSize=20` (reqid 421), thứ tự trả về **trùng khít**
thứ tự hiển thị. Kiểm bằng máy trên 3 mốc thời gian:

| Sắp theo | Đúng DESC? |
|---|---|
| `ngayCapNhat` (điều SRS đòi) | ❌ **false** |
| `ngayTao` | ✅ true |
| `ngayNop` | ❌ false |

⇒ Danh sách đang sắp theo **ngày tạo** giảm dần, không phải ngày cập nhật.

**Hệ quả cụ thể:** hồ sơ `CT-SEED-102` cập nhật lúc `2026-08-07T00:00:00Z` — **mới nhất trong 14 hồ
sơ**, cập nhật ngay hôm đo — nằm ở **dòng 11**. Trong khi `CT-QAW7-CLOSED` (cập nhật `25/07`) đứng dòng
3 và `CT-SEED-107` (cập nhật `20/07`, cũ nhất) đứng dòng 8. Người dùng mở màn không thấy được hồ sơ vừa
có biến động, đúng điều `K72` muốn tránh.

Giống nhau ở **cả hai vai trò** ⇒ không phải chuyện riêng của một cấp đơn vị.

## Vế treo BA — C5, nhãn thứ 5 `Đã hoàn thành`

4 hồ sơ đã kết thúc hiện nhãn `Đã hoàn thành` ở cột SLA: `CT-QAW7-CLOSED` (Đã thanh toán) ·
`CT-SEED-108` (Đã thanh toán) · `CT-SEED-109` (Từ chối) · `CT-SEED-110` (Hủy).

**Đối chiếu chéo với máy chủ:** `GET /api/v1/ho-so-chi-tras` trả `mucDoCanhBao` của **cả 4** hồ sơ này là
`BINH_THUONG`, không phải một mức thứ 5. Tức nhãn `Đã hoàn thành` do giao diện tự sinh theo trạng thái
hồ sơ, không phải giá trị máy chủ trả về. Ghi cả hai mặt vì UI và máy chủ lệch nhau.

`srs-fr-06-chi-tra.md:1058` chỉ liệt kê **4 mức**; `:1523` nói *"không thỏa điều kiện nào thì hiển thị
Bình thường"* — **SRS im lặng** về việc cột SLA hiển thị gì khi hồ sơ đã kết thúc. Câu hỏi đã gửi BA
(`../ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md:82`, Mục 15) và **chưa có phản hồi** — file
`phan-hoi-ba-7-diem-can-chot-2026-08-06.md` chỉ trả lời 7 điểm khác. Theo chuẩn đã khoá §4.1, điểm này
**không được dùng để chấm Fail và cũng không được chấm Pass sạch**.

## Không dùng để chấm (đúng chuẩn đã khoá §4.4)

- Tiêu đề cột là **`SLA`** chứ không phải `Mức cảnh báo thời hạn` — BA đã chốt 24/07/2026 rằng tên `SLA`
  khớp đặc tả (`:1058`, thành phần #16). Kỳ vọng của đối tác về tên cột đã bị BA bác từ trước.
- Bề rộng cột không đúng `80px` — `(80px)` ở `:1058` là gợi ý thiết kế, SRS không ràng buộc bề rộng render.
- Cột `Mức HT %` có trên app nhưng không nằm trong 19 thành phần `:1043-1061`; ô tiêu đề cột `Tên DN`
  trên ảnh đối tác để trống (lượt đo hôm nay **có** chữ `Tên DN`). Cả hai ngoài phạm vi 2 vế đối tác.

## Tiền đề đã kiểm trước khi đo

| Hạng mục | Yêu cầu | Thực tế |
|---|---|---|
| Số dòng | ≥ 1 | **14** |
| Mức `QUA_HAN_NGHIEM_TRONG` | bắt buộc ≥ 1 | **6 hồ sơ** (chuỗi nhãn 20 ký tự — dạng dễ tràn nhất) |
| Độ phủ mức | nên đủ 4/4 | **4/4** |
| Khung nhìn | ≤ 1440×900 | **1440×736** |
| Bản dựng | tải lại rồi ghi bó mã | `index-eWHwDgt2.js`, không đổi giữa phiên |

Không tạo / sửa / xoá bản ghi nào. Không cần seed.

## Tài khoản thay thế — khai rõ

Ảnh vòng 2 của đối tác chụp bằng vai trò `CB_PD_BN`. Tài khoản `cbpd_bn` cấp BN có **0 hồ sơ chi trả**
(đã xác minh lượt 06/08) nên không đo được; `cbpd_tw` gốc đang lỗi đăng nhập 401. Lượt này dùng
**`cbpd_tw_01`** — **giữ nguyên vai trò CB Phê duyệt**, đổi cấp sang TW. Bộ cột hiển thị của vai trò này
giống hệt vai trò CB Nghiệp vụ (10 cột), nên phép đo bề rộng vẫn so sánh được.
