# Bug Report — Tư vấn chuyên sâu / Mạng lưới Tư vấn viên (lô B7 · verify bug dev đã fix)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | Phần mềm Hỗ trợ pháp lý doanh nghiệp (PM HTPLDN) |
| **Môi trường** | https://18.143.165.120.nip.io — **env nội bộ**, KHÔNG phải env nghiệm thu của đối tác (`htpldn-uat.ospgroup.vn`) |
| **Bản dựng** | **R3 2026-08-07 (mới nhất):** `HTPLDN · V1.0.10` · bó mã FE `assets/index-B2W2Krcs.js` · `GET /` `last-modified: Thu, 06 Aug 2026 17:39:54 GMT` (00:39:54 giờ VN 07/08) · `etag W/"6a74c6ea-428"`. ⚠️ Env deploy liên tục: `V1.0.8` (06/08 14:13 VN) → `V1.0.9` (06/08 19:48 VN) → `V1.0.10` (07/08 00:39 VN). Mỗi kết quả re-test chỉ có hiệu lực cho bản dựng ghi tại dòng `Re-test` của chính bug đó |
| **Người test** | QA (Chrome DevTools MCP) |
| **Ngày** | 2026-08-07 01:03:00 |
| **Loại test** | Verify bug dev đã fix (flow `flows/04-verify-bug-dev-fix-khong-ho-so.md`) |
| **Round** | Lô B7 — vòng verify 2026-08-06 |
| **Tài liệu tham chiếu** | [tieuchi/QLTLPLCVV_17.md](tieuchi/QLTLPLCVV_17.md) · [ketqua-QLTLPLCVV_17.txt](ketqua-QLTLPLCVV_17.txt) · [tieuchi/QLKCHTV_37.md](tieuchi/QLKCHTV_37.md) · [ketqua-QLKCHTV_37.txt](ketqua-QLKCHTV_37.txt) · [tieuchi/QLTVV_02.md](tieuchi/QLTVV_02.md) · [ketqua-QLTVV_02.txt](ketqua-QLTVV_02.txt) · [tieuchi/CNHSNLTVV_03.md](tieuchi/CNHSNLTVV_03.md) · [ketqua-CNHSNLTVV_03.txt](ketqua-CNHSNLTVV_03.txt) · [tieuchi/CNDSMLTVV_01.md](tieuchi/CNDSMLTVV_01.md) · [ketqua-CNDSMLTVV_01.txt](ketqua-CNDSMLTVV_01.txt) · [cau-hoi-BA.md](cau-hoi-BA.md) · SRS `srs-v3.5/srs-fr-12-tv-chuyen-sau.md` · `srs-v3.5/srs-fr-13-tv-nhanh.md` · `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` · `srs-v3.5.md` Phụ lục E §H6, §H8 |

---

## Tổng hợp

> **R3 2026-08-07 — env nội bộ, bản dựng `HTPLDN · V1.0.10` / bó mã `assets/index-B2W2Krcs.js` / `GET /`
> last-modified `Thu, 06 Aug 2026 17:39:54 GMT` (00:39 giờ VN 07/08).** `BUG-TVV-CNDSMLTVV-01` đo lại →
> **vẫn Reopen nhưng triệu chứng ĐÃ ĐỔI**: lô không còn bị kéo đổ (hồ sơ hợp lệ trong lô lẫn đã công khai
> được) và lý do từ chối của máy chủ đã là câu nghiệp vụ đọc được; còn lại là giao diện vẫn báo thành công
> khi có hồ sơ bị từ chối. `BUG-TVV-CNHSNLTVV-03` **đã đóng** ở lượt R4+R5 cùng ngày trên bó mã `assets/index-D4Buvu4S.js` (đủ 6/6 lượt [Lưu], bảng GAP trống). **Breakdown 5 bug: 3 Closed · 1 Chờ BA · 1 Reopen.**

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 5    | 0        | 4     | 0      | 1       | 0       | 3      | 2    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-TVCS-QLTLPLCVV-17~~ | Major | P1 | UI/UX | QLTLPLCVV_17 (tab `bug` dòng 300) | `FR-X.1-06 §Mô tả` (`srs-fr-12-tv-chuyen-sau.md:818`) · `§Inputs — File tư liệu` (:843) · `§Postconditions` (:958) · `§AC` (:981, :979) · `SCR-X1-02 thành phần 6` (:1158) | Nút mở tệp đính kèm trong nhóm "Tư liệu pháp lý liên kết" bị vô hiệu hoá, người dùng không xem/tải được tệp | **Closed** |
| ~~BUG-TVN-QLKCHTV-37~~ | Major | P1 | UI/UX | QLKCHTV_37 (tab `bug` dòng 305) | `SCR-X2-03 thành phần 10` (`srs-fr-13-tv-nhanh.md:582`) · `TU_VAN_NHANH.ma_phien` (:727) · `FR-X.2-05 §Inputs` (:392) · `DANH_GIA_TV` (:743) · Phụ lục E §H8 (`srs-v3.5.md:6716`) | Khối "Đánh giá" của phiên tư vấn nhanh không có nút xuất tệp Excel, người dùng không kết xuất được dữ liệu đánh giá | **Closed** |
| BUG-TVV-QLTVV-02-R3 | Minor | P3 | UI/UX | QLTVV_02 (tab `bug` dòng 32) | `SCR-IV-01 thành phần 24-29` (`srs-fr-04-chuyen-gia-tvv.md:1452`-`:1457`) · `BR-CALC-06` (:2538) · `FR-IV-02 §Processing` (:247) · `BR-DATA-07` (`srs-fr-05-vu-viec.md:2394`) · Phụ lục E §H6 (`srs-v3.5.md:6714`) · §C, §F (`srs-fr-05-vu-viec.md:1568`, :1601) — **đặc tả IM LẶNG về thứ tự sắp xếp mặc định của SCR-IV-01** | Danh sách Tư vấn viên / Chuyên gia không sắp xếp theo ngày công nhận mới nhất trước (đang sắp theo ngày tạo) — đặc tả không quy định thứ tự, cần BA chốt | **Chờ BA** |
| BUG-TVV-CNHSNLTVV-03 | Major | P1 | Happy | CNHSNLTVV_03 (tab `bug` dòng 36) | `FR-IV-04 §Mô tả` (`srs-fr-04-chuyen-gia-tvv.md:373`) · `§Preconditions` (:377) · `§AC1` (:432) · `§AC2` (:433) · `§Inputs — chung_chi_moi` (:388) · `§Processing bước 4-5` (:402-:403) · `§Postconditions` (:418) · `§Error Handling E1-E5` (:425-:429) · `SCR-IV-03 thành phần 21` (:1576) | Cập nhật năng lực có đính tệp chứng chỉ: tệp đính kèm không hiện đúng tên, và hồ sơ đã có tệp chứng chỉ thì không mở lại được form cập nhật năng lực | **Closed** |
| BUG-TVV-CNDSMLTVV-01 | Major | P1 | Happy | CNDSMLTVV_01 (tab `bug` dòng 37) | `FR-IV-08 §Processing bước 2` (`srs-fr-04-chuyen-gia-tvv.md:664`) · `§Processing bước 4` (:666) · `§Postconditions` (:685) · `§AC1` (:689) · `§Error Handling E1-E2` (:681, :682) · `SCR-IV-01 §Quy tắc tương tác` (:1464) · `MD-CONG-KHAI` (:1406) · `SCR-IV-02 Số thẻ hành nghề` (:1507) · `SCR-IV-03 nhóm (f)` (:1564) · `BR-PUBLIC-01` / `BR-PUBLIC-03` (`srs-v3.5.md:5729`, :5741) · mẫu thông báo công khai (`srs-v3.5.md:6772`) | Công khai hàng loạt tư vấn viên: hồ sơ bị máy chủ từ chối vẫn báo "Đã công khai … thành công", người dùng không biết hồ sơ nào không đạt và vì sao | **Reopen** |

---

## ~~BUG-TVCS-QLTLPLCVV-17~~ [CLOSED] — Nút mở tệp đính kèm trong nhóm "Tư liệu pháp lý liên kết" bị vô hiệu hoá, không xem/tải được tệp

> **Re-test:** 2026-08-06 14:37:00 — ✅ PASS (Closed-verified). Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng `HTPLDN · V1.0.8` / bó mã `assets/index-DIABnbIr.js` / `GET /` last-modified 06/08/2026 14:13:15 giờ VN · **N = 1 tư liệu × 2 trạng thái** (`Nháp` · `Đã công khai`) = 6 lượt bấm thật · **M = 3/3 dạng** (`.pdf` · `.png` · `.docx`) · **dữ liệu seed:** QA tự tạo mới `TVCS-20260806-0003` (`eb16294e-…`) trên doanh nghiệp `DN-HNI-0001` + 1 tư liệu `14cef4af-…` đính 3 tệp thật, **không đụng dữ liệu sẵn có**. Đo bằng `cbnv_tw_02` (CB_NV_TW, cấp TW — trùng khít vai trò đối tác). **Pass chỉ có hiệu lực cho env + bản dựng nêu trên.**

### Mô tả

Đối tác phản ánh trên màn chi tiết Tư vấn chuyên sâu → nhóm "Tư liệu pháp lý liên kết": mở hộp thoại
xem tư liệu rồi bấm nút mở tệp cạnh tên tệp đính kèm (`Báo cáo mẫu.docx`) thì **nút bị vô hiệu hoá**
(chữ xám, bấm không được), nên không mở được trình xem trực tuyến mà cũng không tải được tệp về máy.

Đo lại bằng thao tác thật trên bản dựng ghi ở đầu file: **không còn tái hiện**. Nút mở tệp thao tác
được ở cả 3 định dạng và cả 2 trạng thái tư liệu; định dạng xem trực tuyến được thì hiện đúng nội dung
tệp, định dạng còn lại thì chuyển tệp về máy đúng nguyên bản.

### Các bước tái hiện

1. Đăng nhập `cbnv_tw_02` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), cấp **TW**, đơn vị
   `00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - Bộ Tư pháp). Theo `srs-fr-12-tv-chuyen-sau.md:820`
   vai trò này có **CRUD đầy đủ** trên tư liệu pháp lý trong phạm vi đơn vị (BR-AUTH-08). Tải lại trang
   để chắc chắn đang chạy bản dựng mới, đọc dấu vân tay bản dựng.
2. Tư vấn → Tư vấn chuyên sâu → **[Thêm mới]** → tạo `TVCS-20260806-0003` (DN `DN-HNI-0001`, lĩnh vực
   Thương mại) — bản ghi QA tự dựng, không đụng dữ liệu sẵn có.
3. Mở nhóm **"Tư liệu pháp lý liên kết"** → **[Thêm tư liệu]** → Loại **Tài liệu**, Lĩnh vực
   **Sở hữu trí tuệ** (giống hệt tư liệu trong ảnh của đối tác) → đính **3 tệp thật**:
   `.pdf` 629 B · `.png` 45.802 B · **`.docx` 964 B** (đúng định dạng tệp đối tác dùng) → **[Thêm mới]**.
4. Ở hàng tư liệu (trạng thái **Nháp**) bấm **[Xem tệp]** → hộp thoại **"Xem tư liệu pháp luật"** mở ra
   (chỉ có nút [Đóng] — cùng hộp thoại trong ảnh đối tác).
5. Bấm **[Xem]** cạnh từng tên tệp — lần lượt `.pdf`, `.png`, `.docx`. Quan sát tệp có mở/tải được không.
6. Bấm **[Công khai]** trên hàng → nhập mô tả công khai → xác nhận. Hàng chuyển **Đã công khai** với bộ
   hành động `Xem tệp / Hủy công khai / Xóa` — **trùng khít hàng trong ảnh đối tác**.
7. Lặp lại bước 4-5 ở trạng thái **Đã công khai**. Trước lượt này **xoá tệp `.docx` đã tải về ở bước 5**
   để chắc chắn tệp nhận được là của chính lượt bấm này.
8. Đối chứng bằng đường thứ hai: gọi thẳng `GET /api/v1/tu-lieu-phap-ly-vvs/{id}/files/{fileId}/download`
   trong cùng phiên, tải liên kết trả về rồi đếm byte + đọc chữ ký đầu tệp.

### Kết quả mong đợi

- Theo `srs-fr-12-tv-chuyen-sau.md:818` và `:958`, chức năng quản lý tư liệu pháp lý của vụ việc
  **hỗ trợ xem trước (preview) tệp đính kèm** — đây là một trong các hành vi bắt buộc của FR-X.1-06.
- Theo `srs-fr-12-tv-chuyen-sau.md:981`, khi cán bộ nghiệp vụ chọn một tệp để xem trực tuyến thì hệ thống
  phải hiển thị nội dung tệp đó, không được để người dùng mắc kẹt ở một điều khiển bấm không được.
- Theo `srs-fr-12-tv-chuyen-sau.md:843`, tệp đính kèm hợp lệ gồm **PDF / DOCX / XLS / hình ảnh** — nên
  hành vi trên phải đúng cho mọi định dạng đã nhận vào, không riêng một định dạng.
- Theo `srs-fr-12-tv-chuyen-sau.md:902`, tư liệu ở trạng thái công khai chỉ bị chặn **sửa**; việc đọc/xem
  tệp không bị chặn theo trạng thái này.
- FR-X.1-06 **không quy định** hệ thống phải làm gì với định dạng không xem trực tuyến được (quy định
  "không hỗ trợ preview thì chuyển sang tải về" chỉ có ở `srs-fr-09-bieu-mau.md:338`, thuộc nhóm Biểu mẫu).
  Vế này của đối tác vì vậy chỉ được **ghi nhận hiện trạng**, không dùng để chấm Fail.

### Kết quả thực tế

- **Không còn vô hiệu hoá.** 6/6 lượt (3 định dạng × 2 trạng thái tư liệu) nút mở tệp đo được:
  `disabled = false` · `aria-disabled = null` · `pointer-events: auto` · `opacity: 1` ·
  màu chữ `rgb(9, 88, 217)` (xanh, không phải xám) · `cursor: pointer` · kích thước 68×24 px.
  Nút `[Xem]` trong hộp thoại "Thêm tư liệu" cũng bật (3/3).
- **`.pdf`** → mở tab trình xem trực tuyến (liên kết ký sẵn), **render đọc được** đúng câu đã nạp vào tệp:
  *"QA UAT B7 QLTLPLCVV_17 - PDF xem truc tuyen 2026-08-06"*, 1/1 trang.
- **`.png`** → mở khung xem ảnh (có thanh xoay/phóng), ảnh render đúng, `naturalWidth × naturalHeight`
  = **240 × 90** khớp kích thước thật của tệp đã tải lên, `complete = true`.
- **`.docx`** → **chuyển tệp về máy**. Tệp nhận được: đúng tên `B7-QLTLPLCVV17-baocao.docx`, **964 byte**,
  **md5 `a397f16763a5e49b88637f87fc779697` trùng khít tệp gốc**; mở gói đọc `word/document.xml` ra đúng câu
  *"QA UAT B7 QLTLPLCVV_17 - DOCX khong xem truc tuyen 2026-08-06"*. ⇒ đúng hành vi đối tác mong đợi cho
  nhánh định dạng không xem trực tuyến được.
- **Đối chứng qua API** (đường đo thứ hai): `GET .../files/{fileId}/download` → **200** cho cả 3 tệp;
  tải liên kết trả về được **629 B `%PDF`** · **45.802 B `\x89PNG`** · **964 B `PK\x03\x04`** — khớp
  từng byte với tệp gốc và khớp `Content-Type` tương ứng. **Hai đường đo không mâu thuẫn.**
- Bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`): thao tác seed
  **1 request / 1 thông báo** *"Đã thêm tư liệu pháp luật"*; thao tác công khai **1 request / 1 thông báo**
  *"Đã công khai tư liệu"* — không lặp, không double-toast. Thao tác bấm `[Xem]` không sinh thông báo
  (đặc tả không đòi thông báo cho thao tác này).

