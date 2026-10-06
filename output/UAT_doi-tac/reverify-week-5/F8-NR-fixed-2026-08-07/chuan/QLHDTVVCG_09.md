# QLHDTVVCG_09 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 315 · **Mô tả (G):** Biểu mẫu chi tiết — **Nhóm 2: Vụ việc liên kết**
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhấn Xem chi tiết
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` §3 (SCR-X3-01)
**Kiểm chéo:** `srs-fr-05-vu-viec.md` §3.B (nhãn trạng thái vụ việc) + SCR-V.I-01 (định dạng mã VV / tên DN / lĩnh vực)

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống hiển thị các trường thông tin giống với thiết kế" — hiểu ở mức **đủ các cột đặc tả khai cho Nhóm 2** | `srs-fr-14-hop-dong-tv.md:279`, `:291` | **MATCH** | TEST | **UI:** mở chi tiết 1 hợp đồng **có ≥1 vụ việc liên kết** → nhóm "Vụ việc liên kết", đọc `innerText` tiêu đề cột, đối chiếu đúng 5 mục ở `:291` (Mã VV / Tên DN / Lĩnh vực / Trạng thái / [Bỏ liên kết]) + có nút `[+ Liên kết VV]`. **Đối chứng:** gọi API đọc bản ghi hợp đồng, so danh sách mã vụ việc trả về với các dòng đang hiển thị |
| **C2** | "…giống với **thiết kế**" ở mức chi tiết ngoài danh sách cột (bố cục, thứ tự, kiểu control) | `srs-fr-14-hop-dong-tv.md:274` → trỏ ra `dac-ta-man-hinh-chuc-nang-v2.md -- MH-14.1`, **tài liệu này KHÔNG có trong nguồn chuẩn** ⇒ **IM LẶNG** | **GAP** | **BA** | Chỉ chụp hiện trạng để mô tả cho BA. **CẤM Pass/Reopen** |
| **C3** | "Dữ liệu hiển thị đúng định dạng và trường thông tin" | `srs-fr-14-hop-dong-tv.md:291` + `srs-fr-05-vu-viec.md:1496`–`:1509` (nhãn + màu badge 12 trạng thái VV) + `:1648`, `:1650` | **MATCH** | TEST | **UI:** trên dòng vụ việc liên kết, đọc `innerText`: Mã VV theo khuôn `VV-{TINH}-YYYYMMDD-SEQ`, Trạng thái là **nhãn tiếng Việt** đúng bảng §B, Lĩnh vực là **tên** lĩnh vực (không phải mã). **Đối chứng:** gọi API đọc chính vụ việc đó, so `ma_vu_viec` + `trang_thai` thô với chuỗi hiển thị |
| **C4** | "Dữ liệu hiển thị không bị tràn/đè lên nhau" | `srs-fr-05-vu-viec.md:1571`–`:1572` (§C cắt chuỗi dài + tooltip) + `:1603` (§F ≥1024×768). Đặc tả **IM LẶNG** về tràn/đè bố cục | **GAP** | **BA** | Chỉ chụp hiện trạng ở 1440×900. **CẤM Pass/Reopen.** Nếu bắt gặp Tên DN dài không cắt + không tooltip → quan sát độc lập vi phạm §C, xử theo gate "bug mới tự lộ" |
| **C5** | "…đồng nhất ngôn ngữ hiển thị" | `srs-fr-05-vu-viec.md:1492` + `:1496`–`:1509` | **MATCH** | TEST | **UI:** đọc `innerText` tiêu đề cột + ô Trạng thái, khẳng định không có mã DB (`DANG_XU_LY`, `HOAN_THANH`…) và không lẫn tiếng Anh. **Đối chứng:** API trả mã DB → chứng minh có lớp dịch nhãn |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:279`**
```
**Form thêm/sửa:** Trang mới với Accordion: Thông tin chung / Vụ việc liên kết / Mốc tiến độ / Thanh toán giai đoạn / Nhật ký.
```

**`srs-fr-14-hop-dong-tv.md:291`** (thành phần Nhóm 2 — **danh sách cột duy nhất đặc tả khai**)
```
| 7 | content (form) | Accordion: Vụ việc liên kết | table + modal | Bảng VV liên kết: Mã VV / Tên DN / Lĩnh vực / Trạng thái / [Bỏ liên kết]. Nút [+ Liên kết VV] -> modal multi-select. N:N | click -> action | trang thêm/sửa — chỉ CB NV |
```

**`srs-fr-14-hop-dong-tv.md:274`**
```
**UX-Spec ref:** dac-ta-man-hinh-chuc-nang-v2.md -- MH-14.1
```
> ⚠️ Đã `find` toàn repo lượt này: **không tồn tại** ⇒ C2 khóa `GAP`.

**`srs-fr-14-hop-dong-tv.md:90`** (Inputs FR-X.3-01 — trường vụ việc liên kết)
```
| 10 | vu_viec_ids | identifier[] | N | FK[] -> VU_VIEC (many-to-many) | — | người dùng chọn |
```

**`srs-fr-05-vu-viec.md:1496`–`:1509`** (§B — ánh xạ `VU_VIEC.trang_thai` → nhãn UI, trọn bảng)
```
| Mã DB | Nhãn UI | Màu badge |
|-------|---------|-----------|
| `MOI_TAO` | Mới tạo | Xám nhạt |
| `CHO_TIEP_NHAN` | Chờ tiếp nhận | Xanh dương |
| `DA_TIEP_NHAN` | Đã tiếp nhận | Xanh lá |
| `DANG_KIEM_TRA` | Đang kiểm tra | Vàng |
| `YEU_CAU_BO_SUNG` | Yêu cầu bổ sung | Cam |
| `DA_PHAN_CONG` | Đã phân công | Xanh dương đậm |
| `DANG_XU_LY` | Đang xử lý | Vàng đậm |
| `CHO_PHE_DUYET` | Chờ phê duyệt | Cam đậm |
| `DA_DUYET` | Đã duyệt | Xanh lá đậm |
| `HOAN_THANH` | Hoàn thành | Xám |
| `DA_DANH_GIA` | Đã đánh giá | Tím |
| `TU_CHOI` | Từ chối | Đỏ |
```

