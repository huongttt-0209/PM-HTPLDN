# Quan sát real-data — NHSYC_08 (Hủy khi đã nhập dữ liệu)

## Tự chạy lại đúng tiền đề

1. Mở form Nhập thủ công `/vu-viec/tao-moi` (vai trò `cbnv_tw`).
2. **Nhập dữ liệu thật**: chọn doanh nghiệp (Công ty TNHH Seed Publishable) + Tiêu đề + Nội dung yêu cầu.
3. Bấm **"Hủy"** — có cài `MutationObserver` trên `document.body` **TRƯỚC** khi bấm để bắt mọi node mới (modal/toast).

**Kết quả:**

```json
{
  "urlSauKhiHuy": "http://18.143.165.120/vu-viec/danh-sach",
  "daRoiForm": true,
  "soDialogXuatHien": 0,
  "nodeChua_chac-chan_xac-nhan_O-lai": []
}
```

⇒ Bấm "Hủy" → **chuyển thẳng về danh sách**, **không hiện hộp thoại xác nhận nào**, dữ liệu đã nhập mất luôn. **Tái hiện đúng** phản ánh của đối tác ("Hệ thống không hiển thị xác nhận").

Ảnh: `web-01-truoc-khi-bam-huy-da-nhap-du-lieu.png` → `web-02-sau-khi-bam-huy-ve-thang-danh-sach-khong-hoi-xac-nhan.png`.

## Đối chiếu SRS — SRS IM LẶNG

| Nguồn đã tra | Kết quả |
|---|---|
| SCR-V.I-02 row 34 (`srs-fr-05` dòng 1695) | Chỉ ghi thanh hành động `[Hủy] [Lưu nháp] [Lưu & Gửi duyệt]` — **không quy định** hộp thoại xác nhận cho nút Hủy |
| §E "Thông báo người dùng (toast/confirm/error chung)" (`srs-fr-05` dòng 1571-1580) | Có confirm cho **"Xóa hồ sơ"** và **"Xóa hàng loạt"** — **KHÔNG có** confirm cho "hủy form khi có dữ liệu chưa lưu" |
| `srs-v3.5.md` (grep "chưa lưu / rời trang / thoát form / hộp thoại xác nhận / Ở lại") | **Không có quy ước toàn cục** nào về xác nhận khi rời form còn dữ liệu chưa lưu |
| `srs-fr-04` §3.0b "Bảng mẫu hộp thoại xác nhận" (dòng 1390-1404) | Là bảng mẫu **chỉ áp dụng "trong section này"** (module Tư vấn viên) và chỉ liệt kê modal cho **hành động nghiệp vụ** (Trình duyệt, Phê duyệt, Từ chối, Công khai, Xóa…). **Không có** modal "hủy form chưa lưu" |
| Thiết kế nội bộ (prototype `pages/vu-viec/form.tsx`) | `<Button onClick={() => navigate('/vu-viec/danh-sach')}>Hủy</Button>` — **cũng không có hộp thoại xác nhận** |

⇒ **SRS im lặng** về yêu cầu hỏi xác nhận khi bấm Hủy. Web đang làm **giống thiết kế nội bộ**.

## Bối cảnh đáng lưu ý cho BA: KHÔNG NHẤT QUÁN GIỮA CÁC MODULE

- Module **Tư vấn viên** (`srs-fr-04`): form CÓ hộp thoại xác nhận khi bấm Hủy (nút "Ở lại") — xem `BUG-QLTVV_22`, `BUG-DKTGMLTVV_14`, `BUG-CNTTTVV_07` tuần này (các bug đó là về việc dữ liệu bị xóa **dù đã chọn "Ở lại"**, tức là hộp thoại có tồn tại).
- Module **Vụ việc** (`srs-fr-05`): form **KHÔNG có** hộp thoại xác nhận nào.

⇒ Cùng một sản phẩm nhưng 2 module hành xử khác nhau ở cùng một thao tác "Hủy form đang nhập dở". Đây là điểm BA nên chuẩn hóa.

## Verdict

**BA confirm.** Đối tác **quan sát đúng thực tế** (đã tái hiện: không có hộp thoại xác nhận), nhưng **SRS không quy định** phải có hộp thoại này → tranh chấp nằm ở **đặc tả**, không phải lỗi dev. Theo quy tắc: evidence đúng actual, chỉ tranh chấp expected/spec → `BA confirm`, QA **không tự Reject**.
