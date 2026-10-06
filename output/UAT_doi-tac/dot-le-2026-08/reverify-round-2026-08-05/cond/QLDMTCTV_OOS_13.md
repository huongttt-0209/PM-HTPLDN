# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_13 (re-verify vòng 1, 05/08/2026)

Loại bug: **tên gọi giấy tờ trên nhãn trường + câu báo lỗi, và việc chặn lưu khi để trống** → điền bảng đối chiếu, 0 GAP.
Tiêu chí lấy nguyên văn từ khối `── CÁCH VERIFY sau Dev fix ──` trong ô *DEV phản hồi lần 1* của chính dòng này.

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Mạng lưới Tư vấn viên → Tổ chức tư vấn → Thêm mới | Mạng lưới Tư vấn viên → Tổ chức tư vấn → nút **Thêm mới** (`/chuyen-gia-tvv/to-chuc/tao-moi`) | Không |
| Bước 1 — đọc nhãn 2 trường giấy tờ | Đọc nhãn hai trường giấy tờ trong nhóm "Thông tin cơ bản" | Đã đọc trong nhóm **Thông tin cơ bản**: "Số Giấy đăng ký hoạt động" và "Ngày cấp Giấy đăng ký hoạt động" | Không |
| Bước 2 — để trống rồi Lưu | Để trống cả hai trường đó, điền đủ các trường bắt buộc còn lại → bấm Lưu, đọc câu báo lỗi | Điền đủ 5 trường bắt buộc còn lại (Tên tổ chức, Loại hình, Người đại diện, Lĩnh vực pháp luật, Địa chỉ trụ sở), để trống 2 trường giấy tờ, bấm **Lưu** | Không |
| Bước 3 — mở màn Chỉnh sửa | Mở màn Chỉnh sửa một tổ chức đã có, đọc lại nhãn hai trường đó | Mở Chỉnh sửa tổ chức **Trung tâm Tư vấn Pháp luật Seed** (TCTV-SEED-0001) và đọc lại 2 nhãn + bấm Lưu để đọc câu báo lỗi | Không |
| Cách bắt câu báo lỗi | Đọc câu báo lỗi hiện ra sau khi bấm Lưu | Cài bộ theo dõi thay đổi trên trang TRƯỚC khi bấm Lưu (không lọc trùng) + đọc lại trực tiếp trên màn + chụp ảnh | Không |
| Kiểm "không tạo bản ghi" | Bước 2 vẫn bị chặn, hồ sơ không được tạo | Sau khi bấm Lưu: không có yêu cầu gửi lên máy chủ, vẫn đứng nguyên màn Thêm mới; quay lại danh sách số đếm các thẻ giữ nguyên (Đang hoạt động 3 · Mới đăng ký 1) | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng màn hình, đã chạy đủ cả 3 bước của khối CÁCH VERIFY (chạy tới thao tác Lưu sinh ra câu báo lỗi, không chấm bằng quan sát tĩnh).

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6)

### Đối chiếu từng vế của khối "✅ PASS khi"

- ✅ **Hai nhãn trường dùng cùng một tên gọi "Giấy đăng ký hoạt động"** → màn Thêm mới đọc được: **"Số Giấy đăng ký hoạt động"** (bắt buộc) và **"Ngày cấp Giấy đăng ký hoạt động"** (bắt buộc). Không còn nhãn "Số Giấy ĐKHĐ Sở TP", cũng không còn "Giấy đăng ký hành nghề".
  Ảnh: [`../image/QLDMTCTV_OOS_13-themmoi-nhan-giay-dang-ky-hoat-dong.png`](../image/QLDMTCTV_OOS_13-themmoi-nhan-giay-dang-ky-hoat-dong.png)
