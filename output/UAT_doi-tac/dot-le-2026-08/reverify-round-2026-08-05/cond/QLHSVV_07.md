# Bảng đối chiếu điều kiện — QLHSVV_07 (re-verify vòng 2, 05/08/2026)

Loại bug: **bấm "Tải" ở nhóm Tài liệu đính kèm không lấy được tệp về máy** → phụ thuộc nguồn gốc của tệp (đính kèm lúc tạo hồ sơ so với thêm sau) ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 2*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy phần **"Phần còn lỗi"** của note làm điều kiện bắt buộc phải hết lỗi, và phần **"Phần đã hết lỗi"** làm mốc phải giữ được (kiểm lại để chắc không hỏng ngược).

| Điều kiện | Bug gốc (phần còn lỗi + phần đã hết lỗi của note) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | Cán bộ nghiệp vụ Trung ương | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp; và thêm **tài khoản doanh nghiệp** "QA UAT Kiem Thu DN" (mã số thuế 0109998887) cho luồng doanh nghiệp tự gửi | Không |
| Màn hình | Nhóm "Tài liệu đính kèm" trên màn Chi tiết vụ việc | Đúng nhóm đó trên màn **Chi tiết vụ việc**, mở bằng cách bấm mã hồ sơ từ danh sách | Không |
| Tiền đề — tệp đính kèm lúc tạo hồ sơ | Note đo trên các hồ sơ 04/08 (VV-BTP-TW-20260804-001, -002, -003, -005) | Hồ sơ -005 không còn trong kho, nên **tự tạo hồ sơ mới qua đúng luồng người dùng** và đính kèm tệp ngay lúc tạo, thay vì chấm trên dữ liệu cũ; đồng thời kiểm lại 2 hồ sơ cũ mà note nêu (-001, -002) vẫn còn | Không |
| Tiền đề — tệp doanh nghiệp gửi kèm từ đầu | Note nêu "đúng những tệp doanh nghiệp gửi kèm ngay từ đầu lại không bao giờ lấy lại được" | Đăng nhập bằng chính **tài khoản doanh nghiệp**, gửi yêu cầu mới **có kèm tệp ngay từ đầu**, rồi mở lại hồ sơ đó để tải | Không |
| Tiền đề — nhóm "Thêm tài liệu" | Note ghi nhóm này đã hết lỗi (9 tệp tải về trùng khít từng byte) | Kiểm lại: **thêm một tệp mới bằng nút "Thêm tài liệu"** trên chính hồ sơ vừa tạo rồi tải về, để chắc phần đang chạy tốt không bị hỏng ngược | Không |
| Bước đo 1 | Bấm nút "Tải" trên từng hàng tệp | Bấm **thật** nút "Tải" ở từng hàng, ở cả 3 nhóm tệp (đính kèm lúc tạo · doanh nghiệp gửi kèm · thêm sau) | Không |
| Bước đo 2 | Bấm nút "Xem" trên hàng tệp | Bấm **thật** nút "Xem" trên hàng tệp đính kèm lúc tạo | Không |
| Bước đo 3 | Đọc tên tệp, cột Định dạng, cột Kích thước ngay trên bảng | Đọc đủ 7 cột của bảng ở từng hồ sơ, kèm ảnh chụp màn | Không |
| Bước đo 4 | Ghi nhận câu thông báo hiện lên khi bấm Tải | Cài **bộ bắt thông báo** trên trang trước khi bấm (thông báo tự tắt sau vài giây), ghi lại toàn bộ thông báo xuất hiện — không lọc trùng | Không |
| Cách kiểm tệp nhận được | Note đối chiếu "trùng khít từng byte với tệp gốc" | Mở thư mục tải xuống lấy **tệp thật đã về máy**, tính **mã kiểm tra toàn vẹn** rồi so với tệp gốc; đối chiếu thêm **dung lượng và mã kiểm tra do kho lưu trữ trả về** | Không |
| Phạm vi rà soát | Note đo trên vài hồ sơ | Rà **toàn bộ tệp đính kèm đang có trong kho hồ sơ vụ việc** để chắc không còn hàng tệp nào mất tên / trống định dạng / trống kích thước | Không |
| Ràng buộc chấm | Không chấm bằng quan sát tĩnh, phải chạy tới bước sinh ra lỗi cũ; không chép kết luận vòng trước | Tự tạo **3 tệp mới** trong phiên đo và bấm Tải/Xem trên từng tệp; không dùng lại kết quả đo của lần trước | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò và màn hình, tự dựng lại tiền đề đã mất, đo đủ cả ba nhóm tệp, chạy trọn tới chỗ sinh ra lỗi cũ và kiểm tệp nhận được bằng mã kiểm tra toàn vẹn.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6)

### Ý còn lỗi (1) — tệp đính kèm ngay lúc tạo hồ sơ (luồng cán bộ nhập tay)

