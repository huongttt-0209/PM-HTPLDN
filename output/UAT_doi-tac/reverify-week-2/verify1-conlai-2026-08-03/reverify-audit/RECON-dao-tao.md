# RECON — tiền đề test 5 case luồng "Đào tạo, tập huấn"

> **Đây KHÔNG phải verdict.** File chỉ dọn sẵn tiền đề (§Nguyên tắc 4 QA_VERIFY_PROTOCOL) để người verify khỏi mất thời gian dò.
> Mọi kết luận Open/Reject/BA confirm/Resolved vẫn phải qua đủ 3 CỔNG + bảng đối chiếu điều kiện + artifact real-data.
>
> **Ngày recon:** 2026-08-03 (env `https://18.143.165.120.nip.io`) · **Người recon:** AGENT-RECON (chỉ đọc file + curl, KHÔNG dùng browser, KHÔNG ghi sheet)

---

## 0. Bảng tổng — 5 case

| Mã TC | Tiền đề SẴN SÀNG? | Mã bản ghi dùng được | Tài khoản | Nếu thiếu thì seed gì |
|---|---|---|---|---|
| **KTDGKQHT_02** | ✅ **SẴN** | `KH-20260716-002` (chính) · `KH-2026-001` (dự phòng) | `cbnv_tw` / `Test@1234` | — không cần seed |
| **QLKTLBG_09** | ✅ **SẴN — recon đã seed** (trước đó 0 tệp Slide) | Bài giảng `RECON 03/08 - Bai giang SLIDE (pptx) kiem thu QLKTLBG_09` — id `53b83ff6-c381-44e9-b4be-a6e7d2610313` | `cbnv_tw` / `Test@1234` | Đã seed 1 file `.pptx` thật. Muốn chắc hơn thì upload lại 1 pptx **qua UI** |
| **QLDXDTTH_01** | ✅ **SẴN** | Đề xuất tham chiếu `d3e209a9-12b9-4adf-8f7d-5adac62c6a91` (DN) · `4f0e973e…` / `647503ce…` (NHT) | DN `0109998887` / `Test@1234` · NHT `nht_qa_01` / `Test@1234` | — không cần seed (case là **tạo mới**, chỉ cần tài khoản + `linhVucId`) |
| **QLLKHDTBD_09** | ✅ **SẴN** (cả 2 màn) | Kế hoạch đào tạo: 12 bản ghi · Kho bài giảng: 7 bản ghi | `cbnv_tw` / `Test@1234` | — không cần seed. ⚠️ Xem §4 về **màn hình nào** |
| **PDKHDTTH_04** | ✅ **SẴN — recon đã seed** (trước đó 0 kế hoạch ở "Chờ duyệt") | `KH-20260803-0002` (khác cấp — dùng cho case) · `KH-20260803-0001` (cùng cấp — baseline đối chứng) | `cbpd_tw_01` / `Test@1234` (⚠️ `cbpd_tw` login FAIL 401) | Đã seed 2 kế hoạch ở trạng thái Chờ duyệt |

---

## 1. KTDGKQHT_02 — chi tiết Khóa học → tab "Điểm danh" / "Kết quả kiểm tra"

**Đối tác phản ánh (nguyên văn, `bug-con-fail-doi-tac-2026-07-31.csv` row 260):**
> "Tab "Kết quả kiểm tra" hiển thị thiếu các trường thông tin: Số buổi có mặt, Số buổi vắng có phép, Số buổi vắng không phép, Tổng số buổi"
> Bằng chứng: `KTDGKQHT_02_v2.jpg`, `KTDGKQHT_02_v2(2).jpg`

### Tiền đề có sẵn

Env có **14 khóa học** (tabCounts: DU_THAO 1 · CHO_DUYET 1 · DA_DUYET 1 · DANG_DIEN_RA 2 · DA_KET_THUC 2 · HOAN_THANH 7). Trong đó có đủ khóa vừa có học viên, vừa có điểm danh, vừa có kết quả kiểm tra:

| Mã khóa học | id | Trạng thái | Học viên | Điểm danh | Kết quả | Lịch học |
|---|---|---|---|---|---|---|
| **`KH-20260716-002`** ⭐ | `033910fc-895d-432a-8407-8f7f0a9516c2` | HOÀN THÀNH | 2 | **4** (đủ 3 trạng thái) | 2 | 2 buổi |
| `KH-2026-001` | `f0cccccc-0000-4000-8000-000000000001` | HOÀN THÀNH | 2 | 2 | 2 | 1 |
| `KH-2026-002` | `f0cccccc-0000-4000-8000-000000000002` | HOÀN THÀNH | 2 | 2 | 2 | 1 |
| `AAA-KH-TW` | `aaaa1111-0000-4000-8000-000000000001` | HOÀN THÀNH | 4 | 4 | 4 | 2 |
| `KH-SEED-0001` | `5eed0002-0000-4000-8000-000000000001` | ĐÃ KẾT THÚC | 8 đăng ký | 1 | 1 | 2 |

**Vì sao chọn `KH-20260716-002` làm bản ghi chính:** đây là khóa DUY NHẤT có điểm danh phủ **cả 3 trạng thái** `CO_MAT` · `VANG_PHEP` · `VANG_KHONG_PHEP` — đúng 3 loại mà đối tác nói đang thiếu. Dữ liệu thực:

