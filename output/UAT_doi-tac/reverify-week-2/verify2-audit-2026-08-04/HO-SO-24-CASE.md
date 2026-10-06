# Hồ sơ 24 case — vòng soát lại 2 (Verify 2), tab `UAT_TGPL Doanh Nghiệp-tuần 2`

> Snapshot sheet 2026-08-04. Cột `DEV phản hồi lần 1` = note VÒNG 1 (của QA hoặc của dev) — dùng để biết BUG GỐC là gì.


---

## row 117 — QLKTLBG_09

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Xem bài giảng/tài liệu chứa Slide
```

**Điều kiện:**
```
1. Đăng nhập tài khoản
```

**Các bước thực hiện:**
```
1. Chọn menu "Đào tạo, tập huấn" -> "Kho tài liệu / Bài giảng"
2. Xem bài giảng/tài liệu chứa Slide
```

**Kết quả mong đợi:**
```
Hệ thống mở khu vực xem trước nội dung với Slide: trình chiếu inline
```

**Kết quả thực tế:**
```
Hệ thống thực hiện tải xuống slide, không trình chiếu inline
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Đã kiểm tra lại đúng điều kiện phản ánh: vai trò Cán bộ nghiệp vụ Trung ương, màn Đào tạo, tập huấn > Kho tài liệu / Bài giảng, bài giảng có Loại tài liệu = Slide, tệp PowerPoint đuôi .pptx, trạng thái Đã công khai, có ảnh đại diện. Tổ kiểm thử tự tạo bài giảng mới bằng luồng Thêm mới để đúng điều kiện, không dùng lại dữ liệu cũ.
- Web đang sai: bấm xem trước bài giảng Slide thì hộp thoại "Xem trước" mở ra nhưng khu vực xem trước TRẮNG HOÀN TOÀN, không trình chiếu nội dung slide. Hộp thoại chỉ hiển thị Công khai, Ngày công khai, Ảnh đại diện, Mô tả công khai và đúng một nút đóng.
- Ngoài ra hệ thống không hiện thông báo thay thế "Không thể xem trực tuyến", cũng không có nút "Tải về" trong hộp thoại xem trước, và cột Thao tác của bảng cũng chỉ có xem trước / Sửa / Xóa. Vì vậy người dùng không có cách nào tiếp cận nội dung bài giảng từ màn này.
- Yêu cầu theo đặc tả:
  + FR-III-07 (UC26) §Mô tả (dòng 726): tài liệu gồm 3 loại Slide (PPTX), PDF, Video (nhúng YouTube) và phải xem trước ngay trong trang.
  + FR-III-07 (UC26) §Tiêu chí chấp nhận (dòng 792): khi người dùng chọn xem trước thì hệ thống phải hiển thị nội dung tệp trên trình duyệt.
  + SCR-III-03 §Thành phần 6 – Bảng xem trước (dòng 1955): Slide/PDF xem trực tiếp trong trình duyệt; nếu định dạng không xem được thì phải hiển thị "Không thể xem trực tuyến" kèm nút "Tải về".
  + SCR-III-03 §Thành phần 4 – Bảng tài liệu, cột Hành động (dòng 1951): phải có "Xem trực tuyến" và "Tải về (chỉ Slide/PDF)" là hai hành động tách bạch.
  + FR-III-07 (UC26) §Inputs dòng 743 quy định tệp Slide đúng là .pptx, nên .pptx thuộc nhóm bắt buộc xem được, không phải định dạng lạ.
- Nghĩa là dù hiểu theo hướng nào thì hiện tại vẫn chưa đạt: hoặc phải trình chiếu được nội dung slide, hoặc tối thiểu phải báo "Không thể xem trực tuyến" kèm nút "Tải về".
- Đối chứng trên cùng màn, cùng tài khoản: bài giảng loại Video vẫn hiển thị được khung YouTube, chứng tỏ khu vực xem trước hoạt động; riêng tệp lưu trên hệ thống thì không hiển thị được.
- Lưu ý so với phản ánh ban đầu: trên bản dựng hiện tại hệ thống không còn tự tải tệp xuống máy nữa, nhưng vẫn không trình chiếu inline, tức yêu cầu chính vẫn chưa đạt.
- Mã lỗi nội bộ: BUG-QLKTLBG_09. Tài khoản kiểm tra: cbnv_tw (Cán bộ nghiệp vụ Trung ương, đơn vị Cục Bổ trợ tư pháp). Bản dựng V1.0.5, kiểm tra ngày 03/08/2026.
```

---

## row 118 — QLDXDTTH_01

- **Tên chức năng:** Quản lý đề xuất đào tạo, tập huấn
- **Tác nhân (đối tác ghi):** Doanh nghiệp/Người hỗ trợ
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Quản lý các đề xuất tổ chức đào tạo/tập huấn từ các đơn vị/cá nhân khác nhau.
```

**Điều kiện:**
```
1. Đăng nhập tài khoản
```

**Các bước thực hiện:**
```
1. Chọn menu "Diễn đàn, hỗ trợ pháp lý" -> Chương trình hỗ trợ pháp lý DN
2. Tại mục "Danh mục", chọn Đào tạo -> Kế hoạch đào tạo
3. Nhấn Gửi đề xuất
4. Nhập thông tin hợp lệ và nhấn Gửi
```

**Kết quả mong đợi:**
```
- Tạo đề xuất ở trạng thái "Mới".
- Gửi thông báo cho Cán bộ nghiệp vụ thuộc đơn vị tiếp nhận.
- Gửi thành công, hệ thống hiển thị thông báo "Đã gửi đề xuất đào tạo".
```

**Kết quả thực tế:**
```
Hệ thống hiển thị thông báo thành công nhưng đề xuất không hiển thị trên màn hình
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
☑️ Đã kiểm tra lại — lỗi không còn, chức năng chạy đúng.
- Đã chạy lại trọn vẹn luồng Gửi đề xuất đào tạo, tập huấn (UC 32) bằng đúng vai trò phản ánh: đăng nhập bằng tài khoản Doanh nghiệp, nhập cùng bộ dữ liệu (lĩnh vực Dân sự, thời gian mong muốn quý 3/2026, địa điểm Hà Nội, số lượng dự kiến 10).
- Kết quả: hệ thống báo "Đề xuất đào tạo đã được gửi thành công" đúng một lần, và đề xuất HIỆN NGAY trên danh sách đề xuất của người gửi mà không cần thao tác gì thêm.
- Đã tải lại trang một lần nữa để kiểm chắc: đề xuất vẫn còn, ở trạng thái "Mới gửi", đúng ngày gửi, kèm hai thao tác Sửa và Xóa của người gửi. Lọc theo trạng thái "Mới gửi" cũng ra đúng đề xuất này.
- Đã kiểm thêm phía tiếp nhận: đăng nhập tài khoản Cán bộ nghiệp vụ đúng đơn vị tiếp nhận của đề xuất — đề xuất hiển thị đầy đủ trên tab "Đề xuất đào tạo", và cán bộ nhận được thông báo "Đề xuất đào tạo mới" ngay tại thời điểm gửi.
- Như vậy cả ba yêu cầu của phiếu kiểm thử đều đạt: đề xuất được tạo ở trạng thái mới, cán bộ nghiệp vụ của đơn vị tiếp nhận nhận được thông báo, và người gửi nhận được thông báo gửi thành công.
- Lưu ý giúp tổ kiểm thử để tránh hiểu nhầm khi kiểm lại: màn hình "Kế hoạch đào tạo" là danh sách các kế hoạch đào tạo đã được ban hành, không phải nơi hiển thị đề xuất vừa gửi. Trong video, danh sách này đã rỗng từ trước khi bấm gửi. Đề xuất vừa gửi nằm ở màn hình danh sách đề xuất đào tạo.
- Tài khoản đã dùng để kiểm: một tài khoản Doanh nghiệp (người gửi) và một tài khoản Cán bộ nghiệp vụ thuộc đúng đơn vị tiếp nhận (người xem).
```

---

## row 119 — QLLKHDTBD_09

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Xuất Excel với điều kiện lọc
```

**Điều kiện:**
```
1. Đăng nhập tài khoản
```

**Các bước thực hiện:**
```
1. Chọn menu "Đào tạo, tập huấn" -> "Kế hoạch đào tạo"
2. Bấm nút "Gửi phê duyệt"
3. Nhập tiêu chí lọc và nhấn Xuất excel
```

**Kết quả mong đợi:**
```
Hệ thống xuất danh sách bài giảng theo điều kiện lọc hiện tại ra tệp Excel.
```

**Kết quả thực tế:**
```
Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Đã kiểm tra lại đúng điều kiện phản ánh: vai trò Cán bộ Nghiệp vụ Trung ương (đơn vị Bộ Tư pháp - Trung ương), màn "Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách", tab "Tất cả", đặt đúng hai giá trị lọc trong phiếu là Từ ngày 01/07/2026 và Đến ngày 31/07/2026, các ô còn lại để trống, rồi bấm "Xuất Excel".
- Lỗi tái hiện: màn danh sách ghi "Hiển thị 1-1 / 1 kết quả" nhưng tệp Excel tải về có 13 dòng dữ liệu, tức toàn bộ danh sách. Trong đó 12 dòng là kế hoạch nằm hoàn toàn ngoài khoảng lọc, ví dụ 01/09/2026 - 31/12/2026 và 01/01/2026 - 31/12/2026.
- Đã đo thêm một bộ lọc thứ hai theo chiều khác để loại trừ trùng số ngẫu nhiên: lọc theo từ khoá tên kế hoạch "RECON" cho 2 kết quả trên màn, tệp Excel vẫn ra đúng 13 dòng, trong đó 11 dòng không hề chứa từ khoá này.
- Mốc đối chứng: khi không đặt bộ lọc nào, số kết quả trên màn và số dòng trong tệp bằng nhau. Cộng với hai phép đo trên, có thể khẳng định tệp luôn lấy trọn danh sách bất kể bộ lọc đang đặt.
- Đã mở tệp ra đếm số dòng bằng hai cách độc lập (đọc thẳng nội dung tệp trong trình duyệt và mở tệp đã tải về bằng công cụ đọc bảng tính), hai cách cho cùng một con số.
- Kỳ vọng theo đặc tả FR-III-14 (UC33) - Lập kế hoạch đào tạo năm:
  + Mục Màn hình SCR-III-00, Thành phần 1 (srs-fr-03-dao-tao.md dòng 1752): nút "Xuất Excel" phải "xuất danh sách KH theo bộ lọc, tối đa 10.000 dòng".
  + Mục Processing - Xuất Excel (srs-fr-03-dao-tao.md dòng 1147, bước 2 tại dòng 1152): "Lấy danh sách theo filter, tối đa 10.000 dòng".
  + Quy tắc BR-DATA-06 (srs-v3.5.md dòng 5524), phạm vi "Toàn bộ CRUD list": "File xuất theo bộ lọc hiện tại, không vượt quá 10.000 rows/file". Phần giới hạn 10.000 dòng đang đạt, phần "theo bộ lọc hiện tại" chưa đạt.
