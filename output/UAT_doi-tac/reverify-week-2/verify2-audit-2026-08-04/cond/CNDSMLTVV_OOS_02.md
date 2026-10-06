# CNDSMLTVV_OOS_02 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 142 · Verdict Verify 2: `Pass`
> **Bug gốc:** hộp thoại **công khai hàng loạt** *thiếu hẳn phần tải tệp đính kèm* — đo được **0 vùng tải tệp / 1 nhãn
> trường**, trong khi hộp thoại mở từ **màn chi tiết** (cùng phiên, cùng tài khoản, cùng hồ sơ) có **2 vùng tải tệp /
> 2 nhãn trường**. Hệ quả: công khai theo lô thì không đính kèm được tệp giới thiệu.
> **Kết quả mong đợi:** hộp thoại hàng loạt phải là mẫu **MD-CONG-KHAI** đủ 3 phần —
> `srs-fr-04-chuyen-gia-tvv.md:1464` (*"**Công khai hàng loạt** (tab 'Đang hoạt động'): chọn nhiều dòng → nút 'Công khai
> lên Cổng pháp luật quốc gia' → **mở MD-CONG-KHAI**"*) + mẫu MD-CONG-KHAI ở `:1406` phần **(b)** *"**File đính kèm** —
> PDF/DOC/DOCX/XLS/XLSX, max 20MB/file, nhiều file, tùy chọn (file giới thiệu cá nhân để DN tham khảo)"* +
> `:657` (*`file_dinh_kem_cong_khai` … "CB Nghiệp vụ upload (tùy chọn) trong modal MD-CONG-KHAI"*).
> Bug phụ thuộc **vai trò + lối vào (hàng loạt vs màn chi tiết) + trạng thái entity** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc
> điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | *"Cán bộ nghiệp vụ cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp"*; lần đo trước dùng `cbnv_tw_02` — đúng vai trò mà `:657` chỉ định người được tải tệp | **`cbnv_tw`** — `CB_NV_TW`, `capDonVi TW`, `donViId 00000000-0000-4000-8000-000000000001`, thanh trên hiện `BTP · TW`. `cbnv_tw_02` **không tồn tại** trên môi trường này nên dùng tài khoản gốc cùng vai trò + cùng cấp + cùng đơn vị (Rule 7). Đã thử thêm **`cbnv_bn`** (bộ ngành) theo yêu cầu: đơn vị đó **0 hồ sơ tư vấn viên** ở cả 10 tab nên không mở được hộp thoại — ảnh `LO-D-v2-00-tai-khoan-bo-nganh-cbnv_bn-thay-0-tu-van-vien.png` | Không |
| Entity + **trạng thái** | *"Tab 'Đang hoạt động' có ít nhất 1 hồ sơ **chưa công khai**"*; phiếu dùng `TVV-SEED-0001` | Môi trường này **không có** `TVV-SEED-0001` ⇒ **tự dựng tiền đề tương đương**: **`TVV-BTP-TW-0063`** (*Tester TKM BTP-TW*), `trangThai HOAT_DONG`, cột Công khai = **"Chưa công khai"** tại thời điểm mở hộp thoại | Không |
| **Lối vào** — biến quyết định của bug gốc | Phiếu bắt so **hai chỗ**: (bước 2-3) hộp thoại từ **thanh thao tác hàng loạt**; (bước 4-5) hộp thoại từ **màn chi tiết** của chính hồ sơ đó | Đo **đủ cả hai**, cùng phiên cùng tài khoản: (A) `/chuyen-gia-tvv/danh-sach` → tích dòng → **"Công khai lên Cổng PLQG"**; (B) màn chi tiết `/chuyen-gia-tvv/06748bb5-e5d4-453f-9490-f07b17fd0a4a` → nút **"Công khai lên Cổng PLQG"** | Không |
| Số hồ sơ chọn trong lô | Phiếu chọn **1** dòng | Đo **cả 1 dòng** (lần này) **và 2 dòng** (khi làm row 124 — ảnh `CNDSMLTVV_01-v2-02`): cả hai lô đều có vùng tải tệp ⇒ không phải "chỉ đúng khi chọn 1" | Không |
| Cách quan sát | *"Đếm xem có vùng tải tệp đính kèm không"* + *"đếm nhãn trường"* (bug gốc: 0 vùng / 1 nhãn) | Lặp đúng phép đếm đó bằng máy: đếm `.ant-form-item-label label` và đếm `.ant-upload` **đã lọc phần tử 0×0** (chống đếm nhầm vùng ẩn), thêm `input[type=file]`, đọc câu hướng dẫn định dạng; **rồi không dừng ở quan sát tĩnh** — tải một tệp PDF thật lên qua chính hộp thoại hàng loạt và chạy hết luồng | Không |

## Kết quả đo

**1. Hộp thoại hàng loạt nay có đủ phần (b).** *"Công khai hàng loạt lên Cổng PLQG"*:
`nhãn trường = ["Mô tả công khai", "Tệp đính kèm (tùy chọn)"]` (**2**, trước là 1) ·
`vùng tải tệp hiển hình = 2` — kích thước thật **592×209** và **590×207** điểm ảnh (không phải phần tử ẩn) ·
`1 ô nhập tệp` · hướng dẫn *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp."*
— khớp phần (b) của `:1406` (PDF/DOC/DOCX/XLS/XLSX, 20MB/tệp, nhiều tệp, tùy chọn).
Ảnh: `CNDSMLTVV_OOS_02-v2-01`.

**2. Vùng tải tệp chạy thật, không phải hình trang trí.** Tải tệp PDF thật
`fixtures/CNDSMLTVV_OOS_02-v2-tep-gioi-thieu.pdf` (1.266 byte, md5 `db816dd27bf019fb813ffeed367fb26b`) qua **chính hộp
thoại hàng loạt** + nhập mô tả → bấm "Công khai": **1 lệnh** (`POST /api/v1/tu-van-viens/batch-cong-khai`) —
**1 thông báo** (*"Đã công khai tư vấn viên thành công"*), bộ bắt thông báo tự kiểm `soObserverDangSong = 1`.

**3. Tệp lưu thật — đọc lại bằng 2 cách đều khớp.**
- Máy chủ: `GET /api/v1/tu-van-viens/{id}` của `TVV-BTP-TW-0063` trả
  `fileDinhKemCongKhai: [{fileId "5eb26e38-f141-455c-93ee-87ab6d74d8b5", tenFile
  "CNDSMLTVV_OOS_02-v2-tep-gioi-thieu.pdf", loaiFile "application/pdf"}]`, `thoiGianDangTai 2026-08-04T11:10:54.243Z`.
- Giao diện: màn chi tiết hiện *"File đính kèm công khai: CNDSMLTVV_OOS_02-v2-tep-gioi-thieu.pdf"* —
  ảnh `CNDSMLTVV_OOS_02-v2-02`.

**4. Chỗ đối chứng của bug gốc nay bằng nhau.** Hộp thoại ở **màn chi tiết**
(*Công khai TVV "TVV R11 Verify Mail Fix" lên Cổng PLQG*) đo ra **đúng cùng bộ số**: 2 nhãn trường · 2 vùng tải tệp
**592×209 / 590×207** · 1 ô nhập tệp — ảnh `CNDSMLTVV_OOS_02-v2-03`. Chênh lệch **2 vùng vs 0 vùng** của bug gốc
đã hết.

## Đã cố BÁC BỎ kết luận `Pass` bằng những cách nào

1. **Nghi "vùng tải tệp có trong mã nhưng bị ẩn, nhìn ảnh tưởng có"** → **BÁC**: đo **kích thước thật từng vùng**
   (592×209 và 590×207) và đã lọc bỏ phần tử 0×0 trước khi đếm.
2. **Nghi "chỉ vẽ giao diện cho có, không nhận tệp"** → **BÁC**: tải tệp PDF **thật** lên qua đúng hộp thoại hàng loạt,
   lưu được và đọc lại đúng tên + đúng loại tệp.
3. **Nghi "nhận tệp nhưng lưu hỏng / gán nhầm hồ sơ"** → **BÁC**: đọc lại bằng **2 cách độc lập** (máy chủ trả về và
   màn chi tiết trên giao diện), cùng ra 1 tệp trên đúng hồ sơ vừa công khai.
4. **Nghi "sửa bằng cách hạ chuẩn bên kia cho bằng nhau"** (gỡ vùng tải tệp ở màn chi tiết) → **BÁC**: hộp thoại màn
   chi tiết **vẫn đủ** 2 nhãn + 2 vùng + câu hướng dẫn định dạng, tức là hai bên bằng nhau **ở mức đúng đặc tả**,
   không phải bằng nhau ở mức cùng thiếu.
5. **Nghi "chỉ đúng khi chọn 1 hồ sơ"** → **BÁC**: lô **2 hồ sơ** (đo ở row 124) cũng có phần "Tệp đính kèm (tùy chọn)".
6. **Nghi "phần (b) có nhưng sai điều kiện đặc tả"** (sai định dạng / dung lượng) → **BÁC**: câu hướng dẫn liệt kê đúng
   `.pdf, .doc, .docx, .xls, .xlsx` và `20MB/tệp`, khớp `:1406(b)` và `:657`.

**Kết luận: 0 GAP** — đúng vai trò, đúng trạng thái entity, đúng **cả hai lối vào** mà phiếu bắt so sánh, đúng phép đếm
của bug gốc, và đã chạy trọn thao tác tải tệp tới lúc dữ liệu lưu được.