**`srs-fr-05-vu-viec.md:1648`** + **`:1650`** (định dạng Mã VV và Lĩnh vực trên bảng danh sách VV)
```
| 13 | table | Mã vụ việc | text (link) | VV-{TINH}-YYYYMMDD-SEQ (160px) | click → MH-05.3 | Luôn |
| 15 | table | Lĩnh vực pháp luật | text | Tên lĩnh vực (tra cứu từ Danh mục) (150px) | — | Luôn |
```

**`srs-fr-05-vu-viec.md:1649`** (Tên DN — quy ước cắt)
```
| 14 | table | Tên doanh nghiệp | text | ten_doanh_nghiep (200px, cắt 40 ký tự) | — | Luôn |
```

**`srs-fr-05-vu-viec.md:1571`–`:1572`** (§C)
```
- Cột tên / tiêu đề > 30 ký tự: cắt + dấu `...` cuối + tooltip hover hiển thị nội dung đầy đủ
- Cột mô tả ngắn > 50 ký tự: cắt + tooltip
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)**. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `srs-fr-14-hop-dong-tv.md:68` và `:291` ("trang thêm/sửa — **chỉ CB NV**") | `:68`, `:291` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Dữ liệu — quyết định** | **1 hợp đồng có ≥1 vụ việc liên kết.** Không có liên kết thì bảng Nhóm 2 rỗng ⇒ **C1/C3/C4/C5 không đo được**, phải ghi Chưa chốt chứ không Pass. Đây là tiền đề đắt nhất của phiếu này | `:291` (bảng VV liên kết), `:90` |
| **Dữ liệu — chất lượng** | Vụ việc liên kết nên có: Tên DN **> 40 ký tự** (để đo §C ở C4) và Trạng thái ở một mã có nhãn rõ ràng (vd `DANG_XU_LY` → "Đang xử lý") để đo C3/C5 | `srs-fr-05-vu-viec.md:1649`, `:1496`–`:1509` |
| **Cách dựng** | Ưu tiên dùng lại hợp đồng QA sẵn có đã có liên kết. Nếu phải tạo, dựng qua chính chức năng "+ Liên kết vụ việc" — **trùng với phiếu `_22`** ⇒ chạy `_22` trước, dùng lại kết quả làm tiền đề cho `_09` (xem thứ tự chạy ở `00-TONG-HOP-QLHDTVVCG.md`) | — |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Bảng Nhóm 2 rỗng vẫn "đúng thiết kế".** Bảng 0 dòng chỉ chứng minh **khung bảng** tồn tại; C3/C4/C5 chấm **dữ liệu hiển thị** nên **không đo được**. Không có vụ việc liên kết ⇒ ghi Chưa chốt, tuyệt đối không Pass bằng ảnh bảng rỗng.
- **Cột Trạng thái hiển thị đúng vì vụ việc tình cờ ở trạng thái có nhãn "dễ".** Một mã đúng không chứng minh cả bảng ánh xạ đúng — nhưng cột K **không** đòi phủ 12 trạng thái ⇒ **không** mở rộng thành ma trận trạng thái (flow 04 luật khóa 4). Đo 1 dòng, ghi rõ đã đo mã nào.
- **Nhãn "Lĩnh vực" hiển thị mã danh mục.** `srs-fr-05-vu-viec.md:1650` đòi **tên** lĩnh vực tra từ Danh mục. Thấy `LV01`/UUID là **Fail** C3/C5, dễ bị bỏ qua vì trông giống dữ liệu hợp lệ.
- **Đọc bằng `textContent`** → gom node ẩn, thấy nhãn tiếng Việt không thật sự hiển thị. Dùng `innerText`.

**Dễ Fail oan:**
- **Fail vì chấm theo bản vẽ Figma / ảnh đối tác.** `MH-14.1` không có trong nguồn chuẩn ⇒ đó chính là lý do C2 khóa `GAP`.
- **Fail vì bảng có thêm cột ngoài `:291`.** Đặc tả liệt kê cột **bắt buộc có**, không cấm thêm. Thừa cột ⇒ ghi nhận cho BA.
- **Fail vì cột `[Bỏ liên kết]` là icon chứ không phải chữ.** Phụ lục E §H6 (`srs-v3.5.md:6758`) bắt cột Hành động dùng **icon + tooltip** thay nhãn text ⇒ icon là **đúng** đặc tả.
- **Fail vì Tên DN bị cắt cụt.** `srs-fr-05-vu-viec.md:1649` quy định **cắt 40 ký tự**, `:1571` quy định cắt + `...` + tooltip. Bị cắt là **đúng**; chỉ sai khi cắt mà **không có tooltip**.
- **Fail vì màn xem chi tiết không có nút `[+ Liên kết VV]`.** `:291` khai nút này cho **trang thêm/sửa**; đặc tả không khai bảng thành phần cho trang xem chi tiết (chỉ nhắc ở `:294`–`:295`). Thiếu nút trên màn chỉ-xem ⇒ đưa vào câu hỏi BA gộp, không Fail C1.