### Bằng chứng

**1. Ảnh chụp:**

![Nhóm "Tư liệu pháp lý liên kết" trước khi seed — trạng thái trống hợp lệ "Chưa có tư liệu pháp luật đính kèm."](image/QLTLPLCVV_17-01-nhom3-truoc-khi-seed.png)

![Hộp thoại "Thêm tư liệu pháp luật" đã điền Loại = Tài liệu, Lĩnh vực = Sở hữu trí tuệ và đính đủ 3 tệp thật .pdf/.png/.docx](image/QLTLPLCVV_17-02-hopthoai-them-tulieu-3tep.png)

![Bảng tư liệu sau khi seed — 1 hàng, cột File = 3, Trạng thái = Nháp, hành động Xem tệp / Sửa / Công khai / Xóa](image/QLTLPLCVV_17-03-bang-tulieu-trang-thai-Nhap.png)

![Hộp thoại "Xem tư liệu pháp luật" ở trạng thái Nháp — 3 nút [Xem] cạnh 3 tên tệp đều màu xanh, bấm được](image/QLTLPLCVV_17-04-hopthoai-xem-tulieu-Nhap-3nut-Xem-xanh.png)

![Bấm [Xem] tệp .pdf — trình xem trực tuyến mở ra và render đọc được chữ "QA UAT B7 QLTLPLCVV_17 - PDF xem truc tuyen 2026-08-06"](image/QLTLPLCVV_17-05-pdf-render-trinh-xem-truc-tuyen.png)

![Bấm [Xem] tệp .png — khung xem ảnh mở ra với thanh xoay/phóng, ảnh render đúng nội dung tệp đã tải lên](image/QLTLPLCVV_17-06-png-preview-khung-xem-anh.png)

![Trạng thái Đã công khai — cùng hộp thoại, cùng vị trí như ảnh đối tác, nhưng 3 nút [Xem] vẫn XANH chứ không xám](image/QLTLPLCVV_17-07-tulieu-DaCongKhai-3nut-Xem-van-dung-duoc.png)

![Hàng tư liệu ở trạng thái "Đã công khai" với bộ hành động Xem tệp / Hủy công khai / Xóa — trùng khít hàng phía sau hộp thoại trong ảnh của đối tác](image/QLTLPLCVV_17-08-hang-tulieu-DaCongKhai-trung-khit-anh-doi-tac.png)

**2. Tệp thật nhận được khi bấm [Xem] trên `.docx`** (nhánh không xem trực tuyến được):
[`evidence/QLTLPLCVV_17-tep-tai-ve-tu-nut-Xem.docx`](evidence/QLTLPLCVV_17-tep-tai-ve-tu-nut-Xem.docx) —
964 byte, md5 `a397f16763a5e49b88637f87fc779697`, trùng khít tệp gốc trong
[`seed-files/B7-QLTLPLCVV17-baocao.docx`](seed-files/B7-QLTLPLCVV17-baocao.docx).

**3. Số đo đầy đủ (chỉ số vô hiệu hoá từng lượt, đối chứng API, số byte/chữ ký):**
[`ketqua-QLTLPLCVV_17.txt`](ketqua-QLTLPLCVV_17.txt) · tiêu chí chấm + bảng đóng GAP:
[`tieuchi/QLTLPLCVV_17.md`](tieuchi/QLTLPLCVV_17.md).

**4. Phản hồi máy chủ (đường đo thứ hai):**

```
GET /api/v1/tu-lieu-phap-ly-vvs/14cef4af-cb15-497b-88d6-8ed3ad22d9e7/files/{fileId}/download → 200
  b5869488… B7-QLTLPLCVV17-tailieu.pdf   → application/pdf                                   629 B  %PDF
  4d09bd8d… B7-QLTLPLCVV17-anh.png       → image/png                                      45.802 B  \x89PNG
  62ecee9e… B7-QLTLPLCVV17-baocao.docx   → application/vnd.openxmlformats-…wordprocessingml   964 B  PK\x03\x04
```

---

## ~~BUG-TVN-QLKCHTV-37~~ [CLOSED] — Khối "Đánh giá" của phiên tư vấn nhanh không có nút xuất tệp Excel, không kết xuất được dữ liệu đánh giá

> **Re-test:** 2026-08-06 15:15:00 — ✅ PASS (Closed-verified). Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng `HTPLDN · V1.0.8` / bó mã `assets/index-DIABnbIr.js` / `GET /` last-modified 06/08/2026 14:13:15 giờ VN · **N = 3 phiên-đánh giá × 1 lượt bấm = 3 lượt bấm thật** + 3 lượt đối chứng máy chủ + 2 lượt kiểm nhánh ngược · **M = 2/2 dạng** (đánh giá **có** nhận xét · đánh giá **không** nhận xét), phủ thêm **2/2 giá trị kênh** (`TV_NHANH` · `TV_THU_CONG`) · **dữ liệu seed:** QA tự dựng mới `TVN-20260806-0001` / `-0002` / `-0003` trên doanh nghiệp `DN-HNI-0001`, **không dùng lại `TVN-20260727-0002` của lượt đo cũ, không đụng dữ liệu sẵn có**. Đo bằng `cbnv_tw_02` (CB_NV_TW, cấp TW — trùng khít vai trò + cấp của đối tác). **Pass chỉ có hiệu lực cho env + bản dựng nêu trên.**

### Mô tả

Đối tác phản ánh trên màn chi tiết phiên tư vấn nhanh (phiên đã **Hoàn thành** và **đã có đánh giá của
doanh nghiệp**): khối **"Đánh giá"** **không có nút chức năng nào để xuất tệp Excel**, nên không kết xuất
được dữ liệu đánh giá của phiên. TKM kiểm lại ngày 03/08 vẫn ghi *"Màn hình chưa có nút chức năng"*.

Đo lại bằng thao tác thật trên bản dựng ghi ở đầu file: **không còn tái hiện**. Khối "Đánh giá" có nút
xuất tệp, bấm ra tệp bảng tính thật, mở tệp đọc thấy đủ 6 trường đặc tả đòi và dữ liệu khớp màn hình.

### Các bước tái hiện

1. Đăng nhập `cbnv_tw_02` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), cấp **TW**, đơn vị
   `00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - Bộ Tư pháp). Đây đúng vai trò + cấp đọc
   được trên ảnh của đối tác. Theo `srs-fr-13-tv-nhanh.md:177` tác nhân của luồng tư vấn nhanh là Cán bộ
   Nghiệp vụ; tài khoản có `read_tu_van_nhanh` + `manage_tu_van_nhanh`. Tải lại trang để chắc chắn đang
   chạy bản dựng mới, đọc dấu vân tay bản dựng.
2. Tư vấn → Tư vấn nhanh → **[Thêm mới]** → tạo 3 phiên mới gắn doanh nghiệp `DN-HNI-0001`
   (`TVN-20260806-0001`, `-0002`, `-0003`) — bản ghi QA tự dựng, không đụng dữ liệu sẵn có.
3. Mỗi phiên: soạn nội dung rồi bấm **[Gửi trả lời]** → phiên chuyển **"Cán bộ trả lời"**.
4. Đưa mỗi phiên lên **"Hoàn thành"** bằng cách tạo **đánh giá của doanh nghiệp**: theo
   `srs-fr-13-tv-nhanh.md:371` doanh nghiệp chấm điểm trên chuyên trang của Cổng PLQG, Cổng gửi vào CMS
   qua dịch vụ tích hợp — trong phần mềm này **vai trò DN không có bất kỳ lối vào nào** (đã kiểm bằng tài
   khoản DN thật `0109998887`: không có menu Tư vấn nhanh, `/api/v1/tu-van-nhanhs` trả **403**), còn đường
   tích hợp đòi chứng thư mà môi trường không cấp. Đường duy nhất phần mềm cung cấp là dịch vụ proxy phía
   CMS — dùng đúng đường đó để dựng tiền đề, với 3 biến thể: **4 sao + có nhận xét** · **5 sao + KHÔNG
   nhận xét** · **3 sao + có nhận xét**.
5. Đổi kênh `TVN-20260806-0003` sang **"Thủ công"** để có biến thể kênh trùng khít ảnh của đối tác.
6. Mở **tab "Hoàn thành"** của màn danh sách → liệt kê toàn bộ nút, tìm nút xuất tệp.
7. Mở **màn chi tiết** từng phiên → đo nút xuất tệp trong khối "Đánh giá" (có mặt chưa · có bị vô hiệu hoá
   không · kích thước).
8. Bấm **thật** nút xuất tệp ở cả 3 phiên → lấy đúng tệp của chính lượt bấm đó → **mở tệp ra đọc** tên
   sheet, tiêu đề cột, từng ô dữ liệu.
9. Kiểm **nhánh ngược**: mở `TVN-20260729-0002` (trạng thái "Cán bộ trả lời", chưa có đánh giá) và
   `TVN-20260727-0004` (đã "Hoàn thành" nhưng KHÔNG có đánh giá) — quan sát nút xuất tệp có hiện không.
10. Đối chứng bằng đường thứ hai: gọi thẳng dịch vụ xuất tệp `GET /api/v1/tu-van-nhanhs/{id}/danh-gia/export`
    và đọc lại bản ghi đánh giá `GET /api/v1/tu-van-nhanhs/{id}` trong cùng phiên, so từng trường với tệp.

### Kết quả mong đợi

- Theo `srs-fr-13-tv-nhanh.md:582` (SCR-X2-03 thành phần 10), khối "Đánh giá" phải cho người dùng **kết xuất
  dữ liệu đánh giá của phiên ra tệp Excel**; điều khiển đó **hiển thị trong tab "Hoàn thành" hoặc ở màn chi
  tiết phiên** — một trong hai vị trí là đủ.
- Cũng theo `:582`, điều khiển này **chỉ hiện khi phiên ở trạng thái Hoàn thành và đã có ít nhất 1 đánh giá**,
  để không rơi vào trường hợp xuất tệp rỗng.
- Tệp kết xuất phải chứa đủ **6 trường**: mã phiên · điểm đánh giá · nhận xét của doanh nghiệp · ngày đánh giá ·
  tên doanh nghiệp · mã doanh nghiệp (`:582`), và dữ liệu phải khớp đánh giá đang hiển thị trên màn.
- Tên tệp theo khuôn `DanhGiaTvNhanh_{ma_phien}_{YYYYMMDD_HHmm}.xlsx` (`:582`), áp quy ước tên tệp kết xuất
  tại **Phụ lục E §H8** (`srs-v3.5.md:6716`) — phần tên viết liền không dấu, `{DinhDanh}` lấy từ `ma_phien`
  (`:727`) và bỏ mọi ký tự không phải chữ/số, bắt buộc có phần giờ-phút để hai lần xuất trong cùng ngày không
  đè nhau. `[BA chốt 2026-08-06]`
- Nhận xét là trường **không bắt buộc** (`:392`, `:743`), nên đánh giá không có nhận xét vẫn phải xuất được và
  ô tương ứng trong tệp phải để trống thay vì sinh giá trị kỹ thuật.

### Kết quả thực tế

- **Nút xuất tệp có mặt và thao tác được** ở **màn chi tiết phiên**, 3/3 phiên: toàn bộ nút trong vùng nội
  dung = `["Quay lại danh sách", "Xuất Excel"]`; đo trên nút: `disabled = false` · `aria-disabled = null` ·
  `pointer-events: auto` · `opacity: 1` · `cursor: pointer` · kích thước 127×32 px.
  Ở **tab "Hoàn thành"** của danh sách không có nút — hợp lệ vì `:582` cho phép "một trong hai vị trí".
- **Bấm thật 3/3 lượt đều ra tệp**: mỗi lượt đúng **1 lời gọi** `GET …/danh-gia/export`, tệp nhận được
  **7008 / 6940 / 7000 byte**, chữ ký `PK\x03\x04`, kiểu nội dung `…spreadsheetml.sheet`. **Ba mã băm md5
  khác nhau** ⇒ ba tệp thật khác nhau, không phải một tệp lấy lại từ bộ nhớ đệm.
- **Mở tệp ra đọc** (openpyxl) — cả 3 tệp: 1 sheet *"Đánh giá TV nhanh"*, vùng A1:F4. Dòng 1 tiêu đề
  *"ĐÁNH GIÁ PHIÊN TƯ VẤN NHANH"*; dòng 3 là **đủ 6/6 tiêu đề cột** đặc tả đòi:
  `Mã phiên | Điểm đánh giá | Nhận xét của doanh nghiệp | Ngày đánh giá | Tên doanh nghiệp | Mã doanh nghiệp`.
  Dòng 4 dữ liệu **khớp từng ô** với khối "Đánh giá" trên màn của chính phiên đó:

  | Phiên | Điểm | Nhận xét trong tệp | Ngày | Tên DN | Mã DN |
  |---|---|---|---|---|---|
  | `TVN-20260806-0001` | `4` (màn: 4 sao, TB 4.0/5) | *"Cán bộ trả lời rõ ràng, đúng trọng tâm câu hỏi của doanh nghiệp. Rất hài lòng."* | `06/08/2026` | `Cong ty TNHH QA UAT Kiem Thu` | `0109998887` |
  | `TVN-20260806-0002` | `5` (màn: 5 sao, TB 5.0/5) | **chuỗi rỗng** (màn hiện `—`) | `06/08/2026` | ↑ | ↑ |
  | `TVN-20260806-0003` | `3` (màn: 3 sao, TB 3.0/5) | *"Nội dung tư vấn tạm ổn nhưng doanh nghiệp mong được trả lời sớm hơn."* | `06/08/2026` | ↑ | ↑ |

  Dạng "không có nhận xét" cho ra **chuỗi rỗng**, không phải chữ `null` / `undefined`, dù máy chủ lưu
  `nhanXet = null`. Tiếng Việt có dấu đọc ra nguyên vẹn, không lỗi mã hoá.
- **Tên tệp đúng khuôn `:582` + §H8** ở cả 3 lượt:
  `DanhGiaTvNhanh_TVN202608060001_20260806_1504.xlsx` · `DanhGiaTvNhanh_TVN202608060002_20260806_1506.xlsx` ·
  `DanhGiaTvNhanh_TVN202608060003_20260806_1510.xlsx`. Phần `{DinhDanh}` đã bỏ dấu gạch nối của `ma_phien`
  đúng quy tắc ký tự §H8 (`TVN-20260806-0001` → `TVN202608060001`); phần giờ-phút bám đúng thời điểm bấm;
  tổng dài 49/255 ký tự.
- **3 thẻ tổng hợp** mà `:582` cũng đòi đều có và số khớp dữ liệu thật: *Tổng đánh giá 1 lượt* ·
  *Điểm trung bình 4.0 / 5.0 / 3.0 trên 5* · *Phân bố điểm 4★×1 / 5★×1 / 3★×1*.
- **Nhánh ngược đúng đặc tả:** `TVN-20260729-0002` (chưa đánh giá) và `TVN-20260727-0004` (đã Hoàn thành
  nhưng không có đánh giá) đều chỉ có nút `["Quay lại danh sách"]`, **không** có khối "Đánh giá" và
  **không** có nút xuất tệp ⇒ đúng điều kiện hiển thị `:582`, và chứng minh nút không hiện bừa.
- **Đối chứng đường thứ hai:** gọi thẳng dịch vụ xuất tệp trả **200** cho cả 3 phiên, kiểu nội dung đúng,
  và **tên tệp do máy chủ đặt** trong `content-disposition` trùng khít tên mà giao diện dùng khi tải về
  (chỉ khác phần giờ-phút do gọi ở phút khác) ⇒ khuôn tên không phải do phía giao diện tự đặt. Đọc lại bản
  ghi đánh giá cho `diem` = 4 / 5 / 3, `nhanXet` = đúng 2 câu tiếng Việt và `null`, `ngayDanhGia` khớp ngày
  hiển thị. **Hai đường đo không mâu thuẫn.**
- Bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1` ở cả 3 chặng đo, có bổ sung
  móc XHR vì ứng dụng gọi xuất tệp bằng XHR chứ không phải fetch): thao tác tạo phiên và gửi trả lời đều
  **1 request / 1 thông báo**, không lặp, không double-toast; thao tác bấm xuất tệp **không sinh thông báo**
  (đặc tả không đòi thông báo cho thao tác này).

