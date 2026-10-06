# QLKCHTV_37 — Xuất Excel đánh giá phiên tư vấn nhanh (sheet `bug` row 305)

**Đợt:** re-verify trên MÔI TRƯỜNG NGHIỆM THU `https://htpldn-uat.ospgroup.vn`
**Ngày đo:** 2026-08-07
**Bản dựng:** V1.0.10 · bó mã `index-Bd1akG3f.js`
**Tài khoản:** `cbnv_tw` — Cán bộ Nghiệp vụ Trung ương
**Phiếu báo:** "Màn hình không có nút chức năng" · TKM retest 3/8: "Màn hình chưa có nút chức năng"

## Verdict: ✅ PASS → `Trạng thái dev fix` = `UAT done`

Không tái hiện: khối "Đánh giá" **đã có nút Xuất Excel** và xuất ra tệp thật, nội dung đúng đủ 6 trường.

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Bug gốc (phiếu đối tác) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ đăng nhập hệ thống | `cbnv_tw` — Cán bộ Nghiệp vụ Trung ương | Không |
| Trạng thái phiên | "Hoàn thành" | Hoàn thành (đúng nhãn trên màn + trên danh sách) | Không |
| Dữ liệu tiền đề | ≥1 bản ghi đánh giá từ doanh nghiệp | 1 đánh giá: 4 điểm + có nhận xét, gắn doanh nghiệp ABC Company | Không |
| Kênh tư vấn | (phiếu không nêu) | TV Nhanh | Không |

0 GAP → đủ điều kiện chốt verdict.

## Cách dựng tiền đề (QA tự tạo, không đụng dữ liệu đối tác)

Toàn bộ 59 phiên tư vấn nhanh đang có trên env nghiệm thu **đều chưa có đánh giá nào**, nên phải tự dựng.
Đã tạo **phiên mới riêng cho QA** thay vì sửa phiên sẵn có của đối tác:

1. Tạo phiên `TVN-20260807-0001` gắn doanh nghiệp ABC Company (MST 0989878455).
2. **Trên giao diện thật** (đúng bước 2 của phiếu): bấm **Trả lời** trên hàng → soạn nội dung → **Gửi trả lời**
   → phiên chuyển sang "Cán bộ trả lời".
3. Nạp đánh giá của doanh nghiệp (4 điểm + nhận xét) — đây là thao tác của DN, trên phần mềm không có màn
   CMS tương ứng nên dùng đường tiếp nhận đánh giá dành cho CMS. Phiên tự chuyển sang **Hoàn thành**.

> Phiên `TVN-20260807-0001` là dữ liệu QA dựng để kiểm thử, có thể xóa sau khi đối tác đọc xong kết quả.

## Kết quả đo

**Nút xuất tệp — có mặt đúng chỗ.** Khối "Đánh giá" ở màn CHI TIẾT phiên hiển thị:

- Nút **[Xuất Excel]** ở góc phải khối.
- 3 thẻ tổng hợp: Tổng đánh giá **1 lượt** · Điểm trung bình **4.0 / 5** · Phân bố điểm **4★ × 1**.
- Dòng đánh giá: Điểm 4 sao · Ngày đánh giá **07/08/2026** · Nhận xét đọc được nguyên vẹn.

Bằng chứng: [image/QLKCHTV_37-nut-xuat-excel-uat.png](../image/QLKCHTV_37-nut-xuat-excel-uat.png)

**Nút ẩn đúng lúc cần ẩn (đối chứng ngược):** trước khi có đánh giá, mở đúng màn chi tiết của chính phiên này
(khi đang ở "Cán bộ trả lời") thì **không có khối Đánh giá và không có nút Xuất Excel**. Sau khi có đánh giá và
phiên sang Hoàn thành thì nút mới hiện → khớp `srs-fr-13-tv-nhanh.md:582` "Nut CHI hien thi khi phien o
HOAN_THANH va da co it nhat 1 danh gia".

