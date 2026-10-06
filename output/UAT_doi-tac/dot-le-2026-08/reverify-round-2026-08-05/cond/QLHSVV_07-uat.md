# QLHSVV_07 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 2`, dòng 128 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác, bản mới nhất | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò (trường hợp 1) | Cán bộ nghiệp vụ tự tạo hồ sơ | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Vai trò (trường hợp 2) | Doanh nghiệp tự gửi yêu cầu | `0151554887` — TKM Company, vai trò DN | Không |
| Màn hình | Chi tiết hồ sơ vụ việc → khối "Tài liệu đính kèm" → nút "Tải" | Đúng khối đó, cả 4 hồ sơ đo | Không |
| Tệp đo | Tệp đính kèm ngay lúc tạo hồ sơ | `qa-uat-tep-thu-nghiem.pdf` 618 B, mã toàn vẹn `57ca6cc8…9a14a9` | Không |
| Hồ sơ cũ | Hồ sơ ngày 04/08 đã có sẵn trên môi trường | `VV-BTP-TW-20260804-005` (tệp lúc tạo) + rà toàn bộ 68 hồ sơ / 14 tệp | Không |
| Nhóm "Thêm tài liệu" | Tệp nạp sau bằng nút "Thêm tài liệu" | Nạp mới `qa-uat-the-hanh-nghe.pdf` (loại "Bổ sung") + 4 tệp cũ của `VV-BTP-TW-20260804-003` | Không |
| Cách đo tải tệp | Bấm nút thật trên giao diện | Bấm nút "Tải" trên hàng tệp; chặn `URL.createObjectURL` để lấy đúng khối byte trình duyệt giao cho người dùng rồi băm SHA-256 tại chỗ | Không |
| Cách đo thông báo | — | Bộ theo dõi DOM cài trước khi bấm, không lọc trùng, đọc `innerText` | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Tự tạo hồ sơ mới, đính kèm tệp ngay lúc tạo — hàng tệp hiện đủ tên/định dạng/dung lượng**: tạo
  `VV-BTP-TW-20260805-002` (Bình Minh AG, đính kèm `qa-uat-tep-thu-nghiem.pdf` ngay ở màn Thêm mới).
  Hàng tệp hiện `qa-uat-tep-thu-nghiem.pdf · Yêu cầu · PDF · 618 B · Sạch · 05/08/2026 15:12` — đủ cả 3 mục.
- **Bấm "Tải" thì tệp về máy, màn hình đứng nguyên, không còn thông báo "Không kết nối được máy chủ."**:
  bấm nút "Tải" → trình duyệt nhận tệp tên đúng `qa-uat-tep-thu-nghiem.pdf`, đường dẫn tải là `blob:` (không
  phải mở màn xem chi tiết như bug gốc); địa chỉ trang giữ nguyên `…/vu-viec/109ba289-…`; bộ theo dõi ghi
  **0 thông báo** trong 3 giây sau khi bấm. Máy chủ trả `200` cho lượt lấy tệp.
- **Doanh nghiệp tự gửi yêu cầu có kèm tệp ngay từ đầu cũng tải về được**: đăng nhập tài khoản doanh nghiệp,
  "Gửi yêu cầu hỗ trợ pháp lý" kèm tệp → tạo `VV-STP-HN-20260805-002`. Mở chi tiết, hàng tệp hiện
  `PDF · 618 B · Sạch`; bấm "Tải" → nhận đủ tệp, 0 thông báo, màn hình đứng nguyên.
- **Tệp nhận được trùng khít từng byte với tệp gốc ở cả hai trường hợp**: mã kiểm tra toàn vẹn SHA-256 của
  khối byte trình duyệt giao cho người dùng ở cả hai lượt đều là
  `57ca6cc8e91c2aa97250f8a2b33c8aa51b6a35aec48c2b7013e2c122db9a14a9`, **trùng đúng** mã của tệp gốc trên máy
  (`shasum -a 256 qa-uat-tep-thu-nghiem.pdf`), dung lượng 618 B khớp.
- **Hồ sơ cũ ngày 04/08 nay cũng hiện đủ tên/định dạng/dung lượng và tải về được**: mở
  `VV-BTP-TW-20260804-005` — hàng tệp hiện `QLHSVV_07-v2-tep-dinh-kem-luc-tao-ho-so.pdf · Yêu cầu · PDF ·
  633 B · Sạch · 04/08/2026 19:25`; bấm "Tải" → nhận đủ 633 byte, 0 thông báo, màn hình đứng nguyên.
- **Rà toàn bộ tệp đính kèm trong kho hồ sơ vụ việc, không còn hàng nào mất tên hay trống định dạng**: quét
  hết **68 hồ sơ vụ việc** đang có trên môi trường → **14 tệp đính kèm**, **0 tệp** thiếu tên, thiếu định dạng
  hoặc thiếu dung lượng. Tải thử cả 14 tệp: **14/14 trả về `200`** và **số byte nhận đúng bằng dung lượng ghi
  trên hàng** (618, 633, 402, 1266, 1617, 4914, 13419, 19725, 36674, 53417, 198122, 217848, 264361 …).
- **Nhóm tệp thêm bằng nút "Thêm tài liệu" vẫn tải về đúng như trước**: nạp mới qua nút "Thêm tài liệu" →
  hàng `qa-uat-the-hanh-nghe.pdf · Bổ sung · PDF · 618 B · Sạch · 05/08/2026 15:16`; bấm "Tải" → mã toàn vẹn
  trùng tệp gốc, 0 thông báo. 4 tệp nhóm "Bổ sung" sẵn có của `VV-BTP-TW-20260804-003` (`.jpg` 13 419 B,
  `.pdf` 1 266 B, `.docx` 36 674 B, `.xlsx` 4 914 B) cũng nằm trong lượt rà 14/14 nói trên và đều tải đủ byte.

Ảnh: `../image/QLHSVV_07-uat-nhap-tay-tep-tai-ve-du-thong-tin.png` ·
`../image/QLHSVV_07-uat-dn-tu-gui-tep-tai-duoc.png` ·
`../image/QLHSVV_07-uat-ho-so-cu-0408-tai-duoc.png` ·
`../image/QLHSVV_07-uat-nhom-them-tai-lieu-tai-duoc.png`

## Ghi nhận thêm

- Dữ liệu phát sinh khi đo (đều là bước bắt buộc của chính khối tiêu chí): `VV-BTP-TW-20260805-002`
  (nhập tay, 2 tệp) và `VV-STP-HN-20260805-002` (doanh nghiệp tự gửi, 1 tệp).
- Hai tệp mẫu QA nạp lên (`qa-uat-tep-thu-nghiem.pdf`, `qa-uat-the-hanh-nghe.pdf`) có nội dung giống hệt nhau
  nên riêng phép so mã toàn vẹn giữa hai tệp này không phân biệt được nếu hệ thống trả nhầm tệp này sang tệp
  kia. Vế "không lẫn tệp" được chứng minh bằng lượt rà 14 tệp có dung lượng khác nhau rõ rệt (từ 402 B đến
  264 361 B) — số byte nhận về khớp đúng từng hàng.
- Không đụng tài khoản hay hồ sơ nghiệp vụ nào của đối tác; chỉ nạp thêm 1 tệp vào hồ sơ do QA vừa tạo.
