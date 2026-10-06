# QLLKHDTBD_50 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 144 · Verdict Verify 2: `Reopen`
> Bug gốc: bảng danh sách `Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách` **thiếu cột và sai định dạng so với
> thiết kế**. Bảng chỉ có 8 cột; thiếu **ô tích chọn dòng**, cột **Số chương trình**, cột **Người tạo**, cột
> **Ngày tạo**; cột ngân sách hiện số thô `100000000.00` thay vì `100.000.000 đ`.
> Kết quả mong đợi của phiếu: *"Bảng có đủ các cột **theo thiết kế** … Số chương trình …"* — chiếu
> `srs-fr-03-dao-tao.md:1770` `| Số chương trình | COUNT CTDT thuộc kế hoạch năm |`.
> Bug gốc **gộp 5 ý**; phiếu ghi rõ đã kiểm với **Cán bộ nghiệp vụ Địa phương** và **Cán bộ phê duyệt Trung ương**
> ⇒ có chiều vai trò ⇒ KHÔNG dùng `--static-bug`, bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**
(bản dựng MỚI, khác gói `index-BrKDNUvo.js` của vòng trước).

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Tài khoản cán bộ — phiếu ghi đã kiểm với **Cán bộ nghiệp vụ Địa phương** và **Cán bộ phê duyệt Trung ương**, kết quả như nhau | Đo bằng **2 vai trò**: (1) **`cbnv_tw`** — Cán bộ NV Trung ương (`CB_NV_TW`, `capDonVi TW`); (2) **`cbpd_tw`** — **Cán bộ phê duyệt Trung ương** (`CB_PD_TW`, `capDonVi TW`), đúng 1 trong 2 vai trò phiếu nêu; thanh trên hiện `Cán bộ PD Trung ương · CB_PD_TW · BTP · TW`. **Cả 2 vai trò ra kết quả giống hệt nhau** | Không |
| Màn hình + thao tác | Menu `Đào tạo, tập huấn → Kế hoạch đào tạo`; xem thanh tiêu đề bảng, **cuộn ngang hết sang phải** | Cùng menu, cùng màn `/dao-tao/ke-hoach/danh-sach`, tab **Tất cả**; cuộn ngang hết (`scrollLeft 464 / scrollWidth 1600 / clientWidth 1136`) rồi chụp toàn trang | Không |
| Dữ liệu tiền đề — có kế hoạch **đã nhập ngân sách** | `KH-20260803-0001` (ngân sách 100.000.000), `KH-20260803-0004`; tổng **14 kế hoạch** | Kho có **15 kế hoạch**, trong đó **`KH-20260803-0001` ngân sách 100.000.000 vẫn còn** (đúng bản ghi phiếu nêu); đủ 3 dạng ngân sách để soi định dạng: có số (`100.000.000 đ`), bằng 0 (`0 đ`), bỏ trống (`—`) | Không |
| Dữ liệu tiền đề — **kế hoạch phải CÓ chương trình con** (điều kiện mới, bug gốc chưa chạm tới vì cột chưa tồn tại) | Bug gốc không nêu (cột `Số chương trình` khi đó chưa có nên không kiểm được giá trị) | **Tự dựng cho đủ** (Nguyên tắc 4): kho hiện có **16 chương trình đào tạo thuộc 8 kế hoạch khác nhau** — vd `KH-20260525-0001` có **4** chương trình **đã duyệt**, `KH-20260509-0001` có 3, `KH-20260508-0004` có 3, `KH-20260508-0001` có 2. Ngoài dữ liệu sẵn có, còn **tạo mới 1 chương trình qua giao diện** (`CTDT-BTP-TW-2026-0015`, gắn kế hoạch `KH-20260723-0001`) để có bản ghi tạo **sau** bản vá | Không |
| Trạng thái bản ghi | Bug gốc không giới hạn trạng thái | Bảng phủ đủ **6 trạng thái**: Nháp 1 · Chờ duyệt 2 · Đã duyệt 6 · Từ chối 2 · Đã công khai 4 (tổng 15). Chương trình con đo được gồm cả `Đã duyệt`, `Chờ duyệt`, `Hoàn thành`, `Dự thảo` ⇒ không thể đổ cho "chỉ đếm trạng thái nào đó" | Không |

## Kết quả từng ý của bug gốc (bug gốc gộp 5 ý)