- ✅ **Hai câu báo lỗi dùng cùng một tên gọi** → bấm Lưu khi để trống, hiện đúng 2 câu:
  - "Số Giấy đăng ký hoạt động là bắt buộc (NĐ 77/2008 Đ.13)"
  - "Hãy nhập thông tin cho trường Ngày cấp Giấy đăng ký hoạt động"
  Cả hai đều gọi giấy tờ là **"Giấy đăng ký hoạt động"**.
  Ảnh: [`../image/QLDMTCTV_OOS_13-bao-loi-hai-truong-cung-ten-goi.png`](../image/QLDMTCTV_OOS_13-bao-loi-hai-truong-cung-ten-goi.png)
- ✅ **Nhất quán giữa màn Thêm mới và màn Chỉnh sửa** → mở Chỉnh sửa "Trung tâm Tư vấn Pháp luật Seed": hai nhãn y hệt ("Số Giấy đăng ký hoạt động" / "Ngày cấp Giấy đăng ký hoạt động"); bấm Lưu khi hai trường trống cũng ra đúng hai câu báo lỗi giống hệt màn Thêm mới.
  Ảnh: [`../image/QLDMTCTV_OOS_13-chinhsua-nhan-giay-dang-ky-hoat-dong.png`](../image/QLDMTCTV_OOS_13-chinhsua-nhan-giay-dang-ky-hoat-dong.png)
- ✅ **Bước 2 vẫn bị chặn, hồ sơ không được tạo** → sau khi bấm Lưu, biểu mẫu viền đỏ hai trường giấy tờ, không phát sinh yêu cầu gửi hồ sơ lên máy chủ, trang vẫn đứng ở "Thêm mới Tổ chức tư vấn". Quay lại danh sách, số đếm các thẻ không đổi (Đang hoạt động 3 · Mới đăng ký 1) → không có bản ghi nào được tạo.

### Đối chiếu khối "❌ FAIL nếu"

- Còn chỗ nào dùng chữ "hành nghề" cho giấy tờ của tổ chức → **không xảy ra**. Rà toàn bộ chữ trên cả màn Thêm mới lẫn màn Chỉnh sửa (kể cả lúc đang hiện câu báo lỗi): không còn chữ "hành nghề".
- Hai trường vẫn gọi tên khác nhau → **không xảy ra** (cùng gọi "Giấy đăng ký hoạt động").
- Bước 2 lưu được hồ sơ trống giấy này → **không xảy ra** (bị chặn, không tạo bản ghi).

### Điểm khối CÁCH VERIFY dặn phải soi kỹ

- ⚠️ "Viết tắt ĐKHĐ chỉ chấp nhận nếu tên đầy đủ đã xuất hiện cùng màn; đừng chấm PASS khi màn chỉ có chữ viết tắt" → màn hiện nay **dùng thẳng tên đầy đủ** "Giấy đăng ký hoạt động" ở cả 4 chỗ (2 nhãn + 2 câu báo lỗi), không còn chữ viết tắt nào. Điều kiện cảnh báo này không bị chạm tới.

### Kết luận

Cả bốn vế của khối "✅ PASS khi" đều đạt, không vế nào của khối "❌ FAIL nếu" xảy ra → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Thứ tự trường trên biểu mẫu nay đã là: Tên tổ chức → Loại hình → Người đại diện → Chức vụ người đại diện → Số Giấy đăng ký hoạt động → Ngày cấp Giấy đăng ký hoạt động → **Lĩnh vực pháp luật → Số lao động** → Địa chỉ trụ sở → Số điện thoại → Email → Website → Số quyết định công bố → Ngày quyết định công bố → Ghi chú. Tức "Lĩnh vực pháp luật" và "Số lao động" đã về đứng cùng nhóm và đứng TRƯỚC nhóm Liên hệ, khớp đặc tả. Đây là phần thứ tự trường mà phiếu gốc từng nêu (BA/Dev không nhận việc ở vòng này) — ghi lại để đối tác/BA biết là hiện trạng cũng đã đúng.
- Nhãn "Lĩnh vực pháp luật" trên biểu mẫu, trong khi cột tương ứng ở bảng danh sách ghi "Lĩnh vực" — chỉ là khác cách rút gọn, không thuộc phạm vi phiếu.
