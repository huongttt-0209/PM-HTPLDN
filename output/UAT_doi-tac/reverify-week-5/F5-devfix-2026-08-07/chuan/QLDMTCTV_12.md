# Chuẩn chấm đã khóa — QLDMTCTV_12 (dòng 149, tab "bug")

> **Giai đoạn A — chỉ đọc đặc tả + ảnh đối tác. KHÔNG mở browser, KHÔNG curl, KHÔNG đo web.**
> **Nguồn đặc tả duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.
> Mọi số dòng dưới đây **đã tự mở file đọc lại trong lượt này (2026-08-07)** — không bê từ phiếu UAT / thư BA /
> báo cáo đợt cũ. Bản `input/srs-update-2026-5-5/` **không được mở** để lấy số dòng.

---

## 1. Nguyên văn phiếu đối tác

- **Mô tả:** `Kiểm tra cửa số Cập nhật trạng thái hoạt động của Tổ chức tư vấn`
- **Điều kiện:** `1. Đăng nhập tài khoản`
- **Các bước:** `1. Chọn menu "Mạng lưới tư vấn viên" => "Tổ chức tư vấn"` · `2. Nhấn Xem chi tiết` · `3. Cập nhật trạng thái`
- **Kết quả mong đợi (nguyên văn):**
  ```
  - Hệ thống mở cửa sổ yêu cầu nhập:
  + Trạng thái mới (danh sách chọn, chỉ hiển thị các trạng thái chuyển được theo máy trạng thái: Đang hoạt động ⟷ Tạm dừng,
    Đang hoạt động hoặc Tạm dừng → Vô hiệu hóa, Vô hiệu hóa → Đang hoạt động).
  + Lý do thay đổi (bắt buộc, tối thiểu 10 ký tự, tối đa 5.000 ký tự).
  ```
- **Trạng thái:** Fail · **Dopai:** N/R · **TKM phản hồi lần 1:** `Màn hình không có nút chức năng` · **Trạng thái dev fix:** Fixed

---

## 2. Ảnh bằng chứng đối tác — đã mở đọc full-res

**File:** [`partner-evidence/QLDMTCTV_12.jpg`](../partner-evidence/QLDMTCTV_12.jpg) (1 ảnh, chụp toàn màn hình Windows).

**Nhìn thấy gì:**

| Hạng mục | Đọc được trên ảnh |
|---|---|
| URL | `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/to-chuc/d6434545-b76b-47ae-8be7-8bceea2d01a7` |
| Đường dẫn điều hướng | `Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Chi tiết` |
| Màn hình | **Chi tiết Tổ chức tư vấn** = SCR-IV-NEW-03 (khớp `srs-fr-04-chuyen-gia-tvv.md:1703` `/chuyen-gia-tvv/to-chuc/:id`) |
| Bản ghi | Tên **“Test thêm mới tổ chức địa phương”** · Mã **`TC-STP-HN-0001`** · Loại hình **Khác** · Người đại diện **TKM** |
| Trạng thái bản ghi | Badge xanh lá **“Đang hoạt động”** (= `HOAT_DONG`) |
| 🔴 Số TVV liên kết | **3** (ô “Số TVV liên kết” = 3) |
| 🔴 Vai trò đang đăng nhập | Góc phải: **`BTP · TW`** + **`Quản trị viên`** + **`QTHT`** ⇒ **Quản trị hệ thống, cấp TW** |
| 🔴 Thẻ “Thao tác” | **RỖNG HOÀN TOÀN** — không có nút nào (không Sửa, không Trình phê duyệt, không Cập nhật trạng thái, không Công khai) |
| Sidebar | `Mạng lưới Tư vấn viên` đang mở, mục **`Tổ chức tư vấn`** được tô đậm |
| Tab hiển thị | Chỉ thấy thẻ “Thông tin tổ chức”; không thấy dải tab (Thông tin / Tư vấn viên liên kết / Lịch sử) trong khung ảnh |
| Bản dựng | Sidebar chân trang ghi **`HTPLDN · V1.0.2`** |
| Mốc giờ máy | **08:47 AM 2026-07-31** (đồng hồ Windows) |

**Neo tái hiện lấy từ ảnh (chỉ những neo cần):**
`env = htpldn-uat.ospgroup.vn` · `màn = /chuyen-gia-tvv/to-chuc/:id` · `bản ghi = TC-STP-HN-0001 (uuid d6434545-b76b-47ae-8be7-8bceea2d01a7)` ·
`trạng thái = Đang hoạt động` · `đơn vị chủ bản ghi = STP-HN (suy từ mã, xem :2210)` · `vai trò đo = QTHT / BTP·TW`.

**🔴 Kết luận đọc ảnh (quyết định cách chấm cả case):** ảnh chứng minh **thẻ Thao tác rỗng**, nhưng **đo bằng QTHT ở
đơn vị BTP·TW trên bản ghi của đơn vị STP-HN**. Theo `:1721` nút “Cập nhật trạng thái” chỉ hiện khi
**Vai trò = Cán bộ Nghiệp vụ *cùng đơn vị***. Ảnh vì thế **lệch 2 chiều cùng lúc** (sai vai trò + khác đơn vị) ⇒
**không đủ căn cứ kết luận “màn hình không có nút chức năng”**, cũng **không đủ căn cứ bác bỏ**. Giai đoạn B phải
đo lại bằng **CB NV cùng đơn vị với bản ghi**; nếu đo bằng QTHT thì thẻ Thao tác rỗng là **đúng đặc tả**, không phải bug.