- Ghi chú thêm: điều kiện lọc CÓ được gửi lên khi bấm xuất tệp, nên phần cần xử lý nằm ở bước dựng dữ liệu cho tệp chứ không phải ở bước gửi điều kiện.
- Phạm vi đã chốt: case này chỉ xét số bản ghi trong tệp có khớp bộ lọc hay không. Danh sách cột và định dạng bên trong tệp không thuộc phạm vi vì đặc tả không quy định.
- Mã lỗi: BUG-QLLKHDTBD_09.
- Verify: tài khoản Cán bộ Nghiệp vụ Trung ương (đơn vị Bộ Tư pháp - Trung ương), bản dựng V1.0.5, ngày 03/08/2026.
```

---

## row 121 — CBKQDTBD_01

- **Tên chức năng:** Công bố kết quả đào tạo bồi dưỡng
- **Tác nhân (đối tác ghi):** Cán  bộ 
 TW,BN,ĐP
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Cung cấp chức năng công bố kết quả, cập nhật kết quả vào tài khoản của học viên.
```

**Điều kiện:**
```
1. Đăng nhập tài khoản 
2. Khóa học ở trạng thái "Hoàn thành" và có học viên có kết quả đã được phê duyệt.
```

**Các bước thực hiện:**
```
1. Chọn menu "Đào tạo, tập huấn" -> "Khóa học"
2. Nhấn xem chi tiết khóa học
3. Chọn tab "Công bố kết quả"
4. Chọn danh sách học viên và bấm nút "Công bố"
```

**Kết quả mong đợi:**
```
Hợp lệ, hệ thống hiển thị thông báo "Đã công bố kết quả cho {số lượng} học viên".
```

**Kết quả thực tế:**
```
Màn hình chi tiết không có tab riêng"Công bố kết quả"
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
☑️ Đã kiểm tra lại — lỗi đã được khắc phục.
- Chức năng công bố kết quả đào tạo (UC38) nay đã có tab riêng "Công bố kết quả" trên màn hình chi tiết khóa học, nằm giữa tab "Kết quả" và tab "Bài giảng đã gán".
- Điều kiện để nhìn thấy và dùng được tab: đăng nhập bằng tài khoản Cán bộ nghiệp vụ đúng đơn vị của khóa học, mở chi tiết khóa học đó. Tab hiển thị ở mọi trạng thái khóa học; riêng việc công bố chỉ có ý nghĩa khi khóa học đã "Hoàn thành" và đã có học viên được duyệt kết quả.
- Đã thử trực tiếp trên khóa học "Tập huấn pháp lý cấp Trung ương 2026" ở trạng thái "Hoàn thành", có 4 học viên đã được duyệt kết quả, bằng tài khoản Cán bộ nghiệp vụ Trung ương:
  + Bấm "Công bố tất cả": hệ thống hỏi xác nhận, sau khi đồng ý thì cả 4 học viên chuyển sang "Đã công bố" và có ghi thời điểm công bố.
  + Bấm "Hủy công bố tất cả": hệ thống bắt nhập lý do tối thiểu 10 ký tự, sau khi nhập thì cả 4 học viên chuyển về "Chưa công bố".
- Trong tab còn có công tắc "Công bố lên Cổng PLQG" và nút công bố/hủy công bố cho từng học viên.
- Đề nghị đối tác mở lại màn hình chi tiết khóa học để kiểm tra và xác nhận giúp.
```

---

## row 124 — CNDSMLTVV_01

- **Tên chức năng:** Cập nhật danh sách mạng lưới tư vấn viên
- **Tác nhân (đối tác ghi):** Cán  bộ  nghiệp  vụ 
 TW,BN,ĐP
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Thực hiện cập nhật danh sách các tư vấn viên đã được phê duyệt lên Cổng công khai.
```

**Điều kiện:**
```
1. Đăng nhập tài khoản 
2. Hồ sơ đang ở trạng thái "Đang hoạt động" và chưa được công khai
```

**Các bước thực hiện:**
```
1. Chọn menu "Mạng lướt tư vấn viên" -> "Tư vấn viên/Chuyên gia"
2. Tích chọn các ứng viên hợp lệ
3. Nhấn "Công khai hàng loạt" và Xác nhận
```

**Kết quả mong đợi:**
```
- Hệ thống hiển thị cửa sổ nhập mô tả công khai (bắt buộc) áp cho các tư vấn viên đã chọn và xác nhận "Công khai {N} tư vấn viên đã chọn lên Cổng pháp luật quốc gia?"
- Lưu mô tả công khai, đặt cờ công khai, chuyển trạng thái công khai, ghi thời điểm.
```

**Kết quả thực tế:**
```
Hệ thống không mở cửa sổ nhập mà hiển thị thông báo "Mô tả công khai là bắt buộc trước khi đẩy lên Cổng pháp luật quốc gia"
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
☑️ Đã kiểm tra lại — chức năng chạy đúng.
- Kiểm tra lại bằng vai trò Cán bộ Nghiệp vụ Trung ương, đúng tiền đề của phiếu: chọn các tư vấn viên đang ở trạng thái "Đang hoạt động" và chưa được công khai.
- Chọn 2 tư vấn viên rồi bấm "Công khai lên Cổng PLQG": hệ thống MỞ cửa sổ nhập như mong đợi, tiêu đề "Công khai hàng loạt lên Cổng PLQG", kèm đúng câu xác nhận "Công khai 2 tư vấn viên đã chọn lên Cổng pháp luật quốc gia?".
- Trong cửa sổ có ô "Mô tả công khai" gắn dấu bắt buộc, giới hạn 5000 ký tự.
- Nếu để trống mô tả rồi bấm "Công khai": hệ thống báo lỗi ngay tại ô nhập ("Vui lòng nhập mô tả công khai") và giữ nguyên cửa sổ, không gửi dữ liệu đi. Đây là chỗ khác với lần bên kiểm thử gặp: thông báo thiếu mô tả nay nằm trong cửa sổ nhập, không còn bắn ra ngoài màn danh sách.
- Nhập mô tả rồi bấm "Công khai": lưu thành công, thông báo "Đã công khai tư vấn viên thành công", cả 2 hồ sơ chuyển từ "Chưa công khai" sang "Công khai".
- Kiểm tra thêm ở màn chi tiết tư vấn viên: nút công khai cũng mở đúng cửa sổ nhập, có thêm phần đính kèm tệp và tự điền lại mô tả đã nhập trước đó.
- Chức năng Cập nhật danh sách mạng lưới tư vấn viên (UC46) hiện hoạt động bình thường. Đề nghị bên kiểm thử xác nhận lại trên bản mới nhất.
- Verify: tài khoản Cán bộ Nghiệp vụ Trung ương, bản dựng V1.0.5, ngày 03/08/2026.
```

---

## row 128 — QLHSVV_07

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Tải tệp
```

**Điều kiện:**
```
1. Đăng nhập tài khoản 
2. Tồn tại bản ghi chứa tệp đính kèm
```

**Các bước thực hiện:**
```
1. Chọn menu "Vụ việc HTPL"
2. Tìm kiếm và nhấn nút Chỉnh sửa tại dòng bản ghi
3. Bấm "Tải"
```

**Kết quả mong đợi:**
```
Hệ thống tải tệp về máy người dùng.
```

**Kết quả thực tế:**
```
Nhấn vào biểu tượng "Tải xuống" hệ thống hiển thị màn hình xem chi tiết
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
☑️ Đã kiểm tra lại — chức năng chạy đúng.
- Kiểm tra lại bằng vai trò Cán bộ Nghiệp vụ Trung ương, đúng tiền đề của phiếu: hồ sơ vụ việc đã tiếp nhận và có tệp đính kèm (tệp ảnh JPG, đã quét sạch) — quản lý hồ sơ vụ việc (UC57).
- Trên hàng tệp trong nhóm "Tài liệu đính kèm", cột "Thao tác" nay có HAI nút tách riêng: nút "Xem" (hình con mắt) và nút "Tải" (hình mũi tên tải xuống). Hai nút làm hai việc khác nhau.
- Bấm "Tải": hệ thống tải tệp về máy người dùng. Đã kiểm tệp nhận được có kích thước và nội dung y hệt tệp đã đính kèm, không sai lệch. Màn hình vẫn đứng nguyên ở trang Chi tiết vụ việc, không mở màn xem nào.
- Bấm "Xem": mới là nút mở khung xem trước tệp ngay trong trang (có phóng to, xoay ảnh), và không tải tệp về máy.
- Lặp lại thao tác "Tải" 3 lần, trong đó 2 lần sau khi tải lại trang và xóa sạch tệp cũ trong thư mục Tải xuống: cả 3 lần tệp đều về máy đầy đủ.
- Kết luận: không còn tình trạng bấm biểu tượng tải xuống mà hệ thống lại mở màn hình xem. Phiếu này đạt.
```

---

## row 129 — TKHSYCHTPL_03

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Tìm kiếm bộ lọc có kết quả
```

**Điều kiện:**
```
1. Đăng nhập tài khoản 
2. Tồn tại bản ghi phù hợp với tiêu chí tìm kiếm
```

**Các bước thực hiện:**
```
1. Chọn menu "Vụ việc HTPL"
2. Tìm kiếm bộ lọc có kết quả
```

**Kết quả mong đợi:**
```
Có kết quả, hệ thống hiển thị danh sách kết quả tìm kiếm, phân trang 20 bản ghi mỗi trang.
```

**Kết quả thực tế:**
```
Khi chọn Mức SLA là "Sắp hết hạn" hệ thống hiển thị thông báo lỗi
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
☑️ Đã kiểm tra lại — lỗi không còn, chức năng chạy đúng.
- Đã kiểm tra lại đúng điều kiện phản ánh: vai trò Cán bộ Nghiệp vụ Trung ương, đơn vị Bộ Tư pháp - Trung ương, màn "Vụ việc HTPL", tab "Tất cả", các ô lọc khác để trống, chỉ chọn ô "Mức SLA" = "Sắp hết hạn".
- Kết quả: hệ thống KHÔNG còn hiện thông báo lỗi. Danh sách trả về 2 hồ sơ, dòng tổng ghi "Hiển thị 1-2 / 2 kết quả", mỗi trang 20 bản ghi đúng như phiếu mong đợi.
- Để chắc chắn không kết luận vội, tổ kiểm thử đã chạy đủ cả 5 phép đo trên cùng một phiên chứ không chỉ bấm một giá trị:
  + Không lọc: 37 hồ sơ.
  + "Bình thường": 30 hồ sơ, không có thông báo lỗi.
  + "Sắp hết hạn": 2 hồ sơ, không có thông báo lỗi.
  + "Quá hạn": 5 hồ sơ, không có thông báo lỗi.
  + "Quá hạn nghiêm trọng": 0 hồ sơ, hiện màn rỗng hợp lệ "Không tìm thấy hồ sơ phù hợp", cũng không có thông báo lỗi.
  Cộng lại 30 + 2 + 5 + 0 = 37, khớp đúng tổng số hồ sơ khi không lọc, tức bộ lọc chia nhóm đúng và không sót hồ sơ nào.
