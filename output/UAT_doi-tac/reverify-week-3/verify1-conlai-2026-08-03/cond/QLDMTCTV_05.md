# QLDMTCTV_05 — Bảng đối chiếu điều kiện + Cổng 3 (SRS vs web)

**Mã TC:** QLDMTCTV_05 · **Dòng sheet:** 318 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **Môi trường:** https://18.143.165.120.nip.io (bản dựng ở chân menu: `HTPLDN · V1.0.5`)
**Cột P (`Trạng thái dev fix 1`):** `dev done` — dev tự điền, là CLAIM chứ không phải bằng chứng · **Cột R:** rỗng tại thời điểm QA verify
**Phản ánh đối tác:** "Chọn thẻ trạng thái" — màn *Mạng lưới Tư vấn viên → Tổ chức tư vấn*. Case gộp **3 ý**: (a) thẻ không có số đếm · (b) thẻ "Mới đăng ký" không có nhãn đỏ · (c) thẻ "Chờ phê duyệt" hiện với Cán bộ Nghiệp vụ.

> Bảng dưới đây là **bảng đối chiếu điều kiện duy nhất** trong file (script `sheet_write.py` đọc mọi bảng markdown trong file này).
> Phần Cổng 3 trình bày dạng gạch đầu dòng; lưới đối chiếu đầy đủ đặt ở `reverify-audit/QLDMTCTV_05.md`.

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES)

- File: `partner-evidence/QLDMTCTV_05.jpg` — đã mở đọc bằng tool Read ở độ phân giải gốc 1921×1041, đồng thời phóng to riêng vùng thanh thẻ và vùng góc phải trên (×3) để đọc chắc chữ, không kết luận từ ảnh thu nhỏ.
- **3 dữ kiện neo (viết ra trước khi hình thành giả thuyết):**
  - (a) URL/bản ghi: `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/to-chuc?trangThai=MOI_DANG_KY&page=1`; đúng 1 dòng `TC-BTP-TW-0009` — "TKM", loại hình "Khác", đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp".
  - (b) Trạng thái entity đối tác đang đứng: thẻ **"Mới đăng ký"** đang được chọn, và thẻ này **có 1 bản ghi** — tức tiền đề "tồn tại tổ chức chưa trình phê duyệt" của ý (b) **có thật** trong ảnh.
  - (c) Dữ liệu tiền đề: góc phải trên ghi **"Cán bộ NV Trung ương · CB_NV_TW"**, phạm vi **BTP · TW**; đồng hồ máy đối tác **2026-07-28 09:00**.
- **🔴 Vai trò đọc được trong ảnh = Cán bộ Nghiệp vụ Trung ương (CB_NV_TW)** — KHÔNG phải Quản trị hệ thống. Giả thuyết "ảnh chụp ở vai trò QTHT nên ý (c) so sai vai trò" (quan sát từ case QLDMTCTV_02 kề bên) **KHÔNG áp dụng cho case này**: đối tác chụp đúng vai trò mà họ phản ánh, nên ý (c) là so sánh hợp lệ.
- **Khoảnh khắc lỗi trong ảnh:** thanh thẻ có đủ 6 mục và **không mục nào có số đếm**; thẻ "Mới đăng ký" **không có dấu đỏ** dù đang có 1 bản ghi; thẻ **"Chờ phê duyệt" vẫn hiện** trong khi vai trò đăng nhập là Cán bộ Nghiệp vụ. Cả 3 ý đối tác nêu đều nhìn thấy được trong đúng 1 ảnh này.

## Cổng 2 — Hiểu bug

- Đối tác phản ánh CỤ THỂ 3 thành phần: (1) số đếm bản ghi trên từng thẻ, (2) dấu đỏ trên thẻ "Mới đăng ký" khi còn tổ chức chưa trình phê duyệt, (3) thẻ "Chờ phê duyệt" lẽ ra chỉ dành cho Cán bộ Phê duyệt.
- Dữ liệu + bước tái hiện: đăng nhập → menu *Mạng lưới Tư vấn viên* → *Tổ chức tư vấn* → đọc thanh thẻ. Ý (b) chỉ đo được khi thẻ "Mới đăng ký" **có ≥1 bản ghi chưa trình phê duyệt**; ý (c) chỉ kết luận được khi so **2 vai trò** Cán bộ Nghiệp vụ và Cán bộ Phê duyệt cùng cấp cùng đơn vị.

---