---

## 3. Bảng dòng khóa Cn

> `C3` của phiếu bị **tách 2** vì đặc tả cover 2 tầng khác nhau: tập giá trị hợp lệ (có quy định) và việc **lọc theo
> trạng thái hiện tại trên giao diện** (im lặng ở màn Tổ chức tư vấn). Không tách sẽ hoặc Fail oan hoặc Pass oan.

| # | Expected đối tác | SRS (file:LINE) | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|
| **C1** | Từ danh sách → Xem chi tiết → **có đường vào chức năng “Cập nhật trạng thái”** (chính chỗ TKM báo “Màn hình không có nút chức năng”) | `srs-fr-04-chuyen-gia-tvv.md:1721` (nút SCR-IV-NEW-03) · `:970` (Màn hình FR-IV-NEW-02) · `:1705` (quyền truy cập màn) · `:974`+`:976` (tác nhân + precondition) | **MATCH** | **TEST** | UI: đăng nhập **CB NV cùng đơn vị bản ghi** → `/chuyen-gia-tvv/to-chuc` → mở chi tiết bản ghi *Đang hoạt động* → tìm chức năng “Cập nhật trạng thái”. **Đối chứng độc lập:** đường thứ 2 ở màn danh sách — dropdown `“…”` của đúng dòng đó (`:1645`) |
| **C2** | Hệ thống mở **cửa sổ** yêu cầu nhập, trong đó có trường **Trạng thái mới** | `:1721` (“mở **hộp thoại** chọn trạng thái mới … + lý do”) · `:983` (`trang_thai_moi` bắt buộc) · `:1399` (mẫu hộp thoại xác nhận) | **MATCH** (riêng **dạng widget** “danh sách chọn”: **GAP**) | **TEST** | Bấm chức năng → phải mở **một bề mặt nhập riêng** cho phép chọn trạng thái mới. **CẤM** Fail vì là Drawer thay vì Modal, hay radio thay vì dropdown — xem §7 |
| **C3a** | Tập trạng thái đích **nằm trong** `Đang hoạt động / Tạm dừng / Vô hiệu hóa` (không lẫn trạng thái ngoài luồng) | `:983` (`HOAT_DONG / TAM_DUNG / VO_HIEU_HOA (theo SM-TCTV)`) · `:1721` · `:2392`–`:2396` (bảng chuyển trạng thái SM-TCTV) | **MATCH** | **TEST** | Đọc **toàn bộ** tùy chọn thật của hộp thoại bằng `innerText` + lọc phần tử đang hiển thị. FAIL nếu lẫn `Mới đăng ký` / `Chờ phê duyệt` / `Đã từ chối` |
| **C3b** | Danh sách **CHỈ hiển thị các trạng thái chuyển được theo máy trạng thái** (lọc theo trạng thái hiện tại của bản ghi) | **IM LẶNG** ở màn Tổ chức tư vấn: `:1721` chỉ liệt kê phẳng “(Tạm dừng / Khôi phục / Vô hiệu hóa)”, không nói lọc; đặc tả chỉ đặt **chốt phía xử lý** `:991` + báo lỗi `:1014` `ERR-TT-TC-01`. **Màn Tư vấn viên (khác màn) lại quy định lọc rõ:** `:1554` | **GAP** | **BA** | **Chưa chốt thì KHÔNG chấm.** Vẫn **ghi lại quan sát** (bản ghi *Đang hoạt động* có hiện “Khôi phục” không) để BA có dữ liệu quyết. Nếu BA chốt phải lọc → đo 3 biến thể ở §5 |
| **C4** | **Lý do thay đổi bắt buộc** | `:984` (`ly_do` … Bắt buộc **Y**) · `:1016` (`ERR-TT-TC-03` “Lý do thay đổi là bắt buộc (≥ 10 ký tự)”) · `:1721` · `:2392` (guard “Có lý do ≥ 10 ký”) | **MATCH** | **TEST** | Bỏ trống lý do → xác nhận: hệ thống **phải từ chối + giữ trạng thái cũ**. **Đối chứng độc lập:** tải lại trang đọc badge trạng thái **và** tab “Lịch sử” (`:1731`) — không được có dòng chuyển trạng thái mới |
| **C5** | Lý do **tối thiểu 10 ký tự** | `:984` (`Min 10 ký tự`) · `:1016` · `:2392` · `:1408`/`:1409` (MD-TAM-DUNG / MD-VO-HIEU-HOA: “tối thiểu 10 ký tự”) | **MATCH** | **TEST** | Đo **2 phía biên**: 9 ký tự → phải bị từ chối; **đúng 10 ký tự → phải được nhận** (đây là vế hay bị bỏ). **Đối chứng:** tab “Lịch sử” (`:1731`) phải lưu đúng chuỗi lý do vừa nhập |
| **C6** | Lý do **tối đa 5.000 ký tự** | **IM LẶNG.** `:984` chỉ ghi `Min 10 ký tự`, không có max. `srs-v3.5.md:805` — kiểu `text (long)` **không** kèm max mặc định. Thực thể TO_CHUC_TU_VAN **không có** trường lưu lý do đổi trạng thái (`:2209`–`:2238`); `ly_do_tu_choi` max 2000 (`:2232`) là **trường KHÁC**. Tiền lệ đặt max cho “lý do thay đổi” tồn tại ở nhóm khác: `srs-fr-02-hoi-dap.md:421` (10–500) | **GAP** | **BA** | **Không chấm.** Chỉ **ghi số đo tham chiếu** (ngưỡng chặn thực tế, nếu có) để BA quyết. Không Fail dù dev không chặn ở 5.000, cũng không Fail nếu dev chặn ở mốc khác |