### Bằng chứng

**1. Ảnh chụp:**

![Tab "Hoàn thành" của màn danh sách Tư vấn nhanh — toolbar chỉ có [+ Thêm mới] và [Làm mới], không có nút xuất tệp; 4 dòng đều ở trạng thái "Hoàn thành"](image/QLKCHTV_37-01-tab-HoanThanh-khong-co-nut-xuat.png)

![Màn chi tiết TVN-20260806-0001 — khối "Đánh giá" có nút [Xuất Excel] ở góc phải cùng 3 thẻ tổng hợp (Tổng đánh giá 1 lượt · Điểm trung bình 4.0/5 · Phân bố điểm 4★×1), bên dưới là 4 sao vàng, Ngày đánh giá 06/08/2026 và câu nhận xét tiếng Việt](image/QLKCHTV_37-02-chitiet-P1-khoi-DanhGia-co-nut-XuatExcel-va-3-the.png)

![Màn chi tiết TVN-20260806-0002 (dạng đánh giá KHÔNG có nhận xét) — nút [Xuất Excel] vẫn có và bấm được, 3 thẻ tổng hợp hiện 1 lượt / 5.0 trên 5 / 5★×1, dòng "Nhận xét" hiển thị dấu — vì đánh giá không kèm nhận xét](image/QLKCHTV_37-03-chitiet-P2-danhgia-khong-nhan-xet.png)

![Màn chi tiết TVN-20260806-0003 — phiên kênh "Thủ công", trùng khít kênh trong ảnh của đối tác; khối "Đánh giá" vẫn có nút [Xuất Excel], 3 thẻ tổng hợp 1 lượt / 3.0 trên 5 / 3★×1 và câu nhận xét tiếng Việt](image/QLKCHTV_37-04-chitiet-P3-kenh-ThuCong-trung-khit-anh-doi-tac.png)

![Đầu màn chi tiết TVN-20260806-0003 — nhãn trạng thái góc phải "Hoàn thành", thanh tiến trình Mới → Cán bộ trả lời → Hoàn thành, bảng Thông tin phiên tư vấn ghi Kênh = "Thủ công", MST 0109998887](image/QLKCHTV_37-05-P3-dau-man-kenh-ThuCong-trangthai-HoanThanh.png)

**2. Ba tệp thật nhận được từ chính 3 lượt bấm nút [Xuất Excel]:**
[`evidence/DanhGiaTvNhanh_TVN202608060001_20260806_1504.xlsx`](evidence/DanhGiaTvNhanh_TVN202608060001_20260806_1504.xlsx) — 7008 byte, md5 `86fafd5a6f41367dea1a8ceaf686da28` ·
[`evidence/DanhGiaTvNhanh_TVN202608060002_20260806_1506.xlsx`](evidence/DanhGiaTvNhanh_TVN202608060002_20260806_1506.xlsx) — 6940 byte, md5 `5db8194db8de6600ac1ec44bd5178f70` ·
[`evidence/DanhGiaTvNhanh_TVN202608060003_20260806_1510.xlsx`](evidence/DanhGiaTvNhanh_TVN202608060003_20260806_1510.xlsx) — 7000 byte, md5 `871e16220f29e2a6a053457faa481943`.

**3. Số đo đầy đủ (chỉ số nút từng lượt, nội dung từng tệp, kiểm khuôn tên, nhánh ngược, đối chứng máy chủ):**
[`ketqua-QLKCHTV_37.txt`](ketqua-QLKCHTV_37.txt) · tiêu chí chấm + bảng đóng GAP:
[`tieuchi/QLKCHTV_37.md`](tieuchi/QLKCHTV_37.md).

**4. Phản hồi máy chủ (đường đo thứ hai):**

```
GET /api/v1/tu-van-nhanhs/{id}/danh-gia/export → 200
  21beee47…  content-disposition: attachment; filename="DanhGiaTvNhanh_TVN202608060001_20260806_1510.xlsx"  7008 B  PK
  f9f1b33a…  content-disposition: attachment; filename="DanhGiaTvNhanh_TVN202608060002_20260806_1510.xlsx"  6939 B  PK
  5f3741ec…  content-disposition: attachment; filename="DanhGiaTvNhanh_TVN202608060003_20260806_1510.xlsx"  7000 B  PK

GET /api/v1/tu-van-nhanhs/{id}
  TVN-20260806-0001  HOAN_THANH  TV_NHANH     diem "4"  nhanXet "Cán bộ trả lời rõ ràng, …"  2026-08-06T08:02:53Z
  TVN-20260806-0002  HOAN_THANH  TV_NHANH     diem "5"  nhanXet null                          2026-08-06T08:02:53Z
  TVN-20260806-0003  HOAN_THANH  TV_THU_CONG  diem "3"  nhanXet "Nội dung tư vấn tạm ổn …"    2026-08-06T08:09:07Z
```

---

## BUG-TVV-QLTVV-02-R3 [CHỜ BA] — Danh sách Tư vấn viên / Chuyên gia không sắp xếp theo ngày công nhận mới nhất trước; đặc tả không quy định thứ tự

> **Re-test:** 2026-08-06 16:25:00 — ⚠️ **CẦN BA** (4/5 vế hết lỗi, 1 vế phải để BA chốt). Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng `HTPLDN · V1.0.8` / bó mã `assets/index-DIABnbIr.js` / `GET /` last-modified 06/08/2026 14:13:15 giờ VN · **N = 6/6 hàng trang 1 đo hết × 4 bề rộng** (1920 · 1440 · 1280 · 1024) = **26 lượt đo hàng** + 1 lượt đối chứng máy chủ · **M = 4/4 dạng** (chưa có điểm · đã có điểm · ô Hành động 3 điều khiển · ô Hành động 2 điều khiển) · **dữ liệu seed:** đổi `CG-QLND38-UAT` sang *Vô hiệu hóa* để dựng dạng thứ 4 rồi **khôi phục** về *Đang hoạt động*, **không đụng bản ghi nào khác**. Đo bằng `cbnv_tw_02` (CB_NV_TW, cấp TW — trùng khít vai trò + cấp của đối tác, **không nới chiều nào**). **Kết quả chỉ có hiệu lực cho env + bản dựng nêu trên.**

### Mô tả

Case này gộp **5 vế** trên màn *Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia*: (a) cột **Điểm ĐG**
tràn/đè lên cột **Trạng thái**; (b) cột Điểm ĐG hiển thị **không đồng nhất** giữa hàng chưa có điểm và hàng
đã có điểm; (c) các nút **Xem / Sửa bị xuống dòng**; (d) mặc định phải **sắp xếp theo ngày công nhận mới
nhất trước**; (e) **20 bản ghi mỗi trang**.

Đo lại bằng toạ độ thật trên bản dựng ghi ở đầu file: **4/5 vế không còn tái hiện** — (a) không hàng nào
chồng lấn, (b) hai ca dữ liệu đã hiển thị cùng một kiểu, (c) ô Hành động là icon nằm gọn một dòng,
(e) mặc định 20 mục/trang. **Riêng vế (d) vẫn khác kỳ vọng của đối tác**: danh sách đang sắp theo **ngày
tạo** mới nhất trước chứ không phải ngày công nhận. Đã tra `srs-fr-04-chuyen-gia-tvv.md` toàn bộ — **đặc tả
không có dòng nào quy định thứ tự sắp xếp mặc định của màn này**, nên không có căn cứ chấm phần mềm sai;
đưa sang BA chốt (câu hỏi ở [cau-hoi-BA.md](cau-hoi-BA.md)).

**Phân biệt với bug cùng mã ở vòng trước:** mã `QLTVV_02` đã có 2 mục ghi nhận trước đây, **nội dung khác
hẳn mục này** — vòng 1 (`reverify-week-2/bug-reports/Pass-bug-report-UAT-tuan-2.md`, đóng 14/07) là cột
"Loại" hiện mã viết tắt + cột Điểm ĐG sai thang `/10`; vòng 2
(`reverify-week-2/bug-reports/mang-luoi-tvv/Pass-bug-report-tuan-2-r2-mang-luoi-tvv.md`, đóng 29/07) là cột
Hành động dùng nhãn chữ thay vì nhóm icon. Cả hai đã đóng và **không** được vá lại; mục này (`-R3`) chỉ nói
về bộ 5 vế của lượt verify 06/08.

### Các bước tái hiện

1. Đăng nhập `cbnv_tw_02` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), cấp **TW**, đơn vị
   *Cục Bổ trợ tư pháp - Bộ Tư pháp*. Đây đúng vai trò + cấp đọc được trên ảnh của đối tác
   (`Cán bộ NV Trung ương  CB_NV_TW`, `BTP · TW`); theo `srs-fr-04-chuyen-gia-tvv.md:1420` vai trò này
   xem/sửa/xoá được tư vấn viên thuộc đơn vị. Tải lại trang, đọc dấu vân tay bản dựng.
2. Mạng lưới Tư vấn viên → **Tư vấn viên / Chuyên gia**, để nguyên tab mặc định **"Đang hoạt động"**,
   **không** đụng bộ lọc và **không** đụng bộ chọn số dòng.
3. Cuộn bảng sang phải để thấy đủ cụm cột **Điểm ĐG · Trạng thái · Ngày công nhận · Hành động**.
4. Đo **từng hàng** bằng toạ độ thật: `right` của ô Điểm ĐG so với `left` của ô Trạng thái; `right` của mọi
   phần tử con **và mọi đoạn văn bản** bên trong ô Điểm ĐG so với `right` của chính ô đó; `scrollWidth`
   và `clientWidth` của ô. Không nhìn bằng mắt.
5. Đo **ô Hành động từng hàng**: số điều khiển, chênh lệch `top` giữa các điều khiển, chiều cao khung ô so
   với chiều cao một điều khiển đơn, số hàng dòng thật của nhãn (`getClientRects().length`).
6. Lặp bước 3-5 ở **4 bề rộng cửa sổ**: 1920 (suy từ ảnh đối tác 1906 px) · 1440 · 1280 · 1024
   (ngưỡng tối thiểu đặc tả cam kết, `srs-fr-05-vu-viec.md:1601`).
7. Dựng dạng dữ liệu còn thiếu: đổi `CG-QLND38-UAT` sang **Vô hiệu hóa** để có ô Hành động bị ẩn bớt điều
   khiển, đo xong **khôi phục** về Đang hoạt động.
8. Lặp bước 3-5 trên 3 tab khác để phủ thêm hàng: **Mới đăng ký** (7 hàng) · **Yêu cầu bổ sung** (6 hàng) ·
   **Vô hiệu hóa** (1 hàng).
9. Đọc cột **"Ngày công nhận" của toàn bộ hàng trang 1** (không dừng ở 2-3 hàng đầu), kiểm dãy có giảm dần
   thật không.
10. Đếm thô `.ant-table-tbody tr.ant-table-row` ở trang 1 và đối chiếu chữ ở chân bảng; mở bộ chọn số dòng
    đọc các lựa chọn và lựa chọn đang được chọn.
11. Đối chứng bằng đường thứ hai: đọc lại **chính lời gọi danh sách mà giao diện dùng** để so thứ tự bản ghi
    máy chủ trả về với thứ tự trên màn.

### Kết quả mong đợi

- Theo `srs-fr-04-chuyen-gia-tvv.md:1452` và `:1453`, **Điểm đánh giá** và **Trạng thái** là **hai thành phần
  riêng** của bảng ⇒ nội dung của thành phần này không được lấn sang chỗ của thành phần kia.
- Theo `srs-fr-05-vu-viec.md:1568`-`:1573` (§C, áp cho toàn hệ thống theo `srs-v3.5.md:6696`), cách xử lý nội
  dung dài mà đặc tả chọn là **cắt trong ô + tooltip**; không có chỗ nào cho phép nội dung hiện tràn sang ô
  khác. Hành vi này phải đúng ít nhất tới bề rộng **1024** (`srs-fr-05-vu-viec.md:1601`).