**Bấm nút thật → nhận được tệp Excel hợp lệ:**

- Kiểu tệp: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, 6.955 byte.
- Tên tệp trình duyệt dùng khi tải về: **`DanhGiaTvNhanh_TVN202608070001_20260807_1907.xlsx`**
  (máy chủ đặt trùng khít: `content-disposition: attachment; filename="DanhGiaTvNhanh_TVN202608070001_20260807_1908.xlsx"`).

**Mở tệp ra đọc nội dung** (giải nén và đọc bảng tính, không chỉ kiểm tệp tạo được):

| Dòng | Nội dung đọc được |
|---|---|
| 1 | `ĐÁNH GIÁ PHIÊN TƯ VẤN NHANH` (tiêu đề) |
| 2 | `Mã phiên` · `Điểm đánh giá` · `Nhận xét của doanh nghiệp` · `Ngày đánh giá` · `Tên doanh nghiệp` · `Mã doanh nghiệp` |
| 3 | `TVN-20260807-0001` · `4` · `Noi dung tra loi ro rang, huu ich cho doanh nghiep.` · `07/08/2026` · `ABC Company` · `0989878455` |

→ **Đủ cả 6 trường phiếu yêu cầu**, từng ô khớp đúng đánh giá đang hiển thị trên màn.

## Đối chiếu SRS

| SRS yêu cầu | Dẫn nguồn | Thực tế |
|---|---|---|
| Khối Đánh giá có [Xuất Excel]; tập cột: mã phiên, điểm đánh giá, nhận xét của DN, ngày đánh giá, tên doanh nghiệp, mã doanh nghiệp | `srs-fr-13-tv-nhanh.md:582` | **Khớp đủ 6 cột** |
| Nút chỉ hiện khi phiên HOAN_THANH và đã có ≥1 đánh giá | `srs-fr-13-tv-nhanh.md:582` `[BA-03 tuần 4]` | Khớp (đã đo cả 2 chiều) |
| Thẻ tổng hợp: Tổng đánh giá (COUNT) / Điểm TB (AVG) / Phân bố | `srs-fr-13-tv-nhanh.md:582` | Khớp — 1 lượt / 4.0 / 4★×1 |
| Tên tệp `DanhGiaTvNhanh_{ma_phien}_{YYYYMMDD_HHmm}.xlsx` theo Phụ lục E §H8 | `srs-fr-13-tv-nhanh.md:582` · `srs-v3.5.md:6760` | **Khớp** — `DanhGiaTvNhanh_TVN202608070001_20260807_1907.xlsx` |
| `{DinhDanh}` lấy từ `ma_phien`, bỏ ký tự không phải chữ/số | `srs-v3.5.md:6760` · `srs-v3.5.md:3718` | Khớp — `TVN-20260807-0001` → `TVN202608070001` |

UC: `srs-fr-13-tv-nhanh.md:362` — **UC 158** (FR-X.2-05).

> **Về khác biệt tên tệp so với phiếu:** phiếu ghi mong đợi `danh-gia-tv-nhanh-{mã phiên}{YYYYMMDD-HHmm}.xlsx`.
> Quy ước đặt tên tệp kết xuất đã được BA chốt lại ngày 06/08/2026 (Phụ lục E §H8) theo khuôn viết liền không dấu,
> áp cho **mọi** nhóm chức năng. Tên phần mềm sinh ra đúng khuôn mới, có đủ mã phiên và giờ-phút để hai lần xuất
> trong cùng ngày không đè nhau. Đây là **khác biệt về quy ước đã chốt, không phải lỗi**.

## Ngoài phiếu này, có thấy gì bất thường không?

Không phát hiện thêm. Một lưu ý thao tác (không phải lỗi): sau khi có đánh giá, màn chi tiết đang mở sẵn vẫn
hiển thị dữ liệu cũ cho tới khi làm mới danh sách rồi mở lại — đã làm mới trước khi đo nên không ảnh hưởng kết luận.