**Vế phụ ghi nhận (KHÔNG kéo verdict, đối tác không nêu):** bố cục — `:1701` ghi “6 nút hành động ở **header**”, app đặt
trong thẻ **“Thao tác”** bên phải. Đặc tả không quy định vị trí đặt nút ⇒ ghi nhận, không Fail.

---

## 4. Trích nguyên văn từng dòng SRS (đã tự mở đọc)

**File `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` (2542 dòng):**

| Dòng | Nguyên văn (cắt ≤300 ký tự) |
|---|---|
| `:966` | `### FR-IV-NEW-02: Cập nhật trạng thái Tổ chức tư vấn `[CR-02][GAP-IV-09]`` |
| `:970` | `**Màn hình:** SCR-IV-NEW-03 (header action button) + SCR-IV-NEW-01 (col_hanh_dong)` |
| `:972` | `**Mô tả:** CB NV chuyển trạng thái Tổ chức tư vấn theo SM-TCTV: HOAT_DONG ⟷ TAM_DUNG, HOAT_DONG/TAM_DUNG → VO_HIEU_HOA, VO_HIEU_HOA → HOAT_DONG (khôi phục).` |
| `:974` | `**Tác nhân:** CB Nghiệp vụ (có quyền Quản lý TC TV)` |
| `:976` | `**Preconditions:** TC TV tồn tại, CB NV cùng đơn vị.` |
| `:983` | `\| 2 \| trang_thai_moi \| text \| Y \| HOAT_DONG / TAM_DUNG / VO_HIEU_HOA (theo SM-TCTV) \|` |
| `:984` | `\| 3 \| ly_do \| text (long) \| Y \| Min 10 ký tự \|` |
| `:991` | `\| 2 \| Kiểm tra transition hợp lệ theo SM-TCTV \| SM-TCTV \|` |
| `:992` | `\| 3 \| Nếu VO_HIEU_HOA: kiểm tra **KHÔNG có TVV đang liên kết hoạt động** (TVV_TO_CHUC.trang_thai = 'KICH_HOAT' AND TU_VAN_VIEN.trang_thai = 'HOAT_DONG') \| — \|` |
| `:1014` | `\| E1 \| Transition không hợp lệ \| ERR-TT-TC-01 \| "Không thể chuyển từ {old} sang {new}" \| ERROR \|` |
| `:1015` | `\| E2 \| VO_HIEU_HOA có TVV đang liên kết \| ERR-TT-TC-02 \| "Tổ chức đang có {N} tư vấn viên đang hoạt động liên kết, không thể vô hiệu hóa" \| ERROR \|` |
| `:1016` | `\| E3 \| Thiếu lý do \| ERR-TT-TC-03 \| "Lý do thay đổi là bắt buộc (≥ 10 ký tự)" \| ERROR \|` |
| `:1019` | `- **Given** CB NV chọn TAM_DUNG TC TV **When** nhập lý do **Then** TC TV → TAM_DUNG` |
| `:1399` | `> **Quy ước UI:** Mọi hộp thoại xác nhận (confirm modal) trong section này dùng template tiêu chuẩn: tiêu đề + nội dung + nút "Xác nhận" (primary) + nút "Hủy" (secondary). …` |
| `:1408` | `\| MD-TAM-DUNG \| Xác nhận tạm dừng? \| **{tên}** sẽ bị tạm dừng và không thể nhận phân công vụ việc mới. Bạn có thể kích hoạt lại bất kỳ lúc nào. Vui lòng nhập lý do (tối thiểu 10 ký tự). \| Tạm dừng \|` |
| `:1409` | `\| MD-VO-HIEU-HOA \| Xác nhận vô hiệu hóa? \| **{tên}** sẽ bị vô hiệu hóa; nếu đang công khai thì chuyển sang Hủy công khai … Vui lòng nhập lý do (tối thiểu 10 ký tự). \| Vô hiệu hóa \|` |
| 🔴 `:1554` | *(màn **Tư vấn viên** — SCR-IV-03, KHÁC màn của case này)* `\| 7 \| header \| Nút **Cập nhật trạng thái** … **Tùy chọn trạng thái mới hiển thị theo trạng thái hiện tại:** (a) Đang hoạt động → hiển thị "Tạm dừng" + "Vô hiệu hóa"; (b) Tạm dừng → hiển thị "Kích hoạt lại (Đang hoạt động)" + "Vô hiệu hóa"; (c) Vô hiệu hóa → hiển thị "Khôi phục (Đang hoạt động)"; (d) **Chờ kích hoạt tài khoản … → CHỈ hiển thị "Vô hiệu hóa khẩn cấp"** …` |
| `:1609` | `**Loại màn hình:** Danh sách 6 tab + thao tác hàng loạt + nhanh hành động cập nhật trạng thái` |
| `:1613` | `- Cán bộ Nghiệp vụ: thêm/sửa/xóa, xuất Excel, công khai, cập nhật trạng thái (Tổ chức tư vấn thuộc đơn vị)` |
| `:1645` | `\| 24 \| bảng \| Hành động \| nhóm icon + dropdown "..." \| … Dropdown "..." chứa: **"Trình phê duyệt"** …; **"Cập nhật trạng thái"** (Cán bộ Nghiệp vụ cùng đơn vị, trạng thái Đang hoạt động/Tạm dừng/Vô hiệu hóa); **"Xóa"** … \|` |
| `:1701` | `**Loại màn hình:** Trang chi tiết 3 tab + 6 nút hành động ở header` |
| `:1703` | `**Đường dẫn:** `/chuyen-gia-tvv/to-chuc/:id`` |
| `:1705` | `- Cán bộ Nghiệp vụ: xem + sửa + trình phê duyệt + cập nhật trạng thái + công khai (Tổ chức tư vấn thuộc đơn vị)` |
| `:1706` | `- Cán bộ Phê duyệt cùng đơn vị: xem + phê duyệt / từ chối` |
| 🔴 `:1721` | `\| 8 \| header \| Nút **Cập nhật trạng thái** \| nút phụ \| "Cập nhật trạng thái" \| Click → mở hộp thoại chọn trạng thái mới (Tạm dừng / Khôi phục / Vô hiệu hóa) + lý do (≥ 10 ký tự) → áp dụng MD-TAM-DUNG hoặc MD-VO-HIEU-HOA. Vô hiệu hóa: kiểm không có tư vấn viên đang liên kết hoạt động; nếu có → từ chối với cảnh báo "Tổ chức đang có {N} tư vấn viên đang hoạt động liên kết, không thể vô hiệu hóa" \| Vai trò = Cán bộ Nghiệp vụ cùng đơn vị; trạng thái ∈ {Đang hoạt động, Tạm dừng, Vô hiệu hóa} \|` |
| `:1731` | `\| 12 \| tab 3 \| Tab "Lịch sử" \| tab + nội dung \| Nhật ký thao tác (lọc theo Tổ chức tư vấn): Thời gian + Người thực hiện + Hành động ("Tạo mới" / "Cập nhật" / "Trình phê duyệt" / "Phê duyệt" / "Từ chối" / "Tạm dừng" / "Vô hiệu hóa" / "Khôi phục" / "Công khai" / "Hủy công khai" / "Xóa mềm") + Ghi chú/lý do \| — \|` |
| `:1741` | `- **Cập nhật trạng thái** (sau khi đã Hoạt động): chuyển Tạm dừng / Khôi phục / Vô hiệu hóa. Vô hiệu hóa: kiểm không có tư vấn viên đang liên kết hoạt động.` |
| 🔴 `:1848` | *(màn **Người hỗ trợ** — SCR-IV-NHT-03, dùng làm **đối chiếu vai trò**)* `\| 5 \| header \| Nút **Cập nhật trạng thái** … \| Vai trò = Cán bộ Nghiệp vụ cùng đơn vị **HOẶC Quản trị hệ thống** \|` |
| `:2210` | `\| 2 \| ma_to_chuc \| text \| Y \| UNIQUE \| Auto: TC-{DV}-{SEQ} \| Mã tổ chức \| — \|` |
| `:2224` | `\| 16 \| trang_thai \| text \| Y \| CHECK IN ('MOI_DANG_KY','CHO_PHE_DUYET','TU_CHOI','HOAT_DONG','TAM_DUNG','VO_HIEU_HOA') \| 'MOI_DANG_KY' \| Trạng thái lifecycle (SM-TCTV) … \|` |
| `:2232` | `\| 16i \| ly_do_tu_choi \| text_long \| N \| Max 2000 ký, ≥ 10 ký nếu có \| \| **Common Approval Field** — Lý do từ chối \| — \|` |
| `:2392` | `\| HOAT_DONG \| TAM_DUNG \| Cán bộ Nghiệp vụ tạm dừng \| Có lý do ≥ 10 ký \| Audit log \| FR-IV-NEW-02 \|` |
| `:2393` | `\| TAM_DUNG \| HOAT_DONG \| Cán bộ Nghiệp vụ kích hoạt lại \| — \| Audit log \| FR-IV-NEW-02 \|` |
| `:2394` | `\| HOAT_DONG \| VO_HIEU_HOA \| Cán bộ Nghiệp vụ vô hiệu hóa \| **KHÔNG có TVV đang liên kết hoạt động** (COUNT TVV_TO_CHUC WHERE to_chuc_id=@id AND TVV.trang_thai='HOAT_DONG' = 0) \| Gỡ khỏi Cổng nếu đã công khai, audit \| FR-IV-NEW-02 \|` |
| `:2395` | `\| TAM_DUNG \| VO_HIEU_HOA \| Cán bộ Nghiệp vụ vô hiệu hóa \| Same guard \| Gỡ khỏi Cổng, audit \| FR-IV-NEW-02 \|` |
| `:2396` | `\| VO_HIEU_HOA \| HOAT_DONG \| Cán bộ Nghiệp vụ khôi phục \| Quyết định từng trường hợp \| Audit log \| FR-IV-NEW-02 \|` |

