# Bảng đối chiếu điều kiện — CBKQDTBD_02

> **Cập nhật 2026-08-03 20:00 — RE-TEST sau khi giao diện được triển khai lại.** Ở mode `reverify`, cột giữa là **điều kiện của bug gốc** (lần đo 17:55), cột phải là điều kiện lần re-test.
> Lỗi do QA tự phát hiện khi verify CBKQDTBD_01 (không có phản ánh đối tác) → cột giữa ghi điều kiện của **bug gốc do QA đo**, không phải điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Điều kiện của bug gốc (đo 17:55) | Mình re-test (20:00) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ đúng đơn vị khóa học (cbnv_tw, CB_NV_TW, Cục Bổ trợ tư pháp, donViId 00000000-0000-4000-8000-000000000001) | Cùng vai trò + cùng đơn vị — cbnv_tw_05 (cbnv_tw bị phiên QA khác chiếm, fallback đúng Rule 7: cùng CB_NV_TW + cùng đơn vị TW) | Không |
| Entity + trạng thái | Khóa học `AAA-KH-TW` trạng thái **Hoàn thành** (đủ tiền đề PRE-02/PRE-03 dòng 1363-1364) | **Chính khóa đó**, vẫn ở Hoàn thành | Không |
| Dữ liệu tiền đề | 4 học viên có kết quả **đã được phê duyệt**, đã công bố mốc 03/08/2026 17:55 | Đúng 4 học viên đó, vẫn "Đã công bố" mốc 17:55 — dữ liệu không đổi giữa 2 lần đo | Không |
| Dữ liệu tiền đề — **khóa đã gán đề kiểm tra** (điểm chưa loại trừ được ở lần đo trước) | Khóa **chưa** gán đề → chưa loại trừ "cột Đề kiểm tra render có điều kiện" | Đã tạo đề `QA-DEKT-0803` (Kích hoạt) và **gán vào chính `AAA-KH-TW`** lúc 20:04; đo cả **trước** và **sau** khi gán | Không |
| Input / filter | Không có bộ lọc — chỉ mở tab và đọc tiêu đề cột | Như vậy; thêm thao tác cuộn ngang hết cỡ | Không |

**Kết luận: 0 GAP.** Mọi điều kiện vai trò / trạng thái / dữ liệu / input của bug gốc đều được dựng lại đúng, và điều kiện còn treo duy nhất của bug gốc (khóa chưa gán đề) đã được đóng bằng **test thật** — tạo đề rồi gán vào chính khóa đó, đo cả trước lẫn sau.

### Biến số đã đổi CÓ CHỦ ĐÍCH — đây là bản chất của re-verify, không phải GAP

`--mode reverify` là đo lại **trên bản dựng mới**, nên khác biệt bản dựng là thứ đang được kiểm chứ không phải điều kiện bị lệch. Khai rõ để đối soát:

- Gói giao diện lúc đo bug gốc (17:55): `index-bJhJGCw4.js`
- Gói giao diện lúc re-test (20:00): `index-RAuQ-eDH.js` — máy chủ ghi `Last-Modified: Mon, 03 Aug 2026 12:51:29 GMT` (19:51 giờ VN)
- Cả 2 lần đo đều **tải lại trang bỏ bộ nhớ đệm** (`ignoreCache`) ngay trước khi đọc cột

⇒ Đúng định nghĩa "dev đã sửa, QA test lại chạy đúng ⇒ `Pass`", **không phải** "không tái hiện được mà không giải thích nổi" (nên KHÔNG dùng `Resolved`).

**Đo bằng 2 phương pháp độc lập (re-test 20:00):**
1. DOM: tiêu đề cột → **12 phần tử** `["", "STT", "Họ tên", "Email", "Số điện thoại", "Đơn vị", "Đề kiểm tra", "Điểm", "Kết quả", "Trạng thái công bố", "Thời điểm công bố", "Hành động"]`; số `<colgroup><col>` = 12; không cột nào ẩn (`display:none` / `offsetWidth === 0`).
2. Ảnh full-res `../bug-reports/dao-tao/image/CBKQDTBD_02-retest-01-tab8-AAA-KH-TW-CHUA-gan-de-du-12-cot.png` — đọc bằng mắt thấy rõ Email / Số điện thoại / Đơn vị / Đề kiểm tra / Điểm.

**Đối chứng bug gốc CÓ THẬT (không phải đo sai):** ảnh `../image/CBKQDTBD_01-F-sau-congbo-thanhcong.png` chụp 17:55 trên **cùng khóa học** chỉ có 7 cột.

**Làm rõ điểm còn treo của bug gốc:** cột "Đề kiểm tra" **hiển thị vô điều kiện** — khóa chưa gán đề thì ô hiện `—`; sau khi gán đề + nhập điểm (khóa `KH-QAW7-HOINGHI`) thì ô hiện đúng tên đề `QA-DEKT-0803 — Đề kiểm tra pháp lý DN (QA seed 03/08)`. Không có chuyện "chỉ hiện khi có đề".
