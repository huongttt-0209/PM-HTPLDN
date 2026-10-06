# BA confirmation needed — lô F6 (QLTLPLCVV · DKTGMLTVV — tab `bug` dòng 301/302/35) — 2026-08-07

> **Phạm vi:** 3 phiếu re-verify FLOW 04 trên bảng `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` tab `bug`:
> dòng **301** `QLTLPLCVV_22`, dòng **302** `QLTLPLCVV_23`, dòng **35** `DKTGMLTVV_13`.
> Cả 3 dòng QA đã đặt `Trạng thái dev fix` = `BA confirm`. **5 điểm** cần BA chốt, chia 2 dạng: **2 case dạng A**
> (QA đã kết luận, cần BA phản hồi đối tác) · **3 case dạng B** (đặc tả mâu thuẫn hoặc im lặng, QA không tự chốt).

> **Môi trường verify:** env NỘI BỘ `https://18.143.165.120.nip.io`, bản dựng **`HTPLDN · V1.0.9`**
> (etag `W/"6a74c6ea-428"`, bó mã `assets/index-B2W2Krcs.js`). Bằng chứng của đối tác chụp trên
> `htpldn-uat.ospgroup.vn` bản `HTPLDN · V1.0` — **hai bản dựng khác nhau thật**, mọi kết luận dưới đây chỉ có
> hiệu lực cho V1.0.9 và cần đo lại khi bản này lên môi trường nghiệm thu.

> **Nguồn citation:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25).
> Mọi số dòng dưới đây QA **tự mở file đọc trong lượt này**, không lấy từ trí nhớ và không lấy từ
> `input/srs-update-2026-5-5/`.

> **Không điểm nào dưới đây là lỗi dev.** Ở cả 5 điểm, phần mềm đang chạy **đúng đặc tả hiện hành** hoặc đúng ý
> đối tác; việc cần chốt là **dọn đặc tả / sửa expected của phiếu**, KHÔNG chặn bàn giao.

**Bảng dẫn — ai cần quyết:**

| # | Dạng | Mã TC | Điểm cần chốt | Người quyết |
|--:|:--:|---|---|---|
| 1 | A | `DKTGMLTVV_13` | Loại hồ sơ có giá trị "Người hỗ trợ" không | BA **+ đối tác** |
| 2 | A | `DKTGMLTVV_13` | Sau khi lưu chuyển về đâu | BA **+ đối tác** |
| 3 | B | `QLTLPLCVV_22` + `QLTLPLCVV_23` | Nhóm tư liệu có được có ô tìm kiếm / bộ lọc không | BA |
| 4 | B | `QLTLPLCVV_23` | Tìm kiếm tư liệu có bắt buộc hỗ trợ không dấu không | BA |
| 5 | B | `DKTGMLTVV_13` | Thông báo thành công có bắt buộc kèm mã hồ sơ không | BA |

> **Điểm 1 và 2 BA không quyết một mình được.** Cả hai nếu chốt theo hướng (1) đều dẫn tới **sửa ô "Kết quả mong
> đợi" của phiếu đối tác** — cần đối tác xác nhận. Điểm 3, 4, 5 thuần nội bộ.

---

<!-- ===== DẠNG A ===== -->

## `DKTGMLTVV_13` — Hồ sơ tạo ở màn Thêm mới Tư vấn viên có mang loại "Người hỗ trợ" không

**Bối cảnh testcase**

- Dòng Excel: **35**, mã TC `DKTGMLTVV_13`.
- Nội dung kiểm tra: vai trò **Người hỗ trợ pháp lý (NHT)**, màn `Thêm mới Tư vấn viên` (`/chuyen-gia-tvv/tao-moi`),
  thao tác nhập dữ liệu hợp lệ rồi bấm `Lưu`.
- Expected trong file UAT:
  - *"Hệ thống tạo hồ sơ tư vấn viên **với loại "Người hỗ trợ"** ở trạng thái "Mới đăng ký"…"*
- Actual đối tác ghi: `Trạng thái` = `Fail`. Ô `TKM phản hồi lần 1` nêu 2 ý — nút submit tên `Lưu` chứ không phải
  `Gửi đăng ký` (*"BA xác nhận tên button sai"*) và *"25/7: Do các trường thông tin đang không đúng với thiết kế
  nên test sau"*. Ảnh đối tác `DKTGMLTVV_13.jpg` chụp đúng màn này, bản `HTPLDN · V1.0`.

**Đối chiếu SRS v3.5**

- Trường **Loại** của hồ sơ tạo ở màn này chỉ nhận **hai** giá trị: `TVV` (Tư vấn viên) hoặc `CG` (Chuyên gia).
  Ràng buộc dữ liệu ghi rõ `CHECK IN ('TVV','CG')`, và bảng thành phần màn hình khai đúng *dropdown 2 lựa chọn*.
- "Người hỗ trợ" trong đặc tả **không phải một giá trị của trường Loại** — nó là **vai trò của người thao tác**
  (tác nhân của FR-IV-03) và là **một đối tượng dữ liệu riêng** (`NGUOI_HO_TRO`), tạo ở **màn khác**
  (`/chuyen-gia-tvv/nguoi-ho-tro/tao-moi`) với **trạng thái khởi tạo khác** (`CHO_KICH_HOAT`, không phải
  `MOI_DANG_KY`).