**File `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md` (7012 dòng):**

| Dòng | Nguyên văn |
|---|---|
| `:805` | `\| text (long) \| Văn bản dài \| Nội dung chi tiết, mô tả \|` — **không có max mặc định** ⇒ không suy ra được 5.000 |
| `:834` | `- QTHT (Quản trị hệ thống) được xem toàn bộ dữ liệu, không bị giới hạn theo đơn vị` — **phạm vi ĐỌC**, không phải quyền thao tác |
| `:5529` | `\| BR-AUTH-08 \| Chính sách phân quyền dữ liệu theo đơn vị áp dụng cho MỌI bảng có cột `don_vi_id`. Exception: (1) QTHT — không scoped theo đơn vị; … \|` — ngoại lệ **phân quyền dữ liệu**, không cấp quyền hành động |

**File `srs-fr-02-hoi-dap.md`** (chỉ dùng làm tiền lệ đặt max cho trường “lý do thay đổi”, KHÔNG dùng làm căn cứ verdict):

| Dòng | Nguyên văn |
|---|---|
| `:421` | `\| E6 \| Cập nhật thời hạn — ly_do_thay_doi < 10 ký tự hoặc > 500 ký tự \| ERR-TH-02 \| "Lý do thay đổi phải từ 10 đến 500 ký tự" \| ERROR \|` |

