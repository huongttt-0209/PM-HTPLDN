# Bảng đối chiếu điều kiện — NHSYC_01 (re-verify vòng 1, 05/08/2026)

Loại bug: **không tạo được hồ sơ yêu cầu nhập tay (lỗi định dạng ngày tiếp nhận)** kèm nhóm ý về mức ưu tiên → phụ thuộc dữ liệu doanh nghiệp thuộc diện ưu tiên và cả hai luồng tạo hồ sơ ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 1*) CÓ khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy nguyên khối đó làm tiêu chí (Precondition / 4 bước / ✅ PASS khi / ❌ FAIL nếu / dòng ⚠️).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Vụ việc HTPL → nhập hồ sơ yêu cầu thủ công | Vụ việc HTPL → **Nhập thủ công** (đi bằng menu bên trái), rồi mở lại hồ sơ ở màn **Chi tiết** | Không |
| Tiền đề — doanh nghiệp thuộc diện ưu tiên | Cần một doanh nghiệp thuộc diện ưu tiên (do phụ nữ làm chủ, hoặc dùng nhiều lao động nữ theo ngưỡng đã dẫn) | Kho chưa có doanh nghiệp nào thuộc diện này nên **tự tạo mới qua giao diện**: "QA REVERIFY 0805 - DN do phu nu lam chu" (mã số thuế 0805202601), đánh dấu **do phụ nữ làm chủ**, 40 lao động / 30 lao động nữ | Không |
| Tiền đề — doanh nghiệp đối chứng | Không nêu, nhưng cần để chứng minh mức ưu tiên là tính chứ không phải giá trị mặc định | Dùng thêm một doanh nghiệp **không thuộc diện ưu tiên** ("Cong ty TNHH QA UAT Kiem Thu", mã số thuế 0109998887) làm nhóm đối chứng | Không |
| Tiền đề — tài khoản doanh nghiệp | Bước 3 cần tài khoản doanh nghiệp thuộc diện ưu tiên tự gửi hồ sơ | Đăng nhập bằng chính tài khoản doanh nghiệp 0109998887; **doanh nghiệp tự cập nhật hồ sơ của mình** thành 20 lao động / 15 lao động nữ để rơi vào diện dùng nhiều lao động nữ | Không |
| Bước 1 | Nhập hồ sơ thủ công đầy đủ, **chọn ngày tiếp nhận từ ô chọn ngày trên giao diện** → Lưu | Điền đủ các trường bắt buộc, **bấm chọn ngày trên lịch của ô "Ngày tiếp nhận"** (không gõ tay), bấm Lưu và đọc thông báo hệ thống trả về | Không |
| Bước 2 | Mở hồ sơ vừa tạo, đọc mức ưu tiên và đối chiếu tiêu chí ưu tiên của doanh nghiệp | Mở màn Chi tiết của hồ sơ vừa tạo, đọc ô **Ưu tiên**; làm thêm **một hồ sơ đối chứng** cùng luồng cho doanh nghiệp không thuộc diện ưu tiên để so hai giá trị | Không |
| Bước 3 | Đăng nhập tài khoản doanh nghiệp, tự gửi một hồ sơ → mở lại bằng `cbnv_tw`, đọc mức ưu tiên | Doanh nghiệp tự gửi **2 hồ sơ**: một hồ sơ **trước** khi khai thông tin lao động và một hồ sơ **sau** khi khai 20 lao động / 15 lao động nữ; cả hai mở lại bằng `cbnv_tw` để đọc mức ưu tiên | Không |
| Bước 4 | Đọc ô "Độ ưu tiên" trên màn danh sách và màn chi tiết | Đọc ô **Độ ưu tiên** ở màn nhập hồ sơ (mở cả danh sách lựa chọn), quét chữ hiển thị ở **màn danh sách** và **màn chi tiết** | Không |
| Cách đo | Phải đọc được mức ưu tiên và biết nó khớp tiêu chí nào | Đo **2 cách**: đọc thẳng ô trên màn hình (kèm ảnh chụp) + đối chiếu mức ưu tiên đang lưu của từng hồ sơ trong danh sách vụ việc | Không |
| Ràng buộc chấm | Không chấm bằng quan sát tĩnh, phải chạy tới bước sinh ra lỗi cũ | Chạy trọn cả 4 bước, **tạo mới 4 hồ sơ vụ việc thật** trong phiên đo (2 luồng cán bộ nhập tay + 2 luồng doanh nghiệp tự gửi) | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò và màn hình, tự dựng đủ tiền đề còn thiếu (doanh nghiệp thuộc diện ưu tiên + doanh nghiệp đối chứng + tài khoản doanh nghiệp), chạy trọn cả 4 bước tới chỗ sinh ra lỗi cũ, đo bằng 2 cách.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw` và tài khoản doanh nghiệp 0109998887)

### Bước 1 — nhập hồ sơ thủ công, chọn ngày tiếp nhận trên giao diện

- ✅ **Lưu thành công**, hệ thống báo đã tiếp nhận kèm mã hồ sơ **VV-BTP-TW-20260805-001**. **Không còn thông báo lỗi định dạng ngày tiếp nhận** — đúng chỗ phiếu đang tắc.
- ✅ Hồ sơ vào thẳng trạng thái **"Đã tiếp nhận"** (bước 3 trên thanh tiến trình).
- ✅ Mã hồ sơ đúng quy tắc của hệ thống: **VV** - đơn vị **BTP-TW** - ngày **20260805** - số thứ tự **001**; hồ sơ thứ hai tạo sau đó ra **-002**, số thứ tự chạy đúng.
- ✅ Thời hạn xử lý hệ thống tự tính **25/08/2026** từ ngày tiếp nhận 04/08/2026 — đúng 15 ngày làm việc (trừ hai ngày cuối tuần 08-09/08, 15-16/08, 22-23/08).
  Ảnh: [`../image/NHSYC_01-r1-uu-tien-3-dn-uu-tien.png`](../image/NHSYC_01-r1-uu-tien-3-dn-uu-tien.png)

### Bước 2 — mức ưu tiên ở luồng cán bộ nhập tay

- ✅ Hồ sơ của doanh nghiệp **do phụ nữ làm chủ** (40 lao động / 30 lao động nữ) → ô **Ưu tiên = 3**, đúng diện "doanh nghiệp do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ".
- ✅ Hồ sơ **đối chứng** cùng luồng, doanh nghiệp không thuộc diện ưu tiên → **VV-BTP-TW-20260805-002**, ô **Ưu tiên = 1** (mức thường). Hai hồ sơ tạo cách nhau 3 phút, chỉ khác doanh nghiệp ⇒ **giá trị là kết quả tính, không phải số mặc định**.
  Ảnh: [`../image/NHSYC_01-r1-uu-tien-1-dn-doi-chung.png`](../image/NHSYC_01-r1-uu-tien-1-dn-doi-chung.png)

### Bước 3 — mức ưu tiên ở luồng doanh nghiệp tự gửi

- ✅ Đăng nhập bằng chính tài khoản doanh nghiệp, tự gửi hồ sơ **VV-STP-HN-20260805-001** khi hồ sơ doanh nghiệp **chưa khai thông tin lao động** → mở lại bằng `cbnv_tw`, ô **Ưu tiên = 1**.
  Ảnh: [`../image/NHSYC_01-r1-dn-tu-gui-truoc-uu-tien-1.png`](../image/NHSYC_01-r1-dn-tu-gui-truoc-uu-tien-1.png)
- ✅ Doanh nghiệp **tự cập nhật hồ sơ của mình** thành 20 lao động / 15 lao động nữ (75%, vượt ngưỡng nhiều lao động nữ), rồi tự gửi tiếp hồ sơ **VV-STP-HN-20260805-002** → mở lại bằng `cbnv_tw`, ô **Ưu tiên = 3**.
  Ảnh: [`../image/NHSYC_01-r1-dn-tu-gui-sau-uu-tien-3.png`](../image/NHSYC_01-r1-dn-tu-gui-sau-uu-tien-3.png)
- ✅ **Cùng một doanh nghiệp, chỉ khác thông tin lao động, mức ưu tiên đổi từ 1 lên 3** ⇒ luồng doanh nghiệp tự gửi nay **có tự tính mức ưu tiên**, đúng ý (3) của phiếu; không còn cảnh chỉ luồng cán bộ nhập tay mới tính.
- ✅ **Giá trị nằm trong thang 1-5** ở cả 4 hồ sơ đo được (1 · 1 · 3 · 3), không có giá trị nào vượt ngưỡng — đúng ý (4) về cách xếp nhóm thay cho cộng dồn.
- ✅ **Cách đo thứ hai cho cùng kết quả**: đối chiếu mức ưu tiên đang lưu của 4 hồ sơ trong danh sách vụ việc, trùng khớp với con số đọc trên màn chi tiết ở cả 4 hồ sơ.

### Bước 4 — ô "Độ ưu tiên" trên giao diện

- ✅ Ô **"Độ ưu tiên"** ở màn nhập hồ sơ nay chỉ còn hai lựa chọn viết bằng chữ dễ hiểu: **"4 — Cán bộ nâng mức, kèm lý do"** và **"5 — Cán bộ nâng mức khẩn, kèm lý do"**, kèm dòng gợi ý **"Để trống để hệ thống tự tính theo hồ sơ doanh nghiệp"**. **Không còn chuỗi mã quy tắc nội bộ nào** — đúng ý (2).
  Ảnh: [`../image/NHSYC_01-r1-o-do-uu-tien-khong-con-ma-quy-tac.png`](../image/NHSYC_01-r1-o-do-uu-tien-khong-con-ma-quy-tac.png)
- ✅ **Màn danh sách** vụ việc: quét toàn bộ chữ hiển thị, **không có chuỗi mã quy tắc nào lộ ra**.
- ✅ **Màn chi tiết**: ô "Ưu tiên" hiện đúng con số, không kèm mã quy tắc.
- ✅ **Nhãn chữ đi kèm đúng chiều với giá trị số**: số càng lớn thì mức càng gấp ("4 — nâng mức" đứng trước "5 — nâng mức khẩn"), và khớp với thang mà nghiệp vụ đã chốt (1 mức thường · 3 diện phụ nữ làm chủ / nhiều lao động nữ · 4-5 do cán bộ nâng mức). Đối chiếu với chính số đo được ở bước 2-3 (doanh nghiệp thường ra 1, doanh nghiệp thuộc diện ưu tiên ra 3) thì chữ và số cùng chiều, **không còn cảnh nhãn chữ ngược với giá trị lưu** — đúng ý (1).

### Kết luận

Bốn bước của khối CÁCH VERIFY đều đạt: tạo được hồ sơ thủ công và không còn lỗi định dạng ngày tiếp nhận, hồ sơ vào trạng thái "Đã tiếp nhận" với mã sinh đúng quy tắc; mức ưu tiên được tính tự động ở **cả hai luồng** (cán bộ nhập tay và doanh nghiệp tự gửi), giá trị nằm trong thang 1-5 và khớp tiêu chí ưu tiên của từng doanh nghiệp; nhãn chữ cùng chiều với con số; giao diện không còn chuỗi mã quy tắc nội bộ. Không điều kiện FAIL nào của phiếu xảy ra → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- **Ô "Ngày tiếp nhận" mặc định sẵn ngày hôm nay, nhưng để nguyên mặc định rồi Lưu thì hệ thống báo "Ngày tiếp nhận không được ở tương lai"** — phải lùi lại một ngày mới lưu được. Đây là chuyện lệch giờ giữa ô chọn ngày và giờ máy chủ, **khác** với lỗi định dạng ngày mà phiếu phản ánh (lỗi định dạng đã hết). Ghi lại để đối tác/BA cân nhắc mở phiếu riêng, vì cán bộ nhập hồ sơ trong ngày sẽ gặp thường xuyên.
- Màn chi tiết chỉ hiện **con số** mức ưu tiên, không kèm chú giải bằng chữ và không có huy hiệu màu. Đúng như nghiệp vụ đã chốt (giá trị hiển thị là con số), nhưng cán bộ mới dùng sẽ khó đoán "3" nghĩa là gì nếu không tra bảng chú giải. Chỉ ghi lại.
- Danh sách vụ việc **không có cột mức ưu tiên**, nên không sắp xếp hay lọc hồ sơ theo mức ưu tiên được. Không thuộc phạm vi phiếu, chỉ ghi lại.
- Dữ liệu do kiểm thử tạo trong phiên đo: doanh nghiệp **"QA REVERIFY 0805 - DN do phu nu lam chu"** (mã số thuế 0805202601); 4 hồ sơ vụ việc **VV-BTP-TW-20260805-001/002** và **VV-STP-HN-20260805-001/002**; hồ sơ doanh nghiệp 0109998887 được chính doanh nghiệp cập nhật thành **20 lao động / 15 lao động nữ** (trước đó bỏ trống) — giữ nguyên để còn đối chiếu bằng chứng.