- Đã dùng bộ đo thông báo dùng chung của tổ kiểm thử (không lọc trùng, chỉ đọc chữ người dùng nhìn thấy, có tự kiểm chỉ một bộ đo đang chạy): số khung thông báo lỗi đếm được ở cả 4 giá trị đều bằng 0. Ảnh chụp ngay sau khi bấm "Tìm kiếm" cũng không bắt được khung thông báo nào.
- Đã tải lại trang bỏ bộ nhớ đệm rồi lặp lại đúng thao tác "Sắp hết hạn" một lần nữa, kết quả không đổi — loại trừ khả năng cửa sổ trình duyệt còn chạy bản cũ.
- Nguyên nhân lỗi cũ đã được xác định và đã được khắc phục ở phần giao diện: bản đối tác quay là bản dựng V1.0.2, khi chọn "Sắp hết hạn" thì giao diện gửi lên máy chủ một mã mức cảnh báo viết khác với mã hệ thống công nhận, nên bị từ chối và không ra kết quả. Bản hiện tại V1.0.5 gửi đúng mã, nên lọc ra kết quả bình thường.
- Chức năng Tìm kiếm hồ sơ vụ việc (UC 58) hiện hoạt động đúng. Đề nghị bên kiểm thử xác nhận lại trên bản mới nhất.
- Verify: tài khoản Cán bộ Nghiệp vụ Trung ương (đơn vị Bộ Tư pháp - Trung ương), bản dựng V1.0.5, ngày 03/08/2026.
```

---

## row 130 — KTDGKQHT_20

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Tỷ lệ chuyên cần trên tab "Kết quả" tính sai mẫu số — lấy số buổi đã điểm danh thay vì tổng số buổi của khóa
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ Trung ương (cbnv_tw)
2. Có khóa học ở trạng thái "Đang diễn ra", có học viên đăng ký
3. Khóa học có NHIỀU buổi trong tab "Lịch học" nhưng mới điểm danh MỘT phần số buổi
```

**Dữ liệu đầu vào:**
```
Khóa học KH-QAW7-HOINGHI "QAW7 — Hội nghị đối thoại DN 2026" (Đang diễn ra, 2 học viên).
Lịch học: 3 buổi (10/05/2026 08:00-10:00; 10/05/2026 14:00-16:00; 11/05/2026 08:00-10:00).
Đã điểm danh 1/3 buổi: học viên 1 = "Vắng có phép", học viên 2 = "Có mặt".
```

**Các bước thực hiện:**
```
1. Chọn menu "Đào tạo, tập huấn" -> "Khóa học"
2. Mở chi tiết khóa học đang diễn ra
3. Vào tab "Lịch học", thêm 3 buổi học
4. Vào tab "Điểm danh", chọn buổi 1, chấm điểm danh cho các học viên rồi nhấn [Lưu điểm danh]
5. Vào tab "Kết quả", đọc ô "Chuyên cần" của từng học viên
6. Nhấn [Xuất DOCX] và mở file để đối chiếu cột "Tổng số buổi" và "Tỉ lệ chuyên cần (%)"
```

**Kết quả mong đợi:**
```
Mẫu số phải là TỔNG SỐ BUỔI CỦA KHÓA (3), theo công thức tỷ lệ chuyên cần = (số buổi Có mặt + số buổi Vắng có phép) / tổng số buổi x 100 (FR-III-05 (UC24) §Quy tắc nghiệp vụ BR-KQ-02, srs-fr-03-dao-tao.md dòng 2251).
Với dữ liệu trên, cả 2 học viên phải là 33.33%: học viên 1 = (0+1)/3, học viên 2 = (1+0)/3.
```

**Kết quả thực tế:**
```
Mẫu số đang là SỐ BUỔI ĐÃ ĐIỂM DANH (1) chứ không phải tổng số buổi của khóa (3).
Tab "Kết quả" hiển thị: học viên 1 "0/1 (100.00%)", học viên 2 "1/1 (100.00%)" — trong khi khóa có 3 buổi.
Đã đo bằng 3 cách độc lập, cùng ra một kết quả:
- Giao diện tab "Kết quả": ô Chuyên cần = 0/1 (100.00%) và 1/1 (100.00%)
- File DOCX xuất từ nút [Xuất DOCX] (mở file đọc nội dung): cột "Tổng số buổi" = 1, "Tỉ lệ chuyên cần (%)" = 100.00
- Dữ liệu máy chủ trả về cho màn hình: tongBuoi = 1, tyLeChuyenCan = "100.00", trong khi danh sách lịch học của chính khóa đó trả về 3 buổi
Tác động: ngưỡng chuyên cần tối thiểu mặc định là 80%. Học viên mới dự 1/3 buổi vẫn được tính 100% nên vượt ngưỡng, dẫn tới kết luận Đạt/Không đạt của khóa học bị sai.
Môi trường: bản dựng V1.0.5, tài khoản cbnv_tw.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Lỗi do QA phát hiện thêm khi verify KTDGKQHT_02 ngày 03/08/2026, không nằm trong phạm vi phiếu gốc nên mở dòng riêng.
- Web đang sai: tỷ lệ chuyên cần trên tab "Kết quả" lấy mẫu số là SỐ BUỔI ĐÃ ĐIỂM DANH thay vì TỔNG SỐ BUỔI CỦA KHÓA. Khóa có 3 buổi trong lịch học, mới điểm danh 1 buổi thì màn hình hiện "0/1 (100.00%)" và "1/1 (100.00%)".
- Đúng theo đặc tả phải là 33.33% cho cả 2 học viên: FR-III-05 (UC24) §Quy tắc nghiệp vụ BR-KQ-02 (srs-fr-03-dao-tao.md dòng 2251) quy định tỷ lệ chuyên cần = (số buổi Có mặt + số buổi Vắng có phép) / tổng số buổi × 100.
- Đã đo bằng 3 cách độc lập, cùng một kết quả: giao diện tab Kết quả; nội dung file DOCX xuất ra (cột "Tổng số buổi" = 1); dữ liệu máy chủ trả về cho màn hình (tổng số buổi = 1 trong khi lịch học của chính khóa đó có 3 buổi).
- Mức độ ảnh hưởng: ngưỡng chuyên cần tối thiểu mặc định là 80%. Học viên mới dự 1/3 buổi vẫn được tính 100% nên vượt ngưỡng, dẫn tới kết luận Đạt/Không đạt của khóa học bị sai.
- Dữ liệu kiểm tra: khóa học KH-QAW7-HOINGHI (Đang diễn ra, 2 học viên, lịch học 3 buổi, đã điểm danh 1 buổi). Tài khoản cbnv_tw. Bản dựng V1.0.5.
```

---

## row 131 — NHSYC_OOS_01

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Nhập hồ sơ vụ việc thủ công — QA phát hiện ngoài phạm vi tiêu chí của phiếu (phát sinh khi verify NHSYC_01): một lần bấm nút lưu bị lỗi thì hệ thống hiển thị CÙNG LÚC HAI thông báo lỗi với hai câu chữ khác nhau, trong khi chỉ có một lần gửi dữ liệu lên máy chủ. Mã bug trong báo cáo QA: BUG-NHSYC_01 (phần thông báo).
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ Trung ương (cbnv_tw_03)
2. Đang ở màn "Thêm mới Hồ sơ Vụ việc" (Vụ việc HTPL -> Nhập thủ công)
3. Thao tác lưu rơi vào nhánh lỗi (ví dụ hồ sơ có tệp đính kèm)
```

**Dữ liệu đầu vào:**
```
Hồ sơ điền đủ trường bắt buộc, doanh nghiệp Cong ty TNHH QA UAT Kiem Thu (MST 0109998887), kênh tiếp nhận Trực tiếp, ngày tiếp nhận để mặc định, có đính kèm 1 tệp PDF 614 B.
```

**Các bước thực hiện:**
```
1. Chọn menu "Vụ việc HTPL"
2. Nhấn [+ Nhập thủ công]
3. Điền đủ thông tin hợp lệ và đính kèm 1 tệp PDF
4. Nhấn [Lưu & Tiếp nhận]
5. Quan sát vùng thông báo ở đỉnh màn hình
```

**Kết quả mong đợi:**
```
Một thao tác chỉ hiển thị MỘT thông báo kết quả. Người dùng nhận đúng một thông điệp, không phải hai câu chữ khác nhau cho cùng một sự việc.
```

**Kết quả thực tế:**
```
Một lần bấm nút sinh HAI khung thông báo lỗi hiện cùng lúc, nội dung khác nhau:
- "Lỗi hệ thống, vui lòng thử lại sau."
- "Có lỗi xảy ra. Vui lòng thử lại sau."

Đo bằng công cụ bắt thông báo dùng chung của QA (không lọc trùng, chỉ đọc chữ người dùng nhìn thấy, có tự kiểm chỉ 1 bộ đo đang chạy): 1 lần gửi dữ liệu lên máy chủ -> 2 khung thông báo. Đã đối chứng thêm bằng cách đọc trực tiếp nội dung đang hiển thị trên màn hình (2 khung) và chụp được ảnh có đủ 2 khung.

Tái hiện 3/3 lần, trong đó 1 lần sau khi tải lại trang bỏ bộ nhớ đệm. Ghi nhận trên bản dựng V1.0.5.

Lưu ý: đây là lỗi hiển thị thông báo, tách khỏi lỗi nghiệp vụ không tạo được hồ sơ đã ghi ở dòng NHSYC_01.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
Đã fix: 1 request lỗi = 1 toast (bỏ toast thủ công ở catch, để hook onError là nguồn duy nhất). Commit a69f48fc3. Verify local 3/3 + 120 (MutationObserver = 1 toast).
```

---

## row 132 — QLKTLBG_10

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Xem bài giảng/tài liệu chứa PDF
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ
2. Có bài giảng Loại tài liệu = PDF, tệp .pdf hợp lệ, trạng thái Đã công khai
```

**Dữ liệu đầu vào:**
```
Bài giảng "QA VERIFY 03/08 - QLKTLBG_10 PDF that cong khai" — Loại tài liệu PDF, tệp QLKTLBG_10-pdf-that-QA.pdf (PDF hợp lệ 2 trang, có chữ đọc được, 979 B), Đã công khai 03/08/2026 16:09
```

**Các bước thực hiện:**
```
1. Chọn menu "Đào tạo, tập huấn" -> "Kho tài liệu / Bài giảng"
2. Bấm [+ Thêm mới], chọn Loại tài liệu = PDF, tải lên tệp .pdf hợp lệ, bật Công khai, bấm [Thêm mới]
3. Trên dòng bài giảng vừa tạo, bấm biểu tượng con mắt (Xem trước)
4. Quan sát khu vực xem trước bên dưới khối Công khai / Ảnh đại diện / Mô tả công khai
```

**Kết quả mong đợi:**
```
Hệ thống mở khu vực xem trước nội dung với PDF: hiển thị nội dung PDF inline (FR-III-07 (UC26) §Tiêu chí chấp nhận dòng 792; SCR-III-03 §Thành phần 6 - Bảng xem trước dòng 1955: "Slide/PDF xem trực tiếp trong trình duyệt").
```