- Đây là thay đổi **có chủ đích, đã ghi trong lịch sử sửa đổi của chính tài liệu**: bản 2026-05-03 gỡ NHT khỏi
  danh sách giá trị `loai_tvv` và tách thành đối tượng riêng.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:296` — *"| 0 | loai_tvv | text | Y | CHECK IN ('TVV','CG') | 'TVV' | NHT chọn (radio) |"*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1490` — *"| 2.2 | nhóm 1 | Loại * | dropdown 2 lựa chọn | "Tư vấn viên" / "Chuyên gia" — mặc định "Tư vấn viên" |"*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1381–1386` — bảng ánh xạ `loai_tvv`: chỉ `TVV → Tư vấn viên`, `CG → Chuyên gia`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:137` — *"CHECK IN ('TVV','CG') … NHT (cán bộ HTPL theo NĐ 55/2019 Đ.7) lưu ở entity riêng NGUOI_HO_TRO"*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2019` — entity `TU_VAN_VIEN`: *"NHT lưu ở entity riêng NGUOI_HO_TRO"*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1799` — màn tạo Người hỗ trợ: *"`/chuyen-gia-tvv/nguoi-ho-tro/tao-moi`"*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2073` — `NGUOI_HO_TRO.trang_thai` mặc định `'CHO_KICH_HOAT'`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:18` — lịch sử 2026-05-03, fix `F-FR04-NEW-02`: *"bỏ NHT khỏi loai_tvv enum + tạo entity NGUOI_HO_TRO"*

**Kết quả verify UI hiện tại**

- Verify lại ngày **07/08/2026** qua Chrome DevTools MCP, tài khoản UAT `nht_ag_uat2` — vai trò `NHT`, cấp `DP`,
  đơn vị `Sở Tư pháp An Giang`.
- Mở URL `https://18.143.165.120.nip.io/chuyen-gia-tvv/tao-moi` (vào bằng click menu, không gõ thẳng URL).
- **Trước khi nhập bất kỳ dữ liệu nào**, mở ô "Loại" và đọc nhãn từng lựa chọn: đúng **2** lựa chọn —
  `Tư vấn viên (TVV)` và `Chuyên gia (CG)`. **Không có "Người hỗ trợ".**
- Hồ sơ tạo ra (`TVV-STP-AG-0004`) mang `loaiTvv = TVV`, hiển thị trên danh sách là `Tư vấn viên`.
- Đối chiếu quan sát với đặc tả: **khớp hoàn toàn** `:296` và `:1490` — dev đang làm đúng.
- Evidence: `../F6-flow04-3case-2026-08-07/image/r35-C2-dropdown-Loai-chi-co-TVV-va-CG-V109.png`
  → https://drive.google.com/file/d/1ShIqR8mfpMvkTVO0ZDZFQrgqlfsFMfSQ/view?usp=drivesdk

**Kết luận QA**

- `DKTGMLTVV_13` (vế "loại Người hỗ trợ") **không phải bug theo SRS v3.5**.
- Web hiện tại **đúng** đặc tả: trường Loại chỉ mở ra `TVV` / `CG`, đúng tập giá trị đã khai ở `:296`, `:1490`,
  `:1381–1386`, `:137`, `:2019`.
- Expected của đối tác sai ở một điểm:
  - đang gán **"Người hỗ trợ"** — vốn là *vai trò của người đi đăng ký hộ* — thành **giá trị trường Loại của hồ sơ
    được đăng ký**. Hai khái niệm này đã được đặc tả tách bạch từ 2026-05-03 (`:18`), thậm chí tách sang màn khác
    (`:1799`) và có trạng thái khởi tạo khác (`:2073`).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị **cập nhật expected của `DKTGMLTVV_13` theo SRS v3.5**, hoặc chốt hướng ngược lại nếu nghiệp vụ thật sự đổi:

- **Hướng 1 (QA đề xuất):** sửa ô "Kết quả mong đợi" của phiếu từ *"với loại **Người hỗ trợ**"* thành
  *"với loại **Tư vấn viên** (hoặc **Chuyên gia**, theo lựa chọn khi nhập)"*. **Cần đối tác xác nhận** vì đây là
  sửa nội dung phiếu của họ.
- **Hướng 2:** nếu nghiệp vụ thật sự cần thêm giá trị "Người hỗ trợ" vào trường Loại của hồ sơ TVV, BA nhập thay
  đổi vào đặc tả trước — tối thiểu 4 chỗ: `Inputs #0` (`:296`), `SCR-IV-02` mục 2.2 (`:1490`), bảng ánh xạ §3.0
  (`:1381–1386`), entity `TU_VAN_VIEN` (`:2019`) — rồi mới verify lại. Kèm quyết định xử lý quan hệ với entity
  `NGUOI_HO_TRO` đang tồn tại song song.
- Verdict QA đề xuất: `Cần BA xác nhận`, **không gửi Dev xử lý**.

---

## `DKTGMLTVV_13` — Sau khi đăng ký thành công thì chuyển sang màn nào

