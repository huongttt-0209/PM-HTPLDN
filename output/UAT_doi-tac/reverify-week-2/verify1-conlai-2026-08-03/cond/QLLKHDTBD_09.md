# Bảng đối chiếu điều kiện — QLLKHDTBD_09 (row 119, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Xuất Excel danh sách Kế hoạch đào tạo năm theo bộ lọc — `FR-III-14 (UC33)`, màn `SCR-III-00`
**Loại bug:** bug FILTER — phụ thuộc vai trò + dữ liệu + giá trị lọc → BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG)
**Ngày re-verify sau dev fix:** 2026-08-04 · **Tài khoản QA dùng:** `cbnv_tw_01` (CB_NV_TW, đơn vị `BTP · TW`, bản dựng `HTPLDN · V1.0.5`, gói giao diện `index-BrKDNUvo.js`) · **Verdict: `Pass`** (vòng 1 ngày 2026-08-03 là `Open`)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res `frames/QLLKHDTBD_09/dense/t000.00s.jpg`, `t008.20s.jpg`, `t014.51s.jpg`) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — nhãn góc phải khung hình ghi "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" | `cbnv_tw_01` — nhãn góc phải "CB Nghiệp vụ - Trung ương #01 · CB_NV_TW", đơn vị "BTP · TW" (ảnh `bug-reports/dao-tao/image/QLLKHDTBD_09-retest-2026-08-04-locA-man-hinh-1-ket-qua.png`). `auth-store` trả `vaiTro:["CB_NV_TW"], capDonVi:"TW", donViId:…-8000-000000000001` (**trùng khít đơn vị của `cbnv_tw` dùng ở vòng 1**), có quyền `export_ke_hoach_dao_tao` | Không |
| Màn hình + tab đang đứng | Màn `Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách`, tab **Tất cả** đang chọn (badge "Tất cả 2") | Cùng màn `/dao-tao/ke-hoach/danh-sach`, tab **Tất cả** đang chọn | Không |
| Dữ liệu tiền đề (phải có bản ghi NẰM NGOÀI khoảng lọc thì phép đo mới phân biệt được) | Có — tệp Excel của đối tác cho thấy kho dữ liệu có **12 kế hoạch**, trong đó chỉ **2** rơi vào khoảng lọc, 10 bản ghi còn lại nằm ngoài (vd `15/5/2026–30/6/2026`, `31/12/2025–30/12/2026`) | Có — baseline không lọc **14 kế hoạch** (2026-08-04), phần lớn nằm ngoài tháng 7/2026 (`01/09–31/12/2026`, `01/01–31/12/2026`, `01/11–30/11/2026`…). **Ban đầu 0 bản ghi rơi vào khoảng lọc của đối tác → phép đo sẽ suy biến (0 vs 12)**, nên QA đã **tự seed** 1 kế hoạch `KH-20260803-0003` (`05/07/2026 – 25/07/2026`) qua đúng luồng "Thêm mới" trên UI (ảnh `image/QLLKHDTBD_09-seed-form-truoc-luu.png`, `image/QLLKHDTBD_09-seed-sau-luu-13-ket-qua.png`) → bản ghi này VẪN CÒN trên môi trường lúc re-verify, tổng 14, trong đó **1** rơi vào khoảng lọc, 13 nằm ngoài. Cấu hình dữ liệu nay tương đương đối tác (có trong + có ngoài) | Không |
| Input / filter / giá trị nhập | **Đúng 1 bộ lọc:** ô "Tìm theo tên hoặc mã kế hoạch" **trống** · "Năm kế hoạch" **trống** · **Từ ngày = 01/07/2026** · **Đến ngày = 31/07/2026** · tab "Tất cả". Địa chỉ trang: `…/dao-tao/ke-hoach/danh-sach?tuNgay=2026-07-01&denNgay=2026-07-31&page=1` | **Bộ lọc A — trùng khít từng giá trị với đối tác:** từ khoá **trống** · Năm **trống** · **Từ ngày = 01/07/2026** · **Đến ngày = 31/07/2026** · tab "Tất cả". Địa chỉ trang ra **đúng chuỗi** `…?tuNgay=2026-07-01&denNgay=2026-07-31&page=1` (ảnh `…/image/BUG-QLLKHDTBD_09-02-loc-01-31.07.2026-man-hinh-1-ket-qua.png`).<br>**Bộ lọc B — chiều lọc KHÁC** để loại trừ trùng ngẫu nhiên: từ khoá tên kế hoạch = `RECON`, các ô ngày **trống** (`…?keyword=RECON&page=1`, ảnh `…/image/BUG-QLLKHDTBD_09-04-loc-tu-khoa-RECON-man-hinh-2-ket-qua.png`) | Không |
| Cách kích hoạt xuất tệp | Bấm nút **[Xuất Excel]** ở góc phải tiêu đề màn (khung hình `t008.20s.jpg`: toast "Xuất Excel thành công" + hộp thoại lưu tệp `ke-hoach-dao-tao-1784950244818.xlsx`) | Bấm đúng nút **[Xuất Excel]** ở cùng vị trí, tệp về `~/Downloads` tên `ke-hoach-dao-tao-<timestamp>.xlsx`, toast "Xuất Excel thành công" (bắt bằng `tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`) | Không |