**Kết quả thực tế:**
```
KHÔNG hiển thị được nội dung PDF. Hộp thoại "Xem trước" mở ra nhưng khu vực xem trước chỉ hiện biểu tượng tệp lỗi của trình duyệt kèm dòng chữ "18.143.165.120.nip.io refused to connect.", không có trang PDF nào.

Hệ thống cũng KHÔNG hiển thị thông báo thay thế "Không thể xem trực tuyến" và KHÔNG có nút "Tải về" (hộp thoại chỉ có đúng 1 nút đóng), nên không có cách nào xem hay tải nội dung bài giảng từ màn này. Cột Thao tác của bảng cũng chỉ có xem trước / Sửa / Xóa, thiếu "Tải về" mà SCR-III-03 §Thành phần 4 (dòng 1951) yêu cầu.

Tái hiện 3/3 lần trên 3 bài giảng PDF khác nhau, trong đó có 1 tệp PDF hợp lệ 2 trang do tổ kiểm thử tự tạo mới qua luồng Thêm mới, nên không phải do tệp cũ hỏng.

Phía máy chủ: tệp PDF được trả về kèm thiết lập chặn nhúng trang (x-frame-options: DENY và content-security-policy: frame-ancestors 'none'), nên khung xem trước bị trình duyệt chặn tải nội dung.

Đối chứng cùng màn, cùng tài khoản: bài giảng loại Video vẫn nhúng và phát được khung YouTube, chứng tỏ khu vực xem trước hoạt động; chỉ tệp lưu trên hệ thống (PDF và Slide) là không hiển thị được.

(Lỗi do tổ kiểm thử phát hiện thêm khi verify case QLKTLBG_09 ngày 03/08/2026 — đối tác chỉ phản ánh loại Slide, không có dòng nào cho loại PDF nên mở dòng mới.)
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
Đã fix (cùng gốc QLKTLBG_09, loại PDF): PDF render inline qua blob same-origin (né x-frame-options/CSP frame-ancestors) + fallback "Không thể xem trực tuyến"+Tải (SRS:1955) + nút Tải về cột Thao tác (SRS:1951). Commit e2a0dea4. Verify local + 120 PASS (blob không bị CSP chặn).
```

---

## row 133 — QLHSVV_OOS_01

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Cột "Loại" của bảng tài liệu đính kèm trong hồ sơ vụ việc hiển thị mã nội bộ thô thay vì chữ tiếng Việt
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ
2. Có hồ sơ vụ việc chứa ít nhất 1 tệp đính kèm
```

**Dữ liệu đầu vào:**
```
Vụ việc VV-BTP-TW-20260803-002 (trạng thái Đã tiếp nhận, đơn vị Bộ Tư pháp - Trung ương), tệp đính kèm QLHSVV_07_qa.jpg (ảnh JPG 38.8 KB, quét sạch, tải lên 03/08/2026 16:13)
```

**Các bước thực hiện:**
```
1. Chọn menu "Vụ việc HTPL"
2. Mở một hồ sơ có tệp đính kèm (nhấn vào dòng bản ghi)
3. Bung nhóm "Tài liệu đính kèm"
4. Đọc giá trị ở cột "Loại" trên hàng tệp
```

**Kết quả mong đợi:**
```
Cột "Loại" hiển thị chữ tiếng Việt dễ hiểu cho người dùng (ví dụ "Bổ sung"), thống nhất với cách các cột khác cùng bảng đang làm và với cách phần mềm đặt tên sự kiện ở Dòng thời gian.
```

**Kết quả thực tế:**
```
Cột "Loại" hiển thị nguyên mã nội bộ viết hoa có gạch dưới: BO_SUNG. Người dùng nghiệp vụ không hiểu đây là loại tài liệu gì.

So sánh ngay trong CÙNG một hàng của CÙNG bảng đó cho thấy đây là chỗ bị bỏ sót chứ không phải quy ước chung: cột "Trạng thái quét" đã được đổi sang tiếng Việt là "Sạch", cột "Định dạng" hiển thị "JPG". Ngoài ra khối "Dòng thời gian" ngay bên dưới cùng màn hình đã gọi đúng nghiệp vụ này là "Bổ sung hồ sơ", chứng tỏ phần mềm đã có sẵn cách diễn đạt tiếng Việt cho khái niệm này.

Lỗi hiển thị ở mọi lần mở màn hình (kiểm 3/3 lần, có 2 lần sau khi tải lại trang bỏ bộ nhớ đệm), không phụ thuộc thao tác.

(Lỗi do tổ kiểm thử phát hiện thêm khi verify case QLHSVV_07 ngày 03/08/2026 - phiếu QLHSVV_07 chỉ nói về nút Tải, không có dòng nào cho phần hiển thị cột Loại nên mở dòng mới.)
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
Đã fix: cột "Loại" bảng tài liệu đính kèm map enum LoaiTaiLieu→nhãn VN (BO_SUNG→"Bổ sung"). Commit f9094d559. Verify local + 120 PASS.
```

---

## row 134 — QLDXDTTH_10

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Tab "Đề xuất đào tạo" (màn Chương trình đào tạo) thiếu cột "Người đề xuất".
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ
2. Đơn vị của cán bộ có ít nhất 1 đề xuất đào tạo do Doanh nghiệp gửi
```

**Dữ liệu đầu vào:**
```
Đề xuất do DN "QA UAT Kiem Thu DN" gửi ngày 03/08/2026, nội dung bắt đầu bằng QA-VERIFY-0803, trạng thái "Mới gửi".
```

**Các bước thực hiện:**
```
1. Vào Đào tạo, tập huấn -> Chương trình đào tạo
2. Chọn tab "Đề xuất đào tạo"
3. Xem danh sách, cuộn hết thanh ngang của bảng
4. Bấm vào nội dung đề xuất để mở màn chi tiết
```

**Kết quả mong đợi:**
```
Bảng đề xuất có cột "Người đề xuất" để cán bộ biết đề xuất là của doanh nghiệp / người hỗ trợ nào.
Căn cứ: FR-III-13 (UC32) §Đặc tả màn hình SCR-III-01 - Thành phần 8 (dòng 1875) liệt kê cột: Lĩnh vực, Nội dung, Người đề xuất, Trạng thái, Ngày tạo, Hành động.
```

**Kết quả thực tế:**
```
Không có cột "Người đề xuất". Bảng chỉ có 8 cột: Nội dung, Lĩnh vực, Thời gian mong muốn, Địa điểm mong muốn, SL dự kiến, Trạng thái, Ngày tạo, Hành động. Đã cuộn hết thanh ngang để chắc chắn không phải cột bị khuất. Màn chi tiết đề xuất cũng không hiển thị người đề xuất. Cán bộ không biết đề xuất là của ai.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
Đã fix: thêm cột "Người đề xuất" (họ tên + đơn vị) ở bảng + chi tiết (SCR-III-01:1875); BE entity relation + join. Commit 80ccfb1c9. Verify local + 120 PASS.
```

---

## row 136 — QLDXDTTH_12

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Màn gửi đề xuất và màn chi tiết đề xuất lộ mã kỹ thuật của lĩnh vực ra cho người dùng.
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Doanh nghiệp hoặc Cán bộ nghiệp vụ
```

**Dữ liệu đầu vào:**
```
Danh mục lĩnh vực pháp luật đang có 10 giá trị.
```

**Các bước thực hiện:**
```
1. Vào Đào tạo, tập huấn -> Chương trình đào tạo -> tab "Đề xuất đào tạo"
2. Bấm "Gửi đề xuất mới", mở ô chọn "Lĩnh vực"
3. Mở màn chi tiết của một đề xuất bất kỳ, xem dòng "Lĩnh vực"
```

**Kết quả mong đợi:**
```
Người dùng chỉ nhìn thấy tên lĩnh vực bằng tiếng Việt, ví dụ "Dân sự", "Thuế", "Lao động" - giống như cột "Lĩnh vực" ở bảng danh sách đang hiển thị đúng.
```

**Kết quả thực tế:**
```
Ô chọn lĩnh vực hiển thị kèm mã kỹ thuật: "DAN_SU - Dân sự", "THUE - Thuế", "LAO_DONG - Lao động", "SHTT - Sở hữu trí tuệ"... Màn chi tiết đề xuất cũng hiển thị "Lĩnh vực: DAN_SU - Dân sự". Trong khi đó cột "Lĩnh vực" của bảng danh sách lại hiển thị đúng là "Dân sự" - tức là không nhất quán ngay trong cùng một chức năng.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
Đã fix: ô chọn Lĩnh vực + bộ lọc + chi tiết chỉ hiển thị tên tiếng Việt (bỏ prefix mã "DAN_SU -"). Commit 04652b4e6. Verify local; bundle 120 live.
```

---

## row 137 — QLDXDTTH_13

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Thông báo "Đề xuất đào tạo mới" hiển thị bằng biểu tượng báo lỗi (dấu X đỏ) thay vì biểu tượng thông tin.
```

**Điều kiện:**
```
1. Doanh nghiệp vừa gửi một đề xuất đào tạo
2. Đăng nhập tài khoản Cán bộ nghiệp vụ thuộc đơn vị tiếp nhận
```

**Dữ liệu đầu vào:**
```
Đề xuất QA-VERIFY-0803 gửi lúc 16:22 ngày 03/08/2026.
```

**Các bước thực hiện:**
```
1. Đăng nhập Cán bộ nghiệp vụ của đơn vị tiếp nhận
2. Bấm biểu tượng chuông thông báo trên thanh đầu trang
3. Nhìn biểu tượng bên trái dòng "Đề xuất đào tạo mới" và so với các dòng thông báo khác
```

**Kết quả mong đợi:**
```
Thông báo báo tin có đề xuất mới là thông báo thông tin bình thường, nên dùng biểu tượng trung tính hoặc biểu tượng thông tin, không dùng biểu tượng báo lỗi.
```

**Kết quả thực tế:**
```
Dòng "Đề xuất đào tạo mới - Có đề xuất đào tạo mới từ người dùng QA UAT Kiem Thu DN" hiển thị biểu tượng dấu X trong vòng tròn màu đỏ, giống hệt biểu tượng báo lỗi. Bốn dòng thông báo còn lại trong cùng danh sách đều dùng dấu tích xanh. Cán bộ dễ hiểu nhầm là hệ thống đang có sự cố.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
Đã fix (hệ thống): thông báo HE_THONG đổi icon CloseCircle đỏ → InfoCircle xanh (phủ mọi thông báo hệ thống: đề xuất mới/kích hoạt TK/đăng nhập/đổi MK). Commit cc1af6b4e. Verify local; bundle 120 live.
```

---

## row 138 — DKTGMLTVV_OOS_01

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Đăng ký tham gia mạng lưới — ràng buộc bắt buộc của ô "Số thẻ hành nghề" khi Loại = Tư vấn viên
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Người hỗ trợ pháp lý cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp
2. Mở màn hình Mạng lưới Tư vấn viên -> Tư vấn viên / Chuyên gia -> Thêm mới
```

**Dữ liệu đầu vào:**
```
Hồ sơ "QA OOS01 Khong So The Hanh Nghe" — Loại = Tư vấn viên (TVV), Ngày sinh 01/01/1988, Giới tính Nam, Số CMND/CCCD 038119880501, Email qa.oos01.thehanhnghe@htpldn.test, Điện thoại 0912340501, Địa chỉ So 1 pho QA Test Ba Dinh Ha Noi, Trình độ Cử nhân, Chuyên ngành Luat kinh te, Số năm kinh nghiệm 5, Lĩnh vực pháp luật Thương mại, File thẻ hành nghề = tệp PDF hợp lệ 605 B. Riêng ô "Số thẻ hành nghề" ĐỂ TRỐNG.
```

**Các bước thực hiện:**
```
1. Chọn menu "Mạng lưới Tư vấn viên" -> "Tư vấn viên / Chuyên gia", bấm [+ Thêm mới]
2. Chọn Loại = "Tư vấn viên (TVV)"
3. Quan sát ô "Số thẻ hành nghề" ở nhóm Nghề nghiệp — hệ thống có báo hiệu đây là thông tin bắt buộc không
4. Điền đủ mọi trường bắt buộc khác, tải lên File thẻ hành nghề, giữ ô "Số thẻ hành nghề" TRỐNG
5. Bấm [Lưu] và quan sát hệ thống có từ chối lưu hay không
```

**Kết quả mong đợi:**
```
Khi Loại = Tư vấn viên, hệ thống phải coi "Số thẻ hành nghề" là thông tin bắt buộc: cho người dùng biết đây là trường bắt buộc và từ chối lưu hồ sơ khi ô này để trống (SCR-IV-02 "Thêm mới / Chỉnh sửa Tư vấn viên" §Danh sách trường, dòng 1507: "Số thẻ hành nghề | ô văn bản | Bắt buộc nếu Loại = Tư vấn viên (theo NĐ 77/2008 Đ.20)").
```

**Kết quả thực tế:**
```
Hệ thống KHÔNG áp ràng buộc này. Ô "Số thẻ hành nghề" không được báo hiệu là bắt buộc, và bấm [Lưu] khi để trống thì hồ sơ LƯU THÀNH CÔNG: tạo ra hồ sơ TVV-BTP-TW-0031 "QA OOS01 Khong So The Hanh Nghe", Loại = Tư vấn viên, trạng thái "Mới đăng ký". Thao tác gửi 3 lệnh, hiện đúng 1 thông báo "Tạo hồ sơ TVV thành công", không có thông báo cản nào.