**Bối cảnh testcase**

- Dòng Excel: **35**, mã TC `DKTGMLTVV_13` (cùng phiếu với case trên, khác vế của "Kết quả mong đợi").
- Nội dung kiểm tra: vai trò **NHT**, sau khi bấm `Lưu` thành công ở màn `Thêm mới Tư vấn viên`.
- Expected trong file UAT:
  - *"…hiển thị thông báo "Đăng ký thành công, chờ thẩm định" cùng mã hồ sơ đã tạo và **chuyển sang trang theo dõi
    tiến độ**."*
- Actual đối tác ghi: `Trạng thái` = `Fail` (chung cho cả phiếu).

**Đối chiếu SRS v3.5**

- Quy ước UI chung của toàn hệ thống, mức **BẮT BUỘC**, quy định **ngược** với expected: sau khi Thêm mới thành công
  thì **quay về trang Danh sách**, kèm toast thông báo.
- Quy ước đó **có** cho phép ngoại lệ (giữ lại trang Chi tiết), nhưng chỉ khi **"có ghi chú riêng tại FR cụ thể"**.
  Đọc trọn FR-IV-03 và SCR-IV-02: **không có ghi chú ngoại lệ nào**.
- Trong toàn bộ đặc tả **không tồn tại màn nào tên "trang theo dõi tiến độ"** cho luồng đăng ký TVV. Cụm chữ này
  xuất hiện đúng **1** lần trong cả thư mục `srs-v3.5/`, và thuộc **nghiệp vụ khác** (đợt báo cáo Chương trình
  HTPLDN, mô tả CB NV TW theo dõi tiến độ nộp báo cáo của các đơn vị).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:6759` — Phụ lục E §H7, **BẮT BUỘC**: *"Sau khi thực hiện thành công thao tác Thêm mới một bản ghi, hệ thống chuyển hướng về trang Danh sách (SCR-XX-01) kèm toast thông báo. Trừ trường hợp đối tác/CĐT yêu cầu giữ lại trang Chi tiết bản ghi vừa tạo (vd. cần thao tác liên hoàn — phải có ghi chú riêng tại FR cụ thể)."*
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:280–363` — trọn FR-IV-03: không có ghi chú ngoại lệ §H7
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1470–1529` — trọn SCR-IV-02: không có ghi chú ngoại lệ §H7
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:621` — **kết quả duy nhất** của chuỗi "theo dõi tiến độ" trong cả thư mục: *"CB NV TW theo dõi tiến độ nộp ở chi tiết Đợt BC (bảng đơn vị + trạng thái nộp)"* — khác nghiệp vụ

**Kết quả verify UI hiện tại**

- Verify lại ngày **07/08/2026**, tài khoản `nht_ag_uat2` (`NHT`, cấp ĐP).
- Bấm `Lưu` **một lần duy nhất** (máy chủ ghi nhận đúng 1 lượt tạo, không bấm lặp), rồi **chỉ đọc, không bấm thêm**.
- `location.href` ngay sau khi lưu: `https://18.143.165.120.nip.io/chuyen-gia-tvv/danh-sach`.
- Breadcrumb: `Trang chủ / Mạng lưới Tư vấn viên / Danh sách`. Tiêu đề màn: `Tư vấn viên / Chuyên gia`.
- Đối chiếu quan sát với đặc tả: **khớp §H7** — dev đang làm đúng quy ước bắt buộc.
- Evidence: `../F6-flow04-3case-2026-08-07/image/r35-C1-C3-C4-C5-ban-ghi-moi-Moi-dang-ky-V109.png`
  → https://drive.google.com/file/d/1BxtC8GIHUqMBcveAI0a-_FPe6rHQQYl5/view?usp=drivesdk

**Kết luận QA**

- `DKTGMLTVV_13` (vế "trang theo dõi tiến độ") **không phải bug theo SRS v3.5**.
- Web hiện tại **đúng** quy ước BẮT BUỘC §H7 (`srs-v3.5.md:6759`).
- Expected của đối tác sai ở hai điểm:
  - yêu cầu một hành vi **ngược** với quy ước bắt buộc áp cho mọi màn hình, mà FR-IV-03/SCR-IV-02 lại **không có
    ghi chú ngoại lệ** — điều kiện duy nhất để được làm khác;
  - viện dẫn một màn **không tồn tại trong đặc tả** ("trang theo dõi tiến độ") cho luồng đăng ký TVV.

**Nội dung đề xuất BA phản hồi đối tác**

- **Hướng 1 (QA đề xuất):** giữ §H7, sửa ô "Kết quả mong đợi" của phiếu thành *"…và **quay lại trang Danh sách tư
  vấn viên**"*. **Cần đối tác xác nhận.**
- **Hướng 2:** nếu nghiệp vụ thật sự cần một màn theo dõi tiến độ hồ sơ cho Người hỗ trợ, BA **định nghĩa màn đó**
  (đường dẫn, thành phần, quyền truy cập) và **ghi ngoại lệ §H7 ngay tại FR-IV-03** — đúng cơ chế ngoại lệ mà chính
  §H7 quy định — rồi mới verify lại.
