# QLDMTCTV_02 — Bảng đối chiếu điều kiện + Cổng 3 (SRS vs web)

**Mã TC:** QLDMTCTV_02 · **Dòng sheet:** 317 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **Môi trường:** https://18.143.165.120.nip.io (bản dựng ở chân menu: `HTPLDN · V1.0.5`)
**Cột P (`Trạng thái dev fix 1`):** `dev done` — dev tự điền, là CLAIM chứ không phải bằng chứng · **Cột R:** rỗng tại thời điểm QA verify
**Phản ánh đối tác:** "Thiếu ô chọn và trường STT" — màn *Mạng lưới Tư vấn viên → Tổ chức tư vấn*

> Bảng dưới đây là **bảng đối chiếu điều kiện duy nhất** trong file (script `sheet_write.py` đọc mọi bảng markdown trong file này).
> Bảng Cổng 3 dạng lưới đầy đủ đặt ở `reverify-audit/QLDMTCTV_02.md` §2 và §3; ở đây trình bày dạng gạch đầu dòng.

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES)

- File: `partner-evidence/QLDMTCTV_02.jpg` — đã mở đọc bằng tool Read, không kết luận từ mô tả text.
- **3 dữ kiện neo (viết ra trước khi hình thành giả thuyết):**
  - (a) URL/bản ghi: `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/to-chuc`; 5 dòng hiện trên khung nhìn — `TC-STP-HN-0001`, `TC-BTP-TW-0008`, `TC-BTP-TW-0007`, `TC-BTP-TW-0005`, `TC-BTP-TW-0004`.
  - (b) Trạng thái entity đối tác đang đứng: thẻ **"Đang hoạt động"** đang chọn; thanh thẻ của đối tác có 6 mục (Đang hoạt động · Chờ phê duyệt · Mới đăng ký · Đã từ chối · Tạm dừng · Vô hiệu hóa).
  - (c) Dữ liệu tiền đề: bảng CÓ dữ liệu; góc phải trên ghi vai trò **"Quản trị viên · QTHT"**, phạm vi **BTP · TW**; đồng hồ máy đối tác **2026-07-28 08:54**.
- **Khoảnh khắc lỗi trong ảnh:** hàng tiêu đề bảng bắt đầu thẳng bằng `Mã tổ chức` — **không có ô tích chọn và không có cột STT**. Đúng như phản ánh.

## Cổng 2 — Hiểu bug

- Đối tác phản ánh CỤ THỂ 2 thành phần thiếu: (1) ô chọn dòng, (2) cột số thứ tự.
- Dữ liệu + bước tái hiện: đăng nhập → menu *Mạng lưới Tư vấn viên* → *Tổ chức tư vấn* → đọc hàng tiêu đề bảng ở thẻ mặc định "Đang hoạt động" (bảng phải có ≥1 dòng mới đo được cột).

---

## 🔴 Bảng đối chiếu điều kiện (0 GAP mới được chốt verdict)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Quản trị viên — vai trò `QTHT`, phạm vi `BTP · TW` | Đã test 3 vai trò, cùng cho một hàng tiêu đề bảng: `cbnv_tw_04` (CB Nghiệp vụ TW — vai trò ra verdict); `admin`/`QTHT` `BTP · TW` (đúng vai trò + đúng phạm vi của đối tác, chạy trong phiên trình duyệt cách ly, chỉ để đối chứng điều kiện, không dùng ra verdict); `cbpd_tw_04` (CB Phê duyệt TW — để mở được thẻ "Chờ phê duyệt") | Không |
| Entity + trạng thái (state machine) | `TO_CHUC_TU_VAN` — thẻ "Đang hoạt động" (trạng thái Đang hoạt động) | Đã đọc hàng tiêu đề ở cả 6 thẻ; 3 thẻ có dữ liệu thật: "Đang hoạt động" (3 dòng), "Mới đăng ký" (1 dòng QA tự seed), "Chờ phê duyệt" (1 dòng QA tự đẩy trạng thái); 3 thẻ còn lại rỗng nhưng vẫn đọc được hàng tiêu đề. Trạng thái của đối tác nằm trong tập đã test | Không |
| Dữ liệu tiền đề (bảng phải có ≥1 dòng thì mới đo được cột) | Bảng có dữ liệu — ≥5 tổ chức | Thẻ "Đang hoạt động" có sẵn 3 tổ chức (`TC-STP-AG-0001`, `TCTV-SEED-0001`, `TC-TW-DEMO-001`). Các thẻ khác rỗng nên QA TỰ SEED 1 tổ chức mới `TC-BTP-TW-0001` ("Trung tam Tu van QA Kiem Cot Bang 0803") qua giao diện rồi tự Trình phê duyệt để có dữ liệu ở thẻ "Mới đăng ký" và "Chờ phê duyệt" — không lấy "thiếu dữ liệu" làm lý do bỏ qua | Không |
| Input / filter / giá trị nhập | Không đặt bộ lọc nào (4 ô lọc đều trống), thẻ mặc định | Không đặt bộ lọc nào, thẻ mặc định "Đang hoạt động", sau đó lần lượt đổi thẻ. Có tải lại trang bỏ qua bộ nhớ đệm (hard reload) rồi đo lại để chắc chắn không chạy mã cũ còn giữ trong tab | Không |