Mở lại hồ sơ vừa tạo ở màn hình chi tiết: ô "Số thẻ hành nghề" hiển thị "—" (không có dữ liệu), trong khi ô "Loại" là "Tư vấn viên" — đúng điều kiện mà đặc tả dòng 1507 yêu cầu bắt buộc.

Cơ chế chặn CÓ tồn tại và chạy đúng cho ô ngay bên cạnh: cùng biểu mẫu đó, lần bấm [Lưu] đầu tiên khi để trống "File thẻ hành nghề" thì hệ thống chặn ngay, không gửi lệnh nào ra máy chủ và báo "File thẻ hành nghề là bắt buộc đối với Tư vấn viên" (đặc tả dòng 1508 đặt cùng điều kiện "bắt buộc nếu Loại = Tư vấn viên"). Sau khi tải tệp lên, biểu mẫu chỉ còn đúng ô "Số thẻ hành nghề" trống và hồ sơ lưu được. Vậy đây là thiếu ràng buộc riêng cho ô "Số thẻ hành nghề", không phải do biểu mẫu chưa có cơ chế kiểm tra dữ liệu.

Kiểm hai chiều: đọc lại hồ sơ vừa tạo bằng giao diện chi tiết và bằng dữ liệu hệ thống trả về đều cho cùng kết quả (Loại = Tư vấn viên, số thẻ hành nghề rỗng).
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Yêu cầu theo đặc tả: SCR-IV-02 "Thêm mới / Chỉnh sửa Tư vấn viên" §Danh sách trường dòng 1507 — "Số thẻ hành nghề | ô văn bản | Bắt buộc nếu Loại = Tư vấn viên (theo NĐ 77/2008 Đ.20)".
- Dòng 1508 ngay kế bên đặt cùng điều kiện cho "File thẻ hành nghề" và đã được cài đúng (chặn được, có thông báo riêng), nên đây là bỏ sót đúng 1 ô chứ không phải thiếu cơ chế.
- Bằng chứng: hồ sơ TVV-BTP-TW-0031 lưu được với Loại = Tư vấn viên và số thẻ hành nghề rỗng.
- Mã lỗi nội bộ: BUG-DKTGMLTVV_OOS_01. Tài khoản kiểm tra: nht_qa_tw (Người hỗ trợ pháp lý, cấp Trung ương, đơn vị Cục Bổ trợ tư pháp). Bản dựng V1.0.5, kiểm tra ngày 03/08/2026.
- Lỗi phát hiện ngoài phạm vi các dòng TC có sẵn (không dòng DKTGMLTVV nào kiểm ràng buộc bắt buộc theo Loại) nên mở dòng mới.
```

---

## row 139 — DKTGMLTVV_OOS_02

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Đăng ký tham gia mạng lưới — nhãn trường trên biểu mẫu Thêm mới Tư vấn viên lệch so với đặc tả
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Người hỗ trợ pháp lý cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp
2. Mở màn hình Mạng lưới Tư vấn viên -> Tư vấn viên / Chuyên gia -> Thêm mới
```

**Dữ liệu đầu vào:**
```
Không cần nhập dữ liệu — chỉ đọc nhãn trên biểu mẫu còn trống.
```

**Các bước thực hiện:**
```
1. Chọn menu "Mạng lưới Tư vấn viên" -> "Tư vấn viên / Chuyên gia", bấm [+ Thêm mới]
2. Đọc tên nhóm thứ hai của biểu mẫu
3. Đọc nhãn ô nhập số giấy tờ tùy thân ở nhóm thông tin cá nhân
4. Đọc nhãn ô chọn trình độ ở nhóm thứ hai
5. Đối chiếu 3 nhãn trên với bảng Danh sách trường của SCR-IV-02
```

**Kết quả mong đợi:**
```
Nhãn hiển thị đúng như đặc tả SCR-IV-02 "Thêm mới / Chỉnh sửa Tư vấn viên" §Danh sách trường:
- dòng 1500 — nhóm 2 tên là "Thông tin nghề nghiệp"
- dòng 1495 — mục 2.7 là "Số Căn cước công dân *"
- dòng 1503 — mục 3.1 là "Trình độ *"
```

**Kết quả thực tế:**
```
Cả 3 nhãn đều lệch so với đặc tả:
1. Tên nhóm 2 hiển thị "Nghề nghiệp" — đặc tả dòng 1500 ghi "Thông tin nghề nghiệp".
2. Nhãn ô giấy tờ tùy thân hiển thị "Số CMND/CCCD" — đặc tả dòng 1495 ghi "Số Căn cước công dân". Đây không chỉ là rút gọn chữ: Chứng minh nhân dân và Căn cước công dân là hai loại giấy tờ khác nhau, nhãn hiện tại cho hiểu là chấp nhận cả số CMND trong khi đặc tả chỉ nêu Căn cước công dân. Cùng chỗ này, màn hình chi tiết hồ sơ cũng hiển thị "CMND/CCCD".
3. Nhãn ô trình độ hiển thị "Trình độ học vấn" — đặc tả dòng 1503 ghi "Trình độ".

Đọc trực tiếp trên biểu mẫu còn trống nên không phụ thuộc dữ liệu thử. Trong 3 điểm trên, điểm 2 ảnh hưởng tới cách hiểu nghiệp vụ (loại giấy tờ được chấp nhận); điểm 1 và 3 là sai khác câu chữ.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
☑️ Đã kiểm tra lại — lỗi không còn, chuyển Pass.
- Kiểm lại ngày 03/08/2026 lúc 21:05 trên màn "Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → Thêm mới", tài khoản nht_qa_tw (Người hỗ trợ pháp lý, cấp Trung ương, Cục Bổ trợ tư pháp). Bản dựng V1.0.5, gói giao diện index-B1e0L2GY.js (khác gói lúc phát hiện lỗi).
- Cả 3 nhãn nay đã đúng đặc tả SCR-IV-02 "Thêm mới / Chỉnh sửa Tư vấn viên" §Danh sách trường:
  1. Tên nhóm 2 hiển thị "Thông tin nghề nghiệp" (dòng 1500) — trước hiển thị "Nghề nghiệp".
  2. Nhãn ô giấy tờ tùy thân hiển thị "Số Căn cước công dân" (dòng 1495) — trước hiển thị "Số CMND/CCCD".
  3. Nhãn ô trình độ hiển thị "Trình độ" (dòng 1503) — trước hiển thị "Trình độ học vấn".
- Rút lại đề nghị BA xác nhận đã nêu ở lần trước: đặc tả không mâu thuẫn ở điểm này. Mọi chuỗi hiển thị cho người dùng trong đặc tả đều dùng "Căn cước công dân" — nhãn và thông báo trùng ở dòng 1495, mã lỗi ERR-TVV-02 dòng 202, mã lỗi ERR-DK-04 dòng 337, gợi ý ô tìm kiếm dòng 1438, kiểm tra khi rời ô dòng 1527. Chữ "cmnd_cccd" chỉ còn tồn tại ở tên cột nội bộ, người dùng không nhìn thấy. Vậy đây chỉ là sai câu chữ trên nhãn, không phải thay đổi phạm vi giấy tờ được chấp nhận — không cần BA quyết.
- Ghi nhận thêm, KHÔNG tính là lỗi: ô nhập gợi ý "9-12 chữ số", trong khi đặc tả dòng 1495 chỉ quy định "tối đa 12 ký tự" nên không trái đặc tả. Nêu ra để bộ phận nghiệp vụ biết ô mang nhãn Căn cước công dân hiện vẫn nhận số 9 chữ số.
- Giữ nguyên phản hồi của dev ở lần trước: [DEV 03/08] Nhãn "Số CMND/CCCD" → đã đổi "Số Căn cước công dân" theo SCR-IV-02 :1495 (commit 16a54e26a). Đủ 3 nhãn đúng SRS → dev done.
```

---

## row 140 — CNDSMLTVV_OOS_01

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Công nhận / công khai danh sách mạng lưới — hủy công khai hàng loạt không hỏi xác nhận
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp
2. Ở tab "Đang hoạt động" của danh sách Tư vấn viên có ít nhất 1 hồ sơ đang ở trạng thái Công khai
```

**Dữ liệu đầu vào:**
```
Hồ sơ TVV-SEED-0001 "Nguyễn Văn Seed" — được công khai ngay trước đó bằng chính luồng công khai hàng loạt của phần mềm (mô tả công khai "QA kiem thu OOS lan 3 - 03/08/2026."), nên ở trạng thái Công khai khi bắt đầu bước đo.
```

**Các bước thực hiện:**
```
1. Chọn menu "Mạng lưới Tư vấn viên" -> "Tư vấn viên / Chuyên gia", tab "Đang hoạt động"
2. Tích chọn 1 dòng đang ở trạng thái Công khai
3. Bấm nút "Hủy công khai" trên thanh thao tác hàng loạt
4. Quan sát liên tục trong 2,2 giây kể từ lúc bấm: hệ thống có mở hộp thoại hỏi lại trước khi gỡ không
5. Đọc trạng thái của dòng sau khi thao tác kết thúc
```

**Kết quả mong đợi:**
```
Hệ thống phải hỏi lại người dùng trước khi gỡ thông tin khỏi Cổng pháp luật quốc gia. SCR-IV-01 §Thao tác hàng loạt dòng 1465: "Hủy công khai hàng loạt (tab "Đang hoạt động"): chọn dòng đã công khai -> nút "Hủy công khai" -> MD-HUY-CONG-KHAI". Mẫu MD-HUY-CONG-KHAI ở §3.0b dòng 1407 gồm tiêu đề "Xác nhận hủy công khai?", nội dung "Thông tin {tên} sẽ bị gỡ khỏi Cổng pháp luật quốc gia. Bạn có thể công khai lại bất kỳ lúc nào." và nút chính "Hủy công khai".
```

**Kết quả thực tế:**
```
Không có bước hỏi lại nào. Hệ thống gỡ công khai ngay khi bấm nút.