- Verdict QA đề xuất: `Cần BA xác nhận`, **không gửi Dev xử lý**.

---

<!-- ===== DẠNG B ===== -->

## `QLTLPLCVV_22` (và `QLTLPLCVV_23`) — Nhóm "Tư liệu pháp lý liên kết" có được phép có ô tìm kiếm / bộ lọc không

**Bối cảnh testcase**

- Dòng Excel: **301**, mã TC `QLTLPLCVV_22` — *"Tìm kiếm tư liệu hỗ trợ tiếng Việt có dấu"*.
- Dòng Excel: **302**, mã TC `QLTLPLCVV_23` — *"Tìm kiếm hỗ trợ tiếng Việt không dấu"* (cùng vấn đề màn hình).
- Nội dung kiểm tra: vai trò **Cán bộ Nghiệp vụ**, nhóm *"Tư liệu pháp lý liên kết"* trong màn **chi tiết Tư vấn
  chuyên sâu**.
- Expected trong file UAT: nhóm này có **phương tiện nhập từ khóa và/hoặc bộ lọc** để tìm tư liệu ngay tại đó.
- Ô `TKM phản hồi lần 1` của cả 2 dòng: *"Màn hình không có chức năng"*.

> ⚠️ **Lưu ý về bằng chứng:** hai dòng 301 và 302 đính **cùng một ảnh** (`QLTLPLCVV_23.jpg` và
> `QLTLPLCVV_24.jpg` trùng khít, md5 `3d926926a8bbdfd3352f9328d55c1c39`). Ảnh chỉ chứng minh *trạng thái màn*,
> không phân biệt được vế "có dấu" với vế "không dấu" ⇒ QA đã **đo riêng từng vế**, không suy case này ra case kia.

**Kết quả verify UI hiện tại**

- Verify lại ngày **07/08/2026**, tài khoản UAT `cbnv_tw_05` (`CB_NV_TW`, cấp TW), trên bản ghi tư vấn chuyên sâu
  `TVCS-20260806-0003`.
- Mở URL `https://18.143.165.120.nip.io/tv-chuyen-sau/eb16294e-6231-45ce-9c50-fe480228f518`, mở nhóm
  *"Tư liệu pháp lý liên kết"*.
- Trong đúng khung của nhóm này có **4 ô nhập/chọn**: 1 ô từ khóa (chữ gợi ý *"Tìm theo tên hoặc mô tả tư liệu"*)
  + 3 bộ lọc `Loại tư liệu` / `Lĩnh vực` / `Trạng thái`; kèm nút `[Tìm kiếm]`, `[Xóa bộ lọc]`, `[Thêm tư liệu]`.
- Bảng tư liệu đủ **9 cột**. Tìm chạy đúng: nhóm có 2 tư liệu, gõ từ khóa → còn 1 dòng đúng bản ghi mong đợi.
- Điểm đang phù hợp đặc tả: **bảng 9 cột và nút `[+ Thêm tư liệu]`** khớp đúng thành phần đã khai ở `:1171`.
  Phần **ô tìm kiếm + 3 bộ lọc** thì không có chỗ nào trong bảng thành phần màn hình quy định — chính là điểm
  cần BA chốt.
- Evidence: `../F6-flow04-3case-2026-08-07/image/QLTLPLCVV-C1-section-co-o-tim-kiem-va-3-bo-loc-V109.png`
  → https://drive.google.com/file/d/1KGFgkn36R1FI1bBLr1cp84WUShXqe1tr/view?usp=drivesdk