## Ghi chú đóng GAP (cập nhật re-verify 2026-08-04)

- **Bộ lọc dùng để kết luận là bộ lọc CỦA ĐỐI TÁC, không phải bộ lọc tiện tái hiện.** Bộ lọc A đặt đúng hai giá trị `01/07/2026` và `31/07/2026`, sinh ra đúng chuỗi tham số trên địa chỉ trang mà đối tác có trong khung hình. Bộ lọc B chỉ đóng vai **phép đo đối chứng thứ hai** trên một chiều lọc khác (từ khoá thay vì khoảng ngày) để loại giả thuyết "trùng số ngẫu nhiên" — nó **không** thay thế bộ lọc A.
- **Tiền đề dữ liệu vẫn nguyên vẹn:** bản ghi `KH-20260803-0003` (`05/07/2026 – 25/07/2026`) do QA seed ở vòng 1 vẫn còn, nên phép đo không suy biến (màn ra 1 kết quả trong khi kho có 14).
- **Đo nội dung tệp, không dừng ở "tải được tệp".** Cả 3 tệp đều được mở bằng `openpyxl` để đếm số dòng dữ liệu:

  - Mốc 0 — không lọc (mốc đối chứng): trên màn **14** → trong tệp **14** ✅
  - Phép A — `Từ ngày 01/07/2026` + `Đến ngày 31/07/2026`: trên màn **1** → trong tệp **1** ✅
  - Phép B — từ khoá tên kế hoạch `RECON`: trên màn **2** → trong tệp **2** ✅

- **Kiểm cả NỘI DUNG chứ không chỉ số lượng:** tệp của phép A chứa đúng `KH-20260803-0003` (`05/07/2026 – 25/07/2026`); tệp của phép B chứa đúng 2 bản ghi có tên bắt đầu bằng `RECON 03/08 …`. Không lẫn bản ghi ngoài bộ lọc.
- **Tệp bằng chứng lưu tại** `fixtures/QLLKHDTBD_09/retest0804-01-khong-loc-man14-file14.xlsx`, `…retest0804-02-locA-tungay01.07-denngay31.07-man1-file1.xlsx`, `…retest0804-03-locB-tukhoa-RECON-man2-file2.xlsx`.
- **Bộ bắt thông báo** cài trước mỗi lần bấm: đúng **1** thông báo "Xuất Excel thành công" mỗi lần, không lặp.

**Kết luận: 0 GAP** — đã tái lập đúng vai trò, đúng màn, đúng cấu hình dữ liệu và **đúng từng giá trị bộ lọc** của đối tác; lỗi không còn tái hiện ở cả 3 phép đo.