Đo tại 7 mốc thời gian sau khi bấm (50 / 150 / 300 / 600 / 1000 / 1500 / 2200 mili-giây): cả 7 mốc đều không có hộp thoại nào mở ra. Ngay tại mốc 50 mili-giây, lệnh gỡ công khai đã được gửi đi rồi — nghĩa là hệ thống không hề chờ người dùng xác nhận. Toàn thao tác gửi đúng 1 lệnh và hiện đúng 1 thông báo "Đã hủy công khai tư vấn viên thành công". Sau đó trạng thái dòng đổi thành "Chưa công khai".

Tái hiện 3/3 lần. Nút "Hủy công khai" nằm ngay cạnh nút "Công khai lên Cổng PLQG" trên cùng thanh thao tác, nên bấm nhầm là thông tin bị gỡ khỏi Cổng pháp luật quốc gia ngay, người dùng không có bước nào để dừng lại.

Đối chiếu trong cùng màn hình: chiều ngược lại (công khai hàng loạt) CÓ mở hộp thoại để người dùng xem lại trước khi xác nhận — nên việc thiếu bước hỏi lại chỉ xảy ra ở chiều hủy công khai.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Yêu cầu theo đặc tả: SCR-IV-01 §Thao tác hàng loạt dòng 1465 quy định luồng "Hủy công khai hàng loạt" phải đi qua MD-HUY-CONG-KHAI; mẫu hộp thoại MD-HUY-CONG-KHAI định nghĩa ở §3.0b dòng 1407.
- Bằng chứng đo: 7 mốc quan sát trong 2,2 giây đều không có hộp thoại; tại mốc 50 mili-giây lệnh gỡ công khai đã gửi. 1 lệnh - 1 thông báo, tái hiện 3/3.
- Ảnh kèm theo chụp thanh thao tác hàng loạt có nút "Hủy công khai" và dòng đang công khai được chọn (điểm vào của thao tác).
- Mã lỗi nội bộ: BUG-CNDSMLTVV_OOS_01. Tài khoản kiểm tra: cbnv_tw_02 (Cán bộ nghiệp vụ Trung ương, đơn vị Cục Bổ trợ tư pháp). Bản dựng V1.0.5, kiểm tra ngày 03/08/2026.
- Dữ liệu thử đã hoàn trả: hồ sơ TVV-SEED-0001 được đưa về đúng trạng thái ban đầu (Chưa công khai) sau khi đo.
- Lỗi phát hiện ngoài phạm vi các dòng TC có sẵn nên mở dòng mới.
```

---

## row 141 — CNKQHT_OOS_01

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Email thông báo "Kết quả hỗ trợ đã được cập nhật" mở đầu thân thư bằng dòng "Phân công:", nói sai bản chất sự kiện.
```

**Điều kiện:**
```
1. Vụ việc hỗ trợ pháp lý đang ở trạng thái Đang xử lý, đã phân công cho Tư vấn viên và người này đã xác nhận tham gia
2. Người phụ trách vụ việc là một Cán bộ nghiệp vụ khác với người được phân công
```

**Dữ liệu đầu vào:**
```
Vụ việc VV-BTP-TW-20260803-001, cán bộ nghiệp vụ phụ trách là cbnv_tw_03, người được phân công là qa_tvvseed28.
```

**Các bước thực hiện:**
```
1. Đăng nhập bằng người được phân công, mở vụ việc, bấm "Cập nhật kết quả", nhập nội dung rồi bấm Xác nhận
2. Mở hộp thư của cán bộ nghiệp vụ phụ trách, mở thư "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260803-001"
3. Đọc dòng tiêu đề lớn ở đầu thân thư
```

**Kết quả mong đợi:**
```
Dòng tiêu đề ở đầu thân thư phải phản ánh đúng loại sự kiện vừa xảy ra, tức là cập nhật kết quả hỗ trợ để cán bộ nghiệp vụ xem xét và chuẩn bị trình phê duyệt.
```

**Kết quả thực tế:**
```
Dòng tiêu đề ở đầu thân thư là "Phân công: Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260803-001". Người nhận đọc dòng đầu sẽ tưởng đây là thư báo phân công vụ việc, trong khi sự kiện thật là cập nhật kết quả. Lỗi tương tự cũng xuất hiện ở thư "Người hỗ trợ đã xác nhận tham gia vụ việc", cũng bị gắn chữ "Phân công:" ở đầu. Thư thuộc nhóm khác, ví dụ "Phản hồi đã được phê duyệt", thì không có tiền tố nào, nên đây không phải chữ cố định của mẫu thư chung.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG - chuyển dev.
- Lỗi do QA phát hiện thêm khi verify CNKQHT_07 (tuần 3) ngày 03/08/2026, không nằm trong phạm vi phiếu gốc nên mở dòng riêng.
- Sự kiện thật là cập nhật kết quả hỗ trợ: theo FR-V.I-15 (UC65) §Processing bước 5 (srs-fr-05-vu-viec.md dòng 1106) và §Postconditions (dòng 1114), đây là thông báo gửi CB NV phụ trách để review, không phải thông báo phân công. Nhưng dòng tiêu đề trong thân thư lại mở đầu bằng "Phân công:".
- Quan sát được: các thông báo của luồng vụ việc đang bị xếp chung một nhóm, và tên nhóm đó được in làm tiền tố tiêu đề thư, nên cả thư "Người hỗ trợ đã xác nhận tham gia vụ việc" cũng bị gắn chữ "Phân công:". Thư nhóm khác không có tiền tố.
- BR-NOTIF-01 (dòng 2466) chỉ bắt buộc gửi đủ 2 kênh in-app + email, không quy định bộ nhóm; dòng 1056 khai loai_thong_bao kiểu text tự do. Vì vậy chỉ yêu cầu tiêu đề thư phản ánh đúng loại sự kiện, cách gắn nhãn để dev/BA chốt.
- Mức độ: Minor, chỉ sai chữ hiển thị, không ảnh hưởng dữ liệu hay luồng xử lý. Nội dung thân thư và người nhận đều đúng.
- Đã kiểm bằng tài khoản Cán bộ Nghiệp vụ Trung ương phụ trách vụ việc (cbnv_tw_03), vụ việc VV-BTP-TW-20260803-001, đo lại 2 lần ở 2 thời điểm và đối chiếu trên 3 thư khác nhau.
```

---

## row 142 — CNDSMLTVV_OOS_02

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Công nhận / công khai danh sách mạng lưới — hộp thoại công khai hàng loạt thiếu phần tệp đính kèm
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp
2. Ở tab "Đang hoạt động" của danh sách Tư vấn viên có ít nhất 1 hồ sơ chưa công khai
```

**Dữ liệu đầu vào:**
```
Hồ sơ TVV-SEED-0001 "Nguyễn Văn Seed", trạng thái Đang hoạt động - Chưa công khai.
```

**Các bước thực hiện:**
```
1. Chọn menu "Mạng lưới Tư vấn viên" -> "Tư vấn viên / Chuyên gia", tab "Đang hoạt động"
2. Tích chọn 1 dòng, bấm nút "Công khai lên Cổng PLQG" trên thanh thao tác hàng loạt
3. Đọc các phần nhập có trong hộp thoại vừa mở, đếm xem có vùng tải tệp đính kèm không
4. Đóng hộp thoại, mở màn hình chi tiết của chính hồ sơ đó rồi bấm "Công khai lên Cổng PLQG"
5. So sánh các phần nhập của hai hộp thoại
```

**Kết quả mong đợi:**
```
Hộp thoại công khai hàng loạt phải là mẫu MD-CONG-KHAI (SCR-IV-01 §Thao tác hàng loạt dòng 1464: "Công khai hàng loạt ... -> nút "Công khai lên Cổng pháp luật quốc gia" -> mở MD-CONG-KHAI"). Mẫu MD-CONG-KHAI ở §3.0b dòng 1406 gồm 3 phần: (a) Mô tả công khai - bắt buộc, tối đa 5000 ký tự; (b) File đính kèm - PDF/DOC/DOCX/XLS/XLSX, tối đa 20MB mỗi tệp, nhiều tệp, tùy chọn; (c) cảnh báo. Phần (b) cũng có trong đặc tả dữ liệu FR-IV-08 dòng 657 (file_dinh_kem_cong_khai — "CB Nghiệp vụ upload (tùy chọn) trong modal MD-CONG-KHAI").
```

**Kết quả thực tế:**
```
Hộp thoại mở từ thao tác hàng loạt ("Công khai hàng loạt lên Cổng PLQG") chỉ có phần (a) và (c). Đếm được 0 vùng tải tệp và chỉ có đúng 1 nhãn trường là "Mô tả công khai"; toàn bộ chữ trong hộp thoại không hề nhắc tới tệp đính kèm hay định dạng tệp. Thiếu hoàn toàn phần (b).

Đối chứng ngay trong cùng phiên làm việc, cùng tài khoản, cùng hồ sơ: hộp thoại công khai mở từ màn hình chi tiết ("Công khai TVV "Nguyễn Văn Seed" lên Cổng PLQG") có 2 vùng tải tệp và 2 nhãn trường là "Mô tả công khai" + "Tệp đính kèm (tùy chọn)", kèm mô tả "Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp." — khớp đúng phần (b) của đặc tả. Ảnh đối chứng: BUG-CNDSMLTVV_OOS_02-doichung-modal-chitiet-CO-vung-tepdinhkem.png.

Vậy phần tải tệp đính kèm đã được làm và chạy được, chỉ riêng đường vào từ thao tác hàng loạt là thiếu — không phải do tài khoản không có quyền đính kèm.

Hệ quả: cán bộ nghiệp vụ công khai theo lô không đính kèm được tệp giới thiệu cho các hồ sơ trong lô, phải mở lại từng hồ sơ để bổ sung.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Yêu cầu theo đặc tả: SCR-IV-01 §Thao tác hàng loạt dòng 1464 (công khai hàng loạt mở MD-CONG-KHAI); mẫu MD-CONG-KHAI §3.0b dòng 1406 phần (b) File đính kèm; FR-IV-08 §Trường dữ liệu dòng 657 (file_dinh_kem_cong_khai, CB Nghiệp vụ upload tùy chọn trong modal MD-CONG-KHAI).
- Bằng chứng đo: hộp thoại hàng loạt có 0 vùng tải tệp / 1 nhãn trường; hộp thoại ở màn hình chi tiết có 2 vùng tải tệp / 2 nhãn trường, đo cùng phiên cùng tài khoản.
- Mã lỗi nội bộ: BUG-CNDSMLTVV_OOS_02. Tài khoản kiểm tra: cbnv_tw_02 (Cán bộ nghiệp vụ Trung ương, đơn vị Cục Bổ trợ tư pháp) — đúng vai trò mà dòng 657 chỉ định. Bản dựng V1.0.5, kiểm tra ngày 03/08/2026.
- Lỗi phát hiện ngoài phạm vi các dòng TC có sẵn nên mở dòng mới.
```

---

## row 143 — CNDSMLTVV_OOS_03

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Công nhận / công khai danh sách mạng lưới — bỏ trống mô tả công khai hiện 2 thông báo lỗi trùng nghĩa
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp
2. Đang mở hộp thoại công khai lên Cổng pháp luật quốc gia của một hồ sơ tư vấn viên
```

**Dữ liệu đầu vào:**
```
Ô "Mô tả công khai" để trống (0 / 5000 ký tự). Hồ sơ dùng để mở hộp thoại: TVV-SEED-0001 "Nguyễn Văn Seed".
```