> **So với bản đối tác đo:** ảnh của đối tác (bản `V1.0`) cho thấy nhóm này **chưa có** thanh lọc và bảng chỉ **7
> cột**. Tức hiện tượng *"Màn hình không có chức năng"* **không còn tái hiện** trên V1.0.9. QA vẫn **không kết luận
> "fix đã có tác dụng"** vì không có ảnh "lỗi cũ" tự chụp trên cùng môi trường.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **§Processing của FR-X.1-06**, tìm kiếm tư liệu **là yêu cầu chức năng bắt buộc**, mô tả rất chi tiết:
   - nhận tiêu chí gồm keyword (tên tư liệu, mô tả), lĩnh vực, loại tư liệu, trạng thái;
   - tìm toàn văn trên `ten_tu_lieu` + `mo_ta`;
   - áp logic AND cho tất cả điều kiện; phân trang mặc định 20/trang.

   Và màn **duy nhất** chứa FR-X.1-06 chính là nhóm tư liệu trong màn chi tiết TVCS — màn riêng SCR-X1-07 đã bị
   **gộp vào** SCR-X1-02.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:942` — *"**Processing — Tìm kiếm tư liệu** `[GAP-X.1-02]`"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:947` — *"| 2 | Nhận tiêu chí: keyword (tên tư liệu, mô tả), lĩnh vực, loại tư liệu, trạng thái | — |"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:950` — *"| 5 | AND logic cho tất cả điều kiện | — |"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:951` — *"| 6 | Phân trang (mặc định 20/trang) và trả về kết quả | BR-DATA-07 |"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:828` — *"**Màn hình:** ~~SCR-X1-07~~ (DEPRECATED v2.1 — gộp thành tab "Tư liệu PL" trong SCR-X1-02 / MH-12.2)"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1153` — *"**FR sử dụng:** FR-X.1-01, FR-X.1-03, FR-X.1-04, FR-X.1-05, **FR-X.1-06**"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1227–1229` — *"### ~~SCR-X1-07: Tư liệu Pháp lý Vụ việc~~ (DEPRECATED v2.1) > **Gộp vào:** Tab "Tư liệu PL liên kết" trong SCR-X1-02 (MH-12.2)."*

2. Nhưng **§Thành phần màn hình của SCR-X1-02** lại **không khai bất kỳ ô tìm kiếm hay bộ lọc nào** cho nhóm này —
   chỉ khai một bảng dữ liệu và nút `[+ Thêm tư liệu]`:
   - dòng thành phần liệt kê đúng 9 cột của bảng + nút `[+ Thêm tư liệu]`, hết;
   - phần mô tả bổ sung cũng chỉ nói *"CRUD tư liệu inline"* + nút Công khai.

   Và **§Acceptance Criteria của FR-X.1-06 không có tiêu chí nào cho tìm kiếm** — 9 tiêu chí đều về hiển thị danh
   sách, xem chi tiết, thêm mới, tải file, quyền của Chuyên gia, preview, công khai/hủy công khai. Đếm số lần
   xuất hiện chuỗi "tìm kiếm"/"search" trong trọn khối AC: **0**.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1171` — *"| 6 | content | Accordion: Tư liệu PL liên kết (UC152) | table | Bảng tư liệu: Tên / Loại / Lĩnh vực / Số file / Trạng thái / Công khai lúc / Người tạo / Ngày tạo / Hành động. Nút [+ Thêm tư liệu] (inline trong tab này) …"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1198` — *"- Tư liệu PL (gộp từ MH-12.7): tab "Tư liệu PL" trong accordion. CRUD tư liệu inline. Nút [Công khai lên Cổng PLQG] khi NHAP + >= 1 file"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:986–996` — trọn §Acceptance Criteria của FR-X.1-06, **0** tiêu chí về tìm kiếm

**Câu hỏi cần BA xác nhận**

Nhóm *"Tư liệu pháp lý liên kết"* trong màn chi tiết Tư vấn chuyên sâu (SCR-X1-02) **có** phải có ô nhập từ khóa và
bộ lọc để người dùng tìm tư liệu ngay tại đó không? Cần được hiểu theo hướng nào?

1. **Hướng 1 — theo §Processing FR-X.1-06 (`:942–951`):** yêu cầu tìm kiếm là bắt buộc, và vì màn riêng đã bị gộp
   vào SCR-X1-02 nên phương tiện tìm kiếm **phải** nằm ngay trong nhóm này. Phần dev đang làm là **đúng**, chỉ
   thiếu ở tài liệu.
2. **Hướng 2 — theo §Thành phần màn hình SCR-X1-02 (`:1171`, `:1198`) + §AC (`:986–996`):** nhóm này chỉ gồm bảng
   dữ liệu và nút Thêm; ô tìm kiếm + 3 bộ lọc là **phần dev làm thêm ngoài đặc tả**, cần quyết giữ hay bỏ.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth. **Không có gì để dev sửa** — web đang chạy đúng ý đối tác.
- Tạm verdict cho `QLTLPLCVV_22` và `QLTLPLCVV_23`: `Cần BA xác nhận` (đã ghi `BA confirm` lên bảng).
- **Nếu BA chọn hướng 1** (QA nghiêng về hướng này): UI hiện tại **đúng**, không phải lỗi. Owner dự kiến:
  **BA cập nhật đặc tả** — bổ sung ô tìm kiếm + 3 bộ lọc vào `SCR-X1-02 §Thành phần màn hình` (nêu rõ tìm theo
  trường nào, có mấy bộ lọc) và bổ sung tiêu chí chấp nhận tương ứng cho FR-X.1-06. Mục đích là **để đặc tả khớp
  sản phẩm đang chạy, KHÔNG chặn bàn giao**.
- **Nếu BA chọn hướng 2:** cần quyết tiếp — bỏ ô tìm kiếm/bộ lọc khỏi UI (owner `Dev FE`), hay giữ và vẫn phải bổ
  sung vào đặc tả. Lưu ý hướng này để lại một câu hỏi chưa có lời giải: **FR-X.1-06 sẽ được thực hiện ở màn nào**,
  khi màn riêng của nó (SCR-X1-07) đã bị khai tử ở `:828` và `:1227–1229`.

---

## `QLTLPLCVV_23` — Tìm kiếm tư liệu có bắt buộc hỗ trợ tiếng Việt không dấu không

**Bối cảnh testcase**

- Dòng Excel: **302**, mã TC `QLTLPLCVV_23`.
- Nội dung kiểm tra: vai trò **Cán bộ Nghiệp vụ**, ô tìm kiếm trong nhóm *"Tư liệu pháp lý liên kết"*.
- Expected trong file UAT: gõ từ khóa tiếng Việt **không dấu** vẫn ra bản ghi có tên viết **có dấu**.

**Kết quả verify UI hiện tại**