- ✅ Tạo mới hồ sơ **VV-BTP-TW-20260805-003** qua đúng luồng thao tác, đính kèm một tệp PDF 446 B ngay trên biểu mẫu trước khi lưu.
- ✅ Sau khi lưu, hàng tệp hiện **đầy đủ**: tên tệp đúng "QA-REVERIFY-0805-QLHSVV07-dinh-kem-luc-tao.pdf", **Định dạng "PDF"**, **Kích thước "446 B"**, Trạng thái quét "Sạch". **Không còn tên thay thế kiểu "File đính kèm 8e7566a5"**, không còn ô định dạng trống hay kích thước gạch ngang.
- ✅ Bấm **"Tải"**: **tệp về máy thật**, màn hình đứng nguyên, **không có thông báo "Không kết nối được máy chủ."** (bộ bắt thông báo không ghi nhận thông báo nào).
- ✅ **Tệp nhận được trùng khít từng byte với tệp gốc**: mã kiểm tra toàn vẹn của tệp tải về bằng đúng mã của tệp gốc (`2e5189a0…f7d6`), dung lượng 446 B khớp; kho lưu trữ cũng trả về đúng mã kiểm tra của tệp gốc.
- ✅ Bấm **"Xem"**: mở được bản xem trước của chính tệp đó — không còn cảnh không mở được.
  Ảnh: [`../image/QLHSVV_07-r2-ho-so-moi-tep-dinh-kem-day-du.png`](../image/QLHSVV_07-r2-ho-so-moi-tep-dinh-kem-day-du.png)

### Ý còn lỗi (2) — tệp doanh nghiệp gửi kèm ngay từ đầu

- ✅ Đăng nhập bằng chính **tài khoản doanh nghiệp**, gửi yêu cầu mới **VV-STP-HN-20260805-003** có kèm tệp ngay từ đầu.
- ✅ Hàng tệp hiện đầy đủ tên / **PDF** / **446 B** / "Sạch"; bấm **"Tải"** thì **tệp về máy**, không có thông báo lỗi.
- ✅ **Tệp nhận được cũng trùng khít từng byte với tệp gốc** (cùng mã kiểm tra `2e5189a0…f7d6`).
  Ảnh: [`../image/QLHSVV_07-r2-dn-gui-kem-tep-tai-ve-ok.png`](../image/QLHSVV_07-r2-dn-gui-kem-tep-tai-ve-ok.png)

### Ý còn lỗi (3) — hai hồ sơ cũ mà phiếu nêu và toàn bộ kho tệp

- ✅ Hồ sơ cũ **VV-BTP-TW-20260804-001** (tệp đính kèm lúc tạo, ngày 04/08) nay hiện đúng tên tệp, **PDF**, **605 B**, "Sạch"; bấm "Tải" thì tệp về máy, không thông báo lỗi.
- ✅ **Rà toàn bộ tệp đính kèm đang có trong kho hồ sơ vụ việc (7 tệp trên 7 hồ sơ)**: **không còn hàng tệp nào** mang tên thay thế kiểu "File đính kèm <chuỗi>", **không hàng nào** trống Định dạng hay trống Kích thước.

### Ý còn lỗi (4) — câu thông báo sai bản chất

- ✅ Trong toàn bộ phiên đo, **không lần bấm "Tải" nào sinh ra câu "Không kết nối được máy chủ."**; nút "Tải" nay tải im lặng, không hiện thông báo nào. Câu gây hiểu nhầm đã hết đường xuất hiện vì bản thân thao tác tải không còn hỏng.

### Phần note ghi đã hết lỗi — kiểm lại để chắc không hỏng ngược

- ✅ Thêm một tệp mới bằng nút **"Thêm tài liệu"** trên chính hồ sơ vừa tạo: hàng tệp hiện đúng tên, **PDF**, **259 B**, loại "Bổ sung"; bấm "Tải" thì tệp về máy và **trùng khít từng byte với tệp gốc** (`526b4924…2bdd`). Nhóm đang chạy tốt vẫn giữ nguyên, không bị hỏng ngược.
- ✅ Hai nút **"Xem"** và **"Tải"** vẫn tách bạch: "Tải" lấy tệp về và giữ nguyên màn hình, "Xem" mở bản xem trước — đúng yêu cầu gốc của phiếu (trước kia bấm "Tải" lại mở màn xem chi tiết).

### Kết luận

Tự dựng lại đủ ba nhóm tệp và bấm thật nút "Tải" trên từng nhóm trong cùng một phiên: tệp đính kèm ngay lúc cán bộ tạo hồ sơ, tệp doanh nghiệp gửi kèm ngay từ đầu, và tệp thêm sau — cả ba đều hiện đủ tên / định dạng / kích thước và đều tải về được đúng tệp, trùng khít từng byte với tệp gốc; hai hồ sơ cũ mà phiếu nêu cũng đã lấy lại được tệp; không còn hàng tệp mất thông tin nào trong kho và không còn câu thông báo gây hiểu nhầm → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Nút **"Xem"** mở tệp ở **thẻ mới của trình duyệt** thay vì khung xem trước ngay trong trang. Yêu cầu của phiếu chỉ là bấm "Tải" thì tệp phải về máy, nên không dùng ý này để chấm; chỉ ghi lại để đối tác/BA biết cách trình bày hiện tại.
- Dữ liệu do kiểm thử tạo trong phiên đo: hồ sơ **VV-BTP-TW-20260805-003** (2 tệp: một đính kèm lúc tạo, một thêm sau) và **VV-STP-HN-20260805-003** (1 tệp doanh nghiệp gửi kèm từ đầu). Tệp gốc dùng để đối chiếu lưu tại `evidence/QA-REVERIFY-0805-QLHSVV07-dinh-kem-luc-tao.pdf` và `evidence/QA-REVERIFY-0805-QLHSVV07-them-tai-lieu.pdf`.