```
DD: QA HV RV5 Hai  | 2026-09-19 | CO_MAT           | coMat=true
DD: QA HV RV5 Hai  | 2026-09-19 | VANG_PHEP        | coMat=false
DD: QA HV RV5 Mot  | 2026-09-19 | VANG_KHONG_PHEP  | coMat=false
DD: QA HV RV5 Mot  | 2026-09-19 | VANG_KHONG_PHEP  | coMat=false
KQ: QA HV RV5 Hai  | soBuoiCoMat=1 | tongBuoi=2 | tyLeChuyenCan=100.00 | diem=1.5 | KHONG_DAT | KHONG_DAT
KQ: QA HV RV5 Mot  | soBuoiCoMat=0 | tongBuoi=2 | tyLeChuyenCan=0.00   | diem=null| null      | null
```

`KH-2026-001` dùng làm dự phòng (số đẹp hơn: `soBuoiCoMat=9 / tongBuoi=10 / tyLeChuyenCan=90.00 / diem=8.5 / DAT / GIOI`).

### Dữ kiện quan trọng cho người verify — máy chủ trả gì

Đo `GET /api/v1/khoa-hocs/{id}/ket-quas` → các trường trả về:

```
congBo · dangKyId · diemKiemTra · email · ghiChu · hoTen · id · ketQua ·
lyDoHuyCongBo · soBuoiCoMat · soDienThoai · tenDonVi · thoiGianCongBo ·
tongBuoi · tyLeChuyenCan · xepLoai
```

Đối chiếu 4 trường đối tác nói thiếu:

| Trường đối tác đòi | Máy chủ có trả? | Ghi chú |
|---|---|---|
| Số buổi có mặt | ✅ **CÓ** — `soBuoiCoMat` | ⇒ nếu giao diện không hiện thì là **giao diện chưa render**, không phải máy chủ thiếu |
| Tổng số buổi | ✅ **CÓ** — `tongBuoi` | ⇒ như trên |
| Số buổi vắng **có phép** | ❌ **KHÔNG** | Chỉ có trạng thái từng buổi ở `diem-danhs.trangThai = VANG_PHEP`, không có số tổng hợp |
| Số buổi vắng **không phép** | ❌ **KHÔNG** | Chỉ có `diem-danhs.trangThai = VANG_KHONG_PHEP` |

`GET /api/v1/khoa-hocs/{id}/diem-danhs` trả: `coMat · donVi · email · ghiChu · hoTen · hocVienId · id · ngayDiemDanh · soDienThoai · trangThai`.

> **Điểm cần soi thêm khi verify (chưa kết luận):** `QA HV RV5 Hai` có `soBuoiCoMat=1 / tongBuoi=2` nhưng `tyLeChuyenCan=100.00`. Có thể do buổi vắng CÓ PHÉP vẫn tính vào chuyên cần — cần đối chiếu SRS trước khi coi là lỗi.

### Tiền đề THIẾU
Không. **Không cần seed.**

### Tài khoản nên dùng
`cbnv_tw` / `Test@1234` (CB_NV_TW, đơn vị `00000000-0000-4000-8000-000000000001`) — tất cả các khóa trên đều thuộc đơn vị này trừ `AAA-KH-DP` / `AAA-KH-BN` / `DDD-KH-*`.

### Lịch sử case anh em (tái dùng được)
- **`BUG-KTDGKQHT_01`** (đã Closed 14/07) cùng bản chất: tab "Kết quả" & "Điểm danh" thiếu cột Email/SĐT/Đơn vị/Xếp loại theo `FR-III-05 §Outputs` (dòng 574–590) + Tab Điểm danh (dòng 1822) → verdict `Open`.
  → `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/bug-reports/Pass-bug-report-UAT-tuan-2.md` (dòng 29, 106)
  → `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/reverify-report-week-2.md:101`
- `KTDGKQHT_03` (Reject → Reopen ×2 → **Pass** rv7) và `KTDGKQHT_08` (**Pass** rv7): khung cond dùng lại được.
  → `.../reverify-week-2/reverify-audit/rv7-conditions/KTDGKQHT_03.md` · `.../rv7-conditions/KTDGKQHT_08.md`
- BA chốt 16/07: khóa chưa kết thúc thì tab "Kết quả kiểm tra" hiện nhãn **"Kết quả tạm tính"**.
  → `.../reverify-week-2/phan-tich-KTDGKQHT-03-08.md:282`
- Ghi nhận chưa đóng: "Tab Điểm danh không tự làm mới sau khi duyệt đăng ký học viên — phải tải lại trang."
  → `.../reverify-week-2/bug-reports/ba-approved-batch/reverify-ba-approved-batch-2026-07-16.md:826`

---

## 2. QLKTLBG_09 — Kho tài liệu / Bài giảng → mở tệp Slide (ppt/pptx)

**Đối tác phản ánh (row 281):**
> "Hệ thống thực hiện tải xuống slide, không trình chiếu inline"
> Bằng chứng: `QLKTLBG_09_v2.webm`

### Tiền đề có sẵn (SAU khi recon seed)

Trước recon env có **6 bài giảng: 5 PDF + 1 VIDEO — 0 tệp Slide** ⇒ case này **không thể verify** nếu không seed. Recon đã seed:

