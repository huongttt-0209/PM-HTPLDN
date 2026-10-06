# DKTGMLTVV_05 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối `── CÁCH VERIFY sau Dev fix ──` ở cột `DEV phản hồi lần 1`, dòng 123
(tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — bundle `assets/index-Dn5IWt_M.js`, nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `nht_qa_tw` — vai trò NHT (Người hỗ trợ pháp lý) | `nht_04_ui` · vai trò NHT · `donViId 00000000-0000-4000-8000-000000000001` · cấp TW · Cục Bổ trợ tư pháp — tài khoản cùng vai trò cùng cấp, vì `nht_qa_tw` không tồn tại trên môi trường này | Không |
| Màn hình | Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → tab "Mới đăng ký" → Thêm mới | Đúng đường dẫn đó, màn "Thêm mới Tư vấn viên" | Không |
| Bước 1 — dữ liệu | Điền đủ mọi trường bắt buộc khác, nạp File thẻ hành nghề ở nhóm 2, để trống ô Bằng cấp/Chứng chỉ | Điền đủ 10 trường bắt buộc + chọn Trình độ, Lĩnh vực; nạp tệp PDF vào "File thẻ hành nghề (PDF)" nhóm 2; để trống nhóm "File đính kèm" | Không |
| Bước 2 — dữ liệu | Nạp một tệp PDF vào ô Bằng cấp/Chứng chỉ rồi bấm Xóa | Nạp `qa-uat-tep-thu-nghiem.pdf` (618 B) rồi bấm Xóa | Không |
| Bước 3 — hồ sơ đã lưu | Hồ sơ tư vấn viên đã lưu có sẵn tệp đính kèm, mở ở chế độ Chỉnh sửa | `TVV-BTP-TW-0080` — trạng thái Mới đăng ký, có sẵn 2 tệp đính kèm | Không |
| Thao tác đo | Bấm thật trên giao diện | Toàn bộ bấm trên màn; thông báo bắt bằng bộ theo dõi DOM không lọc trùng; đếm cả số lượt gọi máy chủ | Không |
| Trả lại dữ liệu | — | Bước 1 bị chặn nên không hồ sơ nào được tạo; bước 3 chỉ hủy xác nhận, hồ sơ `TVV-BTP-TW-0080` còn nguyên 2 tệp | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- Bước 1 · **bị chặn, hồ sơ KHÔNG được tạo**: bấm Lưu → thông báo
  "File đính kèm (Bằng cấp / Chứng chỉ) là bắt buộc khi đăng ký ứng viên mới"; bộ đo ghi nhận **0 lượt gọi
  ghi dữ liệu** lên máy chủ, màn hình đứng nguyên ở trang Thêm mới.
- Bước 1 · **lý do đọc được đúng chỗ thiếu**: câu thông báo gọi thẳng tên ô "File đính kèm (Bằng cấp /
  Chứng chỉ)", không phải chỉ nhắc thẻ hành nghề ⇒ vế FAIL "thông báo chặn chỉ nhắc thẻ hành nghề" không xảy ra.
- Bước 2 · **có bước xác nhận trước khi gỡ**: bấm Xóa ở dòng tệp vừa nạp → hộp thoại "Xác nhận xóa tệp —
  Bạn có chắc chắn muốn xóa tệp "qa-uat-tep-thu-nghiem.pdf"?" với hai nút Hủy / Xóa; tệp vẫn còn trong danh sách
  ở thời điểm hộp thoại mở.
- Bước 2 · **hủy xác nhận thì tệp còn nguyên**: bấm Hủy → tệp vẫn trong danh sách. Bấm Xóa rồi xác nhận →
  tệp mới bị gỡ.
- Bước 3 · **lặp lại ở chế độ Chỉnh sửa**: mở `TVV-BTP-TW-0080` → Sửa → bấm Xóa ở tệp
  `DKTGMLTVV_OOS_01-v2-bang-cap.pdf` → cũng ra đúng hộp thoại xác nhận, tệp còn nguyên khi chưa xác nhận;
  bấm Hủy → cả hai tệp còn đủ. Không xác nhận gỡ để không phá dữ liệu sẵn có của môi trường nghiệm thu —
  vế PASS của phiếu chỉ đòi "phải qua một bước xác nhận trước khi tệp bị gỡ, hủy xác nhận thì tệp còn nguyên",
  và vế FAIL "gỡ tệp ngay không hỏi lại" đã bị loại trừ ở cả hai màn.
- Dòng ⚠️ của phiếu · nhóm 4 "File đính kèm" trên màn chỉ có duy nhất ô "File đính kèm (Bằng cấp / Chứng chỉ)",
  không có ô "Tệp thẻ hành nghề" — đúng như BA đã chốt, **không chấm FAIL**. Ô "File thẻ hành nghề (PDF)" nằm ở
  nhóm 2 "Thông tin nghề nghiệp" như thiết kế.

Ảnh: `../image/DKTGMLTVV_05-uat-chan-luu-thieu-bang-cap.png` ·
`../image/DKTGMLTVV_05-uat-xac-nhan-xoa-tep-tao-moi.png` ·
`../image/DKTGMLTVV_05-uat-xac-nhan-xoa-tep-chinh-sua.png`

## Ghi nhận thêm — thay đổi môi trường do QA thực hiện

Tài khoản `nht_qa_tw` ghi trong `input/input.md` chỉ tồn tại ở môi trường nội bộ, không có trên môi trường
nghiệm thu này; các tài khoản NHT sẵn có ở đây cũng không dùng mật khẩu `Test@1234`. Đã đặt lại mật khẩu tài
khoản kiểm thử `nht_04_ui` (NHT UI Test 04 — tài khoản do QA tạo trước đó, cùng vai trò NHT, cùng cấp TW,
cùng đơn vị Cục Bổ trợ tư pháp) qua luồng "Quên mật khẩu?" + hộp thư của môi trường, nay là `Test@1234`.
Không đụng tài khoản nghiệp vụ nào của đối tác.