- Theo `srs-fr-04-chuyen-gia-tvv.md:1455` và **Phụ lục E §H6** (`srs-v3.5.md:6714`), cột **Hành động** là
  **nhóm icon** (mắt / bút chì / thùng rác) **thay cho nhãn text**, mỗi icon bắt buộc có `aria-label` và
  tooltip; icon Sửa **ẩn khi trạng thái Vô hiệu hóa**. Nhóm icon phải nằm trọn trên **một dòng**.
- Theo `srs-fr-04-chuyen-gia-tvv.md:1457`, `:247` (FR-IV-02 §Processing) và `BR-DATA-07`
  (`srs-fr-05-vu-viec.md:2394`), danh sách mặc định **20 mục/trang** và **hiển thị tổng của mỗi tab**.
- Theo `srs-fr-04-chuyen-gia-tvv.md:2538` (BR-CALC-06), `:958`, `:962`: điểm đánh giá trung bình theo thang
  **1–5**, một chữ số thập phân; **chưa có đánh giá → hiển thị `"—/5"`, không hiển thị `0`**.
- **Thứ tự sắp xếp mặc định của màn này thì đặc tả KHÔNG quy định.** Đã tra `srs-fr-04-chuyen-gia-tvv.md`
  bằng `sắp xếp` / `sort` / `ORDER BY` / `DESC` / `mới nhất trước` → **0 kết quả**; FR-IV-02 §Processing
  (`:243`-`:247`) chỉ có kiểm quyền → kết hợp điều kiện → phân trang; `BR-DATA-07` cũng chỉ nói phân trang.
  (Đối chiếu: các nhóm khác **có** quy định thứ tự — `srs-fr-08-danh-gia.md:904`,
  `srs-fr-12-tv-chuyen-sau.md:1132`, `srs-fr-05-vu-viec.md:1665` — nên đây là chỗ bỏ trống của nhóm IV chứ
  không phải nằm ở tài liệu khác.) ⇒ vế này **không có căn cứ chấm đúng/sai**, phải để BA chốt.

### Kết quả thực tế

- **Vế (a) — không còn tràn/đè.** 6/6 hàng tab "Đang hoạt động" × 4 bề rộng, cộng 13 hàng của 2 tab khác
  (tổng **26 lượt đo hàng**): `right(ô Điểm ĐG) − left(ô Trạng thái)` = **đúng 0 px** ở mọi lượt (hai ô kề
  nhau, dùng chung đường viền). Nội dung bên trong ô Điểm ĐG còn cách mép phải của ô **27,1 → 36,6 px**
  (số đo `dgContentSpillPx` âm ⇒ nằm trong ô), `scrollWidth − clientWidth` của ô = **0** ⇒ không có phần
  nội dung nào bị đẩy ra ngoài. Chữ "Đang hoạt động" đọc nguyên vẹn trên ảnh, không bị ký tự nào chèn lên.
  Bảng vẫn **cuộn ngang** ở 1024/1280/1440 (`scrollWidth 1530 > clientWidth 889` ở 1024) đúng như ảnh đối
  tác, tức là vẫn ở đúng cảnh dễ lộ tràn — mà không tràn.
- **Vế (b) — hai ca dữ liệu đã hiển thị cùng một kiểu.** Hàng **chưa có đánh giá** (4 hàng) hiện **5 sao xám
  + chuỗi `—/5`**; hàng **đã có đánh giá** hiện **5 sao, tô vàng theo điểm + chuỗi `4.1/5` / `3.3/5`**.
  Cây trợ năng đọc được 5 phần tử sao ở **cả hai** ca (ca có điểm thì 4 và 3 phần tử ở trạng thái đã chọn).
  ⇒ Khác nhau chỉ ở **giá trị dữ liệu**, không phải ở **kiểu hiển thị** — bất đồng đối tác nêu **không còn**.
  Giá trị đo được đều trong thang 1–5, một chữ số thập phân, đúng BR-CALC-06.
- **Vế (c) — nút thao tác không xuống dòng, và đã là icon.** Ô Hành động có **3 điều khiển** (24×24 px mỗi
  cái, toạ độ x = 873 · 905 · 937 @1024), chênh lệch `top` giữa chúng = **0 px**; chiều cao khung ô = **24 px**
  = chiều cao một điều khiển đơn (hai dòng thì phải ≥ 48 px); `getClientRects().length` = **1**;
  **không còn ký tự chữ nào** trong ô (`anyText = false`, 3 hình vẽ / ô) và đủ `aria-label`
  *"Xem chi tiết …" / "Sửa …" / "Xóa …"* đúng Phụ lục E §H6. Đúng ở cả 4 bề rộng và cả 3 tab đã đo.
  Ở trạng thái **Vô hiệu hóa**, ô Hành động còn **đúng 2 icon** (mắt + thùng rác) trên một dòng — icon Sửa
  đã ẩn đúng `:1455`.
- **Vế (d) — vẫn khác kỳ vọng đối tác.** Đọc **toàn bộ 6/6 hàng** trang 1, cột Ngày công nhận theo thứ tự
  hiển thị: `—` · `17/07/2026` · `12/07/2026` · `—` · `—` · `—` ⇒ **không giảm dần**, và hàng trống cũng
  không dồn về một phía. Đối chứng đường thứ hai: đọc lại chính lời gọi danh sách mà giao diện dùng — thứ tự
  máy chủ trả về **trùng khít** thứ tự trên màn, và trường **ngày tạo** của dãy đó giảm dần **tuyệt đối**
  (05/08 → 12/07 09:55 → 12/07 00:11 → 30/06 → 01/03/2026 → 01/02/2024). ⇒ Danh sách đang sắp theo **ngày
  tạo mới nhất trước**. **Hai đường đo không mâu thuẫn.** Vì đặc tả không quy định thứ tự nên **không chấm
  phần mềm sai** — đưa BA chốt.
- **Vế (e) — mặc định 20 mục/trang, đúng phần đặc tả nêu.** Vào màn không đụng tay: đường dẫn mang
  `pageSize=20`, chân bảng hiện **"20 / trang"** ở cả **4 tab** đã mở và cả 4 bề rộng; bộ chọn có
  10/20/50/100 và đang chọn 20. Tổng mỗi tab hiển thị đúng: `1-6 / 6 mục` · `1-7 / 7 mục` · `1-6 / 6 mục` ·
  `1-1 / 1 mục`; đếm thô số hàng bảng cho **6 · 7 · 6 · 1**, khớp con số ở chân bảng.
  **Giới hạn đã ghi rõ:** tab đông nhất chỉ có 7 bản ghi (< 21) nên **chưa dựng được cảnh trang bị cắt**;
  bộ chọn nhỏ nhất là 10/trang nên cũng không ép cắt được. Muốn chứng minh việc cắt trang phải seed thêm
  **≥ 14 bản ghi vào cùng một tab**. Ảnh của đối tác cũng chỉ có 10 bản ghi nên phía đối tác cũng chưa
  chạm cảnh này.
- Bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`): hai lượt đổi trạng thái
  bản ghi seed đều **1 request / 1 thông báo** *"Cập nhật trạng thái thành công"*, không lặp, không
  double-toast. Thao tác chuyển tab và cuộn bảng không sinh thông báo (đặc tả không đòi).

### Bằng chứng

**1. Ảnh chụp:**

![Toàn bảng ở bề rộng 1920 — cột Điểm ĐG (5 sao + "—/5" ở hàng chưa có điểm, sao vàng + "4.1/5" · "3.3/5" ở hàng có điểm) nằm gọn, không đè lên cột Trạng thái "Đang hoạt động"; cột Ngày công nhận đọc theo thứ tự — · 17/07/2026 · 12/07/2026 · — · — · — (không giảm dần); cột Hành động 3 icon một dòng; chân bảng "1-6 / 6 mục" + "20 / trang"](image/QLTVV_02-03-1920-toan-bang-cot-NgayCongNhan-khong-giam-dan.png)

![Bề rộng 1440, bảng đã cuộn sang phải đúng cảnh trong ảnh của đối tác — cụm cột Điểm ĐG · Trạng thái · Ngày công nhận · Hành động, không có chữ số nào chèn vào chữ "Đang hoạt động", 3 icon thao tác nằm trên một dòng](image/QLTVV_02-01-1440-cuon-phai-DiemDG-TrangThai-Ngay-HanhDong.png)

![Bề rộng 1024 — ngưỡng tối thiểu đặc tả cam kết; bảng vẫn cuộn ngang (1530 > 889) nhưng ô Điểm ĐG và ô Trạng thái vẫn kề nhau đúng 0 px chồng lấn, cụm 3 icon vẫn một dòng](image/QLTVV_02-02-1024-be-rong-toi-thieu-khong-tran-khong-xuong-dong.png)

![Tab "Vô hiệu hóa" (dạng dữ liệu thứ 4, đo lúc bản ghi seed CG-QLND38-UAT đang bị vô hiệu hóa) — ô Hành động còn đúng 2 icon (mắt xanh + thùng rác đỏ) trên một dòng, icon Sửa đã ẩn đúng đặc tả](image/QLTVV_02-04-1440-tab-VoHieuHoa-o-HanhDong-2-icon-1-dong.png)

**2. Số đo đầy đủ (toạ độ từng hàng × 4 bề rộng, số điều khiển từng ô, thứ tự ngày, đối chứng máy chủ):**
[`ketqua-QLTVV_02.txt`](ketqua-QLTVV_02.txt) · tiêu chí chấm + bảng đóng GAP:
[`tieuchi/QLTVV_02.md`](tieuchi/QLTVV_02.md) · câu hỏi gửi BA: [`cau-hoi-BA.md`](cau-hoi-BA.md) ·
bằng chứng gốc của đối tác: [`partner-evidence/QLTVV_02_v2.png`](partner-evidence/QLTVV_02_v2.png).

**3. Phản hồi máy chủ (đường đo thứ hai — lưu tại [`tvv-list.network-response`](tvv-list.network-response)):**

```
GET /api/v1/tu-van-viens?page=1&pageSize=20&trangThai=HOAT_DONG → 200
  meta { page 1, pageSize 20, total 6, totalPages 1 }
  #  maTvv              ngayCongNhan   ngayTao                diemDanhGiaTb
  1  CG-QLND38-UAT      null           2026-08-05T05:33:14    null
  2  TVV-STP-AG-0001    2026-07-17     2026-07-12T09:55:44    null
  3  TVV-BTP-TW-0002    2026-07-12     2026-07-12T00:11:49    4.1
  4  TVV-SEED-0001      null           2026-06-30T12:28:23    3.3
  5  DDD-TVV-022        null           2026-03-01T00:00:00    null
  6  DDD-TVV-021        null           2024-02-01T00:00:00    null
  ⇒ trùng khít thứ tự trên màn; ngayTao giảm dần tuyệt đối, ngayCongNhan thì không.
```

---

## ~~BUG-TVV-CNHSNLTVV-03~~ [CLOSED] — Cập nhật năng lực có đính tệp chứng chỉ: tệp đính kèm không hiện đúng tên, và hồ sơ đã có tệp chứng chỉ thì không mở lại được form cập nhật năng lực

> **Re-test:** 2026-08-07 03:05:00 R5 — ✅ **PASS (Closed-verified)**. Đo lại trọn vẹn trên bó mã `assets/index-D4Buvu4S.js` · `GET /` last-modified `Thu, 06 Aug 2026 19:23:01 GMT` (02:23 giờ VN 07/08) · vân tay ĐẦU = CUỐI phiên ⇒ R4 + R5 cùng một bản dựng, ghép hợp lệ · tài khoản `nht_qa_tw`. **Đủ 6/6 lượt [Lưu]** (N = 3 hồ sơ × M = 3 dạng, vượt mức khoá N=2×M=3): 2 lượt đối chứng không tệp + 4 lượt có tệp **bắt chéo đủ 4 ô** giữa 2 hồ sơ × 2 kiểu tên tệp. ① Chuỗi kỹ thuật `{"fileDinhKemId":…}` ở dòng "Chứng chỉ chi tiết" tab Năng lực **đã hết** — hiện đúng tên tệp, kể cả tên có dấu cách/ngoặc/`&`; 3 bản ghi cũ từ R3 cũng đã tự hiện đúng tên. ② `[Cập nhật năng lực]` trên hồ sơ đã có tệp: **8/8 lượt mở được form**, 0 lượt bị đẩy `/403`. ③ Đường đo thứ hai: `GET /api/v1/files/{id}` → **200 cho 5/5 tệp**, hết sạch `403 ERR-PERM-FILE-03` (gồm đủ 3 tệp từng hỏng ở R3). ④ Lỗi gốc `500` / "Lỗi hệ thống, vui lòng thử lại sau." không tái hiện; mỗi lượt 1 request ↔ 1 toast; 0 tệp thừa. **Bảng GAP: trống.** Nhật ký: [`../reverify-week-5/F3-devfix-2026-08-07/do/CNHSNLTVV_03-R4-dobanmoi.md`](../reverify-week-5/F3-devfix-2026-08-07/do/CNHSNLTVV_03-R4-dobanmoi.md) · [`…/do/CNHSNLTVV_03-R5-lapgap.md`](../reverify-week-5/F3-devfix-2026-08-07/do/CNHSNLTVV_03-R5-lapgap.md).

### Mô tả

Đối tác phản ánh ở màn *Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → chi tiết hồ sơ →
tab Năng lực → **Cập nhật năng lực***: nhập dữ liệu hợp lệ rồi bấm lưu thì hệ thống **không lưu**
mà hiện thông báo *"Lỗi hệ thống, vui lòng thử lại sau."*

Đo lại bằng thao tác thật trên bản dựng ghi ở đầu file: **vẫn tái hiện, nhưng chỉ ở một nhánh**.
Phiếu của đối tác chỉ ghi *"Nhập dữ liệu hợp lệ"* mà không nói trường nào, nên đã chạy đủ **5 nhánh
khả dĩ** của form trên **2 hồ sơ**. Kết quả tách bạch: bốn lượt lưu **không** đính tệp (sửa trường
chữ/số · đổi lĩnh vực pháp luật · thêm-sửa bằng cấp & chứng chỉ chi tiết) đều lưu thành công và dữ
liệu còn nguyên sau khi tải lại trang; nhưng **cả ba lượt có đính tệp trong khối "Thêm chứng chỉ mới"
đều hỏng** với đúng câu chữ đối tác báo. Ảnh của đối tác cũng đang đính đúng một tệp PDF trong khối
đó — khớp với nhánh hỏng đo được.

Vì phần lưu đã chạy được ở các nhánh khác nên đây là ca **fix một phần**, không phải chưa fix gì.

### Các bước tái hiện

1. Đăng nhập `nht_qa_tw` — vai trò **NHT** (Người hỗ trợ pháp lý), đơn vị
   `00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - Bộ Tư pháp), cấp **TW**.
   Đây là vai trò đọc được trên ảnh của đối tác (huy hiệu `NHT`) và cũng là vai trò duy nhất đặc tả
   cho phép thao tác này (`srs-fr-04-chuyen-gia-tvv.md:375` tác nhân là NHT; `:1576` điều kiện hiển
   thị tab Năng lực là *"Vai trò = Người hỗ trợ (TVV cùng đơn vị)"*). Tải lại trang để chắc chắn đang
   chạy bản dựng mới, đọc dấu vân tay bản dựng.