---

## 5. Tiền đề tối thiểu phải dựng

**Vai trò (dẫn đặc tả, không nới):**

- 🔴 **Bắt buộc: Cán bộ Nghiệp vụ CÙNG ĐƠN VỊ với bản ghi.** Căn cứ `:974` (Tác nhân), `:976` (Preconditions),
  `:1705` (quyền màn chi tiết), `:1721` (điều kiện hiển thị nút), `:1613`+`:1645` (đường thứ 2 ở màn danh sách).
- 🔴 **KHÔNG dùng `admin` / QTHT ra verdict.** SCR-IV-NEW-03 `:1704`–`:1706` **chỉ** liệt kê Cán bộ Nghiệp vụ và
  Cán bộ Phê duyệt; QTHT **không** có trong danh sách. Ngoại lệ QTHT ở `srs-v3.5.md:834` + `:5529` là **phạm vi đọc
  dữ liệu**, không phải quyền thao tác. Đối chiếu ngược: màn Người hỗ trợ `:1848` **ghi rõ** “HOẶC Quản trị hệ thống”
  — màn Tổ chức tư vấn **cố ý không ghi** ⇒ QTHT thấy thẻ Thao tác rỗng là **hợp đặc tả**.
- Dự phòng khi khóa tài khoản (Rule 7): chỉ đổi sang **sibling cùng vai trò + cùng cấp + cùng đơn vị**. Đổi cấp/đơn vị
  = mất giá trị đối chiếu.

**Dữ liệu (bản ghi Tổ chức tư vấn):**

| Biến thể | Trạng thái cần | Dùng cho | Bắt buộc? |
|---|---|---|---|
| **V1** | **Đang hoạt động** (`HOAT_DONG`), thuộc **đơn vị của tài khoản đo** | C1 · C2 · C3a · C4 · C5 | ✅ **Bắt buộc** — 1 bản ghi là đủ |
| V2 | **Tạm dừng** (`TAM_DUNG`), cùng đơn vị | **Chỉ** khi BA chốt C3b | ⏸ chờ BA |
| V3 | **Vô hiệu hóa** (`VO_HIEU_HOA`), cùng đơn vị | **Chỉ** khi BA chốt C3b | ⏸ chờ BA |

**Vì sao đúng 3 biến thể (không quét toàn enum):** vế C3b của đối tác là **mệnh đề toàn tập** (liệt kê cả 3 nhóm
chuyển đổi), và `:2392`–`:2396` quy định **tập chuyển đổi hợp lệ KHÁC NHAU theo từng trạng thái nguồn**
(`HOAT_DONG` → {Tạm dừng, Vô hiệu hóa} · `TAM_DUNG` → {Đang hoạt động, Vô hiệu hóa} · `VO_HIEU_HOA` → {Đang hoạt động}).
**KHÔNG dựng biến thể `MOI_DANG_KY` / `CHO_PHE_DUYET` / `TU_CHOI`** — `:1721` chốt nút chỉ hiện ở
`{Đang hoạt động, Tạm dừng, Vô hiệu hóa}`, ba trạng thái kia không có nút là **đúng đặc tả**.

**Cảnh báo dữ liệu lấy từ ảnh:** bản ghi trong ảnh (`TC-STP-HN-0001`) có **Số TVV liên kết = 3** ⇒ nhánh
**Vô hiệu hóa sẽ bị chặn hợp lệ** theo `:992` / `:1015` / `:2394`. **Đo nhánh chính bằng “Tạm dừng”**; nếu muốn đo
Vô hiệu hóa thì phải dùng bản ghi **không có TVV liên kết hoạt động**, hoặc coi lượt bị chặn là **PASS của guard**.

**Đường đo (ngắn nhất) + đối chứng độc lập:**

1. **Đường UI chính:** `/chuyen-gia-tvv/to-chuc` → mở chi tiết V1 → chức năng “Cập nhật trạng thái” → hộp thoại →
   chọn “Tạm dừng” + nhập lý do → xác nhận → **tải lại trang** đọc badge trạng thái.
2. **Đối chứng độc lập 1 (đặc tả bảo đảm):** tab **“Lịch sử”** của chính bản ghi (`:1731`) phải có dòng
   *Thời gian + Người thực hiện + Hành động “Tạm dừng” + Ghi chú/lý do* khớp chuỗi vừa nhập → chứng minh lý do
   **thực sự được lưu**, không chỉ hiện toast.
3. **Đối chứng độc lập 2:** màn danh sách 6 tab (`:1609`) — bản ghi phải **đổi tab** sang “Tạm dừng”; và đường vào
   thứ 2 (dropdown `“…”` `:1645`) phải hiện cùng chức năng.

---

## 6. Lệnh grep / Read đã chạy trong lượt này