| Trường | Giá trị |
|---|---|
| Tên bài giảng | `RECON 03/08 - Bai giang SLIDE (pptx) kiem thu QLKTLBG_09` |
| id | `53b83ff6-c381-44e9-b4be-a6e7d2610313` |
| Loại tài liệu | `SLIDE` |
| Lĩnh vực | Thuế |
| Dung lượng | 4.5 KB (4624 byte) |
| Tên tệp | `qa-recon-slide-QLKTLBG_09.pptx` (pptx thật, mở được, 1 slide có chữ) |
| fileId | `49871f89-8b54-4a88-8ac2-b990691aae65` |
| Trạng thái quét virus | `SACH` |
| Đơn vị | TW `00000000-0000-4000-8000-000000000001` |

Sau seed: `GET /api/v1/bai-giangs?loaiTaiLieu=SLIDE` → **total = 1**. Tổng kho: 7 (5 PDF · 1 VIDEO · 1 SLIDE).

Tệp nguồn còn ở: `/private/tmp/claude-501/-Users-huongttt-Downloads-antigravity-PM-HTPLDN-skilkk/36873cfb-2fb0-4276-96cd-7a052f84e463/scratchpad/qa-recon-slide-QLKTLBG_09.pptx`

### Dữ kiện quan trọng cho người verify — máy chủ trả gì khi bấm "Xem trực tuyến"

`GET /api/v1/bai-giangs/{id}/preview-url` trả **URL ký hạn 300 giây trỏ thẳng tới tệp .pptx THÔ** trên kho lưu trữ:

```
https://18.143.165.120.nip.io/htpldn/<donVi>/2026/08/<fileId>/qa-recon-slide-QLKTLBG_09.pptx
  ?response-content-disposition=inline&X-Amz-Algorithm=...&X-Amz-Expires=300&...
```

Tải thử URL đó (GET, range 0-0) → header thật:

```
HTTP/2 206
content-disposition: inline
content-type: application/vnd.openxmlformats-officedocument.presentationml.presentation
content-security-policy: frame-ancestors 'none'; object-src 'none'; base-uri 'self'
```

⇒ Máy chủ **không chuyển đổi** pptx sang dạng xem được trên trình duyệt; và header `frame-ancestors 'none'` còn chặn nhúng tệp vào khung iframe. Người verify cần tự chạy thao tác trên UI để xác nhận hành vi thật (đây mới là artifact hợp lệ), nhưng bối cảnh kỹ thuật đã rõ.

> ⚠️ `HEAD` lên URL ký trả **403** (chữ ký chỉ cấp cho GET) — đừng nhầm 403 này là lỗi phân quyền.

### Tiền đề THIẾU
Đã bù. Nếu người verify muốn loại trừ khả năng "bản ghi seed qua API khác bản ghi tạo qua UI" (bài học `feedback-reverify-stored-field-fix-on-fresh-data`) → **upload thêm 1 pptx qua giao diện** rồi test trên bản ghi mới đó.

Cách seed lại nếu cần (2 bước):
```bash
# B1 — upload tệp (field BẮT BUỘC tên là "file")
curl -sk -b $CJ -X POST https://18.143.165.120.nip.io/api/v1/bai-giangs/upload-file \
  -F 'file=@duong/dan/file.pptx;type=application/vnd.openxmlformats-officedocument.presentationml.presentation'
# → trả {id, tenFile, dungLuong, duongDan, trangThaiQuet}

# B2 — tạo bản ghi bài giảng, fileUrl = duongDan ở B1
curl -sk -b $CJ -H 'Content-Type: application/json' -X POST https://18.143.165.120.nip.io/api/v1/bai-giangs \
  -d '{"tenBaiGiang":"...","loaiTaiLieu":"SLIDE","fileUrl":"<duongDan>","dungLuong":<byte>,"congKhai":false,"linhVucIds":["bbbbbbbb-0000-4000-8000-000000000018"]}'
```

### Tài khoản nên dùng
`cbnv_tw` / `Test@1234`.

### Lịch sử case anh em (tái dùng được — RẤT sát)
- **`QLBMHD_17`** (module Biểu mẫu) verdict **`Open`**, y hệt hiện tượng: FE mở `window.open('/api/v1/.../preview')` → 302 tới file thô `response-content-disposition=inline` → trình duyệt không render Office file → hộp thoại tải về. Đối chiếu `srs-fr-09-bieu-mau.md:320-327` (docx→PDF, xlsx→bảng read-only, không hỗ trợ→thông báo + tải).
  → `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-3/cond/QLBMHD_17.md`
- **BA chốt 30/07 cho chính màn Kho bài giảng:** "**Thành phần 6 — Bảng xem trước:** Slide/PDF xem trực tiếp trong trình duyệt; Video nhúng khung YouTube; định dạng không xem được → "Không thể xem trực tuyến" + nút "Tải về"."
  → `.../reverify-week-2/phan-hoi-ba-confirmation-week2-vong2-va-tkdghqhtpl-r2.md:112,116`
- `QLKTLBG_02` (`BA confirm` → BA chốt 30/07 là bug thật, bảng phải đủ 9 cột): khung cond tốt.
  → `.../reverify-week-2/reverify-audit/QLKTLBG_02/audit.md` · `.../reverify-week-2/cond/QLKTLBG_02-r2.md` · `QLKTLBG_02-r4.md`

---

## 3. QLDXDTTH_01 — Doanh nghiệp / NHT gửi đề xuất đào tạo, tập huấn

**Đối tác phản ánh (row 337):**
> "Hệ thống hiển thị thông báo thành công nhưng đề xuất không hiển thị trên màn hình"
> Bằng chứng: `QLDXDTTH_01_v2.webm`

### Tiền đề có sẵn