- Verify lại ngày **07/08/2026**, tài khoản `cbnv_tw_05`, trên `TVCS-20260806-0003`.
- Chọn cụm **2 từ** `Nghi dinh` chứ không dùng 1 từ: bỏ dấu của *"nghị"* là *"nghi"*, trùng tiền tố của *"nghiệp"*
  (*"nghiep"*) ⇒ tìm 1 từ sẽ mất khả năng phân biệt.
- Bấm `[Xóa bộ lọc]` để về mốc gốc: bảng **2** dòng. Gõ `Nghi dinh` (bỏ dấu hoàn toàn) → bảng còn **1** dòng, đúng
  bản ghi tên viết **CÓ DẤU** *"Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa"*.
- Đối chứng độc lập bằng phản hồi máy chủ của **chính lượt tìm đó**: `total = 1`, mã bản ghi
  `0d258d7c-9498-48b3-982d-db85a13cdb96` — **trùng khít** với tập mã của lượt gõ **có dấu** ở phiếu
  `QLTLPLCVV_22`. Tức bỏ dấu và có dấu cho ra **cùng một kết quả**.
- Điểm đang phù hợp đặc tả: khớp `:948` (*"hỗ trợ tiếng Việt unaccent"*). Điểm chưa rõ: xem mục dưới.
- Evidence: `../F6-flow04-3case-2026-08-07/image/r302-C2-tukhoa-khong-dau-Nghi-dinh-van-ra-ban-ghi-co-dau-V109.png`
  → https://drive.google.com/file/d/1PPH3XpTzzzcdmkT5ZYICy0PSgIxuq18i/view?usp=drivesdk

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **§Processing của chính FR-X.1-06**, tìm kiếm tư liệu **có** hỗ trợ không dấu — viết thẳng trong bước xử lý:

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:948` — *"| 3 | Full-text search trên ten_tu_lieu + mo_ta (**hỗ trợ tiếng Việt unaccent**) | BR-DATA-08 |"*

2. Nhưng **quy tắc gốc BR-DATA-08 ở file chính** thì **không nhắc chữ unaccent**, và **phạm vi áp dụng không có
   FR-X.1-06**; phần Ngoại lệ còn ghi rõ các entity khác chỉ "tìm kiếm theo từ khóa". Hai bảng tham chiếu ngay
   trong chính FR-12 cũng chỉ gán BR-DATA-08 cho **FR-X.1-02**, không gán cho FR-X.1-06.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5572` — *"| BR-DATA-08 | **Full-text search:** Hỏi đáp (noi_dung) và Kho câu hỏi (cau_hoi/cau_tra_loi/tu_khoa) hỗ trợ tìm kiếm toàn văn | FR-II-02, FR-X.1-02, FR-X.2-04 | … | Các entity khác: …"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1579` — *"| BR-DATA-08 | Tìm kiếm toàn văn | **FR-X.1-02** |"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1635` — *"| BR-DATA-08 | Tìm kiếm toàn văn (full-text search) cho nội dung tư vấn. Hỗ trợ tiếng Việt unaccent | Architecture AD-09 | **FR-X.1-02** | … |"*

**Câu hỏi cần BA xác nhận**

Tìm kiếm tư liệu pháp lý (**FR-X.1-06**) **có** bắt buộc hỗ trợ tiếng Việt không dấu không? Cần được hiểu theo
hướng nào?

1. **Hướng 1 — theo `:948` (bản trích trong chính FR-X.1-06):** có bắt buộc. Web hiện tại **đúng**.
2. **Hướng 2 — theo BR-DATA-08 gốc (`srs-v3.5.md:5572`) và hai bảng tham chiếu (`:1579`, `:1635`):** FR-X.1-06
   không thuộc phạm vi full-text/unaccent, chỉ cần tìm theo từ khóa thường. Web hiện tại **làm nhiều hơn yêu cầu**.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev. Ở **cả hai hướng**, web hiện tại đều **không sai** — hướng 1 là đúng yêu cầu, hướng 2 là
  làm dôi ra. Đây là câu hỏi **dọn tài liệu**, không chặn bàn giao.
- Tạm verdict cho `QLTLPLCVV_23`: `Cần BA xác nhận`. **Chuẩn chấm vòng này QA vẫn lấy `:948`** (bản trích nằm trong
  chính FR đang verify) — nêu rõ để BA biết QA đã chọn mốc nào khi đo.
- **Nếu BA chọn hướng 1:** đề nghị **đồng bộ lại phạm vi BR-DATA-08 ở file chính** (`srs-v3.5.md:5572`) và hai bảng
  tham chiếu (`:1579`, `:1635`) để bổ sung FR-X.1-06 — hiện chúng đang nói khác với `:948`.
- **Nếu BA chọn hướng 2:** đề nghị **sửa `:948`** bỏ cụm *"(hỗ trợ tiếng Việt unaccent)"* cho khỏi mâu thuẫn, và
  quyết xem có yêu cầu Dev gỡ khả năng không dấu hay giữ nguyên như phần dôi ra.

---

## `DKTGMLTVV_13` — Thông báo đăng ký thành công có bắt buộc kèm mã hồ sơ không

**Bối cảnh testcase**