```bash
# cd Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5
ls -la .                                                  # 18 file + CHANGELOG
grep -n "Tổ chức tư vấn" *.md                             # khoanh vùng: fr-04 là chủ, fr-05/10/14/16 chỉ tham chiếu
grep -n "SCR-" srs-fr-04-chuyen-gia-tvv.md                # định vị SCR-IV-NEW-01/02/03
grep -n "SM-TCTV" srs-fr-04-chuyen-gia-tvv.md             # 966, 972, 983, 991, 1361, 2351…
grep -n "Cập nhật trạng thái" srs-fr-04-chuyen-gia-tvv.md # 1554 (TVV) vs 1721 (TCTV) vs 1848 (NHT)
grep -n "5000\|5\.000" srs-fr-04-chuyen-gia-tvv.md        # KHÔNG có dòng nào cho ly_do đổi trạng thái
grep -n "ly_do" srs-fr-04-chuyen-gia-tvv.md               # 984 (Min 10) · 2232 (ly_do_tu_choi max 2000, field khác)
grep -rn "Lý do thay đổi" *.md                            # 913, 922, 1016 (fr-04) · 421 (fr-02, 10–500)
grep -n "TO_CHUC_TU_VAN" srs-fr-10-quan-tri.md            # chỉ còn dòng danh mục cũ → đã chuyển sang Nhóm IV (:370)
grep -rn "QTHT" srs-v3.5.md | grep -i "toàn bộ|toàn quyền|mọi quyền"   # chỉ :834 (phạm vi ĐỌC)
grep -n "| BR-AUTH-08 " srs-v3.5.md                       # :5529
grep -n "TCTV_\|TOCHUC_" srs-v3.5.md                      # RỖNG → không có bảng quyền action-level riêng cho TCTV
grep -n "to-chuc\|to_chuc" srs-fr-16-api.md               # chỉ API public (mTLS), không có endpoint nội bộ đổi trạng thái
grep -n "trang-thai\|/to-chuc" srs-fr-04-chuyen-gia-tvv.md # 1611, 1665, 1703 (đường dẫn UI)
```

```
Read srs-fr-04-chuyen-gia-tvv.md offset 960  limit 70   # FR-IV-NEW-02 trọn khối (966–1022)
Read srs-fr-04-chuyen-gia-tvv.md offset 1340 limit 80   # §3.0 bảng label SM-TCTV + §3.0b bảng MD-*
Read srs-fr-04-chuyen-gia-tvv.md offset 1607 limit 14   # SCR-IV-NEW-01 quyền truy cập
Read srs-fr-04-chuyen-gia-tvv.md offset 1699 limit 55   # SCR-IV-NEW-03 trọn (header + 3 tab + quy tắc)
Read srs-fr-04-chuyen-gia-tvv.md offset 2204 limit 35   # thực thể TO_CHUC_TU_VAN (2209–2238)
Read srs-fr-04-chuyen-gia-tvv.md offset 2351 limit 60   # SM-TCTV mermaid + bảng trạng thái + bảng chuyển
Read srs-fr-04-chuyen-gia-tvv.md offset 874  limit 50   # FR-IV-12 (TVV) để đối chiếu pattern
Read srs-v3.5.md offset 796 limit 40                    # §3.2.0.2 quy ước kiểu logic + §3.2.0.4 QTHT
Read partner-evidence/QLDMTCTV_12.jpg                   # ảnh full-res
```

**Đã thử từ đồng nghĩa trước khi kết luận im lặng:** “Tổ chức tư vấn”, “tổ chức tư vấn pháp luật”, “cập nhật trạng
thái”, “trạng thái hoạt động”, “máy trạng thái”, “Tạm dừng”, “Vô hiệu hóa”, “Đang hoạt động”, “Lý do thay đổi”,
“ly_do”, “5000 / 5.000”, “text (long)”, `SM-TCTV`, `SCR-`, `TCTV_`. Đã soát dấu thay đổi `[CR-02]` / `[GAP-IV-09]` /
`[BA chốt …]` / `[STT…]` quanh khối FR-IV-NEW-02 + SCR-IV-NEW-03 — **không có** dấu sửa nào bổ sung max ký tự hay
quy tắc lọc dropdown cho Tổ chức tư vấn.

---

## 7. ⚠️ Bẫy chống PASS-oan và FAIL-oan

### 7.1 Chống PASS-oan

1. 🔴 **Thấy có nút “Cập nhật trạng thái” ≠ đã fix.** Vế C1 chỉ là **đường vào**; phải **bấm**, **mở hộp thoại**,
   **submit thật**, rồi **tải lại trang** đọc badge + tab “Lịch sử” (`:1731`). Chốt verdict từ ảnh nút = Pass oan.
2. 🔴 **Đếm tùy chọn dropdown bằng `textContent` = bug ma.** AntD giữ node của select khác + `rc-virtual-list` ẩn
   trong DOM. Phải dùng **`innerText`** và **chỉ lấy phần tử đang hiển thị thật**
   (`getClientRects().length > 0` / `offsetParent !== null`), đọc trên **đúng dropdown vừa mở**.
3. **Toast “thành công” không phải bằng chứng.** Cài bộ bắt thông báo **TRƯỚC khi bấm**, **CẤM lọc trùng**, đếm cả
   số request ghi. Phép đo quyết định = **tải lại trang** + **tab “Lịch sử”** có dòng hành động + đúng chuỗi lý do.
4. **C5 phải đo 2 phía biên.** Chỉ thử 9 ký tự (bị chặn) rồi kết luận đạt là Pass oan — phải chứng minh **đúng 10
   ký tự được nhận** (`:984` là `Min 10`, không phải `>10`). Chuỗi thử **không để khoảng trắng đầu/cuối** (bị trim
   là đổi độ dài thật).