2. Mạng lưới Tư vấn viên → **Tư vấn viên / Chuyên gia** → mở hồ sơ `TVV-BTP-TW-0002` → tab **Năng lực**
   → **[Cập nhật năng lực]**.
3. **Nhánh không có tệp (làm trước để có mốc so sánh):** sửa Trình độ / Số năm kinh nghiệm / Chuyên
   ngành / Số thẻ hành nghề / Kinh nghiệm chi tiết → lưu. Rồi đổi **Lĩnh vực pháp luật** (thêm 2 thẻ,
   bớt 1 thẻ) → lưu. Rồi **thêm 1 bằng cấp + thêm 1 chứng chỉ + sửa nơi cấp của chứng chỉ cũ** → lưu.
   Sau mỗi lượt: **tải lại trang, đọc lại dữ liệu trên màn**.
4. **Nhánh có tệp:** mở lại form, ở khối **"Thêm chứng chỉ mới (PDF, tối đa 10 file)"** đính **1 tệp PDF**
   (dùng đúng kiểu tên tệp của đối tác: `2K15 T3 (4.8) & CN (9.8).pdf`, 638 B), nhập Ghi chú cập nhật
   `a` — dựng lại đúng cảnh trong ảnh của đối tác → bấm **[Lưu]**. Quan sát thông báo.
5. **Tách biến tên tệp:** lặp bước 4 với tệp tên chỉ có chữ/số/gạch nối (`B7-CNHSNLTVV03-chungchi-A.pdf`).
6. **Tách biến hồ sơ:** lặp bước 3 và bước 4 trên hồ sơ **QA tự tạo mới** `TVV-BTP-TW-0038`
   (trạng thái *Mới đăng ký*) để loại trừ khả năng lỗi chỉ xảy ra trên hồ sơ dev đã đụng vào.
7. Sau mỗi lượt hỏng: **tải lại trang và đọc lại hồ sơ** xem có ghi được gì không.
8. Đối chứng bằng đường thứ hai: gửi lại **đúng thân yêu cầu** của lượt hỏng nhưng **bỏ trường mang
   tệp chứng chỉ mới**, so mã phản hồi với lượt có trường đó.

### Kết quả mong đợi

- Theo `srs-fr-04-chuyen-gia-tvv.md:433` (AC2 của FR-IV-04): *"**Given** NHT cập nhật thông tin/chứng chỉ
  + upload file **When** lưu **Then** validate và lưu thành công"* — nghĩa là lượt lưu **có kèm tệp tải lên**
  cũng phải lưu được, đây là ca đặc tả nêu đích danh chứ không phải suy diễn.
- Theo `:388`, tệp chứng chỉ mới là **đầu vào hợp lệ** của chức năng (`chung_chi_moi`, PDF, tối đa 10MB/tệp,
  tổng 50MB, tối đa 10 tệp). Tệp dùng để đo là PDF 638 B và 624 B — nằm sâu trong giới hạn đó.
- Theo `:402`–`:403` (§Processing bước 4-5), khi lưu, hệ thống cập nhật hồ sơ năng lực **và** tạo bản ghi
  tệp đính kèm nếu có tệp mới; theo `:418` (§Postconditions) kết cục bắt buộc là **hồ sơ năng lực được
  cập nhật**.
- Theo `:425`–`:429` (§Error Handling), chức năng này chỉ được phép **từ chối** trong 5 tình huống cụ thể —
  khác đơn vị, tệp vượt 10MB, tổng vượt 50MB, quét thấy mã độc, hồ sơ đã vô hiệu hóa — và mỗi tình huống
  đều phải nói rõ lý do cho người dùng. Dữ liệu đo được **không rơi vào tình huống nào** trong 5 tình huống
  đó, nên hệ thống không được từ chối; và nếu có từ chối thì cũng không được báo một câu chung chung
  không nêu lý do.
- **Không** dùng để chấm lỗi: nhãn nút là *Lưu* hay *Đồng ý*, form là inline hay hộp thoại (`:432` không
  chốt); câu chữ cụ thể của thông báo **thành công** (đặc tả không quy định).

### Kết quả thực tế

**▸ Lượt đo R3 2026-08-07 (bản dựng `V1.0.9` — MỚI):**

- **Lỗi gốc đã hết.** 4/4 lượt lưu CÓ đính tệp ở khối "Thêm chứng chỉ mới" (2 kiểu tên tệp × 2 hồ sơ) đều báo
  *"Cập nhật năng lực thành công"*; mỗi lượt đúng **1 request ghi / 1 thông báo** theo mốc giờ (bộ đếm
  `tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1` trước **mỗi** lượt). Không còn câu
  *"Lỗi hệ thống, vui lòng thử lại sau."*, máy chủ không còn trả 500.
- **Nhưng tệp vừa đính không hiện đúng tên.** Tải lại trang, dòng **"Chứng chỉ chi tiết"** hiện chuỗi kỹ thuật
  `{"fileDinhKemId":"80ae5609-a269-4bf3-a7b1-8c33942462c9"}` thay vì tên tệp. Lặp lại y hệt trên cả 3 hồ sơ.
- **Và hồ sơ đã có tệp chứng chỉ thì không mở lại được form.** Bấm [Cập nhật năng lực] ⇒ chuyển sang trang
  **403 — *"Bạn không có quyền truy cập trang này. Vai trò hiện tại: Người hỗ trợ pháp lý"***, form không mở.

  | Hồ sơ | Loại | Trạng thái | Đã có chứng chỉ kèm tệp? | Mở được form? |
  |---|---|---|---|---|
  | `TVV-BTP-TW-0002` | Chuyên gia | Đang hoạt động | **có** (sẵn từ trước) | ❌ trang 403 |
  | `CG-QLND38-UAT` | Chuyên gia | Đang hoạt động | không | ✅ mở |
  | `TVV-BTP-TW-0038` *(trước khi đính tệp)* | Tư vấn viên | Mới đăng ký | không | ✅ mở |
  | `TVV-BTP-TW-0038` *(sau khi đính tệp)* | Tư vấn viên | Mới đăng ký | **có** | ❌ trang 403 |
  | `TVV-BTP-TW-0003` *(sau khi đính tệp)* | Tư vấn viên | Đang thẩm định | **có** | ❌ trang 403 |

  ⇒ Yếu tố quyết định không phải loại hồ sơ / trạng thái / đơn vị, mà là **hồ sơ đã có chứng chỉ kèm tệp**.
  Hệ quả: đính tệp thành công một lần rồi thì **từ đó không sửa được năng lực của hồ sơ đó nữa**.
  Vì vậy hồ sơ (i) `TVV-BTP-TW-0002` **không bấm được lượt [Lưu] nào** ở vòng này.
- **Đường đo thứ hai (đọc tệp qua máy chủ):** `GET /api/v1/files/{id}` trả **403 `ERR-PERM-FILE-03` —
  *"Loại đối tượng 'TVV_HO_SO' của tệp chưa được đăng ký"*** với **3/3** tệp thử (tệp QA vừa đính, tệp có sẵn
  trên `TVV-BTP-TW-0002`, tệp thẻ hành nghề cũ) ⇒ không tệp nào thuộc hồ sơ tư vấn viên đọc lại được.
- **Đọc lại bản ghi qua máy chủ** khớp với màn hình: `fileDinhKems` có đúng tên tệp vừa đính và
  `hoSo.chungChiChiTiet` có phần tử tương ứng ⇒ chiều ghi đúng, chỗ hỏng nằm ở chiều đọc/hiển thị.
- **Ghi nhận đúng đặc tả, không tính lỗi:** hồ sơ `TVV-BTP-TW-0003` tự chuyển *Yêu cầu bổ sung → Đang thẩm định*
  sau khi lưu năng lực — đúng `srs-fr-04-chuyen-gia-tvv.md:405`.

**▸ Lượt đo R2 2026-08-06 (bản dựng `V1.0.8` — để đối chiếu):**

- **Vẫn tái hiện đúng câu chữ đối tác báo**, ở **3/3 lượt lưu có đính tệp chứng chỉ mới**. Chữ đọc bằng
  bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1` ở cả 4 chặng đo):
  **"Lỗi hệ thống, vui lòng thử lại sau."** — trùng khít ô *Kết quả thực tế* của đối tác.
  Mỗi lượt đúng **1 request ghi / 1 thông báo tính theo mốc giờ** ⇒ không double-toast, không gửi 2 lần.
- **Phản hồi máy chủ của chính lượt bấm đó là lỗi máy chủ**, không phải lỗi nghiệp vụ:

  | Lượt | Hồ sơ | Tệp đính | Kết quả |
  |---|---|---|---|
  | M1 — sửa trường chữ/số | `TVV-BTP-TW-0002` | không | ✅ *"Cập nhật năng lực thành công"* |
  | M2 — đổi lĩnh vực pháp luật | `TVV-BTP-TW-0002` | không | ✅ *"Cập nhật năng lực thành công"* |
  | M3 — thêm/sửa bằng cấp & chứng chỉ chi tiết | `TVV-BTP-TW-0002` | không | ✅ *"Cập nhật năng lực thành công"* |
  | M4 — tệp tên có ký tự đặc biệt + ghi chú `a` | `TVV-BTP-TW-0002` | `2K15 T3 (4.8) & CN (9.8).pdf` 638 B | ❌ **HTTP 500** *"Lỗi hệ thống, vui lòng thử lại sau."* |
  | M4b — tệp tên thường | `TVV-BTP-TW-0002` | `B7-CNHSNLTVV03-chungchi-A.pdf` 624 B | ❌ **HTTP 500** — cùng câu |
  | N2-M1 — sửa trường chữ | `TVV-BTP-TW-0038` | không | ✅ *"Cập nhật năng lực thành công"* |
  | N2-M4 — tệp tên thường | `TVV-BTP-TW-0038` | `B7-CNHSNLTVV03-chungchi-B.pdf` 624 B | ❌ **HTTP 500** — cùng câu |

- **Tên tệp KHÔNG phải nguyên nhân.** Tệp tên có dấu cách + ngoặc đơn + dấu `&` và tệp tên chỉ chữ/số/
  gạch nối hỏng y hệt nhau ⇒ loại được giả thuyết "lỗi do ký tự đặc biệt trong tên tệp".
- **Hồ sơ KHÔNG phải nguyên nhân.** Hồ sơ có sẵn (*Đang hoạt động*, đúng hồ sơ dev khai đã verify) và hồ sơ
  QA tự tạo mới (*Mới đăng ký*) hỏng y hệt nhau ⇒ loại được giả thuyết "chỉ hỏng trên dữ liệu cũ".
- 🔴 **Tải lại trang đọc lại: KHÔNG có gì được lưu** ở các lượt hỏng. `TVV-BTP-TW-0002` giữ nguyên số hiệu
  phiên bản 25 và ghi chú cập nhật rỗng; `TVV-BTP-TW-0038` có danh sách chứng chỉ chi tiết rỗng. Đúng như
  đối tác phản ánh — không phải "báo lỗi nhưng thực ra đã lưu".
- **Đối chứng đường thứ hai — tách được đúng một biến.** Gửi lại **đúng thân yêu cầu** của lượt hỏng nhưng
  **bỏ trường mang tệp chứng chỉ mới** (`chungChiMoiIds`), giữ nguyên mọi trường còn lại, cùng bản ghi cùng
  phiên cùng tài khoản → **HTTP 200**, hồ sơ cập nhật thật. So thân yêu cầu của 3 lượt hỏng với 4 lượt đạt:
  **khác nhau đúng ở một trường duy nhất là danh sách tệp chứng chỉ mới**. **Hai đường đo không mâu thuẫn.**
- **Việc tải tệp lên là bước riêng và bước đó chạy được** — giao diện gửi tệp lên trước (máy chủ nhận, trả
  mã tạo thành công, không sinh thông báo), rồi mới gửi lượt lưu; lượt lưu mới là chỗ hỏng.
- **Hệ quả kèm theo của chính thao tác hỏng này** (đo được, không mở phiếu riêng): tệp đã tải lên **không
  được gỡ** khi lượt lưu hỏng, nên mỗi lần người dùng bấm lưu lại là hồ sơ có thêm một bản ghi tệp thừa —
  đo được 2 tệp thừa trên `TVV-BTP-TW-0002` và 4 tệp thừa (3 bản trùng tên) trên `TVV-BTP-TW-0038`.
  Các tệp này lại **không** hiện ở khối *"Chứng chỉ hiện có"* (vẫn *"Chưa có chứng chỉ nào."*) vì bước gắn
  chứng chỉ nằm trong chính lượt lưu đã hỏng. QA đã dọn sạch toàn bộ tệp thừa sau khi đo.
- **Không kết luận được fix có tác dụng hay không** đối với nhánh nào, vì QA không có ảnh "trước khi fix" của
  chính mình; chỉ kết luận **hiện trạng so với đặc tả**: nhánh có tệp đang sai `:433`.

### Bằng chứng

**1. Ảnh chụp:**

![Form "Cập nhật năng lực" của TVV-BTP-TW-0002 ngay TRƯỚC khi bấm [Lưu] — dựng lại đúng cảnh ảnh đối tác: "Chứng chỉ hiện có → Chưa có chứng chỉ nào.", vùng kéo thả, hàng tệp "2K15 T3 (4.8) & CN (9.8).pdf (638 B)" với 2 điều khiển Xem/Xóa, ô Ghi chú cập nhật = "a" (1/2000), 2 nút [Làm lại] [Lưu]](image/CNHSNLTVV_03-R2-01-M4-truoc-khi-bam-Luu-tep-va-ghichu-a.png)

![Cùng màn đó SAU khi bấm [Lưu] — thông báo đỏ "Lỗi hệ thống, vui lòng thử lại sau." nổi giữa trên, tệp và ghi chú vẫn còn nguyên trong form vì chưa lưu được](image/CNHSNLTVV_03-R2-02-M4-thong-bao-Loi-he-thong-vui-long-thu-lai-sau.png)

![Hồ sơ QA tự tạo mới TVV-BTP-TW-0038 — form trước khi bấm [Lưu], đang đính "B7-CNHSNLTVV03-chungchi-B.pdf (624 B)" (tên tệp chỉ có chữ/số/gạch nối), ghi chú "QA R2 N2-M4 dinh tep chung chi"](image/CNHSNLTVV_03-R2-03-N2-form-truoc-khi-bam-Luu-tep-chungchi-B.png)

![Cùng màn TVV-BTP-TW-0038 sau khi bấm [Lưu] — vẫn "Lỗi hệ thống, vui lòng thử lại sau." ⇒ không phải chuyện riêng của hồ sơ dev đã đụng vào, cũng không phải do tên tệp](image/CNHSNLTVV_03-R2-04-N2-thong-bao-Loi-he-thong-tren-hoso-QA-tu-tao.png)

![Tab Năng lực của TVV-BTP-TW-0002 SAU khi hoàn nguyên — Trình độ "Cử nhân", Số năm "—", 1 bằng cấp, 1 chứng chỉ (nơi cấp "Bo Tu phap"), Số thẻ "STHN-QA-28", 4 lĩnh vực Thương mại/Thuế/Lao động/Đất đai: khớp mốc gốc](image/CNHSNLTVV_03-R2-05-da-hoan-nguyen-TVV-BTP-TW-0002.png)

**Ảnh lượt đo R3 2026-08-07 (bản dựng V1.0.9):**

![Trang 403 "Bạn không có quyền truy cập trang này. Vai trò hiện tại: Người hỗ trợ pháp lý" hiện ra ngay sau khi bấm [Cập nhật năng lực] trên hồ sơ đã có tệp chứng chỉ; sidebar ghi HTPLDN · V1.0.9](image/CNHSNLTVV_03-R3-05-sau-khi-dinh-tep-form-bi-chan-403.png)

![Tab Năng lực của TVV-BTP-TW-0038 sau lượt lưu CÓ đính tệp tên đặc biệt — dòng "Chứng chỉ chi tiết" hiện chuỗi {"fileDinhKemId":"80ae5609-a269-4bf3-a7b1-8c33942462c9"} thay cho tên tệp](image/CNHSNLTVV_03-R3-03-N2-M2-sau-luu-chungchi-hien-chuoi-JSON.png)

![Tab Năng lực của TVV-BTP-TW-0003 sau lượt lưu CÓ đính tệp tên thường — cũng hiện chuỗi {"fileDinhKemId":"3f11f7e4-…"}, Số thẻ hành nghề STHN-QA-99](image/CNHSNLTVV_03-R3-04-N3-M3-sau-luu-chungchi-hien-chuoi-JSON.png)

![Tab Năng lực của TVV-BTP-TW-0038 sau lượt lưu KHÔNG đính tệp — "Chứng chỉ chi tiết —", Kinh nghiệm chi tiết đã nhận chuỗi vừa nhập ⇒ nhánh không tệp lưu được](image/CNHSNLTVV_03-R3-02-N2-M1-sau-luu-khong-tep-chungchi-trong.png)

![Form của CG-QLND38-UAT còn nguyên trên màn sau lượt lưu bị từ chối "Hồ sơ năng lực không tồn tại"](image/CNHSNLTVV_03-R3-01-CG-QLND38-form-van-mo-sau-luot-luu-that-bai.png)

**Ảnh lượt đo R2 2026-08-06 (bản dựng V1.0.8) ở trên.**

**Nhật ký đo đầy đủ lượt R3:** [`../reverify-week-5/F3-devfix-2026-08-07/do/CNHSNLTVV_03.md`](../reverify-week-5/F3-devfix-2026-08-07/do/CNHSNLTVV_03.md)

**2. Số đo đầy đủ (từng lượt bấm, số request / số thông báo theo mốc giờ, dữ liệu sau khi tải lại trang,
đối chứng máy chủ, bảng hoàn nguyên):** [`ketqua-CNHSNLTVV_03.txt`](ketqua-CNHSNLTVV_03.txt) ·
tiêu chí chấm + bảng đóng GAP: [`tieuchi/CNHSNLTVV_03.md`](tieuchi/CNHSNLTVV_03.md) ·
bằng chứng gốc của đối tác: [`partner-evidence/CNHSNLTVV_03.jpg`](partner-evidence/CNHSNLTVV_03.jpg).

**3. Phản hồi máy chủ (đường đo thứ hai) —** lưu tại
[`evidence/CNHSNLTVV_03-R2-M4-patch-nang-luc-500.network-response`](evidence/CNHSNLTVV_03-R2-M4-patch-nang-luc-500.network-response)
và thân yêu cầu tại
[`evidence/CNHSNLTVV_03-R2-M4-patch-nang-luc-500.network-request`](evidence/CNHSNLTVV_03-R2-M4-patch-nang-luc-500.network-request):

```
PATCH /api/v1/tu-van-viens/98cfd963-…/nang-luc   (thân CÓ "chungChiMoiIds")   → 500
  {"success":false,"error":{"code":"ERR-SYS-00-00-01",
   "message":"Lỗi hệ thống, vui lòng thử lại sau",
   "timestamp":"2026-08-06T10:15:49.864Z",
   "requestId":"e10bfc79-6b1b-48b2-a543-5444d8f072e5"}}