- **Ý 1 — thiếu ô tích chọn dòng:** cột đầu bảng đã có hộp tích; bấm ô tích ở dòng tiêu đề thì **10/10 dòng đang hiện được tích theo** ✅ ĐẠT
- **Ý 2 — thiếu cột Người tạo:** đã có, hiện tên người lập (`CB Nghiệp vụ TW 01`, `CB NV DP 02 (BG)`, `Quản trị viên 1`…) ✅ ĐẠT
- **Ý 3 — thiếu cột Ngày tạo:** đã có, đúng dạng ngày/tháng/năm (`03/08/2026`, `25/05/2026`…) ✅ ĐẠT
- **Ý 4 — ngân sách hiện số thô `100000000.00`:** đã sửa thành `100.000.000 đ`, `2.943.499.581 đ`, `0 đ`; bỏ trống hiện `—` ✅ ĐẠT
- **Ý 5 — thiếu cột Số chương trình:** cột đã được thêm **nhưng luôn hiện `0`** cho **toàn bộ 15/15 kế hoạch**, kể cả kế hoạch đang có **4 chương trình đã duyệt** ❌ CHƯA ĐẠT

## Đo ý số 5 — cột Số chương trình

- **Toàn bảng 15/15 dòng đều `0`**, đo ở cả 2 vai trò `cbnv_tw` và `cbpd_tw`, ở cả 2 lần nạp trang khác nhau.
- **Bằng chứng ngược chiều trên chính giao diện:** mở chi tiết chương trình `CTDT-BTP-TW-2026-0012` (trạng thái
  **Đã duyệt**) → ô **`Kế hoạch năm`** ghi rõ **"Kế hoạch đào tạo luật doanh nghiệp năm quý 3 năm 2026 (2026)"**,
  tức `KH-20260525-0001`. Trong khi đó chính dòng `KH-20260525-0001` ở bảng danh sách vẫn hiện **`0`**.
  Riêng kế hoạch này có **4** chương trình đã duyệt trỏ vào.
- **Phép thử bản ghi MỚI:** tạo thêm chương trình `CTDT-BTP-TW-2026-0015` qua giao diện `Tạo mới`, chọn
  `Kế hoạch năm = Kế hoạch kiểm thử HTPLDN 2026` (`KH-20260723-0001`) → lưu thành công (đúng 1 thông báo
  `Tạo chương trình đào tạo thành công`, đúng 1 request ghi). Mở lại chi tiết chương trình thì liên kết kế hoạch
  **đã lưu đúng**; quay lại bảng danh sách, dòng `KH-20260723-0001` **vẫn `0`** ⇒ không phải lỗi "dữ liệu cũ tạo
  trước bản vá".
- Đọc theo cách nào cũng không ra `0`: hiểu là **đếm chương trình gắn với kế hoạch đó** thì phải ra 1–4;
  hiểu là **đếm chương trình cùng năm kế hoạch** thì cả 15 kế hoạch đều năm 2026 nên phải ra 16.

## Đã cố BÁC BỎ (cả 2 chiều)

1. **Cố bác kết luận `Pass` cũ:** không dừng ở "đã thấy đủ tên cột" — chạy tiếp tới bước đọc **giá trị** trong cột mới thêm.
2. **Cố bác chính phát hiện của mình** (tránh báo lỗi oan):
   - Nghi "tại bản ghi mới chưa được đếm" → đo thêm **7 kế hoạch có chương trình tạo từ trước**, vẫn `0`.
   - Nghi "chỉ đếm chương trình đã duyệt, mà bản ghi mình tạo là bản nháp" → kế hoạch `KH-20260525-0001` có **4 chương trình ĐÃ DUYỆT** cũng `0`.
   - Nghi "liên kết kế hoạch không lưu được" → mở lại chi tiết chương trình, ô `Kế hoạch năm` **có đúng tên kế hoạch** ⇒ liên kết đã lưu.
   - Nghi "do vai trò / phạm vi xem dữ liệu" → đo lại bằng **`cbpd_tw` (Cán bộ phê duyệt Trung ương)**, đúng vai trò phiếu nêu, kết quả **giống hệt**.
   - Nghi "trang hiện bản cũ trong bộ nhớ đệm" → đăng nhập lại phiên mới, nạp lại trang, vẫn `0`.
3. **Soi thêm 4 ý còn lại của phiếu** thay vì chỉ nhìn ý dễ thấy — 4 ý kia đều đã đạt, nên báo cáo nêu rõ phần nào đã xong, phần nào chưa.

**Kết luận: 0 GAP về điều kiện** — đã tái lập đúng vai trò (gồm 1 trong 2 vai trò phiếu nêu), đúng màn, đúng thao
tác cuộn ngang, đúng dạng dữ liệu ngân sách và **bổ sung đủ tiền đề kế hoạch có chương trình con**.
**4/5 ý đã hết lỗi, còn 1 ý chưa đạt** (cột `Số chương trình` luôn bằng `0`) ⇒ theo quy tắc "fix một phần = Reopen"
⇒ verdict `Reopen`.