5. **C4 phải kiểm cả hệ quả.** Bỏ trống lý do mà hệ thống chỉ *nháy đỏ ô nhập* nhưng **vẫn đổi trạng thái** ở phía
   sau là FAIL — luôn tải lại trang xác nhận trạng thái **giữ nguyên**.
6. **Mỗi lượt nhập một chuỗi lý do riêng có mốc giờ.** Đọc lại thấy chuỗi của lượt trước = bằng chứng không lưu.
7. **Không suy “dev đã fix” từ ô “Trạng thái dev fix: Fixed”.** Ô đó là chữ của dev. Ghi lại **bản dựng** khi đo
   (ảnh đối tác là `V1.0.2` lúc 2026-07-31) và **tải lại trang** trước khi đo — tab mở lâu vẫn chạy mã cũ.

### 7.2 Chống FAIL-oan

1. 🔴 **KHÔNG Fail vì thẻ “Thao tác” rỗng khi đăng nhập QTHT / admin, hoặc khi bản ghi khác đơn vị.** `:1721` +
   `:1705` chốt nút chỉ hiện với **Cán bộ Nghiệp vụ cùng đơn vị**; QTHT **không** nằm trong danh sách quyền màn này
   (đối chiếu `:1848` màn NHT mới có QTHT). Đây chính là **lỗ của ảnh đối tác**.
2. 🔴 **KHÔNG Fail vì dạng cửa sổ.** Đặc tả `:1721` chỉ nói “mở **hộp thoại**”. Drawer (panel phải) thay Modal
   là **cách hiện**, không có dòng nào quy định. Cũng **không** Fail vì trường trạng thái là **radio** thay vì
   dropdown — `:983` chỉ chốt `trang_thai_moi` bắt buộc + tập giá trị, `:1721` chỉ nói “chọn trạng thái mới”.
3. 🔴 **KHÔNG Fail vì nhãn nút.** App dùng **[Đồng ý]**; `:1408`/`:1409` ghi nhãn primary “Tạm dừng”/“Vô hiệu hóa”,
   `:1399` ghi mẫu “Xác nhận”/“Hủy”. Ba chỗ đã không thống nhất từng chữ ⇒ chỉ đo **có xác nhận được hay không**.
   Theo luật diễn đạt: **mô tả yêu cầu nghiệp vụ, không áp cách hiện thực**.
4. 🔴 **KHÔNG Fail khi “Vô hiệu hóa” bị chặn trên bản ghi có TVV liên kết hoạt động** — đúng `:992` / `:1015` /
   `:2394`. Bản ghi trong ảnh có **3 TVV liên kết**.
5. 🔴 **KHÔNG Fail vì thiếu chặn ở 5.000 ký tự** (C6 = GAP, `:984` chỉ có Min 10; `srs-v3.5.md:805` không đặt max
   cho `text (long)`). Cũng không Fail nếu dev chặn ở mốc khác — ghi số đo, chờ BA.
6. 🔴 **KHÔNG Fail vì dropdown hiện đủ 3 lựa chọn không lọc theo trạng thái hiện tại** (C3b = GAP). `:1721` liệt kê
   phẳng “(Tạm dừng / Khôi phục / Vô hiệu hóa)”; đặc tả chỉ đặt chốt ở **phía xử lý** (`:991`) + mã lỗi
   `ERR-TT-TC-01` (`:1014`) — sự tồn tại của mã lỗi này hàm ý người dùng **có thể** chọn chuyển đổi sai rồi bị chặn.
   Quy định lọc chỉ có ở màn **Tư vấn viên** (`:1554`), là màn khác.
7. **KHÔNG đòi hiện mã lỗi `ERR-TT-TC-01/02/03` trên giao diện.** Mã lỗi là ngôn ngữ dev; yêu cầu nghiệp vụ là
   *hệ thống phải từ chối + nói rõ lý do từ chối + giữ trạng thái cũ*.
8. **KHÔNG Fail vì nút không đặt ở header** (`:1701` nói header, app đặt trong thẻ “Thao tác”) — bố cục không được
   quy định ở mức chấm.
9. **KHÔNG Fail vì không thấy nút ở trạng thái Mới đăng ký / Chờ phê duyệt / Đã từ chối** — đúng `:1721`.
10. **KHÔNG mở rộng case.** Nếu gặp 4xx/5xx ở màn khác / vai trò khác / bộ lọc khác / trường ngoài phạm vi C1–C6:
    **ghi bug candidate**, không điều tra thêm, không kéo verdict của QLDMTCTV_12.

---

## 8. Câu hỏi BA nháp (cho vế GAP)

**Câu 1 — C3b: danh sách trạng thái mới ở màn Tổ chức tư vấn có phải lọc theo trạng thái hiện tại không?**