PATCH /api/v1/tu-van-viens/98cfd963-…/nang-luc   (thân Y HỆT, BỎ "chungChiMoiIds") → 200  success true
POST  /api/v1/tu-van-viens/98cfd963-…/files      (bước tải tệp lên)                 → 201  (chạy được)
```

### Cách verify sau khi fix — *CHỈ dùng cho bug **Reopen***

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản nht_qa_tw / Test@1234 — vai trò Người hỗ trợ pháp lý, đơn vị Cục Bổ trợ tư pháp -
  Bộ Tư pháp, cấp TW. Màn: Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → mở hồ sơ → tab "Năng lực" →
  [Cập nhật năng lực].
  Dữ liệu phải có sẵn: 3 hồ sơ cùng đơn vị với tài khoản trên, và cả 3 đều đã có sẵn phần năng lực (mở tab
   "Năng lực" thấy có Trình độ hoặc Số thẻ hành nghề, không phải toàn dấu "—") —
   (i) 1 hồ sơ Đang hoạt động ĐÃ có chứng chỉ kèm tệp từ trước, ví dụ TVV-BTP-TW-0002;
   (ii) 1 hồ sơ Mới đăng ký, dòng "Chứng chỉ chi tiết" còn là dấu "—", ví dụ TVV-BTP-TW-0037;
   (iii) 1 hồ sơ Yêu cầu bổ sung, dòng "Chứng chỉ chi tiết" còn là dấu "—", ví dụ TVV-BTP-TW-0026.
   Thiếu thì tạo bằng luồng chuẩn: Tư vấn viên / Chuyên gia → [Thêm mới] → điền hồ sơ tối thiểu → lưu.
  Cần thêm: 2 tệp PDF nhỏ (dưới 1 MB) — 1 tệp đặt tên có dấu cách, ngoặc đơn và dấu & (ví dụ
   "2K15 T3 (4.8) & CN (9.8).pdf"), 1 tệp tên chỉ có chữ/số/gạch nối. Cả 2 tệp đã có sẵn trong seed-files/.
1) Trên hồ sơ (i) — hồ sơ SẴN CÓ chứng chỉ kèm tệp: bấm [Cập nhật năng lực]. Form phải mở ra tại chỗ.
   Nếu bị chuyển sang trang báo không có quyền truy cập thì lỗi còn nguyên, ghi lại rồi đo tiếp các bước sau.
2) Trên hồ sơ (ii): mở form, KHÔNG đính tệp, chỉ sửa Trình độ + Kinh nghiệm chi tiết → [Lưu].
   Đây là lượt đối chứng, phải lưu được.
3) Trên hồ sơ (ii): mở lại form, ở khối "Thêm chứng chỉ mới" đính tệp tên có ký tự đặc biệt, nhập Ghi chú
   cập nhật = "a" → [Lưu]. Đọc nguyên văn thông báo hiện ra.
4) Lặp bước 3 trên hồ sơ (iii) với tệp tên thường.
   ⇒ tổng cộng 3 lượt bấm [Lưu]: 1 lượt không tệp + 2 lượt có tệp, cộng lượt mở form ở bước 1.
5) Sau MỖI lượt lưu: tải lại trang, mở lại tab "Năng lực", đọc dòng "Chứng chỉ chi tiết" — phải thấy TÊN TỆP
   vừa đính, không được là một chuỗi ký tự kỹ thuật.
6) Sau MỖI lượt lưu: bấm lại [Cập nhật năng lực] trên chính hồ sơ vừa lưu — form phải mở lại được, và khối
   "Chứng chỉ hiện có" phải liệt kê tệp vừa đính đúng tên, xem/tải được.
7) Đo bằng đường thứ hai: xem phản hồi máy chủ của chính lượt bấm lưu đó, đọc lại bản ghi hồ sơ qua máy chủ
   để so với những gì màn hình đang hiện, và thử mở chính tệp vừa đính qua đường đọc tệp của máy chủ.
✅ PASS khi: đủ 3/3 lượt lưu đều báo thành công, VÀ sau khi tải lại trang thì tệp vừa đính hiện ĐÚNG TÊN ở
   dòng "Chứng chỉ chi tiết" và trong khối "Chứng chỉ hiện có", VÀ mở lại được form [Cập nhật năng lực] trên
   hồ sơ đã có tệp chứng chỉ — cả hồ sơ (i) sẵn có tệp lẫn 2 hồ sơ vừa đính, VÀ phản hồi máy chủ của cả 3 lượt
   đều là thành công và tệp vừa đính đọc lại được, VÀ mỗi lượt chỉ sinh đúng 1 thông báo (đếm theo mốc giờ
   khác nhau, không đếm số phần tử).
❌ FAIL nếu: bất kỳ lượt nào báo lỗi hoặc máy chủ trả lỗi — kể cả khi chỉ hỏng ở 1 trong 2 kiểu tên tệp, hoặc
   chỉ hỏng ở 1 trong các hồ sơ. Cũng FAIL nếu báo thành công nhưng tải lại trang thì tệp không hiện đúng tên,
   hoặc hiện ra một chuỗi ký tự kỹ thuật thay cho tên tệp. Cũng FAIL nếu sau khi hồ sơ đã có tệp chứng chỉ thì
   bấm [Cập nhật năng lực] bị chuyển sang trang báo không có quyền truy cập, khiến hồ sơ đó không còn sửa
   năng lực được nữa.
⚠️ Đừng chấm Fail vì nhãn nút là "Lưu" thay vì "Đồng ý", vì form là inline thay vì hộp thoại, hay vì câu
   chữ cụ thể của thông báo THÀNH CÔNG — đặc tả srs-fr-04-chuyen-gia-tvv.md:432 không chốt những thứ đó.
   Cũng đừng chấm Fail khi hệ thống từ chối ĐÚNG theo :425-:429 (tệp quá 10MB, tổng quá 50MB, có mã độc,
   khác đơn vị, hồ sơ đã vô hiệu hóa) — đó là hành vi đúng.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy lượt lưu báo thành công: lần đo 07/08 cả 4 lượt có tệp đều báo thành
   công mà vẫn chưa đạt. Phép đo quyết định là 2 việc SAU khi lưu — tệp có hiện đúng TÊN không, và có mở lại
   được form trên hồ sơ đã có tệp không. Cũng đừng kết luận từ việc bước tải tệp lên trả về thành công:
   bước đó vốn đã chạy được, chỗ hỏng nằm sau nó.
⚠️ Hồ sơ đang ở "Yêu cầu bổ sung" sau khi lưu năng lực sẽ tự chuyển sang "Đang thẩm định" — đó là hành vi
   ĐÚNG theo srs-fr-04-chuyen-gia-tvv.md:405, không phải lỗi.
⚠️ Kiểm thêm: lượt lưu hỏng (nếu còn) không được để lại tệp thừa trên hồ sơ. Cách đọc: mở tab "Hồ sơ" →
   khối "File đính kèm", đếm số tệp trước và sau lượt bấm.
```

---

## BUG-TVV-CNDSMLTVV-01 [REOPEN] — Công khai hàng loạt tư vấn viên: hồ sơ bị máy chủ từ chối vẫn báo "Đã công khai … thành công", người dùng không biết hồ sơ nào không đạt và vì sao

> **Re-test:** 2026-08-07 01:03:00 — 🔁 **REOPEN, triệu chứng ĐÃ ĐỔI**. Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng **`HTPLDN · V1.0.10`** / bó mã `assets/index-B2W2Krcs.js` / `GET /` last-modified 07/08/2026 00:39:54 giờ VN · tài khoản `cbnv_tw_02` (CB_NV_TW, cấp TW, đơn vị Cục Bổ trợ tư pháp — trùng khít vai trò + cấp + đơn vị đọc được trên ảnh đối tác) · dữ liệu `CG-QLND38-UAT` (Chuyên gia) + `TVV-BTP-TW-0016` (Tư vấn viên **có** số thẻ `THN-TW-2026-016`, QA tự dựng) + `TVV-SEED-0001` (Tư vấn viên **không** số thẻ) · **N = 3 hồ sơ × M = 3 dạng × 2 cỡ lô = 4 lượt bấm công khai thật** + 1 lượt hủy công khai · **phép đo quyết định — tải lại trang rồi đếm:** lượt riêng hồ sơ thiếu số thẻ **0/1** công khai · lượt lô 2 hồ sơ **1/2** công khai, trong khi **cả 4/4 lượt giao diện đều báo *"Đã công khai tư vấn viên thành công"*** · **ĐÃ HẾT LỖI:** một hồ sơ bị từ chối **không còn kéo đổ cả lô**, và lý do từ chối máy chủ trả về đã là câu nghiệp vụ đọc được · **CÒN LỖI:** giao diện bỏ qua danh sách kết quả, báo thành công cả khi có hồ sơ bị từ chối · **dữ liệu:** mọi hồ sơ bị đổi cờ công khai **đã hoàn nguyên**. **Kết quả chỉ có hiệu lực cho env + bản dựng nêu trên.**

### Mô tả

Ở màn *Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia*, tab **Đang hoạt động**: tích chọn hồ sơ rồi bấm
**[Công khai lên Cổng PLQG]**, nhập mô tả và xác nhận. Phiếu có **2 vế**: (1) giao diện nhập mô tả + câu xác
nhận theo số hồ sơ đã chọn; (2) kết quả nghiệp vụ — lưu mô tả, đặt cờ công khai, chuyển trạng thái công khai,
ghi thời điểm.