**Các bước thực hiện:**
```
1. Chọn menu "Mạng lưới Tư vấn viên" -> "Tư vấn viên / Chuyên gia", tab "Đang hoạt động"
2. Tích chọn 1 dòng, bấm "Công khai lên Cổng PLQG" để mở hộp thoại công khai
3. Để trống ô "Mô tả công khai"
4. Bấm nút xác nhận "Công khai"
5. Đếm số dòng báo lỗi hiện ra dưới ô nhập
```

**Kết quả mong đợi:**
```
Hệ thống chặn thao tác và báo cho người dùng đúng một lần về việc thiếu mô tả công khai. FR-IV-08 §Xử lý lỗi dòng 682 định nghĩa duy nhất một mã lỗi cho tình huống này: ERR-CK-02 — "Mô tả công khai là bắt buộc trước khi công khai lên Cổng pháp luật quốc gia".
```

**Kết quả thực tế:**
```
Hệ thống chặn đúng (không gửi lệnh nào ra máy chủ, hộp thoại vẫn mở) nhưng hiện 2 dòng báo lỗi cùng nghĩa cho cùng một ô nhập, xếp chồng ngay dưới ô "Mô tả công khai":
- "Vui lòng nhập mô tả công khai"
- "Mô tả công khai không được để trống"

Đã kiểm cả 2 dòng đều thực sự hiển thị trên màn hình: mỗi dòng chiếm một vùng riêng 592x22 điểm ảnh, không phải chữ ẩn dành cho trình đọc màn hình. Ảnh chụp kèm theo cho thấy cả 2 dòng chữ đỏ.

Ngoài việc lặp, cả 2 câu đều không dùng nội dung thông báo mà đặc tả quy định ở dòng 682.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Yêu cầu theo đặc tả: FR-IV-08 "Công khai mạng lưới TVV (UC46)" §Xử lý lỗi dòng 682 — trường hợp E2 "Thiếu mô tả công khai khi CONG_KHAI" có duy nhất một mã lỗi ERR-CK-02 với nội dung "Mô tả công khai là bắt buộc trước khi công khai lên Cổng pháp luật quốc gia".
- Bằng chứng đo: 2 dòng báo lỗi cùng hiển thị (mỗi dòng 592x22 điểm ảnh, đã loại trừ khả năng chữ ẩn dành cho trình đọc màn hình); 0 lệnh gửi ra máy chủ.
- Mã lỗi nội bộ: BUG-CNDSMLTVV_OOS_03. Tài khoản kiểm tra: cbnv_tw_02 (Cán bộ nghiệp vụ Trung ương, đơn vị Cục Bổ trợ tư pháp). Bản dựng V1.0.5, kiểm tra ngày 03/08/2026.
- Lỗi phát hiện ngoài phạm vi các dòng TC có sẵn nên mở dòng mới.
```

---

## row 144 — QLLKHDTBD_50

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Bảng danh sách Kế hoạch đào tạo thiếu cột và sai định dạng so với thiết kế
```

**Điều kiện:**
```
1. Đăng nhập tài khoản cán bộ (đã kiểm với Cán bộ nghiệp vụ Địa phương và Cán bộ phê duyệt Trung ương, kết quả như nhau)
2. Có sẵn ít nhất 1 kế hoạch đào tạo đã nhập ngân sách dự kiến
```

**Dữ liệu đầu vào:**
```
Kế hoạch KH-20260803-0001 (ngân sách dự kiến 100.000.000), KH-20260803-0004; tổng 14 kế hoạch trong danh sách
```

**Các bước thực hiện:**
```
1. Chọn menu "Đào tạo, tập huấn" -> "Kế hoạch đào tạo"
2. Xem thanh tiêu đề của bảng danh sách, cuộn ngang hết sang phải để thấy toàn bộ cột
3. Đối chiếu với thiết kế màn hình Kế hoạch đào tạo năm (SCR-III-00, Thành phần 3 — Bảng kế hoạch, srs-fr-03-dao-tao.md dòng 1767-1775)
```

**Kết quả mong đợi:**
```
Bảng có đủ các cột theo thiết kế: ô tích chọn dòng, Tên kế hoạch, Năm, Thời gian, Ngân sách dự kiến, Số chương trình, Trạng thái, Người tạo, Ngày tạo, Hành động. Cột ngân sách hiển thị theo định dạng dấu chấm (ví dụ "500.000.000 đ"), rỗng thì hiển thị "—".
```

**Kết quả thực tế:**
```
Bảng chỉ có 8 cột: Mã kế hoạch, Tên kế hoạch, Năm, Từ ngày, Đến ngày, Ngân sách (VNĐ), Trạng thái, Hành động.
- Thiếu 4 thành phần theo thiết kế: ô tích chọn dòng (toàn trang không có ô tích nào), cột "Số chương trình", cột "Người tạo", cột "Ngày tạo".
- Cột ngân sách hiển thị số thô "100000000.00" thay vì "100.000.000 đ". Cùng kế hoạch đó, màn Chi tiết lại hiển thị đúng "100.000.000 VNĐ" nên hai màn không nhất quán.
Đã kiểm bằng 2 cách đều cho kết quả như nhau: đọc danh sách tiêu đề bảng trong mã trang (đúng 8 cột, không có cột nào bị ẩn) và nhìn ảnh chụp sau khi cuộn ngang hết sang phải.
Ảnh hưởng nghiệp vụ: thiếu cột "Người tạo" nên cán bộ phê duyệt không có cách nào biết kế hoạch do đơn vị/người nào lập để ra quyết định duyệt.
Phát hiện thêm trong lúc kiểm tra lại phiếu PDKHDTTH_04 ngày 03/08/2026, không thuộc phạm vi phiếu đó.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
(trống)
```

---

## row 146 — CBKQDTBD_02

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Tab "Công bố kết quả" của màn chi tiết khóa học thiếu 5 cột so với đặc tả: Email, Số điện thoại, Đơn vị, Đề kiểm tra, Điểm.
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ đúng đơn vị của khóa học.
2. Khóa học ở trạng thái "Hoàn thành" và có học viên có kết quả đã được phê duyệt.
```

**Dữ liệu đầu vào:**
```
Khóa học AAA-KH-TW — "Tập huấn pháp lý cấp Trung ương 2026", trạng thái Hoàn thành, 4 học viên đã được duyệt kết quả.
```

**Các bước thực hiện:**
```
1. Chọn menu "Đào tạo, tập huấn" -> "Khóa học"
2. Nhấn xem chi tiết khóa học
3. Chọn tab "Công bố kết quả"
4. Đọc tiêu đề các cột của bảng danh sách học viên
```

**Kết quả mong đợi:**
```
Bảng học viên hiển thị đủ các cột theo đặc tả: Chọn dòng, Họ tên, Email, Số điện thoại, Đơn vị, Đề kiểm tra, Điểm, Kết quả, Trạng thái công bố, Thời điểm công bố, Hành động.
```

**Kết quả thực tế:**
```
Bảng chỉ có 7 cột: Chọn dòng, STT, Họ tên, Kết quả, Trạng thái công bố, Thời điểm công bố, Hành động. Thiếu 5 cột: Email, Số điện thoại, Đơn vị, Đề kiểm tra, Điểm. Bảng không có thanh cuộn ngang nên không phải do cột bị che.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
☑️ Đã kiểm tra lại — lỗi không còn, chuyển Pass.
- Ngày 03/08/2026 lúc 17:55, bảng học viên ở tab "Công bố kết quả" chỉ có 7 cột nên tổ kiểm thử mở dòng này. Lỗi khi đó là có thật (có ảnh chụp màn hình cùng khóa học, cùng tài khoản).
- Kiểm lại lúc 20:00 cùng ngày trên đúng khóa học đó (Tập huấn pháp lý cấp Trung ương 2026, trạng thái Hoàn thành, 4 học viên đã duyệt kết quả): bảng đã hiển thị đủ 12 cột — Chọn dòng, STT, Họ tên, Email, Số điện thoại, Đơn vị, Đề kiểm tra, Điểm, Kết quả, Trạng thái công bố, Thời điểm công bố, Hành động. Đúng theo đặc tả FR-III-19 (UC38) §Đặc tả màn hình SCR-III-02 - Tab 8 "Công bố kết quả" (srs-fr-03-dao-tao.md dòng 1909).
- Nguyên nhân khác biệt giữa hai lần đo: giao diện đã được triển khai lại. Gói giao diện lúc phát hiện lỗi là index-bJhJGCw4.js, lúc kiểm lại là index-RAuQ-eDH.js (máy chủ ghi thời điểm tạo gói 03/08/2026 19:51 giờ Việt Nam). Cả hai lần đều tải lại trang bỏ bộ nhớ đệm trước khi đo.
- Đính chính nội dung dòng này: phần "thiếu 5 cột" nay KHÔNG còn đúng với bản đang chạy. Lưu ý cũ về cột "Đề kiểm tra" cũng đã được làm rõ — cột hiển thị vô điều kiện: khóa chưa gán đề thì hiện dấu "—", khóa đã gán đề thì hiện đúng tên đề (đã dựng đề kiểm tra thật "QA-DEKT-0803" để kiểm chứng trên 2 khóa học).
- Tài khoản kiểm tra lại: cbnv_tw_05 (Cán bộ nghiệp vụ Trung ương, Cục Bổ trợ tư pháp). Bản dựng V1.0.5.
```

---

## row 147 — KTDGKQHT_21

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Tab "Kết quả" của màn chi tiết khóa học không có cột "Đề kiểm tra", kể cả khi khóa học đã được gán đề và điểm đã gắn với đề đó
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ đúng đơn vị của khóa học
2. Có khóa học ở trạng thái "Đang diễn ra" hoặc từ "Đã kết thúc" trở đi (điều kiện để bảng kết quả hiển thị)
3. Khóa học đã được gán ít nhất 1 đề kiểm tra ở trạng thái "Kích hoạt" tại tab "Đề kiểm tra"
4. Có ít nhất 1 học viên trong khóa và học viên đó đã được nhập điểm kiểm tra
```

**Dữ liệu đầu vào:**
```
Đề kiểm tra "QA-DEKT-0803 — Đề kiểm tra pháp lý DN (QA seed 03/08)" (1 câu hỏi, cách tạo Thủ công, điểm đạt 5.0, trạng thái Kích hoạt) — do tổ kiểm thử tạo ngày 03/08/2026 vì hệ thống chưa có đề kiểm tra nào.
Gán đề này vào 2 khóa học: KH-QAW7-HOINGHI ("QAW7 — Hội nghị đối thoại DN 2026", Đang diễn ra, 2 học viên) và AAA-KH-TW ("Tập huấn pháp lý cấp Trung ương 2026", Hoàn thành, 4 học viên đã duyệt kết quả).
Điểm đã nhập trên KH-QAW7-HOINGHI: 9.0 và 4.0.
```

**Các bước thực hiện:**
```
1. Vào "Đào tạo, tập huấn" → "Ngân hàng câu hỏi & Đề kiểm tra" → thẻ "Đề kiểm tra" → "Tạo đề kiểm tra" → kích hoạt đề
2. Vào "Đào tạo, tập huấn" → "Khóa học" → mở khóa học → tab "Đề kiểm tra" → "Gán đề kiểm tra" → chọn đề vừa tạo → "Gán"
3. Mở tab "Kết quả", nhập điểm cho học viên rồi bấm "Lưu kết quả"
4. Tải lại trang bỏ bộ nhớ đệm, mở lại tab "Kết quả"
5. Đọc dãy tiêu đề cột của bảng học viên, cuộn ngang hết cỡ sang phải để xem trọn các cột cuối
```

**Kết quả mong đợi:**
```
Bảng học viên ở tab "Kết quả" hiển thị đủ các cột theo đặc tả, trong đó có cột "Đề kiểm tra" để cán bộ biết điểm đang chấm là điểm của đề nào. Đặc tả: FR-III-05 (UC24) §Đặc tả màn hình SCR-III-02 – Tab 5 "Kết quả kiểm tra" (srs-fr-03-dao-tao.md dòng 1901) liệt kê: STT · Họ tên · Email · Số điện thoại · Đơn vị · Đề kiểm tra · Điểm · Xếp loại (auto BR-KQ-01) · Kết quả (auto BR-KQ-02) · Ghi chú. Bảng Inputs của FR-III-05 (dòng 550) cũng quy định "đề kiểm tra ứng với điểm" là trường bắt buộc khi nhập điểm kiểm tra.
```

**Kết quả thực tế:**
```
Bảng học viên chỉ có 10 cột và KHÔNG có cột "Đề kiểm tra": STT · Họ tên · Email · Số điện thoại · Đơn vị · Chuyên cần · Điểm kiểm tra · Kết quả · Xếp loại · Ghi chú.