> Phiếu UAT QLDMTCTV_12 yêu cầu ô *Trạng thái mới* “chỉ hiển thị các trạng thái chuyển được theo máy trạng thái”.
> Đối chiếu bản chốt: `srs-fr-04-chuyen-gia-tvv.md:1721` (màn Chi tiết Tổ chức tư vấn) chỉ ghi “mở hộp thoại chọn
> trạng thái mới (Tạm dừng / Khôi phục / Vô hiệu hóa)” — **không** nói lọc theo trạng thái hiện tại; đặc tả đặt chốt
> ở phía xử lý (`:991`) kèm mã lỗi `ERR-TT-TC-01` “Không thể chuyển từ {old} sang {new}” (`:1014`), hàm ý người dùng
> **có thể** chọn một chuyển đổi không hợp lệ rồi bị hệ thống từ chối.
> Trong khi đó màn **Tư vấn viên** `:1554` lại quy định rất rõ 4 nhánh lọc theo trạng thái hiện tại.
> **Hỏi:** yêu cầu lọc trên giao diện có áp cho Tổ chức tư vấn giống Tư vấn viên không?
> - **Nhánh (a) — CÓ áp:** BA bổ sung câu lọc theo trạng thái vào `:1721` (mẫu như `:1554`); QA sẽ đo 3 biến thể bản
>   ghi (Đang hoạt động / Tạm dừng / Vô hiệu hóa) và **có thể mở bug** nếu giao diện hiện lựa chọn ngoài tập hợp lệ.
> - **Nhánh (b) — KHÔNG áp (giữ chốt phía xử lý):** BA ghi rõ để QA **không** chấm Fail khi hộp thoại hiện đủ 3 lựa
>   chọn, miễn hệ thống từ chối đúng khi chuyển đổi không hợp lệ. QA chỉ giữ vế C3a (tập lựa chọn không được lẫn
>   trạng thái ngoài luồng như *Mới đăng ký* / *Chờ phê duyệt* / *Đã từ chối*).

**Câu 2 — C6: “Lý do thay đổi” có giới hạn tối đa bao nhiêu ký tự?**

> Phiếu UAT yêu cầu *tối đa 5.000 ký tự*. Bản chốt `srs-fr-04-chuyen-gia-tvv.md:984` chỉ ghi
> `ly_do | text (long) | Y | Min 10 ký tự` — **không có max**; `srs-v3.5.md:805` cũng không đặt max mặc định cho kiểu
> `text (long)`; thực thể TO_CHUC_TU_VAN (`:2209`–`:2238`) không có trường lưu lý do đổi trạng thái (chỉ có
> `ly_do_tu_choi` max 2000 ở `:2232` — trường khác, dùng cho luồng từ chối phê duyệt). Nhóm khác lại có tiền lệ đặt
> ngưỡng cho “lý do thay đổi”: `srs-fr-02-hoi-dap.md:421` chốt 10–500 ký tự.
> **Hỏi:** ngưỡng tối đa của *Lý do thay đổi trạng thái Tổ chức tư vấn* là bao nhiêu — **5.000** (như phiếu),
> **2.000** (đồng bộ `ly_do_tu_choi`), **500** (đồng bộ nhóm Hỏi đáp), hay **không giới hạn**?
> Chốt xong xin bổ sung vào `:984` để QA có căn cứ chấm; hiện QA **không chấm** vế này.

**Câu 3 (phụ, chỉ hỏi nếu điều phối thấy cần) — QTHT có được thao tác Cập nhật trạng thái Tổ chức tư vấn không?**

> `SCR-IV-NEW-03` `:1704`–`:1706` chỉ cấp quyền cho **Cán bộ Nghiệp vụ** và **Cán bộ Phê duyệt** cùng đơn vị;
> `:1721` chốt nút chỉ hiện với Cán bộ Nghiệp vụ cùng đơn vị. Trong khi màn **Người hỗ trợ** `:1848` ghi rõ
> “Cán bộ Nghiệp vụ cùng đơn vị **HOẶC Quản trị hệ thống**”. Ngoại lệ QTHT ở `srs-v3.5.md:834` / `:5529` chỉ nói về
> **phạm vi đọc dữ liệu**.
> **Hỏi:** khác biệt giữa 2 màn là **cố ý** (QTHT không thao tác trên Tổ chức tư vấn) hay **bỏ sót khi soạn**?
> Ảnh bằng chứng của đối tác được chụp bằng đúng tài khoản QTHT, nên câu trả lời quyết định việc “thẻ Thao tác rỗng”
> trong ảnh là **đúng đặc tả** hay là **bug**.

---

## 9. Cảnh báo cho agent Giai đoạn B

1. 🔴 **Ảnh đối tác KHÔNG dùng được làm phép đo.** Đo bằng QTHT / BTP·TW trên bản ghi đơn vị STP-HN — lệch cả vai trò
   lẫn đơn vị so với `:1721`. Phải **dựng lại tiền đề §5** rồi đo; **tuyệt đối không** kết luận “không có nút” từ ảnh.
2. 🔴 **Không dùng `admin`/QTHT ra verdict** (§5 + §7.2 mục 1). Nếu môi trường chỉ có QTHT thì **báo điều phối**,
   đừng hạ chuẩn.
3. **Ghi bản dựng khi đo** (ảnh đối tác: `HTPLDN · V1.0.2`, 2026-07-31 08:47). Trùng khít bản dựng cũ ⇒ báo điều phối
   trước khi chốt, nhưng **vẫn đo thật**.
4. **Chỉ có 2 vế được chấm ngay:** C1 · C2 · C3a · C4 · C5 (**TEST**). C3b · C6 (**BA**) — ghi số đo, **không** ra
   verdict, **không** log bug theo 2 vế đó.
5. **Nhánh đo an toàn = “Tạm dừng”** (bản ghi mẫu có 3 TVV liên kết ⇒ Vô hiệu hóa bị chặn hợp lệ).
6. **Hoàn nguyên:** nếu đã đưa bản ghi sang *Tạm dừng*, đưa lại *Đang hoạt động* qua chính chức năng “Kích hoạt lại”
   (`:2393`) và tải lại trang xác nhận; dòng nhật ký ở tab “Lịch sử” **sẽ còn lưu** — đúng `:1731`, **không phải lỗi**.