- **Vế (1) — không còn tái hiện** (đã đúng từ lượt đo 06/08). Cửa sổ *"Công khai hàng loạt lên Cổng PLQG"*
  mở bình thường, câu xác nhận báo đúng số hồ sơ đã tích.
- **Vế (2) — CÒN LỖI, đây là chỗ Reopen, nhưng đã thu hẹp.** Hệ thống vẫn báo *"Đã công khai tư vấn viên
  thành công"* **kể cả khi hồ sơ bị máy chủ từ chối**. Người dùng **không được cho biết hồ sơ nào không đạt
  và vì sao**, nên tưởng đã công khai xong trong khi thực tế chưa.

**Hồ sơ loại *Tư vấn viên* thiếu Số thẻ hành nghề bị từ chối là ĐÚNG ĐẶC TẢ** —
`srs-fr-04-chuyen-gia-tvv.md:1507` (*"Số thẻ hành nghề | ô văn bản | **Bắt buộc nếu Loại = Tư vấn viên**
(theo NĐ 77/2008 Đ.20)"*). **Bug này KHÔNG đòi công khai được hồ sơ đó**; bug nằm ở chỗ **báo thành công sai
sự thật** và **không nói rõ hồ sơ nào trượt**.

### Các bước tái hiện

1. Đăng nhập `cbnv_tw_02` — vai trò **Cán bộ Nghiệp vụ Trung ương (CB_NV_TW)**, đơn vị *Cục Bổ trợ tư pháp -
   Bộ Tư pháp*. Vai trò này có quyền công khai theo `srs-fr-04-chuyen-gia-tvv.md:647` và `:1420`.
2. Vào *Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia*, tab **Đang hoạt động**.
3. Tích **1 hồ sơ loại *Tư vấn viên* KHÔNG có Số thẻ hành nghề** đang *Đang hoạt động* + *Chưa công khai*
   (lần đo này: `TVV-SEED-0001`).
4. Bấm **[Công khai lên Cổng PLQG]** → nhập mô tả hợp lệ → bấm **[Công khai]**.
5. Đọc nguyên văn câu thông báo, rồi **tải lại trang** và đọc cột *Công khai* của đúng hồ sơ đó.
6. Lặp bước 3-5 nhưng tích **cùng lúc 2 hồ sơ**: 1 hồ sơ *Tư vấn viên* **có** số thẻ (`TVV-BTP-TW-0016`)
   + 1 hồ sơ **không** có số thẻ (`TVV-SEED-0001`) → đếm **mấy trên 2** hồ sơ thực sự chuyển *Công khai*.
7. Đo bằng đường thứ hai: đọc **từng hồ sơ trong danh sách kết quả** của phản hồi máy chủ, không chỉ nhìn
   trạng thái chung; rồi đọc lại từng bản ghi qua máy chủ để so với màn hình.

### Kết quả mong đợi

- Khi một hồ sơ trong lô không đủ điều kiện, hệ thống phải **cho người dùng biết hồ sơ nào không đạt và vì
  sao** — `:681` (`ERR-CK-01`) và `:682` (`ERR-CK-02`) đều quy định thông báo từ chối có nội dung nghiệp vụ
  rõ ràng.
- Thông báo thành công **chỉ được hiện khi thao tác thật sự đã có hiệu lực**, và phải phản ánh đúng đối
  tượng đã công khai — `srs-v3.5.md:6772` (mẫu *"Đã công khai {ten_doi_tuong} '{ma_hoac_ten}' lên Cổng Pháp
  luật Quốc gia."*).
- Với hồ sơ đủ điều kiện, phải **lưu mô tả công khai, đặt cờ công khai, chuyển trạng thái công khai và ghi
  thời điểm đăng tải** cho **đủ các hồ sơ đã chọn** — `:664`, `:666`, `:685`, `:689` (AC1), `:1464`.

### Kết quả thực tế

**1. Báo thành công trong khi không hồ sơ nào được công khai (lô 1 hồ sơ).** Tích riêng `TVV-SEED-0001`
(*Đang hoạt động* + *Chưa công khai*): **1 yêu cầu ghi / 1 thông báo**, nguyên văn *"Đã công khai tư vấn
viên thành công"*, không có thông báo lỗi nào. **Tải lại trang: 0/1 hồ sơ được công khai.**

**2. Báo thành công trong khi chỉ 1 trên 2 hồ sơ được công khai (lô 2 hồ sơ).** Tích cùng lúc
`TVV-BTP-TW-0016` (có số thẻ) + `TVV-SEED-0001` (không số thẻ): **1 yêu cầu ghi / 1 thông báo**, cũng là
*"Đã công khai tư vấn viên thành công"*. **Tải lại trang: 1/2 hồ sơ được công khai** — hồ sơ thiếu số thẻ
vẫn *Chưa công khai*, và **không có bất kỳ dấu hiệu nào trên màn hình cho biết nó đã trượt**.

**3. Máy chủ CÓ báo thất bại kèm lý do rõ ràng — giao diện bỏ qua.** Vỏ ngoài phản hồi là *thành công*
(HTTP 200, `success: true`) nhưng bên trong liệt kê từng hồ sơ:

```json
{"success":true,"data":{"results":[
  {"id":"aaaa1707-…-0d01","success":true,"laCongKhai":true},
  {"id":"5eed0003-…-001","success":false,
   "error":"Tư vấn viên chưa có Số thẻ hành nghề nên chưa thể công khai. Vui lòng bổ sung Số thẻ hành nghề trước."}
]},"meta":null}
```

Giao diện chỉ nhìn trạng thái chung nên luôn báo thành công. **Câu lý do đã đủ rõ để hiển thị thẳng cho
người dùng** — chỉ thiếu bước đưa nó ra màn hình.

**4. Những phần ĐÃ HẾT LỖI so với lượt đo 06/08** (ghi để dev không sửa nhầm chỗ và không làm hỏng lại):

| Vế | Lượt 06/08 | Lượt 07/08 (bản dựng V1.0.10) |
|---|---|---|
| Cửa sổ nhập mô tả + câu xác nhận theo số hồ sơ đã chọn | ✅ đã đúng | ✅ vẫn đúng — 4/4 lượt, câu xác nhận báo đúng 1 và 2 |
| Một hồ sơ bị từ chối kéo đổ cả lô | 🔴 0/2 công khai | ✅ **đã hết** — 1/2, hồ sơ hợp lệ cùng lô đi qua bình thường |
| Nội dung lý do từ chối máy chủ trả về | 🔴 lộ nguyên văn ràng buộc cơ sở dữ liệu | ✅ **đã hết** — câu nghiệp vụ đọc được |
| Giao diện báo kết quả | 🔴 báo thành công sai | 🔴 **còn nguyên** |

**5. Hồ sơ đủ điều kiện ra đủ 4 kết cục.** `TVV-BTP-TW-0016` sau lượt lô 2 hồ sơ: mô tả đúng nguyên văn vừa
nhập · cờ công khai bật · nhóm *Thông tin công khai* hiện ra ở màn chi tiết (`:1564`) · *Thời gian đăng tải
07/08/2026* bám đúng thời điểm bấm. `CG-QLND38-UAT` (Chuyên gia) cũng đủ 4 kết cục.

**6. Lượt bấm hỏng KHÔNG ghi đè mô tả công khai cũ** — `TVV-SEED-0001` qua 2 lượt bị từ chối vẫn giữ nguyên
mô tả công khai cũ và số hiệu phiên bản bản ghi không nhích. Đây là phần đạt, không phải lỗi.

**7. Ghi nhận phụ, không kéo verdict** (đối tác không nêu): câu thông báo thành công *"Đã công khai tư vấn
viên thành công"* thiếu mã/tên đối tượng so với mẫu chuẩn `srs-v3.5.md:6772`.

### Bằng chứng

**1. Ảnh chụp — lượt đo R3 2026-08-07 (bản dựng V1.0.10)**

![BUG-TVV-CNDSMLTVV-01 — LỖI: lô 2 hồ sơ, thông báo "Đã công khai tư vấn viên thành công" trong khi thực tế chỉ 1/2 hồ sơ được công khai](image/CNDSMLTVV_01-R3-03-luot2-lo-2-ho-so-thong-bao.png)
![BUG-TVV-CNDSMLTVV-01 — Sau khi tải lại: bảng đủ cột Mã TVV và cột Công khai, TVV-SEED-0001 vẫn "Chưa công khai" dù đã bị bấm công khai 2 lượt](image/CNDSMLTVV_01-R3-08-ma-tvv-va-cot-cong-khai-day-du.png)
![BUG-TVV-CNDSMLTVV-01 — Hồ sơ đủ điều kiện TVV-BTP-TW-0016: nhóm "Thông tin công khai" hiện đủ mô tả + Thời gian đăng tải 07/08/2026](image/CNDSMLTVV_01-R3-05-V2-chi-tiet-nhom-thong-tin-cong-khai.png)
![BUG-TVV-CNDSMLTVV-01 — Danh sách ngay sau lượt bấm riêng hồ sơ thiếu số thẻ, cửa sổ đã đóng](image/CNDSMLTVV_01-R3-01-luot1-rieng-V3-ngay-sau-bam-modal-da-dong.png)

**2. Ảnh chụp — lượt đo 06/08 (bản dựng V1.0.8, giữ để đối chiếu)**

![BUG-TVV-CNDSMLTVV-01 — Cửa sổ nhập mô tả công khai mở đúng, câu xác nhận báo 1 tư vấn viên đã chọn](image/CNDSMLTVV_01-02-M1-cua-so-nhap-mo-ta-cong-khai-N1.png)
![BUG-TVV-CNDSMLTVV-01 — Bỏ trống mô tả thì bị chặn đúng chỗ, cửa sổ vẫn mở (tình huống ĐÚNG của câu thông báo)](image/CNDSMLTVV_01-03-M3-bo-trong-mo-ta-bi-chan-dung-cho.png)

**3. Số đo đầy đủ lượt R3:**
[`reverify-week-5/F3-devfix-2026-08-07/do/CNDSMLTVV_01.md`](../reverify-week-5/F3-devfix-2026-08-07/do/CNDSMLTVV_01.md)
· chuẩn chấm: [`reverify-week-5/F3-devfix-2026-08-07/chuan/CNDSMLTVV_01.md`](../reverify-week-5/F3-devfix-2026-08-07/chuan/CNDSMLTVV_01.md)
· số đo lượt 06/08: [ketqua-CNDSMLTVV_01.txt](ketqua-CNDSMLTVV_01.txt).

### Cách verify sau khi fix — *CHỈ dùng cho bug **Reopen***

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản cbnv_tw_02 / Test@1234 — vai trò Cán bộ Nghiệp vụ Trung ương, đơn vị Cục Bổ trợ
  tư pháp - Bộ Tư pháp. Màn: Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → tab "Đang hoạt động".
  Dữ liệu phải có sẵn: 3 hồ sơ đang "Đang hoạt động" + "Chưa công khai", đủ 3 biến thể khác nhau —
   (i) loại Chuyên gia (CG-QLND38-UAT);
   (ii) loại Tư vấn viên CÓ Số thẻ hành nghề (TVV-BTP-TW-0016, số thẻ THN-TW-2026-016 — đã dựng sẵn 07/08);
   (iii) loại Tư vấn viên KHÔNG có Số thẻ hành nghề (TVV-SEED-0001) — biến thể quan trọng nhất.
   Hồ sơ nào đang "Công khai" thì dùng chính nút [Hủy công khai] để đưa về "Chưa công khai" trước khi đo.
1) Tích 1 hồ sơ loại (iii) → [Công khai lên Cổng PLQG] → nhập mô tả bất kỳ → xác nhận.
   Đọc NGUYÊN VĂN câu thông báo hiện ra, rồi TẢI LẠI TRANG và đọc cột "Công khai" của đúng hồ sơ đó.
2) Tích CÙNG LÚC 2 hồ sơ: 1 cái loại (ii) + 1 cái loại (iii) → nhập mô tả → xác nhận → tải lại trang →
   đếm xem MẤY TRÊN 2 hồ sơ thực sự chuyển sang "Công khai".
3) Lặp bước 2 nhưng chỉ tích riêng hồ sơ loại (ii) — để biết hồ sơ đó tự nó có công khai được không.
4) Mở màn chi tiết từng hồ sơ vừa thao tác, tab "Hồ sơ", đọc nhóm "Thông tin công khai": phải có đủ
   mô tả vừa nhập + thời gian đăng tải.
5) Đo bằng đường thứ hai: xem phản hồi máy chủ của chính lượt bấm đó — phải đọc từng hồ sơ trong danh
   sách kết quả, không chỉ nhìn trạng thái chung; rồi đọc lại bản ghi để so với màn hình.
✅ PASS khi: (a) với hồ sơ không đủ điều kiện, hệ thống báo TỪ CHỐI rõ hồ sơ nào không đạt và vì sao
   (KHÔNG được báo thành công), VÀ (b) với lô có lẫn hồ sơ hỏng, những hồ sơ hợp lệ còn lại vẫn phải
   được công khai đủ (hoặc hệ thống chặn cả lô nhưng NÓI RÕ là không hồ sơ nào được công khai), VÀ
   (c) mọi hồ sơ báo thành công đều đủ 4 kết cục sau khi tải lại: mô tả đúng nguyên văn · cờ công khai bật ·
   nhóm "Thông tin công khai" hiện ra · thời gian đăng tải bám đúng thời điểm bấm, VÀ (d) số hồ sơ chuyển
   sang "Công khai" sau khi tải lại đúng bằng số hồ sơ mà thông báo nói là đã công khai.
❌ FAIL nếu: báo thành công mà tải lại trang hồ sơ vẫn "Chưa công khai" — kể cả khi chỉ sai 1 hồ sơ trên 2;
   hoặc 1 hồ sơ hỏng vẫn kéo đổ những hồ sơ hợp lệ khác mà người dùng không được báo; hoặc người dùng
   không biết hồ sơ nào không đạt và vì sao; hoặc thời gian đăng tải trống dù cờ công khai đã bật.
⚠️ Đừng chấm Fail vì không thấy phần mềm gọi sang Cổng pháp luật quốc gia, hay vì Cổng chưa hiển thị
   ngay: đặc tả srs-fr-04-chuyen-gia-tvv.md:645 và :686 chốt mô hình KÉO — phần mềm chỉ đặt cờ, Cổng tự
   kéo định kỳ. Cũng đừng chấm Fail vì câu chữ của cửa sổ xác nhận hay nhãn nút, và đừng chấm Fail khi
   hệ thống từ chối ĐÚNG lúc bỏ trống mô tả (:682) hay khi hồ sơ không ở trạng thái cho phép (:681).