- Dòng Excel: **35**, mã TC `DKTGMLTVV_13` (vế thứ ba của "Kết quả mong đợi").
- Nội dung kiểm tra: vai trò **NHT**, câu thông báo hiện ra sau khi bấm `Lưu` thành công.
- Expected trong file UAT: *"…hiển thị thông báo "Đăng ký thành công, chờ thẩm định" **cùng mã hồ sơ đã tạo**…"*

**Kết quả verify UI hiện tại**

- Verify lại ngày **07/08/2026**, tài khoản `nht_ag_uat2`.
- Vì thông báo tự tắt sau vài giây, QA **cài sẵn bộ bắt thông báo trước khi bấm** `Lưu` (không lọc trùng, đọc
  `innerText`), rồi mới bấm **một lần duy nhất**.
- Chuỗi bắt được: **"Đăng ký thành công, chờ thẩm định"** — trùng **nguyên văn** câu chuẩn ở `:351`.
  (4 node bắt được là wrapper + notice của **cùng một** thông báo, khớp đúng **1** lượt tạo phía máy chủ.)
- Câu thông báo **không chứa mã hồ sơ**. Mã `TVV-STP-AG-0004` **có** được sinh ra nhưng chỉ nằm trong dữ liệu máy
  chủ trả về, không ghép vào câu thông báo.
- Điểm đang phù hợp đặc tả: câu chữ thông báo khớp `:351` **chính xác từng chữ**.
- Evidence: `../F6-flow04-3case-2026-08-07/do/r35-POST-tu-van-viens-201.network-response` (thân phản hồi máy chủ,
  chứa `maTvv = TVV-STP-AG-0004`) và `../F6-flow04-3case-2026-08-07/image/r35-C1-C3-C4-C5-ban-ghi-moi-Moi-dang-ky-V109.png`
  → https://drive.google.com/file/d/1BxtC8GIHUqMBcveAI0a-_FPe6rHQQYl5/view?usp=drivesdk

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

> *(Case này **không** thuộc dạng "hai chỗ nói khác nhau" — đặc tả đơn giản là **không nói gì**. Ghi theo cách của
> `ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md` trong cùng thư mục.)*

1. **§Outputs của FR-IV-03 tách riêng hai thứ, không dòng nào yêu cầu ghép mã vào câu thông báo:**

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:348` — *"| 1 | ma_tvv | text | — | TVV-{CODE}-{SEQ} (auto-gen) |"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:351` — *"| 4 | thong_bao | text | — | "Đăng ký thành công, chờ thẩm định" |"*

2. **Hai chỗ còn lại có thể quy định câu thông báo cũng không nhắc:** phần mô tả nút `Lưu` của màn hình và phần
   Hậu điều kiện.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1522` — *"Lưu: tạo mới hoặc cập nhật; nếu tạo mới → đặt trạng thái Mới đăng ký + thông báo Cán bộ Nghiệp vụ cùng đơn vị "Hồ sơ tư vấn viên mới đăng ký: [tên]""*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:353–357` — trọn §Postconditions, không nhắc câu thông báo cho NHT