**Endpoint:** `/api/v1/de-xuat-dao-taos`
- `GET` — tham số lọc: `keyword`, `trangThai`, `linhVucId`
- `POST` — body `CreateDeXuatDaoTaoDto`: **bắt buộc** `linhVucId` (uuid) + `noiDung` (1–5000 ký tự); tuỳ chọn `thoiGianMongMuon` (≤100), `diaDiemMongMuon` (≤200), `soLuongDuKien` (≥1)
- Vòng đời: `MOI_GUI` → `DA_TIEP_NHAN` → `DANG_XU_LY` → `DA_XU_LY` / `TU_CHOI`
- Các bước xử lý: `POST /{id}/receive` · `/{id}/process` · `/{id}/complete` · `/{id}/reject`

**Đề xuất hiện có — 4 bản ghi (theo tầm nhìn `cbnv_tw`):**

| Trạng thái | Lĩnh vực | Nội dung (rút gọn) | Đơn vị | id |
|---|---|---|---|---|
| MOI_GUI | Thương mại | REVERIFY QLDXDTTH_09 … | An Giang `8002-…0006` | `4f0e973e-faae-4e89-ba63-d2f0dd69612e` |
| MOI_GUI | Đất đai | QA UAT _09b … | An Giang `8002-…0006` | `647503ce-18c4-4b2a-afe1-85502593da26` |
| DA_TIEP_NHAN | Thuế | QA UAT _09 An Giang … | An Giang `8002-…0006` | `c49a2fda-e309-4689-ae2c-878a82f4c1ae` |
| DA_TIEP_NHAN | Thuế | QA UAT verify — đề xuất đào tạo … | Hà Nội `8002-…0001` | `d3e209a9-12b9-4adf-8f7d-5adac62c6a91` |

**Phạm vi nhìn thấy đã đo:** DN `0109998887` (đơn vị `8002-…0001`) thấy **1** — đúng đề xuất của chính mình. NHT `nht_qa_01` (đơn vị `8002-…0006`) thấy **3**. `cbnv_dp_01` (An Giang) thấy **3**. `cbnv_bn` thấy **0**. `cbnv_tw` thấy **4**.

**Quyền đã đo (`GET /api/v1/auth/me`):**
- DN `0109998887`: `create_de_xuat_dao_tao` · `read_de_xuat_dao_tao` · `update_de_xuat_dao_tao` · `delete_de_xuat_dao_tao` ✅
- NHT `nht_qa_01`: đủ cả 4 quyền trên ✅

**Lĩnh vực pháp lý để chọn khi nhập (`GET /api/v1/danh-muc?loaiDanhMuc=LINH_VUC_PL&trangThai=KICH_HOAT` — 10 mục):**

| Mã | Tên | id |
|---|---|---|
| THUE | Thuế | `bbbbbbbb-0000-4000-8000-000000000018` |
| LAO_DONG | Lao động | `bbbbbbbb-0000-4000-8000-000000000013` |
| DAT_DAI | Đất đai | `bbbbbbbb-0000-4000-8000-000000000014` |
| DAN_SU | Dân sự | `bbbbbbbb-0000-4000-8000-000000000010` |
| THUONG_MAI | Thương mại | `bbbbbbbb-0000-4000-8000-00000000001c` |
| HINH_SU | Hình sự | `bbbbbbbb-0000-4000-8000-000000000011` |
| HANH_CHINH | Hành chính | `bbbbbbbb-0000-4000-8000-000000000012` |
| SHTT | Sở hữu trí tuệ | `bbbbbbbb-0000-4000-8000-000000000019` |
| DOANH_NGHIEP | Doanh nghiệp | `bbbbbbbb-0000-4000-8000-00000000001a` |
| DAU_TU | Đầu tư | `bbbbbbbb-0000-4000-8000-00000000001b` |

### Tiền đề THIẾU
Không. Case là **tạo mới** nên chỉ cần tài khoản + lĩnh vực — đã đủ. Đừng seed thêm đề xuất trước khi test, vì phép đo chính là *"số bản ghi trước khi gửi → sau khi gửi"*.

> **Gợi ý phép đo (loại claim: Thao tác/state + Filter/count):** đếm số dòng danh sách TRƯỚC khi gửi → gửi (bắt thông báo bằng `tools/toast-capture.js`, **đếm số request kèm số thông báo**) → đếm lại danh sách SAU khi gửi, **không tải lại trang** → rồi tải lại trang đếm lần nữa. Nếu chỉ hiện sau khi tải lại thì bản chất là "danh sách không tự làm mới", khác với "không lưu được".

### Tài khoản nên dùng
- Vai trò DN: **`0109998887`** / `Test@1234` (QA UAT Kiểm Thử DN, đơn vị `8002-…0001` Hà Nội). ⚠️ **Hộp thư nhận OTP là `qa.uat.dn.verify@test.htpldn.vn`**, KHÔNG phải tên đăng nhập — tìm đúng hộp này trong MailHog.
- Vai trò NHT: **`nht_qa_01`** / `Test@1234` (đơn vị `8002-…0006` Sở Tư pháp An Giang).

### Lịch sử case anh em (tái dùng được)
- `QLDXDTTH_03` (rv4 Reopen → **rv5 Pass**): DN chỉ thấy đề xuất của mình + màn chi tiết ẩn hết nút của cán bộ.
  → `.../reverify-week-2/reverify-audit/rv4-conditions/QLDXDTTH_03.md` · `.../rv5-conditions/QLDXDTTH_03.md`