Đã loại trừ khả năng "cột chỉ hiện khi khóa có đề" bằng 4 tình huống đo trên cùng một bản dựng:
(a) khóa chưa gán đề — không có cột;
(b) khóa đã gán đề — vẫn không có cột;
(c) khóa đã gán đề và điểm đã lưu (bản ghi kết quả đã trỏ đúng vào đề) — vẫn không có cột;
(d) đo trên 2 khóa ở 2 trạng thái khác nhau (Đang diễn ra và Hoàn thành) — kết quả như nhau.

Đã loại trừ khả năng cột bị che: kiểm cả cột ẩn trong mã trang (không có cột ẩn nào) và cuộn ngang hết cỡ rồi chụp màn hình đọc lại bằng mắt.

Đối chứng dương tính ngay trên cùng bản dựng và cùng khóa học: tab "Công bố kết quả" CÓ cột "Đề kiểm tra" và hiển thị đúng tên đề vừa gán ("QA-DEKT-0803 — ...") ⇒ dữ liệu đề kiểm tra đã sẵn sàng cho giao diện, chỉ riêng tab "Kết quả" không dựng cột này.

Hệ quả nghiệp vụ: khi một khóa học có nhiều đề kiểm tra, cán bộ nhập/soát điểm ở tab "Kết quả" không có cách nào biết điểm thuộc đề nào, trong khi ngưỡng "điểm đạt" dùng để tính Kết quả Đạt/Không đạt lại lấy theo từng đề (BR-KQ-02).

(Lỗi do tổ kiểm thử phát hiện thêm khi verify case KTDGKQHT_02 ngày 03/08/2026 — phiếu KTDGKQHT_02 nói về nhóm cột số buổi học, không có dòng nào cho cột "Đề kiểm tra" nên mở dòng mới. Cột "Chuyên cần" mà bản dựng thêm vào tab không tính vào lỗi này vì đang là câu hỏi chờ BA xác nhận ở phiếu KTDGKQHT_02.)
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Lỗi do QA phát hiện thêm khi verify KTDGKQHT_02 ngày 03/08/2026, không nằm trong phạm vi phiếu gốc nên mở dòng riêng.
- Web đang sai: bảng học viên ở tab "Kết quả" (màn chi tiết khóa học) không có cột "Đề kiểm tra", nên cán bộ không biết điểm của học viên là điểm của đề nào. Bảng chỉ có 10 cột: STT, Họ tên, Email, Số điện thoại, Đơn vị, Chuyên cần, Điểm kiểm tra, Kết quả, Xếp loại, Ghi chú. Đã cuộn ngang hết cỡ và kiểm cả cột ẩn, không phải do cột bị che.
- Đúng theo đặc tả phải có: FR-III-05 (UC24) §Đặc tả màn hình SCR-III-02 – Tab 5 "Kết quả kiểm tra" (srs-fr-03-dao-tao.md dòng 1901) liệt kê đủ các cột STT, Họ tên, Email, Số điện thoại, Đơn vị, Đề kiểm tra, Điểm, Xếp loại (auto BR-KQ-01), Kết quả (auto BR-KQ-02), Ghi chú. Trường "đề kiểm tra ứng với điểm" cũng là trường bắt buộc khi nhập điểm kiểm tra theo bảng Inputs FR-III-05 (dòng 550).
- Đã loại trừ khả năng "cột chỉ hiện khi khóa có đề": QA tự tạo đề kiểm tra "QA-DEKT-0803" (trạng thái Kích hoạt), gán vào 2 khóa học ở 2 trạng thái khác nhau, rồi nhập điểm để bản ghi kết quả trỏ đúng vào đề. Cột "Đề kiểm tra" vẫn không xuất hiện ở cả 4 tình huống đo.
- Đối chứng ngay trên cùng bản dựng, cùng khóa học: tab "Công bố kết quả" CÓ cột "Đề kiểm tra" và hiển thị đúng tên đề vừa gán, chứng tỏ dữ liệu đề đã sẵn sàng cho giao diện; riêng tab "Kết quả" không dựng cột này.
- Không tính vào lỗi này: cột "Chuyên cần" mà bản dựng thêm vào tab, vì việc gộp số buổi có mặt / tổng buổi / tỷ lệ vào một ô đang là câu hỏi chờ BA xác nhận ở phiếu KTDGKQHT_02.
- Tài khoản kiểm tra: cbnv_tw_05 (Cán bộ nghiệp vụ Trung ương, Cục Bổ trợ tư pháp). Dữ liệu: khóa KH-QAW7-HOINGHI (Đang diễn ra) và AAA-KH-TW (Hoàn thành). Bản dựng V1.0.5, gói giao diện index-RAuQ-eDH.js. Bug ID: BUG-KTDGKQHT_21.
```

---

## row 148 — KTDGKQHT_22

- **Tên chức năng:** (trống)
- **Tác nhân (đối tác ghi):** (trống)
- **Dev fix 1 / Verify (vòng 1):** `dev done` / `Pass`

**Mô tả:**
```
Tab "Đề kiểm tra" của màn chi tiết khóa học thiếu 4 cột theo đặc tả (STT, Mã đề, Lĩnh vực, Người thêm) và không có thao tác "Xem chi tiết" đề
```

**Điều kiện:**
```
1. Đăng nhập tài khoản Cán bộ nghiệp vụ đúng đơn vị của khóa học
2. Có ít nhất 1 đề kiểm tra ở trạng thái "Kích hoạt"
3. Có khóa học đã được gán ít nhất 1 đề kiểm tra đó
```

**Dữ liệu đầu vào:**
```
Đề kiểm tra "QA-DEKT-0803 — Đề kiểm tra pháp lý DN (QA seed 03/08)" (1 câu hỏi, cách tạo Thủ công, điểm đạt 5.0, trạng thái Kích hoạt) — do tổ kiểm thử tạo ngày 03/08/2026 vì hệ thống chưa có đề kiểm tra nào.
Khóa học AAA-KH-TW ("Tập huấn pháp lý cấp Trung ương 2026", trạng thái Hoàn thành), đã gán đề trên lúc 03/08/2026 20:04.
```

**Các bước thực hiện:**
```
1. Vào "Đào tạo, tập huấn" → "Khóa học" → mở khóa học đã gán đề kiểm tra
2. Mở tab "Đề kiểm tra"
3. Đọc dãy tiêu đề cột của bảng đề kiểm tra đã gán
4. Đối chiếu với danh sách cột trong đặc tả màn hình
5. Xem các thao tác có ở cột "Hành động" của dòng đề
```

**Kết quả mong đợi:**
```
Bảng đề kiểm tra đã gán cho cán bộ thấy đủ thông tin nhận diện và truy vết đề theo đặc tả FR-III-05 (UC24) §Đặc tả màn hình SCR-III-02 - Tab 7 (srs-fr-03-dao-tao.md dòng 1908): số thứ tự, mã đề, tên đề, số câu, lĩnh vực của đề, người đã thêm đề vào khóa, thời điểm thêm, và cột hành động có cả xem chi tiết đề lẫn gỡ đề khỏi khóa.
```

**Kết quả thực tế:**
```
Bảng chỉ có 5 cột: Tên đề · Số câu hỏi · Trạng thái · Thời điểm thêm · Hành động.
Thiếu 4 cột: STT, Mã đề, Lĩnh vực, Người thêm.
Cột Hành động chỉ có biểu tượng thùng rác (gỡ đề), không có thao tác xem chi tiết đề.
Ghi nhận thêm: bảng có cột "Trạng thái" không nằm trong đặc tả, và ngay dưới bảng có nút "Gỡ công khai" mà đặc tả tab này không nhắc tới.
```

**DEV phản hồi lần 1 (mô tả BUG GỐC / lý do Pass vòng 1):**
```
✅ Bug ĐÚNG – chuyển dev.
- Lỗi do tổ kiểm thử phát hiện thêm ngày 03/08/2026 trong lúc dựng đề kiểm tra để chốt dòng KTDGKQHT_21, không nằm trong phạm vi phiếu nào của đối tác.
- Tab "Đề kiểm tra" ở màn chi tiết khóa học chỉ có 5 cột: Tên đề · Số câu hỏi · Trạng thái · Thời điểm thêm · Hành động.
- Theo FR-III-05 (UC24) §Đặc tả màn hình SCR-III-02 - Tab 7 "Đề kiểm tra" (srs-fr-03-dao-tao.md dòng 1908), bảng này phải cho cán bộ thấy đủ: STT · Mã đề · Tên đề · Số câu · Lĩnh vực · Người thêm · Thời điểm thêm · Hành động (Xem chi tiết · Gỡ khỏi khóa).
- Đang thiếu 4 cột: STT, Mã đề, Lĩnh vực, Người thêm. Hệ quả nghiệp vụ: khóa gán nhiều đề thì cán bộ không phân biệt được đề nào theo mã, không biết đề thuộc lĩnh vực nào để đối chiếu với lĩnh vực của khóa, và không truy được ai đã thêm đề vào khóa.
- Cột Hành động cũng chỉ có thao tác gỡ đề (biểu tượng thùng rác), không có "Xem chi tiết" như đặc tả — cán bộ không xem được nội dung đề trước khi quyết định giữ hay gỡ.
- Ngoài ra bảng có thêm cột "Trạng thái" không nằm trong danh sách của đặc tả; đây chỉ là ghi nhận, không tính vào lỗi.
- Cần lưu ý thêm (chưa kết luận): ngay dưới bảng có nút "Gỡ công khai" — đặc tả tab này không nhắc tới nút đó, đề nghị dev xác nhận nút này thuộc về tab nào.
- Tài khoản kiểm tra: cbnv_tw_05 (Cán bộ nghiệp vụ Trung ương, Cục Bổ trợ tư pháp). Khóa học AAA-KH-TW, trạng thái Hoàn thành, đã gán đề QA-DEKT-0803. Bản dựng V1.0.5, gói giao diện index-RAuQ-eDH.js.
```