3. **Đối chứng ngược — khi đặc tả *muốn* kèm mã thì viết rõ**, nên sự im lặng ở trên khó coi là "hiển nhiên ngầm hiểu":

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:597` — FR-IV-07 Processing bước 2: *"…gửi mail link kích hoạt vĩnh viễn (1 lần dùng) **kèm mã số TVV**."*

**Câu hỏi cần BA xác nhận**

Câu thông báo hiện ra cho **Người hỗ trợ** sau khi đăng ký hồ sơ TVV thành công **có** bắt buộc kèm mã hồ sơ vừa
tạo không? Cần được hiểu theo hướng nào?

1. **Hướng 1 — theo đúng chữ ở `:351`:** câu thông báo là *"Đăng ký thành công, chờ thẩm định"*, hết. Mã hồ sơ là
   một output riêng, người dùng xem ở danh sách/chi tiết. Web hiện tại **đúng**.
2. **Hướng 2 — theo expected của đối tác:** câu thông báo phải kèm mã, ví dụ *"Đăng ký thành công, chờ thẩm định.
   Mã hồ sơ: TVV-STP-AG-0004"*. Khi đó `:351` **thiếu** và cần bổ sung.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt. Web đang khớp **nguyên văn** câu duy nhất mà đặc tả có ghi.
- Tạm verdict cho `DKTGMLTVV_13` (vế này): `Cần BA xác nhận`.
- **Nếu BA chọn hướng 1:** UI hiện tại **không phải lỗi**; đề nghị cập nhật expected của phiếu, bỏ vế *"cùng mã hồ
  sơ đã tạo"*. Cần đối tác xác nhận vì là sửa nội dung phiếu.
- **Nếu BA chọn hướng 2:** bổ sung **câu chuẩn đầy đủ** vào `§Outputs FR-IV-03` (`:351`) để dev và QA cùng một mốc
  — nêu rõ định dạng ghép mã, tránh mỗi bên hiểu một kiểu. Owner sau đó: `Dev FE`.

---

## Ghi nhận kèm theo — KHÔNG cần BA quyết trong file này

Ô `TKM phản hồi lần 1` của dòng 35 ghi *"Màn hình chức năng không có button Gửi đăng ký, chỉ có button Lưu là do
tên button sai hay thiếu nút chức năng vậy ạ — **BA xác nhận tên button sai**"*. QA đã kiểm và **không đưa điểm này
thành tiêu chí chấm**, vì:

- Đặc tả chốt hiện hành vẫn quy định nhãn nút của màn này là **"Lưu"** —
  `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1522` (*"Hủy" (phụ) / "Lưu"
  (chính)"*) và quy ước nhãn nút **BẮT BUỘC** áp cho mọi màn hình
  `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:6756` §H4 (*"Nút lưu luôn "Lưu""*).
- Chuỗi `"Gửi đăng ký"`: **0 kết quả** trên toàn bộ 18 tệp của thư mục `srs-v3.5/`.
- Không có dấu thay đổi nào (`[STT…]` / `[CR-…]` / `[BA chốt …]`) chạm tới nhãn nút của SCR-IV-02; 3 đợt áp UAT gần
  nhất vào FR-04 (`:24` ngày 2026-07-16, `:26` ngày 2026-07-30, `:27` ngày 2026-07-31) đều **không** đổi nhãn nút,
  dù đợt 2026-07-30 có xử đúng nhóm mã `DKTGMLTVV_02` / `DKTGMLTVV_03`.
- Bước thao tác của **chính phiếu** cũng ghi *"Dữ liệu hợp lệ và nhấn **Lưu**"* ⇒ nút `Lưu` là **tiền đề thao tác**,
  không phải kết quả mong đợi.

⇒ Quyết định *"BA xác nhận tên button sai"* **chưa được nhập vào bản đặc tả này**, nên chưa có hiệu lực để chấm.
Nếu vẫn muốn đổi tên nút, **đề nghị BA cập nhật `SCR-IV-02` (`:1522`) và quy ước `§H4` (`srs-v3.5.md:6756`) trước** —
đi đường sửa đặc tả, không đi đường verify phiếu.

---

## Phần đã đo và ĐẠT — không cần BA quyết

Ghi ở đây để BA thấy phạm vi tranh chấp chỉ nằm ở 5 điểm trên.

| Phiếu | Vế đã đo ĐẠT |
|---|---|
| `QLTLPLCVV_22` | Tìm bằng từ khóa tiếng Việt **có dấu** → bảng từ 2 dòng còn đúng 1 dòng mong đợi, khớp phản hồi máy chủ (`total = 1`) |
| `QLTLPLCVV_23` | Tìm bằng từ khóa **không dấu** → ra đúng bản ghi có dấu, tập mã trùng khít lượt có dấu |
| `DKTGMLTVV_13` | Tạo được hồ sơ `TVV-STP-AG-0004`, đơn vị tự gán đúng theo NHT · trạng thái `Mới đăng ký` · đủ **cả 2** lĩnh vực đã chọn · đúng tổ chức chính · Cán bộ Nghiệp vụ **cùng đơn vị** (đã đối chiếu trùng mã đơn vị **trước khi** chấm) nhận thông báo sau thao tác 52 ms, đúng tên ứng viên · Nhật ký hệ thống có dòng `Tạo mới` / `TU_VAN_VIEN` / mã bản ghi khớp · câu thông báo đúng nguyên văn |

**Không phiếu nào phải `Reopen`** — mọi vế đối chiếu được với đặc tả đều ĐẠT.

**Khai mutate môi trường:** lượt đo có tạo thêm dữ liệu trên env nội bộ — 1 tư liệu *"Nghị định 55/2019 hỗ trợ pháp
lý cho doanh nghiệp nhỏ và vừa"* (Nháp) gắn vào `TVCS-20260806-0003`, và 1 hồ sơ TVV `TVV-STP-AG-0004`
(`MOI_DANG_KY`) kèm 2 tệp PDF. Không đụng dữ liệu của đối tác, không sửa/xóa bản ghi có sẵn.

---

## Nguồn tra cứu

| Nội dung | Đường dẫn |
|---|---|
| Báo cáo đo dòng 301 | [`r301-QLTLPLCVV_22.md`](../F6-flow04-3case-2026-08-07/do/r301-QLTLPLCVV_22.md) |
| Báo cáo đo dòng 302 | [`r302-QLTLPLCVV_23.md`](../F6-flow04-3case-2026-08-07/do/r302-QLTLPLCVV_23.md) |
| Báo cáo đo dòng 35 | [`r35-DKTGMLTVV_13.md`](../F6-flow04-3case-2026-08-07/do/r35-DKTGMLTVV_13.md) |
| Chuẩn chấm khóa **trước** khi đo | [`QLTLPLCVV-301-302.md`](../F6-flow04-3case-2026-08-07/chuan/QLTLPLCVV-301-302.md) · [`DKTGMLTVV_13-row35.md`](../F6-flow04-3case-2026-08-07/chuan/DKTGMLTVV_13-row35.md) |
| Toàn bộ ảnh bằng chứng | [`image/`](../F6-flow04-3case-2026-08-07/image/) — bản Drive đã nhúng trong ô `Kết quả verify` của từng dòng |