- `QLDXDTTH_06` (rv4 Reopen → **rv5 Pass**): DN có nút [Xóa], toast "Đã xóa đề xuất", danh sách cập nhật.
  → `.../reverify-week-2/reverify-audit/rv4-conditions/QLDXDTTH_06.md` · `.../rv5-conditions/QLDXDTTH_06.md`
- `QLDXDTTH_09` (Open Major → **Closed** 15/07): CB NV nhận thông báo khi DN/NHT gửi đề xuất.
  → `.../reverify-week-2/cond/QLDXDTTH_09.md` · `.../reverify-week-2/bug-reports/Pass-BUG-gui-dev-3-loi-con-lai.md`

---

## 4. QLLKHDTBD_09 — lọc rồi Xuất Excel

**Đối tác phản ánh (row 354):**
> Tên chức năng ở phiếu: "Xuất Excel với điều kiện lọc"
> "Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách"
> Tóm tắt lỗi ở cột mô tả: "Xuất Excel không theo điều kiện lọc, hệ thống xuất toàn bộ **danh sách bài giảng**."
> Bằng chứng: `QLLKHDTBD_09.webm`

### ⚠️ Việc PHẢI làm trước tiên — xác định đúng màn hình

Mã `QLLKHDTBD` thuộc nhóm **Kế hoạch đào tạo**, nhưng chữ trong phiếu của đối tác lại nói **"danh sách bài giảng"**. Hai màn khác nhau, hai endpoint khác nhau. **Người verify phải mở `QLLKHDTBD_09.webm` xem đối tác đang đứng ở màn nào** rồi mới chọn surface — nếu chấm nhầm màn thì hỏng cả Cổng 1 lẫn bảng đối chiếu điều kiện. Recon đã chuẩn bị tiền đề cho **cả hai**.

### 4a. Nếu là màn Kế hoạch đào tạo

Endpoint: `GET /api/v1/ke-hoach-dao-taos` (lọc: `keyword`, `nam`, `trangThai`, `tuNgay`, `denNgay`) · xuất: `POST /api/v1/ke-hoach-dao-taos/export` (body cùng bộ tham số).

Tổng **12 bản ghi** (đã gồm 2 bản recon seed cho case PDKHDTTH_04). Phân bố: `NHAP` 6 · `CHO_DUYET` 2 · `DA_DUYET` 3 · `DA_CONG_KHAI` 1 · `TU_CHOI` 0. Tất cả đều `nam=2026`, cùng đơn vị TW.

**Bộ lọc tách được tập con (đã đo, đúng yêu cầu "N < tổng M"):**

| Bộ lọc | Số bản ghi trên danh sách | Số dòng dữ liệu trong file xuất |
|---|---|---|
| (không lọc) | 12 | **12** |
| `trangThai = Nháp` | 6 | **6** |
| `trangThai = Đã duyệt` | 3 | **3** |
| `trangThai = Chờ duyệt` | 2 | — |
| `trangThai = Đã công khai` | 1 | — |
| từ khoá `Seed` | 1 | **1** |
| từ khoá `QA` | 5 | — |
| `nam = 2025` hoặc `2027` | 0 | — |

**Tiêu chí lọc khuyến nghị:** `trangThai = Đã duyệt` (3/12) hoặc từ khoá `Seed` (1/12) — chênh lệch đủ lớn để chứng minh dứt khoát.

Header file xuất: `Mã KH · Tên kế hoạch · Năm · Từ ngày · Đến ngày · Ngân sách (VNĐ) · Trạng thái` (sheet "Kế hoạch đào tạo").

### 4b. Nếu là màn Kho tài liệu / Bài giảng

Endpoint: `GET /api/v1/bai-giangs` (lọc: `loaiTaiLieu`, `linhVucId`, `khoaHocId`, `congKhai`, `tuNgay`, `denNgay`, `keyword`) · xuất: `POST /api/v1/bai-giangs/export`.

Tổng **7 bản ghi** (sau khi recon seed 1 tệp Slide).

| Bộ lọc | Số bản ghi | Số dòng dữ liệu trong file xuất |
|---|---|---|
| (không lọc) | 7 | **7** |
| `loaiTaiLieu = PDF` | 5 | **5** |
| `loaiTaiLieu = Slide` | 1 | **1** |
| `loaiTaiLieu = Video` | 1 | — |

Header file xuất: `Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo · Ngày tạo · Mô tả` (sheet "Bài giảng").

### Dữ kiện quan trọng cho người verify

**Ở tầng máy chủ, việc xuất file ĐANG bám bộ lọc — cả hai màn.** Recon đã gọi thẳng endpoint xuất kèm tham số lọc rồi mở file bằng `openpyxl` đếm dòng: số dòng khớp chính xác số bản ghi của bộ lọc (bảng trên).

⇒ Nếu trên giao diện vẫn ra đủ danh sách thì nghi vấn nằm ở chỗ **giao diện có gửi kèm bộ lọc vào phần thân yêu cầu hay không**. **Bắt buộc đọc thân yêu cầu `POST …/export`** khi bấm nút Xuất Excel (đây chính là phương pháp thứ hai mà `QLKCHTV_13` đã dùng), đừng chỉ so số dòng.

> ⚠️ **Không được kết luận chỉ bằng dung lượng file** — chênh lệch dung lượng giữa các lần xuất rất nhỏ (6.789 → 7.516 byte cho 1 → 12 dòng). **Mở file đếm dòng** (bài học `feedback-verify-export-file-content-not-just-creation`).

