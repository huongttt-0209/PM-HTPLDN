# Bảng đối chiếu điều kiện — TLCTCDG_11 (re-verify vòng 2, 05/08/2026)

Loại bug: **thông điệp cảnh báo trọng số / chuẩn thang điểm ở Tab Tiêu chí khi Lưu** → phụ thuộc trạng thái đợt + dữ liệu tiêu chí ⇒ bắt buộc điền bảng, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 2*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──`, nên tiêu chí lấy từ mục **"Việc Dev (2 phần)"** trong note — (1) và (2) là điều kiện phải đạt; còn lỗi ở bất kỳ phần nào = Reopen.

| Điều kiện | Bug gốc (mục "Việc Dev" trong note) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | Tài khoản nghiệp vụ mở được đợt đánh giá | `cbnv_tw` · CB_NV_TW · Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Đánh giá hiệu quả → Chi tiết đợt đánh giá → Tab Tiêu chí | Đánh giá hiệu quả → Kế hoạch đánh giá → chi tiết **DG-20260730-0002** → Tab **Tiêu chí** | Không |
| Trạng thái đợt | Đợt đang ở trạng thái "Lập kế hoạch" | Đợt **DG-20260730-0002** đang ở **Lập kế hoạch** (bước 1/9 trên thanh tiến trình) | Không |
| Tiền đề dữ liệu — tổng trọng số ≠ 100% | Cần đợt có tổng trọng số khác 100% để cảnh báo hiện ra | 2 tiêu chí: trọng số 45 + 30 = **75%** (≠ 100) — có sẵn, không phải tạo thêm | Không |
| Tiền đề dữ liệu — chuẩn thang điểm ≠ 100 | Cần tổng (điểm tối đa × trọng số ÷ 100) khác 100 | (10×45 + 10×30) ÷ 100 = **7,50** (≠ 100) | Không |
| Thao tác sinh ra lỗi cũ | Nhập thông tin hợp lệ rồi nhấn "Lưu" | Sửa ô Mô tả của tiêu chí 1 → nút **Lưu** bật lên → bấm **Lưu** thật (chạy tới bước sinh ra lỗi, không chấm bằng quan sát tĩnh) | Không |
| Cách bắt thông điệp tự tắt | Đọc thông điệp hệ thống hiện ra sau khi Lưu | Cài bộ theo dõi thay đổi trên trang TRƯỚC khi bấm (không lọc trùng) + hẹn giờ bấm rồi mới chụp màn hình để bắt được thông điệp tự tắt | Không |
| Kiểm "không chặn lưu" | Giữ nguyên việc cho phép lưu — không chặn lưu | Theo dõi mạng: yêu cầu lưu tiêu chí trả về **200** (3 lần lưu, cả 3 đều 200); nội dung sửa được ghi nhận lại trên màn | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng màn hình, đúng trạng thái đợt, đủ tiền đề dữ liệu cho cả hai loại cảnh báo, và đã bấm Lưu thật.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6)

### Phần (1) — dải cảnh báo tổng trọng số

- ✅ **Dải cảnh báo có mặt ở Tab Tiêu chí khi tổng trọng số khác 100%** → hiện dải màu vàng: **"Tổng trọng số hiện tại: 75%. Cần đảm bảo = 100% trước khi trình phê duyệt"**.
- ✅ **Nội dung nêu đúng tổng hiện tại và mốc phải đạt** → con số 75% khớp đúng tổng trọng số thực (45 + 30); mốc 100% và thời điểm "trước khi trình phê duyệt" đều được nêu.
- ✅ **Đúng thông điệp mà phiếu yêu cầu** → khi bấm **Lưu**, hệ thống hiện đồng thời hai thông điệp nổi: "Đã lưu tiêu chí đánh giá" và **"Tổng trọng số hiện tại: 75%. Cần đảm bảo = 100% trước khi trình phê duyệt"** — đúng câu chữ Kết quả mong đợi của phiếu. Lần đo trước chỉ có thông báo thành công, nay đã kèm thông điệp trọng số.
- ✅ **Giữ nguyên nhãn tổng xanh/đỏ** → phía trên bảng vẫn còn "Tổng trọng số: **75%** (Tổng trọng số phải bằng 100%)" in đỏ.
- ✅ **Không chặn lưu** → bấm Lưu vẫn lưu thành công, yêu cầu lưu trả về 200, không có thông báo lỗi chặn nào.
  Ảnh: [`../image/TLCTCDG_11-luu-thanh-cong-kem-thong-diep-trong-so.png`](../image/TLCTCDG_11-luu-thanh-cong-kem-thong-diep-trong-so.png)

### Phần (2) — dải cảnh báo chuẩn thang điểm

- ✅ **Dải cảnh báo có mặt khi tổng (điểm tối đa × trọng số ÷ 100) khác 100** → hiện dải thứ hai: **"Tổng điểm tối đa có trọng số hiện tại: 7.50. Cần đảm bảo = 100 trước khi trình phê duyệt"**.
- ✅ **Nội dung nêu đúng tổng hiện tại** → 7,50 khớp phép tính (10×45 + 10×30) ÷ 100 = 7,50.
- ✅ **Ràng buộc chuẩn thang điểm KHÔNG áp vào thao tác Lưu ở Tab Tiêu chí** → tuy tổng đang là 7,50 (khác 100), thao tác Lưu vẫn thành công, không bị chặn.
  Ảnh: [`../image/TLCTCDG_11-hai-dai-canh-bao-trong-so-va-thang-diem.png`](../image/TLCTCDG_11-hai-dai-canh-bao-trong-so-va-thang-diem.png)

### Kết luận

Cả hai phần việc Dev nêu trong note đều đã có trên bản đang chạy, nội dung đúng số liệu thực, và đúng chủ trương "cảnh báo chứ không chặn lưu". Thông điệp mà phiếu gốc yêu cầu đã xuất hiện đúng lúc bấm Lưu. Không còn phần nào lỗi → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Nút **Lưu** ở Tab Tiêu chí chỉ bật lên khi có thay đổi chưa lưu; lúc mới mở màn thì mờ. Đây là cách làm bình thường, không phải "chặn lưu" — cần biết để không kết luận nhầm.
- Hai dải cảnh báo vẫn hiển thị khi chuyển sang Tab Phân công của cùng đợt. Không sai nghiệp vụ (vẫn là cảnh báo của đợt đó), chỉ ghi lại để biết.
