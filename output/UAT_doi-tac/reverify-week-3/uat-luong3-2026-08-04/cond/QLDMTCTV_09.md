# Bảng đối chiếu điều kiện — QLDMTCTV_09 (dòng 320) — Biểu mẫu Sửa thiếu 3 trường + phải điền sẵn đúng

**Kết luận:** Pass — biểu mẫu Sửa có đủ 3 trường, điền sẵn đúng 15/15 ô trên 2 hồ sơ, và lưu xuống thật.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (`cbnv_tw`, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương, đơn vị Bộ Tư pháp | `cbnv_tw` — Cán bộ NV Trung ương, Cục Bổ trợ tư pháp – Bộ Tư pháp | Không |
| Màn hình / entity + trạng thái | Biểu mẫu **Sửa** Tổ chức tư vấn, mở từ biểu tượng Sửa trên dòng danh sách | Cùng màn (`/chuyen-gia-tvv/to-chuc/{id}/chinh-sua`), mở đúng bằng biểu tượng bút chì trên dòng | Không |
| Dữ liệu tiền đề | Hồ sơ bất kỳ đang có sẵn | 2 hồ sơ có sẵn từ trước, KHÔNG do mình tạo: **TC-BTP-TW-0001** (Đang hoạt động, 2 TVV liên kết) và **TC-BTP-TW-0003** (Đang hoạt động). Cả hai đều có sẵn Số/Ngày QĐ công bố nhưng chưa có tệp | Không |
| Hồ sơ chưa có dữ liệu ở 3 trường thì có ẩn trường không | Nghi vấn vòng 1: chỉ hiện khi hồ sơ đã có dữ liệu | Cả 2 hồ sơ đều `fileDinhKem = []` mà vùng "File đính kèm" vẫn hiện đầy đủ; ô Ghi chú trống vẫn hiện | Không |
| Thao tác / input | Chỉ mở biểu mẫu rồi đọc trường | Mở biểu mẫu → đọc toàn bộ nhãn + giá trị từng ô → so với `GET /api/v1/to-chuc-tu-vans/{id}` → đính kèm tệp thật rồi bấm Lưu (bản ghi TC-BTP-TW-0001) | Không |
| Yêu cầu "điền sẵn đúng, đúng định dạng, không tràn/đè, đồng nhất tiếng Việt" | Vòng 1 không đánh giá được vì thiếu trường | 15/15 ô khớp dữ liệu bản ghi; ngày hiện dd/mm/yyyy; danh mục hiện nhãn tiếng Việt (không lộ mã enum); bố cục 2–3 cột, không tràn/đè | Không |

**Bằng chứng:**
- `image/QLDMTCTV_09-v2-01-sua-TC-BTP-TW-0001-duong-dan-co-ten-to-chuc-va-du-lieu-dien-san.png` — biểu mẫu Sửa TC-BTP-TW-0001: Tên tổ chức, Loại hình "Công ty Luật", Người đại diện "Nguyễn Văn A", Chức vụ "Giám đốc", Số Giấy ĐKHĐ "DKHD-HN-001/2024", Ngày cấp "15/03/2024", Lĩnh vực 3 thẻ, Số lao động 25 — tất cả điền sẵn.
- `image/QLDMTCTV_09-v2-02-sua-nhom-lien-he-cong-bo-tep-dinh-kem-du-3-truong.png` — nhóm Liên hệ (địa chỉ/điện thoại/email/website điền sẵn), nhóm **Công bố** với "QD-TW-0001/2026" + "06/05/2026", nhóm **File đính kèm** với vùng kéo thả.
- `image/QLDMTCTV_OOS_09-v2-01-duong-dan-Chinh-sua-kem-ten-to-chuc-khong-co-cap-Chi-tiet.png` — hồ sơ thứ 2 (TC-BTP-TW-0003) cũng điền sẵn đúng.
- network `PATCH /api/v1/to-chuc-tu-vans/beb25e6f-…` [200] — 1 request, 1 thông báo "Cập nhật thành công"; sau lưu, tệp đính kèm hiện trên màn Chi tiết.