**Kết luận điều kiện: 0 GAP → đủ điều kiện chốt verdict.**

---

## Cổng 3 — SRS yêu cầu (dẫn dòng) vs thực tế web

**Nguồn SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` — bản chốt duy nhất, đã mở file đọc từng dòng, không lấy số dòng từ trí nhớ.

- `SCR-IV-NEW-01: Danh sách Tổ chức tư vấn` — **dòng 1608**; đường dẫn `/chuyen-gia-tvv/to-chuc` — **dòng 1612**.
- FR gốc `FR-IV-NEW-01: Quản lý Tổ chức tư vấn` — **dòng 1027**; **dòng 1029** ghi `**UC Reference:** (chưa có trong CSV — gắn [GAP-IV-07])` → **FR này KHÔNG có mã UC trong SRS**, cấm bịa mã UC trong note gửi đối tác.

### Đối chiếu ĐỦ/THIẾU từng cột của bảng

Đo bằng `innerText` của từng `<th>` (KHÔNG dùng `textContent`) + đọc `outerHTML` thô của `<thead>` để tự kiểm selector, đối chứng bằng ảnh full-res đã mở đọc.

- **Dòng 1637 — hàng 15 "Ô chọn" (checkbox, "Chọn nhiều dòng cho thao tác hàng loạt"):** ✅ **ĐỦ**. `<th class="ant-table-cell ant-table-selection-column">` chứa `input[type=checkbox] aria-label="Select all"`; mỗi dòng dữ liệu có đúng 1 checkbox riêng.
- **Dòng 1638 — hàng 16 "Số thứ tự" (cột, "Tự động đánh số theo trang"):** ✅ **ĐỦ**. `<th>` thứ 2 = `"STT"`; giá trị các dòng = 1, 2, 3 theo thứ tự trang.
- **Dòng 1639 — hàng 17 "Mã tổ chức", định dạng `TC-{Mã đơn vị}-{Số thứ tự}`:** ✅ ĐỦ — `"Mã tổ chức"`, giá trị `TC-STP-AG-0001`, `TC-BTP-TW-0001` đúng định dạng.
- **Dòng 1640 — hàng 18 "Tên tổ chức" (đường liên kết, đậm):** ✅ ĐỦ — hiển thị dạng liên kết bấm được, mở màn chi tiết.
- **Dòng 1641 — hàng 19 "Loại hình" (nhãn tiếng Việt):** ✅ ĐỦ — "Công ty Luật", "Trung tâm Tư vấn Pháp luật".
- **Dòng 1642 — hàng 20 "Người đại diện":** ✅ ĐỦ.
- **Dòng 1643 — hàng 21 "Lĩnh vực" (tags, tối đa 3 thẻ + "+N"):** ✅ ĐỦ — hiển thị dạng thẻ ("Thương mại"); dòng không có lĩnh vực hiển thị "—".
- **Dòng 1644 — hàng 22 "Trạng thái" (badge):** ✅ ĐỦ — badge xanh "Đang hoạt động", vàng "Chờ phê duyệt".
- **Dòng 1645 — hàng 23 "Công khai" (toggle, nhãn "Đã công khai"/"Chưa công khai", bấm → mở hộp thoại công khai):** ⚠️ **CÓ CỘT nhưng LỆCH**. Web render thẻ tĩnh `<span class="ant-tag">`, nhãn "Công khai" / "Riêng tư", `cursor:auto`, không có `.ant-switch`/`button`, bấm không mở hộp thoại. *Ngoài phạm vi phản ánh của đối tác — ghi nhận ở §Ngoài phạm vi.*
- **Dòng 1646 — hàng 24 "Hành động" (2 icon + dropdown "..."):** ⚠️ **CÓ CỘT nhưng LỆCH cách bố trí**. CB Nghiệp vụ: 3 icon Xem/Sửa/Xóa, không có dropdown "..."; "Trình phê duyệt" nằm ở màn chi tiết (đã dùng được, đổi trạng thái thành công). CB Phê duyệt: 3 icon Xem/Duyệt/Từ chối. QTHT: chỉ icon Xem.
- **Không có trong danh sách cột của SRS:** web có **thêm** cột `"Đơn vị quản lý"`. SRS chỉ liệt kê "Đơn vị quản lý" ở hàng 12 (**dòng 1634**) như một **bộ lọc**. ➕ Thừa so với đặc tả.

### Đối chiếu 2 chức năng thao tác hàng loạt (phụ thuộc ô chọn)

- **Dòng 1647 — nút "Công khai" / "Hủy công khai" (thẻ "Đang hoạt động", hiện khi chọn ≥1 dòng):** ✅ **ĐỦ**. Tích ô chọn tất cả (3 dòng) → hiện thanh "Đã chọn 3 tổ chức tư vấn" + 2 nút **[Công khai] [Hủy công khai]** + [Bỏ chọn].
- **Dòng 1648 — nút "Phê duyệt hàng loạt" (thẻ "Chờ phê duyệt", vai trò Cán bộ Phê duyệt cùng đơn vị):** ✅ **ĐỦ**. Đăng nhập `cbpd_tw_04` → thẻ "Chờ phê duyệt" (1 dòng) → tích ô chọn → hiện "Đã chọn 1 tổ chức tư vấn" + nút **[Phê duyệt hàng loạt]** + [Bỏ chọn].

### Đối chiếu số thẻ trạng thái

- **Dòng 1610** — "Danh sách 6 tab": ✅ web có 6 thẻ.
- **Dòng 1628** — thẻ "Chờ phê duyệt": *"Hiển thị khi vai trò là Cán bộ Phê duyệt"*: ✅ ĐÚNG. `cbnv_tw_04` và `admin/QTHT` thấy 5 thẻ (không có "Chờ phê duyệt"); `cbpd_tw_04` thấy 6 thẻ có "Chờ phê duyệt".
  Ảnh của đối tác (28/07) cho thấy vai trò Quản trị viên vẫn nhìn thấy thẻ "Chờ phê duyệt"; bản hiện tại đã ẩn thẻ này với vai trò không phải Cán bộ Phê duyệt — **hướng thay đổi khớp SRS dòng 1628**, không phải thiếu chức năng.

---

## Kết luận

- **Đúng 2 thành phần đối tác phản ánh — "Ô chọn" (dòng 1637) và "Số thứ tự" (dòng 1638) — nay ĐỀU CÓ trên web**, xác nhận bằng 2 phương pháp độc lập cho kết quả trùng nhau:
  1. đọc thô cây DOM: 11 `<th>`, `<th>`#0 là cột ô chọn có `input[type=checkbox]`, `<th>`#1 = "STT", mỗi dòng 1 checkbox, STT = 1/2/3;
  2. ảnh chụp full-res đã mở ra đọc — nhìn thấy rõ ô tích và cột STT.
- 8 cột dữ liệu còn lại theo SRS đều hiện đủ; 2 chức năng hàng loạt phụ thuộc ô chọn (dòng 1647, 1648) đều hoạt động.
- Không thấy tràn chữ / đè chữ; ngôn ngữ hiển thị thống nhất tiếng Việt.
- **⇒ Verdict: `Pass`** (cột Q — Verify). Cột P giữ nguyên `dev done`, KHÔNG đụng tới.

## Ngoài phạm vi case (chưa log — chờ user quyết mở dòng TC mới)

1. Cột "Công khai" không phải toggle bấm được, nhãn "Công khai"/"Riêng tư" thay vì "Đã công khai"/"Chưa công khai" (SRS dòng 1645). Chức năng công khai vẫn làm được qua nút hàng loạt nên không chặn nghiệp vụ.
2. Cột "Đơn vị quản lý" xuất hiện trong bảng dù SRS chỉ liệt kê nó như một bộ lọc (dòng 1634).
3. Cột "Hành động" không có dropdown "..." như SRS dòng 1646 mô tả; "Trình phê duyệt" đặt ở màn chi tiết (vẫn dùng được — đã tự chạy thành công).

## Ghi chú đo lường (chống lặp lại lỗi 16/07)

- Bộ bắt thông báo: dùng đúng `tools/toast-capture.js`, không lọc trùng, đọc bằng `innerText`; tự kiểm `soObserverDangSong = 1` trước cả 2 lần đo.
- Thao tác đổi trạng thái đo kèm số request: tạo tổ chức → 1 request `POST /api/v1/to-chuc-tu-vans` / 1 khung thông báo "Tạo Tổ chức tư vấn thành công"; trình phê duyệt → 1 request `POST .../trinh-phe-duyet` / 1 khung thông báo "Đã trình phê duyệt". Không có thông báo lặp.
- Một lần đo bằng script cho kết quả "bấm Trình phê duyệt không có gì xảy ra"; kiểm lại bằng cây trợ năng thì hộp thoại xác nhận VẪN mở bình thường → nguyên nhân là selector của QA sai, không phải lỗi ứng dụng. Không log.