### Tiền đề THIẾU
Không.

### Tài khoản nên dùng
`cbnv_tw` / `Test@1234`.

### Lịch sử case anh em (tái dùng được)
- Quy tắc gốc **BR-DATA-06**: "File xuất theo bộ lọc hiện tại, không vượt quá 10.000 rows/file" (`srs-v3.5` dòng 5434).
  → `.../reverify-week-2/ba-confirmation-needed-week-2.md:893`
- BA chốt 30/07 cho màn Kho bài giảng: 'Nút "Xuất Excel" (phụ — xuất theo bộ lọc hiện tại, tối đa 10.000 dòng theo BR-DATA-06)'. **Kèm cảnh báo**: nút này *chưa có* trong bản `.md` đặc tả ⇒ nếu phần mềm chưa có nút thì đó là **việc mới cho Dev**, không phải lỗi.
  → `.../reverify-week-2/phan-hoi-ba-confirmation-week2-vong2-va-tkdghqhtpl-r2.md:96,128`
- **Phương pháp đo mẫu (copy nguyên được):** `QLKCHTV_13` — 3 phép đo so sánh + đọc thân yêu cầu để loại trừ khả năng giao diện không truyền bộ lọc.
  → `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-4/cond/QLKCHTV_13.md`
- Tiền lệ ĐẠT: `.../reverify-week-2/reverify-audit/QLTNVV_06/observation.md:8` · `.../reverify-week-4/bug-reports/bug-report-UAT-tuan-4.md:424`

---

## 5. PDKHDTTH_04 — CB phê duyệt khác cấp với người lập bấm Phê duyệt kế hoạch đào tạo

**Đối tác phản ánh (row 360):**
> Tên chức năng ở phiếu: "Cán bộ phê duyệt khác cấp với người lập"
> "Hệ thống không hiển thị thông báo để người dùng dễ dàng nhận biết lý do không phê duyệt được kế hoạch"
> Bằng chứng: `PDKHDTTH_04.jpg`

### Tiền đề có sẵn (SAU khi recon seed)

Trước recon: **0 kế hoạch đào tạo ở trạng thái "Chờ duyệt"** ⇒ không có gì để bấm Phê duyệt. Recon đã seed 2 bản ghi:

| Mã kế hoạch | id | Người lập | Đơn vị người lập | Cấp | Trạng thái | version | Vai trò trong test |
|---|---|---|---|---|---|---|---|
| **`KH-20260803-0002`** ⭐ | `e63cdbc0-3cda-4e02-8e17-bc5961c3dfa3` | `cbnv_bn` | `00000000-0000-4000-8001-000000000001` | **Bộ ngành** | CHỜ DUYỆT | 2 | **Bản ghi KHÁC CẤP — dùng cho case** |
| `KH-20260803-0001` | `758eb2ec-8092-4065-9620-beb75dfaceb3` | `cbnv_tw` | `00000000-0000-4000-8000-000000000001` | Trung ương | CHỜ DUYỆT | 2 | Bản ghi CÙNG CẤP — baseline đối chứng |

### Ma trận phạm vi đã đo — quyết định cặp tài khoản × bản ghi

| Tài khoản phê duyệt | Cấp | Thấy bao nhiêu kế hoạch | Mở được `KH-20260803-0002` (cấp BN)? | Ghi chú |
|---|---|---|---|---|
| **`cbpd_tw_01`** (CB_PD_TW) | TW | **12** — gồm CẢ bản ghi cấp BN | ✅ **200** | ⇒ **Đây là cặp dùng được** |
| `cbpd_bn` (CB_PD_BN) | BN | **0** | — (thử mở kế hoạch cấp TW → **404**) | Không tới được nút |
| `cbnv_bn` (CB_NV_BN) | BN | 0 trước seed / 1 sau seed | — | Chỉ để lập kế hoạch |
| `cbnv_dp_01` (CB_NV_DP) | DP | **0** | — | Không có kế hoạch nào ở cấp ĐP |

> **Kết luận chọn cặp:** phải đi **từ trên xuống** — đăng nhập **`cbpd_tw_01`** (cấp Trung ương) rồi thao tác trên **`KH-20260803-0002`** (người lập ở cấp Bộ ngành). Chiều ngược lại (`cbpd_bn` duyệt kế hoạch của TW) **KHÔNG tới được nút**: danh sách rỗng, mở chi tiết trả `404 ERR-VAL-VII-02-01 "Bản ghi không tồn tại"`, gọi thẳng lệnh duyệt cũng `404` cùng mã.

### Dữ kiện quan trọng cho người verify — máy chủ chào hành động gì

So sánh phần `_links` mà máy chủ trả kèm khi **cùng một tài khoản `cbpd_tw_01`** mở chi tiết 2 kế hoạch:

| Mở kế hoạch | `_links` trả về |
|---|---|
| `KH-20260803-0001` — **cùng cấp** (TW) | `self` + **`approve`** + **`reject`** |
| `KH-20260803-0002` — **khác cấp** (BN) | **CHỈ `self`** — không có `approve`, không có `reject` |

⇒ Máy chủ **cố ý không chào** hành động duyệt/từ chối cho kế hoạch khác cấp. Câu hỏi mà người verify phải trả lời bằng quan sát UI thật:

1. Giao diện có còn hiện nút **[Phê duyệt]** trên bản ghi khác cấp không (giao diện có tôn trọng `_links` không)?
2. Nếu **có nút** → bấm vào thì có thông báo gì? (bắt bằng `tools/toast-capture.js`, ghi cả mã lỗi + số request kèm số thông báo)
3. Nếu **không có nút** → thì "không có thông báo lý do" chính là hiện tượng đối tác mô tả; lúc đó tranh chấp là *hệ thống có phải giải thích vì sao không duyệt được hay không* → tra SRS trước khi chọn giữa `Open` và `BA confirm`.

### Tiền đề THIẾU
Đã bù đủ. Nếu cần thêm kế hoạch ở trạng thái Chờ duyệt:
```bash
# tạo -> lấy id + version -> gửi duyệt
curl -sk -b $CJ -H 'Content-Type: application/json' -X POST https://18.143.165.120.nip.io/api/v1/ke-hoach-dao-taos \
  -d '{"tenKeHoach":"...","nam":2026,"thoiGianBatDau":"2026-09-01","thoiGianKetThuc":"2026-12-31"}'
curl -sk -b $CJ -H 'Content-Type: application/json' -X POST https://18.143.165.120.nip.io/api/v1/ke-hoach-dao-taos/<id>/submit \
  -d '{"version":<version>}'
```
Đăng nhập bằng tài khoản **cấp nào** thì kế hoạch thuộc **cấp đó** (đơn vị lấy từ người lập).

### Tài khoản nên dùng
- Người phê duyệt (khác cấp với người lập): **`cbpd_tw_01`** / `Test@1234` — CB Phê duyệt Trung ương #01, đơn vị `00000000-0000-4000-8000-000000000001`.
  ⚠️ **`cbpd_tw` đăng nhập FAIL** (`401 ERR-AUTH-LOGIN-01`) — đã ghi trong `input/input.md` từ 30/07, recon 03/08 xác nhận vẫn còn. Dùng `_01` theo Rule 7 (cùng vai trò + cùng cấp).
- Người lập (để dựng lại tiền đề nếu cần): `cbnv_bn` / `Test@1234` (cấp Bộ ngành).

### Lịch sử case anh em (tái dùng được — RẤT sát)
- **`KTHSYCHTPL_15`** — khung chuẩn cho đúng tình huống này: *"hành vi chặn ĐÚNG, nhưng thông báo sai vai trò + sai mẫu SRS + lặp 2 lần → **Open**"*. Nêu rõ 4 lỗi của câu thông báo: sai vai trò/hành động · dùng từ kỹ thuật "bản ghi" · không nói người dùng cần làm gì · hiển thị lặp 2 lần. Căn cứ `FR-V.I-06 §Processing` bước 1 (`srs-fr-05:533`, BR-AUTH-01).
  → `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/reverify-audit/KTHSYCHTPL_15/condition-table.md`
- Cùng gốc: `.../reverify-week-2/reverify-audit/LCNHTCVV_07/condition-table.md:55` ("đề nghị dev fix chung 1 lần cho toàn bộ thông báo chặn") · `.../reverify-week-2/reverify-audit/conditions/CNTTTVV_06.md:35` (sau fix thông báo thành *"Bạn không có quyền cập nhật hồ sơ tư vấn viên này (khác đơn vị)"*).
- Riêng luồng Đào tạo: `.../reverify-week-1/cond/TTCTDTTH_17-reverify-V103.md:60` — bấm [Gửi duyệt KQ] khóa `DDD-KH-012` bằng `cbnv_tw_03` bị chặn với thông báo *"Đơn vị của người phê duyệt khác đơn vị của khóa học"* ⇒ **chặn theo đơn vị là đúng nghiệp vụ, không phải lỗi**. Cũng xem `.../reverify-week-2/reverify-audit/EVIDENCE-AUDIT-2026-07-12.md:33`.

---

## 6. Ghi chú vận hành (áp cho cả 5 case)

### Tài khoản — trạng thái đăng nhập đã kiểm 03/08

| Tài khoản | Kết quả | Ghi chú |
|---|---|---|
| `cbnv_tw` | ✅ OK | CB_NV_TW · TW · `8000-…0001` |
| `cbnv_bn` | ✅ OK | CB_NV_BN · BN · `8001-…0001` |
| `cbnv_dp` | ❌ **FAIL 401** `ERR-AUTH-LOGIN-01` | **Phát hiện mới 03/08** — chưa ghi trong `input/input.md` |
| `cbnv_dp_01` | ✅ OK | CB_NV_DP · DP · `8002-…0006` (An Giang) — dùng thay `cbnv_dp` |
| `cbpd_bn` | ✅ OK | CB_PD_BN · BN · `8001-…0001` |
| `cbpd_tw` | ❌ FAIL 401 | Đã biết từ 30/07 |
| `cbpd_tw_01` | ✅ OK | CB_PD_TW · TW · `8000-…0001` |
| `nht_qa_01` | ✅ OK | NHT · DP · `8002-…0006` |
| `0109998887` | ✅ OK | DN · `8002-…0001` — hộp thư OTP `qa.uat.dn.verify@test.htpldn.vn` |

> **Đề nghị bổ sung vào `input/input.md`:** `cbnv_dp` login FAIL → dùng `cbnv_dp_01`.

### Cách đăng nhập bằng lệnh (dùng lại được)

Đăng nhập **2 bước** (có OTP), JWT nằm trong cookie:

```bash
B=https://18.143.165.120.nip.io
CJ=/tmp/cj_<user>.txt

# B1 — lấy otpToken
curl -sk -c $CJ -H 'Content-Type: application/json' -X POST "$B/api/v1/auth/login" \
  -d '{"username":"cbnv_tw","password":"Test@1234"}'
# → {"success":true,"data":{"otpToken":"…","otpExpiresIn":300,"maskedEmail":"cbn***@htpldn.test"}}

# B2 — lấy mã OTP ở MailHog rồi xác thực
curl -s "http://18.143.165.120:8025/api/v2/messages?limit=20"     # tìm đúng hộp thư theo maskedEmail
curl -sk -b $CJ -c $CJ -H 'Content-Type: application/json' -X POST "$B/api/v1/auth/verify-otp" \
  -d '{"otpToken":"<otpToken>","otpCode":"<6 số>"}'

curl -sk -b $CJ "$B/api/v1/auth/me"    # kiểm tra vai trò + cấp + đơn vị
```

Script tiện dụng recon đã dùng: `/tmp/qa_login2.sh <username> <password> <cookiefile> [tenHopThu]`.
⚠️ Giới hạn tần suất đăng nhập **5 lần/60 giây** (`ERR-SYS-00-29-01`) — đừng đăng nhập dồn.

### Endpoint hữu ích

| Mục đích | Lệnh |
|---|---|
| Danh sách khóa học | `GET /api/v1/khoa-hocs?page=1&pageSize=100` (kèm `meta.tabCounts`) |
| Điểm danh của khóa | `GET /api/v1/khoa-hocs/{id}/diem-danhs` (lọc `ngayDiemDanh`, `lichHocId`) |
| Kết quả của khóa | `GET /api/v1/khoa-hocs/{id}/ket-quas` |
| Buổi học | `GET /api/v1/khoa-hocs/{id}/lich-hocs` |
| Kho bài giảng | `GET /api/v1/bai-giangs?loaiTaiLieu=SLIDE\|PDF\|VIDEO` |
| URL xem trước bài giảng | `GET /api/v1/bai-giangs/{id}/preview-url` |
| Kế hoạch đào tạo | `GET /api/v1/ke-hoach-dao-taos?trangThai=&nam=&keyword=` |
| Xuất Excel kế hoạch | `POST /api/v1/ke-hoach-dao-taos/export` (body = bộ lọc) |
| Xuất Excel bài giảng | `POST /api/v1/bai-giangs/export` (body = bộ lọc) |
| Đề xuất đào tạo | `GET` / `POST /api/v1/de-xuat-dao-taos` |
| Lĩnh vực pháp lý | `GET /api/v1/danh-muc?loaiDanhMuc=LINH_VUC_PL&trangThai=KICH_HOAT` |
| Danh mục toàn bộ đặc tả API | `GET /api/docs-json` (đọc được, không cần đăng nhập — 538 đường dẫn) |

### Đường dẫn / tham số SAI đã thử — để người sau khỏi mất công

| Đã thử | Kết quả | Đúng phải là |
|---|---|---|
| `GET /api/v1/danh-mucs?loai=LINH_VUC` | **404** `ERR-SYS-00-04-01` | `/api/v1/danh-muc` (số ít) |
| `GET /api/v1/danh-muc?loai=…` | **422** `ERR-VAL-SYS-00-01` | tham số tên là **`loaiDanhMuc`** |
| `?loaiDanhMuc=LINH_VUC` | **422** "loaiDanhMuc không hợp lệ" | giá trị đúng là **`LINH_VUC_PL`** |
| `POST /api/v1/bai-giangs/upload-file` với field `files` / `tep` | **400** "Unexpected field" | field bắt buộc tên **`file`** |
| `HEAD` lên URL xem trước đã ký | **403** | dùng **`GET`** (chữ ký chỉ cấp cho GET) |
| `GET /api/v1/khoa-hocs/{id}/lich-hocs` với khóa khác đơn vị | **`ERR-AUTH-VPD-00-03`** "Đơn vị của bạn khác đơn vị của khóa học" | đây là **chặn phạm vi đơn vị đúng nghiệp vụ**, không phải lỗi |
| `GET` / `POST approve` kế hoạch của đơn vị khác (từ cấp dưới lên) | **404** `ERR-VAL-VII-02-01` "Bản ghi không tồn tại" | — (xem §5) |

### Dữ liệu recon đã tạo trên env (khai báo minh bạch)

| Thực thể | Mã / id | Ai tạo | Vì sao |
|---|---|---|---|
| Kế hoạch đào tạo | `KH-20260803-0001` / `758eb2ec-8092-4065-9620-beb75dfaceb3` | `cbnv_tw` | baseline cùng cấp cho PDKHDTTH_04 |
| Kế hoạch đào tạo | `KH-20260803-0002` / `e63cdbc0-3cda-4e02-8e17-bc5961c3dfa3` | `cbnv_bn` | bản ghi khác cấp cho PDKHDTTH_04 |
| Tệp tải lên | `49871f89-8b54-4a88-8ac2-b990691aae65` (`qa-recon-slide-QLKTLBG_09.pptx`) | `cbnv_tw` | tệp Slide cho QLKTLBG_09 |
| Bài giảng | `53b83ff6-c381-44e9-b4be-a6e7d2610313` | `cbnv_tw` | bản ghi loại Slide cho QLKTLBG_09 |

Không xóa, không sửa, không phê duyệt bất kỳ bản ghi có sẵn nào. **Chưa bấm Phê duyệt** trên 2 kế hoạch trên — để nguyên trạng thái Chờ duyệt cho người verify.