⚠️ KHÔNG được đòi hệ thống công khai được hồ sơ loại Tư vấn viên thiếu Số thẻ hành nghề: đặc tả
   srs-fr-04-chuyen-gia-tvv.md:1507 ghi "Bắt buộc nếu Loại = Tư vấn viên" nên việc máy chủ từ chối là
   ĐÚNG. Phần phải sửa là: báo thành công sai sự thật, và không cho người dùng biết hồ sơ nào không đạt.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy cửa sổ nhập mô tả mở ra được — phần đó vốn đã chạy đúng từ lượt đo
   06/08. Cũng đừng kết luận từ thông báo thành công, và đừng kết luận từ trạng thái chung của phản hồi
   máy chủ — hiện nay phản hồi báo "thành công" ở vỏ ngoài trong khi bên trong có hồ sơ thất bại.
   Phép đo quyết định là: TẢI LẠI TRANG rồi ĐẾM số hồ sơ thực sự đã chuyển sang "Công khai".
⚠️ Hai phần ĐÃ ĐẠT ở bản dựng V1.0.10, đừng làm hỏng lại khi sửa tiếp: (1) một hồ sơ bị từ chối KHÔNG còn
   kéo đổ cả lô — hồ sơ hợp lệ cùng lô vẫn được công khai đủ; (2) lý do từ chối máy chủ trả về đã là câu
   nghiệp vụ đọc được, không còn lộ nguyên văn ràng buộc của cơ sở dữ liệu.
⚠️ Biến thể dễ bị bỏ sót: hồ sơ loại Tư vấn viên KHÔNG có Số thẻ hành nghề. Chỉ đo hồ sơ Chuyên gia hoặc
   hồ sơ có số thẻ thì sẽ thấy "chạy được" và bỏ lọt toàn bộ lỗi này.
⚠️ Kiểm thêm sau khi fix: lượt bấm hỏng (nếu còn) không được ghi đè mô tả công khai cũ của hồ sơ.
Ảnh lỗi lần này: image/CNDSMLTVV_01-R3-03-luot2-lo-2-ho-so-thong-bao.png +
   image/CNDSMLTVV_01-R3-08-ma-tvv-va-cot-cong-khai-day-du.png
```

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | https://18.143.165.120.nip.io (env **nội bộ**) |
| OTP login | Lấy từ MailHog của env |
| MailHog | http://18.143.165.120:8025 |
| Tài khoản đo | `cbnv_tw_02` / `Test@1234` — CB_NV_TW, cấp TW |
| Frontend | React + Ant Design v5 · bó mã `assets/index-DIABnbIr.js` |
| Tool test | Chrome DevTools MCP (`--isolated`) + `tools/toast-capture.js` |

### Dữ liệu QA đã seed / thay đổi trên env

| Thao tác | Bản ghi | Trên env |
|---|---|---|
| Tạo mới TVCS | `TVCS-20260806-0003` (`eb16294e-6231-45ce-9c50-fe480228f518`), DN `DN-HNI-0001`, lĩnh vực Thương mại, trạng thái Tiếp nhận | `18.143.165.120.nip.io` (nội bộ) |
| Tạo mới tư liệu pháp lý | `14cef4af-cb15-497b-88d6-8ed3ad22d9e7` — Loại Tài liệu, Lĩnh vực Sở hữu trí tuệ, 3 tệp đính kèm | ↑ |
| Đổi trạng thái tư liệu | `Nháp` → `Đã công khai` (14:33), có nhập mô tả công khai | ↑ |
| Tạo mới 3 phiên tư vấn nhanh | `TVN-20260806-0001` (`21beee47-b17f-4ff1-a1cd-b8ce0ffbb4dd`) · `TVN-20260806-0002` (`f9f1b33a-e6ff-4ff5-b3b6-a8ff2b1a4a7e`) · `TVN-20260806-0003` (`5f3741ec-6f0a-4b3a-9d7f-2c4a9e0b7d15`) — DN `DN-HNI-0001`, lần lượt Mới → Cán bộ trả lời → Hoàn thành | ↑ |
| Tạo mới 3 đánh giá của doanh nghiệp | P1 = 4 sao + nhận xét · P2 = 5 sao + KHÔNG nhận xét · P3 = 3 sao + nhận xét (dựng tiền đề "Hoàn thành + đã có đánh giá") | ↑ |
| Đổi kênh phiên | `TVN-20260806-0003`: `TV_NHANH` → `TV_THU_CONG` (để có biến thể kênh "Thủ công" trùng khít ảnh của đối tác) | ↑ |
| Đổi trạng thái tư vấn viên (QLTVV_02) — **đã khôi phục** | `CG-QLND38-UAT` (`38383838-0000-4000-8000-000000000038`, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp): `Đang hoạt động` → `Vô hiệu hóa` (16:00) → **`Đang hoạt động`** (16:04). Mục đích: dựng dạng "ô Hành động bị ẩn bớt điều khiển" theo `srs-fr-04-chuyen-gia-tvv.md:1455`. Đã đọc lại bảng xác nhận bản ghi về đúng trạng thái cũ | ↑ |
| Tạo mới hồ sơ tư vấn viên (CNHSNLTVV_03) — **giữ lại cho dev tái hiện** | `TVV-BTP-TW-0038` (`7c9107b3-9476-4aba-8225-3765ed848635`) "QA B7 CNHSNLTVV03 Ho So Moi", đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, trạng thái *Mới đăng ký*. Mục đích: hồ sơ QA tự tạo để loại trừ khả năng lỗi chỉ xảy ra trên hồ sơ dev đã đụng vào. Đã xoá sạch 4 bản ghi tệp thừa do các lượt lưu hỏng sinh ra | ↑ |
| Cập nhật năng lực (CNHSNLTVV_03) — **đã hoàn nguyên** | `TVV-BTP-TW-0002` (`98cfd963-3cd3-4c8a-bfa9-625460824d6d`): 7 lượt bấm [Lưu] (4 lượt ghi thật) đổi Trình độ / Số năm / Chuyên ngành / Số thẻ / Kinh nghiệm / Lĩnh vực / Bằng cấp / Chứng chỉ. **Đã trả về đúng mốc gốc** (Cử nhân · số năm trống · `STHN-QA-28` · 1 bằng cấp · 1 chứng chỉ nơi cấp "Bo Tu phap" · 4 lĩnh vực Thương mại/Thuế/Lao động/Đất đai · chỉ còn tệp `the-hanh-nghe-qa.pdf`), đã xoá 2 bản ghi tệp thừa; chỉ số hiệu phiên bản là tăng (22 → 27). Đọc lại bằng cả giao diện lẫn máy chủ để xác nhận | ↑ |
| Cờ công khai (CNDSMLTVV_01) — **đã hoàn nguyên** | `CG-QLND38-UAT` (`38383838-…-038`) và `TVV-STP-AG-0001` (`4c1d3aab-db59-40f8-9a58-b8637c42d8ab`): `Chưa công khai` → `Công khai` trong lúc đo → **đã gỡ về `Chưa công khai`** bằng chính luồng [Hủy công khai] (`srs-fr-04-chuyen-gia-tvv.md:1465`), làm từng hồ sơ một. Đã tải lại trang đọc lại: cả hai `Chưa công khai`, thời gian đăng tải rỗng, bảng trùng khít trước khi đo. **Còn lưu lại:** chuỗi mô tả công khai QA nhập vẫn nằm trong 2 bản ghi — đúng đặc tả `:1406` (*"mô tả + file vẫn được giữ lại để tái công khai sau"*), không gỡ được qua giao diện | ↑ |
| Không đổi gì (CNDSMLTVV_01) | `TVV-SEED-0001` và `DDD-TVV-022`: mọi lượt công khai đều bị máy chủ từ chối nên dữ liệu giữ nguyên. `TVV-BTP-TW-0002` và `DDD-TVV-021` không đụng tới | ↑ |

Không đụng bản ghi nào có sẵn của người khác; **không dùng lại `TVN-20260727-0002`** của lượt đo cũ;
không thao tác trên env nghiệm thu của đối tác. Bản ghi `CG-QLND38-UAT` đã trả về đúng trạng thái ban đầu
(cả trạng thái hoạt động lẫn cờ công khai).

---

## Report cuối đợt — lô B7 (5/5 case)

> Kết quả từng case + verdict đã nằm ở §**Tổng hợp** đầu file. Mục dưới đây trả lời 3 câu còn lại:
> lỗi ngoài phạm vi · dữ liệu đã đụng vào · case chưa chốt được.

### ① Lỗi phát hiện ngoài phạm vi 5 case

**Không mở dòng bảng mới nào.** Cả 5 case đều không sinh phiếu lỗi mới trong luồng. Hai quan sát nằm ngoài
vế đối tác nêu, chỉ ghi nhận để phía dự án tự kiểm — **đã báo lại phiên chính, không tự ghi vào bảng**:

| # | Quan sát | Căn cứ đặc tả | Vì sao không mở phiếu |
|---|---|---|---|
| 1 | Ảnh của đối tác (env nghiệm thu, 25/07) có tư vấn viên hiện điểm đánh giá **`8.3/5`** — vượt thang 1–5 | `BR-CALC-06` (`srs-fr-04-chuyen-gia-tvv.md:2538`) · `CHECK BETWEEN 1.0 AND 5.0` (:2035) | Đối tác không nêu vế này; đo lại **không tái hiện** (giá trị đo được 4.1 và 3.3) ⇒ nghi là dữ liệu của riêng env nghiệm thu |
| 2 | Hồ sơ `DDD-TVV-022` có **cờ công khai bật** nhưng **thời gian đăng tải rỗng** | `BR-PUBLIC-03` (`srs-v3.5.md:5697` — *"Auto fill = thời điểm cuối cùng set cong_khai = 1"*) | Dữ liệu **có sẵn từ trước**, không do lượt đo 06/08 sinh ra; đối tác không nêu vế này |

### ② Dữ liệu đã seed / thay đổi trên env

Chi tiết từng bản ghi ở §**Phụ lục → Dữ liệu QA đã seed / thay đổi trên env**. Tóm tắt:

| Nhóm | Bản ghi | Còn trên env hay đã hoàn nguyên |
|---|---|---|
| Tạo mới, **giữ lại** | 1 vụ tư vấn chuyên sâu `TVCS-20260806-0003` · 1 tư liệu pháp lý · 3 phiên tư vấn nhanh `TVN-20260806-0001…0003` + 3 đánh giá doanh nghiệp · 1 hồ sơ tư vấn viên `TVV-BTP-TW-0038` | **Giữ lại** — làm tiền đề cho dev tái hiện 2 bug đang Reopen |
| Đổi trạng thái, **đã hoàn nguyên** | `CG-QLND38-UAT`: trạng thái hoạt động (QLTVV_02) **và** cờ công khai (CNDSMLTVV_01) · `TVV-STP-AG-0001`: cờ công khai · `TVV-BTP-TW-0002`: dữ liệu năng lực (CNHSNLTVV_03) | **Đã trả về đúng nguyên trạng**, đọc lại bằng cả giao diện lẫn máy chủ sau khi tải lại trang |
| Không đụng tới | `TVV-SEED-0001` · `DDD-TVV-021` · `DDD-TVV-022` · mọi bản ghi của người khác · toàn bộ env nghiệm thu của đối tác | — |

**Vết còn lại không gỡ được qua giao diện:** chuỗi mô tả công khai QA nhập vẫn nằm trong 2 bản ghi
`CG-QLND38-UAT` và `TVV-STP-AG-0001` — đúng đặc tả `srs-fr-04-chuyen-gia-tvv.md:1406` (*"mô tả + file vẫn
được giữ lại để tái công khai sau"*), không phải sót dọn dẹp.

### ③ Case chưa chốt được × vì sao × cần ai làm gì

| Case (dòng bảng) | Trạng thái | Vì sao chưa chốt | Cần ai làm gì |
|---|---|---|---|
| **QLTVV_02** (dòng 32) | ⚠️ Cần BA | 4/5 vế đã hết lỗi. Vế còn lại — **thứ tự sắp xếp mặc định** của danh sách — khác kỳ vọng đối tác nhưng **đặc tả `SCR-IV-01` im lặng** về thứ tự mặc định ⇒ không có căn cứ chấm đúng/sai | **BA** trả lời câu hỏi ở [cau-hoi-BA.md](cau-hoi-BA.md) §QLTVV_02. BA chốt xong thì QA đo lại 1 lượt là khép được |
| **CNHSNLTVV_03** (dòng 36) | 🔁 Reopen | Lưu năng lực tư vấn viên **có đính tệp chứng chỉ mới** vẫn hỏng 3/3 lượt với đúng câu đối tác báo; lượt không đính tệp thì chạy được | **Dev** sửa theo khối `CÁCH VERIFY sau Dev fix` trong entry `BUG-TVV-CNHSNLTVV-03`. Tiền đề đã dựng sẵn (`TVV-BTP-TW-0038` + tệp mẫu trong `seed-files/`) |
| **CNDSMLTVV_01** (dòng 37) | 🔁 Reopen | **Triệu chứng đã đổi (bản dựng V1.0.10).** Đã hết: cửa sổ nhập mô tả đúng · một hồ sơ bị từ chối không còn kéo đổ cả lô · lý do từ chối máy chủ trả về đã đọc được. Còn lỗi: giao diện vẫn báo *"Đã công khai tư vấn viên thành công"* khi có hồ sơ bị từ chối — riêng 1 hồ sơ thiếu số thẻ ra 0/1, lô 2 hồ sơ ra 1/2 | **Dev** sửa theo khối `CÁCH VERIFY sau Dev fix` trong entry `BUG-TVV-CNDSMLTVV-01`: đọc từng hồ sơ trong danh sách kết quả rồi báo rõ hồ sơ nào không đạt và vì sao. Biến thể bắt buộc đo lại: hồ sơ loại *Tư vấn viên* **không có Số thẻ hành nghề** (`TVV-SEED-0001`) |
| QLTLPLCVV_17 (dòng 300) · QLKCHTV_37 (dòng 305) | ✅ Đã chốt | — | — |

**Hiệu lực chung:** cả 5 case đo trên **env nội bộ** + bản dựng ghi ở đầu file. Khi bản dựng này lên env
nghiệm thu `htpldn-uat.ospgroup.vn` thì phải xác nhận lại — đừng để người đọc hiểu là đối tác mở lên sẽ hết lỗi.

---

*Bug report generated: 2026-08-06 18:45:00 | QA via Claude Code · flow `flows/04-verify-bug-dev-fix-khong-ho-so.md`*