## 🔴 Bảng đối chiếu điều kiện (0 GAP mới được chốt verdict)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương — vai trò `CB_NV_TW`, phạm vi `BTP · TW` (đọc được ở góc phải trên ảnh) | `cbnv_tw_04` (CB Nghiệp vụ TW, `BTP · TW`) — **trùng khớp tuyệt đối vai trò + cấp + đơn vị của đối tác**, đây là vai trò ra verdict; đối chiếu thêm `cbpd_tw_04` (CB Phê duyệt TW, cùng đơn vị) vì ý (c) bắt buộc so 2 vai trò. Mỗi vai trò chạy trong một phiên trình duyệt cách ly riêng (kho cookie/bộ nhớ tách hẳn) nên không có chuyện dính phiên cũ | Không |
| Entity + trạng thái (state machine) | `TO_CHUC_TU_VAN` — thẻ "Mới đăng ký" đang chọn, chứa 1 tổ chức ở trạng thái Mới đăng ký (chưa trình phê duyệt) | Đã đo cả 6 thẻ. Trạng thái của đối tác ("Mới đăng ký", có bản ghi) nằm trong tập đã test: sau khi seed thì thẻ này có đúng 1 bản ghi `TC-BTP-TW-0002` ở trạng thái "Mới đăng ký"; ngoài ra "Đang hoạt động" 3 bản ghi, "Chờ phê duyệt" 1 bản ghi `TC-BTP-TW-0001`; 3 thẻ còn lại rỗng | Không |
| Dữ liệu tiền đề (thẻ "Mới đăng ký" phải có ≥1 tổ chức CHƯA trình phê duyệt thì mới đo được dấu đỏ) | Có — 1 tổ chức `TC-BTP-TW-0009` nằm ở thẻ "Mới đăng ký" | Đầu phiên thẻ "Mới đăng ký" **RỖNG** → ý (b) mất tiền đề. Đã **TỰ SEED** qua giao diện bằng chính `cbnv_tw_04`: tạo `TC-BTP-TW-0002` ("Trung tam Tu van QA Kiem Cham Do 0803") và **CỐ Ý KHÔNG trình phê duyệt** để giữ đúng trạng thái "Mới đăng ký" như đối tác. Không lấy "thẻ rỗng" làm lý do bỏ qua | Không |
| Input / filter / giá trị nhập | Không đặt bộ lọc nào (4 ô lọc đều trống); thẻ "Mới đăng ký" đang chọn | Không đặt bộ lọc nào. Đã bấm lần lượt từng thẻ và đối chiếu cột Trạng thái của các dòng hiện ra. Sau khi seed có **tải lại trang bỏ qua bộ nhớ đệm (hard reload)** rồi mới đo lại số đếm và dấu đỏ, tránh đọc phải mã cũ còn giữ trong tab | Không |

**Kết luận điều kiện: 0 GAP → đủ điều kiện chốt verdict.**

---

## Cổng 3 — SRS yêu cầu (dẫn dòng) vs thực tế web

