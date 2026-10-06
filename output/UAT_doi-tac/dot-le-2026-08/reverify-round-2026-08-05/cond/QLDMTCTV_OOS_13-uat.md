# QLDMTCTV_OOS_13 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 1`, dòng 339 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Bản mới nhất của môi trường nghiệm thu (bug đo trên V1.0.5) | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Màn hình | Mạng lưới Tư vấn viên → Tổ chức tư vấn → Thêm mới | Sidebar → Mạng lưới Tư vấn viên → Tổ chức tư vấn (`/chuyen-gia-tvv/to-chuc`) → [Thêm mới] (`/tao-moi`) | Không |
| Bước 1 | Đọc nhãn của hai trường giấy tờ trong nhóm "Thông tin cơ bản" | Đọc nguyên văn nhãn của **cả 15 trường** trên biểu mẫu, kèm dấu bắt buộc | Không |
| Bước 2 | Để trống hai trường đó, điền đủ trường bắt buộc còn lại → Lưu, đọc câu báo lỗi | Điền Tên tổ chức / Loại hình / Người đại diện / Lĩnh vực pháp luật / Địa chỉ trụ sở, để trống hai trường giấy tờ → bấm [Lưu], đọc nguyên văn câu báo lỗi + theo dõi yêu cầu gửi lên máy chủ | Không |
| Bước 3 | Mở màn Chỉnh sửa một tổ chức đã có, đọc lại nhãn hai trường | Mở `TC-STP-HN-0001` (`/chinh-sua`), đọc lại nhãn 15 trường; xóa trống trường giấy tờ rồi [Lưu] để đọc thêm câu báo lỗi ở màn này | Không |
| Chốt "không tạo bản ghi" | Hồ sơ không được tạo | Đối chiếu danh sách trước/sau: vẫn 15 tổ chức, không có bản ghi thử nào; bản ghi `TC-STP-HN-0001` giữ nguyên `soGiayDkhd = 3344` | Không |
| Điều kiện về viết tắt | "ĐKHĐ" chỉ chấp nhận nếu tên đầy đủ có trên cùng màn | Đếm số lần chuỗi `ĐKHĐ` và chuỗi `hành nghề` xuất hiện trên từng màn | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Hai nhãn trường nay dùng chung một tên gọi, đúng tên BA chốt**: trên màn Thêm mới đọc được
  `Số Giấy đăng ký hoạt động` và `Ngày cấp Giấy đăng ký hoạt động` — cả hai đều là **tên đầy đủ**, cùng một
  cách gọi. Hai tên khác nhau của phản ánh gốc ("Số Giấy ĐKHĐ Sở TP" và "Ngày cấp Giấy đăng ký hành nghề")
  **không còn**.
- **Hai câu báo lỗi cũng dùng đúng tên gọi đó**: để trống cả hai trường rồi bấm [Lưu] thì hiện
  `Số Giấy đăng ký hoạt động là bắt buộc (NĐ 77/2008 Đ.13)` và
  `Hãy nhập thông tin cho trường Ngày cấp Giấy đăng ký hoạt động`. Không câu nào còn chữ "hành nghề".
- **Không còn chữ "hành nghề" và không còn chữ viết tắt ở bất kỳ đâu trên hai màn**: đếm trên toàn bộ chữ
  của màn Thêm mới và màn Chỉnh sửa — chuỗi `hành nghề` xuất hiện **0 lần**, chuỗi `ĐKHĐ` xuất hiện
  **0 lần**. Nên điều kiện "viết tắt phải kèm tên đầy đủ" không cần xét tới. Màn danh sách Tổ chức tư vấn
  cũng không có chữ nào trong hai chuỗi đó.
- **Nhất quán giữa màn Thêm mới và màn Chỉnh sửa**: mở `TC-STP-HN-0001` ở màn Chỉnh sửa, danh sách nhãn
  **giống hệt** màn Thêm mới, kể cả dấu bắt buộc. Xóa trống trường số giấy rồi [Lưu] ở màn này cũng ra đúng
  câu `Số Giấy đăng ký hoạt động là bắt buộc (NĐ 77/2008 Đ.13)`.
- **Vẫn chặn, không tạo hồ sơ trống giấy này**: cả hai lần bấm [Lưu] đều dừng ở biểu mẫu, **không có yêu cầu
  nào được gửi lên máy chủ**, trang không chuyển. Danh sách trước và sau vẫn **15 tổ chức**, không có bản ghi
  mang tên thử nghiệm. Bản ghi đem ra sửa vẫn giữ nguyên `soGiayDkhd = 3344`, không bị đổi.
- **Phần mức bắt buộc phần mềm đang đúng, dev không đụng** — đo lại thấy vẫn đúng: cả hai trường đều có dấu
  bắt buộc trên biểu mẫu, và hồ sơ trống bị chặn.

### Điều nằm trong "Kết quả mong đợi" gốc, tiện đo luôn

Phản ánh gốc còn nêu thứ tự trường sai so với đặc tả `SCR-IV-NEW-02` (nhóm 2 gồm "Lĩnh vực pháp luật" và
"Số lao động" phải đứng trước nhóm Liên hệ). Thứ tự hiện tại đọc được trên biểu mẫu là:

`Tên tổ chức · Loại hình · Người đại diện · Chức vụ người đại diện · Số Giấy đăng ký hoạt động ·
Ngày cấp Giấy đăng ký hoạt động · **Lĩnh vực pháp luật · Số lao động** · Địa chỉ trụ sở · Số điện thoại ·
Email · Website · Số quyết định công bố · Ngày quyết định công bố · Ghi chú`

Tức "Lĩnh vực pháp luật" và "Số lao động" đã về **liền nhau và đứng trước nhóm Liên hệ** — đúng như đặc tả
mô tả. Phần thứ tự trường của phản ánh gốc cũng đã được khắc phục.

Ảnh: `../image/QLDMTCTV_OOS_13-uat-them-moi-bi-chan-dung-ten-goi.png` ·
`../image/QLDMTCTV_OOS_13-uat-man-chinh-sua-nhan-day-du.png` ·
`../image/QLDMTCTV_OOS_13-uat-cau-bao-loi-dung-ten-goi.png`

## Ghi nhận thêm

- Câu báo lỗi của hai trường **khác nhau về văn phong** (`… là bắt buộc (NĐ 77/2008 Đ.13)` so với
  `Hãy nhập thông tin cho trường …`) nhưng **cùng một tên gọi giấy tờ** — đúng điều phiếu yêu cầu. Ghi lại
  để BA quyết có muốn thống nhất luôn văn phong hai câu hay không; không dùng làm căn cứ trượt.
- Phiếu này ghi tiêu chí ở cột `DEV phản hồi lần 1` và dặn "[ghi vào cột Verify]"; theo yêu cầu của đợt đo
  này thì verdict vẫn ghi vào cột `Verify 2` cho đồng bộ với 36 phiếu còn lại.
- **Không tạo, không sửa dữ liệu nghiệp vụ nào**: hai lần bấm [Lưu] đều bị chặn nên không có bản ghi mới;
  bản ghi `TC-STP-HN-0001` đem ra thử ở màn Chỉnh sửa đã thoát bằng [Hủy], số giấy vẫn là `3344` như cũ.