**Nguồn SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` — bản chốt duy nhất, đã mở file đọc từng dòng, không lấy số dòng từ trí nhớ.

- `SCR-IV-NEW-01: Danh sách Tổ chức tư vấn` — **dòng 1608**; đường dẫn `/chuyen-gia-tvv/to-chuc` — **dòng 1612**.
- FR gốc `FR-IV-NEW-01: Quản lý Tổ chức tư vấn` — **dòng 1027**; **dòng 1029** ghi `**UC Reference:** (chưa có trong CSV — gắn [GAP-IV-07])` → **FR này KHÔNG có mã UC trong SRS**, cấm bịa mã UC trong note gửi đối tác.

### Ý (a) — số đếm trên từng thẻ

- **Dòng 1610** "Loại màn hình: Danh sách **6 tab**…" và **dòng 1617** "Hiển thị 6 tab phân loại theo trạng thái lifecycle": ✅ khớp — Cán bộ Phê duyệt thấy đủ 6 thẻ.
- **Dòng 1625 / 1626 / 1627 / 1628 / 1629 / 1630** — cả 6 thẻ đều ghi loại UI **"tab + số đếm"**; **dòng 1650** (phân trang) ghi "20 mục/trang; **hiển thị tổng mỗi tab**".
- ✅ **ĐỦ.** Web hiện số đếm ngay trên thẻ và **số đếm ĐÚNG với số bản ghi thực**, đo bằng 2 phương pháp trùng nhau (đọc thô cây DOM + ảnh full-res đã mở đọc): "Đang hoạt động" = 3 (bảng 3 dòng) · "Mới đăng ký" = 1 (bảng 1 dòng) · "Chờ phê duyệt" = 1 (bảng 1 dòng).
- Phép thử phân biệt (chứng minh số đếm là động, không phải chữ chết): trước khi seed thẻ "Mới đăng ký" **không có số đếm** và bảng **0 dòng**; sau khi seed 1 tổ chức + tải lại trang thì thẻ hiện **"1"** và bảng **1 dòng**.
- ⚠️ Sai lệch nhỏ, KHÔNG thuộc phản ánh của đối tác: thẻ có **0 bản ghi thì không hiện số đếm** (không hiện số "0"). 3 thẻ "Đã từ chối" / "Tạm dừng" / "Vô hiệu hóa" đang rỗng nên trống trơn. Đây là quy ước hiển thị phổ biến (ẩn huy hiệu khi bằng 0), và khác hẳn triệu chứng đối tác báo (thẻ **có dữ liệu** mà vẫn không có số). Ghi nhận ở §Ngoài phạm vi.

### Ý (b) — dấu đỏ trên thẻ "Mới đăng ký"

- **Dòng 1627** — thẻ "Mới đăng ký", loại UI **"tab + số đếm + chấm đỏ nếu >0"**, nhãn "Tổ chức tư vấn mới do Cán bộ Nghiệp vụ tạo, chưa trình phê duyệt".
- ✅ **ĐỦ.** Sau khi seed 1 tổ chức chưa trình phê duyệt và tải lại trang, thẻ "Mới đăng ký" hiện huy hiệu số đếm **"1" trên nền ĐỎ** (`rgb(245, 34, 45)`), trong khi thẻ "Đang hoạt động" cùng lúc hiện "3" trên nền **xanh** (`rgb(9, 88, 217)`). Tức dấu hiệu đỏ chỉ bật đúng cho thẻ "Mới đăng ký" khi số lượng > 0.
- Phép thử phân biệt: khi thẻ này **= 0** thì không có huy hiệu nào (không đỏ); khi **> 0** thì huy hiệu chuyển đỏ. Đúng điều kiện "nếu > 0" của dòng 1627.
- Ghi chú cách hiện thực: dấu đỏ được gộp vào chính huy hiệu số đếm (một huy hiệu nền đỏ mang số) thay vì vẽ thêm một chấm tròn riêng. Yêu cầu của dòng 1627 gồm 2 phần — có số đếm và có dấu đỏ khi > 0 — **cả 2 đều đang được đáp ứng**, chỉ khác cách trình bày. Triệu chứng đối tác báo ("không có nhãn đỏ mặc dù tồn tại tổ chức chưa trình duyệt") **không còn tái hiện**.

### Ý (c) — thẻ "Chờ phê duyệt" hiện với Cán bộ Nghiệp vụ

- **Dòng 1628** — thẻ "Chờ phê duyệt", cột "Label / Dữ liệu hiển thị" ghi *"Hiển thị khi vai trò là Cán bộ Phê duyệt"*; **dòng 1615** (Quyền truy cập) ghi *"Cán bộ Phê duyệt cùng đơn vị: xem + phê duyệt/từ chối tab 'Chờ phê duyệt'"*.
- ✅ **ĐỦ.** Đo trên 2 vai trò cùng cấp cùng đơn vị, 2 phiên trình duyệt cách ly: `cbnv_tw_04` thấy **5 thẻ**, **KHÔNG** có "Chờ phê duyệt"; `cbpd_tw_04` thấy **6 thẻ**, **CÓ** "Chờ phê duyệt" kèm số đếm 1 và bấm vào lọc ra đúng `TC-BTP-TW-0001` trạng thái "Chờ phê duyệt".
- Triệu chứng đối tác báo (thẻ "Chờ phê duyệt" hiện với Cán bộ Nghiệp vụ) **không còn tái hiện** trên bản dựng hiện tại; hướng thay đổi khớp dòng 1628 + 1615.

### Lọc theo thẻ (phần "Hệ thống lọc danh sách theo trạng thái tương ứng" trong Kết quả mong đợi)

- ✅ **ĐỦ** cho cả 6 thẻ. Mỗi lần bấm thẻ, địa chỉ trang đổi thành `?trangThai=<mã trạng thái>` và bảng chỉ còn các dòng đúng trạng thái đó: "Đang hoạt động" → 3 dòng đều "Đang hoạt động"; "Mới đăng ký" → `TC-BTP-TW-0002` "Mới đăng ký"; "Chờ phê duyệt" → `TC-BTP-TW-0001` "Chờ phê duyệt"; "Đã từ chối" / "Tạm dừng" / "Vô hiệu hóa" → không có dòng nào (đúng, vì không có bản ghi ở các trạng thái này).

### 🔴 Mâu thuẫn nội tại của SRS (nêu để BA biết, không dùng để chấm case)

- **Dòng 1610 / 1617 / 1625-1630** (phần đặc tả màn hình SCR-IV-NEW-01) mô tả **6 tab** trạng thái.
- **Dòng 1129** (Acceptance Criteria của FR-IV-NEW-01) lại ghi: *"**Then** danh sách TC TV thuộc đơn vị, **3 tab** trạng thái"*.
- Hai chỗ trong cùng một tài liệu vênh nhau về số lượng thẻ. Web đang làm theo phần đặc tả màn hình (6 thẻ, ẩn bớt 1 thẻ theo vai trò). Việc này **không làm đổi verdict** của 3 ý trên (cả 3 ý đều đo theo mô tả chi tiết từng thẻ ở dòng 1625-1630), nhưng nên để BA chốt lại con số cho khỏi lệch tài liệu.

---

## Kết luận

- **Cả 3 ý đối tác phản ánh đều KHÔNG còn tái hiện** trên bản dựng hiện tại `HTPLDN · V1.0.5`, kiểm ở đúng vai trò `CB_NV_TW` + đúng đơn vị `BTP · TW` như ảnh đối tác:
  - **(a) số đếm trên thẻ → `Pass`** — có số đếm, và số đếm khớp số bản ghi thực (3 / 1 / 1).
  - **(b) dấu đỏ thẻ "Mới đăng ký" → `Pass`** — sau khi tự seed 1 tổ chức chưa trình phê duyệt, huy hiệu chuyển **nền đỏ** đúng điều kiện "> 0" (dòng 1627).
  - **(c) thẻ "Chờ phê duyệt" hiện với Cán bộ Nghiệp vụ → `Pass`** — nay chỉ Cán bộ Phê duyệt thấy thẻ này (5 thẻ vs 6 thẻ), khớp dòng 1628 + 1615.
- Mỗi kết luận dựa trên 2 phương pháp độc lập cho kết quả trùng nhau: đọc thô cây DOM (kể cả mã HTML gốc của thanh thẻ + màu nền huy hiệu) và ảnh chụp full-res **đã mở ra đọc**.
- Không có lỗi trong bảng điều khiển trình duyệt; các lệnh gọi máy chủ đều 200/304.
- **⇒ Verdict tổng: `Pass`** (cột Q — Verify). Cột P giữ nguyên `dev done`, KHÔNG đụng tới.

## Ngoài phạm vi case (chưa log — chờ user quyết)

1. **Thẻ "Chờ phê duyệt" không chuyển đỏ khi > 0.** Dòng 1628 quy định thẻ này cũng là "tab + số đếm + **chấm đỏ nếu >0**", nhưng với `cbpd_tw_04` thẻ đang có 1 bản ghi mà huy hiệu vẫn **nền xanh** (`rgb(9, 88, 217)`), chỉ thẻ "Mới đăng ký" mới đỏ. Đây là thẻ khác với thẻ đối tác phản ánh nên không tính vào case này.
2. **Thẻ rỗng không hiện số "0"** (xem ý (a)) — dòng 1650 ghi "hiển thị tổng mỗi tab".
3. **Thứ tự thẻ khác SRS.** SRS dòng 1625-1630 xếp: Đang hoạt động → Tạm dừng → Mới đăng ký → Chờ phê duyệt → Đã từ chối → Vô hiệu hóa. Web xếp: Đang hoạt động → Chờ phê duyệt → Mới đăng ký → Đã từ chối → Tạm dừng → Vô hiệu hóa.
4. **Chữ ở màn hình rỗng là "Trống"**, trong khi dòng 1649 mô tả trạng thái rỗng phải là "Chưa có tổ chức tư vấn nào trong mục này" + nút "+ Thêm tổ chức tư vấn" (chỉ ở thẻ Mới đăng ký).

## Ghi chú đo lường (chống lặp lại lỗi 16/07)

- Bộ bắt thông báo: dùng đúng `tools/toast-capture.js`, không lọc trùng, đọc bằng `innerText`; đã tự kiểm `soObserverDangSong = 1` trước khi tin số liệu.
- Thao tác đổi trạng thái (seed) đo kèm số request: tạo tổ chức → **1 request** `POST /api/v1/to-chuc-tu-vans` / **1 khung thông báo** "Tạo Tổ chức tư vấn thành công". Không có thông báo lặp.
- Mọi bước seed đều có ảnh và ảnh **đã được mở ra đọc**, không chỉ lưu.
- Một lần đo bằng script cho kết quả ô "Loại hình" **rỗng** sau khi đã chọn; kiểm lại bằng mã HTML gốc của ô thì giá trị "Trung tâm Tư vấn Pháp luật" **vẫn nằm đúng chỗ** (ứng dụng dùng lớp CSS riêng `.ant-select-content-value`, không phải lớp mặc định mà script tra). Nguyên nhân là **selector của QA sai, không phải lỗi ứng dụng** → không log.
